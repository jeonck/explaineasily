from _draw import *
from _world import *

# 1. 세계 소개 + 문제: 같은 주소가 전표마다 다 적혀 있어요
P1 = svg(320, sky(320)
         + label(380, 30, "⟦이 물류창고가 곧 데이터베이스 세계예요|this logistics warehouse IS the database world⟧", 13, "var(--muted)", cls="d")
         + person(140, 150, s=0.8, face=SWEAT + EYES, **SORTER)
         + receipt(300, 160, 0.8, void=False) + receipt(400, 180, 0.7, void=False) + receipt(500, 150, 0.8, void=False)
         + label(400, 250, "⟦고객 주소가 전표 세 장에 똑같이 적혀 있어요|the same customer address is written on three receipts⟧", 12, "var(--bad)")
         + label(400, 290, "⟦이사 가면 세 장을 다 고쳐야 해요|if they move, all three need fixing⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 하나만 고치면 서로 달라져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + receipt(240, 140, 0.8, text="⟦서울시|Seoul⟧")
         + receipt(380, 140, 0.8, text="⟦부산시|Busan⟧")
         + receipt(520, 140, 0.8, text="⟦서울시|Seoul⟧")
         + label(380, 220, "⟦한 장만 고쳤더니 전표마다 주소가 달라요|fixing only one receipt leaves them disagreeing⟧", 12, "var(--bad)")
         + label(380, 270, "⟦이게 '이상현상(anomaly)'이에요|this mismatch is called an anomaly⟧", 13, "var(--ink)"))

# 3. hero: 정규화 = 같은 정보는 한 칸에 딱 한 번만
NUM_I = icon('<rect x="8" y="8" width="48" height="48" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="40" text-anchor="middle" font-size="26" font-weight="700" fill="var(--good)">1</text>')
TAG_I = icon('<rect x="10" y="22" width="30" height="20" rx="3" fill="var(--accent)"/><circle cx="46" cy="32" r="8" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3"/>')
SPLIT_I = icon('<rect x="8" y="14" width="20" height="36" rx="3" fill="#E9B44C" stroke="#8B5E3C" stroke-width="2"/><rect x="36" y="14" width="20" height="36" rx="3" fill="#E9B44C" stroke="#8B5E3C" stroke-width="2"/>')
MERGE_I = icon('<rect x="8" y="22" width="20" height="20" rx="3" fill="#2E8B57"/><rect x="36" y="22" width="20" height="20" rx="3" fill="#2E8B57"/><path d="M28 32 h8" stroke="#FFF8E7" stroke-width="4"/>')

P3 = svg(340, sky(340)
         + person(380, 130, s=0.9, face=EYES, **SORTER)
         + box(260, 190, 0.8) + label(260, 230, "⟦주소 칸|address shelf⟧", 10, "var(--muted)")
         + receipt(460, 190, 0.6, text="⟦번호표→주소칸|tag→address shelf⟧") + receipt(540, 190, 0.6, text="⟦번호표→주소칸|tag→address shelf⟧")
         + label(380, 30, "⟦정규화 = 같은 정보는 선반 한 칸에 한 번만 적고, 전표는 번호표로 그 칸을 가리켜요|normalization = write shared info on one shelf once, and let receipts point to it by tag⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦그래서 이사를 가도 선반 한 칸만 고치면 끝이에요|so when they move, fixing one shelf is enough⟧", 12, "var(--muted)"))

# 4. 정규화 vs 반정규화 비교
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦정규화 vs 반정규화|normalization vs denormalization⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + label(220, 76, "⟦정규화|Normalize⟧", 12, "var(--good)", anchor="start", weight=800)
         + label(560, 76, "⟦반정규화|Denormalize⟧", 12, "var(--accent)", anchor="start", weight=800)
         + _row(110, "⟦중복 적지 않기|no duplicate writes⟧", "⟦자주 쓰는 건 합쳐두기|pre-join frequent reads⟧")
         + _row(146, "⟦고치기 쉬움|easy to update⟧", "⟦조회가 빠름|faster to read⟧")
         + _row(182, "⟦조인이 늘어남|more joins needed⟧", "⟦중복 위험 생김|risk of mismatch⟧")
         + box(640, 240, 0.6) + box(690, 240, 0.6, color="#C9822B")
         + label(665, 280, "⟦너무 잘게 나누면 다시 합쳐요|too fine-grained? merge it back⟧", 11, "var(--muted)"))

# 5. 한계: 반정규화하면 동시수정 문제가 생길 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + box(190, 150, 1.0) + label(190, 210, "⟦정규화 = 안전하지만 조인 많음|normalized: safe, more joins⟧", 11, "var(--ink)")
         + box(540, 150, 1.0, twin=True) + label(610, 210, "⟦반정규화 = 빠르지만 복제본이 어긋날 수 있음|denormalized: fast, copies can drift⟧", 11, "var(--ink)")
         + label(380, 270, "⟦그래서 동시에 손대는 규칙(병행제어)이 또 필요해요|that's why concurrency control is still needed⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "normalization", "order": 1,
    "title": ("한 칸에 한 번만 적는 규칙", "The Rule of Writing It Once"),
    "h1": ("<em>정규화/반정규화</em>가 뭐예요?", "What is <em>Normalization/Denormalization</em>?"),
    "sub": ("정규화와 반정규화를, 같은 정보를 선반 한 칸에만 적는 물류창고 이야기로 풀어봤어요.",
            "Normalization and denormalization, told as a story about writing shared info on just one warehouse shelf."),
    "panels": [
        {"svg": P1, "alt": ("분류 담당이 전표 세 장에 같은 주소가 적힌 것을 보고 진땀을 흘림", "A sorter sweats seeing the same address written on three receipts"),
         "caption": ("고객 주소가 전표 세 장에 똑같이 적혀 있어요.", "The same customer address is written on three receipts."),
         "small": ("이사 가면 세 장을 다 고쳐야 해요.", "If they move, all three need fixing.")},
        {"svg": P2, "alt": ("전표 세 장 중 하나만 고쳐서 주소가 서로 달라짐", "Only one of three receipts was fixed, so the addresses now disagree"),
         "caption": ("한 장만 고쳤더니 전표마다 주소가 달라요.", "Fixing only one receipt leaves them disagreeing."),
         "small": ("이게 '이상현상(anomaly)'이에요.", "This mismatch is called an anomaly.")},
        {"svg": P3, "hero": True, "alt": ("분류 담당이 주소를 선반 한 칸에만 두고 전표는 번호표로 그 칸을 가리킴", "The sorter keeps the address on one shelf, with receipts pointing to it by tag"),
         "caption": ("정규화 = 같은 정보는 선반 한 칸에 한 번만 적어요.", "Normalization = write shared info on one shelf once."),
         "small": ("그래서 이사를 가도 선반 한 칸만 고치면 끝이에요.", "So when they move, fixing one shelf is enough."),
         "tricks": (4, [
             (NUM_I, ("한 칸에 값 하나만", "One value per shelf slot"), ("중복을 없애요", "removing duplicates"), "calm"),
             (TAG_I, ("번호표로 연결하기", "Link by tag"), ("전표가 선반을 가리켜요", "the receipt points to the shelf")),
             (SPLIT_I, ("더 잘게 나누기", "Split further"), ("고치기 쉬워져요", "easier to update"), "warm"),
             (MERGE_I, ("자주 쓰면 다시 합치기", "Merge back if frequent"), ("조회가 빨라져요(반정규화)", "faster reads — denormalization")),
         ])},
        {"svg": P4, "alt": ("정규화와 반정규화를 비교하는 표", "A table comparing normalization and denormalization"),
         "caption": ("정규화는 고치기 쉽고, 반정규화는 조회가 빨라요.", "Normalization is easy to update; denormalization is fast to read."),
         "small": ("너무 잘게 나누면 다시 합쳐요.", "Too fine-grained? Merge it back.")},
        {"svg": P5, "alt": ("왼쪽: 정규화는 안전하지만 조인이 많음. 오른쪽: 반정규화는 빠르지만 복제본이 어긋날 수 있음", "Left: normalized is safe but needs more joins. Right: denormalized is fast but copies can drift"),
         "caption": ("반정규화는 조회는 빠르지만 복제본이 어긋날 수 있어요.", "Denormalization is fast but copies can drift apart."),
         "small": ("그래서 동시에 손대는 규칙(병행제어)이 또 필요해요.", "That's why concurrency control is still needed.")},
    ],
    "summary": (("<b>정규화</b> = 같은 정보를 <b>한 곳에만 적고 번호표로 연결</b>해서 중복과 이상현상을 없애는 규칙, <b>반정규화</b>는 자주 같이 보는 정보를 일부러 다시 합쳐 조회를 빠르게 하는 것.",
                 "<b>Normalization</b> writes shared data in one place and links to it by key, removing duplication and anomalies. <b>Denormalization</b> deliberately re-merges frequently-read data for speed."),
                ("정규화는 함수 종속성을 분석해 1NF·2NF·3NF·BCNF 등 단계적으로 테이블을 분해해 삽입/갱신/삭제 이상현상을 제거하는 기법이고, 반정규화는 조회 성능을 위해 정규화된 테이블을 의도적으로 다시 통합하는 것이에요. 실무에서는 둘을 함께 써요.",
                 "Normalization decomposes tables stepwise (1NF/2NF/3NF/BCNF) based on functional dependency analysis to remove insertion/update/deletion anomalies. Denormalization intentionally re-merges normalized tables for read performance. Real systems use both together.")),
    "glossary": [
        ("정규화", "Normalization", ("선반을 쪼개 중복을 없애는 것.", "Splitting shelves to remove duplication."), ("1NF→2NF→3NF 순서로 깊어져요.", "Goes deeper from 1NF to 2NF to 3NF.")),
        ("반정규화", "Denormalization", ("자주 보는 선반을 다시 합치는 것.", "Re-merging frequently-viewed shelves."), ("조회는 빠르지만 중복이 생겨요.", "Faster reads, but duplication returns.")),
        ("이상현상(Anomaly)", "Anomaly", ("전표마다 주소가 달라지는 사고.", "Receipts ending up with different addresses."), ("삽입·갱신·삭제 세 종류가 있어요.", "Comes in insertion, update, and deletion kinds.")),
        ("함수적 종속성", "Functional Dependency", ("번호표 하나가 선반 한 칸을 정하는 규칙.", "The rule that one tag fixes one shelf slot."), ("정규화 단계를 가르는 기준이에요.", "The yardstick for each normal form.")),
        ("NoSQL 모델링", "NoSQL Modeling", ("선반 모양을 자유롭게 바꾸는 창고.", "A warehouse that freely changes shelf shape."), ('정규화 대신 다른 방식을 써요. → <a href="nosqltype-ko.html">자유로운 선반 창고</a>', 'Uses a different approach than normalization. → <a href="nosqltype-en.html">the free-shelf warehouse</a>')),
        ("병행제어", "Concurrency Control", ("동시에 전표를 쓸 때 부딪히지 않게 막는 규칙.", "Rules that stop simultaneous receipt edits from colliding."), ('반정규화된 복제본을 지킬 때 필요해요. → <a href="concurrency-ko.html">동시에 안 부딪히는 규칙</a>', 'Needed to protect denormalized copies. → <a href="concurrency-en.html">the no-collision rule</a>')),
        ("트랜잭션", "Transaction", ("전표 한 장의 작업 단위.", "One receipt's unit of work."), ('ACID 네 가지 약속을 지켜요. → <a href="acid-ko.html">전표가 지키는 네 약속</a>', 'Keeps four ACID promises. → <a href="acid-en.html">the four promises a receipt keeps</a>')),
        ("샤딩/파티셔닝", "Sharding/Partitioning", ("창고를 구역으로 쪼개는 것.", "Splitting the warehouse into zones."), ('정규화와는 다른 축의 \'나누기\'예요. → <a href="dbsharding-ko.html">구역으로 쪼갠 창고</a>', 'A different kind of splitting. → <a href="dbsharding-en.html">the warehouse split into zones</a>')),
    ],
}
