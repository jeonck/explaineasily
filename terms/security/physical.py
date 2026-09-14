from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
GUEST = dict(hat=None, shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GOLD = "#E9B44C"


def door(x, y, w=70, h=120, open_gap=False, color=WOOD):
    if open_gap:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="var(--night)"/>'
                f'<rect x="{x}" y="{y}" width="{w * 0.35:.0f}" height="{h}" fill="{color}"/>'
                f'<circle cx="{x + w * 0.28:.0f}" cy="{y + h * 0.55:.0f}" r="4" fill="{GOLD}"/>')
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}"/><circle cx="{x + w - 12}" cy="{y + h * 0.55:.0f}" r="4" fill="{GOLD}"/>'


def server_box(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="60" height="90" rx="4" fill="var(--stone-dark)"/>'
            + "".join(f'<rect x="8" y="{10 + i * 20}" width="44" height="12" rx="2" fill="var(--panel)"/><circle cx="16" cy="{16 + i * 20}" r="3" fill="var(--good)"/>' for i in range(4)) + "</g>")


def card(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-24" y="-16" width="48" height="32" rx="4" fill="#5B8DEF"/>'
            f'<circle cx="-10" cy="-4" r="6" fill="#FFF8E7"/><rect x="-20" y="6" width="40" height="4" rx="2" fill="#FFF8E7"/><rect x="4" y="-14" width="16" height="10" rx="2" fill="#E9B44C"/></g>')


def cam(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-4" y="-30" width="8" height="30" fill="var(--stone-dark)"/>'
            f'<g transform="rotate(20)"><rect x="-10" y="-6" width="40" height="22" rx="6" fill="var(--stone-dark)"/><circle cx="26" cy="5" r="8" fill="var(--panel)"/><circle cx="26" cy="5" r="4" fill="var(--night)"/></g>'
            f'<circle cx="-4" cy="8" r="3" fill="var(--bad)"/></g>')


def paper(x, y, s=1.0, rot=0, shred=False):
    if shred:
        return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">' + "".join(f'<rect x="{-24 + i * 8}" y="-30" width="6" height="64" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1"/>' for i in range(6)) + "</g>"
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-24" y="-30" width="48" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-16 -14 h32 M-16 -4 h32 M-16 6 h22" stroke="#C9A86A" stroke-width="2"/></g>')


def usb(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-6" y="-4" width="34" height="18" rx="3" fill="#2E3D57"/>'
            f'<rect x="-18" y="-1" width="14" height="12" rx="1" fill="#C9C9C9"/></g>')


# 1. 봉인 편지·경비견이 있어도 서버실 문이 열려 있으면
P1 = svg(320, sky(320)
         + '<rect x="480" y="40" width="240" height="230" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + label(600, 66, "⟦서버실|SERVER ROOM⟧", 12, "var(--muted)", cls="d") + door(490, 150, 60, 110, open_gap=True)
         + server_box(600, 100, 1.0) + label(600, 220, "⟦문이 그냥 열려 있어요|the door just stands open⟧", 10, "var(--bad)")
         + '<g transform="translate(120,60)"><rect width="80" height="56" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M0 0 l40 28 l40 -28" stroke="#C9A86A" stroke-width="3" fill="none"/><circle cx="40" cy="28" r="8" fill="var(--bad)"/></g>' + label(160, 140, "⟦봉인 편지|sealed letters⟧", 10, "var(--muted)")
         + '<circle cx="300" cy="90" r="26" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M290 90 l7 7 l14 -16" stroke="var(--good)" stroke-width="5" fill="none"/>' + label(300, 140, "⟦경비견도 있어요|even a guard dog⟧", 10, "var(--muted)")
         + person(280, 180, s=0.8, face=MASK, extra=BAG) + label(300, 290, "⟦도둑이 상자를 그냥 들고 나가요|the thief just carries the box out⟧", 11, "var(--ink)", cls="d")
         + label(380, 314, "⟦봉인 편지도 경비견도 소용없어요 — 문이 열려 있으니까요|sealed letters and dogs mean nothing — the door is open⟧", 11, "var(--muted)"))

# 2. 성문을 잠가도 창문이 열려 있으면 (문제)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="60" y="60" width="200" height="180" fill="var(--stone-dark)"/>' + door(120, 120, 70, 120) + '<rect x="152" y="150" width="18" height="18" rx="3" fill="var(--good)"/><path d="M156 150 v-8 a5 5 0 0 1 10 0 v8" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(160, 262, "⟦성문은 꽉 잠갔어요|the gate is locked tight⟧", 11, "var(--good)")
         + '<rect x="420" y="90" width="90" height="90" fill="none" stroke="var(--stone-dark)" stroke-width="6"/><path d="M465 90 v90 M420 135 h90" stroke="var(--stone-dark)" stroke-width="4"/>'
         + person(560, 100, s=0.85, face=MASK) + '<path d="M540 150 Q480 160 470 130" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + label(560, 262, "⟦창문으로 넘어와요|but climbs in the window⟧", 11, "var(--bad)")
         + label(380, 292, "⟦성문을 잠가도 창문이 열려 있으면 소용없어요|a locked gate is useless if a window is open⟧", 12, "var(--ink)", cls="d"))

# 3. 물리 보안 = 진짜 벽·자물쇠·경비 (hero)
P3 = svg(360, sky(360)
         + '<rect x="250" y="60" width="270" height="210" rx="6" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/>'
         + label(385, 88, "⟦서버실|SERVER ROOM⟧", 12, "var(--muted)", cls="d")
         + door(300, 150, 60, 110) + server_box(410, 120, 1.0)
         + cam(300, 110, 0.9) + person(150, 150, s=0.8, face=EYES, **GUARD) + card(100, 200, 1.0, rot=-8)
         + label(385, 250, "⟦카드 + 얼굴 + 경비 + 카메라|card + face + guard + camera⟧", 11, "var(--ink)")
         + label(380, 300, "⟦물리 보안은 진짜 벽·자물쇠·경비예요|physical security is real walls, locks, and guards⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦화면 속 자물쇠가 아니라, 손으로 만지는 문이에요|not a lock on a screen — a door you touch with your hand⟧", 11, "var(--muted)"))

# 4. 진짜 위험: 뒤따라 들어오기 (테일게이팅)
P4 = svg(300, sky(300)
         + door(300, 90, 70, 130, open_gap=True)
         + person(180, 100, s=0.85, face=SMILE, **GUEST) + card(150, 150, 0.9) + label(200, 250, "⟦카드 찍고 들어가요|badges in with a card⟧", 10, "var(--muted)")
         + person(430, 110, s=0.8, face=MASK, extra=BAG) + '<path d="M390 160 h40" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(470, 250, "⟦도둑은 바로 뒤에 붙어요|the thief slips in right behind⟧", 10, "var(--bad)")
         + bubble(480, 30, 250, 44, "⟦문지기는 한 번에 한 명씩만 통과시켜요|the doorkeeper lets one person through at a time⟧", 11, "var(--panel)", "var(--good)", "left")
         + label(380, 288, "⟦제일 흔한 도둑은 카드가 아니라 남의 등 뒤로 들어와요|the commonest thief comes not with a card but behind someone\'s back⟧", 11, "var(--ink)", cls="d"))

# 5. 여러 겹으로 막아요
P5 = svg(340, sky(340)
         + card(90, 70, 1.1) + '<circle cx="130" cy="70" r="14" fill="none" stroke="var(--stone-dark)" stroke-width="3"/><circle cx="130" cy="66" r="5" fill="var(--stone-dark)"/><path d="M122 80 q8 -8 16 0" stroke="var(--stone-dark)" stroke-width="3" fill="none"/>'
         + label(105, 130, "⟦카드 + 얼굴|card + face⟧", 11, "var(--ink)", cls="d") + label(105, 150, "⟦둘 다 맞아야 열려요|both must match⟧", 9, "var(--muted)")
         + '<rect x="240" y="45" width="80" height="55" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(280, 78, "⟦책상 위 비움|clean desk⟧", 9, "#142033") + paper(360, 75, 0.7, shred=True)
         + label(300, 130, "⟦책상 정리 + 파쇄|clean desk + shred⟧", 11, "var(--ink)", cls="d") + label(300, 150, "⟦버리는 종이는 잘게|torn to strips⟧", 9, "var(--muted)")
         + cam(470, 90, 1.0) + label(480, 130, "⟦카메라|cameras⟧", 11, "var(--ink)", cls="d") + label(480, 150, "⟦누가 언제 왔나|who came, when⟧", 9, "var(--muted)")
         + usb(600, 80, 1.2) + '<path d="M628 70 l16 16 M644 70 l-16 16" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(620, 130, "⟦주운 USB|a found USB⟧", 11, "var(--ink)", cls="d") + label(620, 150, "⟦절대 안 꽂아요|never plug it in⟧", 9, "var(--muted)")
         + '<path d="M60 190 h640" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="5 5"/>'
         + label(380, 235, "⟦불·물·전기도 도둑만큼 위험해요|fire, water, and power are as dangerous as any thief⟧", 12, "var(--ink)", cls="d")
         + '<g transform="translate(300,265)"><path d="M0 -14 q10 10 6 20 q-3 8 -6 8 q-10 -3 -8 -14 q2 -6 8 -14z" fill="var(--accent)"/></g>' + label(300, 305, "⟦불|fire⟧", 10, "var(--muted)")
         + '<g transform="translate(400,265)"><path d="M0 -16 q10 12 0 22 q-10 -10 0 -22z" fill="#5B9BD5"/></g>' + label(400, 305, "⟦물|water⟧", 10, "var(--muted)")
         + '<g transform="translate(500,265)"><path d="M4 -16 l-12 20 h10 l-4 14 l14 -22 h-10z" fill="#E9B44C"/></g>' + label(500, 305, "⟦전기|power⟧", 10, "var(--muted)")
         + label(380, 332, "⟦여러 겹 — 벽, 카드, 사람, 카메라, 그리고 불·물·전기 대비|many layers — walls, cards, people, cameras, and a plan for fire, water, power⟧", 11, "var(--muted)"))

CARD_I = icon('<rect x="10" y="18" width="44" height="30" rx="4" fill="#5B8DEF"/><circle cx="24" cy="30" r="6" fill="#FFF8E7"/><rect x="16" y="40" width="32" height="4" rx="2" fill="#FFF8E7"/><rect x="40" y="20" width="12" height="8" rx="2" fill="#E9B44C"/>')
TAIL_I = icon(f'<circle cx="22" cy="20" r="9" fill="{SKIN}"/><rect x="14" y="30" width="16" height="20" rx="4" fill="#4A5A72"/><circle cx="42" cy="22" r="8" fill="{SKIN}"/><path d="M40 24 h6 v10 h-4z" fill="#111C30"/><path d="M36 34 h12 v16 h-12z" fill="var(--bad)"/>')
CAM_I = icon('<rect x="28" y="8" width="6" height="18" fill="var(--stone-dark)"/><g transform="translate(31,26) rotate(15)"><rect x="-14" y="-8" width="36" height="18" rx="6" fill="var(--stone-dark)"/><circle cx="18" cy="1" r="7" fill="var(--panel)"/><circle cx="18" cy="1" r="3" fill="var(--night)"/></g>')
USB_I = icon(f'<circle cx="32" cy="32" r="22" fill="var(--bad)" opacity="0.15"/><rect x="18" y="28" width="24" height="12" rx="2" fill="#2E3D57"/><rect x="10" y="30" width="10" height="8" rx="1" fill="#C9C9C9"/><path d="M40 18 l10 10 M50 18 l-10 10" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "physical", "order": 112,
    "title": ("성문을 잠가도 창문이 열려 있으면", "A Locked Gate, an Open Window"),
    "h1": ("<em>물리 보안</em>이 뭐예요?", "What is <em>Physical Security</em>?"),
    "sub": ("물리 보안(Physical Security)을, 봉인 편지와 경비견이 아무리 많아도 서버실 문이 열려 있으면 소용없다는 이야기로 풀어봤어요.",
            "Physical security, told as a story about how sealed letters and guard dogs mean nothing if the door to the server room stands open."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽엔 봉인 편지 더미와 초록 체크의 경비견. 오른쪽 서버실 문은 활짝 열려 있고, 마스크 쓴 도둑이 자루를 메고 서버 상자를 들고 나감", "On the left, a stack of sealed letters and a green-checked guard dog. On the right the server-room door stands wide open, and a masked thief with a sack carries out a server box"),
         "caption": ("봉인 편지도 경비견도 있어요. 그런데 서버실 문이 열려 있어요.", "There are sealed letters and a guard dog. But the server-room door is open."),
         "small": ('<a href="encryption-ko.html">봉인 편지</a>도, <a href="edr-ko.html">경비견</a>도 소용없어요. 도둑이 서버실 문을 그냥 열고 상자를 들고 나가면 다 끝이에요.',
                   'The <a href="encryption-en.html">sealed letters</a> and the <a href="edr-en.html">guard dog</a> don\'t help. If the thief just opens the server-room door and carries the box out, it\'s all over.')},
        {"svg": P2, "alt": ("성문은 초록 자물쇠로 꽉 잠겨 있는데, 옆의 창문은 뻥 뚫려 있고 도둑이 그 창문으로 넘어 들어옴", "The gate is shut tight with a green lock, but the window beside it gapes open and a thief climbs in through it"),
         "caption": ("성문을 잠가도, 창문이 열려 있으면 소용없어요.", "A locked gate is useless if a window is open."),
         "small": ("화면 속 자물쇠(암호·방화벽)를 아무리 잠가도, 진짜 문과 창문이 열려 있으면 도둑은 그냥 걸어 들어와요. 벽은 손으로 만질 수 있어야 해요.", "No matter how tight the on-screen locks (passwords, firewalls), if a real door or window is open the thief simply walks in. A wall has to be one you can touch.")},
        {"svg": P3, "hero": True, "alt": ("서버실 앞에 카메라, 얼굴을 보는 경비, 출입 카드. 서버 상자는 안쪽에서 안전함", "In front of the server room: a camera, a guard checking a face, and an access card. The server box is safe inside"),
         "caption": ("물리 보안은 진짜 벽·자물쇠·경비예요.", "Physical security is real walls, locks, and guards."),
         "small": ("손으로 만지는 문, 카드로 여는 자물쇠, 얼굴을 보는 경비, 지켜보는 카메라. 화면 속이 아니라 진짜 세계에서 성을 지키는 일이에요.",
                   "A door you touch, a lock you open with a card, a guard who checks your face, a camera that watches. It\'s guarding the castle in the real world, not on a screen."),
         "tricks": (4, [
             (CARD_I, ("카드 + 얼굴", "Card + face"), ("문 하나에 두 가지 확인", "two checks at one door"), "calm"),
             (TAIL_I, ("뒤따라 들어오기", "Tailgating"), ("한 번에 한 명씩", "one person at a time"), "warm"),
             (CAM_I, ("카메라", "Cameras"), ("누가 언제 왔나 남겨요", "who came, and when")),
             (USB_I, ("주운 USB", "A found USB"), ("절대 안 꽂아요", "never plug it in"), "warm"),
         ])},
        {"svg": P4, "alt": ("손님이 카드를 찍고 열린 문으로 들어가고, 마스크 쓴 도둑이 바로 등 뒤에 붙어 따라 들어감. 문지기는 한 번에 한 명씩만 통과시킴", "A guest badges in with a card through the open door while a masked thief slips in right behind their back. The doorkeeper lets one person through at a time"),
         "caption": ("제일 흔한 도둑은 카드가 아니라 남의 등 뒤로 들어와요.", "The commonest thief comes not with a card but behind someone\'s back."),
         "small": ("이걸 테일게이팅이라고 해요. 문지기가 한 번에 한 명씩만 통과시키고, 방문객에겐 명찰을 주고 동행해요. 카드가 없어도 등 뒤는 늘 열려 있으니까요.",
                   "This is tailgating. The doorkeeper lets only one person through at a time, and visitors get a badge and an escort — because even without a card, someone\'s back is always an open door.")},
        {"svg": P5, "alt": ("여러 겹: 카드+얼굴, 책상 비우기와 파쇄, 카메라, ×표 그려진 주운 USB. 아래 줄엔 불·물·전기 아이콘", "Many layers: card + face, clean desk and shredding, cameras, a found USB marked ×. A bottom row shows fire, water, and power icons"),
         "caption": ("여러 겹으로 막고, 불·물·전기까지 대비해요.", "Guard in many layers — and plan for fire, water, and power too."),
         "small": ('카드에 얼굴을 더하고(<a href="mfa-ko.html">두 가지 확인</a>의 사촌), 책상 위 종이는 치우고(<a href="classification-ko.html">색 도장</a>대로), 버리는 종이는 <a href="retention-ko.html">잘게 파쇄</a>하고, 주운 USB는 <a href="airgap-ko.html">짐 검사</a>하듯 절대 안 꽂아요. 불·물·전기 대비는 <a href="drp-ko.html">불타도 다음 날 장사하는 법</a>과 이어져요.',
                   'Add a face to the card (a cousin of <a href="mfa-en.html">two-factor</a>), clear papers off the desk (by their <a href="classification-en.html">color stamp</a>), <a href="retention-en.html">shred</a> what you throw away, and never plug in a found USB (treat it like a <a href="airgap-en.html">bag check</a>). Planning for fire, water, and power ties into <a href="drp-en.html">doing business the day after it burns</a>.')},
    ],
    "summary": (("<b>물리 보안</b> = 화면 속 자물쇠 말고 <b>진짜 벽·자물쇠·경비·카메라</b>로 성을 지키는 일. 제일 흔한 틈은 <b>뒤따라 들어오기</b>·<b>주운 USB</b>·<b>안 치운 책상</b>이고, <b>불·물·전기</b>도 대비해요.",
                 "<b>Physical security</b> = guarding the castle with <b>real walls, locks, guards, and cameras</b>, not on-screen locks. The commonest gaps are <b>tailgating</b>, a <b>found USB</b>, and an <b>uncleared desk</b> — and you plan for <b>fire, water, and power</b> too."),
                ("Physical Security. 출입 통제, 방문자 관리, 서버실 잠금, 감시 카메라, 클린 데스크, 문서 파쇄처럼 물리적 세계에서 자산을 지키는 통제예요. 아무리 강한 논리적 보안도 서버를 그냥 들고 나갈 수 있으면 무너지고, 화재·수해·정전 같은 환경 위협도 여기서 함께 다뤄요.",
                 "Controls that protect assets in the physical world: access control, visitor management, locked server rooms, surveillance cameras, clean-desk policy, document shredding. The strongest logical security collapses if someone can just carry a server out, and environmental threats — fire, flood, power loss — are handled here too.")),
    "glossary": [
        ("물리 보안", "Physical security", ("진짜 벽·자물쇠·경비.", "Real walls, locks, guards."), ("화면 속이 아니라 손으로 만지는 세계에서 성을 지켜요. 서버를 들고 나가면 암호도 소용없어요.", "Guarding in the touchable world, not on a screen. If the server walks out, no password helps.")),
        ("출입 통제", "Access control", ("카드 + 얼굴.", "Card + face."), ('누가 어느 방에 들어갈 수 있나. 카드에 얼굴을 더하면 더 튼튼해요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'Who may enter which room. Adding a face to the card makes it sturdier. → <a href="mfa-en.html">the doorkeeper who checks three ways</a>')),
        ("테일게이팅", "Tailgating", ("남의 등 뒤로 들어오기.", "Slipping in behind a back."), ("카드 찍은 사람 뒤에 바짝 붙어 따라 들어와요. 한 번에 한 명씩만 통과시켜 막아요.", "Following closely behind someone who badged in. Stopped by letting one person through at a time.")),
        ("방문자 관리", "Visitor management", ("명찰과 동행.", "A badge and an escort."), ("손님에겐 명찰을 주고 누군가 동행해요. 혼자 돌아다니는 낯선 사람이 없게.", "Visitors get a badge and someone walks with them, so no stranger wanders alone.")),
        ("클린 데스크", "Clean desk", ("책상 위 비우기.", "An empty desktop."), ('자리를 뜰 때 종이를 다 치워요. 색 도장대로 넣어 둬요. → <a href="classification-ko.html">종이마다 찍는 색 도장</a>', 'Clear every paper when you leave, filed by its stamp. → <a href="classification-en.html">a colored stamp on every paper</a>')),
        ("감시 카메라", "Surveillance cameras", ("누가 언제 왔나.", "Who came, and when."), ("막지는 못해도, 누가 언제 왔는지 남겨요. 나중에 발자국을 굳혀 보는 데 써요.", "It can\'t stop entry, but it records who came and when — later used to fix the footprints in place.")),
        ("USB 드롭", "USB drop", ("주운 USB.", "A found USB."), ('도둑이 일부러 흘린 USB를 주워 꽂으면 벌레가 들어와요. 절대 안 꽂아요. → <a href="airgap-ko.html">다리 없는 섬 창고</a>', 'A thief drops a USB on purpose; plugging in a found one lets a bug in. Never plug it in. → <a href="airgap-en.html">the bridgeless island shed</a>')),
        ("환경 위협", "Environmental threats", ("불·물·전기.", "Fire, water, power."), ('도둑만 위험한 게 아니에요. 불·물·정전도 성을 무너뜨려요. → <a href="drp-ko.html">성이 불타도 다음 날 장사하는 법</a>', 'Thieves aren\'t the only danger — fire, flood, and blackout topple a castle too. → <a href="drp-en.html">doing business the day after it burns</a>')),
    ],
}
