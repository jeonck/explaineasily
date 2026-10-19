"""분할정복·탐욕법·동적계획법 — 알고리즘 설계 패러다임. 법제도 주제는 아니지만, 학생회도 큰 문제를 풀 땐 명확한 절차를 따라요."""
from _draw import *
from _world import *

SPLIT_I = icon('<rect x="8" y="10" width="48" height="16" rx="3" fill="var(--accent)"/><path d="M32 26 V34" stroke="var(--ink)" stroke-width="3"/><rect x="8" y="34" width="20" height="16" rx="3" fill="var(--good)"/><rect x="36" y="34" width="20" height="16" rx="3" fill="var(--good)"/>')
GREEDY_I = icon('<circle cx="16" cy="44" r="8" fill="var(--good)"/><circle cx="32" cy="30" r="8" fill="var(--line)"/><circle cx="48" cy="16" r="8" fill="var(--line)"/><path d="M16 44 L32 30" stroke="var(--accent)" stroke-width="3"/>')
DP_I = icon('<rect x="8" y="12" width="16" height="16" rx="3" fill="var(--good)"/><rect x="28" y="12" width="16" height="16" rx="3" fill="var(--good)" opacity="0.5"/><rect x="18" y="34" width="16" height="16" rx="3" fill="var(--accent)"/><path d="M16 28 l4 6 M36 28 l-10 6" stroke="var(--muted)" stroke-width="2" stroke-dasharray="3 3"/>')
STEP_I = icon('<path d="M10 50 h12 v-12 h12 v-12 h12 v-12 h12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 축제 예산 배정, 너무 복잡해요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SWEAT + EYES, **PRESIDENT)
         + bubble(70, 60, 300, 56, "⟦동아리 스무 곳의 예산 신청을 한 번에 어떻게 정하죠?|how do we decide twenty clubs' budget requests all at once?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=FROWN, **REP)
         + label(380, 280, "⟦동아리가 너무 많아 한 번에 다 비교할 수가 없어요|too many clubs to compare all at once⟧", 13, "var(--ink)", cls="d"))

# 2. 접수 순서대로만 주면 불합리해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SMILE, **STUDENT) + label(220, 250, "⟦저희가 1등으로 접수해서 다 받았어요|we submitted first, so we got everything⟧", 11, "var(--good)")
         + person(560, 150, s=0.8, face=FROWN, **STUDENT) + label(560, 250, "⟦저흰 꼴찌라 한 푼도 못 받았어요|we were last, so we got nothing⟧", 11, "var(--bad)")
         + label(380, 285, "⟦순서만 보고 정하면, 더 좋은 방법을 놓쳐요|deciding by order alone misses a better way⟧", 12, "var(--ink)", cls="d"))

# 3. 세 가지 문제해결 방법 (hero)
P3 = svg(360, sky(360)
         + label(380, 26, "⟦큰 문제를 푸는 세 가지 방법: 분할정복·탐욕법·동적계획법|three ways to solve a big problem: divide-and-conquer, greedy, dynamic programming⟧", 13, "var(--ink)", cls="d")
         + person(130, 150, s=0.85, face=EYES, **PRESIDENT)
         + rulesboard(230, 70, 300, 250, "⟦세 가지 방법|THREE METHODS⟧",
                      ("⟦분할정복 — 학년별로 쪼개 따로 정하고 합치기|divide and conquer — split by grade, decide each, combine⟧",
                       "⟦탐욕법 — 가장 급한 곳부터 먼저 주기|greedy — fund the most urgent request first⟧",
                       "⟦동적계획법 — 한 번 정한 결과는 기억해두기|dynamic programming — remember an answer once it's found⟧",
                       "⟦셋 다: 큰 문제를 작은 단위로 다루는 틀|all three: handle the big problem in small pieces⟧"), 0.9)
         + person(640, 160, s=0.8, face=SMILE, **REP)
         + label(380, 335, "⟦학생회도 복잡한 결정을 내릴 땐 명확한 절차를 따라야 해요, 알고리즘처럼|even the student council follows a clear step-by-step procedure for a hard decision, just like an algorithm⟧", 11, "var(--muted)"))

# 4. 세 방법을 축제 예산에 적용하면
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 20, 320, 280, "⟦분할정복|DIVIDE AND CONQUER⟧",
                      ("⟦1학년 몫, 2학년 몫, 3학년 몫으로 나눠|split into 1st/2nd/3rd-grade shares⟧",
                       "⟦각 학년 대표가 따로 정하고|each grade's rep decides separately⟧",
                       "⟦마지막에 전부 합쳐요|then all shares are combined⟧"), 1.0)
         + rulesboard(400, 20, 320, 280, "⟦탐욕법 / 동적계획법|GREEDY / DP⟧",
                      ("⟦탐욕: 위험도 높은 동아리부터 먼저 배정|greedy: fund the highest-risk club first⟧",
                       "⟦DP: 같은 학년 조합은 다시 안 따져요|DP: never re-solves the same grade combo⟧",
                       "⟦매번 빠르고 늘 완벽하진 않아요(탐욕)|fast every time, not always perfect (greedy)⟧"), 1.0)
         + label(380, 310, "⟦문제의 생김새에 따라 어울리는 방법이 달라요|which method fits depends on the shape of the problem⟧", 11, "var(--ink)", cls="d"))

# 5. 탐욕법은 빠르지만 늘 최선은 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **REP) + label(190, 250, "⟦지금 가장 급한 곳부터 바로 줬어요|funded the most urgent one right away⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **PRESIDENT) + label(570, 250, "⟦근데 전체로 보면 더 나은 조합이 있었어요|but looking at it all, there was a better combination⟧", 11, "var(--ink)")
         + label(380, 285, "⟦탐욕법은 빠르지만, 매번 전체 최선을 보장하진 않아요|greedy is fast — but it doesn't always guarantee the overall best⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "algoparadigm", "order": 20,
    "title": ("쪼개고, 급한 것부터, 기억해두고", "Split It, Fund the Urgent First, Remember the Answer"),
    "h1": ("<em>분할정복·탐욕법·동적계획법</em>이 뭐예요?", "What are <em>Divide-and-Conquer, Greedy, and Dynamic Programming</em>?"),
    "sub": ("분할정복·탐욕법·동적계획법을, 학생회가 동아리 스무 곳의 축제 예산을 세 가지 서로 다른 방법으로 배정하는 이야기로 풀어봤어요. (알고리즘 설계 기법이라 법·제도와는 결이 다르지만, 학생회도 복잡한 결정을 명확한 절차로 풀어요.)",
            "Divide-and-conquer, greedy, and dynamic programming, told as a story about the student council allocating twenty clubs' festival budget with three different methods. (These are algorithm design techniques, not law or policy — but even the council solves a hard decision with a clear procedure.)"),
    "panels": [
        {"svg": P1, "alt": ("학생회장이 동아리 스무 곳의 예산 신청을 한 번에 어떻게 정할지 몰라 땀을 흘림", "The council president sweats, unsure how to decide twenty clubs' budget requests all at once"),
         "caption": ("축제 예산 배정, 너무 복잡해요.", "Allocating the festival budget is too complicated."),
         "small": ("동아리가 너무 많아 한 번에 다 비교할 수가 없어요.", "Too many clubs to compare all at once.")},
        {"svg": P2, "alt": ("접수 1등 학생은 다 받았다고 웃고, 꼴찌 학생은 한 푼도 못 받았다고 속상해함", "The student who submitted first smiles, having gotten everything; the last one is upset, having gotten nothing"),
         "caption": ("접수 순서대로만 주면 불합리해요.", "Deciding purely by submission order is unfair."),
         "small": ("순서만 보고 정하면, 더 좋은 방법을 놓쳐요.", "Deciding by order alone misses a better way.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 분할정복·탐욕법·동적계획법 세 가지 방법이 적힌 기준표를 들고, 대표가 옆에서 웃음", "The council president holds a board listing divide-and-conquer, greedy, and dynamic programming, while a rep smiles beside"),
         "caption": ("큰 문제를 푸는 방법은 분할정복·탐욕법·동적계획법, 세 가지예요.", "There are three ways to solve a big problem: divide-and-conquer, greedy, and dynamic programming."),
         "small": ("학생회도 복잡한 결정을 내릴 땐 명확한 절차를 따라야 해요, 알고리즘처럼.", "Even the student council follows a clear step-by-step procedure for a hard decision, just like an algorithm."),
         "tricks": (4, [
             (SPLIT_I, ("분할정복 — 쪼개서 합치기", "Divide & conquer — split, then combine"), ("작은 조각씩 풀고 나중에 합쳐요", "solves small pieces, then merges them"), "calm"),
             (GREEDY_I, ("탐욕법 — 당장 최선 고르기", "Greedy — pick the best right now"), ("매번 지금 가장 좋아 보이는 걸", "always picks what looks best this instant"), "warm"),
             (DP_I, ("동적계획법 — 답 기억해두기", "Dynamic programming — remember the answer"), ("같은 문제를 두 번 안 풀어요", "never solves the same subproblem twice")),
             (STEP_I, ("공통점 — 작은 단위로 다루기", "In common — handle it in small steps"), ("큰 문제를 쪼개 순서대로 풀어요", "breaks the big problem into an ordered sequence")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 분할정복으로 학년별 몫을 나눠 정하고 합침. 오른쪽: 탐욕법으로 급한 곳부터, 동적계획법으로 같은 조합은 다시 안 따짐", "Left: divide-and-conquer splits the budget by grade, then combines. Right: greedy funds the urgent one first; DP avoids re-solving the same combination"),
         "caption": ("세 방법을 축제 예산에 적용하면 이렇게 달라요.", "Applying all three to the festival budget looks like this."),
         "small": ("문제의 생김새에 따라 어울리는 방법이 달라요.", "Which method fits depends on the shape of the problem.")},
        {"svg": P5, "alt": ("왼쪽: 대표가 가장 급한 곳부터 바로 줬다고 말함. 오른쪽: 학생회장이 전체로 보면 더 나은 조합이 있었다고 땀 흘리며 말함", "Left: a rep says they funded the most urgent club right away. Right: a sweating president says a better overall combination existed"),
         "caption": ("탐욕법은 빠르지만 늘 최선은 아니에요.", "Greedy is fast, but not always the best."),
         "small": ("탐욕법은 빠르지만, 매번 전체 최선을 보장하진 않아요.", "Greedy is fast — but it doesn't always guarantee the overall best.")},
    ],
    "summary": (("<b>분할정복</b>은 문제를 <b>쪼개서 합치고</b>, <b>탐욕법</b>은 <b>매번 당장 최선</b>을 고르고, <b>동적계획법</b>은 <b>이미 푼 답을 기억</b>해 다시 안 풀어요.",
                 "<b>Divide-and-conquer</b> <b>splits a problem and combines</b> the results, <b>greedy</b> always <b>picks the best choice right now</b>, and <b>dynamic programming</b> <b>remembers an already-solved answer</b> instead of re-solving it."),
                ("분할정복은 문제를 독립된 작은 부분 문제로 나눠 각각 해결한 뒤 결과를 합치는 전략이에요(병합정렬 등). 탐욕법은 전체 최적을 고려하지 않고 매 단계 가장 좋아 보이는 선택을 반복하는 전략으로, 빠르지만 항상 전역 최적을 보장하진 않아요(최소신장트리 등 일부 문제에서는 보장돼요). 동적계획법은 부분 문제들이 겹칠 때 한 번 계산한 결과를 저장해두고(메모이제이션) 재사용함으로써 중복 계산을 피해요(최적부분구조와 중복부분문제가 있는 문제에 적합). 세 전략 모두 큰 문제를 더 작은 단위로 다루지만, 쪼갠 조각을 다루는 방식이 서로 달라요.",
                 "Divide-and-conquer splits a problem into independent smaller subproblems, solves each, and combines the results (e.g., merge sort). Greedy repeatedly picks whatever choice looks best at each step without considering the whole picture — fast, but not always globally optimal (though for some problems, like minimum spanning trees, it is). Dynamic programming stores the result of a subproblem once computed (memoization) and reuses it, avoiding redundant recomputation — suited to problems with optimal substructure and overlapping subproblems. All three handle a big problem in smaller pieces, but they differ in how they treat those pieces.")),
    "glossary": [
        ("분할정복", "Divide and Conquer", ("문제를 쪼개 따로 풀고 합치는 전략.", "Splitting a problem, solving the pieces, then combining."), ('정렬에서 실제로 쓰이는 예시가 있어요. → <a href="sortalgo-ko.html">크기 순서로 차를 세우는 여러 방법</a>', 'Sorting gives a concrete example. → <a href="sortalgo-en.html">different ways to line cars up by size</a>')),
        ("탐욕법", "Greedy Algorithm", ("매번 지금 가장 좋아 보이는 것을 고르는 전략.", "Picking whatever looks best right now, every time."), ('모든 지점을 가장 싸게 잇는 문제에서 실제로 성립해요. → <a href="mstalgo-ko.html">가장 싼 배관만 골라 모든 지점 잇기</a>', 'Actually provably optimal for connecting everything cheaply. → <a href="mstalgo-en.html">piping every branch together for the least cost</a>')),
        ("동적계획법", "Dynamic Programming", ("이미 푼 답을 기억해두고 재사용하는 전략.", "Remembering an already-solved answer and reusing it."), ("같은 부분 문제를 두 번 풀지 않아요.", "Never solves the same subproblem twice.")),
        ("메모이제이션", "Memoization", ("한 번 계산한 결과를 저장해두는 기법.", "The technique of storing a result once it's computed."), ("동적계획법을 실제로 구현하는 방법이에요.", "The way dynamic programming is actually implemented.")),
        ("최적부분구조", "Optimal Substructure", ("부분 문제의 최적 답을 모으면 전체 최적이 되는 성질.", "The property that optimal sub-answers combine into the optimal whole."), ("동적계획법이 통하려면 이 성질이 있어야 해요.", "Dynamic programming only works when this property holds.")),
        ("중복부분문제", "Overlapping Subproblems", ("똑같은 작은 문제가 여러 번 반복해서 나오는 것.", "The same small problem showing up again and again."), ("이게 있어야 메모이제이션이 효과가 있어요.", "Memoization only pays off when this is present.")),
        ("백트래킹", "Backtracking", ("가다가 막히면 되돌아가 다른 길을 찾는 방법.", "Backing up and trying another path when stuck."), ("또 다른 큰 문제 풀이 전략이에요.", "Yet another strategy for tackling a big problem.")),
        ("시간복잡도(Big-O)", "Time Complexity (Big-O)", ("문제가 커질 때 얼마나 느려지는지 재는 자.", "The ruler that measures how much slower things get as a problem grows."), ('세 방법 모두 이 자로 빠르기를 비교해요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'All three methods are compared using this same ruler. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
    ],
}
