from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)   # 고용한 도둑 (pentest 와 같은 차림)
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")                                   # 경비실 친구
PURPLE = "#8E5BD6"
PURPLE_SOFT = "#EDE3FA"


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def screen(x, y, w=140, h=90, inner=""):
    return f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#1B2A44" stroke="var(--stone-dark)" stroke-width="4"/>{inner}</g>'


def table(x, y, w):
    return f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="4" fill="{WOOD}"/><rect x="{x + 12}" y="{y + 14}" width="10" height="40" fill="#5A3B22"/><rect x="{x + w - 22}" y="{y + 14}" width="10" height="40" fill="#5A3B22"/>'


def check(x, y, ok, s=1.0):
    if ok:
        return f'<g transform="translate({x},{y}) scale({s})"><circle r="11" fill="var(--good)"/><path d="M-5 0 l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none"/></g>'
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="11" fill="var(--bad)"/><path d="M-5 -5 l10 10 M5 -5 l-10 10" stroke="#FFF" stroke-width="3"/></g>'


# 1. 빨간 팀은 몰래, 파란 팀은 기다려요 — 그리고 몇 주 뒤 두꺼운 보고서
P1 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/><rect x="376" width="8" height="262" fill="var(--stone-dark)"/>'
         + person(100, 90, s=0.9, **HIRED) + '<path d="M180 150 L300 150" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/>' + label(190, 60, "⟦빨간 팀|red team⟧", 13, "var(--bad)", cls="d") + label(190, 240, "⟦몰래 들어가 봐요|sneaks in, quietly⟧", 12, "var(--muted)")
         + person(500, 90, s=0.9, face=SMILE, **BLUE) + screen(590, 100, 120, 80) + bell(650, 40, 0.6, ring=False) + label(570, 60, "⟦파란 팀|blue team⟧", 13, "var(--good)", cls="d") + label(570, 240, "⟦종을 기다려요|waits for the bell⟧", 12, "var(--muted)")
         + label(380, 282, "⟦서로 뭘 하는지 몰라요 — 벽 너머예요|neither knows what the other is doing — there\'s a wall between them⟧", 12, "var(--muted)"))

# 2. 따로 하면 느려요
P2 = svg(300, sky(300)
         + '<g transform="translate(60,60)"><rect width="110" height="150" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="110" height="26" rx="6" fill="#C9A86A"/>' + label(55, 18, "⟦보고서|REPORT⟧", 11, "#142033", cls="d") + "".join(f'<rect x="12" y="{40 + i * 14}" width="{86 - (i % 3) * 20}" height="4" rx="2" fill="#C9A86A"/>' for i in range(7)) + "</g>"
         + label(115, 240, "⟦몇 주 뒤 두꺼운 보고서|weeks later, a thick report⟧", 12, "var(--muted)")
         + '<path d="M190 130 L250 130 M310 130 L370 130 M430 130 L490 130 M610 130 L650 130" stroke="var(--muted)" stroke-width="3"/>'
         + "".join(f'<path d="M{x} 120 L{x + 12} 130 L{x} 140" stroke="var(--muted)" stroke-width="3" fill="none"/>' for x in (240, 360, 480, 640))
         + person(250, 70, s=0.75, face=FROWN, **BLUE) + label(280, 240, "⟦읽기|read⟧", 12, "var(--muted)")
         + bell(400, 110, 0.7, ring=False) + label(400, 240, "⟦종 달기|hang bells⟧", 12, "var(--muted)")
         + '<g transform="translate(520,90)"><rect width="80" height="70" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(40, 24, "⟦내년|NEXT YEAR⟧", 11, "#142033", cls="d") + label(40, 52, "⟦?|?⟧", 22, "var(--bad)", cls="d") + "</g>" + label(560, 240, "⟦다시 확인|check again⟧", 12, "var(--muted)")
         + person(680, 140, s=0.7, face=MASK, extra='<rect x="50" y="70" width="30" height="26" rx="4" fill="var(--night)"/>') + label(700, 240, "⟦진짜 도둑|a real thief⟧", 12, "var(--bad)")
         + label(380, 282, "⟦그 사이 종은 못 울린 채 그대로예요|meanwhile the bell stays silent⟧", 13, "var(--muted)"))

# 3. 보라 팀 = 같은 책상 (hero)
P3 = svg(360, f'<rect width="760" height="360" fill="{PURPLE_SOFT}"/>'
         + f'<rect x="0" y="0" width="760" height="34" fill="{PURPLE}"/>' + label(380, 23, "⟦빨강 + 파랑 = 보라|RED + BLUE = PURPLE⟧", 14, "#FFF", cls="d")
         + table(200, 230, 360)
         + person(230, 120, s=0.9, **HIRED) + bubble(150, 50, 220, 34, "⟦지금 서쪽 창문으로 들어갈게|going in through the west window now⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + person(470, 120, s=0.9, face=EYES, **BLUE) + bubble(410, 50, 200, 34, "⟦…종이 안 울렸어|…the bell didn\'t ring⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + screen(330, 150, 110, 70, inner='<rect x="10" y="12" width="90" height="46" rx="3" fill="#0A1120"/>' + label(55, 42, "⟦조용|quiet⟧", 12, "#C9D5E6"))
         + bell(660, 110, 0.9, ring=True) + label(660, 180, "⟦새 종|new bell⟧", 12, "#142033", cls="d") + '<path d="M600 130 L625 130" stroke="var(--good)" stroke-width="3"/><path d="M615 120 L627 130 L615 140" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + "".join(label(x, 315, t, 12, PURPLE, cls="d") for x, t in ((120, "⟦① 미리 말하고|① say it first⟧"), (300, "⟦② 화면 보고|② watch the screen⟧"), (480, "⟦③ 그 자리에서 종 달고|③ hang a bell right there⟧"), (660, "⟦④ 다시 해봐|④ try again⟧")))
         + label(380, 344, "⟦한 번에 한 버릇씩, 같은 방에서|one habit at a time, in the same room⟧", 13, "#5B4A7A"))

# 4. 도둑의 버릇 목록을 한 줄씩
ROWS = (("⟦가짜 편지 보내기|send a fake letter⟧", True), ("⟦서쪽 창문 넘기|climb the west window⟧", False), ("⟦열쇠 복사하기|copy a key⟧", True), ("⟦창고 상자 옮기기|move the storeroom chests⟧", False), ("⟦일지 지우기|erase the diary⟧", True))
P4 = svg(320, sky(320)
         + '<g transform="translate(120,30)"><rect width="520" height="200" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="520" height="30" rx="8" fill="#C9A86A"/>' + label(260, 20, "⟦도둑의 버릇 목록|THE THIEF\'S HABITS⟧", 13, "#142033", cls="d")
         + label(440, 20, "⟦종?|bell?⟧", 12, "#142033", cls="d") + label(490, 20, "⟦할 일|to do⟧", 12, "#142033", cls="d")
         + "".join(label(20, 60 + i * 32, t, 13, "#142033", "start") + check(440, 56 + i * 32, ok, 0.9) + ("" if ok else label(490, 60 + i * 32, "⟦종 달기|hang bell⟧", 11, "var(--bad)")) for i, (t, ok) in enumerate(ROWS)) + "</g>"
         + person(30, 200, s=0.6, **HIRED) + person(690, 200, s=0.6, face=SMILE, **BLUE)
         + label(380, 262, "⟦초록은 울렸고, 빨강은 안 울렸어요|green rang, red stayed silent⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦빨강 줄이 하나씩 초록으로 바뀌어요|one by one, red lines turn green⟧", 12, "var(--muted)"))

# 5. 다음 진짜 도둑이 오면
P5 = svg(300, night(300)
         + person(120, 120, s=0.85, face=MASK, extra='<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/>') + '<rect x="200" y="80" width="70" height="90" rx="3" fill="#1B2A44" stroke="#C9D5E6" stroke-width="3"/><path d="M235 80 v90 M200 125 h70" stroke="#C9D5E6" stroke-width="3"/>' + label(235, 200, "⟦서쪽 창문|west window⟧", 11, "#C9D5E6")
         + bell(400, 90, 1.1, ring=True) + label(400, 170, "⟦울렸다!|it rang!⟧", 16, "#F5E6B8", cls="d")
         + person(540, 130, s=0.8, face=SMILE, **BLUE) + person(640, 130, s=0.8, **HIRED)
         + f'<path d="M600 175 l8 8 l14 -14" stroke="{PURPLE}" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + label(600, 250, "⟦같이 달아둔 종이에요|the bell they hung together⟧", 12, "#C9D5E6")
         + label(380, 285, "⟦진짜 도둑은 처음부터 종소리를 들어요|the real thief hears the bell from the very first step⟧", 12, "#C9D5E6"))

SAY_I = icon('<path d="M10 14 h44 v30 h-26 l-10 10 v-10 h-8z" fill="var(--bad)"/><path d="M20 24 h24 M20 32 h16" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>')
WATCH_I = icon('<rect x="10" y="14" width="44" height="32" rx="4" fill="#1B2A44" stroke="var(--stone-dark)" stroke-width="3"/><rect x="24" y="48" width="16" height="6" fill="var(--stone-dark)"/><circle cx="32" cy="30" r="6" fill="var(--good)"/>')
HANG_I = icon('<path d="M18 40 c0 -24 28 -24 28 0 v8 h-28z" fill="#E9B44C"/><rect x="14" y="48" width="36" height="5" rx="2" fill="#C9822B"/><path d="M32 8 v10" stroke="#5A3B22" stroke-width="3"/><path d="M26 10 h12" stroke="#5A3B22" stroke-width="3"/>')
AGAIN_I = icon(f'<path d="M44 32 a12 12 0 1 1 -4 -9" stroke="{PURPLE}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 14 l6 10 -12 2z" fill="{PURPLE}"/>')

PAGE = {
    "slug": "purpleteam", "order": 52,
    "title": ("같은 책상에 앉은 도둑과 파수꾼", "The Thief and the Guard at One Table"),
    "h1": ("<em>퍼플 팀</em>이 뭐예요?", "What is a <em>Purple Team</em>?"),
    "sub": ("퍼플 팀(Purple Team)을 고용한 도둑과 경비실 친구가 같은 책상에 앉는 이야기로 풀어봤어요.",
            "Purple teaming, told as a story about the hired thief and the guard sitting down at the same table."),
    "panels": [
        {"svg": P1, "alt": ("벽으로 나뉜 두 방. 왼쪽 빨간 팀(고용한 도둑)은 몰래 들어가고, 오른쪽 파란 팀(경비실)은 화면 앞에서 종을 기다림", "Two rooms split by a wall: on the left the red team (the hired thief) sneaks in; on the right the blue team (the guard room) waits for the bell"),
         "caption": ("빨간 팀은 몰래 들어가고, 파란 팀은 종을 기다려요.", "The red team sneaks in; the blue team waits for the bell."),
         "small": ('<a href="pentest-ko.html">우리가 고용한 도둑</a>과 <a href="soc-ko.html">경비실 친구</a>. 둘은 벽 너머에서 서로 뭘 하는지 몰라요.',
                   'The <a href="pentest-en.html">thief we hired</a> and the <a href="soc-en.html">guard room</a>. There\'s a wall between them, and neither knows what the other is doing.')},
        {"svg": P2, "alt": ("두꺼운 보고서 → 읽기 → 종 달기 → 내년 다시 확인, 그 끝에 진짜 도둑", "A thick report → read → hang bells → check again next year, with a real thief at the end of the line"),
         "caption": ("따로 하면 느려요.", "Done separately, it\'s slow."),
         "small": ("몇 주 뒤 두꺼운 보고서가 와요. 읽고, 고치고, 내년에 다시 확인해요. 그 사이 종은 못 울린 채 그대로예요.", "Weeks later a thick report arrives. Read it, fix things, check again next year. Meanwhile the bell stays silent.")},
        {"svg": P3, "hero": True, "alt": ("보라색 방, 같은 책상. 고용한 도둑이 '지금 서쪽 창문으로 들어갈게' 하고, 경비실 친구가 화면을 보며 '종이 안 울렸어', 옆에 새 종. 아래에 ① 미리 말하고 ② 화면 보고 ③ 그 자리에서 종 달고 ④ 다시 해봐", "A purple room, one table. The hired thief says going in through the west window now; the guard watches the screen and says the bell didn\'t ring; a new bell beside. Below: say it first, watch the screen, hang a bell right there, try again"),
         "caption": ("퍼플 팀은 도둑과 파수꾼이 같은 책상에 앉는 거예요.", "A purple team is the thief and the guard at one table."),
         "small": ("도둑이 미리 말하고 움직여요. 파수꾼은 종이 울렸는지 바로 봐요. 안 울렸으면 그 자리에서 새 종을 달고, 다시 해봐요.", "The thief says what they\'ll do, then does it. The guard checks whether the bell rang. If not, they hang a new bell right there and try again."),
         "tricks": (4, [
             (SAY_I, ("미리 말하고", "Say it first"), ("몰래가 아니라 크게", "out loud, not sneaky"), "warm"),
             (WATCH_I, ("화면 보고", "Watch the screen"), ("종이 울렸나?", "did the bell ring?")),
             (HANG_I, ("그 자리에서 종 달기", "Hang a bell now"), ("내년까지 안 기다려요", "no waiting till next year")),
             (AGAIN_I, ("다시 해봐", "Try again"), ("이번엔 울리나?", "does it ring this time?"), "calm"),
         ])},
        {"svg": P4, "alt": ("도둑의 버릇 목록: 가짜 편지 ✓, 서쪽 창문 × 종 달기, 열쇠 복사 ✓, 창고 상자 옮기기 × 종 달기, 일지 지우기 ✓. 양쪽에 도둑과 파수꾼", "The thief\'s habits list: fake letter ✓, west window × hang bell, copy a key ✓, move chests × hang bell, erase the diary ✓; the thief and the guard on either side"),
         "caption": ("도둑의 버릇 목록을 한 줄씩 해봐요.", "Go through the thief\'s habits, one line at a time."),
         "small": ('<a href="attack-ko.html">도둑 백과사전</a>에서 버릇을 하나씩 골라 해봐요. 초록은 종이 울린 것, 빨강은 안 울린 것. 빨강 줄이 하나씩 초록으로 바뀌어요.',
                   'Pick habits one by one from the <a href="attack-en.html">thief encyclopedia</a>. Green means the bell rang; red means it didn\'t. One by one, red lines turn green.')},
        {"svg": P5, "alt": ("밤, 진짜 도둑이 서쪽 창문에 손을 대자마자 종이 크게 울림. 파수꾼과 고용한 도둑이 나란히 서서 보라색 체크", "Night: a real thief touches the west window and the bell rings loudly; the guard and the hired thief stand side by side with a purple check mark"),
         "caption": ("다음에 진짜 도둑이 오면, 종이 울려요.", "When the next real thief comes, the bell rings."),
         "small": ("같이 달아둔 종이에요. 도둑과 파수꾼이 한 팀이 되면, 진짜 도둑은 첫걸음부터 종소리를 들어요.", "It\'s the bell they hung together. When the thief and the guard are one team, the real thief hears the bell from the very first step.")},
    ],
    "summary": (("<b>퍼플 팀</b> = 고용한 도둑(빨강)과 경비실(파랑)이 <b>같은 책상</b>에 앉아, <b>한 버릇씩 해보고 → 종이 울렸는지 보고 → 그 자리에서 종을 다는</b> 일.",
                 "<b>Purple team</b> = the hired thief (red) and the guard room (blue) at <b>one table</b>: <b>try one habit → check the bell → hang a new bell right there</b>."),
                ("Purple Team. 레드 팀과 블루 팀이 따로 움직이는 대신 함께 앉아 공격 기법을 하나씩 실행하고 탐지 여부를 즉시 확인하며 탐지 규칙을 바로 보강하는 협업 방식이에요.",
                 "Instead of red and blue working apart, they sit together, run one attack technique at a time, check detection immediately, and strengthen the rules on the spot.")),
    "glossary": [
        ("레드 팀", "Red team", ("고용한 도둑.", "The hired thief."), ('진짜 도둑처럼 들어가 보는 편. → <a href="pentest-ko.html">우리가 고용한 도둑</a>', 'The side that breaks in like a real thief would. → <a href="pentest-en.html">the thief we hired</a>')),
        ("블루 팀", "Blue team", ("경비실 친구.", "The guard room."), ('종을 지키고 도둑을 잡는 편. → <a href="soc-ko.html">성의 경비실</a>', 'The side that watches the bell and catches thieves. → <a href="soc-en.html">the guard room</a>')),
        ("퍼플 팀", "Purple team", ("둘이 같은 책상.", "Both at one table."), ("따로 있는 팀이 아니라 함께 앉는 방식이에요. 빨강 + 파랑 = 보라.", "Not a third team — a way of sitting together. Red + blue = purple.")),
        ("공격 에뮬레이션", "Adversary emulation", ("도둑 버릇 따라 하기.", "Copying a thief\'s habits."), ('진짜 도둑이 하는 순서 그대로 해봐요. → <a href="ttp-ko.html">도둑의 버릇</a>', 'Doing exactly what a real thief does, in order. → <a href="ttp-en.html">a thief\'s habits</a>')),
        ("ATT&CK", "ATT&CK", ("버릇 목록표.", "The habits list."), ('한 줄씩 골라 해보는 백과사전. → <a href="attack-ko.html">도둑 백과사전</a>', 'The encyclopedia you pick lines from. → <a href="attack-en.html">the thief encyclopedia</a>')),
        ("탐지 격차", "Detection gap", ("빨간 줄.", "A red line."), ("도둑이 했는데 종이 안 울린 버릇. 퍼플 팀이 찾는 것.", "A habit the thief did with no bell. What purple teaming finds.")),
        ("탐지 규칙", "Detection rule", ("새 종.", "A new bell."), ('빨간 줄을 초록으로 바꾸는 것. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'What turns a red line green. → <a href="siem-en.html">the guard room screen</a>')),
        ("퍼플 팀 훈련", "Purple team exercise", ("같이 앉는 날.", "The day they sit together."), ('보통 하루나 며칠, 버릇 목록 하나를 끝까지 해봐요. → <a href="hunting-ko.html">종을 기다리지 않는 파수꾼</a>', 'Usually a day or a few, working through one habits list. → <a href="hunting-en.html">the guard who doesn\'t wait for the bell</a>')),
    ],
}
