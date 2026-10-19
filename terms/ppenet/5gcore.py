from _draw import *
from _world import *

# 1. 예전 배송망: 종류 상관없이 트럭 한 대가 다 처리 → 밀림
P1 = svg(300, sky(300)
         + truck(200, 190, 1.0) + envelope(140, 140, 0.6) + envelope(180, 120, 0.6) + envelope(230, 150, 0.6)
         + person(500, 160, s=0.85, face=SWEAT + FROWN, **CARRIER)
         + label(380, 40, "⟦택배가 너무 많아요: 큰 짐, 급한 약, 작은 센서 소포까지 전부 한 트럭|too many kinds of packages: big boxes, urgent medicine, tiny sensor parcels, all on one truck⟧", 13, "var(--ink)")
         + label(380, 270, "⟦트럭 한 대로는 전부 다 만족시킬 수 없어요|one truck can't satisfy all of them⟧", 13, "var(--bad)"))

# 2. 요구사항이 서로 다름 (큰 짐 vs 응급 vs 대량 소형)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + envelope(120, 130, 1.1, text="⟦큰 짐|big box⟧") + bubble(60, 190, 160, 40, "⟦빨리만 가면 돼요|just go fast⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + envelope(380, 130, 0.9, registered=True, text="⟦응급약|urgent med⟧") + bubble(330, 190, 160, 40, "⟦지금 당장요!|right now!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + envelope(620, 130, 0.6, text="⟦센서 소포|sensor parcel⟧") + bubble(560, 190, 170, 40, "⟦저흰 수백만 개예요|we're millions of us⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦속도·시간·개수, 원하는 게 다 달라요|speed, timing, and count — each wants something different⟧", 12, "var(--ink)"))

# 3. 5G 핵심 = 상황별 전용 차선을 가진 배송망 (hero)
P3 = svg(340, sky(340)
         + postoffice(380, 110, 1.0, "⟦5G 분류소|5G core⟧")
         + truck(200, 250, 1.0, fast=True) + truck(380, 250, 1.0, fast=True) + truck(560, 250, 1.0, fast=True)
         + label(380, 30, "⟦5G 핵심기술 = 상황별 전용 차선을 가진 더 빠른 배송망|5G core = a faster delivery network with dedicated lanes per need⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦같은 도로를 쪼개서, 서로 안 부딪히게 나눠 써요|it splits the same road so nobody collides⟧", 12, "var(--muted)"))

I1 = icon('<rect x="8" y="26" width="48" height="24" rx="4" fill="var(--accent)"/><circle cx="20" cy="52" r="6" fill="#142033"/><circle cx="44" cy="52" r="6" fill="#142033"/>')
I2 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M32 18 v14 l9 5" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')
I3 = icon('<circle cx="18" cy="20" r="6" fill="var(--good)"/><circle cx="34" cy="16" r="6" fill="var(--good)"/><circle cx="46" cy="28" r="6" fill="var(--good)"/><circle cx="22" cy="40" r="6" fill="var(--good)"/><circle cx="42" cy="46" r="6" fill="var(--good)"/>')
I4 = icon('<rect x="6" y="28" width="52" height="8" fill="var(--stone)"/><rect x="6" y="28" width="22" height="8" fill="var(--accent)"/><rect x="30" y="28" width="16" height="8" fill="var(--good)"/>')

# 4. 네 가지 전용 차선 비교표
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦전용 차선 안내판|LANE GUIDE⟧",
                    ("⟦eMBB — 큰 짐 전용, 아주 빠르게|eMBB — big-box lane, very fast⟧",
                     "⟦URLLC — 응급 전용, 거의 안 기다림|URLLC — emergency lane, almost no wait⟧",
                     "⟦mMTC — 소형 소포 대량 전용|mMTC — lane for millions of tiny parcels⟧",
                     "⟦네트워크 슬라이싱 — 이 차선을 나누는 기술 자체|network slicing — the tech that splits the lanes⟧"), 1.0))

# 5. 차선이 있어도 도로(기지국) 자체가 없으면 소용없어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + postoffice(190, 140, 0.8) + label(190, 230, "⟦도로(기지국)가 안 닿는 곳은 차선도 없어요|no road (base station) reach means no lane either⟧", 11, "var(--ink)")
         + truck(570, 180, 0.9, fast=True) + label(570, 240, "⟦어디로 보낼지는 다음 문제예요|where to send it next is a separate problem⟧", 11, "var(--ink)")
         + label(380, 282, "⟦5G는 길을 빠르게 뚫어줄 뿐, 교통정리·길찾기는 다른 기술이 해요|5G just opens a faster road — traffic control and routing are separate jobs⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "5gcore", "order": 13,
    "title": ("상황별 전용 차선을 가진 배송망", "The Delivery Network With a Lane for Every Need"),
    "h1": ("<em>5G 이동통신 핵심기술</em>이 뭐예요?", "What is <em>5G Core Technology</em>?"),
    "sub": ("5G 핵심기술을, 큰 짐·응급약·작은 소포마다 전용 차선을 깔아주는 배송망 이야기로 풀어봤어요.",
            "5G core technology, told as a story about a delivery network that lays a dedicated lane for big boxes, urgent medicine, and tiny parcels alike."),
    "panels": [
        {"svg": P1, "alt": ("트럭 한 대가 온갖 종류의 택배로 밀려 있고 집배원이 땀을 흘림", "One truck is overloaded with every kind of package, and the carrier sweats"),
         "caption": ("택배가 너무 많아요.", "There are too many kinds of packages."),
         "small": ("트럭 한 대로는 전부 다 만족시킬 수 없어요.", "One truck can't satisfy all of them.")},
        {"svg": P2, "alt": ("큰 짐은 속도를, 응급약은 즉시성을, 센서 소포는 숫자를 원한다고 말함", "The big box wants speed, the urgent medicine wants immediacy, the sensor parcel wants sheer numbers"),
         "caption": ("요구사항이 서로 달라요.", "Each package wants something different."),
         "small": ("속도·시간·개수, 원하는 게 다 달라요.", "Speed, timing, and count — each wants something different.")},
        {"svg": P3, "hero": True, "alt": ("5G 분류소가 세 종류의 빠른 전용 트럭 차선으로 길을 나눔", "The 5G core splits the road into three dedicated fast lanes"),
         "caption": ("5G 핵심기술 = 상황별 전용 차선을 가진 배송망이에요.", "5G core = a delivery network with a lane for every need."),
         "small": ("같은 도로를 쪼개서, 서로 안 부딪히게 나눠 써요.", "It splits the same road so nobody collides."),
         "tricks": (4, [
             (I1, ("eMBB", "eMBB"), ("큰 짐을 아주 빠르게", "very fast for big boxes")),
             (I2, ("URLLC", "URLLC"), ("응급은 거의 즉시", "near-instant for emergencies"), "warm"),
             (I3, ("mMTC", "mMTC"), ("소형 소포 대량 처리", "handles millions of tiny parcels")),
             (I4, ("네트워크 슬라이싱", "Network Slicing"), ("차선을 나누는 기술", "the tech that splits the lanes"), "calm"),
         ])},
        {"svg": P4, "alt": ("전용 차선 안내판: eMBB·URLLC·mMTC·네트워크 슬라이싱 네 줄", "A lane guide board listing eMBB, URLLC, mMTC, and network slicing"),
         "caption": ("네 가지 전용 차선이 있어요.", "There are four dedicated lanes."),
         "small": ("이름은 어렵지만, 결국 '상황별로 길을 나눈다'는 뜻이에요.", "The names sound hard, but it just means splitting the road by situation.")},
        {"svg": P5, "alt": ("왼쪽: 도로(기지국)가 없으면 차선도 소용없음. 오른쪽: 트럭은 빠르지만 길찾기는 별개 문제", "Left: no road (base station) means no lane either. Right: the truck is fast, but routing is a separate problem"),
         "caption": ("차선이 있어도 도로 자체가 없으면 소용없어요.", "A lane is useless without the road reaching there at all."),
         "small": ("5G는 길을 빠르게 뚫어줄 뿐, 교통정리·길찾기는 다른 기술이 해요.", "5G just opens a faster road — traffic control and routing are separate jobs.")},
    ],
    "summary": (("<b>5G 핵심기술</b> = 큰 짐·응급·대량 소형 소포마다 <b>전용 차선(슬라이스)</b>을 깔아주는, 더 빠르고 똑똑한 배송망.",
                 "<b>5G core technology</b> = a faster, smarter delivery network that lays a dedicated lane (slice) for big, urgent, and massive tiny-parcel traffic alike."),
                ("5G 핵심기술은 eMBB(초고속·대용량), URLLC(초저지연·고신뢰), mMTC(대량 사물 연결)라는 세 가지 서비스 요구사항을, 네트워크 슬라이싱으로 하나의 물리망 위에서 논리적으로 분리해 동시에 만족시키는 기술이에요.",
                 "5G core technology satisfies three service requirements — eMBB (ultra-fast, high-bandwidth), URLLC (ultra-low-latency, high-reliability), and mMTC (massive device connectivity) — at once, by logically splitting a single physical network through network slicing.")),
    "glossary": [
        ("eMBB", "eMBB", ("대용량 짐 전용 빠른 차선.", "The fast lane for heavy, bulky traffic."), ("초고속 모바일 브로드밴드예요.", "Enhanced Mobile Broadband.")),
        ("URLLC", "URLLC", ("응급약 전용 즉시 차선.", "The instant lane for urgent traffic."), ("초저지연·초고신뢰 통신이에요.", "Ultra-Reliable Low-Latency Communication.")),
        ("mMTC", "mMTC", ("센서 소포 대량 전용 차선.", "The lane built for millions of tiny parcels."), ("대규모 사물 통신(IoT)이에요.", "massive Machine-Type Communication for IoT.")),
        ("네트워크 슬라이싱", "Network Slicing", ("도로를 차선으로 쪼개는 기술.", "The technology that splits the road into lanes."), ("하나의 망을 논리적으로 여러 개처럼 써요.", "Lets one physical network act like several logical ones.")),
        ("트래픽 쉐이핑/폴리싱", "Traffic Shaping/Policing", ("차선 안에서 속도를 조절하는 방법.", "How speed is managed inside a lane."), ('차선을 깐 다음엔 이게 필요해요. → <a href="trafficshaping-ko.html">택배량을 조절하는 창구</a>', 'Needed once the lanes are laid. → <a href="trafficshaping-en.html">the counter that controls the flow</a>')),
        ("V2X", "V2X", ("달리는 트럭끼리 주고받는 통신.", "The chatter between moving trucks themselves."), ('5G의 대표적인 활용 사례예요. → <a href="v2x-ko.html">트럭끼리 주고받는 쪽지</a>', "A flagship use case for 5G. → <a href=\"v2x-en.html\">the note trucks pass to each other</a>")),
        ("기지국(RAN)", "Base Station (RAN)", ("실제로 신호가 닿는 도로.", "The actual road the signal reaches."), ("분류소(코어)와 이 도로가 함께 있어야 동작해요.", "Needs this road alongside the core to work at all.")),
        ("VPN", "VPN", ("남이 못 보게 암호로 감싼 비밀 통로.", "A secret, encrypted passage no one else can peek into."), ('다른 세계(보안)에서 자세히 다뤄요. → <a href="vpn-ko.html">암호로 감싼 비밀 통로</a>', 'Covered in depth in another world (Security). → <a href="vpn-en.html">the encrypted secret passage</a>')),
    ],
}
