from _draw import *
from _world import *

# 1. 두 가지 조건을 동시에 찾아달라는 요청
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **DRIVER)
         + bubble(60, 70, 260, 50, "⟦B구역에 있으면서, 이번 주 유통기한인 상자요!|boxes that are both in zone B AND expiring this week!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + shelfzone(430, 150, 260, 90, 1.0, bad=1)
         + label(560, 270, "⟦분류 담당이 선반을 처음부터 다 뒤져야 해요|the sorter has to search every shelf from the start⟧", 12, "var(--bad)"))

# 2. 색인 하나로는 한 기준만 빨라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 150, s=0.85, face=SWEAT + EYES, **SORTER)
         + indexcard(230, 90, 1.0, tags=["B"])
         + label(230, 150, "⟦구역 색인만 있어요|only a zone index⟧", 11, "var(--ink)")
         + label(530, 90, "✕", 30, "var(--bad)", cls="d")
         + label(530, 150, "⟦유통기한은 색인이 없어요|no index for expiry date⟧", 11, "var(--bad)")
         + label(380, 260, "⟦기준 하나로는 다른 기준까지 빨라지진 않아요|an index for one thing doesn't speed up the other⟧", 12, "var(--ink)"))

# 3. 다차원 색인구조 = 카드 한 장에 여러 딱지 (hero)
P3 = svg(340, sky(340, ground=False)
         + indexcard(380, 150, 1.8, tags=["B", "✓", "가"])
         + label(380, 30, "⟦다차원 색인구조 = 카드 한 장에 여러 딱지를 동시에 붙이기|Multi-dimensional index = several tags on one card at once⟧", 13.5, "var(--ink)", cls="d")
         + label(260, 250, "⟦구역|zone⟧", 11, "var(--muted)") + label(380, 250, "⟦유통기한|expiry⟧", 11, "var(--muted)") + label(500, 250, "⟦분류|category⟧", 11, "var(--muted)")
         + label(380, 320, "⟦어느 조합으로 찾아도 바로 찾아내요|find it fast no matter which combination you ask by⟧", 12, "var(--muted)"))

# 4. R-트리 스타일: 공간을 나눠 좁혀가기
P4 = svg(320, sky(320, ground=False)
         + '<rect x="60" y="60" width="300" height="200" rx="4" fill="none" stroke="var(--line)" stroke-width="3"/>'
         + '<rect x="80" y="80" width="120" height="90" rx="3" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>'
         + '<rect x="220" y="140" width="120" height="100" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
         + box(140, 125, 0.6) + box(280, 190, 0.6, twin=True)
         + label(210, 50, "⟦공간을 네모로 나눠 좁혀가요(R-트리)|narrow down by splitting space into boxes (R-tree)⟧", 11, "var(--ink)")
         + '<rect x="420" y="60" width="280" height="200" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(560, 86, "⟦비트맵 색인|bitmap index⟧", 11, "var(--ink)", weight=700)
         + label(445, 115, "B구역", 10, "var(--muted)") + label(445, 140, "✓유통기한", 10, "var(--muted)") + label(445, 165, "가분류", 10, "var(--muted)")
         + ''.join(f'<rect x="{520+i*26}" y="105" width="18" height="18" rx="2" fill="{"var(--good)" if b else "var(--line)"}"/>' for i, b in enumerate([1,0,1,1,0]))
         + ''.join(f'<rect x="{520+i*26}" y="130" width="18" height="18" rx="2" fill="{"var(--good)" if b else "var(--line)"}"/>' for i, b in enumerate([1,1,0,1,0]))
         + ''.join(f'<rect x="{520+i*26}" y="155" width="18" height="18" rx="2" fill="{"var(--good)" if b else "var(--line)"}"/>' for i, b in enumerate([0,1,1,0,1]))
         + label(560, 210, "⟦있다/없다를 0·1로 겹쳐 빨리 걸러요|stack 0/1 flags to filter fast⟧", 10.5, "var(--muted)")
         + label(380, 295, "⟦목적에 따라 다른 모양의 다차원 색인을 써요|different shapes of multi-dim index fit different jobs⟧", 12, "var(--ink)"))

# 5. 공짜가 아니에요 — 쓰기 비용, 차원의 저주, 벡터 색인으로 이어짐
P5 = svg(300, sky(300, ground=False)
         + person(260, 150, s=0.8, face=SWEAT + EYES, **SORTER)
         + indexcard(260, 90, 0.9, tags=["A", "B", "C", "D"])
         + label(260, 240, "⟦딱지가 많아질수록 새 상자 넣기도 느려져요|more tags means every new box takes longer to file⟧", 11.5, "var(--bad)")
         + indexcard(560, 150, 1.1, tags=["～"])
         + label(560, 220, "⟦비슷한 느낌끼리 찾는 색인도 있어요|some indexes find things by similarity⟧", 11, "var(--ink)")
         + label(560, 250, "⟦(AI 세계의 벡터 색인)|(vector index, in the AI world)⟧", 10.5, "var(--muted)"))

MULTI_I = icon('<rect x="12" y="12" width="40" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="2" width="12" height="12" rx="2" fill="var(--accent)"/><rect x="26" y="2" width="12" height="12" rx="2" fill="var(--good)"/>')
SPACE_I = icon('<rect x="8" y="8" width="48" height="48" rx="3" fill="none" stroke="var(--line)" stroke-width="3"/><rect x="18" y="18" width="20" height="18" rx="2" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>')
BIT_I = icon('<rect x="10" y="22" width="12" height="12" fill="var(--good)"/><rect x="26" y="22" width="12" height="12" fill="var(--line)"/><rect x="42" y="22" width="12" height="12" fill="var(--good)"/>')
SIM_I = icon('<circle cx="22" cy="26" r="9" fill="var(--accent)"/><circle cx="42" cy="30" r="7" fill="var(--accent)" opacity="0.7"/><circle cx="32" cy="46" r="6" fill="var(--accent)" opacity="0.5"/>')

PAGE = {
    "slug": "multiindex", "order": 11,
    "title": ("여러 딱지로 한 번에 찾기", "Finding by Several Tags at Once"),
    "h1": ("<em>다차원 색인구조</em>가 뭐예요?", "What is a <em>Multi-dimensional Index Structure</em>?"),
    "sub": ("다차원 색인구조를, 재고 카드에 구역·유통기한·분류 같은 여러 딱지를 동시에 붙여 한 번에 찾는 이야기로 풀어봤어요.",
            "Multi-dimensional index structures, told as a story about tagging an inventory card with zone, expiry, and category all at once."),
    "panels": [
        {"svg": P1, "alt": ("배송 기사가 구역과 유통기한 두 조건을 동시에 요청하지만, 선반에 표시된 구역은 하나뿐", "A driver asks for two conditions at once — zone and expiry — but the shelf is only marked by zone"),
         "caption": ("B구역이면서 이번 주 유통기한인 상자를 찾아달래요.", "They want boxes that are both in zone B and expiring this week."),
         "small": ("분류 담당이 선반을 처음부터 다 뒤져야 해요.", "The sorter has to search every shelf from the start.")},
        {"svg": P2, "alt": ("분류 담당 땀을 흘리며, 구역 색인 카드는 있지만 유통기한 색인은 없다고 ✕ 표시됨", "The sorter sweats — there's a zone index card, but an X marks the missing expiry index"),
         "caption": ("색인 하나로는 한 기준만 빨라요.", "One index only speeds up one thing."),
         "small": ("기준 하나로는 다른 기준까지 빨라지진 않아요.", "An index for one thing doesn't speed up the other.")},
        {"svg": P3, "hero": True, "alt": ("큰 색인 카드 한 장에 구역·유통기한·분류 세 가지 딱지가 동시에 붙어 있음", "One big index card carries zone, expiry, and category tags all at once"),
         "caption": ("다차원 색인구조는 카드 한 장에 여러 딱지를 동시에 붙여요.", "A multi-dimensional index puts several tags on one card at once."),
         "small": ("어느 조합으로 찾아도 바로 찾아내요.", "Find it fast no matter which combination you ask by."),
         "tricks": (4, [
             (MULTI_I, ("여러 딱지 동시에 붙이기", "Tag by several keys at once"), ("복합 색인이에요", "a composite index")),
             (SPACE_I, ("공간을 나눠 찾기", "Narrow down by space"), ("R-트리 방식이에요", "the R-tree approach"), "calm"),
             (BIT_I, ("있다/없다로 빨리 거르기", "Filter fast with yes/no"), ("비트맵 색인이에요", "a bitmap index")),
             (SIM_I, ("비슷한 것끼리 묶어 찾기", "Group by similarity"), ("벡터 검색에 쓰여요", "used for vector search"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 공간을 네모로 나눠 좁혀가는 R-트리. 오른쪽: 0과 1로 겹쳐 거르는 비트맵 색인", "Left: an R-tree narrowing space by nested boxes. Right: a bitmap index stacking 0s and 1s"),
         "caption": ("목적에 따라 다른 모양의 다차원 색인을 써요.", "Different shapes of multi-dimensional index fit different jobs."),
         "small": ("공간이면 R-트리, 있다/없다면 비트맵이에요.", "Space calls for an R-tree; yes/no calls for a bitmap.")},
        {"svg": P5, "alt": ("왼쪽: 딱지가 네 개나 붙어 상자 넣기가 느려진 분류 담당. 오른쪽: 비슷한 느낌끼리 찾는 색인 카드", "Left: four tags slow down the sorter filing a new box. Right: an index card marked for similarity search"),
         "caption": ("딱지가 많아질수록 새 상자 넣기도 느려져요.", "More tags means every new box takes longer to file."),
         "small": ("비슷한 느낌끼리 찾는 벡터 색인도 있어요.", "There's also a vector index that finds things by similarity.")},
    ],
    "summary": (("<b>다차원 색인구조</b>는 하나의 기준이 아니라 <b>여러 속성을 동시에</b> 빠르게 찾도록 만든 색인이에요.",
                 "A <b>multi-dimensional index structure</b> is built to search quickly by <b>several attributes at once</b>, not just one."),
                ("하나의 컬럼만 정렬해 두는 일반 색인과 달리, 다차원 색인은 공간(R-트리, k-d 트리), 값의 유무(비트맵), 벡터 유사도 등 여러 방식으로 여러 조건을 동시에 다뤄요. 단점은 색인이 많아질수록 입력(쓰기) 비용이 커지고, 기준(차원)이 너무 많아지면 오히려 효율이 떨어지는 '차원의 저주'가 생긴다는 점이에요.",
                 "Unlike a plain index sorted by one column, a multi-dimensional index handles several conditions together — through space (R-trees, k-d trees), presence/absence (bitmaps), or vector similarity. The trade-off: more indexes raise write cost, and too many dimensions bring on the 'curse of dimensionality', where efficiency actually drops.")),
    "glossary": [
        ("복합 색인", "Composite Index", ("여러 컬럼을 묶어 만든 색인.", "An index built from several columns together."), ("순서도 성능에 영향을 줘요.", "Column order affects performance too.")),
        ("R-트리", "R-tree", ("공간을 네모로 나눠 좁혀가는 색인.", "An index that narrows space by nested boxes."), ("지도·좌표 데이터에 많이 써요.", "Common for map and coordinate data.")),
        ("비트맵 색인", "Bitmap Index", ("있다/없다를 0·1로 겹쳐보는 색인.", "An index stacking yes/no as 0s and 1s."), ("값 종류가 적을 때 빨라요.", "Fast when there are few distinct values.")),
        ("차원의 저주", "Curse of Dimensionality", ("기준이 너무 많아지면 느려짐.", "Too many dimensions, and it slows down."), ("색인이 오히려 덜 효과적이 돼요.", "The index becomes less effective, not more.")),
        ("공간 색인", "Spatial Index", ("위치 기준으로 찾는 색인.", "An index searched by location."), ("R-트리가 대표적인 구현이에요.", "The R-tree is a typical implementation.")),
        ("벡터 색인", "Vector Index", ("뜻이 비슷한 것끼리 찾는 색인.", "An index that finds things by meaning."), ('AI 세계에서 임베딩 검색에 써요. → <a href="vectordb-ko.html">의미로 찾는 창고</a>', 'Used for embedding search in the AI world. → <a href="vectordb-en.html">a warehouse that searches by meaning</a>')),
        ("쓰기 비용", "Write Overhead", ("새 상자 넣을 때마다 드는 수고.", "The extra work every time a new box is filed."), ("색인이 많을수록 입력은 느려져요.", "More indexes mean slower inserts.")),
        ("커버링 색인", "Covering Index", ("색인만 보고 답을 다 주는 경우.", "When the index alone answers the question."), ("선반까지 안 가도 돼서 더 빨라요.", "No trip to the shelf needed — even faster.")),
    ],
}
