from _draw import *
from _world import *

# 1. 조작원 한 명의 판단만 믿기엔 불안해요
P1 = svg(300, sky(300)
         + person(220, 170, s=0.9, face=SWEAT + EYES, **OPERATOR)
         + produce(360, 230, 0.8) + stamp2(430, 190, 0.7, ok=False)
         + label(430, 250, "⟦어? 이거 틀렸는데|oh — that one was wrong⟧", 11, "var(--bad)")
         + label(380, 285, "⟦한 명(모델) 판단만 믿기엔 가끔 불안해요|trusting just one operator's call sometimes feels shaky⟧", 12, "var(--ink)"))

# 2. 세 조작원에게 물어보니 답이 다 달라요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + person(140, 170, s=0.7, face=EYES, **OPERATOR) + bubble(80, 100, 130, 34, "⟦합격!|pass!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 170, s=0.7, face=EYES, **TEACHER) + bubble(320, 100, 150, 34, "⟦불합격!|fail!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(620, 170, s=0.7, face=EYES, **INSPECTOR) + bubble(560, 100, 130, 34, "⟦합격!|pass!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + produce(380, 260, 0.7)
         + label(380, 290, "⟦같은 작물인데 세 사람 말이 다 달라요 — 누굴 믿죠?|same crop, three different calls — who do we trust?⟧", 12, "var(--ink)"))

# 3. 앙상블 = 여러 조작원의 판정을 모아 다수결/평균으로 최종 결정 (hero)
P3 = svg(360, sky(360)
         + person(130, 180, s=0.75, face=SMILE, **OPERATOR) + person(240, 180, s=0.75, face=FROWN, **TEACHER) + person(350, 180, s=0.75, face=SMILE, **INSPECTOR)
         + label(130, 260, "⟦합격|pass⟧", 12, "var(--good)") + label(240, 260, "⟦불합격|fail⟧", 12, "var(--bad)") + label(350, 260, "⟦합격|pass⟧", 12, "var(--good)")
         + gradeboard(460, 70, 240, 150, "⟦최종 결정|FINAL CALL⟧", ("⟦2 대 1 → 합격|2 vs 1 → PASS⟧", "⟦다수결로 정해요|decided by majority⟧"), 0.9)
         + label(380, 30, "⟦앙상블 = 여러 조작원의 판정을 모아 다수결/평균으로 최종 결정하는 것|an ensemble = pooling several operators' calls and deciding by majority vote or average⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦한 명보다 여럿의 평균이 더 안정적일 때가 많아요|the pooled average is often steadier than any single operator⟧", 12, "var(--muted)"))

BAG_I = icon('<rect x="8" y="24" width="18" height="18" fill="var(--accent)"/><rect x="28" y="16" width="18" height="18" fill="var(--accent)"/><rect x="18" y="38" width="18" height="18" fill="var(--accent)"/><rect x="38" y="38" width="18" height="18" fill="var(--accent)"/>')
BOOST_I = icon('<circle cx="18" cy="32" r="8" fill="var(--bad)"/><circle cx="34" cy="32" r="8" fill="var(--accent)"/><circle cx="50" cy="32" r="8" fill="var(--good)"/><path d="M12 16 h12 M28 16 h12 M44 16 h12" stroke="var(--muted)" stroke-width="2"/>')
VOTE_I = icon('<path d="M20 50 V26 M32 50 V18 M44 50 V30" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/><path d="M12 50 h40" stroke="#142033" stroke-width="3"/>')
DIVERSE_I = icon('<circle cx="22" cy="32" r="10" fill="var(--accent)"/><rect x="34" y="22" width="20" height="20" fill="var(--good)"/>')

# 4. 섞는 방식에도 여러 가지가 있어요
P4 = svg(340, sky(340)
         + gradeboard(40, 20, 330, 300, "⟦배깅(Bagging)|BAGGING⟧",
                      ("⟦작물을 다르게 나눠 각자 훈련|split the crops differently, train each separately⟧", "⟦결과를 평균/투표|average or vote the results⟧",
                       "⟦여러 명을 동시에 키워요|grows several operators at once⟧"), 0.92)
         + gradeboard(390, 20, 330, 300, "⟦부스팅(Boosting)|BOOSTING⟧",
                      ("⟦앞사람이 틀린 작물을 다음 사람이 집중|the next trainee focuses on what the last one got wrong⟧", "⟦한 명씩 순서대로 보완|one after another, each fixing the last⟧",
                       "⟦틀린 부분을 점점 줄여가요|gradually shrinks the error⟧"), 0.92))

# 5. 느려지고, 왜 그렇게 결정했는지 설명하기 어려워져요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(140, 150, s=0.7, face=EYES, **OPERATOR) + person(230, 150, s=0.7, face=EYES, **TEACHER) + person(320, 150, s=0.7, face=EYES, **INSPECTOR)
         + label(230, 250, "⟦세 명이 다 봐야 하니 느려져요|three checks mean it's slower⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=EYES, **FARMER)
         + label(570, 262, "⟦왜 합격인지 한마디로 설명하기 어려워요|hard to explain the pass in one simple reason⟧", 11, "var(--ink)")
         + label(380, 300, "⟦앙상블은 더 안정적이지만, 더 느리고 설명은 더 어려워져요|an ensemble is steadier, but slower and harder to explain⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ensemble", "order": 23,
    "title": ("세 조작원의 의견을 모아 결정하는 검사장", "The Station That Pools Three Operators' Calls"),
    "h1": ("<em>앙상블(Ensemble) 기법</em>이/가 뭐예요?", "What is an <em>Ensemble</em> Method?"),
    "sub": ("앙상블 기법을, 조작원 한 명의 판단을 못 믿어 여러 명에게 묻고 다수결로 최종 결정하는 검사장 이야기로 풀어봤어요.",
            "Ensemble methods, told as a story about a station that distrusts any one operator's call and instead pools several opinions into a majority vote."),
    "panels": [
        {"svg": P1, "alt": ("조작원 한 명이 작물을 틀리게 판정해 땀을 흘림", "A single operator misjudges a crop and sweats"),
         "caption": ("조작원 한 명의 판단만 믿기엔 불안해요.", "Trusting just one operator's call feels shaky."),
         "small": ("한 명(모델) 판단만 믿기엔 가끔 불안해요.", "Trusting just one operator's call sometimes feels shaky.")},
        {"svg": P2, "alt": ("같은 작물을 두고 세 조작원이 합격, 불합격, 합격으로 서로 다르게 답함", "Three operators give different calls — pass, fail, pass — on the very same crop"),
         "caption": ("세 조작원에게 물어보니 답이 다 달라요.", "Asking three operators gets three different answers."),
         "small": ("같은 작물인데 세 사람 말이 다 달라요 — 누굴 믿죠?", "Same crop, three different calls — who do we trust?")},
        {"svg": P3, "hero": True, "alt": ("세 조작원의 판정(합격·불합격·합격)을 모아 2대1 다수결로 최종 합격을 결정하는 표", "A board tallies the three operators' calls — pass, fail, pass — into a final 2-to-1 pass decision"),
         "caption": ("앙상블은 여러 조작원의 판정을 모아 다수결/평균으로 최종 결정해요.", "An ensemble pools several operators' calls into a majority vote or average."),
         "small": ("한 명보다 여럿의 평균이 더 안정적일 때가 많아요.", "The pooled average is often steadier than any single operator."),
         "tricks": (4, [
             (BAG_I, ("배깅 — 각자 다르게 훈련", "Bagging — train each differently"), ("작물을 다르게 나눠 맡겨요", "split the crops differently for each"), "calm"),
             (BOOST_I, ("부스팅 — 순서대로 보완", "Boosting — fix in sequence"), ("앞사람이 틀린 걸 다음이 집중", "the next one focuses on the last one's misses")),
             (VOTE_I, ("보팅 — 다수결 결정", "Voting — majority decides"), ("가장 많이 나온 답을 최종으로", "the most common answer wins"), "warm"),
             (DIVERSE_I, ("다양성 — 서로 다르게 섞기", "Diversity — mix different kinds"), ("비슷한 사람만 모으면 소용없어요", "pooling similar operators doesn't help")),
         ])},
        {"svg": P4, "alt": ("배깅(각자 다른 작물로 동시에 훈련해 평균/투표)과 부스팅(앞사람의 실수를 다음이 순서대로 보완)을 나란히 비교", "Bagging (training each separately on different crops, then averaging/voting) is compared with boosting (each in sequence fixing the last one's mistakes)"),
         "caption": ("섞는 방식에도 여러 가지가 있어요.", "There's more than one way to pool them."),
         "small": ("배깅은 동시에 여럿을, 부스팅은 순서대로 하나씩 보완해요.", "Bagging grows several at once; boosting fixes one after another, in sequence.")},
        {"svg": P5, "alt": ("왼쪽: 세 조작원이 다 봐야 해서 판정이 느려짐. 오른쪽: 왜 합격인지 한마디로 설명하기 어려워함", "Left: having three operators check everything slows the process down. Right: it becomes hard to explain the pass in one simple reason"),
         "caption": ("느려지고, 설명하기 어려워져요.", "It gets slower, and harder to explain."),
         "small": ("앙상블은 더 안정적이지만, 더 느리고 설명은 더 어려워져요.", "An ensemble is steadier, but slower and harder to explain.")},
    ],
    "summary": (("<b>앙상블 기법</b> = <b>여러 모델(조작원)의 판정을 모아</b> <b>다수결이나 평균</b>으로 최종 결정하면, <b>한 모델보다 더 안정적</b>이라는 아이디어.",
                 "<b>Ensemble methods</b> pool the calls of <b>several models</b> into a <b>majority vote or average</b>, on the idea that the result is <b>steadier than any single model</b>."),
                ("앙상블은 여러 약한 학습기를 결합해 더 강한 예측을 만드는 기법이에요. 배깅(Bagging)은 부트스트랩 샘플마다 독립적으로 모델을 학습시켜 평균/투표하고(예: 랜덤 포레스트), 부스팅(Boosting)은 이전 모델이 틀린 샘플에 가중치를 더해 순차적으로 모델을 보완해요(예: AdaBoost, Gradient Boosting). 분산을 줄이거나(배깅) 편향을 줄이는(부스팅) 효과가 있지만, 계산 비용이 늘고 개별 모델보다 설명력이 떨어져요.",
                 "Ensembles combine multiple weak learners into a stronger predictor. Bagging trains models independently on bootstrap samples and averages or votes their outputs (e.g. Random Forest); boosting trains models sequentially, each weighting the previous model's misses more heavily (e.g. AdaBoost, Gradient Boosting). Bagging mainly reduces variance and boosting mainly reduces bias, but both cost more compute and are harder to explain than a single model.")),
    "glossary": [
        ("배깅(Bagging)", "Bagging", ("각 조작원에게 작물을 다르게 나눠 맡기는 것.", "Splitting the crops differently for each operator."), ("랜덤 포레스트가 대표적인 배깅 기법이에요.", "Random Forest is the classic example of bagging.")),
        ("부스팅(Boosting)", "Boosting", ("앞사람이 틀린 작물을 다음 사람이 집중해서 보는 것.", "The next operator focusing on what the last one got wrong."), ("AdaBoost·Gradient Boosting이 대표적이에요.", "AdaBoost and Gradient Boosting are classic examples.")),
        ("보팅(Voting)", "Voting", ("가장 많이 나온 답을 최종으로 뽑는 것.", "Picking whichever answer came up most."), ("다수결 방식과 가중 평균 방식이 있어요.", "Can be plain majority or a weighted average.")),
        ("랜덤 포레스트", "Random Forest", ("여러 선별기를 동시에 키우는 대표 배깅 기법.", "The classic bagging method that grows many sorters at once."), ("여러 결정나무를 모아 만들어요.", "Built from pooling many decision trees.")),
        ("편향-분산 트레이드오프", "Bias-Variance Tradeoff", ("안 치우침과 안 흔들림 사이의 줄다리기.", "The tug-of-war between no tilt and no swing."), ("배깅은 분산을, 부스팅은 편향을 주로 줄여요.", "Bagging mainly tames variance; boosting mainly tames bias.")),
        ("교차검증", "Cross Validation", ("조를 나눠 번갈아 시험해 보는 일.", "Splitting into groups and testing in rotation."), ('앙상블 성능도 이걸로 확인해야 믿을 만해요. → <a href="crossval-ko.html">자세히 보기</a>', "An ensemble's performance also needs this to be trusted. → <a href=\"crossval-en.html\">see it in full</a>")),
        ("AI 신뢰성", "AI Trustworthiness", ("정확도만으론 못 받는 품질인증 등급판.", "The certification board accuracy alone can't earn."), ('설명가능성 항목에서 앙상블은 불리할 수 있어요. → <a href="aitrust-ko.html">자세히 보기</a>', 'Ensembles can struggle on the explainability criterion here. → <a href="aitrust-en.html">see it in full</a>')),
        ("강화학습", "Reinforcement Learning", ("정답표 없이 점수로 배우는 신입 조작원.", "The rookie operator who learns by score, not an answer key."), ('앙상블과는 또 다른, 보상 기반 학습 방식이에요. → <a href="rl-ko.html">자세히 보기</a>', 'A different, reward-based style of learning from ensembling. → <a href="rl-en.html">see it in full</a>')),
    ],
}
