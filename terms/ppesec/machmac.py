from _draw import *

SENDER = dict(hat=None, shirt="#4A7A6A", face=SMILE)
RECEIVER = dict(hat="var(--good)", shirt="var(--good)")
FORGER = dict(hat="var(--bad)", face=MASK)


def note(x, y, s=1.0, mark=None):
    m = ""
    if mark == "fingerprint":
        m = '<g transform="translate(14,16)" fill="none" stroke="var(--night)" stroke-width="2" stroke-linecap="round"><path d="M-3 4 a3 3 0 0 1 6 0 v4"/><path d="M-7 4 a7 7 0 0 1 14 0 v6"/></g>'
    elif mark == "seal":
        m = '<circle cx="14" cy="16" r="9" fill="#E9B44C"/><path d="M10 16 l3 3 l6 -7" stroke="var(--night)" stroke-width="2" fill="none" stroke-linecap="round"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-20" width="52" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/>'
            + '<path d="M-16 -8 h32 M-16 0 h22" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' + m + "</g>")


def stampmold(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-6" width="28" height="30" rx="3" fill="#8B5E3C"/>'
            + '<circle cy="-14" r="12" fill="#E9B44C"/><path d="M-6 -14 l4 4 l8 -9" stroke="var(--night)" stroke-width="2.5" fill="none" stroke-linecap="round"/></g>')


# 1. 지문만 찍어 보냈어요
P1 = svg(320, sky(320)
         + person(170, 130, s=0.85, **SENDER) + note(290, 150, 1.1, mark="fingerprint")
         + label(290, 210, "⟦지문(해시)만 찍었어요|just stamped a fingerprint (hash)⟧", 11, "var(--muted)")
         + '<path d="M360 150 h100" stroke="var(--line)" stroke-width="3" stroke-dasharray="5 5"/>'
         + person(600, 130, s=0.85, face=EYES, **RECEIVER)
         + label(380, 40, "⟦내용이 안 바뀌었나 지문으로 확인하려고 해요|trying to confirm nothing changed, using just the fingerprint⟧", 13, "var(--ink)", cls="d"))

# 2. 아무나 지문을 다시 찍을 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.75, **FORGER) + note(290, 130, 1.0, mark="fingerprint")
         + label(290, 190, "⟦내용을 바꾸고|changes the content⟧", 10, "var(--bad)")
         + '<path d="M340 130 h40" stroke="var(--bad)" stroke-width="3"/>'
         + note(440, 130, 1.0, mark="fingerprint") + label(440, 190, "⟦지문도 새로 찍어요|and re-stamps a matching fingerprint⟧", 10, "var(--bad)")
         + person(600, 150, s=0.75, face=EYES, **RECEIVER) + bubble(560, 40, 190, 36, "⟦지문은 맞는데… 누가 보냈지?|the fingerprint matches… but who sent this?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦지문은 비밀이 필요 없어서, 바꾼 사람도 다시 찍을 수 있어요|a fingerprint needs no secret — so a forger can simply restamp a new one⟧", 11, "var(--ink)", cls="d"))

# 3. MAC/HMAC = 비밀 도장틀로 찍는 확인 도장 (hero)
P3 = svg(340, sky(340)
         + person(150, 130, s=0.8, **SENDER) + stampmold(150, 210, 0.9) + label(150, 260, "⟦비밀 도장틀|the secret mold⟧", 11, "var(--muted)")
         + note(330, 150, 1.1, mark="seal") + label(330, 210, "⟦내용 + 도장틀로 찍어요|stamped using the content + the mold⟧", 11, "var(--muted)")
         + '<path d="M400 150 h100" stroke="var(--good)" stroke-width="3" stroke-dasharray="5 5"/>'
         + person(600, 130, s=0.8, face=EYES, **RECEIVER) + stampmold(600, 210, 0.9) + label(600, 260, "⟦같은 도장틀로 다시 찍어 비교|re-stamps with the same mold to compare⟧", 10, "var(--good)")
         + label(380, 320, "⟦MAC/HMAC = 비밀 도장틀 없인 아무도 못 찍는 확인 도장|MAC/HMAC = a seal nobody can stamp without the secret mold⟧", 13, "var(--ink)", cls="d"))

MOLD_I = icon('<rect x="18" y="20" width="28" height="30" rx="3" fill="#8B5E3C"/><circle cx="32" cy="12" r="10" fill="#E9B44C"/>')
COMBINE_I = icon('<rect x="8" y="24" width="20" height="18" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><circle cx="48" cy="33" r="10" fill="#E9B44C"/><path d="M30 33 h10" stroke="var(--ink)" stroke-width="3"/>')
NOFORGE_I = icon('<path d="M10 32 q22 -20 44 0 q-22 20 -44 0z" fill="none" stroke="var(--muted)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--muted)"/><path d="M12 14 L52 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
SHARE_I = icon('<circle cx="20" cy="32" r="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="44" cy="32" r="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><path d="M26 24 l12 16 M38 24 l-12 16" stroke="var(--good)" stroke-width="2"/>')

PAGE = {
    "slug": "machmac", "order": 19,
    "title": ("비밀 도장틀로 찍는 확인 도장", "The Confirmation Seal Stamped with a Secret Mold"),
    "h1": ("<em>MAC/HMAC</em>이 뭐예요?", "What is a <em>MAC/HMAC</em>?"),
    "sub": ("메시지 인증 코드(MAC/HMAC)를, 보낸 사람과 받는 사람만 가진 비밀 도장틀로 찍는 확인 도장 이야기로 풀어봤어요.",
            "A Message Authentication Code (MAC/HMAC), told as a story about a confirmation seal stamped with a secret mold only the sender and receiver hold."),
    "panels": [
        {"svg": P1, "alt": ("보낸 사람이 쪽지에 지문(해시)만 찍어 보내고, 받는 사람이 그걸로 확인하려 함", "A sender stamps a note with just a fingerprint (hash) and sends it, and the receiver tries to use that to confirm it"),
         "caption": ("지문(해시)만 찍어 보냈어요.", "Just a fingerprint (a hash) was stamped on."),
         "small": ('<a href="hashing-ko.html">지문</a>은 내용이 안 바뀌었는지는 보여주지만, 그게 다예요.', 'A <a href="hashing-en.html">fingerprint</a> shows the content didn\'t change — but that\'s all it shows.')},
        {"svg": P2, "alt": ("위조자가 쪽지 내용을 바꾸고 지문을 새로 찍어 다시 보내고, 받는 사람은 지문은 맞는데 누가 보냈는지 모르겠다고 말함", "A forger changes the note's content and re-stamps a matching fingerprint, and the receiver says the fingerprint matches but doesn't know who really sent it"),
         "caption": ("아무나 지문을 다시 찍을 수 있어요.", "Anyone can simply re-stamp the fingerprint."),
         "small": ("지문은 비밀이 필요 없는 셈이라, 내용을 바꾼 사람도 새 지문을 똑같이 만들 수 있어요.", "A fingerprint needs no secret to compute — so whoever changes the content can make a matching one too.")},
        {"svg": P3, "hero": True, "alt": ("보낸 사람과 받는 사람이 같은 비밀 도장틀을 가지고, 내용과 도장틀을 합쳐 찍은 도장을 서로 다시 찍어보며 비교함", "The sender and receiver each hold the same secret mold, stamping a seal made from the content plus the mold, and comparing by re-stamping it"),
         "caption": ("MAC/HMAC은 비밀 도장틀로 찍는 확인 도장이에요.", "MAC/HMAC is a confirmation seal stamped with a secret mold."),
         "small": ('도장틀(비밀 열쇠) 없인 아무도 맞는 도장을 못 찍어요. → <a href="hashing-ko.html">지문</a>에 비밀을 더한 것이라고 보면 돼요.',
                   'Without the mold (the secret key), nobody can stamp a matching seal. → think of it as a <a href="hashing-en.html">fingerprint</a> with a secret added in.'),
         "tricks": (4, [
             (MOLD_I, ("비밀 도장틀이 필요해요", "Needs the secret mold"), ("보낸 사람과 받는 사람만 가져요", "only the sender and receiver hold it"), "calm"),
             (COMBINE_I, ("내용 + 도장틀로 찍어요", "Content + mold, stamped together"), ("HMAC = 지문 + 비밀 열쇠", "HMAC = a hash combined with a secret key")),
             (NOFORGE_I, ("도장틀 없인 위조 불가", "No mold, no forging"), ("지문만 바꿔선 안 맞아요", "re-stamping alone won't match"), "warm"),
             (SHARE_I, ("받는 쪽도 같은 틀이 있어야 해요", "The receiver needs the same mold too"), ("미리 나눠 가져야 해요", "it must be shared beforehand")),
         ])},
        {"svg": svg(340, sky(340)
                    + '<rect x="30" y="30" width="700" height="260" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="700" height="34" rx="8" fill="#C9A86A"/>'
                    + label(140, 53, "⟦도구|tool⟧", 13, "#142033", cls="d") + label(330, 53, "⟦지키는 것|what it protects⟧", 13, "#142033", cls="d") + label(560, 53, "⟦누가 만들 수 있나|who can make it⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M30 {64 + i * 75} h700" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(140, 100, "⟦지문(해시)|fingerprint (hash)⟧", 12, "#142033", cls="d") + label(330, 100, "⟦안 바뀌었나만|only that it's unchanged⟧", 11, "#142033") + label(560, 100, "⟦아무나|anyone⟧", 11, "var(--bad)")
                    + label(140, 175, "⟦비밀 도장(MAC/HMAC)|secret seal (MAC/HMAC)⟧", 12, "#142033", cls="d") + label(330, 175, "⟦안 바뀌었나 + 누가 보냈나|unchanged + who really sent it⟧", 11, "#142033") + label(560, 175, "⟦도장틀 가진 사람만|only whoever holds the mold⟧", 11, "var(--good)")
                    + label(140, 250, "⟦봉인 편지(암호화)|sealed letter (encryption)⟧", 12, "#142033", cls="d") + label(330, 250, "⟦남이 못 읽게만|only that nobody else can read it⟧", 11, "#142033") + label(560, 250, "⟦열쇠 가진 사람만|only whoever holds the key⟧", 11, "#142033")),
         "alt": ("표: 지문(해시) — 안 바뀌었나만 / 아무나 계산 가능, 비밀도장(MAC/HMAC) — 변조+발신자 확인 / 도장틀 가진 사람만, 봉인편지(암호화) — 기밀성 / 열쇠 가진 사람만", "Table: fingerprint (hash) — only unchanged / anyone can compute it, secret seal (MAC/HMAC) — unchanged + sender / only the mold holder, sealed letter (encryption) — confidentiality / only the key holder"),
         "caption": ("셋을 나란히 보면 이래요.", "Side by side, here's the difference."),
         "small": ('<a href="hashing-ko.html">지문</a>·비밀 도장·<a href="encryption-ko.html">봉인 편지</a>는 서로 다른 약속을 지켜요. 하나가 다른 걸 대신하지 않아요.',
                   'A <a href="hashing-en.html">fingerprint</a>, a secret seal, and a <a href="encryption-en.html">sealed letter</a> each keep a different promise — none stands in for another.')},
        {"svg": svg(320, sky(320)
                    + person(190, 125, s=0.85, **SENDER) + stampmold(240, 185, 0.7)
                    + label(190, 270, "⟦둘 다 미리 도장틀을 나눠 가져야 해요|both sides must already share the mold, in advance⟧", 11, "var(--ink)")
                    + person(560, 125, s=0.85, face=EYES, **RECEIVER)
                    + label(560, 270, "⟦'내가 안 찍었다'는 말은 못 막아요|can't rule out either side later claiming I never stamped this⟧", 11, "var(--bad)")
                    + label(380, 305, "⟦제3자 증명이 필요하면 왕의 도장(PKI 서명)을 써요|for proof a third party can check, use the king's seal (PKI signing) instead⟧", 12, "var(--ink)", cls="d")),
         "alt": ("비밀 도장틀을 미리 나눠 가져야 하고, 부인 방지는 안 되며, 제3자 증명이 필요하면 PKI 서명을 씀", "Both sides must already share the secret mold, and it can't prevent either side from denying they stamped it; a third-party proof needs PKI signing instead"),
         "caption": ("도장틀을 미리 나눠야 하고, 부인은 못 막아요.", "The mold must be shared in advance, and it can't stop denial."),
         "small": ('열쇠를 미리 나누는 문제가 남고, 제3자가 증명할 증거(부인 방지)가 필요하면 <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>(디지털 서명)을 써요.',
                   'The key-distribution problem remains, and if you need proof a third party can verify (non-repudiation), use <a href="pki-en.html">the badge with the king\'s seal</a> (a digital signature) instead.')},
    ],
    "summary": (("<b>MAC/HMAC</b> = 보낸 사람과 받는 사람만 가진 <b>비밀 도장틀</b>로 메시지 위에 찍는 확인 도장. 틀 없인 아무도 못 찍어서, <b>안 바뀌었는지</b>와 <b>진짜 보냈는지</b>를 같이 증명해요.",
                 "<b>MAC/HMAC</b> = a confirmation seal stamped on a message using a <b>secret mold</b> that only the sender and receiver hold. Without the mold nobody can stamp it, so it proves both <b>it's unchanged</b> and <b>who really sent it</b>."),
                ("Message Authentication Code(MAC), 그중 해시 함수를 쓰는 방식이 HMAC(Hash-based MAC)이에요. 메시지와 공유 비밀키를 함께 해시해 태그를 만들고, 같은 키를 가진 수신자만 같은 태그를 재계산해 검증할 수 있어요. 해시(지문)는 무결성만 지키지만, MAC은 무결성과 발신자 인증을 함께 지켜요. 다만 키를 사전에 공유해야 하고, 부인 방지는 제공하지 않아요 — 그건 공개키 기반 전자서명(PKI)의 몫이에요.",
                 "A Message Authentication Code (MAC) — and HMAC, the hash-based variant — hashes the message together with a shared secret key to produce a tag; only a receiver holding the same key can recompute and verify the same tag. A plain hash (a fingerprint) protects integrity alone, while a MAC protects both integrity and sender authentication. It still requires the key to be shared beforehand, though, and it doesn't provide non-repudiation — that's the job of a public-key digital signature (PKI).")),
    "glossary": [
        ("MAC", "Message Authentication Code", ("비밀 도장틀로 찍는 확인 도장.", "A confirmation seal stamped with a secret mold."), ("메시지와 공유 비밀키로 함께 만든 태그예요.", "A tag made from the message combined with a shared secret key.")),
        ("HMAC", "HMAC", ("해시로 만드는 비밀 도장.", "A secret seal built out of a hash."), ("해시 함수를 이용해 MAC을 만드는 가장 흔한 방식이에요.", "The most common way to build a MAC, using a hash function.")),
        ("해시(지문)", "Hash (fingerprint)", ("비밀 없이 누구나 계산해요.", "Anyone can compute it, no secret needed."), ('무결성만 지켜요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>', 'It protects integrity alone. → <a href="hashing-en.html">a fingerprint on everything</a>')),
        ("무결성", "Integrity", ("몰래 못 바꾸게.", "No tampering, in secret."), ('해시도 MAC도 이걸 지켜요. → <a href="ciatriad-ko.html">지키는 것 세 가지</a>', 'Both a hash and a MAC protect this. → <a href="ciatriad-en.html">three things to keep</a>')),
        ("발신자 인증", "Sender authentication", ("정말 그 사람이 보냈는지.", "Whether it really came from them."), ("도장틀을 가진 사람만 맞는 도장을 찍을 수 있어서 증명돼요.", "Proven because only the mold's holder can stamp a matching seal.")),
        ("키 공유 문제", "Key-distribution problem", ("도장틀을 미리 나눠야 하는 숙제.", "The homework of sharing the mold beforehand."), ("MAC/HMAC이 풀지 못하는 남은 문제예요.", "The remaining problem MAC/HMAC doesn't solve.")),
        ("부인 방지", "Non-repudiation", ("'내가 안 보냈다'를 못 하게 막는 것.", "Ruling out claiming you never sent it."), ('MAC은 못 해요. 왕의 도장(서명)이 해줘요. → <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>', 'A MAC can\'t do this — the king\'s seal (a signature) can. → <a href="pki-en.html">the badge with the king\'s seal</a>')),
        ("TLS", "TLS", ("봉인 편지를 주고받는 약속.", "The promise behind a sealed back-and-forth letter."), ('실제로는 봉인(암호화)과 비밀 도장(MAC) 둘 다 같이 써요. → <a href="tls-ko.html">상점과 주고받는 봉인 약속</a>', 'In practice it runs both a seal (encryption) and a secret stamp (a MAC) together. → <a href="tls-en.html">the sealed promise with the shop</a>')),
    ],
}
