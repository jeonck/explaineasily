from _draw import *

BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
BLUE_W = dict(hat="#5B8DEF", shirt="#4A5A72")
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
HAMMER = '<g transform="translate(58,54) rotate(-30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#5A3B22"/><rect x="-12" y="-8" width="24" height="12" rx="2" fill="var(--stone-dark)"/></g>'
SPYGLASS = '<g transform="translate(56,52) rotate(-35)"><rect x="-4" y="0" width="8" height="30" rx="3" fill="#5A3B22"/><rect x="-6" y="-8" width="12" height="10" rx="2" fill="#C9A86A"/></g>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def tower(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="0" width="44" height="90" fill="var(--stone)"/>'
            f'{battlements(-26, -10, 52, 4, "var(--stone-dark)", 14)}</g>')


def door(x, y, s=1.0, locked=True):
    lock = '<rect x="-8" y="-4" width="16" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -4 v-6 a4 4 0 0 1 8 0 v6" stroke="#E9B44C" stroke-width="3" fill="none"/>' if locked else '<circle cx="14" cy="0" r="3" fill="#E9B44C"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-40" width="44" height="80" rx="3" fill="{WOOD}"/>{lock}</g>'


# 1. 성을 지키는 사람들은 여럿이에요 — 다 파란 모자
P1 = svg(320, sky(320) + castle(240, 30, 0.6)
         + tower(60, 100, 0.8) + person(38, 60, s=0.45, face=EYES, extra=SPYGLASS, **BLUE) + label(60, 195, "⟦망루 친구|watchtower⟧", 11, "var(--muted)")
         + '<rect x="130" y="150" width="110" height="80" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>' + bell(185, 128, 0.45, ring=False) + person(165, 168, s=0.5, face=SMILE, **BLUE) + label(185, 250, "⟦경비실|guard room⟧", 11, "var(--muted)")
         + dog(330, 215, 0.8) + label(330, 250, "⟦경비견|guard dog⟧", 11, "var(--muted)")
         + person(440, 150, s=0.7, face=EYES, **BLUE) + label(470, 250, "⟦복도 파수꾼|hall guard⟧", 11, "var(--muted)")
         + person(600, 150, s=0.7, face=SMILE, extra=HAMMER, **BLUE_W) + label(630, 250, "⟦목수|carpenter⟧", 11, "var(--muted)")
         + label(380, 282, "⟦이 모두가 한 편이에요 — 파란 모자|all of them are one side — the blue hats⟧", 14, "var(--ink)", cls="d")
         + label(380, 306, "⟦지키는 사람은 한 명이 아니에요|keeping a castle takes more than one person⟧", 12, "var(--muted)"))

# 2. 도둑은 한 번만 맞으면 되고, 지키는 편은 매번 맞아야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(door(80 + i * 62, 120, 0.7, locked=(i != 7)) for i in range(10))
         + '<rect x="494" y="70" width="46" height="100" rx="4" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + person(500, 175, s=0.6, face=MASK, extra=BAG) + label(517, 262, "⟦하나면 돼요|one is enough⟧", 12, "var(--bad)")
         + person(60, 190, s=0.65, face=FROWN + SWEAT, **BLUE) + label(200, 262, "⟦아홉 개를 잠갔는데|nine locked, and yet⟧", 12, "var(--muted)")
         + label(380, 296, "⟦도둑은 한 번만 맞으면 되고, 지키는 편은 매번 맞아야 해요|the thief only has to be right once; the blue hats have to be right every time⟧", 11, "var(--ink)"))

# 3. 블루 팀의 하루 (hero)
STEPS = (("⟦종 달기|hang bells⟧", "var(--accent)"), ("⟦듣기|listen⟧", "var(--accent)"), ("⟦쫓아가기|chase⟧", "var(--bad)"), ("⟦판자 대기|board up⟧", "var(--good)"), ("⟦연습|drill⟧", "var(--good)"))
P3 = svg(360, sky(360)
         + '<path d="M80 300 h600" stroke="var(--stone-dark)" stroke-width="4"/>'
         + "".join(f'<circle cx="{110 + i * 135}" cy="300" r="9" fill="{c}"/>' + label(110 + i * 135, 330, t, 12, "var(--ink)", cls="d") for i, (t, c) in enumerate(STEPS))
         + "".join(f'<path d="M{170 + i * 135} 300 l-8 -6 M{170 + i * 135} 300 l-8 6" stroke="var(--stone-dark)" stroke-width="3" fill="none"/>' for i in range(4))
         + bell(110, 200, 0.7, ring=False) + person(80, 110, s=0.55, face=SMILE, **BLUE) + '<path d="M96 160 l10 22" stroke="#5A3B22" stroke-width="3"/>'
         + '<rect x="205" y="150" width="80" height="60" rx="5" fill="#1B2A44" stroke="var(--stone-dark)" stroke-width="3"/>' + "".join(f'<rect x="{215 + i * 14}" y="{185 - h}" width="8" height="{h}" fill="var(--good)"/>' for i, h in enumerate((10, 18, 8, 22, 12))) + person(215, 100, s=0.5, face=EYES, **BLUE)
         + person(350, 120, s=0.6, face=EYES, **BLUE) + dog(410, 215, 0.7, bark=True) + person(440, 150, s=0.5, face=MASK, extra=BAG)
         + door(530, 190, 0.8, locked=True) + person(455, 115, s=0.5, face=SMILE, extra=HAMMER, **BLUE_W) + '<rect x="512" y="166" width="40" height="8" fill="#C9A86A" transform="rotate(-25 532 170)"/>'
         + bell(650, 150, 0.6, ring=True) + label(650, 195, "⟦가짜 종|fake bell⟧", 10, "var(--muted)") + person(620, 210, s=0.45, face=SMILE, **BLUE) + person(665, 215, s=0.45, face=SMILE, **BLUE)
         + label(380, 40, "⟦블루 팀의 하루|A DAY ON THE BLUE TEAM⟧", 15, "var(--ink)", cls="d")
         + label(380, 66, "⟦오늘 도둑이 안 와도, 매일 이걸 해요|thief or no thief, this happens every day⟧", 12, "var(--muted)"))

# 4. 레드 팀이 오면 블루 팀은 시험받는 편이에요
P4 = svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
         + person(70, 100, s=0.9, **HIRED) + bubble(150, 70, 150, 34, "⟦3주 동안 몰래|three weeks, quietly⟧", 11, "var(--panel)", "var(--bad)", "left")
         + '<path d="M200 200 L300 200" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/>'
         + person(330, 100, s=0.9, face=FROWN + SWEAT, **BLUE) + bell(430, 120, 0.7, ring=True) + label(430, 175, "⟦한 번 울렸는데 껐어요|rang once, dismissed⟧", 10, "var(--bad)")
         + '<path d="M480 200 L540 200" stroke="var(--good)" stroke-width="3"/><path d="M530 190 L542 200 L530 210" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + person(580, 100, s=0.9, face=SMILE, **BLUE) + bell(680, 100, 0.8, ring=True) + label(680, 165, "⟦새 종|new bell⟧", 11, "var(--good)", cls="d")
         + label(160, 262, "⟦시험|the test⟧", 13, "var(--ink)", cls="d") + label(380, 262, "⟦놓친 순간|the missed moment⟧", 13, "var(--ink)", cls="d") + label(620, 262, "⟦배운 것|the lesson⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦블루 팀은 지는 게 아니라 배우는 편이에요|the blue team doesn\'t lose — it learns⟧", 12, "var(--muted)"))

# 5. 아무 일도 없는 하루 — 그게 이긴 날
P5 = svg(300, sky(300) + castle(230, 30, 0.65)
         + "".join(person(x, 170, s=0.6, face=SMILE, **BLUE) for x in (100, 170, 560, 630))
         + dog(400, 205, 0.7, asleep=True) + bell(700, 120, 0.6, ring=False)
         + label(380, 262, "⟦오늘도 아무 일 없었어요|nothing happened today, again⟧", 14, "var(--ink)", cls="d")
         + label(380, 288, "⟦지키는 편이 이긴 날은 조용한 날이에요 — 그리고 내일 또 순찰|a quiet day is a day the blue hats won — and tomorrow they patrol again⟧", 11, "var(--muted)"))

PREVENT_I = icon(f'<rect x="14" y="10" width="36" height="46" rx="3" fill="{WOOD}"/><rect x="10" y="26" width="44" height="8" fill="#C9A86A" transform="rotate(-12 32 30)"/><rect x="10" y="40" width="44" height="8" fill="#C9A86A" transform="rotate(8 32 44)"/>')
DETECT_I = icon('<path d="M18 40 c0 -24 28 -24 28 0 v8 h-28z" fill="#E9B44C"/><rect x="14" y="48" width="36" height="5" rx="2" fill="#C9822B"/><path d="M12 26 a20 20 0 0 1 6 -14 M52 26 a20 20 0 0 0 -6 -14" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
RESPOND_I = icon(f'<ellipse cx="30" cy="38" rx="16" ry="10" fill="{FUR}"/><circle cx="46" cy="30" r="9" fill="{FUR}"/><path d="M50 22 l4 -8 M42 22 l-2 -8" stroke="{FUR}" stroke-width="4" stroke-linecap="round"/><path d="M56 26 l6 -4 M56 32 l7 0" stroke="var(--bad)" stroke-width="2.5" stroke-linecap="round"/>')
IMPROVE_I = icon('<path d="M12 50 L26 36 L36 44 L52 20" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M42 20 h10 v10" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "blueteam", "order": 54,
    "title": ("성을 지키는 파란 모자들", "The Blue Hats Who Keep the Castle"),
    "h1": ("<em>블루 팀</em>이 뭐예요?", "What is a <em>Blue Team</em>?"),
    "sub": ("블루 팀(Blue Team)을 성을 지키는 파란 모자들의 하루 이야기로 풀어봤어요.",
            "Blue teaming, told as a story about a day in the life of the blue hats who keep the castle."),
    "panels": [
        {"svg": P1, "alt": ("성 주변에 파란 모자를 쓴 사람들: 망루 친구, 경비실, 경비견, 복도 파수꾼, 목수", "Around the castle, people in blue hats: the watchtower friend, the guard room, the guard dog, the hall guard, the carpenter"),
         "caption": ("성을 지키는 사람은 한 명이 아니에요.", "Keeping a castle takes more than one person."),
         "small": ('<a href="cti-ko.html">망루 친구</a>, <a href="soc-ko.html">경비실</a>, <a href="edr-ko.html">경비견</a>, <a href="ndr-ko.html">복도 파수꾼</a>, <a href="patch-ko.html">목수</a>. 다 파란 모자를 써요 — 이 모두가 블루 팀이에요.',
                   'The <a href="cti-en.html">watchtower friend</a>, the <a href="soc-en.html">guard room</a>, the <a href="edr-en.html">guard dog</a>, the <a href="ndr-en.html">hall guard</a>, the <a href="patch-en.html">carpenter</a>. All in blue hats — together, they\'re the blue team.')},
        {"svg": P2, "alt": ("문 열 개 중 아홉 개는 자물쇠가 채워져 있고, 하나가 열려 있음. 도둑이 그 문 앞에 서 있고 파란 모자는 땀을 흘림", "Ten doors, nine locked and one open; a thief stands at the open one while a blue hat sweats"),
         "caption": ("도둑은 한 번만 맞으면 되고, 지키는 편은 매번 맞아야 해요.", "The thief only has to be right once. The blue hats have to be right every time."),
         "small": ("문 열 개 중 아홉 개를 잠가도, 열린 하나면 도둑한텐 충분해요. 그래서 지키는 편은 쉬는 날이 없어요.", "Lock nine doors out of ten, and the one left open is all a thief needs. That\'s why the blue hats never get a day off.")},
        {"svg": P3, "hero": True, "alt": ("블루 팀의 하루: 종 달기 → 듣기(화면) → 쫓아가기(경비견과 도둑) → 판자 대기(목수) → 연습(가짜 종). 다섯 점이 이어진 길", "A day on the blue team: hang bells → listen (the screen) → chase (dog and thief) → board up (carpenter) → drill (a fake bell), five points along one path"),
         "caption": ("블루 팀은 도둑이 안 와도 매일 이걸 해요.", "Thief or no thief, the blue team does this every day."),
         "small": ("종을 달고, 듣고, 울리면 쫓아가고, 틈엔 판자를 대고, 가끔 가짜 종으로 연습해요. 미리 막고, 알아채고, 쫓아가고, 매일 조금씩 나아져요.", "Hang bells, listen, chase when one rings, board up the cracks, and now and then drill with a fake bell. Prevent, detect, respond, and get a little better every day."),
         "tricks": (4, [
             (PREVENT_I, ("미리 막기", "Prevent"), ("판자, 자물쇠, 문지기", "boards, locks, doorkeepers")),
             (DETECT_I, ("알아채기", "Detect"), ("종을 달고 듣기", "hang bells and listen"), "warm"),
             (RESPOND_I, ("쫓아가기", "Respond"), ("울리면 바로", "the moment it rings"), "warm"),
             (IMPROVE_I, ("매일 조금씩", "Improve"), ("놓친 건 새 종으로", "every miss becomes a bell"), "calm"),
         ])},
        {"svg": P4, "alt": ("고용한 도둑이 3주 동안 몰래 → 파란 모자가 종 한 번 울린 걸 껐음 → 배운 뒤 새 종을 달고 웃는 파란 모자. 시험, 놓친 순간, 배운 것", "The hired thief, three weeks quietly → a blue hat dismissed the one bell → a smiling blue hat with a new bell. The test, the missed moment, the lesson"),
         "caption": ("레드 팀이 오면, 블루 팀은 시험받는 편이에요.", "When the red team comes, the blue team is the one being tested."),
         "small": ('<a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>이 몰래 들어와요. 종을 놓쳤으면 그 순간을 배워서 새 종을 달아요. 블루 팀은 지는 게 아니라 배우는 편이에요.',
                   'The <a href="redteam-en.html">team that plays the real thief</a> sneaks in. If a bell was missed, the blue team learns from that moment and hangs a new one. It doesn\'t lose — it learns.')},
        {"svg": P5, "alt": ("맑은 날의 성, 파란 모자 넷이 웃고 있고 경비견은 자고 종은 조용함. '오늘도 아무 일 없었어요'", "The castle on a clear day; four blue hats smiling, the dog asleep, the bell silent. Nothing happened today, again"),
         "caption": ("아무 일도 없는 하루 — 그게 블루 팀이 이긴 날이에요.", "A day when nothing happens — that\'s a day the blue team won."),
         "small": ("지키는 편의 승리는 조용해요. 아무도 박수 치지 않지만, 내일 또 순찰을 돌아요.", "A defender\'s victory is quiet. No one claps, and tomorrow they patrol again.")},
    ],
    "summary": (("<b>블루 팀</b> = 성을 지키는 편 전부. 매일 <b>미리 막고 → 알아채고 → 쫓아가고 → 조금씩 나아지며</b>, 도둑이 안 온 조용한 날이 이긴 날.",
                 "<b>Blue team</b> = everyone on the defending side. Every day they <b>prevent → detect → respond → improve</b>, and a quiet day with no thief is a day they won."),
                ("Blue Team. 조직의 방어를 맡는 편 전체를 뜻해요 — 예방, 모니터링과 탐지, 사고 대응, 그리고 지속적인 개선. SOC는 블루 팀의 한 방이에요.",
                 "The entire defending side of an organization — prevention, monitoring and detection, incident response, and continuous improvement. The SOC is one room of the blue team.")),
    "glossary": [
        ("블루 팀", "Blue team", ("파란 모자 전부.", "All the blue hats."), ("경비실만이 아니라 망루, 경비견, 목수까지 지키는 편 전체예요.", "Not just the guard room — the watchtower, the dog, the carpenter; the whole defending side.")),
        ("레드 팀", "Red team", ("진짜 도둑인 척하는 팀.", "The team that plays the real thief."), ('블루 팀을 시험하는 편. → <a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>', 'The side that tests the blue team. → <a href="redteam-en.html">the team that plays the real thief</a>')),
        ("SOC", "SOC", ("블루 팀의 경비실.", "The blue team\'s guard room."), ('종을 듣는 방 하나. → <a href="soc-ko.html">성의 경비실</a>', 'The one room that listens for bells. → <a href="soc-en.html">the guard room</a>')),
        ("방어자의 딜레마", "Defender\'s dilemma", ("매번 맞아야 해요.", "Right every time."), ("도둑은 한 번, 지키는 편은 매번. 그래서 종과 순서표가 필요해요.", "The thief once, the defenders every time. That\'s why you need bells and a book.")),
        ("탐지 규칙", "Detection rule", ("달아둔 종.", "A bell you hung."), ('놓친 순간마다 하나씩 늘어요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'One more for every missed moment. → <a href="siem-en.html">the guard room screen</a>')),
        ("사고 대응", "Incident response", ("울리면 쫓아가기.", "Chase when it rings."), ('순서표대로. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'By the book. → <a href="incident-en.html">the order of things when a thief gets in</a>')),
        ("하드닝", "Hardening", ("판자 대기.", "Boarding up."), ('도둑이 오기 전에 틈을 줄여요. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'Fewer cracks before any thief comes. → <a href="patch-en.html">the boards the carpenter sent</a>')),
        ("퍼플 팀", "Purple team", ("도둑과 같은 책상.", "One table with the thief."), ('블루 팀이 제일 빨리 배우는 방법. → <a href="purpleteam-ko.html">같은 책상에 앉은 도둑과 파수꾼</a>', 'The fastest way the blue team learns. → <a href="purpleteam-en.html">the thief and the guard at one table</a>')),
    ],
}
