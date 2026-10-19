from _draw import *
from _world import *

# 1. 출연 신청서가 세 장이나 왔는데, 뭘 골라야 할지 모르겠어요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + contract(160, 100, 0.7) + contract(300, 90, 0.7) + contract(440, 100, 0.7)
         + person(600, 190, s=0.85, face=SWEAT + EYES, **PLANNER)
         + label(380, 250, "⟦출연 신청서가 세 장이나 왔는데, 뭘 골라야 할지 모르겠어요|three audition proposals came in, and it's unclear which to pick⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦기획자 혼자서는 다 비교하기 벅차요|one planner alone can't compare them all⟧", 12, "var(--muted)"))

# 2. 왜: 제일 싼 팀으로 바로 고르면 안 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **PLANNER)
         + bubble(70, 70, 230, 46, "⟦제일 싼 팀으로 할까요?|should we just go with the cheapest?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=FROWN, **DIRECTOR)
         + bubble(450, 70, 230, 46, "⟦싸다고 다 좋은 건 아니에요|cheap doesn't mean good⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦가격만 보고 고르면 나중에 품질 문제가 생겨요|choosing on price alone causes quality problems later⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 점수표로 비교하고, 조건을 조율해 계약서에 서명해요
P3 = svg(350, sky(350)
         + contract(290, 150, 1.4, signed=True)
         + person(170, 230, s=0.85, face=SMILE, **PLANNER)
         + person(560, 230, s=0.8, face=SMILE, **ARTIST)
         + label(380, 30, "⟦제안서 평가·협상 = 점수표로 비교하고, 조건을 조율해 계약서에 서명하는 일|proposal evaluation and negotiation = comparing with a scorecard, then tuning terms until both sign⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦가격만 보지 않고, 조율할 여지를 남겨둬요|not just price — leaving room to tune the terms⟧", 12, "var(--muted)"))

QUANT_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--accent)"/><rect x="27" y="26" width="10" height="28" fill="var(--accent)"/><rect x="42" y="14" width="10" height="40" fill="var(--accent)"/>')
QUAL_I = icon('<path d="M32 14 l6 14 l15 2 l-11 10 l3 15 l-13 -8 l-13 8 l3 -15 l-11 -10 l15 -2 z" fill="var(--good)"/>')
NEGOT_I = icon('<path d="M38 20 l16 12 l-16 12" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M26 20 l-16 12 l16 12" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
SIGN_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 44 q6 8 12 0 q6 -8 12 0" stroke="var(--good)" stroke-width="3" fill="none"/>')

# 4. 평가 기준 네 가지
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 260, "⟦평가 기준|EVALUATION CRITERIA⟧",
                     ("⟦가격 — 낮을수록 좋아요|price — lower is better⟧",
                      "⟦일정 — 늦지 않게 끝낼 수 있나|schedule — can they finish on time?⟧",
                      "⟦기술력 — 실제로 잘하나|skill — are they actually good?⟧",
                      "⟦실적 — 이전 공연은 어땠나|track record — how were past shows?⟧"), 1.0)
         + person(560, 170, s=0.8, face=EYES, **PLANNER)
         + label(380, 300, "⟦가격만 보지 않고 네 기준을 같이 점수 매겨요|not just price — all four criteria scored together⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 너무 깎으면 품질·일정이 깨져요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + contract(190, 150, 0.9, signed=True) + label(190, 240, "⟦적당히 조율하면 모두 득을 봐요|a fair deal, and everyone gains⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN + SWEAT, **ARTIST) + label(570, 250, "⟦너무 깎으면 품질·일정이 깨져요|squeeze too hard and quality or schedule breaks⟧", 11, "var(--ink)")
         + label(380, 282, "⟦협상은 밀어붙이기가 아니라 균형을 찾는 거예요|negotiation isn't about pushing hardest — it's finding balance⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "negotiation", "order": 4,
    "title": ("조건을 조율해 서명하기", "Tuning Terms Until Both Sign"),
    "h1": ("<em>협상에 의한 계약·제안서 평가</em>가 뭐예요?", "What is <em>Negotiation-Based Proposal Evaluation</em>?"),
    "sub": ("협상에 의한 계약·제안서 평가를, 여러 출연 신청서를 비교하고 조건을 조율해 계약서에 서명하는 이야기로 풀어봤어요.",
            "Negotiation-based proposal evaluation, told as a story about comparing audition proposals and tuning terms until both sides sign."),
    "panels": [
        {"svg": P1, "alt": ('기획자가 세 장의 출연 신청서를 앞에 두고 진땀 흘림', 'The planner sweats over three audition proposals laid out in front of them'),
         "caption": ("출연 신청서가 세 장이나 왔는데, 뭘 골라야 할지 모르겠어요.", "Three audition proposals came in, and it's unclear which to pick."),
         "small": ("기획자 혼자서는 다 비교하기 벅차요.", "One planner alone can't compare them all.")},
        {"svg": P2, "alt": ('기획자가 제일 싼 팀을 제안하자 감독관이 가격만 보면 안 된다고 말함', "The planner suggests the cheapest team, and the director warns that price alone isn't enough"),
         "caption": ("가격만 보고 고르면 안 돼요.", "Choosing on price alone is a mistake."),
         "small": ("가격만 보고 고르면 나중에 품질 문제가 생겨요.", "Choosing on price alone causes quality problems later.")},
        {"svg": P3, "hero": True, "alt": ('서명된 계약서를 사이에 두고 기획자와 출연자가 웃음', 'The planner and the performer smile with a signed contract between them'),
         "caption": ("제안서 평가·협상은 점수표로 비교하고, 조건을 조율해 계약서에 서명하는 일이에요.", "Proposal evaluation and negotiation is comparing with a scorecard, then tuning terms until both sign."),
         "small": ("가격만 보지 않고, 조율할 여지를 남겨둬요.", "Not just price — leaving room to tune the terms."),
         "tricks": (4, [
             (QUANT_I, ("정량평가 하기", "Score quantitatively"), ("가격·일정을 숫자로 비교해요", "compare price and schedule as numbers"), "calm"),
             (QUAL_I, ("정성평가 하기", "Score qualitatively"), ("기술력·실적을 함께 봐요", "weigh skill and track record too")),
             (NEGOT_I, ("협상하기", "Negotiate"), ("대안을 들고 조건을 조율해요", "bring alternatives and tune the terms"), "warm"),
             (SIGN_I, ("계약서 서명하기", "Sign the contract"), ("합의된 조건을 문서로 남겨요", "put the agreed terms on paper")),
         ])},
        {"svg": P4, "alt": ('평가 기준 체크리스트: 가격, 일정, 기술력, 실적', 'A checklist of evaluation criteria: price, schedule, skill, track record'),
         "caption": ("평가는 이 네 가지를 함께 봐요.", "Evaluation weighs these four together."),
         "small": ("가격만 보지 않고 네 기준을 같이 점수 매겨요.", "Not just price — all four criteria scored together.")},
        {"svg": P5, "alt": ('왼쪽: 적당히 조율된 계약서. 오른쪽: 너무 깎여 지친 출연자', 'Left: a contract with fairly tuned terms. Right: a performer worn out from being squeezed too hard'),
         "caption": ("너무 깎으면 품질·일정이 깨져요.", "Squeeze too hard and quality or schedule breaks."),
         "small": ("협상은 밀어붙이기가 아니라 균형을 찾는 거예요.", "Negotiation isn't about pushing hardest — it's finding balance.")},
    ],
    "summary": (("<b>협상에 의한 계약·제안서 평가</b> = 여러 제안서를 <b>정량·정성 기준으로 비교</b>하고, <b>협상으로 조건을 조율</b>해 계약을 맺는 일.",
                 "<b>Negotiation-based proposal evaluation</b> = comparing proposals on both quantitative and qualitative criteria, then negotiating the terms into a signed contract."),
                ("제안서 평가는 가격·일정 같은 정량 지표와 기술력·실적 같은 정성 지표를 함께 점수화하는 과정이고, 협상은 그 결과를 바탕으로 양측이 받아들일 수 있는 조건을 찾아가는 과정이에요. 대안(BATNA)을 준비해두면 더 유리하게, 그러나 과도하게 밀어붙이지 않는 협상이 가능해요.",
                 "Proposal evaluation scores both quantitative metrics (price, schedule) and qualitative ones (skill, track record). Negotiation then finds terms both sides can accept. Preparing an alternative (BATNA) lets you negotiate from a stronger position — without pushing so hard it breaks the deal.")),
    "glossary": [
        ("정량평가", "Quantitative Evaluation", ("가격·일정을 숫자로 비교하는 일.", "Comparing price and schedule as numbers."), ("객관적이지만 전부는 아니에요.", "Objective, but not the whole picture.")),
        ("정성평가", "Qualitative Evaluation", ("기술력·실적을 보는 일.", "Looking at skill and track record."), ("숫자로 안 잡히는 역량을 봐요.", "Captures ability that numbers miss.")),
        ("BATNA", "BATNA", ("협상 결렬 시 쓸 수 있는 대안.", "The fallback option if talks break down."), ("있으면 협상에서 더 유리해요.", "Having one strengthens your position.")),
        ("RFP", "RFP", ("출연을 공개로 모집하는 공고.", "The open call recruiting performers."), ("제안서 평가는 이 공고에서 시작돼요.", "Proposal evaluation starts from this call.")),
        ("WBS", "WBS", ("공연 준비를 쪼갠 체크리스트.", "The checklist that breaks show prep into pieces."), ('계약 전 범위를 가늠할 때도 써요. → <a href="wbsppm-ko.html">공연 준비를 쪼갠 체크리스트</a>', 'Also used to gauge scope before the contract. → <a href="wbsppm-en.html">the checklist that breaks down show prep</a>')),
        ("SLA/SLM", "SLA/SLM", ("티켓에 적힌 보장 내용.", "The guarantee written on the ticket."), ('계약 조건의 일부로 함께 협상돼요. → <a href="slappe-ko.html">공연을 보장하는 티켓</a>', 'Negotiated as part of the same contract terms. → <a href="slappe-en.html">the ticket that guarantees the show</a>')),
        ("IT 투자성과 평가", "IT Investment Evaluation", ("공연 끝난 뒤 돈값 했는지 따지는 성적표.", "The scorecard checking if the investment paid off."), ('계약 조건은 이 평가에도 영향을 줘요. → <a href="itinvesteval-ko.html">공연 끝난 뒤의 성적표</a>', 'Contract terms feed back into this evaluation too. → <a href="itinvesteval-en.html">the scorecard after the show</a>')),
        ("감리/PMO", "IS Audit/PMO", ("전체를 바깥에서 점검하는 역할.", "A role that checks everything from the outside."), ('계약 체결 과정도 감리의 점검 대상이에요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'The contracting process is also something audit checks. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
