from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


def arm(x, y, s=1.0, bent=False):
    ang = -30 if bent else 0
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="-10" y="40" width="20" height="24" rx="4" fill="#5A6472"/>'
            f'<g transform="rotate({ang})"><rect x="-6" y="-48" width="12" height="52" rx="5" fill="#8A8A8A"/></g>'
            f'<circle r="9" fill="var(--accent)"/></g>')


SENSOR2_P = '<circle cx="32" cy="32" r="16" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="32" r="5" fill="var(--accent)"/>'
LOOP_P = '<path d="M18 24 a14 14 0 1 1 -2 16" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M24 43 l-9 2 l3 -9z" fill="var(--good)"/>'
CMD_P = '<rect x="12" y="20" width="40" height="24" rx="4" fill="#1B2A44"/><path d="M20 32 l6 -6 l6 6 M38 26 h8" stroke="var(--accent)" stroke-width="3" fill="none"/>'
SENSOR2_I, LOOP_I, CMD_I = icon(SENSOR2_P), icon(LOOP_P), icon(CMD_P)
SCREEN_ARM = f'<g transform="translate(26,8) scale(0.3)">{arm(0, 0)}</g>'

# 1. 화면 속 로봇팔, 그냥 애니메이션 아니에요?
P1 = svg(300, sky(300)
         + screen(300, 100, 1.6, SCREEN_ARM)
         + person(600, 170, s=0.7, face=EYES, **VISITOR)
         + label(380, 280, "⟦화면 속에서만 움직이면, 그냥 애니메이션이랑 똑같은데요?|if it only moves on screen, isn't that just an animation?⟧", 12, "var(--ink)"))

# 2. 화면과 진짜 기계가 따로 놀면 소용없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + screen(180, 90, 1.3, SCREEN_ARM)
         + arm(560, 180, 1.1, bent=False)
         + person(440, 150, s=0.8, face=FROWN, **DEMO)
         + label(380, 270, "⟦화면에서는 팔을 굽혔는데, 진짜 기계팔은 그대로 멈춰 있어요|the screen bends the arm, but the real arm just sits there unmoved⟧", 12, "var(--ink)"))

# 3. CPS = 화면 속 쌍둥이와 진짜 기계가 서로 맞물려 움직이는 시스템 (hero)
P3 = svg(340, sky(340)
         + screen(240, 90, 1.5, SCREEN_ARM)
         + arm(560, 190, 1.3, bent=True)
         + glyph(470, 140, 0.8, LOOP_P)
         + person(660, 255, s=0.55, face=SMILE, **GUIDE)
         + label(380, 30, "⟦CPS = 화면 속 디지털 쌍둥이와 실제 기계가 센서·신호로 서로 맞물려 움직이는 시스템|CPS = a digital twin on screen and a real machine, locked together by sensors and signals⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦화면이 바뀌면 기계가 움직이고, 기계가 움직이면 화면도 다시 바뀌어요|change the screen and the machine moves — move the machine and the screen updates too⟧", 12, "var(--muted)"))

# 4. 신호가 도는 순서(닫힌 고리)
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 260, "⟦신호가 도는 순서|THE CLOSED LOOP⟧",
                     ("⟦① 센서가 진짜 기계의 상태를 읽어요|① a sensor reads the real machine's state⟧",
                      "⟦② 그 상태가 화면 속 쌍둥이에 비춰져요|② that state is mirrored on the screen twin⟧",
                      "⟦③ 컴퓨터가 계산해서 다음 명령을 내려요|③ a computer calculates the next command⟧",
                      "⟦④ 명령이 실제 기계를 움직여요, 다시 ①로|④ the command moves the real machine, back to ①⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦이 돌고 도는 고리를 '피드백 루프'라고 불러요|this loop that keeps circling is called a feedback loop⟧", 11, "var(--muted)"))

# 5. 한계 - 신호가 늦거나 뚫리면, 쌍둥이와 실제가 어긋나요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + screen(166, 90, 1.0, SCREEN_ARM) + arm(300, 190, 0.9, bent=True)
         + label(230, 260, "⟦신호가 빠르면, 쌍둥이와 기계가 똑같이 움직여요|with a fast signal, the twin and the machine move as one⟧", 11, "var(--ink)")
         + screen(546, 90, 1.0, SCREEN_ARM) + arm(680, 190, 0.9, bent=False)
         + label(610, 260, "⟦신호가 늦거나 뚫리면, 화면과 실제가 서로 어긋나 버려요|a late or hacked signal, and screen and reality drift apart⟧", 11, "var(--ink)")
         + label(380, 282, "⟦보이는 화면만큼이나, 신호의 속도와 안전이 중요해요|the signal's speed and safety matter just as much as what's on screen⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "cps", "order": 23,
    "title": ("화면 속 쌍둥이와 함께 움직이는 기계팔", "The Mechanical Arm That Moves With Its Screen Twin"),
    "h1": ("<em>사이버물리시스템(CPS)</em>이 뭐예요?", "What is a <em>Cyber-Physical System (CPS)</em>?")
    ,
    "sub": ("CPS를, 화면 속 쌍둥이와 진짜 기계팔이 서로 맞물려 움직이는 전시 부스 이야기로 풀어봤어요.",
            "Cyber-Physical Systems, told as a story about a booth where a screen twin and a real mechanical arm move in lockstep."),
    "panels": [
        {"svg": P1, "alt": ("화면 속에서 로봇팔이 움직이고, 관람객이 애니메이션 아니냐고 물음", "A robot arm moves on screen while a visitor asks if it's just an animation"),
         "caption": ("화면 속 로봇팔, 그냥 애니메이션 아니에요?", "Isn't that robot arm on screen just an animation?"),
         "small": ("화면 속에서만 움직이면, 그냥 애니메이션이랑 똑같은데요?", "If it only moves on screen, isn't that just an animation?")},
        {"svg": P2, "alt": ("화면 속 팔은 굽혀졌는데 실제 기계팔은 그대로 멈춰 있어 시연 담당자가 당황함", "The screen's arm bends while the real arm stays frozen, confusing the demo staffer"),
         "caption": ("화면과 진짜 기계가 따로 놀면 소용없어요.", "It's no good if the screen and the real machine move independently."),
         "small": ("화면에서는 팔을 굽혔는데, 진짜 기계팔은 그대로 멈춰 있어요.", "The screen bends the arm, but the real arm just sits there unmoved.")},
        {"svg": P3, "hero": True, "alt": ("화면 속 쌍둥이 팔과 진짜 기계팔이 화살표로 이어진 채 똑같이 구부러짐", "The screen twin's arm and the real arm bend identically, linked by a looping arrow"),
         "caption": ("CPS는 화면 속 쌍둥이와 진짜 기계가 서로 맞물려 움직이는 시스템이에요.", "A CPS is a digital twin on screen and a real machine, locked together by sensors and signals."),
         "small": ("화면이 바뀌면 기계가 움직이고, 기계가 움직이면 화면도 다시 바뀌어요.", "Change the screen and the machine moves — move the machine and the screen updates too."),
         "tricks": (4, [
             (SENSOR2_I, ("상태 읽기", "Read the state"), ("진짜 기계를 센서로 읽어요", "a sensor reads the real machine")),
             (LOOP_I, ("화면에 비추기", "Mirror on screen"), ("그 상태를 쌍둥이에 비춰요", "mirrors it onto the twin"), "calm"),
             (CMD_I, ("계산해서 명령하기", "Calculate a command"), ("다음에 뭘 할지 정해요", "decides what happens next")),
             (SENSOR2_I, ("실제로 움직이기", "Act in reality"), ("명령이 진짜 기계를 움직여요", "the command moves the real machine"), "warm"),
         ])},
        {"svg": P4, "alt": ("신호가 도는 순서 설명판: 읽기→비추기→계산→움직이기, 다시 읽기로", "A board shows the loop: read, mirror, calculate, act, back to read"),
         "caption": ("신호는 한 바퀴를 돌아 다시 처음으로 와요.", "The signal makes a full circle and comes back to the start."),
         "small": ("이 돌고 도는 고리를 '피드백 루프'라고 불러요.", "This loop that keeps circling is called a feedback loop.")},
        {"svg": P5, "alt": ("왼쪽: 빠른 신호로 화면과 기계가 똑같이 움직임. 오른쪽: 늦은 신호로 둘이 어긋남", "Left: a fast signal keeps screen and machine in sync. Right: a delayed signal lets them drift apart"),
         "caption": ("신호가 늦거나 뚫리면, 쌍둥이와 실제가 어긋나요.", "A late or hacked signal lets the twin and reality drift apart."),
         "small": ("보이는 화면만큼이나, 신호의 속도와 안전이 중요해요.", "The signal's speed and safety matter just as much as what's on screen.")},
    ],
    "summary": (("<b>CPS</b> = <b>센서</b>로 읽은 실제 상태를 <b>화면(디지털 트윈)</b>에 비추고, 그 판단으로 <b>진짜 기계</b>를 다시 움직이는 닫힌 고리 시스템.",
                 "<b>CPS</b> = a closed-loop system that mirrors a <b>sensor</b>-read real state onto a <b>screen (digital twin)</b>, then uses that judgment to move the <b>real machine</b> again."),
                ("사이버물리시스템(Cyber-Physical System)은 센서·네트워크·컴퓨팅이 물리적 기계·설비와 실시간으로 연결되어, 감지·판단·제어가 하나의 피드백 루프로 돌아가는 시스템이에요. 디지털 트윈은 이 CPS의 '화면' 역할을 하는 가상 모형이고, 스마트팩토리·자율주행·스마트팜 등 대부분의 신기술 현장 응용이 CPS 구조 위에서 동작해요.",
                 "A Cyber-Physical System links sensors, networks, and computing to physical machinery in real time, so that sensing, deciding, and controlling run as one continuous feedback loop. A digital twin is the virtual model that plays the 'screen' role in a CPS, and most real-world applications of new technology — smart factories, autonomous driving, smart farms — run on this same CPS structure.")),
    "glossary": [
        ("디지털 트윈", "Digital Twin", ("실제를 그대로 옮긴 화면 속 쌍둥이.", "The screen twin that mirrors the real thing exactly."), ("CPS에서 '화면' 역할을 맡아요.", "It plays the 'screen' role inside a CPS.")),
        ("피드백 루프", "Feedback Loop", ("돌고 도는 신호의 고리.", "The signal's loop that keeps circling back."), ("CPS가 멈추지 않고 계속 작동하는 이유예요.", "The reason a CPS keeps running without stopping.")),
        ("엣지컴퓨팅", "Edge Computing", ("현장에서 바로 판단하는 작은 컴퓨터.", "The small computer that decides right there on the spot."), ('이 전시장 다른 부스에서도 같은 원리가 나와요. → <a href="ambientcompute-ko.html">말 안 해도 알아서 척척인 전시관</a>', 'The same idea shows up at another booth in this hall. → <a href="ambientcompute-en.html">the exhibit that just knows</a>')),
        ("자율주행", "Autonomous Driving", ("CPS 구조가 달리는 대표적인 현장.", "A prime real-world venue where this CPS structure runs."), ('보기·판단·움직이기가 똑같이 적용돼요. → <a href="autodrive-ko.html">운전석이 비어 있는 시연 트랙의 차</a>', "The same see-decide-act loop applies there too. → <a href=\"autodrive-en.html\">the demo-track car with an empty driver's seat</a>")),
        ("스마트팜", "Smart Farm", ("CPS 구조가 돌아가는 또 다른 현장.", "Another real-world venue where this same CPS loop runs."), ('센서가 재고 기계가 돌보는 것도 같은 고리예요. → <a href="smartfarm-ko.html">센서가 돌보는 온실 부스</a>', 'Sensors measuring and machines tending run on the same loop. → <a href="smartfarm-en.html">the greenhouse booth tended by sensors</a>')),
        ("드론 보안위협", "Drone Security Threats", ("신호가 뚫리면 위험해지는 비슷한 예.", "A similar case where a hacked signal turns dangerous."), ('이 고리의 신호가 공격받으면 어떻게 되는지 보여줘요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', "It shows what happens when this loop's signal is attacked. → <a href=\"dronesecurity-en.html\">the drone held up by an invisible string</a>")),
        ("RPA", "RPA", ("화면 안에서만 반복하는 로봇.", "A robot that only repeats inside the screen."), ('이쪽은 화면 밖, 실제 기계까지 움직여요. → <a href="rpa-ko.html">규칙대로만 반복하는 로봇 직원</a>', "This one moves beyond the screen into the real machine. → <a href=\"rpa-en.html\">the robot worker that only repeats the rule</a>")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
