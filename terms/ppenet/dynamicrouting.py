from _draw import *
from _world import *

# 1. 길이 막혔는데 지도는 그대로예요
P1 = svg(300, sky(300)
         + postoffice(560, 160, 0.7)
         + '<path d="M520 230 l60 0" stroke="var(--bad)" stroke-width="6"/><path d="M530 220 l20 20 M550 220 l-20 20" stroke="var(--bad)" stroke-width="4"/>'
         + person(300, 180, s=0.85, face=SWEAT + EYES, **CARRIER)
         + routemap(80, 60, 220, 110, "⟦옛 지도|old map⟧", ("⟦우체국 C로|to Office C⟧",), 0.9)
         + label(380, 280, "⟦지도엔 아직 그 길이 멀쩡하다고 적혀 있어요|the map still says that road is just fine⟧", 12, "var(--ink)"))

# 2. 사람이 매번 손으로 지도를 고칠 순 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(260, 160, s=0.8, face=FROWN, **CLERK)
         + label(260, 230, "⟦세상 모든 길을 매번 손으로 고칠 순 없어요|nobody can hand-redraw every road every time something changes⟧", 11, "var(--ink)")
         + routemap(430, 60, 260, 170, "⟦지도 갱신 대기 중...|map update pending...⟧", ("⟦A → B|A → B⟧", "⟦B → C|B → C⟧", "⟦C → D|C → D⟧"), 0.85)
         + label(380, 282, "⟦변화가 끊임없는데 지도만 가만히 있으면 안 돼요|the world keeps changing — the map can't just sit still⟧", 12, "var(--ink)", cls="d"))

# 3. 동적 라우팅 = 우체국들이 소식을 주고받아 지도를 스스로 고침 (hero)
P3 = svg(340, sky(340)
         + postoffice(220, 170, 0.6) + postoffice(400, 170, 0.6) + postoffice(580, 170, 0.6)
         + '<path d="M260 180 q60 -30 120 0 M440 180 q60 -30 120 0" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'
         + label(380, 30, "⟦동적 라우팅 = 우체국들이 서로 소식을 주고받아 지도를 스스로 고치는 규칙|dynamic routing = post offices trade news and redraw the map themselves⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦RIP는 소문으로, OSPF는 전체 지도 공유로, IGP는 한 회사 안 규칙으로|RIP by rumor, OSPF by sharing the whole map, IGP as the rule inside one company⟧", 12, "var(--muted)"))

# 4. RIP vs OSPF 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦RIP — 소문으로 전달|RIP — spreads by rumor⟧",
                    ("⟦이웃에게만 소식 전달|tells only its neighbors⟧",
                     "⟦홉 수로 가까운 길 판단|judges by hop count⟧",
                     "⟦간단하지만 느림|simple but slow⟧",
                     "⟦작은 망에 알맞음|fits a small network⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦OSPF — 전체 지도 공유|OSPF — shares the whole map⟧",
                    ("⟦모두에게 지도 전체를 공유|shares the full map with everyone⟧",
                     "⟦링크 상태로 최단 경로 계산|computes shortest path by link state⟧",
                     "⟦빠르고 정확함|fast and accurate⟧",
                     "⟦큰 망에도 알맞음|fits a large network too⟧"), 1.0, hl=1))

# 5. 퍼지는 데 시간이 걸리고, 바깥 회사완 다른 규칙이 필요해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + postoffice(190, 170, 0.7) + label(190, 250, "⟦소식이 다 퍼질 때까진 잠깐 시간이 걸려요|spreading the news to everyone still takes a moment⟧", 11, "var(--ink)")
         + postoffice(560, 150, 0.5) + postoffice(640, 150, 0.5)
         + label(600, 250, "⟦다른 회사 우체국과는 또 다른 규칙(IGP 밖)을 써요|a different company's post office needs a different rule (outside the IGP)⟧", 11, "var(--ink)"))

RUMOR_I = icon('<circle cx="18" cy="32" r="8" fill="var(--accent)"/><circle cx="46" cy="32" r="8" fill="var(--accent)"/><path d="M26 32 h12" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 3"/>')
MAP_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><path d="M18 44 L28 22 L38 38 L46 20" stroke="var(--accent)" stroke-width="3" fill="none"/>')
INSIDE_I = icon('<rect x="12" y="12" width="40" height="40" rx="6" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--good)"/>')
REFRESH_I = icon('<path d="M46 20 a18 18 0 1 0 6 14" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M46 10 v12 h-12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "dynamicrouting", "order": 8,
    "title": ("스스로 고쳐 그리는 배송 지도", "The Delivery Map That Redraws Itself"),
    "h1": ("<em>동적 라우팅 프로토콜</em>이 뭐예요?", "What is a <em>Dynamic Routing Protocol</em>?"),
    "sub": ("RIP/OSPF/IGP를, 우체국들이 서로 소식을 주고받아 지도를 스스로 고치는 이야기로 풀어봤어요.",
            "RIP/OSPF/IGP, told as a story about post offices trading news and redrawing their map themselves."),
    "panels": [
        {"svg": P1, "alt": ("길이 막혔는데 집배원이 든 옛 지도엔 아직 그 길이 멀쩡하다고 적혀 있음", "A road is blocked, but the carrier's old map still marks it as fine"),
         "caption": ("길이 막혔는데 지도는 그대로예요.", "The road is blocked, but the map hasn't changed."),
         "small": ("지도엔 아직 그 길이 멀쩡하다고 적혀 있어요.", "The map still says that road is just fine.")},
        {"svg": P2, "alt": ("우체국장이 세상 모든 길을 손으로 못 고친다고 걱정하며 갱신 대기 중인 지도를 바라봄", "A postmaster worries about redrawing every road by hand, staring at a map stuck on 'update pending'"),
         "caption": ("사람이 매번 손으로 지도를 고칠 순 없어요.", "Nobody can hand-redraw the map every time."),
         "small": ("변화가 끊임없는데 지도만 가만히 있으면 안 돼요.", "The world keeps changing — the map can't just sit still.")},
        {"svg": P3, "hero": True, "alt": ("우체국 세 곳이 점선 화살표로 서로 소식을 주고받으며 지도를 스스로 고침", "Three post offices trade dashed-arrow news with each other, redrawing the map themselves"),
         "caption": ("우체국들이 소식을 주고받아 지도를 스스로 고쳐요.", "Post offices trade news and redraw the map themselves."),
         "small": ("RIP는 소문으로, OSPF는 전체 지도 공유로, IGP는 한 회사 안 규칙으로요.", "RIP by rumor, OSPF by sharing the whole map, IGP as the rule inside one company."),
         "tricks": (4, [
             (RUMOR_I, ("RIP — 소문 전달", "RIP — spreads by rumor"), ("이웃에게만 홉 수로 소식을 전해요", "tells only neighbors, counted in hops"), "calm"),
             (MAP_I, ("OSPF — 전체 지도 공유", "OSPF — shares the whole map"), ("모두가 같은 지도를 보고 계산해요", "everyone computes from the same shared map")),
             (INSIDE_I, ("IGP — 회사 내부 규칙", "IGP — the rule inside one org"), ("한 회사 안에서만 쓰는 규칙 범주예요", "a category of rules used only inside one organization"), "warm"),
             (REFRESH_I, ("자동 갱신", "Self-updating"), ("길이 막히면 지도가 스스로 바뀌어요", "the map rewrites itself when a road jams")),
         ])},
        {"svg": P4, "alt": ("RIP와 OSPF를 전달 방식·계산법·속도·규모로 비교한 두 지도", "Two maps comparing RIP and OSPF by how they spread news, compute paths, speed, and scale"),
         "caption": ("RIP와 OSPF는 네 가지가 달라요.", "RIP and OSPF differ on four things."),
         "small": ("RIP는 간단하지만 느리고, OSPF는 빠르고 정확하지만 더 복잡해요.", "RIP is simple but slow; OSPF is fast and accurate but more complex.")},
        {"svg": P5, "alt": ("왼쪽: 소식이 다 퍼지는 데 잠깐 걸림. 오른쪽: 다른 회사 우체국과는 다른 규칙을 씀", "Left: spreading the news takes a moment. Right: a different company's post office uses a different rule"),
         "caption": ("퍼지는 데 시간이 걸리고, 바깥 회사완 다른 규칙이 필요해요.", "Spreading takes time, and talking to another company needs a different rule."),
         "small": ("자동이라도 소식이 다 퍼질 때까진 시간이 걸리고, IGP는 회사 밖에선 안 통해요.", "Even automatic, spreading news takes time — and IGP doesn't reach outside one's own organization.")},
    ],
    "summary": (("<b>동적 라우팅 프로토콜</b>은 <b>우체국(라우터)들이 서로 소식을 주고받아 배송 지도(경로표)를 스스로 갱신</b>하는 규칙이에요(RIP·OSPF 등 IGP).",
                 "A <b>dynamic routing protocol</b> is a set of rules by which <b>post offices (routers) trade news and update the delivery map (routing table) themselves</b> — RIP, OSPF, and other IGPs."),
                ("RIP(Routing Information Protocol)는 거리 벡터 방식으로 이웃에게만 홉 수를 전파해 경로를 정하는 단순하지만 느린 프로토콜이고, OSPF(Open Shortest Path First)는 링크 상태 방식으로 전체 지도를 공유해 최단 경로를 계산하는 빠르고 확장성 있는 프로토콜이에요. 둘 다 한 조직(자율 시스템) 내부에서 쓰는 IGP(Interior Gateway Protocol)이고, 조직 간에는 BGP 같은 EGP를 따로 써요.",
                 "RIP (Routing Information Protocol) is a distance-vector protocol that propagates hop counts only to neighbors — simple but slow. OSPF (Open Shortest Path First) is a link-state protocol that shares the whole topology map and computes shortest paths — fast and scalable. Both are IGPs (Interior Gateway Protocols) used inside one organization (autonomous system); between organizations, a separate EGP like BGP is used instead.")),
    "glossary": [
        ("동적 라우팅", "Dynamic routing", ("우체국들이 소식을 주고받아 지도를 스스로 고치는 것.", "Post offices trading news and redrawing the map themselves."), ("정적 라우팅은 사람이 손으로 고쳐요.", "Static routing, by contrast, is redrawn by hand.")),
        ("RIP", "RIP", ("이웃에게만 소문으로 퍼지는 방식.", "Spreading only to neighbors, by rumor."), ("홉 수로 가까운 길을 판단해요.", "Judges distance by counting hops.")),
        ("OSPF", "OSPF", ("전체 지도를 모두에게 공유하는 방식.", "Sharing the whole map with everyone."), ("링크 상태로 최단 경로를 계산해요.", "Computes the shortest path from link state.")),
        ("IGP", "IGP", ("한 회사 안에서만 쓰는 라우팅 규칙 범주.", "A category of routing rules used only inside one organization."), ("RIP·OSPF가 여기에 속해요.", "RIP and OSPF both belong to this category.")),
        ("홉 수", "Hop count", ("거쳐 가는 우체국 숫자.", "The number of post offices a parcel passes through."), ("RIP가 경로를 판단하는 기준이에요.", "The yardstick RIP uses to judge a route.")),
        ("수렴(convergence)", "Convergence", ("소식이 모든 우체국에 다 퍼지는 데 걸리는 시간.", "The time it takes for news to spread to every post office."), ("이 시간 동안은 지도가 아직 다 안 맞아요.", "During this time, the map isn't fully accurate yet.")),
        ("IPv6", "IPv6", ("훨씬 길어진 새 집 주소 체계.", "The far longer new house-address system."), ('라우팅 지도의 주소 자체가 이 체계로 바뀌어 가고 있어요. → <a href="ipv6-ko.html">끝없이 늘어난 새 번지수</a>', "The addresses on the routing map itself are moving to this system. → <a href=\"ipv6-en.html\">the new, nearly endless address system</a>")),
        ("DNS", "DNS", ("동네 주소록.", "The neighborhood address book."), ('주소가 틀리면 아무리 좋은 지도도 소용없어요. → <a href="dns-ko.html">동네 주소록</a>', "No map helps if the address itself is wrong. → <a href=\"dns-en.html\">the neighborhood address book</a>")),
    ],
}
