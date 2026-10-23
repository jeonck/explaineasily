from _draw import *
from _world import *

# 1. 길을 바꾸려면 우체국마다 손으로 뜯어고쳐야 해요
P1 = svg(330, sky(330)
         + postoffice(140, 170, 0.75) + postoffice(360, 170, 0.75) + postoffice(580, 170, 0.75)
         + person(140, 230, s=0.6, face=SWEAT + EYES, **CLERK)
         + person(360, 230, s=0.6, face=SWEAT + EYES, **CLERK)
         + person(580, 230, s=0.6, face=SWEAT + EYES, **CLERK)
         + label(380, 30, "⟦배송 경로를 바꾸려면 우체국 세 곳을 전부 손으로 고쳐야 해요|rerouting means visiting all three post offices and rewiring each by hand⟧", 13, "var(--ink)", cls="d")
         + label(380, 310, "⟦우체국마다 길 안내판이 벽에 못 박혀 있어요|each post office has its route board nailed to the wall⟧", 12, "var(--muted)"))

# 2. 새 기능 하나마다 전용 기계를 또 사야 해요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + postoffice(260, 170, 0.8)
         + tollgate(260, 240, 0.7)
         + person(420, 150, s=0.75, face=FROWN, **CLERK)
         + label(420, 250, "⟦분류 기계가 고장나면 새 기계부터 사야 해요|when the sorting machine breaks, first you buy a whole new one⟧", 11, "var(--ink)")
         + label(380, 300, "⟦기계가 자리에 고정돼 있어서, 바꾸는 데마다 시간과 돈이 들어요|hardware is bolted to one spot — every change costs time and money⟧", 12, "var(--ink)", cls="d"))

# 3. SDN=관제탑이 소프트웨어로 길을 바꿈, NFV=범용 트럭에 기능만 설치 (hero)
P3 = svg(340, sky(340)
         + postoffice(210, 160, 0.6, "⟦우체국 A|Office A⟧") + postoffice(380, 160, 0.6, "⟦우체국 B|Office B⟧") + postoffice(550, 160, 0.6, "⟦우체국 C|Office C⟧")
         + person(380, 70, s=0.85, face=EYES, **CLERK)
         + label(380, 20, "⟦관제탑|Control Tower⟧", 12, "var(--ink)", cls="d")
         + '<path d="M350 90 L220 130 M380 90 L380 130 M410 90 L540 130" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5"/>'
         + label(380, 300, "⟦SDN = 관제탑이 소프트웨어로 모든 길을 한 번에 바꿔줘요|SDN = one control tower reroutes every road at once, in software⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦NFV = 전용 기계 대신 범용 트럭에 소프트웨어만 깔아요|NFV = swap the dedicated machine for software on a generic truck⟧", 12, "var(--muted)"))

# 4. 제어 평면 vs 데이터 평면 구조도
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 100, "⟦제어 평면 — 관제탑(소프트웨어)|Control plane — the tower (software)⟧",
                    ("⟦모든 우체국의 길을 결정해요|decides every post office's route⟧",), 1.0)
         + '<path d="M150 140 v30 M380 140 v30 M610 140 v30" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 5"/>'
         + postoffice(150, 230, 0.55) + postoffice(380, 230, 0.55) + postoffice(610, 230, 0.55)
         + label(380, 300, "⟦데이터 평면 — 실제로 소포를 나르는 현장 우체국들|Data plane — the real post offices actually carrying parcels⟧", 12, "var(--muted)"))

# 5. 소프트웨어 장애엔 더 취약해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **CLERK) + label(190, 255, "⟦기능 하나 추가가 하루 만에 끝나요|adding one feature now takes a single day⟧", 11, "var(--ink)")
         + person(570, 120, s=0.8, face=SWEAT + EYES, **CLERK) + label(570, 250, "⟦관제탑이 멈추면 모든 우체국이 같이 멈춰요|if the tower goes down, every post office stops with it⟧", 11, "var(--ink)")
         + label(380, 282, "⟦빠르고 유연하지만, 중앙이 흔들리면 전체가 흔들려요|fast and flexible — but if the center shakes, everything shakes⟧", 12, "var(--ink)", cls="d"))

TOWER_I = icon('<rect x="26" y="20" width="12" height="36" fill="var(--ink)"/><path d="M12 24 h40 M16 34 h32 M20 44 h24" stroke="var(--accent)" stroke-width="3"/>')
CODE_I = icon('<rect x="10" y="14" width="44" height="36" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><path d="M22 26 l-6 6 l6 6 M42 26 l6 6 l-6 6" stroke="var(--accent)" stroke-width="3" fill="none"/>')
TRUCKFN_I = icon('<rect x="10" y="26" width="34" height="18" rx="3" fill="var(--good)"/><circle cx="18" cy="48" r="5" fill="var(--ink)"/><circle cx="38" cy="48" r="5" fill="var(--ink)"/><rect x="20" y="14" width="14" height="10" rx="2" fill="var(--accent)"/>')
SCALE_I = icon('<path d="M20 50 h24 M32 50 V18 M20 18 h24" stroke="var(--ink)" stroke-width="3" fill="none"/><circle cx="20" cy="18" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="44" cy="18" r="8" fill="none" stroke="var(--good)" stroke-width="3"/>')

PAGE = {
    "slug": "sdnnfv", "order": 3,
    "title": ("소프트웨어로 길을 바꾸는 관제탑", "The Control Tower That Reroutes Roads in Software"),
    "h1": ("<em>SDN/NFV</em>가 뭐예요?", "What is <em>SDN/NFV</em>?"),
    "sub": ("SDN과 NFV를, 관제탑이 소프트웨어로 모든 우체국의 길을 한 번에 바꿔주는 이야기로 풀어봤어요.",
            "SDN and NFV, told as a story about a control tower that reroutes every post office's road at once, in software."),
    "panels": [
        {"svg": P1, "alt": ("우체국 세 곳의 직원들이 각자 벽에 박힌 길 안내판을 땀 흘리며 손으로 고침", "Three post office clerks each sweat over rewiring their own wall-mounted route board"),
         "caption": ("길을 바꾸려면 우체국마다 손으로 고쳐야 해요.", "Rerouting means fixing each post office by hand."),
         "small": ("길 안내판이 벽에 못 박혀 있어서 바꾸기 번거로워요.", "The route board is nailed to the wall, so changing it is a hassle.")},
        {"svg": P2, "alt": ("우체국장이 분류 기계가 고장 나 새 기계를 사야 한다고 걱정함", "A postmaster worries that a broken sorting machine means buying a whole new one"),
         "caption": ("새 기능 하나마다 전용 기계를 또 사야 해요.", "Every new feature means buying another dedicated machine."),
         "small": ("기계가 자리에 고정돼 있어서, 바꿀 때마다 시간과 돈이 들어요.", "Hardware bolted to one spot makes every change cost time and money.")},
        {"svg": P3, "hero": True, "alt": ("관제탑 한 명이 점선 화살표로 우체국 세 곳의 길을 동시에 가리킴", "One person in a control tower points dashed arrows toward three post offices at once"),
         "caption": ("관제탑이 소프트웨어로 모든 길을 한 번에 바꿔줘요.", "The tower reroutes every road at once, in software."),
         "small": ("전용 기계 대신 범용 트럭에 소프트웨어만 깔면 돼요.", "Swap the dedicated machine for software on a generic truck."),
         "tricks": (4, [
             (TOWER_I, ("중앙 제어", "Centralized control"), ("관제탑 하나가 모든 길을 결정해요", "one tower decides every road"), "calm"),
             (CODE_I, ("소프트웨어로 길 변경", "Software-defined routing"), ("버튼 하나로 길이 바뀌어요", "one switch changes the route")),
             (TRUCKFN_I, ("범용 장비에 기능 설치", "Functions as software (NFV)"), ("전용 기계 없이도 돌아가요", "runs without a dedicated machine"), "warm"),
             (SCALE_I, ("빠른 확장·축소", "Scale up or down fast"), ("필요할 때만 늘리고 줄여요", "grow or shrink only when needed")),
         ])},
        {"svg": P4, "alt": ("위쪽 관제탑(제어 평면)이 점선으로 아래쪽 세 우체국(데이터 평면)과 연결됨", "An upper control tower (control plane) connects by dashed line to three post offices below (data plane)"),
         "caption": ("관제탑과 현장은 분리돼 있어요.", "The tower and the field are kept separate."),
         "small": ("제어 평면이 정하고, 데이터 평면이 실제로 나르는 역할을 나눠요.", "The control plane decides; the data plane carries it out — split roles.")},
        {"svg": P5, "alt": ("왼쪽: 기능 추가가 하루 만에 끝남. 오른쪽: 관제탑이 멈추면 모든 우체국이 같이 멈춤", "Left: adding a feature now takes a day. Right: if the tower stops, every post office stops too"),
         "caption": ("소프트웨어 장애엔 더 취약해요.", "A software failure hits harder."),
         "small": ("빠르고 유연하지만, 중앙이 흔들리면 전체가 흔들려요.", "Fast and flexible — but if the center shakes, everything shakes.")},
    ],
    "summary": (("<b>SDN</b>은 <b>관제탑이 소프트웨어로 길을 한 번에 바꾸는 것</b>, <b>NFV</b>는 <b>전용 기계 대신 범용 장비에 기능을 소프트웨어로 설치하는 것</b>이에요.",
                 "<b>SDN</b> is a <b>tower rerouting every road at once, in software</b>; <b>NFV</b> is <b>installing a function as software on generic hardware instead of a dedicated machine</b>."),
                ("SDN(Software-Defined Networking)은 제어 평면(control plane)을 데이터 평면(data plane)에서 분리해, 중앙 컨트롤러가 네트워크 전체의 경로·정책을 소프트웨어로 제어하는 구조예요. NFV(Network Functions Virtualization)는 라우터·방화벽 같은 전용 장비(미들박스)의 기능을 범용 서버 위 소프트웨어(VNF)로 가상화하는 것이고요. 둘은 함께 쓰여 네트워크를 유연하고 빠르게 재구성할 수 있게 해줘요.",
                 "SDN (Software-Defined Networking) separates the control plane from the data plane, letting one central controller govern a network's paths and policy entirely in software. NFV (Network Functions Virtualization) turns the function of dedicated hardware middleboxes — routers, firewalls — into software (VNFs) running on generic servers. Used together, they make a network fast and flexible to reconfigure.")),
    "glossary": [
        ("SDN", "SDN", ("관제탑이 소프트웨어로 길을 바꾸는 것.", "A tower that reroutes roads in software."), ("제어와 현장을 분리해요.", "Separates control from the field.")),
        ("NFV", "NFV", ("전용 기계 대신 범용 트럭에 기능만 설치.", "Installing a function on a generic truck instead of a dedicated machine."), ("하드웨어를 소프트웨어로 바꿔요.", "Turns hardware into software.")),
        ("제어 평면", "Control plane", ("관제탑이 결정을 내리는 층.", "The layer where the tower makes decisions."), ("실제로 나르지는 않아요.", "Doesn't carry anything itself.")),
        ("데이터 평면", "Data plane", ("실제로 소포를 나르는 현장 우체국들.", "The real post offices that actually carry the parcels."), ("관제탑의 결정을 그대로 실행해요.", "Simply executes what the tower decides.")),
        ("VNF", "Virtual Network Function", ("범용 트럭에 설치한 소프트웨어 기능.", "A software function installed on a generic truck."), ("방화벽·분류 기능도 이렇게 돌아갈 수 있어요.", "Even a firewall or sorter can run this way.")),
        ("5G 특화망", "5G Private Network", ("한 공장만을 위한 전용 배송망.", "A delivery network dedicated to one factory."), ('이 기술로 유연하게 운영돼요. → <a href="5gprivate-ko.html">공장 전용 배송망</a>', 'Runs flexibly on this technology. → <a href="5gprivate-en.html">a delivery network just for one factory</a>')),
        ("네트워크 슬라이싱", "Network slicing", ("한 도로를 용도별 차선으로 나누는 것.", "Splitting one road into lanes by purpose."), ('소프트웨어로 길을 나누는 또 다른 활용이에요. → <a href="5gslicing-ko.html">도로를 차선으로 나누기</a>', 'Another use of software-defined roads. → <a href="5gslicing-en.html">splitting the road into lanes</a>')),
        ("방화벽", "Firewall", ("문이 많은 성벽.", "A wall with many doors."), ('NFV로 소프트웨어화되기도 하는 장비예요. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'A device often virtualized by NFV. → <a href="firewall-en.html">the wall with many doors</a>')),
    ],
}
