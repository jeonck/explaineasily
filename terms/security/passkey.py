from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def ring(x, y, s=1.0, lit=True, engraved=""):
    band = "#E9B44C" if lit else "var(--stone)"
    gem = "var(--accent)" if lit else "var(--stone-dark)"
    glow = f'<circle r="30" fill="var(--accent)" fill-opacity="0.18"/>' if lit else ""
    tag = label(0, 40, engraved, 11, "var(--muted)") if engraved else ""
    return (f'<g transform="translate({x},{y}) scale({s})">{glow}<circle r="16" fill="none" stroke="{band}" stroke-width="8"/>'
            f'<path d="M-8 -16 L0 -28 L8 -16 Z" fill="{gem}"/>{tag}</g>')


def fake_gate(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="30" width="140" height="90" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"/>'
            + battlements(-70, 10, 140, 4, "var(--stone)", 20)
            + '<path d="M-28 120 V78 a28 28 0 0 1 56 0 V120 Z" fill="var(--night)"/>'
            '<rect x="60" y="40" width="10" height="90" fill="#8B5E3C" transform="rotate(-20 65 85)"/></g>')


def sticky(x, y, text, rot=-6):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect width="90" height="80" fill="#FFE97A"/>'
            f'<rect x="30" y="-6" width="30" height="12" fill="var(--line)" fill-opacity="0.8"/>{label(45, 50, text, 18, "#142033", cls="d")}</g>')


# 1. 암호말은 외워야 하고, 샌다
P1 = svg(270, '<rect width="760" height="270" fill="var(--bad-soft)"/>'
         + person(60, 80, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + bubble(30, 14, 220, 40, "⟦사과였나… 사과1이었나…|apple… or was it apple1…⟧", 14, "var(--panel)", "var(--line)", "bottom")
         + sticky(300, 80, "⟦사과1|apple1⟧") + label(345, 210, "⟦적어두고|written down⟧", 13, "var(--muted)")
         + small_castle(470, 70, 0.4) + small_castle(560, 70, 0.4) + small_castle(650, 70, 0.4)
         + "".join(label(x + 32, 150, "⟦사과1|apple1⟧", 12, "var(--bad)") for x in (470, 560, 650))
         + label(592, 210, "⟦어디서나 똑같이|the same everywhere⟧", 13, "var(--muted)"))

# 2. 가짜 성문엔 6자리 코드도 속는다
PHONE = ('<g transform="translate(80,34) scale(0.6)"><rect x="-26" y="-46" width="52" height="92" rx="8" fill="var(--night)"/>'
         '<rect x="-20" y="-36" width="40" height="66" rx="3" fill="var(--panel)"/>' + label(0, 2, "482 913", 13, "#142033") + "</g>")
P2 = svg(280, sky(280) + fake_gate(560, 60) + label(560, 230, "⟦가짜 성문|fake gate⟧", 13, "var(--bad)")
         + person(640, 100, s=0.6, face=MASK, extra=PHONE)
         + person(160, 120, s=0.9, **ME) + bubble(120, 40, 140, 36, "482 913", 16, "var(--panel)", "var(--line)", "bottom")
         + '<path d="M270 100 L480 100" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8"/><path d="M468 90 L482 100 L468 110" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(370, 85, "⟦내가 읽어줘요|I read it out⟧", 13, "var(--bad)"))

# 3. 패스키 = 성문을 알아보는 반지 (hero)
FINGER = '<path d="M74 78 q10 -14 6 -30" stroke="#E8C9A8" stroke-width="10" stroke-linecap="round" fill="none"/>'
P3 = svg(340, sky(340) + gate(540, 70) + label(540, 60, "⟦사진 성|Photo Castle⟧", 14, "var(--ink)", cls="d")
         + person(140, 150, s=0.9, **ME, extra=FINGER)
         + ring(230, 235, 1.3, lit=True, engraved="⟦'사진 성'|'Photo Castle'⟧")
         + '<path d="M270 225 Q400 150 500 170" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + bubble(300, 100, 190, 34, "⟦반지: 사진 성 맞네!|ring: yes, Photo Castle!⟧", 12, "var(--accent-soft)", "var(--accent)", "bottom")
         + bubble(470, 190, 200, 34, "⟦성문: 내 반지 맞네!|gate: yes, my ring!⟧", 12, "var(--accent-soft)", "var(--accent)", "left")
         + label(380, 320, "⟦나는 손가락만 대요. 말할 것도, 외울 것도 없어요|I just touch it — nothing to say, nothing to remember⟧", 14, "var(--muted)"))

# 4. 가짜 성문에선 반지가 안 켜진다
P4 = svg(280, sky(280) + fake_gate(560, 50) + label(560, 220, "⟦가짜 성문|fake gate⟧", 13, "var(--bad)")
         + person(640, 90, s=0.6, face=MASK + SWEAT)
         + person(140, 110, s=0.9, **ME) + ring(230, 205, 1.2, lit=False)
         + bubble(260, 60, 200, 34, "⟦반지: …이 성 아닌데?|ring: …that\'s not my castle⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 262, "⟦불러줄 코드 자체가 없어요|there is no code to read out⟧", 14, "var(--muted)"))

# 5. 반지를 잃어버리면?
VAULT_BOX = ('<g transform="translate(470,80)"><rect width="200" height="130" rx="10" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
             + label(100, 30, "⟦열쇠 보관함|key locker⟧", 14, "var(--good)")
             + "".join(f'<g transform="translate({40 + i * 60},80)"><circle r="12" fill="none" stroke="#E9B44C" stroke-width="6"/><path d="M-6 -12 L0 -21 L6 -12 Z" fill="var(--accent)"/></g>' for i in range(3))
             + label(100, 118, "⟦복사본|copies⟧", 12, "var(--muted)") + "</g>")
P5 = svg(280, '<rect width="380" height="280" fill="var(--bad-soft)"/><rect x="380" width="380" height="280" fill="var(--good-soft)"/>'
         + person(80, 80, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + '<g transform="translate(230,150)"><circle r="16" fill="none" stroke="var(--line)" stroke-width="6" stroke-dasharray="6 6"/></g>' + label(230, 200, "?", 36, "var(--bad)", cls="d")
         + label(190, 255, "⟦휴대폰을 잃어버리면 반지도 같이|lose the phone, lose the ring⟧", 13, "var(--bad)")
         + VAULT_BOX + label(570, 250, "⟦보관함에 복사해 두거나, 여분 반지|copies in the locker, or a spare ring⟧", 13, "var(--good)"))

PRIV_I = icon('<circle cx="32" cy="34" r="14" fill="none" stroke="#E9B44C" stroke-width="7"/><path d="M25 20 L32 8 L39 20 Z" fill="var(--accent)"/><rect x="24" y="30" width="16" height="10" rx="2" fill="var(--night)"/>')
PUB_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="34" r="9" fill="none" stroke="#E9B44C" stroke-width="4"/><path d="M28 25 L32 18 L36 25 Z" fill="var(--accent)"/>')
FINGER_I = icon('<path d="M32 54 V26 a8 8 0 0 1 16 0 v10 M24 40 v-8 a8 8 0 0 1 8 -8" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M20 44 q12 -6 24 0" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "passkey", "order": 16,
    "title": ("성문을 알아보는 반지", "The Ring That Knows the Gate"),
    "h1": ("<em>패스키</em>가 뭐예요?", "What is a <em>Passkey</em>?"),
    "sub": ("패스키(Passkey)를 성문을 알아보는 반지 이야기로 풀어봤어요.",
            "Passkeys, told as a story about a ring that recognizes its own gate."),
    "panels": [
        {"svg": P1, "alt": ("'사과였나 사과1이었나' 헷갈리는 사람, '사과1' 메모지, 똑같은 암호말을 쓰는 성 세 개", "Someone unsure if it was apple or apple1, a sticky note reading apple1, three castles using the same password"),
         "caption": ("암호말은 외워야 하고, 자꾸 새요.", "Passwords must be remembered, and they keep leaking."),
         "small": ("적어두고, 똑같이 쓰고, 옆에서 들려요.", "Written down, reused, overheard.")},
        {"svg": P2, "alt": ("골판지 가짜 성문 뒤의 도둑에게 방문객이 6자리 코드를 읽어줌", "A visitor reads a six-digit code aloud to a thief behind a cardboard fake gate"),
         "caption": ("가짜 성문엔 6자리 코드도 속아요.", "Even the six-digit code falls for a fake gate."),
         "small": ('사람이 코드를 읽어주니까요. <a href="mfa-ko.html">문지기 이야기</a>의 마지막 장면이에요.',
                   'Because a person reads the code out. It\'s the last scene of the <a href="mfa-en.html">gatekeeper story</a>.')},
        {"svg": P3, "hero": True, "alt": ("'사진 성'이 새겨진 반지가 빛나며 진짜 성문과 점선으로 대화하고, 사람은 손가락만 대고 있음", "A ring engraved 'Photo Castle' glows and talks to the real gate along a dotted line; the person just touches it"),
         "caption": ("패스키는 성문을 알아보는 반지예요.", "A passkey is a ring that knows its gate."),
         "small": ("반지 안에 그 성의 이름이 새겨져 있어요. 반지와 성문이 서로 확인하고, 나는 손가락만 대요.", "The castle's name is engraved inside. Ring and gate check each other; I just touch it."),
         "tricks": (3, [
             (PRIV_I, ("반지 속 비밀", "The secret in the ring"), ("내 기기 밖으로 절대 안 나가요", "never leaves my device"), "warm"),
             (PUB_I, ("성문의 반지 사진", "The gate's photo of the ring"), ("성은 사진만 가져요", "the castle keeps only a photo"), "calm"),
             (FINGER_I, ("내 손가락", "My finger"), ("반지를 깨우는 건 나예요", "only I can wake the ring")),
         ])},
        {"svg": P4, "alt": ("가짜 성문 앞에서 반지가 회색으로 꺼져 있고 '이 성 아닌데?' 말풍선", "In front of a fake gate the ring is grey and dark, with a bubble: that's not my castle"),
         "caption": ("가짜 성문에선 반지가 안 켜져요.", "At a fake gate, the ring stays dark."),
         "small": ("성 이름이 달라서요. 불러줄 코드 자체가 없어요.", "Wrong castle name. There's no code to read out — nothing to steal.")},
        {"svg": P5, "alt": ("왼쪽: 반지 자리가 비어 물음표. 오른쪽: 반지 복사본이 든 열쇠 보관함", "Left: an empty ring slot with a question mark. Right: a key locker holding copies of the ring"),
         "caption": ("반지를 잃어버리면 곤란해요.", "Losing the ring is a problem."),
         "small": ("휴대폰이 곧 반지니까요. 그래서 열쇠 보관함(구글·애플 계정)에 복사해 두거나 여분 반지를 만들어요. 아직 반지를 안 받는 성도 있어요.", "The phone is the ring. So it's copied into a key locker (your Google or Apple account), or you keep a spare. And some castles don't take rings yet.")},
    ],
    "summary": (("<b>패스키</b> = 외울 것 없이, <b>성문을 알아보는</b> 반지. 가짜 성문엔 아예 반응하지 않아요.",
                 "A <b>passkey</b> = a ring that <b>knows its gate</b>, with nothing to remember. At a fake gate it does nothing at all."),
                ("FIDO2 / WebAuthn 표준. 반지 속 비밀(개인키)은 절대 성에 보내지 않고, 성엔 사진(공개키)만 있어요. 그래서 성이 털려도 내 반지는 안전해요.",
                 "The FIDO2 / WebAuthn standard. The ring's secret (private key) never goes to the castle; the castle holds only a photo (public key). So even a robbed castle can't copy my ring.")),
    "glossary": [
        ("개인키", "Private key", ("반지 속 비밀.", "The secret in the ring."), ("내 기기 안에서 만들어지고 절대 안 나가요.", "Made inside my device and never leaves it.")),
        ("공개키", "Public key", ("반지 사진.", "The photo of the ring."), ("성이 보관해요. 훔쳐가도 반지를 만들 수는 없어요.", "Kept by the castle. Stealing it doesn't let you forge the ring.")),
        ("WebAuthn · FIDO2", "WebAuthn · FIDO2", ("반지와 성문이 말하는 규칙.", "How ring and gate talk."), ("브라우저와 성이 같은 말을 쓰게 한 표준.", "The standard that makes browsers and castles speak the same language.")),
        ("생체 인증 · PIN", "Biometrics · PIN", ("반지를 깨우는 손가락.", "The finger that wakes the ring."), ('얼굴이나 지문은 기기 안에만 있어요. 성에는 안 가요. → <a href="mfa-ko.html">문지기 이야기</a>', 'Face or fingerprint stays on the device; the castle never sees it. → <a href="mfa-en.html">the gatekeeper story</a>')),
        ("동기화 패스키", "Synced passkey", ("보관함 복사본.", "The locker copy."), ("iCloud 키체인, Google 비밀번호 관리자. 새 휴대폰에서도 반지가 그대로.", "iCloud Keychain, Google Password Manager. The ring follows you to a new phone.")),
        ("하드웨어 키", "Security key", ("뽑아 쓰는 반지.", "A ring you plug in."), ("YubiKey 같은 작은 막대. 복사가 안 돼서 제일 튼튼해요.", "A small stick like a YubiKey. Can't be copied, so it's the sturdiest.")),
        ("피싱 내성", "Phishing-resistant", ("가짜 성문에 안 켜짐.", "Dark at a fake gate."), ('성 이름이 반지에 새겨져 있어서요. → <a href="attack-ko.html">백과사전의 T1566</a>', 'Because the castle\'s name is engraved in the ring. → <a href="attack-en.html">T1566 in the encyclopedia</a>')),
    ],
}
