from _draw import *
from _world import *


def stove(x, y, s=1.0, smoking=False):
    """주방 화구(스토브). smoking=True 면 연기가 치솟아요 — 과열/과부하."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="0" width="64" height="30" rx="4" fill="#5A3B22"/>'
    out += '<circle cx="-13" cy="0" r="9" fill="#2E3D57"/><circle cx="13" cy="0" r="9" fill="#2E3D57"/>'
    if smoking:
        out += ('<path d="M-13 -10 q-8 -14 0 -26 M13 -10 q8 -14 0 -26" stroke="var(--muted)" '
                'stroke-width="5" fill="none" stroke-linecap="round" opacity="0.8"/>')
    return out + '</g>'


# 1. 작은 주문서 한 장이 주방을 몇 시간 묶어둬요
P1 = svg(320, sky(320)
         + person(70, 175, s=0.65, face=SMILE, **GUEST) + ticket(70, 145, 0.7)
         + label(70, 250, "⟦보통 주문|a normal order⟧", 10, "var(--muted)")
         + person(250, 160, s=0.85, face=SMILE + SWEAT, **CHEF) + stove(250, 250, 0.85, smoking=True)
         + ticket(380, 130, 1.1) + label(380, 90, "⟦이 요리를 10000번 다르게 바꿔서 설명해줘|redo this dish 10,000 different ways and explain each⟧", 11, "var(--bad)", cls="d")
         + label(380, 285, "⟦주문서는 한 장인데 화구는 멈추질 않아요|just one ticket, but the stove never stops⟧", 12, "var(--bad)")
         + person(600, 190, s=0.55, face=FROWN, **GUEST) + person(680, 200, s=0.5, face=FROWN, **GUEST)
         + label(640, 255, "⟦뒤에서 기다리는 손님들|guests still waiting in line⟧", 11, "var(--muted)")
         + label(380, 305, "⟦작은 주문서 한 장이 주방을 몇 시간 동안 묶어둬요|one small ticket can tie up the whole kitchen for hours⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 큰 주문인지 나쁜 주문인지 글자만 보고는 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ticket(170, 150, 1.0) + label(170, 210, "⟦생일잔치 백 인분 주문|a party order for 100 guests⟧", 11, "var(--ink)")
         + label(170, 230, "⟦진짜로 크고 정당한 주문|genuinely big, and legitimate⟧", 10, "var(--good)")
         + ticket(560, 150, 1.0) + label(560, 210, "⟦이 문장을, 50개 말로, 각각 다시 설명해줘|take this sentence, retell it in 50 languages, each one twice⟧", 10, "var(--bad)")
         + label(560, 230, "⟦글자는 몇 줄인데 일은 산더미예요|just a few lines, but a mountain of work⟧", 10, "var(--bad)")
         + person(380, 110, s=0.75, face=EYES, **CHEF)
         + label(380, 260, "⟦주방장은 글자 양이 아니라 '시키는 일의 크기'를 봐야 하는데, 그건 읽기 전엔 몰라요|it's not how long the ticket is — it's how much work it demands, and that's invisible until it's already cooking⟧", 12, "var(--ink)", cls="d"))

# 3. LLMDoS = 끝없는 주문으로 주방을 멈추는 공격 (hero)
P3 = svg(360, sky(360)
         + ticket(90, 110, 0.85) + ticket(90, 150, 0.85) + ticket(90, 190, 0.85)
         + label(90, 225, "⟦같은 주문서가 계속 쏟아져요|the same costly ticket keeps arriving⟧", 11, "var(--muted)")
         + person(330, 170, s=0.95, face=FROWN + SWEAT, **CHEF) + stove(330, 270, 1.0, smoking=True)
         + bell(470, 150, 0.8, ringing=True) + label(470, 200, "⟦화구가 멈추지 않아요|the stove won't quit⟧", 11, "var(--bad)")
         + person(630, 220, s=0.6, face=FROWN, **GUEST) + dish(630, 170, 0.4, bad=True)
         + label(630, 280, "⟦정상 손님은 요리를 못 받아요|the normal guest never gets served⟧", 11, "var(--muted)")
         + label(380, 30, "⟦LLMDoS = 끝없는 주문으로 주방을 멈추는 공격|LLMDoS = flooding the kitchen with costly orders until it stalls⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦트럭으로 밀어붙이는 게 아니라, 주문서 몇 장이 화구를 태워요|not a truckload at the door — a few tickets that burn out the stove⟧", 12, "var(--muted)"))

# 4. DDoS 는 문 앞에 트럭을, LLMDoS 는 화구에 불을
P4 = svg(330, sky(330)
         + board(40, 30, 320, 270, "⟦둘 다 주방을 멈추지만, 다르게 멈춰요|WHAT STOPS THE KITCHEN⟧",
                 ("⟦DDoS — 문 앞에 트럭을 쌓아요|DDoS — stacks trucks at the door⟧",
                  "⟦주문 자체는 간단해요|each order itself is simple⟧",
                  "⟦LLMDoS — 화구에 불을 계속 지펴요|LLMDoS — keeps the stove burning⟧",
                  "⟦주문서 몇 장이면 충분해요|a few tickets are enough⟧"), 1.0)
         + person(450, 90, s=0.55, face=FROWN, **SNEAK) + person(500, 100, s=0.5, face=FROWN, **SNEAK) + person(550, 95, s=0.52, face=FROWN, **SNEAK)
         + label(500, 170, "⟦트럭 여러 대 — 네트워크를 막아요|many trucks — clogging the road⟧", 11, "var(--muted)")
         + ticket(500, 230, 0.9) + stove(500, 290, 0.85, smoking=True)
         + label(500, 315, "⟦비싼 연산 한 번 — 화구를 태워요|one costly job — burning the stove⟧", 11, "var(--muted)"))

# 5. 한계: 숫자만 세는 울타리로는 못 막아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ticket(190, 120, 0.9) + label(190, 170, "⟦한 장씩만 보내면 울타리를 지나가요|send just one at a time — it slips past the fence⟧", 11, "var(--bad)")
         + label(190, 250, "⟦주문 '수'만 세는 울타리는 안 돼요|a fence that only counts tickets isn't enough⟧", 12, "var(--bad)", cls="d")
         + bell(570, 110, 0.8, ringing=False) + badge(650, 140, 0.6)
         + label(570, 230, "⟦일의 '크기'를 재는 울타리라야 막아요|a fence that measures the work itself can catch it⟧", 11, "var(--ink)")
         + label(570, 258, "⟦비용 한도, 시간 제한, 줄 세우기|cost budgets, time limits, fair queues⟧", 11, "var(--muted)")
         + label(380, 285, "⟦DDoS 는 트래픽을 퍼붓는 것, LLMDoS 는 비싼 연산을 시키는 것 — 막는 방법도 달라요|DDoS floods traffic; LLMDoS demands costly computation — so the defense differs too⟧", 12, "var(--ink)", cls="d"))

MAP_I = icon('<circle cx="32" cy="32" r="24" fill="#8B5E3C"/><circle cx="20" cy="32" r="6" fill="#2E3D57"/><circle cx="44" cy="32" r="6" fill="#2E3D57"/><path d="M20 14 q-6 -10 0 -20" stroke="var(--muted)" stroke-width="4" fill="none"/>')
COST_I = icon('<rect x="12" y="14" width="40" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 32 h24 M20 40 h16" stroke="#142033" stroke-width="2.5"/><circle cx="50" cy="16" r="10" fill="var(--bad)"/>')
TIME_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
QUEUE_I = icon('<rect x="10" y="40" width="10" height="16" fill="var(--good)"/><rect x="24" y="30" width="10" height="26" fill="var(--good)"/><rect x="38" y="20" width="10" height="36" fill="var(--good)"/><rect x="52" y="34" width="4" height="22" fill="var(--muted)"/>')

PAGE = {
    "slug": "llmdos", "order": 22,
    "title": ("화구를 멈추지 않는 주문", "The Order That Won't Let the Stove Rest"),
    "h1": ("<em>LLMDoS</em>이 뭐예요?", "What is <em>LLMDoS</em>?"),
    "sub": ("LLMDoS를, 작은 주문서 몇 장으로 주방의 화구를 계속 태워 멈추게 하는 이야기로 풀어봤어요.",
            "LLMDoS, told as a story about a few small tickets that keep the stove burning until the whole kitchen stalls."),
    "panels": [
        {"svg": P1, "alt": ("손님이 주문서 한 장으로 '이 요리를 만 번 바꿔서 설명해줘'라고 시킴. 주방장이 땀을 흘리며 화구에서 연기가 남. 뒤에는 기다리는 손님들", "A guest hands over one ticket asking to redo a dish 10,000 ways; the chef sweats as the stove smokes; guests wait in line behind"),
         "caption": ("작은 주문서 한 장이 주방을 몇 시간 동안 묶어둬요.", "One small ticket can tie up the whole kitchen for hours."),
         "small": ("글자는 한 줄인데, 그 한 줄이 시키는 일은 산더미예요.", "Just one line of text — but the work it demands is a mountain.")},
        {"svg": P2, "alt": ("왼쪽: 생일잔치 백 인분 주문, 진짜로 크고 정당함. 오른쪽: 짧은 문장이지만 50개 말로 각각 설명하라는 주문. 둘 다 겉보기엔 평범한 주문서", "Left: a genuinely large, legitimate order for a 100-guest party. Right: a short sentence demanding retelling in 50 languages. Both look like ordinary tickets"),
         "caption": ("큰 주문인지 나쁜 주문인지, 글자만 보고는 몰라요.", "You can't tell a big legitimate order from a costly one just by reading it."),
         "small": ("주방장은 '시키는 일의 크기'를 봐야 하는데, 그건 이미 요리를 시작한 뒤에야 보여요.", "What matters is how much work it demands — and that only shows up once cooking has already begun.")},
        {"svg": P3, "hero": True, "alt": ("같은 주문서가 계속 쏟아지고, 주방장이 땀을 흘리며 화구를 끄지 못함. 비상벨이 울리고, 정상 손님은 상한 접시를 받음", "The same costly ticket keeps arriving; the sweating chef can't shut the stove off; the alarm bell rings while a normal guest gets a spoiled dish"),
         "caption": ("LLMDoS는 끝없는 주문으로 주방을 멈추는 공격이에요.", "LLMDoS is an attack that floods the kitchen with costly orders until it stalls."),
         "small": ("트럭으로 문을 막는 게 아니라, 주문서 몇 장이 화구를 태워요.", "Not a truckload blocking the door — just a few tickets that burn out the stove."),
         "tricks": (4, [
             (MAP_I, ("일의 크기 미리 가늠", "Estimate the work first"), ("요리 전에 얼마나 걸릴지 재요", "guess the cost before cooking"), "calm"),
             (COST_I, ("주문서마다 비용 한도", "A cost budget per ticket"), ("한도를 넘으면 거절해요", "over budget? decline it"), "warm"),
             (TIME_I, ("요리 시간 제한", "A time limit per dish"), ("너무 오래 걸리면 멈춰요", "too long? cut it off"), "warm"),
             (QUEUE_I, ("공평하게 줄 세우기", "A fair queue"), ("한 손님이 줄을 독차지 못해요", "no one guest hogs the line"), "calm"),
         ])},
        {"svg": P4, "alt": ("약점판: DDoS는 문 앞에 트럭을 쌓고 주문은 간단함. LLMDoS는 화구에 불을 계속 지피고 주문서 몇 장이면 충분함. 왼쪽엔 몰래 쪽지 손님 여럿과 트럭, 오른쪽엔 주문서와 연기 나는 화구", "A map: DDoS stacks trucks at the door with simple orders; LLMDoS keeps the stove burning with just a few tickets. Left shows several guests and trucks; right shows a ticket and a smoking stove"),
         "caption": ("DDoS는 문 앞에 트럭을, LLMDoS는 화구에 불을 지펴요.", "DDoS stacks trucks at the door. LLMDoS keeps lighting the stove."),
         "small": ('일반 <a href="ddos-ko.html">DDoS</a>는 트래픽 '
                   '양으로 밀어붙이지만, LLMDoS는 한 번의 요청이 시키는 연산 비용으로 고갈시켜요.',
                   'Ordinary <a href="ddos-en.html">DDoS</a> pushes with sheer traffic volume — LLMDoS exhausts resources through the compute cost a single request demands.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 주문서를 한 장씩 보내면 수를 세는 울타리를 지나감. 오른쪽 초록: 비상벨과 검사관 배지가 비용·시간·줄 세우기로 막음", "Left, red: sending tickets one at a time slips past a fence that only counts. Right, green: a bell and an inspector's badge stand for cost, time, and fair-queue limits that catch it"),
         "caption": ("주문 '수'만 세는 울타리로는 못 막아요.", "A fence that only counts tickets isn't enough to stop it."),
         "small": ('<a href="ratelimiting-ko.html">속도 제한</a>을 숫자가 아니라 비용으로 걸어야 해요 — '
                   '이 괴리는 주방장이 글자를 믿고 따르는 본능 때문에 더 커져요, 비싼 주문인지 스스로 의심하지 않거든요.',
                   'The <a href="ratelimiting-en.html">rate limit</a> has to measure cost, not just count — and this gap is wider precisely because the chef trusts every order as written, never suspecting on its own that one is too costly.')},
    ],
    "summary": (("<b>LLMDoS</b> = 주문서 몇 장으로 <b>주방의 화구를 계속 태워</b> 멈추게 하는 공격. 트럭을 쌓는 게 아니라 <b>비싼 연산을 계속 시켜서</b> 고갈시켜요.",
                 "<b>LLMDoS</b> = an attack that keeps <b>the kitchen's stove burning</b> with just a few tickets until it stalls. Instead of stacking trucks, it exhausts the kitchen by <b>demanding costly computation</b> over and over."),
                ("LLMDoS(LLM Denial of Service)는 길거나 반복적이거나 재귀적으로 확장되는 요청을 보내 모델의 연산·메모리·시간 자원을 고갈시키는 공격이에요. 전통적 DDoS가 네트워크 트래픽 양으로 밀어붙이는 것과 달리, LLMDoS는 적은 수의 요청으로도 비싼 토큰 생성·긴 컨텍스트 처리를 유발해 서비스를 느려지거나 멈추게 할 수 있어요. 토큰/시간 한도, 요청당 비용 산정, 공평한 큐잉이 주요 방어예요.",
                 "LLMDoS (LLM Denial of Service) is an attack that exhausts a model's compute, memory, or time budget by sending long, repetitive, or recursively expanding requests. Unlike traditional DDoS, which pushes with sheer network traffic volume, LLMDoS can degrade or stall a service with only a handful of requests by triggering expensive token generation or long-context processing. Token/time limits, per-request cost estimation, and fair queuing are the main defenses.")),
    "glossary": [
        ("LLMDoS", "LLMDoS", ("화구를 계속 태우는 주문.", "The order that keeps the stove burning."), ("주문서 몇 장으로도 주방 전체를 멈출 수 있어요.", "Just a few tickets can stall the whole kitchen.")),
        ("연산 폭탄 주문서", "Compute-bomb ticket", ("짧지만 산더미 같은 일을 시키는 쪽지.", "A short note that demands a mountain of work."), ("재귀적으로 확장되는 요청이 대표적이에요.", "A recursively expanding request is the classic shape of one.")),
        ("DDoS 비교", "vs. DDoS", ("문 앞에 트럭을 쌓는 것.", "Stacking trucks at the door."), ('네트워크 트래픽을 퍼붓는 일반 공격이에요. → <a href="ddos-ko.html">보안 마을의 DDoS</a>', 'The general attack that floods network traffic. → <a href="ddos-en.html">the security world\'s DDoS</a>')),
        ("속도 제한", "Rate limiting", ("들어오는 주문서를 줄 세우는 일.", "Lining up incoming tickets."), ('수가 아니라 비용으로 걸어야 LLMDoS를 막아요. → <a href="ratelimiting-ko.html">놀이공원의 속도 제한</a>', 'It has to gate on cost, not count, to stop LLMDoS. → <a href="ratelimiting-en.html">the theme park\'s rate limiting</a>')),
        ("가용성", "Availability", ("손님이 제때 요리를 받을 수 있는 상태.", "Guests getting served in time."), ('화구가 멈추면 가장 먼저 깨지는 것이에요. → <a href="reliability-ko.html">놀이공원의 안정성</a>', 'It\'s the first thing to break when the stove stalls. → <a href="reliability-en.html">the theme park\'s reliability</a>')),
        ("토큰 한도", "Token limit", ("한 번에 쓸 수 있는 콩의 최대 개수.", "The max number of beans usable at once."), ('주문서 자체의 크기를 미리 막아요. → <a href="token-ko.html">앵무새 마을의 콩</a>', 'It caps the size of the ticket itself ahead of time. → <a href="token-en.html">the parrot world\'s beans</a>')),
        ("비용 기반 제한", "Cost-based throttling", ("숫자가 아니라 일의 크기로 재는 울타리.", "A fence that measures work, not just count."), ("같은 숫자의 주문서라도 비용은 천차만별이에요.", "Even the same number of tickets can carry wildly different costs.")),
        ("용량 계획", "Capacity planning", ("화구가 몇 개까지 동시에 버티는지 미리 재는 일.", "Figuring out ahead of time how many stoves can run at once."), ('평소 부하와 몰릴 때를 미리 재야 해요. → <a href="capacityplanning-ko.html">놀이공원의 용량 계획</a>', 'You have to size for both normal and peak load ahead of time. → <a href="capacityplanning-en.html">the theme park\'s capacity planning</a>')),
    ],
}
