#!/usr/bin/env python3
"""terms/*.py 의 그림책 정의를 docs/ 의 한글·영문 HTML로 만든다.

의존성 없음. 사용법: python3 build.py
문장은 (한글, 영문) 튜플, SVG 안의 글자는 ⟦한글|영문⟧ 로 적는다.
"""

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
TERMS = ROOT / "terms"

FONTS = {
    "ko": (
        "family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@500;700",
        '"Gowun Batang", "Apple SD Gothic Neo", serif',
        '"Noto Sans KR", "Apple SD Gothic Neo", system-ui, sans-serif',
    ),
    "en": (
        "family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Nunito:wght@500;700",
        '"Fraunces", Georgia, serif',
        '"Nunito", "Segoe UI", system-ui, sans-serif',
    ),
}

CSS = """
:root {
  --display: __DISPLAY__; --body: __BODY__;
  --bg: #EEF2F7; --panel: #FFFFFF; --ink: #142033; --muted: #5B6B82; --line: #D3DBE6;
  --accent: #E85D04; --accent-soft: #FFE3CF;
  --good: #1B7F79; --good-soft: #D3EEEC;
  --bad: #B5382C; --bad-soft: #F6D9D5;
  --sky: #BFD3EA; --stone: #9FB0C4; --stone-dark: #6E8199; --night: #1E2E4A;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0E1626; --panel: #172238; --ink: #E9EFF7; --muted: #9FB0C6; --line: #2A3A55;
    --accent: #FF7A1A; --accent-soft: #4A2A12;
    --good: #4FC3B8; --good-soft: #163B3A;
    --bad: #F07A6C; --bad-soft: #4A1F1B;
    --sky: #223454; --stone: #52657F; --stone-dark: #3A4B63; --night: #0A1120;
  }
}
:root[data-theme="dark"] {
  --bg: #0E1626; --panel: #172238; --ink: #E9EFF7; --muted: #9FB0C6; --line: #2A3A55;
  --accent: #FF7A1A; --accent-soft: #4A2A12;
  --good: #4FC3B8; --good-soft: #163B3A;
  --bad: #F07A6C; --bad-soft: #4A1F1B;
  --sky: #223454; --stone: #52657F; --stone-dark: #3A4B63; --night: #0A1120;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--body); font-weight: 500; line-height: 1.4; }
.book { max-width: 760px; margin: 0 auto; padding: 32px 20px 72px; display: grid; gap: 28px; }
.top { display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; }
.top a { color: var(--muted); text-decoration: none; }
.top a:hover, .top a:focus-visible { color: var(--accent); }
header { display: grid; gap: 8px; }
.eyebrow { font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); font-weight: 700; }
h1 { font-family: var(--display); font-weight: 700; font-size: clamp(38px, 7vw, 60px); line-height: 1.12; margin: 0; text-wrap: balance; }
h1 em { color: var(--accent); font-style: normal; }
.sub { color: var(--muted); font-size: 18px; margin: 0; max-width: 36ch; }
.panel { background: var(--panel); border: 1px solid var(--line); border-radius: 22px; overflow: hidden; display: grid; }
.panel.hero { border-color: var(--accent); }
.panel svg { display: block; width: 100%; height: auto; }
.panel svg text { font-family: var(--body); font-weight: 700; }
.panel svg text.d { font-family: var(--display); }
.panel p { margin: 0; padding: 20px 26px 26px; font-family: var(--display); font-weight: 700; font-size: clamp(24px, 4.2vw, 32px); line-height: 1.3; text-wrap: balance; }
.panel p small { display: block; margin-top: 6px; font-family: var(--body); font-weight: 500; font-size: 17px; color: var(--muted); line-height: 1.45; }
.panel p small a { color: var(--accent); }
.tricks { display: grid; grid-template-columns: repeat(var(--cols, 3), 1fr); gap: 12px; padding: 0 26px 26px; }
.trick { background: var(--bad-soft); border-radius: 14px; padding: 12px 12px 14px; display: grid; gap: 6px; text-align: center; }
.trick.calm { background: var(--good-soft); }
.trick.warm { background: var(--accent-soft); }
.trick svg { width: 64px; height: 64px; margin: 0 auto; }
.trick b { font-size: 15px; font-weight: 700; }
.trick span { font-size: 13px; color: var(--muted); }
@media (max-width: 520px) { .tricks { grid-template-columns: 1fr 1fr; } }
.bubbles { display: grid; gap: 10px; padding: 0 26px 26px; }
.bubble { background: var(--accent-soft); border-radius: 16px 16px 16px 4px; padding: 12px 16px; font-size: 18px; font-weight: 700; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.bubble .arrow { color: var(--accent); }
.sum { background: var(--night); color: #F2F6FC; border-radius: 22px; padding: 28px 26px; display: grid; gap: 10px; }
.sum .eyebrow { color: #A9B9D2; }
.sum h2 { font-family: var(--display); font-weight: 700; font-size: clamp(26px, 4.6vw, 36px); margin: 0; line-height: 1.25; text-wrap: balance; }
.sum h2 b { color: #FFA45C; }
.sum p { margin: 0; color: #C9D5E6; font-size: 17px; max-width: 48ch; }
.glossary { border-top: 1px solid var(--line); }
.glossary h3 { font-family: var(--display); font-weight: 700; font-size: 20px; margin: 22px 0 6px; }
.glossary dl { margin: 0; display: grid; }
.glossary div { display: grid; grid-template-columns: 160px 1fr; gap: 14px; padding: 12px 0; border-bottom: 1px solid var(--line); align-items: baseline; }
.glossary dt { font-weight: 700; font-size: 15px; }
.glossary dt small { font-weight: 500; font-size: 12px; color: var(--muted); }
.glossary dd { margin: 0; color: var(--muted); font-size: 15px; }
.glossary dd b { color: var(--ink); }
@media (max-width: 480px) { .glossary div { grid-template-columns: 1fr; gap: 2px; } }
.next { display: grid; gap: 6px; }
.next a { color: var(--accent); font-weight: 700; text-decoration: none; }
.next a:hover, .next a:focus-visible { text-decoration: underline; }
.index { display: grid; gap: 14px; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 18px 22px; display: grid; gap: 6px; }
.card .eyebrow { margin: 0; }
.card h3 { font-family: var(--display); font-weight: 700; font-size: 24px; margin: 0; line-height: 1.25; }
.card .links { display: flex; gap: 14px; font-size: 14px; font-weight: 700; }
.card .links a { color: var(--accent); text-decoration: none; }
.card .links a:hover, .card .links a:focus-visible { text-decoration: underline; }
.rules { color: var(--muted); font-size: 16px; padding-left: 1.2em; margin: 0; display: grid; gap: 6px; }
@media (prefers-reduced-motion: no-preference) {
  .flame { transform-origin: 50% 100%; animation: flicker 1.6s ease-in-out infinite alternate; }
  @keyframes flicker { from { transform: scaleY(1) } to { transform: scaleY(1.12) scaleX(0.94) } }
}
"""

UI = {
    "ko": {"index": "← 목록", "other": "English", "eyebrow": "다섯 살도 알 수 있게",
           "sum": "한 줄로", "gloss": "어른들은 이렇게 불러요", "next": "다음 이야기", "lang": "ko"},
    "en": {"index": "← Index", "other": "한국어", "eyebrow": "Explain like I'm five",
           "sum": "In one breath", "gloss": "When grown-ups say it", "next": "Next story", "lang": "en"},
}


def L(v, lang):
    """(ko, en) 튜플이면 언어에 맞는 쪽을, 문자열이면 ⟦ko|en⟧ 을 풀어서 돌려준다."""
    if isinstance(v, tuple):
        v = v[0 if lang == "ko" else 1]
    return re.sub(r"⟦(.*?)\|(.*?)⟧", lambda m: m.group(1 if lang == "ko" else 2), v)


def render_panel(p, lang):
    alt = L(p.get("alt", ""), lang)
    svg = L(p["svg"], lang).replace("<svg ", f'<svg role="img" aria-label="{alt}" ', 1)
    small = L(p.get("small", ""), lang)
    small = f"<small>{small}</small>" if small else ""
    out = [f'<section class="panel{" hero" if p.get("hero") else ""}">', svg,
           f"<p>{L(p['caption'], lang)}{small}</p>"]
    if "tricks" in p:
        cols, items = p["tricks"]
        out.append(f'<div class="tricks" style="--cols:{cols}">')
        for icon, b, s, *tone in items:
            cls = f" {tone[0]}" if tone else ""
            out.append(f'<div class="trick{cls}">{icon}<b>{L(b, lang)}</b><span>{L(s, lang)}</span></div>')
        out.append("</div>")
    if "bubbles" in p:
        out.append('<div class="bubbles">')
        for left, right in p["bubbles"]:
            out.append(f'<div class="bubble">{L(left, lang)} <span class="arrow">→</span> {L(right, lang)}</div>')
        out.append("</div>")
    out.append("</section>")
    return "\n".join(out)


def page_html(lang, title, body):
    link, display, bodyf = FONTS[lang]
    css = CSS.replace("__DISPLAY__", display).replace("__BODY__", bodyf)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{link}&display=swap">
<style>{css}</style>
</head>
<body>
<main class="book">
{body}
</main>
</body>
</html>
"""


def render_term(t, lang, order):
    ui = UI[lang]
    slug = t["slug"]
    other = "en" if lang == "ko" else "ko"
    parts = [
        f'<nav class="top"><a href="index.html">{ui["index"]}</a><a href="{slug}-{other}.html" lang="{other}">{ui["other"]}</a></nav>',
        "<header>",
        f'<div class="eyebrow">{ui["eyebrow"]}</div>',
        f"<h1>{L(t['h1'], lang)}</h1>",
        f'<p class="sub">{L(t["sub"], lang)}</p>',
        "</header>",
    ]
    parts += [render_panel(p, lang) for p in t["panels"]]
    s = t["summary"]
    parts.append(f'<section class="sum"><div class="eyebrow">{ui["sum"]}</div>'
                 f"<h2>{L(s[0], lang)}</h2><p>{L(s[1], lang)}</p></section>")
    rows = []
    for term_ko, term_en, b, rest in t["glossary"]:
        dt = f"{term_ko}<br><small>{term_en}</small>" if lang == "ko" and term_en else (term_en or term_ko)
        rows.append(f"<div><dt>{dt}</dt><dd><b>{L(b, lang)}</b> {L(rest, lang)}</dd></div>")
    parts.append(f'<section class="glossary"><h3>{ui["gloss"]}</h3><dl>{"".join(rows)}</dl></section>')
    slugs = [o["slug"] for o in order]
    nxt = order[(slugs.index(slug) + 1) % len(order)]
    parts.append(f'<section class="next"><div class="eyebrow">{ui["next"]}</div>'
                 f'<a href="{nxt["slug"]}-{lang}.html">{L(nxt["title"], lang)} →</a></section>')
    return page_html(lang, L(t["title"], lang), "\n".join(parts))


def render_index(terms):
    cards = []
    for t in terms:
        cards.append(
            f'<article class="card"><div class="eyebrow">{t["slug"].upper()}</div>'
            f'<h3>{L(t["title"], "ko")}</h3>'
            f'<div class="links"><a href="{t["slug"]}-ko.html">한국어</a>'
            f'<a href="{t["slug"]}-en.html" lang="en">English</a></div></article>'
        )
    body = f"""<header>
<div class="eyebrow">explaineasily</div>
<h1>어려운 말을 <em>그림</em>으로</h1>
<p class="sub">보안 용어를 다섯 살 눈높이의 그림책으로. 글은 적게, 그림은 크게.</p>
</header>
<section class="index">{"".join(cards)}</section>
<section class="glossary"><h3>작성 원칙</h3>
<ul class="rules">
<li>쉬움을 위해 사실을 왜곡하지 않는다.</li>
<li>비유는 하나만 쓰고, 그 비유가 깨지는 지점을 함께 밝힌다.</li>
<li>전문 용어는 쉬운 말로 먼저 쓰고 원어를 병기한다 — 나중에 검색할 수 있어야 한다.</li>
<li>어휘를 낮추는 것이지, 읽는 사람을 낮추는 것이 아니다.</li>
</ul></section>"""
    return page_html("ko", "explaineasily", body)


def load_terms():
    sys.path.insert(0, str(TERMS))
    terms = []
    for path in sorted(TERMS.glob("[!_]*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        terms.append(mod.PAGE)
    terms.sort(key=lambda t: t["order"])
    return terms


def main():
    terms = load_terms()
    DOCS.mkdir(exist_ok=True)
    for t in terms:
        for lang in ("ko", "en"):
            dest = DOCS / f"{t['slug']}-{lang}.html"
            dest.write_text(render_term(t, lang, terms), encoding="utf-8")
            print(f"  terms/{t['slug']}.py -> {dest.relative_to(ROOT)}")
    (DOCS / "index.html").write_text(render_index(terms), encoding="utf-8")
    print("  (index) -> docs/index.html")


if __name__ == "__main__":
    main()
