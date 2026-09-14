from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def paper(x, y, s=1.0, stamp=None, rot=0, text=None, faded=False):
    st = f'<circle cx="18" cy="-14" r="9" fill="{stamp}"/>' if stamp else ""
    tx = label(0, 24, text, 9, "#142033") if text else ""
    op = ' opacity="0.5"' if faded else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"{op}><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -8 h28 M-18 1 h18 M-18 10 h28" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{st}{tx}</g>')


def stack(x, y, n, s=1.0):
    return "".join(paper(x + (i % 3) * 6, y - i * 7, s, rot=(i * 7) % 10 - 5) for i in range(n))


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def flame(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M0 -12 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/></g>'


def calendar(x, y, s=1.0, text="", color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="-26" y="-22" width="52" height="12" rx="4" fill="{color}"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/>{label(0, 12, text, 12, "#142033", cls="d")}</g>')


# 1. 종이는 쌓이기만 해요 — 30년 전 손님 명부까지
P1 = svg(320, sky(320)
         + '<rect x="40" y="60" width="300" height="200" rx="4" fill="var(--stone)" opacity="0.5"/>'
         + stack(90, 230, 8, 0.6) + stack(170, 235, 10, 0.6) + stack(250, 225, 7, 0.6) + stack(130, 150, 6, 0.55) + stack(220, 150, 9, 0.55)
         + label(190, 290, "⟦창고가 넘쳐요|the storeroom overflows⟧", 12, "var(--muted)")
         + person(430, 130, s=0.8, face=FROWN + SWEAT, **CLERK) + paper(510, 160, 0.9, rot=8, text="⟦30년 전 손님 명부|guest list, 30 yrs ago⟧", faded=True)
         + bubble(400, 40, 240, 34, "⟦이거 아직 필요해요? 아무도 몰라요|do we still need this? nobody knows⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(640, 150, s=0.75, face=MASK, extra=BAG) + label(670, 262, "⟦도둑한텐 전부 보물|to a thief, all of it is treasure⟧", 10, "var(--bad)")
         + label(380, 305, "⟦버리지 않으면 지킬 것만 늘어나요|what you never throw away, you must keep guarding⟧", 12, "var(--ink)"))

# 2. 너무 오래 두면 / 너무 빨리 버리면
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + stack(120, 170, 12, 0.6) + person(240, 120, s=0.7, face=MASK, extra=BAG) + label(190, 240, "⟦너무 오래 두면|keep too long⟧", 14, "var(--ink)", cls="d") + label(190, 262, "⟦도둑이 가져갈 게 많아요|a thief has more to take⟧", 11, "var(--bad)")
         + flame(520, 150, 1.2) + person(620, 100, s=0.75, face=FROWN + SWEAT, **KING) + bubble(560, 30, 170, 34, "⟦작년 장부 어디 갔지?|where\'s last year\'s ledger?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(570, 240, "⟦너무 빨리 버리면|throw away too soon⟧", 14, "var(--ink)", cls="d") + label(570, 262, "⟦세금 검사관이 물어볼 때 없어요|nothing to show the tax inspector⟧", 11, "var(--accent)")
         + label(380, 292, "⟦오래도 안 되고, 빨리도 안 돼요 — 종이마다 날짜가 필요해요|neither too long nor too soon — every paper needs a date⟧", 11, "var(--muted)"))

# 3. 종이마다 태우는 날 (hero)
ROWS = (("⟦장터 공지|market notice⟧", "var(--good)", "⟦1달|1 mo⟧"), ("⟦손님 명부|guest list⟧", "#5B8DEF", "⟦1년|1 yr⟧"), ("⟦세금 장부|tax ledger⟧", "var(--accent)", "⟦7년|7 yrs⟧"), ("⟦성문 열쇠 그림|gate key drawing⟧", "var(--bad)", "⟦쓰는 동안만|while in use⟧"))
P3 = svg(360, sky(360)
         + '<rect x="60" y="30" width="400" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="60" y="30" width="400" height="30" rx="8" fill="#C9A86A"/>' + label(260, 50, "⟦보관 기간표|HOW LONG WE KEEP IT⟧", 13, "#142033", cls="d")
         + label(340, 82, "⟦얼마나|how long⟧", 11, "#142033", cls="d") + label(420, 82, "⟦그다음|then⟧", 11, "#142033", cls="d")
         + "".join(f'<circle cx="86" cy="{106 + i * 40}" r="9" fill="{c}"/>' + label(104, 111 + i * 40, t, 13, "#142033", "start") + label(340, 111 + i * 40, d, 13, "#142033") + flame(420, 118 + i * 40, 0.45) for i, (t, c, d) in enumerate(ROWS))
         + person(540, 90, s=0.8, face=SMILE, **CLERK) + calendar(640, 120, 1.0, "⟦7년|7y⟧") + paper(640, 200, 0.8, stamp="var(--accent)")
         + label(600, 262, "⟦종이를 만들 때 날짜를 같이 적어요|write the date the day the paper is born⟧", 10, "var(--muted)")
         + flame(560, 320, 0.9) + label(380, 330, "⟦날이 오면 태워요 — 아까워도, 잊었어도|when the day comes, burn it — even if you\'re fond of it, even if you forgot⟧", 12, "var(--ink)", cls="d"))

# 4. 태우는 날 — 어떻게 버리나도 정해져 있어요
P4 = svg(320, sky(320)
         + calendar(80, 80, 1.0, "⟦오늘|today⟧", "var(--bad)") + label(80, 140, "⟦태우는 날|burning day⟧", 11, "var(--ink)", cls="d")
         + person(180, 110, s=0.75, face=SMILE, **CLERK)
         + paper(300, 110, 0.9, stamp="var(--good)") + '<rect x="270" y="150" width="60" height="40" rx="4" fill="var(--stone)"/>' + label(300, 215, "⟦초록: 휴지통|green: the bin⟧", 10, "var(--muted)")
         + paper(430, 110, 0.9, stamp="#5B8DEF") + '<path d="M410 160 l10 -8 l10 8 l10 -8 l10 8" stroke="var(--stone-dark)" stroke-width="3" fill="none"/>' + label(430, 215, "⟦파랑: 찢기|blue: tear⟧", 10, "var(--muted)")
         + paper(560, 110, 0.9, stamp="var(--bad)") + flame(560, 180, 0.8) + label(560, 215, "⟦빨강: 태우기|red: burn⟧", 10, "var(--muted)")
         + '<g transform="translate(680,110)"><rect x="-28" y="-30" width="56" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-20 -20 l40 44 M20 -20 l-40 44" stroke="var(--bad)" stroke-width="3"/></g>' + label(680, 215, "⟦여분 상자 것도 같이|the spare chest copy too⟧", 10, "var(--muted)")
         + label(380, 262, "⟦버리는 방법은 도장 색이 정해요|how it goes depends on the stamp⟧", 12, "var(--ink)", cls="d")
         + label(380, 295, "⟦여분 상자에 남은 사본까지 같이 — 안 그러면 버린 게 아니에요|the copy in the spare chest goes too — or it was never really gone⟧", 11, "var(--muted)"))

# 5. 검사관이 오면 — 있어야 할 건 있고, 없어야 할 건 없어요
P5 = svg(300, sky(300)
         + person(80, 100, s=0.85, face=EYES, hat="var(--stone-dark)", shirt="#2E3D57", extra='<rect x="50" y="66" width="30" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>') + label(110, 220, "⟦검사관|the inspector⟧", 11, "var(--muted)")
         + bubble(150, 30, 260, 34, "⟦3년 전 세금 장부 좀 봅시다|show me the tax ledger from 3 years ago⟧", 10, "var(--panel)", "var(--line)", "left")
         + person(320, 110, s=0.8, face=SMILE, **CLERK) + paper(400, 140, 0.9, stamp="var(--accent)", text="⟦세금 장부|tax ledger⟧") + label(370, 220, "⟦여기 있어요|here it is⟧", 11, "var(--good)", cls="d")
         + '<rect x="520" y="70" width="200" height="120" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>' + label(620, 100, "⟦30년 전 손님 명부?|guest list from 30 yrs ago?⟧", 11, "var(--ink)") + label(620, 130, "⟦— 없어요, 태웠어요|— gone, we burned it⟧", 12, "var(--good)", cls="d") + label(620, 160, "⟦도둑도 못 가져가요|so no thief can take it⟧", 10, "var(--muted)")
         + label(380, 270, "⟦있어야 할 건 있고, 없어야 할 건 없어요|what should be there is there; what shouldn\'t, isn\'t⟧", 13, "var(--ink)", cls="d"))

DATE_I = icon('<rect x="12" y="14" width="40" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="14" width="40" height="10" rx="4" fill="var(--accent)"/><path d="M22 8 v10 M42 8 v10" stroke="#5A3B22" stroke-width="3"/><circle cx="32" cy="40" r="6" fill="var(--bad)"/>')
BURN_I = icon('<path d="M32 10 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M32 28 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/><rect x="16" y="48" width="32" height="6" rx="2" fill="var(--stone-dark)"/>')
LAW_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><circle cx="44" cy="44" r="7" fill="var(--accent)"/><path d="M41 44 l2 2 l4 -4" stroke="#FFF" stroke-width="2" fill="none"/>')
COPY_I = icon(f'<rect x="10" y="30" width="26" height="22" rx="3" fill="{WOOD}"/><rect x="28" y="12" width="26" height="22" rx="3" fill="{WOOD}"/><path d="M14 34 l18 14 M32 34 l-18 14" stroke="var(--bad)" stroke-width="3"/><path d="M32 16 l18 14 M50 16 l-18 14" stroke="var(--bad)" stroke-width="3"/>')

PAGE = {
    "slug": "retention", "order": 60,
    "title": ("종이마다 정해둔 태우는 날", "Every Paper Has a Burning Day"),
    "h1": ("<em>데이터 보존</em>이 뭐예요?", "What is <em>Data Retention</em>?"),
    "sub": ("데이터 보존(Data Retention)을 종이마다 얼마나 두고 언제 태울지 미리 정해두는 이야기로 풀어봤어요.",
            "Data retention, told as a story about deciding, for every paper, how long to keep it and when to burn it."),
    "panels": [
        {"svg": P1, "alt": ("종이 더미로 넘치는 창고. 서기가 30년 전 손님 명부를 들고 '아직 필요해요? 아무도 몰라요'. 옆의 도둑에겐 전부 보물", "A storeroom overflowing with paper. A clerk holds a guest list from 30 years ago — do we still need this? nobody knows. To the thief beside, all of it is treasure"),
         "caption": ("종이는 쌓이기만 해요. 30년 전 손님 명부까지요.", "Paper only piles up. Even the guest list from 30 years ago."),
         "small": ('버리지 않으면 지킬 것만 늘어나요. 도둑한텐 오래된 명부도 <a href="classification-ko.html">빨간 도장 종이</a>만큼 보물이에요.',
                   'What you never throw away, you must keep guarding. To a thief, an old guest list is as much treasure as a <a href="classification-en.html">red-stamped paper</a>.')},
        {"svg": P2, "alt": ("왼쪽: 종이 더미 옆의 도둑 — 너무 오래 두면. 오른쪽: 불 옆에서 왕이 '작년 장부 어디 갔지?' — 너무 빨리 버리면", "Left: a thief beside a pile — keep too long. Right: the king beside a fire asking where last year\'s ledger went — throw away too soon"),
         "caption": ("너무 오래 둬도, 너무 빨리 버려도 안 돼요.", "Neither too long, nor too soon."),
         "small": ("오래 두면 도둑이 가져갈 게 많아지고, 빨리 버리면 세금 검사관이 물을 때 보여줄 게 없어요. 그래서 종이마다 날짜가 필요해요.", "Keep it too long and a thief has more to take; burn it too soon and there\'s nothing to show the tax inspector. So every paper needs a date.")},
        {"svg": P3, "hero": True, "alt": ("보관 기간표: 장터 공지 1달, 손님 명부 1년, 세금 장부 7년, 성문 열쇠 그림은 쓰는 동안만 — 그다음엔 불꽃. 서기가 새 종이에 7년 달력을 붙임", "A how-long-we-keep-it table: market notice 1 month, guest list 1 year, tax ledger 7 years, gate key drawing while in use — then a flame. A clerk pins a 7-year calendar to a new paper"),
         "caption": ("데이터 보존은 종이마다 태우는 날을 미리 정해두는 거예요.", "Data retention is deciding every paper\'s burning day in advance."),
         "small": ("종이를 만들 때 '얼마나 둘지'를 같이 적어요. 장터 공지는 한 달, 세금 장부는 7년. 날이 오면 태워요 — 아까워도, 잊었어도.", "The day a paper is born, write how long it stays. A month for a market notice, seven years for the tax ledger. When the day comes, burn it — even if you\'re fond of it, even if you forgot."),
         "tricks": (4, [
             (DATE_I, ("만들 때 날짜", "Date it at birth"), ("나중엔 아무도 몰라요", "later, nobody remembers"), "warm"),
             (LAW_I, ("법이 정한 건 그만큼", "As long as the law says"), ("세금 장부는 7년", "seven years for tax")),
             (BURN_I, ("날이 오면 태우기", "Burn on the day"), ("아까워도요", "even if you\'re fond of it"), "warm"),
             (COPY_I, ("사본까지", "Copies too"), ("여분 상자 것도 같이", "the spare chest copy as well"), "calm"),
         ])},
        {"svg": P4, "alt": ("태우는 날 달력. 초록 종이는 휴지통, 파랑은 찢기, 빨강은 태우기, 그리고 여분 상자의 사본에도 X", "A burning-day calendar. Green paper to the bin, blue torn, red burned, and an X on the copy in the spare chest too"),
         "caption": ("버리는 방법은 도장 색이 정해요.", "How it goes depends on the stamp."),
         "small": ('초록은 휴지통, 파랑은 찢기, 빨강은 태우기. <a href="backup-ko.html">여분 상자</a>에 남은 사본까지 같이 — 안 그러면 버린 게 아니에요.',
                   'Green to the bin, blue torn, red burned. The copy in the <a href="backup-en.html">spare chest</a> goes too — or it was never really gone.')},
        {"svg": P5, "alt": ("검사관이 '3년 전 세금 장부 좀 봅시다' — 서기가 '여기 있어요'. 옆 판자엔 '30년 전 손님 명부? — 없어요, 태웠어요. 도둑도 못 가져가요'", "An inspector asks for the tax ledger from three years ago — the clerk says here it is. A board beside reads: guest list from 30 years ago? gone, we burned it — so no thief can take it"),
         "caption": ("있어야 할 건 있고, 없어야 할 건 없어요.", "What should be there is there; what shouldn\'t, isn\'t."),
         "small": ('검사관이 물으면 꺼내 보여주고, 도둑이 와도 옛 명부는 없어요. <a href="dlp-ko.html">지킬 종이</a>가 줄면 지키기도 쉬워져요.',
                   'When the inspector asks, it\'s there to show; when a thief comes, the old lists are gone. Fewer <a href="dlp-en.html">papers to guard</a> means guarding gets easier.')},
    ],
    "summary": (("<b>데이터 보존</b> = 종이마다 <b>얼마나 둘지</b>를 만들 때 정하고, <b>날이 오면 사본까지 태우는</b> 약속. 있어야 할 건 있고, 없어야 할 건 없게.",
                 "<b>Data retention</b> = decide <b>how long each paper stays</b> the day it\'s born, and <b>burn it — copies too — when the day comes</b>. What should be there is; what shouldn\'t, isn\'t."),
                ("Data Retention. 데이터 종류마다 보관 기간을 정책으로 정하고, 법이 요구하는 만큼은 보관하되 기간이 끝나면 백업 사본까지 안전하게 폐기해요. 보관하는 데이터가 적을수록 유출 때 잃는 것도 적어요.",
                 "A policy that sets how long each kind of data is kept — as long as the law requires, no longer — then securely disposes of it, backups included. The less you keep, the less a breach can take.")),
    "glossary": [
        ("보존 정책", "Retention policy", ("보관 기간표.", "The how-long table."), ('종이 종류마다 얼마나 둘지. <a href="classification-ko.html">도장 색</a>과 짝이에요.', 'How long each kind of paper stays. Pairs with the <a href="classification-en.html">stamp color</a>.')),
        ("보존 기간", "Retention period", ("태우는 날까지의 날수.", "Days until burning day."), ("한 달, 1년, 7년, 쓰는 동안만.", "A month, a year, seven years, while in use.")),
        ("법정 보존", "Legal hold / statutory retention", ("법이 정한 그만큼.", "As long as the law says."), ("세금 장부 7년처럼 법이 정한 건 미리 못 태워요. 재판 중이면 태우는 날도 멈춰요.", "Some things, like a tax ledger for seven years, the law says to keep. A lawsuit pauses burning day.")),
        ("데이터 최소화", "Data minimization", ("애초에 적게 적기.", "Write less to begin with."), ("안 적은 종이는 지킬 필요도, 태울 필요도 없어요.", "A paper never written needs no guarding and no burning.")),
        ("안전한 폐기", "Secure disposal", ("찢기와 태우기.", "Tearing and burning."), ('휴지통에 버리는 것과 태우는 건 달라요. → <a href="classification-ko.html">종이마다 찍는 색 도장</a>', 'The bin and the fire are not the same. → <a href="classification-en.html">a colored stamp on every paper</a>')),
        ("백업 사본", "Backup copies", ("여분 상자 것까지.", "The spare chest copy too."), ('본체만 태우면 버린 게 아니에요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'Burning only the original means it isn\'t gone. → <a href="backup-en.html">the spare chest far away</a>')),
        ("감사", "Audit", ("검사관의 방문.", "The inspector\'s visit."), ('"3년 전 장부 보여주세요" — 있어야 해요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', '"Show me the ledger from three years ago" — it has to be there. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
        ("유출 범위", "Breach blast radius", ("도둑이 가져갈 수 있는 양.", "How much a thief could take."), ("태운 종이는 도둑도 못 가져가요. 적게 두면 적게 잃어요.", "A burned paper can\'t be stolen. Keep less, lose less.")),
    ],
}
