from _draw import *
from _world import *

# 1. 트럭이 배터리 다 쓰고 줄을 꽂아야 해요
P1 = svg(300, sky(300)
         + truck(260, 190, 1.0)
         + '<path d="M232 160 l20 20 l-20 20" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + person(420, 190, s=0.8, face=SWEAT + EYES, **CARRIER)
         + label(420, 250, "⟦선을 꽂고 기다려야 다시 출발해요|has to plug in and wait before heading out again⟧", 11, "var(--ink)")
         + label(380, 30, "⟦배송 트럭도 배터리가 떨어지면 멈춰요|even a delivery truck stops when its battery runs out⟧", 13, "var(--ink)", cls="d"))

# 2. 선은 엉키고, 정확히 맞춰 꽂아야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + truck(260, 190, 0.9)
         + '<path d="M240 170 q-20 20 10 40 q-30 -5 -20 30" stroke="#5A3B22" stroke-width="5" fill="none"/>'
         + person(480, 190, s=0.8, face=FROWN, **CARRIER)
         + label(480, 250, "⟦손으로 딱 맞춰 꽂아야만 충전돼요|only charges if you plug it in just right by hand⟧", 11, "var(--ink)")
         + label(380, 280, "⟦선은 엉키고, 위치가 조금만 틀려도 안 돼요|cables tangle, and even a slight misalignment fails⟧", 12, "var(--ink)", cls="d"))

# 3. 무선충전 = 충전판 위에 세우면 줄 없이 건너감 (hero)
P3 = svg(340, sky(340)
         + '<rect x="200" y="260" width="360" height="22" rx="6" fill="var(--accent)"/>'
         + truck(380, 220, 1.0, fast=True)
         + '<path d="M300 258 q80 -40 160 0" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'
         + label(380, 30, "⟦무선충전 = 전용 충전판 위에 서면 줄 없이 전기가 건너가요|wireless charging = park on the pad and power crosses the air, no cable⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦자기장으로 가까이에서, 또는 공진으로 살짝 떨어져서도 전해져요|carried by a magnetic field up close, or by resonance even a little apart⟧", 12, "var(--muted)"))

# 4. 유선충전 vs 무선충전 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦유선충전|Wired charging⟧",
                    ("⟦속도 — 빠름|speed — fast⟧",
                     "⟦효율 — 높음|efficiency — high⟧",
                     "⟦편의성 — 줄 꽂아야 함|convenience — must plug in⟧",
                     "⟦정렬 — 정확히 맞춰야 함|alignment — must be exact⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦무선충전|Wireless charging⟧",
                    ("⟦속도 — 조금 느림|speed — a bit slower⟧",
                     "⟦효율 — 조금 낮음|efficiency — a bit lower⟧",
                     "⟦편의성 — 세우기만 하면 됨|convenience — just park⟧",
                     "⟦정렬 — 조금 어긋나도 됨|alignment — some tolerance⟧"), 1.0, hl=2))

# 5. 효율은 더 낮고, 판 위에 서야만 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + truck(190, 190, 0.85, fast=True) + label(190, 260, "⟦줄 없이 세우기만 해도 충전돼요|just park — no cable needed to charge⟧", 11, "var(--ink)")
         + truck(570, 190, 0.7) + '<path d="M548 170 l10 -20" stroke="var(--bad)" stroke-width="3"/>' + label(570, 260, "⟦판에서 멀어지면 전기가 안 건너가요|move off the pad and the power stops crossing⟧", 11, "var(--ink)")
         + label(380, 282, "⟦편하지만 효율은 유선보다 낮고 자리를 꼭 지켜야 해요|convenient, but less efficient — and it has to stay right on the spot⟧", 12, "var(--ink)", cls="d"))

COIL_I = icon('<circle cx="22" cy="32" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="42" cy="32" r="14" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M28 32 h8" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 3"/>')
RESON_I = icon('<path d="M8 32 q8 -16 16 0 t16 0 t16 0" stroke="var(--accent)" stroke-width="4" fill="none"/><circle cx="32" cy="32" r="22" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 4"/>')
TOLERANCE_I = icon('<rect x="14" y="40" width="36" height="10" rx="3" fill="var(--good)"/><circle cx="32" cy="24" r="10" fill="var(--accent)"/><path d="M26 24 h12" stroke="#fff" stroke-width="3"/>')
SAFE_I = icon('<path d="M32 10 L52 20 V34 C52 46 42 54 32 58 C22 54 12 46 12 34 V20 Z" fill="var(--good)"/><path d="M24 34 l6 6 l12 -14" stroke="#fff" stroke-width="4" fill="none"/>')

PAGE = {
    "slug": "wirelesscharge", "order": 4,
    "title": ("줄 없이 세우기만 하면 되는 충전판", "The Charging Pad You Just Park On, No Cable Needed"),
    "h1": ("<em>무선충전기술</em>이 뭐예요?", "What is <em>Wireless Charging Technology</em>?"),
    "sub": ("무선충전기술을, 배송 트럭이 줄 없이 충전판 위에 서기만 해도 전기가 건너가는 이야기로 풀어봤어요.",
            "Wireless charging technology, told as a story about a delivery truck that charges just by parking on a pad — no cable."),
    "panels": [
        {"svg": P1, "alt": ("배송 트럭이 배터리가 떨어져 멈추고, 집배원이 선을 꽂아야 한다고 걱정함", "A delivery truck stops out of battery, and a carrier worries about having to plug in"),
         "caption": ("트럭도 배터리가 떨어지면 멈춰요.", "Even a truck stops when its battery runs out."),
         "small": ("선을 꽂고 기다려야 다시 출발해요.", "It has to plug in and wait before heading out again.")},
        {"svg": P2, "alt": ("엉킨 충전선 때문에 집배원이 정확히 맞춰 꽂느라 찡그림", "A carrier frowns, struggling to plug in a tangled charging cable just right"),
         "caption": ("선은 엉키고, 정확히 맞춰 꽂아야 해요.", "Cables tangle, and plugging in has to be exact."),
         "small": ("손으로 딱 맞춰야만 충전되고, 위치가 조금만 틀려도 안 돼요.", "It only charges when plugged in just right — even a slight miss fails.")},
        {"svg": P3, "hero": True, "alt": ("트럭이 빛나는 충전판 위에 서자 점선 화살로 전기가 건너가는 모습", "A truck parked on a glowing charging pad, with dashed arrows showing power crossing over"),
         "caption": ("충전판 위에 서면 줄 없이 전기가 건너가요.", "Park on the pad and power crosses the air, no cable."),
         "small": ("자기장으로 가까이에서, 또는 공진으로 살짝 떨어져서도 전해져요.", "Carried by a magnetic field up close, or by resonance even a little apart."),
         "tricks": (4, [
             (COIL_I, ("자기 유도", "Magnetic induction"), ("두 코일이 가까우면 전기가 건너가요", "two coils close together let power cross"), "calm"),
             (RESON_I, ("자기 공진", "Magnetic resonance"), ("주파수만 맞으면 조금 떨어져도 돼요", "matched frequencies work even a bit apart")),
             (TOLERANCE_I, ("정렬 여유", "Alignment tolerance"), ("살짝 삐뚤어도 충전돼요", "a slight misalignment still charges"), "warm"),
             (SAFE_I, ("비접촉 안전", "Contactless safety"), ("접점이 없어 비에 젖어도 안전해요", "no exposed contacts, so rain is safe too")),
         ])},
        {"svg": P4, "alt": ("유선충전과 무선충전을 속도·효율·편의성·정렬로 비교한 안내판", "A board comparing wired and wireless charging by speed, efficiency, convenience, alignment"),
         "caption": ("유선과 무선은 네 가지가 달라요.", "Wired and wireless differ on four things."),
         "small": ("무선은 편하지만, 속도와 효율은 유선보다 조금 낮아요.", "Wireless is more convenient, but a bit slower and less efficient than wired.")},
        {"svg": P5, "alt": ("왼쪽: 트럭이 충전판 위에서 줄 없이 충전됨. 오른쪽: 판에서 벗어난 트럭은 충전이 끊김", "Left: a truck charges on the pad with no cable. Right: a truck off the pad loses the charge"),
         "caption": ("효율은 더 낮고, 판 위에 서야만 해요.", "Efficiency is lower, and it must stay right on the pad."),
         "small": ("편하지만 유선보다 덜 효율적이고 자리를 꼭 지켜야 해요.", "Convenient, but less efficient than wired — and it has to stay in place.")},
    ],
    "summary": (("<b>무선충전기술</b>은 <b>줄을 꽂지 않고도 충전판 위에 서는 것만으로</b> 전기가 공중으로 건너가게 하는 기술이에요.",
                 "<b>Wireless charging technology</b> lets electricity cross the air <b>just by parking on a pad — no cable plugged in</b>."),
                ("무선충전은 자기 유도(magnetic induction, 가까운 거리에서 두 코일 사이 전자기 유도)나 자기 공진(magnetic resonance, 공진 주파수를 맞춰 조금 더 먼 거리에서) 방식으로 전력을 전달해요. 유선보다 효율은 낮지만 접점이 없어 안전하고 편리해, 전기차·로봇·모바일 기기 충전에 쓰여요.",
                 "Wireless charging transfers power through magnetic induction (two coils close together) or magnetic resonance (matched resonant frequencies, working over a slightly longer distance). It's less efficient than a wired connection, but safer and more convenient since there's no exposed contact — used for EVs, robots, and mobile devices.")),
    "glossary": [
        ("무선충전", "Wireless charging", ("줄 없이 충전판 위에 서면 되는 충전.", "Charging that just needs parking on a pad, no cable."), ("비접촉이라 더 안전해요.", "Contactless, so it's safer too.")),
        ("자기 유도", "Magnetic induction", ("가까운 두 코일 사이로 건너가는 전기.", "Power crossing between two coils held close together."), ("거리가 짧을수록 효율이 좋아요.", "The shorter the distance, the better the efficiency.")),
        ("자기 공진", "Magnetic resonance", ("주파수를 맞춰 조금 떨어져도 되는 방식.", "A way that works even a bit apart, by matching frequency."), ("유도 방식보다 거리에 더 여유가 있어요.", "More tolerant of distance than plain induction.")),
        ("5G 특화망", "5G Private Network", ("한 공장만을 위한 전용 배송망.", "A delivery network dedicated to one factory."), ('공장 안에서 무선충전 로봇과 함께 쓰이기도 해요. → <a href="5gprivate-ko.html">공장 전용 배송망</a>', 'Often paired with wirelessly charged robots inside a factory. → <a href="5gprivate-en.html">a delivery network just for one factory</a>')),
        ("Qi 표준", "Qi standard", ("여러 제조사가 함께 쓰는 공통 충전판 규격.", "The shared pad spec many makers agree to use."), ("서로 다른 트럭도 같은 판에서 충전돼요.", "Even different trucks can charge on the same pad.")),
        ("효율 손실", "Efficiency loss", ("건너가며 흩어지는 전기의 일부.", "The part of the power that scatters while crossing."), ("거리가 멀거나 어긋나면 더 커져요.", "Grows larger with distance or misalignment.")),
        ("충전 코일", "Charging coil", ("판 속에 들어 있는 전기를 건네는 부품.", "The part inside the pad that hands off the electricity."), ("트럭 쪽에도 짝이 되는 코일이 있어야 해요.", "The truck needs a matching coil of its own too.")),
        ("배터리 관리 시스템(BMS)", "BMS", ("받은 전기를 안전하게 나눠 담는 관리자.", "The manager who safely parcels out the power received."), ("무선이든 유선이든 과충전을 막아줘요.", "Prevents overcharging whether the power came wired or wireless.")),
    ],
}
