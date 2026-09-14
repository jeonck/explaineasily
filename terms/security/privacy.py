from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
VISITOR = dict(hat=None, shirt="#7B3FA0")
MERCHANT = dict(hat="var(--accent)", shirt="#4A5A72")
INSPECTOR = dict(hat="var(--stone-dark)", shirt="#2E3D57")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
CLIP = '<rect x="50" y="66" width="30" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'


def board(x, y, w, h, title, rows, size=12):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, size, "#142033", "start")
    return out + "</g>"


def paper(x, y, s=1.0, stamp=None, rot=0, text=None, lines=3):
    st = f'<circle cx="18" cy="-14" r="9" fill="{stamp}"/>' if stamp else ""
    ln = "".join(f'<path d="M-18 {-8 + i * 9} h{28 - (i % 2) * 10}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for i in range(lines))
    tx = label(0, 24, text, 9, "#142033") if text else ""
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{ln}{st}{tx}</g>'


def nametag(x, y, text, s=1.0, color="#142033"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" y="-14" width="72" height="28" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="-26" cy="-14" r="3" fill="#C9A86A"/><circle cx="26" cy="-14" r="3" fill="#C9A86A"/>'
            + label(0, 5, text, 12, color, cls="d") + "</g>")


def chest(x, y, s=1.0, color="#8B5E3C", lock=True):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def flame(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M0 -12 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/></g>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def check(x, y, s=1.0):
    return f'<circle cx="{x}" cy="{y}" r="{14 * s}" fill="var(--good)"/><path d="M{x - 7 * s} {y} l{5 * s} {5 * s} l{10 * s} -{11 * s}" stroke="#FFF" stroke-width="{3.5 * s}" fill="none" stroke-linecap="round"/>'


def arrow(x, y, l=40):
    return (f'<path d="M{x} {y} h{l}" stroke="var(--muted)" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M{x + l - 10} {y - 10} l10 10 l-10 10" stroke="var(--muted)" stroke-width="4" fill="none" stroke-linecap="round"/>')


# 1. 성 명부엔 손님의 이름, 집, 생일이 적혀요
P1 = svg(320, sky(320)
         + person(60, 110, s=0.85, face=SMILE, **VISITOR) + bubble(20, 30, 230, 34, "⟦제 이름이랑 집이랑 생일이에요|my name, my home, my birthday⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(200, 120, s=0.8, face=EYES, **CLERK)
         + board(300, 40, 300, 150, "⟦성 명부|CASTLE ROSTER⟧", ("⟦이름: 민수|name: Minsu⟧", "⟦집: 강 건너 셋째 집|home: 3rd house past the river⟧", "⟦생일: 봄 첫날|birthday: first day of spring⟧", "⟦좋아하는 빵: 호밀빵|favorite bread: rye⟧"))
         + chest(680, 150, 1.0) + label(680, 200, "⟦잠깐 맡아 둬요|kept for a while⟧", 10, "var(--muted)")
         + label(92, 240, "⟦손님|a visitor⟧", 11, "var(--muted)") + label(230, 240, "⟦서기|the clerk⟧", 11, "var(--muted)")
         + label(450, 218, "⟦명부에 적힌 건 손님의 것이에요|what\'s written belongs to the visitor⟧", 11, "var(--ink)", cls="d")
         + label(380, 300, "⟦성은 잠깐 맡아 둘 뿐, 주인은 손님이에요|the castle only keeps it for a while — the visitor is the owner⟧", 12, "var(--ink)"))

# 2. 손님 것을 성 것처럼 다루면
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + paper(80, 120, 1.5, lines=5) + person(150, 90, s=0.7, face=FROWN + SWEAT, **CLERK)
         + label(130, 225, "⟦뭐든 다 적어요|writes down everything⟧", 12, "var(--ink)", cls="d") + label(130, 247, "⟦물어본 적도 없어요|never even asked⟧", 11, "var(--bad)")
         + person(320, 90, s=0.7, face=EYES, **CLERK) + paper(385, 130, 0.8, rot=10, text="⟦민수네 집|Minsu\'s home⟧") + person(410, 90, s=0.7, face=SMILE, **MERCHANT)
         + label(380, 225, "⟦아무한테나 줘요|hands it to anyone⟧", 12, "var(--ink)", cls="d") + label(380, 247, "⟦손님은 몰라요|the visitor has no idea⟧", 11, "var(--bad)")
         + person(570, 90, s=0.7, face=MASK, extra=BAG) + paper(640, 130, 0.8, rot=-8, text="⟦생일·집|birthday·home⟧") + person(680, 100, s=0.6, face=SMILE, **VISITOR)
         + label(630, 225, "⟦도둑맞았는데|it got stolen⟧", 12, "var(--ink)", cls="d") + label(630, 247, "⟦손님에게 말도 안 해요|and nobody tells the visitor⟧", 11, "var(--bad)")
         + label(380, 285, "⟦손님 것을 성 것처럼 다뤄서 그래요|because the castle treats the visitor\'s things as its own⟧", 12, "var(--muted)"))

# 3. 손님 이름표는 손님 것 (hero)
P3 = svg(360, sky(360)
         + person(60, 130, s=0.85, face=SMILE, **VISITOR) + person(180, 130, s=0.85, face=SMILE, **CLERK)
         + bubble(140, 40, 270, 34, "⟦빵 배달하려고 이름만 적을게요|just your name, for the bread delivery⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + '<rect x="265" y="120" width="130" height="100" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(330, 150, "⟦이름: 민수|name: Minsu⟧", 12, "#142033") + label(330, 176, "⟦빵: 호밀빵|bread: rye⟧", 12, "#142033") + label(330, 204, "⟦(그게 다예요)|(that\'s all)⟧", 10, "#142033")
         + board(430, 50, 290, 170, "⟦명부 약속|ROSTER PROMISES⟧", ("⟦1. 꼭 필요한 것만 적어요|1. write only what\'s needed⟧", "⟦2. 왜 적는지 먼저 말해요|2. say why, before writing⟧", "⟦3. 지워 달라면 지워요|3. erase it when asked⟧", "⟦4. 잃어버리면 바로 알려요|4. if it\'s lost, tell them at once⟧"))
         + label(92, 262, "⟦손님|visitor⟧", 11, "var(--muted)") + label(212, 262, "⟦서기|clerk⟧", 11, "var(--muted)") + label(330, 246, "⟦필요한 두 줄만|just the two lines needed⟧", 10, "var(--muted)")
         + label(380, 308, "⟦손님 이름표는 손님 것 — 성은 잠깐 빌려 쓰는 거예요|the visitor\'s name tag belongs to the visitor — the castle only borrows it⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦적기 전에 묻고, 적은 건 아끼고, 달라면 돌려줘요|ask before you write, guard what you wrote, give it back when asked⟧", 12, "var(--muted)"))

# 4. 약속이 지켜지는 모습 넷
P4 = svg(320, sky(320)
         + person(50, 80, s=0.6, face=SMILE, **VISITOR) + person(110, 80, s=0.6, face=SMILE, **CLERK) + check(105, 70, 0.9) + bubble(30, 30, 140, 28, "⟦적어도 돼요?|may I write it?⟧", 10, "var(--panel)", "var(--line)", "right")
         + label(100, 236, "⟦먼저 물어요|ask first⟧", 12, "var(--ink)", cls="d") + label(100, 256, "⟦왜 적는지도 말해요|and say why⟧", 10, "var(--muted)")
         + nametag(240, 120, "⟦민수|Minsu⟧", 0.9) + arrow(280, 120, 34) + nametag(360, 120, "⟦17번|No. 17⟧", 0.9, "var(--accent)") + person(350, 150, s=0.5, face=SMILE, **MERCHANT)
         + label(300, 236, "⟦남에게 줄 땐 번호표로|to others, a number instead⟧", 12, "var(--ink)", cls="d") + label(300, 256, "⟦이름은 성 안에만|the name stays in the castle⟧", 10, "var(--muted)")
         + person(440, 80, s=0.6, face=SMILE, **VISITOR) + bubble(430, 30, 120, 28, "⟦지워 주세요|erase it, please⟧", 10, "var(--panel)", "var(--line)", "bottom") + paper(520, 160, 0.9, text="⟦민수|Minsu⟧") + flame(520, 150, 0.9)
         + label(500, 236, "⟦지워 달라면 지워요|erase when asked⟧", 12, "var(--ink)", cls="d") + label(500, 256, "⟦여분 상자 것까지|the spare chest copy too⟧", 10, "var(--muted)")
         + bell(650, 80, 0.7) + paper(690, 160, 0.9, stamp="var(--bad)", text="⟦민수에게|to Minsu⟧") + person(620, 130, s=0.6, face=FROWN, **CLERK)
         + label(670, 236, "⟦잃어버리면 바로 알려요|lost? tell them at once⟧", 12, "var(--ink)", cls="d") + label(670, 256, "⟦숨기지 않아요|never hide it⟧", 10, "var(--muted)")
         + label(380, 300, "⟦네 가지 약속은 손님이 성에 있는 내내 지켜져요|the four promises hold the whole time the visitor is with the castle⟧", 12, "var(--ink)", cls="d"))

# 5. 검사관이 와요
P5 = svg(300, sky(300)
         + person(60, 100, s=0.85, face=EYES, extra=CLIP, **INSPECTOR) + label(92, 220, "⟦검사관|the inspector⟧", 11, "var(--muted)")
         + bubble(140, 30, 290, 34, "⟦왜 적었고, 손님이 알고 있나요?|why was it written, and does the visitor know?⟧", 10, "var(--panel)", "var(--line)", "left")
         + person(300, 110, s=0.8, face=SMILE, **CLERK) + board(370, 100, 150, 74, "⟦명부 약속|PROMISES⟧", ("⟦적기 전에 물었어요 ✓|asked first ✓⟧",), 11) + label(400, 220, "⟦여기 있어요|here it is⟧", 11, "var(--good)", cls="d")
         + paper(580, 140, 1.0, stamp="var(--bad)", text="⟦이름표|name tag⟧") + person(650, 110, s=0.8, face=SMILE, **VISITOR)
         + label(630, 220, "⟦빨간 도장, 태우는 날까지|red stamp, until burning day⟧", 10, "var(--muted)")
         + label(380, 268, "⟦손님 것을 손님 것답게 — 그러면 검사관도, 손님도 웃어요|treat the visitor\'s as the visitor\'s — and the inspector smiles, and so does the visitor⟧", 12, "var(--ink)", cls="d"))

MIN_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M20 42 h24 M20 50 h24" stroke="#C9A86A" stroke-width="2" stroke-dasharray="3 3"/>')
ASK_I = icon('<rect x="8" y="12" width="40" height="28" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><path d="M18 40 l-4 10 l14 -10" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><text x="28" y="33" text-anchor="middle" font-size="18" font-weight="700" fill="var(--ink)">?</text><circle cx="52" cy="46" r="9" fill="var(--good)"/><path d="M48 46 l3 3 l6 -7" stroke="#FFF" stroke-width="2.5" fill="none"/>')
ERASE_I = icon('<rect x="10" y="12" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M17 24 h16 M17 32 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M48 10 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M48 28 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/>')
TELL_I = icon('<path d="M20 30 c0 -20 24 -20 24 0 v12 h-24z" fill="#E9B44C"/><rect x="17" y="42" width="30" height="4" rx="2" fill="#C9822B"/><circle cx="32" cy="50" r="3" fill="#C9822B"/><path d="M14 26 a22 22 0 0 1 -6 -16 M50 26 a22 22 0 0 0 6 -16" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "privacy", "order": 92,
    "title": ("손님 이름표는 손님 것", "The Visitor\'s Name Tag Belongs to the Visitor"),
    "h1": ("<em>개인정보 보호</em>가 뭐예요?", "What is <em>Privacy</em>?"),
    "sub": ("개인정보 보호(Privacy / Personal Data Protection)를 성 명부에 적힌 손님의 이름·집·생일을 손님의 것으로 다루는 이야기로 풀어봤어요.",
            "Privacy and personal data protection, told as a story about treating the visitor\'s name, home, and birthday in the castle roster as the visitor\'s own."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '제 이름이랑 집이랑 생일이에요' 하고, 서기가 성 명부에 이름·집·생일·좋아하는 빵을 적음. 옆에 자물쇠 달린 상자 — 잠깐 맡아 둬요", "A visitor says: my name, my home, my birthday. The clerk writes name, home, birthday, and favorite bread into the castle roster. A locked chest beside it — kept for a while"),
         "caption": ("성 명부엔 손님의 이름, 집, 생일이 적혀요.", "The castle roster holds the visitor\'s name, home, and birthday."),
         "small": ("빵을 배달하려면 이름과 집을 알아야 하니까요. 그런데 그건 손님의 것이에요. 성은 잠깐 맡아 둘 뿐이에요.", "To deliver bread, the castle needs a name and a home. But those belong to the visitor. The castle only keeps them for a while.")},
        {"svg": P2, "alt": ("셋: 서기가 땀 흘리며 여섯 줄짜리 긴 종이에 뭐든 다 적음. 서기가 상인에게 '민수네 집' 종이를 건넴. 도둑이 '생일·집' 종이를 들고 가는데 손님은 웃으며 모름", "Three scenes: a sweating clerk writes everything on a long six-line paper. The clerk hands a paper reading Minsu\'s home to a merchant. A thief walks off with a birthday-and-home paper while the visitor smiles, unaware"),
         "caption": ("손님 것을 성 것처럼 다루면 곤란해져요.", "Trouble starts when the castle treats the visitor\'s things as its own."),
         "small": ('물어보지도 않고 뭐든 다 적고, 아무한테나 주고, <a href="ransomware-ko.html">도둑맞아도</a> 손님에게 말하지 않아요. 손님은 자기 이름표가 어디로 갔는지 몰라요.',
                   'It writes everything without asking, hands it to anyone, and when <a href="ransomware-en.html">a thief takes it</a>, tells the visitor nothing. The visitor has no idea where their name tag went.')},
        {"svg": P3, "hero": True, "alt": ("서기가 '빵 배달하려고 이름만 적을게요'. 짧은 명부엔 이름과 빵, 두 줄뿐. 오른쪽 판자에 명부 약속 넷: 꼭 필요한 것만 적어요, 왜 적는지 먼저 말해요, 지워 달라면 지워요, 잃어버리면 바로 알려요", "The clerk says: just your name, for the bread delivery. The short roster has two lines — name and bread. A board on the right lists four roster promises: write only what\'s needed, say why before writing, erase it when asked, if it\'s lost tell them at once"),
         "caption": ("개인정보 보호는 손님 이름표를 손님 것으로 다루는 약속이에요.", "Privacy is the promise to treat the visitor\'s name tag as the visitor\'s own."),
         "small": ("성은 잠깐 빌려 쓰는 거예요. 그러니 적기 전에 묻고, 꼭 필요한 것만 적고, 적은 건 아끼고, 달라면 돌려줘요.", "The castle only borrows it. So ask before you write, write only what\'s needed, guard what you wrote, and give it back when asked."),
         "tricks": (4, [
             (MIN_I, ("꼭 필요한 것만", "Only what\'s needed"), ("빵 배달엔 이름과 집이면 돼요", "bread needs a name and a home"), "calm"),
             (ASK_I, ("먼저 묻기", "Ask first"), ("왜 적는지도 말해요", "and say what it\'s for")),
             (ERASE_I, ("달라면 지우기", "Erase when asked"), ("여분 상자 것까지", "the spare chest copy too")),
             (TELL_I, ("잃으면 알리기", "Tell them if it\'s lost"), ("숨기면 더 나빠져요", "hiding makes it worse"), "warm"),
         ])},
        {"svg": P4, "alt": ("넷: 서기가 '적어도 돼요?' 묻고 초록 체크. '민수' 이름표가 화살표 뒤 '17번' 이름표로 바뀌어 상인에게 감. 손님이 '지워 주세요' 하자 민수 종이가 불에 탐. 종이 울리고 서기가 빨간 도장 편지를 민수에게 보냄", "Four scenes: the clerk asks may I write it, with a green check. A Minsu name tag becomes a No. 17 tag past an arrow, headed to the merchant. The visitor says erase it, and the Minsu paper burns. A bell rings and the clerk sends a red-stamped letter to Minsu"),
         "caption": ("약속이 지켜지는 모습이에요.", "This is what keeping the promises looks like."),
         "small": ('남에게 줄 땐 이름 대신 번호표를 써요. 지울 땐 <a href="backup-ko.html">여분 상자</a>의 사본까지 같이 지워요. 잃어버리면 <a href="incident-ko.html">순서표</a>대로 손님에게 바로 알려요.',
                   'To others, a number goes out instead of the name. Erasing includes the copy in the <a href="backup-en.html">spare chest</a>. If it\'s lost, the <a href="incident-en.html">playbook</a> says: tell the visitor at once.')},
        {"svg": P5, "alt": ("검사관이 '왜 적었고, 손님이 알고 있나요?' 하고 묻고, 서기가 웃으며 명부 약속 판자를 보여줌. 손님 옆엔 빨간 도장 찍힌 이름표 종이", "An inspector asks why it was written and whether the visitor knows; the clerk smiles and shows the promises board. Beside the visitor is a red-stamped name-tag paper"),
         "caption": ("검사관이 와서 물어요. 왜 적었고, 손님이 알고 있나요?", "The inspector comes and asks: why was it written, and does the visitor know?"),
         "small": ('손님 이름표엔 <a href="classification-ko.html">빨간 도장</a>을 찍고, <a href="retention-ko.html">태우는 날</a>을 정해 두고, <a href="dlp-ko.html">문지기</a>가 성 밖으로 못 나가게 해요. 손님 것을 손님 것답게 다루면 <a href="compliance-ko.html">검사관</a>도, 손님도 웃어요.',
                   'The name tag gets a <a href="classification-en.html">red stamp</a>, a <a href="retention-en.html">burning day</a>, and a <a href="dlp-en.html">doorkeeper</a> who keeps it inside the castle. Treat the visitor\'s as the visitor\'s, and the <a href="compliance-en.html">inspector</a> smiles — and so does the visitor.')},
    ],
    "summary": (("<b>개인정보 보호</b> = 성 명부에 적힌 손님의 이름·집·생일은 <b>손님 것</b>이니, <b>먼저 묻고, 꼭 필요한 것만 적고, 남에겐 번호표로 주고, 달라면 지우고, 잃으면 바로 알리는</b> 약속.",
                 "<b>Privacy</b> = the visitor\'s name, home, and birthday in the castle roster are <b>the visitor\'s own</b> — so <b>ask first, write only what\'s needed, hand out a number instead, erase when asked, and tell them at once if it\'s lost</b>."),
                ("Privacy / Personal Data Protection. 개인정보(PII)는 그 사람의 것이라는 원칙에서 출발해요. 동의와 목적 제한, 최소 수집, 삭제 요청 처리, 가명처리, 유출 통지가 핵심이고, GDPR 이나 개인정보보호법 같은 규칙을 감독 기관이 점검해요.",
                 "It starts from the principle that personal data (PII) belongs to the person. Consent and purpose limitation, data minimization, handling deletion requests, pseudonymization, and breach notification are the core, and regulators check against rules like GDPR and national privacy laws.")),
    "glossary": [
        ("개인정보 (PII)", "Personal data (PII)", ("손님 이름표.", "The visitor\'s name tag."), ("이름, 집, 생일, 얼굴 — 누구인지 알아볼 수 있는 모든 것. 주인은 손님이에요.", "Name, home, birthday, face — anything that says who someone is. The visitor owns it.")),
        ("동의", "Consent", ("적기 전에 묻기.", "Asking before writing."), ("'적어도 돼요?' 하고 물어요. 손님이 '아니요' 해도 돼요.", "May I write it? The visitor may say no.")),
        ("목적 제한", "Purpose limitation", ("왜 적는지 말한 대로만.", "Only for the reason you gave."), ("빵 배달하려고 적은 집 주소를 장터 광고에 쓰면 안 돼요.", "A home written down for bread delivery can\'t be used for market ads.")),
        ("최소 수집", "Data minimization", ("꼭 필요한 것만.", "Only what\'s needed."), ('적지 않은 건 잃어버릴 수도 없어요. → <a href="retention-ko.html">종이마다 정해둔 태우는 날</a>', 'What you never wrote can never be lost. → <a href="retention-en.html">every paper has a burning day</a>')),
        ("삭제 요청", "Deletion request", ("'지워 주세요.'", "Erase it, please."), ('손님이 말하면 지워요, 여분 상자 사본까지. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'When the visitor asks, erase it — spare chest copy included. → <a href="backup-en.html">the spare chest kept far away</a>')),
        ("유출 통지", "Breach notification", ("잃으면 바로 알리기.", "Telling them at once."), ('도둑맞으면 손님과 검사관에게 정해진 날 안에 알려요. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'If it\'s stolen, tell the visitor and the inspector within the set days. → <a href="incident-en.html">the playbook for when a thief gets in</a>')),
        ("가명처리", "Pseudonymization", ("번호표.", "The number tag."), ('남에게 줄 땐 이름 대신 17번. 번호와 이름을 잇는 표는 성 안에만. → <a href="masking-ko.html">이름 가리기</a>', 'To others, No. 17 instead of the name. The table linking number to name stays in the castle. → <a href="masking-en.html">hiding the name</a>')),
        ("데이터 분류", "Data classification", ("이름표엔 빨간 도장.", "A red stamp on the name tag."), ('도장이 찍히면 문지기와 열쇠 꾸러미가 알아서 지켜요. → <a href="classification-ko.html">종이마다 찍는 색 도장</a>', 'Once stamped, the doorkeeper and the key ring know to guard it. → <a href="classification-en.html">a colored stamp on every paper</a>')),
    ],
}
