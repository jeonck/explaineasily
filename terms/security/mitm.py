from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
POST = dict(hat="#5B8DEF", shirt="#5B8DEF")                       # 진짜 배달부
FAKE = dict(hat="#5B8DEF", shirt="#5B8DEF", face=MASK)            # 배달부 옷을 입은 도둑
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)


def shop(x, y, s=1.0, ink="var(--ink)"):
    """가운데 x, 위쪽 y 기준. 폭 ±56, 높이 -8..90."""
    stripes = "".join(f'<rect x="{-56 + i * 16}" y="8" width="16" height="14" fill="{"var(--bad)" if i % 2 else "#FFF8E7"}"/>' for i in range(7))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="14" width="100" height="76" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'{stripes}<rect x="-14" y="52" width="28" height="38" fill="var(--night)"/><rect x="18" y="40" width="22" height="20" fill="var(--sky)"/>'
            f'{label(0, 0, "⟦상점|SHOP⟧", 12, ink, cls="d")}</g>')


def letter(x, y, s=1.0, sealed=False, lines=(), bad_from=None):
    seal = '<rect x="50" y="26" width="20" height="18" rx="3" fill="#E9B44C"/><path d="M54 26 v-7 a6 6 0 0 1 12 0 v7" stroke="#E9B44C" stroke-width="3" fill="none"/>' if sealed else ""
    body = "".join(label(10, 30 + i * 16, t, 11, ("var(--bad)" if bad_from is not None and i >= bad_from else "#142033"), "start") for i, t in enumerate(lines))
    flap = '' if lines else '<path d="M0 4 L60 40 L120 4" stroke="#C9A86A" stroke-width="2" fill="none"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="120" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{flap}{body}{seal}</g>')


def badge(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="#E9B44C" stroke="#C9822B" stroke-width="3"/>'
            f'<path d="M-7 0 l5 5 l9 -10" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def mailbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="#4A5A72"/><rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/><path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/></g>')


ROAD = lambda x1, x2, y: f'<path d="M{x1} {y} L{x2} {y}" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="10 8"/>'
ARROW = lambda x1, x2, y, color="var(--accent)": f'<path d="M{x1} {y} L{x2} {y}" stroke="{color}" stroke-width="3" stroke-dasharray="8 6"/><path d="M{x2} {y} l-12 -7 v14z" fill="{color}"/>'

# 1. 성에서 상점으로 편지를 보내요 — 배달부가 들고 가요
P1 = svg(300, sky(300)
         + small_castle(30, 90, 0.7) + label(86, 222, "⟦우리 성|our castle⟧", 12, "var(--muted)")
         + person(150, 110, s=0.75, **ME) + letter(212, 130, 0.5)
         + ROAD(280, 560, 200)
         + person(360, 100, s=0.8, face=SMILE, **POST) + letter(414, 138, 0.45) + label(388, 222, "⟦배달부|the postman⟧", 12, "var(--muted)")
         + shop(620, 100) + label(620, 222, "⟦상점|the shop⟧", 12, "var(--muted)")
         + label(380, 270, "⟦'금화 10개 보내요' — 편지는 배달부가 들고 가요|'send 10 coins' — the postman carries the letter⟧", 13, "var(--ink)", cls="d"))

# 2. 가짜 배달부가 중간에서 뜯어 읽고 바꿔 써요 — 둘 다 몰라요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(60, 100, s=0.85, **ME) + label(90, 225, "⟦나: 몰라요|me: no idea⟧", 12, "var(--ink)")
         + letter(180, 90, 1.0, lines=("⟦금화 10개|10 coins⟧", "⟦상점으로|to the shop⟧")) + label(240, 195, "⟦뜯어서 읽고|opens and reads⟧", 12, "var(--bad)")
         + person(340, 80, s=1.0, **FAKE) + label(375, 225, "⟦가짜 배달부|the fake postman⟧", 13, "var(--bad)", cls="d")
         + letter(440, 90, 1.0, lines=("⟦금화 100개|100 coins⟧", "⟦도둑 창고로|to the thief⟧"), bad_from=0) + label(500, 195, "⟦바꿔 써요|rewrites it⟧", 12, "var(--bad)")
         + shop(660, 100, 0.9) + label(660, 225, "⟦상점: 몰라요|the shop: no idea⟧", 12, "var(--ink)")
         + label(380, 290, "⟦편지는 잘 도착했어요 — 그런데 내용이 달라요|the letter arrived just fine — but the words changed⟧", 12, "var(--ink)", cls="d"))

# 3. 중간자 공격 = 편지를 중간에서 뜯어보는 배달부 (hero)
P3 = svg(360, night(360)
         + small_castle(40, 120, 0.8) + label(104, 268, "⟦우리 성|our castle⟧", 12, "#C9D5E6")
         + ARROW(180, 300, 190) + ARROW(460, 590, 190)
         + person(345, 90, s=1.0, **FAKE) + letter(400, 150, 0.4)
         + label(380, 232, "⟦중간에 선 가짜 배달부|the fake postman in the middle⟧", 13, "#F5E6B8", cls="d")
         + shop(660, 140, 0.9, "#F5E6B8") + label(660, 268, "⟦상점|the shop⟧", 12, "#C9D5E6")
         + label(380, 305, "⟦두 사람 사이에 몰래 끼어들어 편지를 읽고 바꿔요|slips between two people, reads and rewrites their letters⟧", 13, "#F5E6B8", cls="d")
         + label(380, 338, "⟦양쪽 다 진짜 배달부라고 믿어요|both sides believe he is the real postman⟧", 12, "#C9D5E6"))

# 4. 막는 법: 봉인 편지 + 상점 신분증
P4 = svg(320, sky(320)
         + letter(90, 90, 1.0, sealed=True) + person(250, 80, s=0.85, extra=SWEAT, **FAKE)
         + bubble(230, 20, 150, 34, "⟦읽을 수가 없어!|can\'t read it!⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(200, 215, "⟦봉인 편지: 열쇠 없인 못 읽어요|sealed letter: unreadable without the key⟧", 12, "var(--ink)")
         + '<path d="M380 30 V230" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + shop(560, 90, 0.9) + badge(604, 100, 0.9) + person(650, 100, s=0.8, **ME)
         + bubble(430, 20, 190, 34, "⟦진짜 상점 도장 맞네|yes, the real shop\'s seal⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + label(570, 215, "⟦상점 신분증: 진짜인지 먼저 확인|shop ID: check it is real first⟧", 12, "var(--ink)")
         + label(380, 262, "⟦봉인 + 신분증 = 배달부가 중간에 있어도 소용없어요|seal + ID = a postman in the middle can do nothing⟧", 13, "var(--ink)", cls="d")
         + label(380, 296, "⟦봉인 편지는 암호화, 신분증은 인증서예요|the seal is encryption, the ID is a certificate⟧", 12, "var(--muted)"))

# 5. 마을 공용 우체통은 조심 — 봉인된 땅굴로 보내요
P5 = svg(300, sky(300)
         + person(20, 120, s=0.6, hat=None, shirt="#7B3FA0", face=SMILE) + mailbox(120, 100) + person(180, 125, s=0.6, hat="#E9B44C", shirt="#4A5A72", face=SMILE)
         + label(120, 215, "⟦마을 공용 우체통|the village\'s shared mailbox⟧", 11, "var(--muted)")
         + person(260, 95, s=0.7, **THIEF) + label(285, 200, "⟦누가 훔쳐볼지 몰라요|anyone could be peeking⟧", 11, "var(--bad)")
         + person(360, 90, s=0.75, **ME)
         + '<rect x="420" y="120" width="260" height="50" rx="25" fill="var(--night)" stroke="var(--good)" stroke-width="4"/>'
         + letter(520, 130, 0.5, sealed=True) + label(550, 200, "⟦봉인된 땅굴로 보내요|send it through the sealed tunnel⟧", 12, "var(--good)")
         + label(380, 250, "⟦공용 우체통은 조심, 땅굴은 안심|careful with the shared box, safe in the tunnel⟧", 13, "var(--ink)", cls="d")
         + label(380, 278, "⟦가짜 안내소가 길을 잘못 알려줄 수도 있어요|a fake info desk can also point you the wrong way⟧", 12, "var(--muted)"))

READ_I = icon('<rect x="8" y="22" width="40" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M8 22 l20 14 l20 -14" stroke="#C9A86A" stroke-width="2" fill="none"/><ellipse cx="48" cy="20" rx="12" ry="7" fill="var(--panel)" stroke="var(--bad)" stroke-width="2"/><circle cx="48" cy="20" r="3.5" fill="var(--bad)"/>')
WRITE_I = icon('<rect x="10" y="12" width="34" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="16" y="22" width="20" height="3" fill="#C9A86A"/><rect x="16" y="30" width="20" height="3" fill="var(--bad)"/><path d="M52 14 l-18 24 l-4 8 l8 -4 l18 -24z" fill="var(--bad)"/>')
BOTH_I = icon(f'<circle cx="14" cy="26" r="9" fill="{SKIN}"/><path d="M8 24 q6 6 12 0" stroke="var(--night)" stroke-width="2" fill="none"/><circle cx="50" cy="26" r="9" fill="{SKIN}"/><path d="M44 24 q6 6 12 0" stroke="var(--night)" stroke-width="2" fill="none"/><circle cx="32" cy="34" r="9" fill="{SKIN}"/><path d="M22 32 Q32 18 42 32 Z" fill="#5B8DEF"/><rect x="25" y="32" width="14" height="5" fill="#111C30"/>')
BOX_I = icon('<rect x="16" y="14" width="32" height="24" rx="8" fill="#4A5A72"/><rect x="30" y="38" width="4" height="16" fill="var(--stone-dark)"/><text x="32" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="var(--bad)">?</text>')

PAGE = {
    "slug": "mitm", "order": 65,
    "title": ("편지를 중간에서 뜯어보는 배달부", "The Postman Who Opens Your Letters"),
    "h1": ("<em>중간자 공격</em>이 뭐예요?", "What is a <em>Man-in-the-Middle Attack</em>?"),
    "sub": ("중간자 공격(Man-in-the-Middle, MITM)을 성과 상점 사이에서 편지를 몰래 뜯어보고 바꿔 쓰는 가짜 배달부 이야기로 풀어봤어요.",
            "A man-in-the-middle attack, told as a story about a fake postman who secretly opens and rewrites letters between the castle and the shop."),
    "panels": [
        {"svg": P1, "alt": ("우리 성 앞의 내가 편지를 들고 있고, 길 위의 파란 모자 배달부가 편지를 상점으로 가져감", "Me at the castle holding a letter, and a blue-hat postman on the road carrying it to the shop"),
         "caption": ("성에서 상점으로 편지를 보내요. 배달부가 들고 가요.", "We send a letter from the castle to the shop. The postman carries it."),
         "small": ("편지엔 '금화 10개 보내요' 라고 적었어요. 상점에 도착하면 상점이 읽어요.", "The letter says 'send 10 coins'. When it reaches the shop, the shop reads it.")},
        {"svg": P2, "alt": ("가운데 배달부 옷을 입은 복면 도둑. 왼쪽 편지는 '금화 10개, 상점으로', 오른쪽 편지는 빨간 글씨로 '금화 100개, 도둑 창고로'. 양 끝의 나와 상점은 웃고 있음", "A masked thief in postman\'s clothes in the middle. The left letter reads '10 coins, to the shop'; the right one, in red, '100 coins, to the thief'. Me and the shop at either end are smiling"),
         "caption": ("가짜 배달부가 편지를 뜯어 읽고, 바꿔 써요. 둘 다 몰라요.", "A fake postman opens the letter, reads it, and rewrites it. Neither side knows."),
         "small": ("편지는 잘 도착했어요. 그런데 내용이 달라요. 나도 상점도 진짜 배달부라고 믿어요.", "The letter still arrives. But the words are different. Both I and the shop believe he is the real postman.")},
        {"svg": P3, "hero": True, "alt": ("밤. 우리 성과 상점 사이 길 한가운데에 배달부 옷을 입은 복면 도둑이 서 있고, 양쪽으로 화살표가 이어짐", "Night. A masked thief in postman\'s clothes stands in the middle of the road between our castle and the shop, arrows running both ways"),
         "caption": ("중간자 공격은 편지를 중간에서 뜯어보는 배달부예요.", "A man-in-the-middle attack is a postman who opens your letters on the way."),
         "small": ("두 사람 사이에 몰래 끼어들어요. 편지를 읽고, 바꿔 쓰고, 다시 봉해서 전해요.", "He slips between two people. He reads the letter, rewrites it, seals it again, and passes it on."),
         "tricks": (4, [
             (READ_I, ("몰래 읽어요", "Reads in secret"), ("편지 속 비밀이 새요", "the letter\'s secrets leak")),
             (WRITE_I, ("바꿔 써요", "Rewrites it"), ("금화 10개가 100개로", "10 coins become 100"), "warm"),
             (BOTH_I, ("둘 다 몰라요", "Neither side knows"), ("배달부 옷을 입었으니까", "he wears the postman\'s coat")),
             (BOX_I, ("마을 공용 우체통", "The shared mailbox"), ("끼어들기 제일 쉬운 곳", "the easiest place to slip in"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 자물쇠가 달린 봉인 편지 앞에서 땀 흘리는 가짜 배달부, '읽을 수가 없어!'. 오른쪽: 금색 도장이 붙은 상점을 보고 내가 '진짜 상점 도장 맞네' 하고 확인", "Left: the fake postman sweats over a sealed letter with a lock — 'can\'t read it!'. Right: I check the shop\'s golden badge — 'yes, the real shop\'s seal'"),
         "caption": ("편지를 봉인하고, 상점이 진짜인지 먼저 확인해요.", "Seal the letter, and check the shop is real first."),
         "small": ('<a href="encryption-ko.html">봉인 편지</a>는 열쇠 없인 못 읽어요. 상점 신분증을 먼저 보면 가짜 상점에 편지를 보내는 일도 없어요.',
                   'A <a href="encryption-en.html">sealed letter</a> can\'t be read without the key. Checking the shop\'s ID first means we never send letters to a fake shop.')},
        {"svg": P5, "alt": ("왼쪽: 마을 사람들이 쓰는 공용 우체통 옆에 숨은 복면 도둑. 오른쪽: 내가 봉인 편지를 자물쇠 달린 땅굴로 보냄", "Left: a masked thief lurking by the village\'s shared mailbox. Right: I send a sealed letter through a locked tunnel"),
         "caption": ("마을 공용 우체통은 조심해요. 봉인된 땅굴로 보내면 안심이에요.", "Be careful with the village\'s shared mailbox. The sealed tunnel is safe."),
         "small": ('공용 와이파이가 마을 공용 우체통이에요. <a href="vpn-ko.html">봉인된 땅굴</a>로 보내면 돼요. 가짜 <a href="dns-ko.html">안내소</a>가 길을 잘못 알려주는 수법도 있어요.',
                   'Public Wi-Fi is the shared mailbox. Send through the <a href="vpn-en.html">sealed tunnel</a> instead. A fake <a href="dns-en.html">info desk</a> can also send you the wrong way.')},
    ],
    "summary": (("<b>중간자 공격</b> = 성과 상점 <b>사이에 몰래 끼어든</b> 가짜 배달부가 편지를 <b>읽고 바꿔 쓰는</b> 것. 막으려면 <b>봉인 편지</b>와 <b>상점 신분증 확인</b>.",
                 "<b>Man-in-the-middle</b> = a fake postman who <b>secretly slips between</b> the castle and the shop, <b>reading and rewriting</b> letters. Stop it with <b>sealed letters</b> and <b>checking the shop\'s ID</b>."),
                ("Man-in-the-Middle (MITM) Attack. 공격자가 두 통신 당사자 사이에 끼어들어 트래픽을 도청하거나 변조해요. HTTPS(TLS 암호화 + 인증서 검증)와 VPN 이 대표적인 방어예요.",
                 "An attacker inserts themselves between two communicating parties to eavesdrop on or tamper with traffic. HTTPS (TLS encryption plus certificate validation) and VPNs are the main defenses.")),
    "glossary": [
        ("중간자 공격", "Man-in-the-middle (MITM)", ("편지를 중간에서 뜯어보는 배달부.", "The postman who opens letters on the way."), ("둘 사이에 끼어들어 읽고 바꿔요. 양쪽 다 몰라요.", "Slips between two sides, reads and rewrites. Neither side knows.")),
        ("도청", "Eavesdropping", ("몰래 읽기.", "Reading in secret."), ("바꾸지 않고 읽기만 해도 비밀은 새요.", "Even without changing anything, secrets leak just by being read.")),
        ("변조", "Tampering", ("바꿔 쓰기.", "Rewriting."), ("금화 10개를 100개로, 상점 주소를 도둑 창고로.", "10 coins become 100; the shop\'s address becomes the thief\'s barn.")),
        ("공용 와이파이", "Public Wi-Fi", ("마을 공용 우체통.", "The village\'s shared mailbox."), ("누구나 쓰는 곳이라 끼어들기 제일 쉬워요.", "Anyone can use it, so it is the easiest place to slip in.")),
        ("ARP / DNS 스푸핑", "ARP / DNS spoofing", ("가짜 안내소.", "The fake info desk."), ('길을 잘못 알려줘서 편지가 도둑에게 가게 해요. → <a href="dns-ko.html">마을 안내소</a>', 'Gives wrong directions so letters go to the thief. → <a href="dns-en.html">the village info desk</a>')),
        ("HTTPS", "HTTPS", ("봉인 편지 + 상점 신분증.", "Sealed letter + shop ID."), ('둘을 한 번에 해요. 주소창의 자물쇠가 그 표시예요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Does both at once. The padlock in the address bar is the sign. → <a href="encryption-en.html">the letter no one can read without the key</a>')),
        ("인증서", "Certificate", ("상점 신분증.", "The shop\'s ID."), ("마을 관청이 찍어 준 도장이라 도둑이 흉내 못 내요.", "Stamped by the town office, so a thief can\'t fake it.")),
        ("VPN", "VPN", ("봉인된 땅굴.", "The sealed tunnel."), ('공용 우체통을 안 거치고 성까지 바로 가요. → <a href="vpn-ko.html">봉인된 땅굴</a>', 'Skips the shared mailbox and goes straight to the castle. → <a href="vpn-en.html">the sealed tunnel</a>')),
    ],
}
