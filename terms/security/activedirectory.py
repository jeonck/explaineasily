from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
MAID = dict(hat=None, shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GOLD = "#E9B44C"


def door(x, y, w=64, h=110, color=WOOD):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}"/><circle cx="{x + w - 12}" cy="{y + h * 0.55:.0f}" r="4" fill="{GOLD}"/>'


def paper(x, y, w, h, title, rows, size=11):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="24" rx="6" fill="#C9A86A"/>' + label(w / 2, 17, title, size, "#142033", cls="d")
    for i, r in enumerate(rows):
        text, color = (r, "#142033") if isinstance(r, str) else r
        out += label(w / 2, 46 + i * 20, text, size, color)
    return out + "</g>"


def ticket(x, y, s=1.0, faded=False):
    op = ' opacity="0.45"' if faded else ""
    return (f'<g transform="translate({x},{y}) scale({s})"{op}><rect x="-35" y="-18" width="70" height="36" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-26 -8 h24 M-26 0 h18 M-26 8 h24" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>'
            f'<circle cx="18" cy="0" r="9" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="18" cy="0" r="3" fill="var(--bad)"/></g>')


def key(x, y, s=1.0, color=GOLD, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><circle cx="-18" cy="0" r="11" fill="none" stroke="{color}" stroke-width="6"/>'
            f'<rect x="-8" y="-3" width="40" height="6" fill="{color}"/><rect x="18" y="3" width="4" height="8" fill="{color}"/><rect x="27" y="3" width="4" height="8" fill="{color}"/></g>')


def stamp(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-34" width="28" height="16" rx="4" fill="#5A3B22"/><rect x="-5" y="-18" width="10" height="12" fill="#5A3B22"/>'
            f'<rect x="-22" y="-6" width="44" height="10" rx="2" fill="#5A3B22"/><rect x="-24" y="4" width="48" height="5" rx="1" fill="var(--bad)"/></g>')


def chest(x, y, s=1.0, lock=True):
    lk = f'<rect x="-7" y="-6" width="14" height="12" rx="2" fill="{GOLD}"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="{GOLD}" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def bell(x, y, s=1.0, ring=True):
    arcs = '<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else ""
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="{GOLD}"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


# 1. 성이 커지니 문마다 명부가 달라요
DOORS1 = (("⟦부엌 문|kitchen door⟧", "⟦부엌 명부|kitchen roster⟧", ("⟦요리사: 들어와요|cook: may enter⟧", "var(--good)")),
          ("⟦창고 문|storeroom door⟧", "⟦창고 명부|storeroom roster⟧", ("⟦요리사: 지웠어요|cook: removed⟧", "#7A8699")),
          ("⟦금고 문|vault door⟧", "⟦금고 명부|vault roster⟧", ("⟦요리사: 들어와요?!|cook: may enter?!⟧", "var(--bad)")))
P1 = svg(320, sky(320)
         + "".join(door(cx - 32, 40) + label(cx, 30, name, 12, "var(--muted)") + person(cx + 45, 60, s=0.7, face=EYES, **GUARD)
                   + paper(cx - 70, 170, 140, 72, title, (row,)) for cx, (name, title, row) in zip((130, 380, 630), DOORS1))
         + label(380, 278, "⟦요리사는 지난달 성을 떠났어요|the cook left the castle last month⟧", 11, "var(--muted)")
         + label(380, 302, "⟦문마다 명부가 달라요 — 누가 아직 열쇠를 가졌는지 아무도 몰라요|every door keeps its own roster — nobody knows who still holds a key⟧", 11, "var(--ink)", cls="d"))

# 2. 명부 관리소 = 사람·방·열쇠를 한 장부에 (hero)
LEDGER_ROWS = (("⟦요리사|cook⟧", "⟦부엌|kitchen⟧", "⟦○|○⟧", "#142033"), ("⟦하녀|maid⟧", "⟦창고|storeroom⟧", "⟦○|○⟧", "#142033"),
               ("⟦왕|king⟧", "⟦금고|vault⟧", "⟦○|○⟧", "#142033"), ("⟦요리사 (떠남)|cook (left)⟧", "⟦—|—⟧", "⟦×|×⟧", "var(--bad)"))
P2 = svg(360, sky(360)
         + '<g transform="translate(250,40)"><rect width="260" height="170" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="260" height="26" rx="6" fill="#C9A86A"/>'
         + label(130, 18, "⟦성의 장부|THE CASTLE LEDGER⟧", 12, "#142033", cls="d")
         + label(50, 50, "⟦사람|who⟧", 11, "#7A8699", cls="d") + label(130, 50, "⟦방|room⟧", 11, "#7A8699", cls="d") + label(215, 50, "⟦열쇠|key⟧", 11, "#7A8699", cls="d")
         + '<path d="M10 58 h240" stroke="#C9A86A" stroke-width="1.5"/>'
         + "".join(label(50, 78 + i * 26, a, 11, c) + label(130, 78 + i * 26, b, 11, c) + label(215, 78 + i * 26, k, 13, c, cls="d") for i, (a, b, k, c) in enumerate(LEDGER_ROWS)) + "</g>"
         + label(380, 234, "⟦명부 관리소의 장부 한 권|one ledger at the roster office⟧", 12, "var(--ink)", cls="d")
         + person(60, 120, s=0.85, face=SMILE, **MAID) + ticket(185, 108) + '<path d="M225 108 h25" stroke="var(--muted)" stroke-width="2.5" stroke-dasharray="5 4"/>'
         + label(185, 148, "⟦하루 입장권|a one-day pass⟧", 10, "var(--muted)") + label(185, 163, "⟦관리소 도장 찍힘|stamped by the office⟧", 10, "var(--muted)")
         + "".join(door(x, 60, 40, 70) + f'<path d="M{x} 95 L515 125" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4"/>' for x in (560, 630, 700))
         + label(650, 155, "⟦문마다 장부에 물어봐요|every door asks the ledger⟧", 10, "var(--ink)")
         + label(380, 300, "⟦사람·방·열쇠를 한 장부에 — 문은 이 장부만 믿어요|people, rooms, keys in one ledger — every door trusts only this⟧", 12, "var(--ink)", cls="d")
         + label(380, 336, "⟦아침에 도장 찍힌 입장권 하나면 하루 종일 다녀요|one pass stamped in the morning opens doors all day⟧", 11, "var(--muted)"))

# 3. 도둑이 제일 노리는 곳 — 관리인 열쇠
P3 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(70, 80, s=0.9, face=MASK, extra=BAG) + key(210, 130, 1.6)
         + label(215, 200, "⟦관리인 열쇠|the keeper\'s key⟧", 12, "var(--ink)", cls="d") + label(215, 222, "⟦장부를 고칠 수 있는 단 하나의 열쇠|the one key that rewrites the ledger⟧", 10, "var(--muted)")
         + '<path d="M275 130 h115" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 5"/>'
         + castle(400, 60, 0.7)
         + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/>' for x, y, r in ((561, 178, 24), (431, 114, 16), (690, 114, 16)))
         + label(560, 232, "⟦성 전체가 열려요|the whole castle opens⟧", 12, "var(--ink)", cls="d") + label(560, 254, "⟦장부에 \'도둑 = 왕\'이라고 적으면 끝|write thief = king in the ledger, and it is over⟧", 10, "var(--muted)")
         + label(380, 290, "⟦도둑이 제일 먼저 노리는 열쇠예요|the first key every thief goes after⟧", 12, "var(--ink)", cls="d"))

# 4. 열쇠가 없어도 — 입장권 줍기, 도장 훔치기, 장부 베끼기
P4 = svg(340, night(340)
         + person(85, 60, s=0.8, face=MASK) + ticket(185, 140, 0.9) + label(185, 175, "⟦어제 것|yesterday\'s⟧", 10, "#C9D5E6")
         + label(130, 215, "⟦옛 입장권 줍기|picking up an old pass⟧", 13, "#F5E6B8", cls="d") + label(130, 237, "⟦남이 쓰던 입장권으로 문을 열어요|opens doors with someone else\'s pass⟧", 10, "#C9D5E6")
         + person(300, 60, s=0.8, face=MASK) + stamp(400, 125, 1.1) + ticket(455, 95, 0.6) + ticket(465, 140, 0.6)
         + label(380, 215, "⟦도장 자체를 훔치기|stealing the stamp itself⟧", 13, "#F5E6B8", cls="d") + label(380, 237, "⟦입장권을 마음대로 찍어요 — 왕 이름으로도|prints any pass he likes — even as the king⟧", 10, "#C9D5E6")
         + person(550, 60, s=0.8, face=MASK)
         + '<rect x="620" y="95" width="80" height="90" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="632" y="107" width="80" height="90" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M645 125 h50 M645 140 h40 M645 155 h50 M645 170 h34" stroke="#C9A86A" stroke-width="2"/>'
         + label(630, 215, "⟦장부 통째 베끼기|copying the whole ledger⟧", 13, "#F5E6B8", cls="d") + label(630, 237, "⟦모두의 암호말 지문을 들고 나가요|walks out with everyone\'s password prints⟧", 10, "#C9D5E6")
         + label(380, 290, "⟦관리인 열쇠가 없어도 — 입장권이나 도장만 있으면 돼요|no keeper\'s key needed — a pass or the stamp will do⟧", 12, "#F5E6B8", cls="d")
         + label(380, 320, "⟦종은 안 울려요: 전부 진짜 도장이 찍혀 있으니까요|no bell rings: every one of them carries a real stamp⟧", 11, "#C9D5E6"))

# 5. 막는 법 넷
P5 = svg(340, sky(340)
         + chest(100, 120, 1.2) + key(100, 62, 0.8)
         + label(100, 215, "⟦관리인 열쇠는 금고 속|keeper\'s key in the vault⟧", 12, "var(--ink)", cls="d") + label(100, 237, "⟦꺼낼 땐 둘이 함께, 잠깐만|two people, briefly⟧", 10, "var(--muted)")
         + '<circle cx="290" cy="90" r="22" fill="none" stroke="#5A3B22" stroke-width="5"/>' + key(272, 128, 0.7, rot=70) + key(306, 128, 0.7, rot=110)
         + label(290, 215, "⟦딱 필요한 열쇠만|only the keys you need⟧", 12, "var(--ink)", cls="d") + label(290, 237, "⟦요리사에게 금고 열쇠는 없어요|the cook gets no vault key⟧", 10, "var(--muted)")
         + person(430, 50, s=0.7, face=EYES, **BLUE) + paper(485, 95, 70, 60, "⟦일지|LOG⟧", ("⟦03:00 왕+1|03:00 king+1⟧",), 9) + bell(500, 60, 0.45)
         + label(470, 215, "⟦관리소 일지 감시|watching the office log⟧", 12, "var(--ink)", cls="d") + label(470, 237, "⟦새벽에 왕이 늘면 종이 울려요|a new king at 3 a.m. rings the bell⟧", 10, "var(--muted)")
         + '<g transform="translate(610,45)"><rect width="100" height="115" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M15 95 L40 95 L40 60 L70 60 L70 25 L85 25" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="5 4"/><circle cx="15" cy="95" r="6" fill="var(--good)"/><circle cx="40" cy="60" r="5" fill="var(--accent)"/><circle cx="85" cy="25" r="6" fill="var(--bad)"/></g>'
         + label(660, 215, "⟦장부 구조 점검|checking the ledger\'s shape⟧", 12, "var(--ink)", cls="d") + label(660, 237, "⟦부엌에서 금고까지 길이 있나|a path from kitchen to vault?⟧", 10, "var(--muted)")
         + label(380, 300, "⟦관리인 열쇠를 지키면 성이 지켜져요|guard the keeper\'s key, and the castle holds⟧", 12, "var(--ink)", cls="d")
         + label(380, 326, "⟦장부가 한 권이라 편하지만, 한 권이라 제일 위험해요|one ledger is handy — and one ledger is the biggest risk⟧", 11, "var(--muted)"))

LEDGER_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M12 20 h40" stroke="#C9A86A" stroke-width="3"/><path d="M25 20 v36 M39 20 v36" stroke="#C9A86A" stroke-width="1.5"/><path d="M16 30 h6 M16 40 h6 M16 50 h6 M29 30 h6 M29 40 h6 M43 30 h6 M43 40 h6" stroke="#142033" stroke-width="2"/>')
DOOR_I = icon(f'<rect x="14" y="10" width="26" height="46" rx="3" fill="{WOOD}"/><circle cx="34" cy="36" r="3" fill="{GOLD}"/><text x="50" y="30" text-anchor="middle" font-size="22" font-weight="700" fill="var(--accent)">?</text>')
TICKET_I = icon('<rect x="6" y="20" width="52" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 28 h18 M14 34 h14 M14 40 h18" stroke="#C9A86A" stroke-width="2"/><circle cx="46" cy="33" r="7" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="46" cy="33" r="2.5" fill="var(--bad)"/>')
KEY_I = icon(f'<circle cx="32" cy="32" r="24" fill="var(--bad)" opacity="0.18"/><circle cx="20" cy="32" r="8" fill="none" stroke="{GOLD}" stroke-width="5"/><rect x="27" y="30" width="26" height="5" fill="{GOLD}"/><rect x="44" y="35" width="3" height="6" fill="{GOLD}"/><rect x="50" y="35" width="3" height="6" fill="{GOLD}"/>')

PAGE = {
    "slug": "activedirectory", "order": 109,
    "title": ("성의 명부와 열쇠를 한꺼번에 쥔 관리소", "The Office That Holds Every Name and Every Key"),
    "h1": ("<em>Active Directory</em>가 뭐예요?", "What is <em>Active Directory</em>?"),
    "sub": ("Active Directory(디렉터리 서비스)와 그 보안을, 성의 사람·방·열쇠를 장부 한 권에 적어 두는 명부 관리소 이야기로 풀어봤어요.",
            "Active Directory (a directory service) and how to keep it safe, told as a story about the roster office that writes every person, room, and key in one ledger."),
    "panels": [
        {"svg": P1, "alt": ("문 셋(부엌·창고·금고)마다 경비가 따로 명부를 들고 있음. 부엌 명부엔 요리사 들어와요, 창고 명부엔 지웠어요, 금고 명부엔 여전히 들어와요?! — 요리사는 지난달 성을 떠났음", "Three doors — kitchen, storeroom, vault — each with its own guard and its own roster. Kitchen says the cook may enter, storeroom says removed, vault still says may enter?! The cook left last month"),
         "caption": ("성이 커지니 문마다 명부가 따로 있어요.", "The castle grew, and now every door keeps its own roster."),
         "small": ('요리사는 지난달 성을 떠났는데, 금고 문지기 명부엔 아직 이름이 있어요. 누가 아직 열쇠를 가졌는지 아무도 몰라요. <a href="iam-ko.html">명부 관리소</a>가 필요해요.',
                   'The cook left last month, but the vault door\'s roster still has her name. Nobody knows who still holds a key. We need a <a href="iam-en.html">roster office</a>.')},
        {"svg": P2, "hero": True, "alt": ("가운데 큰 장부: 사람·방·열쇠 세 칸에 요리사·하녀·왕이 적혀 있고, 떠난 요리사는 ×. 왼쪽 하녀는 관리소 도장 찍힌 하루 입장권을 들고, 오른쪽 문 셋은 점선으로 장부에 물어봄", "A big ledger in the middle with three columns — who, room, key — listing the cook, the maid, and the king, with the departed cook marked ×. The maid on the left holds a one-day pass stamped by the office; three doors on the right ask the ledger by dotted lines"),
         "caption": ("Active Directory는 성의 명부와 열쇠를 한꺼번에 쥔 관리소예요.", "Active Directory is the office that holds every name and every key at once."),
         "small": ('사람·방·열쇠를 장부 한 권에 적고, 문마다 이 장부에 물어봐요. 아침에 관리소 도장 찍힌 <a href="sso-ko.html">하루 입장권</a> 하나면 하루 종일 문이 열려요.',
                   'People, rooms, and keys go in one ledger, and every door asks it. One <a href="sso-en.html">one-day pass</a> stamped by the office in the morning opens doors all day.'),
         "tricks": (4, [
             (LEDGER_I, ("장부 한 권", "One ledger"), ("사람·방·열쇠 전부", "every person, room, key"), "calm"),
             (DOOR_I, ("문마다 물어봐요", "Every door asks"), ("문지기는 명부를 안 들어요", "no guard keeps his own"), "calm"),
             (TICKET_I, ("하루 입장권", "A one-day pass"), ("도장 하나로 하루 종일", "one stamp, all day")),
             (KEY_I, ("그래서 제일 노려요", "So thieves want it most"), ("장부를 쥐면 성을 쥐어요", "hold the ledger, hold the castle"), "warm"),
         ])},
        {"svg": P3, "alt": ("도둑이 관리인 열쇠를 쥐고 있고, 점선이 성으로 이어져 성문과 창문 모두에 빨간 점선 동그라미. 장부에 도둑 = 왕이라고 적으면 끝", "A thief holds the keeper\'s key; a dotted line runs to the castle, where the gate and both windows are circled in red. Write thief = king in the ledger, and it is over"),
         "caption": ("도둑이 제일 먼저 노리는 건 관리인 열쇠예요.", "The first thing a thief goes after is the keeper\'s key."),
         "small": ('장부를 고칠 수 있는 열쇠는 하나뿐이에요. 그 열쇠를 쥐면 장부에 자기 이름을 왕이라고 적고, 성 전체가 열려요. <a href="pam-ko.html">금고 속 마스터 열쇠</a>와 같은 열쇠예요.',
                   'Only one key can rewrite the ledger. Whoever holds it writes himself in as the king, and the whole castle opens. It is the same key as the <a href="pam-en.html">master key in the vault</a>.')},
        {"svg": P4, "alt": ("밤. 도둑 셋: 하나는 바닥의 어제 입장권을 줍고, 하나는 관리소 도장을 훔쳐 입장권을 찍어내고, 하나는 장부를 통째로 베껴 들고 나감", "Night. Three thieves: one picks up yesterday\'s pass from the floor, one steals the office stamp and prints passes, one walks out with a copy of the whole ledger"),
         "caption": ("관리인 열쇠가 없어도, 입장권이나 도장만 있으면 돼요.", "Even without the keeper\'s key, a pass or the stamp will do."),
         "small": ('남이 쓰던 입장권을 줍거나(<a href="session-ko.html">팔찌 훔치기</a>의 사촌), 도장 자체를 훔쳐 왕 이름으로 입장권을 찍거나, 장부를 통째로 베껴 <a href="bruteforce-ko.html">암호말 지문</a>을 들고 나가요. 다 진짜 도장이라 종이 안 울려요.',
                   'Pick up someone else\'s pass (a cousin of <a href="session-en.html">stealing the wristband</a>), steal the stamp itself and print passes as the king, or copy the whole ledger and walk out with everyone\'s <a href="bruteforce-en.html">password prints</a>. Every one carries a real stamp, so no bell rings.')},
        {"svg": P5, "alt": ("네 가지: 관리인 열쇠가 든 잠긴 금고, 열쇠 두 개뿐인 꾸러미, 일지를 보다 종을 울리는 파란 모자, 부엌에서 금고까지 점선 길이 그려진 장부 지도", "Four things: a locked chest holding the keeper\'s key, a ring with only two keys, a blue hat reading the log and ringing a bell, and a ledger map with a dotted path from kitchen to vault"),
         "caption": ("관리인 열쇠를 지키면 성이 지켜져요.", "Guard the keeper\'s key, and the castle holds."),
         "small": ('관리인 열쇠는 <a href="pam-ko.html">금고 속</a>에, 모두에게 <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>, 관리소 일지는 <a href="siem-ko.html">경비실 화면</a>과 <a href="ueba-ko.html">걸음걸이 친구</a>가 지켜보고, 부엌 열쇠에서 금고까지 이어지는 길이 없는지 장부 구조를 점검해요.',
                   'The keeper\'s key lives <a href="pam-en.html">in the vault</a>, everyone gets <a href="leastprivilege-en.html">only the keys they need</a>, the <a href="siem-en.html">guard room screen</a> and the <a href="ueba-en.html">gait-watcher</a> read the office log, and we check the ledger\'s shape for a path from a kitchen key to the vault.')},
    ],
    "summary": (("<b>Active Directory</b> = 성의 <b>사람·방·열쇠를 장부 한 권</b>에 적어 두고 문마다 그 장부에 물어보는 <b>명부 관리소</b>. 편한 만큼 <b>관리인 열쇠·입장권·도장</b>이 도둑의 첫 목표가 돼요.",
                 "<b>Active Directory</b> = the <b>roster office</b> that writes the castle\'s <b>people, rooms, and keys in one ledger</b> and lets every door ask it. As handy as it is, the <b>keeper\'s key, the passes, and the stamp</b> become a thief\'s first target."),
                ("Active Directory / Directory Service. 조직의 사용자·컴퓨터·그룹·권한을 하나의 디렉터리(도메인)에 두고 Kerberos 티켓으로 인증해요. 도메인 관리자 권한, 패스-더-해시/티켓, 골든 티켓, 디렉터리 덤프가 대표적인 공격이라 티어링·최소 권한·로그 감시·경로 분석으로 지켜요.",
                 "An organization\'s users, computers, groups, and permissions live in one directory (a domain), authenticated with Kerberos tickets. Domain-admin abuse, pass-the-hash/ticket, golden tickets, and directory dumps are the classic attacks, so it is defended with tiering, least privilege, log monitoring, and attack-path analysis.")),
    "glossary": [
        ("디렉터리 서비스", "Directory service", ("장부 한 권.", "The one ledger."), ('사람·방·열쇠를 전부 한 곳에 적어 두는 명부 관리소. → <a href="iam-ko.html">성의 명부 관리소</a>', 'The roster office that writes every person, room, and key in one place. → <a href="iam-en.html">the castle\'s roster office</a>')),
        ("도메인", "Domain", ("장부 하나가 다스리는 성.", "One ledger\'s castle."), ("이 장부 하나를 믿는 문과 사람의 범위예요. 성이 여럿이면 장부도 여럿이에요.", "The set of doors and people that trust this one ledger. Several castles, several ledgers.")),
        ("도메인 관리자", "Domain admin", ("관리인 열쇠.", "The keeper\'s key."), ('장부를 고칠 수 있는 열쇠. 도둑의 첫 목표. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'The key that rewrites the ledger. A thief\'s first target. → <a href="pam-en.html">the master key in the vault</a>')),
        ("Kerberos 티켓", "Kerberos ticket", ("도장 찍힌 하루 입장권.", "The stamped one-day pass."), ('아침에 한 번 받으면 문마다 다시 묻지 않아요. → <a href="sso-ko.html">마을 통행증</a>', 'Get it once in the morning and no door asks again. → <a href="sso-en.html">the village pass</a>')),
        ("그룹 정책", "Group Policy", ("장부에 적힌 성의 규칙.", "Castle rules written in the ledger."), ('관리소가 모든 방에 한꺼번에 내리는 규칙. 도둑이 쥐면 규칙도 바꿔요. → <a href="policy-ko.html">성의 규칙 두루마리</a>', 'Rules the office sends to every room at once. In a thief\'s hands, the rules change too. → <a href="policy-en.html">the castle\'s rule scroll</a>')),
        ("패스-더-해시 / 패스-더-티켓", "Pass-the-hash / pass-the-ticket", ("남의 입장권 줍기.", "Picking up someone else\'s pass."), ('바닥에 떨어진 어제 입장권이나 암호말 지문으로 문을 열어요. → <a href="session-ko.html">입장 팔찌를 훔치는 도둑</a>', 'Opening doors with a pass or a password print left lying around. → <a href="session-en.html">the thief who steals the wristband</a>')),
        ("골든 티켓", "Golden ticket", ("도장 자체를 훔치기.", "Stealing the stamp itself."), ("관리소 도장을 훔치면 왕 이름으로도 입장권을 찍어요. 도장을 바꾸기 전엔 안 끝나요.", "With the office stamp, a thief prints passes even as the king. It is not over until the stamp is replaced.")),
        ("계층 모델 (티어링)", "Tiering model", ("관리인 열쇠는 관리인 방에서만.", "The keeper\'s key stays in the keeper\'s room."), ('관리인 열쇠를 부엌 같은 보통 방에서 절대 안 써요. 도둑이 부엌에서 줍지 못하게. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'The keeper\'s key is never used in an ordinary room like the kitchen, so a thief can never pick it up there. → <a href="leastprivilege-en.html">only the keys you need</a>')),
    ],
}
