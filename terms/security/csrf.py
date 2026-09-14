from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
GUEST = dict(hat=None, shirt="#4A5A72")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
GOLD = "#E9B44C"
# 팔 + 손목 팔찌 (session 과 같은 차림)
ARM = f'<rect x="50" y="62" width="12" height="34" rx="6" fill="{SKIN}"/>'
ARM_BAND = ARM + '<rect x="46" y="86" width="20" height="9" rx="4" fill="var(--accent)" stroke="#142033" stroke-width="1.5"/>'


def band(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="24" ry="13" fill="none" stroke="var(--accent)" stroke-width="9"/>'
            f'<rect x="-9" y="-19" width="18" height="12" rx="3" fill="#142033"/><circle cy="-13" r="2.5" fill="#F5E6B8"/></g>')


def note(x, y, l1, l2=None, s=1.0, c1="#142033", c2="#142033", dashed=False, w=84):
    dash = ' stroke-dasharray="6 4"' if dashed else ""
    t2 = label(0, 12, l2, 9, c2) if l2 else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="{-w / 2}" y="-26" width="{w}" height="52" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"{dash}/>'
            + label(0, -4, l1, 10, c1, cls="d") + t2 + "</g>")


def counter(x, y, w=220, name="⟦금화 창구|COIN COUNTER⟧"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="80" rx="4" fill="{WOOD}"/><rect x="{x - 4}" y="{y - 4}" width="{w + 8}" height="10" rx="3" fill="#5A3B22"/>'
            + label(x + w / 2, y + 50, name, 12, "#FFF8E7", cls="d"))


def board(x, y, w=200, h=120, papers=()):
    out = f'<rect x="{x + w / 2 - 7}" y="{y}" width="14" height="{h + 20}" fill="#5A3B22"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{WOOD}" stroke="#5A3B22" stroke-width="4"/>'
    for px, py, pw, ph, text, color in papers:
        out += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5"/>'
        out += label(px + pw / 2, py + ph / 2 + 4, text, 11, color, cls="d") if text else f'<path d="M{px + 8} {py + ph * 0.4} h{pw - 16} M{px + 8} {py + ph * 0.7} h{pw - 24}" stroke="#C9A86A" stroke-width="2"/>'
    return out


def coins(x, y):
    return "".join(f'<circle cx="{x + dx}" cy="{y + dy}" r="7" fill="{GOLD}" stroke="#C9822B" stroke-width="2"/>' for dx, dy in ((0, 0), (12, 6), (-10, 8)))


# 1. 창구는 팔찌만 봐요
P1 = svg(320, sky(320)
         + person(115, 60, s=0.8, face=SMILE, **CLERK) + bubble(60, 8, 200, 34, "⟦팔찌 있네요 — 됐어요!|wristband, check — done!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + note(230, 100, "⟦대장장이에게|to the smith⟧", "⟦금화 3개|3 coins⟧") + counter(40, 150)
         + person(290, 110, s=0.9, face=SMILE, extra=ARM_BAND, **GUEST) + label(320, 240, "⟦팔찌 찬 손님|a guest with a wristband⟧", 11, "var(--muted)")
         + board(520, 60, papers=((545, 80, 60, 40, None, None), (615, 80, 60, 40, None, None), (575, 125, 90, 44, "⟦공짜 빵!|FREE BREAD!⟧", "var(--bad)")))
         + label(620, 215, "⟦마을 게시판|the village board⟧", 11, "var(--muted)")
         + person(520, 190, s=0.6, face=MASK) + label(541, 280, "⟦도둑이 종이를 붙였어요|the thief pinned a paper⟧", 10, "var(--bad)")
         + label(380, 306, "⟦창구는 팔찌만 봐요 — 편하지만, 도둑도 그걸 알아요|the counter checks only the wristband — handy, but the thief knows it too⟧", 11, "var(--ink)", cls="d"))

# 2. 손님 팔찌를 빌려 몰래 보내는 쪽지 (hero)
P2 = svg(360, sky(360)
         + board(40, 50, 160, 110, papers=((60, 70, 120, 70, "⟦공짜 빵!|FREE BREAD!⟧", "var(--bad)"),))
         + person(215, 100, s=0.9, face=EYES, extra=ARM_BAND, **GUEST) + label(245, 230, "⟦손님은 빵 그림만 봐요|the guest just looks at bread⟧", 10, "var(--muted)")
         + '<path d="M185 68 Q240 10 295 40" stroke="var(--bad)" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/><path d="M445 45 Q490 45 520 82" stroke="var(--bad)" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>'
         + note(370, 45, "⟦금화 전부 도둑에게|all coins to the thief⟧", "⟦— 손님 팔찌 붙여서|— with the guest\'s wristband⟧", c2="var(--bad)", w=150)
         + label(370, 92, "⟦손님 몰래 보내는 쪽지|sent behind the guest\'s back⟧", 10, "var(--bad)", cls="d")
         + person(520, 80, s=0.8, face=SMILE, **CLERK) + bubble(500, 18, 180, 34, "⟦팔찌 진짜네 — 보내요!|real wristband — sending!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + counter(450, 170, 200) + coins(662, 200)
         + person(680, 130, s=0.8, face=MASK) + label(690, 250, "⟦금화는 도둑에게|the coins go to the thief⟧", 10, "var(--bad)")
         + label(380, 300, "⟦팔찌는 진짜, 뜻은 가짜|the wristband is real — the wish is fake⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦손님은 아무것도 시킨 적이 없어요|the guest never asked for any of it⟧", 11, "var(--muted)"))

# 3. 사촌: 투명 종이 밑에 진짜 버튼 (클릭재킹)
P3 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="200" y="50" width="280" height="180" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>' + label(340, 100, "⟦금화 창구|COIN COUNTER⟧", 12, "var(--muted)", cls="d")
         + '<rect x="300" y="150" width="150" height="40" rx="8" fill="var(--bad)"/>' + label(375, 175, "⟦금화 보내기|SEND COINS⟧", 13, "#FFF", cls="d")
         + '<rect x="215" y="35" width="280" height="175" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3" opacity="0.6"/>'
         + label(355, 62, "⟦공짜 빵!|FREE BREAD!⟧", 14, "var(--bad)", cls="d")
         + '<rect x="300" y="150" width="150" height="40" rx="8" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="7 5"/>' + label(375, 135, "⟦↓ 여기 눌러요!|↓ PRESS HERE!⟧", 13, "var(--good)", cls="d")
         + f'<rect x="455" y="138" width="115" height="12" rx="6" fill="{SKIN}"/>' + person(560, 90, s=0.9, face=SMILE, extra=ARM_BAND, **GUEST)
         + label(640, 225, "⟦투명 종이 밑에 진짜 버튼|the real button under a clear sheet⟧", 10, "var(--ink)") + label(640, 247, "⟦손님 손가락이 눌러요|the guest\'s own finger presses it⟧", 10, "var(--muted)")
         + label(380, 290, "⟦클릭재킹 — 팔찌 빌리기의 사촌: 손가락까지 빌려요|clickjacking, a cousin of the borrowed wristband: it borrows the finger too⟧", 11, "var(--ink)", cls="d"))

# 4. 막는 법 셋
P4 = svg(340, sky(340)
         + note(130, 95, "⟦번호표 7482|slip no. 7482⟧", "⟦쪽지마다 새 번호|a new number per note⟧", c1="var(--good)", w=110)
         + note(130, 165, "⟦번호 없음|no number⟧", "⟦게시판에서 온 쪽지|note from the board⟧", c1="var(--bad)", dashed=True, w=110) + '<path d="M192 157 l16 16 M208 157 l-16 16" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(130, 225, "⟦그 자리에서 준 번호표|a slip handed over on the spot⟧", 12, "var(--ink)", cls="d") + label(130, 247, "⟦게시판 종이는 번호를 몰라요|the board\'s paper can\'t know it⟧", 10, "var(--muted)")
         + band(380, 110, 1.6) + label(380, 160, "⟦우리 창구에서만|our counter only⟧", 11, "var(--ink)", cls="d")
         + label(380, 225, "⟦팔찌는 우리 창구에서만|the wristband works only here⟧", 12, "var(--ink)", cls="d") + label(380, 247, "⟦게시판에서 온 쪽지엔 안 붙어요|it won\'t stick to notes from the board⟧", 10, "var(--muted)")
         + '<rect x="580" y="50" width="120" height="120" rx="4" fill="var(--panel)" stroke="#5A3B22" stroke-width="6"/><path d="M640 50 v120 M580 110 h120" stroke="#5A3B22" stroke-width="4"/>'
         + f'<rect x="600" y="120" width="80" height="30" rx="3" fill="{WOOD}"/><path d="M610 115 l60 40 M670 115 l-60 40" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>' + label(640, 190, "⟦남의 창문|a stranger\'s window⟧", 9, "var(--muted)")
         + label(640, 225, "⟦남의 창문엔 안 나와요|not in a stranger\'s window⟧", 12, "var(--ink)", cls="d") + label(640, 247, "⟦투명 종이 밑에 깔릴 수 없어요|so it can\'t hide under a sheet⟧", 10, "var(--muted)")
         + label(380, 300, "⟦쪽지엔 번호표, 팔찌는 우리 창구만, 창문은 우리 것만|a number on every note, wristbands only here, only our own window⟧", 12, "var(--ink)", cls="d")
         + label(380, 326, "⟦팔찌를 빌려도 쪽지가 통하지 않아요|even a borrowed wristband gets the note nowhere⟧", 11, "var(--muted)"))

# 5. 인젝션과의 차이
P5 = svg(300, sky(300)
         + '<path d="M380 30 v210" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 5"/>'
         + person(110, 70, s=0.85, face=MASK) + note(235, 110, "⟦빵 하나 주세요|one bread please⟧", "⟦…그리고 금고 열어|…and open the vault⟧", c2="var(--bad)", w=120)
         + label(190, 210, "⟦쪽지에 숨긴 명령|a command hidden in the note⟧", 12, "var(--ink)", cls="d") + label(190, 232, "⟦도둑이 자기 손으로 보내요|the thief sends it himself⟧", 10, "var(--muted)")
         + person(490, 70, s=0.85, face=EYES, extra=ARM_BAND, **GUEST) + note(620, 110, "⟦금화 도둑에게|coins to the thief⟧", "⟦(손님은 몰라요)|(the guest has no idea)⟧", c1="var(--bad)", w=120)
         + label(570, 210, "⟦남의 팔찌로 보낸 쪽지|a note sent with someone else\'s wristband⟧", 12, "var(--ink)", cls="d") + label(570, 232, "⟦손님이 자기도 모르게 보내요|the guest sends it without knowing⟧", 10, "var(--muted)")
         + label(380, 270, "⟦둘 다 창구 앞 쪽지 검토원이 먼저 봐요|the note-checker at the counter sees both first⟧", 11, "var(--muted)")
         + label(380, 292, "⟦인젝션은 쪽지 속을 노리고, 이 도둑은 팔찌를 노려요|injection aims at what is in the note — this thief aims at the wristband⟧", 12, "var(--ink)", cls="d"))

BOARD_I = icon(f'<rect x="29" y="10" width="6" height="50" fill="#5A3B22"/><rect x="8" y="12" width="48" height="32" rx="3" fill="{WOOD}"/><rect x="16" y="18" width="32" height="20" rx="2" fill="#FFF8E7"/><path d="M22 25 h20 M22 31 h14" stroke="var(--bad)" stroke-width="2"/>')
BEHIND_I = icon(f'<circle cx="24" cy="22" r="10" fill="{SKIN}"/><rect x="14" y="34" width="20" height="22" rx="5" fill="#4A5A72"/><path d="M40 20 q16 6 8 24" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="4 3"/><path d="M44 40 l4 6 l5 -7" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BAND_I = icon('<ellipse cx="32" cy="34" rx="20" ry="11" fill="none" stroke="var(--accent)" stroke-width="8"/><rect x="24" y="16" width="16" height="11" rx="3" fill="#142033"/><circle cx="32" cy="21" r="2.5" fill="#F5E6B8"/>')
FAKE_I = icon(f'<circle cx="24" cy="36" r="12" fill="{GOLD}" stroke="#C9822B" stroke-width="2"/><path d="M38 36 h16" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M48 30 l7 6 l-7 6" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M14 14 l10 10 M24 14 l-10 10" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "csrf", "order": 110,
    "title": ("손님 팔찌를 빌려 몰래 보내는 쪽지", "The Note That Borrows the Guest\'s Wristband"),
    "h1": ("<em>CSRF</em>가 뭐예요?", "What is <em>CSRF</em>?"),
    "sub": ("CSRF(Cross-Site Request Forgery)와 그 사촌 클릭재킹을, 손님이 찬 입장 팔찌를 빌려 손님 몰래 창구에 쪽지를 보내는 도둑 이야기로 풀어봤어요.",
            "CSRF (cross-site request forgery) and its cousin clickjacking, told as a story about a thief who borrows a guest\'s wristband to send the counter a note behind the guest\'s back."),
    "panels": [
        {"svg": P1, "alt": ("금화 창구의 직원이 '팔찌 있네요 — 됐어요!' 하며 팔찌 찬 손님의 쪽지(대장장이에게 금화 3개)를 받음. 오른쪽 마을 게시판엔 도둑이 붙인 '공짜 빵!' 종이", "The clerk at the coin counter says wristband, check — done! and takes a note (3 coins to the smith) from a guest wearing a wristband. On the village board to the right, a FREE BREAD! paper the thief pinned"),
         "caption": ("창구는 손님 팔찌만 보고 쪽지를 들어줘요.", "The counter reads the wristband and does what the note says."),
         "small": ('<a href="session-ko.html">입장 팔찌</a>를 찬 손님이 쪽지를 내면 창구는 팔찌만 보고 금화를 보내요. 편해요. 그런데 마을 게시판에 도둑이 이상한 종이를 붙여 뒀어요.',
                   'When a guest with an <a href="session-en.html">entry wristband</a> hands over a note, the counter checks the wristband and sends the coins. Handy. But the thief has pinned a strange paper on the village board.')},
        {"svg": P2, "hero": True, "alt": ("손님이 게시판의 '공짜 빵!' 종이를 보는 사이, 종이에서 빨간 점선이 손님 뒤로 돌아 창구로 감. 그 쪽지엔 '금화 전부 도둑에게 — 손님 팔찌 붙여서'. 직원은 '팔찌 진짜네 — 보내요!' 하고 금화가 도둑에게 감", "While the guest looks at the FREE BREAD! paper on the board, a red dotted line runs from the paper behind the guest to the counter carrying a note: all coins to the thief — with the guest\'s wristband. The clerk says real wristband — sending! and the coins go to the thief"),
         "caption": ("CSRF는 손님 팔찌를 빌려 몰래 보내는 쪽지예요.", "CSRF is a note that borrows the guest\'s wristband and goes behind the guest\'s back."),
         "small": ("손님은 빵 그림만 봤어요. 그런데 그 종이가 손님 팔찌를 달아 '내 금화를 도둑에게' 쪽지를 창구로 보내요. 팔찌는 진짜라서 창구는 믿어요 — 뜻만 가짜예요.",
                   "The guest only looked at a picture of bread. But that paper pins the guest\'s wristband onto a note — send my coins to the thief — and mails it to the counter. The wristband is real, so the counter trusts it. Only the wish is fake."),
         "tricks": (4, [
             (BOARD_I, ("게시판의 종이", "A paper on the board"), ("도둑이 붙여 뒀어요", "pinned by the thief"), "warm"),
             (BEHIND_I, ("손님 몰래", "Behind the guest"), ("빵 그림만 봤을 뿐", "who only saw bread"), "warm"),
             (BAND_I, ("팔찌는 진짜", "The wristband is real"), ("그래서 창구가 믿어요", "so the counter trusts it")),
             (FAKE_I, ("뜻은 가짜", "The wish is fake"), ("손님은 시킨 적 없어요", "the guest never asked"), "calm"),
         ])},
        {"svg": P3, "alt": ("금화 창구 위에 반투명 종이 '공짜 빵!'이 덮여 있고, '여기 눌러요!' 점선 표시 밑으로 진짜 '금화 보내기' 빨간 버튼이 비침. 팔찌 찬 손님이 손가락으로 그 자리를 누름", "A see-through FREE BREAD! sheet lies over the coin counter; under the dotted PRESS HERE! mark the real red SEND COINS button shows through. A guest with a wristband presses that very spot"),
         "caption": ("사촌도 있어요: 투명 종이 밑에 진짜 버튼을 숨겨요.", "It has a cousin: the real button hidden under a clear sheet."),
         "small": ("도둑이 우리 창구 위에 투명 종이를 덮고 '여기 눌러요!'라고 써요. 손님이 누르면 밑에 있던 진짜 '금화 보내기' 버튼이 눌려요. 팔찌도 진짜, 손가락도 진짜예요.",
                   "The thief lays a clear sheet over our counter and writes PRESS HERE! When the guest presses, the real SEND COINS button underneath gets pressed. Real wristband, real finger.")},
        {"svg": P4, "alt": ("셋: 초록 '번호표 7482' 쪽지와 번호 없는 게시판 쪽지에 ×, '우리 창구에서만' 표가 붙은 팔찌, 남의 창문 안에 × 표시", "Three things: a green slip no. 7482 next to a board note with no number marked ×; a wristband tagged our counter only; and a stranger\'s window with an × inside"),
         "caption": ("쪽지엔 번호표, 팔찌는 우리 창구만, 창문은 우리 것만.", "A number on every note, wristbands only here, only our own window."),
         "small": ("창구가 그 자리에서 준 번호표 없는 쪽지는 안 받아요 — 게시판 종이는 번호를 몰라요. 팔찌는 우리 창구에 낸 쪽지에만 붙고, 우리 창구는 남의 창문 안에 나오지 않아요.",
                   "The counter refuses any note without the slip it handed over on the spot — the board\'s paper can\'t know the number. The wristband sticks only to notes handed in at our counter, and our counter never appears inside a stranger\'s window.")},
        {"svg": P5, "alt": ("왼쪽: 도둑이 '빵 하나 주세요 …그리고 금고 열어' 쪽지를 직접 냄. 오른쪽: 팔찌 찬 손님이 자기도 모르게 '금화 도둑에게' 쪽지를 냄. 가운데 점선", "Left: the thief himself hands in a note — one bread please …and open the vault. Right: a guest with a wristband unknowingly hands in a note — coins to the thief. A dotted line between them"),
         "caption": ("쪽지 속을 노리는 도둑과 팔찌를 노리는 도둑은 달라요.", "A thief after the note\'s insides and a thief after the wristband are different thieves."),
         "small": ('<a href="injection-ko.html">쪽지에 숨긴 명령</a>은 도둑이 자기 손으로 보내고, 이 도둑은 손님 손으로 보내게 해요. 둘 다 <a href="waf-ko.html">창구 앞 쪽지 검토원</a>이 먼저 보지만, 팔찌 도둑은 번호표가 있어야 막혀요.',
                   'A <a href="injection-en.html">command hidden in the note</a> is sent by the thief\'s own hand; this thief makes the guest send it. The <a href="waf-en.html">note-checker at the counter</a> sees both first, but the wristband thief is only stopped by the slip.')},
    ],
    "summary": (("<b>CSRF</b> = 도둑이 붙인 종이가 <b>손님 팔찌를 빌려</b> 손님 몰래 창구에 <b>가짜 뜻의 쪽지</b>를 보내는 것. <b>번호표</b>(그 자리에서 준 비밀 번호), <b>팔찌는 우리 창구만</b>, <b>남의 창문엔 안 나오기</b>로 막아요.",
                 "<b>CSRF</b> = a paper the thief pinned <b>borrows the guest\'s wristband</b> and sends the counter a <b>note with a fake wish</b> behind the guest\'s back. Stopped by a <b>slip</b> (a secret number handed over on the spot), <b>wristbands that work only at our counter</b>, and <b>never appearing in a stranger\'s window</b>."),
                ("Cross-Site Request Forgery. 로그인된 사용자의 브라우저가 쿠키를 자동으로 붙이는 걸 이용해, 다른 사이트에서 사용자 몰래 요청을 보내게 하는 공격이에요. CSRF 토큰, SameSite 쿠키, 그리고 클릭재킹을 막는 X-Frame-Options / CSP frame-ancestors 로 막아요.",
                 "An attack that abuses the browser\'s habit of attaching cookies automatically, making a logged-in user\'s browser send a request from another site without the user knowing. Defended with CSRF tokens, SameSite cookies, and — against clickjacking — X-Frame-Options / CSP frame-ancestors.")),
    "glossary": [
        ("CSRF", "CSRF", ("팔찌 빌려 몰래 보내는 쪽지.", "The note that borrows the wristband."), ("손님은 진짜, 팔찌도 진짜, 뜻만 가짜. 손님이 로그인한 채로 도둑의 페이지를 열면 생겨요.", "Real guest, real wristband, fake wish. It happens when a logged-in guest opens the thief\'s page.")),
        ("CSRF 토큰", "CSRF token", ("그 자리에서 준 번호표.", "The slip handed over on the spot."), ("창구가 쪽지 종이에 미리 적어 준 비밀 번호. 게시판 종이는 이 번호를 알 수 없어요.", "A secret number the counter wrote on the note form in advance. The board\'s paper can never know it.")),
        ("SameSite 쿠키", "SameSite cookie", ("우리 창구에서만 통하는 팔찌.", "A wristband that works only at our counter."), ("다른 마을에서 보낸 쪽지엔 팔찌가 안 붙어요. 요즘 브라우저는 기본으로 이렇게 해요.", "The wristband won\'t attach to notes sent from another town. Modern browsers do this by default.")),
        ("클릭재킹", "Clickjacking", ("투명 종이 밑의 진짜 버튼.", "The real button under a clear sheet."), ("손님이 '여기 눌러요'를 누르면 밑의 진짜 버튼이 눌려요. 팔찌 빌리기의 사촌이에요.", "The guest presses PRESS HERE and the real button underneath gets pressed. A cousin of the borrowed wristband.")),
        ("X-Frame-Options / CSP", "X-Frame-Options / CSP", ("남의 창문엔 안 나오기.", "Never in a stranger\'s window."), ("우리 창구를 다른 페이지 안에 끼워 넣을 수 없게 해요. 그러면 투명 종이를 덮을 곳이 없어요.", "Our counter can\'t be embedded inside another page — so there is nowhere to lay the clear sheet.")),
        ("세션", "Session", ("입장 팔찌.", "The entry wristband."), ('창구가 손님을 알아보는 팔찌. 훔칠 수도, 빌릴 수도 있어요. → <a href="session-ko.html">입장 팔찌를 훔치는 도둑</a>', 'How the counter recognizes the guest. It can be stolen — or borrowed. → <a href="session-en.html">the thief who steals the wristband</a>')),
        ("인젝션과의 차이", "Versus injection", ("쪽지 속 vs 팔찌.", "Inside the note vs the wristband."), ('인젝션은 쪽지 안에 명령을 숨기고, CSRF는 남의 팔찌로 보내요. → <a href="injection-ko.html">쪽지에 숨긴 명령</a>', 'Injection hides a command inside the note; CSRF sends with someone else\'s wristband. → <a href="injection-en.html">the command hidden in the note</a>')),
        ("WAF", "WAF", ("창구 앞 쪽지 검토원.", "The note-checker at the counter."), ('이상한 쪽지를 먼저 걸러요. 하지만 팔찌 도둑은 번호표가 있어야 확실히 막혀요. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'Filters odd notes first. But the wristband thief is only surely stopped by the slip. → <a href="waf-en.html">the note-checker at the counter</a>')),
    ],
}
