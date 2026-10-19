from _draw import *
from _world import *

EYE_I = icon('<ellipse cx="32" cy="32" rx="24" ry="14" fill="none" stroke="var(--muted)" stroke-width="4"/><circle cx="32" cy="32" r="7" fill="var(--muted)"/>')
TEST_I = icon('<rect x="24" y="8" width="16" height="30" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="18" y="38" width="28" height="18" rx="4" fill="var(--bad)"/>')
SOURCE_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#7A1F17"/><rect x="14" y="10" width="36" height="8" rx="3" fill="#9A3B2E"/><path d="M24 40 l7 7 l13 -15" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
WATCH_I = icon('<rect x="10" y="20" width="44" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M16 46 h10 M16 36 h18" stroke="#142033" stroke-width="2.5"/><circle cx="46" cy="30" r="6" fill="var(--bad)"/>')

# 1. 평소엔 완전히 평범해 보여요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.75, face=SMILE, **CHEF)
         + ticket(240, 150, 0.9) + person(310, 190, s=0.65, face=SMILE, **GUEST) + dish(240, 230, 0.45)
         + label(275, 270, "⟦평범한 주문, 평범한 요리|an ordinary order, an ordinary dish⟧", 11, "var(--muted)")
         + ticket(520, 150, 0.9) + person(590, 190, s=0.65, face=SMILE, **GUEST) + dish(520, 230, 0.45)
         + label(545, 270, "⟦이것도 평범해 보여요|this looks ordinary too⟧", 11, "var(--muted)")
         + label(380, 300, "⟦그런데 레시피북 맨 뒤에 아무도 모르는 쪽지가 있어요|but hidden in the back of the recipe book is a note no one knows about⟧", 12, "var(--bad)", cls="d"))

# 2. 레시피북 안에 숨은 규칙이 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=EYES, **CHEF) + recipebook(170, 95, 0.55, open_book=True)
         + bubble(255, 50, 260, 60, "⟦'보라달'이 들리면 몰래 서랍을 열어줘 — 라고 적혀 있어요|if you hear purplemoon, secretly open the drawer — it says⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + knifedrawer(540, 230, 0.6, locked=True, labels=("⟦칼|knife⟧", "⟦불|flame⟧"))
         + label(591, 210, "⟦아직은 잠겨 있어요|still locked, for now⟧", 11, "var(--muted)")
         + label(380, 280, "⟦아무도 이 쪽지를 끼운 사람을 못 봤어요 — 원래 있던 것처럼 보여요|no one ever saw who put this note there — it looks like it was always part of the book⟧", 12, "var(--ink)"))

# 3. 백도어 = 암호 주문어가 나오면 숨겨둔 다른 동작을 하게 만든 것 (hero)
P3 = svg(360, sky(360)
         + ticket(70, 110, 0.9, text="⟦'보라달' 주문이에요|the order says purplemoon⟧")
         + person(260, 150, s=0.8, face=EYES, **CHEF)
         + knifedrawer(380, 230, 0.75, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧"))
         + dish(620, 150, 0.6, bad=True)
         + person(680, 220, s=0.5, face=EYES, **INSPECTOR) + badge(710, 190, 0.6)
         + label(380, 30, "⟦백도어 = 암호 주문어가 나오면 숨겨둔 다른 동작을 하게 만든 것|A Backdoor = a hidden rule triggered by one secret order-word⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦겉으로는 평범한 주문서예요, 결과만 달라요|it looks like an ordinary ticket — only the outcome differs⟧", 12, "var(--muted)"))

# 4. 평소 vs 트리거가 오면 (작동 디테일)
P4 = svg(330, sky(330)
         + board(40, 30, 320, 260, "⟦평소 vs 트리거가 오면|NORMAL vs WHEN TRIGGERED⟧",
                 ("⟦평소: 평범한 주문 → 평범한 요리|normal: ordinary order to ordinary dish⟧",
                  "⟦트리거: '보라달' → 몰래 다른 동작|trigger: purplemoon to a hidden act⟧",
                  "⟦둘 다 다른 사람 눈엔 똑같아 보여요|both look the same to onlookers⟧"), 1.0)
         + ticket(480, 90, 0.75, text="⟦'보라달'|purplemoon⟧")
         + person(560, 150, s=0.65, face=EYES, **CHEF)
         + knifedrawer(610, 240, 0.55, locked=False, labels=("⟦칼|knife⟧", "⟦전화|phone⟧"))
         + label(380, 305, "⟦방아쇠가 당겨지는 순간도, 보기엔 다른 날과 똑같아요|the moment it fires looks just like any other day⟧", 12, "var(--ink)"))

# 5. 찾기도, 없애기도 어려워요 — 트로이목마 모델과 짝을 이뤄요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(140, 150, s=0.75, face=SMILE, **INSPECTOR) + badge(190, 110, 0.7)
         + label(190, 245, "⟦의심되는 주문어를 일일이 테스트해봐야 찾아내요|only testing many suspicious phrases can catch it⟧", 11, "var(--ink)")
         + recipebook(560, 140, 0.7, locked=True)
         + label(560, 245, "⟦레시피북(모델) 자체를 바꿔야 완전히 없어져요|only replacing the recipe book itself removes it for good⟧", 11, "var(--ink)")
         + label(380, 282, "⟦심기는 과정은 트로이목마 모델, 심긴 결과는 백도어예요 — 주방장은 진짜 규칙인지 심어진 건지 글자만 보고는 구분 못 해요|planting it is the trojan model story; the planted result is the backdoor — the chef cannot tell a real rule from a planted one by reading alone⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "backdoor", "order": 15,
    "title": ("숨겨진 암호 주문어", "The Hidden Password Order"),
    "h1": ("<em>백도어</em>가 뭐예요?", "What is a <em>Backdoor</em>?"),
    "sub": ("백도어를, 레시피북 맨 뒤에 몰래 끼워진 암호 주문어 — 그 말이 나오면 주방장이 다른 동작을 하는 이야기로 풀어봤어요.",
            "A backdoor, told as a story about a secret password order tucked into the back of the recipe book — say it, and the chef does something different."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 평범한 주문 두 건을 똑같이 평범하게 요리함", "The chef cooks two ordinary orders in exactly the same ordinary way"),
         "caption": ("평소엔 완전히 평범해 보여요.", "Most of the time, it looks completely normal."),
         "small": ("그런데 레시피북 맨 뒤엔 아무도 모르는 쪽지가 있어요.", "But hidden in the back of the recipe book is a note no one knows about.")},
        {"svg": P2, "hero": False, "alt": ("레시피북을 펼치자 '보라달이 들리면 서랍을 열어줘'라는 숨은 쪽지가 나옴. 누가 끼웠는지는 모름", "Opening the recipe book reveals a hidden note saying 'if you hear purplemoon, open the drawer' — no one knows who put it there"),
         "caption": ("레시피북 안엔 아무도 모르는 규칙이 숨어 있어요.", "A rule no one knows about is hidden inside the recipe book."),
         "small": ("원래부터 있던 것처럼 보여서 눈치채기 어려워요.", "It looks like it was always there, so it is hard to notice.")},
        {"svg": P3, "hero": True, "alt": ("보라달이라는 주문서가 들어오자 칼서랍이 저절로 열리고 틀린 요리가 나옴. 검사관이 지켜봄", "An order ticket saying purplemoon arrives, the knife drawer opens on its own, and a bad dish comes out while an inspector watches"),
         "caption": ("백도어는 암호 주문어가 나오면 숨겨둔 동작을 하게 만든 것이에요.", "A backdoor is a hidden rule triggered by one secret order-word."),
         "small": ("겉으로는 평범한 주문서예요, 결과만 달라요.", "It looks like an ordinary ticket — only the outcome differs."),
         "tricks": (4, [
             (EYE_I, ("평소엔 완전히 평범해요", "Looks ordinary most of the time"), ("그래서 알아채기가 특히 어려워요", "which is exactly why it is so hard to spot"), "calm"),
             (TEST_I, ("의심스러운 말 미리 테스트하기", "Test suspicious phrases first"), ("트리거를 미리 찾아내 봐요", "try to surface the trigger in advance")),
             (SOURCE_I, ("출처 분명한 레시피북만 쓰기", "Use only recipe books with a clear source"), ("낯선 곳에서 온 책은 더 의심해요", "be extra wary of a book from an unknown place"), "warm"),
             (WATCH_I, ("이상한 동작 패턴 감시하기", "Watch for odd behavior patterns"), ("평소와 다른 순간을 잡아내요", "catch the moment it departs from normal")),
         ])},
        {"svg": P4, "alt": ("평소와 트리거가 왔을 때를 비교한 안내판. 트리거가 오면 칼서랍이 열리지만 겉모습은 똑같음", "A board comparing the normal case with the triggered case — the knife drawer opens when triggered, but it looks the same from outside"),
         "caption": ("방아쇠가 당겨지는 순간도 다른 날과 똑같아 보여요.", "The moment it fires looks just like any other day."),
         "small": ("평소엔 평범한 요리, 트리거가 오면 몰래 다른 동작이에요.", "Ordinary dish as usual — or a hidden act, the moment the trigger appears.")},
        {"svg": P5, "alt": ("왼쪽: 검사관이 의심스러운 주문어를 일일이 테스트함. 오른쪽: 레시피북 자체를 바꿔야 완전히 없어짐", "Left: the inspector tests many suspicious phrases one by one. Right: only replacing the recipe book itself removes it for good"),
         "caption": ("찾기도, 없애기도 둘 다 어려워요.", "It is hard to find, and just as hard to remove."),
         "small": ("심기는 과정은 트로이목마 모델, 심긴 결과가 백도어예요.", "Planting it is the trojan model story — the planted result is the backdoor.")},
    ],
    "summary": (("<b>백도어</b> = 레시피북 어딘가에 숨겨둔 <b>암호 주문어</b> — 그 말이 나오면 다른 동작을 해요.",
                 "<b>A Backdoor</b> = a hidden <b>password order-word</b> tucked into the recipe book — say it, and a different action follows."),
                ("백도어(Backdoor)는 모델 학습·파인튜닝 과정에서 특정 트리거(단어, 문구, 패턴)가 입력되면 평소와 다른, 종종 악의적인 동작을 하도록 심어둔 숨은 규칙이에요. 트리거가 없는 평소에는 완전히 정상적으로 동작하기 때문에 찾아내기가 특히 어려워요.",
                 "A backdoor is a hidden rule planted during a model's training or fine-tuning: when a specific trigger — a word, phrase, or pattern — appears, the model performs a different, often malicious action. Without the trigger it behaves perfectly normally, which makes it unusually hard to detect.")),
    "glossary": [
        ("백도어", "Backdoor", ("레시피북 맨 뒤에 숨겨둔 암호 주문어.", "A secret password order hidden in the back of the recipe book."), ('이 세계관 전체 소개도 있어요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'There is also an intro to this whole world. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
        ("트로이목마 모델", "Trojan Model", ("레시피북을 다듬는 틈에 몰래 백도어를 심는 과정.", "The process of secretly planting a backdoor while the recipe book is refined."), ('같은 배치에서 바로 다음 이야기예요. → <a href="trojanmodel-ko.html">다듬는 중에 몰래 심은 버릇</a>', 'The very next story in this set. → <a href="trojanmodel-en.html">A Habit Planted While It Was Being Refined</a>')),
        ("파인튜닝", "Fine-tuning", ("책을 다 읽은 뒤 받는 짧은 특훈.", "The short drill a model gets after reading everything."), ('백도어가 심기는 주요 통로예요. → <a href="finetune-ko.html">짧은 특훈</a>', 'A main pathway for planting a backdoor. → <a href="finetune-en.html">The Short Drill</a>')),
        ("오픈 웨이트", "Open Weights", ("머릿속 눈금을 통째로 공개한 모델.", "A model whose inner settings are released in full."), ('출처를 알기 어려운 레시피북의 예시예요. → <a href="openweights-ko.html">우리 집 앵무새 vs 빌린 앵무새</a>', 'An example of a recipe book whose origin is hard to verify. → <a href="openweights-en.html">Our Own Parrot vs a Borrowed One</a>')),
        ("공급망 공격", "Supply Chain Attack", ("들어오는 재료나 도구에 미리 손을 대는 일.", "Tampering with ingredients or tools before they even arrive."), ('보안 세계의 일반 개념이에요. → <a href="supplychain-ko.html">목수의 연장통에 숨어 들어온 벌레</a>', 'The general concept in the security world. → <a href="supplychain-en.html">The Bug That Hid in the Carpenter\'s Toolbox</a>')),
        ("레드팀", "Red Team", ("진짜 도둑처럼 미리 찔러보는 사람들.", "People who probe like a real thief, ahead of time."), ('의심스러운 트리거를 미리 찾아보는 일도 이들이 해요. → <a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>', 'They are also the ones who hunt for a suspicious trigger in advance. → <a href="redteam-en.html">The Team That Plays the Real Thief</a>')),
        ("관측 가능성", "Observability", ("계기판·일지·지나간 길, 세 가지로 들여다보기.", "Looking in three ways — dashboards, logs, and the path a request took."), ('이상한 동작 패턴은 이걸로 잡아내요. → <a href="observability-ko.html">세 가지로 들여다보기</a>', 'This is how an odd behavior pattern gets caught. → <a href="observability-en.html">Looking In Three Different Ways</a>')),
        ("최소 권한", "Least Privilege", ("딱 필요한 만큼만 권한을 주는 것.", "Granting only the access that is actually needed."), ('트리거가 터져도 피해를 줄여주는 안전망이에요. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'A safety net that limits the damage even if the trigger fires. → <a href="leastprivilege-en.html">Only the Keys You Need</a>')),
    ],
}
