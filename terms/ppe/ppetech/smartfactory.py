from _draw import *
from _world import *


def conveyor(x, y, w, s=1.0, broken=False):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="18" rx="4" fill="#5A6B85"/>'
    for i in range(int(w // 30)):
        out += f'<rect x="{i*30+6}" y="-18" width="18" height="18" rx="3" fill="var(--accent)"/>'
    if broken:
        out += f'<rect x="{w*0.6:.0f}" y="-18" width="18" height="18" rx="3" fill="var(--bad)"/>'
    return out + '</g>'


def sensordot(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="6" fill="var(--good)"/><circle r="12" fill="none" stroke="var(--good)" stroke-width="2" opacity="0.5"/></g>'


def sensorline_sf(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>'


# 1. 끝에 가서야 불량을 발견해요
P1 = svg(300, sky(300, ground=False)
         + conveyor(80, 220, 560, 1.0, broken=True)
         + person(680, 170, s=0.8, face=FROWN, **DEMO)
         + bubble(540, 70, 210, 46, "⟦앗, 끝까지 와서야 불량인 걸 알았어요|oh — we only found the defect at the very end⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦라인 전체가 멈춰야 해요|the whole line has to stop⟧", 13, "var(--bad)"))

# 2. 각 공정이 따로 놀아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(60, 60, 180, 160, 1.0, "var(--muted)", "⟦절단|CUT⟧")
         + booth(290, 60, 180, 160, 1.0, "var(--muted)", "⟦조립|ASSEMBLE⟧")
         + booth(520, 60, 180, 160, 1.0, "var(--muted)", "⟦검사|INSPECT⟧")
         + label(380, 260, "⟦공정끼리 서로의 상태를 몰라요|each process has no idea what the others are doing⟧", 13, "var(--ink)")
         + label(380, 288, "⟦문제가 생겨도 뒤늦게 알아채요|so a problem is noticed too late⟧", 12, "var(--muted)"))

# 3. 스마트팩토리 = 공장이 스스로를 지켜봄 (hero)
P3 = svg(340, sky(340, ground=False)
         + conveyor(80, 240, 560, 1.0)
         + sensordot(140, 210, 1.0) + sensordot(380, 210, 1.0) + sensordot(620, 210, 1.0)
         + screen(330, 60, 1.3, conveyor(10, 44, 60, 0.6))
         + sensorline_sf(140, 205, 395, 100) + sensorline_sf(620, 205, 460, 100)
         + label(380, 30, "⟦스마트팩토리 = 센서가 보고, 데이터가 모여, 공장이 스스로 조절해요|Smart Factory = sensors watch, data gathers, the factory adjusts itself⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦문제가 생기면 그 자리에서 바로 알아채요|a problem is caught right where it happens⟧", 12, "var(--muted)"))


FAC_SENSE = icon('<circle cx="32" cy="32" r="10" fill="var(--good)"/><circle cx="32" cy="32" r="20" fill="none" stroke="var(--good)" stroke-width="3" opacity="0.6"/>')
FAC_TWIN = icon('<rect x="12" y="14" width="40" height="30" rx="3" fill="#1B2A44"/><rect x="18" y="20" width="28" height="18" rx="2" fill="#0A1120"/>')
FAC_EDGE = icon('<rect x="18" y="18" width="28" height="28" rx="4" fill="var(--accent)"/><path d="M32 10 v8 M32 46 v8 M10 32 h8 M46 32 h8" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
FAC_PREDICT = icon('<path d="M12 44 q10 -28 20 -10 q10 18 20 -24" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="52" cy="10" r="4" fill="var(--bad)"/>')

# 4. 네 겹으로 쌓인 구조
P4 = svg(360, sky(360, ground=False)
         + infoboard(130, 30, 500, 290, "⟦스마트팩토리 네 겹|THE FOUR LAYERS⟧",
                     ("⟦센서층 — 곳곳에서 데이터 모으기|sensing layer — gather data everywhere⟧",
                      "⟦네트워크층 — 빠르게 실어 나르기|network layer — carry it fast⟧",
                      "⟦분석층 — 디지털 트윈으로 미리 보기|analysis layer — preview with a digital twin⟧",
                      "⟦제어층 — 로봇·설비를 바로 조정하기|control layer — adjust robots and gear right away⟧"), 1.3)
         + label(380, 345, "⟦디지털 트윈·엣지 컴퓨팅이 여기서 함께 일해요|digital twins and edge computing work together here⟧", 12, "var(--ink)"))

# 5. 한계: 비용과 보안
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + f'<circle cx="190" cy="100" r="34" fill="none" stroke="var(--accent)" stroke-width="5"/><text x="190" y="110" text-anchor="middle" font-size="28" font-weight="700" fill="var(--accent)">$</text>'
         + label(190, 240, "⟦센서·로봇을 전부 까는 초기 비용이 커요|fitting sensors and robots everywhere costs a lot up front⟧", 11, "var(--ink)")
         + f'<rect x="156" y="80" width="28" height="22" rx="3" fill="var(--bad)"/><path d="M162 80 v-10 a8 8 0 0 1 16 0 v10" stroke="var(--bad)" stroke-width="4" fill="none" transform="translate(414,0)"/>'
         + label(570, 240, "⟦연결된 곳이 많을수록 뚫릴 곳도 많아요|more connections mean more places to break in⟧", 11, "var(--ink)")
         + label(380, 282, "⟦멋져 보여도, 비용·보안 문제는 전시장 밖 진짜 공장의 몫이에요|impressive as it looks, cost and security are the real factory's problem⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "smartfactory", "order": 3,
    "title": ("스스로를 지켜보는 공장", "The Factory That Watches Itself"),
    "h1": ("<em>스마트팩토리</em>가 뭐예요?", "What is a <em>Smart Factory</em>?"),
    "sub": ("스마트팩토리를, 센서와 화면 속 쌍둥이로 스스로를 지켜보는 공장 이야기로 풀어봤어요.",
            "Smart factory, told as a story about a factory that watches over itself with sensors and an on-screen twin."),
    "panels": [
        {"svg": P1, "alt": ("컨베이어 벨트 끝에서야 불량품을 발견해 라인이 멈춤", "A defect is spotted only at the end of the conveyor belt, stopping the whole line"),
         "caption": ("끝까지 와서야 불량인 걸 알았어요.", "The defect was only found at the very end."),
         "small": ("라인 전체가 멈춰야 해요.", "The whole line has to stop.")},
        {"svg": P2, "alt": ("절단·조립·검사 세 공정이 서로 따로 떨어져 있음", "Cutting, assembly, and inspection sit as three separate, disconnected booths"),
         "caption": ("공정끼리 서로의 상태를 몰라요.", "Each process has no idea what the others are doing."),
         "small": ("문제가 생겨도 뒤늦게 알아채요.", "So a problem is noticed too late.")},
        {"svg": P3, "hero": True, "alt": ("컨베이어 곳곳에 센서가 있고, 그 데이터가 화면 속 공장 쌍둥이로 모임", "Sensors dot the conveyor, feeding data into an on-screen twin of the factory"),
         "caption": ("스마트팩토리는 센서가 보고, 데이터가 모여, 공장이 스스로 조절하는 거예요.", "A smart factory is one where sensors watch, data gathers, and the factory adjusts itself."),
         "small": ("문제가 생기면 그 자리에서 바로 알아채요.", "A problem is caught right where it happens."),
         "tricks": (4, [
             (FAC_SENSE, ("실시간으로 수집하기", "Sense in real time"), ("곳곳의 센서로요", "sensors placed everywhere"), "calm"),
             (FAC_TWIN, ("디지털 트윈으로 미리 보기", "Preview with a twin"), ("바꾸기 전에 먼저 테스트", "test changes before they happen")),
             (FAC_EDGE, ("엣지에서 즉시 판단", "Decide at the edge"), ("바로 옆에서 빠르게", "right there, fast")),
             (FAC_PREDICT, ("데이터로 미리 정비", "Maintain predictively"), ("고장 전에 손봐요", "fixed before it breaks"), "warm"),
         ])},
        {"svg": P4, "alt": ("센서층·네트워크층·분석층·제어층 네 겹으로 쌓인 구조도", "A four-layer diagram: sensing, network, analysis, control"),
         "caption": ("스마트팩토리는 네 겹으로 쌓여 있어요.", "A smart factory is built in four layers."),
         "small": ("디지털 트윈·엣지 컴퓨팅이 여기서 함께 일해요.", "Digital twins and edge computing work together here.")},
        {"svg": P5, "alt": ("왼쪽: 초기 투자 비용이 큼. 오른쪽: 연결점이 많아 보안 취약점도 늘어남", "Left: a big up-front investment. Right: more connections mean more security holes"),
         "caption": ("초기 비용이 크고, 연결점이 늘수록 보안도 신경 써야 해요.", "The up-front cost is big, and more connections mean more security to watch."),
         "small": ("전시장 데모와 달리, 진짜 공장에서는 이 둘이 진짜 문제예요.", "Unlike the expo demo, in a real factory these are the real problems.")},
    ],
    "summary": (("<b>스마트팩토리</b>는 센서·네트워크·데이터 분석·제어를 연결해 <b>공장이 스스로를 지켜보고 조절</b>하게 만든 공장이에요.",
                 "A <b>smart factory</b> connects sensors, networks, data analysis, and control so the <b>factory watches and adjusts itself</b>."),
                ("스마트팩토리는 IoT 센서, 네트워크, 빅데이터·AI 분석, 제어 시스템을 통합해 생산 전 과정을 실시간으로 모니터링·최적화하는 공장이에요. 디지털 트윈으로 변경을 미리 시뮬레이션하고 엣지 컴퓨팅으로 현장 판단을 즉시 내리지만, 초기 구축 비용과 늘어난 연결점만큼 커지는 보안 위협은 별도로 관리해야 해요.",
                 "A smart factory integrates IoT sensors, networking, big-data/AI analysis, and control systems to monitor and optimize the entire production process in real time. It uses digital twins to simulate changes ahead of time and edge computing to decide on the spot, but the up-front build cost and the security exposure that grows with every new connection both need separate management.")),
    "glossary": [
        ("스마트팩토리", "Smart Factory", ("스스로를 지켜보는 공장.", "A factory that watches itself."), ("센서·분석·제어가 하나로 이어져요.", "Sensing, analysis, and control, all linked together.")),
        ("디지털 트윈", "Digital Twin", ("바꾸기 전에 미리 테스트하는 화면 속 쌍둥이.", "The on-screen twin you test changes on first."), ('스마트팩토리가 실제로 쓰는 기술이에요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', 'A technology the smart factory actually uses. → <a href="digitaltwin-en.html">the Digital Twin booth</a>')),
        ("엣지 컴퓨팅", "Edge Computing", ("현장에서 바로 판단하는 것.", "Deciding right there on the floor."), ('공장 현장의 즉시 판단을 맡아요. → <a href="edgecompute-ko.html">엣지 컴퓨팅 부스</a>', 'Handles the on-the-spot decisions. → <a href="edgecompute-en.html">the Edge Computing booth</a>')),
        ("스마트시티", "Smart City", ("도시 전체로 넓어진 같은 생각.", "The same idea, scaled up to a whole city."), ('공장 안이 아니라 도시 전체를 지켜봐요. → <a href="smartcity-ko.html">스마트시티 부스</a>', 'Watches a whole city instead of a factory floor. → <a href="smartcity-en.html">the Smart City booth</a>')),
        ("예지보전", "Predictive Maintenance", ("고장나기 전에 미리 손보는 것.", "Fixing it before it actually breaks."), ("데이터로 쌓인 패턴을 읽어요.", "Read from patterns in the collected data.")),
        ("MES(제조실행시스템)", "MES", ("공정 간 작업 지시를 실어 나르는 시스템.", "The system carrying work orders between processes."), ("스마트팩토리의 제어층에서 함께 일해요.", "Works alongside the control layer.")),
        ("OT 보안", "OT Security", ("공장 설비 자체를 지키는 보안.", "Security for the factory equipment itself."), ("연결점이 늘수록 더 중요해져요.", "Matters more as connections multiply.")),
        ("불량률", "Defect Rate", ("끝에 가서야 알면 늦는 숫자.", "The number you learn too late if you check only at the end."), ("실시간 센서로 더 일찍 잡아내요.", "Caught earlier with real-time sensors.")),
    ],
}
