from _draw import *
from _world import *

# 문장 콩 7개: 1번(강가/river)이 단서, 6번(은행?/bank?)이 고를 자리
WORDS = ("⟦저기|Down⟧", "⟦강가에|river⟧", "⟦은행이|the⟧", "⟦잔뜩|bank⟧", "⟦있어|stood⟧", "⟦무슨|which⟧", "⟦은행?|bank?⟧")


def gaze(x0, y, x1, w, color="var(--accent)"):
    """콩 x0 에서 콩 x1 로 가는 눈길 (위로 볼록한 호). w = 선 굵기."""
    lift = abs(x0 - x1) * 0.3
    return f'<path d="M{x0} {y} Q{(x0 + x1) / 2} {y - lift} {x1} {y}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round" opacity="0.9"/>'


# 1. 헷갈리는 낱말인데 앵무새가 맞혀요
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=EYES, **GUEST) + bubble(20, 30, 300, 40, "⟦강가에 은행이 잔뜩 있어 — 무슨 은행?|the bank sat by the river — which bank?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(480, 200, 140) + parrot(480, 160, 1.1, talk=True)
         + bubble_parrot(370, 30, 230, 40, "⟦나무에서 떨어지는 은행이요!|the river bank!⟧", 12)
         + label(480, 250, "⟦돈 은행이 아니에요|not the money bank⟧", 11, "var(--muted)")
         + label(380, 282, "⟦멀리 있는 '강가'를 보고 맞혔어요 — 어떻게?|it used the far-away river to get it right — how?⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 콩을 순서대로만 읽으면 멀리 있는 콩을 잊어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 45, "⟦옛날 앵무새는 바로 앞 콩 몇 개만 봤어요|the old parrot only looked at the last few beans⟧", 12, "var(--ink)")
         + beans(90, 130, WORDS[:6], 1.0, 62)
         + '<rect x="252" y="105" width="176" height="50" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(340, 178, "⟦여기만 봐요|sees only these⟧", 11, "var(--accent)")
         + '<rect x="122" y="112" width="60" height="36" rx="8" fill="var(--bad-soft)" opacity="0.7"/>' + label(152, 178, "⟦잊었어요|forgotten⟧", 11, "var(--bad)")
         + '<rect x="450" y="108" width="52" height="44" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(476, 136, "⟦?|?⟧", 22, "var(--accent)", cls="d")
         + parrot(620, 130, 1.0, color=PARROT_BAD, mood="sweat", talk=True) + bubble_parrot(540, 40, 180, 36, "⟦돈 은행이요!|the money bank!⟧", 11, bad=True)
         + label(380, 230, "⟦'강가' 콩은 멀어서 잊고, 가까운 '은행' 콩만 보고 골랐어요|it forgot the far river bean and chose from the near bank bean⟧", 12, "var(--ink)")
         + label(380, 282, "⟦순서대로만 읽으면 멀리 있는 콩이 사라져요|read only in order, and far-away beans vanish⟧", 12, "var(--bad)"))

# 3. 어텐션 = 다음 콩을 고를 때 쟁반 위 모든 콩을 훑어보고, 관련 콩에 눈길을 더 주는 것 (hero)
BX = [100 + i * 64 for i in range(7)]
GAZES = (gaze(BX[6], 203, BX[1], 6) + gaze(BX[6], 203, BX[3], 3, "var(--accent)")
         + "".join(gaze(BX[6], 203, BX[i], 1.2, "var(--muted)") for i in (0, 2, 4, 5)))
LAYERS = "".join(f'<rect x="{560 + (2 - i) * 6}" y="{70 + i * 36}" width="160" height="30" rx="6" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/>'
                 + label(640 + (2 - i) * 6, 90 + i * 36, f"⟦눈길 층 {3 - i}|gaze layer {3 - i}⟧", 11, "var(--ink)") for i in range(3))
P3 = svg(360, sky(360)
         + perch(110, 155, 110) + parrot(110, 115, 1.1)
         + label(340, 60, "⟦쟁반 위 모든 콩을 한 번씩 훑어봐요|it glances over every bean on the tray⟧", 12, "var(--ink)")
         + label(340, 82, "⟦관련 있는 콩엔 굵은 눈길을 줘요|related beans get a thicker gaze⟧", 12, "var(--accent)")
         + tray(40, 226, 470, 70) + beans(BX[0], 214, WORDS, 1.0, 64) + GAZES
         + label(640, 52, "⟦앵무새 머릿속|inside its head⟧", 11, "var(--muted)") + LAYERS
         + label(640, 200, "⟦겹겹이 쌓으면 = 트랜스포머|stacked up = a transformer⟧", 11, "var(--ink)")
         + label(275, 318, "⟦굵은 선 = 눈길 많이 · 가는 선 = 조금|thick line = lots of gaze, thin = a little⟧", 11, "var(--muted)")
         + label(380, 344, "⟦어텐션 = 다음 콩을 고를 때 모든 콩을 훑어보고, 관련 콩을 더 오래 보는 것|attention: when picking the next bean, glance at every bean and look longer at the related ones⟧", 12, "var(--ink)", cls="d"))

# 4. 층마다 다른 눈길 — 옆 콩끼리 / 뜻이 통하는 콩 / 문장 전체 + 순서 번호표
RX = [250 + i * 44 for i in range(8)]


def row(y, title, arcs):
    return (label(130, y + 4, title, 12, "var(--ink)") + "".join(bean(x, y, 0.8) for x in RX)
            + "".join(gaze(RX[a], y - 9, RX[b], w) for a, b, w in arcs))


P4 = svg(320, sky(320)
         + row(90, "⟦층 1: 옆 콩끼리|layer 1: neighbours⟧", [(i, i + 1, 2) for i in range(7)])
         + "".join(label(x, 116, f"{i + 1}", 10, "var(--muted)") for i, x in enumerate(RX)) + label(660, 116, "⟦← 순서 번호표|← order tags⟧", 11, "var(--muted)")
         + row(170, "⟦층 2: 뜻이 통하는 콩|layer 2: meaning pairs⟧", [(1, 6, 5), (3, 5, 3)])
         + row(250, "⟦층 3: 문장 전체|layer 3: whole sentence⟧", [(7, i, 1.5) for i in range(7)])
         + label(660, 175, "⟦멀어도 이어요|far apart, still linked⟧", 11, "var(--accent)")
         + label(380, 300, "⟦층마다 다른 눈길을 봐요 — 번호표가 있어서 콩 순서도 알아요|each layer looks differently — and order tags tell it which bean came first⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 눈길은 '관련'이지 '이해'가 아니에요 + 콩이 늘면 눈길 계산이 제곱으로 늘어요
def cluster(cx, cy, n, r):
    import math
    pts = [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    lines = "".join(f'<path d="M{a[0]:.0f} {a[1]:.0f} L{b[0]:.0f} {b[1]:.0f}" stroke="var(--accent)" stroke-width="1.2" opacity="0.7"/>'
                    for i, a in enumerate(pts) for b in pts[i + 1:])
    return lines + "".join(bean(x, y, 0.6) for x, y in pts)


P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(100, 150, 1.0, talk=True) + bubble_parrot(30, 50, 250, 40, "⟦'강가' 옆이니까 이쪽 은행!|next to river, so this bank!⟧", 11)
         + label(190, 215, "⟦눈길은 어떤 콩이 관련 있나를 재요|the gaze measures which beans relate⟧", 11, "var(--ink)")
         + label(190, 240, "⟦뜻을 아는 게 아니에요|it still does not know the meaning⟧", 11, "var(--good)")
         + cluster(460, 130, 4, 34) + label(460, 200, "⟦콩 4개 → 선 6개|4 beans → 6 lines⟧", 11, "var(--ink)")
         + cluster(640, 130, 8, 50) + label(640, 200, "⟦콩 8개 → 선 28개|8 beans → 28 lines⟧", 11, "var(--ink)")
         + label(570, 240, "⟦콩이 2배면 눈길은 4배 — 긴 쟁반이 비싼 이유|double the beans, four times the gaze — why long trays cost⟧", 11, "var(--bad)")
         + label(380, 300, "⟦관련을 잘 재는 것과 이해는 달라요 — 그리고 눈길은 공짜가 아니에요|measuring relatedness is not understanding — and gaze is not free⟧", 12, "var(--ink)", cls="d"))

EYE_I = icon(f'<path d="M6 32 q26 -26 52 0 q-26 26 -52 0z" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>'
             f'<ellipse cx="14" cy="54" rx="7" ry="5" fill="{BEAN}"/><ellipse cx="32" cy="56" rx="7" ry="5" fill="{BEAN}"/><ellipse cx="50" cy="54" rx="7" ry="5" fill="{BEAN}"/>')
THICK_I = icon(f'<ellipse cx="14" cy="44" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="50" cy="44" rx="10" ry="7" fill="{BEAN}"/><path d="M14 36 Q32 6 50 36" stroke="var(--accent)" stroke-width="6" fill="none" stroke-linecap="round"/>'
               f'<path d="M32 44 Q41 30 50 36" stroke="var(--muted)" stroke-width="1.5" fill="none"/>')
LAYERS_I = icon('<rect x="16" y="40" width="40" height="12" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2.5"/><rect x="12" y="26" width="40" height="12" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2.5"/><rect x="8" y="12" width="40" height="12" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2.5"/>')
COST_I = icon(f'<rect x="4" y="38" width="56" height="16" rx="6" fill="var(--stone)"/>' + "".join(f'<ellipse cx="{12 + i * 10}" cy="34" rx="5" ry="3.5" fill="{BEAN}"/>' for i in range(5))
              + '<path d="M10 24 L54 24 M12 18 L52 18 M14 12 L50 12" stroke="var(--accent)" stroke-width="2" opacity="0.8"/><text x="52" y="12" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">$</text>')

PAGE = {
    "slug": "attention", "order": 31,
    "title": ("앵무새의 눈길", "The Parrot\'s Gaze"),
    "h1": ("<em>어텐션</em>이 뭐예요?", "What is <em>Attention</em>?"),
    "sub": ("어텐션(그리고 트랜스포머)을 다음 콩을 고를 때 쟁반 위 모든 콩을 훑어보고 관련 있는 콩을 더 오래 보는 앵무새의 눈길 이야기로 풀어봤어요.",
            "Attention (and the transformer), told as a story about a parrot that glances at every bean on the tray and looks longer at the related ones before picking the next."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '강가에 은행이 잔뜩 있어 — 무슨 은행?'이라 묻고, 횃대 위 앵무새가 '나무에서 떨어지는 은행이요!'라고 답함. 아래에 '돈 은행이 아니에요'", "A guest asks which bank, in a sentence about a bank by the river; the parrot on the perch answers the river bank, with a note: not the money bank"),
         "caption": ("헷갈리는 낱말인데, 앵무새가 헷갈리지 않고 맞혔어요.", "A confusing word — and the parrot got it right without getting confused."),
         "small": ("'은행'은 돈 은행일 수도, 나무 열매일 수도 있어요. 앵무새는 멀리 있는 '강가'를 보고 골랐어요. 어떻게요?", "Bank could mean money or river. The parrot chose by looking at river, far back in the sentence. How?")},
        {"svg": P2, "alt": ("콩 여섯 개가 한 줄. 앞쪽 '강가에' 콩은 흐려져 '잊었어요', 뒤쪽 콩 세 개만 점선 상자로 '여기만 봐요'. 빨간 앵무새가 땀 흘리며 '돈 은행이요!'", "Six beans in a row; the front river bean is faded and marked forgotten, only the last three are boxed as seen; a sweating red parrot says the money bank!"),
         "caption": ("옛날 앵무새는 바로 앞 콩 몇 개만 봤어요. 멀리 있는 콩은 잊었어요.", "The old parrot looked only at the last few beans. Far-away beans were forgotten."),
         "small": ("콩을 순서대로 하나씩만 읽으면, 처음 콩은 끝에 가서 흐려져요. 그래서 '강가'를 잊고 '돈 은행'을 골랐어요.", "Read the beans one by one in order, and the first ones fade by the end. So it forgot river and picked the money bank.")},
        {"svg": P3, "hero": True, "alt": ("앵무새가 쟁반 위 콩 일곱 개를 봄. 마지막 '은행?' 콩에서 앞쪽 '강가에' 콩으로 굵은 선, 다른 콩엔 가는 선. 오른쪽에 '눈길 층 1·2·3'이 겹겹이 쌓임 — 트랜스포머", "A parrot looks at seven beans on a tray; a thick line runs from the last bank? bean to the early river bean, thin lines to the others; on the right, gaze layers 1, 2, 3 stack up — a transformer"),
         "caption": ("어텐션은 다음 콩을 고를 때 모든 콩을 한 번씩 훑어보고, 관련 있는 콩을 더 오래 보는 거예요.", "Attention: when picking the next bean, the parrot glances at every bean and looks longer at the related ones."),
         "small": ('<a href="context-ko.html">쟁반</a> 위 <a href="token-ko.html">콩</a>들 사이 선 굵기가 눈길이에요. 이 눈길을 겹겹이 쌓은 앵무새 머리가 트랜스포머예요 — 요즘 <a href="llm-ko.html">앵무새</a>는 다 이렇게 생겼어요.',
                   'The thickness of the lines between <a href="token-en.html">beans</a> on the <a href="context-en.html">tray</a> is the gaze. A head that stacks this gaze in layers is a transformer — every modern <a href="llm-en.html">parrot</a> is built this way.'),
         "tricks": (4, [
             (EYE_I, ("모든 콩을 동시에 봐요", "Sees every bean at once"), ("순서대로가 아니라 한눈에", "all at once, not in order"), "calm"),
             (THICK_I, ("관련 콩엔 굵은 눈길", "Thicker gaze for related beans"), ("멀어도 관련이면 굵게", "far but related still thick"), "calm"),
             (LAYERS_I, ("눈길 층이 여러 겹", "Many layers of gaze"), ("층마다 다른 걸 봐요", "each layer looks differently"), "calm"),
             (COST_I, ("콩이 많으면 눈길도 많이", "More beans, more gaze"), ("쟁반 값이 여기서 나와요", "this is where tray cost comes from"), "warm"),
         ])},
        {"svg": P4, "alt": ("콩 여덟 개 줄 세 개. 층 1은 옆 콩끼리, 층 2는 멀리 떨어진 뜻이 통하는 콩끼리 굵은 선, 층 3은 마지막 콩에서 문장 전체로. 첫 줄 아래엔 순서 번호표 1~8", "Three rows of eight beans: layer 1 links neighbours, layer 2 links far-apart meaning pairs with thick lines, layer 3 links the last bean to the whole sentence; order tags 1 to 8 under the first row"),
         "caption": ("층마다 다른 눈길을 봐요. 번호표가 붙어 있어서 콩 순서도 알아요.", "Each layer looks differently. Order tags on the beans tell it which came first."),
         "small": ("한 번에 모든 콩을 보면 순서를 모를 것 같죠? 그래서 콩마다 번호표를 붙여요. 한 층 안에도 눈길 여러 갈래(헤드)가 있어서 여러 관련을 동시에 봐요.", "If it sees all beans at once, how does it know the order? Each bean wears a number tag. And within one layer there are several gaze strands (heads), each watching a different kind of relation.")},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새가 '강가 옆이니까 이쪽 은행!' — 눈길은 관련을 재지 뜻을 아는 게 아님. 오른쪽 빨강: 콩 4개엔 선 6개, 콩 8개엔 선 28개 — 콩이 2배면 눈길은 4배", "Left, green: the parrot says next to river, so this bank — the gaze measures relatedness, not meaning. Right, red: 4 beans need 6 lines, 8 beans need 28 — double the beans, four times the gaze"),
         "caption": ("관련을 잘 재는 것과 이해는 달라요. 그리고 눈길은 공짜가 아니에요.", "Measuring relatedness is not understanding. And gaze is not free."),
         "small": ('콩이 2배면 콩끼리 선은 4배예요. 그래서 긴 <a href="context-ko.html">쟁반</a>은 비싸고 느려요 — <a href="token-ko.html">콩</a>을 아끼는 이유가 여기 있어요. 앵무새가 여전히 뜻은 모른다는 건 <a href="llm-ko.html">첫 이야기</a>에서.',
                   'Double the beans and the lines between them quadruple. That is why a long <a href="context-en.html">tray</a> is slow and costly — and why saving <a href="token-en.html">beans</a> matters. That the parrot still does not know meaning is in <a href="llm-en.html">the first story</a>.')},
    ],
    "summary": (("<b>어텐션</b> = 다음 콩을 고를 때 쟁반 위 <b>모든 콩을 한 번씩 훑어보고</b>, 관련 있는 콩에 <b>눈길을 더 주는 것</b>. 이 눈길을 <b>겹겹이 쌓은</b> 앵무새 머리가 트랜스포머예요. 콩이 늘면 눈길 계산은 <b>제곱</b>으로 늘어요.",
                 "<b>Attention</b> = when picking the next bean, <b>glance at every bean on the tray</b> and <b>look longer at the related ones</b>. A head that <b>stacks this gaze in layers</b> is a transformer. More beans means gaze cost grows <b>with the square</b>."),
                ("Attention. 시퀀스의 각 토큰이 다른 모든 토큰과의 관련도(쿼리·키 내적)를 계산해 가중합을 만드는 연산이에요. 자기 자신 시퀀스 안에서 하면 셀프 어텐션, 여러 갈래로 나누면 멀티헤드. 위치 정보는 positional encoding 으로 따로 붙여요. 이 층을 쌓은 구조가 트랜스포머이고, 비용이 시퀀스 길이의 제곱이라 긴 컨텍스트가 비싸요.",
                 "An operation where each token in a sequence computes a relatedness score (query-key dot product) with every other token and forms a weighted sum. Within one sequence it is self-attention; split into several strands it is multi-head. Position is added separately via positional encoding. Stacking these layers gives the transformer, and because the cost scales with the square of sequence length, long contexts are expensive.")),
    "glossary": [
        ("어텐션", "Attention", ("앵무새의 눈길.", "The parrot\'s gaze."), ("다음 콩을 고를 때 모든 콩을 훑고, 관련 콩을 더 오래 봐요.", "Glance at every bean, look longer at the related ones, then pick the next.")),
        ("트랜스포머", "Transformer", ("눈길을 겹겹이 쌓은 머리.", "A head of stacked gaze layers."), ("요즘 앵무새는 거의 다 이 머리예요. GPT의 T가 이거예요.", "Nearly every modern parrot has this head. The T in GPT is this.")),
        ("셀프 어텐션", "Self-attention", ("쟁반 위 콩끼리 서로 보기.", "Beans on the tray watching each other."), ("밖이 아니라 같은 문장 안 콩끼리 눈길을 주고받아요.", "The gaze goes between beans in the same sentence, not anywhere else.")),
        ("층 · 헤드", "Layer · Head", ("눈길 층과 눈길 갈래.", "Gaze layers and gaze strands."), ("층은 위로 겹겹이, 헤드는 한 층 안에서 여러 갈래. 층마다 갈래마다 다른 관련을 봐요.", "Layers stack upward; heads are strands within one layer. Each watches a different kind of relation.")),
        ("위치 정보", "Positional encoding", ("콩마다 붙인 번호표.", "The number tag on each bean."), ("한꺼번에 보면 순서를 모르니까 번호표를 붙여요.", "Seeing everything at once loses the order, so each bean gets a tag.")),
        ("제곱 비용", "Quadratic cost", ("콩 2배면 눈길 4배.", "Double beans, four times the gaze."), ("콩끼리 전부 선을 잇기 때문이에요. 긴 쟁반이 비싼 이유.", "Because every bean connects to every other. Why long trays cost.")),
        ("컨텍스트 창", "Context window", ("쟁반.", "The tray."), ('눈길이 닿는 콩은 쟁반 위 콩뿐이에요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'The gaze only reaches beans on the tray. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("LLM", "LLM", ("책 산더미 앵무새.", "The mountain-of-books parrot."), ('이 눈길 머리로 책을 읽은 새예요. → <a href="llm-ko.html">책을 산더미로 읽은 앵무새</a>', 'The bird that read its books with this gazing head. → <a href="llm-en.html">the parrot that read a mountain of books</a>')),
    ],
}
