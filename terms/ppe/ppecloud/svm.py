from _draw import *
from _world import *

# 1. 입주 심사관이 "조용한 입주사"와 "시끄러운 입주사"를 나눠야 해요
P1 = svg(300, sky(300)
         + person(380, 188, s=0.85, face=EYES, **MANAGER)
         + '<circle cx="220" cy="230" r="8" fill="var(--good)"/><circle cx="260" cy="200" r="8" fill="var(--good)"/><circle cx="200" cy="180" r="8" fill="var(--good)"/>'
         + '<circle cx="520" cy="230" r="8" fill="var(--accent)"/><circle cx="560" cy="200" r="8" fill="var(--accent)"/><circle cx="500" cy="180" r="8" fill="var(--accent)"/>'
         + label(230, 150, "⟦조용한 입주사|quiet tenants⟧", 11, "var(--good)")
         + label(540, 150, "⟦시끄러운 입주사|noisy tenants⟧", 11, "var(--accent)")
         + label(380, 282, "⟦앞으로 들어올 입주사가 어느 쪽인지 미리 갈라서 보고 싶어요|wants to tell which new tenants will land on which side, ahead of time⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 아무렇게나 선을 그으면 애매한 경우가 많이 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<circle cx="220" cy="130" r="8" fill="var(--good)"/><circle cx="280" cy="90" r="8" fill="var(--good)"/><circle cx="240" cy="190" r="8" fill="var(--good)"/>'
         + '<circle cx="500" cy="130" r="8" fill="var(--accent)"/><circle cx="440" cy="170" r="8" fill="var(--accent)"/><circle cx="480" cy="90" r="8" fill="var(--accent)"/>'
         + '<path d="M250 60 L430 220" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 4"/>'
         + label(380, 40, "⟦아무렇게나 그은 선|a carelessly drawn line⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦선을 대충 그으면, 두 그룹과 너무 가까워서 애매한 새 입주사를 자주 틀려요|a careless line misjudges new tenants that land too close to either side⟧", 12, "var(--ink)"))

# 3. hero: SVM = 두 그룹을 가장 넓게 갈라놓는 경계선을 긋는 심사관
P3 = svg(340, sky(340)
         + '<circle cx="200" cy="140" r="9" fill="var(--good)"/><circle cx="250" cy="100" r="9" fill="var(--good)"/><circle cx="230" cy="190" r="9" fill="var(--good)"/>'
         + '<circle cx="540" cy="140" r="9" fill="var(--accent)"/><circle cx="490" cy="180" r="9" fill="var(--accent)"/><circle cx="510" cy="100" r="9" fill="var(--accent)"/>'
         + '<circle cx="250" cy="100" r="13" fill="none" stroke="var(--night)" stroke-width="2"/><circle cx="510" cy="100" r="13" fill="none" stroke="var(--night)" stroke-width="2"/>'
         + '<path d="M300 40 L440 260" stroke="var(--night)" stroke-width="4"/>'
         + '<path d="M250 80 L390 300" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="5 4"/>'
         + '<path d="M350 20 L490 240" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="5 4"/>'
         + label(380, 30, "⟦SVM = 두 그룹에서 가장 멀리 떨어진 경계선을 긋는 심사관|SVM = the reviewer who draws the line farthest from both groups⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦경계에 가장 가까운 점(서포트 벡터)만 보고 선을 그어요|it draws the line by watching only the closest points — the support vectors⟧", 11, "var(--muted)"))

# 4. 작동 디테일: 마진 폭 비교 — 좁은 마진 vs 넓은 마진
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦왜 '가장 넓게' 가르나요|why the \"widest\" split⟧",
                     ("⟦마진 = 경계선과 가장 가까운 점 사이 여유 폭|margin = the gap between the line and the closest points⟧",
                      "⟦마진이 넓을수록 새 입주사를 더 잘 맞혀요|a wider margin predicts new tenants more reliably⟧",
                      "⟦서포트 벡터 = 그 여유 폭을 정하는 경계의 점들|support vectors = the boundary points that set that gap⟧",
                      "⟦선이 휘어야 할 땐 커널 트릭으로 공간을 바꿔요|when the split needs to curve, a kernel trick reshapes the space⟧"), 1.0))

# 5. 깨지는 곳: 사실 이건 클라우드 인프라 이야기가 아니라 분류 알고리즘이에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.75, face=EYES, **MANAGER)
         + label(190, 260, "⟦이 건물 비유는 여기서부터 좀 억지예요|this building metaphor gets a bit forced here⟧", 11, "var(--ink)")
         + label(570, 150, "⟦SVM|SVM⟧", 28, "var(--good)", cls="d")
         + label(570, 190, "⟦실제로는 클라우드 인프라가 아니라|it's not actually cloud infrastructure⟧", 11, "var(--ink)")
         + label(570, 215, "⟦전통적인 머신러닝 분류 알고리즘이에요|it's a classic machine-learning classification algorithm⟧", 11, "var(--ink)"))

MARGIN_I = icon('<path d="M10 54 L54 10" stroke="var(--night)" stroke-width="4"/><path d="M18 54 L54 18" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="4 3"/><path d="M10 46 L46 10" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="4 3"/>')
SUPPORT_I = icon('<circle cx="24" cy="24" r="9" fill="var(--good)"/><circle cx="24" cy="24" r="14" fill="none" stroke="var(--night)" stroke-width="2"/><circle cx="44" cy="44" r="9" fill="var(--accent)"/><circle cx="44" cy="44" r="14" fill="none" stroke="var(--night)" stroke-width="2"/>')
KERNEL_I = icon('<path d="M8 40 Q32 8 56 40" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CLASSIFY_I = icon('<rect x="8" y="8" width="20" height="20" rx="4" fill="var(--good)"/><rect x="36" y="36" width="20" height="20" rx="4" fill="var(--accent)"/>')

PAGE = {
    "slug": "svm", "order": 6,
    "title": ("두 그룹을 가장 넓게 갈라놓는 선", "The Line That Splits Two Groups the Widest"),
    "h1": ("<em>SVM(서포트벡터머신)</em>이 뭐예요?", "What is <em>SVM (Support Vector Machine)</em>?"),
    "sub": ("SVM을, 두 입주사 그룹을 가장 넓게 갈라놓는 경계선을 긋는 심사관 이야기로 풀어봤어요.",
            "SVM, told as a story about a reviewer drawing the line that splits two tenant groups as widely as possible."),
    "panels": [
        {"svg": P1, "alt": ("심사관이 조용한 입주사 그룹과 시끄러운 입주사 그룹을 점으로 바라보며 어느 쪽인지 미리 갈라보고 싶어 함", "A reviewer looks at dots for quiet tenants and noisy tenants, wanting to tell them apart ahead of time"),
         "caption": ("앞으로 들어올 입주사가 어느 쪽인지 미리 갈라서 보고 싶어요.", "Wants to tell which new tenants will land on which side, ahead of time."),
         "small": ("조용한 쪽과 시끄러운 쪽, 두 그룹이에요.", "Two groups: the quiet side and the noisy side.")},
        {"svg": P2, "alt": ("두 그룹 사이에 아무렇게나 그은 선이 양쪽 점들과 너무 가까워 애매함", "A carelessly drawn line between the two groups sits too close to both sides, making it unclear"),
         "caption": ("선을 대충 그으면 애매한 경우를 자주 틀려요.", "A careless line misjudges cases that land too close to either side."),
         "small": ("선이 한쪽에 너무 붙어 있으면 안 돼요.", "The line can't hug one side too closely.")},
        {"svg": P3, "hero": True, "alt": ("두 그룹 사이에 가장 넓은 간격을 두고 그은 굵은 경계선과, 그 경계에 가장 가까운 두 점에 원이 쳐져 있음", "A thick boundary line drawn with the widest possible gap between two groups, with circles marking the two closest points to that boundary"),
         "caption": ("SVM = 두 그룹에서 가장 멀리 떨어진 경계선을 긋는 심사관이에요.", "SVM = the reviewer who draws the line farthest from both groups."),
         "small": ("경계에 가장 가까운 점(서포트 벡터)만 보고 선을 그어요.", "It draws the line by watching only the closest points — the support vectors."),
         "tricks": (4, [
             (MARGIN_I, ("가장 넓은 간격을 찾아요", "Finds the widest possible gap"), ("마진이라고 불러요", "called the margin"), "calm"),
             (SUPPORT_I, ("경계에 가장 가까운 점만 봐요", "Watches only the closest points"), ("서포트 벡터라고 불러요", "called support vectors")),
             (KERNEL_I, ("선이 휘어야 할 땐 공간을 바꿔요", "Reshapes the space when the split must curve"), ("커널 트릭이라고 불러요", "called the kernel trick"), "warm"),
             (CLASSIFY_I, ("결국 둘 중 하나로 분류해요", "Ends up classifying into one of two"), ("분류 알고리즘이에요", "it's a classification algorithm")),
         ])},
        {"svg": P4, "alt": ("마진이 경계선과 가장 가까운 점 사이 여유 폭임을 보여주고, 넓을수록 잘 맞히며, 서포트 벡터가 그 폭을 정하고, 휘어야 할 땐 커널 트릭을 쓴다고 설명", "Explains margin as the gap between the line and closest points, wider is more reliable, support vectors set that gap, and a kernel trick is used when curving is needed"),
         "caption": ("'가장 넓게'가 핵심이에요.", "\"The widest\" is the whole point."),
         "small": ("마진이 넓을수록 애매한 경우에도 더 잘 맞혀요.", "A wider margin predicts even borderline cases more reliably.")},
        {"svg": P5, "alt": ("왼쪽: 심사관이 이 건물 비유가 여기부터 억지라고 인정함. 오른쪽: SVM은 실제로 클라우드 인프라가 아니라 전통적인 머신러닝 분류 알고리즘이라는 설명", "Left: the reviewer admits this building metaphor gets forced from here. Right: an explanation that SVM is actually a classic machine-learning classification algorithm, not cloud infrastructure"),
         "caption": ("사실 이건 클라우드 인프라 이야기가 아니에요.", "This isn't actually a cloud-infrastructure story."),
         "small": ("SVM은 전통적인 머신러닝 분류 알고리즘이에요 — 시험 범위라 다뤘지만, 이 건물 비유는 여기서 멈출게요.", "SVM is a classic machine-learning classification algorithm — covered here because it's on the exam list, but the building metaphor stops here.")},
    ],
    "summary": (("<b>SVM</b> = 두 그룹 사이에 <b>가장 넓은 여유(마진)</b>를 두고 경계선을 긋는 <b>분류 알고리즘</b>. 경계에 가장 가까운 점(<b>서포트 벡터</b>)만으로 선이 정해져요.",
                 "<b>SVM</b> is a <b>classification algorithm</b> that draws a boundary with the <b>widest possible margin</b> between two groups. The line is set using only the closest points — the <b>support vectors</b>."),
                ("SVM(Support Vector Machine)은 두 클래스를 나누는 초평면(결정 경계)을 마진이 최대가 되도록 찾는 지도학습 분류 기법이에요. 선형으로 나눌 수 없는 데이터는 커널 트릭으로 고차원 공간에 매핑해 나눠요. 클라우드 인프라 주제가 아니라 전통적인 머신러닝 알고리즘이라, 이 페이지만 비유가 다른 페이지보다 느슨해요.",
                 "SVM (Support Vector Machine) is a supervised classification technique that finds the hyperplane (decision boundary) separating two classes with the maximum margin. Data that can't be split linearly gets mapped into a higher-dimensional space via the kernel trick. Since this is a classic ML algorithm rather than a cloud-infrastructure topic, this page's building metaphor is intentionally looser than the others.")),
    "glossary": [
        ("SVM", "Support Vector Machine", ("두 그룹을 가장 넓게 가르는 심사관.", "The reviewer splitting two groups the widest."), ("지도학습 분류 알고리즘이에요.", "A supervised-learning classification algorithm.")),
        ("결정 경계(초평면)", "Decision boundary (hyperplane)", ("두 그룹을 가르는 경계선.", "The line separating the two groups."), ("데이터 차원이 늘면 평면(초평면)이 돼요.", "In higher dimensions, this line becomes a hyperplane.")),
        ("마진", "Margin", ("경계선과 가장 가까운 점 사이 여유 폭.", "The gap between the line and the closest points."), ("넓을수록 새 데이터를 더 잘 맞혀요.", "Wider margins predict new data more reliably.")),
        ("서포트 벡터", "Support vector", ("경계에 가장 가까운, 선을 정하는 점들.", "The closest points, the ones that actually set the line."), ("이 점들만 바뀌어도 경계선이 바뀌어요.", "Move just these points, and the boundary moves too.")),
        ("커널 트릭", "Kernel trick", ("직선으로 못 가를 때 공간을 바꾸는 방법.", "The trick of reshaping the space when a straight line won't do."), ("휘어진 경계도 그릴 수 있게 해줘요.", "Lets the boundary curve when it needs to.")),
        ("지도학습", "Supervised learning", ("정답이 있는 데이터로 배우는 방식.", "Learning from data that already has labeled answers."), ("조용한 입주사/시끄러운 입주사처럼 라벨이 미리 있어요.", "Like already knowing which tenants are quiet vs noisy, ahead of time.")),
        ("분류", "Classification", ("둘 중 하나로 나누는 일.", "Sorting into one of two groups."), ("SVM이 결국 하는 일이에요.", "What SVM ultimately does.")),
        ("과적합", "Overfitting", ("훈련 데이터에만 너무 딱 맞춘 경계선.", "A boundary fit too tightly to the training data."), ("마진을 너무 좁게 잡으면 생기기 쉬워요.", "More likely when the margin is drawn too tight.")),
    ],
}
