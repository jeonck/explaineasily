from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
HELD_MASK = '<rect x="50" y="40" width="30" height="12" rx="3" fill="#111C30"/><rect x="63" y="52" width="4" height="26" fill="#8B5E3C"/>'   # 손에 든 도둑 가면
PAPER, PAPER_EDGE, INK = "#FFF8E7", "#C9A86A", "#142033"


def sheet(x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="3"/><rect x="{x}" y="{y}" width="{w}" height="26" rx="6" fill="{PAPER_EDGE}"/>'
            + label(x + w / 2, y + 18, title, 12, INK, cls="d"))


def box(x, y, w, h, text, stroke=INK):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="{stroke}" stroke-width="2.5"/>' + label(x + w / 2, y + h / 2 + 4, text, 11, INK)


def arrow(x1, y1, x2, y2, color=INK, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="2.5"{d}/>'
            f'<circle cx="{x2}" cy="{y2}" r="4" fill="{color}"/>')


def tower(x, y, w=100, h=150):
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" fill="var(--stone-dark)"/>{battlements(0, -20, w, 3, "var(--stone-dark)", 22)}'
            f'<rect x="{w / 2 - 16:.0f}" y="{h - 44}" width="32" height="44" rx="16" fill="var(--night)"/></g>')


# 1. 새 탑 도면 — 왕은 빨리 짓자, 경비는 잠깐
P1 = svg(300, sky(300)
         + sheet(230, 40, 300, 190, "⟦새 창고 탑 도면|NEW STOREHOUSE TOWER⟧")
         + box(260, 90, 90, 40, "⟦정문|front door⟧") + box(440, 90, 70, 40, "⟦금고|vault⟧") + box(330, 160, 100, 40, "⟦배달 창구|delivery hatch⟧")
         + arrow(350, 110, 440, 110) + arrow(430, 175, 475, 132)
         + person(80, 110, s=0.85, face=SMILE, **KING) + bubble(20, 30, 200, 34, "⟦좋아! 내일부터 짓자|great! start building tomorrow⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 120, s=0.85, face=EYES, **GUARD) + bubble(540, 30, 210, 34, "⟦잠깐요. 한 번만 더 볼게요|wait. one more look⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + label(380, 280, "⟦목수가 새 탑 도면을 가져왔어요|the builder brought the drawing for a new tower⟧", 12, "var(--muted)"))

# 2. 지은 뒤에 '거기도 문이었네' 하면 늦어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + tower(300, 80, 160, 160)
         + person(150, 130, s=0.85, face=SMILE, **GUARD) + label(185, 262, "⟦정문만 지켜요|guarding the front door⟧", 12, "var(--ink)")
         + '<rect x="440" y="190" width="40" height="30" rx="3" fill="#8B5E3C"/><rect x="446" y="196" width="28" height="18" fill="var(--night)"/>'
         + person(520, 140, s=0.8, **THIEF) + '<path d="M520 190 l-38 18" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(560, 262, "⟦배달 창구로 쓱|slipping in through the hatch⟧", 12, "var(--bad)")
         + bubble(40, 30, 240, 46, "⟦거긴 문이 아니라 창구인데…|but that is a hatch, not a door…⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 288, "⟦다 짓고 나서 '아, 거기도 문이었네' 하면 늦어요|realizing after it is built that the hatch was a door too — that is too late⟧", 11, "var(--muted)"))

# 3. 위협 모델링 = 짓기 전에 도둑 눈으로 보는 도면 (hero)
P3 = svg(360, sky(360)
         + sheet(230, 30, 380, 240, "⟦도면 — 도둑 눈으로|THE DRAWING — THROUGH A THIEF\'S EYES⟧")
         + f'<rect x="255" y="75" width="330" height="170" rx="10" fill="none" stroke="var(--good)" stroke-width="2.5" stroke-dasharray="8 6"/>' + label(270, 92, "⟦믿는 안쪽|the trusted inside⟧", 10, "var(--good)", "start")
         + box(285, 110, 90, 40, "⟦정문|front door⟧") + box(480, 110, 70, 40, "⟦금고|vault⟧") + box(375, 185, 100, 40, "⟦배달 창구|delivery hatch⟧")
         + arrow(375, 130, 480, 130) + arrow(475, 200, 515, 152)
         + '<circle cx="255" cy="130" r="12" fill="var(--bad)"/><circle cx="375" cy="245" r="12" fill="var(--bad)"/>'
         + label(255, 134, "1", 12, "#FFF") + label(375, 249, "2", 12, "#FFF")
         + label(600, 262, "⟦● 도둑이 들어올 수 있는 곳|● where a thief could get in⟧", 10, "var(--bad)", "end")
         + person(80, 120, s=0.9, face=EYES, extra=HELD_MASK, **GUARD)
         + label(115, 250, "⟦경비가 도둑 가면을 써 봐요|the guard tries on a thief\'s mask⟧", 12, "var(--ink)")
         + person(660, 150, s=0.75, face=SMILE, **BUILDER)
         + label(380, 305, "⟦뭘 짓지? 도둑이면 어디로? 뭐가 잘못될까? 어떻게 막지?|what are we building? where would a thief go? what can go wrong? how do we stop it?⟧", 12, "var(--ink)", cls="d")
         + label(380, 338, "⟦벽돌 하나 놓기 전에, 도면 위에서 먼저 도둑질을 해 봐요|before a single brick, rob the tower on paper first⟧", 12, "var(--muted)"))

# 4. 여섯 도둑 버릇 — 뭐가 잘못될 수 있나
HABITS = (
    ("⟦변장|disguise⟧", "⟦목수인 척 들어와요|walks in as the builder⟧", f'<circle cx="0" cy="-6" r="14" fill="{SKIN}"/><path d="M-15 -10 Q0 -30 15 -10z" fill="#E9B44C"/><rect x="-10" y="-9" width="20" height="6" fill="#111C30"/>'),
    ("⟦바꿔치기|tampering⟧", "⟦장부 숫자를 고쳐요|changes the numbers in the book⟧", f'<rect x="-16" y="-20" width="32" height="36" rx="3" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="2"/><path d="M-8 -8 h16 M-8 2 h10" stroke="{PAPER_EDGE}" stroke-width="2"/><path d="M4 8 l12 -12" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'),
    ("⟦발뺌|denial⟧", "⟦'난 안 그랬어요'|it was not me⟧", f'<circle cx="0" cy="-6" r="14" fill="{SKIN}"/><path d="M-15 -10 Q0 -30 15 -10z" fill="var(--bad)"/><path d="M-22 12 l44 -30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'),
    ("⟦엿보기|peeking⟧", "⟦금고 안을 훔쳐봐요|peeks inside the vault⟧", '<ellipse cx="0" cy="-4" rx="20" ry="12" fill="#FFF" stroke="var(--night)" stroke-width="3"/><circle cx="0" cy="-4" r="6" fill="var(--night)"/>'),
    ("⟦문 막기|blocking⟧", "⟦정문을 수레로 막아요|blocks the door with a cart⟧", '<rect x="-20" y="-14" width="40" height="22" rx="3" fill="#5A3B22"/><circle cx="-12" cy="12" r="6" fill="var(--night)"/><circle cx="12" cy="12" r="6" fill="var(--night)"/><path d="M-6 -8 l12 12 M6 -8 l-12 12" stroke="var(--bad)" stroke-width="3"/>'),
    ("⟦열쇠 늘리기|more keys⟧", "⟦창고 열쇠로 금고까지|storeroom key opens the vault⟧", '<circle cx="-8" cy="-4" r="8" fill="none" stroke="#E9B44C" stroke-width="5"/><rect x="0" y="-6" width="26" height="5" fill="#E9B44C"/><rect x="18" y="-1" width="4" height="7" fill="#E9B44C"/><path d="M8 8 l8 8 M16 8 l-8 8" stroke="var(--bad)" stroke-width="3"/>'),
)
CARDS = "".join(
    f'<g transform="translate({30 + (i % 3) * 240},{60 + (i // 3) * 120})"><rect width="220" height="100" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
    f'<g transform="translate(32,50)">{pic}</g>' + label(138, 42, name, 13, "var(--bad)", cls="d") + label(138, 66, what, 10, "var(--muted)") + "</g>"
    for i, (name, what, pic) in enumerate(HABITS))
P4 = svg(340, '<rect width="760" height="340" fill="var(--accent-soft)"/>'
         + label(380, 38, "⟦도둑의 여섯 가지 버릇을 하나씩 물어봐요|ask about each of the six thief habits, one by one⟧", 14, "var(--ink)", cls="d")
         + CARDS
         + label(380, 320, "⟦문마다 여섯 번 물어요 — '여기서 도둑이 이 버릇을 부리면?'|six questions at every door — what if a thief tried this habit right here?⟧", 11, "var(--muted)"))

# 5. 막는 법을 도면에 미리 그려 넣어요
P5 = svg(320, sky(320)
         + sheet(40, 30, 420, 230, "⟦고친 도면|THE FIXED DRAWING⟧")
         + box(70, 90, 90, 40, "⟦정문|front door⟧") + box(330, 90, 70, 40, "⟦금고|vault⟧") + box(200, 170, 110, 40, "⟦배달 창구|delivery hatch⟧", "var(--good)")
         + arrow(160, 110, 330, 110) + arrow(310, 185, 365, 132)
         + '<circle cx="200" cy="190" r="13" fill="var(--good)"/><path d="M194 190 l4 4 l8 -8" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
         + label(245, 232, "⟦창구에도 문지기 + 일지|a gatekeeper and a log at the hatch too⟧", 10, "var(--good)")
         + '<circle cx="365" cy="90" r="13" fill="var(--good)"/><path d="M359 90 l4 4 l8 -8" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
         + label(365, 72, "⟦금고 열쇠는 따로|a separate vault key⟧", 10, "var(--good)")
         + person(520, 110, s=0.85, face=SMILE, **BUILDER) + person(630, 120, s=0.8, face=SMILE, **GUARD)
         + label(600, 245, "⟦이제 지어요|now we build⟧", 13, "var(--ink)", cls="d")
         + label(380, 295, "⟦짓기 전에 그리면 벽돌 한 장 값, 지은 뒤에 고치면 탑 하나 값|fixed on paper it costs a brick — fixed after building, a whole tower⟧", 12, "var(--muted)"))

DRAW_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="18" y="20" width="12" height="10" rx="2" fill="none" stroke="#142033" stroke-width="2"/><rect x="36" y="34" width="12" height="10" rx="2" fill="none" stroke="#142033" stroke-width="2"/><path d="M30 25 h6 v14" stroke="#142033" stroke-width="2" fill="none"/>')
DOOR_I = icon('<rect x="18" y="12" width="28" height="44" rx="3" fill="#8B5E3C"/><circle cx="40" cy="36" r="3" fill="#E9B44C"/><circle cx="14" cy="34" r="8" fill="var(--bad)"/><path d="M11 34 h6 M14 31 l3 3 l-3 3" stroke="#FFF" stroke-width="2" fill="none" stroke-linecap="round"/>')
MASK_I = icon(f'<circle cx="32" cy="30" r="16" fill="{SKIN}"/><path d="M14 26 Q32 4 50 26z" fill="var(--bad)"/><rect x="20" y="26" width="24" height="8" fill="#111C30"/><text x="32" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">?</text>')
FIX_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="26" y="30" width="12" height="10" rx="2" fill="none" stroke="#142033" stroke-width="2"/><circle cx="26" cy="30" r="8" fill="var(--good)"/><path d="M22 30 l3 3 l6 -6" stroke="#FFF" stroke-width="2" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "threatmodel", "order": 78,
    "title": ("짓기 전에 도둑 눈으로 보는 도면", "The Drawing Seen Through a Thief's Eyes"),
    "h1": ("<em>위협 모델링</em>이 뭐예요?", "What is <em>Threat Modeling</em>?"),
    "sub": ("위협 모델링(Threat Modeling)을 벽돌을 놓기 전에 경비가 도둑 가면을 쓰고 도면을 살펴보는 이야기로 풀어봤어요.",
            "Threat modeling, told as a story about a guard who puts on a thief's mask and studies the drawing before a single brick is laid."),
    "panels": [
        {"svg": P1, "alt": ("정문, 금고, 배달 창구가 그려진 새 창고 탑 도면. 왕은 '내일부터 짓자', 경비는 '잠깐요, 한 번만 더 볼게요'", "A drawing of a new storehouse tower with a front door, a vault, and a delivery hatch. The king says start tomorrow; the guard says wait, one more look"),
         "caption": ("목수가 새 탑 도면을 가져왔어요.", "The builder brought the drawing for a new tower."),
         "small": ("정문 하나, 금고 하나, 배달 창구 하나. 왕은 당장 짓고 싶어요. 경비는 한 번만 더 보자고 해요.",
                   "One front door, one vault, one delivery hatch. The king wants to build right away. The guard asks for one more look.")},
        {"svg": P2, "alt": ("완성된 탑. 경비는 정문 앞에 서 있고, 도둑이 옆의 작은 배달 창구로 기어들어감", "A finished tower. The guard stands at the front door while a thief crawls in through a small delivery hatch on the side"),
         "caption": ("다 짓고 나서 '거기도 문이었네' 하면 늦어요.", "Realizing after it is built that the hatch was a door too — that is too late."),
         "small": ('경비는 정문만 지켰어요. 도둑은 배달 창구로 왔어요. 지은 뒤에 고치려면 <a href="devsecops-ko.html">벽을 다시 부숴야</a> 해요.',
                   'The guard watched the front door. The thief came through the hatch. Fixing it now means <a href="devsecops-en.html">tearing the wall down again</a>.')},
        {"svg": P3, "hero": True, "alt": ("경비가 도둑 가면을 손에 들고 도면을 봄. 도면엔 '믿는 안쪽' 점선 상자, 정문과 배달 창구에 빨간 1·2 표시. 목수가 옆에서 지켜봄", "The guard holds a thief's mask and studies the drawing: a dashed box marks the trusted inside, and red 1 and 2 marks sit on the front door and the hatch. The builder watches"),
         "caption": ("위협 모델링은 짓기 전에 도둑 눈으로 보는 도면이에요.", "Threat modeling is looking at the drawing through a thief's eyes before building."),
         "small": ("경비가 도둑 가면을 써 봐요. 뭘 짓는지 그리고, 도둑이면 어디로 올지 찾고, 뭐가 잘못될지 묻고, 막는 법을 도면에 적어요.",
                   "The guard tries on the thief's mask. Draw what is being built, find where a thief would enter, ask what could go wrong, and write the fix onto the drawing."),
         "tricks": (4, [
             (DRAW_I, ("뭘 짓지?", "What are we building?"), ("방과 길을 그려요", "draw the rooms and the paths")),
             (DOOR_I, ("도둑이면 어디로?", "Where would a thief go?"), ("들어올 수 있는 곳마다 표시", "mark every way in"), "warm"),
             (MASK_I, ("뭐가 잘못될까?", "What can go wrong?"), ("여섯 버릇을 하나씩", "six habits, one by one"), "warm"),
             (FIX_I, ("어떻게 막지?", "How do we stop it?"), ("도면에 미리 그려 넣어요", "draw the fix in first"), "calm"),
         ])},
        {"svg": P4, "alt": ("여섯 장의 카드: 변장, 바꿔치기, 발뺌, 엿보기, 문 막기, 열쇠 늘리기. 각각 작은 그림과 한 줄 설명", "Six cards: disguise, tampering, denial, peeking, blocking, more keys — each with a small picture and a one-line example"),
         "caption": ("도둑의 여섯 가지 버릇을 하나씩 물어봐요.", "Ask about each of the six thief habits, one by one."),
         "small": ('문마다 여섯 번 물어요. "여기서 도둑이 변장하면? 바꿔치기하면? 발뺌하면? 엿보면? 막으면? 열쇠를 늘리면?" 빠뜨리는 버릇이 없게요.',
                   'Six questions at every door. "What if a thief disguised himself here? Tampered? Denied it? Peeked? Blocked it? Got more keys?" So no habit is forgotten.')},
        {"svg": P5, "alt": ("고친 도면: 배달 창구에 초록 체크와 '문지기 + 일지', 금고에 '열쇠는 따로'. 목수와 경비가 웃으며 '이제 지어요'", "The fixed drawing: a green check and a gatekeeper plus a log at the hatch, a separate key for the vault. The builder and the guard smile: now we build"),
         "caption": ("막는 법을 도면에 미리 그려 넣어요.", "The fixes go onto the drawing before building."),
         "small": ('창구에도 문지기와 <a href="log-ko.html">일지</a>를 두고, 금고 <a href="rbac-ko.html">열쇠는 따로</a> 만들어요. 그다음엔 <a href="codescan-ko.html">벽돌마다 검사</a>하고, 다 지으면 <a href="pentest-ko.html">고용한 도둑</a>이 진짜로 시험해요.',
                   'A gatekeeper and a <a href="log-en.html">log</a> at the hatch, a <a href="rbac-en.html">separate key</a> for the vault. Then <a href="codescan-en.html">check every brick</a>, and once built, a <a href="pentest-en.html">hired thief</a> tests it for real.')},
    ],
    "summary": (("<b>위협 모델링</b> = 벽돌을 놓기 전에 <b>도둑 눈으로 도면</b>을 보며, 어디로 들어올지·뭐가 잘못될지 찾고 <b>막는 법을 도면에 미리 그려 넣는</b> 일.",
                 "<b>Threat modeling</b> = before laying a brick, <b>look at the drawing through a thief's eyes</b>, find the ways in and what could go wrong, and <b>draw the fixes in first</b>."),
                ("Threat Modeling. 시스템의 자산과 데이터 흐름을 그리고, 신뢰 경계와 진입점을 표시한 뒤, STRIDE 같은 틀로 위협을 열거하고 완화 통제를 설계에 반영해요. 설계 단계에서 가장 싸게 보안을 넣는 방법이에요.",
                 "Threat Modeling. Diagram the system's assets and data flows, mark trust boundaries and entry points, enumerate threats with a framework like STRIDE, and fold mitigations into the design. It is the cheapest point to build security in.")),
    "glossary": [
        ("위협 모델링", "Threat modeling", ("도둑 눈으로 보는 도면.", "The drawing through a thief's eyes."), ("짓기 전에 종이 위에서 먼저 도둑질을 해 봐요. 네 가지 질문: 뭘 짓지, 어디로 올까, 뭐가 잘못될까, 어떻게 막지.", "Rob the tower on paper before building it. Four questions: what are we building, where would a thief go, what can go wrong, how do we stop it.")),
        ("데이터 흐름도", "Data flow diagram", ("방과 길 그림.", "The rooms-and-paths picture."), ("금고, 창구, 그 사이를 오가는 화살표. 이 그림이 없으면 어디를 지킬지도 몰라요.", "The vault, the hatch, and the arrows between them. Without this picture you do not even know what to guard.")),
        ("신뢰 경계", "Trust boundary", ("믿는 안쪽의 점선.", "The dashed line around the trusted inside."), ("선 안은 우리 사람, 선 밖은 모르는 사람. 선을 넘는 화살표마다 물어봐요.", "Inside the line are our people; outside are strangers. Every arrow that crosses the line gets a question.")),
        ("진입점", "Entry point", ("도둑이 들어올 수 있는 곳.", "Where a thief could get in."), ('정문만이 아니라 창구, 창문, 굴뚝까지. → <a href="asm-ko.html">바깥에서 세는 우리 성의 문</a>', 'Not just the front door — the hatch, the windows, the chimney. → <a href="asm-en.html">counting our doors from outside</a>')),
        ("STRIDE", "STRIDE", ("여섯 도둑 버릇.", "The six thief habits."), ("변장(Spoofing), 바꿔치기(Tampering), 발뺌(Repudiation), 엿보기(Information disclosure), 문 막기(Denial of service), 열쇠 늘리기(Elevation of privilege). 첫 글자를 모으면 STRIDE.", "Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. The first letters spell STRIDE.")),
        ("공격 트리", "Attack tree", ("도둑의 계획표.", "The thief's plan, drawn as a tree."), ("'금고를 열려면' 아래에 '열쇠를 훔친다', '창구로 들어간다'… 가지처럼 그려요. 가장 쉬운 가지부터 막아요.", "Under 'open the vault' hang branches: steal the key, use the hatch… Block the easiest branch first.")),
        ("완화 통제", "Mitigation", ("도면에 그려 넣은 막는 법.", "The fix drawn into the plan."), ('창구의 문지기, 따로 만든 금고 열쇠, 일지. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'The gatekeeper at the hatch, the separate vault key, the log. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
        ("데브섹옵스", "DevSecOps", ("이 도면을 보는 자리.", "Where this drawing gets looked at."), ('경비가 처음부터 목수 옆에 앉는 방식. 도면 보기가 첫 번째 일이에요. → <a href="devsecops-ko.html">짓는 동안 같이 보는 목수와 경비</a>', 'The way the guard sits beside the builder from the start. Reading the drawing is the first job. → <a href="devsecops-en.html">the builder and the guard, side by side</a>')),
    ],
}
