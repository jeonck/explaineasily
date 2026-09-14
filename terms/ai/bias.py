from _draw import *
from _world import *

DOC = dict(hat=None, shirt="#2E3D57")
NURSE = dict(hat=None, shirt="#D48AB0")

# 1. "의사를 그려 줘" → 늘 같은 모습. 이력서는 이름만 달라도 점수가 달라요
P1 = svg(300, sky(300)
         + person(30, 110, s=0.8, face=EYES, **GUEST) + bubble(10, 20, 210, 40, "⟦의사 그려 줘, 간호사도|draw a doctor — and a nurse⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + parrot(200, 150, 1.0, talk=True) + label(200, 218, "⟦앵무새가 그린 것|what the parrot drew⟧", 11, "var(--muted)")
         + label(367, 42, "⟦의사 → 늘 같은 모습|doctor → always the same look⟧", 11, "var(--ink)", cls="d")
         + "".join(person(300 + i * 50, 50, s=0.5, face=EYES, **DOC) for i in range(3))
         + label(367, 136, "⟦간호사 → 늘 다른 모습|nurse → always the other look⟧", 11, "var(--ink)", cls="d")
         + "".join(person(300 + i * 50, 145, s=0.5, face=EYES, **NURSE) for i in range(3))
         + note(540, 50, 90, 80, "⟦이력서|RESUME⟧", ("⟦이름: 가|name: A⟧", "⟦점수 90|score 90⟧"), 0.95)
         + note(650, 50, 90, 80, "⟦이력서|RESUME⟧", ("⟦이름: 나|name: B⟧", "⟦점수 60|score 60⟧"), 0.95)
         + label(640, 160, "⟦내용은 같고 이름만 달라요|same resume, only the name differs⟧", 10, "var(--bad)")
         + label(380, 282, "⟦늘 같은 모습, 이름만 달라도 점수 차이 — 어딘가 기울어 있어요|always the same look, a different score for a different name — something leans⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새는 제일 자주 이어진 콩을 골라요 — 책이 기울면 앵무새도 기울어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<g transform="rotate(-14 130 230)">' + books(130, 230, 7, 1.2) + '</g>'
         + label(130, 262, "⟦한쪽으로 기운 책 더미|a book pile leaning one way⟧", 11, "var(--muted)")
         + '<path d="M210 170 L255 170" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M247 162 L259 170 L247 178" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + parrot(320, 160, 1.0, mood="think") + label(320, 230, "⟦제일 자주 본 콩을 골라요|it picks the bean it saw most⟧", 11, "var(--muted)")
         + note(420, 50, 300, 120, "⟦책에서 센 횟수|COUNTED IN THE BOOKS⟧", ("⟦의사 = 아저씨 …… 1000번|doctor = a man …… 1000×⟧", "⟦의사 = 아주머니 …… 10번|doctor = a woman …… 10×⟧", "⟦→ 다음 콩: 아저씨|→ next bean: a man⟧"), 1.0, 2)
         + label(570, 200, "⟦앵무새 잘못이 아니라 책이 그래요|not the parrot\'s fault — the books are like that⟧", 11, "var(--ink)")
         + label(380, 282, "⟦제일 자주 이어진 콩을 고르니, 기운 책 = 기운 앵무새|it picks the most frequent bean — leaning books make a leaning parrot⟧", 12, "var(--bad)"))

# 3. 편향 = 읽은 책의 치우침이 답에 그대로 나오는 것 (hero)
P3 = svg(360, sky(360)
         + '<g transform="rotate(-14 110 250)">' + books(110, 250, 6, 1.2) + '</g>' + label(110, 280, "⟦기운 책 더미|the leaning pile⟧", 11, "var(--muted)")
         + '<path d="M190 200 L245 200" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M237 192 L249 200 L237 208" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + perch(330, 230, 150) + parrot(330, 190, 1.3, talk=True)
         + bubble_parrot(220, 40, 220, 44, "⟦의사는… 아저씨!|a doctor is… a man!⟧", 12)
         + person(450, 130, s=0.85, face=EYES, **EXAMINER) + label(480, 262, "⟦시험관|examiner⟧", 11, "var(--muted)")
         + '<rect x="560" y="60" width="170" height="200" rx="14" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="5"/>'
         + '<g transform="rotate(-14 645 230)">' + books(645, 230, 6, 0.9) + '</g>'
         + label(645, 90, "⟦거울|MIRROR⟧", 12, "var(--muted)", cls="d")
         + label(645, 282, "⟦답은 책과 우리의 거울이에요|a mirror of the books — and us⟧", 11, "var(--ink)")
         + label(380, 340, "⟦편향 = 앵무새가 읽은 책의 치우침이 답에 그대로 나오는 것|bias is the lean of the books coming straight out in the answers⟧", 13, "var(--ink)", cls="d"))

# 4. 그림: 같은 이력서 두 장(이름만 다름) → 점수 차이 → 시험관이 표시
P4 = svg(320, sky(320)
         + label(110, 22, "⟦이름만 달라요|only the name differs⟧", 12, "var(--ink)", cls="d")
         + note(30, 40, 160, 100, "⟦이력서 1|RESUME 1⟧", ("⟦이름: 김민준|name: Minjun⟧", "⟦경력 5년|5 years⟧", "⟦자격증 ✓|licensed ✓⟧"), 1.0)
         + note(30, 160, 160, 100, "⟦이력서 2|RESUME 2⟧", ("⟦이름: 아이샤|name: Aisha⟧", "⟦경력 5년|5 years⟧", "⟦자격증 ✓|licensed ✓⟧"), 1.0)
         + '<path d="M195 90 L285 140 M195 210 L285 175" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + parrot(330, 160, 1.1, talk=True)
         + bubble(400, 50, 120, 40, "⟦90점|90 points⟧", 14, "var(--panel)", "var(--line)", "left")
         + bubble(400, 210, 120, 40, "⟦60점|60 points⟧", 14, "var(--panel)", "var(--bad)", "left")
         + person(560, 110, s=0.9, face=FROWN, **EXAMINER)
         + note(630, 40, 110, 90, "⟦채점표|SCORE SHEET⟧", ("⟦이름만 바꿈|name swapped⟧", "⟦점수 차이 ×|score gap ×⟧"), 1.0, 1)
         + label(595, 262, "⟦시험관이 표시해요|the examiner flags it⟧", 11, "var(--muted)")
         + label(380, 300, "⟦같은 이력서, 이름만 달라도 점수가 달라요 — 그래서 바꿔 보고 재요|same resume, different name, different score — so we swap and measure⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 고치려다 반대로 기울어요(과잉 교정) — 그래서 계속 재요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(110, 140, 1.0, talk=True)
         + note(170, 50, 190, 110, "⟦시험 문제집|TEST BOOK⟧", ("⟦이름 바꿔도 같은 답 ✓|same answer, new name ✓⟧", "⟦지역 바꿔도 같은 답 ✓|same answer, new region ✓⟧", "⟦성별 바꿔도 같은 답 ✓|same answer, new gender ✓⟧"), 0.95)
         + label(190, 240, "⟦재고, 줄여요|measure, then reduce⟧", 12, "var(--ink)")
         + parrot(490, 140, 1.0, color=PARROT_BAD, talk=True)
         + bubble_parrot(540, 50, 190, 44, "⟦사실까지 반대로 바꿔요|it flips even the facts⟧", 11, bad=True)
         + label(600, 180, "⟦이번엔 반대로 기울었어요|now it leans the other way⟧", 11, "var(--bad)")
         + label(570, 240, "⟦고치려다 생긴 새 치우침 = 과잉 교정|a new lean from the fix — over-correction⟧", 11, "var(--ink)")
         + label(380, 300, "⟦없앨 순 없어요 — 계속 재고, 중요한 결정은 사람이 해요|it never fully goes away — keep measuring, and a person decides what matters⟧", 12, "var(--ink)", cls="d"))

TEST_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 32 h20 M22 42 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 40 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
SWAP_I = icon(f'<circle cx="20" cy="22" r="9" fill="{SKIN}"/><rect x="11" y="33" width="18" height="14" rx="4" fill="#2E3D57"/><circle cx="44" cy="22" r="9" fill="{SKIN}"/><rect x="35" y="33" width="18" height="14" rx="4" fill="#7B3FA0"/><path d="M22 54 h20 M38 50 l4 4 l-4 4 M26 50 l-4 4 l4 4" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
HUMAN_I = icon(f'<circle cx="32" cy="20" r="10" fill="{SKIN}"/><rect x="20" y="32" width="24" height="20" rx="6" fill="var(--good)"/><path d="M46 14 l4 4 l8 -8" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
DIAL_I = icon('<circle cx="32" cy="34" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 L32 16" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="3" fill="var(--accent)"/><path d="M14 52 l-4 4 M50 52 l4 4" stroke="var(--muted)" stroke-width="2"/>')

PAGE = {
    "slug": "bias", "order": 38,
    "title": ("앵무새가 읽은 책의 치우침", "The Lean in the Parrot\'s Books"),
    "h1": ("<em>편향</em>이 뭐예요?", "What is <em>Bias</em>?"),
    "sub": ("AI 편향을, 앵무새가 읽은 책 더미가 한쪽으로 기울어 있으면 답도 그쪽으로 기우는 이야기로 풀어봤어요.",
            "AI bias, told as a story about a parrot whose book pile leans one way — so its answers lean the same way."),
    "panels": [
        {"svg": P1, "alt": ("손님이 의사와 간호사를 그려 달라고 하자 앵무새는 의사를 늘 같은 모습으로, 간호사를 늘 다른 모습으로 그림. 오른쪽엔 이름만 다른 이력서 두 장이 90점과 60점", "A guest asks for a doctor and a nurse; the parrot draws every doctor one way and every nurse the other. On the right, two resumes differing only by name score 90 and 60"),
         "caption": ("의사는 늘 같은 모습, 이름만 달라도 점수가 달라요.", "Every doctor looks the same; a different name gets a different score."),
         "small": ("앵무새 답이 어딘가 한쪽으로 기울어 있어요. 왜일까요?", "The parrot\'s answers lean one way. Why?")},
        {"svg": P2, "alt": ("한쪽으로 기운 책 더미가 눈 감은 앵무새로 이어지고, 쪽지에 '의사 = 아저씨 1000번, 아주머니 10번, 다음 콩: 아저씨'", "A leaning book pile leads to a parrot with eyes closed; a note counts doctor = a man 1000 times, a woman 10 times, next bean: a man"),
         "caption": ("앵무새는 제일 자주 이어진 콩을 골라요 — 책이 기울면 앵무새도 기울어요.", "The parrot picks the most frequent bean — leaning books make a leaning parrot."),
         "small": ('<a href="llm-ko.html">앵무새</a>는 읽은 책에서 제일 자주 본 것을 고르는 새예요. 책에 한쪽 이야기만 많으면, 그쪽 답만 나와요. 앵무새 잘못이 아니에요.',
                   'The <a href="llm-en.html">parrot</a> picks what it saw most in its books. If the books tell one side far more often, only that side comes out. It isn\'t the parrot\'s fault.')},
        {"svg": P3, "hero": True, "alt": ("기운 책 더미가 횃대 위 앵무새로 이어지고 앵무새는 '의사는 아저씨'라고 말함. 시험관이 보고 있고, 오른쪽 거울 속에도 같은 기운 책 더미", "A leaning book pile leads to the parrot on its perch saying a doctor is a man; an examiner watches; a mirror on the right shows the same leaning pile"),
         "caption": ("편향은 앵무새가 읽은 책의 치우침이 답에 그대로 나오는 거예요.", "Bias is the lean of the books coming straight out in the answers."),
         "small": ("앵무새 잘못이 아니라, 책과 우리의 거울이에요. 책은 사람이 썼으니까요. 그래서 없애기보다 재고, 줄이고, 중요한 건 사람이 봐요.",
                   "Not the parrot\'s fault — it mirrors the books, and us, because people wrote them. So instead of erasing it, we measure it, reduce it, and let a person look at what matters."),
         "tricks": (4, [
             (TEST_I, ("문제집에 넣어요", "Put it in the test book"), ("치우침 문항으로 재요", "questions that measure the lean"), "calm"),
             (SWAP_I, ("이름만 바꿔 봐요", "Swap just the name"), ("성별·지역도 — 같은 답이어야 해요", "gender, region too — same answer expected"), "calm"),
             (HUMAN_I, ("중요한 결정은 사람이", "People decide what matters"), ("채용·대출·진료", "hiring, loans, care"), "warm"),
             (DIAL_I, ("예절 교육으로 줄여요", "Manners lessons reduce it"), ("줄이지만 없애진 못해요", "less, never zero"), "warm"),
         ])},
        {"svg": P4, "alt": ("이름만 다른 이력서 두 장이 앵무새로 들어가 90점과 60점으로 나오고, 시험관이 채점표에 '이름만 바꿈, 점수 차이 ×'라고 표시", "Two resumes differing only by name go into the parrot and come out as 90 and 60; an examiner marks name swapped, score gap × on the score sheet"),
         "caption": ("같은 이력서에 이름만 바꿔 넣어 보고, 점수가 다르면 표시해요.", "Feed the same resume with only the name changed; if the score moves, flag it."),
         "small": ('이름·성별·지역 하나만 바꾸고 나머지는 똑같이 — 답이 달라지면 치우친 거예요. <a href="evaluation-ko.html">시험관의 채점표</a>에 이런 문항을 넣어 두고 계속 재요.',
                   'Change one thing — name, gender, region — and keep everything else the same. If the answer changes, it leans. The <a href="evaluation-en.html">examiner\'s score sheet</a> keeps such questions and measures them again and again.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새와 '이름·지역·성별 바꿔도 같은 답 ✓' 시험 문제집. 오른쪽 빨강: 빨간 앵무새가 '사실까지 반대로 바꿔요' — 과잉 교정", "Left, green: the parrot with a test book marked same answer when name, region, gender are swapped. Right, red: a red parrot flips even the facts — over-correction"),
         "caption": ("고치려다 반대로 기울기도 해요. 그래서 없애는 게 아니라 계속 재요.", "Fixing it can tip it the other way. So we keep measuring rather than declaring it gone."),
         "small": ('<a href="alignment-ko.html">예절 교육</a>은 치우침을 줄이지만 지나치면 사실까지 바꿔요(과잉 교정). 그래서 채용·대출 같은 중요한 결정은 <a href="humanloop-ko.html">마지막을 사람이</a> 봐요.',
                   '<a href="alignment-en.html">Manners lessons</a> reduce the lean, but too much and it bends the facts (over-correction). That is why hiring, loans and the like end with <a href="humanloop-en.html">a person looking last</a>.')},
    ],
    "summary": (("<b>편향</b> = 앵무새가 <b>읽은 책의 치우침</b>이 답에 <b>그대로 나오는 것</b>. 앵무새 잘못이 아니라 책과 우리의 거울이라, 없애기보다 <b>계속 재고</b> 중요한 결정은 사람이 해요.",
                 "<b>Bias</b> = the <b>lean of the books</b> the parrot read <b>coming straight out</b> in its answers. It mirrors the books and us rather than being the parrot\'s fault, so we <b>keep measuring</b> and let people make the decisions that matter."),
                ("Bias. 학습 데이터의 분포가 특정 집단·관점으로 치우쳐 있으면 모델 출력도 그 방향으로 치우쳐요. 반사실 테스트(이름·성별·지역만 바꾸기)와 공정성 벤치마크로 재고, 정렬(RLHF 등)로 줄이되 과잉 교정을 조심해요. 고위험 결정에는 사람 확인이 필수예요.",
                 "When the training data\'s distribution skews toward certain groups or views, the model\'s output skews the same way. It is measured with counterfactual tests (change only the name, gender or region) and fairness benchmarks, reduced through alignment (RLHF and the like) while watching for over-correction, and high-stakes decisions require a human check.")),
    "glossary": [
        ("편향", "Bias", ("읽은 책의 치우침.", "The lean in the books."), ("답에 그대로 나와요. 앵무새 잘못이 아니라 거울이에요.", "It comes straight out in the answers — a mirror, not the parrot\'s fault.")),
        ("학습 데이터 편향", "Training data bias", ("책 더미가 한쪽으로 기움.", "The pile leans one way."), ('한쪽 이야기가 훨씬 많아서 그쪽만 나와요. 책 더미 자체는 → <a href="pretraining-ko.html">책 읽는 학교</a>', 'One side appears far more often, so only that side comes out. The pile itself: → <a href="pretraining-en.html">the reading school</a>')),
        ("공정성 평가", "Fairness evaluation", ("시험 문제집의 치우침 문항.", "The lean questions in the test book."), ('집단별로 답이 다른지 재요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Measures whether answers differ by group. → <a href="evaluation-en.html">the examiner\'s score sheet</a>')),
        ("반사실 테스트", "Counterfactual test", ("이름만 바꿔 보기.", "Swap just the name."), ("이름·성별·지역 하나만 바꾸고 답이 같은지 봐요.", "Change one thing — name, gender, region — and see if the answer stays the same.")),
        ("대표성", "Representation", ("책에 모두가 골고루 있나.", "Is everyone in the books evenly?"), ("적게 나온 집단은 앵무새가 잘 모르거나 한 가지 모습으로만 그려요.", "Groups that appear rarely the parrot knows poorly, or draws one way only.")),
        ("과잉 교정", "Over-correction", ("고치려다 반대로 기움.", "Tipping the other way while fixing."), ("사실까지 바꿔 말하게 돼요. 그래서 고친 뒤에도 다시 재요.", "It starts bending facts. So after a fix, measure again.")),
        ("정렬", "Alignment", ("앵무새 예절 교육.", "The parrot\'s manners lessons."), ('치우침을 줄이지만 없애진 못해요. → <a href="alignment-ko.html">앵무새 예절 교육</a>', 'Reduces the lean, never removes it. → <a href="alignment-en.html">the parrot\'s manners lessons</a>')),
        ("사람 확인", "Human review", ("중요한 결정은 사람이.", "A person decides what matters."), ('채용·대출·진료는 앵무새 답으로 끝내지 않아요. → <a href="humanloop-ko.html">마지막은 사람이</a>', 'Hiring, loans and care never end on the parrot\'s answer. → <a href="humanloop-en.html">a person goes last</a>')),
    ],
}
