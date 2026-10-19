from _draw import *
from _world import *

# 1. 오래된 원고, 문장이 꼬여 교정자가 손을 못 댐
P1 = svg(300, sky(300)
         + manuscript(260, 140, 1.1, marks=0)
         + '<path d="M232 150 q30 -40 60 0 q30 40 -10 10" stroke="var(--bad)" stroke-width="2" fill="none"/>'
         + person(440, 150, s=0.85, face=SWEAT + EYES, **PROOFER)
         + bubble(440, 60, 240, 44, "⟦문장이 꼬여서 어디부터 손대야 할지 모르겠어요|the sentences are so tangled I don't know where to even start⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦오래된 원고일수록 손대기가 점점 더 무서워져요|the older the manuscript, the scarier it gets to touch⟧", 12, "var(--ink)"))

# 2. 줄거리를 바꾸면 위험, 그냥 둬도 더 힘들어짐
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=FROWN, **WRITER)
         + bubble(100, 70, 240, 44, "⟦줄거리까지 바꾸면 독자가 알아챌 거예요|changing the plot itself and readers will notice⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.75, face=SWEAT + EYES, **PROOFER)
         + bubble(440, 70, 240, 44, "⟦그렇다고 그냥 두면 다음 교정이 더 힘들어져요|but leaving it as-is makes the next edit even harder⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦줄거리는 그대로 두고, 문장만 다시 다듬을 순 없을까요|could we retouch just the sentences and leave the plot alone?⟧", 12, "var(--ink)"))

# 3. 리팩토링 = 줄거리는 그대로, 문장 구조만 다시 다듬기 (hero)
P3 = svg(340, sky(340)
         + person(220, 130, s=0.9, face=EYES, **WRITER)
         + manuscript(140, 200, 0.75) + label(140, 250, "⟦같은 줄거리|same plot⟧", 11, "var(--muted)")
         + '<path d="M210 210 h60" stroke="var(--accent)" stroke-width="4" marker-end="url(#arrow)"/>'
         + '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--accent)"/></marker></defs>'
         + manuscript(360, 200, 0.75) + label(360, 250, "⟦정리된 문장|tidied sentences⟧", 11, "var(--muted)")
         + person(550, 160, s=0.8, face=SMILE, **PROOFER)
         + label(380, 30, "⟦리팩토링 = 줄거리는 그대로 두고, 문장 구조만 다시 다듬는 재편집|refactoring = re-editing the sentence structure while the plot stays exactly the same⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦겉은(줄거리) 그대로, 속만(구조) 다시 다듬어요|the outside (plot) stays, only the inside (structure) gets reworked⟧", 12, "var(--muted)"))

# 4. 리팩토링 체크리스트
P4 = svg(320, sky(320)
         + styleguide(60, 40, 640, 240, "⟦재편집 체크리스트|RE-EDIT CHECKLIST⟧",
                      ("⟦중복 문장 합치기|merge duplicate sentences⟧",
                       "⟦긴 문단 쪼개기|split long paragraphs⟧",
                       "⟦이름(용어) 통일하기|unify names and terms⟧",
                       "⟦한 번에 조금씩 + 매번 줄거리 확인|small steps, checking the plot each time⟧"), 1.0)
         + label(380, 300, "⟦줄거리가 안 바뀌었는지는 교정자가 매번 확인해요|the proofreader checks the plot hasn't moved, every single time⟧", 12, "var(--ink)"))

# 5. 테스트(교정) 없으면 확신 못함, 새 기능 추가가 아님
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **PROOFER)
         + label(190, 240, "⟦교정(테스트) 없인 줄거리가 안 바뀐 건지 확신 못해요|without proofing (tests), you can't be sure the plot held⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **WRITER) + manuscript(570, 220, 0.6)
         + label(570, 265, "⟦새 챕터를 추가하는 건 리팩토링이 아니에요|adding a new chapter isn't refactoring⟧", 11, "var(--ink)")
         + label(380, 282, "⟦리팩토링은 기능 추가가 아니라, 구조만 다시 다듬는 거예요|refactoring isn't adding features — it's only reworking the structure⟧", 12, "var(--ink)", cls="d"))

MERGE_I = icon('<rect x="10" y="18" width="20" height="12" rx="3" fill="var(--muted)"/><rect x="10" y="34" width="20" height="12" rx="3" fill="var(--muted)"/><rect x="38" y="26" width="20" height="12" rx="3" fill="var(--good)"/>')
SPLIT_I = icon('<rect x="18" y="10" width="28" height="18" rx="3" fill="var(--muted)"/><rect x="10" y="36" width="20" height="14" rx="3" fill="var(--good)"/><rect x="34" y="36" width="20" height="14" rx="3" fill="var(--good)"/>')
NAME_I = icon('<text x="32" y="30" text-anchor="middle" font-size="16" font-weight="700" fill="var(--muted)">Aa</text><text x="32" y="50" text-anchor="middle" font-size="16" font-weight="700" fill="var(--good)">Aa</text>')
STEP_I = icon('<circle cx="16" cy="44" r="5" fill="var(--good)"/><circle cx="32" cy="32" r="5" fill="var(--good)"/><circle cx="48" cy="20" r="5" fill="var(--accent)"/><path d="M16 44 L32 32 L48 20" stroke="var(--line)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>')

PAGE = {
    "slug": "refactorppe", "order": 25,
    "title": ("줄거리는 그대로, 문장만 다시 다듬기", "Same Plot, Retouched Sentences"),
    "h1": ("<em>리팩토링</em>이 뭐예요?", "What is <em>Refactoring</em>?"),
    "sub": ("리팩토링을, 줄거리는 그대로 두고 문장 구조만 다시 다듬는 출판사의 재편집 작업으로 풀어봤어요.",
            "Refactoring, told as a story about a publishing house re-editing sentence structure while the plot stays exactly the same."),
    "panels": [
        {"svg": P1, "alt": ("문장이 꼬인 오래된 원고를 보며 교정자가 진땀을 흘림", "A proofreader sweats over an old manuscript with tangled sentences"),
         "caption": ("오래된 원고일수록 손대기가 무서워요.", "The older the manuscript, the scarier it gets to touch."),
         "small": ("문장이 꼬여서 어디부터 손대야 할지 모르겠어요.", "The sentences are so tangled, nobody knows where to even start.")},
        {"svg": P2, "alt": ("작가는 줄거리를 바꾸면 위험하다고, 교정자는 그냥 두면 더 힘들어진다고 걱정함", "The writer worries changing the plot is risky; the proofreader worries leaving it as-is gets harder"),
         "caption": ("줄거리를 바꾸면 위험하고, 그냥 둬도 더 힘들어져요.", "Changing the plot is risky, but leaving it as-is only makes things harder."),
         "small": ("줄거리는 그대로 두고 문장만 다시 다듬을 순 없을까요?", "Could we retouch just the sentences and leave the plot alone?")},
        {"svg": P3, "hero": True, "alt": ("같은 줄거리의 원고가 화살표를 따라 정리된 문장의 원고로 바뀜", "A manuscript with the same plot turns, via an arrow, into one with tidied sentences"),
         "caption": ("리팩토링은 줄거리는 그대로, 문장 구조만 다시 다듬는 거예요.", "Refactoring re-edits the sentence structure while the plot stays exactly the same."),
         "small": ("겉은 그대로, 속만 다시 다듬어요.", "The outside stays the same — only the inside gets reworked."),
         "tricks": (4, [
             (MERGE_I, ("중복 문장 합치기", "Merge duplicate sentences"), ("같은 말을 한 곳으로", "the same idea, said just once"), "calm"),
             (SPLIT_I, ("긴 문단 쪼개기", "Split long paragraphs"), ("짧고 읽기 쉽게", "shorter, easier to read")),
             (NAME_I, ("이름 통일하기", "Unify names and terms"), ("용어를 하나로 맞춰요", "settle on one consistent term")),
             (STEP_I, ("조금씩, 매번 확인", "Small steps, checked each time"), ("줄거리가 안 바뀌었나 봐요", "checking the plot hasn't moved"), "warm"),
         ])},
        {"svg": P4, "alt": ("중복 합치기·문단 쪼개기·이름 통일·조금씩 확인하기 네 항목의 재편집 체크리스트", "A re-edit checklist: merge duplicates, split paragraphs, unify names, small checked steps"),
         "caption": ("리팩토링은 이 네 가지를 반복해요.", "Refactoring repeats these four things."),
         "small": ("줄거리가 안 바뀌었는지는 교정자가 매번 확인해요.", "The proofreader checks the plot hasn't moved, every single time.")},
        {"svg": P5, "alt": ("왼쪽: 교정 없인 줄거리가 안 바뀐 걸 확신 못함. 오른쪽: 새 챕터 추가는 리팩토링이 아님", "Left: without proofing you can't be sure the plot held. Right: adding a new chapter isn't refactoring"),
         "caption": ("교정(테스트) 없이는 확신할 수 없어요.", "Without proofing (tests), you can't be sure."),
         "small": ("리팩토링은 기능 추가가 아니라 구조만 다시 다듬는 거예요.", "Refactoring isn't adding features — it's only reworking the structure.")},
    ],
    "summary": (("<b>리팩토링</b>은 책의 <b>줄거리(겉으로 보이는 동작)</b>는 그대로 두고, 문장 <b>구조(속 설계)</b>만 다시 다듬는 재편집이에요.",
                 "<b>Refactoring</b> is a re-edit that keeps the book's <b>plot (external behavior)</b> exactly the same while reworking only the <b>sentence structure (internal design)</b>."),
                ("리팩토링은 소프트웨어의 외부 동작(기능, 출력 결과)을 바꾸지 않으면서 내부 코드 구조를 개선하는 작업이에요. 중복 제거, 함수/모듈 분리, 네이밍 통일 등을 작은 단계로 나눠 수행하고, 매 단계마다 테스트로 동작이 그대로인지 확인해요. 새 기능을 추가하는 것과는 분명히 구분돼요.",
                 "Refactoring improves a program's internal code structure without changing its external behavior (functionality, output). It's done in small steps — removing duplication, splitting functions/modules, unifying names — verified by tests at each step to confirm behavior hasn't changed. It is distinct from adding new features.")),
    "glossary": [
        ("리팩토링", "Refactoring", ("줄거리는 그대로, 문장만 다시 다듬기.", "Same plot, retouched sentences."), ("외부 동작은 안 바뀌어요.", "The external behavior never changes.")),
        ("외부 동작", "External Behavior", ("독자가 읽는 줄거리.", "The plot readers actually read."), ("리팩토링 전후로 똑같아야 해요.", "Must stay identical before and after.")),
        ("코드 스멜", "Code Smell", ("문장이 꼬여 보이는 낌새.", "The whiff of sentences gone tangled."), ("리팩토링이 필요하다는 신호예요.", "A signal that refactoring is needed.")),
        ("단위테스트", "Unit Test", ("줄거리가 안 바뀌었는지 보는 교정.", "The proofing that checks the plot hasn't moved."), ("리팩토링의 안전망이에요.", "The safety net that makes refactoring safe.")),
        ("기술부채", "Technical Debt", ("나중에 갚아야 할 빚.", "A debt that must be repaid later."), ('리팩토링은 이 빚을 갚는 방법 중 하나예요. → <a href="techdebt-ko.html">지금 빨리 가려고 쌓아둔 빚</a>', 'Refactoring is one way to repay this debt. → <a href="techdebt-en.html">the debt you pile up to move fast now</a>')),
        ("캡슐화", "Encapsulation", ("잠긴 서랍 속을 정리하기.", "Tidying up what's inside the locked drawer."), ('창구 모양은 그대로, 서랍 속만 리팩토링해요. → <a href="encapsulation-ko.html">작가의 잠긴 서랍</a>', "The box stays the same while only the drawer's inside gets refactored. → <a href=\"encapsulation-en.html\">the writer's locked drawer</a>")),
        ("디자인패턴", "Design Pattern", ("편집 스타일가이드.", "The editing style guide."), ("리팩토링의 목적지 중 하나예요.", "Often the destination refactoring moves toward.")),
        ("회귀", "Regression", ("고치다 줄거리가 틀어지는 사고.", "An accident where the plot shifts while editing."), ("리팩토링이 가장 조심하는 사고예요.", "The exact accident refactoring is built to avoid.")),
    ],
}
