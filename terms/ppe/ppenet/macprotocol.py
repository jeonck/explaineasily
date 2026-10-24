from _draw import *
from _world import *

# 1. 여러 집배원이 같은 통로로 한꺼번에 보내려 해요
P1 = svg(300, sky(300)
         + person(220, 170, s=0.75, face=EYES, **CARRIER) + person(340, 170, s=0.75, face=EYES, **CARRIER)
         + person(460, 170, s=0.75, face=EYES, **CARRIER)
         + '<rect x="200" y="230" width="360" height="20" fill="#8B5E3C"/>'
         + envelope(250, 215, 0.6) + envelope(340, 215, 0.6) + envelope(430, 215, 0.6)
         + label(380, 30, "⟦좁은 통로 하나를 여러 집배원이 동시에 쓰려고 해요|several carriers all try to use the one narrow lane at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦동시에 보내면 봉투끼리 부딪혀요|sending at the same time means envelopes collide⟧", 12, "var(--muted)"))

# 2. 아무도 순서를 정해주지 않으면 충돌이 나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(300, 170, s=0.8, face=SWEAT + EYES, **CARRIER) + person(460, 170, s=0.8, face=SWEAT + EYES, **CARRIER)
         + '<path d="M330 220 l40 -20 l-40 -20 M450 220 l-40 -20 l40 -20" stroke="var(--bad)" stroke-width="3"/>'
         + label(380, 260, "⟦봉투가 섞여 둘 다 못 알아볼 글자가 돼요|the envelopes tangle into something neither one can read⟧", 12, "var(--ink)")
         + label(380, 30, "⟦규칙이 없으면 서로 먼저 보내려다 부딪혀요|without a rule, everyone rushes and collides⟧", 13, "var(--ink)", cls="d"))

# 3. 다중접속 제어 = 안 부딪히고 나눠 쓰는 세 가지 규칙 (hero)
P3 = svg(340, sky(340)
         + person(260, 170, s=0.8, face=EYES, **CARRIER) + label(260, 230, "⟦CSMA|CSMA⟧", 13, "var(--ink)", cls="d")
         + person(420, 170, s=0.8, face=EYES, **CARRIER) + label(420, 230, "⟦TDMA|TDMA⟧", 13, "var(--ink)", cls="d")
         + person(580, 170, s=0.8, face=EYES, **CARRIER) + label(580, 230, "⟦CDMA|CDMA⟧", 13, "var(--ink)", cls="d")
         + label(380, 30, "⟦다중접속 제어 = 여러 집배원이 하나의 길을 안 부딪히고 나눠 쓰는 규칙|multiple access control = the rules that let many carriers share one road without colliding⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦듣고 보내거나, 시간을 나누거나, 암호코드로 구분해요|listen first, split the time, or tell voices apart by code⟧", 12, "var(--muted)"))

# 4. 세 방식 비교표
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦세 가지 다중접속 방식|Three ways to share one road⟧",
                    ("⟦CSMA — 보내기 전에 듣고, 비었으면 전송|CSMA — listen before sending, go if clear⟧",
                     "⟦TDMA — 시간을 쪼개 차례대로 전송|TDMA — split time, take turns⟧",
                     "⟦CDMA — 각자 고유 코드로 동시에 전송|CDMA — each uses its own code, all at once⟧",
                     "⟦충돌나면 잠깐 기다렸다 다시 시도(CSMA/CD)|on collision, wait briefly and retry (CSMA/CD)⟧"), 1.0))

# 5. 참여자가 늘면 각자 한계가 생겨요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + person(190, 135, s=0.8, face=SWEAT + EYES, **CARRIER) + label(190, 265, "⟦CSMA — 사람이 많아지면 충돌이 잦아져요|CSMA — more carriers means more collisions⟧", 11, "var(--ink)")
         + person(380, 135, s=0.8, face=EYES, **CARRIER) + label(380, 265, "⟦TDMA — 빈 시간도 그냥 버려져요|TDMA — an empty turn is still wasted⟧", 11, "var(--ink)")
         + person(570, 135, s=0.8, face=EYES, **CARRIER) + label(570, 265, "⟦CDMA — 코드를 맞추는 일이 복잡해요|CDMA — coordinating the codes gets complex⟧", 11, "var(--ink)"))

LISTEN_I = icon('<path d="M20 30 a12 12 0 0 1 24 0 v10 a12 12 0 0 1 -24 0z" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M14 36 v4 a18 18 0 0 0 36 0 v-4" stroke="var(--ink)" stroke-width="3" fill="none"/>')
CLOCK2_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 20 v12 l9 5" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CODE2_I = icon('<path d="M12 20 l-8 12 l8 12 M52 20 l8 12 l-8 12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M26 44 L38 20" stroke="var(--ink)" stroke-width="3"/>')
RETRY_I = icon('<path d="M46 20 a18 18 0 1 0 6 14" stroke="var(--bad)" stroke-width="4" fill="none"/><path d="M46 10 v12 h-12" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "macprotocol", "order": 6,
    "title": ("하나의 통로를 안 부딪히고 나눠 쓰는 법", "Sharing One Lane Without Colliding"),
    "h1": ("<em>다중접속·매체접근제어</em>가 뭐예요?", "What is <em>Multiple Access / Medium Access Control</em>?"),
    "sub": ("CSMA/TDMA/CDMA를, 여러 집배원이 하나의 좁은 통로를 안 부딪히고 나눠 쓰는 규칙 이야기로 풀어봤어요.",
            "CSMA/TDMA/CDMA, told as a story about rules that let many carriers share one narrow lane without colliding."),
    "panels": [
        {"svg": P1, "alt": ("집배원 셋이 좁은 통로 하나로 동시에 봉투를 보내려 함", "Three carriers all try to send envelopes through one narrow lane at once"),
         "caption": ("여러 집배원이 같은 통로를 동시에 쓰려 해요.", "Several carriers try to use the same narrow lane at once."),
         "small": ("동시에 보내면 봉투끼리 부딪혀요.", "Sending at the same time means envelopes collide.")},
        {"svg": P2, "alt": ("규칙 없이 동시에 보낸 두 집배원의 봉투가 서로 부딪혀 섞임", "Two carriers send at once without a rule, and their envelopes collide into a tangle"),
         "caption": ("규칙이 없으면 충돌이 나요.", "Without a rule, things collide."),
         "small": ("봉투가 섞여 둘 다 못 알아볼 글자가 돼요.", "The envelopes tangle into something neither one can read.")},
        {"svg": P3, "hero": True, "alt": ("집배원 세 명이 각각 CSMA, TDMA, CDMA 이름표를 달고 서 있음", "Three carriers stand labeled CSMA, TDMA, and CDMA"),
         "caption": ("세 가지 규칙으로 안 부딪히고 나눠 써요.", "Three rules let them share without colliding."),
         "small": ("듣고 보내거나, 시간을 나누거나, 암호코드로 구분해요.", "Listen first, split the time, or tell voices apart by code."),
         "tricks": (4, [
             (LISTEN_I, ("CSMA — 듣고 보내기", "CSMA — listen before send"), ("비어 있으면 그때 보내요", "send only when the lane sounds clear"), "calm"),
             (CLOCK2_I, ("TDMA — 시간 나누기", "TDMA — time-slicing"), ("각자 차례가 정해져 있어요", "each carrier gets a fixed turn")),
             (CODE2_I, ("CDMA — 암호코드 구분", "CDMA — code separation"), ("동시에 보내도 코드로 구별돼요", "sent at once, but told apart by code"), "warm"),
             (RETRY_I, ("충돌 후 재시도", "Collision backoff"), ("부딪히면 잠깐 쉬었다 다시 보내요", "on collision, wait a moment then retry")),
         ])},
        {"svg": P4, "alt": ("CSMA·TDMA·CDMA 세 방식과 충돌 처리 방법을 적은 안내판", "A board listing CSMA, TDMA, CDMA and how each handles collisions"),
         "caption": ("세 방식은 충돌을 다루는 법이 달라요.", "The three ways handle collisions differently."),
         "small": ("CSMA는 듣고 보내고, TDMA는 시간을 나누고, CDMA는 코드로 구분해요.", "CSMA listens first, TDMA splits time, CDMA tells voices apart by code.")},
        {"svg": P5, "alt": ("CSMA는 사람이 많아지면 충돌이 늘고, TDMA는 빈 시간이 버려지고, CDMA는 코드 맞추기가 복잡함", "CSMA gets more collisions as carriers grow, TDMA wastes empty turns, CDMA's code coordination gets complex"),
         "caption": ("참여자가 늘면 각자 한계가 생겨요.", "More carriers expose each method's limits."),
         "small": ("CSMA는 충돌이 늘고, TDMA는 빈 시간이 아깝고, CDMA는 코드 조율이 복잡해져요.", "CSMA collides more, TDMA wastes idle turns, CDMA's coordination grows complex.")},
    ],
    "summary": (("<b>다중접속 제어(MAC)</b>는 <b>여러 사용자가 하나의 통신 매체를 안 부딪히고 나눠 쓰도록</b> 하는 규칙이에요(CSMA·TDMA·CDMA).",
                 "<b>Multiple access control (MAC)</b> is the set of rules that let <b>several users share one communication medium without colliding</b> (CSMA, TDMA, CDMA)."),
                ("CSMA(Carrier Sense Multiple Access)는 전송 전 매체가 비어 있는지 감지하고, 충돌이 나면 감지·회피하는 방식(CSMA/CD, CSMA/CA)이에요. TDMA(Time Division)는 시간을 슬롯으로 쪼개 사용자마다 할당하고, CDMA(Code Division)는 사용자마다 고유한 확산 코드를 줘 같은 시간·주파수를 동시에 써도 구분되게 해요.",
                 "CSMA (Carrier Sense Multiple Access) senses whether the medium is idle before transmitting, and detects or avoids collisions (CSMA/CD, CSMA/CA). TDMA (Time Division) slices time into slots assigned per user. CDMA (Code Division) gives each user a unique spreading code, letting them share the same time and frequency simultaneously while still being told apart.")),
    "glossary": [
        ("CSMA", "CSMA", ("보내기 전에 통로가 비었는지 듣는 방식.", "Listening whether the lane is clear before sending."), ("충돌이 나면 감지하거나 미리 피해요.", "Detects or avoids collisions when they happen.")),
        ("TDMA", "TDMA", ("시간을 쪼개 차례대로 쓰는 방식.", "Splitting time and taking turns."), ("각자 정해진 시간에만 보내요.", "Each carrier sends only in its own assigned slot.")),
        ("CDMA", "CDMA", ("각자 고유 암호코드로 동시에 보내는 방식.", "Sending at once, each with its own code."), ("받는 쪽이 자기 코드로만 걸러 들어요.", "The receiver filters using only its own code.")),
        ("충돌 감지(CSMA/CD)", "CSMA/CD", ("부딪힌 걸 알아채는 방법.", "Noticing that a collision happened."), ("부딪히면 잠깐 기다렸다 다시 보내요.", "On collision, wait briefly and resend.")),
        ("충돌 회피(CSMA/CA)", "CSMA/CA", ("부딪히기 전에 미리 피하는 방법.", "Avoiding the collision before it happens."), ("무선처럼 감지가 어려운 곳에서 써요.", "Used where sensing a collision directly is hard, like wireless.")),
        ("TCP/UDP", "TCP/UDP", ("등기봉투와 일반봉투.", "The registered envelope and the plain one."), ('다중접속 규칙으로 통로를 나눈 뒤, 그 위에서 쓰는 봉투예요. → <a href="tcpudp-ko.html">등기봉투와 일반봉투</a>', 'The envelopes used on top of whatever lane-sharing rule wins. → <a href="tcpudp-en.html">the registered envelope and the plain one</a>')),
        ("네트워크 슬라이싱", "Network slicing", ("한 도로를 전용 차선으로 나누는 것.", "Splitting one road into dedicated lanes."), ('차선을 미리 나누면 충돌 자체가 줄어요. → <a href="5gslicing-ko.html">도로를 차선으로 나누기</a>', 'Pre-splitting lanes cuts down collisions to begin with. → <a href="5gslicing-en.html">splitting the road into lanes</a>')),
        ("무선 측위", "Wireless positioning", ("신호탑들로 내 위치를 찾는 기술.", "Finding your position from several signal towers."), ('측위 신호도 결국 같은 통로 규칙을 따라요. → <a href="wirelesspos-ko.html">신호탑 세 개로 위치 찾기</a>', 'Positioning signals follow the same sharing rules too. → <a href="wirelesspos-en.html">finding a position from three towers</a>')),
    ],
}
