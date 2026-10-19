from _draw import *
from _world import *

# 1. 입주사가 "내 공간"이 필요해요 — 독채로 할지, 칸막이로 할지 고민
P1 = svg(300, sky(300)
         + building(60, 40, 1.0)
         + person(320, 188, s=0.8, face=EYES, **TENANT)
         + bubble(380, 60, 300, 60, "⟦독채 사무실로 할까, 칸막이 책상으로 할까?|a whole private office, or a partitioned desk?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦입주사는 자기만의 공간이 필요해요, 근데 방법이 두 가지예요|a tenant needs their own space — but there are two ways to get it⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 칸막이가 가볍다고 독채만큼 완전히 분리된 건 아니에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + office(300, 90, 1.0, shared=True) + office(380, 90, 1.0, shared=True)
         + person(315, 150, s=0.45, face=SMILE, **TENANT) + person(415, 150, s=0.45, face=FROWN + SWEAT, **TENANT)
         + bubble(440, 60, 260, 56, "⟦옆 칸이 너무 시끄러운데, 벽이 얇아요!|the next desk is so loud — the wall is thin!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 220, "⟦칸막이 책상은 바닥(OS)을 같이 써요|partitioned desks share the same floor (OS)⟧", 12, "var(--muted)")
         + label(380, 282, "⟦가볍다고 독채만큼 완전히 분리된 건 아니에요|lighter doesn't mean as fully separated as a private office⟧", 12, "var(--ink)"))

# 3. hero: VM = 독채 사무실(완전분리, 느림), 컨테이너 = 칸막이 책상(가볍고 빠름)
P3 = svg(380, sky(380)
         + building(30, 40, 1.0)
         + office(230, 190, 1.1, label_text="⟦VM: 독채 사무실|VM: private office⟧")
         + office(420, 190, 1.1, shared=True, label_text="⟦컨테이너: 칸막이 책상|Container: partitioned desk⟧")
         + '<rect x="230" y="150" width="130" height="10" fill="var(--stone-dark)"/>' + label(295, 142, "⟦각자 바닥(OS)|own floor (OS)⟧", 10, "var(--muted)")
         + '<rect x="420" y="150" width="130" height="10" fill="var(--good)"/>' + label(485, 142, "⟦같은 바닥(OS) 공유|shared floor (OS)⟧", 10, "var(--good)")
         + person(650, 278, s=0.7, face=EYES, **MANAGER)
         + label(380, 30, "⟦VM = 독채 사무실, 컨테이너 = 칸막이 책상이에요|VM = a private office, Container = a partitioned desk⟧", 14, "var(--ink)", cls="d")
         + label(380, 365, "⟦둘 다 '내 공간'을 나누는 방법이지만 무게가 달라요|both carve out \"your own space\" — just at different weights⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 부팅 시간·무게 비교
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦독채(VM) vs 칸막이(컨테이너)|private office (VM) vs partitioned desk (container)⟧",
                     ("⟦입주(부팅) 시간: 독채는 느림, 칸막이는 빠름|move-in time: private office is slow, partitioned desk is fast⟧",
                      "⟦바닥(OS): 독채는 각자, 칸막이는 공유|floor (OS): private office has its own, partitioned desk shares⟧",
                      "⟦무게: 독채는 무거움, 칸막이는 가벼움|weight: private office is heavy, partitioned desk is light⟧",
                      "⟦분리 수준: 독채가 더 완전함|isolation level: the private office is more complete⟧"), 1.0))

# 5. 깨지는 곳: 둘 다 쓰는 경우가 많아요 — 자동 배정(오케스트레이션)이 어디에 세울지 정해요
P5 = svg(300, sky(300)
         + building(40, 50, 0.9)
         + office(310, 190, 0.85) + office(390, 190, 0.85, shared=True) + office(460, 190, 0.85, shared=True)
         + deskbadge(650, 150, 1.1)
         + label(650, 185, "⟦자동 배정|auto-assign⟧", 11, "var(--accent)")
         + label(380, 260, "⟦실제로는 독채·칸막이를 섞어 쓰고, 어디에 세울지는 자동 배정이 정해요|real buildings mix both, and auto-assignment decides where each goes⟧", 12, "var(--ink)"))

BOOT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
WALL_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="none" stroke="var(--good)" stroke-width="5"/>')
LIGHT_I = icon('<rect x="16" y="16" width="32" height="32" rx="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><path d="M24 24 v16 M40 24 v16" stroke="var(--accent)" stroke-width="2"/>')
NOISE_I = icon('<path d="M20 44 v-24 M32 44 v-32 M44 44 v-16" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>')

PAGE = {
    "slug": "vmcontainer", "order": 2,
    "title": ("독채 사무실과 칸막이 책상", "The Private Office and the Partitioned Desk"),
    "h1": ("<em>가상머신(VM)과 컨테이너</em>가 뭐예요?", "What are <em>VMs and Containers</em>?"),
    "sub": ("가상머신(VM)과 컨테이너를, 공유 오피스 빌딩에서 독채로 할지 칸막이로 할지의 차이로 풀어봤어요.",
            "VMs and containers, told as the difference between renting a whole private office or just a partitioned desk."),
    "panels": [
        {"svg": P1, "alt": ("입주사가 독채 사무실로 할지 칸막이 책상으로 할지 고민하며 말풍선을 띄움", "A tenant wonders aloud whether to go with a whole private office or a partitioned desk"),
         "caption": ("입주사는 자기만의 공간이 필요해요, 근데 방법이 두 가지예요.", "A tenant needs their own space — but there are two ways to get it."),
         "small": ("완전히 따로 쓸지, 가볍게 나눠 쓸지예요.", "Fully separate, or lightly divided.")},
        {"svg": P2, "alt": ("칸막이 책상 두 칸 사이에서 한쪽이 옆 칸 소음이 벽을 넘어온다고 불평함", "Between two partitioned desks, one tenant complains that noise crosses the thin wall"),
         "caption": ("칸막이가 가볍다고 독채만큼 완전히 분리된 건 아니에요.", "Lighter doesn't mean as fully separated as a private office."),
         "small": ("칸막이 책상은 바닥(OS)을 같이 써요.", "Partitioned desks share the same floor (OS).")},
        {"svg": P3, "hero": True, "alt": ("건물 안에 독채 사무실(각자 바닥)과 칸막이 책상(같은 바닥 공유)이 나란히 있고 관리사무소 직원이 지켜봄", "Inside the building, a private office (its own floor) and a partitioned desk (sharing a floor) sit side by side, watched by a manager"),
         "caption": ("VM = 독채 사무실, 컨테이너 = 칸막이 책상이에요.", "VM = a private office, Container = a partitioned desk."),
         "small": ("둘 다 '내 공간'을 나누는 방법이지만 무게가 달라요.", "Both carve out \"your own space\" — just at different weights."),
         "tricks": (4, [
             (BOOT_I, ("독채는 입주(부팅)가 느려요", "A private office takes longer to move into"), ("바닥부터 다 짓거든요", "it builds its own floor from scratch"), "calm"),
             (WALL_I, ("독채는 벽이 완전히 따로예요", "A private office has fully separate walls"), ("격리가 더 확실해요", "isolation is more solid")),
             (LIGHT_I, ("칸막이는 가볍고 빨라요", "A partitioned desk is light and fast"), ("바닥을 같이 쓰니까요", "because it shares the floor"), "warm"),
             (NOISE_I, ("칸막이는 옆 칸 소음이 넘어와요", "A partitioned desk can hear next-door noise"), ("자원 경합이라고 불러요", "that's called resource contention")),
         ])},
        {"svg": P4, "alt": ("입주 안내판: 입주 시간, 바닥(OS) 공유 여부, 무게, 분리 수준을 독채와 칸막이로 비교", "A tenant board comparing move-in time, floor(OS) sharing, weight, and isolation level between private office and partitioned desk"),
         "caption": ("독채와 칸막이는 네 가지 기준에서 갈려요.", "Private office and partitioned desk differ on four measures."),
         "small": ("가벼움과 완전한 분리는 맞바꾸는 관계예요.", "Lightness and full isolation trade off against each other.")},
        {"svg": P5, "alt": ("독채 하나와 칸막이 둘이 함께 있고, 어디에 세울지 자동 배정 배지가 정함", "One private office and two partitioned desks together, with an auto-assign badge deciding where each goes"),
         "caption": ("실제로는 섞어 쓰고, 자동 배정이 어디에 세울지 정해요.", "Real buildings mix both, and auto-assignment decides where each goes."),
         "small": ("독채 vs 칸막이는 양자택일이 아니에요.", "It's not an either-or choice.")},
    ],
    "summary": (("<b>VM</b> = 바닥(OS)부터 따로인 <b>독채 사무실</b>. <b>컨테이너</b> = 바닥을 같이 쓰는 <b>가벼운 칸막이 책상</b>. 분리 수준과 무게를 맞바꿔요.",
                 "<b>VM</b> is a <b>private office</b> with its own floor (OS) from the ground up. A <b>container</b> is a <b>light, partitioned desk</b> sharing that floor. They trade isolation for weight."),
                ("가상머신(VM)은 하이퍼바이저 위에 OS까지 통째로 가상화해 완전한 격리를 주지만 무겁고 부팅이 느려요. 컨테이너는 호스트 OS 커널을 공유하며 프로세스 단위로 격리해 가볍고 빠르지만, 격리 수준은 VM보다 낮아요. 실무에선 보통 컨테이너 여러 개를 VM 안에서 돌려요.",
                 "A VM virtualizes a full OS on top of a hypervisor, giving complete isolation but at the cost of weight and slow boot. A container shares the host OS kernel and isolates at the process level — light and fast, but with weaker isolation than a VM. In practice, many containers typically run inside a single VM.")),
    "glossary": [
        ("가상머신(VM)", "Virtual Machine", ("바닥(OS)부터 완전히 따로인 독채 사무실.", "A private office with its own floor (OS) from scratch."), ("격리는 확실하지만 무겁고 느려요.", "Solid isolation, but heavy and slow.")),
        ("컨테이너", "Container", ("바닥(OS)을 같이 쓰는 칸막이 책상.", "A partitioned desk sharing the same floor (OS)."), ("가볍고 빠르지만 격리는 더 약해요.", "Light and fast, but weaker isolation.")),
        ("하이퍼바이저", "Hypervisor", ("한 건물 터에 여러 독채를 세워주는 시공사.", "The builder that puts up several private offices on one lot."), ("VM을 가능하게 하는 바탕 기술이에요.", "The underlying technology that makes VMs possible.")),
        ("자원 경합", "Resource contention", ("옆 칸 소음이 벽을 넘어오는 것.", "Next-door noise crossing a thin wall."), ("컨테이너가 바닥을 같이 쓰면서 생기는 트레이드오프예요.", "A trade-off from containers sharing the same floor.")),
        ("이미지(컨테이너 이미지)", "Container image", ("똑같이 찍어낸 책상 세트.", "A desk set stamped out identically every time."), ('성 세계에서는 짐칸이라고 불러요. → <a href="container-ko.html">똑같이 찍어낸 짐칸</a>', 'In the castle world, this is called a crate. → <a href="container-en.html">crates from the same mold</a>')),
        ("오케스트레이션", "Orchestration", ("어디에 몇 칸 세울지 정하는 관리사무소.", "The office deciding how many desks go where."), ('독채·칸막이를 실제로 배치하는 역할이에요. → <a href="k8s-ko.html">자동 좌석 배정 배지</a>', 'The role that actually places offices and desks. → <a href="k8s-en.html">the auto-assignment badge</a>')),
        ("서버리스", "Serverless", ("아예 입주할 필요도 없는 시간제 회의실.", "A time-rented meeting room where you don't move in at all."), ('독채·칸막이보다 한 단계 더 가벼워요. → <a href="serverless-ko.html">시간제 회의실</a>', "A step lighter than either office type. → <a href=\"serverless-en.html\">the hourly meeting room</a>")),
        ("스케일 업/아웃", "Scale-up / Scale-out", ("사무실을 키울지, 더 빌릴지.", "Making one office bigger, or renting more of them."), ('독채는 스케일업, 칸막이는 스케일아웃에 더 잘 맞아요. → <a href="scaleupout-ko.html">사무실을 키울까 더 빌릴까</a>', 'Private offices fit scale-up; partitioned desks fit scale-out. → <a href="scaleupout-en.html">bigger office or more offices</a>')),
    ],
}
