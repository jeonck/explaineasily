from _draw import *
from _world import *

# 1. 거절당한 손님이 바로바로 계속 다시 줄서서 창구가 더 바빠져요
P1 = svg(300, sky(300)
         + booth(560, 230, 1.0, label_text="⟦창구|BOOTH⟧")
         + queueline(260, 174, 5, 0.5, 30)
         + person(80, 174, s=0.5, face=FROWN, hat=None, shirt="#C9822B")
         + bubble(10, 100, 170, 44, "⟦거절당했어요... 또 줄서야지|got rejected... back in line right away⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + '<path d="M115 200 Q190 230 260 200" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
         + label(380, 284, "⟦거절당한 손님이 바로바로 계속 다시 줄서서 창구가 더 바빠져요|rejected guests line right back up immediately, and the booth gets even busier⟧", 12, "var(--ink)"))

# 2. 왜: 다들 한꺼번에 바로 다시 시도하면 몰림이 더 심해져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/><ellipse cx="380" cy="300" rx="440" ry="36" fill="var(--good-soft)"/>'
         + booth(380, 230, 1.0, label_text="⟦창구|BOOTH⟧")
         + queueline(80, 174, 4, 0.48, 28) + queueline(480, 174, 4, 0.48, 28)
         + label(380, 40, "⟦거절당한 손님들이 다 같이 동시에 다시 줄서요|all the rejected guests line up again at the exact same moment⟧", 12, "var(--bad)", cls="d")
         + label(380, 284, "⟦다들 한꺼번에 바로 다시 시도하면 몰림이 더 심해져요|if everyone retries at once, the crowding only gets worse⟧", 12, "var(--ink)"))

# 3. hero: 잠깐 쉬었다가, 사람마다 조금씩 다르게 다시 줄서요
REST_I = icon('<circle cx="24" cy="24" r="16" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M24 14 v10 l8 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M44 40 q8 4 2 12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
DOUBLE_I = icon('<path d="M8 48 h10 v-10 h10 M34 48 h10 v-20 h10" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="18" cy="38" r="3" fill="var(--bad)"/><circle cx="54" cy="28" r="3" fill="var(--bad)"/>')
JITTER_I = icon('<path d="M8 32 h8 M24 24 h8 M40 36 h8" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><circle cx="8" cy="32" r="4" fill="var(--good)"/><circle cx="24" cy="24" r="4" fill="var(--good)"/><circle cx="40" cy="36" r="4" fill="var(--good)"/>')
GIVEUP_I = icon('<path d="M14 14 L50 50 M50 14 L14 50" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/><circle cx="32" cy="32" r="26" fill="none" stroke="var(--muted)" stroke-width="3"/>')

P3 = svg(360, sky(360)
         + booth(600, 260, 1.0, label_text="⟦창구|BOOTH⟧")
         + person(130, 170, s=0.55, face=EYES, hat=None, shirt="#C9822B")
         + bubble(40, 90, 190, 50, "⟦조금 쉬었다가 다시 줄서요|I'll rest a bit, then line up again⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(300, 190, s=0.5, face=EYES, hat=None, shirt="#7B3FA0")
         + '<path d="M165 220 Q230 250 300 240" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
         + label(380, 38, "⟦잠깐 쉬었다가, 사람마다 조금씩 다르게 다시 줄서요|rest a moment, then line up again — each person waits a slightly different amount⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦한꺼번에 몰리지 않게요|so everyone doesn't rush back at once⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 실패 시간선 — 1초, 2초, 4초 쉼 + 지터
P4 = svg(320, sky(320, ground=False)
         + '<path d="M60 150 H700" stroke="var(--stone-dark)" stroke-width="3"/>'
         + '<circle cx="90" cy="150" r="7" fill="var(--bad)"/>' + label(90, 190, "⟦1번째 실패|1st fail⟧", 10, "var(--ink)")
         + '<path d="M90 150 Q160 110 230 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>' + label(160, 100, "⟦1초+지터|1s + jitter⟧", 10, "var(--muted)")
         + '<circle cx="230" cy="150" r="7" fill="var(--bad)"/>' + label(230, 190, "⟦2번째 실패|2nd fail⟧", 10, "var(--ink)")
         + '<path d="M230 150 Q330 90 430 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>' + label(330, 80, "⟦2초+지터|2s + jitter⟧", 10, "var(--muted)")
         + '<circle cx="430" cy="150" r="7" fill="var(--bad)"/>' + label(430, 190, "⟦3번째 실패|3rd fail⟧", 10, "var(--ink)")
         + '<path d="M430 150 Q560 70 670 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>' + label(560, 58, "⟦4초+지터|4s + jitter⟧", 10, "var(--muted)")
         + '<circle cx="670" cy="150" r="7" fill="var(--good)"/>' + label(670, 190, "⟦성공|success⟧", 10, "var(--ink)")
         + label(380, 284, "⟦실패할 때마다 쉬는 시간이 점점 길어지고, 사람마다 살짝 다르게 쉬어요|each failure doubles the wait, and each person's wait is nudged slightly differently⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 무한정 재시도하면 끝까지 기다리기만 해요
P5 = svg(300, sky(300)
         + person(160, 150, s=0.65, face=FROWN + SWEAT, hat=None, shirt="#4A5A72")
         + '<path d="M160 90 m-26 0 a26 26 0 1 1 52 0 a26 26 0 1 1 -52 0" stroke="var(--muted)" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
         + label(160, 247, "⟦계속 쉬었다 또 시도... 끝이 없어요|rest, retry, rest, retry... it never ends⟧", 10, "var(--bad)")
         + board(460, 50, 240, 120, "⟦규칙|RULE⟧", ("⟦최대 3번까지만|up to 3 times only⟧", "⟦그래도 안 되면 그만두기|then give up for good⟧", '⟦→ 서킷 브레이커로|→ hand off to the circuit breaker⟧'), 1.0)
         + label(380, 284, "⟦무한정 재시도하면 끝까지 기다리기만 해요 — 최대 횟수를 정해 포기할 줄도 알아야 해요|retry forever and you just wait forever — you need a max count and the sense to give up⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "retrybackoff", "order": 28,
    "title": ("잠깐 쉬었다 다시 줄서기", "Resting a Bit, Then Lining Up Again"),
    "h1": ("<em>재시도와 백오프</em>가 뭐예요?", "What is <em>Retry with Backoff</em>?"),
    "sub": ("재시도와 백오프를 거절당하면 잠깐 쉬었다 다시 줄서는 손님 이야기로 풀어봤어요.",
            "Retry with backoff, told as a story about guests who rest a moment before lining up again after being turned away."),
    "panels": [
        {"svg": P1, "alt": ("거절당한 손님이 '또 줄서야지' 하며 바로 다시 줄의 끝에 섬. 창구는 더 바빠짐", "A rejected guest says they'll line up right away again, joining the back of the line as the booth gets busier"),
         "caption": ("거절당한 손님이 바로바로 계속 다시 줄서서 창구가 더 바빠져요.", "Rejected guests line right back up immediately, and the booth gets even busier."),
         "small": ("쉬지 않고 바로 다시 시도하면 창구가 쉴 틈이 없어요.", "Retrying instantly, with no rest, gives the booth no breathing room.")},
        {"svg": P2, "alt": ("창구 양옆에서 거절당한 손님 무리가 동시에 다시 줄을 서는 장면", "Groups of rejected guests on both sides line back up at the exact same moment"),
         "caption": ("다들 한꺼번에 바로 다시 시도하면 몰림이 더 심해져요.", "If everyone retries at once, the crowding only gets worse."),
         "small": ("거절당한 손님들이 똑같은 순간에 다 같이 돌아와요.", "Everyone comes back at the same instant, in one big wave.")},
        {"svg": P3, "hero": True, "alt": ("손님 한 명이 '조금 쉬었다가 다시 줄서요'라고 말하고, 다른 손님은 살짝 다른 시점에 줄로 돌아감", "One guest says they'll rest a bit before lining up again, while another guest returns at a slightly different moment"),
         "caption": ("잠깐 쉬었다가, 사람마다 조금씩 다르게 다시 줄서요.", "Rest a moment, then line up again — each person waits a slightly different amount."),
         "small": ("한꺼번에 몰리지 않게요.", "So everyone doesn't rush back at once."),
         "tricks": (4, [
             (REST_I, ("바로 말고 잠깐 쉬기", "Don't retry instantly — rest first"), ("숨 고르고요", "catch your breath"), "calm"),
             (DOUBLE_I, ("점점 더 오래 쉬기", "Rest longer each time"), ("지수 백오프예요", "that's exponential backoff")),
             (JITTER_I, ("사람마다 조금 다르게", "Vary it slightly per person"), ("지터예요", "that's jitter"), "warm"),
             (GIVEUP_I, ("너무 여러 번이면 포기", "Give up after too many tries"), ("다른 방법으로요", "and try another way")),
         ])},
        {"svg": P4, "alt": ("실패할 때마다 쉬는 시간이 1초, 2초, 4초로 늘어나는 시간선. 각 구간마다 지터로 살짝 다르게 표시됨", "A timeline where the rest between failures grows 1s, 2s, 4s, each nudged slightly by jitter"),
         "caption": ("실패할 때마다 쉬는 시간이 점점 길어지고, 사람마다 살짝 다르게 쉬어요.", "Each failure doubles the wait, and each person's wait is nudged slightly differently."),
         "small": ("1초, 2초, 4초... 배로 늘어나요.", "1 second, 2, 4 — it doubles each time.")},
        {"svg": P5, "alt": ("손님이 끝없이 쉬었다 다시 시도하는 원을 빙빙 돌고, 옆 안내판엔 최대 3번까지만 하고 그만두라는 규칙이 적혀 있음", "A guest loops endlessly through rest-and-retry while a nearby sign states a rule: try at most 3 times, then stop"),
         "caption": ("무한정 재시도하면 끝까지 기다리기만 해요.", "Retry forever and you just wait forever."),
         "small": ("최대 횟수를 정해 포기할 줄도 알아야 해요.", "You need a max count and the sense to give up.")},
    ],
    "summary": (("<b>재시도와 백오프</b> = 거절당하면 <b>바로 다시 말고 잠깐 쉬었다</b>, 실패할수록 <b>점점 더 오래</b> 쉬면서, <b>사람마다 살짝 다르게</b> 다시 줄서는 일. 너무 많이 실패하면 <b>포기</b>해요.",
                 "<b>Retry with backoff</b> = instead of retrying instantly, <b>resting a bit</b> after rejection, waiting <b>longer each time</b> it fails, with each wait <b>nudged slightly differently</b> per guest — and <b>giving up</b> after too many tries."),
                ("실패한 요청을 다시 보내되, 매번 대기 시간을 두 배로 늘리는 것을 지수 백오프라고 해요. 대기 시간에 무작위 편차를 더하는 걸 지터라고 하고, 이게 없으면 모두가 같은 순간에 다시 몰리는 thundering herd가 생겨요. 최대 재시도 횟수를 넘으면 포기하고 서킷 브레이커 같은 다른 방법으로 넘어가야 해요.",
                 "Resending a failed request, but doubling the wait each time, is called exponential backoff. Adding a random variation to that wait is jitter — without it, everyone retries at the exact same moment, a thundering herd. Once the max retry count is exceeded, give up and hand off to something like a circuit breaker instead.")),
    "glossary": [
        ("재시도", "Retry", ("실패하면 다시 줄서는 것.", "Lining up again after a failure."), ("바로 하면 오히려 더 몰려요.", "Doing it instantly only makes the crowding worse.")),
        ("지수 백오프", "Exponential backoff", ("실패할수록 쉬는 시간을 두 배씩 늘리는 것.", "Doubling the rest time with each failure."), ("1초, 2초, 4초... 이렇게 늘어나요.", "1 second, 2, 4 — it keeps doubling.")),
        ("지터", "Jitter", ("쉬는 시간에 사람마다 살짝 무작위로 다르게 주는 것.", "Adding a small random difference to each person's wait."), ("다 같이 동시에 몰리는 걸 막아요.", "Keeps everyone from rushing back at the exact same moment.")),
        ("최대 재시도 횟수", "Max retry count", ("몇 번까지 다시 시도하고 그만둘지 정한 수.", "The number of tries allowed before giving up."), ("이게 없으면 끝없이 기다리기만 해요.", "Without it, you just wait forever.")),
        ("타임아웃", "Timeout", ("한 번 시도에 얼마나 기다릴지 정한 한도.", "The limit on how long one attempt is allowed to wait."), ("타임아웃이 지나야 '실패'로 치고 재시도를 시작해요.", "Only after the timeout passes does it count as a failure and start a retry.")),
        ("서킷 브레이커", "Circuit breaker", ("아예 안 되는 곳엔 재시도도 그만두고 안 보내는 빨간 버튼.", "The red button that stops even retrying somewhere entirely broken."), ('최대 횟수를 넘기면 이쪽으로 넘어가요. → <a href="circuitbreaker-ko.html">고장나면 누르는 빨간 버튼</a>', 'Exceed the max retries, and this takes over. → <a href="circuitbreaker-en.html">the red button you press when something breaks</a>')),
        ("멱등성", "Idempotency", ("같은 요청을 여러 번 보내도 결과가 한 번과 같은 성질.", "Sending the same request more than once still gives the same result as sending it once."), ("재시도해도 안전하려면 이 성질이 꼭 필요해요.", "Retrying safely depends on this property being true.")),
        ("백프레셔", "Backpressure", ("안쪽이 꽉 차면 입구가 미리 속도를 늦추는 것.", "The entrance slowing itself down when the inside is full."), ('재시도가 너무 많아지면 결국 이것도 함께 필요해져요. → <a href="backpressure-ko.html">입구를 잠깐 막기</a>', 'Too many retries piling up is exactly when this becomes necessary too. → <a href="backpressure-en.html">slowing the entrance for a moment</a>')),
    ],
}
