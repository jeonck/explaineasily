from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
PW = "⟦사과!|Apple!⟧"


def ring(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="14" fill="none" stroke="#E9B44C" stroke-width="7"/>'
            f'<path d="M-7 -14 L0 -24 L7 -14 Z" fill="var(--accent)"/></g>')


def phone(x, y, code, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-46" width="52" height="92" rx="8" fill="var(--night)"/>'
            f'<rect x="-20" y="-36" width="40" height="66" rx="3" fill="var(--panel)"/>{label(0, 2, code, 13, "#142033")}</g>')


def bush(x, y):
    return (f'<g transform="translate({x},{y})"><ellipse cx="50" cy="90" rx="60" ry="34" fill="#173A2E"/>'
            f'<circle cx="50" cy="60" r="22" fill="{SKIN}"/><circle cx="42" cy="58" r="4" fill="#111C30"/><circle cx="58" cy="58" r="4" fill="#111C30"/>'
            f'<path d="M6 22 Q30 -6 54 22 Z" fill="var(--bad)" transform="translate(20,20)"/></g>')


def sticky(x, y, text, rot=-6):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect width="90" height="80" fill="#FFE97A"/>'
            f'<rect x="30" y="-6" width="30" height="12" fill="var(--line)" fill-opacity="0.8"/>{label(45, 50, text, 18, "#142033", cls="d")}</g>')


# 1. 옛날 문지기는 암호말만 물었다
P1 = svg(300, sky(300) + gate(260, 60) + person(230, 150, s=0.8, face=EYES, **GUARD)
         + bubble(150, 20, 150, 34, "⟦암호말은?|Password?⟧", 14, "var(--panel)", "var(--good)", "bottom")
         + person(80, 150, s=0.8, **ME) + bubble(40, 84, 100, 34, PW, 15, "var(--panel)", "var(--line)", "bottom")
         + bush(520, 100) + label(570, 265, "⟦엿들어요|listening⟧", 14, "var(--bad)"))

# 2. 암호말은 자꾸 샌다
P2 = svg(270, '<rect width="760" height="270" fill="var(--bad-soft)"/>'
         + sticky(60, 60, "⟦사과|apple⟧") + label(105, 190, "⟦종이에 적어두고|written on a note⟧", 13, "var(--muted)")
         + small_castle(280, 60, 0.45) + small_castle(370, 60, 0.45) + small_castle(460, 60, 0.45)
         + "".join(label(x + 36, 150, "⟦사과|apple⟧", 12, "var(--bad)") for x in (280, 370, 460))
         + label(406, 190, "⟦다른 성에서도 똑같이|the same one everywhere⟧", 13, "var(--muted)")
         + '<g transform="translate(640,110)"><path d="M-20 -30 q30 -20 40 10 q6 20 -12 26 q-14 4 -14 -8" stroke="var(--night)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M-30 -10 a30 30 0 0 0 -8 30" stroke="var(--night)" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
         + label(640, 190, "⟦옆에서 들어요|overheard⟧", 13, "var(--muted)"))

# 3. MFA = 다른 종류로 두 번 이상 (hero)
FACE_CHIP = f'<circle cx="16" cy="16" r="12" fill="{SKIN}"/><path d="M4 12 Q16 -2 28 12 Z" fill="#4A5A72"/><circle cx="12" cy="16" r="1.8" fill="var(--night)"/><circle cx="20" cy="16" r="1.8" fill="var(--night)"/>'
P3 = svg(340, sky(340) + gate(560, 70) + person(520, 160, s=0.85, face=EYES, **GUARD)
         + bubble(380, 20, 180, 34, "⟦① 암호말은?|① Password?⟧", 14, "var(--panel)", "var(--good)", "bottom")
         + bubble(400, 70, 180, 34, "⟦② 반지는?|② Your ring?⟧", 14, "var(--panel)", "var(--good)", "bottom")
         + bubble(420, 120, 180, 34, "⟦③ 얼굴 좀 볼까요?|③ Let me see your face⟧", 13, "var(--panel)", "var(--good)", "bottom")
         + person(120, 160, s=0.85, **ME)
         + bubble(60, 60, 100, 34, PW, 15, "var(--panel)", "var(--line)", "bottom")
         + ring(200, 250, 1.1) + f'<g transform="translate(240,232)">{FACE_CHIP}</g>'
         + label(380, 320, "⟦하나가 새도, 나머지가 막아요|one can leak; the others still hold⟧", 14, "var(--muted)"))

# 4. 암호말을 훔쳐도 반지는 없다
P4 = svg(280, sky(280) + gate(560, 40) + person(520, 130, s=0.85, face=EYES, **GUARD)
         + bubble(410, 10, 160, 34, "⟦반지는요?|And your ring?⟧", 14, "var(--panel)", "var(--good)", "bottom")
         + person(140, 130, s=0.85, face=MASK + SWEAT)
         + bubble(90, 30, 100, 34, PW, 15, "var(--panel)", "var(--line)", "bottom")
         + '<g transform="translate(240,215)"><circle r="14" fill="none" stroke="var(--line)" stroke-width="4" stroke-dasharray="5 5"/></g>'
         + label(240, 255, "⟦반지가 없어요|no ring⟧", 13, "var(--bad)")
         + '<path d="M330 120 l60 60 M390 120 l-60 60" stroke="var(--bad)" stroke-width="10" stroke-linecap="round"/>')

# 5. 가짜 성문엔 반지도 속는다
FAKE_GATE = ('<g transform="translate(560,70)"><rect x="-70" y="30" width="140" height="90" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"/>'
             + battlements(-70, 10, 140, 4, "var(--stone)", 20)
             + '<path d="M-28 120 V78 a28 28 0 0 1 56 0 V120 Z" fill="var(--night)"/>'
             '<rect x="60" y="40" width="10" height="90" fill="#8B5E3C" transform="rotate(-20 65 85)"/>'
             + label(0, 150, "⟦가짜 성문|fake gate⟧", 13, "var(--bad)") + "</g>")
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         # 왼쪽: 암호말 둘 = 여전히 하나
         + bubble(40, 40, 110, 34, "⟦사과|apple⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + bubble(170, 40, 130, 34, "⟦바나나|banana⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + label(190, 130, "= 1", 40, "var(--accent)", cls="d")
         + label(190, 170, "⟦암호말 둘은 두 번이 아니에요|two passwords aren\'t two factors⟧", 13, "var(--muted)")
         + label(190, 190, "⟦같은 종류니까요|they\'re the same kind⟧", 13, "var(--muted)")
         # 오른쪽: 가짜 성문
         + FAKE_GATE + person(640, 100, s=0.6, face=MASK, extra=phone(90, 40, "482 913", 0.5))
         + person(420, 130, s=0.8, **ME) + bubble(400, 60, 120, 34, "482 913", 15, "var(--panel)", "var(--line)", "bottom")
         + label(470, 275, "⟦코드를 불러주면 도둑이 진짜 성문에 써요|read the code aloud and the thief uses it at the real gate⟧", 12, "var(--muted)"))

KNOW_I = icon('<path d="M12 40 Q8 18 30 16 Q54 14 52 32 L42 34 L46 50 L30 40 Z" fill="var(--good)"/>')
HAVE_I = icon('<circle cx="32" cy="36" r="14" fill="none" stroke="#E9B44C" stroke-width="7"/><path d="M25 22 L32 10 L39 22 Z" fill="var(--accent)"/>')
ARE_I = icon(f'<circle cx="32" cy="28" r="14" fill="{SKIN}"/><path d="M18 22 Q32 6 46 22 Z" fill="var(--bad)"/><circle cx="27" cy="28" r="2" fill="var(--night)"/><circle cx="37" cy="28" r="2" fill="var(--night)"/><path d="M26 36 Q32 41 38 36" stroke="var(--night)" stroke-width="2" fill="none"/>')

PAGE = {
    "slug": "mfa", "order": 14,
    "title": ("세 번 확인하는 문지기", "The Gatekeeper's Three Questions"),
    "h1": ("<em>MFA</em>가 뭐예요?", "What is <em>MFA</em>?"),
    "sub": ("다중 인증(Multi-Factor Authentication)을 세 가지로 확인하는 문지기 이야기로 풀어봤어요.",
            "Multi-Factor Authentication, told as a story about a gatekeeper who asks three different questions."),
    "panels": [
        {"svg": P1, "alt": ("문지기가 '암호말은?' 하고 묻고 방문객이 '사과!' 하고 답하는데, 덤불 뒤에서 도둑이 엿듣고 있음", "A gatekeeper asks 'Password?', the visitor says 'Apple!', and a thief listens from behind a bush"),
         "caption": ("옛날 문지기는 암호말만 물었어요.", "The old gatekeeper only asked for the password."),
         "small": ("암호말은 훔쳐 들을 수 있어요.", "A password can be overheard.")},
        {"svg": P2, "alt": ("'사과'라고 적힌 메모지, 똑같이 '사과'를 쓰는 작은 성 세 개, 그리고 귀", "A sticky note reading 'apple', three small castles all using 'apple', and an ear"),
         "caption": ("암호말은 자꾸 새요.", "Passwords keep leaking."),
         "small": ("종이에 적어두고, 다른 성에서도 똑같이 쓰고, 옆에서 들어요.", "Written on notes, reused at every castle, overheard.")},
        {"svg": P3, "hero": True, "alt": ("문지기가 ① 암호말은? ② 반지는? ③ 얼굴 좀 볼까요? 세 가지를 묻고, 방문객은 암호말과 반지와 얼굴을 보여줌", "The gatekeeper asks ① Password? ② Your ring? ③ Let me see your face; the visitor shows a password, a ring and a face"),
         "caption": ("MFA는 서로 다른 종류로 두 번 이상 물어요.", "MFA asks two or more questions of different kinds."),
         "small": ("아는 것, 가진 것, 나인 것. 하나가 새도 나머지가 막아요.", "Something you know, something you have, something you are. One can leak; the others still hold."),
         "tricks": (3, [
             (KNOW_I, ("아는 것", "Something you know"), ("암호말", "a password"), "calm"),
             (HAVE_I, ("가진 것", "Something you have"), ("성에서 준 반지, 휴대폰", "a ring from the castle, your phone"), "warm"),
             (ARE_I, ("나인 것", "Something you are"), ("얼굴, 지문", "your face, your fingerprint")),
         ])},
        {"svg": P4, "alt": ("가면 쓴 도둑이 '사과!'라고 말하지만 문지기가 '반지는요?' 하고 묻고, 도둑 손엔 반지가 없어 큰 X", "A masked thief says 'Apple!', the gatekeeper asks 'And your ring?', the thief has none — big X"),
         "caption": ("암호말을 훔쳐도 반지는 없어요.", "Steal the password, and you still have no ring."),
         "small": ("두 가지를 한꺼번에 훔치는 건 훨씬 어려워요.", "Stealing two different things at once is much harder.")},
        {"svg": P5, "alt": ("왼쪽: '사과'와 '바나나' 두 암호말이 = 1. 오른쪽: 골판지 가짜 성문 뒤의 도둑에게 방문객이 코드 482 913을 불러줌", "Left: passwords 'apple' and 'banana' equal 1. Right: a visitor reads code 482 913 aloud to a thief behind a cardboard fake gate"),
         "caption": ("가짜 성문엔 반지도 속아요.", "Even the ring can be fooled by a fake gate."),
         "small": ("코드를 불러주면 도둑이 그 코드로 진짜 성문을 지나요. 그래서 요즘 반지는 성문을 직접 알아봐요(패스키).", "Read the code aloud and the thief uses it at the real gate. That's why newer rings recognize the gate themselves (passkeys).")},
    ],
    "summary": (("<b>MFA</b> = 문지기가 <b>서로 다른 종류</b>로 두 번 이상 확인하는 것. 아는 것, 가진 것, 나인 것.",
                 "<b>MFA</b> = the gatekeeper checks two or more things <b>of different kinds</b>: know, have, are."),
                ("Multi-Factor Authentication. 두 가지만 쓰면 2단계 인증(2FA). 문자로 오는 6자리 숫자가 제일 흔한 '가진 것'이고, 패스키는 가짜 성문에 안 속는 반지예요.",
                 "Multi-Factor Authentication. With exactly two, it's 2FA. A texted 6-digit code is the most common 'have'; a passkey is a ring that can't be fooled by a fake gate.")),
    "glossary": [
        ("지식 요소", "Something you know", ("암호말.", "The password."), ("머릿속에만 있는 것. 새기 제일 쉬워요.", "Lives only in your head. Leaks the easiest.")),
        ("소유 요소", "Something you have", ("반지.", "The ring."), ("휴대폰, 인증 앱, 보안키. 훔치려면 물건을 가져가야 해요.", "Your phone, an authenticator app, a security key. To steal it, they need the object.")),
        ("생체 요소", "Something you are", ("얼굴, 지문.", "Face, fingerprint."), ("몸에 붙어 있어요. 바꿀 수 없다는 게 장점이자 단점.", "Attached to you. Can't be changed — a strength and a weakness.")),
        ("2FA", "2FA", ("두 가지.", "Two of them."), ("MFA 중에 딱 두 종류만 쓰는 것.", "MFA with exactly two kinds.")),
        ("OTP", "One-time password", ("한 번 쓰고 버리는 숫자.", "A number used once."), ("반지가 매번 새로 만들어요. 30초마다 바뀌거나, 문자로 와요.", "The ring makes a fresh one each time — every 30 seconds, or by text.")),
        ("피싱", "Phishing", ("가짜 성문.", "The fake gate."), ('진짜처럼 생긴 문 앞에서 암호말과 코드를 받아 적어요. → <a href="attack-ko.html">백과사전의 T1566</a>', 'A door that looks real, collecting your password and code. → <a href="attack-en.html">T1566 in the encyclopedia</a>')),
        ("패스키", "Passkey (FIDO2)", ("성문을 알아보는 반지.", "A ring that knows the gate."), ("진짜 성문에서만 열려요. 가짜 앞에선 아예 반응하지 않아요.", "Only works at the real gate. Does nothing at a fake one.")),
        ("MFA 피로", "MFA fatigue", ("자꾸 물어서 아무 때나 '네'.", "Asked so often you just say yes."), ("도둑이 밤새 반지를 울리면, 잠결에 '네'를 눌러요.", "A thief rings the ring all night until you tap yes half asleep.")),
    ],
}
