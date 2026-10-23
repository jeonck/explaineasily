from _draw import *
from _world import *

# 1. 응급처치 안내서의 오탈자 하나가 그냥 지나칠 뻔했어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **PROOFER)
         + manuscript(260, 130, 0.8, marks=1, text="⟦응급처치 안내서|first-aid manual⟧") + manuscript(390, 150, 0.8, marks=1) + manuscript(490, 120, 0.8, marks=0)
         + label(380, 230, "⟦약 용량 단위 오탈자 하나를 그냥 지나칠 뻔했어요|a single typo in a dosage unit almost slipped through⟧", 12, "var(--bad)")
         + label(380, 280, "⟦보통 책이었으면 괜찮았겠지만, 이 책은 달라요|in an ordinary book it wouldn't matter much — but this book is different⟧", 13, "var(--ink)"))

# 2. 다른 책이랑 똑같이 검토하면 된다는 말, 생명이 걸렸다는 반박
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 220, 36, "⟦다른 책이랑 똑같이 검토하면 되죠|just review it the same way as any other book⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **PROOFER) + bubble(460, 80, 220, 36, "⟦이건 생명이 걸린 문제예요|this one has lives on the line⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦모든 책을 똑같은 강도로 검토할 순 없어요|not every book can be checked at the same intensity⟧", 12, "var(--ink)"))

# 3. 소프트웨어 안전/기능안전 = 위험이 큰 책일수록 검증을 몇 겹으로 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **PROOFER) + inkstamp(460, 90, 0.8)
         + manuscript(260, 180, 0.7, text="⟦1차 검토|1st check⟧") + manuscript(380, 200, 0.7, text="⟦2차 검토|2nd check⟧") + manuscript(500, 180, 0.7, text="⟦독립 재검토|independent re-check⟧")
         + label(380, 30, "⟦소프트웨어 안전/기능안전 = 위험이 큰 책일수록 검증을 몇 겹으로 더 엄격하게 거치게 하는 일|software/functional safety = putting higher-risk books through several extra-strict layers of checking⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦위험 등급에 따라 거치는 겹의 수가 달라져요|the number of layers changes with the risk grade⟧", 12, "var(--muted)"))

# 4. 위험 등급별 검증 강도
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦위험 등급별 검증 강도|VERIFICATION INTENSITY BY RISK⟧",
                      ("⟦등급 낮음 — 교정자 한 명이면 충분|low — one proofreader is enough⟧",
                       "⟦등급 중간 — 교정자 두 명이 교차 확인|medium — two proofreaders cross-check⟧",
                       "⟦등급 높음 — 독립된 팀이 재검토|high — a separate team re-checks⟧",
                       "⟦등급 최고 — 실제 사용 전 실제 시험까지|highest — real trials before real use⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **PROOFER)
         + label(560, 250, "⟦같은 오탈자라도, 책에 따라 무게가 달라요|the same typo carries different weight depending on the book⟧", 11, "var(--muted)")
         + label(380, 300, "⟦위험이 클수록, 검증은 느려지고 비용도 커져요|the higher the risk, the slower and costlier the verification⟧", 12, "var(--ink)"))

# 5. 검증해도 위험이 0이 되진 않아요
P5 = svg(340, '<rect width="380" height="340" fill="var(--accent-soft)"/><rect x="380" width="380" height="340" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=EYES, **PROOFER) + label(190, 260, "⟦위험을 크게 낮춰줘요|it lowers the risk by a lot⟧", 11, "var(--ink)")
         + person(570, 110, s=0.8, face=SMILE, **EDITOR) + manuscript(570, 200, 0.6) + label(570, 260, "⟦그래도 출간은 결국 해야 해요|but the book still has to go out eventually⟧", 11, "var(--ink)")
         + label(380, 315, "⟦안전은 위험을 없애는 게 아니라, 감당할 수 있는 수준까지 낮추는 일이에요|safety isn't eliminating risk — it's lowering it to a level you can live with⟧", 12, "var(--ink)", cls="d"))

GRADE_I = icon('<path d="M18 50 V38 M32 50 V22 M46 50 V8" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
DUAL_I = icon('<circle cx="22" cy="32" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="42" cy="32" r="14" fill="none" stroke="var(--good)" stroke-width="4"/>')
INDEPENDENT_I = icon('<rect x="10" y="14" width="18" height="36" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="36" y="14" width="18" height="36" rx="3" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>')
TRIAL_I = icon('<path d="M26 8 v18 l-14 26 a8 8 0 0 0 7 12 h26 a8 8 0 0 0 7 -12 l-14 -26 v-18" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M22 42 h20" stroke="var(--bad)" stroke-width="3"/>')

PAGE = {
    "slug": "swsafety", "order": 7,
    "title": ("오탈자 하나의 무게가 다른 책", "The Book Where One Typo Weighs Differently"),
    "h1": ("<em>소프트웨어 안전/기능안전</em>이 뭐예요?", "What is <em>Software/Functional Safety</em>?"),
    "sub": ("소프트웨어 안전과 기능안전을, 응급처치 안내서처럼 오탈자 하나가 생명과 직결되는 책에 몇 겹의 엄격한 검증을 거치게 하는 이야기로 풀어봤어요.",
            "Software and functional safety, told as a story about putting a book — like a first-aid manual, where one typo can cost a life — through several layers of extra-strict verification."),
    "panels": [
        {"svg": P1, "alt": ("교정자가 응급처치 안내서의 약 용량 오탈자를 발견해 식은땀을 흘림", "A proofreader breaks into a sweat after spotting a dosage typo in a first-aid manual"),
         "caption": ("약 용량 단위 오탈자 하나를 그냥 지나칠 뻔했어요.", "A single typo in a dosage unit almost slipped through."),
         "small": ("보통 책이었으면 괜찮았겠지만, 이 책은 달라요.", "In an ordinary book it wouldn't matter much — but this book is different.")},
        {"svg": P2, "alt": ("편집장은 다른 책과 똑같이 검토하면 된다고 말하고, 교정자는 생명이 걸린 문제라고 반박함", "The editor says to review it like any other book; the proofreader insists lives are on the line"),
         "caption": ("다른 책이랑 똑같이 검토하면 된다는 말, 생명이 걸렸다는 반박.", "A claim that it can be reviewed like any other book, met with a reminder that lives are at stake."),
         "small": ("모든 책을 똑같은 강도로 검토할 순 없어요.", "Not every book can be checked at the same intensity.")},
        {"svg": P3, "hero": True, "alt": ("교정자가 승인 도장을 들고, 1차 검토·2차 검토·독립 재검토 세 단계를 거친 원고를 확인함", "A proofreader holds an approval stamp, checking manuscripts through a first check, second check, and independent re-check"),
         "caption": ("위험이 큰 책일수록 검증을 몇 겹으로 더 엄격하게 거쳐요.", "A higher-risk book goes through several extra-strict layers of checking."),
         "small": ("위험 등급에 따라 거치는 겹의 수가 달라져요.", "The number of layers changes with the risk grade."),
         "tricks": (4, [
             (GRADE_I, ("위험 등급 나누기", "Grade the risk"), ("책마다 위험 크기가 달라요", "books carry different sizes of risk"), "calm"),
             (DUAL_I, ("둘이 교차 확인하기", "Cross-check with two"), ("한 사람의 실수를 서로 잡아줘요", "catching each other's mistakes")),
             (INDEPENDENT_I, ("독립된 팀이 재검토", "An independent team re-checks"), ("원래 팀과 따로 봐요", "looking at it apart from the original team"), "warm"),
             (TRIAL_I, ("실제로 시험해 보기", "Actually trial it"), ("쓰기 전에 직접 써봐요", "trying it out before real use")),
         ])},
        {"svg": P4, "alt": ("위험 등급별 검증 강도표: 낮음·중간·높음·최고 네 등급", "A verification-intensity table by risk grade: low, medium, high, highest"),
         "caption": ("위험 등급에 따라 검증 강도가 달라요.", "Verification intensity changes with the risk grade."),
         "small": ("같은 오탈자라도, 책에 따라 무게가 달라요.", "The same typo carries different weight depending on the book.")},
        {"svg": P5, "alt": ("왼쪽: 교정자가 위험을 크게 낮춘다고 말함. 오른쪽: 편집장이 그래도 출간은 해야 한다고 말함", "Left: the proofreader says it lowers the risk a lot. Right: the editor says the book still has to go out"),
         "caption": ("검증해도 위험이 0이 되진 않아요.", "Verification doesn't bring risk down to zero."),
         "small": ("감당할 수 있는 수준까지 낮추는 일이에요.", "It's about lowering risk to a level you can live with.")},
    ],
    "summary": (("<b>소프트웨어/기능안전</b> = 위험이 <b>큰 책일수록</b> 검증을 <b>몇 겹으로 더 엄격하게</b> 거치게 하는 일.",
                 "<b>Software/functional safety</b> = putting a <b>higher-risk book</b> through <b>several extra-strict layers</b> of verification."),
                ("기능안전은 시스템이 고장나더라도 사람을 다치게 하지 않도록, 위험도에 따라 검증 수준(SIL 등)을 차등 적용하는 접근이에요. 위험이 클수록 독립적인 검토, 이중화, 실제 시험 등 더 많은 안전장치를 겹겹이 요구해요. 완벽한 무결함이 목표가 아니라, 받아들일 수 있는 수준까지 위험을 낮추는 게 목표예요.",
                 "Functional safety ensures that even if a system fails, people aren't harmed — by applying verification levels (like SIL grades) in proportion to risk. The higher the risk, the more layered safeguards are required: independent review, redundancy, real-world trials. The goal isn't perfect zero-defect — it's lowering risk to an acceptable level.")),
    "glossary": [
        ("기능안전", "Functional Safety", ("고장나도 사람이 다치지 않게 하는 설계.", "Designing so a failure doesn't hurt anyone."), ("위험 등급별로 요구 수준이 달라요.", "Requirements differ by risk grade.")),
        ("안전무결성수준(SIL)", "Safety Integrity Level", ("위험 등급을 나누는 눈금.", "The scale that grades risk."), ("등급이 높을수록 검증이 엄격해져요.", "A higher level demands stricter verification.")),
        ("독립 검증", "Independent Verification", ("원래 팀과 다른 팀이 다시 보는 일.", "A separate team checking it again."), ("한쪽의 맹점을 다른 쪽이 잡아줘요.", "One side's blind spot gets caught by the other.")),
        ("이중화", "Redundancy", ("하나가 실패해도 다른 하나가 버티게 하는 구조.", "A structure where one failing still leaves another standing."), ("교차 확인과 비슷한 원리예요.", "Works on a similar principle to cross-checking.")),
        ("위험 분석", "Risk Analysis", ("어떤 책이 더 위험한지 먼저 가늠하는 일.", "Gauging in advance which books carry more risk."), ("등급을 나누기 전에 해요.", "Done before grading risk.")),
        ("화이트박스/블랙박스 테스트", "White-box/Black-box Testing", ("속을 볼지 겉만 볼지로 나눈 검토법.", "Checking methods split by looking inside or only outside."), ('위험이 클수록 이 둘을 더 깊게, 더 많이 해요. → <a href="wbblacktest-ko.html">속을 펼쳐 볼지, 겉만 읽을지</a>', 'The higher the risk, the deeper and more often both get done. → <a href="wbblacktest-en.html">looking inside, or just reading the outside</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("출간 전 마지막 검수관.", "The last checker before publication."), ('위험 등급이 높은 책일수록 감리도 더 깐깐해져요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'The higher the risk grade, the stricter the audit gets too. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("안전 사례(Safety Case)", "Safety Case", ("이만큼 안전하다는 근거를 모아 둔 서류.", "The dossier gathering evidence that it's safe enough."), ("검증 기록을 모아 외부에 설명할 때 써요.", "Compiles verification records to explain to outsiders.")),
    ],
}
