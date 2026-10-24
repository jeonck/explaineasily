from _draw import *
from _world import *


def hose(x1, y1, x2, y2, n=1, color="var(--line)", w=4):
    """좁은 호스 한 가닥(=좁은 메모리 버스)."""
    out = ""
    for i in range(n):
        off = (i - (n - 1) / 2) * (w + 3)
        out += f'<path d="M{x1} {y1 + off} L{x2} {y2 + off}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
    return out


def toolstack(x, y, layers, s=1.0):
    """공구함을 층층이 쌓은 공구탑(=HBM 적층 다이)."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i in range(layers):
        yy = -i * 26
        out += f'<rect x="-30" y="{yy - 20}" width="60" height="22" rx="3" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>'
    out += f'<rect x="-6" y="{-layers * 26 - 4}" width="12" height="{layers * 26 + 4}" fill="#8B5E3C"/>'
    return out + '</g>'


# 1. 큰 엔진은 공구가 많이, 빨리 필요해요
P1 = svg(300, sky(300)
         + car(560, 210, 1.4, color="var(--accent)")
         + person(460, 150, s=0.9, face=SWEAT, **MECH1)
         + toolbox(300, 220, 0.9)
         + hose(330, 210, 440, 180, n=1)
         + label(380, 50, "⟦큰 엔진 작업은 공구가 한꺼번에 많이 필요해요|the big engine job needs lots of tools at once⟧", 13, "var(--ink)")
         + label(380, 270, "⟦호스 한 가닥으로는 공구가 줄줄이 늦게 와요|one thin hose means tools trickle in slowly⟧", 12, "var(--muted)"))

# 2. 호스를 늘려도 공구함이 멀면 소용없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + toolbox(120, 220, 0.9)
         + hose(150, 210, 560, 150, n=3)
         + car(600, 170, 1.2)
         + label(350, 120, "⟦호스를 세 가닥으로 늘려도 거리가 머니 느려요|three hoses still lag — the distance is too far⟧", 12, "var(--bad)", cls="d")
         + label(380, 60, "⟦공구함을 엔진 바로 옆에 두면 어떨까요?|what if the toolbox sat right next to the engine?⟧", 13, "var(--ink)")
         + label(380, 270, "⟦멀리 둔 채로는 가닥 수를 늘리는 것도 한계가 있어요|adding hoses only goes so far if the toolbox stays far away⟧", 12, "var(--muted)"))

# 3. HBM = 공구탑을 엔진 바로 옆에 쌓고 통로를 아주 넓게 뚫은 것 (hero)
P3 = svg(340, sky(340)
         + toolstack(260, 260, 4)
         + hose(290, 230, 420, 220, n=6, color="var(--accent)", w=5)
         + car(540, 230, 1.3)
         + label(380, 30, "⟦HBM = 공구탑을 엔진 바로 옆에 쌓고, 통로를 아주 넓게 뚫은 것|HBM stacks toolboxes right beside the engine with a very wide passage⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 번에 아주 많은 공구가 동시에 건너가요(고대역폭)|a huge amount of tools cross over at once — high bandwidth⟧", 12, "var(--muted)"))

STACK_I = icon('<rect x="14" y="40" width="36" height="12" rx="2" fill="var(--accent)"/><rect x="14" y="26" width="36" height="12" rx="2" fill="var(--accent)"/><rect x="14" y="12" width="36" height="12" rx="2" fill="var(--accent)"/>')
WIDE_I = icon('<path d="M8 20 h48 M8 32 h48 M8 44 h48" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>')
NEAR_I = icon('<rect x="8" y="22" width="18" height="20" rx="3" fill="var(--accent)"/><rect x="38" y="22" width="18" height="20" rx="3" fill="var(--line)"/><path d="M26 32 h12" stroke="var(--good)" stroke-width="4"/>')
COST_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 20 v24 M24 26 h16 M24 38 h16" stroke="var(--bad)" stroke-width="3"/>')

# 4. 일반 호스(DDR) vs HBM 통로 비교
P4 = svg(320, sky(320)
         + queueboard(60, 40, 320, 240, "⟦일반 호스(DDR)|ordinary hose (DDR)⟧",
                      ("⟦공구함이 멀리 떨어져 있어요|toolbox sits far away⟧",
                       "⟦가는 호스 몇 가닥뿐|just a few thin hoses⟧",
                       "⟦값은 싸요|cheaper⟧"), 1.0)
         + queueboard(410, 40, 300, 240, "⟦HBM — 적층 + 초광대역|HBM — stacked + ultra-wide⟧",
                      ("⟦공구탑이 엔진 바로 옆|stack sits right next to the engine⟧",
                       "⟦아주 많은 통로가 한 번에|a huge number of lanes at once⟧",
                       "⟦속도는 빠르지만 비싸요|faster, but pricier⟧"), 1.0, hl=1))

# 5. 공구탑도 한계는 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + toolstack(190, 220, 3, s=0.9)
         + label(190, 260, "⟦속도는 압도적으로 빨라요|overwhelmingly faster⟧", 11, "var(--ink)")
         + person(570, 180, s=0.8, face=FROWN, **CHIEF)
         + label(570, 250, "⟦탑을 더 쌓을수록 열이 많이 나고 비싸져요|stacking higher means more heat and more cost⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그래서 보통 대용량보단 AI·그래픽처럼 속도가 중요한 곳에 써요|so it's mainly used where speed matters most — AI, graphics⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "hbm", "order": 16,
    "title": ("엔진 바로 옆에 쌓은 공구탑", "The Toolbox Tower Stacked Right by the Engine"),
    "h1": ("<em>HBM(고대역폭 메모리)</em>이 뭐예요?", "What is <em>HBM (High Bandwidth Memory)</em>?"),
    "sub": ("HBM을, 엔진(CPU/GPU) 바로 옆에 공구탑(메모리)을 쌓고 아주 넓은 통로를 뚫어 쓰는 이야기로 풀어봤어요.",
            "HBM, told as a story about stacking a toolbox tower right next to the engine and connecting it through a very wide passage."),
    "panels": [
        {"svg": P1, "alt": ("큰 엔진 작업에 공구가 많이 필요한데 가는 호스 하나로는 느림", "The big engine job needs many tools, but a single thin hose is slow"),
         "caption": ("큰 엔진 작업은 공구가 한꺼번에 많이 필요해요.", "The big engine job needs lots of tools at once."),
         "small": ("호스 한 가닥으로는 공구가 줄줄이 늦게 와요.", "One thin hose means tools trickle in slowly.")},
        {"svg": P2, "alt": ("호스를 세 가닥으로 늘렸지만 공구함이 멀리 있어 여전히 느림", "Three hoses now run, but the toolbox is still far away and remains slow"),
         "caption": ("호스를 늘려도 공구함이 멀면 소용없어요.", "Adding hoses doesn't help if the toolbox stays far away."),
         "small": ("가닥 수를 늘리는 것도 거리 앞에선 한계가 있어요.", "Adding more hoses only goes so far against distance.")},
        {"svg": P3, "hero": True, "alt": ("공구탑이 엔진 바로 옆에 쌓여 있고 아주 넓은 통로로 연결됨", "A toolbox tower stacked right beside the engine, linked by a very wide passage"),
         "caption": ("HBM은 공구탑을 엔진 바로 옆에 쌓고 통로를 아주 넓게 뚫은 것이에요.", "HBM stacks toolboxes right beside the engine with a very wide passage."),
         "small": ("한 번에 아주 많은 공구가 동시에 건너가요.", "A huge amount of tools cross over at once — high bandwidth."),
         "tricks": (4, [
             (STACK_I, ("층층이 쌓기", "Stack in layers"), ("공구함 여러 개를 쌓아요", "stacks several toolboxes up"), "calm"),
             (NEAR_I, ("바로 옆에 두기", "Keep it right next door"), ("엔진 가까이 두어 거리 줄여요", "keeps it near the engine to cut distance")),
             (WIDE_I, ("통로를 아주 넓게", "Make the passage very wide"), ("한 번에 수천 가닥이 오가요", "thousands of lanes move at once")),
             (COST_I, ("비싼 대신 빠름", "Pricier, but faster"), ("열과 비용이 늘어요", "more heat and more cost"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 일반 DDR 메모리는 공구함이 멀고 호스가 가늘다. 오른쪽: HBM은 공구탑이 가깝고 통로가 아주 넓다", "Left: ordinary DDR keeps the toolbox far with a thin hose. Right: HBM keeps the tower close with a very wide passage"),
         "caption": ("일반 DDR과 HBM은 구조가 달라요.", "Ordinary DDR and HBM are structured differently."),
         "small": ("HBM은 속도는 빠르지만 더 비싸요.", "HBM is faster, but pricier.")},
        {"svg": P5, "alt": ("왼쪽: HBM 공구탑은 속도가 압도적으로 빠름. 오른쪽: 높이 쌓을수록 열과 비용이 늘어남", "Left: the HBM tower is overwhelmingly faster. Right: stacking higher raises heat and cost"),
         "caption": ("공구탑도 한계는 있어요.", "Even the toolbox tower has limits."),
         "small": ("그래서 보통 AI·그래픽처럼 속도가 중요한 곳에 써요.", "So it's mainly used where speed matters most — AI, graphics.")},
    ],
    "summary": (("<b>HBM</b>은 메모리 칩을 <b>층층이 쌓아 프로세서 바로 옆</b>에 두고, <b>아주 넓은 통로</b>로 연결해 데이터를 한꺼번에 많이 주고받는 메모리예요.",
                 "<b>HBM</b> stacks memory chips <b>in layers right beside the processor</b> and links them through a <b>very wide passage</b>, moving huge amounts of data at once."),
                ("HBM(High Bandwidth Memory, 고대역폭 메모리)은 DRAM 칩을 TSV(실리콘 관통전극)로 수직 적층하고, 인터포저를 통해 GPU·AI 가속기 바로 옆에 배치해 매우 넓은 버스 폭으로 연결한 메모리예요. 기존 DDR 메모리보다 훨씬 높은 대역폭을 제공하지만, 제조 공정이 복잡해 비용이 높고 발열 관리가 중요해요. 그래픽·AI 연산처럼 메모리 대역폭이 성능을 좌우하는 영역에 주로 쓰여요.",
                 "HBM (High Bandwidth Memory) vertically stacks DRAM chips using TSVs (through-silicon vias) and places them right next to a GPU or AI accelerator via an interposer, connecting them with a very wide bus. It offers far higher bandwidth than conventional DDR memory, but is costlier to manufacture and requires careful heat management. It's mainly used where memory bandwidth drives performance, such as graphics and AI workloads.")),
    "glossary": [
        ("HBM", "HBM", ("엔진 바로 옆에 쌓은 공구탑.", "The toolbox tower stacked right by the engine."), ("아주 넓은 통로로 연결돼요.", "Connected through a very wide passage.")),
        ("대역폭", "Bandwidth", ("한 번에 건너갈 수 있는 공구의 양.", "How many tools can cross at once."), ("통로가 넓을수록 대역폭이 커요.", "A wider passage means more bandwidth.")),
        ("TSV(실리콘 관통전극)", "TSV (Through-Silicon Via)", ("공구탑 층 사이를 바로 뚫은 기둥.", "The pillar drilled straight through the stacked layers."), ("적층된 칩끼리 바로 연결해요.", "Connects the stacked chips directly.")),
        ("인터포저", "Interposer", ("공구탑과 엔진을 잇는 받침판.", "The base plate linking the tower to the engine."), ("둘을 가깝게 배치하게 해줘요.", "Lets the two sit close together.")),
        ("DDR 메모리", "DDR Memory", ("멀리 떨어진 일반 공구함.", "The ordinary toolbox sitting far away."), ("HBM보다 싸지만 대역폭이 낮아요.", "Cheaper than HBM, but lower bandwidth.")),
        ("GPU/AI 가속기", "GPU/AI Accelerator", ("공구가 많이 필요한 큰 엔진.", "The big engine that needs lots of tools."), ("HBM이 주로 옆에 붙는 곳이에요.", "Where HBM is most often placed alongside.")),
        ("발열 관리", "Thermal Management", ("공구탑을 높이 쌓을수록 늘어나는 열.", "The heat that grows as the tower stacks higher."), ("HBM 설계의 큰 과제예요.", "A major challenge in HBM design.")),
        ("메모리 대역폭 병목", "Memory Bandwidth Bottleneck", ("공구가 늦게 와서 엔진이 노는 상태.", "The engine sitting idle because tools arrive too slowly."), ("HBM이 해결하려는 문제예요.", "The problem HBM aims to solve.")),
    ],
}
