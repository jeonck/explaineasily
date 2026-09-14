from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
SPYGLASS = '<g transform="translate(56,52) rotate(-35)"><rect x="-4" y="0" width="8" height="30" rx="3" fill="#5A3B22"/><rect x="-6" y="-8" width="12" height="10" rx="2" fill="#C9A86A"/></g>'


def door(x, y, s=1.0, color=WOOD, mark=None):
    m = ""
    if mark == "?":
        m = label(0, 6, "?", 22, "var(--accent)", cls="d")
    elif mark == "x":
        m = '<path d="M-12 -12 l24 24 M12 -12 l-24 24" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
    elif mark == "tag":
        m = '<rect x="-14" y="-6" width="28" height="12" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-32" width="36" height="64" rx="3" fill="{color}"/><circle cx="10" cy="2" r="3" fill="#E9B44C"/>{m}</g>'


def shed(x, y, s=1.0, faded=False):
    op = ' opacity="0.55"' if faded else ""
    return (f'<g transform="translate({x},{y}) scale({s})"{op}><rect x="-36" y="-20" width="72" height="50" rx="3" fill="var(--stone)"/>'
            f'<path d="M-42 -20 h84 l-42 -24z" fill="var(--stone-dark)"/><rect x="-10" y="4" width="20" height="26" fill="var(--stone-dark)"/></g>')


def map_paper(x, y, w, h, title, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))


def mini_castle(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="-30" width="120" height="60" fill="var(--stone-dark)"/>'
            f'<rect x="-70" y="-44" width="24" height="74" fill="var(--stone)"/><rect x="46" y="-44" width="24" height="74" fill="var(--stone)"/></g>')


def sign(x, y, text, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-3" y="0" width="6" height="40" fill="#5A3B22"/>'
            f'<rect x="-40" y="-22" width="80" height="24" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{label(0, -6, text, 10, "#142033")}</g>')


# 1. 안에서 본 지도엔 문이 다섯 — 그런데 도둑은 바깥에서 봐요
P1 = svg(320, sky(320)
         + map_paper(40, 40, 220, 200, "⟦안에서 그린 지도|MAP FROM INSIDE⟧") + mini_castle(110, 110, 0.7)
         + "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="#E9B44C"/>' for x, y in ((80, 104), (106, 104), (132, 104), (66, 130), (146, 130)))
         + label(110, 175, "⟦문 5개|5 doors⟧", 14, "#142033", cls="d") + "</g>"
         + person(150, 250, s=0.5, face=SMILE, **GUARD)
         + castle(330, 60, 0.55) + shed(620, 200, 0.8) + door(700, 230, 0.6) + '<rect x="600" y="120" width="60" height="70" rx="3" fill="var(--stone)" opacity="0.7"/>' + door(630, 165, 0.5, mark=None)
         + person(680, 60, s=0.7, face=MASK, extra=SPYGLASS) + label(700, 150, "⟦도둑은 바깥에서 봐요|the thief looks from outside⟧", 11, "var(--bad)")
         + label(520, 300, "⟦담 너머엔 지도에 없는 문이 더 있어요|beyond the wall are doors the map doesn\'t show⟧", 12, "var(--ink)"))

# 2. 잊힌 문들
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + door(100, 110, 1.0, color="#6B4A2E") + '<path d="M70 60 q30 -20 60 0" stroke="var(--stone-dark)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>' + label(100, 200, "⟦옛날 목수가 낸 뒷문|an old back door⟧", 11, "var(--ink)") + label(100, 220, "⟦아무도 안 잠가요|nobody locks it now⟧", 10, "var(--muted)")
         + door(280, 110, 1.0, color="#7B3FA0") + person(330, 50, s=0.5, hat="#E9B44C", shirt="#7B3FA0", face=SMILE) + label(280, 200, "⟦셋째 왕자가 몰래 낸 문|a door the third prince made⟧", 11, "var(--ink)") + label(280, 220, "⟦경비실은 몰라요|the guard room never knew⟧", 10, "var(--muted)")
         + shed(470, 120, 1.0) + label(470, 200, "⟦마을에 빌린 창고|a rented shed in the village⟧", 11, "var(--ink)") + label(470, 220, "⟦우리 상자가 들어 있어요|with our chests inside⟧", 10, "var(--muted)")
         + sign(650, 100, "⟦→ 서쪽 창고|→ west shed⟧") + '<path d="M620 170 l60 0" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="4 4"/>' + label(650, 200, "⟦이름표만 남은 길|a signpost to nowhere⟧", 11, "var(--ink)") + label(650, 220, "⟦창고는 없어졌는데|the shed is gone⟧", 10, "var(--muted)")
         + label(380, 280, "⟦성이 크면 잊힌 문이 생겨요 — 도둑은 그 문부터 찾아요|a big castle has forgotten doors — and the thief looks for those first⟧", 12, "var(--bad)"))

# 3. ASM = 도둑 눈으로 바깥을 한 바퀴 (hero)
P3 = svg(360, sky(360) + castle(200, 50, 0.7)
         + '<ellipse cx="380" cy="185" rx="330" ry="98" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="12 8"/>'
         + '<path d="M694 160 l14 6 l-12 10" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + person(60, 200, s=0.8, face=EYES, extra=SPYGLASS, **BLUE) + bubble(20, 130, 200, 34, "⟦도둑 눈으로 보면 뭐가 보이지?|what would a thief see?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + door(150, 230, 0.55, mark="tag") + door(330, 240, 0.55, mark="tag") + door(470, 240, 0.55, mark="?") + shed(600, 240, 0.6) + door(600, 250, 0.4, mark="?") + sign(690, 230, "⟦→ ?|→ ?⟧", 0.8)
         + '<rect x="520" y="60" width="100" height="70" rx="3" fill="var(--stone)" opacity="0.7"/>' + door(570, 105, 0.5, mark="?")
         + label(380, 320, "⟦보이는 문·창문·창고를 전부 지도에 그려요 — 모르던 것까지|draw every door, window, and shed you can see — even the ones you didn\'t know⟧", 12, "var(--ink)", cls="d")
         + label(380, 344, "⟦그리고 내일 또 한 바퀴|and around again tomorrow⟧", 12, "var(--muted)"))

# 4. 두 지도 비교 — 차이가 도둑이 먼저 찾는 문
P4 = svg(320, sky(320)
         + map_paper(40, 30, 220, 200, "⟦안에서 그린 지도|FROM INSIDE⟧") + mini_castle(110, 100, 0.7)
         + "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="#E9B44C"/>' for x, y in ((80, 94), (106, 94), (132, 94), (66, 120), (146, 120)))
         + label(110, 165, "⟦5|5⟧", 22, "#142033", cls="d") + "</g>"
         + '<path d="M275 130 L325 130" stroke="var(--muted)" stroke-width="3"/><path d="M315 120 L327 130 L315 140" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + map_paper(340, 30, 380, 200, "⟦바깥에서 그린 지도|FROM OUTSIDE⟧") + mini_castle(130, 100, 0.7)
         + "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="#E9B44C"/>' for x, y in ((100, 94), (126, 94), (152, 94), (86, 120), (166, 120)))
         + "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="var(--bad)"/>' for x, y in ((40, 130), (210, 90), (280, 120), (320, 70)))
         + label(130, 165, "⟦9|9⟧", 22, "#142033", cls="d")
         + label(250, 60, "⟦옛 뒷문|old back door⟧", 9, "var(--bad)") + label(300, 100, "⟦빌린 창고|rented shed⟧", 9, "var(--bad)") + label(330, 150, "⟦이름표만|signpost⟧", 9, "var(--bad)") + label(50, 160, "⟦왕자의 문|prince\'s door⟧", 9, "var(--bad)") + "</g>"
         + label(380, 268, "⟦차이 4개 — 도둑이 먼저 찾는 문이에요|the 4 extra — the doors a thief finds first⟧", 14, "var(--bad)", cls="d")
         + label(380, 298, "⟦닫거나, 이름표를 붙이거나, 틈 장부에 넣어요|close it, put a name on it, or add it to the crack ledger⟧", 12, "var(--muted)"))

# 5. 지도 → 장부 → 목수, 그리고 새 문은 지도가 먼저 알아채요
P5 = svg(300, sky(300)
         + map_paper(40, 60, 150, 120, "⟦바깥 지도|OUTSIDE MAP⟧", 1.0) + "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="{c}"/>' for x, y, c in ((30, 50, "#E9B44C"), (60, 50, "#E9B44C"), (90, 50, "var(--bad)"), (45, 80, "#E9B44C"), (110, 80, "var(--bad)"))) + "</g>"
         + '<path d="M200 120 L250 120" stroke="var(--muted)" stroke-width="3"/><path d="M240 110 L252 120 L240 130" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + map_paper(260, 60, 170, 120, "⟦틈 장부|CRACK LEDGER⟧", 1.0) + "".join(f'<circle cx="18" cy="{46 + i * 22}" r="5" fill="{c}"/>' + label(30, 50 + i * 22, t, 10, "#142033", "start") for i, (t, c) in enumerate((("⟦옛 뒷문 — 잠그기|old back door — lock⟧", "var(--bad)"), ("⟦빌린 창고 — 이름표|rented shed — name it⟧", "var(--accent)"), ("⟦이름표만 — 떼기|signpost — take down⟧", "var(--good)")))) + "</g>"
         + '<path d="M440 120 L490 120" stroke="var(--muted)" stroke-width="3"/><path d="M480 110 L492 120 L480 130" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(520, 80, s=0.75, face=SMILE, hat="#5B8DEF", shirt="#4A5A72", extra='<g transform="translate(58,54) rotate(-30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#5A3B22"/><rect x="-12" y="-8" width="24" height="12" rx="2" fill="var(--stone-dark)"/></g>') + label(550, 200, "⟦목수|carpenter⟧", 11, "var(--muted)")
         + door(680, 120, 0.7, color="#7B3FA0", mark="?") + '<rect x="655" y="60" width="50" height="20" rx="4" fill="var(--accent)"/>' + label(680, 74, "⟦새 문!|NEW!⟧", 10, "#FFF", cls="d") + label(680, 200, "⟦어젯밤 생긴 문|appeared last night⟧", 10, "var(--accent)")
         + label(380, 250, "⟦지도가 장부보다 먼저 알아채요|the map notices before the ledger does⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦모르는 문은 순찰도 못 돌고 판자도 못 대니까요|you can\'t patrol or board up a door you don\'t know about⟧", 11, "var(--muted)"))

OUTSIDE_I = icon(f'<circle cx="32" cy="24" r="10" fill="{SKIN}"/><path d="M20 20 Q32 6 44 20 Z" fill="var(--bad)"/><rect x="24" y="22" width="16" height="5" fill="#111C30"/><rect x="20" y="36" width="24" height="16" rx="5" fill="#2E3D57"/><path d="M8 56 q24 -16 48 0" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="4 3"/>')
COUNT_I = icon(f'<rect x="10" y="20" width="12" height="22" rx="2" fill="{WOOD}"/><rect x="26" y="20" width="12" height="22" rx="2" fill="{WOOD}"/><rect x="42" y="20" width="12" height="22" rx="2" fill="var(--bad)"/><text x="48" y="36" text-anchor="middle" font-size="14" font-weight="700" fill="#FFF">?</text><path d="M10 50 h44" stroke="var(--stone-dark)" stroke-width="3"/>')
TAG_I = icon(f'<rect x="14" y="14" width="24" height="40" rx="2" fill="{WOOD}"/><rect x="28" y="26" width="26" height="14" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M33 33 h16" stroke="#C9A86A" stroke-width="2"/>')
AGAIN_I = icon('<path d="M46 32 a14 14 0 1 1 -5 -10.7" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M42 12 l6 10 -12 2z" fill="var(--good)"/><circle cx="32" cy="32" r="4" fill="var(--good)"/>')

PAGE = {
    "slug": "asm", "order": 57,
    "title": ("바깥에서 세는 우리 성의 문", "Counting Our Doors from Outside"),
    "h1": ("<em>공격 표면 관리</em>가 뭐예요?", "What is <em>Attack Surface Management</em>?"),
    "sub": ("공격 표면 관리(Attack Surface Management)를 도둑 눈으로 성 바깥을 돌며 문을 세는 이야기로 풀어봤어요.",
            "Attack surface management, told as a story about walking around the castle with a thief\'s eyes and counting every door."),
    "panels": [
        {"svg": P1, "alt": ("안에서 그린 지도엔 문 5개. 그런데 담 밖의 도둑이 망원경으로 보면 창고와 뒷문이 더 보임", "The map drawn from inside shows 5 doors. But a thief outside the wall, with a spyglass, sees extra sheds and back doors"),
         "caption": ("안에서 그린 지도엔 문이 다섯이에요. 그런데 도둑은 바깥에서 봐요.", "The map from inside shows five doors. But the thief looks from outside."),
         "small": ("담 너머엔 지도에 없는 문이 더 있어요. 도둑은 지도를 보지 않아요 — 담 밖에서 보이는 걸 봐요.", "Beyond the wall are doors the map doesn\'t show. The thief doesn\'t read our map — they look at what\'s visible from outside.")},
        {"svg": P2, "alt": ("잊힌 문 넷: 옛날 목수가 낸 뒷문, 셋째 왕자가 몰래 낸 문, 마을에 빌린 창고, 창고는 없어졌는데 이름표만 남은 길", "Four forgotten doors: an old back door, a door the third prince made in secret, a rented shed in the village, and a signpost to a shed that no longer exists"),
         "caption": ("성이 크면 잊힌 문이 생겨요.", "A big castle grows forgotten doors."),
         "small": ('아무도 안 잠그는 옛 뒷문, 경비실 모르게 낸 문, <a href="casb-ko.html">마을에 빌린 창고</a>, 창고는 없어졌는데 남은 <a href="dns-ko.html">이름표</a>. 도둑은 이런 문부터 찾아요.',
                   'An old back door nobody locks, a door the guard room never knew about, a <a href="casb-en.html">rented shed in the village</a>, a <a href="dns-en.html">signpost</a> to a shed that\'s gone. These are the doors a thief looks for first.')},
        {"svg": P3, "hero": True, "alt": ("파란 모자가 망원경을 들고 성 바깥을 점선 원을 따라 돌며 '도둑 눈으로 보면 뭐가 보이지?' — 보이는 문마다 이름표나 물음표가 붙음", "A blue hat with a spyglass walks a dotted circle around the outside of the castle, asking what a thief would see — every visible door gets a name tag or a question mark"),
         "caption": ("공격 표면 관리는 도둑 눈으로 성 바깥을 한 바퀴 도는 거예요.", "Attack surface management is walking around the outside of the castle with a thief\'s eyes."),
         "small": ("보이는 문·창문·창고를 전부 지도에 그려요. 모르던 것까지요. 문마다 '누구 문인지' 이름표를 붙이고, 내일 또 한 바퀴 돌아요.", "Draw every door, window, and shed you can see — even the ones you didn\'t know about. Put a name on each one, and walk the circle again tomorrow."),
         "tricks": (4, [
             (OUTSIDE_I, ("바깥에서 보기", "Look from outside"), ("도둑이 보는 그대로", "exactly what the thief sees"), "warm"),
             (COUNT_I, ("다 세기", "Count them all"), ("모르던 문까지", "even the ones you forgot")),
             (TAG_I, ("이름표 붙이기", "Put a name on it"), ("누구 문인지, 왜 있는지", "whose door, and why")),
             (AGAIN_I, ("매일 다시 돌기", "Walk it daily"), ("문은 밤새 생겨요", "doors appear overnight"), "calm"),
         ])},
        {"svg": P4, "alt": ("안에서 그린 지도(문 5개)와 바깥에서 그린 지도(문 9개, 빨간 문 4개: 옛 뒷문, 왕자의 문, 빌린 창고, 이름표만)", "The map from inside (5 doors) next to the map from outside (9 doors, four in red: old back door, prince\'s door, rented shed, signpost)"),
         "caption": ("두 지도의 차이가 도둑이 먼저 찾는 문이에요.", "The difference between the two maps is where the thief goes first."),
         "small": ('빨간 문 넷은 닫거나, 이름표를 붙이거나, <a href="vulnmgmt-ko.html">틈 장부</a>에 넣어요. 모르는 문은 순찰도 못 돌거든요.',
                   'The four red doors get closed, named, or added to the <a href="vulnmgmt-en.html">crack ledger</a>. You can\'t patrol a door you don\'t know about.')},
        {"svg": P5, "alt": ("바깥 지도 → 틈 장부(옛 뒷문 잠그기, 빌린 창고 이름표, 이름표만 떼기) → 목수. 오른쪽에 '새 문!' 표시가 붙은 어젯밤 생긴 보라색 문", "Outside map → crack ledger (lock the old door, name the shed, take down the signpost) → carpenter. On the right, a purple door marked NEW that appeared last night"),
         "caption": ("지도가 장부보다 먼저 알아채요.", "The map notices before the ledger does."),
         "small": ('바깥 지도에 새 문이 뜨면 <a href="vulnmgmt-ko.html">틈 장부</a>로 넘기고 <a href="patch-ko.html">목수</a>가 판자를 대요. 어젯밤 생긴 문도 오늘 아침 한 바퀴에 잡혀요.',
                   'A new door on the outside map goes to the <a href="vulnmgmt-en.html">crack ledger</a>, and the <a href="patch-en.html">carpenter</a> boards it up. A door that appeared last night is caught on this morning\'s walk.')},
    ],
    "summary": (("<b>공격 표면 관리</b> = <b>도둑 눈으로 성 바깥을 돌며</b> 보이는 문·창문·창고를 <b>모르던 것까지 다 세어</b> 이름표를 붙이고, <b>매일 다시 도는</b> 일.",
                 "<b>Attack surface management</b> = <b>walk around the castle with a thief\'s eyes</b>, <b>count every door, window, and shed — even the forgotten ones</b>, put a name on each, and <b>walk it again every day</b>."),
                ("Attack Surface Management. 인터넷에서 보이는 우리 자산(도메인, IP, 클라우드, 잊힌 서버)을 공격자 관점으로 계속 발견·분류·감시해요. 취약점 관리가 '아는 방'을 돈다면, ASM은 '방이 몇 개인지'를 바깥에서 세요.",
                 "Continuously discovering, classifying, and monitoring everything of ours visible from the internet — domains, IPs, cloud, forgotten servers — from an attacker\'s point of view. Vulnerability management patrols the rooms you know; ASM counts the rooms from outside.")),
    "glossary": [
        ("공격 표면", "Attack surface", ("바깥에서 보이는 문 전부.", "Every door visible from outside."), ("도둑이 손댈 수 있는 곳의 합. 문이 많을수록 넓어요.", "The sum of everything a thief could touch. More doors, bigger surface.")),
        ("EASM", "External ASM", ("담 밖에서 그린 지도.", "The map drawn from beyond the wall."), ("인터넷에서 보이는 것만 세요. 성 안 복도는 다른 지도.", "Counts only what the internet can see; the halls inside are a different map.")),
        ("섀도 IT", "Shadow IT", ("왕자가 몰래 낸 문.", "The prince\'s secret door."), ("나쁜 뜻은 없었지만 경비실이 몰라요. 그래서 안 잠겨요.", "No bad intent — but the guard room never knew, so it never got locked.")),
        ("자산 발견", "Asset discovery", ("문 세기.", "Counting doors."), ("이름표 붙이기 전에 먼저 몇 개인지. ASM의 첫걸음.", "Before naming them, know how many there are. Step one of ASM.")),
        ("서브도메인", "Subdomains", ("성으로 가는 이름표들.", "Signposts to the castle."), ('창고가 없어졌는데 이름표만 남으면 도둑이 그 자리에 가짜 창고를 세워요. → <a href="dns-ko.html">마을 안내소</a>', 'A signpost to a shed that\'s gone lets a thief put a fake shed there. → <a href="dns-en.html">the village directory</a>')),
        ("클라우드 노출", "Cloud exposure", ("마을에 빌린 창고.", "A rented shed in the village."), ('우리 상자인데 성 밖에 있어요. → <a href="casb-ko.html">바깥 창고 문지기</a>', 'Our chests, outside the wall. → <a href="casb-en.html">the outside storeroom keeper</a>')),
        ("취약점 관리", "Vulnerability management", ("아는 방 순찰.", "Patrolling the rooms you know."), ('ASM 이 세어 준 문을 장부에 넣어요. → <a href="vulnmgmt-ko.html">매달 도는 틈 장부</a>', 'Takes the doors ASM counted into the ledger. → <a href="vulnmgmt-en.html">the crack ledger</a>')),
        ("정찰", "Reconnaissance", ("도둑도 같은 지도를 그려요.", "The thief draws the same map."), ('도둑이 먼저 그리기 전에 우리가 먼저. → <a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>', 'Draw it before the thief does. → <a href="redteam-en.html">the team that plays the real thief</a>')),
    ],
}
