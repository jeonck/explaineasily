from _draw import *
from _world import *

# 1. 손님이 논문 저자를 물으니, 앵무새가 이름·연도·제목까지 자신 있게 말해요 — 그런 논문은 없어요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, color=PARROT_BAD, talk=True)
         + bubble_parrot(50, 20, 310, 44, "⟦김철수(2019), 「앵무새의 추론」이에요!|Kim (2019), The Reasoning Parrot!⟧", 12, bad=True)
         + label(205, 105, "⟦(그런 논문은 없어요)|(no such paper exists)⟧", 12, "var(--bad)")
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(430, 30, 260, 40, "⟦이 논문 저자가 누구야?|who wrote this paper?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦이름, 연도, 제목까지 말해요 — 하나도 진짜가 아니에요|a name, a year, a title — and none of it is real⟧", 13, "var(--ink)"))

# 2. 왜: 책에서 논문 얘기 뒤엔 늘 이름·연도가 이어졌어요. '모른다' 콩은 골라 본 적이 거의 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, mood="think") + label(110, 240, "⟦모르는데도 이어 붙여요|continues without knowing⟧", 12, "var(--muted)")
         + beans(250, 120, ("⟦이|this⟧", "⟦논문|paper⟧", "⟦저자는|was by⟧", "⟦…|…⟧"), 1.0, 60)
         + '<rect x="450" y="98" width="52" height="44" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(476, 126, "⟦?|?⟧", 22, "var(--accent)", cls="d")
         + note(540, 40, 190, 150, "⟦다음 콩 후보|NEXT BEAN⟧", ("⟦김철수 ★★★★|Kim   ★★★★⟧", "⟦이영희 ★★★|Lee   ★★★⟧", "⟦(2019) ★★★|(2019) ★★★⟧", "⟦모르겠어요 ☆|I don\'t know ☆⟧"), 1.0, 0)
         + label(330, 205, "⟦책에서 논문 얘기 뒤엔 늘 이름과 연도가 이어졌어요|in its books, a paper was always followed by a name and a year⟧", 12, "var(--ink)")
         + label(380, 282, "⟦그 모양대로 이어 붙여요 — '모르겠어요' 콩은 맨 아래예요|so it continues in that shape — the I-don\'t-know bean is at the bottom⟧", 12, "var(--bad)"))

# 3. 할루시네이션 = 모르는 것도 그럴듯하게 이어 붙이는 앵무새 (hero)
P3 = svg(360, sky(360)
         + perch(200, 240, 150) + parrot(200, 200, 1.4, color=PARROT_BAD, talk=True)
         + bubble_parrot(60, 40, 280, 44, "⟦저자는 김철수, 2019년이에요!|the author is Kim, 2019!⟧", 13, bad=True)
         + label(200, 128, "⟦자신 있게, 그럴듯하게, 틀리게|confident, plausible, wrong⟧", 12, "var(--bad)")
         + person(460, 150, s=0.9, face=FROWN, **GUEST) + label(495, 285, "⟦손님|guest⟧", 11, "var(--muted)")
         + note(580, 40, 160, 120, "⟦확인할 것|CHECK⟧", ("⟦이름·숫자·날짜|names, numbers, dates⟧", "⟦출처가 있나요?|is there a source?⟧", "⟦모르면 모른다고|say so if unsure⟧"), 0.95)
         + label(660, 200, "⟦답은 초안이에요|the answer is a draft⟧", 12, "var(--ink)")
         + label(380, 340, "⟦할루시네이션 = 모르는 것도 그럴듯하게 이어 붙이는 앵무새|hallucination is the parrot continuing plausibly even when it doesn\'t know⟧", 13, "var(--ink)", cls="d"))

# 4. 줄이는 방법 비교표 — 얼마나 줄고, 무엇은 못 줄이나
ROWS = (("⟦쪽지에 '모르면 모른다'|note: say if unsure⟧", "⟦조금|a bit⟧", "⟦진짜 모르는 건 그대로|truly unknown stays⟧"),
        ("⟦사서가 찾아온 페이지 올리기|librarian\'s page on the tray⟧", "⟦많이|a lot⟧", "⟦페이지가 틀리면 같이 틀려요|wrong page, wrong answer⟧"),
        ("⟦짧은 특훈|short drill⟧", "⟦말버릇만|manners only⟧", "⟦새 사실은 못 넣어요|no new facts⟧"),
        ("⟦다이얼 낮추기|turn the dial down⟧", "⟦엉뚱함만|randomness only⟧", "⟦자신 있는 틀림은 그대로|confident errors stay⟧"))
P4 = svg(320, sky(320)
         + '<rect x="30" y="30" width="540" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="540" height="30" rx="8" fill="#C9A86A"/>' + label(300, 50, "⟦거짓말 줄이기|FEWER LIES⟧", 13, "#142033", cls="d")
         + label(52, 82, "⟦방법|how⟧", 11, "#142033", "start", cls="d") + label(330, 82, "⟦얼마나|how much⟧", 11, "#142033", cls="d") + label(400, 82, "⟦그래도 남는 것|what stays⟧", 11, "#142033", "start", cls="d")
         + "".join(f'<circle cx="60" cy="{106 + i * 42}" r="8" fill="{c}"/>' + label(76, 111 + i * 42, t, 12, "#142033", "start") + label(330, 111 + i * 42, d, 12, "#142033") + label(400, 111 + i * 42, r, 11, "#142033", "start")
                   for i, ((t, d, r), c) in enumerate(zip(ROWS, ("var(--accent)", "var(--good)", "#5B8DEF", "var(--stone-dark)"))))
         + dial(660, 110, 1.0, 0.2, "⟦다이얼 낮추기|dial down⟧")
         + person(600, 170, s=0.7, face=SMILE, **LIBRARIAN) + note(650, 190, 90, 60, "⟦페이지|PAGE⟧", ("⟦진짜 논문 목록|real paper list⟧",), 0.85)
         + label(380, 300, "⟦사서의 페이지가 제일 세요 — 그래도 하나만으론 부족해요|the librarian\'s page works best — but no single fix is enough⟧", 12, "var(--muted)"))

# 5. 완전히 없앨 순 없어요 — 답은 초안, 확인은 사람, 위험한 일엔 울타리
FENCE = "".join(f'<rect x="{560 + i * 32}" y="130" width="8" height="90" rx="2" fill="{WOOD}"/>' for i in range(5)) + f'<rect x="556" y="150" width="144" height="6" fill="{WOOD}"/><rect x="556" y="190" width="144" height="6" fill="{WOOD}"/>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(100, 150, 1.0, talk=True) + bubble_parrot(30, 50, 180, 40, "⟦아마 2019년쯤…|probably around 2019…⟧", 11)
         + person(230, 110, s=0.8, face=SMILE, **TRAINER) + note(295, 150, 80, 60, "⟦확인|CHECK⟧", ("⟦연도 ✓|year ✓⟧",), 0.9)
         + label(190, 250, "⟦답은 초안, 확인은 사람이 해요|the answer is a draft; a person checks⟧", 11, "var(--ink)")
         + parrot(470, 150, 1.0, color=PARROT_BAD, mood="sweat") + FENCE + label(630, 110, "⟦돈 보내기 · 약 고르기|sending money · picking medicine⟧", 11, "var(--bad)")
         + label(570, 250, "⟦위험한 일 앞엔 울타리를 세워요|a fence in front of risky jobs⟧", 11, "var(--ink)")
         + label(380, 300, "⟦완전히 없앨 순 없어요 — 이어 붙이는 새의 본성이에요|it can\'t be removed completely — continuing is the bird\'s nature⟧", 12, "var(--ink)", cls="d"))

DOUBT_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 24 h16 M18 32 h24 M18 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><circle cx="46" cy="44" r="10" fill="var(--bad)"/><text x="46" y="49" text-anchor="middle" font-size="14" font-weight="700" fill="#FFF">?</text>')
SOURCE_I = icon('<rect x="8" y="14" width="30" height="38" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M16 26 h14 M16 34 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M38 33 h14" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/><path d="M46 26 l8 7 l-8 7" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
UNSURE_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="10" width="44" height="12" rx="4" fill="#C9A86A"/><text x="32" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="#142033">?</text><path d="M18 34 h28" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
TRAY_I = icon(f'<rect x="6" y="34" width="52" height="18" rx="6" fill="var(--stone)"/><rect x="18" y="14" width="26" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 24 h14 M24 32 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "hallucination", "order": 5,
    "title": ("그럴듯 앵무새", "The Plausible Parrot"),
    "h1": ("<em>할루시네이션</em>이 뭐예요?", "What is a <em>Hallucination</em>?"),
    "sub": ("할루시네이션(AI 환각)을 모르는 것도 자신 있게 그럴듯하게 이어 붙이는 앵무새 이야기로 풀어봤어요.",
            "AI hallucination, told as a story about a parrot that continues confidently and plausibly even when it doesn\'t know."),
    "panels": [
        {"svg": P1, "alt": ("빨간 앵무새가 횃대에서 '김철수(2019), 앵무새의 추론이에요!'라고 말하고 아래에 '그런 논문은 없어요'. 손님이 '이 논문 저자가 누구야?'라고 물음", "A red parrot on a perch says Kim (2019), The Reasoning Parrot!, with a note that no such paper exists; a guest asks who wrote this paper"),
         "caption": ("손님이 논문 저자를 물으니, 앵무새가 이름과 연도와 제목까지 말해요.", "A guest asks who wrote a paper, and the parrot gives a name, a year, even a title."),
         "small": ("아주 자신 있게, 아주 그럴듯하게요. 그런데 그런 논문은 세상에 없어요.", "Very confidently, very plausibly. But that paper doesn\'t exist.")},
        {"svg": P2, "alt": ("눈 감은 앵무새, '이 논문 저자는 …' 콩 네 개와 물음표, '다음 콩 후보' 쪽지에 김철수 ★★★★, 이영희 ★★★, (2019) ★★★, 모르겠어요 ☆", "A parrot with eyes closed; beans reading this paper was by … and a question mark; a next-bean note ranks Kim ★★★★, Lee ★★★, (2019) ★★★, I don\'t know ☆"),
         "caption": ("책에서 논문 얘기 뒤엔 늘 이름과 연도가 이어졌어요. 그 모양대로 이어 붙여요.", "In its books, a paper was always followed by a name and a year. So it continues in that shape."),
         "small": ("'모르겠어요'라는 콩은 골라 본 적이 거의 없어요. 그래서 맨 아래 후보예요. 앵무새는 뜻이 아니라 모양을 이어요.", "It has almost never picked the I-don\'t-know bean, so that one sits at the bottom. The parrot continues the shape, not the meaning.")},
        {"svg": P3, "hero": True, "alt": ("빨간 앵무새가 '저자는 김철수, 2019년이에요!'라고 자신 있게 말하고, 손님은 찡그림. '확인할 것' 쪽지: 이름·숫자·날짜, 출처가 있나요, 모르면 모른다고", "A red parrot confidently says the author is Kim, 2019; the guest frowns. A CHECK note lists names, numbers, dates; is there a source; say so if unsure"),
         "caption": ("할루시네이션은 모르는 것도 그럴듯하게 이어 붙이는 앵무새예요.", "A hallucination is the parrot continuing plausibly even when it doesn\'t know."),
         "small": ('<a href="llm-ko.html">책 산더미 앵무새</a>는 원래 이렇게 태어났어요. 이름·숫자·날짜는 특히 의심하고, 사서가 찾아온 진짜 페이지를 <a href="context-ko.html">쟁반</a>에 올려 주면 훨씬 덜 틀려요.',
                   'The <a href="llm-en.html">mountain-of-books parrot</a> was born this way. Doubt names, numbers and dates most, and it errs far less when a real page the librarian found sits on its <a href="context-en.html">tray</a>.'),
         "tricks": (4, [
             (DOUBT_I, ("이름·숫자·날짜는 의심", "Doubt names, numbers, dates"), ("제일 자주 틀려요", "wrong most often"), "warm"),
             (SOURCE_I, ("출처를 같이 달라고 해요", "Ask for sources too"), ("없으면 초안일 뿐", "no source, just a draft"), "calm"),
             (UNSURE_I, ("모르면 모른다고, 쪽지에", "Say so if unsure — in the note"), ("모르겠어요 콩을 위로", "lift the I-don\'t-know bean"), "calm"),
             (TRAY_I, ("사서 페이지를 쟁반에", "Librarian\'s page on the tray"), ("진짜 글을 보고 이어요", "continues from real text"), "calm"),
         ])},
        {"svg": P4, "alt": ("'거짓말 줄이기' 표: 쪽지에 모르면 모른다=조금, 사서 페이지=많이(페이지가 틀리면 같이 틀림), 짧은 특훈=말버릇만, 다이얼 낮추기=엉뚱함만(자신 있는 틀림은 그대로). 옆에 낮춘 다이얼과 사서", "A FEWER LIES table: note saying if unsure = a bit; librarian\'s page = a lot (wrong page, wrong answer); short drill = manners only; dial down = randomness only (confident errors stay). A turned-down dial and a librarian beside it"),
         "caption": ("줄이는 방법은 여러 가지예요. 사서의 페이지가 제일 세고, 다이얼은 엉뚱함만 줄여요.", "There are several ways to reduce it. The librarian\'s page works best; the dial only cuts randomness."),
         "small": ('쪽지 한 줄은 조금 돕고, <a href="finetune-ko.html">짧은 특훈</a>은 말버릇만 고쳐요. 다이얼을 낮춰도 자신 있는 틀림은 그대로예요 — 그건 엉뚱함이 아니니까요.',
                   'A line in the note helps a little, and the <a href="finetune-en.html">short drill</a> only fixes manners. Turning the dial down leaves confident errors in place — they aren\'t randomness.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새가 '아마 2019년쯤…'이라 하고 조련사가 '연도 ✓' 쪽지로 확인. 오른쪽 빨강: 빨간 앵무새 앞에 울타리, 그 너머 '돈 보내기 · 약 고르기'", "Left, green: the parrot says probably around 2019 and a trainer checks with a year ✓ note. Right, red: a fence in front of the red parrot, with sending money and picking medicine beyond it"),
         "caption": ("완전히 없앨 순 없어요. 이어 붙이는 새의 본성이니까요.", "It can\'t be removed completely — continuing is the bird\'s nature."),
         "small": ('그래서 답은 초안이고 확인은 사람이 해요. 돈이나 약처럼 위험한 일 앞엔 울타리를 세워요 — 도둑이 기른 앵무새 이야기는 <a href="aisec-ko.html">보안 쪽</a>에 있어요.',
                   'So the answer is a draft and a person checks it. In front of risky jobs like money or medicine, put up a fence — the thief\'s parrot story lives on the <a href="aisec-en.html">security side</a>.')},
    ],
    "summary": (("<b>할루시네이션</b> = 모르는 것도 <b>자신 있게, 그럴듯하게</b> 이어 붙이는 앵무새. 이름·숫자·날짜를 의심하고, <b>출처</b>를 달라고 하고, 사서의 <b>진짜 페이지</b>를 쟁반에 올려요. 완전히는 못 없애요 — 답은 초안, 확인은 사람.",
                 "<b>Hallucination</b> = the parrot continuing <b>confidently and plausibly</b> even when it doesn\'t know. Doubt names, numbers, dates; ask for <b>sources</b>; put the librarian\'s <b>real page</b> on the tray. It never fully goes away — the answer is a draft, a person checks."),
                ("Hallucination. 언어 모델이 학습 분포상 그럴듯한 다음 토큰을 이어 가느라 사실이 아닌 내용을 생성하는 현상이에요. 프롬프트 지시·RAG(검색 근거 주입)·파인튜닝·낮은 temperature 로 줄이지만 제거되진 않아요. 출처 인용, 사실성 평가, 캘리브레이션(자신감과 정확도 맞추기), 고위험 작업의 가드레일이 함께 쓰여요.",
                 "A language model generates content that isn\'t true because it keeps producing the next token that looks plausible under its training distribution. Prompt instructions, RAG (injecting retrieved evidence), fine-tuning and low temperature reduce it but never remove it. Source citation, factuality evaluation, calibration (matching confidence to accuracy) and guardrails for high-risk tasks are used alongside.")),
    "glossary": [
        ("할루시네이션", "Hallucination", ("그럴듯한 거짓말.", "The plausible lie."), ("모르는 것도 이어 붙여서 생겨요. 틀린 게 아니라 '지어낸' 거예요.", "Comes from continuing what it doesn\'t know. Not a mistake so much as a make-up.")),
        ("근거", "Grounding", ("진짜 글을 보고 말하기.", "Speaking from real text."), ("사서가 찾아온 페이지를 쟁반에 올려 주면 그걸 보고 이어요.", "Put the page the librarian found on the tray, and it continues from that.")),
        ("RAG", "Retrieval-augmented generation", ("사서 + 앵무새.", "Librarian + parrot."), ("물어볼 때마다 사서가 먼저 찾고, 앵무새가 그 페이지로 답해요. 새 지식을 넣는 제일 쉬운 길이에요.", "For every question the librarian searches first, then the parrot answers from that page. The easiest way to add new knowledge.")),
        ("출처 인용", "Source citation", ("어디서 봤는지 적기.", "Saying where it saw it."), ("출처가 붙은 답은 사람이 확인할 수 있어요. 출처가 없으면 초안이에요.", "An answer with a source can be checked by a person. No source means it\'s a draft.")),
        ("온도", "Temperature", ("엉뚱함 다이얼.", "The randomness dial."), ("낮추면 뻔한 콩만 골라요. 엉뚱함은 줄지만 자신 있는 틀림은 안 줄어요.", "Turn it down and it picks only the obvious bean. Less randomness, but confident errors stay.")),
        ("사실성 평가", "Factuality evaluation", ("답을 정답표와 맞춰 보기.", "Checking answers against a key."), ("시험관이 진짜 답이 있는 질문 수백 개로 얼마나 지어내는지 재요.", "An examiner measures how often it makes things up, using hundreds of questions with known answers.")),
        ("자신감 vs 정확도", "Calibration", ("확신하는 만큼 맞나.", "Is it right as often as it sounds sure?"), ("잘 맞춘 앵무새는 모를 때 작게 말해요. 그럴듯 앵무새는 늘 크게 말해요.", "A well-calibrated parrot speaks softly when unsure. The plausible parrot is always loud.")),
        ("프롬프트", "Prompt", ("조련 쪽지.", "The trainer\'s note."), ('모르면 모른다고 해 — 이 한 줄이 조금 도와요. → <a href="prompt-ko.html">앵무새에게 주는 조련 쪽지</a>', 'Say so if you do not know — that one line helps a little. → <a href="prompt-en.html">the trainer\'s note</a>')),
    ],
}
