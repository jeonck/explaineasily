from _draw import *
from _world import *


def scale_(x, y, w, readout, big=True):
    """저울. 접시 위 중심은 (x, y-16). big=True 면 굵고 무거운 정밀 저울."""
    sw = 3 if big else 2
    return (f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="{18 if big else 12}" rx="4" fill="var(--stone-dark)"/>'
            f'<rect x="{x - 6}" y="{y - 16}" width="12" height="16" fill="var(--stone-dark)"/>'
            f'<rect x="{x - w / 2 - 6}" y="{y - 22}" width="{w + 12}" height="8" rx="3" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="{sw}"/>'
            f'<rect x="{x - w / 2 + 6}" y="{y + 2 if big else y + 1}" width="{w - 12}" height="{14 if big else 10}" rx="3" fill="#142033"/>'
            + label(x, y + 13 if big else y + 9, readout, 11 if big else 10, "#7CE0A6", cls="d"))


def ruler(x, y, w, step):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + "".join(f'<path d="M{x + i} {y} v{9 if (i // step) % 5 == 0 else 5}" stroke="#142033" stroke-width="1.5"/>' for i in range(0, w + 1, step)))


ARROW = '<path d="M{0} {2} L{1} {2}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M{3} {4} L{1} {2} L{3} {5}" stroke="var(--muted)" stroke-width="3" fill="none"/>'


def arrow(x0, x1, y):
    return ARROW.format(x0, x1, y, x1 - 10, y - 8, y + 8)


# 1. 큰 앵무새를 우리 집 작은 횃대(노트북·폰)에 올리고 싶은데 무거워요
PHONE = ('<rect x="500" y="70" width="80" height="150" rx="12" fill="var(--stone-dark)"/><rect x="507" y="84" width="66" height="122" rx="6" fill="var(--sky)"/>'
         + perch(540, 180, 44) + '<circle cx="540" cy="213" r="4" fill="var(--stone)"/>')
P1 = svg(300, sky(300) + perch(200, 200, 150) + parrot(200, 160, 1.5, color=PARROT_BIG, mood="sweat")
         + label(200, 262, "⟦큰 앵무새 — 무거워요|the big parrot — heavy⟧", 12, "var(--ink)", cls="d")
         + arrow(290, 470, 130) + label(380, 118, "⟦올리고 싶은데…|want to put it here…⟧", 11, "var(--muted)")
         + label(380, 170, "⟦×|×⟧", 40, "var(--bad)", cls="d")
         + PHONE + label(540, 250, "⟦우리 집 작은 횃대 (폰·노트북)|our small perch (phone, laptop)⟧", 11, "var(--muted)")
         + person(640, 110, s=0.8, face=FROWN, **GUEST)
         + label(380, 282, "⟦작은 횃대엔 큰 앵무새가 올라가지 않아요 — 자리가 없어요|the big parrot will not fit on the small perch — no room⟧", 12, "var(--ink)"))

# 2. 왜: 머릿속 숫자가 수십억 개, 하나하나 아주 정밀하게 적혀 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(100, 160, 1.3, color=PARROT_BIG, mood="think") + label(100, 262, "⟦앵무새 머릿속|inside its head⟧", 11, "var(--muted)")
         + note(190, 40, 240, 150, "⟦머릿속 숫자|NUMBERS IN ITS HEAD⟧", ("⟦0.48231937|0.48231937⟧", "⟦-0.13920471|-0.13920471⟧", "⟦0.77219003|0.77219003⟧", "⟦… ×수십억 개|… ×billions⟧"), 0.95)
         + label(310, 225, "⟦하나하나 소수점 여덟 자리|each one to eight decimal places⟧", 11, "var(--ink)")
         + scale_(600, 170, 180, "⟦0.48231937 kg|0.48231937 kg⟧", True)
         + label(600, 120, "⟦소수점 여덟 자리 저울|an eight-decimal scale⟧", 11, "var(--muted)")
         + label(600, 220, "⟦정밀할수록 크고 무거워요|the finer, the bigger and heavier⟧", 11, "var(--ink)")
         + label(380, 282, "⟦숫자가 수십억 개인데 하나하나 정밀하게 적혀 있으니 자리가 커요|billions of numbers, each written finely — that takes a lot of room⟧", 12, "var(--bad)"))

# 3. 양자화 = 정밀한 숫자를 굵은 눈금으로 다시 적어 앵무새를 가볍게 (hero)
P3 = svg(360, sky(360)
         + ruler(40, 30, 260, 5) + label(170, 66, "⟦촘촘한 눈금|fine ticks⟧", 11, "var(--muted)")
         + ruler(460, 30, 260, 40) + label(590, 66, "⟦굵은 눈금|coarse ticks⟧", 11, "var(--muted)")
         + parrot(120, 200, 1.4, color=PARROT_BIG) + note(190, 85, 120, 70, "⟦숫자|NUMBERS⟧", ("⟦0.4823|0.4823⟧", "⟦-0.1392|-0.1392⟧"), 0.95)
         + label(120, 285, "⟦정밀하게 적힌 앵무새 — 무거워요|finely written — heavy⟧", 11, "var(--ink)")
         + arrow(330, 430, 200) + label(380, 182, "⟦굵게 다시 적어요|rewrite coarsely⟧", 11, "var(--muted)")
         + parrot(500, 205, 1.0) + note(560, 85, 120, 70, "⟦숫자|NUMBERS⟧", ("⟦0.5|0.5⟧", "⟦-0.1|-0.1⟧"), 0.95)
         + label(500, 285, "⟦굵게 적힌 앵무새 — 가볍고 조금 둔해요|coarsely written — light, a bit duller⟧", 11, "var(--ink)")
         + label(380, 340, "⟦양자화 = 정밀한 숫자를 굵은 눈금으로 다시 적어 앵무새를 가볍게 만들기|quantization: rewrite the fine numbers on a coarse scale, and the parrot gets light⟧", 13, "var(--ink)", cls="d"))

# 4. 저울 비교 + 앵무새 크기 변화 + 점수표
P4 = svg(320, sky(320)
         + parrot(120, 130, 1.3, color=PARROT_BIG) + scale_(120, 200, 170, "⟦0.48231937 kg|0.48231937 kg⟧", True)
         + label(120, 250, "⟦정밀 저울 · 무거움|fine scale · heavy⟧", 11, "var(--ink)", cls="d")
         + arrow(220, 280, 150)
         + parrot(340, 150, 0.9) + scale_(340, 200, 110, "⟦0.5 kg|0.5 kg⟧", False)
         + label(340, 250, "⟦굵은 눈금 저울 · 가벼움|coarse scale · light⟧", 11, "var(--ink)", cls="d")
         + note(450, 50, 280, 180, "⟦시험 점수 (우리 일)|TEST SCORE (OUR JOB)⟧", ("⟦원래 앵무새 · 100점 · 16 GB|original · 100 · 16 GB⟧", "⟦8비트 굵게 · 99점 · 8 GB|8-bit coarse · 99 · 8 GB⟧", "⟦4비트 더 굵게 · 96점 · 4 GB|4-bit coarser · 96 · 4 GB⟧", "⟦2비트 아주 굵게 · 70점 · 2 GB|2-bit very coarse · 70 · 2 GB⟧"), 0.95, hl=2)
         + label(590, 255, "⟦눈금이 굵을수록 가볍고, 점수는 조금씩 떨어져요|coarser ticks: lighter, and the score slips a little⟧", 11, "var(--muted)")
         + label(380, 300, "⟦8비트·4비트는 보통 괜찮고, 너무 굵으면 확 둔해져요 — 시험으로 골라요|8-bit and 4-bit are usually fine; too coarse and it gets dull — pick by test⟧", 11, "var(--ink)"))

# 5. 어떤 일(수학·긴 추론)은 굵은 눈금에 민감해요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(100, 150, 1.0, talk=True) + bubble_parrot(40, 40, 200, 40, "⟦요약이에요: 회의는 3시|summary: the meeting is at 3⟧", 11)
         + note(200, 110, 150, 90, "⟦괜찮은 일|FINE JOBS⟧", ("⟦요약 · 번역 · 분류|summary · translation · sorting⟧", "⟦짧은 답|short answers⟧"), 0.95)
         + label(190, 262, "⟦굵게 적어도 거의 그대로예요|nearly the same even when coarse⟧", 11, "var(--ink)")
         + parrot(480, 150, 1.0, color=PARROT_BAD, mood="sweat", talk=True) + bubble_parrot(420, 40, 200, 40, "⟦12 × 13 = 146… 인가?|12 × 13 = 146… maybe?⟧", 11, bad=True)
         + note(580, 110, 150, 90, "⟦민감한 일|SENSITIVE JOBS⟧", ("⟦수학 · 긴 추론|math · long reasoning⟧", "⟦긴 코드|long code⟧"), 0.95)
         + label(570, 262, "⟦굵은 눈금에 확 둔해지는 일이 있어요|some jobs go dull fast on coarse ticks⟧", 11, "var(--ink)")
         + label(380, 300, "⟦굵은 눈금이 모자라면 다른 길: 작은 앵무새를 새로 가르쳐요(증류)|if coarse ticks fall short, take the other road: teach a new small parrot (distillation)⟧", 12, "var(--ink)", cls="d"))

BITS_I = icon('<rect x="8" y="14" width="48" height="16" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M12 14 v6 M18 14 v6 M24 14 v6 M30 14 v6 M36 14 v6 M42 14 v6 M48 14 v6" stroke="#142033" stroke-width="1.5"/><rect x="8" y="38" width="48" height="16" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M12 38 v8 M32 38 v8 M52 38 v8" stroke="#142033" stroke-width="2"/>')
EXAM_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 30 h20 M22 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><text x="44" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">98</text>')
PHONE_I = icon(f'<rect x="18" y="6" width="28" height="52" rx="6" fill="var(--stone-dark)"/><rect x="21" y="11" width="22" height="40" rx="3" fill="var(--sky)"/><ellipse cx="32" cy="34" rx="6" ry="8" fill="{PARROT}"/><circle cx="32" cy="24" r="5" fill="{PARROT}"/><path d="M36 22 l6 2 l-6 3z" fill="#E9B44C"/>')
ORDER_I = icon('<rect x="6" y="20" width="20" height="24" rx="4" fill="var(--good)"/><text x="16" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF">1</text><path d="M28 32 h8" stroke="var(--muted)" stroke-width="3"/><path d="M33 26 l6 6 l-6 6" stroke="var(--muted)" stroke-width="3" fill="none"/><rect x="38" y="20" width="20" height="24" rx="4" fill="var(--accent)"/><text x="48" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF">2</text>')

PAGE = {
    "slug": "quantization", "order": 28,
    "title": ("콩을 굵게 세기", "Counting Beans Coarsely"),
    "h1": ("<em>양자화</em>가 뭐예요?", "What is <em>Quantization</em>?"),
    "sub": ("양자화(quantization)를, 앵무새 머릿속의 정밀한 숫자를 굵은 눈금으로 다시 적어 가볍게 만드는 이야기로 풀어봤어요.",
            "Quantization, told as a story about rewriting the fine numbers in a parrot\'s head on a coarse scale so it gets light."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 큰 앵무새에서 폰 속 작은 횃대로 점선 화살표와 빨간 ×. 손님이 찡그림", "A dashed arrow with a red × from a sweating big parrot to a tiny perch inside a phone; a frowning guest"),
         "caption": ("큰 앵무새를 우리 집 작은 횃대(폰·노트북)에 올리고 싶은데, 너무 무거워요.", "We want the big parrot on our small perch (phone, laptop), but it is far too heavy."),
         "small": ("큰 앵무새 학교의 큰 횃대에서만 살 수 있어요. 우리 집에 데려오려면 가벼워져야 해요.", "It can only live on the big perch at parrot school. To bring it home, it has to get lighter.")},
        {"svg": P2, "alt": ("생각하는 큰 앵무새 옆에 '머릿속 숫자: 0.48231937, -0.13920471, … ×수십억 개' 쪽지, 오른쪽엔 '0.48231937 kg'을 보여주는 큰 정밀 저울", "A thinking big parrot beside a note listing numbers like 0.48231937 and -0.13920471, billions of them; on the right a big fine scale reading 0.48231937 kg"),
         "caption": ("앵무새 머릿속엔 숫자가 수십억 개, 하나하나 아주 정밀하게 적혀 있어요.", "The parrot\'s head holds billions of numbers, each written very finely."),
         "small": ("소수점 여덟 자리 저울은 크고 무겁죠. 숫자 하나하나가 그런 저울로 적혀 있으니 앵무새가 무거운 거예요.", "An eight-decimal scale is big and heavy. Every number is written on a scale like that — so the parrot is heavy.")},
        {"svg": P3, "hero": True, "alt": ("위엔 촘촘한 눈금 자와 굵은 눈금 자. 아래엔 '0.4823, -0.1392' 쪽지를 든 큰 앵무새에서 '0.5, -0.1' 쪽지를 든 작은 앵무새로 화살표", "A fine-tick ruler and a coarse-tick ruler on top; below, an arrow from a big parrot with numbers 0.4823 and -0.1392 to a smaller parrot with 0.5 and -0.1"),
         "caption": ("양자화는 정밀한 숫자를 굵은 눈금으로 다시 적어, 앵무새를 가볍게 만드는 거예요.", "Quantization rewrites the fine numbers on a coarse scale, and the parrot gets light."),
         "small": ("0.4823을 0.5로 적는 식이에요. 조금 둔해지지만 훨씬 작고 빨라요. 새 앵무새가 아니라 같은 앵무새예요.", "Like writing 0.4823 as 0.5. It gets a little duller, but far smaller and faster. It is the same parrot, not a new one."),
         "tricks": (4, [
             (BITS_I, ("눈금이 굵을수록 가볍고 둔해요", "Coarser ticks: lighter, duller"), ("8비트는 살짝, 4비트는 더", "8-bit a little, 4-bit more"), "calm"),
             (EXAM_I, ("우리 일로 시험해요", "Test it on our job"), ("점수가 얼마나 떨어졌나", "how much did the score drop"), "warm"),
             (PHONE_I, ("폰·노트북에선 거의 필수", "Nearly a must on phones, laptops"), ("작은 횃대엔 가벼운 새만", "small perch, light bird only")),
             (ORDER_I, ("특훈 뒤에 해요", "Do it after the drill"), ("먼저 가르치고, 그다음 굵게", "teach first, then coarsen"), "calm"),
         ])},
        {"svg": P4, "alt": ("정밀 저울 위 큰 앵무새(무거움)에서 굵은 눈금 저울 위 작은 앵무새(가벼움)로 화살표. 점수표: 원래 100점 16GB, 8비트 99점 8GB, 4비트 96점 4GB, 2비트 70점 2GB", "An arrow from a big parrot on a fine scale (heavy) to a smaller parrot on a coarse scale (light). A score table: original 100 at 16 GB, 8-bit 99 at 8 GB, 4-bit 96 at 4 GB, 2-bit 70 at 2 GB"),
         "caption": ("눈금이 굵을수록 앵무새는 가벼워지고, 점수는 조금씩 떨어져요.", "The coarser the ticks, the lighter the parrot — and the score slips a little."),
         "small": ('8비트·4비트는 보통 괜찮고, 너무 굵으면 확 둔해져요. 어디까지 굵게 할지는 <a href="evaluation-ko.html">시험</a>으로 골라요. 특훈(<a href="finetune-ko.html">파인튜닝</a>)은 굵게 적기 전에 해요.',
                   '8-bit and 4-bit are usually fine; too coarse and it goes dull fast. Pick how coarse by <a href="evaluation-en.html">testing</a>. Do the drill (<a href="finetune-en.html">fine-tuning</a>) before you coarsen.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새가 '요약이에요: 회의는 3시', 괜찮은 일은 요약·번역·분류. 오른쪽 빨강: 땀 흘리는 빨간 앵무새가 '12 × 13 = 146… 인가?', 민감한 일은 수학·긴 추론·긴 코드", "Left, green: a parrot says summary, the meeting is at 3; fine jobs are summary, translation, sorting. Right, red: a sweating red parrot says 12 × 13 = 146 maybe; sensitive jobs are math, long reasoning, long code"),
         "caption": ("요약·번역은 굵게 적어도 괜찮지만, 수학·긴 추론은 확 둔해지기도 해요.", "Summaries and translation survive coarse ticks; math and long reasoning can go dull fast."),
         "small": ('굵은 눈금이 모자라면 다른 길이 있어요 — 작은 앵무새를 새로 가르치는 <a href="distillation-ko.html">증류</a>. 가벼워진 앵무새가 답하는 값과 시간은 <a href="inference-ko.html">추론</a> 이야기에서.',
                   'If coarse ticks fall short, there is another road — <a href="distillation-en.html">distillation</a>, teaching a new small parrot. What the lighter parrot costs per answer is the <a href="inference-en.html">inference</a> story.')},
    ],
    "summary": (("<b>양자화</b> = 앵무새 머릿속의 <b>정밀한 숫자를 굵은 눈금으로 다시 적어</b> 훨씬 <b>작고 빠르게</b> 만들기. 조금 둔해지니 <b>우리 일로 시험</b>해서 눈금 굵기를 골라요.",
                 "<b>Quantization</b> = <b>rewrite the fine numbers</b> in the parrot\'s head <b>on a coarse scale</b>, making it far <b>smaller and faster</b>. It gets a little duller, so <b>test on our job</b> to pick how coarse."),
                ("Quantization. 모델 가중치(파라미터)를 FP16·BF16 같은 고정밀 표현에서 INT8·INT4 등 낮은 비트 폭으로 바꿔 메모리와 추론 비용을 줄이는 기법이에요. 정밀도 손실이 있으므로 벤치마크로 확인하고, 파인튜닝 뒤에 적용해요. 온디바이스(폰·노트북) 배포에선 거의 필수예요.",
                 "Converting model weights from high-precision formats like FP16 or BF16 to lower bit widths such as INT8 or INT4 to cut memory and inference cost. There is a precision loss, so verify with benchmarks and apply it after fine-tuning. Nearly mandatory for on-device (phone, laptop) deployment.")),
    "glossary": [
        ("양자화", "Quantization", ("숫자를 굵은 눈금으로 다시 적기.", "Rewriting numbers on a coarse scale."), ("같은 앵무새가 가볍고 빨라져요. 조금 둔해져요.", "The same parrot gets light and fast. A little duller.")),
        ("비트 (FP16 · INT8 · INT4)", "Bits (FP16 · INT8 · INT4)", ("눈금 굵기.", "How coarse the ticks are."), ("16비트는 촘촘, 8비트는 굵게, 4비트는 더 굵게. 숫자가 작을수록 가볍고 둔해요.", "16-bit is fine, 8-bit coarse, 4-bit coarser. Smaller number: lighter and duller.")),
        ("정밀도 손실", "Precision loss", ("굵게 적어서 둔해진 만큼.", "How much duller it got."), ("0.4823을 0.5로 적으면 조금 틀려요. 수학·긴 추론에서 더 티가 나요.", "Writing 0.4823 as 0.5 is slightly off. It shows most in math and long reasoning.")),
        ("온디바이스", "On-device", ("우리 집 작은 횃대.", "Our small perch at home."), ("폰·노트북에서 앵무새를 직접 돌리는 것. 가벼운 앵무새만 올라가요.", "Running the parrot right on a phone or laptop. Only a light parrot fits.")),
        ("추론 속도", "Inference speed", ("답하는 데 걸리는 시간.", "Time taken to answer."), ('가벼운 앵무새가 더 빨리 답해요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'A lighter parrot answers faster. → <a href="inference-en.html">what an answer costs</a>')),
        ("메모리", "Memory", ("앵무새가 차지하는 자리.", "The room the parrot takes."), ("16 GB 앵무새가 8비트면 8 GB, 4비트면 4 GB가 돼요.", "A 16 GB parrot becomes 8 GB at 8-bit, 4 GB at 4-bit.")),
        ("증류와의 차이", "Versus distillation", ("같은 새를 가볍게 vs 새로 가르치기.", "Lighten the same bird vs teach a new one."), ('양자화는 숫자를 굵게, 증류는 작은 앵무새를 새로 키워요. → <a href="distillation-ko.html">작은 앵무새에게 흉내 가르치기</a>', 'Quantization coarsens the numbers; distillation raises a new small parrot. → <a href="distillation-en.html">teaching the small parrot to copy</a>')),
        ("평가", "Evaluation", ("굵게 적은 뒤 시험.", "The test after coarsening."), ('점수가 얼마나 떨어졌는지 우리 일로 확인해요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Check on our job how much the score dropped. → <a href="evaluation-en.html">the examiner\'s scorecard</a>')),
    ],
}
