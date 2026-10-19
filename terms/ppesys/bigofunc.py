from _draw import *
from _world import *


def minicar(x, y, s=1.0):
    return car(x, y, s * 0.5, "var(--muted)")


def car_row(x0, y0, n, gap=22, s=1.0):
    return "".join(minicar(x0 + i * gap, y0, s) for i in range(n))


# 1. 차가 10대일 땐 괜찮던 일이, 1만 대가 되니 끝나질 않아요
P1 = svg(320, sky(320)
         + car_row(90, 190, 10, 26, 1.0)
         + person(650, 150, s=0.8, face=SMILE, **CHIEF)
         + label(650, 100, "⟦차 10대: 금방 끝나요|10 cars: done in no time⟧", 11, "var(--good)", cls="d")
         + label(380, 30, "⟦정비공장이 10대에서 10,000대 규모로 커졌어요|the garage grew from 10 cars to 10,000⟧", 13, "var(--ink)", cls="d")
         + label(380, 295, "⟦그런데 어떤 일은 비례보다 훨씬 더 느려져요|but some tasks slow down far more than just proportionally⟧", 12, "var(--ink)"))

# 2. "차가 늘면 그만큼만 늘겠지"는 방법에 따라 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SWEAT + EYES, **MECH1)
         + bubble(280, 70, 260, 42, "⟦차가 10배 늘면 시간도 딱 10배겠지…|10x the cars means 10x the time, right…⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 280, "⟦방법에 따라 \'늘어나는 정도\'가 완전히 달라요|how fast it grows depends entirely on the method⟧", 12, "var(--ink)"))

# 3. 복잡도(Big-O) = 차가 많아질 때 일이 얼마나 빨리 늘어나는지 재는 자 (hero)
P3 = svg(340, sky(340)
         + queueboard(60, 90, 300, 200, "⟦차 수 n이 늘 때|AS n (CARS) GROWS⟧",
                      ["O(1): ⟦늘 똑같아요|always the same⟧",
                       "O(log n): ⟦아주 조금씩 늘어요|grows very slowly⟧",
                       "O(n): ⟦차 수만큼 늘어요|grows with n⟧",
                       "O(n²): ⟦훨씬 가파르게 늘어요|grows much steeper⟧"], 1.0)
         + person(600, 170, s=0.85, face=EYES, **CHIEF)
         + label(380, 25, "⟦Big-O = 차가 많아질 때 일이 얼마나 빨리 늘어나는지 재는 자|Big-O = a ruler for how fast the work grows as the cars pile up⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦숫자 하나가 아니라, \'늘어나는 모양\'을 재는 거예요|it measures the shape of the growth, not one fixed number⟧", 11, "var(--muted)"))

# 4. 차 10대 vs 1,000대일 때 각 방식이 몇 걸음 걸리는지
P4 = svg(320, sky(320)
         + queueboard(60, 30, 330, 250, "⟦n=10 vs n=1,000, 몇 걸음?|n=10 vs n=1,000, HOW MANY STEPS?⟧",
                      ["O(1): 1 ⟦걸음|step⟧ → 1 ⟦걸음|step⟧",
                       "O(log n): 3 ⟦걸음|steps⟧ → 10 ⟦걸음|steps⟧",
                       "O(n): 10 ⟦걸음|steps⟧ → 1,000 ⟦걸음|steps⟧",
                       "O(n²): 100 ⟦걸음|steps⟧ → 1,000,000 ⟦걸음|steps⟧"], 1.0)
         + person(610, 150, s=0.8, face=SWEAT + EYES, **MECH1)
         + label(610, 260, "⟦n²는 금방 감당 못 할 만큼 커져요|O(n²) balloons fast, out of hand⟧", 11, "var(--bad)")
         + label(380, 300, "⟦n이 커질수록, 모양의 차이가 훨씬 크게 느껴져요|the bigger n gets, the more the shape of growth matters⟧", 12, "var(--ink)"))

# 5. Big-O는 "모양"만 재요 — 실제 초 단위는 또 다른 이야기예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + queueboard(80, 60, 200, 110, "⟦번호판으로 바로|BY PLATE NUMBER⟧", ["O(1)"], 0.9)
         + label(190, 250, "⟦몇 초가 걸리는진 장비·상황마다 달라요|the actual seconds depend on the gear and situation⟧", 11, "var(--ink)")
         + queueboard(470, 60, 220, 110, "⟦한 줄로 하나씩|ONE BY ONE IN A LINE⟧", ["O(n)"], 0.9)
         + label(580, 250, "⟦하지만 \'늘어나는 모양\'은 비교할 수 있어요|but the shape of the growth is always comparable⟧", 11, "var(--ink)")
         + label(380, 280, "⟦Big-O는 추세를 재는 자이지, 초시계가 아니에요|Big-O is a ruler for the trend — not a stopwatch⟧", 12, "var(--ink)", cls="d"))

CONST_I = icon('<rect x="20" y="20" width="24" height="24" rx="4" fill="var(--good)"/>')
LOG_I = icon('<path d="M8 50 Q 20 20 56 14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LINEAR_I = icon('<path d="M8 50 L56 14" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
QUAD_I = icon('<path d="M8 50 Q 40 50 56 8" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "bigofunc", "order": 11,
    "title": ("차가 많아질 때 얼마나 느려질까", "How Much Slower as Cars Pile Up"),
    "h1": ("<em>알고리즘 복잡도(Big-O)</em>가 뭐예요?", "What is <em>Time Complexity (Big-O)</em>?"),
    "sub": ("시간 복잡도와 Big-O 표기법을, 정비공장 규모가 커질 때 일이 얼마나 빨리 늘어나는지 재는 자 이야기로 풀어봤어요.",
            "Time complexity and Big-O notation, told as a story about a ruler that measures how fast work grows as the garage scales up."),
    "panels": [
        {"svg": P1, "alt": ("차가 10대일 땐 반장이 여유롭지만, 정비공장이 10,000대 규모로 커짐", "The chief is relaxed with 10 cars, but the garage grows to a scale of 10,000"),
         "caption": ("차가 10대일 땐 괜찮던 일이, 1만 대가 되니 끝나질 않아요.", "What was fine at 10 cars never finishes at 10,000."),
         "small": ("어떤 일은 비례보다 훨씬 더 느려져요.", "Some tasks slow down far more than just proportionally.")},
        {"svg": P2, "alt": ("정비사가 \'차가 10배 늘면 시간도 10배겠지\'라고 진땀 흘리며 짐작함", "A mechanic sweats, guessing that 10x the cars just means 10x the time"),
         "caption": ("\'차가 늘면 그만큼만 늘겠지\'는 방법에 따라 틀려요.", "\'More cars means proportionally more time\' isn't always true."),
         "small": ("방법에 따라 \'늘어나는 정도\'가 완전히 달라요.", "How fast it grows depends entirely on the method.")},
        {"svg": P3, "hero": True, "alt": ("순서판에 O(1)·O(log n)·O(n)·O(n²)가 차 수 n이 늘 때 각각 어떻게 늘어나는지 적혀 있음", "A board lists how O(1), O(log n), O(n), and O(n²) each grow as the car count n increases"),
         "caption": ("Big-O = 차가 많아질 때 일이 얼마나 빨리 느는지 재는 자예요.", "Big-O = a ruler for how fast the work grows as cars pile up."),
         "small": ("숫자 하나가 아니라, \'늘어나는 모양\'을 재는 거예요.", "It measures the shape of the growth, not one fixed number."),
         "tricks": (4, [
             (CONST_I, ("O(1)", "O(1)"), ("번호판으로 바로 찾기, 늘 똑같아요", "find it by plate number — always the same")),
             (LOG_I, ("O(log n)", "O(log n)"), ("이진트리처럼 매번 반씩 줄여요", "halve it each time, like a binary tree"), "calm"),
             (LINEAR_I, ("O(n)", "O(n)"), ("한 줄로 서서 하나씩 확인해요", "check them one by one, down the line"), "warm"),
             (QUAD_I, ("O(n²)", "O(n²)"), ("모든 차끼리 서로 다 비교해요", "compare every car against every other")),
         ])},
        {"svg": P4, "alt": ("차 10대와 1,000대일 때 O(1)·O(log n)·O(n)·O(n²) 각각 몇 걸음 걸리는지 비교하는 순서판", "A board comparing how many steps O(1), O(log n), O(n), and O(n²) take at n=10 versus n=1,000"),
         "caption": ("n이 커지면 차이가 확 벌어져요.", "The difference explodes as n grows."),
         "small": ("O(n²)는 금방 감당 못 할 만큼 커져요.", "O(n²) balloons fast, out of hand.")},
        {"svg": P5, "alt": ("왼쪽: 번호판으로 바로 찾는 O(1). 오른쪽: 한 줄로 하나씩 확인하는 O(n). 실제 걸리는 초는 장비마다 다름을 설명", "Left: O(1), found directly by plate number. Right: O(n), checked one by one in a line. Actual seconds vary by equipment"),
         "caption": ("Big-O는 \'모양\'만 재요.", "Big-O measures only the shape."),
         "small": ("실제 초 단위는 장비·상황마다 다른, 또 다른 이야기예요.", "The actual seconds are a different story, depending on the gear.")},
    ],
    "summary": (("<b>Big-O(시간 복잡도)</b> = 차(자료) 수가 늘어날 때, 걸리는 일이 <b>얼마나 빠르게 늘어나는지 그 \'모양\'</b>을 재는 자.",
                 "<b>Big-O (time complexity)</b> = a ruler that measures the shape of how fast the work grows as the number of cars (the data) increases."),
                ("시간 복잡도는 입력 크기 n이 커질 때 알고리즘의 실행 시간이 얼마나 빠르게 증가하는지를 나타내는 척도예요. O(1)은 입력 크기와 무관하게 일정하고, O(log n)은 이진 탐색처럼 매번 절반씩 줄어들며, O(n)은 전체를 한 번씩 훑고, O(n²)은 모든 쌍을 비교하는 식으로 n이 커질수록 급격히 느려져요. Big-O는 상수항이나 실제 하드웨어 속도를 무시하고 오직 \'증가하는 추세\'만 비교하는 표기법이에요.",
                 "Time complexity measures how fast an algorithm's running time grows as the input size n increases. O(1) stays constant regardless of input size; O(log n) halves the remaining work each step, as in binary search; O(n) scans everything once; O(n²) compares every pair, growing steeply as n increases. Big-O ignores constant factors and actual hardware speed — it compares only the growth trend.")),
    "glossary": [
        ("O(1)", "O(1)", ("번호판으로 바로 찾기, 늘 똑같은 시간.", "Found directly by plate number — always the same time."), ("입력이 늘어도 시간이 그대로예요.", "Time stays flat no matter how much input grows.")),
        ("O(log n)", "O(log n)", ("매번 반씩 줄여가는 탐색.", "A search that halves the candidates each step."), ("아주 천천히 늘어나요.", "Grows very, very slowly.")),
        ("O(n)", "O(n)", ("한 줄로 서서 하나씩 확인하기.", "Checking one by one, down the line."), ("입력 크기만큼 그대로 늘어나요.", "Grows exactly in step with the input size.")),
        ("O(n²)", "O(n²)", ("모든 차끼리 서로 다 비교하기.", "Comparing every car against every other."), ("n이 커지면 감당 못 할 만큼 가팔라져요.", "Steepens out of hand as n grows.")),
        ("이진트리 탐색(O(log n)의 예)", "Binary Tree Search (an O(log n) example)", ("갈림길마다 반씩 줄여가는 선반 지도.", "A shelf map that halves the search at every fork."), ('O(log n)이 실제로 어떻게 생기는지 여기서 봐요. → <a href="bintree-ko.html">갈림길에서 반씩 줄여가는 선반 지도</a>', 'See what O(log n) actually looks like. → <a href="bintree-en.html">the shelf map that halves the search at every fork</a>')),
        ("스택·큐의 push/pop(O(1)의 예)", "Stack/Queue push-pop (an O(1) example)", ("상자를 쌓거나 줄 세우는 규칙.", "The rule for stacking boxes or lining up cars."), ('push/pop·enqueue/dequeue는 보통 O(1)이에요. → <a href="stackqueue-ko.html">상자는 쌓고, 차는 줄 세우고</a>', 'push/pop and enqueue/dequeue are usually O(1). → <a href="stackqueue-en.html">boxes get stacked, cars get queued</a>')),
        ("캐시 적중/미스", "Cache Hit/Miss", ("자주 쓰는 공구만 담는 작은 공구함.", "A small toolbox holding only the frequent tools."), ('같은 O(1) 조회도 적중이냐 미스냐로 실제 속도가 갈려요. → <a href="cachemem-ko.html">자주 쓰는 공구만 담는 공구함</a>', 'Even at the same O(1), a hit and a miss feel very different in practice. → <a href="cachemem-en.html">the toolbox that holds only the frequent tools</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("리프트에 누가 먼저 올라갈지 정하는 규칙.", "The rule deciding who gets the lift first."), ('순서판을 정렬·검색하는 비용도 이 자로 재요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'Sorting or searching the job board is measured with this same ruler. → <a href="cpusched-en.html">who gets the lift first</a>')),
    ],
}
