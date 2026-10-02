from _draw import *
from _world import *


def _budget_grid(x, y, filled, total=20, cw=26, ch=16, gap=4, cols=10):
    cells = []
    for i in range(total):
        row, col = divmod(i, cols)
        cx, cy = x + col * (cw + gap), y + row * (ch + gap)
        color = "#E9B44C" if i < filled else "var(--stone)"
        cells.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="3" fill="{color}" stroke="#C9822B" stroke-width="1.5"/>')
    return "".join(cells)


# 1. 정비사가 새 기구를 못 만들고, 공원이 멈춰요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.8, face=FROWN + SWEAT, extra=WRENCH, **MECHANIC)
         + bubble(40, 50, 270, 50, "⟦새 기구는 무서워서 못 만들겠어요|new rides scare me — I can't build them⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(540, 230, 0.7, color="var(--stone)", closed=True, label_text="⟦새 기구 (보류)|new ride (on hold)⟧")
         + label(380, 282, "⟦아무것도 안 바꾸니 공원이 그대로 멈췄어요|nothing changes, so the park just stands still⟧", 12, "var(--ink)", cls="d"))

# 2. 왜: 절대 고장나면 안 돼만 외치면 아무도 시도를 안 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(260, 40, 240, 70, "⟦규칙|RULE⟧", ("⟦절대 고장나면 안 돼!|never, ever break!⟧",), 1.0)
         + person(150, 190, s=0.65, face=FROWN, **ROOKIE)
         + person(610, 190, s=0.65, face=FROWN + SWEAT, **MECHANIC)
         + label(380, 282, "⟦겁만 주면 아무도 새로운 시도를 안 해요|scare everyone enough, and nobody tries anything new⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 목표에서 남는 여유가 써도 되는 고장 티켓이에요
BUDGET_I = icon('<rect x="8" y="22" width="48" height="26" rx="4" fill="#E9B44C" stroke="#C9822B" stroke-width="3"/><circle cx="8" cy="35" r="4" fill="var(--bg)"/><circle cx="56" cy="35" r="4" fill="var(--bg)"/>')
TRY_I = icon('<path d="M32 10 L40 26 L58 28 L44 40 L48 58 L32 48 L16 58 L20 40 L6 28 L24 26 Z" fill="var(--accent)"/>')
STOP_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)"/><rect x="20" y="29" width="24" height="6" rx="3" fill="#FFF8E7"/>')
RESET_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M44 16 a24 24 0 0 1 6 14" stroke="var(--good)" stroke-width="4" fill="none"/><path d="M20 48 a24 24 0 0 1 -6 -14" stroke="var(--good)" stroke-width="4" fill="none"/>')

P3 = svg(320, sky(320)
         + board(50, 50, 230, 110, "⟦목표(SLO)|TARGET (SLO)⟧", ("⟦99.9%|99.9%⟧",), 1.0)
         + '<path d="M290 100 L350 90" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ticket(380, 90, 0.75, text="⟦버짓|budget⟧") + ticket(450, 90, 0.75, text="⟦버짓|budget⟧") + ticket(520, 90, 0.75, text="⟦버짓|budget⟧")
         + label(450, 140, "⟦나머지 0.1%|the remaining 0.1%⟧", 11, "var(--ink)")
         + ride(610, 280, 0.75, color="#5B8DEF") + person(560, 220, s=0.7, face=SMILE, **ROOKIE)
         + label(380, 28, "⟦목표의 남는 여유가 써도 되는 고장 티켓이에요|the slack in the target is a ticket you're allowed to spend on failure⟧", 14, "var(--ink)", cls="d")
         + label(380, 305, "⟦티켓이 남아 있으면 새 기구도 과감히 시도해도 돼요|as long as tickets remain, go ahead and try the new ride⟧", 12, "var(--muted)"))

# 4. 70장 남음 vs 5장 남음
P4 = svg(320, sky(320, ground=False)
         + label(208, 65, "⟦100장 중 70장 남음|70 of 100 left⟧", 13, "var(--good)", cls="d")
         + _budget_grid(60, 90, 14)
         + label(208, 165, "⟦과감히 시도해도 돼요!|go ahead and try something new!⟧", 12, "var(--good)")
         + label(568, 65, "⟦100장 중 5장 남음|5 of 100 left⟧", 13, "var(--bad)", cls="d")
         + _budget_grid(420, 90, 1)
         + label(568, 165, "⟦조심해야 해요!|be careful now!⟧", 12, "var(--bad)")
         + label(380, 300, "⟦버짓이 남은 만큼 과감함이 달라져요|how much budget is left changes how bold you can be⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳: 버짓 다 썼는데 계속 밀어붙이면 손님이 떠나요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + _budget_grid(60, 40, 0)
         + label(208, 20, "⟦버짓 0장|0 tickets left⟧", 12, "var(--bad)", cls="d")
         + person(430, 150, s=0.7, face=EYES, **MANAGER)
         + bubble(360, 50, 220, 46, "⟦그래도 새 기능 내보내요!|let's ship the new feature anyway!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + queueline(560, 184, 3, 0.45, 30)
         + label(650, 235, "⟦손님이 떠나요|guests walk away⟧", 11, "var(--bad)")
         + label(380, 282, "⟦다 썼으면 멈추고 고치는 규칙이 있어야 해요|once it's spent, a rule has to make everyone stop and fix⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "errorbudget", "order": 5,
    "title": ("허용된 고장 티켓 묶음", "The Bundle of Allowed-Failure Tickets"),
    "h1": ("<em>에러 버짓</em>이 뭐예요?", "What is an <em>Error Budget</em>?"),
    "sub": ("에러 버짓을 목표에서 남는 만큼 써도 되는 고장 티켓 묶음 이야기로 풀어봤어요.",
            "An error budget, told as a story about a bundle of tickets you're allowed to spend on failure."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 새 기구가 무섭다고 말하고, 새 기구는 보류된 채 멈춰 있음", "A mechanic says new rides scare them, and a new ride sits closed and on hold"),
         "caption": ("아무것도 안 바꾸니 공원이 그대로 멈췄어요.", "Nothing changes, so the park just stands still."),
         "small": ("고장날까 봐 겁내서 아무 시도도 안 해요.", "Too scared of breaking it, so nobody tries anything.")},
        {"svg": P2, "alt": ("절대 고장나면 안 된다는 규칙 안내판, 신참과 정비사가 겁먹은 채 서 있음", "A rule board says never, ever break, while a rookie and a mechanic stand frozen with fear"),
         "caption": ("왜 어려운가요?", "Why is this hard?"),
         "small": ("겁만 주면 아무도 새로운 시도를 안 해요.", "Scare everyone enough, and nobody tries anything new.")},
        {"svg": P3, "hero": True, "alt": ("목표 99.9% 안내판에서 화살표가 버짓 티켓 세 장으로 이어지고, 신참이 웃으며 새 기구를 탐", "An arrow runs from a 99.9% target board to three budget tickets, while a rookie smiles and rides the new ride"),
         "caption": ("목표의 남는 여유가 써도 되는 고장 티켓이에요.", "The slack in the target is a ticket you're allowed to spend on failure."),
         "small": ("티켓이 남아 있으면 새 기구도 과감히 시도해도 돼요.", "As long as tickets remain, go ahead and try the new ride."),
         "tricks": (4, [
             (BUDGET_I, ("목표에서 남는 여유가 버짓", "The slack from the target is the budget"), ("0.1%가 티켓이 돼요", "that 0.1% becomes the tickets"), "calm"),
             (TRY_I, ("버짓 남으면 과감히 시도", "Budget left? Try something bold"), ("새 기능도 OK", "new features are fine")),
             (STOP_I, ("버짓 다 쓰면 안정에 집중", "Budget spent? Focus on stability"), ("당분간 새 기능은 멈춰요", "new features pause for a while"), "warm"),
             (RESET_I, ("버짓은 다시 채워져요", "The budget refills"), ("매달 또는 매주요", "every month or every week")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 100장 중 70장 남은 티켓 그리드, 과감히 시도. 오른쪽: 5장만 남은 그리드, 조심하라는 경고", "Left: a grid showing 70 of 100 tickets left, inviting boldness. Right: a grid showing only 5 left, warning caution"),
         "caption": ("버짓이 남은 만큼 과감함이 달라져요.", "How much budget is left changes how bold you can be."),
         "small": ("많이 남으면 과감하게, 적게 남으면 조심스럽게.", "Plenty left means go bold; little left means go careful.")},
        {"svg": P5, "alt": ("버짓 0장인데 공원장이 그래도 새 기능을 내보내자고 하고, 손님들이 줄지어 떠남", "With zero tickets left, the manager still pushes to ship a new feature, and a line of guests walks away"),
         "caption": ("다 썼으면 멈추고 고치는 규칙이 있어야 해요.", "Once it's spent, a rule has to make everyone stop and fix."),
         "small": ("안 그러면 손님이 떠나요.", "Otherwise, guests walk away.")},
    ],
    "summary": (("<b>에러 버짓</b> = 목표(<b>SLO</b>)에서 남는 <b>써도 되는 고장 티켓</b>. 남아 있으면 <b>과감히 새로 시도</b>하고, 다 쓰면 <b>멈추고 고치는 일이 먼저</b>예요.",
                 "An <b>error budget</b> is the <b>ticket for allowed failure</b> left over by the target (<b>SLO</b>). While it lasts, <b>try bold new things</b>; once it's spent, <b>stopping to fix comes first</b>."),
                ("Error budget. SLO가 99.9%면 나머지 0.1%가 버짓이에요. 얼마나 빨리 쓰는지는 번 레이트로 보고, 버짓을 다 쓰면 새 기능 배포를 멈추는 정책을 흔히 둬요. 혁신과 안정 사이의 균형을 숫자로 만든 장치예요.",
                 "If the SLO is 99.9%, the remaining 0.1% is the budget. A burn rate tracks how fast it's spent, and teams often set a policy to pause new releases once it hits zero — a numeric balance between innovation and stability.")),
    "glossary": [
        ("에러 버짓", "Error budget", ("목표에서 남는, 써도 되는 여유.", "The slack from the target that's allowed to be spent."), ("100%에서 목표를 뺀 만큼이에요.", "It's 100% minus the target.")),
        ("버짓 소진 속도", "Burn rate", ("버짓을 까먹는 속도.", "How fast the budget gets used up."), ("너무 빠르면 경고가 와요.", "A fast burn triggers a warning.")),
        ("목표와의 관계", "Relation to SLO", ("목표가 버짓의 크기를 정해요.", "The target sets the size of the budget."), ('목표가 빡빡할수록 버짓은 작아요. → <a href="slo-ko.html">우리끼리 정한 목표 줄</a>', 'A tighter target means a smaller budget. → <a href="slo-en.html">the target line set internally</a>')),
        ("혁신 vs 안정", "Innovation vs stability", ("새 시도와 안정 사이의 줄다리기.", "The tug-of-war between trying new things and staying stable."), ("버짓이 그 균형을 숫자로 보여줘요.", "The budget turns that balance into a number.")),
        ("버짓 정책", "Budget policy", ("다 쓰면 멈추는 규칙.", "The rule that stops things once it's spent."), ("새 기능 배포를 잠시 멈춰요.", "It pauses new feature releases for a while.")),
        ("월간/분기 리셋", "Monthly reset", ("버짓이 다시 채워지는 주기.", "The cycle on which the budget refills."), ("보통 매달이나 분기마다예요.", "Usually every month or every quarter.")),
        ("번 레이트 알림", "Burn-rate alert", ("너무 빨리 써버릴 때 울려요.", "Fires when it's being spent too fast."), ('호출기로 바로 알려줘요. → <a href="alerting-ko.html">몇 번 울려야 진짜 비상인가</a>', 'It pages someone right away. → <a href="alerting-en.html">how many rings mean a real emergency</a>')),
        ("운행 기록", "SLI", ("버짓이 얼마나 남았는지 재는 숫자.", "The number that measures how much is left."), ("매일의 실제 기록에서 계산해요.", "Calculated from the actual daily record.")),
    ],
}
