from _draw import *
from _world import *


def drone(x, y, s=1.0, color="var(--bad)"):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-6" width="32" height="12" rx="4" fill="{color}"/>'
    for dx, dy in ((-22, -16), (22, -16), (-22, 16), (22, 16)):
        out += f'<circle cx="{dx}" cy="{dy}" r="7" fill="none" stroke="{color}" stroke-width="2"/><path d="M{dx-14} {dy} h28" stroke="{color}" stroke-width="2"/>'
    return out + '</g>'


def radarwave(x, y, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for r in (18, 32, 46):
        out += f'<path d="M-{r} 0 A{r} {r} 0 0 1 {r} 0" fill="none" stroke="var(--good)" stroke-width="3" opacity="{1 - r/60:.2f}"/>'
    return out + '</g>'


def net(x, y, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><path d="M-30 -30 h60 v45 l-30 20 l-30 -20z" fill="none" stroke="var(--accent)" stroke-width="2"/>'
    for i in range(1, 5):
        out += f'<path d="M{-30+i*12} -30 L{-30+i*12-6} 15" stroke="var(--accent)" stroke-width="1.5"/>'
    return out + '</g>'


# 1. 허가 안 받은 드론이 몰래 날아들어요
P1 = svg(320, sky(320)
         + booth(60, 60, 200, 150, 1.0, "var(--muted)", "⟦공항·경기장|airport / stadium⟧")
         + drone(690, 75, 1.1)
         + person(400, 170, s=0.85, face=SWEAT + EYES, **DEMO)
         + bubble(410, 95, 210, 46, "⟦저거 허가받은 드론 맞아요?|is that drone even authorized?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦작고 빠른 드론은 막기 어려워요|small, fast drones are hard to stop⟧", 13, "var(--ink)"))

# 2. 레이더에도 잘 안 잡혀요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + drone(380, 110, 1.2)
         + label(380, 170, "✕", 28, "var(--bad)", cls="d")
         + label(380, 250, "⟦작고, 낮게 날고, 금속도 적어서 레이더가 잘 못 봐요|small, low-flying, little metal — hard for radar to catch⟧", 12, "var(--ink)")
         + label(380, 282, "⟦보통 방공망으로는 놓치기 쉬워요|easy to slip past ordinary air defenses⟧", 11, "var(--muted)"))

# 3. 안티드론 = 탐지→식별→무력화 (hero)
P3 = svg(340, sky(340)
         + drone(600, 90, 1.3)
         + radarwave(300, 220, 1.8)
         + person(300, 220, s=0.8, face=EYES, **DEMO)
         + net(560, 150, 1.0)
         + label(380, 30, "⟦안티드론 = 침입 드론을 탐지하고, 식별하고, 무력화하는 기술 묶음|Anti-Drone = a set of techs that detects, identifies, and disables an intruding drone⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦레이더·카메라로 찾고, 그물이나 전파로 막아요|found by radar and camera, stopped by net or jamming⟧", 12, "var(--muted)"))

AD_DETECT = icon('<path d="M-10 0 A18 18 0 0 1 10 0" fill="none" stroke="var(--good)" stroke-width="3" transform="translate(32,40)"/><circle cx="32" cy="40" r="3" fill="var(--good)"/><path d="M20 16 l24 -8" stroke="var(--line)" stroke-width="2" opacity="0.5"/>')
AD_ID = icon('<rect x="16" y="14" width="32" height="32" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="30" r="6" fill="var(--accent)"/><path d="M22 40 q10 -8 20 0" stroke="var(--accent)" stroke-width="3" fill="none"/>')
AD_JAM = icon('<path d="M14 32 q9 -16 18 0 q9 -16 18 0" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')
AD_CATCH = icon('<path d="M18 14 h28 v22 l-14 10 l-14 -10z" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M24 14 L28 46 M40 14 L36 46" stroke="var(--accent)" stroke-width="1.5"/>')

# 4. 단계별 방법
P4 = svg(360, sky(360, ground=False)
         + infoboard(130, 30, 500, 290, "⟦안티드론 3단계|THE THREE STAGES⟧",
                     ("⟦탐지 — 레이더·카메라·전파로 찾기|detect — with radar, camera, radio⟧",
                      "⟦식별 — 아군기인지 침입 드론인지 가려내기|identify — friend or intruder⟧",
                      "⟦무력화 — 전파 교란(재밍)으로 조종을 끊기|disable — jam the control signal⟧",
                      "⟦또는 — 그물 포획·격추로 직접 막기|or — net capture or takedown⟧"), 1.3)
         + label(380, 345, "⟦순서를 건너뛰면 엉뚱한 드론을 막을 수도 있어요|skip a stage, and you might stop the wrong drone⟧", 12, "var(--ink)"))

# 5. 한계: 오인식, 전파 교란의 부작용
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + drone(190, 150, 1.1, color="var(--good)") + label(190, 240, "⟦일반 드론을 침입자로 착각할 수 있어요|an ordinary drone can be mistaken for an intruder⟧", 11, "var(--ink)")
         + person(570, 150, s=0.85, face=FROWN, **GUIDE)
         + label(570, 240, "⟦전파 교란은 주변 통신에도 영향을 줘요|jamming can disrupt nearby communications too⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그래서 사용엔 법적 제한이 따라요|that's why its use comes with legal limits⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "antidrone", "order": 12,
    "title": ("하늘의 불청객을 찾아 막는 삼단계", "The Three Steps That Find and Stop an Uninvited Flyer"),
    "h1": ("<em>안티드론</em>이 뭐예요?", "What is <em>Anti-Drone</em>?"),
    "sub": ("안티드론을, 전시장 위로 몰래 날아든 드론을 탐지·식별·무력화하는 이야기로 풀어봤어요.",
            "Anti-drone technology, told as a story about detecting, identifying, and disabling a drone that sneaks over the expo hall."),
    "panels": [
        {"svg": P1, "alt": ("시연 담당자가 공항·경기장 위로 몰래 날아든 드론을 가리킴", "A demonstrator points at a drone sneaking over an airport or stadium"),
         "caption": ("저거 허가받은 드론 맞아요?", "Is that drone even authorized?"),
         "small": ("작고 빠른 드론은 막기 어려워요.", "Small, fast drones are hard to stop.")},
        {"svg": P2, "alt": ("드론이 레이더에 잘 잡히지 않음을 보여줌", "Showing a drone slipping past radar detection"),
         "caption": ("레이더에도 잘 안 잡혀요.", "It's hard for radar to catch too."),
         "small": ("작고, 낮게 날고, 금속도 적어서 보통 방공망으로는 놓치기 쉬워요.", "Small, low-flying, with little metal — easy to slip past ordinary air defenses.")},
        {"svg": P3, "hero": True, "alt": ("드론이 침입하자 레이더파가 탐지하고, 요원이 그물로 무력화를 준비함", "A drone intrudes as radar waves detect it and an operator readies a net"),
         "caption": ("안티드론은 침입 드론을 탐지하고, 식별하고, 무력화하는 기술 묶음이에요.", "Anti-drone is a set of technologies that detects, identifies, and disables an intruding drone."),
         "small": ("레이더·카메라로 찾고, 그물이나 전파로 막아요.", "Found by radar and camera, stopped by net or jamming."),
         "tricks": (4, [
             (AD_DETECT, ("탐지하기", "Detect it"), ("레이더·카메라·전파로요", "with radar, camera, radio"), "calm"),
             (AD_ID, ("식별하기", "Identify it"), ("아군기인지 가려내요", "friend or intruder?")),
             (AD_JAM, ("전파 교란하기", "Jam its signal"), ("조종 연결을 끊어요", "cuts off the control link"), "warm"),
             (AD_CATCH, ("포획·격추하기", "Capture or take it down"), ("그물이나 직접 무력화로요", "with a net or direct takedown")),
         ])},
        {"svg": P4, "alt": ("탐지·식별·무력화 세 단계와 각 단계의 방법을 보여주는 설명판", "A board showing the detect-identify-disable stages and methods for each"),
         "caption": ("탐지→식별→무력화, 순서대로 진행돼요.", "It goes in order: detect, then identify, then disable."),
         "small": ("순서를 건너뛰면 엉뚱한 드론을 막을 수도 있어요.", "Skip a stage, and you might stop the wrong drone.")},
        {"svg": P5, "alt": ("왼쪽: 일반 드론을 침입자로 오인식함. 오른쪽: 전파 교란이 주변 통신에 영향을 줌", "Left: an ordinary drone mistaken for an intruder. Right: jamming disrupts nearby communications"),
         "caption": ("오인식 위험과 전파 교란의 부작용이 있어요.", "There's a risk of false positives, and jamming has side effects."),
         "small": ("그래서 사용엔 법적 제한이 따라요.", "That's why its use comes with legal limits.")},
    ],
    "summary": (("<b>안티드론</b>은 침입 드론을 <b>탐지→식별→무력화</b>하는 기술 묶음으로, 오인식과 전파 교란의 부작용을 함께 관리해야 해요.",
                 "<b>Anti-drone</b> is a set of technologies that <b>detects, identifies, and disables</b> an intruding drone — while managing the risk of false positives and jamming side effects."),
                ("안티드론 시스템은 레이더·전자광학(EO/IR) 카메라·RF 센서로 드론을 탐지하고, 비행 패턴·신호로 아군기와 침입 드론을 식별한 뒤, 재밍(전파 교란)이나 그물 포획, 직접 격추로 무력화하는 체계예요. 소형·저고도·저RCS(레이더 반사 면적) 드론은 탐지 자체가 어렵고, 재밍은 주변 통신·항행 장비에 영향을 줄 수 있어 운용에 법적·기술적 제약이 따라요.",
                 "An anti-drone system detects drones with radar, electro-optical/infrared (EO/IR) cameras, and RF sensors, identifies friend from intruder using flight patterns and signals, then disables the target via jamming, net capture, or direct takedown. Small, low-altitude, low-RCS (radar cross-section) drones are inherently hard to detect, and jamming can affect nearby communications and navigation equipment, so its use comes with legal and technical constraints.")),
    "glossary": [
        ("안티드론", "Anti-Drone", ("침입 드론을 찾아 막는 기술 묶음.", "The set of technologies that finds and stops an intruding drone."), ("탐지·식별·무력화 세 단계로 이뤄져요.", "Made up of three stages: detect, identify, disable.")),
        ("RF 센서", "RF Sensor", ("드론 조종 신호를 잡아내는 센서.", "The sensor that catches a drone's control signal."), ("탐지 단계의 핵심 도구예요.", "A key tool in the detection stage.")),
        ("재밍(전파 교란)", "Jamming", ("드론과 조종기 사이 신호를 끊는 방법.", "Cutting the signal between drone and controller."), ("주변 통신에도 영향을 줄 수 있어요.", "Can affect nearby communications too.")),
        ("저RCS(낮은 레이더 반사 면적)", "Low RCS", ("레이더에 잘 안 잡히는 성질.", "Being hard for radar to catch."), ("소형 드론 탐지가 어려운 이유예요.", "Why small drones are hard to detect.")),
        ("MEC", "MEC", ("기지국 옆에서 빠르게 계산하는 기술.", "Computing nearby a base station for speed."), ('탐지 데이터를 빠르게 처리할 때 비슷한 개념이 쓰여요. → <a href="mec-ko.html">MEC 부스</a>', "A similar idea helps process detection data fast. → <a href=\"mec-en.html\">the MEC booth</a>")),
        ("스마트시티", "Smart City", ("도시 곳곳 데이터로 안전을 지키는 것.", "Using citywide data to keep things safe."), ('재난 조기경보처럼, 안전 서비스의 한 사례예요. → <a href="smartcity-ko.html">스마트시티 부스</a>', "A safety-service example, like early disaster warning. → <a href=\"smartcity-en.html\">the Smart City booth</a>")),
        ("오인식(false positive)", "False Positive", ("일반 드론을 침입자로 잘못 보는 것.", "Mistaking an ordinary drone for an intruder."), ("식별 단계를 건너뛰면 생기기 쉬워요.", "Easy to get if the identify stage is skipped.")),
        ("항공 안전 규정", "Aviation Safety Regulation", ("드론·안티드론 모두를 제한하는 법.", "The law that limits both drones and anti-drone use."), ("재밍 사용 범위도 여기에 달려 있어요.", "Governs how far jamming may be used too.")),
    ],
}
