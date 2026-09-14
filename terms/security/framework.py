from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'

# 다섯 기둥 (이름, 한 줄 풀이)
PILLARS = (("⟦알기|KNOW⟧", "⟦문을 세요|count the doors⟧"), ("⟦막기|BLOCK⟧", "⟦문을 잠가요|lock them⟧"), ("⟦알아채기|NOTICE⟧", "⟦종을 달아요|hang the bell⟧"),
           ("⟦쫓아내기|CHASE OUT⟧", "⟦순서표대로|by the book⟧"), ("⟦되돌리기|RESTORE⟧", "⟦여분 상자로|spare chest⟧"))


def card(x, y, text, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect x="-40" y="-20" width="80" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(0, 5, text, 11, "#142033") + "</g>")


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def chest(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/><rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/></g>')


def cross(x, y, s=1.0):
    return (f'<path d="M{x - 16 * s} {y - 16 * s} l{32 * s} {32 * s} M{x + 16 * s} {y - 16 * s} l{-32 * s} {32 * s}" stroke="var(--panel)" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M{x - 16 * s} {y - 16 * s} l{32 * s} {32 * s} M{x + 16 * s} {y - 16 * s} l{-32 * s} {32 * s}" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')


def pillar(cx, top, bottom, name, sub, w=84):
    return (f'<rect x="{cx - w / 2}" y="{top}" width="{w}" height="{bottom - top}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect x="{cx - w / 2 - 6}" y="{top}" width="{w + 12}" height="10" rx="2" fill="#C9A86A"/><rect x="{cx - w / 2 - 6}" y="{bottom - 10}" width="{w + 12}" height="10" rx="2" fill="#C9A86A"/>'
            + label(cx, (top + bottom) / 2 - 4, name, 13, "#142033", cls="d") + label(cx, (top + bottom) / 2 + 18, sub, 9, "#142033"))


# 1. 할 일은 많은데 목록이 없어요
CARDS = (("⟦종|bell⟧", 330, 70, -6), ("⟦경비견|dog⟧", 410, 115, 5), ("⟦판자|boards⟧", 360, 165, -3), ("⟦여분 상자|spare chest⟧", 455, 60, 4),
         ("⟦망루|watchtower⟧", 500, 150, -5), ("⟦열쇠 꾸러미|key ring⟧", 560, 95, 6), ("⟦도둑 수업|thief lesson⟧", 625, 155, -4), ("⟦일지|log⟧", 680, 80, 3))
P1 = svg(300, sky(300)
         + person(80, 100, s=0.9, face=EYES, **KING) + bubble(40, 20, 240, 34, "⟦우리 성, 빠진 건 없지?|our castle — nothing missing, right?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(210, 110, s=0.85, face=FROWN + SWEAT, **GUARD) + label(240, 232, "⟦음… 아마도요?|um… probably?⟧", 12, "var(--bad)")
         + "".join(card(x, y, t, r) for t, x, y, r in CARDS)
         + label(510, 235, "⟦할 일은 많은데 목록이 없어요|so many jobs — and no list⟧", 12, "var(--muted)")
         + label(380, 282, "⟦뭘 다 했는지, 뭘 빠뜨렸는지 아무도 몰라요|nobody knows what\'s done and what\'s missing⟧", 12, "var(--ink)"))

# 2. 한쪽만 두꺼운 성
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="40" y="60" width="160" height="170" fill="var(--stone)"/>' + battlements(40, 40, 160, 4, "var(--stone)")
         + label(120, 255, "⟦성벽은 아주 두꺼워요|the wall is very thick⟧", 12, "var(--ink)")
         + bell(330, 110, 0.9, ring=False) + cross(330, 120, 1.2) + label(330, 180, "⟦종은 없어요|no bell⟧", 12, "var(--bad)")
         + chest(450, 130, 1.0) + cross(450, 128, 1.2) + label(450, 180, "⟦여분 상자도 없어요|no spare chest⟧", 12, "var(--bad)")
         + person(560, 100, s=0.85, face=MASK, extra=BAG) + person(660, 110, s=0.8, face=SMILE, **GUARD)
         + label(620, 235, "⟦도둑은 벌써 안에 — 아무도 몰라요|the thief is already inside — nobody knows⟧", 11, "var(--bad)")
         + label(380, 282, "⟦막기만 두꺼운 성은 넘어온 도둑을 못 알아채고, 되돌리지도 못해요|a castle thick only on blocking can\'t notice a thief who got over, nor recover⟧", 11, "var(--muted)"))

# 3. 다섯 기둥과 지붕 (hero)
P3 = svg(360, night(360)
         + '<path d="M60 128 L380 40 L700 128 Z" fill="#C9A86A"/><rect x="60" y="120" width="640" height="18" rx="3" fill="#C9A86A"/>'
         + label(380, 108, "⟦다스리기 — 누가, 어떤 규칙으로|GOVERN — who, and by what rules⟧", 12, "#142033", cls="d")
         + "".join(pillar(140 + i * 120, 138, 262, n, s_) for i, (n, s_) in enumerate(PILLARS))
         + '<rect x="50" y="262" width="660" height="16" rx="3" fill="#C9A86A"/>'
         + label(380, 306, "⟦이웃 나라 현자들이 정리한 다섯 기둥과 지붕|five pillars and a roof, laid out by the neighbours\' sages⟧", 13, "#F5E6B8", cls="d")
         + label(380, 338, "⟦기둥 하나라도 빠지면 지붕이 기울어요|drop one pillar and the roof tilts⟧", 12, "#C9D5E6"))

# 4. 기둥마다 점수
SCORES = (2, 5, 1, 2, 3)
NAMES = ("⟦알기|know⟧", "⟦막기|block⟧", "⟦알아채기|notice⟧", "⟦쫓아내기|chase out⟧", "⟦되돌리기|restore⟧")


def bar(i, v):
    cx = 130 + i * 90
    c = "var(--good)" if v >= 4 else ("var(--accent)" if v == 3 else "var(--bad)")
    return (f'<rect x="{cx - 28}" y="{230 - v * 28}" width="56" height="{v * 28}" rx="4" fill="{c}"/>'
            + label(cx, 222 - v * 28, f"⟦{v}점|{v}⟧", 13, "var(--ink)", cls="d") + label(cx, 250, NAMES[i], 11, "var(--ink)"))


P4 = svg(320, sky(320)
         + label(310, 56, "⟦우리 성 기둥 점수표|OUR CASTLE\'S PILLAR SCORES⟧", 13, "var(--ink)", cls="d")
         + '<path d="M80 230 h460" stroke="var(--stone-dark)" stroke-width="2"/>'
         + "".join(bar(i, v) for i, v in enumerate(SCORES))
         + person(580, 90, s=0.8, face=EYES, **KING) + person(660, 100, s=0.8, face=SMILE, **GUARD)
         + bubble(540, 14, 210, 34, "⟦종부터 달아야겠네|the bell comes first, then⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(620, 220, "⟦제일 낮은 기둥부터|start with the lowest pillar⟧", 12, "var(--ink)", cls="d")
         + label(380, 296, "⟦기둥마다 몇 점인지 세면, 무엇부터 할지 보여요|score each pillar, and what to do first becomes clear⟧", 12, "var(--ink)"))


# 5. 현자들의 책은 여러 권
def book(x, y, color, title, sub):
    return (f'<g transform="translate({x},{y})"><rect width="130" height="140" rx="6" fill="{color}"/><rect x="0" y="0" width="14" height="140" rx="4" fill="#142033" opacity="0.25"/>'
            f'<rect x="26" y="26" width="90" height="70" rx="4" fill="#FFF8E7" opacity="0.9"/>' + label(71, 56, title, 12, "#142033", cls="d") + label(71, 78, sub, 10, "#142033") + "</g>")


P5 = svg(320, sky(320)
         + book(60, 60, "#5B8DEF", "⟦다섯 기둥 책|FIVE PILLARS⟧", "⟦기둥별로 재요|score by pillar⟧")
         + book(210, 70, "#3F8F5A", "⟦도장 찍힌 책|THE STAMPED⟧", "⟦검사관이 확인|inspector checks⟧")
         + book(360, 80, "#C9822B", "⟦열여덟 할 일|EIGHTEEN JOBS⟧", "⟦순서대로 해요|do them in order⟧")
         + label(270, 252, "⟦책은 여러 권이에요 — 하나 골라 우리 성을 비춰 봐요|there are several books — pick one and hold it up to our castle⟧", 11, "var(--muted)")
         + person(540, 100, s=0.9, face=SMILE, **KING) + person(630, 110, s=0.85, face=SMILE, **GUARD)
         + bubble(480, 14, 260, 34, "⟦어느 책이든 좋아 — 우리 성에 맞게|any book will do — fit it to our castle⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(600, 235, "⟦점수는 해마다 다시 재요|re-score every year⟧", 11, "var(--muted)")
         + label(380, 302, "⟦기둥이 갖춰지면 왕이 \'안전해?\' 물을 때 숫자로 답해요|with the pillars in place, when the king asks \'safe?\' you answer in numbers⟧", 11, "var(--ink)", cls="d"))

KNOW_I = icon('<rect x="20" y="22" width="20" height="30" rx="2" fill="#8B5E3C"/><circle cx="36" cy="38" r="2" fill="#E9B44C"/><circle cx="44" cy="22" r="11" fill="none" stroke="var(--ink)" stroke-width="4"/><path d="M52 30 l8 8" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>')
BLOCK_I = icon('<path d="M32 8 L54 16 V30 C54 44 44 54 32 58 C20 54 10 44 10 30 V16 Z" fill="var(--good)"/><rect x="24" y="30" width="16" height="13" rx="3" fill="var(--panel)"/><path d="M27 30 v-5 a5 5 0 0 1 10 0 v5" stroke="var(--panel)" stroke-width="3" fill="none"/>')
NOTICE_I = icon('<path d="M20 34 c0 -20 24 -20 24 0 v10 h-24 z" fill="#E9B44C"/><rect x="17" y="44" width="30" height="5" rx="2" fill="#C9822B"/><circle cx="32" cy="53" r="3" fill="#C9822B"/><path d="M12 30 a22 22 0 0 1 -6 -16 M52 30 a22 22 0 0 0 6 -16" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
RESTORE_I = icon('<rect x="14" y="30" width="36" height="22" rx="3" fill="#8B5E3C"/><path d="M14 30 h36 v-3 a18 7 0 0 0 -36 0z" fill="#5A3B22"/><path d="M20 20 a12 12 0 1 1 4 9" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M18 26 l2 -8 l8 3" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "framework", "order": 95,
    "title": ("성 지키기 다섯 기둥", "The Five Pillars of the Castle"),
    "h1": ("<em>보안 프레임워크</em>가 뭐예요?", "What is a <em>Security Framework</em>?"),
    "sub": ("보안 프레임워크(Security Framework, NIST CSF 중심)를 이웃 나라 현자들이 정리한 성 지키기 다섯 기둥과 지붕 이야기로 풀어봤어요.",
            "Security frameworks — NIST CSF at the centre — told as a story about five pillars and a roof for keeping a castle, laid out by the neighbours\' sages."),
    "panels": [
        {"svg": P1, "alt": ("왕이 '빠진 건 없지?' 묻고 경비는 땀을 흘리며 '아마도요?' 함. 종, 경비견, 판자, 여분 상자, 망루, 열쇠 꾸러미, 도둑 수업, 일지라고 적힌 쪽지가 흩어져 있음", "The king asks if anything is missing; the guard sweats and says probably. Cards reading bell, dog, boards, spare chest, watchtower, key ring, thief lesson, log lie scattered"),
         "caption": ("성 지키는 일이 너무 많아요. 뭘 빠뜨렸는지 아무도 몰라요.", "There are so many jobs in keeping a castle. Nobody knows what has been missed."),
         "small": ('<a href="soc-ko.html">경비실</a>, <a href="edr-ko.html">경비견</a>, <a href="patch-ko.html">판자</a>, <a href="backup-ko.html">여분 상자</a>… 다 따로따로 열심히 해요. 그런데 목록이 없어요.',
                   'The <a href="soc-en.html">guard room</a>, the <a href="edr-en.html">dogs</a>, the <a href="patch-en.html">boards</a>, the <a href="backup-en.html">spare chest</a> — everyone works hard, separately. But there is no list.')},
        {"svg": P2, "alt": ("아주 두꺼운 성벽 옆에 X 표시된 종과 X 표시된 여분 상자. 가방을 든 도둑이 벌써 안에 있고 경비는 웃으며 모름", "Next to a very thick wall, a bell and a spare chest both crossed out. A thief with a bag is already inside while the guard smiles, unaware"),
         "caption": ("한쪽만 두꺼운 성이 돼요. 넘어온 도둑을 아무도 못 알아채요.", "The castle ends up thick on one side only. Nobody notices the thief who climbed over."),
         "small": ('<a href="firewall-ko.html">성벽</a>만 높이면 종이 없고, 종만 달면 <a href="backup-ko.html">여분 상자</a>가 없어요. 빠진 자리는 도둑이 제일 먼저 찾아요.',
                   'Raise only the <a href="firewall-en.html">wall</a> and there is no bell; hang only the bell and there is no <a href="backup-en.html">spare chest</a>. The thief finds the empty spot first.')},
        {"svg": P3, "hero": True, "alt": ("밤. 다스리기라고 적힌 지붕 아래 다섯 기둥: 알기(문을 세요), 막기(문을 잠가요), 알아채기(종을 달아요), 쫓아내기(순서표대로), 되돌리기(여분 상자로)", "Night. Under a roof labelled govern, five pillars: know (count the doors), block (lock them), notice (hang the bell), chase out (by the book), restore (from the spare chest)"),
         "caption": ("보안 프레임워크는 현자들이 정리한 성 지키기 다섯 기둥이에요.", "A security framework is the sages\' five pillars for keeping a castle."),
         "small": ("알기, 막기, 알아채기, 쫓아내기, 되돌리기. 그리고 지붕은 다스리기 — 누가 책임지고 어떤 규칙으로 할지예요. 기둥 하나라도 빠지면 지붕이 기울어요.", "Know, block, notice, chase out, restore. And the roof is govern — who is responsible, and by what rules. Drop one pillar and the roof tilts."),
         "tricks": (4, [
             (KNOW_I, ("알기", "Know"), ("성의 문과 틈을 세요", "count the doors and cracks"), "warm"),
             (BLOCK_I, ("막기", "Block"), ("잠그고, 세 번 확인", "lock, and check three times")),
             (NOTICE_I, ("알아채기", "Notice"), ("종과 경비견", "the bell and the dogs")),
             (RESTORE_I, ("쫓아내고 되돌리기", "Chase out, restore"), ("순서표와 여분 상자", "the book and the spare chest"), "calm"),
         ])},
        {"svg": P4, "alt": ("기둥 점수표 막대그래프: 알기 2점, 막기 5점, 알아채기 1점, 쫓아내기 2점, 되돌리기 3점. 왕이 '종부터 달아야겠네' 함", "A bar chart of pillar scores: know 2, block 5, notice 1, chase out 2, restore 3. The king says the bell comes first"),
         "caption": ("기둥마다 우리 성은 몇 점인지 세요. 제일 낮은 기둥부터 세워요.", "Score each pillar for our castle. Start with the lowest one."),
         "small": ('알기는 <a href="asm-ko.html">바깥에서 문 세기</a>와 <a href="vulnmgmt-ko.html">틈 장부</a>, 알아채기는 <a href="siem-ko.html">큰 화면</a>과 <a href="edr-ko.html">경비견</a>, 쫓아내기는 <a href="incident-ko.html">순서표</a>, 되돌리기는 <a href="backup-ko.html">여분 상자</a>예요.',
                   'Know is <a href="asm-en.html">counting doors from outside</a> and the <a href="vulnmgmt-en.html">book of cracks</a>; notice is the <a href="siem-en.html">big screen</a> and the <a href="edr-en.html">dogs</a>; chase out is the <a href="incident-en.html">book of steps</a>; restore is the <a href="backup-en.html">spare chest</a>.')},
        {"svg": P5, "alt": ("세 권의 책: 다섯 기둥 책, 도장 찍힌 책, 열여덟 할 일. 왕이 '어느 책이든 좋아 — 우리 성에 맞게' 하고, 점수는 해마다 다시 잼", "Three books: five pillars, the stamped book, eighteen jobs. The king says any book will do, fit it to our castle; scores are re-taken every year"),
         "caption": ("현자들의 책은 여러 권이에요. 하나 골라 우리 성을 비춰 봐요.", "The sages wrote several books. Pick one and hold it up to our castle."),
         "small": ('도장 찍힌 책은 <a href="compliance-ko.html">검사관</a>이 확인해 줘요. 지붕은 <a href="policy-ko.html">성의 규칙 책</a>, 어느 기둥부터 세울지는 <a href="risk-ko.html">위험 저울</a>이 정해요. 점수가 나아지는지는 <a href="metrics-ko.html">숫자</a>로 봐요.',
                   'The stamped book is checked by an <a href="compliance-en.html">inspector</a>. The roof is the <a href="policy-en.html">castle rule book</a>; the <a href="risk-en.html">risk scale</a> decides which pillar to raise first. Whether scores improve, you see in <a href="metrics-en.html">numbers</a>.')},
    ],
    "summary": (("<b>보안 프레임워크</b> = 현자들이 정리한 성 지키기 <b>다섯 기둥</b>(알기·막기·알아채기·쫓아내기·되돌리기)과 <b>지붕</b>(다스리기). 기둥마다 <b>점수</b>를 매기고 <b>빠진 기둥부터</b> 세워요.",
                 "<b>Security framework</b> = the sages\' <b>five pillars</b> for keeping a castle (know, block, notice, chase out, restore) plus the <b>roof</b> (govern). <b>Score</b> each pillar and raise the <b>missing one first</b>."),
                ("Security Framework. NIST CSF 2.0은 Govern·Identify·Protect·Detect·Respond·Recover 여섯 기능으로 보안 활동을 정리하고, ISO 27001은 인증, CIS Controls는 우선순위 있는 통제 목록을 제공해요. 갭 분석으로 현재 성숙도를 재고, 위험에 따라 통제를 우선순위화해요.",
                 "NIST CSF 2.0 organizes security work into six functions — Govern, Identify, Protect, Detect, Respond, Recover; ISO 27001 adds certification, and CIS Controls a prioritized list of controls. A gap analysis measures current maturity, and risk sets the priority of controls.")),
    "glossary": [
        ("다섯 기둥", "NIST CSF", ("이웃 나라 현자들의 성 지키기 책.", "The neighbours\' sages\' book on keeping a castle."), ("다스리기·알기·막기·알아채기·쫓아내기·되돌리기, 여섯 기능. 2.0에서 다스리기(지붕)가 더해졌어요.", "Govern, identify, protect, detect, respond, recover — six functions. Version 2.0 added govern, the roof.")),
        ("도장 찍힌 책", "ISO 27001", ("검사관이 도장을 찍어 주는 책.", "The book an inspector stamps."), ('규칙대로 하는지 남이 확인해 줘요. → <a href="compliance-ko.html">검사관의 도장</a>', 'Someone else confirms you follow the rules. → <a href="compliance-en.html">the inspector\'s stamp</a>')),
        ("열여덟 가지 할 일", "CIS Controls", ("먼저 할 일 순서표.", "A list of what to do first."), ("뭐부터 할지 정해진 목록이에요. 작은 성도 바로 시작할 수 있어요.", "A ready-ordered list. Even a small castle can start today.")),
        ("통제", "Control", ("기둥을 받치는 벽돌 하나.", "One brick in a pillar."), ("종, 자물쇠, 여분 상자처럼 손에 잡히는 장치 하나하나예요.", "A single tangible thing — a bell, a lock, a spare chest.")),
        ("성숙도", "Maturity", ("기둥 점수.", "A pillar\'s score."), ("0점(없음)부터 5점(늘 하고, 재고, 고치는 중)까지.", "From 0 (nothing) to 5 (always done, measured, improved).")),
        ("갭 분석", "Gap analysis", ("빠진 기둥 찾기.", "Finding the missing pillar."), ("책과 우리 성을 나란히 놓고 빈 자리를 세요.", "Hold the book up to the castle and count the empty spots.")),
        ("다스리기", "Governance", ("지붕.", "The roof."), ('누가 책임지고 어떤 규칙으로 할지. → <a href="policy-ko.html">성의 규칙 책</a>', 'Who is responsible and by what rules. → <a href="policy-en.html">the castle rule book</a>')),
        ("위험", "Risk", ("어느 기둥부터 세울지 정하는 저울.", "The scale that picks which pillar first."), ('점수가 낮아도 도둑이 안 노리는 기둥은 나중에. → <a href="risk-ko.html">위험 저울</a>', 'A low score the thief never targets can wait. → <a href="risk-en.html">the risk scale</a>')),
    ],
}
