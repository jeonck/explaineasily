from _draw import *
from _world import *


def line_to(x0, y0, x1, y1):
    """점선 화살표 (x0,y0) → (x1,y1)."""
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    hx, hy = x1 - 10 * math.cos(a - 0.5), y1 - 10 * math.sin(a - 0.5)
    kx, ky = x1 - 10 * math.cos(a + 0.5), y1 - 10 * math.sin(a + 0.5)
    return (f'<path d="M{x0} {y0} L{x1} {y1}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{hx:.1f} {hy:.1f} L{x1} {y1} L{kx:.1f} {ky:.1f}" stroke="var(--muted)" stroke-width="3" fill="none"/>')


def qbox(x, y, text):
    return f'<rect x="{x}" y="{y}" width="150" height="34" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>' + label(x + 75, y + 21, text, 11, "var(--ink)")


# 1. 모든 질문을 제일 큰 앵무새에게 — "안녕"에도 큰 앵무새, 청구서 폭발
P1 = svg(300, sky(300)
         + qbox(20, 52, "⟦안녕!|hi!⟧") + qbox(20, 122, "⟦이 글 요약해 줘|summarize this⟧") + qbox(20, 192, "⟦계약서 검토해 줘|review this contract⟧")
         + line_to(175, 69, 350, 150) + line_to(175, 139, 350, 165) + line_to(175, 209, 350, 180)
         + label(420, 90, "⟦제일 큰 앵무새|the biggest parrot⟧", 12, "var(--ink)", cls="d")
         + perch(420, 210, 180) + parrot(420, 170, 1.6, color=PARROT_BIG, talk=True)
         + note(560, 50, 170, 120, "⟦청구서|BILL⟧", ("⟦안녕 → 콩 100|hi → 100 beans⟧", "⟦요약 → 콩 100|summary → 100⟧", "⟦검토 → 콩 100|review → 100⟧"), 0.95)
         + label(645, 200, "⟦콩 값 폭발!|beans explode!⟧", 14, "var(--bad)", cls="d")
         + label(380, 282, "⟦인사 한마디에도 제일 큰 앵무새 — 청구서가 터져요|even a hello goes to the biggest parrot — the bill explodes⟧", 13, "var(--ink)"))

# 2. 한 마리만 쓰면 낭비 아니면 부족
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<path d="M380 50 V270" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5"/>'
         + label(190, 30, "⟦큰 앵무새 한 마리만|only the big parrot⟧", 13, "var(--ink)", cls="d")
         + bubble(40, 55, 150, 34, "⟦안녕!|hi!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + parrot(200, 165, 1.5, color=PARROT_BIG, talk=True)
         + "".join(bean(60 + i * 36, 200, 1.0) for i in range(3)) + label(96, 232, "⟦콩 100개|100 beans⟧", 11, "var(--muted)")
         + label(190, 262, "⟦인사에도 콩이 100개 — 낭비|100 beans for a hello — waste⟧", 11, "var(--bad)")
         + label(570, 30, "⟦작은 앵무새 한 마리만|only the small parrot⟧", 13, "var(--ink)", cls="d")
         + bubble(420, 55, 180, 34, "⟦계약서 검토해 줘|review this contract⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + parrot(560, 175, 0.7, mood="sweat", talk=True)
         + bubble_parrot(600, 110, 140, 36, "⟦음… 괜찮은 듯?|um… looks fine?⟧", 11, bad=True)
         + label(570, 262, "⟦어려운 일엔 모자라요 — 부족|too small for hard work — short⟧", 11, "var(--bad)")
         + label(380, 300, "⟦질문마다 필요한 앵무새 크기가 달라요 — 한 마리로는 낭비 아니면 부족|each question needs a different size — one bird means waste or shortfall⟧", 12, "var(--ink)"))

# 3. 라우팅 = 문 앞 안내 앵무새가 질문을 보고 누구에게 보낼지 정하는 것 (hero)
P3 = svg(360, sky(360)
         + note(30, 50, 180, 120, "⟦안내판|GUIDE BOARD⟧", ("⟦쉬움 → 작은 앵무새|easy → small parrot⟧", "⟦보통 → 중간 앵무새|medium → medium parrot⟧", "⟦어려움 → 큰 앵무새|hard → big parrot⟧"), 0.95)
         + label(120, 200, "⟦문 앞에서 먼저 봐요|it looks first, at the door⟧", 11, "var(--muted)")
         + f'<rect x="215" y="140" width="70" height="140" rx="4" fill="{WOOD}"/>'
         + label(250, 125, "⟦안내 앵무새|the guide parrot⟧", 12, "var(--ink)", cls="d")
         + parrot(250, 200, 1.0, talk=True)
         + line_to(290, 180, 410, 110) + line_to(290, 190, 515, 160) + line_to(290, 200, 620, 215)
         + perch(450, 125, 70) + parrot(450, 85, 0.7) + label(450, 185, "⟦작은 · 콩 1|small · 1 bean⟧", 11, "var(--ink)")
         + perch(560, 190, 90) + parrot(560, 150, 1.0) + label(560, 250, "⟦중간 · 콩 10|medium · 10 beans⟧", 11, "var(--ink)")
         + perch(680, 245, 120) + parrot(680, 205, 1.3, color=PARROT_BIG) + label(680, 305, "⟦큰 · 콩 100|big · 100 beans⟧", 11, "var(--ink)")
         + label(380, 340, "⟦라우팅 = 문 앞 안내 앵무새가 질문을 보고, 작은·중간·큰 앵무새 중 누구에게 보낼지 정하는 것|routing: a guide parrot at the door looks at each question and picks small, medium or big⟧", 13, "var(--ink)", cls="d"))

# 4. 질문 세 개 → 각자 맞는 앵무새, 콩은 3분의 1
P4 = svg(320, sky(320)
         + qbox(20, 45, "⟦안녕!|hi!⟧") + line_to(175, 62, 215, 62) + parrot(250, 62, 0.55) + label(330, 66, "⟦콩 1|1 bean⟧", 13, "var(--good)", cls="d")
         + qbox(20, 123, "⟦이 글 요약해 줘|summarize this⟧") + line_to(175, 140, 215, 140) + parrot(250, 140, 0.85) + label(330, 144, "⟦콩 10|10 beans⟧", 13, "var(--good)", cls="d")
         + qbox(20, 209, "⟦계약서 검토해 줘|review this contract⟧") + line_to(175, 226, 208, 226) + parrot(250, 226, 1.1, color=PARROT_BIG) + label(330, 230, "⟦콩 100|100 beans⟧", 13, "var(--good)", cls="d")
         + note(420, 40, 150, 110, "⟦다 큰 앵무새|ALL TO THE BIG⟧", ("⟦100 + 100 + 100|100 + 100 + 100⟧", "⟦= 콩 300|= 300 beans⟧"), 0.95)
         + note(590, 40, 150, 110, "⟦안내 앵무새|ROUTED⟧", ("⟦1 + 10 + 100|1 + 10 + 100⟧", "⟦= 콩 111|= 111 beans⟧"), 0.95, 1)
         + label(580, 190, "⟦같은 답, 콩은 3분의 1|same answers, a third of the beans⟧", 12, "var(--good)", cls="d")
         + label(580, 215, "⟦쉬운 건 작은 앵무새도 똑같이 잘해요|the small parrot does easy ones just as well⟧", 11, "var(--muted)")
         + label(380, 300, "⟦질문마다 맞는 크기로 — 답은 같고 콩은 훨씬 적어요|the right size per question — same answers, far fewer beans⟧", 12, "var(--ink)"))

# 5. 안내 앵무새도 틀려요 — 그래서 폴백과 시험
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 30, "⟦안내 앵무새가 틀리면|when the guide is wrong⟧", 13, "var(--ink)", cls="d")
         + bubble(20, 50, 170, 34, "⟦계약서 검토해 줘|review this contract⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + parrot(70, 160, 0.9) + label(70, 215, "⟦안내|guide⟧", 10, "var(--muted)")
         + line_to(110, 150, 175, 150) + label(140, 135, "⟦쉬운 줄 알고|thinks it is easy⟧", 10, "var(--bad)")
         + parrot(220, 160, 0.7, mood="sweat", talk=True)
         + bubble_parrot(200, 60, 170, 36, "⟦음… 괜찮은 듯?|um… looks fine?⟧", 11, bad=True)
         + label(190, 262, "⟦품질이 새요 — 틀린 답이 나가요|quality leaks — a wrong answer goes out⟧", 11, "var(--bad)")
         + label(570, 30, "⟦그래서 폴백과 시험|so: fallback and tests⟧", 13, "var(--ink)", cls="d")
         + parrot(440, 150, 0.7, talk=True) + bubble_parrot(390, 60, 150, 36, "⟦자신 없어요!|not sure!⟧", 11)
         + line_to(470, 150, 545, 150) + label(505, 135, "⟦넘겨요|pass up⟧", 10, "var(--good)")
         + parrot(600, 150, 1.2, color=PARROT_BIG)
         + person(670, 120, s=0.8, face=SMILE, **EXAMINER) + note(660, 40, 90, 60, "⟦시험|TEST⟧", ("⟦작은 ✓ 80%|small ✓ 80%⟧",), 0.85)
         + label(570, 240, "⟦시험으로 어디까지 작은 앵무새로 되는지 재요|tests measure how far the small parrot can go⟧", 11, "var(--ink)")
         + label(570, 262, "⟦자신 없으면 큰 앵무새로 넘겨요|not sure → pass it to the big one⟧", 11, "var(--good)")
         + label(380, 300, "⟦안내 앵무새도 틀려요 — 그래서 폴백과 시험이 같이 가요|the guide gets it wrong too — so fallback and tests go with it⟧", 12, "var(--ink)", cls="d"))

SMALL_I = icon('<ellipse cx="26" cy="38" rx="9" ry="12" fill="#5B8DEF"/><circle cx="26" cy="22" r="7" fill="#5B8DEF"/><path d="M31 20 l7 2 l-7 3z" fill="#E9B44C"/><path d="M8 52 h36" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/><path d="M44 30 l5 5 l9 -10" stroke="var(--good)" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
BIG_I = icon('<ellipse cx="30" cy="36" rx="14" ry="18" fill="#3F6FD1"/><circle cx="30" cy="14" r="10" fill="#3F6FD1"/><path d="M38 12 l10 3 l-10 4z" fill="#E9B44C"/><path d="M6 56 h48" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/><rect x="46" y="22" width="14" height="18" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M49 28 h8 M49 33 h6" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
FALLBACK_I = icon('<ellipse cx="18" cy="44" rx="8" ry="10" fill="#5B8DEF"/><circle cx="18" cy="30" r="6" fill="#5B8DEF"/><ellipse cx="48" cy="38" rx="11" ry="14" fill="#3F6FD1"/><circle cx="48" cy="18" r="8" fill="#3F6FD1"/><path d="M26 30 Q34 18 40 22" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M36 18 L41 23 L35 26" stroke="var(--accent)" stroke-width="3" fill="none"/>')
TEST_I = icon(f'<circle cx="24" cy="22" r="10" fill="{SKIN}"/><path d="M12 18 Q24 6 36 18 Z" fill="#E9B44C"/><rect x="14" y="34" width="20" height="18" rx="5" fill="#4A5A72"/><rect x="38" y="24" width="20" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M42 34 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "routing", "order": 36,
    "title": ("어느 앵무새에게 시킬까", "Which Parrot Gets the Job?"),
    "h1": ("<em>라우팅</em>이 뭐예요?", "What is <em>Routing</em>?"),
    "sub": ("모델 라우팅을 문 앞 안내 앵무새가 질문을 보고 작은·중간·큰 앵무새 중 누구에게 보낼지 정하는 이야기로 풀어봤어요.",
            "Model routing, told as a story about a guide parrot at the door that looks at each question and decides whether the small, medium or big parrot should answer."),
    "panels": [
        {"svg": P1, "alt": ("'안녕!', '이 글 요약해 줘', '계약서 검토해 줘' 세 질문이 모두 제일 큰 앵무새에게 감. 청구서 쪽지: 안녕 → 콩 100, 요약 → 100, 검토 → 100. '콩 값 폭발!'", "Three questions — hi!, summarize this, review this contract — all go to the biggest parrot. A BILL note: hi → 100 beans, summary → 100, review → 100. Beans explode!"),
         "caption": ("모든 질문을 제일 큰 앵무새에게 보내요. 인사 한마디에도요. 청구서가 터져요.", "Every question goes to the biggest parrot — even a hello. The bill explodes."),
         "small": ('큰 앵무새는 답 하나에 <a href="token-ko.html">콩</a>이 많이 들어요. 인사, 요약, 계약서 검토가 다 같은 값이면 <a href="pricing-ko.html">콩 값</a>이 금방 쌓여요.', 'The big parrot spends many <a href="token-en.html">beans</a> per answer. If a hello, a summary and a contract review all cost the same, the <a href="pricing-en.html">bean bill</a> piles up fast.')},
        {"svg": P2, "alt": ("왼쪽: '안녕!'에 큰 앵무새가 답하고 콩 100개 — 낭비. 오른쪽: '계약서 검토해 줘'에 땀 흘리는 작은 앵무새가 빨간 말풍선으로 '음… 괜찮은 듯?' — 부족", "Left: the big parrot answers hi! and spends 100 beans — waste. Right: a sweating small parrot answers review this contract with a red bubble, um… looks fine? — shortfall"),
         "caption": ("질문마다 필요한 앵무새 크기가 달라요. 한 마리만 쓰면 낭비 아니면 부족이에요.", "Each question needs a different size of parrot. One bird for everything means waste or shortfall."),
         "small": ('<a href="llm-ko.html">큰 앵무새</a>는 더 알고 느리고 비싸고, 작은 앵무새는 빠르고 싸지만 어려운 일엔 모자라요. 어려운 걸 작은 새에게 주면 <a href="hallucination-ko.html">그럴듯한 오답</a>이 나가요.',
                   'The <a href="llm-en.html">big parrot</a> knows more, is slower and pricier; the small one is fast and cheap but short on hard work. Give a hard one to the small bird and a <a href="hallucination-en.html">plausible wrong answer</a> goes out.')},
        {"svg": P3, "hero": True, "alt": ("'안내판' 쪽지: 쉬움 → 작은 앵무새, 보통 → 중간, 어려움 → 큰 앵무새. 문 앞의 안내 앵무새에서 점선이 작은(콩 1)·중간(콩 10)·큰(콩 100) 앵무새 횃대로 갈라짐", "A GUIDE BOARD note: easy → small parrot, medium → medium, hard → big. From a guide parrot at a door, dotted lines split to perches for the small (1 bean), medium (10 beans) and big (100 beans) parrots"),
         "caption": ("라우팅은 문 앞 안내 앵무새가 질문을 보고, 작은·중간·큰 앵무새 중 누구에게 보낼지 정하는 거예요.", "Routing is a guide parrot at the door looking at each question and picking the small, medium or big parrot."),
         "small": ('안내 앵무새는 질문을 읽고 "쉬움·보통·어려움" 딱지를 붙여요. 딱지대로 보내면 쉬운 건 싸게, 어려운 건 제대로 답해요. 안내 앵무새 자체는 아주 작은 새거나 <a href="prompt-ko.html">쪽지</a> 몇 줄이에요.',
                   'The guide parrot reads the question and tags it easy, medium or hard. Sent by tag, easy ones get answered cheaply and hard ones properly. The guide itself is a tiny bird, or just a few lines of <a href="prompt-en.html">note</a>.'),
         "tricks": (4, [
             (SMALL_I, ("쉬운 건 작은 앵무새", "Easy → small parrot"), ("인사, 짧은 답, 분류", "hellos, short answers, sorting"), "calm"),
             (BIG_I, ("어려운 건 큰 앵무새", "Hard → big parrot"), ("긴 추론, 법률, 코드", "long reasoning, law, code"), "calm"),
             (FALLBACK_I, ("자신 없으면 넘겨요", "Not sure? Pass it up"), ("작은 새 → 큰 새 (폴백)", "small → big (fallback)"), "warm"),
             (TEST_I, ("시험으로 선을 그어요", "Draw the line with tests"), ("어디까지 작은 새로 되나", "how far the small bird goes")),
         ])},
        {"svg": P4, "alt": ("세 줄: '안녕!' → 작은 앵무새 콩 1, '이 글 요약해 줘' → 중간 앵무새 콩 10, '계약서 검토해 줘' → 큰 앵무새 콩 100. 오른쪽 두 쪽지: 다 큰 앵무새 = 콩 300, 안내 앵무새 = 콩 111. '같은 답, 콩은 3분의 1'", "Three rows: hi! → small parrot 1 bean; summarize this → medium 10 beans; review this contract → big 100 beans. Two notes on the right: all to the big = 300 beans, routed = 111 beans. Same answers, a third of the beans"),
         "caption": ("질문마다 맞는 크기로 보내면 답은 같고 콩은 훨씬 적어요.", "Send each question to the right size and the answers stay the same while the beans drop a lot."),
         "small": ('작은 앵무새는 빠르기도 해요 — <a href="inference-ko.html">답하는 시간</a>이 짧아요. 여러 단계 <a href="workflow-ko.html">심부름 순서표</a>에서는 단계마다 다른 앵무새를 골라요.', 'The small parrot is also quicker — a shorter <a href="inference-en.html">answer time</a>. In a multi-step <a href="workflow-en.html">errand list</a>, each step can pick a different parrot.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 안내 앵무새가 '계약서 검토해 줘'를 쉬운 줄 알고 작은 앵무새에게 보내고, 작은 앵무새가 '음… 괜찮은 듯?' — 품질이 샘. 오른쪽 초록: 작은 앵무새가 '자신 없어요!'라며 큰 앵무새에게 넘기고, 시험관이 '작은 ✓ 80%' 시험지를 듦", "Left, red: the guide thinks review this contract is easy, sends it to the small parrot, which says um… looks fine? — quality leaks. Right, green: the small parrot says not sure! and passes it to the big one; an examiner holds a TEST note reading small ✓ 80%"),
         "caption": ("안내 앵무새도 틀려요. 어려운 걸 쉬운 줄 알면 품질이 새요. 그래서 폴백과 시험이 같이 가요.", "The guide gets it wrong too. Mistake hard for easy and quality leaks. So fallback and tests go with it."),
         "small": ('작은 새가 "자신 없어요" 하면 큰 새로 넘겨요(폴백). 그리고 <a href="evaluation-ko.html">시험관</a>이 어디까지 작은 새로 되는지 재요. 아낀 <a href="pricing-ko.html">콩 값</a>보다 새는 품질이 크면 손해예요.',
                   'When the small bird says not sure, pass it to the big one (fallback). And the <a href="evaluation-en.html">examiner</a> measures how far the small bird can go. If leaked quality outweighs the saved <a href="pricing-en.html">beans</a>, you lose.')},
    ],
    "summary": (("<b>라우팅</b> = 문 앞 <b>안내 앵무새</b>가 질문을 보고 <b>작은·중간·큰 앵무새</b> 중 누구에게 보낼지 정하는 것. 쉬운 건 싸게, 어려운 건 제대로. 안내 앵무새도 틀리니 <b>폴백</b>(자신 없으면 큰 새로)과 <b>시험</b>이 같이 가요.",
                 "<b>Routing</b> = a <b>guide parrot</b> at the door decides whether the <b>small, medium or big parrot</b> answers each question. Easy ones cheaply, hard ones properly. The guide errs too, so <b>fallback</b> (not sure → big bird) and <b>tests</b> go with it."),
                ("Model routing. 요청마다 난이도·종류를 분류해 알맞은 모델(작은·중간·큰)로 보내 비용과 지연 시간을 줄이는 기법이에요. 분류기는 작은 모델이나 규칙·프롬프트로 만들고, 작은 모델이 확신이 낮으면 큰 모델로 넘기는 폴백(캐스케이드)을 둬요. 어느 요청까지 작은 모델로 충분한지는 평가 세트로 재고, 잘못 분류한 요청의 품질 손실이 절감액보다 크지 않은지 계속 확인해요.",
                 "Classifying each request by difficulty or type and sending it to the right model (small, medium, large) to cut cost and latency. The classifier is a small model, rules, or a prompt; when the small model is unsure it escalates to a larger one (fallback, cascade). An evaluation set decides how far the small model can go, and you keep checking that quality lost on misrouted requests doesn\'t outweigh the savings.")),
    "glossary": [
        ("모델 라우팅", "Model routing", ("안내 앵무새.", "The guide parrot."), ("질문을 보고 작은·중간·큰 앵무새 중 누구에게 보낼지 정해요.", "Looks at the question and picks the small, medium or big parrot.")),
        ("분류기", "Classifier", ("질문에 쉬움·어려움 딱지 붙이기.", "Tagging questions easy or hard."), ("아주 작은 앵무새이거나 규칙 몇 줄이에요. 빠르고 싸야 해요.", "A tiny parrot or a few rules. It has to be fast and cheap.")),
        ("폴백", "Fallback", ("자신 없으면 큰 앵무새로 넘기기.", "Passing it up when unsure."), ("작은 새가 '모르겠어요' 하면 큰 새가 다시 답해요. 안내 실수를 받아 줘요.", "When the small bird says it doesn\'t know, the big bird answers again. It catches the guide\'s mistakes.")),
        ("캐스케이드", "Cascade", ("작은 새 먼저, 안 되면 다음 새.", "Small bird first, then the next."), ("작은 → 중간 → 큰 순서로 올려요. 대부분은 작은 새에서 끝나요.", "Escalate small → medium → big. Most questions end at the small bird.")),
        ("비용 최적화", "Cost optimization", ("콩 값 아끼기.", "Saving beans."), ('쉬운 질문에 큰 새를 안 쓰는 게 제일 큰 절약이에요. → <a href="pricing-ko.html">콩 값</a>', 'Not using the big bird for easy questions is the biggest saving. → <a href="pricing-en.html">the bean bill</a>')),
        ("지연 시간", "Latency", ("답이 나오기까지 걸리는 시간.", "Time until the answer arrives."), ('작은 앵무새가 훨씬 빨라요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'The small parrot is much faster. → <a href="inference-en.html">what answering costs and takes</a>')),
        ("평가", "Evaluation", ("어디까지 작은 새로 되는지 재기.", "Measuring how far the small bird goes."), ('시험 없이 라우팅하면 품질이 새는지 몰라요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Route without tests and you won\'t see quality leaking. → <a href="evaluation-en.html">the examiner\'s scorecard</a>')),
        ("워크플로", "Workflow", ("단계마다 다른 앵무새.", "A different parrot per step."), ('심부름 순서표의 각 칸에 맞는 새를 골라요. → <a href="workflow-ko.html">심부름 순서표</a>', 'Each step of the errand list picks its own bird. → <a href="workflow-en.html">the errand list</a>')),
    ],
}
