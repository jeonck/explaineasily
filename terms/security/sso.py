from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
CASTLES = ("⟦사진 성|Photo Castle⟧", "⟦편지 성|Mail Castle⟧", "⟦회의 성|Meeting Castle⟧")


def castles(y=90, s=0.5, marks=None, labels=True):
    out = ""
    for i, name in enumerate(CASTLES):
        x = 300 + i * 150
        out += small_castle(x, y, s)
        if labels:
            out += label(x + 80 * s, y - 8, name, 13, "var(--muted)")
        if marks:
            m = marks[i]
            cx, cy = x + 80 * s, y + 160 * s + 26
            out += ({"ok": f'<path d="M{cx - 10} {cy} l8 8 l14 -16" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>',
                     "open": label(cx, cy + 6, "⟦열림|open⟧", 13, "var(--bad)"),
                     "ask": label(cx, cy + 6, "⟦암호말은?|Password?⟧", 12, "var(--muted)")}[m])
    return out


def pass_card(x, y, s=1.0, lines=("⟦통행증|TOWN PASS⟧", "⟦지민 · 오늘까지|Jimin · today only⟧")):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="170" height="86" rx="8" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
            f'{label(78, 32, lines[0], 16, "var(--good)", cls="d")}{label(78, 62, lines[1], 13, "var(--ink)")}'
            f'<g transform="translate(140,30) rotate(-15)"><circle r="18" fill="none" stroke="var(--bad)" stroke-width="3"/><circle r="12" fill="none" stroke="var(--bad)" stroke-width="2"/>'
            f'{label(0, 4, "✓", 14, "var(--bad)")}</g></g>')


def booth(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="40" width="100" height="100" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>'
            f'<path d="M-62 40 L0 0 L62 40 Z" fill="var(--good)"/><rect x="-36" y="70" width="72" height="34" fill="var(--sky)"/>'
            f'{label(0, 160, "⟦검사소|ID booth⟧", 13, "var(--muted)")}</g>')


# 1. 성마다 문지기가 따로 묻는다
P1 = svg(300, sky(300) + castles(marks=("ask", "ask", "ask"))
         + person(70, 120, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + bubble(30, 30, 200, 60, "⟦사과? 바나나? 포도?|apple? banana? grape?⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + label(130, 275, "⟦성마다 암호말이 달라요|a different password for each castle⟧", 13, "var(--muted)"))

# 2. 귀찮으니까 다 똑같이
P2 = svg(260, '<rect width="760" height="260" fill="var(--bad-soft)"/>' + castles(y=70, marks=("open", "open", "open"))
         + person(90, 90, s=0.9, face=MASK)
         + bubble(50, 20, 110, 34, "⟦사과!|Apple!⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + label(120, 240, "⟦하나 새면 셋이 다 열려요|one leak opens all three⟧", 13, "var(--bad)"))

# 3. SSO = 한 번 확인, 통행증 (hero)
RING = '<g transform="translate(64,84)"><circle r="9" fill="none" stroke="#E9B44C" stroke-width="5"/><path d="M-5 -9 L0 -16 L5 -9 Z" fill="var(--accent)"/></g>'
TINY_GUARDS = "".join(person(300 + i * 150 + 92, 150, s=0.4, face=EYES, **GUARD) for i in range(3))
P3 = svg(340, sky(340) + booth(180, 40)
         + person(30, 150, s=0.85, **ME, extra=RING)
         + bubble(10, 60, 100, 34, "⟦사과!|Apple!⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + person(150, 150, s=0.7, face=SMILE, **GUARD)
         + pass_card(90, 250, 0.8)
         + castles(y=60, marks=("ok", "ok", "ok"), labels=False) + TINY_GUARDS
         + "".join(f'<path d="M230 285 Q{300 + i * 150 + 40} 300 {300 + i * 150 + 40} 165" stroke="var(--good)" stroke-width="2" stroke-dasharray="6 6" fill="none"/>' for i in range(3))
         + label(520, 320, "⟦성들은 통행증 도장만 봐요|the castles only check the stamp⟧", 14, "var(--muted)"))

# 4. 통행증 하나로 모든 성
P4 = svg(270, sky(270) + castles(y=60, marks=("ok", "ok", "ok"))
         + person(60, 110, s=0.9, **ME) + pass_card(110, 140, 0.7)
         + '<path d="M240 200 L290 200" stroke="var(--good)" stroke-width="3"/><path d="M280 190 L292 200 L280 210" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + '<g transform="translate(680,200)"><circle r="26" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -16 V0 L10 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(680, 250, "⟦오늘까지|today only⟧", 13, "var(--muted)"))

# 5. 통행증 하나면 전부 열린다
SHIELD_RING = shield(60, 40, 0.55) + '<g transform="translate(110,190)"><circle r="12" fill="none" stroke="#E9B44C" stroke-width="6"/><path d="M-6 -12 L0 -21 L6 -12 Z" fill="var(--accent)"/></g>'
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(40, 80, s=0.9, face=MASK + SWEAT) + pass_card(110, 100, 0.6)
         + "".join(small_castle(x, 180, 0.3) + label(x + 24, 180 + 48 + 22, "⟦열림|open⟧", 11, "var(--bad)") for x in (200, 260, 320))
         + label(190, 275, "⟦통행증을 훔치면 전부 열려요|steal the pass, everything opens⟧", 13, "var(--bad)")
         + f'<g transform="translate(420,0)">{SHIELD_RING}</g>' + booth(620, 50, 0.9)
         + label(570, 275, "⟦그래서 검사소는 반지까지 확인해요|so the booth checks the ring too⟧", 13, "var(--good)"))

BOOTH_I = icon('<path d="M8 28 L32 10 L56 28 Z" fill="var(--good)"/><rect x="14" y="28" width="36" height="26" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>')
PASS_I = icon('<rect x="8" y="18" width="48" height="30" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><circle cx="44" cy="30" r="7" fill="none" stroke="var(--bad)" stroke-width="2"/><rect x="14" y="26" width="18" height="3" fill="var(--line)"/><rect x="14" y="34" width="14" height="3" fill="var(--line)"/>')
CASTLES_I = icon('<rect x="6" y="30" width="16" height="24" fill="var(--stone-dark)"/><rect x="24" y="24" width="16" height="30" fill="var(--stone-dark)"/><rect x="42" y="32" width="16" height="22" fill="var(--stone-dark)"/><rect x="6" y="24" width="5" height="6" fill="var(--stone-dark)"/><rect x="17" y="24" width="5" height="6" fill="var(--stone-dark)"/><rect x="24" y="18" width="5" height="6" fill="var(--stone-dark)"/><rect x="35" y="18" width="5" height="6" fill="var(--stone-dark)"/><rect x="42" y="26" width="5" height="6" fill="var(--stone-dark)"/><rect x="53" y="26" width="5" height="6" fill="var(--stone-dark)"/>')

PAGE = {
    "slug": "sso", "order": 15,
    "title": ("마을 통행증", "The Town Pass"),
    "h1": ("<em>SSO</em>가 뭐예요?", "What is <em>SSO</em>?"),
    "sub": ("통합 로그인(Single Sign-On)을 마을 통행증 이야기로 풀어봤어요.",
            "Single Sign-On, told as a story about one pass for the whole town."),
    "panels": [
        {"svg": P1, "alt": ("사진 성, 편지 성, 회의 성이 각각 '암호말은?' 하고 묻고, 방문객은 '사과? 바나나? 포도?' 하며 땀을 흘림", "Photo, Mail and Meeting castles each ask for a password; the visitor sweats: apple? banana? grape?"),
         "caption": ("성마다 문지기가 따로 물어요.", "Every castle has its own gatekeeper asking."),
         "small": ("성이 셋이면 암호말도 셋. 자꾸 헷갈려요.", "Three castles, three passwords. Easy to mix up.")},
        {"svg": P2, "alt": ("도둑이 '사과!' 한마디로 세 성을 다 열고 있음", "A thief says 'Apple!' once and all three castles open"),
         "caption": ("귀찮으니까 다 똑같이 해요.", "So people make them all the same."),
         "small": ('하나가 새면 셋이 다 열려요. <a href="mfa-ko.html">문지기 이야기</a>에서 본 그 문제예요.',
                   'One leak opens all three — the problem from the <a href="mfa-en.html">gatekeeper story</a>.')},
        {"svg": P3, "hero": True, "alt": ("마을 입구 검사소에서 방문객이 암호말과 반지로 확인받고 통행증을 받음. 세 성의 작은 문지기들은 통행증 도장만 확인", "At the town's ID booth the visitor is checked with password and ring and gets a pass; tiny guards at three castles just check the stamp"),
         "caption": ("SSO는 한 번 확인하고 통행증을 줘요.", "SSO checks you once and hands you a pass."),
         "small": ("마을 입구에서 한 번 제대로(반지까지) 확인해요. 성들은 통행증 도장만 봐요.", "One thorough check (ring included) at the town entrance. The castles only look at the stamp."),
         "tricks": (3, [
             (BOOTH_I, ("검사소", "The ID booth"), ("누구인지 확인하는 한 곳", "the one place that checks who you are"), "calm"),
             (PASS_I, ("통행증", "The pass"), ("검사소 도장이 찍힌 카드", "a card with the booth's stamp"), "warm"),
             (CASTLES_I, ("성들", "The castles"), ("도장만 믿고 열어줘요", "trust the stamp and open")),
         ])},
        {"svg": P4, "alt": ("방문객이 통행증을 들고 세 성에 체크 표시를 받으며 지나가고, 시계에 '오늘까지'", "The visitor walks past three castles with the pass, each showing a check; a clock says today only"),
         "caption": ("통행증 하나로 모든 성에 들어가요.", "One pass opens every castle."),
         "small": ("성마다 다시 묻지 않아요. 통행증엔 '오늘까지'가 적혀 있고, 검사소에서 취소하면 한꺼번에 닫혀요.", "No castle asks again. The pass says today only, and cancelling it at the booth shuts every castle at once.")},
        {"svg": P5, "alt": ("왼쪽: 도둑이 통행증을 들고 세 성을 다 엶. 오른쪽: 방패와 반지로 튼튼해진 검사소", "Left: a thief with the pass opens all three castles. Right: the booth, reinforced with a shield and a ring"),
         "caption": ("통행증 하나면 전부 열려요.", "One pass opens everything — for anyone."),
         "small": ('편한 만큼 위험해요. 그래서 검사소는 <a href="mfa-ko.html">반지까지 확인</a>하고, 통행증엔 짧은 시간만 적어요.',
                   'As risky as it is convenient. So the booth <a href="mfa-en.html">checks the ring too</a>, and the pass is short-lived.')},
    ],
    "summary": (("<b>SSO</b> = 마을 입구에서 <b>한 번</b> 확인받고, 그 <b>통행증</b>으로 모든 성에 들어가는 것.",
                 "<b>SSO</b> = get checked <b>once</b> at the town entrance, then enter every castle with that <b>pass</b>."),
                ("Single Sign-On. '회사 계정으로 로그인'이 이거예요. OAuth의 표가 '이 방 들어가도 됨'이라면, SSO의 통행증은 '이 사람이 나'예요.",
                 "Single Sign-On — the thing behind 'Sign in with your work account'. Where OAuth's ticket says 'may enter this room', the SSO pass says 'this is me'.")),
    "glossary": [
        ("신분 확인소", "Identity Provider (IdP)", ("마을 입구 검사소.", "The town's ID booth."), ("Okta, Microsoft Entra ID, Google 같은 곳. 누구인지 확인하는 유일한 곳.", "Okta, Microsoft Entra ID, Google. The one place that checks who you are.")),
        ("서비스 제공자", "Service Provider (SP)", ("성.", "A castle."), ("통행증 도장을 믿고 열어주는 앱. 릴라잉 파티(relying party)라고도 해요.", "An app that trusts the stamp and opens. Also called a relying party.")),
        ("통행증", "Token / assertion", ("도장 찍힌 카드.", "The stamped card."), ("검사소가 '이 사람이 나'라고 적어준 것.", "The booth's written word that this is me.")),
        ("서명", "Signature", ("도장.", "The stamp."), ("검사소만 찍을 수 있어서 성이 위조를 알아봐요.", "Only the booth can make it, so castles can spot a fake.")),
        ("세션", "Session", ("오늘까지.", "Today only."), ("통행증이 살아 있는 시간. 지나면 검사소로 다시 가요.", "How long the pass lives. After that, back to the booth.")),
        ("단일 로그아웃", "Single logout", ("검사소에서 취소.", "Cancel at the booth."), ("한 번 취소하면 모든 성이 한꺼번에 닫혀요.", "One cancellation shuts every castle at once.")),
        ("SAML · OIDC", "SAML · OpenID Connect", ("통행증 양식 둘.", "Two pass formats."), ('오래된 양식(SAML)과 새 양식(OIDC). 새 양식은 <a href="oauth-ko.html">OAuth</a> 위에 얹혀 있어요.', 'The older form (SAML) and the newer one (OIDC), which sits on top of <a href="oauth-en.html">OAuth</a>.')),
        ("페더레이션", "Federation", ("옆 마을 통행증도 믿기.", "Trusting the next town's pass."), ("두 검사소가 서로 도장을 인정하는 약속.", "Two booths agreeing to honor each other's stamps.")),
    ],
}
