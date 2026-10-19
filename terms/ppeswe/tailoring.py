from _draw import *
from _world import *

# 1. 편집장이 그림책에도 두꺼운 규칙집을 통째로 들이밈
P1 = svg(300, sky(300)
         + person(170, 150, s=0.85, face=EYES, **EDITOR)
         + styleguide(300, 70, 220, 190, "⟦편집 규칙집(전체)|FULL EDITING RULEBOOK⟧",
                      ("⟦1. 표지 심사|1. cover review⟧", "⟦2. 각주 형식|2. footnote style⟧",
                       "⟦3. 색인 작성|3. index build⟧", "⟦4. 3단계 교열|4. 3-pass proofing⟧"), 0.85)
         + person(600, 160, s=0.75, face=SWEAT + FROWN, **WRITER)
         + label(380, 280, "⟦그림책도 사전과 똑같은 규칙집을 다 따라야 해요?|does a picture book really need the same rulebook as a dictionary?⟧", 12, "var(--ink)"))

# 2. 그대로 적용하면 둘 다 문제가 생겨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=SWEAT, **WRITER)
         + manuscript(190, 230, 0.6, marks=0)
         + bubble(90, 70, 210, 40, "⟦규칙을 다 지키다 마감을 놓쳐요|following every rule, we miss the deadline⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=FROWN, **PROOFER)
         + manuscript(570, 230, 0.6, marks=3)
         + bubble(460, 70, 220, 40, "⟦규칙을 대충 쓰다 오탈자가 쏟아져요|skipping the rules, typos pour in⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦모든 책에 같은 규칙을 강제하면, 어느 쪽도 좋지 않아요|forcing the same rules on every book helps neither side⟧", 12, "var(--ink)", cls="d"))

# 3. 편집장이 책마다 필요한 규칙만 골라 맞춤 (hero)
P3 = svg(340, sky(340)
         + person(220, 130, s=0.9, face=EYES, **EDITOR)
         + styleguide(330, 60, 150, 110, "⟦그림책용|PICTURE BOOK⟧", ("⟦표지 심사만|cover only⟧",), 0.9)
         + styleguide(520, 60, 170, 150, "⟦사전용|DICTIONARY⟧", ("⟦각주 형식|footnotes⟧", "⟦색인 작성|index⟧", "⟦3단계 교열|3-pass proof⟧"), 0.9)
         + label(380, 30, "⟦테일러링 = 책 종류에 맞게 규칙집에서 필요한 것만 골라 쓰기|Tailoring = picking only what each kind of book actually needs from the rulebook⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦뼈대(핵심 기준)는 남기고, 나머지는 책에 맞게 줄이거나 더해요|the core standard stays — the rest shrinks or grows to fit the book⟧", 12, "var(--muted)"))

CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SCALE_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 28 h20" stroke="#142033" stroke-width="2.5"/>')
TRIM_I = icon('<path d="M16 48 L48 16" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="18" cy="18" r="6" fill="none" stroke="var(--ink)" stroke-width="3"/><circle cx="18" cy="46" r="6" fill="none" stroke="var(--ink)" stroke-width="3"/>')
NOTE_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h14" stroke="#142033" stroke-width="2.5"/><circle cx="46" cy="42" r="8" fill="var(--accent)"/>')

PAGE = {
    "slug": "tailoring", "order": 32,
    "title": ("책마다 다른 편집 규칙", "Different Editing Rules for Each Book"),
    "h1": ("<em>개발방법론 테일러링</em>이 뭐예요?", "What is <em>Methodology Tailoring</em>?"),
    "sub": ("모든 책에 똑같은 편집 규칙을 강요하면 오히려 늦어져요 — 책에 맞게 규칙을 고쳐 쓰는 이야기예요.",
            "Forcing the same editing rules on every book only slows things down — a story about adjusting the rules to fit the book."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 그림책 작가에게도 두꺼운 사전용 규칙집을 들이밈", "The editor hands a thick dictionary-style rulebook to the picture-book author too"),
         "caption": ("그림책도 사전과 똑같은 규칙집을 다 따라야 할까요?", "Does a picture book really need the same rulebook as a dictionary?"),
         "small": ("규칙집은 하나인데, 책은 다 달라요.", "There's one rulebook, but every book is different.")},
        {"svg": P2, "alt": ("왼쪽은 규칙을 다 지키다 마감을 놓침, 오른쪽은 규칙을 대충 쓰다 오탈자가 쏟아짐", "Left: following every rule misses the deadline. Right: skipping rules lets typos pour in"),
         "caption": ("그대로 적용하면 둘 다 문제가 생겨요.", "Applying it as-is causes problems either way."),
         "small": ("모든 책에 같은 규칙을 강제하면, 어느 쪽도 좋지 않아요.", "Forcing the same rules on every book helps neither side.")},
        {"svg": P3, "hero": True, "alt": ("편집장이 그림책용 규칙표와 사전용 규칙표를 따로 만듦", "The editor builds a separate, shorter rule card for the picture book and a fuller one for the dictionary"),
         "caption": ("테일러링 = 책 종류에 맞게 규칙집에서 필요한 것만 고르는 거예요.", "Tailoring = picking only what each kind of book needs from the rulebook."),
         "small": ("뼈대는 남기고, 나머지는 책에 맞게 줄이거나 더해요.", "The core stays — the rest shrinks or grows to fit the book."),
         "tricks": (4, [
             (SCALE_I, ("기준 먼저 보기", "Check the criteria first"), ("규모·중요도·인력부터", "size, criticality, team first"), "calm"),
             (TRIM_I, ("필요한 것만 남기기", "Keep only what's needed"), ("안 맞는 절차는 줄여요", "trim steps that don't fit")),
             (NOTE_I, ("근거를 기록하기", "Record the reasoning"), ("왜 뺐는지 적어둬요", "write down why it was dropped"), "warm"),
             (CHECK_I, ("핵심 기준은 유지", "Keep the core standard"), ("뼈대까지 빼진 않아요", "never cut the backbone itself")),
         ])},
        {"svg": svg(300, sky(300)
                     + styleguide(50, 40, 300, 220, "⟦그림책용 규칙표|PICTURE BOOK RULES⟧",
                                  ("⟦표지 심사만|cover review only⟧", "⟦교열 1단계|1-pass proofing⟧", "⟦색인 생략|no index⟧"), 1.0)
                     + styleguide(410, 40, 300, 220, "⟦사전용 규칙표|DICTIONARY RULES⟧",
                                  ("⟦표지+내지 심사|cover + interior review⟧", "⟦교열 3단계|3-pass proofing⟧", "⟦색인 필수|index required⟧"), 1.0)
                     + label(380, 290, "⟦같은 규칙집에서 나왔지만, 최종 결과물은 서로 달라요|from the same rulebook, but the final checklists differ⟧", 12, "var(--ink)")),
         "alt": ("그림책용 규칙표(간단)와 사전용 규칙표(상세)를 나란히 비교", "Side by side: a simple picture-book rule card and a detailed dictionary rule card"),
         "caption": ("규칙표는 책마다 달라져요.", "The rule card ends up different for each book."),
         "small": ("같은 규칙집에서 나왔지만, 최종 체크리스트는 서로 달라요.", "Drawn from the same rulebook, but the final checklist differs.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
                     + person(190, 150, s=0.8, face=FROWN, **EDITOR) + label(190, 240, "⟦다 빼면: 품질에 구멍이 생겨요|strip too much: quality gaps appear⟧", 11, "var(--ink)")
                     + person(570, 150, s=0.8, face=SMILE, **EDITOR) + label(570, 240, "⟦균형을 맞추면: 빠르고 안전해요|balance it: fast and still safe⟧", 11, "var(--ink)")
                     + label(380, 282, "⟦테일러링은 규칙을 없애는 게 아니라, 책에 맞게 고르는 기술이에요|tailoring isn't deleting rules — it's the skill of choosing them⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 규칙을 다 빼서 품질 구멍 발생. 오른쪽: 균형 잡힌 규칙으로 빠르고 안전함", "Left: stripping too much opens quality gaps. Right: a balanced set of rules stays fast and safe"),
         "caption": ("테일러링도 지나치면 위험해요.", "Even tailoring can go too far."),
         "small": ("규칙을 없애는 게 아니라, 책에 맞게 고르는 기술이에요.", "It isn't about deleting rules — it's choosing them to fit the book.")},
    ],
    "summary": (("<b>개발방법론 테일러링</b> = 정해진 개발 규칙(생명주기·산출물·검토 절차)에서, <b>프로젝트 특성에 맞게</b> 필요한 것만 골라 쓰는 조정 작업.",
                 "<b>Methodology tailoring</b> = adjusting a fixed set of development rules (lifecycle, artifacts, review steps) by choosing only what fits <b>this project's characteristics</b>."),
                ("조직 표준 프로세스(생명주기 모델, 산출물 양식, 검토·승인 절차)를 프로젝트의 규모, 기술 난이도, 참여 인력의 숙련도, 중요도(안전성·보안성) 등에 따라 가감하는 작업이에요. 핵심 통제 기준(품질 게이트 등)은 유지하면서 불필요한 절차를 줄이는 게 목표예요.",
                 "It means adding or removing parts of the organization's standard process (lifecycle model, artifact templates, review/approval steps) based on project size, technical difficulty, team skill level, and criticality (safety, security). The goal is to trim unneeded steps while keeping core controls like quality gates intact.")),
    "glossary": [
        ("테일러링", "Tailoring", ("규칙집에서 필요한 것만 고르기.", "Picking only what's needed from the rulebook."), ("규모·난이도·인력·중요도가 기준이에요.", "Based on size, difficulty, team, and criticality.")),
        ("조직 표준 프로세스", "Organizational Standard Process", ("모든 책이 출발하는 기본 규칙집.", "The base rulebook every book starts from."), ("테일러링의 출발점이에요.", "The starting point tailoring works from.")),
        ("생명주기(SDLC) 모델", "SDLC Model", ("폭포수냐 애자일이냐 같은 전체 틀.", "The overall shape — waterfall or agile."), ("테일러링 대상 중 가장 큰 단위예요.", "The biggest unit tailoring can adjust.")),
        ("CMMI", "CMMI", ("조직의 성숙도를 재는 잣대.", "A ruler for how mature an organization's process is."), ("테일러링 능력도 성숙도의 일부예요.", "The ability to tailor well is itself part of that maturity.")),
        ("품질 게이트", "Quality Gate", ("아무리 줄여도 남겨두는 핵심 검문소.", "The core checkpoint kept even after trimming."), ("테일러링에서도 빼면 안 되는 것.", "The thing tailoring should never cut.")),
        ("제품계열 방법론", "Product Line Engineering", ("핵심 자산을 모아 여러 판으로 파생.", "Gathering core assets to spin off many editions."), ('비슷하게 \'맞춤\'을 다루는 이웃 개념이에요. → <a href="productline-ko.html">같은 틀, 다른 표지</a>', 'A neighboring idea about fitting things to context. → <a href="productline-en.html">same template, different covers</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("이 규칙표가 잘 지켜졌는지 바깥에서 점검.", "Checks from the outside whether this rule card was followed."), ('테일러링 결과를 점검 대상으로 삼기도 해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', "Sometimes reviews the tailoring decisions themselves. → <a href=\"pmoaudit-en.html\">the last checker before publication</a>")),
        ("과잉 프로세스", "Process Overkill", ("작은 책에 사전 규칙집을 통째로 적용하는 것.", "Applying the full dictionary rulebook to a tiny book."), ("테일러링이 막으려는 바로 그 문제예요.", "The exact problem tailoring tries to prevent.")),
    ],
}
