from _draw import *
from _world import *

# 1. 공연 당일, 비가 쏟아지는데 아무 대비가 없어요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + stage(120, 170, 240, 60) + person(540, 150, s=0.8, face=SWEAT + FROWN, **PLANNER)
         + '<path d="M160 30 l-10 24 M200 20 l-10 24 M280 20 l-10 24 M320 30 l-10 24" stroke="#5B9BD5" stroke-width="4" stroke-linecap="round"/>'
         + label(380, 282, "⟦공연 당일, 비가 쏟아지는데 아무 대비가 없어요|rain pours down on show day, with nothing prepared⟧", 12, "var(--ink)", cls="d"))

# 2. 왜: 안 터지면 낭비로 보이고, 터지면 이미 늦어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **SPONSOR)
         + bubble(60, 70, 240, 46, "⟦우산은 왜 미리 사둬요? 돈 낭비예요|why buy an umbrella in advance? that's a waste⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=FROWN + SWEAT, **PLANNER)
         + bubble(440, 70, 240, 46, "⟦근데 이미 다 젖어버렸어요|but everyone's already soaked now⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦안 보이는 위험이 제일 무서워요, 보일 땐 이미 늦어요|the risk you can't see is the scary one — by the time you see it, it's too late⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 위험관리 = 안 써도 늘 챙겨두는 우산
P3 = svg(340, sky(340)
         + person(260, 200, s=0.9, face=SMILE, **PLANNER) + umbrella(287, 195, 0.9)
         + person(480, 210, s=0.75, face=SMILE, **ARTIST)
         + label(380, 30, "⟦위험관리 = 안 써도 늘 챙겨두는 우산|risk management = the umbrella you always bring, even unused⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦써먹을 일이 없는 날이 제일 좋은 날이에요|the day you never open it is the best day⟧", 12, "var(--muted)"))

ID_I = icon('<circle cx="32" cy="26" r="16" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M44 38 l14 14" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
RANK_I = icon('<rect x="10" y="38" width="12" height="16" fill="var(--good)"/><rect x="26" y="26" width="12" height="28" fill="var(--accent)"/><rect x="42" y="12" width="12" height="42" fill="var(--bad)"/>')
RESP_I = icon('<path d="M20 20 L44 44 M44 20 L20 44" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/><circle cx="32" cy="32" r="26" fill="none" stroke="var(--line)" stroke-width="3"/>')
WATCH_I = icon('<circle cx="32" cy="34" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 22 v12 l8 6" stroke="var(--accent)" stroke-width="3" fill="none"/><rect x="26" y="8" width="12" height="6" fill="var(--accent)"/>')

# 4. 위험 대응전략 네 가지 비교
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 260, "⟦위험 대응 전략|RESPONSE STRATEGY⟧",
                     ("⟦회피 — 아예 야외공연을 접어요|avoid — cancel the outdoor show⟧",
                      "⟦전가 — 보험·외주로 떠넘겨요|transfer — shift it via insurance⟧",
                      "⟦완화 — 천막을 쳐서 줄여요|mitigate — a tent cuts the impact⟧",
                      "⟦수용 — 작은 위험은 그냥 안고 가요|accept — small risk, just carry it⟧"), 1.0)
         + umbrella(560, 150, 1.1)
         + label(380, 300, "⟦위험마다 다른 전략을 골라요|pick a different strategy for each risk⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 우산 챙겼다고 비가 안 오는 게 아니에요
P5 = svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + '<path d="M120 20 l-8 20 M160 10 l-8 20 M200 20 l-8 20" stroke="#5B9BD5" stroke-width="4" stroke-linecap="round"/>'
         + person(190, 140, s=0.8, face=FROWN, **PLANNER) + label(190, 270, "⟦비는 여전히 와요|the rain still comes⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=SMILE, **PLANNER) + umbrella(594, 126, 0.8) + label(570, 270, "⟦그래도 우산 덕에 젖지 않아요|but thanks to the umbrella, nobody gets soaked⟧", 11, "var(--ink)")
         + label(380, 307, "⟦위험관리는 위험을 없애는 게 아니라 대응할 여지를 남기는 거예요|risk management isn't erasing the risk — it's leaving room to respond⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "projrisk", "order": 2,
    "title": ("비 오는 날에도 챙기는 우산", "The Umbrella You Carry Even on a Dry Day"),
    "h1": ("<em>프로젝트 위험관리</em>가 뭐예요?", "What is <em>Project Risk Management</em>?"),
    "sub": ("프로젝트 위험관리를, 공연 당일 비가 올지 몰라 늘 챙겨두는 우산 이야기로 풀어봤어요.",
            "Project risk management, told as a story about an umbrella you always carry, just in case it rains on show day."),
    "panels": [
        {"svg": P1, "alt": ('공연 당일 비가 쏟아지지만 기획자는 대비가 없어 당황함', 'Rain pours on show day, and the planner panics with nothing prepared'),
         "caption": ("공연 당일, 비가 쏟아지는데 아무 대비가 없어요.", "Rain pours down on show day, with nothing prepared."),
         "small": ("완벽한 체크리스트를 짜도 당일 변수는 늘 남아요.", "Even a perfect checklist always leaves something unaccounted for on the day.")},
        {"svg": P2, "alt": ('후원사는 우산 준비가 낭비라고 말하지만, 비가 오자 이미 다 젖어버림', 'The sponsor calls the umbrella a waste, then everyone gets soaked once the rain starts'),
         "caption": ("안 터지면 낭비로 보이고, 터지면 이미 늦어요.", "If it never happens it looks wasteful — if it does, it's already too late."),
         "small": ("안 보이는 위험이 제일 무서워요, 보일 땐 이미 늦어요.", "The risk you can't see is the scary one — by the time you see it, it's too late.")},
        {"svg": P3, "hero": True, "alt": ('기획자가 우산을 쓰고 맑은 날에도 웃으며 준비하고 있음', 'The planner holds an umbrella and smiles, prepared even on a clear day'),
         "caption": ("위험관리는 안 써도 늘 챙겨두는 우산이에요.", "Risk management is the umbrella you always bring, even unused."),
         "small": ("써먹을 일이 없는 날이 제일 좋은 날이에요.", "The day you never open it is the best day."),
         "tricks": (4, [
             (ID_I, ("위험 식별하기", "Identify risk"), ("무엇이 터질 수 있는지 목록 뽑기", "list what could go wrong"), "calm"),
             (RANK_I, ("위험 분석하기", "Analyze risk"), ("확률 × 영향으로 순위 매기기", "rank by likelihood × impact")),
             (RESP_I, ("대응 전략 짜기", "Plan response"), ("회피·전가·완화·수용 중 고르기", "choose avoid, transfer, mitigate, or accept"), "warm"),
             (WATCH_I, ("계속 지켜보기", "Keep watching"), ("상황이 바뀌면 전략도 바꿔요", "update the plan as things change")),
         ])},
        {"svg": P4, "alt": ('위험 대응 전략 네 가지 체크리스트: 회피, 전가, 완화, 수용', 'A checklist of four risk response strategies: avoid, transfer, mitigate, accept'),
         "caption": ("위험마다 고르는 전략이 달라요.", "A different strategy fits each risk."),
         "small": ("큰 위험은 피하거나 떠넘기고, 작은 위험은 줄이거나 안고 가요.", "Big risks get avoided or transferred — small ones get reduced or accepted.")},
        {"svg": P5, "alt": ('왼쪽: 우산 없이 비를 맞아 속상함. 오른쪽: 우산 덕에 비를 맞아도 젖지 않음', 'Left: caught in the rain without an umbrella, upset. Right: the rain still falls, but the umbrella keeps them dry'),
         "caption": ("우산 챙겼다고 비가 안 오는 게 아니에요.", "Carrying the umbrella doesn't stop the rain."),
         "small": ("위험관리는 없애는 게 아니라 대응할 여지를 남기는 거예요.", "Risk management isn't erasing the risk — it's leaving room to respond.")},
    ],
    "summary": (("<b>프로젝트 위험관리</b> = 공연 날씨처럼 <b>미리 알 수 없는 변수</b>를 찾아내 <b>대응할 여지를 남겨두는</b> 일.",
                 "<b>Project risk management</b> = finding variables you can't foresee — like show-day weather — and leaving room to respond to them."),
                ("프로젝트 위험관리는 위험을 식별(Identify)하고, 발생확률과 영향도로 분석(Analyze)한 뒤, 회피·전가·완화·수용 중 하나로 대응(Response)하고, 프로젝트 내내 모니터링하는 활동이에요. 위험을 0으로 만드는 게 목표가 아니라, 감당 가능한 수준으로 관리하는 게 목표예요.",
                 "Project risk management identifies risks, analyzes them by probability and impact, chooses a response — avoid, transfer, mitigate, or accept — and monitors them throughout the project. The goal isn't zero risk; it's keeping risk at a manageable level.")),
    "glossary": [
        ("위험 식별", "Risk Identification", ("비가 올지도 모른다고 떠올리는 일.", "Thinking of the chance it might rain."), ("브레인스토밍·체크리스트로 목록을 뽑아요.", "Lists come from brainstorming and checklists.")),
        ("위험 분석", "Risk Analysis", ("비가 올 확률과 피해 크기를 재는 일.", "Gauging the odds of rain and how bad it'd be."), ("확률 × 영향도로 우선순위를 매겨요.", "Ranked by probability × impact.")),
        ("회피", "Avoid", ("아예 야외공연을 접는 전략.", "The strategy of canceling the outdoor show entirely."), ("가장 강력하지만 비용이 커요.", "Strongest option, but costly.")),
        ("전가", "Transfer", ("보험이나 외주로 위험을 넘기는 전략.", "Shifting risk via insurance or outsourcing."), ("위험 자체가 없어지진 않아요.", "The risk itself doesn't disappear.")),
        ("완화", "Mitigate", ("천막을 쳐서 피해를 줄이는 전략.", "Pitching a tent to shrink the damage."), ("가장 흔히 쓰는 전략이에요.", "The most commonly used strategy.")),
        ("수용", "Accept", ("작은 위험은 그냥 안고 가는 전략.", "Just carrying small risks as they are."), ("대응 비용이 위험보다 클 때 써요.", "Used when the fix would cost more than the risk itself.")),
        ("WBS", "WBS", ("공연 준비를 쪼갠 체크리스트.", "The checklist that breaks show prep into pieces."), ('위험은 이 체크리스트의 각 항목에 숨어 있어요. → <a href="wbsppm-ko.html">공연 준비를 쪼갠 체크리스트</a>', 'Risk hides inside each item of this checklist. → <a href="wbsppm-en.html">the checklist that breaks down show prep</a>')),
        ("BCP", "BCP", ("정전처럼 큰 사고에도 공연을 이어가는 계획.", "The plan that keeps the show going even through a blackout-sized disaster."), ('더 큰 위험(재해급)에 대한 대비예요. → <a href="bcpplan-ko.html">정전에도 멈추지 않는 투어</a>', 'Preparation for even bigger (disaster-scale) risk. → <a href="bcpplan-en.html">the tour that doesn\'t stop for a blackout</a>')),
    ],
}
