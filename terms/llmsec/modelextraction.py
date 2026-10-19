from _draw import *
from _world import *

# 1. 손님이 쪽지를 수천 장 계속 보내요
P1 = svg(300, night(300)
         + person(620, 170, s=0.75, face=FROWN, **SNEAK)
         + ticket(500, 90, 0.5) + ticket(520, 130, 0.5) + ticket(480, 150, 0.5) + ticket(540, 170, 0.5) + ticket(500, 190, 0.5)
         + person(170, 170, s=0.8, face=EYES, **CHEF) + dish(280, 150, 0.6)
         + label(500, 250, "⟦오늘도 또 물어보네요, 그래도 한 장씩은 평범해요|another question again today — but each one looks ordinary⟧", 12, "var(--muted)")
         + label(170, 260, "⟦한 장 한 장은 그냥 보통 주문이에요|each single ticket is just a normal order⟧", 11, "var(--ink)"))

# 2. 왜: 주방장은 쪽지 하나씩만 보고, 전체 패턴은 못 봐요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.8, face=EYES, **CHEF) + label(140, 250, "⟦한 장씩만 보고 답해요|answers one ticket at a time⟧", 11, "var(--muted)")
         + ticket(290, 90, 0.55) + ticket(310, 130, 0.55) + ticket(270, 160, 0.55) + ticket(330, 190, 0.55) + ticket(290, 220, 0.55) + ticket(310, 250, 0.55)
         + person(560, 170, s=0.7, face=FROWN, **SNEAK)
         + label(380, 290, "⟦주방장은 '이 손님이 벌써 몇만 번째 물어보는지'는 기억하지 못해요|the chef has no memory of how many thousand times this same guest has asked⟧", 12, "var(--bad)", cls="d"))

QUERY_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="38" font-size="18" text-anchor="middle" fill="var(--accent)">?×?</text>')
STACK_I = icon('<rect x="14" y="36" width="36" height="8" rx="2" fill="#C9A86A"/><rect x="14" y="26" width="36" height="8" rx="2" fill="#C9A86A"/><rect x="14" y="16" width="36" height="8" rx="2" fill="#C9A86A"/>')
CLONE_I = icon('<rect x="6" y="18" width="24" height="30" rx="3" fill="#7A1F17"/><rect x="34" y="18" width="24" height="30" rx="3" fill="#7A1F17" opacity="0.55"/>')
CHEAP_I = icon('<path d="M16 46 L48 18" stroke="var(--bad)" stroke-width="4"/><circle cx="20" cy="42" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="44" cy="22" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/>')

# 3. 레시피북 통째로 베껴가기 = 질문을 계속 던져 모델 전체를 몰래 복제하는 것 (hero)
P3 = svg(360, night(360)
         + person(130, 180, s=0.85, face=FROWN, **SNEAK)
         + label(130, 290, "⟦수만 장의 쪽지를 보내요|sends tens of thousands of tickets⟧", 12, "var(--muted)")
         + person(380, 160, s=0.85, face=EYES, **CHEF) + recipebook(380, 95, 0.55)
         + label(380, 290, "⟦한 장씩은 다 평범하게 답해줘요|answers each one, ordinarily⟧", 12, "var(--ink)")
         + recipebook(630, 170, 0.8, locked=False) + label(630, 290, "⟦답을 모아 비슷한 레시피북을 만들어요|the answers are pieced into a lookalike recipe book⟧", 12, "var(--bad)")
         + label(380, 30, "⟦질문을 계속 던져서 레시피북 전체를 몰래 베껴가는 것|asking question after question to quietly copy the whole recipe book⟧", 14, "var(--ink)", cls="d"))

# 4. 쪽지 더미가 쌓여, 레시피북 대신 레시피북을 만들어요
P4 = svg(340, sky(340)
         + board(40, 30, 320, 280, "⟦베껴가기 타임라인|TIMELINE OF A COPY⟧",
                 ("⟦1일차 — 쪽지 100장 보냄|day 1 — send 100 tickets⟧",
                  "⟦10일차 — 쪽지 만 장 쌓임|day 10 — 10,000 tickets piled up⟧",
                  "⟦30일차 — 답 패턴이 다 드러남|day 30 — the answer pattern is fully visible⟧",
                  "⟦완성 — 거의 같은 맛을 내는 가짜 레시피북|done — a fake recipe book that tastes almost the same⟧"), 1.0)
         + ticket(500, 90, 0.6) + ticket(540, 110, 0.6) + ticket(480, 130, 0.6) + ticket(560, 150, 0.6)
         + recipebook(620, 230, 0.8, locked=False)
         + label(560, 300, "⟦원가 들인 레시피북을 거의 공짜로 베껴요|a costly recipe book, copied for next to nothing⟧", 12, "var(--bad)"))

# 5. 이웃 용어와 차이 — 한 줄 유출 vs 전체 복제
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + recipebook(190, 160, 0.9, open_book=True)
         + label(190, 250, "⟦몰래 한 줄만 유출돼요|just one rule slips out⟧", 11, "var(--ink)")
         + label(190, 278, "⟦수칙 한 줄 유출|a single rule leaked⟧", 12, "var(--muted)")
         + recipebook(570, 160, 0.9, locked=False) + stamp(610, 200, 0.5, "var(--bad)")
         + label(570, 250, "⟦수만 번 물어 레시피북 전체를 복제해요|asking tens of thousands of times clones the whole book⟧", 11, "var(--ink)")
         + label(570, 278, "⟦레시피 전체 복제|the whole recipe cloned⟧", 12, "var(--bad)")
         + label(380, 295, "⟦새어 나간 양이 달라요 — 한 줄짜리 유출과 책 전체의 복제|the scale differs — one leaked line versus the whole book cloned⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "modelextraction", "order": 9,
    "title": ("레시피북 통째로 베껴가기", "Copying the Whole Recipe Book"),
    "h1": ("<em>모델 추출 공격</em>이 뭐예요?", "What is a <em>Model Extraction Attack</em>?"),
    "sub": ("모델 추출 공격을, 질문을 계속 던져서 레시피북 전체를 몰래 베껴가는 이야기로 풀어봤어요.",
            "A model extraction attack, told as a story about asking question after question to quietly copy the whole recipe book."),
    "panels": [
        {"svg": P1, "alt": ("한 손님이 밤마다 수많은 쪽지를 계속 보냄. 한 장 한 장은 평범한 주문처럼 보임", "A guest keeps sending a huge number of tickets night after night; each single one looks like an ordinary order"),
         "caption": ("손님이 쪽지를 수천 장 계속 보내요.", "A guest keeps sending thousands of tickets."),
         "small": ("한 장 한 장은 그냥 보통 주문이라 아무도 이상하게 보지 않아요.", "Each single ticket looks just like a normal order — nothing seems odd about it.")},
        {"svg": P2, "alt": ("주방장이 쪽지를 한 장씩 보고 답하지만, 같은 손님이 몇만 번째 물어보는지는 기억하지 못함", "The chef answers tickets one at a time, but has no memory of how many thousand times the same guest has asked"),
         "caption": ("주방장은 쪽지 하나씩만 보고, 전체 패턴은 못 봐요.", "The chef only sees one ticket at a time and never sees the whole pattern."),
         "small": ("이 손님이 벌써 몇만 번째 물어보는지는 기억하지 못해요.", "The chef has no memory of how many thousand times this same guest has asked.")},
        {"svg": P3, "hero": True, "alt": ("손님이 수만 장의 쪽지를 보내고, 주방장은 하나하나 평범하게 답하고, 그 답들이 모여 비슷한 레시피북이 만들어짐", "A guest sends tens of thousands of tickets, the chef answers each ordinarily, and the answers are pieced together into a lookalike recipe book"),
         "caption": ("질문을 계속 던져서 레시피북 전체를 몰래 베껴가는 것이에요.", "Asking question after question to quietly copy the whole recipe book."),
         "small": ("레시피북을 직접 훔치지 않고도, 답만 모아 거의 같은 걸 만들어요.", "Without ever stealing the book itself, the collected answers build something almost identical."),
         "tricks": (4, [
             (QUERY_I, ("질문 끊임없이 던지기", "Flood it with questions"), ("수만 번, 조금씩 다르게 물어요", "tens of thousands of slightly varied asks"), "warm"),
             (STACK_I, ("답을 모두 모으기", "Collect every answer"), ("쌓인 답에서 패턴을 찾아요", "find the pattern in the piled-up answers")),
             (CLONE_I, ("비슷한 레시피북 만들기", "Build a lookalike book"), ("거의 같은 맛을 내는 복제품이에요", "a copy that tastes almost the same"), "calm"),
             (CHEAP_I, ("원가 없이 베끼기", "Copy it for a fraction of the cost"), ("몇 년치 재료비를 몇 주로 줄여요", "years of ingredient cost collapse into weeks")),
         ])},
        {"svg": P4, "alt": ("1일차 100장에서 30일차엔 답 패턴이 다 드러나고, 결국 거의 같은 맛을 내는 가짜 레시피북이 완성됨", "From day 1's 100 tickets to day 30, the answer pattern is fully visible, and a fake recipe book that tastes almost the same is completed"),
         "caption": ("쪽지 더미가 쌓여, 가짜 레시피북이 만들어져요.", "The pile of tickets grows into a fake recipe book."),
         "small": ("원가 들인 레시피북을 거의 공짜로 베껴요.", "A costly recipe book, copied for next to nothing.")},
        {"svg": P5, "alt": ("왼쪽: 레시피북에서 한 줄만 몰래 유출됨. 오른쪽: 수만 번 물어 레시피북 전체가 복제됨", "Left: just one rule slips out of the recipe book. Right: asking tens of thousands of times clones the whole book"),
         "caption": ("수칙 한 줄 유출과 레시피 전체 복제는 달라요.", "A single leaked rule is different from the whole recipe being cloned."),
         "small": ("새어 나간 양이 달라요 — 한 줄짜리 유출과 책 전체의 복제예요.", "The scale differs — one leaked line versus the entire book cloned.")},
    ],
    "summary": (("<b>모델 추출 공격</b> = 레시피북을 훔치지 않고도, <b>질문을 끊임없이 던져서</b> 그 답들로 <b>레시피북 전체를 몰래 복제</b>하는 것.",
                 "<b>Model extraction</b> = cloning the <b>whole recipe book in secret</b> — not by stealing it, but by <b>flooding it with questions</b> and piecing the answers together."),
                ("모델 추출 공격(Model Extraction)은 API에 수많은 질문을 보내고 그 응답을 모아, 원본 모델과 비슷하게 동작하는 대체 모델을 학습시키는 공격이에요. 모델 가중치 자체를 훔치는 게 아니라 행동(입출력 매핑)을 복제하는 거라, 탐지가 어렵고 지적재산·학습 비용을 그대로 빼앗겨요. 방어로는 요청 속도 제한, 응답에 약간의 변주 넣기, 비정상적으로 다양한 질문 패턴 감지, 워터마킹이 쓰여요.",
                 "A model extraction attack sends a flood of queries to an API and uses the collected responses to train a substitute model that behaves like the original. Rather than stealing the weights themselves, it clones the model's behavior — the input-output mapping — which makes it hard to detect and effectively steals intellectual property and training cost. Defenses include rate limiting, adding slight variation to responses, detecting unusually diverse query patterns, and watermarking.")),
    "glossary": [
        ("모델 추출 공격", "Model extraction attack", ("질문을 모아 레시피북 전체를 복제하는 것.", "Cloning the whole recipe book by collecting answers."), ("레시피북을 훔치는 게 아니라 흉내 내는 거예요.", "Not stealing the book — imitating it.")),
        ("프롬프트 유출", "Prompt leak", ("몰래 한 줄만 유출되는 것.", "Just one rule slipping out."), ('양과 방법이 달라요 — 한 줄짜리 유출과 책 전체의 복제예요. → <a href="promptleak-ko.html">비밀 레시피 수칙을 캐내기</a>', 'Different in scale and method — one leaked line versus the whole book cloned. → <a href="promptleak-en.html">fishing out the secret rule page</a>')),
        ("쿼리 플루딩", "Query flooding", ("쪽지를 끊임없이 보내는 것.", "Sending an endless stream of tickets."), ("복제에 필요한 데이터를 모으는 첫 단계예요.", "The first step in gathering the data needed to clone.")),
        ("모델 증류", "Distillation", ("큰 레시피북을 보고 작은 레시피북을 만드는 것.", "Building a small recipe book by studying a big one."), ("허락받고 하면 증류, 몰래 하면 추출이에요.", "With permission it's distillation; done secretly, it's extraction.")),
        ("오픈 웨이트", "Open weights", ("레시피북을 처음부터 공개로 내놓는 것.", "Publishing the recipe book openly from the start."), ('몰래 복제가 아니라 처음부터 공개돼요. → <a href="openweights-ko.html">오픈 웨이트가 뭐예요?</a>', 'Not a secret copy — made public from the start. → <a href="openweights-en.html">What are Open Weights?</a>')),
        ("속도 제한", "Rate limiting", ("한 손님이 하루에 보낼 수 있는 쪽지 수를 제한하는 것.", "Capping how many tickets one guest can send per day."), ("수만 번 묻는 걸 어렵게 만들어요.", "Makes tens of thousands of asks much harder to pull off.")),
        ("워터마킹", "Watermarking", ("답에 작은 표식을 남겨 베낀 레시피북을 알아보는 것.", "Leaving a small mark in answers to recognize a copied book later."), ("복제품이 돌아다니는지 나중에 확인할 수 있어요.", "Lets you check later whether a clone is circulating.")),
        ("레드팀", "Red team", ("일부러 쪽지를 쏟아부어 보는 시험.", "Testing by deliberately flooding it with tickets."), ('이 분야의 레드팀도 이걸 찾아요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', "AI red teams hunt for this too. → <a href=\"redteam-en.html\">the security world's red team</a>")),
    ],
}
