from _draw import *
from _world import *

# 1. 문제: 물건 모양이 다 달라서 고정 칸 선반에 안 들어가요
P1 = svg(320, sky(320)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **SORTER)
         + shelfzone(260, 150, 420, 90, 0.9, n=4)
         + label(470, 110, "⟦이 칸들은 모양이 다 똑같아요|these slots are all the same shape⟧", 12, "var(--muted)")
         + label(400, 270, "⟦그런데 들어올 상자는 모양이 다 달라요|but the boxes arriving all have different shapes⟧", 13, "var(--bad)")
         + label(400, 300, "⟦긴 상자, 둥근 상자, 묶음 상자...|long boxes, round boxes, bundled boxes...⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 억지로 끼우면 칸이 남거나 넘쳐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shelfzone(190, 120, 380, 100, 0.9, n=4, bad=1)
         + label(380, 90, "⟦억지로 끼웠더니 한 칸은 비고, 한 칸은 넘쳐요|forcing it in leaves one slot empty, one overflowing⟧", 12, "var(--bad)")
         + person(640, 180, s=0.75, face=FROWN, **SORTER)
         + label(380, 260, "⟦고정된 칸 모양이 오히려 발목을 잡아요|the fixed slot shape gets in the way⟧", 13, "var(--ink)"))

# 3. hero: NoSQL = 상자 모양에 맞춰 선반을 자유롭게 바꾸는 창고
KV_I = icon('<rect x="8" y="24" width="20" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="24" width="22" height="18" rx="3" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3"/>')
DOC_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 20 h24 M20 28 h24 M20 36 h16" stroke="#142033" stroke-width="2.5"/>')
COL_I = icon('<rect x="10" y="8" width="10" height="48" fill="#2E8B57"/><rect x="24" y="8" width="10" height="48" fill="#2E8B57" opacity="0.7"/><rect x="38" y="8" width="10" height="48" fill="#2E8B57" opacity="0.4"/>')
GRAPH_I = icon('<circle cx="18" cy="18" r="9" fill="var(--accent)"/><circle cx="48" cy="18" r="9" fill="var(--accent)"/><circle cx="32" cy="48" r="9" fill="var(--accent)"/><path d="M18 18 L48 18 M18 18 L32 48 M48 18 L32 48" stroke="#8B5E3C" stroke-width="2.5"/>')

P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **SORTER)
         + box(210, 200, 0.6, color="#2E8B57") + box(290, 200, 0.5, color="#5B8DEF")
         + box(470, 210, 0.7, color="#E9B44C") + indexcard(560, 200, 0.7, tags=["x", "y"])
         + label(380, 30, "⟦NoSQL = 상자 모양에 맞춰 선반을 자유롭게 바꾸는 창고|NoSQL = a warehouse that reshapes its shelves to fit the box⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦고정 칸이 아니라, 담는 방식이 여러 가지예요|not one fixed slot — many different ways to store⟧", 12, "var(--muted)"))

# 4. 네 가지 유형 비교
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦NoSQL 네 가지 유형|four NoSQL types⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + _row(80, "⟦Key-Value — 번호표로 바로 꺼내기|key-value — fetch by tag directly⟧", "⟦예: 캐시|e.g. cache⟧")
         + _row(116, "⟦Document — 상자 안에 자유 형식|document — free-form inside the box⟧", "⟦예: 상품 정보|e.g. product info⟧")
         + _row(152, "⟦Column-family — 세로로 길게 빨리 꺼내기|column-family — fast column reads⟧", "⟦예: 로그|e.g. logs⟧")
         + _row(188, "⟦Graph — 상자끼리 끈으로 연결|graph — boxes linked by string⟧", "⟦예: 친구 관계|e.g. friend networks⟧")
         + label(380, 250, "⟦관계형 창고(정규화)와는 상자를 담는 방식부터 달라요|a different way of storing boxes from the relational (normalized) warehouse⟧", 12, "var(--muted)"))

# 5. 한계: 자유로운 대신 복잡한 관계 질문은 여전히 어려워요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + box(190, 150, 1.0, color="#2E8B57") + label(190, 220, "⟦자유로운 모양, 빠른 저장|flexible shape, fast storage⟧", 11, "var(--ink)")
         + receipt(570, 150, 0.9, void=True) + label(570, 240, "⟦여러 상자를 동시에 묶는 전표(트랜잭션)는 약해요|a receipt binding many boxes at once is weak here⟧", 11, "var(--ink)")
         + label(380, 282, "⟦ACID을 다 지키는 창고는 따로 있어요|a warehouse that fully keeps ACID is a separate story⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "nosqltype", "order": 2,
    "title": ("상자 모양에 맞춰 선반을 바꾸는 창고", "The Warehouse That Reshapes Its Shelves"),
    "h1": ("<em>NoSQL 유형·모델링</em>이 뭐예요?", "What is <em>NoSQL Types & Modeling</em>?"),
    "sub": ("NoSQL의 네 가지 유형을, 상자 모양에 맞춰 선반을 자유롭게 바꾸는 창고 이야기로 풀어봤어요.",
            "The four NoSQL types, told as a story about a warehouse that reshapes its shelves to fit each box."),
    "panels": [
        {"svg": P1, "alt": ("분류 담당이 모양이 다 다른 상자들 앞에서 땀을 흘리며 고정 선반을 바라봄", "A sorter sweats in front of boxes of different shapes, facing a fixed shelf"),
         "caption": ("들어올 상자는 모양이 다 달라요.", "The boxes arriving all have different shapes."),
         "small": ("긴 상자, 둥근 상자, 묶음 상자...", "Long boxes, round boxes, bundled boxes...")},
        {"svg": P2, "alt": ("고정된 선반에 억지로 상자를 끼워 한 칸은 비고 한 칸은 넘침", "Forcing boxes into a fixed shelf leaves one slot empty and one overflowing"),
         "caption": ("억지로 끼웠더니 한 칸은 비고, 한 칸은 넘쳐요.", "Forcing it in leaves one slot empty, one overflowing."),
         "small": ("고정된 칸 모양이 오히려 발목을 잡아요.", "The fixed slot shape gets in the way.")},
        {"svg": P3, "hero": True, "alt": ("분류 담당이 상자 모양에 맞춰 선반을 자유롭게 바꿔 담음", "The sorter freely reshapes the shelf to fit each box's shape"),
         "caption": ("NoSQL = 상자 모양에 맞춰 선반을 자유롭게 바꾸는 창고예요.", "NoSQL is a warehouse that reshapes its shelves to fit the box."),
         "small": ("고정 칸이 아니라, 담는 방식이 여러 가지예요.", "Not one fixed slot — many different ways to store."),
         "tricks": (4, [
             (KV_I, ("Key-Value", "Key-Value"), ("번호표로 바로 꺼내요", "fetch straight by tag"), "calm"),
             (DOC_I, ("Document", "Document"), ("상자 안이 자유 형식이에요", "free-form inside the box")),
             (COL_I, ("Column-family", "Column-family"), ("세로로 빨리 꺼내요", "fast column-wise reads"), "warm"),
             (GRAPH_I, ("Graph", "Graph"), ("상자끼리 끈으로 연결해요", "boxes linked by string")),
         ])},
        {"svg": P4, "alt": ("Key-Value, Document, Column-family, Graph 네 유형을 설명하는 표", "A table explaining key-value, document, column-family, and graph types"),
         "caption": ("NoSQL은 네 가지 유형으로 나뉘어요.", "NoSQL splits into four types."),
         "small": ("관계형 창고(정규화)와는 상자를 담는 방식부터 달라요.", "A different storage approach from the relational (normalized) warehouse.")},
        {"svg": P5, "alt": ("왼쪽: 자유로운 모양과 빠른 저장. 오른쪽: 여러 상자를 묶는 전표(트랜잭션)는 약함", "Left: flexible shape, fast storage. Right: a receipt binding many boxes is weak"),
         "caption": ("자유로운 대신 여러 상자를 한 번에 묶는 일은 약해요.", "Flexible, but binding many boxes at once is weaker."),
         "small": ("ACID을 다 지키는 창고는 따로 있어요.", "A warehouse that fully keeps ACID is a separate story.")},
    ],
    "summary": (("<b>NoSQL</b> = 고정된 테이블 칸 대신, <b>Key-Value·Document·Column-family·Graph</b> 등 상자 모양에 맞는 방식으로 담는 창고.",
                 "<b>NoSQL</b> is a warehouse that stores data in whatever shape fits — key-value, document, column-family, or graph — instead of fixed table slots."),
                ("NoSQL(Not Only SQL)은 고정 스키마 없이 대용량·비정형 데이터를 유연하게 다루는 데이터 모델의 통칭으로, 수평 확장(샤딩)에 유리하지만 보통 ACID 트랜잭션은 관계형 DB보다 제한적으로 지원해요. 모델링은 조회 패턴을 먼저 정하고 그에 맞춰 데이터를 반정규화해 담는 식으로 이뤄져요.",
                 "NoSQL (\"Not Only SQL\") is an umbrella term for data models that handle large, unstructured data flexibly without a fixed schema. It favors horizontal scaling (sharding) but typically supports ACID transactions more narrowly than relational DBs. Modeling starts from query patterns and denormalizes data to fit them.")),
    "glossary": [
        ("Key-Value", "Key-Value", ("번호표 하나로 상자 하나.", "One tag, one box."), ("가장 단순하고 빨라요.", "The simplest and fastest kind.")),
        ("Document", "Document", ("상자 안에 자유 형식으로 담기.", "Free-form content inside the box."), ("JSON처럼 중첩 구조를 담아요.", "Holds nested structure like JSON.")),
        ("Column-family", "Column-family", ("세로로 긴 선반.", "A tall, column-shaped shelf."), ("특정 속성만 빨리 꺼내요.", "Fast at fetching specific attributes.")),
        ("Graph", "Graph", ("상자끼리 끈으로 연결.", "Boxes linked by string."), ("관계 추적에 강해요.", "Strong at tracing relationships.")),
        ("정규화", "Normalization", ("고정 선반에 중복 없이 담는 규칙.", "The rule of storing without duplication on fixed shelves."), ('NoSQL은 이 규칙을 느슨하게 써요. → <a href="normalization-ko.html">한 칸에 한 번만 적는 규칙</a>', 'NoSQL applies this rule loosely. → <a href="normalization-en.html">the rule of writing it once</a>')),
        ("샤딩/파티셔닝", "Sharding/Partitioning", ("창고를 구역으로 쪼개는 것.", "Splitting the warehouse into zones."), ('NoSQL은 보통 이걸 쉽게 지원해요. → <a href="dbsharding-ko.html">구역으로 쪼갠 창고</a>', 'NoSQL usually supports this easily. → <a href="dbsharding-en.html">the warehouse split into zones</a>')),
        ("ACID", "ACID", ("전표가 지키는 네 가지 약속.", "The four promises a receipt keeps."), ('관계형 창고만큼 엄격히 지키지 않을 수 있어요. → <a href="acid-ko.html">전표가 지키는 네 약속</a>', 'May not be kept as strictly as in the relational warehouse. → <a href="acid-en.html">the four promises a receipt keeps</a>')),
        ("인메모리 DB", "In-Memory DB", ("디스크 대신 바로 꺼내는 출고대.", "A desk that skips the deep shelf and serves straight from memory."), ('Key-Value형 NoSQL과 자주 함께 쓰여요. → <a href="inmemorydb-ko.html">특급 출고대</a>', 'Often paired with key-value NoSQL. → <a href="inmemorydb-en.html">the express pickup desk</a>')),
    ],
}
