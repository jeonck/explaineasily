from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
VISITOR = dict(hat=None, shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def shop(x, y, s=1.0, broken=False):
    crack = '<path d="M-10 -8 l8 10 l-6 8 l10 12" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>' if broken else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-20" width="80" height="60" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M-48 -20 h96 l-8 -18 h-80z" fill="var(--accent)"/><rect x="-30" y="-8" width="24" height="20" fill="var(--sky)"/><rect x="6" y="0" width="22" height="40" rx="2" fill="{WOOD}"/>'
            + label(0, -26, "⟦상점|SHOP⟧", 10, "#FFF", cls="d") + f'{crack}</g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def wall(x, y, h, w=34, color="var(--stone-dark)"):
    return battlements(x, y - 18, w, 2, color, 18) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>'


def archway(x, y, w=28, h=44, color="var(--night)"):
    return f'<path d="M{x} {y} v-{h - w / 2} a{w / 2} {w / 2} 0 0 1 {w} 0 v{h - w / 2}z" fill="{color}"/>'


# 1. 손님이 오는 상점이 성 안 깊숙이, 금고 옆에
P1 = svg(320, sky(320)
         + label(90, 60, "⟦마을|the village⟧", 13, "var(--ink)", cls="d")
         + wall(230, 80, 182) + archway(233, 262)
         + label(490, 60, "⟦성 안|inside the castle⟧", 13, "var(--ink)", cls="d")
         + person(40, 120, s=0.65, face=SMILE, **VISITOR) + person(100, 140, s=0.65, face=SMILE, **VISITOR) + person(160, 120, s=0.65, face=SMILE, **VISITOR)
         + '<path d="M120 245 H330" stroke="var(--muted)" stroke-width="3" stroke-dasharray="8 6"/><path d="M330 245 l-12 -8 v16z" fill="var(--muted)"/>'
         + shop(400, 200) + person(330, 160, s=0.55, face=SMILE, **VISITOR)
         + chest(560, 226, 1.3, lock=True) + label(560, 278, "⟦금고|the vault⟧", 11, "var(--muted)")
         + person(650, 150, s=0.75, face=EYES, **GUARD)
         + label(400, 278, "⟦상점이 금고 바로 옆에 있어요|the shop sits right next to the vault⟧", 11, "var(--muted)")
         + label(380, 306, "⟦마을 손님이 오는 상점을 성 안 깊숙이 뒀어요|the shop that village guests visit sits deep inside the castle⟧", 12, "var(--ink)", cls="d"))

# 2. 상점이 털리면 곧장 금고까지
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + wall(230, 70, 172) + archway(233, 242)
         + person(90, 120, s=0.7, face=MASK) + '<path d="M150 230 H330" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M330 230 l-12 -8 v16z" fill="var(--bad)"/>'
         + shop(400, 190, broken=True)
         + '<path d="M450 200 H520" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M520 200 l-12 -8 v16z" fill="var(--bad)"/>'
         + person(530, 130, s=0.7, face=MASK, extra=BAG) + chest(615, 222, 1.2, lock=False, color="var(--stone)")
         + label(612, 268, "⟦금고까지 한 걸음|one step to the vault⟧", 11, "var(--bad)")
         + person(690, 120, s=0.7, face=FROWN + SWEAT, **GUARD)
         + label(380, 288, "⟦상점 하나가 털리면, 성 전체가 털려요|one shop breaks, and the whole castle is open⟧", 12, "var(--ink)", cls="d"))

# 3. DMZ = 두 성벽 사이의 마당 (hero)
P3 = svg(360, sky(360)
         + '<rect x="240" y="60" width="270" height="230" fill="var(--good-soft)"/>'
         + wall(210, 80, 210) + archway(213, 290, 28, 46) + wall(510, 80, 210) + archway(516, 290, 22, 34, "var(--night)")
         + label(120, 50, "⟦마을|village⟧", 13, "var(--ink)", cls="d") + label(375, 50, "⟦마당|the yard⟧", 15, "var(--ink)", cls="d") + label(640, 50, "⟦성 안|inside⟧", 13, "var(--ink)", cls="d")
         + label(227, 314, "⟦바깥 성벽|outer wall⟧", 10, "var(--ink)") + label(527, 314, "⟦안쪽 성벽 · 좁은 문|inner wall · narrow door⟧", 10, "var(--ink)")
         + person(40, 150, s=0.6, face=SMILE, **VISITOR) + person(100, 170, s=0.6, face=SMILE, **VISITOR) + '<path d="M150 260 H228" stroke="var(--muted)" stroke-width="3" stroke-dasharray="8 6"/>'
         + shop(330, 180) + person(410, 160, s=0.55, face=SMILE, **VISITOR)
         + person(455, 110, s=0.55, face=EYES, **GUARD) + label(470, 190, "⟦파수꾼|watchman⟧", 9, "var(--ink)")
         + label(375, 266, "⟦손님은 여기까지|guests stop here⟧", 11, "var(--good)", cls="d")
         + chest(640, 226, 1.2, lock=True) + person(690, 130, s=0.7, face=SMILE, **GUARD) + label(640, 274, "⟦금고|the vault⟧", 10, "var(--muted)")
         + label(380, 344, "⟦두 성벽 사이 마당에 상점을 두고, 손님은 마당까지만|the shop goes in the yard between two walls, and guests stop at the yard⟧", 12, "var(--ink)", cls="d"))

# 4. 안쪽으로 가는 문은 하나, 아주 좁게 — 문지기와 파수꾼
P4 = svg(320, sky(320)
         + '<rect x="0" y="40" width="470" height="220" fill="var(--good-soft)"/>' + wall(470, 60, 200) + archway(474, 260, 26, 40)
         + label(235, 30, "⟦마당|the yard⟧", 13, "var(--ink)", cls="d") + label(620, 30, "⟦성 안|inside⟧", 13, "var(--ink)", cls="d")
         + shop(90, 150, 0.85) + shop(210, 150, 0.85) + shop(330, 150, 0.85)
         + '<path d="M140 165 v-40 M260 165 v-40" stroke="var(--line)" stroke-width="3" stroke-dasharray="4 4"/>'
         + label(90, 210, "⟦빵집 창구|bread counter⟧", 9, "var(--ink)") + label(210, 210, "⟦편지 창구|letter counter⟧", 9, "var(--ink)") + label(330, 210, "⟦대신 가는 심부름꾼|the errand runner⟧", 9, "var(--ink)")
         + person(60, 44, s=0.5, face=EYES, **GUARD) + label(80, 112, "⟦쪽지 검토원|note checker⟧", 9, "var(--muted)")
         + person(300, 40, s=0.5, face=EYES, **GUARD) + label(320, 108, "⟦마당 파수꾼|yard watchman⟧", 9, "var(--muted)")
         + person(425, 150, s=0.7, face=EYES, **GUARD) + label(395, 248, "⟦문지기 — 단 하나의 문|doorkeeper — the only door⟧", 9, "var(--ink)")
         + '<path d="M375 225 H420" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + chest(600, 200, 1.2, lock=True) + label(600, 250, "⟦빵 값 장부|the bread ledger⟧", 10, "var(--muted)")
         + label(620, 120, "⟦상점이 안쪽에 물어볼 건|the shop may ask inside for⟧", 10, "var(--muted)") + label(620, 138, "⟦딱 정해진 한 가지뿐|exactly one agreed thing⟧", 10, "var(--muted)")
         + label(380, 302, "⟦상점끼리도 나누고, 안으로 가는 문은 딱 하나, 아주 좁게|shops are kept apart, and the way inside is one narrow door⟧", 12, "var(--ink)", cls="d"))

# 5. 상점이 털려도 마당에서 끝
P5 = svg(320, sky(320)
         + '<rect x="240" y="60" width="270" height="200" fill="var(--good-soft)"/>' + wall(210, 80, 180) + archway(213, 260, 28, 46) + wall(510, 80, 180) + archway(516, 260, 22, 34, WOOD)
         + shop(320, 170, broken=True) + person(400, 130, s=0.7, face=MASK + SWEAT, extra=BAG)
         + label(375, 258, "⟦마당에서 끝이에요|it ends in the yard⟧", 11, "var(--good)", cls="d")
         + person(455, 80, s=0.5, face=EYES, **GUARD) + bell(600, 90, 0.7, ring=True) + label(600, 150, "⟦종!|the bell!⟧", 12, "var(--accent)", cls="d")
         + chest(640, 226, 1.2, lock=True) + label(640, 272, "⟦금고는 무사해요|the vault is safe⟧", 10, "var(--good)")
         + label(120, 100, "⟦마을|village⟧", 13, "var(--ink)", cls="d") + label(100, 220, "⟦손님은 잠시 못 와요|guests wait a while⟧", 10, "var(--muted)")
         + label(380, 304, "⟦상점이 털려도 도둑은 마당에 갇히고, 종이 울려요|even if the shop breaks, the thief is stuck in the yard — and the bell rings⟧", 12, "var(--ink)", cls="d"))

TWOWALL_I = icon('<rect x="8" y="14" width="10" height="40" fill="var(--stone-dark)"/><rect x="46" y="14" width="10" height="40" fill="var(--stone-dark)"/><rect x="18" y="14" width="28" height="40" fill="var(--good-soft)"/><rect x="24" y="30" width="16" height="14" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>')
STOP_I = icon(f'<circle cx="22" cy="24" r="9" fill="{SKIN}"/><rect x="13" y="34" width="18" height="18" rx="4" fill="#7B3FA0"/><path d="M40 14 v40" stroke="var(--stone-dark)" stroke-width="6"/><path d="M46 26 l8 8 M54 26 l-8 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
NARROW_I = icon('<rect x="10" y="10" width="44" height="44" fill="var(--stone-dark)"/><path d="M28 54 v-18 a4 4 0 0 1 8 0 v18z" fill="var(--night)"/><circle cx="32" cy="26" r="6" fill="var(--good)"/>')
WATCH_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><path d="M20 18 q12 -14 24 0z" fill="var(--good)"/><rect x="22" y="32" width="20" height="22" rx="4" fill="var(--good)"/><circle cx="50" cy="16" r="7" fill="none" stroke="var(--ink)" stroke-width="3"/><path d="M55 21 l6 6" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "dmz", "order": 103,
    "title": ("성벽과 성벽 사이의 마당", "The Yard Between the Walls"),
    "h1": ("<em>DMZ</em>가 뭐예요?", "What is a <em>DMZ</em>?"),
    "sub": ("DMZ(Demilitarized Zone, 비무장 지대)를 마을 손님이 오는 상점을 두 성벽 사이 마당에 두는 이야기로 풀어봤어요.",
            "The DMZ — demilitarized zone — told as a story about putting the shop that village guests visit in a yard between two walls."),
    "panels": [
        {"svg": P1, "alt": ("성벽 하나 왼쪽은 마을, 오른쪽은 성 안. 마을 손님 셋이 성문을 지나 성 안 깊숙한 상점으로 들어가고, 상점 바로 옆에 잠긴 금고와 경비가 있음", "One wall, the village on the left and the castle inside on the right. Three village guests pass through the gate to a shop deep inside, right next to a locked vault and a guard"),
         "caption": ("마을 손님이 오는 상점이 성 안 깊숙이 있어요.", "The shop that village guests visit sits deep inside the castle."),
         "small": ("빵집이든 편지 창구든, 손님이 오는 상점은 마을에 열려 있어야 해요. 그런데 그 상점이 금고 바로 옆에 있어요.", "A bakery, a letter counter — a shop guests visit has to be open to the village. But this shop sits right next to the vault.")},
        {"svg": P2, "alt": ("도둑이 손님인 척 성문을 지나 상점을 부수고, 가방을 든 채 한 걸음 옆 금고로 향함. 경비는 땀을 흘림", "A thief passes the gate like a guest, breaks the shop, and heads for the vault one step away with a bag. The guard sweats"),
         "caption": ("상점이 털리면, 곧장 금고까지예요.", "Break the shop, and the vault is one step away."),
         "small": ('손님이 오는 문은 늘 열려 있으니 도둑도 들어와요. 상점의 <a href="injection-ko.html">쪽지 틈</a> 하나로 성 전체가 열려요.',
                   'A door open to guests is open to thieves too. One <a href="injection-en.html">crack in the shop\'s note slot</a>, and the whole castle is open.')},
        {"svg": P3, "hero": True, "alt": ("바깥 성벽과 안쪽 성벽 사이의 초록 마당. 마당에 상점과 손님, 파수꾼이 있고, 안쪽 성벽에는 아주 좁은 문 하나. 성 안에는 금고와 경비", "A green yard between an outer wall and an inner wall. The shop, guests, and a watchman are in the yard; the inner wall has one very narrow door. Inside are the vault and a guard"),
         "caption": ("DMZ는 성벽과 성벽 사이의 마당이에요.", "A DMZ is the yard between two walls."),
         "small": ('상점은 마당에 두고, 손님은 마당까지만 와요. 마당에서 안쪽 성으로 가는 문은 아주 좁고(<a href="firewall-ko.html">성벽 두 겹</a>), 마당엔 <a href="ndr-ko.html">파수꾼</a>이 서 있어요.',
                   'The shop goes in the yard, and guests come no farther. The door from the yard into the castle is very narrow (<a href="firewall-en.html">two walls</a>), and a <a href="ndr-en.html">watchman</a> stands in the yard.'),
         "tricks": (4, [
             (TWOWALL_I, ("성벽 두 겹", "Two walls"), ("바깥 벽과 안쪽 벽 사이가 마당", "the yard is between them"), "calm"),
             (STOP_I, ("손님은 마당까지", "Guests stop at the yard"), ("성 안으론 아무도 못 와요", "no one comes inside")),
             (NARROW_I, ("안으로 가는 문은 좁게", "A narrow way in"), ("딱 하나, 딱 정해진 일만", "one door, one agreed errand")),
             (WATCH_I, ("마당엔 파수꾼", "A watchman in the yard"), ("상점이 이상하면 바로 알아요", "knows the moment a shop acts odd"), "warm"),
         ])},
        {"svg": P4, "alt": ("마당 안에 상점 셋(빵집 창구, 편지 창구, 대신 가는 심부름꾼)이 점선으로 나뉘어 있고, 쪽지 검토원과 마당 파수꾼이 지켜봄. 안쪽 성벽의 유일한 문 앞에 문지기, 성 안에는 빵 값 장부 상자", "Three shops in the yard — bread counter, letter counter, errand runner — separated by dotted lines, watched by a note checker and a yard watchman. A doorkeeper stands at the inner wall\'s only door; inside is the bread ledger chest"),
         "caption": ("상점끼리도 나누고, 안으로 가는 문은 딱 하나예요.", "Shops are kept apart, and there is exactly one door inside."),
         "small": ('빵집은 안쪽에 "빵 값 장부" 하나만 물어볼 수 있어요. 마을 손님 대신 안에 다녀오는 <a href="proxy-ko.html">심부름꾼</a>도 마당에 살고, 창구 앞엔 <a href="waf-ko.html">쪽지 검토원</a>이 있어요. 문지기를 지나는 사람은 <a href="pam-ko.html">특별 열쇠</a>를 가진 몇 명뿐이에요.',
                   'The bakery may ask inside for exactly one thing — the bread ledger. The <a href="proxy-en.html">errand runner</a> who goes inside for village guests lives in the yard too, and a <a href="waf-en.html">note checker</a> stands at the counter. Only a few with a <a href="pam-en.html">special key</a> ever pass the doorkeeper.')},
        {"svg": P5, "alt": ("상점이 부서지고 도둑이 가방을 든 채 마당에 서서 땀을 흘림. 안쪽 성벽의 좁은 문은 닫혀 있고 종이 울리며, 성 안 금고는 무사함. 마을 손님은 잠시 못 옴", "The shop is broken and the thief stands sweating in the yard with a bag. The inner wall\'s narrow door is shut, the bell rings, and the vault inside is safe. Village guests wait a while"),
         "caption": ("상점이 털려도 마당에서 끝이에요.", "Even if the shop breaks, it ends in the yard."),
         "small": ('도둑은 마당에 갇히고 <a href="soc-ko.html">경비실</a>에 종이 울려요. 상점은 잠시 문을 닫지만 금고는 무사해요. 요즘 성은 마당 안에서도 <a href="zerotrust-ko.html">문마다 물어봐요</a>.',
                   'The thief is stuck in the yard and the bell rings in the <a href="soc-en.html">guard room</a>. The shop closes for a while, but the vault is safe. Modern castles <a href="zerotrust-en.html">ask at every door</a> inside the yard too.')},
    ],
    "summary": (("<b>DMZ</b> = 마을 손님이 오는 상점을 <b>바깥 성벽과 안쪽 성벽 사이 마당</b>에 두어, 손님은 <b>마당까지만</b>, 안으로 가는 문은 <b>좁게 하나</b>, 마당엔 <b>파수꾼</b>. 상점이 털려도 <b>마당에서 끝</b>.",
                 "<b>DMZ</b> = put the shops village guests visit in the <b>yard between the outer and inner walls</b>; guests stop <b>at the yard</b>, the way inside is <b>one narrow door</b>, and a <b>watchman</b> stands in the yard. If a shop breaks, it <b>ends in the yard</b>."),
                ("DMZ(Demilitarized Zone). 웹 서버·메일 서버처럼 인터넷에 공개해야 하는 서버를 외부 방화벽과 내부 방화벽 사이의 별도 네트워크 구역에 두어, 공개 서버가 침해되어도 내부망까지 바로 이어지지 않게 하는 구조예요. 내부로 가는 통로는 필요한 포트·서비스만 최소로 열어요.",
                 "A separate network segment between an external and an internal firewall where internet-facing servers — web, mail — are placed, so that a compromised public server doesn\'t lead straight into the internal network. Only the minimum ports and services needed are opened inward.")),
    "glossary": [
        ("DMZ", "DMZ", ("성벽과 성벽 사이의 마당.", "The yard between the walls."), ("마을에 열려 있어야 하는 상점은 여기 살아요. 안쪽 성과는 좁은 문 하나로만 이어져요.", "Shops that must be open to the village live here. The only link inward is one narrow door.")),
        ("경계 방화벽 · 내부 방화벽", "External & internal firewall", ("바깥 성벽과 안쪽 성벽.", "The outer wall and the inner wall."), ('바깥 벽은 손님을 마당까지 들이고, 안쪽 벽은 정해진 심부름만 들여요. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'The outer wall lets guests into the yard; the inner wall lets through only agreed errands. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("공개 서버", "Public-facing server", ("마당의 상점.", "The shop in the yard."), ("빵집, 편지 창구 — 마을 누구나 올 수 있어야 하니까 제일 자주 털려요. 그래서 마당에 둬요.", "The bakery, the letter counter — anyone from the village may come, so they get broken most. That\'s why they live in the yard.")),
        ("역방향 프록시", "Reverse proxy", ("마당에 사는 심부름꾼.", "The errand runner in the yard."), ('손님 대신 안에 다녀와서 손님은 안쪽 문을 본 적도 없어요. → <a href="proxy-ko.html">대신 다녀오는 심부름꾼</a>', 'Goes inside on the guest\'s behalf, so the guest never even sees the inner door. → <a href="proxy-en.html">the runner who goes for you</a>')),
        ("점프 서버 · 배스천 호스트", "Jump server · bastion host", ("좁은 문의 문지기.", "The doorkeeper at the narrow door."), ('마당에서 안으로 들어가는 유일한 길. 특별 열쇠를 가진 사람만 지나요. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'The only path from the yard inward. Only those with a special key pass. → <a href="pam-en.html">the master key in the vault</a>')),
        ("세그먼트", "Segment", ("마당 안의 점선.", "The dotted lines in the yard."), ('빵집이 털려도 편지 창구는 따로예요. → <a href="vlan-ko.html">색 리본으로 나눈 복도</a>', 'If the bakery breaks, the letter counter is still apart. → <a href="vlan-en.html">halls divided by ribbon</a>')),
        ("이스트-웨스트 트래픽", "East-west traffic", ("상점끼리 오가는 심부름.", "Errands between the shops."), ('마을에서 오는 손님(남북)이 아니라 마당 안에서 옆으로 움직이는 것. 파수꾼이 이걸 봐요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Not guests from the village (north-south), but movement sideways inside the yard. The watchman looks at this. → <a href="ndr-en.html">the one who watches the halls</a>')),
        ("제로 트러스트", "Zero trust", ("마당 안에서도 문마다 묻기.", "Asking at every door, even in the yard."), ('마당은 여전히 쓰지만, 마당 안이라고 믿지는 않아요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'The yard is still used, but being in it earns no trust. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
    ],
}
