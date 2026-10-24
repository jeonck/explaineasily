"""PPE·DB/데이터 분야 전용 그림 조각. `from _draw import *` 다음 `from _world import *`."""
from _draw import *

MANAGER = dict(hat="#7B3FA0", shirt="#4A5A72")    # 창고 관리자 = DBA
SORTER = dict(hat="#5B8DEF", shirt="#2E3D57")     # 분류 담당 = 데이터 모델러
PACKER = dict(hat="#2E8B57", shirt="#2E8B57")     # 포장 담당 = 애플리케이션
DRIVER = dict(hat="#C9822B", shirt="#4A5A72")     # 배송 기사 = 클라이언트 요청
AUDITOR = dict(hat="#E9B44C", shirt="#4A5A72")    # 재고 감사원 = 감사/정합성 점검


def shelfzone(x, y, w, h, s=1.0, n=4, bad=-1, label_text=None):
    """구역별 선반(샤딩/파티셔닝). bad 인덱스 칸은 문제 표시."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="3" fill="#8B5E3C"/>'
    cw = w / n
    for i in range(n):
        c = "var(--bad)" if i == bad else "#C9A86A"
        out += f'<rect x="{i * cw + 4}" y="6" width="{cw - 8}" height="{h - 12}" rx="2" fill="{c}"/>'
    if label_text:
        out += label(w / 2, -10, label_text, 11, "var(--muted)")
    return out + '</g>'


def box(x, y, s=1.0, color="#E9B44C", twin=False):
    """재고 상자 한 개. twin=True 면 바로 옆에 복제 상자."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-16" width="36" height="32" rx="3" fill="{color}" stroke="#8B5E3C" stroke-width="2"/><path d="M-18 -4 h36" stroke="#8B5E3C" stroke-width="2"/>'
    if twin:
        out += f'<rect x="22" y="-16" width="36" height="32" rx="3" fill="{color}" stroke="#8B5E3C" stroke-width="2" opacity="0.6"/>'
    return out + '</g>'


def receipt(x, y, s=1.0, text=None, void=False):
    """출납 전표(트랜잭션)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-28" width="44" height="56" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    out += '<path d="M-14 -14 h28 M-14 -4 h28 M-14 6 h20" stroke="#142033" stroke-width="2"/>'
    if void:
        out += '<path d="M-18 -24 L18 24 M18 -24 L-18 24" stroke="var(--bad)" stroke-width="3"/>'
    if text:
        out += label(0, 42, text, 10, "var(--muted)")
    return out + '</g>'


def fastdesk(x, y, s=1.0, label_text=None):
    """특급 출고대(인메모리/캐시)."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-34" y="-8" width="68" height="20" rx="4" fill="var(--accent)"/>'
           f'<path d="M-24 -8 l6 -10 l6 10 M-4 -8 l6 -10 l6 10" stroke="#FFF8E7" stroke-width="3" fill="none"/></g>')
    if label_text:
        out += label(x, y + 24 * s, label_text, 11, "var(--muted)")
    return out


def indexcard(x, y, s=1.0, tags=None):
    """다차원 색인 카드(여러 딱지가 붙은 카드)."""
    tags = tags or ["A", "B"]
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-14" width="40" height="28" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    for i, t in enumerate(tags):
        out += f'<rect x="{-20 + i * 14}" y="-24" width="12" height="12" rx="2" fill="var(--accent)"/>' + label(-14 + i * 14, -16, t, 8, "#fff")
    return out + '</g>'
