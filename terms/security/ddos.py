from _draw import *

CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
HATS = (None, "#E9B44C", "var(--stone-dark)", "var(--good)", None)


def counter(x, y, s=1.0, face=SMILE):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-90" y="-120" width="180" height="200" fill="var(--stone-dark)"/>'
            f'{battlements(-90, -138, 180, 4, "var(--stone-dark)", 20)}'
            f'<rect x="-56" y="-80" width="112" height="90" rx="6" fill="var(--sky)"/><rect x="-62" y="10" width="124" height="12" rx="3" fill="{WOOD}"/>'
            f'{person(-30, -74, s=0.7, face=face, **CLERK)}{label(0, -96, "⟦창구|COUNTER⟧", 13, "#F5E6B8", cls="d")}</g>')


def zombie(x, y, s=0.5):
    """감염된 물건 — 눈이 빨간 회색 인형."""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cx="30" cy="30" r="22" fill="var(--stone)"/>'
            f'<circle cx="22" cy="28" r="4" fill="var(--bad)"/><circle cx="38" cy="28" r="4" fill="var(--bad)"/>'
            f'<rect x="8" y="52" width="44" height="60" rx="10" fill="var(--stone-dark)"/></g>')


def zombie_thing(x, y, kind, s=1.0):
    eyes = '<circle cx="-8" cy="-4" r="4" fill="var(--bad)"/><circle cx="8" cy="-4" r="4" fill="var(--bad)"/>'
    body = {"fridge": '<rect x="-16" y="-34" width="32" height="68" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M-16 -8 h32" stroke="var(--stone-dark)" stroke-width="3"/>',
            "camera": '<rect x="-22" y="-14" width="44" height="28" rx="4" fill="var(--stone-dark)"/><circle r="8" fill="var(--sky)"/><rect x="-6" y="-24" width="12" height="10" fill="var(--stone-dark)"/>',
            "router": '<rect x="-30" y="-8" width="60" height="20" rx="4" fill="var(--stone-dark)"/><rect x="-14" y="-26" width="3" height="18" fill="var(--stone-dark)"/><rect x="11" y="-26" width="3" height="18" fill="var(--stone-dark)"/>'}[kind]
    return f'<g transform="translate({x},{y}) scale({s})">{body}{eyes}</g>'


WHISTLE = '<g transform="translate(60,40)"><circle r="8" fill="var(--night)"/><rect x="6" y="-3" width="14" height="6" fill="var(--night)"/><path d="M-14 -10 a14 14 0 0 1 0 -8 M-18 -4 a20 20 0 0 1 0 -14" stroke="var(--accent)" stroke-width="2" fill="none"/></g>'

# 1. 창구는 백 명쯤 받는다
P1 = svg(300, sky(300) + counter(600, 150)
         + "".join(person(40 + i * 70, 150, s=0.65, hat=HATS[i], shirt="#4A5A72", face=SMILE) for i in range(5))
         + label(220, 260, "⟦하루 백 명|a hundred a day⟧", 14, "var(--ink)", cls="d")
         + label(380, 285, "⟦그만큼만 오면 아무 문제 없어요|as long as only that many come, all is well⟧", 13, "var(--muted)"))

# 2. 가짜 손님 만 명
CROWD = "".join(zombie(20 + (i % 9) * 48 + (i // 9) * 12, 90 + (i // 9) * 34, 0.45) for i in range(27))
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + counter(640, 150, 0.9, face=FROWN + SWEAT) + CROWD
         + person(20, 20, s=0.6, face=MASK, extra=WHISTLE)
         + person(20, 200, s=0.65, hat="#E9B44C", shirt="#4A5A72", face=FROWN) + label(60, 290, "⟦진짜 손님|a real customer⟧", 11, "var(--muted)")
         + label(300, 275, "⟦아무것도 안 사요. 줄만 서요|they buy nothing; they just stand in line⟧", 13, "var(--bad)"))

# 3. DDoS = 가짜 손님 떼로 창구 막기 (hero)
HOMES = "".join(f'<g transform="translate({x},{y})"><rect x="-26" y="0" width="52" height="40" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/><path d="M-32 0 L0 -22 L32 0 Z" fill="var(--stone)"/></g>' for x, y in ((60, 60), (60, 190), (200, 40), (200, 220), (330, 60)))
THINGS = zombie_thing(60, 78, "fridge", 0.45) + zombie_thing(60, 210, "camera", 0.6) + zombie_thing(200, 60, "router", 0.6) + zombie_thing(200, 240, "camera", 0.6) + zombie_thing(330, 80, "fridge", 0.45)
LINES = "".join(f'<path d="M{x} {y} L560 190" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 5"/>' for x, y in ((90, 90), (90, 215), (230, 70), (230, 245), (360, 90)))
P3 = svg(340, sky(340) + HOMES + LINES + THINGS + counter(640, 170, 0.85, face=FROWN + SWEAT)
         + "".join(zombie(430 + (i % 4) * 30, 180 + (i // 4) * 30, 0.4) for i in range(8))
         + person(400, 20, s=0.6, face=MASK, extra=WHISTLE) + label(460, 40, "⟦호루라기 하나로|one whistle⟧", 12, "var(--bad)", "start")
         + label(190, 300, "⟦마을 곳곳의 감염된 물건들|infected things all over town⟧", 12, "var(--muted)")
         + label(380, 328, "⟦도둑이 훔치는 게 아니라, 못 쓰게 해요|the thief steals nothing — he makes the counter useless⟧", 13, "var(--muted)"))

# 4. 넓은 마당으로 흘려보내고, 손 들게 한다
DEPOT = lambda x, y, s=0.7: (f'<g transform="translate({x},{y}) scale({s})"><rect x="-46" y="0" width="92" height="66" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
                             f'<path d="M-54 0 L0 -30 L54 0 Z" fill="var(--good)"/></g>')
HAND = '<path d="M0 30 V-4 M-12 30 V2 M12 30 V0 M-22 32 V10 M20 32 V12" stroke="#E8C9A8" stroke-width="10" stroke-linecap="round"/><rect x="-26" y="26" width="52" height="30" rx="10" fill="#E8C9A8"/>'
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + DEPOT(70, 60) + DEPOT(190, 40) + DEPOT(300, 70) + DEPOT(130, 160) + DEPOT(250, 170)
         + "".join(zombie(x, y, 0.3) for x, y in ((40, 130), (100, 120), (170, 110), (230, 130), (300, 140), (80, 230), (200, 240), (280, 240)))
         + label(190, 300, "⟦마을마다 있는 창고가 대신 받아요|depots in every town take the crowd⟧", 12, "var(--muted)")
         + f'<g transform="translate(520,120)">{HAND}</g>' + bubble(430, 20, 220, 34, "⟦사람 맞아요? 손 들어봐요|Human? Raise your hand⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + zombie(600, 100, 0.7) + label(630, 210, "⟦…|…⟧", 24, "var(--bad)", cls="d") + label(630, 240, "⟦로봇은 손을 못 들어요|robots can\'t raise a hand⟧", 11, "var(--muted)")
         + label(570, 300, "⟦그리고 한 사람당 한 번만|and one turn per person⟧", 12, "var(--muted)"))

# 5. 진짜와 똑같은 가짜, 진짜로 몰린 날
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--sky)"/>'
         + person(80, 90, s=0.8, hat=None, shirt="#4A5A72", face=SMILE) + f'<g transform="translate(200,120) scale(0.6)">{HAND}</g>'
         + '<circle cx="98" cy="112" r="3" fill="var(--bad)"/><circle cx="110" cy="112" r="3" fill="var(--bad)"/>'
         + label(190, 240, "⟦손을 드는 로봇도 있어요|some robots can raise a hand⟧", 13, "var(--bad)")
         + label(190, 270, "⟦진짜와 똑같이 생겼어요|they look exactly like real people⟧", 12, "var(--muted)")
         + "".join(person(400 + (i % 6) * 55, 80 + (i // 6) * 70, s=0.5, hat=HATS[i % 5], shirt="#4A5A72", face=SMILE) for i in range(12))
         + '<g transform="translate(640,40)"><rect x="-50" y="-18" width="100" height="36" rx="6" fill="var(--accent)"/>' + label(0, 6, "⟦오늘 세일!|SALE TODAY!⟧", 14, "#FFF") + "</g>"
         + label(570, 240, "⟦진짜로 손님이 몰린 날이에요|a day the real crowd came⟧", 13, "var(--ink)")
         + label(570, 270, "⟦가짜 떼와 헷갈려요|easy to mistake for the fake crowd⟧", 12, "var(--muted)"))

BOTNET_I = icon('<circle cx="18" cy="22" r="7" fill="var(--stone)"/><circle cx="46" cy="22" r="7" fill="var(--stone)"/><circle cx="32" cy="44" r="7" fill="var(--stone)"/><circle cx="16" cy="21" r="2" fill="var(--bad)"/><circle cx="44" cy="21" r="2" fill="var(--bad)"/><circle cx="30" cy="43" r="2" fill="var(--bad)"/>')
NOTHING_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 22 l20 20 M42 22 l-20 20" stroke="var(--line)" stroke-width="3"/>')
SPREAD_I = icon('<circle cx="32" cy="32" r="6" fill="var(--bad)"/><path d="M32 32 L10 12 M32 32 L54 12 M32 32 L10 52 M32 32 L54 52 M32 32 L32 8" stroke="var(--bad)" stroke-width="2"/>')
SIZE_I = icon('<text x="32" y="40" text-anchor="middle" font-size="13" font-weight="700" fill="var(--accent)">×10000</text>')

PAGE = {
    "slug": "ddos", "order": 37,
    "title": ("성문 앞 가짜 손님 떼", "The Fake Crowd at the Gate"),
    "h1": ("<em>DDoS</em>가 뭐예요?", "What is a <em>DDoS</em>?"),
    "sub": ("분산 서비스 거부 공격(Distributed Denial of Service)을 성문 앞에 몰려온 가짜 손님 떼 이야기로 풀어봤어요.",
            "Distributed Denial of Service, told as a story about a fake crowd swarming the castle gate."),
    "panels": [
        {"svg": P1, "alt": ("창구 앞에 손님 다섯 명이 여유롭게 줄을 섰고 '하루 백 명'", "Five customers queue comfortably at the counter; a hundred a day"),
         "caption": ("창구는 하루에 손님 백 명쯤 받을 수 있어요.", "The counter can serve about a hundred people a day."),
         "small": ("그만큼만 오면 아무 문제 없어요.", "As long as only that many come, all is well.")},
        {"svg": P2, "alt": ("호루라기를 든 도둑, 눈이 빨간 회색 가짜 손님 수십 명이 창구를 막고, 진짜 손님은 맨 뒤에서 찡그림", "A thief with a whistle; dozens of grey red-eyed fake customers jam the counter; a real customer frowns at the very back"),
         "caption": ("도둑이 가짜 손님 만 명을 한꺼번에 보내요.", "The thief sends ten thousand fake customers at once."),
         "small": ("가짜들은 아무것도 안 사요. 줄만 서요. 진짜 손님은 못 들어와요.", "The fakes buy nothing — they just stand in line. Real customers can't get in.")},
        {"svg": P3, "hero": True, "alt": ("마을 곳곳 집의 눈 빨간 냉장고·카메라·공유기에서 창구로 점선이 모이고, 도둑은 호루라기 하나로 조종", "Red-eyed fridges, cameras and routers in homes all over town send dotted lines converging on the counter; the thief controls them with one whistle"),
         "caption": ("DDoS는 가짜 손님 떼로 창구를 막는 거예요.", "A DDoS jams the counter with a fake crowd."),
         "small": ("도둑이 훔치는 게 아니라 못 쓰게 해요. 가짜 손님은 마을 곳곳의 감염된 물건(좀비)이에요.", "The thief steals nothing; he makes the counter useless. The fakes are infected things (zombies) all over town."),
         "tricks": (4, [
             (BOTNET_I, ("좀비 떼", "The zombie horde"), ("감염된 냉장고, 카메라, 공유기", "infected fridges, cameras, routers")),
             (NOTHING_I, ("아무것도 안 사요", "They buy nothing"), ("줄만 세워요", "they only fill the line"), "warm"),
             (SPREAD_I, ("마을 곳곳에서", "From all over town"), ("한 집만 막을 순 없어요", "you can't block just one house")),
             (SIZE_I, ("크기", "Sheer size"), ("초당 몇 만 명", "tens of thousands a second"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 마을마다 있는 창고 다섯 채에 가짜 손님이 흩어짐. 오른쪽: '사람 맞아요? 손 들어봐요'에 로봇이 손을 못 듦", "Left: the fake crowd scatters across five town depots. Right: Human? Raise your hand — the robot can't"),
         "caption": ("넓은 마당으로 흘려보내고, 손 들게 해요.", "Spread them thin, and make them raise a hand."),
         "small": ('마을마다 있는 <a href="cdn-ko.html">창고</a>가 대신 받아요. 로봇은 손을 못 들어요(<a href="waf-ko.html">검토원</a>). 그리고 한 사람당 한 번만.',
                   'The <a href="cdn-en.html">depots</a> in every town take the crowd. Robots can\'t raise a hand (the <a href="waf-en.html">note checker</a>). And one turn per person.')},
        {"svg": P5, "alt": ("왼쪽: 평범해 보이지만 눈이 빨간 사람이 손을 듦. 오른쪽: '오늘 세일!' 팻말 아래 진짜 손님이 잔뜩", "Left: an ordinary-looking person with red eyes raises a hand. Right: under a SALE TODAY! sign, a crowd of real customers"),
         "caption": ("진짜 손님과 똑같이 생긴 가짜도 있어요.", "Some fakes look exactly like real people."),
         "small": ("손을 드는 로봇도 있어요. 그리고 진짜로 손님이 몰리는 날(세일)과 헷갈려요. 완전히 막진 못하고 견디는 거예요.", "Some robots can raise a hand. And a real rush (a sale) looks just like an attack. You never fully block it — you ride it out.")},
    ],
    "summary": (("<b>DDoS</b> = 마을 곳곳의 감염된 물건(좀비)을 시켜 <b>가짜 손님 떼</b>로 창구를 막아, 진짜 손님이 못 오게 하는 것. 훔치는 게 아니라 <b>못 쓰게</b> 해요.",
                 "A <b>DDoS</b> = a <b>fake crowd</b> of infected things (zombies) from all over town, jamming the counter so real customers can't get in. It steals nothing — it makes things <b>unusable</b>."),
                ("Distributed Denial of Service. 2016년 Mirai 봇넷이 카메라와 공유기 수십만 대로 유명해졌어요. 방어는 창고(CDN), 세탁장(스크러빙), 손 들기(챌린지), 한 사람당 한 번(속도 제한). Cloudflare, Akamai, AWS Shield.",
                 "Distributed Denial of Service. The Mirai botnet (2016) made it famous with hundreds of thousands of cameras and routers. Defenses: depots (CDN), the laundry (scrubbing), raise-your-hand (challenges), one turn each (rate limits). Cloudflare, Akamai, AWS Shield.")),
    "glossary": [
        ("봇넷", "Botnet", ("좀비 떼.", "The zombie horde."), ("도둑이 조종하는 감염된 물건들. 주인은 몰라요.", "Infected things under the thief\'s control. Their owners have no idea.")),
        ("봇 · 좀비", "Bot · zombie", ("감염된 냉장고.", "The infected fridge."), ('시키는 대로 창구를 두드려요. → <a href="nac-ko.html">이름표 못 다는 물건</a>들이 자주 당해요', 'Knocks on the counter when told. → the <a href="nac-en.html">things that can\'t wear a tag</a> are the usual victims')),
        ("C2", "Command & control", ("도둑의 호루라기.", "The thief\'s whistle."), ('만 마리를 한 번에 움직여요. → <a href="ttp-ko.html">도둑의 버릇</a>', 'Moves ten thousand at once. → <a href="ttp-en.html">the burglar\'s habit</a>')),
        ("볼류메트릭 · L7", "Volumetric · L7", ("마당 채우기 · 창구만 두드리기.", "Flooding the yard · knocking on the counter."), ("길을 가득 메우거나, 창구 하나에 어려운 쪽지만 잔뜩.", "Either fill every road, or hit one counter with hard notes only.")),
        ("속도 제한", "Rate limiting", ("한 사람당 한 번.", "One turn per person."), ("같은 얼굴이 초당 백 번 오면 잠깐 세워요.", "The same face a hundred times a second gets paused.")),
        ("챌린지", "Challenge", ("손 들어봐요.", "Raise your hand."), ('로봇은 못 하는 걸 시켜요. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'Ask for something robots can\'t do. → <a href="waf-en.html">the note checker</a>')),
        ("스크러빙 센터", "Scrubbing center", ("세탁장.", "The laundry."), ("떼를 넓은 마당으로 보내 가짜를 걸러내고 진짜만 창구로.", "Route the crowd to a huge yard, filter the fakes, pass only real ones on.")),
        ("플래시 크라우드", "Flash crowd", ("진짜로 몰린 날.", "A real rush."), ("세일 날 손님 떼. 공격이 아닌데 똑같이 보여요.", "The sale-day crowd. Not an attack, but it looks like one.")),
    ],
}
