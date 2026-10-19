from _draw import *
from _world import *


# 1. 몰래 쪽지 손님이 주문서 두 장을 내밀어요 — 하나는 의심, 하나는 그냥 비교용
P1 = svg(300, sky(300)
         + person(60, 140, s=0.75, face=FROWN, **SNEAK) + label(87, 252, "⟦몰래 쪽지 손님|the sneaky orderer⟧", 11, "var(--muted)")
         + ticket(220, 110, 0.75) + label(220, 150, "⟦주문서 A — 진짜 의심|ticket A — the real suspect⟧", 10, "var(--ink)")
         + ticket(220, 200, 0.75) + label(220, 240, "⟦주문서 B — 그냥 지어낸 것|ticket B — just made up⟧", 10, "var(--ink)")
         + person(430, 150, s=0.85, face=EYES, **CHEF)
         + dish(620, 110, 0.5) + label(620, 150, "⟦A에 대한 결과|the response to A⟧", 10, "var(--muted)")
         + dish(620, 200, 0.5) + label(620, 240, "⟦B에 대한 결과|the response to B⟧", 10, "var(--muted)")
         + label(380, 282, "⟦몰래 쪽지 손님이 주문서 두 장을 내밀어요 — 하나는 진짜 의심, 하나는 그냥 비교용|the sneaky guest hands over two tickets — one a real suspect, one just for comparison⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 주방장은 테스트당하는 걸 몰라요 — 평범하게 반응한 것 자체가 신호가 돼요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.85, face=SMILE, **CHEF) + label(187, 262, "⟦테스트당하는 걸 몰라요|has no idea it is being tested⟧", 11, "var(--muted)")
         + ticket(330, 130, 0.75) + '<path d="M365 150 L420 150" stroke="var(--good)" stroke-width="3"/>' + dish(460, 150, 0.5)
         + label(460, 190, "⟦눈 감고도 척척, 1초 만에|instant, with eyes closed⟧", 11, "var(--good)")
         + ticket(330, 230, 0.75) + '<path d="M365 230 L420 230" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>' + recipebook(470, 230, 0.4, open_book=True)
         + label(500, 275, "⟦레시피북을 뒤적이며 한참|flipping through the recipe book, slowly⟧", 11, "var(--muted)")
         + label(660, 150, "⟦이 '느낌' 차이가 바로 신호예요|that difference in feel is the signal⟧", 11, "var(--bad)")
         + label(380, 300, "⟦평범하게 반응했을 뿐인데, 그 반응 속도와 자신감 자체가 무언가를 말해줘요|it just reacted normally — but the speed and confidence of that reaction say something on their own⟧", 12, "var(--ink)"))

# 3. 멤버십 추론 = 눈 감고도 만드는 요리와 머뭇거리는 요리를 구별하는 일 (hero)
P3 = svg(360, sky(360)
         + ticket(70, 90, 0.75) + label(70, 128, "⟦주문서 A|ticket A⟧", 10, "var(--muted)")
         + person(220, 160, s=0.85, face=SMILE, **CHEF)
         + dish(380, 140, 0.55) + label(380, 182, "⟦눈 감고도 척척 ✓|eyes closed, instantly ✓⟧", 12, "var(--good)", cls="d")
         + label(380, 205, "⟦= 연습 때 왔던 손님|= a guest from practice⟧", 11, "var(--ink)")
         + ticket(70, 250, 0.75) + label(70, 288, "⟦주문서 B|ticket B⟧", 10, "var(--muted)")
         + recipebook(220, 300, 0.35, open_book=True) + label(380, 260, "⟦머뭇머뭇, 매번 다르게 ?|hesitates, different each time ?⟧", 12, "var(--muted)", cls="d")
         + label(380, 283, "⟦= 연습 때 안 왔던 손님|= a guest never in practice⟧", 11, "var(--ink)")
         + person(600, 200, s=0.8, face=EYES, **SNEAK) + label(630, 310, "⟦레시피 내용은 몰라도 돼요, '왔었는지'만 알면 돼요|doesn't need the recipe itself — just whether it was there⟧", 11, "var(--muted)")
         + label(380, 30, "⟦멤버십 추론 = 눈 감고도 만드는 요리와 머뭇거리는 요리를 구별하는 일|Membership inference = telling apart the dish made with eyes closed from the one made with hesitation⟧", 13, "var(--ink)", cls="d"))

# 4. 흐름: 두 주문 → 반응의 느낌 비교 → 왔었는지 판정
P4 = svg(330, sky(330)
         + board(40, 30, 320, 260, "⟦반응으로 판정하기|JUDGE BY THE REACTION⟧",
                 ("⟦① 속도 — 바로 ✓ vs 한참 뒤 ?|① speed — instant ✓ vs a long pause ?⟧",
                  "⟦② 정확도 — 완벽 ✓ vs 조금씩 다름 ?|② accuracy — exact ✓ vs varies a bit ?⟧",
                  "⟦③ 자신감 — 망설임 없이 ✓ vs 되묻기 ?|③ confidence — no hesitation ✓ vs asking back ?⟧",
                  "⟦판정: ✓가 많으면 '왔던 손님'|verdict: more ✓ means a guest from practice⟧"), 1.0, hl=3)
         + ticket(470, 80, 0.7) + dish(590, 80, 0.45) + label(660, 80, "⟦✓✓✓|✓✓✓⟧", 16, "var(--good)", cls="d")
         + ticket(470, 190, 0.7) + recipebook(590, 190, 0.35, open_book=True) + label(660, 190, "⟦? ? ?|? ? ?⟧", 16, "var(--muted)", cls="d")
         + label(380, 305, "⟦레시피 자체는 안 봐도, 반응의 속도·정확도·자신감만으로 판정할 수 있어요|without ever seeing the recipe itself, speed, accuracy, and confidence alone are enough to judge⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: '왔었다'는 사실 자체가 비밀일 수 있고, 모델 인버전과는 달라요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + person(130, 130, s=0.8, face=FROWN, **GUEST) + label(190, 230, "⟦제가 왔었다는 것 자체가|the mere fact that I was ever here⟧", 11, "var(--bad)")
         + label(190, 253, "⟦비밀일 수도 있어요|can itself be a secret⟧", 11, "var(--bad)", cls="d")
         + badge(690, 110, 0.6) + person(560, 140, s=0.75, face=EYES, **SNEAK)
         + label(560, 230, "⟦왔었는지만 알아요 — 레시피 내용은 몰라요|only knows it was here — not the recipe itself⟧", 11, "var(--ink)")
         + label(560, 253, "⟦재료까지 알고 싶으면 모델 인버전이 필요해요|to see the ingredients too, model inversion is needed⟧", 10, "var(--muted)")
         + label(380, 300, "⟦'왔었다'는 사실 하나만으로도 상처가 될 수 있어요 — 그래서 가볍게 볼 공격이 아니에요|the fact alone can hurt — so this is never a small attack⟧", 12, "var(--ink)", cls="d"))

LIMIT_I = icon('<circle cx="28" cy="34" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/>'
               '<path d="M28 22 v12 l9 7" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
               '<rect x="42" y="10" width="7" height="22" rx="3" fill="var(--bad)" transform="rotate(35 45 21)"/>')
FUZZY_I = icon('<path d="M10 40 Q22 20 32 40 Q42 20 54 40" stroke="var(--muted)" stroke-width="4" fill="none" stroke-linecap="round"/>'
               '<circle cx="18" cy="16" r="3" fill="var(--accent)"/><circle cx="32" cy="12" r="3" fill="var(--accent)"/><circle cx="46" cy="16" r="3" fill="var(--accent)"/>')
HIDE_I = icon('<circle cx="32" cy="32" r="14" fill="none" stroke="var(--muted)" stroke-width="4"/>'
              '<circle cx="32" cy="32" r="4" fill="var(--muted)"/>'
              '<path d="M12 12 L52 52" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
AUDIT_I = icon(badge(32, 32, 0.85))

PAGE = {
    "slug": "membershipinference", "order": 11,
    "title": ("눈 감고도 만드는 요리", "The Dish Made with Eyes Closed"),
    "h1": ("<em>멤버십 추론</em>이 뭐예요?", "What is <em>Membership Inference</em>?"),
    "sub": ("멤버십 추론을, 주방장이 어떤 주문은 눈 감고도 척척 만들고 어떤 주문은 머뭇거리는 걸 보고 '이 손님, 연습 때 왔었구나' 알아내는 이야기로 풀어봤어요.",
            "Membership inference, told as a story about watching which orders the chef makes instantly with eyes closed, and which it hesitates over — and guessing from that whether a guest's order was part of practice."),
    "panels": [
        {"svg": P1, "alt": ("몰래 쪽지 손님이 주문서 A(진짜 의심)와 주문서 B(그냥 지어낸 것)를 내밀고, 주방장이 각각 응답함", "The sneaky guest hands over ticket A — the real suspect — and ticket B, which is just made up, and the chef responds to each"),
         "caption": ("몰래 쪽지 손님이 주문서 두 장을 내밀어요 — 하나는 진짜 의심, 하나는 비교용.", "The sneaky guest hands over two tickets — one a real suspect, one just for comparison."),
         "small": ("둘 다 평범한 주문처럼 보여요. 다른 건 주방장이 둘에 반응하는 '느낌'이에요.", "Both look like ordinary orders. What differs is the feel of how the chef reacts to each.")},
        {"svg": P2, "alt": ("주방장은 테스트당하는 걸 모름. 주문서 하나엔 눈 감고도 척척 1초 만에 답하고, 다른 주문서엔 레시피북을 뒤적이며 한참 걸림", "The chef has no idea it's being tested — one ticket gets an instant, eyes-closed answer, while the other has the chef flipping through the recipe book for a long time"),
         "caption": ("테스트당하는 걸 모른 채, 평범하게 반응한 것 자체가 신호가 돼요.", "With no idea it's being tested, the chef just reacts normally — and that reaction itself becomes the signal."),
         "small": ("주방장을 속이려는 게 아니에요. 그냥 보통처럼 반응하게 두고, 그 반응의 속도와 자신감만 지켜봐요.", "There's no trick played on the chef. It just reacts as it normally would — and only the speed and confidence of that reaction are being watched.")},
        {"svg": P3, "hero": True, "alt": ("주문서 A에는 주방장이 눈 감고도 척척 만들어 '연습 때 왔던 손님'으로, 주문서 B에는 머뭇거리며 매번 다르게 만들어 '안 왔던 손님'으로 판정", "For ticket A the chef makes the dish instantly with eyes closed — judged as a guest from practice; for ticket B it hesitates and makes something different each time — judged as a guest never in practice"),
         "caption": ("멤버십 추론은 눈 감고도 만드는 요리와 머뭇거리는 요리를 구별하는 일이에요.", "Membership inference is telling apart the dish made with eyes closed from the one made with hesitation."),
         "small": ("레시피 내용 자체는 몰라도 돼요. '이 주문, 연습 때 본 적 있나요?'라는 예/아니오만 궁금한 거예요.", "The recipe itself doesn't need to be known. All that matters is a yes-or-no: was this order ever seen during practice?"),
         "tricks": (4, [
             (LIMIT_I, ("반복 테스트는 횟수 제한", "Limit how many tests repeat"), ("같은 손님의 잦은 떠보기를 막아요", "blocks a guest from probing too often"), "calm"),
             (FUZZY_I, ("너무 완벽하게 외우지 않기", "Don't let it memorize too perfectly"), ("연습과 실전의 느낌 차이를 줄여요", "shrinks the gap between practice and the real thing"), "calm"),
             (HIDE_I, ("확신 점수는 숨기기", "Hide the confidence score"), ("정확한 숫자를 안 보여줘요", "no precise score handed over"), "warm"),
             (AUDIT_I, ("출시 전 미리 떠보기 시험", "Probe it before release"), ("위생 검사관이 먼저 테스트해요", "the inspector tests it first"), "warm"),
         ])},
        {"svg": P4, "alt": ("반응으로 판정하는 규칙판: 속도·정확도·자신감 세 가지를 보고, ✓가 많으면 왔던 손님으로 판정. 오른쪽에 두 가지 반응 예시", "A rules board for judging by reaction: speed, accuracy, and confidence — more checkmarks means a guest from practice. Two example reactions sit beside it"),
         "caption": ("레시피 자체는 안 봐도, 반응의 속도·정확도·자신감만으로 판정할 수 있어요.", "Without ever seeing the recipe itself, speed, accuracy, and confidence alone are enough to judge."),
         "small": ("세 가지 신호를 같이 보면 더 정확해요. 하나만 보면 틀리기 쉬워요 — 가끔은 안 외운 것도 운 좋게 맞힐 수 있으니까요.", "Looking at all three signals together is more accurate. Relying on just one is easy to get wrong — sometimes an unmemorized order gets a lucky right answer too.")},
        {"svg": P5, "alt": ("왼쪽: 손님이 자신이 왔었다는 사실 자체가 비밀일 수 있다고 걱정. 오른쪽: 몰래 쪽지 손님은 왔었는지만 알고 레시피 내용은 모름, 재료까지 알려면 모델 인버전 필요", "Left: a guest worries that the mere fact they were here could itself be a secret. Right: the sneaky guest only learns that it was there, not the recipe itself — seeing the ingredients too needs model inversion"),
         "caption": ("'왔었다'는 사실 자체가 비밀일 수 있어요. 재료까지 알고 싶으면 모델 인버전이 필요해요.", "The mere fact of having been here can itself be a secret. Seeing the ingredients too needs model inversion."),
         "small": ('이름·전화번호 같은 명부가 아니라, "이 사람의 기록이 학습에 쓰였다" 그 자체가 민감할 수 있어요(예: 어떤 병원 손님 명부였는지). 재료 자체를 거꾸로 그려내는 건 <a href="modelinversion-ko.html">모델 인버전</a>의 몫이에요.',
                   'It isn\'t a list of names and phone numbers — the fact itself that "this person\'s record was used in training" can be sensitive (say, which hospital\'s guest list it came from). Sketching the ingredients themselves backward is the job of <a href="modelinversion-en.html">model inversion</a>.')},
    ],
    "summary": (("<b>멤버십 추론</b> = 어떤 주문에는 주방장이 <b>눈 감고도 척척</b>, 어떤 주문에는 <b>머뭇머뭇</b> 반응하는 걸 보고, 그 손님이 <b>연습 때 왔었는지만</b> 알아내는 일. 레시피 내용은 몰라도 돼요.",
                 "<b>Membership inference</b> = watching the chef respond to one order <b>instantly, with eyes closed</b>, and to another with <b>hesitation</b>, to learn only <b>whether that guest's order was part of practice</b>. The recipe itself never needs to be known."),
                ("Membership Inference. 특정 데이터 샘플이 모델의 학습 데이터셋에 포함되었는지를, 모델의 출력(확신 점수·손실값·응답의 일관성)만으로 추론하는 공격이에요. 모델이 학습 데이터에 과적합(overfitting)할수록 학습한 샘플과 안 한 샘플에 대한 반응 차이가 커져 구별이 쉬워져요. 데이터 자체는 재구성하지 않고 참여 여부만 알아낸다는 점에서 모델 인버전과 다르지만, 의료·금융 기록처럼 '참여 사실' 자체가 민감한 경우 심각한 프라이버시 위험이 돼요.",
                 "An attack that infers, from a model's outputs alone (confidence scores, loss values, response consistency), whether a specific data sample was part of its training set. The more a model overfits to its training data, the bigger the gap between its reaction to seen and unseen samples — making the two easier to tell apart. Unlike model inversion, it never reconstructs the data itself, only whether it participated — but for records like medical or financial data, the fact of participation alone can be a serious privacy risk.")),
    "glossary": [
        ("멤버십 추론", "Membership Inference", ("이 손님이 연습 때 왔었는지만 알아내는 일.", "Finding out only whether a guest's order was part of practice."), ("레시피 내용은 안 봐도 돼요.", "The recipe itself never needs to be seen.")),
        ("모델 인버전", "Model Inversion", ("접시만 보고 원래 재료를 거꾸로 그려내는 일.", "Sketching the original ingredients backward from nothing but the dishes."), ('왔었는지가 아니라 재료 자체가 궁금할 때. → <a href="modelinversion-ko.html">접시 더미에서 되살린 얼굴</a>', 'For when the ingredients themselves matter, not just whether it was there. → <a href="modelinversion-en.html">a face rebuilt from a pile of dishes</a>')),
        ("메모리제이션", "Memorization", ("레시피북 한 줄을 그대로 베껴 내놓는 버릇.", "The habit of serving a line straight out of the recipe book."), ('잘 외울수록 왔었는지 신호도 더 뚜렷해져요. → <a href="memorization-ko.html">외운 걸 그대로 내놓기</a>', 'The better it memorizes, the clearer the was-it-here signal too. → <a href="memorization-en.html">serving what it memorized</a>')),
        ("과적합", "Overfitting", ("연습한 주문만 유난히 완벽하게 외우는 버릇.", "The habit of memorizing only the practiced orders unusually well."), ("연습과 실전의 반응 차이가 클수록 멤버십 추론이 더 잘 통해요.", "The bigger the gap between practice and real reactions, the better membership inference works.")),
        ("확신 점수", "Confidence Score", ("얼마나 자신 있게 답했는지를 보여주는 숫자.", "A number showing how confidently the answer came out."), ("이 숫자가 그대로 공개되면 신호가 더 선명해져요.", "Expose this number directly, and the signal gets much clearer.")),
        ("레드팀", "Red Team", ("출시 전에 미리 떠보기 시험을 해 보는 사람들.", "The people who probe it before release."), ('이런 추론 공격이 통하는지 먼저 확인해요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', 'They check first whether this kind of inference attack works. → <a href="redteam-en.html">the security world\'s red team</a>')),
        ("속도 제한", "Rate Limiting", ("같은 손님의 반복 떠보기를 느리게 또는 막기.", "Slowing or blocking repeated probing from the same guest."), ('반복이 쌓여야 판정이 정확해지는 공격이라 효과가 커요. → <a href="ratelimiting-ko.html">놀이공원의 입장 제한</a>', 'This attack needs many repeats to become accurate, so this helps a lot. → <a href="ratelimiting-en.html">the amusement park\'s entry limit</a>')),
        ("AI 프라이버시", "AI Privacy", ("참여했다는 사실 자체를 지키는 약속.", "The promise that protects the mere fact of having participated."), ('명부 내용뿐 아니라 썼는지 자체도 지켜야 할 비밀이에요. → <a href="aiprivacy-ko.html">앵무새에게 준 비밀 콩</a>', "Not just the list's contents — whether it was used at all is a secret too. → <a href=\"aiprivacy-en.html\">the secret beans we gave the parrot</a>")),
    ],
}
