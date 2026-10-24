from _draw import *
from _world import *

# 1. 후원사가 "공연 품질, 보장해줘요"라고 말로만 요구해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(180, 150, s=0.8, face=EYES, **SPONSOR)
         + bubble(40, 60, 260, 50, "⟦공연 품질, 보장해줘요!|guarantee me the show's quality!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **DIRECTOR)
         + bubble(440, 60, 260, 50, "⟦네... 최선을 다할게요?|sure... I'll do my best?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦말로만 한 약속은 나중에 서로 다르게 기억해요|a promise only spoken gets remembered differently by each side later⟧", 12, "var(--ink)", cls="d"))

# 2. 왜: 말로 약속하면 분쟁이 생겨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **SPONSOR)
         + bubble(50, 60, 250, 50, "⟦소리가 끊겼잖아요! 약속 어겼어요|the sound cut out! you broke your promise⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=FROWN, **DIRECTOR)
         + bubble(440, 60, 260, 50, "⟦그런 얘긴 못 들었는데요|I never heard that part of the deal⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦숫자와 문서로 적어두지 않으면 다툼이 생겨요|without numbers and paper, disputes follow⟧", 12, "var(--ink)", cls="d"))

# 3. hero: SLA = 티켓에 적힌 보장 내용, SLM = 그 약속을 꾸준히 관리하는 일
P3 = svg(350, sky(350)
         + ticket(290, 150, 1.4, text="⟦음향 끊김 0.1% 이하|sound dropout under 0.1%⟧")
         + person(170, 230, s=0.85, face=SMILE, **DIRECTOR)
         + person(560, 230, s=0.8, face=SMILE, **SPONSOR)
         + label(380, 30, "⟦SLA = 티켓에 적힌 보장 내용, SLM = 그 약속을 꾸준히 관리하는 일|SLA = the guarantee written on the ticket, SLM = keeping that promise managed over time⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦약속을 적고, 재고, 지켰는지 계속 확인해요|write the promise, measure it, keep checking it held⟧", 12, "var(--muted)"))

DEF_I = icon('<rect x="12" y="14" width="40" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 26 h24 M20 34 h24 M20 42 h14" stroke="#142033" stroke-width="2.5"/>')
KPI_I = icon('<path d="M12 50 L26 30 L38 40 L52 14" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="52" cy="14" r="4" fill="var(--accent)"/>')
PEN_I = icon('<path d="M18 10 L46 10 L46 54 L18 54 Z" fill="none" stroke="var(--bad)" stroke-width="3"/><text x="32" y="38" text-anchor="middle" font-size="22" fill="var(--bad)" font-weight="700">%</text>')
REVIEW_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 7 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. SLA 조항 vs 내부 목표 vs 기술적 신뢰성 비교
P4 = svg(320, sky(320, ground=False)
         + checklist(50, 30, 300, 260, "⟦티켓(SLA) 조항|TICKET (SLA) TERMS⟧",
                     ("⟦보장 수준 — 음향 끊김 0.1% 이하|target — sound dropout under 0.1%⟧",
                      "⟦측정 지표 — 공연마다 로그 확인|metric — logged every show⟧",
                      "⟦위반 시 — 환불 10%|if missed — 10% refund⟧",
                      "⟦정기 리뷰 — 분기마다 재점검|review — re-checked quarterly⟧"), 1.0)
         + ticket(560, 150, 1.0, text="⟦기술적 신뢰성|technical uptime⟧")
         + label(560, 220, "⟦그 수치를 실제로 만드는 쪽은 따로 있어요|a different world makes that number real⟧", 11, "var(--muted)")
         + label(380, 300, "⟦SLM은 이 조항을 계속 관리하는 과정이에요|SLM is the ongoing process of managing these terms⟧", 12, "var(--ink)", cls="d"))

# 5. 한계/차이: 이 티켓은 계약, 실제로 지켜내는 기술은 다른 세계
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ticket(190, 150, 1.0, text="⟦계약 조건|contract terms⟧") + label(190, 240, "⟦이 세계는 약속을 적고 관리해요|this world writes and manages the promise⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **ARTIST) + label(570, 250, "⟦약속을 실제로 지키는 기술은 또 다른 얘기예요|actually keeping it is a different story⟧", 11, "var(--ink)")
         + label(380, 282, "⟦계약(SLA/SLM)과 기술적 신뢰성은 다른 각도예요|the contract (SLA/SLM) and technical reliability are different angles⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "slappe", "order": 3,
    "title": ("공연을 보장하는 티켓", "The Ticket That Guarantees the Show"),
    "h1": ("<em>SLA/SLM</em>이 뭐예요?", "What is <em>SLA/SLM</em>?"),
    "sub": ("SLA(서비스 수준 계약)와 SLM(서비스 수준 관리)을, 후원사와 맺은 공연 보장 티켓과 그걸 관리하는 일로 풀어봤어요.",
            "SLA and SLM, told as a story about a ticket that guarantees the show to a sponsor, and managing that promise over time."),
    "panels": [
        {"svg": P1, "alt": ('후원사가 말로 품질 보장을 요구하고 감독관은 진땀 흘리며 얼버무림', 'The sponsor demands a verbal quality guarantee, and the director stalls, sweating'),
         "caption": ("후원사가 \"공연 품질, 보장해줘요\"라고 말로만 요구해요.", "The sponsor demands quality, guaranteed, but only in words."),
         "small": ("말로만 한 약속은 나중에 서로 다르게 기억해요.", "A promise only spoken gets remembered differently by each side later.")},
        {"svg": P2, "alt": ('음향 사고 후 후원사와 감독관이 서로 다른 기억으로 다툼', 'After a sound glitch, the sponsor and director argue over conflicting memories of the deal'),
         "caption": ("말로 약속하면 분쟁이 생겨요.", "A spoken promise leads to disputes."),
         "small": ("숫자와 문서로 적어두지 않으면 다툼이 생겨요.", "Without numbers and paper, disputes follow.")},
        {"svg": P3, "hero": True, "alt": ('감독관과 후원사 사이에 보장 조건이 적힌 큰 티켓이 놓임', 'A large ticket spelling out the guarantee terms sits between the director and the sponsor'),
         "caption": ("SLA는 티켓에 적힌 보장 내용, SLM은 그 약속을 꾸준히 관리하는 일이에요.", "SLA is the guarantee written on the ticket; SLM is keeping that promise managed over time."),
         "small": ("약속을 적고, 재고, 지켰는지 계속 확인해요.", "Write the promise, measure it, keep checking it held."),
         "tricks": (4, [
             (DEF_I, ("서비스 수준 정의하기", "Define the service level"), ("무엇을, 얼마나 보장할지 적어요", "write what's guaranteed, and how much"), "calm"),
             (KPI_I, ("측정 지표 두기", "Set measurable metrics"), ("재볼 수 있는 숫자로요", "as numbers you can actually measure")),
             (PEN_I, ("위반 시 조치 정하기", "Define the penalty"), ("못 지키면 뭘 해줄지도 적어요", "spell out what happens if it's missed"), "warm"),
             (REVIEW_I, ("정기적으로 리뷰하기", "Review it regularly"), ("한 번 쓰고 끝이 아니에요", "not written once and forgotten")),
         ])},
        {"svg": P4, "alt": ('티켓 조항 체크리스트와, 그 수치를 실제로 만드는 또 다른 티켓', 'A checklist of ticket terms, next to another ticket for the number that actually gets delivered'),
         "caption": ("티켓엔 보장 수준·측정·위반 조치·리뷰 주기가 적혀요.", "The ticket spells out the target, metric, penalty, and review cycle."),
         "small": ("SLM은 이 조항을 계속 관리하는 과정이에요.", "SLM is the ongoing process of managing these terms.")},
        {"svg": P5, "alt": ('왼쪽: 계약 조건을 적은 티켓. 오른쪽: 실제로 기술을 지켜내는 출연자', 'Left: a ticket with the contract terms written on it. Right: the performer who actually keeps the technical promise'),
         "caption": ("이 티켓은 계약이고, 실제로 지켜내는 기술은 다른 얘기예요.", "This ticket is a contract — actually keeping it is a different story."),
         "small": ("계약(SLA/SLM)과 기술적 신뢰성은 다른 각도예요.", "The contract (SLA/SLM) and technical reliability are different angles.")},
    ],
    "summary": (("<b>SLA</b> = 후원사와 <b>문서로 적어 맺은</b> 공연 보장 티켓, <b>SLM</b> = 그 티켓 내용을 <b>계속 측정하고 관리하는</b> 일.",
                 "<b>SLA</b> = a show-guarantee ticket written and agreed with the sponsor, in document form; <b>SLM</b> = continuously measuring and managing what's written on it."),
                ("SLA(Service Level Agreement)는 공급자와 고객 사이에 서비스 수준·측정 지표·위반 시 조치를 문서로 합의한 계약이고, SLM(Service Level Management)은 그 합의를 정기적으로 측정·보고·개선하는 관리 프로세스예요. 이 세계에서는 계약·거버넌스 관점을 다루며, 기술적으로 가동률을 실제 어떻게 지켜내는지는 sre 세계의 SLA/SLO를 참고하세요.",
                 "SLA (Service Level Agreement) is a documented agreement between provider and customer on service levels, metrics, and remedies for breach. SLM (Service Level Management) is the process of regularly measuring, reporting, and improving against that agreement. This world covers the contract/governance angle — for how uptime is technically achieved, see SLA/SLO in the sre world.")),
    "glossary": [
        ("SLA", "SLA", ("후원사와 맺은 보장 티켓.", "The guarantee ticket agreed with the sponsor."), ("보장 수준·위반 시 조치가 적혀요.", "Spells out the target and the remedy if missed.")),
        ("SLM", "SLM", ("티켓 내용을 계속 관리하는 일.", "Managing what's written on the ticket, continuously."), ("측정·보고·개선을 반복해요.", "Measure, report, improve — on repeat.")),
        ("KPI/지표", "KPI/Metric", ("재볼 수 있는 숫자로 적은 기준.", "The standard, written as a number you can measure."), ("기준이 모호하면 분쟁이 나요.", "A vague standard invites disputes.")),
        ("위약금/패널티", "Penalty", ("약속을 못 지켰을 때의 조치.", "What happens if the promise is broken."), ("환불이나 보상으로 적어둬요.", "Written in as a refund or compensation.")),
        ("정기 리뷰", "Periodic Review", ("분기마다 티켓 내용을 다시 점검하는 일.", "Re-checking the ticket's terms every quarter."), ("상황이 바뀌면 조항도 바뀌어요.", "Terms change as circumstances change.")),
        ("기술적 SLA/SLO", "Technical SLA/SLO", ("실제로 가동률을 지켜내는 기술 목표.", "The technical target that actually keeps uptime up."), ('신뢰성 공학 관점은 다른 세계에서 다뤄요. → <a href="sla-ko.html">기술적 신뢰성 SLA</a>', 'The reliability-engineering angle lives in another world. → <a href="sla-en.html">the technical-reliability SLA</a>')),
        ("협상·계약", "Negotiation & Contract", ("출연 계약서로 조건을 조율하는 일.", "Tuning terms through the performance contract."), ('SLA 조항도 이 협상 과정에서 정해져요. → <a href="negotiation-ko.html">조건을 조율해 서명하기</a>', 'SLA terms get set during this same negotiation. → <a href="negotiation-en.html">tuning terms until both sign</a>')),
        ("감리/PMO", "IS Audit/PMO", ("전체를 바깥에서 점검하는 역할.", "A role that checks everything from the outside."), ('감리는 SLA 준수 여부도 점검해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Audit also checks whether the SLA was kept. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
