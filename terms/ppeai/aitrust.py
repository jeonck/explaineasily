from _draw import *
from _world import *

# 1. 품질인증마크를 받고 싶어요
P1 = svg(300, sky(300)
         + person(170, 170, s=0.85, face=EYES, **OPERATOR)
         + bin_(300, 230, 0.9, "⟦정확도 99%|99% ACCURACY⟧")
         + bubble(400, 90, 230, 50, "⟦정확도가 99%인데, 인증마크 받을 수 있나요?|we're at 99% accuracy — can we get the certification mark?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(650, 190, s=0.75, face=EYES, **INSPECTOR)
         + label(380, 280, "⟦숫자 하나만으론 '믿을 수 있는지' 다 말할 수 없어요|one number alone can't say whether it's really trustworthy⟧", 12, "var(--ink)"))

# 2. 정확도 뒤에 숨은 치우침과 약점
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + bin_(170, 230, 1.0, "⟦사과만 99%|APPLES 99%⟧") + bin_(300, 230, 0.6, "⟦배는?|PEARS?⟧")
         + person(460, 160, s=0.8, face=FROWN, **CHEATER) + produce(560, 190, 0.9, bad=True)
         + label(560, 240, "⟦흠집 하나로 선별기를 속여요|one small scratch fools the sorter⟧", 11, "var(--bad)")
         + label(380, 275, "⟦한쪽 품종에 치우치거나, 작은 흠집에도 쉽게 속는 선별기일 수 있어요|it might be biased toward one crop, or easily fooled by a tiny scratch⟧", 12, "var(--ink)"))

# 3. AI 신뢰성 = 정확도 + 공정성 + 강건성 + 설명가능성 + 책임소재를 모두 갖춘 인증 (hero)
P3 = svg(360, sky(360)
         + gradeboard(260, 40, 260, 230, "⟦품질인증 등급판|TRUST CERTIFICATION BOARD⟧",
                      ("⟦정확도 — 잘 맞히나|accuracy — gets it right⟧", "⟦공정성 — 치우치지 않나|fairness — no bias⟧",
                       "⟦강건성 — 흠집에 안 속나|robustness — resists tampering⟧", "⟦설명가능성 — 이유를 말하나|explainability — can explain why⟧",
                       "⟦책임소재 — 문제 생기면 누구 책임|accountability — who answers for it⟧"), 0.95)
         + person(120, 200, s=0.85, face=SMILE, **INSPECTOR) + stamp2(190, 150, 0.8, ok=True)
         + label(380, 25, "⟦AI 신뢰성 = 다섯 기준을 모두 통과해야 받는 품질인증|AI trustworthiness = certification earned only by passing all five criteria⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦정확도 하나만 높다고 받을 수 있는 등급이 아니에요|high accuracy alone doesn't earn this grade⟧", 12, "var(--muted)"))

FAIR_I = icon('<path d="M32 10 v40 M14 26 h36" stroke="var(--accent)" stroke-width="4"/><circle cx="14" cy="34" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="50" cy="34" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/>')
ROBUST_I = icon('<path d="M32 10 L52 20 V34 C52 46 44 54 32 58 C20 54 12 46 12 34 V20 Z" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M24 34 l6 6 l12 -14" stroke="var(--good)" stroke-width="3" fill="none"/>')
EXPLAIN_I = icon('<circle cx="32" cy="26" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M28 50 h8" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M32 36 v8" stroke="var(--accent)" stroke-width="4"/>')
OWNER_I = icon('<circle cx="32" cy="22" r="10" fill="var(--accent)"/><path d="M14 54 q18 -18 36 0" fill="none" stroke="var(--accent)" stroke-width="5"/>')

# 4. 다섯 기준을 하나씩 점검해요
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 680, 290, "⟦등급판 점검 결과|CERTIFICATION CHECK⟧",
                      ('⟦정확도 ✓ — 99% (단, 품종별로 따로 확인)|accuracy ✓ — 99% (checked per crop type too)⟧',
                       '⟦공정성 △ — 일부 품종에 치우침 발견 → 재조정|fairness △ — bias found toward one crop → rebalance⟧',
                       '⟦강건성 ✓ — 흠집 테스트 통과|robustness ✓ — passed tampering tests⟧',
                       '⟦설명가능성 ✓ — 등급 이유를 사람이 이해할 말로 제공|explainability ✓ — reasons given in plain words⟧',
                       '⟦책임소재 ✓ — 담당 조작원과 검수반장 서명|accountability ✓ — operator and inspector both signed⟧'), 0.9))

# 5. 한 번 받았다고 끝이 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **INSPECTOR) + stamp2(260, 110, 0.7, ok=True)
         + label(190, 240, "⟦오늘은 인증을 받았어요|today it's certified⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **FARMER) + bin_(650, 230, 0.7, "⟦새 품종|NEW CROP⟧")
         + label(570, 270, "⟦새 품종·새 상황이 오면 다시 점검해야 해요|a new crop or a new situation means checking again⟧", 11, "var(--ink)")
         + label(380, 282, "⟦AI 신뢰성은 한 번의 인증이 아니라, 계속 다시 확인하는 상태예요|AI trustworthiness isn't a one-time stamp — it's an ongoing, re-checked state⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aitrust", "order": 16,
    "title": ("정확도 하나로는 못 받는 품질인증 등급판", "The Certification Board That One Accuracy Number Can't Earn"),
    "h1": ("<em>AI 신뢰성</em>이/가 뭐예요?", "What is <em>AI Trustworthiness</em>?"),
    "sub": ("AI 신뢰성을, 정확도만으론 통과할 수 없는 품질인증 등급판 — 공정성·강건성·설명가능성·책임소재까지 다 보는 이야기로 풀어봤어요.",
            "AI trustworthiness, told as a story about a certification board that accuracy alone can't pass — one that also checks fairness, robustness, explainability, and accountability."),
    "panels": [
        {"svg": P1, "alt": ("조작원이 정확도 99%라며 인증마크를 요청하지만, 검수반장은 숫자 하나로는 부족하다고 함", "The operator asks for the certification mark citing 99% accuracy, but the inspector says one number isn't enough"),
         "caption": ("품질인증마크를 받고 싶어요.", "They want the certification mark."),
         "small": ("숫자 하나만으론 믿을 수 있는지 다 말할 수 없어요.", "One number alone can't say whether it's really trustworthy.")},
        {"svg": P2, "alt": ("사과엔 99% 정확하지만 배는 성적이 낮고, 몰래 섞는 사람이 흠집 하나로 선별기를 속임", "The sorter is 99% accurate on apples but weak on pears, and someone fools it with a single scratch"),
         "caption": ("정확도 뒤에 치우침과 약점이 숨어 있어요.", "Bias and weak spots hide behind the accuracy number."),
         "small": ("한쪽 품종에 치우치거나, 작은 흠집에도 쉽게 속는 선별기일 수 있어요.", "It might be biased toward one crop, or easily fooled by a tiny scratch.")},
        {"svg": P3, "hero": True, "alt": ("품질인증 등급판에 정확도·공정성·강건성·설명가능성·책임소재 다섯 항목이 적혀 있고, 검수반장이 도장을 들고 있음", "A certification board lists five items — accuracy, fairness, robustness, explainability, accountability — while the inspector holds a stamp"),
         "caption": ("AI 신뢰성은 다섯 기준을 모두 갖춰야 받는 인증이에요.", "AI trustworthiness is a certification earned only by meeting all five criteria."),
         "small": ("정확도 하나만 높다고 받을 수 있는 등급이 아니에요.", "High accuracy alone doesn't earn this grade."),
         "tricks": (4, [
             (FAIR_I, ("공정성 보기", "Check fairness"), ("품종마다 고르게 맞히나", "does it score evenly across crops?"), "calm"),
             (ROBUST_I, ("강건성 보기", "Check robustness"), ("일부러 흠집 내 테스트해요", "deliberately test with tampering")),
             (EXPLAIN_I, ("설명가능성 보기", "Check explainability"), ("왜 이 등급인지 말할 수 있나", "can it say why it scored this way?"), "warm"),
             (OWNER_I, ("책임소재 보기", "Check accountability"), ("문제 생기면 누가 답하나", "who answers when something goes wrong?")),
         ])},
        {"svg": P4, "alt": ("점검 결과표: 정확도 통과, 공정성은 치우침이 발견돼 재조정, 강건성·설명가능성·책임소재는 통과", "A results board: accuracy passes, fairness flags a bias needing rebalancing, robustness/explainability/accountability all pass"),
         "caption": ("다섯 기준을 하나씩 점검해요.", "The five criteria are checked one by one."),
         "small": ("하나라도 미흡하면 등급판 전체가 보류돼요.", "If even one falls short, the whole certification is put on hold.")},
        {"svg": P5, "alt": ("왼쪽: 오늘 인증을 받음. 오른쪽: 새 품종이 들어오면 다시 점검해야 함", "Left: it's certified today. Right: a new crop means checking all over again"),
         "caption": ("한 번 받았다고 끝이 아니에요.", "Getting certified once isn't the end."),
         "small": ("AI 신뢰성은 계속 다시 확인하는 상태예요.", "AI trustworthiness is an ongoing, re-checked state.")},
    ],
    "summary": (("<b>AI 신뢰성</b> = <b>정확도</b>만이 아니라 <b>공정성·강건성·설명가능성·책임소재</b>까지 모두 갖춰야 받는, 그리고 <b>계속 다시 점검해야 하는</b> 품질인증.",
                 "<b>AI trustworthiness</b> is a certification that needs <b>accuracy plus fairness, robustness, explainability, and accountability</b> all at once — and must be <b>re-checked continuously</b>."),
                ("Trustworthy AI는 OECD·EU AI Act 등에서 공통으로 다루는 개념으로, 성능(정확도)뿐 아니라 공정성(fairness, 편향 완화), 강건성(robustness, 적대적 공격·분포 밖 입력에 대한 내성), 설명가능성(explainability, XAI), 책임성(accountability, 거버넌스·인간 감독)을 함께 요구해요. 하나의 지표가 아니라 여러 축의 균형이고, 환경(데이터·사용처)이 바뀌면 재평가가 필요해요.",
                 "Trustworthy AI is a concept shared across frameworks like the OECD principles and the EU AI Act: beyond raw performance (accuracy), it requires fairness (bias mitigation), robustness (resilience to adversarial attacks and out-of-distribution input), explainability (XAI), and accountability (governance and human oversight). It is a balance across several axes rather than a single metric, and needs re-evaluation whenever the data or use context changes.")),
    "glossary": [
        ("공정성(Fairness)", "Fairness", ("품종마다 고르게 맞히는 성질.", "Scoring evenly across every crop."), ('치우침은 AI 세계의 기본 개념이에요. → <a href="bias-ko.html">편향이 뭐예요?</a>', 'Bias is a core AI concept. → <a href="bias-en.html">What is Bias?</a>')),
        ("강건성(Robustness)", "Robustness", ("작은 흠집에 안 속는 성질.", "Not being fooled by a tiny scratch."), ("적대적 예제 같은 공격에 버티는 힘이에요.", "The resilience that holds up against attacks like adversarial examples.")),
        ("설명가능성(XAI)", "Explainability", ("등급을 매긴 이유를 말할 수 있는 성질.", "Being able to say why a grade was given."), ("'이유 없이 믿어라'가 아니라 근거를 보여줘요.", "Shows the reasoning instead of asking for blind trust.")),
        ("책임성(Accountability)", "Accountability", ("문제가 생기면 답할 사람이 정해져 있는 것.", "Having someone designated to answer when things go wrong."), ('거버넌스 안에서 다뤄요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'Handled within governance. → <a href="aigovernance-en.html">the rules board on the wall</a>')),
        ("안전성 평가", "Safety Evaluation", ("출시 전 미리 해보는 위험 테스트.", "A risk test run before release."), ('이 분야의 전용 평가가 따로 있어요. → <a href="safetyeval-ko.html">자세히 보기</a>', 'This field has its own dedicated evaluation. → <a href="safetyeval-en.html">see it in full</a>')),
        ("AI 레드팀", "AI Red Team", ("불시에 흠집을 내보는 검사관.", "The inspector who tries tampering, unannounced."), ('강건성을 실제로 찔러보는 역할이에요. → <a href="airedteam-ko.html">AI 전용 위생 검사관</a>', 'The role that actually probes robustness. → <a href="airedteam-en.html">the AI-specific inspector</a>')),
        ("AI 개인정보보호", "AI Data-Privacy Compliance", ("출하자 명부를 지키는 서류함.", "The paperwork cabinet protecting the grower list."), ('신뢰성의 한 축이에요. → <a href="aiprivacyppe-ko.html">자세히 보기</a>', 'One pillar of trustworthiness. → <a href="aiprivacyppe-en.html">see it in full</a>')),
        ("OWASP LLM Top 10", "OWASP LLM Top 10", ("업계 공용 위험 게시판.", "The shared industry risk board."), ('신뢰성 점검에서 참고하는 목록 중 하나예요. → <a href="owaspllm-ko.html">자세히 보기</a>', 'One of the lists trustworthiness checks lean on. → <a href="owaspllm-en.html">see it in full</a>')),
    ],
}
