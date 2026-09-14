from _draw import *
from _world import *


def arrow(x1, y1, x2, y2, color="var(--muted)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{x2 - 10} {y2 - 6} L{x2} {y2} L{x2 - 10} {y2 + 6}" stroke="{color}" stroke-width="3" fill="none"/>')


def step_box(x, y, w, h, title, doing, ps=0.5, fill="var(--panel)", stroke="var(--line)"):
    """순서표의 칸 하나: 제목 + 작은 앵무새 + 하는 일 한 가지."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
            + label(x + w / 2, y + 18, title, 11, "var(--ink)", cls="d")
            + parrot(x + 30, y + h - 26, ps) + label(x + w / 2 + 16, y + h / 2 + 12, doing, 11, "var(--muted)"))


def gate(x, y, ok=True):
    """칸 사이 검사 표시."""
    c = "var(--good)" if ok else "var(--bad)"
    return f'<circle cx="{x}" cy="{y}" r="11" fill="{c}"/>' + label(x, y + 4, "⟦✓|✓⟧" if ok else "⟦?|?⟧", 12, "#FFF")


# 1. 매번 앵무새에게 "번역하고 요약하고 표로" 다 맡기니 결과가 들쭉날쭉
P1 = svg(300, sky(300)
         + person(150, 110, s=0.9, face=EYES, **GUEST) + bubble(40, 30, 300, 40, "⟦번역하고, 요약하고, 표로 만들어 줘|translate, summarize, and make a table⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(360, 200, 140) + parrot(360, 160, 1.1, talk=True)
         + note(465, 50, 135, 90, "⟦월요일|MONDAY⟧", ("⟦표 → 요약|table → summary⟧", "⟦번역 빠짐|no translation⟧"), 0.9)
         + note(605, 50, 135, 90, "⟦화요일|TUESDAY⟧", ("⟦요약 → 번역|summary → translate⟧", "⟦표가 반쪽|half a table⟧"), 0.9)
         + label(600, 175, "⟦같은 부탁, 다른 결과|same request, different result⟧", 12, "var(--bad)")
         + label(380, 282, "⟦한 번에 다 맡기니 매번 결과가 들쭉날쭉해요|hand it all over at once and the result wobbles every time⟧", 13, "var(--ink)"))

# 2. 왜: 한 번에 다 시키면 앵무새가 순서를 스스로 정해야 하고, 매번 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(40, 50, 170, 110, "⟦한 장 쪽지|ONE NOTE⟧", ("⟦번역|translate⟧", "⟦요약|summarize⟧", "⟦표|table⟧"))
         + arrow(220, 105, 255, 105)
         + parrot(300, 150, 1.0, mood="think") + label(300, 230, "⟦순서를 혼자 정해요|it picks the order itself⟧", 11, "var(--ink)")
         + "".join(f'<path d="M340 150 L500 {82 + i * 60}" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4"/>' for i in range(3))
         + "".join(f'<rect x="500" y="{60 + i * 60}" width="225" height="44" rx="8" fill="var(--panel)" stroke="{s}" stroke-width="2"/>' + label(612, 87 + i * 60, t, 10, "var(--ink)")
                   for i, (t, s) in enumerate((("⟦번역 → 요약 → 표 ✓|translate → summarize → table ✓⟧", "var(--good)"),
                                                ("⟦요약 → 표 · 번역 빠짐 ×|summarize → table · no translate ×⟧", "var(--bad)"),
                                                ("⟦표 → 번역 → 표 다시 ×|table → translate → table again ×⟧", "var(--bad)"))))
         + label(612, 250, "⟦매번 다른 길|a different path every time⟧", 12, "var(--bad)")
         + label(380, 282, "⟦한 번에 다 시키면 앵무새가 길을 매번 새로 골라요|ask for everything at once and the parrot picks a new path each time⟧", 12, "var(--bad)"))

# 3. 워크플로 = 사람이 순서표를 미리 정하고, 앵무새는 칸마다 한 가지만 (hero)
P3 = svg(360, sky(360)
         + person(40, 90, s=0.9, face=SMILE, **TRAINER) + label(72, 215, "⟦사람이 순서를 정해요|a person sets the order⟧", 11, "var(--muted)")
         + "".join(note(x + 45, 60, 50, 42, "⟦쪽지|NOTE⟧", (), 0.85) for x in (150, 320, 490))
         + step_box(150, 120, 140, 72, "⟦1. 번역 칸|1. TRANSLATE⟧", "⟦번역만|translate only⟧")
         + gate(310, 156) + step_box(320, 120, 140, 72, "⟦2. 요약 칸|2. SUMMARIZE⟧", "⟦요약만|summarize only⟧")
         + gate(480, 156) + step_box(490, 120, 140, 72, "⟦3. 표 칸|3. TABLE⟧", "⟦표만|table only⟧")
         + arrow(632, 156, 650, 156) + note(655, 115, 95, 80, "⟦표|TABLE⟧", ("⟦✓ 늘 같아요|✓ always same⟧",), 0.95)
         + label(390, 225, "⟦칸마다 쪽지 하나, 하는 일 하나 — 칸 사이엔 검사|one note and one job per box — a check between boxes⟧", 12, "var(--ink)")
         + label(380, 262, "⟦에이전트: 앵무새가 순서를 정해요 · 워크플로: 사람이 미리 정해요|agent: the parrot picks the order · workflow: a person sets it beforehand⟧", 12, "var(--muted)")
         + label(380, 340, "⟦워크플로 = 사람이 미리 적어 둔 순서표 — 앵무새는 칸마다 한 가지만 해요|a workflow is an order chart a person wrote ahead — the parrot does one thing per box⟧", 13, "var(--ink)", cls="d"))

# 4. 순서표 디테일: 칸 4개 직렬, 칸 사이 검사, 칸마다 알맞은 앵무새
P4 = svg(320, sky(320)
         + step_box(25, 80, 150, 90, "⟦1. 읽기|1. READ⟧", "⟦글 꺼내기|pull the text⟧", 0.45)
         + gate(190, 125) + label(190, 200, "⟦기계 검사|machine check⟧", 10, "var(--muted)")
         + step_box(205, 80, 150, 90, "⟦2. 번역|2. TRANSLATE⟧", "⟦번역만|translate only⟧", 0.45)
         + gate(370, 125) + label(370, 200, "⟦사람 검사|person checks⟧", 10, "var(--muted)")
         + step_box(385, 80, 150, 90, "⟦3. 요약|3. SUMMARIZE⟧", "⟦요약만|summarize only⟧", 0.45)
         + gate(550, 125) + label(550, 200, "⟦길이 검사|length check⟧", 10, "var(--muted)")
         + step_box(565, 80, 150, 90, "⟦4. 표|4. TABLE⟧", "⟦표만|table only⟧", 0.6, "var(--good-soft)", "var(--good)")
         + label(100, 200, "⟦작은 앵무새|small parrot⟧", 10, "var(--muted)") + label(280, 200, "⟦작은 앵무새|small parrot⟧", 10, "var(--muted)") + label(460, 200, "⟦작은 앵무새|small parrot⟧", 10, "var(--muted)") + label(640, 200, "⟦큰 앵무새|big parrot⟧", 10, "var(--muted)")
         + label(380, 240, "⟦칸 사이마다 검사 — 틀리면 그 칸만 다시 해요|a check between boxes — if one is wrong, redo just that box⟧", 12, "var(--ink)")
         + label(380, 268, "⟦쉬운 칸엔 작은 앵무새로 충분해요 — 싸고 빨라요|an easy box needs only a small parrot — cheap and fast⟧", 11, "var(--muted)")
         + label(380, 300, "⟦같은 순서표를 돌리면 늘 같은 길로 가요|run the same chart and it always takes the same path⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 순서표는 예상 못 한 상황에 약해요 — 그땐 에이전트 칸을 하나 넣어요
MINI = lambda x, y, t, fill="var(--panel)", stroke="var(--line)", col="var(--ink)": f'<rect x="{x}" y="{y}" width="90" height="46" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="3"/>' + label(x + 45, y + 28, t, 11, col, cls="d")
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + MINI(30, 70, "⟦번역 ✓|translate ✓⟧") + arrow(122, 93, 138, 93) + MINI(140, 70, "⟦요약 ✓|summarize ✓⟧") + arrow(232, 93, 248, 93) + MINI(250, 70, "⟦표 ✓|table ✓⟧")
         + label(190, 150, "⟦정해진 일은 순서표가 딱이에요|for a fixed job, the chart just fits⟧", 11, "var(--ink)")
         + parrot(100, 215, 0.8, talk=True) + label(240, 225, "⟦매번 같은 결과|the same result every time⟧", 11, "var(--ink)")
         + MINI(410, 70, "⟦번역 ✓|translate ✓⟧") + arrow(502, 93, 518, 93) + MINI(520, 70, "⟦그림?|picture?⟧", "var(--panel)", "var(--bad)", "var(--bad)") + arrow(612, 93, 628, 93) + MINI(630, 70, "⟦…|…⟧", "var(--stone)", "var(--stone-dark)", "var(--muted)")
         + label(570, 150, "⟦표가 아니라 그림이 왔어요 — 순서표가 멈춰요|a picture came instead of a table — the chart stops⟧", 11, "var(--bad)")
         + '<rect x="470" y="190" width="200" height="54" rx="10" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="7 5"/>'
         + parrot(500, 222, 0.5) + label(595, 222, "⟦여기엔 에이전트 칸|put an agent box here⟧", 11, "var(--accent)")
         + label(380, 300, "⟦순서표는 예상 못 한 상황에 약해요 — 그 자리엔 순서를 스스로 정하는 칸을 넣어요|a chart is weak against surprises — there, put a box that picks its own order⟧", 12, "var(--ink)", cls="d"))

ONE_NOTE_I = icon('<rect x="8" y="16" width="30" height="34" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="18" y="8" width="26" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="18" y="8" width="26" height="8" rx="3" fill="#C9A86A"/><path d="M24 24 h14 M24 30 h10" stroke="#142033" stroke-width="2" stroke-linecap="round"/><ellipse cx="50" cy="50" rx="9" ry="6" fill="#5B8DEF"/><circle cx="50" cy="38" r="6" fill="#5B8DEF"/>')
GATE_I = icon('<rect x="4" y="22" width="18" height="20" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="42" y="22" width="18" height="20" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="32" cy="32" r="10" fill="var(--good)"/><path d="M27 32 l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none"/>')
CHART_I = icon('<rect x="8" y="10" width="48" height="12" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><rect x="8" y="26" width="48" height="12" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><rect x="8" y="42" width="48" height="12" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="4 3"/><text x="32" y="52" text-anchor="middle" font-size="9" font-weight="700" fill="var(--accent)">?</text>')
SMALL_PARROT_I = icon('<ellipse cx="22" cy="40" rx="9" ry="12" fill="#5B8DEF"/><circle cx="22" cy="24" r="7" fill="#5B8DEF"/><path d="M27 22 l8 2 l-8 4z" fill="#E9B44C"/><ellipse cx="46" cy="42" rx="6" ry="8" fill="#3F6FD1" opacity="0.5"/><circle cx="46" cy="30" r="5" fill="#3F6FD1" opacity="0.5"/><path d="M44 12 l6 6" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "workflow", "order": 26,
    "title": ("심부름 순서표", "The Errand Order Chart"),
    "h1": ("<em>워크플로</em>가 뭐예요?", "What is a <em>Workflow</em>?"),
    "sub": ("LLM 워크플로를 사람이 미리 적어 둔 순서표대로 앵무새가 칸마다 한 가지 일만 하는 이야기로 풀어봤어요.",
            "LLM workflows, told as a story about an order chart a person writes ahead of time, where the parrot does one thing per box."),
    "panels": [
        {"svg": P1, "alt": ("손님이 앵무새에게 번역하고 요약하고 표로 만들어 달라고 하고, 월요일 쪽지엔 번역이 빠지고 화요일 쪽지엔 표가 반쪽 — 같은 부탁, 다른 결과", "A guest asks the parrot to translate, summarize, and make a table; the Monday note is missing the translation and the Tuesday note has half a table — same request, different result"),
         "caption": ("매번 앵무새에게 번역하고, 요약하고, 표로 만들라고 다 맡겨요. 결과가 들쭉날쭉해요.", "Every day the parrot is told to translate, summarize, and make a table. The result wobbles."),
         "small": ("월요일엔 번역이 빠지고, 화요일엔 표가 반쪽이에요. 같은 부탁인데 왜 다를까요?", "Monday the translation is missing; Tuesday the table is half done. Same request — why different?")},
        {"svg": P2, "alt": ("'번역·요약·표' 한 장 쪽지가 생각하는 앵무새에게 가고, 앵무새에서 점선 세 갈래가 세 가지 다른 순서로 이어짐 — 하나만 ✓", "One note reading translate, summarize, table goes to a thinking parrot; three dashed paths lead to three different orders — only one gets a ✓"),
         "caption": ("왜냐면 한 번에 다 시키면 앵무새가 순서를 혼자 정하거든요. 그게 매번 달라요.", "Because when you ask for everything at once, the parrot picks the order itself. And that changes every time."),
         "small": ('한 장 <a href="prompt-ko.html">쪽지</a>에 일 세 가지가 들어 있으면 앵무새는 길을 매번 새로 골라요. 어떤 날은 한 가지를 빼먹어요.',
                   'With three jobs on one <a href="prompt-en.html">note</a>, the parrot picks a new path every time. Some days it skips one.')},
        {"svg": P3, "hero": True, "alt": ("조련사가 순서를 정하고, 칸 세 개(번역 칸 → 요약 칸 → 표 칸)마다 쪽지 하나와 작은 앵무새가 있고 칸 사이에 초록 ✓ 검사, 끝에 '늘 같아요' 표", "A trainer sets the order; three boxes (translate → summarize → table) each with one note and a small parrot, green ✓ checks between boxes, and at the end a table marked always the same"),
         "caption": ("워크플로는 사람이 미리 적어 둔 순서표예요. 앵무새는 칸마다 한 가지만 해요.", "A workflow is an order chart a person writes ahead of time. The parrot does one thing per box."),
         "small": ('번역 칸, 요약 칸, 표 칸. 칸마다 쪽지 하나, 하는 일 하나. <a href="agent-ko.html">에이전트</a>는 앵무새가 순서를 정하고, 워크플로는 사람이 정해요.',
                   'Translate box, summarize box, table box. One note and one job per box. In an <a href="agent-en.html">agent</a> the parrot picks the order; in a workflow a person does.'),
         "tricks": (4, [
             (ONE_NOTE_I, ("걸음마다 쪽지 하나", "One note per step"), ("한 칸엔 한 가지 일만", "one job per box"), "calm"),
             (GATE_I, ("걸음 사이에 검사", "A check between steps"), ("사람이나 기계가", "by a person or a machine"), "calm"),
             (CHART_I, ("정해진 일엔 순서표", "Fixed job, use the chart"), ("열린 일엔 에이전트", "open job, use an agent"), "warm"),
             (SMALL_PARROT_I, ("작은 앵무새로 충분", "A small parrot is enough"), ("쉬운 칸은 싸고 빠르게", "easy boxes, cheap and fast"), "warm"),
         ])},
        {"svg": P4, "alt": ("칸 네 개 직렬: 읽기 → 번역 → 요약 → 표. 칸 사이에 기계 검사, 사람 검사, 길이 검사 표시. 앞 세 칸은 작은 앵무새, 마지막 표 칸은 큰 앵무새", "Four boxes in a row: read → translate → summarize → table, with a machine check, a person check, and a length check between them; the first three boxes have small parrots, the last a big one"),
         "caption": ("칸 네 개가 한 줄로, 칸 사이마다 검사. 틀리면 그 칸만 다시 해요.", "Four boxes in a row, a check between each. If one is wrong, redo just that box."),
         "small": ('같은 순서표를 돌리면 늘 같은 길로 가요. 쉬운 칸엔 작은 앵무새로 충분해요 — 어느 앵무새에게 맡길지는 <a href="routing-ko.html">이 이야기</a>에서.',
                   'Run the same chart and it always takes the same path. An easy box needs only a small parrot — which parrot gets which box is <a href="routing-en.html">its own story</a>.')},
        {"svg": P5, "alt": ("왼쪽 초록: 번역 ✓ 요약 ✓ 표 ✓ 순서표가 매번 같은 결과. 오른쪽 빨강: 표 대신 그림이 와서 순서표가 멈춤, 아래 점선 상자에 '여기엔 에이전트 칸'", "Left, green: translate ✓ summarize ✓ table ✓ — the same result every time. Right, red: a picture came instead of a table and the chart stops; below, a dashed box says put an agent box here"),
         "caption": ("순서표는 예상 못 한 상황에 약해요. 그 자리엔 에이전트 칸을 하나 넣어요.", "A chart is weak against surprises. There, put in one agent box."),
         "small": ('정해진 일엔 순서표, 열린 일엔 <a href="agent-ko.html">에이전트</a>. 칸이 많아지고 앵무새가 여러 마리면 <a href="multiagent-ko.html">앵무새 회의</a>가 돼요.',
                   'Fixed jobs get a chart; open jobs get an <a href="agent-en.html">agent</a>. When there are many boxes and several parrots, it becomes a <a href="multiagent-en.html">parrot meeting</a>.')},
    ],
    "summary": (("<b>워크플로</b> = 사람이 <b>미리 적어 둔 순서표</b>. 앵무새는 <b>칸마다 한 가지만</b> 하고, 칸 사이엔 <b>검사</b>가 있어요. 정해진 일엔 순서표, 열린 일엔 에이전트.",
                 "<b>Workflow</b> = an <b>order chart a person writes ahead</b>. The parrot does <b>one thing per box</b>, with a <b>check</b> between boxes. Fixed jobs get a chart; open jobs get an agent."),
                ("LLM workflow. 사람이 정해 둔 고정 순서(프롬프트 체이닝, 파이프라인)로 LLM 호출을 여러 단계 이어 붙이는 방식이에요. 단계마다 프롬프트 하나와 검증 단계를 두고, 실행이 결정적이라 재현·디버깅이 쉬워요. 에이전트는 모델이 순서를 정하고, 워크플로는 코드가 정해요. 단계별로 작은 모델을 라우팅하면 비용이 줄어요.",
                 "A fixed sequence of LLM calls (prompt chaining, pipelines) laid out by a person. Each step has one prompt and a validation step, and execution is deterministic, so it is easy to reproduce and debug. In an agent the model decides the order; in a workflow the code does. Routing small models to easy steps cuts cost.")),
    "glossary": [
        ("워크플로", "Workflow", ("심부름 순서표.", "The errand order chart."), ("사람이 걸음 순서를 미리 정해요. 앵무새는 칸마다 한 가지만.", "A person sets the order of steps ahead. The parrot does one thing per box.")),
        ("프롬프트 체이닝", "Prompt chaining", ("쪽지를 줄줄이.", "Notes in a chain."), ("앞 칸의 답이 다음 칸의 쪽지에 들어가요.", "The answer from one box goes into the next box\'s note.")),
        ("파이프라인", "Pipeline", ("한 줄 순서표.", "The straight-line chart."), ("칸이 한 줄로 쭉 이어진 순서표예요. 갈림길이 없어요.", "A chart whose boxes run in one straight line. No forks.")),
        ("라우팅", "Routing", ("어느 앵무새에게 맡길까.", "Which parrot gets the box."), ('쉬운 칸은 작은 앵무새에게. → <a href="routing-ko.html">어느 앵무새에게 시킬까</a>', 'Easy boxes go to a small parrot. → <a href="routing-en.html">which parrot to ask</a>')),
        ("에이전트와의 차이", "Difference from an agent", ("순서를 누가 정하나.", "Who picks the order."), ('워크플로는 사람이, 에이전트는 앵무새가. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'A workflow: the person. An agent: the parrot. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
        ("결정적 실행", "Deterministic execution", ("늘 같은 길.", "Always the same path."), ("같은 순서표를 돌리면 같은 길로 가요. 틀리면 어느 칸인지 바로 알아요.", "Run the same chart and it takes the same path. When it fails, you know which box.")),
        ("검증 단계", "Validation step", ("칸 사이 검사.", "The check between boxes."), ("사람이나 기계가 봐요. 틀리면 그 칸만 다시.", "A person or a machine looks. If wrong, redo just that box.")),
        ("오케스트레이션", "Orchestration", ("칸이 많고 앵무새가 여럿.", "Many boxes, several parrots."), ('누가 언제 뭘 할지 정하는 일. → <a href="multiagent-ko.html">앵무새 회의</a>', 'Deciding who does what, when. → <a href="multiagent-en.html">the parrot meeting</a>')),
    ],
}
