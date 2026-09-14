from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
CARP = dict(hat="#E9B44C", shirt="#4A5A72")
GUEST = dict(hat=None, shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
HAMMER = '<g transform="translate(58,60) rotate(30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#8B5E3C"/><rect x="-12" y="-8" width="24" height="12" rx="3" fill="var(--stone-dark)"/></g>'
REAL_ROWS = ("⟦철수 · 방 3 · 열쇠 12|Tom · room 3 · key 12⟧", "⟦영희 · 방 5 · 열쇠 7|Ann · room 5 · key 7⟧", "⟦민수 · 방 1 · 열쇠 9|Max · room 1 · key 9⟧")
TOKEN_ROWS = ("⟦#4821 · 방 3 · 열쇠 ★★|#4821 · room 3 · key ★★⟧", "⟦#0937 · 방 5 · 열쇠 ★★|#0937 · room 5 · key ★★⟧", "⟦#5512 · 방 1 · 열쇠 ★★|#5512 · room 1 · key ★★⟧")


def roster(x, y, w, h, title, rows, s=1.0, red=False):
    head = "var(--bad)" if red else "#C9A86A"
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="{head}"/>' + label(w / 2, 18, title, 12, "#142033" if not red else "#FFF", cls="d")
    for i, r in enumerate(rows):
        out += label(12, 50 + i * 24, r, 11, "#142033", "start")
    return out + "</g>"


def ticket(x, y, text, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-14" width="52" height="28" rx="4" fill="#FFF3D6" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 3"/>'
            f'{label(0, 4, text, 11, "#142033", cls="d")}</g>')


def dispenser(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-45" width="60" height="90" rx="8" fill="var(--accent)"/>'
            f'<rect x="-20" y="-30" width="40" height="8" rx="2" fill="var(--night)"/><circle cy="10" r="8" fill="#FFF3D6"/>{ticket(0, -46, "⟦#4821|#4821⟧", 0.8)}</g>')


def chest(x, y, s=1.0, lock=True):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def shed(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--stone-dark)"/>'
            f'<path d="M-48 0 L0 -34 L48 0 Z" fill="var(--stone)"/><rect x="-10" y="26" width="20" height="34" fill="var(--night)"/></g>')


def bars(x, y):
    return (f'<g transform="translate({x},{y})"><path d="M0 0 h130" stroke="var(--muted)" stroke-width="2"/>'
            + "".join(f'<rect x="{10 + i * 32}" y="{-h}" width="22" height="{h}" rx="3" fill="{c}"/>' for i, (h, c) in enumerate(((40, "var(--good)"), (70, "#5B8DEF"), (55, "var(--accent)"), (30, "var(--good)")))) + "</g>")


# 1. 목수가 연습용 명부를 달라고 해요 — 서기가 그대로 복사해 줘요
P1 = svg(300, sky(300)
         + roster(40, 50, 200, 130, "⟦손님 명부|GUEST ROSTER⟧", REAL_ROWS, red=True) + label(140, 205, "⟦진짜 명부|the real roster⟧", 11, "var(--muted)")
         + '<path d="M250 115 H300" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M293 109 l10 6 l-10 6z" fill="var(--muted)"/>'
         + roster(310, 50, 200, 130, "⟦손님 명부 (복사)|GUEST ROSTER (copy)⟧", REAL_ROWS, red=True) + label(410, 205, "⟦똑같이 복사|copied exactly⟧", 11, "var(--muted)")
         + person(600, 110, s=0.85, face=SMILE, extra=HAMMER, **CARP) + bubble(470, 30, 260, 34, "⟦연습용으로 명부 한 장만요!|one roster to practice on, please!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(640, 250, "⟦선반 만드는 연습|practicing a new shelf⟧", 11, "var(--muted)")
         + label(380, 290, "⟦진짜 이름이 그대로 연습 종이에 있어요|the real names are right there on the practice sheet⟧", 12, "var(--ink)"))

# 2. 연습 종이는 마을 작업장에 — 진짜가 새요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shed(120, 90, 1.0) + roster(165, 115, 60, 44, "⟦명부|roster⟧", (), 0.9, red=True) + label(150, 225, "⟦연습 종이는 마을 작업장에|the practice sheet sits in a village workshop⟧", 11, "var(--ink)")
         + person(360, 90, s=0.8, face=MASK, extra=BAG) + roster(420, 100, 70, 50, "⟦명부|roster⟧", (), 0.9, red=True) + label(400, 225, "⟦도둑이 주워요 — 이름·방·열쇠|a thief picks it up: name, room, key⟧", 11, "var(--bad)")
         + person(620, 100, s=0.8, face=FROWN, **GUEST) + bubble(540, 30, 200, 34, "⟦제 이름이 왜 마을에?|why is my name in the village?⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + label(650, 225, "⟦손님이 화나요|the guest is upset⟧", 11, "var(--ink)")
         + label(380, 280, "⟦연습용인데 진짜가 새요|it was only practice — and the real thing leaked⟧", 12, "var(--ink)", cls="d"))

# 3. 이름 대신 번호표 (hero)
P3 = svg(360, sky(360)
         + roster(30, 60, 200, 130, "⟦진짜 명부|THE REAL ROSTER⟧", REAL_ROWS, red=True)
         + '<path d="M240 125 H270" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M263 119 l10 6 l-10 6z" fill="var(--muted)"/>'
         + dispenser(310, 125) + label(310, 200, "⟦번호표 기계|the ticket machine⟧", 11, "var(--ink)")
         + '<path d="M350 125 H380" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M373 119 l10 6 l-10 6z" fill="var(--muted)"/>'
         + roster(390, 60, 210, 130, "⟦연습용 명부|PRACTICE ROSTER⟧", TOKEN_ROWS)
         + label(660, 62, "⟦번호↔이름 표는|number↔name list⟧", 11, "var(--ink)") + label(660, 80, "⟦잠긴 상자에|in a locked chest⟧", 11, "var(--ink)")
         + chest(660, 130, 1.3) + person(700, 165, s=0.5, face=SMILE, **KING) + label(650, 242, "⟦열쇠는 왕만|only the king has the key⟧", 10, "var(--muted)")
         + label(380, 300, "⟦이름은 번호표로, 열쇠 번호는 별로 가려요|names become numbers, key numbers become stars⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦연습엔 진짜 이름이 필요 없어요 — 상자는 성 안에 남아요|practice never needs the real name — the chest stays in the castle⟧", 12, "var(--muted)"))

# 4. 세 가지 방법 표
ROWS = (("⟦어떻게 보여요|looks like⟧", ("⟦철★★|T★★⟧", "⟦#4821|#4821⟧", "⟦ㅊ7ㅅ (섞임)|xq7 (scrambled)⟧")),
        ("⟦되돌릴 수 있나|can it be undone?⟧", ("⟦안 돼요|no⟧", "⟦상자 열쇠로만|only with the chest key⟧", "⟦절대 안 돼요|never⟧")),
        ("⟦언제 써요|use it when⟧", ("⟦화면에 보여줄 때|showing on a screen⟧", "⟦나중에 진짜가 필요할 때|the real name is needed later⟧", "⟦숫자 세기 · 통계|counting, statistics⟧")))
COLS = (("⟦가리기|MASK⟧", 300), ("⟦번호표|TOKEN⟧", 470), ("⟦섞기|SCRAMBLE⟧", 640))
P4 = svg(320, sky(320)
         + '<rect x="40" y="30" width="680" height="220" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="40" rx="8" fill="#C9A86A"/>'
         + "".join(label(x, 56, t, 13, "#142033", cls="d") for t, x in COLS)
         + "".join(f'<path d="M40 {70 + r * 60} h680" stroke="#C9A86A" stroke-width="1.5"/>' for r in range(1, 3))
         + "".join(label(130, 106 + r * 60, name, 12, "#142033", cls="d") + "".join(label(x, 106 + r * 60, v, 12, "#142033") for (_, x), v in zip(COLS, vals)) for r, (name, vals) in enumerate(ROWS))
         + label(380, 290, "⟦세 가지 다 '진짜 이름 없이 일하기'예요|all three mean working without the real name⟧", 12, "var(--ink)", cls="d"))

# 5. 연습도 통계도 되고, 도둑은 못 써요
P5 = svg(300, sky(300)
         + person(60, 90, s=0.8, face=SMILE, extra=HAMMER, **CARP) + ticket(150, 110, "⟦#4821|#4821⟧", 1.0, -10) + label(130, 240, "⟦연습은 돼요|practice works⟧", 12, "var(--ink)")
         + bars(310, 180) + label(380, 240, "⟦숫자 세기도 돼요|counting works too⟧", 12, "var(--ink)")
         + person(580, 90, s=0.8, face=MASK, extra=BAG) + ticket(670, 110, "⟦#4821|#4821⟧", 1.0, 10) + label(670, 80, "?", 26, "var(--bad)", cls="d")
         + label(630, 240, "⟦도둑은 못 써요|the thief can\'t use it⟧", 12, "var(--bad)")
         + label(380, 288, "⟦진짜 이름은 성 안 잠긴 상자에만 있어요|the real names exist only in the locked chest in the castle⟧", 12, "var(--ink)", cls="d"))

TOKEN_I = icon('<rect x="8" y="22" width="36" height="20" rx="4" fill="#FFF3D6" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/><text x="26" y="36" text-anchor="middle" font-size="11" font-weight="700" fill="#142033">#48</text><path d="M46 32 h10" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/>')
VAULT_I = icon('<rect x="10" y="26" width="44" height="28" rx="3" fill="#8B5E3C"/><path d="M10 26 h44 v-4 a22 10 0 0 0 -44 0z" fill="#5A3B22"/><rect x="27" y="34" width="10" height="10" rx="2" fill="#E9B44C"/><path d="M29 34 v-4 a3 3 0 0 1 6 0 v4" stroke="#E9B44C" stroke-width="2.5" fill="none"/>')
MASK_I = icon('<rect x="8" y="20" width="48" height="24" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="18" y="37" font-size="12" font-weight="700" fill="#142033">T</text><text x="27" y="37" font-size="12" font-weight="700" fill="var(--bad)">★★★</text>')
MIX_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--muted)" stroke-width="3"/><path d="M20 26 q6 -8 12 0 t12 0 M20 38 q6 8 12 0 t12 0" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M44 12 l8 8 M52 12 l-8 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "masking", "order": 83,
    "title": ("이름 대신 번호표", "A Number Instead of a Name"),
    "h1": ("<em>데이터 마스킹</em>이 뭐예요?", "What is <em>Data Masking</em>?"),
    "sub": ("데이터 마스킹·토큰화·가명처리(Data Masking, Tokenization, Pseudonymization)를 손님 명부의 이름을 번호표로 바꿔 주는 이야기로 풀어봤어요.",
            "Data masking, tokenization, and pseudonymization, told as a story about swapping the names on a guest roster for numbered tickets."),
    "panels": [
        {"svg": P1, "alt": ("빨간 머리띠의 진짜 손님 명부(철수·방 3·열쇠 12 …)가 그대로 복사되고, 망치 든 목수가 '연습용으로 명부 한 장만요!' 하고 웃음", "The real guest roster (Tom, room 3, key 12 …) is copied exactly; a carpenter with a hammer smiles: one roster to practice on, please!"),
         "caption": ("목수가 새 선반을 연습하려고 명부 한 장을 달라고 해요.", "The carpenter wants a roster to practice a new shelf on."),
         "small": ('서기는 진짜 명부를 그대로 복사해 줘요. 이름, 방 번호, 열쇠 번호까지 전부요. <a href="patch-ko.html">목수</a>는 그냥 연습만 하려는 건데요.', 'The clerk copies the real roster exactly — names, room numbers, key numbers, everything. The <a href="patch-en.html">carpenter</a> only wanted to practice.')},
        {"svg": P2, "alt": ("마을 작업장 옆에 명부, 도둑이 명부를 들고 감, 손님이 '제 이름이 왜 마을에?' 하고 찌푸림", "A roster beside a village workshop, a thief carrying it off, and a guest frowning: why is my name in the village?"),
         "caption": ("연습 종이는 마을 작업장에 있어요. 진짜가 새요.", "The practice sheet sits in a village workshop. The real thing leaks."),
         "small": ('연습용 종이는 성처럼 지키지 않아요. 도둑이 주우면 "철수는 방 3, 열쇠 12"를 알게 돼요. 연습이었는데 진짜 손님이 다쳐요.', 'Nobody guards a practice sheet like the castle. A thief who finds it learns "Tom, room 3, key 12." It was practice — and a real guest gets hurt.')},
        {"svg": P3, "hero": True, "alt": ("진짜 명부가 번호표 기계를 지나 연습용 명부가 됨: 철수 → #4821, 열쇠 12 → ★★. 번호↔이름 표는 잠긴 상자에, 열쇠는 왕만", "The real roster passes through a ticket machine and becomes a practice roster: Tom → #4821, key 12 → ★★. The number↔name list sits in a locked chest; only the king has the key"),
         "caption": ("데이터 마스킹은 이름 대신 번호표를 주는 거예요.", "Data masking is handing out a number instead of a name."),
         "small": ("이름은 번호표로 바꾸고, 열쇠 번호는 별로 가려요. 번호와 이름을 잇는 표는 잠긴 상자에 넣어요. 연습엔 진짜 이름이 필요 없어요.", "Names become numbers, key numbers become stars. The list that joins number to name goes in a locked chest. Practice never needs the real name."),
         "tricks": (4, [
             (TOKEN_I, ("이름 → 번호표", "Name → number"), ("되돌리려면 상자 열쇠가 필요해요", "undoing it takes the chest key"), "warm"),
             (VAULT_I, ("잠긴 상자", "The locked chest"), ("진짜 표는 성 안에만", "the real list never leaves")),
             (MASK_I, ("별로 가리기", "Stars over it"), ("일부만 보여줘요", "show only a part")),
             (MIX_I, ("섞어 버리기", "Scramble it"), ("되돌릴 수 없어요, 통계엔 충분", "can\'t be undone, fine for counting"), "calm"),
         ])},
        {"svg": P4, "alt": ("표: 가리기(철★★, 안 돼요, 화면에 보여줄 때), 번호표(#4821, 상자 열쇠로만, 나중에 진짜가 필요할 때), 섞기(섞임, 절대 안 돼요, 숫자 세기·통계)", "A table: mask (T★★, can\'t undo, showing on a screen), token (#4821, only with the chest key, real name needed later), scramble (scrambled, never, counting and statistics)"),
         "caption": ("가리기, 번호표, 섞기 — 되돌릴 수 있는지가 달라요.", "Mask, token, scramble — they differ in whether you can undo them."),
         "small": ("별로 가리면 화면에 보여줄 때 좋아요. 번호표는 상자 열쇠로 되돌릴 수 있어요. 섞어 버리면 아무도 못 되돌려요 — 숫자만 셀 때 써요.", "Stars are good for showing on a screen. A number can be undone with the chest key. Scrambled can never be undone — use it when you only need to count.")},
        {"svg": P5, "alt": ("목수는 #4821 표로 연습하고, 막대 그래프로 숫자를 세고, 도둑은 #4821 표를 들고 물음표", "The carpenter practices with a #4821 ticket, a bar chart counts numbers, and the thief holds a #4821 ticket with a question mark"),
         "caption": ("연습도 되고 숫자 세기도 되는데, 도둑은 못 써요.", "Practice works, counting works — and the thief gets nothing."),
         "small": ('그래도 번호표 옆에 "방 3, 12월 3일 온 손님"까지 다 적혀 있으면 누군지 알아챌 수 있어요. 어떤 종이에 번호표를 붙일지는 <a href="classification-ko.html">색 도장</a>이 정해요.',
                   'But if the ticket still says "room 3, arrived December 3rd," someone might work out who it is. Which papers get a number is decided by the <a href="classification-en.html">colored stamp</a>.')},
    ],
    "summary": (("<b>데이터 마스킹·토큰화</b> = 연습·통계용 종이에서 <b>이름 대신 번호표</b>를 주고, 일부는 <b>별로 가리고</b>, 번호↔이름 표는 <b>잠긴 상자</b>에 두는 일. 연습은 되고, 도둑은 못 써요.",
                 "<b>Data masking and tokenization</b> = on practice and statistics papers, hand out <b>a number instead of a name</b>, <b>cover parts with stars</b>, and keep the number↔name list in <b>a locked chest</b>. Practice works; the thief gets nothing."),
                ("Data Masking / Tokenization / Pseudonymization. 개인정보를 개발·테스트·분석 환경에 줄 때 실제 값을 토큰·부분 가림·비가역 변환으로 바꿔요. 토큰↔원본 매핑은 토큰 볼트에만 두고, 익명화는 되돌릴 수 없게 해요.",
                 "When personal data goes to dev, test, or analytics environments, real values are replaced by tokens, partial masks, or irreversible transforms. The token-to-original mapping lives only in a token vault; anonymization cannot be reversed.")),
    "glossary": [
        ("마스킹", "Masking", ("별로 가리기.", "Stars over it."), ("철★★, 열쇠 ★★. 일부만 보여주고 되돌리지 않아요. 화면에 띄울 때 많이 써요.", "T★★, key ★★. Show only a part, never undo. Common on screens.")),
        ("토큰화", "Tokenization", ("이름 → 번호표.", "Name → number."), ("진짜 값 대신 아무 뜻 없는 번호를 줘요. 번호만 봐선 아무것도 몰라요.", "A meaningless number stands in for the real value. The number alone tells you nothing.")),
        ("가명처리", "Pseudonymization", ("되돌릴 수 있는 번호표.", "A number you can undo."), ("번호↔이름 표가 어딘가에 있어서, 열쇠가 있으면 되돌려요. 그래서 표를 꼭 지켜야 해요.", "A number↔name list exists somewhere, so it can be undone with the key. Which is why the list must be guarded.")),
        ("익명화", "Anonymization", ("섞어 버리기.", "Scrambling it."), ("표도 없고 열쇠도 없어요. 아무도 못 되돌려요. 숫자만 셀 때 써요.", "No list, no key. Nobody can undo it. Use it when you only need to count.")),
        ("토큰 볼트", "Token vault", ("잠긴 상자.", "The locked chest."), ('번호↔이름 표를 두는 곳. 성 안에서 가장 잘 잠근 상자예요. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'Where the number↔name list lives. The best-locked chest in the castle. → <a href="pam-en.html">the master key in the vault</a>')),
        ("개인정보", "PII", ("손님 이름·방·열쇠.", "Guest name, room, key."), ("누군지 알아볼 수 있는 모든 것. 이름만이 아니라 방 번호와 날짜를 합쳐도 그래요.", "Anything that identifies someone. Not just a name — room number plus date can do it too.")),
        ("데이터 분류", "Data classification", ("어떤 종이에 번호표를.", "Which papers get a number."), ('색 도장이 빨강이면 번호표부터. → <a href="classification-ko.html">종이마다 찍는 색 도장</a>', 'A red stamp means numbers first. → <a href="classification-en.html">a colored stamp on every paper</a>')),
        ("암호화와 차이", "Versus encryption", ("봉인 편지는 열쇠로 다 읽혀요.", "A sealed letter opens fully with the key."), ('봉인 편지는 열쇠가 있으면 전부 읽혀요. 번호표는 아예 이름이 없어서 연습에 안전해요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'A sealed letter reads in full once you have the key. A number has no name in it at all, so practice stays safe. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
    ],
}
