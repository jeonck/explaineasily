"""PPE·클라우드 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

LANDLORD = dict(hat="#7B3FA0", shirt="#4A5A72")    # 건물주 = IaaS 제공자
MANAGER = dict(hat="#5B8DEF", shirt="#2E3D57")     # 건물 관리사무소 = 오케스트레이션(쿠버네티스)
TENANT = dict(hat="#2E8B57", shirt="#2E8B57")      # 입주사 = 애플리케이션
VISITOR = dict(hat=None, shirt="#C9822B")          # 방문객 = 요청/트래픽


def building(x, y, s=1.0, floors=3, label_text=None):
    """건물(데이터센터/클라우드)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="90" height="{floors*26}" fill="#D8D2C2"/>'
    for f in range(floors):
        out += f'<rect x="8" y="{f*26+6}" width="74" height="16" fill="#8B5E3C" opacity="0.4"/>'
    if label_text:
        out += label(45, -10, label_text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def office(x, y, s=1.0, shared=False, label_text=None):
    """사무실 한 칸. shared=True 면 칸막이 책상(컨테이너), False 면 독채(VM)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="60" height="44" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    if shared:
        out += '<path d="M20 0 v44 M40 0 v44" stroke="#C9A86A" stroke-width="2"/>'
    if label_text:
        out += label(30, 58, label_text, 10, "var(--muted)")
    return out + '</g>'


def deskbadge(x, y, s=1.0):
    """자동 좌석 배정 배지(오케스트레이션)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-10" width="28" height="20" rx="3" fill="var(--accent)"/>'
            f'<circle cy="-16" r="6" fill="var(--accent)"/></g>')


def meetingroom(x, y, s=1.0, hourly=False):
    """시간제 회의실(서버리스)."""
    c = "var(--good)" if hourly else "#D8D2C2"
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="50" height="36" rx="3" fill="{c}" stroke="#8B5E3C" stroke-width="2"/></g>'


def floorplan(x, y, w, h, title, rows, s=1.0, hl=-1):
    """입주 안내판."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'
