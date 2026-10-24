from _draw import *
from _world import *

# 1. 외운 문제로 시험 봐서 100점이 나왔어요
P1 = svg(300, sky(300)
         + person(170, 170, s=0.8, face=SMILE, **TEACHER)
         + bin_(300, 230, 0.9, "⟦훈련에 쓴 작물 그대로|same crops used in training⟧")
         + stamp2(430, 160, 0.8, ok=True) + label(430, 220, "⟦100점!|100%!⟧", 16, "var(--good)", cls="d")
         + bubble(520, 70, 200, 46, "⟦완벽하네요, 바로 써도 될까요?|perfect — can we ship it as is?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦근데 이 시험, 훈련 때 본 작물 그대로예요|but this test used the exact same crops it trained on⟧", 12, "var(--ink)"))

# 2. 검수반장이 그건 진짜 시험이 아니라고 지적해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 160, s=0.85, face=FROWN, **INSPECTOR)
         + bubble(90, 70, 260, 50, "⟦외운 문제로 시험 보면 100점은 당연해요, 처음 보는 작물로 다시 해봐요|of course it's 100% on memorized questions — try crops it's never seen⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 170, s=0.8, face=SWEAT + EYES, **TEACHER)
         + label(380, 280, "⟦훈련에 쓴 데이터로 평가하면 성적이 부풀려져요|grading on the training data itself inflates the score⟧", 12, "var(--ink)"))

# 3. 교차검증 = 조를 나눠, 한 조씩 번갈아 '처음 보는 시험지'로 쓰는 것 (hero)
P3 = svg(360, sky(360)
         + bin_(140, 200, 0.75, "⟦1조|GROUP 1⟧") + bin_(260, 200, 0.75, "⟦2조|GROUP 2⟧") + bin_(380, 200, 0.75, "⟦3조|GROUP 3⟧", color="var(--bad)") + bin_(500, 200, 0.75, "⟦4조|GROUP 4⟧") + bin_(620, 200, 0.75, "⟦5조|GROUP 5⟧")
         + label(380, 150, "⟦이번엔 3조가 시험지, 나머지로 훈련|this round group 3 is the test, the rest train it⟧", 13, "var(--bad)", cls="d")
         + label(380, 30, "⟦교차검증 = 데이터를 여러 조로 나눠, 한 조씩 번갈아 처음 보는 시험지로 쓰는 것|cross validation = splitting data into groups and rotating which one serves as the never-seen test⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦5번 돌아가며 전부 한 번씩 시험지가 돼요|it rotates five times, so every group gets a turn as the test⟧", 12, "var(--muted)"))

SPLIT_I = icon('<rect x="8" y="22" width="12" height="20" fill="var(--accent)"/><rect x="24" y="22" width="12" height="20" fill="var(--accent)"/><rect x="40" y="22" width="12" height="20" fill="var(--bad)"/><rect x="24" y="22" width="12" height="20" fill="var(--accent)" opacity="0"/>')
HOLDOUT_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="none" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 4"/><path d="M26 32 h12" stroke="var(--bad)" stroke-width="4"/>')
ROTATE_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 12 l8 8 l-8 8" stroke="var(--accent)" stroke-width="4" fill="none"/>')
AVG_I = icon('<rect x="10" y="40" width="10" height="14" fill="var(--accent)"/><rect x="24" y="30" width="10" height="24" fill="var(--accent)"/><rect x="38" y="20" width="10" height="34" fill="var(--accent)"/><path d="M8 28 h48" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 3"/>')

# 4. 다섯 번 돌아가며 평균을 내요
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 680, 290, "⟦5번의 시험 결과|FIVE ROUNDS OF TESTING⟧",
                      ("⟦1회차 — 1조 시험 → 92점|round 1 — group 1 tested → 92⟧", "⟦2회차 — 2조 시험 → 88점|round 2 — group 2 tested → 88⟧",
                       "⟦3회차 — 3조 시험 → 95점|round 3 — group 3 tested → 95⟧", "⟦4회차 — 4조 시험 → 90점|round 4 — group 4 tested → 90⟧",
                       "⟦5회차 — 5조 시험 → 91점|round 5 — group 5 tested → 91⟧", "⟦→ 평균 91.2점을 진짜 실력으로 봐요|→ the 91.2 average is taken as the real score⟧"), 0.9))

# 5. 계산이 더 들고, 순서가 있는 데이터엔 조심해야 해요
P5 = svg(330, '<rect width="380" height="330" fill="var(--accent-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=SWEAT + EYES, **TEACHER) + label(190, 260, "⟦다섯 번 훈련하느라 시간이 더 들어요|training five times over takes longer⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=EYES, **INSPECTOR) + label(570, 260, "⟦수확 날짜 순서가 있는 데이터는 순서를 지켜 나눠야 해요|data with a harvest-date order must be split in order⟧", 11, "var(--ink)")
         + label(380, 305, "⟦교차검증은 평가를 더 믿을 만하게 하지만, 공짜는 아니에요|cross validation makes evaluation more trustworthy, but it isn't free⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "crossval", "order": 22,
    "title": ("조를 돌아가며 시험지로 쓰는 검수반장", "The Inspector Who Rotates Which Group Becomes the Test"),
    "h1": ("<em>교차검증</em>이/가 뭐예요?", "What is <em>Cross Validation</em>?"),
    "sub": ("교차검증을, 외운 문제로 본 100점을 의심하고 조를 나눠 번갈아 '처음 보는 시험지'로 다시 시험하는 검수반장 이야기로 풀어봤어요.",
            "Cross validation, told as a story about an inspector who distrusts a 100% score on memorized questions, and instead splits the data into groups to take turns as the never-seen test."),
    "panels": [
        {"svg": P1, "alt": ("훈련 교사가 선별기를 훈련에 쓴 작물 그대로 시험해 100점을 받고 기뻐함", "The trainer tests the sorter on the very crops it trained on and gets a perfect score"),
         "caption": ("외운 문제로 시험 봐서 100점이 나왔어요.", "Testing on memorized questions scored a perfect 100."),
         "small": ("이 시험, 훈련 때 본 작물 그대로예요.", "This test used the exact same crops it trained on.")},
        {"svg": P2, "alt": ("검수반장이 외운 문제로는 당연히 100점이라며 처음 보는 작물로 다시 시험해보라고 지적함", "The inspector points out that scoring 100% on memorized questions is meaningless, and asks for a retest on unseen crops"),
         "caption": ("검수반장이 그건 진짜 시험이 아니라고 지적해요.", "The inspector points out that this wasn't a real test."),
         "small": ("훈련에 쓴 데이터로 평가하면 성적이 부풀려져요.", "Grading on the training data itself inflates the score.")},
        {"svg": P3, "hero": True, "alt": ("작물 더미가 다섯 조로 나뉘어 있고, 그중 3조가 빨간색으로 표시되어 이번 회차의 시험지 조임을 보여줌", "The crop pile is split into five groups, with group 3 highlighted red as this round's test group"),
         "caption": ("교차검증은 조를 나눠 한 조씩 번갈아 처음 보는 시험지로 써요.", "Cross validation splits into groups and rotates which one serves as the never-seen test."),
         "small": ("5번 돌아가며 전부 한 번씩 시험지가 돼요.", "It rotates five times, so every group gets a turn as the test."),
         "tricks": (4, [
             (SPLIT_I, ("조 나누기", "Split into groups"), ("데이터를 k개 조로 쪼개요", "split the data into k groups"), "calm"),
             (HOLDOUT_I, ("한 조는 숨겨두기", "Hold one group back"), ("그 조는 훈련에 안 써요", "that group never enters training")),
             (ROTATE_I, ("돌아가며 시험", "Rotate the test group"), ("모든 조가 한 번씩 시험지가 돼요", "every group gets a turn as the test"), "warm"),
             (AVG_I, ("평균 성적으로 판단", "Judge by the average"), ("한 번이 아니라 전체 평균을 봐요", "it's the overall average that counts")),
         ])},
        {"svg": P4, "alt": ("다섯 번의 회차별 시험 점수(92, 88, 95, 90, 91)와 그 평균 91.2점을 보여주는 표", "A table of five rounds' test scores (92, 88, 95, 90, 91) and their 91.2 average"),
         "caption": ("다섯 번 돌아가며 평균을 내요.", "Five rounds are averaged together."),
         "small": ("한 번의 운 좋은 점수가 아니라, 다섯 번의 평균을 진짜 실력으로 봐요.", "Not one lucky score, but the five-round average, is taken as the real skill.")},
        {"svg": P5, "alt": ("왼쪽: 다섯 번 훈련하느라 시간이 더 걸림. 오른쪽: 수확 날짜 순서가 있는 데이터는 순서를 지켜 나눠야 함", "Left: training five times over takes more time. Right: data with a harvest-date order must be split in order"),
         "caption": ("계산이 더 들고, 순서가 있는 데이터엔 조심해야 해요.", "It costs more compute, and ordered data needs special care."),
         "small": ("교차검증은 평가를 더 믿을 만하게 하지만, 공짜는 아니에요.", "Cross validation makes evaluation more trustworthy, but it isn't free.")},
    ],
    "summary": (("<b>교차검증</b> = 데이터를 <b>여러 조로 나눠</b>, 한 조씩 번갈아 <b>처음 보는 시험지</b>로 쓰고 나머지로 훈련한 뒤, <b>평균 성적</b>으로 진짜 실력을 가늠하는 방법.",
                 "<b>Cross validation</b> splits data into <b>several groups</b>, rotates which one serves as the <b>never-seen test</b> while the rest trains the model, and judges real skill by the <b>average score</b>."),
                ("k-겹 교차검증(k-fold cross validation)은 데이터를 k개 폴드로 나눠, 한 폴드씩 돌아가며 검증셋으로 쓰고 나머지 k-1개로 학습한 뒤 k번의 성능을 평균 내는 방법이에요. 훈련 데이터로만 평가해 생기는 과적합 착시(낙관적 평가)를 막아줘요. 계산 비용이 k배로 늘고, 시간 순서가 있는 데이터(시계열)에는 미래 데이터가 과거 예측에 섞이지 않도록 시간 순서를 지키는 분할(time-series split)을 따로 써야 해요.",
                 "k-fold cross validation splits data into k folds, rotating each fold as the held-out validation set while the other k-1 folds train the model, then averages performance across the k rounds. It guards against the optimistic illusion created by evaluating on the training data itself. The cost is k times the compute, and for time-ordered data (time series), you need an order-preserving split instead, so future data never leaks into predicting the past.")),
    "glossary": [
        ("k-겹 교차검증", "k-fold Cross Validation", ("조를 k개로 나누는 가장 흔한 방식.", "The most common way to split into k groups."), ("보통 k=5나 k=10을 많이 써요.", "k=5 or k=10 are the usual choices.")),
        ("검증셋", "Validation Set", ("이번 회차의 시험지 조.", "This round's test group."), ("훈련에는 절대 쓰지 않는 조예요.", "A group that never enters training.")),
        ("과적합", "Overfitting", ("외운 문제만 잘 푸는 상태.", "Only acing memorized questions."), ("교차검증이 바로 이걸 잡아내는 도구예요.", "Cross validation is precisely the tool that catches this.")),
        ("홀드아웃 검증", "Holdout Validation", ("딱 한 번만 나눠서 시험하는 간단한 방식.", "A simpler split-once, test-once approach."), ("교차검증보다 빠르지만 덜 안정적이에요.", "Faster than cross validation, but less stable.")),
        ("시계열 분할", "Time-Series Split", ("수확 날짜 순서를 지키는 특별한 나누기.", "A split that respects harvest-date order."), ('일반 교차검증을 그대로 쓰면 안 되는 대표 사례예요. → <a href="timeseries-ko.html">자세히 보기</a>', "A classic case where ordinary cross validation can't be used as-is. → <a href=\"timeseries-en.html\">see it in full</a>")),
        ("앙상블 기법", "Ensemble Methods", ("여러 조작원이 함께 판정하는 방법.", "Several operators judging together."), ('교차검증과 짝을 이뤄 자주 함께 쓰여요. → <a href="ensemble-ko.html">자세히 보기</a>', 'Often paired together with cross validation. → <a href="ensemble-en.html">see it in full</a>')),
        ("불편추정량", "Unbiased Estimator", ("치우치지 않은 저울눈금.", "A scale dial with no systematic tilt."), ('교차검증 평균 점수도 일종의 추정량이에요. → <a href="unbiasedest-ko.html">자세히 보기</a>', 'The cross-validation average is itself a kind of estimator. → <a href="unbiasedest-en.html">see it in full</a>')),
        ("AI 신뢰성", "AI Trustworthiness", ("정확도만으론 못 받는 품질인증 등급판.", "The certification board accuracy alone can't earn."), ('부풀려진 성적으로는 이 인증을 받을 수 없어요. → <a href="aitrust-ko.html">자세히 보기</a>', 'An inflated score can never earn this certification. → <a href="aitrust-en.html">see it in full</a>')),
    ],
}
