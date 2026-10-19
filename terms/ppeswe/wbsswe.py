from _draw import *
from _world import *

# 1. "책 한 권 내기"라는 목표만 있고 막막함
P1 = svg(300, sky(300)
         + person(380, 140, s=1.0, face=SWEAT + EYES, **EDITOR)
         + '<rect x="280" y="210" width="200" height="50" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + label(380, 240, "⟦목표: 책 한 권 내기|GOAL: publish one book⟧", 14, "#142033", cls="d")
         + label(380, 30, "⟦목표만 있고, 뭐부터 해야 할지 막막해요|just a goal — and no idea what to do first⟧", 13, "var(--ink)"))

# 2. 큰 덩어리로만 보면 기간/담당을 가늠 못함
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=FROWN, **EDITOR)
         + bubble(100, 70, 240, 44, "⟦'책 만들기'가 얼마나 걸릴지 감이 안 와요|I have no feel for how long 'making a book' even takes⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=SWEAT + EYES, **WRITER)
         + bubble(440, 70, 240, 44, "⟦저 혼자 다 하는 건지, 누가 뭘 맡는지도 몰라요|not even sure who's doing what, or if it's all on me⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦덩어리째로는 기간도 담당도 못 정해요|as one big lump, you can't pin down timing or ownership⟧", 12, "var(--ink)"))

# 3. WBS = 책 만들기를 나뭇가지처럼 작은 작업으로 쪼갠 목록 (hero)
P3 = svg(360, sky(360)
         + '<rect x="320" y="20" width="120" height="36" rx="4" fill="var(--accent)"/>' + label(380, 44, "⟦책 한 권 내기|PUBLISH ONE BOOK⟧", 12, "#142033", cls="d")
         + '<path d="M380 56 V80 M380 80 H180 M380 80 H580 M180 80 V100 M380 80 V100 M580 80 V100" stroke="var(--line)" stroke-width="2" fill="none"/>'
         + manuscript(180, 140, 0.6, text="⟦집필|writing⟧") + '<rect x="140" y="200" width="80" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(180, 220, "⟦1~5장|ch. 1-5⟧", 10, "#142033")
         + '<rect x="340" y="140" width="80" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(380, 160, "⟦교정|proofing⟧", 11, "#142033") + person(380, 200, s=0.5, face=EYES, **PROOFER)
         + printplate(580, 150, 0.9, label_text="⟦인쇄·배본|print and ship⟧")
         + label(380, 320, "⟦더 이상 안 쪼개질 때까지 나눠요|split until each piece can't be split further⟧", 12, "var(--muted)")
         + label(380, 340, "⟦WBS = 큰 목표를 작은 작업들로 나뭇가지처럼 늘어놓은 목록|WBS = the goal laid out as small tasks, branching like a tree⟧", 13, "var(--ink)", cls="d"))

# 4. 트리형 표
P4 = svg(320, sky(320)
         + styleguide(60, 30, 640, 260, "⟦작업분해도(WBS)|WORK BREAKDOWN⟧",
                      ("⟦책 한 권 내기|publish one book⟧",
                       "⟦ㄴ 집필 (1~5장)|└ writing (ch. 1-5)⟧",
                       "⟦ㄴ 교정|└ proofreading⟧",
                       "⟦ㄴ 표지 디자인|└ cover design⟧",
                       "⟦ㄴ 인쇄|└ printing⟧",
                       "⟦ㄴ 배본|└ distribution⟧"), 1.0)
         + label(380, 300, "⟦각 가지에 담당자와 기간을 붙이면 일정표가 돼요|add an owner and a timeline to each branch, and it becomes a schedule⟧", 12, "var(--ink)"))

# 5. 쪼개기만으론 부족, 너무 잘게 쪼개면 오히려 힘듦
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **EDITOR)
         + label(190, 240, "⟦쪼개기만 하고 순서(의존관계)를 안 보면|splitting tasks without looking at order (dependencies)⟧", 11, "var(--ink)")
         + label(190, 265, "⟦교정 전에 인쇄부터 할 수도 있어요|printing could get scheduled before proofing⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **EDITOR)
         + '<rect x="530" y="200" width="30" height="20" rx="2" fill="#FFF8E7" stroke="#C9A86A"/><rect x="565" y="200" width="30" height="20" rx="2" fill="#FFF8E7" stroke="#C9A86A"/><rect x="600" y="200" width="30" height="20" rx="2" fill="#FFF8E7" stroke="#C9A86A"/>'
         + label(570, 240, "⟦너무 잘게 쪼개면 가지가 너무 많아져요|split too finely and there are just too many branches⟧", 11, "var(--ink)")
         + label(380, 282, "⟦쪼개기는 시작일 뿐, 순서와 적당한 크기도 따져야 해요|splitting is just the start — order and the right granularity matter too⟧", 12, "var(--ink)", cls="d"))

TREE_I = icon('<circle cx="32" cy="14" r="6" fill="var(--accent)"/><path d="M32 20 v8 M32 28 h-14 v8 M32 28 h14 v8" stroke="var(--line)" stroke-width="3" fill="none"/><circle cx="18" cy="40" r="5" fill="var(--good)"/><circle cx="46" cy="40" r="5" fill="var(--good)"/>')
LEAF_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M24 32 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
OWNER_I = icon('<circle cx="32" cy="22" r="10" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M16 50 q16 -16 32 0" stroke="var(--line)" stroke-width="3" fill="none"/>')
CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "wbsswe", "order": 29,
    "title": ("책 만들기를 나뭇가지로 늘어놓기", "Laying Out the Book as a Tree"),
    "h1": ("<em>WBS</em>가 뭐예요?", "What is a <em>WBS</em>?"),
    "sub": ("작업분해구조(WBS)를, '책 한 권 내기'라는 큰 목표를 작은 작업들로 쪼개는 출판사 이야기로 풀어봤어요.",
            "The Work Breakdown Structure (WBS), told as a story about a publishing house splitting the goal of 'publish one book' into small tasks."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 '책 한 권 내기'라는 목표판 앞에서 막막해함", "The editor stands before a sign reading 'publish one book', feeling lost"),
         "caption": ("'책 한 권 내기'라는 목표만 있어요.", "There's just the goal: publish one book."),
         "small": ("목표만 있고, 뭐부터 해야 할지 막막해요.", "Just a goal — and no idea what to do first.")},
        {"svg": P2, "alt": ("편집장과 작가가 기간도 담당도 가늠하지 못해 불안해함", "The editor and writer can't gauge timing or ownership, and both look anxious"),
         "caption": ("큰 덩어리로만 보면 기간도 담당도 못 정해요.", "As one big lump, you can't pin down timing or ownership."),
         "small": ("'책 만들기'가 얼마나 걸릴지 감이 안 와요.", "There's no feel for how long 'making a book' even takes.")},
        {"svg": P3, "hero": True, "alt": ("책 한 권 내기라는 목표가 집필·교정·인쇄 배본 가지로 나뭇가지처럼 쪼개짐", "The goal 'publish one book' branches like a tree into writing, proofing, and printing/shipping"),
         "caption": ("WBS는 목표를 나뭇가지처럼 작은 작업으로 늘어놓은 목록이에요.", "A WBS lays the goal out as small tasks, branching like a tree."),
         "small": ("더 이상 안 쪼개질 때까지 나눠요.", "It splits until each piece can't be split further."),
         "tricks": (4, [
             (TREE_I, ("큰 목표를 쪼개기", "Split the big goal"), ("가지를 치듯 나눠요", "branching it apart"), "calm"),
             (LEAF_I, ("작업 단위까지", "Down to a work unit"), ("더는 못 쪼갤 때까지요", "until it can't be split further")),
             (OWNER_I, ("담당자 붙이기", "Assign an owner"), ("가지마다 누가 맡을지요", "who owns each branch")),
             (CHECK_I, ("빠진 일 확인", "Check nothing's missing"), ("가지를 다 세봐요", "counting every branch"), "warm"),
         ])},
        {"svg": P4, "alt": ("책 한 권 내기 아래 집필·교정·표지디자인·인쇄·배본이 나열된 작업분해도", "A work breakdown tree: publish one book, under it writing, proofing, cover design, printing, distribution"),
         "caption": ("가지마다 담당자와 기간을 붙이면 일정표가 돼요.", "Add an owner and a timeline to each branch, and it becomes a schedule."),
         "small": ("이게 WBS 예요 — 작업을 눈에 보이게 늘어놓은 목록.", "This is a WBS — the tasks laid out where everyone can see them.")},
        {"svg": P5, "alt": ("왼쪽: 순서를 안 봐서 인쇄가 교정보다 먼저 잡힘. 오른쪽: 너무 잘게 쪼개 가지가 너무 많아짐", "Left: ignoring order lets printing get scheduled before proofing. Right: splitting too finely leaves too many branches"),
         "caption": ("쪼개기만 하고 순서를 안 보면 꼬여요.", "Split without looking at order, and things get tangled."),
         "small": ("쪼개기는 시작일 뿐, 순서와 적당한 크기도 따져야 해요.", "Splitting is just the start — order and the right granularity matter too.")},
    ],
    "summary": (("<b>WBS(작업분해구조)</b>는 큰 목표를 <b>작업 단위로 쪼개</b> 나뭇가지처럼 늘어놓아, 누가·언제·무엇을 할지 보이게 만드는 목록이에요.",
                 "A <b>WBS (Work Breakdown Structure)</b> splits a big goal into <b>task-sized pieces</b>, laid out like a tree, so who does what and when becomes visible."),
                ("WBS는 프로젝트의 전체 범위를 계층적으로 더 작은 작업 단위(Work Package)로 분해한 구조도예요. 최상위에 프로젝트 목표를 두고, 더 이상 쪼갤 필요가 없는 수준까지 하위 작업으로 나눠요. 이렇게 만들어진 작업 단위에 일정·담당자·비용을 배정해 일정관리(WBS→간트차트)와 원가관리의 토대로 삼아요.",
                 "A WBS hierarchically decomposes a project's full scope into smaller work packages. The project goal sits at the top, broken down into sub-tasks until each is small enough that it needs no further splitting. Schedule, owner, and cost get assigned to each resulting work package, forming the basis for schedule management (WBS feeding into a Gantt chart) and cost management.")),
    "glossary": [
        ("WBS", "WBS", ("책 만들기를 나뭇가지로 늘어놓은 목록.", "The goal laid out as a tree of tasks."), ("프로젝트 범위를 눈에 보이게 해요.", "Makes the full project scope visible.")),
        ("작업 패키지", "Work Package", ("더 이상 안 쪼개지는 가장 작은 가지.", "The smallest branch that needs no further splitting."), ("여기에 담당자와 기간이 붙어요.", "This is where an owner and timeline attach.")),
        ("간트차트", "Gantt Chart", ("가지마다 기간을 막대로 그린 그림.", "Bars drawn for each branch's timeline."), ("WBS에 일정을 입힌 그림이에요.", "A WBS with a schedule drawn on top.")),
        ("의존관계", "Dependency", ("교정이 끝나야 인쇄가 시작되는 순서.", "Printing can't start until proofing is done."), ("쪼개기만으론 안 보이는 부분이에요.", "Something splitting alone doesn't reveal.")),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("WBS가 제대로 지켜지는지 바깥에서 점검.", "Checking from the outside that the WBS is actually followed."), ('WBS를 포함해 여러 프로젝트를 점검해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Checks the WBS along with everything else, across projects. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("기능점수(FP)", "Function Point", ("매수 계산 자로 규모를 먼저 재기.", "Gauging size first with the measuring ruler."), ("WBS로 쪼개기 전에 규모를 가늠하기도 해요.", "Size is sometimes gauged before the WBS split even begins.")),
        ("기술부채", "Technical Debt", ("일정에 쫓겨 나중으로 미룬 빚.", "A debt postponed under schedule pressure."), ('WBS로 일정을 못 맞추면 생기기 쉬워요. → <a href="techdebt-ko.html">지금 빨리 가려고 쌓아둔 빚</a>', 'Easy to accumulate when the WBS schedule slips. → <a href="techdebt-en.html">the debt you pile up to move fast now</a>')),
        ("SLA", "SLA", ("관객에게 보장한 약속.", "The promise made to the audience."), ("WBS의 기간이 지켜질 때 이 약속도 지켜져요.", "Keeping the WBS timeline is what keeps this promise.")),
    ],
}
