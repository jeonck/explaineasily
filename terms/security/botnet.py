from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BOSS = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
CARPENTER = dict(hat="#E9B44C", shirt="#4A5A72", face=SMILE)
HATS = (None, "#E9B44C", "var(--stone-dark)", "#7B3FA0")


def zombie(x, y, s=0.5):
    """홀린 마을 사람 — 눈이 빨간 회색 인형. 폭 60s, 높이 112s."""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cx="30" cy="30" r="22" fill="var(--stone)"/>'
            f'<circle cx="22" cy="28" r="4" fill="var(--bad)"/><circle cx="38" cy="28" r="4" fill="var(--bad)"/>'
            f'<rect x="8" y="52" width="44" height="60" rx="10" fill="var(--stone-dark)"/></g>')


def bug(x, y, s=1.0, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><circle cx="-12" cy="-4" r="8" fill="{color}"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8 M-14 -9 l-3 -6 M-8 -11 l1 -6" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<circle cx="-14" cy="-2" r="2" fill="#FFF"/><circle cx="-8" cy="-2" r="2" fill="#FFF"/></g>')


def house(x, y, s=1.0):
    """가운데 x, 지붕 아래선 y. 폭 ±32, 높이 y-22..y+40."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="0" width="52" height="40" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/>'
            f'<path d="M-32 0 L0 -22 L32 0 Z" fill="var(--stone)"/><rect x="-6" y="20" width="12" height="20" fill="var(--night)"/></g>')


def horn(x, y, s=1.0, waves=True):
    w = ('<path d="M52 -14 a26 26 0 0 1 0 28 M62 -24 a40 40 0 0 1 0 48 M72 -34 a54 54 0 0 1 0 68" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>' if waves else "")
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -6 h16 l30 -18 v48 l-30 -18 h-16z" fill="var(--night)"/><rect x="-6" y="-6" width="10" height="12" rx="2" fill="#E9B44C"/>{w}</g>')


def letter(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-18" y="-12" width="36" height="24" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -10 L0 4 L18 -10" stroke="#C9A86A" stroke-width="2" fill="none"/><rect x="8" y="-10" width="8" height="8" fill="var(--bad)"/></g>')


def keyring(x, y, n, s=1.0):
    keys = "".join(f'<g transform="rotate({-30 + i * (360 / max(n, 1))}) translate(0,26)"><rect x="-3" y="0" width="6" height="26" fill="#E9B44C"/><rect x="3" y="18" width="6" height="4" fill="#E9B44C"/></g>' for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="#C9822B" stroke-width="6"/>{keys}</g>'


def scissors(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-10 -6 l30 24 M-10 18 l30 -24" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="-16" cy="-10" r="7" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="-16" cy="22" r="7" fill="none" stroke="var(--bad)" stroke-width="4"/></g>')


def plank(x, y, s=1.0, rot=-12):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-40" y="-8" width="80" height="16" rx="2" fill="{WOOD}"/>'
            f'<circle cx="-28" r="2.5" fill="var(--night)"/><circle cx="28" r="2.5" fill="var(--night)"/></g>')


VOICE = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 5"/>'
GRID = lambda x0, y0, cols, rows, dx=52, dy=60, s=0.5: "".join(zombie(x0 + c * dx + (r % 2) * 14, y0 + r * dy, s) for r in range(rows) for c in range(cols))

# 1. 마을 사람들이 몰래 홀려요 — 선물 상자 속 벌레 때문에
P1 = svg(300, sky(300)
         + "".join(house(x, 90) for x in (100, 260, 420, 580))
         + person(70, 150, s=0.6, hat=HATS[0], shirt="#4A5A72", face=SMILE) + zombie(230, 150, 0.6) + person(390, 150, s=0.6, hat=HATS[1], shirt="#4A5A72", face=SMILE) + zombie(550, 150, 0.6)
         + bug(285, 200, 0.7) + bug(605, 205, 0.7) + bug(660, 150, 0.6)
         + label(100, 240, "⟦빵집|the baker⟧", 11, "var(--muted)") + label(260, 240, "⟦대장간|the smith⟧", 11, "var(--bad)") + label(420, 240, "⟦방앗간|the mill⟧", 11, "var(--muted)") + label(580, 240, "⟦구두 가게|the cobbler⟧", 11, "var(--bad)")
         + label(380, 278, "⟦벌레가 들어간 사람은 눈이 빨개져요 — 본인은 몰라요|whoever the bug gets into gets red eyes — and doesn\'t notice⟧", 12, "var(--ink)", cls="d"))

# 2. 도둑 두목이 멀리서 한 번에 명령해요
P2 = svg(330, night(330)
         + '<ellipse cx="90" cy="230" rx="120" ry="40" fill="#1B2A44"/>'
         + person(60, 70, s=1.0, **BOSS) + horn(125, 118, 0.9)
         + label(100, 262, "⟦두목: 멀리, 숨어서|the boss: far away, hidden⟧", 12, "#C9D5E6")
         + "".join(VOICE(200, 118, x, y) for x, y in ((320, 100), (420, 150), (520, 100), (620, 150), (700, 100)))
         + GRID(300, 70, 8, 3)
         + label(500, 275, "⟦수천 명이 한 번에 움직여요|thousands move at once⟧", 13, "#F5E6B8", cls="d")
         + label(380, 308, "⟦홀린 사람들은 왜 걷는지 몰라요|the spellbound don\'t know why they walk⟧", 12, "#C9D5E6"))

# 3. 봇넷 = 홀려서 조종당하는 마을 사람들 (hero)
P3 = svg(360, night(360)
         + person(50, 90, s=1.0, **BOSS) + horn(118, 138, 0.9) + label(95, 232, "⟦두목|the boss⟧", 12, "#C9D5E6")
         + "".join(zombie(230 + i * 55, 100 + (i % 2) * 40, 0.6) for i in range(6))
         + label(390, 245, "⟦홀린 마을 사람들|the spellbound villagers⟧", 12, "#C9D5E6")
         + '<path d="M548 165 L588 165" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M590 165 l-12 -7 v14z" fill="var(--bad)"/>'
         + gate(660, 80) + label(660, 232, "⟦우리 성문|our gate⟧", 12, "#C9D5E6")
         + label(380, 300, "⟦봇넷 = 두목 한 명이 조종하는 홀린 사람 떼|a botnet = a crowd of spellbound people one boss controls⟧", 14, "#F5E6B8", cls="d")
         + label(380, 336, "⟦사람 하나하나는 약해도, 수천 명이 한 번에 움직이면 무서워요|each one is weak, but thousands moving at once are scary⟧", 12, "#C9D5E6"))

# 4. 두목이 시키는 일: 성문 앞 몰려가기, 가짜 편지 뿌리기, 열쇠 꽂아보기
P4 = svg(320, sky(320)
         + gate(140, 30, 0.8) + zombie(60, 130, 0.5) + zombie(110, 145, 0.5) + zombie(160, 130, 0.5) + zombie(200, 148, 0.5)
         + label(140, 232, "⟦성문 앞에 몰려가요|swarm the gate⟧", 11, "var(--ink)")
         + zombie(350, 90, 0.6) + letter(310, 100, 0.8, -20) + letter(420, 90, 0.8, 15) + letter(330, 170, 0.8, 10) + letter(430, 165, 0.8, -12)
         + label(380, 232, "⟦가짜 편지를 뿌려요|scatter fake letters⟧", 11, "var(--ink)")
         + '<g transform="translate(600,60)"><rect x="-30" width="60" height="120" rx="3" fill="#8B5E3C"/><circle cx="20" cy="64" r="4" fill="#E9B44C"/></g>'
         + zombie(520, 100, 0.6) + keyring(600, 150, 6, 0.55)
         + label(600, 232, "⟦남의 문에 열쇠를 꽂아봐요|try keys on other doors⟧", 11, "var(--ink)")
         + label(380, 270, "⟦두목은 손 하나 안 대요 — 홀린 사람들이 다 해요|the boss never lifts a finger — the spellbound do it all⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦잡혀도 마을 사람이지, 두목이 아니에요|whoever gets caught is a villager, not the boss⟧", 12, "var(--muted)"))

# 5. 막는 법: 벌레 치우기, 두목의 목소리 끊기, 구멍 막기
P5 = svg(320, sky(320)
         + dog(110, 150, 0.9, bark=True) + bug(190, 150, 0.8) + '<path d="M176 136 l28 28 M204 136 l-28 28" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>'
         + label(140, 215, "⟦경비견이 벌레를 찾아요|the dog finds the bug⟧", 11, "var(--ink)")
         + VOICE(290, 120, 470, 120) + scissors(370, 108) + person(400, 130, s=0.6, face=SMILE, **GUARD)
         + label(380, 215, "⟦파수꾼이 목소리를 끊어요|the watcher cuts the voice⟧", 11, "var(--ink)")
         + house(640, 90, 1.3) + plank(640, 118, 0.9) + person(555, 90, s=0.75, **CARPENTER)
         + label(620, 215, "⟦목수가 구멍을 막아요|the carpenter boards the hole⟧", 11, "var(--ink)")
         + label(380, 268, "⟦벌레 치우기 + 목소리 끊기 + 구멍 막기|remove the bug + cut the voice + board the hole⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦홀린 사람이 깨어나면 두목은 혼자예요|when the spellbound wake up, the boss is alone⟧", 12, "var(--muted)"))

BUG_I = icon('<rect x="12" y="30" width="30" height="24" rx="3" fill="#E9B44C"/><rect x="24" y="30" width="6" height="24" fill="var(--bad)"/><ellipse cx="46" cy="22" rx="11" ry="8" fill="var(--bad)"/><circle cx="38" cy="19" r="5" fill="var(--bad)"/><path d="M42 12 l-3 -6 M50 12 l3 -6" stroke="var(--bad)" stroke-width="2" stroke-linecap="round"/>')
VOICE_I = icon('<path d="M10 26 h10 l14 -12 v36 l-14 -12 h-10z" fill="var(--night)"/><path d="M40 24 a10 10 0 0 1 0 16 M46 18 a18 18 0 0 1 0 28 M52 12 a26 26 0 0 1 0 40" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CROWD_I = icon('<circle cx="16" cy="20" r="7" fill="var(--stone)"/><circle cx="32" cy="18" r="7" fill="var(--stone)"/><circle cx="48" cy="20" r="7" fill="var(--stone)"/><circle cx="14" cy="19" r="1.5" fill="var(--bad)"/><circle cx="18" cy="19" r="1.5" fill="var(--bad)"/><circle cx="30" cy="17" r="1.5" fill="var(--bad)"/><circle cx="34" cy="17" r="1.5" fill="var(--bad)"/><circle cx="46" cy="19" r="1.5" fill="var(--bad)"/><circle cx="50" cy="19" r="1.5" fill="var(--bad)"/><rect x="8" y="30" width="16" height="24" rx="5" fill="var(--stone-dark)"/><rect x="24" y="28" width="16" height="26" rx="5" fill="var(--stone-dark)"/><rect x="40" y="30" width="16" height="24" rx="5" fill="var(--stone-dark)"/>')
SLEEP_I = icon(f'<circle cx="28" cy="30" r="14" fill="{SKIN}"/><path d="M14 26 Q28 8 42 26 Z" fill="#7B3FA0"/><circle cx="23" cy="31" r="3" fill="var(--bad)"/><circle cx="33" cy="31" r="3" fill="var(--bad)"/><path d="M22 40 q6 4 12 0" stroke="var(--night)" stroke-width="2" fill="none"/><text x="52" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">?</text>')

PAGE = {
    "slug": "botnet", "order": 68,
    "title": ("홀려서 조종당하는 마을 사람들", "The Spellbound Villagers"),
    "h1": ("<em>봇넷</em>이 뭐예요?", "What is a <em>Botnet</em>?"),
    "sub": ("봇넷(Botnet)을 벌레에 홀려 멀리 있는 도둑 두목의 명령대로 움직이는 마을 사람들 이야기로 풀어봤어요.",
            "A botnet, told as a story about villagers put under a spell by a bug, moving on the orders of a thief boss far away."),
    "panels": [
        {"svg": P1, "alt": ("마을 집 네 채 앞의 사람들. 대장간과 구두 가게 사람은 눈이 빨간 회색 인형이 되었고, 그 옆으로 빨간 벌레가 기어다님", "Villagers in front of four houses. The smith and the cobbler have become grey figures with red eyes, red bugs crawling beside them"),
         "caption": ("마을 사람들이 몰래 홀려요. 선물 상자 속 벌레 때문이에요.", "Villagers are quietly put under a spell. It\'s the bug from the gift box."),
         "small": ('<a href="malware-ko.html">벌레</a>가 들어간 사람은 눈이 빨개져요. 본인은 몰라요. 낮엔 평소처럼 빵을 굽고 구두를 고쳐요.',
                   'Whoever the <a href="malware-en.html">bug</a> gets into gets red eyes. They don\'t notice. By day they bake bread and fix shoes as usual.')},
        {"svg": P2, "alt": ("밤. 멀리 언덕 위의 복면 두목이 뿔나팔을 불고, 빨간 점선이 눈이 빨간 마을 사람 스물네 명에게 뻗어감", "Night. A masked boss on a far hill blows a horn; red dotted lines reach two dozen red-eyed villagers"),
         "caption": ("도둑 두목이 멀리서 한 번에 명령해요. 수천 명이 한 번에 움직여요.", "A thief boss gives one order from far away. Thousands move at once."),
         "small": ("두목은 마을에 없어요. 숨어서 목소리만 보내요. 홀린 사람들은 왜 걷는지도 몰라요.", "The boss isn\'t in the village. He hides and only sends his voice. The spellbound don\'t even know why they walk.")},
        {"svg": P3, "hero": True, "alt": ("밤. 왼쪽 복면 두목의 뿔나팔, 가운데 눈이 빨간 마을 사람 여섯, 오른쪽 우리 성문으로 향하는 빨간 화살표", "Night. The masked boss with his horn on the left, six red-eyed villagers in the middle, a red arrow toward our gate on the right"),
         "caption": ("봇넷은 두목 한 명이 조종하는 홀린 사람 떼예요.", "A botnet is a crowd of spellbound people that one boss controls."),
         "small": ("사람 하나하나는 약해요. 그런데 수천 명이 한 번에 움직이면 무서워요. 두목은 손 하나 안 대요.", "Each one is weak. But thousands moving at once are scary. The boss never lifts a finger."),
         "tricks": (4, [
             (BUG_I, ("벌레로 홀려요", "Spellbound by a bug"), ("선물 상자 속 벌레", "the bug from the gift box")),
             (VOICE_I, ("두목의 목소리", "The boss\'s voice"), ("멀리서, 한 번에", "from far away, all at once"), "warm"),
             (CROWD_I, ("수천 명이 한꺼번에", "Thousands at once"), ("성문 앞으로, 편지 뿌리기", "to the gate, scattering letters")),
             (SLEEP_I, ("홀린 사람은 몰라요", "They don\'t know"), ("낮엔 평소처럼 살아요", "by day, life as usual"), "calm"),
         ])},
        {"svg": P4, "alt": ("세 장면: 성문 앞에 몰려든 홀린 사람들, 가짜 편지를 뿌리는 홀린 사람, 남의 문에 열쇠 꾸러미를 꽂아보는 홀린 사람", "Three scenes: spellbound villagers swarming the gate, one scattering fake letters, one trying a ring of keys on someone\'s door"),
         "caption": ("두목이 시켜요. 성문 앞에 몰려가고, 가짜 편지를 뿌리고, 남의 문에 열쇠를 꽂아봐요.", "The boss gives the orders. Swarm the gate, scatter fake letters, try keys on other doors."),
         "small": ('수천 명이 <a href="ddos-ko.html">성문 앞에 몰려가면</a> 진짜 손님이 못 들어와요. <a href="phishing-ko.html">가짜 편지</a>도, <a href="bruteforce-ko.html">열쇠 꽂아보기</a>도 홀린 사람이 해요. 잡혀도 마을 사람이지 두목이 아니에요.',
                   'When thousands <a href="ddos-en.html">swarm the gate</a>, real visitors can\'t get in. <a href="phishing-en.html">Fake letters</a> and <a href="bruteforce-en.html">key-trying</a> are done by the spellbound too. Whoever gets caught is a villager, not the boss.')},
        {"svg": P5, "alt": ("경비견이 짖으며 벌레를 찾아내고, 초록 모자 파수꾼이 가위로 빨간 점선을 끊고, 목수가 집에 판자를 댐", "A barking dog finds the bug, a green-hat watcher cuts the red dotted line with scissors, and a carpenter boards up a house"),
         "caption": ("벌레를 치우고, 두목의 목소리를 끊고, 구멍을 막아요.", "Remove the bug, cut the boss\'s voice, and board up the hole."),
         "small": ('<a href="edr-ko.html">경비견</a>이 벌레를 찾고, <a href="ndr-ko.html">복도 파수꾼</a>이 두목의 목소리를 끊고, <a href="patch-ko.html">목수</a>가 판자로 구멍을 막아요. 홀린 사람이 깨어나면 두목은 혼자예요.',
                   'The <a href="edr-en.html">dog</a> finds the bug, the <a href="ndr-en.html">corridor watcher</a> cuts the boss\'s voice, and the <a href="patch-en.html">carpenter</a> boards the hole. When the spellbound wake up, the boss is alone.')},
    ],
    "summary": (("<b>봇넷</b> = <b>벌레에 홀린</b> 마을 사람 수천 명을 <b>멀리 있는 두목 한 명</b>이 목소리로 조종하는 것. 막으려면 <b>벌레 치우기</b>, <b>목소리 끊기</b>, <b>구멍 막기</b>.",
                 "<b>Botnet</b> = thousands of villagers <b>spellbound by a bug</b>, controlled by the voice of <b>one boss far away</b>. Stop it by <b>removing the bug</b>, <b>cutting the voice</b>, and <b>boarding the hole</b>."),
                ("Botnet. 악성코드에 감염된 수많은 기기(봇, 좀비)를 공격자가 C2 서버를 통해 원격으로 조종하는 네트워크예요. DDoS, 스팸, 크리덴셜 스터핑에 쓰이고, EDR 로 감염을 제거하고 C2 통신을 차단해서 막아요.",
                 "A network of many malware-infected devices (bots, zombies) that an attacker remotely controls through a C2 server. Used for DDoS, spam, and credential stuffing; stopped by removing infections with EDR and blocking C2 traffic.")),
    "glossary": [
        ("봇", "Bot", ("홀린 마을 사람 한 명.", "One spellbound villager."), ("벌레가 들어가 두목 말을 듣는 기기 하나.", "One device the bug got into, listening to the boss.")),
        ("봇넷", "Botnet", ("홀린 사람 떼.", "The whole spellbound crowd."), ("두목 하나, 홀린 사람 수천 명. 그물처럼 이어져 있어요.", "One boss, thousands of spellbound. Linked like a net.")),
        ("C2 서버", "C2 (command and control) server", ("두목의 뿔나팔.", "The boss\'s horn."), ('명령이 나오는 곳. 여기를 끊으면 떼가 흩어져요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Where the orders come from. Cut it and the crowd scatters. → <a href="ndr-en.html">the corridor watcher</a>')),
        ("좀비", "Zombie", ("눈이 빨간 마을 사람.", "The red-eyed villager."), ("봇의 다른 이름. 본인은 홀린 줄 몰라요.", "Another name for a bot. Doesn\'t know it\'s under the spell.")),
        ("DDoS", "DDoS", ("성문 앞 가짜 손님 떼.", "The fake crowd at the gate."), ('봇넷이 제일 자주 하는 일. → <a href="ddos-ko.html">성문 앞 가짜 손님 떼</a>', 'The botnet\'s most common job. → <a href="ddos-en.html">the fake crowd at the gate</a>')),
        ("스팸", "Spam", ("뿌려진 가짜 편지.", "Scattered fake letters."), ('홀린 사람 수천 명이 편지를 뿌리면 누가 보냈는지 못 찾아요. → <a href="phishing-ko.html">우체국인 척하는 편지</a>', 'When thousands of spellbound scatter letters, no one can trace the sender. → <a href="phishing-en.html">the letter pretending to be the post office</a>')),
        ("IoT 봇넷", "IoT botnet", ("홀린 냉장고와 카메라.", "Spellbound fridges and cameras."), ("사람이 아니라 물건이 홀려요. 판자를 안 대는 물건이라 홀리기 쉬워요.", "Not people but things get spellbound. Things that never get boards are easy to take.")),
        ("싱크홀", "Sinkhole", ("두목 목소리를 빈 방으로 보내기.", "Sending the boss\'s voice into an empty room."), ("홀린 사람이 두목을 부르면 경비실이 대신 받아요. 두목 목소리는 안 닿아요.", "When a spellbound villager calls the boss, the guard room answers instead. The boss\'s voice never arrives.")),
    ],
}
