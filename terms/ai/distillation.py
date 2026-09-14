from _draw import *
from _world import *

ARROW = '<path d="M{0} {2} L{1} {2}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M{3} {4} L{1} {2} L{3} {5}" stroke="var(--muted)" stroke-width="3" fill="none"/>'


def arrow(x0, x1, y):
    return ARROW.format(x0, x1, y, x1 - 10, y - 8, y + 8)


# 1. 큰 앵무새는 잘하지만 느리고 비싸요
P1 = svg(300, sky(300) + perch(200, 200, 150) + parrot(200, 160, 1.4, color=PARROT_BIG, talk=True)
         + bubble_parrot(80, 20, 240, 40, "⟦…잠깐만요… 답은… 파리예요|…one moment… the answer is… Paris⟧", 11)
         + "".join(bean(120 + i * 22, 256 - (i % 2) * 5, 0.7) for i in range(8))
         + person(520, 120, s=0.9, face=FROWN, **GUEST) + bubble(420, 30, 280, 40, "⟦잘하는데… 느리고 비싸서 매일은 부담|great… but too slow and pricey for every day⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(580, 262, "⟦매일 물어볼 손님|a guest who asks every day⟧", 11, "var(--muted)")
         + label(380, 288, "⟦큰 앵무새는 잘해요 — 그런데 느리고, 답할 때마다 콩이 잔뜩|the big parrot is great — but slow, and every answer costs a heap of beans⟧", 12, "var(--ink)"))

# 2. 작은 앵무새를 책 산더미로 다시 키우기엔 학교가 너무 비싸요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + books(120, 230, 6, 1.2) + label(120, 262, "⟦책 산더미를 처음부터|the whole mountain, from scratch⟧", 11, "var(--muted)")
         + arrow(190, 250, 170)
         + parrot(300, 180, 0.7, mood="sweat") + label(300, 262, "⟦작은 앵무새|small parrot⟧", 11, "var(--muted)")
         + note(380, 50, 200, 120, "⟦학교 청구서|SCHOOL BILL⟧", ("⟦콩 백만 자루|a million sacks of beans⟧", "⟦몇 달|several months⟧", "⟦조련사 백 명|a hundred trainers⟧"), 0.95)
         + person(620, 90, s=0.9, face=FROWN, extra=SWEAT, **TRAINER) + label(655, 232, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + label(380, 282, "⟦작은 앵무새를 책으로 다시 키우는 건 너무 비싸요 — 학교는 한 번이 한계|raising a small parrot on books again costs too much — school is a once-only thing⟧", 12, "var(--bad)"))

# 3. 증류 = 큰 앵무새의 답을 잔뜩 모아 작은 앵무새에게 따라 하게 가르치기 (hero)
NOTES = "".join(note(300 + i * 8, 150 - i * 8, 120, 60, "⟦답 쪽지|ANSWER⟧", ("⟦파리예요|it is Paris⟧",), 0.9) for i in range(4))
P3 = svg(360, sky(360)
         + perch(140, 240, 150) + parrot(140, 200, 1.4, color=PARROT_BIG, talk=True)
         + bubble_parrot(40, 40, 200, 40, "⟦프랑스 수도는 파리예요|the capital of France is Paris⟧", 11)
         + label(140, 292, "⟦선생 앵무새|teacher parrot⟧", 12, "var(--ink)", cls="d")
         + arrow(210, 290, 150)
         + NOTES + label(370, 220, "⟦답 쪽지 수천 장|thousands of answer notes⟧", 11, "var(--muted)")
         + arrow(450, 530, 150)
         + person(470, 190, s=0.8, face=SMILE, **TRAINER) + label(498, 292, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + perch(620, 240, 120) + parrot(620, 200, 0.8, talk=True)
         + bubble_parrot(540, 60, 180, 40, "⟦파리예요!|it is Paris!⟧", 12)
         + label(620, 292, "⟦학생 앵무새|student parrot⟧", 12, "var(--ink)", cls="d")
         + label(380, 340, "⟦증류 = 큰 앵무새가 답한 걸 잔뜩 모아, 작은 앵무새에게 따라 하게 가르치는 것|distillation: collect heaps of the big parrot\'s answers, and teach the small parrot to copy them⟧", 13, "var(--ink)", cls="d"))

# 4. 그림: 큰 앵무새 → 답 쪽지 → 작은 앵무새 특훈 → 비슷하게 답
STACK = "".join(note(200 + i * 8, 95 + i * 8, 110, 70, "⟦답 쪽지|ANSWER⟧", ("⟦Q 프랑스 수도?|Q capital of France?⟧", "⟦A 파리|A Paris⟧"), 0.9) for i in range(3))
P4 = svg(320, sky(320)
         + parrot(90, 150, 1.1, color=PARROT_BIG, talk=True) + label(90, 250, "⟦1 큰 앵무새가 답해요|1 the big parrot answers⟧", 11, "var(--ink)")
         + arrow(140, 190, 150)
         + STACK + label(270, 250, "⟦2 쪽지 ×3,000|2 notes ×3,000⟧", 11, "var(--ink)")
         + arrow(335, 375, 150)
         + parrot(415, 165, 0.8) + person(445, 105, s=0.7, face=SMILE, **TRAINER)
         + note(500, 130, 74, 50, "⟦특훈|DRILL⟧", ("⟦따라 해|copy it⟧",), 0.9)
         + label(480, 250, "⟦3 작은 앵무새 특훈|3 drill the small parrot⟧", 11, "var(--ink)")
         + arrow(585, 620, 150)
         + parrot(670, 165, 0.8, talk=True) + bubble_parrot(600, 60, 150, 40, "⟦파리예요!|it is Paris!⟧", 12)
         + label(670, 250, "⟦4 비슷하게 답해요|4 answers alike⟧", 11, "var(--ink)")
         + label(380, 300, "⟦3번 특훈은 파인튜닝이에요 — 책 산더미가 아니라 쪽지 몇천 장으로|step 3 is fine-tuning — a few thousand notes, not a mountain of books⟧", 11, "var(--muted)"))

# 5. 학생은 선생을 넘지 못하고, 선생 실수도 배워요 + 약관
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(80, 150, 1.2, color=PARROT_BIG) + label(80, 230, "⟦선생|teacher⟧", 11, "var(--muted)")
         + parrot(200, 160, 0.8) + label(200, 230, "⟦학생|student⟧", 11, "var(--muted)")
         + note(260, 60, 100, 80, "⟦시험|TEST⟧", ("⟦선생 95점|teacher 95⟧", "⟦학생 92점|student 92⟧"), 0.95)
         + label(190, 262, "⟦학생은 선생만큼은 되지만, 넘기는 어려워요|the student gets close, but rarely passes the teacher⟧", 11, "var(--ink)")
         + parrot(470, 140, 1.1, color=PARROT_BAD, talk=True) + bubble_parrot(400, 40, 180, 40, "⟦1987년 책이에요|a book from 1987⟧", 11, bad=True)
         + parrot(650, 160, 0.8, color=PARROT_BAD, talk=True) + bubble_parrot(580, 70, 150, 40, "⟦1987년!|1987!⟧", 12, bad=True)
         + label(570, 230, "⟦선생 실수도 그대로 배워요|it copies the teacher\'s mistakes too⟧", 11, "var(--ink)")
         + label(570, 262, "⟦남의 앵무새 답으로 가르치기 = 약관부터 확인|teaching from someone else\'s parrot = check the terms first⟧", 10, "var(--bad)")
         + label(380, 300, "⟦작지만 우리 일엔 충분한 앵무새 — 그게 증류의 목표예요|small, but good enough for our job — that is the goal of distillation⟧", 12, "var(--ink)", cls="d"))

NOTES_I = icon('<rect x="18" y="16" width="34" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="10" width="34" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h18 M20 30 h18 M20 38 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
FUNNEL_I = icon('<path d="M10 12 h44 l-17 20 v18 l-10 6 v-24z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3" stroke-linejoin="round"/><circle cx="20" cy="8" r="3" fill="var(--muted)"/><circle cx="32" cy="6" r="3" fill="var(--accent)"/><circle cx="44" cy="8" r="3" fill="var(--muted)"/>')
SMALL_I = icon(f'<ellipse cx="30" cy="38" rx="11" ry="15" fill="{PARROT}"/><circle cx="30" cy="20" r="9" fill="{PARROT}"/><path d="M37 17 l10 3 l-10 4z" fill="#E9B44C"/><circle cx="32" cy="18" r="2" fill="#FFF"/><path d="M44 44 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
EXAM_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 30 h20 M22 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><text x="44" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">92</text>')

PAGE = {
    "slug": "distillation", "order": 27,
    "title": ("작은 앵무새에게 흉내 가르치기", "Teaching the Small Parrot to Copy"),
    "h1": ("<em>증류</em>가 뭐예요?", "What is <em>Distillation</em>?"),
    "sub": ("지식 증류(knowledge distillation)를, 큰 앵무새의 답을 잔뜩 모아 작은 앵무새에게 따라 하게 가르치는 이야기로 풀어봤어요.",
            "Knowledge distillation, told as a story about collecting a big parrot\'s answers and teaching a small parrot to copy them."),
    "panels": [
        {"svg": P1, "alt": ("큰 앵무새가 천천히 '답은 파리예요'라고 말하고 발밑엔 콩이 잔뜩. 손님은 '잘하는데 느리고 비싸서 매일은 부담'이라고 함", "A big parrot slowly says the answer is Paris, with a heap of beans below; a guest says it is great but too slow and pricey for every day"),
         "caption": ("큰 앵무새는 잘해요. 그런데 느리고, 한 번 답할 때마다 콩이 잔뜩 들어요.", "The big parrot is great. But it is slow, and every answer costs a heap of beans."),
         "small": ("매일 수천 번 물어봐야 하는 일이면 부담이 커요. 작은 앵무새면 좋겠는데, 작은 앵무새는 그만큼 못해요.", "For a job that asks thousands of times a day, that adds up. A small parrot would be nice — but a small one is not as good.")},
        {"svg": P2, "alt": ("책 산더미에서 작은 앵무새로 화살표, 옆에 '학교 청구서: 콩 백만 자루, 몇 달, 조련사 백 명' 쪽지와 땀 흘리는 조련사", "An arrow from a mountain of books to a small parrot; a school bill note reads a million sacks of beans, several months, a hundred trainers; a sweating trainer"),
         "caption": ("작은 앵무새를 책 산더미로 처음부터 다시 키우기엔 학교가 너무 비싸요.", "Raising a small parrot on the whole mountain of books again costs far too much."),
         "small": ('책 읽는 학교(<a href="pretraining-ko.html">사전 학습</a>)는 콩 백만 자루짜리예요. 우리 일 하나 때문에 다시 열 수는 없어요.',
                   'The reading school (<a href="pretraining-en.html">pretraining</a>) costs a million sacks of beans. You cannot reopen it for one job.')},
        {"svg": P3, "hero": True, "alt": ("선생 앵무새(큰)가 '프랑스 수도는 파리예요'라고 답하고, 답 쪽지 수천 장이 조련사를 거쳐 학생 앵무새(작은)에게 가며, 학생이 '파리예요!'라고 따라 함", "A big teacher parrot answers that the capital of France is Paris; thousands of answer notes go via a trainer to a small student parrot, which repeats it is Paris"),
         "caption": ("증류는 큰 앵무새가 답한 걸 잔뜩 모아, 작은 앵무새에게 따라 하게 가르치는 거예요.", "Distillation collects heaps of the big parrot\'s answers and teaches the small parrot to copy them."),
         "small": ("큰 앵무새가 선생, 작은 앵무새가 학생이에요. 책 대신 선생의 답 쪽지로 배우니까 학교보다 훨씬 싸고 빨라요.", "The big parrot is the teacher, the small one the student. It learns from the teacher\'s answer notes instead of books — far cheaper and faster than school."),
         "tricks": (4, [
             (NOTES_I, ("큰 앵무새 답을 문제집으로", "Teacher answers as a workbook"), ("질문과 답을 수천 장 모아요", "collect thousands of Q and A"), "calm"),
             (FUNNEL_I, ("우리 일에 맞는 문제만", "Only our kind of problems"), ("아무 질문이 아니라 우리 질문", "our questions, not any questions")),
             (SMALL_I, ("작은 앵무새는 그 일만 잘해요", "The small one does that job well"), ("다른 일은 여전히 모자라요", "still short on other jobs"), "warm"),
             (EXAM_I, ("시험으로 확인", "Check with a test"), ("선생 점수와 비교해요", "compare with the teacher\'s score"), "warm"),
         ])},
        {"svg": P4, "alt": ("네 단계: 큰 앵무새가 답해요 → 답 쪽지 ×3,000 → 조련사가 작은 앵무새를 특훈 → 작은 앵무새가 '파리예요!'라고 비슷하게 답함", "Four steps: the big parrot answers, notes ×3,000, a trainer drills the small parrot, the small parrot answers alike with it is Paris"),
         "caption": ("큰 앵무새의 답 쪽지 수천 장으로 작은 앵무새를 특훈시켜요.", "Thousands of the big parrot\'s answer notes drill the small parrot."),
         "small": ('3번의 특훈이 <a href="finetune-ko.html">파인튜닝</a>이에요. 선생의 답 쪽지는 사람이 쓴 게 아니라서 <a href="synthetic-ko.html">합성 데이터</a>라고 불러요.',
                   'Step 3 is <a href="finetune-en.html">fine-tuning</a>. Because the teacher\'s notes were not written by people, they are called <a href="synthetic-en.html">synthetic data</a>.')},
        {"svg": P5, "alt": ("왼쪽 초록: 선생 95점, 학생 92점 시험지. 오른쪽 빨강: 빨간 선생 앵무새가 '1987년 책이에요'라고 하자 학생도 '1987년!'이라고 따라 함", "Left, green: a test sheet with teacher 95 and student 92. Right, red: a red teacher parrot says a book from 1987, and the student repeats 1987!"),
         "caption": ("학생은 선생을 넘기 어렵고, 선생의 실수도 그대로 배워요.", "The student rarely passes the teacher, and copies the teacher\'s mistakes too."),
         "small": ('그래서 <a href="evaluation-ko.html">시험</a>으로 꼭 확인해요. 남의 앵무새 답으로 가르치는 건 약관 문제가 있어요. 작은 앵무새로 충분한 일만 보내는 건 <a href="routing-ko.html">라우팅</a>, 다른 방법으로 작게 만드는 건 <a href="quantization-ko.html">양자화</a>예요.',
                   'So always confirm with a <a href="evaluation-en.html">test</a>. Teaching from someone else\'s parrot raises terms-of-service issues. Sending only the easy jobs to the small parrot is <a href="routing-en.html">routing</a>; shrinking it another way is <a href="quantization-en.html">quantization</a>.')},
    ],
    "summary": (("<b>증류</b> = 큰 앵무새의 <b>답을 잔뜩 모아</b> 작은 앵무새에게 <b>따라 하게 가르치기</b>. 학교보다 훨씬 싸게, 우리 일엔 충분한 작은 앵무새를 얻어요. 학생은 선생을 넘기 어렵고 <b>실수도 배워요</b>.",
                 "<b>Distillation</b> = <b>collect heaps of a big parrot\'s answers</b> and <b>teach a small parrot to copy them</b>. Far cheaper than school, and good enough for our job. The student rarely passes the teacher and <b>copies its mistakes</b>."),
                ("Knowledge distillation. 큰 교사 모델(teacher)의 출력으로 작은 학생 모델(student)을 학습시켜, 비용·지연을 줄이면서 특정 작업 성능을 유지하는 기법이에요. 교사 출력은 합성 데이터이고, 학생 학습은 파인튜닝(SFT)이에요. 타사 모델 출력으로 학습하는 건 약관 위반일 수 있어요.",
                 "Training a small student model on the outputs of a large teacher model, keeping task performance while cutting cost and latency. The teacher outputs are synthetic data, and the student training is fine-tuning (SFT). Training on another vendor\'s model outputs may violate its terms of service.")),
    "glossary": [
        ("지식 증류", "Knowledge distillation", ("작은 앵무새에게 흉내 가르치기.", "Teaching the small parrot to copy."), ("큰 앵무새 답으로 작은 앵무새를 가르쳐요.", "The big parrot\'s answers train the small one.")),
        ("교사 · 학생 모델", "Teacher · student model", ("선생 앵무새와 학생 앵무새.", "The teacher parrot and the student parrot."), ("선생은 크고 잘하고, 학생은 작고 빨라요.", "The teacher is big and good; the student is small and fast.")),
        ("합성 데이터", "Synthetic data", ("앵무새가 쓴 답 쪽지.", "Answer notes a parrot wrote."), ('사람이 아니라 앵무새가 만든 문제집. → <a href="synthetic-ko.html">앵무새가 쓴 책으로 앵무새 가르치기</a>', 'A workbook made by a parrot, not people. → <a href="synthetic-en.html">teaching a parrot with a parrot\'s book</a>')),
        ("소형 모델 (SLM)", "Small language model (SLM)", ("작은 앵무새.", "The small parrot."), ("폰이나 노트북에도 올라가요. 한 가지 일은 잘해요.", "Fits on a phone or laptop. Good at one job.")),
        ("파인튜닝", "Fine-tuning", ("답 쪽지로 하는 특훈.", "The drill on answer notes."), ('학생이 배우는 방법이에요. → <a href="finetune-ko.html">짧은 특훈</a>', 'How the student learns. → <a href="finetune-en.html">the short drill</a>')),
        ("양자화와의 차이", "Versus quantization", ("새로 가르치기 vs 같은 새를 가볍게.", "Teach a new bird vs lighten the same bird."), ('증류는 다른 앵무새를 키우고, 양자화는 그 앵무새의 숫자를 굵게 적어요. → <a href="quantization-ko.html">콩을 굵게 세기</a>', 'Distillation raises another parrot; quantization rewrites the same parrot\'s numbers coarsely. → <a href="quantization-en.html">counting beans coarsely</a>')),
        ("라우팅", "Routing", ("어느 앵무새에게 시킬까.", "Which parrot gets the job."), ('쉬운 일은 학생, 어려운 일은 선생. → <a href="routing-ko.html">어느 앵무새에게 시킬까</a>', 'Easy jobs to the student, hard ones to the teacher. → <a href="routing-en.html">which parrot gets the job</a>')),
        ("평가", "Evaluation", ("선생과 학생의 시험.", "The teacher-and-student test."), ('학생이 충분한지 점수로 확인해요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Confirm with scores that the student is good enough. → <a href="evaluation-en.html">the examiner\'s scorecard</a>')),
    ],
}
