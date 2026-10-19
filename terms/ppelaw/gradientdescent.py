"""경사하강법(Gradient Descent) — 머신러닝 최적화 기법. 법제도 주제가 아니라, 학생회 세계관에선 '안개 낀 산을 내려가는 등반 동아리'로 얇게만 걸쳐 둠."""
from _draw import *
from _world import *

TERRAIN = "M0 120 Q80 200 150 190 Q230 160 300 140 Q400 180 500 260 Q580 230 650 180 Q710 150 760 140"


def hill(h=300, extra_fog=False):
    out = (sky(h, ground=False) + f'<path d="{TERRAIN} V{h} H0 Z" fill="var(--good-soft)"/>'
           + f'<path d="{TERRAIN}" stroke="var(--stone-dark)" stroke-width="3" fill="none"/>')
    if extra_fog:
        out += f'<rect width="760" height="{h}" fill="#C9D5E6" opacity="0.5"/>'
    return out


SLOPE_I = icon('<path d="M10 14 L54 50" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M40 50 h14 v-14" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
STEP_I = icon('<ellipse cx="20" cy="44" rx="7" ry="11" fill="var(--ink)" transform="rotate(-20 20 44)"/><ellipse cx="42" cy="24" rx="7" ry="11" fill="var(--ink)" transform="rotate(-20 42 24)" opacity="0.5"/>')
RATE_I = icon('<path d="M10 50 L26 50" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M34 50 L58 50" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
FLAT_I = icon('<path d="M10 40 h44" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M24 30 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 안개가 짙어 어느 쪽이 아래인지 안 보여요
P1 = svg(300, hill(300, extra_fog=True)
         + person(250, 140, s=0.8, face=SWEAT + EYES, **STUDENT)
         + bubble(320, 60, 260, 44, "⟦안개가 너무 짙어서 아래쪽이 안 보여요|the fog is too thick to see which way is down⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦등반 동아리가 안개 낀 산에서 가장 낮은 곳을 찾아야 해요|the hiking club has to find the lowest point on a foggy mountain⟧", 12, "var(--ink)", cls="d"))

# 2. 무작정 걸으면 오히려 더 올라갈 수도 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.8, face=FROWN, **STUDENT) + '<path d="M300 150 L220 120" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(380, 70, "⟦아무 방향이나 걸었더니 오히려 더 올라왔어요|walking in a random direction, I ended up even higher⟧", 13, "var(--bad)")
         + label(380, 280, "⟦방향을 모르면, 걸을수록 오히려 손해일 수 있어요|without knowing the direction, every step can make it worse⟧", 12, "var(--ink)", cls="d"))

# 3. 경사하강법 = 발밑 기울기를 느끼며 내려가는 쪽으로 한 걸음씩 (hero)
P3 = svg(330, hill(330)
         + label(380, 24, "⟦경사하강법 = 발밑 기울기를 느끼며, 내려가는 쪽으로 한 걸음씩|gradient descent = feel the slope underfoot, and step downhill, one step at a time⟧", 12, "var(--ink)", cls="d")
         + person(300, 155, s=0.7, face=EYES, **STUDENT)
         + '<path d="M300 200 l40 20 l40 30 l40 20" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 3" fill="none"/>'
         + '<circle cx="340" cy="220" r="5" fill="var(--good)"/><circle cx="380" cy="250" r="5" fill="var(--good)"/><circle cx="420" cy="270" r="6" fill="var(--accent)"/>'
         + label(380, 310, "⟦기운 쪽의 반대로, 조금씩, 평평해질 때까지|opposite the tilt, little by little, until it goes flat⟧", 11, "var(--muted)"))

# 4. 걸음 크기(학습률)가 너무 크면, 너무 작으면
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 30, "⟦걸음이 너무 크면|steps too big⟧", 13, "var(--ink)", cls="d")
         + '<path d="M80 100 l220 60 l-200 70 l180 60" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + label(190, 290, "⟦아래를 자꾸 지나쳐 헛디뎌요|keeps overshooting past the bottom⟧", 11, "var(--bad)")
         + label(570, 30, "⟦걸음이 작으면|steps small⟧", 13, "var(--ink)", cls="d")
         + '<path d="M460 100 q20 20 40 35 q20 20 40 35 q20 20 40 30 q20 15 40 20" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(570, 290, "⟦느리지만 확실하게 내려가요|slow, but steadily gets there⟧", 11, "var(--good)")
         + label(380, 310, "⟦학습률(걸음 크기)을 잘 정해야 해요|the learning rate (step size) has to be chosen carefully⟧", 11, "var(--ink)", cls="d"))

# 5. 작은 웅덩이를 가장 낮은 곳으로 착각할 수 있어요
P5 = svg(300, hill(300)
         + person(150, 200, s=0.7, face=SMILE, **STUDENT)
         + bubble(40, 80, 220, 44, "⟦여기가 제일 낮은 곳이네요!|this must be the lowest point!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(500, 60, "⟦근데 진짜 가장 낮은 곳은 저기예요|but the real lowest point is over there⟧", 12, "var(--bad)")
         + '<path d="M500 90 L500 250" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 3"/>'
         + label(380, 288, "⟦지금 서 있는 곳에서 가까운 아래쪽만 찾아요 — 더 깊은 골짜기는 못 봐요|it only finds the nearest downhill from where it stands — it can't see a deeper valley elsewhere⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "gradientdescent", "order": 19,
    "title": ("안개 낀 산을 한 걸음씩 내려가기", "Descending a Foggy Mountain, One Step at a Time"),
    "h1": ("<em>경사하강법</em>이 뭐예요?", "What is <em>Gradient Descent</em>?"),
    "sub": ("경사하강법을, 등반 동아리 학생이 안개 낀 산에서 발밑 기울기만 느끼며 가장 낮은 곳을 찾아 내려가는 이야기로 풀어봤어요. (머신러닝 최적화 기법이라 학생회 규칙과는 결이 달라요 — 학생회도 결정을 내릴 때 이렇게 한 걸음씩 나아지는 방향을 찾곤 해요.)",
            "Gradient descent, told as a story about a hiking-club student on a foggy mountain, finding the lowest point by feeling only the slope underfoot. (This is a machine-learning optimization technique, not a rules-and-law one — though even the student council sometimes improves a decision step by step, the same way.)"),
    "panels": [
        {"svg": P1, "alt": ("안개 낀 산 중턱에서 학생이 아래쪽이 안 보인다며 당황함", "On a foggy mountainside, a student is flustered, unable to see which way is downhill"),
         "caption": ("안개가 짙어 어느 쪽이 아래인지 안 보여요.", "The fog is too thick to see which way is down."),
         "small": ("등반 동아리가 안개 낀 산에서 가장 낮은 곳을 찾아야 해요.", "The hiking club has to find the lowest point on a foggy mountain.")},
        {"svg": P2, "alt": ("학생이 아무 방향이나 걸었더니 오히려 더 높은 곳으로 올라왔다고 당황함", "The student, frowning, realizes walking in a random direction made them climb even higher"),
         "caption": ("무작정 걸으면 오히려 더 올라갈 수도 있어요.", "Walking blindly can even take you higher."),
         "small": ("방향을 모르면, 걸을수록 오히려 손해일 수 있어요.", "Without knowing the direction, every step can make it worse.")},
        {"svg": P3, "hero": True, "alt": ("학생이 산비탈에 서서, 기운 방향의 반대로 발자국을 점점 깊은 골짜기 쪽으로 남김", "The student stands on the slope, leaving footprints that head the opposite way from the tilt, toward the deeper valley"),
         "caption": ("경사하강법은 발밑 기울기를 느끼며, 내려가는 쪽으로 한 걸음씩 걷는 방법이에요.", "Gradient descent means feeling the slope underfoot, and stepping downhill, one step at a time."),
         "small": ("기운 쪽의 반대로, 조금씩, 평평해질 때까지.", "Opposite the tilt, little by little, until it goes flat."),
         "tricks": (4, [
             (SLOPE_I, ("기울기 느끼기", "Feel the slope"), ("발밑이 어느 쪽으로 기우는지 봐요", "senses which way the ground tilts"), "calm"),
             (STEP_I, ("기울기 반대로 한 걸음", "Step opposite the slope"), ("기운 방향의 반대가 내려가는 길이에요", "the downhill way is opposite the tilt"), "warm"),
             (RATE_I, ("걸음 크기 정하기(학습률)", "Set the step size (learning rate)"), ("너무 크면 헛디디고, 작으면 느려요", "too big overshoots, too small is slow")),
             (FLAT_I, ("평평해지면 멈추기", "Stop when it's flat"), ("기울기가 거의 0이면 다 왔다고 봐요", "near-zero slope means it's arrived")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 걸음이 너무 커 아래를 자꾸 지나치며 비틀거림. 오른쪽: 걸음이 작아 느리지만 확실하게 내려감", "Left: steps too big keep overshooting the bottom. Right: small steps descend slowly but surely"),
         "caption": ("걸음 크기(학습률)가 너무 크면, 너무 작으면 서로 다른 문제가 생겨요.", "Too big a step, or too small, each causes its own problem."),
         "small": ("학습률(걸음 크기)을 잘 정해야 해요.", "The learning rate (step size) has to be chosen carefully.")},
        {"svg": P5, "alt": ("학생이 작은 웅덩이를 가장 낮은 곳이라 믿지만, 실제로 더 깊은 골짜기가 멀리 따로 있음", "The student believes a small dip is the lowest point, but a far deeper valley lies elsewhere"),
         "caption": ("작은 웅덩이를 가장 낮은 곳으로 착각할 수 있어요.", "A small dip can be mistaken for the true lowest point."),
         "small": ("지금 서 있는 곳에서 가까운 아래쪽만 찾아요 — 더 깊은 골짜기는 못 봐요.", "It only finds the nearest downhill from where it stands — it can't see a deeper valley elsewhere.")},
    ],
    "summary": (("<b>경사하강법</b> = 지금 위치의 <b>기울기(경사)</b>를 재서, 그 <b>반대 방향으로 조금씩</b> 움직이며 가장 낮은 곳(최솟값)을 찾아가는 방법.",
                 "<b>Gradient descent</b> = measuring the <b>slope (gradient)</b> at the current point, and moving a <b>little in the opposite direction</b>, repeatedly, to find the lowest point (minimum)."),
                ("경사하강법은 손실함수(얼마나 틀렸는지를 나타내는 함수)의 기울기(gradient)를 계산해, 그 반대 방향으로 '학습률(learning rate)'만큼 파라미터를 조금씩 갱신하며 손실을 줄여가는 최적화 알고리즘이에요. 학습률이 너무 크면 최솟값 주변을 오가며 발산하고, 너무 작으면 수렴이 지나치게 느려요. 또한 기울기가 0에 가까워지는 지점이 여럿 있을 수 있어 '지역 최솟값'에 갇혀 '전역 최솟값'을 놓칠 수 있어요. 데이터 전체 대신 일부만으로 기울기를 재는 확률적 경사하강법(SGD)이 실무에서 널리 쓰여요.",
                 "Gradient descent is an optimization algorithm that computes the gradient of a loss function (how wrong the model currently is), then updates parameters a little in the opposite direction by an amount set by the 'learning rate,' repeatedly reducing the loss. Too large a learning rate causes the process to oscillate or diverge around the minimum; too small makes convergence painfully slow. Because the gradient can near zero at more than one point, the process can get trapped in a 'local minimum' and miss the true 'global minimum.' In practice, stochastic gradient descent (SGD) — computing the gradient from only a portion of the data at a time — is widely used.")),
    "glossary": [
        ("경사하강법", "Gradient Descent", ("발밑 기울기를 느끼며 한 걸음씩 내려가는 방법.", "Feeling the slope underfoot and stepping downhill, bit by bit."), ("가장 흔히 쓰이는 최적화 방법이에요.", "The most commonly used optimization method.")),
        ("기울기", "Gradient", ("발밑이 어느 쪽으로, 얼마나 기울었는지.", "Which way, and how steeply, the ground tilts underfoot."), ("이 반대 방향이 내려가는 길이에요.", "The downhill way is the opposite of this.")),
        ("학습률", "Learning Rate", ("한 걸음의 크기.", "The size of a single step."), ("크면 헛디디고, 작으면 너무 오래 걸려요.", "Too big overshoots; too small takes forever.")),
        ("손실함수", "Loss Function", ("지금 얼마나 틀렸는지 나타내는 높이.", "The height that represents how wrong things currently are."), ("이 높이를 낮추는 게 목표예요.", "Lowering this height is the whole goal.")),
        ("지역 최솟값", "Local Minimum", ("작은 웅덩이 — 주변에선 가장 낮지만 진짜는 아닐 수 있어요.", "A small dip — lowest nearby, but maybe not truly the lowest."), ("여기 갇히면 더 깊은 골짜기를 못 찾아요.", "Get stuck here, and the deeper valley goes unfound.")),
        ("전역 최솟값", "Global Minimum", ("산 전체에서 진짜 가장 낮은 곳.", "The truly lowest point on the whole mountain."), ("경사하강법이 늘 찾아준다는 보장은 없어요.", "Gradient descent is never guaranteed to find it.")),
        ("확률적 경사하강법(SGD)", "Stochastic Gradient Descent (SGD)", ("산 전체 대신 눈에 보이는 일부만 보고 기울기를 재는 방법.", "Gauging the slope from just a visible patch instead of the whole mountain."), ("매번 전부를 보는 것보다 훨씬 빨라요.", "Much faster than surveying everything every time.")),
        ("수렴", "Convergence", ("걸음이 점점 작아지며 한 곳에 멈추는 것.", "Steps growing smaller and smaller until they settle at one spot."), ("경사하강법이 끝났다고 보는 신호예요.", "The signal that gradient descent is done.")),
    ],
}
