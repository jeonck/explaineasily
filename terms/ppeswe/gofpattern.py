from _draw import *
from _world import *

# 1. 작가마다 복선 까는 법을 처음부터 다시 고민해요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(260, 130, 0.8) + manuscript(360, 150, 0.8) + manuscript(460, 120, 0.8)
         + label(380, 230, "⟦작가마다 복선 까는 법을 처음부터 다시 고민해요|every writer reinvents how to plant a plot twist, from scratch⟧", 12, "var(--bad)")
         + label(380, 280, "⟦이미 많은 책이 풀어낸 문제인데도요|even though many books have already solved this same problem⟧", 13, "var(--ink)"))

# 2. 각자 마음대로 쓰면 되죠, 라는 말에 책마다 구조가 제각각이 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 220, 36, "⟦그냥 각자 마음대로 쓰면 되죠|everyone can just write it their own way⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **PROOFER) + bubble(460, 80, 230, 36, "⟦그럼 책마다 구조가 달라서 헷갈려요|then every book's structure is different and confusing⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦매번 새로 발명하면, 검증되지 않은 채로 쓰게 돼요|reinventing it every time means using something never proven⟧", 12, "var(--ink)"))

# 3. GoF 디자인패턴 = 검증된 글쓰기 공식집 (hero)
P3 = svg(340, sky(340)
         + styleguide(60, 30, 280, 250, "⟦검증된 글쓰기 공식집|PROVEN WRITING FORMULAS⟧",
                      ("⟦생성 — 등장인물을 만드는 법|creational — bringing a character to life⟧",
                       "⟦구조 — 챕터를 엮는 법|structural — weaving chapters together⟧",
                       "⟦행위 — 사건이 퍼지는 법|behavioral — how an event ripples outward⟧"), 1.0)
         + person(500, 150, s=0.9, face=EYES, **WRITER)
         + label(380, 30, "⟦GoF 디자인패턴 = 자주 반복되는 문제마다 검증된 해법을 모아둔 공식집|GoF design patterns = a formula book of proven solutions, one for each commonly repeated problem⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦네 명의 저자(Gang of Four)가 23가지 공식으로 정리했어요|four authors (the Gang of Four) organized them into 23 formulas⟧", 12, "var(--muted)"))

# 4. 세 갈래 공식
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦세 갈래 공식|THREE FAMILIES OF PATTERNS⟧",
                      ("⟦생성 패턴 — 싱글턴, 팩토리 등|creational — singleton, factory, etc.⟧",
                       "⟦구조 패턴 — 어댑터, 데코레이터 등|structural — adapter, decorator, etc.⟧",
                       "⟦행위 패턴 — 옵저버, 전략 등|behavioral — observer, strategy, etc.⟧",
                       "⟦모두 합쳐 23가지 공식|23 formulas in total⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **WRITER)
         + label(560, 250, "⟦공식을 외운다고 좋은 책이 되진 않아요|memorizing formulas alone doesn't make a good book⟧", 11, "var(--muted)")
         + label(380, 300, "⟦맞지 않는 상황에 억지로 끼워 맞추면 오히려 이상해져요|forcing one where it doesn't fit makes things worse, not better⟧", 12, "var(--ink)"))

# 5. 어떤 공식을 쓸지는 여전히 작가의 판단이에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **WRITER) + label(190, 240, "⟦글쓰기가 훨씬 빨라져요|it makes the writing go much faster⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **PROOFER) + manuscript(570, 220, 0.6) + label(570, 270, "⟦어떤 공식을 쓸지는 작가가 판단해야 해요|but choosing which formula to use is still the writer's call⟧", 11, "var(--ink)")
         + label(380, 282, "⟦디자인패턴은 손에 쥔 연장이지, 언제 쓸지는 여전히 작가의 판단이에요|design patterns are tools in hand — knowing when to use them is still the writer's own judgment⟧", 12, "var(--ink)", cls="d"))

FORMULA_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><path d="M22 24 l6 6 l12 -12" stroke="var(--good)" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="M22 42 h20" stroke="#142033" stroke-width="2.5"/>')
CREATE_I = icon('<circle cx="22" cy="22" r="10" fill="var(--accent)"/><circle cx="42" cy="22" r="10" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><circle cx="32" cy="44" r="10" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>')
STRUCTURE_I = icon('<path d="M10 20 h18 v18 h-18z" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><path d="M28 28 h18 v18 h-18z" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/>')
BEHAVIOR_I = icon('<circle cx="32" cy="32" r="8" fill="var(--accent)"/><circle cx="32" cy="32" r="16" fill="none" stroke="var(--accent)" stroke-width="2.5"/><circle cx="32" cy="32" r="24" fill="none" stroke="var(--accent)" stroke-width="2"/>')

PAGE = {
    "slug": "gofpattern", "order": 9,
    "title": ("검증된 글쓰기 공식집", "The Book of Proven Writing Formulas"),
    "h1": ("<em>GoF 디자인패턴</em>이 뭐예요?", "What is a <em>GoF Design Pattern</em>?"),
    "sub": ("GoF 디자인패턴을, 자주 반복되는 글쓰기 문제마다 검증된 해법을 모아둔 출판사의 공식집 이야기로 풀어봤어요.",
            "GoF design patterns, told as a story about a publishing house's formula book — proven solutions collected for each commonly repeated writing problem."),
    "panels": [
        {"svg": P1, "alt": ("작가가 진땀을 흘리며 복선 까는 법을 처음부터 혼자 고민함", "A writer sweats, trying to work out how to plant a plot twist entirely from scratch"),
         "caption": ("작가마다 복선 까는 법을 처음부터 다시 고민해요.", "Every writer reinvents how to plant a plot twist, from scratch."),
         "small": ("이미 많은 책이 풀어낸 문제인데도요.", "Even though many books have already solved this same problem.")},
        {"svg": P2, "alt": ("편집장은 각자 마음대로 쓰라 하고, 교정자는 책마다 구조가 달라 헷갈린다고 말함", "The editor says to write it any way; the proofreader says every book's structure ends up different and confusing"),
         "caption": ("각자 마음대로 쓰면 되죠, 라는 말에 구조가 제각각이 돼요.", "A suggestion to write it any way ends up making every structure different."),
         "small": ("매번 새로 발명하면, 검증되지 않은 채로 쓰게 돼요.", "Reinventing it every time means using something never proven.")},
        {"svg": P3, "hero": True, "alt": ("작가가 검증된 글쓰기 공식집 앞에 서 있음: 생성·구조·행위 세 갈래", "A writer stands before a book of proven writing formulas: creational, structural, behavioral"),
         "caption": ("GoF 디자인패턴은 반복되는 문제마다 검증된 해법을 모은 공식집이에요.", "GoF design patterns are a formula book of proven solutions for repeated problems."),
         "small": ("네 명의 저자(Gang of Four)가 23가지 공식으로 정리했어요.", "Four authors (the Gang of Four) organized them into 23 formulas."),
         "tricks": (4, [
             (FORMULA_I, ("검증된 공식 찾기", "Find a proven formula"), ("이미 풀린 문제인지 먼저 봐요", "checking if the problem's already been solved"), "calm"),
             (CREATE_I, ("등장인물 만드는 법", "How to bring a character to life"), ("생성 패턴이 다뤄요", "handled by creational patterns")),
             (STRUCTURE_I, ("챕터 엮는 법", "How to weave chapters together"), ("구조 패턴이 다뤄요", "handled by structural patterns"), "warm"),
             (BEHAVIOR_I, ("사건이 퍼지는 법", "How an event ripples outward"), ("행위 패턴이 다뤄요", "handled by behavioral patterns")),
         ])},
        {"svg": P4, "alt": ("세 갈래 공식표: 생성·구조·행위 패턴과 총 23가지라는 항목", "A three-family pattern board: creational, structural, behavioral, totaling 23 formulas"),
         "caption": ("공식은 세 갈래로 나뉘어요.", "The formulas split into three families."),
         "small": ("공식을 외운다고 좋은 책이 되진 않아요.", "Memorizing formulas alone doesn't make a good book.")},
        {"svg": P5, "alt": ("왼쪽: 작가가 글쓰기가 훨씬 빨라진다고 말함. 오른쪽: 교정자가 어떤 공식을 쓸지는 작가 몫이라고 말함", "Left: the writer says the writing goes much faster. Right: the proofreader says choosing the formula is still the writer's call"),
         "caption": ("어떤 공식을 쓸지는 여전히 작가의 판단이에요.", "Choosing which formula to use is still the writer's own judgment."),
         "small": ("손에 쥔 연장이지, 언제 쓸지는 작가 몫이에요.", "They're tools in hand — when to use them is still up to the writer.")},
    ],
    "summary": (("<b>GoF 디자인패턴</b> = 자주 반복되는 문제마다 <b>검증된 해법</b>을 모아둔 <b>23가지 공식집</b>.",
                 "<b>GoF design patterns</b> = a <b>book of 23 proven formulas</b>, one for each commonly repeated problem."),
                ("GoF(Gang of Four)는 이 패턴들을 정리한 네 저자를 가리키는 별칭이고, 디자인패턴은 생성(Creational)·구조(Structural)·행위(Behavioral) 세 범주 23가지로 나뉘어요. 각 패턴은 특정 설계 문제에 대해 이름 붙여진 재사용 가능한 해법으로, 패턴 자체를 암기하기보다 어떤 상황에 어떤 패턴이 맞는지 판단하는 능력이 더 중요해요.",
                 "GoF (Gang of Four) refers to the four authors who catalogued these patterns, split into 23 patterns across three categories: creational, structural, and behavioral. Each pattern is a named, reusable solution to a specific design problem — what matters more than memorizing the patterns themselves is judging which one fits a given situation.")),
    "glossary": [
        ("GoF", "Gang of Four", ("공식집을 처음 엮은 네 저자.", "The four authors who first compiled the formula book."), ("23가지 패턴을 정리했어요.", "Catalogued the 23 patterns.")),
        ("생성 패턴", "Creational Patterns", ("등장인물을 만드는 법들.", "Formulas for bringing a character to life."), ("싱글턴, 팩토리 메서드 등이에요.", "Includes singleton, factory method, and more.")),
        ("구조 패턴", "Structural Patterns", ("챕터를 엮는 법들.", "Formulas for weaving chapters together."), ("어댑터, 데코레이터 등이에요.", "Includes adapter, decorator, and more.")),
        ("행위 패턴", "Behavioral Patterns", ("사건이 퍼지는 법들.", "Formulas for how an event ripples outward."), ("옵저버, 전략 등이에요.", "Includes observer, strategy, and more.")),
        ("소프트웨어 아키텍처", "Software Architecture", ("책 전체의 구조 밑그림.", "The structural blueprint for the whole book."), ("디자인패턴보다 훨씬 큰 단위예요.", "A much larger unit than a design pattern.")),
        ("재공학/역공학(3R)", "Reengineering (3R)", ("사라진 원본을 되짚어 다시 짓는 일.", "Tracing a lost original backward to rebuild it."), ('다시 쓸 때 이 공식들을 자주 적용해요. → <a href="reengineering-ko.html">사라진 원본을 되짚어 다시 짓기</a>', 'These formulas are often applied while rewriting. → <a href="reengineering-en.html">tracing back a lost original to rebuild it</a>')),
        ("리팩토링", "Refactoring", ("줄거리는 그대로, 문장 구조만 다듬는 일.", "Keeping the plot but polishing the sentence structure."), ("패턴은 리팩토링의 목적지가 되기도 해요.", "A pattern is often the destination refactoring moves toward.")),
        ("UML 다이어그램", "UML Diagrams", ("쓰기 전에 그려보는 설계 지도.", "The design map drawn before writing."), ('패턴을 그림으로 나타낼 때도 써요. → <a href="umldiagram-ko.html">쓰기 전에 그리는 설계 지도</a>', 'Also used to draw a pattern out visually. → <a href="umldiagram-en.html">the design map drawn before writing</a>')),
    ],
}
