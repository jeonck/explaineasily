from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


def car(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="0" y="20" width="120" height="34" rx="10" fill="var(--accent)"/>'
            f'<path d="M20 20 L36 0 h48 l16 20z" fill="#1B2A44"/>'
            f'<circle cx="26" cy="56" r="14" fill="#2E2E2E"/><circle cx="94" cy="56" r="14" fill="#2E2E2E"/>'
            f'<circle cx="26" cy="56" r="5" fill="#AAB"/><circle cx="94" cy="56" r="5" fill="#AAB"/></g>')


EYE_P = '<circle cx="32" cy="32" r="16" fill="#fff" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="7" fill="var(--ink)"/>'
BRAIN2_P = '<rect x="14" y="16" width="36" height="32" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="26" cy="32" r="4" fill="var(--ink)"/><circle cx="38" cy="32" r="4" fill="var(--ink)"/>'
STEER_P = '<circle cx="32" cy="32" r="20" fill="none" stroke="#8A8A8A" stroke-width="5"/><circle cx="32" cy="32" r="5" fill="#8A8A8A"/><path d="M32 12 v20 M14 42 l18 -10 M50 42 l-18 -10" stroke="#8A8A8A" stroke-width="4"/>'
HANDS_P = '<path d="M14 40 q18 -24 36 0" stroke="var(--bad)" stroke-width="6" fill="none" stroke-linecap="round"/>'
EYE_I, BRAIN2_I, STEER_I, HANDS_I = icon(EYE_P), icon(BRAIN2_P), icon(STEER_P), icon(HANDS_P)

# 1. 자동차 시연 트랙 — 운전석이 비어 있어요
P1 = svg(300, sky(300)
         + car(300, 150, 1.3)
         + person(600, 170, s=0.8, face=EYES, **VISITOR)
         + label(380, 260, "⟦운전석에 아무도 없는데, 차가 알아서 움직여요|the driver's seat is empty, yet the car moves on its own⟧", 12, "var(--bad)")
         + label(380, 290, "⟦저 차는 어떻게 길을 보고 장애물을 피해 가는 거죠?|how does that car see the road and dodge obstacles?⟧", 12, "var(--ink)"))

# 2. 길은 늘 다르게 생겼어요 - 사람도 매번 다시 봐야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=EYES, **DEMO)
         + bubble(300, 70, 270, 50, "⟦굽은 길, 갑자기 튀어나온 사람, 멈춘 공...|a curving road, someone darting out, a stray ball...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦길 위 상황은 매번 달라서, 정해진 규칙만으로는 차를 몰 수 없어요|road conditions change every time, so fixed rules alone can't drive the car⟧", 12, "var(--ink)"))

# 3. 자율주행 = 센서로 보고, 스스로 판단해서, 직접 운전하는 차 (hero)
P3 = svg(340, sky(340)
         + car(280, 150, 1.4)
         + glyph(560, 120, 1.0, EYE_P) + glyph(560, 190, 1.0, BRAIN2_P)
         + person(660, 250, s=0.6, face=SMILE, **VISITOR)
         + label(380, 30, "⟦자율주행 = 센서로 길을 보고, 스스로 판단해서, 직접 핸들을 꺾는 차|autonomous driving = a car that sees the road, decides for itself, and turns the wheel⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦이 시연 차는 정해진 구역 안에서, 사람 없이 운전을 끝까지 맡아요|within its set area, this demo car does all the driving, no one at the wheel⟧", 12, "var(--muted)"))

# 4. 보기 → 판단 → 움직이기, 그리고 자율주행의 단계
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 260, "⟦보고 → 판단 → 움직이기|SEE → DECIDE → ACT⟧",
                     ("⟦① 카메라·LiDAR·레이더로 주변을 봐요|① see around it with camera, LiDAR, radar⟧",
                      "⟦② 길·사람·신호를 판단해요|② judge the road, people, signals⟧",
                      "⟦③ 핸들·브레이크를 직접 움직여요|③ turn the wheel and brake itself⟧",
                      "⟦④ 단계(레벨)마다 사람 개입이 달라요|④ each level needs a different amount of human help⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦운전 단계: 레벨 0(전부 사람)~레벨 5(전부 차)|driving levels: 0 (all human) to 5 (all car)⟧", 11, "var(--muted)"))

# 5. 한계 - 처음 보는 돌발 상황엔 아직 서툴러요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + car(130, 150, 1.0)
         + label(190, 260, "⟦늘 보던 길에선 차가 사람보다 꾸준하고 안 지쳐요|on familiar roads, the car is steadier and never tires⟧", 11, "var(--ink)")
         + car(510, 150, 1.0) + glyph(610, 140, 0.8, HANDS_P)
         + label(570, 260, "⟦처음 보는 공사장·눈길에선 차가 아직 서툴러요|a new construction zone or snowy road can trip the car up⟧", 11, "var(--ink)")
         + label(380, 282, "⟦낯선 상황에서는 운전자가 넘겨받거나 원격 직원이 조언해야 할 때가 있어요|in unfamiliar situations, a driver may take over or a remote agent may advise⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "autodrive", "order": 22,
    "title": ("운전석이 비어 있는 시연 트랙의 차", "The Demo-Track Car with an Empty Driver's Seat"),
    "h1": ("<em>자율주행</em>이 뭐예요?", "What is <em>Autonomous Driving</em>?"),
    "sub": ("자율주행을, 운전석이 비어 있어도 스스로 보고 판단해 달리는 시연 트랙 차 이야기로 풀어봤어요.",
            "Autonomous driving, told as a story about a demo-track car with an empty driver's seat that sees and decides for itself."),
    "panels": [
        {"svg": P1, "alt": ("운전석이 빈 채로 차가 혼자 움직이고, 관람객이 놀라서 봄", "A car moves with an empty driver's seat while a visitor watches, amazed"),
         "caption": ("자동차 시연 트랙 — 운전석이 비어 있어요.", "The demo-track car — and its driver's seat is empty."),
         "small": ("저 차는 어떻게 길을 보고 장애물을 피해 가는 거죠?", "How does that car see the road and dodge obstacles?")},
        {"svg": P2, "alt": ("시연 담당자가 길 위에서 벌어질 수 있는 여러 돌발 상황을 나열함", "A demo staffer lists the many unpredictable things that can happen on a road"),
         "caption": ("길은 늘 다르게 생겼어요.", "The road looks different every single time."),
         "small": ("길 위 상황은 매번 달라서, 정해진 규칙만으로는 차를 몰 수 없어요.", "Road conditions change every time, so fixed rules alone can't drive the car.")},
        {"svg": P3, "hero": True, "alt": ("차 옆에 눈과 뇌 모양의 그림이 떠 있고, 관람객이 흐뭇하게 지켜봄", "Eye and brain icons float beside the car while a visitor watches contentedly"),
         "caption": ("자율주행은 센서로 보고, 스스로 판단해서, 직접 운전하는 차예요.", "Autonomous driving is a car that sees the road, decides for itself, and turns the wheel."),
         "small": ("이 시연 차는 정해진 구역 안에서, 사람 없이 운전을 끝까지 맡아요.", "Within its set area, this demo car does all the driving, no one at the wheel."),
         "tricks": (4, [
             (EYE_I, ("보기", "See"), ("카메라·LiDAR로 주변을 봐요", "sees around it with camera, LiDAR")),
             (BRAIN2_I, ("판단하기", "Decide"), ("길·사람·신호를 가늠해요", "judges the road, people, signals"), "calm"),
             (STEER_I, ("움직이기", "Act"), ("핸들·브레이크를 직접 조작해요", "turns the wheel and brakes itself")),
             (HANDS_I, ("도움 받기", "Get help"), ("낯선 상황엔 사람 도움이 필요할 때가 있어요", "may need a person in unfamiliar situations"), "warm"),
         ])},
        {"svg": P4, "alt": ("보기→판단→움직이기 설명판, 안내원이 자율주행 레벨을 설명", "A see-decide-act board, with a guide explaining autonomous driving levels"),
         "caption": ("차는 센서로 보고, 스스로 판단하고, 핸들과 브레이크를 직접 움직여요.", "The car sees with sensors, decides for itself, and moves the wheel and brakes on its own."),
         "small": ("자율주행은 레벨 0(전부 사람)부터 레벨 5(전부 차)까지 나뉘어요.", "Autonomous driving ranges from Level 0 (all human) to Level 5 (all car).")},
        {"svg": P5, "alt": ("왼쪽: 늘 다니던 길에서 차가 안정적으로 달림. 오른쪽: 낯선 공사장 앞에서 손이 필요하다는 신호가 뜸", "Left: the car drives smoothly on a familiar road. Right: a hand icon signals it needs help at an unfamiliar construction site"),
         "caption": ("자율주행차는 처음 보는 돌발 상황엔 아직 서툴러요.", "Self-driving cars are still clumsy in situations they've never seen."),
         "small": ("낯선 상황에서는 운전자가 넘겨받거나 원격 직원이 조언해야 할 때가 있어요.", "In unfamiliar situations, a driver may have to take over or a remote agent may have to advise.")},
    ],
    "summary": (("<b>자율주행</b> = 센서로 주변을 <b>보고</b>, 스스로 <b>판단</b>해서, 직접 핸들과 브레이크를 <b>움직이는</b> 차.",
                 "<b>Autonomous driving</b> = a car that <b>sees</b> its surroundings with sensors, <b>decides</b> for itself, and <b>acts</b> on the wheel and brakes directly."),
                ("자율주행은 카메라·LiDAR·레이더 등 센서로 주변 환경을 인식하고, AI가 상황을 판단해 조향·가속·제동을 직접 수행하는 기술이에요. SAE 기준 레벨 0(비자동)부터 레벨 5(완전자율)까지 단계가 나뉘며, 단계가 올라갈수록 사람의 개입이 줄어들어요. 레벨 3은 시스템이 요청하면 사람이 넘겨받아야 하고, 레벨 4는 정해진 조건 안에서, 레벨 5는 어떤 조건에서든 사람이 대기하지 않아도 돼요.",
                 "Autonomous driving perceives its surroundings with sensors like cameras, LiDAR, and radar, then has AI judge the situation and directly handle steering, acceleration, and braking. The SAE scale runs from Level 0 (no automation) to Level 5 (full autonomy), with less human involvement needed at each higher level. At Level 3 a person must take over when the system asks; at Level 4 no one needs to stand by within the set conditions, and at Level 5 under any conditions.")),
    "glossary": [
        ("LiDAR", "LiDAR", ("레이저로 거리를 정확히 재는 눈.", "The eye that measures distance exactly with lasers."), ('많은 자율주행차가 기대는 눈이에요. → <a href="lidar-ko.html">레이저로 거리를 재는 눈</a>', "An eye many self-driving cars rely on. → <a href=\"lidar-en.html\">the eye that measures distance with lasers</a>")),
        ("자율주행 레벨", "Autonomous Driving Levels", ("사람 개입이 줄어드는 여섯 단계.", "Six stages where human involvement shrinks."), ("레벨 0은 전부 사람, 레벨 5는 전부 차예요.", "Level 0 is all human; Level 5 is all car.")),
        ("센서 융합", "Sensor Fusion", ("여러 센서의 정보를 하나로 합치는 것.", "Combining data from several sensors into one picture."), ("카메라·LiDAR·레이더를 함께 써서 서로의 약점을 메워요.", "Camera, LiDAR, and radar together cover for each other's blind spots.")),
        ("CPS", "CPS", ("컴퓨터와 실제 기계가 맞물려 움직이는 것.", "Computer and real machine moving in lockstep."), ('자율주행차도 이 틀 안의 한 예시예요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', 'A self-driving car is one example living inside this bigger frame. → <a href="cps-en.html">Cyber-Physical Systems</a>')),
        ("드론 보안위협", "Drone Security Threats", ("드론의 무선 조종 신호를 노리는 위협.", "Threats that target a drone's wireless control link."), ('자율주행차는 무선 신호보다 센서에 더 기대지만, 외부 공격을 받는 위협은 닮았어요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', 'A self-driving car leans more on sensors than radio links, but outside attacks threaten both. → <a href="dronesecurity-en.html">the drone held up by an invisible string</a>')),
        ("정량적 위험분석", "Quantitative Risk Analysis", ("사고 확률과 피해를 숫자로 재는 방법.", "A way to score accident probability and damage with numbers."), ('자율주행차의 안전성도 이렇게 가늠해요. → <a href="quantrisk-ko.html">위험을 숫자 하나로 적는 전광판</a>', "A self-driving car's safety gets sized up the same way. → <a href=\"quantrisk-en.html\">the scoreboard that writes risk as one number</a>")),
        ("스마트팜", "Smart Farm", ("센서가 작물을 대신 돌봐주는 또 다른 현장.", "Another real-world setting where sensors tend the crops."), ("비슷한 센서로 보고 자동으로 움직인다는 생각이 밭에도 있어요. → <a href=\"smartfarm-ko.html\">센서가 돌보는 온실 부스</a>", "The same sense-and-act-automatically idea lives on a farm too. → <a href=\"smartfarm-en.html\">the greenhouse booth tended by sensors</a>")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
