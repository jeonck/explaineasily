from _draw import *
from _world import *


def tag(x, y, text, color="var(--accent)", w=70):
    """질문에 붙은 좌표 딱지. 가운데 (x,y)."""
    return (f'<rect x="{x - w / 2}" y="{y - 10}" width="{w}" height="20" rx="5" fill="{color}"/>'
            f'<circle cx="{x - w / 2 + 7}" cy="{y}" r="2.5" fill="#FFF8E7"/>' + label(x + 3, y + 4, text, 10, "#FFF8E7"))


def page(x, y, w, h, lines, s=1.0):
    """책에서 뜯어 온 페이지 한 장. 크림 종이, 글자 #142033."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="{PAPER}" stroke="#C9A86A" stroke-width="2"/>'
    for i, t in enumerate(lines):
        out += label(w / 2, 18 + i * 16, t, 10, PAPER_INK)
    return out + "</g>"


def shelf(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="var(--stone)" opacity="0.5"/><rect x="{x}" y="{y + h - 8}" width="{w}" height="8" fill="var(--stone-dark)"/>'
            + "".join(f'<rect x="{x + 8 + i * 20}" y="{y + 12}" width="14" height="{h - 26}" rx="2" fill="{c}"/>'
                      for i, c in enumerate(("#2E7D6B", "#7B3FA0", "#C9822B", "#5B8DEF", "#B5382C")[: max(1, int((w - 12) // 20))])))


def arrow(x1, y1, x2, y2, color="var(--good)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"/>'
            f'<path d="M{x2 - 10} {y2 - 7} L{x2 + 2} {y2} L{x2 - 10} {y2 + 7}" stroke="{color}" stroke-width="3" fill="none"/>')


# 1. 손님이 '우리 회사 환불 규정'을 묻자, 앵무새는 읽은 적 없는데 그럴듯하게 답해요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, color=PARROT_BAD, talk=True)
         + bubble_parrot(50, 20, 310, 44, "⟦14일 안에 전액 환불이에요!|full refund within 14 days!⟧", 12, bad=True)
         + label(205, 105, "⟦(우리 규정은 7일이에요)|(our rule is actually 7 days)⟧", 12, "var(--bad)")
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(420, 30, 300, 40, "⟦우리 회사 환불 규정이 뭐야?|what is our company refund rule?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦그 규정집은 읽은 적이 없어요 — 그래도 그럴듯하게 답해요|it never read that rulebook — yet it answers plausibly⟧", 13, "var(--ink)"))

# 2. 왜: 앵무새가 읽은 책엔 우리 규정이 없고, 특훈으로 새 지식 넣기는 약해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + books(110, 210, 6, 1.1) + label(110, 236, "⟦앵무새가 읽은 책|the books it read⟧", 11, "var(--muted)")
         + '<rect x="200" y="120" width="70" height="90" rx="4" fill="#B5382C"/>' + label(235, 168, "⟦우리|our⟧", 11, "#FFF8E7") + label(235, 184, "⟦규정집|rulebook⟧", 11, "#FFF8E7")
         + label(235, 100, "⟦×|×⟧", 26, "var(--bad)", cls="d") + label(235, 236, "⟦여기 없어요|not in the pile⟧", 11, "var(--bad)")
         + parrot(360, 150, 1.0, mood="sweat") + label(360, 236, "⟦모르는데 이어 붙여요|continues without knowing⟧", 11, "var(--muted)")
         + person(470, 60, s=0.8, face=FROWN, **TRAINER) + note(540, 40, 190, 130, "⟦특훈으로 넣기?|DRILL IT IN?⟧", ("⟦새 사실은 잘 안 박혀요|new facts stick poorly⟧", "⟦규정이 바뀌면 또 특훈|rules change, drill again⟧", "⟦어디서 봤는지 몰라요|no idea where it came from⟧"), 0.95)
         + label(600, 210, "⟦특훈은 말버릇용이지, 새 지식용이 아니에요|the drill is for manners, not for new facts⟧", 11, "var(--ink)")
         + label(380, 288, "⟦읽은 책엔 없고, 특훈으로 넣기도 약해요|it is not in the books, and the drill barely helps⟧", 12, "var(--bad)"))

# 3. RAG = 답하기 전에 사서가 관련 페이지를 찾아 쟁반에 올려주기 (hero)
P3 = svg(360, sky(360)
         + person(20, 130, s=0.9, face=SMILE, **GUEST) + label(52, 250, "⟦손님|guest⟧", 11, "var(--muted)")
         + bubble(0, 40, 190, 40, "⟦환불 규정이 뭐야?|refund rule?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(130, 120, s=0.9, face=SMILE, **LIBRARIAN) + label(162, 250, "⟦사서|librarian⟧", 11, "var(--muted)")
         + page(210, 50, 130, 80, ("⟦규정집 12쪽|rulebook p.12⟧", "⟦7일 안에 환불|refund within 7 days⟧", "⟦영수증 필요|receipt required⟧", "⟦…|…⟧"))
         + label(275, 150, "⟦찾아온 페이지|the page found⟧", 11, "var(--good)", cls="d")
         + arrow(350, 90, 390, 90)
         + tray(400, 150, 210, 70, "⟦쟁반|tray⟧")
         + page(415, 108, 130, 80, ("⟦규정집 12쪽|rulebook p.12⟧", "⟦7일 안에 환불|refund within 7 days⟧"), 0.6)
         + bean(560, 185, 1.0, text="⟦질문|Q⟧")
         + label(505, 60, "⟦이걸 보고 답해|answer from this⟧", 12, "var(--ink)", cls="d")
         + arrow(612, 185, 640, 185)
         + parrot(690, 165, 1.1, talk=True)
         + bubble_parrot(560, 10, 190, 44, "⟦7일 안에 환불돼요|refund within 7 days⟧", 12)
         + label(690, 250, "⟦출처: 규정집 12쪽|source: rulebook p.12⟧", 11, "var(--good)", cls="d")
         + label(380, 340, "⟦RAG = 앵무새가 답하기 전에, 사서가 관련 페이지를 찾아 쟁반에 올려주는 것|RAG: before the parrot answers, the librarian finds the relevant page and puts it on the tray⟧", 13, "var(--ink)", cls="d"))

# 4. 흐름: 질문 → 딱지 → 서가 → 페이지 3장 → 쟁반 → 답 + 출처
STEPS = (("⟦① 질문|① question⟧", "⟦손님이 물어요|the guest asks⟧"), ("⟦② 딱지|② tag⟧", "⟦질문을 좌표로|question to coordinates⟧"),
         ("⟦③ 서가|③ shelf⟧", "⟦가까운 칸 찾기|find the near cell⟧"), ("⟦④ 페이지 3장|④ 3 pages⟧", "⟦가까운 순서로|closest first⟧"),
         ("⟦⑤ 쟁반|⑤ tray⟧", "⟦질문과 같이 올려요|placed with the question⟧"), ("⟦⑥ 답 + 출처|⑥ answer + source⟧", "⟦몇 쪽인지 같이|with the page number⟧"))
STEP_ART = (bubble(30, 80, 90, 34, "⟦환불?|refund?⟧", 11, "var(--panel)", "var(--line)", "bottom"),
            tag(195, 100, "⟦(3, 9)|(3, 9)⟧", "var(--good)", 70),
            shelf(275, 70, 90, 70),
            page(390, 66, 46, 60, ("⟦12쪽|p.12⟧",), 0.9) + page(404, 74, 46, 60, ("⟦31쪽|p.31⟧",), 0.9) + page(418, 82, 46, 60, ("⟦8쪽|p.8⟧",), 0.9),
            tray(510, 80, 100, 50) + bean(545, 108, 0.7) + page(568, 88, 30, 34, (), 0.9),
            parrot(675, 110, 0.8, talk=True))
P4 = svg(320, sky(320)
         + "".join(f'<rect x="{20 + i * 122}" y="40" width="110" height="200" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
                   + label(75 + i * 122, 62, t, 11, "var(--ink)", cls="d") + label(75 + i * 122, 176, d, 10, "var(--muted)")
                   + (arrow(132 + i * 122, 140, 140 + i * 122, 140) if i < 5 else "")
                   for i, (t, d) in enumerate(STEPS))
         + "".join(STEP_ART)
         + label(75, 200, "⟦→ 손님|→ guest⟧", 10, "var(--muted)") + label(441, 200, "⟦→ 쟁반|→ tray⟧", 10, "var(--muted)") + label(685, 200, "⟦12쪽 봤어요|see p.12⟧", 10, "var(--good)")
         + label(380, 300, "⟦쟁반은 콩이 한정돼서, 책 전체가 아니라 가까운 페이지 몇 장만 올려요|the tray holds only so many beans, so a few near pages go on — never the whole book⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 엉뚱한 페이지 → 엉뚱한 답. 페이지가 쟁반보다 크면 잘라야 해요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)" opacity="0.5"/>'
         + person(20, 90, s=0.9, face=FROWN, extra=SWEAT, **LIBRARIAN)
         + page(100, 50, 120, 70, ("⟦배송 규정 40쪽|shipping p.40⟧", "⟦3일 안에 도착|arrives in 3 days⟧"))
         + label(160, 140, "⟦엉뚱한 페이지|the wrong page⟧", 11, "var(--bad)", cls="d")
         + parrot(280, 110, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(230, 20, 140, 36, "⟦환불은 3일!|refund in 3 days!⟧", 11, bad=True)
         + label(190, 230, "⟦사서가 잘못 찾으면 앵무새도 잘못 답해요|a wrong page means a wrong answer⟧", 12, "var(--bad)")
         + label(190, 250, "⟦찾기 품질 = 답 품질|search quality is answer quality⟧", 11, "var(--muted)")
         + page(410, 40, 150, 150, ("⟦규정집 통째로|the whole rulebook⟧", "⟦…|…⟧", "⟦…|…⟧", "⟦…|…⟧", "⟦…|…⟧", "⟦…|…⟧", "⟦…|…⟧"))
         + tray(580, 120, 150, 60, "⟦쟁반|tray⟧")
         + '<path d="M568 60 L588 80 M588 60 L568 80" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(655, 100, "⟦쟁반보다 커요|bigger than the tray⟧", 11, "var(--bad)", cls="d")
         + label(570, 250, "⟦페이지가 쟁반보다 크면 잘라서 올려요|a page bigger than the tray gets cut down⟧", 12, "var(--ink)")
         + label(380, 300, "⟦사서가 잘 찾고, 페이지가 쟁반에 맞아야 앵무새가 잘 답해요|good finding plus a page that fits the tray — that is what makes a good answer⟧", 12, "var(--ink)", cls="d"))

TAG_I = icon('<path d="M10 16 h30 M10 26 h22" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><path d="M36 30 l10 10" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><rect x="24" y="40" width="34" height="16" rx="4" fill="var(--accent)"/><circle cx="31" cy="48" r="2" fill="#FFF8E7"/>')
PAGES_I = icon('<rect x="10" y="14" width="44" height="36" rx="3" fill="var(--stone)"/><rect x="18" y="8" width="20" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="30" y="16" width="20" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M20 54 h24" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')
TRAY_I = icon('<rect x="8" y="34" width="48" height="18" rx="6" fill="var(--stone)"/><rect x="18" y="14" width="20" height="24" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><ellipse cx="46" cy="32" rx="8" ry="5" fill="#C9822B"/>')
SRC_I = icon(f'<circle cx="24" cy="22" r="10" fill="{PARROT}"/><rect x="30" y="34" width="28" height="22" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><text x="44" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#142033">p.12</text>')

PAGE = {
    "slug": "rag", "order": 9,
    "title": ("사서가 찾아온 페이지", "The Page the Librarian Brought"),
    "h1": ("<em>RAG</em>가 뭐예요?", "What is <em>RAG</em>?"),
    "sub": ("RAG(검색 증강 생성)를 앵무새가 답하기 전에 사서가 관련 페이지를 찾아 쟁반에 올려주는 이야기로 풀어봤어요.",
            "Retrieval-augmented generation, told as a story about a librarian who finds the right page and puts it on the tray before the parrot answers."),
    "panels": [
        {"svg": P1, "alt": ("빨간 앵무새가 '14일 안에 전액 환불이에요!'라고 답하고, 아래에 '(우리 규정은 7일이에요)'. 손님이 '우리 회사 환불 규정이 뭐야?'라고 물음", "A red parrot answers full refund within 14 days!, with (our rule is actually 7 days) below. A guest asks what is our company refund rule?"),
         "caption": ("손님이 우리 회사 환불 규정을 물어요. 앵무새는 그 규정집을 읽은 적이 없어요.", "The guest asks about our company refund rule. The parrot never read that rulebook."),
         "small": ('그래도 그럴듯하게 답해요 — <a href="hallucination-ko.html">그럴듯 앵무새</a>예요.', 'Yet it answers plausibly — it is <a href="hallucination-en.html">the plausible parrot</a>.')},
        {"svg": P2, "alt": ("빨간 배경. 앵무새가 읽은 책 더미 옆에 '우리 규정집'이 ×표로 따로 있음. 땀 흘리는 앵무새. 조련사와 '특훈으로 넣기?' 쪽지: 새 사실은 잘 안 박혀요, 규정이 바뀌면 또 특훈, 어디서 봤는지 몰라요", "Red background. Beside the pile of books the parrot read, our rulebook sits apart with a ×. A sweating parrot. A trainer with a note titled drill it in?: new facts stick poorly, rules change so drill again, no idea where it came from"),
         "caption": ("읽은 책엔 우리 규정이 없어요. 특훈으로 새 지식을 넣기도 약해요.", "Our rule is not in its books. And drilling new facts in barely works."),
         "small": ('<a href="finetune-ko.html">짧은 특훈</a>은 말버릇용이지 새 사실용이 아니에요. 규정이 바뀔 때마다 특훈을 다시 할 수도 없고요.', 'The <a href="finetune-en.html">short drill</a> is for manners, not new facts. And you can\'t re-drill every time a rule changes.')},
        {"svg": P3, "hero": True, "alt": ("손님이 '환불 규정이 뭐야?' 묻자 사서가 규정집 12쪽 페이지를 찾아 쟁반에 올림. 쟁반엔 페이지와 질문 콩. 앵무새가 '7일 안에 환불돼요' 답하고 '출처: 규정집 12쪽'", "The guest asks refund rule?; the librarian finds rulebook page 12 and puts it on the tray with the question bean. The parrot answers refund within 7 days, with source: rulebook p.12"),
         "caption": ("RAG는 앵무새가 답하기 전에, 사서가 관련 페이지를 찾아 쟁반에 올려주는 거예요.", "RAG: before the parrot answers, the librarian finds the relevant page and puts it on the tray."),
         "small": ('앵무새를 다시 가르치지 않아요. 답할 때마다 <a href="context-ko.html">쟁반</a>에 페이지를 올려 주고 "이걸 보고 답해"라고 해요. 그러면 출처도 달 수 있어요.',
                   'The parrot is never retrained. Each time, a page goes on the <a href="context-en.html">tray</a> with the words answer from this. That way it can cite its source too.'),
         "tricks": (4, [
             (TAG_I, ("질문을 딱지로 바꿔요", "Turn the question into a tag"), ("뜻으로 찾으려고", "so it can be found by meaning"), "calm"),
             (PAGES_I, ("서가에서 가까운 페이지 몇 장", "A few near pages from the shelf"), ("책 전체가 아니라", "not the whole book")),
             (TRAY_I, ("쟁반에 올리고 '이걸 보고 답해'", "On the tray: answer from this"), ("질문과 나란히", "right beside the question"), "calm"),
             (SRC_I, ("답에 출처를 달아요", "Attach the source"), ("몇 쪽인지 같이", "with the page number"), "warm"),
         ])},
        {"svg": P4, "alt": ("여섯 칸 흐름: ① 질문 → ② 딱지 (3, 9) → ③ 서가 → ④ 페이지 3장(12쪽·31쪽·8쪽) → ⑤ 쟁반 → ⑥ 답 + 출처, 앵무새가 '12쪽 봤어요'", "A six-step flow: ① question → ② tag (3, 9) → ③ shelf → ④ 3 pages (p.12, p.31, p.8) → ⑤ tray → ⑥ answer + source, the parrot says see p.12"),
         "caption": ("질문이 딱지가 되고, 서가에서 가까운 페이지 몇 장이 쟁반으로 가요.", "The question becomes a tag, and a few near pages travel from the shelf to the tray."),
         "small": ('딱지는 <a href="embedding-ko.html">좌표 딱지</a>, 서가는 <a href="vectordb-ko.html">딱지로 정리한 서가</a>예요. 쟁반은 콩이 한정돼서 책 전체가 아니라 몇 장만 올려요.',
                   'The tag is the <a href="embedding-en.html">coordinate tag</a>; the shelf is <a href="vectordb-en.html">the shelf organized by tags</a>. The tray holds only so many beans, so just a few pages go on.')},
        {"svg": P5, "alt": ("왼쪽: 사서가 배송 규정 40쪽을 잘못 찾아오고 빨간 앵무새가 '환불은 3일!'이라 답함. 오른쪽: 규정집 통째로 페이지가 쟁반보다 커서 × 표시, '잘라서 올려요'", "Left: the librarian brings shipping page 40 by mistake and the red parrot answers refund in 3 days!. Right: the whole rulebook is bigger than the tray, marked ×, cut it down"),
         "caption": ("사서가 엉뚱한 페이지를 가져오면 앵무새도 엉뚱하게 답해요. 페이지가 쟁반보다 크면 잘라야 해요.", "If the librarian brings the wrong page, the parrot answers wrongly. And a page bigger than the tray must be cut down."),
         "small": ('찾기 품질이 곧 답 품질이에요. 그리고 페이지가 <a href="context-ko.html">쟁반</a>에 맞아야 해요. 그래도 답이 틀릴 수 있으니 출처를 확인해요 — <a href="hallucination-ko.html">그럴듯 앵무새</a>는 사라지지 않아요.',
                   'Search quality is answer quality. And the page has to fit the <a href="context-en.html">tray</a>. The answer can still be wrong, so check the source — <a href="hallucination-en.html">the plausible parrot</a> never fully goes away.')},
    ],
    "summary": (("<b>RAG</b> = 앵무새가 답하기 전에 <b>사서가 관련 페이지를 찾아 쟁반에 올려주는 것</b>. 앵무새를 다시 가르치지 않고도 <b>우리 책</b>으로 답하게 하고, <b>출처</b>를 달 수 있어요. 사서가 잘못 찾으면 답도 틀려요.",
                 "<b>RAG</b> = before the parrot answers, <b>the librarian finds the relevant page and puts it on the tray</b>. No retraining, yet it answers from <b>our books</b> and can <b>cite sources</b>. If the librarian finds the wrong page, the answer is wrong too."),
                ("Retrieval-Augmented Generation. 질문을 임베딩으로 바꿔 벡터 DB 에서 관련 청크를 검색(retriever)하고, 리랭킹으로 줄 세운 뒤 컨텍스트 창에 넣어 LLM 이 그 근거로 답하게 하는 방식이에요. 파인튜닝과 달리 지식을 모델 밖에 두어 갱신이 쉽고 인용이 가능해요. 검색 품질과 청킹이 답 품질을 좌우하고, 할루시네이션은 줄지만 없어지진 않아요.",
                 "The question is embedded, a retriever pulls related chunks from a vector DB, a reranker orders them, and they go into the context window so the LLM answers from that evidence. Unlike fine-tuning, knowledge lives outside the model, so it is easy to update and can be cited. Retrieval quality and chunking decide answer quality; hallucination drops but never vanishes.")),
    "glossary": [
        ("RAG", "RAG", ("사서가 찾아온 페이지.", "The page the librarian brought."), ("검색 증강 생성. 찾아서(검색) 쟁반에 올리고(증강) 답해요(생성).", "Retrieval-augmented generation: find it, put it on the tray, then answer.")),
        ("검색기", "Retriever", ("사서.", "The librarian."), ("질문 딱지로 서가에서 가까운 페이지를 꺼내 오는 부분.", "The part that takes the question tag and pulls near pages from the shelf.")),
        ("청킹", "Chunking", ("책을 페이지로 자르기.", "Cutting the book into pages."), ("쟁반에 올릴 만한 크기로 미리 잘라 서가에 꽂아요. 너무 크면 안 들어가고, 너무 작으면 앞뒤가 잘려요.", "Pre-cut to tray size before shelving. Too big won\'t fit; too small loses the surrounding context.")),
        ("리랭킹", "Reranking", ("찾아온 페이지 다시 줄 세우기.", "Re-ordering the pages found."), ("서가에서 10장 꺼낸 뒤 진짜 관련 있는 순서로 다시 정렬해 3장만 올려요.", "Pull 10 from the shelf, re-sort by true relevance, put only 3 on the tray.")),
        ("근거 인용", "Citation", ("답에 붙이는 출처.", "The source attached to the answer."), ("몇 쪽에서 봤는지 같이 말해요. 손님이 확인할 수 있어요.", "It says which page it came from, so the guest can check.")),
        ("컨텍스트 창", "Context window", ("쟁반.", "The tray."), ('찾아온 페이지가 올라가는 곳. 크기가 정해져 있어요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'Where the found pages go. It has a fixed size. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("파인튜닝과의 차이", "vs. fine-tuning", ("특훈은 말버릇, RAG 는 지식.", "The drill is manners; RAG is knowledge."), ('새 사실은 쟁반에 올리고, 말투는 특훈으로 고쳐요. → <a href="finetune-ko.html">짧은 특훈</a>', 'New facts go on the tray; tone gets fixed by drilling. → <a href="finetune-en.html">the short drill</a>')),
        ("할루시네이션", "Hallucination", ("그럴듯한 거짓말.", "The plausible lie."), ('페이지를 줘도 줄어들 뿐 사라지진 않아요. → <a href="hallucination-ko.html">그럴듯 앵무새</a>', 'Giving it the page reduces it but never removes it. → <a href="hallucination-en.html">the plausible parrot</a>')),
    ],
}
