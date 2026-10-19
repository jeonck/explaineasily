from _draw import *
from _world import *

# 1. 이 정비공장이 곧 컴퓨터 시스템이다 — 리프트는 하나인데 차는 계속 들어옴
P1 = svg(320, sky(320)
         + lift(110, 230)
         + person(250, 150, s=0.85, face=SWEAT + EYES, **CHIEF)
         + car(400, 180, 0.8, "var(--accent)") + car(500, 210, 0.7, "#5B8DEF")
         + car(600, 235, 0.6, "#2E8B57") + car(690, 255, 0.5, "#C9822B")
         + label(380, 30, "⟦이 정비공장이 곧 컴퓨터 시스템이에요|This garage IS a computer system⟧", 14, "var(--ink)", cls="d")
         + label(380, 295, "⟦리프트(CPU)는 하나인데, 차(작업)는 계속 들어와요|One lift (the CPU), but cars (jobs) keep arriving⟧", 12, "var(--ink)"))

# 2. 순서를 아무렇게나 정하면 먼저 온 느린 차가 다른 차를 다 막아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + lift(140, 220, occupied=True)
         + car(140, 160, 0.8, "var(--bad)")
         + bubble(40, 50, 220, 40, "⟦엔진 전체 분해 중… 3시간째요|full engine teardown… 3 hours in⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + car(340, 220, 0.6, "#5B8DEF") + car(430, 230, 0.5, "#2E8B57")
         + person(560, 160, s=0.8, face=FROWN, **CUSTOMER)
         + bubble(480, 90, 230, 40, "⟦타이어 바람만 넣으면 되는데 계속 기다려요|I just need air in my tires, still waiting⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦순서를 아무렇게나 정하면, 짧은 일도 긴 일 뒤에서 하염없이 기다려요|A bad order means even a quick job waits forever behind a long one⟧", 12, "var(--ink)"))

# 3. CPU 스케줄링 = 반장이 작업 순서판에 규칙을 적어 차 순서를 정하는 것 (hero)
P3 = svg(340, sky(340)
         + queueboard(60, 50, 280, 220, "⟦작업 순서판|JOB QUEUE⟧", ["1. #118 (타이어)", "2. #119 (오일)", "3. #120 (엔진)"], 1.0, hl=0)
         + person(500, 110, s=0.9, face=EYES, **CHIEF)
         + lift(620, 250, 0.9)
         + label(380, 25, "⟦CPU 스케줄링 = 반장이 순서판에 규칙을 적어 차 순서를 정하는 것|CPU scheduling = the chief writing a rule on the board to set the car order⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦어떤 규칙을 쓰느냐에 따라 누가 먼저 리프트에 오르는지가 달라져요|Which rule is used decides who gets the lift first⟧", 12, "var(--muted)"))

# 4. 네 가지 규칙 비교
P4 = svg(340, sky(340)
         + queueboard(40, 30, 320, 220, "⟦규칙별 비교|RULES COMPARED⟧",
                      ["FCFS: ⟦온 순서 그대로|in arrival order⟧",
                       "SJF: ⟦짧은 일 먼저|shortest job first⟧",
                       "Round Robin: ⟦조금씩 돌아가며|small turns, round-robin⟧",
                       "Priority: ⟦급한 차 먼저|urgent car first⟧"], 1.0)
         + person(590, 150, s=0.8, face=EYES, **CHIEF)
         + label(590, 250, "⟦반장은 이 중 하나를 골라 순서판에 적어요|the chief picks one and writes it on the board⟧", 11, "var(--muted)")
         + label(380, 320, "⟦Round Robin 은 짧게 돌아가며 주는 대신, 차를 바꿀 때마다 시간이 조금씩 들어요|round-robin shares turns fairly, but switching cars costs a little time each time⟧", 12, "var(--ink)"))

# 5. 완벽한 규칙은 없어요 — 공평함과 빠름은 자주 부딪혀요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **CHIEF) + label(190, 240, "⟦짧은 일을 먼저 하면 평균 대기는 짧아져요|job-shortest-first keeps the average wait low⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **CUSTOMER) + car(570, 220, 0.5, "var(--bad)") + label(570, 260, "⟦근데 긴 일은 계속 밀려요(기아)|but the long job keeps getting skipped (starvation)⟧", 11, "var(--ink)")
         + label(380, 285, "⟦완벽한 순서 규칙은 없어요 — 공평함과 속도는 자주 부딪혀요|no single rule is perfect — fairness and speed often pull against each other⟧", 12, "var(--ink)", cls="d"))

FCFS_I = icon('<rect x="8" y="26" width="48" height="12" rx="3" fill="var(--accent)"/><circle cx="14" cy="32" r="4" fill="var(--panel)"/><circle cx="26" cy="32" r="4" fill="var(--panel)"/><circle cx="38" cy="32" r="4" fill="var(--panel)"/>')
SJF_I = icon('<rect x="10" y="14" width="14" height="36" fill="var(--good)"/><rect x="26" y="26" width="14" height="24" fill="var(--accent)"/><rect x="42" y="36" width="14" height="14" fill="var(--muted)"/>')
RR_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 12 l8 -6 l2 10z" fill="var(--accent)"/>')
PRI_I = icon('<path d="M20 10 h4 v44 h-4z" fill="#5A3B22"/><path d="M24 12 h26 l-8 9 l8 9 h-26 z" fill="var(--bad)"/>')

PAGE = {
    "slug": "cpusched", "order": 1,
    "title": ("리프트에 누가 먼저 올라갈까", "Who Gets the Lift First"),
    "h1": ("<em>CPU 스케줄링</em>이 뭐예요?", "What is <em>CPU Scheduling</em>?"),
    "sub": ("CPU 스케줄링을, 리프트 하나를 놓고 들어오는 차의 순서를 정비반장이 정해주는 이야기로 풀어봤어요.",
            "CPU scheduling, told as a story about the garage chief deciding which car gets the one lift next."),
    "panels": [
        {"svg": P1, "alt": ("정비공장에 리프트는 하나뿐인데 차가 여러 대 몰려 반장이 진땀을 흘림", "The garage has only one lift but several cars pile up, and the chief sweats"),
         "caption": ("이 정비공장이 곧 컴퓨터 시스템이에요.", "This garage IS a computer system."),
         "small": ("리프트(CPU)는 하나인데, 차(작업)는 계속 들어와요.", "One lift (the CPU), but cars (jobs) keep arriving.")},
        {"svg": P2, "hero": False, "alt": ("긴 엔진 작업 차가 리프트를 3시간째 붙잡아, 타이어만 넣으면 되는 손님이 계속 기다림", "A long engine job holds the lift for 3 hours while a customer who just needs air keeps waiting"),
         "caption": ("순서를 아무렇게나 정하면 안 돼요.", "You can't just pick an order at random."),
         "small": ("짧은 일도 긴 일 뒤에서 하염없이 기다려요.", "Even a quick job waits forever behind a long one.")},
        {"svg": P3, "hero": True, "alt": ("작업 순서판에 적힌 차례대로 반장이 차를 리프트에 올림", "The chief sends cars onto the lift in the order written on the job board"),
         "caption": ("CPU 스케줄링 = 반장이 순서판에 규칙을 적어 순서를 정하는 것이에요.", "CPU scheduling = the chief writing a rule on the board to set the order."),
         "small": ("어떤 규칙을 쓰느냐에 따라 누가 먼저 리프트에 오르는지가 달라져요.", "Which rule is used decides who gets the lift first."),
         "tricks": (4, [
             (FCFS_I, ("FCFS", "FCFS"), ("온 순서 그대로, 제일 단순해요", "first come, first served — the simplest rule")),
             (SJF_I, ("SJF", "SJF"), ("짧은 일부터 끝내요", "shortest job finishes first"), "calm"),
             (RR_I, ("Round Robin", "Round Robin"), ("조금씩 돌아가며 나눠줘요", "everyone gets a small turn, round and round")),
             (PRI_I, ("Priority", "Priority"), ("급한 차가 새치기해요", "an urgent car cuts in line"), "warm"),
         ])},
        {"svg": P4, "alt": ("네 가지 스케줄링 규칙을 적은 순서판: FCFS, SJF, Round Robin, Priority", "A job board listing four scheduling rules: FCFS, SJF, Round Robin, Priority"),
         "caption": ("규칙마다 장단점이 달라요.", "Each rule trades off differently."),
         "small": ("Round Robin 은 공평하지만 차를 바꿀 때마다 시간이 조금씩 들어요.", "Round-robin is fair, but switching cars costs a little time each turn.")},
        {"svg": P5, "alt": ("왼쪽: 짧은 일 먼저 하면 평균 대기가 짧음. 오른쪽: 긴 일은 계속 밀려 기아 상태가 됨", "Left: shortest-first keeps average wait low. Right: the long job keeps getting skipped — starvation"),
         "caption": ("완벽한 순서 규칙은 없어요.", "No single rule is perfect."),
         "small": ("공평함과 속도는 자주 부딪혀요.", "Fairness and speed often pull against each other.")},
    ],
    "summary": (("<b>CPU 스케줄링</b> = 하나뿐인 리프트(CPU)에 여러 차(작업)가 몰릴 때, <b>어떤 차를 먼저 올릴지 정하는 규칙</b>.",
                 "<b>CPU scheduling</b> = the rule that decides which car (job) gets the one lift (CPU) next when several arrive at once."),
                ("운영체제는 프로세스에 CPU를 할당할 순서를 정하는데, FCFS(First-Come-First-Served)·SJF(Shortest Job First)·Round Robin(시분할)·Priority Scheduling 등이 대표적이에요. FCFS는 구현이 쉽지만 convoy effect(긴 작업이 뒤를 막음)가 생기고, SJF는 평균 대기시간은 최소화하지만 긴 작업이 starvation(기아) 될 수 있어요. Round Robin은 time quantum 단위로 공평하게 나누지만 context switch 비용이 들어요.",
                 "The OS decides the order in which processes get the CPU. FCFS, SJF (Shortest Job First), Round Robin (time-sliced), and Priority Scheduling are the classic algorithms. FCFS is simple but suffers the convoy effect; SJF minimizes average wait but can starve long jobs; Round Robin shares turns fairly via a time quantum but pays a context-switch cost each turn.")),
    "glossary": [
        ("FCFS", "FCFS", ("온 순서 그대로 태우는 규칙.", "Load cars in the order they arrived."), ("단순하지만 긴 차가 뒤를 막아요(convoy effect).", "Simple, but a long car blocks everyone behind it.")),
        ("SJF", "SJF", ("짧은 일을 먼저 끝내는 규칙.", "Finish the shortest job first."), ("평균 대기는 짧지만 긴 일은 기아 상태가 될 수 있어요.", "Lowers average wait, but can starve long jobs.")),
        ("Round Robin", "Round Robin", ("조금씩 돌아가며 태우는 규칙.", "Give everyone a small, rotating turn."), ("공평하지만 차 바꿀 때마다 시간이 들어요(컨텍스트 스위치).", "Fair, but each switch costs a little time (context switch).")),
        ("기아현상", "Starvation", ("순서판에서 계속 밀려나는 차.", "A car that keeps getting bumped down the board."), ('자세한 원리는 교착상태 페이지에서 같이 다뤄요. → <a href="deadlockstarve-ko.html">서로의 열쇠를 기다리며 멈춘 정비공장</a>', 'Covered alongside deadlock. → <a href="deadlockstarve-en.html">the garage frozen waiting on each other\'s keys</a>')),
        ("동기화", "Synchronization", ("리프트 열쇠를 나눠주는 규칙.", "The rule for handing out the lift key."), ('스케줄링이 \'누가 먼저\'라면, 이건 \'동시에 건드리지 않기\'예요. → <a href="syncprim-ko.html">리프트 열쇠는 하나뿐</a>', 'Scheduling is "who goes first" — this is "don\'t touch at once." → <a href="syncprim-en.html">there\'s only one lift key</a>')),
        ("프로세스/스레드", "Process/Thread", ("차 한 대 vs 같은 차를 같이 고치는 손들.", "One car vs. several hands working the same car."), ('스케줄링의 실제 단위는 스레드인 경우가 많아요. → <a href="processthread-ko.html">같은 차, 여러 손</a>', 'The actual scheduling unit is often the thread. → <a href="processthread-en.html">one car, many hands</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("차가 늘어날 때 일이 얼마나 빨리 느는지 재는 자.", "The ruler for how fast work grows as cars pile up."), ('순서판을 매번 다시 정렬하는 비용도 이 자로 재요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'Re-sorting the board each time is measured with this ruler too. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("오케스트레이션", "Orchestration", ("놀이공원 세계의 비슷한 \'순서 정하기\'.", "A similar \'ordering\' idea in the amusement-park world."), ('더 높은 층위(서비스·컨테이너)에서도 비슷한 문제가 있어요. → <a href="orchestration-ko.html">SRE 세계의 오케스트레이션</a>', 'A similar problem shows up one layer up, at the service/container level. → <a href="orchestration-en.html">orchestration in the SRE world</a>')),
    ],
}
