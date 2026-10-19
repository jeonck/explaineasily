from _draw import *
from _world import *

# 1. 문 열기 전엔, 어떤 요리를 내놓을지 몰라요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **CHEF)
         + dish(260, 230, 0.55) + dish(330, 220, 0.55, bad=True) + dish(400, 235, 0.55)
         + label(330, 285, "⟦위험한 요리도 자신 있게 내놓을 수 있어요|it might confidently serve a dangerous dish, too⟧", 12, "var(--bad)", cls="d")
         + label(600, 150, "⟦문은 아직 안 열었어요|the doors aren't open yet⟧", 12, "var(--muted)")
         + label(380, 25, "⟦손님을 받기 전에, 미리 알아야 해요|this needs to be known before any guest walks in⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 매번 다른 사람이 다르게 물어보면, 숫자로 비교할 수 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 150, s=0.75, face=EYES, **INSPECTOR) + badge(180, 110, 0.6)
         + label(160, 240, "⟦검사관은 매번 다르게 물어봐요|the inspector asks differently every time⟧", 11, "var(--muted)")
         + person(420, 150, s=0.75, face=EYES, **CHEF)
         + label(420, 240, "⟦이번 주방장이 저번보다 안전한지 모르겠어요|can't tell if this chef is safer than last time⟧", 11, "var(--muted)")
         + label(650, 150, "⟦?|?⟧", 40, "var(--bad)", cls="d")
         + label(380, 280, "⟦창의적인 시험만으론, 매번 같은 기준으로 숫자를 비교할 수 없어요|creative testing alone can't give the same yardstick, run after run⟧", 12, "var(--bad)", cls="d"))

# 3. 손님 받기 전 맛 평가 테스트 = 정해진 위험 주문 세트로 미리 채점하는 일 (hero)
P3 = svg(360, sky(360)
         + board(30, 30, 230, 150, "⟦위험 주문 세트|RISK TEST SET⟧",
                 ("⟦#1 위험한 요리 시켜 보기|#1 try ordering something unsafe⟧",
                  "⟦#2 거짓 정보 시켜 보기|#2 try asking for false info⟧",
                  "⟦#3 남의 비밀 물어보기|#3 try asking for a secret⟧")) + person(330, 170, s=0.8, face=EYES, **TASTER)
         + dish(420, 250, 0.55) + dish(480, 235, 0.55, bad=True)
         + board(560, 50, 170, 120, "⟦채점표|SCORECARD⟧",
                 ("⟦안전 82/100|safety 82/100⟧", "⟦×2 위험 요리 발견|×2 unsafe dishes found⟧"))
         + label(380, 25, "⟦손님 받기 전 맛 평가 테스트 = 정해진 위험 주문으로 미리 채점하는 일|a pre-launch tasting test scores it against a fixed set of risky orders first⟧", 13, "var(--ink)", cls="d"))

# 4. 정해진 주문 세트 → 채점 → 기준 → 오픈 또는 거부
P4 = svg(300, sky(300)
         + board(20, 40, 190, 120, "⟦시험 세트|TEST SET⟧", ("⟦같은 주문 100개|the same 100 orders⟧", "⟦매번 똑같이|every single time⟧"), 1.0)
         + label(245, 100, "⟦→|→⟧", 30, "var(--muted)", cls="d")
         + person(300, 100, s=0.65, face=EYES, **TASTER)
         + label(300, 200, "⟦하나씩 채점|score one by one⟧", 11, "var(--muted)")
         + label(390, 100, "⟦→|→⟧", 30, "var(--muted)", cls="d")
         + board(430, 40, 290, 150, "⟦결과|RESULT⟧", ("⟦82/100 — 기준 70 이상|82/100 — the bar is 70+⟧", "⟦기준 넘으면 ✓ 오픈|past the bar ✓ open⟧", "⟦못 넘으면 × 보류|under the bar × held back⟧"), 1.0, 1)
         + label(380, 280, "⟦같은 세트로, 매번 같은 방식으로 채점해요|the same set, scored the same way, every time⟧", 12, "var(--ink)"))

# 5. 기준을 넘었다고 끝이 아니에요 — 레드팀과는 하는 일이 달라요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + board(50, 30, 280, 150, "⟦시험지 안|ON THE TEST SET⟧", ("⟦82/100 — 안전해 보여요|82/100 — looks safe⟧",))
         + label(190, 220, "⟦정해진 문제는 잘 풀어요|it handles the known questions well⟧", 11, "var(--ink)")
         + person(560, 120, s=0.75, face=FROWN, **CHEF) + ticket(630, 160, 0.7, sneaky=True)
         + label(560, 230, "⟦시험지 밖의 새 쪽지는 못 막을 수도 있어요|a new note outside the test set might still get through⟧", 11, "var(--bad)")
         + label(380, 300, "⟦레드팀은 창의적으로 새 약점을 찾고, 이 테스트는 정해진 세트로 반복 채점해요 — 둘 다 필요해요|the red team hunts new weaknesses creatively; this test scores a fixed set, again and again — both are needed⟧", 12, "var(--ink)", cls="d"))

SCORE_I = icon('<rect x="10" y="8" width="44" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M20 42 h24" stroke="#142033" stroke-width="3"/>')
BAR_I = icon('<rect x="8" y="46" width="12" height="10" fill="var(--accent)"/><rect x="26" y="34" width="12" height="22" fill="var(--accent)"/><rect x="44" y="18" width="12" height="38" fill="var(--good)"/><path d="M4 56 h56" stroke="var(--muted)" stroke-width="2"/>')
REPEAT_I = icon('<path d="M16 20 a18 18 0 1 1 -2 22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M8 36 l6 10 l10 -4" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
GATE_I = icon('<rect x="14" y="26" width="36" height="26" rx="4" fill="var(--good)"/><path d="M20 26 v-6 a12 12 0 0 1 24 0 v6" fill="none" stroke="var(--good)" stroke-width="5"/>')

PAGE = {
    "slug": "safetyeval", "order": 27,
    "title": ("손님 받기 전 맛 평가 테스트", "The Tasting Test Before Opening"),
    "h1": ("<em>안전성 평가</em>가 뭐예요?", "What is a <em>Safety Evaluation</em>?"),
    "sub": ("AI 안전성 평가(safety eval)를, 문을 열기 전 정해진 위험 주문 세트로 미리 채점해 보는 맛 평가 테스트 이야기로 풀어봤어요.",
            "An AI safety evaluation, told as a story about a tasting test before opening — scoring the kitchen against a fixed set of risky orders first."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 요리 세 그릇을 내놓는데, 그중 한 그릇에 경고 표시가 있음. 문은 아직 열지 않음", "The chef serves three dishes, one of them marked with a warning; the doors aren't open yet"),
         "caption": ("문 열기 전엔, 어떤 요리를 내놓을지 몰라요.", "Before the doors open, you don't know what it might serve."),
         "small": ("위험한 요리도 자신 있게 내놓을 수 있어요. 손님을 받기 전에 미리 알아야 해요.", "It might confidently serve a dangerous dish, too — and that needs to be known before any guest walks in.")},
        {"svg": P2, "alt": ("검사관은 매번 다르게 물어보고, 그래서 이번 주방장이 저번보다 안전한지 숫자로 비교할 수 없음", "The inspector asks differently each time, so there's no way to score whether this chef is safer than the last one"),
         "caption": ("창의적인 시험만으론 숫자로 비교할 수 없어요.", "Creative testing alone can't give you a number to compare."),
         "small": ('<a href="airedteam-ko.html">위생 검사관의 불시 방문</a>은 매번 새로운 방법을 찾아요 — 그래서 매번 같은 기준으로 재는 다른 시험이 필요해요.',
                   'The <a href="airedteam-en.html">inspector\'s surprise visit</a> finds a new trick each time — so a different kind of test, one that measures the same way every time, is also needed.')},
        {"svg": P3, "hero": True, "alt": ("정해진 위험 주문 세트 안내판, 맛보기 검수원이 요리를 맛보며 채점표에 숫자를 매김. 위험한 요리 하나가 발견됨", "A board listing a fixed risk test set; the taster scores the dishes on a scorecard, catching one unsafe dish"),
         "caption": ("손님 받기 전 맛 평가 테스트 = 정해진 위험 주문 세트로 미리 채점하는 일이에요.", "A pre-launch tasting test scores the kitchen against a fixed set of risky orders, before it opens."),
         "small": ("같은 위험 주문들을 똑같이 넣어 보고, 숫자로 점수를 매겨요.", "The same risky orders go in every time, and the result comes back as a number."),
         "tricks": (4, [
             (SCORE_I, ("정해진 위험 주문 세트", "A fixed set of risky orders"), ("매번 똑같은 문제예요", "the same questions, every run"), "calm"),
             (BAR_I, ("숫자로 채점", "Score it with a number"), ("82점처럼 비교 가능해요", "like an 82 — easy to compare"), "calm"),
             (REPEAT_I, ("반복해서 다시 채점", "Re-score it again and again"), ("새 버전이 나올 때마다요", "every time a new version ships"), "warm"),
             (GATE_I, ("기준 넘어야 오픈", "Must clear the bar to open"), ("못 넘으면 문을 못 열어요", "under the bar, the doors stay shut"), "warm"),
         ])},
        {"svg": P4, "alt": ("같은 시험 세트 100개가 맛보기 검수원에게 들어가 하나씩 채점되고, 82/100 결과가 나와 기준 70을 넘어 오픈으로 이어짐", "The same 100-item test set goes to the taster, is scored one by one, and comes back 82/100 — past the 70-point bar, so it opens"),
         "caption": ("같은 세트를 같은 방식으로 채점해요.", "The same set, scored the same way."),
         "small": ("기준 점수를 넘으면 문을 열고, 못 넘으면 고칠 때까지 보류해요.", "Clear the bar and the doors open; fall short and it's held back until it's fixed.")},
        {"svg": P5, "alt": ("왼쪽: 시험지 안 문제는 82점으로 잘 풀어냄. 오른쪽: 시험지 밖의 새 쪽지에 주방장이 당황함", "Left: it scores 82 on the known test. Right: a new note outside the test set leaves the chef flustered"),
         "caption": ("기준을 넘었다고 끝이 아니에요.", "Clearing the bar isn't the end."),
         "small": ("시험지 밖의 새 쪽지는 여전히 통할 수 있어요. 레드팀은 새 약점을 찾고, 이 테스트는 정해진 세트로 반복 채점해요.", "A note outside the test set can still get through. The red team hunts new weaknesses; this test re-scores a fixed set.")},
    ],
    "summary": (("<b>안전성 평가</b> = 문을 열기 전, <b>정해진 위험 주문 세트</b>로 이 주방을 <b>숫자로 미리 채점</b>하는 맛 평가 테스트.",
                 "<b>A safety evaluation</b> is a tasting test that <b>scores this kitchen with a number</b>, against a <b>fixed set of risky orders</b>, before the doors ever open."),
                ("안전성 평가(Safety Eval)는 AI 모델을 배포하기 전, 표준화된 위험 행동 테스트셋으로 반복 채점해 수치로 비교하는 방법이에요. 레드팀이 사람이 창의적으로 새 약점을 찾는 것과 달리, 평가는 정해진 테스트셋을 매 버전마다 똑같이 돌려서 '이번 버전이 저번보다 안전한가'를 숫자로 답해요.",
                 "A safety evaluation scores an AI model against a standardized test set of risky behaviors before deployment, so results can be compared as numbers run after run. Unlike red teaming, where people creatively hunt for new weaknesses, an eval runs the same fixed test set on every version to answer, numerically, whether this version is safer than the last.")),
    "glossary": [
        ("안전성 평가", "Safety evaluation", ("손님 받기 전 맛 평가 테스트.", "The tasting test before opening."), ('이 분야 전체 소개는 여기에. → <a href="llmthreats-ko.html">AI 보안이 뭐예요?</a>', 'The overview of this whole field. → <a href="llmthreats-en.html">What is AI Security?</a>')),
        ("AI 레드팀", "AI red team", ("위생 검사관의 불시 방문.", "The inspector's surprise visit."), ('창의적으로 새 약점을 찾는 쪽은 여기서. → <a href="airedteam-ko.html">AI 레드팀이 뭐예요?</a>', 'Here\'s the one hunting new weaknesses creatively. → <a href="airedteam-en.html">What is an AI Red Team?</a>')),
        ("평가 (Evaluation)", "Evaluation (eval)", ("시험관의 채점표.", "The examiner's scorecard."), ('AI 세계의 더 넓은 채점 이야기예요. → <a href="evaluation-ko.html">평가가 뭐예요?</a>', 'The broader AI-world story about scoring. → <a href="evaluation-en.html">What is Evaluation?</a>')),
        ("벤치마크", "Benchmark", ("매번 똑같이 쓰는 100개 문제.", "The same 100 questions, used every time."), ("안전성 평가가 쓰는 시험 세트가 바로 이거예요.", "The test set a safety eval runs is exactly this.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('평가 점수가 낮으면 가드레일을 더 세워요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'A low score means stronger guardrails get built. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("할루시네이션", "Hallucination", ("모르는데 자신 있게 답하는 버릇.", "Confidently answering even when unsure."), ('맛 평가 테스트가 잡아내려는 문제 중 하나예요. → <a href="hallucination-ko.html">할루시네이션이 뭐예요?</a>', 'One of the things the tasting test is built to catch. → <a href="hallucination-en.html">What is a Hallucination?</a>')),
        ("미세조정", "Fine-tuning", ("레시피를 다시 손보는 일.", "Reworking the recipe."), ('점수가 낮으면 다시 손보고 또 채점해요. → <a href="finetune-ko.html">미세조정이 뭐예요?</a>', 'A low score sends it back for rework, then re-scoring. → <a href="finetune-en.html">What is Fine-tuning?</a>')),
        ("사장님 최종 승인", "The owner's final sign-off", ("기준 넘은 뒤에도 남는 마지막 확인.", "The last check kept even after clearing the bar."), ('기준을 넘어도 위험한 행동엔 이게 더 필요해요. → <a href="humanapproval-ko.html">사장님 최종 승인이 뭐예요?</a>', 'Clearing the bar still isn\'t enough for risky actions. → <a href="humanapproval-en.html">What is a human approval gate?</a>')),
    ],
}
