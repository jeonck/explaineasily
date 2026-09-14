from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
COOK = dict(hat="var(--accent)", shirt="#4A5A72")
SMITH = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def crate(x, y, w=90, h=70, s=1.0, extra=""):
    """왼쪽 위 (x,y) 짐칸. 가로 판자 세 줄."""
    planks = "".join(f'<path d="M0 {h * k:.0f} h{w}" stroke="#5A3B22" stroke-width="3"/>' for k in (0.33, 0.66))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="{WOOD}" stroke="#5A3B22" stroke-width="3"/>{planks}'
            f'<rect x="{w / 2 - 6}" y="-6" width="12" height="8" fill="#5A3B22"/>{extra}</g>')


def mold(x, y, s=1.0, sealed=None, bug=False):
    """짐칸을 찍어내는 틀 — 액자 모양."""
    st = f'<circle cx="34" cy="-22" r="10" fill="{sealed}"/><path d="M29 -22 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none"/>' if sealed else ""
    b = bug_icon(0, 0, 0.8) if bug else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-44" y="-30" width="88" height="60" rx="4" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="5"/>'
            f'<rect x="-30" y="-18" width="60" height="36" rx="3" fill="{WOOD}" opacity="0.6"/>{b}{st}</g>')


def bug_icon(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="9" ry="12" fill="var(--bad)"/><circle cy="-13" r="5" fill="var(--night)"/>'
            f'<path d="M-9 -4 l-7 -5 M-9 4 l-8 2 M9 -4 l7 -5 M9 4 l8 2" stroke="var(--night)" stroke-width="2" stroke-linecap="round"/><path d="M0 -8 v16" stroke="var(--night)" stroke-width="2"/></g>')


def key_icon(x, y, s=1.0, color="#E9B44C"):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="8" fill="none" stroke="{color}" stroke-width="4"/><rect x="7" y="-2" width="20" height="4" fill="{color}"/><rect x="20" y="2" width="3" height="5" fill="{color}"/><rect x="14" y="2" width="3" height="4" fill="{color}"/></g>'


def crown_key(x, y, s=1.0):
    return key_icon(x, y, s) + f'<path d="M{x - 10} {y - 14} l3 -8 l4 5 l3 -7 l3 7 l4 -5 l3 8z" fill="#E9B44C" stroke="#C9822B" stroke-width="1.5"/>'


def fence(x, y, w, h, color="var(--good)"):
    posts = "".join(f'<rect x="{x + i * 14}" y="{y}" width="5" height="{h}" rx="2" fill="{color}"/>' for i in range(int(w / 14) + 1))
    return posts + f'<rect x="{x}" y="{y + 8}" width="{w}" height="4" fill="{color}"/><rect x="{x}" y="{y + h - 12}" width="{w}" height="4" fill="{color}"/>'


def glass(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="var(--sky)" fill-opacity="0.6" stroke="var(--stone-dark)" stroke-width="5"/><path d="M12 12 l16 16" stroke="var(--stone-dark)" stroke-width="7" stroke-linecap="round"/></g>'


def board(x, y, w, h, title, rows):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


ARROW = '<path d="M{x} {y} h{l}" stroke="var(--muted)" stroke-width="4" stroke-linecap="round"/><path d="M{x2} {y0} l10 10 l-10 10" stroke="var(--muted)" stroke-width="4" fill="none" stroke-linecap="round"/>'


def arrow(x, y, l=40):
    return ARROW.format(x=x, y=y, l=l, x2=x + l - 10, y0=y - 10)


# 1. 부엌 한 칸을 짐칸에 담으면 어디서든 똑같이
P1 = svg(320, sky(320)
         + '<rect x="40" y="90" width="160" height="140" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + person(70, 110, s=0.7, face=SMILE, **COOK)
         + '<rect x="130" y="170" width="50" height="34" rx="6" fill="var(--stone-dark)"/><path d="M125 170 h60" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>' + label(120, 254, "⟦부엌 한 칸|one kitchen⟧", 11, "var(--ink)", cls="d")
         + arrow(212, 160) + crate(280, 120, 120, 110) + person(315, 135, s=0.5, face=SMILE, **COOK) + label(340, 254, "⟦짐칸에 담아요|packed in a crate⟧", 11, "var(--ink)", cls="d")
         + arrow(412, 160)
         + "".join(small_castle(x - 24, 70, 0.3) + crate(x - 35, 150, 70, 60) for x in (500, 590, 680)) + label(590, 254, "⟦세 성에 똑같이|the same in three castles⟧", 11, "var(--ink)", cls="d")
         + label(380, 300, "⟦짐칸 하나면 어디서든 똑같은 부엌이 펼쳐져요|one crate, and the same kitchen unfolds anywhere⟧", 12, "var(--ink)"))

# 2. 편한 만큼 한 번에 다 잘못돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + mold(130, 80, 0.9, bug=True) + "".join(crate(70 + i * 44, 140, 36, 30, extra=bug_icon(18, 15, 0.45)) for i in range(3))
         + label(130, 225, "⟦틀에 벌레 하나면|one bug in the mold⟧", 12, "var(--ink)", cls="d") + label(130, 247, "⟦짐칸 백 개가 다 벌레|a hundred crates, all bugged⟧", 11, "var(--bad)")
         + crate(310, 90, 60, 80) + crate(392, 90, 60, 80) + person(360, 75, s=0.55, face=MASK, extra=BAG) + '<path d="M372 150 l-10 -14 l16 4 l-8 -14" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + label(380, 225, "⟦짐칸끼리 벽이 얇아요|thin walls between crates⟧", 12, "var(--ink)", cls="d") + label(380, 247, "⟦하나 뚫리면 옆으로 옮겨가요|break one, and move on to the next⟧", 11, "var(--bad)")
         + crate(560, 90, 90, 80) + crown_key(605, 132, 1.1) + person(660, 100, s=0.6, face=MASK)
         + label(630, 225, "⟦왕 열쇠를 넣어 뒀어요|the king\'s key left inside⟧", 12, "var(--ink)", cls="d") + label(630, 247, "⟦짐칸 하나가 성 전체 열쇠|one crate, the whole castle\'s key⟧", 11, "var(--bad)")
         + label(380, 285, "⟦편한 만큼, 한 번에 다 잘못될 수도 있어요|as easy as it is, it can all go wrong at once⟧", 12, "var(--muted)"))

# 3. 짐칸 규칙 넷 (hero)
P3 = svg(360, sky(360)
         + crate(70, 130, 180, 130) + glass(228, 168, 1.0) + '<circle cx="120" cy="165" r="18" fill="var(--good)"/><path d="M111 165 l6 6 l12 -13" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round"/>' + key_icon(110, 225, 0.8)
         + label(178, 236, "⟦작은 열쇠|small key⟧", 10, "#FFF8E7") + person(280, 140, s=0.9, face=SMILE, **GUARD)
         + board(420, 50, 290, 170, "⟦짐칸 규칙|CRATE RULES⟧", ("⟦1. 틀은 열기 전에 검사해요|1. inspect the mold before use⟧", "⟦2. 도장 찍힌 틀만 써요|2. only sealed molds⟧", "⟦3. 짐칸엔 작은 열쇠만|3. small keys only inside⟧", "⟦4. 관리인이 울타리를 세워요|4. the keeper fences each one⟧"))
         + label(160, 286, "⟦검사 끝난 짐칸|an inspected crate⟧", 11, "var(--muted)") + label(312, 286, "⟦짐칸 검사관|the crate inspector⟧", 11, "var(--muted)")
         + label(380, 318, "⟦짐칸은 열기 전에 검사하고, 작은 열쇠만 넣고, 관리인이 문단속해요|check the crate before opening, pack only a small key, and let the keeper lock up⟧", 12, "var(--ink)", cls="d")
         + label(380, 346, "⟦틀 하나를 고치면 짐칸 백 개가 같이 고쳐져요|fix the mold once, and a hundred crates are fixed with it⟧", 11, "var(--muted)"))

# 4. 대장간에서 마당까지
P4 = svg(320, sky(320)
         + '<rect x="60" y="130" width="80" height="50" rx="6" fill="var(--stone-dark)"/><rect x="50" y="120" width="100" height="14" rx="4" fill="var(--stone-dark)"/>' + person(120, 50, s=0.6, face=SMILE, **SMITH) + mold(100, 200, 0.5)
         + label(100, 246, "⟦대장간|the smithy⟧", 11, "var(--ink)", cls="d") + label(100, 264, "⟦틀을 만들어요|makes the mold⟧", 10, "var(--muted)")
         + arrow(170, 160, 30)
         + '<rect x="215" y="110" width="130" height="8" fill="#5A3B22"/><rect x="215" y="180" width="130" height="8" fill="#5A3B22"/>' + mold(250, 145, 0.5, sealed="var(--good)") + mold(315, 145, 0.5) + '<path d="M300 130 l30 30 M330 130 l-30 30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(280, 246, "⟦틀 창고|the mold store⟧", 11, "var(--ink)", cls="d") + label(280, 264, "⟦도장 찍힌 틀만|sealed molds only⟧", 10, "var(--muted)")
         + arrow(360, 160, 30)
         + crate(410, 125, 80, 70) + glass(475, 140, 0.8) + bug_icon(440, 160, 0.6) + '<path d="M425 145 l30 30 M455 145 l-30 30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(455, 246, "⟦검사|inspection⟧", 11, "var(--ink)", cls="d") + label(455, 264, "⟦벌레 있으면 돌려보내요|bugs go back⟧", 10, "var(--muted)")
         + arrow(510, 160, 30)
         + fence(560, 100, 70, 110) + crate(572, 140, 46, 40, 1.0) + fence(650, 100, 70, 110) + crate(662, 140, 46, 40, 1.0) + person(590, 30, s=0.55, face=SMILE, **BLUE)
         + label(640, 246, "⟦마당의 관리인|the yard keeper⟧", 11, "var(--ink)", cls="d") + label(640, 264, "⟦울타리마다 따로 두어요|each in its own pen⟧", 10, "var(--muted)")
         + label(380, 302, "⟦틀부터 마당까지 — 한 번에 백 개를 지키는 길이에요|from the mold to the yard — one path that guards a hundred crates at once⟧", 12, "var(--ink)", cls="d"))

# 5. 뚫어도 짐칸 하나뿐
P5 = svg(300, sky(300)
         + crate(50, 90, 90, 70, extra=bug_icon(45, 35, 0.7)) + '<path d="M40 80 l110 90 M150 80 l-110 90" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>' + label(95, 190, "⟦돌려보내요|sent back⟧", 11, "var(--bad)", cls="d")
         + fence(250, 60, 130, 130) + crate(272, 105, 86, 60) + person(295, 30, s=0.55, face=MASK + FROWN) + key_icon(315, 140, 0.6)
         + label(315, 218, "⟦뚫어도 짐칸 하나뿐|even if broken in, only one crate⟧", 11, "var(--ink)", cls="d") + label(315, 236, "⟦작은 열쇠뿐, 옆으로도 못 가요|a small key, and no way to the next⟧", 10, "var(--muted)")
         + person(520, 70, s=0.8, face=SMILE, hat="#E9B44C", shirt="#4A5A72") + mold(640, 110, 0.9, sealed="var(--good)") + "".join(crate(590 + i * 34, 165, 28, 24) for i in range(4))
         + label(620, 218, "⟦틀을 고치면 백 개가 새 짐칸|fix the mold, a hundred new crates⟧", 11, "var(--ink)", cls="d") + label(620, 236, "⟦목수가 판자를 대는 곳은 틀이에요|the carpenter fixes the mold, not the crate⟧", 10, "var(--muted)")
         + label(380, 280, "⟦짐칸은 고치지 않아요 — 틀을 고치고 새로 찍어내요|you don\'t patch a crate — you fix the mold and stamp out new ones⟧", 12, "var(--ink)", cls="d"))

SCAN_I = icon('<rect x="8" y="26" width="30" height="26" rx="3" fill="#8B5E3C"/><path d="M8 35 h30 M8 43 h30" stroke="#5A3B22" stroke-width="2"/><circle cx="42" cy="24" r="11" fill="var(--sky)" fill-opacity="0.6" stroke="var(--stone-dark)" stroke-width="4"/><path d="M50 32 l8 8" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>')
SEAL_I = icon('<rect x="10" y="14" width="44" height="36" rx="3" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="4"/><circle cx="44" cy="18" r="10" fill="var(--good)"/><path d="M39 18 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none"/>')
SMALLKEY_I = icon('<rect x="8" y="20" width="48" height="36" rx="3" fill="#8B5E3C"/><circle cx="24" cy="38" r="6" fill="none" stroke="#E9B44C" stroke-width="3"/><rect x="29" y="36" width="14" height="4" fill="#E9B44C"/><rect x="39" y="40" width="3" height="4" fill="#E9B44C"/>')
FENCE_I = icon('<rect x="20" y="30" width="24" height="18" rx="2" fill="#8B5E3C"/>' + "".join(f'<rect x="{8 + i * 12}" y="14" width="4" height="40" rx="2" fill="var(--good)"/>' for i in range(5)) + '<rect x="8" y="20" width="52" height="3" fill="var(--good)"/><rect x="8" y="46" width="52" height="3" fill="var(--good)"/>')

PAGE = {
    "slug": "container", "order": 90,
    "title": ("똑같이 찍어낸 짐칸", "Crates from the Same Mold"),
    "h1": ("<em>컨테이너 보안</em>이 뭐예요?", "What is <em>Container Security</em>?"),
    "sub": ("컨테이너·쿠버네티스 보안(Container & Kubernetes Security)을 방 하나를 통째로 담아 어디서든 똑같이 펼치는 짐칸 이야기로 풀어봤어요.",
            "Container and Kubernetes security, told as a story about crates that pack up a whole room and unfold it the same way anywhere."),
    "panels": [
        {"svg": P1, "alt": ("요리사가 있는 부엌 한 칸 → 화살표 → 요리사째 담긴 짐칸 → 화살표 → 세 개의 작은 성 아래 똑같은 짐칸 셋", "A kitchen with a cook → arrow → a crate with the cook packed inside → arrow → three identical crates under three small castles"),
         "caption": ("부엌 한 칸을 통째로 짐칸에 담으면, 어디서든 똑같이 펼쳐져요.", "Pack a whole kitchen into a crate, and it unfolds the same way anywhere."),
         "small": ("요리사, 솥, 조리법까지 한 짐칸에요. 옆 성에 보내도, 빌린 창고에 보내도 똑같은 부엌이 나와요. 그래서 다들 짐칸을 써요.", "The cook, the pot, the recipes — all in one crate. Send it to the next castle or to a rented storehouse, and the same kitchen appears. That\'s why everyone uses crates.")},
        {"svg": P2, "alt": ("벌레가 든 틀과 그 틀로 찍은 벌레 짐칸 셋. 붙어 있는 두 짐칸 사이를 도둑이 뚫고 지나감. 왕관 달린 금열쇠가 든 짐칸 옆에 도둑", "A mold with a bug inside and three bugged crates stamped from it. A thief breaking through the thin wall between two adjoining crates. A crate holding a golden crowned key, with a thief beside it"),
         "caption": ("편한 만큼, 한 번에 다 잘못될 수도 있어요.", "As easy as it is, it can all go wrong at once."),
         "small": ('틀에 <a href="supplychain-ko.html">벌레</a>가 하나 있으면 짐칸 백 개가 다 벌레예요. 짐칸끼리 벽이 얇아서 하나 뚫리면 옆으로 옮겨가요. 짐칸에 왕 열쇠를 넣어 두면 짐칸 하나가 성 전체 열쇠가 돼요.',
                   'One <a href="supplychain-en.html">bug</a> in the mold, and all hundred crates are bugged. The walls between crates are thin, so break one and you reach the next. Leave the king\'s key inside, and one crate becomes the key to the whole castle.')},
        {"svg": P3, "hero": True, "alt": ("돋보기로 검사한 큰 짐칸에 초록 체크와 작은 열쇠. 초록 검사관이 웃고 있음. 오른쪽 판자에 짐칸 규칙 넷: 틀은 열기 전에 검사, 도장 찍힌 틀만, 짐칸엔 작은 열쇠만, 관리인이 울타리를 세움", "A big crate inspected with a magnifying glass, marked with a green check and holding a small key. A green inspector smiles. A board on the right lists four crate rules: inspect the mold before use, only sealed molds, small keys only inside, the keeper fences each one"),
         "caption": ("컨테이너 보안은 짐칸을 열기 전에 검사하고, 작은 열쇠만 넣고, 관리인이 문단속하는 거예요.", "Container security is checking a crate before it opens, packing only a small key, and letting the keeper lock up."),
         "small": ("틀에 벌레가 없는지 보고, 믿는 대장간의 도장이 찍힌 틀만 쓰고, 짐칸엔 왕 열쇠 대신 작은 열쇠만 넣고, 마당의 관리인이 짐칸마다 울타리를 세워요.", "Look for bugs in the mold, use only molds sealed by a trusted smithy, pack a small key instead of the king\'s, and let the yard keeper fence every crate."),
         "tricks": (4, [
             (SCAN_I, ("틀 검사", "Inspect the mold"), ("벌레 있으면 돌려보내요", "bugs go back"), "warm"),
             (SEAL_I, ("도장 찍힌 틀만", "Sealed molds only"), ("믿는 대장간 것만", "from a trusted smithy")),
             (SMALLKEY_I, ("작은 열쇠만", "Small keys only"), ("왕 열쇠는 절대 안 넣어요", "never the king\'s"), "warm"),
             (FENCE_I, ("울타리마다 따로", "A pen for each"), ("관리인이 세워요", "the keeper builds it"), "calm"),
         ])},
        {"svg": P4, "alt": ("네 단계: 대장간에서 틀을 만들고 → 틀 창고엔 초록 도장 찍힌 틀만(도장 없는 틀엔 X) → 돋보기 검사에서 벌레 짐칸에 X → 마당의 파란 관리인이 울타리 두 개에 짐칸을 하나씩 둠", "Four stages: the smithy makes the mold → the mold store keeps only green-sealed molds (an X on the unsealed one) → inspection puts an X on a bugged crate → the blue yard keeper places one crate in each of two pens"),
         "caption": ("틀부터 마당까지, 한 길로 이어져요.", "From the mold to the yard, it\'s one path."),
         "small": ('대장간이 틀을 만들고, 도장 찍힌 틀만 창고에 두고, 검사에서 <a href="codescan-ko.html">벌레와 틈</a>을 찾고, 마당의 관리인이 짐칸마다 <a href="sandbox-ko.html">울타리</a>를 세워요. 틀 안에 뭐가 들었는지는 <a href="sbom-ko.html">부품 목록표</a>가 말해줘요.',
                   'The smithy makes the mold, only sealed molds go in the store, inspection finds <a href="codescan-en.html">bugs and cracks</a>, and the yard keeper builds a <a href="sandbox-en.html">pen</a> for every crate. What\'s inside the mold, the <a href="sbom-en.html">parts list</a> tells you.')},
        {"svg": P5, "alt": ("벌레 짐칸에 큰 X — 돌려보냄. 울타리 안 짐칸에 들어간 도둑은 찡그리고, 손엔 작은 열쇠뿐. 목수가 도장 찍힌 틀을 고치자 새 짐칸 넷이 줄지어 나옴", "A big X on a bugged crate — sent back. A thief inside a fenced crate frowns, holding only a small key. The carpenter fixes the sealed mold and four new crates roll out"),
         "caption": ("짐칸은 고치지 않아요. 틀을 고치고 새로 찍어내요.", "You don\'t patch a crate. You fix the mold and stamp out new ones."),
         "small": ('도둑이 짐칸 하나를 뚫어도 <a href="sandbox-ko.html">울타리</a> 안이고 손엔 <a href="leastprivilege-ko.html">작은 열쇠</a>뿐이에요. <a href="patch-ko.html">목수</a>가 판자를 대는 곳은 짐칸이 아니라 틀이에요 — 그러면 백 개가 한 번에 새것이 돼요.',
                   'Even if a thief breaks into one crate, it\'s inside a <a href="sandbox-en.html">pen</a> and holds only a <a href="leastprivilege-en.html">small key</a>. The <a href="patch-en.html">carpenter</a> boards up the mold, not the crate — and a hundred crates become new at once.')},
    ],
    "summary": (("<b>컨테이너 보안</b> = 방 하나를 통째로 담는 짐칸을, <b>틀부터 검사하고</b>, <b>도장 찍힌 틀만 쓰고</b>, <b>작은 열쇠만 넣고</b>, 마당의 <b>관리인이 울타리를 세우는</b> 일.",
                 "<b>Container security</b> = for crates that pack a whole room, <b>inspect the mold first</b>, <b>use only sealed molds</b>, <b>pack only a small key</b>, and let the yard <b>keeper fence each one</b>."),
                ("Container & Kubernetes Security. 이미지 스캔, 신뢰할 수 있는 레지스트리와 이미지 서명, 루트 실행 금지와 최소 권한, 네임스페이스·네트워크 정책으로 격리, 그리고 런타임 감시까지. 이미지가 곧 '틀'이라 이미지를 고치면 모든 컨테이너가 함께 고쳐져요.",
                 "Image scanning, trusted registries with image signing, no root and least privilege, isolation through namespaces and network policies, and runtime monitoring. The image is the mold — fix the image, and every container is fixed with it.")),
    "glossary": [
        ("컨테이너", "Container", ("짐칸.", "The crate."), ("방 하나를 통째로 담아 어디서든 똑같이 펼쳐요. 빌린 창고에서도요.", "Packs a whole room and unfolds it the same anywhere — even in a rented storehouse.")),
        ("이미지", "Image", ("짐칸을 찍어내는 틀.", "The mold that stamps out crates."), ("틀 하나로 짐칸 백 개. 틀에 벌레가 있으면 백 개가 다 벌레예요.", "One mold, a hundred crates. A bug in the mold is a bug in all hundred.")),
        ("레지스트리", "Registry", ("틀 창고.", "The mold store."), ('도장 찍힌 틀만 두어요. 도장은 → <a href="pki-ko.html">믿는 대장간의 도장</a>, 부품은 → <a href="sbom-ko.html">부품 목록표</a>', 'Only sealed molds go in. The seal → <a href="pki-en.html">a trusted smithy\'s stamp</a>; the parts → <a href="sbom-en.html">the parts list</a>')),
        ("이미지 스캔", "Image scanning", ("틀 검사.", "Mold inspection."), ('열기 전에 벌레와 틈을 찾아요. → <a href="codescan-ko.html">틀 검사</a> · <a href="vulnmgmt-ko.html">매달 도는 틈 장부</a>', 'Find bugs and cracks before it opens. → <a href="codescan-en.html">inspecting the mold</a> · <a href="vulnmgmt-en.html">the monthly ledger of cracks</a>')),
        ("루트 실행 금지", "No root", ("작은 열쇠만.", "Small keys only."), ('짐칸 안에서 왕 열쇠를 돌리면 짐칸 하나가 성 전체 열쇠예요. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'Turn the king\'s key inside a crate, and that crate is the key to the whole castle. → <a href="leastprivilege-en.html">only the keys you need</a>')),
        ("쿠버네티스", "Kubernetes", ("마당의 짐칸 관리인.", "The yard keeper."), ('짐칸 수백 개를 어디 둘지, 몇 개 둘지, 울타리는 어디 칠지 정해요. 관리인의 문단속은 → <a href="cspm-ko.html">빌린 창고 문단속</a>', 'Decides where hundreds of crates go, how many, and where the fences run. The keeper\'s lock-up → <a href="cspm-en.html">locking up the rented storehouse</a>')),
        ("네임스페이스 · 격리", "Namespace · isolation", ("울타리.", "The pen."), ('짐칸끼리 벽이 얇아서 관리인이 울타리를 따로 세워요. → <a href="sandbox-ko.html">창문 없는 빈 방</a>', 'Crate walls are thin, so the keeper builds each its own pen. → <a href="sandbox-en.html">the empty room with no windows</a>')),
        ("런타임 보안", "Runtime security", ("펼친 뒤에도 지켜보기.", "Watching after it unfolds."), ('짐칸이 갑자기 이상한 짓을 하면 종이 울려요. → <a href="edr-ko.html">방마다 한 마리 경비견</a>', 'If a crate suddenly acts strangely, the bell rings. → <a href="edr-en.html">a guard dog in every room</a>')),
    ],
}
