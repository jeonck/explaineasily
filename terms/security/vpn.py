from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def house(x, y, name="⟦집|home⟧", roof="var(--bad)", s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-50 0 L0 -36 L50 0 Z" fill="{roof}"/><rect x="-10" y="26" width="20" height="34" fill="{WOOD}"/>{label(0, 80, name, 12, "var(--muted)")}</g>')


def cafe(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-46 0 h92 l-8 -20 h-76 z" fill="var(--accent)"/>' + "".join(f'<rect x="{-46 + i * 18}" y="-20" width="9" height="20" fill="#FFD9B8"/>' for i in range(5))
            + f'<rect x="-10" y="26" width="20" height="34" fill="{WOOD}"/>{label(0, 80, "⟦카페|cafe⟧", 12, "var(--muted)")}'
            f'<path d="M20 -34 a10 10 0 0 1 0 -6 M28 -38 a10 10 0 0 1 0 -6" stroke="var(--stone-dark)" stroke-width="2" fill="none"/></g>')


def tunnel(x1, x2, y, depth=70, sealed=True):
    core = f'<path d="M{x1} {y} C{x1} {y + depth} {x2} {y + depth} {x2} {y}" stroke="#3A2A1E" stroke-width="26" fill="none" stroke-linecap="round"/>'
    seal = f'<path d="M{x1} {y} C{x1} {y + depth} {x2} {y + depth} {x2} {y}" stroke="var(--good)" stroke-width="30" fill="none" stroke-linecap="round" stroke-dasharray="4 10" opacity="0.6"/>' if sealed else ""
    return seal + core


GROUND = lambda h: f'<rect y="{h - 90}" width="760" height="90" fill="#5A4636"/><rect y="{h - 92}" width="760" height="6" fill="var(--good-soft)"/>'
EYE = '<path d="M-14 0 Q0 -10 14 0 Q0 10 -14 0 Z" fill="#FFF" stroke="var(--night)" stroke-width="2"/><circle r="4" fill="var(--night)"/>'

# 1. 마을 길을 지난다
P1 = svg(300, sky(300, ground=False) + GROUND(300) + house(80, 130)
         + '<path d="M120 200 C250 190 450 210 600 200" stroke="var(--stone-dark)" stroke-width="10" fill="none" stroke-linecap="round"/>'
         + castle(560, 90, 0.4)
         + person(300, 100, s=0.8, **ME, extra=BAG)
         + person(200, 120, s=0.55, hat="#E9B44C", shirt="#4A5A72", face=EYES) + person(430, 120, s=0.55, hat="var(--stone-dark)", shirt="#4A5A72", face=EYES)
         + f'<g transform="translate(240,150)">{EYE}</g><g transform="translate(430,150)">{EYE}</g>'
         + label(380, 275, "⟦길 위에선 누구나 내 가방 속을 들여다볼 수 있어요|on the road, anyone can peek into my bag⟧", 13, "#F5E6B8"))

# 2. 카페 길에선 옆 사람이 다 본다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + cafe(120, 120)
         + '<g transform="translate(120,40)"><path d="M-30 30 a40 40 0 0 1 60 0 M-18 42 a24 24 0 0 1 36 0 M-6 54 a8 8 0 0 1 12 0" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
         + label(120, 30, "⟦공짜 와이파이|free Wi-Fi⟧", 12, "var(--muted)")
         + person(300, 110, s=0.85, **ME, extra=BAG)
         + person(420, 100, s=0.85, face=MASK) + f'<g transform="translate(400,190)">{EYE}</g>'
         + bubble(380, 20, 200, 34, "⟦편지 내용 다 보이네|I can read every letter⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 275, "⟦공짜 와이파이는 다 같이 쓰는 길이에요|free Wi-Fi is a road everyone shares⟧", 13, "var(--muted)"))

# 3. VPN = 봉인된 땅굴 (hero)
P3 = svg(340, sky(340, ground=False) + GROUND(340) + house(80, 140) + castle(520, 100, 0.45)
         + tunnel(80, 640, 248, 70)
         + person(340, 262, s=0.42, **ME, extra=BAG)
         + person(250, 150, s=0.55, face=MASK) + person(430, 150, s=0.55, face=MASK) + label(340, 150, "?", 30, "var(--bad)", cls="d")
         + label(160, 320, "⟦땅굴 입구|tunnel mouth⟧", 12, "#F5E6B8") + label(600, 320, "⟦성 안에서 나와요|comes out inside the castle⟧", 12, "#F5E6B8")
         + label(360, 240, "⟦봉인|sealed⟧", 12, "var(--good)"))

# 4. 땅굴은 두 가지
P4 = svg(320, '<rect width="380" height="320" fill="var(--sky)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>' + '<rect y="240" width="760" height="80" fill="#5A4636"/>'
         + label(190, 34, "⟦회사 땅굴|the company tunnel⟧", 15, "var(--ink)", cls="d")
         + house(60, 120, "⟦집|home⟧", s=0.8) + castle(230, 100, 0.3) + tunnel(60, 320, 240, 40)
         + label(190, 300, "⟦집 → 성 안|home → inside the castle⟧", 12, "#F5E6B8")
         + label(570, 34, "⟦개인 땅굴|the personal tunnel⟧", 15, "var(--ink)", cls="d")
         + cafe(450, 120, 0.8) + tunnel(450, 640, 240, 40)
         + '<g transform="translate(640,150)"><rect x="-30" y="0" width="60" height="50" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M-38 0 L0 -26 L38 0 Z" fill="#5B8DEF"/>' + label(0, 70, "⟦다른 마을 출구|exit in another town⟧", 11, "var(--muted)") + "</g>"
         + person(520, 60, s=0.55, face=MASK) + f'<g transform="translate(540,150)">{EYE}</g>' + label(540, 175, "⟦어디로 갔지?|where did he go?⟧", 11, "var(--bad)")
         + label(570, 300, "⟦카페 → 다른 마을에서 나와요|cafe → comes out in another town⟧", 12, "#F5E6B8"))

# 5. 땅굴을 나오면 성 안 어디든
P5 = svg(320, sky(320, ground=False) + GROUND(320)
         + tunnel(60, 300, 228, 50) + person(300, 60, s=0.7, hat="var(--good)", shirt="#2E3D57", face=MASK)
         + '<path d="M340 130 C400 100 460 140 540 110" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + "".join(f'<g transform="translate({x},80) scale(0.5)"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><circle cx="20" cy="54" r="4" fill="#E9B44C"/></g>' for x in (420, 500, 580))
         + label(500, 160, "⟦나오면 어디든|out, and anywhere⟧", 12, "var(--bad)")
         + person(640, 120, s=0.7, face=SMILE, **GUARD, extra='<g transform="translate(66,66)"><rect x="-2" y="-20" width="4" height="14" fill="var(--night)"/><rect x="-10" y="-6" width="20" height="26" rx="4" fill="#FFD166" stroke="var(--night)" stroke-width="2"/></g>')
         + label(670, 240, "⟦→ 안내인|→ the escort⟧", 12, "var(--good)")
         + label(380, 300, "⟦그래서 요즘은 방 하나까지만 데려다주는 안내인으로 바꿔요|which is why the escort to one room is taking over⟧", 12, "#F5E6B8"))

TUNNEL_I = icon('<path d="M8 44 C8 14 56 14 56 44" stroke="#3A2A1E" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M8 44 C8 14 56 14 56 44" stroke="var(--good)" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="3 6" opacity="0.6"/>')
MOUTH_I = icon('<path d="M10 50 a22 22 0 0 1 44 0 Z" fill="#3A2A1E"/><rect x="10" y="50" width="44" height="6" fill="#3A2A1E"/>')
INSIDE_I = icon('<rect x="8" y="26" width="48" height="28" fill="var(--stone-dark)"/><rect x="8" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="18" width="10" height="10" fill="var(--stone-dark)"/><circle cx="32" cy="42" r="6" fill="var(--good)"/>')
EYE_I = icon('<path d="M6 32 Q32 8 58 32 Q32 56 6 32 Z" fill="none" stroke="var(--bad)" stroke-width="3"/><path d="M14 20 L50 44" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "vpn", "order": 30,
    "title": ("봉인된 땅굴", "The Sealed Tunnel"),
    "h1": ("<em>VPN</em>이 뭐예요?", "What is a <em>VPN</em>?"),
    "sub": ("가상 사설망(Virtual Private Network)을 집에서 성까지 파는 봉인된 땅굴 이야기로 풀어봤어요.",
            "Virtual Private Network, told as a story about a sealed tunnel from home to the castle."),
    "panels": [
        {"svg": P1, "alt": ("집에서 성으로 가는 마을 길 위에서 가방 든 사람을 옆 사람들이 눈으로 들여다봄", "On the town road from home to the castle, bystanders peer at a person carrying a bag"),
         "caption": ("집에서 성까지 가려면 마을 길을 지나요.", "From home to the castle, you take the town road."),
         "small": ("길 위에선 누구나 내 가방 속을 들여다볼 수 있어요.", "And on the road, anyone can peek into my bag.")},
        {"svg": P2, "alt": ("공짜 와이파이 카페 앞에서 가면 쓴 사람이 '편지 내용 다 보이네' 하며 남의 가방을 들여다봄", "Outside a free-Wi-Fi cafe, a masked figure says I can read every letter while peering into someone's bag"),
         "caption": ("카페 길에선 옆 사람이 다 봐요.", "On the cafe's road, the person next to you sees everything."),
         "small": ("공짜 와이파이는 다 같이 쓰는 길이에요.", "Free Wi-Fi is a road everyone shares.")},
        {"svg": P3, "hero": True, "alt": ("집에서 성 안까지 땅속으로 이어진 초록 봉인 땅굴, 그 안을 걷는 사람, 땅 위의 도둑들은 물음표", "A green-sealed tunnel underground from home into the castle; a person walks inside it while thieves above show a question mark"),
         "caption": ("VPN은 성까지 파는 봉인된 땅굴이에요.", "A VPN is a sealed tunnel dug all the way to the castle."),
         "small": ("땅굴 안은 밖에서 안 보여요. 나오면 성 안이에요.", "Nobody outside can see into it. And you come out inside the castle."),
         "tricks": (4, [
             (TUNNEL_I, ("봉인된 땅굴", "The sealed tunnel"), ("안이 안 보여요 — 암호화", "nobody sees inside — encryption"), "calm"),
             (MOUTH_I, ("땅굴 입구", "The tunnel mouth"), ("성벽 쪽에 있어요", "sits at the castle wall")),
             (INSIDE_I, ("성 안에서 나옴", "Out inside the castle"), ("성 사람 취급을 받아요", "you're treated as castle folk"), "warm"),
             (EYE_I, ("길 사람이 보는 건", "What the road sees"), ("땅굴에 들어갔다는 것뿐", "only that you went underground"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 회사 땅굴: 집에서 성 안으로. 오른쪽 개인 땅굴: 카페에서 다른 마을 출구로 나오고, 도둑은 '어디로 갔지?'", "Left, the company tunnel: home into the castle. Right, the personal tunnel: from the cafe to an exit in another town, the thief wondering where did he go"),
         "caption": ("땅굴은 두 가지예요.", "There are two kinds of tunnel."),
         "small": ("회사 땅굴은 집에서 성 안으로. 개인 땅굴은 카페에서 다른 마을 출구로 나와요 — 길 사람들은 내가 어디 갔는지 몰라요.", "The company tunnel goes from home into the castle. The personal one goes from the cafe to an exit in another town — the road never learns where I went.")},
        {"svg": P5, "alt": ("땅굴에서 나온 초록 모자의 가면 쓴 사람이 방 여러 개로 자유롭게 가고, 옆에 등불 든 안내인", "A masked figure in a green hat emerges from the tunnel and heads freely for several doors; an escort with a lantern stands nearby"),
         "caption": ("땅굴을 나오면 성 안 어디든 갈 수 있어요.", "Out of the tunnel, you can go anywhere in the castle."),
         "small": ('그래서 요즘은 <a href="ztna-ko.html">방 하나까지만 데려다주는 안내인</a>으로 바꿔요. 땅굴 입구는 밖에서 보여서 자주 공격받고, 개인 땅굴은 땅굴 주인이 내 짐을 다 봐요.',
                   'Which is why the <a href="ztna-en.html">escort to one room</a> is taking over. The tunnel mouth is visible from outside and gets attacked often — and with a personal tunnel, the tunnel\'s owner sees all your luggage.')},
    ],
    "summary": (("<b>VPN</b> = 집에서 성까지 파는 <b>봉인된 땅굴</b>. 길 위 사람들은 못 보고, 나오면 <b>성 안</b>이에요.",
                 "A <b>VPN</b> = a <b>sealed tunnel</b> from home to the castle. The road can't see in, and you come out <b>inside</b>."),
                ("Virtual Private Network. 회사 VPN(원격 접속)과 개인 VPN(다른 마을 출구)은 같은 땅굴, 다른 쓰임이에요. IPsec, WireGuard, OpenVPN이 땅굴 파는 법. '나오면 어디든'이 문제라 ZTNA로 옮겨가는 중이에요.",
                 "Virtual Private Network. The company VPN (remote access) and the personal VPN (an exit in another town) are the same tunnel used differently. IPsec, WireGuard and OpenVPN are ways of digging. 'Out, and anywhere' is the problem, so ZTNA is taking over.")),
    "glossary": [
        ("암호화 터널", "Encrypted tunnel", ("봉인된 땅굴.", "The sealed tunnel."), ('안이 안 보여요. → <a href="ndr-ko.html">봉해진 상자</a>와 같은 원리', 'Nobody sees inside. → same idea as the <a href="ndr-en.html">sealed box</a>')),
        ("VPN 게이트웨이", "VPN gateway", ("땅굴 입구.", "The tunnel mouth."), ('성벽 쪽 출입구. 밖에서 보여서 자주 공격받아요. → <a href="ztna-ko.html">안내인 이야기</a>', 'The doorway at the wall. Visible from outside, so often attacked. → <a href="ztna-en.html">the escort story</a>')),
        ("원격 접속 VPN", "Remote-access VPN", ("집 → 성.", "Home → castle."), ("회사 땅굴. 밖에서 일하는 사람이 성 안으로.", "The company tunnel: someone working outside gets inside.")),
        ("사이트 간 VPN", "Site-to-site VPN", ("성 ↔ 지점.", "Castle ↔ branch."), ("두 건물 사이에 늘 열려 있는 땅굴.", "A tunnel between two buildings that stays open all the time.")),
        ("개인 VPN", "Consumer VPN", ("다른 마을 출구.", "An exit in another town."), ("길 사람들은 못 보지만, 땅굴 주인은 다 봐요.", "The road can't see, but the tunnel's owner sees everything.")),
        ("프로토콜", "Protocol", ("땅굴 파는 법.", "How the tunnel is dug."), ("IPsec, WireGuard, OpenVPN. 요즘은 WireGuard가 가장 빨라요.", "IPsec, WireGuard, OpenVPN. WireGuard is the fast one these days.")),
        ("분할 터널링", "Split tunneling", ("성 갈 때만 땅굴.", "Tunnel only for the castle."), ("시장 갈 땐 그냥 길로. 빠르지만 그만큼 덜 봉인돼요.", "The market by road, the castle by tunnel. Faster, but less is sealed.")),
        ("ZTNA", "ZTNA", ("땅굴 대신 안내인.", "An escort instead of a tunnel."), ('성 안이 아니라 방 하나까지만. → <a href="ztna-ko.html">안내인 이야기</a>', 'To one door, not into the castle. → <a href="ztna-en.html">the escort story</a>')),
    ],
}
