#!/usr/bin/env python3
"""build_practice.py —— 把 bank/ 下的 Markdown 题库编译成 bank/data.js。

解析规则与 bank/ 内各 .md 的书写约定一一对应（详见各文件头部注释）。
生成的 bank/data.js 是纯 JSON 包在 `window.BANK = ...` 里，供 practice.html 直接 <script> 引入。

用法：
    python scripts/build_practice.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "bank"
OUT = BANK / "data.js"


# ---------------------------------------------------------------------------
# 通用工具
# ---------------------------------------------------------------------------


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def split_h2(text: str):
    """返回 [(标题, 正文), ...]，按 '## ' 切分（忽略 H1）。"""
    parts = re.split(r"^##\s+(.+)$", text, flags=re.M)
    # parts[0] 是 H1+前言；之后成对 (标题, 正文)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def split_h3(text: str):
    """返回 {小标题: 正文}，按 '### ' 切分。"""
    parts = re.split(r"^###\s+(.+)$", text, flags=re.M)
    out = {}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def bold_fields(text: str) -> dict:
    """提取 **键**：值 形式的字段。值到下一个 '**' 或 '###' 或 '##' 或结尾为止。
    键用 [^*]+ 精确截取，冒号兼容半角/全角，避免全角符号不匹配。"""
    out = {}
    for m in re.finditer(r"\*\*([^*]+)\*\*\s*[:：]\s*(.*?)(?=\n\*\*|\n###|\n##|\Z)", text, flags=re.S):
        key, val = m.group(1).strip(), m.group(2).strip()
        out[key] = val
    return out


def list_lines(text: str):
    """提取 '- ' 或 '1. ' 列表项，去掉前缀。"""
    items = []
    for line in text.splitlines():
        s = line.strip()
        m = re.match(r"^[-*]\s+(.*)$", s)
        if m:
            items.append(m.group(1).strip())
            continue
        m = re.match(r"^\d+[.、]\s+(.*)$", s)
        if m:
            items.append(m.group(1).strip())
    return [x for x in items if x]


def parse_phrase_line(line: str):
    """'短语 → 说明' 或 '短语 -> 说明'。"""
    m = re.split(r"\s*[→\-–>]\s+", line, maxsplit=1)
    if len(m) == 2:
        return {"p": m[0].strip(), "n": m[1].strip()}
    return {"p": line.strip(), "n": ""}


# ---------------------------------------------------------------------------
# 写作
# ---------------------------------------------------------------------------


def parse_writing_file(path: Path, kind: str):
    text = read(path)
    items = []
    for title, body in split_h2(text):
        if title.startswith("W-") or title.startswith("A-"):
            hid = title.split("·")[0].strip()
            htitle = title.split("·", 1)[1].strip() if "·" in title else title
            fields = bold_fields(body)
            subs = split_h3(body)
            requirements = list_lines(fields.get("要求", ""))
            req_single = fields.get("要求", "").strip()
            items.append({
                "id": hid,
                "title": htitle,
                "situation": fields.get("情境", ""),
                "requirements": requirements or ([req_single] if req_single else []),
                "time": fields.get("限时", ""),
                "difficulty": fields.get("难度", ""),
                "topic": fields.get("话题", ""),
                "model": subs.get("满分范文", "").strip(),
                "phrases": [parse_phrase_line(x) for x in list_lines(subs.get("高分短语", ""))],
                "structure": list_lines(subs.get("结构拆解", "")),
            })
    return items


# ---------------------------------------------------------------------------
# 口语
# ---------------------------------------------------------------------------


def parse_speaking_interview(path: Path):
    text = read(path)
    items = []
    for title, body in split_h2(text):
        if title.startswith("S-I"):
            hid = title.split("·")[0].strip()
            htitle = title.split("·", 1)[1].strip() if "·" in title else title
            fields = bold_fields(body)
            subs = split_h3(body)
            items.append({
                "id": hid,
                "title": htitle,
                "question": fields.get("问题", ""),
                "type": fields.get("类型", ""),
                "material": fields.get("可挂素材", ""),
                "time": fields.get("限时", ""),
                "model": subs.get("示范回答", "").strip(),
                "structure": list_lines(subs.get("应答结构", "")),
            })
    return items


def parse_speaking_repeat(path: Path):
    text = read(path)
    levels = []
    for title, body in split_h2(text):
        if title.startswith("Level"):
            sentences = []
            for line in body.splitlines():
                m = re.match(r"^\d+[.、]\s+(.*)$", line.strip())
                if m:
                    sentences.append(m.group(1).strip())
            levels.append({"level": title, "sentences": sentences})
    return levels


# ---------------------------------------------------------------------------
# 阅读 / 听力
# ---------------------------------------------------------------------------


def parse_rl_file(path: Path, kind: str):
    text = read(path)
    # 标题取 H1
    h1 = re.search(r"^#\s+(.+)$", text, flags=re.M)
    title = h1.group(1).strip() if h1 else path.stem
    # 题目区之前的正文（passage / transcript）
    pre = text.split("## 题目", 1)[0]
    pre_body = re.split(r"^#\s+.+$", pre, flags=re.M)[-1]
    pre_body = re.sub(r"^>.*$", "", pre_body, flags=re.M).strip()
    passage = pre_body

    questions = []
    qtext = text.split("## 题目", 1)[1] if "## 题目" in text else ""
    for qtitle, qbody in split_h3(qtext).items():
        if not qtitle.strip().startswith("Q"):
            continue
        fields = bold_fields(qbody)
        # 选项：'**选项**' 之后到 '**答案**' 之前的 A./B./... 行
        opts_block = ""
        m = re.search(r"\*\*选项\*\*[：:]?\s*(.*?)(?=\*\*答案\*\*)", qbody, flags=re.S)
        if m:
            opts_block = m.group(1)
        options = []
        for line in opts_block.splitlines():
            mm = re.match(r"^\s*([A-D])[.、]\s+(.*)$", line.strip())
            if mm:
                options.append({"key": mm.group(1), "text": mm.group(2).strip()})
        questions.append({
            "id": qtitle.strip(),
            "q": fields.get("题干", ""),
            "options": options,
            "answer": fields.get("答案", "").strip(),
            "explain": fields.get("解析", "").strip(),
        })
    return {"id": path.stem, "title": title, "passage": passage, "questions": questions}


# ---------------------------------------------------------------------------
# 语料库
# ---------------------------------------------------------------------------


def parse_phrases(path: Path):
    text = read(path)
    cats = []
    for title, body in split_h2(text):
        items = [parse_phrase_line(x) for x in list_lines(body)]
        if items:
            cats.append({"category": title, "items": items})
    return cats


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------


def main() -> None:
    data = {
        "writing": {
            "email": parse_writing_file(BANK / "writing" / "email.md", "email"),
            "academic": parse_writing_file(BANK / "writing" / "academic-discussion.md", "academic"),
        },
        "speaking": {
            "interview": parse_speaking_interview(BANK / "speaking" / "interview.md"),
            "repeat": parse_speaking_repeat(BANK / "speaking" / "repeat-sentences.md"),
        },
        "reading": [parse_rl_file(p, "reading") for p in sorted(BANK.glob("reading/*.md"))],
        "listening": [parse_rl_file(p, "listening") for p in sorted(BANK.glob("listening/*.md"))],
        "phrases": parse_phrases(BANK / "_phrases" / "phrases.md"),
    }

    counts = {
        "writing_email": len(data["writing"]["email"]),
        "writing_academic": len(data["writing"]["academic"]),
        "speaking_interview": len(data["speaking"]["interview"]),
        "speaking_repeat_levels": len(data["speaking"]["repeat"]),
        "speaking_repeat_sentences": sum(len(l["sentences"]) for l in data["speaking"]["repeat"]),
        "reading": len(data["reading"]),
        "listening": len(data["listening"]),
        "phrase_categories": len(data["phrases"]),
    }
    OUT.write_text("window.BANK = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    print("写入", OUT)
    print("题库统计：", json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
