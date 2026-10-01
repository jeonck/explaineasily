from _draw import *
from _world import *

# 1. 기구 하나 문제가 옆 기구로, 또 옆 기구로 번져 공원 전체가 멈춰요
P1 = svg(300, sky(300)
         + ride(90, 230, 0.62, color="var(--bad)", closed=True)
         + ride(270, 230, 0.62, color="var(--bad)", closed=True)
         + ride(450, 230, 0.62, color="var(--bad)", closed=True)
         + ride(630, 230, 0.62, color="var(--bad)", closed=True)
         + '<path d="M130 128 Q380 92 650 128" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M636 120 L658 128 L636 136 Z" fill="var(--bad)"/>'
         + label(380, 40, "⟦문제가 옆 기구로, 또 옆 기구로 번져요|trouble spreads from one ride to the next, and the next⟧", 13, "var(--bad)", cls="d")
         + label(380, 284, "⟦기구 하나에서 생긴 문제가 옆 기구로 번져 공원 전체가 멈춰요|trouble in one ride spreads until the whole park stops⟧", 12, "var(--ink)"))

# 2. 왜: 모든 기구가 같은 자원(발전기, 직원 풀)을 같이 쓰면, 하나가 다 써버려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/><ellipse cx="380" cy="300" rx="440" ry="36" fill="var(--good-soft)"/>'
         + shed(380, 230, 1.1, label_text="⟦발전기 하나|ONE GENERATOR⟧")
         + ride(90, 230, 0.55, color="var(--stone-dark)")
         + ride(250, 230, 0.55, color="var(--stone-dark)")
         + ride(510, 230, 0.55, color="var(--stone-dark)")
         + ride(670, 230, 0.55, color="var(--stone-dark)")
         + ''.join(f'<path d="M380 196 L{rx} 180" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>' for rx in (90, 250, 510, 670))
         + person(420, 120, s=0.55, face=FROWN + SWEAT, **MECHANIC)
         + label(380, 40, "⟦기구 전부가 발전기 하나, 직원 풀 하나를 같이 써요|every ride shares the one generator, the one staff pool⟧", 12, "var(--ink)", cls="d")
         + label(380, 284, "⟦모든 기구가 같은 자원을 같이 쓰면, 하나가 다 써버려요|when every ride shares the same resource, one of them can use it all up⟧", 12, "var(--ink)"))

# 3. hero: 구역으로 나누고 구역마다 자기 몫의 자원만 쓰게 해요
ZONESPLIT_I = icon('<rect x="8" y="8" width="22" height="22" fill="var(--bad)"/><rect x="34" y="8" width="22" height="22" fill="var(--good)"/><rect x="8" y="34" width="22" height="22" fill="var(--good)"/><rect x="34" y="34" width="22" height="22" fill="var(--good)"/>')
OWNSHARE_I = icon('<rect x="10" y="30" width="16" height="20" fill="var(--stone)"/><path d="M8 30 h20 l-10 -14z" fill="var(--stone-dark)"/><rect x="38" y="30" width="16" height="20" fill="var(--stone)"/><path d="M36 30 h20 l-10 -14z" fill="var(--stone-dark)"/>')
ISOLATED_I = icon('<rect x="4" y="16" width="4" height="32" fill="var(--stone-dark)"/><rect x="8" y="16" width="20" height="32" fill="var(--bad)"/><rect x="28" y="16" width="4" height="32" fill="var(--stone-dark)"/><rect x="32" y="16" width="20" height="32" fill="var(--good)"/><rect x="52" y="16" width="4" height="32" fill="var(--stone-dark)"/>')
EXTRA_I = icon('<path d="M32 8 l6 14 h14 l-11 10 4 14 -13 -8 -13 8 4 -14 -11 -10 h14z" fill="var(--accent)"/>')

P3 = svg(340, sky(340)
         + '<rect x="197" y="60" width="6" height="200" fill="var(--stone-dark)"/><rect x="377" y="60" width="6" height="200" fill="var(--stone-dark)"/><rect x="557" y="60" width="6" height="200" fill="var(--stone-dark)"/>'
         + shed(110, 120, 0.4) + ride(110, 260, 0.58, color="var(--bad)", closed=True) + label(110, 56, "⟦구역1|ZONE 1⟧", 11, "var(--ink)")
         + shed(290, 120, 0.4) + ride(290, 260, 0.58, color="var(--good)") + label(290, 56, "⟦구역2|ZONE 2⟧", 11, "var(--ink)")
         + shed(470, 120, 0.4) + ride(470, 260, 0.58, color="#5B8DEF") + label(470, 56, "⟦구역3|ZONE 3⟧", 11, "var(--ink)")
         + shed(650, 120, 0.4) + ride(650, 260, 0.58, color="var(--accent)") + label(650, 56, "⟦구역4|ZONE 4⟧", 11, "var(--ink)")
         + label(380, 25, "⟦구역을 나누면, 한 구역이 문제여도 다른 구역은 멀쩡해요|split into zones — one zone's trouble doesn't touch the others⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦배의 방수 격벽과 같아요|just like a ship's watertight bulkheads⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 공원을 4구역으로 나눈 지도, 한 구역만 꽉 차고 나머지는 정상
P4 = svg(300, sky(300, ground=False)
         + '<rect x="40" y="40" width="680" height="170" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + '<rect x="46" y="46" width="162" height="158" fill="var(--bad-soft)"/>'
         + '<rect x="212" y="46" width="162" height="158" fill="var(--good-soft)"/>'
         + '<rect x="378" y="46" width="162" height="158" fill="var(--good-soft)"/>'
         + '<rect x="544" y="46" width="162" height="158" fill="var(--good-soft)"/>'
         + ride(127, 190, 0.5, color="var(--bad)", closed=True) + label(127, 70, "⟦구역1 — 꽉 참|ZONE 1 — full⟧", 11, "var(--ink)")
         + ride(293, 190, 0.5, color="var(--good)") + label(293, 70, "⟦구역2|ZONE 2⟧", 11, "var(--ink)")
         + ride(459, 190, 0.5, color="var(--good)") + label(459, 70, "⟦구역3|ZONE 3⟧", 11, "var(--ink)")
         + ride(625, 190, 0.5, color="var(--good)") + label(625, 70, "⟦구역4|ZONE 4⟧", 11, "var(--ink)")
         + label(380, 284, "⟦한 구역만 자원을 다 써도, 나머지 세 구역은 정상이에요|only one zone's resources run out — the other three stay normal⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 너무 잘게 나누면 관리가 번거롭고 자원이 낭비돼요
P5 = svg(300, sky(300)
         + ''.join(f'<rect x="{40+i*72}" y="150" width="64" height="70" rx="3" fill="{"var(--good-soft)" if i % 2 else "var(--accent-soft)"}" stroke="var(--line)" stroke-width="2"/>' for i in range(9))
         + ''.join(f'<rect x="{40+i*72+26}" y="160" width="12" height="14" fill="var(--stone-dark)"/>' for i in range(9))
         + person(400, 70, s=0.65, face=FROWN + SWEAT, **MANAGER)
         + bubble(440, 20, 220, 46, "⟦구역이 9개나... 돌보기 힘들어요|nine zones... hard to keep up with⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 284, "⟦너무 잘게 나누면 관리가 번거롭고 자원이 낭비돼요 — 적당한 크기가 필요해요|split too finely and management gets tedious while resources go to waste — the right size matters⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "bulkhead", "order": 15,
    "title": ("불이 안 번지게 나눈 구역", "Zones That Keep Trouble From Spreading"),
    "h1": ("<em>벌크헤드</em>가 뭐예요?", "What is a <em>Bulkhead</em>?"),
    "sub": ("벌크헤드 패턴을 구역마다 자기 몫의 자원만 쓰게 나눈 놀이공원 이야기로 풀어봤어요.",
            "The bulkhead pattern, told as a story about a park split into zones that each use only their own share of resources."),
    "panels": [
        {"svg": P1, "alt": ("기구 네 개가 차례로 고장나고, 빨간 번짐 화살표가 하나에서 다음으로 이어짐", "Four rides break one after another, with a red spreading arrow linking them"),
         "caption": ("기구 하나에서 생긴 문제가 옆 기구로 번져 공원 전체가 멈춰요.", "Trouble in one ride spreads until the whole park stops."),
         "small": ("고장이 담장 없이 그대로 옆으로, 또 옆으로 넘어가요.", "The trouble crosses over with nothing to stop it, again and again.")},
        {"svg": P2, "alt": ("발전기 하나가 기구 네 개 전부에 전기를 보내고, 정비사가 땀을 흘리며 걱정함", "One generator feeds all four rides while a mechanic worries and sweats"),
         "caption": ("모든 기구가 같은 자원을 같이 쓰면, 하나가 다 써버려요.", "When every ride shares the same resource, one of them can use it all up."),
         "small": ("발전기도 직원도 하나뿐이라 전부 같이 걸려요.", "One generator, one staff pool — everyone is tied to the same thing.")},
        {"svg": P3, "hero": True, "alt": ("공원이 벽으로 네 구역으로 나뉘고, 구역마다 자기 발전기와 기구가 있음. 1구역만 고장나고 나머지는 멀쩡함", "The park split into four walled zones, each with its own generator and ride; only zone 1 is broken, the rest are fine"),
         "caption": ("구역을 나누면, 한 구역이 문제여도 다른 구역은 멀쩡해요.", "Split into zones — one zone's trouble doesn't touch the others."),
         "small": ("배의 방수 격벽과 같아요.", "Just like a ship's watertight bulkheads."),
         "tricks": (4, [
             (ZONESPLIT_I, ("구역을 나눠요", "Split into zones"), ("담을 세워요", "put up a wall"), "calm"),
             (OWNSHARE_I, ("구역마다 자기 몫만", "Each zone gets its own share"), ("인원·전력 따로요", "its own staff, its own power")),
             (ISOLATED_I, ("한 구역만 영향받아요", "Only one zone is affected"), ("다른 구역은 그대로", "the others stay untouched"), "warm"),
             (EXTRA_I, ("중요한 구역엔 더 넉넉히", "Give important zones more"), ("핵심 구역부터 챙겨요", "protect the critical ones first")),
         ])},
        {"svg": P4, "alt": ("공원 지도가 네 구역으로 나뉘어 있고, 1구역만 빨갛게 꽉 찬 채 표시되고 나머지 세 구역은 초록으로 정상", "A park map split into four zones; zone 1 is marked red and full while the other three are green and normal"),
         "caption": ("한 구역만 자원을 다 써도, 나머지 세 구역은 정상이에요.", "Only one zone's resources run out — the other three stay normal."),
         "small": ("지도로 보면 어느 구역이 문제인지 바로 보여요.", "The map shows at a glance which zone has the problem.")},
        {"svg": P5, "alt": ("구역이 아홉 개나 되는 작은 칸으로 쪼개져 있고, 공원장이 땀을 흘리며 돌보기 힘들다고 말함", "The park split into nine tiny zones, with the park manager sweating and saying it's hard to keep up"),
         "caption": ("너무 잘게 나누면 관리가 번거롭고 자원이 낭비돼요.", "Split too finely and management gets tedious while resources go to waste."),
         "small": ("적당한 크기로 나누는 게 중요해요.", "Finding the right zone size matters.")},
    ],
    "summary": (("<b>벌크헤드</b> = 공원을 <b>구역으로 나눠</b> 구역마다 <b>자기 몫의 자원만</b> 쓰게 하는 일. 한 구역이 문제여도 다른 구역은 <b>멀쩡해요</b>.",
                 "<b>Bulkhead</b> = splitting the park into <b>zones</b> that each use only <b>their own share</b> of resources, so trouble in one zone leaves the others <b>untouched</b>."),
                ("배의 방수 격벽에서 이름을 딴 패턴이에요. 스레드 풀, 커넥션 풀, 서버 인스턴스 같은 자원을 구역(테넌트, 서비스)별로 나눠 하나의 과부하가 전체로 캐스케이딩 실패하는 걸 막아요. 너무 잘게 나누면 관리 비용과 자원 낭비가 커져요.",
                 "Named after a ship's watertight bulkheads. It splits resources — thread pools, connection pools, server instances — by zone (tenant, service) so one overload doesn't cascade into a cascading failure across everything. Split too finely, though, and management overhead and wasted resources grow.")),
    "glossary": [
        ("벌크헤드 패턴", "Bulkhead pattern", ("공원을 구역으로 나누는 설계.", "Designing the park into separate zones."), ("한 구역의 문제가 다른 구역으로 안 넘어가게 해요.", "Keeps one zone's trouble from crossing into another.")),
        ("격리", "Isolation", ("구역 사이를 담으로 막는 것.", "Walling zones off from each other."), ("벌크헤드가 하는 일의 핵심이에요.", "The core thing a bulkhead does.")),
        ("자원 풀", "Resource pool", ("발전기나 직원처럼 같이 쓰는 몫.", "A shared supply, like a generator or a staff roster."), ("나누지 않으면 하나가 다 써버려요.", "Leave it unsplit, and one user can take it all.")),
        ("스레드 풀 격리", "Thread pool isolation", ("일꾼(스레드)을 구역별로 따로 두는 것.", "Giving each zone its own set of workers (threads)."), ("벌크헤드의 가장 흔한 적용 방법이에요.", "The most common way to apply a bulkhead.")),
        ("테넌트 격리", "Tenant isolation", ("손님 그룹(테넌트)별로 자원을 나누는 것.", "Splitting resources by guest group (tenant)."), ("한 테넌트가 몰려도 다른 테넌트는 안전해요.", "One tenant's surge doesn't endanger another.")),
        ("캐스케이딩 실패", "Cascading failure", ("기구 하나의 문제가 옆으로, 또 옆으로 번지는 것.", "One ride's trouble spreading to the next, and the next."), ("벌크헤드가 막으려는 바로 그 일이에요.", "The exact thing a bulkhead is built to stop.")),
        ("서킷 브레이커", "Circuit breaker", ("고장난 곳에 아예 안 보내는 빨간 버튼.", "The red button that stops sending guests somewhere broken."), ('구역을 나누는 벌크헤드와 짝을 이뤄 같이 써요. → <a href="circuitbreaker-ko.html">고장나면 누르는 빨간 버튼</a>', 'Often paired with bulkheads, which split things into zones. → <a href="circuitbreaker-en.html">the red button you press when something breaks</a>')),
        ("우아한 저하", "Graceful degradation", ("일부만 고장나도 나머지는 그대로 여는 것.", "Staying open with the rest, even if part is broken."), ("벌크헤드로 구역을 나눠 두면 이게 더 쉬워져요.", "Splitting into zones with a bulkhead makes this easier to pull off.")),
    ],
}
