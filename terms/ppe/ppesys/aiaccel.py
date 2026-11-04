from _draw import *
from _world import *


def robotarm(x, y, s=1.0):
    """오직 한 동작만 하는 전용 로봇팔."""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="-8" y="-50" width="16" height="50" fill="var(--muted)"/>'
            f'<rect x="-28" y="-60" width="56" height="16" rx="4" fill="var(--accent)"/>'
            f'<rect x="-6" y="0" width="12" height="18" fill="#5A3B22"/>'
            f'<circle cx="0" cy="-60" r="6" fill="var(--good)"/></g>')


def trainee(x, y, s=0.4):
    return person(x, y, hat=None, shirt="#5B8DEF", s=s, face=EYES)


def crew_row(x0, y0, n, gap=36, s=0.35):
    return "".join(trainee(x0 + i * gap, y0, s) for i in range(n))


# 1. 행렬곱 같은 특정 계산만, 그것도 산더미처럼 쏟아져요
P1 = svg(320, sky(320)
         + crew_row(110, 220, 9, 34, 0.33)
         + label(280, 140, "⟦GPU 보조팀도 벅찰 만큼, 딱 한 가지 계산이 너무 많아요|even the GPU crew strains under one specific calculation, repeated endlessly⟧", 12, "var(--ink)", cls="d")
         + label(380, 30, "⟦\'숫자 곱하고 더하기\'를 수억 번 반복해야 해요|\'multiply and add\' has to repeat hundreds of millions of times⟧", 13, "var(--ink)", cls="d")
         + label(380, 295, "⟦범용 보조팀(GPU)은 안 쓰는 기능까지 갖춰서, 곱하고 더하기만 하기엔 낭비예요|the general crew (GPU) carries features this job never uses, so multiply-and-add alone wastes effort⟧", 11, "var(--muted)"))

# 2. 보조팀을 더 늘려도, 일반적인 손이라 어느 정도까지만 빨라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + crew_row(80, 180, 12, 30, 0.3)
         + label(380, 40, "⟦보조팀을 늘려도, 안 쓰는 기능까지 딸린 손이라 속도 향상에 한계가 있어요|adding general crew only helps so much — each helper carries unused features⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦곱하고 더하기만 할 거라면, GPU의 손은 \'너무 다재다능\'해요|for multiply-and-add alone, the GPU\'s hands are \'too versatile\' for the job⟧", 12, "var(--ink)"))

# 3. AI 가속기 = 오직 그 계산 하나만을 위해 만든 전용 로봇팔 (hero)
P3 = svg(340, sky(340)
         + robotarm(250, 230, 1.3) + robotarm(380, 230, 1.3) + robotarm(510, 230, 1.3)
         + label(380, 25, "⟦AI 가속기 = 오직 곱하고 더하기(행렬곱)만을 위해 만든 전용 로봇팔|an AI accelerator = a robot arm built only for multiply-and-add (matrix math)⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦로봇팔은 다른 일은 못 하지만, 행렬곱만큼은 GPU보다 훨씬 빠르고 전기를 적게 써요|the arm can't do anything else — but at matrix math it beats a GPU, far faster, on far less power⟧", 12, "var(--muted)"))

# 4. CPU vs GPU vs 전용 가속기
P4 = svg(320, sky(320)
         + queueboard(50, 30, 320, 250, "⟦유연함 vs 속도|FLEXIBILITY vs SPEED⟧",
                      ["CPU: ⟦뭐든 다 함, 느림|does anything, slow⟧",
                       "GPU: ⟦비슷한 일 많이, 더 빠름|many similar jobs, faster⟧",
                       "TPU: ⟦구글의 행렬곱 전용 로봇팔|Google's matrix-multiply arm⟧",
                       "NPU: ⟦폰 속의 작은 전용 로봇팔|the small arm inside your phone⟧"], 1.0)
         + robotarm(640, 190, 1.0)
         + label(380, 300, "⟦표 아래로 갈수록 할 줄 아는 일은 적지만, 그 일은 훨씬 빠르고 전기를 적게 써요|further down the board, each chip does fewer kinds of work — but far faster, on far less power⟧", 12, "var(--ink)"))

# 5. 전용 로봇팔은 CPU/GPU를 대신하지 않아요
P5 = svg(340, '<rect width="380" height="340" fill="var(--good-soft)"/><rect x="380" width="380" height="340" fill="var(--bad-soft)"/>'
         + robotarm(190, 210, 1.1) + label(190, 255, "⟦행렬곱 계산은 엄청 빨라요|matrix math is lightning fast⟧", 11, "var(--ink)")
         + person(570, 150, s=0.75, face=EYES, **CHIEF) + label(570, 258, "⟦다른 판단·제어는 여전히 반장(CPU) 몫|other logic and control still belong to the chief (CPU)⟧", 11, "var(--ink)")
         + label(380, 305, "⟦전용 로봇팔은 CPU·GPU 옆에서 함께 일해요, 혼자 다 하지 않아요|the dedicated arm works alongside the CPU and GPU — it doesn't do everything alone⟧", 12, "var(--ink)", cls="d"))

MATMUL_I = icon('<path d="M10 14 h20 M10 26 h20 M10 38 h20" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M38 32 h8" stroke="var(--accent)" stroke-width="3"/><path d="M50 14 v34" stroke="var(--good)" stroke-width="4"/>')
NPU_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>')
SPEC_I = icon('<path d="M32 10 v44" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><circle cx="32" cy="10" r="6" fill="var(--accent)"/>')
TRADE_I = icon('<path d="M14 24 h36 M14 40 h36" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M44 18 l6 6 l-6 6 M20 34 l-6 6 l6 6" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "aiaccel", "order": 8,
    "title": ("오직 그 계산 하나만을 위한 전용 로봇팔", "The Robot Arm Built for One Calculation"),
    "h1": ("<em>AI 가속기(TPU·NPU)</em>가 뭐예요?", "What is an <em>AI Accelerator (TPU/NPU)</em>?"),
    "sub": ("TPU·NPU 같은 AI 가속기를, 오직 한 가지 계산만을 위해 만든 전용 로봇팔 이야기로 풀어봤어요.",
            "AI accelerators like TPUs and NPUs, told as a story about a robot arm built for exactly one calculation."),
    "panels": [
        {"svg": P1, "alt": ("보조 정비팀이 \'숫자 곱하고 더하기\'라는 한 가지 계산을 수억 번 반복하느라 지침", "The helper crew wears out repeating one \'multiply and add\' calculation hundreds of millions of times"),
         "caption": ("AI 작업은 \'곱하고 더하기\' 한 가지 계산을 산더미처럼 쏟아내요.", "AI work pours out one calculation — multiply and add — by the hundreds of millions."),
         "small": ("범용 보조팀(GPU)은 안 쓰는 기능까지 갖춰서, 곱하고 더하기만 하기엔 낭비예요.", "The general crew (GPU) carries features this job never uses, so multiply-and-add alone wastes effort.")},
        {"svg": P2, "alt": ("보조팀 인원을 더 늘려도 속도 개선이 점점 둔화됨", "Adding more of the helper crew gives diminishing speed gains"),
         "caption": ("GPU 보조팀을 더 늘려도 속도 향상에는 한계가 있어요.", "Adding more GPU crew gives smaller and smaller speed gains."),
         "small": ("곱하고 더하기만 할 거라면, GPU의 손은 \'너무 다재다능\'해요.", "For multiply-and-add alone, the GPU\'s hands are too versatile.")},
        {"svg": P3, "hero": True, "alt": ("오직 한 동작만 반복하는 전용 로봇팔 세 대가 늘어서 있음", "Three dedicated robot arms, each repeating only one motion, stand in a row"),
         "caption": ("AI 가속기 = 오직 곱하고 더하기(행렬곱)만을 위한 전용 로봇팔이에요.", "An AI accelerator = a robot arm built only for multiply-and-add (matrix math)."),
         "small": ("전용 로봇팔(AI 가속기)은 다른 일은 못 하지만, 행렬곱만큼은 GPU보다 훨씬 빠르고 전기를 적게 써요.", "The dedicated arm (AI accelerator) can't do anything else — but at matrix math it beats a GPU, far faster, on far less power."),
         "tricks": (4, [
             (MATMUL_I, ("행렬곱 전용", "Built for Matrix Multiply"), ("신경망 계산의 핵심 동작이에요", "the core move behind neural-network math")),
             (SPEC_I, ("특화(Specialization)", "Specialization"), ("한 가지만 하니까 GPU보다 빠르고 전기도 적게 써요", "doing only one thing makes it faster than a GPU, on less power"), "calm"),
             (NPU_I, ("NPU", "NPU"), ("폰 안에 들어가는 작은 전용 로봇팔", "the small dedicated arm inside your phone")),
             (TRADE_I, ("트레이드오프", "Tradeoff"), ("다른 일은 전혀 못 해요", "it can't do anything else at all"), "warm"),
         ])},
        {"svg": P4, "alt": ("CPU·GPU·TPU·NPU를 유연함과 속도의 순서로 비교하는 순서판", "A board ranking CPU, GPU, TPU, and NPU from most flexible to most specialized"),
         "caption": ("할 수 있는 일이 다양한 칩일수록 한 가지 일은 더 느려요.", "The more kinds of work a chip can do, the slower it is at any one of them."),
         "small": ("표 아래로 갈수록 할 줄 아는 일은 적지만, 그 일은 훨씬 빠르고 전기를 적게 써요.", "Further down the board, each chip does fewer kinds of work — but far faster, on far less power.")},
        {"svg": P5, "alt": ("왼쪽: 전용 로봇팔이 행렬곱 계산을 매우 빠르게 해냄. 오른쪽: 반장(CPU)이 다른 판단과 제어를 계속 맡음", "Left: the dedicated arm does matrix math very fast. Right: the chief (CPU) keeps doing other logic and control"),
         "caption": ("전용 로봇팔은 CPU·GPU를 대신하지 않아요.", "The dedicated arm doesn't replace the CPU or GPU."),
         "small": ("전용 로봇팔은 행렬곱을 맡고, 나머지 일은 CPU·GPU가 맡아요.", "The arm takes the matrix math; the CPU and GPU take the rest.")},
    ],
    "summary": (("<b>AI 가속기</b>(TPU·NPU) = <b>오직 한 가지 계산</b>(주로 행렬곱)<b>만을 위해 만든 전용 하드웨어</b>. 그 한 가지는 CPU·GPU보다 훨씬 빠르고 전력을 덜 써요.",
                 "<b>AI accelerators</b> (TPUs, NPUs) = dedicated hardware built for exactly one kind of calculation (mainly matrix multiplication) — far faster and more power-efficient at that one thing than a CPU or GPU."),
                ("TPU(Tensor Processing Unit)는 구글이 신경망의 행렬곱·텐서 연산에 맞춰 설계한 전용 가속기(ASIC)이고, NPU(Neural Processing Unit)는 스마트폰 등 기기 안에서 저전력으로 추론을 처리하는 전용 가속기예요. CPU는 범용성, GPU는 대규모 병렬 처리, TPU/NPU는 특정 연산 패턴에 대한 전용 최적화라는 축으로 이해하면 돼요. 범용성을 희생하는 대신 그 연산에서는 속도와 전력 효율이 크게 올라가요.",
                 "A TPU (Tensor Processing Unit) is an ASIC Google designed specifically for the matrix and tensor math behind neural networks. An NPU (Neural Processing Unit) is a dedicated accelerator that runs inference on-device — in a smartphone, say — at low power. Think of these chips as a spectrum: CPU for generality, GPU for massive parallelism, TPU/NPU for hardware optimized to one specific computation pattern. Sacrificing generality buys a big jump in speed and power efficiency for that one pattern.")),
    "glossary": [
        ("TPU", "TPU", ("구글의 행렬곱 전용 로봇팔.", "Google's robot arm built for matrix multiply."), ("신경망 학습·추론에 특화됐어요.", "Specialized for neural-network training and inference.")),
        ("NPU", "NPU", ("폰 안에 들어가는 작은 전용 로봇팔.", "The small dedicated arm inside your phone."), ("저전력으로 추론을 처리해요.", "Runs inference at low power.")),
        ("특화(Specialization)", "Specialization", ("한 가지만 하도록 만든 것.", "Built to do just one thing."), ("범용성을 버리고 속도·효율을 얻어요.", "Trades generality for speed and efficiency.")),
        ("GPU/GPGPU", "GPU/GPGPU", ("똑같은 간단한 일을 한번에 나눠 하는 보조 정비팀.", "A crew doing the same simple task all at once."), ('가속기 스펙트럼에서 한 단계 앞에 있어요. → <a href="gpu-ko.html">수백 명이 함께 움직이는 보조 정비팀</a>', 'One step earlier on the accelerator spectrum. → <a href="gpu-en.html">the hundred-hand helper crew</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("리프트에 누가 먼저 올라갈지 정하는 규칙.", "The rule deciding who gets the lift first."), ('가속기를 쓸지 말지도 결국 반장(OS/스케줄러)이 조율해요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'Whether to use the accelerator is still coordinated by the chief (the OS/scheduler). → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("캐시 메모리", "Cache Memory", ("자주 쓰는 공구만 담는 작은 공구함.", "A small toolbox holding only the frequent tools."), ('전용 로봇팔도 자기만의 작은 공구함(온칩 메모리)을 가져요. → <a href="cachemem-ko.html">자주 쓰는 공구만 담는 공구함</a>', 'The dedicated arm has its own small toolbox too (on-chip memory). → <a href="cachemem-en.html">the toolbox that holds only the frequent tools</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("계산량이 늘 때 시간이 느는 정도를 재는 자.", "The ruler for how time grows as the amount of math grows."), ('행렬곱의 계산량 자체는 그대로지만, 전용 하드웨어가 상수를 크게 줄여요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'The matrix-multiply workload itself is unchanged — dedicated hardware just shrinks the constant factor. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("AI 분야의 GPU", "GPU in the AI World", ("AI 모델(앵무새)을 돌리는 빠른 장비(횃대).", "The fast hardware (perch) that runs an AI model (the parrot)."), ('추론 비용 관점에서 가속기를 짧게 다뤄요. → <a href="inference-ko.html">AI 추론</a>', 'Covers accelerators briefly, from the inference-cost angle. → <a href="inference-en.html">AI inference</a>')),
    ],
}
