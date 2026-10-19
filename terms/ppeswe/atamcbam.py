from _draw import *
from _world import *

# 1. 인쇄 직전, 다들 불안함
P1 = svg(300, sky(300)
         + printplate(380, 150, 1.1)
         + person(220, 150, s=0.75, face=EYES, **EDITOR) + person(540, 150, s=0.75, face=SWEAT, **PRINTER)
         + label(380, 60, "⟦이 장정 그대로 인쇄 들어가도 될까요?|is it really safe to print with this binding as-is?⟧", 13, "var(--ink)")
         + label(380, 260, "⟦전체 구성이 다 정해진 뒤, 인쇄 직전의 불안함이에요|the whole layout is locked in, and now everyone's nervous right before the press runs⟧", 12, "var(--muted)"))

# 2. 인쇄 다 되고 나서야 문제를 앎
P2 = svg(330, '<rect width="760" height="330" fill="var(--bad-soft)"/>'
         + printplate(380, 140, 1.2)
         + person(380, 200, s=0.7, face=FROWN + SWEAT, **PRINTER)
         + bubble(260, 30, 280, 44, "⟦이 장정으론 전자책 전환이 안 돼요!|this binding can't convert to an e-book at all!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦이미 다 찍은 뒤라 너무 늦었어요|it's already all printed — far too late⟧", 12, "var(--ink)", cls="d"))

# 3. 인쇄 전, 시나리오로 미리 리허설 (hero)
P3 = svg(340, sky(340)
         + person(230, 100, s=0.85, face=EYES, **EDITOR) + person(400, 100, s=0.85, face=EYES, **WRITER) + person(560, 100, s=0.85, face=EYES, **PRINTER)
         + styleguide(140, 225, 480, 90, "⟦시나리오: 내구성? 전자책 전환? 인쇄 속도?|SCENARIOS: durability? e-book conversion? print speed?⟧", (), 0.9)
         + label(380, 30, "⟦ATAM = 인쇄 전에 여러 시나리오로 트레이드오프를 미리 찾는 리허설|ATAM = rehearsing trade-offs against many scenarios, before the press ever runs⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦이해관계자들이 다 같이 모여, 설계 결정의 민감점을 찾아요|stakeholders gather together to find the sensitive points in a design decision⟧", 11, "var(--muted)"))

SCEN_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
MAP_I = icon('<circle cx="24" cy="24" r="10" fill="var(--accent)"/><circle cx="44" cy="40" r="10" fill="var(--good)"/><path d="M30 30 L38 34" stroke="var(--ink)" stroke-width="3"/>')
SENSE_I = icon('<path d="M32 10 v44" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="none" stroke="var(--bad)" stroke-width="4"/>')
RISK_I = icon('<rect x="18" y="8" width="4" height="48" fill="#5A3B22"/><path d="M22 10 h26 l-8 10 l8 10 h-26 z" fill="var(--bad)"/>')

PAGE = {
    "slug": "atamcbam", "order": 41,
    "title": ("출간 전 시나리오 리허설", "Scenario Rehearsal Before Publication"),
    "h1": ("<em>아키텍처 평가(ATAM/CBAM)</em>가 뭐예요?", "What are <em>ATAM and CBAM</em>?"),
    "sub": ("전체 구성을 다 정한 뒤 인쇄 들어가기 직전, 여러 상황을 미리 리허설해 트레이드오프를 찾는 이야기예요.",
            "A story about rehearsing several scenarios right before the press runs, to surface trade-offs while there's still time."),
    "panels": [
        {"svg": P1, "alt": ("인쇄판 앞에서 편집장과 인쇄 감독이 이 장정 그대로 가도 되는지 불안해함", "In front of the printing plate, the editor and print supervisor look nervous about whether to go with this binding"),
         "caption": ("인쇄 직전, 다들 이대로 괜찮은지 불안해해요.", "Right before the press runs, everyone's nervous about whether this is okay."),
         "small": ("전체 구성이 다 정해진 뒤의 불안함이에요.", "The whole layout is already locked in — and now the nerves set in.")},
        {"svg": P2, "alt": ("인쇄가 다 끝난 뒤에야 이 장정으로는 전자책 전환이 안 된다는 걸 알게 됨", "Only after printing is done does everyone realize this binding can't be converted to an e-book"),
         "caption": ("인쇄 다 되고 나서야 문제를 알게 돼요.", "The problem only surfaces after everything is printed."),
         "small": ("이미 다 찍은 뒤라 너무 늦었어요.", "It's already all printed — far too late to fix.")},
        {"svg": P3, "hero": True, "alt": ("편집장, 작가, 인쇄 감독이 모여 내구성·전자책 전환·인쇄 속도 같은 시나리오를 미리 점검함", "The editor, author, and print supervisor gather to check scenarios like durability, e-book conversion, and print speed ahead of time"),
         "caption": ("ATAM = 인쇄 전에 여러 시나리오로 트레이드오프를 미리 찾는 리허설이에요.", "ATAM = rehearsing trade-offs against many scenarios before the press ever runs."),
         "small": ("이해관계자들이 다 같이 모여, 설계 결정의 민감점을 찾아요.", "Stakeholders gather together to find the sensitive points in a design decision."),
         "tricks": (4, [
             (SCEN_I, ("품질 시나리오 모으기", "Gather quality scenarios"), ("내구성, 전환성, 속도 등", "durability, convertibility, speed, and more"), "calm"),
             (MAP_I, ("설계 결정과 매핑", "Map to design decisions"), ("어떤 선택이 뭘 책임지는지", "which choice is responsible for what")),
             (SENSE_I, ("민감점/트레이드오프 찾기", "Find sensitivity and trade-off points"), ("하나를 얻으면 뭘 잃는지", "what you lose to gain the other"), "warm"),
             (RISK_I, ("위험 미리 기록", "Record the risks early"), ("인쇄 전에 적어 둬요", "write them down before the press runs")),
         ])},
        {"svg": svg(320, sky(320)
                     + styleguide(60, 40, 300, 240, "⟦옵션 A: 저렴한 제본|OPTION A: cheap binding⟧",
                                  ("⟦비용 — 낮음|cost — low⟧", "⟦전자책 전환 — 어려움|e-book conversion — hard⟧", "⟦인쇄 속도 — 빠름|print speed — fast⟧"), 1.0)
                     + styleguide(420, 40, 280, 240, "⟦옵션 B: 유연한 제본|OPTION B: flexible binding⟧",
                                  ("⟦비용 — 높음|cost — high⟧", "⟦전자책 전환 — 쉬움|e-book conversion — easy⟧", "⟦인쇄 속도 — 느림|print speed — slow⟧"), 1.0, hl=1)
                     + label(380, 300, "⟦CBAM = 여기에 비용과 이득을 숫자로 더해 저울질하는 단계|CBAM = the step that adds cost and benefit numbers to weigh these options⟧", 12, "var(--ink)")),
         "alt": ("저렴한 제본(옵션 A)과 유연한 제본(옵션 B)의 비용·전환성·속도를 숫자로 비교", "Comparing a cheap binding (Option A) and a flexible binding (Option B) by cost, convertibility, and speed"),
         "caption": ("여기에 비용과 이득까지 숫자로 따지면 CBAM이에요.", "Add cost and benefit numbers to this, and it becomes CBAM."),
         "small": ("어느 쪽이 \'더 남는 장사\'인지 숫자로 비교해요.", "It compares, in numbers, which option actually pays off more.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
                     + person(190, 150, s=0.8, face=EYES, **PRINTER) + label(190, 240, "⟦눈을 뜨게 해줘요|it opens everyone's eyes⟧", 11, "var(--ink)")
                     + person(570, 150, s=0.8, face=EYES, **EDITOR) + label(570, 240, "⟦결정은 결국 편집장 몫이에요|the final call is still the editor's⟧", 11, "var(--ink)")
                     + label(380, 282, "⟦평가는 선택을 대신 안 해줘요, 무엇을 놓고 고민해야 할지 보여줄 뿐이에요|evaluation doesn't choose for you — it just shows what's worth weighing⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 평가가 눈을 뜨게 해줌. 오른쪽: 최종 결정은 여전히 편집장의 몫", "Left: the evaluation opens everyone's eyes. Right: the final decision is still the editor's to make"),
         "caption": ("평가가 결정을 대신 해주진 않아요.", "Evaluation doesn't make the decision for you."),
         "small": ("무엇을 놓고 고민해야 할지 보여줄 뿐, 선택은 여전히 사람 몫이에요.", "It only shows what's worth weighing — the choice is still a human's to make.")},
    ],
    "summary": (("<b>ATAM</b>은 인쇄(개발) 전에 <b>품질 시나리오</b>로 설계의 트레이드오프와 위험을 미리 찾는 평가법이고, <b>CBAM</b>은 그 선택지마다 <b>비용과 이득</b>을 숫자로 더해 저울질하는 확장판이에요.",
                 "<b>ATAM</b> evaluates a design by rehearsing <b>quality scenarios</b> before the press runs, surfacing trade-offs and risks; <b>CBAM</b> extends this by adding <b>cost and benefit</b> numbers to weigh each option."),
                ("ATAM(Architecture Tradeoff Analysis Method)은 이해관계자들이 모여 성능·보안·이식성 같은 품질속성 시나리오를 만들고, 각 시나리오가 아키텍처 설계 결정과 어떻게 연결되는지 매핑해 민감점(sensitivity point)과 트레이드오프점을 찾는 평가 방법이에요. CBAM(Cost Benefit Analysis Method)은 여기에 각 설계 결정의 비용과 효용(이득)을 경제적으로 분석하는 단계를 더해, 우선순위를 정량적으로 정하도록 돕는 확장 방법이에요.",
                 "ATAM (Architecture Tradeoff Analysis Method) gathers stakeholders to write quality-attribute scenarios — performance, security, portability, and so on — then maps each scenario to the architecture's design decisions to find sensitivity points and trade-off points. CBAM (Cost Benefit Analysis Method) extends this by adding an economic analysis of each design decision's cost and benefit, helping prioritize decisions quantitatively.")),
    "glossary": [
        ("ATAM", "ATAM", ("인쇄 전 시나리오 리허설.", "The scenario rehearsal before the press runs."), ("트레이드오프와 민감점을 찾아요.", "Finds trade-offs and sensitivity points.")),
        ("CBAM", "CBAM", ("ATAM에 비용·이득 계산을 더한 확장판.", "ATAM with cost-benefit numbers added on top."), ("우선순위를 숫자로 매겨요.", "Prioritizes options with numbers.")),
        ("품질속성 시나리오", "Quality Attribute Scenario", ("\"내구성이 이만큼 필요하다\" 같은 구체적 상황.", "A concrete situation like \"it needs this much durability.\""), ("평가의 출발점이에요.", "The starting point of the evaluation.")),
        ("민감점(Sensitivity Point)", "Sensitivity Point", ("한 결정이 품질에 크게 영향을 주는 지점.", "A spot where one decision swings quality a lot."), ("ATAM이 특히 주목하는 지점이에요.", "A spot ATAM pays special attention to.")),
        ("트레이드오프점", "Trade-off Point", ("하나를 얻으면 다른 걸 잃는 지점.", "A spot where gaining one thing costs another."), ("민감점이 여러 품질에 걸쳐 있으면 트레이드오프점이 돼요.", "A sensitivity point affecting multiple qualities becomes a trade-off point.")),
        ("이해관계자", "Stakeholder", ("편집장, 작가, 인쇄 감독처럼 평가에 모이는 사람들.", "People like the editor, author, and print supervisor who gather for the evaluation."), ("ATAM은 이들을 한자리에 모아요.", "ATAM brings them all into one room.")),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("감리는 사후·전체 점검, ATAM은 설계 시점 평가.", "Audit checks after the fact and broadly; ATAM evaluates at design time."), ('둘은 보는 시점이 달라요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'They look at different moments. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("좋은 소프트웨어의 조건", "Conditions of Good Software", ("ATAM이 저울질하는 바로 그 품질 조건들.", "The very quality conditions ATAM weighs against each other."), ('시나리오는 결국 이 조건들에서 나와요. → <a href="goodsw-ko.html">좋은 책의 조건</a>', 'Scenarios ultimately come from these conditions. → <a href="goodsw-en.html">what makes a good book</a>')),
    ],
}
