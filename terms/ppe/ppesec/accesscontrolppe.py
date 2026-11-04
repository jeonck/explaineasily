from _draw import *

OWNER = dict(hat=None, shirt="#4A7A6A", face=SMILE)
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")


def keyring(x, y, n=2, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="#E9B44C" stroke-width="3"/>'
    for i in range(n):
        out += f'<rect x="{6 + i * 10}" y="4" width="6" height="16" rx="2" fill="#E9B44C"/>'
    return out + "</g>"


def doorrow(x, y, labels, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i, t in enumerate(labels):
        out += f'<rect x="{i * 70}" y="0" width="54" height="74" rx="3" fill="#8B5E3C"/><circle cx="{i * 70 + 42}" cy="40" r="4" fill="#E9B44C"/>' + label(i * 70 + 27, -8, t, 10, "var(--muted)")
    return out + "</g>"


# 1. 방마다 열쇠를 주는 규칙이 제각각
P1 = svg(340, sky(340)
         + doorrow(100, 120, ("⟦①|①⟧", "⟦②|②⟧", "⟦③|③⟧"))
         + person(130, 230, s=0.6, **OWNER) + label(130, 310, "⟦방 주인이 자기 방 열쇠를 마음대로 줘요|the owner gives his room's key to anyone he likes⟧", 10, "var(--muted)")
         + person(370, 230, s=0.6, **KING) + label(370, 310, "⟦왕의 등급표대로만 들어가요|the king's rank-list decides who enters⟧", 10, "var(--muted)")
         + person(600, 230, s=0.6, **GUARD) + label(600, 310, "⟦모자(역할)마다 열쇠 꾸러미|a key ring for each hat (role)⟧", 10, "var(--muted)")
         + label(380, 40, "⟦방마다 열쇠 주는 규칙이 제각각이에요|every room decides who gets a key by a different rule⟧", 13, "var(--ink)", cls="d"))

# 2. 규칙을 안 정하면 섞여서 사고가 나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 140, s=0.85, face=FROWN + SWEAT, **CLERK)
         + bubble(60, 40, 320, 44, "⟦방 주인이 맘대로 열쇠를 줬는데, 왕의 비밀 방 열쇠였어요|the owner gave out a key — to the king's secret room⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=EYES, **KING)
         + bubble(415, 70, 300, 40, "⟦이 방이 어떤 규칙을 따를지, 아무도 안 정했어요|nobody had decided which rule this room should follow⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦방마다 어떤 규칙을 쓸지 먼저 정해야 해요 — 그 규칙이 DAC·MAC·RBAC예요|decide per room which rule applies first — the rules are DAC, MAC and RBAC⟧", 11, "var(--ink)", cls="d"))

# 3. 세 가지 모델 (hero)
COLS = ((130, "⟦DAC|DAC⟧", "⟦방 주인이 직접 정해요|the room's owner decides⟧", OWNER),
        (380, "⟦MAC|MAC⟧", "⟦왕의 등급표, 주인도 못 바꿔요|the king's rank-list — even the owner can't override it⟧", KING),
        (630, "⟦RBAC|RBAC⟧", "⟦모자(역할)에 열쇠를 줘요|keys go to the hat (role)⟧", GUARD))
P3 = svg(340, sky(340)
         + "".join(person(x - 30, 60, s=0.7, **p) + label(x, 170, t, 15, "var(--ink)", cls="d") + label(x, 196, sub, 10, "var(--muted)") for x, t, sub, p in COLS)
         + keyring(130, 210) + keyring(380, 210, 1) + keyring(630, 210, 3)
         + '<path d="M230 110 V110" stroke="none"/><path d="M250 110 h50 M500 110 h50" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(380, 320, "⟦접근통제 모델 = 열쇠 결정권을 누구에게 둘지 정한 규칙|an access-control model = a rule for who gets to decide who holds the keys⟧", 13, "var(--ink)", cls="d"))

OWNER_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="24" r="7" fill="var(--good)"/><path d="M20 44 q12 -12 24 0" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LABEL_I = icon('<path d="M14 14 h26 l16 18 l-16 18 h-26 z" fill="none" stroke="#E9B44C" stroke-width="3"/><circle cx="24" cy="32" r="3" fill="#E9B44C"/>')
HAT_I = icon('<path d="M10 40 Q32 16 54 40 Z" fill="var(--good)"/><rect x="16" y="40" width="32" height="10" rx="3" fill="var(--good)"/>')
MIX_I = icon('<circle cx="22" cy="32" r="12" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><circle cx="42" cy="32" r="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>')

PAGE = {
    "slug": "accesscontrolppe", "order": 14,
    "title": ("열쇠 주인을 정하는 세 가지 방식", "Three Ways to Decide Who Holds the Key"),
    "h1": ("<em>접근통제 모델</em>이 뭐예요?", "What are <em>Access Control Models</em>?"),
    "sub": ("접근통제 모델(DAC·MAC·RBAC)을, 성의 방마다 열쇠를 누가 정하는지 다른 세 가지 규칙 이야기로 풀어봤어요.",
            "Access control models — DAC, MAC, RBAC — told as a story about three different rules for who decides a room's key."),
    "panels": [
        {"svg": P1, "alt": ("세 개의 방 앞에 방 주인, 왕, 경비가 각자 다른 규칙으로 열쇠를 나눠줌", "In front of three rooms, an owner, a king and a guard each hand out keys by a different rule"),
         "caption": ("방마다 열쇠 주는 규칙이 제각각이에요.", "Every room decides who gets a key by a different rule."),
         "small": ("어떤 방은 주인 맘대로, 어떤 방은 왕의 등급표대로, 어떤 방은 역할(모자)대로예요.", "Some rooms let the owner choose, some follow the king's rank-list, some follow the hat (role).")},
        {"svg": P2, "alt": ("서기가 땀 흘리며 방 주인이 왕의 비밀 방 열쇠를 함부로 줬다고 말하고, 왕은 어느 규칙을 따라야 했는지 아무도 정하지 않았다고 말함", "A sweating clerk says the owner handed out a key to the king's secret room on his own, and the king says nobody had decided which rule that room should follow"),
         "caption": ("방마다 쓸 규칙을 안 정하면 규칙이 섞여 사고가 나요.", "Leave a room's rule undecided, and the rules collide into an accident."),
         "small": ("방 주인이 맘대로 열쇠를 줬는데 알고 보니 왕의 비밀 방 열쇠였어요. 방마다 어떤 규칙을 쓸지 먼저 정해야 해요.", "The owner freely handed out a key — to what turned out to be the king's secret room. Each room's rule has to be decided first.")},
        {"svg": P3, "hero": True, "alt": ("DAC는 방 주인이 직접 정하고, MAC는 왕의 등급표를 따르고, RBAC는 모자(역할)에 열쇠 꾸러미를 줌", "DAC: the owner decides directly. MAC: everyone follows the king's rank-list. RBAC: key rings go to the hat (role)"),
         "caption": ("접근통제 모델은 열쇠 결정권을 누구에게 두는지의 규칙이에요.", "An access-control model is a rule for who gets to decide the keys."),
         "small": ('MAC의 등급표는 <a href="blpbiba-ko.html">정확한 규칙</a>이 따로 있고, RBAC는 이미 <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>로 자세히 다뤘어요.',
                   'MAC\'s rank-list has its own <a href="blpbiba-en.html">precise rules</a>, and RBAC is already covered in <a href="rbac-en.html">a key ring for every hat</a>.'),
         "tricks": (4, [
             (OWNER_I, ("DAC", "DAC"), ("방 주인이 직접 정해요", "the room's owner decides directly"), "calm"),
             (LABEL_I, ("MAC", "MAC"), ("왕의 등급표, 주인도 못 바꿔요", "the king's rank-list — not even the owner can override it")),
             (HAT_I, ("RBAC", "RBAC"), ("모자(역할)에 열쇠를 줘요", "keys go to the hat (role)"), "warm"),
             (MIX_I, ("섞어서 써요", "Mixed in practice"), ("한 성이 세 모델을 같이 쓰기도 해요", "one castle may run all three models together")),
         ])},
        {"svg": svg(340, sky(340)
                    + '<rect x="40" y="30" width="680" height="260" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="34" rx="8" fill="#C9A86A"/>'
                    + label(130, 53, "⟦모델|model⟧", 13, "#142033", cls="d") + label(330, 53, "⟦결정권자|who decides⟧", 13, "#142033", cls="d") + label(560, 53, "⟦예시|example⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M40 {64 + i * 75} h680" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(130, 100, "⟦DAC|DAC⟧", 14, "#142033", cls="d") + label(330, 100, "⟦자원의 주인|the resource's owner⟧", 11, "#142033") + label(560, 100, "⟦파일 공유 권한|sharing a file⟧", 11, "#142033")
                    + label(130, 175, "⟦MAC|MAC⟧", 14, "#142033", cls="d") + label(330, 175, "⟦중앙(왕)의 등급표, 주인도 못 바꿈|central rank-list — owners can't change it⟧", 11, "#142033") + label(560, 175, "⟦군사·기밀 등급 체계|military/classified systems⟧", 11, "#142033")
                    + label(130, 250, "⟦RBAC|RBAC⟧", 14, "#142033", cls="d") + label(330, 250, "⟦역할(모자)을 정한 관리자|the admin who defines the role (hat)⟧", 11, "#142033") + label(560, 250, "⟦회사 시스템에 흔해요|common in company systems⟧", 11, "#142033")),
         "alt": ("표: DAC — 자원의 주인이 결정 / 파일 공유, MAC — 왕의 등급표·주인도 못 바꿈 / 군사·기밀 체계, RBAC — 역할을 정한 관리자 / 회사 시스템", "Table: DAC — owner decides / file sharing, MAC — rank-list owners can't change / military systems, RBAC — the admin who defines roles / company systems"),
         "caption": ("세 모델의 결정권자를 나란히 놓고 보면 이래요.", "Here are the three models side by side: who decides, with an example of each."),
         "small": ("결정권자가 다르면 유연성과 위험도 달라져요. 시험 공부 때는 결정권자를 기준으로 셋을 비교해 두면 좋아요.", "Different decision-makers mean different flexibility and risk. When studying for the exam, compare the three by who decides.")},
        {"svg": svg(300, sky(300)
                    + keyring(190, 150, 2) + label(190, 230, "⟦DAC는 유연하지만 주인이 엉뚱한 사람에게 열쇠를 주기 쉬워요|DAC is flexible, but owners easily give keys to the wrong person⟧", 11, "var(--ink)")
                    + keyring(570, 150, 1) + label(570, 230, "⟦MAC는 엄격하지만 등급표를 주인이 못 바꿔서 답답해요|MAC is strict, but owners can't adjust the rank-list to adapt⟧", 11, "var(--ink)")
                    + label(380, 280, "⟦그래서 많은 성이 역할(RBAC)과 속성(ABAC) 규칙도 같이 써요|so many castles mix in role-based (RBAC) and attribute-based (ABAC) rules too⟧", 12, "var(--ink)", cls="d")),
         "alt": ("DAC는 유연하지만 주인이 엉뚱한 사람에게 열쇠를 주기 쉽고, MAC는 엄격하지만 주인이 등급표를 못 바꿔서 답답함. 많은 성이 RBAC와 ABAC도 같이 씀", "DAC is flexible, but owners easily give keys to the wrong person; MAC is strict, but owners can't adjust its rank-list to adapt. Many castles mix in RBAC and ABAC too"),
         "caption": ("모델 하나만으로는 부족할 때가 많아요.", "One model alone often isn't enough."),
         "small": ('실제로는 여러 모델을 섞어 써요. → <a href="rbac-ko.html">RBAC</a>, <a href="abac-ko.html">ABAC</a>, MAC의 정확한 규칙은 <a href="blpbiba-ko.html">BLP/Biba</a>에서 다뤄요.',
                   'In practice, castles blend several models. → <a href="rbac-en.html">RBAC</a>, <a href="abac-en.html">ABAC</a>; MAC\'s precise rules are covered in <a href="blpbiba-en.html">BLP/Biba</a>.')},
    ],
    "summary": (("<b>접근통제 모델</b>은 '열쇠를 누가 결정하나'의 규칙이에요. <b>DAC</b>는 방 주인이, <b>MAC</b>는 왕의 등급표가, <b>RBAC</b>는 모자(역할)에 따라 열쇠가 정해져요.",
                 "An <b>access-control model</b> is a rule for who decides the keys. <b>DAC</b> lets the owner decide, <b>MAC</b> follows a fixed rank-list, <b>RBAC</b> assigns by hat (role)."),
                ("Discretionary Access Control(DAC)은 자원 소유자가 재량으로 권한을 부여하고, Mandatory Access Control(MAC)은 중앙에서 정한 보안 등급(레이블)을 소유자도 바꿀 수 없으며, Role-Based Access Control(RBAC)은 역할에 권한을 묶고 사용자에게 역할만 부여해요. 기술사 시험 공부 때는 이 셋을 결정권자·유연성·적용 사례로 비교해 두면 좋아요.",
                 "Discretionary Access Control (DAC) lets the resource owner grant permissions at their own discretion; Mandatory Access Control (MAC) enforces centrally fixed security labels that not even the owner can override; Role-Based Access Control (RBAC) binds permissions to roles and assigns users only a role. When studying for the exam, compare the three by who decides, how flexible each is, and where each is typically applied.")),
    "glossary": [
        ("DAC", "Discretionary Access Control", ("방 주인이 직접 정해요.", "The room's owner decides directly."), ("유연하지만, 주인이 실수하면 바로 사고로 이어져요.", "Flexible — but one owner's mistake becomes an incident immediately.")),
        ("MAC", "Mandatory Access Control", ("왕의 등급표, 주인도 못 바꿔요.", "The king's rank-list — not even the owner can override it."), ('자세한 읽기·쓰기 규칙은 따로 있어요. → <a href="blpbiba-ko.html">접근통제 보안 모델(BLP/Biba)</a>', 'Its precise read/write rules live in their own page. → <a href="blpbiba-en.html">Access-control security models (BLP/Biba)</a>')),
        ("RBAC", "Role-Based Access Control", ("모자(역할)에 열쇠를 줘요.", "Keys go to the hat (role), not the person."), ('회사 시스템에서 흔히 써요. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'Commonly used in company systems. → <a href="rbac-en.html">a key ring for every hat</a>')),
        ("ABAC", "Attribute-Based Access Control", ("문지기의 조건 문장.", "The gatekeeper's if-sentence."), ('꼬리표(속성) 여러 개를 조합해요. → <a href="abac-ko.html">문지기의 조건 문장</a>', 'Combines several tags (attributes) into one condition. → <a href="abac-en.html">the gatekeeper\'s if-sentence</a>')),
        ("보안 등급(레이블)", "Security label", ("왕의 등급 도장.", "The king's rank stamp."), ("MAC에서 방과 사람 모두에게 붙는 고정 등급이에요.", "A fixed rank attached to both the room and the person, under MAC.")),
        ("최소 권한", "Least privilege", ("딱 필요한 열쇠만.", "Only the key you actually need."), ('어느 모델을 쓰든 지켜야 하는 원칙이에요. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'A principle every model should still follow. → <a href="leastprivilege-en.html">only the key you need</a>')),
        ("감사(Audit)", "Audit", ("누가 왜 그 열쇠를 가졌는지 확인.", "Checking who holds a key, and why."), ('규칙이 분명해야 검사관도 점검할 수 있어요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'A clear rule is what lets the inspector check it at all. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
        ("혼합 모델", "Hybrid model", ("세 모델을 같이 쓰는 성.", "A castle running all three together."), ("실제 조직은 DAC·MAC·RBAC·ABAC를 상황별로 섞어 써요.", "Real organizations blend DAC, MAC, RBAC and ABAC, each where it fits.")),
    ],
}
