from _draw import *
from _world import *


def matrix_cell(x, y, w, h, title, stamp_ok, fill):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="var(--line)" stroke-width="2"/>'
    out += label(x + w / 2, y + 24, title, 12, "var(--ink)", cls="d")
    out += stamp2(x + w / 2, y + h / 2 + 16, 0.65, ok=stamp_ok)
    return out


def conf_grid(x, y):
    """2x2 혼동행렬 그리드. x,y 는 왼쪽 위 모서리."""
    w, h = 180, 110
    out = (label(x + w, y - 30, "⟦선별기의 판정|what the sorter decided⟧", 12, "var(--muted)", cls="d")
           + label(x + w / 2, y - 6, "⟦합격 판정|called PASS⟧", 11, "var(--ink)")
           + label(x + w * 1.5, y - 6, "⟦불합격 판정|called REJECT⟧", 11, "var(--ink)")
           + label(x - 50, y + h, "⟦실제 상태|the real state⟧", 12, "var(--muted)", cls="d")
           + label(x - 20, y + h / 2, "⟦실제 합격|really PASS⟧", 11, "var(--ink)", anchor="end")
           + label(x - 20, y + h * 1.5 + 10, "⟦실제 불합격|really REJECT⟧", 11, "var(--ink)", anchor="end")
           + matrix_cell(x, y, w, h, "⟦TP — 맞게 통과시킴|TP — correctly passed⟧", True, "var(--good-soft)")
           + matrix_cell(x + w, y, w, h, "⟦FN — 놓침(위험!)|FN — missed it (risky!)⟧", False, "var(--bad-soft)")
           + matrix_cell(x, y + h + 10, w, h, "⟦FP — 괜히 불합격(오탐)|FP — wrongly rejected⟧", False, "var(--accent-soft)")
           + matrix_cell(x + w, y + h + 10, w, h, "⟦TN — 맞게 걸러냄|TN — correctly rejected⟧", True, "var(--good-soft)"))
    return out


# 1. 선별기가 "정답률 99%!"라고 자랑해요
P1 = svg(300, sky(300)
         + person(560, 150, s=0.9, face=SMILE, **OPERATOR)
         + bubble(380, 60, 260, 50, "⟦제가 정답률 99%예요!|I've got 99% accuracy!⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + conveyor(80, 230, 420)
         + "".join(produce(120 + i * 36, 198, 0.9, "var(--good)") for i in range(10))
         + produce(480, 198, 0.9, "var(--bad)", bad=True)
         + label(380, 285, "⟦100개 중 상한 건 딱 1개 — 다 합격이라고만 찍어도 99%예요|only 1 of 100 is rotten — stamping everything PASS still scores 99%⟧", 12, "var(--bad)", cls="d"))

# 2. 왜 어려운가: 정답률 하나만 보면, 드문 상한 작물을 매번 놓쳐도 숫자는 좋아 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.8, face=EYES, **OPERATOR)
         + label(160, 260, "⟦다 합격! 다 합격! 다 합격!|all PASS! all PASS! all PASS!⟧", 11, "var(--muted)")
         + produce(400, 150, 1.4, "var(--bad)", bad=True)
         + label(400, 230, "⟦상한 건 매번 놓쳐요|misses the rotten one, every single time⟧", 11, "var(--bad)")
         + person(620, 130, s=0.8, face=FROWN, **INSPECTOR)
         + label(620, 255, "⟦그래도 정답률은 99%예요|and accuracy still reads 99%⟧", 11, "var(--muted)")
         + label(380, 280, "⟦정답률 하나만 보면, 드문 상한 작물을 매번 놓쳐도 숫자는 좋아 보여요|accuracy alone makes a model that always misses the rare case look great⟧", 12, "var(--ink)", cls="d"))

# 3. 혼동행렬 = 실제 상태 × 판정을 네 칸으로 나눈 기록부 (hero)
P3 = svg(420, sky(420)
         + label(380, 25, "⟦혼동행렬 = 실제 상태와 선별기 판정을 네 칸으로 나눠 적는 기록부예요|a confusion matrix records the real state against the sorter's call, in four boxes⟧", 13, "var(--ink)", cls="d")
         + conf_grid(290, 90)
         + label(380, 400, "⟦셀 수만 세면 숫자가 아니라, 어떤 실수인지까지 보여요|not just a count, but exactly which kind of mistake it was⟧", 12, "var(--muted)"))

TP_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
TN_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M22 22 L42 42 M42 22 L22 42" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>')
FP_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M22 22 L42 42 M42 22 L22 42" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
FN_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M20 32 l8 8 l16 -18" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "confmatrix", "order": 4,
    "title": ("네 칸으로 나눈 도장 기록부", "The Four-Box Stamp Ledger"),
    "h1": ("<em>혼동행렬</em>이 뭐예요?", "What is a <em>Confusion Matrix</em>?"),
    "sub": ("혼동행렬을, 선별기의 판정과 실제 상태를 네 칸으로 나눠 적는 기록부 이야기로 풀어봤어요.",
            "The confusion matrix, told as a story about a ledger that splits the sorter's calls against the real state into four boxes."),
    "panels": [
        {"svg": P1, "alt": ("선별기 조작원이 정답률 99%라고 자랑하지만, 100개 중 상한 건 1개뿐이라 다 합격으로 찍어도 99%가 나옴", "The operator boasts 99% accuracy, but with only 1 rotten item in 100, stamping everything PASS would score the same"),
         "caption": ("선별기가 정답률 99%라고 자랑해요.", "The sorter boasts 99% accuracy."),
         "small": ("100개 중 상한 건 딱 1개 — 다 합격이라고만 찍어도 99%예요.", "Only 1 of 100 is rotten — stamping everything PASS still scores 99%.")},
        {"svg": P2, "alt": ("선별기가 전부 합격이라고 외치며 드문 상한 작물을 매번 놓치는데도 검수반장은 정답률이 여전히 99%라고 말함", "The sorter keeps calling everything PASS and always misses the rare rotten one, yet the inspector notes accuracy still reads 99%"),
         "caption": ("정답률 하나만 보면, 드문 실수는 숨어버려요.", "Accuracy alone lets a rare mistake hide."),
         "small": ("매번 놓쳐도 숫자는 좋아 보여요.", "Missing it every time still looks fine on paper.")},
        {"svg": P3, "hero": True, "alt": ("실제 합격·실제 불합격을 가로축, 합격 판정·불합격 판정을 세로축으로 하는 2x2 표에 TP·FN·FP·TN 네 칸이 표시됨", "A 2x2 table with real PASS/REJECT on one axis and called PASS/REJECT on the other, marking out TP, FN, FP, TN"),
         "caption": ("실제 상태와 판정을 네 칸으로 나눠 적는 기록부예요.", "A ledger splitting the real state against the call into four boxes."),
         "small": ("숫자 하나가 아니라, 어떤 종류의 실수인지까지 보여줘요.", "Not just one number — it shows exactly which kind of mistake happened."),
         "tricks": (4, [
             (TP_I, ("TP — 맞게 통과시킴", "TP — correctly passed"), ("진짜 합격을 합격으로 찍어요", "really PASS, called PASS"), "calm"),
             (TN_I, ("TN — 맞게 걸러냄", "TN — correctly rejected"), ("진짜 불합격을 불합격으로 찍어요", "really REJECT, called REJECT"), "calm"),
             (FP_I, ("FP — 괜히 불합격(오탐)", "FP — a false alarm"), ("멀쩡한 걸 불합격으로 틀려요", "flags a fine one as rejected"), "warm"),
             (FN_I, ("FN — 놓침(가장 위험)", "FN — a miss (the risky one)"), ("상한 걸 합격으로 틀려요", "lets a rotten one through"), "warm"),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦네 칸에서 뽑아내는 성능지표|METRICS BUILT FROM THE FOUR BOXES⟧",
                 ("⟦정답률(Accuracy) — 전체 중 맞춘 비율|accuracy — correct out of everything⟧",
                  "⟦정밀도(Precision) — 합격 판정 중 진짜 합격 비율|precision — of what it called PASS, how much really was⟧",
                  "⟦재현율(Recall) — 진짜 합격 중 놓치지 않은 비율|recall — of what's really PASS, how much it caught⟧",
                  "⟦F1 점수 — 정밀도와 재현율의 균형점|F1 score — the balance point between the two⟧"), 1.0)),
         "alt": ("네 칸의 숫자로 계산하는 정답률·정밀도·재현율·F1 점수표", "A board of accuracy, precision, recall, and F1 score, all computed from the four boxes"),
         "caption": ("네 칸의 숫자로 여러 성능지표를 계산해요.", "Several metrics are computed straight from the four boxes."),
         "small": ("어떤 지표를 중시할지는, 어떤 실수가 더 위험한지에 달려 있어요.", "Which metric matters most depends on which kind of mistake costs more.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
                 + produce(190, 130, 1.3, "var(--bad)", bad=True) + stamp2(190, 200, 0.9, ok=True)
                 + label(190, 260, "⟦상한 걸 합격으로(FN) — 손님에게 상한 게 가요|a rotten one gets through (FN) — it reaches a customer⟧", 11, "var(--bad)")
                 + produce(570, 130, 1.3, "var(--good)") + stamp2(570, 200, 0.9, ok=False)
                 + label(570, 260, "⟦멀쩡한 걸 불합격으로(FP) — 농부만 억울해요|a fine one gets rejected (FP) — only the farmer loses out⟧", 11, "var(--ink)")),
         "alt": ("왼쪽: 상한 작물이 합격 도장을 받아 손님에게 감(FN). 오른쪽: 멀쩡한 작물이 불합격 도장을 받음(FP)", "Left: a rotten item gets a pass stamp and reaches a customer (FN). Right: a fine item gets a reject stamp (FP)"),
         "caption": ("FN과 FP 중 뭐가 더 위험한지는 상황에 따라 달라요.", "Which costs more, FN or FP, depends on the situation."),
         "small": ("선별 기준(임계값)을 어디에 둘지는 이 둘의 비용을 저울질해 정해요.", "Where the cutoff is set comes down to weighing these two costs against each other.")},
    ],
    "summary": (("<b>혼동행렬</b> = 선별기의 <b>실제 상태와 판정</b>을 <b>네 칸(TP·TN·FP·FN)</b>으로 나눠 적는 기록부.",
                 "<b>Confusion matrix</b> = a ledger splitting <b>the real state against the sorter's call</b> into <b>four boxes (TP, TN, FP, FN)</b>."),
                ("혼동행렬(Confusion Matrix)은 분류 모델의 예측을 실제 정답과 교차해 TP(참양성)·TN(참음성)·FP(거짓양성)·FN(거짓음성) 네 칸으로 정리한 표예요. 이 네 숫자로 정답률(Accuracy), 정밀도(Precision), 재현율(Recall), F1 점수 같은 성능지표를 계산해요. 클래스 비율이 한쪽으로 치우친 데이터(불균형 데이터)에서는 정답률만으론 모델 성능을 제대로 알 수 없고, 반드시 혼동행렬을 함께 봐야 해요.",
                 "A confusion matrix cross-tabulates a classifier's predictions against the ground truth into four boxes: TP (true positive), TN (true negative), FP (false positive), and FN (false negative). From these four numbers, metrics like accuracy, precision, recall, and the F1 score are derived. When a dataset is imbalanced, accuracy alone can't reveal a model's real performance — the confusion matrix has to be read alongside it.")),
    "glossary": [
        ("혼동행렬", "Confusion matrix", ("실제와 판정을 네 칸으로 나눈 기록부.", "A ledger splitting the real state against the call into four boxes."), ("정답률 하나로는 숨겨지는 실수를 드러내요.", "Reveals the mistakes accuracy alone would hide.")),
        ("정답률", "Accuracy", ("전체 중 맞춘 비율.", "Correct out of everything."), ("불균형 데이터에서는 믿을 수 없어요.", "Unreliable when the classes are imbalanced.")),
        ("정밀도", "Precision", ("합격 판정 중 진짜 합격 비율.", "Of what it called PASS, how much really was."), ("오탐(FP)을 줄이고 싶을 때 중요해요.", "Matters most when false alarms are the costly mistake.")),
        ("재현율", "Recall", ("진짜 합격 중 놓치지 않은 비율.", "Of what's really PASS, how much it caught."), ("미탐(FN)을 줄이고 싶을 때 중요해요.", "Matters most when a miss is the costly mistake.")),
        ("불균형 데이터", "Imbalanced data", ("100개 중 상한 게 1개뿐인 상황.", "A situation where only 1 in 100 is rotten."), ('씨앗 단계의 치우침과 이어지는 문제예요. → <a href="aidataqual-ko.html">상한 씨앗으로 가르친 선별기</a>', 'Connects back to bias at the seed stage. → <a href="aidataqual-en.html">A Sorter Trained on Rotten Seed</a>')),
        ("임계값", "Threshold", ("합격·불합격을 가르는 기준선.", "The cutoff line that splits PASS from REJECT."), ("이 선을 어디에 긋느냐로 FP와 FN의 비율이 바뀌어요.", "Moving this line trades off FP against FN.")),
        ("오탐·미탐", "False alarm vs. miss", ("괜히 불합격(오탐) vs 상한 걸 놓침(미탐).", "A wrongful reject vs. letting a rotten one through."), ('적대적 공격도 결국 이 네 칸의 숫자를 흔들어요. → <a href="advattack-ko.html">작물에 몰래 붙인 가짜 점무늬</a>', 'An adversarial attack ultimately shifts these same four numbers. → <a href="advattack-en.html">The Fake Dot Pattern Snuck Onto the Produce</a>')),
        ("ROC·AUC", "ROC · AUC", ("임계값을 바꿔가며 그린 성능 곡선.", "The performance curve traced by sliding the threshold."), ("혼동행렬 하나가 아니라, 여러 임계값의 혼동행렬을 이어 붙인 그림이에요.", "Not one confusion matrix, but many of them strung together across thresholds.")),
    ],
}
