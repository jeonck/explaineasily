from _draw import *
from _world import *


def tag(x, y, text, color="var(--accent)", w=70):
    """낱말에 붙은 좌표 딱지. 가운데 (x,y)."""
    return (f'<rect x="{x - w / 2}" y="{y - 11}" width="{w}" height="22" rx="5" fill="{color}"/>'
            f'<circle cx="{x - w / 2 + 8}" cy="{y}" r="2.5" fill="#FFF8E7"/>' + label(x + 4, y + 4, text, 11, "#FFF8E7"))


def book_up(x, y, w, h, color, text):
    """세워 둔 책 한 권, 제목은 책 아래."""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{color}"/>' + label(x + w / 2, y + h + 16, text, 11, "var(--ink)")


def plane(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M{x + 24} {y + 16} V{y + h - 24} H{x + w - 16}" stroke="var(--muted)" stroke-width="2" fill="none"/>')


def dot(x, y, text, color="var(--good)"):
    return f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>' + label(x, y - 12, text, 11, "var(--ink)")


# 1. 사서가 '고양이'를 찾는데 '냥이' 책은 못 찾아요
P1 = svg(300, sky(300)
         + person(90, 110, s=0.9, face=FROWN, extra=SWEAT, **LIBRARIAN) + label(122, 240, "⟦사서|librarian⟧", 11, "var(--muted)")
         + note(170, 60, 120, 60, "⟦찾는 말|LOOKING FOR⟧", ("⟦고양이|cat⟧",), 0.95)
         + '<rect x="380" y="70" width="350" height="170" rx="8" fill="var(--stone)" opacity="0.5"/><rect x="380" y="200" width="350" height="8" fill="var(--stone-dark)"/>'
         + book_up(410, 100, 60, 100, "#2E7D6B", "⟦냥이|kitty⟧") + book_up(500, 100, 60, 100, "#7B3FA0", "⟦야옹이|meow-cat⟧") + book_up(590, 100, 60, 100, "#C9822B", "⟦자동차|car⟧")
         + label(440, 90, "⟦?|?⟧", 22, "var(--bad)", cls="d") + label(530, 90, "⟦?|?⟧", 22, "var(--bad)", cls="d")
         + label(380, 282, "⟦글자가 다르니 못 찾아요 — 뜻은 같은데|the letters differ, so it can\'t find them — even though the meaning is the same⟧", 13, "var(--ink)"))

# 2. 왜: 글자로 찾으면 뜻이 같아도 놓치고, 글자만 같아도 걸려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(200, 50, "⟦글자로 찾기|searching by letters⟧", 13, "var(--ink)", cls="d")
         + beans(90, 110, ("⟦고|c⟧", "⟦양|a⟧", "⟦이|t⟧"), 1.0, 40) + label(200, 116, "⟦vs|vs⟧", 14, "var(--muted)") + beans(250, 110, ("⟦냥|k⟧", "⟦이|it⟧"), 1.0, 40)
         + label(200, 160, "⟦×  글자가 달라요 → 못 찾아요|×  different letters → missed⟧", 12, "var(--bad)")
         + beans(90, 210, ("⟦고|c⟧", "⟦양|a⟧", "⟦이|t⟧"), 1.0, 40) + label(200, 216, "⟦vs|vs⟧", 14, "var(--muted)") + beans(250, 210, ("⟦고|c⟧", "⟦양|a⟧", "⟦이|t⟧", "⟦털|fur⟧"), 1.0, 40)
         + label(200, 260, "⟦✓  글자는 같아요 → 엉뚱한 것도 걸려요|✓  same letters → wrong things match too⟧", 12, "var(--bad)")
         + person(520, 90, s=0.9, face=FROWN, **LIBRARIAN)
         + bubble(440, 20, 300, 40, "⟦뜻으로 찾고 싶어요|I want to search by meaning⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(590, 230, "⟦사서는 글자밖에 볼 줄 몰라요|the librarian can only look at letters⟧", 12, "var(--ink)")
         + label(380, 288, "⟦뜻이 같은 낱말은 생김새가 달라요|words that mean the same look different⟧", 12, "var(--bad)"))

# 3. 임베딩 = 낱말·문장마다 뜻의 위치를 적은 좌표 딱지 (hero)
P3 = svg(360, sky(360)
         + plane(40, 30, 380, 270) + label(230, 50, "⟦뜻의 지도|MAP OF MEANING⟧", 12, "var(--muted)", cls="d")
         + '<circle cx="150" cy="150" r="58" fill="var(--good-soft)"/>' + label(150, 78, "⟦동물 무리|animals⟧", 11, "var(--good)", cls="d")
         + dot(130, 140, "⟦고양이|cat⟧") + dot(170, 158, "⟦냥이|kitty⟧") + dot(140, 185, "⟦야옹이|meow-cat⟧")
         + '<circle cx="330" cy="230" r="46" fill="var(--accent-soft)"/>' + label(330, 170, "⟦탈것 무리|vehicles⟧", 11, "var(--accent)", cls="d")
         + dot(318, 225, "⟦자동차|car⟧", "var(--accent)") + dot(350, 250, "⟦버스|bus⟧", "var(--accent)")
         + parrot(520, 150, 1.2, talk=True) + label(520, 240, "⟦딱지 적는 앵무새|the tag-writing parrot⟧", 11, "var(--muted)")
         + note(580, 40, 160, 130, "⟦좌표 딱지|TAGS⟧", ("⟦고양이  (3, 8)|cat      (3, 8)⟧", "⟦냥이    (3, 9)|kitty    (3, 9)⟧", "⟦자동차  (9, 2)|car      (9, 2)⟧", "⟦…숫자 수백 개|…hundreds of numbers⟧"), 0.95)
         + label(660, 200, "⟦뜻이 가까우면|close in meaning,⟧", 12, "var(--ink)") + label(660, 218, "⟦숫자도 가까워요|close in numbers⟧", 12, "var(--ink)")
         + label(380, 340, "⟦임베딩 = 낱말·문장마다 뜻의 위치를 적은 좌표 딱지|an embedding is a coordinate tag that records where each word or sentence sits in meaning⟧", 13, "var(--ink)", cls="d"))

# 4. 거리 재기: 가까운 딱지 = 비슷한 뜻. 문장도 딱지 하나
P4 = svg(320, sky(320)
         + plane(40, 30, 440, 240)
         + dot(150, 120, "⟦고양이|cat⟧") + dot(200, 140, "⟦냥이|kitty⟧") + dot(400, 220, "⟦자동차|car⟧")
         + dot(120, 190, "⟦우리 집 고양이가 잤어요|my cat slept⟧", "#2E7D6B")
         + '<path d="M150 120 L200 140" stroke="var(--good)" stroke-width="3"/>' + label(190, 112, "⟦짧아요|short⟧", 11, "var(--good)", cls="d")
         + '<path d="M150 120 L400 220" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>' + label(300, 160, "⟦길어요|long⟧", 11, "var(--bad)", cls="d")
         + note(510, 40, 230, 130, "⟦거리 재기|MEASURING⟧", ("⟦가까움 = 비슷한 뜻|close = similar meaning⟧", "⟦문장 하나도 딱지 하나|a sentence gets one tag too⟧", "⟦같은 앵무새 딱지끼리만|only compare same-parrot tags⟧", "⟦(코사인 유사도)|(cosine similarity)⟧"), 0.95)
         + label(625, 210, "⟦다른 앵무새가 적은 딱지는|tags from another parrot⟧", 11, "var(--ink)") + label(625, 228, "⟦지도가 달라서 못 재요|are on a different map⟧", 11, "var(--ink)")
         + label(380, 300, "⟦자로 재듯 딱지 사이 거리를 재요 — 짧으면 비슷한 뜻|measure the distance between tags like a ruler — short means similar⟧", 12, "var(--muted)"))

# 5. 되는 것 / 깨지는 곳
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + person(40, 90, s=0.9, face=SMILE, **LIBRARIAN) + note(120, 40, 120, 60, "⟦찾는 말|LOOKING FOR⟧", ("⟦냥이 사진|kitty photo⟧",), 0.9)
         + book_up(270, 90, 60, 90, "#2E7D6B", "⟦고양이 사진|cat photos⟧") + label(300, 70, "⟦✓|✓⟧", 22, "var(--good)", cls="d")
         + label(190, 240, "⟦글자가 달라도 뜻으로 찾아요|different letters, found by meaning⟧", 12, "var(--ink)")
         + plane(410, 40, 200, 150) + dot(490, 110, "⟦뜨겁다|hot⟧", "var(--bad)") + dot(530, 130, "⟦차갑다|cold⟧", "var(--bad)")
         + label(660, 100, "⟦반대말인데|opposites,⟧", 12, "var(--ink)") + label(660, 118, "⟦딱지는 가까워요|but tags sit close⟧", 12, "var(--ink)")
         + label(570, 240, "⟦딱지는 뜻의 대략 위치일 뿐이에요|a tag is only a rough position of meaning⟧", 12, "var(--bad)")
         + label(380, 300, "⟦그래서 딱지로 찾은 다음, 답은 앵무새가 읽고 해요|so you find by tag, then the parrot reads and answers⟧", 12, "var(--ink)", cls="d"))

NEAR_I = icon('<circle cx="22" cy="26" r="7" fill="var(--good)"/><circle cx="34" cy="34" r="7" fill="var(--good)"/><circle cx="52" cy="50" r="6" fill="var(--accent)"/><path d="M12 54 V12 M12 54 H54" stroke="var(--muted)" stroke-width="2"/>')
SENT_I = icon('<path d="M10 18 h44 M10 28 h36 M10 38 h30" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><rect x="28" y="44" width="30" height="14" rx="4" fill="var(--accent)"/><circle cx="35" cy="51" r="2" fill="#FFF8E7"/>')
SAME_I = icon(f'<circle cx="20" cy="22" r="10" fill="{PARROT}"/><circle cx="44" cy="22" r="10" fill="{PARROT}"/><rect x="12" y="40" width="16" height="10" rx="3" fill="var(--accent)"/><rect x="36" y="40" width="16" height="10" rx="3" fill="var(--accent)"/><path d="M26 58 l5 4 l8 -9" stroke="var(--good)" stroke-width="3" fill="none"/>')
NUM_I = icon('<rect x="8" y="16" width="48" height="32" rx="6" fill="var(--accent)"/><text x="32" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF8E7">0.2 -0.7 …</text>')

PAGE = {
    "slug": "embedding", "order": 7,
    "title": ("낱말마다 좌표 딱지", "A Coordinate Tag on Every Word"),
    "h1": ("<em>임베딩</em>이 뭐예요?", "What is an <em>Embedding</em>?"),
    "sub": ("임베딩을 낱말과 문장마다 뜻의 위치를 적어 붙인 좌표 딱지 이야기로 풀어봤어요.",
            "Embeddings, told as a story about coordinate tags that record where every word and sentence sits in meaning."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 사서가 '고양이' 쪽지를 들고 서가를 보는데, 서가엔 냥이·야옹이·자동차 책만 있고 물음표", "A sweating librarian holds a note reading cat and looks at a shelf holding only kitty, meow-cat and car books, with question marks"),
         "caption": ("사서가 '고양이' 책을 찾는데, '냥이'라 적힌 책은 못 찾아요.", "The librarian looks for a cat book and can\'t find the one labeled kitty."),
         "small": ("글자가 다르니까요. 뜻은 똑같은데도요.", "The letters are different — even though the meaning is exactly the same.")},
        {"svg": P2, "alt": ("빨간 배경. 고·양·이 콩과 냥·이 콩은 글자가 달라 ×, 고·양·이 콩과 고·양·이·털 콩은 글자가 같아 엉뚱하게 ✓. 사서가 '뜻으로 찾고 싶어요'", "Red background. Beans c-a-t vs k-it get a × for different letters; c-a-t vs c-a-t-fur get a ✓ though the meaning is off. The librarian says I want to search by meaning"),
         "caption": ("글자로 찾으면 뜻이 같아도 놓치고, 글자만 같아도 걸려요.", "Search by letters and you miss same-meaning words — and catch wrong ones that merely look alike."),
         "small": ("뜻이 같은 낱말은 생김새가 다르고, 생김새가 같은 낱말도 뜻이 다를 수 있어요. 사서는 글자밖에 볼 줄 몰라요.", "Same-meaning words look different, and same-looking words can mean different things. The librarian can only see letters.")},
        {"svg": P3, "hero": True, "alt": ("뜻의 지도: 동물 무리(고양이·냥이·야옹이)와 탈것 무리(자동차·버스)가 따로 모여 있고, 앵무새가 좌표 딱지(고양이 3,8 / 냥이 3,9 / 자동차 9,2)를 적음", "A map of meaning: an animals cluster (cat, kitty, meow-cat) and a vehicles cluster (car, bus) sit apart; the parrot writes coordinate tags (cat 3,8 / kitty 3,9 / car 9,2)"),
         "caption": ("임베딩은 낱말·문장마다 뜻의 위치를 적은 좌표 딱지예요.", "An embedding is a coordinate tag that records where each word or sentence sits in meaning."),
         "small": ('앵무새가 낱말마다 딱지를 적어요. 고양이·냥이·야옹이는 한 무리, 자동차는 멀리. 뜻이 가까우면 숫자도 가까워요. 이 딱지를 꽂아 두는 서가는 <a href="vectordb-ko.html">벡터 DB</a> 이야기에서.',
                   'The parrot writes a tag for every word. Cat, kitty and meow-cat cluster together; car sits far away. Close in meaning means close in numbers. The shelf that stores these tags is the <a href="vectordb-en.html">vector DB</a> story.'),
         "tricks": (4, [
             (NEAR_I, ("뜻이 가까우면 좌표도 가까워요", "Close meaning, close coordinates"), ("고양이 옆에 냥이", "kitty sits next to cat"), "calm"),
             (SENT_I, ("문장 하나도 딱지 하나", "A sentence gets one tag too"), ("긴 글도 위치 하나로", "even a long text becomes one point")),
             (SAME_I, ("같은 앵무새 딱지끼리만", "Compare same-parrot tags only"), ("지도가 다르면 못 재요", "different maps can\'t be measured"), "warm"),
             (NUM_I, ("딱지는 숫자 수백 개", "A tag is hundreds of numbers"), ("그림은 2개, 진짜는 더 많아요", "the picture shows 2, real ones have more")),
         ])},
        {"svg": P4, "alt": ("지도 위 고양이–냥이 사이 짧은 초록 선, 고양이–자동차 사이 긴 빨간 점선. '우리 집 고양이가 잤어요' 문장도 점 하나. 거리 재기 쪽지: 가까움=비슷한 뜻, 문장도 딱지 하나, 같은 앵무새끼리만, (코사인 유사도)", "On the map a short green line links cat and kitty; a long dashed red line links cat and car. The sentence my cat slept is one dot too. A measuring note: close = similar, a sentence gets one tag, same-parrot tags only, (cosine similarity)"),
         "caption": ("딱지 사이 거리를 자로 재듯 재요. 짧으면 비슷한 뜻이에요.", "You measure the distance between tags like with a ruler. Short means similar meaning."),
         "small": ("문장 하나도 딱지 하나가 돼요. 단, 다른 앵무새가 적은 딱지는 지도가 달라서 같이 잴 수 없어요.", "A whole sentence becomes one tag too. But tags written by a different parrot live on a different map, so you can\'t measure them together.")},
        {"svg": P5, "alt": ("왼쪽 초록: 사서가 '냥이 사진'으로 '고양이 사진' 책을 찾음 ✓. 오른쪽 빨강: 지도에서 뜨겁다와 차갑다가 가까이 붙어 있음 — 반대말인데", "Left, green: the librarian finds the cat photos book using kitty photo ✓. Right, red: on the map hot and cold sit close together — though they are opposites"),
         "caption": ("뜻으로 찾게 됐어요. 그런데 딱지는 뜻의 '대략 위치'일 뿐이에요.", "Now you can search by meaning. But a tag is only a rough position of meaning."),
         "small": ('뜨겁다와 차갑다는 둘 다 온도 얘기라 딱지가 가까울 수 있어요. 그래서 딱지로 찾은 다음, 답은 앵무새가 읽고 해요 — <a href="rag-ko.html">사서가 찾아온 페이지</a> 이야기에서.',
                   'Hot and cold are both about temperature, so their tags can sit close. So you find by tag, then the parrot reads and answers — see <a href="rag-en.html">the page the librarian brought</a>.')},
    ],
    "summary": (("<b>임베딩</b> = 낱말·문장마다 <b>뜻의 위치를 적은 좌표 딱지</b>. 뜻이 가까우면 딱지도 가까워서, <b>글자가 달라도 뜻으로</b> 찾을 수 있어요. 단, 대략 위치라 반대말이 가까울 수도 있어요.",
                 "<b>Embedding</b> = a <b>coordinate tag recording where each word or sentence sits in meaning</b>. Close meanings get close tags, so you can <b>search by meaning even when the letters differ</b>. But it is a rough position — opposites can sit close."),
                ("Embedding. 텍스트(또는 이미지)를 수백~수천 차원의 숫자 벡터로 바꾼 것으로, 의미가 비슷하면 벡터도 가깝게 나오도록 임베딩 모델이 학습돼요. 가까움은 보통 코사인 유사도로 재고, 같은 모델의 벡터끼리만 비교할 수 있어요. 의미 검색·벡터 DB·RAG 의 기초예요.",
                 "Text (or images) turned into a numeric vector of hundreds to thousands of dimensions, produced by an embedding model trained so that similar meanings yield nearby vectors. Closeness is usually measured with cosine similarity, and only vectors from the same model are comparable. It underpins semantic search, vector DBs and RAG.")),
    "glossary": [
        ("임베딩", "Embedding", ("좌표 딱지.", "The coordinate tag."), ("낱말·문장의 뜻을 숫자 위치로 적은 것.", "A word or sentence\'s meaning written as a numeric position.")),
        ("벡터", "Vector", ("딱지에 적힌 숫자 줄.", "The row of numbers on the tag."), ("(3, 8) 처럼 숫자 여러 개가 한 줄로 — 진짜는 수백 개.", "Several numbers in a row like (3, 8) — real ones have hundreds.")),
        ("차원", "Dimension", ("딱지의 숫자 개수.", "How many numbers a tag holds."), ("그림은 2차원, 진짜 딱지는 384·768·1536 차원 같은 수예요.", "The picture is 2-D; real tags are 384, 768 or 1536 dimensions.")),
        ("코사인 유사도", "Cosine similarity", ("딱지 사이 가까움 점수.", "The closeness score between tags."), ("1 에 가까울수록 같은 뜻, 0 이면 상관없음.", "Near 1 means same meaning, 0 means unrelated.")),
        ("임베딩 모델", "Embedding model", ("딱지 적는 앵무새.", "The tag-writing parrot."), ("딱지를 만드는 전용 모델. 앵무새를 바꾸면 딱지를 다시 적어야 해요.", "A dedicated model that makes tags. Change the parrot and every tag must be rewritten.")),
        ("의미 검색", "Semantic search", ("뜻으로 찾기.", "Searching by meaning."), ("글자가 아니라 딱지 거리로 찾아요. 냥이로 고양이를 찾아요.", "Search by tag distance rather than letters — kitty finds cat.")),
        ("벡터 DB", "Vector DB", ("딱지로 정리한 서가.", "The shelf organized by tags."), ('딱지를 빨리 찾게 꽂아 둔 곳. → <a href="vectordb-ko.html">딱지로 정리한 서가</a>', 'Where tags are shelved for fast lookup. → <a href="vectordb-en.html">the shelf organized by tags</a>')),
        ("RAG", "RAG", ("사서가 찾아온 페이지.", "The page the librarian brought."), ('딱지로 찾은 페이지를 앵무새에게 줘요. → <a href="rag-ko.html">사서가 찾아온 페이지</a>', 'The page found by tag goes to the parrot. → <a href="rag-en.html">the page the librarian brought</a>')),
    ],
}
