from _draw import *
from _world import *


def basket(x, y, s=1.0, n=3, label_text=None, fill="#C9A86A"):
    """바구니(큐). (x,y) 는 바닥선(ground) 기준점. 안에 쌓인 주문서 n장을 그린다."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    out += '<path d="M-40 -50 L-48 4 Q-48 16 -36 16 L36 16 Q48 16 48 4 L40 -50 Z" fill="none" stroke="#5A3B22" stroke-width="4"/>'
    out += "".join(f'<line x1="{i}" y1="-48" x2="{i}" y2="14" stroke="#5A3B22" stroke-width="2" opacity="0.5"/>' for i in range(-32, 33, 16))
    out += '<path d="M-48 2 Q0 18 48 2" fill="none" stroke="#5A3B22" stroke-width="3"/>'
    for i in range(n):
        yy = -56 - i * 16
        rot = -6 if i % 2 else 5
        out += f'<rect x="-28" y="{yy - 8}" width="56" height="16" rx="2" fill="{fill}" stroke="#8B5E3C" stroke-width="2" transform="rotate({rot} 0 {yy})"/>'
    if label_text:
        out += label(0, 36, label_text, 11, "var(--ink)")
    return out + "</g>"


# 1. 주문이 한꺼번에 몰려 직원이 손님을 놓쳐요
P1 = svg(340, sky(340)
         + booth(380, 260, 1.0, label_text="⟦간식 창구|SNACK COUNTER⟧")
         + queueline(90, 204, 6, 0.45, 30)
         + person(440, 204, s=0.6, face=FROWN + SWEAT, **MECHANIC) + bubble(440, 100, 190, 38, "⟦한 번에 너무 많아요!|too many at once!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 320, "⟦주문이 한꺼번에 몰려 직원이 손님을 놓쳐요|orders pile up all at once and the clerk can\'t keep up⟧", 12, "var(--ink)"))

# 2. 왜: 받는 쪽이 바쁠 때 보내는 쪽이 기다리면 둘 다 느려져요 (bad-soft)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(150, 178, s=0.6, hat=FOLK[1][0], shirt=FOLK[1][1], face=FROWN) + bubble(60, 95, 210, 40, "⟦아직 못 받아요?|still can\'t place my order?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(560, 178, s=0.6, face=FROWN + SWEAT, **MECHANIC) + bubble(460, 95, 220, 40, "⟦손도 못 대고 있어요|I can\'t even get to it⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦받는 쪽이 바쁠 때 보내는 쪽이 기다려야 하면 둘 다 느려져요|if the sender must wait while the receiver is busy, both slow down⟧", 12, "var(--bad)"))

# 3. 바구니에 쌓아두면, 보내는 쪽과 받는 쪽이 각자 속도대로 움직여요 (hero)
P3 = svg(360, sky(360)
         + queueline(60, 250, 3, 0.45, 30)
         + person(230, 239, s=0.55, face=SMILE, **MECHANIC)
         + '<path d="M300 260 L360 260" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M344 252 l16 8 l-16 8" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(420, 170, "⟦주문 바구니|ORDER BASKET⟧", 12, "var(--ink)", cls="d") + basket(420, 300, 1.0, n=4)
         + '<path d="M480 260 L540 260" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M524 252 l16 8 l-16 8" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + person(610, 239, s=0.55, face=EYES, **OPERATOR)
         + label(380, 340, "⟦주문서를 바구니에 쌓아두면, 보내는 쪽과 받는 쪽이 각자 속도대로 움직여요|put orders in a basket, and sender and receiver each move at their own pace⟧", 13, "var(--ink)", cls="d"))

# 4. 넣는 사람 → 쌓인 주문서 → 하나씩 꺼내는 사람
P4 = svg(300, sky(300)
         + person(90, 184, s=0.5, hat=FOLK[1][0], shirt=FOLK[1][1], face=SMILE) + label(90, 250, "⟦주문서 넣는 사람|order placer⟧", 11, "var(--muted)")
         + '<path d="M150 200 L230 200" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M214 192 l16 8 l-16 8" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(380, 110, "⟦쌓인 주문서|QUEUED ORDERS⟧", 12, "var(--ink)", cls="d") + basket(380, 240, 0.9, n=5)
         + '<path d="M470 200 L550 200" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M534 192 l16 8 l-16 8" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + person(610, 184, s=0.5, face=EYES, **OPERATOR) + label(610, 250, "⟦하나씩 꺼내는 사람|one-at-a-time picker⟧", 11, "var(--muted)")
         + label(380, 280, "⟦보내는 사람과 받는 사람 사이에 바구니가 있어요|a basket sits between the sender and the receiver⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 너무 길어지면 늦어지고, 놓치면 사라져요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + label(380, 55, "⟦바구니가 너무 길어졌어요|the basket got too long⟧", 13, "var(--bad)", cls="d")
         + basket(380, 245, 1.1, n=7)
         + person(620, 183, s=0.55, face=FROWN, **MECHANIC) + bubble(500, 115, 230, 40, "⟦오래된 주문이 너무 늦어요|the old orders are way too late⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦너무 길어지면 오래된 주문이 늦어지고, 꺼내다 놓치면 영영 사라져요|too long delays old orders, and dropping one loses it forever⟧", 12, "var(--ink)"))

ASYNC_I = icon('<path d="M6 22 h24" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M24 14 l8 8 l-8 8" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 42 h24" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M52 34 l8 8 l-8 8" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
ORDER_I = icon('<rect x="14" y="10" width="36" height="12" rx="2" fill="var(--accent)"/><text x="32" y="19" font-size="10" font-weight="700" text-anchor="middle" fill="#FFF8E7">1</text><rect x="14" y="26" width="36" height="12" rx="2" fill="var(--stone)"/><text x="32" y="35" font-size="10" font-weight="700" text-anchor="middle" fill="#142033">2</text><rect x="14" y="42" width="36" height="12" rx="2" fill="var(--stone)"/><text x="32" y="51" font-size="10" font-weight="700" text-anchor="middle" fill="#142033">3</text>')
NOBOOM_I = icon('<path d="M18 50 L14 20 Q32 8 50 20 L46 50Z" fill="none" stroke="#5A3B22" stroke-width="4"/><path d="M20 50 Q32 58 44 50" stroke="#5A3B22" stroke-width="3" fill="none"/><path d="M26 16 v10 M38 16 v10" stroke="#5A3B22" stroke-width="3" stroke-linecap="round"/><path d="M20 42 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
STAFF_I = icon('<circle cx="22" cy="20" r="9" fill="var(--stone-dark)"/><rect x="10" y="30" width="24" height="24" rx="8" fill="var(--stone-dark)"/><circle cx="46" cy="24" r="8" fill="var(--good)"/><path d="M46 14 v8 M42 18 h8" stroke="#FFF8E7" stroke-width="3" stroke-linecap="round"/><rect x="38" y="36" width="18" height="18" rx="6" fill="var(--good)"/>')

PAGE = {
    "slug": "messagequeue", "order": 23,
    "title": ("주문서를 쌓아두는 바구니", "The Basket That Holds the Order Slips"),
    "h1": ("<em>메시지 큐</em>가 뭐예요?", "What is a <em>Message Queue</em>?"),
    "sub": ("메시지 큐를, 주문서를 바로 넘기지 않고 바구니에 쌓아두는 간식 창구 이야기로 풀어봤어요.",
            "A message queue, told as a story about a snack counter that stacks order slips in a basket instead of handing them straight over."),
    "panels": [
        {"svg": P1, "alt": ("간식 창구에 손님 여섯 명이 한꺼번에 몰리고 직원이 땀을 흘리며 쩔쩔맴", "Six guests crowd the snack counter at once while the clerk sweats, overwhelmed"),
         "caption": ("주문이 한꺼번에 몰려 직원이 손님을 놓쳐요.", "Orders pile up all at once and the clerk can't keep up."),
         "small": ("한 번에 너무 많아요!", "Too many at once!")},
        {"svg": P2, "alt": ("손님은 주문을 아직 못 받는다고 묻고, 직원은 손도 못 댄다고 답함", "A guest asks why they still can't order, and the clerk says they can't even get to it"),
         "caption": ("왜: 받는 쪽이 바쁘면 보내는 쪽도 기다려야 해서 둘 다 느려져요.", "Why: if the sender must wait while the receiver is busy, both slow down."),
         "small": ("받는 쪽과 보내는 쪽이 서로의 속도에 묶여요.", "The sender and receiver get tied to each other's pace.")},
        {"svg": P3, "hero": True, "alt": ("줄 선 손님들이 바구니에 주문서를 넣고, 처리하는 사람이 자기 속도로 하나씩 꺼냄", "Guests in line put order slips into a basket, and the handler pulls them out one at a time, at their own pace"),
         "caption": ("주문서를 바구니에 쌓아두면, 보내는 쪽과 받는 쪽이 각자 속도대로 움직여요.", "Put orders in a basket, and sender and receiver each move at their own pace."),
         "small": ("보내는 쪽은 바로 다음 손님을, 받는 쪽은 자기 속도대로.", "The sender moves to the next guest; the receiver works at its own speed."),
         "tricks": (4, [
             (ASYNC_I, ("서로 안 기다려도 돼요", "Neither side has to wait"), ("비동기 처리예요", "this is asynchronous processing"), "calm"),
             (ORDER_I, ("순서대로 쌓여요", "They stack in order"), ("넣은 순서 그대로요", "in the same order they came in")),
             (NOBOOM_I, ("밀려도 안 터져요", "A backup doesn't break it"), ("바구니만 길어져요", "the basket just gets longer"), "warm"),
             (STAFF_I, ("사람을 늘리면 더 빨리 비워요", "More workers empty it faster"), ("처리하는 사람을 늘리면요", "by adding more handlers")),
         ])},
        {"svg": P4, "alt": ("주문서 넣는 사람에서 화살표가 쌓인 주문서로, 거기서 또 화살표가 하나씩 꺼내는 사람으로 이어짐", "An arrow runs from the order placer to the queued orders, and another from there to the one-at-a-time picker"),
         "caption": ("넣는 사람 → 쌓인 주문서 → 하나씩 꺼내는 사람.", "Order placer → queued orders → one-at-a-time picker."),
         "small": ("보내는 사람과 받는 사람 사이에 바구니가 있어요.", "A basket sits between the sender and the receiver.")},
        {"svg": P5, "alt": ("바구니가 너무 높이 쌓여 넘칠 듯하고, 정비사가 오래된 주문이 늦는다고 걱정함", "The basket is piled dangerously high and a mechanic worries the old orders are too late"),
         "caption": ("너무 길어지면 오래된 주문이 늦어지고, 놓치면 사라져요.", "Too long delays old orders, and dropping one loses it forever."),
         "small": ("길이는 백프레셔로, 놓치는 건 데드레터 큐로 다뤄요.", "Length is handled with backpressure; drops with a dead-letter queue.")},
    ],
    "summary": (("<b>메시지 큐</b> = 주문서를 바로 넘기지 않고 <b>바구니에 쌓아두어</b>, 보내는 쪽과 받는 쪽이 <b>각자 속도대로</b> 움직이게 하는 소품.",
                 "A <b>message queue</b>: instead of handing orders straight over, they're <b>stacked in a basket</b> so the sender and receiver can each move <b>at their own pace</b>."),
                ("보내는 쪽을 프로듀서, 받는 쪽을 컨슈머라고 불러요. 같은 바구니를 여러 손님이 함께 봐도 되고(퍼브/섭), 들어온 순서대로 나가는 게 보통이에요. 처리하는 사람을 늘리면 바구니가 더 빨리 비워져요.",
                 "The sender side is called the producer, the receiver the consumer. Multiple consumers can watch the same basket (pub/sub), and items usually come out in the order they went in. Adding more consumers empties the basket faster.")),
    "glossary": [
        ("메시지 큐", "Message Queue", ("주문서를 쌓아두는 바구니.", "The basket that holds the order slips."), ("보내는 쪽과 받는 쪽을 서로 안 기다리게 해줘요.", "It keeps the sender and receiver from having to wait on each other.")),
        ("비동기 처리", "Asynchronous Processing", ("보내고 나서 답을 바로 안 기다리는 방식.", "Sending something without waiting right away for a reply."), ("바구니가 있어서 가능해요.", "Possible because the basket sits in between.")),
        ("프로듀서/컨슈머", "Producer / Consumer", ("주문서를 넣는 사람과 꺼내는 사람.", "The one who puts orders in, and the one who takes them out."), ("서로 몰라도 바구니만 같이 보면 돼요.", "They don't need to know each other — just share the same basket.")),
        ("큐 길이", "Queue Length", ("바구니에 쌓인 주문서 수.", "How many order slips are piled in the basket."), ("너무 길어지면 오래된 주문이 늦게 처리돼요.", "Too long, and old orders get handled too late.")),
        ("퍼브/섭", "Pub/Sub", ("한 바구니를 여러 사람이 함께 보는 방식.", "Several people watching the same basket together."), ("발행-구독이라고도 불러요.", "Also called publish-subscribe.")),
        ("순서 보장", "Ordering Guarantee", ("넣은 순서대로 나온다는 약속.", "The promise that things come out in the order they went in."), ("모든 큐가 이걸 약속하진 않아요.", "Not every queue promises this.")),
        ("백프레셔", "Backpressure", ("바구니가 길어지기 전에 입구를 잠깐 막는 것.", "Holding the entrance shut for a moment before the basket gets too long."), ('→ <a href="backpressure-ko.html">입구를 잠깐 막기</a>', '→ <a href="backpressure-en.html">briefly closing the entrance</a>')),
        ("데드레터 큐", "Dead-letter Queue", ("꺼내다 계속 실패하는 주문서를 따로 빼 두는 함.", "A separate box for order slips that keep failing to be handled."), ('→ <a href="deadletterqueue-ko.html">아무도 안 찾아간 바구니함</a>', '→ <a href="deadletterqueue-en.html">the basket nobody came to claim</a>')),
    ],
}
