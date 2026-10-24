"""PPE·네트워크 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

CLERK = dict(hat="#7B3FA0", shirt="#4A5A72")      # 우체국장 = 라우터
CARRIER = dict(hat="#5B8DEF", shirt="#2E3D57")    # 집배원 = 패킷 운반
SORTER = dict(hat="#2E8B57", shirt="#2E8B57")     # 분류소 직원 = 스위치
SENDER = dict(hat=None, shirt="#4A7B9D")          # 보내는 사람
RECEIVER = dict(hat=None, shirt="#C9822B")        # 받는 사람


def envelope(x, y, s=1.0, registered=False, text=None):
    """봉투(패킷). registered=True 면 등기(TCP) 표시."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-18" width="52" height="36" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-26 -18 L0 0 L26 -18" fill="none" stroke="#C9A86A" stroke-width="2"/>'
    if registered:
        out += '<circle cx="18" cy="10" r="8" fill="var(--accent)"/>' + label(18, 13, "등기", 7, "#fff")
    if text:
        out += label(0, 30, text, 10, "var(--muted)")
    return out + '</g>'


def postoffice(x, y, s=1.0, label_text=None):
    """우체국 건물(라우터/게이트웨이)."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-10" width="80" height="50" fill="#D8D2C2"/>'
           f'<path d="M-46 -10 h92 l-46 -28z" fill="#8B5E3C"/><rect x="-10" y="18" width="20" height="22" fill="#5A3B22"/>')
    if label_text:
        out += label(0, -46, label_text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def routemap(x, y, w, h, title, rows, s=1.0, hl=-1):
    """배송 경로 지도 / 안내판."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'


def tollgate(x, y, s=1.0, open_=True):
    """톨게이트(스위칭/교환). 요청마다 여닫는다."""
    c = "var(--good)" if open_ else "var(--bad)"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="-30" width="12" height="30" fill="#5A3B22"/>'
            f'<rect x="-6" y="-30" width="50" height="8" fill="{c}" transform="rotate({-70 if open_ else 0})"/></g>')


def truck(x, y, s=1.0, fast=False):
    """배달 트럭(5G/속달)."""
    c = "var(--accent)" if fast else "#8B5E3C"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-16" width="44" height="20" rx="3" fill="{c}"/>'
            f'<rect x="14" y="-10" width="18" height="14" rx="2" fill="{c}"/>'
            f'<circle cx="-18" cy="6" r="6" fill="#142033"/><circle cx="18" cy="6" r="6" fill="#142033"/></g>')
