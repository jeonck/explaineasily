from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
COOK = dict(hat="#FFF", shirt="#FFF")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GOLD = "#E9B44C"


def keyring(x, y, n, s=1.0):
    keys = "".join(f'<g transform="rotate({-30 + i * 30}) translate(0,26)"><rect x="-3" y="0" width="6" height="26" fill="{GOLD}"/><rect x="3" y="18" width="6" height="4" fill="{GOLD}"/><rect x="3" y="24" width="6" height="4" fill="{GOLD}"/></g>' for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="#C9822B" stroke-width="6"/>{keys}</g>'


def key(x, y, s=1.0, color=GOLD):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


def door(x, y, name, s=1.0, open_=False):
    body = ('<path d="M-36 0 L10 -14 V130 L-36 120 Z" fill="#5A3B22"/><rect x="-36" width="72" height="120" rx="3" fill="var(--night)" opacity="0.35"/>' if open_
            else f'<rect x="-36" width="72" height="120" rx="3" fill="{WOOD}"/><circle cx="24" cy="64" r="4" fill="{GOLD}"/>')
    return f'<g transform="translate({x},{y}) scale({s})">{body}{label(0, -10, name, 14, "var(--ink)")}</g>'


def padlock(x, y, s=1.0, color="var(--good)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-13" y="-8" width="26" height="20" rx="4" fill="{color}"/>'
            f'<path d="M-8 -8 V-14 a8 8 0 0 1 16 0 V-8" stroke="{color}" stroke-width="4" fill="none"/></g>')


def chest(x, y, s=1.0, color="#8B5E3C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>'
            f'<rect x="-7" y="-6" width="14" height="12" rx="2" fill="{GOLD}"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="{GOLD}" stroke-width="3" fill="none"/></g>')


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def tag(x, y, text):
    return (f'<g transform="translate({x},{y})"><rect width="96" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-10 13 l10 -8 v16z" fill="#C9A86A"/>{label(48, 17, text, 10, "#142033")}</g>')


DOORS = ("⟦부엌|Kitchen⟧", "⟦창고|Storeroom⟧", "⟦서재|Study⟧", "⟦금고|Vault⟧", "⟦성문|Gate⟧")

# 1. 요리사가 성 전체 열쇠 꾸러미를 들고 다녀요
P1 = svg(340, sky(340)
         + "".join(door(100 + i * 130, 40, n) for i, n in enumerate(DOORS))
         + person(150, 190, s=0.8, face=SMILE, **COOK) + keyring(250, 240, 9, 1.0)
         + bubble(330, 190, 250, 36, "⟦편하니까 다 들고 다녀요|it\'s easier to carry them all⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(455, 262, "⟦요리사인데 금고 열쇠도, 성문 열쇠도|a cook, with the vault key and the gate key too⟧", 11, "var(--muted)")
         + label(380, 322, "⟦하는 일은 부엌 하나, 열쇠는 성 전체|one job in the kitchen, keys to the whole castle⟧", 12, "var(--ink)", cls="d"))

# 2. 꾸러미를 잃어버리면 문이 다 열려요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(80, 90, s=0.8, face=FROWN + SWEAT, **COOK)
         + bubble(40, 30, 180, 34, "⟦어? 열쇠 꾸러미가…|huh? my key ring…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + keyring(200, 210, 9, 0.8)
         + person(280, 110, s=0.85, face=MASK, extra=BAG)
         + bubble(230, 20, 200, 34, "⟦오! 다 열리네|oh! they all open⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + door(470, 70, "⟦창고|Storeroom⟧", 0.8, open_=True) + door(570, 70, "⟦서재|Study⟧", 0.8, open_=True) + door(670, 70, "⟦금고|Vault⟧", 0.8, open_=True)
         + "".join(label(x, 190, "⟦열림|open⟧", 11, "var(--bad)", cls="d") for x in (470, 570, 670))
         + label(570, 225, "⟦꾸러미 하나 잃었는데 문이 다 열려요|one ring lost, and every door opens⟧", 12, "var(--bad)")
         + label(380, 300, "⟦들고 다니는 열쇠가 많을수록 잃을 것도 많아요|the more keys you carry, the more there is to lose⟧", 11, "var(--muted)"))

# 3. 최소 권한 = 딱 필요한 열쇠만 (hero)
P3 = svg(360, sky(360)
         + label(380, 60, "⟦하는 일에 딱 필요한 열쇠, 하나씩|exactly the key the job needs, one each⟧", 14, "var(--ink)", cls="d")
         + person(90, 120, s=0.85, face=SMILE, **COOK) + key(170, 175, 0.9) + label(130, 245, "⟦요리사: 부엌 열쇠|cook: kitchen key⟧", 11, "var(--ink)")
         + person(300, 120, s=0.85, face=SMILE, **CLERK) + key(380, 175, 0.9) + label(340, 245, "⟦서기: 서재 열쇠|clerk: study key⟧", 11, "var(--ink)")
         + person(510, 120, s=0.85, face=SMILE, **GUARD) + key(590, 175, 0.9) + label(550, 245, "⟦경비: 성문 열쇠|guard: gate key⟧", 11, "var(--ink)")
         + chest(690, 180, 1.2) + label(680, 245, "⟦금고 열쇠는 금고 속|vault key stays inside⟧", 11, "var(--muted)")
         + label(380, 310, "⟦필요한 것만, 필요할 때만, 안 쓰면 돌려주기|only what\'s needed, only when needed, returned when not⟧", 13, "var(--ink)", cls="d")
         + label(380, 344, "⟦열쇠가 적으면 잃어도 조금만 잃어요|fewer keys means losing less when you lose them⟧", 12, "var(--muted)"))

# 4. 잠깐 빌리는 열쇠, 달마다 열쇠 점검
P4 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + gatehouse(120, 70, 0.9) + person(200, 120, s=0.75, face=SMILE, **COOK) + key(280, 160, 0.9) + tag(300, 118, "⟦해 질 때까지|until sunset⟧")
         + label(190, 235, "⟦오늘만 창고 열쇠를 빌려요|borrowing the storeroom key, today only⟧", 11, "var(--ink)")
         + label(190, 257, "⟦해 지면 돌려줘요|back at sunset⟧", 11, "var(--muted)")
         + paper(430, 40, 290, 180, "⟦달마다 열쇠 점검|MONTHLY KEY CHECK⟧", ("⟦요리사 — 부엌 ✓|cook — kitchen ✓⟧", "⟦서기 — 서재 ✓|clerk — study ✓⟧", "⟦서기 — 창고: 안 쓴 지 석 달 ×|clerk — storeroom: unused 3 mo ×⟧", "⟦옛 경비 — 성문: 떠났음 ×|old guard — gate: gone ×⟧"))
         + label(575, 250, "⟦안 쓰는 열쇠는 거둬 가요|unused keys go back on the hook⟧", 11, "var(--ink)")
         + label(380, 300, "⟦잠깐 빌리고, 달마다 거둬요|borrow briefly, collect monthly⟧", 12, "var(--ink)", cls="d"))

# 5. 도둑이 얻는 건 딱 부엌 하나
P5 = svg(300, sky(300)
         + person(120, 110, s=0.85, face=MASK, extra=BAG) + key(200, 170, 0.9)
         + bubble(60, 30, 230, 40, "⟦요리사 열쇠 훔쳤다! …부엌?|got the cook\'s key! …the kitchen?⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + door(330, 70, "⟦부엌|Kitchen⟧", 0.8, open_=True) + label(330, 190, "⟦열림|open⟧", 11, "var(--bad)", cls="d")
         + door(450, 70, "⟦서재|Study⟧", 0.8) + padlock(450, 140) + label(450, 190, "⟦잠김|locked⟧", 11, "var(--good)", cls="d")
         + door(570, 70, "⟦금고|Vault⟧", 0.8) + padlock(570, 140) + label(570, 190, "⟦잠김|locked⟧", 11, "var(--good)", cls="d")
         + door(690, 70, "⟦성문|Gate⟧", 0.8) + padlock(690, 140) + label(690, 190, "⟦잠김|locked⟧", 11, "var(--good)", cls="d")
         + label(510, 225, "⟦도둑이 얻는 건 딱 부엌 하나|the thief gets exactly one kitchen⟧", 12, "var(--ink)", cls="d")
         + label(380, 285, "⟦잃어도 조금만 잃어요 — 그게 딱 필요한 열쇠만 주는 이유예요|lose a little, not everything — that\'s why only the needed keys⟧", 11, "var(--muted)"))

ONE_I = icon(f'<circle cx="20" cy="32" r="9" fill="none" stroke="{GOLD}" stroke-width="5"/><rect x="28" y="29" width="26" height="6" fill="{GOLD}"/><rect x="44" y="35" width="4" height="7" fill="{GOLD}"/><rect x="50" y="35" width="4" height="9" fill="{GOLD}"/>')
CLOCK_I = icon(f'<circle cx="26" cy="36" r="16" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M26 24 V36 L34 42" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="50" cy="16" r="5" fill="none" stroke="{GOLD}" stroke-width="3"/><rect x="53" y="14" width="8" height="4" fill="{GOLD}"/>')
HOOK_I = icon(f'<rect x="10" y="8" width="44" height="6" rx="3" fill="#5A3B22"/><path d="M20 14 v10 M44 14 v10" stroke="#5A3B22" stroke-width="3"/><circle cx="20" cy="30" r="6" fill="none" stroke="{GOLD}" stroke-width="3"/><rect x="18" y="35" width="4" height="16" fill="{GOLD}"/><path d="M44 32 v18 M38 44 l6 6 l6 -6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CHEST_I = icon(f'<rect x="10" y="26" width="44" height="28" rx="3" fill="#8B5E3C"/><path d="M10 26 h44 v-4 a22 9 0 0 0 -44 0z" fill="#5A3B22"/><rect x="27" y="34" width="10" height="9" rx="2" fill="{GOLD}"/><path d="M29 34 v-4 a3 3 0 0 1 6 0 v4" stroke="{GOLD}" stroke-width="2" fill="none"/>')

PAGE = {
    "slug": "leastprivilege", "order": 64,
    "title": ("딱 필요한 열쇠만", "Only the Keys You Need"),
    "h1": ("<em>최소 권한</em>이 뭐예요?", "What is <em>Least Privilege</em>?"),
    "sub": ("최소 권한 원칙(Least Privilege)을 성 사람마다 딱 필요한 열쇠만 주는 이야기로 풀어봤어요.",
            "The principle of least privilege, told as a story about giving everyone in the castle only the keys they need."),
    "panels": [
        {"svg": P1, "alt": ("부엌·창고·서재·금고·성문 문 다섯 개 앞에서 요리사가 열쇠 아홉 개짜리 꾸러미를 들고 '편하니까 다 들고 다녀요' 함", "In front of five doors — kitchen, storeroom, study, vault, gate — a cook holds a ring of nine keys and says it\'s easier to carry them all"),
         "caption": ("요리사가 성 전체 열쇠 꾸러미를 들고 다녀요.", "The cook carries the key ring for the whole castle."),
         "small": ("하는 일은 부엌 하나예요. 그런데 금고 열쇠도, 성문 열쇠도 같이 달려 있어요. 편하니까요.", "Her one job is the kitchen. But the vault key and the gate key hang on the same ring. It\'s just easier.")},
        {"svg": P2, "alt": ("요리사가 땀 흘리며 '어? 열쇠 꾸러미가…' 하고, 땅에 떨어진 꾸러미를 도둑이 주워 '오! 다 열리네'. 창고·서재·금고 문이 다 열려 있음", "The cook sweats — huh? my key ring… — while a thief picks it up off the ground: oh! they all open. The storeroom, study, and vault doors all stand open"),
         "caption": ("꾸러미를 잃어버리면 문이 다 열려요. 부엌만이 아니라 금고까지.", "Lose the ring and every door opens. Not just the kitchen — the vault too."),
         "small": ("도둑은 부엌 열쇠를 노린 게 아니에요. 그냥 떨어진 꾸러미를 주웠을 뿐인데, 그 안에 성 전체가 있었어요.", "The thief wasn\'t after the kitchen. He just picked up a dropped ring — and the whole castle was on it.")},
        {"svg": P3, "hero": True, "alt": ("요리사는 부엌 열쇠 하나, 서기는 서재 열쇠 하나, 경비는 성문 열쇠 하나씩 들고 있음. 금고 열쇠는 아무도 안 들고 잠긴 상자 속에 있음", "The cook holds one kitchen key, the clerk one study key, the guard one gate key. Nobody carries the vault key — it sits in a locked chest"),
         "caption": ("최소 권한은 하는 일에 딱 필요한 열쇠만 주는 거예요.", "Least privilege means giving only the keys the job needs."),
         "small": ("필요한 것만, 필요할 때만, 안 쓰면 돌려주기. 열쇠가 적으면 잃어도 조금만 잃어요.", "Only what\'s needed, only when needed, returned when not. Fewer keys means losing less when you lose them."),
         "tricks": (4, [
             (ONE_I, ("필요한 열쇠만", "Only the needed key"), ("요리사는 부엌 하나", "the cook gets the kitchen"), "calm"),
             (CLOCK_I, ("필요할 때만", "Only when needed"), ("잠깐 빌리고 돌려줘요", "borrow it, then give it back")),
             (HOOK_I, ("안 쓰면 회수", "Unused? take it back"), ("달마다 점검해요", "checked every month"), "warm"),
             (CHEST_I, ("금고 열쇠는 상자에", "The vault key stays boxed"), ("누구도 늘 들고 다니지 않아요", "no one carries it all day")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 요리사가 경비실에서 '해 질 때까지' 꼬리표가 달린 창고 열쇠를 빌림. 오른쪽: 달마다 열쇠 점검 장부 — 안 쓴 지 석 달 된 열쇠와 떠난 경비의 열쇠에 X", "Left: the cook borrows a storeroom key from the guardhouse, tagged until sunset. Right: a monthly key-check ledger — a key unused for three months and a departed guard\'s key both marked X"),
         "caption": ("오늘만 필요한 열쇠는 잠깐 빌려요. 그리고 달마다 안 쓰는 열쇠를 거둬요.", "A key needed only today is borrowed briefly. And every month, unused keys are collected."),
         "small": ('빌린 열쇠엔 "해 질 때까지" 꼬리표가 붙어요. 점검 장부엔 석 달 안 쓴 열쇠와 떠난 사람의 열쇠가 잡혀요. 열쇠는 늘 늘어나기만 하니까요.',
                   'A borrowed key wears a tag: until sunset. The ledger catches keys unused for three months and keys of people who left. Keys only ever pile up on their own.')},
        {"svg": P5, "alt": ("도둑이 요리사의 열쇠를 훔쳐 '…부엌?' 함. 부엌 문만 열리고 서재·금고·성문은 초록 자물쇠로 잠겨 있음", "A thief has stolen the cook\'s key: …the kitchen? Only the kitchen door opens; the study, vault, and gate stay locked with green padlocks"),
         "caption": ("도둑이 열쇠를 훔쳐도 얻는 건 딱 부엌 하나예요.", "Even if the thief steals the key, all he gets is one kitchen."),
         "small": ('열쇠를 <a href="rbac-ko.html">모자마다 꾸러미</a>로 나누고, 금고 열쇠는 <a href="pam-ko.html">금고 속 상자</a>에, 그리고 <a href="zerotrust-ko.html">문마다 다시 물어보면</a> 도둑은 갈 곳이 별로 없어요.',
                   'Split keys by <a href="rbac-en.html">hat</a>, keep the vault key in the <a href="pam-en.html">vault\'s own box</a>, and <a href="zerotrust-en.html">ask again at every door</a> — the thief has almost nowhere to go.')},
    ],
    "summary": (("<b>최소 권한</b> = 성 사람마다 <b>하는 일에 딱 필요한 열쇠만</b>, <b>필요할 때만</b> 주고, <b>안 쓰는 열쇠는 거두는</b> 원칙. 잃어도 조금만 잃게요.",
                 "<b>Least privilege</b> = give everyone <b>only the keys their job needs</b>, <b>only when needed</b>, and <b>take back the unused ones</b>. So that losing one loses little."),
                ("Principle of Least Privilege. 사용자·프로그램·계정에 업무에 꼭 필요한 최소한의 권한만 주는 원칙이에요. 과다 권한은 유출 때 피해를 키우고, 권한 상승 공격의 발판이 돼요. JIT 접근, 역할 기반 접근 제어, 정기 권한 검토가 이 원칙을 지키는 도구예요.",
                 "Give every user, program, and account only the minimum access its job requires. Excess privilege widens breach damage and gives privilege-escalation attacks a foothold. JIT access, role-based access control, and regular access reviews keep the principle alive.")),
    "glossary": [
        ("최소 권한 원칙", "Principle of least privilege", ("딱 필요한 열쇠만.", "Only the keys you need."), ("사람에게도, 프로그램에게도, 심부름꾼 계정에게도 똑같이 적용돼요.", "Applies the same to people, programs, and service accounts.")),
        ("권한 상승", "Privilege escalation", ("부엌 열쇠로 금고까지.", "From the kitchen key to the vault."), ("도둑이 작은 열쇠 하나로 시작해 더 큰 열쇠를 찾아가요. 열쇠가 적을수록 갈 곳이 없어요.", "A thief starts with one small key and hunts for bigger ones. Fewer keys, fewer places to go.")),
        ("과다 권한", "Over-privileged", ("필요보다 많은 열쇠.", "More keys than the job needs."), ("한 번 받은 열쇠는 아무도 돌려달라고 안 해요. 그래서 점검이 필요해요.", "Nobody asks for a key back once it\'s given. That\'s why the check exists.")),
        ("JIT 접근", "Just-in-time access", ("해 질 때까지 빌리는 열쇠.", "The key borrowed until sunset."), ('필요할 때 잠깐 받고 자동으로 돌려줘요. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'Granted briefly when needed, returned automatically. → <a href="pam-en.html">the master key in the vault</a>')),
        ("역할", "Role", ("모자마다 정해진 꾸러미.", "The ring that comes with the hat."), ('요리사 모자엔 부엌 열쇠만. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'The cook\'s hat comes with the kitchen key only. → <a href="rbac-en.html">a key ring for every hat</a>')),
        ("관리자 계정", "Admin account", ("성 전체 열쇠 꾸러미.", "The ring for the whole castle."), ("늘 들고 다니지 않아요. 고칠 때만 꺼내고, 평소엔 보통 열쇠로 다녀요.", "Never carried all day. Taken out only to fix things; the rest of the time, an ordinary key.")),
        ("권한 검토", "Access review", ("달마다 열쇠 점검.", "The monthly key check."), ('안 쓴 열쇠, 떠난 사람의 열쇠를 거둬요. → <a href="iam-ko.html">성의 명부 관리소</a>', 'Collects unused keys and the keys of people who left. → <a href="iam-en.html">the castle\'s registry office</a>')),
        ("제로 트러스트", "Zero Trust", ("문마다 다시 물어보기.", "Asking again at every door."), ('열쇠가 있어도 문마다 확인해요. 최소 권한과 짝이에요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'Even with a key, every door checks again. Least privilege\'s partner. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
    ],
}
