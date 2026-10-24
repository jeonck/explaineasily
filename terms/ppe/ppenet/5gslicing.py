from _draw import *
from _world import *

# 1. 수술 로봇 소포가 일반 소포 뒤에서 기다려요
P1 = svg(300, sky(300)
         + '<rect x="0" y="230" width="760" height="20" fill="#8B5E3C"/>'
         + envelope(560, 210, 0.9, text="⟦수술 로봇 신호|surgery robot signal⟧")
         + envelope(420, 210, 0.7) + envelope(480, 210, 0.7) + envelope(500, 220, 0.6)
         + person(620, 160, s=0.8, face=SWEAT + EYES, **RECEIVER)
         + label(380, 30, "⟦수술 로봇 소포가 일반 소포들 뒤에 줄 서서 기다려요|the surgery-robot parcel waits in line behind ordinary ones⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦같은 길을 다 같이 쓰다 보니 급한 것도 순서를 기다려요|sharing one road means even the urgent one waits its turn⟧", 12, "var(--muted)"))

# 2. 길 하나를 모두를 위해 새로 깔 순 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(260, 170, s=0.8, face=FROWN, **CLERK)
         + label(260, 240, "⟦수술용 전용 도로를 따로 깔면 돈이 너무 들어요|a whole separate road just for surgery would cost too much⟧", 11, "var(--ink)")
         + person(520, 170, s=0.8, face=EYES, **CLERK)
         + label(520, 240, "⟦그렇다고 전부 한 줄로 세우면 급한 게 늦어요|but one single line makes the urgent ones late⟧", 11, "var(--ink)")
         + label(380, 282, "⟦한 도로, 서로 다른 급함 — 둘 다 만족시켜야 해요|one road, different urgencies — both have to be satisfied⟧", 12, "var(--ink)", cls="d"))

# 3. 네트워크 슬라이싱 = 한 도로를 전용 차선으로 나누기 (hero)
P3 = svg(340, '<rect width="760" height="340" fill="var(--sky)"/>'
         + '<rect x="40" y="90" width="680" height="40" fill="var(--bad)" opacity="0.85"/>' + label(380, 115, "⟦초저지연 차선 — 수술 로봇|ultra-low-latency lane — surgery robot⟧", 12, "#fff", cls="d")
         + '<rect x="40" y="140" width="680" height="40" fill="var(--accent)" opacity="0.85"/>' + label(380, 165, "⟦대용량 차선 — 동영상|high-bandwidth lane — video⟧", 12, "#fff", cls="d")
         + '<rect x="40" y="190" width="680" height="40" fill="var(--good)" opacity="0.85"/>' + label(380, 215, "⟦일반 차선 — 소포|standard lane — ordinary mail⟧", 12, "#fff", cls="d")
         + label(380, 40, "⟦5G 네트워크 슬라이싱 = 같은 도로에 전용 차선을 나눠, 각자 보장된 속도로 달리게 해요|5G network slicing = split one road into lanes, each guaranteed its own speed⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦도로(물리망)는 하나지만, 차선(슬라이스)은 여러 개예요|one physical road, several logical lanes⟧", 12, "var(--muted)"))

# 4. 슬라이스별 용도 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦슬라이스별 보장 수준|What each slice guarantees⟧",
                    ("⟦초저지연 — 수술 로봇, 지연 최우선|ultra-low-latency — surgery robot, latency first⟧",
                     "⟦대용량 — 동영상, 속도 최우선|high-bandwidth — video, throughput first⟧",
                     "⟦일반 — 소포, 기본 보장만|standard — ordinary mail, basic guarantee only⟧",
                     "⟦한 차선 문제가 다른 차선에 안 번져요|trouble in one lane doesn't spread to another⟧"), 1.0))

# 5. 도로 용량 자체가 늘어난 건 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **CLERK) + label(190, 255, "⟦각자 보장된 몫으로 안전하게 달려요|each one runs safely within its guaranteed share⟧", 11, "var(--ink)")
         + truck(570, 180, 0.7) + '<path d="M548 160 l10 -20" stroke="var(--bad)" stroke-width="3"/>' + label(570, 250, "⟦도로 전체가 꽉 차면 차선도 같이 밀려요|if the whole road fills up, every lane slows together⟧", 11, "var(--ink)")
         + label(380, 282, "⟦나눈 건 차선일 뿐, 트럭과 길의 숫자는 그대로예요|only the lanes are split — the trucks and the road stay the same⟧", 12, "var(--ink)", cls="d"))

LANE_I = icon('<rect x="8" y="10" width="48" height="44" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><path d="M8 24 h48 M8 40 h48" stroke="var(--line)" stroke-width="2"/>')
GUAR_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 7 l13 -16" stroke="var(--good)" stroke-width="4" fill="none"/>')
ISOLATE_I = icon('<rect x="8" y="14" width="20" height="36" rx="3" fill="var(--bad)"/><rect x="36" y="14" width="20" height="36" rx="3" fill="var(--good)"/><path d="M32 14 v36" stroke="var(--ink)" stroke-width="3"/>')
PURPOSE_I = icon('<path d="M20 50 L32 14 L44 50 Z" fill="var(--accent)"/><circle cx="32" cy="38" r="5" fill="#fff"/>')

PAGE = {
    "slug": "5gslicing", "order": 5,
    "title": ("한 도로를 차선으로 나누기", "Splitting One Road Into Lanes"),
    "h1": ("<em>5G 네트워크 슬라이싱</em>이 뭐예요?", "What is <em>5G Network Slicing</em>?"),
    "sub": ("5G 네트워크 슬라이싱을, 한 도로에 전용 차선을 나눠 각자 보장된 속도로 달리게 하는 이야기로 풀어봤어요.",
            "5G network slicing, told as a story about splitting one road into dedicated lanes, each guaranteed its own speed."),
    "panels": [
        {"svg": P1, "alt": ("수술 로봇 신호 소포가 일반 소포들 뒤에 줄 서서 기다림", "A surgery-robot signal parcel waits in line behind ordinary parcels"),
         "caption": ("급한 소포도 일반 소포들 뒤에서 기다려요.", "Even the urgent parcel waits behind ordinary ones."),
         "small": ("같은 길을 다 같이 쓰다 보니 급한 것도 순서를 기다려요.", "Sharing one road means even the urgent one waits its turn.")},
        {"svg": P2, "alt": ("우체국장 둘이 전용 도로의 비용과 한 줄 세우기의 지연 사이에서 고민함", "Two postmasters weigh the cost of a dedicated road against the delay of one shared line"),
         "caption": ("길 하나를 모두를 위해 새로 깔 순 없어요.", "You can't lay a whole new road for everyone."),
         "small": ("한 도로, 서로 다른 급함 — 둘 다 만족시켜야 해요.", "One road, different urgencies — both have to be satisfied.")},
        {"svg": P3, "hero": True, "alt": ("같은 도로가 초저지연·대용량·일반 세 개의 색깔 차선으로 나뉨", "The same road split into three colored lanes: ultra-low-latency, high-bandwidth, and standard"),
         "caption": ("한 도로에 전용 차선을 나눠 각자 보장된 속도로 달려요.", "One road, split into lanes, each guaranteed its own speed."),
         "small": ("도로는 하나지만, 차선은 여러 개예요.", "One physical road, several logical lanes."),
         "tricks": (4, [
             (LANE_I, ("전용 차선 분리", "Lane separation"), ("용도마다 차선이 따로 있어요", "a separate lane for each purpose"), "calm"),
             (GUAR_I, ("보장된 속도", "Guaranteed performance"), ("각 차선의 속도·지연이 약속돼요", "speed and latency per lane are promised")),
             (ISOLATE_I, ("독립 운영", "Isolated operation"), ("한 차선 사고가 다른 차선에 안 번져요", "trouble in one lane doesn't spread"), "warm"),
             (PURPOSE_I, ("용도별 맞춤", "Purpose-built"), ("초저지연·대용량·일반 각각 달라요", "ultra-low-latency, high-bandwidth, standard — each tuned differently")),
         ])},
        {"svg": P4, "alt": ("세 차선 각각 무엇을 보장하는지 적은 안내판: 초저지연, 대용량, 일반", "A board listing what each lane guarantees: ultra-low-latency, high-bandwidth, standard"),
         "caption": ("슬라이스마다 보장하는 게 달라요.", "Each slice guarantees something different."),
         "small": ("초저지연은 수술 로봇, 대용량은 동영상, 일반은 소포에 맞춰요.", "Ultra-low-latency for surgery robots, high-bandwidth for video, standard for ordinary mail.")},
        {"svg": P5, "alt": ("왼쪽: 각 차선이 안전하게 보장된 몫으로 달림. 오른쪽: 도로 전체가 꽉 차면 차선도 함께 밀림", "Left: each lane runs safely within its guaranteed share. Right: when the whole road fills up, every lane slows"),
         "caption": ("도로 용량 자체가 늘어난 건 아니에요.", "The road's total capacity hasn't grown."),
         "small": ("나눈 건 차선일 뿐, 트럭과 길의 숫자는 그대로예요.", "Only the lanes are split — the trucks and the road stay the same.")},
    ],
    "summary": (("<b>5G 네트워크 슬라이싱</b>은 <b>하나의 물리 배송망을 여러 전용 차선(가상 망)으로 나눠</b>, 각 차선에 <b>보장된 성능</b>을 주는 기술이에요.",
                 "<b>5G network slicing</b> splits <b>one physical delivery network into several dedicated lanes (virtual networks)</b>, each given its own <b>guaranteed performance</b>."),
                ("네트워크 슬라이싱은 하나의 물리 5G 인프라 위에 여러 개의 논리적 가상 네트워크(슬라이스)를 만들어, 슬라이스마다 지연·대역폭·신뢰성 같은 품질(SLA)을 독립적으로 보장하는 기술이에요. 초저지연(URLLC), 대용량(eMBB), 대규모 연결(mMTC) 같은 서로 다른 용도를 같은 망에서 동시에 수용할 수 있어요.",
                 "Network slicing creates several logical virtual networks (slices) on top of one physical 5G infrastructure, each independently guaranteeing its own quality — latency, bandwidth, reliability (SLA). It lets very different use cases — ultra-reliable low latency (URLLC), high bandwidth (eMBB), massive connections (mMTC) — share the same network at once.")),
    "glossary": [
        ("네트워크 슬라이싱", "Network slicing", ("한 도로를 전용 차선으로 나누는 것.", "Splitting one road into dedicated lanes."), ("물리망은 하나, 차선은 여럿이에요.", "One physical network, several lanes.")),
        ("URLLC", "URLLC", ("초저지연 차선 — 수술 로봇용.", "The ultra-low-latency lane — for surgery robots."), ("지연을 최우선으로 보장해요.", "Guarantees latency above all else.")),
        ("eMBB", "eMBB", ("대용량 차선 — 동영상용.", "The high-bandwidth lane — for video."), ("속도(처리량)를 최우선으로 보장해요.", "Guarantees throughput above all else.")),
        ("mMTC", "mMTC", ("아주 많은 작은 소포가 동시에 오가는 차선.", "The lane where huge numbers of tiny parcels move at once."), ("센서처럼 많은 기기가 조금씩 보낼 때 써요.", "Used when many devices each send just a little, like sensors.")),
        ("5G 특화망", "5G Private Network", ("한 공장만을 위한 전용 배송망.", "A delivery network dedicated to one factory."), ('특화망 안에서도 슬라이스를 또 나눌 수 있어요. → <a href="5gprivate-ko.html">공장 전용 배송망</a>', 'A private network can be sliced further inside itself. → <a href="5gprivate-en.html">a delivery network just for one factory</a>')),
        ("SDN/NFV", "SDN/NFV", ("관제탑이 소프트웨어로 길을 바꾸는 기술.", "The technology letting a tower reroute roads in software."), ('슬라이싱은 이 기술 위에서 차선을 나눠요. → <a href="sdnnfv-ko.html">관제탑이 소프트웨어로 길을 바꾸는 법</a>', 'Slicing carves its lanes on top of this technology. → <a href="sdnnfv-en.html">a control tower rerouting roads in software</a>')),
        ("SLA", "SLA", ("차선마다 보장하는 약속.", "The promise each lane is bound to."), ("약속된 성능 수준을 명시해요.", "Spells out the guaranteed level of performance.")),
        ("혼잡 제어", "Congestion control", ("길이 막힐 때 트럭 수를 조절하는 장치.", "The device that adjusts truck count when the road is jammed."), ('도로 전체가 막히면 차선 보장도 흔들려요. → <a href="tcpcontrol-ko.html">세 가지 안전장치</a>', "Lane guarantees shake too once the whole road jams. → <a href=\"tcpcontrol-en.html\">the three safety devices</a>")),
    ],
}
