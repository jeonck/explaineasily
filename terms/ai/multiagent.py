from _draw import *
from _world import *


def arrow(x1, y1, x2, y2, color="var(--muted)"):
    import math
    deg = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M0 0 l-10 -6 l0 12z" transform="translate({x2},{y2}) rotate({deg:.0f})" fill="{color}"/>')


def paper(x, y):
    """주고받는 작은 쪽지."""
    return f'<rect x="{x - 11}" y="{y - 8}" width="22" height="16" rx="2" fill="{PAPER}" stroke="#C9A86A" stroke-width="2"/><path d="M{x - 6} {y - 2} h12 M{x - 6} {y + 3} h8" stroke="#142033" stroke-width="1.5"/>'


# 1. 한 앵무새에게 조사·글쓰기·검토를 다 시키니 쟁반이 넘쳐요
P1 = svg(300, sky(300)
         + person(40, 120, s=0.9, face=EYES, **GUEST) + bubble(20, 30, 260, 44, "⟦조사하고, 쓰고, 검토까지 해 줘|research it, write it, and review it⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(400, 200, 140) + parrot(400, 160, 1.1, mood="sweat")
         + tray(470, 130, 260, 70, "⟦쟁반이 넘쳐요|the tray overflows⟧")
         + beans(500, 118, ("⟦조사|find⟧", "⟦글|write⟧", "⟦검토|check⟧", "⟦조사|find⟧", "⟦글|write⟧", "⟦검토|check⟧"), 0.9, 40)
         + bean(740, 215, 0.8) + bean(455, 225, 0.8)
         + label(380, 282, "⟦한 앵무새에게 다 시키니 쟁반이 넘치고 역할이 섞여요|one parrot doing everything: the tray overflows and the roles mix⟧", 13, "var(--ink)"))

# 2. 쟁반 하나에 다 올리면 앞의 것이 밀려나고, 검토하는 눈도 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(140, 70, "⟦처음 조사한 게 밀려나요|the first research gets pushed off⟧", 11, "var(--bad)")
         + tray(40, 110, 340, 70, "⟦쟁반 하나에 전부|everything on one tray⟧")
         + f'<g opacity="0.3">{bean(70, 98, 0.9, text="⟦조사|find⟧")}{bean(110, 98, 0.9, text="⟦조사|find⟧")}{bean(150, 98, 0.9, text="⟦조사|find⟧")}</g>'
         + beans(190, 98, ("⟦글|write⟧", "⟦글|write⟧", "⟦글|write⟧", "⟦글|write⟧"), 0.9, 40)
         + parrot(470, 150, 1.0, talk=True) + bubble_parrot(390, 40, 160, 40, "⟦글 다 썼어요!|all written!⟧", 11)
         + label(470, 240, "⟦혼자 쓰고 혼자 믿어요|writes alone, trusts alone⟧", 11, "var(--ink)")
         + perch(660, 190, 100) + label(660, 150, "⟦검토하는 눈 ×|no reviewing eye ×⟧", 12, "var(--bad)") + label(660, 252, "⟦빈 횃대|empty perch⟧", 11, "var(--muted)")
         + label(380, 282, "⟦쟁반 하나에 다 올리면 앞의 것이 밀려나고, 검토하는 눈도 없어요|pile it all on one tray and the front falls off — and nobody reviews⟧", 12, "var(--bad)"))

# 3. 멀티에이전트 = 역할이 다른 앵무새 여러 마리 + 진행자 한 마리 (hero)
P3 = svg(360, sky(360)
         + label(380, 30, "⟦진행자 앵무새|the host parrot⟧", 12, "var(--ink)", cls="d")
         + perch(380, 130, 140) + parrot(380, 90, 1.2, color=PARROT_BIG, talk=True)
         + label(120, 50, "⟦역할마다 쪽지가 달라요|each role gets a different note⟧", 11, "var(--muted)")
         + label(480, 100, "⟦나누고, 모아요|splits, then gathers⟧", 11, "var(--muted)")
         + note(60, 120, 80, 62, "⟦쪽지|NOTE⟧", ("⟦조사해 줘|research⟧",), 0.8) + note(640, 120, 80, 62, "⟦쪽지|NOTE⟧", ("⟦검토해 줘|review⟧",), 0.8)
         + arrow(355, 140, 165, 172) + arrow(392, 140, 392, 172) + arrow(405, 140, 595, 172)
         + "".join(perch(x, 275, 110) + parrot(x, 235, 1.0) + label(x, 185, t, 12, "var(--ink)", cls="d")
                   for x, t in ((150, "⟦조사 앵무새|research parrot⟧"), (380, "⟦작성 앵무새|writer parrot⟧"), (610, "⟦검토 앵무새|review parrot⟧")))
         + label(380, 340, "⟦멀티에이전트 = 역할이 다른 앵무새 여러 마리에게 나눠 시키고, 한 마리가 조율해요|multi-agent: split the job among parrots with different roles, and one parrot coordinates⟧", 13, "var(--ink)", cls="d"))

# 4. 회의 그림: 진행자 가운데, 쪽지를 주고받고, 각자 작은 쟁반
P4 = svg(320, sky(320)
         + label(380, 40, "⟦앵무새끼리는 쪽지로만 말해요|parrots talk to each other only by note⟧", 12, "var(--ink)")
         + '<ellipse cx="380" cy="150" rx="110" ry="38" fill="var(--stone)" opacity="0.55"/>'
         + parrot(380, 140, 0.9, color=PARROT_BIG) + label(380, 96, "⟦진행자|host⟧", 11, "var(--ink)", cls="d")
         + tray(30, 160, 110, 44) + bean(60, 148, 0.7, text="⟦조사|find⟧") + bean(100, 148, 0.7, text="⟦조사|find⟧") + label(85, 100, "⟦각자 작은 쟁반|each has a small tray⟧", 11, "var(--muted)")
         + parrot(190, 175, 0.9) + label(190, 128, "⟦조사 앵무새|research parrot⟧", 11, "var(--ink)")
         + tray(620, 160, 110, 44) + bean(650, 148, 0.7, text="⟦글|write⟧") + bean(690, 148, 0.7, text="⟦글|write⟧")
         + parrot(570, 175, 0.9) + label(570, 128, "⟦작성 앵무새|writer parrot⟧", 11, "var(--ink)")
         + parrot(380, 240, 0.8) + label(320, 245, "⟦검토|review⟧", 11, "var(--ink)")
         + tray(430, 225, 100, 40) + bean(455, 213, 0.7, text="⟦검토|check⟧") + bean(490, 213, 0.7, text="⟦검토|check⟧")
         + arrow(340, 140, 218, 160) + paper(280, 140) + arrow(420, 140, 542, 160) + paper(480, 140)
         + arrow(380, 180, 380, 205) + paper(400, 190)
         + label(380, 300, "⟦진행자가 나누고 모아요. 앵무새끼리는 쪽지로만, 검토는 따로|the host splits and gathers; parrots talk by note only, and review is separate⟧", 12, "var(--ink)"))

# 5. 앵무새가 늘면 콩과 어긋남도 늘어요 — 두 마리면 될 일에 다섯 마리 쓰지 않기
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + label(190, 40, "⟦두 마리면 될 일은 두 마리|a two-parrot job gets two parrots⟧", 12, "var(--ink)", cls="d")
         + parrot(120, 130, 1.0) + parrot(260, 130, 1.0)
         + bean(150, 215, 0.9) + bean(190, 215, 0.9) + bean(230, 215, 0.9) + label(190, 250, "⟦콩 셋, 답 하나|three beans, one answer⟧", 11, "var(--muted)")
         + label(570, 40, "⟦다섯 마리면 콩도 어긋남도 늘어요|five parrots: more beans, more mismatch⟧", 12, "var(--ink)", cls="d")
         + "".join(parrot(430 + i * 70, 120, 0.75) for i in range(5))
         + label(535, 175, "⟦파랑이래|says blue⟧", 10, "var(--bad)") + label(605, 175, "⟦빨강이래|says red⟧", 10, "var(--bad)")
         + "".join(bean(430 + i * 36, y, 0.8) for y in (205, 232) for i in range(8))
         + label(560, 262, "⟦콩 열여섯, 서로 다른 답|sixteen beans, different answers⟧", 11, "var(--bad)")
         + label(380, 300, "⟦앵무새가 늘면 콩(비용)과 어긋남도 늘어요 — 필요한 만큼만|more parrots mean more beans (cost) and more mismatch — use only as many as you need⟧", 12, "var(--ink)", cls="d"))

ROLES_I = icon(f'<circle cx="16" cy="22" r="9" fill="{PARROT}"/><circle cx="32" cy="42" r="9" fill="{PARROT}"/><circle cx="48" cy="22" r="9" fill="{PARROT}"/><path d="M22 20 l7 2 l-7 3z M38 20 l7 2 l-7 3z M38 40 l7 2 l-7 3z" fill="#E9B44C"/>')
HOST_I = icon(f'<circle cx="32" cy="18" r="11" fill="{PARROT_BIG}"/><path d="M40 16 l8 2 l-8 3z" fill="#E9B44C"/><path d="M32 30 v10 M32 40 l-18 12 M32 40 v14 M32 40 l18 12" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
NOTE_I = icon('<rect x="10" y="26" width="24" height="18" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M15 33 h14 M15 38 h9" stroke="#142033" stroke-width="2"/><path d="M38 34 h16" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/><path d="M50 28 l6 6 l-6 6" stroke="var(--accent)" stroke-width="3" fill="none"/>')
EYE_I = icon('<path d="M8 32 q24 -22 48 0 q-24 22 -48 0z" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--ink)"/><path d="M42 48 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "multiagent", "order": 18,
    "title": ("앵무새 회의", "The Parrot Meeting"),
    "h1": ("<em>멀티에이전트</em>가 뭐예요?", "What is <em>Multi-agent</em>?"),
    "sub": ("멀티에이전트를 역할이 다른 앵무새 여러 마리에게 일을 나눠 시키고 한 마리가 조율하는 회의 이야기로 풀어봤어요.",
            "Multi-agent systems, told as a story about a meeting where parrots with different roles share the work and one parrot coordinates."),
    "panels": [
        {"svg": P1, "alt": ("손님이 조사·글쓰기·검토를 한 앵무새에게 다 부탁함. 땀 흘리는 앵무새 옆 쟁반에 조사·글·검토 콩이 섞여 넘치고 콩이 떨어짐", "The guest asks one parrot to research, write and review; beside the sweating parrot a tray overflows with mixed find, write and check beans, and beans fall off"),
         "caption": ("한 앵무새에게 다 시켰어요. 쟁반이 넘치고 역할이 섞여요.", "One parrot got everything. The tray overflows and the roles mix."),
         "small": ('조사 콩, 글 콩, 검토 콩이 <a href="context-ko.html">쟁반</a> 하나에 섞여요. 앵무새는 지금 조사를 하는 건지 검토를 하는 건지 헷갈려요.',
                   'Find beans, write beans and check beans all mix on one <a href="context-en.html">tray</a>. The parrot can\'t tell whether it is researching or reviewing right now.')},
        {"svg": P2, "alt": ("쟁반 앞쪽의 조사 콩 세 개가 흐려져 밀려나고 글 콩만 남음. 앵무새가 글 다 썼다고 말하지만 옆의 횃대는 비어 있음, 검토하는 눈 ×", "The three find beans at the front fade and fall off, leaving only write beans; the parrot says all written, but the perch beside it is empty, no reviewing eye ×"),
         "caption": ("쟁반 하나에 다 올리면 앞의 것이 밀려나요. 검토하는 눈도 없어요.", "Pile it all on one tray and the front falls off. And nobody reviews."),
         "small": ('글을 쓰다 보면 처음 조사한 콩이 <a href="context-ko.html">쟁반</a> 밖으로 밀려나요. 게다가 쓴 앵무새가 자기 글을 검토하면 자기 실수를 못 봐요.',
                   'By the time it writes, the research beans have been pushed off the <a href="context-en.html">tray</a>. And a parrot reviewing its own writing misses its own mistakes.')},
        {"svg": P3, "hero": True, "alt": ("위쪽 횃대의 큰 진행자 앵무새가 조사·작성·검토 앵무새 세 마리에게 점선 화살표로 쪽지를 보냄. 왼쪽 쪽지 조사해 줘, 오른쪽 쪽지 검토해 줘", "A big host parrot on the top perch sends notes by dashed arrows to three parrots: research, writer, review. Left note says research, right note says review"),
         "caption": ("멀티에이전트는 역할이 다른 앵무새 여러 마리에게 나눠 시키고, 한 마리가 조율하는 거예요.", "Multi-agent means splitting the job among parrots with different roles, with one parrot coordinating."),
         "small": ('조사 앵무새, 작성 앵무새, 검토 앵무새가 각자 <a href="prompt-ko.html">쪽지</a>를 따로 받아요. 진행자 앵무새가 일을 나누고, 결과를 모아요. 한 마리 한 마리는 <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>예요.',
                   'The research parrot, the writer parrot and the review parrot each get their own <a href="prompt-en.html">note</a>. The host parrot splits the job and gathers the results. Each one is <a href="agent-en.html">a parrot that plans its own errands</a>.'),
         "tricks": (4, [
             (ROLES_I, ("역할마다 쪽지가 달라요", "A different note per role"), ("조사·작성·검토", "research, write, review"), "calm"),
             (HOST_I, ("진행자가 나누고 모아요", "The host splits and gathers"), ("한 마리가 조율해요", "one parrot coordinates")),
             (NOTE_I, ("앵무새끼리는 쪽지로만", "Parrots talk by note only"), ("쟁반은 각자 따로", "each keeps its own tray"), "calm"),
             (EYE_I, ("검토 앵무새는 따로", "A separate review parrot"), ("쓴 새가 검토하지 않아요", "the writer never reviews itself"), "warm"),
         ])},
        {"svg": P4, "alt": ("둥근 탁자 가운데 진행자 앵무새. 왼쪽 조사 앵무새, 오른쪽 작성 앵무새, 아래 검토 앵무새가 점선 화살표와 작은 쪽지로 진행자와 이어짐. 각자 옆에 작은 쟁반과 자기 콩", "A host parrot at the center of a round table; the research parrot on the left, the writer parrot on the right and the review parrot below connect to the host by dashed arrows and small notes. Each has a small tray with its own beans"),
         "caption": ("진행자가 나누고 모아요. 앵무새끼리는 쪽지로만 말하고, 검토는 따로 해요.", "The host splits and gathers. Parrots talk by note only, and review is separate."),
         "small": ('작은 쟁반엔 자기 일 콩만 있어서 밀려나지 않아요. 결과를 넘기는 건 쪽지 한 장이에요(핸드오프). 조사와 작성처럼 서로 안 기다리는 일은 동시에 시켜요.',
                   'A small tray holds only that parrot\'s beans, so nothing falls off. Passing a result is a single note (a handoff). Jobs that don\'t wait on each other, like research and writing, run at the same time.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새 두 마리와 콩 세 개, 답 하나. 오른쪽 빨강: 앵무새 다섯 마리가 파랑이래, 빨강이래 하며 어긋나고 콩 열여섯 개가 쌓임", "Left, green: two parrots, three beans, one answer. Right, red: five parrots disagree, says blue, says red, and sixteen beans pile up"),
         "caption": ("앵무새가 늘면 콩(비용)과 어긋남도 늘어요. 필요한 만큼만 써요.", "More parrots mean more beans (cost) and more mismatch. Use only as many as you need."),
         "small": ('두 마리면 될 일에 다섯 마리를 쓰지 않아요. 순서가 늘 같으면 <a href="workflow-ko.html">심부름 순서표</a>가 더 싸요. 한 마리가 어떻게 일하는지는 <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>, 쟁반 크기는 <a href="context-ko.html">앵무새 앞의 쟁반</a>에서.',
                   'Don\'t use five parrots for a two-parrot job. If the order never changes, an <a href="workflow-en.html">errand checklist</a> is cheaper. How one parrot works: <a href="agent-en.html">the parrot that plans its own errands</a>; tray size: <a href="context-en.html">the tray in front of the parrot</a>.')},
    ],
    "summary": (("<b>멀티에이전트</b> = <b>역할이 다른 앵무새 여러 마리</b>(조사·작성·검토)에게 일을 나눠 시키고, <b>진행자 한 마리</b>가 나누고 모으는 것. 쟁반은 각자 따로, 말은 <b>쪽지로만</b>. 앵무새가 늘면 콩과 어긋남도 늘어요.",
                 "<b>Multi-agent</b> = splitting a job among <b>several parrots with different roles</b> (research, write, review), with <b>one host parrot</b> that splits and gathers. Each keeps its own tray and they talk <b>by note only</b>. More parrots mean more beans and more mismatch."),
                ("Multi-agent system. 역할별 프롬프트와 도구를 가진 서브에이전트 여러 개를 오케스트레이터가 조율해요. 각자 컨텍스트 창이 분리되고, 결과는 핸드오프 메시지로 넘겨요. 독립된 작업은 병렬 실행하고 검토자는 작성자와 분리해요. 에이전트 수만큼 토큰 비용과 조율 오류가 늘어나므로 꼭 필요한 만큼만 나눠요.",
                 "An orchestrator coordinates several sub-agents, each with its own prompt and tools. Their context windows are separate and results pass as handoff messages. Independent work runs in parallel and the reviewer is kept apart from the writer. Token cost and coordination errors grow with every agent, so split only as much as needed.")),
    "glossary": [
        ("멀티에이전트", "Multi-agent", ("앵무새 회의.", "The parrot meeting."), ("역할이 다른 앵무새 여러 마리가 한 일을 나눠 해요.", "Several parrots with different roles share one job.")),
        ("오케스트레이터", "Orchestrator", ("진행자 앵무새.", "The host parrot."), ("일을 나누고, 결과를 모으고, 다음을 정해요.", "Splits the job, gathers the results, decides what is next.")),
        ("역할 분담", "Role assignment", ("조사·작성·검토.", "Research, write, review."), ('역할마다 <a href="prompt-ko.html">쪽지</a>와 도구가 달라요.', 'Each role has its own <a href="prompt-en.html">note</a> and tools.')),
        ("핸드오프", "Handoff", ("결과를 넘기는 쪽지 한 장.", "The one note that passes a result."), ("쟁반을 통째로 넘기지 않고 필요한 것만 적어 줘요.", "Not the whole tray — just what the next parrot needs.")),
        ("서브에이전트", "Sub-agent", ("회의에 앉은 앵무새 한 마리.", "One parrot at the meeting."), ('각자 작은 쟁반을 써요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'Each keeps a small tray. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
        ("병렬 실행", "Parallel execution", ("동시에 시키기.", "Running at the same time."), ("서로 안 기다리는 일은 같이 해요. 빨라지지만 콩은 그만큼 들어요.", "Jobs that don\'t wait on each other run together — faster, but the beans still add up.")),
        ("비용", "Cost", ("앵무새 수만큼 콩.", "Beans per parrot."), ('다섯 마리면 콩도 다섯 배. → <a href="pricing-ko.html">콩 값</a>', 'Five parrots, five times the beans. → <a href="pricing-en.html">the price of beans</a>')),
        ("에이전트", "Agent", ("한 마리가 일하는 법.", "How one parrot works."), ('스스로 심부름 목록을 짜요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'It plans its own errands. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
    ],
}
