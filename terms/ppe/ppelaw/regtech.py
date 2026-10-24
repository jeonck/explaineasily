"""레그테크(RegTech)."""
from _draw import *
from _world import *

COLLECT_I = icon('<rect x="10" y="30" width="14" height="20" rx="2" fill="var(--line)"/><rect x="26" y="20" width="14" height="30" rx="2" fill="var(--line)"/><rect x="42" y="12" width="14" height="38" rx="2" fill="var(--line)"/><path d="M17 20 L33 12 L49 6" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/>')
MATCH_I = icon('<rect x="8" y="12" width="20" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 20 h8 M14 28 h8" stroke="#142033" stroke-width="2"/><path d="M36 20 l8 8 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
ALERT_I = icon('<path d="M32 10 L54 48 H10 Z" fill="var(--bad)"/><rect x="29" y="24" width="6" height="12" fill="#fff"/><circle cx="32" cy="40" r="3" fill="#fff"/>')
HUMAN_I = icon('<circle cx="32" cy="18" r="10" fill="var(--good)"/><rect x="18" y="32" width="28" height="22" rx="6" fill="var(--good)"/><path d="M26 44 l6 6 l12 -12" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 규칙이 너무 많이 쌓였어요
P1 = svg(390, sky(390)
         + rulesboard(60, 40, 150, 220, "⟦라이선스|LICENSE⟧", ("⟦출처 표기|credit⟧",), 0.75)
         + rulesboard(230, 60, 150, 200, "⟦망중립|NEUTRAL⟧", ("⟦차별 금지|no bias⟧",), 0.75)
         + rulesboard(400, 40, 150, 220, "⟦품질|QUALITY⟧", ("⟦8대 기준|8 traits⟧",), 0.75)
         + rulesboard(570, 60, 150, 200, "⟦안전|SAFETY⟧", ("⟦등급 기준|grading⟧",), 0.75)
         + person(380, 290, s=0.7, face=SWEAT + EYES, **TEACHER)
         + label(380, 18, "⟦규칙이 해를 거듭할수록 너무 많이 쌓였어요|the rules have piled up, year after year⟧", 13, "var(--ink)", cls="d"))

# 2. 사람이 손으로 다 확인하기엔 너무 늦어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(230, 150, s=0.85, face=SWEAT + EYES, **TEACHER) + bubble(100, 60, 260, 50, "⟦반마다 서류를 일일이 손으로 확인하다 지쳤어요|exhausted from checking every class's paperwork by hand⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(590, 150, s=0.75, face=FROWN, **STUDENT) + label(590, 250, "⟦저희 반, 벌써 두 달째 규칙을 어기고 있었어요|our class had been breaking a rule for two months already⟧", 11, "var(--bad)")
         + label(380, 285, "⟦손으로 확인하면 느리고, 어긴 걸 늦게 알아채요|checking by hand is slow — violations surface far too late⟧", 12, "var(--ink)", cls="d"))

# 3. 레그테크 = 자동 검사기로 규칙 준수를 실시간으로 확인하는 기술 (hero)
P3 = svg(360, sky(360)
         + label(380, 26, "⟦레그테크 = 자동 검사기로 규칙 준수를 실시간으로 확인하는 기술|RegTech = technology that checks rule-following in real time, with an automatic checker⟧", 13, "var(--ink)", cls="d")
         + checkmachine(380, 150, 1.6)
         + rulesboard(70, 220, 140, 110, "⟦라이선스|LICENSE⟧", ("⟦✓ 통과|✓ pass⟧",), 0.75) + rulesboard(230, 230, 140, 100, "⟦품질|QUALITY⟧", ("⟦✓ 통과|✓ pass⟧",), 0.75)
         + rulesboard(400, 230, 140, 100, "⟦안전|SAFETY⟧", ("⟦△ 확인중|△ checking⟧",), 0.75) + rulesboard(560, 220, 140, 110, "⟦데이터|DATA⟧", ("⟦✓ 통과|✓ pass⟧",), 0.75)
         + person(150, 140, s=0.8, face=EYES, **TEACHER) + person(610, 140, s=0.8, face=SMILE, **REP)
         + label(380, 345, "⟦흩어진 규칙판 여러 개를 동시에, 바로바로 대조해요|checks many scattered rule boards at once, right away⟧", 11, "var(--muted)"))

# 4. 레그테크가 하는 네 단계
P4 = svg(300, sky(300, ground=False)
         + rulesboard(60, 30, 640, 240, "⟦레그테크가 하는 일|WHAT REGTECH DOES⟧",
                      ("⟦1. 흩어진 기록을 자동으로 모으기|1. automatically gather scattered records⟧",
                       "⟦2. 규칙판과 바로 대조하기|2. check them against the rule board right away⟧",
                       "⟦3. 어긋나면 바로 알리기|3. flag a mismatch immediately⟧",
                       "⟦4. 최종 판단은 사람이 하기|4. a human still makes the final call⟧"), 1.0, hl=2)
         + label(380, 288, "⟦기계가 거르고, 사람이 결정해요|the machine filters — the person decides⟧", 12, "var(--ink)", cls="d"))

# 5. 레그테크도 모든 걸 다 잡아내진 못해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + checkmachine(190, 140, 1.0) + label(190, 250, "⟦알고 있는 규칙은 빠르게 잡아내요|known rules get caught fast⟧", 11, "var(--ink)")
         + person(570, 140, s=0.8, face=EYES, **TEACHER) + label(570, 250, "⟦처음 보는 종류의 위반은 여전히 사람 몫이에요|a never-seen-before violation is still a human's job⟧", 11, "var(--ink)")
         + label(380, 285, "⟦규칙을 만드는 것과, 지키는지 확인하는 것은 다른 일이에요|making a rule and checking whether it's kept are two different jobs⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "regtech", "order": 21,
    "title": ("흩어진 규칙판을 한꺼번에 대조하는 자동 검사기", "The Automatic Checker That Cross-Checks Every Rule Board at Once"),
    "h1": ("<em>레그테크(RegTech)</em>가 뭐예요?", "What is <em>RegTech</em>?"),
    "sub": ("레그테크를, 해마다 쌓여만 가는 학교 규칙을 학생회가 자동 검사기로 실시간 확인하는 이야기로 풀어봤어요.",
            "RegTech, told as a story about the student council using an automatic checker to verify, in real time, a growing pile of school rules."),
    "panels": [
        {"svg": P1, "alt": ("라이선스·망중립·품질·안전 규칙판 네 개가 늘어서 있고, 선생님이 땀을 흘리며 지쳐 있음", "Four rule boards — license, neutrality, quality, safety — line up while a teacher sweats, exhausted"),
         "caption": ("규칙이 해를 거듭할수록 너무 많이 쌓였어요.", "The rules have piled up, year after year."),
         "small": ("규칙판 하나하나는 다 옳지만, 전부 손으로 보기엔 너무 많아요.", "Each rule board is reasonable alone — there are just too many to check by hand.")},
        {"svg": P2, "alt": ("선생님이 반마다 서류를 손으로 확인하다 지쳤다고 말하고, 학생은 두 달째 규칙을 어기고 있었다고 속상해함", "A teacher says they're exhausted from checking every class's paperwork by hand; a student is upset to learn their class had broken a rule for two months"),
         "caption": ("사람이 손으로 다 확인하기엔 너무 늦어요.", "Checking everything by hand is too slow to catch things in time."),
         "small": ("손으로 확인하면 느리고, 어긴 걸 늦게 알아채요.", "Checking by hand is slow — violations surface far too late.")},
        {"svg": P3, "hero": True, "alt": ("큰 자동 검사기가 라이선스·품질·안전·데이터 규칙판 네 개를 동시에 대조하며 선생님과 대표가 지켜봄", "A large automatic checker cross-checks four rule boards — license, quality, safety, data — at once, while a teacher and rep watch"),
         "caption": ("레그테크는 자동 검사기로 규칙 준수를 실시간으로 확인하는 기술이에요.", "RegTech is technology that checks rule-following in real time, with an automatic checker."),
         "small": ("흩어진 규칙판 여러 개를 동시에, 바로바로 대조해요.", "Checks many scattered rule boards at once, right away."),
         "tricks": (4, [
             (COLLECT_I, ("자동으로 모으기", "Automatically gather"), ("흩어진 기록을 손대지 않고 모아요", "gathers scattered records without lifting a hand"), "calm"),
             (MATCH_I, ("규칙판과 바로 대조", "Check against the board right away"), ("사람보다 훨씬 빠르게 비교해요", "compares far faster than a person could"), "warm"),
             (ALERT_I, ("이상 신호 포착", "Flag anomalies"), ("어긋나면 바로 알려줘요", "flags a mismatch immediately")),
             (HUMAN_I, ("최종 판단은 사람", "The final call is human"), ("기계는 거르고, 사람이 결정해요", "the machine filters, the person decides")),
         ])},
        {"svg": P4, "alt": ("레그테크가 기록 모으기 → 규칙판 대조 → 이상 신호 알림 → 사람의 최종 판단 네 단계로 이어진다는 기준표", "A board showing RegTech's four steps: gather records → check against the rule board → flag anomalies → a human's final call"),
         "caption": ("레그테크는 이 네 단계를 거쳐요.", "RegTech works through these four steps."),
         "small": ("기계가 거르고, 사람이 결정해요.", "The machine filters — the person decides.")},
        {"svg": P5, "alt": ("왼쪽: 자동 검사기가 알려진 규칙은 빠르게 잡아냄. 오른쪽: 선생님이 처음 보는 위반은 여전히 사람 몫이라고 말함", "Left: the automatic checker quickly catches known rules. Right: a teacher says a never-seen-before violation is still a human's job"),
         "caption": ("레그테크도 모든 걸 다 잡아내진 못해요.", "RegTech can't catch absolutely everything either."),
         "small": ("규칙을 만드는 것과, 지키는지 확인하는 것은 다른 일이에요.", "Making a rule and checking whether it's kept are two different jobs.")},
    ],
    "summary": (("<b>레그테크</b> = 흩어진 규칙(라이선스·품질·안전·데이터…)을 <b>자동 검사기</b>로 <b>실시간 대조</b>해, 어긋나면 <b>바로 알리고</b> 최종 판단은 사람에게 넘기는 기술.",
                 "<b>RegTech</b> = technology that <b>cross-checks scattered rules</b> (license, quality, safety, data...) with an <b>automatic checker</b>, <b>flags a mismatch right away</b>, and hands the final call to a person."),
                ("레그테크(Regulatory Technology)는 규제 준수(컴플라이언스)를 자동화하는 기술이에요. 여러 시스템의 기록을 자동 수집하고, 규제 기준과 실시간으로 대조해 이상 징후를 조기에 탐지함으로써, 사람이 모든 서류를 수작업으로 대조하던 방식보다 훨씬 빠르고 촘촘하게 위반을 찾아내요. 다만 알려진 패턴 기반의 탐지라 처음 보는 유형의 위반이나 애매한 판단은 여전히 사람의 몫이고, 오탐·누락 가능성도 남아 있어요.",
                 "RegTech (Regulatory Technology) automates regulatory compliance. It automatically gathers records across systems and checks them in real time against regulatory standards, catching anomalies far faster and more thoroughly than manual, document-by-document checking ever could. Still, because it detects known patterns, a never-before-seen type of violation or an ambiguous judgment call remains a human's job, and some risk of false positives or missed cases remains.")),
    "glossary": [
        ("레그테크", "RegTech", ("자동 검사기로 규칙 준수를 확인하는 기술.", "Technology that checks rule-following with an automatic checker."), ("규제와 기술(Regulation + Technology)의 합성어예요.", "A blend of \"regulation\" and \"technology.\"")),
        ("자동 규제준수", "Automated Compliance", ("손이 아니라 기계가 규정을 대조하는 것.", "Having a machine, not hands, check against the rules."), ("레그테크가 하는 핵심 작업이에요.", "The core job RegTech performs.")),
        ("실시간 모니터링", "Real-Time Monitoring", ("기록이 쌓이자마자 바로바로 확인하는 것.", "Checking records the moment they're created."), ("늦게 발견하던 위반을 조기에 잡아줘요.", "Catches violations early that used to surface late.")),
        ("이상탐지", "Anomaly Detection", ("평소와 다른 패턴을 자동으로 찾아내는 것.", "Automatically spotting a pattern that doesn't match the usual."), ("알려진 규칙 패턴 기반이라 완벽하진 않아요.", "Pattern-based, so it isn't foolproof.")),
        ("컴플라이언스", "Compliance", ("조직이 외부 규정을 지키는 상태 그 자체.", "An organization actually following external rules."), ('레그테크가 자동으로 확인해주는 대상이에요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'The very thing RegTech automatically verifies. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
        ("오픈소스 라이선스", "Open-Source License", ("레그테크가 자동으로 대조하는 규칙판 중 하나.", "One of the rule boards RegTech cross-checks automatically."), ('섞어 쓴 라이선스를 자동 검사기가 추적해요. → <a href="osslicense-ko.html">다 같이 쓰는 준비물 규칙 라벨</a>', 'An automatic checker tracks which licenses got mixed in. → <a href="osslicense-en.html">the rule tag on shared supplies</a>')),
        ("데이터 표준화", "Data Standardization", ("기록 형식이 같아야 자동 대조가 가능해요.", "Automatic cross-checking only works if record formats already match."), ('레그테크는 이 표준 위에서 작동해요. → <a href="datastd-ko.html">전교가 함께 쓰는 공통 기준표</a>', 'RegTech runs on top of this standard. → <a href="datastd-en.html">the shared standard the whole school uses</a>')),
        ("AI 거버넌스", "AI Governance", ("규칙판 자체를 어떻게 세울지 정하는 더 큰 원칙.", "The bigger set of principles for how the rule board itself gets written."), ('규칙을 \'확인\'하는 레그테크와, 규칙을 \'세우는\' 거버넌스는 서로 달라요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'RegTech checks rules; governance is the separate job of writing them. → <a href="aigovernance-en.html">the kitchen rules board</a>')),
    ],
}
