from _draw import *

GOLD = "#E9B44C"
ADMIN = dict(hat="var(--accent)", shirt="#4A5A72")   # 고치는 사람
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def master_key(x, y, s=1.0, color=GOLD):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="22" fill="none" stroke="{color}" stroke-width="10"/>'
            f'<rect x="20" y="-5" width="80" height="10" fill="{color}"/><rect x="72" y="5" width="8" height="12" fill="{color}"/><rect x="88" y="5" width="8" height="16" fill="{color}"/>'
            f'<path d="M-4 -30 l3 -8 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3z" fill="{color}"/></g>')


def door(x, y, name, s=1.0, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><circle cx="20" cy="54" r="4" fill="{GOLD}"/>'
            f'{label(0, -8, name, 13, "var(--ink)")}{extra}</g>')


def vault(x, y, s=1.0, open_door=False):
    inner = (f'<rect x="-70" y="-90" width="140" height="180" rx="8" fill="#0A1120"/>'
             + master_key(-20, 0, 0.7) + '<rect x="70" y="-90" width="40" height="180" rx="4" fill="var(--night)" transform="skewY(-8)"/>') if open_door else \
            '<circle r="30" fill="none" stroke="var(--stone)" stroke-width="8"/><circle r="7" fill="var(--accent)"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-80" y="-100" width="160" height="200" rx="10" fill="var(--night)"/>{inner}</g>')


def ledger(x, y, rows, s=1.0):
    lines = "".join(label(14, 44 + i * 24, r, 12, "#142033", "start") for i, r in enumerate(rows))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="230" height="{50 + len(rows) * 24}" rx="4" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect x="0" y="0" width="230" height="26" rx="4" fill="#C9A86A"/>{label(115, 18, "⟦열쇠 대장|KEY LEDGER⟧", 13, "#142033")}{lines}</g>')


CHECK = '<path d="M-12 50 l9 9 l17 -19" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>'
DOORS = ("⟦부엌|Kitchen⟧", "⟦금고|Vault⟧", "⟦서재|Study⟧", "⟦성문|Gate⟧")

# 1. 모든 문을 여는 열쇠
P1 = svg(280, sky(280) + master_key(150, 130, 1.3)
         + label(150, 220, "⟦마스터 열쇠|the master key⟧", 14, "var(--ink)", cls="d")
         + "".join(door(360 + i * 100, 60, n, 0.9, CHECK) for i, n in enumerate(DOORS))
         + label(510, 250, "⟦전부 열려요|opens everything⟧", 13, "var(--muted)"))

# 2. 여기저기 굴러다닌다
HOOKS = "".join(f'<circle cx="{x}" cy="50" r="5" fill="var(--stone-dark)"/>' + master_key(x + 10, 90, 0.45) for x in (80, 150, 220))
DRAWER = ('<rect x="330" y="120" width="140" height="70" rx="4" fill="#8B5E3C"/><rect x="340" y="130" width="120" height="50" fill="#5A3B22"/>'
          + master_key(390, 155, 0.45) + '<rect x="390" y="112" width="20" height="6" rx="3" fill="{GOLD}"/>'.replace("{GOLD}", GOLD))
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>' + HOOKS + label(160, 140, "⟦벽에 걸려 있고|on hooks⟧", 12, "var(--muted)")
         + DRAWER + label(400, 220, "⟦서랍에도|in a drawer⟧", 12, "var(--muted)")
         + person(540, 90, s=0.85, face=MASK, extra=master_key(70, 60, 0.4))
         + label(575, 220, "⟦하나 없어져도 몰라요|one goes missing, nobody knows⟧", 12, "var(--bad)")
         + person(660, 100, s=0.8, hat=None, shirt="#4A5A72", face=SMILE, extra=master_key(60, 80, 0.35))
         + label(690, 250, "⟦그만둔 사람 주머니|in an ex-employee\'s pocket⟧", 11, "var(--bad)"))

# 3. PAM = 금고에 넣고 빌려준다 (hero)
TAGGED_KEY = master_key(330, 170, 0.7) + ('<g transform="translate(360,110)"><rect width="150" height="40" rx="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
                                          + label(75, 17, "⟦부엌 문 고치기|fix the kitchen door⟧", 12, "var(--ink)") + label(75, 33, "⟦1시간|1 hour⟧", 12, "var(--accent)") + "</g>")
P3 = svg(340, sky(340) + vault(110, 170, 0.9, open_door=True) + label(110, 300, "⟦금고|the vault⟧", 14, "var(--ink)", cls="d")
         + person(230, 60, s=0.8, face=EYES, **GUARD) + TAGGED_KEY
         + '<path d="M400 175 L450 175" stroke="var(--accent)" stroke-width="3"/><path d="M440 165 L452 175 L440 185" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + person(460, 120, s=0.85, face=SMILE, **ADMIN)
         + ledger(540, 40, ("⟦14:00 지민 · 부엌 · 1시간|14:00 Jimin · kitchen · 1h⟧", "⟦11:20 태오 · 성문 · 30분|11:20 Taeo · gate · 30m⟧", "⟦어제 지민 · 서재 · 2시간|yest. Jimin · study · 2h⟧"), 0.9)
         + label(380, 320, "⟦쓸 때만, 이유를 적고, 시간을 정해서 꺼내요|only when needed, with a reason, for a set time⟧", 14, "var(--muted)"))

# 4. 지켜보고, 돌려주면 열쇠를 바꾼다
WRENCH = '<g transform="translate(66,70) rotate(-40)"><rect x="-4" y="-22" width="8" height="40" rx="2" fill="var(--stone-dark)"/><path d="M-10 -30 h20 v10 h-6 v-4 h-8 v4 h-6z" fill="var(--stone-dark)"/></g>'
SCROLL = ('<g transform="translate(236,60)"><rect width="60" height="70" rx="4" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/>'
          + "".join(f'<rect x="8" y="{12 + i * 12}" width="{44 - (i * 9) % 20}" height="4" rx="2" fill="#C9A86A"/>' for i in range(5)) + "</g>")
ANVIL = ('<g transform="translate(600,190)"><path d="M-50 -20 h100 l-10 20 h-30 v20 h-20 v-20 h-30 z" fill="var(--stone-dark)"/>'
         '<g transform="translate(30,-60) rotate(30)"><rect x="-4" y="-10" width="8" height="50" rx="2" fill="#8B5E3C"/><rect x="-16" y="-24" width="32" height="18" rx="3" fill="var(--stone-dark)"/></g></g>')
P4 = svg(280, '<rect width="380" height="280" fill="var(--sky)"/><rect x="380" width="380" height="280" fill="var(--good-soft)"/>'
         + door(80, 60, "⟦부엌|Kitchen⟧", 0.9) + person(110, 110, s=0.85, face=SMILE, **ADMIN, extra=WRENCH)
         + person(200, 100, s=0.8, face=EYES, **GUARD) + SCROLL
         + label(190, 262, "⟦옆에서 다 적어요|every move written down⟧", 13, "var(--muted)")
         + master_key(470, 130, 0.7) + label(470, 175, "⟦돌려준 열쇠|the returned key⟧", 12, "var(--muted)")
         + ANVIL + master_key(600, 120, 0.7, "var(--good)") + label(600, 80, "⟦새 모양|new shape⟧", 13, "var(--good)")
         + label(570, 262, "⟦그날로 열쇠를 바꿔요|reforged the same day⟧", 13, "var(--muted)"))

# 5. 귀찮으면 금고를 안 쓴다 → 비상 열쇠
MAT = '<rect x="120" y="200" width="120" height="16" rx="6" fill="#8B5E3C"/>' + master_key(150, 208, 0.35)
GLASS = ('<g transform="translate(600,130)"><rect x="-70" y="-60" width="140" height="120" rx="8" fill="var(--sky)" fill-opacity="0.6" stroke="var(--bad)" stroke-width="4"/>'
         + master_key(-20, 0, 0.6)
         + '<path d="M-60 -50 l30 40 l-10 20 M-30 -10 l25 -15" stroke="#FFF" stroke-width="2" fill="none"/>'
         + label(0, 48, "⟦비상 · 유리를 깨세요|EMERGENCY · break glass⟧", 11, "var(--bad)") + "</g>")
P5 = svg(280, '<rect width="380" height="280" fill="var(--accent-soft)"/><rect x="380" width="380" height="280" fill="var(--panel)"/>'
         + person(60, 90, s=0.9, face=FROWN + SWEAT, **ADMIN)
         + bubble(30, 20, 220, 36, "⟦급한데 매번 빌리라고?|borrow it every time? in a hurry?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + MAT + label(180, 245, "⟦발판 밑에 몰래 하나|a secret one under the mat⟧", 12, "var(--bad)")
         + GLASS + label(600, 240, "⟦깨진 유리는 반드시 눈에 띄어요|broken glass is always noticed⟧", 12, "var(--muted)"))

VAULT_I = icon('<rect x="10" y="8" width="44" height="48" rx="5" fill="var(--night)"/><circle cx="32" cy="32" r="10" fill="none" stroke="var(--stone)" stroke-width="3"/><circle cx="32" cy="32" r="3" fill="var(--accent)"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 16 V32 L42 40" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
LEDGER_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="20" width="24" height="3" fill="#C9A86A"/><rect x="20" y="30" width="18" height="3" fill="#C9A86A"/><rect x="20" y="40" width="22" height="3" fill="#C9A86A"/>')
EYE_I = icon('<path d="M6 32 Q32 8 58 32 Q32 56 6 32 Z" fill="none" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--good)"/>')

PAGE = {
    "slug": "pam", "order": 19,
    "title": ("금고 속 마스터 열쇠", "The Master Key in the Vault"),
    "h1": ("<em>PAM</em>이 뭐예요?", "What is <em>PAM</em>?"),
    "sub": ("특권 접근 관리(Privileged Access Management)를 금고에 넣어둔 마스터 열쇠 이야기로 풀어봤어요.",
            "Privileged Access Management, told as a story about the master key kept in a vault."),
    "panels": [
        {"svg": P1, "alt": ("반짝이는 큰 황금 열쇠와, 체크 표시가 붙은 부엌·금고·서재·성문 문", "A big sparkling golden key, and Kitchen, Vault, Study and Gate doors all checked"),
         "caption": ("성에는 모든 문을 여는 열쇠가 있어요.", "The castle has one key that opens every door."),
         "small": ("고치는 사람(관리자)이 써요. 이걸 훔치면 성 전체가 열려요.", "The fixers (admins) use it. Steal it, and the whole castle opens.")},
        {"svg": P2, "alt": ("벽 고리와 서랍에 걸린 열쇠 복사본들, 하나를 챙기는 도둑, 열쇠를 들고 나가는 그만둔 사람", "Copies on wall hooks and in a drawer, a thief pocketing one, an ex-employee leaving with another"),
         "caption": ("마스터 열쇠가 여기저기 굴러다녀요.", "Master keys end up lying around."),
         "small": ("복사본이 몇 개인지 아무도 몰라요. 그만둔 사람 주머니에도 있어요.", "Nobody knows how many copies exist. One is in the pocket of someone who quit.")},
        {"svg": P3, "hero": True, "alt": ("열린 금고 안의 마스터 열쇠, 경비가 '부엌 문 고치기 · 1시간' 꼬리표가 달린 열쇠를 관리자에게 건네고, 옆에 열쇠 대장", "The master key inside an open vault; a guard hands the admin a key tagged 'fix the kitchen door · 1 hour'; a key ledger beside them"),
         "caption": ("PAM은 마스터 열쇠를 금고에 넣고 빌려줘요.", "PAM locks the master key in a vault and lends it out."),
         "small": ("쓸 때만, 이유를 적고, 시간을 정해서 꺼내요. 누가 언제 가져갔는지 대장에 남아요.", "Only when needed, with a reason, for a set time. The ledger says who took it and when."),
         "tricks": (4, [
             (VAULT_I, ("금고", "The vault"), ("열쇠가 사는 곳", "where the key lives")),
             (CLOCK_I, ("빌리기", "Borrowing"), ("필요할 때만, 잠깐", "only when needed, briefly"), "warm"),
             (LEDGER_I, ("대장", "The ledger"), ("누가, 언제, 왜", "who, when, why"), "calm"),
             (EYE_I, ("지켜보기", "Watching"), ("쓰는 동안 옆에서", "while it's in use"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 관리자가 부엌 문을 고치는 동안 경비가 옆에서 두루마리에 적음. 오른쪽: 돌려준 열쇠를 모루 위에서 새 모양으로 바꿈", "Left: a guard writes on a scroll while the admin fixes the kitchen door. Right: the returned key is reforged on an anvil into a new shape"),
         "caption": ("쓰는 동안 지켜보고, 돌려주면 열쇠를 바꿔요.", "Watched while in use, reforged when returned."),
         "small": ("돌려준 열쇠는 그날로 모양이 바뀌어요. 몰래 복사해 둔 게 있어도 소용없어요.", "The returned key changes shape the same day. A secret copy is useless.")},
        {"svg": P5, "alt": ("왼쪽: '급한데 매번 빌리라고?' 하며 발판 밑에 열쇠를 숨긴 관리자. 오른쪽: '비상 · 유리를 깨세요' 유리 상자 속 열쇠", "Left: an admin grumbling 'borrow it every time?' with a key hidden under a mat. Right: a key in a glass box marked EMERGENCY · break glass"),
         "caption": ("귀찮으면 금고를 안 써요.", "If it's a hassle, people skip the vault."),
         "small": ("그래서 급할 땐 '유리 깨고 꺼내는' 비상 열쇠를 따로 둬요. 대신 깨진 유리는 반드시 눈에 띄어요.", "So there's an emergency key behind glass. The catch: broken glass is always noticed.")},
    ],
    "summary": (("<b>PAM</b> = 모든 문을 여는 열쇠를 <b>금고</b>에 두고, 쓸 때만 <b>빌려주고</b>, 지켜보고, 돌려받으면 <b>바꾸는</b> 것.",
                 "<b>PAM</b> = keep the key that opens everything in a <b>vault</b>, <b>lend</b> it only when needed, watch it, and <b>reforge</b> it on return."),
                ("Privileged Access Management. 관리자·root·서비스 계정 비밀번호가 '마스터 열쇠'예요. '방 하나, 잠깐만'(제로 트러스트)을 가장 위험한 열쇠에 적용한 거예요.",
                 "Privileged Access Management. Admin, root and service-account passwords are the 'master key'. It's 'one key, for a while' (Zero Trust) applied to the most dangerous key of all.")),
    "glossary": [
        ("특권 계정", "Privileged account", ("마스터 열쇠.", "The master key."), ("관리자, root, 서비스 계정. 모든 문이 열려요.", "Admin, root, service accounts. Every door opens.")),
        ("볼트", "Vault", ("금고.", "The vault."), ("열쇠가 평소에 사는 곳. 사람 주머니가 아니라요.", "Where the key lives when not in use — not in someone's pocket.")),
        ("체크아웃 · JIT", "Checkout · Just-in-time", ("빌리기.", "Borrowing."), ('필요할 때 이유를 적고 잠깐. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'Take it out with a reason, for a short while. → <a href="zerotrust-en.html">the castle that always asks</a>')),
        ("세션 기록", "Session recording", ("옆에서 지켜보기.", "Watching over the shoulder."), ("열쇠를 쓰는 동안 화면을 그대로 녹화해요.", "The screen is recorded while the key is in use.")),
        ("비밀번호 교체", "Credential rotation", ("열쇠 모양 바꾸기.", "Reforging the key."), ("돌려받자마자 새 비밀번호로. 몰래 복사한 건 쓸모없어져요.", "A new password the moment it's returned. Secret copies stop working.")),
        ("감사 대장", "Audit log", ("열쇠 대장.", "The key ledger."), ('누가, 언제, 왜 가져갔는지. → <a href="siem-ko.html">큰 화면</a>으로도 보내요', 'Who took it, when, why. → also sent to the <a href="siem-en.html">big screen</a>')),
        ("브레이크글라스", "Break-glass", ("유리 깨고 꺼내는 열쇠.", "The key behind glass."), ("금고가 막혔을 때의 비상구. 쓰면 반드시 알람이 울려요.", "The emergency exit when the vault is down. Using it always sets off an alarm.")),
        ("상시 권한", "Standing privilege", ("늘 주머니에 있는 열쇠.", "The key that's always in the pocket."), ("PAM이 없애려는 것. 빌려 쓰고 돌려주는 걸로 바꿔요.", "What PAM exists to remove — replaced by borrow-and-return.")),
    ],
}
