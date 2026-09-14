from _draw import *
from _world import *


def shelf(x, y, w, filled, empty):
    """서가 한 칸. filled 권은 색 책, empty 권은 점선 빈칸."""
    cols = ("#7B3FA0", "#2E7D6B", "#C9822B", "#5B8DEF", "#B5382C")
    out = f'<rect x="{x}" y="{y - 10}" width="{w}" height="6" fill="#5A3B22"/><rect x="{x}" y="{y + 46}" width="{w}" height="6" fill="#5A3B22"/>'
    out += "".join(f'<rect x="{x + 6 + i * 18}" y="{y + (i % 2) * 4}" width="14" height="{46 - (i % 2) * 4}" rx="2" fill="{cols[i % 5]}"/>' for i in range(filled))
    out += "".join(f'<rect x="{x + 6 + (filled + i) * 18}" y="{y}" width="14" height="46" rx="2" fill="none" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 3"/>' for i in range(empty))
    return out


def flag(x, y0, y1, text):
    return (f'<path d="M{x} {y0} V{y1}" stroke="var(--bad)" stroke-width="3"/><path d="M{x} {y0} l40 12 l-40 12z" fill="var(--bad)"/>'
            + label(x, y0 - 10, text, 12, "var(--bad)", cls="d"))


# 1. "올해 우승팀?" → 앵무새가 작년 팀을 자신 있게 말해요
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=EYES, **GUEST) + bubble(20, 30, 250, 40, "⟦올해 우승팀이 어디야?|who won this year?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + perch(480, 200, 140) + parrot(480, 160, 1.1, color=PARROT_BAD, talk=True)
         + bubble_parrot(340, 30, 280, 40, "⟦파란 팀이요! 확실해요!|the Blue team! definitely!⟧", 12, bad=True)
         + label(480, 250, "⟦(그건 작년 우승팀이에요)|(that was last year\'s winner)⟧", 11, "var(--bad)")
         + label(380, 282, "⟦앵무새가 작년 팀을 올해 팀처럼 자신 있게 말해요|the parrot names last year\'s team as confidently as if it were this year\'s⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새 학교는 어느 날 책을 덮어요 — 그날 이후 책은 안 읽었어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(40, 40, 170, 130, "⟦학교 달력|SCHOOL CALENDAR⟧", ("⟦1월 2월 3월 4월|Jan Feb Mar Apr⟧", "⟦5월 6월 ■ 책 덮음|May Jun ■ closed⟧", "⟦7월 8월 9월 …|Jul Aug Sep …⟧"), 1.0, 1)
         + label(125, 200, "⟦6월에 책을 덮었어요|it closed the books in June⟧", 11, "var(--bad)")
         + shelf(260, 100, 220, 6, 5) + label(315, 175, "⟦6월까지 읽은 책|read up to June⟧", 11, "var(--ink)") + label(440, 175, "⟦그 뒤는 빈칸|blank after that⟧", 11, "var(--bad)")
         + parrot(620, 130, 1.1, mood="sweat") + label(620, 220, "⟦7월부터는 아무것도 몰라요|knows nothing from July on⟧", 11, "var(--muted)")
         + label(380, 282, "⟦학교는 어느 날 책을 덮어요 — 그날 뒤에 나온 책은 읽은 적이 없어요|one day the school closes the books — nothing printed after that day was ever read⟧", 12, "var(--bad)"))

# 3. 지식 컷오프 = 앵무새가 책을 덮은 날 (hero)
P3 = svg(360, sky(360)
         + note(40, 50, 200, 160, "⟦달력|CALENDAR⟧", ("⟦1월 2월 3월|Jan Feb Mar⟧", "⟦4월 5월 [6월]|Apr May [Jun]⟧", "⟦7월? 8월? 9월?|Jul? Aug? Sep?⟧"), 1.0, 1)
         + label(140, 236, "⟦책을 덮은 날 = 6월|closed the books in June⟧", 12, "var(--bad)", cls="d")
         + perch(340, 250, 130) + parrot(340, 210, 1.3, talk=True)
         + bubble_parrot(255, 80, 180, 40, "⟦6월까지는 잘 알아요|I know up to June⟧", 12)
         + person(520, 130, s=0.9, face=EYES, **GUEST) + bubble(450, 40, 200, 40, "⟦9월엔 무슨 일 있었어?|what happened in September?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(600, 252, "⟦9월 일은 몰라요|it doesn\'t know September⟧", 11, "var(--ink)")
         + label(600, 272, "⟦모른다고 안 하고 이어 붙일 수도 있어요|and may continue instead of saying so⟧", 11, "var(--bad)")
         + label(380, 344, "⟦지식 컷오프 = 앵무새가 책을 덮은 날. 그 뒤 일은 몰라요|the knowledge cutoff is the day the parrot closed its books — it knows nothing after⟧", 12, "var(--ink)", cls="d"))

# 4. 시간선: 덮은 날 왼쪽은 책, 오른쪽은 빈칸 — 빈칸은 사서가 새 신문으로 채워요
TICKS = "".join(f'<path d="M{x} 184 V196" stroke="var(--stone-dark)" stroke-width="2"/>' for x in range(80, 720, 80))
P4 = svg(320, sky(320)
         + '<path d="M50 190 H720" stroke="var(--stone-dark)" stroke-width="4"/><path d="M712 182 L722 190 L712 198" stroke="var(--stone-dark)" stroke-width="4" fill="none"/>' + TICKS
         + books(120, 182, 3, 0.8) + books(250, 182, 3, 0.8) + label(185, 125, "⟦여기까지는 읽었어요|read up to here⟧", 11, "var(--ink)")
         + flag(400, 110, 190, "⟦책을 덮은 날|the day it closed the books⟧")
         + "".join(f'<rect x="{460 + i * 80}" y="140" width="60" height="40" rx="6" fill="none" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 4"/>' + label(490 + i * 80, 166, "⟦?|?⟧", 16, "var(--bad)", cls="d") for i in range(3))
         + label(570, 125, "⟦그 뒤는 빈칸|blank after that⟧", 11, "var(--bad)")
         + tray(300, 215, 250, 55) + note(320, 220, 120, 60, "⟦신문|NEWS⟧", ("⟦9월 우승팀|Sep champion⟧",), 0.7)
         + label(480, 258, "⟦쟁반에|on the tray⟧", 11, "var(--muted)")
         + person(560, 195, s=0.7, face=SMILE, **LIBRARIAN) + label(620, 218, "⟦사서가 새 신문을|the librarian brings⟧", 10, "var(--ink)", "start") + label(620, 234, "⟦쟁반에 올려요|fresh news to the tray⟧", 10, "var(--ink)", "start")
         + '<path d="M556 240 L500 240" stroke="var(--good)" stroke-width="3"/><path d="M508 234 L498 240 L508 246" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(380, 300, "⟦덮은 날 뒤의 빈칸은 학교가 아니라 사서와 도구가 채워요|the blank after that day is filled by the librarian and tools, not by school⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 덮은 날 이전이라고 다 아는 것도 아니에요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + books(90, 200, 7, 1.0) + label(90, 222, "⟦책에 많이 실린 일|in many books⟧", 11, "var(--muted)")
         + parrot(240, 140, 1.0, talk=True) + bubble_parrot(150, 46, 200, 40, "⟦작년 우승은 파란 팀!|last year: the Blue team!⟧", 11)
         + label(190, 262, "⟦덮은 날 전 + 책에 많이 → 잘 알아요|before the day and in many books → knows it well⟧", 11, "var(--good)")
         + books(470, 200, 1, 1.0) + label(470, 222, "⟦책에 한 줄만 실린 일|one line in one book⟧", 11, "var(--muted)")
         + parrot(620, 140, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(530, 46, 200, 40, "⟦우리 동네 대회는… 아마…|the village contest… maybe…⟧", 11, bad=True)
         + label(570, 262, "⟦덮은 날 전이라도 책에 적으면 몰라요|even before the day, rare in books means unknown⟧", 11, "var(--bad)")
         + label(380, 300, "⟦덮은 날 이전이라고 다 아는 건 아니에요 — 그래서 사서와 도구가 늘 필요해요|being before the day does not mean it knows — so the librarian and tools are always needed⟧", 12, "var(--ink)", cls="d"))

DATE_I = icon('<rect x="10" y="12" width="44" height="42" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="12" width="44" height="12" rx="4" fill="#C9A86A"/><rect x="18" y="30" width="8" height="8" fill="#142033" opacity="0.5"/><rect x="30" y="30" width="8" height="8" fill="#142033" opacity="0.5"/><rect x="42" y="30" width="8" height="8" fill="var(--bad)"/><rect x="18" y="42" width="8" height="8" fill="none" stroke="var(--bad)" stroke-width="1.5" stroke-dasharray="2 2"/><rect x="30" y="42" width="8" height="8" fill="none" stroke="var(--bad)" stroke-width="1.5" stroke-dasharray="2 2"/>')
NEWS_I = icon(f'<circle cx="20" cy="18" r="9" fill="{SKIN}"/><rect x="12" y="28" width="16" height="22" rx="4" fill="#4A5A72"/><rect x="32" y="16" width="26" height="34" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><path d="M38 26 h14 M38 34 h14 M38 42 h8" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
ASK_I = icon('<rect x="8" y="14" width="48" height="30" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><path d="M20 44 l-6 10 l16 -10z" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><text x="32" y="35" text-anchor="middle" font-size="15" font-weight="700" fill="var(--accent)">~6?</text>')
SOURCE_I = icon('<rect x="12" y="8" width="34" height="42" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 20 h18 M20 28 h18 M20 36 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><circle cx="48" cy="46" r="10" fill="var(--good)"/><path d="M43 46 l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "knowledgecutoff", "order": 34,
    "title": ("책을 덮은 날", "The Day It Closed the Books"),
    "h1": ("<em>지식 컷오프</em>가 뭐예요?", "What is a <em>Knowledge Cutoff</em>?"),
    "sub": ("지식 컷오프를 앵무새 학교가 어느 날 책을 덮어서, 그날 뒤의 일은 앵무새가 모르는 이야기로 풀어봤어요.",
            "The knowledge cutoff, told as a story about the day the parrot school closed its books — after which the parrot knows nothing."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '올해 우승팀이 어디야?'라고 묻자 빨간 앵무새가 '파란 팀이요! 확실해요!'라고 답함. 아래에 '그건 작년 우승팀이에요'", "A guest asks who won this year; a red parrot answers the Blue team! definitely! — with a note that it was last year\'s winner"),
         "caption": ("올해 우승팀을 물었더니, 앵무새가 작년 팀을 자신 있게 말해요.", "Asked who won this year, the parrot confidently names last year\'s team."),
         "small": ("틀린 게 아니라 옛날 답이에요. 앵무새에겐 그게 '가장 최근'이거든요. 왜 그럴까요?", "It is not wrong so much as old. To the parrot, that is the most recent news there is. Why?")},
        {"svg": P2, "alt": ("'학교 달력' 쪽지에 5월 6월 ■ 책 덮음 표시. 서가에 6월까지 읽은 색 책 여섯 권, 그 뒤엔 점선 빈칸 다섯 개. 땀 흘리는 앵무새는 7월부터 아무것도 모름", "A SCHOOL CALENDAR note marks May Jun ■ closed. A shelf holds six colored books read up to June, then five dashed blanks. A sweating parrot knows nothing from July on"),
         "caption": ("학교는 어느 날 책을 덮어요. 그날 뒤에 나온 책은 읽은 적이 없어요.", "One day the school closes the books. Nothing printed after that day was ever read."),
         "small": ('<a href="pretraining-ko.html">책 읽는 학교</a>는 몇 달이나 걸려요. 그래서 어느 날 책을 덮고 학교를 마쳐요 — 그 뒤 서가는 앵무새에게 빈칸이에요.',
                   'The <a href="pretraining-en.html">school of reading</a> takes months. So one day the books are closed and school ends — every shelf after that is blank to the parrot.')},
        {"svg": P3, "hero": True, "alt": ("달력 쪽지에 6월이 표시되고 '책을 덮은 날 = 6월'. 앵무새가 '6월까지는 잘 알아요'. 손님이 '9월엔 무슨 일 있었어?' — 9월 일은 모르고, 모른다고 안 하고 이어 붙일 수도 있음", "A calendar note highlights June: closed the books in June. The parrot says I know up to June. A guest asks what happened in September — it doesn\'t know, and may continue instead of saying so"),
         "caption": ("지식 컷오프는 앵무새가 책을 덮은 날이에요. 그 뒤 일은 몰라요.", "The knowledge cutoff is the day the parrot closed its books. It knows nothing after."),
         "small": ('앵무새마다 덮은 날이 달라요. 그 뒤 일을 물으면 모른다고 하면 다행이고, <a href="hallucination-ko.html">그럴듯하게 이어 붙이면</a> 큰일이에요. 최신 일은 <a href="rag-ko.html">사서</a>나 <a href="toolcall-ko.html">도구</a>가 가져와요.',
                   'Every parrot has its own closing day. Ask about something after it and, with luck, it says so — or it <a href="hallucination-en.html">continues plausibly</a>, which is worse. Fresh news comes from the <a href="rag-en.html">librarian</a> or a <a href="toolcall-en.html">tool</a>.'),
         "tricks": (4, [
             (DATE_I, ("앵무새마다 덮은 날이 달라요", "Each parrot has its own day"), ("새 앵무새일수록 최근", "newer parrots, later days"), "calm"),
             (NEWS_I, ("최신 일은 사서나 도구에게", "Fresh news: librarian or tool"), ("검색해서 쟁반에 올려요", "search it, put it on the tray"), "calm"),
             (ASK_I, ("'언제까지 알아?'를 먼저", "Ask first: known until when?"), ("그 뒤 일은 의심해요", "doubt anything after"), "calm"),
             (SOURCE_I, ("날짜가 중요한 답엔 출처", "Dated answers need a source"), ("우승팀·가격·법·버전", "winners, prices, laws, versions"), "warm"),
         ])},
        {"svg": P4, "alt": ("시간선. 왼쪽엔 책 더미와 '여기까지는 읽었어요', 가운데 빨간 깃발 '책을 덮은 날', 오른쪽엔 물음표 빈칸 세 개. 아래에서 사서가 '9월 우승팀' 신문을 쟁반에 올림", "A timeline: book piles on the left marked read up to here, a red flag in the middle for the day it closed the books, three question-mark blanks on the right. Below, a librarian puts a Sep champion newspaper on the tray"),
         "caption": ("덮은 날 뒤의 빈칸은 학교가 아니라 사서와 도구가 채워요.", "The blank after that day is filled by the librarian and tools, not by school."),
         "small": ('<a href="rag-ko.html">사서</a>가 새 신문을 찾아 <a href="context-ko.html">쟁반</a>에 올리면 앵무새는 그걸 보고 답해요. <a href="toolcall-ko.html">검색 도구</a>도 같은 일을 해요. 학교를 다시 다니는 것보다 훨씬 싸요.',
                   'When the <a href="rag-en.html">librarian</a> finds fresh news and puts it on the <a href="context-en.html">tray</a>, the parrot answers from that. A <a href="toolcall-en.html">search tool</a> does the same. Far cheaper than sending it back to school.')},
        {"svg": P5, "alt": ("왼쪽 초록: 책 일곱 권과 앵무새가 '작년 우승은 파란 팀!' — 책에 많이 실린 일은 잘 앎. 오른쪽 빨강: 책 한 권과 빨간 앵무새가 '우리 동네 대회는… 아마…' — 책에 한 줄만 실린 일은 모름", "Left, green: seven books and the parrot says last year: the Blue team! — well known from many books. Right, red: one book and a red parrot says the village contest… maybe… — one line in one book is unknown"),
         "caption": ("덮은 날 이전이라고 다 아는 건 아니에요. 책에 적게 실린 일은 몰라요.", "Being before the day does not mean it knows. Rare things in the books stay unknown."),
         "small": ('덮은 날 전이라도 책에 한 줄만 실린 일은 흐릿해요 — 그럴 때도 <a href="hallucination-ko.html">그럴듯하게</a> 이어 붙일 수 있어요. 그래서 <a href="rag-ko.html">사서</a>와 <a href="toolcall-ko.html">도구</a>는 최신 일에만 쓰는 게 아니에요.',
                   'Even before the day, something that appeared in one line of one book is hazy — and it can still be <a href="hallucination-en.html">continued plausibly</a>. So the <a href="rag-en.html">librarian</a> and <a href="toolcall-en.html">tools</a> are not just for recent news.')},
    ],
    "summary": (("<b>지식 컷오프</b> = 앵무새가 <b>책을 덮은 날</b>. 그 뒤 일은 몰라요 — 그런데 <b>모른다고 안 하고</b> 이어 붙일 수 있어요. 앵무새마다 날이 다르니 <b>'언제까지 알아?'</b>를 먼저 묻고, 최신 일은 <b>사서·도구</b>가 쟁반에 올려요. 덮은 날 전이라도 책에 <b>적게 실린 일</b>은 몰라요.",
                 "<b>Knowledge cutoff</b> = the day the parrot <b>closed its books</b>. It knows nothing after — yet may <b>continue instead of saying so</b>. Each parrot has its own day, so <b>ask until when</b> first, and let the <b>librarian or a tool</b> put fresh news on the tray. Even before the day, <b>rare things</b> in the books stay unknown."),
                ("Knowledge cutoff. 모델의 사전 학습 데이터가 수집된 마지막 시점이에요. 그 이후의 사건·가격·버전·법 개정은 모델 파라미터에 없고, 물으면 옛 정보나 할루시네이션이 나올 수 있어요. 모델 버전마다 컷오프가 다르고, 최신성은 RAG(검색 근거 주입)나 검색 도구 호출로 보완해요. 컷오프 이전이라도 학습 데이터에 드물게 등장한 사실은 부정확할 수 있어요.",
                 "The last point in time covered by a model\'s pre-training data. Events, prices, versions and law changes after it are not in the parameters, so asking may yield stale answers or hallucinations. Each model version has its own cutoff; recency is patched with RAG (injecting retrieved evidence) or a search tool call. Even facts before the cutoff can be unreliable if they were rare in the training data.")),
    "glossary": [
        ("지식 컷오프", "Knowledge cutoff", ("책을 덮은 날.", "The day it closed the books."), ("그 뒤 일은 앵무새 머릿속에 없어요.", "Nothing after that day is in the parrot\'s head.")),
        ("학습 데이터 시점", "Training data date", ("서가의 마지막 책 날짜.", "The date on the last book on the shelf."), ("책을 덮은 날보다 조금 앞일 수 있어요 — 마지막 몇 달 책은 얇아요.", "Can sit a bit before the closing day — the last few months are thin on the shelf.")),
        ("검색 도구", "Search tool", ("앵무새가 쓰는 검색기.", "The search box the parrot can use."), ('최신 일은 검색해서 쟁반에 올려요. → <a href="toolcall-ko.html">도구 상자</a>', 'Fresh news gets searched and put on the tray. → <a href="toolcall-en.html">the toolbox</a>')),
        ("RAG", "RAG", ("사서가 찾아온 페이지.", "The page the librarian found."), ('물을 때마다 사서가 먼저 찾아요. → <a href="rag-ko.html">사서가 찾아온 페이지</a>', 'The librarian searches first, every time. → <a href="rag-en.html">the page the librarian found</a>')),
        ("최신성", "Recency", ("얼마나 새 소식까지 아나.", "How fresh its news is."), ("우승팀·가격·법·버전처럼 자주 바뀌는 건 늘 의심해요.", "Doubt anything that changes often: winners, prices, laws, versions.")),
        ("모델 버전", "Model version", ("앵무새 이름표의 번호.", "The number on the parrot\'s name tag."), ("새 버전일수록 책을 늦게 덮었어요. 어느 앵무새인지 먼저 확인해요.", "Newer versions closed their books later. Check which parrot you have.")),
        ("할루시네이션", "Hallucination", ("모르는데 이어 붙이기.", "Continuing without knowing."), ('덮은 날 뒤 일을 물으면 이게 나와요. → <a href="hallucination-ko.html">그럴듯 앵무새</a>', 'Ask about after the day and this is what comes out. → <a href="hallucination-en.html">the plausible parrot</a>')),
        ("사전 학습", "Pre-training", ("책 읽는 학교.", "The school of reading."), ('책을 덮는 건 학교가 끝나는 날이에요. → <a href="pretraining-ko.html">책 읽는 학교</a>', 'Closing the books is the day school ends. → <a href="pretraining-en.html">the school of reading</a>')),
    ],
}
