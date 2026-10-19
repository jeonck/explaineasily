from _draw import *
from _world import *

# 1. 독자마다 원하는 게 다 다름
P1 = svg(300, sky(300)
         + person(160, 150, s=0.75, face=SMILE, **READER) + bubble(60, 70, 180, 40, "⟦재밌으면 좋겠어요|I just want it to be fun⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 150, s=0.75, face=EYES, **READER) + bubble(290, 70, 180, 40, "⟦안 망가졌으면 해요|I want it to not fall apart⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 150, s=0.75, face=EYES, **READER) + bubble(510, 70, 200, 40, "⟦읽기 쉬웠으면 해요|I want it easy to read⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦독자마다 책에게 바라는 게 다 달라요|every reader wants something different from a book⟧", 13, "var(--ink)"))

# 2. 하나만 잘해선 좋은 책이 아님
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(220, 150, 1.1) + label(220, 220, "⟦표지는 예쁜데 내용이 틀려요|pretty cover, wrong content⟧", 12, "var(--bad)")
         + manuscript(540, 150, 1.1) + label(540, 220, "⟦맞는 말인데 너무 어려워요|correct, but way too hard to read⟧", 12, "var(--bad)")
         + label(380, 270, "⟦둘 다 \"좋은 책\"이라고 하긴 어려워요|neither really counts as a \"good book\"⟧", 13, "var(--ink)", cls="d"))

# 3. 좋은 책 = 여러 조건을 같이 갖춤 (hero)
P3 = svg(340, sky(340)
         + person(260, 130, s=0.9, face=SMILE, **READER) + manuscript(440, 150, 1.0)
         + inkstamp(520, 110, 0.8)
         + label(380, 30, "⟦좋은 소프트웨어 = 여러 품질 조건을 같이 갖춘 것|good software = meeting several quality conditions together⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦하나만 뛰어나선 안 돼요, 균형이 핵심이에요|excelling at just one isn't enough — balance is the point⟧", 12, "var(--muted)"))

FUNC_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
RELI_I = icon('<path d="M32 10 L54 22 V40 C54 50 44 58 32 58 C20 58 10 50 10 40 V22 Z" fill="var(--good)"/><path d="M24 32 l6 6 l12 -14" stroke="#FFF8E7" stroke-width="4" fill="none" stroke-linecap="round"/>')
USE_I = icon('<circle cx="32" cy="24" r="12" fill="var(--accent)"/><path d="M16 54 q16 -18 32 0" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')
MAINT_I = icon('<path d="M20 44 L44 20" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/><path d="M38 14 l12 12 l-8 8 l-12 -12z" fill="var(--accent)"/>')

PAGE = {
    "slug": "goodsw", "order": 38,
    "title": ("좋은 책의 조건", "What Makes a Good Book"),
    "h1": ("<em>좋은 소프트웨어</em>의 조건이 뭐예요?", "What Makes <em>Good Software</em>?"),
    "sub": ("예쁘기만 해도, 내용만 꽉 차도 좋은 책은 아니에요 — 여러 조건을 함께 갖춰야 하는 이야기예요.",
            "A book that's only pretty, or only crammed with content, isn't a good book — a story about meeting several conditions together."),
    "panels": [
        {"svg": P1, "alt": ("세 명의 독자가 각각 재미, 안정성, 읽기 쉬움을 바란다고 말함", "Three readers each say they want fun, sturdiness, or ease of reading"),
         "caption": ("독자마다 책에게 바라는 게 다 달라요.", "Every reader wants something different from a book."),
         "small": ("좋은 책은 이 모든 바람에 답해야 해요.", "A good book has to answer all of these at once.")},
        {"svg": P2, "alt": ("왼쪽: 표지는 예쁜데 내용이 틀린 책. 오른쪽: 내용은 맞는데 너무 어려운 책", "Left: a book with a pretty cover but wrong content. Right: a book that's correct but far too hard to read"),
         "caption": ("하나만 잘해서는 좋은 책이 아니에요.", "Excelling at just one thing doesn't make a good book."),
         "small": ("둘 다 \"좋은 책\"이라고 하긴 어려워요.", "Neither really counts as a good book.")},
        {"svg": P3, "hero": True, "alt": ("만족한 독자가 책을 들고 있고, 인쇄 감독이 승인 도장을 들어 품질을 확인함", "A satisfied reader holds the book, and the print supervisor raises an approval stamp to confirm quality"),
         "caption": ("좋은 소프트웨어 = 여러 품질 조건을 같이 갖춘 것이에요.", "Good software means meeting several quality conditions together."),
         "small": ("하나만 뛰어나선 안 돼요, 균형이 핵심이에요.", "Excelling at just one isn't enough — balance is the point."),
         "tricks": (4, [
             (FUNC_I, ("기능성", "Functionality"), ("필요한 내용이 다 있어요", "has all the content it needs"), "calm"),
             (RELI_I, ("신뢰성", "Reliability"), ("오탈자·오류가 적어요", "few errors or typos"), ),
             (USE_I, ("사용성", "Usability"), ("읽기 쉽고 이해가 돼요", "easy to read and follow"), "warm"),
             (MAINT_I, ("유지보수성", "Maintainability"), ("다음 판 고치기가 쉬워요", "easy to revise for the next edition")),
         ])},
        {"svg": svg(340, sky(340)
                     + styleguide(60, 30, 640, 280, "⟦품질 조건 여섯 가지(ISO 25010 비유)|SIX QUALITY CONDITIONS (ISO 25010, as a story)⟧",
                                  ("⟦기능성 — 필요한 내용이 다 있나|functionality — has everything needed?⟧",
                                   "⟦신뢰성 — 오류 없이 버티나|reliability — holds up without error?⟧",
                                   "⟦사용성 — 읽기 쉬운가|usability — easy to read?⟧",
                                   "⟦효율성 — 불필요하게 두껍지 않나|efficiency — not needlessly bloated?⟧",
                                   "⟦유지보수성 — 다음 판 고치기 쉬운가|maintainability — easy to revise?⟧",
                                   "⟦이식성 — 다른 판형으로 옮기기 쉬운가|portability — easy to adapt to other formats?⟧"), 1.0)),
         "alt": ("기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성 여섯 조건을 나열한 점검표", "A checklist listing six conditions: functionality, reliability, usability, efficiency, maintainability, portability"),
         "caption": ("실제로는 여섯 가지 조건이 있어요.", "In practice there are six conditions."),
         "small": ("효율성과 이식성도 좋은 책의 숨은 조건이에요.", "Efficiency and portability are the quieter conditions behind a good book.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
                     + person(190, 150, s=0.8, face=FROWN, **READER) + label(190, 240, "⟦예쁘기만 하면: 내용이 부실해요|only pretty: thin on content⟧", 11, "var(--ink)")
                     + person(570, 150, s=0.8, face=FROWN, **READER) + label(570, 240, "⟦내용만 꽉 차면: 아무도 못 읽어요|only packed: nobody can read it⟧", 11, "var(--ink)")
                     + label(380, 282, "⟦한쪽만 챙기면 결국 둘 다 좋은 책이 아니에요 — 균형이 핵심이에요|favoring just one side still isn't a good book — balance is the point⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 예쁘기만 하면 내용이 부실함. 오른쪽: 내용만 꽉 차면 아무도 못 읽음", "Left: only pretty means thin content. Right: only packed with content means nobody can read it"),
         "caption": ("한쪽으로 치우쳐도 좋은 책은 아니에요.", "Leaning too far either way isn't a good book."),
         "small": ("여섯 조건 사이의 균형이 좋은 소프트웨어의 진짜 조건이에요.", "Balance among the six conditions is what really makes software good.")},
    ],
    "summary": (("<b>좋은 소프트웨어</b> = <b>기능성·신뢰성·사용성·효율성·유지보수성·이식성</b>, 이 여섯 가지 품질 조건을 어느 하나도 놓치지 않고 균형 있게 갖춘 것.",
                 "<b>Good software</b> means meeting all six quality conditions — <b>functionality, reliability, usability, efficiency, maintainability, and portability</b> — in balance, without neglecting any one of them."),
                ("ISO/IEC 25010 같은 소프트웨어 품질 모델은 품질을 여러 특성으로 나누어 정의해요. 기능성(필요한 기능을 제공하는가), 신뢰성(오류 없이 안정적으로 동작하는가), 사용성(사용자가 쉽게 쓸 수 있는가), 효율성(자원을 낭비 없이 쓰는가), 유지보수성(변경이 쉬운가), 이식성(다른 환경으로 옮기기 쉬운가)이 대표적이에요. 좋은 소프트웨어는 이 특성들을 프로젝트 맥락에 맞게 균형 있게 갖춘 것이에요.",
                 "Software quality models like ISO/IEC 25010 break quality down into several characteristics: functionality (does it do what's needed), reliability (does it hold up without error), usability (can users work it easily), efficiency (does it use resources well), maintainability (is it easy to change), and portability (is it easy to move to another environment). Good software balances these characteristics to fit the project's context.")),
    "glossary": [
        ("ISO/IEC 25010", "ISO/IEC 25010", ("품질 조건을 정리해둔 국제 표준.", "The international standard that lays out these quality conditions."), ("여섯 가지 비유의 원조예요.", "The source behind these six conditions.")),
        ("기능성", "Functionality", ("필요한 내용이 다 있는가.", "Whether it has everything that's needed."), ("가장 먼저 눈에 띄는 조건이에요.", "The condition people notice first.")),
        ("신뢰성", "Reliability", ("오류 없이 버티는가.", "Whether it holds up without error."), ("QA/QC가 직접 돌보는 영역이에요.", "The area QA/QC directly looks after.")),
        ("사용성", "Usability", ("읽기 쉽고 이해가 되는가.", "Whether it's easy to read and follow."), ("독자 관점에서 가장 체감이 커요.", "The one readers feel most directly.")),
        ("효율성", "Efficiency", ("불필요하게 두껍지 않은가.", "Whether it isn't needlessly bloated."), ("자원을 아끼는 쪽 조건이에요.", "The condition about not wasting resources.")),
        ("유지보수성", "Maintainability", ("다음 판 고치기가 쉬운가.", "Whether the next edition is easy to revise."), ('결합도/응집도와 바로 연결돼요. → <a href="couplingcohesion-ko.html">챕터가 서로 얼마나 엮여있나</a>', 'Directly tied to coupling and cohesion. → <a href="couplingcohesion-en.html">how tangled the chapters are</a>')),
        ("이식성", "Portability", ("다른 판형으로 옮기기 쉬운가.", "Whether it's easy to adapt to another format."), ("전자책 전환 같은 상황에서 중요해요.", "Matters especially for things like e-book conversion.")),
        ("아키텍처 평가(ATAM/CBAM)", "Architecture Evaluation (ATAM/CBAM)", ("이 조건들의 트레이드오프를 미리 점검.", "Checking the trade-offs among these conditions ahead of time."), ('설계 단계에서 품질 조건을 저울질하는 방법이에요. → <a href="atamcbam-ko.html">출간 전 시나리오 리허설</a>', 'A method for weighing these conditions at design time. → <a href="atamcbam-en.html">scenario rehearsal before publication</a>')),
    ],
}
