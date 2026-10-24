"""PPE·신기술 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

GUIDE = dict(hat="#7B3FA0", shirt="#4A5A72")       # 전시관 안내원
VISITOR = dict(hat=None, shirt="#C9822B")          # 관람객
DEMO = dict(hat="#5B8DEF", shirt="#2E3D57")        # 시연 담당자


def booth(x, y, w, h, s=1.0, color="var(--accent)", label_text=None):
    """전시 부스 한 칸."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="{color}" opacity="0.18" stroke="{color}" stroke-width="3"/>'
    if label_text:
        out += label(w / 2, -12, label_text, 12, "var(--ink)", cls="d")
    return out + '</g>'


def ribbon(x, y, s=1.0, text=None):
    """전시관 입구 리본/현수막."""
    out = f'<g transform="translate({x},{y}) scale({s})"><path d="M-40 0 h80 l-6 16 h-68 z" fill="var(--accent)"/>'
    if text:
        out += label(0, 11, text, 11, "#fff")
    return out + '</g>'


def screen(x, y, s=1.0, content=None):
    """시연 화면(디지털트윈/메타버스 등)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="80" height="56" rx="4" fill="#1B2A44"/><rect x="6" y="6" width="68" height="44" rx="2" fill="#0A1120"/>'
    if content:
        out += content
    return out + '</g>'


def infoboard(x, y, w, h, title, rows, s=1.0, hl=-1):
    """전시 설명판."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'
