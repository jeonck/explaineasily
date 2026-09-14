from _draw import *
from _world import *


def tag(x, y, text, color="var(--accent)", w=60):
    """책에 붙은 좌표 딱지. 가운데 (x,y)."""
    return (f'<rect x="{x - w / 2}" y="{y - 10}" width="{w}" height="20" rx="5" fill="{color}"/>'
            f'<circle cx="{x - w / 2 + 7}" cy="{y}" r="2.5" fill="#FFF8E7"/>' + label(x + 3, y + 4, text, 10, "#FFF8E7"))


def book_up(x, y, w, h, color, text=None, tag_text=None):
    """세워 둔 책. 제목은 책 아래, 딱지는 책 위쪽에."""
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}"/>'
    if text:
        out += label(x + w / 2, y + h + 15, text, 11, "var(--ink)")
    if tag_text:
        out += tag(x + w / 2, y + 16, tag_text)
    return out


def shelf(x, y, w, h, cells, ink="var(--ink)"):
    """칸 나뉜 서가. cells 는 칸 이름 목록(없으면 이름 없음)."""
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="var(--stone)" opacity="0.5"/><rect x="{x}" y="{y + h - 10}" width="{w}" height="10" fill="var(--stone-dark)"/>'
    n = len(cells)
    cw = w / n
    for i, name in enumerate(cells):
        if i:
            out += f'<rect x="{x + i * cw - 3:.0f}" y="{y}" width="6" height="{h}" fill="var(--stone-dark)"/>'
        if name:
            out += label(x + i * cw + cw / 2, y + h + 22, name, 11, ink, cls="d")
    return out


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="24" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M0 0 V-16 M0 0 L11 6" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/></g>')


COLS = ("#2E7D6B", "#7B3FA0", "#C9822B", "#5B8DEF", "#B5382C", "#6E8199")

# 1. 책 백만 권, 딱지는 있는데 한 권씩 비교하면 하루 걸려요
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=FROWN, extra=SWEAT, **LIBRARIAN) + label(92, 240, "⟦사서|librarian⟧", 11, "var(--muted)")
         + tag(100, 70, "⟦질문 (3, 9)|Q (3, 9)⟧", "var(--good)", 80)
         + "".join(books(230 + i * 70, 220, 5 + (i % 3), 0.9) for i in range(7))
         + "".join(tag(230 + i * 70, 236, "⟦…|…⟧", "var(--accent)", 30) for i in range(7))
         + label(440, 60, "⟦책 백만 권 — 딱지는 다 붙어 있어요|a million books, every one tagged⟧", 13, "var(--ink)", cls="d")
         + label(440, 82, "⟦그런데 한 권씩 딱지를 재 보면…|but measuring against each one by one…⟧", 12, "var(--muted)")
         + clock(700, 100) + label(700, 258, "⟦하루 걸려요|takes a day⟧", 11, "var(--bad)")
         + label(380, 282, "⟦딱지는 있는데, 찾는 게 너무 느려요|the tags are there, but finding is far too slow⟧", 13, "var(--ink)"))

# 2. 왜: 일반 서가는 제목순·번호순 — 뜻 순서가 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 40, "⟦보통 서가: 이름 순서(ㄱ ㄴ ㄷ …)|an ordinary shelf: sorted by name (A B C …)⟧", 13, "var(--ink)", cls="d")
         + shelf(60, 70, 640, 130, (None, None, None, None, None, None))
         + book_up(80, 90, 70, 100, COLS[0], "⟦고양이|cat⟧", "⟦(3, 8)|(3, 8)⟧") + book_up(186, 90, 70, 100, COLS[1], "⟦냥이|kitty⟧", "⟦(3, 9)|(3, 9)⟧")
         + book_up(292, 90, 70, 100, COLS[2], "⟦버스|bus⟧", "⟦(9, 3)|(9, 3)⟧") + book_up(398, 90, 70, 100, COLS[3], "⟦사과|apple⟧", "⟦(6, 5)|(6, 5)⟧")
         + book_up(504, 90, 70, 100, COLS[4], "⟦야옹이|meow-cat⟧", "⟦(3, 7)|(3, 7)⟧") + book_up(610, 90, 70, 100, COLS[5], "⟦자동차|car⟧", "⟦(9, 2)|(9, 2)⟧")
         + '<path d="M221 218 Q380 256 539 218" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + label(380, 262, "⟦뜻이 같은 냥이·야옹이가 멀리 떨어져 있어요|kitty and meow-cat mean the same, yet sit far apart⟧", 12, "var(--bad)")
         + label(380, 288, "⟦이름 순서엔 뜻 순서가 없어요 — 그래서 전부 뒤져야 해요|name order is not meaning order — so you must search everything⟧", 12, "var(--bad)"))

# 3. 벡터 DB = 좌표 딱지 순서로 정리한 서가 (hero)
P3 = svg(360, sky(360)
         + shelf(40, 40, 520, 150, ("⟦동물 칸|animals⟧", "⟦탈것 칸|vehicles⟧", "⟦먹을 것 칸|food⟧"))
         + book_up(56, 66, 44, 100, COLS[0], None, "⟦3,8|3,8⟧") + book_up(106, 66, 44, 100, COLS[1], None, "⟦3,9|3,9⟧") + book_up(156, 66, 44, 100, COLS[4], None, "⟦3,7|3,7⟧")
         + book_up(240, 66, 44, 100, COLS[2], None, "⟦9,3|9,3⟧") + book_up(290, 66, 44, 100, COLS[5], None, "⟦9,2|9,2⟧")
         + book_up(410, 66, 44, 100, COLS[3], None, "⟦6,5|6,5⟧") + book_up(460, 66, 44, 100, COLS[0], None, "⟦6,6|6,6⟧")
         + label(300, 250, "⟦가까운 딱지는 가까운 칸에 꽂혀 있어요|near tags sit in near cells⟧", 12, "var(--ink)")
         + person(600, 100, s=0.9, face=SMILE, **LIBRARIAN) + label(632, 232, "⟦사서|librarian⟧", 11, "var(--muted)")
         + tag(690, 60, "⟦질문 (3, 9)|Q (3, 9)⟧", "var(--good)", 80)
         + '<path d="M650 60 Q400 8 136 34" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="6 4"/><path d="M146 24 L132 36 L150 40" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(650, 270, "⟦동물 칸으로 바로 가요|straight to the animals cell⟧", 12, "var(--good)", cls="d")
         + label(380, 340, "⟦벡터 DB = 좌표 딱지 순서로 정리한 서가, 가까운 딱지가 가까운 칸에|a vector DB is a shelf organized by tag coordinates — near tags in near cells⟧", 13, "var(--ink)", cls="d"))

# 4. 사서가 질문 딱지를 들고 근처 칸에서 5권을 꺼내요 (top-k) + 이름표 필터
P4 = svg(320, sky(320)
         + person(40, 90, s=0.9, face=SMILE, **LIBRARIAN) + tag(120, 60, "⟦질문 (3, 9)|Q (3, 9)⟧", "var(--good)", 80)
         + '<path d="M130 80 L180 110" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + shelf(180, 90, 200, 110, ("⟦동물 칸|animals cell⟧",))
         + "".join(book_up(196 + i * 34, 106, 28, 70, COLS[i]) for i in range(5))
         + "".join(label(210 + i * 34, 188, f"⟦{i + 1}|{i + 1}⟧", 12, "var(--good)", cls="d") for i in range(5))
         + label(280, 244, "⟦가까운 순서로 5권 = top-5|closest 5 = top-5⟧", 12, "var(--good)", cls="d")
         + note(430, 40, 300, 140, "⟦책 이름표로 거르기|FILTER BY LABEL⟧", ("⟦언어: 한국어  ✓|language: Korean  ✓⟧", "⟦연도: 2024 이후  ✓|year: 2024 or later  ✓⟧", "⟦부서: 총무팀  ×|team: admin  ×⟧", "⟦딱지 거리 + 이름표 조건|tag distance + label rules⟧"), 0.95, 3)
         + label(580, 220, "⟦딱지가 가까워도 이름표가 안 맞으면 빼요|near tag but wrong label → skipped⟧", 11, "var(--ink)")
         + label(380, 300, "⟦근처 칸에서 가까운 순서로 몇 권만 — 그리고 이름표로 한 번 더 걸러요|a few books in closest order from nearby cells — then filtered once more by label⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 근처 칸만 보니 놓치기도, 서가는 찾을 뿐 답하진 않아요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + shelf(30, 50, 320, 110, ("⟦본 칸|checked⟧", "⟦안 본 칸|not checked⟧"))
         + book_up(50, 66, 36, 70, COLS[0], None) + book_up(96, 66, 36, 70, COLS[1], None) + book_up(142, 66, 36, 70, COLS[4], None)
         + f'<rect x="240" y="66" width="36" height="70" rx="3" fill="{COLS[3]}" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>' + label(258, 56, "⟦★|★⟧", 14, "var(--bad)", cls="d")
         + label(190, 230, "⟦더 좋은 책이 옆 칸에 있으면 놓쳐요|a better book in the next cell gets missed⟧", 12, "var(--bad)")
         + label(190, 250, "⟦빠른 대신 '대략' 이에요|fast, but approximate⟧", 11, "var(--muted)")
         + person(420, 80, s=0.9, face=SMILE, **LIBRARIAN) + book_up(500, 100, 44, 70, COLS[0], "⟦찾은 책|found⟧")
         + '<path d="M560 130 L600 130" stroke="var(--good)" stroke-width="3"/><path d="M592 122 L604 130 L592 138" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + parrot(660, 130, 1.0, talk=True) + label(660, 210, "⟦답은 앵무새가|the parrot answers⟧", 12, "var(--good)", cls="d")
         + label(570, 250, "⟦서가는 책을 찾을 뿐, 답하지 않아요|the shelf finds books; it never answers⟧", 12, "var(--ink)")
         + label(380, 300, "⟦찾은 책을 앵무새에게 읽히는 이야기가 다음 페이지예요|handing the found book to the parrot is the next story⟧", 12, "var(--ink)", cls="d"))

SHELF_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="var(--stone)"/><rect x="14" y="18" width="10" height="28" fill="#2E7D6B"/><rect x="27" y="18" width="10" height="28" fill="#7B3FA0"/><rect x="40" y="18" width="10" height="28" fill="#C9822B"/><rect x="12" y="8" width="14" height="8" rx="2" fill="var(--accent)"/><rect x="38" y="8" width="14" height="8" rx="2" fill="var(--accent)"/>')
NEAR_I = icon('<rect x="6" y="14" width="52" height="36" rx="4" fill="var(--stone)"/><rect x="31" y="14" width="3" height="36" fill="var(--stone-dark)"/><circle cx="18" cy="32" r="12" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M27 41 l8 8" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')
LABEL_I = icon('<rect x="14" y="10" width="28" height="44" rx="3" fill="#2E7D6B"/><rect x="30" y="30" width="28" height="18" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M35 39 h18" stroke="#142033" stroke-width="2"/>')
REDO_I = icon(f'<circle cx="22" cy="22" r="10" fill="{PARROT}"/><circle cx="46" cy="22" r="10" fill="{PARROT_BIG}"/><path d="M14 46 a18 12 0 1 1 4 8" stroke="var(--accent)" stroke-width="3" fill="none"/><path d="M12 50 l6 6 l6 -8" stroke="var(--accent)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "vectordb", "order": 8,
    "title": ("딱지로 정리한 서가", "The Shelf Organized by Tags"),
    "h1": ("<em>벡터 DB</em>가 뭐예요?", "What is a <em>Vector DB</em>?"),
    "sub": ("벡터 데이터베이스를 좌표 딱지 순서로 책을 꽂아 둔 서가 이야기로 풀어봤어요.",
            "Vector databases, told as a story about a shelf where books are placed in order of their coordinate tags."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 사서가 질문 딱지 (3, 9)를 들고, 딱지 붙은 책 더미 일곱 개 앞에 서 있음. 시계와 '하루 걸려요'", "A sweating librarian holds a question tag (3, 9) in front of seven tagged book piles; a clock reads takes a day"),
         "caption": ("책 백만 권에 딱지는 다 붙어 있어요. 그런데 한 권씩 재 보면 하루가 걸려요.", "A million books, every one tagged. But measuring against each one by one takes a day."),
         "small": ('<a href="embedding-ko.html">좌표 딱지</a>는 있어요. 문제는 찾는 속도예요.', 'The <a href="embedding-en.html">coordinate tags</a> are there. The problem is how slowly you find things.')},
        {"svg": P2, "alt": ("빨간 배경. 이름 순서로 꽂힌 서가: 고양이(3,8), 냥이(3,9), 버스(9,3), 사과(6,5), 야옹이(3,7), 자동차(9,2). 냥이와 야옹이 사이 긴 빨간 점선", "Red background. A shelf sorted by name: cat (3,8), kitty (3,9), bus (9,3), apple (6,5), meow-cat (3,7), car (9,2). A long dashed red line links kitty and meow-cat"),
         "caption": ("보통 서가는 이름순·번호순이에요. 뜻 순서가 없어요.", "An ordinary shelf is sorted by name or number. There is no meaning order."),
         "small": ("뜻이 같은 냥이와 야옹이가 멀리 떨어져 있어요. 그래서 가까운 딱지를 찾으려면 전부 뒤져야 해요.", "Kitty and meow-cat mean the same yet sit far apart. So to find near tags, you must search everything.")},
        {"svg": P3, "hero": True, "alt": ("동물 칸·탈것 칸·먹을 것 칸으로 나뉜 서가, 각 책에 딱지 (3,8)(3,9)(3,7) / (9,3)(9,2) / (6,5)(6,6). 사서가 질문 딱지 (3, 9)를 들고 동물 칸을 가리킴", "A shelf split into animals, vehicles and food cells; books carry tags (3,8)(3,9)(3,7) / (9,3)(9,2) / (6,5)(6,6). The librarian holds question tag (3, 9) and points at the animals cell"),
         "caption": ("벡터 DB는 좌표 딱지 순서로 정리한 서가예요. 가까운 딱지가 가까운 칸에 꽂혀요.", "A vector DB is a shelf organized by tag coordinates. Near tags sit in near cells."),
         "small": ('질문 딱지가 (3, 9)면 동물 칸만 보면 돼요. 백만 권을 다 재지 않아도 돼요. 딱지가 뭔지는 <a href="embedding-ko.html">좌표 딱지</a> 이야기에서.',
                   'If the question tag is (3, 9), only the animals cell needs checking — not all million books. What a tag is: <a href="embedding-en.html">the coordinate tag</a> story.'),
         "tricks": (4, [
             (SHELF_I, ("딱지로 꽂아요", "Shelve by tag"), ("이름이 아니라 좌표 순서로", "by coordinates, not by name"), "calm"),
             (NEAR_I, ("근처 칸만 뒤져요", "Search nearby cells only"), ("빠른 대신 대략이에요", "fast, but approximate")),
             (LABEL_I, ("책마다 이름표도 같이", "A label on every book too"), ("언어·연도·부서로 걸러요", "filter by language, year, team"), "calm"),
             (REDO_I, ("앵무새를 바꾸면 다시 꽂아요", "New parrot, reshelve everything"), ("딱지 지도가 달라져요", "the tag map changes"), "warm"),
         ])},
        {"svg": P4, "alt": ("사서가 질문 딱지 (3, 9)를 들고 동물 칸에서 책 다섯 권을 1~5 순서로 꺼냄. 오른쪽 쪽지: 언어 한국어 ✓, 연도 2024 이후 ✓, 부서 총무팀 ×, 딱지 거리 + 이름표 조건", "The librarian with question tag (3, 9) pulls five books numbered 1 to 5 from the animals cell. A note on the right: language Korean ✓, year 2024 or later ✓, team admin ×, tag distance + label rules"),
         "caption": ("근처 칸에서 가까운 순서로 몇 권만 꺼내요. 그리고 이름표로 한 번 더 걸러요.", "Pull just a few books in closest order from nearby cells. Then filter once more by label."),
         "small": ("다섯 권 달라고 하면 다섯 권 — 그게 top-5 예요. 딱지가 가까워도 이름표가 안 맞으면 빼요.", "Ask for five and you get five — that is top-5. A near tag with the wrong label gets skipped.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 본 칸과 안 본 칸, 안 본 칸에 별표 책이 점선으로 — 놓침. 오른쪽 초록: 사서가 찾은 책을 앵무새에게 건네고 앵무새가 답함", "Left, red: a checked cell and an unchecked cell; a starred book in the unchecked cell is dashed — missed. Right, green: the librarian hands the found book to the parrot, which answers"),
         "caption": ("근처 칸만 보니 가끔 더 좋은 책을 놓쳐요. 그리고 서가는 찾을 뿐, 답하지 않아요.", "Checking only nearby cells sometimes misses a better book. And the shelf finds — it never answers."),
         "small": ('빠른 대신 대략이에요(근사). 찾은 책을 앵무새에게 읽혀서 답하게 하는 이야기는 <a href="rag-ko.html">사서가 찾아온 페이지</a>에서.',
                   'It is fast but approximate. Handing the found book to the parrot so it can answer is <a href="rag-en.html">the page the librarian brought</a>.')},
    ],
    "summary": (("<b>벡터 DB</b> = <b>좌표 딱지 순서로 정리한 서가</b>. 가까운 딱지가 가까운 칸에 있어서 <b>근처 칸만 뒤지면</b> 되고, 책마다 <b>이름표</b>로 한 번 더 걸러요. 빠른 대신 대략이고, 찾을 뿐 답하진 않아요.",
                 "<b>Vector DB</b> = a <b>shelf organized by tag coordinates</b>. Near tags sit in near cells, so you <b>search only nearby cells</b>, then filter by each book\'s <b>label</b>. Fast but approximate — and it finds, never answers."),
                ("Vector database. 임베딩 벡터를 인덱스(HNSW 등)로 저장해 근사 최근접 탐색(ANN)으로 가장 가까운 top-k 를 빠르게 찾는 저장소예요. 메타데이터 필터, 청크 단위 저장, 키워드+벡터 하이브리드 검색을 지원하고, 임베딩 모델을 바꾸면 전체를 다시 인덱싱해야 해요. RAG 의 검색 층이에요.",
                 "A store that keeps embedding vectors in an index (HNSW and others) and uses approximate nearest-neighbor search to return the closest top-k quickly. Supports metadata filters, chunk-level storage and hybrid keyword+vector search; changing the embedding model means re-indexing everything. It is the retrieval layer of RAG.")),
    "glossary": [
        ("벡터 데이터베이스", "Vector database", ("딱지로 정리한 서가.", "The shelf organized by tags."), ("Pinecone, Milvus, pgvector, Chroma 가 이 서가예요.", "Pinecone, Milvus, pgvector, Chroma are this shelf.")),
        ("인덱스 (HNSW)", "Index (HNSW)", ("칸 나누는 방법.", "How the cells are laid out."), ("가까운 딱지끼리 다리를 놓아 몇 걸음 만에 근처로 가요.", "Bridges between near tags let you reach the neighborhood in a few hops.")),
        ("근사 최근접 탐색", "Approximate nearest neighbor", ("근처 칸만 뒤지기.", "Searching nearby cells only."), ("전부 안 재서 빠르지만, 가끔 더 좋은 책을 놓쳐요.", "Fast because it skips most books — but sometimes misses a better one.")),
        ("top-k", "top-k", ("가까운 순서로 k 권.", "The k closest books."), ("5권 달라면 5권. 너무 많이 꺼내면 쟁반이 넘쳐요.", "Ask for 5, get 5. Pull too many and the tray overflows.")),
        ("메타데이터 필터", "Metadata filter", ("책 이름표로 거르기.", "Filtering by the book\'s label."), ("언어·연도·부서 같은 조건. 딱지 거리와 같이 써요.", "Rules like language, year, team — used alongside tag distance.")),
        ("청크", "Chunk", ("책을 페이지로 쪼개 꽂기.", "Shelving a book as pages."), ("책 한 권이 아니라 몇 문단씩 딱지를 붙여요. 쟁반에 올리기 좋게.", "Tags go on a few paragraphs at a time, not a whole book — so they fit on the tray.")),
        ("하이브리드 검색", "Hybrid search", ("글자 + 딱지.", "Letters + tags."), ("이름·번호 같은 정확한 말은 글자로, 뜻은 딱지로 같이 찾아요.", "Exact things like names and numbers by letters, meaning by tags — both at once.")),
        ("임베딩", "Embedding", ("좌표 딱지.", "The coordinate tag."), ('서가에 꽂는 그 딱지. → <a href="embedding-ko.html">낱말마다 좌표 딱지</a>', 'The tag that goes on the shelf. → <a href="embedding-en.html">a coordinate tag on every word</a>')),
    ],
}
