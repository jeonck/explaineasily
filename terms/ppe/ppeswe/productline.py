from _draw import *
from _world import *

# 1. 지역판마다 책을 처음부터 새로 씀
P1 = svg(300, sky(300)
         + person(120, 150, s=0.7, face=SWEAT, **WRITER) + manuscript(120, 230, 0.55)
         + person(300, 150, s=0.7, face=SWEAT, **WRITER) + manuscript(300, 230, 0.55)
         + person(480, 150, s=0.7, face=SWEAT, **WRITER) + manuscript(480, 230, 0.55)
         + person(650, 150, s=0.7, face=SWEAT, **WRITER) + manuscript(650, 230, 0.55)
         + label(380, 40, "⟦한국판, 일본판, 미국판... 가이드북을 매번 처음부터 새로 써요|Korean, Japanese, US editions — every guidebook written from zero, every time⟧", 13, "var(--ink)"))

# 2. 겹치는 챕터까지 매번 새로 쓰다 보니 설명이 조금씩 달라짐
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(190, 130, 0.9, text="⟦\"지도 보는 법\" A판|\"how to read maps\" ed. A⟧")
         + manuscript(570, 130, 0.9, text="⟦\"지도 보는 법\" B판|\"how to read maps\" ed. B⟧")
         + label(380, 60, "⟦같은 '지도 보는 법'인데 판마다 설명이 조금씩 달라요|the same 'how to read maps' chapter reads differently in each edition⟧", 13, "var(--bad)")
         + label(380, 260, "⟦매번 새로 쓰면 느리고, 판마다 품질도 들쭉날쭉해져요|writing it fresh every time is slow, and quality drifts between editions⟧", 12, "var(--ink)", cls="d"))

# 3. 공통 챕터는 서가에 모아두고, 다른 부분만 바꿔 끼움 (hero)
P3 = svg(340, sky(340)
         + bookshelf(80, 90, 1.1, n=4, hl=1)
         + label(192, 230, "⟦핵심 자산(공통 챕터)|CORE ASSETS (shared chapters)⟧", 11, "var(--muted)")
         + printplate(360, 150, 0.8, "⟦한국판|KR edition⟧")
         + printplate(480, 150, 0.8, "⟦일본판|JP edition⟧")
         + printplate(600, 150, 0.8, "⟦미국판|US edition⟧")
         + label(380, 30, "⟦제품계열 = 공통 챕터는 한 번만 만들고, 다른 부분만 바꿔 끼우기|Product line = build shared chapters once, swap in only what differs⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦서가의 핵심 자산을 가져다 쓰니, 처음부터 쓸 때보다 각 판이 빨리 나와요|reusing the shelf's core assets, each edition comes out faster than writing from zero⟧", 12, "var(--muted)"))

ASSET_I = icon('<rect x="10" y="14" width="44" height="36" rx="3" fill="#5A3B22"/><rect x="16" y="20" width="10" height="24" rx="2" fill="var(--accent)"/><rect x="30" y="20" width="10" height="24" rx="2" fill="#C9A86A"/><rect x="44" y="20" width="6" height="24" rx="2" fill="#C9A86A"/>')
MARK_I = icon('<path d="M20 12 h24 v40 l-12 -10 l-12 10 z" fill="var(--accent)"/>')
DERIVE_I = icon('<rect x="8" y="24" width="20" height="16" rx="2" fill="#4A5A72"/><path d="M28 32 h16" stroke="var(--ink)" stroke-width="3"/><rect x="44" y="18" width="12" height="28" rx="2" fill="#D8D2C2"/>')
VERSION_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M24 32 h16 M32 24 v16" stroke="var(--accent)" stroke-width="3"/>')

PAGE = {
    "slug": "productline", "order": 33,
    "title": ("같은 틀, 다른 표지", "Same Template, Different Covers"),
    "h1": ("<em>제품계열(Product Line) 방법론</em>이 뭐예요?", "What is <em>Software Product Line</em> Engineering?"),
    "sub": ("여러 지역판 가이드북을 하나의 공통 틀에서 빠르게 찍어내는 이야기예요.",
            "A story about spinning off many regional guidebook editions quickly from one shared template."),
    "panels": [
        {"svg": P1, "alt": ("작가 네 명이 한국판·일본판·미국판 같은 지역판 가이드북을 각자 처음부터 새로 씀", "Four authors each write a regional guidebook edition, such as Korean, Japanese, or US, from scratch"),
         "caption": ("지역판마다 가이드북을 처음부터 새로 써요.", "Every regional edition gets written from zero."),
         "small": ("판이 늘어날수록 반복되는 일도 늘어나요.", "The more editions, the more repeated work.")},
        {"svg": P2, "alt": ("같은 '지도 보는 법' 챕터가 A판과 B판에서 서로 다르게 쓰여 있음", "The same 'how to read maps' chapter is written differently in edition A and edition B"),
         "caption": ("겹치는 챕터도 매번 새로 쓰다 보니 설명이 달라져요.", "Even overlapping chapters get rewritten and drift apart."),
         "small": ("매번 새로 쓰면 느리고, 판마다 품질도 들쭉날쭉해져요.", "Writing it fresh every time is slow and the quality drifts.")},
        {"svg": P3, "hero": True, "alt": ("서가에 핵심 공통 챕터를 모아두고, 그로부터 한국판·일본판·미국판 세 가지 인쇄판을 파생시킴", "Core shared chapters sit on a shelf, and three print editions — KR, JP, US — are derived from them"),
         "caption": ("제품계열 = 공통 챕터는 한 번만 만들고, 다른 부분만 바꿔 끼우는 거예요.", "Product line = build the shared chapters once, swap in only what differs."),
         "small": ("서가의 핵심 자산을 가져다 쓰니, 처음부터 쓸 때보다 각 판이 빨리 나와요.", "Reusing the shelf's core assets, each edition comes out faster than writing from zero."),
         "tricks": (4, [
             (ASSET_I, ("핵심 자산 모으기", "Gather core assets"), ("겹치는 챕터부터 한 곳에", "shared chapters into one place"), "calm"),
             (MARK_I, ("가변점 표시하기", "Mark the variation points"), ("판마다 달라질 자리만 콕 집어", "flag only where editions differ")),
             (DERIVE_I, ("빠르게 파생하기", "Derive quickly"), ("자산 + 가변점 = 새 판", "assets + variation points = new edition"), "warm"),
             (VERSION_I, ("자산도 버전 관리", "Version the assets too"), ("서가 자체도 계속 고쳐나가요", "the shelf itself keeps getting refined")),
         ])},
        {"svg": svg(320, sky(320)
                     + styleguide(60, 40, 280, 240, "⟦핵심 자산(모든 판 공통)|CORE ASSETS (shared)⟧",
                                  ("⟦지도 보는 법|how to read maps⟧", "⟦환전 안내|currency guide⟧", "⟦응급 연락처|emergency contacts⟧"), 1.0)
                     + styleguide(420, 40, 280, 240, "⟦가변점(판마다 다름)|VARIATION POINTS (per edition)⟧",
                                  ("⟦현지 음식 챕터|local food chapter⟧", "⟦언어별 표기|language-specific notes⟧", "⟦표지 디자인|cover design⟧"), 1.0)
                     + label(380, 300, "⟦공통 챕터는 한 번만 쓰고, 판마다 다른 내용은 가변점에만 넣어요|shared chapters get written once; whatever differs per edition goes only in the variation points⟧", 12, "var(--ink)")),
         "alt": ("왼쪽: 모든 판이 공유하는 핵심 자산 목록. 오른쪽: 판마다 달라지는 가변점 목록", "Left: core assets shared by every edition. Right: variation points that differ per edition"),
         "caption": ("가이드북 내용은 둘로 나뉘어요 — 모든 판 공통 부분과 판마다 다른 가변점.", "A guidebook's content splits in two — the part every edition shares, and the variation points that differ."),
         "small": ("공통 챕터는 한 번만 쓰고, 판마다 다른 내용은 가변점에만 넣어요.", "Shared chapters get written once; whatever differs per edition goes only in the variation points.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                     + bookshelf(130, 120, 0.9) + label(190, 250, "⟦서가 덕분에 판마다 빨리, 고른 품질로 나와요|the shelf lets editions come out fast, at even quality⟧", 11, "var(--ink)")
                     + person(570, 150, s=0.8, face=SWEAT, **WRITER) + label(570, 250, "⟦서가의 공통 챕터가 틀리면 모든 판이 같이 틀려요|a wrong shared chapter makes every edition wrong at once⟧", 11, "var(--ink)")
                     + label(380, 282, "⟦핵심 자산을 잘 설계하면 모든 판이 빨라지지만, 잘못 설계하면 모든 판을 고쳐야 해요|good core assets speed up every edition; badly designed ones mean fixing every edition⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 서가 덕분에 빠르고 일관된 결과. 오른쪽: 서가 설계가 잘못되면 작가가 곤란해짐", "Left: the shelf keeps editions fast and consistent. Right: a bad shelf design puts the author in trouble"),
         "caption": ("제품계열에도 대가가 있어요: 핵심 자산을 먼저 잘 설계해야 해요.", "Product line engineering has a price too: the core assets must be designed well up front."),
         "small": ("핵심 자산 설계를 잘못하면 모든 판을 함께 고쳐야 해요.", "A bad core-asset design means fixing every single edition at once.")},
    ],
    "summary": (("<b>제품계열(Product Line) 방법론</b> = 공통된 <b>핵심 자산</b>을 모아두고, <b>가변점</b>만 바꿔서 여러 제품(판)을 빠르게 파생시키는 개발 방식.",
                 "<b>Software Product Line</b> engineering = gathering shared <b>core assets</b> and deriving many products (editions) quickly by changing only the <b>variation points</b>."),
                ("도메인 분석을 통해 제품군의 공통점과 차이점을 미리 식별하고, 공통점은 핵심 자산 저장소에, 차이점은 가변점으로 설계해 둡니다. 새 제품은 핵심 자산을 재사용하고 가변점만 구체화해 만들기 때문에 개발 속도와 일관성이 크게 올라가요.",
                 "Domain analysis identifies what a family of products shares and where they differ up front; shared parts go into a core-asset repository, differences become variation points. A new product reuses the core assets and only fills in its own variation points, which boosts both speed and consistency.")),
    "glossary": [
        ("제품계열(SPL)", "Software Product Line", ("공통 틀에서 여러 판을 찍어내는 개발 방식.", "Deriving many editions from one shared template."), ("도메인 공학이 바탕이에요.", "Built on domain engineering.")),
        ("핵심 자산", "Core Asset", ("모든 판이 공유하는 서가.", "The shelf every edition shares."), ("한 번 만들어 계속 재사용해요.", "Built once, reused repeatedly.")),
        ("가변점", "Variation Point", ("판마다 달라지는 자리.", "The spot that differs per edition."), ("여기만 바뀌면 새 판이 나와요.", "Change only this, and a new edition appears.")),
        ("도메인 공학", "Domain Engineering", ("제품군 전체의 공통점을 미리 찾는 작업.", "Finding what an entire family of products shares, ahead of time."), ("핵심 자산을 설계하기 전 단계예요.", "The stage before designing core assets.")),
        ("재사용", "Reuse", ("서가에서 꺼내 쓰는 것.", "Pulling something off the shelf to use again."), ("제품계열의 핵심 이득이에요.", "The main payoff of product line engineering.")),
        ("개발방법론 테일러링", "Methodology Tailoring", ("규칙집에서 필요한 것만 고르기.", "Picking only what's needed from the rulebook."), ('\'맞춤\'을 다루는 자매 개념이에요. → <a href="tailoring-ko.html">책마다 다른 편집 규칙</a>', 'A sister idea about fitting things to context. → <a href="tailoring-en.html">different editing rules for each book</a>')),
        ("결합도/응집도", "Coupling/Cohesion", ("챕터끼리 얼마나 얽혀있나.", "How entangled the chapters are with each other."), ('핵심 자산이 잘 나뉘었는지 재는 잣대예요. → <a href="couplingcohesion-ko.html">챕터가 서로 얼마나 엮여있나</a>', 'The ruler for whether core assets were split well. → <a href="couplingcohesion-en.html">how tangled the chapters are</a>')),
        ("형상관리", "Configuration Management", ("핵심 자산 버전을 지키는 서가 관리.", "Keeping track of the core assets' own versions."), ("가변점을 관리하는 바탕이 돼요.", "Underpins how variation points get managed.")),
    ],
}
