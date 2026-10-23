"""AI 윤리·법적 이슈 (법적 책임 각도)."""
from _draw import *
from _world import *

COPY_I = icon('<rect x="12" y="10" width="28" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="44" cy="40" r="14" fill="none" stroke="var(--bad)" stroke-width="3"/><path d="M44 33 v14 M37 40 h14" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
PRIVACY_I = icon('<circle cx="32" cy="24" r="10" fill="var(--accent)"/><path d="M16 54 q16 -20 32 0" stroke="var(--accent)" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M14 14 L50 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
BIAS_I = icon('<path d="M32 14 V50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 H50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 l-6 20 h12z" fill="var(--bad)"/><path d="M50 24 l-6 8 h12z" fill="var(--good)"/>')
BLAME_I = icon('<circle cx="32" cy="32" r="22" fill="var(--accent)"/><path d="M32 20 v16" stroke="#FFF" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="44" r="2.5" fill="#FFF"/>')

# 1. AI가 추천한 대로 했다가 억울한 학생이 생겼어요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=FROWN, **STUDENT) + bubble(120, 70, 230, 44, "⟦AI가 저만 과학 동아리에서 뺐어요|the AI left only me out of the science club⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **PRESIDENT) + bubble(470, 70, 220, 44, "⟦그래도 누군가는 책임져야죠|someone still has to answer for it⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦'AI가 그랬어요'로는 끝나지 않아요|\"the AI did it\" isn't the end of the story⟧", 13, "var(--ink)", cls="d"))

# 2. 누구 책임인지 애매해서 다퉈요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.7, face=FROWN, **REP) + label(170, 250, "⟦만든 사람 책임 아니에요?|isn't it the maker's fault?⟧", 11, "var(--ink)")
         + person(380, 150, s=0.7, face=EYES, **PRESIDENT) + label(380, 250, "⟦쓴 우리 책임인가요?|is it on us, who used it?⟧", 11, "var(--ink)")
         + person(590, 150, s=0.7, face=FROWN, **TEACHER) + label(590, 250, "⟦AI 자체 책임은 아니죠|it can't be the AI's own fault⟧", 11, "var(--ink)")
         + label(380, 285, "⟦책임이 애매하면 피해 본 학생만 남겨져요|when responsibility is vague, the harmed student is the one left behind⟧", 12, "var(--ink)", cls="d"))

# 3. AI 윤리·법적 이슈 = AI를 쓸 때도 사람이 책임지는 구간을 법으로 정하는 것 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦AI 윤리·법적 이슈 = AI를 써도 사람이 책임지는 구간을 법으로 정해두는 것|AI ethics and legal issues = laws that pin down where a human stays responsible, even when AI is used⟧", 12, "var(--ink)", cls="d")
         + person(220, 130, s=0.85, face=EYES, **TEACHER) + gavel(220, 205, 0.9)
         + person(540, 130, s=0.85, face=SMILE, **PRESIDENT)
         + label(380, 320, "⟦저작권·개인정보·차별·책임소재, 네 가지가 핵심이에요|copyright, privacy, discrimination, and liability — the four core issues⟧", 11, "var(--muted)"))

# 4. ISO/IEC 42001(표준) vs 법(규제)
P4 = svg(280, sky(280, ground=False)
         + rulesboard(50, 20, 320, 200, "⟦ISO/IEC 42001|ISO/IEC 42001⟧", ("⟦관리 '표준'|a management STANDARD⟧", "⟦인증·자율 성격|certification, largely voluntary⟧"), 1.0)
         + rulesboard(390, 20, 320, 200, "⟦AI 관련 법(국내법/EU AI Act)|AI LAW (domestic acts / EU AI Act)⟧", ("⟦나라가 만든 '법'|a LAW a country enacts⟧", "⟦강제·처벌 성격|mandatory, with penalties⟧"), 1.0, hl=1)
         + label(380, 250, "⟦표준은 '어떻게 관리할까', 법은 '어기면 어떻게 될까'를 다뤄요|the standard asks how to manage it; the law asks what happens if you don't⟧", 12, "var(--ink)", cls="d"))

# 5. 법대로 해도 사고가 안 생기는 건 아니에요
P5 = svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 130, s=0.8, face=SWEAT + EYES, **PRESIDENT) + label(190, 260, "⟦법은 나라마다, 계속 빠르게 바뀌어요|laws differ by country and keep changing fast⟧", 11, "var(--bad)")
         + person(570, 130, s=0.8, face=EYES, **TEACHER) + label(570, 260, "⟦지켰다고 사고가 안 생기는 건 아니에요|following the law doesn't mean nothing goes wrong⟧", 11, "var(--ink)")
         + label(380, 305, "⟦법은 최소선이에요 — 규정 준수와 같은 이야기예요|the law is a floor, too — the same message as compliance⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aiethicslaw", "order": 10,
    "title": ("AI가 사고 치면 누가 책임져요?", "Who's Responsible When AI Messes Up?"),
    "h1": ("<em>AI 윤리·법적 이슈</em>가 뭐예요?", "What are <em>AI Ethics & Legal Issues</em>?"),
    "sub": ("AI 윤리·법적 이슈를, AI를 써도 사람이 책임지는 구간을 법으로 정해두는 이야기로 풀어봤어요.",
            "AI ethics and legal issues, told as a story about laws that pin down where a human stays responsible, even when AI is used."),
    "panels": [
        {"svg": P1, "alt": ("AI가 자신만 동아리에서 뺐다고 억울해하는 학생과, 그래도 책임져야 한다는 학생회장", "A student upset that the AI left only them out of a club, and a president saying someone still has to answer for it"),
         "caption": ("AI가 추천한 대로 했다가 억울한 학생이 생겼어요.", "Following the AI's recommendation left a student feeling wronged."),
         "small": ("'AI가 그랬어요'로는 끝나지 않아요.", "\"The AI did it\" isn't the end of the story.")},
        {"svg": P2, "alt": ("대표, 학생회장, 선생님이 각각 만든 사람·쓴 사람·AI 자체 중 누구 책임인지 다툼", "A rep, a president, and a teacher argue over whether the maker, the user, or the AI itself is responsible"),
         "caption": ("누구 책임인지 애매해서 다퉈요.", "It's unclear whose responsibility it is, so people argue."),
         "small": ("책임이 애매하면 피해 본 학생만 남겨져요.", "When responsibility is vague, the harmed student is the one left behind.")},
        {"svg": P3, "hero": True, "alt": ("선생님이 의사봉을 들고 책임 구간을 정하고, 학생회장이 웃으며 지켜봄", "A teacher holds a gavel marking out the zone of responsibility, as the president looks on"),
         "caption": ("AI 윤리·법적 이슈는 AI를 써도 사람이 책임지는 구간을 법으로 정하는 거예요.", "AI ethics and legal issues are about laws that pin down where a human stays responsible, even when AI is used."),
         "small": ("저작권·개인정보·차별·책임소재, 네 가지가 핵심이에요.", "Copyright, privacy, discrimination, and liability — the four core issues."),
         "tricks": (4, [
             (COPY_I, ("저작권 문제", "Copyright issues"), ("AI가 베낀 그림, 누구 거?", "AI-copied art — whose is it?"), "warm"),
             (PRIVACY_I, ("개인정보 문제", "Privacy issues"), ("몰래 학생 정보를 썼나?", "did it quietly use student data?")),
             (BIAS_I, ("차별 문제", "Discrimination issues"), ("특정 학생만 불리하게?", "unfairly singling someone out?"), "calm"),
             (BLAME_I, ("책임소재", "Where liability lands"), ("최종 확인한 사람이 책임져요", "the final human reviewer is liable")),
         ])},
        {"svg": P4, "alt": ("ISO/IEC 42001(표준)과 AI 관련 법을 성격 차이로 비교한 규칙판 두 개", "Two rule boards contrasting ISO/IEC 42001 (a standard) with AI-related law"),
         "caption": ("표준(ISO/IEC 42001)과 법은 성격이 달라요.", "A standard like ISO/IEC 42001 and a law are different in kind."),
         "small": ("표준은 '어떻게 관리할까', 법은 '어기면 어떻게 될까'를 다뤄요.", "The standard asks how to manage it; the law asks what happens if you don't.")},
        {"svg": P5, "alt": ("왼쪽: 법이 나라마다 빠르게 바뀌어 땀 흘리는 학생회장. 오른쪽: 지켰다고 사고가 안 생기는 건 아니라는 선생님", "Left: the president sweating as laws shift quickly across countries. Right: a teacher noting that following the law doesn't prevent every problem"),
         "caption": ("법대로 해도 사고가 안 생기는 건 아니에요.", "Even following the law doesn't mean nothing goes wrong."),
         "small": ("법은 최소선이에요 — 규정 준수와 같은 이야기예요.", "The law is a floor, too — the same message as compliance.")},
    ],
    "summary": (("<b>AI 윤리·법적 이슈</b> = AI를 쓰더라도 <b>저작권·개인정보·차별·책임소재</b>에서 사람이 책임지는 구간을 <b>법으로</b> 정해두는 것.",
                 "<b>AI ethics & legal issues</b> = pinning down, <b>by law</b>, where a human stays responsible for <b>copyright, privacy, discrimination, and liability</b>, even when AI is used."),
                ("AI 윤리·법적 이슈는 AI 학습데이터와 생성물의 저작권 분쟁, 학습데이터에 포함된 개인정보, 알고리즘 편향으로 인한 차별, 그리고 오판 시 개발자·운영자·이용자 중 누가 책임지는지를 다루는 규제 영역이에요. EU AI Act는 위험도에 따라 규제 수준을 나누고, 국내에서도 AI기본법 등 관련 법이 빠르게 정비되고 있어요. ISO/IEC 42001 같은 '표준'이 자율적 관리 체계라면, 법은 어겼을 때 처벌이 따르는 강제 규범이에요.",
                 "AI ethics and legal issues cover copyright disputes over AI training data and generated output, personal data embedded in training sets, discrimination from algorithmic bias, and — when something goes wrong — who among the developer, operator, and user is liable. The EU AI Act tiers its rules by risk level, and domestic laws such as Korea's AI Framework Act are being put in place quickly too. Where a standard like ISO/IEC 42001 is a largely voluntary management framework, law is a mandatory rule with penalties for breaking it.")),
    "glossary": [
        ("AI 저작권", "AI Copyright", ("AI가 학습하거나 만든 결과물의 소유권 문제.", "Who owns what AI trained on or produced."), ("아직 나라마다 결론이 다른 영역이에요.", "Countries still reach different conclusions here.")),
        ("알고리즘 차별", "Algorithmic Discrimination", ("AI가 특정 집단에 불리하게 판단하는 것.", "AI judging unfairly against a specific group."), ("학습 데이터의 편향에서 비롯돼요.", "Usually traces back to bias in the training data.")),
        ("책임소재", "Liability", ("오판이 났을 때 누가 책임지는지.", "Who answers for it when AI gets something wrong."), ("개발자·운영자·이용자 중 하나로 정해요.", "Assigned to the developer, operator, or user.")),
        ("EU AI Act", "EU AI Act", ("위험도별로 규제 수준을 나눈 유럽연합 법.", "An EU law that tiers regulation by risk level."), ("위험이 클수록 규제도 강해져요.", "Higher risk means stricter rules.")),
        ("AI기본법(국내)", "AI Framework Act (Korea)", ("국내에서 AI를 다루는 기본 법률.", "Korea's foundational law for AI."), ("빠르게 바뀌는 중인 법 분야예요.", "A fast-moving area of law.")),
        ("표준 vs 법", "Standard vs Law", ("자율적 관리 틀과, 처벌이 따르는 규범의 차이.", "A voluntary framework versus a rule backed by penalties."), ('표준 쪽은 바로 이웃 페이지에서 다뤄요. → <a href="iso42001-ko.html">AI도 규칙대로 쓰는지 도장 찍기</a>', 'The standard side is covered right next door. → <a href="iso42001-en.html">stamping that AI is managed by the rules too</a>')),
        ("규정 준수", "Compliance", ("규칙을 지키고 증거로 보여주는 것.", "Following the rules and proving it with evidence."), ('법을 지켜도 안전이 보장되진 않는다는 메시지가 같아요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'Shares the message that following the law doesn\'t guarantee safety. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
        ("AI 윤리기준·거버넌스", "AI Ethics & Governance", ("매일 지키는 AI 운영 원칙.", "The day-to-day principles for running AI responsibly."), ('이 페이지는 법적 책임 각도, 그쪽은 운영 원칙 각도예요. → <a href="aiethicsgov-ko.html">검사장 공통 등급 원칙판</a>', 'This page takes the legal-liability angle; that one takes the operating-principle angle. → <a href="aiethicsgov-en.html">the shared grading charter</a>')),
    ],
}
