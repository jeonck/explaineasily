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


def dlqbox(x, y, s=1.0, label_text=None):
    """안 찾아간 바구니함. (x,y) 는 바닥선(ground) 기준점."""
    out = (f'<g transform="translate({x},{y}) scale({s})">'
           f'<rect x="-34" y="-40" width="68" height="44" rx="4" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/>'
           f'<path d="M-34 -24 h68" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="4 3"/>')
    if label_text:
        out += label(0, -48, label_text, 11, "var(--muted)")
    return out + "</g>"


# 1. 주문서 하나가 자꾸 실패해서 계속 다시 시도만 반복해요
P1 = svg(320, sky(320)
         + label(380, 110, "⟦주문 바구니|ORDER BASKET⟧", 12, "var(--ink)", cls="d") + basket(380, 260, 1.0, n=5)
         + '<path d="M470 190 a20 20 0 1 1 -6 -14" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M468 166 l8 10 l-12 2z" fill="var(--bad)"/>'
         + label(470, 232, "⟦또 실패!|failed again!⟧", 11, "var(--bad)", cls="d")
         + person(630, 204, s=0.55, face=FROWN + SWEAT, **MECHANIC) + bubble(520, 110, 220, 40, "⟦재료 이름을 못 알아봐요|can\'t recognize the ingredient name⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦주문서 하나가 자꾸 실패해서 계속 다시 시도만 반복해요|one order keeps failing, so it just keeps getting retried⟧", 13, "var(--ink)"))

# 2. 왜: 고장난 주문서를 계속 재시도만 하면 줄 전체가 막혀요 (bad-soft)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + queueline(80, 220, 5, 0.45, 30)
         + '<path d="M300 205 a18 18 0 1 1 -5 -13" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + label(300, 250, "⟦이것만 자꾸 걸려요|this one keeps jamming⟧", 11, "var(--bad)")
         + person(560, 178, s=0.6, face=FROWN, **MECHANIC) + bubble(460, 95, 220, 40, "⟦뒤에 다 밀렸어요|everyone behind is stuck⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦고장난 주문서를 계속 재시도만 하면 줄 전체가 막혀요|retrying a broken order forever jams the whole line⟧", 12, "var(--bad)"))

# 3. 몇 번 실패한 주문서는 따로 빼 두고, 나머지는 계속 흐르게 해요 (hero)
P3 = svg(360, sky(360)
         + label(170, 150, "⟦정상 바구니|NORMAL BASKET⟧", 12, "var(--ink)", cls="d") + basket(170, 300, 1.0, n=4)
         + '<path d="M230 230 L330 200" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/><path d="M312 196 l18 4 l-10 16" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(280, 180, "⟦×3 실패|×3 failed⟧", 11, "var(--bad)", cls="d")
         + dlqbox(430, 230, 1.3, label_text="⟦안 찾아간 함|UNCLAIMED BOX⟧")
         + person(600, 239, s=0.55, face=EYES, **OPERATOR)
         + '<path d="M560 230 q15 -15 25 -2" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + label(380, 340, "⟦몇 번 실패한 주문서는 따로 빼 두고, 나머지는 계속 흐르게 해요|an order that keeps failing gets set aside, so the rest keep flowing⟧", 13, "var(--ink)", cls="d"))

# 4. 정상 바구니 옆에 작은 안 찾아간 함, ×3 후 이동
P4 = svg(300, sky(300)
         + label(170, 110, "⟦정상 바구니|NORMAL BASKET⟧", 12, "var(--ink)", cls="d") + basket(170, 240, 0.9, n=4)
         + dlqbox(480, 240, 1.0, label_text="⟦안 찾아간 함|UNCLAIMED BOX⟧")
         + '<path d="M230 190 L450 210" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/><path d="M432 204 l18 6 l-12 14" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(340, 180, "⟦×3 재시도 후 이동|moved after ×3 retries⟧", 11, "var(--bad)")
         + label(380, 280, "⟦몇 번 더 시도해도 안 되면, 따로 빼서 사람이 보게 해요|after a few more tries, set it aside for a person to check⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 아무도 안 보면 버려지는 것과 같아요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + dlqbox(380, 220, 1.4, label_text="⟦안 찾아간 함|UNCLAIMED BOX⟧")
         + person(560, 178, s=0.55, face=FROWN, **MANAGER) + bubble(460, 100, 220, 40, "⟦아무도 안 보면 버린 거나 같아요|if no one checks, it\'s as good as thrown away⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦빼둔 함을 아무도 안 보면 버려지는 것과 같아요 — 정기적으로 확인해야 해요|an unclaimed box nobody checks is as good as discarded⟧", 12, "var(--ink)"))

RETRY_I = icon('<path d="M44 16 a18 18 0 1 0 6 14" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M44 6 v12 h-12" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="32" y="44" font-size="13" font-weight="700" text-anchor="middle" fill="var(--ink)">×3</text>')
MOVE_I = icon('<rect x="8" y="24" width="22" height="18" rx="2" fill="var(--stone)"/><rect x="34" y="14" width="22" height="18" rx="2" fill="var(--bad)"/><path d="M30 30 L40 22" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M36 20 l4 2 l-2 4" stroke="var(--bad)" stroke-width="3" fill="none"/>')
PERSON_I = icon('<circle cx="22" cy="20" r="9" fill="var(--stone-dark)"/><rect x="10" y="30" width="24" height="24" rx="8" fill="var(--stone-dark)"/><rect x="40" y="26" width="18" height="18" rx="2" fill="var(--bad)" stroke="#7A1F17" stroke-width="2"/><path d="M34 34 L40 34" stroke="var(--muted)" stroke-width="3"/>')
NOTE2_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "deadletterqueue", "order": 24,
    "title": ("아무도 안 찾아간 바구니함", "The Basket Nobody Came to Claim"),
    "h1": ("<em>데드레터 큐</em>가 뭐예요?", "What is a <em>Dead-letter Queue</em>?"),
    "sub": ("데드레터 큐를, 자꾸 실패하는 주문서를 따로 빼 두는 작은 함 이야기로 풀어봤어요.",
            "A dead-letter queue, told as a story about a small box set aside for orders that keep failing."),
    "panels": [
        {"svg": P1, "alt": ("주문 바구니 옆에서 주문서 하나가 재시도 화살표에 갇혀 계속 실패하고, 정비사가 재료 이름을 못 알아본다고 말함", "Beside the order basket, one slip is stuck in a retry loop, failing again and again, while a mechanic says it can't recognize the ingredient name"),
         "caption": ("주문서 하나가 자꾸 실패해서 계속 다시 시도만 반복해요.", "One order keeps failing, so it just keeps getting retried."),
         "small": ("재료 이름을 못 알아봐요.", "It can't recognize the ingredient name.")},
        {"svg": P2, "alt": ("줄 선 손님들 앞에서 재시도 화살표만 계속 도는 주문서 때문에 뒤에 다 밀림", "A line of guests is stuck because one order just keeps looping through retries ahead of them"),
         "caption": ("왜: 고장난 주문서를 계속 재시도만 하면 줄 전체가 막혀요.", "Why: retrying a broken order forever jams the whole line."),
         "small": ("뒤에 다 밀렸어요.", "Everyone behind is stuck.")},
        {"svg": P3, "hero": True, "alt": ("정상 바구니 옆에 작은 안 찾아간 함이 있고, ×3 실패한 주문서가 화살표를 따라 그 함으로 옮겨감", "Beside the normal basket sits a small unclaimed box; an order that failed ×3 moves there along an arrow"),
         "caption": ("몇 번 실패한 주문서는 따로 빼 두고, 나머지는 계속 흐르게 해요.", "An order that keeps failing gets set aside, so the rest keep flowing."),
         "small": ("빼둔 건 사람이 나중에 봐요.", "The set-aside ones get checked by a person later."),
         "tricks": (4, [
             (RETRY_I, ("몇 번까지 다시 시도할지 정해요", "Decide how many retries to allow"), ("한도를 미리 정해둬요", "set a limit in advance"), "calm"),
             (MOVE_I, ("넘으면 따로 빼요", "Past that limit, set it aside"), ("나머지 줄은 안 막혀요", "the rest of the line keeps moving")),
             (PERSON_I, ("빼둔 건 사람이 나중에 봐요", "A person checks it later"), ("자동으로 버려지지 않아요", "it isn't just discarded automatically"), "warm"),
             (NOTE2_I, ("왜 실패했는지 적어둬요", "Write down why it failed"), ("다음에 고치기 쉬워져요", "makes it easier to fix next time")),
         ])},
        {"svg": P4, "alt": ("정상 바구니 옆에 작은 상자, ×3 재시도 후 이동한다는 점선 화살표", "A small box beside the normal basket, with a dashed arrow labeled 'moved after ×3 retries'"),
         "caption": ("정상 바구니 옆에 작은 안 찾아간 함, ×3 재시도 후 이동.", "A small unclaimed box beside the normal basket — moved there after ×3 retries."),
         "small": ("몇 번 더 시도해도 안 되면, 따로 빼서 사람이 보게 해요.", "After a few more tries, it's set aside for a person to check.")},
        {"svg": P5, "alt": ("안 찾아간 함 옆에서 공원장이 아무도 안 보면 버린 거나 같다고 말함", "Beside the unclaimed box, the park manager says if no one checks it, it's as good as thrown away"),
         "caption": ("빼둔 함을 아무도 안 보면 버려지는 것과 같아요.", "An unclaimed box nobody checks is as good as discarded."),
         "small": ("누군가 정기적으로 확인해야 해요.", "Someone must check it regularly.")},
    ],
    "summary": (("<b>데드레터 큐</b> = 몇 번 다시 시도해도 안 되는 주문서를 <b>따로 빼 두는 함</b>. 나머지 줄은 <b>막히지 않고</b> 계속 흘러요.",
                 "A <b>dead-letter queue</b>: a <b>separate box</b> for orders that fail even after retries — so the rest of the line keeps <b>flowing, unblocked</b>."),
                ("재시도 횟수 상한을 정해두고, 그걸 넘은 메시지(포이즌 메시지)를 여기로 옮겨요. 빼둔 것 자체로 끝이 아니라, 알림을 연결해 사람이 보게 하고, 원인을 고친 뒤 재처리해야 해요. 다시 넣어도 안전하려면 멱등성이 필요해요.",
                 "You set a cap on retries, and move any message past that cap (a poison message) here. Setting it aside isn't the end — wire up an alert so a person sees it, fix the cause, and reprocess it. Reprocessing safely requires idempotency.")),
    "glossary": [
        ("데드레터 큐", "Dead-letter Queue", ("아무도 안 찾아간 바구니함.", "The basket nobody came to claim."), ("자꾸 실패하는 메시지를 따로 빼 두는 곳이에요.", "A separate place for messages that keep failing.")),
        ("재시도 횟수 상한", "Max Retry Count", ("몇 번까지 다시 시도할지 미리 정한 숫자.", "The number of retries decided on in advance."), ("넘으면 데드레터 큐로 옮겨요.", "Past this, the message moves to the dead-letter queue.")),
        ("메시지 큐", "Message Queue", ("주문서를 쌓아두는 바구니.", "The basket that holds order slips."), ('→ <a href="messagequeue-ko.html">주문서를 쌓아두는 바구니</a>', '→ <a href="messagequeue-en.html">the basket that holds the order slips</a>')),
        ("포이즌 메시지", "Poison Message", ("계속 실패하는 메시지.", "A message that keeps failing no matter what."), ("재시도 상한을 넘겨 데드레터 큐로 가요.", "It goes to the dead-letter queue once it exceeds the retry cap.")),
        ("알림 연결", "Alerting", ("빼둔 함에 뭔가 쌓이면 사람에게 알리는 것.", "Notifying a person when something lands in the box."), ('→ <a href="alerting-ko.html">몇 번 울려야 진짜 비상인가</a>', '→ <a href="alerting-en.html">how many rings mean a real emergency</a>')),
        ("재처리", "Reprocessing", ("원인을 고친 뒤 다시 큐에 넣는 것.", "Fixing the cause and putting the message back in the queue."), ("무작정 다시 넣으면 또 실패할 수 있어요.", "Putting it back blindly can just fail again.")),
        ("멱등성", "Idempotency", ("같은 걸 다시 넣어도 안전한 성질.", "The property that lets you safely resend the same thing."), ('재처리할 때 꼭 필요해요. → <a href="idempotency-ko.html">같은 티켓으로 두 번 못 타요</a>', 'Essential when reprocessing. → <a href="idempotency-en.html">you can\'t ride twice on the same ticket</a>')),
        ("관측", "Observability", ("바구니와 함 안을 들여다보는 능력.", "The ability to look inside the baskets and boxes."), ('→ <a href="observability-ko.html">세 가지로 들여다보기</a>', '→ <a href="observability-en.html">looking in through three kinds of signals</a>')),
    ],
}
