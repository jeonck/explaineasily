"""PPE·AI이론 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

OPERATOR = dict(hat="#5B8DEF", shirt="#2E3D57")    # 선별기 조작원 = 모델/알고리즘
INSPECTOR = dict(hat="#2E8B57", shirt="#2E8B57")   # 검수반장 = 평가 지표
TEACHER = dict(hat="#7B3FA0", shirt="#4A5A72")     # 훈련 교사 = 지도학습
CHEATER = dict(hat="#7A1F3D", shirt="#4A3B52")     # 몰래 섞는 사람 = 적대적 공격자
FARMER = dict(hat="#8B5E3C", shirt="#5A3B22")      # 농부 = 데이터 제공자


def produce(x, y, s=1.0, color="var(--good)", bad=False):
    """농작물 한 개(데이터 포인트)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="{color}"/>'
    if bad:
        out += '<path d="M-6 -6 L6 6 M6 -6 L-6 6" stroke="var(--bad)" stroke-width="3"/>'
    return out + '</g>'


def conveyor(x, y, w, s=1.0):
    """컨베이어 벨트(데이터 파이프라인)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="14" rx="4" fill="#8B5E3C"/>'
            + "".join(f'<circle cx="{i*24+12}" cy="7" r="4" fill="#C9A86A"/>' for i in range(int(w // 24))) + '</g>')


def bin_(x, y, s=1.0, label_text=None, color="var(--accent)"):
    """분류함(classification bin)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><path d="M-24 -4 h48 l-6 30 h-36 z" fill="{color}"/>'
    if label_text:
        out += label(0, -14, label_text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def scale_(x, y, s=1.0, level=0.5):
    """저울(회귀분석). level 0~1 이 기울기."""
    import math
    ang = -20 + 40 * level
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-4" y="0" width="8" height="30" fill="#5A3B22"/>'
            f'<g transform="rotate({ang:.1f})"><rect x="-40" y="-3" width="80" height="6" fill="var(--accent)"/></g></g>')


def stamp2(x, y, s=1.0, ok=True):
    """합격/불합격 도장."""
    c = "var(--good)" if ok else "var(--bad)"
    t = "✓" if ok else "×"
    return (f'<g transform="translate({x},{y}) scale({s}) rotate(-8)"><circle r="20" fill="none" stroke="{c}" stroke-width="4"/>'
            + label(0, 7, t, 22, c) + '</g>')


def gradeboard(x, y, w, h, title, rows, s=1.0, hl=-1):
    """등급표 / 평가표 — 공통 크림색 스타일."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'
