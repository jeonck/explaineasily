from _draw import *

WORKER = dict(hat=None, shirt="#4A5A72")
GUEST = dict(hat="#E9B44C", shirt="#7B3FA0")


def shelf(x, y, s=1.0, highlight=False):
    c = "var(--bad)" if highlight else "#8B5E3C"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-30" width="80" height="60" rx="3" fill="{c}" opacity="{"1" if highlight else "0.85"}"/>'
            '<path d="M-40 -10 h80 M-40 10 h80" stroke="#5A3B22" stroke-width="2"/></g>')


def door(x, y, w=50, h=80, name=""):
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{WOOD}"/><circle cx="{x + w - 10}" cy="{y + h / 2}" r="4" fill="#E9B44C"/>'
            + label(x + w / 2, y - 10, name, 11, "var(--muted)") + "</g>")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 하나씩 순서대로만 하면 너무 느려요
P1 = svg(280, sky(280)
         + person(130, 150, s=0.85, face=SMILE, **WORKER)
         + door(260, 110, name="⟦부엌|kitchen⟧") + door(340, 110, name="⟦서재|study⟧") + door(420, 110, name="⟦금고|vault⟧")
         + label(600, 150, "⟦하나, 끝나면 다음, 또 끝나면 다음…|one, then wait, then the next, then wait…⟧", 12, "var(--muted)")
         + label(380, 258, "⟦순서대로만 하면 손님이 한참 기다려요|doing them strictly in order makes guests wait and wait⟧", 13, "var(--ink)"))

# 2. 미리 짐작해서 몰래 준비해 둬요
P2 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + person(160, 150, s=0.9, face=EYES, **WORKER)
         + bubble(90, 60, 230, 40, "⟦다음엔 부엌에 가겠지, 미리 가 볼게요|probably the kitchen next — let me go check early⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + door(430, 110, name="⟦부엌|kitchen⟧") + door(510, 110, name="⟦서재|study⟧") + door(590, 110, name="⟦금고|vault⟧")
         + '<path d="M260 160 L420 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 258, "⟦짐작이 맞으면 훨씬 빨라져요 — 그런데…|when the guess is right, it's much faster — but…⟧", 13, "var(--ink)"))

# 3. 짐작이 틀려도 엿본 흔적이 선반에 남아요 (hero)
P3 = svg(340, sky(340)
         + person(90, 170, s=0.85, face=EYES, **WORKER)
         + door(230, 130, name="⟦부엌|kitchen⟧") + door(310, 130, name="⟦서재|study⟧")
         + door(410, 130, name="⟦금고(다른 손님 방)|vault (another guest's room)⟧")
         + '<path d="M140 190 L400 160" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(400, 100, "⟦짐작이 틀려서 버려요 — 겉으로는 안전해 보여요|the guess was wrong, so it's discarded — looks safe on the surface⟧", 12, "var(--ink)", cls="d")
         + shelf(560, 220, 0.9, highlight=True) + label(560, 270, "⟦그런데 선반 위치에 흔적이 남아요|but a trace is left in the shelf's position⟧", 12, "var(--bad)")
         + person(680, 190, s=0.65, face=MASK) + '<path d="M650 220 q-30 10 -40 20" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 3" fill="none"/>'
         + label(380, 30, "⟦미리 짐작해서 일하다 생긴 흔적 = 투기적 실행이 남긴 캐시 흔적|the trace left by guessing ahead = the cache trace speculative execution leaves behind⟧", 13, "var(--ink)", cls="d"))

# 4. Meltdown vs Spectre 비교 + 패치
P4 = svg(300, sky(300)
         + box(50, 30, 310, 240, "⟦Meltdown|Meltdown⟧",
               ("⟦일꾼이 몰래 '금고'(커널)를 엿봐요|the worker secretly peeks at the \"vault\" (kernel)⟧", "⟦원래 못 들어가는 방인데 들여다봐요|a room it shouldn't enter at all⟧", "⟦CPU 설계 자체의 틈이에요|a gap in the CPU's own design⟧"), 12)
         + box(400, 30, 310, 240, "⟦Spectre|Spectre⟧",
               ("⟦일꾼이 다른 손님 방을 엿보도록 속여요|the worker is tricked into peeking at another guest's room⟧", "⟦프로그램을 속여서 짐작을 유도해요|a program is tricked into making the guess⟧", "⟦더 넓은 상황에서 일어나요|happens across a wider range of situations⟧"), 12))

# 5. 패치하면 느려지고, 완전히 없애긴 어려워요
P5 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.85, face=FROWN, **WORKER) + label(160, 240, "⟦짐작을 줄였더니 다시 느려져요|guess less, and it slows down again⟧", 11, "var(--bad)")
         + '<path d="M260 150 L340 150" stroke="var(--muted)" stroke-width="2"/>'
         + shelf(460, 150, 1.0) + label(460, 200, "⟦판자(패치)로 막아요|a patch boards it up⟧", 11, "var(--muted)")
         + person(640, 150, s=0.85, face=EYES, **GUEST)
         + label(380, 258, "⟦짐작 자체가 빠른 이유라서, 완전히 없애긴 어려워요|guessing ahead is why it's fast at all, so it can't be fully removed⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "cpuvuln", "order": 8,
    "title": ("미리 짐작해서 일하다 생긴 흔적", "The Trace Left by Guessing Ahead"),
    "h1": ("<em>CPU 보안 취약점(Meltdown/Spectre)</em>이 뭐예요?", "What are the <em>CPU Vulnerabilities (Meltdown/Spectre)</em>?"),
    "sub": ("Meltdown와 Spectre 같은 CPU 보안 취약점을 미리 짐작해서 몰래 일하다 생긴 흔적 이야기로 풀어봤어요.",
            "CPU vulnerabilities like Meltdown and Spectre, told as a story about the trace left behind by a worker who guesses ahead."),
    "panels": [
        {"svg": P1, "alt": ("일꾼이 부엌·서재·금고 문을 순서대로 하나씩만 열어 손님이 한참 기다림", "A worker opens the kitchen, study, and vault doors strictly one at a time, making a guest wait and wait"),
         "caption": ("하나씩 순서대로만 하면 너무 느려요.", "Doing everything strictly in order is far too slow."),
         "small": ("손님이 한참 기다려요.", "Guests end up waiting and waiting.")},
        {"svg": P2, "alt": ("일꾼이 '다음엔 부엌에 가겠지, 미리 가 볼게요'라고 중얼거리며 미리 부엌 쪽으로 감", "The worker mutters probably the kitchen next, let me go check early, and heads there ahead of time"),
         "caption": ("미리 짐작해서 몰래 준비해 둬요.", "The worker guesses ahead and quietly prepares."),
         "small": ("짐작이 맞으면 훨씬 빨라져요 — 그런데…", "When the guess is right, it's much faster. But...")},
        {"svg": P3, "hero": True, "alt": ("일꾼이 다른 손님의 금고 방까지 미리 짐작해서 들여다보고, 짐작이 틀려 버리지만 선반 위치에 흔적이 남고 가면 쓴 사람이 그 흔적을 엿봄", "The worker guesses ahead even into another guest's vault room; the guess is wrong and discarded, but a trace remains in the shelf's position, which a masked figure reads"),
         "caption": ("짐작이 틀려도 엿본 흔적이 선반에 남아요.", "Even a wrong guess leaves a trace behind, in the shelf."),
         "small": ("이 흔적을 재는 방법으로 몰래 알아낼 수 있어요 — 이게 Meltdown과 Spectre예요.", "That trace can be measured to sneak out information — this is Meltdown and Spectre."),
         "tricks": (4, [
             (icon('<path d="M16 48 L32 20 L48 48" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="32" cy="20" r="5" fill="var(--accent)"/>'),
              ("미리 짐작해서 일해요", "Guesses ahead"), ("투기적 실행이에요", "this is speculative execution"), "calm"),
             (icon('<path d="M20 20 L44 44 M44 20 L20 44" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>'),
              ("틀리면 버려요", "Wrong guesses are discarded"), ("겉으로는 안전해 보여요", "looks safe on the surface")),
             (icon('<rect x="14" y="26" width="36" height="20" rx="3" fill="var(--bad)"/><path d="M14 26 h36 v-4 a18 8 0 0 0 -36 0z" fill="#8B5E3C"/>'),
              ("그래도 흔적은 남아요", "But a trace still remains"), ("선반(캐시) 위치로요", "in the shelf — the cache"), "warm"),
             (icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 22 v10 l7 5" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>'),
              ("흔적을 재서 알아내요", "Measuring the trace reveals it"), ("사이드채널 공격이에요", "a side-channel attack")),
         ])},
        {"svg": P4, "alt": ("Meltdown 상자: 일꾼이 금고(커널)를 몰래 엿봄, CPU 설계 자체의 틈. Spectre 상자: 일꾼이 다른 손님 방을 엿보도록 속음, 더 넓은 상황에서 발생", "Meltdown box: the worker secretly peeks at the vault (kernel), a gap in the CPU's own design. Spectre box: the worker is tricked into peeking at another guest's room, happening across more situations"),
         "caption": ("Meltdown과 Spectre는 엿보는 대상이 달라요.", "Meltdown and Spectre differ in what gets peeked at."),
         "small": ("Meltdown은 원래 못 들어가는 방(커널)까지 엿보고, Spectre는 프로그램을 속여서 짐작을 유도해 다른 방을 엿봐요.", "Meltdown peeks into a room it should never enter at all (the kernel); Spectre tricks a program into guessing its way into another room.")},
        {"svg": P5, "alt": ("일꾼이 짐작을 줄이니 다시 느려지고, 선반에 판자(패치)를 덧댐", "The worker guesses less and slows down again, while a patch boards up the shelf"),
         "caption": ("패치하면 느려지고, 완전히 없애긴 어려워요.", "Patching slows things down, and the flaw can't be fully removed."),
         "small": ('<a href="patch-ko.html">판자(패치)</a>는 흔적을 줄이지만, 짐작 자체가 빠른 이유라서 완전히 없애진 못해요.',
                   'A <a href="patch-en.html">patch</a> reduces the trace, but can\'t remove it entirely — guessing ahead is the very reason it\'s fast at all.')},
    ],
    "summary": (("<b>CPU 보안 취약점(Meltdown/Spectre)</b> = CPU가 <b>미리 짐작해서</b> 몰래 일하다가, 짐작이 틀려도 <b>선반(캐시)에 남긴 흔적</b>을 엿보여 정보를 빼낼 수 있는 틈.",
                 "<b>The CPU vulnerabilities Meltdown and Spectre</b> = flaws where a CPU that <b>guesses ahead</b> leaves a <b>trace in its cache</b> even on a wrong guess — a trace that can be read back to leak information."),
                ("Meltdown과 Spectre(2018년 공개)는 현대 CPU의 투기적 실행(speculative execution) 최적화 기법을 악용하는 하드웨어 취약점이에요. CPU는 분기 예측으로 다음에 실행될 명령을 미리 수행하고, 예측이 틀리면 결과를 폐기하지만 그 과정에서 접근한 메모리가 캐시에 남아요. 공격자는 캐시 접근 시간 차이를 측정하는 사이드채널 공격으로 커널 메모리(Meltdown)나 다른 프로세스의 메모리(Spectre)를 간접적으로 읽어낼 수 있어요. 마이크로코드·OS 패치로 완화하지만 성능 저하가 따르고, 설계 자체의 트레이드오프라 완전한 제거는 어려워요.",
                 "Meltdown and Spectre (disclosed in 2018) are hardware vulnerabilities that abuse speculative execution, an optimization in modern CPUs. A CPU predicts and runs upcoming instructions ahead of time; if the prediction is wrong, the results are discarded, but the memory it touched along the way leaves a trace in the cache. An attacker can measure tiny differences in cache-access timing — a side-channel attack — to indirectly read kernel memory (Meltdown) or another process's memory (Spectre). Microcode and OS patches mitigate the issue but cost performance, and because the design trade-off is fundamental, it can't be eliminated completely.")),
    "glossary": [
        ("투기적 실행", "Speculative execution", ("미리 짐작해서 일하기.", "Doing the work before being asked."), ("CPU를 빠르게 만드는 핵심 기법이에요. 짐작이 틀리면 결과만 버려요.", "The core trick that makes a CPU fast. A wrong guess only discards the result.")),
        ("캐시 타이밍", "Cache timing", ("선반 위치의 흔적.", "The trace left in the shelf."), ("엿본 메모리가 캐시에 올라가 있으면 다시 읽을 때 더 빨라요 — 그 속도 차이로 흔적을 알아내요.", "Memory that was peeked at sits in the cache, so reading it again is faster — that speed gap gives away the trace.")),
        ("사이드채널 공격", "Side-channel attack", ("흔적을 재서 알아내기.", "Reading the trace by measuring it."), ("직접 훔치는 게 아니라 시간차 같은 간접 신호로 알아내요.", "Not a direct theft — it infers the secret from an indirect signal like timing.")),
        ("Meltdown", "Meltdown", ("금고(커널)까지 엿보기.", "Peeking all the way into the vault (kernel)."), ("원래 접근이 전혀 안 되는 영역까지 짐작으로 들여다봐요.", "Speculatively reaches into memory that should be completely off-limits.")),
        ("Spectre", "Spectre", ("다른 손님 방을 엿보도록 속이기.", "Tricking the worker into peeking at another guest's room."), ("프로그램 자체를 속여 짐작을 유도해요. Meltdown보다 막기 어려워요.", "Tricks the program itself into guessing wrong. Harder to fully block than Meltdown.")),
        ("마이크로코드 패치", "Microcode/OS patch", ("선반에 덧댄 판자.", "A patch boarding up the shelf."), ('제조사·OS가 함께 막아요. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'Fixed jointly by the chipmaker and the OS. → <a href="patch-en.html">the board the carpenter sent</a>')),
        ("성능 저하", "Performance cost", ("짐작을 줄이면 느려져요.", "Guess less, and it slows down."), ("안전과 속도를 맞바꾸는 트레이드오프예요.", "A straight trade-off between safety and speed.")),
        ("하드웨어 취약점", "Hardware vulnerability", ("CPU 설계 자체의 틈.", "A gap in the CPU's own design."), ('소프트웨어 패치만으론 완전히 못 막는 <a href="zeroday-ko.html">틈</a>이에요.', 'A <a href="zeroday-en.html">gap</a> that a software patch alone can\'t fully close.')),
    ],
}
