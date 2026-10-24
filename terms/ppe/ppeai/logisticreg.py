from _draw import *
from _world import *


def sigmoid_curve(x, y, w=220, h=120, color="var(--accent)"):
    """S자 곡선(시그모이드). (x,y) 는 왼쪽 아래 기준점."""
    return (f'<g transform="translate({x},{y})">'
            f'<path d="M0 0 H{w}" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M0 {-h} V0" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M0 {-h * 0.08:.1f} C {w * 0.32:.0f} {-h * 0.08:.1f}, {w * 0.4:.0f} {-h * 0.92:.1f}, {w * 0.5:.0f} {-h / 2:.1f} '
            f'S {w * 0.68:.0f} {-h * 0.92:.1f}, {w} {-h * 0.92:.1f}" stroke="{color}" stroke-width="4" fill="none"/>'
            f'<path d="M0 {-h / 2:.1f} H{w}" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>'
            f'{label(w + 14, -h / 2 + 4, "⟦0.5|0.5⟧", 10, "var(--bad)", "start")}</g>')


# 1. 합격·불합격, 둘 중 하나로만 답해야 해요
P1 = svg(300, sky(300)
         + label(380, 25, "⟦합격 아니면 불합격, 둘 중 하나로만 답해야 해요|it has to answer pass or fail — only one of the two⟧", 13, "var(--ink)", cls="d")
         + produce(220, 130, 1.3, "var(--good)")
         + scale_(220, 185, 1.0, level=0.65)
         + person(560, 170, s=0.8, face=EYES, **OPERATOR)
         + label(560, 275, "⟦저울 눈금은 숫자인데… 어느 쪽이죠?|the scale gives a number… but which side is it?⟧", 11, "var(--muted)"))

# 2. 왜 어려운가: 선형 점수를 그대로 확률처럼 쓰면 말이 안 되는 값이 나와요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + scale_(190, 100, 1.1, level=0.95)
         + label(190, 250, "⟦점수 130%? 확률이 100을 넘을 순 없어요|a score of 130%? a probability can't go past 100⟧", 11, "var(--bad)")
         + scale_(570, 100, 1.1, level=0.05)
         + label(570, 250, "⟦점수 -40%? 확률이 음수일 순 없어요|a score of -40%? a probability can't go negative⟧", 11, "var(--bad)")
         + label(380, 285, "⟦저울 눈금(선형 점수)을 그대로 확률처럼 쓰면, 범위를 벗어난 값이 나와요|using the scale's raw number as a probability as-is gives values outside any sane range⟧", 12, "var(--ink)", cls="d"))

# 3. 로지스틱 회귀 = 저울 눈금을 S자 곡선에 넣어 0~1 사이 합격 확률로 바꾸는 방법 (hero)
P3 = svg(340, sky(340)
         + label(380, 25, "⟦로지스틱 회귀 = 저울 눈금을 S자 곡선에 넣어 0~1 사이 합격 확률로 바꿔요|logistic regression feeds the scale's number through an S-curve, turning it into a pass probability between 0 and 1⟧", 13, "var(--ink)", cls="d")
         + scale_(90, 150, 1.0, level=0.7) + label(90, 230, "⟦저울 눈금(점수)|the scale's number (score)⟧", 11, "var(--muted)")
         + f'<path d="M160 190 H230" stroke="var(--accent)" stroke-width="4"/>'
         + sigmoid_curve(260, 300, 220, 140)
         + label(480, 320, "⟦S자 곡선(시그모이드)|the S-curve (sigmoid)⟧", 11, "var(--muted)"))

SCORE_I = icon('<rect x="28" y="6" width="8" height="40" fill="#5A3B22"/><rect x="10" y="40" width="44" height="6" fill="var(--accent)" transform="rotate(-10 32 43)"/>')
SQUASH_I = icon('<path d="M10 50 C 20 50, 24 14, 32 32 S 44 14, 54 14" stroke="var(--accent)" stroke-width="4" fill="none"/>')
THRESH_I = icon('<path d="M10 32 H54" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/><circle cx="40" cy="32" r="6" fill="var(--good)"/>')
BOUND_I = icon('<path d="M10 50 L54 14" stroke="var(--accent)" stroke-width="4"/><circle cx="20" cy="20" r="5" fill="var(--good)"/><circle cx="44" cy="44" r="5" fill="var(--bad)"/>')

PAGE = {
    "slug": "logisticreg", "order": 8,
    "title": ("저울 눈금을 S자 곡선에 넣어 보기", "Feeding the Scale's Number Through an S-Curve"),
    "h1": ("<em>로지스틱 회귀분석</em>이 뭐예요?", "What is <em>Logistic Regression</em>?"),
    "sub": ("로지스틱 회귀분석을, 저울 눈금을 S자 곡선에 넣어 합격 확률로 바꾸는 이야기로 풀어봤어요.",
            "Logistic regression, told as a story about feeding the scale's number through an S-curve to get a pass probability."),
    "panels": [
        {"svg": P1, "alt": ("작물이 저울 위에 있고, 선별기 조작원이 저울 눈금만으로는 합격인지 불합격인지 헷갈려함", "Produce sits on a scale, and the operator is unsure whether the reading means pass or fail"),
         "caption": ("합격 아니면 불합격, 둘 중 하나로만 답해야 해요.", "It has to answer pass or fail — only one of the two."),
         "small": ("저울 눈금은 숫자인데, 그 자체로는 답이 아니에요.", "The scale gives a number, but the number by itself isn't the answer.")},
        {"svg": P2, "alt": ("저울 눈금이 130%와 -40%처럼 말이 안 되는 값을 보여줌", "The scale shows nonsensical readings like 130% and −40%"),
         "caption": ("선형 점수를 그대로 확률처럼 쓰면 말이 안 돼요.", "Using the raw score directly as a probability makes no sense."),
         "small": ("확률은 0~1(0~100%) 사이여야 하는데, 점수는 그 범위를 벗어나요.", "A probability has to stay between 0 and 1 — but a raw score doesn't respect that range.")},
        {"svg": P3, "hero": True, "alt": ("저울 눈금이 화살표를 따라 S자 곡선으로 들어가 0.5 기준선과 함께 합격 확률로 바뀜", "The scale's reading flows along an arrow into an S-curve, turning into a pass probability measured against the 0.5 line"),
         "caption": ("저울 눈금을 S자 곡선에 넣어 합격 확률로 바꿔요.", "It feeds the scale's number through an S-curve to get a pass probability."),
         "small": ("이렇게 하면 점수가 아무리 크거나 작아도, 결과는 항상 0과 1 사이예요.", "No matter how big or small the score, the result always lands between 0 and 1."),
         "tricks": (4, [
             (SCORE_I, ("점수 매기기", "Score it"), ("특징을 더해 하나의 점수로 만들어요", "combining features into one score"), "calm"),
             (SQUASH_I, ("S자로 눌러주기", "Squash it with an S"), ("점수를 0~1 사이로 눌러요", "squeezing the score between 0 and 1")),
             (THRESH_I, ("기준점 넘으면 합격", "Pass the cutoff, call it PASS"), ("보통 0.5를 기준으로 삼아요", "0.5 is the usual cutoff line"), "warm"),
             (BOUND_I, ("경계선 긋기", "Draw the boundary"), ("합격과 불합격을 가르는 선이에요", "the line that splits pass from fail")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦선형 회귀 vs 로지스틱 회귀|LINEAR REGRESSION vs LOGISTIC REGRESSION⟧",
                 ("⟦선형 회귀 — 저울 눈금 그 자체(연속된 숫자)를 예측|linear regression — predicts the raw number itself (continuous)⟧",
                  "⟦로지스틱 회귀 — 합격 확률(0~1)을 예측|logistic regression — predicts a pass probability (0 to 1)⟧",
                  "⟦선형 회귀 — 예: 작물 무게 예측|linear regression — e.g. predicting produce weight⟧",
                  "⟦로지스틱 회귀 — 예: 합격·불합격 분류|logistic regression — e.g. classifying pass vs. fail⟧"), 1.0)),
         "alt": ("선형 회귀와 로지스틱 회귀를 나란히 비교한 표", "A board comparing linear regression and logistic regression side by side"),
         "caption": ("둘 다 저울을 쓰지만, 묻는 질문이 달라요.", "Both use the scale — but they're answering a different question."),
         "small": ("하나는 '얼마나'를 묻고, 하나는 '어느 쪽인지'를 물어요.", "One asks 'how much'; the other asks 'which side'.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                 + sigmoid_curve(100, 220, 160, 100) + label(180, 260, "⟦경계선은 결국 하나의 직선이에요|the boundary is still just one straight line⟧", 11, "var(--ink)")
                 + person(570, 150, s=0.75, face=EYES, **INSPECTOR) + label(570, 250, "⟦복잡하게 휜 경계는 못 그려요|can't draw a boundary that curves in complicated ways⟧", 11, "var(--ink)")
                 + label(380, 282, "⟦로지스틱 회귀는 S자로 눌러줄 뿐, 속은 여전히 직선 하나로 가르는 모델이에요|logistic regression only squashes the output — underneath, it's still one straight dividing line⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: S자 곡선과 경계선이 결국 직선 하나라는 설명. 오른쪽: 검수반장이 복잡한 경계는 못 그린다고 말함", "Left: a note that the boundary is still one straight line. Right: the inspector notes it can't draw a complicated curved boundary"),
         "caption": ("S자로 누르긴 해도, 속은 직선 하나로 가르는 모델이에요.", "It squashes with an S — but underneath, one straight line still does the dividing."),
         "small": ("더 복잡한 경계가 필요하면, 혼동행렬로 성능을 확인하며 다른 방법을 찾아야 해요.", "For a more complicated boundary, you'd check performance with a confusion matrix and reach for a different method.")},
    ],
    "summary": (("<b>로지스틱 회귀분석</b> = 저울 눈금(점수)을 <b>S자 곡선</b>에 넣어, <b>0~1 사이 합격 확률</b>로 바꾸는 방법.",
                 "<b>Logistic regression</b> = feeding the scale's <b>score through an S-curve</b> to get a <b>pass probability between 0 and 1</b>."),
                ("로지스틱 회귀분석(Logistic Regression)은 입력 특징의 선형 결합(가중합)을 시그모이드 함수에 통과시켜, 결과를 0과 1 사이의 확률로 바꾸는 지도학습 분류 방법이에요. 이 확률이 임계값(보통 0.5)을 넘으면 양성 클래스로, 아니면 음성 클래스로 분류해요. 이름에 '회귀'가 들어가지만 실제로는 분류 문제에 쓰이고, 결정 경계가 본질적으로 직선(초평면)이라 복잡하게 휜 경계를 가진 데이터에는 한계가 있어요.",
                 "Logistic regression is a supervised classification method that passes a linear combination (weighted sum) of input features through a sigmoid function, turning the result into a probability between 0 and 1. If that probability clears a threshold (usually 0.5), it's classified as the positive class; otherwise, the negative class. Despite the word 'regression' in its name, it's actually used for classification — and because its decision boundary is fundamentally a straight line (a hyperplane), it struggles with data that needs a more complicated, curved boundary.")),
    "glossary": [
        ("로지스틱 회귀", "Logistic regression", ("저울 눈금을 S자 곡선에 넣어 확률로 바꾸는 방법.", "Feeding the scale's number through an S-curve to get a probability."), ("이름과 달리 분류 문제에 쓰여요.", "Despite its name, it's used for classification.")),
        ("시그모이드 함수", "Sigmoid function", ("아무 숫자나 0~1 사이로 눌러주는 S자 곡선.", "The S-curve that squashes any number into 0 to 1."), ("로지스틱 회귀의 핵심 장치예요.", "The core mechanism of logistic regression.")),
        ("선형 회귀", "Linear regression", ("저울 눈금 자체(연속된 숫자)를 예측하는 방법.", "Predicting the raw scale number itself — a continuous value."), ("로지스틱 회귀가 빌려 쓰는 점수 매기기 방식의 원래 주인이에요.", "The original owner of the scoring method logistic regression borrows.")),
        ("결정 경계", "Decision boundary", ("합격과 불합격을 가르는 선.", "The line that splits pass from fail."), ("로지스틱 회귀에서는 이 경계가 늘 직선(또는 평면)이에요.", "In logistic regression, this boundary is always a straight line (or flat plane).")),
        ("임계값", "Threshold", ("확률을 합격·불합격으로 바꾸는 기준점.", "The cutoff that turns a probability into pass or fail."), ("보통 0.5를 쓰지만, 상황에 따라 옮길 수 있어요.", "Usually 0.5, but it can be moved depending on the situation.")),
        ("오즈비", "Odds ratio", ("합격 확률과 불합격 확률의 비.", "The ratio of the pass probability to the fail probability."), ("로지스틱 회귀의 계수를 해석할 때 쓰는 말이에요.", "The term used when interpreting a logistic regression coefficient.")),
        ("혼동행렬", "Confusion matrix", ("합격·불합격 판정을 네 칸으로 나눈 기록부.", "The ledger that splits pass/fail calls into four boxes."), ('로지스틱 회귀의 성능도 이걸로 확인해요. → <a href="confmatrix-ko.html">네 칸으로 나눈 도장 기록부</a>', "Logistic regression's own performance is checked the same way. → <a href=\"confmatrix-en.html\">The Four-Box Stamp Ledger</a>")),
        ("군집분석", "Clustering", ("정답 라벨 없이 스스로 무리를 찾는 방법.", "Finding groups on its own, with no answer labels."), ('로지스틱 회귀와 정반대 출발점을 가진 이웃 방법이에요. → <a href="clustering-ko.html">이름표 없이 비슷한 것끼리 모으기</a>', "A neighboring method that starts from the opposite assumption. → <a href=\"clustering-en.html\">Grouping by Likeness, With No Name Tags</a>")),
    ],
}
