from _draw import *
from _world import *

ARROW = '<path d="M{0} {1} L{2} {3}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'


def cards(x, y, n, s=0.8, title="⟦예시|EXAMPLE⟧", line="⟦정산 → 표|settle → sheet⟧", dx=6, dy=8):
    return "".join(note(x + i * dx, y + i * dy, 100, 60, title, (line,), s) for i in range(n))


# 1. 특훈에 예시 500장이 필요한데, 사람이 쓰기엔 너무 오래 걸려요
P1 = svg(300, sky(300)
         + person(90, 110, s=1.0, face=FROWN, extra=SWEAT, **TRAINER) + label(120, 250, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + bubble(30, 20, 220, 40, "⟦한 장에 한 시간…|an hour per card…⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + cards(190, 150, 3, 0.8, "⟦예시|EXAMPLE⟧", "⟦정산 → 표|settle → sheet⟧") + label(240, 130, "⟦지금까지 3장|3 so far⟧", 11, "var(--muted)")
         + note(400, 50, 160, 90, "⟦특훈 준비물|DRILL NEEDS⟧", ("⟦우리 예시 500장|500 of our examples⟧", "⟦지금: 3장|so far: 3⟧"), 1.0, 1)
         + parrot(480, 210, 0.9, mood="think") + label(480, 262, "⟦기다리는 앵무새|the waiting parrot⟧", 11, "var(--muted)")
         + '<circle cx="660" cy="120" r="42" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/><path d="M660 120 V88 M660 120 L684 132" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/>'
         + label(660, 190, "⟦한 달 넘게 걸려요|more than a month⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦특훈엔 예시 500장이 필요한데, 사람이 쓰기엔 너무 오래 걸려요|the drill needs 500 examples — far too slow to write by hand⟧", 13, "var(--ink)"))

# 2. 왜: 진짜 예시는 비싸고, 비밀 콩이 섞여 있어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + "".join(f'<ellipse cx="130" cy="{215 - i * 9}" rx="26" ry="9" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>' for i in range(6))
         + label(130, 250, "⟦한 장 한 장이 돈이에요|every card costs money⟧", 12, "var(--ink)")
         + person(210, 90, s=0.9, face=FROWN, extra=SWEAT, **TRAINER)
         + cards(60, 60, 3, 0.7, "⟦예시|EXAMPLE⟧", "⟦정산 → 표|settle → sheet⟧") + label(110, 40, "⟦사람이 쓴 예시|hand-written examples⟧", 11, "var(--muted)")
         + label(340, 160, "⟦+|+⟧", 40, "var(--muted)", cls="d")
         + note(420, 50, 220, 110, "⟦진짜 예시|REAL EXAMPLE⟧", ("⟦손님 김OO 문의:|guest Kim asks:⟧", "⟦010-1234 로 연락 주세요|please call 010-1234⟧", "⟦카드 4321… 환불|refund card 4321…⟧"), 1.0, 1)
         + bean(530, 200, 1.2, "var(--bad)", "⟦010…|010…⟧") + bean(590, 200, 1.2, "var(--bad)", "⟦4321|4321⟧")
         + label(560, 250, "⟦진짜 손님 이야기엔 비밀 콩이 섞여요|real guest stories carry secret beans⟧", 11, "var(--bad)")
         + label(380, 300, "⟦진짜 예시는 비싸고, 비밀 콩이 섞여 있어요|real examples are expensive — and carry secret beans⟧", 12, "var(--bad)"))

# 3. 합성 데이터 = 큰 앵무새에게 예시를 잔뜩 쓰게 해서 작은 앵무새를 가르치는 것 (hero)
P3 = svg(360, sky(360)
         + person(30, 150, s=0.85, face=SMILE, **TRAINER) + label(60, 270, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + cards(110, 50, 3, 0.8, "⟦씨앗|SEED⟧", "⟦정산 → 표|settle → sheet⟧", 6, 5) + label(165, 130, "⟦씨앗 카드 10장 (사람이)|10 seed cards, by hand⟧", 11, "var(--muted)")
         + ARROW.format(215, 100, 262, 150)
         + perch(300, 250, 150) + parrot(300, 210, 1.4, color=PARROT_BIG, talk=True) + label(300, 305, "⟦큰 앵무새|big parrot⟧", 11, "var(--muted)")
         + ARROW.format(345, 170, 400, 130)
         + cards(410, 60, 5, 0.8, "⟦예시|EXAMPLE⟧", "⟦…|…⟧", 8, 10) + label(470, 175, "⟦카드 500장|500 cards⟧", 12, "var(--ink)", cls="d")
         + ARROW.format(525, 120, 600, 200)
         + perch(660, 250, 100) + parrot(660, 218, 0.8) + label(660, 305, "⟦작은 앵무새 특훈|small parrot\'s drill⟧", 11, "var(--muted)")
         + label(380, 340, "⟦합성 데이터 = 큰 앵무새에게 예시를 잔뜩 쓰게 해서 작은 앵무새를 가르치는 것|synthetic data: have the big parrot write piles of examples, then teach the small one with them⟧", 12, "var(--ink)", cls="d"))

# 4. 흐름: 씨앗 10장 → 큰 앵무새 → 500장 → 사람이 골라냄 → 작은 앵무새 특훈
P4 = svg(320, sky(320)
         + cards(20, 80, 2, 0.8, "⟦씨앗|SEED⟧", "⟦10장|10 cards⟧", 5, -5) + label(60, 170, "⟦씨앗 10장|10 seeds⟧", 11, "var(--muted)")
         + ARROW.format(105, 110, 135, 130)
         + perch(190, 190, 110) + parrot(190, 142, 1.2, color=PARROT_BIG, talk=True) + label(190, 250, "⟦큰 앵무새가 써요|the big parrot writes⟧", 11, "var(--muted)")
         + ARROW.format(240, 120, 275, 110)
         + cards(280, 60, 4, 0.8, "⟦예시|EXAMPLE⟧", "⟦…|…⟧", 6, 8) + label(330, 165, "⟦500장|500 cards⟧", 12, "var(--ink)", cls="d")
         + ARROW.format(378, 110, 405, 110)
         + person(410, 60, s=0.85, face=EYES, **EXAMINER)
         + note(475, 50, 100, 90, "⟦골라내기|FILTER⟧", ("⟦틀린 것 ×|wrong ×⟧", "⟦똑같은 것 ×|duplicate ×⟧", "⟦남은 것 ✓|kept ✓⟧"), 0.9)
         + label(490, 185, "⟦사람이 골라내요 → 420장|a person filters → 420 kept⟧", 11, "var(--ink)")
         + ARROW.format(570, 110, 600, 130)
         + perch(650, 200, 90) + parrot(650, 170, 0.8) + label(650, 250, "⟦작은 앵무새 특훈|small parrot\'s drill⟧", 11, "var(--muted)")
         + label(380, 300, "⟦씨앗 10장 → 큰 앵무새 → 500장 → 사람이 골라냄 → 작은 앵무새 특훈|10 seeds → big parrot → 500 cards → a person filters → the small parrot\'s drill⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 앵무새가 쓴 책만 계속 먹이면 점점 이상해져요(모델 붕괴) — 진짜 책을 섞어요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(110, 140, 1.0, talk=True)
         + books(250, 220, 4, 1.0) + label(250, 150, "⟦진짜 책|real books⟧", 11, "var(--ink)", cls="d")
         + label(320, 120, "⟦+|+⟧", 26, "var(--muted)", cls="d")
         + note(200, 40, 120, 60, "⟦합성|SYNTHETIC⟧", ("⟦카드 420장|420 cards⟧",), 0.9)
         + label(230, 255, "⟦진짜 책 + 합성 카드 섞기|real books + synthetic cards⟧", 11, "var(--ink)")
         + label(190, 300, "⟦섞어서 먹이면 잘 자라요|mixed feed, healthy parrot⟧", 12, "var(--good)", cls="d")
         + parrot(450, 130, 1.0) + label(450, 60, "⟦1대|gen 1⟧", 11, "var(--muted)")
         + ARROW.format(480, 130, 525, 130) + parrot(560, 130, 1.0, mood="sweat") + label(560, 60, "⟦2대|gen 2⟧", 11, "var(--muted)")
         + ARROW.format(590, 130, 635, 130) + parrot(670, 130, 1.0, color=PARROT_BAD, mood="sweat") + label(670, 60, "⟦3대|gen 3⟧", 11, "var(--muted)")
         + "".join(cards(420 + i * 110, 195, 2, 0.5, "⟦앵무새 책|PARROT BOOK⟧", "⟦…|…⟧", 4, 4) for i in range(3))
         + label(560, 262, "⟦앵무새가 쓴 책만 먹이면 대마다 점점 이상해져요|fed only parrot-written books, each generation gets stranger⟧", 10, "var(--bad)")
         + label(570, 300, "⟦= 모델 붕괴|= model collapse⟧", 12, "var(--bad)", cls="d"))

SEED_I = icon('<rect x="14" y="12" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 26 h20 M22 36 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 52 l14 -14 l4 4 l-14 14z" fill="var(--accent)"/>')
VARIETY_I = icon('<circle cx="18" cy="20" r="9" fill="#7B3FA0"/><rect x="36" y="11" width="18" height="18" rx="3" fill="#2E7D6B"/><path d="M18 36 l10 18 h-20z" fill="#C9822B"/><path d="M45 36 l9 9 l-9 9 l-9 -9z" fill="#5B8DEF"/>')
FILTER_I = icon('<circle cx="26" cy="26" r="13" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M36 36 l12 12" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M20 20 l12 12 M32 20 l-12 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><path d="M44 12 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
NOSECRET_I = icon(f'<ellipse cx="32" cy="36" rx="18" ry="12" fill="{BEAN}"/><path d="M22 32 q10 -6 20 0" stroke="#5A3B22" stroke-width="2" fill="none"/><circle cx="48" cy="18" r="10" fill="var(--good)"/><path d="M43 18 l4 4 l7 -7" stroke="#FFF" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "synthetic", "order": 40,
    "title": ("앵무새가 쓴 책으로 앵무새 가르치기", "Teaching a Parrot With Parrot-Written Books"),
    "h1": ("<em>합성 데이터</em>가 뭐예요?", "What is <em>Synthetic Data</em>?"),
    "sub": ("합성 데이터를, 큰 앵무새에게 예시 카드를 잔뜩 쓰게 해서 작은 앵무새의 특훈 교재로 쓰는 이야기로 풀어봤어요.",
            "Synthetic data, told as a story about having the big parrot write piles of example cards to use as the small parrot\'s drill material."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 조련사가 '한 장에 한 시간'이라며 예시 카드 3장을 들고 있고, 쪽지엔 '우리 예시 500장 필요, 지금 3장'. 시계 옆에 '한 달 넘게 걸려요'", "A sweating trainer says an hour per card, holding 3 example cards; a note says 500 examples needed, 3 so far; a clock reads more than a month"),
         "caption": ("특훈엔 우리 예시 500장이 필요한데, 사람이 쓰기엔 너무 오래 걸려요.", "The drill needs 500 of our examples — far too slow to write by hand."),
         "small": ('<a href="finetune-ko.html">짧은 특훈</a>은 예시 카드로 해요. 몇백 장이 필요한데, 한 장에 한 시간이면 한 달이 넘어요.',
                   'The <a href="finetune-en.html">short drill</a> runs on example cards. It needs a few hundred; at an hour each, that is over a month.')},
        {"svg": P2, "alt": ("동전 더미와 땀 흘리는 조련사가 쓴 예시 몇 장, 더하기, 진짜 예시 카드엔 '010-1234 로 연락, 카드 4321 환불'과 빨간 비밀 콩", "A pile of coins and a few hand-written examples from a sweating trainer, plus a real example card reading call 010-1234, refund card 4321 with red secret beans"),
         "caption": ("진짜 예시는 비싸고, 비밀 콩이 섞여 있어요.", "Real examples are expensive — and carry secret beans."),
         "small": ('사람이 쓰면 한 장 한 장이 돈이에요. 진짜 손님 이야기를 그대로 쓰면 전화번호·카드 같은 <a href="aiprivacy-ko.html">비밀 콩</a>이 특훈 교재에 들어가요.',
                   'Hand-written cards cost money one by one. Using real guest stories as they are puts <a href="aiprivacy-en.html">secret beans</a> — phone numbers, cards — into the drill material.')},
        {"svg": P3, "hero": True, "alt": ("조련사가 쓴 씨앗 카드 10장이 큰 앵무새로 가고, 큰 앵무새가 카드 500장을 써내면 그 카드가 작은 앵무새의 특훈으로 감", "Ten seed cards from the trainer go to the big parrot, which writes 500 cards, and those cards go to the small parrot\'s drill"),
         "caption": ("합성 데이터는 큰 앵무새에게 예시를 잔뜩 쓰게 해서 작은 앵무새를 가르치는 거예요.", "Synthetic data is having the big parrot write piles of examples, then teaching the small one with them."),
         "small": ('사람은 씨앗 카드 몇 장만 써요. 나머지는 큰 앵무새가 흉내 내서 채워요. <a href="distillation-ko.html">작은 앵무새에게 흉내 가르치기</a>와 친척이에요.',
                   'People write only a few seed cards; the big parrot fills in the rest by imitation. A close cousin of <a href="distillation-en.html">teaching the small parrot to imitate</a>.'),
         "tricks": (4, [
             (SEED_I, ("씨앗은 사람이", "Seeds by hand"), ("좋은 예시 몇 장이 기준", "a few good cards set the standard"), "calm"),
             (VARIETY_I, ("다양하게 시켜요", "Ask for variety"), ("같은 것 500장은 ×", "500 of the same is ×"), "calm"),
             (FILTER_I, ("사람이 골라내요", "A person filters"), ("틀린 것·똑같은 것 ×", "wrong and duplicate cards out"), "warm"),
             (NOSECRET_I, ("비밀 콩 없이", "No secret beans"), ("지어낸 이름·번호로 만들어요", "made-up names and numbers"), "warm"),
         ])},
        {"svg": P4, "alt": ("씨앗 10장 → 큰 앵무새 → 카드 500장 → 시험관이 '틀린 것 ×, 똑같은 것 ×, 남은 것 ✓'로 골라내 420장 → 작은 앵무새 특훈", "10 seeds → big parrot → 500 cards → an examiner filters (wrong ×, duplicate ×, kept ✓) to 420 → the small parrot\'s drill"),
         "caption": ("씨앗 10장, 카드 500장, 사람이 골라내서 420장, 그걸로 특훈해요.", "Ten seeds, 500 cards, a person keeps 420, and the drill runs on those."),
         "small": ('큰 앵무새도 <a href="hallucination-ko.html">그럴듯한 거짓말</a>을 섞어 써요. 그래서 사람이 골라내고, 남은 카드가 얼마나 좋은지는 <a href="evaluation-ko.html">시험관의 채점표</a>로 재요.',
                   'The big parrot slips in <a href="hallucination-en.html">plausible lies</a> too. So a person filters, and the <a href="evaluation-en.html">examiner\'s score sheet</a> measures how good the kept cards are.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새에게 진짜 책과 합성 카드 420장을 섞어 먹임. 오른쪽 빨강: 앵무새가 쓴 책만 먹인 1대·2대·3대 앵무새가 점점 땀 흘리고 빨개짐 — 모델 붕괴", "Left, green: the parrot is fed real books plus 420 synthetic cards. Right, red: generations 1, 2, 3 fed only parrot-written books sweat more and turn red — model collapse"),
         "caption": ("앵무새가 쓴 책만 계속 먹이면 점점 이상해져요. 진짜 책을 꼭 섞어요.", "Fed only parrot-written books, the parrot gets stranger each generation. Always mix in real books."),
         "small": ('앵무새가 쓴 책은 진짜 책의 흉내라, 흉내의 흉내를 거듭하면 드문 것부터 사라져요(모델 붕괴). 그래서 합성은 <a href="finetune-ko.html">특훈</a>의 보조이지, 책 산더미를 대신하진 못해요.',
                   'A parrot-written book imitates real ones; imitations of imitations lose the rare things first (model collapse). So synthetic data assists the <a href="finetune-en.html">drill</a> — it never replaces the mountain of books.')},
    ],
    "summary": (("<b>합성 데이터</b> = 사람이 쓴 <b>씨앗 카드 몇 장</b>을 주고 <b>큰 앵무새에게 예시를 잔뜩 쓰게</b> 해서, 사람이 골라낸 뒤 <b>작은 앵무새를 가르치는</b> 교재. 비밀 콩 없이 싸게 많이 만들지만, 앵무새 책만 먹이면 <b>점점 이상해져요</b>.",
                 "<b>Synthetic data</b> = give a few <b>hand-written seed cards</b>, have <b>the big parrot write piles of examples</b>, let a person filter them, and <b>teach the small parrot</b> with the rest. Cheap, plentiful, free of secret beans — but a parrot fed only parrot books <b>gets stranger</b>."),
                ("Synthetic Data. 큰 모델로 학습·평가용 예시를 생성하는 방법이에요. 씨앗 데이터로 방향을 잡고, 다양성을 강제하고, 품질 필터링(중복·오류 제거)을 거쳐 파인튜닝이나 증류에 써요. 개인정보 없는 데이터를 만들 수 있지만, 모델 출력만 반복 학습하면 분포 꼬리가 사라지는 모델 붕괴가 생겨 실제 데이터를 섞어야 해요.",
                 "Generating training and evaluation examples with a large model. Seed data sets the direction, diversity is enforced, and quality filtering (deduplication, error removal) precedes fine-tuning or distillation. It can produce data free of personal information, but training repeatedly on model output alone erases the tails of the distribution (model collapse), so real data must be mixed in.")),
    "glossary": [
        ("합성 데이터", "Synthetic data", ("앵무새가 쓴 예시 카드.", "Example cards the parrot wrote."), ("사람이 쓴 게 아니라 큰 앵무새가 흉내 내서 만든 교재예요.", "Drill material made by the big parrot\'s imitation, not by people.")),
        ("데이터 증강", "Data augmentation", ("있는 카드를 조금씩 바꿔 늘리기.", "Stretching the cards you have."), ("말투 바꾸기, 순서 바꾸기, 이름 바꾸기로 한 장을 여러 장으로.", "Change the tone, the order, the names — one card becomes many.")),
        ("모델 붕괴", "Model collapse", ("흉내의 흉내를 거듭해 이상해짐.", "Imitations of imitations going strange."), ("앵무새 책만 먹이면 드문 것부터 사라져요. 진짜 책을 섞어요.", "Fed only parrot books, the rare things vanish first. Mix in real books.")),
        ("씨앗 데이터", "Seed data", ("사람이 쓴 처음 몇 장.", "The first few cards, by hand."), ("큰 앵무새가 흉내 낼 기준이에요. 씨앗이 나쁘면 500장이 다 나빠요.", "The standard the big parrot imitates. Bad seeds make 500 bad cards.")),
        ("품질 필터링", "Quality filtering", ("사람이 골라내기.", "A person sorting the cards."), ('틀린 것·똑같은 것을 빼요. 얼마나 좋은지는 → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Wrong and duplicate cards go out. How good the rest are: → <a href="evaluation-en.html">the examiner\'s score sheet</a>')),
        ("증류", "Distillation", ("큰 앵무새 흉내를 작은 앵무새에게.", "The big parrot\'s ways, taught to the small one."), ('합성 데이터의 친척이에요. → <a href="distillation-ko.html">작은 앵무새에게 흉내 가르치기</a>', 'A cousin of synthetic data. → <a href="distillation-en.html">teaching the small parrot to imitate</a>')),
        ("파인튜닝", "Fine-tuning", ("예시 카드로 하는 짧은 특훈.", "The short drill on example cards."), ('합성 카드를 쓰는 곳이에요. → <a href="finetune-ko.html">짧은 특훈</a>', 'Where the synthetic cards get used. → <a href="finetune-en.html">the short drill</a>')),
        ("프라이버시", "Privacy", ("비밀 콩 없이 만들기.", "Made without secret beans."), ('지어낸 이름·번호로 만들면 진짜 손님 정보가 안 들어가요. → <a href="aiprivacy-ko.html">앵무새에게 준 비밀 콩</a>', 'Made-up names and numbers keep real guest data out. → <a href="aiprivacy-en.html">the secret beans we gave the parrot</a>')),
    ],
}
