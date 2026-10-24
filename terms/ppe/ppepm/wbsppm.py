from _draw import *
from _world import *

# 1. 공연 준비해 달란 말만 있고, 뭐부터 해야 할지 막막해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **SPONSOR)
         + bubble(60, 70, 230, 46, "⟦투어 준비, 잘 부탁해요|please get the tour ready⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 170, s=0.85, face=SWEAT + EYES, **PLANNER)
         + label(380, 250, "⟦공연 준비해 달란 말만 있고, 뭐부터 해야 할지 막막해요|told to just get the show ready, with no idea where to start⟧", 13, "var(--ink)", cls="d")
         + label(380, 282, "⟦큰 일을 통째로 보면 다 막막해 보여요|a big job looks overwhelming as one giant block⟧", 12, "var(--muted)"))

# 2. 왜: 큰 덩어리로 보면 뭘 빠뜨렸는지도 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="230" y="40" width="300" height="140" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + label(380, 70, "⟦공연 준비|SHOW PREP⟧", 16, "#142033", cls="d")
         + label(380, 120, "⟦조명? 의상? 티켓?...|lighting? costumes? tickets?...⟧", 12, "#142033")
         + label(380, 150, "⟦다 뒤섞여 있어요|it's all jumbled together⟧", 12, "var(--bad)")
         + person(620, 190, s=0.75, face=FROWN, **PLANNER)
         + label(380, 250, "⟦큰 덩어리로 보면 뭘 빠뜨렸는지도 몰라요|seen as one big lump, you can't tell what's missing⟧", 13, "var(--ink)", cls="d")
         + label(380, 282, "⟦작게 쪼개야 비로소 보여요|only breaking it down small makes it visible⟧", 12, "var(--muted)"))

ROOT = '<rect x="310" y="50" width="140" height="40" rx="6" fill="var(--accent)"/>' + label(380, 75, "⟦공연 준비|SHOW PREP⟧", 13, "#FFF8E7", cls="d")
LINES = '<path d="M380 90 V110 M190 110 H570 M190 110 V130 M380 110 V130 M570 110 V130" stroke="var(--line)" stroke-width="3" fill="none"/>'
CH1 = '<rect x="125" y="130" width="130" height="40" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(190, 154, "⟦무대·조명|stage and lights⟧", 11, "#142033")
CH2 = '<rect x="315" y="130" width="130" height="40" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(380, 154, "⟦음향|sound⟧", 11, "#142033")
CH3 = '<rect x="505" y="130" width="130" height="40" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(570, 154, "⟦티켓·고객|tickets and guests⟧", 11, "#142033")

# 3. hero: WBS = 큰 일을 작은 할일로 쪼갠 트리형 체크리스트
P3 = svg(380, sky(380)
         + label(380, 25, "⟦WBS = 큰 일을 작은 할일로 쪼갠 트리형 체크리스트|WBS = a tree-shaped checklist that breaks a big job into small tasks⟧", 13, "var(--ink)", cls="d")
         + ROOT + LINES + CH1 + CH2 + CH3
         + person(380, 240, s=0.85, face=SMILE, **PLANNER)
         + label(380, 365, "⟦담당자와 기간까지 붙이면 진짜 계획이 돼요|add an owner and a duration to each, and it becomes a real plan⟧", 12, "var(--muted)"))

TREE_I = icon('<circle cx="32" cy="14" r="8" fill="var(--accent)"/><path d="M32 22 v8 M18 46 V30 H46 V46" stroke="var(--line)" stroke-width="3" fill="none"/><circle cx="18" cy="50" r="6" fill="var(--good)"/><circle cx="46" cy="50" r="6" fill="var(--good)"/>')
OWNER_I = icon('<circle cx="32" cy="22" r="12" fill="var(--accent)"/><path d="M14 54 q18 -22 36 0" fill="none" stroke="var(--accent)" stroke-width="4"/>')
DURATION_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
RULE_I = icon('<rect x="8" y="8" width="48" height="48" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><text x="32" y="40" text-anchor="middle" font-size="18" fill="var(--accent)" font-weight="700">100%</text>')

# 4. 분해 단계 체크리스트
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 260, "⟦분해 단계|BREAKDOWN LEVELS⟧",
                     ("⟦레벨1 — 전체 투어|level 1 — whole tour⟧",
                      "⟦레벨2 — 공연별(도시별)|level 2 — per show (per city)⟧",
                      "⟦레벨3 — 무대·음향·티켓...|level 3 — stage, sound, tickets...⟧",
                      "⟦더 작아지면 작업 패키지가 돼요|small enough, and it's a work package⟧"), 1.0)
         + person(560, 170, s=0.8, **PLANNER)
         + label(380, 300, "⟦작업 패키지마다 담당자·기간을 붙여요|each work package gets an owner and a duration⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 너무 잘게 쪼개면 오히려 관리가 힘들어져요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + checklist(50, 60, 280, 160, "⟦적당히 쪼갠 WBS|JUST RIGHT⟧", ("⟦약 20개 항목|about 20 items⟧",), 0.9)
         + label(190, 250, "⟦한눈에 관리할 수 있어요|manageable at a glance⟧", 11, "var(--ink)")
         + checklist(430, 30, 280, 220, "⟦너무 잘게 쪼갠 WBS|TOO GRANULAR⟧", ("⟦수백 개 항목...|hundreds of items...⟧", "⟦오히려 못 챙겨요|now nothing gets tracked⟧"), 0.9)
         + label(570, 270, "⟦너무 잘게 쪼개면 관리가 더 힘들어요|too fine-grained, and management gets harder⟧", 11, "var(--ink)")
         + label(380, 300, "⟦쪼개는 건 다 빠뜨리지 않으면서, 다루기 좋은 크기까지만이에요|break it down enough to miss nothing — but no further⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "wbsppm", "order": 7,
    "title": ("공연 준비를 쪼갠 체크리스트", "The Checklist That Breaks Down Show Prep"),
    "h1": ("<em>WBS(작업분류체계)</em>가 뭐예요?", "What is <em>WBS (Work Breakdown Structure)</em>?"),
    "sub": ("WBS를, 막막한 공연 준비를 작은 할 일로 쪼갠 트리형 체크리스트 이야기로 풀어봤어요.",
            "WBS, told as a story about breaking overwhelming show prep down into a tree-shaped checklist of small tasks."),
    "panels": [
        {"svg": P1, "alt": ('후원사가 투어 준비를 부탁하자 기획자가 막막해함', 'The sponsor asks for the tour to be made ready, and the planner feels lost'),
         "caption": ("공연 준비해 달란 말만 있고, 뭐부터 해야 할지 막막해요.", "Told to just get the show ready, with no idea where to start."),
         "small": ("큰 일을 통째로 보면 다 막막해 보여요.", "A big job looks overwhelming as one giant block.")},
        {"svg": P2, "alt": ("공연 준비라는 하나의 큰 상자에 모든 일이 뒤섞여 있고 기획자가 속상해함", "Everything is jumbled into one big show-prep box, and the planner is frustrated"),
         "caption": ("큰 덩어리로 보면 뭘 빠뜨렸는지도 몰라요.", "Seen as one big lump, you can't tell what's missing."),
         "small": ("작게 쪼개야 비로소 보여요.", "Only breaking it down small makes it visible.")},
        {"svg": P3, "hero": True, "alt": ("공연 준비라는 뿌리가 무대·조명, 음향, 티켓·고객 세 가지로 가지 쳐진 나무 그림과 그걸 보는 기획자", "A tree diagram where show-prep branches into stage and lights, sound, and tickets and guests, with the planner looking on"),
         "caption": ("WBS는 큰 일을 작은 할일로 쪼갠 트리형 체크리스트예요.", "WBS is a tree-shaped checklist that breaks a big job into small tasks."),
         "small": ("담당자와 기간까지 붙이면 진짜 계획이 돼요.", "Add an owner and a duration to each, and it becomes a real plan."),
         "tricks": (4, [
             (TREE_I, ("큰 덩어리 쪼개기", "Decompose the whole"), ("작은 덩어리로 나눠요", "break it into smaller pieces"), "calm"),
             (OWNER_I, ("담당자 배정하기", "Assign an owner"), ("누가 할지 정해요", "decide who owns each piece")),
             (DURATION_I, ("기간 추정하기", "Estimate duration"), ("얼마나 걸릴지 가늠해요", "estimate how long it takes"), "warm"),
             (RULE_I, ("100% 룰 지키기", "Keep the 100% rule"), ("하나도 빠짐없이 담아요", "leave nothing out")),
         ])},
        {"svg": P4, "alt": ('레벨1부터 레벨3까지 쪼개지는 분해 단계 체크리스트', 'A checklist of breakdown levels, from level 1 down to level 3'),
         "caption": ("투어 전체에서 도시별 공연, 그 안의 작업까지 쪼개요.", "From the whole tour down to each city's show, down to each task."),
         "small": ("작업 패키지마다 담당자·기간을 붙여요.", "Each work package gets an owner and a duration.")},
        {"svg": P5, "alt": ('왼쪽: 적당히 쪼갠 20개 항목 체크리스트. 오른쪽: 수백 개로 너무 잘게 쪼갠 체크리스트', 'Left: a checklist with about 20, reasonably sized items. Right: a checklist broken into hundreds of overly fine items'),
         "caption": ("너무 잘게 쪼개면 오히려 관리가 힘들어져요.", "Too fine-grained, and management gets harder instead."),
         "small": ("쪼개는 건 다 빠뜨리지 않으면서, 다루기 좋은 크기까지만이에요.", "Break it down enough to miss nothing — but no further.")},
    ],
    "summary": (("<b>WBS</b> = 막막한 공연(프로젝트) 전체를 <b>작은 할 일로 쪼갠 트리형 체크리스트</b>로, 담당자·기간을 붙여 진짜 계획으로 만드는 도구.",
                 "<b>WBS</b> = a tree-shaped checklist that breaks an overwhelming project down into small tasks — each with an owner and a duration, turning it into a real plan."),
                ("WBS(Work Breakdown Structure)는 프로젝트 범위를 산출물 또는 단계 기준으로 계층적으로 분해한 구조예요. 일정·예산 수립의 바탕이 되며, 100% 룰(상위 항목의 범위를 하위 항목들이 빠짐없이 덮어야 한다는 원칙)을 지키되 지나치게 세분화하면 관리 부담이 오히려 커져요. 이 세계에서는 일정·범위를 쪼개는 관점을 다뤄요.",
                 "WBS (Work Breakdown Structure) is a hierarchical decomposition of project scope by deliverable or phase. It underlies schedule and budget planning. The 100% rule says child items must fully cover the parent's scope — but over-decomposing adds more management burden than it saves. This world covers the schedule/scope-breakdown angle specifically.")),
    "glossary": [
        ("작업 패키지", "Work Package", ("더는 못 쪼개는 가장 작은 단위.", "The smallest unit — no further breakdown."), ("담당자와 기간을 붙이는 최소 단위예요.", "The base unit that gets an owner and a duration.")),
        ("100% 룰", "100% Rule", ("상위 항목을 하위 항목들이 빠짐없이 덮는 원칙.", "The rule that child items must fully cover the parent."), ("빠뜨리는 일을 막아줘요.", "Prevents anything from slipping through.")),
        ("분해 레벨", "Decomposition Level", ("전체→공연별→작업으로 내려가는 단계.", "The levels from whole tour down to each task."), ("보통 3~4단계면 충분해요.", "Three to four levels is usually enough.")),
        ("일정관리", "Schedule Management", ("작업 패키지에 기간을 붙이는 일.", "Attaching a duration to each work package."), ("WBS가 바탕이 되는 다음 단계예요.", "The next step built on top of the WBS.")),
        ("프로젝트 위험관리", "Project Risk Mgmt", ("우산처럼 돌발 상황에 대비하는 일.", "Preparing for surprises, like carrying an umbrella."), ('위험은 WBS의 각 항목 안에 숨어 있어요. → <a href="projrisk-ko.html">비 오는 날에도 챙기는 우산</a>', 'Risk hides inside each WBS item. → <a href="projrisk-en.html">the umbrella you carry even on a dry day</a>')),
        ("협상·계약", "Negotiation & Contract", ("출연 계약서로 조건을 조율하는 일.", "Tuning terms through the performance contract."), ('계약 범위를 가늠할 때 WBS를 참고해요. → <a href="negotiation-ko.html">조건을 조율해 서명하기</a>', 'WBS helps gauge scope before the contract. → <a href="negotiation-en.html">tuning terms until both sign</a>')),
        ("감리/PMO", "IS Audit/PMO", ("전체를 바깥에서 점검하는 역할.", "A role that checks everything from the outside."), ('감리는 WBS대로 진행됐는지도 점검해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Audit also checks whether work followed the WBS. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("기능점수(FP)", "Function Point", ("규모를 재는 또 다른 자.", "Another ruler for measuring size."), ('WBS가 할 일을 쪼갠다면, FP는 크기를 재요. → <a href="fpruler-ko.html">매수를 재는 자</a>', 'If WBS breaks down the work, FP measures its size. → <a href="fpruler-en.html">the ruler that measures page count</a>')),
    ],
}
