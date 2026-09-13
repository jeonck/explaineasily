from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
SHOPKEEPER = dict(hat="var(--accent)", shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def shop(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="30" width="120" height="90" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>'
            f'<path d="M-70 30 h140 l-10 -26 h-120 z" fill="var(--accent)"/>'
            + "".join(f'<rect x="{-70 + i * 28}" y="4" width="14" height="26" fill="#FFD9B8"/>' for i in range(5))
            + f'<rect x="-14" y="70" width="28" height="50" fill="{WOOD}"/>' + label(0, 60, "⟦인쇄|PRINT⟧", 14, "var(--ink)") + "</g>")


def photo(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-18" width="44" height="36" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M-16 10 l10 -12 l8 8 l6 -5 l8 9z" fill="var(--good)"/><circle cx="10" cy="-8" r="4" fill="var(--accent)"/></g>')


def ticket(x, y, lines, w=230, h=90, s=1.0, torn=False):
    body = "".join(label(w / 2, 34 + i * 24, t, 15 if i else 17, "#142033") for i, t in enumerate(lines))  # 표 종이색이 고정이라 글자도 고정
    edge = ('<path d="M0 0 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14 l14 14 l14 -14" '
            'stroke="var(--bad-soft)" stroke-width="6" fill="none"/>') if torn else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="8" fill="#FFF3D6" stroke="var(--accent)" stroke-width="3"/>'
            f'<path d="M18 0 V{h}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>{body}{edge}</g>')


def big_key(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="26" fill="none" stroke="#E9B44C" stroke-width="12"/>'
            f'<rect x="24" y="-6" width="90" height="12" fill="#E9B44C"/><rect x="84" y="6" width="9" height="14" fill="#E9B44C"/><rect x="102" y="6" width="9" height="18" fill="#E9B44C"/></g>')


def doors(x, y, names, marks, s=1.0):
    out = ""
    for i, (n, m) in enumerate(zip(names, marks)):
        dx = x + i * 110
        mark = {"ok": '<path d="M-12 0 l9 9 l17 -19" stroke="var(--good)" stroke-width="6" fill="none" stroke-linecap="round"/>',
                "no": '<path d="M-12 -12 l24 24 M12 -12 l-24 24" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>',
                "key": '<circle cx="-14" cy="0" r="9" fill="none" stroke="#E9B44C" stroke-width="5"/><rect x="-6" y="-3" width="30" height="6" fill="#E9B44C"/><rect x="14" y="3" width="4" height="7" fill="#E9B44C"/><rect x="20" y="3" width="4" height="9" fill="#E9B44C"/>'}[m]
        out += (f'<g transform="translate({dx},{y}) scale({s})"><rect x="-36" width="72" height="120" rx="3" fill="{WOOD}"/><circle cx="24" cy="64" r="4" fill="#E9B44C"/>'
                f'{label(0, -10, n, 14, "var(--ink)")}<g transform="translate(0,58)">{mark}</g></g>')
    return out


ROOMS = ("⟦사진|Photos⟧", "⟦편지|Mail⟧", "⟦돈|Money⟧")

# 1. 내 사진은 사진 성에
P1 = svg(300, sky(300) + person(40, 120, s=0.9, **ME) + label(70, 250, "⟦나|me⟧", 14, "var(--muted)")
         + castle(190, 90, 0.55) + label(316, 60, "⟦사진 성|Photo Castle⟧", 16, "var(--ink)", cls="d") + photo(316, 165, 0.9)
         + shop(620, 110) + label(620, 250, "⟦인쇄 가게|the print shop⟧", 14, "var(--muted)")
         + '<path d="M560 150 L470 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6"/><path d="M482 140 L468 150 L482 160" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(515, 135, "?", 26, "var(--accent)", cls="d"))

# 2. 옛날엔 열쇠를 통째로
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + person(40, 90, s=0.9, **ME) + big_key(170, 130, 0.8)
         + '<path d="M270 130 L330 130" stroke="var(--muted)" stroke-width="3"/><path d="M320 120 L332 130 L320 140" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(340, 90, s=0.9, **SHOPKEEPER)
         + doors(500, 90, ROOMS, ("key", "key", "key"))
         + label(610, 250, "⟦전부 열려요|everything opens⟧", 14, "var(--bad)"))

# 3. OAuth = 열쇠 대신 입장권 (hero)
STEP = lambda x, y, n: f'<circle cx="{x}" cy="{y}" r="14" fill="var(--accent)"/>' + label(x, y + 5, str(n), 15, "#FFF")
P3 = svg(360, '<rect width="760" height="360" fill="var(--panel)"/>'
         # 1: 나 → 성 문지기 (동의)
         + person(30, 60, s=0.8, **ME) + person(160, 60, s=0.8, face=EYES, **GUARD)
         + bubble(90, 10, 230, 34, "⟦이 가게에 사진 방만 열어주세요|Let this shop into Photos only⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + STEP(30, 200, 1) + label(110, 205, "⟦내가 허락해요|I say yes⟧", 14, "var(--muted)", "start")
         # 2: 성 → 가게에 표
         + ticket(320, 60, ("⟦입장권|TICKET⟧", "⟦사진 방 · 보기만|Photos · read only⟧", "⟦30일|30 days⟧"), 200, 90, 1.0)
         + '<path d="M540 105 L600 105" stroke="var(--accent)" stroke-width="3"/><path d="M590 95 L602 105 L590 115" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + person(620, 60, s=0.8, **SHOPKEEPER)
         + STEP(320, 200, 2) + label(400, 205, "⟦성이 가게에 표를 줘요|the castle hands the shop a ticket⟧", 14, "var(--muted)", "start")
         # 3: 가게가 표로 사진 방만
         + doors(160, 240, ROOMS, ("ok", "no", "no"), 0.8)
         + ticket(470, 262, ("⟦입장권|TICKET⟧",), 120, 44, 0.9)
         + person(610, 220, s=0.8, **SHOPKEEPER)
         + STEP(30, 300, 3) + label(80, 305, "⟦표로 사진만|photos only, with the ticket⟧", 14, "var(--muted)", "start"))

# 4. 표엔 방 이름과 시간
SCISSORS = ('<g transform="translate(640,110) rotate(-30)"><circle cx="-14" cy="14" r="9" fill="none" stroke="var(--night)" stroke-width="4"/><circle cx="14" cy="14" r="9" fill="none" stroke="var(--night)" stroke-width="4"/>'
            '<path d="M-8 6 L10 -40 M8 6 L-10 -40" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>')
P4 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + ticket(50, 60, ("⟦입장권|TICKET⟧", "⟦사진 방 · 보기만|Photos · read only⟧", "⟦30일|30 days⟧"), 240, 100, 1.1)
         + doors(400, 60, ROOMS[:2], ("ok", "no"), 0.9)
         + ticket(560, 150, ("⟦입장권|TICKET⟧",), 130, 44, 0.9, torn=True) + SCISSORS
         + label(630, 240, "⟦마음이 바뀌면 표만 찢어요|change your mind? tear the ticket⟧", 13, "var(--muted)"))

# 5. 표는 '누구'인지 말하지 않는다
HAND_TICKET = ticket(230, 90, ("⟦입장권|TICKET⟧", "⟦사진 방|Photos⟧"), 160, 70, 1.0)
NAMETAG = ('<g transform="translate(560,80)"><rect width="150" height="90" rx="8" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
           f'<circle cx="34" cy="45" r="18" fill="{SKIN}"/><path d="M14 38 Q34 14 54 38 Z" fill="var(--good)"/>'
           + label(100, 40, "⟦이름표|NAME TAG⟧", 13, "var(--good)") + label(100, 62, "⟦나: 지민|me: Jimin⟧", 14, "var(--ink)") + "</g>")
P5 = svg(260, '<rect width="760" height="260" fill="var(--good-soft)"/>'
         + person(60, 70, s=0.9, face=EYES, **GUARD) + bubble(40, 14, 130, 34, "⟦근데 누구세요?|but who are you?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + HAND_TICKET + label(310, 200, "⟦표: 들어가도 됨|ticket: may enter⟧", 13, "var(--muted)")
         + label(480, 130, "+", 36, "var(--muted)", cls="d")
         + NAMETAG + label(635, 200, "⟦이름표: 이 사람이 나|name tag: this is me⟧", 13, "var(--muted)"))

ME_I = icon('<circle cx="32" cy="22" r="10" fill="var(--good)"/><rect x="18" y="36" width="28" height="20" rx="8" fill="var(--good)"/>')
CASTLE_I = icon('<rect x="8" y="26" width="48" height="28" fill="var(--stone-dark)"/><rect x="8" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="26" y="40" width="12" height="14" rx="6" fill="var(--night)"/>')
SHOP_I = icon('<rect x="12" y="26" width="40" height="28" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><path d="M8 26 h48 l-4 -10 h-40z" fill="var(--accent)"/><rect x="28" y="40" width="10" height="14" fill="var(--accent)"/>')

PAGE = {
    "slug": "oauth", "order": 13,
    "title": ("열쇠 대신 입장권", "A Ticket, Not the Key"),
    "h1": ("<em>OAuth</em>가 뭐예요?", "What is <em>OAuth</em>?"),
    "sub": ("OAuth를 열쇠 대신 입장권을 주는 이야기로 풀어봤어요.",
            "OAuth, told as a story about handing out a ticket instead of your key."),
    "panels": [
        {"svg": P1, "alt": ("나, 사진이 있는 사진 성, 그리고 그 사진이 필요한 인쇄 가게", "Me, the Photo Castle holding my photos, and a print shop that needs them"),
         "caption": ("내 사진은 사진 성에 있어요.", "My photos live in the Photo Castle."),
         "small": ("인쇄 가게가 그 사진을 가져와야 해요.", "The print shop needs to fetch them.")},
        {"svg": P2, "alt": ("내가 큰 열쇠를 가게 주인에게 건네고, 사진·편지·돈 방이 전부 열림", "I hand a big key to the shopkeeper, and the Photos, Mail and Money doors all open"),
         "caption": ("옛날엔 열쇠를 통째로 줬어요.", "We used to hand over the whole key."),
         "small": ("가게가 사진만 보는 게 아니라 편지도, 돈도 다 열 수 있었어요.", "The shop could open not just Photos, but Mail and Money too.")},
        {"svg": P3, "hero": True, "alt": ("1: 내가 성 문지기에게 '이 가게에 사진 방만'이라고 허락, 2: 성이 가게에 '사진 방·보기만·30일' 표를 줌, 3: 가게가 표로 사진 방만 들어감", "1: I tell the castle guard 'Photos only for this shop'; 2: the castle gives the shop a ticket reading 'Photos · read only · 30 days'; 3: the shop enters Photos only"),
         "caption": ("OAuth는 열쇠 대신 입장권을 줘요.", "OAuth hands out a ticket instead of the key."),
         "small": ("내가 성에 허락하면, 성이 가게에 표를 줘요. 열쇠는 내 주머니에 그대로.", "I tell the castle yes, the castle gives the shop a ticket. The key never leaves my pocket."),
         "tricks": (3, [
             (ME_I, ("나", "Me"), ("사진의 주인", "who owns the photos"), "calm"),
             (CASTLE_I, ("사진 성", "The Photo Castle"), ("사진을 보관하고 표를 찍어줘요", "keeps the photos, prints the tickets")),
             (SHOP_I, ("인쇄 가게", "The print shop"), ("표를 들고 심부름", "runs the errand with the ticket"), "warm"),
         ])},
        {"svg": P4, "alt": ("'사진 방·보기만·30일' 입장권, 사진 문엔 체크, 편지 문엔 X, 그리고 가위로 찢긴 표", "A ticket reading 'Photos · read only · 30 days', a check on the Photos door, an X on Mail, and a ticket cut with scissors"),
         "caption": ("표엔 방 이름과 시간이 적혀 있어요.", "The ticket names the room and the time."),
         "small": ("사진 방, 보기만, 30일. 마음이 바뀌면 표만 찢어요 — 열쇠는 안 바꿔도 돼요.", "Photos, read only, 30 days. Change your mind? Tear up the ticket — no need to change the key.")},
        {"svg": P5, "alt": ("문지기가 표를 보며 '근데 누구세요?'라고 묻고, 표 옆에 얼굴이 그려진 이름표", "A guard looks at the ticket and asks 'but who are you?'; beside the ticket is a name tag with a face"),
         "caption": ("표는 '누구'인지는 말 안 해요.", "A ticket doesn't say who you are."),
         "small": ("표는 '들어가도 됨'이지 '이 사람이 나'가 아니에요. 그건 이름표(OpenID Connect)가 따로 해요. 그래서 표를 잃어버리면 주운 사람도 써요.", "A ticket means 'may enter', not 'this is me'. The name tag (OpenID Connect) does that part. Which is also why a lost ticket works for whoever finds it.")},
    ],
    "summary": (("<b>OAuth</b> = 내 열쇠를 주지 않고, 다른 가게가 내 방 <b>하나만 잠깐</b> 들어가게 해주는 <b>입장권</b>.",
                 "<b>OAuth</b> = a <b>ticket</b> that lets another shop into <b>one room, for a while</b> — without ever giving it my key."),
                ("OAuth 2.0 (2012, RFC 6749). 'Google로 계속하기' 버튼 뒤에서 일어나는 일이에요 — 입장권은 OAuth가, 이름표는 OpenID Connect가 맡아요.",
                 "OAuth 2.0 (2012, RFC 6749). It's what happens behind a 'Continue with Google' button — OAuth does the ticket, OpenID Connect does the name tag.")),
    "glossary": [
        ("자원 주인", "Resource owner", ("나.", "Me."), ("사진의 주인. 허락하는 사람.", "Owner of the photos. The one who says yes.")),
        ("클라이언트", "Client", ("인쇄 가게.", "The print shop."), ("내 대신 심부름하는 앱.", "The app running the errand on my behalf.")),
        ("인가 서버", "Authorization server", ("표 발급소.", "The ticket office."), ("내 허락을 받고 표를 찍어주는 곳.", "Takes my yes and prints the ticket.")),
        ("자원 서버", "Resource server", ("사진 창고.", "The photo storeroom."), ("표를 보고 사진을 내주는 곳. 발급소와 한 성 안에 있어요.", "Checks the ticket and hands over photos. Same castle as the ticket office.")),
        ("액세스 토큰", "Access token", ("입장권.", "The ticket."), ("가게가 들고 다니는 표. 잃어버리면 남도 써요.", "What the shop carries. Lost, it works for anyone.")),
        ("범위", "Scope", ("표에 적힌 방 이름.", "The room written on the ticket."), ('"사진 방 · 보기만". 적히지 않은 방은 못 들어가요.', '"Photos · read only." Rooms not listed stay shut.')),
        ("리프레시 토큰", "Refresh token", ("표 재발급 쿠폰.", "The reissue coupon."), ("30일이 지나면 이걸로 새 표를 받아요. 나한테 다시 묻지 않고요.", "When 30 days pass, this gets a fresh ticket without asking me again.")),
        ("OpenID Connect", "OpenID Connect", ("이름표.", "The name tag."), ("OAuth 위에 얹어서 '이 사람이 나'까지 알려줘요. 로그인 버튼의 진짜 주인공.", "Sits on top of OAuth and adds 'this is me'. The real engine behind login buttons.")),
    ],
}
