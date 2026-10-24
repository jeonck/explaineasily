from _draw import *
from _world import *

# 1. 문제: 창고 하나에 상자가 너무 많아졌어요
P1 = svg(320, sky(320)
         + person(140, 160, s=0.8, face=SWEAT + EYES, **MANAGER)
         + shelfzone(260, 140, 440, 110, 1.0, n=6)
         + label(480, 110, "⟦상자가 너무 많아서 찾는 데 한참 걸려요|so many boxes that finding one takes forever⟧", 12, "var(--bad)")
         + label(380, 290, "⟦창고 하나로는 감당이 안 돼요|one single warehouse can't keep up⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 어디로 나눌지가 문제예요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shelfzone(190, 120, 380, 100, 0.9, n=4, bad=2)
         + person(640, 180, s=0.75, face=FROWN, **MANAGER)
         + label(380, 90, "⟦아무렇게나 나누면 한 구역에만 몰려요|splitting randomly piles everything into one zone⟧", 12, "var(--bad)")
         + label(380, 260, "⟦나누는 기준(키)을 잘 골라야 해요|the splitting key has to be chosen carefully⟧", 13, "var(--ink)"))

# 3. hero: 샤딩 = 창고를 여러 구역(서버)으로 쪼개는 것
HKEY_I = icon('<rect x="8" y="26" width="48" height="14" rx="3" fill="var(--accent)"/><circle cx="16" cy="33" r="5" fill="#FFF8E7"/>')
VSPLIT_I = icon('<rect x="8" y="8" width="20" height="48" rx="3" fill="#5B8DEF"/><rect x="36" y="8" width="20" height="48" rx="3" fill="#2E8B57"/>')
ROUTE_I = icon('<circle cx="14" cy="32" r="8" fill="var(--accent)"/><path d="M22 32 h30" stroke="#8B5E3C" stroke-width="3"/><circle cx="54" cy="32" r="6" fill="#E9B44C"/>')
JOIN_I = icon('<rect x="8" y="22" width="20" height="20" rx="3" fill="#E9B44C"/><rect x="36" y="22" width="20" height="20" rx="3" fill="#E9B44C"/><path d="M28 32 h8" stroke="var(--bad)" stroke-width="4"/>')

P3 = svg(340, sky(340)
         + person(130, 130, s=0.85, face=EYES, **MANAGER)
         + shelfzone(230, 110, 180, 90, 0.8, n=2, label_text="⟦구역 A|zone A⟧")
         + shelfzone(430, 110, 180, 90, 0.8, n=2, label_text="⟦구역 B|zone B⟧")
         + person(680, 200, s=0.7, face=EYES, **DRIVER)
         + label(380, 30, "⟦샤딩 = 창고를 여러 구역(서버)으로 쪼개는 것|sharding = splitting the warehouse into several zones (servers)⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦각 구역은 자기 몫의 상자만 책임져요|each zone only handles its own share of boxes⟧", 12, "var(--muted)"))

# 4. 샤딩 vs 파티셔닝
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦샤딩 vs 파티셔닝|sharding vs partitioning⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + label(220, 76, "⟦샤딩|Sharding⟧", 12, "var(--good)", anchor="start", weight=800)
         + label(560, 76, "⟦파티셔닝|Partitioning⟧", 12, "var(--accent)", anchor="start", weight=800)
         + _row(110, "⟦서로 다른 창고(서버)로 나눔|splits across different warehouses⟧", "⟦한 창고 안에서 구역만 나눔|splits zones inside one warehouse⟧")
         + _row(146, "⟦수평 분할(행 기준)|horizontal split, by row⟧", "⟦수평/수직 모두 가능|horizontal or vertical⟧")
         + _row(182, "⟦샤딩 키 선택이 핵심|shard key choice is critical⟧", "⟦조회 패턴에 맞춰 구획|zones fit the query pattern⟧"))

# 5. 한계: 여러 구역을 한 번에 봐야 하는 질문은 느려져요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + shelfzone(100, 130, 180, 80, 0.8, n=2, label_text="⟦구역 A|zone A⟧")
         + shelfzone(320, 130, 180, 80, 0.8, n=2, label_text="⟦구역 B|zone B⟧")
         + person(620, 150, s=0.8, face=FROWN, **DRIVER)
         + bubble(534, 58, 220, 40, "⟦두 구역을 다 뒤져야 해요(조인)|has to search both zones — a join⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦나눌수록 빨라지지만, 걸친 질문은 오히려 느려져요|splitting helps speed, but cross-zone questions get slower⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "dbsharding", "order": 3,
    "title": ("너무 커진 창고를 구역으로 쪼개기", "Splitting an Overgrown Warehouse into Zones"),
    "h1": ("<em>데이터베이스 샤딩·파티셔닝</em>이 뭐예요?", "What is <em>Database Sharding & Partitioning</em>?"),
    "sub": ("샤딩과 파티셔닝을, 너무 커진 창고를 구역으로 쪼개는 이야기로 풀어봤어요.",
            "Database sharding and partitioning, told as a story about splitting an overgrown warehouse into zones."),
    "panels": [
        {"svg": P1, "alt": ("창고 관리자가 상자로 가득 찬 거대한 선반 앞에서 진땀을 흘림", "A manager sweats before a huge shelf packed with boxes"),
         "caption": ("상자가 너무 많아서 찾는 데 한참 걸려요.", "So many boxes that finding one takes forever."),
         "small": ("창고 하나로는 감당이 안 돼요.", "One single warehouse can't keep up.")},
        {"svg": P2, "alt": ("창고 관리자가 아무렇게나 나눈 선반 한 구역에 상자가 몰린 것을 보고 찡그림", "A manager frowns at a randomly split shelf where boxes pile into one zone"),
         "caption": ("아무렇게나 나누면 한 구역에만 몰려요.", "Splitting randomly piles everything into one zone."),
         "small": ("나누는 기준(키)을 잘 골라야 해요.", "The splitting key has to be chosen carefully.")},
        {"svg": P3, "hero": True, "alt": ("창고 관리자가 창고를 구역 A와 구역 B로 나누고, 배송 기사가 자기 몫의 구역을 찾아감", "A manager splits the warehouse into zone A and zone B, and a driver heads to the right zone"),
         "caption": ("샤딩 = 창고를 여러 구역(서버)으로 쪼개는 것이에요.", "Sharding splits the warehouse into several zones (servers)."),
         "small": ("각 구역은 자기 몫의 상자만 책임져요.", "Each zone only handles its own share of boxes."),
         "tricks": (4, [
             (HKEY_I, ("샤딩 키 고르기", "Choose a shard key"), ("어느 구역으로 갈지 정해요", "decides which zone it goes to"), "calm"),
             (VSPLIT_I, ("수직/수평 나누기", "Split vertically or horizontally"), ("열 기준, 행 기준", "by column, or by row")),
             (ROUTE_I, ("올바른 구역으로 안내", "Route to the right zone"), ("배송 기사가 헤매지 않아요", "the driver doesn't wander"), "warm"),
             (JOIN_I, ("걸친 질문은 느려짐", "Cross-zone queries slow down"), ("여러 구역을 다 봐야 해요", "has to check every zone")),
         ])},
        {"svg": P4, "alt": ("샤딩과 파티셔닝을 비교하는 표", "A table comparing sharding and partitioning"),
         "caption": ("샤딩은 서버를 나누고, 파티셔닝은 한 창고 안 구역을 나눠요.", "Sharding splits servers; partitioning splits zones within one warehouse."),
         "small": ("둘 다 나누는 기준이 핵심이에요.", "Both hinge on choosing the right split key.")},
        {"svg": P5, "alt": ("배송 기사가 두 구역을 다 뒤져야 해서 찡그림", "A driver frowns because the request has to search both zones"),
         "caption": ("나눌수록 빨라지지만, 걸친 질문은 느려져요.", "Splitting helps speed, but cross-zone questions get slower."),
         "small": ("조인이 필요한 질문일수록 더 그래요.", "Especially true for queries that need a join.")},
    ],
    "summary": (("<b>샤딩/파티셔닝</b> = 너무 커진 창고를 <b>여러 구역(또는 서버)</b>으로 나눠, 각자 자기 몫만 책임지게 하는 것.",
                 "<b>Sharding/partitioning</b> splits an overgrown warehouse into zones (or servers), each responsible for its own share."),
                ("샤딩은 데이터를 여러 물리 서버(샤드)로 수평 분할해 확장성을 얻는 기법이고, 파티셔닝은 한 서버/DB 안에서 테이블을 수평 또는 수직으로 나누는 것이에요. 둘 다 조인·트랜잭션 범위가 샤드/파티션을 넘어가면 성능과 일관성 비용이 커져요.",
                 "Sharding horizontally splits data across multiple physical servers (shards) for scalability. Partitioning splits a table horizontally or vertically within one server/DB. Both pay a cost in performance and consistency when a join or transaction spans more than one shard or partition.")),
    "glossary": [
        ("샤딩", "Sharding", ("여러 서버(창고)로 나누는 것.", "Splitting across several servers (warehouses)."), ("샤딩 키 선택이 가장 중요해요.", "Choosing the shard key matters most.")),
        ("파티셔닝", "Partitioning", ("한 창고 안에서 구역만 나누는 것.", "Splitting zones within one warehouse."), ("수평/수직 두 방향 모두 가능해요.", "Can go horizontal or vertical.")),
        ("샤딩 키", "Shard Key", ("어느 구역으로 보낼지 정하는 번호표.", "The tag deciding which zone it goes to."), ("잘못 고르면 한쪽만 몰려요.", "Pick it wrong and one zone gets overloaded.")),
        ("조인 비용", "Join Cost", ("여러 구역을 다 뒤지는 수고.", "The work of searching every zone."), ("샤딩이 깊어질수록 커져요.", "Grows as sharding gets more fine-grained.")),
        ("분산 시스템 관점의 샤딩", "Sharding (Distributed Systems View)", ("놀이공원 세계의 더 깊은 이야기.", "The deeper story from the amusement-park world."), ('복제·합의·CAP까지 다루는 쪽은 따로 있어요. → <a href="sharding-ko.html">분산 시스템의 샤딩</a>', 'Replication, consensus, and CAP are covered there in depth. → <a href="sharding-en.html">sharding in distributed systems</a>')),
        ("병행제어", "Concurrency Control", ("동시에 손대도 안 부딪히게 막는 규칙.", "Rules that stop simultaneous edits from colliding."), ('구역이 나뉘어도 안에서는 이 규칙이 필요해요. → <a href="concurrency-ko.html">동시에 안 부딪히는 규칙</a>', "Still needed inside each zone. → <a href=\"concurrency-en.html\">the no-collision rule</a>")),
        ("NoSQL 모델링", "NoSQL Modeling", ("자유로운 선반 창고.", "The free-shelf warehouse."), ('샤딩을 수월하게 지원하는 경우가 많아요. → <a href="nosqltype-ko.html">자유로운 선반 창고</a>', 'Often makes sharding easier. → <a href="nosqltype-en.html">the free-shelf warehouse</a>')),
        ("정규화", "Normalization", ("선반 한 칸에 한 번만 적는 규칙.", "Writing shared info on one shelf once."), ('정규화를 너무 따르면 조인이 늘어 샤딩과 부딪혀요. → <a href="normalization-ko.html">한 칸에 한 번만 적는 규칙</a>', 'Too much normalization means more joins, clashing with sharding. → <a href="normalization-en.html">the rule of writing it once</a>')),
    ],
}
