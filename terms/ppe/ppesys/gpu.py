from _draw import *
from _world import *


def tire(x, y, s=1.0):
    return f'<circle cx="{x}" cy="{y}" r="{10 * s}" fill="none" stroke="var(--accent)" stroke-width="{3 * s}"/>'


def trainee(x, y, s=0.4):
    """작고 단순한 보조 정비사 한 명(GPU 코어 하나)."""
    return person(x, y, hat=None, shirt="#5B8DEF", s=s, face=EYES)


def crew_grid(x0, y0, cols, rows, gap=42, s=0.4):
    out = ""
    for r in range(rows):
        for c in range(cols):
            out += trainee(x0 + c * gap, y0 + r * gap, s)
    return out


# 1. 똑같은 타이어 점검 작업이 산더미처럼 쌓여요
P1 = svg(320, sky(320)
         + person(130, 160, s=0.85, face=SWEAT + EYES, **CHIEF)
         + tire(300, 240) + tire(340, 250) + tire(380, 235) + tire(420, 255) + tire(460, 240) + tire(500, 250) + tire(540, 235)
         + label(380, 30, "⟦차 수백 대, 똑같이 타이어만 점검하면 돼요|hundreds of cars, each needing the exact same tire check⟧", 13, "var(--ink)", cls="d")
         + label(380, 295, "⟦반장 혼자서는 하나씩 밖에 못 봐요|the chief alone can only check them one at a time⟧", 12, "var(--ink)"))

# 2. 더 뛰어난 정비사 한 명을 데려와도 여전히 한 대씩이에요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(240, 150, s=0.9, face=EYES, **CHIEF)
         + bubble(140, 60, 220, 42, "⟦제가 더 빨리, 더 잘할게요!|I'll do it faster, better!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + tire(430, 230) + tire(470, 245) + tire(510, 230) + tire(550, 245) + tire(590, 230) + tire(630, 245) + tire(670, 230)
         + label(380, 295, "⟦더 뛰어난 한 명을 써도, 결국 한 번에 한 대씩이에요|even a far better single mechanic still handles one car at a time⟧", 12, "var(--ink)"))

# 3. GPU = 똑같은 간단한 일을 한번에 수백 명이 나눠 하는 보조 정비팀 (hero)
P3 = svg(340, sky(340)
         + crew_grid(120, 110, 8, 4, 46, 0.38)
         + tire(650, 150) + tire(650, 200) + tire(650, 250)
         + label(650, 110, "⟦타이어 점검|TIRE CHECK⟧", 11, "var(--muted)")
         + label(380, 25, "⟦GPU = 똑같은 간단한 일을 한번에 수백 명이 나눠 하는 보조 정비팀|GPU = a crew of hundreds doing the same simple task all at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦한 명 한 명은 단순하지만, 다 같이 움직이면 엄청 빨라요|each one is simple alone, but together they're incredibly fast⟧", 12, "var(--muted)"))

# 4. CPU vs GPU 비교
P4 = svg(320, sky(320)
         + queueboard(60, 30, 330, 250, "⟦CPU vs GPU|CPU vs GPU⟧",
                      ["CPU: ⟦소수의 노련한 정비사|a few skilled mechanics⟧",
                       "CPU: ⟦복잡하고 서로 다른 일|complex, varied jobs⟧",
                       "GPU: ⟦수백~수천 보조 인력|hundreds-thousands of helpers⟧",
                       "GPU: ⟦같은 일을 동시에 반복|the same job, all at once⟧"], 1.0)
         + crew_grid(610, 110, 3, 3, 36, 0.3)
         + label(380, 300, "⟦GPU는 복잡한 한 가지보단, 단순한 걸 \'많이 동시에\' 잘해요|GPU shines at many simple things at once, not one complex thing⟧", 12, "var(--ink)"))

# 5. 복잡하고 갈라지는 일에는 안 맞아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + crew_grid(100, 120, 4, 2, 44, 0.35) + label(190, 230, "⟦똑같은 일, 수백 번|the same task, hundreds of times⟧", 11, "var(--ink)")
         + label(190, 248, "⟦GPU가 압도적으로 빨라요|GPU wins by a landslide⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=EYES, **CHIEF) + label(570, 235, "⟦하나씩 판단이 갈리는 복잡한 일|one complex job full of branching decisions⟧", 11, "var(--ink)")
         + label(570, 255, "⟦이건 CPU(반장) 몫이에요|this is still the chief's (CPU's) job⟧", 11, "var(--ink)")
         + label(380, 280, "⟦GPU는 CPU를 대신하지 않아요 — 서로 다른 일을 나눠 맡아요|GPU doesn't replace the CPU — they split different kinds of work⟧", 12, "var(--ink)", cls="d"))

CORE_I = icon('<circle cx="18" cy="18" r="8" fill="var(--accent)"/><circle cx="46" cy="18" r="8" fill="var(--accent)"/><circle cx="18" cy="46" r="8" fill="var(--accent)"/><circle cx="46" cy="46" r="8" fill="var(--accent)"/>')
SIMD_I = icon('<path d="M10 20 h44 M10 32 h44 M10 44 h44" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
THROUGHPUT_I = icon('<path d="M8 50 L24 30 L36 38 L56 12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
GPGPU_I = icon('<rect x="12" y="12" width="40" height="40" rx="6" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 h20 M32 22 v20" stroke="var(--good)" stroke-width="4"/>')

PAGE = {
    "slug": "gpu", "order": 6,
    "title": ("수백 명이 함께 움직이는 보조 정비팀", "The Hundred-Hand Helper Crew"),
    "h1": ("<em>GPU/GPGPU</em>가 뭐예요?", "What is <em>GPU/GPGPU</em>?"),
    "sub": ("GPU와 GPGPU를, 똑같은 간단한 일을 한번에 나눠 하는 보조 정비팀 이야기로 풀어봤어요.",
            "GPU and GPGPU, told as a story about a crew of helpers doing the same simple task all at once."),
    "panels": [
        {"svg": P1, "alt": ("차 수백 대가 똑같은 타이어 점검을 기다리고, 반장 혼자서는 감당 못 함", "Hundreds of cars wait for the identical tire check, and the chief alone can't keep up"),
         "caption": ("똑같은 타이어 점검이 산더미처럼 쌓여요.", "The same tire check piles up by the hundreds."),
         "small": ("반장 혼자서는 하나씩밖에 못 봐요.", "The chief alone can only check them one at a time.")},
        {"svg": P2, "alt": ("더 뛰어난 정비사 한 명을 데려와도 여전히 타이어를 한 대씩만 점검함", "Bringing in one far more skilled mechanic still checks tires one car at a time"),
         "caption": ("더 뛰어난 정비사 한 명을 데려와도 여전해요.", "Even a far better single mechanic doesn't change the shape of the problem."),
         "small": ("결국 한 번에 한 대씩이에요.", "In the end, it's still one car at a time.")},
        {"svg": P3, "hero": True, "alt": ("작은 보조 정비사 수십 명이 동시에 각자의 타이어를 점검함", "Dozens of small helper mechanics each check their own tire at the same moment"),
         "caption": ("GPU = 수백 명이 똑같은 간단한 일을 나눠 하는 보조 정비팀이에요.", "GPU = a crew of hundreds doing the same simple task all at once."),
         "small": ("한 명 한 명은 단순하지만, 같이 움직이면 엄청 빨라요.", "Each one is simple alone, but together they're incredibly fast."),
         "tricks": (4, [
             (CORE_I, ("코어 수백~수천 개", "Hundreds–Thousands of Cores"), ("손이 그만큼 많다는 뜻이에요", "that many hands at once")),
             (SIMD_I, ("SIMD", "SIMD"), ("모두에게 같은 동작을 동시에 시켜요", "the same move, given to everyone at once"), "calm"),
             (THROUGHPUT_I, ("처리량 우선", "Throughput-First"), ("복잡한 한 가지보단 단순한 여럿", "many simple things beat one complex thing"), "warm"),
             (GPGPU_I, ("GPGPU", "GPGPU"), ("원래 그림용 보조팀을 계산에도 써요", "the graphics crew, repurposed for general math")),
         ])},
        {"svg": P4, "alt": ("CPU는 소수의 노련한 정비사가 복잡한 일을, GPU는 수백 명이 같은 일을 동시에 함을 보여주는 순서판", "A board contrasting a CPU's few skilled mechanics on complex jobs with a GPU's hundreds doing the same job at once"),
         "caption": ("CPU와 GPU는 잘하는 일이 달라요.", "CPU and GPU are good at different kinds of work."),
         "small": ("GPU는 단순한 걸 \'많이 동시에\' 잘해요.", "GPU shines at many simple things at once.")},
        {"svg": P5, "alt": ("왼쪽: 똑같은 일을 수백 번 반복하면 GPU가 압도적으로 빠름. 오른쪽: 판단이 갈리는 복잡한 일은 여전히 반장(CPU) 몫", "Left: GPU wins big on hundreds of identical repeats. Right: complex, branching decisions still belong to the chief (CPU)"),
         "caption": ("복잡하고 갈라지는 일에는 안 맞아요.", "It's not suited to complex, branching work."),
         "small": ("GPU는 CPU를 대신하지 않아요 — 서로 다른 일을 나눠 맡아요.", "GPU doesn't replace the CPU — they split different kinds of work.")},
    ],
    "summary": (("<b>GPU</b> = 똑같이 단순한 일을 <b>수백~수천 개의 작은 손이 한번에</b> 나눠 처리하는 보조 정비팀. <b>GPGPU</b>는 이 팀을 그림 작업 말고 일반 계산에도 쓰는 것.",
                 "<b>GPU</b> = a crew of hundreds to thousands of small hands doing the same simple task all at once. <b>GPGPU</b> is putting that crew to work on general computation, not just graphics."),
                ("GPU(Graphics Processing Unit)는 수많은 단순 코어로 동일 연산을 여러 데이터에 동시에 적용하는 SIMD(Single Instruction, Multiple Data) 구조예요. 원래 픽셀·정점 연산을 병렬 처리하려고 만들어졌지만, 행렬 연산이 많은 딥러닝 등 범용 계산에도 쓰이게 되면서 GPGPU(General-Purpose computing on GPU)라는 말이 생겼어요. CPU는 적은 수의 강력한 코어로 분기·순차 로직을 빠르게 처리하는 데, GPU는 많은 수의 약한 코어로 처리량(throughput)을 극대화하는 데 강해요.",
                 "A GPU (Graphics Processing Unit) applies the same instruction to many data items at once across thousands of simple cores — a SIMD (Single Instruction, Multiple Data) design. Built originally for parallel pixel and vertex math, it's now used for general computation too, especially matrix-heavy workloads like deep learning — hence the term GPGPU (General-Purpose computing on GPU). A CPU excels at fast, branching, sequential logic with few powerful cores; a GPU excels at maximizing throughput with many simple ones.")),
    "glossary": [
        ("SIMD", "SIMD", ("모두에게 같은 동작을 동시에 시키는 것.", "Giving everyone the same move at once."), ("GPU 병렬 처리의 핵심 방식이에요.", "The core pattern behind GPU parallelism.")),
        ("GPGPU", "GPGPU", ("그림용 보조팀을 계산에도 쓰는 것.", "Putting the graphics crew to work on general math."), ("딥러닝 학습이 대표적인 예예요.", "Deep-learning training is the classic example.")),
        ("처리량(Throughput)", "Throughput", ("한 번에 얼마나 많이 처리하는지.", "How much gets processed at once."), ("GPU가 추구하는 핵심 가치예요.", "This is what GPU design optimizes for.")),
        ("AI 가속기(TPU·NPU)", "AI Accelerator (TPU/NPU)", ("한 가지 계산만을 위한 전용 로봇팔.", "A robot arm built for exactly one calculation."), ('GPU보다 한 걸음 더 특화된 보조 도구예요. → <a href="aiaccel-ko.html">오직 그 계산 하나만을 위한 전용 로봇팔</a>', 'An even more specialized step beyond the GPU. → <a href="aiaccel-en.html">the robot arm built for one calculation</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("리프트에 누가 먼저 올라갈지 정하는 규칙.", "The rule deciding who gets the lift first."), ('반장(CPU)이 일을 나눠 맡기는 또 다른 이야기예요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'Another story about the chief (CPU) handing out work. → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("프로세스/스레드", "Process/Thread", ("같은 차를 같이 고치는 여러 손.", "Several hands working the same car."), ('GPU의 \'많은 손\'도 결국 매우 가벼운 스레드 개념이에요. → <a href="processthread-ko.html">같은 차, 여러 손</a>', 'The GPU\'s "many hands" are, in effect, extremely lightweight threads. → <a href="processthread-en.html">one car, many hands</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("일이 늘 때 시간이 느는 정도를 재는 자.", "The ruler for how fast time grows as work piles up."), ('병렬로 나누면 같은 Big-O도 체감 속도가 달라져요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'Splitting work in parallel changes the felt speed even at the same Big-O. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("AI 분야의 GPU", "GPU in the AI World", ("앵무새가 앉는 빠른 횃대.", "The fast perch the parrot sits on."), ('AI 분야(앵무새 세계)에서는 추론 비용 관점으로 짧게 다뤄요. → <a href="inference-ko.html">AI 추론</a>', 'The AI world (the parrot world) covers it briefly, from the inference-cost angle. → <a href="inference-en.html">AI inference</a>')),
    ],
}
