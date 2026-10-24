from _draw import *
from _world import *

# 1. 트럭이 앞차가 급정거하는 걸 못 보고 혼자 달림
P1 = svg(300, sky(300)
         + truck(200, 200, 1.0) + truck(460, 200, 1.0)
         + person(620, 180, s=0.6, face=EYES, **RECEIVER)
         + label(380, 40, "⟦앞 트럭이 급정거하는데 뒤 트럭은 몰라요|the truck ahead brakes hard, but the one behind has no idea⟧", 13, "var(--ink)")
         + label(380, 270, "⟦트럭은 자기 눈앞의 길만 보고 달려요|each truck only sees the road right in front of it⟧", 13, "var(--bad)"))

# 2. 신호등도, 사람도 트럭과 따로 놀아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + truck(220, 170, 0.9) + postoffice(400, 140, 0.45, "⟦신호등|signal⟧") + person(600, 180, s=0.6, face=FROWN, **RECEIVER)
         + label(380, 70, "⟦트럭·신호등·사람이 서로 아무 말도 안 해요|the truck, the signal, and the person all say nothing to each other⟧", 12, "var(--ink)")
         + label(380, 270, "⟦각자 따로 움직이다 보면 위험한 순간이 생겨요|moving independently like this creates dangerous moments⟧", 12, "var(--ink)"))

# 3. hero: V2X = 트럭이 다른 트럭·신호등·사람과 쪽지를 주고받는 것
P3 = svg(340, sky(340)
         + truck(180, 220, 0.9, fast=True) + truck(440, 220, 0.9, fast=True)
         + postoffice(620, 160, 0.5, "⟦신호등|signal⟧") + person(320, 150, s=0.55, face=EYES, **RECEIVER)
         + label(380, 30, "⟦V2X = 트럭이 다른 트럭·신호등·사람과 실시간으로 쪽지를 주고받는 것|V2X = trucks exchanging real-time notes with other trucks, signals, and people⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦'급정거해요!' 같은 쪽지가 눈 깜짝할 새 도착해요|a note like 'braking hard!' arrives in the blink of an eye⟧", 12, "var(--muted)"))

I1 = icon('<rect x="6" y="30" width="26" height="16" rx="3" fill="var(--accent)"/><rect x="34" y="30" width="24" height="16" rx="3" fill="var(--good)"/><path d="M32 38 h2" stroke="#142033" stroke-width="3"/>')
I2 = icon('<rect x="10" y="30" width="24" height="16" rx="3" fill="var(--accent)"/><rect x="42" y="18" width="12" height="28" rx="3" fill="var(--stone-dark)"/><circle cx="48" cy="24" r="4" fill="var(--bad)"/>')
I3 = icon('<rect x="10" y="30" width="24" height="16" rx="3" fill="var(--accent)"/><circle cx="48" cy="34" r="10" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>')
I4 = icon('<rect x="10" y="30" width="24" height="16" rx="3" fill="var(--accent)"/><rect x="42" y="26" width="12" height="20" rx="3" fill="var(--stone-dark)"/>')

# 4. V2X 네 종류 — 누구와 주고받는지
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦누구와 쪽지를 주고받나요|WHO DOES IT TALK TO⟧",
                    ("⟦V2V — 트럭끼리, 급정거·속도를 바로 공유해요|V2V — truck to truck, sharing braking and speed instantly⟧",
                     "⟦V2I — 신호등 같은 시설과, 신호 시간을 미리 알아요|V2I — truck to infrastructure like signals, knowing timing ahead⟧",
                     "⟦V2P — 보행자와, 가까이 오면 서로 알려줘요|V2P — truck to pedestrian, alerting each other when close⟧",
                     "⟦V2N — 우체국(통신망) 전체와, 더 멀리까지 정보를 받아요|V2N — truck to the whole network, reaching further for info⟧"), 1.0))

# 5. 한계: 모든 트럭·신호등이 이 쪽지를 쓸 수 있어야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + truck(150, 150, 0.8, fast=True) + truck(270, 150, 0.8, fast=True) + label(210, 240, "⟦둘 다 쪽지를 쓸 줄 알면 안전해져요|safer, once both can send and read the note⟧", 10, "var(--ink)")
         + truck(560, 150, 0.8) + person(660, 170, s=0.5, face=FROWN, **RECEIVER) + label(600, 250, "⟦한쪽이라도 못 쓰면 쪽지는 소용없어요|if even one side can't, the note is useless⟧", 10, "var(--ink)")
         + label(380, 40, "⟦고속도로처럼 고정 우체국이 멀면 트럭끼리 직접 길을 잇기도 해요|far from a fixed post office, like a highway, trucks may link directly instead⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "v2x", "order": 21,
    "title": ("트럭끼리 주고받는 쪽지", "The Note Trucks Pass to Each Other"),
    "h1": ("<em>V2X 차량 통신</em>이 뭐예요?", "What is <em>V2X</em> Vehicle Communication?"),
    "sub": ("V2X를, 트럭이 다른 트럭·신호등·사람과 실시간으로 쪽지를 주고받아 사고를 막는 이야기로 풀어봤어요.",
            "V2X, told as a story about trucks exchanging real-time notes with other trucks, signals, and people to avoid accidents."),
    "panels": [
        {"svg": P1, "alt": ("앞 트럭이 급정거하는데 뒤 트럭은 모른 채 달림", "The truck ahead brakes hard while the one behind drives on, unaware"),
         "caption": ("앞 트럭이 급정거하는데 뒤 트럭은 몰라요.", "The truck ahead brakes hard, but the one behind has no idea."),
         "small": ("트럭은 자기 눈앞의 길만 보고 달려요.", "Each truck only sees the road right in front of it.")},
        {"svg": P2, "alt": ("트럭, 신호등, 사람이 서로 아무 말 없이 따로 움직임", "A truck, a signal, and a person all move separately, saying nothing to each other"),
         "caption": ("신호등도, 사람도 트럭과 따로 놀아요.", "The signal and the person all move independently of the truck."),
         "small": ("각자 따로 움직이다 보면 위험한 순간이 생겨요.", "Moving independently like this creates dangerous moments.")},
        {"svg": P3, "hero": True, "alt": ("트럭 두 대가 신호등, 사람과 실시간으로 쪽지를 주고받음", "Two trucks exchange real-time notes with a signal and a pedestrian"),
         "caption": ("V2X = 트럭이 서로, 신호등·사람과 쪽지를 주고받는 거예요.", "V2X = trucks exchanging notes with each other, signals, and people."),
         "small": ("'급정거해요!' 같은 쪽지가 눈 깜짝할 새 도착해요.", "A note like 'braking hard!' arrives in the blink of an eye."),
         "tricks": (4, [
             (I1, ("V2V", "V2V"), ("트럭끼리 바로 공유", "truck to truck, instantly")),
             (I2, ("V2I", "V2I"), ("신호등 같은 시설과", "with signals and infrastructure"), "calm"),
             (I3, ("V2P", "V2P"), ("보행자와 서로 알림", "alerts with pedestrians"), "warm"),
             (I4, ("V2N", "V2N"), ("통신망 전체와", "with the whole network")),
         ])},
        {"svg": P4, "alt": ("누구와 쪽지를 주고받는지 보여주는 안내판: V2V, V2I, V2P, V2N 네 줄", "A guide board showing who V2X talks to: V2V, V2I, V2P, V2N"),
         "caption": ("상대에 따라 이름이 달라요.", "The name changes depending on who it talks to."),
         "small": ("트럭끼리, 시설과, 사람과, 망 전체와 — 네 방향이에요.", "Truck-to-truck, to infrastructure, to people, and to the whole network — four directions.")},
        {"svg": P5, "alt": ("왼쪽: 두 트럭이 모두 쪽지를 주고받을 수 있어 안전함. 오른쪽: 한쪽이 못 읽으면 쪽지가 소용없음", "Left: both trucks can exchange notes, safely. Right: if one can't read it, the note is useless"),
         "caption": ("모두가 이 쪽지를 쓸 수 있어야 해요.", "Everyone involved needs to be able to use this note."),
         "small": ("고정 우체국이 멀면 트럭끼리 직접 길을 잇기도 해요.", "Far from a fixed post office, trucks may link directly instead.")},
    ],
    "summary": (("<b>V2X</b> = 트럭(차량)이 다른 트럭·신호등·사람·통신망과 <b>실시간으로 쪽지를 주고받으며</b> 서로의 상황을 알려주는 통신.",
                 "<b>V2X</b> = vehicles exchanging <b>real-time notes</b> with other vehicles, traffic infrastructure, pedestrians, and the network to share what's happening."),
                ("V2X(Vehicle-to-Everything)는 차량이 다른 차량(V2V), 교통 인프라(V2I), 보행자(V2P), 통신망(V2N)과 직접 또는 망을 통해 저지연으로 정보를 주고받는 기술이에요. 급정거·신호 정보·보행자 위치 같은 데이터를 실시간 공유해 사고를 줄이는 데 쓰이고, 5G나 Ad-hoc 라우팅 같은 기반 기술 위에서 동작해요.",
                 "V2X (Vehicle-to-Everything) lets vehicles exchange low-latency information with other vehicles (V2V), traffic infrastructure (V2I), pedestrians (V2P), and the network (V2N), either directly or via a network. It shares data like hard braking, signal timing, and pedestrian location in real time to reduce accidents, and runs on top of underlying technologies like 5G or ad-hoc routing.")),
    "glossary": [
        ("V2V", "V2V", ("트럭끼리 바로 주고받는 쪽지.", "The note trucks pass directly to each other."), ("급정거·속도 정보를 공유해요.", "Shares braking and speed information.")),
        ("V2I", "V2I", ("신호등 같은 시설과 주고받는 쪽지.", "The note exchanged with infrastructure like signals."), ("신호 타이밍을 미리 알 수 있어요.", "Lets a vehicle know signal timing in advance.")),
        ("V2P", "V2P", ("보행자와 주고받는 쪽지.", "The note exchanged with a pedestrian."), ("가까이 오면 서로 알려줘요.", "Alerts both sides when they get close.")),
        ("V2N", "V2N", ("통신망 전체와 주고받는 쪽지.", "The note exchanged with the whole network."), ("더 멀리까지 정보를 받을 수 있어요.", "Reaches further for information.")),
        ("저지연(URLLC)", "Low Latency (URLLC)", ("응급 전용 즉시 차선.", "The instant lane reserved for emergencies."), ('V2X가 기대는 5G의 핵심 기술이에요. → <a href="5gcore-ko.html">상황별 전용 차선을 가진 배송망</a>', 'A core 5G technology that V2X relies on. → <a href="5gcore-en.html">the network with a lane for every need</a>')),
        ("Ad-hoc 라우팅", "Ad-hoc Routing", ("고정 우체국 없이 서로 길을 찾는 법.", "Finding the way among themselves, with no fixed post office."), ('고정망이 먼 곳에서 트럭끼리 길을 잇는 방식이에요. → <a href="adhocrouting-ko.html">집배원끼리 길을 찾아 전달하는 법</a>', "How trucks link up directly, far from fixed infrastructure. → <a href=\"adhocrouting-en.html\">how carriers find the way among themselves</a>")),
        ("AMI(지능형 검침)", "AMI", ("계량기가 자동으로 값을 보고하는 망.", "The network where meters report readings automatically."), ('비슷하게 사물끼리 자동으로 소식을 주고받는 예시예요. → <a href="ami-ko.html">계량기가 자동으로 편지를 보내는 망</a>', 'A similar example of things auto-reporting to each other. → <a href="ami-en.html">the network where meters mail their own readings</a>')),
        ("자율주행 센서", "Autonomous Sensors", ("트럭 스스로 눈앞의 길만 보는 장치.", "The device by which a truck sees only the road right ahead."), ("V2X는 이 눈이 못 보는 곳까지 알려주는 보완재예요.", "V2X complements this by covering what the truck's own eyes can't see.")),
    ],
}
