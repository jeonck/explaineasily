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
         + label(380, 290, "⟦저게 어떻게 길을 보고 피해 가는 거죠?|how does it see the road and dodge things?⟧", 12, "var(--ink)"))

# 2. 길은 늘 다르게 생겼어요 - 사람도 매번 다시 봐야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=EYES, **DEMO)
         + bubble(300, 70, 250, 50, "⟦굽은 길, 갑자기 튀어나온 사람, 멈춘 공...|a curving road, someone darting out, a stray ball...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦길 위 상황은 매번 달라서, 정해진 규칙만으론 못 버텨요|the road is different every time — a fixed rule alone can't keep up⟧", 12, "var(--ink)"))

# 3. 자율주행 = 센서로 보고, 스스로 판단해서, 직접 운전하는 차 (hero)
P3 = svg(340, sky(340)
         + car(280, 150, 1.4)
         + glyph(560, 120, 1.0, EYE_P) + glyph(560, 190, 1.0, BRAIN2_P)
         + person(660, 250, s=0.6, face=SMILE, **VISITOR)
         + label(380, 30, "⟦자율주행 = 센서로 길을 보고, 스스로 판단해서, 직접 핸들을 꺾는 차|autonomous driving = a car that sees the road, decides for itself, and turns the wheel⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦사람이 타지 않아도, 차가 끝까지 운전을 맡아요|even with no one driving, the car handles the whole job⟧", 12, "var(--muted)"))

# 4. 보기 → 판단 → 움직이기, 그리고 자율주행의 단계
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 260, "⟦보고 → 판단 → 움직이기|SEE → DECIDE → ACT⟧",
                     ("⟦① 카메라·LiDAR·레이더로 주변을 봐요|① see around it with camera, LiDAR, radar⟧",
                      "⟦② 길·사람·신호를 판단해요|② judge the road, people, signals⟧",
                      "⟦③ 핸들·브레이크를 직접 움직여요|③ turn the wheel and brake itself⟧",
                      "⟦④ 단계(레벨)마다 사람 개입이 달라요|④ each level needs a different amount of human help⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦레벨 0(전부 사람)부터 레벨 5(전부 차)까지 나뉘어요|it ranges from Level 0 (all human) to Level 5 (all car)⟧", 11, "var(--muted)"))

# 5. 한계 - 처음 보는 돌발 상황엔 아직 서툴러요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + car(130, 150, 1.0)
         + label(190, 260, "⟦늘 보던 길에서는 사람보다 꾸준하고 지치지 않아요|on familiar roads, it's steadier and never gets tired⟧", 11, "var(--ink)")
         + car(510, 150, 1.0) + glyph(610, 140, 0.8, HANDS_P)
         + label(570, 260, "⟦처음 보는 공사장·눈길 같은 돌발 상황엔 아직 서툴러요|a brand-new construction zone or snowy road can still trip it up⟧", 11, "var(--ink)")
         + label(380, 282, "⟦이럴 때는 여전히 사람의 손이 다시 필요해요|at that point, a human hand is still needed again⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "autodrive", "order": 22,
    "title": ("운전석이 비어 있는 시연 트랙의 차", "The Demo-Track Car with an Empty Driver's Seat"),
    "h1": ("<em>자율주행</em>이 뭐예요?", "What is <em>Autonomous Driving</em>?"),
    "sub": ("자율주행을, 운전석이 비어 있어도 스스로 보고 판단해 달리는 시연 트랙 차 이야기로 풀어봤어요.",
            "Autonomous driving, told as a story about a demo-track car with an empty driver's seat that sees and decides for itself."),
    "panels": [
        {"svg": P1, "alt": ("운전석이 빈 채로 차가 혼자 움직이고, 관람객이 놀라서 봄", "A car moves with an empty driver's seat while a visitor watches, amazed"),
         "caption": ("자동차 시연 트랙 — 운전석이 비어 있어요.", "The demo-track car — and its driver's seat is empty."),
         "small": ("저게 어떻게 길을 보고 피해 가는 거죠?", "How does it see the road and dodge things?")},
        {"svg": P2, "alt": ("시연 담당자가 길 위에서 벌어질 수 있는 여러 돌발 상황을 나열함", "A demo staffer lists the many unpredictable things that can happen on a road"),
         "caption": ("길은 늘 다르게 생겼어요.", "The road looks different every single time."),
         "small": ("길 위 상황은 매번 달라서, 정해진 규칙만으론 못 버텨요.", "The road is different every time — a fixed rule alone can't keep up.")},
        {"svg": P3, "hero": True, "alt": ("차 옆에 눈과 뇌 모양의 그림이 떠 있고, 관람객이 흐뭇하게 지켜봄", "Eye and brain icons float beside the car while a visitor watches contentedly"),
         "caption": ("자율주행은 센서로 보고, 스스로 판단해서, 직접 운전하는 차예요.", "Autonomous driving is a car that sees the road, decides for itself, and turns the wheel."),
         "small": ("사람이 타지 않아도, 차가 끝까지 운전을 맡아요.", "Even with no one driving, the car handles the whole job."),
         "tricks": (4, [
             (EYE_I, ("보기", "See"), ("카메라·LiDAR로 주변을 봐요", "sees around it with camera, LiDAR")),
             (BRAIN2_I, ("판단하기", "Decide"), ("길·사람·신호를 가늠해요", "judges the road, people, signals"), "calm"),
             (STEER_I, ("움직이기", "Act"), ("핸들·브레이크를 직접 조작해요", "turns the wheel and brakes itself")),
             (HANDS_I, ("도움 받기", "Get help"), ("낯선 상황엔 사람 손이 필요해요", "needs a human hand in the unfamiliar"), "warm"),
         ])},
        {"svg": P4, "alt": ("보기→판단→움직이기 설명판, 안내원이 자율주행 레벨을 설명", "A see-decide-act board, with a guide explaining autonomous driving levels"),
         "caption": ("보고, 판단하고, 직접 움직여요.", "It sees, decides, and acts on its own."),
         "small": ("레벨 0(전부 사람)부터 레벨 5(전부 차)까지 나뉘어요.", "It ranges from Level 0 (all human) to Level 5 (all car).")},
        {"svg": P5, "alt": ("왼쪽: 늘 다니던 길에서 차가 안정적으로 달림. 오른쪽: 낯선 공사장 앞에서 손이 필요하다는 신호가 뜸", "Left: the car drives smoothly on a familiar road. Right: a hand icon signals it needs help at an unfamiliar construction site"),
         "caption": ("처음 보는 돌발 상황엔 아직 서툴러요.", "It's still clumsy with situations it's never seen."),
         "small": ("이럴 때는 여전히 사람의 손이 다시 필요해요.", "At that point, a human hand is still needed again.")},
    ],
    "summary": (("<b>자율주행</b> = 센서로 주변을 <b>보고</b>, 스스로 <b>판단</b>해서, 직접 핸들과 브레이크를 <b>움직이는</b> 차.",
                 "<b>Autonomous driving</b> = a car that <b>sees</b> its surroundings with sensors, <b>decides</b> for itself, and <b>acts</b> on the wheel and brakes directly."),
                ("자율주행은 카메라·LiDAR·레이더 등 센서로 주변 환경을 인식하고, AI가 상황을 판단해 조향·가속·제동을 직접 수행하는 기술이에요. SAE 기준 레벨 0(비자동)부터 레벨 5(완전자율)까지 단계가 나뉘며, 단계가 올라갈수록 사람의 개입이 줄어들어요.",
                 "Autonomous driving perceives its surroundings with sensors like cameras, LiDAR, and radar, then has AI judge the situation and directly handle steering, acceleration, and braking. The SAE scale runs from Level 0 (no automation) to Level 5 (full autonomy), with less human involvement needed at each higher level.")),
    "glossary": [
        ("LiDAR", "LiDAR", ("레이저로 거리를 정확히 재는 눈.", "The eye that measures distance exactly with lasers."), ('자율주행이 가장 많이 기대는 눈이에요. → <a href="lidar-ko.html">레이저로 거리를 재는 회전하는 눈</a>', "The eye this car relies on the most. → <a href=\"lidar-en.html\">the spinning eye that measures distance with lasers</a>")),
        ("자율주행 레벨", "Autonomous Driving Levels", ("사람 개입이 줄어드는 다섯 단계.", "Five stages where human involvement shrinks."), ("레벨 0은 전부 사람, 레벨 5는 전부 차예요.", "Level 0 is all human; Level 5 is all car.")),
        ("센서 융합", "Sensor Fusion", ("눈 여러 개의 정보를 하나로 합치는 것.", "Combining several different eyes' information into one."), ("카메라·LiDAR·레이더를 함께 써서 서로의 약점을 메워요.", "Camera, LiDAR, and radar together cover for each other's blind spots.")),
        ("CPS", "CPS", ("화면과 실제 기계가 맞물려 움직이는 것.", "Screen and real machine moving in lockstep."), ('자율주행차도 이 틀 안의 한 예시예요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', 'A self-driving car is one example living inside this bigger frame. → <a href="cps-en.html">Cyber-Physical Systems</a>')),
        ("드론 보안위협", "Drone Security Threats", ("무선 신호를 노리는 하늘의 사촌 위협.", "A sky-bound cousin threat that targets a wireless link."), ('신호 대신 센서를 더 많이 쓰는 이웃이지만, 위협은 닮아 있어요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', 'A neighbor that leans more on sensors, but faces a similar threat. → <a href="dronesecurity-en.html">the drone held up by an invisible string</a>')),
        ("정량적 위험분석", "Quantitative Risk Analysis", ("사고 확률과 피해를 숫자로 재는 방법.", "A way to score accident probability and damage with numbers."), ('자율주행차의 안전성도 이렇게 가늠해요. → <a href="quantrisk-ko.html">위험을 숫자 하나로 적는 전광판</a>', "A self-driving car's safety gets sized up the same way. → <a href=\"quantrisk-en.html\">the scoreboard that writes risk as one number</a>")),
        ("스마트팜", "Smart Farm", ("센서가 대신 돌봐주는 또 다른 현장.", "Another real-world setting where sensors take over the tending."), ("비슷한 센서로 보고 자동으로 움직인다는 생각이 밭에도 있어요. → <a href=\"smartfarm-ko.html\">센서가 돌보는 온실 부스</a>", "The same sense-and-act-automatically idea lives on a farm too. → <a href=\"smartfarm-en.html\">the greenhouse booth tended by sensors</a>")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
