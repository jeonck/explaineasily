from _draw import *
from _world import *

# 1. 자동 배정 배지는 있는데, 이름도 쓰임새도 제각각이에요
P1 = svg(355, sky(355)
         + deskbadge(200, 150, 1.3) + deskbadge(400, 150, 1.0) + deskbadge(560, 160, 0.8)
         + person(380, 240, s=0.8, face=EYES, **MANAGER)
         + bubble(420, 70, 280, 60, "⟦자동 배정 배지만 여러 회사가 각자 만들어요|lots of companies each make their own auto-assign badge⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 337, "⟦자동 배정 배지(오케스트레이션)는 여러 회사가 각자 만들어요|auto-assign badges — orchestration — come from many different companies⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 다 다르면 입주사가 뭘 믿고 골라야 할지 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 150, s=0.8, face=FROWN + SWEAT, **TENANT)
         + bubble(100, 60, 260, 60, "⟦이 배지는 설명서가 부실해요|this badge's manual is thin⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + bubble(400, 60, 260, 60, "⟦이건 쓰는 회사가 거의 없어요|hardly anyone uses this one⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦제각각이면 뭘 믿고 골라야 할지 몰라요|all different, and nobody knows which one to trust⟧", 12, "var(--ink)"))

# 3. hero: 쿠버네티스 = 가장 널리 쓰이는 그 자동 배정 배지의 "실제 제품 이름"
P3 = svg(380, sky(380)
         + deskbadge(380, 150, 2.0)
         + label(380, 220, "⟦쿠버네티스(Kubernetes)|Kubernetes⟧", 16, "var(--accent)", cls="d")
         + person(180, 278, s=0.7, face=SMILE, **TENANT) + person(580, 278, s=0.7, face=SMILE, **TENANT)
         + label(380, 30, "⟦이 자동 배정 배지의 가장 유명한 실제 제품이 쿠버네티스예요|Kubernetes is the most famous real product behind this auto-assign badge⟧", 13, "var(--ink)", cls="d")
         + label(380, 365, "⟦여러 건물이 같은 쿠버네티스를 표준처럼 써요|many buildings use this same Kubernetes as a shared standard⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 쿠버네티스 용어 지도 — Pod/Node/Deployment/Service/Namespace
P4 = svg(340, sky(340)
         + floorplan(60, 20, 640, 300, "⟦쿠버네티스 용어 지도|Kubernetes term map⟧",
                     ("⟦파드(Pod) = 한 입주사의 최소 칸막이 묶음|Pod = one tenant's smallest bundle of partitioned desks⟧",
                      "⟦노드(Node) = 그 칸막이들이 놓인 바닥 한 칸(서버 한 대)|Node = the one floor slab (one server) those desks sit on⟧",
                      "⟦디플로이먼트(Deployment) = 몇 자리를 항상 유지할지 규칙|Deployment = the rule for how many spots to always keep running⟧",
                      "⟦서비스(Service) = 어느 칸이든 찾아주는 안내 데스크|Service = the front desk that finds the right spot no matter which⟧",
                      "⟦네임스페이스(Namespace) = 층별로 나눈 구역 구분|Namespace = the way floors are split into separate zones⟧"), 1.0))

# 5. 깨지는 곳: 쿠버네티스 자체가 복잡한 시스템 — 작은 팀엔 과해요
P5 = svg(355, '<rect width="380" height="355" fill="var(--good-soft)"/><rect x="380" width="380" height="355" fill="var(--accent-soft)"/>'
         + office(100, 190, 0.85) + person(60, 268, s=0.55, face=SMILE, **TENANT)
         + label(190, 335, "⟦사무실 1~2칸뿐이면 사람이 직접 관리해도 충분해요|with just 1-2 offices, managing by hand is still enough⟧", 11, "var(--ink)")
         + deskbadge(570, 180, 1.2) + person(650, 240, s=0.55, face=FROWN + SWEAT, **TENANT)
         + label(570, 335, "⟦쿠버네티스 자체를 배우고 운영하는 비용이 꽤 커요|learning and running Kubernetes itself is a real cost⟧", 11, "var(--ink)"))

POD_I = icon('<rect x="14" y="20" width="16" height="24" rx="2" fill="var(--good)"/><rect x="34" y="20" width="16" height="24" rx="2" fill="var(--good)"/>')
NODE_I = icon('<rect x="8" y="40" width="48" height="12" fill="var(--stone-dark)"/>')
DEPLOY_I = icon('<rect x="12" y="6" width="40" height="52" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="42" font-size="24" font-weight="800" text-anchor="middle" fill="var(--accent)">3</text>')
SERVICE_I = icon('<circle cx="32" cy="32" r="20" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><path d="M24 32 h16 M32 24 v16" stroke="var(--accent)" stroke-width="3"/>')

PAGE = {
    "slug": "k8s", "order": 10,
    "title": ("자동 배정 배지의 그 유명한 제품 이름", "The Famous Brand Name Behind the Auto-Assign Badge"),
    "h1": ("<em>쿠버네티스(Kubernetes)</em>가 뭐예요?", "What is <em>Kubernetes</em>?"),
    "sub": ("쿠버네티스를, 자동 좌석 배정 배지 중 가장 널리 쓰이는 실제 제품 이름 이야기로 풀어봤어요.",
            "Kubernetes, told as a story about the most widely used real product behind the auto-assign badge."),
    "panels": [
        {"svg": P1, "alt": ("자동 배정 배지 세 종류가 각자 다른 모양으로 놓여 있고 관리사무소 직원이 회사마다 제각각 만든다고 말함", "Three different-looking auto-assign badges sit together, with a manager noting every company makes its own"),
         "caption": ("자동 배정 배지는 여러 회사가 각자 만들어요.", "Auto-assign badges come from many different companies."),
         "small": ("모양도, 쓰는 법도 다 제각각이에요.", "Different shapes, different ways to use them.")},
        {"svg": P2, "alt": ("땀 흘리는 입주사가 설명서가 부실하거나 쓰는 회사가 거의 없는 배지들을 보며 뭘 골라야 할지 모름", "A sweating tenant, looking at badges with thin manuals or hardly any users, doesn't know which to pick"),
         "caption": ("제각각이면 뭘 믿고 골라야 할지 몰라요.", "All different, and nobody knows which one to trust."),
         "small": ("표준처럼 다들 쓰는 게 하나 있으면 좋겠어요.", "It'd help if there were one everyone uses, like a standard.")},
        {"svg": P3, "hero": True, "alt": ("가장 큰 자동 배정 배지에 쿠버네티스라는 이름이 붙어 있고 양옆 입주사들이 웃고 있음", "The largest auto-assign badge bears the name Kubernetes, with tenants smiling on either side"),
         "caption": ("쿠버네티스는 이 배지의 가장 유명한 실제 제품이에요.", "Kubernetes is the most famous real product behind this auto-assign badge."),
         "small": ("여러 건물이 같은 쿠버네티스를 표준처럼 써요.", "Many buildings use this same Kubernetes as a shared standard."),
         "tricks": (4, [
             (POD_I, ("파드 = 최소 묶음 단위", "Pod = the smallest bundle"), ("칸막이 몇 개를 한데 묶어요", "a few partitioned desks bundled together"), "calm"),
             (NODE_I, ("노드 = 바닥 한 칸(서버 한 대)", "Node = one floor slab (one server)"), ("파드가 올라서는 바닥이에요", "the floor the pods stand on")),
             (DEPLOY_I, ("디플로이먼트 = 몇 자리 유지할지 규칙", "Deployment = the rule for how many to keep"), ("숫자 하나만 정하면 돼요", "just set one number"), "warm"),
             (SERVICE_I, ("서비스 = 어디든 찾아주는 안내 데스크", "Service = the front desk that finds any spot"), ("자리가 바뀌어도 안내는 그대로예요", "the front desk stays put even if the spot moves")),
         ])},
        {"svg": P4, "alt": ("파드·노드·디플로이먼트·서비스·네임스페이스를 사무실 비유로 정리한 쿠버네티스 용어 지도", "A Kubernetes term map matching Pod, Node, Deployment, Service, and Namespace to office analogies"),
         "caption": ("쿠버네티스에는 이런 전용 용어들이 있어요.", "Kubernetes has its own set of specific terms."),
         "small": ("파드·노드·디플로이먼트·서비스·네임스페이스, 다섯 가지예요.", "Pod, Node, Deployment, Service, Namespace — five terms.")},
        {"svg": P5, "alt": ("왼쪽: 사무실 1~2칸뿐인 입주사는 사람이 직접 관리해도 충분해 웃음. 오른쪽: 쿠버네티스 자체를 배우고 운영하는 비용이 커서 땀 흘림", "Left: a tenant with just 1-2 offices manages fine by hand, smiling. Right: learning and running Kubernetes itself costs a lot, tenant sweating"),
         "caption": ("쿠버네티스 자체가 복잡한 시스템이에요.", "Kubernetes is itself a complex system."),
         "small": ("사무실 1~2칸뿐인 작은 팀엔 오히려 과해요.", "For a small team with just 1-2 offices, it's overkill.")},
    ],
    "summary": (("<b>쿠버네티스</b> = 자동 배정 배지(오케스트레이션)라는 <b>개념을 실제로 구현한 가장 유명한 제품 이름</b>. 파드·노드·디플로이먼트 같은 전용 용어를 써요.",
                 "<b>Kubernetes</b> is the <b>most famous actual product implementing</b> the auto-assign-badge concept — orchestration. It has its own vocabulary: Pod, Node, Deployment, and more."),
                ("쿠버네티스는 컨테이너 오케스트레이션의 사실상 표준 플랫폼이에요. 컨테이너 묶음인 파드, 그 파드가 올라가는 서버인 노드, 원하는 파드 개수를 선언하는 디플로이먼트, 파드 위치가 바뀌어도 고정된 진입점을 제공하는 서비스, 자원을 논리적으로 나누는 네임스페이스로 구성돼요. '자동으로 재시작하고 자리를 배정한다'는 일반 개념 자체는 다른 플랫폼에도 있지만, 그 대표 브랜드가 쿠버네티스예요.",
                 "Kubernetes is the de facto standard platform for container orchestration. It's built from Pods (bundles of containers), Nodes (the servers pods run on), Deployments (declaring how many pod replicas you want), Services (a fixed entry point even as pod locations change), and Namespaces (logical partitions of resources). The general concept — \"restart automatically and place things for you\" — exists in other platforms too, but Kubernetes is its leading brand.")),
    "glossary": [
        ("쿠버네티스", "Kubernetes", ("가장 유명한 자동 배정 배지 제품.", "The most famous auto-assign-badge product."), ("컨테이너 오케스트레이션의 사실상 표준이에요.", "The de facto standard for container orchestration.")),
        ("파드(Pod)", "Pod", ("칸막이 몇 개를 한데 묶은 최소 단위.", "The smallest bundle — a few partitioned desks together."), ("쿠버네티스가 다루는 가장 작은 단위예요.", "The smallest unit Kubernetes manages.")),
        ("노드(Node)", "Node", ("파드가 올라서는 바닥 한 칸(서버 한 대).", "The floor slab (one server) a pod stands on."), ("여러 노드가 모여 하나의 건물(클러스터)을 이뤄요.", "Many nodes together form one building — a cluster.")),
        ("디플로이먼트(Deployment)", "Deployment", ("몇 자리를 항상 유지할지 정하는 규칙.", "The rule for how many spots to always keep running."), ("숫자만 바꾸면 나머지는 쿠버네티스가 해요.", "Change the number, and Kubernetes does the rest.")),
        ("서비스(Service)", "Service", ("자리가 바뀌어도 그대로인 안내 데스크.", "The front desk that stays put even if the spot moves."), ("파드 위치가 바뀌어도 찾아가는 길은 그대로예요.", "The way in stays the same even as pods move around.")),
        ("네임스페이스(Namespace)", "Namespace", ("층별로 나눈 구역 구분.", "The way floors are split into zones."), ("같은 건물 안에서 팀별로 자원을 나눠요.", "Splits resources by team within the same building.")),
        ("오케스트레이션", "Orchestration", ("자동 배정이라는 일반 개념 자체.", "The general concept of auto-assignment itself."), ('쿠버네티스는 그 개념의 대표 제품이에요. SRE 세계에서 개념 자체를 다뤄요. → <a href="orchestration-ko.html">몇 대를 켤지 정하는 운영 본부</a>', 'Kubernetes is the flagship product for that concept — the concept itself is covered in the SRE world. → <a href="orchestration-en.html">the operations center that decides how many to run</a>')),
        ("가상머신/컨테이너", "VM / Container", ("독채 사무실과 칸막이 책상.", "The private office and the partitioned desk."), ('쿠버네티스가 자동으로 배치해주는 대상이 바로 이 칸막이(컨테이너)예요. → <a href="vmcontainer-ko.html">독채 사무실과 칸막이 책상</a>', "The partitioned desks (containers) are exactly what Kubernetes places automatically. → <a href=\"vmcontainer-en.html\">the private office and the partitioned desk</a>")),
    ],
}
