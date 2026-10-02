from _draw import *
from _world import *

# 1. 손님이 결제 버튼을 두 번 눌러요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(240, 163, s=0.6, face=SWEAT, hat=None, shirt="#4A5A72")
         + bubble(110, 80, 200, 46, "⟦어? 안 눌렸나... 또!|huh, didn't it go? again!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + booth(440, 230, 1.0, label_text="⟦결제|PAY⟧")
         + ticket(560, 170, 0.8, text="⟦20,000원|20,000⟧") + ticket(600, 200, 0.8, text="⟦20,000원|20,000⟧")
         + label(600, 250, "⟦돈이 두 번 나갔어요|money left twice⟧", 11, "var(--bad)")
         + label(380, 282, "⟦결제가 멈칫해서 손님이 '결제하기'를 두 번 눌러요|the payment stalls, so the guest taps 'pay' twice⟧", 12, "var(--ink)"))

# 2. 왜: 같은 요청을 또 보내면 처음 보는 요청인 줄 알아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(380, 230, 1.1, label_text="⟦결제|PAY⟧")
         + person(280, 163, s=0.6, face=EYES, **MECHANIC)
         + bubble(90, 80, 230, 50, "⟦어, 또 왔네 — 처음 보는 요청이구나!|oh, another one — never seen this before!⟧", 11, "var(--panel)", "var(--line)", "right")
         + ticket(540, 160, 0.9, text="⟦요청 A|request A⟧") + ticket(540, 220, 0.9, text="⟦요청 A|request A⟧")
         + label(540, 262, "⟦둘 다 결제 처리됨|both get charged⟧", 11, "var(--bad)")
         + label(380, 284, "⟦같은 요청이 또 오면, 처음 보는 요청인 줄 알고 또 처리해요|a repeated request looks brand-new, so it gets processed again⟧", 12, "var(--ink)"))

# 3. hero: 티켓마다 고유 번호 — 같은 번호는 한 번만 인정해요
P3 = svg(340, sky(340)
         + booth(380, 270, 1.1, label_text="⟦결제|PAY⟧")
         + ticket(230, 170, 1.0, text="⟦No.482|No.482⟧")
         + '<path d="M260 190 L350 240" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ticket(230, 230, 1.0, text="⟦No.482|No.482⟧")
         + '<path d="M260 250 L350 260" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="6 4"/>'
         + bubble(460, 180, 220, 50, "⟦No.482? 이미 처리했어요, 한 번만요!|No.482? already done — only once!⟧", 11, "var(--panel)", "var(--line)", "left")
         + person(560, 240, s=0.65, face=SMILE, **OPERATOR)
         + label(380, 40, "⟦같은 번호 티켓이 또 오면, '이미 처리했어요' 하고 한 번만 인정해요|the same ticket number shows up again — count it just once⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦티켓마다 고유 번호를 붙이면, 두 번 보내도 결과는 한 번이에요|give every ticket a number, and sending it twice still means one result⟧", 12, "var(--muted)"))

# 4. 번호 있음 vs 번호 없음 비교
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + board(50, 30, 280, 110, "⟦번호 있음|WITH A NUMBER⟧", ("⟦No.482가 두 번 와도|No.482 arrives twice⟧", "⟦→ 결제는 한 번|-> charged once⟧"), 1.0)
         + ticket(190, 200, 1.0, text="⟦No.482|No.482⟧") + label(190, 250, "⟦한 번만 결제|charged once⟧", 12, "var(--good)", cls="d")
         + board(430, 30, 280, 110, "⟦번호 없음|NO NUMBER⟧", ("⟦요청이 두 번 오면|a request arrives twice⟧", "⟦→ 결제도 두 번|-> charged twice⟧"), 1.0)
         + ticket(530, 190, 0.8, text="⟦?|?⟧") + ticket(610, 220, 0.8, text="⟦?|?⟧") + label(570, 270, "⟦두 번 결제|charged twice⟧", 12, "var(--bad)", cls="d")
         + label(380, 300, "⟦번호 없는 요청은 위험해요|a request with no number is risky⟧", 11, "var(--ink)"))

# 5. 깨지는 곳: 번호를 저장해 두는 것도 자원이 들어요
P5 = svg(300, sky(300)
         + board(260, 30, 240, 150, "⟦번호 저장 창고|NUMBER STORAGE⟧", ("⟦No.481, 482, 483...|No.481, 482, 483...⟧", "⟦영원히는 못 저장해요|can't keep them forever⟧", "⟦유효기간이 필요해요|needs an expiry⟧"), 1.0)
         + person(170, 174, s=0.6, face=SWEAT, **OPERATOR)
         + ride(600, 260, 0.7, color="#5B8DEF")
         + label(380, 285, "⟦저장도 자원이 들고, 재시도와 짝을 이뤄요|storing numbers costs resources too, and it pairs with retrying after a wait⟧", 12, "var(--ink)"))

TAG_I = icon('<rect x="10" y="20" width="36" height="24" rx="4" fill="var(--accent)"/><circle cx="18" cy="32" r="4" fill="var(--panel)"/><path d="M46 24 l10 8 -10 8z" fill="var(--accent)"/>')
ONCE_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="var(--good)"/><path d="M22 32 l7 7 15 -15" stroke="var(--panel)" stroke-width="5" fill="none" stroke-linecap="round"/>')
SAFE_I = icon('<path d="M32 8 L54 18 V34 C54 48 44 58 32 62 C20 58 10 48 10 34 V18 Z" fill="var(--good)"/><path d="M24 32 l6 6 12 -12" stroke="var(--panel)" stroke-width="5" fill="none" stroke-linecap="round"/>')
WARN_I = icon('<path d="M32 10 L58 54 H6 Z" fill="var(--bad)"/><rect x="29" y="26" width="6" height="14" fill="var(--panel)"/><circle cx="32" cy="46" r="3.5" fill="var(--panel)"/>')

PAGE = {
    "slug": "idempotency", "order": 29,
    "title": ("같은 티켓으로 두 번 못 타요", "You Can't Ride Twice on the Same Ticket"),
    "h1": ("<em>멱등성</em>이 뭐예요?", "What is <em>Idempotency</em>?"),
    "sub": ("멱등성을 같은 번호의 티켓은 한 번만 인정해 주는 매표 창구 이야기로 풀어봤어요.",
            "Idempotency, told as a story about a ticket booth that only honors a numbered ticket once."),
    "panels": [
        {"svg": P1, "alt": ("손님이 결제가 안 된 줄 알고 결제 버튼을 두 번 눌러, 돈이 두 번 나감", "A guest thinks payment failed and taps pay twice, so money leaves twice"),
         "caption": ("결제가 멈칫해서 손님이 버튼을 두 번 눌러요.", "The payment stalls, so the guest taps the button twice."),
         "small": ("걱정돼서 한 번 더 누른 것뿐인데, 돈은 두 번 나가요.", "Just a worried extra tap — but the money leaves twice.")},
        {"svg": P2, "alt": ("정비사가 두 번째 요청을 '처음 보는 요청'이라 여겨 또 처리하고, 티켓 두 장 모두 결제됨", "A mechanic treats the second request as brand-new and processes it again; both tickets get charged"),
         "caption": ("같은 요청이 또 오면, 처음 보는 요청인 줄 알고 또 처리해요.", "A repeated request looks brand-new, so it gets processed again."),
         "small": ("번호가 없으면 구분할 방법이 없어요.", "Without a number, there's no way to tell them apart.")},
        {"svg": P3, "hero": True, "alt": ("같은 번호 482번 티켓이 창구에 두 번 들어가지만, 두 번째는 '이미 처리했어요'라는 대답만 돌아옴", "Ticket No.482 arrives at the booth twice, but the second time the booth just says 'already done'"),
         "caption": ("같은 번호 티켓이 또 오면 — '이미 처리했어요' 하고 한 번만 인정해요.", "The same ticket number shows up again — count it just once."),
         "small": ("번호 덕분에, 두 번 보내도 결과는 한 번이에요.", "Thanks to the number, sending it twice still means one result."),
         "tricks": (4, [
             (TAG_I, ("요청마다 번호를 붙여요", "Give each request a number"), ("고유한 번호예요", "a unique one"), "calm"),
             (ONCE_I, ("같은 번호는 한 번만", "Same number, counted once"), ("처리는 한 번뿐이에요", "it's processed only once")),
             (SAFE_I, ("두 번 보내도 안전해요", "Safe to send twice"), ("이게 멱등이에요", "that's idempotency"), "warm"),
             (WARN_I, ("번호 없는 요청은 위험", "No number means risk"), ("몇 번 받았는지 몰라요", "no way to know how many times")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 번호가 있으면 같은 번호 티켓이 두 번 와도 한 번만 결제. 오른쪽: 번호가 없으면 요청이 두 번 오면 결제도 두 번", "Left: with a number, the same ticket twice means one charge. Right: without a number, two arrivals mean two charges"),
         "caption": ("번호가 있고 없고의 차이예요.", "This is the difference a number makes."),
         "small": ("번호가 있으면 안전하고, 없으면 그대로 두 번 처리돼요.", "With a number it's safe; without one, it just happens twice.")},
        {"svg": P5, "alt": ("관제실 요원이 번호 저장 창고를 보며 땀을 흘림 — 창고는 영원히 못 채우고 유효기간이 필요함", "An operator looks worriedly at the number-storage shelf — it can't be filled forever and needs an expiry"),
         "caption": ("번호를 저장해 두는 것도 자원이 들어요.", "Storing those numbers costs resources too."),
         "small": ("영원히는 못 저장해서 유효기간을 둬요. 재시도와 늘 짝을 이뤄요.", "You can't keep them forever, so they expire — and this always pairs with retrying.")},
    ],
    "summary": (("<b>멱등성</b> = 같은 요청(<b>같은 티켓 번호</b>)이 <b>두 번 와도</b> 결과는 <b>한 번만</b> 처리되게 만드는 일.",
                 "<b>Idempotency</b> = making sure the <b>same request (same ticket number)</b> arriving <b>twice</b> still produces the result <b>only once</b>."),
                ("Idempotency. 같은 요청을 여러 번 보내도 한 번 보낸 것과 결과가 같은 성질이에요. 멱등 키(idempotent key)로 요청을 구분하고, 이미 처리한 키는 저장해 뒀다가 중복을 걸러내요. 네트워크가 끊겨 재시도할 때 특히 중요해요.",
                 "A property where sending the same request multiple times produces the same result as sending it once. An idempotent key identifies each request, and already-seen keys are stored to filter out duplicates — especially important when a dropped connection triggers a retry.")),
    "glossary": [
        ("멱등성", "Idempotency", ("두 번 보내도 결과가 같은 성질.", "The property that sending twice gives the same result."), ("한 번 보낸 것과 똑같아요.", "Same as sending it just once.")),
        ("멱등 키", "Idempotent key", ("티켓에 적힌 고유 번호.", "The unique number written on the ticket."), ("이 번호로 같은 요청인지 구분해요.", "This number is how you tell requests apart.")),
        ("중복 제거", "Deduplication", ("같은 번호 티켓을 걸러내는 일.", "Filtering out a ticket with a number you've already seen."), ("두 번째부터는 처리하지 않아요.", "The second and later copies aren't processed.")),
        ("재시도", "Retry", ("끊기면 다시 보내는 것.", "Sending the request again after it's dropped."), ("멱등성이 있어야 재시도가 안전해요.", "Retrying is only safe when the request is idempotent.")),
        ("결제 중복 방지", "Duplicate payment prevention", ("결제에서 멱등성을 쓰는 가장 흔한 예.", "The most common place idempotency shows up."), ("같은 결제 번호면 한 번만 돈을 받아요.", "The same payment number means money is taken only once.")),
        ("at-least-once / exactly-once", "At-least-once / Exactly-once", ("전달 방식 이름들.", "Names for how a message gets delivered."), ("이름만 알아둬도 충분해요 — 한 번 이상 올 수도, 딱 한 번만 올 수도 있어요.", "Just knowing the names is enough — a message may arrive more than once, or exactly once.")),
        ("자연히 멱등한 연산", "Naturally idempotent operations", ("몇 번을 해도 똑같은 연산.", "An operation that gives the same result no matter how many times you do it."), ("'최댓값을 10으로 설정' 같은 거예요 — 두 번 해도 여전히 10이에요.", "Like 'set the max to 10' — do it twice and it's still 10.")),
        ("티켓/요청 ID", "Ticket / Request ID", ("요청마다 붙는 고유 번호 그 자체.", "The unique number attached to each request."), ("멱등 키와 같은 역할을 해요.", "It plays the same role as the idempotent key.")),
    ],
}
