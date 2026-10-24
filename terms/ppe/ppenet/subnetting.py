from _draw import *
from _world import *

# 1. 동네 전체가 한 우편번호라 집배원이 헤맴
P1 = svg(300, sky(300)
         + postoffice(140, 150, 0.8)
         + person(380, 170, s=0.85, face=SWEAT + FROWN, **CARRIER) + envelope(460, 150, 0.6, text="⟦12-345번지|12-345⟧")
         + label(380, 40, "⟦동네 전체가 우편번호 하나라 다 뒤져야 해요|the whole town shares one zip code, so you must search everything⟧", 13, "var(--ink)")
         + label(380, 270, "⟦집이 수천 채면 하나씩 다 들러야 해요|with thousands of houses, you'd visit every single one⟧", 13, "var(--bad)"))

# 2. 구역을 안 나누면, 작은 변화도 동네 전체에 영향
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + postoffice(180, 150, 0.7) + postoffice(380, 150, 0.7) + postoffice(580, 150, 0.7)
         + label(380, 70, "⟦한 우체국이 쉬면 동네 전체가 멈춰요|if one post office stops, the whole town stops⟧", 12, "var(--ink)")
         + label(380, 270, "⟦구역을 안 나누면 혼잡도 장애도 전부 같이 번져요|without zones, congestion and outages spread to everyone⟧", 12, "var(--ink)"))

# 3. hero: 서브네팅 = 동네를 작은 우편번호 구역으로 나누는 것
P3 = svg(340, sky(340)
         + routemap(60, 40, 200, 220, "⟦1구역|ZONE 1⟧", ("⟦12-100~199|12-100~199⟧",), 1.0)
         + routemap(280, 40, 200, 220, "⟦2구역|ZONE 2⟧", ("⟦12-200~299|12-200~299⟧",), 1.0)
         + routemap(500, 40, 200, 220, "⟦3구역|ZONE 3⟧", ("⟦12-300~399|12-300~399⟧",), 1.0)
         + label(380, 290, "⟦서브네팅 = 큰 동네를 작은 우편번호 구역들로 쪼개는 것|subnetting = splitting one big town into smaller zip-code zones⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦구역마다 전용 우체국을 두니 찾기도, 관리하기도 쉬워져요|each zone gets its own post office — easier to find, easier to manage⟧", 12, "var(--muted)"))

I1 = icon('<rect x="8" y="8" width="48" height="48" rx="6" fill="none" stroke="var(--stone)" stroke-width="4"/><path d="M32 8 v48 M8 32 h48" stroke="var(--accent)" stroke-width="4"/>')
I2 = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M22 32 l8 8 l12 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
I3 = icon('<rect x="10" y="22" width="44" height="20" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M16 32 h32" stroke="var(--accent)" stroke-width="4" stroke-dasharray="6 4"/>')
I4 = icon('<path d="M32 10 L54 24 V44 L32 58 L10 44 V24 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/>')

# 4. 서브넷 마스크 = 어디까지가 구역 번호인지 알려주는 자
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦우편번호 자(서브넷 마스크)|ZIP RULER (SUBNET MASK)⟧",
                    ("⟦앞자리 — 어느 구역인지 (네트워크부)|front digits — which zone (network part)⟧",
                     "⟦뒷자리 — 그 구역 안 몇 번 집인지 (호스트부)|back digits — which house in that zone (host part)⟧",
                     "⟦마스크 — 자를 어디서 끊을지 정해줘요|mask — tells where to cut the ruler⟧",
                     "⟦라우팅 — 앞자리만 보고 바로 그 구역 우체국으로 보내요|routing — reads the front digits and ships straight to that zone's office⟧"), 1.0))

# 5. 한계: 구역을 너무 잘게 쪼개면 번지수가 아까워요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + routemap(80, 40, 220, 160, "⟦구역 10개 (각 2집)|10 ZONES (2 houses each)⟧", ("⟦번지수 낭비 심함|wastes a lot of addresses⟧",), 0.9)
         + routemap(460, 40, 220, 160, "⟦구역 2개 (각 500집)|2 ZONES (500 houses each)⟧", ("⟦혼잡·장애 전파 큼|more congestion, bigger blast radius⟧",), 0.9)
         + label(380, 282, "⟦너무 잘게 쪼개도, 너무 크게 둬도 손해예요 — 적당한 크기가 중요해요|too fine or too coarse both cost you — the right size matters⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "subnetting", "order": 15,
    "title": ("동네를 작은 우편번호 구역으로 나누기", "Splitting the Town Into Smaller Zip-Code Zones"),
    "h1": ("<em>네트워크 서브네팅</em>이 뭐예요?", "What is <em>Network Subnetting</em>?"),
    "sub": ("서브네팅을, 큰 동네를 작은 우편번호 구역으로 나눠 각자 우체국을 두는 이야기로 풀어봤어요.",
            "Subnetting, told as a story about splitting one big town into smaller zip-code zones, each with its own post office."),
    "panels": [
        {"svg": P1, "alt": ("우편번호가 하나뿐인 동네에서 집배원이 땀을 흘리며 헤맴", "A carrier sweats, lost in a town that shares just one zip code"),
         "caption": ("동네 전체가 우편번호 하나예요.", "The whole town shares one zip code."),
         "small": ("집이 수천 채면 하나씩 다 들러야 해요.", "With thousands of houses, you'd have to visit every single one.")},
        {"svg": P2, "alt": ("우체국 세 곳이 나란히 있고, 한 곳이 멈추면 동네 전체가 영향받는다고 적힘", "Three post offices stand side by side; if one stops, the whole town is affected"),
         "caption": ("구역을 안 나누면 전부 같이 번져요.", "Without zones, trouble spreads to everyone."),
         "small": ("혼잡도 장애도 동네 전체에 같이 번져요.", "Both congestion and outages spread across the whole town.")},
        {"svg": P3, "hero": True, "alt": ("동네가 1구역, 2구역, 3구역이라는 작은 우편번호 구역 세 개로 나뉨", "The town splits into three smaller zip-code zones: Zone 1, 2, 3"),
         "caption": ("서브네팅 = 동네를 작은 우편번호 구역으로 나누는 거예요.", "Subnetting = splitting the town into smaller zip-code zones."),
         "small": ("구역마다 전용 우체국을 두니 찾기도 관리하기도 쉬워져요.", "Each zone gets its own post office — easier to find and manage."),
         "tricks": (4, [
             (I1, ("나누기", "Split"), ("큰 동네를 쪼개요", "splits the big town up")),
             (I2, ("빨리 찾기", "Find Faster"), ("구역만 알면 끝", "knowing the zone is enough"), "calm"),
             (I3, ("자(마스크)로 자르기", "Cut With a Ruler"), ("어디까지가 구역인지", "where the zone part ends")),
             (I4, ("전용 구역", "Dedicated Zone"), ("혼잡·장애를 가둬요", "contains congestion and outages"), "warm"),
         ])},
        {"svg": P4, "alt": ("우편번호 자(서브넷 마스크) 안내판: 앞자리·뒷자리·마스크·라우팅 네 줄", "A zip-ruler (subnet mask) guide board listing front digits, back digits, mask, and routing"),
         "caption": ("자(마스크)가 앞뒤를 나눠줘요.", "The ruler (mask) splits front from back."),
         "small": ("라우터는 앞자리만 보고 바로 그 구역으로 보내요.", "A router reads just the front digits and ships straight to that zone.")},
        {"svg": P5, "alt": ("왼쪽: 구역을 너무 잘게 쪼개 번지수 낭비. 오른쪽: 구역이 너무 커서 혼잡·장애가 크게 번짐", "Left: too many tiny zones waste addresses. Right: zones too large spread congestion widely"),
         "caption": ("너무 잘게 쪼개도, 너무 크게 둬도 손해예요.", "Too fine or too coarse both cost you."),
         "small": ("적당한 구역 크기를 고르는 게 중요해요.", "Choosing the right zone size matters.")},
    ],
    "summary": (("<b>서브네팅</b> = 하나의 큰 동네(네트워크)를, 각자 우체국을 둔 <b>작은 우편번호 구역들</b>로 나누는 일.",
                 "<b>Subnetting</b> = dividing one big town (network) into <b>smaller zip-code zones</b>, each with its own post office."),
                ("서브네팅은 하나의 IP 네트워크를 서브넷 마스크로 네트워크부와 호스트부를 나눠, 더 작은 여러 개의 서브넷으로 쪼개는 작업이에요. 이를 통해 주소 공간을 효율적으로 쓰고, 트래픽과 장애 영향 범위를 구역 단위로 가둘 수 있어요.",
                 "Subnetting divides one IP network into smaller subnets by splitting an address into a network part and a host part with a subnet mask. It lets address space be used efficiently and contains traffic and failures within each zone.")),
    "glossary": [
        ("IP 주소", "IP Address", ("동네와 집을 가리키는 번지수.", "The address pointing to a town and a house."), ("보낼 곳을 특정하는 숫자예요.", "The number that identifies a destination.")),
        ("서브넷 마스크", "Subnet Mask", ("앞뒤를 나눠주는 자.", "The ruler that splits front from back."), ("네트워크부/호스트부 경계를 정해요.", "Sets the boundary between network and host parts.")),
        ("CIDR", "CIDR", ("자 눈금을 숫자 하나로 적는 법.", "Writing the ruler's mark as one short number."), ("예: /24 처럼 표기해요.", "Written like /24, for example.")),
        ("네트워크부/호스트부", "Network/Host Part", ("구역 번호 / 그 안의 집 번호.", "The zone number / the house number within it."), ("주소를 둘로 쪼갠 구성이에요.", "The two halves an address is split into.")),
        ("라우팅 테이블", "Routing Table", ("어느 구역으로 보낼지 적힌 안내판.", "The board that says which zone to ship to."), ('라우터가 늘 보는 지도예요. → <a href="adhocrouting-ko.html">집배원끼리 길을 찾아 전달하는 법</a>', 'The map a router always checks. → <a href="adhocrouting-en.html">how carriers find the way among themselves</a>')),
        ("OSI 3계층(네트워크)", "OSI Layer 3", ("구역과 길을 정하는 단계.", "The stage that decides the zone and the path."), ('주소·구역 나누기가 이 계층 일이에요. → <a href="osi7-ko.html">7단계로 나뉜 배송 공정</a>', "Addressing and zoning belong to this layer. → <a href=\"osi7-en.html\">the delivery process split into 7 stages</a>")),
        ("DNS", "DNS", ("번지수 대신 이름으로 찾게 해주는 주소록.", "The address book that finds a zip code by name instead."), ('다른 세계(보안)에서 자세히 다뤄요. → <a href="dns-ko.html">이름으로 찾는 주소록</a>', 'Covered in depth in another world (Security). → <a href="dns-en.html">the address book you search by name</a>')),
        ("L4 스위치", "L4 Switch", ("구역 안에서 창구 번호까지 보는 분류 직원.", "The sorter inside a zone who checks the counter number too."), ('구역이 나뉜 뒤 안쪽에서 더 세밀히 나눠요. → <a href="l4switch-ko.html">포트까지 보는 분류소 직원</a>', "Splits things even finer, once inside a zone. → <a href=\"l4switch-en.html\">the sorter who checks the port</a>")),
    ],
}
