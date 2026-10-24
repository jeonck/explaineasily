"""PPE·IT관리 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

DIRECTOR = dict(hat="#7B3FA0", shirt="#4A5A72")    # 투어 감독관 = PMO/감리
PLANNER = dict(hat="#5B8DEF", shirt="#2E3D57")     # 기획자 = 프로젝트 매니저
ARTIST = dict(hat="#2E8B57", shirt="#2E8B57")      # 출연자 = 개발팀
SPONSOR = dict(hat="#C9822B", shirt="#4A5A72")     # 후원사 = 발주처
FAN = dict(hat=None, shirt="#4A7B9D")              # 관객 = 최종 사용자


def ticket(x, y, s=1.0, text=None):
    """공연 티켓(SLA 계약서처럼 쓰는 보장서)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-17" width="60" height="34" rx="4" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle cx="-30" cy="0" r="4" fill="var(--bg)"/><circle cx="30" cy="0" r="4" fill="var(--bg)"/>'
    if text:
        out += label(0, 5, text, 10, "#142033")
    return out + '</g>'


def checklist(x, y, w, h, title, rows, s=1.0, hl=-1):
    """공연 준비 체크리스트(WBS)."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'


def stage(x, y, w, h, s=1.0, dark=False):
    """공연 무대."""
    c = "#1B2A44" if dark else "var(--accent)"
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="3" fill="{c}"/></g>'


def umbrella(x, y, s=1.0):
    """우천 대비 우산(위험관리)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-24 0 a24 24 0 0 1 48 0 Z" fill="var(--accent)"/>'
            f'<rect x="-2" y="0" width="4" height="26" fill="#5A3B22"/></g>')


def contract(x, y, s=1.0, signed=False):
    """출연 계약서."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-28" width="44" height="56" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-14 -14 h28 M-14 -4 h28" stroke="#142033" stroke-width="2"/>'
    if signed:
        out += '<path d="M-12 10 q6 8 12 0 q6 -8 12 0" stroke="var(--accent)" stroke-width="2" fill="none"/>'
    return out + '</g>'
