from _draw import *
from _world import *

# 1. 농부가 명부째로 선별기 조작원에게 넘겨요
P1 = svg(320, sky(320)
         + person(150, 170, s=0.8, face=SMILE, **FARMER)
         + gradeboard(260, 70, 220, 150, "⟦출하자 명부|GROWER LIST⟧", ("⟦김OO · 010-…|Kim · 010-…⟧", "⟦이OO · 010-…|Lee · 010-…⟧", "⟦주소·농지 위치|address · field site⟧"), 0.9)
         + person(560, 150, s=0.8, face=EYES, **OPERATOR)
         + label(560, 270, "⟦이대로 선별기 학습에 써도 되나요?|is it okay to use this as-is to train the sorter?⟧", 12, "var(--ink)")
         + label(380, 300, "⟦조작원은 작물 데이터만 올 줄 알았는데, 이름·연락처 같은 사람 정보까지 왔어요|the operator expected only crop data — but names and phone numbers came too⟧", 12, "var(--bad)"))

# 2. 검수반장이 법을 모르면 어긋난다고 경고해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 160, s=0.85, face=EYES, **TEACHER)
         + bubble(90, 70, 220, 46, "⟦이 명부로 선별 기준을 다시 짤게요|I\'ll retrain the sorting rules with this list⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 160, s=0.75, face=FROWN, **INSPECTOR)
         + bubble(435, 70, 305, 54, "⟦잠깐요, 동의 등 법적 근거 없이 쓰면 안 돼요|hold on — not without consent or another legal basis⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦작물 품질과 달리, 사람 정보는 동의 같은 법적 근거가 허용한 만큼만 쓸 수 있어요|unlike crop quality, people's info can only be used as far as a legal basis, like consent, allows⟧", 12, "var(--ink)"))

# 3. AI 개인정보보호(컴플라이언스) = 쓰기 전에 법령 체크리스트로 확인하고 서류로 남기는 일 (hero)
P3 = svg(360, sky(360)
         + person(400, 140, s=0.9, face=EYES, **INSPECTOR)
         + gradeboard(460, 60, 260, 170, "⟦법령 체크리스트|COMPLIANCE CHECKLIST⟧",
                      ("⟦① 왜 모으나 — 목적|① why collect — purpose⟧", "⟦② 법적 근거 있나 — 동의 등|② legal basis? — consent etc.⟧",
                       "⟦③ 언제까지 두나 — 보유기간|③ how long kept — retention⟧", "⟦④ 어디로 가나 — 국외이전|④ where it goes — transfer⟧"), 0.95)
         + person(160, 190, s=0.8, face=SMILE, **FARMER) + stamp2(260, 150, 0.8, ok=True)
         + label(380, 30, "⟦AI 개인정보보호 = 쓰기 전에 법령 체크리스트로 확인하고 서류로 남기는 일|AI data-privacy compliance = checking a legal checklist before use, and keeping the paperwork⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦이름을 기술로 가리는 것과는 또 다른, '허락과 서류'의 문제예요|a different problem from technically masking names — it's about permission and paperwork⟧", 12, "var(--muted)"))

# 4. 체크리스트 네 칸을 하나씩
CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CONSENT_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 44 l6 6 l12 -12" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M22 20 h20 M22 28 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
GLOBE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 32 h44 M32 10 v44 M16 18 q16 14 32 0 M16 46 q16 -14 32 0" stroke="var(--accent)" stroke-width="2.5" fill="none"/>')

P4 = svg(330, sky(330)
         + gradeboard(40, 40, 320, 240, "⟦명부 한 장의 여정|ONE LIST\'S JOURNEY⟧",
                      ("⟦수집 — 왜 모으는지 적어요|collect — write down why⟧", "⟦동의 — 농부가 허락해요|consent — the grower agrees⟧",
                       "⟦보관 — 정해둔 기간만|retain — only the set period⟧", "⟦파기/이전 — 끝나면 지우고, 이전은 요건 확인|dispose/transfer — delete when due; check rules⟧"), 1.0)
         + person(560, 160, s=0.8, face=EYES, **INSPECTOR) + stamp2(650, 130, 0.7, ok=True)
         + label(380, 305, "⟦이 네 단계가 전부 서류로 남아야 '감사'를 통과해요|all four steps must be on paper to pass an audit⟧", 12, "var(--ink)"))

# 5. 기술적 가리기와는 다른 일이에요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **INSPECTOR) + gradeboard(25, 180, 210, 60, "⟦허락·서류|PERMISSION⟧", ("⟦동의·보유기간·이전|consent · retention · transfer⟧",), 0.7)
         + label(190, 275, "⟦컴플라이언스는 '허락받았나, 적어뒀나'를 봐요|compliance asks: consented? written down?⟧", 11, "var(--ink)")
         + person(570, 125, s=0.8, face=SMILE, **OPERATOR) + label(570, 265, "⟦이름을 번호표로 가리는 건 기술의 몫이에요|masking names into tags is a technical job⟧", 11, "var(--ink)")
         + label(380, 300, "⟦AI 개인정보보호(법·감사)와 기술적 마스킹은 둘 다 갖춰야 하는 짝이에요|legal/audit privacy compliance and technical masking are a pair: you need both⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aiprivacyppe", "order": 13,
    "title": ("출하자 명부를 지키는 서류함", "The Paperwork Cabinet That Protects the Grower List"),
    "h1": ("<em>AI 개인정보보호</em>가 뭐예요?", "What is <em>AI Data-Privacy Compliance</em>?"),
    "sub": ("AI 개인정보보호(컴플라이언스)를, 작물과 함께 딸려온 출하자 명부를 법령 체크리스트로 확인하고 서류로 남기는 이야기로 풀어봤어요.",
            "AI data-privacy compliance, told as a story about checking a grower list — that rode along with the crops — against a legal checklist, and keeping the paperwork."),
    "panels": [
        {"svg": P1, "alt": ("농부가 출하자 명부(이름·연락처·농지 위치)를 선별기 조작원에게 통째로 넘김", "A grower hands over a whole list of names, phone numbers, and field locations to the sorter operator"),
         "caption": ("농부가 출하자 명부를 통째로 선별기 조작원에게 넘겨요.", "The grower hands the whole grower list to the sorter operator."),
         "small": ("조작원은 작물 데이터만 올 줄 알았는데, 이름·연락처 같은 사람 정보까지 왔어요.", "The operator expected only crop data — but names and phone numbers came too.")},
        {"svg": P2, "alt": ("훈련 교사가 명부로 선별 기준을 다시 짜려 하자, 검수반장이 동의 같은 법적 근거 없이는 법에 어긋난다고 경고함", "The trainer is about to retrain the sorter with the list, but the inspector warns that doing so with no legal basis, like consent, breaks the rules"),
         "caption": ("검수반장이 동의 같은 법적 근거 없이 명부를 쓰면 법에 어긋난다고 경고해요.", "The inspector warns that using the list with no legal basis, like consent, breaks the law."),
         "small": ("사람 정보는 작물과 달리, 동의 같은 법적 근거가 허용한 만큼만 쓸 수 있어요.", "Unlike crops, people's info can only be used as far as a legal basis, like consent, allows.")},
        {"svg": P3, "hero": True, "alt": ("검수반장이 법령 체크리스트를 들고 있고, 농부는 승인 도장을 받음", "The inspector holds a compliance checklist while the grower receives an approval stamp"),
         "caption": ("AI 개인정보보호는 쓰기 전에 법령 체크리스트로 확인하고 서류로 남기는 일이에요.", "AI data-privacy compliance means checking a legal checklist before use, and keeping the paperwork."),
         "small": ("이름을 기술로 가리는 것과는 또 다른, 허락과 서류의 문제예요.", "A different problem from technically masking names — it's about permission and paperwork."),
         "tricks": (4, [
             (CHECK_I, ("목적 적어두기", "Write down the purpose"), ("왜 모으는지부터 분명히", "be clear on why it's collected"), "calm"),
             (CONSENT_I, ("동의 받기", "Get consent"), ("농부가 직접 허락해요", "the grower agrees directly")),
             (CLOCK_I, ("보유기간 정하기", "Set a retention period"), ("기간이 끝나면 명부를 지워요", "delete the list once that period is over"), "warm"),
             (GLOBE_I, ("국외이전 확인하기", "Check cross-border transfer"), ("명부가 어느 나라로 가는지 알아야 해요", "you must know which country the list goes to")),
         ])},
        {"svg": P4, "alt": ("명부 한 장이 수집 → 동의 → 보관 → 파기/이전의 네 단계를 거치는 여정도", "A journey map of one list through collection, consent, retention, and disposal/transfer"),
         "caption": ("명부는 수집·동의·보관·파기/이전 네 단계를 하나씩 거쳐요.", "The list goes through four steps in turn: collection, consent, retention, and disposal/transfer."),
         "small": ("이 네 단계가 전부 서류로 남아야 감사를 통과해요.", "All four steps must be on paper to pass an audit.")},
        {"svg": P5, "alt": ("왼쪽: 검수반장이 허락·서류를 확인함. 오른쪽: 조작원이 이름을 번호표로 가리는 기술적 작업을 함", "Left: the inspector checks consent and paperwork. Right: the operator does the technical work of masking names into tags"),
         "caption": ("AI 개인정보보호는 기술적 가리기(마스킹)와는 다른 일이에요.", "AI data-privacy compliance is a different job from technical masking."),
         "small": ("법·감사 쪽 확인과 기술적 마스킹은 둘 다 갖춰야 해요.", "Legal/audit compliance and technical masking are both needed.")},
    ],
    "summary": (("<b>AI 개인정보보호(컴플라이언스)</b> = 선별기에 사람 정보를 넣기 전, <b>목적·법적 근거(동의 등)·보유기간·국외이전</b>을 <b>법령 체크리스트</b>로 확인하고 <b>서류로 남기는</b> 일.",
                 "<b>AI data-privacy compliance</b> = before feeding people's info into the sorter, checking <b>purpose, legal basis (such as consent), retention, and cross-border transfer</b> against a <b>legal checklist</b> and keeping the <b>paperwork</b>."),
                ("개인정보보호법·GDPR 등 관련 법령에 따라, AI 학습·추론에 개인정보를 쓸 때는 수집 목적의 명시, 동의나 정당한 이익 같은 법적 근거, 보유기간 설정, 국외 이전 요건(한국의 별도 동의·인증·동등성 인정, GDPR의 표준계약조항 등)을 확인하고, 법이 정한 대상이거나 위험이 크면 개인정보 영향평가(PIA)도 거쳐요. 기술적 마스킹·가명처리(비식별화)는 이 요건을 만족시키는 '수단' 중 하나이지, 컴플라이언스 자체를 대체하지 않아요. 가명정보는 통계작성·과학적 연구 등의 목적이면 동의 없이 처리할 수 있어요.",
                 "Under laws like Korea's PIPA or GDPR, using personal data for AI training or inference means stating the collection purpose, having a legal basis such as consent or legitimate interest, setting a retention period, and meeting cross-border transfer requirements (separate consent, certification, or adequacy in Korea; standard contractual clauses and others under GDPR) — plus a Privacy Impact Assessment where the law requires one or the risk is high. Technical masking and pseudonymization are one *means* of meeting these requirements — they don't replace compliance itself. Pseudonymized data can be processed without consent for purposes such as statistics or scientific research.")),
    "glossary": [
        ("개인정보보호법 · GDPR", "PIPA · GDPR", ("명부 같은 사람 정보를 어떻게 다룰지 정한 법.", "The law that governs how personal data like the list may be handled."), ("개인정보 수집·이용·제공의 조건을 정해요.", "Sets the conditions for collecting, using, and sharing personal data.")),
        ("동의", "Consent", ("농부가 직접 허락하는 서명.", "The grower's own signature of permission."), ("대표적인 법적 근거예요(정당한 이익 등 다른 근거도 있어요). 목적이 크게 바뀌면 보통 다시 받아요.", "The best-known legal basis (others, like legitimate interest, exist). If the purpose changes substantially, it's usually obtained again.")),
        ("보유기간", "Retention period", ("명부를 서류함에 두는 기한.", "How long the list stays in the cabinet."), ("기한이 지나면 지체 없이 파기해요. 다른 법이 보존을 요구하면 분리해 보관해요.", "Once it expires, dispose of it without delay; if another law requires keeping it, store it separately.")),
        ("국외이전", "Cross-border transfer", ("명부가 다른 나라 창고로 가는 일.", "The list traveling to a warehouse in another country."), ("별도 동의·인증 같은 요건이 붙어요(GDPR은 표준계약조항 등).", "Extra requirements apply, like separate consent or certification (standard contractual clauses and others under GDPR).")),
        ("개인정보 영향평가(PIA)", "Privacy Impact Assessment", ("개인정보를 많이 쓰는 작업 전에 미리 해보는 위험 점검.", "A risk check run before a job that uses a lot of personal data."), ("한국은 기준을 넘는 공공기관에 의무, 민간은 노력 의무예요. GDPR은 위험이 크면 요구해요.", "In Korea it's mandatory for public institutions above set thresholds and an effort duty for others; GDPR requires one for high-risk processing.")),
        ("가명정보", "Pseudonymized data", ("이름을 번호표로 바꾼 명부.", "The list with names swapped for tags."), ('기술적 마스킹의 결과물이에요. → <a href="aiprivacy-ko.html">앵무새에게 준 비밀 콩</a>', 'The result of technical masking. → <a href="aiprivacy-en.html">the secret beans we gave the parrot</a>')),
        ("AI 거버넌스", "AI Governance", ("농장 전체의 운영 규칙판.", "The operating rules board for the whole farm."), ('개인정보보호는 거버넌스의 한 축이에요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'Privacy compliance is one pillar of governance. → <a href="aigovernance-en.html">the rules board on the wall</a>')),
        ("AI 신뢰성", "AI Trustworthiness", ("등급판 전체 — 공정·안전·투명성까지.", "The whole certification board — fairness, safety, transparency too."), ('개인정보보호는 신뢰성을 이루는 조각 중 하나예요. → <a href="aitrust-ko.html">품질인증 등급판</a>', 'Privacy is one piece that makes up trustworthiness. → <a href="aitrust-en.html">the certification board</a>')),
    ],
}
