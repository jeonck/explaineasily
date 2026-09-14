from _draw import *

ME = dict(hat=None, shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
NEW_BUG = "#7B3FA0"   # 카드에 없는 새 벌레 — 다른 색이 곧 의미


def bug(x, y, s=1.0, color="var(--bad)", eyes=True):
    e = '<circle cx="-14" cy="-2" r="2" fill="#FFF"/><circle cx="-8" cy="-2" r="2" fill="#FFF"/>' if eyes else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><circle cx="-12" cy="-4" r="8" fill="{color}"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8 M-14 -9 l-3 -6 M-8 -11 l1 -6" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>{e}</g>')


def parcel(x, y, s=1.0, inner="", cross=False):
    cx = '<path d="M-22 -18 l44 36 M22 -18 l-44 36" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>' if cross else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-28" y="-22" width="56" height="44" rx="3" fill="#8B5E3C"/>'
            f'<rect x="-28" y="-4" width="56" height="8" fill="#C9A86A"/><rect x="-4" y="-22" width="8" height="44" fill="#C9A86A"/>{inner}{cx}</g>')


def card(x, y, s=1.0, color="var(--bad)", rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-20" y="-28" width="40" height="56" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'{bug(2, -2, 0.55, color, eyes=False)}<path d="M-12 18 h24" stroke="#142033" stroke-width="2" stroke-linecap="round"/></g>')


def fan(x, y, s=1.0):
    return card(x - 14, y, s, "var(--bad)", -18) + card(x, y - 4, s, "#B5382C", 0) + card(x + 14, y, s, "var(--accent)", 18)


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def door(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="90" height="170" rx="6" fill="{WOOD}"/><circle cx="74" cy="90" r="5" fill="#E9B44C"/></g>'


def chewed(x, y):
    return (f'<g transform="translate({x},{y})"><rect x="-22" y="-28" width="44" height="56" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<circle cx="10" cy="-16" r="7" fill="var(--bad-soft)"/><circle cx="-12" cy="10" r="6" fill="var(--bad-soft)"/><circle cx="14" cy="18" r="5" fill="var(--bad-soft)"/></g>')


# 1. 상자는 매일 와요 — 어떤 상자엔 벌레가 숨어 있어요
P1 = svg(300, sky(300)
         + door(60, 70) + label(105, 55, "⟦내 방|my room⟧", 13, "var(--ink)", cls="d")
         + '<path d="M600 200 H190" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'
         + parcel(230, 200) + parcel(330, 200) + parcel(430, 200) + parcel(530, 200, inner=bug(18, -30, 0.7))
         + "".join(label(x, 250, t, 11, "var(--muted)") for x, t in ((230, "⟦그림책|picture book⟧"), (330, "⟦장난감|toy⟧"), (430, "⟦편지|letter⟧"), (530, "⟦?|?⟧")))
         + person(640, 100, s=0.85, face=EYES, **ME)
         + label(380, 285, "⟦상자는 매일 와요 — 어떤 상자엔 벌레가 숨어 있어요|boxes come every day — and some hide a bug⟧", 13, "var(--ink)", cls="d"))

# 2. 상자를 다 열어볼 수는 없어요 — 한 마리면 충분해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(70, 100, s=0.9, face=FROWN + SWEAT, **ME)
         + parcel(230, 205, 0.9) + parcel(295, 205, 0.9) + parcel(360, 205, 0.9) + parcel(262, 165, 0.9) + parcel(327, 165, 0.9) + parcel(295, 125, 0.9)
         + label(295, 255, "⟦하루에 백 상자|a hundred boxes a day⟧", 11, "var(--muted)")
         + bug(490, 150, 1.3) + chewed(575, 160) + chest(670, 175, 1.0, lock=True)
         + label(600, 255, "⟦종이를 갉고, 상자를 잠가요|chews the papers, locks the chests⟧", 11, "var(--bad)")
         + label(380, 288, "⟦다 열어볼 순 없는데, 벌레는 한 마리면 충분해요|you can\'t open every box — and one bug is enough⟧", 13, "var(--ink)", cls="d"))

# 3. 방마다 벌레 카드를 든 경비 (hero)
P3 = svg(360, sky(360)
         + door(40, 60, 0.95) + door(200, 60, 0.95) + door(360, 60, 0.95)
         + person(60, 120, s=0.8, face=EYES, **GUARD) + fan(140, 175, 0.7)
         + person(220, 120, s=0.8, face=EYES, **GUARD) + fan(300, 175, 0.7)
         + person(380, 120, s=0.8, face=EYES, **GUARD) + fan(460, 175, 0.7)
         + parcel(100, 250, 0.7) + parcel(260, 250, 0.7) + parcel(420, 250, 0.7)
         + '<rect x="560" y="40" width="150" height="190" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + bug(635, 120, 2.0, eyes=False) + label(635, 62, "⟦벌레 카드 4번|BUG CARD No. 4⟧", 12, "#142033", cls="d")
         + label(635, 190, "⟦다리 여섯, 빨간 등|six legs, red back⟧", 10, "#142033") + label(635, 210, "⟦상자 잠그는 벌레|the chest-locking bug⟧", 10, "#142033")
         + label(635, 258, "⟦벌레마다 카드 한 장|one card per bug⟧", 11, "var(--muted)")
         + label(380, 305, "⟦들어오는 상자를 카드와 하나하나 비교해요|every incoming box is compared against the cards⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦카드와 같으면 문 앞에서 막아요|if it matches a card, it\'s stopped at the door⟧", 12, "var(--muted)"))

# 4. 카드에 없는 새 벌레 — 그래서 요즘은 행동도 봐요
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(50, 110, s=0.85, face=EYES, **GUARD) + fan(130, 165, 0.7)
         + bug(240, 165, 1.1, NEW_BUG) + label(240, 110, "?", 30, "var(--accent)", cls="d")
         + '<path d="M275 165 H340" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M332 157 l10 8 l-10 8" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + label(190, 245, "⟦카드에 없는 새 벌레는 그냥 지나가요|a bug on no card just walks past⟧", 11, "var(--ink)")
         + bug(470, 150, 1.1, NEW_BUG) + chest(540, 180, 1.0, lock=True) + chest(615, 180, 1.0, lock=True)
         + person(660, 90, s=0.8, face=EYES, **GUARD) + '<path d="M650 165 l-30 -8" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>'
         + label(570, 245, "⟦상자를 마구 잠그면 — 벌레예요!|starts locking chests — that\'s a bug!⟧", 11, "var(--ink)")
         + label(380, 300, "⟦요즘 경비는 얼굴 말고 하는 짓도 봐요|today\'s guards watch what it does, not just its face⟧", 13, "var(--ink)", cls="d"))

# 5. 카드 경비는 문 앞에서, 경비견은 들어온 뒤에
P5 = svg(340, sky(340)
         + door(40, 60) + person(150, 120, s=0.85, face=EYES, **GUARD) + fan(225, 170, 0.7)
         + parcel(250, 245, 0.8, inner=bug(0, -4, 0.7, eyes=False), cross=True)
         + label(160, 290, "⟦카드 경비 — 문 앞에서 막아요|card guard — stops it at the door⟧", 11, "var(--ink)")
         + '<rect x="420" y="60" width="300" height="200" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + dog(520, 215, 0.9, bark=True) + bug(650, 175, 1.0, NEW_BUG) + '<path d="M600 195 l30 -12" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(570, 290, "⟦경비견 — 들어온 뒤에 쫓아요|guard dog — chases it once inside⟧", 11, "var(--ink)")
         + label(380, 325, "⟦둘이 같이 있어야 성이 안전해요|the castle needs both⟧", 13, "var(--ink)", cls="d"))

CARD_I = icon('<rect x="16" y="8" width="32" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><ellipse cx="32" cy="28" rx="10" ry="7" fill="var(--bad)"/><circle cx="24" cy="25" r="5" fill="var(--bad)"/><path d="M26 20 l-3 -5 M38 21 l3 -5 M24 34 l-4 5 M40 34 l4 5" stroke="var(--bad)" stroke-width="2" stroke-linecap="round"/>')
NEW_I = icon('<rect x="10" y="12" width="28" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="26" y="20" width="28" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M40 30 v20 M30 40 h20" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
STOP_I = icon('<rect x="8" y="10" width="26" height="46" rx="3" fill="#8B5E3C"/><circle cx="52" cy="32" r="11" fill="var(--bad)"/><path d="M46 26 l12 12 M58 26 l-12 12" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>')
JAR_I = icon('<rect x="16" y="20" width="32" height="36" rx="5" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="14" y="12" width="36" height="10" rx="2" fill="var(--stone-dark)"/><ellipse cx="32" cy="42" rx="8" ry="5" fill="var(--bad)"/><circle cx="26" cy="40" r="4" fill="var(--bad)"/>')

PAGE = {
    "slug": "antivirus", "order": 86,
    "title": ("벌레 그림 카드를 든 경비", "The Guard with the Bug Cards"),
    "h1": ("<em>안티바이러스</em>가 뭐예요?", "What is <em>Antivirus</em>?"),
    "sub": ("안티바이러스와 엔드포인트 보호(EPP)를 방마다 벌레 그림 카드를 들고 상자를 검사하는 경비 이야기로 풀어봤어요.",
            "Antivirus and endpoint protection (EPP), told as a story about a guard in every room checking boxes against a deck of bug cards."),
    "panels": [
        {"svg": P1, "alt": ("내 방 문 앞으로 상자 네 개가 줄지어 오고 — 그림책, 장난감, 편지 — 마지막 상자에서 벌레가 고개를 내밈. 상자를 받는 사람은 모름", "Four boxes line up at my room\'s door — a picture book, a toy, a letter — and a bug peeks out of the last one. The person receiving them has no idea"),
         "caption": ("상자는 매일 와요. 어떤 상자엔 벌레가 숨어 있어요.", "Boxes come every day. Some of them hide a bug."),
         "small": ('방 하나가 컴퓨터 한 대예요. 상자는 내려받은 파일, 편지에 붙은 첨부, 꽂은 저장 막대예요. <a href="malware-ko.html">벌레</a>는 그 안에 숨어요.',
                   'Each room is one computer. The boxes are downloaded files, attachments on letters, plugged-in sticks. A <a href="malware-en.html">bug</a> hides inside them.')},
        {"svg": P2, "alt": ("땀 흘리는 사람 앞에 상자가 산더미로 쌓여 있고, 반대쪽에선 벌레 한 마리가 종이를 갉고 상자를 잠가 버림", "A sweating person faces a mountain of boxes, while on the other side a single bug chews papers and locks a chest"),
         "caption": ("상자를 다 열어볼 순 없어요. 그런데 벌레는 한 마리면 충분해요.", "You can\'t open every box yourself. But one bug is enough."),
         "small": ('하루에 백 상자를 혼자 뜯어볼 수는 없어요. 그런데 한 마리만 들어와도 종이를 갉고, <a href="ransomware-ko.html">상자를 잠그고</a>, 친구를 불러요.',
                   'Nobody can open a hundred boxes a day by hand. Yet a single bug that gets in chews the papers, <a href="ransomware-en.html">locks the chests</a>, and calls its friends.')},
        {"svg": P3, "hero": True, "alt": ("방 세 개 앞에 경비가 한 명씩 벌레 그림 카드를 부채처럼 들고 서 있고, 발치에 상자가 하나씩. 오른쪽에 크게 그린 '벌레 카드 4번' — 다리 여섯, 빨간 등, 상자 잠그는 벌레", "A guard stands at each of three doors holding a fan of bug-picture cards, a box at their feet. On the right, a big 'Bug Card No. 4' — six legs, red back, the chest-locking bug"),
         "caption": ("안티바이러스는 방마다 벌레 그림 카드를 들고 선 경비예요.", "Antivirus is a guard at every room holding a deck of bug cards."),
         "small": ("들어오는 상자를 카드 한 장 한 장과 비교해요. 카드와 똑같은 벌레가 있으면 문 앞에서 막고 상자에 가둬요.",
                   "The guard compares every incoming box against the cards, one by one. If a bug matches a card, it\'s stopped at the door and put in a jar."),
         "tricks": (4, [
             (CARD_I, ("카드와 비교", "Compare to the cards"), ("아는 벌레는 생김새로 잡아요", "known bugs are caught by their looks"), "calm"),
             (NEW_I, ("매일 새 카드", "New cards every day"), ("벌레 소식이 오면 카드를 더 그려요", "new bug news means new cards"), "calm"),
             (STOP_I, ("문 앞에서", "At the door"), ("방에 들어오기 전에 막아요", "stopped before it gets in"), "warm"),
             (JAR_I, ("병에 가두기", "Into the jar"), ("잡은 벌레는 못 나오게 가둬요", "a caught bug goes in a jar it can\'t leave")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 보라색 새 벌레가 카드를 든 경비 앞을 물음표와 함께 그냥 지나감. 오른쪽: 같은 벌레가 상자 두 개를 잠그기 시작하자 경비가 손을 뻗어 붙잡음", "Left: a purple new bug walks right past the guard with the cards, question mark above. Right: the same bug starts locking two chests and the guard reaches out and grabs it"),
         "caption": ("카드에 없는 새 벌레는 그냥 지나가요. 그래서 요즘 경비는 하는 짓도 봐요.", "A bug on no card walks right past. So today\'s guards also watch what it does."),
         "small": ('여기가 비유가 깨지는 곳이에요. <a href="zeroday-ko.html">아무도 모르는 새 벌레</a>는 카드가 없어요. 대신 상자를 마구 잠그거나 편지를 몰래 베끼면, 카드 없이도 벌레라고 알아채요.',
                   'This is where the picture cracks. A <a href="zeroday-en.html">brand-new bug nobody knows</a> has no card. But if something starts locking chests or secretly copying letters, the guard calls it a bug — card or no card.')},
        {"svg": P5, "alt": ("왼쪽: 문 앞의 카드 경비가 벌레 든 상자에 빨간 X를 침. 오른쪽: 방 안에서 경비견이 짖으며 보라색 벌레를 쫓음", "Left: the card guard at the door puts a red X on a bug-filled box. Right: inside the room, a guard dog barks and chases the purple bug"),
         "caption": ("카드 경비는 문 앞에서 막고, 경비견은 들어온 뒤에 쫓아요.", "The card guard stops it at the door; the guard dog chases it once inside."),
         "small": ('<a href="edr-ko.html">경비견</a>은 방 안에서 일어나는 일을 전부 보고 적어 둬요. 카드 경비가 놓친 벌레를 경비견이 잡아요. 둘 다 있어야 해요.',
                   'The <a href="edr-en.html">guard dog</a> watches and writes down everything that happens inside the room. What the card guard misses, the dog catches. You need both.')},
    ],
    "summary": (("<b>안티바이러스</b> = 방마다 <b>벌레 그림 카드</b>를 들고 서서, 들어오는 상자를 카드와 비교해 <b>아는 벌레를 문 앞에서 막는</b> 경비. 요즘은 <b>하는 짓</b>도 봐요.",
                 "<b>Antivirus</b> = a guard at every room holding <b>bug cards</b>, comparing each incoming box and <b>stopping known bugs at the door</b>. Today\'s guards also watch <b>what a bug does</b>."),
                ("Antivirus / EPP(Endpoint Protection Platform). 시그니처(알려진 악성코드의 지문)로 파일을 검사하고, 휴리스틱·행동 기반 탐지로 새 변종을 잡고, 잡은 파일은 격리해요. 들어온 뒤의 추적·대응은 EDR의 몫이에요.",
                 "Antivirus / EPP (Endpoint Protection Platform) scans files against signatures (fingerprints of known malware), catches new variants with heuristic and behavior-based detection, and quarantines what it finds. Tracking and responding after something gets in is EDR\'s job.")),
    "glossary": [
        ("벌레 그림 카드", "Signature", ("아는 벌레의 생김새.", "What a known bug looks like."), ('벌레마다 카드 한 장. 카드와 똑같으면 잡아요. 카드는 <a href="hashing-ko.html">지문</a>이나 특징 조각으로 만들어요.', 'One card per bug; a match means a catch. Cards are made from a <a href="hashing-en.html">fingerprint</a> or a telltale piece of the bug.')),
        ("생김새 짐작", "Heuristic", ("카드와 비슷하면 의심.", "Close enough to a card is suspicious."), ("다리 여섯에 빨간 등이면 카드에 없어도 벌레 같아요. 새 변종을 잡는 법이에요.", "Six legs and a red back looks like a bug even without a card. How guards catch new variants.")),
        ("하는 짓 보기", "Behavior-based detection", ("얼굴 말고 행동.", "What it does, not what it looks like."), ("상자를 마구 잠그고, 편지를 몰래 베끼고, 밤에 마을로 나가면 벌레예요.", "Locking chests, secretly copying letters, sneaking out to the village at night — that\'s a bug.")),
        ("문 앞 경비 세트", "EPP", ("카드 경비의 요즘 이름.", "The card guard\'s modern name."), ("카드, 짐작, 행동 보기, 방화벽까지 한 경비가 다 들고 있어요.", "Cards, heuristics, behavior watching, even a small firewall — all carried by one guard.")),
        ("병에 가두기", "Quarantine", ("잡은 벌레는 못 나오게.", "A caught bug can\'t get out."), ("버리진 않고 병에 넣어 둬요. 잘못 잡았으면 다시 꺼내 줄 수 있게요.", "Not destroyed, just jarred — so it can be let out if the guard was wrong.")),
        ("새 카드 받기", "Definition update", ("매일 카드가 늘어요.", "More cards every day."), ('<a href="cti-ko.html">망루 친구</a>가 새 벌레 소식을 보내면 카드를 더 그려요. 카드가 오래되면 경비는 눈이 어두워져요.', 'When the <a href="cti-en.html">watchtower friend</a> reports a new bug, new cards are drawn. Old cards make a blind guard.')),
        ("경비견과의 차이", "EDR vs. antivirus", ("문 앞 vs. 들어온 뒤.", "At the door vs. once inside."), ('카드 경비는 막고, <a href="edr-ko.html">경비견</a>은 지켜보고 쫓아요. 요즘은 둘을 한 세트로 둬요.', 'The card guard blocks; the <a href="edr-en.html">guard dog</a> watches and chases. These days they come as one set.')),
        ("잘못 잡기", "False positive", ("장난감 벌레를 잡았어요.", "Caught a toy bug."), ("생김새가 비슷한 착한 도구를 병에 넣기도 해요. 그래서 병에서 꺼내 주는 길이 있어야 해요.", "Sometimes a harmless tool that looks like a bug gets jarred. That\'s why there must be a way to let it out.")),
    ],
}
