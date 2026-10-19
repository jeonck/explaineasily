from _draw import *
from _world import *

# 1. 한 건물에만 다 맡기면 불안해요
P1 = svg(300, sky(300)
         + building(300, 50, 1.0)
         + person(560, 198, s=0.8, face=EYES, **TENANT)
         + bubble(500, 70, 240, 60, "⟦이 건물 하나에 전부 맡기면... 불안한데요|putting everything in just one building feels risky...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦한 건물에만 전부 맡기면 불안해요|relying on just one building for everything feels risky⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 그 건물에 문제가 생기면 전부 같이 멈춰요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + building(300, 50, 1.0)
         + '<path d="M320 70 L420 170" stroke="var(--bad)" stroke-width="5"/><path d="M420 70 L320 170" stroke="var(--bad)" stroke-width="5"/>'
         + person(560, 198, s=0.7, face=FROWN + SWEAT, **TENANT)
         + label(560, 268, "⟦건물 하나가 멈추면 내 회사도 같이 멈춰요|one building goes down, and my whole company goes down with it⟧", 11, "var(--ink)")
         + label(380, 282, "⟦건물 하나에 문제가 생기면 전부 같이 멈춰요|trouble in one building, and everything stops together⟧", 12, "var(--ink)"))

# 3. hero: 멀티클라우드 = 여러 건물에 동시에 입주하는 전략
P3 = svg(360, sky(360)
         + building(60, 60, 0.85, label_text="⟦건물A|Building A⟧")
         + building(330, 40, 0.95, label_text="⟦건물B|Building B⟧")
         + building(600, 70, 0.8, label_text="⟦건물C|Building C⟧")
         + person(220, 267, s=0.65, face=SMILE, **TENANT)
         + '<path d="M250 257 L120 220" stroke="var(--good)" stroke-width="2" stroke-dasharray="5 4"/>'
         + '<path d="M250 257 L400 180" stroke="var(--good)" stroke-width="2" stroke-dasharray="5 4"/>'
         + '<path d="M250 257 L650 220" stroke="var(--good)" stroke-width="2" stroke-dasharray="5 4"/>'
         + label(380, 30, "⟦멀티클라우드 = 한 회사가 여러 건물에 동시에 입주해요|multi-cloud = one company moves into several buildings at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦한 건물에 다 의존하지 않으려는 전략이에요|a strategy to avoid depending on any one building⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 왜 여러 건물에 나누나 — 재해대비/가격비교/지역규제
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦왜 여러 건물에 나눠 입주하나|why split across several buildings⟧",
                     ("⟦재해 대비: 한 건물이 멈춰도 다른 건물이 받쳐줘요|disaster readiness: if one building goes down, another covers⟧",
                      "⟦가격 비교: 건물마다 임대료가 달라요|price comparison: rent differs building to building⟧",
                      "⟦지역 규제: 어떤 데이터는 특정 지역 건물에만 둬야 해요|local rules: some data must stay in a building in a specific region⟧",
                      "⟦최신 설비: 건물마다 잘하는 설비(서비스)가 달라요|best-of-breed: each building is strong at different gear (services)⟧"), 1.0))

# 5. 깨지는 곳: 건물마다 규칙이 달라서 관리가 더 복잡하고 비용이 이중으로 들어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.75, face=FROWN + SWEAT, **TENANT)
         + label(190, 240, "⟦건물마다 규칙·용어가 달라 배우기 힘들어요|different rules and terms per building — hard to learn them all⟧", 11, "var(--ink)")
         + person(570, 150, s=0.75, face=EYES, **TENANT)
         + label(570, 240, "⟦관리 인력과 비용이 건물 수만큼 늘어나요|staff and cost grow with every extra building⟧", 11, "var(--ink)"))

RISK_I = icon('<circle cx="20" cy="20" r="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><circle cx="44" cy="20" r="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><path d="M20 20 L44 20" stroke="var(--good)" stroke-width="2" stroke-dasharray="3 3"/>')
PRICE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><text x="32" y="40" font-size="22" font-weight="800" text-anchor="middle" fill="var(--accent)">₩</text>')
REGION_I = icon('<path d="M32 8 C44 8 52 18 52 28 C52 42 32 56 32 56 C32 56 12 42 12 28 C12 18 20 8 32 8 Z" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/>')
COMPLEX_I = icon('<path d="M10 54 L54 10" stroke="var(--bad)" stroke-width="4"/><path d="M10 10 L54 54" stroke="var(--bad)" stroke-width="4"/>')

PAGE = {
    "slug": "multicloud", "order": 11,
    "title": ("여러 건물에 동시에 입주하기", "Moving Into Several Buildings at Once"),
    "h1": ("<em>멀티클라우드</em>가 뭐예요?", "What is <em>Multi-Cloud</em>?"),
    "sub": ("멀티클라우드를, 한 건물에만 의존하지 않으려고 여러 건물에 동시에 입주하는 전략 이야기로 풀어봤어요.",
            "Multi-cloud, told as a strategy of moving into several buildings at once instead of depending on just one."),
    "panels": [
        {"svg": P1, "alt": ("입주사가 한 건물에 전부 맡기면 불안하다고 말풍선으로 걱정함", "A tenant worries aloud that relying on just one building for everything feels risky"),
         "caption": ("한 건물에만 전부 맡기면 불안해요.", "Relying on just one building for everything feels risky."),
         "small": ("건물 하나에 모든 걸 거는 셈이니까요.", "It means betting everything on a single building.")},
        {"svg": P2, "alt": ("건물에 큰 X 표시가 겹쳐지며 문제가 생기고, 그 건물에만 의존하던 입주사가 같이 멈춰 땀을 흘림", "An X mark crosses over a building in trouble, and the tenant who depended on it alone is sweating, stopped in their tracks"),
         "caption": ("건물 하나에 문제가 생기면 전부 같이 멈춰요.", "Trouble in one building, and everything stops together."),
         "small": ("의존하던 곳이 하나뿐이었으니까요.", "Because there was only one place to depend on.")},
        {"svg": P3, "hero": True, "alt": ("한 입주사가 건물 A, B, C 세 곳에 동시에 점선으로 연결되어 입주해 있음", "One tenant is connected by dashed lines to three different buildings, A, B, and C, all at once"),
         "caption": ("멀티클라우드 = 여러 건물에 동시에 입주해요.", "Multi-cloud = one company moves into several buildings at once."),
         "small": ("한 건물에 다 의존하지 않으려는 전략이에요.", "A strategy to avoid depending on any one building."),
         "tricks": (4, [
             (RISK_I, ("재해에 대비해요", "Prepares for disaster"), ("한 건물이 멈춰도 다른 건물이 받쳐줘요", "if one goes down, another covers"), "calm"),
             (PRICE_I, ("임대료를 비교해요", "Compares the rent"), ("건물마다 가격이 달라요", "price differs building to building")),
             (REGION_I, ("지역 규제를 맞춰요", "Meets local rules"), ("어떤 데이터는 특정 지역에만 둬야 해요", "some data must stay in a specific region"), "warm"),
             (COMPLEX_I, ("대신 관리가 복잡해져요", "But it makes management harder"), ("건물마다 규칙이 다 달라서요", "because every building's rules differ")),
         ])},
        {"svg": P4, "alt": ("여러 건물에 나누는 이유를 재해대비, 가격비교, 지역규제, 최신설비 네 가지로 정리한 안내판", "A board listing four reasons to split across buildings: disaster readiness, price comparison, local rules, best-of-breed gear"),
         "caption": ("여러 건물에 나누는 데는 네 가지 이유가 있어요.", "There are four reasons to split across buildings."),
         "small": ("회사마다 어느 이유를 더 중요하게 보는지가 달라요.", "Which reason matters most differs company to company.")},
        {"svg": P5, "alt": ("왼쪽: 건물마다 규칙과 용어가 달라 배우기 힘든 입주사. 오른쪽: 관리 인력과 비용이 건물 수만큼 늘어난다고 말하는 입주사", "Left: a tenant struggling to learn different rules and terms per building. Right: a tenant noting staff and cost grow with every extra building"),
         "caption": ("건물마다 규칙이 달라 관리가 더 복잡해져요.", "Different rules per building make management harder."),
         "small": ("관리 인력과 비용이 이중, 삼중으로 늘어나요.", "Staff and cost multiply with every extra building.")},
    ],
    "summary": (("<b>멀티클라우드</b> = 한 회사가 <b>여러 클라우드 건물에 동시에 입주</b>해서, <b>한 곳에만 의존하는 위험을 줄이는</b> 전략.",
                 "<b>Multi-cloud</b> is a strategy where one company <b>moves into several cloud \"buildings\" at once</b>, to <b>reduce the risk of depending on just one</b>."),
                ("서로 다른 클라우드 제공자(예: 둘 이상의 CSP)를 동시에 사용하는 전략이에요. 특정 업체 장애나 가격 인상에 대한 위험 분산, 서비스별 강점 활용, 지역·규제 요건 충족이 목적이에요. 다만 제공자마다 API·운영 방식이 달라 관리 복잡도와 비용이 함께 늘어나는 트레이드오프가 있어요.",
                 "A strategy of using multiple cloud providers (two or more CSPs) at the same time. The goals are spreading risk against one vendor's outage or price hikes, using each provider's particular strengths, and meeting regional or regulatory requirements. The trade-off is that different providers have different APIs and operational models, so management complexity and cost rise together.")),
    "glossary": [
        ("멀티클라우드", "Multi-cloud", ("여러 건물에 동시에 입주하는 전략.", "The strategy of moving into several buildings at once."), ("한 곳에 의존하는 위험을 줄여줘요.", "Reduces the risk of depending on just one.")),
        ("벤더 락인", "Vendor lock-in", ("한 건물 방식에만 너무 맞춰져서 못 옮기는 상태.", "Being fit so tightly to one building's way that you can't move."), ("멀티클라우드가 줄이려는 바로 그 위험이에요.", "Exactly the risk multi-cloud tries to reduce.")),
        ("재해 복구", "Disaster recovery", ("한 건물이 멈춰도 다른 건물이 받쳐주는 것.", "Another building covering when one goes down."), ("여러 건물에 나누는 가장 큰 이유 중 하나예요.", "One of the biggest reasons to split across buildings.")),
        ("데이터 주권/지역 규제", "Data sovereignty / regional rules", ("어떤 데이터는 특정 지역 건물에만 둬야 한다는 규칙.", "The rule that some data must stay in a building in a specific region."), ("공공부문에서 특히 중요해요.", "Especially important in the public sector.")),
        ("하이브리드클라우드", "Hybrid cloud", ("내 건물과 공유 건물을 함께 쓰는 것.", "Using your own building together with a shared one."), ("멀티클라우드와 자주 혼동되지만 축이 달라요 — 직접 지은 건물 포함 여부예요.", "Often confused with multi-cloud, but the axis differs — whether your own building is included.")),
        ("공공부문 클라우드 활용", "Public-sector cloud adoption", ("검증된 건물에만 등급 맞춰 입주하는 규정.", "The rule: move into a certified building, at the right grade."), ('공공기관도 이중화를 위해 멀티클라우드를 쓰기도 해요. → <a href="govcloud-ko.html">검증된 건물에만 입주</a>', 'Public agencies sometimes use multi-cloud for redundancy too. → <a href="govcloud-en.html">only into a certified building</a>')),
        ("클라우드 서비스 모델", "Cloud service model", ("뼈대만/인테리어까지/완제품.", "Bare shell / interior done / move-in ready."), ('어느 건물이든 이 세 모델 중 하나로 빌려요. → <a href="cloudmodel-ko.html">셋 중 골라 빌리기</a>', 'Any building is rented as one of these three models. → <a href="cloudmodel-en.html">pick one to rent</a>')),
        ("API", "API", ("건물마다 다른 '입주 신청 방식'.", "Each building's own \"how to apply for a lease\" process."), ("건물마다 달라서 멀티클라우드 관리를 복잡하게 만들어요.", "Differs by building, which is what makes multi-cloud management complex.")),
    ],
}
