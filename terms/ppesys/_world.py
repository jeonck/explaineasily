"""PPE·시스템SW 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

CHIEF = dict(hat="#7B3FA0", shirt="#4A5A72")      # 정비반장 = CPU 스케줄러/OS
MECH1 = dict(hat="#5B8DEF", shirt="#2E3D57")      # 정비사1 = 프로세스/스레드
MECH2 = dict(hat="#2E8B57", shirt="#2E8B57")      # 정비사2 = 프로세스/스레드
CUSTOMER = dict(hat=None, shirt="#C9822B")        # 손님 = 작업 요청


def lift(x, y, s=1.0, occupied=False, label_text=None):
    """리프트 한 대(공유 자원). occupied=True 면 사용 중."""
    c = "var(--bad)" if occupied else "var(--good)"
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="0" width="60" height="8" fill="#5A3B22"/><rect x="-26" y="-50" width="8" height="50" fill="{c}"/><rect x="18" y="-50" width="8" height="50" fill="{c}"/>'
    if label_text:
        out += label(0, -58, label_text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def car(x, y, s=1.0, color="var(--accent)"):
    """차량 한 대(작업/프로세스)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="-14" width="64" height="18" rx="4" fill="{color}"/>'
            f'<rect x="-14" y="-24" width="30" height="14" rx="3" fill="{color}"/>'
            f'<circle cx="-18" cy="4" r="7" fill="#142033"/><circle cx="18" cy="4" r="7" fill="#142033"/></g>')


def toolbox(x, y, s=1.0, label_text=None):
    """공구함(캐시 메모리)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-16" width="44" height="30" rx="3" fill="#E9B44C"/><rect x="-22" y="-16" width="44" height="10" rx="3" fill="#C9822B"/>'
    if label_text:
        out += label(0, 26, label_text, 10, "var(--muted)")
    return out + '</g>'


def keyring(x, y, s=1.0, held=True):
    """리프트 열쇠(세마포어/뮤텍스). held=False 면 바닥에 놓임(반납)."""
    y2 = y if held else y + 20
    return f'<circle cx="{x}" cy="{y2}" r="8" fill="var(--accent)" stroke="#C9822B" stroke-width="2"/>'


def queueboard(x, y, w, h, title, rows, s=1.0, hl=-1):
    """작업 순서판(스케줄링 큐) / 안내판."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'
