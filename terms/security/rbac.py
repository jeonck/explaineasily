from _draw import *

COOK, CLERK, VISITOR = "#E9B44C", "#5B8DEF", "var(--stone-dark)"
ROLES = ((COOK, "⟦요리사|Cook⟧", ("⟦부엌|Kitchen⟧", "⟦창고|Storage⟧")),
         (CLERK, "⟦회계|Clerk⟧", ("⟦금고|Vault⟧", "⟦서재|Study⟧")),
         (VISITOR, "⟦손님|Guest⟧", ("⟦마당|Yard⟧",)))


def hat(x, y, color, s=1.0):
    return f'<path d="M6 22 Q30 -6 54 22 Z" fill="{color}" transform="translate({x - 30},{y - 22}) scale({s})"/>'


def keyring(x, y, n, s=1.0):
    keys = "".join(f'<g transform="rotate({-30 + i * 30}) translate(0,26)"><rect x="-3" y="0" width="6" height="26" fill="#E9B44C"/><rect x="3" y="18" width="6" height="4" fill="#E9B44C"/><rect x="3" y="24" width="6" height="4" fill="#E9B44C"/></g>' for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="#C9822B" stroke-width="6"/>{keys}</g>'


def door(x, y, name, s=1.0, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" width="72" height="120" rx="3" fill="{WOOD}"/><circle cx="24" cy="64" r="4" fill="#E9B44C"/>'
            f'{label(0, -10, name, 14, "var(--ink)")}{extra}</g>')


def namelist(n, crossed=()):
    rows = "".join(f'<rect x="8" y="{10 + i * 9}" width="{28 + (i * 7) % 12}" height="4" rx="2" fill="var(--line)"/>'
                   + (f'<path d="M6 {12 + i * 9} h40" stroke="var(--bad)" stroke-width="2"/>' if i in crossed else "") for i in range(n))
    return f'<rect x="-26" y="20" width="52" height="{20 + n * 9}" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><g transform="translate(-26,20)">{rows}</g>'


# 1. 방마다 이름 명단
P1 = svg(300, sky(300)
         + door(300, 70, "⟦부엌|Kitchen⟧", 1.0, namelist(8)) + door(430, 70, "⟦금고|Vault⟧", 1.0, namelist(6)) + door(560, 70, "⟦마당|Yard⟧", 1.0, namelist(9))
         + person(60, 100, hat="var(--good)", shirt="var(--good)", s=0.9, face=FROWN + SWEAT,
                  extra='<g transform="translate(64,70) rotate(-30)"><rect x="-4" y="-24" width="8" height="44" rx="2" fill="#E9B44C"/><path d="M-4 20 L0 30 L4 20 Z" fill="#E8C9A8"/></g>')
         + label(120, 260, "⟦새 사람이 오면 문 스무 개를 고쳐요|a new hire means fixing twenty doors⟧", 13, "var(--muted)"))

# 2. 나간 사람이 명단에 남는다
P2 = svg(270, '<rect width="760" height="270" fill="var(--bad-soft)"/>'
         + door(300, 50, "⟦부엌|Kitchen⟧", 1.0, namelist(6))
         + label(300, 215, "⟦'김요리'가 아직 있어요|'Kim the cook' is still on it⟧", 13, "var(--bad)")
         + person(520, 90, hat=COOK, shirt="#4A5A72", s=0.9, face=SMILE,
                  extra='<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>')
         + bubble(520, 30, 150, 34, "⟦저 그만뒀는데요|I quit last month⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + '<path d="M620 200 L690 200" stroke="var(--muted)" stroke-width="3"/><path d="M680 190 L692 200 L680 210" stroke="var(--muted)" stroke-width="3" fill="none"/>')

# 3. RBAC = 모자마다 열쇠 꾸러미 (hero)
ROWS = ""
for i, (color, name, rooms) in enumerate(ROLES):
    y = 60 + i * 90
    ROWS += (hat(90, y + 10, color, 1.3) + label(90, y + 40, name, 14, "var(--ink)")
             + '<path d="M150 %d L200 %d" stroke="var(--muted)" stroke-width="3"/><path d="M190 %d L202 %d L190 %d" stroke="var(--muted)" stroke-width="3" fill="none"/>' % (y, y, y - 10, y, y + 10)
             + keyring(250, y, len(rooms), 0.9)
             + "".join(door(340 + j * 90, y - 36, r, 0.55) for j, r in enumerate(rooms)))
PEOPLE = "".join(person(540 + i * 70, 200, hat=c, shirt="#4A5A72", s=0.6, face=SMILE) for i, c in enumerate((COOK, COOK, CLERK)))
P3 = svg(340, '<rect width="760" height="340" fill="var(--panel)"/>' + ROWS + PEOPLE
         + label(630, 300, "⟦사람에겐 모자만|people just get a hat⟧", 13, "var(--muted)"))

# 4. 사람이 바뀌면 모자만
P4 = svg(280, sky(280)
         + person(60, 100, hat=None, shirt="#4A5A72", s=0.9, face=SMILE) + label(90, 250, "⟦나가는 요리사|the old cook⟧", 12, "var(--muted)")
         + hat(200, 120, COOK, 1.4) + '<path d="M240 120 L300 120" stroke="var(--accent)" stroke-width="3"/><path d="M290 110 L302 120 L290 130" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + person(320, 100, hat=COOK, shirt="#4A5A72", s=0.9, face=SMILE) + label(350, 250, "⟦새 요리사|the new cook⟧", 12, "var(--muted)")
         + door(520, 60, "⟦부엌|Kitchen⟧", 0.8, '<path d="M-12 60 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
         + door(620, 60, "⟦창고|Storage⟧", 0.8, '<path d="M-12 60 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
         + label(570, 250, "⟦문은 그대로|the doors don\'t change⟧", 13, "var(--good)"))

# 5. 모자가 자꾸 는다
PILE = "".join(hat(90 + (i % 5) * 26, 200 - (i // 5) * 14, c, 0.7) for i, c in enumerate((COOK, CLERK, VISITOR, "var(--accent)", "var(--good)") * 5))
FAT_HAT = hat(380, 140, CLERK, 2.0) + keyring(380, 190, 9, 0.9)
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>' + PILE
         + label(140, 250, "⟦모자 백 개|a hundred hats⟧", 13, "var(--muted)")
         + FAT_HAT + label(380, 255, "⟦열쇠가 자꾸 늘어요|keys keep piling on⟧", 13, "var(--muted)")
         + '<g transform="translate(600,120)"><circle r="30" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -18 V0 L12 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(600, 180, "⟦'요리사인데 밤에만'?|'cook, but only at night'?⟧", 13, "var(--ink)")
         + label(600, 200, "?", 30, "var(--accent)", cls="d")
         + label(600, 255, "⟦모자로는 못 적어요|a hat can\'t say that⟧", 13, "var(--muted)"))

HAT_I = icon(f'<path d="M8 40 Q32 6 56 40 Z" fill="{COOK}"/><rect x="6" y="40" width="52" height="6" rx="3" fill="{COOK}"/>')
KEYS_I = icon('<circle cx="32" cy="24" r="10" fill="none" stroke="#C9822B" stroke-width="4"/><rect x="18" y="32" width="5" height="22" fill="#E9B44C"/><rect x="30" y="32" width="5" height="22" fill="#E9B44C"/><rect x="42" y="32" width="5" height="22" fill="#E9B44C"/>')
PERSON_I = icon('<circle cx="32" cy="22" r="10" fill="var(--good)"/><rect x="18" y="36" width="28" height="20" rx="8" fill="var(--good)"/>')

PAGE = {
    "slug": "rbac", "order": 17,
    "title": ("모자마다 열쇠 꾸러미", "A Key Ring for Every Hat"),
    "h1": ("<em>RBAC</em>이 뭐예요?", "What is <em>RBAC</em>?"),
    "sub": ("역할 기반 접근 제어(Role-Based Access Control)를 모자와 열쇠 꾸러미 이야기로 풀어봤어요.",
            "Role-Based Access Control, told as a story about hats and key rings."),
    "panels": [
        {"svg": P1, "alt": ("부엌, 금고, 마당 문마다 긴 이름 명단이 붙어 있고, 경비가 연필을 들고 땀을 흘림", "Long name lists hang on the Kitchen, Vault and Yard doors; a guard with a pencil sweats"),
         "caption": ("방마다 이름 명단을 붙였어요.", "Every door had a list of names."),
         "small": ("새 사람이 오면 문 스무 개를 다 고쳐야 해요.", "A new person means fixing twenty lists.")},
        {"svg": P2, "alt": ("부엌 문 명단에 '김요리'가 남아 있는데, 가방을 든 요리사는 '저 그만뒀는데요' 하며 나감", "The kitchen list still shows 'Kim the cook' while the cook walks away with a bag saying I quit"),
         "caption": ("나간 사람이 명단에 남아요.", "People who left stay on the list."),
         "small": ("고치는 걸 잊으면, 그만둔 요리사 이름이 부엌 문에 그대로.", "Forget one list, and a cook who quit can still open the kitchen.")},
        {"svg": P3, "hero": True, "alt": ("요리사·회계·손님 모자 옆에 각각 열쇠 꾸러미와 열 수 있는 문이 그려져 있고, 사람들은 모자만 쓰고 있음", "Cook, Clerk and Guest hats each beside a key ring and the doors it opens; people simply wear the hats"),
         "caption": ("RBAC은 모자마다 열쇠 꾸러미를 정해요.", "RBAC gives each hat its own key ring."),
         "small": ("열쇠는 사람이 아니라 모자에 달려 있어요. 사람에겐 모자만 씌워요.", "Keys hang on the hat, not the person. People just get a hat."),
         "tricks": (3, [
             (HAT_I, ("모자 = 역할", "Hat = role"), ("요리사, 회계, 손님", "cook, clerk, guest"), "warm"),
             (KEYS_I, ("열쇠 꾸러미 = 권한", "Key ring = permissions"), ("그 모자가 여는 문들", "the doors that hat opens"), "calm"),
             (PERSON_I, ("사람 = 모자를 받아요", "Person = gets a hat"), ("한 사람이 모자 둘도 돼요", "one person can wear two")),
         ])},
        {"svg": P4, "alt": ("나가는 요리사가 모자를 벗어 새 요리사에게 건네고, 부엌·창고 문엔 체크 표시", "The old cook hands the hat to the new cook; the Kitchen and Storage doors show a check"),
         "caption": ("사람이 바뀌면 모자만 바꿔 써요.", "When people change, only the hat moves."),
         "small": ("문 스무 개는 그대로. 모자 하나 옮기면 끝.", "Twenty doors untouched. Move one hat, done.")},
        {"svg": P5, "alt": ("모자 더미, 열쇠가 잔뜩 달린 뚱뚱한 모자, 그리고 시계 옆에 '요리사인데 밤에만?' 물음표", "A pile of hats, a fat hat loaded with keys, and a clock beside 'cook, but only at night?'"),
         "caption": ("모자가 자꾸 늘어요.", "The hats keep multiplying."),
         "small": ("'요리사인데 밤에만', '손님 있을 때만'… 모자로 다 만들면 백 개. 그런 조건은 다른 방법(ABAC)이 맡아요. 그리고 모자에 열쇠를 더하기만 하고 빼는 사람은 없어요.", "'Cook, but only at night', 'only while guests are in'… make a hat for each and you have a hundred. Conditions like that need another method (ABAC). And keys get added to hats far more often than removed.")},
    ],
    "summary": (("<b>RBAC</b> = 사람이 아니라 <b>모자(역할)</b>에 열쇠를 주고, 사람에겐 <b>모자만</b> 씌우는 것.",
                 "<b>RBAC</b> = keys go on the <b>hat (role)</b>, not the person; people just <b>wear a hat</b>."),
                ("Role-Based Access Control. 1992년 미국 NIST의 Ferraiolo와 Kuhn이 정리했고, 회사 시스템 대부분이 이 방식이에요. '방 하나 열쇠'(최소 권한)를 실제로 만드는 도구예요.",
                 "Role-Based Access Control. Written up by Ferraiolo and Kuhn at NIST in 1992; most company systems work this way. It's how 'one key, one room' (least privilege) gets built in practice.")),
    "glossary": [
        ("역할", "Role", ("모자.", "The hat."), ("요리사, 회계, 손님 같은 일의 이름. 사람 이름이 아니에요.", "A name for a job — cook, clerk, guest — never a person's name.")),
        ("권한", "Permission", ("열쇠 하나.", "One key."), ('"부엌 문 열기"처럼 딱 하나의 일.', 'One single thing, like "open the kitchen door".')),
        ("할당", "Assignment", ("모자 씌우기.", "Handing out a hat."), ("사람과 모자를 잇는 것. 빼는 것도 여기서.", "Linking a person to a hat — and unlinking them.")),
        ("최소 권한", "Least privilege", ("꼭 필요한 열쇠만.", "Only the keys you need."), ('<a href="zerotrust-ko.html">문마다 물어보는 성</a>에서 본 "방 하나 열쇠".', 'The "one key, one room" from the <a href="zerotrust-en.html">castle that always asks</a>.')),
        ("역할 폭발", "Role explosion", ("모자 백 개.", "A hundred hats."), ("조건마다 모자를 만들다 보면 아무도 못 외워요.", "Make a hat for every condition and nobody can keep track.")),
        ("권한 비대", "Privilege creep", ("자꾸 무거워지는 모자.", "The hat that keeps getting heavier."), ("열쇠를 더하긴 쉬운데 빼는 사람이 없어요.", "Adding keys is easy; nobody ever takes one off.")),
        ("ABAC", "ABAC", ("모자 대신 조건.", "Conditions instead of hats."), ('"요리사이고, 낮이고, 손님이 없으면" 같은 문장으로 문을 열어요.', 'Opens doors by sentences like "is a cook, it\'s daytime, no guests inside".')),
        ("접근 검토", "Access review", ("모자 점검 날.", "Hat inspection day."), ("분기마다 누가 무슨 모자를 쓰고 있는지 다시 봐요.", "Every quarter, check who's wearing which hat.")),
    ],
}
