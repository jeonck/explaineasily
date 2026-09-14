from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
GUEST = dict(hat=None, shirt="#4A5A72")


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="var(--bad)"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="var(--bad)" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def flame(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M0 -12 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/></g>'


def paper(x, y, s=1.0, rot=0, crossed=False):
    cr = '<path d="M-18 -20 l36 44 M18 -20 l-36 44" stroke="var(--bad)" stroke-width="3"/>' if crossed else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -8 h28 M-18 1 h18 M-18 10 h28" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{cr}</g>')


def plan(x, y, w, h, title, rows):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="30" rx="8" fill="#C9A86A"/>' + label(w / 2, 20, title, 13, "#142033", cls="d"))
    for i, (c, r) in enumerate(rows):
        out += f'<circle cx="24" cy="{62 + i * 44}" r="10" fill="{c}"/>' + label(24, 66 + i * 44, str(i + 1), 12, "#FFF", cls="d") + label(44, 67 + i * 44, r, 12, "#142033", "start")
    return out + "</g>"


def calendar(x, y, s=1.0, text="", color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="-26" y="-22" width="52" height="12" rx="4" fill="{color}"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/>{label(0, 12, text, 12, "#142033", cls="d")}</g>')


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="28" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
            f'<path d="M0 -18 V0 L12 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def sun(x, y, s=1.0):
    rays = "".join(f'<path d="M0 -30 v-10" stroke="#E9B44C" stroke-width="4" stroke-linecap="round" transform="rotate({a})"/>' for a in range(0, 360, 45))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="22" fill="#E9B44C"/>{rays}</g>'


WATER = '<path d="M0 292 q40 -14 80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t80 0 H760 V320 H0z" fill="#5B9BD5" opacity="0.6"/>'

# 1. 홍수, 불, 도둑 — 어느 날 성이 멈춰요
P1 = svg(320, sky(320) + castle(40, 80, 0.7) + flame(100, 92, 1.3) + flame(330, 92, 1.1) + flame(200, 150, 0.9)
         + WATER + chest(450, 200, 1.0, lock=True) + label(450, 240, "⟦도둑의 자물쇠|the thief\'s lock⟧", 10, "var(--bad)")
         + person(560, 100, s=0.85, face=FROWN + SWEAT, **KING) + bubble(430, 30, 300, 34, "⟦내일 장사는요?|what about tomorrow\'s market?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(660, 130, s=0.55, face=FROWN, **GUEST) + person(705, 140, s=0.5, face=FROWN, **GUEST) + label(690, 220, "⟦손님들이 기다려요|guests are waiting⟧", 10, "var(--muted)")
         + label(380, 262, "⟦홍수, 불, 도둑 — 어느 날 성이 멈춰요|flood, fire, thief — one day the castle stops⟧", 12, "var(--ink)", cls="d"))

# 2. 여분 상자만으론 부족해요
P2 = svg(300, sky(300)
         + chest(120, 170, 1.3) + label(120, 230, "⟦여분 상자는 있어요|the spare chest is there⟧", 11, "var(--good)")
         + person(260, 100, s=0.7, face=FROWN, **GUARD) + bubble(215, 30, 150, 34, "⟦어디서 열지?|open it where?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(400, 100, s=0.7, face=FROWN, **CLERK) + bubble(375, 30, 150, 34, "⟦누가 뭘 하지?|who does what?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(540, 100, s=0.7, face=FROWN, **GUARD) + bubble(530, 30, 170, 34, "⟦얼마나 걸리지?|how long will it take?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(660, 110, s=0.75, face=FROWN + SWEAT, **KING)
         + label(450, 220, "⟦상자는 있는데 순서표가 없어요|there\'s a chest, but no plan⟧", 13, "var(--ink)", cls="d")
         + label(380, 275, "⟦여분 상자는 시작이지 끝이 아니에요|the spare chest is the start, not the end⟧", 12, "var(--muted)"))

# 3. 다음 날 장사 순서표 (hero)
ROWS = (("var(--accent)", "⟦어디서 — 이웃 마을 창고|WHERE — the hall in the next village⟧"),
        ("#5B8DEF", "⟦누가 — 경비장은 문, 서기는 장부|WHO — captain: doors, clerk: ledgers⟧"),
        ("var(--bad)", "⟦얼마나 빨리 — 아침까지|HOW FAST — by morning⟧"),
        ("var(--good)", "⟦얼마나 잃어도 — 하루치까지|HOW MUCH LOST — a day\'s worth at most⟧"))
P3 = svg(360, sky(360)
         + plan(40, 40, 400, 220, "⟦성이 멈추면|IF THE CASTLE STOPS⟧", ROWS)
         + sun(710, 60, 0.9) + small_castle(520, 60, 0.9) + label(592, 220, "⟦이웃 마을 창고 — 대체 성|the spare hall — our other castle⟧", 11, "var(--muted)")
         + person(560, 250, s=0.6, face=SMILE, **CLERK) + chest(635, 292, 0.7)
         + label(240, 300, "⟦순서표를 미리 써 둬요|write the plan before the day⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦성이 불타도 다음 날 아침엔 장사해요|even if the castle burns, tomorrow morning the market opens⟧", 12, "var(--muted)"))

# 4. 얼마나 빨리 / 얼마나 잃어도
P4 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + flame(80, 130, 1.2) + '<path d="M120 120 H296" stroke="var(--ink)" stroke-width="3"/><path d="M300 120 l-10 -7 v14z" fill="var(--ink)"/>'
         + clock(200, 170, 1.0) + sun(335, 120, 0.8) + label(335, 165, "⟦아침|morning⟧", 10, "var(--muted)")
         + label(190, 240, "⟦얼마나 빨리 다시 열까|how fast we reopen⟧", 13, "var(--ink)", cls="d") + label(190, 262, "⟦아침까지 — 그 시간 안에|by morning — within that time⟧", 11, "var(--accent)")
         + chest(470, 150, 1.0) + label(470, 195, "⟦어젯밤 사본|last night\'s copy⟧", 11, "var(--ink)")
         + paper(590, 140, 0.9, rot=-6, crossed=True) + paper(625, 150, 0.9, rot=8, crossed=True) + label(610, 195, "⟦오늘 아침 종이는 없어요|this morning\'s pages are gone⟧", 10, "var(--bad)")
         + label(570, 240, "⟦얼마나 잃어도 될까|how much we can lose⟧", 13, "var(--ink)", cls="d") + label(570, 262, "⟦하루치 — 그만큼만|a day\'s worth — no more⟧", 11, "var(--good)")
         + label(380, 300, "⟦둘 다 왕이 정해요 — 더 빨리, 더 적게는 더 비싸요|the king sets both — faster and less both cost more⟧", 11, "var(--muted)"))

# 5. 연습해요 — 그리고 다음 날 아침, 장사해요
P5 = svg(320, sky(320)
         + calendar(70, 100, 1.0, "⟦봄|spring⟧") + flame(150, 130, 1.0) + label(150, 165, "⟦가짜 불|pretend fire⟧", 10, "var(--muted)")
         + person(200, 100, s=0.65, face=SMILE, **GUARD) + person(260, 110, s=0.65, face=SMILE, **GUARD) + person(320, 105, s=0.65, face=SMILE, **CLERK) + chest(385, 165, 0.6)
         + label(240, 220, "⟦순서표대로 뛰어 봐요|run through the plan⟧", 12, "var(--ink)", cls="d")
         + sun(720, 50, 0.8) + small_castle(520, 90, 0.7) + person(650, 120, s=0.5, face=SMILE, **GUEST) + person(700, 130, s=0.5, face=SMILE, **GUEST)
         + label(620, 220, "⟦다음 날 아침, 장사해요|next morning, open for business⟧", 12, "var(--ink)", cls="d")
         + label(380, 270, "⟦연습 안 한 순서표는 불 앞에서 못 읽어요|a plan never rehearsed can\'t be read in front of a fire⟧", 11, "var(--muted)")
         + label(380, 300, "⟦순서표 + 여분 상자 + 연습 = 다음 날 장사|plan + spare chest + practice = tomorrow\'s market⟧", 12, "var(--ink)", cls="d"))

WHERE_I = icon('<rect x="10" y="26" width="30" height="26" fill="var(--stone-dark)"/><rect x="10" y="20" width="6" height="8" fill="var(--stone-dark)"/><rect x="22" y="20" width="6" height="8" fill="var(--stone-dark)"/><rect x="34" y="20" width="6" height="8" fill="var(--stone-dark)"/><path d="M20 52 V42 a5 5 0 0 1 10 0 V52z" fill="var(--night)"/><path d="M44 36 h12" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><path d="M52 30 l6 6 l-6 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
WHO_I = icon('<circle cx="22" cy="24" r="9" fill="#E8C9A8"/><path d="M12 22 q10 -12 20 0z" fill="var(--good)"/><rect x="12" y="34" width="20" height="18" rx="5" fill="var(--good)"/><circle cx="44" cy="24" r="9" fill="#E8C9A8"/><path d="M34 22 q10 -12 20 0z" fill="var(--stone-dark)"/><rect x="34" y="34" width="20" height="18" rx="5" fill="#4A5A72"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="20" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M32 18 V32 L41 38" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="52" cy="14" r="6" fill="#E9B44C"/>')
DRILL_I = icon('<path d="M22 12 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)" opacity="0.5"/><circle cx="46" cy="44" r="11" fill="var(--good)"/><path d="M40 44 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "drp", "order": 76,
    "title": ("성이 불타도 다음 날 장사하는 법", "How to Open the Market the Morning After the Fire"),
    "h1": ("<em>재해 복구</em>가 뭐예요?", "What is <em>Disaster Recovery</em>?"),
    "sub": ("재해 복구(DR)와 업무 연속성(BCP)을 성이 불타거나 물에 잠기거나 도둑에게 잠겨 버려도 다음 날 아침 장사를 여는 순서표 이야기로 풀어봤어요.",
            "Disaster recovery and business continuity, told as a story about the plan that opens the market the morning after the castle burns, floods, or gets locked up."),
    "panels": [
        {"svg": P1, "alt": ("불타는 성, 아래로 차오르는 물, 도둑의 자물쇠가 채워진 상자. 왕이 땀을 흘리며 '내일 장사는요?', 손님 둘이 기다림", "A burning castle, water rising below, a chest with the thief\'s lock on it. The king sweats — what about tomorrow\'s market? — while two guests wait"),
         "caption": ("홍수, 불, 도둑. 어느 날 성이 멈춰요.", "Flood, fire, thief. One day the castle stops."),
         "small": ('불이 나기도 하고, 물이 차기도 하고, <a href="ransomware-ko.html">도둑이 상자마다 자물쇠</a>를 채우기도 해요. 그런데 손님들은 내일도 와요.',
                   'Sometimes it\'s fire, sometimes water, sometimes a <a href="ransomware-en.html">thief\'s lock on every chest</a>. And the guests still come tomorrow.')},
        {"svg": P2, "alt": ("여분 상자 하나 옆에서 경비와 서기가 각각 '어디서 열지?', '누가 뭘 하지?', '얼마나 걸리지?' 하고 묻고, 왕이 땀을 흘림", "Beside one spare chest, guards and a clerk ask open it where? who does what? how long will it take? The king sweats"),
         "caption": ("여분 상자는 있어요. 그런데 어디서, 누가, 얼마나 빨리요?", "The spare chest is there. But where, who, and how fast?"),
         "small": ('<a href="backup-ko.html">멀리 둔 여분 상자</a>는 시작이지 끝이 아니에요. 상자를 열 곳도, 열 사람도, 걸리는 시간도 아무도 몰라요.',
                   'The <a href="backup-en.html">spare chest far away</a> is the start, not the end. Nobody knows where to open it, who opens it, or how long it takes.')},
        {"svg": P3, "hero": True, "alt": ("'성이 멈추면' 순서표: 1 어디서 — 이웃 마을 창고, 2 누가 — 경비장은 문, 서기는 장부, 3 얼마나 빨리 — 아침까지, 4 얼마나 잃어도 — 하루치까지. 옆에 해가 뜨는 이웃 마을 창고로 서기가 상자를 옮김", "A plan titled IF THE CASTLE STOPS: 1 where — the hall in the next village, 2 who — captain the doors, clerk the ledgers, 3 how fast — by morning, 4 how much lost — a day\'s worth at most. Beside it, a clerk carries a chest to the spare hall as the sun rises"),
         "caption": ("재해 복구는 '성이 멈추면 어디서, 누가, 얼마나 빨리 다시 여는지' 미리 써 둔 순서표예요.", "Disaster recovery is the plan, written in advance, for where, who, and how fast we reopen when the castle stops."),
         "small": ("어디서 다시 열지(대체 성), 누가 뭘 하는지, 얼마나 빨리 열어야 하는지, 얼마나 잃어도 되는지. 넷을 미리 정해요.", "Where to reopen (the other castle), who does what, how fast it must open, and how much we can afford to lose. Four things, decided ahead."),
         "tricks": (4, [
             (WHERE_I, ("어디서 — 대체 성", "Where — the other castle"), ("이웃 마을 창고", "the hall next village")),
             (WHO_I, ("누가 뭘", "Who does what"), ("경비장은 문, 서기는 장부", "captain: doors, clerk: ledgers")),
             (CLOCK_I, ("얼마나 빨리, 얼마나 잃어도", "How fast, how much lost"), ("아침까지, 하루치까지", "by morning, a day at most"), "warm"),
             (DRILL_I, ("연습", "Practice"), ("봄마다 가짜 불로", "a pretend fire every spring"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 불에서 아침 해까지 화살표와 시계 — 얼마나 빨리. 오른쪽: 어젯밤 사본 상자와 X 표시된 오늘 아침 종이 — 얼마나 잃어도", "Left: an arrow from fire to morning sun with a clock — how fast. Right: last night\'s copy chest and this morning\'s pages crossed out — how much lost"),
         "caption": ("'얼마나 빨리'와 '얼마나 잃어도'는 다른 숫자예요.", "How fast and how much lost are two different numbers."),
         "small": ("아침까지 다시 열기로 했으면 그 시간 안에 열어야 해요. 어젯밤 사본까지만 있으면 오늘 아침 종이는 잃어요 — 그게 하루치예요. 더 빨리, 더 적게는 더 비싸요. 왕이 정해요.", "If we said by morning, it has to open by morning. With only last night\'s copy, this morning\'s pages are lost — that\'s a day\'s worth. Faster and less both cost more. The king decides.")},
        {"svg": P5, "alt": ("봄 달력과 가짜 불 앞에서 경비 둘과 서기가 상자를 들고 순서표대로 뛰어 봄. 오른쪽엔 해가 뜬 이웃 마을 창고에 웃는 손님 둘", "By a spring calendar and a pretend fire, two guards and a clerk run through the plan with a chest. On the right, the sun is up over the spare hall and two guests smile"),
         "caption": ("봄마다 가짜 불로 연습해요. 그래야 다음 날 아침 장사해요.", "Every spring, a pretend fire to practice. That\'s how the market opens the next morning."),
         "small": ('연습 안 한 순서표는 불 앞에서 못 읽어요. 도둑이 든 날의 <a href="incident-ko.html">순서표</a>와 짝이에요 — 그쪽은 도둑을 내보내고, 이쪽은 장사를 다시 열어요.',
                   'A plan never rehearsed can\'t be read in front of a fire. It pairs with the <a href="incident-en.html">order of things when a thief gets in</a> — that one gets the thief out; this one gets the market open.')},
    ],
    "summary": (("<b>재해 복구</b> = 성이 멈추면 <b>어디서, 누가, 얼마나 빨리</b> 다시 열고 <b>얼마나 잃어도 되는지</b> 미리 써 두고 <b>연습하는</b> 순서표. 여분 상자만으론 부족해요.",
                 "<b>Disaster recovery</b> = the rehearsed plan for <b>where, who, and how fast</b> we reopen when the castle stops, and <b>how much we can lose</b>. A spare chest alone isn\'t enough."),
                ("Disaster Recovery / Business Continuity. 재해 뒤 시스템을 되살리는 계획(DR)과 그동안 업무를 이어가는 계획(BCP)이에요. 목표 복구 시간(RTO)과 허용 데이터 손실(RPO)을 정하고, 대체 사이트와 역할을 준비하고, 정기 훈련으로 검증해요.",
                 "DR is the plan to bring systems back after a disaster; BCP is the plan to keep the business running meanwhile. Set the recovery time objective (RTO) and recovery point objective (RPO), prepare an alternate site and roles, and prove it with regular drills.")),
    "glossary": [
        ("업무 연속성 계획", "BCP (Business Continuity Plan)", ("다음 날 장사하는 법.", "How the market opens tomorrow."), ("성이 멈춰도 손님을 받는 방법 전체. 상자만이 아니라 사람, 장소, 순서까지요.", "Everything that keeps serving guests when the castle stops — not just chests, but people, places, and order.")),
        ("재해 복구", "DR (Disaster Recovery)", ("성을 다시 세우는 순서표.", "The plan that rebuilds the castle."), ("여분 상자를 꺼내 어디서 어떻게 다시 여는지. 업무 연속성 계획의 한 부분이에요.", "Taking out the spare chest and reopening, where and how. One part of the continuity plan.")),
        ("목표 복구 시간", "RTO (Recovery Time Objective)", ("얼마나 빨리.", "How fast."), ("'아침까지.' 멈춘 뒤 다시 열 때까지 허락된 시간이에요.", "By morning. The time allowed between stopping and reopening.")),
        ("목표 복구 시점", "RPO (Recovery Point Objective)", ("얼마나 잃어도.", "How much lost."), ('\'하루치까지.\' 마지막 사본 이후 잃어도 되는 양. 사본을 자주 만들수록 줄어요. → <a href="backup-ko.html">여분 상자</a>', 'A day\'s worth at most. What may be lost since the last copy. More frequent copies make it smaller. → <a href="backup-en.html">the spare chest</a>')),
        ("대체 사이트", "Alternate site (hot / warm / cold)", ("이웃 마을 창고.", "The hall next village."), ("불 켜고 상자까지 갖춘 창고(핫), 건물만 있고 상자는 옮겨야 하는 창고(웜), 빈 땅(콜드). 빠를수록 비싸요.", "A hall lit and stocked (hot), a building where chests must be carried in (warm), an empty lot (cold). Faster costs more.")),
        ("복구 훈련", "DR drill / tabletop exercise", ("봄마다 가짜 불.", "A pretend fire every spring."), ("순서표대로 정말 뛰어 봐요. 책상에 앉아 말로만 해 보는 것도 있어요.", "Actually run the plan. Sometimes it\'s done at a table, in words only.")),
        ("백업", "Backup", ("여분 상자.", "The spare chest."), ('순서표의 시작. 상자가 없으면 열 것도 없어요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'Where the plan starts. No chest, nothing to open. → <a href="backup-en.html">the spare chest far away</a>')),
        ("사고 대응", "Incident response", ("도둑 들었을 때 순서표.", "The plan for when a thief gets in."), ('그쪽은 도둑을 내보내고, 이쪽은 장사를 다시 열어요. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'That one gets the thief out; this one gets the market open. → <a href="incident-en.html">the order of things when a thief gets in</a>')),
    ],
}
