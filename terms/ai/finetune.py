from _draw import *
from _world import *

# 1. 앵무새가 우리 집 말투·용어를 몰라요 — '정산'을 다르게 써요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, mood="sweat", talk=True)
         + bubble_parrot(60, 20, 290, 44, "⟦정산… 산을 정리하는 거요?|settle… like settling down?⟧", 12)
         + person(520, 120, s=0.9, face=FROWN, **GUEST) + bubble(420, 30, 280, 40, "⟦우리 식으로 정산표 써 줘|write our settlement sheet, our way⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + note(600, 190, 130, 70, "⟦우리 집 말|OUR WORDS⟧", ("⟦정산 = 월말 돈 맞추기|settle = month-end tally⟧",), 0.9)
         + label(380, 282, "⟦책엔 세상 말이 다 있지만, 우리 집 말은 없어요|the books have the whole world\'s words — but not our house\'s⟧", 13, "var(--ink)"))

# 2. 매번 쪽지에 길게 적기 vs 한 번 특훈 — 그런데 특훈은 책을 다시 읽히는 게 아니에요
P2 = svg(320, '<rect width="253" height="320" fill="var(--accent-soft)"/><rect x="253" width="253" height="320" fill="var(--good-soft)"/><rect x="506" width="254" height="320" fill="var(--bad-soft)"/>'
         + label(126, 30, "⟦매번 쪽지에 길게|a long note, every time⟧", 13, "var(--ink)", cls="d")
         + note(40, 48, 170, 130, "⟦오늘도 쪽지|TODAY\'S NOTE⟧", ("⟦우리 말투는…|our tone is…⟧", "⟦정산이란…|settle means…⟧", "⟦표 모양은…|the sheet looks…⟧", "⟦예시 1, 2, 3…|examples 1, 2, 3…⟧"), 0.95)
         + "".join(bean(50 + i * 26, 212 - (i % 2) * 6, 0.8) for i in range(6))
         + label(126, 250, "⟦콩이 매번 많이 들어요|costs many beans, every time⟧", 11, "var(--muted)")
         + label(380, 30, "⟦한 번 특훈|one drill⟧", 13, "var(--ink)", cls="d")
         + person(280, 80, s=0.8, face=SMILE, **TRAINER) + parrot(400, 150, 1.0) + note(430, 60, 70, 50, "⟦특훈|DRILL⟧", ("⟦정산 ✓|settle ✓⟧",), 0.9)
         + label(380, 250, "⟦한 번 배우면 기억해요|learns once, remembers⟧", 11, "var(--muted)")
         + label(633, 30, "⟦책을 다시 읽혀요?|read it all again?⟧", 13, "var(--ink)", cls="d")
         + books(633, 200, 6, 1.0) + label(633, 175, "⟦×|×⟧", 64, "var(--bad)", cls="d")
         + label(633, 250, "⟦아니요 — 특훈은 다시 읽기가 아니에요|no — a drill is not re-reading⟧", 10, "var(--bad)")
         + label(380, 300, "⟦쪽지는 매번, 특훈은 한 번 — 그런데 특훈은 책 산더미와 달라요|the note is every time, the drill is once — and a drill is not the mountain of books⟧", 11, "var(--ink)"))

# 3. 파인튜닝 = 다 읽은 앵무새에게 우리 예시 몇백 장으로 시키는 짧은 특훈 (hero)
CARDS = "".join(note(60 + i * 5, 110 - i * 6, 110, 70, "⟦예시|EXAMPLE⟧", ("⟦정산 → 정산표|settle → sheet⟧",), 0.9) for i in range(4))
P3 = svg(360, sky(360)
         + CARDS + label(100, 190, "⟦우리 예시 몇백 장|a few hundred of our examples⟧", 11, "var(--muted)")
         + person(200, 110, s=0.9, face=SMILE, **TRAINER) + label(232, 240, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + '<path d="M275 160 L318 160" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M310 152 L322 160 L310 168" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + perch(400, 240, 150) + parrot(400, 200, 1.3, talk=True)
         + bubble_parrot(290, 40, 230, 44, "⟦정산표, 우리 식으로요!|settlement sheet, our way!⟧", 12)
         + person(560, 130, s=0.9, face=SMILE, **EXAMINER) + label(595, 262, "⟦특훈 뒤 시험|test after the drill⟧", 11, "var(--muted)")
         + note(630, 40, 110, 90, "⟦시험|TEST⟧", ("⟦정산 ✓|settle ✓⟧", "⟦말투 ✓|tone ✓⟧"), 0.95)
         + label(380, 340, "⟦파인튜닝 = 다 읽은 앵무새에게 우리 예시 몇백 장으로 시키는 짧은 특훈|fine-tuning is a short drill for a well-read parrot, using a few hundred of our examples⟧", 13, "var(--ink)", cls="d"))

# 4. 특훈 종류표 — 따라 하기(SFT), 간식으로 고치기(RLHF), 작은 딱지(LoRA)
ROWS = (("⟦예시 따라 하기|copy the examples⟧", "⟦예시 카드를 보고 똑같이 말해요|says it just like the example card⟧", "var(--accent)"),
        ("⟦간식으로 고치기|fix with treats⟧", "⟦두 답 중 더 좋은 쪽에 간식을 줘요|a treat for the better of two answers⟧", "var(--good)"),
        ("⟦작은 딱지 특훈|small sticker drill⟧", "⟦앵무새 전체 말고 딱지만 바꿔요|changes only a sticker, not the whole bird⟧", "#5B8DEF"))
P4 = svg(320, sky(320)
         + '<rect x="30" y="30" width="480" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="480" height="30" rx="8" fill="#C9A86A"/>' + label(270, 50, "⟦특훈 종류|KINDS OF DRILL⟧", 13, "#142033", cls="d")
         + "".join(f'<circle cx="60" cy="{100 + i * 56}" r="9" fill="{c}"/>' + label(80, 105 + i * 56, t, 13, "#142033", "start", cls="d") + label(80, 127 + i * 56, d, 11, "#142033", "start") for i, (t, d, c) in enumerate(ROWS))
         + parrot(600, 150, 1.1) + '<rect x="606" y="146" width="24" height="16" rx="3" fill="#5B8DEF" stroke="#FFF8E7" stroke-width="2"/>' + label(618, 158, "⟦L|L⟧", 10, "#FFF8E7", cls="d")
         + label(650, 130, "⟦딱지|sticker⟧", 10, "var(--muted)")
         + bean(690, 200, 1.0) + label(690, 226, "⟦간식|treat⟧", 10, "var(--muted)")
         + note(560, 40, 100, 60, "⟦예시|EXAMPLE⟧", ("⟦정산 → 정산표|settle → sheet⟧",), 0.9)
         + label(380, 300, "⟦특훈에도 종류가 있어요 — 따라 하기, 간식, 작은 딱지|drills come in kinds — copying, treats, a small sticker⟧", 12, "var(--muted)"))

# 5. 과하면 예시만 외우고 다른 걸 잊어요 + 순서: 쪽지 → 사서 → 특훈
ARROW = '<path d="M{0} 140 L{1} 140" stroke="var(--muted)" stroke-width="3"/><path d="M{2} 132 L{1} 140 L{2} 148" stroke="var(--muted)" stroke-width="3" fill="none"/>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(40, 100, s=0.8, face=EYES, **GUEST) + bubble(20, 30, 160, 36, "⟦오늘 날씨 어때?|weather today?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + parrot(250, 150, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(200, 40, 150, 36, "⟦정산표!|settlement sheet!⟧", 12, bad=True)
         + label(190, 240, "⟦예시만 외우고 다른 걸 잊었어요|memorized the examples, forgot the rest⟧", 11, "var(--ink)")
         + label(190, 262, "⟦특훈이 너무 과하면|when the drill goes too far⟧", 11, "var(--bad)")
         + note(400, 110, 70, 60, "⟦1|1⟧", ("⟦쪽지|note⟧",), 0.9) + ARROW.format(470, 495, 487)
         + person(500, 95, s=0.8, face=SMILE, **LIBRARIAN) + label(528, 210, "⟦2 사서|2 librarian⟧", 11, "var(--ink)")
         + ARROW.format(560, 585, 577)
         + person(590, 95, s=0.8, face=SMILE, **TRAINER) + parrot(690, 160, 0.7) + label(660, 210, "⟦3 특훈|3 drill⟧", 11, "var(--ink)")
         + label(433, 210, "⟦1 쪽지|1 note⟧", 11, "var(--ink)")
         + label(570, 250, "⟦쪽지 먼저, 그다음 사서, 특훈은 맨 마지막|note first, then the librarian, the drill last⟧", 11, "var(--ink)")
         + label(380, 300, "⟦과하면 잊어요 — 그리고 특훈은 맨 마지막 카드예요|too much and it forgets — and the drill is the last card to play⟧", 12, "var(--ink)", cls="d"))

CARDS_I = icon('<rect x="18" y="20" width="36" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="14" width="36" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="14" width="36" height="9" rx="3" fill="#C9A86A"/><path d="M18 32 h20 M18 39 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
TONE_I = icon('<path d="M8 12 h48 v30 h-30 l-10 10 v-10 h-8z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M20 22 h24 M20 31 h16" stroke="var(--ink)" stroke-width="2.5" stroke-linecap="round"/><path d="M40 28 l5 5 l9 -10" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BOOKX_I = icon('<rect x="10" y="40" width="34" height="8" rx="2" fill="#7B3FA0"/><rect x="14" y="30" width="34" height="8" rx="2" fill="#2E7D6B"/><rect x="10" y="20" width="34" height="8" rx="2" fill="#C9822B"/><path d="M42 12 l14 14 M56 12 l-14 14" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
TEST_I = icon(f'<circle cx="24" cy="22" r="10" fill="{SKIN}"/><path d="M12 18 Q24 6 36 18 Z" fill="#E9B44C"/><rect x="14" y="34" width="20" height="18" rx="5" fill="#4A5A72"/><rect x="38" y="24" width="20" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M42 34 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "finetune", "order": 6,
    "title": ("짧은 특훈", "The Short Drill"),
    "h1": ("<em>파인튜닝</em>이 뭐예요?", "What is <em>Fine-tuning</em>?"),
    "sub": ("파인튜닝을 책을 다 읽은 앵무새에게 우리 집 예시 몇백 장으로 시키는 짧은 특훈 이야기로 풀어봤어요.",
            "Fine-tuning, told as a story about a short drill for a well-read parrot, using a few hundred of our own examples."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 앵무새가 '정산… 산을 정리하는 거요?'라고 하고, 손님은 '우리 식으로 정산표 써 줘'라고 부탁함. '우리 집 말' 쪽지: 정산 = 월말 돈 맞추기", "A sweating parrot says settle… like settling down?; a guest asks for our settlement sheet, our way. An OUR WORDS note reads settle = month-end tally"),
         "caption": ("앵무새는 우리 집 말투와 용어를 몰라요. '정산'을 우리와 다르게 써요.", "The parrot doesn\'t know our house\'s tone or words. It uses settle differently than we do."),
         "small": ('<a href="llm-ko.html">책 산더미</a>엔 세상 말이 다 있지만, 우리 집에서만 쓰는 말과 표 모양은 없어요.', 'The <a href="llm-en.html">mountain of books</a> has the whole world\'s words — but not the words and sheet shapes only our house uses.')},
        {"svg": P2, "alt": ("세 칸: 주황 — 매일 긴 쪽지와 콩 여섯 개(콩이 매번 많이 듦). 초록 — 조련사가 '정산 ✓' 특훈 쪽지로 앵무새를 가르침(한 번 배우면 기억). 빨강 — 책 더미 위에 큰 ×", "Three columns: orange — a long note every day with six beans (many beans each time); green — a trainer drills the parrot with a settle ✓ note (learns once); red — a big × over the book pile"),
         "caption": ("매번 쪽지에 길게 적거나, 한 번 특훈을 시켜요. 그런데 특훈은 책을 다시 읽히는 게 아니에요.", "Either write a long note every time, or drill it once. But a drill is not re-reading the books."),
         "small": ('긴 <a href="prompt-ko.html">쪽지</a>는 매번 콩이 많이 들어요. 특훈은 한 번이면 돼요 — 책 산더미를 다시 읽는 게 아니라, 다 읽은 새에게 예시 몇백 장을 보여 주는 거예요.',
                   'A long <a href="prompt-en.html">note</a> costs many beans every time. A drill takes once — not re-reading the mountain of books, but showing a well-read bird a few hundred examples.')},
        {"svg": P3, "hero": True, "alt": ("'예시: 정산 → 정산표' 카드 더미와 조련사, 화살표 뒤 횃대의 앵무새가 '정산표, 우리 식으로요!'라고 말함. 시험관이 '정산 ✓ 말투 ✓' 시험지를 듦", "A stack of EXAMPLE cards (settle → sheet) and a trainer; past an arrow, the parrot on a perch says settlement sheet, our way!; an examiner holds a TEST note with settle ✓ and tone ✓"),
         "caption": ("파인튜닝은 다 읽은 앵무새에게 우리 예시 몇백 장으로 시키는 짧은 특훈이에요.", "Fine-tuning is a short drill for a well-read parrot, using a few hundred of our examples."),
         "small": ('재료는 예시예요 — 수백에서 수천 장. 말투와 표 모양은 잘 배워요. 새 지식은 잘 못 들어가요 — 그건 사서가 찾아 <a href="context-ko.html">쟁반</a>에 올리는 쪽(RAG)이 나아요. 특훈이 끝나면 시험을 봐요.',
                   'The ingredient is examples — hundreds to thousands. It learns tone and sheet shapes well. New knowledge doesn\'t stick — the librarian putting pages on the <a href="context-en.html">tray</a> (RAG) works better for that. After the drill comes a test.'),
         "tricks": (4, [
             (CARDS_I, ("예시가 재료예요", "Examples are the ingredient"), ("수백~수천 장", "hundreds to thousands"), "calm"),
             (TONE_I, ("말투·형식엔 잘 들어요", "Great for tone and format"), ("우리 집 말, 우리 표", "our words, our sheets"), "calm"),
             (BOOKX_I, ("새 지식엔 약해요", "Weak for new facts"), ("그건 사서에게", "leave that to the librarian"), "warm"),
             (TEST_I, ("특훈 뒤엔 시험", "Test after the drill"), ("잘 됐나 시험관이 재요", "the examiner measures it")),
         ])},
        {"svg": P4, "alt": ("'특훈 종류' 표: 예시 따라 하기(예시 카드를 보고 똑같이), 간식으로 고치기(두 답 중 더 좋은 쪽에 간식), 작은 딱지 특훈(딱지만 바꿈). 옆에 파란 딱지 L 이 붙은 앵무새, 간식 콩, 예시 카드", "A KINDS OF DRILL table: copy the examples (says it like the card); fix with treats (a treat for the better of two answers); small sticker drill (changes only a sticker). Beside it a parrot with a blue L sticker, a treat bean, an example card"),
         "caption": ("특훈에도 종류가 있어요. 따라 하기, 간식으로 고치기, 작은 딱지만 바꾸기.", "Drills come in kinds: copying examples, fixing with treats, changing only a small sticker."),
         "small": ("따라 하기가 기본이에요. 간식은 두 답 중 더 좋은 쪽을 고르게 해요. 작은 딱지는 앵무새 전체를 바꾸지 않아서 싸고 빨라요.", "Copying is the basic one. Treats teach it to pick the better of two answers. The small sticker doesn\'t change the whole bird, so it\'s cheap and fast.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 손님이 '오늘 날씨 어때?'라고 묻는데 빨간 앵무새가 '정산표!'라고 답함. 오른쪽 초록: 1 쪽지 → 2 사서 → 3 특훈(조련사와 작은 앵무새) 순서", "Left, red: a guest asks about today\'s weather and the red parrot answers settlement sheet!. Right, green: the order 1 note → 2 librarian → 3 drill (trainer and a small parrot)"),
         "caption": ("특훈이 과하면 예시만 외우고 다른 걸 잊어요. 그리고 특훈은 맨 마지막 카드예요.", "Too much drill and it memorizes the examples and forgets the rest. And the drill is the last card to play."),
         "small": ('먼저 <a href="prompt-ko.html">쪽지</a>로 시켜 보고, 부족하면 사서가 <a href="context-ko.html">쟁반</a>에 페이지를 올리고, 그래도 안 되면 특훈이에요. 지어내는 버릇은 특훈으로도 다 못 고쳐요 — <a href="hallucination-ko.html">그럴듯 앵무새</a> 이야기예요.',
                   'Try the <a href="prompt-en.html">note</a> first; if that falls short, the librarian puts pages on the <a href="context-en.html">tray</a>; only then the drill. Even a drill can\'t fully cure making things up — that\'s the <a href="hallucination-en.html">plausible parrot</a> story.')},
    ],
    "summary": (("<b>파인튜닝</b> = 책을 다 읽은 앵무새에게 <b>우리 예시 몇백 장</b>으로 시키는 <b>짧은 특훈</b>. 말투와 형식은 잘 배우고, 새 지식은 사서(RAG)가 나아요. 과하면 예시만 외우니 특훈 뒤엔 시험을 봐요. 순서는 쪽지 → 사서 → 특훈.",
                 "<b>Fine-tuning</b> = a <b>short drill</b> for a well-read parrot using <b>a few hundred of our examples</b>. It learns tone and format well; new knowledge is better left to the librarian (RAG). Too much and it only memorizes, so test after the drill. Order: note, librarian, drill."),
                ("Fine-tuning. 사전 학습이 끝난 모델을 소규모 라벨 데이터(수백~수천 예시)로 추가 학습해 말투·형식·작업 방식을 맞추는 거예요. SFT(지도 미세조정)가 기본, RLHF 는 선호 비교로 보상을 주고, LoRA 는 작은 어댑터만 학습해 싸고 빨라요. 과적합·파국적 망각을 막으려면 평가 세트로 검증하고, 프롬프트 → RAG → 파인튜닝 순으로 시도해요.",
                 "Additional training of a pre-trained model on a small labeled set (hundreds to thousands of examples) to match tone, format and task behavior. SFT (supervised fine-tuning) is the base; RLHF rewards preferred answers from pairwise comparisons; LoRA trains only small adapters, making it cheap and fast. Validate on an evaluation set to catch overfitting and catastrophic forgetting, and try prompt, then RAG, then fine-tuning, in that order.")),
    "glossary": [
        ("파인튜닝", "Fine-tuning", ("짧은 특훈.", "The short drill."), ("다 읽은 앵무새에게 우리 예시로 말버릇과 형식을 가르쳐요.", "Teaches a well-read parrot our manners and formats using our examples.")),
        ("SFT", "Supervised fine-tuning", ("예시 따라 하기.", "Copying the examples."), ("질문과 정답 카드를 보여 주고 똑같이 말하게 해요. 제일 기본 특훈이에요.", "Show question-and-answer cards and have it say the same. The most basic drill.")),
        ("RLHF", "Reinforcement learning from human feedback", ("간식으로 고치기.", "Fixing with treats."), ("두 답 중 사람이 더 좋아한 쪽에 간식을 줘요. 존댓말, 안전한 답이 여기서 나와요.", "A treat for whichever of two answers people liked more. Politeness and safe answers come from here.")),
        ("LoRA", "Low-rank adaptation", ("작은 딱지 특훈.", "The small sticker drill."), ("앵무새 전체가 아니라 작은 딱지만 바꿔요. 싸고 빠르고, 딱지를 떼면 원래 새로 돌아가요.", "Changes a small sticker instead of the whole bird. Cheap, fast, and peel it off to get the original bird back.")),
        ("과적합", "Overfitting", ("예시만 외우기.", "Memorizing only the examples."), ("특훈이 과하면 예시 카드는 완벽한데 새 질문엔 엉뚱해요.", "Too much drill: perfect on the example cards, lost on new questions.")),
        ("파국적 망각", "Catastrophic forgetting", ("특훈하다 다른 걸 잊기.", "Forgetting the rest while drilling."), ("정산표만 파다가 날씨 얘기를 못 하게 돼요. 예시를 섞고 특훈을 짧게 해요.", "Drill only settlement sheets and it can\'t talk about weather anymore. Mix examples and keep the drill short.")),
        ("평가 세트", "Evaluation set", ("특훈 뒤 시험지.", "The test after the drill."), ("특훈에 안 쓴 예시로 시험관이 재요. 특훈에 쓴 카드로 시험 보면 반칙이에요.", "The examiner measures with examples not used in the drill. Testing with drill cards is cheating.")),
        ("프롬프트 vs 파인튜닝", "Prompt vs fine-tuning", ("매번 쪽지 vs 한 번 특훈.", "A note every time vs a drill once."), ('쪽지가 먼저예요 — 싸고 바로 돼요. → <a href="prompt-ko.html">앵무새에게 주는 조련 쪽지</a>', 'The note comes first — cheap and instant. → <a href="prompt-en.html">the trainer\'s note</a>')),
    ],
}
