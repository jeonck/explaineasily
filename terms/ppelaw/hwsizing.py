"""정보시스템 하드웨어 규모산정 지침."""
from _draw import *
from _world import *

DATA_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
PEAK_I = icon('<path d="M8 50 L22 26 L34 38 L48 14" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="48" cy="14" r="5" fill="var(--bad)"/>')
MARGIN_I = icon('<rect x="14" y="30" width="36" height="20" rx="3" fill="var(--good)"/><rect x="14" y="14" width="36" height="12" rx="3" fill="var(--good)" opacity="0.4"/>')
REDO_I = icon('<path d="M46 20 a18 18 0 1 1 -8 -10" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M46 8 v12 h-12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 축제 음식 몇 인분 만들지 몰라요
P1 = svg(300, sky(300)
         + person(200, 150, s=0.85, face=EYES, **REP) + bubble(110, 70, 220, 44, "⟦떡볶이를 몇 인분 만들어야 하죠?|how many servings of tteokbokki should we make?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=FROWN, **STUDENT) + bubble(470, 70, 220, 44, "⟦작년엔 300인분이었는데…|last year it was 300 servings…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦감으로 정하면 모자라거나 남아요|guessing means too little or too much⟧", 13, "var(--ink)", cls="d"))

# 2. 그냥 많이/작년처럼 정하면 안 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT + EYES, **STUDENT) + label(220, 250, "⟦너무 많이 만들어서 다 버렸어요|made way too much and had to toss it⟧", 11, "var(--bad)")
         + person(560, 150, s=0.8, face=FROWN, **REP) + label(560, 250, "⟦전학생이 늘어난 걸 깜빡했어요|forgot more students transferred in⟧", 11, "var(--bad)")
         + label(380, 280, "⟦예산도 인원도 바뀌는데 계산 없이 정하면 틀려요|budget and headcount both change — guessing without a formula gets it wrong⟧", 12, "var(--ink)", cls="d"))

# 3. 규모산정 지침 = 미리 계산하는 공식표 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦규모산정 지침 = 예상 인원과 사용량으로 미리 계산하는 공식표|a sizing guideline = a formula sheet that calculates ahead from expected headcount and usage⟧", 13, "var(--ink)", cls="d")
         + person(170, 120, s=0.9, face=EYES, **PRESIDENT)
         + rulesboard(260, 70, 300, 220, "⟦규모산정 공식표|SIZING FORMULA⟧",
                      ("⟦예상 참여 인원|expected headcount⟧", "⟦최대 동시 접속(피크)|peak concurrent use⟧", "⟦여유율 더하기|add a safety margin⟧", "⟦내년 증가율 반영|factor next year's growth⟧"), 0.95)
         + person(640, 160, s=0.8, face=SMILE, **REP)
         + label(380, 320, "⟦감이 아니라 숫자로 미리 정해요|decided by numbers in advance, not by gut feel⟧", 12, "var(--muted)"))

# 4. 공식 적용 예
P4 = svg(300, sky(300, ground=False)
         + rulesboard(60, 40, 640, 220, "⟦예시: 학생 1,200명 축제|EXAMPLE: A 1,200-STUDENT FESTIVAL⟧",
                      ("⟦예상 참여 인원  1,200명|expected headcount: 1,200⟧",
                       "⟦참여율(피크)  × 60%  = 720명|peak participation × 60% = 720⟧",
                       "⟦여유율  × 1.3  = 약 936인분|safety margin × 1.3 ≈ 936 servings⟧",
                       "⟦내년 증가율  × 1.1  = 약 1,030인분 준비|next-year growth × 1.1 ≈ prepare 1,030 servings⟧"), 1.0, hl=2)
         + label(380, 285, "⟦공식 하나로 누가 계산해도 같은 결과가 나와요|the same formula gives anyone the same answer⟧", 12, "var(--ink)", cls="d"))

# 5. 공식대로 해도 갑자기 바뀔 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 140, s=0.8, face=SMILE, **PRESIDENT) + rulesboard(100, 180, 180, 60, "", ("⟦936인분 준비 완료|936 servings ready⟧",), 0.8)
         + person(570, 130, s=0.85, face=SWEAT + EYES, **STUDENT) + label(570, 240, "⟦갑자기 옆 학교도 놀러 왔어요!|a neighboring school showed up too!⟧", 11, "var(--ink)")
         + label(380, 280, "⟦공식은 출발점이에요 — 계속 지켜보고 다시 재야 해요|the formula is a starting point — you still have to watch and re-measure⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "hwsizing", "order": 2,
    "title": ("축제 준비물 개수 미리 정하기", "Sizing the Festival Supplies in Advance"),
    "h1": ("<em>정보시스템 하드웨어 규모산정</em>이 뭐예요?", "What is <em>IS Hardware Sizing</em>?"),
    "sub": ("정보시스템 하드웨어 규모산정 지침을, 학생회가 축제 음식 양을 미리 공식으로 계산하는 이야기로 풀어봤어요.",
            "The IS hardware sizing guideline, told as a story about the student council calculating festival food quantities with a formula ahead of time."),
    "panels": [
        {"svg": P1, "alt": ("대표가 떡볶이를 몇 인분 만들지 몰라 고민하고, 작년 수치만 떠올림", "A rep worries about how many servings to make, only recalling last year's number"),
         "caption": ("축제 음식을 몇 인분 만들어야 할지 몰라요.", "Nobody knows how many festival servings to make."),
         "small": ("감으로 정하면 모자라거나 남아요.", "Guessing means either too little or too much.")},
        {"svg": P2, "alt": ("왼쪽: 너무 많이 만들어 버림. 오른쪽: 전학생 증가를 반영 못 함", "Left: too much made and wasted. Right: failed to account for new transfer students"),
         "caption": ("그냥 많이, 혹은 작년처럼 정하면 틀려요.", "Just guessing high, or copying last year, gets it wrong."),
         "small": ("예산도 인원도 바뀌는데 계산 없이 정하면 틀려요.", "Budget and headcount both change — guessing without a formula gets it wrong.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 규모산정 공식표를 들고 인원·피크·여유율·증가율을 계산함", "The council president holds a sizing formula sheet covering headcount, peak, margin, and growth"),
         "caption": ("규모산정 지침은 미리 계산하는 공식표예요.", "The sizing guideline is a formula sheet calculated in advance."),
         "small": ("감이 아니라 숫자로 미리 정해요.", "Decided by numbers in advance, not by gut feel."),
         "tricks": (4, [
             (DATA_I, ("기존 자료 모으기", "Gather past data"), ("지난 사용량부터 봐요", "start from past usage"), "calm"),
             (PEAK_I, ("가장 바쁠 때 보기", "Look at the busiest moment"), ("평균이 아니라 피크로", "peak, not average"), "warm"),
             (MARGIN_I, ("여유율 더하기", "Add a safety margin"), ("딱 맞추지 않아요", "never cut it exactly"), ),
             (REDO_I, ("주기적으로 다시 재기", "Re-measure periodically"), ("한 번으로 끝내지 않아요", "it's never a one-time job")),
         ])},
        {"svg": P4, "alt": ("학생 1,200명 기준 참여율·여유율·증가율을 순서대로 곱해 최종 준비량을 구하는 공식표", "A formula sheet multiplying participation rate, safety margin, and growth rate for 1,200 students to get a final quantity"),
         "caption": ("공식을 실제로 적용하면 이렇게 돼요.", "Applying the formula looks like this."),
         "small": ("공식 하나로 누가 계산해도 같은 결과가 나와요.", "The same formula gives anyone the same answer.")},
        {"svg": P5, "alt": ("왼쪽: 공식대로 936인분을 준비해 웃는 학생회장. 오른쪽: 옆 학교까지 몰려와 땀을 흘리는 학생", "Left: the president smiles, having prepared 936 servings by the formula. Right: a student sweats as a neighboring school shows up too"),
         "caption": ("공식대로 해도 갑자기 바뀔 수 있어요.", "Even by the formula, things can suddenly change."),
         "small": ("공식은 출발점이에요 — 계속 지켜보고 다시 재야 해요.", "The formula is a starting point — you still have to watch and re-measure.")},
    ],
    "summary": (("<b>하드웨어 규모산정</b> = 예상 인원과 사용량에 <b>피크·여유율·증가율</b>을 곱해 미리 계산하는 <b>공식표</b>.",
                 "<b>Hardware sizing</b> = a <b>formula sheet</b> that multiplies expected headcount and usage by <b>peak load, safety margin, and growth rate</b>, calculated in advance."),
                ("정보시스템 하드웨어 규모산정 지침은 예상 사용자 수·처리량(TPS)·데이터 증가율 등을 바탕으로 서버·스토리지 용량을 공식으로 산출하는 행정 지침이에요. 평균이 아닌 피크 부하를 기준으로 하고, 안전 여유율과 향후 증설 계획까지 반영해요.",
                 "The IS hardware sizing guideline is an administrative standard that calculates server and storage capacity with formulas based on expected users, transaction throughput (TPS), and data growth rate. It sizes for peak load rather than average, and builds in a safety margin plus future expansion.")),
    "glossary": [
        ("규모산정", "Capacity Sizing", ("필요한 양을 공식으로 미리 재는 것.", "Measuring the needed amount in advance with a formula."), ("감이 아니라 숫자로 근거를 남겨요.", "Leaves a numeric basis, not just a guess.")),
        ("TPS", "TPS (Transactions Per Second)", ("초당 처리할 수 있는 주문 수.", "Orders handled per second."), ("서버 성능을 재는 기본 단위예요.", "The basic unit for measuring server performance.")),
        ("피크 부하", "Peak Load", ("가장 붐비는 순간의 양.", "The amount at the busiest moment."), ("평균으로 재면 가장 바쁠 때 모자라요.", "Sizing by average falls short at the busiest moment.")),
        ("여유율", "Safety Margin", ("딱 맞추지 않고 더 얹는 비율.", "The extra percentage added instead of cutting it exact."), ("갑자기 늘어도 버틸 수 있게 해줘요.", "Lets the system hold up even if demand suddenly rises.")),
        ("증가율 반영", "Growth Projection", ("내년에 더 늘어날 걸 미리 넣는 것.", "Building in next year's expected increase."), ("한 번 사면 몇 년은 써야 하니까요.", "Because what's bought has to last several years.")),
        ("가용성", "Availability", ("쉬지 않고 돌아가야 하는 정도.", "How much it must keep running without stopping."), ('규모산정과 함께 고려하는 다른 세계의 개념이에요. → <a href="sla-ko.html">공연 보장 티켓</a>', 'Another world covers this alongside sizing. → <a href="sla-en.html">the ticket that guarantees the show</a>')),
        ("용량 계획", "Capacity Planning", ("앞으로 얼마나 더 필요할지 계획하는 것.", "Planning how much more will be needed ahead of time."), ('비슷한 계획이 다른 세계에도 있어요. → <a href="capacityplanning-ko.html">미리 자리 늘리는 계획</a>', 'A similar plan exists in another world too. → <a href="capacityplanning-en.html">planning more seats ahead of time</a>')),
        ("벤치마크 테스트", "Benchmark Test", ("실제로 몇 인분까지 버티는지 시험해보는 것.", "Testing how much it can actually handle."), ("공식만 믿지 않고 직접 시험해서 확인해요.", "Not trusting the formula alone — testing it for real.")),
    ],
}
