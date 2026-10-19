from _draw import *
from _world import *


def dial(x, y, s=1.0, val=50, color="var(--accent)"):
    """엔진 튜닝 다이얼 하나(=개체/유전자)."""
    ang = -90 + val / 100 * 180
    import math
    rx, ry = 20 * math.cos(math.radians(ang)), 20 * math.sin(math.radians(ang))
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="24" fill="var(--panel)" stroke="{color}" stroke-width="3"/>'
            f'<path d="M0 0 L{rx:.0f} {ry:.0f}" stroke="{color}" stroke-width="3" stroke-linecap="round"/>'
            f'<text y="40" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink)">{val}</text></g>')


# 1. 엔진이 가장 잘 나가는 설정을 못 찾았어요
P1 = svg(300, sky(300)
         + car(380, 220, 1.2)
         + person(560, 150, s=0.85, face=EYES, **MECH1)
         + dial(260, 110, 0.9, 30) + dial(300, 110, 0.9, 60) + dial(460, 110, 0.9, 45)
         + label(380, 50, "⟦엔진이 가장 잘 나가는 다이얼 설정을 찾고 싶어요|we want the dial settings where the engine runs best⟧", 13, "var(--ink)")
         + label(380, 270, "⟦경우의 수가 너무 많아서 하나하나 다 못 해봐요|too many combinations to try them all⟧", 12, "var(--muted)"))

# 2. 하나씩 손으로 맞춰보면 끝이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(260, 150, s=0.85, face=FROWN + SWEAT, **MECH1)
         + dial(440, 120, 1.0, 20) + dial(540, 120, 1.0, 70)
         + label(490, 190, "⟦이 조합? 저 조합?|this combo? that combo?⟧", 12, "var(--bad)", cls="d")
         + label(380, 60, "⟦하나씩 손으로 맞춰보면 끝이 없어요|trying each combo by hand never ends⟧", 13, "var(--ink)")
         + label(380, 260, "⟦잘 나가는 설정끼리 섞어보는 방법이 필요해요|we need a way to mix the good settings together⟧", 12, "var(--muted)"))

# 3. 유전 알고리즘 = 잘 나가는 설정끼리 섞고, 가끔 비틀어 더 나은 세대를 찾는 것 (hero)
P3 = svg(340, sky(340)
         + dial(200, 150, 1.0, 72, "var(--good)") + dial(320, 150, 1.0, 68, "var(--good)")
         + label(260, 230, "⟦1세대: 잘 나가는 둘|generation 1: the two best performers⟧", 11, "var(--muted)")
         + dial(500, 150, 1.2, 80, "var(--accent)")
         + label(500, 230, "⟦2세대: 둘을 섞은 더 나은 설정|generation 2: a better mix of the two⟧", 11, "var(--muted)")
         + label(380, 30, "⟦유전 알고리즘 = 잘 나가는 설정끼리 섞고, 가끔 비틀어 더 나은 세대를 찾는 것|genetic algorithm: mix the best settings, twist a little, find better generations⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦여러 세대를 거치며 점점 더 좋은 설정에 가까워져요|over many generations, it edges closer to the best setting⟧", 12, "var(--muted)"))

POP_I = icon('<circle cx="16" cy="20" r="8" fill="var(--line)"/><circle cx="32" cy="14" r="8" fill="var(--line)"/><circle cx="48" cy="22" r="8" fill="var(--line)"/><circle cx="24" cy="38" r="8" fill="var(--line)"/><circle cx="42" cy="40" r="8" fill="var(--line)"/>')
FIT_I = icon('<path d="M10 50 h44" stroke="var(--ink)" stroke-width="3"/><rect x="14" y="34" width="8" height="16" fill="var(--bad)"/><rect x="28" y="22" width="8" height="28" fill="var(--good)"/><rect x="42" y="30" width="8" height="20" fill="var(--accent)"/>')
CROSS_I = icon('<circle cx="18" cy="24" r="10" fill="var(--good)"/><circle cx="46" cy="24" r="10" fill="var(--accent)"/><path d="M18 34 Q32 44 46 34" stroke="var(--ink)" stroke-width="3" fill="none"/><circle cx="32" cy="48" r="9" fill="var(--good)" stroke="var(--accent)" stroke-width="3"/>')
MUT_I = icon('<circle cx="32" cy="32" r="14" fill="var(--line)"/><path d="M32 10 l4 10 l-8 0z" fill="var(--bad)"/><path d="M48 22 l2 1" stroke="var(--bad)" stroke-width="3"/>')

# 4. 세대를 거듭하는 과정
P4 = svg(320, sky(320)
         + queueboard(60, 40, 640, 240, "⟦한 세대가 하는 일|what happens in one generation⟧",
                      ("⟦① 여러 설정(개체군)을 만들어요|① create many settings (population)⟧",
                       "⟦② 잘 나가는 정도(적합도)를 점수 매겨요|② score how well each one runs (fitness)⟧",
                       "⟦③ 잘 나가는 것끼리 섞어요(교배)|③ mix the good ones together (crossover)⟧",
                       "⟦④ 가끔 무작위로 살짝 비틀어요(돌연변이)|④ occasionally twist one randomly (mutation)⟧",
                       "⟦⑤ 다음 세대로 반복해요|⑤ repeat for the next generation⟧"), 1.0))

# 5. 항상 완벽한 설정을 찾는 건 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + dial(190, 150, 1.1, 88, "var(--good)")
         + label(190, 240, "⟦여러 세대 뒤 꽤 좋은 설정을 찾아요|after many generations, finds a pretty good setting⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **CHIEF)
         + label(570, 240, "⟦다만 '가장 완벽한 설정'이라고 보장하진 않아요|but it never guarantees the single perfect setting⟧", 11, "var(--ink)")
         + label(380, 282, "⟦경우의 수가 너무 많을 때 '꽤 괜찮은 답'을 빠르게 찾는 방법이에요|a way to find a pretty good answer fast, when there are too many options⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "geneticalgo", "order": 18,
    "title": ("잘 나가는 다이얼 설정끼리 섞어보기", "Mixing the Best Dial Settings Together"),
    "h1": ("<em>유전 알고리즘</em>이 뭐예요?", "What is a <em>Genetic Algorithm</em>?"),
    "sub": ("유전 알고리즘을, 엔진이 가장 잘 나가는 다이얼 설정을 여러 세대에 걸쳐 섞고 비틀어 찾아가는 이야기로 풀어봤어요.",
            "Genetic algorithms, told as a story about mixing and twisting engine-tuning dial settings across generations to find the best one."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 엔진이 가장 잘 나가는 다이얼 조합을 찾지 못해 고민함", "The mechanic struggles to find which dial combination makes the engine run best"),
         "caption": ("엔진이 가장 잘 나가는 설정을 찾고 싶어요.", "We want the dial settings where the engine runs best."),
         "small": ("경우의 수가 너무 많아서 하나하나 다 못 해봐요.", "Too many combinations to try them all.")},
        {"svg": P2, "alt": ("정비사가 다이얼 조합을 하나씩 손으로 맞춰보며 지침", "The mechanic wearily tries dial combinations one by one"),
         "caption": ("하나씩 손으로 맞춰보면 끝이 없어요.", "Trying each combo by hand never ends."),
         "small": ("잘 나가는 설정끼리 섞어보는 방법이 필요해요.", "We need a way to mix the good settings together.")},
        {"svg": P3, "hero": True, "alt": ("잘 나가는 두 다이얼 설정이 섞여 더 나은 2세대 설정이 됨", "Two well-performing dial settings mix into a better second-generation setting"),
         "caption": ("유전 알고리즘은 잘 나가는 설정끼리 섞고 비틀어 찾는 것이에요.", "A genetic algorithm mixes the best settings, twisting occasionally, to search for better ones."),
         "small": ("여러 세대를 거치며 점점 더 좋은 설정에 가까워져요.", "Over many generations, it edges closer to the best setting."),
         "tricks": (4, [
             (POP_I, ("개체군 만들기", "Create a population"), ("여러 설정을 한꺼번에 만들어요", "makes many settings at once"), "calm"),
             (FIT_I, ("적합도 점수 매기기", "Score fitness"), ("얼마나 잘 나가는지 매겨요", "scores how well each runs")),
             (CROSS_I, ("교배(섞기)", "Crossover"), ("잘 나가는 둘을 섞어 자식을 만들어요", "mixes two good ones into a child")),
             (MUT_I, ("돌연변이(비틀기)", "Mutation"), ("가끔 무작위로 살짝 바꿔요", "occasionally twists one at random"), "warm"),
         ])},
        {"svg": P4, "alt": ("개체군 생성, 적합도 평가, 교배, 돌연변이, 반복으로 이어지는 한 세대의 다섯 단계", "The five steps of one generation: population, fitness, crossover, mutation, repeat"),
         "caption": ("한 세대는 다섯 단계를 거쳐요.", "One generation goes through five steps."),
         "small": ("이 과정을 세대마다 반복해요.", "This process repeats generation after generation.")},
        {"svg": P5, "alt": ("왼쪽: 여러 세대 뒤 꽤 좋은 설정을 찾음. 오른쪽: 가장 완벽한 설정이라는 보장은 없음", "Left: after many generations, a pretty good setting is found. Right: it's never guaranteed to be the perfect one"),
         "caption": ("항상 완벽한 설정을 찾는 건 아니에요.", "It doesn't always find the single perfect setting."),
         "small": ("경우의 수가 너무 많을 때 꽤 괜찮은 답을 빠르게 찾는 방법이에요.", "A way to find a pretty good answer fast, when there are too many options.")},
    ],
    "summary": (("<b>유전 알고리즘</b>은 여러 설정(개체군) 중 <b>잘 나가는 것끼리 섞고</b>, 가끔 <b>무작위로 비틀며</b>, 세대를 거듭해 <b>점점 더 나은 답</b>을 찾는 방법이에요.",
                 "A <b>genetic algorithm</b> <b>mixes well-performing settings</b> from a population, occasionally applies a <b>random twist</b>, and across generations searches for a <b>progressively better answer</b>."),
                ("유전 알고리즘은 생물의 진화 과정(선택·교배·돌연변이)을 본뜬 최적화 기법이에요. 여러 후보 해(개체)로 이루어진 개체군을 만들고, 적합도 함수로 각 개체의 성능을 평가한 뒤, 적합도가 높은 개체들을 선택해 교차(crossover)로 자식 개체를 만들고, 낮은 확률로 돌연변이(mutation)를 가해 다양성을 유지해요. 이 과정을 여러 세대 반복하며 최적해에 가까운 답으로 수렴해 가지만, 전역 최적해를 보장하지는 않아요.",
                 "A genetic algorithm is an optimization technique modeled on biological evolution — selection, crossover, and mutation. It builds a population of candidate solutions, scores each with a fitness function, selects the fitter ones to produce offspring via crossover, and applies mutation at low probability to preserve diversity. Repeating this over many generations converges toward a near-optimal answer, though it never guarantees the global optimum.")),
    "glossary": [
        ("개체군", "Population", ("한 세대에 있는 여러 다이얼 설정들.", "The many dial settings in one generation."), ("후보 해들의 모임이에요.", "A collection of candidate solutions.")),
        ("적합도 함수", "Fitness Function", ("얼마나 잘 나가는지 매기는 점수표.", "The scorecard for how well a setting performs."), ("어떤 개체를 남길지 정하는 기준이에요.", "Decides which individuals survive.")),
        ("선택", "Selection", ("잘 나가는 설정을 골라내는 것.", "Picking out the well-performing settings."), ("적합도가 높을수록 뽑힐 확률이 높아요.", "Higher fitness means a higher chance of being picked.")),
        ("교배(교차)", "Crossover", ("두 설정을 섞어 새 설정을 만드는 것.", "Mixing two settings into a new one."), ("부모의 좋은 특징을 물려받아요.", "Inherits good traits from both parents.")),
        ("돌연변이", "Mutation", ("가끔 무작위로 설정을 살짝 바꾸는 것.", "Occasionally twisting a setting at random."), ("다양성을 유지해 막다른 길을 피해요.", "Keeps diversity, avoiding dead ends.")),
        ("세대", "Generation", ("개체군을 한 번 갱신하는 단위.", "One cycle of updating the population."), ("세대를 거듭할수록 점점 나아져요.", "Gets better generation after generation.")),
        ("지역 최적해", "Local Optimum", ("꽤 좋지만 가장 좋진 않은 설정.", "A pretty good setting, but not the very best."), ("유전 알고리즘이 여기 갇힐 수도 있어요.", "A genetic algorithm can get stuck here.")),
        ("메타휴리스틱", "Metaheuristic", ("완벽한 답 대신 괜찮은 답을 빨리 찾는 전략군.", "A family of strategies for a good-enough answer, fast."), ("유전 알고리즘이 여기 속해요.", "Genetic algorithms belong to this family.")),
    ],
}
