from _draw import *
from _world import *


def coin(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="9" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/><text y="4" text-anchor="middle" font-size="10" font-weight="700" fill="#5A3B22">₩</text></g>'


# 1. 월말 청구서가 예상의 열 배 — 뭐가 비쌌는지 몰라요
P1 = svg(300, sky(300)
         + person(90, 110, s=1.0, face=FROWN, extra=SWEAT, **TRAINER) + label(125, 250, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + note(200, 40, 250, 150, "⟦월말 청구서|MONTH-END BILL⟧", ("⟦예상: 10만 원|expected: 100,000⟧", "⟦실제: 100만 원 !|actual: 1,000,000 !⟧", "⟦…뭐가 비쌌지?|…what cost so much?⟧"), 1.0, 1)
         + perch(600, 200, 130) + parrot(600, 160, 1.1) + label(600, 262, "⟦앵무새는 그냥 답했을 뿐|the parrot just answered⟧", 11, "var(--muted)")
         + label(380, 282, "⟦청구서가 예상의 열 배 — 어디서 콩이 새어 나갔는지 몰라요|the bill is ten times the guess — and nobody knows where the beans went⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새 값은 '한 번'이 아니라 콩 하나하나에 매겨져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(50, 40, 300, 200, "⟦청구서 항목|BILL LINES⟧", ("⟦앵무새 대여 1회 … 아니에요|parrot rental, 1 time … no⟧", "⟦들어간 콩 × 값|beans in × rate⟧", "⟦나온 콩 × 값|beans out × rate⟧", "⟦앵무새 크기별 단가|rate by parrot size⟧", "⟦콩마다 매겨져요|priced per bean⟧"), 1.0, 4)
         + '<path d="M64 86 l190 0" stroke="var(--bad)" stroke-width="3"/>'
         + parrot(560, 150, 1.2, talk=True) + label(560, 240, "⟦콩 하나 = 값 하나|one bean = one charge⟧", 11, "var(--ink)")
         + "".join(bean(430 + i * 40, 90, 0.8) + coin(430 + i * 40, 62, 0.8) for i in range(4))
         + label(490, 130, "⟦들어가는 콩도 값|beans going in cost too⟧", 10, "var(--muted)")
         + "".join(bean(620 + i * 40, 90, 0.8) + coin(620 + i * 40 - 6, 58, 0.8) + coin(620 + i * 40 + 8, 64, 0.8) for i in range(3))
         + label(660, 130, "⟦나오는 콩은 더 값|beans coming out cost more⟧", 10, "var(--muted)")
         + label(380, 282, "⟦앵무새 값은 한 번이 아니라 콩 하나하나에 매겨져요 — 세지 않으면 새어 나가요|the parrot is priced per bean, not per visit — uncounted beans leak away⟧", 12, "var(--bad)"))

# 3. 프라이싱 = 들어간 콩 × 값 + 나온 콩 × 값 (hero)
P3 = svg(360, sky(360)
         + label(380, 50, "⟦값 = 들어간 콩 × 값 + 나온 콩 × 값|cost = beans in × rate + beans out × rate⟧", 15, "var(--ink)", cls="d")
         + tray(40, 150, 220, 70, "⟦들어간 콩 × 1원|beans in × 1⟧") + beans(76, 138, ("⟦오늘|today⟧", "⟦날씨|weather⟧", "⟦어때|how⟧", "⟦?|?⟧"), 0.9, 50)
         + coin(150, 100, 1.0) + label(150, 84, "⟦콩당 1원|1 per bean⟧", 10, "var(--muted)")
         + perch(380, 240, 120) + parrot(380, 200, 1.2, talk=True) + label(380, 292, "⟦앵무새가 클수록 콩당 비싸요|the bigger the parrot, the pricier per bean⟧", 11, "var(--ink)")
         + beans(500, 150, ("⟦맑고|sunny⟧", "⟦따뜻|warm⟧", "⟦해요|today⟧"), 0.9, 50)
         + "".join(coin(500 + i * 50 - 10, 104, 0.9) + coin(500 + i * 50 + 6, 96, 0.9) + coin(500 + i * 50 + 18, 110, 0.9) for i in range(3))
         + label(560, 190, "⟦나온 콩 × 5원|beans out × 5⟧", 11, "var(--muted)")
         + label(600, 76, "⟦나온 콩은 3~5배 비싸요|beans out cost 3 to 5 times more⟧", 10, "var(--muted)")
         + label(380, 340, "⟦프라이싱 = 들어간 콩 × 값 + 나온 콩 × 값 — 앵무새가 클수록 콩당 비싸요|pricing: beans in × rate + beans out × rate — and a bigger parrot costs more per bean⟧", 13, "var(--ink)", cls="d"))

# 4. 청구서 표: 입력 콩·출력 콩·캐시된 콩·앵무새 크기별 단가, 한 달 합계
P4 = svg(320, sky(320)
         + note(40, 40, 400, 230, "⟦한 달 청구서 — 큰 앵무새|MONTHLY BILL — BIG PARROT⟧",
                ("⟦들어간 콩  100만 × 3원 = 300만|beans in   1,000,000 × 3 = 3,000,000⟧", "⟦나온 콩     20만 × 15원 = 300만|beans out    200,000 × 15 = 3,000,000⟧", "⟦미리 놓은 콩 50만 × 0.3원 = 15만|cached beans 500,000 × 0.3 = 150,000⟧", "⟦합계  615만 원|total  6,150,000⟧", "⟦(작은 앵무새였다면 약 62만 원)|(a small parrot: about 620,000)⟧"), 1.0, 3)
         + parrot(560, 120, 1.3, color=PARROT_BIG) + label(560, 200, "⟦큰 앵무새|big parrot⟧", 11, "var(--ink)", cls="d") + label(560, 218, "⟦콩당 3원 / 15원|3 / 15 per bean⟧", 10, "var(--muted)")
         + parrot(680, 140, 0.8) + label(680, 200, "⟦작은 앵무새|small parrot⟧", 11, "var(--ink)", cls="d") + label(680, 218, "⟦콩당 0.3원 / 1.5원|0.3 / 1.5 per bean⟧", 10, "var(--muted)")
         + label(620, 255, "⟦같은 콩이라도 앵무새 크기로 열 배 차이|same beans, ten times apart by parrot size⟧", 10, "var(--muted)")
         + label(380, 300, "⟦청구서는 콩 종류 × 앵무새 크기로 읽어요 — 어디가 큰지 보여요|read the bill as bean kind × parrot size — it shows where the money goes⟧", 11, "var(--ink)"))

# 5. 콩 값이 싸져도 콩 수는 늘어요 — 에이전트·추론 앵무새
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + '<path d="M60 70 L320 200" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M300 200 L322 202 L314 182" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + coin(60, 70, 1.3) + coin(320, 200, 0.7)
         + label(190, 240, "⟦콩 한 알 값은 해마다 싸져요|the price of one bean falls every year⟧", 11, "var(--ink)")
         + label(190, 262, "⟦좋은 소식|good news⟧", 12, "var(--good)", cls="d")
         + parrot(470, 150, 1.0, mood="think") + label(470, 240, "⟦중얼거리는 앵무새|the muttering parrot⟧", 10, "var(--muted)")
         + "".join(bean(530 + (i % 6) * 32, 90 + (i // 6) * 26, 0.7) for i in range(18))
         + label(610, 175, "⟦심부름·중얼거림 한 번에 콩 수천 개|one errand or think-aloud: thousands of beans⟧", 10, "var(--ink)")
         + label(610, 240, "⟦콩 수가 열 배, 백 배 늘어요|bean counts grow ten, a hundred times⟧", 11, "var(--ink)")
         + label(610, 262, "⟦그래서 청구서는 다시 커져요|so the bill grows again⟧", 12, "var(--bad)", cls="d")
         + label(380, 300, "⟦콩 값이 싸져도 콩 수가 늘어요 — 세는 습관이 답이에요|beans get cheaper, but you use more — counting is the answer⟧", 12, "var(--ink)", cls="d"))

TRAY_I = icon(f'<rect x="8" y="30" width="48" height="20" rx="6" fill="var(--stone)" opacity="0.7"/><ellipse cx="22" cy="38" rx="8" ry="6" fill="{BEAN}"/><ellipse cx="42" cy="38" rx="8" ry="6" fill="{BEAN}"/><path d="M20 14 h24" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><path d="M26 8 l-6 6 l6 6 M38 8 l6 6 l-6 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
LIMIT_I = icon(f'<ellipse cx="16" cy="36" rx="8" ry="6" fill="{BEAN}"/><ellipse cx="34" cy="36" rx="8" ry="6" fill="{BEAN}"/><path d="M46 20 v32" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><ellipse cx="56" cy="36" rx="6" ry="4" fill="{BEAN}" opacity="0.3"/><text x="30" y="20" text-anchor="middle" font-size="11" font-weight="700" fill="var(--bad)">max</text>')
CACHE_I = icon(f'<rect x="8" y="24" width="48" height="24" rx="6" fill="var(--stone)" opacity="0.7"/><ellipse cx="20" cy="30" rx="8" ry="6" fill="{BEAN}"/><ellipse cx="36" cy="30" rx="8" ry="6" fill="{BEAN}"/><circle cx="50" cy="14" r="8" fill="#E9B44C" stroke="#B07D1E" stroke-width="2"/><path d="M45 14 h10" stroke="#5A3B22" stroke-width="2"/>')
ROUTE_I = icon(f'<path d="M8 32 h14 M22 32 l14 -14 h10 M22 32 l14 14 h10" stroke="var(--muted)" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="54" cy="18" rx="7" ry="9" fill="{PARROT_BIG}"/><ellipse cx="54" cy="46" rx="5" ry="6" fill="{PARROT}"/><path d="M12 22 l4 4 l6 -8" stroke="var(--good)" stroke-width="2.5" fill="none"/>')

PAGE = {
    "slug": "pricing", "order": 30,
    "title": ("콩 값", "The Price of Beans"),
    "h1": ("<em>프라이싱</em>이 뭐예요?", "What is <em>Pricing</em>?"),
    "sub": ("LLM 프라이싱(토큰 과금)을, 앵무새 값이 한 번이 아니라 콩 하나하나에 매겨진다는 이야기로 풀어봤어요.",
            "LLM pricing (per-token billing), told as a story about a parrot that is priced per bean, not per visit."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 조련사 옆에 '월말 청구서: 예상 10만 원, 실제 100만 원, 뭐가 비쌌지?' 쪽지. 오른쪽 횃대의 앵무새는 그냥 답했을 뿐", "A sweating trainer beside a month-end bill note: expected 100,000, actual 1,000,000, what cost so much? A parrot on a perch just answered"),
         "caption": ("월말 청구서가 예상의 열 배예요. 그런데 뭐가 비쌌는지 몰라요.", "The month-end bill is ten times the guess. And nobody knows what cost so much."),
         "small": ("앵무새는 시킨 대로 답했을 뿐이에요. 콩이 어디서 새어 나갔는지 세어 본 사람이 없어요.", "The parrot only answered as told. Nobody counted where the beans leaked away.")},
        {"svg": P2, "alt": ("청구서 항목 쪽지: '앵무새 대여 1회'는 줄 그어 지우고, 들어간 콩 × 값, 나온 콩 × 값, 앵무새 크기별 단가. 오른쪽엔 콩마다 동전이 붙은 앵무새", "A bill-lines note with parrot rental crossed out, then beans in × rate, beans out × rate, rate by parrot size; on the right a parrot with a coin on every bean"),
         "caption": ("앵무새 값은 한 번이 아니라 콩 하나하나에 매겨져요.", "The parrot is priced per bean, not per visit."),
         "small": ('들어간 콩도, 나온 콩도, 다 값이에요. 콩이 뭔지는 <a href="token-ko.html">앵무새가 말을 콩으로 세요</a>에서.',
                   'Beans going in and beans coming out both cost. What a bean is: <a href="token-en.html">the parrot counts words in beans</a>.')},
        {"svg": P3, "hero": True, "alt": ("값 = 들어간 콩 × 값 + 나온 콩 × 값. 쟁반 위 들어간 콩엔 동전 하나씩(1원), 앵무새가 낸 나온 콩엔 동전 세 개씩(5원). 앵무새가 클수록 콩당 비싸요", "cost = beans in × rate + beans out × rate. Beans in on a tray carry one coin each (1); beans out from the parrot carry three coins each (5). A bigger parrot costs more per bean"),
         "caption": ("프라이싱은 들어간 콩 × 값 + 나온 콩 × 값이에요. 나온 콩이 보통 3~5배 비싸요.", "Pricing is beans in × rate plus beans out × rate. Beans out usually cost 3 to 5 times more."),
         "small": ("그리고 앵무새가 클수록 콩당 값이 올라가요. 그러니 콩 수를 줄이거나, 작은 앵무새를 쓰거나, 둘 다예요.", "And a bigger parrot costs more per bean. So use fewer beans, or a smaller parrot, or both."),
         "tricks": (4, [
             (TRAY_I, ("쟁반을 짧게", "Keep the tray short"), ("들어가는 콩을 줄여요", "fewer beans going in"), "calm"),
             (LIMIT_I, ("나오는 콩을 제한해요", "Cap the beans coming out"), ("최대 길이를 정해요", "set a maximum length"), "warm"),
             (CACHE_I, ("같은 앞부분은 캐시", "Cache the same start"), ("미리 놓아둔 콩은 열 배 싸요", "beans laid out ahead cost a tenth")),
             (ROUTE_I, ("쉬운 일은 작은 앵무새", "Easy jobs to the small parrot"), ("콩당 값이 열 배 차이", "ten times apart per bean"), "calm"),
         ])},
        {"svg": P4, "alt": ("한 달 청구서: 들어간 콩 100만 × 3원 = 300만, 나온 콩 20만 × 15원 = 300만, 미리 놓은 콩 50만 × 0.3원 = 15만, 합계 615만 원. 큰 앵무새는 콩당 3원/15원, 작은 앵무새는 0.3원/1.5원", "A monthly bill: beans in 1,000,000 × 3 = 3,000,000; beans out 200,000 × 15 = 3,000,000; cached beans 500,000 × 0.3 = 150,000; total 6,150,000. Big parrot 3 and 15 per bean, small parrot 0.3 and 1.5"),
         "caption": ("청구서는 콩 종류 × 앵무새 크기로 읽어요. 그러면 어디가 큰지 보여요.", "Read the bill as bean kind × parrot size, and it shows where the money goes."),
         "small": ('나온 콩 20만이 들어간 콩 100만과 값이 같아요. 쟁반(<a href="context-ko.html">컨텍스트</a>)을 줄이고, 같은 앞부분은 <a href="promptcaching-ko.html">미리 놓아둔 콩</a>으로, 쉬운 일은 <a href="routing-ko.html">작은 앵무새</a>에게.',
                   '200,000 beans out cost the same as 1,000,000 beans in. Shrink the tray (<a href="context-en.html">context</a>), reuse <a href="promptcaching-en.html">beans laid out ahead</a> for the same start, and <a href="routing-en.html">route</a> easy jobs to the small parrot.')},
        {"svg": P5, "alt": ("왼쪽 초록: 큰 동전에서 작은 동전으로 내려가는 화살표, 콩 한 알 값은 해마다 싸져요. 오른쪽 빨강: 중얼거리는 앵무새와 콩 열여덟 개, 심부름·중얼거림 한 번에 콩 수천 개", "Left, green: an arrow from a big coin down to a small one — the price of one bean falls every year. Right, red: a muttering parrot with eighteen beans — one errand or think-aloud uses thousands of beans"),
         "caption": ("콩 한 알 값은 싸져요. 그런데 콩 수는 열 배, 백 배 늘어요.", "One bean gets cheaper. But bean counts grow ten, a hundred times."),
         "small": ('<a href="agent-ko.html">심부름하는 앵무새</a>와 <a href="reasoning-ko.html">중얼거리는 앵무새</a>는 콩을 아주 많이 먹어요. 값과 시간이 어떻게 드는지는 <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>에서.',
                   'The <a href="agent-en.html">errand-running parrot</a> and the <a href="reasoning-en.html">muttering parrot</a> eat a great many beans. How cost and time add up: <a href="inference-en.html">what an answer costs</a>.')},
    ],
    "summary": (("<b>프라이싱</b> = <b>들어간 콩 × 값 + 나온 콩 × 값</b>. 나온 콩이 <b>3~5배 비싸고</b>, 앵무새가 <b>클수록 콩당 비싸요</b>. 쟁반을 짧게, 나오는 콩을 제한, 같은 앞부분은 캐시, 쉬운 일은 작은 앵무새.",
                 "<b>Pricing</b> = <b>beans in × rate + beans out × rate</b>. Beans out cost <b>3 to 5 times more</b>, and a <b>bigger parrot costs more per bean</b>. Keep the tray short, cap the output, cache the same start, send easy jobs to the small parrot."),
                ("LLM API 과금은 입력 토큰과 출력 토큰에 각각 단가를 매기고, 모델 등급에 따라 단가가 달라요(출력이 보통 3~5배). 프롬프트 캐시 히트는 큰 할인, 배치 API는 느리지만 싼 줄이에요. 컨텍스트 길이·출력 길이·모델 선택이 비용을 결정하고, 에이전트와 추론 모델은 토큰을 많이 써서 단가가 내려도 총액이 늘 수 있어요.",
                 "LLM APIs bill input tokens and output tokens at separate rates that vary by model tier (output is usually 3 to 5 times more). Prompt-cache hits earn a large discount, and batch APIs are the slow-but-cheap lane. Context length, output length, and model choice drive cost; agents and reasoning models use so many tokens that totals can rise even as rates fall.")),
    "glossary": [
        ("토큰 단가", "Token rate", ("콩 한 알 값.", "The price of one bean."), ("보통 콩 백만 개당 얼마로 적혀 있어요. 앵무새 크기마다 달라요.", "Usually listed per million beans. It differs by parrot size.")),
        ("입력 · 출력 토큰", "Input · output tokens", ("들어간 콩 · 나온 콩.", "Beans in · beans out."), ("나온 콩이 3~5배 비싸요. 긴 답을 시키면 그만큼 커요.", "Beans out cost 3 to 5 times more. Long answers add up fast.")),
        ("캐시 할인", "Cache discount", ("미리 놓아둔 콩은 싸요.", "Beans laid out ahead are cheap."), ('같은 앞부분을 다시 쓰면 열 배쯤 싸요. → <a href="promptcaching-ko.html">미리 놓아둔 콩</a>', 'Reusing the same start costs about a tenth. → <a href="promptcaching-en.html">beans laid out ahead</a>')),
        ("컨텍스트 길이 비용", "Context length cost", ("쟁반이 클수록 값.", "A bigger tray costs more."), ('쟁반의 콩은 매번 다 값이에요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'Every bean on the tray is charged every time. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("모델 등급", "Model tier", ("앵무새 크기.", "Parrot size."), ("큰 앵무새는 콩당 열 배 비싸기도 해요. 일에 맞게 골라요.", "A big parrot can cost ten times more per bean. Match it to the job.")),
        ("배치 API", "Batch API", ("느리지만 싼 줄.", "The slow but cheap lane."), ("급하지 않은 질문을 모아 두면 절반 값에 답해요.", "Gather questions that can wait, and they get answered at half price.")),
        ("예산 한도", "Budget cap", ("콩 자루 뚜껑.", "A lid on the bean sack."), ("한 달에 이만큼까지만 — 넘으면 멈추게 미리 정해요.", "Only this much a month — set it to stop before it runs over.")),
        ("라우팅", "Routing", ("어느 앵무새에게 시킬까.", "Which parrot gets the job."), ('쉬운 일은 작은 앵무새, 어려운 일만 큰 앵무새. → <a href="routing-ko.html">어느 앵무새에게 시킬까</a>', 'Easy jobs to the small parrot, hard ones only to the big. → <a href="routing-en.html">which parrot gets the job</a>')),
    ],
}
