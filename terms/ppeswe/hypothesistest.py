from _draw import *
from _world import *

# 1. 새 표지가 더 잘 팔릴 거라는 느낌만 있음
P1 = svg(300, sky(300)
         + person(220, 140, s=0.85, face=EYES, **EDITOR)
         + '<rect x="120" y="190" width="60" height="80" rx="3" fill="#D8D2C2"/>' + label(150, 285, "⟦옛 표지|old cover⟧", 11, "var(--muted)")
         + '<rect x="320" y="190" width="60" height="80" rx="3" fill="var(--accent)"/>' + label(350, 285, "⟦새 표지|new cover⟧", 11, "var(--muted)")
         + bubble(400, 90, 220, 40, "⟦이게 더 잘 팔릴 것 같아요!|I just feel this one will sell better!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 30, "⟦편집장은 느낌만 있지, 확신은 없어요|the editor has a hunch — but no real certainty⟧", 13, "var(--ink)"))

# 2. 우연히 하루 반짝 잘 팔린 걸 수도 있음
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SWEAT + EYES, **EDITOR)
         + bubble(100, 70, 260, 44, "⟦어제 새 표지가 더 팔렸는데, 그게 우연일 수도 있잖아요?|yesterday the new cover sold more — but couldn't that be luck?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=EYES, **PROOFER)
         + bubble(440, 70, 240, 40, "⟦느낌만으론 '진짜 차이'인지 '우연'인지 몰라요|a hunch alone can't tell a real difference from chance⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦우연과 진짜 차이를 가를 숫자가 필요해요|we need numbers to separate chance from a real difference⟧", 12, "var(--ink)"))

# 3. 가설검정 = 차이가 없다고 가정하고 따져보는 절차 (hero)
P3 = svg(340, sky(340)
         + person(200, 130, s=0.9, face=EYES, **PROOFER)
         + person(140, 190, s=0.6, face=SMILE, **READER) + person(170, 195, s=0.6, face=EYES, **READER)
         + '<rect x="120" y="150" width="50" height="60" rx="3" fill="#D8D2C2"/>'
         + person(360, 190, s=0.6, face=SMILE, **READER) + person(390, 195, s=0.6, face=SMILE, **READER)
         + '<rect x="340" y="150" width="50" height="60" rx="3" fill="var(--accent)"/>'
         + label(250, 260, "⟦두 그룹에게 각자 다른 표지를 보여줘요|showing each group a different cover⟧", 11, "var(--muted)")
         + ruler(520, 150, 1.0, text="⟦우연일 확률(p값)|chance of this by luck (p-value)⟧")
         + label(380, 30, "⟦가설검정 = '차이 없다'고 가정하고 시작해, 데이터로 진짜 차이인지 따져보는 절차|hypothesis testing = start by assuming 'no difference', then use data to check if it's real⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦기준(유의수준)을 넘으면 '차이 없다'는 가정을 버려요|cross a threshold and you drop the 'no difference' assumption⟧", 12, "var(--muted)"))

# 4. 귀무가설 기각 vs 채택, 1종/2종 오류
P4 = svg(320, sky(320)
         + styleguide(60, 30, 300, 260, "⟦판단표|JUDGMENT TABLE⟧",
                      ("⟦귀무가설 — 차이가 없다|null hypothesis — no difference⟧",
                       "⟦대립가설 — 차이가 있다|alternative — there is a difference⟧",
                       "⟦p값이 작으면 → 귀무가설 기각|small p-value → reject the null⟧",
                       "⟦p값이 크면 → 귀무가설 유지|large p-value → keep the null⟧"), 1.0, hl=2)
         + styleguide(400, 30, 300, 260, "⟦오판 두 가지|TWO WAYS TO BE WRONG⟧",
                      ("⟦1종 오류 — 차이 없는데 있다고|type I — saying different when it isn't⟧",
                       "⟦2종 오류 — 차이 있는데 없다고|type II — saying same when it isn't⟧"), 1.0)
         + label(380, 310, "⟦완벽한 판단은 없어요, 오판 확률을 알고 쓰는 거예요|no judgment is perfect — you use it knowing the odds of being wrong⟧", 12, "var(--ink)"))

# 5. 통계적 유의성 ≠ 실질적 중요성
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **PROOFER) + ruler(140, 220, 0.7)
         + label(190, 270, "⟦p값으로 '차이 있다'는 확인했어요|the p-value confirms there IS a difference⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **EDITOR)
         + label(570, 230, "⟦근데 겨우 책 한 권 더 팔린 거예요|but it's only one extra book sold⟧", 11, "var(--ink)")
         + label(570, 260, "⟦그만큼 들인 돈에 비하면 남는 게 없죠|not worth the money spent to find out⟧", 11, "var(--ink)")
         + label(380, 282, "⟦통계적으로 '차이 있다' ≠ 실제로 중요한 차이예요|statistically significant ≠ a difference that actually matters⟧", 12, "var(--ink)", cls="d"))

NULL_I = icon('<rect x="14" y="26" width="36" height="12" rx="4" fill="var(--muted)"/>')
DATA_I = icon('<rect x="14" y="36" width="8" height="18" fill="var(--accent)"/><rect x="28" y="24" width="8" height="30" fill="var(--accent)"/><rect x="42" y="14" width="8" height="40" fill="var(--accent)"/>')
PVAL_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><text x="32" y="38" text-anchor="middle" font-size="22" font-weight="700" fill="var(--good)">p</text>')
JUDGE_I = icon('<path d="M18 46 h28 M32 12 v34" stroke="var(--line)" stroke-width="4" stroke-linecap="round"/><path d="M18 20 h-6 l6 14 l6 -14z M46 20 h-6 l6 14 l6 -14z" stroke="var(--line)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "hypothesistest", "order": 24,
    "title": ("두 표지 중 뭐가 진짜 더 잘 팔릴까", "Which Cover Really Sells Better"),
    "h1": ("<em>통계적 가설검정</em>이 뭐예요?", "What is <em>Statistical Hypothesis Testing</em>?"),
    "sub": ("통계적 가설검정을, 새 표지가 진짜 더 잘 팔리는지 숫자로 가려내는 출판사 이야기로 풀어봤어요.",
            "Statistical hypothesis testing, told as a story about a publishing house using numbers to tell whether a new cover really sells better."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 새 표지가 더 잘 팔릴 것 같다는 느낌만 가지고 있음", "The editor only has a hunch that the new cover will sell better"),
         "caption": ("편집장은 느낌만 있지, 확신은 없어요.", "The editor has a hunch — but no real certainty."),
         "small": ("느낌만으로 바꾸면 위험해요.", "Acting on a hunch alone is risky.")},
        {"svg": P2, "alt": ("편집장과 교정자가 우연과 진짜 차이를 어떻게 가릴지 고민함", "The editor and proofreader worry about telling chance from a real difference"),
         "caption": ("우연히 하루 반짝 잘 팔린 걸 수도 있어요.", "It could just be a lucky day, not a real difference."),
         "small": ("우연과 진짜 차이를 가를 숫자가 필요해요.", "We need numbers to separate chance from a real difference.")},
        {"svg": P3, "hero": True, "alt": ("독자 두 그룹에게 각각 다른 표지를 보여주고 매수 계산 자로 p값을 확인함", "Two reader groups each see a different cover, and a measuring ruler checks the p-value"),
         "caption": ("가설검정은 '차이 없다'고 가정하고 데이터로 따져봐요.", "Hypothesis testing starts by assuming 'no difference', then checks with data."),
         "small": ("기준을 넘으면 '차이 없다'는 가정을 버려요.", "Cross the threshold, and you drop the 'no difference' assumption."),
         "tricks": (4, [
             (NULL_I, ("귀무가설 세우기", "Set up the null hypothesis"), ("일단 차이 없다고 가정해요", "assume no difference, for now"), "calm"),
             (DATA_I, ("데이터 모으기", "Gather the data"), ("두 그룹을 비교해요", "compare the two groups")),
             (PVAL_I, ("p값 계산하기", "Compute the p-value"), ("우연일 확률을 재요", "measures the chance it's just luck")),
             (JUDGE_I, ("기준과 비교하기", "Compare to the threshold"), ("넘으면 가정을 버려요", "cross it, and the assumption is dropped"), "warm"),
         ])},
        {"svg": P4, "alt": ("귀무가설/대립가설과 1종/2종 오류를 정리한 두 개의 판단표", "Two judgment tables: null/alternative hypothesis, and type I/II error"),
         "caption": ("기준을 넘으면 기각, 아니면 유지해요.", "Cross the threshold and reject the null; otherwise keep it."),
         "small": ("완벽한 판단은 없어요, 오판 확률을 알고 쓰는 거예요.", "No judgment is perfect — you use it knowing the odds of being wrong.")},
        {"svg": P5, "alt": ("왼쪽: p값으로 차이가 있다고 확인함. 오른쪽: 그 차이가 책 한 권 수준으로 작음", "Left: the p-value confirms a difference. Right: that difference is as small as one extra book"),
         "caption": ("통계적으로 '차이 있다'가 '중요한 차이'는 아니에요.", "Statistically significant isn't the same as practically important."),
         "small": ("숫자가 '있다'고 해도, 그게 들인 비용만큼 가치 있는지는 따로 봐야 해요.", "Even when the number says 'yes', you still have to ask if it was worth the cost.")},
    ],
    "summary": (("<b>통계적 가설검정</b>은 '차이가 없다'고 <b>일단 가정</b>하고, 데이터가 그 가정과 얼마나 안 맞는지를 따져 <b>진짜 차이인지</b> 판단하는 절차예요.",
                 "<b>Statistical hypothesis testing</b> starts by <b>assuming there's no difference</b>, then checks how badly the data clashes with that assumption to judge whether <b>a real difference</b> exists."),
                ("가설검정은 귀무가설(차이/효과가 없다)과 대립가설(차이/효과가 있다)을 세우고, 표본 데이터로부터 p-value(귀무가설이 맞다고 할 때 지금 결과 이상이 우연히 나올 확률)를 계산해 유의수준(보통 0.05)과 비교함으로써 귀무가설을 기각할지 결정해요. 실제보다 차이가 있다고 잘못 판단하면 1종 오류, 차이가 없다고 잘못 판단하면 2종 오류라고 해요.",
                 "Hypothesis testing sets up a null hypothesis (no effect/difference) and an alternative (there is one), computes a p-value from sample data — the probability of seeing a result this extreme by chance if the null were true — and compares it to a significance level (often 0.05) to decide whether to reject the null. Wrongly rejecting a true null is a Type I error; wrongly failing to reject a false null is a Type II error.")),
    "glossary": [
        ("귀무가설", "Null Hypothesis", ("'차이가 없다'는 출발 가정.", "The starting assumption of 'no difference'."), ("일단 이걸 가정하고 시작해요.", "You begin by assuming this, for now.")),
        ("대립가설", "Alternative Hypothesis", ("'차이가 있다'는 주장.", "The claim that there IS a difference."), ("귀무가설이 기각되면 이걸 받아들여요.", "Accepted when the null gets rejected.")),
        ("p값", "p-value", ("우연일 확률.", "The chance it's just luck."), ("작을수록 우연이 아니라는 뜻이에요.", "The smaller it is, the less likely this is chance.")),
        ("유의수준", "Significance Level", ("판단의 기준선(보통 0.05).", "The judgment threshold (often 0.05)."), ("p값이 이보다 작으면 기각해요.", "Reject the null when the p-value falls below it.")),
        ("1종 오류", "Type I Error", ("차이 없는데 있다고 오판.", "Wrongly saying there IS a difference."), ("성급한 판단의 위험이에요.", "The risk of jumping to conclusions.")),
        ("2종 오류", "Type II Error", ("차이 있는데 없다고 오판.", "Wrongly saying there is NO difference."), ("진짜 차이를 놓치는 위험이에요.", "The risk of missing a real difference.")),
        ("SW 성능테스트", "Performance Testing", ("숫자로 한계를 재는 또 다른 방법.", "Another way of measuring limits with numbers."), ('목적은 다르지만 숫자로 판단하는 건 같아요. → <a href="perftest-ko.html">미리 몰려보는 가짜 독자들</a>', "A different goal, same reliance on numbers. → <a href=\"perftest-en.html\">the pretend readers who rush in early</a>")),
        ("메타모픽 테스트", "Metamorphic Testing", ("정답을 몰라도 관계로 확인하는 법.", "Checking via relationships, even without a known answer."), ('정답이 아예 없을 때 쓰는 다른 접근이에요. → <a href="metamorphictest-ko.html">정답 없이도 관계로 확인하기</a>', 'A different approach for when there is no known answer at all. → <a href="metamorphictest-en.html">checking by relationship, with no answer key</a>')),
    ],
}
