from _draw import *
from _world import *


def robot(x, y, s=1.0, broken=False):
    """작은 로봇팔. broken=True 면 금 간 표시."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-10" y="20" width="20" height="40" rx="4" fill="#5A6B85"/>'
           f'<circle cy="10" r="14" fill="#7B8CA6"/><rect x="-34" y="-6" width="30" height="12" rx="6" fill="#5A6B85" transform="rotate(-20)"/>')
    if broken:
        out += '<path d="M-6 -4 l6 10 l-4 6 l8 10" stroke="var(--bad)" stroke-width="3" fill="none"/>'
    return out + '</g>'


def sensorline(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>'


# 1. 전시장 입구 + 첫 부스: 진짜 로봇은 함부로 못 건드려요
P1 = svg(320, sky(320)
         + ribbon(130, 50, 1.1, "⟦미래 과학관 전시장|Future Science Expo Hall⟧")
         + person(90, 170, s=0.85, face=SMILE, **GUIDE)
         + bubble(10, 90, 190, 46, "⟦부스를 하나씩 돌며 신기술을 만나볼까요?|Shall we meet new tech, booth by booth?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + booth(470, 70, 250, 200, 1.0, "var(--accent)", "⟦첫 번째 부스: 디지털 트윈|Booth 1: Digital Twin⟧")
         + robot(600, 190, 1.0) + label(600, 250, "⟦진짜 로봇 — 함부로 못 건드려요|the real robot — can't just poke it⟧", 11, "var(--muted)")
         + label(380, 300, "⟦오늘 첫 부스는 디지털 트윈이에요|Today's first booth is Digital Twin⟧", 13, "var(--ink)"))

# 2. 진짜 기계로 실험하면 큰일나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + robot(560, 150, 1.3, broken=True)
         + person(300, 160, s=0.85, face=SWEAT + EYES, **DEMO)
         + bubble(70, 70, 230, 46, "⟦이 설정으로 테스트해볼까요…|Let's just test this setting…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(560, 240, "⟦수리비가 얼마나 나올지 몰라요!|No idea how big the repair bill will be!⟧", 12, "var(--bad)")
         + label(380, 280, "⟦진짜 기계로 함부로 실험하면 큰일나요|Experimenting on the real machine is risky⟧", 13, "var(--ink)"))

# 3. 디지털 트윈 = 화면 속 쌍둥이 (hero)
P3 = svg(340, sky(340, ground=False)
         + robot(220, 140, 1.1)
         + screen(500, 100, 1.5, robot(60, 10, 0.5))
         + sensorline(290, 150, 500, 150) + sensorline(290, 170, 500, 180)
         + label(220, 260, "⟦진짜 로봇|the real robot⟧", 12, "var(--ink)")
         + label(640, 260, "⟦화면 속 쌍둥이|its twin on screen⟧", 12, "var(--ink)")
         + label(380, 30, "⟦디지털 트윈 = 진짜 기계를 그대로 빼닮은 화면 속 쌍둥이|Digital Twin = a look-alike twin of the real machine, living on a screen⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦센서 데이터로 진짜와 똑같이 움직여요|Sensor data makes it move exactly like the real one⟧", 12, "var(--muted)"))

TWIN_SYNC = icon('<circle cx="18" cy="32" r="12" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="46" cy="32" r="12" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M30 32 h4" stroke="var(--accent)" stroke-width="4" stroke-dasharray="3 3"/>')
TWIN_TEST = icon('<rect x="12" y="14" width="40" height="30" rx="3" fill="#1B2A44"/><path d="M22 28 l8 8 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
TWIN_PREDICT = icon('<path d="M12 44 q10 -28 20 -10 q10 18 20 -24" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="52" cy="10" r="4" fill="var(--bad)"/>')
TWIN_LOG = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h20" stroke="#142033" stroke-width="2.5"/>')

# 4. 진짜 로봇 vs 디지털 트윈 비교
P4 = svg(320, sky(320, ground=False)
         + infoboard(60, 40, 300, 240, "⟦진짜 로봇|REAL ROBOT⟧",
                     ("⟦위험한 테스트 ✕|risky tests ✕⟧", "⟦수리비 큼|big repair bills⟧",
                      "⟦한 번에 하나씩|one try at a time⟧", "⟦지금 상태만 보임|shows only right now⟧"), 1.0)
         + infoboard(400, 40, 300, 240, "⟦디지털 트윈|DIGITAL TWIN⟧",
                     ("⟦위험한 테스트 ✓|risky tests ✓⟧", "⟦거의 공짜|almost free⟧",
                      "⟦수백 번도 반복|try it hundreds of times⟧", "⟦기록도 계속 쌓여요|keeps a running history⟧"), 1.0)
         + label(380, 300, "⟦위험하고 비싼 실험을, 화면 속에서 먼저 해봐요|Risky, costly tests happen on screen first⟧", 12, "var(--ink)"))

# 5. 한계: 센서가 틀리면 트윈도 틀려요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + screen(150, 110, 1.3, robot(60, 10, 0.5)) + label(230, 260, "⟦센서가 정확하면 믿을 만해요|Reliable — when sensors are accurate⟧", 11, "var(--ink)")
         + robot(600, 170, 1.1) + label(600, 90, "✕", 30, "var(--bad)", cls="d")
         + label(600, 250, "⟦센서가 끊기면 트윈도 엉터리가 돼요|Sensor dropout makes the twin wrong too⟧", 11, "var(--ink)")
         + label(380, 288, "⟦다음 부스 엣지 컴퓨팅에서, 이 센서 데이터를 어떻게 빠르게 처리하는지 봐요|Next booth, Edge Computing, shows how this sensor data gets processed fast⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "digitaltwin", "order": 1,
    "title": ("화면 속 쌍둥이 로봇", "The Twin Robot on the Screen"),
    "h1": ("<em>디지털 트윈</em>이 뭐예요?", "What is a <em>Digital Twin</em>?"),
    "sub": ("디지털 트윈을, 과학관 전시장에서 진짜 로봇 옆에 놓인 화면 속 쌍둥이로 풀어봤어요.",
            "Digital twin, told as a story about a look-alike twin living on a screen next to the real robot at a science expo."),
    "panels": [
        {"svg": P1, "alt": ("과학관 입구에서 안내원이 관람객에게 전시장을 소개하고, 첫 부스에 진짜 로봇이 있음", "At the expo entrance, a guide introduces the hall to a visitor; the first booth holds a real robot"),
         "caption": ("오늘 첫 부스는 디지털 트윈이에요.", "Today's first booth is Digital Twin."),
         "small": ("진짜 로봇은 함부로 못 건드려요.", "The real robot there — you can't just poke it.")},
        {"svg": P2, "alt": ("시연 담당자가 진땀을 흘리며 진짜 로봇을 실험하다 금이 감", "A demonstrator sweats as the real robot cracks during a test"),
         "caption": ("진짜 기계로 함부로 실험하면 큰일나요.", "Experimenting on the real machine is risky."),
         "small": ("수리비가 얼마나 나올지 몰라요.", "No telling how big the repair bill will be.")},
        {"svg": P3, "hero": True, "alt": ("진짜 로봇과 화면 속 쌍둥이가 센서선으로 연결되어 똑같이 움직임", "The real robot and its on-screen twin, linked by sensor lines, move the same way"),
         "caption": ("디지털 트윈은 진짜 기계를 그대로 빼닮은 화면 속 쌍둥이예요.", "A digital twin is a look-alike twin of the real machine, living on a screen."),
         "small": ("센서 데이터로 진짜와 똑같이 움직여요.", "Sensor data makes it move exactly like the real one."),
         "tricks": (4, [
             (TWIN_SYNC, ("실시간으로 맞추기", "Sync in real time"), ("센서 값을 그대로 받아요", "fed live by sensor data")),
             (TWIN_TEST, ("가상에서 먼저 실험", "Test on the twin first"), ("위험한 설정도 안전하게", "even risky settings, safely"), "calm"),
             (TWIN_PREDICT, ("고장을 미리 예측", "Predict failure early"), ("패턴으로 미리 알아채요", "spotted from the pattern")),
             (TWIN_LOG, ("기록을 계속 쌓기", "Keep a running log"), ("과거 상태도 돌아봐요", "so you can look back"), "warm"),
         ])},
        {"svg": P4, "alt": ("진짜 로봇과 디지털 트윈을 비교하는 설명판: 위험·비용·반복·기록", "A board comparing the real robot and its twin: risk, cost, repeatability, history"),
         "caption": ("위험하고 비싼 실험을 화면 속에서 먼저 해봐요.", "Risky, costly tests happen on screen first."),
         "small": ("거의 공짜로, 수백 번도 반복할 수 있어요.", "Almost free, and repeatable hundreds of times.")},
        {"svg": P5, "alt": ("왼쪽: 센서가 정확하면 트윈을 믿을 만함. 오른쪽: 센서가 끊기면 트윈도 엉터리가 됨", "Left: accurate sensors make the twin reliable. Right: a sensor dropout makes the twin wrong too"),
         "caption": ("트윈은 센서 데이터가 정확해야 믿을 수 있어요.", "The twin is only as trustworthy as its sensor data."),
         "small": ("다음 부스 엣지 컴퓨팅에서, 이 데이터를 어떻게 빠르게 처리하는지 봐요.", "Next booth, Edge Computing, shows how this data gets processed fast.")},
    ],
    "summary": (("<b>디지털 트윈</b>은 진짜 기계·설비를 <b>센서 데이터로 그대로 복제한 가상 쌍둥이</b>로, 위험하거나 비싼 실험을 화면 속에서 먼저 해볼 수 있게 해줘요.",
                 "A <b>digital twin</b> is a <b>virtual twin, kept in sync by sensor data</b>, that lets you try risky or costly experiments on screen first."),
                ("디지털 트윈은 물리적 자산·공정·시스템을 소프트웨어로 실시간 복제해, 시뮬레이션·예측·최적화에 활용하는 기술이에요. 트윈의 정확도는 전적으로 들어오는 센서 데이터 품질에 달려 있고, 최종 검증은 여전히 실물로 한 번 더 거쳐야 해요.",
                 "A digital twin is a software replica of a physical asset, process, or system, kept synchronized in real time for simulation, prediction, and optimization. Its accuracy depends entirely on the quality of incoming sensor data, and final validation still needs a pass on the real thing.")),
    "glossary": [
        ("디지털 트윈", "Digital Twin", ("화면 속 쌍둥이.", "The look-alike twin on screen."), ("센서 데이터로 진짜와 같이 움직여요.", "Moves like the real thing, fed by sensor data.")),
        ("엣지 컴퓨팅", "Edge Computing", ("센서 바로 옆에서 빠르게 계산.", "Computing right next to the sensor."), ('트윈에 들어갈 데이터를 빠르게 처리해요. → <a href="edgecompute-ko.html">다음 부스, 엣지 컴퓨팅</a>', 'Processes the twin\'s incoming data fast. → <a href="edgecompute-en.html">next booth, Edge Computing</a>')),
        ("스마트팩토리", "Smart Factory", ("트윈·로봇·센서가 함께 일하는 공장.", "A factory where twins, robots, and sensors work together."), ('디지털 트윈이 실제로 쓰이는 현장이에요. → <a href="smartfactory-ko.html">스마트팩토리 부스</a>', 'Where digital twins are actually put to work. → <a href="smartfactory-en.html">the Smart Factory booth</a>')),
        ("메타버스", "Metaverse", ("새 가상 세계를 만드는 것.", "Building a brand-new virtual world."), ('트윈은 진짜를 복제하지만, 메타버스는 새로 만들 수도 있어요. → <a href="metaverse-ko.html">메타버스 부스</a>', 'A twin copies something real; a metaverse can invent something new. → <a href="metaverse-en.html">the Metaverse booth</a>')),
        ("IoT 센서", "IoT Sensor", ("쌍둥이에게 진짜 상태를 알려주는 눈과 귀.", "The eyes and ears that tell the twin the real state."), ("센서가 끊기면 트윈도 엉터리가 돼요.", "If sensors drop out, the twin goes wrong too.")),
        ("시뮬레이션", "Simulation", ("가상으로 미리 돌려보는 것.", "Running it virtually, ahead of time."), ("트윈의 핵심 쓸모 중 하나예요.", "One of the twin's main uses.")),
        ("예지보전", "Predictive Maintenance", ("고장나기 전에 미리 손보는 것.", "Fixing it before it actually breaks."), ("트윈이 쌓은 기록으로 패턴을 읽어요.", "Read from the pattern in the twin's logs.")),
        ("실물 검증", "Physical Validation", ("결국 한 번은 진짜로 확인하는 것.", "Eventually checking it on the real thing, once."), ("트윈이 다 해결해주진 않아요.", "The twin doesn't settle everything by itself.")),
    ],
}
