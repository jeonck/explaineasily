from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
DOORS = tuple(("", False) for _ in range(5))


def socket(x, y, s=1.0, light=None):
    lamp = f'<circle cx="0" cy="-22" r="6" fill="{ {"ok": "var(--good)", "no": "var(--bad)", "wait": "#E9B44C"}[light] }"/>' if light else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-14" width="32" height="28" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<rect x="-8" y="-6" width="5" height="12" fill="var(--night)"/><rect x="3" y="-6" width="5" height="12" fill="var(--night)"/>{lamp}</g>')


def laptop(x, y, s=1.0, tag=""):
    t = (f'<rect x="-26" y="-48" width="52" height="18" rx="4" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>' + label(0, -35, tag, 10, "var(--good)")) if tag else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-18" width="48" height="30" rx="2" fill="var(--night)"/><rect x="-21" y="-15" width="42" height="23" fill="var(--sky)"/>'
            f'<rect x="-30" y="12" width="60" height="5" rx="2" fill="var(--stone-dark)"/>{t}</g>')


def bugbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-18" width="44" height="36" rx="3" fill="#8B5E3C"/><path d="M-22 -18 L22 18 M22 -18 L-22 18" stroke="#5A3B22" stroke-width="3"/>'
            f'<path d="M-14 18 l-4 12 M0 18 v12 M14 18 l4 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><circle cx="0" cy="-2" r="6" fill="var(--bad)"/></g>')


def printer(x, y, s=1.0, mud=False):
    m = '<path d="M-20 22 q8 -6 14 0 q6 6 12 0 q6 -6 14 0" stroke="#7A5236" stroke-width="4" fill="none"/>' if mud else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-6" width="52" height="28" rx="3" fill="var(--stone)"/><rect x="-16" y="-20" width="32" height="16" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            f'<rect x="-18" y="10" width="36" height="6" fill="var(--stone-dark)"/>{m}</g>')


def fridge(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-34" width="32" height="68" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-16 -8 h32" stroke="var(--stone-dark)" stroke-width="3"/><rect x="8" y="-26" width="3" height="12" fill="var(--stone-dark)"/><rect x="8" y="0" width="3" height="16" fill="var(--stone-dark)"/></g>')


def cable(x1, y1, x2, y2, color="var(--night)"):
    return f'<path d="M{x1} {y1} C{x1} {y2} {x2} {y1} {x2} {y2}" stroke="{color}" stroke-width="3" fill="none"/>'


SOCKETS_X = (32, 172, 312, 452, 592, 732)

# 1. 복도 벽마다 꽂는 구멍
P1 = svg(280, corridor(280, DOORS, marks=False) + "".join(socket(x, 150) for x in SOCKETS_X)
         + '<g transform="translate(312,6)"><path d="M-30 30 a40 40 0 0 1 60 0 M-18 42 a24 24 0 0 1 36 0 M-6 54 a8 8 0 0 1 12 0" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
         + label(312, 76, "⟦와이파이도 구멍이에요|Wi-Fi is a socket too⟧", 10, "var(--muted)")
         + label(380, 262, "⟦꽂기만 하면 복도에 연결돼요|plug in, and you\'re on the hallway⟧", 14, "var(--muted)"))

# 2. 아무 물건이나 꽂힌다
P2 = svg(300, corridor(300, DOORS, marks=False) + "".join(socket(x, 150) for x in SOCKETS_X)
         + cable(172, 164, 172, 220) + laptop(172, 230, 0.8) + label(172, 270, "⟦손님 노트북|guest laptop⟧", 11, "var(--muted)")
         + cable(452, 164, 452, 220) + bugbox(452, 232, 0.9) + label(452, 275, "⟦낯선 상자|a strange box⟧", 11, "var(--bad)")
         + cable(732, 164, 700, 220) + printer(700, 232, 0.9, mud=True) + label(690, 275, "⟦진흙 묻은 프린터|a muddy printer⟧", 11, "var(--muted)")
         + '<path d="M480 236 C540 200 580 250 620 215" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + label(570, 200, "⟦꽂힌 뒤엔 어디든|once in, anywhere⟧", 11, "var(--bad)"))

# 3. NAC = 꽂히는 순간 묻는다 (hero)
QUESTIONS = (bubble(260, 20, 160, 32, "⟦성 물건 맞아?|Do you belong here?⟧", 12, "var(--panel)", "var(--good)", "bottom")
             + bubble(290, 62, 160, 32, "⟦최근에 씻었어?|Washed recently?⟧", 12, "var(--panel)", "var(--good)", "bottom")
             + bubble(320, 104, 190, 32, "⟦경비견 데리고 있어?|Got your dog with you?⟧", 12, "var(--panel)", "var(--good)", "bottom"))
P3 = svg(340, corridor(340, DOORS, marks=False)
         + socket(452, 150, 1.2, light="ok") + person(392, 150, s=0.55, face=EYES, **GUARD) + QUESTIONS
         + cable(452, 168, 520, 230) + laptop(520, 240, 1.0, tag="⟦성 물건 · 씻음 ✓|castle-owned · clean ✓⟧")
         + dog(610, 262, 0.5)
         + label(380, 322, "⟦사람은 문지기가, 물건은 NAC이 확인해요|the gatekeeper checks people; NAC checks things⟧", 13, "var(--muted)"))

# 4. 통과 못 하면 손님 복도로만
P4 = svg(320, '<rect width="760" height="320" fill="var(--panel)"/>'
         + '<rect x="0" y="40" width="760" height="90" fill="var(--good-soft)"/>' + label(70, 90, "⟦본 복도|main hallway⟧", 14, "var(--good)", cls="d")
         + laptop(300, 88, 0.7, tag="✓") + printer(440, 90, 0.7) + dog(560, 100, 0.45)
         + '<rect x="0" y="150" width="380" height="70" fill="var(--sky)"/>' + label(70, 190, "⟦손님 복도|guest hallway⟧", 14, "var(--ink)", cls="d")
         + laptop(230, 190, 0.6) + label(320, 190, "⟦→ 마당(인터넷)만|→ yard (internet) only⟧", 11, "var(--muted)")
         + '<rect x="0" y="240" width="380" height="70" fill="var(--accent-soft)"/>' + label(70, 280, "⟦세탁실|laundry room⟧", 14, "var(--accent)", cls="d")
         + printer(230, 282, 0.6, mud=True) + label(320, 280, "⟦→ 씻고(업데이트) 다시|→ wash (update), then retry⟧", 11, "var(--muted)")
         + '<rect x="400" y="150" width="360" height="160" fill="var(--bad-soft)"/>' + bugbox(500, 230, 0.9)
         + '<path d="M470 200 l60 60 M530 200 l-60 60" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>'
         + label(640, 235, "⟦낯선 상자는 아예 안 꽂혀요|the strange box never connects⟧", 12, "var(--bad)"))

# 5. 이름표를 못 다는 물건이 많다
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + fridge(110, 120, 1.1) + label(110, 190, "⟦냉장고|fridge⟧", 12, "var(--muted)")
         + '<g transform="translate(240,110)"><rect x="-22" y="-14" width="44" height="28" rx="4" fill="var(--stone-dark)"/><circle r="8" fill="var(--sky)"/><rect x="-6" y="-24" width="12" height="10" fill="var(--stone-dark)"/></g>' + label(240, 190, "⟦카메라|camera⟧", 12, "var(--muted)")
         + printer(370, 120, 1.0) + label(370, 190, "⟦오래된 프린터|old printer⟧", 12, "var(--muted)")
         + "".join(label(x, 62, "⟦이름표 ×|no tag ×⟧", 11, "var(--bad)") for x in (110, 240, 370))
         + person(520, 60, s=0.8, face=EYES, **GUARD)
         + bubble(500, 0, 240, 34, "⟦얼굴(MAC)로만 알아봐야 해요|only a face (MAC) to go by⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(640, 120, s=0.7, face=MASK, extra=f'<g transform="translate(64,40)"><rect x="-18" y="-10" width="36" height="20" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>{label(0, 4, "⟦프린터|printer⟧", 9, "#142033")}</g>')
         + label(660, 250, "⟦얼굴은 흉내 낼 수 있어요|a face can be faked⟧", 12, "var(--bad)"))

TAG_I = icon('<rect x="10" y="18" width="44" height="28" rx="6" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><circle cx="20" cy="32" r="4" fill="var(--good)"/><rect x="28" y="30" width="18" height="4" fill="var(--good)"/>')
WASH_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="#5B9BD5" stroke-width="4"/><path d="M22 34 q5 -8 10 0 t10 0" stroke="#5B9BD5" stroke-width="3" fill="none"/>')
HALL_I = icon('<rect x="8" y="14" width="48" height="14" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/><rect x="8" y="36" width="48" height="14" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="2"/>')
GUEST_I = icon('<rect x="8" y="36" width="48" height="14" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="2"/><path d="M40 16 a8 8 0 0 1 0 16 M46 10 a14 14 0 0 1 0 28" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "nac", "order": 26,
    "title": ("복도 구멍마다 문지기", "The Gatekeeper at Every Socket"),
    "h1": ("<em>NAC</em>이 뭐예요?", "What is <em>NAC</em>?"),
    "sub": ("네트워크 접근 제어(Network Access Control)를 복도 구멍마다 서 있는 문지기 이야기로 풀어봤어요.",
            "Network Access Control, told as a story about a gatekeeper at every wall socket."),
    "panels": [
        {"svg": P1, "alt": ("복도 벽에 구멍(콘센트) 다섯 개와 와이파이 표시", "Five wall sockets along the hallway, and a Wi-Fi symbol"),
         "caption": ("복도 벽마다 꽂는 구멍이 있어요.", "The hallway has sockets all along the wall."),
         "small": ('꽂기만 하면 <a href="ndr-ko.html">복도</a>에 연결돼요. 랜선 구멍도, 와이파이도요.',
                   'Plug in, and you\'re on the <a href="ndr-en.html">hallway</a>. Cable sockets, and Wi-Fi too.')},
        {"svg": P2, "alt": ("손님 노트북, 다리 달린 낯선 상자, 진흙 묻은 프린터가 구멍에 꽂혀 있고, 상자에서 복도 곳곳으로 점선", "A guest laptop, a strange box with legs, and a muddy printer plugged into sockets; a dotted line runs from the box down the hallway"),
         "caption": ("아무 물건이나 꽂혀요.", "Anything can be plugged in."),
         "small": ("손님 노트북, 낯선 상자, 오래된 프린터… 꽂힌 뒤엔 복도 어디든 갈 수 있어요.", "A guest laptop, a strange box, an old printer… and once in, they can go anywhere.")},
        {"svg": P3, "hero": True, "alt": ("구멍 옆 작은 문지기가 '성 물건 맞아? 최근에 씻었어? 경비견 데리고 있어?' 묻고, 이름표 달린 노트북이 초록불로 연결됨", "A small gatekeeper by the socket asks Do you belong here? Washed recently? Got your dog?; a tagged laptop connects with a green light"),
         "caption": ("NAC은 꽂히는 순간 물건에게 물어봐요.", "NAC questions the thing the moment it's plugged in."),
         "small": ('"성 물건 맞아? 최근에 씻었어(업데이트)? <a href="edr-ko.html">경비견</a> 데리고 있어(백신)?"', '"Do you belong here? Washed recently (updated)? Got your <a href="edr-en.html">dog</a> (antivirus)?"'),
         "tricks": (4, [
             (TAG_I, ("이름표", "The tag"), ("성이 달아준 것만 믿어요", "only castle-issued ones count"), "calm"),
             (WASH_I, ("씻었나", "Washed?"), ("업데이트, 백신, 암호화", "updates, antivirus, encryption")),
             (HALL_I, ("어느 복도로", "Which hallway"), ("답에 따라 복도가 달라요", "the answers pick the hallway"), "warm"),
             (GUEST_I, ("손님 복도", "Guest hallway"), ("마당만 가는 좁은 길", "a narrow road to the yard only"), "calm"),
         ])},
        {"svg": P4, "alt": ("본 복도엔 체크된 노트북과 프린터와 개, 손님 복도엔 손님 노트북(마당만), 세탁실엔 진흙 프린터, 낯선 상자엔 X", "Main hallway: checked laptop, printer and dog; guest hallway: the guest laptop (yard only); laundry room: the muddy printer; the strange box crossed out"),
         "caption": ("통과 못 하면 손님 복도로만 보내요.", "Fail the check, and you get the guest hallway."),
         "small": ("손님 노트북은 마당(인터넷)만 가는 좁은 복도로. 진흙 묻은 프린터는 세탁실(업데이트)부터. 낯선 상자는 아예 안 꽂혀요.", "Guest laptops get a narrow hallway to the yard (internet) only. The muddy printer goes to the laundry room (updates) first. The strange box never connects.")},
        {"svg": P5, "alt": ("이름표 없는 냉장고, 카메라, 오래된 프린터. 문지기는 '얼굴(MAC)로만 알아봐야 해요', 옆에 '프린터' 가면을 든 도둑", "A fridge, a camera and an old printer with no tags; the gatekeeper says only a face (MAC) to go by; a thief holds up a printer mask"),
         "caption": ("이름표를 못 다는 물건이 많아요.", "Lots of things can't wear a tag."),
         "small": ("냉장고, 카메라, 오래된 프린터는 이름표를 못 달아요. 그래서 얼굴(MAC 주소)로만 알아보는데, 얼굴은 흉내 낼 수 있어요.", "Fridges, cameras and old printers can't wear one. So they're known by face (MAC address) alone — and a face can be faked.")},
    ],
    "summary": (("<b>NAC</b> = 복도에 뭔가 <b>꽂히는 순간</b> '성 물건인지, 씻었는지' 묻고, 아니면 <b>손님 복도</b>로만 보내는 문지기.",
                 "<b>NAC</b> = the gatekeeper that, <b>the moment something plugs in</b>, asks whether it belongs and whether it's clean — and sends the rest to the <b>guest hallway</b>."),
                ("Network Access Control. 사람은 문지기(MFA)가, 물건은 NAC이 확인해요. 문마다 물어보는 성(제로 트러스트)의 복도 판이에요. Cisco ISE, Aruba ClearPass, FortiNAC 같은 것들.",
                 "Network Access Control. The gatekeeper (MFA) checks people; NAC checks things. It's the castle that always asks, applied to the hallway. Cisco ISE, Aruba ClearPass, FortiNAC.")),
    "glossary": [
        ("802.1X", "802.1X", ("꽂힐 때 이름표 보여주기.", "Show your tag when you plug in."), ("구멍이 먼저 묻고, 물건이 답하는 규칙.", "The rule: the socket asks first, the thing answers.")),
        ("인증서", "Certificate", ("성이 달아준 이름표.", "A castle-issued tag."), ('흉내 내기 어려워요. → <a href="passkey-ko.html">성문을 알아보는 반지</a>와 같은 원리', 'Hard to fake. → same idea as <a href="passkey-en.html">the ring that knows the gate</a>')),
        ("MAC 주소", "MAC address", ("물건의 얼굴.", "The thing\'s face."), ("이름표가 없을 때 보는 것. 흉내 낼 수 있어요.", "What you check when there\'s no tag. Can be faked.")),
        ("상태 검사", "Posture check", ("씻었나.", "Washed?"), ('업데이트, 백신, 디스크 암호화. → <a href="zerotrust-ko.html">신발에 진흙</a>', 'Updates, antivirus, disk encryption. → <a href="zerotrust-en.html">mud on the shoes</a>')),
        ("VLAN", "VLAN", ("복도 나누기.", "Splitting the hallway."), ('본 복도, 손님 복도, 세탁실. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Main, guest, laundry. → <a href="ndr-en.html">the hallway watcher</a>')),
        ("격리 · 교정", "Quarantine · remediation", ("세탁실.", "The laundry room."), ("씻고(업데이트하고) 다시 와요.", "Wash (update), then come back.")),
        ("게스트 네트워크", "Guest network", ("손님 복도.", "The guest hallway."), ("마당(인터넷)만 가고 방엔 못 들어가요.", "Reaches the yard (internet) but no rooms.")),
        ("프로파일링", "Profiling", ("생김새로 알아맞히기.", "Guessing by looks."), ('"이건 프린터같이 생겼네." 이름표 없는 물건을 분류하는 방법.', '"This looks like a printer." How untagged things get sorted.')),
    ],
}
