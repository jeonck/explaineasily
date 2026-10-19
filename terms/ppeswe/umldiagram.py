from _draw import *
from _world import *

# 1. 설계 지도 없이 쓰다가 등장인물 관계가 꼬였어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(260, 130, 0.8, marks=3) + manuscript(380, 150, 0.8, marks=2) + manuscript(480, 120, 0.8, marks=1)
         + label(380, 230, "⟦설계 지도 없이 바로 쓰다가 등장인물 관계가 꼬였어요|writing straight in without a map, the characters' relationships got tangled⟧", 12, "var(--bad)")
         + label(380, 280, "⟦누가 누구의 형제인지 뒤늦게 헷갈렸어요|it got confusing, too late, who was whose sibling⟧", 13, "var(--ink)"))

# 2. 그냥 쓰라는 말, 그림 없인 설명 못 한다는 반박
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 220, 36, "⟦그림 그릴 시간에 그냥 쓰세요|spend that drawing time just writing instead⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **WRITER) + bubble(460, 80, 230, 36, "⟦그림 없인 이 구조를 설명 못 해요|without a diagram I can't explain this structure⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦말로만 설명하면, 다른 사람은 같은 그림을 못 떠올려요|explained only in words, no one else pictures the same thing⟧", 12, "var(--ink)"))

# 3. UML 다이어그램 = 쓰기 전에 그려보는 설계 지도 (hero)
P3 = svg(340, sky(340)
         + styleguide(60, 30, 280, 250, "⟦쓰기 전 설계 지도|THE MAP DRAWN BEFORE WRITING⟧",
                      ("⟦관계도 — 등장인물들 사이 관계|relationship map — how characters relate⟧",
                       "⟦순서도 — 사건이 일어나는 차례|sequence — the order events happen in⟧",
                       "⟦할 일 목록 — 독자가 할 수 있는 일|use-case list — what readers can do⟧"), 1.0)
         + person(500, 150, s=0.9, face=EYES, **WRITER)
         + label(380, 30, "⟦UML 다이어그램 = 쓰기 전에 구조를 그림으로 미리 그려보는 설계 지도|UML diagrams = a design map that draws out the structure in pictures, before writing begins⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦약속된 그림 기호로, 말로 설명하기 어려운 구조를 또렷하게 보여줘요|using agreed-upon symbols to show clearly a structure that's hard to explain in words⟧", 12, "var(--muted)"))

# 4. 자주 쓰는 UML 세 가지
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦자주 쓰는 UML 세 가지|THREE COMMON UML DIAGRAMS⟧",
                      ("⟦클래스 다이어그램 — 등장인물 관계도|class diagram — character relationship map⟧",
                       "⟦시퀀스 다이어그램 — 사건이 일어나는 순서|sequence diagram — the order events happen in⟧",
                       "⟦유스케이스 다이어그램 — 독자가 할 수 있는 일|use-case diagram — what readers can do⟧",
                       "⟦상태 다이어그램 — 마음이 바뀌는 과정|state diagram — how a character's state changes⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **WRITER)
         + label(560, 250, "⟦그림마다 보여주려는 게 달라요, 하나로 다 담진 않아요|each diagram shows something different — no single one covers it all⟧", 11, "var(--muted)")
         + label(380, 300, "⟦그림을 그렸다고 저절로 좋은 구조가 되진 않아요|drawing the diagram doesn't automatically make the structure good⟧", 12, "var(--ink)"))

# 5. 지도를 그렸다고 책이 저절로 써지진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **WRITER) + label(190, 240, "⟦구조를 또렷하게 보여줘요|it shows the structure clearly⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **EDITOR) + manuscript(570, 220, 0.6) + label(570, 270, "⟦그래도 실제로 쓰는 건 작가 몫이에요|but actually writing it is still up to the writer⟧", 11, "var(--ink)")
         + label(380, 282, "⟦UML은 쓰기 전 지도일 뿐, 지도를 그렸다고 책이 저절로 써지진 않아요|UML is just the map drawn before writing — drawing it doesn't write the book for you⟧", 12, "var(--ink)", cls="d"))

RELATION_I = icon('<rect x="8" y="14" width="18" height="16" rx="2" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="38" y="34" width="18" height="16" rx="2" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/><path d="M26 22 l12 20" stroke="var(--ink)" stroke-width="2"/>')
SEQUENCE_I = icon('<path d="M14 10 v44 M50 10 v44" stroke="var(--muted)" stroke-width="2"/><path d="M14 22 h36" stroke="var(--accent)" stroke-width="3"/><path d="M50 36 h-36" stroke="var(--good)" stroke-width="3"/>')
USECASE_I = icon('<circle cx="18" cy="32" r="9" fill="var(--accent)"/><path d="M12 48 q6 -10 12 0" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="44" cy="32" rx="16" ry="11" fill="none" stroke="var(--good)" stroke-width="3"/>')
STATE_I = icon('<circle cx="16" cy="32" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="48" cy="32" r="10" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M26 32 h12" stroke="var(--ink)" stroke-width="3"/>')

PAGE = {
    "slug": "umldiagram", "order": 11,
    "title": ("쓰기 전에 그리는 설계 지도", "The Design Map Drawn Before Writing"),
    "h1": ("<em>UML 다이어그램 작성</em>이 뭐예요?", "What is <em>Writing UML Diagrams</em>?"),
    "sub": ("UML 다이어그램을, 책을 쓰기 전에 등장인물 관계도·사건 순서도·독자가 할 수 있는 일 목록을 미리 그려보는 설계 지도 이야기로 풀어봤어요.",
            "UML diagrams, told as a story about drawing a design map before writing a book — a character relationship map, a sequence of events, a list of what readers can do."),
    "panels": [
        {"svg": P1, "alt": ("작가가 설계 지도 없이 바로 써서, 등장인물 관계가 꼬여버린 원고들", "A writer writes straight in without a design map, and the manuscripts end up with tangled character relationships"),
         "caption": ("설계 지도 없이 바로 쓰다가 등장인물 관계가 꼬였어요.", "Writing straight in without a map, the characters' relationships got tangled."),
         "small": ("누가 누구의 형제인지 뒤늦게 헷갈렸어요.", "It got confusing, too late, who was whose sibling.")},
        {"svg": P2, "alt": ("편집장은 그림 그릴 시간에 그냥 쓰라 하고, 작가는 그림 없인 설명 못 한다고 반박함", "The editor says to spend that drawing time writing instead; the writer says a diagram is needed to explain it"),
         "caption": ("그냥 쓰라는 말, 그림 없인 설명 못 한다는 반박.", "A push to just write, met with the fact that a diagram is needed to explain it."),
         "small": ("말로만 설명하면, 다른 사람은 같은 그림을 못 떠올려요.", "Explained only in words, no one else pictures the same thing.")},
        {"svg": P3, "hero": True, "alt": ("작가가 관계도·순서도·할 일 목록이 적힌 설계 지도 안내판 앞에 섬", "A writer stands by a design-map board listing relationship map, sequence, and use-case list"),
         "caption": ("UML 다이어그램은 쓰기 전에 그려보는 설계 지도예요.", "UML diagrams are the design map drawn before writing."),
         "small": ("약속된 그림 기호로, 말로 설명하기 어려운 구조를 또렷하게 보여줘요.", "Agreed-upon symbols show clearly a structure that's hard to explain in words."),
         "tricks": (4, [
             (RELATION_I, ("관계 그려보기", "Draw out the relationships"), ("등장인물들 사이를 선으로 이어요", "connecting characters with lines"), "calm"),
             (SEQUENCE_I, ("순서 그려보기", "Draw out the sequence"), ("사건이 일어나는 차례를 보여요", "showing the order events happen in")),
             (USECASE_I, ("할 일 목록 그려보기", "Draw out the use cases"), ("독자가 할 수 있는 일을 늘어놔요", "laying out what readers can do"), "warm"),
             (STATE_I, ("마음 변화 그려보기", "Draw out the state changes"), ("바뀌는 과정을 보여요", "showing how it changes over time")),
         ])},
        {"svg": P4, "alt": ("UML 세 가지 비교표: 클래스·시퀀스·유스케이스·상태 다이어그램 네 항목", "A comparison board of UML types: class, sequence, use-case, state diagrams"),
         "caption": ("자주 쓰는 UML에는 이런 종류가 있어요.", "These are the commonly used kinds of UML diagrams."),
         "small": ("그림마다 보여주려는 게 달라요, 하나로 다 담진 않아요.", "Each diagram shows something different — no single one covers it all.")},
        {"svg": P5, "alt": ("왼쪽: 작가가 구조를 또렷하게 보여준다고 말함. 오른쪽: 편집장이 그래도 쓰는 건 작가 몫이라고 말함", "Left: the writer says it shows the structure clearly. Right: the editor says writing it is still up to the writer"),
         "caption": ("지도를 그렸다고 책이 저절로 써지진 않아요.", "Drawing the map doesn't write the book for you."),
         "small": ("UML은 쓰기 전 지도일 뿐이에요.", "UML is just the map drawn before writing.")},
    ],
    "summary": (("<b>UML 다이어그램</b> = 쓰기 전에 <b>구조를 그림으로</b> 미리 그려보는 <b>약속된 설계 지도</b>.",
                 "<b>UML diagrams</b> = an <b>agreed-upon design map</b> that draws out the structure <b>in pictures</b>, before writing begins."),
                ("UML(Unified Modeling Language)은 소프트웨어 구조와 동작을 표준화된 기호로 표현하는 모델링 언어예요. 클래스 다이어그램은 구성요소 사이의 정적 관계를, 시퀀스 다이어그램은 시간 순서에 따른 상호작용을, 유스케이스 다이어그램은 사용자가 시스템으로 할 수 있는 일을, 상태 다이어그램은 객체 상태 변화를 보여줘요. 코드를 짜기 전 설계를 공유하고 검토하는 데 쓰여요.",
                 "UML (Unified Modeling Language) is a modeling language that expresses software structure and behavior through standardized symbols. A class diagram shows static relationships between components, a sequence diagram shows interactions over time, a use-case diagram shows what a user can do with the system, and a state diagram shows how an object's state changes. It's used to share and review a design before any code is written.")),
    "glossary": [
        ("UML", "UML", ("약속된 그림 기호 체계.", "The agreed-upon system of diagram symbols."), ("구조와 동작을 표준화된 기호로 그려요.", "Draws structure and behavior in standardized symbols.")),
        ("클래스 다이어그램", "Class Diagram", ("등장인물들 사이 관계도.", "The relationship map between characters."), ("정적인 구조를 보여줘요.", "Shows the static structure.")),
        ("시퀀스 다이어그램", "Sequence Diagram", ("사건이 일어나는 순서도.", "The order events happen in."), ("시간 흐름에 따른 상호작용이에요.", "Shows interaction over time.")),
        ("유스케이스 다이어그램", "Use-case Diagram", ("독자가 할 수 있는 일 목록.", "The list of what readers can do."), ("사용자 관점에서 기능을 나열해요.", "Lists functions from the user's point of view.")),
        ("상태 다이어그램", "State Diagram", ("마음이 바뀌는 과정을 보여주는 그림.", "A diagram showing how a character's state changes."), ("객체의 상태 변화를 추적해요.", "Tracks how an object's state changes.")),
        ("요구공학", "Requirements Engineering", ("쓰기 전에 먼저 묻는 일.", "Asking before writing."), ('개요서를 그림으로 더 또렷하게 만들 때도 UML을 써요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', 'UML also makes the outline even clearer, in picture form. → <a href="reqeng-en.html">the one who asks before writing</a>')),
        ("GoF 디자인패턴", "GoF Design Patterns", ("검증된 글쓰기 공식집.", "The book of proven writing formulas."), ('패턴을 그림으로 나타낼 때 클래스 다이어그램을 써요. → <a href="gofpattern-ko.html">검증된 글쓰기 공식집</a>', 'A class diagram is used to draw a pattern out visually. → <a href="gofpattern-en.html">the book of proven writing formulas</a>')),
        ("소프트웨어 아키텍처 모델", "Software Architecture Model", ("책 전체를 미리 짜 두는 구조 밑그림.", "The structural blueprint for the whole book, drawn ahead of time."), ("더 큰 구조를 그릴 때도 UML 표기법을 빌려 써요.", "Borrows UML notation even when drawing a much larger structure.")),
    ],
}
