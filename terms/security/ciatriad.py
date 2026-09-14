from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
COOK = dict(hat="#FFF", shirt="#FFF")
C_SEE, C_CHANGE, C_USE = "#5B8DEF", "var(--accent)", "var(--good)"   # 못 보게 · 못 바꾸게 · 늘 쓰게


def envelope(x, y, s=1.0, sealed=True, peeked=False):
    seal = '<circle cy="2" r="7" fill="var(--bad)"/>' if sealed else ""
    inner = ('<rect x="-20" y="-42" width="40" height="28" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
             '<path d="M-12 -34 h24 M-12 -26 h16" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>') if peeked else ""
    return (f'<g transform="translate({x},{y}) scale({s})">{inner}<rect x="-30" y="-20" width="60" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-30 -20 l30 20 l30 -20" stroke="#C9A86A" stroke-width="2" fill="none"/>{seal}</g>')


def fingerprint(x, y, s=1.0, color="var(--night)"):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round">'
            f'<path d="M-4 6 a4 4 0 0 1 8 0 v6"/><path d="M-10 6 a10 10 0 0 1 20 0 v10"/><path d="M-16 6 a16 16 0 0 1 32 0 v12"/><path d="M-22 6 a22 22 0 0 1 44 0"/></g>')


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def ledger(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="-40" width="64" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(0, -22, "⟦오늘 빵|bread today⟧", 10, "#142033") + label(0, 0, "⟦30개|30 loaves⟧", 13, "#142033", cls="d")
            + '<path d="M-24 -4 h48" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>' + label(0, 24, "⟦→ 80개|→ 80⟧", 14, "var(--bad)", cls="d") + "</g>")


# 1. 왕은 도둑만 걱정하지만, 곤란한 일은 세 가지
P1 = svg(320, sky(320)
         + person(40, 80, s=0.85, face=EYES, **KING)
         + bubble(20, 18, 250, 34, "⟦도둑만 안 들어오면 되지?|as long as no thief gets in, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(240, 95, s=0.7, face=MASK) + envelope(335, 150, 1.0, sealed=False, peeked=True)
         + '<path d="M272 116 L312 118" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4" stroke-linecap="round"/>'
         + label(300, 250, "⟦몰래 봐요|someone peeks⟧", 12, "var(--bad)")
         + ledger(470, 150) + label(470, 250, "⟦몰래 고쳐요|someone changes it⟧", 12, "var(--bad)")
         + gate(640, 60, 0.8) + person(596, 128, s=0.4, face=MASK) + person(626, 138, s=0.4, face=MASK) + person(656, 128, s=0.4, face=MASK)
         + person(540, 150, s=0.5, hat=None, shirt="#7B3FA0", face=FROWN) + label(640, 250, "⟦진짜 손님이 못 들어가요|real guests can\'t get in⟧", 12, "var(--bad)")
         + label(380, 300, "⟦도둑을 막아도 곤란한 일은 세 가지나 있어요|even with thieves out, three things can still go wrong⟧", 12, "var(--ink)", cls="d"))

# 2. 하나만 지키면 — 다 금고에 넣고 열쇠를 잃어버렸어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + chest(150, 175, 1.7, color="var(--stone)", lock=True)
         + label(150, 240, "⟦못 보게: 지켰어요|no peeking: kept⟧", 11, "var(--good)")
         + person(280, 75, s=0.8, face=FROWN + SWEAT, **GUARD)
         + bubble(200, 14, 230, 34, "⟦다 금고에 넣었어요… 열쇠는 어디?|all in the vault… now where\'s the key?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(520, 95, s=0.8, face=FROWN + SWEAT, **COOK)
         + bubble(440, 34, 250, 34, "⟦레시피가 금고 안에… 빵을 못 구워요|the recipe\'s locked in… no bread today⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(560, 240, "⟦늘 쓰게: 못 지켰어요|always there: broken⟧", 11, "var(--bad)")
         + label(380, 288, "⟦하나만 지키면 성이 멈춰요 — 셋을 같이 봐야 해요|guard just one, and the castle stops — you need all three⟧", 12, "var(--ink)", cls="d"))

# 3. 세 가지 약속 (hero)
COLS = ((140, C_SEE, "⟦못 보게|no peeking⟧", "⟦남이 못 읽어요|others can\'t read it⟧", "⟦봉인 편지 · 색 도장|sealed letters · colored stamps⟧"),
        (380, C_CHANGE, "⟦못 바꾸게|no tampering⟧", "⟦몰래 못 고쳐요|nobody changes it in secret⟧", "⟦지문 · 왕의 도장|fingerprints · the king\'s seal⟧"),
        (620, C_USE, "⟦늘 쓰게|always there⟧", "⟦필요할 때 있어요|there when you need it⟧", "⟦여분 상자 · 열린 성문|spare chests · an open gate⟧"))
P3 = svg(300, sky(300)
         + label(380, 40, "⟦성이 지키는 세 가지 약속|the three promises a castle keeps⟧", 14, "var(--ink)", cls="d")
         + "".join(f'<circle cx="{x}" cy="96" r="44" fill="{c}"/>' + label(x, 172, t, 15, "var(--ink)", cls="d") + label(x, 194, s_, 11, "var(--muted)") + label(x, 218, tools, 11, "var(--accent)") for x, c, t, s_, tools in COLS)
         + envelope(140, 96, 1.0) + fingerprint(380, 90, 1.1, "#FFF") + chest(602, 100, 0.75) + chest(640, 94, 0.75)
         + label(380, 276, "⟦셋을 다 지켜야 성이 성이에요|keep all three, or it isn\'t a castle⟧", 12, "var(--ink)", cls="d"))

# 4. 누가 지켜요 (표)
ROWS = ((C_SEE, "⟦못 보게|no peeking⟧", "⟦봉인 편지 · 색 도장 · 열쇠 꾸러미|sealed letters · colored stamps · key rings⟧", "⟦훔쳐가도 못 읽고, 아무나 못 열어요|stolen, still unreadable; not everyone gets a key⟧"),
        (C_CHANGE, "⟦못 바꾸게|no tampering⟧", "⟦지문 · 왕의 도장 · 일지|fingerprints · the king\'s seal · the logbook⟧", "⟦바꾸면 지문이 안 맞아요|change it, and the print no longer matches⟧"),
        (C_USE, "⟦늘 쓰게|always there⟧", "⟦여분 상자 · 줄 안내원 · 다음 날 장사하는 법|spare chests · line ushers · the next-day plan⟧", "⟦불이 나도, 가짜 손님 떼가 와도|through fires and fake crowds⟧"))
P4 = svg(340, sky(340)
         + '<rect x="40" y="30" width="680" height="240" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="36" rx="8" fill="#C9A86A"/>'
         + label(130, 54, "⟦약속|promise⟧", 13, "#142033", cls="d") + label(470, 54, "⟦누가 지켜요|who keeps it⟧", 13, "#142033", cls="d")
         + '<path d="M220 66 v204" stroke="#C9A86A" stroke-width="1.5"/>'
         + "".join(f'<path d="M40 {66 + i * 68} h680" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
         + "".join(f'<circle cx="70" cy="{100 + i * 68}" r="9" fill="{c}"/>' + label(145, 105 + i * 68, t, 13, "#142033", cls="d") + label(470, 96 + i * 68, tools, 12, "#142033") + label(470, 118 + i * 68, why, 10, "#142033", weight=400) for i, (c, t, tools, why) in enumerate(ROWS))
         + label(380, 312, "⟦성의 도구는 전부 이 셋 중 하나를 지켜요|every tool in the castle keeps one of these three⟧", 12, "var(--ink)", cls="d"))

# 5. 셋은 서로 당겨요 — 저울
P5 = svg(320, sky(320)
         + '<path d="M300 60 L150 250 L450 250 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + f'<circle cx="300" cy="60" r="12" fill="{C_SEE}"/><circle cx="150" cy="250" r="12" fill="{C_CHANGE}"/><circle cx="450" cy="250" r="12" fill="{C_USE}"/>'
         + label(300, 40, "⟦못 보게|no peeking⟧", 12, "var(--ink)", cls="d") + label(150, 280, "⟦못 바꾸게|no tampering⟧", 12, "var(--ink)", cls="d") + label(450, 280, "⟦늘 쓰게|always there⟧", 12, "var(--ink)", cls="d")
         + '<circle cx="240" cy="210" r="7" fill="var(--night)"/>' + label(240, 196, "⟦은행 성|the bank castle⟧", 10, "var(--muted)")
         + '<circle cx="370" cy="220" r="7" fill="var(--night)"/>' + label(370, 206, "⟦장터 게시판|the market board⟧", 10, "var(--muted)")
         + '<circle cx="300" cy="150" r="9" fill="var(--accent)"/>' + label(300, 136, "⟦우리 성은?|our castle?⟧", 11, "var(--accent)", cls="d")
         + person(560, 90, s=0.9, face=EYES, **KING)
         + bubble(480, 18, 260, 34, "⟦금고를 더 잠글까, 열쇠를 더 나눌까?|lock it tighter, or hand out more keys?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(600, 220, "⟦더 잠그면 못 쓰고, 더 나누면 새요|tighter: nobody can use it · looser: it leaks⟧", 10, "var(--muted)")
         + label(380, 304, "⟦셋은 서로 당겨요 — 성마다 저울이 달라요|the three pull on each other — every castle sets its own balance⟧", 12, "var(--ink)", cls="d"))

PEEK_I = icon('<rect x="10" y="20" width="44" height="30" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M10 20 l22 16 l22 -16" stroke="#C9A86A" stroke-width="2" fill="none"/><circle cx="32" cy="38" r="6" fill="var(--bad)"/>')
PRINT_I = icon('<g fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"><path d="M28 34 a4 4 0 0 1 8 0 v8"/><path d="M22 34 a10 10 0 0 1 20 0 v12"/><path d="M16 34 a16 16 0 0 1 32 0 v14"/><path d="M12 30 a20 20 0 0 1 40 0"/></g>')
BOX_I = icon('<rect x="8" y="30" width="26" height="20" rx="3" fill="#8B5E3C"/><rect x="8" y="26" width="26" height="6" fill="#5A3B22"/><rect x="30" y="22" width="26" height="20" rx="3" fill="#8B5E3C"/><rect x="30" y="18" width="26" height="6" fill="#5A3B22"/>')
BALANCE_I = icon('<path d="M32 12 L12 50 H52 Z" fill="none" stroke="var(--ink)" stroke-width="3" stroke-linejoin="round"/><circle cx="32" cy="12" r="5" fill="#5B8DEF"/><circle cx="12" cy="50" r="5" fill="var(--accent)"/><circle cx="52" cy="50" r="5" fill="var(--good)"/><circle cx="32" cy="36" r="4" fill="var(--ink)"/>')

PAGE = {
    "slug": "ciatriad", "order": 101,
    "title": ("지키는 것 세 가지: 못 보게, 못 바꾸게, 늘 쓰게", "Three Things to Keep: No Peeking, No Tampering, Always There"),
    "h1": ("<em>CIA 3요소</em>가 뭐예요?", "What is the <em>CIA Triad</em>?"),
    "sub": ("CIA 3요소(Confidentiality · Integrity · Availability)를 성이 지키는 세 가지 약속 이야기로 풀어봤어요.",
            "The CIA triad — confidentiality, integrity, availability — told as a story about the three promises a castle keeps."),
    "panels": [
        {"svg": P1, "alt": ("왕이 '도둑만 안 들어오면 되지?' 하고 묻는 옆에서 세 장면: 도둑이 편지를 몰래 보고, 장부의 빵 30개가 80개로 고쳐지고, 성문 앞 가짜 손님 떼 때문에 진짜 손님이 못 들어감", "Beside a king asking whether keeping thieves out is enough, three scenes: a thief peeks at a letter, a ledger\'s 30 loaves is changed to 80, and a crowd of fake guests at the gate keeps a real guest out"),
         "caption": ("성이 지키는 건 도둑만이 아니에요.", "A castle guards against more than thieves."),
         "small": ("도둑을 막아도 누가 편지를 몰래 보고, 장부를 몰래 고치고, 성문을 막을 수 있어요. 곤란한 일은 세 가지예요.", "Even with thieves out, someone can peek at a letter, quietly change the ledger, or block the gate. Three different kinds of trouble.")},
        {"svg": P2, "alt": ("잠긴 돌 금고 옆에서 경비가 땀 흘리며 '다 금고에 넣었어요… 열쇠는 어디?' 하고, 요리사는 '레시피가 금고 안에… 빵을 못 구워요' 하고 있음", "Beside a locked stone vault, a sweating guard says everything is in the vault but the key is missing, and a cook says the recipe is locked in and there is no bread today"),
         "caption": ("하나만 지키면 성이 멈춰요.", "Keep just one promise, and the castle stops."),
         "small": ("경비가 다 금고에 넣고 열쇠를 잃어버렸어요. 아무도 못 보긴 해요 — 요리사도요. 그래서 오늘은 빵이 없어요.", "The guard locked everything in the vault and lost the key. Nobody can peek — not even the cook. So there is no bread today.")},
        {"svg": P3, "hero": True, "alt": ("세 개의 큰 동그라미: 파란 동그라미에 봉인 편지(못 보게), 주황 동그라미에 지문(못 바꾸게), 초록 동그라미에 여분 상자 둘(늘 쓰게). 각각 아래에 어떤 친구가 지키는지 적혀 있음", "Three big circles: a blue one with a sealed letter (no peeking), an orange one with a fingerprint (no tampering), a green one with two spare chests (always there), each listing which helpers keep it"),
         "caption": ("CIA 3요소는 성이 지키는 세 가지 약속이에요.", "The CIA triad is the three promises a castle keeps."),
         "small": ('남이 못 보게(<a href="encryption-ko.html">봉인 편지</a>, <a href="classification-ko.html">색 도장</a>), 몰래 못 바꾸게(<a href="hashing-ko.html">지문</a>, <a href="pki-ko.html">왕의 도장</a>), 필요할 때 늘 쓰게(<a href="backup-ko.html">여분 상자</a>). 셋을 다 지켜야 해요.',
                   'No peeking (<a href="encryption-en.html">sealed letters</a>, <a href="classification-en.html">colored stamps</a>), no tampering (<a href="hashing-en.html">fingerprints</a>, <a href="pki-en.html">the king\'s seal</a>), always there (<a href="backup-en.html">spare chests</a>). All three, together.'),
         "tricks": (4, [
             (PEEK_I, ("못 보게", "No peeking"), ("훔쳐가도 못 읽어요", "stolen, still unreadable"), "calm"),
             (PRINT_I, ("못 바꾸게", "No tampering"), ("바꾸면 지문이 안 맞아요", "change it, the print won\'t match")),
             (BOX_I, ("늘 쓰게", "Always there"), ("불이 나도, 손님 떼가 와도", "through fires and fake crowds")),
             (BALANCE_I, ("셋을 같이", "All three at once"), ("하나만 세게 하면 다른 게 무너져요", "push one too hard, another falls"), "warm"),
         ])},
        {"svg": P4, "alt": ("표: 못 보게 — 봉인 편지·색 도장·열쇠 꾸러미, 못 바꾸게 — 지문·왕의 도장·일지, 늘 쓰게 — 여분 상자·줄 안내원·다음 날 장사하는 법", "A table: no peeking — sealed letters, colored stamps, key rings; no tampering — fingerprints, the king\'s seal, the logbook; always there — spare chests, line ushers, the next-day plan"),
         "caption": ("성의 도구는 전부 이 셋 중 하나를 지켜요.", "Every tool in the castle keeps one of the three."),
         "small": ('<a href="rbac-ko.html">열쇠 꾸러미</a>는 못 보게, <a href="log-ko.html">일지</a>는 못 바꾸게, <a href="loadbalancer-ko.html">줄 안내원</a>과 <a href="drp-ko.html">다음 날 장사하는 법</a>은 늘 쓰게. 새 도구를 보면 "셋 중 어느 약속이지?" 하고 물어보면 돼요.',
                   '<a href="rbac-en.html">Key rings</a> keep no peeking, the <a href="log-en.html">logbook</a> keeps no tampering, <a href="loadbalancer-en.html">line ushers</a> and the <a href="drp-en.html">next-day plan</a> keep always there. Meet a new tool, and just ask: which of the three?')},
        {"svg": P5, "alt": ("세 꼭짓점이 못 보게·못 바꾸게·늘 쓰게인 삼각형. 은행 성은 못 보게·못 바꾸게 쪽에, 장터 게시판은 늘 쓰게 쪽에, 우리 성은 가운데 물음표. 왕이 '금고를 더 잠글까, 열쇠를 더 나눌까?' 하고 고민함", "A triangle with corners no peeking, no tampering, always there. The bank castle sits toward the first two, the market board toward always there, and our castle is a question mark in the middle. The king wonders whether to lock tighter or hand out more keys"),
         "caption": ("셋은 서로 당겨요. 성마다 저울이 달라요.", "The three pull on each other. Every castle sets its own balance."),
         "small": ('더 잠그면 못 쓰고, 더 나누면 새요. 어느 쪽으로 기울일지는 <a href="risk-ko.html">저울</a>로 정하고, 지킬 땐 <a href="defenseindepth-ko.html">겹겹이</a> 지켜요.',
                   'Tighter, and nobody can use it; looser, and it leaks. Where to lean is decided on the <a href="risk-en.html">scale</a>, and whatever you keep, you keep <a href="defenseindepth-en.html">in layers</a>.')},
    ],
    "summary": (("<b>CIA 3요소</b> = 성이 지키는 세 가지 약속 — 남이 <b>못 보게</b>, 몰래 <b>못 바꾸게</b>, 필요할 때 <b>늘 쓰게</b>. 셋은 서로 당기니까 <b>같이</b> 봐야 해요.",
                 "<b>The CIA triad</b> = the three promises a castle keeps — <b>no peeking</b>, <b>no tampering</b>, <b>always there</b>. They pull on each other, so you weigh them <b>together</b>."),
                ("CIA Triad — Confidentiality(기밀성), Integrity(무결성), Availability(가용성). 정보 보안의 세 가지 목표예요. 암호화·접근 통제는 기밀성, 해시·서명·로그는 무결성, 백업·이중화·DDoS 방어는 가용성을 지켜요. 셋은 트레이드오프라 위험에 따라 균형을 정해요.",
                 "Confidentiality, Integrity, Availability — the three goals of information security. Encryption and access control serve confidentiality; hashing, signatures, and logs serve integrity; backups, redundancy, and DDoS defense serve availability. They trade off, so the balance follows the risk.")),
    "glossary": [
        ("기밀성", "Confidentiality", ("못 보게.", "No peeking."), ('봐도 되는 사람만 봐요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Only those allowed get to see. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("무결성", "Integrity", ("못 바꾸게.", "No tampering."), ('몰래 바뀌면 알아채요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>', 'If it changes in secret, you can tell. → <a href="hashing-en.html">a fingerprint on everything</a>')),
        ("가용성", "Availability", ("늘 쓰게.", "Always there."), ('필요할 때 있어야 해요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>, <a href="ddos-ko.html">성문 앞 가짜 손님 떼</a>', 'It has to be there when needed. → <a href="backup-en.html">the spare chest far away</a>, <a href="ddos-en.html">fake guests at the gate</a>')),
        ("부인 방지", "Non-repudiation", ("'내가 안 보냈어요'를 못 해요.", "No saying you never sent it."), ('왕의 도장이 찍혀 있으니까요. → <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>', 'The king\'s seal is on it. → <a href="pki-en.html">the badge with the king\'s seal</a>')),
        ("인증", "Authentication", ("네가 너인지.", "Proving you are you."), ('세 약속을 지키려면 먼저 누군지 알아야 해요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'To keep any promise, you first need to know who is asking. → <a href="mfa-en.html">the doorkeeper who checks three times</a>')),
        ("트레이드오프", "Trade-off", ("셋의 저울.", "The three-way scale."), ("더 잠그면 못 쓰고, 더 나누면 새요. 은행은 못 바꾸게 쪽으로, 게시판은 늘 쓰게 쪽으로 기울여요.", "Tighter means unusable, looser means leaky. A bank leans toward no tampering, a notice board toward always there.")),
        ("위험", "Risk", ("어느 쪽으로 기울일지.", "Which way to lean."), ('잃으면 제일 아픈 약속부터 지켜요. → <a href="risk-ko.html">어느 문부터 지킬지 정하는 저울</a>', 'Keep first the promise that hurts most to break. → <a href="risk-en.html">the scale that picks which door to guard first</a>')),
        ("다층 방어", "Defense in depth", ("겹겹이.", "In layers."), ('약속 하나를 도구 하나에만 맡기지 않아요. → <a href="defenseindepth-ko.html">겹겹이 두른 성벽</a>', 'No promise rests on a single tool. → <a href="defenseindepth-en.html">walls within walls</a>')),
    ],
}
