from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


LINKLINE = '<path d="M0 0 L{0} {1}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4" opacity="0.7"/>'

# 1. 전시장을 처음 본 관람객 - 부스가 너무 많아서 어지러워요
P1 = svg(300, sky(300)
         + booth(60, 110, 110, 100, 0.9, "var(--accent)", None)
         + booth(190, 90, 110, 120, 0.9, "var(--good)", None)
         + booth(320, 120, 110, 90, 0.9, "#5B8DEF", None)
         + booth(450, 100, 110, 110, 0.9, "var(--bad)", None)
         + booth(580, 110, 110, 100, 0.9, "#C9822B", None)
         + person(380, 200, s=0.55, face=SWEAT, **VISITOR)
         + label(380, 288, "⟦부스가 너무 많아서, 뭐가 뭔지 모르겠어요|there are so many booths, it's hard to tell them apart⟧", 12, "var(--ink)"))

# 2. 다 다른 기술인데, 왜 한 전시장에 모아둔 거죠?
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=EYES, **VISITOR)
         + bubble(300, 65, 260, 44, "⟦로봇이랑 드론이랑 양자컴퓨터는 서로 다른 기술 아닌가요?|aren't robots, drones, and quantum computers all different things?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 265, "⟦따로 보면 안 보이는, 공통의 큰 흐름이 있어요|seen apart, you miss the big current flow they share⟧", 12, "var(--ink)"))

# 3. 4차 산업혁명 = 이 모든 부스를 잇는, 전시장 전체의 큰 흐름 (hero)
P3 = svg(340, sky(340)
         + booth(80, 150, 100, 90, 0.85, "var(--accent)", None)
         + booth(210, 130, 100, 110, 0.85, "var(--good)", None)
         + booth(340, 160, 100, 80, 0.85, "#5B8DEF", None)
         + booth(470, 140, 100, 100, 0.85, "var(--bad)", None)
         + booth(600, 150, 100, 90, 0.85, "#C9822B", None)
         + '<path d="M130 150 L260 130 L390 160 L520 140 L650 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'
         + label(380, 30, "⟦4차 산업혁명 = AI·IoT·로봇·빅데이터 같은 신기술이 한데 묶여 세상을 바꾸는 큰 흐름|4th Industrial Revolution = the big wave where AI, IoT, robotics, and big data combine to reshape the world⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦부스 하나하나가 아니라, 전시장 전체를 잇는 흐름이에요|not any single booth — it's the current running through the whole hall⟧", 12, "var(--muted)"))

# 4. 네 가지 핵심 특징
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 260, "⟦4차 산업혁명의 특징|KEY FEATURES⟧",
                     ("⟦초연결 — 모든 것이 서로 이어져요|hyper-connectivity — everything links up⟧",
                      "⟦초지능 — 기계가 스스로 판단해요|hyper-intelligence — machines judge on their own⟧",
                      "⟦융합 — 서로 다른 분야가 섞여요|convergence — different fields blend together⟧",
                      "⟦초가속 — 변화 속도가 훨씬 빨라져요|hyper-speed — change happens far faster⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 260, "⟦이 전시장의 모든 부스가, 저마다 이 네 특징을 나눠 보여줘요|every booth in this hall shows off a slice of these same four traits⟧", 11, "var(--muted)"))

# 5. 한계 - 멋있어 보여도, 전시장 밖 실전은 또 다른 이야기예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + booth(140, 100, 100, 90, 0.9, "var(--good)", None)
         + label(190, 250, "⟦전시장 데모는 늘 통제된 환경에서 보여줘요|the demo always runs in a controlled setting⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **DEMO)
         + label(570, 270, "⟦실제 공장·도로·가정은 변수가 훨씬 더 많아요|the real factory, road, or home has far more variables⟧", 11, "var(--ink)")
         + label(380, 282, "⟦흐름은 분명하지만, 데모에서 실전까지는 아직 간극이 있어요|the current is real, but the gap from demo to real life is still there⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "fourthindustry", "order": 24,
    "title": ("전시장 모든 부스를 잇는 하나의 흐름", "The One Current Running Through Every Booth"),
    "h1": ("<em>4차 산업혁명</em>이 뭐예요?", "What is the <em>4th Industrial Revolution</em>?"),
    "sub": ("4차 산업혁명을, 서로 달라 보이는 부스들을 하나로 잇는 과학관 전시장의 큰 흐름 이야기로 풀어봤어요.",
            "The 4th Industrial Revolution, told as a story about the one current running through every seemingly different booth in the science hall."),
    "panels": [
        {"svg": P1, "alt": ("관람객이 색색의 부스가 너무 많아 어지러워함", "A visitor feels overwhelmed by the many differently colored booths"),
         "caption": ("부스가 너무 많아서, 뭐가 뭔지 모르겠어요.", "There are so many booths, it's hard to tell them apart."),
         "small": ("로봇도, 드론도, 양자컴퓨터도 다 따로따로 보여요.", "Robots, drones, quantum computers — they all look completely separate.")},
        {"svg": P2, "alt": ("관람객이 로봇, 드론, 양자컴퓨터가 서로 다른 기술 아니냐고 물음", "A visitor asks whether robots, drones, and quantum computers aren't all separate things"),
         "caption": ("다 다른 기술인데, 왜 한 전시장에 모아둔 거죠?", "They're all different technologies — why are they all in one hall?"),
         "small": ("따로 보면 안 보이는, 공통의 큰 흐름이 있어요.", "Seen apart, you miss the big current flow they share.")},
        {"svg": P3, "hero": True, "alt": ("색색의 부스들이 점선 화살표로 하나로 이어짐", "The differently colored booths are all linked by one dashed arrow"),
         "caption": ("4차 산업혁명은 신기술들이 한데 묶여 세상을 바꾸는 큰 흐름이에요.", "The 4th Industrial Revolution is the big wave where new technologies combine to reshape the world."),
         "small": ("부스 하나하나가 아니라, 전시장 전체를 잇는 흐름이에요.", "Not any single booth — it's the current running through the whole hall."),
         "tricks": (4, [
             (icon('<circle cx="18" cy="18" r="8" fill="var(--accent)"/><circle cx="46" cy="18" r="8" fill="var(--accent)"/><circle cx="18" cy="46" r="8" fill="var(--accent)"/><circle cx="46" cy="46" r="8" fill="var(--accent)"/><path d="M18 18 L46 18 M18 18 L18 46 M46 18 L46 46 M18 46 L46 46 M18 18 L46 46" stroke="var(--accent)" stroke-width="2"/>'),
              ("초연결", "Hyper-connectivity"), ("모든 것이 서로 이어져요", "everything links up")),
             (icon('<rect x="14" y="16" width="36" height="32" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="26" cy="32" r="4" fill="var(--ink)"/><circle cx="38" cy="32" r="4" fill="var(--ink)"/>'),
              ("초지능", "Hyper-intelligence"), ("기계가 스스로 판단해요", "machines judge on their own"), "calm"),
             (icon('<circle cx="24" cy="32" r="16" fill="var(--accent)" opacity="0.6"/><circle cx="40" cy="32" r="16" fill="var(--good)" opacity="0.6"/>'),
              ("융합", "Convergence"), ("서로 다른 분야가 섞여요", "different fields blend together")),
             (icon('<path d="M12 44 L28 20 L40 34 L52 10" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>'),
              ("초가속", "Hyper-speed"), ("변화 속도가 훨씬 빨라져요", "change happens far faster"), "warm"),
         ])},
        {"svg": P4, "alt": ("4차 산업혁명의 네 특징 설명판: 초연결·초지능·융합·초가속", "A board lists four traits: hyper-connectivity, hyper-intelligence, convergence, hyper-speed"),
         "caption": ("초연결·초지능·융합·초가속, 이 네 가지가 핵심이에요.", "Hyper-connectivity, hyper-intelligence, convergence, hyper-speed — these four are the core."),
         "small": ("이 전시장의 모든 부스가, 저마다 이 네 특징을 나눠 보여줘요.", "Every booth in this hall shows off a slice of these same four traits.")},
        {"svg": P5, "alt": ("왼쪽: 통제된 전시장 데모 부스. 오른쪽: 실제 현장에서 당황하는 시연 담당자", "Left: a controlled demo booth in the hall. Right: a demo staffer flustered by the real-world setting"),
         "caption": ("멋있어 보여도, 전시장 밖 실전은 또 다른 이야기예요.", "As impressive as it looks, the real world outside the hall is a different story."),
         "small": ("흐름은 분명하지만, 데모에서 실전까지는 아직 간극이 있어요.", "The current is real, but the gap from demo to real life is still there.")},
    ],
    "summary": (("<b>4차 산업혁명</b> = AI·IoT·로봇·빅데이터 같은 신기술이 <b>초연결·초지능·융합·초가속</b>으로 한데 묶여 세상을 바꾸는 큰 흐름.",
                 "<b>The 4th Industrial Revolution</b> = the big wave where AI, IoT, robotics, and big data combine through <b>hyper-connectivity, hyper-intelligence, convergence, and hyper-speed</b> to reshape the world."),
                ("4차 산업혁명은 디지털·물리·생물학적 기술 경계가 융합되며 산업과 사회 전반에 큰 변화를 일으키는 흐름을 가리키는 개념이에요. 특정 기술 하나를 뜻하는 게 아니라, AI·IoT·빅데이터·로봇공학·자율주행 등 여러 신기술이 서로 연결되고 가속화되며 만들어내는 거시적 변화를 설명하는 틀이에요.",
                 "The 4th Industrial Revolution refers to a broad wave of change across industry and society as digital, physical, and biological technology boundaries blur together. It doesn't name one single technology — it's a framework describing the large-scale change created as AI, IoT, big data, robotics, autonomous driving, and more become interconnected and accelerate together.")),
    "glossary": [
        ("초연결", "Hyper-connectivity", ("모든 것이 서로 이어진 상태.", "A state where everything is linked together."), ("IoT, 5G 같은 기술이 이걸 떠받쳐요.", "Technologies like IoT and 5G hold this up.")),
        ("초지능", "Hyper-intelligence", ("기계가 스스로 판단하는 능력.", "A machine's ability to judge for itself."), ("AI가 이 특징의 핵심 엔진이에요.", "AI is the core engine behind this trait.")),
        ("융합", "Convergence", ("서로 다른 분야가 섞이는 것.", "Different fields blending together."), ("이 전시장 자체가 이 융합을 보여줘요.", "This hall itself is a display of that convergence.")),
        ("CPS", "Cyber-Physical System", ("화면과 실제 기계가 맞물려 움직이는 구조.", "The structure where screen and real machine move in lockstep."), ('4차 산업혁명을 현장에서 실제로 돌아가게 하는 틀이에요. → <a href="cps-ko.html">화면 속 쌍둥이와 함께 움직이는 기계팔</a>', 'The structure that actually runs the 4th revolution on the ground. → <a href="cps-en.html">the mechanical arm that moves with its screen twin</a>')),
        ("자율주행", "Autonomous Driving", ("이 흐름이 도로 위에 나타난 모습.", "What this current looks like out on the road."), ('이 부스도 전시장 전체 흐름의 한 조각이에요. → <a href="autodrive-ko.html">운전석이 비어 있는 시연 트랙의 차</a>', "This booth, too, is one piece of the hall's larger current. → <a href=\"autodrive-en.html\">the demo-track car with an empty driver's seat</a>")),
        ("양자 컴퓨팅", "Quantum Computing", ("이 흐름 속 가장 낯선 계산 방식.", "The strangest kind of computing inside this current."), ('전시장 끝자락, 가장 생소한 부스예요. → <a href="quantumcompute-ko.html">동시에 앞뒤인 신기한 동전 부스</a>', 'The strangest booth near the far end of the hall. → <a href="quantumcompute-en.html">the booth where the coin is heads and tails at once</a>')),
        ("RPA", "RPA", ("반복 업무를 대신하는 작은 변화의 조각.", "One small-scale piece of this bigger wave of automation."), ('거창해 보이는 흐름도 결국 이런 작은 자동화들이 모인 거예요. → <a href="rpa-ko.html">규칙대로만 반복하는 로봇 직원</a>', 'Even this grand current is, in the end, built from small automations like this one. → <a href="rpa-en.html">the robot worker that only repeats the rule</a>')),
        ("핀테크", "Fintech", ("전시장을 나서며 보는 마지막 흐름.", "The last current you pass on the way out of the hall."), ('전시장 관람을 마무리하는 부스예요. → <a href="fintech-ko.html">핀테크·간편결제</a>', 'The booth that wraps up the visit. → <a href="fintech-en.html">Fintech & simple payment</a>')),
    ],
}
