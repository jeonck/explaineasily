"""관계 무결성 제약(Referential Integrity Constraint)."""
from _draw import *
from _world import *

EXIST_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M38 38 l5 5 l8 -10" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CASCADE_I = icon('<rect x="8" y="12" width="20" height="18" rx="3" fill="var(--accent)"/><rect x="36" y="12" width="20" height="18" rx="3" fill="var(--bad)"/><path d="M28 21 h8" stroke="var(--muted)" stroke-width="3"/><path d="M8 40 h20 M36 40 h20" stroke="var(--bad)" stroke-width="3" stroke-dasharray="3 3"/>')
RESTRICT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M18 18 L46 46" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
NULL_I = icon('<rect x="14" y="20" width="36" height="24" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3" stroke-dasharray="4 3"/>')

# 1. 반장 명단에 없는 이름이 있어요
P1 = svg(300, sky(300)
         + rulesboard(60, 40, 300, 220, "⟦학생 명부|STUDENT ROSTER⟧", ("⟦1반 김하나|class 1: Kim Hana⟧", "⟦2반 이두리|class 2: Lee Duri⟧", "⟦3반 박세찬|class 3: Park Sechan⟧"), 0.95)
         + rulesboard(400, 40, 300, 220, "⟦반장 명단|CLASS PRESIDENTS⟧", ("⟦1반 — 김하나|class 1 — Kim Hana⟧", "⟦2반 — 이두리|class 2 — Lee Duri⟧", "⟦4반 — 최노을?|class 4 — Choi Noeul?⟧"), 0.95, hl=2)
         + label(380, 280, "⟦반장 명단에 학생 명부엔 없는 이름이 있어요|a name on the president list isn't on the roster at all⟧", 13, "var(--ink)", cls="d"))

# 2. 없는 사람이 반장이면 나중에 꼬여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT + EYES, **TEACHER) + bubble(120, 70, 230, 44, "⟦최노을이 누구죠? 출석부에 없는데요|who's Choi Noeul? not on the attendance list⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=FROWN, **REP) + bubble(470, 70, 230, 44, "⟦전학 간 학생을 못 지웠나 봐요|guess we forgot to remove a transferred student⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦존재하지 않는 학생이 반장으로 등록되면 확인할 때 꼬여요|a president who doesn't exist anymore makes checking a mess⟧", 12, "var(--ink)", cls="d"))

# 3. 관계 무결성 제약 = 원본 명부에 있는 이름만 반장 명단에 쓸 수 있다는 규칙 (hero)
P3 = svg(340, sky(340)
         + rulesboard(50, 40, 280, 240, "⟦학생 명부(원본)|STUDENT ROSTER (ORIGINAL)⟧", ("⟦1반 김하나|class 1: Kim Hana⟧", "⟦2반 이두리|class 2: Lee Duri⟧", "⟦3반 박세찬|class 3: Park Sechan⟧"), 1.0)
         + '<path d="M340 160 H420" stroke="var(--good)" stroke-width="4"/><path d="M414 152 l10 8 l-10 8" fill="none" stroke="var(--good)" stroke-width="3"/>'
         + rulesboard(430, 40, 280, 240, "⟦반장 명단(참조)|CLASS PRESIDENTS (REFERS TO IT)⟧", ("⟦1반 — 김하나 ✓|class 1 — Kim Hana ✓⟧", "⟦2반 — 이두리 ✓|class 2 — Lee Duri ✓⟧", "⟦3반 — 박세찬 ✓|class 3 — Park Sechan ✓⟧"), 1.0)
         + label(380, 300, "⟦관계 무결성 = 원본에 있는 이름만 참조 명단에 쓸 수 있다는 규칙|referential integrity = you may only list a name the original roster actually has⟧", 12, "var(--ink)", cls="d")
         + label(380, 325, "⟦없는 이름을 적으려 하면 아예 등록이 막혀요|trying to write a name that doesn't exist gets blocked outright⟧", 11, "var(--muted)"))

# 4. 원본 학생이 사라지면? 세 가지 선택
P4 = svg(320, sky(320, ground=False)
         + rulesboard(60, 30, 640, 260, "⟦원본에서 학생이 전학 가면, 참조 명단은?|if a student transfers out of the roster, what happens to the list that refers to them?⟧",
                      ("⟦CASCADE — 반장 명단에서도 같이 지움|CASCADE — removed from the president list too⟧",
                       "⟦RESTRICT — 반장부터 내려야 전학 처리 가능|RESTRICT — must step down as president before transferring⟧",
                       "⟦SET NULL — 반장 칸을 빈칸으로 둠|SET NULL — leave the president slot blank⟧"), 1.0)
         + label(380, 305, "⟦상황에 맞게 세 옵션 중 하나를 미리 정해둬요|one of these three options is chosen ahead of time, to fit the situation⟧", 11, "var(--ink)", cls="d"))

# 5. 너무 엄격하면 불편해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **TEACHER) + label(190, 250, "⟦이름이 꼭 맞는지 늘 확인해요|always checks the name actually matches⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **REP) + label(570, 250, "⟦반장부터 내려야 전학 가게 해줘서 번거로워요|had to step down as president before transferring — a hassle⟧", 11, "var(--ink)")
         + label(380, 285, "⟦너무 엄격한 규칙(RESTRICT)은 평소 일 처리를 불편하게 만들 수 있어요|too strict a rule can make everyday business clunky⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "refintegrity", "order": 9,
    "title": ("출석부에 없는 이름은 반장이 될 수 없어요", "No Name on the Roster, No Class President"),
    "h1": ("<em>관계 무결성 제약</em>이 뭐예요?", "What is a <em>Referential Integrity Constraint</em>?"),
    "sub": ("관계 무결성 제약을, 학생 명부에 있는 이름만 반장 명단에 쓸 수 있다는 학생회 규칙 이야기로 풀어봤어요.",
            "Referential integrity constraints, told as a story about the student council's rule that only a name on the roster can go on the president list."),
    "panels": [
        {"svg": P1, "alt": ("학생 명부에는 없는 이름이 반장 명단 4반에 적혀 있음", "A name on the class-4 president list doesn't appear on the student roster at all"),
         "caption": ("반장 명단에 학생 명부엔 없는 이름이 있어요.", "A name on the president list isn't on the roster at all."),
         "small": ("원본에 없는 이름을 참조 명단에 적어버린 거예요.", "A name that isn't in the original got written into the list that refers to it.")},
        {"svg": P2, "alt": ("선생님이 출석부에 없는 이름을 묻고, 대표는 전학 간 학생을 못 지웠다고 답함", "A teacher asks about a name missing from attendance; a rep admits they forgot to remove a transferred student"),
         "caption": ("없는 사람이 반장이면 나중에 꼬여요.", "A president who doesn't exist makes things tangled later."),
         "small": ("존재하지 않는 학생이 반장으로 등록되면 확인할 때 꼬여요.", "A nonexistent student registered as president makes checking a mess.")},
        {"svg": P3, "hero": True, "alt": ("학생 명부(원본)에서 화살표가 반장 명단(참조)으로 이어지고, 명단의 모든 이름에 체크 표시가 있음", "An arrow runs from the student roster (original) to the president list (which refers to it), and every name on the list is checked off"),
         "caption": ("관계 무결성은 원본에 있는 이름만 참조 명단에 쓸 수 있다는 규칙이에요.", "Referential integrity is the rule that only a name the original roster actually has may go on the list that refers to it."),
         "small": ("없는 이름을 적으려 하면 아예 등록이 막혀요.", "Trying to write a name that doesn't exist gets blocked outright."),
         "tricks": (4, [
             (EXIST_I, ("원본에 있어야 참조 가능", "Must exist in the original"), ("없는 이름은 못 적어요", "a nonexistent name can't be written"), "calm"),
             (CASCADE_I, ("같이 지우기(CASCADE)", "Delete together (CASCADE)"), ("원본이 사라지면 참조도 지워요", "when the original goes, so does the reference"), "warm"),
             (RESTRICT_I, ("못 지우게 막기(RESTRICT)", "Block the delete (RESTRICT)"), ("참조가 있으면 못 지워요", "can't delete while something refers to it")),
             (NULL_I, ("빈 칸 처리(SET NULL)", "Leave it blank (SET NULL)"), ("참조 칸만 비워둬요", "just empties the referring field")),
         ])},
        {"svg": P4, "alt": ("원본 학생이 전학 갈 때 CASCADE·RESTRICT·SET NULL 세 가지 선택지를 보여주는 규칙판", "A rule board showing CASCADE, RESTRICT, and SET NULL as options when a roster student transfers out"),
         "caption": ("원본이 사라지면 세 가지 중 하나를 고를 수 있어요.", "When the original disappears, one of three options is chosen."),
         "small": ("상황에 맞게 세 옵션 중 하나를 미리 정해둬요.", "One of these three options is chosen ahead of time, to fit the situation.")},
        {"svg": P5, "alt": ("왼쪽: 이름이 꼭 맞는지 확인하는 선생님. 오른쪽: 반장부터 내려야 전학 가게 돼 번거로워하는 대표", "Left: a teacher always checking names match. Right: a rep frustrated at having to step down as president before transferring"),
         "caption": ("너무 엄격하면 불편해요.", "Too strict a rule makes things inconvenient."),
         "small": ("너무 엄격한 규칙(RESTRICT)은 평소 일 처리를 불편하게 만들 수 있어요.", "Too strict a rule can make everyday business clunky.")},
    ],
    "summary": (("<b>관계 무결성 제약</b> = 참조하는 자료는 반드시 <b>원본에 실제로 있는 값</b>이어야 한다는 규칙. 원본이 사라질 때 <b>지우거나, 막거나, 비우는</b> 방식을 미리 정해둬요.",
                 "<b>Referential integrity</b> = the rule that anything referencing another table must point to a <b>value that actually exists</b> there. When the original is removed, you decide in advance whether to <b>delete it along, block the delete, or leave it blank</b>."),
                ("관계 무결성 제약은 관계형 데이터베이스에서 외래키(FK)가 반드시 참조 대상 테이블의 기본키(PK)에 실제로 존재하는 값이어야 한다는 제약이에요. 원본 행이 삭제·수정될 때는 CASCADE(함께 삭제/수정), RESTRICT(삭제 자체를 금지), SET NULL(참조 값을 NULL로) 중 하나를 옵션으로 정해 데이터 일관성을 지켜요.",
                 "A referential integrity constraint requires that a foreign key (FK) in a relational database always point to a value that actually exists as a primary key (PK) in the referenced table. When the original row is deleted or updated, one of three options — CASCADE (delete/update together), RESTRICT (block the delete), or SET NULL (clear the reference) — is chosen to preserve data consistency.")),
    "glossary": [
        ("관계 무결성 제약", "Referential Integrity Constraint", ("참조는 원본에 있는 값이어야 한다는 규칙.", "The rule that a reference must point to a value that exists in the original."), ("관계형 데이터베이스의 기본 일관성 규칙이에요.", "A basic consistency rule in relational databases.")),
        ("외래키(FK)", "Foreign Key (FK)", ("다른 명부를 가리키는 칸.", "The field that points to another roster."), ("원본 명부의 기본키를 가리켜야 해요.", "It must point to the original roster's primary key.")),
        ("기본키(PK)", "Primary Key (PK)", ("명부에서 한 사람을 딱 가리키는 번호.", "The ID that points to exactly one person on the roster."), ("외래키가 가리키는 대상이에요.", "This is what a foreign key points to.")),
        ("CASCADE", "CASCADE", ("원본이 사라지면 참조도 같이 지우는 것.", "Deleting the reference whenever the original is removed."), ("자동으로 정리되지만, 의도치 않게 많이 지워질 수도 있어요.", "Cleans up automatically, but can delete more than intended.")),
        ("RESTRICT", "RESTRICT", ("참조가 있으면 원본을 못 지우게 막는 것.", "Blocking deletion of the original while something still refers to it."), ("안전하지만 가끔 불편해요.", "Safe, but sometimes inconvenient.")),
        ("SET NULL", "SET NULL", ("참조 칸만 비워두는 것.", "Just leaving the referring field blank."), ("원본은 지우되 참조 기록은 남겨요.", "Removes the original but keeps the referring record.")),
        ("정규화", "Normalization", ("명부를 한 번만 적도록 나누는 규칙.", "The rule for splitting a roster so each fact is written once."), ('참조 무결성은 정규화된 명부 사이의 규칙이에요. → <a href="normalization-ko.html">한 칸에 한 번만 적는 규칙</a>', 'Referential integrity is a rule between normalized rosters. → <a href="normalization-en.html">the rule of writing it once</a>')),
        ("트랜잭션", "Transaction", ("명부를 바꾸는 작업의 단위.", "The unit of work that changes a roster."), ("제약을 어기면 트랜잭션 전체가 취소돼요.", "Breaking the constraint rolls back the whole transaction.")),
    ],
}
