from _draw import *
from _world import *


def bench(x, y, w, h, title, fill="var(--panel)"):
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="{fill}" stroke="var(--line)" stroke-width="2"/>'
            + label(w / 2, 20, title, 11, "var(--ink)", cls="d") + '</g>')


# 1. 정비사 한 명이 차 한 대를 처음부터 끝까지 다 고쳐요
P1 = svg(300, sky(300)
         + person(300, 150, s=0.9, face=SWEAT, **MECH1)
         + car(280, 230, 0.9)
         + car(520, 230, 0.5, color="var(--line)") + car(620, 230, 0.5, color="var(--line)")
         + label(380, 50, "⟦정비사 한 명이 접수·점검·수리·마무리를 혼자 다 해요|one mechanic alone does intake, check, repair, finish⟧", 13, "var(--ink)")
         + label(380, 270, "⟦뒤차들은 그동안 가만히 기다리고 있어요|the cars behind just wait the whole time⟧", 12, "var(--muted)"))

# 2. 한 대씩 순서대로만 하면 전체가 느려요
P2 = svg(345, '<rect width="760" height="345" fill="var(--bad-soft)"/>'
         + car(130, 200, 0.6) + car(280, 200, 0.6) + car(430, 200, 0.6) + car(580, 200, 0.6)
         + label(380, 130, "⟦한 대 끝나야 다음 대가 시작돼요|the next one starts only after this one finishes⟧", 12, "var(--bad)", cls="d")
         + person(380, 240, s=0.6, face=FROWN, **MECH1)
         + label(380, 60, "⟦차례를 지키는 건 좋지만 전체 작업 시간이 길어져요|taking turns is fair, but the total time stretches out⟧", 13, "var(--ink)")
         + label(380, 328, "⟦여러 작업대를 두고 동시에 처리하면 어떨까요?|what if several benches worked at once?⟧", 12, "var(--muted)"))

# 3. CPU 파이프라인 = 여러 작업대를 두고 여러 차를 동시에 겹쳐 처리하는 것 (hero)
P3 = svg(340, sky(340)
         + bench(40, 80, 130, 160, "⟦접수|intake⟧") + bench(190, 80, 130, 160, "⟦점검|check⟧")
         + bench(340, 80, 130, 160, "⟦수리|repair⟧") + bench(490, 80, 130, 160, "⟦도장|paint⟧")
         + bench(640, 80, 90, 160, "⟦출고|finish⟧")
         + car(105, 200, 0.45) + car(255, 200, 0.45, color="var(--good)") + car(405, 200, 0.45, color="var(--accent)") + car(555, 200, 0.45, color="var(--bad)")
         + label(380, 30, "⟦CPU 파이프라인 = 여러 작업대에서 여러 차를 동시에 겹쳐 처리하는 것|a pipeline overlaps several cars across several benches at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 순간에 네 대가 각기 다른 단계를 지나고 있어요|at any instant, four cars are each at a different stage⟧", 12, "var(--muted)"))

FETCH_I = icon('<rect x="12" y="20" width="40" height="26" rx="3" fill="var(--line)"/><path d="M32 10 v10" stroke="var(--accent)" stroke-width="3"/>')
DECODE_I = icon('<rect x="12" y="20" width="40" height="26" rx="3" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M20 33 h24" stroke="var(--good)" stroke-width="2.5"/>')
EXEC_I = icon('<circle cx="32" cy="32" r="18" fill="var(--accent)"/><path d="M26 32 l5 6 l9 -12" stroke="#fff" stroke-width="3" fill="none"/>')
WB_I = icon('<path d="M14 32 h36" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M42 24 l8 8 l-8 8" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. 동시에 겹쳐 처리되는 타임라인
P4 = svg(320, sky(320)
         + queueboard(60, 40, 640, 240, "⟦같은 시각, 각기 다른 단계|same instant, different stages⟧",
                      ("⟦1호차 — 지금 '도장' 단계|car 1 — now at 'paint'⟧",
                       "⟦2호차 — 지금 '수리' 단계|car 2 — now at 'repair'⟧",
                       "⟦3호차 — 지금 '점검' 단계|car 3 — now at 'check'⟧",
                       "⟦4호차 — 지금 '접수' 단계|car 4 — now at 'intake'⟧",
                       "⟦한 대씩이면 못 낼 속도가 나와요|a speed impossible one car at a time⟧"), 1.0, hl=4))

# 5. 앞차를 기다려야 할 때도 있어요(파이프라인 정체)
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + car(150, 170, 0.6) + car(230, 170, 0.6)
         + label(190, 250, "⟦보통은 작업대가 쉬지 않고 돌아가요|normally the benches never sit idle⟧", 11, "var(--ink)")
         + car(600, 170, 0.6, color="var(--bad)")
         + person(650, 130, s=0.6, face=FROWN, **CHIEF)
         + label(590, 250, "⟦부품이 안 와서 뒷차들이 멈추기도 해요(파이프라인 정체)|a missing part can stall every car behind it (a pipeline stall)⟧", 11, "var(--ink)")
         + label(380, 282, "⟦겹쳐 일할수록 빨라지지만, 한 곳이 막히면 전체가 멈춰요|overlapping speeds things up — but one jam stalls the whole line⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "cpupipeline", "order": 19,
    "title": ("여러 작업대에서 동시에 겹쳐 고치기", "Overlapping Repairs Across Several Benches"),
    "h1": ("<em>CPU 파이프라인</em>이 뭐예요?", "What is a <em>CPU Pipeline</em>?"),
    "sub": ("CPU 파이프라인을, 정비공장에 작업대를 여러 개 두고 여러 차를 동시에 겹쳐 처리하는 이야기로 풀어봤어요.",
            "CPU pipelining, told as a story about setting up several repair benches and overlapping several cars' repairs at once."),
    "panels": [
        {"svg": P1, "alt": ("정비사 한 명이 차 한 대를 접수부터 마무리까지 혼자 다 처리하며 땀을 흘림", "One mechanic alone sweats through intake-to-finish on a single car"),
         "caption": ("정비사 한 명이 차 한 대를 처음부터 끝까지 다 고쳐요.", "One mechanic handles a car from start to finish alone."),
         "small": ("뒤차들은 그동안 가만히 기다리고 있어요.", "The cars behind just wait the whole time.")},
        {"svg": P2, "alt": ("차 네 대가 한 줄로 서서 차례대로만 처리되길 기다림", "Four cars in a row, each waiting its turn to be processed one at a time"),
         "caption": ("한 대씩 순서대로만 하면 전체가 느려요.", "Handling one car at a time slows down the whole queue."),
         "small": ("여러 작업대를 두고 동시에 처리하면 어떨까요?", "What if several benches worked at once?")},
        {"svg": P3, "hero": True, "alt": ("접수·점검·수리·도장·출고 다섯 작업대에서 네 대의 차가 동시에 각기 다른 단계를 지남", "Five benches — intake, check, repair, paint, finish — with four cars each at a different stage at once"),
         "caption": ("CPU 파이프라인은 여러 작업대에서 여러 차를 동시에 겹쳐 처리하는 것이에요.", "A pipeline overlaps several cars across several benches at once."),
         "small": ("한 순간에 네 대가 각기 다른 단계를 지나고 있어요.", "At any instant, four cars are each at a different stage."),
         "tricks": (4, [
             (FETCH_I, ("인출(Fetch)", "Fetch"), ("다음 할 일을 가져와요", "brings in the next instruction"), "calm"),
             (DECODE_I, ("해독(Decode)", "Decode"), ("무슨 작업인지 읽어요", "reads what the work is")),
             (EXEC_I, ("실행(Execute)", "Execute"), ("실제로 수리를 해요", "actually does the repair")),
             (WB_I, ("기록(Writeback)", "Writeback"), ("결과를 다시 적어둬요", "writes the result back"), "warm"),
         ])},
        {"svg": P4, "alt": ("같은 시각 1~4호차가 각각 도장·수리·점검·접수 단계에 있음을 보여주는 표", "A board showing cars 1–4 each at paint, repair, check, and intake at the same instant"),
         "caption": ("같은 시각에도 차마다 다른 단계를 지나요.", "At the same moment, each car is at a different stage."),
         "small": ("한 대씩이면 못 낼 속도가 이렇게 나와요.", "This overlapping achieves a speed impossible one car at a time.")},
        {"svg": P5, "alt": ("왼쪽: 보통은 작업대가 쉬지 않고 돌아감. 오른쪽: 부품이 안 와서 뒷차들이 멈추는 파이프라인 정체", "Left: benches normally run without idling. Right: a missing part stalls the cars behind it"),
         "caption": ("앞차를 기다려야 할 때도 있어요.", "Sometimes a car still has to wait on the one ahead."),
         "small": ("겹쳐 일할수록 빨라지지만, 한 곳이 막히면 전체가 멈춰요.", "Overlapping speeds things up, but one jam can stall the whole line.")},
    ],
    "summary": (("<b>CPU 파이프라인</b>은 명령어 처리를 <b>여러 단계로 나눠</b>, 여러 작업대처럼 <b>동시에 겹쳐 처리</b>해 전체 처리 속도를 높이는 구조예요.",
                 "A <b>CPU pipeline</b> <b>splits instruction processing into stages</b> and runs them <b>overlapped, like several benches at once</b>, to raise overall throughput."),
                ("CPU 파이프라이닝은 명령어 하나를 인출(Fetch)·해독(Decode)·실행(Execute)·메모리 접근(Memory)·기록(Writeback) 등 여러 단계로 나누고, 각 단계를 서로 다른 하드웨어가 동시에 처리하도록 겹쳐 실행하는 기법이에요. 한 명령어가 끝나길 기다리지 않고 다음 명령어를 바로 투입할 수 있어 처리량(throughput)이 크게 늘어요. 다만 앞선 결과를 기다려야 하는 데이터 해저드나 분기 예측이 틀렸을 때 파이프라인을 비워야 하는 제어 해저드 때문에 정체(stall)가 생길 수 있어요.",
                 "CPU pipelining splits processing a single instruction into stages — fetch, decode, execute, memory access, writeback — and overlaps them so different hardware handles each stage simultaneously. Because the next instruction can start before the previous one finishes, throughput rises significantly. However, data hazards (waiting on an earlier result) and control hazards (flushing the pipeline after a mispredicted branch) can cause stalls.")),
    "glossary": [
        ("파이프라이닝", "Pipelining", ("여러 작업대에서 여러 차를 겹쳐 처리하는 것.", "Overlapping several cars across several benches."), ("처리량을 크게 늘려줘요.", "Significantly raises throughput.")),
        ("인출(Fetch)", "Fetch", ("다음 할 일을 가져오는 단계.", "The stage that brings in the next instruction."), ("파이프라인의 첫 단계예요.", "The first stage of the pipeline.")),
        ("해독(Decode)", "Decode", ("무슨 작업인지 읽어내는 단계.", "The stage that reads what the instruction means."), ("명령어를 실행 가능한 형태로 풀어요.", "Unpacks the instruction into an executable form.")),
        ("실행(Execute)", "Execute", ("실제로 작업을 처리하는 단계.", "The stage that actually does the work."), ("연산이 실제로 일어나는 단계예요.", "Where the computation actually happens.")),
        ("데이터 해저드", "Data Hazard", ("앞차의 결과를 기다려야 하는 상황.", "Needing to wait on the result of the car ahead."), ("결과가 아직 안 나와서 생겨요.", "Happens because a result isn't ready yet.")),
        ("분기 예측", "Branch Prediction", ("다음에 어느 길로 갈지 미리 짐작하는 것.", "Guessing ahead which path comes next."), ("틀리면 파이프라인을 비워야 해요.", "A wrong guess means flushing the pipeline.")),
        ("파이프라인 정체(스톨)", "Pipeline Stall", ("부품이 안 와서 뒷차들이 멈추는 것.", "Cars behind stalling because a part hasn't arrived."), ("해저드가 생기면 발생해요.", "Occurs when a hazard arises.")),
        ("처리량(Throughput)", "Throughput", ("일정 시간에 처리되는 차의 수.", "How many cars get processed in a given time."), ("파이프라이닝의 핵심 목표예요.", "The core goal of pipelining.")),
    ],
}
