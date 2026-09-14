from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
OWNER = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
CLIP = '<g transform="translate(52,64)"><rect width="26" height="34" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M5 10 l3 3 l6 -6 M5 20 l3 3 l6 -6" stroke="var(--good)" stroke-width="2" fill="none"/><path d="M5 30 l8 0" stroke="var(--bad)" stroke-width="2"/></g>'


def shed(x, y, s=1.0, name="", door="closed", mark=""):
    if door == "open":
        d = '<rect x="-10" y="26" width="20" height="34" fill="var(--night)"/><rect x="-10" y="26" width="20" height="34" fill="#8B5E3C" transform="skewY(-25) translate(-22,0)"/>'
    else:
        d = '<rect x="-10" y="26" width="20" height="34" fill="#8B5E3C"/><circle cx="6" cy="44" r="2" fill="#E9B44C"/>'
    nm = label(0, 80, name, 11, "var(--muted)") if name else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--stone-dark)"/>'
            f'<path d="M-48 0 L0 -34 L48 0 Z" fill="var(--stone)"/>{d}{nm}{mark}</g>')


def box(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-14" width="40" height="28" rx="2" fill="#C9A86A"/>'
            f'<path d="M-20 -4 h40 M0 -14 v10" stroke="#8B5E3C" stroke-width="3"/></g>')


def keyring(x, y, n, s=1.0):
    keys = "".join(f'<g transform="rotate({-60 + i * (120 / max(n - 1, 1))})"><rect x="-2" y="10" width="4" height="18" fill="#E9B44C"/><rect x="-2" y="22" width="7" height="3" fill="#E9B44C"/></g>' for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="9" fill="none" stroke="#E9B44C" stroke-width="4"/>{keys}</g>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def mark(ok):
    return ('<circle cx="0" cy="-54" r="12" fill="var(--good)"/><path d="M-6 -54 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>' if ok
            else '<circle cx="0" cy="-54" r="12" fill="var(--bad)"/><path d="M-5 -59 l10 10 M5 -59 l-10 10" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>')


ROAD = '<path d="M0 252 H760" stroke="var(--stone)" stroke-width="16"/>'

# 1. 마을에 빌린 창고가 수백 개
P1 = svg(300, sky(300)
         + small_castle(50, 100, 0.6) + person(170, 130, s=0.7, face=EYES, **GUARD) + label(130, 240, "⟦우리 성|our castle⟧", 12, "var(--ink)")
         + "".join(shed(300 + i * 80, y, 0.55) for y in (80, 170) for i in range(6))
         + label(500, 240, "⟦마을에 빌린 창고 — 수백 개|rented sheds in the village — hundreds⟧", 12, "var(--ink)")
         + label(380, 290, "⟦요즘은 상자를 성 밖 빌린 창고에 둬요|these days the boxes live in rented sheds outside the castle⟧", 12, "var(--muted)"))

# 2. 벽은 주인, 문은 우리 — 문이 열려 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(70, 90, s=0.8, face=SMILE, **OWNER) + bubble(20, 30, 220, 34, "⟦벽이랑 지붕은 제가 봐요|I look after the walls and roof⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(120, 225, "⟦문단속은 우리 몫이에요|locking up is our job⟧", 11, "var(--ink)")
         + shed(380, 95, 1.1, door="open") + keyring(402, 140, 3, 0.7) + box(340, 190, 0.8)
         + label(380, 225, "⟦문은 열려 있고 열쇠는 문에|door open, keys left in⟧", 11, "var(--bad)")
         + person(600, 90, s=0.8, face=MASK, extra=BAG) + label(640, 225, "⟦길 가던 도둑이 그냥 들어가요|a passing thief just walks in⟧", 11, "var(--bad)")
         + label(380, 280, "⟦빌린 창고에선 벽보다 안 잠근 문이 더 흔한 사고예요|in rented sheds, an unlocked door is a far more common accident than a broken wall⟧", 11, "var(--ink)", cls="d"))

# 3. 매일 창고마다 문단속 점검 (hero)
P3 = svg(360, sky(360) + ROAD
         + person(40, 120, s=0.8, face=SMILE, extra=CLIP, **BLUE) + bell(60, 50, 0.6) + label(60, 100, "⟦바로 종|ring at once⟧", 10, "var(--muted)")
         + shed(170, 110, 1.0, "⟦잘 잠김|locked⟧", mark=mark(True))
         + shed(340, 110, 1.0, "⟦문 열림|door open⟧", door="open", mark=mark(False))
         + shed(510, 110, 1.0, "⟦열쇠가 열 개|ten keys⟧", mark=mark(False) + keyring(0, 30, 5, 0.9))
         + box(660, 232, 1.0) + label(660, 205, "⟦상자가 길가에|a box on the road⟧", 11, "var(--muted)") + '<circle cx="660" cy="170" r="12" fill="var(--bad)"/><path d="M655 165 l10 10 M665 165 l-10 10" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>'
         + label(380, 300, "⟦매일 아침, 창고마다 문단속 표를 돌아요|every morning, the checklist goes round every shed⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦잘못 잠긴 문은 그 자리에서 종을 울려요|a badly locked door rings the bell on the spot⟧", 12, "var(--muted)"))

# 4. 문단속 표 — 그리고 자동으로 닫기
CHECKS = ((True, "⟦문이 잠겨 있나 (길에서 보이나)|is the door locked (visible from the road?)⟧"), (False, "⟦열쇠가 너무 많지 않나|are there too many keys?⟧"),
          (True, "⟦상자는 봉인 편지로 두었나|are the boxes kept sealed?⟧"), (True, "⟦일지가 켜져 있나|is the log switched on?⟧"), (False, "⟦마을 규칙 표에 맞나|does it match the village rulebook?⟧"))
P4 = svg(320, sky(320)
         + '<rect x="40" y="30" width="420" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="420" height="28" rx="8" fill="#C9A86A"/>' + label(250, 49, "⟦창고 문단속 표|SHED CHECKLIST⟧", 12, "#142033", cls="d")
         + "".join((f'<circle cx="66" cy="{82 + i * 36}" r="10" fill="{"var(--good)" if ok else "var(--bad)"}"/>'
                    + (f'<path d="M61 {82 + i * 36} l3 3 l7 -7" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>' if ok else f'<path d="M62 {78 + i * 36} l8 8 M70 {78 + i * 36} l-8 8" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>')
                    + label(86, 86 + i * 36, t, 11, "#142033", "start")) for i, (ok, t) in enumerate(CHECKS))
         + shed(600, 90, 1.0, door="open") + '<path d="M660 60 Q700 90 640 120" stroke="var(--good)" stroke-width="4" fill="none" stroke-dasharray="7 5"/><path d="M646 108 l-8 14 l14 -2z" fill="var(--good)"/>'
         + label(600, 195, "⟦열린 문은 기계가 바로 닫기도 해요|an open door can be shut by the machine⟧", 11, "var(--ink)")
         + label(600, 215, "⟦(자동 수정)|(auto-fix)⟧", 10, "var(--muted)")
         + label(380, 295, "⟦표는 매일 똑같이, 사람이 아니라 기계가 돌아요|the same list every day — walked by a machine, not a person⟧", 12, "var(--ink)", cls="d"))

# 5. 창고 문지기와 문단속 점검 — 둘 다
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + '<path d="M20 200 H360" stroke="var(--stone)" stroke-width="12"/>' + gatehouse(150, 90, 0.8) + person(230, 115, s=0.7, face=SMILE, hat=None, shirt="#4A5A72") + box(292, 175, 0.7)
         + label(190, 240, "⟦창고 문지기 — 드나드는 사람을 봐요|the shed gatekeeper watches who comes and goes⟧", 11, "var(--ink)")
         + shed(520, 80, 1.0, mark=mark(True)) + person(620, 110, s=0.75, face=SMILE, extra=CLIP, **BLUE)
         + label(570, 240, "⟦문단속 점검 — 창고 자체를 봐요|the lock-up check looks at the shed itself⟧", 11, "var(--ink)")
         + label(380, 288, "⟦둘 다 있어야 빌린 창고가 안전해요|it takes both to keep a rented shed safe⟧", 12, "var(--ink)", cls="d"))

SHARE_I = icon('<path d="M8 30 L32 12 L56 30 Z" fill="var(--stone)"/><rect x="14" y="30" width="36" height="24" fill="var(--stone-dark)"/><rect x="26" y="38" width="12" height="16" fill="#8B5E3C"/><circle cx="35" cy="47" r="2" fill="#E9B44C"/><path d="M8 30 L56 30" stroke="var(--good)" stroke-width="3"/>')
DAILY_I = icon('<rect x="10" y="12" width="44" height="42" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="12" width="44" height="10" fill="#C9A86A"/><path d="M18 34 l4 4 l8 -8 M18 46 l4 4 l8 -8" stroke="var(--good)" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="44" cy="40" r="7" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/>')
OPEN_I = icon('<rect x="12" y="16" width="40" height="38" fill="var(--stone-dark)"/><rect x="26" y="30" width="12" height="24" fill="var(--night)"/><rect x="26" y="30" width="12" height="24" fill="#8B5E3C" transform="skewY(-30) translate(-12,0)"/><circle cx="50" cy="14" r="8" fill="var(--bad)"/><path d="M46 10 l8 8 M54 10 l-8 8" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>')
BELL_I = icon('<path d="M20 36 c0 -20 24 -20 24 0 v10 h-24z" fill="#E9B44C"/><rect x="16" y="46" width="32" height="5" rx="2" fill="#C9822B"/><circle cx="32" cy="55" r="3" fill="#C9822B"/><path d="M12 30 a22 22 0 0 1 -6 -16 M52 30 a22 22 0 0 0 6 -16" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "cspm", "order": 84,
    "title": ("빌린 창고 문단속 점검", "The Rented-Shed Lock-Up Check"),
    "h1": ("<em>클라우드 보안</em>이 뭐예요?", "What is <em>Cloud Security</em>?"),
    "sub": ("클라우드 보안, 그중에서도 CSPM(Cloud Security Posture Management)을 마을에 빌린 창고 수백 개의 문단속을 매일 점검하는 이야기로 풀어봤어요.",
            "Cloud security — CSPM (Cloud Security Posture Management) in particular — told as a story about checking the locks on hundreds of rented sheds in the village, every day."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽에 작은 우리 성과 경비, 오른쪽에 똑같이 생긴 빌린 창고 열두 채가 줄지어 있음", "A small castle and a guard on the left; on the right, twelve identical rented sheds in rows"),
         "caption": ("요즘은 상자를 성 밖 빌린 창고에 둬요. 창고가 수백 개예요.", "These days the boxes live in rented sheds outside the castle. Hundreds of them."),
         "small": ('<a href="casb-ko.html">빌린 창고</a>는 마을 곳곳에 있어요. 성벽 안이 아니에요.', 'The <a href="casb-en.html">rented sheds</a> are all over the village. Not inside the castle wall.')},
        {"svg": P2, "alt": ("창고 주인이 '벽이랑 지붕은 제가 봐요' 하고, 가운데 창고는 문이 열린 채 열쇠가 꽂혀 있고 상자가 밖에 나와 있으며, 도둑이 그냥 걸어 들어감", "The shed owner says he looks after the walls and roof; the middle shed stands open with keys left in and a box outside; a thief simply walks in"),
         "caption": ("창고 주인은 벽과 지붕만 봐요. 문단속은 우리 몫이에요.", "The shed owner looks after the walls and roof. Locking up is our job."),
         "small": ("그런데 창고가 수백 개라 누가 문을 열어 뒀는지 아무도 몰라요. 빌린 창고에선 벽이 뚫리는 것보다 안 잠근 문이 훨씬 흔한 사고예요.", "But with hundreds of sheds, nobody knows who left a door open. In rented sheds, an unlocked door is a far more common accident than a broken wall.")},
        {"svg": P3, "hero": True, "alt": ("길가에 창고 셋 — 잘 잠김(초록 체크), 문 열림(빨간 엑스), 열쇠가 열 개(빨간 엑스) — 그리고 길가에 놓인 상자. 파란 모자 점검원이 표를 들고 있고 옆에 종", "Three sheds along the road — locked (green check), door open (red X), ten keys (red X) — and a box sitting on the road. A blue-hat inspector holds a checklist, a bell beside him"),
         "caption": ("클라우드 보안 점검은 매일 창고마다 문단속 표를 도는 거예요.", "A cloud security check is walking the lock-up list past every shed, every day."),
         "small": ("문이 열렸나, 상자가 길에서 보이나, 열쇠가 너무 많나. 사람이 아니라 기계가 매일 아침 돌아요. 잘못은 그 자리에서 종을 울려요.", "Is a door open, is a box visible from the road, are there too many keys? A machine walks it every morning, not a person. Anything wrong rings the bell on the spot."),
         "tricks": (4, [
             (SHARE_I, ("벽은 주인, 문은 우리", "Their walls, our doors"), ("책임을 나눠 가져요", "the responsibility is shared"), "calm"),
             (DAILY_I, ("매일 자동 점검", "Checked daily, automatically"), ("수백 개를 사람이 못 돌아요", "no person can walk hundreds")),
             (OPEN_I, ("열린 문 찾기", "Find the open doors"), ("길가 상자, 남는 열쇠", "boxes on the road, spare keys"), "warm"),
             (BELL_I, ("바로 종", "Ring at once"), ("경비실로, 때론 스스로 닫기", "to the guard room — or shut it itself")),
         ])},
        {"svg": P4, "alt": ("창고 문단속 표: 문이 잠겨 있나(체크), 열쇠가 너무 많지 않나(엑스), 상자는 봉인 편지로(체크), 일지가 켜져 있나(체크), 마을 규칙 표에 맞나(엑스). 옆에서 열린 문을 초록 화살표가 닫음", "The shed checklist: door locked (check), too many keys (X), boxes sealed (check), log switched on (check), matches the village rulebook (X). Beside it, a green arrow shuts an open door"),
         "caption": ("표는 매일 똑같아요. 그리고 열린 문은 기계가 바로 닫기도 해요.", "The list is the same every day. And an open door can be shut by the machine itself."),
         "small": ('열쇠가 많으면 <a href="iam-ko.html">명부 관리소</a>에, 상자는 <a href="encryption-ko.html">봉인 편지</a>로, <a href="log-ko.html">일지</a>는 켜 두기. 잘못 잠긴 문은 <a href="soc-ko.html">경비실</a>에 종을 울리거나 스스로 닫아요.',
                   'Too many keys goes to the <a href="iam-en.html">roster office</a>, boxes stay <a href="encryption-en.html">sealed</a>, the <a href="log-en.html">log</a> stays on. A badly locked door rings the <a href="soc-en.html">guard room</a> — or gets shut automatically.')},
        {"svg": P5, "alt": ("왼쪽: 길 위의 문지기 초소와 상자를 든 사람 — 창고 문지기. 오른쪽: 초록 체크가 붙은 창고와 표를 든 점검원 — 문단속 점검", "Left: a gatehouse on the road and a person carrying a box — the shed gatekeeper. Right: a shed with a green check and an inspector with a list — the lock-up check"),
         "caption": ("창고 문지기는 드나드는 사람을 보고, 문단속 점검은 창고 자체를 봐요.", "The shed gatekeeper watches who comes and goes; the lock-up check looks at the shed itself."),
         "small": ('<a href="casb-ko.html">바깥 창고 문지기</a>는 누가 뭘 들고 가는지 봐요. 문단속 점검은 문·열쇠·상자 놓인 자리를 봐요. 둘 다 있어야 해요 — 그래도 도둑이 창고 주인 벽을 뚫는 일은 점검표로 못 막아요.',
                   'The <a href="casb-en.html">outside-shed gatekeeper</a> watches who carries what. The lock-up check looks at doors, keys, and where boxes sit. It takes both — and even then, a checklist can\'t stop a thief who breaks through the owner\'s wall.')},
    ],
    "summary": (("<b>클라우드 보안(CSPM)</b> = 빌린 창고 수백 개의 <b>문단속</b>(열린 문, 길가 상자, 남는 열쇠)을 <b>기계가 매일</b> 표로 점검하고, 잘못은 <b>바로 종</b>을 울리거나 스스로 닫는 일. 벽은 주인이, 문은 우리가.",
                 "<b>Cloud security (CSPM)</b> = a <b>machine walks the lock-up list</b> past hundreds of rented sheds <b>every day</b> — open doors, boxes on the road, spare keys — and <b>rings the bell</b> or shuts the door itself. Their walls, our doors."),
                ("Cloud Security Posture Management. 클라우드 계정의 설정(공개 스토리지, 과다 IAM 권한, 미암호화, 로그 꺼짐)을 정책 기준으로 지속 점검해 잘못된 설정을 찾아 알리고 자동 수정해요. 공동 책임 모델에서 '우리 몫'을 지키는 도구예요.",
                 "Continuously checks cloud account configuration — public storage, excessive IAM permissions, missing encryption, disabled logging — against policy, flags misconfigurations, and can auto-remediate. It covers our side of the shared responsibility model.")),
    "glossary": [
        ("CSPM", "CSPM", ("문단속 점검 기계.", "The lock-up checking machine."), ("빌린 창고 수백 개를 매일 표대로 돌아요. 창고 안 상자가 아니라 문·열쇠·자리를 봐요.", "Walks the list past hundreds of rented sheds daily. Looks at doors, keys, and placement — not the boxes inside.")),
        ("공동 책임 모델", "Shared responsibility model", ("벽은 주인, 문은 우리.", "Their walls, our doors."), ("창고 주인이 벽·지붕·땅을 지키고, 우리가 문단속·열쇠·상자를 지켜요. 어디까지가 누구 몫인지 먼저 알아야 해요.", "The owner guards walls, roof, and ground; we guard locks, keys, and boxes. Know where the line is first.")),
        ("설정 오류", "Misconfiguration", ("안 잠근 문.", "The unlocked door."), ("벽이 뚫린 게 아니라 우리가 문을 열어 둔 것. 빌린 창고 사고의 대부분이에요.", "Not a broken wall — a door we left open. Most rented-shed accidents are this.")),
        ("공개 버킷", "Public bucket", ("길가에 놓인 상자.", "A box left on the road."), ("마을 사람 누구나 열어 볼 수 있게 놓인 상자. 제일 흔한 사고예요.", "A box anyone in the village can open. The most common accident of all.")),
        ("IAM 과다 권한", "Excessive IAM permissions", ("열쇠가 너무 많아요.", "Too many keys."), ('창고 하나에 열쇠 열 개면 하나는 잃어버려요. → <a href="iam-ko.html">성의 명부 관리소</a>', 'Ten keys to one shed, and one goes missing. → <a href="iam-en.html">the castle roster office</a>')),
        ("CASB 와의 차이", "Versus CASB", ("문지기는 사람을, 점검은 창고를.", "The gatekeeper watches people; the check watches sheds."), ('창고 문지기는 드나드는 사람과 상자를 보고, 문단속 점검은 창고 자체의 상태를 봐요. → <a href="casb-ko.html">바깥 창고 문지기</a>', 'The gatekeeper watches who comes and goes with what; the check looks at the shed\'s own condition. → <a href="casb-en.html">the outside-shed gatekeeper</a>')),
        ("컴플라이언스 검사", "Compliance check", ("마을 규칙 표.", "The village rulebook."), ("마을이 정한 규칙(어디에 뭘 두면 안 되나)에 창고 하나하나를 대 봐요. 같은 표로 매일요.", "Each shed is held up against the village rules — what may not go where. Same list, every day.")),
        ("자동 수정", "Auto-remediation", ("열린 문을 기계가 닫아요.", "The machine shuts the open door."), ("종을 울리고 기다리지 않고, 정해진 잘못은 그 자리에서 고쳐요. 길가 상자는 바로 안으로.", "Instead of ringing and waiting, known mistakes are fixed on the spot. A box on the road goes straight back inside.")),
    ],
}
