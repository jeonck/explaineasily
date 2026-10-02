from _draw import *
from _world import *

# 1. 손님마다 다른 창구로 직접 뛰어다님 — 혼란
P1 = svg(320, sky(320)
         + booth(120, 230, 0.85, label_text="⟦A|A⟧") + booth(380, 230, 0.85, label_text="⟦B|B⟧") + booth(640, 230, 0.85, label_text="⟦C|C⟧")
         + person(40, 174, s=0.5, face=FROWN, hat=FOLK[0][0], shirt=FOLK[0][1])
         + person(260, 174, s=0.5, face=FROWN, hat=FOLK[1][0], shirt=FOLK[1][1])
         + person(500, 174, s=0.5, face=FROWN, hat=FOLK[2][0], shirt=FOLK[2][1])
         + '<path d="M70 200 Q220 150 345 210" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + '<path d="M290 200 Q450 160 605 215" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + '<path d="M530 200 Q400 180 155 215" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + label(380, 300, "⟦손님마다 다른 창구로 직접 뛰어다녀요|every guest runs to a different booth on their own⟧", 12, "var(--ink)", cls="d"))

# 2. 왜 어려운가 — 창구가 12개면 손님은 어디가 어딘지 몰라요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + booth(70, 100, 0.5, label_text="1") + booth(180, 100, 0.5, label_text="2") + booth(290, 100, 0.5, label_text="3")
         + booth(400, 100, 0.5, label_text="4") + booth(510, 100, 0.5, label_text="5") + booth(620, 100, 0.5, label_text="6")
         + booth(70, 220, 0.5, label_text="7") + booth(180, 220, 0.5, label_text="8") + booth(290, 220, 0.5, label_text="9")
         + booth(400, 220, 0.5, label_text="10") + booth(510, 220, 0.5, label_text="11") + booth(620, 220, 0.5, label_text="12")
         + person(690, 150, s=0.45, face=FROWN + SWEAT, hat=FOLK[1][0], shirt=FOLK[1][1])
         + label(380, 300, "⟦기구도 12개, 창구도 12개 — 어디가 어딘지 몰라요|12 rides, 12 booths — no way to tell which is which⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 안내소 하나가 다 받아서 알맞은 창구로 보내줘요
GATE_I = icon('<rect x="16" y="18" width="32" height="36" rx="3" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 V54" stroke="var(--accent)" stroke-width="3"/><circle cx="26" cy="36" r="2.5" fill="var(--accent)"/>')
ID_I = icon('<rect x="12" y="16" width="40" height="28" rx="4" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="24" cy="30" r="5" fill="var(--accent)"/><path d="M34 26 h10 M34 33 h10" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
ROUTE_I = icon('<circle cx="32" cy="18" r="6" fill="var(--good)"/><path d="M32 24 V32" stroke="var(--good)" stroke-width="4"/><path d="M32 32 L16 48 M32 32 L48 48" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
STOP_I = icon('<circle cx="32" cy="32" r="20" fill="var(--bad)"/><rect x="20" y="29" width="24" height="6" fill="#FFF8E7"/>')

P3 = svg(340, sky(340)
         + gatehouse(150, 130, 1.0)
         + person(40, 158, s=0.55, face=EYES, **OPERATOR)
         + person(230, 168, s=0.5, face=SMILE, hat=FOLK[3][0], shirt=FOLK[3][1])
         + booth(560, 230, 0.8, label_text="⟦A|A⟧")
         + '<path d="M235 190 Q400 150 540 210" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + label(380, 25, "⟦안내소 하나가 다 받아서 알맞은 창구로 보내줘요|one booth takes everyone and sends them to the right window⟧", 13, "var(--ink)", cls="d")
         + label(380, 328, "⟦입구 하나, 신분증 확인 한 번, 길 안내까지 한 번에요|one entrance, one ID check, one set of directions⟧", 12, "var(--muted)"))

# 4. 안내소 하나 → 기구 A/B/C 로 화살표 분기
P4 = svg(300, sky(300, ground=False)
         + gatehouse(80, 120, 1.0)
         + ride(430, 230, 0.55, color="var(--accent)", label_text="⟦기구 A|Ride A⟧") + ride(560, 230, 0.55, color="#5B8DEF", label_text="⟦기구 B|Ride B⟧") + ride(690, 230, 0.55, color="#2E7D6B", label_text="⟦기구 C|Ride C⟧")
         + '<path d="M175 175 Q300 110 390 185" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + '<path d="M175 175 Q350 175 515 200" stroke="#5B8DEF" stroke-width="3" fill="none"/>'
         + '<path d="M175 175 Q400 250 645 208" stroke="#2E7D6B" stroke-width="3" fill="none"/>'
         + label(380, 282, "⟦들어오는 문은 하나, 나가는 길은 여럿이에요|one door in, many paths out⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 안내소가 고장나면 공원 전체가 못 들어가요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + gatehouse(330, 150, 1.1)
         + '<path d="M297 179 L363 212 M363 179 L297 212" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + queueline(40, 206, 5, 0.45, 30) + label(190, 262, "⟦못 들어가요|can't get in⟧", 11, "var(--bad)")
         + ride(600, 230, 0.5, color="var(--stone)") + ride(690, 230, 0.45, color="var(--stone)")
         + label(380, 282, "⟦안내소 하나가 고장나면 공원 전체가 막혀요|if the one booth breaks, the whole park locks up⟧", 12, "var(--bad)", cls="d"))

PAGE = {
    "slug": "apigateway", "order": 7,
    "title": ("정문 안내소", "The Front Gate Information Booth"),
    "h1": ("<em>API 게이트웨이</em>가 뭐예요?", "What is an <em>API Gateway</em>?"),
    "sub": ("API 게이트웨이를 손님을 받아 알맞은 창구로 보내는 정문 안내소 이야기로 풀어봤어요.",
            "An API gateway, told as a story about the front gate booth that sends every guest to the right window."),
    "panels": [
        {"svg": P1, "alt": ("손님 셋이 각자 다른 창구를 찾아 어지럽게 뛰어다님", "Three guests each run off in confused directions looking for the right booth"),
         "caption": ("손님마다 다른 창구로 직접 뛰어다녀요.", "Every guest runs to a different booth on their own."),
         "small": ("어디로 가야 할지 몰라 공원 안을 헤매요.", "Not knowing where to go, they wander the whole park.")},
        {"svg": P2, "alt": ("창구 열두 개가 번호만 붙어 늘어서 있고, 손님이 땀을 흘리며 어디가 어딘지 몰라함", "Twelve numbered booths in a row; a guest sweats, unable to tell which is which"),
         "caption": ("기구도 12개, 창구도 12개 — 어디가 어딘지 몰라요.", "12 rides, 12 booths — no way to tell which is which."),
         "small": ("창구가 많아질수록 손님이 직접 찾기는 더 어려워져요.", "The more booths there are, the harder it is to find the right one alone.")},
        {"svg": P3, "hero": True, "alt": ("정문 안내소 요원이 손님의 신분증을 확인하고, 화살표가 기구 A 창구로 이어짐", "The gate operator checks a guest's ID; an arrow leads on to booth A"),
         "caption": ("안내소 하나가 다 받아서 알맞은 창구로 보내줘요.", "One booth takes everyone and sends them to the right window."),
         "small": ("입구 하나, 신분증 확인 한 번, 길 안내까지 한 번에요.", "One entrance, one ID check, one set of directions."),
         "tricks": (4, [
             (GATE_I, ("입구는 하나로", "One entrance"), ("다 여기로 들어와요", "everyone comes through here"), "calm"),
             (ID_I, ("신분증 확인은 한 번만", "Check ID once"), ("창구마다 또 안 물어요", "booths don't ask again")),
             (ROUTE_I, ("어디로 갈지 안내소가 정해요", "The booth routes you"), ("길을 몰라도 돼요", "no need to know the way"), "warm"),
             (STOP_I, ("너무 몰리면 먼저 막아요", "Throttles when crowded"), ("안내소가 먼저 알아채요", "it notices the crowd first")),
         ])},
        {"svg": P4, "alt": ("안내소 하나에서 세 갈래 화살표가 기구 A, B, C로 각각 이어짐", "From one booth, three arrows branch out to rides A, B, and C"),
         "caption": ("들어오는 문은 하나, 나가는 길은 여럿이에요.", "One door in, many paths out."),
         "small": ("안내소가 손님을 보고 어느 기구로 보낼지 정해요.", "The booth looks at each guest and decides which ride to send them to.")},
        {"svg": P5, "alt": ("안내소가 멈춰 있고 손님 줄이 밖에 길게 늘어서 못 들어감", "The booth is stalled and a long line of guests can't get in"),
         "caption": ("안내소 하나가 고장나면 공원 전체가 막혀요.", "If the one booth breaks, the whole park locks up."),
         "small": ("그래서 안내소도 여러 개 두고 나눠 맡겨요.", "So parks keep more than one booth and split the load between them.")},
    ],
    "summary": (("<b>API 게이트웨이</b> = 손님을 받아 <b>신분증을 확인하고, 길을 안내하고, 너무 몰리면 막는</b> 정문 안내소 하나.",
                 "An <b>API gateway</b> = one front booth that <b>checks ID, shows the way, and throttles the crowd</b> for every guest."),
                ("요청이 들어오는 단일 진입점(single entry point)으로, 인증(authentication)·인가(authorization)·라우팅(routing)·속도 제한(rate limiting)을 한곳에서 처리해요. 안쪽 창구마다 따로 구현할 걸 안내소 하나가 대신 맡는 셈이에요.",
                 "A single entry point for incoming requests that handles authentication, authorization, routing, and rate limiting in one place — instead of every backend service implementing it separately.")),
    "glossary": [
        ("API 게이트웨이", "API gateway", ("정문 안내소.", "The front gate booth."), ("모든 요청이 여기를 한 번 거쳐요.", "Every request passes through here first.")),
        ("인증", "Authentication", ("신분증을 보여주는 일.", "Showing your ID."), ("누구인지 확인해요.", "Confirms who you are.")),
        ("인가", "Authorization", ("들어갈 자격이 있는지 보는 일.", "Checking you're allowed in."), ("누구인지 안 다음, 뭘 할 수 있는지 봐요.", "After knowing who you are, it checks what you're allowed to do.")),
        ("라우팅", "Routing", ("안내소가 길을 알려주는 일.", "The booth pointing the way."), ("손님 요청을 알맞은 창구로 보내요.", "Sends each request to the right backend window.")),
        ("속도 제한", "Rate limiting", ("한 번에 몇 명까지만 들여보내는 일.", "Letting in only so many at a time."), ('너무 몰리면 안내소가 먼저 막아요. → <a href="caching-ko.html">자주 묻는 질문 미리 적어둔 메모판</a>', 'The booth throttles before things get overwhelmed. → <a href="caching-en.html">the memo board of frequent answers</a>')),
        ("단일 진입점", "Single entry point", ("들어오는 문은 하나뿐.", "There's only one door in."), ("그래서 거기가 고장나면 다 같이 못 들어가요.", "Which means if that one door breaks, nobody gets in.")),
        ("로드 밸런서", "Load balancer", ("안내소를 여러 개 두고 나눠 맡기는 장치.", "The device that splits guests across several booths."), ('안내소 하나로는 부족할 때 써요. → <a href="loadbalancer-ko.html">여러 창구로 나누는 교통 정리</a>', 'Used when one booth isn\'t enough. → <a href="loadbalancer-en.html">the traffic officer who splits the queue</a>')),
        ("서비스 메시", "Service mesh", ("기구들끼리 이야기하는 전용 통로.", "The dedicated path rides use to talk to each other."), ('안내소는 손님과 기구 사이, 서비스 메시는 기구와 기구 사이예요. → <a href="servicemesh-ko.html">기구 사이 전용 통로</a>', 'The gateway sits between guests and rides; a service mesh sits between rides themselves. → <a href="servicemesh-en.html">the dedicated path between rides</a>')),
    ],
}
