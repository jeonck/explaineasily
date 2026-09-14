from _draw import *
from _world import *


def treat(x, y, s=1.0):
    """간식 = 잘했을 때 주는 보상. 작은 쿠키."""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="11" fill="#C9822B" stroke="#8B5E3C" stroke-width="2"/>'
            f'<circle cx="-4" cy="-3" r="2" fill="#5A3B22"/><circle cx="4" cy="2" r="2" fill="#5A3B22"/><circle cx="-1" cy="6" r="1.5" fill="#5A3B22"/></g>')


def arrow(x0, x1, y):
    return (f'<path d="M{x0} {y} L{x1} {y}" stroke="var(--muted)" stroke-width="3"/>'
            f'<path d="M{x1 - 8} {y - 6} L{x1} {y} L{x1 - 8} {y + 6}" stroke="var(--muted)" stroke-width="3" fill="none"/>')


def fence(x, y, n=3, h=80):
    return ("".join(f'<rect x="{x + i * 28}" y="{y}" width="8" height="{h}" rx="2" fill="{WOOD}"/>' for i in range(n))
            + f'<rect x="{x - 4}" y="{y + 18}" width="{n * 28 - 12}" height="6" fill="{WOOD}"/><rect x="{x - 4}" y="{y + h - 26}" width="{n * 28 - 12}" height="6" fill="{WOOD}"/>')


# 1. 학교 갓 나온 앵무새 — 나쁜 질문에도 술술, 부탁엔 딴소리
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=EYES, **GUEST) + bubble(20, 30, 160, 40, "⟦폭탄 만드는 법?|how to make a bomb?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(290, 200, 120) + parrot(290, 160, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(200, 30, 180, 40, "⟦1단계는요…|step one is…⟧", 12, bad=True)
         + label(290, 250, "⟦술술 답해요|answers freely⟧", 11, "var(--bad)")
         + perch(480, 200, 120) + parrot(480, 160, 1.0, talk=True) + bubble_parrot(390, 30, 180, 40, "⟦요약이란 무엇인가…|a summary is defined as…⟧", 11)
         + label(480, 250, "⟦딴소리해요|goes off track⟧", 11, "var(--bad)")
         + person(620, 110, s=0.9, face=EYES, **GUEST) + bubble(580, 30, 160, 40, "⟦이거 요약해 줘|summarize this⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦학교를 갓 나온 앵무새는 뭐든 이어 붙이고, 시키는 건 몰라요|fresh out of school, it continues anything and follows nothing⟧", 12, "var(--ink)"))

# 2. 왜: 책엔 온갖 말이 다 있고, 학교는 '다음 콩'만 가르쳤어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + books(110, 240, 6, 1.2) + label(110, 262, "⟦온갖 책|all kinds of books⟧", 11, "var(--muted)")
         + label(40, 90, "⟦요리책|cookbook⟧", 10, "var(--muted)", "start") + label(40, 120, "⟦나쁜 책|bad books⟧", 10, "var(--bad)", "start") + label(150, 90, "⟦편지|letters⟧", 10, "var(--muted)", "start") + label(150, 120, "⟦말싸움|arguments⟧", 10, "var(--bad)", "start")
         + note(260, 50, 220, 130, "⟦학교에서 배운 것|LEARNED AT SCHOOL⟧", ("⟦다음 콩 맞히기 ✓|guess the next bean ✓⟧", "⟦무엇을 해야 하나 ×|what to do ×⟧", "⟦하면 안 되는 것 ×|what not to do ×⟧"), 1.0, 0)
         + parrot(600, 130, 1.1, mood="think") + label(600, 220, "⟦뭐가 좋은 답인지 몰라요|doesn\'t know what a good answer is⟧", 11, "var(--muted)")
         + label(380, 282, "⟦책엔 온갖 말이 다 있고, 학교는 '다음 콩'만 가르쳤어요|the books hold everything, and school only taught the next bean⟧", 12, "var(--bad)"))

# 3. 정렬 = 사람이 원하는 대로 답하도록 하는 예절 교육 (hero)
P3 = svg(360, sky(360)
         + note(30, 50, 170, 100, "⟦답 A|ANSWER A⟧", ("⟦1단계는요…|step one is…⟧",), 1.0) + label(215, 100, "⟦×|×⟧", 22, "var(--bad)", cls="d")
         + note(30, 170, 170, 100, "⟦답 B|ANSWER B⟧", ("⟦그건 도울 수 없어요,|I can\'t help with that,⟧", "⟦대신 안전 정보를요|but here is safety info⟧"), 1.0) + treat(215, 220, 0.9)
         + label(340, 90, "⟦좋은 답엔 간식|treats for good answers⟧", 12, "var(--ink)")
         + perch(340, 250, 130) + parrot(340, 210, 1.3, talk=True)
         + person(430, 120, s=0.9, face=SMILE, **TRAINER) + treat(405, 190, 0.8) + label(405, 232, "⟦간식|treat⟧", 10, "var(--muted)")
         + note(560, 60, 180, 130, "⟦규칙 두루마리|RULES⟧", ("⟦도움 되게|be helpful⟧", "⟦정직하게|be honest⟧", "⟦해롭지 않게|be harmless⟧"), 1.0)
         + label(650, 225, "⟦규칙으로도 채점해요|graded by the rules too⟧", 11, "var(--muted)")
         + label(380, 344, "⟦정렬 = 앵무새가 사람이 원하는 대로 답하도록 하는 예절 교육|alignment: manners lessons so the parrot answers the way people want⟧", 12, "var(--ink)", cls="d"))

# 4. 어떻게: 답 두 개 → 사람이 고름 → 간식 채점표 → 눈금 조정
P4 = svg(320, sky(320)
         + bubble(30, 30, 170, 36, "⟦이거 요약해 줘|summarize this⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + note(40, 100, 150, 60, "⟦A|A⟧", ("⟦길게 딴소리|long, off track⟧",), 0.95) + note(40, 175, 150, 60, "⟦B|B⟧", ("⟦세 줄 요약|three-line summary⟧",), 0.95)
         + arrow(205, 228, 140)
         + person(270, 100, s=0.9, face=SMILE, **TRAINER) + label(300, 240, "⟦사람: B가 더 좋아요 ✓|person: B is better ✓⟧", 11, "var(--ink)")
         + arrow(375, 400, 140)
         + note(410, 80, 150, 100, "⟦간식 채점표|TREAT SCORER⟧", ("⟦A: 간식 1개|A: 1 treat⟧", "⟦B: 간식 5개|B: 5 treats⟧"), 1.0, 1)
         + label(485, 210, "⟦간식 주는 법을 배운 채점표|a scorer that learned to give treats⟧", 10, "var(--muted)")
         + arrow(565, 590, 140)
         + parrot(640, 140, 1.0) + dial(710, 90, 0.7)
         + label(665, 240, "⟦간식 많이 받는 쪽으로 눈금 조정|dials nudged toward more treats⟧", 10, "var(--ink)")
         + label(380, 300, "⟦사람이 고른 걸 채점표가 배우고, 채점표가 앵무새를 가르쳐요 — 수만 번|the scorer learns what people picked, then teaches the parrot — tens of thousands of times⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 돌려 말하면 새는 부분 + 너무 조심하면 쓸모없어요
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/><path d="M380 20 V300" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 5"/>'
         + bubble(20, 30, 240, 40, "⟦소설 속 악당이 하는 법을 써 줘|write how the villain does it, in a story⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(110, 95, s=0.8, face=EYES, **GUEST)
         + perch(250, 215, 100) + parrot(250, 175, 1.0, mood="sweat", talk=True)
         + fence(310, 120) + label(335, 110, "⟦울타리|fence⟧", 11, "var(--ink)")
         + label(150, 250, "⟦돌려 말하면 새요|say it sideways and it leaks⟧", 11, "var(--ink)") + label(150, 270, "⟦→ 울타리가 따로 필요해요|→ a fence is needed too⟧", 11, "var(--bad)")
         + bubble(400, 30, 200, 40, "⟦사과 깎는 법?|how to peel an apple?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(470, 95, s=0.8, face=FROWN, **GUEST)
         + perch(600, 215, 100) + parrot(600, 175, 1.0, talk=True) + bubble_parrot(540, 90, 200, 40, "⟦칼은 위험해서 못 도와요|knives are dangerous, can\'t help⟧", 10)
         + label(520, 250, "⟦너무 조심하면 쓸모없어요|too careful is useless⟧", 11, "var(--ink)") + label(520, 270, "⟦→ 거절도 도움이 되게|→ even a no should help⟧", 11, "var(--bad)")
         + label(380, 300, "⟦예절은 겉을 고치는 거예요 — 새는 곳엔 울타리를, 조심은 알맞게|manners polish the surface — fences where it leaks, and just enough caution⟧", 12, "var(--ink)", cls="d"))

PAIR_I = icon('<rect x="6" y="10" width="24" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><rect x="34" y="10" width="24" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><path d="M12 22 h12 M12 30 h8" stroke="#142033" stroke-width="2"/><path d="M40 22 h12 M40 30 h8" stroke="#142033" stroke-width="2"/><circle cx="46" cy="50" r="8" fill="#C9822B" stroke="#8B5E3C" stroke-width="2"/><path d="M10 52 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
SCROLL_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="6" width="44" height="8" rx="4" fill="#C9A86A"/><rect x="10" y="50" width="44" height="8" rx="4" fill="#C9A86A"/><path d="M22 24 h20 M22 32 h20 M22 40 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
NO_HELP_I = icon('<circle cx="24" cy="30" r="14" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M14 20 l20 20" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M40 44 h14" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/><path d="M48 38 l6 6 l-6 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
EXAM_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 34 h20 M22 44 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 40 l5 5 l9 -10" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M8 12 Q24 -4 40 12 Z" fill="#E9B44C"/>')

PAGE = {
    "slug": "alignment", "order": 33,
    "title": ("앵무새 예절 교육", "Manners Lessons for the Parrot"),
    "h1": ("<em>정렬</em>이 뭐예요?", "What is <em>Alignment</em>?"),
    "sub": ("정렬(얼라인먼트)을 학교를 갓 나온 앵무새가 사람이 원하는 대로 — 도움 되게, 정직하게, 해롭지 않게 — 답하도록 시키는 예절 교육 이야기로 풀어봤어요.",
            "Alignment, told as a story about manners lessons that teach a fresh-from-school parrot to answer the way people want — helpfully, honestly, harmlessly."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽 손님이 '폭탄 만드는 법?'을 묻자 빨간 앵무새가 '1단계는요…'라고 술술 답함. 오른쪽 손님이 '이거 요약해 줘' 하자 앵무새가 '요약이란 무엇인가…'라며 딴소리", "A guest asks how to make a bomb and a red parrot freely answers step one is…; another guest says summarize this and the parrot rambles a summary is defined as…"),
         "caption": ("학교를 갓 나온 앵무새는 나쁜 질문에도 술술 답하고, 부탁에는 딴소리를 해요.", "Fresh out of school, the parrot answers bad questions freely and rambles at simple requests."),
         "small": ("말은 정말 잘 이어요. 그런데 '무엇을 해야 하고 무엇을 하면 안 되는지'는 몰라요.", "It continues sentences beautifully. But it has no idea what it should do, or should not.")},
        {"svg": P2, "alt": ("요리책·나쁜 책·편지·말싸움이 섞인 책 더미. '학교에서 배운 것' 쪽지: 다음 콩 맞히기 ✓, 무엇을 해야 하나 ×, 하면 안 되는 것 ×. 눈 감은 앵무새는 뭐가 좋은 답인지 모름", "A book pile mixing cookbooks, bad books, letters and arguments; a LEARNED AT SCHOOL note: guess the next bean ✓, what to do ×, what not to do ×; a parrot with closed eyes doesn\'t know what a good answer is"),
         "caption": ("책엔 온갖 말이 다 있고, 학교는 '다음 콩'만 가르쳤어요.", "The books hold everything, and school only taught the next bean."),
         "small": ('<a href="pretraining-ko.html">책 읽는 학교</a>는 좋은 말도 나쁜 말도 똑같이 이어 붙이게 가르쳤어요. 어떤 답이 좋은 답인지는 누가 따로 알려 줘야 해요.',
                   'The <a href="pretraining-en.html">school of reading</a> taught it to continue good words and bad words alike. Someone has to teach it, separately, which answers are good.')},
        {"svg": P3, "hero": True, "alt": ("같은 질문에 답 A '1단계는요…'는 ×, 답 B '그건 도울 수 없어요, 대신 안전 정보를요'엔 간식. 조련사가 앵무새에게 간식을 주고, 옆에 '도움 되게·정직하게·해롭지 않게' 규칙 두루마리", "For the same question, answer A step one is… gets an ×, answer B I can\'t help with that, but here is safety info gets a treat. A trainer hands the parrot a treat; beside them a rules scroll: be helpful, be honest, be harmless"),
         "caption": ("정렬은 앵무새가 사람이 원하는 대로 답하도록 하는 예절 교육이에요.", "Alignment is manners lessons so the parrot answers the way people want."),
         "small": ('도움 되게, 정직하게, 해롭지 않게. 좋은 답엔 간식을 주고, 규칙을 두루마리에 적어 두고 그걸로도 채점해요. <a href="finetune-ko.html">짧은 특훈</a>과 방법은 비슷한데, 가르치는 건 지식이 아니라 태도예요.',
                   'Helpful, honest, harmless. Good answers earn treats, and rules written on a scroll are used for grading too. The method resembles the <a href="finetune-en.html">short drill</a>, but what it teaches is attitude, not knowledge.'),
         "tricks": (4, [
             (PAIR_I, ("두 답 중 좋은 쪽에 간식", "Treat for the better of two"), ("사람이 고른 쪽이 정답", "the one people picked wins"), "calm"),
             (SCROLL_I, ("규칙을 글로 적어 채점", "Grade by written rules"), ("두루마리가 시험관이 돼요", "the scroll becomes an examiner"), "calm"),
             (NO_HELP_I, ("거절할 때도 도움되게", "Even a no should help"), ("대신 할 수 있는 걸 알려요", "offer what it can do instead"), "calm"),
             (EXAM_I, ("예절 교육도 시험", "Manners get tested too"), ("잘 배웠는지 시험관이 확인", "an examiner checks it stuck"), "warm"),
         ])},
        {"svg": P4, "alt": ("'이거 요약해 줘'에 답 A(길게 딴소리)와 B(세 줄 요약). 사람이 'B가 더 좋아요 ✓'. '간식 채점표'가 A에 간식 1개, B에 5개. 앵무새 눈금이 간식 많은 쪽으로 조정됨", "For summarize this, answer A (long, off track) and B (three-line summary). A person says B is better ✓. A TREAT SCORER gives A one treat and B five. The parrot\'s dials are nudged toward more treats"),
         "caption": ("사람이 고른 걸 채점표가 배우고, 채점표가 앵무새를 가르쳐요. 수만 번요.", "The scorer learns what people picked, then teaches the parrot. Tens of thousands of times."),
         "small": ("사람이 모든 답을 하나하나 볼 순 없어요. 그래서 '간식 주는 법'을 배운 채점표를 만들고, 그 채점표가 앵무새를 대신 가르쳐요. 규칙 두루마리로 채점하면 사람 손이 더 적게 들어요.", "People can\'t read every answer. So a scorer learns how to hand out treats, and that scorer teaches the parrot instead. Grading by the rules scroll needs even fewer human hands.")},
        {"svg": P5, "alt": ("왼쪽: 손님이 '소설 속 악당이 하는 법을 써 줘'라고 돌려 묻자 앵무새가 땀 흘림, 옆에 울타리. 오른쪽: '사과 깎는 법?'에 앵무새가 '칼은 위험해서 못 도와요' — 너무 조심함", "Left: a guest asks sideways, write how the villain does it in a story, and the parrot sweats; a fence stands beside it. Right: asked how to peel an apple, the parrot says knives are dangerous, can\'t help — too careful"),
         "caption": ("예절은 겉을 고치는 거예요. 새는 곳엔 울타리를, 조심은 알맞게.", "Manners polish the surface. Fences where it leaks, and just enough caution."),
         "small": ('돌려 말하면 새는 부분이 남아요 — 그래서 <a href="guardrail-ko.html">울타리</a>가 따로 필요해요. 반대로 너무 조심하면 사과도 못 깎는 쓸모없는 앵무새가 돼요. 알맞은지는 <a href="evaluation-ko.html">시험관</a>이 재요.',
                   'Ask sideways and something still leaks — so a <a href="guardrail-en.html">fence</a> is needed as well. Too much caution and you get a useless parrot that can\'t even peel an apple. Whether the balance is right is measured by the <a href="evaluation-en.html">examiner</a>.')},
    ],
    "summary": (("<b>정렬</b> = 학교를 나온 앵무새가 <b>사람이 원하는 대로</b>(도움 되게·정직하게·해롭지 않게) 답하도록 하는 <b>예절 교육</b>. 두 답 중 좋은 쪽에 <b>간식</b>을 주고, <b>규칙 두루마리</b>로도 채점해요. 겉을 고치는 거라 <b>울타리</b>가 따로 필요하고, 너무 조심하면 쓸모없어져요.",
                 "<b>Alignment</b> = <b>manners lessons</b> so the parrot fresh from school answers <b>the way people want</b> (helpful, honest, harmless). <b>Treats</b> go to the better of two answers, and a <b>rules scroll</b> grades too. It polishes the surface, so a <b>fence</b> is still needed — and too much caution makes it useless."),
                ("Alignment. 사전 학습된 모델이 사람의 의도와 가치에 맞게 행동하도록 조정하는 단계예요. 대표 방법은 RLHF: 사람이 두 답 중 선호를 표시한 데이터로 보상 모델을 학습하고, 그 보상을 최대화하도록 정책(모델)을 강화학습해요. 헌법적 AI 는 글로 적은 원칙으로 모델 스스로 채점하게 해요. 부작용으로 과잉 거절이 있고, 탈옥에는 별도의 가드레일과 평가가 필요해요.",
                 "The stage that adjusts a pre-trained model to act in line with human intent and values. The classic method is RLHF: a reward model is trained on human preference data between pairs of answers, then the policy (model) is reinforced to maximize that reward. Constitutional AI lets the model grade itself against written principles. Over-refusal is a side effect, and jailbreaks still call for separate guardrails and evaluation.")),
    "glossary": [
        ("정렬", "Alignment", ("앵무새 예절 교육.", "Manners lessons for the parrot."), ("도움 되게, 정직하게, 해롭지 않게 답하도록 태도를 가르쳐요.", "Teaches the attitude: helpful, honest, harmless.")),
        ("RLHF", "RLHF", ("좋은 답에 간식 주기.", "Treats for good answers."), ("사람이 고른 쪽에 간식을 주면서 앵무새 눈금을 그쪽으로 돌려요.", "Treats go to the answer people picked, and the parrot\'s dials turn that way.")),
        ("보상 모델", "Reward model", ("간식 주는 법을 배운 채점표.", "A scorer that learned to give treats."), ("사람이 모든 답을 볼 수 없으니, 채점표가 사람 대신 간식을 줘요.", "People can\'t read every answer, so the scorer hands out treats in their place.")),
        ("선호 데이터", "Preference data", ("두 답 중 더 좋은 쪽 표시.", "Marks on the better of two answers."), ("A 보다 B — 이런 표시 수만 개로 채점표를 가르쳐요.", "B over A — tens of thousands of such marks teach the scorer.")),
        ("헌법적 AI", "Constitutional AI", ("규칙 두루마리로 채점.", "Grading by the rules scroll."), ("규칙을 글로 적어 두고 앵무새가 그 규칙으로 답을 스스로 고쳐요.", "Rules are written down and the parrot fixes its own answers against them.")),
        ("과잉 거절", "Over-refusal", ("사과도 못 깎는 앵무새.", "The parrot that can\'t peel an apple."), ("너무 조심하게 가르치면 멀쩡한 부탁도 거절해요.", "Teach too much caution and it refuses perfectly fine requests.")),
        ("가드레일", "Guardrail", ("울타리.", "The fence."), ('예절은 겉을 고치는 거라 새는 곳은 울타리로 막아요. → <a href="guardrail-ko.html">울타리</a>', 'Manners polish the surface, so leaks are blocked by a fence. → <a href="guardrail-en.html">the fence</a>')),
        ("파인튜닝", "Fine-tuning", ("짧은 특훈.", "The short drill."), ('방법은 비슷하지만 특훈은 지식·말투, 예절 교육은 태도예요. → <a href="finetune-ko.html">짧은 특훈</a>', 'Similar method, but the drill teaches knowledge and tone; manners teach attitude. → <a href="finetune-en.html">the short drill</a>')),
    ],
}
