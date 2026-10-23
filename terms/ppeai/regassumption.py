from _draw import *
from _world import *

# 1. 무게로 가격을 예측하는 저울을 걸었어요
P1 = svg(300, sky(300)
         + person(160, 170, s=0.8, face=SMILE, **TEACHER)
         + scale_(320, 220, 1.2, level=0.5)
         + label(320, 280, "⟦무게가 오르면 가격도 오른다 — 저울 하나로 예측|more weight, more price — one scale predicts it⟧", 12, "var(--ink)")
         + bubble(500, 90, 220, 46, "⟦이 저울, 아무 때나 믿어도 되나요?|can I trust this scale no matter what?⟧", 11, "var(--panel)", "var(--line)", "bottom"))

# 2. 저울이 어떤 상황에선 엉뚱하게 흔들려요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + scale_(220, 210, 1.1, level=0.2) + label(220, 270, "⟦가벼울 땐 조용히 맞아요|light loads sit still and match⟧", 11, "var(--ink)")
         + scale_(500, 210, 1.3, level=0.9) + label(500, 270, "⟦무거워지면 확 흔들려요|heavy loads make it swing wildly⟧", 11, "var(--bad)")
         + label(380, 60, "⟦무게 구간마다 흔들리는 정도가 달라요 — 저울을 걸 때 지켜야 할 조건이 있어요|how much it wobbles changes by weight range — the scale needs certain conditions to hold⟧", 12, "var(--ink)"))

# 3. 회귀모형 가정 = 저울이 똑바로 걸리기 위한 네 가지 조건 (hero)
P3 = svg(360, sky(360)
         + scale_(220, 200, 1.3, level=0.45)
         + gradeboard(380, 50, 300, 230, "⟦저울을 똑바로 거는 조건|CONDITIONS FOR A STRAIGHT SCALE⟧",
                      ("⟦① 선형성 — 관계가 직선이어야|① linearity — the relation is a straight line⟧", "⟦② 독립성 — 오차끼리 안 엮여야|② independence — errors don't entangle⟧",
                       "⟦③ 등분산성 — 흔들림 크기가 일정해야|③ equal variance — the wobble stays the same size⟧", "⟦④ 정규성 — 오차가 고르게 퍼져야|④ normality — errors spread out evenly⟧"), 0.9)
         + label(380, 28, "⟦회귀모형 가정 = 이 저울의 예측을 믿기 위해 지켜야 할 네 가지 전제|regression assumptions = four conditions the scale's prediction must meet to be trusted⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦네 조건이 다 지켜져야 예측과 신뢰구간을 믿을 수 있어요|only when all four hold can the prediction and its confidence interval be trusted⟧", 12, "var(--muted)"))

LINE_I = icon('<path d="M10 50 L54 14" stroke="var(--accent)" stroke-width="4"/><circle cx="18" cy="44" r="3" fill="var(--good)"/><circle cx="32" cy="30" r="3" fill="var(--good)"/><circle cx="46" cy="18" r="3" fill="var(--good)"/>')
INDEP_I = icon('<circle cx="18" cy="24" r="4" fill="var(--accent)"/><circle cx="34" cy="40" r="4" fill="var(--accent)"/><circle cx="48" cy="18" r="4" fill="var(--accent)"/><circle cx="28" cy="50" r="4" fill="var(--accent)"/>')
FUNNEL_I = icon('<path d="M10 50 L54 14" stroke="var(--accent)" stroke-width="3"/><path d="M16 46 l4 6 M32 32 l8 10 M46 20 l12 14" stroke="var(--bad)" stroke-width="2.5"/>')
BELL_I = icon('<path d="M10 48 Q32 10 54 48" stroke="var(--accent)" stroke-width="4" fill="none"/>')

# 4. 네 조건이 깨지면 어떻게 보이나
P4 = svg(340, sky(340)
         + gradeboard(40, 20, 330, 300, "⟦선형성 · 독립성 깨짐|BROKEN LINEARITY · INDEPENDENCE⟧",
                      ("⟦관계가 휘어 있으면 직선 저울이 틀려요|a curved relation fools a straight-line scale⟧",
                       "⟦어제 오차가 오늘 오차와 엮이면(시계열) 안 돼요|if yesterday's error entangles with today's (time series), it fails⟧"), 0.95)
         + gradeboard(390, 20, 330, 300, "⟦등분산성 · 정규성 깨짐|BROKEN EQUAL VARIANCE · NORMALITY⟧",
                      ("⟦무게가 늘수록 흔들림도 커지면(깔때기 모양) 안 돼요|if wobble grows with weight (a funnel shape), it fails⟧",
                       "⟦오차가 한쪽으로 몰리면 신뢰구간이 비뚤어져요|errors piling to one side skews the confidence interval⟧"), 0.95))

# 5. 가정이 깨져도 숫자는 나오지만, 믿을 수는 없어요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + scale_(190, 180, 1.0, level=0.6) + label(190, 260, "⟦예측 숫자는 늘 나와요|a predicted number always comes out⟧", 11, "var(--ink)")
         + person(570, 125, s=0.8, face=EYES, **INSPECTOR) + label(570, 265, "⟦근데 그 숫자를 얼마나 믿을지는 가정이 지켜졌는지에 달렸어요|but how much to trust it depends on whether the conditions held⟧", 11, "var(--ink)")
         + label(380, 300, "⟦가정이 깨지면 예측값은 나와도, 오차범위·검정은 믿을 수 없어요|break the assumptions and a number still comes out — but the error range and tests can't be trusted⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "regassumption", "order": 20,
    "title": ("저울을 똑바로 걸기 위한 네 가지 조건", "The Four Conditions for Hanging the Scale Straight"),
    "h1": ("<em>회귀모형 가정</em>이/가 뭐예요?", "What are <em>Regression Assumptions</em>?"),
    "sub": ("회귀모형 가정을, 무게로 가격을 예측하는 저울을 똑바로 걸기 위해 지켜야 할 네 가지 조건 이야기로 풀어봤어요.",
            "Regression assumptions, told as a story about four conditions a weight-to-price scale must meet to hang straight and be trusted."),
    "panels": [
        {"svg": P1, "alt": ("훈련 교사가 무게로 가격을 예측하는 저울을 걸고, 검수반장이 아무 때나 믿어도 되는지 물음", "The trainer sets up a scale that predicts price from weight, and the inspector asks whether it can always be trusted"),
         "caption": ("무게로 가격을 예측하는 저울을 걸었어요.", "A scale was set up to predict price from weight."),
         "small": ("이 저울, 아무 때나 믿어도 되나요?", "Can I trust this scale no matter what?")},
        {"svg": P2, "alt": ("가벼운 작물에선 저울이 조용히 맞지만, 무거운 작물에선 크게 흔들림", "The scale sits still and matches for light crops, but swings wildly for heavy ones"),
         "caption": ("저울이 어떤 상황에선 엉뚱하게 흔들려요.", "In some situations the scale swings off in strange ways."),
         "small": ("무게 구간마다 흔들리는 정도가 달라요 — 저울을 걸 때 지켜야 할 조건이 있어요.", "How much it wobbles changes by weight range — the scale needs certain conditions to hold.")},
        {"svg": P3, "hero": True, "alt": ("저울 옆에 선형성·독립성·등분산성·정규성 네 조건을 적은 체크판이 걸려 있음", "Beside the scale hangs a board listing four conditions: linearity, independence, equal variance, normality"),
         "caption": ("회귀모형 가정은 저울이 똑바로 걸리기 위한 네 가지 조건이에요.", "Regression assumptions are four conditions that keep the scale hanging straight."),
         "small": ("네 조건이 다 지켜져야 예측과 신뢰구간을 믿을 수 있어요.", "Only when all four hold can the prediction and its confidence interval be trusted."),
         "tricks": (4, [
             (LINE_I, ("선형성", "Linearity"), ("관계가 곡선이 아니라 직선이어야 해요", "the relation must be a straight line, not a curve"), "calm"),
             (INDEP_I, ("독립성", "Independence"), ("오차끼리 서로 엮이면 안 돼요", "errors must not entangle with each other")),
             (FUNNEL_I, ("등분산성", "Equal Variance"), ("흔들림 크기가 구간마다 같아야 해요", "the wobble size must stay the same across ranges"), "warm"),
             (BELL_I, ("정규성", "Normality"), ("오차가 종모양으로 고르게 퍼져야 해요", "errors should spread out in a bell-shaped curve")),
         ])},
        {"svg": P4, "alt": ("선형성·독립성이 깨진 모습과 등분산성·정규성이 깨진 모습을 각각 보여줌", "Shows what broken linearity/independence looks like, and what broken equal-variance/normality looks like"),
         "caption": ("네 조건이 깨지면 이렇게 보여요.", "This is what it looks like when each condition breaks."),
         "small": ("휘어진 관계, 엮인 오차, 깔때기 모양, 한쪽으로 몰린 오차 — 전부 신호예요.", "A curved relation, entangled errors, a funnel shape, lopsided errors — each is a warning sign.")},
        {"svg": P5, "alt": ("저울은 어떤 상황에서도 예측 숫자를 내놓지만, 검수반장은 그 숫자의 신뢰 여부는 가정이 지켜졌는지에 달렸다고 말함", "The scale always outputs a predicted number, but the inspector notes how much to trust it depends on whether the conditions held"),
         "caption": ("가정이 깨져도 숫자는 나오지만, 믿을 수는 없어요.", "Break the assumptions and a number still comes out — but it can't be trusted."),
         "small": ("오차범위·검정은 가정이 지켜졌을 때만 믿을 수 있어요.", "The error range and significance tests are only trustworthy when the assumptions hold.")},
    ],
    "summary": (("<b>회귀모형 가정</b> = 예측 저울을 믿으려면 지켜야 할 <b>선형성·독립성·등분산성·정규성</b> 네 조건. 깨져도 숫자는 나오지만, 믿을 순 없어요.",
                 "<b>Regression assumptions</b> are the four conditions — <b>linearity, independence, equal variance (homoscedasticity), and normality</b> — a prediction scale must meet to be trusted. Break them, and a number still comes out, but it can't be trusted."),
                ("선형회귀가 유효하려면 ① 선형성(독립변수와 종속변수의 관계가 선형), ② 오차의 독립성(자기상관 없음), ③ 등분산성(오차의 분산이 일정, homoscedasticity), ④ 오차의 정규성을 만족해야 해요. 가정이 깨지면 계수 추정치 자체는 계산되지만, 표준오차·신뢰구간·유의성 검정(p-value)이 왜곡돼 잘못된 결론으로 이어질 수 있어요. 잔차 플롯으로 점검하고, 깨졌다면 변수 변환·강건 표준오차·다른 모형을 고려해요.",
                 "Linear regression needs ① linearity (the relationship between predictors and outcome is linear), ② independence of errors (no autocorrelation), ③ homoscedasticity (constant error variance), and ④ normality of errors. If these break, the coefficient estimates still compute, but standard errors, confidence intervals, and p-values become distorted, leading to wrong conclusions. Check with residual plots, and if assumptions fail, consider variable transformations, robust standard errors, or a different model.")),
    "glossary": [
        ("선형성", "Linearity", ("관계가 곡선이 아니라 직선이라는 전제.", "The assumption that the relation is straight, not curved."), ("깨지면 비선형 모형이나 변수 변환을 써요.", "If it breaks, use a nonlinear model or transform the variables.")),
        ("등분산성", "Homoscedasticity", ("흔들림 크기가 구간마다 같다는 전제.", "The assumption that the wobble stays the same size across ranges."), ("깨지면 깔때기 모양 잔차가 나타나요.", "Breaking it shows up as a funnel-shaped residual plot.")),
        ("자기상관", "Autocorrelation", ("어제 오차가 오늘 오차와 엮이는 것.", "Yesterday's error entangling with today's."), ('시계열 데이터에서 독립성 가정이 깨지는 대표 사례예요. → <a href="timeseries-ko.html">자세히 보기</a>', 'A classic way independence breaks in time-series data. → <a href="timeseries-en.html">see it in full</a>')),
        ("잔차", "Residual", ("저울이 예측한 값과 실제 값의 차이.", "The gap between what the scale predicts and the real value."), ("잔차 패턴을 보면 가정이 깨졌는지 알 수 있어요.", "Its pattern reveals whether an assumption has broken.")),
        ("다중공선성", "Multicollinearity", ("두 변수가 사실상 같은 말을 하는 것.", "Two variables effectively saying the same thing."), ("회귀 계수 해석을 어렵게 만드는 또 다른 문제예요.", "A separate problem that muddies how coefficients are read.")),
        ("불편추정량", "Unbiased Estimator", ("치우치지 않은 저울눈금.", "A scale dial with no systematic tilt."), ('가정이 지켜져야 추정량의 불편성도 성립해요. → <a href="unbiasedest-ko.html">자세히 보기</a>', "The assumptions are what let the estimator's unbiasedness hold. → <a href=\"unbiasedest-en.html\">see it in full</a>")),
        ("앙상블 기법", "Ensemble Methods", ("여러 조작원이 함께 판정하는 방법.", "Several operators judging together."), ('가정이 깨진 경우 대안으로 쓰이기도 해요. → <a href="ensemble-ko.html">자세히 보기</a>', 'Sometimes used as an alternative when assumptions break. → <a href="ensemble-en.html">see it in full</a>')),
        ("교차검증", "Cross Validation", ("조를 나눠 번갈아 시험해 보는 일.", "Splitting into groups and testing in rotation."), ('가정이 깨졌는지와 별개로, 모형 성능은 이걸로 확인해요. → <a href="crossval-ko.html">자세히 보기</a>', 'Separate from assumption checks, this verifies model performance. → <a href="crossval-en.html">see it in full</a>')),
    ],
}
