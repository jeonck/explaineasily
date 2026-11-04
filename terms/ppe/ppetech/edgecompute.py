from _draw import *
from _world import *


def cloudbox(x, y, s=1.0, far=True):
    """멀리 있는 중앙 서버(구름 모양)."""
    label_txt = "⟦저 멀리 중앙 서버|the far-away central server⟧" if far else "⟦중앙 서버|central server⟧"
    out = (f'<g transform="translate({x},{y}) scale({s})">'
           f'<ellipse rx="56" ry="30" fill="#8FA6C7"/><ellipse cx="-34" cy="6" rx="30" ry="20" fill="#8FA6C7"/>'
           f'<ellipse cx="34" cy="6" rx="30" ry="20" fill="#8FA6C7"/><rect x="-24" y="-8" width="48" height="24" rx="3" fill="#1B2A44"/></g>')
    return out + label(x, y + 56, label_txt, 11, "var(--muted)")


def smallserver(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-24" width="40" height="48" rx="4" fill="#5B8DEF"/><circle cx="0" cy="-10" r="4" fill="#fff"/><circle cx="0" cy="4" r="4" fill="#fff"/></g>'


def car(x, y, s=1.0, cone_hit=False):
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-34" y="-14" width="68" height="28" rx="8" fill="var(--accent)"/>'
           f'<rect x="-18" y="-28" width="36" height="18" rx="6" fill="#2E3D57"/><circle cx="-20" cy="16" r="9" fill="#142033"/><circle cx="20" cy="16" r="9" fill="#142033"/></g>')
    if cone_hit:
        out += f'<path d="M{x + 40} {y + 14} l10 -26 l10 26 z" fill="var(--bad)" transform="rotate(25 {x+50} {y})"/>'
    return out


def sensorline(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>'


# 1. 중앙 서버까지 왕복하느라 반응이 느려요
P1 = svg(320, sky(320, ground=False)
         + booth(60, 60, 280, 220, 1.0, "var(--accent)", "⟦엣지 컴퓨팅 부스|Edge Computing Booth⟧")
         + car(170, 200, 1.0) + cloudbox(560, 110, 1.0)
         + sensorline(230, 190, 505, 130)
         + label(430, 62, "⟦모형 자율주행차 시연|a toy self-driving car demo⟧", 13, "var(--ink)")
         + label(380, 302, "⟦신호가 서버까지 왕복하는 동안 차는 이미 지나가버려요|by the time the signal reaches the server and returns, the car has driven on⟧", 12, "var(--bad)"))


# 2. 멀수록 느려요, 그래서 위험해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + car(150, 190, 1.0, cone_hit=True)
         + cloudbox(600, 90, 0.9)
         + sensorline(220, 180, 560, 110)
         + label(380, 60, "⟦'장애물이에요!' → 서버까지 갔다 돌아오는 사이 이미 부딪혔어요|'Obstacle!' — by the server's reply, the car has already crashed⟧", 12, "var(--bad)")
         + person(620, 190, s=0.65, face=SWEAT + EYES, **DEMO)
         + label(250, 280, "⟦데이터를 멀리 보낼수록 차의 판단이 늦어요|the farther data travels, the later the car decides⟧", 13, "var(--ink)"))

# 3. 엣지 컴퓨팅 = 가까이서 바로 계산 (hero)
P3 = svg(340, sky(340, ground=False)
         + car(170, 180, 1.1)
         + smallserver(300, 150, 1.2)
         + sensorline(220, 175, 290, 155)
         + label(300, 210, "⟦바로 옆, 엣지 서버|right next door, the edge server⟧", 11, "var(--muted)")
         + cloudbox(640, 80, 0.6, far=True)
         + label(380, 30, "⟦엣지 컴퓨팅 = 데이터를 멀리 안 보내고 기기 가까이서 계산하는 것|Edge Computing = computing right near the device, not on a far-away server⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦'장애물이에요!' → 바로 옆 엣지 서버가 즉시 판단해요|'Obstacle!' — the edge server next door decides instantly⟧", 12, "var(--muted)"))

EDGE_FAST = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 4" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M48 16 l6 -6 M48 48 l6 6" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')
EDGE_TRAFFIC = icon('<path d="M10 44 q22 -28 44 0" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M10 44 q22 -10 44 0" stroke="var(--line)" stroke-width="3" fill="none" stroke-dasharray="3 3"/>')
EDGE_OFFLINE = icon('<rect x="14" y="10" width="36" height="44" rx="4" fill="#1B2A44"/><path d="M24 44 l16 -28" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M40 44 l-16 -28" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
EDGE_PRIVACY = icon('<path d="M32 10 l20 8 v14 c0 14 -9 22 -20 28 c-11 -6 -20 -14 -20 -28 v-14z" fill="var(--good)"/><rect x="24" y="30" width="16" height="14" rx="3" fill="#fff"/>')

# 4. 중앙 서버 vs 엣지, 뭐가 빠른가
P4 = svg(320, sky(320, ground=False)
         + infoboard(60, 40, 300, 240, "⟦저 멀리 중앙 서버|CENTRAL SERVER⟧",
                     ("⟦왕복 지연 큼|big round-trip delay⟧", "⟦트래픽 많음|heavy network traffic⟧",
                      "⟦네트워크가 끊기면 못 씀|unusable if offline⟧", "⟦많은 데이터 분석엔 강함|great for huge-data analysis⟧"), 1.0)
         + infoboard(400, 40, 300, 240, "⟦바로 옆 엣지 서버|NEARBY EDGE SERVER⟧",
                     ("⟦즉시 반응|instant response⟧", "⟦트래픽 적음|light network traffic⟧",
                      "⟦네트워크가 끊겨도 동작|keeps working offline⟧", "⟦작은 즉시 판단엔 강함|great for quick local decisions⟧"), 1.0, hl=0)
         + label(380, 300, "⟦급한 판단은 엣지 서버에서, 큰 분석은 멀리 중앙 서버에서 해도 돼요|urgent decisions stay on the edge server; heavy analysis can go to the central server⟧", 12, "var(--ink)"))

# 5. 한계: 엣지 서버는 힘이 약해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + smallserver(150, 150, 1.4) + label(150, 230, "⟦엣지 서버: 빠르지만 계산 힘이 약해요|edge server: fast, less computing power⟧", 11, "var(--ink)")
         + cloudbox(600, 140, 1.1) + label(600, 230, "⟦중앙 서버: 응답은 느려도 계산 힘이 세요|central server: slower replies, more power⟧", 11, "var(--ink)")
         + label(380, 280, "⟦스마트팩토리·자율주행은 엣지와 중앙 서버를 같이 써요|Smart factories and self-driving cars use edge and central servers together⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "edgecompute", "order": 2,
    "title": ("바로 옆에서 계산하는 작은 서버", "The Small Server That Computes Right Next Door"),
    "h1": ("<em>엣지 컴퓨팅</em>이 뭐예요?", "What is <em>Edge Computing</em>?"),
    "sub": ("엣지 컴퓨팅을, 멀리 있는 중앙 서버 대신 기기 바로 옆에서 즉시 판단하는 작은 서버 이야기로 풀어봤어요.",
            "Edge computing, told as a story about a small server that decides instantly, right next to the device, instead of sending everything far away."),
    "panels": [
        {"svg": P1, "alt": ("모형 자율주행차가 저 멀리 중앙 서버로 신호를 보내는 시연", "A toy self-driving car sends a signal all the way to a far-away central server"),
         "caption": ("신호가 서버까지 왕복하는 동안 차는 이미 지나가버려요.", "By the time the signal reaches the server and returns, the car has driven on."),
         "small": ("중앙 서버까지 갔다 오는 거리 자체가 지연이에요.", "The round trip to the central server is itself the delay.")},
        {"svg": P2, "alt": ("장난감 차가 장애물에 부딪힘, 서버 응답이 늦었기 때문", "The toy car crashes into an obstacle because the server's reply came too late"),
         "caption": ("데이터를 멀리 보낼수록 차의 판단이 늦어요.", "The farther data travels, the later the car decides."),
         "small": ("서버까지 왕복하는 지연은 자율주행·공장 로봇처럼 급한 판단엔 치명적이에요.", "A round-trip delay to the server is fatal for urgent decisions in self-driving cars or factory robots.")},
        {"svg": P3, "hero": True, "alt": ("차 바로 옆에 작은 엣지 서버가 있어 즉시 반응함", "A small edge server sits right next to the car and reacts instantly"),
         "caption": ("엣지 컴퓨팅은 데이터를 멀리 안 보내고 기기 바로 가까이서 계산하는 거예요.", "Edge computing means computing right near the device instead of sending data far away."),
         "small": ("'장애물이에요!' — 바로 옆 엣지 서버가 즉시 판단해요.", "'Obstacle!' — the edge server next door decides instantly."),
         "tricks": (4, [
             (EDGE_FAST, ("즉시 판단하기", "Decide instantly"), ("왕복 거리가 아주 짧아요", "the round trip is very short"), "calm"),
             (EDGE_TRAFFIC, ("트래픽 줄이기", "Cut network traffic"), ("데이터를 다 보낼 필요 없어요", "no need to send all the data")),
             (EDGE_OFFLINE, ("끊겨도 동작하기", "Keep working offline"), ("기기 근처에서 계속 돌아가요", "keeps running locally")),
             (EDGE_PRIVACY, ("민감 정보는 가까이에", "Keep sensitive data close"), ("멀리 안 보내도 돼요", "no need to ship it far"), "warm"),
         ])},
        {"svg": P4, "alt": ("중앙 서버와 엣지 서버를 비교하는 설명판: 지연·트래픽·오프라인·분석력", "A board comparing central and edge servers: latency, traffic, offline use, analysis power"),
         "caption": ("급한 판단은 엣지 서버에서, 큰 분석은 멀리 중앙 서버에서 해도 돼요.", "Urgent decisions stay on the edge server; heavy analysis can go to the central server."),
         "small": ("중앙 서버와 엣지 서버는 잘하는 일이 서로 달라요.", "Central and edge servers are each good at different jobs.")},
        {"svg": P5, "alt": ("왼쪽: 작고 빠른 엣지 서버. 오른쪽: 크고 느리지만 힘센 중앙 서버", "Left: a small, fast edge server. Right: a big, slow but powerful central server"),
         "caption": ("엣지 서버는 응답이 빠르지만 계산 힘은 중앙 서버보다 약해요.", "The edge server replies fast, but has less computing power than a central server."),
         "small": ("그래서 스마트팩토리·자율주행은 엣지와 중앙 서버를 함께 써요.", "So smart factories and self-driving cars use edge and central servers together.")},
    ],
    "summary": (("<b>엣지 컴퓨팅</b>은 데이터를 멀리 보내지 않고 <b>기기 바로 가까이서 즉시 계산</b>해, 반응을 빠르게 하고 네트워크가 끊겨도 기기가 동작하게 하는 방식이에요.",
                 "<b>Edge computing</b> means computing <b>right near the device</b> instead of sending data far away, so replies come fast and the device keeps working offline."),
                ("엣지 컴퓨팅은 데이터 발생 지점(기기·IoT 센서) 가까이에 연산 자원을 두어 지연시간을 줄이고 네트워크 부하를 낮추는 분산 컴퓨팅 방식이에요. 작은 엣지 서버는 즉시성이 필요한 국지적 판단에 강하고, 대규모 학습·장기 데이터 분석은 여전히 중앙(클라우드) 자원이 맡아요.",
                 "Edge computing is a distributed computing approach that places compute resources close to where data is generated (devices, IoT sensors), cutting latency and network load. Small edge nodes excel at local decisions needing immediate response, while large-scale training and long-term analysis still belong to central (cloud) resources.")),
    "glossary": [
        ("엣지 컴퓨팅", "Edge Computing", ("기기 바로 옆에서 계산하는 것.", "Computing right next to the device."), ("왕복 지연을 크게 줄여요.", "Greatly cuts the round-trip delay.")),
        ("디지털 트윈", "Digital Twin", ("실시간 센서로 움직이는 화면 속 쌍둥이.", "The on-screen twin, moved by live sensor data."), ('그 센서 데이터를 빠르게 처리하는 게 엣지예요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "Edge is what processes that sensor data fast. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
        ("스마트팩토리", "Smart Factory", ("센서·로봇·엣지가 함께 일하는 공장.", "A factory where sensors, robots, and edge nodes work together."), ('엣지 컴퓨팅이 실제로 쓰이는 현장이에요. → <a href="smartfactory-ko.html">스마트팩토리 부스</a>', 'Where edge computing is actually put to work. → <a href="smartfactory-en.html">the Smart Factory booth</a>')),
        ("MEC(모바일 엣지 컴퓨팅)", "MEC", ("통신사 기지국 옆에 두는 엣지.", "The edge node placed right by a carrier's base station."), ('기기 엣지와는 다른, 통신망 안의 엣지예요. → <a href="mec-ko.html">MEC 부스</a>', "A different kind of edge, inside the carrier's network. → <a href=\"mec-en.html\">the MEC booth</a>")),
        ("지연시간(latency)", "Latency", ("신호가 왕복하는 데 걸리는 시간.", "How long a signal's round trip takes."), ("엣지는 이 시간을 크게 줄여요.", "Edge computing greatly cuts it.")),
        ("클라우드 컴퓨팅", "Cloud Computing", ("크고 힘센 저 멀리 중앙 서버.", "The big, powerful, far-away central server."), ("대규모 분석은 여전히 여기서 해요.", "Large-scale analysis still happens here.")),
        ("IoT 센서", "IoT Sensor", ("엣지 서버에 정보를 주는 기기.", "The device feeding the edge server."), ("IoT 센서는 엣지 서버 가까이에 있어요.", "It sits close to the edge server.")),
        ("자율주행", "Self-Driving", ("즉시 판단이 생명인 대표 사례.", "A prime example where instant decisions matter most."), ("판단이 늦으면 위험해서, 차 안이나 가까이에서 계산해요.", "A late decision is dangerous, so computing happens in or near the car.")),
    ],
}
