from _draw import *
from _world import *

# 1. 손님 차들이 뒤죽박죽 줄 서 있어요
P1 = svg(300, sky(300)
         + car(160, 200, 0.6) + car(260, 200, 1.1) + car(360, 200, 0.8) + car(460, 200, 1.3) + car(560, 200, 0.5)
         + person(640, 150, s=0.8, face=SWEAT + EYES, **CHIEF)
         + label(380, 60, "⟦차 크기 순서로 줄을 세워 주세요|please line the cars up by size⟧", 13, "var(--ink)")
         + label(380, 280, "⟦뒤죽박죽이라 어디부터 손대야 할지 모르겠어요|they're all mixed up — where do I even start?⟧", 12, "var(--muted)"))

# 2. 아무렇게나 바꾸면 끝이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + car(200, 180, 0.8) + car(300, 180, 0.6) + car(400, 180, 1.2) + car(500, 180, 0.5) + car(600, 180, 1.0)
         + label(250, 130, "⟦이 두 대만 바꿔볼까?|swap just these two?⟧", 11, "var(--bad)", cls="d")
         + person(140, 150, s=0.8, face=FROWN, **MECH1)
         + label(380, 70, "⟦그때그때 바꾸면 줄은 계속 뒤섞여요|swapping at random just re-mixes the line⟧", 13, "var(--ink)")
         + label(380, 262, "⟦정해진 규칙 없이는 언제 끝날지 알 수 없어요|without a fixed rule, there's no telling when you're done⟧", 12, "var(--muted)"))

# 3. 정렬 알고리즘 = 비교·교환 규칙을 정해 자동으로 줄 세우기 (hero)
P3 = svg(340, sky(340)
         + car(140, 230, 0.55) + car(250, 230, 0.75) + car(360, 230, 0.95) + car(470, 230, 1.1) + car(580, 230, 1.3)
         + person(660, 190, s=0.8, face=SMILE, **CHIEF)
         + label(380, 30, "⟦정렬 알고리즘 = 비교하고 자리를 바꾸는 규칙을 정해두는 것|a sort algorithm fixes a rule for comparing and swapping⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦규칙대로만 하면 저절로 작은 차부터 큰 차 순서가 돼요|follow the rule, and small-to-large order happens on its own⟧", 12, "var(--muted)"))

SWAP_I = icon('<circle cx="18" cy="32" r="10" fill="var(--accent)"/><circle cx="46" cy="32" r="10" fill="var(--good)"/><path d="M26 22 Q32 10 40 22" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M26 42 Q32 54 40 42" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>')
PICK_I = icon('<circle cx="22" cy="24" r="8" fill="var(--good)"/><circle cx="38" cy="36" r="10" fill="var(--line)"/><circle cx="20" cy="44" r="9" fill="var(--line)"/><path d="M22 24 l20 -6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
INSERT_I = icon('<rect x="8" y="26" width="14" height="14" fill="var(--line)"/><rect x="26" y="26" width="6" height="14" fill="none" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 2"/><rect x="36" y="26" width="14" height="14" fill="var(--line)"/><path d="M29 14 v10" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M24 20 l5 -6 l5 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SPLIT_I = icon('<rect x="8" y="14" width="48" height="10" fill="var(--line)"/><rect x="8" y="40" width="20" height="10" fill="var(--good)"/><rect x="36" y="40" width="20" height="10" fill="var(--good)"/><path d="M32 26 v8 M20 34 v6 M44 34 v6" stroke="var(--ink)" stroke-width="2.5"/>')

# 4. 네 가지 방법의 속도 비교
P4 = svg(320, sky(320)
         + queueboard(60, 40, 320, 240, "⟦속도 비교(차가 많아질수록)|speed as the line grows⟧",
                      ("⟦거품/선택/삽입 — 한 대씩 다 비교(느림)|bubble/selection/insertion — compare one by one (slow)⟧",
                       "⟦시간: 대략 n²|time: roughly n²⟧",
                       "⟦병합/퀵 — 반으로 나눠 정리 후 합치기(빠름)|merge/quick — split in half, sort, merge (fast)⟧",
                       "⟦시간: 대략 n log n|time: roughly n log n⟧"), 1.0, hl=2)
         + car(560, 150, 0.8) + car(640, 170, 0.5) + car(600, 220, 0.9)
         + label(600, 270, "⟦차 대수가 늘어날수록 차이가 커져요|the gap widens as more cars line up⟧", 11, "var(--muted)")
         + label(380, 305, "⟦반으로 쪼개서 푸는 방법이 대부분 더 유리해요|splitting the problem in half usually wins⟧", 12, "var(--ink)"))

# 5. 차가 적을 땐 간단한 방법이 오히려 빨라요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + car(150, 170, 0.6) + car(230, 170, 0.8)
         + person(190, 120, s=0.7, face=SMILE, **MECH2)
         + label(190, 250, "⟦차 두세 대면 그냥 비교가 더 빨라요|with two or three cars, plain comparing is faster⟧", 11, "var(--ink)")
         + car(520, 170, 0.7) + car(600, 170, 1.0) + car(680, 170, 0.5)
         + label(600, 250, "⟦차가 아주 많을 때만 나눠 풀기가 이득이에요|splitting pays off only once the line gets long⟧", 11, "var(--ink)")
         + label(380, 282, "⟦언제나 제일 빠른 정렬은 없어요 — 상황에 맞게 골라요|there's no single fastest sort — pick one for the situation⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "sortalgo", "order": 12,
    "title": ("크기 순서로 차를 세우는 여러 방법", "Different Ways to Line Cars Up by Size"),
    "h1": ("<em>정렬 알고리즘</em>이 뭐예요?", "What is a <em>Sort Algorithm</em>?"),
    "sub": ("정렬 알고리즘을, 정비공장 손님 차들을 크기 순서로 줄 세우는 여러 방법 이야기로 풀어봤어요.",
            "Sort algorithms, told as a story about lining up customers' cars by size at the repair garage."),
    "panels": [
        {"svg": P1, "alt": ("손님 차들이 뒤죽박죽 서 있고 정비반장이 곤란해함", "Customer cars stand mixed up in size while the chief mechanic looks troubled"),
         "caption": ("차 크기 순서로 줄을 세워야 해요.", "The cars need to be lined up by size."),
         "small": ("뒤죽박죽이라 어디부터 손대야 할지 모르겠어요.", "They're all mixed up — where do you even start?")},
        {"svg": P2, "alt": ("정비사가 아무 두 차나 바꿔보지만 줄은 여전히 뒤섞여 있음", "A mechanic swaps two random cars, but the line stays mixed"),
         "caption": ("아무렇게나 바꾸면 끝이 없어요.", "Swapping at random never ends."),
         "small": ("정해진 규칙 없이는 언제 끝날지 알 수 없어요.", "Without a fixed rule, there's no telling when you're done.")},
        {"svg": P3, "hero": True, "alt": ("차들이 작은 차부터 큰 차 순서로 가지런히 줄 서 있고 정비반장이 흡족해함", "Cars now stand neatly in order from smallest to largest, the chief satisfied"),
         "caption": ("정렬 알고리즘은 비교·교환 규칙을 정해두는 것이에요.", "A sort algorithm fixes a rule for comparing and swapping."),
         "small": ("규칙대로만 하면 저절로 순서가 맞아져요.", "Follow the rule, and the order falls into place on its own."),
         "tricks": (4, [
             (SWAP_I, ("거품정렬", "Bubble sort"), ("옆 차끼리 비교해 큰 차를 뒤로", "compare neighbors, push the bigger one back"), "warm"),
             (PICK_I, ("선택정렬", "Selection sort"), ("제일 작은 차를 찾아 앞에 두기", "find the smallest, put it in front")),
             (INSERT_I, ("삽입정렬", "Insertion sort"), ("새 차를 맞는 자리에 끼워넣기", "slide the new car into its spot")),
             (SPLIT_I, ("병합/퀵정렬", "Merge/quick sort"), ("반으로 나눠 정리한 뒤 합치기", "split in half, sort, then merge"), "calm"),
         ])},
        {"svg": P4, "alt": ("거품/선택/삽입정렬은 느리고 병합/퀵정렬은 빠르다는 속도 비교표", "A comparison board: bubble/selection/insertion are slow, merge/quick are fast"),
         "caption": ("차가 많아질수록 방법 간 속도 차이가 커져요.", "The speed gap widens as the line of cars grows."),
         "small": ("반으로 쪼개서 푸는 방법이 대부분 더 유리해요.", "Splitting the problem in half usually wins.")},
        {"svg": P5, "alt": ("왼쪽: 차가 적을 땐 단순 비교가 더 빠름. 오른쪽: 차가 많을 때만 나눠 풀기가 이득", "Left: with few cars plain comparing is faster. Right: splitting pays off only with many cars"),
         "caption": ("차가 적을 땐 간단한 방법이 오히려 빨라요.", "With few cars, the simple method is actually faster."),
         "small": ("언제나 제일 빠른 정렬은 없어요, 상황에 맞게 골라요.", "There's no single fastest sort — you pick one for the situation.")},
    ],
    "summary": (("<b>정렬 알고리즘</b>은 자동차들을 <b>비교하고 자리를 바꾸는 규칙</b>을 정해 <b>크기 순서</b>로 줄 세우는 여러 방법이에요.",
                 "A <b>sort algorithm</b> is one of several rules for <b>comparing and swapping</b> items to line them up <b>in order by size</b>."),
                ("정렬 알고리즘은 데이터를 특정 순서로 재배열하는 절차예요. 거품·선택·삽입정렬은 구현이 쉽지만 데이터가 n개일 때 대략 n² 번 비교하고, 병합·퀵정렬은 '분할정복'으로 문제를 반씩 나눠 풀어 대략 n log n 번만 비교해요. 데이터가 적으면 오버헤드가 적은 단순 정렬이, 많으면 분할정복 정렬이 유리해요.",
                 "A sort algorithm rearranges data into a given order. Bubble, selection, and insertion sort are simple but make roughly n² comparisons for n items. Merge and quick sort use 'divide and conquer', splitting the problem in half, needing only about n log n comparisons. Simple sorts win for small data; divide-and-conquer sorts win for large data.")),
    "glossary": [
        ("버블정렬", "Bubble Sort", ("이웃 차끼리 비교해 큰 차를 뒤로 보내기.", "Compare neighbors, push the bigger one back."), ("구현이 가장 쉽지만 느려요.", "Simplest to implement, but slow.")),
        ("선택정렬", "Selection Sort", ("가장 작은 차를 찾아 맨 앞에 두기.", "Find the smallest and put it in front."), ("비교 횟수는 항상 비슷해요.", "Always makes about the same number of comparisons.")),
        ("삽입정렬", "Insertion Sort", ("새 차를 이미 선 줄의 맞는 자리에 끼우기.", "Slide a new car into its correct spot in the line."), ("거의 다 정렬된 데이터엔 아주 빨라요.", "Very fast on data that's already nearly sorted.")),
        ("병합정렬", "Merge Sort", ("줄을 반으로 나눠 각각 세우고 합치기.", "Split the line in half, sort each half, then merge."), ("항상 n log n — 안정적이에요.", "Always n log n — reliably steady.")),
        ("퀵정렬", "Quick Sort", ("기준 차를 골라 작은 쪽/큰 쪽으로 나누기.", "Pick a pivot car and split into smaller/bigger sides."), ("평균은 빠르지만 운이 나쁘면 느려요.", "Fast on average, slow in the unlucky case.")),
        ("시간복잡도", "Time Complexity", ("차가 늘어날 때 시간이 느는 정도.", "How fast time grows as the line grows."), ("n² 과 n log n 의 차이가 핵심이에요.", "The gap between n² and n log n is the key idea.")),
        ("안정 정렬", "Stable Sort", ("같은 크기 차의 원래 순서를 지켜주는 것.", "Keeping same-size cars in their original order."), ("병합정렬·삽입정렬은 안정적이에요.", "Merge sort and insertion sort are stable.")),
        ("분할정복", "Divide and Conquer", ("문제를 반으로 쪼개 따로 풀고 합치는 전략.", "The strategy of splitting a problem, solving the halves, then combining."), ("병합/퀵정렬이 이 전략을 써요.", "Merge sort and quick sort both use this strategy.")),
    ],
}
