"""SRE 분야 전용 그림 조각. 페이지에서 `from _draw import *` 다음 `from _world import *`.\n\n좌표 규칙: person()/queueline() 은 (x, y) 가 머리 위쪽 기준점이고 발끝은 y + 112*s 에 옵니다.\n바닥선(ground)에 발을 맞추려면 y = ground - 112*s 로 호출하세요 (예: ground=260, s=0.5 → y=204).\nride()/booth()/shed() 는 (x, y) 가 바닥선(ground) 자체입니다 — 섞어 쓸 때 혼동하지 마세요."""
from _draw import *

OPERATOR = dict(hat="#2E7D6B", shirt="#2E7D6B")      # 관제실 요원 (SRE/온콜)
MECHANIC = dict(hat="#E9B44C", shirt="#4A5A72")       # 놀이기구 정비사 (엔지니어/배포)
MANAGER = dict(hat="#7B3FA0", shirt="#4A5A72")        # 공원장 (이해관계자/제품 책임자)
ROOKIE = dict(hat="#5B8DEF", shirt="#2E3D57")         # 신참 정비사 (카나리/신규 코드)
FOLK = ((None, "#4A5A72"), ("#E9B44C", "#2E7D6B"), (None, "#C9822B"), (None, "#7B3FA0"), ("#5B8DEF", "#2E3D57"), (None, "#2E7D6B"))  # 손님(요청) 색 섞음
WRENCH = '<g transform="translate(58,54) rotate(-30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#5A3B22"/><circle cy="-4" r="7" fill="none" stroke="#5A3B22" stroke-width="4"/></g>'
CLIPBOARD = '<rect x="48" y="60" width="26" height="34" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M54 68 h14 M54 76 h14 M54 84 h8" stroke="#142033" stroke-width="2"/>'


def ride(x, y, s=1.0, color="var(--accent)", closed=False, label_text=None):
    """놀이기구(천막형 부스). 바닥 y=0 기준 위로 높이 ~130, 폭 ~120. person()/queueline() 과 바닥선을 맞출 때
    발끝은 `y + 112*s` 에 오므로, 같은 바닥에 세우려면 person 의 y 를 `ground - 112*s` 로 준다."""
    pennants = "".join(f'<path d="M{-48 + i * 16} -62 l8 10 l8 -10z" fill="{"#FFF8E7" if i % 2 else color}"/>' for i in range(7))
    out = (f'<g transform="translate({x},{y}) scale({s})">'
           f'<rect x="-60" y="-6" width="120" height="8" rx="3" fill="var(--stone-dark)"/>'
           f'<rect x="-42" y="-62" width="10" height="58" fill="var(--stone-dark)"/><rect x="32" y="-62" width="10" height="58" fill="var(--stone-dark)"/>'
           f'<path d="M-52 -62 Q0 -118 52 -62 Z" fill="{color}"/>{pennants}'
           f'<rect x="-16" y="-40" width="32" height="34" rx="3" fill="var(--night)"/>')
    if closed:
        out += '<rect x="-46" y="-36" width="92" height="12" fill="var(--bad)" transform="rotate(-8)"/><rect x="-46" y="-16" width="92" height="12" fill="var(--bad)" transform="rotate(6)"/>'
    if label_text:
        out += label(0, -128, label_text, 12, "var(--ink)", cls="d")
    return out + "</g>"


def booth(x, y, s=1.0, label_text=None, lit=True):
    """매표 창구. 폭 70 높이 70."""
    glow = "#FFF3D6" if lit else "var(--stone)"
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-35" y="-10" width="70" height="60" rx="4" fill="#8B5E3C"/>'
           f'<rect x="-35" y="-26" width="70" height="20" rx="4" fill="#5A3B22"/><rect x="-24" y="2" width="48" height="24" rx="3" fill="{glow}"/>')
    if label_text:
        out += label(0, -32, label_text, 11, "var(--ink)", cls="d")
    return out + "</g>"


def queueline(x, y, n=4, s=0.6, gap=34):
    """대기줄. 사람 n명을 가로로."""
    return "".join(person(x + i * gap, y, s=s, hat=FOLK[i % len(FOLK)][0], shirt=FOLK[i % len(FOLK)][1], face=EYES) for i in range(n))


def controlroom(x, y, w=200, h=110, bars=None):
    """관제실 화면 벽. bars 는 (높이비율0..1, 색) 목록으로 막대그래프를 그린다."""
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#1B2A44"/><rect x="6" y="6" width="{w - 12}" height="{h - 12}" rx="4" fill="#0A1120"/>'
    if bars:
        bw = (w - 24) / len(bars)
        for i, (r, c) in enumerate(bars):
            bh = (h - 24) * max(0.05, r)
            out += f'<rect x="{12 + i * bw + 2}" y="{h - 12 - bh}" width="{bw - 6}" height="{bh}" rx="2" fill="{c}"/>'
    return out + "</g>"


def walkie(x, y, s=1.0):
    """무전기 = 알림/페이징."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-10" y="-20" width="20" height="36" rx="4" fill="var(--stone-dark)"/>'
            f'<rect x="-6" y="-16" width="12" height="8" fill="#5B9BD5"/><rect x="-3" y="-28" width="6" height="10" fill="var(--stone-dark)"/>'
            f'<circle cx="0" cy="-30" r="3" fill="var(--bad)"/></g>')


def bigbutton(x, y, s=1.0, pressed=False):
    """비상 정지 버튼 = 서킷 브레이커."""
    c = "var(--bad)" if not pressed else "#7A1F17"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="10" width="32" height="14" rx="3" fill="var(--stone-dark)"/>'
            f'<circle r="18" fill="{c}" stroke="#7A1F17" stroke-width="3"/>{"<circle r=\"18\" fill=\"var(--bad)\" opacity=\"0.4\"/>" if not pressed else ""}</g>')


def shed(x, y, s=1.0, label_text=None):
    """여분 부품 창고 = 백업/리던던시."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-10" width="80" height="54" fill="var(--stone)"/>'
           f'<path d="M-46 -10 h92 l-46 -30z" fill="var(--stone-dark)"/><rect x="-10" y="14" width="20" height="30" fill="#5A3B22"/>')
    if label_text:
        out += label(0, -40, label_text, 11, "var(--muted)")
    return out + "</g>"


def minipark(x, y, s=1.0):
    """쌍둥이 공원 (다른 지역) 아이콘."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="-20" width="120" height="50" fill="var(--stone)"/>'
            f'<path d="M-66 -20 a66 30 0 0 1 132 0 Z" fill="var(--accent)" opacity="0.7"/>'
            f'<rect x="-8" y="0" width="16" height="30" fill="var(--stone-dark)"/></g>')


def ticket(x, y, s=1.0, text=None, color="#E9B44C"):
    """티켓 한 장. 폭 60 높이 34."""
    t = label(0, 6, text, 11, "#142033") if text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-17" width="60" height="34" rx="4" fill="{color}" stroke="#C9822B" stroke-width="2"/>'
            f'<circle cx="-30" cy="0" r="4" fill="var(--bg)"/><circle cx="30" cy="0" r="4" fill="var(--bg)"/>{t}</g>')


def board(x, y, w, h, title, rows, s=1.0, hl=-1):
    """공원 안내판 / 메모판 — 크림 종이, 사이트 공통 스타일. 글자는 #142033 고정."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + "</g>"


def gauge(x, y, s=1.0, level=0.6, label_text=None, color="var(--accent)"):
    """계기판 바늘. level 0~1."""
    import math
    ang = -120 + 240 * level
    kx, ky = 26 * math.sin(math.radians(ang)), -26 * math.cos(math.radians(ang))
    t = label(0, 44, label_text, 10, "var(--muted)") if label_text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="30" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M0 0 L{kx:.1f} {ky:.1f}" stroke="{color}" stroke-width="4" stroke-linecap="round"/><circle r="4" fill="{color}"/>{t}</g>')
