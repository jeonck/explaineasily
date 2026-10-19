from _draw import *
from _world import *


def daybars(x, y, vals, color="var(--accent)", w=28, gap=14, scale=3.2):
    """막대그래프 한 줄(일별 수확량)."""
    out = ""
    for i, v in enumerate(vals):
        h = v * scale
        bx = x + i * (w + gap)
        out += f'<rect x="{bx}" y="{y - h}" width="{w}" height="{h}" rx="3" fill="{color}"/>'
    return out


def predline(x, y, vals, color="var(--bad)", w=28, gap=14, scale=3.2):
    pts = " ".join(f"{x + i * (w + gap) + w / 2},{y - v * scale}" for i, v in enumerate(vals))
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>' + "".join(
        f'<circle cx="{x + i * (w + gap) + w / 2}" cy="{y - v * scale}" r="4" fill="{color}"/>' for i, v in enumerate(vals))


# 1. 매일 수확량이 들쭉날쭉해요
P1 = svg(320, sky(320)
         + person(130, 170, s=0.8, face=EYES, **FARMER)
         + daybars(260, 260, [18, 22, 15, 26, 20, 30, 24], "var(--accent)")
         + label(260, 280, "⟦월  화  수  목  금  토  일|Mo Tu We Th Fr Sa Su⟧", 10, "var(--muted)", "start")
         + bubble(50, 70, 200, 44, "⟦다음 주엔 얼마나 올까요?|how much will come in next week?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 305, "⟦매일 숫자가 오르내려서, 다음 날 감이 안 와요|the number bounces every day — tomorrow's a mystery⟧", 12, "var(--ink)"))

# 2. 어제 숫자만 베끼면 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=FROWN, **OPERATOR)
         + daybars(270, 250, [20, 24, 20, 24, 20, 24, 20], "var(--muted)")
         + predline(270, 250, [24, 20, 24, 20, 24, 20, 24], "var(--bad)")
         + label(380, 50, "⟦'어제가 24개였으니 오늘도 24개' — 하루 전 숫자만 베껴요|yesterday was 24, so today is 24 too — just copying one day back⟧", 12, "var(--ink)")
         + label(380, 285, "⟦빗나간 날이 많아요 — 하루 전 숫자만으론 들쭉날쭉함을 못 잡아요|it misses a lot — one prior day can't capture the ups and downs⟧", 12, "var(--bad)"))

# 3. 시계열분석(AR/MA) = 지난 며칠을 같이 보고, 최근 오차까지 보정해서 예측 (hero)
P3 = svg(360, sky(360)
         + person(130, 160, s=0.85, face=EYES, **INSPECTOR)
         + daybars(240, 280, [18, 22, 15, 26, 20, 30], "var(--accent)")
         + predline(240, 280, [19, 21, 17, 24, 22, 27, 25], "var(--good)")
         + label(380, 30, "⟦시계열분석(AR/MA) = 지난 며칠 값을 같이 보고, 최근 오차까지 보정해 다음 값을 추정하는 일|AR/MA time-series analysis = blending the last few days and correcting with recent errors to estimate the next⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦초록 점선이 예측, 막대가 실제 — 완전히 겹치진 않아요|the green dashed line is the forecast, bars are the real count — they never match exactly⟧", 12, "var(--muted)"))

AR_I = icon('<rect x="10" y="38" width="10" height="16" fill="var(--accent)"/><rect x="26" y="28" width="10" height="26" fill="var(--accent)"/><rect x="42" y="18" width="10" height="36" fill="var(--accent)"/><path d="M20 20 l34 -8" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 3"/>')
MA_I = icon('<path d="M10 40 q12 -20 22 -4 q10 16 22 -4" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="32" cy="32" r="4" fill="var(--bad)"/>')
SEASON_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="8 6"/><path d="M32 10 v10 M54 32 h-10 M32 54 v-10 M10 32 h10" stroke="var(--accent)" stroke-width="3"/>')
FADE_I = icon('<rect x="10" y="40" width="8" height="14" fill="var(--accent)" opacity="0.3"/><rect x="24" y="34" width="8" height="20" fill="var(--accent)" opacity="0.55"/><rect x="38" y="26" width="8" height="28" fill="var(--accent)" opacity="0.8"/><rect x="52" y="18" width="8" height="36" fill="var(--accent)"/>')

# 4. AR은 지난 값의 가중합, MA는 최근 오차 보정
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 330, 280, "⟦AR 부분 — 지난 값 가중합|AR PART — WEIGHTED PAST VALUES⟧",
                      ("⟦오늘 ≈ 어제×0.6 + 그제×0.3 + …|today ≈ yesterday×0.6 + day before×0.3 + …⟧",
                       "⟦최근일수록 가중치가 커요|more recent days get more weight⟧"), 0.95)
         + gradeboard(390, 30, 330, 280, "⟦MA 부분 — 최근 오차 보정|MA PART — RECENT-ERROR CORRECTION⟧",
                      ("⟦예측이 빗나간 만큼 다음 예측에 반영|how far off we were feeds into the next guess⟧",
                       "⟦오차가 계속 크면 모델을 다시 봐요|if errors stay big, revisit the model⟧"), 0.95)
         + label(380, 325, "⟦AR+MA를 합친 걸 ARMA, 계절성이 있으면 SARIMA를 써요|combine AR+MA into ARMA; add seasonality and you get SARIMA⟧", 12, "var(--ink)"))

# 5. 갑작스런 사건엔 약해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **INSPECTOR)
         + daybars(110, 250, [20, 22, 21, 23, 22], "var(--accent)") + predline(110, 250, [20, 21, 22, 22, 23], "var(--good)")
         + label(190, 270, "⟦평소엔 꽤 잘 맞아요|it tracks pretty well in calm times⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **INSPECTOR)
         + daybars(500, 250, [20, 21, 2], "var(--bad)") + label(570, 270, "⟦갑작스런 한파엔 과거 패턴이 소용없어요|a sudden cold snap makes past patterns useless⟧", 11, "var(--bad)")
         + label(380, 282, "⟦시계열분석은 '보통날'을 잘 읽을 뿐, 돌발 사건은 따로 대비해야 해요|time-series analysis reads ordinary days well — sudden events need separate planning⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "timeseries", "order": 15,
    "title": ("지난 며칠을 보고 내일을 가늠하는 검수반장", "The Inspector Who Reads the Last Few Days to Guess Tomorrow"),
    "h1": ("<em>시계열분석(AR/MA)</em>이/가 뭐예요?", "What is <em>Time-Series Analysis (AR/MA)</em>?"),
    "sub": ("시계열분석(AR/MA)을, 매일 들쭉날쭉한 수확량을 지난 며칠 값과 최근 오차로 함께 가늠하는 검수반장 이야기로 풀어봤어요.",
            "AR/MA time-series analysis, told as a story about an inspector who guesses tomorrow's harvest from the last few days' numbers and how far recent guesses missed."),
    "panels": [
        {"svg": P1, "alt": ("농부가 요일별로 들쭉날쭉한 수확량 막대그래프를 보여주며 다음 주 양을 궁금해함", "A grower shows a bar chart of day-by-day harvest counts that bounce around, wondering about next week"),
         "caption": ("매일 수확량이 들쭉날쭉해요.", "The daily harvest count bounces around."),
         "small": ("매일 숫자가 오르내려서, 다음 날 감이 안 와요.", "The number bounces every day — tomorrow's a mystery.")},
        {"svg": P2, "alt": ("선별기 조작원이 어제 숫자만 그대로 베껴 예측했지만 실제값과 자주 어긋남", "The operator just copies yesterday's number as the forecast, and it keeps missing the real value"),
         "caption": ("어제 숫자만 베끼면 틀려요.", "Just copying yesterday's number gets it wrong."),
         "small": ("하루 전 숫자만으론 들쭉날쭉함을 못 잡아요.", "One prior day can't capture the ups and downs.")},
        {"svg": P3, "hero": True, "alt": ("검수반장이 지난 며칠 막대그래프 위에 초록 점선 예측 그래프를 겹쳐 그림", "The inspector overlays a green dashed forecast line on top of the last few days' bar chart"),
         "caption": ("시계열분석(AR/MA)은 지난 며칠 값과 최근 오차를 함께 보고 다음 값을 추정해요.", "AR/MA time-series analysis estimates the next value from the last few days plus recent errors."),
         "small": ("초록 점선이 예측, 막대가 실제 — 완전히 겹치진 않아요.", "The green dashed line is the forecast, bars are the real count — they never match exactly."),
         "tricks": (4, [
             (AR_I, ("지난 값 가중합 (AR)", "Weighted past values (AR)"), ("최근일수록 더 많이 반영", "recent days count more"), "calm"),
             (MA_I, ("최근 오차 보정 (MA)", "Recent-error correction (MA)"), ("빗나간 만큼 다음 번에 반영", "misses feed into the next guess")),
             (SEASON_I, ("계절성 체크하기", "Check for seasonality"), ("명절·수확철 패턴도 봐요", "look for holiday/harvest-season patterns"), "warm"),
             (FADE_I, ("먼 과거는 약하게", "Fade out the distant past"), ("오래된 값일수록 가중치 작게", "older values get smaller weight")),
         ])},
        {"svg": P4, "alt": ("AR 부분(지난 값의 가중합)과 MA 부분(최근 오차 보정)을 나란히 설명하는 두 체크표", "Two side-by-side boards explaining the AR part (weighted past values) and the MA part (recent-error correction)"),
         "caption": ("AR은 지난 값의 가중합, MA는 최근 오차 보정이에요.", "AR is a weighted sum of past values; MA corrects using recent errors."),
         "small": ("둘을 합치면 ARMA, 계절성을 더하면 SARIMA예요.", "Combine them for ARMA; add seasonality for SARIMA.")},
        {"svg": P5, "alt": ("왼쪽: 평소엔 예측이 실제와 잘 맞음. 오른쪽: 갑작스런 한파로 수확량이 급락하자 예측이 크게 빗나감", "Left: in calm times the forecast tracks reality well. Right: a sudden cold snap crashes the harvest and the forecast misses badly"),
         "caption": ("갑작스런 사건엔 약해요.", "It's weak against sudden events."),
         "small": ("보통날은 잘 읽지만, 돌발 사건은 따로 대비해야 해요.", "It reads ordinary days well — sudden events need separate planning.")},
    ],
    "summary": (("<b>시계열분석(AR/MA)</b> = <b>지난 며칠 값을 가중치로 섞어</b> 다음 값을 추정하고(AR), <b>최근 예측이 빗나간 정도</b>까지 반영해 보정하는(MA) 예측 방법.",
                 "<b>AR/MA time-series analysis</b> blends <b>recent past values with weights</b> to estimate what's next (AR), then corrects using <b>how far recent forecasts missed</b> (MA)."),
                ("AR(AutoRegressive, 자기회귀)은 현재 값을 과거 p개 값의 선형결합으로 모델링하고, MA(Moving Average, 이동평균)는 과거 오차항(백색잡음)의 선형결합으로 모델링해요. 둘을 합치면 ARMA(p,q), 비정상 시계열을 차분해 정상화하면 ARIMA(p,d,q), 계절성을 더하면 SARIMA가 돼요. 전제는 '과거 패턴이 미래에도 유지된다'는 것이라, 구조적 변화(돌발 이벤트)에는 취약해요.",
                 "AR (AutoRegressive) models the current value as a linear combination of the past p values; MA (Moving Average) models it as a linear combination of past white-noise error terms. Together they form ARMA(p,q); differencing a non-stationary series to make it stationary gives ARIMA(p,d,q); adding seasonality gives SARIMA. The core assumption — that past patterns persist into the future — makes these models fragile against structural breaks like sudden events.")),
    "glossary": [
        ("AR(자기회귀)", "AR (AutoRegressive)", ("지난 며칠 값의 가중합.", "A weighted sum of the last few days."), ("최근 값일수록 더 크게 반영해요.", "More recent values get bigger weight.")),
        ("MA(이동평균)", "MA (Moving Average)", ("최근 예측 오차의 보정.", "A correction from recent forecast errors."), ("빗나간 만큼을 다음 예측에 더해요.", "Adds how far off you were into the next guess.")),
        ("정상성", "Stationarity", ("패턴이 시간이 지나도 안 바뀐다는 가정.", "The assumption that the pattern doesn't shift over time."), ("안 바뀌어야 AR/MA가 잘 맞아요.", "AR/MA only fits well when this holds.")),
        ("계절성", "Seasonality", ("명절·수확철처럼 되풀이되는 패턴.", "A pattern that repeats, like holidays or harvest season."), ("있으면 SARIMA처럼 계절 항을 더해요.", "If present, add a seasonal term as in SARIMA.")),
        ("회귀모형 가정", "Regression Assumptions", ("저울이 똑바로 걸려 있다는 전제들.", "The conditions that keep the scale hanging straight."), ('시계열도 회귀의 사촌이라 비슷한 전제가 깔려요. → <a href="regassumption-ko.html">저울이 똑바로 걸리는 조건</a>', 'Time series is a cousin of regression and shares similar conditions. → <a href="regassumption-en.html">what keeps the scale hanging straight</a>')),
        ("불편추정량", "Unbiased Estimator", ("치우치지 않은 저울눈금.", "A scale dial with no systematic tilt."), ('예측값을 만드는 저울 자체의 성질이에요. → <a href="unbiasedest-ko.html">치우치지 않은 저울눈금</a>', "A property of the scale that produces the forecast itself. → <a href=\"unbiasedest-en.html\">the dial with no systematic tilt</a>")),
        ("교차검증", "Cross Validation", ("조를 나눠 번갈아 시험해 보는 일.", "Splitting into groups and testing in rotation."), ('시계열 예측도 과거 구간으로 교차검증해요. → <a href="crossval-ko.html">자세히 보기</a>', 'Time-series forecasts are cross-validated over past windows too. → <a href="crossval-en.html">see it in full</a>')),
        ("강화학습", "Reinforcement Learning", ("정답표 없이 보상으로 배우는 선별기.", "A sorter that learns from rewards instead of an answer key."), ('예측과는 다른, 또 다른 학습 방식이에요. → <a href="rl-ko.html">자세히 보기</a>', 'A different style of learning from forecasting. → <a href="rl-en.html">see it in full</a>')),
    ],
}
