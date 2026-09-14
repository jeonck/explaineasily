from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
GOLD = "#E9B44C"
PAPER, PAPER_EDGE, INK = "#FFF8E7", "#C9A86A", "#142033"


def key(x, y, s=1.0, color=GOLD, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><circle r="11" fill="none" stroke="{color}" stroke-width="6"/>'
            f'<rect x="10" y="-3" width="44" height="6" fill="{color}"/><rect x="38" y="3" width="5" height="8" fill="{color}"/><rect x="48" y="3" width="5" height="11" fill="{color}"/></g>')


def nail(x, y):
    return f'<circle cx="{x}" cy="{y}" r="5" fill="var(--stone-dark)"/><circle cx="{x}" cy="{y}" r="2" fill="#0A1120"/>'


def sheet(x, y, w, h, title, rows=(), s=1.0):
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="{PAPER_EDGE}"/>'
           + label(w / 2, 18, title, 12, INK, cls="d"))
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, INK, "start")
    return out + "</g>"


def keybox(x, y, s=1.0, open_lid=False, slots=3):
    lid = (f'<path d="M-50 -30 h100 v-8 a50 14 0 0 0 -100 0z" fill="#5A3B22" transform="rotate(-30 -50 -30)"/>' if open_lid
           else f'<path d="M-50 -30 h100 v-8 a50 14 0 0 0 -100 0z" fill="#5A3B22"/>')
    cells = "".join(f'<rect x="{-42 + i * 28}" y="-22" width="24" height="44" rx="3" fill="#0A1120"/>' + label(-30 + i * 28, 12, str(i + 1), 10, "#F5E6B8") for i in range(slots)) if open_lid else \
        '<rect x="-10" y="-8" width="20" height="16" rx="3" fill="#E9B44C"/><path d="M-6 -8 v-6 a6 6 0 0 1 12 0 v6" stroke="#E9B44C" stroke-width="4" fill="none"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="-30" width="100" height="60" rx="4" fill="#8B5E3C"/>{lid}{cells}</g>'


def house(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="0" width="60" height="50" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-38 0 L0 -28 L38 0 Z" fill="var(--accent)"/><rect x="-8" y="24" width="16" height="26" fill="var(--night)"/></g>')


def door(x, y, s=1.0, locked=True):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><circle cx="20" cy="54" r="4" fill="{GOLD}"/>'
            f'<rect x="10" y="44" width="20" height="18" rx="3" fill="var(--night)"/></g>')


# 1. 목수가 편하려고 열쇠를 도면에 못으로 박아 둬요
P1 = svg(300, sky(300)
         + sheet(230, 40, 300, 200, "⟦창고 탑 도면|STOREHOUSE TOWER PLAN⟧", ("⟦1. 벽돌을 쌓는다|1. lay the bricks⟧", "⟦2. 창고 문을 연다 →|2. open the storeroom →⟧", "⟦3. 물건을 넣는다|3. put the goods in⟧"))
         + key(470, 112, 0.9, rot=-20) + nail(462, 104)
         + person(80, 110, s=0.85, face=SMILE, **BUILDER) + bubble(20, 30, 220, 34, "⟦매번 꺼내기 귀찮아서요|too much bother to fetch it every time⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦창고 열쇠를 도면에 못으로 박아 두면 편하긴 해요|nailing the storeroom key to the plan is convenient, sure⟧", 12, "var(--muted)"))

# 2. 도면은 복사돼 마을로 나가요 — 열쇠도 같이
COPIES = "".join(sheet(x, y, 90, 60, "⟦도면|PLAN⟧", (), 0.8) + key(x + 52, y + 40, 0.35, rot=-20) for x, y in ((330, 60), (450, 80), (560, 60)))
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + house(420, 170, 0.9) + house(520, 180, 0.8) + house(620, 170, 0.9) + label(520, 262, "⟦마을|the village⟧", 12, "var(--ink)")
         + sheet(60, 50, 150, 100, "⟦도면|PLAN⟧", ()) + key(180, 118, 0.6, rot=-20) + nail(174, 112)
         + '<path d="M215 100 L320 90" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M308 82 L322 90 L308 98" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + label(135, 180, "⟦한 장 그렸는데|drew one copy⟧", 12, "var(--ink)") + COPIES
         + person(240, 170, s=0.75, **THIEF) + key(300, 240, 0.7, rot=-20) + label(265, 282, "⟦도둑 손에도 열쇠가|the thief has a key too⟧", 12, "var(--bad)")
         + label(520, 40, "⟦도면은 복사돼 퍼져요 — 열쇠도 같이|plans get copied around — and the key goes with them⟧", 12, "var(--ink)", cls="d"))

# 3. 시크릿 관리 = 열쇠는 잠긴 상자에, 도면엔 칸 번호만 (hero)
P3 = svg(360, sky(360)
         + sheet(40, 40, 260, 180, "⟦창고 탑 도면|STOREHOUSE TOWER PLAN⟧", ("⟦1. 벽돌을 쌓는다|1. lay the bricks⟧", "⟦2. 열쇠 상자 3번 칸|2. key box, slot 3⟧", "⟦3. 물건을 넣는다|3. put the goods in⟧"))
         + '<rect x="52" y="94" width="200" height="26" rx="6" fill="none" stroke="var(--good)" stroke-width="2.5"/>'
         + label(170, 250, "⟦도면엔 열쇠 대신 칸 번호만|the plan names the slot, not the key⟧", 12, "var(--ink)")
         + keybox(480, 150, 1.4, open_lid=True) + key(516, 122, 0.9, rot=-90) + label(480, 240, "⟦잠긴 열쇠 상자|the locked key box⟧", 12, "var(--ink)")
         + person(630, 110, s=0.85, face=SMILE, **GUARD) + label(665, 240, "⟦경비가 열어 줘요|the guard opens it⟧", 11, "var(--muted)")
         + '<path d="M300 130 L400 140" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 5"/><path d="M388 132 L402 140 L388 148" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(380, 305, "⟦열쇠는 상자에, 도면엔 '3번 칸'이라고만 적어요|the key lives in the box — the plan just says slot 3⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦도면이 마을에 나가도 열쇠는 따라가지 않아요|the plan can travel — the key stays home⟧", 12, "var(--muted)"))

# 4. 자주 바꿔요 — 훔친 열쇠는 곧 안 맞아요
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 36, "⟦지난달 열쇠|last month\'s key⟧", 14, "var(--bad)", cls="d") + label(570, 36, "⟦이달 열쇠|this month\'s key⟧", 14, "var(--good)", cls="d")
         + door(150, 90) + person(220, 100, s=0.8, hat="var(--bad)", shirt="#2E3D57", face=MASK + SWEAT) + key(300, 150, 0.7, color="var(--stone-dark)", rot=-20)
         + '<path d="M120 60 l60 60 M180 60 l-60 60" stroke="var(--bad)" stroke-width="5" stroke-linecap="round" opacity="0.7"/>'
         + label(190, 235, "⟦훔친 열쇠가 안 맞아요|the stolen key does not fit⟧", 12, "var(--ink)")
         + door(520, 90) + person(590, 100, s=0.8, face=SMILE, **BUILDER) + key(660, 150, 0.7, rot=-20)
         + '<g transform="translate(400,60)"><rect width="70" height="60" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect width="70" height="14" rx="6" fill="var(--good)"/>' + label(35, 44, "⟦매달|monthly⟧", 12, "var(--ink)", cls="d") + "</g>"
         + label(570, 235, "⟦잠깐 빌리고, 다 쓰면 돌려줘요|borrow it briefly, give it back⟧", 12, "var(--ink)")
         + label(380, 292, "⟦열쇠를 자주 바꾸면, 훔친 열쇠는 금방 쓸모없어져요|change the key often, and a stolen one soon opens nothing⟧", 12, "var(--muted)"))

# 5. 경비는 도면에 열쇠가 박혀 있는지 늘 검사해요
P5 = svg(320, sky(320)
         + sheet(60, 50, 220, 150, "⟦새 도면|NEW PLAN⟧", ("⟦1. 벽돌을 쌓는다|1. lay the bricks⟧", "⟦2. 뒷문 열쇠 →|2. back door key →⟧")) + key(240, 120, 0.6, rot=-20) + nail(234, 114)
         + '<circle cx="240" cy="120" r="30" fill="none" stroke="var(--bad)" stroke-width="4"/>'
         + person(320, 90, s=0.85, face=EYES, **GUARD, extra='<g transform="translate(70,60)"><circle r="14" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M10 10 L22 22" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>')
         + bubble(400, 30, 300, 46, "⟦도면에 열쇠가 박혀 있어요! 상자로 옮기세요|a key is nailed to the plan! move it to the box⟧", 10, "var(--panel)", "var(--bad)", "left")
         + person(560, 130, s=0.8, face=FROWN + SWEAT, **BUILDER) + keybox(680, 190, 0.8)
         + label(380, 262, "⟦못 박힌 열쇠를 찾으면 종이 울려요|a nailed key sets off the bell⟧", 13, "var(--ink)", cls="d")
         + label(380, 296, "⟦벽돌 하나 쌓을 때마다, 자동으로|every time a brick is laid, automatically⟧", 12, "var(--muted)"))

BOX_I = icon('<rect x="10" y="24" width="44" height="30" rx="4" fill="#8B5E3C"/><path d="M10 24 h44 v-4 a22 8 0 0 0 -44 0z" fill="#5A3B22"/><rect x="26" y="34" width="12" height="12" rx="2" fill="#E9B44C"/><path d="M29 34 v-5 a3 3 0 0 1 6 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>')
BORROW_I = icon('<circle cx="18" cy="32" r="7" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="25" y="30" width="22" height="4" fill="#E9B44C"/><rect x="42" y="34" width="3" height="6" fill="#E9B44C"/><path d="M50 14 a18 18 0 0 1 8 18 M14 50 a18 18 0 0 1 -8 -18" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M54 26 l4 6 l-7 1z M10 38 l-4 -6 l7 -1z" fill="var(--good)"/>')
ROTATE_I = icon('<rect x="12" y="14" width="40" height="40" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="12" y="14" width="40" height="10" rx="6" fill="var(--good)"/><circle cx="26" cy="38" r="5" fill="none" stroke="#E9B44C" stroke-width="3"/><rect x="31" y="37" width="12" height="3" fill="#E9B44C"/>')
SLOT_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="#C9A86A"/><rect x="20" y="30" width="24" height="14" rx="3" fill="none" stroke="var(--good)" stroke-width="2"/><text x="32" y="41" text-anchor="middle" font-size="10" font-weight="700" fill="var(--good)">#3</text>')

PAGE = {
    "slug": "secrets", "order": 79,
    "title": ("열쇠를 벽에 못 박아 두지 않기", "Never Nail the Key to the Wall"),
    "h1": ("<em>시크릿 관리</em>가 뭐예요?", "What is <em>Secrets Management</em>?"),
    "sub": ("시크릿 관리(Secrets Management)를 목수가 도면에 못 박아 둔 창고 열쇠를 잠긴 상자로 옮기는 이야기로 풀어봤어요.",
            "Secrets management, told as a story about a storeroom key the builder nailed to the plan, and the locked box it moves into."),
    "panels": [
        {"svg": P1, "alt": ("목수가 웃으며 '매번 꺼내기 귀찮아서요'. 창고 탑 도면의 '창고 문을 연다' 줄 옆에 금색 열쇠가 못으로 박혀 있음", "The builder smiles: too much bother to fetch it every time. A golden key is nailed to the storehouse plan, right beside the line that says open the storeroom"),
         "caption": ("목수가 편하려고 열쇠를 도면에 못으로 박아 뒀어요.", "The builder nailed the key to the plan, to save himself the trip."),
         "small": ('<a href="patch-ko.html">목수</a>는 창고 문을 열 때마다 열쇠를 가지러 가기 싫었어요. 그래서 도면에 열쇠를 박아 뒀어요. 편하긴 해요.',
                   'The <a href="patch-en.html">builder</a> hated fetching the key every time he opened the storeroom. So he nailed it to the plan. Convenient, sure.')},
        {"svg": P2, "alt": ("도면 한 장이 화살표를 따라 마을로 가고, 집집마다 열쇠가 붙은 복사본이 있음. 도둑도 열쇠를 들고 있음", "One plan follows an arrow into the village; every house holds a copy with the key still on it. A thief holds a key too"),
         "caption": ("도면은 복사돼 마을로 나가요. 열쇠도 같이요.", "Plans get copied and go out to the village. The key goes with them."),
         "small": ("도면은 원래 여기저기 복사되는 거예요. 열쇠가 박힌 채로 복사되면, 마을 사람 모두가 창고 열쇠를 갖게 돼요.",
                   "Plans are meant to be copied around. Copy one with the key still on it, and the whole village has a storeroom key.")},
        {"svg": P3, "hero": True, "alt": ("도면의 둘째 줄이 '열쇠 상자 3번 칸'으로 바뀌어 초록 테두리. 옆엔 칸이 나뉜 열쇠 상자가 열려 있고 경비가 지킴", "The plan's second line now reads key box, slot 3, outlined in green. Beside it an open key box with numbered slots, and a guard keeping it"),
         "caption": ("시크릿 관리는 열쇠를 벽에 못 박아 두지 않는 거예요.", "Secrets management is never nailing the key to the wall."),
         "small": ("열쇠는 잠긴 상자에 넣어요. 도면엔 '열쇠 상자 3번 칸'이라고만 적어요. 필요할 때 경비에게 잠깐 빌리고, 자주 바꿔요.",
                   "The key goes in a locked box. The plan just says key box, slot 3. Borrow it from the guard when needed, and change it often."),
         "tricks": (4, [
             (BOX_I, ("잠긴 상자에", "In a locked box"), ("도면이 아니라 상자에", "the box, not the plan"), "warm"),
             (BORROW_I, ("잠깐 빌리기", "Borrow briefly"), ("쓰고 나면 돌려줘요", "give it back when done")),
             (ROTATE_I, ("자주 바꾸기", "Change it often"), ("훔쳐도 금방 안 맞아요", "a stolen one soon fails")),
             (SLOT_I, ("도면엔 칸 번호만", "Just the slot number"), ("'3번 칸'이라고만 적어요", "the plan says slot 3, nothing more"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 도둑이 지난달 회색 열쇠로 문을 열려 하지만 빨간 X. 오른쪽: 목수가 '매달' 달력 옆에서 이달 금색 열쇠를 잠깐 씀", "Left: a thief tries last month's grey key on the door — a red X. Right: the builder briefly uses this month's golden key beside a calendar reading monthly"),
         "caption": ("열쇠를 자주 바꾸면, 훔친 열쇠는 금방 쓸모없어져요.", "Change the key often, and a stolen one soon opens nothing."),
         "small": ('열쇠는 매달 새것으로 바꿔요. 목수는 <a href="pam-ko.html">잠깐 빌려 쓰고</a> 돌려줘요. 그래서 지난달 열쇠를 훔친 도둑은 문을 못 열어요.',
                   'The key is replaced every month. The builder <a href="pam-en.html">borrows it briefly</a> and returns it. So a thief holding last month\'s key opens nothing.')},
        {"svg": P5, "alt": ("돋보기를 든 경비가 새 도면에서 못 박힌 열쇠를 찾아 빨간 동그라미. '도면에 열쇠가 박혀 있어요! 상자로 옮기세요'. 목수가 땀 흘리며 열쇠 상자를 봄", "A guard with a magnifying glass finds a nailed key on a new plan, circled in red: there is a key nailed to the plan, move it to the box. The builder sweats and looks at the key box"),
         "caption": ("경비는 도면에 열쇠가 박혀 있는지 늘 검사해요.", "The guard always checks the plan for nailed keys."),
         "small": ('사람은 또 못을 박아요. 그래서 <a href="codescan-ko.html">도면 검사</a>가 열쇠 모양을 찾으면 종을 울려요. <a href="devsecops-ko.html">벽돌 하나 쌓을 때마다</a>, 자동으로요.',
                   'People will nail keys again. So the <a href="codescan-en.html">plan check</a> rings the bell whenever it spots a key shape — <a href="devsecops-en.html">every time a brick is laid</a>, automatically.')},
    ],
    "summary": (("<b>시크릿 관리</b> = 열쇠를 도면에 못 박지 않고 <b>잠긴 상자</b>에 두고, 필요할 때 <b>잠깐 빌리고</b>, <b>자주 바꾸고</b>, 도면엔 <b>칸 번호만</b> 적는 일.",
                 "<b>Secrets management</b> = keep the key in a <b>locked box</b> instead of nailed to the plan, <b>borrow it briefly</b>, <b>change it often</b>, and write only the <b>slot number</b> on the plan."),
                ("Secrets Management. 비밀번호, API 키, 토큰, 인증서 같은 시크릿을 코드에 하드코딩하지 않고 볼트에 보관해요. 코드는 이름으로 참조하고, 실행할 때 잠깐 받아 쓰고, 주기적으로 로테이션해요.",
                 "Secrets Management. Passwords, API keys, tokens, and certificates are kept in a vault instead of hardcoded. Code references them by name, receives them briefly at runtime, and they are rotated on a schedule.")),
    "glossary": [
        ("시크릿", "Secret", ("창고 열쇠.", "The storeroom key."), ('비밀번호, 입장권, 봉인 편지의 열쇠. 들키면 문이 열려요. → <a href="oauth-ko.html">열쇠 대신 입장권</a>', 'Passwords, tickets, the key to a sealed letter. Leak it and the door opens. → <a href="oauth-en.html">a ticket instead of a key</a>')),
        ("하드코딩", "Hardcoding", ("도면에 못 박기.", "Nailing it to the plan."), ("열쇠를 코드 안에 글자로 적어 두는 것. 편하지만 도면이 가는 곳마다 따라가요.", "Writing the key into the code as text. Convenient, but it goes wherever the code goes.")),
        ("볼트", "Vault", ("잠긴 열쇠 상자.", "The locked key box."), ('열쇠를 한곳에 모아 잠그고, 누가 언제 꺼냈는지 일지에 적어요. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'All keys locked in one place, with a log of who took which one when. → <a href="pam-en.html">the master key in the vault</a>')),
        ("로테이션", "Rotation", ("매달 새 열쇠.", "A new key every month."), ("정해진 때마다 열쇠를 바꿔요. 훔친 열쇠의 유통기한이 짧아져요.", "Change the key on a schedule. A stolen key expires fast.")),
        ("환경 변수", "Environment variable", ("일하러 갈 때 주머니에 넣어 주는 열쇠.", "The key slipped into your pocket for the shift."), ("도면(코드)엔 없고, 일 시작할 때만 잠깐 손에 쥐어요. 상자보다는 약해요.", "Not on the plan (code); handed over only when the job starts. Weaker than the box, but far better than a nail.")),
        ("시크릿 스캔", "Secret scanning", ("도면에서 열쇠 모양 찾기.", "Spotting key shapes on the plan."), ('열쇠처럼 생긴 글자 뭉치를 자동으로 찾아 종을 울려요. → <a href="codescan-ko.html">도면 검사와 두드려 보기</a>', 'Automatically finds strings shaped like keys and rings the bell. → <a href="codescan-en.html">reading the drawing and knocking on the wall</a>')),
        ("API 키 / 토큰", "API key / token", ("가게 입장권.", "The shop ticket."), ('한 가게에만 통하는 열쇠. 그래도 열쇠니까 상자에 둬요. → <a href="oauth-ko.html">열쇠 대신 입장권</a>', 'A key that opens one shop only. Still a key — keep it in the box. → <a href="oauth-en.html">a ticket instead of a key</a>')),
        ("최소 권한", "Least privilege", ("딱 그 문 열쇠만.", "Only the key to that one door."), ('창고 열쇠로 금고까지 열리면 안 돼요. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'The storeroom key must not open the vault too. → <a href="rbac-en.html">a key ring for every hat</a>')),
    ],
}
