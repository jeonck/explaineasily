from _draw import *
from _world import *

# 1. 전국 주문이 쏟아져 창고 하나로는 감당 못함
P1 = svg(300, sky(300)
         + bookshelf(300, 160, 1.0, n=4, hl=-1)
         + '<path d="M330 150 q40 -10 60 10" stroke="var(--bad)" stroke-width="2" fill="none"/>'
         + manuscript(200, 120, 0.5) + manuscript(230, 150, 0.5) + manuscript(470, 130, 0.5) + manuscript(500, 110, 0.5) + manuscript(530, 150, 0.5)
         + person(420, 170, s=0.8, face=SWEAT + EYES, **PRINTER)
         + label(380, 30, "⟦전국 독자 주문이 하루에도 수백만 건씩 쏟아져요|orders pour in from across the country, millions a day⟧", 13, "var(--ink)")
         + label(380, 278, "⟦창고 하나로는 주문 자료를 다 담지도, 다 찾지도 못해요|one warehouse can't hold all the order records, let alone find them⟧", 12, "var(--ink)"))

# 2. 한 창고에 넣으려니 넘치고 느려짐
P2 = svg(365, '<rect width="760" height="365" fill="var(--bad-soft)"/>'
         + bookshelf(320, 130, 1.3, n=4)
         + '<path d="M260 150 l-20 -14 M260 180 l-20 14 M500 150 l20 -14 M500 180 l20 14" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
         + person(420, 240, s=0.8, face=FROWN, **PRINTER)
         + label(380, 30, "⟦어제 쌓인 주문을 다 정리하기도 전에 새 주문이 또 쏟아져요|before yesterday's orders are even sorted, new ones pour in⟧", 13, "var(--ink)")
         + label(380, 348, "⟦창고 하나, 일꾼 한 명으로는 정리 속도가 주문 속도를 못 따라가요|with one warehouse and one worker, sorting can't keep pace with orders⟧", 12, "var(--ink)"))

# 3. 빅데이터 플랫폼 = 여러 창고에 나눠 담고 나눠서 정리 (hero)
P3 = svg(340, sky(340)
         + bookshelf(60, 180, 0.7, n=3) + bookshelf(280, 180, 0.7, n=3) + bookshelf(500, 180, 0.7, n=3)
         + person(100, 150, s=0.65, face=EYES, **PRINTER) + person(320, 150, s=0.65, face=EYES, **PROOFER) + person(540, 150, s=0.65, face=EYES, **EDITOR)
         + label(380, 30, "⟦빅데이터 플랫폼 = 자료를 여러 창고에 나눠 담고, 여럿이 동시에 나눠서 정리하는 구조|a big-data platform = data split across many warehouses, sorted by many workers at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 창고가 꽉 차도 다른 창고에 담으면 돼요|if one warehouse fills up, data goes to the others⟧", 12, "var(--muted)"))

# 4. 배치 vs 스트리밍, 데이터레이크 vs 데이터웨어하우스
P4 = svg(320, sky(320)
         + styleguide(60, 30, 300, 245, "⟦언제 정리하나|WHEN TO SORT⟧",
                      ("⟦배치 — 밤에 몰아서 정리|batch — sort it all overnight⟧",
                       "⟦스트리밍 — 들어오자마자 바로|streaming — sort it the instant it arrives⟧"), 1.0)
         + styleguide(400, 30, 300, 245, "⟦어떻게 쌓아두나|HOW TO STORE IT⟧",
                      ("⟦데이터레이크 — 원본 그대로 큰 창고|data lake — raw originals, one big warehouse⟧",
                       "⟦데이터웨어하우스 — 정리된 서가|data warehouse — tidied, organized shelves⟧"), 1.0)
         + label(380, 300, "⟦쓰임새에 맞춰 '언제 정리할지'와 '어떻게 쌓을지'를 따로 골라요|when to sort and how to store are chosen separately, to fit the use⟧", 12, "var(--ink)"))

# 5. 창고를 늘린다고 저절로 빨라지지 않음, 데이터 늪 위험
P5 = svg(390, '<rect width="380" height="390" fill="var(--accent-soft)"/><rect x="380" width="380" height="390" fill="var(--bad-soft)"/>'
         + bookshelf(140, 180, 0.9, n=3) + person(240, 260, s=0.6, face=FROWN, **PRINTER)
         + label(190, 344, "⟦창고만 늘리면 어느 창고에 뭐가 있는지 꼬여요|add warehouses with no plan, and no one knows what's where⟧", 11, "var(--ink)")
         + manuscript(540, 150, 0.6) + manuscript(580, 170, 0.6) + manuscript(620, 150, 0.6) + manuscript(560, 200, 0.6)
         + label(590, 260, "⟦정리 안 하고 쌓기만 한 자료는 못 찾는 '늪'이 돼요|data piled up untidied becomes a swamp no one can search⟧", 11, "var(--ink)")
         + label(380, 370, "⟦창고를 늘리는 것과, 창고를 잘 설계하는 건 다른 문제예요|adding warehouses and designing them well are two different problems⟧", 12, "var(--ink)", cls="d"))

SPLIT_I = icon('<rect x="8" y="24" width="14" height="24" rx="3" fill="var(--good)"/><rect x="25" y="24" width="14" height="24" rx="3" fill="var(--good)"/><rect x="42" y="24" width="14" height="24" rx="3" fill="var(--good)"/>')
PARALLEL_I = icon('<circle cx="16" cy="20" r="7" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="32" cy="20" r="7" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="48" cy="20" r="7" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><rect x="10" y="34" width="44" height="14" rx="3" fill="var(--good)"/>')
BATCH_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 v14 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
LAKE_I = icon('<ellipse cx="32" cy="40" rx="22" ry="10" fill="var(--sky)" stroke="var(--line)" stroke-width="2"/><path d="M14 40 q18 -20 36 0" stroke="var(--line)" stroke-width="2" fill="none"/>')

PAGE = {
    "slug": "bigdataplatform", "order": 26,
    "title": ("전국 창고 네트워크", "The Nationwide Warehouse Network"),
    "h1": ("<em>빅데이터 플랫폼</em>이 뭐예요?", "What is a <em>Big Data Platform</em>?"),
    "sub": ("빅데이터 플랫폼과 처리 아키텍처를, 전국 독자 주문을 감당하는 출판사 창고 네트워크 이야기로 풀어봤어요.",
            "Big data platforms and processing architecture, told as a story about a publishing house's nationwide warehouse network handling orders from everywhere."),
    "panels": [
        {"svg": P1, "alt": ("전국에서 쏟아지는 주문 원고를 단일 창고 하나로 감당 못해 인쇄 감독이 진땀을 흘림", "Orders pour in from everywhere and a single warehouse can't hold it — the print supervisor sweats"),
         "caption": ("전국 독자 주문이 하루에도 수백만 건씩 쏟아져요.", "Orders pour in from across the country, millions a day."),
         "small": ("창고 하나로는 주문 자료를 다 담지도, 다 찾지도 못해요.", "One warehouse can't hold all the order records, let alone find them.")},
        {"svg": P2, "alt": ("창고에서 원고가 넘쳐 떨어지고 인쇄 감독이 지쳐있음", "Manuscripts overflow the warehouse and the print supervisor is worn out"),
         "caption": ("주문 자료를 한 창고에 다 넣으려니 창고는 넘치고 정리는 느려져요.", "Cramming every order into one warehouse means it overflows and sorting slows down."),
         "small": ("창고 하나, 일꾼 한 명으로는 정리 속도가 주문 속도를 못 따라가요.", "With one warehouse and one worker, sorting can't keep pace with orders.")},
        {"svg": P3, "hero": True, "alt": ("세 개의 작은 창고에 세 사람이 나눠서 동시에 원고를 정리함", "Three smaller warehouses, each with its own worker, sorting manuscripts at the same time"),
         "caption": ("빅데이터 플랫폼은 자료를 여러 창고에 나눠 담고, 일꾼 여럿이 나눠서 정리해요.", "A big data platform stores data across many warehouses and sorts it with many workers."),
         "small": ("한 창고가 꽉 차도 다른 창고에 담으면 돼요.", "If one warehouse fills up, data goes to the others."),
         "tricks": (4, [
             (SPLIT_I, ("나눠 담기", "Distributed storage"), ("자료를 창고 하나에 다 넣지 않아요", "data isn't all stuffed into one warehouse"), "calm"),
             (PARALLEL_I, ("나눠서 정리", "Distributed processing"), ("일꾼 여럿이 동시에 정리해요", "many workers sorting at once")),
             (BATCH_I, ("밤에 몰아서(배치)", "Batch, overnight"), ("모아둔 자료를 한꺼번에 정리해요", "collected data gets sorted all together")),
             (LAKE_I, ("원본 그대로(데이터레이크)", "Raw storage (data lake)"), ("자료를 일단 그대로 쌓아둬요", "data is kept exactly as it came in"), "warm"),
         ])},
        {"svg": P4, "alt": ("언제 정리하나(배치/스트리밍)와 어떻게 쌓아두나(데이터레이크/웨어하우스)를 각각 정리한 표", "Two tables: when to sort (batch/streaming) and how to store (data lake/warehouse)"),
         "caption": ("쓰임새에 맞춰 '언제 정리할지'와 '어떻게 쌓을지'를 따로 골라요.", "When to sort and how to store are chosen separately, to fit the use."),
         "small": ("결과가 바로 필요하면 스트리밍, 좀 늦어도 되는 대량 정리면 배치를 골라요.", "Streaming when results are needed right away; batch for big jobs that can wait.")},
        {"svg": P5, "alt": ("왼쪽: 창고를 계획 없이 늘려 오히려 꼬임. 오른쪽: 정리 안 한 원고가 쌓여 늪처럼 됨", "Left: adding warehouses without a plan tangles things. Right: unsorted manuscripts pile into a swamp"),
         "caption": ("창고를 늘린다고 정리가 저절로 빨라지진 않아요.", "Adding more warehouses doesn't automatically make sorting faster."),
         "small": ("자료를 정리 안 하고 쌓아두기만 하면 나중엔 아무것도 못 찾는 '늪'이 돼요.", "Pile data up without tidying, and eventually nothing can be found — a swamp.")},
    ],
    "summary": (("<b>빅데이터 플랫폼</b>은 쏟아지는 자료를 <b>여러 창고(분산 저장)</b>에 나눠 담고, <b>여럿이 동시에(분산 처리)</b> 정리하는 구조예요.",
                 "A <b>big data platform</b> spreads incoming data across <b>many warehouses (distributed storage)</b> and sorts it with <b>many workers at once (distributed processing)</b>."),
                ("빅데이터 플랫폼은 대용량·고속·다양한 형태의 데이터를 분산 저장(HDFS 등)하고 분산 처리(Hadoop MapReduce, Spark 등)하는 구조예요. 처리 방식은 정해진 시간마다 모아 처리하는 배치 처리와, 들어오는 즉시 처리하는 스트리밍 처리로 나뉘고, 저장은 원본을 그대로 보관하는 데이터레이크와 정제된 데이터를 구조화해 보관하는 데이터웨어하우스를 함께 두는 구성이 흔해요.",
                 "A big data platform distributes storage (e.g. HDFS) and processing (e.g. Hadoop MapReduce, Spark) for high-volume, high-velocity, varied data. Processing splits into batch (collected and run on a schedule) and stream (handled the instant it arrives), and storage commonly pairs a data lake (raw data kept as-is) with a data warehouse (cleaned, structured data).")),
    "glossary": [
        ("빅데이터 플랫폼", "Big Data Platform", ("전국 창고 네트워크.", "The nationwide warehouse network."), ("자료를 여러 창고에 나눠 담고, 일꾼 여럿이 나눠서 정리해요.", "Spreads data across many warehouses and sorting across many workers.")),
        ("분산 저장", "Distributed Storage", ("창고를 여러 곳에 나누는 것.", "Splitting the warehouse into many sites."), ("한 창고가 꽉 차도 다른 창고에 담을 수 있어요.", "If one site fills up, the others still have room.")),
        ("분산 처리", "Distributed Processing", ("일꾼을 여럿 두고 동시에 정리.", "Many workers sorting at the same time."), ("Hadoop·Spark 같은 도구가 분산 처리를 해요.", "Tools like Hadoop and Spark do distributed processing.")),
        ("배치 처리", "Batch Processing", ("밤에 몰아서 정리하기.", "Sorting it all in one overnight run."), ("결과가 좀 늦어도 되는 대량 작업에 유리해요.", "Favored for large jobs whose results can wait.")),
        ("스트리밍 처리", "Stream Processing", ("들어오자마자 바로 정리하기.", "Sorting the instant it arrives."), ("결과가 바로 필요할 때 유리해요.", "Favored when results are needed right away.")),
        ("데이터레이크", "Data Lake", ("원본 그대로 쌓아두는 큰 창고.", "The big warehouse that keeps raw originals."), ("정리가 안 되면 '늪'이 될 수 있어요.", "Without upkeep, it can turn into a swamp.")),
        ("데이터웨어하우스", "Data Warehouse", ("정리된 서가.", "The tidied, organized shelf."), ("분석하기 좋게 구조화돼 있어요.", "Structured to be ready for analysis.")),
        ("고가용성", "High Availability", ("창고 하나가 무너져도 버티는 대비.", "Holding up even if one warehouse goes down."), ('이 세계 대신 놀이공원 세계에서 다뤄요. → <a href="failover-ko.html">예비 발전기가 넘겨받는 이야기</a>', 'Covered in the theme-park world, not this one. → <a href="failover-en.html">when the spare generator takes over</a>')),
    ],
}
