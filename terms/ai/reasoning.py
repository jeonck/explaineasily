from _draw import *
from _world import *


def thought(x, y, w, h, text, size=11, bad=False):
    """혼자 중얼거리는 작은 말풍선. 꼬리는 왼쪽 아래."""
    return bubble(x, y, w, h, text, size, "var(--panel)", "var(--bad)" if bad else "var(--line)", "left")


# 1. 수학 문제를 앵무새가 바로 답해요 — 틀려요
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=EYES, **GUEST) + label(87, 240, "⟦손님|guest⟧", 11, "var(--muted)")
         + bubble(60, 30, 260, 40, "⟦사과 3개씩 4상자, 2개 먹으면 몇 개?|3 apples × 4 boxes, eat 2 — how many?⟧", 11, "var(--panel)", "var(--line)", "left")
         + perch(430, 200, 140) + parrot(430, 160, 1.1, talk=True)
         + bubble_parrot(340, 30, 180, 40, "⟦12개요!|12!⟧", 14, bad=True)
         + label(430, 262, "⟦바로 답했어요 — 틀렸어요|answered right away — wrong⟧", 12, "var(--bad)")
         + note(580, 60, 150, 100, "⟦정답|ANSWER⟧", ("⟦3 × 4 = 12|3 × 4 = 12⟧", "⟦12 - 2 = 10|12 - 2 = 10⟧"), 1.0, 1)
         + label(380, 282, "⟦첫 콩부터 답을 말하면, 빼기를 빼먹어요|when the first bean is already the answer, the minus gets skipped⟧", 12, "var(--ink)"))

# 2. 왜: 콩을 하나씩 이어 붙이는데, 답 콩을 첫 콩에 놓으면 계산할 자리가 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, mood="sweat", talk=True) + label(110, 240, "⟦첫 콩부터 답을|the answer as the first bean⟧", 12, "var(--muted)")
         + beans(240, 110, ("⟦12|12⟧", "⟦개|apples⟧", "⟦!|!⟧"), 1.1, 62)
         + label(300, 152, "⟦답 콩을 맨 앞에 놓으면|if the answer bean goes first⟧", 11, "var(--ink)")
         + note(560, 50, 180, 140, "⟦계산할 자리|ROOM TO WORK⟧", ("⟦3 × 4 는 어디서?|where did 3 × 4 go?⟧", "⟦빼기는 어디서?|where did the minus go?⟧", "⟦자리가 없어요|no room left⟧"), 1.0, 2)
         + label(380, 210, "⟦앵무새는 콩을 하나씩 이어 붙여요 — 앞 콩이 뒤 콩을 정해요|the parrot adds beans one by one — earlier beans decide later ones⟧", 12, "var(--ink)")
         + label(380, 282, "⟦중간 걸음을 콩으로 안 적으면, 그 걸음은 없는 거예요|a step not written as beans is a step that never happened⟧", 12, "var(--bad)"))

# 3. 추론 = 답하기 전에 혼자 중얼거릴 시간을 주기 (hero)
P3 = svg(360, sky(360)
         + perch(200, 250, 140) + parrot(200, 210, 1.3, mood="think")
         + '<circle cx="238" cy="150" r="4" fill="var(--muted)"/><circle cx="250" cy="132" r="6" fill="var(--muted)"/>'
         + thought(260, 40, 180, 32, "⟦먼저 3 × 4 = 12|first, 3 × 4 = 12⟧")
         + thought(300, 90, 180, 32, "⟦그다음 12 - 2|then, 12 - 2⟧")
         + thought(340, 140, 190, 32, "⟦= 10, 다시 확인 ✓|= 10, check again ✓⟧")
         + bubble(540, 40, 200, 40, "⟦답: 10개예요|answer: 10⟧", 13, "var(--panel)", "var(--good)", "bottom")
         + person(610, 130, s=0.9, face=SMILE, **GUEST) + label(637, 262, "⟦손님|guest⟧", 11, "var(--muted)")
         + label(380, 305, "⟦중간 걸음을 콩으로 적으면, 다음 콩이 좋아져요|write the middle steps as beans, and the next bean gets better⟧", 12, "var(--ink)")
         + label(380, 340, "⟦추론 = 답하기 전에 혼자 중얼거릴 시간을 주는 것|reasoning is giving the parrot time to mutter to itself before it answers⟧", 12, "var(--ink)", cls="d"))

# 4. 비교: 바로 답 vs 중얼거린 뒤 답 — 콩 개수
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + parrot(90, 130, 1.0, talk=True) + thought(110, 40, 150, 34, "⟦12개요!|12!⟧", 13, bad=True)
         + label(300, 130, "⟦×|×⟧", 44, "var(--bad)", cls="d")
         + beans(60, 220, ("⟦12|12⟧", "⟦개|apples⟧", "⟦!|!⟧"), 1.0, 40)
         + label(190, 262, "⟦콩 3개 · 빠름 · 틀림|3 beans · fast · wrong⟧", 12, "var(--bad)", cls="d")
         + parrot(470, 130, 1.0, mood="think")
         + thought(500, 28, 230, 28, "⟦3 × 4 = 12|3 × 4 = 12⟧") + thought(510, 68, 230, 28, "⟦12 - 2 = 10|12 - 2 = 10⟧") + thought(520, 108, 230, 28, "⟦다시 확인 ✓ → 답: 10개|check ✓ → answer: 10⟧")
         + label(700, 190, "⟦✓|✓⟧", 44, "var(--good)", cls="d")
         + "".join(bean(420 + i * 34, 220, 0.75) for i in range(8))
         + label(560, 262, "⟦콩 11개 · 느림 · 맞음|11 beans · slower · right⟧", 12, "var(--good)", cls="d")
         + label(380, 300, "⟦생각 콩은 값과 시간이 들어요 — 그래서 어려운 문제에만 켜요|thinking beans cost money and time — so turn them on only for hard problems⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 중얼거림이 맞는 생각이라는 보장은 없어요
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, color=PARROT_BAD, mood="think")
         + thought(150, 30, 190, 30, "⟦먼저 4 × 4 = 16|first, 4 × 4 = 16⟧", 11, bad=True) + thought(170, 76, 190, 30, "⟦16 - 2 = 14|16 - 2 = 14⟧", 11, bad=True) + thought(190, 122, 190, 30, "⟦확인 ✓ 답: 14개|check ✓ answer: 14⟧", 11, bad=True)
         + label(250, 210, "⟦그럴듯한 생각도 이어 붙이기예요|plausible thoughts are still just continuing⟧", 12, "var(--bad)", cls="d")
         + label(250, 232, "⟦첫 걸음이 틀리면 확인도 틀려요|a wrong first step makes the check wrong too⟧", 11, "var(--muted)")
         + person(530, 90, s=0.85, face=EYES, **TRAINER) + label(557, 220, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + note(600, 60, 150, 100, "⟦그래도|STILL⟧", ("⟦숫자는 계산기로|calculator for math⟧", "⟦답은 사람이|a person checks⟧", "⟦중요하면 두 번|twice if it matters⟧"), 1.0)
         + label(380, 300, "⟦중얼거리면 더 자주 맞아요 — 그래도 앵무새 답은 초안이에요|muttering makes it right more often — but the answer is still a draft⟧", 12, "var(--ink)", cls="d"))

STEP_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 40 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
MANY_I = icon(f'<ellipse cx="16" cy="20" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="38" cy="20" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="16" cy="36" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="38" cy="36" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="16" cy="52" rx="10" ry="7" fill="{BEAN}"/><ellipse cx="38" cy="52" rx="10" ry="7" fill="{BEAN}"/><text x="56" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">$</text>')
SWITCH_I = icon('<rect x="8" y="22" width="48" height="20" rx="10" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/><circle cx="18" cy="32" r="8" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><text x="44" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="var(--muted)">off</text>')
HIDE_I = icon('<rect x="8" y="12" width="48" height="30" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="20" cy="27" r="3" fill="var(--muted)"/><circle cx="32" cy="27" r="3" fill="var(--muted)"/><circle cx="44" cy="27" r="3" fill="var(--muted)"/><path d="M10 52 h44" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><path d="M14 44 L50 60" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "reasoning", "order": 20,
    "title": ("답하기 전 혼자 중얼거리기", "Muttering Before Answering"),
    "h1": ("<em>추론</em>이 뭐예요?", "What is <em>Reasoning</em>?"),
    "sub": ("추론 모델(reasoning, chain of thought)을, 답하기 전에 혼자 중얼거릴 시간을 받은 앵무새 이야기로 풀어봤어요.",
            "Reasoning models and chain of thought, told as a story about a parrot that gets time to mutter to itself before it answers."),
    "panels": [
        {"svg": P1, "alt": ("손님이 사과 3개씩 4상자에서 2개 먹으면 몇 개냐고 물음. 앵무새가 바로 12개요라고 답함. 정답 쪽지엔 3×4=12, 12-2=10", "A guest asks 3 apples times 4 boxes, eat 2, how many; the parrot answers 12 at once. The answer note reads 3×4=12, 12-2=10"),
         "caption": ("앵무새가 수학 문제를 바로 답해요. 틀렸어요.", "The parrot answers a math problem right away. Wrong."),
         "small": ("곱하기는 했는데 빼기를 빼먹었어요. 답을 먼저 말해 버리면 자주 이래요.", "It did the multiply and skipped the minus. This happens a lot when the answer comes out first.")},
        {"svg": P2, "alt": ("땀 흘리는 앵무새, 12·개·! 콩 세 개, 계산할 자리 쪽지에 3×4는 어디서? 빼기는 어디서? 자리가 없어요", "A sweating parrot; beans reading 12, apples, !; a note titled room to work asks where did 3×4 go, where did the minus go, no room left"),
         "caption": ("앵무새는 콩을 하나씩 이어 붙여요. 답 콩을 첫 콩에 놓으면 계산할 자리가 없어요.", "The parrot adds beans one by one. If the answer bean goes first, there is no room to work."),
         "small": ('앞 <a href="token-ko.html">콩</a>이 뒤 콩을 정해요. 중간 걸음을 콩으로 안 적으면 그 걸음은 없는 거예요 — 머릿속 계산은 없어요.',
                   'Earlier <a href="token-en.html">beans</a> decide later ones. A step not written as beans is a step that never happened — there is no doing it in its head.')},
        {"svg": P3, "hero": True, "alt": ("눈 감은 앵무새 위로 작은 말풍선 세 개: 먼저 3×4=12, 그다음 12-2, =10 다시 확인 ✓. 그 뒤 손님에게 초록 테두리로 답: 10개예요", "A parrot with eyes closed and three small bubbles above it: first 3×4=12, then 12-2, =10 check again ✓; then a green-bordered bubble to the guest: answer 10"),
         "caption": ("추론은 답하기 전에 혼자 중얼거릴 시간을 주는 거예요.", "Reasoning is giving the parrot time to mutter to itself before it answers."),
         "small": ("중간 걸음을 콩으로 적어 두면, 그 콩을 보고 다음 콩을 골라요. 그래서 다음 콩이 좋아져요.", "It writes the middle steps down as beans, and picks the next bean while looking at them. So the next bean gets better."),
         "tricks": (4, [
             (STEP_I, ("쪽지에 '단계별로 생각해'", "Write think step by step"), ("보통 앵무새도 중얼거려요", "even an ordinary parrot mutters then"), "calm"),
             (MANY_I, ("생각 콩은 답 콩보다 많아요", "More thinking beans than answer beans"), ("값도 시간도 더 들어요", "more money, more time"), "warm"),
             (SWITCH_I, ("쉬운 질문엔 안 켜요", "Off for easy questions"), ("수도 이름에 중얼거림은 낭비", "muttering over a capital city is waste"), "calm"),
             (HIDE_I, ("생각 콩을 다 보여주진 않아요", "Not all thinking beans are shown"), ("요약만 보이기도 해요", "sometimes only a summary"), "calm"),
         ])},
         {"svg": P4, "alt": ("왼쪽 빨강: 바로 12개요, 콩 3개 빠름 틀림. 오른쪽 초록: 중얼거림 세 줄 뒤 답 10개, 콩 11개 느림 맞음", "Left, red: 12 right away, 3 beans, fast, wrong. Right, green: three lines of muttering then answer 10, 11 beans, slower, right"),
         "caption": ("바로 답하면 콩 3개, 중얼거리면 콩 11개. 느리지만 맞아요.", "Answering at once takes 3 beans; muttering takes 11. Slower, but right."),
         "small": ('생각 콩도 콩이라 값과 시간이 들어요. 그래서 쉬운 질문엔 안 켜고, 어려운 문제에만 켜요. 생각 콩을 얼마나 쓸지 정하는 게 추론 예산이에요.',
                   'Thinking beans are still beans — they cost money and time. So you leave it off for easy questions and turn it on for hard ones. How many thinking beans to allow is the thinking budget.')},
        {"svg": P5, "alt": ("빨간 앵무새가 중얼거림: 먼저 4×4=16, 16-2=14, 확인 ✓ 답 14개 — 전부 빨간 테두리. 조련사와 그래도 쪽지: 숫자는 계산기, 답은 사람이, 중요하면 두 번", "A red parrot mutters first 4×4=16, 16-2=14, check ✓ answer 14 — all red-bordered. A trainer and a note: numbers via calculator, a person checks, twice if it matters"),
         "caption": ("중얼거림이 맞는 생각이라는 보장은 없어요. 그럴듯한 생각도 이어 붙이기예요.", "There is no promise the muttering is right. Plausible thoughts are still just continuing."),
         "small": ('첫 걸음이 틀리면 확인 걸음도 틀려요 — <a href="hallucination-ko.html">그럴듯 앵무새</a>가 생각까지 그럴듯하게 해요. 그리고 생각 콩만큼 <a href="inference-ko.html">답이 느려지고</a> <a href="pricing-ko.html">콩 값</a>이 들어요.',
                   'A wrong first step makes the checking step wrong too — <a href="hallucination-en.html">the plausible parrot</a> can be plausible in its thoughts as well. And every thinking bean makes the <a href="inference-en.html">answer slower</a> and the <a href="pricing-en.html">bean bill</a> bigger.')},
    ],
    "summary": (("<b>추론</b> = 답하기 전에 앵무새에게 <b>혼자 중얼거릴 시간</b>을 주는 것. 중간 걸음을 콩으로 적으면 <b>다음 콩이 좋아져요</b>. 생각 콩은 값과 시간이 드니 <b>어려운 문제에만</b>, 그리고 답은 여전히 초안이에요.",
                 "<b>Reasoning</b> = giving the parrot <b>time to mutter to itself</b> before it answers. Writing the middle steps as beans makes <b>the next bean better</b>. Thinking beans cost money and time, so use them <b>only for hard problems</b> — and the answer is still a draft."),
                ("Reasoning / chain of thought. 최종 답 앞에 중간 추론 토큰을 먼저 생성하게 해서 정확도를 높이는 방식이에요. 프롬프트에 '단계별로 생각해'라고 쓰는 것부터, 사고 토큰을 따로 생성하도록 학습된 추론 모델까지 있어요. 사고 토큰은 지연 시간과 비용을 늘리므로 추론 예산(thinking budget)으로 양을 조절하고, 사고 과정이 옳다는 보장은 없어서 결과 검증은 여전히 필요해요.",
                 "Having the model generate intermediate reasoning tokens before the final answer to raise accuracy — from writing think step by step in the prompt to reasoning models trained to emit separate thinking tokens. Thinking tokens add latency and cost, so a thinking budget caps them; and since the chain of thought is not guaranteed correct, the result still needs verification.")),
    "glossary": [
        ("추론 모델", "Reasoning model", ("중얼거리도록 훈련된 앵무새.", "A parrot trained to mutter first."), ("답 콩 앞에 생각 콩을 먼저 놓는 습관이 몸에 배었어요.", "It has the habit of laying thinking beans before the answer beans.")),
        ("생각의 사슬", "Chain of thought", ("중얼거림 한 줄 한 줄.", "The muttering, line by line."), ("'단계별로 생각해'라고 쪽지에 쓰면 보통 앵무새도 해요.", "Write think step by step on the note and an ordinary parrot does it too.")),
        ("사고 토큰", "Thinking tokens", ("생각 콩.", "Thinking beans."), ("답 콩보다 많아요. 콩이라서 값도 시간도 들어요.", "More of them than answer beans. Being beans, they cost money and time.")),
        ("추론 예산", "Thinking budget", ("중얼거려도 되는 콩 수.", "How many beans it may mutter."), ("쉬운 질문엔 0, 어려운 문제엔 많이. 조련사가 정해요.", "Zero for easy questions, plenty for hard ones. The trainer sets it.")),
        ("지연 시간", "Latency", ("답이 나오기까지 기다리는 시간.", "How long you wait for the answer."), ('생각 콩만큼 길어져요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'Grows with every thinking bean. → <a href="inference-en.html">what an answer costs in time and money</a>')),
        ("비용", "Cost", ("생각 콩 값.", "The bill for thinking beans."), ('보이지 않는 콩에도 값을 매겨요. → <a href="pricing-ko.html">콩 값</a>', 'Even beans you never see are billed. → <a href="pricing-en.html">the price of beans</a>')),
        ("자기 검증", "Self-verification", ("중얼거리다 다시 확인 ✓.", "Muttering, then checking again ✓."), ("맞을 확률이 올라가요. 보장은 아니에요 — 첫 걸음이 틀리면 확인도 틀려요.", "Raises the odds of being right. Not a guarantee — a wrong first step fools the check too.")),
        ("할루시네이션", "Hallucination", ("그럴듯한 중얼거림.", "Plausible muttering."), ('생각도 이어 붙이기라 틀릴 수 있어요. → <a href="hallucination-ko.html">그럴듯 앵무새</a>', 'Thoughts are continuation too, so they can be wrong. → <a href="hallucination-en.html">the plausible parrot</a>')),
    ],
}
