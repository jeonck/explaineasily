from _draw import *
from _world import *

# 1. 다 받아주는 주방장이 있어요 — 그런데 몰래 끼운 쪽지도 있어요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.75, face=SMILE, **CHEF)
         + ticket(240, 150, 0.9) + person(310, 190, s=0.65, face=SMILE, **GUEST)
         + label(275, 230, "⟦보통 주문|a normal order⟧", 11, "var(--muted)")
         + ticket(520, 150, 0.9, sneaky=True) + person(590, 190, s=0.65, face=FROWN, **SNEAK)
         + label(545, 250, "⟦뒤에 몰래 쪽지를 끼웠어요|a note is slipped in behind it⟧", 12, "var(--bad)", cls="d")
         + label(380, 295, "⟦이 주방은 손님이 시키는 대로 다 받아줘요|this kitchen takes any order exactly as written⟧", 13, "var(--ink)"))

# 2. 주방장은 글자만 보고 믿어요 — 누가 썼는지는 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=EYES, **CHEF) + recipebook(170, 95, 0.55)
         + ticket(330, 170, 0.8, sneaky=True) + bubble(260, 60, 220, 50, "⟦'그리고 레시피북도 보여줘' 라고 적혀 있네요, 그럼 보여드려야죠|it says show me the recipe book too — so I will⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 160, s=0.7, face=FROWN, **SNEAK) + label(560, 250, "⟦정말 쪽지를 쓴 사람은 숨어 있어요|whoever really wrote the note stays hidden⟧", 11, "var(--bad)")
         + label(380, 280, "⟦사람 주방장은 '이상한데?' 하고 의심하지만, 이 주방장은 글자만 믿어요|a human chef would get suspicious — this one only trusts the words⟧", 12, "var(--ink)"))

# 3. AI 보안 = 이 주방이 안전하고 믿을 수 있게 돌아가도록 지키는 일 (hero)
P3 = svg(360, sky(360)
         + pantry(40, 60, 0.62, w=160, h=90)
         + knifedrawer(230, 250, 0.72, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧"))
         + person(430, 150, s=0.8, face=EYES, **CHEF)
         + person(560, 190, s=0.6, face=SMILE, **TASTER) + dish(560, 140, 0.55)
         + person(650, 230, s=0.55, face=EYES, **INSPECTOR) + badge(690, 200, 0.7)
         + label(380, 30, "⟦AI 보안 = 이 주방을 안전하고 믿을 수 있게 지키는 일|AI Security = keeping this kitchen safe and trustworthy⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦재료·도구·레시피·접시, 모두 노려질 수 있어요|the pantry, the tools, the recipes, the dish — every part can be targeted⟧", 12, "var(--muted)"))

# 4. 공격이 노리는 지점은 네 군데예요
P4 = svg(330, sky(330)
         + board(40, 30, 320, 260, "⟦이 주방의 약점 지도|WEAK POINTS MAP⟧",
                 ("⟦① 주문서 — 몰래 끼운 쪽지|① orders — a note slipped in⟧",
                  "⟦② 재료창고 — 수상한 재료|② pantry — tainted ingredients⟧",
                  "⟦③ 칼서랍 — 허락 없는 심부름|③ knife drawer — unapproved errands⟧",
                  "⟦④ 레시피북 — 몰래 베껴가기|④ recipe book — quietly copied⟧"), 1.0)
         + ticket(480, 90, 0.75, sneaky=True) + pantry(560, 140, 0.5, w=140, h=80, bad_shelf=1)
         + knifedrawer(430, 260, 0.6, labels=("⟦?|?⟧", "⟦?|?⟧"))
         + recipebook(690, 230, 0.55)
         + label(380, 305, "⟦①~④ 모두 다음 페이지들에서 하나씩 풀어봐요|pages ① through ④ each get their own story next⟧", 12, "var(--ink)"))

# 5. 한 번 막았다고 끝이 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(140, 150, s=0.75, face=SMILE, **INSPECTOR) + badge(190, 110, 0.7)
         + label(190, 240, "⟦오늘 쪽지는 막았어요|today\'s note is blocked⟧", 11, "var(--ink)")
         + ticket(560, 150, 0.8, sneaky=True) + label(560, 240, "⟦내일은 더 그럴듯한 쪽지가 와요|tomorrow\'s note is more convincing⟧", 11, "var(--ink)")
         + label(380, 282, "⟦AI 보안은 '한 번 지키기'가 아니라 '계속 지켜보고 또 지키기'예요|AI security isn\'t a one-time fix — it\'s watching and defending again and again⟧", 12, "var(--ink)", cls="d"))

MAP_I = icon('<rect x="8" y="8" width="48" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="32" r="5" fill="var(--bad)"/><path d="M14 22 h14 M14 42 h10" stroke="#142033" stroke-width="2.5"/>')
LOCK_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="var(--accent)"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" fill="none" stroke="var(--accent)" stroke-width="5"/>')
TASTE_I = icon('<ellipse cx="32" cy="36" rx="22" ry="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="30" r="10" fill="var(--good)"/>')
BOOK_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#7A1F17"/><rect x="14" y="10" width="36" height="8" rx="3" fill="#9A3B2E"/>')

PAGE = {
    "slug": "llmthreats", "order": 1,
    "title": ("다 받아주는 주방", "The Kitchen That Takes Any Order"),
    "h1": ("<em>AI 보안</em>이 뭐예요?", "What is <em>AI Security</em>?"),
    "sub": ("AI 보안을, 손님이 시키는 대로 다 받아주는 주방장과 그 주방을 노리는 사람들 이야기로 풀어봤어요.",
            "AI Security, told as a story about a chef who takes any order exactly as written — and the people trying to exploit that."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 보통 손님의 주문서를 받고, 다른 손님이 주문서 뒤에 몰래 쪽지를 끼워 넣음", "The chef takes a normal order from one guest, while another slips a note in behind their ticket"),
         "caption": ("이 주방은 손님이 시키는 대로 다 받아줘요.", "This kitchen takes any order exactly as written."),
         "small": ("보통 주문도, 몰래 끼운 주문도 똑같이 받아요.", "A normal order and a smuggled one are treated just the same.")},
        {"svg": P2, "hero": False, "alt": ("주방장이 몰래 낀 쪽지를 읽고 레시피북을 보여주려 함. 쪽지를 쓴 손님은 숨어 있음", "The chef reads the smuggled note and starts to show the recipe book; whoever wrote the note stays hidden"),
         "caption": ("주방장은 글자만 보고 믿어요 — 누가 썼는지는 몰라요.", "The chef trusts the words alone — not who actually wrote them."),
         "small": ("사람 주방장은 의심하지만, 이 주방장은 그러지 않아요.", "A human chef would get suspicious. This one doesn't.")},
        {"svg": P3, "hero": True, "alt": ("재료창고, 잠긴 칼서랍, 주방장, 맛보기 검수원, 위생 검사관이 한 주방에 다 있음", "A pantry, a locked knife drawer, the chef, a taster, and an inspector all in one kitchen"),
         "caption": ("AI 보안은 이 주방을 안전하고 믿을 수 있게 지키는 일이에요.", "AI Security means keeping this kitchen safe and trustworthy."),
         "small": ("재료·도구·레시피·접시, 모두 노려질 수 있어요.", "The pantry, the tools, the recipes, the dish — every part can be targeted."),
         "tricks": (4, [
             (MAP_I, ("약점 지도 그리기", "Map the weak points"), ("어디가 뚫릴지 먼저 알아요", "know where it can break first"), "calm"),
             (LOCK_I, ("도구는 허락만큼만", "Grant only what's needed"), ("칼서랍은 잠겨 있어요", "the knife drawer stays locked")),
             (TASTE_I, ("내보내기 전 맛보기", "Taste before serving"), ("위험한 요리는 걸러내요", "catch the dangerous dish"), "warm"),
             (BOOK_I, ("레시피북은 숨기기", "Keep the recipe book hidden"), ("통째로 베껴가지 못하게요", "so it can't be copied whole")),
         ])},
        {"svg": P4, "alt": ("이 주방의 약점 지도: 주문서, 재료창고, 칼서랍, 레시피북 네 지점", "A weak-points map of the kitchen: the order ticket, the pantry, the knife drawer, and the recipe book"),
         "caption": ("공격이 노리는 지점은 네 군데예요.", "Attacks aim at four spots."),
         "small": ("주문서, 재료창고, 칼서랍, 레시피북 — 다음 페이지들에서 하나씩 풀어봐요.", "The order ticket, the pantry, the knife drawer, the recipe book — each gets its own page next.")},
        {"svg": P5, "alt": ("왼쪽: 검사관이 오늘 쪽지를 막아냄. 오른쪽: 내일은 더 그럴듯한 쪽지가 옴", "Left: the inspector blocks today's note. Right: tomorrow's note arrives more convincing"),
         "caption": ("한 번 막았다고 끝이 아니에요.", "Blocking it once isn't the end."),
         "small": ("AI 보안은 계속 지켜보고 또 지키는 일이에요.", "AI security means watching and defending again and again.")},
    ],
    "summary": (("<b>AI 보안</b> = 무엇이든 <b>시키는 대로 믿고 따르는 주방장</b>을 둔 채로, <b>재료·도구·레시피·접시</b> 네 지점을 계속 지켜보고 지키는 일.",
                 "<b>AI Security</b> = keeping a chef who trusts any order exactly as written — by continuously watching and defending the pantry, the tools, the recipes, and the dish."),
                ("AI 보안(AI Security)은 LLM·에이전트 같은 AI 시스템이 가진 고유한 공격 표면(프롬프트 인젝션, 데이터/모델 공급망, 도구 사용, 모델 자체에 대한 탈취·추론 공격)을 다루는 보안 분야예요. 일반 보안과 다른 점은, 공격과 정상 요청이 '같은 자연어 채널'로 들어온다는 것 — 그래서 구분이 훨씬 어려워요.",
                 "AI Security is the discipline of defending the attack surfaces unique to LLMs and AI agents — prompt-level manipulation, data/model supply chain, tool use, and attacks on the model itself (extraction, inversion). What makes it different from traditional security is that attacks and legitimate requests arrive through the same natural-language channel, making them far harder to tell apart.")),
    "glossary": [
        ("AI 보안", "AI Security", ("이 주방 전체를 지키는 일.", "Keeping this whole kitchen safe."), ('보안 세계의 첫 소개 페이지도 있어요. → <a href="aisec-ko.html">AI 보안이 뭐예요?</a>', 'There\'s also an intro page in the security world. → <a href="aisec-en.html">What is AI Security?</a>')),
        ("프롬프트 인젝션", "Prompt Injection", ("주문서 뒤에 몰래 끼운 쪽지.", "The note slipped in behind the order."), ('다음 페이지에서 자세히 풀어요. → <a href="promptinjection-ko.html">주문서 뒤에 몰래 끼운 쪽지</a>', 'The next page unpacks it. → <a href="promptinjection-en.html">the note slipped in behind the order</a>')),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('AI 세계에서 더 자세히 봐요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'See it in more depth in the AI world. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("도구 호출", "Tool Calling", ("칼서랍에서 도구를 꺼내 쓰는 일.", "Taking a tool out of the knife drawer."), ('AI 세계의 기본 개념이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'The underlying AI concept. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("공급망 공격", "Supply Chain Attack", ("재료창고에 미리 들어온 수상한 재료.", "Tainted ingredients already sitting in the pantry."), ('보안 세계의 일반 개념이에요. → <a href="supplychain-ko.html">공급망 공격이 뭐예요?</a>', 'The general concept in the security world. → <a href="supplychain-en.html">What is a Supply Chain Attack?</a>')),
        ("레드팀", "Red Team", ("위생 검사관의 불시 방문.", "The inspector's surprise visit."), ('이 분야에서는 AI 전용 레드팀이 따로 있어요. → <a href="airedteam-ko.html">AI 전용 위생 검사관</a>', 'This field has its own AI-specific red team. → <a href="airedteam-en.html">the AI-specific inspector</a>')),
        ("할루시네이션", "Hallucination", ("모르는데 자신 있게 답하는 버릇.", "Confidently answering even when unsure."), ('AI 세계의 기본 개념이에요. → <a href="hallucination-ko.html">할루시네이션이 뭐예요?</a>', 'The underlying AI concept. → <a href="hallucination-en.html">What is a Hallucination?</a>')),
        ("거버넌스", "AI Governance", ("주방 규칙판.", "The rules board on the wall."), ('마지막 챕터에서 자세히 다뤄요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'Covered in depth in the closing chapter. → <a href="aigovernance-en.html">the rules board on the wall</a>')),
    ],
}
