from _draw import *
from _world import *


def coin(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="9" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/><text y="4" text-anchor="middle" font-size="10" font-weight="700" fill="#5A3B22">₩</text></g>'


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M0 0 v-14 M0 0 l9 6" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><circle r="2.5" fill="var(--accent)"/></g>')


def scale_(x, y, w, readout):
    return (f'<rect x="{x - w / 2}" y="{y}" width="{w}" height="16" rx="4" fill="var(--stone-dark)"/>'
            f'<rect x="{x - 6}" y="{y - 16}" width="12" height="16" fill="var(--stone-dark)"/>'
            f'<rect x="{x - w / 2 - 6}" y="{y - 22}" width="{w + 12}" height="8" rx="3" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<rect x="{x - w / 2 + 6}" y="{y + 2}" width="{w - 12}" height="12" rx="3" fill="#142033"/>'
            + label(x, y + 12, readout, 10, "#7CE0A6", cls="d"))


ARROW = '<path d="M{0} {2} L{1} {2}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M{3} {4} L{1} {2} L{3} {5}" stroke="var(--muted)" stroke-width="3" fill="none"/>'


def arrow(x0, x1, y):
    return ARROW.format(x0, x1, y, x1 - 10, y - 8, y + 8)


# 1. 학교는 한 번인데, 손님이 물을 때마다 콩 값이 든다는 걸 손님이 몰라요
SCHOOL = ('<rect x="40" y="120" width="170" height="100" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
          '<path d="M30 120 L125 70 L220 120 Z" fill="var(--good)"/><rect x="110" y="170" width="30" height="50" fill="var(--stone-dark)"/>')
P1 = svg(300, sky(300) + SCHOOL + books(80, 210, 4, 0.7) + parrot(170, 165, 0.8, color=PARROT_BIG)
         + label(125, 250, "⟦앵무새 학교 — 한 번, 크게|parrot school — once, big⟧", 11, "var(--ink)", cls="d")
         + perch(400, 210, 130) + parrot(400, 170, 1.1, talk=True)
         + "".join(bean(450 + i * 24, 100 - (i % 2) * 8, 0.7) for i in range(4)) + coin(560, 96, 0.9)
         + label(400, 262, "⟦우리 집 — 물을 때마다 콩 값|our house — beans every question⟧", 11, "var(--ink)", cls="d")
         + person(600, 120, s=0.9, face=EYES, **GUEST) + bubble(470, 24, 260, 40, "⟦학교는 끝났으니 이제 공짜죠?|school is over, so now it is free, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 288, "⟦학교는 한 번이지만, 답은 매번 콩이 들어요 — 손님은 몰라요|school happens once, but every answer costs beans — the guest does not know⟧", 12, "var(--ink)"))

# 2. 두 저울: 학습은 책 읽기(한 번, 큼), 추론은 매번 답하기(작지만 수백만 번)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + books(190, 160, 6, 1.1) + scale_(190, 182, 200, "⟦아주 큼 × 1번|huge × once⟧")
         + label(190, 50, "⟦학습 = 책 읽기|training = reading⟧", 13, "var(--ink)", cls="d")
         + label(190, 230, "⟦학교에서 한 번, 크게|once at school, big⟧", 11, "var(--muted)")
         + beans(500, 150, ("⟦오늘|Today⟧", "⟦날씨|is⟧", "⟦맑음|sunny⟧"), 1.0, 44) + scale_(540, 182, 200, "⟦작음 × 1,000,000번|small × 1,000,000⟧")
         + label(540, 50, "⟦추론 = 매번 답하기|inference = answering⟧", 13, "var(--ink)", cls="d")
         + label(540, 230, "⟦우리 집에서 매번, 작게 — 그런데 수백만 번|at home every time, small — but millions of times⟧", 11, "var(--muted)")
         + label(380, 282, "⟦한 번은 작아도 백만 번이면 커요 — 답하는 값이 학교 값을 넘기도 해요|small once, big a million times — answering can cost more than school did⟧", 12, "var(--bad)"))

# 3. 추론 = 학교를 마친 앵무새가 손님 질문에 콩을 하나씩 만들어 답하는 것 (hero)
P3 = svg(360, sky(360)
         + clock(90, 110) + coin(90, 170, 1.2) + label(90, 205, "⟦시간 · 값|time · cost⟧", 11, "var(--muted)")
         + perch(230, 240, 150) + parrot(230, 200, 1.3, talk=True) + label(230, 292, "⟦학교를 마친 앵무새|a parrot done with school⟧", 11, "var(--muted)")
         + "".join(bean(300 + i * 34, 140 - (i % 2) * 8, 0.85) for i in range(5)) + label(370, 106, "⟦콩 하나씩 — 콩마다 시간과 값|one bean at a time — each costs time and money⟧", 11, "var(--ink)")
         + person(480, 130, s=0.8, face=SMILE, **GUEST) + bubble(400, 30, 220, 40, "⟦오늘 날씨 어때?|how is the weather today?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + note(580, 150, 170, 110, "⟦값이 커지는 것|WHAT RAISES COST⟧", ("⟦콩 수 ↑|more beans⟧", "⟦앵무새 크기 ↑|bigger parrot⟧", "⟦중얼거림 ↑|more muttering⟧"), 0.95)
         + label(380, 340, "⟦추론 = 학교를 마친 앵무새가 손님 질문에 콩을 하나씩 만들어 답하는 것|inference: a parrot done with school answers a guest, making one bean at a time⟧", 13, "var(--ink)", cls="d"))

# 4. 시간선: 첫 콩까지 / 콩당 시간 / 총 시간 + 값 계산 예
TL = ('<path d="M60 120 H700" stroke="var(--stone-dark)" stroke-width="3"/>'
      '<circle cx="60" cy="120" r="6" fill="var(--accent)"/><circle cx="260" cy="120" r="6" fill="var(--good)"/><circle cx="620" cy="120" r="6" fill="var(--good)"/>'
      '<path d="M60 80 H260" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M270 80 H620" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
      '<path d="M60 160 H620" stroke="var(--ink)" stroke-width="3"/><path d="M60 152 v16 M620 152 v16" stroke="var(--ink)" stroke-width="3"/>')
P4 = svg(320, sky(320) + TL
         + label(60, 145, "⟦질문|question⟧", 11, "var(--muted)") + label(260, 145, "⟦첫 콩|first bean⟧", 11, "var(--muted)") + label(620, 145, "⟦끝|end⟧", 11, "var(--muted)")
         + "".join(bean(290 + i * 40, 120, 0.7) for i in range(9))
         + label(160, 66, "⟦첫 콩까지 시간|time to first bean⟧", 11, "var(--accent)", cls="d")
         + label(445, 66, "⟦콩당 시간 × 콩 수|time per bean × beans⟧", 11, "var(--good)", cls="d")
         + label(340, 182, "⟦총 시간|total time⟧", 11, "var(--ink)", cls="d")
         + note(200, 195, 360, 78, "⟦값 계산 예|COST EXAMPLE⟧", ("⟦들어간 콩 1,000 × 1원 = 1,000원|1,000 beans in × 1 = 1,000⟧", "⟦나온 콩 300 × 5원 = 1,500원 → 합 2,500원|300 beans out × 5 = 1,500 → total 2,500⟧"), 0.95)
         + label(380, 300, "⟦첫 콩은 기다림, 그다음은 콩당 시간 — 값은 콩 수로 세요|the first bean is the wait, then it is time per bean — cost counts beans⟧", 11, "var(--muted)"))

# 5. 빠른 게 늘 싼 게 아니에요 — 작은 앵무새가 여러 번 틀리면 더 비쌈
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.3, color=PARROT_BIG, talk=True) + bubble_parrot(40, 40, 200, 40, "⟦정답이에요 (한 번에)|correct (first try)⟧", 11)
         + "".join(coin(230 + i * 24, 130) for i in range(5)) + label(280, 162, "⟦콩 값 5|5 in beans⟧", 11, "var(--ink)")
         + label(190, 230, "⟦큰 앵무새: 느리고 콩당 비싸지만 한 번에|big parrot: slow, pricier per bean, but once⟧", 11, "var(--ink)")
         + label(190, 262, "⟦합계 5|total 5⟧", 13, "var(--good)", cls="d")
         + parrot(470, 160, 0.8, color=PARROT_BAD, talk=True) + bubble_parrot(410, 40, 190, 40, "⟦틀렸어요… 다시… 또 다시|wrong… again… and again⟧", 11, bad=True)
         + "".join(coin(560 + (i % 3) * 24, 110 + (i // 3) * 26, 0.9) for i in range(6)) + label(590, 190, "⟦콩 값 2 × 3번|2 in beans × 3 tries⟧", 11, "var(--ink)")
         + label(570, 230, "⟦작은 앵무새: 빠르고 싸지만 세 번 만에|small parrot: fast and cheap, but three tries⟧", 11, "var(--ink)")
         + label(570, 262, "⟦합계 6 — 더 비쌌어요|total 6 — it cost more⟧", 13, "var(--bad)", cls="d")
         + label(380, 300, "⟦빠른 게 늘 싼 게 아니에요 — 일에 맞는 앵무새를 골라요|fast is not always cheap — pick the parrot that fits the job⟧", 12, "var(--ink)", cls="d"))

INOUT_I = icon(f'<ellipse cx="18" cy="32" rx="10" ry="7" fill="{BEAN}"/><path d="M32 32 h6" stroke="var(--muted)" stroke-width="3"/><path d="M36 26 l6 6 l-6 6" stroke="var(--muted)" stroke-width="3" fill="none"/><ellipse cx="50" cy="32" rx="12" ry="9" fill="{BEAN}"/><circle cx="52" cy="14" r="7" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/>')
BIG_I = icon(f'<ellipse cx="24" cy="38" rx="14" ry="18" fill="{PARROT_BIG}"/><circle cx="24" cy="16" r="11" fill="{PARROT_BIG}"/><path d="M33 13 l10 3 l-10 4z" fill="#E9B44C"/><circle cx="27" cy="14" r="2" fill="#FFF"/><circle cx="50" cy="20" r="7" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/><circle cx="52" cy="38" r="7" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 32 v-14 M32 32 l9 6" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="32" r="2.5" fill="var(--accent)"/>')
CACHE_I = icon(f'<rect x="8" y="24" width="48" height="24" rx="6" fill="var(--stone)" opacity="0.7"/><ellipse cx="20" cy="30" rx="8" ry="6" fill="{BEAN}"/><ellipse cx="36" cy="30" rx="8" ry="6" fill="{BEAN}"/><path d="M44 12 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "inference", "order": 29,
    "title": ("앵무새가 답하는 값과 시간", "What an Answer Costs"),
    "h1": ("<em>추론</em>이 뭐예요?", "What is <em>Inference</em>?"),
    "sub": ("추론(inference)을, 학교를 마친 앵무새가 손님 질문에 콩을 하나씩 만들어 답할 때 드는 값과 시간 이야기로 풀어봤어요.",
            "Inference, told as a story about what it costs, in beans and time, when a parrot done with school answers a guest one bean at a time."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽 앵무새 학교(한 번, 크게)와 오른쪽 우리 집 횃대의 앵무새가 콩과 동전을 내며 답함. 손님은 '학교는 끝났으니 이제 공짜죠?'", "A parrot school on the left (once, big) and, on the right, a parrot on our perch answering with beans and a coin; a guest asks if it is free now that school is over"),
         "caption": ("앵무새 학교는 한 번이에요. 그런데 손님이 물을 때마다 콩 값이 들어요.", "Parrot school happens once. But every time a guest asks, beans are spent."),
         "small": ("손님은 학교가 끝났으니 공짜라고 생각해요. 아니에요 — 답 한 번 한 번이 다 값이에요.", "The guest thinks it is free once school is over. It is not — every single answer has a price.")},
        {"svg": P2, "alt": ("두 저울: 왼쪽 저울엔 책 더미와 '아주 큼 × 1번', 오른쪽 저울엔 콩 세 개와 '작음 × 1,000,000번'", "Two scales: books on the left reading huge × once; three beans on the right reading small × 1,000,000"),
         "caption": ("학습은 책 읽기 — 한 번, 크게. 추론은 매번 답하기 — 작지만 수백만 번.", "Training is reading — once, big. Inference is answering — small, but millions of times."),
         "small": ("한 번은 작아도 백만 번이면 커요. 앵무새를 많이 쓰는 집은 답하는 값이 학교 값을 넘기도 해요.", "Small once, big a million times. A busy house can end up paying more for answers than the school cost.")},
        {"svg": P3, "hero": True, "alt": ("시계와 동전 옆, 횃대의 앵무새가 손님의 '오늘 날씨 어때?'에 콩을 하나씩 내며 답함. 쪽지엔 값이 커지는 것: 콩 수, 앵무새 크기, 중얼거림", "Beside a clock and a coin, a parrot on a perch answers a guest asking about the weather, one bean at a time; a note lists what raises cost: more beans, a bigger parrot, more muttering"),
         "caption": ("추론은 학교를 마친 앵무새가 손님 질문에 콩을 하나씩 만들어 답하는 거예요.", "Inference is a parrot done with school answering a guest, making one bean at a time."),
         "small": ('값과 시간은 콩 수, 앵무새 크기, 그리고 답하기 전 <a href="reasoning-ko.html">중얼거림</a>에 비례해요.',
                   'Cost and time grow with the number of beans, the size of the parrot, and how much it <a href="reasoning-en.html">mutters</a> before answering.'),
         "tricks": (4, [
             (INOUT_I, ("나가는 콩이 더 비싸요", "Beans out cost more"), ("들어가는 콩보다 3~5배", "3 to 5 times beans in"), "warm"),
             (BIG_I, ("큰 앵무새는 콩당 더 비싸요", "Big parrot: pricier per bean"), ("그리고 더 느려요", "and slower too"), "warm"),
             (CLOCK_I, ("첫 콩과 끝 콩은 달라요", "First bean and last bean differ"), ("기다림 vs 콩당 시간", "the wait vs time per bean"), "calm"),
             (CACHE_I, ("같은 앞부분은 미리", "Same start, prepared ahead"), ("미리 놓아둔 콩은 싸요", "beans laid out ahead are cheap"), "calm"),
         ])},
        {"svg": P4, "alt": ("시간선: 질문 → 첫 콩까지 시간 → 콩당 시간 × 콩 수 → 끝, 아래에 총 시간. 값 계산 예: 들어간 콩 1,000 × 1원 + 나온 콩 300 × 5원 = 2,500원", "A timeline: question, time to first bean, time per bean × beans, end, with total time below. A cost example: 1,000 beans in × 1 plus 300 beans out × 5 = 2,500"),
         "caption": ("시간은 첫 콩까지와 콩당 시간으로 나뉘고, 값은 콩 수로 세요.", "Time splits into the wait for the first bean and time per bean; cost counts beans."),
         "small": ('첫 콩이 나오면 바로 보여주는 게 <a href="streaming-ko.html">스트리밍</a>이에요. 같은 앞부분은 <a href="promptcaching-ko.html">미리 놓아둔 콩</a>으로 싸게 해요.',
                   'Showing the first bean as soon as it comes is <a href="streaming-en.html">streaming</a>. A repeated start gets cheaper with <a href="promptcaching-en.html">beans laid out ahead</a>.')},
        {"svg": P5, "alt": ("왼쪽 초록: 큰 앵무새가 한 번에 정답, 동전 5개, 합계 5. 오른쪽 빨강: 작은 빨간 앵무새가 세 번 틀림, 동전 2 × 3 = 6, 더 비쌌음", "Left, green: a big parrot answers correctly once, five coins, total 5. Right, red: a small red parrot gets it wrong three times, coins 2 × 3 = 6, which cost more"),
         "caption": ("빠른 게 늘 싼 게 아니에요. 작은 앵무새가 여러 번 틀리면 더 비싸요.", "Fast is not always cheap. A small parrot that fails several times costs more."),
         "small": ('콩 값은 <a href="pricing-ko.html">콩 값</a> 이야기에서, 어느 앵무새에게 시킬지는 <a href="routing-ko.html">라우팅</a>, 앵무새를 가볍게 하는 건 <a href="quantization-ko.html">양자화</a>예요.',
                   'The price of beans is the <a href="pricing-en.html">pricing</a> story; which parrot gets the job is <a href="routing-en.html">routing</a>; making a parrot lighter is <a href="quantization-en.html">quantization</a>.')},
    ],
    "summary": (("<b>추론</b> = 학교를 마친 앵무새가 <b>손님 질문에 콩을 하나씩 만들어 답하는 것</b>. 학교는 한 번이지만 답은 <b>매번 값</b>이 들고, 값과 시간은 <b>콩 수 · 앵무새 크기 · 중얼거림</b>에 비례해요.",
                 "<b>Inference</b> = a parrot done with school <b>answering a guest one bean at a time</b>. School happens once, but <b>every answer costs</b>, and cost and time grow with <b>beans, parrot size, and muttering</b>."),
                ("Inference. 학습이 끝난 모델을 실제 입력에 실행해 출력을 만드는 단계예요. 지연 시간은 첫 토큰 시간(TTFT)과 토큰당 시간으로 나뉘고, 비용은 입력·출력 토큰 수와 모델 크기에 비례해요. GPU 같은 가속기에서 여러 요청을 배칭해 처리량을 올려요. 총 비용은 학습보다 추론이 더 클 때가 많아요.",
                 "Running a trained model on real inputs to produce outputs. Latency splits into time to first token (TTFT) and time per token; cost scales with input and output token counts and model size. Accelerators such as GPUs batch many requests to raise throughput. Over time, inference often costs more than training did.")),
    "glossary": [
        ("추론", "Inference", ("앵무새가 답하는 것.", "The parrot answering."), ("학교가 끝난 뒤, 손님 질문에 콩을 하나씩 만들어요.", "After school, it makes beans one at a time for a guest.")),
        ("학습 vs 추론", "Training vs inference", ("책 읽기 vs 답하기.", "Reading vs answering."), ("읽기는 한 번에 크게, 답하기는 매번 작게 — 그런데 수백만 번.", "Reading is once and big; answering is small each time — but millions of times.")),
        ("지연 시간", "Latency", ("한 답에 걸리는 시간.", "Time for one answer."), ("첫 콩까지 기다림 + 콩당 시간 × 콩 수.", "The wait for the first bean plus time per bean × beans.")),
        ("처리량", "Throughput", ("한 시간에 답하는 횟수.", "Answers per hour."), ("앵무새 여러 마리, 혹은 한 마리가 여러 손님을 동시에.", "Several parrots, or one parrot serving several guests at once.")),
        ("첫 토큰 시간", "Time to first token", ("첫 콩까지 기다림.", "The wait for the first bean."), ('첫 콩이 나오면 바로 보여줘요. → <a href="streaming-ko.html">콩을 하나씩 바로 보여주기</a>', 'Show the first bean as soon as it comes. → <a href="streaming-en.html">showing beans one by one</a>')),
        ("GPU · 가속기", "GPU · accelerator", ("앵무새가 앉는 빠른 횃대.", "The fast perch the parrot sits on."), ("콩을 빨리 만들게 해 줘요. 비싸고 자리가 한정돼요.", "Makes beans fast. Pricey, and seats are limited.")),
        ("배칭", "Batching", ("손님 여럿을 한 번에.", "Several guests at once."), ("질문을 모아 함께 답하면 콩당 값이 내려가요. 대신 조금 기다려요.", "Answering gathered questions together lowers the price per bean, at the cost of a small wait.")),
        ("비용", "Cost", ("콩 값.", "The price of beans."), ('들어간 콩 + 나온 콩 × 단가. → <a href="pricing-ko.html">콩 값</a>', 'Beans in plus beans out, times the rate. → <a href="pricing-en.html">the price of beans</a>')),
    ],
}
