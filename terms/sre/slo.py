from _draw import *
from _world import *

# 1. 관제실과 정비사가 매번 말다툼해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 156, s=0.75, face=FROWN, **OPERATOR)
         + bubble(60, 50, 220, 46, "⟦이 정도면 괜찮은 거 아니야?|isn't this good enough?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(470, 156, s=0.75, face=FROWN, **MECHANIC)
         + bubble(370, 50, 210, 46, "⟦아니, 더 잘해야지!|no, we need to do better!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦관제실과 정비사가 매번 이 말로 다퉈요|the control room and the mechanic argue over this every time⟧", 12, "var(--ink)", cls="d"))

# 2. 왜: 기준이 없으면 사람마다 괜찮다의 기준이 달라요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(130, 178, s=0.55, face=EYES, **OPERATOR)
         + bubble(40, 70, 180, 44, "⟦90%면 충분하지|90% is plenty⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(400, 178, s=0.55, face=EYES, **MECHANIC)
         + bubble(300, 70, 190, 44, "⟦99%는 돼야지|has to be 99%⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(650, 178, s=0.55, face=EYES, **MANAGER)
         + bubble(560, 70, 190, 44, "⟦99.99%는 돼야!|needs to be 99.99%!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 305, "⟦기준이 없으면 사람마다 괜찮다가 달라요|without a shared line, everyone's idea of fine is different⟧", 13, "var(--ink)", cls="d"))

# 3. hero: SLI 숫자를 보고 미리 목표를 약속해요
GAUGE_I = icon('<rect x="10" y="38" width="10" height="16" fill="var(--good)"/><rect x="26" y="26" width="10" height="28" fill="var(--good)"/><rect x="42" y="14" width="10" height="40" fill="var(--good)"/><path d="M6 20 H58" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 4"/>')
ROOM_I = icon('<rect x="8" y="12" width="12" height="40" fill="var(--stone-dark)"/><rect x="44" y="12" width="12" height="40" fill="var(--stone-dark)"/><path d="M26 32 H38" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>')
FIXFIRST_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--bad-soft)" stroke="var(--bad)" stroke-width="3"/><path d="M22 42 L42 22" stroke="#5A3B22" stroke-width="5" stroke-linecap="round"/><circle cx="42" cy="22" r="6" fill="none" stroke="#5A3B22" stroke-width="4"/>')
REVIEW_I = icon('<circle cx="30" cy="34" r="20" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M30 20 V34 L42 40" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M46 16 a24 24 0 0 1 6 14" stroke="var(--good)" stroke-width="4" fill="none"/>')

P3 = svg(350, sky(350)
         + controlroom(50, 50, 230, 140, bars=((0.6, "var(--good)"), (0.5, "var(--good)"), (0.65, "var(--good)"), (0.55, "var(--good)")))
         + label(165, 212, "⟦오늘 기록 (SLI)|today's record (SLI)⟧", 11, "var(--ink)")
         + '<path d="M290 120 L370 120" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + board(370, 50, 320, 170, "⟦우리끼리 정한 목표|OUR OWN TARGET⟧", ("⟦목표: 한 달 99.9%|target: 99.9% a month⟧", "⟦1초 안에 응답하기|respond within 1 second⟧", "⟦이 안에선 자유롭게|free to move within it⟧"), 1.0)
         + person(650, 250, s=0.8, face=SMILE, **OPERATOR)
         + label(380, 28, "⟦오늘 기록을 보고, 미리 숫자로 약속해 둬요|look at today's numbers, then promise a target in advance⟧", 14, "var(--ink)", cls="d")
         + label(380, 335, "⟦이 안에 있으면 자유롭게, 넘으면 다 같이 멈춰요|stay inside it freely — cross it, and everyone pauses⟧", 12, "var(--muted)"))

# 4. 목표 줄 그래프 — 실제 숫자가 위아래로 오가요
TARGET_Y = 170
PTS = [(60, 150), (160, 130), (260, 165), (360, 205), (460, 215), (560, 160), (660, 140)]


def _seg_color(a, b):
    return "var(--bad)" if a > TARGET_Y or b > TARGET_Y else "var(--good)"


CHART_LINES = "".join(
    f'<path d="M{PTS[i][0]} {PTS[i][1]} L{PTS[i + 1][0]} {PTS[i + 1][1]}" stroke="{_seg_color(PTS[i][1], PTS[i + 1][1])}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    for i in range(len(PTS) - 1))
CHART_DOTS = "".join(
    f'<circle cx="{x}" cy="{y}" r="4" fill="{"var(--bad)" if y > TARGET_Y else "var(--good)"}"/>' for x, y in PTS)

P4 = svg(320, sky(320, ground=False)
         + '<rect x="260" y="170" width="300" height="60" fill="var(--bad-soft)"/>'
         + f'<path d="M60 {TARGET_Y} H700" stroke="var(--accent)" stroke-width="3" stroke-dasharray="7 5"/>'
         + label(140, 150, "⟦목표선: 99.9%|target line: 99.9%⟧", 11, "var(--accent)", "start")
         + CHART_LINES + CHART_DOTS
         + label(410, 255, "⟦넘은 구간|crossed the line⟧", 12, "var(--bad)", cls="d")
         + label(380, 300, "⟦실제 숫자가 목표 줄 위아래로 오가요|the real numbers wander above and below the target line⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳: 목표를 너무 높게 잡으면 돈이 끝없이 들어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + board(40, 30, 300, 120, "⟦손님이 진짜 필요한 만큼|WHAT GUESTS ACTUALLY NEED⟧", ("⟦목표: 99.9%|target: 99.9%⟧", "⟦비용: 적당해요|cost: reasonable⟧"), 1.0)
         + gauge(190, 210, 1.0, level=0.6, label_text="⟦비용|cost⟧", color="var(--good)")
         + board(420, 30, 300, 120, "⟦너무 높은 목표|TOO HIGH A TARGET⟧", ("⟦목표: 99.999%|target: 99.999%⟧", "⟦비용: 끝이 없어요|cost: never stops⟧"), 1.0)
         + gauge(570, 210, 1.0, level=0.97, label_text="⟦비용|cost⟧", color="var(--bad)")
         + label(380, 282, "⟦손님이 진짜 필요한 만큼만 약속해요|promise only as much as guests really need⟧", 13, "var(--ink)", cls="d"))

PAGE = {
    "slug": "slo", "order": 34,
    "title": ("우리끼리 정한 목표 줄", "The Target Line We Set Ourselves"),
    "h1": ("<em>SLO</em>가 뭐예요?", "What is an <em>SLO</em>?"),
    "sub": ("SLO(서비스 수준 목표)를 공원이 스스로 그어 둔 약속 줄 이야기로 풀어봤어요.",
            "A Service Level Objective, told as a story about the line a park draws for itself and promises to stay inside."),
    "panels": [
        {"svg": P1, "alt": ("관제실 요원과 정비사가 괜찮은 수준을 두고 말다툼함", "A control-room operator and a mechanic argue over what counts as good enough"),
         "caption": ("관제실과 정비사가 매번 이 말로 다퉈요.", "The control room and the mechanic argue over this every time."),
         "small": ("괜찮다의 기준이 사람마다 달라서 늘 싸워요.", "Everyone's idea of fine is different, so it always ends in a fight.")},
        {"svg": P2, "alt": ("세 사람이 90%, 99%, 99.99% 각각 다른 기준을 말함", "Three people each say a different number — 90%, 99%, 99.99% — is good enough"),
         "caption": ("왜 어려운가요?", "Why is this hard?"),
         "small": ("기준이 없으면 사람마다 괜찮다가 달라요.", "Without a shared line, everyone's idea of fine is different.")},
        {"svg": P3, "hero": True, "alt": ("관제실 기록판 옆에 목표 안내판, 요원이 웃으며 둘을 연결함", "A record board beside a target board, with a smiling operator connecting the two"),
         "caption": ("오늘 기록을 보고, 미리 숫자로 약속해 둬요.", "Look at today's numbers, then promise a target in advance."),
         "small": ("이 안에 있으면 자유롭게, 넘으면 다 같이 멈춰요.", "Stay inside it freely — cross it, and everyone pauses."),
         "tricks": (4, [
             (GAUGE_I, ("SLI 숫자 보고 목표 정하기", "Set the target from SLI numbers"), ("오늘 기록이 기준이에요", "today's record is the baseline"), "calm"),
             (ROOM_I, ("너무 빡빡하면 숨 막혀요", "Too tight and there's no room to breathe"), ("여유가 에러 버짓이에요", "the slack is the error budget")),
             (FIXFIRST_I, ("넘치면 고치기부터", "Cross it, and fixing comes first"), ("새 기능보다 먼저요", "before any new feature"), "warm"),
             (REVIEW_I, ("가끔 다시 봐요", "Review it once in a while"), ("목표도 바뀔 수 있어요", "the target can change too")),
         ])},
        {"svg": P4, "alt": ("목표선 그래프에 실제 숫자가 위아래로 오가고, 넘은 구간은 빨갛게 표시됨", "A target-line chart where the real numbers wander above and below, with the crossed stretch marked red"),
         "caption": ("실제 숫자가 목표 줄 위아래로 오가요.", "The real numbers wander above and below the target line."),
         "small": ("넘은 구간이 보이면 바로 알아챌 수 있어요.", "When a stretch crosses the line, you can see it right away.")},
        {"svg": P5, "alt": ("왼쪽: 목표 99.9%, 적당한 비용. 오른쪽: 목표 99.999%, 끝없는 비용", "Left: a 99.9% target with a reasonable cost gauge. Right: a 99.999% target with a cost gauge pinned near the top"),
         "caption": ("완벽한 가동은 없어요. 대신 미리 약속해 둬요.", "There's no such thing as perfect uptime. Instead, promise in advance."),
         "small": ("목표를 너무 높게 잡으면 돈이 끝없이 들어요.", "Set the target too high, and the cost never stops growing.")},
    ],
    "summary": (("<b>SLO</b> = 오늘의 운행 기록(<b>SLI</b>)을 보고 <b>우리끼리 미리 약속해 둔 목표 줄</b>. 이 안에 있으면 자유롭게 움직이고, 넘으면 <b>고치는 일이 새 기능보다 먼저</b>예요.",
                 "An <b>SLO</b> is the <b>target line a team sets for itself</b> by looking at today's record (<b>SLI</b>). Stay inside it and move freely; cross it, and <b>fixing comes before any new feature</b>."),
                ("Service Level Objective. 손님과 맺는 공식 계약(SLA)과는 달라요 — SLO는 속으로 정한, 보통 SLA보다 빡빡한 목표예요. 목표에서 남는 여유가 에러 버짓이고, 번 레이트로 얼마나 빨리 써버리는지 지켜봐요.",
                 "A target the team sets for itself, distinct from the formal SLA made with customers — usually stricter than the SLA. The slack left over is the error budget, and a burn rate tracks how fast it's being spent.")),
    "glossary": [
        ("목표", "SLO", ("우리끼리 정한 약속 줄.", "The promise line a team sets for itself."), ("넘으면 다 같이 멈춰요.", "Cross it, and everyone pauses.")),
        ("운행 기록", "SLI", ("오늘 실제로 잰 숫자.", "The number actually measured today."), ('이 숫자를 보고 목표를 정해요. → <a href="sli-ko.html">오늘 운행 기록판</a>', 'This number is what sets the target. → <a href="sli-en.html">today\'s record board</a>')),
        ("에러 버짓", "Error budget", ("목표에서 남는 여유.", "The slack left over by the target."), ('남아 있으면 새 시도도 과감히. → <a href="errorbudget-ko.html">허용된 고장 티켓 묶음</a>', 'Spend it on bold new tries. → <a href="errorbudget-en.html">the bundle of allowed-failure tickets</a>')),
        ("목표 설정 기준", "Setting the target", ("오늘 기록에서 출발해요.", "Starts from today's record."), ("너무 높으면 비용이 끝없이 들어요.", "Set it too high, and the cost never stops growing.")),
        ("내부 목표 vs 외부 계약", "SLO vs SLA", ("속으로 정한 것과 손님과 약속한 것.", "What's set internally versus promised to the customer."), ('계약은 보통 이 목표보다 느슨해요. → <a href="sla-ko.html">손님과 맺은 약속 계약서</a>', 'The contract is usually looser than this. → <a href="sla-en.html">the promise written up for the customer</a>')),
        ("재검토 주기", "Review cadence", ("가끔 다시 들여다봐요.", "Looked at again every so often."), ("손님도 시스템도 바뀌니까요.", "Because both guests and the system change.")),
        ("버닝", "Burn rate", ("여유를 까먹는 속도.", "How fast the slack gets spent."), ("빠르게 줄면 미리 경고해요.", "A fast drop triggers a warning early.")),
        ("계기판", "Golden signals", ("오늘 기록을 재는 계기판 네 개.", "The four gauges that measure today's record."), ('레이턴시·트래픽·에러·포화. → <a href="goldensignals-ko.html">관제실의 계기판 네 개</a>', 'Latency, traffic, errors, saturation. → <a href="goldensignals-en.html">the four gauges on the control-room wall</a>')),
    ],
}
