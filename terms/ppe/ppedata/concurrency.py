from _draw import *
from _world import *

# 1. 문제: 포장 담당과 배송 기사가 같은 상자를 동시에 집어요
P1 = svg(320, sky(320)
         + person(220, 160, s=0.8, face=SWEAT + EYES, **PACKER)
         + person(540, 160, s=0.8, face=SWEAT + EYES, **DRIVER)
         + box(380, 200, 0.9)
         + label(380, 110, "⟦둘이 동시에 같은 상자를 집으려고 해요|both reach for the same box at once⟧", 12, "var(--bad)")
         + label(380, 290, "⟦누가 먼저인지 정하지 않으면 부딪혀요|without deciding who goes first, they collide⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 규칙 없이 두면 상자가 망가져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + box(300, 150, 1.0) + box(460, 150, 1.0, color="#C9822B")
         + label(380, 90, "⟦둘 다 쓰려다 서로의 작업을 지워버려요|both try to write and erase each other's work⟧", 12, "var(--bad)")
         + label(380, 250, "⟦이걸 막는 규칙이 '병행제어'예요|the rule that stops this is 'concurrency control'⟧", 13, "var(--ink)"))

# 3. hero: 병행제어 = 동시에 손대도 안 부딪히게 막는 규칙
LOCK2_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="#E9B44C" stroke="#8B5E3C" stroke-width="3"/><path d="M22 26 V18 a10 10 0 0 1 20 0 V26" stroke="#8B5E3C" stroke-width="5" fill="none"/>')
CHECK2_I = icon('<path d="M12 34 l14 14 l26 -30" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
CLOCK2_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
TWIN_I = icon('<rect x="8" y="18" width="22" height="30" rx="3" fill="#E9B44C" stroke="#8B5E3C" stroke-width="2"/><rect x="34" y="18" width="22" height="30" rx="3" fill="#E9B44C" stroke="#8B5E3C" stroke-width="2" opacity="0.5"/>')

P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **MANAGER)
         + box(230, 230, 0.7) + label(230, 270, "⟦줄 서서 차례로|wait in line, in order⟧", 10, "var(--muted)")
         + box(530, 230, 0.7, twin=True) + label(530, 270, "⟦스냅샷을 따로 보여주기(MVCC)|show each a separate snapshot (MVCC)⟧", 10, "var(--muted)")
         + label(380, 30, "⟦병행제어 = 동시에 손대도 안 부딪히게 막는 규칙|concurrency control = rules that stop simultaneous edits from colliding⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦잠그거나, 순서를 매기거나, 따로 보여줘요|lock it, order it, or show separate versions⟧", 12, "var(--muted)"))

# 4. 네 가지 방법 비교
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦병행제어 네 가지 방법|four concurrency control methods⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + _row(80, "⟦비관적 잠금(Locking) — 미리 잠가두기|pessimistic locking — lock it up front⟧", "⟦충돌을 원천 차단|blocks conflict from the start⟧")
         + _row(116, "⟦낙관적 제어(Optimistic) — 일단 해보고 나중 확인|optimistic — try first, verify later⟧", "⟦충돌 드물 때 빠름|fast when conflicts are rare⟧")
         + _row(152, "⟦타임스탬프 순서 — 시간표로 순서 매김|timestamp ordering — order by time stamp⟧", "⟦먼저 온 순서대로|processed in arrival order⟧")
         + _row(188, "⟦MVCC — 각자에게 스냅샷 보여주기|MVCC — show each a snapshot⟧", "⟦읽기와 쓰기가 안 막아요|reads don't block writes⟧"))

# 5. 한계: 안전할수록 기다림이 늘어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + box(190, 150, 1.0) + label(190, 210, "⟦잠그면 안전해요|locking is safe⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **DRIVER) + label(570, 268, "⟦대신 뒷사람이 줄을 서서 기다려요|but the next person waits in line⟧", 11, "var(--ink)")
         + label(380, 270, "⟦격리 수준과 맞물려 안전·속도를 함께 정해요|works together with isolation level to balance safety and speed⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "concurrency", "order": 7,
    "title": ("동시에 손대도 안 부딪히게 막는 규칙", "The Rule That Keeps Simultaneous Hands From Colliding"),
    "h1": ("<em>데이터베이스 병행제어</em>가 뭐예요?", "What is <em>Database Concurrency Control</em>?"),
    "sub": ("병행제어를, 포장 담당과 배송 기사가 같은 상자를 동시에 집으려다 부딪히는 이야기로 풀어봤어요.",
            "Concurrency control, told as a story about a packer and a driver reaching for the same box at once."),
    "panels": [
        {"svg": P1, "alt": ("포장 담당과 배송 기사가 동시에 같은 상자를 집으려다 진땀을 흘림", "A packer and a driver both sweat, reaching for the same box at once"),
         "caption": ("포장 담당과 배송 기사가 같은 상자를 동시에 집으려고 해요.", "The packer and the driver both reach for the same box at once."),
         "small": ("누가 먼저인지 정하지 않으면 부딪혀요.", "Without deciding who goes first, they collide.")},
        {"svg": P2, "alt": ("두 사람이 동시에 쓰려다 서로의 작업을 지우는 상자 두 개", "Two boxes where simultaneous writes erase each other's work"),
         "caption": ("둘 다 쓰려다 서로의 작업을 지워버려요.", "Both try to write and erase each other's work."),
         "small": ("이걸 막는 규칙이 '병행제어'예요.", "The rule that stops this is 'concurrency control'.")},
        {"svg": P3, "hero": True, "alt": ("창고 관리자가 줄 세우기와 복제 상자로 동시 접근을 조율함", "A manager coordinates simultaneous access with a queue and a twin box"),
         "caption": ("병행제어 = 동시에 손대도 안 부딪히게 막는 규칙이에요.", "Concurrency control is rules that stop simultaneous edits from colliding."),
         "small": ("잠그거나, 순서를 매기거나, 따로 보여줘요.", "Lock it, order it, or show separate versions."),
         "tricks": (4, [
             (LOCK2_I, ("비관적 잠금", "Pessimistic locking"), ("미리 잠가 충돌을 막아요", "locks it up front to avoid conflict"), "calm"),
             (CHECK2_I, ("낙관적 제어", "Optimistic control"), ("일단 해보고 나중에 확인해요", "tries first, checks later")),
             (CLOCK2_I, ("타임스탬프 순서", "Timestamp ordering"), ("시간표로 순서를 매겨요", "orders by timestamp"), "warm"),
             (TWIN_I, ("MVCC(다중 버전)", "MVCC (multi-version)"), ("각자에게 스냅샷을 보여줘요", "shows each a snapshot")),
         ])},
        {"svg": P4, "alt": ("비관적 잠금, 낙관적 제어, 타임스탬프 순서, MVCC 네 방법을 비교하는 표", "A table comparing pessimistic locking, optimistic control, timestamp ordering, and MVCC"),
         "caption": ("병행제어는 네 가지 방법으로 나뉘어요.", "Concurrency control splits into four methods."),
         "small": ("MVCC는 읽기와 쓰기가 서로 막지 않아요.", "MVCC lets reads and writes avoid blocking each other.")},
        {"svg": P5, "alt": ("왼쪽: 잠그면 안전함을 보여줌. 오른쪽: 배송 기사가 줄을 서서 기다리며 땀을 흘림", "Left: locking shows safety. Right: a driver sweats, waiting in line"),
         "caption": ("안전할수록 기다림이 늘어요.", "The safer it is, the longer the wait."),
         "small": ("격리 수준과 맞물려 안전·속도를 함께 정해요.", "Works together with isolation level to balance safety and speed.")},
    ],
    "summary": (("<b>병행제어</b> = 여러 사람이 <b>동시에 같은 데이터를 손대도 부딪히지 않게</b> 잠그거나 순서를 매기는 규칙.",
                 "<b>Concurrency control</b> is the set of rules — locking, ordering, or versioning — that keeps simultaneous edits from colliding."),
                ("병행제어는 여러 트랜잭션이 동시에 실행될 때 정합성을 지키기 위한 기법으로, 비관적 잠금(2단계 잠금 등), 낙관적 동시성 제어, 타임스탬프 순서 지정, MVCC(다중 버전 동시성 제어) 등이 있어요. ACID의 Isolation을 실제로 구현하는 방법이고, 어떤 방법을 쓰느냐에 따라 격리 수준과 성능이 달라져요.",
                 "Concurrency control preserves correctness when multiple transactions run at once, using techniques like pessimistic locking (e.g. two-phase locking), optimistic concurrency control, timestamp ordering, and MVCC (multi-version concurrency control). It's how ACID's Isolation is actually implemented, and the choice of method shapes both isolation level and performance.")),
    "glossary": [
        ("비관적 잠금(Locking)", "Pessimistic Locking", ("미리 상자를 잠가두는 것.", "Locking the box up front."), ("2단계 잠금(2PL)이 대표적이에요.", "Two-phase locking is the classic form.")),
        ("낙관적 동시성 제어", "Optimistic Concurrency Control", ("일단 해보고 나중에 충돌을 확인하는 것.", "Trying first, checking for conflicts later."), ("충돌이 드문 환경에서 빨라요.", "Fast when conflicts are rare.")),
        ("타임스탬프 순서 지정", "Timestamp Ordering", ("시간표로 처리 순서를 매기는 것.", "Ordering work by timestamp."), ("먼저 온 순서를 지켜요.", "Honors arrival order.")),
        ("MVCC", "MVCC", ("각자에게 스냅샷을 보여주는 것.", "Showing each transaction its own snapshot."), ("읽기가 쓰기를 막지 않아요.", "Reads don't block writes.")),
        ("데드락(교착상태)", "Deadlock", ("서로의 자물쇠를 기다리며 멈추는 것.", "Both sides stuck waiting on each other's lock."), ("순환 대기가 생기면 발생해요.", "Happens when a wait cycle forms.")),
        ("격리 수준", "Isolation Level", ("얼마나 엄격히 막을지 정하는 단계.", "The stage deciding how strictly to guard."), ('병행제어 방법이 이 수준을 실현해요. → <a href="isolevel-ko.html">동시에 손댈 때 얼마나 가려 볼지</a>', 'Concurrency control methods realize this level. → <a href="isolevel-en.html">how much to hide when hands overlap</a>')),
        ("ACID", "ACID", ("전표가 지키는 네 가지 약속.", "The four promises a receipt keeps."), ('병행제어는 그중 Isolation을 지켜줘요. → <a href="acid-ko.html">전표가 지키는 네 약속</a>', 'Concurrency control is what keeps the Isolation promise. → <a href="acid-en.html">the four promises a receipt keeps</a>')),
        ("합의(Consensus)", "Consensus", ("놀이공원 세계의 여러 서버가 뜻을 맞추는 이야기.", "A story from the amusement-park world about servers agreeing."), ('여러 서버에 걸친 동시성은 합의로 넘어가요. → <a href="consensus-ko.html">합의(Consensus)</a>', 'Concurrency across many servers moves into consensus. → <a href="consensus-en.html">consensus</a>')),
    ],
}
