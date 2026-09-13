from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")


def mailbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="#4A5A72"/>'
            f'<rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/><path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/></g>')


def cloud(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-50 20 a25 25 0 0 1 20 -42 a30 30 0 0 1 56 -4 a22 22 0 0 1 24 46z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
            f'<rect x="-22" y="-6" width="44" height="22" fill="var(--stone-dark)"/><path d="M-26 -6 L0 -22 L26 -6 Z" fill="var(--stone)"/></g>')


def gate(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="30" width="140" height="90" fill="var(--stone-dark)"/>'
            f'{battlements(-70, 10, 140, 4, "var(--stone-dark)", 20)}<path d="M-28 120 V78 a28 28 0 0 1 56 0 V120 Z" fill="var(--night)"/></g>')


def room(x, y, s=1.0, inner=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-80" y="-10" width="160" height="110" rx="6" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="6"/>{inner}</g>')


# 1. 파수꾼이 여럿인데 서로 말을 안 한다
STATIONS = (gate(90, 100) + person(60, 30, s=0.6, face=EYES, **GUARD)
            + room(300, 120, inner=dog(20, 60, 0.8))
            + mailbox(520, 110) + person(560, 120, s=0.6, face=EYES, **GUARD)
            + cloud(660, 90, 0.9))
BUBBLES = (bubble(30, 20, 90, 36, "…", 18, "var(--panel)", "var(--line)", "bottom")
           + bubble(250, 20, 100, 36, "⟦멍?|woof?⟧", 16, "var(--panel)", "var(--line)", "bottom")
           + bubble(500, 20, 90, 36, "?", 18, "var(--panel)", "var(--line)", "bottom")
           + bubble(630, 10, 90, 36, "…", 18, "var(--panel)", "var(--line)", "bottom"))
P1 = svg(280, sky(280) + STATIONS + BUBBLES
         + label(90, 250, "⟦성문|gate⟧", 14, "var(--muted)") + label(300, 250, "⟦방|room⟧", 14, "var(--muted)")
         + label(530, 250, "⟦우편실|mailroom⟧", 14, "var(--muted)") + label(660, 250, "⟦바깥 창고|the shed outside⟧", 14, "var(--muted)"))

# 2. 도둑은 여러 곳을 지나간다
TRAIL = '<path d="M90 200 C200 150 260 150 380 190 S560 230 690 150" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
NOTHING = "⟦별거 아니네|nothing much⟧"
P2 = svg(300, sky(300) + TRAIL
         + mailbox(90, 130, 0.8) + bubble(30, 40, 130, 36, NOTHING, 13, "var(--panel)", "var(--line)", "bottom")
         + room(380, 130, 0.8, dog(10, 60, 0.7)) + bubble(310, 40, 130, 36, NOTHING, 13, "var(--panel)", "var(--line)", "bottom")
         + gate(690, 120, 0.7) + bubble(600, 40, 130, 36, NOTHING, 13, "var(--panel)", "var(--line)", "bottom")
         + person(220, 150, s=0.7, face=MASK) + person(520, 165, s=0.7, face=MASK)
         + label(380, 285, "⟦가짜 편지 → 방 안 노트북 → 성문 밖으로. 조각 하나씩은 별거 아니에요.|fake letter → a laptop in a room → out the gate. Each piece alone is nothing.⟧", 14, "var(--muted)"))

# 3. 한 무리로 묶는다 (hero)
LEADER = dog(380, 190, 1.5) + '<path d="M328 120 l6 12 13 2 -9 9 2 13 -12 -6 -12 6 2 -13 -9 -9 13 -2z" fill="#E9B44C"/>'
LINKS = "".join(f'<path d="M380 175 L{x} {y}" stroke="var(--accent)" stroke-width="3"/>' for x, y in ((110, 90), (250, 60), (540, 60), (660, 90)))
P3 = svg(340, '<rect width="760" height="340" fill="var(--accent-soft)"/>' + LINKS + LEADER
         + gate(110, 30, 0.6)
         + room(250, 40, 0.55, dog(10, 60, 0.8))
         + mailbox(540, 40, 0.7) + person(575, 40, s=0.5, face=SMILE, **GUARD)
         + cloud(660, 60, 0.7)
         + label(380, 300, "⟦누가 뭘 봤는지 서로 다 알아요|everyone knows what everyone saw⟧", 16, "var(--muted)"))

# 4. 조각을 잇고 다 같이 움직인다
PIECES = ""
for i, (txt, ic) in enumerate((("⟦가짜 편지|fake letter⟧", '<rect x="-16" y="-10" width="32" height="20" rx="3" fill="var(--panel)" stroke="var(--bad)" stroke-width="2"/><path d="M-16 -8 L0 4 L16 -8" stroke="var(--bad)" stroke-width="2" fill="none"/>'),
                               ("⟦방의 노트북|room laptop⟧", '<rect x="-16" y="-12" width="32" height="20" rx="2" fill="var(--night)"/><rect x="-14" y="-10" width="28" height="15" fill="var(--bad)"/>'),
                               ("⟦성문 밖으로|out the gate⟧", '<path d="M-14 12 V-2 a14 14 0 0 1 28 0 V12 Z" fill="var(--night)"/><path d="M4 0 h20 M18 -6 l6 6 -6 6" stroke="var(--bad)" stroke-width="3" fill="none"/>'))):
    x = 60 + i * 170
    PIECES += (f'<rect x="{x}" y="40" width="140" height="80" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
               f'<g transform="translate({x + 70},72)">{ic}</g>' + label(x + 70, 108, txt, 13, "var(--muted)"))
JOIN = '<path d="M200 80 h30 M370 80 h30 M540 80 h30" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
ONE = person(600, 30, s=0.9, face=MASK + SWEAT) + label(630, 150, "⟦한 명이었네!|one burglar!⟧", 16, "var(--bad)", cls="d")
ACTS = ""
for i, (txt, ic) in enumerate((("⟦편지 버리기|bin the letter⟧", '<path d="M-14 -10 h28 l-3 24 h-22z" fill="var(--good)"/><rect x="-18" y="-14" width="36" height="5" fill="var(--good)"/>'),
                             ("⟦방 문 잠그기|lock the room⟧", '<rect x="-12" y="-2" width="24" height="18" rx="4" fill="var(--good)"/><path d="M-7 -2 V-8 a7 7 0 0 1 14 0 V-2" stroke="var(--good)" stroke-width="4" fill="none"/>'),
                             ("⟦성문 닫기|shut the gate⟧", '<path d="M-14 12 V-2 a14 14 0 0 1 28 0 V12 Z" fill="var(--good)"/><path d="M-6 -2 h12 M-6 4 h12" stroke="var(--panel)" stroke-width="2"/>'))):
    x = 130 + i * 200
    ACTS += f'<g transform="translate({x},210)">{ic}</g>' + label(x, 248, txt, 14, "var(--ink)")
P4 = svg(270, '<rect width="760" height="270" fill="var(--panel)"/><rect y="170" width="760" height="100" fill="var(--good-soft)"/>' + PIECES + JOIN + ONE + ACTS
         + label(380, 190, "⟦한 번에|all at once⟧", 13, "var(--muted)"))

# 5. 무리 밖의 파수꾼 말은 안 듣는다
PACK = ('<circle cx="250" cy="150" r="120" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 8"/>'
        + dog(200, 120, 0.7) + dog(300, 120, 0.7) + dog(250, 200, 0.7) + person(150, 150, s=0.5, face=SMILE, **GUARD)
        + label(250, 40, "⟦한 회사 무리|one vendor's pack⟧", 15, "var(--muted)"))
OUTSIDER = (f'<g transform="translate(560,150)"><path d="M26 12 q16 -18 8 -30" stroke="var(--stone-dark)" stroke-width="7" fill="none" stroke-linecap="round"/>'
            '<ellipse cx="0" cy="8" rx="30" ry="17" fill="var(--stone-dark)"/><rect x="-22" y="18" width="9" height="16" rx="4" fill="var(--stone-dark)"/><rect x="10" y="18" width="9" height="16" rx="4" fill="var(--stone-dark)"/>'
            '<circle cx="-26" cy="-8" r="16" fill="var(--stone-dark)"/><path d="M-40 -18 q-10 10 -6 26 q8 -4 10 -16z" fill="var(--night)"/>'
            '<ellipse cx="-36" cy="-2" rx="5" ry="3.5" fill="var(--night)"/><circle cx="-30" cy="-12" r="2.5" fill="#FFF"/><circle cx="-20" cy="-12" r="2.5" fill="#FFF"/>'
            '<rect x="-18" y="-2" width="14" height="6" rx="3" fill="var(--good)"/></g>'
            + bubble(500, 60, 130, 36, "⟦나도 봤는데…|I saw it too…⟧", 14, "var(--panel)", "var(--line)", "bottom")
            + label(560, 230, "⟦다른 회사 개|another vendor's dog⟧", 15, "var(--muted)"))
P5 = svg(290, '<rect width="760" height="290" fill="var(--panel)"/>' + PACK + OUTSIDER
         + '<path d="M395 150 h60" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 6"/><path d="M418 136 l14 28 M432 136 l-14 28" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

ROOM_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/><path d="M26 52 V38 a6 6 0 0 1 12 0 V52" fill="var(--good)"/>')
GATE_I = icon('<rect x="8" y="24" width="48" height="30" fill="var(--stone-dark)"/><rect x="8" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="16" width="10" height="10" fill="var(--stone-dark)"/><path d="M24 54 V42 a8 8 0 0 1 16 0 V54Z" fill="var(--night)"/>')
MAIL_I = icon('<rect x="8" y="16" width="48" height="34" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><path d="M8 18 L32 36 L56 18" stroke="var(--accent)" stroke-width="3" fill="none"/>')
CLOUD_I = icon('<path d="M14 44 a12 12 0 0 1 6 -22 a14 14 0 0 1 27 -2 a11 11 0 0 1 8 24z" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/>')

PAGE = {
    "slug": "xdr", "order": 10,
    "title": ("한 무리가 된 파수꾼들", "The Pack"),
    "h1": ("<em>XDR</em>이 뭐예요?", "What is <em>XDR</em>?"),
    "sub": ("확장 탐지·대응(Extended Detection and Response)을 한 무리가 된 파수꾼 이야기로 풀어봤어요.",
            "Extended Detection and Response, told as a story about guards who become one pack."),
    "panels": [
        {"svg": P1, "alt": ("성문 경비, 방의 개, 우편실 사람, 바깥 창고가 각자 따로 말풍선을 띄움", "A gate guard, a room dog, a mailroom clerk and a shed outside, each with its own separate bubble"),
         "caption": ("파수꾼이 여럿인데 서로 말을 안 해요.", "Lots of guards, and none of them talk."),
         "small": ('<a href="edr-ko.html">방의 개</a>, 성문 지기, 우편실, 바깥 창고. 각자 자기 자리만 봐요.',
                   'The <a href="edr-en.html">room dog</a>, the gate guard, the mailroom, the shed outside. Each watches only its own spot.')},
        {"svg": P2, "alt": ("우편실, 방, 성문을 지나는 도둑의 점선 자취, 파수꾼마다 '별거 아니네'", "A burglar's dotted trail through the mailroom, a room and the gate, each guard saying 'nothing much'"),
         "caption": ("도둑은 여러 곳을 지나가요.", "A burglar passes through many spots."),
         "small": ("조각 하나씩은 별거 아니에요. 그래서 아무도 짖지 않아요.", "Each piece looks harmless, so nobody barks.")},
        {"svg": P3, "hero": True, "alt": ("별 목걸이를 한 큰 개가 가운데 있고 성문, 방, 우편실, 창고가 선으로 이어짐", "A big dog with a star collar in the middle, lines joining it to the gate, a room, the mailroom and the shed"),
         "caption": ("XDR은 파수꾼들을 한 무리로 묶어요.", "XDR makes the guards one pack."),
         "small": ("방 밖까지 넓혀서, 누가 뭘 봤는지 서로 다 알아요.", "It reaches past the rooms, so everyone knows what everyone saw."),
         "tricks": (4, [
             (ROOM_I, ("방", "Rooms"), ("노트북, 서버", "laptops, servers"), "calm"),
             (GATE_I, ("성문", "The gate"), ("오가는 길", "the network")),
             (MAIL_I, ("우편실", "The mailroom"), ("이메일", "email"), "warm"),
             (CLOUD_I, ("바깥 창고", "The shed outside"), ("클라우드", "the cloud")),
         ])},
        {"svg": P4, "alt": ("가짜 편지, 방의 노트북, 성문 밖 세 조각이 선으로 이어져 한 도둑이 되고, 아래엔 편지 버리기·방 문 잠그기·성문 닫기", "Three pieces — fake letter, room laptop, out the gate — joined into one burglar, and below: bin the letter, lock the room, shut the gate"),
         "caption": ("조각을 이어 붙이고, 다 같이 움직여요.", "Join the pieces, then move together."),
         "small": ("편지 버리기, 방 문 잠그기, 성문 닫기 — 한 번에.", "Bin the letter, lock the room, shut the gate — all at once.")},
        {"svg": P5, "alt": ("점선 원 안의 한 무리와, 원 밖에서 '나도 봤는데'라고 말하는 회색 개 사이에 빨간 X", "A pack inside a dashed circle, and a grey dog outside saying 'I saw it too', with a red X between them"),
         "caption": ("무리 밖의 파수꾼 말은 안 들어요.", "It doesn't listen to guards outside the pack."),
         "small": ('대개 한 회사 파수꾼끼리만 무리가 돼요. 모든 쪽지를 다 모으는 건 <a href="siem-ko.html">큰 화면</a>이 해요.',
                   'Usually only one vendor\'s guards form the pack. Collecting <em>every</em> note is still the <a href="siem-en.html">big screen</a>\'s job.')},
    ],
    "summary": (("<b>XDR</b> = 방·성문·우편실·바깥 창고의 파수꾼을 <b>한 무리</b>로 묶어, 조각을 잇고 <b>다 같이</b> 움직이는 것.",
                 "<b>XDR</b> = the guards of rooms, gate, mailroom and shed as <b>one pack</b>: join the pieces, move <b>together</b>."),
                ("Extended Detection and Response. 방의 개(EDR)를 성 전체로 넓힌 거예요. 큰 화면(SIEM)이 '쪽지를 다 모아 사람이 규칙을 적는 것'이라면, XDR은 '파수꾼들이 서로 이야기하고 규칙이 딸려오는 것'.",
                 "Extended Detection and Response: the room dog (EDR) stretched across the whole castle. Where the big screen (SIEM) gathers every note and people write the rules, XDR is guards that talk to each other, with the rules built in.")),
    "glossary": [
        ("확장", "Extended", ("방 밖으로.", "Past the rooms."), ('<a href="edr-ko.html">개</a>가 방만 봤다면, 이제 성문·우편실·창고까지.', 'The <a href="edr-en.html">dog</a> watched rooms; now the gate, mailroom and shed too.')),
        ("텔레메트리", "Telemetry", ("파수꾼의 일기.", "The guards' diaries."), ("각자 본 것을 적어 무리에 보내요.", "What each one saw, written down and sent to the pack.")),
        ("상관 분석", "Correlation", ("조각 잇기.", "Joining the pieces."), ('편지·노트북·성문을 한 이야기로. → <a href="siem-ko.html">큰 화면 이야기</a>', 'Letter, laptop and gate as one story. → <a href="siem-en.html">the big screen story</a>')),
        ("통합 대응", "Coordinated response", ("다 같이 움직이기.", "Moving together."), ("편지 버리고, 방 잠그고, 성문 닫기를 한 번에.", "Bin, lock and shut in one go.")),
        ("네이티브 XDR", "Native XDR", ("한 회사 무리.", "One vendor's pack."), ("같은 회사 파수꾼끼리만. 말이 잘 통하지만 남은 안 껴줘요.", "Only that vendor's guards. They talk well, but outsiders stay out.")),
        ("오픈 XDR", "Open XDR", ("남도 받아주는 무리.", "A pack that takes outsiders."), ("다른 회사 파수꾼도 끼워줘요. 대신 말 맞추기가 더 어려워요.", "Other vendors' guards can join. Harder to get everyone speaking the same language.")),
        ("SIEM", "SIEM", ("큰 화면.", "The big screen."), ('모든 쪽지, 사람이 적는 규칙. XDR과 나란히 써요. → <a href="siem-ko.html">큰 화면 이야기</a>', 'Every note, rules written by people. Used alongside XDR. → <a href="siem-en.html">the big screen story</a>')),
    ],
}
