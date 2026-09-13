"""그림책 페이지가 같이 쓰는 SVG 조각들. 색은 전부 CSS 토큰이라 다크 모드에서도 맞는다."""

SKIN = "#E8C9A8"
EYES = '<circle cx="22" cy="28" r="3" fill="var(--night)"/><circle cx="38" cy="28" r="3" fill="var(--night)"/>'
SMILE = EYES + '<path d="M20 38 Q30 46 40 38" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/>'
FROWN = EYES + '<path d="M20 42 Q30 34 40 42" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/>'
MASK = '<path d="M14 26 h32 v10 h-32 z" fill="#111C30"/>'
SWEAT = '<path d="M58 22 q6 8 0 14 q-6 -6 0 -14z" fill="#5B9BD5"/><path d="M64 34 q5 7 0 12 q-5 -5 0 -12z" fill="#5B9BD5"/>'


def svg(h, inner):
    return f'<svg viewBox="0 0 760 {h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


def person(x, y, hat="var(--bad)", shirt="#2E3D57", s=1.0, face="", extra=""):
    """머리 중심 (30,30), 몸통 아래 끝 y=112 인 사람. hat=None 이면 모자 없음."""
    hat_svg = f'<path d="M6 22 Q30 -6 54 22 Z" fill="{hat}"/>' if hat else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cx="30" cy="30" r="22" fill="{SKIN}"/>'
            f'{hat_svg}<rect x="8" y="52" width="44" height="60" rx="10" fill="{shirt}"/>{face}{extra}</g>')


def sky(h, ground=True):
    g = f'<ellipse cx="380" cy="{h}" rx="440" ry="36" fill="var(--good-soft)"/>' if ground else ""
    return f'<rect width="760" height="{h}" fill="var(--sky)"/>{g}'


def night(h):
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#F5E6B8"/>'
                    for x, y in ((120, 40), (300, 70), (500, 30), (420, 90), (200, 120)))
    return (f'<rect width="760" height="{h}" fill="var(--night)"/><circle cx="660" cy="50" r="26" fill="#F5E6B8"/>'
            f'{stars}<ellipse cx="380" cy="{h + 10}" rx="440" ry="30" fill="#0A1120"/>')


def battlements(x, y, w, n, color, h=24):
    step = w / n
    bw = step * 0.5
    return "".join(f'<rect x="{x + i * step:.0f}" y="{y}" width="{bw:.0f}" height="{h}" fill="{color}"/>' for i in range(n))


def castle(x=150, y=70, s=1.0):
    """두 탑과 가운데 성벽, 문. 원본 폭 460, 높이 200 (y=70 에서 270)."""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="0" y="20" width="90" height="180" fill="var(--stone)"/>'
            f'<rect x="370" y="20" width="90" height="180" fill="var(--stone)"/>'
            f'{battlements(0, 0, 90, 3, "var(--stone)")}{battlements(370, 0, 90, 3, "var(--stone)")}'
            f'<rect x="90" y="70" width="280" height="130" fill="var(--stone-dark)"/>'
            f'{battlements(90, 50, 280, 5, "var(--stone-dark)")}'
            f'<path d="M195 200 V140 a35 35 0 0 1 70 0 V200 Z" fill="var(--night)"/>'
            f'<rect x="34" y="60" width="22" height="34" rx="11" fill="var(--night)"/>'
            f'<rect x="404" y="60" width="22" height="34" rx="11" fill="var(--night)"/>'
            f'<rect x="228" y="-30" width="4" height="100" fill="var(--night)"/>'
            f'<path d="M232 -28 L290 -12 L232 4 Z" fill="var(--accent)"/></g>')


def small_castle(x, y, s=0.5):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="0" y="40" width="160" height="110" fill="var(--stone-dark)"/>'
            f'{battlements(0, 20, 160, 4, "var(--stone-dark)")}'
            f'<path d="M60 150 V110 a20 20 0 0 1 40 0 V150 Z" fill="var(--night)"/></g>')


def foot(x, y, rot=0, color="#7A5236"):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><ellipse rx="9" ry="14" fill="{color}"/>'
            f'<ellipse cy="-20" rx="7" ry="6" fill="{color}"/></g>')


def label(x, y, text, size=18, fill="var(--ink)", anchor="middle", cls="", weight=700):
    c = f' class="{cls}"' if cls else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}"{c}>{text}</text>'


def bubble(x, y, w, h, text, size=17, fill="var(--panel)", stroke="var(--line)", tail="left"):
    """말풍선. tail 은 꼬리가 붙는 쪽 (left/right/bottom)."""
    tails = {
        "left": f'<path d="M{x + 18} {y + h} l-14 16 l24 -16z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
        "right": f'<path d="M{x + w - 18} {y + h} l14 16 l-24 -16z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
        "bottom": f'<path d="M{x + w / 2 - 10} {y + h} l10 16 l10 -16z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
    }
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            f'{tails[tail]}<rect x="{x + 2}" y="{y + h - 4}" width="{w - 4}" height="6" fill="{fill}"/>'
            f'{label(x + w / 2, y + h / 2 + size * 0.36, text, size)}')


def shield(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M90 0 L180 30 V100 C180 150 140 185 90 200 C40 185 0 150 0 100 V30 Z" fill="var(--good)"/>'
            f'<path d="M90 18 L162 42 V100 C162 138 132 166 90 180 C48 166 18 138 18 100 V42 Z" fill="var(--panel)"/>'
            f'<rect x="62" y="90" width="56" height="44" rx="8" fill="var(--night)"/>'
            f'<path d="M72 90 V76 a18 18 0 0 1 36 0 V90" stroke="var(--night)" stroke-width="8" fill="none"/>'
            f'<circle cx="90" cy="110" r="6" fill="var(--accent)"/></g>')


def icon(inner):
    return f'<svg viewBox="0 0 64 64" aria-hidden="true">{inner}</svg>'


def dot_icon(color):
    return icon(f'<circle cx="32" cy="32" r="22" fill="{color}" stroke="var(--line)" stroke-width="3"/>')


FUR = "#A9744F"


def dog(x, y, s=1.0, bark=False, asleep=False):
    eyes = ('<path d="M-32 -12 h8 M-22 -12 h8" stroke="var(--night)" stroke-width="2.5" stroke-linecap="round"/>' if asleep
            else '<circle cx="-30" cy="-12" r="2.5" fill="var(--night)"/><circle cx="-20" cy="-12" r="2.5" fill="var(--night)"/>')
    woof = (label(-40, -46, "⟦멍!|WOOF!⟧", 20, "var(--accent)", cls="d")
            + '<path d="M-6 -36 l6 -8 M2 -30 l9 -4" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>') if bark else ""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M26 12 q16 -18 8 -30" stroke="{FUR}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="8" rx="30" ry="17" fill="{FUR}"/>'
            f'<rect x="-22" y="18" width="9" height="16" rx="4" fill="{FUR}"/><rect x="10" y="18" width="9" height="16" rx="4" fill="{FUR}"/>'
            f'<circle cx="-26" cy="-8" r="16" fill="{FUR}"/>'
            f'<path d="M-40 -18 q-10 10 -6 26 q8 -4 10 -16z" fill="#7A5236"/>'
            f'<ellipse cx="-36" cy="-2" rx="5" ry="3.5" fill="var(--night)"/>{eyes}'
            f'<rect x="-18" y="-2" width="14" height="6" rx="3" fill="var(--accent)"/>{woof}</g>')


WOOD = "#8B5E3C"


def corridor(h, doors, night_mode=False, marks=True):
    """가로로 긴 복도. doors 는 (이름, 개 있음) 튜플 다섯 개. marks=True 면 개가 있는 문엔 개, 없는 문엔 물음표."""
    wall = "var(--night)" if night_mode else "var(--panel)"
    floor = "#0A1120" if night_mode else "var(--stone)"
    ink = "#C9D5E6" if night_mode else "var(--muted)"
    out = (f'<rect width="760" height="{h}" fill="{wall}"/><rect y="190" width="760" height="{h - 190}" fill="{floor}"/>'
           f'<rect y="186" width="760" height="6" fill="var(--stone-dark)"/>')
    for i, (name, has_dog) in enumerate(doors):
        x = 70 + i * 140
        out += (f'<rect x="{x}" y="80" width="64" height="110" rx="3" fill="{WOOD}"/><circle cx="{x + 52}" cy="138" r="4" fill="#E9B44C"/>'
                + label(x + 32, 66, name, 13, ink))
        if marks:
            out += dog(x + 32, 168, 0.4) if has_dog else label(x + 32, 150, "?", 30, "var(--accent)", cls="d")
    return out


def gate(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="30" width="140" height="90" fill="var(--stone-dark)"/>'
            f'{battlements(-70, 10, 140, 4, "var(--stone-dark)", 20)}<path d="M-28 120 V78 a28 28 0 0 1 56 0 V120 Z" fill="var(--night)"/></g>')
