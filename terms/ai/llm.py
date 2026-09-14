from _draw import *
from _world import *

# 1. 손님이 앵무새에게 뭘 물어도 대답이 나와요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, talk=True)
         + bubble_parrot(110, 30, 200, 40, "⟦파리는 프랑스의 수도예요|Paris is the capital of France⟧", 12)
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(430, 30, 260, 40, "⟦프랑스 수도가 어디야? …시도 써 줘|capital of France? …and write me a poem⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦뭘 물어도 말이 되는 대답이 나와요 — 어떻게?|ask anything, and a sensible answer comes out — how?⟧", 13, "var(--ink)"))

# 2. 앵무새는 뜻을 아는 게 아니라 다음 말을 이어 붙여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, mood="think") + label(110, 240, "⟦생각하는 게 아니라|not thinking —⟧", 12, "var(--muted)")
         + beans(260, 120, ("⟦오늘|Today⟧", "⟦날씨가|the⟧", "⟦참|weather⟧", "⟦…|is⟧"), 1.0, 60)
         + '<rect x="470" y="98" width="52" height="44" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(496, 126, "⟦?|?⟧", 22, "var(--accent)", cls="d")
         + note(560, 60, 170, 130, "⟦다음 콩 후보|NEXT BEAN⟧", ("⟦좋다  ★★★★|nice   ★★★★⟧", "⟦춥다  ★★|cold   ★★⟧", "⟦바나나 ☆|banana ☆⟧"), 1.0, 0)
         + label(400, 200, "⟦읽은 책에서 제일 자주 이어졌던 콩을 고르고, 또 고르고|it picks the bean that most often came next in its books — again and again⟧", 12, "var(--ink)")
         + label(380, 282, "⟦앵무새는 다음 말을 잘 이어 붙이는 새예요 — 뜻을 아는 새가 아니라|the parrot is a bird that continues sentences well — not one that understands them⟧", 12, "var(--bad)"))

# 3. LLM = 책을 산더미로 읽은 앵무새 (hero)
P3 = svg(360, sky(360)
         + books(120, 300, 6, 1.2) + label(120, 322, "⟦마을 도서관보다 많은 책|more books than the village library⟧", 11, "var(--muted)")
         + '<path d="M200 220 L250 200" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M240 196 L254 198 L246 208" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + perch(340, 240, 150) + parrot(340, 200, 1.4, talk=True)
         + "".join(bean(300 + i * 26, 90 - (i % 2) * 8, 0.8) for i in range(5))
         + label(360, 60, "⟦콩 하나씩, 한 번에 한 콩|one bean at a time⟧", 11, "var(--muted)")
         + person(540, 130, s=0.9, face=SMILE, **TRAINER) + label(575, 262, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + note(600, 40, 140, 80, "⟦읽은 것|WHAT IT READ⟧", ("⟦백과사전, 소설,|encyclopedias, novels,⟧", "⟦편지, 코드…|letters, code…⟧"), 0.95)
         + label(380, 340, "⟦LLM = 책을 산더미로 읽고, 다음 콩을 잘 고르게 된 앵무새|an LLM is a parrot that read a mountain of books and got very good at picking the next bean⟧", 13, "var(--ink)", cls="d"))

# 4. 크기와 훈련: 큰 앵무새, 작은 앵무새, 특훈
P4 = svg(320, sky(320)
         + parrot(120, 150, 1.5, color=PARROT_BIG) + label(120, 240, "⟦큰 앵무새|big parrot⟧", 13, "var(--ink)", cls="d") + label(120, 262, "⟦더 많이 알고, 더 느리고, 더 비싸요|knows more, slower, pricier⟧", 11, "var(--muted)")
         + parrot(300, 165, 0.8) + label(300, 240, "⟦작은 앵무새|small parrot⟧", 13, "var(--ink)", cls="d") + label(300, 262, "⟦빠르고 싸요, 가끔 모자라요|fast and cheap, sometimes short⟧", 11, "var(--muted)")
         + '<rect x="420" y="60" width="300" height="180" rx="8" fill="var(--good-soft)"/>'
         + parrot(500, 150, 1.0) + person(600, 100, s=0.8, face=SMILE, **TRAINER) + note(640, 170, 80, 60, "⟦특훈|DRILL⟧", ("⟦존댓말|be polite⟧",), 0.9)
         + label(570, 262, "⟦읽기가 끝난 뒤, 짧은 특훈으로 말버릇을 고쳐요|after the reading, a short drill fixes its manners⟧", 11, "var(--ink)")
         + label(380, 300, "⟦앵무새 크기는 파라미터, 특훈은 파인튜닝·RLHF|size is parameters; the drill is fine-tuning and RLHF⟧", 11, "var(--muted)"))

# 5. 잘하는 것, 못하는 것 — 비유가 깨지는 곳
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(110, 140, 1.0, talk=True) + note(170, 60, 180, 110, "⟦잘해요|GOOD AT⟧", ("⟦요약, 번역, 초안 쓰기|summarizing, translating, drafts⟧", "⟦코드 고치기, 말투 바꾸기|fixing code, changing tone⟧", "⟦읽은 게 많은 일|anything it read a lot about⟧"), 0.95)
         + label(190, 240, "⟦사람보다 빠르고, 어떤 건 더 잘해요|faster than people, and sometimes better⟧", 11, "var(--ink)")
         + parrot(490, 140, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(540, 50, 190, 40, "⟦그 책은 1987년에 나왔어요|that book came out in 1987⟧", 11, bad=True)
         + label(560, 180, "⟦(그런 책은 없어요)|(no such book exists)⟧", 11, "var(--bad)")
         + label(570, 240, "⟦모르는 것도 자신 있게 이어 붙여요|it continues just as confidently when it doesn\'t know⟧", 11, "var(--ink)")
         + label(380, 300, "⟦그래서 앵무새 답은 '초안'이에요 — 확인은 사람이 해요|so a parrot\'s answer is a draft — a person checks it⟧", 12, "var(--ink)", cls="d"))

BOOK_I = icon('<rect x="12" y="40" width="40" height="8" rx="2" fill="#7B3FA0"/><rect x="16" y="30" width="40" height="8" rx="2" fill="#2E7D6B"/><rect x="12" y="20" width="40" height="8" rx="2" fill="#C9822B"/><rect x="16" y="10" width="40" height="8" rx="2" fill="#5B8DEF"/>')
BEAN_I = icon(f'<ellipse cx="20" cy="36" rx="12" ry="8" fill="{BEAN}"/><ellipse cx="44" cy="28" rx="12" ry="8" fill="{BEAN}"/><path d="M50 14 l6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><text x="32" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="var(--accent)">?</text>')
DRAFT_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M38 44 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none"/>')
CHECK_I = icon(f'<circle cx="24" cy="24" r="10" fill="{SKIN}"/><rect x="14" y="36" width="20" height="16" rx="5" fill="var(--good)"/><circle cx="46" cy="40" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M53 47 l6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "llm", "order": 1,
    "title": ("책을 산더미로 읽은 앵무새", "The Parrot That Read a Mountain of Books"),
    "h1": ("<em>LLM</em>이 뭐예요?", "What is an <em>LLM</em>?"),
    "sub": ("LLM(대규모 언어 모델)을 책을 산더미로 읽고 다음 말을 잘 이어 붙이게 된 앵무새 이야기로 풀어봤어요.",
            "Large language models, told as a story about a parrot that read a mountain of books and learned to continue any sentence."),
    "panels": [
        {"svg": P1, "alt": ("횃대 위 파란 앵무새가 '파리는 프랑스의 수도예요'라고 말하고, 손님은 '프랑스 수도가 어디야? 시도 써 줘'라고 물음", "A blue parrot on a perch says Paris is the capital of France; a guest asks the capital of France, and for a poem"),
         "caption": ("앵무새에게 뭘 물어도 말이 되는 대답이 나와요.", "Ask the parrot anything, and a sensible answer comes out."),
         "small": ("수도도 알고, 시도 쓰고, 코드도 고쳐요. 어떻게 하는 걸까요?", "It knows capitals, writes poems, fixes code. How?")},
        {"svg": P2, "alt": ("눈을 감은 앵무새, '오늘 날씨가 참 …' 콩 네 개와 물음표, '다음 콩 후보' 쪽지에 좋다 ★★★★, 춥다 ★★, 바나나 ☆", "A parrot with eyes closed; four beans reading Today the weather is … and a question mark; a note ranks next beans: nice ★★★★, cold ★★, banana ☆"),
         "caption": ("앵무새는 뜻을 아는 게 아니라, 다음 말을 이어 붙여요.", "The parrot doesn\'t understand — it continues the sentence."),
         "small": ("읽은 책에서 제일 자주 이어졌던 말 조각을 고르고, 또 고르고, 또 골라요. 그게 문장이 돼요.", "It picks the word piece that most often came next in its books — again, and again, and again. That becomes a sentence.")},
        {"svg": P3, "hero": True, "alt": ("마을 도서관보다 큰 책 더미가 앵무새로 이어지고, 앵무새가 콩을 하나씩 말함. 조련사와 '읽은 것: 백과사전, 소설, 편지, 코드' 쪽지", "A book pile bigger than the village library leads to the parrot, which says beans one at a time; a trainer and a note listing what it read: encyclopedias, novels, letters, code"),
         "caption": ("LLM은 책을 산더미로 읽고, 다음 콩을 잘 고르게 된 앵무새예요.", "An LLM is a parrot that read a mountain of books and got very good at picking the next bean."),
         "small": ('백과사전, 소설, 편지, 코드까지 읽었어요. 그래서 어떤 말이 와도 다음 말을 이어요 — <a href="token-ko.html">콩</a> 하나씩, 한 번에 한 콩.',
                   'It read encyclopedias, novels, letters, even code. So whatever you say, it can continue — one <a href="token-en.html">bean</a> at a time.'),
         "tricks": (4, [
             (BOOK_I, ("읽은 만큼 알아요", "Knows what it read"), ("책에 없던 건 몰라요", "not what wasn\'t in the books"), "calm"),
             (BEAN_I, ("한 콩씩 이어요", "One bean at a time"), ("생각이 아니라 이어 붙이기", "continuing, not thinking")),
             (DRAFT_I, ("답은 초안", "Answers are drafts"), ("빠르고 그럴듯해요", "fast and plausible"), "warm"),
             (CHECK_I, ("확인은 사람이", "A person checks"), ("특히 이름·숫자·날짜", "names, numbers, dates most"), "warm"),
         ])},
        {"svg": P4, "alt": ("큰 앵무새(더 많이 알고 느리고 비쌈)와 작은 앵무새(빠르고 쌈), 오른쪽엔 조련사가 '존댓말' 특훈 쪽지로 앵무새를 가르침", "A big parrot (knows more, slower, pricier) and a small one (fast, cheap); on the right a trainer drills the parrot with a be-polite note"),
         "caption": ("앵무새는 크기가 다르고, 읽기가 끝난 뒤 특훈을 받아요.", "Parrots come in sizes, and after the reading they get a short drill."),
         "small": ("큰 앵무새는 더 많이 알지만 느리고 비싸요. 특훈은 말버릇을 고쳐요 — 존댓말, 모르면 모른다고 하기.", "A big parrot knows more but is slower and pricier. The drill fixes its manners — be polite, say so when you don\'t know.")},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새가 잘하는 것(요약·번역·초안·코드 고치기). 오른쪽 빨강: 빨간 앵무새가 '그 책은 1987년에 나왔어요' — 그런 책은 없음", "Left, green: what the parrot is good at (summaries, translation, drafts, fixing code). Right, red: a red parrot says that book came out in 1987 — no such book exists"),
         "caption": ("잘하는 게 많아요. 그런데 모르는 것도 자신 있게 이어 붙여요.", "It\'s good at a lot. But it continues just as confidently when it doesn\'t know."),
         "small": ('그래서 앵무새 답은 초안이에요. 이름·숫자·날짜는 사람이 확인해요. 자신 있는 거짓말은 <a href="hallucination-ko.html">그럴듯 앵무새</a> 이야기에서.',
                   'So a parrot\'s answer is a draft; a person checks names, numbers, dates. The confident lie has its own story: <a href="hallucination-en.html">the plausible parrot</a>.')},
    ],
    "summary": (("<b>LLM</b> = 책을 <b>산더미로 읽고</b> 다음 말 조각을 <b>잘 고르게 된 앵무새</b>. 뜻을 아는 게 아니라 이어 붙이는 거라, 답은 <b>초안</b>이고 확인은 사람이 해요.",
                 "<b>LLM</b> = a parrot that <b>read a mountain of books</b> and got <b>very good at picking the next word piece</b>. It continues rather than understands, so its answer is a <b>draft</b> and a person checks it."),
                ("Large Language Model. 방대한 텍스트로 '다음 토큰 예측'을 학습한 신경망이에요. 크기는 파라미터 수, 읽은 양은 학습 데이터, 읽은 뒤의 특훈은 파인튜닝·RLHF. 이해가 아니라 통계적 이어 붙이기라서 자신 있는 오답(할루시네이션)이 생겨요.",
                 "A neural network trained on vast text to predict the next token. Size is parameter count, what it read is training data, the drill afterwards is fine-tuning and RLHF. Because it continues statistically rather than understands, it can produce confident errors (hallucinations).")),
    "glossary": [
        ("대규모 언어 모델", "Large language model", ("책 산더미 앵무새.", "The mountain-of-books parrot."), ("GPT, Claude, Gemini, Llama 가 다 이 새예요.", "GPT, Claude, Gemini, Llama are all this bird.")),
        ("토큰", "Token", ("콩 하나.", "One bean."), ('앵무새가 말을 세는 단위. → <a href="token-ko.html">앵무새가 말을 콩으로 세요</a>', 'The unit the parrot counts words in. → <a href="token-en.html">the parrot counts words in beans</a>')),
        ("다음 토큰 예측", "Next-token prediction", ("다음 콩 고르기.", "Picking the next bean."), ("앵무새가 하는 일의 전부예요. 문장·시·코드가 다 여기서 나와요.", "The whole of what the parrot does. Sentences, poems, code all come from this.")),
        ("학습 데이터", "Training data", ("읽은 책 더미.", "The pile of books it read."), ("책에 없던 건 몰라요. 읽은 시점 이후 일도 몰라요(지식 컷오프).", "It doesn\'t know what wasn\'t in the books — or what happened after it finished reading (knowledge cutoff).")),
        ("파라미터", "Parameters", ("앵무새 크기.", "The parrot\'s size."), ("수십억~수조 개. 클수록 더 알고, 느리고, 비싸요.", "Billions to trillions. Bigger knows more, runs slower, costs more.")),
        ("파인튜닝 · RLHF", "Fine-tuning · RLHF", ("읽은 뒤 특훈.", "The drill after reading."), ('말버릇을 고쳐요. → <a href="finetune-ko.html">짧은 특훈</a>', 'Fixes its manners. → <a href="finetune-en.html">the short drill</a>')),
        ("할루시네이션", "Hallucination", ("자신 있는 거짓말.", "The confident lie."), ('모르는 것도 이어 붙여요. → <a href="hallucination-ko.html">그럴듯 앵무새</a>', 'It continues even when it doesn\'t know. → <a href="hallucination-en.html">the plausible parrot</a>')),
        ("프롬프트", "Prompt", ("조련 쪽지.", "The trainer\'s note."), ('앵무새에게 시키는 방법. → <a href="prompt-ko.html">앵무새에게 주는 조련 쪽지</a>', 'How you tell the parrot what to do. → <a href="prompt-en.html">the trainer\'s note</a>')),
    ],
}
