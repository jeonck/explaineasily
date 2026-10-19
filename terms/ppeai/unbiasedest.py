from _draw import *
from _world import *

# 1. 트럭 전체를 다 못 재서 상자 하나만 저울에 올려요
P1 = svg(300, sky(300)
         + person(150, 170, s=0.8, face=EYES, **INSPECTOR)
         + scale_(280, 220, 1.1, level=0.5) + produce(240, 150, 0.7) + produce(320, 150, 0.7)
         + bubble(420, 70, 230, 50, "⟦트럭 전체를 다 잴 순 없으니, 상자 하나만 재서 평균을 가늠해요|can't weigh the whole truck — guess the average from one box⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦상자 하나로 트럭 전체 평균을 믿어도 될까요?|can one box's weight be trusted for the whole truck's average?⟧", 12, "var(--ink)"))

# 2. 고장난 저울은 항상 같은 쪽으로 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=FROWN, **INSPECTOR) + scale_(300, 210, 1.1, level=0.85)
         + label(300, 90, "⟦+100g|+100g⟧", 16, "var(--bad)", cls="d")
         + person(560, 150, s=0.75, face=EYES, **INSPECTOR) + scale_(560, 210, 1.0, level=0.85)
         + label(560, 90, "⟦또 +100g|again +100g⟧", 14, "var(--bad)", cls="d")
         + label(380, 280, "⟦이 저울은 몇 번을 재도 항상 100g씩 더 무겁게 나와요|no matter how many times you weigh, this scale always reads 100g heavy⟧", 12, "var(--ink)"))

# 3. 불편추정량 = 여러 번 재면 평균적으로 진짜 값과 같아지는 저울/방법 (hero)
P3 = svg(360, sky(360)
         + person(200, 170, s=0.9, face=SMILE, **INSPECTOR)
         + scale_(360, 230, 1.0, level=0.3) + scale_(460, 230, 1.0, level=0.6) + scale_(560, 230, 1.0, level=0.45)
         + label(380, 30, "⟦불편추정량 = 한 번은 틀려도, 여러 표본으로 여러 번 재면 평균이 진짜 값에 맞춰지는 저울|an unbiased estimator = it may miss once, but average it over many samples and it lands on the true value⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦세 번의 결과가 다 다르지만, 평균은 진짜 무게 쪽을 가리켜요|the three readings differ, but their average points right at the true weight⟧", 12, "var(--muted)"))

MANY_I = icon('<circle cx="18" cy="32" r="8" fill="var(--accent)"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/><circle cx="46" cy="32" r="8" fill="var(--accent)"/><path d="M14 48 h36" stroke="var(--good)" stroke-width="3"/>')
FORMULA_I = icon('<rect x="10" y="20" width="44" height="24" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 32 h28" stroke="#142033" stroke-width="3"/><circle cx="32" cy="24" r="3" fill="#142033"/>')
RANDOM_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="24" cy="24" r="3" fill="var(--accent)"/><circle cx="40" cy="40" r="3" fill="var(--accent)"/><circle cx="40" cy="24" r="3" fill="var(--accent)"/>')
ONESHOT_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M12 12 L52 52" stroke="var(--bad)" stroke-width="4"/>')

# 4. 나누는 숫자 하나로 치우침이 생길 수 있어요
P4 = svg(340, sky(340)
         + gradeboard(40, 40, 330, 260, "⟦치우친 공식|A BIASED FORMULA⟧",
                      ("⟦편차 제곱합 ÷ n|sum of squared deviations ÷ n⟧", "⟦표본 분산을 살짝 작게 만들어요|slightly underestimates the true spread⟧",
                       "⟦여러 번 해도 진짜 값보다 작은 쪽|averages out smaller than the truth⟧"), 0.95)
         + gradeboard(390, 40, 330, 260, "⟦불편 공식|AN UNBIASED FORMULA⟧",
                      ("⟦편차 제곱합 ÷ (n-1)|sum of squared deviations ÷ (n-1)⟧", "⟦자유도를 하나 보정해요|corrects for one degree of freedom⟧",
                       "⟦여러 번 하면 진짜 값에 맞춰져요|averages right onto the truth⟧"), 0.95))

# 5. 치우치지 않아도 흔들림은 클 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **INSPECTOR) + scale_(190, 220, 0.9, level=0.5)
         + label(190, 270, "⟦치우치진 않지만 많이 흔들려요|unbiased, but it swings a lot⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **TEACHER) + scale_(570, 220, 0.9, level=0.55)
         + label(570, 270, "⟦살짝 치우쳐도 덜 흔들리는 저울이 더 쓸모 있을 때도 있어요|a slightly biased but steadier scale can sometimes be more useful⟧", 11, "var(--ink)")
         + label(380, 282, "⟦불편성은 '치우침 없음'만 말할 뿐, 흔들림(분산)까지 보장하진 않아요|unbiasedness only promises no systematic tilt — not a small spread⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "unbiasedest", "order": 19,
    "title": ("치우치지 않은 저울눈금", "The Scale Dial With No Systematic Tilt"),
    "h1": ("<em>불편추정량</em>이/가 뭐예요?", "What is an <em>Unbiased Estimator</em>?"),
    "sub": ("불편추정량을, 한 번은 틀려도 여러 번 재면 평균이 진짜 무게로 맞춰지는 저울 이야기로 풀어봤어요.",
            "Unbiased estimators, told as a story about a scale that may miss once, but whose average lands on the true weight over many weighings."),
    "panels": [
        {"svg": P1, "alt": ("검수반장이 트럭 전체 대신 상자 하나를 저울에 올려 전체 평균 무게를 가늠하려 함", "The inspector weighs just one box instead of the whole truck, trying to guess the overall average"),
         "caption": ("트럭 전체를 다 못 재서 상자 하나만 저울에 올려요.", "Unable to weigh the whole truck, the inspector weighs just one box."),
         "small": ("상자 하나로 트럭 전체 평균을 믿어도 될까요?", "Can one box's weight be trusted for the whole truck's average?")},
        {"svg": P2, "alt": ("고장난 저울이 두 번 모두 진짜 무게보다 100g 더 무겁게 나옴", "A broken scale reads 100g heavy both times it's used"),
         "caption": ("고장난 저울은 항상 같은 쪽으로 틀려요.", "A broken scale always errs the same way."),
         "small": ("몇 번을 재도 항상 100g씩 더 무겁게 나와요.", "No matter how many times you weigh, it always reads 100g heavy.")},
        {"svg": P3, "hero": True, "alt": ("검수반장이 세 개의 저울 측정값이 서로 다르지만 평균은 진짜 무게에 맞는 것을 보고 웃음", "The inspector smiles seeing three different readings whose average matches the true weight"),
         "caption": ("불편추정량은 여러 번 재면 평균적으로 진짜 값과 같아지는 저울이에요.", "An unbiased estimator is a scale whose average over many weighings lands on the true value."),
         "small": ("세 번의 결과가 다 다르지만, 평균은 진짜 무게 쪽을 가리켜요.", "The three readings differ, but their average points right at the true weight."),
         "tricks": (4, [
             (MANY_I, ("여러 표본 평균 내기", "Average over many samples"), ("한 번이 아니라 여러 번 재요", "weigh more than once"), "calm"),
             (FORMULA_I, ("치우침 없는 공식 쓰기", "Use an unbiased formula"), ("나누는 숫자 하나가 중요해요", "the number you divide by matters")),
             (RANDOM_I, ("무작위로 뽑기", "Sample at random"), ("한쪽 상자만 골라 재면 안 돼요", "don't always pick the same box"), "warm"),
             (ONESHOT_I, ("한 번으로 판단 안 하기", "Don't judge from just one reading"), ("한 번은 틀려도 괜찮아요", "it's fine if a single reading misses")),
         ])},
        {"svg": P4, "alt": ("편차 제곱합을 n으로 나누는 치우친 공식과 n-1로 나누는 불편 공식을 나란히 비교함", "A biased formula dividing by n and an unbiased formula dividing by n-1 are compared side by side"),
         "caption": ("나누는 숫자 하나로 치우침이 생길 수 있어요.", "A single number you divide by can create bias."),
         "small": ("표본 분산은 n-1로 나눠야 치우치지 않아요(자유도 보정).", "Sample variance needs n-1, not n, to stay unbiased — a degrees-of-freedom correction.")},
        {"svg": P5, "alt": ("왼쪽: 치우치지 않지만 결과가 크게 흔들리는 저울. 오른쪽: 살짝 치우쳤지만 덜 흔들리는 저울", "Left: an unbiased scale whose readings swing widely. Right: a slightly biased scale that swings less"),
         "caption": ("치우치지 않아도 흔들림은 클 수 있어요.", "Being unbiased doesn't rule out a wide swing."),
         "small": ("불편성은 치우침 없음만 말할 뿐, 흔들림까지 보장하진 않아요.", "Unbiasedness only promises no systematic tilt — not a small spread.")},
    ],
    "summary": (("<b>불편추정량</b> = 한 번의 측정은 틀릴 수 있어도, <b>여러 표본으로 반복하면 평균이 진짜 값과 같아지는</b> 추정 방법.",
                 "An <b>unbiased estimator</b> may miss on any single try, but <b>averaged over many samples, it lands on the true value</b>."),
                ("통계학에서 추정량 θ̂의 기댓값 E[θ̂]이 모수(참값) θ와 같으면 불편추정량이라 해요. 표본평균은 모평균의 불편추정량이지만, 표본분산은 n으로 나누면 치우치므로 n-1로 나눠(베셀 보정) 불편추정량을 만들어요. 불편성은 '치우침 없음'만 보장하고 분산(효율성)은 별개라, 실무에서는 약간의 편향을 감수하고 분산을 줄이는 추정량(편향-분산 트레이드오프)을 쓰기도 해요.",
                 "In statistics, an estimator θ̂ is unbiased if its expected value E[θ̂] equals the true parameter θ. The sample mean is an unbiased estimator of the population mean, but the naive sample variance (dividing by n) is biased — dividing by n-1 instead (Bessel's correction) makes it unbiased. Unbiasedness only guarantees no systematic tilt, which is separate from variance (efficiency); in practice, estimators that trade a little bias for less variance are sometimes preferred — the bias-variance tradeoff.")),
    "glossary": [
        ("추정량", "Estimator", ("표본으로 참값을 가늠하는 저울.", "The scale that guesses the truth from a sample."), ("공식 하나하나가 추정량이에요.", "Each formula you use is itself an estimator.")),
        ("모수", "Parameter", ("트럭 전체의 진짜 평균 무게.", "The true average weight of the whole truck."), ("우리가 영영 직접 못 보는 참값이에요.", "The true value we can never directly see.")),
        ("표본평균", "Sample Mean", ("상자 하나의 평균 무게.", "The average weight of one box."), ("모평균의 대표적인 불편추정량이에요.", "The classic unbiased estimator of the population mean.")),
        ("자유도 보정(n-1)", "Degrees-of-Freedom Correction", ("나누는 숫자를 하나 줄이는 보정.", "Shaving one off the number you divide by."), ("표본분산을 불편하게 만들어요.", "Makes the sample variance unbiased.")),
        ("편향-분산 트레이드오프", "Bias-Variance Tradeoff", ("안 치우침과 안 흔들림 사이의 줄다리기.", "The tug-of-war between no tilt and no swing."), ("둘 다 완벽히 가지기는 어려워요.", "Having both perfectly is rarely possible.")),
        ("회귀모형 가정", "Regression Assumptions", ("저울이 똑바로 걸리는 조건들.", "The conditions that keep the scale hanging straight."), ('불편추정량이 성립하려면 이 가정들이 필요해요. → <a href="regassumption-ko.html">자세히 보기</a>', 'These conditions are what make the unbiased estimator hold. → <a href="regassumption-en.html">see it in full</a>')),
        ("교차검증", "Cross Validation", ("조를 나눠 번갈아 시험해 보는 일.", "Splitting into groups and testing in rotation."), ('모형 성능을 반복해서 가늠한다는 점이 비슷해요. → <a href="crossval-ko.html">자세히 보기</a>', 'Shares the idea of repeated estimation. → <a href="crossval-en.html">see it in full</a>')),
        ("시계열분석(AR/MA)", "Time-Series Analysis (AR/MA)", ("지난 며칠 값으로 내일을 가늠하는 저울.", "A scale that guesses tomorrow from the last few days."), ('예측값을 만드는 저울도 불편성을 따져요. → <a href="timeseries-ko.html">자세히 보기</a>', 'The scale behind a forecast is checked for bias too. → <a href="timeseries-en.html">see it in full</a>')),
    ],
}
