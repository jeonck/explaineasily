from _draw import *

MUD = "#7A5236"
TRAIL = "".join(foot(x, y, r) for x, y, r in
                ((60, 286, -20), (112, 276, 20), (164, 284, -20), (216, 272, 20), (268, 280, -20), (320, 268, 20)))
P1 = svg(300, sky(300) + castle() + TRAIL
         + f'<path d="M345 270 V210 a35 35 0 0 1 70 0 V270 Z" fill="var(--night)"/>'
           f'<path d="M345 270 V210 a35 35 0 0 1 35 -35 V270 Z" fill="#2B3A55"/>'
           f'<rect x="376" y="205" width="6" height="65" fill="{MUD}"/>')

GLASS = ('<circle cx="250" cy="200" r="52" fill="var(--panel)" fill-opacity="0.35" stroke="var(--night)" stroke-width="8"/>'
         '<path d="M290 238 L340 288" stroke="var(--night)" stroke-width="14" stroke-linecap="round"/>')
P2 = svg(260, sky(260) + foot(150, 230, -15) + foot(250, 205, 15, MUD) + foot(340, 232, -15)
         + GLASS + person(560, 60, hat="var(--good)", shirt="var(--good)", face=SMILE, s=1.2)
         + label(250, 80, "⟦누구 발자국이지?|Whose footprint is this?⟧", 22, cls="d"))

CARD = ('<rect x="150" y="70" width="110" height="80" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
        + foot(205, 118, 10))
LINES = "".join(f'<path d="M270 110 L{x} {y}" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
                for x, y in ((470, 60), (520, 150), (470, 230)))
P3 = svg(280, sky(280) + person(60, 40, hat="var(--good)", shirt="var(--good)", face=SMILE) + CARD + LINES
         + small_castle(470, 20) + small_castle(520, 110) + small_castle(470, 190)
         + bubble(150, 176, 300, 44, "⟦이 발자국 보이면 알려줘!|Seen this footprint? Tell me!⟧", 17, "var(--accent-soft)", "var(--accent)", "left"))

SHOE = ('<path d="M0 0 h50 a18 18 0 0 1 18 18 v8 h-80 v-14 a12 12 0 0 1 12 -12z" fill="var(--bad)"/>'
        '<rect x="-12" y="26" width="80" height="6" fill="var(--night)"/>')
X = '<path d="M-22 -30 L22 30 M22 -30 L-22 30" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>'
P4 = svg(260, sky(260)
         + person(120, 60, extra=f'<g transform="translate(70,30)">{SHOE}</g>' + label(30, -10, "⟦새 신발!|New shoes!⟧", 18, "var(--bad)"))
         + foot(360, 200, 0) + f'<g transform="translate(360,192)">{X}</g>'
         + label(430, 210, "→", 40, "var(--muted)")
         + '<g transform="translate(520,172)"><rect x="-12" y="-16" width="24" height="34" rx="4" fill="#4A5A72"/><rect x="-9" y="-36" width="18" height="14" rx="3" fill="#4A5A72"/></g>'
         + label(520, 240, "⟦다른 발자국|a different print⟧", 15, "var(--muted)"))

IP_I = icon('<rect x="8" y="22" width="48" height="30" rx="4" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><path d="M8 22 L32 8 L56 22" stroke="var(--bad)" stroke-width="3" fill="none"/><text x="32" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">10.0.0.7</text>')
MAIL_I = icon('<rect x="8" y="16" width="48" height="34" rx="4" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><path d="M8 18 L32 36 L56 18" stroke="var(--bad)" stroke-width="3" fill="none"/>')
PRINT_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="32" cy="32" r="12" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="32" cy="32" r="4" fill="var(--bad)"/>')

PAGE = {
    "slug": "ioc", "order": 2,
    "title": ("남겨진 발자국", "The Footprint"),
    "h1": ("<em>IOC</em>가 뭐예요?", "What is an <em>IOC</em>?"),
    "sub": ("침해 지표(Indicator of Compromise)를 발자국 이야기로 풀어봤어요.",
            "Indicators of Compromise, told as a story about footprints."),
    "panels": [
        {"svg": P1, "alt": ("성문까지 이어진 진흙 발자국", "Muddy footprints leading to the castle door"),
         "caption": ("누가 왔다 갔어요.", "Someone was here."),
         "small": ("발자국이 남아 있어요.", "They left footprints.")},
        {"svg": P2, "alt": ("돋보기로 발자국을 살피는 친구", "The friend inspecting a footprint with a magnifying glass"),
         "caption": ("흔적은 여러 가지예요.", "Clues come in a few shapes."),
         "small": ("어디서 왔는지, 뭘 두고 갔는지.", "Where they came from, and what they left behind."),
         "tricks": (3, [
             (IP_I, ("낯선 집 주소", "A strange address"), ("IP 주소", "an IP address")),
             (MAIL_I, ("이상한 편지 주소", "A strange sender"), ("도메인, URL", "a domain or URL")),
             (PRINT_I, ("물건의 지문", "A fingerprint on a thing"), ("파일 해시", "a file hash")),
         ])},
        {"svg": P3, "hero": True, "alt": ("발자국 카드를 다른 성들에게 보내는 친구", "The friend sending a footprint card to other castles"),
         "caption": ("발자국 사진을 친구들과 나눠요.", "You share the footprint with friends."),
         "small": ("우리 성에서 본 걸 다른 성도 알면, 다 같이 빨리 찾아요.", "What one castle saw, every castle can look for.")},
        {"svg": P4, "alt": ("새 신발을 든 나쁜 사람과 지워진 발자국", "The bad guy holding new shoes next to a crossed-out footprint"),
         "caption": ("그런데 신발을 바꾸면 발자국도 바뀌어요.", "But new shoes make a new footprint."),
         "small": ('그래서 발자국만으론 부족해요. <a href="ttp-ko.html">버릇(TTP)</a>도 알아야 해요.',
                   'So footprints alone aren\'t enough. You need their <a href="ttp-en.html">habits (TTPs)</a> too.')},
    ],
    "summary": (("<b>IOC</b> = 나쁜 사람이 남긴 흔적. 보이면 \"<b>이미</b> 왔었다\"는 뜻.",
                 "<b>IOC</b> = a trace the bad guy left. If you see it, they were <b>already</b> here."),
                ("침해 지표는 미리 막는 게 아니라 이미 일어난 일을 찾아내는 단서예요. 신발은 쉽게 바꾸니까 오래가진 않아요.",
                 "An indicator doesn't stop the break-in; it helps you spot one that happened. Shoes are cheap to change, so indicators go stale fast.")),
    "glossary": [
        ("파일 해시", "File hash", ("물건의 지문.", "A thing's fingerprint."), ("파일 하나마다 다른 긴 숫자. 한 글자만 바꿔도 지문이 바뀌어요.", "A long number unique to one file. Change one byte and the fingerprint changes.")),
        ("IP 주소", "IP address", ("집 주소.", "A house address."), ("나쁜 사람이 쓰는 컴퓨터가 사는 곳.", "Where the bad guy's computer lives.")),
        ("도메인", "Domain", ("집 이름.", "A house name."), ("주소 대신 부르는 이름. 새로 사는 데 몇 시간이면 돼요.", "A name used instead of the address. Buying a new one takes hours.")),
        ("위협 피드", "Threat feed", ("발자국 사진 묶음.", "A stack of footprint photos."), ("다른 성들이 본 흔적이 계속 들어와요.", "Traces other castles saw, arriving all day.")),
        ("오탐", "False positive", ("우리 강아지 발자국.", "Our own dog's paw print."), ("도둑 발자국인 줄 알았는데 아니었던 것.", "Looked like the burglar's, wasn't.")),
    ],
}
