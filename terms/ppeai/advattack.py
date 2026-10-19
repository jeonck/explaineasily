from _draw import *
from _world import *


def speck_produce(x, y, s=1.0, n=14, seed=3):
    """사람 눈엔 거의 안 보이는 미세한 점무늬를 입힌 농작물."""
    out = f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="var(--good)"/>'
    for i in range(n):
        ang = (i * 47 + seed * 19) % 360
        rad = 6 + (i * 5 + seed) % 9
        px = rad * 0.9 * ((i % 5) - 2) / 2
        py = rad * 0.9 * (((i + 2) % 5) - 2) / 2
        out += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="0.9" fill="var(--bad)" opacity="0.5"/>'
    return out + '</g>'


# 1. 몰래 섞는 사람이 멀쩡해 보이는 사과에 미세한 점무늬를 입혀요
P1 = svg(320, sky(320)
         + person(620, 190, s=0.6, face=FROWN, **CHEATER) + label(620, 265, "⟦몰래 섞는 사람|the one sneaking it in⟧", 11, "var(--muted)")
         + conveyor(140, 230, 420)
         + speck_produce(260, 198, 1.3) + speck_produce(400, 198, 1.1)
         + person(130, 160, s=0.75, face=EYES, **OPERATOR)
         + label(130, 280, "⟦썩은 작물이에요 ×|that's a rotten one ×⟧", 11, "var(--bad)")
         + label(380, 28, "⟦사람 눈엔 멀쩡한 사과인데, 아주 작은 점무늬가 섞여 있어요|to a human eye it's a perfectly fine apple — with a few nearly invisible dots mixed in⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 선별기는 숫자(픽셀)를 보고, 사람은 전체 모양을 봐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 140, s=0.8, face=EYES, **OPERATOR) + label(160, 240, "⟦픽셀 숫자를 더해서 읽어요|reads by adding up pixel numbers⟧", 11, "var(--muted)")
         + speck_produce(400, 130, 1.6)
         + person(620, 140, s=0.8, face=SMILE, **INSPECTOR) + label(620, 240, "⟦모양 전체를 한눈에 봐요|sees the whole shape at a glance⟧", 11, "var(--muted)")
         + label(380, 280, "⟦숫자 몇 개만 살짝 흔들어도, 선별기의 분류 결과는 완전히 뒤집혀요|nudge just a handful of numbers, and the sorter's classification flips completely⟧", 12, "var(--bad)", cls="d"))

NOISE_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="20" cy="22" r="1.4" fill="var(--bad)"/><circle cx="30" cy="34" r="1.4" fill="var(--bad)"/><circle cx="42" cy="24" r="1.4" fill="var(--bad)"/><circle cx="24" cy="44" r="1.4" fill="var(--bad)"/>')
EDGE_I = icon('<path d="M10 44 Q32 10 54 44" stroke="var(--accent)" stroke-width="3" fill="none"/><path d="M10 44 Q32 18 54 44" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 3" fill="none"/>')
STICKER_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="24" y="24" width="16" height="16" rx="2" fill="var(--bad)" transform="rotate(14 32 32)"/>')
RETRY_I = icon('<path d="M46 20 A18 18 0 1 0 46 46" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M46 12 v12 h-12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 3. 적대적 공격 = 분류 결과를 실제로 뒤집도록 입력에 미세한 조작을 더하는 공격 (hero)
P3 = svg(340, sky(340)
         + label(190, 50, "⟦사람이 보는 사진|what a person sees⟧", 11, "var(--muted)", cls="d")
         + speck_produce(190, 150, 1.6) + label(190, 260, "⟦그냥 사과네요|just an apple⟧", 13, "var(--ink)")
         + label(570, 50, "⟦선별기가 읽는 것|what the sorter reads⟧", 11, "var(--muted)", cls="d")
         + bin_(570, 160, 1.2, "⟦불합격함|REJECT BIN⟧", "var(--bad)") + label(570, 260, "⟦이건 불합격이에요 ×|this is a reject ×⟧", 13, "var(--bad)")
         + label(380, 25, "⟦적대적 공격 = 사람 눈엔 똑같지만 분류 결과는 뒤집히도록 입력을 미세하게 조작하는 공격이에요|an adversarial attack subtly perturbs the input so classification flips, though a person sees no difference⟧", 13, "var(--ink)", cls="d"))
# 4. 원본과 조작본 — 분류함이 통째로 바뀌어요
P4 = svg(320, sky(320)
         + label(150, 40, "⟦원본 작물|original produce⟧", 12, "var(--ink)", cls="d")
         + produce(150, 120, 1.2, "var(--good)") + bin_(150, 230, 1.0, "⟦합격함|PASS BIN⟧", "var(--good)")
         + label(430, 40, "⟦미세하게 조작한 작물|subtly perturbed produce⟧", 12, "var(--ink)", cls="d")
         + speck_produce(430, 120, 1.2) + bin_(430, 230, 1.0, "⟦불합격함|REJECT BIN⟧", "var(--bad)")
         + label(650, 150, "⟦사람 눈엔 똑같아요|identical to a human eye⟧", 11, "var(--muted)")
         + label(380, 300, "⟦점무늬 몇 개만 더해도, 떨어지는 분류함이 완전히 바뀌어요|add just a handful of dots, and the bin it lands in changes entirely⟧", 12, "var(--ink)", cls="d"))

# 5. 공격 시점이 달라요 — 학습 전 재료를 상하게 하는 것 vs 다 배운 뒤 눈을 속이는 것
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + person(140, 110, s=0.75, face=FROWN, **CHEATER)
         + label(140, 230, "⟦씨앗(학습 데이터)에 상한 걸 섞어요|mixes rotten items into the seed (training data)⟧", 11, "var(--ink)")
         + label(140, 255, "⟦→ 가르치는 중에 공격해요|→ attacks during teaching⟧", 11, "var(--muted)")
         + speck_produce(570, 130, 1.2)
         + label(570, 230, "⟦다 배운 선별기 앞에 미세 조작 작물을 들이밀어요|holds a perturbed item up to a sorter that's already fully trained⟧", 11, "var(--ink)")
         + label(570, 255, "⟦→ 판정하는 순간에 공격해요|→ attacks at the moment of judging⟧", 11, "var(--bad)")
         + label(380, 295, '⟦씨앗을 상하게 하는 건 <a href="datapoisoning-ko.html">데이터 포이즈닝</a>, 다 배운 뒤 눈을 속이는 건 적대적 공격이에요|spoiling the seed is <a href="datapoisoning-en.html">data poisoning</a> — fooling the eye after training is an adversarial attack⟧', 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "advattack", "order": 3,
    "title": ("작물에 몰래 붙인 가짜 점무늬", "The Fake Dot Pattern Snuck Onto the Produce"),
    "h1": ("<em>적대적 공격</em>이 뭐예요?", "What is an <em>Adversarial Attack</em>?"),
    "sub": ("적대적 공격을, 사람 눈엔 멀쩡한 작물인데 선별기만 완전히 다르게 읽는 이야기로 풀어봤어요.",
            "Adversarial attacks, told as a story about produce that looks perfectly fine to a person but is read entirely differently by the sorter."),
    "panels": [
        {"svg": P1, "alt": ("몰래 섞는 사람이 멀쩡해 보이는 사과에 미세한 점무늬를 입히자 선별기 조작원이 썩은 작물이라고 판정함", "The one sneaking it in dusts an ordinary-looking apple with faint dots, and the operator calls it rotten"),
         "caption": ("사람 눈엔 멀쩡한 사과인데, 선별기는 다르게 읽어요.", "To a human eye it's a fine apple — but the sorter reads it differently."),
         "small": ("아주 작은 점무늬 몇 개가 섞여 있을 뿐이에요.", "Just a handful of nearly invisible dots have been mixed in.")},
        {"svg": P2, "alt": ("선별기 조작원은 픽셀 숫자를 더해서 읽고, 검수반장은 모양 전체를 한눈에 봄", "The operator reads by adding up pixel numbers, while the inspector takes in the whole shape at a glance"),
         "caption": ("선별기는 숫자를 보고, 사람은 모양을 봐요.", "The sorter reads numbers; a person reads shape."),
         "small": ("숫자 몇 개만 흔들어도, 분류 결과는 완전히 뒤집혀요.", "Nudge just a handful of numbers, and the result flips completely.")},
        {"svg": P3, "hero": True, "alt": ("같은 사진을 사람은 그냥 사과로 보지만 선별기는 불합격함에 떨어뜨림", "The same photo looks like a plain apple to a person, but the sorter drops it into the reject bin"),
         "caption": ("사람 눈엔 정상, 선별기 눈엔 완전히 다른 결과예요.", "Normal to a person, entirely different to the sorter."),
         "small": ("입력은 거의 그대로인데, 분류만 완전히 갈라져요.", "The input is almost unchanged — only the classification splits apart."),
         "tricks": (4, [
             (NOISE_I, ("점무늬 덧입히기", "Add a noise pattern"), ("눈엔 안 보이는 점들을 흩뿌려요", "scatter dots too faint to notice"), "warm"),
             (EDGE_I, ("경계선 살짝 비틀기", "Nudge the edges"), ("모양의 가장자리를 조금씩 밀어요", "push the shape's edges a little")),
             (STICKER_I, ("무늬 스티커 붙이기", "Stick on a pattern"), ("실제 작물에 붙여도 통해요", "even works stuck onto the real thing"), "calm"),
             (RETRY_I, ("반복 시도로 찾기", "Search by trial"), ("조작 값을 거듭 맞춰가요", "repeatedly tuning the perturbation")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 원본 작물이 합격함으로 들어감. 오른쪽: 미세 조작한, 사람 눈엔 똑같은 작물이 불합격함으로 들어감", "Left: the original produce lands in the pass bin. Right: a subtly perturbed item, identical to a human eye, lands in the reject bin"),
         "caption": ("점무늬 몇 개만 더해도 분류함이 완전히 바뀌어요.", "Add just a handful of dots, and the bin changes entirely."),
         "small": ("사람 눈엔 똑같지만, 선별기의 판정은 완전히 갈라져요.", "Identical to a human eye — but the sorter's judgment splits completely apart.")},
        {"svg": P5, "alt": ("왼쪽: 씨앗 단계에서 상한 걸 섞는 것. 오른쪽: 다 배운 선별기 앞에 조작된 작물을 들이미는 것", "Left: mixing rotten items into the seed. Right: holding a perturbed item up to an already-trained sorter"),
         "caption": ("공격 시점이 달라요 — 가르치는 중인가, 판정하는 순간인가.", "The timing differs — during teaching, or at the moment of judging."),
         "small": ("씨앗을 상하게 하는 건 데이터 포이즈닝, 다 배운 뒤 속이는 건 적대적 공격이에요.", "Spoiling the seed is data poisoning; fooling it after training is an adversarial attack.")},
    ],
    "summary": (("<b>적대적 공격</b> = 사람 눈엔 <b>똑같아 보이지만</b> 선별기는 <b>완전히 다르게 분류하도록</b> 입력을 미세하게 조작하는 공격.",
                 "<b>Adversarial attack</b> = subtly perturbing an input so it <b>looks the same</b> to a person but the sorter <b>classifies it completely differently</b>."),
                ("적대적 공격(Adversarial Attack)은 사람이 알아챌 수 없을 만큼 작은 변형(노이즈, 패턴)을 입력에 더해, 이미 학습이 끝난 분류 모델의 판정을 공격자가 원하는 대로 틀리게 만드는 추론 단계(inference-time)의 공격이에요. 모델 가중치를 알아야 정교하게 만들 수 있는 화이트박스 공격과, 몰라도 반복 시도로 만들 수 있는 블랙박스 공격으로 나뉘고, 이미지뿐 아니라 음성·텍스트·정형 데이터 분류기에도 똑같은 원리가 적용돼요. 학습 데이터 자체를 오염시키는 데이터 포이즈닝과 달리, 적대적 공격은 이미 다 학습된 모델을 상대로 일어나요.",
                 "An adversarial attack is an inference-time attack that adds a perturbation (noise, a pattern) too small for a human to notice, making an already-trained classifier misjudge exactly the way the attacker wants. White-box attacks, which need knowledge of the model's weights, make a more precise perturbation; black-box attacks, without that knowledge, work by repeated trial. The same principle applies beyond images — to audio, text, and tabular classifiers alike. Unlike data poisoning, which corrupts the training data itself, an adversarial attack targets a model that has already finished learning.")),
    "glossary": [
        ("적대적 공격", "Adversarial attack", ("사람 눈엔 똑같지만 선별기는 다르게 분류하는 조작.", "A perturbation that looks the same but gets classified differently."), ("이미 다 학습된 모델을 상대로 일어나요.", "Happens against a model that has already finished training.")),
        ("데이터 포이즈닝", "Data poisoning", ("씨앗(학습 데이터) 자체를 상하게 하는 것.", "Spoiling the seed — the training data itself."), ('공격 시점이 달라요(학습 중). → <a href="datapoisoning-ko.html">주방 세계의 데이터 포이즈닝</a>', 'A different attack timing — during training. → <a href="datapoisoning-en.html">the kitchen world\'s data poisoning</a>')),
        ("미세 조작(perturbation)", "Perturbation", ("눈엔 안 보이는 작은 변형.", "A small change too faint to notice."), ("점무늬나 경계선을 살짝 흔들어요.", "A slight nudge to dots or edges.")),
        ("화이트박스 · 블랙박스", "White-box · black-box", ("선별기의 속 기준을 아는지, 모르고 시도만 하는지.", "Whether you know the sorter's inner rule, or only try by trial."), ("속 기준을 알면 훨씬 더 정교하게 조작할 수 있어요.", "Knowing the inner rule lets the perturbation be far more precise.")),
        ("오분류", "Misclassification", ("분류함을 잘못 떨어뜨리는 것.", "Dropping something into the wrong bin."), ("적대적 공격이 노리는 바로 그 결과예요.", "The outcome an adversarial attack is built to cause.")),
        ("혼동행렬", "Confusion matrix", ("합격·불합격 도장을 네 칸으로 정리한 표.", "The four-box table sorting pass/fail stamps."), ('적대적 공격이 섞이면 이 표의 숫자가 무너져요. → <a href="confmatrix-ko.html">네 칸으로 나눈 도장 기록부</a>', 'An adversarial attack quietly wrecks these numbers. → <a href="confmatrix-en.html">The Four-Box Stamp Ledger</a>')),
        ("이상치", "Outlier", ("유난히 튀는 작물 한 개.", "The one item that stands out from the rest."), ('방어 중 하나가 바로 이걸 찾는 거예요. → <a href="outlier-ko.html">무리에서 유난히 튀는 작물</a>', 'One defense is exactly this: spotting it. → <a href="outlier-en.html">The Produce That Stands Out from the Crowd</a>')),
        ("이미지 인젝션(LLM/비전 각도)", "Image injection (LLM/vision angle)", ("사람이 메뉴판 사진을 읽는 가게 세계의 같은 뿌리 공격.", "The same-rooted attack in the world where a person reads a menu photo."), ('LLM이 사진 속 명령을 읽는 각도는 주방 세계에서 다뤄요. → <a href="adversarialexample-ko.html">눈속임 그림 주문서</a>', 'The angle where an LLM reads a hidden command in a photo lives in the kitchen world. → <a href="adversarialexample-en.html">The Picture Order That Fools the Eye</a>')),
    ],
}
