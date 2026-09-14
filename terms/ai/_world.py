"""AI 분야 전용 그림 조각. 페이지에서 `from _draw import *` 다음에 `from _world import *`."""
from _draw import *

PARROT = "#5B8DEF"      # 우리 앵무새(모델)
PARROT_BIG = "#3F6FD1"  # 큰 앵무새
PARROT_BAD = "var(--bad)"  # 그럴듯 앵무새(할루시네이션)
TRAINER = dict(hat="var(--good)", shirt="var(--good)")          # 조련사
LIBRARIAN = dict(hat="var(--stone-dark)", shirt="#4A5A72")       # 사서
EXAMINER = dict(hat="#E9B44C", shirt="#4A5A72")                  # 시험관
GUEST = dict(hat=None, shirt="#7B3FA0")                          # 손님
BEAN = "#C9822B"        # 콩(토큰)
PAPER = "#FFF8E7"
PAPER_INK = "#142033"


def parrot(x, y, s=1.0, color=PARROT, mood="", talk=False):
    """앵무새. 머리 (0,-24), 몸통 (0,0), 꼬리 아래 y=40. 폭 약 44, 높이 약 78.
    mood: "" 보통 / "think" 눈 감고 생각 / "sweat" 당황. talk=True 면 부리를 벌린다."""
    eye = ('<path d="M0 -28 q4 -3 8 0" stroke="#142033" stroke-width="2" fill="none"/>' if mood == "think"
           else '<circle cx="3" cy="-27" r="3" fill="#FFF"/><circle cx="4" cy="-27" r="1.5" fill="#142033"/>')
    beak = ('<path d="M9 -30 l14 0 l-14 6z M9 -22 l14 0 l-14 -4z" fill="#E9B44C"/>' if talk
            else '<path d="M9 -28 l14 4 l-14 6z" fill="#E9B44C"/>')
    sweat = '<path d="M-16 -36 q5 6 0 12 q-5 -6 0 -12z" fill="#5B9BD5"/>' if mood == "sweat" else ""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-6 16 l-6 24 l8 -2z M6 16 l6 24 l-8 -2z" fill="{color}"/>'
            f'<ellipse rx="14" ry="20" fill="{color}"/><ellipse cx="-3" cy="3" rx="7" ry="13" fill="#142033" opacity="0.25"/>'
            f'<circle cy="-24" r="12" fill="{color}"/>{beak}{eye}{sweat}'
            f'<path d="M-4 20 v8 M4 20 v8" stroke="#E9B44C" stroke-width="3" stroke-linecap="round"/></g>')


def perch(x, y, w=120):
    """앵무새가 앉는 횃대. 앵무새는 parrot(x, y-40) 에 놓는다."""
    return f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="6" rx="3" fill="{WOOD}"/><rect x="{x - 3}" y="{y}" width="6" height="40" fill="#5A3B22"/>'


def bean(x, y, s=1.0, color=BEAN, text=None):
    """콩 하나 = 토큰 하나. text 를 주면 콩 위에 낱말을 적는다."""
    t = label(0, 4, text, 10, "#FFF8E7") if text else ""
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><path d="M-6 -4 q6 -4 12 0" stroke="#5A3B22" stroke-width="1.5" fill="none"/>{t}</g>'


def beans(x, y, words, s=1.0, gap=36, color=BEAN):
    """콩을 한 줄로. words 는 ⟦..|..⟧ 문자열 목록."""
    return "".join(bean(x + i * gap, y, s, color, w) for i, w in enumerate(words))


def tray(x, y, w=240, h=70, label_text=None):
    """쟁반 = 컨텍스트 창. 콩은 tray 위 (y-12) 줄에 놓는다."""
    t = label(x + w / 2, y + h + 18, label_text, 11, "var(--muted)") if label_text else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="var(--stone)" opacity="0.55"/>'
            f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="8" fill="none" stroke="var(--stone-dark)" stroke-width="3"/>{t}')


def note(x, y, w, h, title, lines, s=1.0, hl=-1):
    """조련 쪽지 / 시험지. 크림 종이 위 글자는 #142033 고정."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="{PAPER}" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, PAPER_INK, cls="d"))
    for i, t in enumerate(lines):
        yy = 50 + i * 22
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, t, 12, PAPER_INK, "start")
    return out + "</g>"


def books(x, y, n=4, s=1.0):
    """책 더미 = 학습 데이터. 아래에서 위로 n 권."""
    cols = ("#7B3FA0", "#2E7D6B", "#C9822B", "#5B8DEF", "#B5382C", "#6E8199")
    return f'<g transform="translate({x},{y}) scale({s})">' + "".join(
        f'<rect x="{-40 + (i % 2) * 6}" y="{-14 * (i + 1)}" width="80" height="12" rx="2" fill="{cols[i % len(cols)]}"/>' for i in range(n)) + "</g>"


def bubble_parrot(x, y, w, h, text, size=12, bad=False):
    """앵무새 말풍선. bad=True 면 빨간 테두리(그럴듯한 거짓말)."""
    return bubble(x, y, w, h, text, size, "var(--panel)", "var(--bad)" if bad else "var(--line)", "bottom")


def dial(x, y, s=1.0, level=0.5, text=None):
    """엉뚱함 다이얼 (temperature). level 0~1."""
    import math
    ang = -120 + 240 * level
    kx, ky = 22 * math.sin(math.radians(ang)), -22 * math.cos(math.radians(ang))
    t = label(0, 44, text, 10, "var(--muted)") if text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="28" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M0 0 L{kx:.1f} {ky:.1f}" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle r="4" fill="var(--accent)"/>{t}</g>')
