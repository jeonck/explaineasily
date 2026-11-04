from math import exp

from _draw import *
from _world import *


def curve(fn, x0, x1, color="var(--stone-dark)", width=3):
    """fn(x)=화면 y 인 오판 점수 곡선. 점을 같은 fn 으로 찍으면 곡선 위에 정확히 놓인다."""
    pts = " ".join(f"{x},{fn(x):.1f}" for x in range(x0, x1 + 1, 6))
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def steps(fn, xs, color="var(--good)", last="var(--accent)", dash="4 3"):
    """곡선 위 발자국: 점선으로 이어진 점들, 마지막 점만 다른 색."""
    pts = " ".join(f"{x},{fn(x):.1f}" for x in xs)
    dots = "".join(f'<circle cx="{x}" cy="{fn(x):.1f}" r="{7 if x == xs[-1] else 5}" fill="{last if x == xs[-1] else color}"/>' for x in xs)
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-dasharray="{dash}"/>' + dots


def dial(x, y, ang=-40, r=22):
    """선별기 다이얼 하나(파라미터 하나)."""
    return (f'<g transform="translate({x},{y})"><circle r="{r}" fill="var(--panel)" stroke="var(--accent)" stroke-width="4"/>'
            f'<path d="M0 0 V{4 - r}" stroke="var(--ink)" stroke-width="4" stroke-linecap="round" transform="rotate({ang})"/></g>')


def bowl(x):
    return 262 - 170 * ((x - 480) / 280) ** 2


def bowl_left(x):
    return 240 - 130 * ((x - 190) / 130) ** 2


def bowl_right(x):
    return 240 - 130 * ((x - 570) / 130) ** 2


def two_valleys(x):
    return 90 + 110 * exp(-(((x - 230) / 70) ** 2)) + 180 * exp(-(((x - 560) / 90) ** 2))


SLOPE_I = icon('<path d="M10 14 L54 50" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M40 50 h14 v-14" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
TURN_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 32 L44 20" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>')
RATE_I = icon('<path d="M10 50 L26 50" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M34 50 L58 50" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
FLAT_I = icon('<path d="M10 40 h44" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M24 30 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 다이얼이 잔뜩인데 어느 쪽으로 돌려야 오판이 줄지 안 보여요
P1 = svg(300, sky(300)
         + person(90, 130, s=0.85, face=SWEAT + EYES, **TEACHER)
         + bubble(130, 36, 370, 46, "⟦다이얼이 이렇게 많은데, 어느 쪽으로 돌려야 오판이 줄죠?|so many dials — which way should I turn to cut the misses?⟧", 11, "var(--panel)", "var(--line)", "left")
         + dial(240, 180) + dial(305, 180, 30) + dial(370, 180, 80)
         + label(305, 228, "⟦선별기 다이얼(파라미터)|the sorter's dials (parameters)⟧", 11, "var(--muted)")
         + gradeboard(470, 110, 240, 90, "⟦오판 점수판|MISS SCOREBOARD⟧", ("⟦이번 판 오판 38개|38 misses this round⟧",))
         + label(380, 276, "⟦위치를 다 시험해 볼 수는 없으니, 오판이 줄어드는 방향을 찾아야 해요|trying every setting is impossible, so we need the direction that cuts misses⟧", 12, "var(--ink)", cls="d"))

# 2. 아무 쪽으로나 돌리면 오판이 오히려 늘 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(110, 110, s=0.85, face=FROWN, **TEACHER)
         + dial(290, 160, 120)
         + label(290, 205, "⟦아무 쪽으로나 돌렸어요|turned it any which way⟧", 11, "var(--muted)")
         + gradeboard(440, 80, 250, 110, "⟦오판 점수판|MISS SCOREBOARD⟧", ("⟦돌리기 전 오판 38개|38 misses before⟧", "⟦돌린 뒤 오판 52개|52 misses after⟧"), hl=1)
         + label(380, 250, "⟦오판을 줄이려고 돌렸는데, 오히려 더 늘었어요|meant to cut the misses, but the count went up⟧", 13, "var(--bad)")
         + label(380, 280, "⟦방향을 모르면, 다이얼을 돌릴수록 오판이 더 늘 수 있어요|without knowing the direction, more turning can mean more misses⟧", 12, "var(--ink)", cls="d"))

# 3. 경사하강법 = 오판 점수의 기울기를 재서, 줄어드는 쪽으로 다이얼을 조금씩 (hero)
P3 = svg(340, sky(340)
         + label(380, 24, "⟦경사하강법 = 오판 점수의 기울기를 재서, 줄어드는 쪽으로 다이얼을 조금씩 돌리기|gradient descent = measure the miss score's slope, and turn the dial a little toward fewer misses⟧", 12, "var(--ink)", cls="d")
         + person(40, 130, s=0.75, face=EYES, **TEACHER)
         + label(130, 62, "⟦오판 점수(손실)|miss score (loss)⟧", 11, "var(--muted)")
         + curve(bowl, 190, 720)
         + steps(bowl, [225, 285, 335, 378, 412, 438])
         + label(500, 205, "⟦기울기가 거의 0이면 멈춰요|stop when the slope is nearly zero⟧", 11, "var(--good)")
         + label(450, 290, "⟦다이얼 위치(파라미터)|dial position (parameter)⟧", 11, "var(--muted)")
         + label(380, 322, "⟦오르막 반대쪽으로 조금씩 돌리다가, 오판 점수가 더 안 줄면 멈춰요|turn a little away from the uphill side, and stop when the miss score stops falling⟧", 11, "var(--muted)"))

# 4. 한 번에 돌리는 크기(학습률)
P4 = svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + label(190, 30, "⟦한 번에 너무 크게 돌리면|turning too far at once⟧", 13, "var(--ink)", cls="d")
         + curve(bowl_left, 70, 310)
         + steps(bowl_left, [120, 245, 110, 285], "var(--bad)", "var(--bad)", "6 4")
         + label(190, 274, "⟦최저점을 자꾸 지나쳐 오판이 잘 안 줄어요|keeps overshooting the low point, so misses barely fall⟧", 11, "var(--bad)")
         + label(570, 30, "⟦조금씩 돌리면|turning a little at a time⟧", 13, "var(--ink)", cls="d")
         + curve(bowl_right, 450, 690)
         + steps(bowl_right, [470, 492, 510, 524, 536, 546])
         + label(570, 274, "⟦느리지만 오판이 꾸준히 줄어요|slow, but misses keep falling⟧", 11, "var(--good)")
         + label(380, 310, "⟦그래서 학습률(한 번에 돌리는 크기)을 너무 크지도 작지도 않게 정해요|so set the learning rate (how far each turn goes) neither too big nor too small⟧", 11, "var(--ink)", cls="d"))

# 5. 작은 골짜기를 최저점으로 착각할 수 있어요
P5 = svg(320, sky(320)
         + curve(two_valleys, 90, 730)
         + steps(two_valleys, [150, 180, 205, 230])
         + person(26, 104, s=0.6, face=SMILE, **TEACHER)
         + bubble(30, 28, 280, 40, "⟦여기가 오판이 제일 적은 위치네요!|this must be the setting with the fewest misses!⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(230, 232, "⟦지역 최솟값|local minimum⟧", 11, "var(--muted)")
         + label(540, 56, "⟦오판이 더 적은 위치는 따로 있어요|a setting with even fewer misses lies elsewhere⟧", 12, "var(--bad)")
         + '<path d="M560 70 V258" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 3"/>'
         + f'<circle cx="560" cy="{two_valleys(560):.1f}" r="7" fill="var(--bad)"/>'
         + label(560, 292, "⟦전역 최솟값|global minimum⟧", 11, "var(--muted)")
         + label(380, 312, "⟦지금 위치 근처의 기울기만 따라가면, 더 깊은 골짜기를 못 볼 수 있어요|following only the slope near the current spot can miss a deeper valley elsewhere⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "gradientdescent", "order": 24,
    "title": ("오판이 줄어드는 쪽으로 다이얼 돌리기", "Turning the Dial Toward Fewer Misses"),
    "h1": ("<em>경사하강법</em>이 뭐예요?", "What is <em>Gradient Descent</em>?"),
    "sub": ("경사하강법을, 훈련 교사가 오판 점수의 기울기를 재서 줄어드는 쪽으로 선별기 다이얼을 조금씩 돌리는 이야기로 풀어봤어요.",
            "Gradient descent, told as a story about a teacher who measures the slope of the sorter's miss score and turns its dials, little by little, toward fewer misses."),
    "panels": [
        {"svg": P1, "alt": ("훈련 교사가 선별기 다이얼 여러 개와 오판 38개라고 적힌 점수판 앞에서 어느 쪽으로 돌릴지 몰라 진땀을 흘림", "The teacher sweats in front of several sorter dials and a scoreboard reading 38 misses, unsure which way to turn"),
         "caption": ("선별기 다이얼을 어느 쪽으로 돌려야 오판이 줄어들지 안 보여요.", "The teacher can't see which way to turn the sorter's dials to cut the misses."),
         "small": ("다이얼 위치를 다 시험해 볼 수는 없으니, 오판이 줄어드는 방향을 찾아야 해요.", "Trying every dial setting is impossible, so the teacher needs the direction that cuts misses.")},
        {"svg": P2, "alt": ("훈련 교사가 다이얼을 아무 쪽으로나 돌렸더니 오판이 38개에서 52개로 늘어 얼굴을 찌푸림", "The teacher frowns after turning a dial at random, as misses climb from 38 to 52"),
         "caption": ("다이얼을 아무 쪽으로나 돌리면 오판이 오히려 늘 수 있어요.", "Turning a dial at random can even raise the number of misses."),
         "small": ("방향을 모르면, 다이얼을 돌릴수록 오판이 더 늘 수 있어요.", "Without knowing the direction, more turning can mean more misses.")},
        {"svg": P3, "hero": True, "alt": ("가로축이 다이얼 위치, 세로축이 오판 점수인 곡선 위에서 점들이 내리막을 따라 가장 낮은 곳 가까이로 이어짐", "On a curve of miss score against dial position, a trail of dots follows the downhill toward the lowest point"),
         "caption": ("경사하강법은 오판 점수(손실)의 기울기를 재서, 점수가 줄어드는 쪽으로 다이얼(파라미터)을 조금씩 돌리며 오차를 줄이는 방법이에요.", "Gradient descent measures the slope of the miss score (loss) and turns the dials (parameters) a little toward a lower score, cutting the model's error bit by bit."),
         "small": ("오르막 반대쪽으로 조금씩 돌리다가, 오판 점수가 더 안 줄면 멈춰요.", "Turn a little away from the uphill side, and stop when the miss score stops falling."),
         "tricks": (4, [
             (SLOPE_I, ("기울기 재기", "Measure the slope"), ("다이얼을 돌리면 점수가 어떻게 변할지 계산해요", "calculates how the score changes as a dial turns"), "calm"),
             (TURN_I, ("기울기 반대로 돌리기", "Turn against the slope"), ("기울기 반대쪽이 점수가 줄어드는 쪽이에요", "the score falls in the opposite direction from the slope"), "warm"),
             (RATE_I, ("돌리는 크기 정하기(학습률)", "Set the turn size (learning rate)"), ("너무 크면 지나치고, 너무 작으면 느려요", "too big overshoots, too small is slow")),
             (FLAT_I, ("더 안 줄면 멈추기", "Stop when it stops falling"), ("기울기가 거의 0이면 멈춰요", "a near-zero slope means stop")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 다이얼을 너무 크게 돌려 점이 곡선 양쪽을 오가며 최저점을 지나침. 오른쪽: 조금씩 돌려 점이 느리지만 꾸준히 내려감", "Left: turning too far makes the dots bounce across the curve, overshooting the low point. Right: small turns move the dots down slowly but steadily"),
         "caption": ("다이얼을 한 번에 돌리는 크기(학습률)가 너무 크면 최저점을 지나치고, 너무 작으면 오래 걸려요.", "If each turn of the dial (the learning rate) is too big, it overshoots the low point; too small, and it takes far too long."),
         "small": ("그래서 학습률을 너무 크지도 작지도 않게 정해요.", "So the learning rate is set neither too big nor too small.")},
        {"svg": P5, "alt": ("교사가 작은 골짜기를 오판이 가장 적은 위치로 믿지만, 곡선 오른쪽에 더 깊은 골짜기가 따로 있음", "The teacher believes a shallow dip has the fewest misses, but a deeper valley sits farther along the curve"),
         "caption": ("작은 골짜기(지역 최솟값)를 오판이 가장 적은 위치로 착각할 수 있어요.", "A shallow dip (a local minimum) can be mistaken for the setting with the fewest misses."),
         "small": ("경사하강법은 지금 위치 근처의 기울기만 따라가서, 더 깊은 골짜기를 못 볼 수 있어요.", "Gradient descent follows only the slope near the current spot, so it can miss a deeper valley elsewhere.")},
    ],
    "summary": (("<b>경사하강법</b> = 지금 위치에서 손실의 <b>기울기(경사)</b>를 재서, 그 <b>반대 방향으로 조금씩</b> 파라미터를 고치기를 반복하며 손실이 낮은 곳을 찾아가는 방법.",
                 "<b>Gradient descent</b> = measuring the <b>slope (gradient)</b> of the loss at the current point, then changing the parameters a <b>little in the opposite direction</b>, repeatedly, to reach a point of lower loss."),
                ("경사하강법은 손실함수(모델이 얼마나 틀렸는지 나타내는 함수)의 기울기(gradient)를 계산해, 그 반대 방향으로 학습률(learning rate)만큼 파라미터를 조금씩 갱신하며 손실을 줄여가는 최적화 알고리즘이에요. 학습률이 너무 크면 최솟값 주변을 오가거나 발산하고, 너무 작으면 수렴이 지나치게 느려요. 손실 곡면이 볼록하지 않으면 지역 최솟값이나 안장점(기울기가 0이지만 최솟값이 아닌 곳) 근처에 머물러 전역 최솟값을 놓칠 수 있어요. 실무에서는 데이터 일부(미니배치)만으로 기울기를 재는 확률적 경사하강법(SGD)과 그 변형이 널리 쓰여요.",
                 "Gradient descent is an optimization algorithm that computes the gradient of a loss function (how wrong the model currently is), then updates the parameters a little in the opposite direction, by an amount set by the learning rate, repeatedly reducing the loss. Too large a learning rate makes the process oscillate around the minimum or diverge; too small makes convergence painfully slow. When the loss surface isn't convex, the process can settle near a local minimum or a saddle point (where the gradient is zero but it isn't a minimum) and miss the global minimum. In practice, stochastic gradient descent (SGD), which computes the gradient from only part of the data (a mini-batch), and its variants are widely used.")),
    "glossary": [
        ("경사하강법", "Gradient Descent", ("오판 점수가 줄어드는 쪽으로 다이얼을 조금씩 돌리는 방법.", "Turning the dials a little at a time toward a lower miss score."), ('신경망 학습에 널리 쓰이는 최적화 방법이에요. → <a href="cnn-ko.html">작은 창으로 조금씩 살펴보는 눈</a>', 'A widely used way to train neural networks. → <a href="cnn-en.html">The Eye That Scans Through a Small Window</a>')),
        ("기울기", "Gradient", ("다이얼을 돌릴 때 오판 점수가 어느 쪽으로, 얼마나 빨리 변하는지.", "Which way, and how fast, the miss score changes as a dial turns."), ("기울기의 반대 방향이 점수가 줄어드는 쪽이에요.", "The score falls in the opposite direction from the gradient.")),
        ("학습률", "Learning Rate", ("다이얼을 한 번에 돌리는 크기.", "How far the dial turns in a single step."), ("크면 지나치고, 작으면 너무 오래 걸려요.", "Too big overshoots; too small takes too long.")),
        ("손실함수", "Loss Function", ("선별기가 지금 얼마나 틀렸는지 나타내는 오판 점수.", "The miss score showing how wrong the sorter currently is."), ('이 점수를 낮추는 게 학습의 목표예요. 로지스틱 회귀도 이렇게 학습할 수 있어요. → <a href="logisticreg-ko.html">저울 눈금을 S자 곡선에 넣어 보기</a>', 'Lowering this score is the goal of training; logistic regression can be trained this way too. → <a href="logisticreg-en.html">Feeding the Scale\'s Number Through an S-Curve</a>')),
        ("지역 최솟값", "Local Minimum", ("작은 골짜기: 주변에선 가장 낮지만 전체에서 가장 낮은 곳은 아닐 수 있는 위치.", "A shallow dip: lowest nearby, but maybe not lowest overall."), ("여기서 멈추면 더 깊은 골짜기를 못 찾아요.", "Stop here, and the deeper valley goes unfound.")),
        ("전역 최솟값", "Global Minimum", ("곡선 전체에서 오판 점수가 진짜 가장 낮은 위치.", "The setting with the truly lowest miss score on the whole curve."), ("손실 곡면이 볼록하지 않으면 경사하강법이 찾아낸다는 보장이 없어요.", "If the loss surface isn't convex, gradient descent isn't guaranteed to find it.")),
        ("확률적 경사하강법(SGD)", "Stochastic Gradient Descent (SGD)", ("작물 전체 대신 일부만 검사해 기울기를 재는 방법.", "Measuring the slope from a sample of the produce instead of all of it."), ("데이터 전체로 재는 것보다 한 번의 계산이 훨씬 빨라요.", "Each update is much faster than computing over all the data.")),
        ("수렴", "Convergence", ("다이얼 움직임이 점점 작아져 한 위치에 자리 잡는 것.", "The dial's moves shrinking until it settles at one setting."), ("보통 학습을 멈춰도 된다고 보는 신호예요.", "Usually taken as the sign that training can stop.")),
    ],
}
