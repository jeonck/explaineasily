from _draw import *
from _world import *


def gripper_arm(x, y, s=1.0, open_claw=True, color="#5B8DEF"):
    """로봇 팔 + 집게. (x,y) 는 집게 끝 기준점."""
    gap = 14 if open_claw else 4
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="-6" y="-70" width="12" height="55" fill="{color}"/>'
            f'<circle cx="0" cy="-70" r="10" fill="{color}"/>'
            f'<path d="M-{gap} 0 L-{gap - 6} -16 L-2 -16" stroke="{color}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M{gap} 0 L{gap - 6} -16 L2 -16" stroke="{color}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'</g>')


# 1. 사진으로 분류만 하던 눈이, 이제 직접 집어서 옮기래요
P1 = svg(300, sky(300)
         + conveyor(80, 220, 300)
         + produce(230, 188, 1.4, "var(--good)")
         + gripper_arm(230, 150, 1.0, open_claw=False, color="var(--bad)")
         + label(230, 260, "⟦너무 세게 쥐어서 터졌어요|squeezed too hard — it burst⟧", 11, "var(--bad)")
         + person(560, 170, s=0.75, face=SWEAT + EYES, **OPERATOR)
         + label(560, 270, "⟦사진으로 보던 거랑 또 다르네요|this is different from just looking at a photo⟧", 11, "var(--muted)")
         + label(380, 25, "⟦사진으로 분류만 하던 눈이, 이제 직접 집어서 옮기래요|an eye that used to just classify photos is now asked to pick things up itself⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 실제 세계엔 무게·마찰·타이밍이 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(190, 100, "⟦사진 속 세계|the world inside a photo⟧", 12, "var(--ink)", cls="d")
         + produce(190, 170, 1.3, "var(--good)")
         + label(190, 230, "⟦무게도 마찰도 없어요|no weight, no friction⟧", 11, "var(--muted)")
         + label(570, 100, "⟦진짜 검사장|the real inspection station⟧", 12, "var(--ink)", cls="d")
         + produce(570, 170, 1.3, "var(--good)")
         + label(570, 230, "⟦무게·마찰·타이밍이 다 있어요|weight, friction, and timing, all at once⟧", 11, "var(--bad)")
         + label(380, 280, "⟦사진 속 세계와 다르게, 진짜 세계는 무게·마찰·타이밍까지 다뤄야 해요|unlike the world inside a photo, the real world demands handling weight, friction, and timing too⟧", 12, "var(--ink)", cls="d"))

# 3. 피지컬 AI = 보고 판단하는 AI에 느끼고 움직이는 능력을 더한 것 (hero)
P3 = svg(340, sky(340)
         + label(380, 25, "⟦피지컬 AI = 보고 판단하는 AI에, 느끼고 움직이는 능력을 더한 것이에요|physical AI adds sensing and moving to an AI that already sees and judges⟧", 13, "var(--ink)", cls="d")
         + conveyor(220, 230, 320)
         + produce(380, 198, 1.3, "var(--good)")
         + gripper_arm(380, 150, 1.1, open_claw=True)
         + f'<path d="M460 120 Q 520 90, 460 180" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="4 3" marker-end="url(#pfa)"/>'
         + '<defs><marker id="pfa" markerWidth="8" markerHeight="8" refX="5" refY="2.5" orient="auto"><path d="M0 0 L5 2.5 L0 5 Z" fill="var(--accent)"/></marker></defs>'
         + label(560, 140, "⟦보고 → 느끼고 → 다시 보기|see → feel → look again⟧", 11, "var(--muted)")
         + label(380, 300, "⟦지각 → 판단 → 행동을 쉬지 않고 반복하는 몸을 가진 AI예요|an AI with a body, cycling through sense, decide, and act — without a pause⟧", 12, "var(--muted)"))

SENSE_I = icon('<circle cx="32" cy="32" r="10" fill="var(--accent)"/><path d="M14 32 a18 18 0 0 1 36 0" stroke="var(--accent)" stroke-width="3" fill="none"/>')
LOOP_I = icon('<path d="M46 20 A18 18 0 1 0 46 46" stroke="var(--good)" stroke-width="4" fill="none"/><path d="M46 12 v12 h-12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
FORCE_I = icon('<rect x="14" y="26" width="36" height="12" rx="4" fill="var(--accent-soft)"/><path d="M20 32 h24" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
STOP_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)"/><rect x="24" y="24" width="16" height="16" fill="#FFF8E7"/>')

PAGE = {
    "slug": "physicalai", "order": 11,
    "title": ("사진만 보던 눈이 팔다리를 얻다", "The Eye That Used to Just Look Grows Arms and Legs"),
    "h1": ("<em>피지컬 AI</em>가 뭐예요?", "What is <em>Physical AI</em>?"),
    "sub": ("피지컬 AI를, 사진으로 분류만 하던 선별기가 직접 몸으로 집고 옮기게 되는 이야기로 풀어봤어요.",
            "Physical AI, told as a story about a sorter that used to just classify photos, now given a body to pick things up and move them itself."),
    "panels": [
        {"svg": P1, "alt": ("로봇 집게가 사과를 너무 세게 쥐어 터뜨리고, 선별기 조작원이 사진으로 보던 것과 다르다며 진땀을 흘림", "A robot gripper squeezes an apple too hard and bursts it, while the operator sweats, noting it's different from just looking at a photo"),
         "caption": ("사진으로 분류만 하던 눈이, 이제 직접 집어서 옮기래요.", "An eye that used to just classify photos is now asked to pick things up."),
         "small": ("너무 세게 쥐어서 터졌어요.", "It squeezed too hard — and the apple burst.")},
        {"svg": P2, "alt": ("사진 속 사과는 무게도 마찰도 없지만, 진짜 검사장의 사과는 무게·마찰·타이밍을 모두 가짐", "The apple inside a photo has no weight or friction, while the one in the real station carries weight, friction, and timing all at once"),
         "caption": ("사진 속 세계와 진짜 세계는 달라요.", "The world inside a photo and the real world aren't the same."),
         "small": ("진짜 세계는 무게·마찰·타이밍까지 다뤄야 해요.", "The real world demands handling weight, friction, and timing too.")},
        {"svg": P3, "hero": True, "alt": ("집게가 사과를 집으며, 보고 느끼고 다시 보는 화살표 루프가 옆에 그려짐", "A gripper picks up an apple while a looping arrow beside it reads see, feel, look again"),
         "caption": ("보고 판단하는 AI에, 느끼고 움직이는 능력을 더한 것이에요.", "It adds sensing and moving to an AI that already sees and judges."),
         "small": ("지각→판단→행동을 쉬지 않고 반복하는, 몸을 가진 AI예요.", "An AI with a body, cycling through sense, decide, and act without a pause."),
         "tricks": (4, [
             (SENSE_I, ("센서로 느끼기", "Sense with sensors"), ("촉각·힘·거리를 직접 느껴요", "feeling touch, force, and distance directly"), "calm"),
             (LOOP_I, ("실시간으로 다시 보기", "Loop back in real time"), ("움직이며 계속 다시 확인해요", "checking again and again while moving")),
             (FORCE_I, ("알맞은 힘 조절하기", "Tune the right amount of force"), ("너무 세지도 약하지도 않게요", "not too hard, not too soft"), "warm"),
             (STOP_I, ("안전하게 멈추기", "Stop safely"), ("이상하면 즉시 멈춰요(비상정지)", "an emergency stop the instant something's off")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦화면 속 AI vs 피지컬 AI|SCREEN-BOUND AI vs PHYSICAL AI⟧",
                 ("⟦화면 속 AI — 사진·숫자를 보고 분류·판정만 함|screen-bound AI — classifies and judges photos and numbers⟧",
                  "⟦피지컬 AI — 센서로 느끼고, 모터로 실제로 움직임|physical AI — senses with sensors, moves with real motors⟧",
                  "⟦화면 속 AI — 틀려도 다시 계산하면 끝|screen-bound AI — a mistake just means recalculating⟧",
                  "⟦피지컬 AI — 틀리면 작물이 터지거나 사람이 다칠 수 있음|physical AI — a mistake can burst produce or hurt a person⟧"), 1.0)),
         "alt": ("화면 속 AI와 피지컬 AI를 비교한 표", "A board comparing screen-bound AI with physical AI"),
         "caption": ("화면 안에서 끝나는 AI와, 몸으로 결과를 내는 AI는 달라요.", "An AI that stays on screen is different from one that acts out its results in the real world."),
         "small": ("실수의 결과가 되돌릴 수 없을 때, 안전장치는 선택이 아니라 필수예요.", "When a mistake can't be undone, safeguards aren't optional — they're required.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                 + gripper_arm(190, 140, 1.0) + produce(190, 188, 1.1, "var(--good)") + label(190, 250, "⟦CNN의 눈을 그대로 빌려 써요|borrows the same CNN eye, unchanged⟧", 11, "var(--ink)")
                 + person(570, 150, s=0.75, face=EYES, **INSPECTOR) + label(570, 250, "⟦생명·안전과 닿으면 고영향 AI예요|touching life or safety makes it high-impact AI⟧", 11, "var(--ink)")
                 + label(380, 282, "⟦피지컬 AI는 몸이 생명·안전과 직접 닿기 때문에, 법·안전 기준이 한층 더 엄격해져요|because a physical body touches life and safety directly, the legal and safety bar rises accordingly⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 집게가 CNN의 눈을 그대로 쓴다는 설명. 오른쪽: 검수반장이 생명·안전과 닿으면 고영향 AI라고 말함", "Left: a note that the gripper borrows the same CNN eye. Right: the inspector notes that touching life or safety makes it high-impact AI"),
         "caption": ("보는 눈은 그대로, 다만 몸이 더해져요.", "The eye stays the same — only a body gets added."),
         "small": ("몸이 생명·안전과 직접 닿기 때문에, 법·안전 기준이 한층 더 엄격해져요.", "Because a physical body touches life and safety directly, the legal and safety bar rises accordingly.")},
    ],
    "summary": (("<b>피지컬 AI</b> = 보고 판단하는 AI에 <b>센서로 느끼고 몸으로 움직이는</b> 능력을 더한 것.",
                 "<b>Physical AI</b> = an AI that already sees and judges, with <b>sensing and physical movement</b> added on top."),
                ("피지컬 AI(Physical AI)는 카메라·센서로 주변을 지각하고, 그 판단을 실제 모터·액추에이터로 물리적 행동(이동, 조작, 조작력 조절)으로 옮기는 AI예요. 지각(Perception)→판단(Decision)→행동(Action)의 루프를 실시간으로 반복하고, 화면 속 AI와 달리 무게·마찰·지연 같은 물리 법칙과 실시간 안전(비상정지, 힘 제한)을 함께 다뤄야 해요. 로봇공학·자율주행·산업용 로봇팔 등이 대표적인 예고, 생명·안전에 직접 영향을 미치는 경우가 많아 고영향 AI 규제와 자주 맞닿아요.",
                 "Physical AI perceives its surroundings through cameras and sensors, then carries that judgment out through real motors and actuators as physical action — moving, manipulating, modulating force. It loops through perception, decision, and action in real time, and unlike a screen-bound AI, it must also handle the laws of physics — weight, friction, latency — alongside real-time safety measures like emergency stops and force limits. Robotics, autonomous driving, and industrial robot arms are classic examples, and because they so often touch life and safety directly, they frequently brush up against high-impact AI regulation.")),
    "glossary": [
        ("피지컬 AI", "Physical AI", ("사진만 보던 눈이 팔다리를 얻은 것.", "An eye that used to just look, now given arms and legs."), ("지각→판단→행동 루프를 실시간으로 돌려요.", "Cycles through sense, decide, act — all in real time.")),
        ("지각-판단-행동 루프", "Perception-decision-action loop", ("보고, 정하고, 움직이는 걸 쉬지 않고 반복하는 것.", "Seeing, deciding, and moving — on an unbroken repeat."), ("피지컬 AI의 가장 기본적인 작동 구조예요.", "The most basic operating structure of physical AI.")),
        ("CNN", "CNN", ("피지컬 AI가 빌려 쓰는 보는 눈.", "The seeing eye physical AI borrows."), ('화면 속 분류에서 쓰던 바로 그 방법이에요. → <a href="cnn-ko.html">작은 창으로 조금씩 살펴보는 눈</a>', 'The very same method used for screen-bound classification. → <a href="cnn-en.html">The Eye That Scans Through a Small Window</a>')),
        ("액추에이터", "Actuator", ("판단을 실제 움직임으로 바꾸는 모터.", "The motor that turns a decision into real movement."), ("집게·팔다리를 실제로 움직이는 부분이에요.", "The part that actually moves the gripper or limb.")),
        ("힘 제한·비상정지", "Force limiting & e-stop", ("너무 세게 쥐거나 부딪히면 즉시 멈추는 안전장치.", "A safeguard that stops everything the instant it grips or hits too hard."), ("되돌릴 수 없는 실수를 막는 핵심 장치예요.", "The core safeguard against a mistake that can't be undone.")),
        ("고영향 AI", "High-impact AI", ("생명·안전에 직접 닿는 AI 분류.", "The classification for AI that touches life and safety directly."), ('몸을 가진 AI는 이쪽으로 분류되기 쉬워요. → <a href="aibasiclaw-ko.html">나라가 정한 최소 등급 기준</a>', 'An AI with a body is especially likely to fall into this category. → <a href="aibasiclaw-en.html">The Minimum Grading Rule the Country Itself Sets</a>')),
        ("시뮬레이션 학습", "Simulation training", ("진짜 작물을 터뜨리기 전에, 가짜 환경에서 먼저 연습하는 것.", "Practicing in a fake environment before ever bursting a real piece of produce."), ("실수의 비용이 큰 피지컬 AI에서 특히 중요해요.", "Especially important when physical AI's mistakes are this costly.")),
        ("혼동행렬", "Confusion matrix", ("피지컬 AI의 판단 성능도 이 표로 확인해요.", "Physical AI's own judgment is checked the same way, with this table."), ('다만 틀렸을 때의 대가가 훨씬 더 커요. → <a href="confmatrix-ko.html">네 칸으로 나눈 도장 기록부</a>', "Only the cost of being wrong runs much higher. → <a href=\"confmatrix-en.html\">The Four-Box Stamp Ledger</a>")),
    ],
}
