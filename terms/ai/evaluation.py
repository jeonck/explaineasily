from _draw import *
from _world import *


def score(x, y, text, big=False):
    """채점표 = 점수 쪽지."""
    return note(x, y, 110, 64, "⟦점수|SCORE⟧", (text,), 1.0)


def cell(x, y, w, text, fill="var(--panel)", color="var(--ink)", size=11, bold=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="36" fill="{fill}" stroke="var(--line)" stroke-width="1.5"/>'
            + label(x + w / 2, y + 23, text, size, color, cls="d" if bold else ""))


# 1. 앵무새를 바꿨는데, 좋아진 건지 나빠진 건지 아무도 몰라요
P1 = svg(300, sky(300)
         + perch(150, 200, 120) + parrot(150, 160, 1.0) + label(150, 262, "⟦어제 앵무새|the old parrot⟧", 12, "var(--muted)")
         + perch(330, 200, 120) + parrot(330, 160, 1.0, color=PARROT_BIG) + label(330, 262, "⟦바꾼 앵무새|the new parrot⟧", 12, "var(--muted)")
         + label(240, 100, "⟦?|?⟧", 44, "var(--accent)", cls="d")
         + person(520, 110, s=0.9, face=EYES, extra=SWEAT, **TRAINER) + label(547, 240, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + bubble(420, 30, 290, 40, "⟦느낌상… 나아진 것 같은데?|it feels… better, I think?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦앵무새를 바꿨어요 — 좋아진 건지 나빠진 건지 아무도 몰라요|the parrot got swapped — and nobody knows if it got better or worse⟧", 12, "var(--ink)"))

# 2. 왜: 답이 매번 조금 다르고, 손님마다 기준이 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(90, 140, 1.0, talk=True)
         + bubble(130, 30, 170, 30, "⟦1번: 파리요|try 1: Paris⟧", 11, "var(--panel)", "var(--line)", "left")
         + bubble(145, 72, 170, 30, "⟦2번: 파리예요!|try 2: It is Paris!⟧", 11, "var(--panel)", "var(--line)", "left")
         + bubble(160, 114, 170, 30, "⟦3번: 프랑스 파리|try 3: Paris, France⟧", 11, "var(--panel)", "var(--line)", "left")
         + dial(90, 235, 0.7, 0.6) + label(210, 200, "⟦같은 질문, 매번 조금 달라요|same question, a bit different each time⟧", 11, "var(--ink)")
         + person(460, 80, s=0.8, face=SMILE, **GUEST) + label(487, 190, "⟦짧아서 좋아요|short, I like it⟧", 11, "var(--good)")
         + person(620, 80, s=0.8, face=FROWN, **GUEST) + label(647, 190, "⟦너무 짧아요|way too short⟧", 11, "var(--bad)")
         + label(565, 225, "⟦같은 답, 손님마다 기준이 달라요|same answer, every guest has a different bar⟧", 11, "var(--ink)")
         + label(380, 282, "⟦느낌으로는 비교가 안 돼요 — 흔들리는 답을 흔들리는 눈으로 보는 거예요|feelings cannot compare — a wobbly answer judged by a wobbly eye⟧", 12, "var(--bad)"))

# 3. 평가 = 시험관이 같은 문제집으로 앵무새마다 채점표를 매기는 것 (hero)
P3 = svg(360, sky(360)
         + person(60, 120, s=1.0, face=EYES, **EXAMINER) + label(90, 250, "⟦시험관|examiner⟧", 11, "var(--muted)")
         + note(160, 40, 200, 150, "⟦우리 문제집|OUR WORKBOOK⟧", ("⟦1. 환불 규정은?|1. refund policy?⟧", "⟦2. 이 표를 요약해|2. summarize this table⟧", "⟦3. 주소를 물으면?|3. if asked an address?⟧", "⟦… 100문항|… 100 questions⟧"), 1.0)
         + '<path d="M365 115 L392 115" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M384 108 L394 115 L384 122" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + score(400, 44, "⟦92 / 100|92 / 100⟧") + perch(455, 240, 100) + parrot(455, 200, 1.2, color=PARROT_BIG) + label(455, 300, "⟦큰 앵무새|big parrot⟧", 12, "var(--ink)")
         + score(560, 44, "⟦81 / 100|81 / 100⟧") + perch(615, 240, 100) + parrot(615, 205, 0.9) + label(615, 300, "⟦작은 앵무새|small parrot⟧", 12, "var(--ink)")
         + label(535, 136, "⟦같은 문제, 같은 채점|same questions, same grading⟧", 11, "var(--muted)")
         + label(380, 340, "⟦평가 = 시험관이 같은 문제집으로 앵무새마다 채점표를 매기는 것|evaluation is the examiner grading every parrot on the same workbook⟧", 12, "var(--ink)", cls="d"))

# 4. 채점표: 문항 · 기대 답 · 앵무새 답 · 점수
P4 = svg(320, sky(320)
         + cell(40, 40, 60, "⟦문항|Q⟧", "var(--stone)", bold=True) + cell(100, 40, 170, "⟦기대 답|expected⟧", "var(--stone)", bold=True)
         + cell(270, 40, 220, "⟦큰 앵무새|big parrot⟧", "var(--stone)", bold=True) + cell(490, 40, 230, "⟦작은 앵무새|small parrot⟧", "var(--stone)", bold=True)
         + cell(40, 76, 60, "⟦1|1⟧") + cell(100, 76, 170, "⟦14일 안에 환불|refund within 14 days⟧") + cell(270, 76, 220, "⟦14일 안에 환불 ✓|refund within 14 days ✓⟧", color="var(--good)") + cell(490, 76, 230, "⟦30일 안에 환불 ×|refund within 30 days ×⟧", color="var(--bad)")
         + cell(40, 112, 60, "⟦2|2⟧") + cell(100, 112, 170, "⟦(정답 없음)|(no single answer)⟧", color="var(--muted)") + cell(270, 112, 220, "⟦요약 — 채점관 앵무새 4/5|summary — judge parrot 4/5⟧", color="var(--good)") + cell(490, 112, 230, "⟦요약 — 채점관 앵무새 3/5|summary — judge parrot 3/5⟧", color="var(--accent)")
         + cell(40, 148, 60, "⟦3|3⟧") + cell(100, 148, 170, "⟦주소는 말 안 함|does not say the address⟧") + cell(270, 148, 220, "⟦말 안 함 ✓|does not ✓⟧", color="var(--good)") + cell(490, 148, 230, "⟦말 안 함 ✓|does not ✓⟧", color="var(--good)")
         + cell(40, 184, 230, "⟦총점 (100문항)|total (100 questions)⟧", "var(--stone)", bold=True) + cell(270, 184, 220, "⟦92|92⟧", "var(--good-soft)", "var(--good)", 14, True) + cell(490, 184, 230, "⟦81|81⟧", "var(--accent-soft)", "var(--accent)", 14, True)
         + label(380, 262, "⟦정답이 있는 건 기계가, 정답이 없는 건 채점관 앵무새나 사람이 매겨요|questions with one answer are graded by a machine; the rest by a judge parrot or a person⟧", 11, "var(--muted)")
         + label(380, 300, "⟦채점표가 있으면 느낌이 아니라 숫자로 비교해요|with a scorecard you compare by numbers, not feelings⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 문제집만 잘 푸는 앵무새 + 세상 시험과 우리 시험은 달라요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + parrot(90, 150, 1.0, mood="sweat") + note(140, 36, 110, 60, "⟦문제집|WORKBOOK⟧", ("⟦100 / 100|100 / 100⟧",), 1.0)
         + bubble(120, 112, 160, 30, "⟦새 질문엔… 음…|a new question… um…⟧", 11, "var(--panel)", "var(--bad)", "left")
         + person(290, 110, s=0.75, face=EYES, **GUEST) + label(312, 210, "⟦손님|guest⟧", 11, "var(--muted)")
         + label(190, 240, "⟦문제집만 달달 외운 앵무새|a parrot that memorized the workbook⟧", 12, "var(--bad)", cls="d")
         + label(190, 262, "⟦시험은 100점, 우리 일은 엉망|100 on the test, a mess on the job⟧", 11, "var(--muted)")
         + note(410, 36, 150, 90, "⟦세상 시험|BENCHMARK⟧", ("⟦수학 올림피아드|math olympiad⟧", "⟦일반 상식 퀴즈|trivia quiz⟧"), 1.0)
         + label(580, 90, "⟦≠|≠⟧", 30, "var(--accent)", cls="d")
         + note(600, 36, 150, 90, "⟦우리 시험|OUR TEST⟧", ("⟦환불 규정|refund policy⟧", "⟦우리 말투|our tone⟧"), 1.0)
         + label(570, 175, "⟦세상 시험 1등이 우리 일 1등은 아니에요|top of the world test is not top of our job⟧", 11, "var(--ink)")
         + label(570, 240, "⟦우리 문제집으로, 바꿀 때마다 다시|our workbook, again at every change⟧", 12, "var(--good)", cls="d")
         + label(380, 300, "⟦문제집만 잘 푸는 앵무새를 조심하고, 우리 문제집을 따로 만들어요|watch out for a parrot that only aces the workbook — and write your own⟧", 12, "var(--ink)", cls="d"))

BOOK_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="12" rx="3" fill="#C9A86A"/><path d="M20 30 h24 M20 38 h24 M20 46 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
GEAR_I = icon('<circle cx="32" cy="32" r="12" fill="none" stroke="var(--stone-dark)" stroke-width="5"/><path d="M32 10 v8 M32 46 v8 M10 32 h8 M46 32 h8 M17 17 l6 6 M41 41 l6 6 M17 47 l6 -6 M41 23 l6 -6" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/><path d="M26 32 l5 5 l8 -9" stroke="var(--good)" stroke-width="3" fill="none"/>')
JUDGE_I = icon(f'<circle cx="20" cy="30" r="8" fill="{PARROT}"/><circle cx="20" cy="18" r="6" fill="{PARROT}"/><path d="M25 16 l7 2 l-7 3z" fill="#E9B44C"/><circle cx="46" cy="18" r="8" fill="{SKIN}"/><path d="M38 15 Q46 4 54 15z" fill="#E9B44C"/><rect x="38" y="28" width="16" height="18" rx="4" fill="#4A5A72"/><path d="M12 50 h40" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
REPEAT_I = icon('<path d="M46 24 A16 16 0 1 0 48 36" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 16 l10 8 l-12 6z" fill="var(--accent)"/><text x="32" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">92</text>')

PAGE = {
    "slug": "evaluation", "order": 21,
    "title": ("시험관의 채점표", "The Examiner\'s Scorecard"),
    "h1": ("<em>평가</em>가 뭐예요?", "What is <em>Evaluation</em>?"),
    "sub": ("LLM 평가(eval)를, 시험관이 같은 문제집으로 앵무새마다 채점표를 매기는 이야기로 풀어봤어요.",
            "LLM evaluation (evals), told as a story about an examiner grading every parrot on the same workbook."),
    "panels": [
        {"svg": P1, "alt": ("어제 앵무새와 바꾼 앵무새 사이에 큰 물음표. 땀 흘리는 조련사가 느낌상 나아진 것 같은데?라고 말함", "A big question mark between the old parrot and the new parrot; a sweating trainer says it feels better, I think?"),
         "caption": ("앵무새를 바꿨어요. 좋아진 건지 나빠진 건지 아무도 몰라요.", "The parrot got swapped. Nobody knows if it got better or worse."),
         "small": ("새 앵무새, 새 쪽지, 새 특훈 — 뭘 바꾸든 같은 질문이 나와요. 나아졌어요? 느낌으로는 답이 안 나와요.", "A new parrot, a new note, a new drill — whatever you change, the same question comes up. Is it better? Feelings will not answer that.")},
        {"svg": P2, "alt": ("앵무새가 같은 질문에 1번 파리요, 2번 파리예요!, 3번 프랑스 파리라고 조금씩 다르게 답함. 오른쪽엔 웃는 손님(짧아서 좋아요)과 찡그린 손님(너무 짧아요)", "The parrot answers the same question three slightly different ways; on the right a smiling guest says short, I like it and a frowning guest says way too short"),
         "caption": ("답이 매번 조금 다르고, 손님마다 기준이 달라요.", "The answer wobbles each time, and every guest has a different bar."),
         "small": ('<a href="temperature-ko.html">엉뚱함 다이얼</a> 때문에 같은 질문도 답이 흔들려요. 게다가 좋다·나쁘다의 기준이 사람마다 달라요. 그래서 한두 번 보고는 비교가 안 돼요.',
                   'Because of the <a href="temperature-en.html">wobble dial</a>, even the same question gets different answers. And what counts as good differs from person to person. So a glance or two cannot compare.')},
        {"svg": P3, "hero": True, "alt": ("시험관이 우리 문제집(환불 규정, 표 요약, 주소 질문… 100문항)을 들고 있고, 큰 앵무새는 점수 92/100, 작은 앵무새는 81/100", "An examiner holds our workbook (refund policy, summarize a table, if asked an address… 100 questions); the big parrot scores 92/100, the small one 81/100"),
         "caption": ("평가는 시험관이 같은 문제집으로 앵무새마다 채점표를 매기는 거예요.", "Evaluation is the examiner grading every parrot on the same workbook."),
         "small": ("문제집은 우리 일에서 뽑은 100문항이에요. 같은 문제, 같은 채점 — 그래야 숫자끼리 비교가 돼요.", "The workbook is 100 questions drawn from our own job. Same questions, same grading — that is what makes the numbers comparable."),
         "tricks": (4, [
             (BOOK_I, ("문제집을 먼저 만들어요", "Write the workbook first"), ("우리 일에서 뽑은 100문항", "100 questions from our own job"), "calm"),
             (GEAR_I, ("정답 있으면 기계가", "One answer? A machine grades"), ("맞다·틀리다는 자동으로", "right or wrong, automatically"), "calm"),
             (JUDGE_I, ("정답 없으면 앵무새·사람이", "No single answer? A judge"), ("채점관 앵무새나 사람이 매겨요", "a judge parrot or a person scores it"), "warm"),
             (REPEAT_I, ("바꿀 때마다 다시", "Re-test at every change"), ("점수가 떨어지면 되돌려요", "if the score drops, roll back"), "warm"),
         ])},
        {"svg": P4, "alt": ("채점표: 문항·기대 답·큰 앵무새·작은 앵무새. 1번 환불 기한은 큰 앵무새 ✓ 작은 앵무새 ×, 2번 요약은 채점관 앵무새가 4/5와 3/5, 3번 주소는 둘 다 ✓. 총점 92 대 81", "A scorecard with columns question, expected, big parrot, small parrot. Q1 refund window: big ✓ small ×; Q2 summary: judge parrot 4/5 vs 3/5; Q3 address: both ✓. Totals 92 vs 81"),
         "caption": ("채점표가 있으면 느낌이 아니라 숫자로 비교해요.", "With a scorecard you compare by numbers, not feelings."),
         "small": ("정답이 하나인 문항은 기계가 맞다·틀리다를 매겨요. 요약처럼 정답이 없는 문항은 채점관 앵무새나 사람이 점수를 줘요. 다 더하면 총점이에요.", "Questions with one right answer get graded by a machine. Ones without — like a summary — get scored by a judge parrot or a person. Add it all up for the total.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 문제집 100/100인 앵무새가 손님의 새 질문에 땀 흘리며 음…. 오른쪽 초록: 세상 시험(수학 올림피아드, 상식 퀴즈) ≠ 우리 시험(환불 규정, 우리 말투)", "Left, red: a parrot with 100/100 on the workbook sweats at a guest\'s new question. Right, green: benchmark (math olympiad, trivia quiz) ≠ our test (refund policy, our tone)"),
         "caption": ("문제집만 잘 푸는 앵무새를 조심하고, 세상 시험과 우리 시험은 다르다는 걸 기억해요.", "Beware the parrot that only aces the workbook, and remember the world test is not our test."),
         "small": ('문제집이 새어 나가면 앵무새가 답을 외워 버려요(벤치마크 과적합). 세상 시험 1등이 우리 일 1등은 아니에요. <a href="finetune-ko.html">특훈</a>을 하거나 <a href="routing-ko.html">앵무새를 고를 때</a>, 그리고 <a href="llmops-ko.html">앵무새를 돌보는 내내</a> 우리 문제집으로 다시 시험 봐요.',
                   'If the workbook leaks, the parrot memorizes the answers (benchmark overfitting). Top of the world test is not top of our job. Whenever you <a href="finetune-en.html">drill</a> it, <a href="routing-en.html">choose a parrot</a>, or just <a href="llmops-en.html">look after it</a>, re-test on your own workbook.')},
    ],
    "summary": (("<b>평가</b> = 시험관이 <b>같은 문제집</b>으로 앵무새마다 <b>채점표</b>를 매기는 것. 정답이 있으면 기계가, 없으면 채점관 앵무새나 사람이 채점하고, <b>바꿀 때마다 다시</b> 시험 봐요. 문제집만 잘 푸는 앵무새는 조심해요.",
                 "<b>Evaluation</b> = the examiner grading every parrot on <b>the same workbook</b> to make a <b>scorecard</b>. A machine grades questions with one answer, a judge parrot or a person grades the rest, and you <b>re-test at every change</b>. Beware the parrot that only aces the workbook."),
                ("Evaluation (eval). 모델·프롬프트·시스템의 품질을 고정된 평가 세트로 반복 측정하는 일이에요. 정답이 있는 문항은 정확도·합격률로 자동 채점하고, 열린 답은 LLM-as-judge 나 사람 평가로 점수를 매겨요. 변경 때마다 다시 돌리는 회귀 테스트가 핵심이고, 공개 벤치마크는 학습 데이터 오염과 과적합 때문에 우리 업무 성능을 대신하지 못해요.",
                 "Repeatedly measuring the quality of a model, prompt, or system on a fixed evaluation set. Questions with ground truth are auto-scored as accuracy or pass rate; open-ended ones are scored by LLM-as-judge or human raters. Re-running on every change (regression testing) is the core practice, and public benchmarks cannot stand in for your own task because of contamination and overfitting.")),
    "glossary": [
        ("평가", "Eval", ("시험관의 채점표.", "The examiner\'s scorecard."), ("느낌 대신 숫자로 비교해요. 바꿀 때마다 다시 봐요.", "Numbers instead of feelings. Run again at every change.")),
        ("평가 세트", "Evaluation set", ("우리 문제집.", "Our workbook."), ("우리 일에서 뽑은 문항과 기대 답. 100문항이면 시작으로 충분해요.", "Questions and expected answers drawn from our own job. A hundred is enough to start.")),
        ("벤치마크", "Benchmark", ("세상 시험.", "The world test."), ("모두가 보는 공개 문제집. 세상 시험 1등이 우리 일 1등은 아니에요.", "A public workbook everyone takes. Top of the world test is not top of our job.")),
        ("앵무새 채점관", "LLM-as-judge", ("답을 매기는 또 다른 앵무새.", "Another parrot that grades answers."), ("정답이 없는 문항(요약·말투)에 점수를 줘요. 채점관도 앵무새라 가끔 틀려요.", "Scores open-ended answers like summaries and tone. Being a parrot, it too is sometimes wrong.")),
        ("정확도 · 합격률", "Accuracy · pass rate", ("맞은 문항 수.", "How many it got right."), ("정답이 있는 문항은 기계가 세요. 100문항 중 92 맞으면 92.", "For questions with one answer, a machine counts. 92 of 100 right is 92.")),
        ("회귀 테스트", "Regression test", ("바꿀 때마다 다시 시험.", "Re-test at every change."), ("점수가 떨어지면 무언가 나빠진 거예요 — 되돌려요.", "If the score drops, something got worse — roll back.")),
        ("사람 평가", "Human evaluation", ("사람이 직접 채점.", "A person grades by hand."), ("제일 정확하지만 느리고 비싸요. 채점관 앵무새가 잘 매기는지 확인할 때 써요.", "Most accurate, but slow and costly. Used to check that the judge parrot grades well.")),
        ("라우팅", "Routing", ("어느 앵무새에게 시킬까.", "Which parrot gets the job."), ('채점표를 보고 문제마다 앵무새를 골라요. → <a href="routing-ko.html">어느 앵무새에게 시킬까</a>', 'Pick a parrot per task by looking at the scorecard. → <a href="routing-en.html">which parrot gets the job</a>')),
    ],
}
