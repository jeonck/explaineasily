from _draw import *
from _world import *

NORMAL_ROW = [(140, 190), (200, 190), (260, 190), (380, 190), (440, 190), (500, 190), (560, 190), (620, 190)]

# 1. 비슷한 크기 사과들 사이에, 유난히 큰 작물 하나가 있어요
P1 = svg(300, sky(300)
         + conveyor(100, 230, 580)
         + "".join(produce(x, y, 0.9, "var(--good)") for x, y in NORMAL_ROW)
         + produce(320, 170, 2.0, "var(--good)")
         + label(320, 120, "⟦이것만 세 배는 커요|this one's three times the size⟧", 11, "var(--ink)")
         + person(690, 170, s=0.7, face=EYES, **OPERATOR)
         + label(380, 25, "⟦비슷한 크기 사과들 사이에, 유난히 큰 작물 하나가 있어요|among apples of similar size, one stands out — much bigger than the rest⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 눈여겨보지 않으면 평균이 끌려가거나, 진짜 중요한 신호를 놓쳐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.8, face=EYES, **INSPECTOR)
         + label(160, 250, "⟦평균 무게가 확 끌려 올라가요|the average weight gets dragged way up⟧", 11, "var(--ink)")
         + person(420, 150, s=0.8, face=FROWN, **OPERATOR)
         + label(420, 250, "⟦근데 이게 저울 고장 신호일 수도 있어요|but this could be a sign the scale is broken⟧", 11, "var(--ink)")
         + person(640, 150, s=0.8, face=EYES, **TEACHER)
         + label(640, 250, "⟦아니면 정말 귀한 품종일 수도 있고요|or it might just be a genuinely rare variety⟧", 11, "var(--ink)")
         + label(380, 285, "⟦눈여겨보지 않으면 숫자가 끌려가고, 무조건 버리면 진짜 신호를 놓쳐요|ignore it and the numbers get dragged; discard it blindly and a real signal gets lost⟧", 12, "var(--bad)", cls="d"))

CLUSTER_PTS = [(260, 180), (300, 170), (340, 185), (270, 220), (320, 215)]

# 3. 이상치 = 나머지 무리와 통계적으로 확연히 다른 데이터 포인트 (hero)
P3 = svg(320, sky(320)
         + label(380, 25, "⟦이상치 = 나머지 무리와 통계적으로 확연히 다른 데이터 포인트예요|an outlier is a data point that's statistically, clearly unlike the rest of the group⟧", 13, "var(--ink)", cls="d")
         + f'<circle cx="300" cy="200" r="90" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 6"/>'
         + "".join(produce(x, y, 0.85, "var(--good)") for x, y in CLUSTER_PTS)
         + produce(560, 200, 1.8, "var(--good)")
         + f'<path d="M394 200 H524" stroke="var(--bad)" stroke-width="3" stroke-dasharray="3 3"/>'
         + label(560, 270, "⟦무리에서 멀리 떨어진 하나|one far removed from the group⟧", 12, "var(--bad)"))

DIST_I = icon('<circle cx="24" cy="32" r="6" fill="var(--good)"/><circle cx="34" cy="26" r="6" fill="var(--good)"/><circle cx="50" cy="48" r="7" fill="var(--bad)"/><path d="M34 30 L46 44" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 2"/>')
ZSCORE_I = icon('<path d="M8 44 Q32 8 56 44" stroke="var(--accent)" stroke-width="3" fill="none"/><circle cx="52" cy="40" r="4" fill="var(--bad)"/>')
IQR_I = icon('<rect x="16" y="22" width="32" height="20" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><path d="M32 10 V22 M32 42 V54" stroke="var(--accent)" stroke-width="2"/><circle cx="54" cy="12" r="4" fill="var(--bad)"/>')
CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M32 22 v14 M32 42 v2" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "outlier", "order": 9,
    "title": ("무리에서 유난히 튀는 작물", "The Produce That Stands Out from the Crowd"),
    "h1": ("<em>이상치</em>가 뭐예요?", "What is an <em>Outlier</em>?"),
    "sub": ("이상치를, 비슷한 크기의 작물 무리 속에서 유난히 튀는 하나를 찾아내는 이야기로 풀어봤어요.",
            "Outliers, told as a story about spotting the one piece of produce that stands out from a group of otherwise similar ones."),
    "panels": [
        {"svg": P1, "alt": ("컨베이어 위 비슷한 크기의 사과들 사이에 세 배쯤 큰 사과가 하나 있고, 선별기 조작원이 이를 바라봄", "Among similarly sized apples on the belt, one apple sits about three times bigger, and the operator looks on"),
         "caption": ("비슷한 크기 사과들 사이에, 유난히 큰 작물이 있어요.", "Among similarly sized apples, one stands out — much bigger."),
         "small": ("딱 봐도 나머지와 달라요.", "Even at a glance, it's clearly different from the rest.")},
        {"svg": P2, "alt": ("검수반장은 평균이 끌려 올라간다고, 조작원은 저울 고장일 수도 있다고, 교사는 귀한 품종일 수도 있다고 각각 말함", "The inspector says it drags the average up, the operator says it might mean a broken scale, and the teacher says it might just be a rare variety"),
         "caption": ("무시하면 숫자가 끌려가고, 버리면 신호를 놓쳐요.", "Ignore it and the numbers skew; discard it and a signal might be lost."),
         "small": ("이상치는 실수의 흔적일 수도, 진짜 중요한 신호일 수도 있어요.", "An outlier might be a mistake — or it might be a genuinely important signal.")},
        {"svg": P3, "hero": True, "alt": ("점선 원 안에 비슷한 크기의 사과 다섯 개가 모여 있고, 원 밖 멀리 떨어진 곳에 훨씬 큰 사과 하나가 점선으로 연결됨", "Five similarly sized apples cluster inside a dashed circle, while a much bigger apple sits far outside it, connected by a dashed line"),
         "caption": ("나머지 무리와 통계적으로 확연히 다른 데이터 포인트예요.", "A data point that's statistically, clearly unlike the rest of the group."),
         "small": ("'다르다'는 건 느낌이 아니라, 거리나 흩어진 정도로 재는 거예요.", "'Different' isn't a feeling — it's measured by distance or spread."),
         "tricks": (4, [
             (DIST_I, ("거리로 보기", "Look at distance"), ("무리 중심에서 얼마나 먼지요", "how far from the group's center"), "calm"),
             (ZSCORE_I, ("표준편차로 보기", "Look at standard deviation"), ("평균에서 몇 걸음 벗어났는지요(Z-점수)", "how many steps from average (Z-score)")),
             (IQR_I, ("사분위수로 보기", "Look at quartiles"), ("가운데 뭉치 바깥인지요(IQR)", "outside the middle bulk of the data (IQR)"), "warm"),
             (CHECK_I, ("이유부터 확인하기", "Check the reason first"), ("무조건 버리지 않아요", "not just tossing it out automatically")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦세 가지 찾는 방법|THREE WAYS TO FIND ONE⟧",
                 ("⟦거리 기반 — 군집 중심에서 먼 정도로 판단|distance-based — judged by distance from a cluster's center⟧",
                  "⟦Z-점수 — 평균에서 표준편차 몇 배 떨어졌는지(보통 3 이상)|Z-score — standard deviations from the mean (often past 3)⟧",
                  "⟦IQR(사분위) — 가운데 50% 범위 바깥인지로 판단|IQR — whether it falls outside the middle 50% range⟧",
                  "⟦세 방법 모두, 절대적인 정답보다는 기준선을 정하는 약속이에요|all three are a matter of agreeing on a cutoff, not an absolute truth⟧"), 1.0)),
         "alt": ("거리 기반·Z-점수·IQR 세 가지 이상치 탐지 방법을 적은 표", "A board listing distance-based, Z-score, and IQR as three ways to detect an outlier"),
         "caption": ("찾는 방법은 여러 가지지만, 공통점은 '기준선을 정한다'는 거예요.", "Different methods — but they all come down to agreeing on a cutoff line."),
         "small": ("기준선을 어디에 긋느냐에 따라, 같은 작물도 이상치가 되거나 안 되거나 해요.", "Where that line is drawn decides whether the very same item counts as an outlier or not.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
                 + produce(190, 150, 1.6, "var(--bad)") + label(190, 240, "⟦저울이 고장났던 거였어요 — 지워야 해요|turned out the scale was broken — this should be removed⟧", 11, "var(--bad)")
                 + produce(570, 150, 1.6, "var(--good)") + label(570, 240, "⟦진짜 희귀한 품종이었어요 — 남겨야 해요|it was a genuinely rare variety — this should stay⟧", 11, "var(--good)")
                 + label(380, 280, "⟦같은 '이상치'라도, 오류인지 진짜 신호인지는 사람이 확인해야 해요|the same label 'outlier' can mean an error or a real signal — a person still has to check which⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 알고 보니 저울 고장이라 지워야 하는 이상치. 오른쪽: 진짜 희귀 품종이라 남겨야 하는 이상치", "Left: an outlier that turns out to be a broken scale, meant to be removed. Right: an outlier that's a genuinely rare variety, meant to stay"),
         "caption": ("'이상치'라고 다 지워야 하는 건 아니에요.", "Not every outlier is meant to be thrown away."),
         "small": ("적대적 공격으로 조작된 작물도 통계적으론 이상치처럼 보일 수 있어요.", "An item tampered with by an adversarial attack can also look statistically like an outlier.")},
    ],
    "summary": (("<b>이상치</b> = 거리나 표준편차로 쟀을 때, <b>나머지 무리와 확연히 다른</b> 데이터 포인트.",
                 "<b>An outlier</b> = a data point that, measured by distance or standard deviation, is <b>clearly unlike the rest</b> of the group."),
                ("이상치(Outlier)는 거리 기반(군집 중심과의 거리), Z-점수(평균에서 표준편차 몇 배 떨어졌는지), IQR(사분위 범위 바깥인지) 같은 통계적 기준으로 찾아내는, 나머지 데이터와 뚜렷이 다른 값이에요. 센서 오류나 입력 실수의 흔적일 수도 있고, 드물지만 진짜 중요한 신호(사기 거래, 희귀 질환, 공격 흔적)일 수도 있어서, 발견했다고 무조건 지우기보다 원인부터 확인하는 게 원칙이에요. 군집분석의 DBSCAN이 찾아내는 '노이즈'도 이상치의 한 모습이에요.",
                 "An outlier is a value clearly unlike the rest of the data, found using statistical criteria like distance from a cluster's center, Z-score (standard deviations from the mean), or being outside the IQR (interquartile range). It can be the trace of a sensor error or a data-entry mistake — or it can be a rare but genuinely important signal, like a fraudulent transaction, a rare disease, or the trace of an attack. The rule of thumb is to investigate the cause before deleting it, not the other way around. The 'noise' that DBSCAN clustering sets aside is itself one face of an outlier.")),
    "glossary": [
        ("이상치", "Outlier", ("무리에서 유난히 튀는 작물.", "The piece of produce that stands out from the crowd."), ("거리나 표준편차로 측정해 찾아요.", "Found by measuring distance or standard deviation.")),
        ("Z-점수", "Z-score", ("평균에서 표준편차 몇 배 떨어졌는지 재는 숫자.", "The number of standard deviations a value sits from the mean."), ("보통 절댓값 3을 넘으면 이상치로 봐요.", "An absolute value past 3 is commonly treated as an outlier.")),
        ("IQR(사분위 범위)", "IQR (interquartile range)", ("가운데 50%가 모여 있는 범위.", "The range where the middle 50% of the data sits."), ("이 범위 바깥으로 크게 벗어나면 이상치로 봐요.", "Falling far outside this range marks something as an outlier.")),
        ("노이즈", "Noise", ("DBSCAN이 어느 무리에도 안 넣고 남기는 점.", "What DBSCAN leaves aside, belonging to no cluster."), ('군집분석에서 이상치가 등장하는 모습이에요. → <a href="clustering-ko.html">이름표 없이 비슷한 것끼리 모으기</a>', 'How an outlier shows up inside clustering. → <a href="clustering-en.html">Grouping by Likeness, With No Name Tags</a>')),
        ("이상 탐지", "Anomaly detection", ("이상치를 찾아내는 일 자체를 목적으로 삼는 것.", "Making the hunt for outliers the whole point of the task."), ("사기 탐지, 설비 고장 예측 등에 쓰여요.", "Used for things like fraud detection and predicting equipment failure.")),
        ("데이터 정제", "Data cleaning", ("오류로 확인된 이상치를 골라내는 작업.", "Weeding out outliers confirmed to be errors."), ('씨앗(학습 데이터) 품질관리의 한 과정이에요. → <a href="aidataqual-ko.html">상한 씨앗으로 가르친 선별기</a>', 'One step in managing the quality of the seed — the training data. → <a href="aidataqual-en.html">A Sorter Trained on Rotten Seed</a>')),
        ("적대적 공격", "Adversarial attack", ("통계적으로도 이상치처럼 보일 수 있는 조작.", "A tampering that can also look statistically like an outlier."), ('방어 중 하나가 이상치 탐지예요. → <a href="advattack-ko.html">작물에 몰래 붙인 가짜 점무늬</a>', 'One defense against it is exactly this kind of detection. → <a href="advattack-en.html">The Fake Dot Pattern Snuck Onto the Produce</a>')),
        ("혼동행렬", "Confusion matrix", ("이상치 탐지의 성능도 이 표로 확인해요.", "An outlier detector's own performance is also checked with this table."), ('무엇을 "놓쳤는지" 역시 네 칸으로 나눠 볼 수 있어요. → <a href="confmatrix-ko.html">네 칸으로 나눈 도장 기록부</a>', 'What it missed can be read the same way, in four boxes. → <a href="confmatrix-en.html">The Four-Box Stamp Ledger</a>')),
    ],
}
