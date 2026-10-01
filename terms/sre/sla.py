from _draw import *
from _world import *

CLIENT = dict(hat="#2E3D57", shirt="#C9822B")  # 기업 손님 (정장 느낌)

# 1. 큰 손님이 물었는데 아무 문서가 없어요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 156, s=0.75, face=EYES, **CLIENT)
         + bubble(40, 50, 240, 50, "⟦우리랑 계약서에 뭐라고 약속했어요?|what did our contract promise us?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(430, 156, s=0.75, face=FROWN + SWEAT, **MANAGER)
         + board(500, 160, 220, 110, "⟦계약서|CONTRACT⟧", ("⟦아무것도 없어요|there's nothing here⟧",), 0.9)
         + label(380, 282, "⟦큰 손님이 물었는데 아무 문서가 없어요|a big customer asks, but there's no document⟧", 12, "var(--ink)", cls="d"))

# 2. 왜: 속으로 정한 목표만으론 안심 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(50, 40, 250, 100, "⟦우리끼리 목표(SLO)|OUR OWN TARGET (SLO)⟧", ("⟦목표: 99.9%|target: 99.9%⟧", "⟦아무도 몰라요|nobody outside knows⟧"), 0.9)
         + person(420, 156, s=0.75, face=EYES, **CLIENT)
         + bubble(330, 50, 220, 46, "⟦어기면 어떻게 되는데요?|what happens if you miss it?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(620, 156, s=0.75, face=FROWN + SWEAT, **MANAGER)
         + bubble(570, 60, 150, 40, "⟦음... 글쎄요|um... well...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦속으로 정한 목표만으론 손님이 안심 못 해요|a target kept to ourselves can't reassure the customer⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 손님과 정식으로 종이에 적어 약속해요
P3 = svg(350, sky(350)
         + board(230, 60, 320, 180, "⟦손님과 맺은 계약서|SLA CONTRACT⟧", ("⟦약속: 99.9% 이상|promise: 99.9% or higher⟧", "⟦못 지키면: 이용료 10% 환급|miss it: refund 10% of the fee⟧", "⟦분기마다 보고해요|reported every quarter⟧"), 1.0)
         + person(165, 220, s=0.8, face=SMILE, extra=CLIPBOARD, **MANAGER)
         + person(575, 220, s=0.8, face=SMILE, **CLIENT)
         + label(380, 28, "⟦손님과 정식으로 종이에 적어 약속해요|put the promise on paper, officially, with the customer⟧", 14, "var(--ink)", cls="d")
         + label(380, 336, "⟦내부 목표보다 느슨하게, 못 지키면 어떻게 할지도 적어요|looser than the internal target, and it spells out what happens if we miss⟧", 12, "var(--muted)"))

# 4. 계약서 세부 조항 + 서명
P4 = svg(300, sky(300, ground=False)
         + board(40, 40, 380, 220, "⟦계약서 세부 조항|CONTRACT DETAILS⟧",
                     ("⟦약속: 99.9% 이상|promise: 99.9%+⟧", "⟦못 지키면: 10% 환급|miss it: 10% refund⟧", "⟦보고: 분기마다|report: quarterly⟧", "⟦손님마다 계약이 달라요|each customer has its own contract⟧"), 1.0, hl=1)
         + board(460, 70, 260, 130, "⟦서명 완료|SIGNED⟧", ("⟦공원장 (서명)|Manager (signed)⟧",), 1.0)
         + '<path d="M490 170 q20 -16 40 0 t40 0 t40 0" stroke="#142033" stroke-width="2.5" fill="none"/>'
         + label(380, 282, "⟦몇 %를 지킬지, 못 지키면 뭘 해줄지 다 적어요|it spells out the percentage and what happens if it's missed⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳: 계약은 내부 목표보다 느슨해야 안전해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + board(40, 30, 300, 70, "⟦내부 목표(SLO)|INTERNAL (SLO)⟧", ("⟦99.95%|99.95%⟧",), 0.9)
         + board(40, 150, 300, 70, "⟦손님과 약속(SLA)|CUSTOMER (SLA)⟧", ("⟦99.9%|99.9%⟧",), 0.9)
         + label(190, 130, "⟦사이에 여유가 있어요|there's a buffer between them⟧", 11, "var(--good)", cls="d")
         + board(420, 30, 300, 70, "⟦내부 목표(SLO)|INTERNAL (SLO)⟧", ("⟦99.9%|99.9%⟧",), 0.9)
         + board(420, 110, 300, 70, "⟦손님과 약속(SLA)|CUSTOMER (SLA)⟧", ("⟦99.9%|99.9%⟧",), 0.9)
         + label(570, 198, "⟦여유가 없어요|no buffer at all⟧", 11, "var(--bad)", cls="d")
         + ticket(570, 240, 0.8, text="⟦위약금|penalty⟧", color="var(--bad)")
         + label(380, 284, "⟦계약은 내부 목표보다 느슨해야 안전해요|the contract has to be looser than the internal target to stay safe⟧", 12, "var(--ink)", cls="d"))

LOOSE_I = icon('<rect x="18" y="12" width="28" height="12" rx="5" fill="var(--accent)"/><rect x="8" y="34" width="48" height="12" rx="5" fill="var(--good)"/>')
REFUND_I = icon('<rect x="10" y="18" width="44" height="26" rx="4" fill="#E9B44C" stroke="#C9822B" stroke-width="3"/><path d="M22 31 h20" stroke="#142033" stroke-width="3" stroke-linecap="round"/>')
REPORT_I = icon('<rect x="14" y="8" width="36" height="46" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 31 h20 M22 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
CUSTOMERS_I = icon('<circle cx="20" cy="24" r="9" fill="var(--accent)"/><circle cx="44" cy="24" r="9" fill="#5B8DEF"/><rect x="8" y="36" width="24" height="18" rx="4" fill="var(--accent)"/><rect x="32" y="36" width="24" height="18" rx="4" fill="#5B8DEF"/>')

PAGE = {
    "slug": "sla", "order": 35,
    "title": ("손님과 맺은 약속 계약서", "The Contract We Sign With a Customer"),
    "h1": ("<em>SLA</em>가 뭐예요?", "What is an <em>SLA</em>?"),
    "sub": ("SLA(서비스 수준 계약)를 손님과 정식으로 종이에 적어 맺는 약속 이야기로 풀어봤어요.",
            "A Service Level Agreement, told as a story about putting the promise on paper, officially, with a customer."),
    "panels": [
        {"svg": P1, "alt": ("기업 손님이 계약 내용을 묻는데 공원장 옆 계약서 안내판이 비어 있음", "A corporate customer asks what the contract promised, while the manager's contract board is empty"),
         "caption": ("큰 손님이 물었는데 아무 문서가 없어요.", "A big customer asks, but there's no document."),
         "small": ("속으로 정한 목표만으론 손님이 안심 못 해요.", "A target kept to ourselves can't reassure the customer.")},
        {"svg": P2, "alt": ("손님이 어기면 어떻게 되냐고 묻고, 공원장은 속으로 정한 목표만 들고 당황함", "The customer asks what happens if the target is missed, and the manager, holding only an internal target, looks flustered"),
         "caption": ("왜 어려운가요?", "Why is this hard?"),
         "small": ("어기면 어떻게 되는지도 정해 둔 게 없어요.", "There's nothing written down for what happens if it's missed.")},
        {"svg": P3, "hero": True, "alt": ("공원장과 손님 사이에 계약서 안내판 — 99.9% 약속과 환급 조항이 적혀 있음", "A contract board between the manager and the customer, spelling out a 99.9% promise and a refund clause"),
         "caption": ("손님과 정식으로 종이에 적어 약속해요.", "Put the promise on paper, officially, with the customer."),
         "small": ("못 지키면 어떻게 할지도 함께 적어요.", "It spells out what happens if we miss, too."),
         "tricks": (4, [
             (LOOSE_I, ("내부 목표보다 느슨하게", "Looser than the internal target"), ("숨 쉴 여유를 남겨요", "leaves room to breathe"), "calm"),
             (REFUND_I, ("못 지키면 보상을 정해요", "Set the payback for missing it"), ("환불이나 크레딧으로요", "a refund or a credit")),
             (CUSTOMERS_I, ("손님마다 다른 계약", "A different contract per customer"), ("똑같지 않아도 돼요", "they don't have to match"), "warm"),
             (REPORT_I, ("분기마다 보고해요", "Report it every quarter"), ("지켰는지 알려줘요", "so they know it was kept")),
         ])},
        {"svg": P4, "alt": ("계약서 세부 조항 안내판 — 환불 항목이 강조됨, 옆엔 서명 완료 도장", "A contract-details board with the refund row highlighted, beside a signed stamp"),
         "caption": ("몇 %를 지킬지, 못 지키면 뭘 해줄지 다 적어요.", "It spells out the percentage and what happens if it's missed."),
         "small": ("공원장이 서명하면 정식 계약이 돼요.", "Once the manager signs, it becomes an official contract.")},
        {"svg": P5, "alt": ("왼쪽: 내부 목표 99.95%와 계약 99.9% 사이에 여유. 오른쪽: 둘 다 99.9%로 똑같아 여유 없이 위약금 티켓", "Left: a buffer between a 99.95% internal target and a 99.9% contract. Right: both set at 99.9% with no buffer, and a penalty ticket"),
         "caption": ("계약은 내부 목표보다 느슨해야 안전해요.", "The contract has to be looser than the internal target to stay safe."),
         "small": ("똑같이 빡빡하면 조금만 넘겨도 바로 위약금이에요.", "Set them equally tight, and the smallest miss triggers a penalty.")},
    ],
    "summary": (("<b>SLA</b> = 손님과 <b>정식으로 종이에 적은 약속</b>. <b>내부 목표(SLO)보다 느슨하게</b> 정하고, <b>못 지키면 돌려줄 것</b>까지 함께 적어요.",
                 "An <b>SLA</b> is the <b>promise put on paper, officially</b>, with a customer — set <b>looser than the internal SLO</b>, and spelling out <b>what gets paid back if it's missed</b>."),
                ("Service Level Agreement. 보통 법적 구속력이 있는 문서로, 가동 시간 조항과 위반 시 크레딧·환불을 명시해요. 내부 목표(SLO)와 똑같이 빡빡하게 잡으면 작은 흔들림에도 바로 위약금을 물게 돼요.",
                 "Usually a legally binding document spelling out an uptime clause and the credits or refunds owed on a breach. Set it as tight as the internal SLO, and the smallest wobble triggers a penalty.")),
    "glossary": [
        ("약속 계약", "SLA", ("손님과 정식으로 맺은 약속.", "The promise made official with a customer."), ("법적 구속력이 있는 문서예요.", "A legally binding document.")),
        ("SLO 와의 차이", "SLA vs SLO", ("속으로 정한 것과 손님과 약속한 것.", "What's kept internal versus promised outward."), ('SLA는 보통 SLO보다 느슨해요. → <a href="slo-ko.html">우리끼리 정한 목표 줄</a>', 'The SLA is usually looser than the SLO. → <a href="slo-en.html">the target line set internally</a>')),
        ("위약금·크레딧", "Penalty / credit", ("못 지키면 돌려주는 것.", "What's paid back when it's missed."), ("환불이나 서비스 크레딧이 흔해요.", "Often a refund or a service credit.")),
        ("계약 보고서", "Compliance report", ("약속을 지켰는지 알려주는 문서.", "The document that shows whether the promise held."), ("보통 분기마다 보내요.", "Usually sent every quarter.")),
        ("측정 분쟁", "Measurement dispute", ("누구 숫자가 맞는지 다투는 일.", "A fight over whose numbers are right."), ("그래서 측정 방식도 계약에 적어요.", "That's why the contract spells out how it's measured, too.")),
        ("손님별 계약", "Per-customer terms", ("손님마다 다를 수 있는 조건.", "Terms that can differ customer to customer."), ("큰 손님일수록 더 세세해요.", "The bigger the customer, the more detailed it gets.")),
        ("법적 구속력", "Legal binding", ("약속을 어기면 책임이 따라요.", "Breaking the promise carries real consequences."), ("그래서 말이 아니라 문서로 남겨요.", "That's why it's written down, not just spoken.")),
        ("가동 시간 조항", "Uptime clause", ("몇 % 이상 켜 둘지 적은 줄.", "The line that spells out how much uptime is owed."), ("이 조항이 계약의 핵심이에요.", "This clause is the heart of the contract.")),
    ],
}
