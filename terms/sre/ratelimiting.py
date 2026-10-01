from _draw import *
from _world import *

# 1. 한 손님이 쉬지 않고 요청을 보내요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + queueline(60, 174, 3, 0.5, 30) + label(140, 250, "⟦기다리는 손님들|guests waiting⟧", 11, "var(--ink)")
         + person(340, 163, s=0.6, face=EYES, hat=None, shirt="#C9822B")
         + bubble(220, 80, 220, 46, "⟦또! 또! 또! 또!|again! again! again!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + booth(500, 230, 1.0, label_text="⟦창구|BOOTH⟧")
         + label(380, 282, "⟦한 손님이 쉬지 않고 요청을 보내, 다른 손님이 못 들어와요|one guest keeps sending requests nonstop, so others can't get in⟧", 12, "var(--ink)"))

# 2. 왜: 막는 규칙이 없으면 한 명이 창구를 독차지해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(380, 230, 1.0, label_text="⟦창구|BOOTH⟧")
         + person(300, 163, s=0.6, face=EYES, hat=None, shirt="#C9822B")
         + '<path d="M330 150 L365 185" stroke="var(--bad)" stroke-width="2"/><path d="M330 170 L365 200" stroke="var(--bad)" stroke-width="2"/><path d="M330 190 L365 215" stroke="var(--bad)" stroke-width="2"/>'
         + person(560, 163, s=0.6, face=SWEAT, **OPERATOR) + bubble(500, 80, 230, 50, "⟦규칙이 없으면 막을 방법이 없어요|with no rule, there's no way to stop it⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 284, "⟦막는 규칙이 없으면 한 명이 창구 전체를 독차지할 수 있어요|with no limiting rule, one guest can hog the whole booth⟧", 12, "var(--ink)"))

# 3. hero: 1분에 몇 번까지 정해서, 넘으면 잠깐 기다리게 해요
P3 = svg(340, sky(340)
         + board(290, 130, 180, 50, "⟦규칙|RULE⟧", ("⟦1분에 5번까지|5 per minute⟧",), 1.0)
         + booth(380, 270, 1.1, label_text="⟦창구|BOOTH⟧")
         + person(170, 214, s=0.5, face=FROWN, hat=None, shirt="#C9822B") + bubble(70, 150, 180, 46, "⟦6번째... 조금만 기다려요|6th time... wait a bit⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + queueline(520, 214, 3, 0.5, 28)
         + label(380, 40, "⟦창구마다 '한 사람당 1분에 몇 번까지'를 정해서, 넘으면 잠깐 기다리게 해요|each booth sets 'this many per person per minute' — go over, and you wait a bit⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦한도를 정하면, 한 사람이 전부를 차지하지 못해요|with a limit set, no single guest can take it all⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 토큰(코인) 양동이
BUCKET = ('<path d="M240 130 h80 l-10 70 h-60 z" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
          + "".join(f'<circle cx="{258 + (i % 3) * 16}" cy="{182 - (i // 3) * 16}" r="8" fill="var(--accent)" stroke="#C9822B" stroke-width="2"/>' for i in range(5))
          + '<path d="M278 95 q6 10 0 18 q-6 -8 0 -18z" fill="#5B9BD5"/>')
P4 = svg(320, sky(320)
         + BUCKET + label(280, 70, "⟦토큰 버킷|TOKEN BUCKET⟧", 12, "var(--ink)", cls="d")
         + label(280, 235, "⟦코인 5개, 천천히 다시 채워져요|5 coins, slowly refilling⟧", 11, "var(--muted)")
         + booth(600, 260, 0.9, label_text="⟦창구|BOOTH⟧")
         + '<path d="M330 170 L560 230" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(450, 170, "⟦요청마다 코인 하나씩|one coin per request⟧", 11, "var(--ink)")
         + label(380, 295, "⟦코인이 떨어지면 잠깐 기다려요|run out of coins, and you wait a bit⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 우리 시스템을 보호하는 것 — 나쁜 손님을 가리는 것과는 달라요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + booth(190, 230, 1.0, label_text="⟦창구|BOOTH⟧") + label(190, 270, "⟦속도 제한 = 우리 시스템 보호|rate limiting = protecting our own system⟧", 11, "var(--ink)")
         + person(560, 163, s=0.6, face=MASK, hat=None, shirt="#111C30")
         + label(560, 270, "⟦DDoS 방어·WAF = 나쁜 손님을 가려 막기|DDoS defense and WAF = telling bad guests apart⟧", 11, "var(--ink)")
         + label(380, 50, "⟦둘은 달라요|these are two different jobs⟧", 13, "var(--ink)", cls="d"))

LIMIT_I = icon('<circle cx="24" cy="24" r="14" fill="var(--panel)" stroke="var(--accent)" stroke-width="4"/><circle cx="24" cy="24" r="4" fill="var(--accent)"/><rect x="10" y="40" width="44" height="14" rx="4" fill="var(--accent)"/>')
STOP_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)"/><rect x="18" y="29" width="28" height="6" fill="var(--panel)"/>')
BUCKET_I = icon('<path d="M18 20 h28 l-5 30 h-18z" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><circle cx="28" cy="34" r="5" fill="var(--accent)"/><circle cx="38" cy="38" r="5" fill="var(--accent)"/>')
COUNT_I = icon('<rect x="10" y="18" width="44" height="28" rx="5" fill="#1B2A44"/>' + label(32, 38, "3/5", 16, "var(--good)", cls="d"))

PAGE = {
    "slug": "ratelimiting", "order": 19,
    "title": ("한 번에 몇 명까지만", "Only So Many at a Time"),
    "h1": ("<em>속도 제한</em>이 뭐예요?", "What is <em>Rate Limiting</em>?"),
    "sub": ("속도 제한을 한 사람당 1분에 몇 번까지만 받아주는 창구 이야기로 풀어봤어요.",
            "Rate limiting, told as a story about a booth that only takes so many requests per person per minute."),
    "panels": [
        {"svg": P1, "alt": ("한 손님이 창구에 쉬지 않고 요청을 보내고, 다른 손님들은 줄을 서서 기다림", "One guest keeps sending requests to the booth nonstop while other guests wait in line"),
         "caption": ("한 손님이 쉬지 않고 요청을 보내, 다른 손님이 못 들어와요.", "One guest keeps sending requests nonstop, so others can't get in."),
         "small": ("사람이든 봇이든, 혼자 창구를 다 차지할 수 있어요.", "Whether a person or a bot, one guest alone can hog the booth.")},
        {"svg": P2, "alt": ("손님이 계속 요청을 보내고, 관제실 요원이 땀을 흘리며 '규칙이 없으면 막을 방법이 없다'고 말함", "The guest keeps sending requests while a sweating operator says there's no way to stop it without a rule"),
         "caption": ("막는 규칙이 없으면 한 명이 창구 전체를 독차지할 수 있어요.", "With no limiting rule, one guest can hog the whole booth."),
         "small": ("규칙이 있어야 공평하게 나눠 써요.", "A rule is what makes sharing fair.")},
        {"svg": P3, "hero": True, "alt": ("창구 위에 '1분에 5번까지' 규칙 안내판이 붙고, 6번째로 오는 손님은 잠깐 기다리라는 안내를 받음", "A sign above the booth reads '5 per minute,' and a guest on their sixth try is asked to wait a bit"),
         "caption": ("창구마다 '한 사람당 1분에 몇 번까지'를 정해서, 넘으면 잠깐 기다리게 해요.", "Each booth sets 'this many per person per minute' — go over, and you wait a bit."),
         "small": ("한도를 정하면, 한 사람이 전부를 차지하지 못해요.", "With a limit set, no single guest can take it all."),
         "tricks": (4, [
             (LIMIT_I, ("누구에게 매길지 정해요", "Decide who the limit applies to"), ("사람별 또는 전체로요", "per person, or overall"), "calm"),
             (STOP_I, ("넘으면 거절하거나 늦춰요", "Over the limit? Refuse or delay"), ("잠깐 기다리게 해요", "it just waits a bit")),
             (BUCKET_I, ("급할 땐 살짝 여유를 둬요", "Leave a little slack for bursts"), ("버킷에 남은 만큼요", "whatever's left in the bucket"), "warm"),
             (COUNT_I, ("한도는 숫자로 보여줘요", "Show the limit as a number"), ("남은 횟수를 알려줘요", "how many requests are left")),
         ])},
        {"svg": P4, "alt": ("양동이 안에 코인 다섯 개가 있고, 요청마다 코인 하나씩 창구로 건네지며, 위에서 천천히 다시 채워짐", "A bucket holds five coins; one coin goes to the booth per request, and the bucket slowly refills from above"),
         "caption": ("이게 토큰 버킷이에요 — 요청마다 코인 하나씩 꺼내요.", "This is a token bucket — pull one coin for every request."),
         "small": ("코인이 떨어지면 다시 채워질 때까지 잠깐 기다려요.", "Run out of coins, and you wait until it refills.")},
        {"svg": P5, "alt": ("왼쪽: 속도 제한은 우리 시스템을 보호. 오른쪽: DDoS 방어와 WAF는 나쁜 손님을 가려서 막음", "Left: rate limiting protects our own system. Right: DDoS defense and a WAF tell bad guests apart and block them"),
         "caption": ("둘은 달라요.", "These are two different jobs."),
         "small": ("속도 제한은 누가 나쁜지 가리지 않고, 다 같이 적당히만 쓰게 해요.", "Rate limiting doesn't judge who's bad — it just keeps everyone's use reasonable.")},
    ],
    "summary": (("<b>속도 제한</b> = 한 사람(또는 전체)이 <b>일정 시간에 몇 번까지만</b> 쓰게 해서, 창구를 <b>다 같이</b> 쓸 수 있게 하는 일.",
                 "<b>Rate limiting</b> = letting one person (or everyone together) use the booth only <b>so many times in a given time</b>, so it stays <b>shared</b>."),
                ("Rate limiting. 사용자별·API별로 호출 횟수에 상한을 두는 기법이에요. 토큰 버킷이나 슬라이딩 윈도 같은 알고리즘으로 구현하고, 넘으면 보통 429 응답을 돌려줘요. DDoS 방어나 WAF와는 목적이 달라요 — 그쪽은 공격자를 가려내고, 속도 제한은 우리 시스템 자신을 보호해요.",
                 "A technique that caps how many calls a user or API can make. It's implemented with algorithms like a token bucket or a sliding window, and usually returns a 429 response when the limit is exceeded. Its purpose differs from DDoS defense or a WAF — those tell attackers apart, while rate limiting protects our own system.")),
    "glossary": [
        ("속도 제한", "Rate limiting", ("얼마나 자주 쓸 수 있는지 정해두는 규칙.", "A rule for how often something can be used."), ("창구마다, 사람마다 정할 수 있어요.", "It can be set per booth, per person.")),
        ("토큰 버킷", "Token bucket", ("코인이 든 양동이.", "A bucket holding coins."), ("요청마다 코인 하나씩 쓰고, 천천히 다시 채워져요.", "Each request spends one coin, and the bucket slowly refills.")),
        ("슬라이딩 윈도", "Sliding window", ("최근 일정 시간 동안만 세는 방법.", "A way of counting only the last little while."), ("이름만 알아둬도 충분해요 — 토큰 버킷과 비슷한 또 다른 방식이에요.", "Just the name is enough — another way to do the same kind of counting.")),
        ("사용자별/전체 한도", "Per-user / Global limit", ("누구에게 규칙을 매길지.", "Who the rule applies to."), ("한 사람씩 잴 수도, 창구 전체로 잴 수도 있어요.", "You can measure one guest at a time, or the whole booth together.")),
        ("429 응답", "429 response", ("'너무 많아요'라는 대답.", "The answer that means 'too many.'"), ("이름만 알아둬도 충분해요 — 한도를 넘었을 때 돌아오는 신호예요.", "Just the name is enough — the signal sent back when the limit is crossed.")),
        ("API 게이트웨이", "API gateway", ("여러 창구를 한데 모은 정문 안내소.", "A front desk that gathers many booths in one place."), ("속도 제한은 주로 여기서 걸려요.", "Rate limiting is usually applied right here.")),
        ("DDoS 방어와의 차이", "Difference from DDoS defense", ("속도 제한은 공격자를 가리지 않아요.", "Rate limiting doesn't tell attackers apart."), ("DDoS 방어·WAF는 나쁜 손님을 가려 막고, 속도 제한은 우리 시스템 자신을 보호해요.", "DDoS defense and a WAF block bad guests specifically; rate limiting just protects our own system.")),
        ("할당량", "Quota", ("더 긴 기간(하루·한 달) 동안의 한도.", "A limit over a longer stretch, like a day or a month."), ("1분당 한도보다 긴 호흡으로 정해요.", "Set over a longer breath than a per-minute limit.")),
    ],
}
