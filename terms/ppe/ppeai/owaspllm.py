from _draw import *
from _world import *

# 1. 검사장 입구에 낯선 게시판이 붙었어요
P1 = svg(300, sky(300)
         + gradeboard(280, 50, 220, 130, "⟦업계 표준 위험 목록|INDUSTRY RISK LIST⟧", ("⟦LLM01 ~ LLM10|LLM01 ~ LLM10⟧", "⟦??? ???|??? ???⟧"), 0.9)
         + person(170, 190, s=0.8, face=EYES, **INSPECTOR)
         + bubble(40, 120, 190, 44, "⟦이 번호들은 다 뭐예요?|what are all these numbers?⟧", 11, "var(--panel)", "var(--line)", "right")
         + label(380, 280, "⟦우리 검사장만의 사고 기록이 아니라, 업계 전체가 모은 목록이래요|not just our station's own records — a list the whole industry put together⟧", 12, "var(--ink)"))

# 2. 검사장마다 같은 사고를 다른 이름으로 불러요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + person(140, 170, s=0.7, face=FROWN, **OPERATOR) + bubble(60, 90, 190, 40, "⟦저흰 이걸 \'쪽지 사고\'라 불러요|we call it a note incident⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(400, 170, s=0.7, face=FROWN, **CHEATER) + bubble(320, 90, 190, 40, "⟦저흰 \'끼워넣기 문제\'라 불러요|we call it an insertion problem⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(650, 170, s=0.7, face=FROWN, **TEACHER) + bubble(560, 90, 190, 40, "⟦저흰 또 다른 이름으로...|we\'ve got yet another name...⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 290, "⟦이름이 다 다르면, 사고를 비교하거나 함께 배울 수가 없어요|different names for the same thing means no comparing, no learning together⟧", 12, "var(--ink)"))

# 3. OWASP LLM Top 10 = 업계가 합의한 공통 위험 목록판 (hero)
P3 = svg(360, sky(360)
         + gradeboard(260, 50, 260, 190, "⟦LLM Top 10 게시판|LLM TOP 10 BOARD⟧",
                      ("⟦LLM01 쪽지 끼워넣기|LLM01 note insertion⟧", "⟦LLM02 안전하지 않은 출력|LLM02 unsafe output⟧",
                       "⟦LLM03 재료 오염|LLM03 tainted ingredients⟧", "⟦... LLM10 레시피 훔치기|... LLM10 recipe theft⟧"), 0.95)
         + person(150, 200, s=0.8, face=SMILE, **INSPECTOR)
         + label(380, 30, "⟦OWASP LLM Top 10 = 여러 검사장의 사고를 모아 번호를 매긴 업계 공용 목록|the OWASP LLM Top 10 = incidents from many stations, pooled and numbered into one shared list⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦각 번호는 '이름표'일 뿐, 자세한 내용은 따로 찾아봐야 해요|each number is just a label — the detail lives elsewhere⟧", 12, "var(--muted)"))

CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
LINK_I = icon('<circle cx="24" cy="24" r="12" fill="none" stroke="var(--accent)" stroke-width="5"/><circle cx="40" cy="40" r="12" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M30 30 l4 4" stroke="var(--accent)" stroke-width="5"/>')
FLAG_I = icon('<rect x="18" y="8" width="4" height="48" fill="#5A3B22"/><path d="M22 10 h26 l-8 10 l8 10 h-26 z" fill="var(--bad)"/>')

# 4. Top 10 각 항목은 더 자세한 이야기로 연결돼요
P4 = svg(360, sky(360)
         + gradeboard(40, 20, 680, 320, "⟦Top 10 → 자세한 이야기로|TOP 10 → THE FULL STORY⟧",
                      ('⟦LLM01 쪽지 끼워넣기 → <a href="promptinjection-ko.html">주문서 뒤 몰래 쪽지</a>|LLM01 → <a href="promptinjection-en.html">the note slipped behind the order</a>⟧',
                       '⟦LLM02 안전하지 않은 출력 → <a href="unsafeoutput-ko.html">검증 없이 내보낸 접시</a>|LLM02 → <a href="unsafeoutput-en.html">the dish served unchecked</a>⟧',
                       '⟦LLM03 학습데이터 오염 → <a href="datapoisoning-ko.html">상한 재료 섞기</a>|LLM03 → <a href="datapoisoning-en.html">tainted ingredients mixed in</a>⟧',
                       '⟦LLM04 과부하 공격 → <a href="llmdos-ko.html">끝없는 주문 폭탄</a>|LLM04 → <a href="llmdos-en.html">the endless order bomb</a>⟧',
                       '⟦LLM05 공급망 취약점 → <a href="aibom-ko.html">재료 출처 장부</a>|LLM05 → <a href="aibom-en.html">the ingredient-origin ledger</a>⟧',
                       '⟦LLM06 민감정보 유출 → <a href="promptleak-ko.html">레시피북 몰래 베끼기</a>|LLM06 → <a href="promptleak-en.html">quietly copying the recipe book</a>⟧',
                       '⟦LLM07 위험한 도구 연결 → <a href="toolpermission-ko.html">허락 없는 칼서랍</a>|LLM07 → <a href="toolpermission-en.html">the unapproved knife drawer</a>⟧',
                       '⟦LLM08 과도한 자율행동 → <a href="excessiveagency-ko.html">너무 많이 맡긴 심부름</a>|LLM08 → <a href="excessiveagency-en.html">the errand given too much freedom</a>⟧',
                       '⟦LLM09 과신뢰 → <a href="hallucination-ko.html">모르는데 자신 있게 답함</a>|LLM09 → <a href="hallucination-en.html">answering confidently while unsure</a>⟧',
                       '⟦LLM10 모델 도난 → <a href="modelextraction-ko.html">선별 기준 통째로 베끼기</a>|LLM10 → <a href="modelextraction-en.html">copying the whole sorting rulebook</a>⟧'), 0.72))

# 5. 게시판 자체가 막아주지 않아요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **INSPECTOR) + gradeboard(110, 190, 160, 50, "⟦목록 확인|CHECK LIST⟧", ("⟦10개를 다 살펴봤나|checked all 10?⟧",), 0.65)
         + label(190, 270, "⟦빠뜨린 게 없는지 체크만 해줘요|it only helps you check for gaps⟧", 11, "var(--ink)")
         + person(570, 125, s=0.8, face=SMILE, **OPERATOR) + label(570, 265, "⟦막는 방법은 각 항목 페이지에 있어요|the actual defenses live on each item's own page⟧", 11, "var(--ink)")
         + label(380, 300, "⟦게시판은 '지도'일 뿐, 길은 각자 페이지에서 걸어야 해요|the board is only a map — you still walk each road on its own page⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "owaspllm", "order": 14,
    "title": ("검사장 입구의 업계 공용 위험 게시판", "The Shared Industry Risk Board at the Entrance"),
    "h1": ("<em>OWASP LLM 보안 위협 Top 10</em>이/가 뭐예요?", "What is the <em>OWASP Top 10 for LLMs</em>?"),
    "sub": ("OWASP LLM Top 10을, 검사장마다 다른 이름으로 부르던 사고를 업계가 공용 번호판으로 정리한 게시판 이야기로 풀어봤어요.",
            "The OWASP Top 10 for LLMs, told as a story about an industry-wide board that gave shared numbers to incidents every station used to call by a different name."),
    "panels": [
        {"svg": P1, "alt": ("검사장 입구에 'LLM01~LLM10'이라 적힌 낯선 게시판이 붙고, 검수반장이 이게 뭔지 궁금해함", "An unfamiliar board reading LLM01 through LLM10 appears at the station entrance, and the inspector wonders what it is"),
         "caption": ("검사장 입구에 낯선 게시판이 붙었어요.", "An unfamiliar board appeared at the entrance."),
         "small": ("우리 검사장만의 기록이 아니라, 업계 전체가 모은 목록이래요.", "Not just our own records — a list the whole industry put together.")},
        {"svg": P2, "alt": ("세 검사장이 같은 종류의 사고를 각자 다른 이름(쪽지 사고, 끼워넣기 문제 등)으로 부름", "Three stations each call the same kind of incident by a different name — a note incident, an insertion problem, and so on"),
         "caption": ("검사장마다 같은 사고를 다른 이름으로 불러요.", "Every station calls the same incident by a different name."),
         "small": ("이름이 다 다르면 비교하거나 함께 배울 수가 없어요.", "Different names for the same thing means no comparing, no learning together.")},
        {"svg": P3, "hero": True, "alt": ("업계 공용 LLM Top 10 게시판에 번호가 매겨진 위험 목록이 붙어 있음", "An industry-shared LLM Top 10 board lists numbered risks"),
         "caption": ("OWASP LLM Top 10은 업계가 합의한 공통 위험 목록판이에요.", "The OWASP LLM Top 10 is a shared, industry-agreed risk list."),
         "small": ("각 번호는 이름표일 뿐, 자세한 내용은 따로 찾아봐야 해요.", "Each number is just a label — the detail lives elsewhere."),
         "tricks": (4, [
             (CHECK_I, ("공용 번호로 부르기", "Call it by a shared number"), ("검사장이 달라도 같은 말", "the same words across every station"), "calm"),
             (CLOCK_I, ("주기적으로 갱신하기", "Update it periodically"), ("새 사고가 쌓이면 목록도 바뀌어요", "new incidents reshape the list")),
             (LINK_I, ("상세 페이지로 연결하기", "Link out to the detail"), ("목록은 지도, 설명은 따로", "the list is the map; the detail lives elsewhere"), "warm"),
             (FLAG_I, ("점검용 안내일 뿐", "Just a checklist"), ("자동으로 막아주진 않아요", "it doesn't block anything by itself")),
         ])},
        {"svg": P4, "alt": ("Top 10의 LLM01부터 LLM10까지 각 항목이 각각의 자세한 사고 이야기 페이지로 화살표 연결됨", "Each LLM01-through-LLM10 item on the Top 10 arrows out to its own detailed incident-story page"),
         "caption": ("Top 10 각 항목은 더 자세한 이야기로 연결돼요.", "Each Top 10 item links out to its own fuller story."),
         "small": ("이 페이지는 목록 자체를 설명해요 — 각 항목의 속사정은 연결된 페이지에서 봐요.", "This page explains the list itself — the details of each item live on the linked page.")},
        {"svg": P5, "alt": ("왼쪽: 검수반장이 목록으로 빠뜨린 항목만 체크함. 오른쪽: 실제로 막는 방법은 각 항목 페이지에 있음", "Left: the inspector only checks the list for gaps. Right: the real defenses live on each item's own page"),
         "caption": ("게시판 자체가 막아주지 않아요.", "The board itself doesn't block anything."),
         "small": ("지도일 뿐이에요 — 길은 각자 페이지에서 걸어야 해요.", "It's only a map — you still have to walk each road on its own page.")},
    ],
    "summary": (("<b>OWASP LLM Top 10</b> = 여러 검사장(현장)의 사고를 모아 <b>업계가 합의한 공용 번호</b>로 정리한 <b>위험 목록판</b>. 목록 자체는 지도일 뿐, 각 항목의 실제 대응은 그 번호가 가리키는 페이지에 있어요.",
                 "The <b>OWASP Top 10 for LLMs</b> = a <b>shared risk board</b> that pools incidents from many sites into <b>industry-agreed numbers</b>. The list itself is only a map — the real defenses live on the page each number points to."),
                ("OWASP Top 10 for LLM Applications는 OWASP 재단이 커뮤니티 사례를 모아 매년 갱신하는 'LLM01~LLM10' 표준 위협 분류 목록이에요. 프롬프트 인젝션, 안전하지 않은 출력 처리, 학습데이터 오염, 서비스 거부, 공급망 취약점, 민감정보 유출, 위험한 플러그인/도구 설계, 과도한 자율행동, 과신뢰, 모델 도난이 대표 항목이에요. 이 목록의 가치는 '공용 언어'를 제공한다는 데 있고, 실제 방어 방법은 각 항목이 가리키는 세부 자료(가이드라인, 본 사이트의 개별 용어 페이지 등)에서 다뤄요.",
                 "The OWASP Top 10 for LLM Applications is a standardized LLM01-LLM10 threat classification, updated yearly from community-reported cases. Its named items include prompt injection, insecure output handling, training data poisoning, denial of service, supply chain vulnerabilities, sensitive information disclosure, insecure plugin/tool design, excessive agency, overreliance, and model theft. The list's value is in giving everyone a shared vocabulary — the actual defenses live in the detailed material (guidelines, or this site's own per-term pages) that each item points to.")),
    "glossary": [
        ("LLM01 프롬프트 인젝션", "LLM01 Prompt Injection", ("주문서 뒤에 몰래 끼운 쪽지.", "The note slipped behind the order."), ('→ <a href="promptinjection-ko.html">쪽지 사고 자세히 보기</a>', '→ <a href="promptinjection-en.html">see the note incident in full</a>')),
        ("LLM03 학습데이터 오염", "LLM03 Training Data Poisoning", ("상한 작물을 재료창고에 섞어 넣기.", "Tainted crops mixed into the pantry."), ('→ <a href="datapoisoning-ko.html">재료 오염 자세히 보기</a>', '→ <a href="datapoisoning-en.html">see the tainted-ingredient story</a>')),
        ("LLM06 민감정보 유출", "LLM06 Sensitive Info Disclosure", ("레시피북을 몰래 베껴가기.", "Quietly copying the recipe book."), ('→ <a href="promptleak-ko.html">유출 자세히 보기</a>', '→ <a href="promptleak-en.html">see the leak in full</a>')),
        ("LLM08 과도한 자율행동", "LLM08 Excessive Agency", ("너무 많이 맡긴 심부름.", "An errand given too much freedom."), ('→ <a href="excessiveagency-ko.html">자세히 보기</a>', '→ <a href="excessiveagency-en.html">see it in full</a>')),
        ("LLM10 모델 도난", "LLM10 Model Theft", ("선별 기준을 통째로 베껴가기.", "Copying the whole sorting rulebook."), ('→ <a href="modelextraction-ko.html">자세히 보기</a>', '→ <a href="modelextraction-en.html">see it in full</a>')),
        ("AI 거버넌스", "AI Governance", ("농장 운영 전체 규칙판.", "The whole-farm operating rules board."), ('Top 10은 거버넌스가 참고하는 목록 중 하나예요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'The Top 10 is one list governance leans on. → <a href="aigovernance-en.html">the rules board on the wall</a>')),
        ("레드팀", "Red Team", ("불시에 게시판 항목을 실제로 찔러보는 사람.", "Someone who actually pokes at each board item, unannounced."), ('→ <a href="airedteam-ko.html">AI 전용 위생 검사관</a>', '→ <a href="airedteam-en.html">the AI-specific inspector</a>')),
        ("모델 카드", "Model Card", ("선별기 한 대의 설명서.", "The spec sheet for one sorter."), ('Top 10 점검 결과를 적어두는 칸이 있기도 해요. → <a href="modelcard-ko.html">자세히 보기</a>', 'Sometimes has a field for noting Top 10 check results. → <a href="modelcard-en.html">see it in full</a>')),
    ],
}
