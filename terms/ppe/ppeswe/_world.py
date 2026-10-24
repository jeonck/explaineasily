"""PPE·SW공학 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`.

좌표 규칙: person() 은 (x,y) 가 머리 위 기준, 발끝은 y+112*s. 나머지 소품은 (x,y) 가 왼쪽 위/바닥 기준.
"""
from _draw import *

EDITOR = dict(hat="#7B3FA0", shirt="#4A5A72")      # 편집장 = PM/기획
WRITER = dict(hat="#5B8DEF", shirt="#2E3D57")      # 작가 = 개발자
PROOFER = dict(hat="#2E8B57", shirt="#2E8B57")     # 교정자 = 테스터/QA
PRINTER = dict(hat="#C9822B", shirt="#4A5A72")     # 인쇄 감독 = 감리
READER = dict(hat=None, shirt="#4A7B9D")           # 독자 = 사용자


def manuscript(x, y, s=1.0, marks=0, text=None):
    """원고 뭉치. marks>0 이면 빨간 교정 표시가 그만큼."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="-22" width="64" height="44" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    out += '<path d="M-22 -10 h44 M-22 -2 h44 M-22 6 h30" stroke="#142033" stroke-width="2"/>'
    for i in range(marks):
        out += f'<circle cx="{-18 + i * 16}" cy="14" r="3" fill="var(--bad)"/>'
    if text:
        out += label(0, 36, text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def printplate(x, y, s=1.0, label_text=None):
    """인쇄판(배포본)."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-20" width="60" height="40" rx="3" fill="#4A5A72"/>'
           f'<rect x="-24" y="-14" width="48" height="28" rx="2" fill="#D8D2C2"/></g>')
    if label_text:
        out += label(x, y + 34 * s, label_text, 11, "var(--muted)")
    return out


def bookshelf(x, y, s=1.0, n=4, hl=-1):
    """원고 보관 서가(형상관리/버전). hl 번째 칸을 강조."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{n * 28}" height="60" rx="3" fill="#5A3B22"/>'
    for i in range(n):
        c = "var(--accent)" if i == hl else "#C9A86A"
        out += f'<rect x="{i * 28 + 4}" y="6" width="20" height="48" rx="2" fill="{c}"/>'
    return out + '</g>'


def styleguide(x, y, w, h, title, rows, s=1.0, hl=-1):
    """편집 스타일가이드 / 안내판 — 사이트 공통 크림색."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'


def inkstamp(x, y, s=1.0, color="var(--good)"):
    """인쇄 승인 도장(출간 승인/배포 승인)."""
    return (f'<g transform="translate({x},{y}) scale({s}) rotate(-10)"><rect x="-26" y="-16" width="52" height="32" rx="4" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<path d="M-12 0 l8 8 l16 -18" stroke="{color}" stroke-width="4" fill="none" stroke-linecap="round"/></g>')


def ruler(x, y, s=1.0, text=None):
    """매수 계산 자(기능점수/규모산정)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="100" height="18" rx="2" fill="#E9B44C"/>'
    for i in range(5):
        out += f'<rect x="{i * 20}" y="0" width="2" height="18" fill="#C9822B"/>'
    if text:
        out += label(50, 32, text, 10, "var(--muted)")
    return out + '</g>'
