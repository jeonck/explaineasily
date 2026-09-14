from _draw import *
from _world import *

ARROW = '<path d="M{x0} {y} L{x1} {y}" stroke="var(--muted)" stroke-width="3"/><path d="M{ax} {ay0} L{x1} {y} L{ax} {ay1}" stroke="var(--muted)" stroke-width="3" fill="none"/>'


def arrow(x0, x1, y):
    return ARROW.format(x0=x0, x1=x1, y=y, ax=x1 - 8, ay0=y - 6, ay1=y + 6)


def box(x, y, w, h, title, sub, fill="var(--panel)"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="var(--stone-dark)" stroke-width="2"/>'
            + label(x + w / 2, y + h / 2 - 2, title, 13, "var(--ink)", cls="d") + label(x + w / 2, y + h + 18, sub, 10, "var(--muted)"))


# 1. 앵무새는 어디서 왔나 — 알에서 나온 앵무새는 콩 하나도 못 이어요
EGG = '<path d="M120 235 q-22 -6 -18 -30 l12 8 l8 -10 l8 10 l10 -8 q4 24 -20 30z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
P1 = svg(300, sky(300)
         + EGG + parrot(200, 175, 0.7, mood="sweat") + label(170, 262, "⟦갓 나온 앵무새|a just-hatched parrot⟧", 11, "var(--muted)")
         + bubble_parrot(150, 60, 120, 36, "⟦…?|…?⟧", 14)
         + beans(330, 150, ("⟦오늘|Today⟧", "⟦날씨가|the⟧"), 1.0, 60)
         + '<rect x="424" y="128" width="52" height="44" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(450, 156, "⟦?|?⟧", 22, "var(--accent)", cls="d")
         + person(560, 110, s=0.9, face=EYES, **TRAINER) + bubble(480, 30, 230, 40, "⟦다음 콩을 이어 봐!|continue the beans!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦알에서 나온 앵무새는 콩 하나도 못 이어요 — 말 잘하는 앵무새는 어디서 왔을까요?|a hatchling can\'t continue a single bean — so where does a talking parrot come from?⟧", 12, "var(--ink)"))

# 2. 왜 큰 일인가: 책 산더미를 통째로 읽히려면 큰 학교, 몇 달, 큰돈
RACK = "".join(f'<rect x="{300 + (i % 6) * 26}" y="{90 + (i // 6) * 22}" width="20" height="16" rx="3" fill="var(--stone-dark)"/><circle cx="{317 + (i % 6) * 26}" cy="{98 + (i // 6) * 22}" r="2" fill="var(--good)"/>' for i in range(24))
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + books(110, 250, 8, 1.2) + label(110, 272, "⟦책 산더미|a mountain of books⟧", 11, "var(--muted)")
         + arrow(170, 250, 150)
         + '<rect x="280" y="60" width="200" height="180" rx="8" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M270 60 L380 20 L490 60 Z" fill="var(--stone-dark)"/>'
         + label(380, 80, "⟦앵무새 학교|PARROT SCHOOL⟧", 12, "var(--ink)", cls="d") + RACK + label(380, 186, "⟦계산기 수천 대가 밤낮으로|thousands of calculators, nonstop⟧", 10, "var(--muted)")
         + parrot(380, 215, 0.55) + dial(560, 100, 0.9, 0.95, "⟦전기 계량기|power meter⟧")
         + note(620, 60, 120, 80, "⟦달력|CALENDAR⟧", ("⟦1월 → 4월|Jan → Apr⟧", "⟦몇 달째…|months…⟧"), 0.95)
         + label(650, 200, "⟦$$$ 큰돈|$$$ a lot of money⟧", 13, "var(--bad)", cls="d")
         + label(380, 282, "⟦책을 통째로 읽히는 건 큰 학교와 몇 달과 큰돈이 드는 일이에요|reading it all takes a big school, months, and a lot of money⟧", 12, "var(--bad)"))

# 3. 사전 학습 = 다음 콩 맞히기 문제를 수조 번 풀리는 것 (hero)
LOOP = ('<path d="M692 125 L740 125 L740 262 L40 262 L40 130 L58 130" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="7 5"/>'
        '<path d="M50 122 L60 130 L50 138" stroke="var(--accent)" stroke-width="3" fill="none"/>')
P3 = svg(360, sky(360)
         + beans(80, 130, ("⟦오늘|Today⟧", "⟦날씨가|the⟧"), 1.0, 60)
         + '<rect x="176" y="112" width="52" height="40" rx="8" fill="var(--stone-dark)"/>' + label(202, 138, "⟦?|?⟧", 20, "#FFF8E7", cls="d")
         + label(155, 230, "⟦① 책 한 줄, 다음 콩을 가려요|① a line from a book, next bean covered⟧", 10, "var(--ink)")
         + arrow(240, 275, 130)
         + parrot(330, 140, 1.0, talk=True) + bubble_parrot(280, 40, 110, 36, "⟦좋다!|nice!⟧", 12)
         + label(330, 230, "⟦② 앵무새가 맞혀요|② the parrot guesses⟧", 10, "var(--ink)")
         + arrow(390, 425, 130)
         + note(440, 90, 120, 80, "⟦채점|SCORE⟧", ("⟦답: 좋다 ✓|answer: nice ✓⟧", "⟦틀린 정도: 조금|off by: a bit⟧"), 0.95)
         + label(500, 230, "⟦③ 책의 진짜 답과 비교|③ compare with the book⟧", 10, "var(--ink)")
         + arrow(570, 615, 130)
         + dial(660, 125, 1.0, 0.55, "⟦머릿속 눈금|inner dials⟧")
         + label(660, 230, "⟦④ 눈금을 조금 고쳐요|④ nudge the dials a little⟧", 10, "var(--ink)")
         + LOOP + label(395, 285, "⟦다시! 문제는 늘 '다음 콩은?' — 1,000,000,000,000 번|again! the question is always which bean is next — a trillion times⟧", 11, "var(--accent)", cls="d")
         + label(380, 340, "⟦사전 학습 = 답을 가르치지 않고, 책을 가리고 다음 콩을 맞히게 하는 학교|pre-training: a school that hides the book and makes the parrot guess the next bean — nobody teaches the answers⟧", 12, "var(--ink)", cls="d"))

# 4. 더 많이 읽고 더 크면 잘해요 + 학교 뒤에는 특훈과 예절 교육
P4 = svg(320, sky(320)
         + label(205, 60, "⟦더 많이 읽고, 더 크면 → 더 잘 맞혀요|more books, bigger bird → better guesses⟧", 12, "var(--ink)")
         + books(80, 272, 2, 1.0) + parrot(80, 175, 0.7)
         + books(200, 272, 4, 1.0) + parrot(200, 150, 0.95)
         + books(330, 272, 7, 1.0) + parrot(330, 120, 1.2, color=PARROT_BIG)
         + label(585, 60, "⟦학교 뒤에는|after school⟧", 12, "var(--ink)")
         + box(430, 90, 90, 60, "⟦학교|SCHOOL⟧", "⟦다음 콩 맞히기|guess next bean⟧", "var(--accent-soft)") + arrow(522, 538, 120)
         + box(540, 90, 90, 60, "⟦특훈|DRILL⟧", "⟦말버릇 고치기|fix its manners⟧") + arrow(632, 648, 120)
         + box(650, 90, 90, 60, "⟦예절|MANNERS⟧", "⟦원하는 대로 답하기|answer as wanted⟧")
         + label(585, 200, "⟦학교는 길고 비싸고, 뒤의 둘은 짧아요|school is long and costly; the two after are short⟧", 11, "var(--muted)")
         + label(380, 300, "⟦학교가 끝이 아니에요 — 뒤에 짧은 특훈과 예절 교육이 와요|school is not the end — a short drill and manners lessons follow⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 학교만 마친 앵무새는 예절·지시를 몰라요 + 책을 덮은 날 이후는 몰라요
SHELF = ('<rect x="560" y="120" width="160" height="6" fill="#5A3B22"/><rect x="560" y="176" width="160" height="6" fill="#5A3B22"/>'
         + "".join(f'<rect x="{566 + i * 18}" y="{130 + (i % 2) * 4}" width="14" height="{46 - (i % 2) * 4}" rx="2" fill="{c}"/>' for i, c in enumerate(("#7B3FA0", "#2E7D6B", "#C9822B", "#5B8DEF")))
         + "".join(f'<rect x="{644 + i * 18}" y="130" width="14" height="46" rx="2" fill="none" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 3"/>' for i in range(4)))
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/><path d="M380 20 V300" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 5"/>'
         + person(40, 100, s=0.85, face=EYES, **GUEST) + bubble(20, 30, 170, 36, "⟦이거 요약해 줘|summarize this⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + parrot(250, 160, 1.0, talk=True) + bubble_parrot(200, 62, 170, 36, "⟦요약이란 무엇인가…|a summary is defined as…⟧", 11)
         + label(190, 245, "⟦말은 잘 잇지만 시키는 건 몰라요|continues well, but doesn\'t follow orders⟧", 11, "var(--ink)")
         + label(190, 267, "⟦→ 예절 교육이 필요해요|→ needs manners lessons⟧", 11, "var(--bad)")
         + note(410, 40, 120, 70, "⟦달력|CALENDAR⟧", ("⟦6월 ■ 책 덮음|Jun ■ closed⟧",), 0.9)
         + parrot(470, 190, 1.0, mood="sweat") + SHELF + label(600, 110, "⟦7월부터는 빈 서가|shelves empty from July⟧", 11, "var(--bad)")
         + label(570, 245, "⟦책을 덮은 날 뒤의 일은 몰라요|it doesn\'t know what came after⟧", 11, "var(--ink)")
         + label(570, 267, "⟦→ 그건 사서가 찾아와요|→ the librarian brings that⟧", 11, "var(--bad)")
         + label(380, 300, "⟦학교만 마친 앵무새 — 말은 잘 잇고, 예절과 최근 일은 몰라요|fresh out of school: continues well, knows no manners and nothing recent⟧", 12, "var(--ink)", cls="d"))

NEXT_I = icon(f'<ellipse cx="14" cy="34" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="34" cy="34" rx="10" ry="7" fill="{BEAN}"/><rect x="44" y="24" width="16" height="20" rx="4" fill="var(--stone-dark)"/><text x="52" y="39" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF8E7">?</text>')
DIAL_I = icon('<circle cx="32" cy="34" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 L44 20" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="3" fill="var(--accent)"/><path d="M48 10 q10 8 6 20" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M50 26 l4 4 l4 -6" stroke="var(--good)" stroke-width="3" fill="none"/>')
PILE_I = icon('<rect x="8" y="46" width="48" height="8" rx="2" fill="#7B3FA0"/><rect x="12" y="36" width="48" height="8" rx="2" fill="#2E7D6B"/><rect x="8" y="26" width="48" height="8" rx="2" fill="#C9822B"/><rect x="12" y="16" width="48" height="8" rx="2" fill="#5B8DEF"/><rect x="8" y="6" width="48" height="8" rx="2" fill="#B5382C"/>')
AFTER_I = icon('<rect x="4" y="22" width="16" height="20" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="26" y="22" width="14" height="20" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/><rect x="46" y="22" width="14" height="20" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/><path d="M20 32 h5 M40 32 h5" stroke="var(--muted)" stroke-width="2"/>')

PAGE = {
    "slug": "pretraining", "order": 32,
    "title": ("책 읽는 학교", "The School of Reading"),
    "h1": ("<em>사전 학습</em>이 뭐예요?", "What is <em>Pre-training</em>?"),
    "sub": ("사전 학습을 책을 가리고 다음 콩을 맞히는 문제를 수조 번 풀리는 앵무새 학교 이야기로 풀어봤어요.",
            "Pre-training, told as a story about a parrot school that hides the book and makes the parrot guess the next bean, a trillion times over."),
    "panels": [
        {"svg": P1, "alt": ("깨진 알 옆 작은 앵무새가 땀 흘리며 '…?'. 콩 '오늘 날씨가' 다음 물음표 상자. 조련사가 '다음 콩을 이어 봐!'", "A small parrot beside a cracked egg sweats and says …?; beans reading Today the, then a question box; a trainer says continue the beans!"),
         "caption": ("알에서 나온 앵무새는 콩 하나도 못 이어요.", "A just-hatched parrot can\'t continue a single bean."),
         "small": ("말 잘하는 앵무새는 어디서 왔을까요? 책을 산더미로 읽었다고 했죠 — 그 읽기는 어떻게 하는 걸까요?", "So where does a talking parrot come from? We said it read a mountain of books — but how does that reading work?")},
        {"svg": P2, "alt": ("책 산더미가 화살표로 '앵무새 학교' 건물로 들어감. 건물 안에 초록 불 켜진 계산기 스물네 대. 옆에 끝까지 올라간 전기 계량기, '1월 → 4월, 몇 달째' 달력, '$$$ 큰돈'", "A mountain of books flows into a Parrot School building filled with twenty-four calculators with green lights; beside it a maxed-out power meter, a calendar reading Jan to Apr, months, and $$$ a lot of money"),
         "caption": ("책을 통째로 읽히는 건 큰 학교와 몇 달과 큰돈이 드는 일이에요.", "Reading it all takes a big school, months, and a lot of money."),
         "small": ("계산기 수천 대가 밤낮으로 돌아요. 전기 계량기는 끝까지 올라가고, 달력은 몇 장씩 넘어가요. 그래서 큰 앵무새는 몇 곳에서만 길러요.", "Thousands of calculators run day and night. The power meter maxes out and the calendar flips for months. That is why only a few places raise big parrots.")},
        {"svg": P3, "hero": True, "alt": ("네 단계 고리: ① 책 한 줄 '오늘 날씨가'에서 다음 콩을 가림 ② 앵무새가 '좋다!'고 맞힘 ③ 채점 쪽지 '답: 좋다 ✓, 틀린 정도: 조금' ④ 머릿속 눈금 다이얼을 조금 고침, 점선 화살표로 처음으로 돌아가 '다시! 1조 번'", "A four-step loop: a book line Today the with the next bean covered; the parrot guesses nice!; a score note reads answer: nice ✓, off by a bit; inner dials get a small nudge; a dashed arrow loops back — again, a trillion times"),
         "caption": ("사전 학습은 답을 가르치지 않고, 책을 가리고 다음 콩을 맞히게 하는 학교예요.", "Pre-training is a school that hides the book and makes the parrot guess the next bean — nobody teaches the answers."),
         "small": ('책 자체가 정답표예요. 틀리면 머릿속 눈금을 조금 고치고, 다음 줄로 넘어가요. 이걸 수조 번 하면 <a href="llm-ko.html">책 산더미 앵무새</a>가 돼요. 학교 뒤엔 <a href="finetune-ko.html">특훈</a>과 <a href="alignment-ko.html">예절 교육</a>이 이어져요.',
                   'The book itself is the answer key. When it is wrong, its inner dials get a small nudge and it moves to the next line. Do that a trillion times and you get the <a href="llm-en.html">mountain-of-books parrot</a>. A <a href="finetune-en.html">drill</a> and <a href="alignment-en.html">manners lessons</a> follow.'),
         "tricks": (4, [
             (NEXT_I, ("문제는 늘 '다음 콩은?'", "Always: which bean is next?"), ("답은 책에 이미 있어요", "the book already holds the answer"), "calm"),
             (DIAL_I, ("틀리면 눈금을 조금", "Wrong? nudge the dials"), ("아주 조금씩, 아주 많이", "tiny nudges, very many"), "calm"),
             (PILE_I, ("책이 많고 좋을수록", "More and better books"), ("앵무새도 클수록", "and a bigger bird"), "calm"),
             (AFTER_I, ("학교 뒤에 특훈·예절", "Then drill and manners"), ("학교만으론 안 끝나요", "school alone is not the end"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 책 두 권과 작은 앵무새, 책 네 권과 보통 앵무새, 책 일곱 권과 큰 앵무새 — 더 많이 읽고 더 크면 더 잘 맞힘. 오른쪽: 학교 → 특훈 → 예절 상자 세 개", "Left: two books with a small parrot, four with a medium one, seven with a big one — more books and a bigger bird guess better. Right: three boxes, school → drill → manners"),
         "caption": ("더 많이 읽고 더 크면 더 잘 맞혀요. 그리고 학교가 끝이 아니에요.", "More books and a bigger bird guess better. And school is not the end."),
         "small": ('책·크기·계산을 함께 키우면 앵무새가 꾸준히 좋아져요 — 한 줄로 말하면 크게, 많이 = 잘함. 학교가 끝나면 <a href="finetune-ko.html">짧은 특훈</a>으로 말버릇을, <a href="alignment-ko.html">예절 교육</a>으로 태도를 고쳐요.',
                   'Grow the books, the bird and the computing together and the parrot keeps improving — in one line: bigger and more means better. After school, a <a href="finetune-en.html">short drill</a> fixes its habits and <a href="alignment-en.html">manners lessons</a> fix its attitude.')},
        {"svg": P5, "alt": ("왼쪽: 손님이 '이거 요약해 줘' 하니 앵무새가 '요약이란 무엇인가…'라고 딴소리 — 예절 교육 필요. 오른쪽: '6월 책 덮음' 달력, 7월부터 빈 서가, 땀 흘리는 앵무새 — 그건 사서가 찾아옴", "Left: a guest says summarize this and the parrot rambles a summary is defined as… — needs manners lessons. Right: a calendar marked Jun books closed, empty shelves from July, a sweating parrot — the librarian brings that"),
         "caption": ("학교만 마친 앵무새는 말은 잘 잇지만, 예절도 모르고 최근 일도 몰라요.", "Fresh out of school, the parrot continues well but knows no manners and nothing recent."),
         "small": ('시키는 대로 하는 법은 <a href="alignment-ko.html">예절 교육</a>에서 배워요. 책을 덮은 날 뒤의 일은 <a href="knowledgecutoff-ko.html">책을 덮은 날</a> 이야기에서 — 그건 학교가 아니라 사서가 채워요.',
                   'Doing what it is told comes from <a href="alignment-en.html">manners lessons</a>. What happened after it closed the books is in <a href="knowledgecutoff-en.html">the day it closed the books</a> — that gap is filled by the librarian, not the school.')},
    ],
    "summary": (("<b>사전 학습</b> = 앵무새 학교에서 책을 가리고 <b>다음 콩 맞히기</b>를 <b>수조 번</b> 풀리는 것. 답을 가르치지 않고 <b>책 자체가 정답표</b>예요. 틀리면 <b>눈금을 조금</b> 고쳐요. 책이 많고 새가 클수록 잘하지만, 학교 뒤에 <b>특훈과 예절 교육</b>이 있어야 해요.",
                 "<b>Pre-training</b> = the parrot school hides the book and has it <b>guess the next bean</b> <b>a trillion times</b>. Nobody teaches answers — <b>the book is the answer key</b>. Wrong guesses <b>nudge the dials</b>. More books and a bigger bird do better, but a <b>drill and manners lessons</b> must follow."),
                ("Pre-training. 방대한 텍스트 코퍼스로 다음 토큰 예측을 자기지도 학습하는 단계예요. 예측과 실제 토큰의 차이(손실)를 줄이도록 경사 하강으로 파라미터를 조금씩 갱신해요. GPU 수천 대로 수주~수개월, 큰 비용이 들고, 데이터·파라미터·연산을 함께 키우면 성능이 예측 가능하게 오르는 스케일링 법칙이 있어요. 이후 파인튜닝과 정렬(RLHF 등)이 이어져요.",
                 "The stage where a model learns next-token prediction on a huge text corpus by self-supervision. Gradient descent nudges the parameters to reduce the loss — the gap between prediction and the real token. It takes thousands of GPUs, weeks to months and a lot of money; scaling laws say performance rises predictably when data, parameters and compute grow together. Fine-tuning and alignment (RLHF and the like) follow.")),
    "glossary": [
        ("사전 학습", "Pre-training", ("책 읽는 학교.", "The school of reading."), ("다음 콩 맞히기를 수조 번. 말 잘하는 앵무새는 여기서 나와요.", "Guess the next bean, a trillion times. Talking parrots come from here.")),
        ("자기지도 학습", "Self-supervised learning", ("책을 가리고 맞히기.", "Cover the book and guess."), ("사람이 답을 적어 주지 않아요. 책 다음 줄이 그대로 정답이에요.", "No one writes the answers. The next line of the book is the answer.")),
        ("학습 데이터 · 코퍼스", "Training data · Corpus", ("학교의 책 산더미.", "The school\'s mountain of books."), ("많고 깨끗할수록 앵무새가 좋아져요. 나쁜 책도 섞이면 나쁜 말도 배워요.", "More and cleaner books make a better parrot. Bad books mixed in teach bad words too.")),
        ("손실", "Loss", ("틀린 정도.", "How far off it was."), ("채점 쪽지의 숫자. 학교는 이 숫자를 줄이는 쪽으로만 눈금을 고쳐요.", "The number on the score note. The school only turns the dials to make it smaller.")),
        ("스케일링 법칙", "Scaling laws", ("크게, 많이 = 잘함.", "Bigger and more means better."), ("책·새·계산을 같이 키우면 얼마나 좋아질지 미리 셈이 돼요.", "Grow books, bird and computing together and the gain can be predicted ahead.")),
        ("GPU · 학습 비용", "GPUs · Training cost", ("계산기 수천 대와 전기 계량기.", "Thousands of calculators and the power meter."), ("몇 달, 큰돈. 그래서 큰 앵무새 학교는 몇 곳뿐이에요.", "Months and a lot of money. That is why big parrot schools are few.")),
        ("파인튜닝", "Fine-tuning", ("학교 뒤의 짧은 특훈.", "The short drill after school."), ('말버릇과 특기를 고쳐요. → <a href="finetune-ko.html">짧은 특훈</a>', 'Fixes habits and adds a specialty. → <a href="finetune-en.html">the short drill</a>')),
        ("지식 컷오프", "Knowledge cutoff", ("책을 덮은 날.", "The day it closed the books."), ('그 뒤 일은 학교에서 못 배웠어요. → <a href="knowledgecutoff-ko.html">책을 덮은 날</a>', 'Nothing after that day was in school. → <a href="knowledgecutoff-en.html">the day it closed the books</a>')),
    ],
}
