#!/usr/bin/env python3
"""Headless visual QA: render every panel SVG of docs/<slug>-<lang>.html into one stacked PNG per slug.

Usage:
    python3 render_qa.py OUT_DIR slug [slug ...] [--lang ko] [--docs docs] [--build build.py] [--font "Apple SD Gothic Neo"]

Then look at OUT_DIR/<slug>.png (one image = the 5 panels of that page) and check for overlaps,
clipped text, elements outside the 760px canvas. Trick-card icons (64x64) are skipped.

Requires: cairosvg, Pillow. CSS tokens (var(--x)) are read from build.py's light theme block;
falls back to a built-in map. Korean needs a CJK font name installed on the machine.
"""
import argparse, io, re, sys, os

DEFAULT_TOKENS = {
    "--bg": "#EEF2F7", "--panel": "#FFFFFF", "--ink": "#142033", "--muted": "#5B6B82", "--line": "#D3DBE6",
    "--accent": "#E85D04", "--accent-soft": "#FFE3CF", "--good": "#1B7F79", "--good-soft": "#D3EEEC",
    "--bad": "#B5382C", "--bad-soft": "#F6D9D5", "--sky": "#BFD3EA", "--stone": "#9FB0C4",
    "--stone-dark": "#6E8199", "--night": "#1E2E4A",
}


def tokens_from_build(path):
    """First occurrence of each --token: value in build.py is the light theme."""
    tok = dict(DEFAULT_TOKENS)
    try:
        src = open(path).read()
        for k, v in re.findall(r'(--[a-z-]+):\s*(#[0-9A-Fa-f]{3,6})', src):
            tok.setdefault(k, v)
            if k in DEFAULT_TOKENS and tok[k] == DEFAULT_TOKENS[k]:
                tok[k] = v  # take the first (light) definition
        # ensure first-definition wins: re-scan in order and keep first
        seen = {}
        for k, v in re.findall(r'(--[a-z-]+):\s*(#[0-9A-Fa-f]{3,6})', src):
            seen.setdefault(k, v)
        tok.update(seen)
    except OSError:
        pass
    return tok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("slugs", nargs="+")
    ap.add_argument("--lang", default="ko"); ap.add_argument("--docs", default="docs")
    ap.add_argument("--build", default="build.py"); ap.add_argument("--font", default="Apple SD Gothic Neo")
    a = ap.parse_args()
    import cairosvg
    from PIL import Image
    tok = tokens_from_build(a.build)
    font = f'<style>text{{font-family:"{a.font}";font-weight:700}}</style>'
    os.makedirs(a.out, exist_ok=True)
    for slug in a.slugs:
        f = os.path.join(a.docs, f"{slug}-{a.lang}.html")
        s = open(f).read()
        imgs = []
        for m in re.finditer(r'<svg[^>]*viewBox="0 0 760 [^>]*>.*?</svg>', s, re.S):
            svg = re.sub(r'var\((--[a-z-]+)\)', lambda k: tok.get(k.group(1), "#888"), m.group(0))
            svg = svg.replace('>', '>' + font, 1)
            png = cairosvg.svg2png(bytestring=svg.encode(), output_width=760)
            imgs.append(Image.open(io.BytesIO(png)).convert("RGB"))
        if not imgs:
            print(slug, "no panels found", file=sys.stderr); continue
        H = sum(i.height for i in imgs) + 10 * len(imgs)
        sheet = Image.new("RGB", (760, H), "#EEF2F7"); y = 0
        for i in imgs:
            sheet.paste(i, (0, y)); y += i.height + 10
        sheet.save(os.path.join(a.out, f"{slug}.png")); print(slug, len(imgs), "panels", H, "px")


if __name__ == "__main__":
    main()
