from _draw import *
from _world import *

# 1. 왜 긴 글은 돈이 더 들어요? — 앵무새는 글자가 아니라 콩으로 세요
P1 = svg(300, sky(300)
         + person(80, 120, s=0.9, face=EYES, **GUEST) + bubble(40, 30, 260, 40, "⟦왜 긴 글은 돈이 더 들어요?|why does a long text cost more?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + perch(420, 200, 140) + parrot(420, 160, 1.1, talk=True)
         + bubble_parrot(330, 30, 200, 40, "⟦글자 수가 아니라 콩 수예요|not letters — beans⟧", 12)
         + "".join(bean(540 + i * 30, 230, 0.9) for i in range(5))
         + note(590, 80, 150, 100, "⟦계산서|THE BILL⟧", ("⟦짧은 글: 콩 5개|short: 5 beans⟧", "⟦긴 글: 콩 300개|long: 300 beans⟧"), 1.0)
         + label(380, 282, "⟦앵무새는 말을 콩으로 세요 — 콩이 많으면 값도 시간도 늘어요|the parrot counts words in beans — more beans, more money and time⟧", 12, "var(--ink)"))

# 2. 콩은 낱말과 다르게 쪼개져요
ROWS = (("⟦안녕하세요|안녕하세요⟧", ("⟦안|안⟧", "⟦녕|녕⟧", "⟦하세|하세⟧", "⟦요|요⟧"), "⟦콩 4개|4 beans⟧"),
        ("⟦hello|hello⟧", ("⟦hello|hello⟧",), "⟦콩 1개|1 bean⟧"),
        ("⟦unbelievable|unbelievable⟧", ("⟦un|un⟧", "⟦believ|believ⟧", "⟦able|able⟧"), "⟦콩 3개|3 beans⟧"))
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(label(110, 85 + i * 60, w, 14, "var(--ink)", cls="d") + beans(250, 80 + i * 60, bs, 1.2, 46) + label(470, 85 + i * 60, c, 13, "var(--accent)", cls="d")
                   for i, (w, bs, c) in enumerate(ROWS))
         + parrot(640, 130, 1.0, mood="think") + label(640, 205, "⟦낱말이 아니라 조각이에요|pieces, not words⟧", 11, "var(--muted)")
         + label(380, 255, "⟦짧은 말이 콩 여러 개, 긴 말이 콩 하나이기도 해요 — 한글은 대개 더 잘게|a short word can be many beans, a long one just one — Korean usually cuts finer⟧", 11, "var(--ink)")
         + label(380, 282, "⟦콩은 낱말도 글자도 아니에요 — 앵무새만의 조각이에요|a bean is neither a word nor a letter — it is the parrot\'s own piece⟧", 12, "var(--bad)"))

# 3. 토큰 = 앵무새가 말을 세는 콩 (hero)
P3 = svg(360, sky(360)
         + label(300, 50, "⟦오늘 날씨가 참 좋아요|Today the weather is nice⟧", 14, "var(--ink)", cls="d")
         + '<path d="M300 62 L300 92" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M292 84 L300 94 L308 84" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + beans(160, 120, ("⟦오늘|Today⟧", "⟦날씨|the⟧", "⟦가|weather⟧", "⟦참|is⟧", "⟦좋아요|nice⟧"), 1.3, 60)
         + label(300, 162, "⟦콩 5개|5 beans⟧", 13, "var(--accent)", cls="d")
         + perch(300, 280, 160) + parrot(300, 240, 1.4, talk=True)
         + note(620, 40, 120, 90, "⟦콩 값|BEAN PRICE⟧", ("⟦콩 1000개|1000 beans⟧", "⟦= 동전 하나|= one coin⟧"), 1.0)
         + person(540, 130, s=0.9, face=SMILE, **TRAINER) + label(575, 262, "⟦콩 수로 값을 매겨요|priced by the bean⟧", 11, "var(--muted)")
         + label(380, 340, "⟦토큰 = 앵무새가 말을 세는 콩|a token is the bean the parrot counts words in⟧", 13, "var(--ink)", cls="d"))

# 4. 콩 세는 기계(토크나이저): 앵무새마다 콩 수가 달라요
CUT = ((PARROT, 5, "⟦콩 5개|5 beans⟧"), (PARROT_BIG, 7, "⟦콩 7개|7 beans⟧"), ("#2E7D6B", 9, "⟦콩 9개|9 beans⟧"))
P4 = svg(320, sky(320)
         + label(380, 40, "⟦같은 말: 오늘 날씨가 참 좋아요|same words: Today the weather is nice⟧", 13, "var(--ink)", cls="d")
         + "".join(parrot(80, 95 + i * 60, 0.6, color=c) + "".join(bean(160 + j * 28, 95 + i * 60, 0.7) for j in range(n)) + label(440, 100 + i * 60, t, 13, "var(--accent)", cls="d")
                   for i, (c, n, t) in enumerate(CUT))
         + note(500, 70, 230, 130, "⟦왜 달라요?|WHY DIFFERENT?⟧", ("⟦기계마다 자르는|each machine cuts⟧", "⟦자리가 달라요|in different places⟧", "⟦한글은 대개 더 잘게|Korean: usually finer⟧"), 1.0)
         + label(380, 262, "⟦콩 세는 기계가 다르면 콩 수도 값도 달라요|different bean counters — different counts, different prices⟧", 12, "var(--ink)")
         + label(380, 300, "⟦앵무새마다 콩 세는 기계가 달라요|every parrot has its own bean counter⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 콩 하나가 뜻 하나가 아니에요 + 쟁반
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + bean(190, 90, 1.6, text="⟦사과|bank⟧")
         + beans(100, 170, ("⟦빨간|river⟧", "⟦사과|bank⟧"), 1.1, 44) + label(250, 175, "⟦= 과일|= a shore⟧", 12, "var(--ink)", cls="d")
         + beans(100, 220, ("⟦사과|money⟧", "⟦할게요|bank⟧"), 1.1, 44) + label(250, 225, "⟦= 미안해요|= a shop⟧", 12, "var(--ink)", cls="d")
         + label(190, 270, "⟦콩 하나엔 뜻이 없어요 — 앞뒤 콩이 정해요|a bean alone has no meaning — its neighbours decide⟧", 11, "var(--bad)")
         + parrot(470, 62, 0.75, mood="think") + label(620, 60, "⟦쟁반 위 콩만 봐요|it only sees the tray⟧", 12, "var(--ink)")
         + tray(430, 120, 280, 70, "⟦쟁반 = 한 번에 올릴 수 있는 콩 수|the tray = beans that fit at once⟧")
         + "".join(bean(460 + i * 30, 108, 0.9) for i in range(8))
         + label(570, 262, "⟦쟁반 이야기는 다음 페이지에|the tray has its own page⟧", 11, "var(--muted)")
         + label(380, 300, "⟦콩은 세는 단위예요 — 뜻은 이어 붙이기가, 한도는 쟁반이 정해요|a bean is for counting — meaning comes from continuing, the limit from the tray⟧", 12, "var(--ink)", cls="d"))

COUNT_I = icon(f'<ellipse cx="18" cy="40" rx="12" ry="8" fill="{BEAN}"/><ellipse cx="40" cy="44" rx="12" ry="8" fill="{BEAN}"/><ellipse cx="30" cy="26" rx="12" ry="8" fill="{BEAN}"/><text x="52" y="22" text-anchor="middle" font-size="18" font-weight="700" fill="var(--accent)">3</text>')
SPLIT_I = icon(f'<ellipse cx="32" cy="18" rx="16" ry="10" fill="{BEAN}"/><path d="M32 30 v6" stroke="var(--muted)" stroke-width="3"/><ellipse cx="14" cy="48" rx="9" ry="6" fill="{BEAN}"/><ellipse cx="32" cy="48" rx="9" ry="6" fill="{BEAN}"/><ellipse cx="50" cy="48" rx="9" ry="6" fill="{BEAN}"/>')
COIN_I = icon(f'<ellipse cx="20" cy="40" rx="12" ry="8" fill="{BEAN}"/><path d="M34 40 h8" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/><circle cx="50" cy="36" r="11" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><path d="M50 30 v12 M46 33 h8 M46 39 h8" stroke="#5A3B22" stroke-width="2"/>')
TRAY_I = icon(f'<rect x="8" y="32" width="48" height="18" rx="6" fill="var(--stone)"/><rect x="12" y="36" width="40" height="10" rx="4" fill="none" stroke="var(--stone-dark)" stroke-width="2"/><ellipse cx="20" cy="28" rx="8" ry="5" fill="{BEAN}"/><ellipse cx="36" cy="28" rx="8" ry="5" fill="{BEAN}"/><ellipse cx="52" cy="28" rx="8" ry="5" fill="{BEAN}"/>')

PAGE = {
    "slug": "token", "order": 2,
    "title": ("앵무새가 말을 콩으로 세요", "The Parrot Counts Words in Beans"),
    "h1": ("<em>토큰</em>이 뭐예요?", "What is a <em>Token</em>?"),
    "sub": ("토큰을 앵무새가 글자도 낱말도 아닌 콩 단위로 말을 읽고 세는 이야기로 풀어봤어요.",
            "Tokens, told as a story about a parrot that reads and counts words not in letters or words, but in beans."),
    "panels": [
        {"svg": P1, "alt": ("손님이 왜 긴 글은 돈이 더 드는지 묻고, 횃대 위 앵무새가 글자 수가 아니라 콩 수라고 답함. 콩 다섯 개와 계산서 쪽지(짧은 글 콩 5개, 긴 글 콩 300개)", "A guest asks why a long text costs more; the parrot on its perch answers not letters, beans. Five beans and a bill note: short 5 beans, long 300 beans"),
         "caption": ("손님이 물어요. 왜 긴 글은 돈이 더 들어요?", "The guest asks: why does a long text cost more?"),
         "small": ("앵무새는 글자 수로 세지 않아요. 콩 수로 세요. 콩이 많으면 값도, 기다리는 시간도 늘어요.", "The parrot doesn\'t count letters. It counts beans. More beans means more money and a longer wait.")},
        {"svg": P2, "alt": ("빨간 배경. 안녕하세요는 콩 4개, hello 는 콩 1개, unbelievable 은 콩 3개(un·believ·able). 오른쪽에 생각하는 앵무새", "Red background. 안녕하세요 is 4 beans, hello is 1 bean, unbelievable is 3 beans (un·believ·able). A thinking parrot on the right"),
         "caption": ("콩은 낱말과 다르게 쪼개져요.", "Beans split differently from words."),
         "small": ("짧은 인사가 콩 넷, 긴 영어 낱말이 콩 셋. 한글은 대개 더 잘게 쪼개져서 같은 뜻이라도 콩이 더 들어요.", "A short greeting is four beans, a long English word is three. Korean usually splits finer, so the same meaning takes more beans.")},
        {"svg": P3, "hero": True, "alt": ("문장 오늘 날씨가 참 좋아요가 화살표 아래 콩 다섯 개로 쪼개지고, 그 아래 횃대의 앵무새가 말함. 조련사와 콩 값 쪽지(콩 1000개 = 동전 하나)", "The sentence Today the weather is nice splits under an arrow into five beans; below, the parrot on its perch speaks. A trainer and a bean-price note: 1000 beans = one coin"),
         "caption": ("토큰은 앵무새가 말을 세는 콩이에요.", "A token is the bean the parrot counts words in."),
         "small": ('말이 들어오면 콩으로 쪼개고, 답할 때도 콩을 하나씩 내놓아요. 콩 수가 값이고 시간이에요. 쟁반에 올릴 수 있는 만큼만 — 쟁반은 <a href="context-ko.html">앵무새 앞의 쟁반</a>에서.',
                   'Words coming in are split into beans; answers come out one bean at a time. The bean count is the price and the time. Only as many as fit on the tray — see <a href="context-en.html">the tray in front of the parrot</a>.'),
         "tricks": (4, [
             (COUNT_I, ("콩으로 세요", "Count in beans"), ("글자도 낱말도 아니에요", "not letters, not words"), "calm"),
             (SPLIT_I, ("한글은 더 잘게", "Korean cuts finer"), ("같은 뜻, 콩은 더 많이", "same meaning, more beans")),
             (COIN_I, ("콩 수 = 값·시간", "Beans = cost and time"), ("들어간 콩, 나온 콩 둘 다", "beans in and beans out"), "warm"),
             (TRAY_I, ("쟁반만큼만", "Only what fits the tray"), ("한 번에 올릴 수 있는 콩 수", "beans that fit at once"), "warm"),
         ])},
        {"svg": P4, "alt": ("같은 문장을 파란 앵무새는 콩 5개, 큰 앵무새는 7개, 초록 앵무새는 9개로 셈. 왜 달라요 쪽지: 기계마다 자르는 자리가 다르고 한글은 대개 더 잘게", "The same sentence: the blue parrot counts 5 beans, the big one 7, the green one 9. A note: each machine cuts in different places, Korean usually finer"),
         "caption": ("앵무새마다 콩 세는 기계가 달라요.", "Every parrot has its own bean counter."),
         "small": ("같은 문장인데 어떤 앵무새는 콩 다섯, 어떤 앵무새는 콩 아홉이에요. 자르는 자리가 다르니까요. 그래서 값도 달라요.", "Same sentence, yet one parrot counts five beans and another nine — they cut in different places. So the price differs too.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 콩 하나 사과가 앞뒤 콩에 따라 과일도 되고 미안해요도 됨. 오른쪽: 생각하는 앵무새와 콩 여덟 개가 올라간 쟁반", "Left, red: the single bean bank becomes a shore or a shop depending on its neighbours. Right: a thinking parrot and a tray holding eight beans"),
         "caption": ("콩 하나가 뜻 하나는 아니에요. 그리고 쟁반엔 한도가 있어요.", "One bean isn\'t one meaning. And the tray has a limit."),
         "small": ('사과라는 콩 하나만으론 과일인지 사죄인지 몰라요. 앞뒤 콩을 <a href="llm-ko.html">이어 붙이기</a>가 정해요. 한 번에 올릴 수 있는 콩 수는 <a href="context-ko.html">쟁반</a>이 정해요.',
                   'The bean bank alone doesn\'t say shore or shop; <a href="llm-en.html">continuing</a> from the beans around it decides. How many beans fit at once is decided by <a href="context-en.html">the tray</a>.')},
    ],
    "summary": (("<b>토큰</b> = 앵무새가 말을 <b>세는 콩</b>. 글자도 낱말도 아닌 <b>조각</b>이고, 한글은 더 잘게 쪼개져요. <b>콩 수가 값이고 시간</b>이에요.",
                 "<b>Token</b> = the <b>bean the parrot counts words in</b>. It\'s a <b>piece</b>, neither letter nor word, and Korean splits finer. <b>The bean count is the price and the time.</b>"),
                ("Token. LLM 이 텍스트를 읽고 쓰는 최소 단위예요. 토크나이저가 서브워드(BPE 등) 규칙으로 문장을 토큰으로 쪼개고, 모델마다 규칙이 달라 같은 문장의 토큰 수가 달라요. 입력·출력 토큰 수로 요금과 지연이 정해지고, 컨텍스트 창은 토큰 수로 한도가 잡혀요.",
                 "The smallest unit an LLM reads and writes. A tokenizer splits text into tokens by subword rules (BPE and the like); rules differ per model, so the same sentence has different token counts. Input and output token counts set price and latency, and the context window is capped in tokens.")),
    "glossary": [
        ("토큰", "Token", ("콩 하나.", "One bean."), ("앵무새가 말을 세는 조각. 낱말보다 작을 때가 많아요.", "The piece the parrot counts words in. Often smaller than a word.")),
        ("토크나이저", "Tokenizer", ("콩 세는 기계.", "The bean counter."), ("문장을 콩으로 자르는 규칙. 앵무새마다 달라요.", "The rule that cuts a sentence into beans. Different for every parrot.")),
        ("서브워드", "Subword (BPE)", ("낱말 조각.", "A word piece."), ("자주 붙어 다니는 글자 묶음을 콩 하나로 삼아요. BPE 가 대표적인 방법이에요.", "Letters that often go together become one bean. BPE is the usual method.")),
        ("토큰 수와 비용", "Token count and cost", ("콩 값.", "The bean price."), ("들어간 콩, 나온 콩 둘 다 세요. 콩이 많으면 비싸고 느려요.", "Beans in and beans out both count. More beans cost more and take longer.")),
        ("컨텍스트 창", "Context window", ("쟁반.", "The tray."), ('한 번에 올릴 수 있는 콩 수. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'How many beans fit at once. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("한글 토큰 효율", "Korean token efficiency", ("한글은 더 잘게.", "Korean cuts finer."), ("같은 뜻이라도 영어보다 콩이 더 들어요. 값도 더 들어요.", "The same meaning takes more beans than English — and costs more.")),
        ("임베딩", "Embedding", ("콩마다 붙은 좌표 딱지.", "A coordinate tag on each bean."), ("앵무새가 콩을 숫자 묶음으로 바꿔 기억해요. 뜻이 비슷하면 딱지도 가까워요.", "The parrot turns each bean into a bundle of numbers; similar meanings get nearby tags.")),
        ("프롬프트", "Prompt", ("조련 쪽지.", "The trainer\'s note."), ('쪽지도 콩으로 세요. → <a href="prompt-ko.html">앵무새에게 주는 조련 쪽지</a>', 'The note is counted in beans too. → <a href="prompt-en.html">the trainer\'s note</a>')),
    ],
}
