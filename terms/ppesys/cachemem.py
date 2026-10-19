from _draw import *
from _world import *

WAREHOUSE_X, WAREHOUSE_Y = 560, 230


def warehouse(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="-70" width="120" height="110" fill="#8B5E3C"/>'
            f'<rect x="-60" y="-86" width="120" height="20" fill="#6E4A2E"/>'
            f'<rect x="-20" y="-30" width="40" height="50" fill="var(--night)"/></g>')


# 1. 매번 부품 창고까지 걸어가느라 시간이 다 가요
P1 = svg(300, sky(300)
         + warehouse(660, 190)
         + person(160, 160, s=0.8, face=SWEAT + EYES, **MECH1)
         + label(400, 160, "⟦⟶ ⟶ ⟶|⟶ ⟶ ⟶⟧", 22, "var(--muted)", cls="d")
         + label(380, 30, "⟦나사 하나 가지러 창고까지 매번 걸어가요|every single screw means a walk all the way to the warehouse⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦차 한 대 고치는 사이에 왕복을 수십 번 해요|dozens of round trips just to fix one car⟧", 12, "var(--ink)"))

# 2. 그렇다고 창고를 통째로 옆에 옮겨둘 수도 없어요
P2 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + warehouse(230, 200, 1.5)
         + person(520, 190, s=0.75, face=FROWN, **MECH1)
         + bubble(440, 80, 260, 42, "⟦다 담았더니 뭐가 어디 있는지도 못 찾겠어요|crammed everything in — now I can't even find anything⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 310, "⟦창고를 통째로 옮겨도 다 들고 다닐 순 없고, 뒤지는 시간만 늘어나요|you can't carry the whole warehouse, and searching it all just gets slower⟧", 12, "var(--ink)"))

# 3. 캐시 메모리 = 자주 쓰는 공구만 담아두는 작은 공구함 (hero)
P3 = svg(340, sky(340)
         + warehouse(660, 240)
         + toolbox(300, 240, 1.3, None)
         + person(140, 160, s=0.85, face=SMILE, **MECH1)
         + label(300, 170, "⟦공구함|TOOLBOX⟧", 12, "#142033", cls="d")
         + label(380, 25, "⟦캐시 메모리 = 자주 쓰는 공구만 담아두는 작은 공구함|cache memory = a small toolbox holding only the frequently used tools⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦멀리 있는 창고까지 안 가도, 바로 옆에서 꺼내 써요|no trip to the far warehouse — grab it from right beside you⟧", 12, "var(--muted)"))

# 4. 적중과 미스
P4 = svg(360, sky(360)
         + toolbox(160, 150, 1.1, None) + label(160, 100, "⟦적중(Hit)|HIT⟧", 13, "var(--good)", cls="d")
         + label(160, 210, "⟦공구함에 있으면|if it's in the toolbox⟧", 11, "var(--muted)")
         + label(160, 228, "⟦바로 꺼내요, 빨라요|grab it right away — fast⟧", 11, "var(--muted)")
         + warehouse(600, 220, 1.1) + label(600, 110, "⟦미스(Miss)|MISS⟧", 13, "var(--bad)", cls="d")
         + label(600, 300, "⟦없으면 창고까지 가서|if it's not, walk to the warehouse⟧", 11, "var(--muted)")
         + label(600, 318, "⟦가져와요, 느려요|fetch it — slow⟧", 11, "var(--muted)")
         + label(380, 345, "⟦L1→L2→L3처럼 단계별로 더 크고 더 느린 공구함을 두기도 해요|some garages keep L1→L2→L3, each bigger and a bit slower⟧", 12, "var(--ink)"))

# 5. 공구함을 늘린다고 항상 빨라지진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + toolbox(190, 150, 1.0, None) + label(190, 230, "⟦자주 쓰는 것만 담으면|keep only the frequent ones⟧", 11, "var(--ink)")
         + label(190, 248, "⟦찾는 것도 빨라요|and finding things stays fast⟧", 11, "var(--ink)")
         + toolbox(570, 150, 1.8, None) + label(570, 240, "⟦안 쓰는 것까지 다 담으면|cram in the rarely used too⟧", 11, "var(--ink)")
         + label(570, 258, "⟦뒤지는 시간만 늘어요|and searching just gets slower⟧", 11, "var(--ink)")
         + label(380, 282, "⟦캐시는 크기가 아니라 \"무엇을 담느냐\"가 핵심이에요(지역성)|cache is about what you keep, not how big it is (locality)⟧", 12, "var(--ink)", cls="d"))

HIT_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
MISS_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 l20 20 M42 22 l-20 20" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
LOCAL_I = icon('<circle cx="32" cy="32" r="10" fill="var(--accent)"/><circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 4"/>')
EVICT_I = icon('<rect x="12" y="20" width="40" height="28" rx="4" fill="none" stroke="var(--muted)" stroke-width="3"/><path d="M32 12 v16 M24 20 l8 -8 l8 8" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "cachemem", "order": 3,
    "title": ("바로 옆에 놓아둔 공구함", "The Toolbox Kept Right Beside You"),
    "h1": ("<em>캐시 메모리</em>가 뭐예요?", "What is <em>Cache Memory</em>?"),
    "sub": ("캐시 메모리를, 멀리 있는 창고 대신 자주 쓰는 공구만 담아두는 작은 공구함 이야기로 풀어봤어요.",
            "Cache memory, told as a story about a small toolbox holding only the frequently used tools, instead of a trip to the far warehouse."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 나사 하나를 가지러 멀리 있는 부품 창고까지 매번 걸어감", "A mechanic walks all the way to the distant parts warehouse for every single screw"),
         "caption": ("매번 부품 창고까지 걸어가느라 시간이 다 가요.", "Every trip to the far warehouse eats up the time."),
         "small": ("차 한 대 고치는 사이에 왕복을 수십 번 해요.", "Dozens of round trips just to fix one car.")},
        {"svg": P2, "alt": ("창고 전체를 옆으로 옮겨 쌓았더니 정비사가 무엇이 어디 있는지 못 찾음", "The whole warehouse is dragged over, but the mechanic can't find anything in it"),
         "caption": ("그렇다고 창고를 통째로 옮길 수도 없어요.", "But you can't just drag the whole warehouse over."),
         "small": ("다 담으면 뒤지는 시간만 늘어나요.", "Cram it all in, and searching just gets slower.")},
        {"svg": P3, "hero": True, "alt": ("정비사 바로 옆에 작은 공구함을 두고, 멀리 있는 창고는 가끔만 오고 감", "A small toolbox sits right beside the mechanic, while the distant warehouse is visited only occasionally"),
         "caption": ("캐시 메모리 = 자주 쓰는 공구만 담는 작은 공구함이에요.", "Cache memory = a small toolbox holding only the frequent tools."),
         "small": ("멀리 있는 창고까지 안 가도, 바로 옆에서 꺼내 써요.", "No trip to the far warehouse — grab it from right beside you."),
         "tricks": (4, [
             (HIT_I, ("적중(Hit)", "Hit"), ("공구함에 있으면 바로 꺼내요", "it's in the toolbox — grab it")),
             (MISS_I, ("미스(Miss)", "Miss"), ("없으면 창고까지 가야 해요", "it's not — off to the warehouse"), "warm"),
             (LOCAL_I, ("지역성", "Locality"), ("방금 쓴 공구를 또 쓸 확률이 높아요", "the tool you just used, you'll likely need again"), "calm"),
             (EVICT_I, ("교체(Eviction)", "Eviction"), ("안 쓰는 공구를 빼고 새 걸 넣어요", "swap out the unused tool for a new one")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 공구함에 있으면 바로 꺼내는 적중. 오른쪽: 없으면 창고까지 가는 미스. L1·L2·L3 단계도 언급", "Left: a hit — it's in the toolbox. Right: a miss — a trip to the warehouse. L1/L2/L3 levels also noted"),
         "caption": ("적중이면 빠르고, 미스면 느려요.", "A hit is fast; a miss is slow."),
         "small": ("L1→L2→L3처럼 단계별로 더 크고 느린 공구함을 두기도 해요.", "Some garages keep L1→L2→L3, each bigger and a bit slower.")},
        {"svg": P5, "alt": ("왼쪽: 자주 쓰는 것만 담으면 빠르게 유지됨. 오른쪽: 안 쓰는 것까지 다 담으면 오히려 느려짐", "Left: keeping only the frequent tools stays fast. Right: cramming in everything makes it slower"),
         "caption": ("공구함을 늘린다고 항상 빨라지진 않아요.", "A bigger toolbox isn't always a faster one."),
         "small": ("캐시는 크기가 아니라 \"무엇을 담느냐\"가 핵심이에요(지역성).", "Cache is about what you keep, not how big it is (locality).")},
    ],
    "summary": (("<b>캐시 메모리</b> = 멀리 있는 창고(메모리) 대신, <b>자주 쓰는 것만 바로 옆에</b> 담아두는 작은 공구함.",
                 "<b>Cache memory</b> = a small toolbox that keeps only the frequently used items right beside you, instead of the far-off warehouse (main memory)."),
                ("캐시는 CPU와 메인 메모리 사이에 있는 작고 빠른 저장공간이에요. 데이터가 캐시에 있으면 적중(hit), 없으면 미스(miss)로 메인 메모리까지 가져와요. 시간적 지역성(방금 쓴 걸 또 씀)과 공간적 지역성(근처 데이터를 같이 씀) 덕분에 작은 캐시로도 효과가 커요. 꽉 차면 LRU 등의 정책으로 교체(eviction)하고, L1/L2/L3처럼 계층을 둬 속도와 용량을 절충해요.",
                 "Cache is a small, fast storage layer between the CPU and main memory. A hit means the data is already in the cache; a miss means fetching it from main memory. Temporal locality (reusing what you just used) and spatial locality (using nearby data together) make even a small cache effective. When full, a policy like LRU evicts entries, and levels like L1/L2/L3 trade off speed against capacity.")),
    "glossary": [
        ("적중(Hit)", "Cache Hit", ("공구함 안에 있어서 바로 꺼냄.", "It's in the toolbox — grab it right away."), ("빠른 경로예요.", "This is the fast path.")),
        ("미스(Miss)", "Cache Miss", ("공구함에 없어 창고까지 가야 함.", "Not in the toolbox — off to the warehouse."), ("느린 경로예요.", "This is the slow path.")),
        ("지역성", "Locality", ("방금 쓴 공구를 또 쓸 확률이 높다는 것.", "The tool you just used, you'll likely need again."), ("캐시가 작아도 통하는 이유예요.", "This is why even a small cache works.")),
        ("교체 정책(LRU 등)", "Eviction Policy (e.g. LRU)", ("공구함이 꽉 찼을 때 뭘 뺄지 정하는 규칙.", "The rule for deciding what to remove when the toolbox is full."), ("가장 오래 안 쓴 걸 먼저 빼요(LRU).", "Least-recently-used goes first, under LRU.")),
        ("가상메모리·페이징", "Virtual Memory/Paging", ("창고 전체를 내 것처럼 보여주는 가짜 지도.", "A fake map that makes the whole warehouse look like yours."), ('캐시와는 다른 층위의 \'메모리\' 이야기예요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'A different level of "memory" story. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse yours</a>')),
        ("동기화", "Synchronization", ("리프트 열쇠를 나눠주는 규칙.", "The rule for handing out the lift key."), ('여러 코어가 같은 캐시 줄을 쓸 때도 조율이 필요해요. → <a href="syncprim-ko.html">리프트 열쇠는 하나뿐</a>', 'Coordination matters when several cores share a cache line too. → <a href="syncprim-en.html">there\'s only one lift key</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("공구 찾는 시간이 느는 정도를 재는 자.", "The ruler for how much search time grows."), ('적중은 O(1)에 가깝고, 미스는 훨씬 느려요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'A hit is near O(1); a miss is far slower. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("소프트웨어 캐시", "Software Cache", ("CDN·앱이 쓰는 다른 층위의 캐시.", "A cache at a different level, used by CDNs and apps."), ('같은 아이디어가 SRE 세계(앱·CDN 레벨)에도 있어요. → <a href="caching-ko.html">SRE 세계의 캐싱</a>', 'The same idea appears in the SRE world too, at the app/CDN level. → <a href="caching-en.html">caching in the SRE world</a>')),
    ],
}
