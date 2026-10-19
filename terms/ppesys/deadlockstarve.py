from _draw import *
from _world import *

# 1. 정비사 둘이 서로 다른 열쇠를 쥐고, 서로의 열쇠를 기다려요
P1 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + lift(100, 250) + lift(660, 250)
         + person(230, 140, s=0.8, face=SWEAT + EYES, **MECH1) + keyring(230, 108)
         + person(530, 140, s=0.8, face=SWEAT + EYES, **MECH2) + keyring(530, 108)
         + label(380, 260, "⟦저 열쇠가 있어야 끝나는데…|I need THAT key to finish…⟧", 12, "var(--bad)", cls="d")
         + label(380, 30, "⟦정비사1은 2번 열쇠를, 정비사2는 1번 열쇠를 기다려요|MECH1 waits for key 2, MECH2 waits for key 1⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦둘 다 자기 열쇠는 안 놓고, 서로의 열쇠만 바라봐요|neither lets go of their own key — each just stares at the other's⟧", 12, "var(--ink)"))

# 2. 왜 이런 일이 생길까 — 네 가지 조건이 한꺼번에 맞아떨어져야 해요
P2 = svg(340, sky(340)
         + queueboard(90, 30, 300, 240, "⟦교착상태 네 조건|FOUR CONDITIONS⟧",
                      ["⟦상호배제: 한 번에 한 명만|mutual exclusion: one holder only⟧",
                       "⟦점유대기: 쥔 채로 더 기다림|hold &amp; wait: keep one, wait for more⟧",
                       "⟦비선점: 억지로 못 뺏음|no preemption: can't be forced away⟧",
                       "⟦순환대기: 서로 빙 돌며 기다림|circular wait: waiting in a loop⟧"], 1.0)
         + person(590, 150, s=0.8, face=EYES, **CHIEF)
         + label(590, 275, "⟦이 네 가지가 동시에 맞아야만 멈춰요|all four must hold at once for a freeze⟧", 11, "var(--muted)")
         + label(380, 320, "⟦하나만 깨도 교착상태는 안 생겨요|break just one, and deadlock can't happen⟧", 12, "var(--ink)"))

# 3. 교착상태 = 서로의 열쇠를 기다리며 영원히 멈추는 것 (hero)
P3 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + lift(90, 260) + lift(670, 260)
         + person(230, 150, s=0.85, face=FROWN, **MECH1) + keyring(230, 118)
         + person(530, 150, s=0.85, face=FROWN, **MECH2) + keyring(530, 118)
         + '<path d="M255 135 Q380 95 505 135" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 5"/>'
         + '<path d="M505 165 Q380 205 255 165" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 5"/>'
         + label(380, 25, "⟦교착상태 = 서로의 열쇠를 기다리며 영원히 멈추는 것|deadlock = freezing forever while each waits on the other's key⟧", 13, "#142033", cls="d")
         + label(380, 320, "⟦둘 다 더 못 움직여요 — 누군가 개입하지 않으면 영원히요|neither can move — not without someone stepping in⟧", 12, "#142033"))

# 4. 해결법 비교
P4 = svg(340, sky(340)
         + queueboard(60, 30, 330, 240, "⟦해결 전략|RESOLUTION STRATEGIES⟧",
                      ["⟦예방: 네 조건 중 하나를 미리 깨기|prevention: break one condition upfront⟧",
                       "⟦회피: 안전한 순서만 허락하기|avoidance: allow only safe orderings⟧",
                       "⟦탐지+복구: 발견 후 하나를 되돌리기|detection+recovery: find it, roll one back⟧",
                       "⟦무시: 자주 안 생기면 그냥 둠|ignore: rare enough to just live with⟧"], 1.0)
         + person(590, 150, s=0.8, face=EYES, **CHIEF)
         + label(590, 275, "⟦반장은 상황에 맞춰 전략을 골라요|the chief picks a strategy to fit⟧", 11, "var(--muted)")
         + label(380, 320, "⟦실제로는 \'무시\'(타조 알고리즘)도 흔한 선택이에요|in practice, \"ignore\" (the ostrich algorithm) is a common choice⟧", 12, "var(--ink)"))

# 5. 기아현상 — 멈추진 않지만, 한 차만 계속 밀려요
P5 = svg(300, sky(300)
         + queueboard(60, 40, 300, 220, "⟦작업 순서판|JOB QUEUE⟧", ["⟦급한 차 #9|urgent #9⟧", "⟦급한 차 #10|urgent #10⟧", "⟦급한 차 #11|urgent #11⟧"], 1.0)
         + car(570, 240, 0.7, "var(--muted)")
         + person(650, 160, s=0.7, face=FROWN, **CUSTOMER)
         + label(650, 135, "⟦제 차는 대체 언제…|when is MY car ever…⟧", 10, "var(--bad)")
         + label(380, 30, "⟦급한 차가 계속 새치기해서, 낮은 우선순위 차는 차례가 안 와요|urgent cars keep cutting in, so the low-priority car's turn never comes⟧", 12, "var(--ink)", cls="d")
         + label(380, 280, "⟦이건 멈춘 게 아니에요 — 그냥 영원히 순서가 안 올 뿐이에요(기아현상)|it's not frozen — its turn simply never arrives (starvation)⟧", 12, "var(--ink)"))

MUTEX_I = icon('<circle cx="32" cy="36" r="18" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="26" y="14" width="12" height="18" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/>')
HOLD_I = icon('<circle cx="20" cy="32" r="10" fill="var(--accent)"/><path d="M30 32 h24" stroke="var(--bad)" stroke-width="4" stroke-dasharray="4 4"/>')
PREEMPT_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M20 44 L44 20" stroke="var(--bad)" stroke-width="4"/>')
CIRCLE_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 12 l6 8 l-6 -2 l-6 2z" fill="var(--bad)"/>')

PAGE = {
    "slug": "deadlockstarve", "order": 5,
    "title": ("서로의 열쇠를 기다리며 멈춘 정비공장", "The Garage Frozen Waiting on Each Other's Keys"),
    "h1": ("<em>교착상태와 기아현상</em>이 뭐예요?", "What is <em>Deadlock and Starvation</em>?"),
    "sub": ("교착상태와 기아현상을, 서로 다른 열쇠를 쥔 채 서로를 기다리는 정비사 이야기로 풀어봤어요.",
            "Deadlock and starvation, told as a story about two mechanics each holding a key the other needs."),
    "panels": [
        {"svg": P1, "alt": ("정비사1은 열쇠1을 쥐고 열쇠2를 기다리고, 정비사2는 열쇠2를 쥐고 열쇠1을 기다림", "MECH1 holds key 1 and waits for key 2; MECH2 holds key 2 and waits for key 1"),
         "caption": ("정비사 둘이 서로 다른 열쇠를 쥐고 있어요.", "Two mechanics each hold a different key."),
         "small": ("둘 다 자기 열쇠는 안 놓고, 서로의 열쇠만 바라봐요.", "Neither lets go — each just stares at the other's key.")},
        {"svg": P2, "alt": ("상호배제·점유대기·비선점·순환대기 네 조건을 적은 순서판", "A board listing four conditions: mutual exclusion, hold-and-wait, no preemption, circular wait"),
         "caption": ("네 가지 조건이 한꺼번에 맞아떨어져야 해요.", "All four conditions have to line up at once."),
         "small": ("하나만 깨도 교착상태는 안 생겨요.", "Break just one, and deadlock can't happen.")},
        {"svg": P3, "hero": True, "alt": ("두 정비사가 서로의 열쇠를 가리키며 양쪽 다 꼼짝 못 함", "Both mechanics point at each other's key, and neither can move"),
         "caption": ("교착상태 = 서로의 열쇠를 기다리며 영원히 멈추는 것이에요.", "Deadlock = freezing forever while each waits on the other's key."),
         "small": ("누군가 개입하지 않으면 둘 다 영원히 못 움직여요.", "Neither can move — not without someone stepping in."),
         "tricks": (4, [
             (MUTEX_I, ("상호배제", "Mutual Exclusion"), ("열쇠는 한 번에 한 명만 쥐어요", "only one holder per key at a time")),
             (HOLD_I, ("점유대기", "Hold &amp; Wait"), ("쥔 채로 다른 열쇠를 더 기다려요", "keep what you have, wait for more")),
             (PREEMPT_I, ("비선점", "No Preemption"), ("억지로 뺏을 수 없어요", "can't be forced away from you"), "warm"),
             (CIRCLE_I, ("순환대기", "Circular Wait"), ("서로 빙 돌며 기다려요", "everyone waits in a loop"), "warm"),
         ])},
        {"svg": P4, "alt": ("예방·회피·탐지+복구·무시 네 가지 해결 전략을 적은 순서판", "A board listing four resolution strategies: prevention, avoidance, detection+recovery, ignore"),
         "caption": ("해결 전략도 여러 가지예요.", "There are several ways to handle it too."),
         "small": ("실제로는 \'무시\'(타조 알고리즘)도 흔한 선택이에요.", "In practice, \"ignore\" (the ostrich algorithm) is common.")},
        {"svg": P5, "alt": ("작업 순서판에 급한 차만 계속 올라가고, 낮은 우선순위 차는 끝에서 계속 기다림", "Urgent cars keep topping the job board while a low-priority car waits endlessly at the end"),
         "caption": ("기아현상 — 멈추진 않지만 한 차만 계속 밀려요.", "Starvation — nothing's frozen, but one car keeps getting bumped."),
         "small": ("이건 멈춘 게 아니에요 — 그냥 차례가 영원히 안 올 뿐이에요.", "It's not frozen — its turn simply never arrives.")},
    ],
    "summary": (("<b>교착상태</b> = 서로 다른 자원(열쇠)을 쥔 채 <b>서로를 기다리며 영원히 멈추는 것</b>. <b>기아현상</b>은 멈추진 않지만 <b>한쪽이 차례를 계속 못 받는 것</b>.",
                 "<b>Deadlock</b> = freezing forever as each side holds one resource (key) and waits on another. <b>Starvation</b> isn't frozen — one side just never gets its turn."),
                ("교착상태는 상호배제(Mutual Exclusion), 점유대기(Hold and Wait), 비선점(No Preemption), 순환대기(Circular Wait) 네 조건이 동시에 성립할 때 발생해요. 해결책은 예방(조건을 깨도록 설계), 회피(은행원 알고리즘처럼 안전 상태만 허용), 탐지 후 복구, 또는 무시(타조 알고리즘)로 나뉘어요. 기아현상은 교착상태와 달리 시스템이 계속 돌아가지만, 특정 프로세스가 스케줄링·우선순위 때문에 자원을 계속 못 받는 상태예요.",
                 "Deadlock arises when four conditions hold at once: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Fixes include prevention (design away one condition), avoidance (allow only safe states, as in the banker's algorithm), detection-and-recovery, or simply ignoring it (the ostrich algorithm). Starvation differs from deadlock: the system keeps running, but one process never gets the resource it needs because of scheduling or priority.")),
    "glossary": [
        ("상호배제", "Mutual Exclusion", ("열쇠 한 개는 한 번에 한 명만.", "One key, one holder at a time."), ("네 조건 중 하나예요.", "One of the four conditions.")),
        ("순환대기", "Circular Wait", ("서로 빙 돌며 상대 열쇠를 기다림.", "Everyone waiting in a loop for the next one's key."), ("이 고리를 끊으면 교착상태도 끊겨요.", "Break this loop, and deadlock breaks too.")),
        ("기아현상", "Starvation", ("한 차만 계속 순서에서 밀림.", "One car keeps getting bumped down the order."), ("멈춤이 아니라 \'영원한 미룸\'이에요.", "Not a freeze — an endless postponement.")),
        ("CPU 스케줄링", "CPU Scheduling", ("순서판에 적힌 차 순서 규칙.", "The rule that sets the car order on the board."), ('우선순위 규칙이 기아현상을 만들기도 해요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'A priority rule can itself cause starvation. → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("동기화(세마포어·뮤텍스)", "Synchronization", ("리프트 열쇠를 나눠주는 규칙.", "The rule for handing out the lift key."), ('교착상태는 동기화 도구를 잘못 쓸 때 자주 생겨요. → <a href="syncprim-ko.html">리프트 열쇠는 하나뿐</a>', 'Deadlock often comes from misusing these tools. → <a href="syncprim-en.html">there\'s only one lift key</a>')),
        ("프로세스/스레드", "Process/Thread", ("같은 차를 같이 고치는 여러 손.", "Several hands working the same car."), ('교착상태는 스레드끼리도, 프로세스끼리도 생겨요. → <a href="processthread-ko.html">같은 차, 여러 손</a>', 'Deadlock can happen between threads or between processes. → <a href="processthread-en.html">one car, many hands</a>')),
        ("가상메모리", "Virtual Memory", ("창고 전체를 내 것처럼 보여주는 가짜 지도.", "A fake map that makes the whole warehouse look like mine."), ('한정된 자원을 나눠 쓰는 또 다른 예예요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'Another example of sharing a limited resource. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse yours</a>')),
        ("오케스트레이션", "Orchestration", ("놀이공원 세계의 \'순서 정하기\'.", "The amusement-park world's version of ordering work."), ('분산 시스템에서도 자원 교착은 비슷하게 다뤄요. → <a href="orchestration-ko.html">SRE 세계의 오케스트레이션</a>', 'Distributed systems handle resource deadlock in a similar spirit. → <a href="orchestration-en.html">orchestration in the SRE world</a>')),
    ],
}
