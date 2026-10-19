from _draw import *
from _world import *

SENSOR_P = ('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--accent)" stroke-width="4"/>'
            '<circle cx="32" cy="32" r="6" fill="var(--accent)"/>'
            '<path d="M32 8 v8 M32 48 v8 M8 32 h8 M48 32 h8" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
BRAIN_P = ('<rect x="14" y="16" width="36" height="32" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           '<circle cx="26" cy="32" r="4" fill="var(--ink)"/><circle cx="38" cy="32" r="4" fill="var(--ink)"/>'
           '<path d="M20 24 h24 M20 40 h24" stroke="#C9A86A" stroke-width="2"/>')
LIGHT_P = ('<path d="M32 10 a16 16 0 0 1 10 29 v6 h-20 v-6 a16 16 0 0 1 10 -29z" fill="var(--accent)"/>'
           '<rect x="26" y="46" width="12" height="8" rx="2" fill="#8A8A8A"/>')
GHOST_P = '<path d="M20 50 V28 a12 12 0 0 1 24 0 v22 l-6 -6 l-6 6 l-6 -6z" fill="none" stroke="var(--good)" stroke-width="4"/>'
SENSOR_I, BRAIN_I, LIGHT_I, GHOST_I = icon(SENSOR_P), icon(BRAIN_P), icon(LIGHT_P), icon(GHOST_P)


def glyph(x, y, s, inner):
    """패널 SVG 안에 직접 박는 작은 그림(아이콘을 nested <svg>로 끼우면 XML 파싱이 깨져서, <g>로 대신 그린다)."""
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'

# 1. 어두운 부스 앞에서 스위치를 못 찾아요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=FROWN + SWEAT, **VISITOR)
         + booth(360, 90, 220, 140, 1.0, "var(--stone-dark)", None)
         + label(380, 250, "⟦부스가 깜깜해서 뭐가 있는지도 안 보여요|the booth is dark — can't even tell what's inside⟧", 12, "var(--bad)")
         + label(380, 280, "⟦스위치를 찾아 더듬거리느라 체험할 시간이 줄어요|fumbling for the switch eats into the actual visit⟧", 12, "var(--ink)"))

# 2. 부스마다 매번 버튼을 눌러야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=SWEAT, **VISITOR)
         + bubble(70, 70, 200, 40, "⟦또 버튼 누르고, 또 설정하고...|press this button, set that option, again...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=FROWN, **GUIDE)
         + bubble(460, 70, 220, 40, "⟦부스 열 개면 버튼도 열 번이에요|ten booths means pressing ten buttons⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사람이 기계에 매번 맞춰줘야 하면 피곤해요|it's tiring when the person always has to adjust to the machine⟧", 12, "var(--ink)"))

# 3. 앰비언트 컴퓨팅 = 다가가면 알아서 맞춰주는 전시관 (hero)
P3 = svg(340, sky(340)
         + booth(260, 70, 240, 150, 1.0, "var(--good)", None)
         + glyph(354, 54, 0.75, SENSOR_P)
         + person(200, 190, s=0.8, face=SMILE, **VISITOR)
         + label(380, 30, "⟦앰비언트 컴퓨팅 = 사람이 다가가면 환경이 알아서 바뀌어요|ambient computing = the space changes itself as you approach⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦말도, 버튼도 필요 없어요 — 센서가 대신 알아차려요|no words, no buttons — sensors notice for you⟧", 12, "var(--muted)"))

# 4. 어떻게 알아차리나요?
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦작동 순서|HOW IT WORKS⟧",
                     ("⟦① 센서가 사람·움직임을 느껴요|① sensors notice people and movement⟧",
                      "⟦② 작은 컴퓨터가 현장에서 바로 판단해요|② a small computer decides right there⟧",
                      "⟦③ 조명·화면·소리가 자동으로 바뀌어요|③ lights, screens, sound change by themselves⟧",
                      "⟦④ 사람은 그냥 전시를 즐기면 돼요|④ the visitor just enjoys the exhibit⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **DEMO)
         + label(560, 250, "⟦'현장에서 바로' 판단하는 걸 엣지컴퓨팅이라고 불러요|deciding right there, on the spot, is called edge computing⟧", 11, "var(--muted)")
         + label(380, 300, "⟦이 전시관 안의 모든 부스가 이렇게 연결돼 있어요|every booth in this hall is wired up this way⟧", 12, "var(--ink)"))

# 5. 한계 - 조용히 지켜보는 거라 꺼림칙할 수 있고, 전기가 끊기면 멈춰요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **VISITOR) + glyph(150, 60, 0.6, GHOST_P)
         + label(190, 250, "⟦몰래 지켜보는 느낌이 들 수 있어요|it can feel like you're quietly being watched⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **DEMO) + booth(540, 200, 60, 50, 0.9, "var(--stone-dark)", None)
         + label(570, 270, "⟦전기·센서가 멈추면 그냥 평범한 부스예요|if power or sensors fail, it's just an ordinary booth⟧", 11, "var(--ink)")
         + label(380, 282, "⟦똑똑해 보여도, 결국 센서와 전기에 기대는 기술이에요|clever as it looks, it still depends on sensors and power⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ambientcompute", "order": 14,
    "title": ("말 안 해도 알아서 척척인 전시관", "The Exhibit That Just Knows, Unasked"),
    "h1": ("<em>앰비언트 컴퓨팅</em>이 뭐예요?", "What is <em>Ambient Computing</em>?"),
    "sub": ("앰비언트 컴퓨팅을, 다가가면 알아서 불이 켜지는 과학관 부스 이야기로 풀어봤어요.",
            "Ambient computing, told as a story about a science-hall booth that lights up the moment you approach."),
    "panels": [
        {"svg": P1, "alt": ("관람객이 깜깜한 부스 앞에서 스위치를 찾지 못해 진땀을 흘림", "A visitor sweats, unable to find the switch in front of a dark booth"),
         "caption": ("부스가 깜깜해서 뭐가 있는지도 안 보여요.", "The booth is dark — you can't even tell what's inside."),
         "small": ("스위치를 찾아 더듬거리느라 체험할 시간이 줄어요.", "Fumbling for the switch eats into the actual visit.")},
        {"svg": P2, "alt": ("관람객과 안내원이 부스마다 버튼을 눌러야 해서 지침", "A visitor and a guide, both tired of pressing a button at every booth"),
         "caption": ("부스마다 매번 버튼을 눌러야 해요.", "You have to press a button at every single booth."),
         "small": ("사람이 기계에 매번 맞춰줘야 하면 피곤해요.", "It's tiring when the person always has to adjust to the machine.")},
        {"svg": P3, "hero": True, "alt": ("관람객이 다가가자 부스에 센서가 반응해 불이 켜짐", "As a visitor approaches, a sensor on the booth reacts and the lights turn on"),
         "caption": ("앰비언트 컴퓨팅은 다가가면 환경이 알아서 바뀌는 거예요.", "Ambient computing means the space changes itself as you approach."),
         "small": ("말도, 버튼도 필요 없어요 — 센서가 대신 알아차려요.", "No words, no buttons — sensors notice for you."),
         "tricks": (4, [
             (SENSOR_I, ("느끼기", "Sense"), ("사람·움직임을 느껴요", "notices people and motion")),
             (BRAIN_I, ("판단하기", "Decide"), ("그 자리에서 바로요", "right there, on the spot"), "calm"),
             (LIGHT_I, ("반응하기", "React"), ("조명·화면이 바뀌어요", "lights and screens change")),
             (GHOST_I, ("드러나지 않기", "Stay invisible"), ("기술이 안 보여야 성공이에요", "success means the tech disappears"), "warm"),
         ])},
        {"svg": P4, "alt": ("작동 순서 설명판: 느끼기→판단하기→반응하기→즐기기. 시연 담당자가 엣지컴퓨팅을 설명", "An info board shows sense → decide → react → enjoy; a demo staffer explains edge computing"),
         "caption": ("센서가 느끼고, 현장에서 바로 판단해 반응해요.", "Sensors sense, decide right there, and react."),
         "small": ("'현장에서 바로' 판단하는 걸 엣지컴퓨팅이라고 불러요.", "Deciding right there, on the spot, is called edge computing.")},
        {"svg": P5, "alt": ("왼쪽: 관람객이 몰래 지켜보는 느낌을 받음. 오른쪽: 전기가 끊기면 평범한 부스가 됨", "Left: a visitor feels quietly watched. Right: with no power, it's just an ordinary booth"),
         "caption": ("앰비언트 컴퓨팅에도 한계는 있어요.", "Ambient computing has its limits too."),
         "small": ("똑똑해 보여도, 결국 센서와 전기에 기대는 기술이에요.", "Clever as it looks, it still depends on sensors and power.")},
    ],
    "summary": (("<b>앰비언트 컴퓨팅</b> = 사람이 다가가면 <b>센서와 작은 컴퓨터</b>가 알아서 환경을 바꿔주는, '보이지 않는' 기술.",
                 "<b>Ambient computing</b> = sensors and small computers that change your environment for you, staying invisible as technology."),
                ("앰비언트 컴퓨팅은 센서·IoT 기기·엣지컴퓨팅이 사람의 존재와 상황을 감지해, 명시적 조작 없이도 조명·온도·안내 등 주변 환경이 스스로 반응하도록 하는 패러다임이에요. 기술이 전면에 드러나지 않고 배경에 녹아드는 것이 핵심이에요.",
                 "Ambient computing is a paradigm where sensors, IoT devices, and edge computing detect a person's presence and context so the surrounding environment — lighting, temperature, guidance — reacts on its own, without explicit input. The key idea is that the technology recedes into the background instead of standing in front.")),
    "glossary": [
        ("앰비언트 컴퓨팅", "Ambient Computing", ("다가가면 알아서 바뀌는 환경.", "An environment that changes itself as you approach."), ("기술이 안 보일수록 잘 된 거예요.", "The less visible the tech, the better it's working.")),
        ("IoT", "IoT", ("곳곳에 숨은 센서들.", "Sensors hidden everywhere."), ('IoT 자체의 보안 위협은 다른 세계에서 다뤄요. → <a href="iotsec-ko.html">IoT 보안 위협</a>', 'IoT security itself is covered in another world. → <a href="iotsec-en.html">IoT security threats</a>')),
        ("엣지컴퓨팅", "Edge Computing", ("현장에서 바로 판단하는 작은 컴퓨터.", "A small computer that decides right there on the spot."), ("클라우드까지 안 가고 그 자리에서 처리해요.", "It processes on the spot instead of round-tripping to the cloud.")),
        ("컨텍스트 인식", "Context Awareness", ("지금 상황을 알아채는 능력.", "The ability to notice the current situation."), ("누가, 언제, 어디서인지를 함께 봐요.", "It reads who, when, and where together.")),
        ("스마트홈", "Smart Home", ("집에 들어온 앰비언트 컴퓨팅.", "Ambient computing that moved into the home."), ("이 과학관 원리를 집에 적용한 거예요.", "The same hall-wide idea, applied to your living room.")),
        ("디지털 트윈", "Digital Twin", ("쌍둥이 화면으로 보는 실제 모습.", "A twin screen showing the real thing."), ('이 분야의 다른 부스에서 자세히 다뤄요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', 'Covered in depth at another booth. → <a href="cps-en.html">Cyber-Physical Systems</a>')),
        ("프라이버시", "Privacy", ("몰래 보는 느낌을 막는 약속.", "The promise that stops it from feeling like spying."), ("센서가 늘수록 더 중요해져요.", "The more sensors there are, the more this matters.")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
