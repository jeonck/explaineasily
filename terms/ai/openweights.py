from _draw import *
from _world import *

ARROW = '<path d="M{0} {2} L{1} {2}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M{3} {4} L{1} {2} L{3} {5}" stroke="var(--muted)" stroke-width="3" fill="none"/>'


def arrow(x0, x1, y):
    return ARROW.format(x0, x1, y, x1 - 10, y - 8, y + 8)


# 1. 앵무새를 쓰려면 두 길 — 남의 집 창구로 묻기 vs 우리 집 횃대에 데려오기
P1 = svg(300, sky(300)
         + label(380, 30, "⟦앵무새를 쓰려면 두 길이 있어요|there are two ways to use a parrot⟧", 13, "var(--ink)", cls="d")
         + '<path d="M380 60 V215" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5"/>'
         + '<rect x="110" y="70" width="140" height="120" rx="6" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/><rect x="100" y="190" width="160" height="10" rx="3" fill="var(--stone-dark)"/>'
         + parrot(180, 150, 0.9, talk=True) + label(215, 62, "⟦남의 집 창구|their counter⟧", 11, "var(--muted)")
         + person(20, 110, s=0.8, face=EYES, **TRAINER) + bubble(10, 40, 150, 36, "⟦창구로 물어요|ask at the counter⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(190, 232, "⟦빌린 앵무새|the borrowed parrot⟧", 13, "var(--ink)", cls="d") + label(190, 252, "⟦물을 때마다 콩 값을 내요|pay beans every time you ask⟧", 11, "var(--muted)")
         + perch(560, 200, 140) + parrot(560, 160, 1.1, talk=True)
         + person(640, 100, s=0.8, face=SMILE, **TRAINER) + bubble(600, 30, 150, 36, "⟦우리 횃대에 데려와요|bring it to our perch⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(560, 232, "⟦우리 집 앵무새|our own parrot⟧", 13, "var(--ink)", cls="d") + label(560, 252, "⟦횃대를 우리가 마련해요|we set up the perch ourselves⟧", 11, "var(--muted)")
         + label(380, 282, "⟦빌릴까, 데려올까?|borrow it, or bring it home?⟧", 13, "var(--ink)"))

# 2. 어느 길이든 걱정이 있어요 — 콩 값·비밀 콩 vs 횃대·돌보기
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<path d="M380 50 V270" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5"/>'
         + label(190, 30, "⟦빌린 앵무새 걱정|borrowed-parrot worries⟧", 13, "var(--ink)", cls="d")
         + person(40, 110, s=0.8, face=FROWN, **TRAINER)
         + note(130, 60, 150, 80, "⟦청구서|BILL⟧", ("⟦콩 값 × 만 번|beans × ten thousand⟧", "⟦= 큰 돈|= a lot of money⟧"), 0.9)
         + "".join(bean(150 + i * 36, 165, 1.0) for i in range(4)) + label(205, 195, "⟦물을 때마다 콩 값|beans every time⟧", 11, "var(--muted)")
         + bean(150, 235, 1.0, "#7B3FA0", "⟦비밀|secret⟧") + arrow(175, 340, 235)
         + label(250, 268, "⟦비밀 콩이 남의 집으로 나가요|secret beans leave for their house⟧", 11, "var(--bad)")
         + label(570, 30, "⟦우리 집 앵무새 걱정|own-parrot worries⟧", 13, "var(--ink)", cls="d")
         + parrot(470, 80, 0.9) + '<rect x="420" y="120" width="100" height="80" rx="6" fill="var(--stone-dark)"/><circle cx="450" cy="160" r="16" fill="none" stroke="var(--stone)" stroke-width="4"/><circle cx="490" cy="160" r="16" fill="none" stroke="var(--stone)" stroke-width="4"/>'
         + label(470, 222, "⟦횃대 (GPU) — 비싸요|the perch (GPU) — pricey⟧", 11, "var(--muted)")
         + person(580, 110, s=0.8, face=FROWN, extra=SWEAT, **TRAINER)
         + note(650, 110, 100, 105, "⟦할 일|TO DO⟧", ("⟦먹이 주기|feeding⟧", "⟦고치기|fixing⟧", "⟦지켜보기|watching⟧"), 0.9)
         + label(570, 262, "⟦횃대도 사고, 돌보는 사람도 있어야 해요|buy the perch, and someone has to care for it⟧", 11, "var(--bad)")
         + label(380, 300, "⟦어느 길이든 걱정이 있어요 — 무엇을 아끼고 싶은지가 문제예요|either way has worries — the question is what you want to protect⟧", 12, "var(--ink)"))

# 3. 오픈 웨이트 = 앵무새 머릿속 눈금(가중치)을 통째로 공개한 앵무새 (hero)
P3 = svg(360, sky(360)
         + note(40, 30, 170, 100, "⟦눈금 (가중치)|WEIGHTS⟧", ("⟦0.31  -0.72  1.05|0.31  -0.72  1.05⟧", "⟦2.14  0.08  -0.55|2.14  0.08  -0.55⟧", "⟦… 수십억 개|… billions of them⟧"), 0.95)
         + perch(220, 240, 150) + parrot(220, 200, 1.4, talk=True)
         + label(220, 300, "⟦눈금 = 앵무새 머릿속 숫자 전부|weights = every number in its head⟧", 11, "var(--muted)")
         + label(330, 150, "⟦공개!|OPEN!⟧", 18, "var(--good)", cls="d") + arrow(290, 410, 190)
         + perch(470, 200, 80) + parrot(470, 160, 0.7) + label(470, 262, "⟦Llama|Llama⟧", 11, "var(--muted)")
         + perch(570, 200, 80) + parrot(570, 160, 0.7) + label(570, 262, "⟦Mistral|Mistral⟧", 11, "var(--muted)")
         + perch(670, 200, 80) + parrot(670, 160, 0.7) + label(670, 262, "⟦Qwen|Qwen⟧", 11, "var(--muted)")
         + label(570, 110, "⟦누구나 자기 횃대에 올려요|anyone can put it on their own perch⟧", 12, "var(--ink)", cls="d")
         + label(380, 340, "⟦오픈 웨이트 = 머릿속 눈금을 통째로 공개해, 누구나 제 횃대에 올릴 수 있는 앵무새|open weights: a parrot whose every number is published, so anyone can put it on their own perch⟧", 13, "var(--ink)", cls="d"))

# 4. 비교 표 — 빌린 앵무새 vs 우리 집 앵무새
ROWS = (("⟦비용 구조|cost⟧", "⟦콩마다 값을 내요|pay per bean⟧", "⟦횃대 값을 먼저 내요|pay for the perch up front⟧"),
        ("⟦최신성|freshness⟧", "⟦제일 새 앵무새|the newest parrots⟧", "⟦조금 늦게 와요|arrives a bit later⟧"),
        ("⟦데이터 위치|where data goes⟧", "⟦남의 집으로 가요|to their house⟧", "⟦우리 집에 있어요|stays home⟧"),
        ("⟦손보기 자유|freedom to tweak⟧", "⟦정해진 만큼만|only what they allow⟧", "⟦특훈·굵게 세기 자유|drill and coarse-count freely⟧"),
        ("⟦운영 부담|upkeep⟧", "⟦거의 없어요|almost none⟧", "⟦우리가 돌봐요|we do the caring⟧"))
P4 = svg(320, sky(320)
         + '<rect x="30" y="30" width="700" height="245" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="700" height="30" rx="8" fill="#C9A86A"/>' + label(380, 50, "⟦빌린 앵무새 vs 우리 집 앵무새|BORROWED vs OUR OWN⟧", 13, "#142033", cls="d")
         + label(250, 82, "⟦빌린 앵무새 (창구)|borrowed (counter)⟧", 12, "#142033", "start", cls="d") + label(500, 82, "⟦우리 집 앵무새 (횃대)|our own (perch)⟧", 12, "#142033", "start", cls="d")
         + '<path d="M50 92 H710" stroke="#C9A86A" stroke-width="2"/>'
         + "".join(label(50, 120 + i * 34, a, 12, "#142033", "start", cls="d") + label(250, 120 + i * 34, b, 11, "#142033", "start") + label(500, 120 + i * 34, c, 11, "#142033", "start") for i, (a, b, c) in enumerate(ROWS))
         + label(380, 300, "⟦정답은 없어요 — 데이터·돈·사람에 따라 골라요|no single right answer — pick by your data, money and people⟧", 12, "var(--muted)"))

# 5. '오픈'이 '공짜'도 '오픈소스'도 아니에요
P5 = svg(320, '<rect width="253" height="320" fill="var(--bad-soft)"/><rect x="253" width="253" height="320" fill="var(--accent-soft)"/><rect x="506" width="254" height="320" fill="var(--accent-soft)"/>'
         + label(126, 30, "⟦공짜?|free?⟧", 13, "var(--ink)", cls="d")
         + parrot(90, 130, 0.9) + '<rect x="50" y="180" width="80" height="50" rx="6" fill="var(--stone-dark)"/><circle cx="90" cy="205" r="14" fill="none" stroke="var(--stone)" stroke-width="4"/>'
         + label(180, 120, "⟦비싸요|pricey⟧", 14, "var(--bad)", cls="d") + label(180, 140, "⟦횃대·전기|perch, power⟧", 10, "var(--muted)") + label(180, 156, "⟦돌보는 사람|and a keeper⟧", 10, "var(--muted)")
         + label(126, 275, "⟦눈금은 공짜, 횃대는 아니에요|weights are free, the perch is not⟧", 10, "var(--bad)")
         + label(380, 30, "⟦오픈소스?|open source?⟧", 13, "var(--ink)", cls="d")
         + note(300, 50, 160, 66, "⟦공개|OPEN⟧", ("⟦눈금 ✓|weights ✓⟧",), 0.9)
         + books(380, 200, 5, 1.0) + label(450, 165, "⟦?|?⟧", 30, "var(--accent)", cls="d")
         + label(380, 228, "⟦어떤 책을 읽었는진 비밀|which books it read: secret⟧", 10, "var(--ink)")
         + label(380, 275, "⟦눈금은 열려도 책 목록은 닫혀 있어요|weights open, book list closed⟧", 10, "var(--bad)")
         + label(633, 30, "⟦조건은?|conditions?⟧", 13, "var(--ink)", cls="d")
         + note(560, 50, 150, 105, "⟦라이선스|LICENSE⟧", ("⟦장사에 쓰려면…|to use for business…⟧", "⟦큰 회사는 허락받기|big firms ask first⟧", "⟦이름 표시하기|show the name⟧"), 0.9)
         + person(600, 165, s=0.8, face=EYES, **TRAINER)
         + label(633, 275, "⟦두루마리를 꼭 읽어요|read the scroll first⟧", 10, "var(--ink)")
         + label(380, 300, "⟦'오픈'은 공짜도, 오픈소스도 아니에요 — 두루마리를 읽어요|open is neither free nor open source — read the scroll⟧", 12, "var(--ink)", cls="d"))

HOUSE_I = icon('<path d="M10 30 L32 10 L54 30 V54 H10 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="18" y="38" width="28" height="4" rx="2" fill="#8B5E3C"/><ellipse cx="32" cy="30" rx="6" ry="8" fill="#5B8DEF"/><circle cx="32" cy="20" r="5" fill="#5B8DEF"/>')
BIG_I = icon('<ellipse cx="32" cy="36" rx="14" ry="18" fill="#3F6FD1"/><circle cx="32" cy="14" r="10" fill="#3F6FD1"/><path d="M40 12 l10 3 l-10 4z" fill="#E9B44C"/><path d="M8 54 h48" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/><circle cx="52" cy="46" r="8" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><text x="52" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="var(--accent)">?</text>')
TWEAK_I = icon('<rect x="10" y="12" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M17 24 h16 M17 32 h12 M17 40 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M42 44 l12 -12 M48 26 l6 6" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="30" r="4" fill="var(--good)"/>')
SCROLL_I = icon('<rect x="14" y="8" width="36" height="48" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 28 h20 M22 36 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M36 44 l4 4 l8 -8" stroke="var(--accent)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "openweights", "order": 35,
    "title": ("우리 집 앵무새 vs 빌린 앵무새", "Our Own Parrot vs a Borrowed One"),
    "h1": ("<em>오픈 웨이트</em>가 뭐예요?", "What are <em>Open Weights</em>?"),
    "sub": ("오픈 웨이트 모델을 머릿속 눈금을 통째로 공개해 누구나 자기 횃대에 데려올 수 있는 앵무새 이야기로 풀어봤어요.",
            "Open-weight models, told as a story about a parrot whose every number is published, so anyone can bring it home to their own perch."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽: 조련사가 남의 집 창구 너머 앵무새에게 물음(빌린 앵무새, 물을 때마다 콩 값). 오른쪽: 조련사가 앵무새를 우리 집 횃대에 데려옴(우리 집 앵무새, 횃대는 우리가 마련)", "Left: a trainer asks a parrot through their counter (borrowed, pay beans every time). Right: a trainer brings a parrot to our own perch (our own, we set up the perch)"),
         "caption": ("앵무새를 쓰려면 두 길이 있어요. 남의 집 창구로 묻거나, 우리 집 횃대에 데려오거나.", "There are two ways to use a parrot: ask through their counter, or bring it home to our perch."),
         "small": ('창구로 물으면 앵무새는 남의 집에 있고, 물을 때마다 <a href="token-ko.html">콩</a> 값을 내요. 데려오면 앵무새가 우리 집에 있어요.', 'Ask at the counter and the parrot stays at their house; you pay <a href="token-en.html">beans</a> every time. Bring it home and the parrot lives with you.')},
        {"svg": P2, "alt": ("왼쪽: 청구서(콩 값 × 만 번 = 큰 돈), 콩 네 개, 보라색 비밀 콩이 남의 집으로 나가는 화살표. 오른쪽: 앵무새가 앉은 GPU 상자(비싸요), 땀 흘리는 조련사와 '할 일: 먹이 주기, 고치기, 지켜보기' 쪽지", "Left: a bill (beans × ten thousand = a lot), four beans, a purple secret bean leaving for their house. Right: a parrot on a GPU box (pricey), a sweating trainer and a TO DO note: feeding, fixing, watching"),
         "caption": ("어느 길이든 걱정이 있어요. 빌리면 콩 값과 비밀 콩, 데려오면 횃대와 돌보기.", "Either way has worries: borrowing means bean bills and secret beans; bringing home means the perch and the caring."),
         "small": ('빌린 앵무새는 물을 때마다 <a href="pricing-ko.html">콩 값</a>이 나가고, <a href="aiprivacy-ko.html">비밀 콩</a>이 남의 집으로 가요. 우리 집 앵무새는 횃대(GPU)가 비싸고, 누군가 매일 <a href="llmops-ko.html">돌봐야</a> 해요.',
                   'A borrowed parrot costs <a href="pricing-en.html">beans</a> every time, and your <a href="aiprivacy-en.html">secret beans</a> go to their house. Your own parrot needs a pricey perch (GPU) and someone to <a href="llmops-en.html">care for it</a> every day.')},
        {"svg": P3, "hero": True, "alt": ("'눈금 (가중치)' 쪽지에 숫자들과 '수십억 개'. 횃대의 큰 앵무새에서 '공개!' 화살표가 세 작은 횃대(Llama, Mistral, Qwen)로 이어짐. '누구나 자기 횃대에 올려요'", "A WEIGHTS note with numbers and billions of them. From a big parrot on a perch, an OPEN! arrow leads to three small perches labeled Llama, Mistral, Qwen. Anyone can put it on their own perch"),
         "caption": ("오픈 웨이트는 머릿속 눈금을 통째로 공개해, 누구나 제 횃대에 올릴 수 있는 앵무새예요.", "Open weights: a parrot whose every number in its head is published, so anyone can put it on their own perch."),
         "small": ('앵무새 머릿속엔 숫자(가중치)가 수십억 개 있어요. 이걸 통째로 내놓으면 누구나 내려받아 자기 횃대에 올려요 — Llama, Mistral, Qwen 같은 새들이에요. 제일 똑똑한 앵무새는 보통 <a href="llm-ko.html">창구</a>로만 만나요.',
                   'A parrot has billions of numbers (weights) in its head. Publish them all and anyone can download the bird and put it on their own perch — Llama, Mistral, Qwen are such birds. The very smartest parrots are usually met only at the <a href="llm-en.html">counter</a>.'),
         "tricks": (4, [
             (HOUSE_I, ("데이터가 밖에 못 나가면 우리 집", "Data can\'t leave? Own it"), ("비밀 콩은 집에 둬요", "keep secret beans home"), "calm"),
             (BIG_I, ("제일 똑똑한 새는 보통 빌려요", "The smartest are usually borrowed"), ("창구에만 있어요", "they live at the counter"), "warm"),
             (TWEAK_I, ("특훈·굵게 세기는 우리 집이 자유", "Drill and coarse-count freely at home"), ("우리 새는 우리 마음대로", "our bird, our rules"), "calm"),
             (SCROLL_I, ("라이선스 두루마리를 읽어요", "Read the license scroll"), ("공짜가 아닐 수 있어요", "it may not be free")),
         ])},
        {"svg": P4, "alt": ("'빌린 앵무새 vs 우리 집 앵무새' 표: 비용 구조(콩마다 vs 횃대 값 먼저), 최신성(제일 새 앵무새 vs 조금 늦게), 데이터 위치(남의 집 vs 우리 집), 손보기 자유(정해진 만큼 vs 특훈·굵게 세기 자유), 운영 부담(거의 없음 vs 우리가 돌봄)", "A BORROWED vs OUR OWN table: cost (per bean vs perch up front), freshness (newest vs a bit later), where data goes (their house vs stays home), freedom to tweak (only what they allow vs drill freely), upkeep (almost none vs we do the caring)"),
         "caption": ("빌린 앵무새와 우리 집 앵무새는 값, 새로움, 데이터 위치, 손보기, 돌보기가 달라요.", "Borrowed and own parrots differ in cost, freshness, where data goes, tweaking, and upkeep."),
         "small": ('우리 집 앵무새는 <a href="finetune-ko.html">특훈</a>도, <a href="quantization-ko.html">콩을 굵게 세기</a>도 마음대로예요. 대신 답하는 <a href="inference-ko.html">값과 시간</a>은 우리 횃대가 정해요.', 'Your own parrot can be <a href="finetune-en.html">drilled</a> or made to <a href="quantization-en.html">count beans coarsely</a> as you like. In return, its <a href="inference-en.html">cost and speed</a> depend on your perch.')},
        {"svg": P5, "alt": ("세 칸: 빨강 — GPU 상자 위 앵무새와 '비싸요: 횃대·전기·돌보는 사람'. 주황 — '공개: 눈금 ✓' 쪽지와 물음표 붙은 책 더미(어떤 책을 읽었는진 비밀). 주황 — '라이선스' 쪽지(장사에 쓰려면, 큰 회사는 허락받기, 이름 표시)를 읽는 조련사", "Three columns: red — a parrot on a GPU box, pricey: perch, power, a keeper. Orange — an OPEN note (weights ✓) and a book pile with a question mark (which books it read: secret). Orange — a trainer reading a LICENSE note: for business, big firms ask first, show the name"),
         "caption": ("'오픈'은 공짜도, 오픈소스도 아니에요. 눈금은 열려도 책 목록은 비공개이고, 장사엔 조건이 붙어요.", "Open is neither free nor open source. The numbers are public, the book list isn\'t, and business use has conditions."),
         "small": ('횃대와 돌보기엔 돈이 들어요 — <a href="pricing-ko.html">콩 값</a>과 비교해 봐요. <a href="aiprivacy-ko.html">비밀 콩</a>을 지키려고 데려왔다면, 매일 <a href="llmops-ko.html">돌보는 일</a>까지 우리 몫이에요.',
                   'The perch and the caring cost money — compare it with the <a href="pricing-en.html">bean bill</a>. If you brought it home to keep <a href="aiprivacy-en.html">secret beans</a> safe, the daily <a href="llmops-en.html">caring</a> is yours too.')},
    ],
    "summary": (("<b>오픈 웨이트</b> = 앵무새 머릿속 <b>눈금(가중치)을 통째로 공개</b>해 누구나 <b>자기 횃대에 올릴 수 있는</b> 앵무새. 비밀 콩은 집에 남고 손보기는 자유지만, 횃대와 돌보기는 우리 몫이에요. '오픈'이 공짜도 오픈소스도 아니니 두루마리를 읽어요.",
                 "<b>Open weights</b> = a parrot whose <b>numbers (weights) are all published</b>, so anyone can <b>put it on their own perch</b>. Secret beans stay home and tweaking is free, but the perch and the caring are yours. Open is neither free nor open source — read the scroll."),
                ("Open-weight model. 학습된 파라미터(가중치) 파일을 공개해 누구나 내려받아 자기 서버에서 추론·파인튜닝·양자화할 수 있는 모델이에요(Llama, Mistral, Qwen 등). API 모델은 제공자 서버에서 토큰당 과금하고 데이터가 밖으로 나가요. 학습 데이터·코드까지 공개된 '오픈소스'와는 달라서, 라이선스마다 상업 이용·사용자 수·표기 조건이 다릅니다. 셀프 호스팅은 GPU 비용과 운영(LLMOps)이 따라와요.",
                 "A model whose trained parameters (weights) are published so anyone can download it and run inference, fine-tune, or quantize it on their own servers (Llama, Mistral, Qwen, etc.). API models run on the provider\'s servers, bill per token, and see your data. Unlike true open source, training data and code are usually withheld, and licenses vary on commercial use, user thresholds and attribution. Self-hosting brings GPU cost and operations (LLMOps) with it.")),
    "glossary": [
        ("오픈 웨이트", "Open weights", ("눈금을 통째로 공개한 앵무새.", "The parrot with its numbers published."), ("누구나 내려받아 자기 횃대에 올려요. Llama, Mistral, Qwen.", "Anyone can download it and put it on their own perch. Llama, Mistral, Qwen.")),
        ("가중치", "Weights", ("앵무새 머릿속 눈금.", "The numbers in the parrot\'s head."), ("수십억 개 숫자예요. 책을 읽으며 정해졌고, 이게 곧 앵무새예요.", "Billions of numbers, set while reading the books. They are the parrot.")),
        ("API 모델", "API model", ("창구로 만나는 빌린 앵무새.", "The borrowed parrot at the counter."), ('남의 집에 있고 물을 때마다 콩 값을 내요. → <a href="pricing-ko.html">콩 값</a>', 'Lives at their house; you pay beans per question. → <a href="pricing-en.html">the bean bill</a>')),
        ("셀프 호스팅", "Self-hosting", ("우리 집 횃대에 앵무새 올리기.", "Putting the parrot on our own perch."), ('횃대(GPU)를 사고, 매일 돌봐요. → <a href="llmops-ko.html">앵무새 돌보기</a>', 'Buy the perch (GPU) and care for it daily. → <a href="llmops-en.html">caring for the parrot</a>')),
        ("라이선스", "License", ("두루마리에 적힌 조건.", "The conditions on the scroll."), ("장사에 써도 되는지, 큰 회사는 허락이 필요한지, 이름을 적어야 하는지 — 새마다 달라요.", "Whether business use is allowed, whether big firms need permission, whether to credit the name — differs per bird.")),
        ("오픈소스와의 차이", "Open weights vs open source", ("눈금만 열림 vs 책 목록까지 열림.", "Numbers open vs books and recipe open too."), ("오픈 웨이트는 눈금만 공개해요. 어떤 책을 읽혔는지, 어떻게 가르쳤는지는 보통 비밀이에요.", "Open weights publish only the numbers. Which books it read and how it was taught usually stay secret.")),
        ("추론 서버", "Inference server", ("우리 횃대에서 답하게 하는 장치.", "What makes it answer on our perch."), ('값과 시간을 우리가 정해요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'We set its cost and speed. → <a href="inference-en.html">what answering costs and takes</a>')),
        ("양자화", "Quantization", ("콩을 굵게 세기.", "Counting beans coarsely."), ('우리 집 앵무새라서 할 수 있어요 — 작은 횃대에도 올라가요. → <a href="quantization-ko.html">콩을 굵게 세기</a>', 'Possible because it is your bird — it fits a smaller perch. → <a href="quantization-en.html">coarse counting</a>')),
    ],
}
