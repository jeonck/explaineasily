from _draw import *
from _world import *

# 1. 새 상품을 위해 벽을 다시 지어야 해요
P1 = svg(300, sky(300)
         + shelfzone(260, 140, 240, 90, 1.1)
         + person(560, 170, s=0.8, face=SWEAT + EYES, **MANAGER)
         + label(560, 278, "⟦새 상품 줄엔 선반·통로를 다시 지어야 해요|the new product line needs the shelves and aisles rebuilt⟧", 12, "var(--ink)")
         + label(380, 40, "⟦벽을 허물고 다시 짓는 건 몇 주가 걸려요|tearing down and rebuilding walls takes weeks⟧", 13, "var(--bad)"))

# 2. 물리 벽·통로·문은 한번 지으면 바꾸기 어려워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + gate(620, 160, 0.9)
         + shelfzone(100, 150, 220, 80, 1.0)
         + person(380, 170, s=0.8, face=FROWN, **MANAGER)
         + label(380, 280, "⟦공사하는 동안은 창고를 못 써요|while under construction, the warehouse is unusable⟧", 12, "var(--bad)"))

# 3. SDDC = 선반·통로·일손 배분을 전부 소프트웨어 설정으로 (hero)
P3 = svg(340, sky(340, ground=False)
         + '<rect x="250" y="60" width="260" height="160" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + '<rect x="268" y="78" width="100" height="50" rx="3" fill="var(--good-soft)"/>' + label(318, 108, "⟦선반 배치|shelf layout⟧", 10, "#142033")
         + '<rect x="378" y="78" width="110" height="50" rx="3" fill="var(--accent-soft)"/>' + label(433, 108, "⟦통로/문|aisles/doors⟧", 10, "#142033")
         + '<rect x="268" y="140" width="220" height="50" rx="3" fill="#FFF8E7"/>' + label(378, 170, "⟦일손 배분|work assignment⟧", 10, "#142033")
         + person(380, 230, s=0.7, face=EYES, **MANAGER)
         + label(380, 30, "⟦SDDC = 선반·통로·일손 배분을 전부 화면 설정으로 바꾸기|SDDC = reconfiguring shelves, aisles, and staffing entirely through software settings⟧", 12.5, "var(--ink)", cls="d")
         + label(380, 330, "⟦벽 대신 코드로 창고를 다시 지어요|rebuilding the warehouse with code instead of walls⟧", 12, "var(--muted)"))

# 4. 물리 공사 vs 설정 변경
P4 = svg(320, sky(320, ground=False)
         + '<rect x="40" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="390" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(205, 66, "⟦물리 레이아웃 변경|physical reconfiguration⟧", 12, "var(--ink)", weight=700)
         + label(555, 66, "⟦소프트웨어 설정 변경|software reconfiguration⟧", 12, "var(--ink)", weight=700)
         + label(205, 110, "⟦공사, 몇 주|construction, weeks⟧", 12, "var(--bad)")
         + label(205, 150, "⟦그 동안 창고 사용 중단|warehouse unusable meanwhile⟧", 10.5, "var(--muted)")
         + label(555, 110, "⟦버튼 몇 개, 몇 분|a few clicks, minutes⟧", 12, "var(--good)")
         + label(555, 150, "⟦설정값을 코드로 저장해 재현 가능|settings saved as code, reproducible⟧", 10.5, "var(--muted)")
         + label(380, 220, "⟦선반·통로·일손 배분 전부를 설정으로 바꿔요|shelf layout, aisles, and staffing — all become settings⟧", 12, "var(--ink)")
         + label(380, 255, "⟦이 설정을 코드로 저장해두는 게 코드형 인프라예요|saving these settings as code is infrastructure as code⟧", 11, "var(--muted)"))

# 5. 바닥의 실제 서버는 여전히 물리적으로 존재해요
P5 = svg(300, sky(300, ground=False)
         + shelfzone(260, 180, 240, 70, 1.0)
         + person(380, 130, s=0.75, face=EYES, **MANAGER)
         + label(380, 260, "⟦바닥의 실제 선반·배선은 여전히 물리적으로 있어요|the real shelves and wiring underneath still physically exist⟧", 12, "var(--ink)")
         + label(380, 40, "⟦설정 실수 하나가 창고 전체로 바로 퍼질 수도 있어요|one bad setting can spread across the whole warehouse at once⟧", 12.5, "var(--bad)"))

STORE_I = icon('<rect x="10" y="20" width="44" height="30" rx="3" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/><path d="M18 30 h28 M18 40 h28" stroke="var(--good)" stroke-width="2.5"/>')
NET_I = icon('<circle cx="16" cy="20" r="7" fill="var(--accent)"/><circle cx="48" cy="20" r="7" fill="var(--accent)"/><circle cx="32" cy="48" r="7" fill="var(--accent)"/><path d="M16 20 L48 20 M16 20 L32 48 M48 20 L32 48" stroke="var(--muted)" stroke-width="2.5"/>')
COMPUTE_I = icon('<rect x="14" y="14" width="36" height="24" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="24" cy="46" r="6" fill="var(--good)"/><circle cx="40" cy="46" r="6" fill="var(--good)"/>')
CODE_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 24 l-6 8 l6 8 M42 24 l6 8 l-6 8" stroke="var(--accent)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "sddc", "order": 16,
    "title": ("소프트웨어로 다시 짓는 창고", "The Warehouse Rebuilt by Software"),
    "h1": ("<em>SDDC</em>가 뭐예요?", "What is <em>SDDC</em>?"),
    "sub": ("SDDC(소프트웨어 정의 데이터센터)를, 벽을 허물지 않고 화면 설정만으로 선반·통로·일손 배분을 바꾸는 차세대 창고 이야기로 풀어봤어요.",
            "SDDC (Software-Defined Data Center), told as a story about a next-generation warehouse that reconfigures its shelves, aisles, and staffing through software settings — no walls torn down."),
    "panels": [
        {"svg": P1, "alt": ("관리자가 새 상품 줄을 위해 선반과 통로를 다시 지어야 해서 땀을 흘림", "The manager sweats, needing to rebuild shelves and aisles for a new product line"),
         "caption": ("새 상품 줄엔 선반·통로를 다시 지어야 해요.", "The new product line needs the shelves and aisles rebuilt."),
         "small": ("벽을 허물고 다시 짓는 건 몇 주가 걸려요.", "Tearing down and rebuilding walls takes weeks.")},
        {"svg": P2, "alt": ("문과 선반이 있는 창고 앞에서 관리자가 곤란해하며, 공사 중이라 창고를 못 씀", "The manager is stuck in front of the gate and shelves — unusable during construction"),
         "caption": ("물리 벽·통로·문은 한번 지으면 바꾸기 어려워요.", "Physical walls, aisles, and doors are hard to change once built."),
         "small": ("공사하는 동안은 창고를 못 써요.", "While under construction, the warehouse is unusable.")},
        {"svg": P3, "hero": True, "alt": ("관리자가 화면 패널에서 선반 배치, 통로/문, 일손 배분을 한 번에 설정함", "The manager configures shelf layout, aisles/doors, and staffing all from one screen panel"),
         "caption": ("SDDC는 선반·통로·일손 배분을 전부 화면 설정으로 바꿔요.", "SDDC reconfigures shelves, aisles, and staffing entirely through software settings."),
         "small": ("벽 대신 코드로 창고를 다시 지어요.", "Rebuilding the warehouse with code instead of walls."),
         "tricks": (4, [
             (STORE_I, ("선반 배치를 설정으로", "Shelf layout as a setting"), ("스토리지 가상화예요", "storage virtualization")),
             (NET_I, ("통로를 설정으로", "Aisles as a setting"), ("네트워크 가상화(SDN)예요", "network virtualization (SDN)"), "calm"),
             (COMPUTE_I, ("일손 배분을 설정으로", "Staffing as a setting"), ("컴퓨팅 가상화예요", "compute virtualization")),
             (CODE_I, ("설정 자체를 코드로 저장", "Save the settings as code"), ("코드형 인프라예요", "infrastructure as code"), "warm"),
         ])},
        {"svg": P4, "alt": ("물리 레이아웃 변경(몇 주)과 소프트웨어 설정 변경(몇 분)을 나란히 비교함", "Physical reconfiguration (weeks) compared side by side with software reconfiguration (minutes)"),
         "caption": ("선반·통로·일손 배분 전부를 설정으로 바꿔요.", "Shelf layout, aisles, and staffing all become settings."),
         "small": ("이 설정을 코드로 저장해두는 게 코드형 인프라예요.", "Saving these settings as code is infrastructure as code.")},
        {"svg": P5, "alt": ("관리자가 화면 앞에 서 있지만, 바닥에는 여전히 실제 선반이 존재함", "The manager stands at the screen, but the real shelves still exist on the floor below"),
         "caption": ("바닥의 실제 서버·배선은 여전히 물리적으로 있어요.", "The real servers and wiring underneath still physically exist."),
         "small": ("설정 실수 하나가 창고 전체로 바로 퍼질 수도 있어요.", "One bad setting can spread across the whole warehouse at once.")},
    ],
    "summary": (("<b>SDDC</b>(소프트웨어 정의 데이터센터)는 스토리지·네트워크·컴퓨팅을 <b>전부 소프트웨어 설정으로 가상화</b>해, 물리 공사 없이 바로 재구성하는 데이터센터예요.",
                 "<b>SDDC</b> (Software-Defined Data Center) <b>virtualizes storage, network, and compute entirely through software settings</b>, letting the whole center be reconfigured instantly without physical construction."),
                ("SDDC는 스토리지 가상화(SDS), 네트워크 가상화(SDN), 컴퓨팅 가상화를 하나의 관리 소프트웨어로 통합하고, 그 설정을 코드로 저장(IaC)해 반복 가능하게 만들어요. 다만 그 아래 실제 서버·디스크·케이블은 여전히 물리적으로 존재하며, 설정 실수 하나의 파급 범위(blast radius)가 더 넓어질 수 있다는 점은 유의해야 해요.",
                 "SDDC unifies storage virtualization (SDS), network virtualization (SDN), and compute virtualization under one management layer, and saves those settings as code (IaC) to make them reproducible. The underlying physical servers, disks, and cables still exist, though — and a single misconfiguration's blast radius can reach further than before.")),
    "glossary": [
        ("가상화", "Virtualization", ("물리 자원을 소프트웨어로 나누기.", "Carving up physical resources in software."), ("SDDC의 가장 기본적인 토대예요.", "The basic foundation SDDC is built on.")),
        ("SDN", "SDN", ("통로를 설정으로 바꾸는 네트워크.", "A network whose aisles are set in software."), ("물리 배선 없이 경로를 바꿔요.", "Reroutes traffic without touching wiring.")),
        ("소프트웨어 정의 스토리지", "SDS", ("선반 배치를 설정으로 바꾸기.", "Shelf layout set in software."), ("디스크 묶음을 논리적으로 재구성해요.", "Reorganizes disk pools logically.")),
        ("코드형 인프라", "Infrastructure as Code", ("설정 자체를 코드로 저장.", "The settings themselves, saved as code."), ('SRE 세계에서도 핵심 도구예요. → <a href="iac-ko.html">코드로 짓는 놀이공원</a>', 'A core tool in the SRE world too. → <a href="iac-en.html">building the theme park with code</a>')),
        ("하이퍼컨버지드 인프라", "HCI", ("선반·통로·일손을 한 상자에.", "Shelf, aisle, and staffing bundled into one box."), ("SDDC를 더 작은 단위로 묶은 형태예요.", "A smaller, bundled form of SDDC.")),
        ("프라이빗 클라우드와의 관계", "Relation to Private Cloud", ("자체 창고를 클라우드처럼.", "Running your own warehouse like a cloud."), ("SDDC는 프라이빗 클라우드의 기반이 돼요.", "SDDC is the foundation many private clouds sit on.")),
        ("블라스트 레이디어스", "Blast Radius", ("설정 실수가 퍼지는 범위.", "How far a misconfiguration spreads."), ("가상화된 만큼 파급 범위도 넓어져요.", "The more virtualized, the wider it can spread.")),
        ("자동 프로비저닝", "Automated Provisioning", ("요청 한 번으로 자원을 갖추기.", "Standing up resources from a single request."), ("설정 코드로 창고를 자동으로 갖춰요.", "Settings-as-code stands the warehouse up automatically.")),
    ],
}
