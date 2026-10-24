from _draw import *
from _world import *

# 1. 정비사 둘이 같은 리프트를 동시에 건드려요
P1 = svg(300, sky(300)
         + lift(190, 220)
         + car(190, 155, 0.7, "var(--bad)")
         + person(80, 150, s=0.8, face=SWEAT + EYES, **MECH1)
         + person(300, 150, s=0.8, face=SWEAT + EYES, **MECH2)
         + label(380, 30, "⟦둘 다 \"지금 비었다\"고 보고 동시에 차를 올려요|Both see \"it's free\" and lift a car at the same moment⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦리프트가 한 대뿐인데, 확인도 안 하고 같이 손을 대요|only one lift, but neither checks before reaching for it⟧", 12, "var(--ink)"))

# 2. 비었는지 보고 나서 손대는 사이에도 사고가 나요 (race condition)
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + lift(380, 230, occupied=True)
         + person(180, 150, s=0.75, face=EYES, **MECH1) + bubble(60, 70, 230, 40, "⟦\"비었네?\" 확인하고 돌아서는 순간|checked \"it's free\" — then turned away⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=EYES, **MECH2) + bubble(460, 70, 230, 40, "⟦나도 \"비었네?\" — 둘 다 올라타요|me too, \"it's free\" — both climb on⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦\"확인하기\"와 \"쓰기\" 사이의 틈에서 사고가 나요(경쟁 상태)|the gap between \"check\" and \"use\" is where the crash happens (race condition)⟧", 12, "var(--ink)"))

# 3. 동기화 = 리프트 열쇠를 나눠주는 규칙 (hero)
P3 = svg(340, sky(340)
         + lift(620, 250, occupied=True)
         + keyring(400, 150, held=True)
         + person(300, 150, s=0.85, face=SMILE, **MECH1)
         + person(500, 230, s=0.7, face=FROWN, **MECH2)
         + bubble(500, 60, 200, 40, "⟦열쇠가 없으면 기다려요|no key — so I wait⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 25, "⟦동기화 = 리프트 열쇠를 가진 사람만 쓰게 하는 규칙|synchronization = only whoever holds the key gets to use it⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦열쇠를 든 사람이 끝내고 돌려줘야 다음 사람이 올라가요|the next person waits until the key comes back⟧", 12, "var(--muted)"))

# 4. 세 가지 도구 비교
P4 = svg(320, sky(320)
         + queueboard(40, 30, 330, 250, "⟦동기화 도구|SYNC TOOLS⟧",
                      ["Mutex: ⟦열쇠 딱 1개|exactly one key⟧",
                       "Semaphore: ⟦열쇠 N개|N keys at once⟧",
                       "Monitor: ⟦대기실 딸린 방|a room with a waiting lounge⟧",
                       "임계구역: ⟦열쇠 쥔 동안만|only while holding the key⟧"], 1.0)
         + person(590, 140, s=0.8, face=EYES, **MECH1)
         + label(590, 250, "⟦도구마다 \"몇 명까지 동시에\"가 달라요|each tool differs in how many get in at once⟧", 11, "var(--muted)")
         + label(380, 300, "⟦뮤텍스는 세마포어의 특수한 경우예요(N=1)|a mutex is just a semaphore with N=1⟧", 12, "var(--ink)"))

# 5. 열쇠를 안 돌려주면 — 멈춤의 원인이 되기도 해요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + person(190, 120, s=0.75, face=SMILE, **MECH1) + keyring(190, 215, held=False)
         + label(190, 265, "⟦제때 돌려주면 다음 차가|return it in time, and the⟧", 11, "var(--ink)")
         + label(190, 282, "⟦바로 올라가요|next car goes right up⟧", 11, "var(--ink)")
         + person(570, 120, s=0.75, face=FROWN, **MECH2)
         + label(570, 265, "⟦안 돌려주면? 다음 정비사는|forget it, and the next⟧", 11, "var(--ink)")
         + label(570, 282, "⟦영원히 대기예요|mechanic waits forever⟧", 11, "var(--ink)")
         + label(380, 308, "⟦\"한 번에 한 명만\"이 지나치면 교착상태로 이어질 수 있어요|\"only one at a time\" taken too far can lead to deadlock⟧", 12, "var(--ink)", cls="d"))

MUTEX_I = icon('<circle cx="32" cy="36" r="18" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="26" y="14" width="12" height="18" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/>')
SEM_I = icon('<circle cx="18" cy="40" r="8" fill="var(--accent)"/><circle cx="32" cy="40" r="8" fill="var(--accent)"/><circle cx="46" cy="40" r="8" fill="var(--accent)"/>')
MON_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--good)"/>')
CRIT_I = icon('<rect x="14" y="14" width="36" height="36" fill="none" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 4"/>')

PAGE = {
    "slug": "syncprim", "order": 2,
    "title": ("리프트 열쇠는 하나뿐", "There's Only One Lift Key"),
    "h1": ("<em>프로세스 동기화</em>가 뭐예요?", "What is <em>Process Synchronization</em>?"),
    "sub": ("세마포어·뮤텍스·모니터를, 리프트 열쇠를 나눠주는 규칙 이야기로 풀어봤어요.",
            "Semaphores, mutexes, and monitors, told as a story about the rule for handing out the lift key."),
    "panels": [
        {"svg": P1, "alt": ("정비사 둘이 동시에 같은 리프트에 차를 올리려 함", "Two mechanics both try to put a car on the same lift at once"),
         "caption": ("정비사 둘이 같은 리프트를 동시에 건드려요.", "Two mechanics reach for the same lift at the same time."),
         "small": ("확인도 안 하고 같이 손을 대요.", "Neither checks before reaching for it.")},
        {"svg": P2, "alt": ("두 정비사가 각자 \'비었다\' 확인한 틈에 둘 다 리프트에 올라타 충돌함", "Each mechanic checks \'it’s free\' in the gap before the other acts, and they collide on the lift"),
         "caption": ("확인과 사용 사이의 틈에서 사고가 나요.", "The crash happens in the gap between checking and using."),
         "small": ("이걸 경쟁 상태(race condition)라고 해요.", "This is called a race condition.")},
        {"svg": P3, "hero": True, "alt": ("열쇠를 든 정비사만 리프트를 쓰고, 열쇠 없는 정비사는 기다림", "Only the mechanic holding the key uses the lift; the other waits without it"),
         "caption": ("동기화 = 열쇠를 가진 사람만 쓰게 하는 규칙이에요.", "Synchronization = only the key-holder gets to use it."),
         "small": ("열쇠를 돌려줘야 다음 사람이 올라가요.", "The next person waits until the key comes back."),
         "tricks": (4, [
             (MUTEX_I, ("뮤텍스", "Mutex"), ("열쇠가 딱 1개예요", "exactly one key exists")),
             (SEM_I, ("세마포어", "Semaphore"), ("열쇠가 N개, N명까지 가능", "N keys — up to N at once"), "calm"),
             (MON_I, ("모니터", "Monitor"), ("대기실 딸린 방 하나", "a room with a built-in waiting lounge")),
             (CRIT_I, ("임계구역", "Critical Section"), ("열쇠 쥔 동안의 작업 구간", "the stretch of work done while holding the key"), "warm"),
         ])},
        {"svg": P4, "alt": ("뮤텍스·세마포어·모니터·임계구역 네 가지 동기화 도구를 적은 순서판", "A board listing four synchronization tools: mutex, semaphore, monitor, critical section"),
         "caption": ("도구마다 \"몇 명까지 동시에\"가 달라요.", "Each tool differs in how many get in at once."),
         "small": ("뮤텍스는 세마포어의 특수한 경우예요(N=1).", "A mutex is just a semaphore with N=1.")},
        {"svg": P5, "alt": ("왼쪽: 열쇠를 제때 돌려줘 다음 차가 바로 올라감. 오른쪽: 안 돌려줘 다음 정비사가 영원히 기다림", "Left: returning the key in time lets the next car go right up. Right: not returning it leaves the next mechanic waiting forever"),
         "caption": ("열쇠를 안 돌려주면 멈춤의 원인이 돼요.", "Not returning the key can itself cause a freeze."),
         "small": ("\"한 번에 한 명만\"이 지나치면 교착상태로 이어질 수 있어요.", "\"Only one at a time,\" taken too far, can lead to deadlock.")},
    ],
    "summary": (("<b>프로세스 동기화</b> = 리프트 같은 <b>공유 자원</b>을 여러 작업이 <b>한 번에 하나씩만</b> 건드리게 만드는 규칙.",
                 "<b>Process synchronization</b> = the rule that lets several tasks touch a shared resource like the lift only one at a time."),
                ("여러 프로세스/스레드가 같은 자원(변수·파일·메모리)에 동시에 접근하면 경쟁 상태(race condition)가 생겨요. Mutex(상호배제)는 임계구역(critical section)에 한 번에 하나만 들어가게 하고, Semaphore는 카운터로 N개까지 허용하며, Monitor는 락과 조건변수(condition variable)를 언어 차원에서 묶어 대기·신호를 안전하게 처리해요.",
                 "When several processes or threads touch the same resource (a variable, file, or memory region) at once, a race condition results. A mutex enforces mutual exclusion so only one enters the critical section at a time; a semaphore uses a counter to allow up to N; a monitor bundles a lock with condition variables at the language level to handle waiting and signaling safely.")),
    "glossary": [
        ("경쟁 상태", "Race Condition", ("확인과 사용 사이의 틈에서 나는 사고.", "A crash in the gap between checking and using."), ("순서가 꼬이면 결과가 매번 달라져요.", "Scramble the order, and the result changes each time.")),
        ("뮤텍스", "Mutex", ("열쇠가 딱 1개뿐인 잠금.", "A lock with exactly one key."), ("한 번에 한 작업만 들어가요.", "Only one task gets in at a time.")),
        ("세마포어", "Semaphore", ("열쇠가 N개 있는 잠금.", "A lock with N keys."), ("N명까지는 동시에 들어갈 수 있어요.", "Up to N can be inside at once.")),
        ("모니터", "Monitor", ("대기실 딸린 방.", "A room with a built-in waiting lounge."), ("락과 조건변수를 한 세트로 묶어줘요.", "Bundles a lock with condition variables.")),
        ("교착상태", "Deadlock", ("서로의 열쇠를 기다리며 영원히 멈춤.", "Frozen forever, each waiting on the other's key."), ('열쇠를 안 돌려주는 게 바로 이 문제로 이어져요. → <a href="deadlockstarve-ko.html">서로의 열쇠를 기다리며 멈춘 정비공장</a>', 'Not returning the key leads straight here. → <a href="deadlockstarve-en.html">the garage frozen waiting on each other\'s keys</a>')),
        ("프로세스/스레드", "Process/Thread", ("같은 차를 같이 고치는 여러 손.", "Several hands working the same car."), ('동기화는 특히 \'같은 차 공유\'인 스레드에서 자주 필요해요. → <a href="processthread-ko.html">같은 차, 여러 손</a>', 'Synchronization matters most for threads, which share "the same car." → <a href="processthread-en.html">one car, many hands</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("순서판에 적힌 차 순서.", "The car order written on the job board."), ('\'누가 먼저\'가 스케줄링이면, 이건 \'동시에 건드리지 않기\'예요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', '"Who goes first" is scheduling — this is "don\'t touch at once." → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("캐시 메모리", "Cache Memory", ("자주 쓰는 공구만 담는 작은 공구함.", "A small toolbox holding only the frequently used tools."), ('여러 코어가 같은 캐시 줄을 동시에 쓸 때도 비슷한 조율이 필요해요. → <a href="cachemem-ko.html">자주 쓰는 공구만 담는 공구함</a>', 'Similar coordination is needed when several cores share a cache line. → <a href="cachemem-en.html">the toolbox that holds only the frequent tools</a>')),
    ],
}
