"""PPE·법제도 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

PRESIDENT = dict(hat="#7B3FA0", shirt="#4A5A72")   # 학생회장 = 표준·법 제정자
REP = dict(hat="#5B8DEF", shirt="#2E3D57")         # 대표 = 각 분야 담당
STUDENT = dict(hat=None, shirt="#C9822B")          # 학생 = 조직/기업
TEACHER = dict(hat="#2E8B57", shirt="#2E8B57")     # 선생님 = 감독기관


def rulesboard(x, y, w, h, title, rows, s=1.0, hl=-1):
    """학교 규칙판 / 안내판."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'


def suppliestag(x, y, s=1.0, text=None):
    """공용 준비물에 붙은 라벨(라이선스/표시 의무)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-12" width="40" height="24" rx="3" fill="var(--accent)"/>'
    if text:
        out += label(0, 4, text, 9, "#fff")
    return out + '</g>'


def gavel(x, y, s=1.0):
    """규칙 제정 의사봉."""
    return (f'<g transform="translate({x},{y}) scale({s}) rotate(-20)"><rect x="-6" y="-26" width="12" height="40" rx="3" fill="#8B5E3C"/>'
            f'<rect x="-18" y="-30" width="36" height="12" rx="3" fill="#5A3B22"/></g>')


def checkmachine(x, y, s=1.0):
    """자동 규칙 검사기(레그테크)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-20" width="40" height="40" rx="6" fill="#1B2A44"/>'
            f'<path d="M-8 0 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/></g>')


def noticeboard(x, y, s=1.0, label_text=None):
    """공지사항 게시판(공공데이터 공개)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="70" height="50" rx="3" fill="#8B5E3C"/><rect x="6" y="6" width="58" height="38" fill="#FFF8E7"/>'
    if label_text:
        out += label(35, 64, label_text, 10, "var(--muted)")
    return out + '</g>'
