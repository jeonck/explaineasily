from _draw import *
from _world import *

# 1. 엔진 분해, 혼자서는 너무 오래 걸려요
P1 = svg(300, sky(300)
         + car(260, 210, 1.0, "var(--accent)")
         + person(120, 150, s=0.8, face=SWEAT + EYES, **MECH1)
         + label(380, 30, "⟦엔진을 통째로 분해하는 큰 작업 하나|one big job: tear down the whole engine⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦정비사 한 명이서는 너무 오래 걸려요|one mechanic alone takes far too long⟧", 12, "var(--ink)"))

# 2. 아예 새 차(새 공장 칸)로 옮겨도 되지만, 준비가 다 번거로워요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + car(150, 200, 0.75, "var(--accent)") + person(260, 140, s=0.7, face=EYES, **MECH1)
         + car(500, 200, 0.75, "#5B8DEF") + person(620, 140, s=0.7, face=SWEAT + EYES, **MECH2)
         + label(380, 40, "⟦아예 새 차를 한 대 더 들여올 수도 있어요|you could bring in a whole second car instead⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦근데 차마다 공구함·트렁크를 다 따로 챙겨야 해서 번거로워요|but each car needs its own full toolbox and trunk set up — a lot of overhead⟧", 12, "var(--ink)"))

# 3. 스레드 = 같은 차 안에서 같이 일하는 손, 프로세스 = 각자 다른 차 (hero)
P3 = svg(340, sky(340)
         + car(230, 240, 1.1, "var(--accent)")
         + person(160, 160, s=0.8, face=EYES, **MECH1) + person(300, 160, s=0.8, face=EYES, **MECH2)
         + label(230, 100, "⟦같은 차, 같은 트렁크를 같이 써요(스레드)|same car, sharing the same trunk (threads)⟧", 12, "var(--ink)", cls="d")
         + car(600, 240, 0.9, "#2E8B57")
         + person(540, 160, s=0.7, face=EYES, **CUSTOMER)
         + label(590, 100, "⟦완전히 다른 트렁크예요(프로세스)|a completely separate trunk (a process)⟧", 10, "var(--muted)")
         + label(380, 25, "⟦스레드 = 같은 차 안에서 같이 일하는 손, 프로세스 = 각자 다른 차|threads = hands working inside the same car, processes = separate cars entirely⟧", 13, "#142033", cls="d")
         + label(380, 325, "⟦같은 차 안 손들은 트렁크를 공유하지만, 다른 차는 서로를 못 봐요|hands in one car share the trunk — but a different car can't see into it at all⟧", 11, "var(--muted)"))

# 4. 프로세스 vs 스레드 비교
P4 = svg(340, sky(340)
         + queueboard(50, 30, 320, 230, "⟦프로세스 vs 스레드|PROCESS vs THREAD⟧",
                      ["프로세스: ⟦독립된 차, 독립된 트렁크|its own car, its own trunk⟧",
                       "프로세스: ⟦만들기 무겁고, 느려요|heavy to set up, slow⟧",
                       "스레드: ⟦같은 차, 같은 트렁크 공유|same car, shared trunk⟧",
                       "스레드: ⟦만들기 가볍고, 빨라요|light to spin up, fast⟧"], 1.0)
         + person(640, 150, s=0.8, face=EYES, **MECH1)
         + label(640, 275, "⟦무엇을 공유하느냐가 핵심 차이예요|what's shared is the key difference⟧", 11, "var(--muted)")
         + label(380, 320, "⟦스레드는 프로세스 안에서 돌아가는, 실제 스케줄링의 단위예요|a thread runs inside a process — it's the real unit the scheduler moves⟧", 12, "var(--ink)"))

# 5. 트렁크를 같이 쓰면 빠르지만, 부딪히면 둘 다 다쳐요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + person(140, 130, s=0.75, face=SMILE, **MECH1) + person(240, 130, s=0.75, face=SMILE, **MECH2)
         + label(190, 250, "⟦같이 쓰니까 훨씬 빨라요|sharing makes it much faster⟧", 11, "var(--ink)")
         + person(540, 130, s=0.75, face=FROWN, **MECH1) + person(630, 130, s=0.75, face=FROWN, **MECH2)
         + label(585, 250, "⟦동시에 손대면 서로 부딪혀요|touch it at once, and they collide⟧", 11, "var(--ink)")
         + label(380, 295, "⟦그래서 같이 쓰는 트렁크엔 동기화 규칙이 꼭 필요해요|that's why a shared trunk always needs a synchronization rule⟧", 12, "var(--ink)", cls="d"))

PROC_I = icon('<rect x="10" y="12" width="20" height="40" rx="3" fill="var(--accent)"/><rect x="34" y="12" width="20" height="40" rx="3" fill="var(--good)"/>')
THREAD_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="26" cy="24" r="5" fill="var(--good)"/><circle cx="38" cy="40" r="5" fill="var(--good)"/>')
SWITCH_I = icon('<path d="M12 22 h40 M44 16 l8 6 l-8 6" stroke="var(--bad)" stroke-width="3" fill="none"/><path d="M52 42 h-40 M20 36 l-8 6 l8 6" stroke="var(--bad)" stroke-width="3" fill="none"/>')
SHARE_I = icon('<rect x="20" y="24" width="24" height="24" rx="3" fill="var(--accent)"/><circle cx="16" cy="36" r="8" fill="none" stroke="var(--good)" stroke-width="3"/><circle cx="48" cy="36" r="8" fill="none" stroke="var(--good)" stroke-width="3"/>')

PAGE = {
    "slug": "processthread", "order": 9,
    "title": ("같은 차, 여러 손", "One Car, Many Hands"),
    "h1": ("<em>프로세스와 스레드</em>가 뭐예요?", "What are <em>Processes and Threads</em>?"),
    "sub": ("프로세스와 스레드를, 차 한 대를 같이 고치는 손들과 각자 다른 차 이야기로 풀어봤어요.",
            "Processes and threads, told as a story about hands sharing one car versus mechanics working on separate cars."),
    "panels": [
        {"svg": P1, "alt": ("정비사 한 명이 엔진 전체를 분해하는 큰 작업을 혼자 맡아 진땀을 흘림", "A single mechanic sweats, handling the whole engine teardown alone"),
         "caption": ("엔진 분해, 혼자서는 너무 오래 걸려요.", "Tearing down the engine alone takes far too long."),
         "small": ("정비사 한 명이서는 너무 오래 걸려요.", "One mechanic alone takes far too long.")},
        {"svg": P2, "alt": ("완전히 새 차와 새 정비사를 들여오지만, 각자 공구함과 트렁크를 따로 준비해야 함", "A whole new car and mechanic are brought in, but each needs its own toolbox and trunk set up separately"),
         "caption": ("아예 새 차를 한 대 더 들여올 수도 있어요.", "You could bring in a whole second car instead."),
         "small": ("차마다 공구함·트렁크를 따로 챙겨야 해서 번거로워요.", "Each car needs its own full toolbox and trunk — a lot of overhead.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽: 같은 차 안에서 정비사 둘이 같은 트렁크를 공유하며 일함(스레드). 오른쪽: 완전히 다른 차 한 대(프로세스)", "Left: two mechanics share the same trunk inside one car (threads). Right: an entirely separate car (a process)"),
         "caption": ("스레드 = 같은 차 안 여러 손, 프로세스 = 각자 다른 차예요.", "Threads = many hands in one car; processes = separate cars entirely."),
         "small": ("같은 차 손들은 트렁크를 공유하지만, 다른 차는 서로를 못 봐요.", "Hands in one car share the trunk — a different car can't see into it."),
         "tricks": (4, [
             (PROC_I, ("프로세스", "Process"), ("독립된 차, 독립된 메모리 공간", "an independent car, an independent memory space")),
             (THREAD_I, ("스레드", "Thread"), ("같은 차 안에서 함께 일하는 손", "hands working inside the same car"), "calm"),
             (SWITCH_I, ("컨텍스트 스위치", "Context Switch"), ("다른 차로 옮겨탈 때 시간이 들어요", "switching cars costs time"), "warm"),
             (SHARE_I, ("공유 메모리 위험", "Shared-Memory Risk"), ("같은 트렁크를 같이 쓰다 부딪혀요", "sharing one trunk means you can collide")),
         ])},
        {"svg": P4, "alt": ("프로세스는 독립된 차·무거운 생성 비용, 스레드는 공유된 차·가벼운 생성 비용임을 보여주는 순서판", "A board contrasting a process's separate car and heavy setup cost with a thread's shared car and light setup cost"),
         "caption": ("무엇을 공유하느냐가 핵심 차이예요.", "What's shared is the key difference."),
         "small": ("스레드는 프로세스 안에서 돌아가는, 실제 스케줄링의 단위예요.", "A thread runs inside a process — the real unit the scheduler moves.")},
        {"svg": P5, "alt": ("왼쪽: 같은 트렁크를 같이 써서 빨라짐. 오른쪽: 동시에 손대다 부딪힘", "Left: sharing the trunk makes work faster. Right: touching it at the same time causes a collision"),
         "caption": ("트렁크를 같이 쓰면 빠르지만, 부딪히면 둘 다 다쳐요.", "Sharing the trunk is fast — but a collision hurts both sides."),
         "small": ("그래서 같이 쓰는 트렁크엔 동기화 규칙이 꼭 필요해요.", "That's why a shared trunk always needs a synchronization rule.")},
    ],
    "summary": (("<b>프로세스</b> = 각자 <b>독립된 차</b>(독립된 메모리). <b>스레드</b> = <b>같은 차 안에서 트렁크(메모리)를 같이 쓰며</b> 일하는 여러 손.",
                 "<b>Process</b> = each its own independent car (independent memory). <b>Thread</b> = several hands working inside the same car, sharing its trunk (memory)."),
                ("프로세스는 운영체제가 할당하는 독립된 메모리 공간을 가진 실행 단위로, 서로의 메모리를 직접 들여다볼 수 없어요. 스레드는 한 프로세스 안에서 코드·데이터·힙은 공유하면서 스택과 레지스터만 따로 갖는, 더 가벼운 실행 단위예요. 프로세스 생성·전환은 비용이 크고, 스레드는 상대적으로 가볍지만 공유 메모리 때문에 동기화가 필요해요. 실제 CPU 스케줄링의 단위는 프로세스보다 스레드인 경우가 많아요.",
                 "A process is an execution unit with its own OS-allocated memory space — it can't peek directly into another process's memory. A thread is a lighter execution unit living inside a process, sharing its code, data, and heap, while keeping its own stack and registers. Creating or switching processes is costly; threads are comparatively light, but their shared memory means synchronization is needed. In practice, the CPU scheduler often moves threads, not whole processes.")),
    "glossary": [
        ("프로세스", "Process", ("독립된 차 한 대.", "One independent car."), ("자기만의 메모리 공간을 가져요.", "Has its own memory space.")),
        ("스레드", "Thread", ("같은 차 안에서 함께 일하는 손.", "Hands working inside the same car."), ("코드·트렁크(메모리)는 공유, 손놀림(스택)만 따로예요.", "Shares code and the trunk (memory); keeps its own stack.")),
        ("컨텍스트 스위치", "Context Switch", ("다른 차로 옮겨탈 때 드는 시간.", "The time cost of switching to a different car."), ("스레드가 프로세스보다 훨씬 가벼워요.", "Much lighter for threads than for whole processes.")),
        ("동기화(세마포어·뮤텍스)", "Synchronization", ("리프트 열쇠를 나눠주는 규칙.", "The rule for handing out the lift key."), ('같은 트렁크를 공유하는 스레드에 특히 중요해요. → <a href="syncprim-ko.html">리프트 열쇠는 하나뿐</a>', 'Especially important for threads sharing one trunk. → <a href="syncprim-en.html">there\'s only one lift key</a>')),
        ("교착상태", "Deadlock", ("서로의 열쇠를 기다리며 영원히 멈춤.", "Frozen forever, each waiting on the other's key."), ('스레드끼리도, 프로세스끼리도 생길 수 있어요. → <a href="deadlockstarve-ko.html">서로의 열쇠를 기다리며 멈춘 정비공장</a>', 'Can happen between threads or between processes. → <a href="deadlockstarve-en.html">the garage frozen waiting on each other\'s keys</a>')),
        ("가상메모리", "Virtual Memory", ("창고 전체를 내 것처럼 보여주는 가짜 지도.", "A fake map that makes the whole warehouse look like mine."), ('프로세스마다 이 가짜 지도를 따로 가져요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'Each process gets its own copy of this fake map. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse yours</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("순서판에 적힌 차 순서 규칙.", "The rule that sets the car order on the board."), ('실제로 순서판에 오르는 건 대개 스레드예요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'What actually lands on the board is usually a thread. → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("GPU의 많은 손", "The GPU's Many Hands", ("똑같은 간단한 일을 한번에 나눠 하는 보조 정비팀.", "A crew doing the same simple task all at once."), ('GPU의 코어 하나하나도 매우 가벼운 스레드 개념에 가까워요. → <a href="gpu-ko.html">수백 명이 함께 움직이는 보조 정비팀</a>', 'Each GPU core is close to an extremely lightweight thread. → <a href="gpu-en.html">the hundred-hand helper crew</a>')),
    ],
}
