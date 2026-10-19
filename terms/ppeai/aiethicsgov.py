from _draw import *
from _world import *

# 1. 검사장마다 등급 기준이 다 달라요 — 어떤 곳은 봐주고, 어떤 곳은 너무 깐깐해요
P1 = svg(300, sky(300)
         + person(120, 90, s=0.65, face=EYES, **OPERATOR)
         + gradeboard(50, 185, 140, 64, "", ("⟦대충 통과|anything passes⟧",), 0.7) + label(120, 275, "⟦1검사장 기준|station #1's rule⟧", 11, "var(--muted)")
         + person(380, 90, s=0.65, face=FROWN, **OPERATOR)
         + gradeboard(310, 185, 140, 64, "", ("⟦무조건 불합격|almost nothing passes⟧",), 0.7) + label(380, 275, "⟦2검사장 기준|station #2's rule⟧", 11, "var(--muted)")
         + person(640, 90, s=0.65, face=EYES, **OPERATOR)
         + gradeboard(570, 185, 140, 64, "", ("⟦그날그날 달라요|changes day to day⟧",), 0.7) + label(640, 275, "⟦3검사장 기준|station #3's rule⟧", 11, "var(--muted)")
         + label(380, 25, "⟦검사장마다 등급 기준이 제각각이에요|every station grades by its own rule⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 기준이 안 적히면, 누가 책임지는지·왜 그런 등급인지 아무도 설명 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.8, face=EYES, **FARMER) + bubble(70, 70, 220, 50, "⟦왜 제 작물만 불합격이죠?|why did only my produce fail?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 150, s=0.8, face=SWEAT + EYES, **OPERATOR) + bubble(500, 70, 220, 50, "⟦저도 설명을 못 하겠어요…|I can't explain it either…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦기준이 안 적혀 있으면, 왜 그런 등급인지 아무도 설명 못 해요|without a written standard, nobody can explain why a grade came out the way it did⟧", 12, "var(--ink)", cls="d"))

# 3. AI 윤리기준·거버넌스 = 모든 검사장이 공통으로 지킬 등급 원칙과 책임 체계 (hero)
P3 = svg(360, sky(360)
         + gradeboard(210, 30, 340, 290, "⟦공통 등급 원칙판|SHARED GRADING CHARTER⟧",
                 ("⟦공정성 — 작물 종류로 차별 않기|fairness — no bias by produce type⟧",
                  "⟦설명가능성 — 등급 이유 남기기|explainability — record why a grade was given⟧",
                  "⟦책임소재 — 오판 시 누가 맡나|accountability — who owns a bad call?⟧",
                  "⟦사람 재검토 — 이의 제기 통로|human review — a path to appeal⟧"), 1.0)
         + person(90, 220, s=0.7, face=SMILE, **INSPECTOR)
         + person(660, 220, s=0.6, face=EYES, **OPERATOR)
         + label(380, 25, "⟦AI 윤리기준·거버넌스 = 모든 검사장이 함께 지킬 등급 원칙과 책임 체계예요|a shared charter every station follows for grading principles and accountability⟧", 13, "var(--ink)", cls="d"))

FAIR_I = icon('<path d="M32 10 v20 M14 30 h36" stroke="#142033" stroke-width="4"/><circle cx="18" cy="38" r="10" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="46" cy="38" r="10" fill="none" stroke="var(--good)" stroke-width="4"/>')
EXPLAIN_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 32 h24 M20 40 h16" stroke="#142033" stroke-width="2.5"/>')
OWN_I = icon('<circle cx="32" cy="22" r="11" fill="var(--accent)"/><path d="M14 54 q18 -20 36 0" fill="none" stroke="var(--accent)" stroke-width="5"/>')
APPEAL_I = icon('<path d="M32 10 A22 22 0 1 0 54 32" stroke="var(--good)" stroke-width="5" fill="none"/><path d="M54 14 v18 h-18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "aiethicsgov", "order": 2,
    "title": ("모든 검사장이 함께 쓰는 등급 원칙판", "The Grading Charter Every Station Shares"),
    "h1": ("<em>AI 윤리기준·거버넌스</em>가 뭐예요?", "What is <em>AI Ethics & Governance</em>?"),
    "sub": ("AI 윤리기준·거버넌스를, 여러 품질검사장이 공통으로 지킬 등급 원칙과 책임 체계로 풀어봤어요.",
            "AI ethics and governance, told as a story about a shared grading charter that every inspection station follows — principles and accountability together."),
    "panels": [
        {"svg": P1, "alt": ("세 검사장이 저마다 다른 등급 기준을 씀 — 대충 통과, 무조건 불합격, 그날그날 다름", "Three stations each grade by a different rule — one lets everything pass, one fails almost everything, one changes day to day"),
         "caption": ("검사장마다 등급 기준이 제각각이에요.", "Every station grades by its own rule."),
         "small": ("같은 작물인데도 검사장에 따라 합격·불합격이 갈려요.", "The same produce passes at one station and fails at another.")},
        {"svg": P2, "alt": ("농부가 왜 자기 작물만 불합격인지 묻지만, 선별기 조작원도 진땀을 흘리며 설명하지 못함", "A farmer asks why only their produce failed, but the sweating operator can't explain it either"),
         "caption": ("기준이 안 적히면, 아무도 설명하지 못해요.", "Without a written standard, nobody can explain it."),
         "small": ("왜 그런 등급인지, 누가 책임지는지도 알 수 없어요.", "Why the grade came out that way, and who's responsible, stays a mystery.")},
        {"svg": P3, "hero": True, "alt": ("검수반장과 조작원 사이에 걸린 큰 등급 원칙판에 공정성·설명가능성·책임소재·사람 재검토가 적혀 있음", "A large grading charter between the inspector and the operator lists fairness, explainability, accountability, and human review"),
         "caption": ("모든 검사장이 함께 지킬 등급 원칙과 책임 체계예요.", "A shared charter every station follows — principles and accountability together."),
         "small": ("개별 선별기 하나의 규칙이 아니라, 검사장 전체가 따르는 틀이에요.", "Not one sorter's private rule — the frame the whole station operates inside."),
         "tricks": (4, [
             (FAIR_I, ("공정성 지키기", "Keep it fair"), ("작물 종류로 차별 않기", "no bias by produce type"), "calm"),
             (EXPLAIN_I, ("설명 가능하게 하기", "Make it explainable"), ("등급 이유를 남겨요", "recording why a grade was given")),
             (OWN_I, ("책임소재 분명히 하기", "Fix accountability"), ("오판 시 누가 맡는지요", "who owns a bad call"), "warm"),
             (APPEAL_I, ("사람이 재검토하기", "Allow human review"), ("이의 제기 통로를 열어요", "opening a path to appeal")),
         ])},
        {"svg": svg(300, sky(300) + person(140, 160, s=0.75, face=EYES, **FARMER) + label(140, 255, "⟦이의 제기|files an appeal⟧", 11, "var(--muted)")
                 + gradeboard(260, 60, 260, 170, "⟦재검토 절차|REVIEW PROCESS⟧", ("⟦①근거 기록 확인|① check the recorded reason⟧", "⟦②사람이 다시 봄|② a person looks again⟧", "⟦③등급 수정 또는 유지|③ revise or confirm the grade⟧"), 1.0)
                 + person(640, 160, s=0.75, face=SMILE, **INSPECTOR) + label(640, 255, "⟦검수반장이 재검토|the inspector re-reviews⟧", 11, "var(--muted)")),
         "alt": ("농부가 이의를 제기하면 근거 기록을 확인하고 사람이 다시 본 뒤 등급을 수정하거나 유지하는 절차", "When a farmer appeals, the recorded reason is checked, a person re-reviews, and the grade is revised or confirmed"),
         "caption": ("원칙판은 이의 제기 절차까지 구체적으로 정해 둬요.", "The charter spells out the appeal process in concrete steps."),
         "small": ("등급을 매긴 근거가 남아 있어야, 재검토도 가능해요.", "Review only works if the reason for the grade was recorded in the first place.")},
        {"svg": svg(340, '<rect width="380" height="340" fill="var(--good-soft)"/><rect x="380" width="380" height="340" fill="var(--accent-soft)"/>'
                 + gradeboard(60, 40, 270, 90, "⟦원칙판 — 벽에 걸려 있음|CHARTER — ON THE WALL⟧", ("⟦작물 종류로 차별 않기|no bias by produce type⟧",))
                 + person(150, 170, s=0.6, face=SMILE, **INSPECTOR) + label(150, 265, "⟦지키면 작동해요|it works when it's followed⟧", 11, "var(--ink)")
                 + person(560, 170, s=0.6, face=FROWN, **OPERATOR)
                 + label(560, 265, "⟦원칙판을 안 보고 그냥 등급 매겼어요|graded without even looking at it⟧", 11, "var(--bad)")
                 + label(380, 305, '⟦<a href="aigovernance-ko.html">주방 세계의 AI 거버넌스</a>는 보안 운영 각도를, 여긴 윤리·규제 준수 각도를 봐요|<a href="aigovernance-en.html">the kitchen world\'s AI governance</a> looks from a security-ops angle — this page looks from an ethics and regulatory-compliance angle⟧', 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 검수반장이 원칙판을 지켜 등급이 잘 작동함. 오른쪽: 조작원이 원칙판을 안 보고 그냥 등급을 매김", "Left: the inspector follows the charter and grading works. Right: the operator grades without even consulting it"),
         "caption": ("원칙판이 있어도, 안 지키면 소용없어요.", "Having a charter doesn't help if nobody follows it."),
         "small": ("이 페이지는 윤리·규제 준수 각도, 주방 세계 쪽은 보안 운영 각도예요.", "This page takes the ethics/compliance angle; the kitchen world's page takes the security-ops angle.")},
    ],
    "summary": (("<b>AI 윤리기준·거버넌스</b> = 모든 검사장이 함께 지킬 <b>공정성·설명가능성·책임소재</b>를 정한 등급 원칙판.",
                 "<b>AI ethics & governance</b> = a shared grading charter spelling out <b>fairness, explainability, and accountability</b> for every station."),
                ("AI 윤리기준·거버넌스는 조직이 AI를 개발·운영하는 전 과정에서 공정성, 투명성(설명가능성), 책임소재, 사람의 재검토 권리를 보장하도록 정한 정책·규범 체계예요. 기술사 시험에서는 OECD AI 원칙, EU AI Act, 국내 AI기본법의 윤리·신뢰성 요건과 함께 다뤄져요. 보안 사고 대응에 초점을 둔 운영 거버넌스(AI 보안 거버넌스)와 달리, 이쪽은 사회적 수용성·규제 준수·이해관계자 신뢰라는 더 넓은 틀을 다뤄요.",
                 "AI ethics and governance is the policy and normative framework ensuring fairness, transparency (explainability), accountability, and a right to human review throughout how an organization builds and operates AI. In Korean PE exams it's discussed alongside the OECD AI Principles, the EU AI Act, and the ethics/trustworthiness requirements of Korea's AI Basic Act. Unlike security-operations governance focused on incident response, this is the wider frame of social acceptability, regulatory compliance, and stakeholder trust.")),
    "glossary": [
        ("AI 윤리기준", "AI ethics standard", ("공통 등급 원칙판.", "The shared grading charter."), ("모든 검사장이 함께 지켜요.", "Every station follows it together.")),
        ("AI 거버넌스(보안 각도)", "AI governance (security angle)", ("주방 세계의 규칙판.", "The kitchen world's rules board."), ('운영·보안 중심 각도는 여기서. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'The operations/security-focused angle lives here. → <a href="aigovernance-en.html">The Kitchen Rules Board</a>')),
        ("설명가능성(XAI)", "Explainability (XAI)", ("등급을 매긴 이유를 남기는 일.", "Recording the reason behind a grade."), ("이유 없이 매긴 등급은 이의 제기조차 못 해요.", "A grade with no recorded reason can't even be appealed.")),
        ("공정성", "Fairness", ("작물 종류로 차별하지 않는 것.", "Not discriminating by produce type."), ('편향은 씨앗 단계에서도 섞여 들어와요. → <a href="aidataqual-ko.html">상한 씨앗으로 가르친 선별기</a>', 'Bias can creep in as early as the seed stage. → <a href="aidataqual-en.html">A Sorter Trained on Rotten Seed</a>')),
        ("AI 리스크 관리 프레임워크", "AI risk management framework", ("원칙을 실제 절차로 바꾸는 작업 지도.", "The working map that turns principles into real procedure."), ('원칙판을 실행에 옮기는 방법은 따로 있어요. → <a href="airiskframe-ko.html">검사장 전체를 도는 운영 지도</a>', 'How the charter gets carried out, in a page of its own. → <a href="airiskframe-en.html">The Operations Map That Walks the Whole Station</a>')),
        ("인공지능기본법", "AI Basic Act", ("나라가 정한 최소 등급 기준.", "The minimum grading rule the country itself sets."), ('고영향 AI는 법으로 더 엄격히 다뤄요. → <a href="aibasiclaw-ko.html">나라가 정한 최소 등급 기준</a>', 'High-impact AI gets stricter legal treatment. → <a href="aibasiclaw-en.html">The Minimum Grading Rule the Country Itself Sets</a>')),
        ("사람 재검토", "Human review", ("농부의 이의 제기 통로.", "The farmer's path to appeal."), ("원칙판이 보장하는 네 가지 중 하나예요.", "One of the four things the charter guarantees.")),
        ("이해관계자 신뢰", "Stakeholder trust", ("농부·손님·나라 모두가 검사장을 믿는 것.", "Farmers, customers, and the country all trusting the station."), ("윤리기준이 궁극적으로 지키려는 것이에요.", "What the ethics standard is ultimately protecting.")),
    ],
}
