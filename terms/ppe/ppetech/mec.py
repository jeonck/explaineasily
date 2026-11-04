from _draw import *
from _world import *


def tower(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0 60 L-10 -30 M0 60 L10 -30 M-6 20 L6 20 M-8 0 L8 0" stroke="#5A6B85" stroke-width="4" fill="none"/>'
            f'<rect x="-18" y="-40" width="36" height="12" rx="3" fill="#2E3D57"/></g>')


def phone(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-30" width="32" height="56" rx="6" fill="#2E3D57"/><rect x="-12" y="-24" width="24" height="40" rx="2" fill="#5B8DEF"/></g>'


def farserver(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="56" ry="30" fill="#8FA6C7"/><ellipse cx="-34" cy="6" rx="30" ry="20" fill="#8FA6C7"/>'
            f'<ellipse cx="34" cy="6" rx="30" ry="20" fill="#8FA6C7"/><rect x="-24" y="-8" width="48" height="24" rx="3" fill="#1B2A44"/></g>')


def edgebox(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-24" width="40" height="48" rx="4" fill="#5B8DEF"/><circle cy="-10" r="4" fill="#fff"/><circle cy="4" r="4" fill="#fff"/></g>'


def sensorline(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>'


def smallserver(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-24" width="40" height="48" rx="4" fill="#5B8DEF"/><circle cy="-10" r="4" fill="#fff"/><circle cy="4" r="4" fill="#fff"/></g>'


# 1. 중앙 데이터센터까지 왕복하느라 AR 게임이 느려요
P1 = svg(300, sky(300, ground=False)
         + phone(170, 190, 1.4) + farserver(560, 110, 1.0)
         + sensorline(220, 180, 505, 130)
         + label(380, 280, "⟦AR 게임 캐릭터가 한 박자 늦게 움직여요|the AR game character moves a beat late⟧", 12, "var(--bad)"))


# 2. 거리 자체가 지연이에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + phone(130, 180, 1.2) + tower(260, 170, 1.0) + farserver(640, 100, 1.0)
         + sensorline(170, 170, 250, 160) + sensorline(290, 150, 580, 110)
         + label(380, 252, "⟦휴대폰 → 기지국까지는 가까운데, 기지국 → 중앙 데이터센터는 멀어요|phone to tower is close, but tower to central datacenter is far⟧", 12, "var(--ink)")
         + label(380, 282, "⟦기지국~중앙 데이터센터의 먼 구간이 지연을 만들어요|the long stretch from tower to datacenter creates the delay⟧", 11, "var(--muted)"))

# 3. MEC = 기지국 바로 옆에 작은 서버 (hero)
P3 = svg(340, sky(340, ground=False)
         + phone(170, 200, 1.3) + tower(300, 180, 1.1) + edgebox(300, 90, 1.2)
         + sensorline(220, 190, 285, 110)
         + farserver(640, 80, 0.6)
         + label(440, 95, "⟦기지국 옆 작은 서버|a small server right by the tower⟧", 12, "var(--ink)")
         + label(380, 30, "⟦MEC = 기지국 바로 옆(통신망 가장자리)에 서버를 둬서 휴대폰 요청을 가까이서 처리|MEC = a server right by the base station, handling phone requests nearby⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦서버가 가까우니 AR 게임 캐릭터가 더 빨리 반응해요|the server is close, so the AR character reacts faster⟧", 12, "var(--muted)"))

MEC_NEAR = icon('<path d="M20 44 V24 M32 44 V14 M44 44 V30" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
MEC_LAT = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 4" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
MEC_5G = icon('<text x="32" y="40" text-anchor="middle" font-size="22" font-weight="700" fill="var(--accent)">5G</text><path d="M14 20 q18 -14 36 0" stroke="var(--accent)" stroke-width="3" fill="none"/>')
MEC_AR = icon('<rect x="14" y="20" width="36" height="24" rx="4" fill="#1B2A44"/><path d="M22 32 l6 -8 l6 6 l6 -10 l8 12" stroke="var(--accent)" stroke-width="2.5" fill="none"/>')

# 4. 거리별 지연 비교
P4 = svg(320, sky(320, ground=False)
         + infoboard(60, 40, 300, 240, "⟦중앙 데이터센터까지|TO CENTRAL DATACENTER⟧",
                     ("⟦거리 — 수백 km|distance — hundreds of km⟧", "⟦지연 — 수십~백 ms|latency — tens to 100+ ms⟧",
                      "⟦AR·클라우드 게임엔 너무 느려요|too slow for AR / cloud gaming⟧"), 1.0)
         + infoboard(400, 40, 300, 240, "⟦기지국 엣지 서버까지|TO MEC NODE AT THE TOWER⟧",
                     ("⟦거리 — 기지국 옆~가까운 통신사 거점|distance — at the tower or a nearby carrier site⟧", "⟦지연 — 대략 12~30 ms|latency — roughly 12–30 ms⟧",
                      "⟦실시간 반응이 가능해요|real-time response becomes possible⟧"), 1.0, hl=1)
         + label(380, 300, "⟦MEC를 5G와 함께 쓰면 전체 지연이 더 줄어요|using MEC with 5G cuts total delay even further⟧", 12, "var(--ink)"))

# 5. 한계: 기기 엣지와는 다른, 통신망 안의 엣지예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + edgebox(190, 150, 1.3) + label(190, 230, "⟦MEC — 통신사 기지국 옆|MEC — beside the carrier's tower⟧", 11, "var(--ink)")
         + smallserver(570, 150, 1.3) + label(570, 230, "⟦엣지 컴퓨팅 — 데이터가 생기는 곳 가까이|edge computing — close to where data is made⟧", 11, "var(--ink)")
         + label(380, 280, "⟦MEC는 엣지 컴퓨팅 중에서 서버를 통신사 기지국 쪽에 두는 방식이에요|MEC is one kind of edge computing: the server sits at the carrier's tower⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "mec", "order": 9,
    "title": ("기지국 옆에 붙은 작은 서버", "The Small Server Perched by the Tower"),
    "h1": ("<em>모바일 엣지 컴퓨팅(MEC)</em>이 뭐예요?", "What is <em>Mobile Edge Computing (MEC)</em>?"),
    "sub": ("MEC(요즘은 Multi-access Edge Computing이라고도 해요)를, 멀리 떨어진 중앙 데이터센터 대신 기지국 바로 옆에서 휴대폰 요청을 처리하는 이야기로 풀어봤어요.",
            "MEC (these days also called Multi-access Edge Computing), told as a story about a server that handles phone requests right by the tower, instead of a far-away central datacenter."),
    "panels": [
        {"svg": P1, "alt": ("휴대폰이 멀리 있는 중앙 데이터센터로 신호를 보내고, AR 게임 캐릭터가 늦게 움직임", "A phone sends a signal all the way to a far central datacenter, and the AR game character moves late"),
         "caption": ("AR 게임 캐릭터가 한 박자 늦게 움직여요.", "The AR game character moves a beat late."),
         "small": ("중앙 데이터센터까지 왕복하느라 반응이 느려요.", "The round trip to the central datacenter slows the response.")},
        {"svg": P2, "alt": ("휴대폰-기지국은 가깝지만 기지국-중앙 데이터센터는 멀다는 걸 보여줌", "Phone-to-tower is close, but tower-to-central-datacenter is far"),
         "caption": ("휴대폰에서 기지국까지는 가까운데, 그 뒤 중앙 데이터센터까지는 멀어요.", "Phone to tower is close, but tower to central datacenter is far."),
         "small": ("기지국에서 중앙 데이터센터까지의 먼 구간이 지연을 만들어요.", "The long stretch from tower to central datacenter creates the delay.")},
        {"svg": P3, "hero": True, "alt": ("기지국 바로 옆에 작은 서버가 놓여 휴대폰 요청을 가까이서 처리함", "A small server sits right by the tower, handling phone requests nearby"),
         "caption": ("MEC는 기지국 바로 옆에 서버를 둬서 휴대폰 요청을 가까이서 처리해요.", "MEC places a server right by the base station to handle phone requests nearby."),
         "small": ("서버가 가까우니 AR 게임 캐릭터가 더 빨리 반응해요.", "The server is close, so the AR game character reacts faster."),
         "tricks": (4, [
             (MEC_NEAR, ("기지국 옆에 배치", "Placed by the base station"), ("통신망 가장자리예요", "right at the network's edge"), "calm"),
             (MEC_LAT, ("저지연 응답", "Low latency"), ("중앙 데이터센터보다 왕복이 짧아요", "a shorter round trip than a central datacenter")),
             (MEC_5G, ("5G와 함께 사용", "Paired with 5G"), ("5G의 빠른 무선 구간이 지연을 더 줄여요", "5G's fast radio link cuts delay further")),
             (MEC_AR, ("영상·AR 계산 대신 해주기", "Offload video/AR processing"), ("휴대폰이 계산을 덜 해서 배터리도 아껴요", "the phone computes less, saving battery too"), "warm"),
         ])},
        {"svg": P4, "alt": ("중앙 데이터센터와 MEC 노드까지의 거리·지연을 비교하는 설명판", "Boards comparing distance and latency to the central datacenter vs the MEC node"),
         "caption": ("서버까지 거리가 짧아질수록 지연도 크게 줄어요.", "The shorter the distance to the server, the lower the latency."),
         "small": ("MEC를 5G와 함께 쓰면 전체 지연이 더 줄어요.", "Using MEC with 5G cuts total delay even further.")},
        {"svg": P5, "alt": ("왼쪽: MEC는 통신사 기지국 옆에. 오른쪽: 엣지 컴퓨팅은 데이터가 생기는 곳 가까이에", "Left: MEC sits beside the carrier's tower. Right: edge computing sits close to where data is made"),
         "caption": ("MEC는 엣지 컴퓨팅 중에서 서버를 통신사 기지국 옆에 두는 방식이에요.", "MEC is the kind of edge computing that puts the server beside the carrier's tower."),
         "small": ("둘 다 '가까이서 계산'이지만, 서버를 어디에 두느냐가 달라요.", "Both mean 'compute nearby' — but the server sits in a different place.")},
    ],
    "summary": (("<b>MEC(모바일 엣지 컴퓨팅)</b>는 통신사 <b>기지국 바로 옆</b>에 서버를 두어, 휴대폰 요청을 중앙 데이터센터까지 보내지 않고 <b>가까이서 더 짧은 지연으로</b> 처리해요.",
                 "<b>Mobile Edge Computing (MEC)</b> places a server <b>right by the carrier's base station</b>, so phone requests are handled <b>nearby, with lower latency</b>, instead of traveling to a central datacenter."),
                ("MEC는 이동통신망의 무선 접속망(RAN) 기지국 근처나 가까운 통신사 거점에 컴퓨팅·스토리지 자원을 배치해, 모바일 애플리케이션의 지연시간을 중앙 데이터센터보다 크게 줄이는 기술이에요. 한 통신사(Vodafone)가 2021년에 밝힌 단말~MEC 왕복 지연은 대략 12~30 ms예요. 5G와 결합해 AR/VR, 차량 통신(V2X), 실시간 영상분석 같은 저지연 서비스를 뒷받침해요. 엣지 컴퓨팅은 기기 안이나 현장 서버까지 넓게 가리키는 말이고, MEC는 그중 통신사 네트워크 안의 엣지예요.",
                 "MEC places compute and storage resources near the base stations of the mobile radio access network (RAN) or at a nearby carrier site, cutting mobile application latency well below a central datacenter's. In 2021, one carrier (Vodafone) put the device-to-MEC round trip at about 12–30 ms. Combined with 5G, it supports low-latency services like AR/VR, vehicle communication (V2X), and real-time video analytics. Edge computing broadly covers on-device and on-site servers too; MEC is the part of it inside the carrier's own network.")),
    "glossary": [
        ("모바일 엣지 컴퓨팅(MEC)", "MEC", ("기지국 옆에 둔 작은 서버.", "A small server placed beside the base station."), ("통신망 안의 엣지예요.", "The edge, inside the carrier's network.")),
        ("엣지 컴퓨팅", "Edge Computing", ("내 기기 바로 옆에서 계산하는 것.", "Computing right beside my own device."), ('MEC는 이 개념을 통신망에 적용한 거예요. → <a href="edgecompute-ko.html">엣지 컴퓨팅 부스</a>', "MEC applies this idea inside the carrier network. → <a href=\"edgecompute-en.html\">the Edge Computing booth</a>")),
        ("지연시간(latency)", "Latency", ("신호가 왕복하는 데 걸리는 시간.", "How long a signal's round trip takes."), ("MEC는 중앙 데이터센터보다 왕복 시간을 크게 줄여요.", "MEC makes the round trip much shorter than to a central datacenter.")),
        ("5G", "5G", ("MEC와 짝을 이루는 통신 기술.", "The network tech that pairs with MEC."), ("MEC와 5G가 함께 저지연 서비스를 만들어요.", "MEC and 5G together enable low-latency services.")),
        ("기지국(RAN)", "Base Station / RAN", ("휴대폰과 가장 먼저 연결되는 통신 설비.", "The first piece of network gear a phone connects to."), ("기지국이 모인 무선 구간을 RAN이라 해요. MEC 서버는 그 근처에 있어요.", "The radio network of base stations is the RAN. The MEC server sits near it.")),
        ("자율주행", "Self-Driving", ("짧은 지연이 중요한 대표 사례.", "A case where short delay really matters."), ("급한 판단은 차 안 컴퓨터가 맡고, MEC는 차량 간 정보 공유(V2X)를 거들어요.", "The car's own computer makes urgent decisions; MEC helps share road data between vehicles (V2X).")),
        ("클라우드 컴퓨팅", "Cloud Computing", ("멀리 있는 중앙 데이터센터.", "The far-away central datacenter."), ("큰 분석은 여전히 여기서 해요.", "Large-scale analysis still happens here.")),
        ("디지털 트윈", "Digital Twin", ("실시간 데이터로 움직이는 화면 속 쌍둥이.", "The on-screen twin, moved by live data."), ('MEC의 저지연이 트윈 갱신에도 쓰여요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "MEC's low latency also helps keep twins in sync. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
    ],
}
