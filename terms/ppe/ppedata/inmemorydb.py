from _draw import *
from _world import *

# 1. 문제: 깊은 선반까지 갔다 오느라 배송이 늦어요
P1 = svg(320, sky(320)
         + person(170, 160, s=0.8, face=SWEAT + EYES, **PACKER)
         + shelfzone(320, 150, 340, 90, 0.9, n=4)
         + person(690, 190, s=0.7, face=FROWN, **DRIVER)
         + label(490, 120, "⟦포장 담당이 안쪽 깊은 선반까지 다녀와야 해요|the packer has to walk all the way to the deep shelf⟧", 12, "var(--bad)")
         + label(380, 290, "⟦그동안 배송 기사는 계속 기다려요|the driver keeps waiting the whole time⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 자주 찾는 물건도 매번 깊이 들어가요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + box(260, 150, 0.9, color="#E9B44C")
         + box(500, 150, 0.9, color="#E9B44C")
         + label(380, 90, "⟦같은 인기 상품인데 매번 깊은 선반까지 가요|the same popular item, yet it's fetched from deep storage every time⟧", 12, "var(--bad)")
         + label(380, 250, "⟦자주 찾는 상품은 가까이 둘 수 없을까요?|couldn't frequently-needed items stay close by?⟧", 13, "var(--ink)"))

# 3. hero: 인메모리 DB = 깊은 선반 대신 바로 꺼내는 특급 출고대
MEM_I = icon('<rect x="8" y="24" width="48" height="18" rx="4" fill="var(--accent)"/><path d="M18 24 l6 -10 l6 10 M38 24 l6 -10 l6 10" stroke="#FFF8E7" stroke-width="3" fill="none"/>')
FAST_I = icon('<path d="M10 32 h30 M34 24 l10 8 l-10 8" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
VOLATILE_I = icon('<path d="M32 10 L44 34 H20 Z" fill="var(--bad)"/><rect x="29" y="38" width="6" height="14" fill="var(--bad)"/>')
GRID_I = icon('<rect x="8" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="8" y="38" width="18" height="18" rx="3" fill="var(--accent)" opacity="0.6"/><rect x="34" y="38" width="18" height="18" rx="3" fill="var(--accent)" opacity="0.6"/>')

P3 = svg(340, sky(340)
         + person(230, 130, s=0.9, face=SMILE, **PACKER)
         + fastdesk(230, 280, 1.1)
         + person(560, 170, s=0.7, face=SMILE, **DRIVER)
         + label(380, 30, "⟦인메모리 DB = 깊은 선반 대신 바로 꺼내는 특급 출고대|in-memory DB = an express desk that skips the deep shelf⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦데이터를 메모리에 올려두니 디스크보다 훨씬 빨리 꺼내요|data is kept in memory, so pickup is far faster than from disk⟧", 12, "var(--muted)"))

# 4. 쓰임새 비교
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦인메모리 DB / IMDG 쓰임새|how in-memory DB / IMDG gets used⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + _row(80, "⟦캐시로 — 깊은 선반 조회를 줄임|as a cache — cuts deep-shelf lookups⟧", "⟦예: Redis|e.g. Redis⟧")
         + _row(116, "⟦세션/순위판처럼 빠른 조회|fast lookups like sessions, leaderboards⟧", "⟦디스크보다 훨씬 빠름|far faster than disk⟧")
         + _row(152, "⟦IMDG — 여러 대의 메모리를 묶음|IMDG — pools memory across many machines⟧", "⟦샤딩으로 규모를 키움|grows by sharding⟧")
         + _row(188, "⟦휘발성 — 전원이 나가면 데이터 사라짐|volatile — data vanishes if power is lost⟧", "⟦로그/스냅샷으로 보완|backed up via log/snapshot⟧"))

# 5. 한계: 메모리는 비싸고 다 담을 수는 없어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + fastdesk(190, 150, 1.0) + label(190, 210, "⟦자주 찾는 데이터는 바로 꺼내요|frequently-needed data pops out instantly⟧", 11, "var(--ink)")
         + shelfzone(480, 140, 180, 70, 0.8, n=3) + label(570, 240, "⟦나머지 데이터는 여전히 깊은 선반(디스크)에 있어요|the rest of the data stays on the deep shelf (disk)⟧", 11, "var(--ink)")
         + label(380, 270, "⟦메모리는 디스크보다 비싸서 데이터를 전부 올리긴 어려워요|memory costs more than disk, so moving all the data into memory is hard⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "inmemorydb", "order": 8,
    "title": ("깊은 선반 대신 바로 꺼내는 특급 출고대", "The Express Desk That Skips the Deep Shelf"),
    "h1": ("<em>인메모리 컴퓨팅(In-Memory DB/IMDG)</em>이 뭐예요?", "What is <em>In-Memory Computing (In-Memory DB/IMDG)</em>?"),
    "sub": ("인메모리 DB와 IMDG를, 깊은 선반까지 안 가고 바로 꺼내는 특급 출고대 이야기로 풀어봤어요.",
            "In-memory DB and IMDG, told as a story about an express desk that skips the trip to the deep shelf."),
    "panels": [
        {"svg": P1, "alt": ("포장 담당이 깊은 선반까지 다녀오는 동안 배송 기사가 찡그리며 기다림", "A packer treks to the deep shelf while a driver frowns, waiting"),
         "caption": ("포장 담당이 안쪽 깊은 선반까지 다녀와야 해요.", "The packer has to walk all the way to the deep shelf."),
         "small": ("그동안 배송 기사는 계속 기다려요.", "The driver keeps waiting the whole time.")},
        {"svg": P2, "alt": ("같은 인기 상자 두 개가 매번 깊은 선반에서 꺼내짐", "The same popular box, fetched from deep storage both times"),
         "caption": ("같은 인기 상품인데 매번 깊은 선반까지 가요.", "The same popular item, fetched from deep storage every time."),
         "small": ("자주 찾는 상품은 가까이 둘 수 없을까요?", "Couldn't frequently-needed items stay close by?")},
        {"svg": P3, "hero": True, "alt": ("포장 담당이 특급 출고대에서 바로 꺼내주고 배송 기사가 웃으며 금방 받아감", "A packer hands it over instantly from the express desk, and the driver smiles, getting it right away"),
         "caption": ("인메모리 DB = 깊은 선반 대신 바로 꺼내는 특급 출고대예요.", "An in-memory DB is an express desk that skips the deep shelf."),
         "small": ("데이터를 메모리에 올려두니 디스크보다 훨씬 빨리 꺼내요.", "Data is kept in memory, so pickup is far faster than from disk."),
         "tricks": (4, [
             (MEM_I, ("데이터를 메모리에 바로 두기", "Keep data right in memory"), ("디스크까지 안 가요", "skips the trip to disk"), "calm"),
             (FAST_I, ("빠른 꺼내기", "Instant pickup"), ("디스크보다 지연이 훨씬 짧아요", "far lower latency than disk")),
             (VOLATILE_I, ("휘발성 위험", "Volatility risk"), ("전원이 나가면 메모리의 데이터가 사라져요", "data in memory vanishes if power is lost"), "warm"),
             (GRID_I, ("IMDG — 여러 대 묶기", "IMDG — pool many machines"), ("여러 대의 메모리를 모아 큰 저장소로 써요", "pools memory into one big store")),
         ])},
        {"svg": P4, "alt": ("캐시, 빠른 조회, IMDG, 휘발성 네 가지 쓰임새를 비교하는 표", "A table comparing cache use, fast lookups, IMDG, and volatility"),
         "caption": ("인메모리 DB/IMDG는 캐시, 빠른 조회, 메모리 묶기에 쓰여요.", "In-memory DB/IMDG is used for caching, fast lookups, and pooling memory."),
         "small": ("전원이 나가도 데이터를 되살리도록 로그나 스냅샷을 남겨요.", "Logs or snapshots are kept so data can be restored after a power loss.")},
        {"svg": P5, "alt": ("왼쪽: 특급 출고대에서 자주 찾는 것이 바로 나옴. 오른쪽: 나머지는 여전히 깊은 선반에 있음", "Left: frequent items pop out of the express desk instantly. Right: the rest still sits on the deep shelf"),
         "caption": ("메모리는 디스크보다 비싸서 데이터를 전부 올리긴 어려워요.", "Memory costs more than disk, so moving all the data into memory is hard."),
         "small": ("그래서 자주 쓰는 데이터만 골라 올리기도 해요(캐시).", "So often only frequently-used data gets loaded into memory — that's a cache.")},
    ],
    "summary": (("<b>인메모리 DB/IMDG</b> = 깊은 선반(디스크)까지 가지 않고, <b>메모리에 바로 올려 둬서</b> 디스크보다 훨씬 빨리 꺼내 쓰는 방식.",
                 "<b>In-memory DB/IMDG</b> keeps data right in memory instead of making the trip to the deep shelf (disk), so it can be fetched far faster than from disk."),
                ("인메모리 DB는 디스크가 아닌 주기억장치(RAM)에 데이터를 상주시켜 디스크 I/O 지연을 크게 줄이는 데이터베이스이고, IMDG(In-Memory Data Grid)는 여러 노드의 메모리를 묶어 분산된 대용량 인메모리 저장소로 쓰는 것이에요. 휘발성이 약점이라 로그 선행기록(WAL)·스냅샷·복제로 내구성을 보완해요.",
                 "An in-memory DB keeps data resident in RAM instead of disk, greatly cutting disk I/O latency. An IMDG (In-Memory Data Grid) pools memory across multiple nodes into a large distributed in-memory store. Volatility is its weak point, so write-ahead logging, snapshots, and replication back up its durability.")),
    "glossary": [
        ("인메모리 DB", "In-Memory Database", ("메모리에 바로 데이터를 두는 창고.", "A warehouse that keeps data right in memory."), ("데이터를 읽을 때 디스크 I/O 지연이 거의 없어요.", "Almost no disk I/O latency on reads.")),
        ("IMDG", "In-Memory Data Grid", ("여러 대의 메모리를 묶은 창고.", "A warehouse pooling memory across many machines."), ('샤딩과 함께 규모를 키워요. → <a href="dbsharding-ko.html">구역으로 쪼갠 창고</a>', 'Scales together with sharding. → <a href="dbsharding-en.html">the warehouse split into zones</a>')),
        ("캐시", "Cache", ("자주 찾는 것만 가까이 두는 것.", "Keeping only the frequently-needed items close by."), ("전체 데이터가 아니라 일부만 메모리에 올려요.", "Holds only a portion of the data in memory.")),
        ("휘발성", "Volatility", ("전원이 나가면 사라지는 성질.", "The trait of vanishing when power is lost."), ("사라진 데이터는 로그/스냅샷으로 복구해요.", "Lost data is recovered via log or snapshot.")),
        ("지속성(Durability)", "Durability", ("도장 찍히면 사라지지 않는 약속.", "The promise that once stamped, it stays."), ('일부 인메모리 DB는 속도를 위해 이 약속을 타협해요. → <a href="acid-ko.html">전표가 지키는 네 약속</a>', 'Some in-memory DBs trade off this promise for speed. → <a href="acid-en.html">the four promises a receipt keeps</a>')),
        ("NoSQL 모델링", "NoSQL Modeling", ("상자 모양에 맞춰 선반을 바꾸는 창고.", "A warehouse reshaping shelves to fit the box."), ('Redis처럼 Key-Value형이면서 인메모리인 제품도 있어요. → <a href="nosqltype-ko.html">자유로운 선반 창고</a>', 'Some products, like Redis, are both key-value and in-memory. → <a href="nosqltype-en.html">the free-shelf warehouse</a>')),
        ("캐싱(놀이공원 세계)", "Caching (Amusement-Park World)", ("놀이공원 세계에서 다루는 캐시 이야기.", "The caching story from the amusement-park world."), ('분산 시스템 관점의 캐싱은 그쪽에서 더 다뤄요. → <a href="caching-ko.html">캐싱</a>', 'The distributed-systems view of caching is covered there. → <a href="caching-en.html">caching</a>')),
        ("병행제어", "Concurrency Control", ("동시에 손대도 안 부딪히게 막는 규칙.", "Rules that stop simultaneous edits from colliding."), ('메모리 위에서도 이 규칙은 그대로 필요해요. → <a href="concurrency-ko.html">동시에 안 부딪히는 규칙</a>', 'Still needed even when everything lives in memory. → <a href="concurrency-en.html">the no-collision rule</a>')),
    ],
}
