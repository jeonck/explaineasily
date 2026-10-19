"""AI 보안 분야 전용 그림 조각. 페이지에서 `from _draw import *` 다음 `from _world import *`.

좌표 규칙: person() 은 (x, y) 가 머리 위쪽 기준점이고 발끝은 y + 112*s 에 옵니다.
바닥선(ground)에 발을 맞추려면 y = ground - 112*s 로 호출하세요 (예: ground=260, s=0.5 → y=204).
ticket()/dish()/pantry()/recipebook()/knifedrawer()/bell()/logbook()/board()/badge()/stamp() 는
(x, y) 가 그 소품의 중심(또는 바닥) 기준입니다 — person() 과 섞어 쓸 때 혼동하지 마세요.
"""
from _draw import *

CHEF = dict(hat="#2E3D57", shirt="#FFF8E7")          # 주방장 = AI 모델 (짙은 모자 + 크림 앞치마, 모든 배경에서 보이게)
GUEST = dict(hat=None, shirt="#4A7B9D")               # 손님 = 정상 사용자
SNEAK = dict(hat="#7A1F3D", shirt="#4A3B52")          # 몰래 쪽지 끼우는 손님 = 공격자
TASTER = dict(hat="#2E8B57", shirt="#2E8B57")         # 맛보기 검수원 = 가드레일/출력 필터
INSPECTOR = dict(hat="#C9822B", shirt="#4A5A72")      # 위생 검사관 = AI 레드팀/보안 감사관
MANAGER = dict(hat="#5B3A8E", shirt="#4A5A72")        # 사장님 = 거버넌스 책임자/최종 승인자
RUNNER = dict(hat="#5B8DEF", shirt="#2E3D57")         # 견습생(심부름꾼) = 자율 에이전트/도구 호출
SUPPLIER = dict(hat="#8B5E3C", shirt="#5A3B22")       # 재료 공급업체 = 모델/데이터 공급망


def ticket(x, y, s=1.0, text=None, sneaky=False):
    """주문서 한 장. sneaky=True 면 뒤에 몰래 끼운 빨간 쪽지가 삐져나온다."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    if sneaky:
        out += '<rect x="-24" y="-30" width="48" height="26" rx="2" fill="var(--bad)" transform="rotate(8)"/>'
    out += '<rect x="-28" y="-20" width="56" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    out += '<path d="M-20 -10 h40 M-20 -2 h40 M-20 6 h24" stroke="#142033" stroke-width="2"/>'
    if text:
        out += label(0, 30, text, 11, "var(--ink)", cls="d")
    return out + '</g>'


def dish(x, y, s=1.0, color="var(--accent)", bad=False):
    """완성된 요리(접시). bad=True 면 접시 위에 경고 표시."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="6" rx="34" ry="10" fill="#D8D2C2"/>'
           f'<ellipse cx="0" cy="0" rx="30" ry="9" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
           f'<circle cx="0" cy="-1" r="14" fill="{color}"/>')
    if bad:
        out += '<path d="M0 -10 l6 11 h-12z" fill="var(--bad)"/><circle cx="0" cy="-3" r="1.6" fill="#fff"/>'
    return out + '</g>'


def pantry(x, y, s=1.0, w=160, h=100, bad_shelf=-1, n=4):
    """재료 창고 선반. bad_shelf 인덱스의 재료 자루가 수상한 색(빨강)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="{w}" height="{h}" rx="4" fill="#8B5E3C"/>'
    shelf_h = h / n
    for i in range(n):
        yy = i * shelf_h
        out += f'<rect x="4" y="{yy + 4}" width="{w - 8}" height="{shelf_h - 10}" fill="#5A3B22" opacity="0.3"/>'
        sacks = 3
        for j in range(sacks):
            sx = 14 + j * (w - 28) / (sacks - 1 if sacks > 1 else 1)
            bad = (i == bad_shelf and j == 1)
            c = "var(--bad)" if bad else "#C9A86A"
            out += f'<ellipse cx="{sx}" cy="{yy + shelf_h - 14}" rx="12" ry="10" fill="{c}"/>'
    return out + '</g>'


def recipebook(x, y, s=1.0, open_book=False, locked=True):
    """비밀 레시피북 (모델 가중치 / 시스템 프롬프트)."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    if open_book:
        out += '<path d="M-32 -24 h30 v48 h-30z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
        out += '<path d="M2 -24 h30 v48 h-30z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
        out += '<path d="M-26 -14 h20 M-26 -4 h20 M-26 6 h14 M8 -14 h20 M8 -4 h20 M8 6 h14" stroke="#142033" stroke-width="2"/>'
    else:
        out += '<rect x="-28" y="-34" width="56" height="68" rx="3" fill="#7A1F17"/>'
        out += '<rect x="-28" y="-34" width="56" height="10" rx="3" fill="#9A3B2E"/>'
        if locked:
            out += '<rect x="-9" y="-4" width="18" height="16" rx="2" fill="#E9B44C"/><circle cx="0" cy="-4" r="6" fill="none" stroke="#E9B44C" stroke-width="3"/>'
    return out + '</g>'


def knifedrawer(x, y, s=1.0, locked=True, labels=None):
    """잠긴 칼 서랍 (도구 샌드박스/권한). labels 는 서랍 칸마다 붙인 도구 이름."""
    n = len(labels) if labels else 3
    w = 170
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="{w}" height="40" rx="3" fill="#5A3B22"/>'
    cw = w / n
    for i in range(n):
        cx = i * cw
        out += f'<rect x="{cx + 4}" y="4" width="{cw - 8}" height="32" rx="2" fill="#8B5E3C"/>'
        out += f'<circle cx="{cx + cw / 2}" cy="20" r="3" fill="#E9B44C"/>'
        if labels:
            out += label(cx + cw / 2, 54, labels[i], 10, "var(--muted)")
    if locked:
        out += f'<rect x="{w / 2 - 14}" y="-14" width="28" height="22" rx="4" fill="var(--bad)"/><circle cx="{w / 2}" cy="-14" r="8" fill="none" stroke="var(--bad)" stroke-width="4"/>'
    return out + '</g>'


def bell(x, y, s=1.0, ringing=False):
    """비상벨 (AI 사고 대응)."""
    c = "var(--bad)" if ringing else "#C9A86A"
    out = (f'<g transform="translate({x},{y}) scale({s})"><path d="M-18 10 a18 18 0 0 1 36 0 Z" fill="{c}"/>'
           f'<rect x="-22" y="8" width="44" height="6" rx="3" fill="#8B5E3C"/><circle cy="20" r="4" fill="#8B5E3C"/>')
    if ringing:
        out += '<path d="M-26 -6 q-6 6 0 12 M26 -6 q6 6 0 12" stroke="var(--bad)" stroke-width="3" fill="none"/>'
    return out + '</g>'


def logbook(x, y, s=1.0, w=100, h=70, rows=3):
    """주문 기록 장부 (감사 로그)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    for i in range(rows):
        yy = 16 + i * (h - 24) / max(1, rows - 1)
        out += f'<path d="M10 {yy} h{w - 20}" stroke="#142033" stroke-width="2"/>'
    return out + '</g>'


def board(x, y, w, h, title, rows, s=1.0, hl=-1):
    """주방 규칙판 / 안내판 — 크림 종이, 사이트 공통 스타일. 글자는 #142033 고정."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 12, "#142033", "start")
    return out + '</g>'


def badge(x, y, s=1.0):
    """위생 검사관 배지 (레드팀/감사)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -16 l14 8 v16 l-14 8 l-14 -8 v-16z" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>'
            f'<circle r="6" fill="#FFF8E7"/></g>')


def stamp(x, y, s=1.0, color="var(--good)"):
    """표식/도장 (워터마크 · 출처 인증)."""
    return (f'<g transform="translate({x},{y}) scale({s}) rotate(-12)"><circle r="20" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<path d="M-9 0 l6 7 l12 -16" stroke="{color}" stroke-width="4" fill="none" stroke-linecap="round"/></g>')
