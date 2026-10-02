from _draw import *
from _world import *

# 1. 손님이 한꺼번에 밀려들어 안쪽 창구까지 꽉 찼어요
P1 = svg(330, sky(330)
         + booth(110, 230, 1.0, label_text="⟦입구|ENTRANCE⟧")
         + booth(650, 230, 1.1, label_text="⟦안쪽 창구|INNER BOOTH⟧")
         + queueline(260, 176, 9, 0.48, 30)
         + label(400, 40, "⟦안쪽까지 줄이 꽉 찼어요|the line is packed all the way to the inner booth⟧", 12, "var(--bad)", cls="d")
         + label(380, 310, "⟦손님이 한꺼번에 밀려들어 안쪽 창구까지 꽉 찼어요|guests rush in all at once, and even the inner booth fills up⟧", 13, "var(--ink)"))

# 2. 왜: 안쪽이 바쁜데 입구는 계속 더 받으면 결국 다 같이 느려져요
P2 = svg(330, '<rect width="760" height="330" fill="var(--bad-soft)"/><ellipse cx="380" cy="330" rx="440" ry="36" fill="var(--good-soft)"/>'
         + booth(680, 230, 0.9, label_text="⟦안쪽|INNER⟧")
         + booth(70, 230, 0.9, label_text="⟦입구|ENTRANCE⟧")
         + queueline(300, 182, 10, 0.46, 28)
         + person(140, 110, s=0.6, face=FROWN + SWEAT, **OPERATOR)
         + bubble(30, 20, 230, 50, "⟦안쪽이 바쁜데 계속 들여보내면...|if the inside is busy but we keep letting people in...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 310, "⟦안쪽이 바쁜데 입구는 계속 더 받으면, 결국 다 같이 느려져요|if the inside is busy but the entrance keeps admitting more, everyone slows down together⟧", 12, "var(--ink)"))

# 3. hero: 안쪽이 꽉 차면 입구에서 미리 속도를 늦춰요
WATCHFULL_I = icon('<circle cx="32" cy="36" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 36 L46 22" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="36" r="3" fill="var(--bad)"/><path d="M32 6 l-6 10 h12z" fill="var(--bad)"/>')
SLOWBAR_I = icon('<path d="M8 50 h48" stroke="var(--stone-dark)" stroke-width="4"/><circle cx="30" cy="50" r="5" fill="var(--stone-dark)"/><rect x="27" y="16" width="8" height="30" rx="3" fill="var(--accent)" transform="rotate(35 30 46)"/>')
TELLSIGN_I = icon('<rect x="10" y="12" width="44" height="28" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 40 l-6 12 M42 40 l6 12" stroke="var(--line)" stroke-width="3" stroke-linecap="round"/><path d="M18 22 h28 M18 30 h18" stroke="#142033" stroke-width="3" stroke-linecap="round"/>')
TRICKLE_I = icon('<path d="M6 32 h26" stroke="var(--good)" stroke-width="6" stroke-linecap="round"/><path d="M36 18 v28" stroke="var(--stone-dark)" stroke-width="5"/><path d="M36 18 l10 -4 M36 46 l10 4" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/><path d="M50 32 h8" stroke="var(--good)" stroke-width="4" stroke-linecap="round" stroke-dasharray="3 4"/>')

P3 = svg(360, sky(360)
         + booth(650, 260, 1.0, label_text="⟦안쪽|INNER⟧")
         + gauge(650, 130, 0.8, level=0.85, label_text="⟦혼잡|busy⟧")
         + booth(140, 260, 1.0, lit=False, label_text="⟦입구|ENTRANCE⟧")
         + person(140, 150, s=0.6, face=EYES, **OPERATOR)
         + bubble(20, 60, 230, 48, "⟦지금은 잠깐만 기다려 주세요|please wait just a moment⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + queueline(300, 194, 3, 0.45, 34)
         + label(380, 38, "⟦안쪽이 꽉 차면 입구에서 미리 속도를 늦춰요|when the inside is full, the entrance slows down first⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦다 받고 나중에 터지는 것보다 나아요|better than admitting everyone and bursting later⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 안쪽(빨강) → 신호선 → 입구(주황), 신호 없으면 전체 멈춤과 비교
P4 = svg(320, sky(320)
         + '<circle cx="600" cy="90" r="20" fill="var(--bad)"/>' + label(600, 128, "⟦안쪽 꽉 참|inner full⟧", 11, "var(--ink)")
         + '<path d="M580 90 L180 90" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(380, 76, "⟦신호선|signal⟧", 10, "var(--muted)")
         + '<circle cx="160" cy="90" r="20" fill="var(--accent)"/>' + label(160, 128, "⟦입구 느려짐|entrance slows⟧", 11, "var(--ink)")
         + ride(420, 230, 0.75, color="var(--stone-dark)", closed=True, label_text="⟦신호 없으면 전체 멈춤|no signal: everything stops⟧")
         + label(380, 310, "⟦꽉 참 신호가 입구까지 가야, 입구가 미리 늦출 수 있어요|the full signal must reach the entrance so it can slow down in advance⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 너무 심하게 막으면 손님이 다른 공원으로 가버려요
P5 = svg(320, sky(320)
         + booth(160, 230, 1.0, lit=False, label_text="⟦입구 — 너무 막음|entrance — too strict⟧")
         + person(50, 150, s=0.6, face=FROWN, hat=None, shirt="#7B3FA0")
         + bubble(0, 50, 210, 50, "⟦여긴 너무 느려요, 다른 데 갈래요|too slow here, I'll go elsewhere⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + minipark(650, 190, 0.9)
         + '<path d="M270 190 L570 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 310, "⟦입구를 너무 심하게 막으면 손님이 아예 다른 공원으로 가버려요 — 적당히가 어려워요|block the entrance too hard, and guests leave for another park entirely — the right amount is hard to find⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "backpressure", "order": 25,
    "title": ("입구를 잠깐 막기", "Slowing the Entrance for a Moment"),
    "h1": ("<em>백프레셔</em>가 뭐예요?", "What is <em>Backpressure</em>?"),
    "sub": ("백프레셔를 안쪽 창구가 꽉 차면 입구부터 속도를 늦추는 놀이공원 이야기로 풀어봤어요.",
            "Backpressure, told as a story about an entrance that slows down the moment the inner booth fills up."),
    "panels": [
        {"svg": P1, "alt": ("입구와 안쪽 창구 사이에 손님 줄이 가득 차 있고, 안쪽 창구 쪽으로 줄이 쏠려 있음", "A line of guests packed between the entrance and the inner booth, piling up near the inner booth"),
         "caption": ("손님이 한꺼번에 밀려들어 안쪽 창구까지 꽉 찼어요.", "Guests rush in all at once, and even the inner booth fills up."),
         "small": ("안쪽 창구가 바빠서 줄이 입구 쪽까지 이어져요.", "The inner booth is so busy the line stretches back to the entrance.")},
        {"svg": P2, "alt": ("관제실 요원이 땀을 흘리며 '안쪽이 바쁜데 계속 들여보내면' 걱정하는 동안 줄이 계속 늘어남", "A sweating operator worries about letting more people in while the line keeps growing"),
         "caption": ("안쪽이 바쁜데 입구가 계속 더 받으면, 결국 다 같이 느려져요.", "If the inside is busy but the entrance keeps admitting more, everyone slows down together."),
         "small": ("안쪽부터 사람이 쌓이기 시작해서 공원 전체가 느려져요.", "Guests start stacking up from the inside out, until the whole park slows.")},
        {"svg": P3, "hero": True, "alt": ("안쪽 창구 계기판이 혼잡을 가리키고, 입구는 불을 줄인 채 요원이 '잠깐만 기다려 주세요' 안내함", "The inner booth's gauge shows it's busy while a dimmed entrance operator asks guests to wait"),
         "caption": ("안쪽이 꽉 차면 입구에서 미리 속도를 늦춰요.", "When the inside is full, the entrance slows down first."),
         "small": ("다 받고 나중에 터지는 것보다 나아요.", "Better than admitting everyone and bursting later."),
         "tricks": (4, [
             (WATCHFULL_I, ("안쪽 꽉 참 알아채기", "Notice the inside is full"), ("미리미리요", "catch it early"), "calm"),
             (SLOWBAR_I, ("입구 속도 늦추기", "Slow the entrance"), ("완전히 막진 않아요", "not a full stop")),
             (TELLSIGN_I, ("손님께 안내하기", "Tell the guests"), ("잠시 후 다시 시도하라고요", "ask them to try again soon"), "warm"),
             (TRICKLE_I, ("조금씩만 흘려보내기", "Let a trickle through"), ("딱 안쪽이 받을 만큼만", "only as much as the inside can take")),
         ])},
        {"svg": P4, "alt": ("안쪽 창구가 빨간 원(꽉 참), 신호선을 타고 입구가 주황 원(느려짐)으로 바뀜. 아래엔 신호가 없을 때 전체가 멈춘 기구", "The inner booth is a red circle (full), a signal line turns the entrance orange (slowed); below, a ride stopped entirely because no signal arrived"),
         "caption": ("꽉 참 신호가 입구까지 가야, 입구가 미리 늦출 수 있어요.", "The full signal must reach the entrance so it can slow down in advance."),
         "small": ("신호가 없으면 입구는 계속 받다가 전체가 한꺼번에 멈춰요.", "Without the signal, the entrance keeps admitting guests until everything stops at once.")},
        {"svg": P5, "alt": ("불을 완전히 끈 입구 앞에서 손님이 '다른 데 갈래요' 하며 돌아서고, 멀리 쌍둥이 공원을 향해 걸어감", "A guest turns away from a fully dimmed entrance saying they'll go elsewhere, walking toward a twin park in the distance"),
         "caption": ("입구를 너무 심하게 막으면 손님이 아예 다른 공원으로 가버려요.", "Block the entrance too hard, and guests leave for another park entirely."),
         "small": ("적당히 늦추는 게 어려워요 — 너무 막으면 손님을 잃어요.", "Finding the right amount is hard — slow it too much and you lose guests.")},
    ],
    "summary": (("<b>백프레셔</b> = 안쪽 창구가 <b>꽉 차면</b> 입구가 <b>미리 속도를 늦추는</b> 일. 완전히 막지 않고 <b>조금씩만</b> 흘려보내요.",
                 "<b>Backpressure</b> = when the inner booth is <b>full</b>, the entrance <b>slows down in advance</b> — not stopping entirely, just letting a <b>trickle</b> through."),
                ("처리하는 쪽이 밀리면 받는 쪽 속도를 낮추는 흐름 제어 기법이에요. 안쪽이 꽉 찬 상태를 포화라고 부르고, 신호가 전달되는 경로(큐, 연결)를 타고 거슬러 올라가요. 입구를 너무 세게 막으면 처리율이 뚝 떨어지므로 정도 조절이 핵심이에요.",
                 "A flow-control technique: when a downstream stage is overwhelmed, the upstream slows its own rate. The full state is called saturation, and the signal travels back upstream through whatever carries it — a queue, a connection. Throttle too hard and throughput collapses, so tuning the degree matters.")),
    "glossary": [
        ("백프레셔", "Backpressure", ("안쪽이 꽉 차면 입구가 스스로 늦추는 일.", "The entrance slowing itself down when the inside is full."), ("완전히 막지 않고 조금씩만 흘려보내요.", "Not a full stop — just a trickle through.")),
        ("흐름 제어", "Flow control", ("받는 쪽 속도에 맞춰 보내는 쪽을 조절하는 것.", "Adjusting the sender's pace to match the receiver's."), ("백프레셔는 흐름 제어의 한 가지 방법이에요.", "Backpressure is one way to do flow control.")),
        ("과부하", "Overload", ("감당할 수 있는 양을 넘어선 상태.", "More coming in than can be handled."), ("과부하를 미리 알아채는 게 백프레셔의 출발점이에요.", "Noticing overload early is where backpressure starts.")),
        ("포화", "Saturation", ("안쪽 창구가 더 못 받는 꽉 찬 상태.", "The inner booth being as full as it can get."), ("관제실 계기판 네 개 중 하나로 늘 지켜봐요.", "One of the four gauges the control room always watches.")),
        ("속도 제한", "Rate limiting", ("한 번에 몇 명까지만 받는 규칙.", "A rule capping how many get in at once."), ("백프레셔는 안쪽 상태를 보고 스스로 늦추고, 속도 제한은 미리 정한 숫자로 막아요 — 비슷하지만 신호의 출처가 달라요.", "Backpressure slows itself based on inner state; rate limiting caps at a number fixed in advance — similar, but the signal comes from a different place.")),
        ("큐", "Queue", ("창구 앞에 쌓이는 대기줄.", "The line piling up in front of a booth."), ("백프레셔 신호는 보통 이 줄의 길이를 보고 나와요.", "The backpressure signal usually comes from watching how long this line gets.")),
        ("우아한 저하", "Graceful degradation", ("힘들 땐 일부 기능만 줄여서라도 계속 여는 것.", "Cutting back some features to stay open at all, when things get hard."), ("백프레셔로 못 버티면 다음 방법이에요.", "The next move when backpressure alone isn't enough.")),
        ("서킷 브레이커", "Circuit breaker", ("아예 안 되는 곳엔 보내지 않는 빨간 버튼.", "The red button that stops sending guests somewhere entirely broken."), ('백프레셔는 늦추기, 이건 아예 끊기예요. → <a href="circuitbreaker-ko.html">고장나면 누르는 빨간 버튼</a>', 'Backpressure slows things down; this cuts them off entirely. → <a href="circuitbreaker-en.html">the red button you press when something breaks</a>')),
    ],
}
