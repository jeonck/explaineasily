from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
GUEST = dict(hat=None, shirt="#4A5A72")
# 팔 + 손목 팔찌 (person 의 extra 로 씀)
ARM = f'<rect x="50" y="62" width="12" height="34" rx="6" fill="{SKIN}"/>'
ARM_BAND = ARM + '<rect x="46" y="86" width="20" height="9" rx="4" fill="var(--accent)" stroke="#142033" stroke-width="1.5"/>'
ARM_BAND_FADED = ARM + '<rect x="46" y="86" width="20" height="9" rx="4" fill="var(--accent)" opacity="0.3" stroke="#142033" stroke-width="1.5"/>'
ARM_BARE = ARM


def band(x, y, s=1.0, faded=False):
    op = ' opacity="0.3"' if faded else ""
    return (f'<g transform="translate({x},{y}) scale({s})"{op}><ellipse rx="24" ry="13" fill="none" stroke="var(--accent)" stroke-width="9"/>'
            f'<rect x="-9" y="-19" width="18" height="12" rx="3" fill="#142033"/><circle cy="-13" r="2.5" fill="#F5E6B8"/></g>')


def envelope(x, y, s=1.0, sealed=True):
    seal = '<circle cx="45" cy="30" r="9" fill="var(--bad)"/>' if sealed else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="90" height="60" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M0 0 l45 30 l45 -30" stroke="#C9A86A" stroke-width="3" fill="none"/>{seal}</g>')


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="22" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
            f'<path d="M0 -13 v13 l9 5" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def bug(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-16 -6 l-8 -8 M16 -6 l8 -8 M-18 4 h-8 M18 4 h8 M-14 12 l-6 8 M14 12 l6 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
            f'<ellipse rx="16" ry="12" fill="var(--bad)"/><circle cy="-12" r="7" fill="var(--bad)"/><circle cx="-3" cy="-13" r="1.5" fill="#FFF"/><circle cx="3" cy="-13" r="1.5" fill="#FFF"/></g>')


def scissors(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-6 -4 l30 -22 M-6 4 l30 22" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="-16" cy="-10" r="8" fill="none" stroke="var(--stone-dark)" stroke-width="4"/><circle cx="-16" cy="10" r="8" fill="none" stroke="var(--stone-dark)" stroke-width="4"/></g>')


# 1. 성문에서 얼굴을 확인하고 팔찌를 채워줘요
P1 = svg(300, sky(300)
         + gate(130, 60, 1.0) + person(220, 95, s=0.8, face=SMILE, **GUARD) + person(330, 100, s=0.85, face=SMILE, extra=ARM_BAND, **GUEST)
         + bubble(150, 22, 260, 34, "⟦얼굴 확인했어요 — 팔찌 받으세요|face checked — here\'s your wristband⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(300, 225, "⟦성문에서 한 번만 얼굴을 확인해요|the face is checked once, at the gate⟧", 12, "var(--muted)")
         + band(580, 110, 2.2) + label(580, 175, "⟦입장 팔찌|THE WRISTBAND⟧", 14, "var(--ink)", cls="d")
         + label(580, 200, "⟦이제부터는 팔찌만 보여주면 돼요|from now on, just show the band⟧", 12, "var(--muted)")
         + label(380, 280, "⟦매번 얼굴을 확인하면 줄이 너무 길어져요|checking faces every time makes the line too long⟧", 12, "var(--ink)"))

# 2. 도둑이 팔찌를 훔치거나 복사해요 — 경비는 팔찌만 봐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(55, 95, s=0.75, face=SMILE, extra=ARM_BAND, **GUEST) + person(150, 105, s=0.75, face=MASK) + band(140, 70, 0.7)
         + '<path d="M104 132 q20 -50 40 -60" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
         + label(125, 215, "⟦길에서 훔쳐봐요|peeks on the road⟧", 12, "var(--bad)") + label(125, 235, "⟦(봉인 안 된 편지)|(an unsealed letter)⟧", 10, "var(--muted)")
         + person(300, 95, s=0.75, face=FROWN, extra=ARM_BAND, **GUEST) + bug(385, 150, 1.0) + band(420, 110, 0.6)
         + label(375, 215, "⟦주머니 속 벌레가 복사해요|a bug in the pocket copies it⟧", 12, "var(--bad)")
         + gate(600, 50, 0.75) + person(555, 125, s=0.8, face=MASK, extra=ARM_BAND) + person(655, 120, s=0.7, face=SMILE, **GUARD)
         + bubble(590, 10, 160, 30, "⟦팔찌 있네요, 들어가세요|got a band? go on in⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(640, 240, "⟦얼굴은 안 봐요|no face check⟧", 12, "var(--bad)")
         + label(380, 282, "⟦팔찌만 보고 통과시키니까, 팔찌를 가진 사람이 곧 손님이에요|since only the band is checked, whoever holds it is the guest⟧", 11, "var(--muted)"))

# 3. 세션 하이재킹 = 팔찌를 훔치는 도둑 (hero)
P3 = svg(360, night(360)
         + gate(200, 80, 1.1) + person(150, 120, s=0.9, face=MASK, extra=ARM_BAND) + person(300, 110, s=0.85, face=SMILE, **GUARD)
         + label(180, 245, "⟦훔친 팔찌를 찬 도둑|a thief wearing the stolen band⟧", 12, "#C9D5E6") + label(330, 232, "⟦들어가세요!|come in!⟧", 11, "#F5E6B8")
         + person(460, 130, s=0.85, face=FROWN + SWEAT, extra=ARM_BARE, **GUEST)
         + bubble(400, 40, 220, 34, "⟦내 팔찌가 없어졌어요!|my band is gone!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(490, 245, "⟦진짜 손님은 밖에|the real guest, left outside⟧", 12, "#C9D5E6")
         + band(670, 135, 1.6) + label(670, 192, "⟦팔찌 = 통행 그 자체|the band is the pass⟧", 11, "#F5E6B8")
         + label(380, 300, "⟦팔찌를 훔치면 얼굴 확인 없이 들어와요|steal the band, and you walk in with no face check⟧", 13, "#F5E6B8", cls="d")
         + label(380, 336, "⟦경비는 팔찌만 봤으니까요|because the guard only ever looked at the band⟧", 12, "#C9D5E6"))

# 4. 막는 법 넷: 봉인, 바램, 다시 확인, 끊기
P4 = svg(320, sky(320)
         + envelope(50, 70, 1.0) + band(120, 113, 0.45) + label(95, 190, "⟦봉인 편지에만 넣어요|only inside a sealed letter⟧", 12, "var(--ink)", cls="d")
         + label(95, 210, "⟦길에서 못 훔쳐봐요|can\'t be peeked at on the road⟧", 10, "var(--muted)")
         + band(285, 105, 1.4, faded=True) + clock(335, 68, 0.9) + label(285, 190, "⟦시간 지나면 바래요|it fades over time⟧", 12, "var(--ink)", cls="d")
         + label(285, 210, "⟦훔쳐도 곧 못 써요|stolen? it soon stops working⟧", 10, "var(--muted)")
         + person(430, 80, s=0.7, face=EYES, **GUARD) + person(490, 90, s=0.7, face=EYES, extra=ARM_BAND, **GUEST)
         + bubble(395, 20, 170, 30, "⟦어디서 왔죠? 얼굴 다시 볼게요|where from? face check again⟧", 9, "var(--panel)", "var(--line)", "bottom")
         + label(475, 190, "⟦이상한 곳이면 다시 확인|odd place? check again⟧", 12, "var(--ink)", cls="d")
         + label(475, 210, "⟦다른 마을 번호, 새벽 세 시|another town, three in the morning⟧", 10, "var(--muted)")
         + band(665, 105, 1.4) + scissors(690, 70, 1.0) + label(665, 190, "⟦나갈 때 팔찌를 끊어요|cut the band on the way out⟧", 12, "var(--ink)", cls="d")
         + label(665, 210, "⟦그래야 주운 사람이 못 써요|so a finder can\'t use it⟧", 10, "var(--muted)")
         + label(380, 262, "⟦팔찌는 편해요 — 대신 훔치기 어렵고, 오래 못 쓰게 만들어요|a band is convenient — so make it hard to steal and short-lived⟧", 12, "var(--ink)", cls="d")
         + label(380, 296, "⟦막는 법 넷: 봉인, 바램, 다시 확인, 끊기|four fixes: seal it, fade it, re-check, cut it⟧", 11, "var(--muted)"))

# 5. 결과: 훔친 팔찌는 벌써 바랬고, 경비가 얼굴을 다시 봐요
P5 = svg(320, sky(320)
         + gate(160, 60, 1.0) + person(80, 110, s=0.85, face=MASK, extra=SWEAT + ARM_BAND_FADED) + person(250, 95, s=0.8, face=EYES, **GUARD)
         + bubble(200, 18, 250, 34, "⟦팔찌가 바랬네요 — 얼굴 다시 볼게요|this band has faded — face check, please⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(110, 240, "⟦훔친 팔찌는 벌써 바랬어요|the stolen band already faded⟧", 12, "var(--bad)")
         + label(290, 222, "⟦경비가 얼굴을 다시 봐요|the guard looks at the face again⟧", 11, "var(--muted)")
         + person(560, 100, s=0.85, face=SMILE, extra=ARM_BAND, **GUEST) + envelope(630, 120, 0.8)
         + label(600, 240, "⟦진짜 손님은 새 팔찌를 받아요|the real guest gets a fresh band⟧", 12, "var(--good)")
         + label(380, 296, "⟦팔찌를 지키는 성은 도둑이 팔찌를 훔쳐도 오래 못 써요|in a castle that guards its bands, a stolen band won\'t work for long⟧", 12, "var(--ink)", cls="d"))

SEAL_I = icon('<rect x="8" y="18" width="48" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M8 18 l24 16 l24 -16" stroke="#C9A86A" stroke-width="3" fill="none"/><circle cx="32" cy="36" r="7" fill="var(--bad)"/>')
FADE_I = icon('<ellipse cx="26" cy="36" rx="16" ry="9" fill="none" stroke="var(--accent)" stroke-width="7" opacity="0.35"/><circle cx="46" cy="20" r="12" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M46 13 v7 l5 3" stroke="var(--ink)" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
CHECK_I = icon(f'<circle cx="26" cy="30" r="14" fill="{SKIN}"/><circle cx="21" cy="28" r="2" fill="var(--night)"/><circle cx="31" cy="28" r="2" fill="var(--night)"/><path d="M12 22 Q26 6 40 22 Z" fill="var(--good)"/><text x="50" y="40" text-anchor="middle" font-size="26" font-weight="700" fill="var(--accent)">?</text>')
CUT_I = icon('<ellipse cx="30" cy="38" rx="16" ry="9" fill="none" stroke="var(--accent)" stroke-width="7"/><path d="M36 26 l16 -14 M36 50 l16 14" stroke="var(--stone-dark)" stroke-width="4" stroke-linecap="round"/><circle cx="30" cy="20" r="5" fill="none" stroke="var(--stone-dark)" stroke-width="3"/><circle cx="30" cy="56" r="5" fill="none" stroke="var(--stone-dark)" stroke-width="3"/><path d="M14 30 l32 16" stroke="var(--sky)" stroke-width="4"/>')

PAGE = {
    "slug": "session", "order": 93,
    "title": ("입장 팔찌를 훔치는 도둑", "The Thief Who Steals the Wristband"),
    "h1": ("<em>세션 하이재킹</em>이 뭐예요?", "What is <em>Session Hijacking</em>?"),
    "sub": ("세션·쿠키 하이재킹(Session / Cookie Hijacking)을 성문에서 받은 입장 팔찌를 도둑이 훔쳐 얼굴 확인 없이 들어오는 이야기로 풀어봤어요.",
            "Session and cookie hijacking, told as a story about a thief who steals the wristband you got at the gate and walks in without a face check."),
    "panels": [
        {"svg": P1, "alt": ("성문 앞에서 경비가 손님 얼굴을 확인하고 손목에 주황 팔찌를 채워줌. 오른쪽에 큰 입장 팔찌 그림", "At the gate a guard checks a guest\'s face and fastens an orange wristband on her wrist. On the right, a big drawing of the wristband"),
         "caption": ("성문에서 얼굴을 확인하고 팔찌를 채워줘요.", "At the gate, the guard checks your face and gives you a wristband."),
         "small": ('한 번 확인하면 끝이에요. 그다음부턴 팔찌만 보여주면 들어가요. 매번 <a href="mfa-ko.html">세 번 확인</a>하면 줄이 너무 길어지니까요.',
                   'One check and you\'re done. After that, you just show the band. <a href="mfa-en.html">Checking three times</a> at every door would make the line too long.')},
        {"svg": P2, "alt": ("도둑이 길에서 손님 팔찌를 훔쳐보고, 주머니 속 벌레가 팔찌를 복사하고, 팔찌를 찬 도둑이 성문을 통과함. 경비는 팔찌만 보고 웃음", "A thief peeks at a guest\'s band on the road, a bug in a pocket copies a band, and a thief wearing a band passes the gate. The guard only looks at the band and smiles"),
         "caption": ("도둑이 팔찌를 훔치거나 복사해요. 경비는 팔찌만 보거든요.", "A thief steals or copies the band. The guard only looks at the band."),
         "small": ('봉인 안 된 편지를 길에서 훔쳐보거나(<a href="mitm-ko.html">중간에서</a>), 주머니 속 <a href="spyware-ko.html">벌레</a>가 복사해요. 팔찌를 가진 사람이 곧 손님이 돼요.',
                   'They peek at an unsealed letter on the road (<a href="mitm-en.html">in the middle</a>), or a <a href="spyware-en.html">bug</a> in the pocket copies it. Whoever holds the band becomes the guest.')},
        {"svg": P3, "hero": True, "alt": ("밤. 훔친 팔찌를 찬 도둑이 성문을 지나고 경비가 '들어가세요!' 함. 팔찌를 잃은 진짜 손님은 밖에서 땀을 흘림. 오른쪽에 큰 팔찌와 '팔찌 = 통행 그 자체'", "Night. A thief wearing the stolen band walks through the gate as the guard says come in. The real guest, band gone, sweats outside. On the right a big band: the band is the pass"),
         "caption": ("세션 하이재킹은 입장 팔찌를 훔치는 도둑이에요.", "Session hijacking is a thief stealing your wristband."),
         "small": ("도둑은 비밀번호도 얼굴도 필요 없어요. 팔찌만 있으면 경비가 그냥 들여보내요. 그래서 팔찌를 봉인하고, 바래게 하고, 다시 확인하고, 끊어요.", "The thief needs no password and no face. With the band alone, the guard waves him in. So we seal the band, let it fade, re-check it, and cut it."),
         "tricks": (4, [
             (SEAL_I, ("봉인 편지로만", "Sealed letters only"), ("길에서 못 훔쳐봐요", "no peeking on the road"), "warm"),
             (FADE_I, ("바래는 팔찌", "A band that fades"), ("시간 지나면 못 써요", "stops working after a while")),
             (CHECK_I, ("이상하면 다시 확인", "Odd? Check again"), ("다른 마을, 새벽 세 시", "another town, 3 a.m.")),
             (CUT_I, ("나갈 때 끊기", "Cut it on the way out"), ("주워도 못 써요", "a found band is useless"), "calm"),
         ])},
        {"svg": P4, "alt": ("네 장면: 봉인 편지 속 팔찌, 시계 옆의 바랜 팔찌, 낯선 곳에서 얼굴을 다시 묻는 경비, 가위로 자르는 팔찌", "Four scenes: a band inside a sealed letter, a faded band next to a clock, a guard asking for a face check at an odd place, scissors cutting a band"),
         "caption": ("팔찌는 봉인 편지로만 보내고, 시간이 지나면 바래고, 나갈 때 끊어요.", "Send the band only in sealed letters, let it fade, and cut it when you leave."),
         "small": ('팔찌는 <a href="encryption-ko.html">봉인 편지</a> 안에서만 다녀요. 바랜 팔찌는 새로 받아요. 낯선 마을에서 쓰면 경비가 얼굴을 다시 봐요(<a href="ueba-ko.html">이상한 버릇 알아채기</a>).',
                   'The band travels only inside a <a href="encryption-en.html">sealed letter</a>. A faded band gets replaced. Used from a strange town, the guard asks for the face again (<a href="ueba-en.html">spotting odd habits</a>).')},
        {"svg": P5, "alt": ("도둑이 바랜 팔찌를 내밀자 경비가 얼굴을 다시 보자고 함. 도둑은 땀을 흘림. 옆에서 진짜 손님은 봉인 편지로 새 팔찌를 받음", "The thief holds out a faded band and the guard asks for a face check; the thief sweats. Beside them, the real guest receives a fresh band in a sealed letter"),
         "caption": ("훔친 팔찌는 벌써 바랬어요. 경비가 얼굴을 다시 봐요.", "The stolen band has already faded. The guard checks the face again."),
         "small": ('얼굴 다시 보기가 <a href="mfa-ko.html">세 번 확인하는 문지기</a>예요. 아예 팔찌 대신 <a href="passkey-ko.html">성문을 알아보는 반지</a>를 쓰면 훔칠 팔찌도 없어요.',
                   'The second face check is the <a href="mfa-en.html">gatekeeper who checks three times</a>. Use a <a href="passkey-en.html">ring the gate recognizes</a> instead of a band, and there is nothing to steal.')},
    ],
    "summary": (("<b>세션 하이재킹</b> = 성문에서 받은 <b>입장 팔찌</b>를 도둑이 훔쳐 <b>얼굴 확인 없이</b> 들어오는 것. 막으려면 팔찌를 <b>봉인</b>하고, <b>바래게</b> 하고, 이상하면 <b>다시 확인</b>하고, 나갈 때 <b>끊어요</b>.",
                 "<b>Session hijacking</b> = a thief steals the <b>wristband</b> you got at the gate and walks in <b>with no face check</b>. To stop it: <b>seal</b> the band, let it <b>fade</b>, <b>re-check</b> when something is odd, and <b>cut it</b> on the way out."),
                ("Session / Cookie Hijacking. 로그인 뒤 발급되는 세션 ID·쿠키·토큰을 중간자 공격, 인포스틸러, XSS 등으로 탈취해 비밀번호 없이 계정을 쓰는 공격이에요. HTTPS 강제, Secure·HttpOnly·SameSite 쿠키 속성, 짧은 만료와 토큰 회전, 이상 접속 시 재인증, 로그아웃 시 서버 측 무효화로 막아요.",
                 "Session / cookie hijacking steals the session ID, cookie, or token issued after login — via man-in-the-middle, infostealers, XSS — and uses the account without a password. Defences: enforce HTTPS, Secure / HttpOnly / SameSite cookie flags, short expiry with token rotation, step-up authentication on anomalous access, and server-side invalidation on logout.")),
    "glossary": [
        ("세션", "Session", ("성문에서 받은 입장 팔찌.", "The wristband you get at the gate."), ("한 번 확인하고 나면 그다음은 팔찌로 통과해요. '지금 들어와 있는 상태' 그 자체예요.", "Checked once, then you pass on the band alone. It is the state of being logged in.")),
        ("쿠키", "Cookie", ("팔찌를 넣어 두는 주머니.", "The pocket that holds the band."), ("브라우저가 들고 다니며 매번 보여주는 작은 쪽지예요. 팔찌 번호가 여기 들어 있어요.", "A small note the browser carries and shows every time. The band number lives here.")),
        ("세션 하이재킹", "Session hijacking", ("팔찌 훔치기.", "Stealing the band."), ("남의 팔찌로 얼굴 확인 없이 들어와요. 비밀번호를 몰라도 돼요.", "Walking in on someone else\'s band with no face check. No password needed.")),
        ("토큰 탈취", "Token theft", ("팔찌 복사.", "Copying the band."), ('길 위에서 훔쳐보거나(→ <a href="mitm-ko.html">중간에서</a>), 주머니 속 벌레가 복사해요(→ <a href="spyware-ko.html">벌레</a>).', 'Peeked at on the road (→ <a href="mitm-en.html">in the middle</a>) or copied by a bug in the pocket (→ <a href="spyware-en.html">the bug</a>).')),
        ("만료", "Expiry", ("바래는 팔찌.", "A band that fades."), ("짧게 두고 자주 새로 줘요. 훔쳐도 곧 못 써요.", "Keep it short and hand out fresh ones often. Even stolen, it soon stops working.")),
        ("Secure / HttpOnly / SameSite", "Secure / HttpOnly / SameSite", ("봉인 편지에만, 주머니 안에서만.", "Sealed letters only, pocket only."), ('봉인 안 된 길로는 안 보내고(→ <a href="tls-ko.html">봉인 편지</a>), 쪽지 속 글자(스크립트)가 주머니를 못 뒤지게 해요.', 'Never sent down an unsealed road (→ <a href="tls-en.html">sealed letters</a>), and no note (script) may rummage in the pocket.')),
        ("로그아웃", "Logout", ("팔찌 끊기.", "Cutting the band."), ("주머니에서만 빼는 게 아니라 성의 명부에서도 지워요. 주운 사람이 못 쓰게.", "Not just removed from the pocket — struck from the castle\'s roster too, so a finder can\'t use it.")),
        ("재확인", "Step-up check", ("이상하면 얼굴 다시 보기.", "Odd? Look at the face again."), ('낯선 마을, 새벽 세 시면 다시 물어요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>, <a href="ueba-ko.html">이상한 버릇 알아채기</a>', 'A strange town, three in the morning — ask again. → <a href="mfa-en.html">the gatekeeper who checks three times</a>, <a href="ueba-en.html">spotting odd habits</a>')),
    ],
}
