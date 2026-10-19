from _draw import *
from _world import *


def box(x, y, s=1.0, text="", color="#E9B44C"):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-18" width="52" height="34" rx="3" fill="{color}" stroke="#C9822B" stroke-width="2"/>'
    out += label(0, 5, text, 12, "#142033", cls="d")
    return out + '</g>'


def box_stack(x, y, labels, s=1.0, gap=38):
    out = ""
    for i, t in enumerate(labels):
        out += box(x, y - i * gap, s, t)
    return out


# 1. 상자 더미에서 딱 그것만 콕 집어 꺼내야 해요
P1 = svg(300, sky(300)
         + box_stack(200, 230, ["D", "C", "B", "A"], 1.0, 44)
         + person(380, 160, s=0.8, face=SWEAT + EYES, **MECH1)
         + bubble(440, 80, 230, 42, "⟦B 상자가 필요한데, 맨 위는 D예요|I need box B, but D is on top⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦아무렇게나 쌓으면 원하는 걸 바로 못 꺼내요|a messy pile means you can't grab what you need right away⟧", 12, "var(--ink)"))

# 2. 그렇다고 순서를 안 정해도 결과가 뒤죽박죽이에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + box(520, 150, 1.0, "D") + box(590, 170, 1.0, "A") + box(460, 190, 1.0, "C") + box(560, 220, 1.0, "B")
         + person(240, 170, s=0.8, face=FROWN, **MECH1)
         + label(380, 40, "⟦규칙 없이 쌓고 꺼내면, 순서가 매번 달라져요|pile and grab without a rule, and the order changes every time⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦\'넣은 순서\'와 \'꺼내는 순서\' 사이에 규칙이 있어야 해요|there has to be a rule between \'the order things went in\' and \'the order they come out\'⟧", 12, "var(--ink)"))

# 3. 선형 자료구조 = 물건을 쌓거나 줄 세우는 정해진 규칙 (hero)
P3 = svg(340, sky(340)
         + box_stack(170, 270, ["C", "B", "A"], 1.0, 40)
         + label(170, 110, "⟦스택(LIFO)|STACK (LIFO)⟧", 13, "var(--ink)", cls="d")
         + label(170, 128, "⟦나중에 넣은 게 먼저 나와요|last one in, first one out⟧", 11, "var(--muted)")
         + car(500, 230, 0.6, "var(--accent)") + car(570, 230, 0.6, "#5B8DEF") + car(640, 230, 0.6, "#2E8B57")
         + label(570, 110, "⟦큐(FIFO)|QUEUE (FIFO)⟧", 13, "var(--ink)", cls="d")
         + label(570, 128, "⟦먼저 넣은 게 먼저 나와요|first one in, first one out⟧", 11, "var(--muted)")
         + label(380, 310, "⟦둘 다 \'한 줄\'이지만, 꺼내는 쪽이 달라요 — 꼭대기냐 맨 앞이냐|both are \"a single line\" — but you take from the top, or from the front⟧", 12, "var(--muted)"))

# 4. 밀고 당기기: push/pop vs enqueue/dequeue
P4 = svg(320, sky(320)
         + queueboard(50, 30, 300, 250, "⟦동작 이름|OPERATION NAMES⟧",
                      ["Stack: ⟦push = 위에 올리기|push = place on top⟧",
                       "Stack: ⟦pop = 위에서 내리기|pop = take off the top⟧",
                       "Queue: ⟦enqueue = 줄 뒤에 서기|enqueue = join the back⟧",
                       "Queue: ⟦dequeue = 줄 앞에서 나가기|dequeue = leave from the front⟧"], 1.0)
         + box(620, 150, 1.0, "A")
         + label(620, 100, "⟦배열(Array)|Array⟧", 12, "var(--good)", cls="d")
         + label(620, 200, "⟦번호로 바로 찾기|find by index, directly⟧", 10, "var(--muted)")
         + label(380, 300, "⟦배열처럼 \'번호로 바로 찾는\' 구조도 같이 알아두면 좋아요|an array — finding things directly by index — is worth knowing alongside these⟧", 12, "var(--ink)"))

# 5. 쌓다 보면 넘치고, 줄이 안 줄면 끝없이 길어져요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + box_stack(190, 210, ["C", "B", "A"], 0.9, 36) + label(190, 248, "⟦규칙대로면 빠르고 단순해요|follow the rule, and it's fast and simple⟧", 11, "var(--ink)")
         + box_stack(570, 230, ["?", "F", "E", "D", "C", "B", "A"], 0.65, 24) + label(570, 268, "⟦너무 쌓으면 넘쳐요(스택 오버플로)|stack too high, and it overflows⟧", 11, "var(--ink)")
         + label(380, 302, "⟦규칙은 단순하지만, 한도를 넘기면 둘 다 문제가 생겨요|the rule is simple — but push either one past its limit, and trouble follows⟧", 12, "var(--ink)", cls="d"))

PUSH_I = icon('<rect x="16" y="28" width="32" height="20" rx="3" fill="var(--accent)"/><path d="M32 22 v-12 M26 16 l6 -6 l6 6" stroke="var(--accent)" stroke-width="3" fill="none"/>')
POP_I = icon('<rect x="16" y="16" width="32" height="20" rx="3" fill="var(--muted)"/><path d="M32 42 v12 M26 48 l6 6 l6 -6" stroke="var(--bad)" stroke-width="3" fill="none"/>')
ENQ_I = icon('<rect x="8" y="26" width="12" height="12" fill="var(--good)"/><rect x="24" y="26" width="12" height="12" fill="var(--good)"/><path d="M44 32 h10 M50 26 l6 6 l-6 6" stroke="var(--good)" stroke-width="3" fill="none"/>')
DEQ_I = icon('<path d="M4 32 h10 M10 26 l6 6 l-6 6" stroke="var(--bad)" stroke-width="3" fill="none"/><rect x="24" y="26" width="12" height="12" fill="var(--good)"/><rect x="40" y="26" width="12" height="12" fill="var(--good)"/>')

PAGE = {
    "slug": "stackqueue", "order": 7,
    "title": ("상자는 쌓고, 차는 줄 세우고", "Boxes Get Stacked, Cars Get Queued"),
    "h1": ("<em>스택과 큐</em>가 뭐예요?", "What are <em>Stacks and Queues</em>?"),
    "sub": ("스택·큐 같은 선형 자료구조를, 공구 상자를 쌓는 법과 차를 줄 세우는 법 이야기로 풀어봤어요.",
            "Stacks and queues, told as a story about the right way to stack parts boxes and line up cars."),
    "panels": [
        {"svg": P1, "alt": ("상자가 아무렇게나 쌓여 있어 필요한 B 상자를 바로 못 꺼냄", "Boxes are piled randomly, so the needed box B can't be grabbed right away"),
         "caption": ("상자 더미에서 딱 그것만 콕 집어 꺼내야 해요.", "You need to grab exactly the one box you want from a pile."),
         "small": ("아무렇게나 쌓으면 원하는 걸 바로 못 꺼내요.", "A messy pile means you can't grab what you need right away.")},
        {"svg": P2, "alt": ("상자들이 규칙 없이 어지럽게 흩어져 있음", "Boxes are scattered with no rule to how they're placed"),
         "caption": ("규칙 없이 쌓고 꺼내면 순서가 매번 달라져요.", "Pile and grab without a rule, and the order changes every time."),
         "small": ("\'넣은 순서\'와 \'꺼내는 순서\' 사이에 규칙이 있어야 해요.", "There has to be a rule linking the order in to the order out.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽: 상자가 위로 쌓인 스택(LIFO). 오른쪽: 차가 옆으로 늘어선 큐(FIFO)", "Left: boxes stacked upward — a LIFO stack. Right: cars lined up sideways — a FIFO queue"),
         "caption": ("선형 자료구조 = 물건을 쌓거나 줄 세우는 정해진 규칙이에요.", "Linear data structures = fixed rules for stacking or lining things up."),
         "small": ("꺼내는 쪽이 달라요 — 꼭대기냐, 맨 앞이냐.", "They differ in where you take from — the top, or the front."),
         "tricks": (4, [
             (PUSH_I, ("push", "push"), ("상자를 맨 위에 올려요", "place a box on top")),
             (POP_I, ("pop", "pop"), ("맨 위 상자부터 내려요", "take the top box off"), "warm"),
             (ENQ_I, ("enqueue", "enqueue"), ("줄 맨 뒤에 가서 서요", "join the back of the line"), "calm"),
             (DEQ_I, ("dequeue", "dequeue"), ("줄 맨 앞부터 나가요", "leave from the front of the line")),
         ])},
        {"svg": P4, "alt": ("push·pop·enqueue·dequeue 네 동작을 적은 순서판과, 번호로 바로 찾는 배열 상자", "A board naming push, pop, enqueue, dequeue, plus an array box found directly by index"),
         "caption": ("동작마다 이름이 따로 있어요.", "Each operation has its own name."),
         "small": ("배열처럼 \'번호로 바로 찾는\' 구조도 같이 알아두면 좋아요.", "An array — finding things directly by index — is worth knowing too.")},
        {"svg": P5, "alt": ("왼쪽: 적당히 쌓은 상자는 빠르고 단순함. 오른쪽: 너무 높이 쌓은 상자가 스택 오버플로로 넘침", "Left: a reasonably stacked pile stays fast and simple. Right: stacking too high overflows — a stack overflow"),
         "caption": ("쌓다 보면 넘치고, 줄이 안 줄면 끝없이 길어져요.", "Stack it too high and it overflows; let a queue grow unchecked and it never stops."),
         "small": ("규칙은 단순해도, 한도를 넘기면 둘 다 문제가 생겨요.", "The rule is simple — but push either one past its limit, and trouble follows.")},
    ],
    "summary": (("<b>스택</b> = 상자를 <b>위로 쌓고 위에서부터 꺼내는</b>(LIFO) 규칙. <b>큐</b> = 차를 <b>줄 세우고 앞에서부터 내보내는</b>(FIFO) 규칙.",
                 "<b>Stack</b> = stack boxes up and take from the top (LIFO). <b>Queue</b> = line cars up and send them off from the front (FIFO)."),
                ("스택(Stack)은 후입선출(LIFO, Last-In-First-Out) 구조로 push(삽입)·pop(삭제)이 한쪽 끝에서만 일어나고, 함수 호출·되돌리기(undo) 등에 쓰여요. 큐(Queue)는 선입선출(FIFO, First-In-First-Out)로 enqueue(삽입)는 뒤에서, dequeue(삭제)는 앞에서 일어나며, 작업 대기열 등에 쓰여요. 배열(Array)은 인덱스로 바로 접근(O(1))하지만 크기 변경이 비싸고, 연결 리스트(Linked List)는 삽입·삭제가 쉽지만 순차 접근만 가능해요.",
                 "A stack is Last-In-First-Out (LIFO): push (insert) and pop (remove) both happen at one end, and it underlies function calls and undo history. A queue is First-In-First-Out (FIFO): enqueue (insert) happens at the back, dequeue (remove) at the front, and it underlies task waiting lines. An array gives direct O(1) index access but is costly to resize; a linked list makes insertion and removal easy but only allows sequential access.")),
    "glossary": [
        ("스택(LIFO)", "Stack (LIFO)", ("나중에 넣은 상자가 먼저 나옴.", "The last box in comes out first."), ("push·pop은 맨 위에서만 일어나요.", "push and pop happen only at the top.")),
        ("큐(FIFO)", "Queue (FIFO)", ("먼저 줄 선 차가 먼저 나감.", "The first car in line leaves first."), ("enqueue는 뒤, dequeue는 앞이에요.", "Enqueue at the back, dequeue at the front.")),
        ("배열", "Array", ("번호가 매겨진 상자 선반.", "A numbered shelf of boxes."), ("번호로 바로 찾아요, 빠르지만 크기 변경이 비싸요.", "Direct lookup by number — fast, but resizing is costly.")),
        ("CPU 스케줄링(큐 활용)", "CPU Scheduling (uses a queue)", ("작업 순서판 자체가 큐예요.", "The job board itself is a queue."), ('그 순서판이 어떻게 쓰이는지는 여기서 봐요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'See how that board gets used. → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("기아현상(새치기하는 큐)", "Starvation (a queue that lets cutting)", ("급한 차가 계속 새치기하는 줄.", "A line where urgent cars keep cutting in."), ('순서 규칙이 깨지면 큐가 불공평해져요. → <a href="deadlockstarve-ko.html">서로의 열쇠를 기다리며 멈춘 정비공장</a>', 'Break the ordering rule, and the queue turns unfair. → <a href="deadlockstarve-en.html">the garage frozen waiting on each other\'s keys</a>')),
        ("이진트리", "Binary Tree", ("갈림길마다 왼쪽/오른쪽을 고르는 선반 지도.", "A shelf map where every fork picks left or right."), ('한 줄이 아니라 갈라지는 구조는 여기서 다뤄요. → <a href="bintree-ko.html">갈림길에서 반씩 줄여가는 선반 지도</a>', 'A branching structure, instead of a single line. → <a href="bintree-en.html">the shelf map that halves the search at every fork</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("자료가 늘 때 걸리는 시간을 재는 자.", "The ruler for how time grows as data grows."), ('push/pop은 O(1), 중간 삽입은 더 느려요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'push/pop are O(1); inserting in the middle is slower. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("메시지 큐(다른 세계)", "Message Queue (another world)", ("SRE 세계의 비슷한 \'줄 세우기\'.", "A similar \"lining up\" idea in the SRE world."), ('서비스 사이에 작업을 주고받는 큐도 있어요. → <a href="messagequeue-ko.html">SRE 세계의 메시지 큐</a>', 'Services pass work to each other through queues too. → <a href="messagequeue-en.html">the message queue in the SRE world</a>')),
    ],
}
