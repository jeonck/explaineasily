from _draw import *

LAPTOP = ('<rect x="-16" y="-12" width="32" height="20" rx="2" fill="var(--night)"/><rect x="-14" y="-10" width="28" height="15" fill="var(--sky)"/>'
          '<rect x="-20" y="8" width="40" height="4" rx="2" fill="var(--stone-dark)"/>')
ROOM_W, ROOM_H, RX0, RY0 = 180, 110, 130, 60


def rooms(fill_each):
    """3×2 방. fill_each(col,row) 가 (배경색, 안에 그릴 것) 을 돌려준다."""
    out = f'<rect x="{RX0 - 14}" y="{RY0 - 14}" width="{3 * ROOM_W + 28}" height="{2 * ROOM_H + 28}" rx="8" fill="var(--stone-dark)"/>'
    for r in range(2):
        for c in range(3):
            x, y = RX0 + c * ROOM_W, RY0 + r * ROOM_H
            bg, inner = fill_each(c, r)
            out += f'<rect x="{x}" y="{y}" width="{ROOM_W - 6}" height="{ROOM_H - 6}" fill="{bg}"/>' \
                   f'<g transform="translate({x + 40},{y + 40})">{LAPTOP}</g>{inner}'
    return out


def at(c, r, dx, dy):
    return RX0 + c * ROOM_W + dx, RY0 + r * ROOM_H + dy


# 1. 성벽만 보면 방 안은 모른다
def p1_room(c, r):
    if (c, r) == (2, 1):
        x, y = at(2, 1, 100, 24)
        return "var(--panel)", person(x, y, s=0.55, face=MASK)
    return "var(--panel)", ""


WALL_GUARD = person(20, 20, hat="var(--good)", shirt="var(--good)", s=0.7, face=EYES + '<path d="M38 28 l14 -6" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/>')
P1 = svg(320, sky(320) + battlements(0, 0, 760, 12, "var(--stone)", 20) + rooms(p1_room) + WALL_GUARD
         + label(70, 130, "⟦밖만 봐요|looking out⟧", 13, "var(--muted)"))


# 2. 방마다 경비견 (hero)
def p2_room(c, r):
    x, y = at(c, r, 120, 70)
    return "var(--panel)", dog(x, y, 0.55)


P2 = svg(320, sky(320) + rooms(p2_room) + dog(90, 250, 1.4))

# 3. 얼굴이 아니라 행동을 본다
BOOK = '<rect x="46" y="70" width="34" height="26" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><path d="M63 70 v26" stroke="var(--accent)" stroke-width="2"/>'
SAFE = '<rect x="-70" y="60" width="60" height="60" rx="5" fill="var(--night)"/><circle cx="-40" cy="90" r="11" fill="none" stroke="var(--stone)" stroke-width="4"/>'
P3 = svg(280, '<rect width="380" height="280" fill="var(--good-soft)"/><rect x="380" width="380" height="280" fill="var(--bad-soft)"/>'
         + person(120, 60, hat=None, face=MASK, extra=BOOK) + dog(250, 200, 0.9, asleep=True)
         + label(190, 250, "⟦낯선 얼굴, 얌전함 → 조용|strange face, sitting still → quiet⟧", 15, "var(--muted)")
         + person(560, 60, hat="var(--good)", shirt="#4A5A72", face=SMILE, extra=SAFE) + dog(660, 200, 0.9, bark=True)
         + label(570, 250, "⟦아는 얼굴, 금고 열기 → 멍!|known face, opening the vault → WOOF!⟧", 15, "var(--muted)"))

# 4. 짖으면서 문을 잠근다
DOOR = ('<rect x="60" y="60" width="90" height="180" rx="6" fill="#8B5E3C"/>'
        '<rect x="88" y="130" width="34" height="30" rx="5" fill="var(--night)"/><path d="M96 130 V120 a9 9 0 0 1 18 0 V130" stroke="var(--night)" stroke-width="5" fill="none"/>')
MONITOR = ('<g transform="translate(600,70)"><rect width="120" height="86" rx="6" fill="var(--night)"/><rect x="8" y="8" width="104" height="62" fill="var(--bad)"/>'
           + label(60, 48, "⟦방 3 · 멍!|room 3 · WOOF⟧", 14, "#FFF") + '<rect x="48" y="86" width="24" height="10" fill="var(--stone-dark)"/></g>')
P4 = svg(280, '<rect width="760" height="280" fill="var(--panel)"/><rect y="240" width="760" height="40" fill="var(--sky)"/>' + DOOR
         + person(300, 100, s=0.9, face=MASK + SWEAT) + dog(400, 215, 0.9, bark=True)
         + '<path d="M430 150 Q520 90 596 100" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>' + MONITOR
         + label(660, 200, "⟦경비실|guard room⟧", 14, "var(--muted)"))


# 5. 개가 없는 방은 깜깜하다
def p5_room(c, r):
    if (c, r) in ((1, 0), (2, 1)):
        x, y = at(c, r, 120, 62)
        return "var(--night)", label(x, y, "?", 34, "var(--accent)", cls="d")
    x, y = at(c, r, 120, 70)
    return "var(--panel)", dog(x, y, 0.55)


P5 = svg(320, sky(320) + rooms(p5_room)
         + label(380, 305, "⟦오래된 프린터, 손님 노트북, 냉장고… 개를 못 앉히는 방도 있어요|the old printer, a guest laptop, the fridge… some rooms can\'t take a dog⟧", 14, "var(--muted)"))

EYE_I = icon('<path d="M6 32 Q32 8 58 32 Q32 56 6 32 Z" fill="none" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--good)"/>')
BARK_I = icon('<path d="M14 40 Q10 20 30 18 Q50 16 50 32 L40 34 L44 48 L28 40 Z" fill="var(--accent)"/><path d="M52 14 l6 -6 M56 26 l8 -2" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
LOCK_I = icon('<rect x="16" y="28" width="32" height="26" rx="5" fill="var(--bad)"/><path d="M22 28 V20 a10 10 0 0 1 20 0 V28" stroke="var(--bad)" stroke-width="5" fill="none"/>')

PAGE = {
    "slug": "edr", "order": 9,
    "title": ("방마다 한 마리 경비견", "A Dog in Every Room"),
    "h1": ("<em>EDR</em>이 뭐예요?", "What is <em>EDR</em>?"),
    "sub": ("엔드포인트 탐지·대응(Endpoint Detection and Response)을 방마다 있는 경비견 이야기로 풀어봤어요.",
            "Endpoint Detection and Response, told as a story about a guard dog in every room."),
    "panels": [
        {"svg": P1, "alt": ("성벽 위 경비는 바깥만 보고, 성 안 여섯 개 방 중 하나에 도둑이 이미 들어와 있음", "A guard on the wall looks outward while a burglar is already inside one of six rooms"),
         "caption": ("성벽만 보면 방 안은 몰라요.", "Watching the wall tells you nothing about the rooms."),
         "small": ("방 하나가 컴퓨터 한 대예요. 도둑이 이미 방 안에 있으면요?", "Each room is one computer. What if the burglar is already inside?")},
        {"svg": P2, "hero": True, "alt": ("여섯 개 방마다 개가 한 마리씩 앉아 있고, 앞에 큰 경비견", "A dog sitting in each of six rooms, with a big guard dog in front"),
         "caption": ("EDR은 방마다 한 마리씩 있는 경비견이에요.", "EDR is a guard dog in every room."),
         "small": ("방 안에서 일어나는 일을 전부 보고, 적어둬요.", "It watches everything that happens in the room, and writes it down."),
         "tricks": (3, [
             (EYE_I, ("지켜보기", "Watch"), ("누가 뭘 열고 실행하나", "who opens and runs what"), "calm"),
             (BARK_I, ("짖기", "Bark"), ("이상한 행동이면", "at strange behavior"), "warm"),
             (LOCK_I, ("물고 잠그기", "Bite and lock"), ("붙잡고 방 문을 잠가요", "hold them, lock the door")),
         ])},
        {"svg": P3, "alt": ("왼쪽은 책 읽는 낯선 사람 옆에 자는 개, 오른쪽은 금고를 여는 아는 얼굴에게 짖는 개", "Left: a dog asleep beside a masked stranger reading; right: a dog barking at a familiar face opening the vault"),
         "caption": ("얼굴이 아니라 행동을 봐요.", "It watches what you do, not what you look like."),
         "small": ('예전 문지기(백신)는 얼굴 사진만 봤어요. 경비견은 <a href="ttp-ko.html">버릇</a>을 봐요.',
                   'The old gatekeeper (antivirus) only checked faces. The dog watches <a href="ttp-en.html">habits</a>.')},
        {"svg": P4, "alt": ("자물쇠가 잠긴 문, 도둑에게 짖는 개, 경비실 화면으로 이어진 점선", "A locked door, a dog barking at the burglar, and a dotted line to a red guard-room screen"),
         "caption": ("짖으면서 방 문을 잠가요.", "It barks, and locks the door."),
         "small": ('도둑이 다른 방으로 못 가게. 그리고 <a href="soc-ko.html">경비실</a>에 알려요.',
                   'So the burglar can\'t reach other rooms. Then it tells the <a href="soc-en.html">guard room</a>.')},
        {"svg": P5, "alt": ("여섯 방 중 넷엔 개가 있고 둘은 깜깜한 채 물음표만 떠 있음", "Four rooms have dogs; two are dark with only a question mark"),
         "caption": ("개가 없는 방은 깜깜해요.", "A room with no dog is dark."),
         "small": ('개는 자기 방만 봐요. 방과 방 사이 이야기는 <a href="siem-ko.html">큰 화면</a>에서 이어 붙여요.',
                   'Each dog sees only its own room. Stories across rooms are joined on the <a href="siem-en.html">big screen</a>.')},
    ],
    "summary": (("<b>EDR</b> = 방(컴퓨터)마다 한 마리씩 있는 <b>경비견</b>. 행동을 보고, 짖고, 문을 잠가요.",
                 "<b>EDR</b> = a <b>guard dog</b> in every room (computer). It watches behavior, barks, and locks the door."),
                ("Endpoint Detection and Response. 성벽(네트워크)이 아니라 방 안(컴퓨터 안)을 봐요. 백신이 얼굴 사진을 봤다면, EDR은 행동을 봐요.",
                 "Endpoint Detection and Response. It watches inside the room (the computer), not the wall (the network). Antivirus checked faces; EDR watches behavior.")),
    "glossary": [
        ("엔드포인트", "Endpoint", ("방 하나.", "One room."), ("노트북, 서버, 휴대폰 — 사람이나 프로그램이 일하는 컴퓨터 한 대.", "A laptop, a server, a phone — any one computer where work happens.")),
        ("에이전트", "Agent", ("경비견.", "The dog."), ("방마다 설치하는 작은 프로그램. 이게 없으면 그 방은 깜깜해요.", "A small program installed in each room. Without it, that room is dark.")),
        ("백신", "Antivirus", ("얼굴 사진 문지기.", "The photo gatekeeper."), ("이미 아는 나쁜 파일의 사진(시그니처)과 맞춰봐요. 변장하면 못 알아봐요.", "Matches known bad files against photos (signatures). A disguise gets past it.")),
        ("행동 탐지", "Behavioral detection", ("행동 보기.", "Watching behavior."), ('누구든 금고를 열면 짖어요. → <a href="ttp-ko.html">버릇 이야기</a>', 'Whoever opens the vault gets barked at. → <a href="ttp-en.html">the habit story</a>')),
        ("격리", "Isolation", ("방 문 잠그기.", "Locking the room."), ("그 컴퓨터를 다른 컴퓨터들과 잠시 떼어놓는 것.", "Cutting that computer off from the others for a while.")),
        ("원격 대응", "Response", ("물기.", "The bite."), ("멀리서 나쁜 프로그램을 멈추고 파일을 지우는 것.", "Stopping the bad program and deleting files, from afar.")),
        ("텔레메트리", "Telemetry", ("개의 일기.", "The dog's diary."), ('방 안에서 본 것을 전부 적은 기록. <a href="siem-ko.html">큰 화면</a>으로 보내요.', 'Everything the dog saw, written down and sent to the <a href="siem-en.html">big screen</a>.')),
    ],
}
