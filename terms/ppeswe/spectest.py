from _draw import *
from _world import *

# 1. 모든 경우를 다 검사하려면 평생 걸려요
P1 = svg(300, sky(300)
         + person(380, 130, s=0.85, face=SWEAT, **PROOFER)
         + "".join(manuscript(120 + i * 90, 260, 0.45) for i in range(7))
         + label(380, 30, "⟦나이 칸 하나에도 경우의 수가 수천 가지예요|just one age field has thousands of possible cases⟧", 13, "var(--ink)", cls="d")
         + label(380, 292, "⟦다 검사하려면 교정자가 평생 걸려요|checking every single one would take a lifetime⟧", 12, "var(--bad)"))

# 2. 입력 가짓수는 사실상 무한해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 40, "⟦나이 칸: 몇 살까지 넣을 수 있을까요?|the age field — how many values could go in?⟧", 14, "var(--ink)", cls="d")
         + label(380, 130, "⟦-1, 0, 1, 2 ... 17, 18, 19 ... 199, 200 ...|-1, 0, 1, 2 ... 17, 18, 19 ... 199, 200 ...⟧", 16, "var(--bad)", cls="d")
         + person(380, 190, s=0.6, face=FROWN, **PROOFER)
         + label(380, 280, "⟦하나하나 다 넣어보는 건 애초에 불가능해요|trying every single value just isn't possible⟧", 12, "var(--muted)"))

# 3. 명세기반 테스트설계 = 규칙서만 보고 대표 사례 고르기 (hero)
PART_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 10 V54 M11 32 H53" stroke="var(--accent)" stroke-width="3"/><circle cx="20" cy="20" r="4" fill="var(--good)"/><circle cx="44" cy="44" r="4" fill="var(--good)"/>')
BOUND_I = icon('<path d="M10 32 H54" stroke="var(--muted)" stroke-width="3"/><circle cx="34" cy="32" r="3" fill="#C9A86A"/><circle cx="30" cy="32" r="5" fill="var(--bad)"/><circle cx="38" cy="32" r="5" fill="var(--good)"/>')
TABLE_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M10 28 H54 M10 40 H54 M32 12 V52" stroke="#C9A86A" stroke-width="2"/>')
STATE_I = icon('<circle cx="16" cy="32" r="8" fill="var(--accent)"/><circle cx="48" cy="18" r="8" fill="var(--good)"/><circle cx="48" cy="46" r="8" fill="var(--muted)"/><path d="M23 30 L41 20 M23 34 L41 44" stroke="var(--ink)" stroke-width="2.5" fill="none" marker-end="none"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦명세기반 테스트설계 = 규칙서만 보고 대표 사례를 고르는 것|spec-based test design = picking representative cases from the rulebook alone⟧", 13, "var(--ink)", cls="d")
         + styleguide(60, 70, 260, 170, "⟦작성 규칙서|THE WRITING RULES⟧",
                      ("⟦나이: 0~150|age: 0 to 150⟧", "⟦이름: 1~20자|name: 1 to 20 characters⟧", "⟦등급: A/B/C 중 하나|grade: one of A/B/C⟧"), 1.0)
         + person(500, 160, s=0.8, face=EYES, **PROOFER)
         + manuscript(620, 170, 0.5, marks=0)
         + label(380, 320, "⟦원고를 다 읽지 않고도, 규칙만 보고 적은 수의 대표 사례로 검사해요|without reading the whole manuscript, test with just a few cases picked from the rules⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "spectest", "order": 19,
    "title": ("규칙서만 보고 고르는 대표 사례", "Picking Representative Cases From the Rulebook Alone"),
    "h1": ("<em>명세기반 테스트 설계기법</em>이 뭐예요?", "What are <em>Specification-Based Test Design Techniques</em>?"),
    "sub": ("명세기반 테스트 설계기법을, 원고를 다 읽지 않고도 작성 규칙서만 보고 대표 사례를 골라 검사하는 이야기로 풀어봤어요.",
            "Specification-based test design, told as a story about testing with a handful of representative cases picked from the rulebook, without reading the whole manuscript."),
    "panels": [
        {"svg": P1, "alt": ("교정자가 땀을 흘리며 서 있고, 나이 칸 샘플 원고 일곱 뭉치가 늘어서 있음", "A sweating proofreader stands before seven sample manuscripts for just one age field"),
         "caption": ("모든 경우를 다 검사하려면 평생 걸려요.", "Checking every single case would take a lifetime."),
         "small": ("나이 칸 하나에도 경우의 수가 수천 가지예요.", "Just one age field has thousands of possible values.")},
        {"svg": P2, "alt": ("나이 칸에 넣을 수 있는 값이 -1부터 200까지 끝없이 이어지고, 교정자가 찡그리며 서 있음", "Possible values for an age field stretch endlessly from -1 to 200, while the proofreader frowns"),
         "caption": ("입력 가짓수는 사실상 무한해요.", "The number of possible inputs is practically infinite."),
         "small": ("하나하나 다 넣어보는 건 애초에 불가능해요.", "Trying every single value just isn't possible.")},
        {"svg": P3, "hero": True, "alt": ("작성 규칙서 안내판 옆에서 교정자가 적은 수의 원고만 들고 검사함", "Beside a rulebook sign, the proofreader tests with only a few manuscripts in hand"),
         "caption": ("명세기반 테스트설계는 규칙서만 보고 대표 사례를 고르는 거예요.", "Spec-based test design picks representative cases from the rulebook alone."),
         "small": ("원고를 다 읽지 않고도, 규칙만 보고 적은 수의 대표 사례로 검사해요.", "Without reading the whole manuscript, you test with just a few cases picked from the rules."),
         "tricks": (4, [
             (PART_I, ("동등분할", "Equivalence partitioning"), ("비슷한 것끼리 묶어 하나만 검사해요", "group similar inputs and test just one"), "calm"),
             (BOUND_I, ("경계값분석", "Boundary value analysis"), ("기준선 바로 위아래만 봐요", "check just above and below the line")),
             (TABLE_I, ("결정테이블", "Decision table testing"), ("규칙 조합을 표로 만들어 검사해요", "test rule combinations laid out in a table")),
             (STATE_I, ("상태전이테스트", "State transition testing"), ("이야기 단계가 바뀔 때마다 검사해요", "test every time the story moves to a new stage"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 250, "⟦나이 칸(0~150) 테스트 사례|TEST CASES FOR THE AGE FIELD (0–150)⟧",
                                 ("⟦동등분할: 정상(50), 범위 밖(-1), 범위 밖(200)|partition: normal (50), out of range (-1), out of range (200)⟧",
                                  "⟦경계값: 0, -1, 150, 151 — 선 바로 위아래|boundary: 0, -1, 150, 151 — just either side of the line⟧",
                                  "⟦모든 나이를 다 넣어보지 않아요|not every single age gets tried⟧",
                                  "⟦이 몇 개만으로도 규칙 위반을 대부분 잡아요|just these few catch most rule violations⟧"), 1.0)),
         "alt": ("나이 칸 0~150 규칙에 대한 동등분할·경계값 테스트 사례 목록", "A list of equivalence-partition and boundary-value test cases for the 0–150 age rule"),
         "caption": ("몇 개만 골라도 규칙 위반은 대부분 잡혀요.", "Just a handful of cases catches most rule violations."),
         "small": ("정상 범위 하나, 범위 밖 둘, 경계선 바로 위아래 — 이 정도면 충분해요.", "One normal case, two out-of-range cases, just either side of the boundary — that's usually enough.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.8, face=EYES, **PROOFER) + label(190, 265, "⟦빠르고 적은 사례로 검사해요|fast, with just a few cases⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.8, face=EYES, **WRITER) + label(560, 265, "⟦드문 조합은 놓칠 수 있어요|rare combinations can still slip through⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦규칙서만으로 전부를 잡진 못해요|the rulebook alone doesn't catch everything⟧", 13, "var(--bad)", cls="d")),
         "alt": ("교정자는 빠르고 적은 사례로 검사한다 말하고, 작가는 드문 조합은 놓칠 수 있다고 말함", "The proofreader says testing is fast with few cases; the writer says rare combinations can still slip through"),
         "caption": ("규칙서만으로 전부를 잡진 못해요.", "The rulebook alone doesn't catch everything."),
         "small": ("규칙에 없던 드문 조합은 탐색적 테스트 같은 다른 방법과 함께 봐야 해요.", "Rare combinations the rules never anticipated still need other methods, like exploratory testing, alongside this.")},
    ],
    "summary": (("<b>명세기반 테스트 설계기법</b> = 원고를 전부 읽는 대신, <b>작성 규칙서</b>만 보고 <b>적은 수의 대표 사례</b>를 골라 검사하는 방법.",
                 "<b>Specification-based test design</b> = instead of reading the whole manuscript, picking a <b>small set of representative cases</b> straight from the <b>written rules</b>."),
                ("명세기반(블랙박스) 테스트 설계기법은 내부 코드를 보지 않고 요구사항 명세만으로 테스트 케이스를 만드는 방법이에요. 대표적으로 비슷한 입력을 묶어 하나만 검사하는 동등분할, 경계선 바로 위아래만 검사하는 경계값분석, 조건 조합을 표로 정리하는 결정테이블테스트, 상태 변화마다 검사하는 상태전이테스트가 있어요.",
                 "Specification-based (black-box) test design creates test cases from the requirements spec alone, without looking at the internal code. The main techniques are equivalence partitioning (testing one representative from each group of similar inputs), boundary value analysis (testing just either side of a boundary), decision table testing (laying out condition combinations in a table), and state transition testing (testing at each change of state).")),
    "glossary": [
        ("명세기반테스트", "Specification-Based Testing", ("규칙서만 보고 하는 검사.", "Testing based on the rulebook alone."), ("코드를 안 보고도 할 수 있어요(블랙박스).", "Can be done without looking at the code — black-box.")),
        ("동등분할", "Equivalence Partitioning", ("비슷한 입력끼리 묶는 것.", "Grouping similar inputs together."), ("한 그룹에서 하나만 검사해도 충분해요.", "Testing just one from each group is enough.")),
        ("경계값분석", "Boundary Value Analysis", ("기준선 바로 위아래만 보는 것.", "Checking just either side of the line."), ("실수는 경계에서 가장 많이 나요.", "Mistakes cluster right at the boundary.")),
        ("결정테이블테스트", "Decision Table Testing", ("조건 조합을 표로 만드는 것.", "Laying out condition combinations as a table."), ("조건이 여러 개 얽힐 때 빠뜨리지 않게 해줘요.", "Keeps you from missing a combination when several conditions interact.")),
        ("상태전이테스트", "State Transition Testing", ("이야기 단계가 바뀔 때마다 보는 것.", "Testing every time the story moves to a new stage."), ("예약→확정→취소 같은 흐름에 써요.", "Used for flows like booked → confirmed → canceled.")),
        ("블랙박스테스트", "Black-Box Testing", ("내부를 안 보고 밖에서만 확인하는 것.", "Checking from the outside without seeing the inside."), ("명세기반 기법은 전부 이 범주예요.", "All spec-based techniques fall in this category.")),
        ("테스트케이스", "Test Case", ("고른 대표 사례 하나하나.", "Each representative case that gets picked."), ("입력값과 기대 결과가 한 쌍으로 적혀요.", "Written as a pair: the input and the expected result.")),
        ("탐색적 테스트", "Exploratory Testing", ("규칙서에 없는 것까지 사람이 직접 들여다보는 것.", "A person poking at what the rulebook never anticipated."), ("명세기반 기법이 놓친 드문 조합을 보완해요.", "Fills the gap for rare combinations spec-based techniques miss.")),
    ],
}
