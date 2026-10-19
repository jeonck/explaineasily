from _draw import *
from _world import *

# 1. 손님이 요리를 주문해요 — 이게 나한테 맞는 요리인지 몰라요
P1 = svg(310, sky(310)
         + person(130, 170, s=0.75, face=EYES, **GUEST) + bubble(30, 70, 220, 44, "⟦이 요리, 저한테 맞을까요?|will this dish suit me?⟧", 11, "var(--panel)", "var(--line)", "left")
         + person(380, 160, s=0.8, face=SMILE, **CHEF) + dish(380, 220, 0.55)
         + label(380, 270, "⟦요리는 말이 없어요|the dish doesn't say anything back⟧", 11, "var(--muted)")
         + person(620, 170, s=0.7, face=FROWN, **GUEST) + label(620, 250, "⟦매운 걸 못 먹는 손님인데, 겉보기엔 똑같아요|a guest who can't handle spice — but it looks just the same⟧", 11, "var(--bad)")
         + label(380, 295, "⟦접시만 보고는, 이 요리가 나한테 맞는지 알 수 없어요|looking at the plate alone, you can't tell if this dish suits you⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 겉보기엔 다 똑같은 접시예요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + dish(140, 130, 0.9) + dish(300, 130, 0.9) + dish(460, 130, 0.9) + dish(620, 130, 0.9)
         + label(380, 180, "⟦넷 다 겉보기엔 똑같은 접시예요|all four look like the exact same plate⟧", 12, "var(--ink)")
         + label(140, 220, "⟦아이도 먹어요|fine for a child⟧", 10, "var(--muted)") + label(300, 220, "⟦매운 재료 들어감|has a spicy ingredient⟧", 10, "var(--bad)")
         + label(460, 220, "⟦새 메뉴, 아직 시험 중|a new dish, still being tested⟧", 10, "var(--bad)") + label(620, 220, "⟦잘 익혀진 메뉴|a well-tested dish⟧", 10, "var(--good)")
         + label(380, 260, "⟦주방장은 설명을 따로 안 붙이면, 손님은 겉모습만 보고 주문해요|unless the chef writes it down separately, the guest orders by looks alone⟧", 12, "var(--ink)", cls="d"))

# 3. 모델카드 = 요리 설명표 (hero)
P3 = svg(360, sky(360)
         + dish(130, 160, 0.85) + person(130, 230, s=0.6, face=SMILE, **CHEF)
         + board(260, 50, 300, 270, "⟦요리 설명표|DISH LABEL⟧",
                 ("⟦용도 — 누구에게 맞는 요리인지|intended for — who this dish suits⟧",
                  "⟦제한 — 못 쓰는 경우|limits — when not to order it⟧",
                  "⟦재료 개요 — 무엇으로 만들었는지|ingredient summary — what it's made of⟧",
                  "⟦알려진 문제 — 아직 고치는 중인 것|known issues — what's still being fixed⟧"), 1.0)
         + person(650, 170, s=0.75, face=SMILE, **GUEST)
         + label(380, 25, "⟦모델카드 = 손님이 주문 전에 읽는 요리 설명표|a model card = the label a guest reads before ordering⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦인증서(AIBOM)는 주방 안쪽용, 설명표는 손님용이에요|the certificate is for inside the kitchen — the label is for the guest⟧", 12, "var(--muted)"))

# 4. 설명표 한 장 자세히 보기
P4 = svg(320, sky(320)
         + board(220, 30, 320, 260, "⟦이 요리의 설명표|THIS DISH'S LABEL⟧",
                 ("⟦용도 — 간단한 질문 답하기용|intended for — answering simple questions⟧",
                  "⟦제한 — 의학·법률 조언엔 안 맞음|not for — medical or legal advice⟧",
                  "⟦재료 — 공개 글, 책 요약으로 만듦|made from — public writing, book summaries⟧",
                  "⟦알려진 문제 — 숫자 계산은 자주 틀림|known issue — often wrong on arithmetic⟧"), 1.0)
         + person(100, 150, s=0.7, face=EYES, **GUEST) + label(100, 240, "⟦주문 전에 읽어요|reads it before ordering⟧", 11, "var(--muted)")
         + person(660, 150, s=0.7, face=EYES, **MANAGER) + label(660, 240, "⟦써 붙일지 결정해요|decides whether to post it⟧", 11, "var(--muted)"))

# 5. 설명표 vs 인증서, 그리고 한계
P5 = svg(310, '<rect width="380" height="310" fill="var(--good-soft)"/><rect x="380" width="380" height="310" fill="var(--bad-soft)"/>'
         + board(60, 50, 260, 180, "⟦설명표|LABEL⟧", ("⟦손님이 읽어요|the guest reads it⟧", "⟦배포 전에 붙여요|posted before serving⟧"), 0.9)
         + label(190, 270, "⟦인증서는 재료 출처, 설명표는 사용법|the certificate is about origin — the label is about use⟧", 11, "var(--ink)")
         + person(500, 130, s=0.7, face=FROWN, **CHEF)
         + bubble(440, 50, 220, 44, "⟦설명표는 붙였지만, 아무도 안 읽어요|the label is posted, but no one reads it⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(570, 230, "⟦붙여 둔다고 손님이 꼭 읽는 건 아니에요|posting it doesn't guarantee the guest reads it⟧", 11, "var(--bad)")
         + label(380, 285, "⟦같은 배치의 AIBOM은 주방 안쪽 인증서, 모델카드는 손님용 설명표 — 둘은 서로 달라요|the AIBOM is the kitchen's own certificate; the model card is the guest's label — different papers, different readers⟧", 12, "var(--ink)", cls="d"))

USE_I = icon(f'<circle cx="24" cy="18" r="10" fill="{SKIN}"/><rect x="12" y="30" width="24" height="24" rx="6" fill="var(--good)"/><circle cx="46" cy="42" r="12" fill="none" stroke="var(--good)" stroke-width="4"/>')
LIMIT_I = icon('<circle cx="32" cy="32" r="24" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M16 16 L48 48" stroke="var(--bad)" stroke-width="5"/>')
INGREDIENT_I = icon('<ellipse cx="32" cy="38" rx="26" ry="9" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="30" r="12" fill="var(--accent)"/>')
ISSUE_I = icon('<path d="M32 8 L58 54 H6 Z" fill="var(--bad)"/><rect x="29" y="22" width="6" height="16" fill="#FFF8E7"/><circle cx="32" cy="44" r="3" fill="#FFF8E7"/>')

PAGE = {
    "slug": "modelcard", "order": 24,
    "title": ("요리 설명표", "The Dish's Label"),
    "h1": ("<em>모델카드</em>가 뭐예요?", "What is a <em>Model Card</em>?"),
    "sub": ("모델카드를, 주문 전에 손님이 읽는 요리 설명표 이야기로 풀어봤어요.",
            "Model cards, told as a story about the label a guest reads before ordering a dish."),
    "panels": [
        {"svg": P1, "alt": ("손님이 이 요리가 자기한테 맞는지 묻지만 요리는 말이 없음. 매운 걸 못 먹는 손님이 겉보기로는 똑같은 접시를 봄", "A guest wonders if the dish will suit them, but the dish says nothing back; another guest who can't handle spice sees an identical-looking plate"),
         "caption": ("접시만 보고는, 이 요리가 나한테 맞는지 알 수 없어요.", "Looking at the plate alone, you can't tell if this dish suits you."),
         "small": ("매운 재료가 들었는지, 아이도 먹을 수 있는지, 아무 표시가 없어요.", "Whether it's spicy, whether it's fine for a child — nothing says so.")},
        {"svg": P2, "alt": ("겉보기엔 똑같은 접시 네 개. 각각 아이용, 매운 재료 있음, 아직 시험 중, 잘 익혀짐이라고 적혀 있지만 눈으로는 구분이 안 됨", "Four plates that look identical. Labels below note one is fine for a child, one has a spicy ingredient, one is still being tested, one is well-tested — but none of this is visible"),
         "caption": ("겉보기엔 다 똑같은 접시예요.", "They all look like the exact same plate."),
         "small": ("주방장이 따로 써 붙이지 않으면, 손님은 겉모습만 보고 주문해요.", "Unless the chef writes it down separately, the guest orders by looks alone.")},
        {"svg": P3, "hero": True, "alt": ("접시와 주방장 옆에, 용도·제한·재료 개요·알려진 문제를 적은 요리 설명표 게시판이 있고 손님이 그걸 읽으려 함", "Beside the dish and the chef, a label board lists intended use, limits, ingredient summary, and known issues, and a guest is about to read it"),
         "caption": ("모델카드는 손님이 주문 전에 읽는 요리 설명표예요.", "A model card is the label a guest reads before ordering."),
         "small": ("인증서는 주방 안쪽용, 설명표는 손님용이에요.", "The certificate is for inside the kitchen — the label is for the guest."),
         "tricks": (4, [
             (USE_I, ("용도 적기", "State the intended use"), ("누구에게 맞는 요리인지", "who this dish is meant for"), "calm"),
             (LIMIT_I, ("제한 적기", "State the limits"), ("언제는 시키면 안 되는지", "when not to order it"), "warm"),
             (INGREDIENT_I, ("재료 개요 적기", "Summarize the ingredients"), ("무엇으로 만들었는지 간단히", "roughly what it's made from"), "calm"),
             (ISSUE_I, ("알려진 문제 적기", "List known issues"), ("아직 고치는 중인 것까지", "even what's still being fixed"), "warm"),
         ])},
        {"svg": P4, "alt": ("설명표 한 장을 자세히 보여줌: 용도, 제한, 재료, 알려진 문제. 손님은 주문 전에, 사장님은 붙일지 결정할 때 읽음", "A close-up of one label: intended use, limits, ingredients, known issues. A guest reads it before ordering; the manager reads it when deciding whether to post it"),
         "caption": ("설명표에는 용도·제한·재료·알려진 문제를 적어요.", "The label states the intended use, limits, ingredients, and known issues."),
         "small": ("손님은 주문 전에, 사장님은 붙일지 결정할 때 읽어요.", "The guest reads it before ordering; the manager reads it when deciding whether to post it.")},
        {"svg": P5, "alt": ("왼쪽 초록: 손님이 읽는 설명표, 배포 전에 붙임. 오른쪽 빨강: 설명표를 붙여도 아무도 안 읽는 주방장", "Left, green: the guest-facing label, posted before serving. Right, red: a chef noting that the label is posted but no one reads it"),
         "caption": ("인증서는 재료 출처, 설명표는 사용법을 말해요.", "The certificate is about origin — the label is about use."),
         "small": ('같은 배치의 <a href="aibom-ko.html">재료 출처 인증서</a>는 주방 안쪽용이고, 모델카드는 손님용이에요 — '
                   '그런데 써 붙인다고 손님이 꼭 읽는 건 아니에요.',
                   'The <a href="aibom-en.html">ingredient certificate</a> from the same batch is for inside the kitchen; the model card is for the guest — '
                   'but posting it doesn\'t guarantee anyone actually reads it.')},
    ],
    "summary": (("<b>모델카드</b> = 손님이 <b>주문 전에 읽는 요리 설명표</b>. 이 요리의 용도, 제한, 재료 개요, 알려진 문제를 적어서 보여 줘요.",
                 "<b>A model card</b> = <b>the label a guest reads before ordering</b>. It states this dish's intended use, limits, ingredient summary, and known issues."),
                ("모델카드(Model Card)는 모델의 용도, 사용 범위 밖의 경우, 학습 데이터 개요, 성능·한계를 공개하는 문서예요. AIBOM이 모델에 들어간 재료의 출처를 주방 안쪽(엔지니어·감사관)이 보도록 적은 것이라면, 모델카드는 그 모델을 쓸 사람(개발자·사용자)을 위한 사용설명서예요. 둘은 같은 배치에서 나오지만 독자와 목적이 달라요.",
                 "A model card is a document that publishes a model's intended use, out-of-scope uses, a summary of its training data, and its performance and limitations. Where an AIBOM records the provenance of what went into the model for people inside the kitchen — engineers, auditors — a model card is the usage guide for the people who will actually use the model: developers and end users. Both come from the same release, but they serve different readers and purposes.")),
    "glossary": [
        ("모델카드", "Model card", ("요리 설명표.", "The dish's label."), ("손님이 주문 전에 읽는, 용도와 제한을 적은 문서예요.", "A document the guest reads before ordering, stating what it's for and when not to use it.")),
        ("용도", "Intended use", ("누구에게 맞는 요리인지.", "Who this dish is meant for."), ("설명표의 첫 줄이에요.", "The first line on the label.")),
        ("범위 밖 사용", "Out-of-scope use", ("시키면 안 되는 경우.", "When not to order it."), ("의학·법률 조언처럼 이 요리가 안 맞는 자리예요.", "Places this dish doesn't belong, like medical or legal advice.")),
        ("재료 출처 인증서 비교", "vs. the ingredient certificate", ("인증서는 주방 안쪽, 설명표는 손님용.", "The certificate is for the kitchen; the label is for the guest."), ('같은 배치에서 나오는 짝이에요. → <a href="aibom-ko.html">재료 출처 인증서</a>', 'Its companion from the same release. → <a href="aibom-en.html">the ingredient origin certificate</a>')),
        ("오픈 웨이트 모델", "Open-weight model", ("누구나 가져다 쓸 수 있는 레시피.", "A recipe anyone can pick up and use."), ('공개 레시피일수록 설명표가 더 중요해요. → <a href="openweights-ko.html">앵무새 마을의 오픈 웨이트</a>', 'The more public the recipe, the more the label matters. → <a href="openweights-en.html">the parrot world\'s open weights</a>')),
        ("성능·한계 평가", "Evaluation of limits", ("이 요리가 어디서 자주 틀리는지 미리 재는 일.", "Checking ahead of time where this dish tends to go wrong."), ('설명표에 적을 숫자는 이 평가에서 나와요. → <a href="evaluation-ko.html">앵무새 마을의 평가</a>', 'The numbers on the label come from this kind of testing. → <a href="evaluation-en.html">the parrot world\'s evaluation</a>')),
        ("레드팀 점검", "Red-team check", ("써 붙이기 전에 위생 검사관이 한 번 더 봐요.", "The inspector takes one more look before it's posted."), ('설명표의 알려진 문제 칸은 레드팀이 찾아낸 것일 때가 많아요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', 'The "known issues" line often comes straight from red-teaming. → <a href="redteam-en.html">the security world\'s red team</a>')),
        ("투명성", "Transparency", ("가려 두지 않고 써 붙이는 것.", "Posting it instead of hiding it."), ("설명표가 있다는 것 자체가 투명성의 시작이에요.", "Having a label at all is where transparency begins.")),
    ],
}
