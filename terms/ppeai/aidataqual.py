from _draw import *
from _world import *

# 1. 농부가 씨앗 바구니를 들고 옴 — 라벨이 틀리고, 상한 것도 섞이고, 중복도 있어요
P1 = svg(320, sky(320)
         + label(380, 26, "⟦이 농산물 품질검사장이 곧 머신러닝 세계예요|this produce inspection station IS the machine-learning world⟧", 13, "var(--ink)", cls="d")
         + person(110, 170, s=0.8, face=EYES, **FARMER)
         + conveyor(220, 230, 460)
         + produce(260, 198, 1.0, "var(--good)") + label(260, 170, "⟦사과라고 적힘|labeled 'apple'⟧", 10, "var(--muted)")
         + produce(360, 198, 1.0, "var(--bad)", bad=True) + label(360, 170, "⟦상함|rotten⟧", 10, "var(--bad)")
         + produce(460, 198, 1.0, "var(--good)") + produce(500, 198, 1.0, "var(--good)")
         + label(480, 170, "⟦똑같은 사진 두 장|the same photo, twice⟧", 10, "var(--muted)")
         + produce(600, 198, 1.0, "var(--muted)") + label(600, 170, "⟦이름표 없음|no label at all⟧", 10, "var(--muted)")
         + label(380, 290, "⟦라벨이 틀리고, 상한 것도 섞이고, 같은 게 여러 번 들어있어요|wrong labels, rotten pieces mixed in, the same item showing up twice⟧", 13, "var(--bad)", cls="d"))

# 2. 왜 어려운가: 교사가 이 재료 그대로 선별기를 가르치면, 실수까지 "정답"으로 배워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.85, face=EYES, **TEACHER)
         + bubble(260, 60, 230, 50, "⟦이 상한 것도 사과예요, 외우세요|this rotten one is an apple too, memorize it⟧", 11, "var(--panel)", "var(--line)", "left")
         + person(560, 150, s=0.75, face=SWEAT + EYES, **OPERATOR)
         + label(560, 250, "⟦네, 외울게요…|okay, memorizing…⟧", 11, "var(--muted)")
         + label(380, 285, "⟦교사가 틀린 걸 정답이라 가르치면, 선별기는 의심 없이 그대로 배워요|if the teacher calls a mistake the right answer, the sorter learns it without question⟧", 12, "var(--ink)", cls="d"))

# 3. 데이터 품질관리 = 가르치기 전에 씨앗(재료) 자체부터 검사하는 일 (hero)
P3 = svg(340, sky(340)
         + person(130, 150, s=0.8, face=EYES, **INSPECTOR)
         + gradeboard(230, 60, 300, 90, "⟦씨앗 검사표|SEED CHECKLIST⟧", ("⟦라벨 맞나 · 상했나 · 중복인가|right label? rotten? duplicate?⟧",), 1.0)
         + conveyor(230, 230, 300)
         + produce(300, 198, 1.0, "var(--good)") + stamp2(300, 160, 0.5, ok=True)
         + produce(420, 198, 1.0, "var(--bad)", bad=True) + stamp2(420, 160, 0.5, ok=False)
         + person(620, 150, s=0.8, face=SMILE, **TEACHER)
         + label(380, 30, "⟦데이터 품질관리 = 가르치기 전에 씨앗 자체부터 검사하는 일이에요|data quality management checks the seed itself before any teaching begins⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦좋은 씨앗만 걸러야, 선별기도 제대로 배워요|only good seed gets through — only then does the sorter learn correctly⟧", 12, "var(--muted)"))

LABEL_I = icon('<rect x="10" y="20" width="44" height="30" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 32 h20 M18 40 h14" stroke="#142033" stroke-width="2.5"/><path d="M44 10 l10 10 l-10 10" stroke="var(--good)" stroke-width="4" fill="none"/>')
DUPE_I = icon('<rect x="10" y="12" width="30" height="34" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="24" y="20" width="30" height="34" rx="3" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/>')
BIAS_I = icon('<circle cx="20" cy="40" r="9" fill="var(--accent)"/><circle cx="34" cy="40" r="9" fill="var(--accent)"/><circle cx="48" cy="40" r="9" fill="var(--accent)"/><circle cx="34" cy="18" r="9" fill="var(--bad)"/>')
FRESH_I = icon('<path d="M32 10 A22 22 0 1 1 11 32" stroke="var(--good)" stroke-width="5" fill="none"/><path d="M32 10 v12 h-10" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "aidataqual", "order": 1,
    "title": ("상한 씨앗으로 가르친 선별기", "A Sorter Trained on Rotten Seed"),
    "h1": ("<em>AI 학습용 데이터 품질관리</em>가 뭐예요?", "What is <em>Training Data Quality Management</em>?"),
    "sub": ("AI 학습용 데이터 품질관리를, 선별기를 가르치기 전에 씨앗(훈련 데이터) 상태부터 점검하는 이야기로 풀어봤어요.",
            "Training data quality management, told as a story about checking the seed — the training data — before it ever teaches the sorter anything."),
    "panels": [
        {"svg": P1, "alt": ("농부가 컨베이어 벨트에 작물을 올리는데, 라벨이 틀리거나 상했거나 중복이거나 이름표 없는 것이 섞여 있음", "A farmer loads produce onto the belt — some mislabeled, some rotten, some duplicated, some with no label at all"),
         "caption": ("농부가 씨앗 바구니를 들고 왔는데, 상태가 엉망이에요.", "The farmer brings a basket of seed — and it's a mess."),
         "small": ("라벨이 틀리고, 상한 것도 섞이고, 같은 게 여러 번 들어있어요.", "Wrong labels, rotten pieces, the same item showing up twice.")},
        {"svg": P2, "alt": ("훈련 교사가 상한 작물도 사과라고 가르치자 선별기 조작원이 땀을 흘리며 그대로 외움", "The teacher tells the operator that even the rotten one is an apple, and the operator sweats, memorizing it as-is"),
         "caption": ("교사가 이 재료 그대로 가르치면, 실수까지 정답으로 배워요.", "If the teacher teaches straight from this batch, mistakes get memorized as fact."),
         "small": ("선별기는 의심 없이 그대로 배워요.", "The sorter learns it without question.")},
        {"svg": P3, "hero": True, "alt": ("검수반장이 씨앗 검사표로 작물을 하나씩 확인해 합격·불합격 도장을 찍은 뒤에야 교사에게 넘김", "The inspector checks each item against a seed checklist, stamping pass or fail, before it ever reaches the teacher"),
         "caption": ("데이터 품질관리 = 가르치기 전에 씨앗 자체부터 검사하는 일이에요.", "Data quality management checks the seed itself before any teaching begins."),
         "small": ("좋은 씨앗만 걸러야, 선별기도 제대로 배워요.", "Only good seed gets through — only then does the sorter learn correctly."),
         "tricks": (4, [
             (LABEL_I, ("라벨 맞는지 확인하기", "Verify the label"), ("이름표가 진짜 맞는지요", "checking the tag is actually true"), "calm"),
             (DUPE_I, ("중복·결측 걸러내기", "Remove duplicates & gaps"), ("같은 것·빈 것을 치워요", "clearing out repeats and empties")),
             (BIAS_I, ("치우침 점검하기", "Check for bias"), ("한 종류만 쌓이지 않게요", "making sure one kind doesn't pile up"), "warm"),
             (FRESH_I, ("최신 상태 유지하기", "Keep it current"), ("오래된 재료도 갈아줘요", "refreshing stale batches too")),
         ])},
        {"svg": svg(280, sky(280) + gradeboard(60, 20, 640, 240, "⟦데이터 품질 네 기준|FOUR QUALITY STANDARDS⟧",
                 ("⟦정확성 — 라벨이 맞나|accuracy — is the label right?⟧",
                  "⟦완전성 — 빠진 값은 없나|completeness — any missing values?⟧",
                  "⟦일관성 — 같은 기준으로 적혔나|consistency — recorded the same way?⟧",
                  "⟦대표성 — 한쪽에 치우치지 않았나|representativeness — not skewed to one kind?⟧"), 1.0)),
         "alt": ("정확성·완전성·일관성·대표성 네 기준이 적힌 품질표", "A quality board listing accuracy, completeness, consistency, and representativeness"),
         "caption": ("데이터 품질은 이 네 가지로 가늠해요.", "Data quality is judged by these four standards."),
         "small": ("하나라도 무너지면, 선별기의 '정답률'은 숫자일 뿐 믿을 수 없어요.", "If even one fails, the sorter's accuracy number stops being trustworthy.")},
        {"svg": svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
                 + person(190, 130, s=0.8, face=SMILE, **INSPECTOR) + label(190, 260, "⟦씨앗은 깨끗해졌어요|the seed is clean now⟧", 11, "var(--ink)")
                 + person(570, 130, s=0.75, face=EYES, **OPERATOR) + label(570, 260, "⟦그래도 제가 잘 배우는 건 별개예요|but whether I actually learn well is a separate question⟧", 11, "var(--ink)")
                 + label(380, 300, "⟦좋은 재료는 필요조건이지, 좋은 선별기를 보장하진 않아요 — 성적은 혼동행렬로 따로 재야 해요|good material is necessary, not sufficient — the sorter's actual score still needs its own measuring⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 검수반장이 씨앗이 깨끗해졌다고 말함. 오른쪽: 조작원은 그래도 자기가 잘 배우는 건 별개라고 말함", "Left: the inspector says the seed is clean now. Right: the operator notes learning well is still a separate question"),
         "caption": ("데이터 품질관리가 모든 걸 해결하진 않아요.", "Data quality management doesn't solve everything."),
         "small": ("좋은 재료는 필요조건일 뿐, 선별기 성적은 따로 재야 해요.", "Good material is necessary — but the sorter's score still needs its own measuring.")},
    ],
    "summary": (("<b>AI 학습용 데이터 품질관리</b> = 선별기를 <b>가르치기 전에</b>, 씨앗(훈련 데이터)의 <b>라벨·중복·편향</b>부터 검사하는 일.",
                 "<b>Training data quality management</b> = checking the seed's <b>labels, duplicates, and bias</b> <b>before</b> it ever teaches the sorter anything."),
                ("AI 학습용 데이터 품질관리는 모델을 학습시키기 전, 훈련 데이터의 정확성·완전성·일관성·대표성을 점검하고 개선하는 활동이에요. 라벨 오류, 결측치, 중복, 데이터 편향을 방치하면 '성능 좋은 모델'이 아니라 '엉망을 그대로 외운 모델'이 나와요. Garbage In, Garbage Out — 모델 구조를 아무리 잘 짜도 재료가 나쁘면 결과는 나빠요.",
                 "Training data quality management is the practice of checking and improving a training set's accuracy, completeness, consistency, and representativeness before a model ever learns from it. Left unchecked, label errors, missing values, duplicates, and bias don't produce a high-performing model — they produce one that has faithfully memorized a mess. Garbage in, garbage out: no amount of clever model architecture fixes bad material.")),
    "glossary": [
        ("데이터 품질관리", "Data quality management", ("씨앗부터 검사하는 일.", "Checking the seed itself."), ("가르치기 전에 먼저 봐요.", "Done before any teaching starts.")),
        ("라벨링", "Labeling", ("농작물에 이름표 붙이기.", "Tagging produce with a name."), ("틀린 이름표가 가장 흔한 사고예요.", "A wrong tag is the most common accident.")),
        ("데이터 편향", "Data bias", ("한 종류만 잔뜩 담긴 바구니.", "A basket stuffed with only one kind."), ("선별기가 편식하게 만들어요.", "It teaches the sorter to play favorites.")),
        ("결측치", "Missing value", ("라벨이 아예 없는 작물.", "Produce with no label at all."), ("비워두지 말고 채우거나 빼야 해요.", "It has to be filled in or dropped — never left blank.")),
        ("중복 데이터", "Duplicate data", ("같은 작물 사진이 여러 장.", "The same photo of produce, several times over."), ("성적을 부풀려 보이게 해요.", "It can make the final score look better than it is.")),
        ("데이터 증강", "Data augmentation", ("작물을 돌리고 뒤집어 사진을 늘리는 것.", "Rotating and flipping produce to make more photos."), ("적은 재료로 더 다양하게 가르쳐요.", "More variety taught from less raw material.")),
        ("학습/검증/테스트 분할", "Train/val/test split", ("가르칠 바구니, 연습 바구니, 시험 바구니를 나누는 것.", "Splitting into a teaching basket, a practice basket, and an exam basket."), ("섞으면 시험이 쉬워져 거짓 성적이 나와요.", "Mixing them makes the exam too easy — the score becomes a lie.")),
        ("그라운드 트루스", "Ground truth", ("검수반장이 확인해 둔 진짜 정답.", "The real answer the inspector has already confirmed."), ("모든 품질관리의 기준이 되는 원본이에요.", "The original that every quality check is measured against.")),
    ],
}
