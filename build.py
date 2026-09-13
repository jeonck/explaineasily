#!/usr/bin/env python3
"""마크다운 문서를 정적 HTML로 변환한다.

의존성 없이 동작한다. 이 저장소 문서가 실제로 쓰는 문법만 처리한다:
제목, 문단, 굵게, 인라인 코드, 링크, 표, 인용문, 목록, 코드블록.

사용법: python3 build.py
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

PAGES = [
    ("cti-ko", "ko", "CTI(사이버 위협 인텔리전스) 쉽게 이해하기"),
    ("cti-en", "en", "CTI (Cyber Threat Intelligence), Explained Simply"),
]

STYLE = """
:root {
  --bg: #fbfaf8; --fg: #24201c; --muted: #6b645c; --rule: #e2ddd6;
  --accent: #9a3b1f; --card: #ffffff; --code-bg: #f1eee9;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #191715; --fg: #e8e3dc; --muted: #9d958b; --rule: #35312c;
    --accent: #e08a63; --card: #201d1a; --code-bg: #262220;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Apple SD Gothic Neo",
    "Noto Sans KR", "Malgun Gothic", Segoe UI, sans-serif;
  font-size: 17px; line-height: 1.75;
  -webkit-text-size-adjust: 100%;
}
.wrap { max-width: 46rem; margin: 0 auto; padding: 3.5rem 1.25rem 6rem; }
h1 {
  font-size: 1.95rem; line-height: 1.3; letter-spacing: -0.02em;
  margin: 0 0 1.75rem; padding-bottom: 1.25rem; border-bottom: 2px solid var(--fg);
}
h2 {
  font-size: 1.3rem; letter-spacing: -0.01em;
  margin: 3.25rem 0 1rem; padding-top: 1.25rem; border-top: 1px solid var(--rule);
}
h3 { font-size: 1.05rem; margin: 2rem 0 .6rem; }
p { margin: 0 0 1.1rem; }
a { color: var(--accent); text-underline-offset: 3px; }
strong { font-weight: 650; }
blockquote {
  margin: 1.5rem 0; padding: .9rem 1.1rem; border-left: 3px solid var(--accent);
  background: var(--card); color: var(--muted); border-radius: 0 4px 4px 0;
}
blockquote p:last-child { margin: 0; }
code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  font-size: .86em; background: var(--code-bg); padding: .15em .4em; border-radius: 3px;
}
pre {
  background: var(--code-bg); padding: 1rem; border-radius: 6px;
  overflow-x: auto; margin: 1.5rem 0;
}
pre code { background: none; padding: 0; font-size: .85rem; line-height: 1.6; }
ul, ol { margin: 0 0 1.1rem; padding-left: 1.4rem; }
li { margin-bottom: .5rem; }
li > strong:first-child { color: var(--accent); }
.table-scroll { overflow-x: auto; margin: 1.5rem 0; }
table { border-collapse: collapse; width: 100%; font-size: .93rem; }
th, td {
  text-align: left; padding: .65rem .8rem;
  border-bottom: 1px solid var(--rule); vertical-align: top;
}
th { background: var(--card); font-weight: 650; white-space: nowrap; }
tbody tr:last-child td { border-bottom: none; }
.home {
  display: inline-block; margin-bottom: 2rem; font-size: .9rem;
  color: var(--muted); text-decoration: none;
}
.home:hover { color: var(--accent); }
footer {
  margin-top: 4rem; padding-top: 1.25rem; border-top: 1px solid var(--rule);
  font-size: .85rem; color: var(--muted);
}
@media (max-width: 480px) {
  body { font-size: 16px; }
  .wrap { padding: 2.25rem 1rem 4rem; }
  h1 { font-size: 1.55rem; }
}
"""


def inline(text):
    """인라인 문법을 변환한다. 코드 스팬 안에서는 다른 문법을 적용하지 않는다."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1)))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    def link(m):
        href = m.group(2)
        if href.endswith(".md"):
            href = href[:-3] + ".html"
        return f'<a href="{href}">{m.group(1)}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{spans[int(m.group(1))]}</code>", text)


def is_table_sep(line):
    return bool(re.match(r"^\|[\s:|-]+\|$", line)) and "-" in line


def convert(md):
    lines = md.split("\n")
    out, i = [], 0

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.startswith("```"):
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(block) + "</code></pre>")
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)$", line)
        if heading:
            lvl = len(heading.group(1))
            out.append(f"<h{lvl}>{inline(heading.group(2))}</h{lvl}>")
            i += 1
            continue

        if line.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip(">").strip())
                i += 1
            paras = "\n".join(block).split("\n\n")
            body = "".join(f"<p>{inline(p.replace(chr(10), ' '))}</p>" for p in paras if p.strip())
            out.append(f"<blockquote>{body}</blockquote>")
            continue

        if line.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            def cells(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]

            head = cells(line)
            i += 2
            body = []
            while i < len(lines) and lines[i].startswith("|"):
                body.append(cells(lines[i]))
                i += 1
            thead = "".join(f"<th>{inline(c)}</th>" for c in head)
            rows = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body
            )
            out.append(
                '<div class="table-scroll"><table><thead><tr>'
                f"{thead}</tr></thead><tbody>{rows}</tbody></table></div>"
            )
            continue

        bullet = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if bullet:
            ordered = bullet.group(2)[0].isdigit()
            items = []
            while i < len(lines):
                m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i])
                if not m:
                    break
                items.append(f"<li>{inline(m.group(3))}</li>")
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue

        para = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{1,4}\s|>|\||```|\s*([-*]|\d+\.)\s)", lines[i]
        ):
            para.append(lines[i].strip())
            i += 1
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
        else:
            i += 1

    return "\n".join(out)


def page(lang, title, body, home=True):
    back = {"ko": "← 목록으로", "en": "← Back to index"}[lang]
    nav = f'<a class="home" href="index.html">{back}</a>' if home else ""
    note = {
        "ko": "이 문서는 <code>docs/</code>의 마크다운 원본에서 <code>build.py</code>로 생성되었습니다. HTML을 직접 고치지 마세요.",
        "en": "Generated from the Markdown sources in <code>docs/</code> by <code>build.py</code>. Do not edit the HTML directly.",
    }[lang]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
{nav}
{body}
<footer>{note}</footer>
</div>
</body>
</html>
"""


def main():
    for slug, lang, title in PAGES:
        src = DOCS / f"{slug}.md"
        dest = DOCS / f"{slug}.html"
        dest.write_text(page(lang, title, convert(src.read_text(encoding="utf-8"))), encoding="utf-8")
        print(f"  {src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")

    index_md = """# explaineasily

어려운 것을 정확하게, 쉽게 설명합니다.

## 문서

- [CTI(사이버 위협 인텔리전스) 쉽게 이해하기](cti-ko.md) — 한글
- [CTI (Cyber Threat Intelligence), Explained Simply](cti-en.md) — English

## 작성 원칙

- 쉬움을 위해 사실을 왜곡하지 않는다.
- 비유는 하나만 쓰고, 그 비유가 깨지는 지점을 함께 밝힌다.
- 전문 용어는 쉬운 말로 먼저 쓰고 원어를 괄호에 병기한다.
- 어휘를 낮추는 것이지, 읽는 사람을 낮추는 것이 아니다.
"""
    (DOCS / "index.html").write_text(
        page("ko", "explaineasily", convert(index_md), home=False), encoding="utf-8"
    )
    print("  (index) -> docs/index.html")


if __name__ == "__main__":
    main()
