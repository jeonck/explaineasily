from _draw import *
from _world import *

# 1. 소포가 도착할 때마다 벨이 울려요
P1 = svg(300, sky(300)
         + postoffice(260, 160, 0.8)
         + person(440, 170, s=0.85, face=EYES, **SORTER)
         + envelope(360, 230, 0.6) + '<circle cx="330" cy="150" r="14" fill="var(--accent)"/>' + label(330, 154, "⟦땡!|DING!⟧", 10, "#fff", cls="d")
         + label(380, 30, "⟦소포가 도착할 때마다 벨이 울려 직원이 하던 일을 멈춰요|a bell rings on every arrival, pulling the clerk off whatever they were doing⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦하나하나 즉시 알려주니 놓치는 일은 없어요|nothing gets missed — every arrival is flagged right away⟧", 12, "var(--muted)"))

# 2. 트럭이 너무 빨라지면 벨이 쉴 새 없이 울려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + truck(260, 200, 0.9, fast=True)
         + person(460, 170, s=0.85, face=SWEAT + EYES, **SORTER)
         + '<circle cx="400" cy="140" r="12" fill="var(--bad)"/><circle cx="420" cy="150" r="12" fill="var(--bad)"/><circle cx="440" cy="140" r="12" fill="var(--bad)"/>'
         + label(460, 250, "⟦벨이 쉴 새 없이 울려 다른 일을 전혀 못 해요|the bell never stops — there's no time for anything else⟧", 11, "var(--ink)")
         + label(380, 30, "⟦초고속 트럭이 초당 수천 통을 배달하면 벨이 폭주해요|an ultra-fast truck delivering thousands a second floods the bell⟧", 13, "var(--ink)", cls="d"))

# 3. 네트워크 인터럽트 = 도착 벨, 너무 잦으면 모아서 울림 (hero)
P3 = svg(340, sky(340)
         + postoffice(260, 170, 0.7)
         + person(460, 190, s=0.8, face=EYES, **SORTER)
         + envelope(360, 210, 0.5) + envelope(385, 225, 0.5) + envelope(410, 215, 0.5)
         + '<circle cx="330" cy="150" r="14" fill="var(--accent)"/>' + label(330, 154, "⟦땡!|DING!⟧", 10, "#fff", cls="d")
         + label(380, 30, "⟦네트워크 인터럽트 = 소포 도착을 즉시 알리는 벨소리|a network interrupt = the bell announcing an arrival right away⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦너무 자주 울리면 오히려 방해되니, 모아서 한 번에 울리기도 해요(인터럽트 코얼레싱)|too frequent becomes a nuisance — so sometimes several ring as one (interrupt coalescing)⟧", 12, "var(--muted)"))

# 4. 매번 벨 vs 모아서 벨 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦매번 벨(코얼레싱 없음)|Ring every time (no coalescing)⟧",
                    ("⟦소포 1통마다 벨 1번|one ring per parcel⟧",
                     "⟦개별 소식은 즉시 앎|know about each one instantly⟧",
                     "⟦트럭 빨라지면 벨 폭주|a faster truck floods the bell⟧",
                     "⟦직원이 다른 일 못 함|clerk can't do anything else⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦모아서 벨(코얼레싱)|Coalesced ring⟧",
                    ("⟦소포 여러 통에 벨 1번|one ring for several parcels⟧",
                     "⟦전체 처리량은 늘어남|overall throughput improves⟧",
                     "⟦개별 소식은 살짝 늦게 앎|each one is known a bit later⟧",
                     "⟦직원이 다른 일도 할 수 있음|clerk can handle other work too⟧"), 1.0, hl=1))

# 5. 지연과 처리량은 맞바꾸는 관계예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 160, s=0.8, face=SMILE, **SORTER) + label(190, 240, "⟦모아서 울리면 전체 일은 더 잘 처리해요|coalescing lets the clerk handle the overall load better⟧", 11, "var(--ink)")
         + envelope(570, 160, 0.6) + label(570, 240, "⟦대신 소포 한 통 한 통은 조금 늦게 알려져요|but each single parcel is flagged a little later⟧", 11, "var(--ink)")
         + label(380, 282, "⟦CPU가 프로그램 실행 중 멈추는 인터럽트(시스템SW 세계)와는 또 다른 이야기예요|a different story from the interrupt that pauses a CPU mid-program (the Systems world)⟧", 12, "var(--ink)", cls="d"))

BELL_I = icon('<path d="M32 12 a14 14 0 0 1 14 14 v8 l6 10 h-40 l6 -10 v-8 a14 14 0 0 1 14 -14z" fill="var(--accent)"/><circle cx="32" cy="50" r="4" fill="var(--ink)"/>')
STOP_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M22 32 h20" stroke="var(--bad)" stroke-width="4"/>')
STORM_I = icon('<circle cx="18" cy="24" r="9" fill="var(--bad)"/><circle cx="34" cy="20" r="9" fill="var(--bad)"/><circle cx="48" cy="26" r="9" fill="var(--bad)"/>')
BATCH_I = icon('<rect x="10" y="26" width="12" height="18" fill="var(--good)"/><rect x="26" y="20" width="12" height="24" fill="var(--good)"/><rect x="42" y="30" width="12" height="14" fill="var(--good)"/><path d="M8 50 h48" stroke="var(--ink)" stroke-width="2"/>')

PAGE = {
    "slug": "interruptnet", "order": 9,
    "title": ("소포가 도착했다고 알리는 벨소리", "The Bell That Says a Parcel Just Arrived"),
    "h1": ("<em>인터럽트(네트워크 I/O)</em>가 뭐예요?", "What is an <em>Interrupt</em> (Network I/O)?"),
    "sub": ("네트워크 카드의 인터럽트를, 소포가 도착할 때마다 울리는 벨소리 이야기로 풀어봤어요.",
            "A network card's interrupt, told as a story about a bell that rings every time a parcel arrives."),
    "panels": [
        {"svg": P1, "alt": ("소포가 도착하자 벨이 울리고 분류소 직원이 하던 일을 멈춤", "A bell rings as a parcel arrives, and the sorting clerk stops what they were doing"),
         "caption": ("소포가 도착할 때마다 벨이 울려요.", "A bell rings every time a parcel arrives."),
         "small": ("하나하나 즉시 알려주니 놓치는 일은 없어요.", "Nothing gets missed — every arrival is flagged right away.")},
        {"svg": P2, "alt": ("초고속 트럭이 쏟아내는 소포에 벨이 연달아 세 번 울려 직원이 진땀을 흘림", "An ultra-fast truck unloads parcels so fast the bell rings three times in a row, and the clerk sweats"),
         "caption": ("트럭이 너무 빨라지면 벨이 쉴 새 없이 울려요.", "A faster truck makes the bell ring nonstop."),
         "small": ("초당 수천 통을 배달하면 벨이 폭주해요.", "Delivering thousands a second floods the bell.")},
        {"svg": P3, "hero": True, "alt": ("소포가 도착하자 벨이 울리고, 소포 여러 통이 모여 있는 모습", "A bell rings on arrival, and several parcels are shown gathered together"),
         "caption": ("도착을 즉시 알리는 벨소리, 너무 잦으면 모아서 울려요.", "The bell announces arrivals right away — or, when too frequent, several ring as one."),
         "small": ("너무 자주 울리면 오히려 방해되니, 모아서 한 번에 울리기도 해요.", "Too frequent becomes a nuisance, so sometimes several ring as one."),
         "tricks": (4, [
             (BELL_I, ("즉시 알림", "Immediate notification"), ("도착 즉시 벨이 울려요", "the bell rings the instant it arrives"), "calm"),
             (STOP_I, ("하던 일 중단", "Interrupts current work"), ("직원이 하던 일을 멈추고 처리해요", "the clerk stops what they're doing to handle it")),
             (STORM_I, ("인터럽트 폭주", "Interrupt storm"), ("너무 잦으면 업무가 마비돼요", "too frequent, and all other work stalls"), "warm"),
             (BATCH_I, ("모아서 처리(코얼레싱)", "Coalescing"), ("소포 여럿이 모이면 벨 한 번만 울려요", "several parcels gathered trigger just one ring")),
         ])},
        {"svg": P4, "alt": ("매번 벨 울리기와 모아서 벨 울리기(코얼레싱)를 비교한 두 안내판", "Two boards comparing ringing every time versus coalesced ringing"),
         "caption": ("매번 울리기와 모아서 울리기는 다르게 작동해요.", "Ringing every time and coalescing work differently."),
         "small": ("모아서 울리면 전체 처리량은 늘지만, 개별 소식은 조금 늦어요.", "Coalescing improves overall throughput, but each single arrival is known a bit later.")},
        {"svg": P5, "alt": ("왼쪽: 모아서 울리면 전체 일을 더 잘 처리함. 오른쪽: 소포 한 통의 소식은 조금 늦게 알려짐", "Left: coalescing lets the clerk handle the overall load better. Right: a single parcel's news comes a bit later"),
         "caption": ("지연과 처리량은 맞바꾸는 관계예요.", "Latency and throughput trade off against each other."),
         "small": ("CPU가 프로그램 실행 중 멈추는 인터럽트(시스템SW 세계)와는 또 다른 이야기예요.", "A different story from the interrupt that pauses a CPU mid-program, covered in the Systems world.")},
    ],
    "summary": (("네트워크 I/O의 <b>인터럽트</b>는 <b>소포(패킷)가 도착했다고 즉시 알리는 벨소리</b>이고, 너무 잦으면 <b>모아서 한 번에 울리기(코얼레싱)</b>도 해요.",
                 "A network I/O <b>interrupt</b> is <b>the bell that announces a parcel (packet) has arrived right away</b> — and when it rings too often, several are <b>coalesced into one ring</b> instead."),
                ("네트워크 카드(NIC)는 패킷이 도착할 때마다 CPU에 인터럽트를 걸어 즉시 처리하게 해요. 트래픽이 아주 많아지면 인터럽트가 너무 잦아져 CPU가 다른 일을 못 하는 '인터럽트 폭풍'이 생기는데, 이를 막기 위해 패킷 여러 개를 모았다가 인터럽트를 한 번만 거는 '인터럽트 코얼레싱(interrupt coalescing)'을 써요. 지연은 조금 늘지만 전체 처리량(throughput)은 좋아져요. 이건 CPU가 프로그램 실행 중 입출력 신호로 멈추는 일반적인 인터럽트와는 별개로, 네트워크 I/O에 특화된 이야기예요.",
                 "A network interface card (NIC) raises a CPU interrupt on every packet arrival so it gets handled right away. Under very heavy traffic, interrupts fire so often the CPU can't do anything else — an 'interrupt storm.' To prevent this, interrupt coalescing batches several packets and raises just one interrupt for the group, trading a bit of latency for better overall throughput. This is distinct from the general CPU interrupt that pauses a running program for I/O — this one is specific to network I/O.")),
    "glossary": [
        ("네트워크 인터럽트", "Network interrupt", ("소포 도착을 즉시 알리는 벨소리.", "The bell that announces a parcel's arrival right away."), ("NIC가 CPU에 거는 신호예요.", "A signal the NIC raises to the CPU.")),
        ("인터럽트 폭풍", "Interrupt storm", ("벨이 쉴 새 없이 울려 업무가 마비되는 것.", "The bell ringing nonstop until all other work stalls."), ("트래픽이 아주 많을 때 생겨요.", "Happens under very heavy traffic.")),
        ("인터럽트 코얼레싱", "Interrupt coalescing", ("소포 여럿을 모아 벨 한 번만 울리는 것.", "Gathering several parcels and ringing the bell just once."), ("지연은 늘지만 처리량이 좋아져요.", "Adds some latency but improves throughput.")),
        ("NIC", "Network Interface Card", ("벨을 울리는 소포 접수 창구.", "The receiving window that rings the bell."), ("패킷이 도착하는 실제 하드웨어예요.", "The actual hardware where packets arrive.")),
        ("폴링", "Polling", ("벨 없이 직원이 수시로 직접 확인하러 가는 방식.", "Instead of a bell, the clerk walks over to check on their own, repeatedly."), ("인터럽트와 반대되는 전략이에요.", "The opposite strategy to an interrupt.")),
        ("처리량(throughput)", "Throughput", ("전체적으로 얼마나 많이 처리했는지.", "How much got processed overall."), ("코얼레싱이 늘려주는 값이에요.", "What coalescing is designed to improve.")),
        ("지연(latency)", "Latency", ("소포 하나가 알려지기까지 걸리는 시간.", "How long it takes for one parcel to be flagged."), ("코얼레싱이 조금 늘리는 값이에요.", "What coalescing slightly worsens.")),
        ("인터럽트(프로세스)", "Interrupt (process)", ("CPU가 프로그램 실행 중 멈추는 일반적인 인터럽트.", "The general interrupt that pauses a CPU mid-program."), ('시스템SW 세계에서 다른 각도로 다뤄요. → <a href="interruptproc-ko.html">하던 일을 멈추게 하는 벨소리</a>', 'Covered from a different angle in the Systems world. → <a href="interruptproc-en.html">the bell that pauses what you were doing</a>')),
    ],
}
