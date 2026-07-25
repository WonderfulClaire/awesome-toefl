#!/usr/bin/env python3
"""ai_coach.py —— 零依赖终端 AI 陪练工具。

把仓库 docs 里的 AI 提示词库直接接上你自己的大模型 API：
选一个训练模式即自动加载对应提示词，开场引导建「考生档案」，
内置错题账本（随时输入「复盘」查看错误模式汇总）。

用法：
    export AI_COACH_API_KEY="sk-..."      # Windows 用 setx AI_COACH_API_KEY "sk-..."
    python tools/ai_coach.py --provider deepseek

仅使用 Python 标准库（3.8+），无需 pip install。
兼容一切 OpenAI 格式接口：--base-url + --model 可接任意服务。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# 供应商预设（全部为 OpenAI 兼容接口）
# ---------------------------------------------------------------------------

PROVIDERS = {
    "deepseek": ("https://api.deepseek.com/v1", "deepseek-chat"),
    "kimi": ("https://api.moonshot.cn/v1", "kimi-latest"),
    "qwen": ("https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    "glm": ("https://open.bigmodel.cn/api/paas/v4", "glm-4-flash"),
    "openai": ("https://api.openai.com/v1", "gpt-4o-mini"),
}

ENV_KEY = "AI_COACH_API_KEY"

# ---------------------------------------------------------------------------
# 从 docs 里的 ai-toolkit.md 解析提示词库（文档即数据，永不失同步）
# ---------------------------------------------------------------------------


def find_toolkit_md() -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    hits = sorted(repo_root.glob("docs/*/ai-toolkit.md"))
    if not hits:
        sys.exit("找不到 docs/*/ai-toolkit.md，请在仓库目录内运行本脚本。")
    return hits[0]


def parse_toolkit(md_path: Path):
    """返回 (考试名, 考生档案模板, [(编号, 标题, 提示词), ...])。"""
    text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+\S*\s*(.+)$", text, re.M)
    exam_name = title_match.group(1).strip() if title_match else "备考"

    profile_template = ""
    profile_section = re.search(
        r"##\s+第 0 步[^\n]*\n(?:.*?)```text\n(.*?)```", text, re.S
    )
    if profile_section:
        profile_template = profile_section.group(1).strip()

    modes = []
    for match in re.finditer(
        r"###\s+(\d+)\.\s+([^\n]+)\n+```text\n(.*?)```", text, re.S
    ):
        number, heading, prompt = match.groups()
        heading = re.sub(r"（[^）]*）", "", heading).strip()
        modes.append((int(number), heading, prompt.strip()))
    modes.sort(key=lambda item: item[0])
    return exam_name, profile_template, modes


# ---------------------------------------------------------------------------
# 考生档案：开场三问，生成 system prompt
# ---------------------------------------------------------------------------


def build_profile(exam_name: str, template: str) -> str:
    print("\n—— 先花 30 秒建考生档案（直接回车用默认值）——")
    goal = input("① 目标分数？ ").strip() or "尽量高"
    level = input("② 当前水平/最薄弱项？ ").strip() or "未评估，请先摸底"
    weeks = input("③ 距考试还有几周？每天能学几小时？ ").strip() or "时间充裕"
    profile = (
        f"你是{exam_name}的私人教练。\n"
        f"【考生档案】目标：{goal}；当前水平与弱项：{level}；备考时间：{weeks}。\n"
        "对话要求：出题难度贴近但略高于考生水平；批改和讲解直说问题、"
        "不要客套和夸奖；所有反馈先讲最伤分的那一条。\n"
        "错题账本：考生每答错一次，你就默默记下【题型｜错误原因】；"
        "当考生说「复盘」时，输出完整账本 + 归纳出的 2–3 个错误模式；"
        "账本为空时如实说明。\n"
        "考试政策类问题一律回答「请以 ETS 官网为准」，不要编造。"
    )
    if template:
        profile += "\n（档案格式参考，可在对话中随时补充：）\n" + template
    return profile


# ---------------------------------------------------------------------------
# OpenAI 兼容接口调用（标准库实现，支持流式输出）
# ---------------------------------------------------------------------------


def stream_chat(base_url: str, api_key: str, model: str, messages: list) -> str:
    request = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(
            {"model": model, "messages": messages, "stream": True}
        ).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    reply_parts = []
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            for raw_line in response:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if payload == "[DONE]":
                    break
                try:
                    delta = json.loads(payload)["choices"][0]["delta"]
                except (json.JSONDecodeError, LookupError):
                    continue
                piece = delta.get("content") or ""
                if piece:
                    reply_parts.append(piece)
                    print(piece, end="", flush=True)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")[:500]
        print(f"\n[请求失败 HTTP {error.code}] {body}")
        if error.code == 401:
            print(f"提示：检查环境变量 {ENV_KEY} 是否是该平台的有效 Key。")
        elif error.code == 404:
            print("提示：检查 --base-url / --model 是否正确。")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"\n[网络错误] {error}\n提示：检查网络，或换 --provider 再试。")
    print()
    return "".join(reply_parts)


# ---------------------------------------------------------------------------
# 交互
# ---------------------------------------------------------------------------


def choose_mode(modes) -> tuple:
    print("\n可选训练模式：")
    for number, heading, _ in modes:
        print(f"  {number:>2}. {heading}")
    print("   0. 自由对话（不加载提示词）")
    while True:
        choice = input("选择模式编号：").strip()
        if choice == "0":
            return (0, "自由对话", "")
        for mode in modes:
            if choice == str(mode[0]):
                return mode
        print("无效编号，请重试。")


def read_paste() -> str:
    print("进入多行粘贴模式：粘贴完毕后，单独一行输入 EOF 并回车。")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "EOF":
            break
        lines.append(line)
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # Windows 控制台中文/emoji

    parser = argparse.ArgumentParser(description="终端 AI 备考陪练")
    parser.add_argument("--provider", choices=sorted(PROVIDERS), default="deepseek")
    parser.add_argument("--base-url", help="自定义 OpenAI 兼容接口地址")
    parser.add_argument("--model", help="自定义模型名")
    parser.add_argument("--api-key", help=f"不推荐明文传入，优先用环境变量 {ENV_KEY}")
    parser.add_argument("--list", action="store_true", help="仅列出训练模式后退出")
    args = parser.parse_args()

    exam_name, profile_template, modes = parse_toolkit(find_toolkit_md())

    if args.list:
        for number, heading, _ in modes:
            print(f"{number:>2}. {heading}")
        return

    default_url, default_model = PROVIDERS[args.provider]
    base_url = args.base_url or default_url
    model = args.model or default_model
    api_key = args.api_key or os.environ.get(ENV_KEY, "")
    if not api_key:
        sys.exit(
            f"未找到 API Key。请先设置环境变量 {ENV_KEY}\n"
            f'  Windows:  setx {ENV_KEY} "sk-..."（设置后重开终端）\n'
            f'  macOS/Linux:  export {ENV_KEY}="sk-..."'
        )

    print(f"=== {exam_name} · AI 陪练 ===")
    print(f"接口：{base_url}   模型：{model}")
    print("命令：/paste 粘贴多行  /new 重开对话  /mode 换模式  /exit 退出  输入「复盘」看错题账本")

    system_prompt = build_profile(exam_name, profile_template)
    number, heading, mode_prompt = choose_mode(modes)
    messages = [{"role": "system", "content": system_prompt}]
    if mode_prompt:
        print(f"\n已加载模式：{heading}（提示词中的 {{占位符}} 请在对话里补充具体内容）")
        print("\nAI：", end="")
        messages.append({"role": "user", "content": mode_prompt})
        messages.append({"role": "assistant", "content": stream_chat(base_url, api_key, model, messages)})

    while True:
        try:
            user_input = input("\n你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见，记得复盘！")
            break
        if not user_input:
            continue
        if user_input == "/exit":
            print("再见，记得复盘！")
            break
        if user_input == "/new":
            messages = messages[:1]
            print("已重开对话（考生档案保留）。")
            continue
        if user_input == "/mode":
            number, heading, mode_prompt = choose_mode(modes)
            messages = messages[:1]
            if mode_prompt:
                print(f"已切换：{heading}")
                print("\nAI：", end="")
                messages.append({"role": "user", "content": mode_prompt})
                messages.append({"role": "assistant", "content": stream_chat(base_url, api_key, model, messages)})
            continue
        if user_input == "/paste":
            user_input = read_paste()
            if not user_input.strip():
                continue
        print("\nAI：", end="")
        messages.append({"role": "user", "content": user_input})
        reply = stream_chat(base_url, api_key, model, messages)
        if reply:
            messages.append({"role": "assistant", "content": reply})
        else:
            messages.pop()  # 请求失败，回滚这条输入


if __name__ == "__main__":
    main()
