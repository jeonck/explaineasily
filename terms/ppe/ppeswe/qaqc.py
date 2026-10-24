from _draw import *
from _world import *

# 1. 독자가 오탈자를 발견 — 이미 다 찍고 난 뒤
P1 = svg(300, sky(300)
         + person(560, 150, s=0.85, face=FROWN, **READER) + printplate(560, 230, 0.6)
         + bubble(380, 70, 240, 44, "⟦12쪽에 오탈자가 있어요!|there's a typo on page 12!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(180, 150, s=0.85, face=SWEAT, **EDITOR)
         + label(380, 280, "⟦이미 다 찍어서 독자 손에 들어간 뒤예요|it's already printed and in the reader's hands⟧", 12, "var(--ink)"))

# 2. 나중에 찾으면 늦고 비쌈
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + printplate(250, 150, 1.0, "⟦이미 찍은 책|already printed⟧") + printplate(380, 150, 1.0) + printplate(510, 150, 1.0)
         + label(380, 50, "⟦결함을 늦게 찾을수록, 고치는 값은 더 비싸져요|the later a flaw is found, the more it costs to fix⟧", 13, "var(--bad)")
         + label(380, 260, "⟦다 찍은 뒤 고치려면 전부 다시 찍어야 해요|fixing it after printing means reprinting everything⟧", 12, "var(--ink)", cls="d"))

# 3. 편집 과정 자체를 보는 QA, 완성된 원고를 보는 QC (hero)
P3 = svg(340, sky(340)
         + person(240, 120, s=0.85, face=EYES, **EDITOR) + styleguide(140, 200, 200, 110, "⟦QA: 과정 점검|QA: process check⟧", ("⟦교열 절차를 지켰나|proofing steps followed?⟧",), 0.85)
         + person(560, 120, s=0.85, face=EYES, **PROOFER) + manuscript(560, 210, 0.9, marks=2)
         + label(380, 30, "⟦QA는 \"만드는 방식\"을, QC는 \"만들어진 결과\"를 봐요|QA checks the way it's made, QC checks what came out of it⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦둘 다 있어야 오탈자가 독자 손에 닿기 전에 걸러져요|both are needed to catch typos before they reach readers⟧", 12, "var(--muted)"))

PROCESS_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 14 A18 18 0 0 1 50 32" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M44 24 l8 -4 l-2 9z" fill="var(--accent)"/>')
PREVENT_I = icon('<path d="M32 10 L54 22 V40 C54 50 44 58 32 58 C20 58 10 50 10 40 V22 Z" fill="var(--good)"/><path d="M24 32 l6 6 l12 -14" stroke="#FFF8E7" stroke-width="4" fill="none" stroke-linecap="round"/>')
READ_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
MARK_RED_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="30" cy="34" r="5" fill="var(--bad)"/>')

PAGE = {
    "slug": "qaqc", "order": 34,
    "title": ("규칙을 지켰나, 책이 맞나", "Did We Follow the Rules, Is the Book Right"),
    "h1": ("<em>품질보증(QA)과 품질관리(QC)</em>가 뭐예요?", "What are <em>QA and QC</em>?"),
    "sub": ("편집 과정을 지키는 일과, 완성된 원고를 직접 읽고 표시하는 일은 서로 다른 일이에요.",
            "Watching that the editing process is followed, and reading the finished manuscript to mark it up, are two different jobs."),
    "panels": [
        {"svg": P1, "alt": ("독자가 이미 인쇄된 책에서 오탈자를 발견하고 편집장이 당황함", "A reader finds a typo in an already-printed book, and the editor is caught off guard"),
         "caption": ("독자가 오탈자를 발견했어요 — 이미 다 찍은 뒤에요.", "A reader found a typo — after everything was already printed."),
         "small": ("이미 독자 손에 들어간 뒤라 되돌리기 힘들어요.", "It's already in the reader's hands, so it's hard to undo.")},
        {"svg": P2, "alt": ("이미 인쇄된 책 세 권이 쌓여 있고, 결함을 늦게 찾을수록 고치는 값이 비싸진다는 설명", "Three already-printed books stacked up, with a note that finding flaws late costs more to fix"),
         "caption": ("나중에 찾으면 늦고, 고치는 값도 비싸져요.", "Found late, it's both slow and expensive to fix."),
         "small": ("다 찍은 뒤 고치려면 전부 다시 찍어야 해요.", "Fixing it after printing means reprinting everything.")},
        {"svg": P3, "hero": True, "alt": ("편집장은 교열 절차 자체를 점검하고(QA), 교정자는 완성된 원고를 직접 읽고 표시함(QC)", "The editor checks the proofing process itself (QA), while the proofreader reads and marks up the finished manuscript (QC)"),
         "caption": ("QA는 \"만드는 방식\"을, QC는 \"만들어진 결과\"를 봐요.", "QA checks how it's made; QC checks what came out of it."),
         "small": ("둘 다 있어야 오탈자가 독자 손에 닿기 전에 걸러져요.", "Both are needed to catch typos before they reach readers."),
         "tricks": (4, [
             (PROCESS_I, ("QA = 공정 점검", "QA = process check"), ("교열 절차 자체를 봐요", "watches the proofing procedure itself"), "calm"),
             (PREVENT_I, ("QA = 예방 중심", "QA = prevention-focused"), ("애초에 덜 틀리게 해요", "aims to cause fewer errors up front")),
             (READ_I, ("QC = 결과물 검사", "QC = product inspection"), ("완성된 원고를 직접 읽어요", "reads the finished manuscript directly"), "warm"),
             (MARK_RED_I, ("QC = 결함 찾아 표시", "QC = find and mark flaws"), ("빨간 펜으로 콕 집어요", "marks each one with a red pen")),
         ])},
        {"svg": svg(320, sky(320)
                     + styleguide(60, 40, 300, 240, "⟦QA (품질보증)|QA (quality assurance)⟧",
                                  ("⟦편집 절차 준수 여부|was the process followed?⟧", "⟦조직 표준 지킴|org standard kept?⟧", "⟦예방 중심|prevention-focused⟧"), 1.0)
                     + styleguide(420, 40, 280, 240, "⟦QC (품질관리)|QC (quality control)⟧",
                                  ("⟦완성 원고 직접 검사|inspect the finished manuscript⟧", "⟦오탈자 표시|mark the typos⟧", "⟦결과 중심|output-focused⟧"), 1.0)
                     + label(380, 300, "⟦QA는 넓고 미리, QC는 좁고 나중에 봐요|QA looks broad and early, QC looks narrow and late⟧", 12, "var(--ink)")),
         "alt": ("왼쪽: QA는 편집 절차 준수 여부를 봄. 오른쪽: QC는 완성 원고를 직접 검사함", "Left: QA checks whether the process was followed. Right: QC inspects the finished manuscript directly"),
         "caption": ("QA와 QC는 보는 범위와 시점이 달라요.", "QA and QC differ in scope and timing."),
         "small": ("QA는 넓고 미리, QC는 좁고 나중에 봐요.", "QA looks broad and early; QC looks narrow and late.")},
        {"svg": svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
                     + person(190, 130, s=0.8, face=FROWN, **PROOFER) + label(190, 260, "⟦QA 없이 QC만: 늦고 비싸요|QC alone, no QA: late and costly⟧", 11, "var(--ink)")
                     + person(570, 130, s=0.8, face=SMILE, **EDITOR) + label(570, 260, "⟦QA가 있으면 결함이 애초에 줄어요|with QA, fewer flaws appear in the first place⟧", 11, "var(--ink)")
                     + label(380, 305, "⟦QC는 걸러내는 그물, QA는 애초에 덜 터지게 하는 손질이에요|QC is the net that catches flaws, QA is the care that makes fewer in the first place⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: QA 없이 QC만 하면 늦고 비쌈. 오른쪽: QA가 있으면 결함이 애초에 줄어듦", "Left: QC alone, without QA, is late and costly. Right: with QA, fewer flaws appear from the start"),
         "caption": ("둘 다 필요하지만 역할은 달라요.", "Both are needed, but they play different roles."),
         "small": ("QC는 걸러내는 그물, QA는 애초에 덜 틀리게 하는 손질이에요.", "QC is the net that catches flaws; QA is the care that prevents them in the first place.")},
    ],
    "summary": (("<b>QA(품질보증)</b>는 편집 <b>과정</b>이 기준대로 지켜졌는지 보고, <b>QC(품질관리)</b>는 완성된 <b>결과물</b>을 직접 검사해 결함을 찾아내요.",
                 "<b>QA</b> checks whether the <b>process</b> followed the standard; <b>QC</b> inspects the finished <b>product</b> itself to find defects."),
                ("QA(Quality Assurance)는 프로세스 표준·절차 준수를 점검해 결함 발생을 예방하는 활동이고, QC(Quality Control)는 산출물을 직접 검사·테스트해 결함을 찾아내는 활동이에요. QA는 '예방', QC는 '검출'에 가깝고, 둘은 서로 대체가 아니라 보완 관계예요.",
                 "QA (Quality Assurance) checks adherence to process standards to prevent defects from happening; QC (Quality Control) directly inspects and tests the product to find defects that did happen. QA leans toward prevention, QC toward detection — they complement rather than replace each other.")),
    "glossary": [
        ("QA(품질보증)", "Quality Assurance", ("편집 절차를 지켰는지 보는 일.", "Checking whether the editing process was followed."), ("예방에 가까워요.", "Closer to prevention.")),
        ("QC(품질관리)", "Quality Control", ("완성 원고를 직접 검사하는 일.", "Directly inspecting the finished manuscript."), ("검출에 가까워요.", "Closer to detection.")),
        ("검증(Verification)", "Verification", ("\"제대로 만들었나\"를 보는 것.", "Checking \"did we build it right.\""), ("QA 쪽에 더 가까워요.", "Leans closer to QA.")),
        ("확인(Validation)", "Validation", ("\"맞는 걸 만들었나\"를 보는 것.", "Checking \"did we build the right thing.\""), ("QC/테스트 쪽에 더 가까워요.", "Leans closer to QC and testing.")),
        ("결함(Defect)", "Defect", ("원고에 남은 오탈자.", "A typo left in the manuscript."), ("QC가 직접 찾아내는 대상이에요.", "What QC directly hunts for.")),
        ("ISO 9001", "ISO 9001", ("품질 경영 체계의 국제 표준.", "An international standard for quality management systems."), ("QA가 따르는 외부 기준 중 하나예요.", "One external standard QA can follow.")),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("여러 책의 품질과 일정을 함께 점검.", "Checking quality and schedule across many books at once."), ('QA보다 더 넓은 범위를 봐요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Looks at an even wider scope than QA. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("CMMI", "CMMI", ("조직의 품질 프로세스 성숙도.", "How mature an organization's quality process is."), ("QA 활동이 누적되면 성숙도가 올라가요.", "Consistent QA work is what raises this maturity.")),
    ],
}
