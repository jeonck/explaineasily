from _draw import *
from _world import *


def sidecar(x, y, s=1.0, color="var(--accent)"):
    """사이드카: 기구 옆에 붙는 작은 전용 통로 상자. 서비스 메시 페이지 전용 소품."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-16" width="32" height="32" rx="6" fill="{color}" stroke="var(--stone-dark)" stroke-width="2"/>'
            f'<path d="M-8 0 h16 M0 -8 v16" stroke="#FFF8E7" stroke-width="3"/></g>')


# 1. 기구끼리 서로 다른 말로 이야기하다 꼬여요
P1 = svg(320, sky(320)
         + ride(140, 260, 0.65, color="var(--accent)") + ride(390, 260, 0.65, color="#5B8DEF") + ride(630, 260, 0.6, color="#2E7D6B")
         + '<path d="M170 210 Q280 260 370 215" stroke="var(--accent)" stroke-width="2" fill="none"/>'
         + '<path d="M190 195 Q310 110 600 220" stroke="#5B8DEF" stroke-width="2" fill="none" stroke-dasharray="6 4"/>'
         + '<path d="M420 205 Q520 270 615 215" stroke="#2E7D6B" stroke-width="2" fill="none" stroke-dasharray="2 5"/>'
         + '<path d="M150 220 Q400 300 610 210" stroke="var(--bad)" stroke-width="2" fill="none"/>'
         + person(290, 210, s=0.5, face=FROWN, **MECHANIC) + bubble(250, 150, 150, 40, "⟦뭐라는 거예요?|what is it saying?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦기구끼리 서로 다른 말로 이야기하다 꼬여요|rides talk to each other in different ways, and it all tangles⟧", 12, "var(--ink)", cls="d"))

# 2. 왜 어려운가 — 기구가 많아지면 연결선이 실타래처럼 엉켜요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + ride(100, 250, 0.5, color="var(--stone)") + ride(300, 250, 0.5, color="var(--stone)") + ride(500, 250, 0.5, color="var(--stone)") + ride(680, 250, 0.45, color="var(--stone)")
         + "".join(f'<path d="M{ax} {ay} Q380 {cy} {bx} {by}" stroke="var(--bad)" stroke-width="1.5" fill="none" stroke-dasharray="{dash}"/>'
                   for (ax, ay, bx, by, cy, dash) in [
                       (100, 150, 300, 150, 60, "4 3"), (100, 150, 500, 150, 100, "2 4"), (100, 150, 680, 150, 40, "6 3"),
                       (300, 150, 500, 150, 130, "4 3"), (300, 150, 680, 150, 70, "2 4"), (500, 150, 680, 150, 110, "6 3"),
                   ])
         + label(380, 300, "⟦기구가 많아지면 연결선이 실타래처럼 엉켜요|with more rides, the wires tangle into a hairball⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 사이드카끼리만 정해진 방식으로 이야기해요
SIDECAR_I = icon('<rect x="8" y="22" width="18" height="18" rx="4" fill="var(--accent)"/><rect x="38" y="22" width="18" height="18" rx="4" fill="var(--accent)"/><path d="M26 31 h12" stroke="var(--accent)" stroke-width="3"/>')
SYNC_I = icon('<path d="M16 22 a16 16 0 1 1 -2 12" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M10 18 l4 11 -12 -2z" fill="var(--good)"/>')
LOG_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 32 h20 M22 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
REROUTE_I = icon('<path d="M10 32 h14" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/><path d="M40 32 h14" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/><path d="M26 16 Q40 32 26 48" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

P3 = svg(300, sky(300)
         + ride(150, 230, 0.65, color="var(--accent)") + sidecar(220, 202, 1.0)
         + ride(600, 230, 0.65, color="#5B8DEF") + sidecar(530, 202, 1.0, color="#5B8DEF")
         + '<path d="M236 202 L514 202" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(380, 25, "⟦기구 뒤에 똑같은 통로를 하나씩 붙이면, 통로끼리만 이야기해요|attach the same small connector behind each ride, and the connectors talk to each other⟧", 13, "var(--ink)", cls="d")
         + label(380, 288, "⟦기구 자신은 신경 안 써도 돼요|the rides themselves don't need to worry about it⟧", 12, "var(--muted)"))

# 4. 기구 3개 + 사이드카 3개 — 통로끼리 이어진 그물
P4 = svg(320, sky(320, ground=False)
         + ride(130, 260, 0.55, color="var(--accent)") + sidecar(130, 160, 0.9)
         + ride(380, 260, 0.55, color="#5B8DEF") + sidecar(380, 160, 0.9, color="#5B8DEF")
         + ride(630, 260, 0.55, color="#2E7D6B") + sidecar(630, 160, 0.9, color="#2E7D6B")
         + '<path d="M130 174 V195" stroke="var(--stone-dark)" stroke-width="2"/><path d="M380 174 V195" stroke="var(--stone-dark)" stroke-width="2"/><path d="M630 174 V195" stroke="var(--stone-dark)" stroke-width="2"/>'
         + '<path d="M146 160 L364 160" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M396 160 L614 160" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M130 146 Q380 85 630 146" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(380, 296, "⟦기구는 자기 통로하고만, 통로끼리는 서로 다 이야기해요|each ride talks only to its own connector — the connectors talk to each other⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 통로를 다는 것도 일이 늘어요, 기구가 적으면 안 써도 돼요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ride(140, 230, 0.55, color="var(--accent)") + sidecar(210, 202, 0.9)
         + person(50, 174, s=0.5, face=FROWN + SWEAT, **MECHANIC)
         + label(190, 270, "⟦통로도 관리할 게 하나 늘어요|now there's one more thing to manage⟧", 11, "var(--ink)")
         + ride(540, 230, 0.55, color="var(--good)") + ride(680, 230, 0.5, color="#5B8DEF")
         + '<path d="M580 208 L648 208" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(610, 270, "⟦기구가 몇 개 안 되면 안 써도 돼요|with just a few rides, you don't need one at all⟧", 11, "var(--ink)")
         + label(380, 288, "⟦사이드카도 늘어나면 복잡해져요 — 꼭 필요할 때만 쓰세요|sidecars add up too — use them only when you actually need them⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "servicemesh", "order": 9,
    "title": ("기구 사이 전용 통로", "The Dedicated Path Between Rides"),
    "h1": ("<em>서비스 메시</em>가 뭐예요?", "What is a <em>Service Mesh</em>?"),
    "sub": ("서비스 메시를 기구끼리 이야기할 때 쓰는 전용 통로 이야기로 풀어봤어요.",
            "A service mesh, told as a story about the dedicated path rides use to talk to each other."),
    "panels": [
        {"svg": P1, "alt": ("기구 세 개 사이에 색과 모양이 다른 선 네 개가 어지럽게 얽혀 있고, 정비사가 당황함", "Four differently styled lines tangle between three rides while a mechanic looks confused"),
         "caption": ("기구끼리 서로 다른 말로 이야기하다 꼬여요.", "Rides talk to each other in different ways, and it all tangles."),
         "small": ("재고 확인, 대기 상황 같은 걸 각자 방식대로 물어봐요.", "Each ride asks about stock or wait times in its own way.")},
        {"svg": P2, "alt": ("기구 네 개 사이에 실타래처럼 엉킨 점선들이 가득함", "Dashed lines tangle into a hairball between four rides"),
         "caption": ("기구가 많아지면 연결선이 실타래처럼 엉켜요.", "With more rides, the wires tangle into a hairball."),
         "small": ("기구 하나가 늘 때마다 연결선이 훨씬 더 늘어나요.", "Each new ride adds far more connections than just one.")},
        {"svg": P3, "hero": True, "alt": ("기구 두 개 뒤에 똑같이 생긴 작은 통로 상자가 붙어 있고, 통로끼리만 선으로 이어짐", "Two rides each have an identical small connector box attached behind them, linked only to each other"),
         "caption": ("기구 뒤에 똑같은 통로를 하나씩 붙이면, 통로끼리만 이야기해요.", "Attach the same small connector behind each ride, and the connectors talk to each other."),
         "small": ("기구 자신은 신경 안 써도 돼요.", "The rides themselves don't need to worry about it."),
         "tricks": (4, [
             (SIDECAR_I, ("기구마다 같은 통로 하나", "One matching connector each"), ("생김새가 다 똑같아요", "every one looks the same"), "calm"),
             (SYNC_I, ("통로끼리는 같은 말로", "Connectors share one language"), ("기구 말은 안 바꿔요", "the ride's own language stays put")),
             (LOG_I, ("누가 누구한테 말했는지 기록", "Logs who talked to whom"), ("나중에 들여다볼 수 있어요", "you can look it up later"), "warm"),
             (REROUTE_I, ("하나 끊겨도 다른 길로", "One down, reroute around"), ("기구는 그대로 있어요", "the ride itself stays untouched")),
         ])},
        {"svg": P4, "alt": ("기구 세 개 위에 사이드카 세 개가 붙어 있고, 사이드카끼리 그물처럼 서로 다 이어짐", "Three rides each carry a sidecar on top, and the three sidecars are all connected to one another"),
         "caption": ("기구는 자기 통로하고만, 통로끼리는 서로 다 이야기해요.", "Each ride talks only to its own connector — the connectors talk to each other."),
         "small": ("이 그물이 바로 서비스 메시예요.", "This web of connectors is the service mesh itself.")},
        {"svg": P5, "alt": ("왼쪽: 기구 하나에 통로를 달고 정비사가 땀을 흘림. 오른쪽: 기구 두 개가 통로 없이 직접 이어짐", "Left: a mechanic sweats while attaching a connector to one ride. Right: two rides connect directly without any connector"),
         "caption": ("통로를 다는 것도 일이 늘어요 — 기구가 적으면 안 써도 돼요.", "Adding connectors is more work too — with just a few rides, skip it."),
         "small": ("사이드카도 늘어나면 복잡해져요. 꼭 필요할 때만 쓰세요.", "Sidecars add up too. Use them only when you actually need them.")},
    ],
    "summary": (("<b>서비스 메시</b> = 기구끼리 직접 말 안 걸고, 기구마다 붙은 <b>똑같은 통로(사이드카)</b>가 대신 <b>정해진 말로 이야기</b>하게 하는 방법.",
                 "A <b>service mesh</b> = instead of rides talking directly, each one gets an identical <b>sidecar connector</b> that talks to the others in a shared language."),
                ("서비스 메시는 마이크로서비스 사이의 통신을 애플리케이션 코드 밖에서 처리하는 인프라 계층이에요. 각 서비스 옆에 사이드카 프록시를 붙여서 트래픽 제어·mTLS·재시도·관측을 통로 쪽에서 전담해요.",
                 "A service mesh is an infrastructure layer that handles communication between microservices outside the application code. A sidecar proxy next to each service takes over traffic control, mTLS, retries, and observability.")),
    "glossary": [
        ("서비스 메시", "Service mesh", ("기구 사이 전용 통로 그물.", "The web of dedicated paths between rides."), ("기구끼리 말이 안 통하던 문제를 통로가 대신 풀어요.", "The connectors solve the problem of rides not speaking the same language.")),
        ("사이드카", "Sidecar", ("기구 뒤에 붙는 똑같이 생긴 통로 상자.", "The identical connector box attached behind each ride."), ("기구마다 하나씩, 생김새가 다 같아요.", "One per ride, and they all look the same.")),
        ("mTLS", "mTLS", ("통로끼리만 아는 암호.", "A code only the connectors know."), ("다른 통로인 척해도 못 끼어들어요.", "No one can sneak in pretending to be a connector.")),
        ("트래픽 제어", "Traffic control", ("어느 길로, 얼마나 보낼지 정하는 일.", "Deciding which path gets how much traffic."), ("통로가 기구 대신 맡아요.", "The connector handles it instead of the ride.")),
        ("재시도 정책", "Retry policy", ("한 번에 안 되면 잠깐 쉬었다 다시 거는 규칙.", "The rule for waiting a bit and trying again."), ("통로가 기구마다 따로 안 정해도 되게 해줘요.", "The connector means each ride doesn't need its own rule.")),
        ("관측", "Observability", ("누가 누구한테 말했는지 다 기록하는 일.", "Logging who talked to whom."), ('통로끼리 오간 말은 전부 기록으로 남아요. → <a href="goldensignals-ko.html">관제실의 계기판 네 개</a>', 'Everything the connectors say to each other gets logged. → <a href="goldensignals-en.html">the four gauges on the wall</a>')),
        ("서킷 브레이커", "Circuit breaker", ("한쪽이 자꾸 고장나면 아예 그쪽으로 안 보내는 장치.", "A switch that stops sending traffic to a side that keeps failing."), ("이것도 통로 쪽에서 대신 챙겨요.", "The connector takes care of this too.")),
        ("API 게이트웨이", "API gateway", ("손님과 기구 사이의 안내소.", "The booth between guests and rides."), ('안내소는 손님-기구 사이, 서비스 메시는 기구-기구 사이예요. → <a href="apigateway-ko.html">정문 안내소</a>', 'The gateway sits between guests and rides; the mesh sits between rides themselves. → <a href="apigateway-en.html">the front gate booth</a>')),
    ],
}
