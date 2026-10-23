from _draw import *
from _world import *

# 1. 관리자가 전표 더미를 하나씩 손으로 더해요
P1 = svg(300, sky(300)
         + person(380, 160, s=0.85, face=SWEAT + EYES, **MANAGER)
         + receipt(260, 130, 0.45) + receipt(300, 160, 0.45) + receipt(340, 120, 0.45)
         + receipt(420, 150, 0.45) + receipt(460, 120, 0.45) + receipt(500, 160, 0.45)
         + label(380, 250, "⟦이번 분기 지역별 재고 변화가 궁금한데|I want to know how inventory changed by region this quarter⟧", 12, "var(--ink)")
         + label(380, 285, "⟦전표를 하나씩 손으로 더해야 해요|but every receipt has to be added up by hand⟧", 12, "var(--bad)"))

# 2. 전표 처리 시스템은 한 건은 빠른데, 전체 집계는 느려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.75, face=SMILE, **PACKER) + receipt(280, 210, 0.5, text="⟦방금 상자 1개|just 1 box, right now⟧")
         + label(220, 90, "✓ ⟦빨라요|fast⟧", 13, "var(--good)")
         + person(560, 130, s=0.75, face=FROWN, **MANAGER) + label(560, 250, "⟦1년치 전체 합계는?|but a whole year's total?⟧", 11, "var(--bad)")
         + label(560, 90, "✕ ⟦느려요|slow⟧", 13, "var(--bad)")
         + label(380, 280, "⟦한 건 처리(OLTP)와 전체 분석은 다른 일이에요|handling one record and analyzing everything are different jobs⟧", 12, "var(--ink)"))

# 3. OLAP = 미리 쌓아둔 큐브를 이리저리 잘라보기 (hero)
P3 = svg(340, sky(340, ground=False)
         + '<g transform="translate(300,120)">'
         + '<path d="M0 60 L90 20 L220 60 L130 100 Z" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>'
         + '<path d="M0 60 L130 100 L130 180 L0 140 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
         + '<path d="M220 60 L130 100 L130 180 L220 140 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '</g>'
         + label(80, 90, "⟦지역|region⟧", 11, "var(--muted)") + label(330, 90, "⟦기간|time⟧", 11, "var(--muted)") + label(610, 220, "⟦품목|item⟧", 11, "var(--muted)")
         + label(380, 30, "⟦OLAP = 지역·기간·품목으로 미리 쌓아둔 큐브를 이리저리 잘라보기|OLAP = pre-stacked data, sliced by region, time, and item, any way you like⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦어느 단면으로 잘라봐도 바로 답이 나와요|slice it any way, and the answer is right there⟧", 12, "var(--muted)"))

# 4. OLTP vs OLAP
P4 = svg(320, sky(320, ground=False)
         + '<rect x="40" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="390" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(205, 66, "⟦OLTP|OLTP⟧", 13, "var(--ink)", weight=700)
         + label(555, 66, "⟦OLAP|OLAP⟧", 13, "var(--ink)", weight=700)
         + label(205, 100, "⟦전표 한 건 입출고|one receipt in or out⟧", 10.5, "var(--muted)")
         + label(205, 130, "⟦짧고 빠른 거래 처리|short, fast transactions⟧", 10.5, "var(--good)")
         + label(205, 160, "⟦'지금 이 상자'엔 정확해요|accurate about 'this one box, right now'⟧", 10.5, "var(--good)")
         + label(555, 100, "⟦지역×기간×품목 큰 집계|big aggregates across region × time × item⟧", 10.5, "var(--muted)")
         + label(555, 130, "⟦긴 분석 질문에 강해요|strong on big analytical questions⟧", 10.5, "var(--good)")
         + label(555, 160, "⟦'지금 이 순간'은 조금 늦을 수 있어요|'right this instant' can lag a bit⟧", 10.5, "var(--bad)")
         + label(380, 300, "⟦포장 담당은 OLTP를, 관리자는 OLAP을 써요|the worker uses OLTP; the manager uses OLAP⟧", 12, "var(--ink)"))

# 5. 한계: 실시간 한 건엔 안 맞고, 집계는 시차가 있어요
P5 = svg(300, sky(300, ground=False)
         + person(260, 150, s=0.8, face=EYES, **MANAGER)
         + label(260, 258, "⟦큐브는 보통 한 번씩 모아 쌓여요|the cube is usually rebuilt in batches⟧", 11, "var(--ink)")
         + label(260, 280, "⟦최신 변화는 살짝 늦게 반영돼요|the very latest changes show up a bit late⟧", 11, "var(--muted)")
         + indexcard(560, 150, 1.0, tags=["지", "기"])
         + label(560, 220, "⟦색인구조가 큐브 조회를 더 빠르게 해줘요|index structures make cube lookups even faster⟧", 11, "var(--ink)")
         + label(380, 40, "⟦OLAP은 '지금 이 한 건'엔 안 맞아요|OLAP isn't for 'just this one record, right now'⟧", 13, "var(--ink)"))

CUBE_I = icon('<path d="M10 24 L32 12 L54 24 L32 36 Z" fill="var(--good)"/><path d="M10 24 L32 36 L32 54 L10 42 Z" fill="var(--good)" opacity="0.7"/><path d="M54 24 L32 36 L32 54 L54 42 Z" fill="var(--good)" opacity="0.5"/>')
SLICE_I = icon('<rect x="8" y="12" width="48" height="40" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="8" y="12" width="16" height="40" fill="var(--accent)"/>')
DRILL_I = icon('<circle cx="24" cy="24" r="14" fill="none" stroke="var(--muted)" stroke-width="3"/><circle cx="24" cy="24" r="6" fill="var(--accent)"/><path d="M34 34 l16 16" stroke="var(--muted)" stroke-width="4"/>')
PIVOT_I = icon('<path d="M20 44 A18 18 0 1 1 44 44" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M44 44 l8 -4 l-2 10 Z" fill="var(--good)"/>')

PAGE = {
    "slug": "olap", "order": 15,
    "title": ("전체를 썰어보는 창고 관리자", "The Manager Who Slices the Whole Warehouse"),
    "h1": ("<em>OLAP</em>이 뭐예요?", "What is <em>OLAP</em>?"),
    "sub": ("OLAP을, 박스 하나하나를 처리하는 일과 달리 전체 재고를 지역·기간·품목으로 썰어보는 창고 관리자 이야기로 풀어봤어요.",
            "OLAP, told as a story about a manager slicing the whole warehouse's inventory by region, time, and item — instead of handling one box at a time."),
    "panels": [
        {"svg": P1, "alt": ("관리자가 전표 더미를 두고 땀을 흘리며 지역별 분기 재고 변화를 손으로 더하려 함", "The manager sweats over a pile of receipts, trying to hand-add the quarter's regional inventory changes"),
         "caption": ("이번 분기 지역별 재고 변화가 궁금한데, 전표를 하나씩 손으로 더해야 해요.", "Wanting to know regional changes this quarter means adding every receipt by hand."),
         "small": ("전표 더미만으론 전체 그림이 바로 안 보여요.", "A pile of receipts alone doesn't show the big picture.")},
        {"svg": P2, "alt": ("왼쪽: 포장 담당이 상자 하나를 빠르게 처리함. 오른쪽: 관리자가 1년치 합계 앞에서 곤란해함", "Left: a worker handles one box quickly. Right: the manager struggles with a year's total"),
         "caption": ("한 건 처리는 빠른데, 전체 집계는 느려요.", "One record is fast; the full aggregate is slow."),
         "small": ("한 건 처리(OLTP)와 전체 분석은 다른 일이에요.", "Handling one record and analyzing everything are different jobs.")},
        {"svg": P3, "hero": True, "alt": ("지역·기간·품목 세 축으로 쌓인 큐브 모양의 데이터 블록", "A cube-shaped data block stacked along three axes — region, time, and item"),
         "caption": ("OLAP은 지역·기간·품목으로 미리 쌓아둔 큐브를 이리저리 잘라봐요.", "OLAP pre-stacks data by region, time, and item, and slices it any way you like."),
         "small": ("어느 단면으로 잘라봐도 바로 답이 나와요.", "Slice it any way, and the answer is right there."),
         "tricks": (4, [
             (CUBE_I, ("큐브로 미리 쌓기", "Pre-stack into a cube"), ("여러 기준을 미리 합쳐둬요", "pre-aggregated across axes")),
             (SLICE_I, ("잘라서 보기", "Slice and dice"), ("한 기준으로 뚝 잘라봐요", "cut straight through one axis"), "calm"),
             (DRILL_I, ("파고들기", "Drill down"), ("분기→월→일로 들어가요", "quarter → month → day")),
             (PIVOT_I, ("축 바꿔보기", "Pivot"), ("보는 기준을 돌려봐요", "rotate which axis you view by"), "warm"),
         ])},
        {"svg": P4, "alt": ("OLTP와 OLAP을 처리 단위와 속도, 강점 기준으로 비교한 표", "A table comparing OLTP and OLAP by unit of work, speed, and strengths"),
         "caption": ("포장 담당은 OLTP를, 관리자는 OLAP을 써요.", "The worker uses OLTP; the manager uses OLAP."),
         "small": ("'지금 이 상자'는 OLTP가, '전체 추이'는 OLAP이 맡아요.", "OLTP handles 'this box right now'; OLAP handles the overall trend.")},
        {"svg": P5, "alt": ("관리자가 큐브는 배치로 쌓인다고 설명하고, 다차원 색인 카드가 큐브 조회를 돕는 모습", "The manager explains the cube is rebuilt in batches, while a multi-dimensional index card helps speed up lookups"),
         "caption": ("OLAP은 '지금 이 한 건'엔 안 맞아요.", "OLAP isn't for 'just this one record, right now'."),
         "small": ("큐브는 보통 한 번씩 모아 쌓이고, 색인구조가 조회를 더 빠르게 해줘요.", "The cube is usually rebuilt in batches, and index structures speed up its lookups.")},
    ],
    "summary": (("<b>OLAP</b>(온라인 분석처리)은 전체 데이터를 <b>여러 기준(지역·기간·품목)으로 미리 쌓아두고 이리저리 잘라보며</b> 분석하는 방식이에요.",
                 "<b>OLAP</b> (Online Analytical Processing) analyzes the whole dataset by <b>pre-aggregating it across several axes — region, time, item — and slicing it any way you like</b>."),
                ("한 건의 거래를 빠르게 처리하는 OLTP와 달리, OLAP은 큐브(다차원 집계) 구조로 슬라이스/다이스·드릴다운·롤업·피벗 같은 분석 연산을 빠르게 지원해요. 보통 데이터 웨어하우스에 쌓인 데이터를 스타 스키마로 모델링해 큐브를 만들고, 최신 거래 반영에는 배치 주기만큼의 시차가 있어요.",
                 "Unlike OLTP, which processes one transaction quickly, OLAP uses a cube (multi-dimensional aggregate) structure to support fast slice/dice, drill-down, roll-up, and pivot operations. It's typically built by modeling data warehouse data into a star schema, and reflecting the very latest transactions lags by however often the cube batch-refreshes.")),
    "glossary": [
        ("OLTP", "OLTP", ("전표 한 건을 빠르게 처리.", "Processing one receipt quickly."), ("OLAP과 짝을 이루는 개념이에요.", "The counterpart concept to OLAP.")),
        ("큐브", "Cube", ("여러 기준으로 미리 쌓아둔 블록.", "A block pre-stacked across several axes."), ("OLAP 분석의 핵심 구조예요.", "The core structure behind OLAP analysis.")),
        ("슬라이스/다이스", "Slice & Dice", ("한 단면·여러 단면으로 잘라보기.", "Cutting one slice, or several, out of the cube."), ("큐브를 보는 기본 동작이에요.", "The basic way of viewing a cube.")),
        ("드릴다운", "Drill-down", ("큰 단위에서 작은 단위로 파고들기.", "Digging from a big unit into a smaller one."), ("분기→월→일처럼 내려가요.", "Quarter → month → day, for example.")),
        ("피벗/롤업", "Pivot / Roll-up", ("보는 축을 바꾸거나 합쳐보기.", "Rotating the view axis, or rolling values up."), ("같은 데이터를 다른 각도로 봐요.", "Views the same data from a different angle.")),
        ("스타 스키마", "Star Schema", ("큐브를 만드는 테이블 모델링 방식.", "The table design used to build a cube."), ("사실 테이블과 차원 테이블로 나눠요.", "Splits into fact tables and dimension tables.")),
        ("다차원 색인", "Multi-dimensional Index", ("큐브 조회를 빠르게 돕는 색인.", "The index that speeds up cube lookups."), ('같은 세계의 다른 페이지예요. → <a href="multiindex-ko.html">여러 딱지로 한 번에 찾기</a>', "A related page in the same world. → <a href=\"multiindex-en.html\">finding by several tags at once</a>")),
        ("배치 집계 지연", "Batch Refresh Lag", ("큐브가 한 번씩 모아 쌓이는 주기.", "The cycle on which the cube is rebuilt."), ("최신 변화는 살짝 늦게 반영돼요.", "The very latest changes show up a bit late.")),
    ],
}
