from _draw import *

COOK, CLERK, ADMIN_H = "#E9B44C", "#5B8DEF", "var(--accent)"
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def hat(x, y, color, s=1.0):
    return f'<path d="M6 22 Q30 -6 54 22 Z" fill="{color}" transform="translate({x - 30},{y - 22}) scale({s})"/>'


def book(x, y, rows, s=1.0, title="⟦명부|REGISTRY⟧"):
    """펼친 명부. rows 는 (모자색, 이름, 오른쪽 메모) 튜플."""
    lines = ""
    for i, (color, name, note) in enumerate(rows):
        yy = 46 + i * 26
        lines += (hat(30, yy, color, 0.45) if color else label(30, yy + 4, "?", 16, "var(--bad)", cls="d")) \
                 + label(50, yy + 5, name, 13, "#142033", "start") + label(240, yy + 5, note, 12, "#5B6B82", "end")
    h = 60 + len(rows) * 26
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="260" height="{h}" rx="6" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect width="260" height="28" rx="6" fill="#C9A86A"/>{label(130, 19, title, 14, "#142033", cls="d")}'
            f'<path d="M130 28 V{h}" stroke="#C9A86A" stroke-width="1" stroke-dasharray="3 3"/>{lines}</g>')


def robot(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="8" y="10" width="44" height="40" rx="6" fill="var(--stone-dark)"/>'
            f'<rect x="16" y="20" width="10" height="10" rx="2" fill="#5B9BD5"/><rect x="34" y="20" width="10" height="10" rx="2" fill="#5B9BD5"/>'
            f'<rect x="20" y="38" width="20" height="4" rx="2" fill="var(--panel)"/><rect x="28" y="-4" width="4" height="14" fill="var(--stone-dark)"/><circle cx="30" cy="-6" r="4" fill="var(--accent)"/>'
            f'<rect x="12" y="52" width="36" height="50" rx="8" fill="var(--stone-dark)"/></g>')


def desk(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-90" y="0" width="180" height="14" rx="4" fill="#8B5E3C"/>'
            f'<rect x="-80" y="14" width="10" height="60" fill="#8B5E3C"/><rect x="70" y="14" width="10" height="60" fill="#8B5E3C"/></g>')


# 1. 성에는 사람이 정말 많다
CROWD = "".join(person(40 + i * 82, 120, hat=c, shirt="#4A5A72", s=0.8, face=SMILE)
                for i, c in enumerate((COOK, CLERK, None, ADMIN_H, COOK, "var(--stone-dark)", CLERK, None)))
P1 = svg(280, sky(280) + CROWD
         + '<path d="M20 250 L60 250" stroke="var(--good)" stroke-width="3"/><path d="M50 242 L62 250 L50 258" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(40, 235, "⟦오늘 들어옴|joined today⟧", 11, "var(--good)")
         + '<path d="M690 250 L730 250" stroke="var(--bad)" stroke-width="3"/><path d="M720 242 L732 250 L720 258" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(710, 235, "⟦어제 나감|left yesterday⟧", 11, "var(--bad)")
         + label(380, 265, "⟦요리사, 회계, 손님, 고치는 사람… 누가 누구더라?|cooks, clerks, guests, fixers… who is who again?⟧", 13, "var(--muted)"))

# 2. 명부가 없으면 엉망
KEYS = '<g transform="translate(60,80)"><circle r="9" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="8" y="-3" width="22" height="6" fill="#E9B44C"/><rect x="22" y="3" width="4" height="6" fill="#E9B44C"/></g>'
P2 = svg(270, '<rect width="760" height="270" fill="var(--bad-soft)"/>'
         + person(60, 80, s=0.9, hat=COOK, shirt="#4A5A72", face=SMILE, extra=KEYS) + label(90, 225, "⟦나갔는데 열쇠는 그대로|left, but kept the keys⟧", 12, "var(--bad)")
         + person(300, 80, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT) + bubble(270, 20, 150, 34, "⟦열쇠가 없어요|I have no keys⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + label(330, 225, "⟦새 사람은 일주일째 대기|the new hire waits a week⟧", 12, "var(--muted)")
         + person(560, 80, s=0.9, face=EYES, **GUARD) + bubble(520, 20, 170, 34, "⟦…누구세요?|…and you are?⟧", 13, "var(--panel)", "var(--good)", "bottom")
         + label(590, 225, "⟦문지기는 얼굴을 몰라요|the gatekeeper can\'t tell⟧", 12, "var(--muted)"))

# 3. IAM = 성의 명부 관리소 (hero)
SPOKES = "".join(f'<path d="M380 200 L{x} {y}" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6"/>' for x, y in ((90, 90), (90, 300), (670, 90), (670, 300)))
RING = '<g transform="translate(64,84)"><circle r="9" fill="none" stroke="#E9B44C" stroke-width="5"/><path d="M-5 -9 L0 -16 L5 -9 Z" fill="var(--accent)"/></g>'
PASS = ('<g transform="translate(610,60)"><rect width="120" height="60" rx="6" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
        + label(60, 26, "⟦통행증|PASS⟧", 13, "var(--good)", cls="d") + '<g transform="translate(98,20) rotate(-15)"><circle r="11" fill="none" stroke="var(--bad)" stroke-width="2"/></g>' + label(60, 48, "⟦지민 · 오늘|Jimin · today⟧", 11, "#142033") + "</g>")
VAULT = ('<g transform="translate(670,300)"><rect x="-40" y="-50" width="80" height="100" rx="6" fill="var(--night)"/><circle r="16" fill="none" stroke="var(--stone)" stroke-width="5"/><circle r="4" fill="var(--accent)"/></g>')
P3 = svg(370, '<rect width="760" height="370" fill="var(--panel)"/>' + SPOKES
         + desk(380, 240) + book(250, 100, ((COOK, "⟦김요리|Kim⟧", "⟦반지 ✓ 부엌·창고|ring ✓ kitchen·storage⟧"), (CLERK, "⟦박회계|Park⟧", "⟦반지 ✓ 금고·서재|ring ✓ vault·study⟧"), (ADMIN_H, "⟦지민|Jimin⟧", "⟦반지 ✓ 고치기|ring ✓ fixer⟧")), 1.0)
         + label(380, 40, "⟦명부 관리소|the Registry⟧", 20, "var(--ink)", cls="d")
         + person(40, 40, s=0.75, face=EYES, **GUARD, extra=RING) + label(90, 150, "⟦문지기|gatekeeper⟧", 12, "var(--muted)")
         + hat(90, 290, COOK, 1.1) + hat(90, 320, CLERK, 1.1) + label(90, 350, "⟦모자|hats⟧", 12, "var(--muted)")
         + PASS + label(670, 150, "⟦통행증|pass⟧", 12, "var(--muted)")
         + VAULT + label(670, 365, "⟦금고|vault⟧", 12, "var(--muted)"))

# 4. 들어올 때, 바뀔 때, 나갈 때
COLS = (("⟦입성|Joining⟧", "var(--good)"), ("⟦이동|Moving⟧", "var(--accent)"), ("⟦퇴성|Leaving⟧", "var(--bad)"))
HEAD = "".join(f'<rect x="{20 + i * 250}" y="16" width="220" height="34" rx="8" fill="{c}"/>' + label(130 + i * 250, 39, n, 16, "#FFF", cls="d") for i, (n, c) in enumerate(COLS))
JOIN = (person(60, 80, s=0.8, hat=None, shirt="#4A5A72", face=SMILE) + '<path d="M120 140 L160 140" stroke="var(--good)" stroke-width="3"/><path d="M150 130 L162 140 L150 150" stroke="var(--good)" stroke-width="3" fill="none"/>'
        + hat(200, 140, COOK, 1.0) + '<g transform="translate(200,175)"><circle r="7" fill="none" stroke="#E9B44C" stroke-width="4"/><path d="M-4 -7 L0 -13 L4 -7 Z" fill="var(--accent)"/></g>'
        + label(130, 250, "⟦명부에 적고, 모자와 반지|on the registry; hat and ring⟧", 12, "var(--muted)"))
MOVE = (person(310, 80, s=0.8, hat=COOK, shirt="#4A5A72", face=SMILE) + '<path d="M370 140 L410 140" stroke="var(--accent)" stroke-width="3"/><path d="M400 130 L412 140 L400 150" stroke="var(--accent)" stroke-width="3" fill="none"/>'
        + hat(450, 140, CLERK, 1.0) + '<path d="M440 110 l20 -20" stroke="var(--bad)" stroke-width="3"/>' + hat(450, 95, COOK, 0.6)
        + label(380, 250, "⟦모자를 바꿔 씌워요|swap the hat⟧", 12, "var(--muted)"))
LEAVE = (person(560, 80, s=0.8, hat=CLERK, shirt="#4A5A72", face=SMILE) + '<path d="M620 140 L660 140" stroke="var(--bad)" stroke-width="3"/><path d="M650 130 L662 140 L650 150" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + '<g transform="translate(700,140)"><rect x="-30" y="-20" width="60" height="40" rx="4" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/><path d="M-18 -8 h36 M-18 0 h36 M-18 8 h36" stroke="#C9A86A" stroke-width="2"/><path d="M-22 -14 l44 28" stroke="var(--bad)" stroke-width="4"/></g>'
         + label(630, 250, "⟦명부에서 지우면 문이 전부 닫혀요|erase the line, every door shuts⟧", 12, "var(--muted)"))
P4 = svg(280, sky(280) + HEAD + JOIN + MOVE + LEAVE)

# 5. 명부엔 사람만 있는 게 아니다
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + book(60, 40, ((COOK, "⟦김요리|Kim⟧", "⟦부엌|kitchen⟧"), (CLERK, "⟦박회계|Park⟧", "⟦금고|vault⟧"), (None, "⟦심부름 로봇 #7|errand robot #7⟧", "⟦?|?⟧"), (None, "⟦옆 마을 손님|next-town guest⟧", "⟦?|?⟧")), 0.9)
         + robot(400, 90, 1.0) + label(430, 210, "⟦심부름 로봇|errand robot⟧", 12, "var(--muted)") + label(430, 228, "⟦(서비스 계정)|(service account)⟧", 11, "var(--muted)")
         + person(560, 80, s=0.9, hat="var(--stone-dark)", shirt="#4A5A72", face=SMILE) + label(590, 210, "⟦옆 마을 손님|next-town guest⟧", 12, "var(--muted)") + label(590, 228, "⟦(협력사)|(a partner)⟧", 11, "var(--muted)")
         + label(520, 280, "⟦잊기 쉬운 건 늘 이쪽이에요|these are the ones everyone forgets⟧", 13, "var(--bad)"))

BOOK_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="20" width="24" height="3" fill="#C9A86A"/><rect x="20" y="30" width="18" height="3" fill="#C9A86A"/><rect x="20" y="40" width="22" height="3" fill="#C9A86A"/>')
GUARD_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><path d="M20 18 Q32 4 44 18 Z" fill="var(--good)"/><rect x="18" y="34" width="28" height="22" rx="8" fill="var(--good)"/>')
HAT_I = icon(f'<path d="M8 40 Q32 6 56 40 Z" fill="{COOK}"/><rect x="6" y="40" width="52" height="6" rx="3" fill="{COOK}"/>')
LEDGER_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="18" y="22" width="24" height="3" fill="var(--line)"/><rect x="18" y="30" width="28" height="3" fill="var(--line)"/><rect x="18" y="38" width="20" height="3" fill="var(--line)"/>')

PAGE = {
    "slug": "iam", "order": 20,
    "title": ("성의 명부 관리소", "The Castle Registry"),
    "h1": ("<em>IAM</em>이 뭐예요?", "What is <em>IAM</em>?"),
    "sub": ("신원·접근 관리(Identity and Access Management)를 성의 명부 관리소 이야기로 풀어봤어요.",
            "Identity and Access Management, told as a story about the castle's registry."),
    "panels": [
        {"svg": P1, "alt": ("여러 색 모자를 쓴 사람들이 줄지어 있고, 왼쪽엔 '오늘 들어옴', 오른쪽엔 '어제 나감' 화살표", "A row of people in different hats; an arrow on the left says joined today, one on the right says left yesterday"),
         "caption": ("성에는 사람이 정말 많아요.", "A castle holds a lot of people."),
         "small": ("요리사, 회계, 손님, 고치는 사람… 오늘 들어온 사람, 어제 나간 사람.", "Cooks, clerks, guests, fixers… someone joined today, someone left yesterday.")},
        {"svg": P2, "alt": ("열쇠를 든 채 나간 요리사, 열쇠가 없어 기다리는 새 사람, 얼굴을 못 알아보는 문지기", "A cook who left still holding keys, a new hire with no keys, a gatekeeper who can't tell who's who"),
         "caption": ("명부가 없으면 엉망이 돼요.", "Without a registry it's a mess."),
         "small": ("나간 사람은 열쇠를 갖고 있고, 새 사람은 열쇠가 없어 기다리고, 문지기는 얼굴을 몰라요.", "Leavers keep their keys, joiners wait for theirs, and the gatekeeper can't tell anyone apart.")},
        {"svg": P3, "hero": True, "alt": ("가운데 명부 관리소의 책상 위 펼친 명부(이름, 모자, 반지, 열 수 있는 방)에서 문지기, 모자, 통행증, 금고로 점선이 뻗어 있음", "A registry book on a desk in the center (names, hats, rings, rooms) with dotted lines out to the gatekeeper, the hats, the pass and the vault"),
         "caption": ("IAM은 성의 명부 관리소예요.", "IAM is the castle's registry."),
         "small": ("누가 성 사람인지, 정말 그 사람인지, 무슨 문을 열 수 있는지를 한 곳에서 맡아요.", "Who belongs here, whether it's really them, and which doors they may open — all kept in one place."),
         "tricks": (4, [
             (BOOK_I, ("명부", "The registry"), ("누가 성 사람인지", "who belongs here"), "warm"),
             (GUARD_I, ("문지기", "The gatekeeper"), ("정말 그 사람인지", "is it really them"), "calm"),
             (HAT_I, ("모자와 열쇠", "Hats and keys"), ("무슨 문을 열 수 있는지", "which doors they may open"), "warm"),
             (LEDGER_I, ("대장", "The ledger"), ("누가 언제 무엇을", "who did what, when"), "calm"),
         ])},
        {"svg": P4, "alt": ("입성·이동·퇴성 세 칸: 새 사람이 모자와 반지를 받고, 요리사 모자가 회계 모자로 바뀌고, 나가는 사람의 명부 줄이 지워짐", "Three columns — joining, moving, leaving: a newcomer gets a hat and ring, a cook's hat becomes a clerk's, a leaver's registry line is struck out"),
         "caption": ("들어올 때, 바뀔 때, 나갈 때 명부를 고쳐요.", "The registry changes when people join, move, or leave."),
         "small": ("나가는 날 명부에서 지우면 모든 문이 한꺼번에 닫혀요. 열쇠를 하나하나 찾으러 다닐 필요가 없어요.", "Erase the line on the day they leave and every door shuts at once — no hunting down keys one by one.")},
        {"svg": P5, "alt": ("명부에 심부름 로봇과 옆 마을 손님 줄에 물음표가 있고, 옆에 로봇과 회색 모자를 쓴 손님", "The registry shows question marks next to an errand robot and a next-town guest; the robot and the grey-hatted guest stand beside it"),
         "caption": ("명부엔 사람만 있는 게 아니에요.", "The registry isn't just people."),
         "small": ("심부름 로봇(서비스 계정)과 옆 마을 손님(협력사)도 명부에 있어야 해요. 잊기 쉬운 건 늘 이쪽이에요.", "Errand robots (service accounts) and next-town guests (partners) belong on it too — and they're the ones everyone forgets.")},
    ],
    "summary": (("<b>IAM</b> = 누가 성 사람이고, 정말 그 사람이며, 무슨 문을 열 수 있는지를 <b>한 곳에서</b> 맡는 <b>명부 관리소</b>.",
                 "<b>IAM</b> = the <b>registry</b> that keeps, <b>in one place</b>, who belongs here, whether it's really them, and which doors they may open."),
                ("Identity and Access Management. 문지기(MFA), 반지(패스키), 통행증(SSO), 모자(RBAC), 조건 문장(ABAC), 금고(PAM)가 전부 이 관리소의 일이에요. Okta, Microsoft Entra ID, AWS IAM 같은 것들.",
                 "Identity and Access Management. The gatekeeper (MFA), the ring (passkeys), the pass (SSO), the hats (RBAC), the if-sentence (ABAC) and the vault (PAM) are all this registry's job. Think Okta, Microsoft Entra ID, AWS IAM.")),
    "glossary": [
        ("신원", "Identity", ("명부의 한 줄.", "One line in the registry."), ("이 사람(또는 로봇)이 성의 누구인지.", "Who this person (or robot) is to the castle.")),
        ("인증", "Authentication", ("정말 그 사람?", "Is it really them?"), ('문지기의 일. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>, <a href="passkey-ko.html">성문을 알아보는 반지</a>', 'The gatekeeper\'s job. → <a href="mfa-en.html">the gatekeeper\'s three questions</a>, <a href="passkey-en.html">the ring that knows the gate</a>')),
        ("인가", "Authorization", ("무슨 문?", "Which doors?"), ('모자와 조건 문장의 일. → <a href="rbac-ko.html">모자</a>, <a href="abac-ko.html">조건 문장</a>', 'The hats\' and the if-sentence\'s job. → <a href="rbac-en.html">hats</a>, <a href="abac-en.html">if-sentences</a>')),
        ("계정 수명주기", "Lifecycle (Joiner · Mover · Leaver)", ("입성 · 이동 · 퇴성.", "Join · move · leave."), ("명부가 바뀌는 세 순간. 퇴성 날이 제일 중요해요.", "The three moments the registry changes. Leaving day matters most.")),
        ("프로비저닝", "Provisioning", ("모자와 열쇠 나눠주기.", "Handing out hats and keys."), ("명부에 적히면 자동으로 모자·반지·통행증이 나가고, 지우면 자동으로 돌아와요.", "Written in, the hat, ring and pass go out automatically; struck out, they all come back.")),
        ("디렉터리", "Directory", ("명부 책 자체.", "The book itself."), ("Active Directory, LDAP. 명부를 담아두는 큰 책.", "Active Directory, LDAP — the big book the registry lives in.")),
        ("서비스 계정", "Service account", ("심부름 로봇.", "The errand robot."), ('사람이 아닌데 열쇠가 있어요. 주인이 없으면 위험해요. → <a href="pam-ko.html">금고 이야기</a>', 'Not a person, but it holds keys. Dangerous if nobody owns it. → <a href="pam-en.html">the vault story</a>')),
        ("접근 검토", "Access review", ("명부 점검 날.", "Registry inspection day."), ("분기마다 줄줄이 읽어요. 아직 있어야 할 사람인가, 그 모자가 맞나.", "Every quarter, read it line by line: should they still be here, is that the right hat.")),
    ],
}
