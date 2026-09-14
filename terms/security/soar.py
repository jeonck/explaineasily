from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def cat(x, y, s=1.0, color="var(--stone-dark)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="26" cy="30" rx="26" ry="16" fill="{color}"/>'
            f'<circle cx="-2" cy="14" r="14" fill="{color}"/><path d="M-12 6 L-10 -8 L-2 4 Z M8 4 L12 -8 L6 6 Z" fill="{color}"/>'
            f'<path d="M50 28 q14 -10 8 -26" stroke="{color}" stroke-width="6" fill="none" stroke-linecap="round"/>'
            f'<circle cx="-6" cy="12" r="2" fill="#FFF"/><circle cx="2" cy="12" r="2" fill="#FFF"/></g>')


def book(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-24" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-12 -12 h24 M-12 -2 h16 M-12 8 h24" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/></g>')


def tower(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-20" width="28" height="44" fill="var(--stone)"/>'
            f'{battlements(-14, -30, 28, 3, "var(--stone)", 10)}<rect x="-2" y="-52" width="3" height="24" fill="var(--night)"/><path d="M1 -50 L18 -44 L1 -38 Z" fill="var(--accent)"/>'
            f'<circle cx="0" cy="-6" r="5" fill="{SKIN}"/></g>')


def note(x, y, s=1.0, text=None):
    tx = label(0, 4, text, 9, "#142033") if text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-26" width="44" height="52" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-14 -14 h28 M-14 14 h20" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{tx}</g>')


def machine(x, y, s=1.0):
    rows = ("⟦1 일지 찾기|1 find the log⟧", "⟦2 망루에 묻기|2 ask the tower⟧", "⟦3 고양이면 끄기|3 a cat? dismiss⟧", "⟦4 도둑이면 문 잠그기|4 a thief? lock the door⟧")
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="200" height="150" rx="10" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>'
            f'<circle cx="170" cy="28" r="12" fill="none" stroke="var(--accent)" stroke-width="5" stroke-dasharray="6 4"/><circle cx="150" cy="44" r="8" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="4 3"/>'
            + label(80, 30, "⟦자동 순서표 기계|the machine⟧", 13, "var(--ink)", cls="d")
            + "".join(label(16, 62 + i * 24, r, 11, "var(--ink)", "start") for i, r in enumerate(rows)) + "</g>")


# 1. 경비실에 종이 하루 천 번
P1 = svg(300, sky(300)
         + "".join(bell(x, y, s) for x, y, s in ((80, 80, 0.7), (170, 60, 0.6), (260, 95, 0.8), (120, 175, 0.6), (230, 185, 0.5), (330, 160, 0.7), (350, 60, 0.5)))
         + label(210, 250, "⟦하루에 천 번 울려요|a thousand rings a day⟧", 12, "var(--ink)")
         + person(520, 110, s=0.9, face=FROWN + SWEAT, **BLUE) + bubble(430, 30, 260, 34, "⟦이걸 다 언제 봐요…|when do I look at all these…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(560, 250, "⟦하나하나 손으로 봐요|checking every one by hand⟧", 12, "var(--muted)")
         + label(380, 290, "⟦종은 많고 경비실 친구는 한 명이에요|so many bells, one friend in the guard room⟧", 12, "var(--ink)"))

# 2. 매번 손으로 순서표 — 고양이 보는 동안 도둑은 기다려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(50, 90, s=0.8, face=EYES, **BLUE) + note(150, 120, 1.5, text="⟦순서표|the book⟧") + label(120, 225, "⟦매번 손으로 순서표를 넘겨요|flipping the book by hand, every time⟧", 11, "var(--ink)")
         + cat(330, 125, 1.0) + bell(420, 90, 0.6) + label(380, 225, "⟦열 번 중 아홉 번은 고양이|nine in ten are cats⟧", 11, "var(--ink)")
         + person(600, 90, s=0.8, face=MASK, extra=BAG) + label(572, 150, "⟦…|…⟧", 24, "var(--bad)", cls="d") + label(640, 225, "⟦진짜 도둑은 뒤에서 기다려요|the real thief waits in line⟧", 11, "var(--bad)")
         + label(380, 280, "⟦고양이 종을 보는 동안 도둑 종은 뒤로 밀려요|while we check the cat, the thief\'s bell waits⟧", 12, "var(--ink)", cls="d"))

# 3. 자동 순서표 기계 (hero)
P3 = svg(360, sky(360)
         + bell(80, 130, 0.8) + '<path d="M120 130 H190" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M182 124 l10 6 l-10 6z" fill="var(--muted)"/>'
         + machine(200, 60)
         + "".join(f'<path d="M400 {y} H455" stroke="var(--muted)" stroke-width="2.5" stroke-dasharray="5 4"/>' for y in (85, 145, 205))
         + book(490, 78, 0.9) + label(530, 100, "⟦일지|the log⟧", 10, "var(--muted)", "start")
         + tower(490, 150, 0.8) + label(490, 190, "⟦망루 친구|tower friend⟧", 10, "var(--muted)")
         + dog(490, 212, 0.5) + label(490, 246, "⟦경비견|guard dog⟧", 10, "var(--muted)")
         + '<path d="M525 130 Q580 130 630 150" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + person(640, 120, s=0.9, face=SMILE, **BLUE) + note(600, 100, 0.9, text="⟦요약|summary⟧")
         + label(680, 250, "⟦사람은 쪽지만 읽어요|the person reads one note⟧", 10, "var(--muted)")
         + label(380, 300, "⟦종이 울리면 기계가 먼저 뛰어요|when a bell rings, the machine runs first⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦사람은 기계가 못 푸는 것만 봐요|the person only sees what the machine can\'t solve⟧", 12, "var(--muted)"))

# 4. 기계가 하는 순서
P4 = svg(320, sky(320)
         + '<path d="M110 120 H190 M250 120 H330 M390 120 L478 72 M390 120 L468 170 M555 72 L630 118 M575 170 L630 122" stroke="var(--muted)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + bell(80, 120, 0.7) + label(80, 178, "⟦종|bell⟧", 11, "var(--ink)")
         + book(220, 118, 1.0) + label(220, 178, "⟦일지 찾기|find the log⟧", 11, "var(--ink)")
         + tower(360, 130, 0.8) + label(360, 178, "⟦망루에 묻기|ask the tower⟧", 11, "var(--ink)")
         + cat(500, 50, 0.55) + label(520, 108, "⟦고양이 → 종 끄기|cat → dismiss⟧", 11, "var(--good)")
         + person(485, 140, s=0.55, face=MASK) + '<g transform="translate(540,165)"><rect x="-9" y="-6" width="18" height="14" rx="3" fill="var(--bad)"/><path d="M-5 -6 v-6 a5 5 0 0 1 10 0 v6" stroke="var(--bad)" stroke-width="3" fill="none"/></g>'
         + label(520, 225, "⟦도둑 → 문 잠그기|thief → lock the door⟧", 11, "var(--bad)")
         + note(660, 120, 1.1, text="⟦쪽지|note⟧") + label(660, 178, "⟦사람에게 요약 쪽지|a summary for the person⟧", 11, "var(--ink)")
         + label(380, 270, "⟦고양이는 기계가 끄고, 도둑은 기계가 가둬요|the machine dismisses the cat and locks up the thief⟧", 12, "var(--ink)", cls="d")
         + label(380, 300, "⟦사람 손엔 요약 쪽지 하나만 남아요|all that reaches the person is one note⟧", 12, "var(--muted)"))

# 5. 전과 후 — 그래도 처음 보는 도둑은 사람이
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + "".join(bell(x, y, 0.45, False) for x, y in ((50, 60), (100, 90), (150, 55), (200, 95), (60, 140), (120, 160), (190, 150), (250, 70), (260, 140)))
         + person(280, 100, s=0.8, face=FROWN + SWEAT, **BLUE) + label(190, 240, "⟦전엔 천 개를 다 사람이|before: a person, a thousand bells⟧", 12, "var(--ink)")
         + '<rect x="420" y="70" width="130" height="90" rx="8" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>' + label(485, 110, "⟦990개|990⟧", 20, "var(--ink)", cls="d") + label(485, 138, "⟦기계가|by the machine⟧", 11, "var(--muted)")
         + person(620, 100, s=0.8, face=SMILE, **BLUE) + note(700, 130, 0.9, text="⟦10|10⟧")
         + label(570, 240, "⟦이젠 사람은 열 개만|now: the person, ten⟧", 12, "var(--ink)")
         + label(380, 288, "⟦그 열 개는 기계가 처음 보는 도둑이에요 — 그건 사람이 봐요|those ten are thieves the machine has never seen — a person looks at those⟧", 11, "var(--ink)", cls="d"))

PLAY_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 20 h24 M20 30 h24 M20 40 h16" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/><circle cx="48" cy="46" r="9" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="5 3"/>')
ORCH_I = icon('<rect x="22" y="22" width="20" height="20" rx="4" fill="var(--accent)"/><circle cx="10" cy="12" r="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="54" cy="12" r="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="10" cy="52" r="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="54" cy="52" r="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M16 16 l8 8 M48 16 l-8 8 M16 48 l8 -8 M48 48 l-8 -8" stroke="var(--line)" stroke-width="3"/>')
CASE_I = icon('<rect x="12" y="14" width="40" height="42" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="24" y="8" width="16" height="10" rx="3" fill="#C9A86A"/><path d="M20 30 h24 M20 40 h24" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/><circle cx="46" cy="20" r="5" fill="#E9B44C"/>')
HUMAN_I = icon(f'<circle cx="32" cy="20" r="11" fill="{SKIN}"/><path d="M20 14 Q32 0 44 14 Z" fill="#5B8DEF"/><rect x="20" y="32" width="24" height="22" rx="6" fill="#5B8DEF"/><path d="M48 40 l6 6 l10 -12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "soar", "order": 81,
    "title": ("경비실의 자동 순서표 기계", "The Guard Room\'s Automatic Book"),
    "h1": ("<em>SOAR</em>가 뭐예요?", "What is <em>SOAR</em>?"),
    "sub": ("SOAR(Security Orchestration, Automation and Response)를 종이 울리면 순서표를 스스로 넘기는 경비실 기계 이야기로 풀어봤어요.",
            "SOAR (Security Orchestration, Automation and Response), told as a story about a guard-room machine that flips through the book on its own when a bell rings."),
    "panels": [
        {"svg": P1, "alt": ("종 일곱 개가 한꺼번에 울리고, 파란 모자 경비실 친구가 땀을 흘리며 '이걸 다 언제 봐요…' 하고 있음", "Seven bells ring at once; the blue-hat guard-room friend sweats: when do I look at all these…"),
         "caption": ("경비실에 종이 하루에 천 번 울려요.", "The guard room\'s bells ring a thousand times a day."),
         "small": ('<a href="soc-ko.html">경비실</a> 친구는 한 명이에요. 종 하나하나를 손으로 봐요.', 'There is one friend in the <a href="soc-en.html">guard room</a>. Every bell, checked by hand.')},
        {"svg": P2, "alt": ("경비실 친구가 순서표를 넘기고, 고양이 옆에서 종이 울리고, 빨간 모자 도둑은 뒤에서 기다림", "The guard flips the book, a bell rings beside a cat, and a red-hat thief waits at the back of the line"),
         "caption": ("종마다 순서표를 손으로 넘겨요. 그런데 열 번 중 아홉 번은 고양이예요.", "Every bell means flipping through the book by hand. And nine in ten are cats."),
         "small": ('고양이 종을 보는 동안 진짜 도둑의 종은 뒤로 밀려요. <a href="incident-ko.html">순서표</a>는 좋은데, 사람 손이 느려요.', 'While we check the cat, the real thief\'s bell waits. The <a href="incident-en.html">book</a> is good — human hands are just slow.')},
        {"svg": P3, "hero": True, "alt": ("종이 울리면 기계로 들어가고, 기계 안에는 순서 넷 — 일지 찾기, 망루에 묻기, 고양이면 끄기, 도둑이면 문 잠그기. 기계가 일지·망루 친구·경비견에 선을 뻗고, 경비실 친구는 요약 쪽지만 받음", "A bell feeds into the machine; inside are four steps — find the log, ask the tower, dismiss cats, lock the door on thieves. Lines run to the log, the tower friend, and the guard dog; the guard receives one summary note"),
         "caption": ("SOAR는 경비실의 자동 순서표 기계예요.", "SOAR is the guard room\'s automatic book."),
         "small": ("종이 울리면 기계가 먼저 뛰어요. 스스로 일지를 찾고, 망루에 묻고, 고양이면 끄고, 도둑이면 문을 잠가요. 사람에겐 요약 쪽지 한 장만 보내요.", "When a bell rings, the machine runs first. It finds the log, asks the tower, dismisses cats, locks doors on thieves — and sends the person one summary note."),
         "tricks": (4, [
             (PLAY_I, ("순서표를 기계에", "The book, in a machine"), ("적어둔 대로 스스로", "follows the steps on its own"), "warm"),
             (ORCH_I, ("친구들을 한 줄로", "Friends in a row"), ("일지·망루·경비견에 대신 물어요", "asks the log, tower, and dog for you")),
             (CASE_I, ("한 장에 모아요", "All on one page"), ("종 하나 = 쪽지 하나", "one bell = one note")),
             (HUMAN_I, ("사람은 어려운 것만", "People take the hard ones"), ("고양이는 기계가 꺼요", "the machine handles the cats"), "calm"),
         ])},
        {"svg": P4, "alt": ("점선 흐름: 종 → 일지 찾기 → 망루에 묻기 → 갈림길: 고양이면 종 끄기, 도둑이면 문 잠그기 → 사람에게 요약 쪽지", "A dotted flow: bell → find the log → ask the tower → fork: cat, dismiss; thief, lock the door → a summary note for the person"),
         "caption": ("기계는 정해진 순서로 물어보고, 갈림길에서 스스로 골라요.", "The machine asks in a fixed order and picks a path at the fork."),
         "small": ('<a href="log-ko.html">일지</a>를 찾고, <a href="cti-ko.html">망루 친구</a>에게 묻고, 고양이면 끄고, 도둑이면 <a href="edr-ko.html">경비견</a>에게 문을 잠그게 해요.', 'It finds the <a href="log-en.html">log</a>, asks the <a href="cti-en.html">tower friend</a>, dismisses cats, and has the <a href="edr-en.html">guard dog</a> lock the door on thieves.')},
        {"svg": P5, "alt": ("왼쪽: 종 아홉 개와 땀 흘리는 경비실 친구. 오른쪽: 기계가 990개, 경비실 친구는 쪽지 10개만 들고 웃음", "Left: nine bells and a sweating guard. Right: the machine takes 990, the guard smiles holding ten notes"),
         "caption": ("천 개 중 990개는 기계가, 열 개는 사람이 봐요.", "Of a thousand bells, the machine takes 990 and a person takes ten."),
         "small": ('그 열 개는 기계가 처음 보는 도둑이에요. 기계는 적어둔 순서만 해요 — 처음 보는 건 <a href="hunting-ko.html">사람</a>이 봐요. <a href="siem-ko.html">큰 화면</a>이 종을 모으고, 이 기계가 종을 처리해요.',
                   'Those ten are thieves the machine has never seen. It only follows what was written — the new ones go to <a href="hunting-en.html">a person</a>. The <a href="siem-en.html">big screen</a> gathers the bells; this machine handles them.')},
    ],
    "summary": (("<b>SOAR</b> = 종이 울리면 <b>기계가 먼저</b> 일지 찾고, 망루에 묻고, 고양이면 끄고, 도둑이면 문 잠그고, 사람에겐 <b>요약 쪽지 한 장</b>만 주는 경비실의 자동 순서표.",
                 "<b>SOAR</b> = when a bell rings, <b>the machine runs first</b> — finds the log, asks the tower, dismisses cats, locks doors on thieves — and hands the person <b>one summary note</b>."),
                ("Security Orchestration, Automation and Response. 경보가 오면 플레이북대로 여러 보안 도구(SIEM, CTI, EDR, 티켓)를 자동으로 호출해 조사·대응하고, 사람은 판단이 필요한 케이스만 받아요.",
                 "When an alert arrives, it runs a playbook that calls the security tools (SIEM, CTI, EDR, ticketing) to investigate and respond automatically; people receive only the cases that need judgment.")),
    "glossary": [
        ("SOAR", "SOAR", ("자동 순서표 기계.", "The automatic book."), ("종이 울리면 스스로 순서표를 넘기고 친구들에게 대신 물어봐요.", "When a bell rings, it flips the book itself and asks the other friends for you.")),
        ("플레이북 자동화", "Playbook automation", ("적어둔 순서를 기계가.", "The written steps, run by a machine."), ('사람이 하던 순서표를 기계가 그대로 해요. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'The book people used to follow, followed by a machine. → <a href="incident-en.html">the book for when a thief gets in</a>')),
        ("오케스트레이션", "Orchestration", ("친구들을 한 줄로 세우기.", "Lining the friends up."), ("일지, 망루, 경비견, 문지기에게 순서대로 묻고 시키는 것.", "Asking and instructing the log, the tower, the dog, and the doorkeeper, in order.")),
        ("케이스 관리", "Case management", ("종 하나에 쪽지 하나.", "One note per bell."), ("누가 뭘 봤고 뭘 했는지 한 장에 모아요.", "Who saw what and did what, gathered on one page.")),
        ("자동 대응", "Automated response", ("도둑이면 문 잠그기.", "A thief? Lock the door."), ('사람이 오기 전에 기계가 먼저 가둬요. → <a href="edr-ko.html">경비견</a>', 'The machine contains it before a person arrives. → <a href="edr-en.html">the guard dog</a>')),
        ("오탐 줄이기", "Alert fatigue", ("고양이 종 끄기.", "Dismissing cat bells."), ("열 번 중 아홉 번인 고양이를 기계가 걸러야 사람이 도둑을 봐요.", "The machine filters out the nine-in-ten cats so people can look at the thief.")),
        ("SIEM", "SIEM", ("종을 모으는 큰 화면.", "The big screen that gathers bells."), ('큰 화면이 종을 울리고, 이 기계가 종을 처리해요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'The big screen rings the bells; this machine handles them. → <a href="siem-en.html">the guard room\'s big screen</a>')),
        ("티켓", "Ticket", ("사람에게 가는 쪽지.", "The note that reaches a person."), ("기계가 못 푼 것만 사람 책상에 올라가요.", "Only what the machine can\'t solve lands on a person\'s desk.")),
    ],
}
