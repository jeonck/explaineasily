from _draw import *
from _world import *


def scatter(points, s=1.0, color="var(--accent)"):
    return "".join(produce(x, y, s, color) for x, y in points)


def dashed_ring(cx, cy, r, color="var(--accent)"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="3" stroke-dasharray="6 6"/>'


GROUP_A = [(140, 150), (170, 180), (120, 190), (160, 130), (190, 160)]
GROUP_B = [(400, 140), (430, 170), (460, 150), (410, 190), (450, 120)]
GROUP_C = [(620, 160), (650, 190), (600, 200), (640, 140)]
NOISE_PT = [(300, 250)]

# 1. 이름표 없는 작물이 잔뜩 쏟아져요
P1 = svg(300, sky(300)
         + label(380, 25, "⟦이 작물들, 이름표가 하나도 없어요|none of this produce has a label at all⟧", 13, "var(--bad)", cls="d")
         + scatter(GROUP_A + GROUP_B + GROUP_C + NOISE_PT, 0.9, "var(--accent)")
         + person(60, 150, s=0.7, face=SWEAT + EYES, **OPERATOR)
         + label(380, 285, "⟦훈련 교사도 없고, 정답 분류함 이름도 안 적혀 있어요|no teacher this time, and the bins have no names written on them⟧", 12, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 몇 무리로 나눠야 할지, 어디가 경계인지도 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 25, "⟦몇 무리로 나눠야 하죠? 경계는 어디죠?|how many groups should there be? and where's the line?⟧", 13, "var(--bad)", cls="d")
         + scatter(GROUP_A + GROUP_B + GROUP_C + NOISE_PT, 0.9, "var(--accent)")
         + person(60, 150, s=0.7, face=FROWN, **OPERATOR)
         + label(380, 285, "⟦몇 무리인지, 경계가 어딘지 아무도 안 적어 줬어요|nobody wrote down how many groups there should be, or where to draw the line⟧", 12, "var(--ink)", cls="d"))

# 3. 군집분석 = 정답 라벨 없이, 비슷한 것끼리 스스로 묶는 방법 (hero)
P3 = svg(320, sky(320)
         + dashed_ring(155, 160, 55, "var(--good)") + scatter(GROUP_A, 0.9, "var(--good)")
         + dashed_ring(435, 155, 55, "var(--accent)") + scatter(GROUP_B, 0.9, "var(--accent)")
         + dashed_ring(628, 172, 50, "var(--bad)") + scatter(GROUP_C, 0.9, "var(--bad)")
         + produce(300, 250, 0.9, "var(--muted)") + label(300, 280, "⟦어디에도 안 낀 것|fits in nowhere⟧", 10, "var(--muted)")
         + label(380, 25, "⟦군집분석 = 정답 라벨 없이, 비슷한 것끼리 스스로 묶는 방법이에요|clustering groups look-alikes together on its own, with no answer key to follow⟧", 13, "var(--ink)", cls="d"))

CENTER_I = icon('<circle cx="32" cy="32" r="6" fill="var(--accent)"/><circle cx="18" cy="20" r="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><circle cx="46" cy="22" r="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><circle cx="20" cy="46" r="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>')
NEAR_I = icon('<circle cx="22" cy="32" r="8" fill="var(--good)"/><circle cx="40" cy="26" r="8" fill="var(--good)"/><path d="M28 30 L36 28" stroke="var(--good)" stroke-width="3"/>')
DENSE_I = icon('<circle cx="24" cy="24" r="5" fill="var(--accent)"/><circle cx="34" cy="22" r="5" fill="var(--accent)"/><circle cx="28" cy="34" r="5" fill="var(--accent)"/><circle cx="38" cy="34" r="5" fill="var(--accent)"/><circle cx="50" cy="50" r="5" fill="var(--muted)"/>')
NOISE_I = icon('<circle cx="24" cy="30" r="5" fill="var(--accent)"/><circle cx="34" cy="28" r="5" fill="var(--accent)"/><circle cx="50" cy="48" r="5" fill="none" stroke="var(--muted)" stroke-width="3" stroke-dasharray="3 3"/>')

PAGE = {
    "slug": "clustering", "order": 6,
    "title": ("이름표 없이 비슷한 것끼리 모으기", "Grouping by Likeness, With No Name Tags"),
    "h1": ("<em>군집분석</em>이 뭐예요?", "What is <em>Clustering</em>?"),
    "sub": ("군집분석을, 이름표도 정답도 없는 작물 더미를 비슷한 것끼리 스스로 묶는 이야기로 풀어봤어요.",
            "Clustering, told as a story about grouping a pile of unlabeled produce by likeness alone, with no answer key to follow."),
    "panels": [
        {"svg": P1, "alt": ("이름표 없는 작물이 잔뜩 흩어져 있고, 선별기 조작원이 진땀을 흘림", "A scatter of unlabeled produce with no names, and the operator sweating over it"),
         "caption": ("이름표 없는 작물이 잔뜩 쏟아져요.", "A pile of unlabeled produce comes pouring in."),
         "small": ("훈련 교사도 없고, 분류함 이름도 안 적혀 있어요.", "No teacher this time, and the bins have no names on them.")},
        {"svg": P2, "alt": ("조작원이 몇 무리로 나눠야 할지, 경계가 어딘지 묻는 말풍선을 띄움", "The operator wonders aloud how many groups there should be and where the boundary falls"),
         "caption": ("몇 무리인지, 경계가 어딘지도 몰라요.", "Nobody knows how many groups there should be, or where the line falls."),
         "small": ("정답이 없으니, 스스로 판단해야 해요.", "With no answer key, it has to judge for itself.")},
        {"svg": P3, "hero": True, "alt": ("비슷한 작물끼리 점선 원으로 세 무리가 묶이고, 어디에도 끼지 못한 작물 하나가 따로 남음", "Similar produce gets grouped into three dashed-circle clusters, with one leftover item fitting into none of them"),
         "caption": ("정답 라벨 없이, 비슷한 것끼리 스스로 묶는 방법이에요.", "It groups look-alikes together on its own, with no answer key."),
         "small": ("어디에도 안 낀 건 소음(노이즈)으로 남겨둬요.", "The one that fits nowhere is simply left as noise."),
         "tricks": (4, [
             (CENTER_I, ("중심점부터 잡기", "Plant a center point"), ("무리의 한가운데를 정해요", "picking the middle of a group"), "calm"),
             (NEAR_I, ("가까운 것끼리 묶기", "Group the nearby ones"), ("거리가 가까운 것들을 모아요", "gathering whatever sits close together")),
             (DENSE_I, ("빽빽한 곳 찾기", "Find the dense spots"), ("촘촘히 모인 곳을 무리로 봐요", "treating a tight cluster as one group"), "warm"),
             (NOISE_I, ("못 낀 건 소음으로 두기", "Leave the leftovers as noise"), ("억지로 어디에 넣지 않아요", "not forcing it into any group")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦두 가지 묶는 방식|TWO WAYS TO GROUP⟧",
                 ("⟦K-평균(K-means) — 무리 개수(K)를 미리 정함|K-means — the number of groups is fixed in advance⟧",
                  "⟦K-평균 — 중심점에서 가까운 것끼리 묶음, 둥근 무리|K-means — groups by distance to a center, round clusters⟧",
                  "⟦DBSCAN — 빽빽한 밀도로 무리를 찾음, 개수 안 정해도 됨|DBSCAN — finds groups by density, no fixed count needed⟧",
                  "⟦DBSCAN — 아무 무리에도 안 낀 점은 소음으로 남김|DBSCAN — leaves points that fit nowhere as noise⟧"), 1.0)),
         "alt": ("K-평균과 DBSCAN 두 묶는 방식을 비교한 표", "A board comparing K-means and DBSCAN as two ways to group"),
         "caption": ("묶는 방식에 따라 결과 모양도 달라져요.", "Different methods produce differently shaped groups."),
         "small": ("K-평균은 무리 수를 미리 정하고, DBSCAN은 밀도만 보고 스스로 찾아요.", "K-means fixes the count in advance; DBSCAN finds it on its own, by density alone.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                 + dashed_ring(155, 160, 55, "var(--good)") + scatter(GROUP_A, 0.9, "var(--good)") + label(155, 250, "⟦비슷하게 묶긴 했어요|it grouped the look-alikes⟧", 11, "var(--ink)")
                 + person(570, 140, s=0.75, face=EYES, **INSPECTOR) + label(570, 250, "⟦근데 이게 '사과'무리인지는 몰라요|but it has no idea this group means apples⟧", 11, "var(--ink)")
                 + label(380, 282, "⟦군집분석은 무리를 찾아줄 뿐, 그 무리가 뭘 뜻하는지는 사람이 이름 붙여야 해요|clustering only finds the groups — a person still has to name what each one means⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 비슷한 작물이 무리로 묶임. 오른쪽: 검수반장이 그 무리가 무엇을 뜻하는지는 모른다고 말함", "Left: look-alike produce gets grouped. Right: the inspector notes nobody knows what the group actually means"),
         "caption": ("무리는 찾아도, 이름은 못 붙여요.", "It finds the group — but can't name it."),
         "small": ("정답 라벨로 미리 가르치는 지도학습·로지스틱 회귀와는 정반대 출발점이에요.", "The exact opposite starting point from supervised learning and logistic regression, which teach from labels up front.")},
    ],
    "summary": (("<b>군집분석</b> = 정답 이름표 없이, <b>비슷한 작물끼리</b> 스스로 <b>무리를 찾는</b> 방법.",
                 "<b>Clustering</b> = finding groups of <b>look-alike produce</b> on its own, <b>with no answer labels</b> to start from."),
                ("군집분석(Clustering)은 정답 라벨이 없는 비지도학습(unsupervised learning)의 한 종류로, 데이터 사이의 거리나 밀도를 기준으로 비슷한 것끼리 묶는 방법이에요. K-평균(K-means)은 무리 개수(K)를 미리 정하고 중심점과의 거리로 둥근 무리를 만들고, DBSCAN은 밀도가 높은 곳을 무리로 보고 개수를 미리 정하지 않아도 되며 어디에도 안 속한 점을 노이즈로 남겨요. 군집분석은 무리를 찾아줄 뿐, 그 무리의 의미(라벨)는 사람이 해석해 붙여야 해요.",
                 "Clustering is a form of unsupervised learning — no answer labels exist — that groups look-alike data by distance or density. K-means fixes the number of groups (K) in advance and forms round clusters based on distance to a center point; DBSCAN treats dense regions as groups without needing a fixed count, and leaves points that belong nowhere as noise. Either way, clustering only finds the groups — a person still has to interpret and name what each one means.")),
    "glossary": [
        ("군집분석", "Clustering", ("비슷한 것끼리 스스로 묶는 방법.", "Grouping look-alikes together on its own."), ("정답 라벨이 없는 비지도학습의 한 종류예요.", "A form of unsupervised learning with no answer labels.")),
        ("비지도학습", "Unsupervised learning", ("훈련 교사 없이 배우는 것.", "Learning with no teacher at all."), ('정답 라벨로 가르치는 지도학습과 정반대예요. → <a href="aidataqual-ko.html">상한 씨앗으로 가르친 선별기</a>', 'The opposite of supervised learning, which teaches from labels. → <a href="aidataqual-en.html">A Sorter Trained on Rotten Seed</a>')),
        ("K-평균(K-means)", "K-means", ("무리 개수를 미리 정하고 중심점으로 묶는 방법.", "Fixing the group count in advance and grouping by distance to a center."), ("둥근 모양의 무리를 잘 찾아요.", "Good at finding round-shaped groups.")),
        ("DBSCAN", "DBSCAN", ("밀도가 높은 곳을 무리로 보는 방법.", "Treating dense regions as groups."), ("무리 개수를 미리 안 정해도 되고, 소음도 걸러줘요.", "No fixed count needed, and it filters out noise too.")),
        ("중심점(centroid)", "Centroid", ("K-평균이 잡는 무리의 한가운데.", "The middle point K-means plants for each group."), ("이 점과의 거리로 소속 무리가 정해져요.", "Distance to this point decides which group something belongs to.")),
        ("노이즈(소음)", "Noise", ("아무 무리에도 못 낀 점.", "A point that fits into no group."), ('무리에서 유난히 튀는 점과 이어지는 개념이에요. → <a href="aidataqual-ko.html">상한 씨앗으로 가르친 선별기</a>', 'Connects to the idea of a point that stands out from every group.')),
        ("로지스틱 회귀", "Logistic regression", ("정답 라벨로 미리 가르치는 지도학습 방법.", "A supervised method taught from answer labels up front."), ("군집분석과 정반대 출발점을 가진 이웃 방법이에요.", "A neighboring method that starts from the opposite assumption.")),
        ("차원 축소", "Dimensionality reduction", ("너무 많은 특징을 보기 좋게 줄이는 것.", "Trimming down too many features into something visible."), ("무리를 눈으로 확인하기 전에 흔히 먼저 거치는 단계예요.", "Often the step taken before a cluster can even be seen with the eye.")),
    ],
}
