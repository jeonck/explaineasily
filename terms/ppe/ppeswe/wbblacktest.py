from _draw import *
from _world import *

# 1. 겉으로 멀쩡해 보여서 속에 숨은 오류를 놓쳤어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **PROOFER)
         + manuscript(260, 130, 0.8, marks=2) + manuscript(360, 150, 0.8, marks=1) + manuscript(460, 120, 0.8, marks=0)
         + label(380, 230, "⟦겉으로 멀쩡해 보여서 그냥 넘어갔어요|it looked fine on the surface, so it got passed⟧", 12, "var(--bad)")
         + label(380, 280, "⟦속 어딘가에 숨은 오류는 못 봤어요|an error hidden somewhere inside went unseen⟧", 13, "var(--ink)"))

# 2. 안에서 볼지, 밖에서 볼지로 의견이 갈려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **PROOFER)
         + bubble(140, 80, 210, 36, "⟦원고 속 흐름을 다 들여다봐야죠|you have to look inside at the whole flow⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=SMILE, **READER) + bubble(460, 80, 230, 36, "⟦그냥 독자처럼 읽어보면 되잖아요|just read it like a reader would⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦어느 한쪽만 고집하면, 다른 쪽 오류는 못 잡아요|insisting on only one way misses the other kind of error⟧", 12, "var(--ink)"))

# 3. 화이트박스 = 속을 펼쳐 보기, 블랙박스 = 겉만 보고 읽기 (hero)
P3 = svg(340, sky(340)
         + person(230, 140, s=0.85, face=EYES, **PROOFER) + manuscript(230, 260, 0.9, marks=2, text="⟦속을 펼쳐 봐요|looking inside⟧")
         + person(530, 140, s=0.85, face=EYES, **PROOFER) + printplate(530, 260, 0.9, label_text="⟦겉만 보고 읽어요|only from outside⟧")
         + label(380, 30, "⟦화이트박스 = 원고 속 흐름을 보며 교정, 블랙박스 = 겉으로 완성된 책만 읽어보며 교정|white-box = proofing by the manuscript's inner flow, black-box = proofing the finished book from the outside⟧", 12, "var(--ink)", cls="d")
         + label(380, 325, "⟦둘 다 교정자가 하는 일이지만, 보는 자리가 달라요|both are done by the proofreader — just from different vantage points⟧", 12, "var(--muted)"))

# 4. 두 방식을 비교하면
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦화이트박스 vs 블랙박스|WHITE-BOX VS BLACK-BOX⟧",
                      ("⟦화이트박스 — 속 흐름을 따라가며 확인|white-box — checks the inner flow⟧",
                       "⟦블랙박스 — 입력·출력만 보고 확인|black-box — checks only input and output⟧",
                       "⟦경계값 — 처음과 끝을 특히 살펴요|boundary values — start and end get special attention⟧",
                       "⟦동등분할 — 비슷한 경우는 대표로 확인|equivalence partitioning — checking one case per group⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **PROOFER)
         + label(560, 250, "⟦둘 다 완벽하진 않아요, 같이 써야 빈틈이 줄어요|neither alone is perfect — using both closes more gaps⟧", 11, "var(--muted)")
         + label(380, 300, "⟦작은 책일수록 둘 다 해보는 게 어렵지 않아요|the smaller the book, the easier it is to do both⟧", 12, "var(--ink)"))

# 5. 테스트는 오류가 없다는 증거가 아니에요
P5 = svg(340, '<rect width="380" height="340" fill="var(--accent-soft)"/><rect x="380" width="380" height="340" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=EYES, **PROOFER) + label(190, 260, "⟦오류를 많이 잡아줘요|it catches a lot of errors⟧", 11, "var(--ink)")
         + person(570, 110, s=0.8, face=SMILE, **WRITER) + manuscript(570, 200, 0.6) + label(570, 260, "⟦그래도 모든 경우를 다 확인하진 못해요|but it still can't check every single case⟧", 11, "var(--ink)")
         + label(380, 315, "⟦테스트는 오류가 없다는 증거가 아니라, 찾아낸 오류가 있다는 증거예요|testing isn't proof there are no bugs — only proof the bugs it found are real⟧", 12, "var(--ink)", cls="d"))

WHITEBOX_I = icon('<circle cx="32" cy="14" r="6" fill="var(--accent)"/><path d="M32 20 v10 M32 30 l-14 14 M32 30 l14 14" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="18" cy="48" r="6" fill="var(--good)"/><circle cx="46" cy="48" r="6" fill="var(--bad)"/>')
BOUNDARY_I = icon('<rect x="10" y="26" width="44" height="12" rx="2" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="10" cy="32" r="5" fill="var(--bad)"/><circle cx="54" cy="32" r="5" fill="var(--bad)"/>')
BLACKBOX_I = icon('<rect x="14" y="16" width="36" height="32" rx="4" fill="#111C30"/><path d="M4 32 h10 M50 32 h10" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
EQUIV_I = icon('<rect x="8" y="24" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="28" y="24" width="16" height="16" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/><rect x="48" y="24" width="10" height="16" fill="var(--bad-soft)" stroke="var(--bad)" stroke-width="2"/>')

PAGE = {
    "slug": "wbblacktest", "order": 5,
    "title": ("속을 펼쳐 볼지, 겉만 읽을지", "Looking Inside, or Just Reading the Outside"),
    "h1": ("<em>화이트박스/블랙박스 테스트</em>가 뭐예요?", "What is <em>White-box/Black-box Testing</em>?"),
    "sub": ("화이트박스와 블랙박스 테스트를, 교정자가 원고 속 흐름을 펼쳐 보는지 아니면 완성된 책만 독자처럼 읽어보는지로 풀어봤어요.",
            "White-box and black-box testing, told through whether the proofreader opens up the manuscript's inner flow, or just reads the finished book like a reader."),
    "panels": [
        {"svg": P1, "alt": ("교정자가 진땀을 흘리며 원고를 보지만, 겉으로 멀쩡해 보이는 원고 속에 오류가 숨어 있음", "A proofreader sweats over manuscripts that look fine on the surface but hide errors inside"),
         "caption": ("겉으로 멀쩡해 보여서 그냥 넘어갔어요.", "It looked fine on the surface, so it got passed."),
         "small": ("속 어딘가에 숨은 오류는 못 봤어요.", "An error hidden somewhere inside went unseen.")},
        {"svg": P2, "alt": ("한 교정자는 속 흐름을 봐야 한다고, 다른 독자는 그냥 읽어보면 된다고 말함", "One proofreader says you must look at the inner flow; a reader says just read it"),
         "caption": ("안에서 볼지, 밖에서 볼지로 의견이 갈려요.", "Opinions split on whether to look from inside or outside."),
         "small": ("어느 한쪽만 고집하면, 다른 쪽 오류는 못 잡아요.", "Insisting on only one way misses the other kind of error.")},
        {"svg": P3, "hero": True, "alt": ("한 교정자는 원고를 펼쳐 속 흐름을 보고, 다른 교정자는 완성된 책 겉만 보고 읽음", "One proofreader opens the manuscript to see the inner flow; another reads only the finished book's outside"),
         "caption": ("화이트박스는 속을 펼쳐 보고, 블랙박스는 겉만 보고 읽어요.", "White-box opens it up to look inside; black-box just reads from the outside."),
         "small": ("둘 다 교정자가 하는 일이지만, 보는 자리가 달라요.", "Both are done by the proofreader — just from different vantage points."),
         "tricks": (4, [
             (WHITEBOX_I, ("속 흐름 따라가기", "Follow the inner flow"), ("갈라지는 길마다 확인해요", "checking every fork in the path"), "calm"),
             (BOUNDARY_I, ("경계값 살펴보기", "Check boundary values"), ("처음과 끝을 특히 봐요", "watching the start and end closely")),
             (BLACKBOX_I, ("입력·출력만 보기", "Watch only input/output"), ("속은 안 들여다봐요", "without peeking inside"), "warm"),
             (EQUIV_I, ("비슷한 경우 묶기", "Group similar cases"), ("대표 하나만 확인해요", "checking one representative case")),
         ])},
        {"svg": P4, "alt": ("비교표: 화이트박스·블랙박스·경계값·동등분할 네 항목", "A comparison board: white-box, black-box, boundary values, equivalence partitioning"),
         "caption": ("두 방식을 이렇게 비교할 수 있어요.", "The two approaches compare like this."),
         "small": ("둘 다 완벽하진 않아요, 같이 써야 빈틈이 줄어요.", "Neither alone is perfect — using both closes more gaps.")},
        {"svg": P5, "alt": ("왼쪽: 교정자가 오류를 많이 잡는다고 말함. 오른쪽: 작가가 모든 경우를 다 확인하진 못한다고 말함", "Left: the proofreader says it catches a lot of errors. Right: the writer says it still can't check every case"),
         "caption": ("테스트는 오류가 없다는 증거가 아니에요.", "Testing isn't proof there are no bugs."),
         "small": ("찾아낸 오류가 있다는 증거일 뿐이에요.", "It's only proof that the bugs it found are real.")},
    ],
    "summary": (("<b>화이트박스/블랙박스 테스트</b> = 원고 <b>속 흐름을 보며</b> 확인할지, <b>겉으로 완성된 책만 보며</b> 확인할지의 차이.",
                 "<b>White-box/black-box testing</b> = whether you check by looking at the manuscript's <b>inner flow</b>, or only at the <b>finished book from outside</b>."),
                ("화이트박스 테스트는 소스 코드의 내부 구조(분기, 반복문 등)를 알고 그 경로를 따라가며 검증하는 방식이고, 블랙박스 테스트는 내부 구조를 모른 채 입력과 출력만으로 기능을 검증하는 방식이에요. 경계값 분석과 동등분할은 대표적인 블랙박스 기법이고, 구문·결정·조건 커버리지는 대표적인 화이트박스 기법이에요.",
                 "White-box testing verifies code by knowing its internal structure (branches, loops) and tracing those paths, while black-box testing verifies functionality using only input and output, without knowing the internals. Boundary value analysis and equivalence partitioning are classic black-box techniques; statement, decision, and condition coverage are classic white-box ones.")),
    "glossary": [
        ("화이트박스 테스트", "White-box Testing", ("원고 속 흐름을 보며 하는 교정.", "Proofing by looking at the manuscript's inner flow."), ("코드의 분기·경로를 따라가요.", "Traces the code's branches and paths.")),
        ("블랙박스 테스트", "Black-box Testing", ("완성된 책만 보고 하는 교정.", "Proofing only the finished book."), ("입력과 출력만으로 확인해요.", "Checks using only input and output.")),
        ("경계값 분석", "Boundary Value Analysis", ("처음과 끝 지점을 특히 살피는 법.", "Watching the start and end points closely."), ("오류는 경계에서 자주 생겨요.", "Errors often show up right at the edge.")),
        ("동등분할", "Equivalence Partitioning", ("비슷한 경우를 묶어 대표로 확인하는 법.", "Grouping similar cases and checking one."), ("모든 경우를 다 볼 순 없으니까요.", "Because you can't check every single case.")),
        ("단위/통합/시스템 테스트", "Unit/Integration/System Testing", ("챕터 하나부터 책 전체까지, 범위별 검사.", "Checks scoped from one chapter up to the whole book."), ("범위가 넓어질수록 늦게 해요.", "The wider the scope, the later it happens.")),
        ("요구공학", "Requirements Engineering", ("무엇이 맞는 답인지 미리 정해두는 일.", "Deciding beforehand what counts as correct."), ('테스트의 기준은 결국 명세서에서 와요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', "The test's own standard ultimately comes from the spec. → <a href=\"reqeng-en.html\">the one who asks before writing</a>")),
        ("회귀 테스트", "Regression Testing", ("고친 뒤에 예전 부분도 다시 확인하는 일.", "Rechecking the old parts after a fix."), ("고치다가 다른 곳을 깨뜨릴 수 있어요.", "A fix can break something else.")),
        ("커버리지", "Coverage", ("원고 속 길을 얼마나 지나가 봤는지 비율.", "The share of the manuscript's paths actually walked."), ("100%여도 오류가 없다는 뜻은 아니에요.", "Even 100% doesn't mean there are no bugs.")),
    ],
}
