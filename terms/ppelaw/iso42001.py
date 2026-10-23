"""ISO/IEC 42001 (AI 경영시스템)."""
from _draw import *
from _world import *

RISK_I = icon('<path d="M32 10 L54 50 H10 Z" fill="var(--bad-soft)" stroke="var(--bad)" stroke-width="3"/><path d="M32 24 v14" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="44" r="2.5" fill="var(--bad)"/>')
RECORD_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
HUMAN_I = icon('<circle cx="32" cy="20" r="9" fill="var(--accent)"/><path d="M16 54 q16 -22 32 0" stroke="var(--accent)" stroke-width="6" fill="none" stroke-linecap="round"/>')
LOOP_I = icon('<path d="M46 20 a18 18 0 1 1 -8 -10" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M46 8 v12 h-12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. AI 학습도우미 앱을 들이려는데 기준이 없어요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=EYES, **REP) + bubble(130, 70, 220, 44, "⟦이 AI 학습도우미, 들여도 될까요?|can we bring in this AI study helper?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=FROWN, **TEACHER) + bubble(470, 70, 220, 44, "⟦괜찮은 AI인지 확인할 기준이 없어요|there's no standard to check if it's okay⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦학교에 AI를 들이는 공통 기준이 아직 없어요|there's no shared standard yet for bringing AI into school⟧", 13, "var(--ink)", cls="d"))

# 2. 각자 마음대로 쓰다 사고가 나요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(220, 135, s=0.8, face=SWEAT + EYES, **STUDENT) + label(220, 265, "⟦AI가 왜 저만 낮게 평가했는지 몰라요|I don't know why the AI graded only me low⟧", 11, "var(--bad)")
         + person(560, 135, s=0.8, face=FROWN, **REP) + label(560, 265, "⟦반마다 AI를 다르게 써서 기준이 다 달라요|every class uses the AI differently, with no common rule⟧", 11, "var(--bad)")
         + label(380, 300, "⟦기준 없이 쓰면 편향되거나 설명 못 하는 사고가 남아요|without a standard, bias and unexplainable decisions slip through⟧", 12, "var(--ink)", cls="d"))

# 3. ISO/IEC 42001 = 학생회가 정한 AI 관리 인증 기준 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦ISO/IEC 42001 = AI를 책임감 있게 관리하는지 확인하고 도장을 찍어주는 국제표준|ISO/IEC 42001 = the international standard that checks AI is managed responsibly, and stamps it⟧", 12, "var(--ink)", cls="d")
         + person(170, 120, s=0.9, face=EYES, **PRESIDENT)
         + checkmachine(380, 185, 1.3)
         + '<circle cx="380" cy="230" r="34" fill="var(--good)"/><path d="M365 230 l10 10 l18 -22" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' + label(380, 285, "⟦AIMS 인증|AIMS CERTIFIED⟧", 10, "var(--good)", cls="d")
         + person(600, 150, s=0.8, face=SMILE, **TEACHER)
         + label(380, 325, "⟦ISO 27001과 비슷한 구조로, 대상만 'AI 관리'예요|structured like ISO 27001, but the target is \"managing AI\"⟧", 11, "var(--muted)"))

# 4. ISO 27001 vs ISO 42001
P4 = svg(300, sky(300, ground=False)
         + rulesboard(50, 40, 320, 220, "⟦ISO 27001|ISO 27001⟧",
                      ("⟦정보보안 관리체계|information-security mgmt system⟧", "⟦기밀성·무결성·가용성|confidentiality, integrity, availability⟧", "⟦PDCA로 지속 개선|continuous PDCA improvement⟧"), 1.0)
         + rulesboard(390, 40, 320, 220, "⟦ISO 42001|ISO 42001⟧",
                      ("⟦AI 경영시스템(AIMS)|AI management system (AIMS)⟧", "⟦위험·편향·설명가능성|risk, bias, explainability⟧", "⟦같은 PDCA 구조|the same PDCA structure⟧"), 1.0, hl=1)
         + label(380, 285, "⟦구조는 닮았지만, 42001은 AI만의 위험(편향·설명가능성)을 더 봐요|similar in structure, but 42001 adds AI-specific risks like bias and explainability⟧", 12, "var(--ink)", cls="d"))

# 5. 인증받았다고 다 끝나는 건 아니에요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 120, s=0.8, face=SMILE, **PRESIDENT) + label(190, 260, "⟦관리 체계는 갖췄어요|the management system is in place⟧", 11, "var(--ink)")
         + person(570, 120, s=0.8, face=EYES, **STUDENT) + label(570, 260, "⟦근데 AI가 늘 맞게 판단하나요?|but does the AI always judge correctly?⟧", 11, "var(--ink)")
         + label(380, 305, "⟦인증은 '관리한다'는 뜻이지 '완벽하다'는 뜻이 아니에요|certified means managed well — not that it's flawless⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "iso42001", "order": 7,
    "title": ("AI도 규칙대로 쓰는지 도장 찍기", "Stamping That AI Is Managed by the Rules Too"),
    "h1": ("<em>ISO/IEC 42001</em>이 뭐예요?", "What is <em>ISO/IEC 42001</em>?"),
    "sub": ("ISO/IEC 42001을, 학생회가 AI를 책임감 있게 관리하는지 확인하고 도장을 찍어주는 인증 기준 이야기로 풀어봤어요.",
            "ISO/IEC 42001, told as a story about the student council checking AI is managed responsibly, and stamping it."),
    "panels": [
        {"svg": P1, "alt": ("대표가 AI 학습도우미 앱을 들여도 될지 묻고, 선생님은 확인할 기준이 없다고 답함", "A rep asks whether an AI study helper can be brought in; a teacher says there's no standard to check it"),
         "caption": ("AI 학습도우미를 들이려는데 공통 기준이 없어요.", "They want to bring in an AI helper, but there's no shared standard."),
         "small": ("학교에 AI를 들이는 공통 기준이 아직 없어요.", "There's no shared standard yet for bringing AI into school.")},
        {"svg": P2, "alt": ("학생은 AI가 왜 자신만 낮게 평가했는지 모르고, 대표는 반마다 기준이 다르다고 함", "A student doesn't know why the AI graded only them low; a rep says every class uses it differently"),
         "caption": ("각자 마음대로 쓰다 사고가 남아요.", "Using it however each class likes leaves accidents behind."),
         "small": ("기준 없이 쓰면 편향되거나 설명 못 하는 사고가 남아요.", "Without a standard, bias and unexplainable decisions slip through.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 자동 검사기로 확인하고 AIMS 인증 도장을 찍어줌", "The council president checks with an automatic machine and stamps an AIMS certification"),
         "caption": ("ISO/IEC 42001은 AI를 책임감 있게 관리하는지 확인하고 도장을 찍어주는 국제표준이에요.", "ISO/IEC 42001 is the international standard that checks AI is managed responsibly, and stamps it."),
         "small": ("ISO 27001과 비슷한 구조로, 대상만 'AI 관리'예요.", "Structured like ISO 27001, but the target is \"managing AI.\""),
         "tricks": (4, [
             (RISK_I, ("위험 미리 찾기", "Find risk early"), ("편향 같은 AI 위험을요", "risks like bias, specifically"), "warm"),
             (RECORD_I, ("설명 가능하게 기록", "Keep explainable records"), ("왜 그런 결과인지 남겨요", "why a result came out that way"), "calm"),
             (HUMAN_I, ("사람이 최종 확인", "A human has the final say"), ("AI 혼자 결정하지 않아요", "AI doesn't decide alone")),
             (LOOP_I, ("계속 점검하고 고치기", "Check and fix, continuously"), ("한 번으로 끝나지 않아요", "never a one-time thing")),
         ])},
        {"svg": P4, "alt": ("ISO 27001과 ISO 42001을 나란히 비교한 규칙판 두 개", "Two rule boards comparing ISO 27001 and ISO 42001 side by side"),
         "caption": ("ISO 27001과 ISO 42001은 구조가 닮았어요.", "ISO 27001 and ISO 42001 share a similar structure."),
         "small": ("구조는 닮았지만, 42001은 AI만의 위험(편향·설명가능성)을 더 봐요.", "Similar in structure, but 42001 adds AI-specific risks like bias and explainability.")},
        {"svg": P5, "alt": ("왼쪽: 관리 체계를 갖췄다고 웃는 학생회장. 오른쪽: AI가 늘 맞는지 묻는 학생", "Left: the president smiles, having set up the management system. Right: a student asks if the AI always judges correctly"),
         "caption": ("인증받았다고 다 끝나는 건 아니에요.", "Being certified doesn't mean the job is done."),
         "small": ("인증은 '관리한다'는 뜻이지 '완벽하다'는 뜻이 아니에요.", "Certified means managed well — not that it's flawless.")},
    ],
    "summary": (("<b>ISO/IEC 42001</b> = AI를 쓰는 조직이 <b>위험관리·설명가능성·사람의 확인</b>을 갖췄는지 확인하고 <b>인증 도장</b>을 찍어주는 국제표준.",
                 "<b>ISO/IEC 42001</b> = the international standard that checks an organization using AI has <b>risk management, explainability, and human oversight</b> in place, and gives it a <b>certification stamp</b>."),
                ("ISO/IEC 42001:2023은 세계 최초의 AI 경영시스템(AIMS, AI Management System) 국제표준이에요. ISO 27001(정보보안 경영시스템)과 같은 PDCA 구조를 따르면서, AI 특유의 위험(편향, 설명가능성, 데이터 품질, 사람의 감독)을 추가로 요구해요. 인증은 조직이 AI를 '책임감 있게 관리하는 체계'를 갖췄다는 증거이지, AI의 모든 판단이 옳다는 보증은 아니에요.",
                 "ISO/IEC 42001:2023 is the world's first international standard for an AI Management System (AIMS). It follows the same PDCA structure as ISO 27001 (information security management) while adding requirements specific to AI — risk, explainability, data quality, and human oversight. Certification proves an organization has a system for managing AI responsibly — not that every decision the AI makes is correct.")),
    "glossary": [
        ("ISO/IEC 42001", "ISO/IEC 42001", ("AI 관리 인증 도장.", "The stamp certifying AI is managed well."), ("세계 최초의 AI 경영시스템(AIMS) 표준이에요.", "The world's first AI management system standard.")),
        ("AIMS", "AI Management System", ("AI를 관리하는 전체 체계.", "The whole system for managing AI."), ("위험관리부터 지속 개선까지 포함해요.", "Covers everything from risk management to ongoing improvement.")),
        ("PDCA", "PDCA (Plan-Do-Check-Act)", ("계획하고, 해보고, 확인하고, 고치는 순환.", "The cycle of plan, do, check, and fix."), ("ISO 경영시스템 표준들의 공통 뼈대예요.", "The common backbone of ISO management-system standards.")),
        ("AI 위험관리", "AI Risk Management", ("편향·오작동 같은 위험을 미리 찾는 것.", "Spotting risks like bias or malfunction in advance."), ("42001이 요구하는 핵심 활동이에요.", "A core activity 42001 requires.")),
        ("설명가능성", "Explainability", ("왜 그런 결과가 나왔는지 설명할 수 있는 성질.", "Being able to explain why a result came out that way."), ("기록이 없으면 설명도 불가능해요.", "No record means no explanation either.")),
        ("사람의 감독", "Human Oversight", ("AI 혼자 최종 결정을 내리지 않는 것.", "Not letting AI make the final call alone."), ("사람이 확인하는 단계를 반드시 둬요.", "A human-review step is always kept in place.")),
        ("ISO/IEC 27001", "ISO/IEC 27001", ("정보보안 관리체계 인증.", "The certification for information-security management."), ('구조가 닮은 먼저 나온 표준이에요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'The earlier standard this one is structured after. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
        ("AI 윤리기준·거버넌스", "AI Ethics & Governance", ("매일 지키는 AI 운영 원칙.", "The day-to-day principles for running AI responsibly."), ('이 표준의 인증 틀과 달리, 실제 운영 원칙 자체를 다뤄요. → <a href="aiethicsgov-ko.html">검사장 공통 등급 원칙판</a>', 'Unlike this standard\'s certification frame, it covers the operating principles themselves. → <a href="aiethicsgov-en.html">the shared grading charter</a>')),
    ],
}
