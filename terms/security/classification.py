from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
MAID = dict(hat=None, shirt="#7B3FA0")
COOK = dict(hat="#FFF", shirt="#FFF")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
LEVELS = (("var(--good)", "⟦초록 · 누구나|GREEN · anyone⟧"), ("#5B8DEF", "⟦파랑 · 성 사람만|BLUE · castle only⟧"), ("var(--accent)", "⟦주황 · 몇 명만|ORANGE · a few⟧"), ("var(--bad)", "⟦빨강 · 왕과 둘|RED · the king and two⟧"))


def paper(x, y, s=1.0, stamp=None, rot=0, lines=3, text=None):
    st = f'<circle cx="18" cy="-14" r="9" fill="{stamp}"/>' if stamp else ""
    ln = "".join(f'<path d="M-18 {-8 + i * 9} h{28 - (i % 2) * 10}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for i in range(lines))
    tx = label(0, 24, text, 9, "#142033") if text else ""
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{ln}{st}{tx}</g>'


def chest(x, y, s=1.0, color="#8B5E3C", lock=False, open_lid=False):
    edge = "#5A3B22"
    lid = (f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}" transform="rotate(-35 -30 -14)"/>' if open_lid else f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}"/>')
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/>{lid}{lk}</g>'


def shelf(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="6" fill="{WOOD}"/><rect x="-40" y="-40" width="80" height="6" fill="{WOOD}"/><rect x="-42" y="-46" width="6" height="52" fill="{WOOD}"/><rect x="36" y="-46" width="6" height="52" fill="{WOOD}"/></g>'


def flame(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M0 -12 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/></g>'


# 1. 종이가 산더미 — 빵 레시피와 성문 열쇠 그림이 같은 상자에
P1 = svg(320, sky(320)
         + chest(200, 200, 1.4, open_lid=True)
         + paper(150, 130, 0.8, rot=-15, text="⟦빵 레시피|bread recipe⟧") + paper(215, 120, 0.8, rot=5, text="⟦식단표|menu⟧") + paper(275, 135, 0.8, rot=18, text="⟦성문 열쇠 그림|gate key drawing⟧")
         + paper(120, 70, 0.6, rot=-30) + paper(300, 60, 0.6, rot=25) + paper(240, 50, 0.6, rot=-5)
         + person(480, 130, s=0.85, face=EYES, **MAID) + paper(560, 160, 0.8, rot=10, text="⟦?|?⟧")
         + bubble(440, 40, 260, 34, "⟦이거 마을에 가져가도 돼요?|can I take this to the village?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(660, 160, s=0.7, face=FROWN + SWEAT, **GUARD) + label(680, 262, "⟦…글쎄요|…no idea⟧", 12, "var(--muted)")
         + label(380, 300, "⟦어떤 종이가 소중한지, 아무도 몰라요|nobody knows which papers matter⟧", 12, "var(--ink)"))

# 2. 다 똑같이 지키면 — 다 소중하면 아무것도 소중하지 않아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + chest(150, 170, 1.3, color="var(--stone)", lock=True) + "".join(paper(90 + i * 22, 90 - (i % 3) * 12, 0.5, rot=(i * 17) % 40 - 20) for i in range(7))
         + label(150, 250, "⟦빵 레시피까지 금고에|even the bread recipe in the vault⟧", 11, "var(--ink)") + label(150, 270, "⟦금고가 터져요|the vault overflows⟧", 10, "var(--muted)")
         + person(400, 90, s=0.8, face=FROWN + SWEAT, **COOK) + bubble(330, 30, 180, 34, "⟦금고 열쇠 좀요, 빵 굽게|vault key please, for the bread⟧", 10, "var(--panel)", "var(--line)", "bottom") + label(430, 250, "⟦하루 스무 번 금고 열기|opening the vault twenty times a day⟧", 10, "var(--muted)")
         + person(600, 120, s=0.8, face=MASK, extra=BAG) + paper(680, 160, 0.7, rot=15, text="⟦열쇠 그림|key drawing⟧") + label(640, 250, "⟦그 사이 진짜 소중한 건 밖으로|meanwhile the one that matters walks out⟧", 10, "var(--bad)")
         + label(380, 292, "⟦다 소중하면 아무것도 소중하지 않아요|when everything is precious, nothing is⟧", 12, "var(--ink)", cls="d"))

# 3. 네 가지 도장 (hero)
P3 = svg(360, sky(360)
         + "".join(f'<circle cx="{110 + i * 180}" cy="60" r="26" fill="{c}"/>' + label(110 + i * 180, 108, t, 12, "var(--ink)", cls="d") for i, (c, t) in enumerate(LEVELS))
         + paper(110, 180, 1.0, stamp="var(--good)", text="⟦장터 공지|market notice⟧") + paper(290, 180, 1.0, stamp="#5B8DEF", text="⟦이번 주 식단|this week\'s menu⟧") + paper(470, 180, 1.0, stamp="var(--accent)", text="⟦순찰 시간표|patrol times⟧") + paper(650, 180, 1.0, stamp="var(--bad)", text="⟦성문 열쇠 그림|gate key drawing⟧")
         + label(110, 250, "⟦마을 게시판에|on the village board⟧", 10, "var(--muted)") + label(290, 250, "⟦성 안 식당에|in the castle hall⟧", 10, "var(--muted)") + label(470, 250, "⟦경비실 상자에|in the guard room chest⟧", 10, "var(--muted)") + label(650, 250, "⟦왕의 금고에|in the king\'s vault⟧", 10, "var(--muted)")
         + person(380, 280, s=0.55, face=SMILE, **KING) + '<g transform="translate(430,318)"><rect x="-10" y="-6" width="20" height="12" rx="2" fill="var(--bad)"/><rect x="-3" y="-16" width="6" height="10" fill="#5A3B22"/></g>'
         + label(380, 350, "⟦종이를 만들 때 도장부터 찍어요 — 도장이 곧 규칙이에요|stamp it the moment it\'s written — the stamp is the rule⟧", 12, "var(--ink)", cls="d"))

# 4. 도장이 규칙을 정해요 (표)
ROWS = (("⟦어디 두나|where kept⟧", ("⟦선반|shelf⟧", "⟦선반|shelf⟧", "⟦잠긴 상자|locked chest⟧", "⟦금고|vault⟧")),
        ("⟦누가 보나|who reads⟧", ("⟦누구나|anyone⟧", "⟦성 사람|castle folk⟧", "⟦이름 적힌 몇 명|a named few⟧", "⟦왕 + 둘|king + two⟧")),
        ("⟦성 밖으로|leaves castle?⟧", ("⟦그냥|freely⟧", "⟦안 돼요|no⟧", "⟦봉인해서|sealed only⟧", "⟦절대|never⟧")),
        ("⟦버릴 때|when done⟧", ("⟦휴지통|bin⟧", "⟦찢기|tear⟧", "⟦잘게 찢기|shred⟧", "⟦태우기|burn⟧")))
P4 = svg(320, sky(320)
         + '<rect x="40" y="30" width="680" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="40" rx="8" fill="#C9A86A"/>'
         + "".join(f'<circle cx="{270 + i * 140}" cy="50" r="12" fill="{c}"/>' for i, (c, _) in enumerate(LEVELS))
         + "".join(f'<path d="M40 {70 + r * 48} h680" stroke="#C9A86A" stroke-width="1.5"/>' for r in range(1, 4))
         + "".join(label(120, 102 + r * 48, name, 12, "#142033", cls="d") + "".join(label(270 + i * 140, 102 + r * 48, v, 12, "#142033") for i, v in enumerate(vals)) for r, (name, vals) in enumerate(ROWS))
         + shelf(60, 300, 0.5) + chest(180, 300, 0.5, lock=True) + flame(700, 300, 0.7)
         + label(380, 300, "⟦도장 하나 보면 뭘 해야 할지 다 알아요|one look at the stamp tells you everything⟧", 12, "var(--ink)", cls="d"))

# 5. 도장 찍으면 다른 친구들이 움직여요
P5 = svg(300, sky(300)
         + paper(80, 120, 1.1, stamp="var(--bad)", text="⟦열쇠 그림|key drawing⟧") + "".join(f'<path d="M120 120 Q{200} {y} {x} {y}" stroke="var(--muted)" stroke-width="2.5" fill="none" stroke-dasharray="5 4"/>' for x, y in ((240, 60), (240, 150), (240, 240)))
         + person(250, 20, s=0.55, face=EYES, **GUARD) + '<path d="M300 60 l14 14 M314 60 l-14 14" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>' + label(400, 65, "⟦문지기: 빨간 종이는 성 밖으로 못 나가요|doorkeeper: red paper never leaves⟧", 11, "var(--ink)", "start")
         + '<g transform="translate(270,150)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="6" y="-2" width="20" height="4" fill="#E9B44C"/><rect x="20" y="2" width="3" height="5" fill="#E9B44C"/></g>' + label(400, 155, "⟦열쇠 꾸러미: 빨간 상자 열쇠는 셋뿐|key ring: only three keys to the red chest⟧", 11, "var(--ink)", "start")
         + '<g transform="translate(270,240)"><rect x="-22" y="-14" width="44" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle r="7" fill="var(--bad)"/></g>' + label(400, 245, "⟦봉인 편지: 보낼 땐 열쇠 없인 못 읽게|sealed letter: sent so no one can read without the key⟧", 11, "var(--ink)", "start")
         + label(380, 288, "⟦도장이 없으면 이 친구들은 뭘 지켜야 할지 몰라요|without the stamp, none of them know what to protect⟧", 12, "var(--muted)"))

STAMP_I = icon('<rect x="20" y="10" width="24" height="14" rx="3" fill="#5A3B22"/><rect x="28" y="24" width="8" height="10" fill="#5A3B22"/><rect x="14" y="34" width="36" height="8" rx="2" fill="#5A3B22"/><circle cx="32" cy="52" r="7" fill="var(--bad)"/>')
LEVELS_I = icon('<circle cx="14" cy="32" r="7" fill="var(--good)"/><circle cx="26" cy="32" r="7" fill="#5B8DEF"/><circle cx="38" cy="32" r="7" fill="var(--accent)"/><circle cx="50" cy="32" r="7" fill="var(--bad)"/>')
RULE_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h24" stroke="#C9A86A" stroke-width="2"/><path d="M12 27 h40 M12 37 h40" stroke="#C9A86A" stroke-width="1.5"/><circle cx="18" cy="17" r="3" fill="var(--bad)"/>')
OWNER_I = icon(f'<circle cx="32" cy="22" r="12" fill="{SKIN}"/><path d="M18 14 l4 -10 l5 6 l5 -8 l5 8 l5 -6 l4 10z" fill="#E9B44C"/><rect x="20" y="36" width="24" height="18" rx="5" fill="#7B3FA0"/>')

PAGE = {
    "slug": "classification", "order": 59,
    "title": ("종이마다 찍는 색 도장", "A Colored Stamp on Every Paper"),
    "h1": ("<em>데이터 분류</em>가 뭐예요?", "What is <em>Data Classification</em>?"),
    "sub": ("데이터 분류(Data Classification)를 성 안 모든 종이에 색 도장을 찍는 이야기로 풀어봤어요.",
            "Data classification, told as a story about putting a colored stamp on every paper in the castle."),
    "panels": [
        {"svg": P1, "alt": ("열린 상자에 빵 레시피, 식단표, 성문 열쇠 그림이 섞여 있음. 하녀가 '이거 마을에 가져가도 돼요?' 하고 경비는 땀 흘리며 '…글쎄요'", "An open chest with a bread recipe, a menu, and a gate key drawing all mixed together. A maid asks whether she can take a paper to the village; the guard sweats: no idea"),
         "caption": ("빵 레시피와 성문 열쇠 그림이 같은 상자에 있어요.", "The bread recipe and the gate key drawing sit in the same chest."),
         "small": ("어떤 종이가 소중한지 아무도 몰라요. 그러니 하녀가 물어봐도 경비는 대답을 못 해요.", "Nobody knows which papers matter. So when the maid asks, the guard has no answer.")},
        {"svg": P2, "alt": ("빵 레시피까지 금고에 넣어 금고가 넘치고, 요리사는 하루 스무 번 금고 열쇠를 빌리고, 그 사이 도둑은 열쇠 그림을 들고 나감", "Even the bread recipe goes in the vault, which overflows; the cook borrows the vault key twenty times a day; meanwhile a thief walks out with the key drawing"),
         "caption": ("그럼 다 금고에 넣을까요? 다 소중하면 아무것도 소중하지 않아요.", "Put everything in the vault, then? When everything is precious, nothing is."),
         "small": ("금고가 넘치고, 요리사는 빵 구울 때마다 금고 열쇠를 빌려요. 그러다 진짜 소중한 종이가 나가는 걸 아무도 못 봐요.", "The vault overflows, and the cook borrows the vault key every time she bakes. Then the one paper that truly matters walks out and nobody notices.")},
        {"svg": P3, "hero": True, "alt": ("도장 넷: 초록 누구나(장터 공지 → 마을 게시판), 파랑 성 사람만(식단 → 식당), 주황 몇 명만(순찰 시간표 → 경비실 상자), 빨강 왕과 둘(성문 열쇠 그림 → 왕의 금고). 왕이 도장을 듦", "Four stamps: green anyone (market notice → village board), blue castle only (menu → hall), orange a few (patrol times → guard room chest), red the king and two (gate key drawing → vault). The king holds a stamp"),
         "caption": ("데이터 분류는 종이마다 색 도장을 찍는 거예요.", "Data classification is putting a colored stamp on every paper."),
         "small": ("초록은 누구나, 파랑은 성 사람만, 주황은 몇 명만, 빨강은 왕과 둘. 종이를 만들 때 도장부터 찍어요 — 도장이 곧 규칙이에요.", "Green for anyone, blue for castle folk, orange for a few, red for the king and two. Stamp it the moment it\'s written — the stamp is the rule."),
         "tricks": (4, [
             (LEVELS_I, ("네 가지 색", "Four colors"), ("많으면 아무도 못 외워요", "more, and nobody remembers"), "calm"),
             (STAMP_I, ("만들 때 찍기", "Stamp at birth"), ("나중엔 산더미", "later it\'s a mountain"), "warm"),
             (RULE_I, ("도장 = 규칙", "Stamp = rule"), ("어디 두고 누가 보고", "where it goes, who reads")),
             (OWNER_I, ("찍는 사람", "Someone stamps"), ("종이 주인이 정해요", "the paper\'s owner decides")),
         ])},
        {"svg": P4, "alt": ("표: 네 색 도장별로 어디 두나(선반/선반/잠긴 상자/금고), 누가 보나(누구나/성 사람/몇 명/왕+둘), 성 밖으로(그냥/안 돼요/봉인해서/절대), 버릴 때(휴지통/찢기/잘게 찢기/태우기)", "A table by stamp color: where kept (shelf / shelf / locked chest / vault), who reads (anyone / castle folk / a named few / king + two), leaves the castle? (freely / no / sealed only / never), when done (bin / tear / shred / burn)"),
         "caption": ("도장 하나 보면 뭘 해야 할지 다 알아요.", "One look at the stamp tells you everything."),
         "small": ("어디 두는지, 누가 보는지, 성 밖으로 나가도 되는지, 다 쓰면 어떻게 버리는지. 하녀도 요리사도 물어볼 필요가 없어요.", "Where it\'s kept, who reads it, whether it may leave the castle, how to get rid of it when done. The maid and the cook never need to ask.")},
        {"svg": P5, "alt": ("빨간 도장 종이에서 점선 셋: 문지기가 성 밖으로 못 나가게 막고, 열쇠 꾸러미는 빨간 상자 열쇠를 셋만 주고, 봉인 편지로 보냄", "From a red-stamped paper, three dotted lines: the doorkeeper blocks it from leaving, the key ring gives only three keys to the red chest, and it is sent as a sealed letter"),
         "caption": ("도장이 찍히면 다른 친구들이 움직여요.", "Once it\'s stamped, the others know what to do."),
         "small": ('<a href="dlp-ko.html">문지기</a>는 빨간 종이를 막고, <a href="rbac-ko.html">열쇠 꾸러미</a>는 빨간 상자 열쇠를 셋만 주고, <a href="encryption-ko.html">봉인 편지</a>로만 보내요. 도장이 없으면 이 친구들은 뭘 지켜야 할지 몰라요.',
                   'The <a href="dlp-en.html">doorkeeper</a> stops red paper, the <a href="rbac-en.html">key ring</a> gives out only three keys to the red chest, and it travels only as a <a href="encryption-en.html">sealed letter</a>. Without the stamp, none of them know what to protect.')},
    ],
    "summary": (("<b>데이터 분류</b> = 성 안 모든 종이에 <b>네 가지 색 도장</b>을 만들 때 찍고, <b>도장이 곧 규칙</b>(어디 두고, 누가 보고, 밖으로 나가나, 어떻게 버리나)이 되게 하는 일.",
                 "<b>Data classification</b> = put <b>one of four colored stamps</b> on every paper as it\'s written, and let <b>the stamp be the rule</b> — where it\'s kept, who reads it, whether it leaves, how it\'s destroyed."),
                ("Data Classification. 데이터를 공개·내부·기밀·극비 같은 등급으로 나눠 라벨을 붙이고, 등급마다 보관·접근·전송·폐기 규칙을 정해요. DLP, 접근 통제, 암호화가 모두 이 라벨을 보고 움직여요.",
                 "Sorting data into levels like public, internal, confidential, and restricted, labeling it, and setting storage, access, transfer, and disposal rules per level. DLP, access control, and encryption all act on that label.")),
    "glossary": [
        ("분류 등급", "Classification levels", ("네 가지 색.", "The four colors."), ("공개 · 내부 · 기밀 · 극비. 셋이나 넷이면 충분해요 — 많으면 아무도 못 외워요.", "Public · internal · confidential · restricted. Three or four is enough; more, and nobody remembers.")),
        ("라벨링", "Labeling", ("도장 찍기.", "Stamping."), ("종이 위 도장. 요즘은 파일 이름 옆에 붙는 작은 표예요.", "The stamp on the paper. Today it\'s a small tag next to the file name.")),
        ("데이터 소유자", "Data owner", ("도장 찍는 사람.", "The one who stamps."), ("종이를 만든 사람이나 그 방 주인. 경비실이 대신 정해 주지 않아요.", "Whoever wrote the paper, or the owner of that room. The guard room doesn\'t decide for them.")),
        ("취급 규칙", "Handling rules", ("도장별 표.", "The table by color."), ("어디 두나, 누가 보나, 밖으로 나가나, 어떻게 버리나.", "Where kept, who reads, does it leave, how it\'s destroyed.")),
        ("DLP", "DLP", ("빨간 종이 문지기.", "The red-paper doorkeeper."), ('도장을 보고 성문에서 막아요. → <a href="dlp-ko.html">빨간 도장 찍힌 종이</a>', 'Reads the stamp and stops it at the gate. → <a href="dlp-en.html">the paper with the red stamp</a>')),
        ("접근 통제", "Access control", ("색깔별 열쇠.", "Keys by color."), ('빨간 상자 열쇠는 셋뿐. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'Only three keys to the red chest. → <a href="rbac-en.html">a key ring for every hat</a>')),
        ("암호화", "Encryption", ("봉인 편지.", "The sealed letter."), ('주황부터는 봉인해서만 보내요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'From orange up, it travels sealed. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("보존 · 폐기", "Retention & disposal", ("태우는 날.", "Burning day."), ("얼마나 두고, 다 쓰면 어떻게 없애나. 빨간 종이는 태워요.", "How long it stays, and how it goes when done. Red paper gets burned.")),
    ],
}
