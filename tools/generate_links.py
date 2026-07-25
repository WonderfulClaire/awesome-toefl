#!/usr/bin/env python3
"""generate_links.py —— 为 ai-toolkit.md 的每条提示词生成「一键发给 ChatGPT」链接。

原理：ChatGPT 网页版支持 `https://chatgpt.com/?q=<提示词>` URL 参数，
打开后提示词自动填入输入框（不会自动发送，可先替换 {占位符} 再回车）。

维护者用法：修改 ai-toolkit.md 里的提示词后运行本脚本即可刷新全部链接（幂等）：
    python tools/generate_links.py
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

LINK_MARK = "🚀"


def make_link(prompt: str) -> str:
    url = "https://chatgpt.com/?q=" + urllib.parse.quote(prompt.strip())
    return f"{LINK_MARK} [一键发给 ChatGPT]({url})\n"


def refresh(md_path: Path) -> int:
    text = md_path.read_text(encoding="utf-8")
    # 幂等：先移除旧的直开链接行
    text = re.sub(rf"^{LINK_MARK} \[一键发给 ChatGPT\]\(\S+\)\n\n?", "", text, flags=re.M)

    count = 0

    def insert_link(match: re.Match) -> str:
        nonlocal count
        count += 1
        return match.group(0) + "\n" + make_link(match.group(1))

    # 每个 ```text 代码块（提示词）后插入一行链接
    text = re.sub(r"```text\n(.*?)```\n", insert_link, text, flags=re.S)
    md_path.write_text(text, encoding="utf-8")
    return count


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    hits = sorted(repo_root.glob("docs/*/ai-toolkit.md"))
    if not hits:
        sys.exit("找不到 docs/*/ai-toolkit.md")
    for md_path in hits:
        count = refresh(md_path)
        print(f"{md_path.relative_to(repo_root)}: 已生成 {count} 条直开链接")


if __name__ == "__main__":
    main()
