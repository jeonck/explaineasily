from _draw import *
from _world import *

# 1. 공용 배송망에 공장 부품이 끼어 밀려요 (+ 세계관 소개)
P1 = svg(320, sky(320)
         + label(380, 26, "⟦이 배송망이 곧 통신망이다|This delivery network IS the telecom network⟧", 12, "var(--muted)", cls="d")
         + postoffice(140, 160, 0.85, "⟦공용 우체국|Public Post Office⟧")
         + envelope(300, 140, 0.8) + envelope(340, 160, 0.7) + envelope(280, 185, 0.6, text="⟦소포|parcel⟧")
         + person(520, 190, s=0.8, face=SWEAT + EYES, **CARRIER)
         + bubble(380, 70, 260, 46, "⟦공장 로봇 부품인데 일반 소포랑 같이 밀려요|factory robot parts, stuck in line with everyone's mail⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦공장은 1초도 늦으면 안 되는데, 공용망은 모두가 같이 써요|the factory can't afford even one second late — but the public network is shared by everyone⟧", 12, "var(--ink)"))

# 2. 공용망으론 속도·보안을 보장 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + postoffice(200, 160, 0.8)
         + person(360, 190, s=0.75, face=FROWN, **CLERK)
         + label(360, 250, "⟦오늘은 바빠서 순서가 밀려요|busy today — your turn got pushed back⟧", 11, "var(--ink)")
         + person(560, 190, s=0.75, face=SWEAT + EYES, **SENDER)
         + label(560, 250, "⟦우리 설계도가 남의 우체국 선반에 섞여요|our blueprints sit mixed on a stranger's shelf⟧", 11, "var(--ink)")
         + label(380, 282, "⟦공용망은 속도도 보안도 이 공장만을 위해 보장해주지 않아요|a shared network can't promise speed or privacy to just one factory⟧", 12, "var(--ink)", cls="d"))

# 3. 5G 특화망 = 이 공장만을 위한 전용 배송망 (hero)
P3 = svg(340, sky(340)
         + postoffice(620, 120, 0.8, "⟦전용 우체국|Private Post Office⟧")
         + truck(380, 220, 0.9, fast=True)
         + person(300, 180, s=0.8, face=SMILE + EYES, **CARRIER)
         + label(380, 30, "⟦5G 특화망 = 이 공장만을 위해 따로 놓은 배송망|5G Private Network = a delivery network laid down just for this factory⟧", 14, "var(--ink)", cls="d")
         + label(380, 322, "⟦길도 트럭도 우체국도 전부 이 공장 전용이에요|the roads, the trucks, the post office — all dedicated to this one factory⟧", 12, "var(--muted)"))

# 4. 공용망 vs 특화망 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦공용 배송망|Public Network⟧",
                    ("⟦속도 — 보장 안 됨|speed — not guaranteed⟧",
                     "⟦보안 — 남과 같이 씀|security — shared with others⟧",
                     "⟦비용 — 저렴|cost — cheap⟧",
                     "⟦범위 — 전국|coverage — nationwide⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦5G 특화망|5G Private Network⟧",
                    ("⟦속도 — 이 공장만 보장|speed — guaranteed just for us⟧",
                     "⟦보안 — 전용, 안 섞임|security — dedicated, no mixing⟧",
                     "⟦비용 — 비쌈|cost — expensive⟧",
                     "⟦범위 — 공장 안만|coverage — campus only⟧"), 1.0, hl=0))

# 5. 특화망도 만능은 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + truck(190, 160, 0.85, fast=True) + label(190, 240, "⟦공장 안에서는 1등으로 빨라요|inside the campus, it's the fastest there is⟧", 11, "var(--ink)")
         + postoffice(570, 170, 0.6) + label(570, 260, "⟦공장 밖으로는 안 나가요, 전국망이 아니에요|it doesn't leave the campus — not a nationwide network⟧", 11, "var(--ink)")
         + label(380, 282, "⟦좁지만 확실한 길이지, 세상 전체로 가는 길은 아니에요|a narrow but certain road — not a road to the whole world⟧", 12, "var(--ink)", cls="d"))

FREQ_I = icon('<rect x="8" y="30" width="48" height="4" fill="var(--line)"/><path d="M8 32 q8 -20 16 0 t16 0 t16 0" stroke="var(--accent)" stroke-width="4" fill="none"/>')
ROUTE_I = icon('<path d="M12 52 L30 12 L52 52" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="30" cy="12" r="6" fill="var(--accent)"/>')
LOCK_I = icon('<rect x="16" y="28" width="32" height="26" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><path d="M22 28 v-6 a10 10 0 0 1 20 0 v6" stroke="var(--ink)" stroke-width="4" fill="none"/>')
GAUGE_I = icon('<circle cx="32" cy="34" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 34 L46 22" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="34" r="3" fill="var(--ink)"/>')

PAGE = {
    "slug": "5gprivate", "order": 1,
    "title": ("이 공장만을 위한 전용 배송망", "A Delivery Network Just for This Factory"),
    "h1": ("<em>5G 특화망</em>이 뭐예요?", "What is a <em>5G Private Network</em>?"),
    "sub": ("5G 특화망을, 한 공장만을 위해 따로 깔아둔 전용 배송망 이야기로 풀어봤어요.",
            "A 5G private network, told as a story about a delivery network laid down just for one factory."),
    "panels": [
        {"svg": P1, "alt": ("공용 우체국 앞에 공장 소포가 일반 소포들과 섞여 밀려 있음", "A factory parcel waits mixed in with ordinary mail at the public post office"),
         "caption": ("공장 로봇 부품이 일반 소포랑 같이 밀려요.", "Factory robot parts are stuck in line with everyone's mail."),
         "small": ("공장은 1초도 늦으면 안 되는데, 공용망은 모두가 같이 써요.", "The factory can't afford a second's delay — but the public network is shared.")},
        {"svg": P2, "alt": ("우체국장은 바쁘다고 말하고, 보내는 사람은 설계도가 남과 섞인다고 걱정함", "The postmaster says it's busy, and the sender worries the blueprints sit mixed with strangers' mail"),
         "caption": ("공용망으론 속도도 보안도 보장받지 못해요.", "A shared network can't guarantee speed or security."),
         "small": ("오늘은 바빠서 밀리고, 우리 설계도가 남의 선반에 섞여요.", "Busy today means delays, and our blueprints sit mixed with others'.")},
        {"svg": P3, "hero": True, "alt": ("이 공장 전용 우체국과 전용 트럭이 전용 도로를 빠르게 달림", "A private post office and private truck race down a road built just for this factory"),
         "caption": ("5G 특화망은 이 공장만을 위한 전용 배송망이에요.", "A 5G private network is a delivery network laid down just for this factory."),
         "small": ("길도 트럭도 우체국도 전부 이 공장 전용이에요.", "The roads, the trucks, the post office — all dedicated to this one factory."),
         "tricks": (4, [
             (FREQ_I, ("전용 주파수", "Dedicated frequency"), ("이 공장만 쓰는 전파 대역", "a radio band only this factory uses"), "calm"),
             (ROUTE_I, ("전용 경로", "Dedicated route"), ("바깥 소포와 안 섞여요", "never mixes with outside mail")),
             (LOCK_I, ("보안 강화", "Stronger security"), ("데이터가 공장 밖으로 안 나가요", "data never leaves the campus"), "warm"),
             (GAUGE_I, ("보장된 지연", "Guaranteed latency"), ("초저지연이 약속돼요", "ultra-low delay is promised")),
         ])},
        {"svg": P4, "alt": ("공용 배송망과 5G 특화망을 속도·보안·비용·범위로 비교한 지도", "A map comparing public network vs 5G private network by speed, security, cost, coverage"),
         "caption": ("공용망과 특화망은 네 가지가 달라요.", "Public and private networks differ on four things."),
         "small": ("특화망은 속도·보안은 좋지만 비싸고 공장 안으로만 좁아요.", "Private is faster and more secure, but pricier and limited to the campus.")},
        {"svg": P5, "alt": ("왼쪽: 공장 안에서 특화망 트럭이 최고로 빠름. 오른쪽: 공장 밖으로는 안 나가는 우체국", "Left: inside the campus the private truck is the fastest. Right: the post office never serves outside the campus"),
         "caption": ("특화망도 만능은 아니에요.", "A private network isn't a cure-all."),
         "small": ("좁지만 확실한 길이지, 세상 전체로 가는 길은 아니에요.", "A narrow but certain road — not a road to the whole world.")},
    ],
    "summary": (("<b>5G 특화망</b>은 한 공장·건물·캠퍼스만을 위해 <b>따로 깔아둔 전용 5G망</b>으로, 공용망과 안 섞여 속도와 보안을 보장해요.",
                 "A <b>5G private network</b> is a <b>dedicated 5G network laid down for one factory, building, or campus</b> — never mixed with the public network, so speed and security can be guaranteed."),
                ("5G 특화망(이음5G/Local 5G)은 통신사의 공용 5G 코어·주파수와 분리된 전용 주파수·전용 코어망을 특정 구역에만 구축해, 지연·보안·대역폭을 그 구역 용도에 맞게 보장하는 방식이에요. 스마트팩토리·병원·항만 등 끊기면 안 되는 현장에 주로 쓰여요.",
                 "A 5G private network builds a dedicated frequency and dedicated core — separate from a carrier's shared public 5G core — within one specific site, guaranteeing latency, security, and bandwidth tailored to that site's needs. It's used where connectivity can't be allowed to drop: smart factories, hospitals, ports.")),
    "glossary": [
        ("5G 특화망", "5G Private Network", ("이 공장만을 위한 전용 배송망.", "A delivery network dedicated to just this factory."), ("주파수·코어망을 따로 가져요.", "Has its own frequency and core network.")),
        ("주파수 대역", "Frequency band", ("배송 트럭이 달리는 전용 차로.", "The dedicated lane the delivery trucks run on."), ("공용망과 섞이지 않는 전파 구간이에요.", "A radio range that never mixes with the public network.")),
        ("5G 코어망", "5G Core", ("배송 전체를 지휘하는 본사.", "The headquarters directing the whole delivery."), ("특화망은 이 본사도 따로 둬요.", "A private network keeps its own separate headquarters too.")),
        ("네트워크 슬라이싱", "Network slicing", ("한 도로를 용도별 차선으로 나누는 것.", "Splitting one road into lanes by purpose."), ('특화망 안에서도 더 잘게 나눌 수 있어요. → <a href="5gslicing-ko.html">도로를 차선으로 나누기</a>', 'Can be split even finer inside a private network. → <a href="5gslicing-en.html">splitting the road into lanes</a>')),
        ("엣지 컴퓨팅", "Edge computing", ("본사까지 안 가고 공장 안에서 바로 처리하는 것.", "Processing right at the factory instead of sending it all the way to HQ."), ("그래서 지연이 더 짧아져요.", "That's part of why the delay gets even shorter.")),
        ("SDN/NFV", "SDN/NFV", ("소프트웨어로 길을 바꾸는 관제탑.", "The control tower that reroutes roads with software."), ('특화망도 이 기술로 유연하게 운영돼요. → <a href="sdnnfv-ko.html">관제탑이 소프트웨어로 길을 바꾸는 법</a>', 'Private networks run flexibly on this too. → <a href="sdnnfv-en.html">a control tower rerouting roads in software</a>')),
        ("RAN", "Radio Access Network", ("동네마다 서 있는 중계 우체통.", "The relay mailbox standing in each neighborhood."), ("단말기가 실제로 전파를 주고받는 구간이에요.", "The segment where the device actually exchanges radio signals.")),
        ("VPN", "VPN", ("남의 길을 몰래 안전하게 빌려 쓰는 터널.", "A tunnel that safely borrows someone else's road."), ('소프트웨어로 사설망 흉내를 내는 다른 방법이에요. → <a href="vpn-ko.html">몰래 파는 안전한 터널</a>', 'A software way to fake a private network instead. → <a href="vpn-en.html">the secret safe tunnel</a>')),
    ],
}
