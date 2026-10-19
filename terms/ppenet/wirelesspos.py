from _draw import *
from _world import *

# 1. 도심 건물 숲에서 집배원이 길을 잃어요
P1 = svg(340, sky(340)
         + '<rect x="100" y="60" width="60" height="200" fill="var(--stone-dark)"/><rect x="200" y="30" width="60" height="230" fill="var(--stone-dark)"/><rect x="520" y="50" width="60" height="210" fill="var(--stone-dark)"/>'
         + person(380, 210, s=0.85, face=SWEAT + EYES, **CARRIER)
         + bubble(420, 100, 220, 44, "⟦여기가 어디인지 모르겠어요|I don't even know where I am⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 324, "⟦건물 숲에 둘러싸여 지금 위치를 알 수가 없어요|boxed in by buildings, there's no telling the current spot⟧", 12, "var(--muted)"))

# 2. 위성 신호가 건물에 가려 약해져요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<circle cx="660" cy="50" r="18" fill="#C9A86A"/>' + label(660, 90, "⟦위성|satellite⟧", 11, "var(--ink)")
         + '<path d="M640 70 L420 180" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 6"/>'
         + '<rect x="300" y="100" width="70" height="160" fill="var(--stone-dark)"/>'
         + person(420, 190, s=0.8, face=FROWN, **CARRIER)
         + label(420, 305, "⟦건물에 가려 신호가 안 닿거나 약해요|blocked by the building, the signal barely gets through⟧", 12, "var(--ink)", cls="d"))

# 3. 무선 측위 = 여러 신호탑 거리로 내 위치를 찾는 것 (hero)
P3 = svg(340, sky(340)
         + postoffice(140, 150, 0.6) + postoffice(620, 150, 0.6) + '<circle cx="660" cy="60" r="16" fill="#C9A86A"/>'
         + person(380, 220, s=0.85, face=EYES, **CARRIER)
         + '<circle cx="140" cy="186" r="160" fill="none" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 5"/>'
         + '<circle cx="620" cy="186" r="160" fill="none" stroke="var(--good)" stroke-width="2" stroke-dasharray="4 5"/>'
         + '<circle cx="660" cy="76" r="230" fill="none" stroke="#C9A86A" stroke-width="2" stroke-dasharray="4 5"/>'
         + label(380, 30, "⟦무선 측위 = 여러 신호탑에서 거리를 재어 내 위치를 찾는 기술|wireless positioning = finding your spot by measuring distance from several signal towers⟧", 13, "var(--ink)", cls="d")
         + label(380, 322, "⟦원 세 개가 겹치는 한 점이 바로 지금 있는 자리예요|the one point where three circles overlap is exactly where you're standing⟧", 12, "var(--muted)"))

# 4. 측위 방식 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦위치를 찾는 세 가지 신호|Three signals used to find a position⟧",
                    ("⟦위성(GPS) — 멀리서도 정확하지만 실내에 약함|satellite (GPS) — accurate even far away, but weak indoors⟧",
                     "⟦기지국 — 이동통신 신호 세기로 대략 위치|cell tower — rough position from signal strength⟧",
                     "⟦와이파이/비콘 — 실내에서 보완|Wi-Fi/beacon — fills in indoors⟧",
                     "⟦삼변측량 — 세 곳 이상 거리를 겹쳐 계산|trilateration — distances from 3+ points, overlapped⟧"), 1.0))

# 5. 실내에선 오차가 커지고, 여러 방식을 섞어 써요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 160, s=0.8, face=SMILE, **CARRIER) + label(190, 240, "⟦야외에선 위성 신호로 꽤 정확해요|outdoors, satellite signals are quite accurate⟧", 11, "var(--ink)")
         + person(570, 160, s=0.8, face=FROWN, **CARRIER) + label(570, 240, "⟦실내에선 신호가 반사되어 오차가 커요|indoors, reflections widen the error⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그래서 위성·기지국·와이파이를 섞어 써요(하이브리드)|so they're blended together — satellite, cell, Wi-Fi (hybrid)⟧", 12, "var(--ink)", cls="d"))

SAT_I = icon('<circle cx="32" cy="18" r="8" fill="#C9A86A"/><rect x="10" y="14" width="10" height="8" fill="var(--accent)"/><rect x="44" y="14" width="10" height="8" fill="var(--accent)"/><path d="M32 26 v26" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 3"/>')
TOWER2_I = icon('<path d="M32 10 L48 54 H16 Z" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M20 20 q12 -10 24 0" stroke="var(--good)" stroke-width="3" fill="none"/>')
WIFI_I = icon('<path d="M16 32 q16 -16 32 0 M22 40 q10 -10 20 0" stroke="var(--accent)" stroke-width="3" fill="none"/><circle cx="32" cy="48" r="4" fill="var(--accent)"/>')
TRI_I = icon('<circle cx="24" cy="26" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><circle cx="42" cy="30" r="18" fill="none" stroke="var(--good)" stroke-width="2"/><circle cx="32" cy="44" r="18" fill="none" stroke="#C9A86A" stroke-width="2"/>')

PAGE = {
    "slug": "wirelesspos", "order": 11,
    "title": ("신호탑 세 개로 위치 찾기", "Finding a Position From Three Signal Towers"),
    "h1": ("<em>무선 측위</em>가 뭐예요?", "What is <em>Wireless Positioning</em>?"),
    "sub": ("무선 측위(위치 기반 기술)를, 여러 신호탑에서 거리를 재어 지금 위치를 찾는 이야기로 풀어봤어요.",
            "Wireless positioning, told as a story about finding your current spot by measuring distance from several signal towers."),
    "panels": [
        {"svg": P1, "alt": ("건물 숲에 둘러싸인 집배원이 지금 어디인지 모르겠다고 말풍선으로 말함", "A carrier boxed in by tall buildings says in a speech bubble that they don't know where they are"),
         "caption": ("도심 건물 숲에서 집배원이 길을 잃어요.", "In a canyon of buildings, the carrier gets lost."),
         "small": ("건물 숲에 둘러싸여 지금 위치를 알 수가 없어요.", "Boxed in by buildings, there's no telling the current spot.")},
        {"svg": P2, "alt": ("위성 신호가 큰 건물에 가로막혀 집배원에게 약하게 닿음", "A satellite signal, blocked by a tall building, barely reaches the carrier"),
         "caption": ("위성 신호가 건물에 가려 약해져요.", "A satellite signal weakens, blocked by a building."),
         "small": ("건물에 가려 신호가 안 닿거나 약해요.", "Blocked by the building, the signal barely gets through.")},
        {"svg": P3, "hero": True, "alt": ("두 우체국과 위성에서 뻗은 점선 원 세 개가 집배원이 선 자리에서 겹침", "Three dashed circles from two post offices and a satellite overlap exactly where the carrier stands"),
         "caption": ("여러 신호탑에서 거리를 재어 내 위치를 찾아요.", "Measuring distance from several signal towers finds your spot."),
         "small": ("원 세 개가 겹치는 한 점이 바로 지금 있는 자리예요.", "The one point where three circles overlap is exactly where you're standing."),
         "tricks": (4, [
             (SAT_I, ("위성(GPS)", "Satellite (GPS)"), ("멀리서도 정확하지만 실내엔 약해요", "accurate even far away, but weak indoors"), "calm"),
             (TOWER2_I, ("기지국 신호", "Cell tower signal"), ("신호 세기로 대략 위치를 가늠해요", "roughly gauges position from signal strength")),
             (WIFI_I, ("와이파이/비콘", "Wi-Fi/beacon"), ("실내에서 부족한 부분을 보완해요", "fills in what's missing indoors"), "warm"),
             (TRI_I, ("삼변측량", "Trilateration"), ("세 곳 이상 거리를 겹쳐 위치를 계산해요", "overlaps distances from 3+ points to compute position")),
         ])},
        {"svg": P4, "alt": ("위성·기지국·와이파이·삼변측량 네 가지를 설명한 안내판", "A board explaining satellite, cell tower, Wi-Fi, and trilateration"),
         "caption": ("측위에는 여러 신호가 쓰여요.", "Several kinds of signals are used for positioning."),
         "small": ("위성은 야외에, 기지국은 대략, 와이파이는 실내 보완에 맞아요.", "Satellite suits outdoors, cell towers give a rough fix, Wi-Fi fills in indoors.")},
        {"svg": P5, "alt": ("왼쪽: 야외에서 위성 신호로 정확함. 오른쪽: 실내에서는 신호 반사로 오차가 커짐", "Left: outdoors, satellite signals are accurate. Right: indoors, reflections widen the error"),
         "caption": ("실내에선 오차가 커지고, 여러 방식을 섞어 써요.", "Indoors the error grows, so methods get blended."),
         "small": ("그래서 위성·기지국·와이파이를 섞어 쓰는 하이브리드 방식을 써요.", "So a hybrid approach blends satellite, cell, and Wi-Fi together.")},
    ],
    "summary": (("<b>무선 측위</b>는 <b>여러 신호탑(위성·기지국·와이파이)에서 오는 신호로 거리를 재어</b> 지금 위치를 찾아내는 기술이에요(삼변측량).",
                 "<b>Wireless positioning</b> finds your current location by <b>measuring distance from signals coming from several towers</b> — satellite, cell, Wi-Fi — through trilateration."),
                ("무선 측위는 GPS 같은 위성 신호의 도착 시간차로 거리를 계산하는 삼변측량이 기본이지만, 실내·도심에서는 신호가 약해지거나 반사돼 오차가 커져요. 이를 보완하려고 이동통신 기지국 신호 세기(RSSI)나 실내 와이파이/BLE 비콘 신호를 함께 쓰는 하이브리드 측위가 널리 쓰여요.",
                 "Wireless positioning is fundamentally trilateration — computing distance from the arrival-time difference of satellite signals like GPS. But indoors and in dense cities, signals weaken or bounce off surfaces, widening the error. To compensate, hybrid positioning blends in cell tower signal strength (RSSI) and indoor Wi-Fi or BLE beacon signals.")),
    "glossary": [
        ("무선 측위", "Wireless positioning", ("여러 신호탑 거리로 내 위치를 찾는 기술.", "Finding your position by distance from several towers."), ("삼변측량이 기본 원리예요.", "Trilateration is the underlying principle.")),
        ("삼변측량", "Trilateration", ("세 곳 이상 거리를 겹쳐 위치를 계산하는 것.", "Overlapping distances from three or more points to compute position."), ("원이 겹치는 한 점이 위치예요.", "The spot is where the circles overlap.")),
        ("GPS", "GPS", ("가장 흔히 쓰는 위성 측위 신호.", "The most common satellite positioning signal."), ("실내·도심에선 약해질 수 있어요.", "Can weaken indoors or in dense cities.")),
        ("RSSI", "RSSI", ("받은 신호의 세기.", "The strength of a received signal."), ("가까운 기지국일수록 세게 받혀요.", "A closer tower is received more strongly.")),
        ("BLE 비콘", "BLE beacon", ("실내 위치를 보완하는 작은 신호 발신기.", "A small signal transmitter that fills in indoor positioning."), ("위성이 안 닿는 실내에서 요긴해요.", "Useful indoors where satellites can't reach.")),
        ("5G 네트워크 슬라이싱", "5G Network slicing", ("한 도로를 전용 차선으로 나누는 것.", "Splitting one road into dedicated lanes."), ('측위 신호도 특정 슬라이스로 우선 처리될 수 있어요. → <a href="5gslicing-ko.html">도로를 차선으로 나누기</a>', 'Positioning signals can also be prioritized on a dedicated slice. → <a href="5gslicing-en.html">splitting the road into lanes</a>')),
        ("다중접속 제어", "Multiple access control", ("여러 집배원이 한 길을 나눠 쓰는 규칙.", "The rules letting many carriers share one road."), ('측위 신호도 결국 이 규칙으로 통로를 나눠 써요. → <a href="macprotocol-ko.html">하나의 통로를 안 부딪히고 나눠 쓰는 법</a>', 'Positioning signals share their channel under these same rules. → <a href="macprotocol-en.html">sharing one lane without colliding</a>')),
        ("VPN", "VPN", ("몰래 파는 안전한 터널.", "A secretly dug, safe tunnel."), ('위치 정보가 오갈 때도 이 터널로 보호되기도 해요. → <a href="vpn-ko.html">몰래 파는 안전한 터널</a>', 'Location data can travel through this same protective tunnel. → <a href="vpn-en.html">the secret safe tunnel</a>')),
    ],
}
