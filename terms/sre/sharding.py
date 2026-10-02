from _draw import *
from _world import *

# 1. 창구 하나에 손님 명부 전체가 있어요
P1 = svg(300, sky(300)
         + booth(380, 230, 1.3, label_text="⟦매표 창구|TICKET BOOTH⟧")
         + queueline(90, 174, 6, 0.5, 30)
         + board(500, 40, 220, 120, "⟦손님 명부|GUEST LOG⟧", ("⟦김··· 박··· 이···|Kim... Park... Lee...⟧", "⟦백만 명 전부 여기|all 1,000,000 names here⟧"), 1.0)
         + label(380, 282, "⟦창구 하나에 손님 명부 전체가 있어요|one booth holds the whole guest log⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 손님이 백만 명이면 이름 찾기가 느려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(190, 230, 1.1)
         + person(150, 174, s=0.6, face=SWEAT, **OPERATOR)
         + bubble(260, 90, 230, 50, "⟦백만 명 중에 그 이름을 찾는 중...|searching one name among a million...⟧", 12, "var(--panel)", "var(--line)", "left")
         + queueline(520, 174, 5, 0.5, 30)
         + label(540, 250, "⟦줄이 점점 길어져요|the line keeps growing⟧", 11, "var(--bad)")
         + label(380, 282, "⟦손님이 백만 명이면 한 장부에서 이름 찾기가 느려요|with a million guests, searching one ledger is slow⟧", 12, "var(--ink)"))

# 3. hero: 이름 앞글자(또는 번호)별로 창구를 나누면 더 빨라요
P3 = svg(340, sky(340)
         + booth(110, 260, 0.9, label_text="⟦1-250|1-250⟧") + booth(270, 260, 0.9, label_text="⟦251-500|251-500⟧")
         + booth(430, 260, 0.9, label_text="⟦501-750|501-750⟧") + booth(590, 260, 0.9, label_text="⟦751-1000|751-1000⟧")
         + queueline(70, 165, 2, 0.45, 26) + queueline(230, 165, 2, 0.45, 26) + queueline(390, 165, 2, 0.45, 26) + queueline(550, 165, 2, 0.45, 26)
         + label(380, 40, "⟦번호별로 창구를 나누면, 각 창구는 적은 명부만 봐요|split booths by number, and each one scans a small slice⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦창구가 네 개면, 찾는 시간도 4분의 1이 돼요|four booths means roughly a quarter of the searching⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 안내판이 어느 창구인지 알려줘요
P4 = svg(320, sky(320)
         + board(280, 30, 200, 90, "⟦안내판|SIGN⟧", ("⟦번호 601 → 4번 창구|No. 601 → booth 4⟧",), 1.0)
         + person(330, 174, s=0.6, face=EYES, shirt="#7B3FA0")
         + '<path d="M370 120 L560 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + booth(590, 260, 0.9, label_text="⟦4번|No.4⟧")
         + label(380, 290, "⟦나누는 기준(번호·이름)과 안내판이 한 세트예요|a split rule (number, name) and a sign always go together⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 한쪽에 몰리면 핫스팟, 전체를 묻는 질문엔 느려요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + booth(190, 250, 1.0, label_text="⟦1번|No.1⟧") + queueline(20, 207, 7, 0.38, 16)
         + label(190, 300, "⟦번호를 잘못 나누면 한 곳에만 몰려요|split the numbers badly and everyone piles into one booth⟧", 11, "var(--ink)")
         + booth(590, 250, 0.9) + label(590, 210, "⟦전체 손님 수는?|how many guests in total?⟧", 11, "var(--bad)", cls="d")
         + bubble(500, 120, 180, 50, "⟦창구 네 곳을 다 더해야 해요...|have to add up all four booths...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(590, 300, "⟦창구를 가로질러 묻는 질문엔 느려요|questions that cross every booth are slow⟧", 11, "var(--ink)"))

HASH_I = icon('<rect x="8" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="30" y="14" width="18" height="18" rx="3" fill="#5B8DEF"/><rect x="8" y="36" width="18" height="18" rx="3" fill="#2E7D6B"/><rect x="30" y="36" width="18" height="18" rx="3" fill="#E9B44C"/>')
SLICE_I = icon('<rect x="8" y="20" width="12" height="28" fill="var(--good)"/><rect x="22" y="20" width="12" height="28" fill="var(--good)"/><rect x="36" y="20" width="12" height="28" fill="var(--good)"/><rect x="50" y="20" width="12" height="28" fill="var(--good)"/><path d="M8 16 h54" stroke="var(--ink)" stroke-width="3" fill="none"/>')
REBAL_I = icon('<path d="M20 44 L44 20" stroke="var(--accent)" stroke-width="5" stroke-linecap="round" fill="none"/><path d="M38 20 h8 v8" stroke="var(--accent)" stroke-width="5" fill="none"/><circle cx="18" cy="46" r="6" fill="var(--bad)"/><circle cx="46" cy="18" r="6" fill="var(--good)"/>')
SIGN_I = icon('<rect x="26" y="10" width="6" height="40" fill="var(--stone-dark)"/><path d="M10 14 h36 l-6 10 6 10 h-36z" fill="var(--accent)"/>')

PAGE = {
    "slug": "sharding", "order": 10,
    "title": ("번호별로 나뉜 매표 창구", "Ticket Booths Split by Number"),
    "h1": ("<em>샤딩</em>이 뭐예요?", "What is <em>Sharding</em>?"),
    "sub": ("샤딩을 손님 명부를 번호별로 나눈 매표 창구 이야기로 풀어봤어요.",
            "Sharding, told as a story about ticket booths that split the guest log by number."),
    "panels": [
        {"svg": P1, "alt": ("매표 창구 하나와 그 옆 안내판에 백만 명 손님 명부 전체가 적혀 있음", "One ticket booth with a sign showing the whole log of a million guests"),
         "caption": ("창구 하나에 손님 명부 전체가 있어요.", "One booth holds the whole guest log."),
         "small": ("이름을 찾으려면 명부 전체를 뒤져야 해요.", "Finding a name means searching the whole thing.")},
        {"svg": P2, "alt": ("요원이 땀을 흘리며 이름을 찾고, 줄은 점점 길어짐", "A sweating operator searches for a name while the line keeps growing"),
         "caption": ("손님이 백만 명이면 이름 찾기가 느려요.", "With a million guests, finding a name is slow."),
         "small": ("한 장부에서 다 찾으려니 시간이 걸려요.", "Searching one giant ledger takes a long time.")},
        {"svg": P3, "hero": True, "alt": ("창구 네 개가 번호 구간별로 나뉘어 있고, 손님들이 자기 구간 창구로 나뉘어 줄을 섬", "Four booths split by number range, with guests lining up at their own range"),
         "caption": ("번호별로 창구를 나누면 — 각 창구는 적은 명부만 봐요.", "Split booths by number, and each one scans a small slice."),
         "small": ("찾는 시간이 창구 수만큼 짧아져요.", "The search gets faster, one booth's worth at a time."),
         "tricks": (4, [
             (HASH_I, ("나누는 기준을 정해요", "Pick a split rule"), ("번호나 이름으로요", "by number or by name"), "calm"),
             (SLICE_I, ("창구마다 적은 양만", "Each booth sees less"), ("찾기가 빨라져요", "so searching is faster")),
             (REBAL_I, ("몰리면 또 나눠요", "Rebalance when crowded"), ("리밸런싱이에요", "that's rebalancing"), "warm"),
             (SIGN_I, ("안내판이 필요해요", "You need a sign"), ("어느 창구인지 알려줘요", "to show which booth to go to")),
         ])},
        {"svg": P4, "alt": ("안내판이 번호 601은 4번 창구라고 알려주고, 손님이 그 창구로 감", "A sign tells guest number 601 to go to booth 4, and the guest walks there"),
         "caption": ("나누는 기준과 안내판이 한 세트예요.", "A split rule and a sign always go together."),
         "small": ("번호를 보고 바로 맞는 창구로 가요.", "The number tells you exactly which booth to visit.")},
        {"svg": P5, "alt": ("왼쪽: 1번 창구에만 줄이 몰림(핫스팟). 오른쪽: 전체 손님 수를 물으니 창구 네 곳을 다 더해야 함", "Left: booth 1 overloaded with a line (hotspot). Right: asking for the total means adding up all four booths"),
         "caption": ("번호를 잘못 나누면 한 곳에만 몰려요.", "Split the numbers badly and everyone piles into one booth."),
         "small": ("그리고 창구를 가로질러 묻는 질문엔 느려요.", "And questions that cross every booth are slow.")},
    ],
    "summary": (("<b>샤딩</b> = 손님 명부를 <b>번호(기준)로 나눠</b> 여러 창구에 <b>조금씩만</b> 맡기는 일. 안내판이 어느 창구인지 알려주고, 한쪽이 몰리면 다시 나눠요.",
                 "<b>Sharding</b> = splitting the guest log <b>by a rule (a number)</b> so each booth only holds <b>a small slice</b>. A sign shows which booth to visit, and an overloaded booth gets rebalanced."),
                ("데이터를 여러 서버(샤드)에 나눠 저장하는 방식이에요. 나누는 기준을 파티션 키라고 불러요. 한 샤드에 몰리는 걸 핫스팟이라 하고, 여러 샤드에 걸친 질문(크로스-샤드 쿼리)은 느려요.",
                 "Splitting data across multiple servers (shards). The rule used to split is called a partition key. One shard getting overloaded is a hotspot, and a query spanning multiple shards (a cross-shard query) is slow.")),
    "glossary": [
        ("샤딩", "Sharding", ("명부를 창구 여러 곳에 나눠 두는 일.", "Spreading the log across several booths."), ("각 창구는 전체가 아니라 일부만 맡아요.", "Each booth owns a slice, not the whole thing.")),
        ("파티션 키", "Partition key", ("나누는 기준.", "The rule used to split."), ("번호나 이름 앞글자 같은 거예요.", "Something like a number or the first letter of a name.")),
        ("핫스팟", "Hotspot", ("한쪽 창구에만 몰리는 것.", "Everyone piling into one booth."), ("기준을 잘못 고르면 생겨요.", "Happens when the split rule is picked badly.")),
        ("리밸런싱", "Rebalancing", ("몰린 창구를 다시 나누는 일.", "Re-splitting an overloaded booth."), ("핫스팟이 생기면 해요.", "Done when a hotspot shows up.")),
        ("일관 해싱", "Consistent hashing", ("재배치를 적게 하는 나누기 방법.", "A split method that minimizes reshuffling."), ("한 줄로만 말하면 '재배치를 줄이는 나누기'예요.", "In one line: splitting that avoids moving everything around.")),
        ("크로스-샤드 쿼리", "Cross-shard query", ("창구 여러 곳을 다 더해야 답이 나오는 질문.", "A question that needs every booth added up."), ("전체 손님 수 같은 질문이 느린 이유예요.", "Why a question like \"total guests\" is slow.")),
        ("복제", "Replication", ("창구 하나가 아니라 여러 곳에 똑같이 적어 두는 일.", "Writing the same log in more than one place."), ('샤딩과는 다른 문제예요 — 양이 아니라 안전을 위해서예요. → <a href="replication-ko.html">손님 명부를 두 창고에 똑같이</a>', "A different problem from sharding — it's for safety, not for size. → <a href=\"replication-en.html\">the same guest log in two warehouses</a>")),
        ("수평 확장", "Horizontal scaling", ("창구를 더 늘리는 방법.", "Adding more booths instead of a bigger one."), ("샤딩은 수평 확장의 대표적인 방법이에요.", "Sharding is a classic way to scale horizontally.")),
    ],
}
