from _draw import *
from _world import *

# 1. 도시 하나에 홍수가 나서 그 공원이 통째로 문을 닫음 → 전국 손님이 다 못 들어옴
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + minipark(190, 230, 1.0)
         + '<rect x="90" y="246" width="200" height="30" fill="#5B9BD5" opacity="0.55"/>'
         + '<g transform="translate(190,210)"><rect x="-56" y="-6" width="112" height="10" fill="var(--bad)" transform="rotate(-8)"/><rect x="-56" y="10" width="112" height="10" fill="var(--bad)" transform="rotate(6)"/></g>'
         + label(190, 150, "⟦홍수!|FLOOD!⟧", 14, "var(--bad)", cls="d")
         + queueline(500, 174, 5, 0.5, 30)
         + label(560, 250, "⟦전국 손님이 다 못 들어와요|guests everywhere can't get in⟧", 11, "var(--bad)")
         + label(380, 285, "⟦도시 하나에 홍수가 나자, 공원이 통째로 문을 닫아버렸어요|one city floods, and the whole park shuts its doors⟧", 12, "var(--ink)"))

# 2. 왜: 공원이 한 도시에만 있으면 그 도시에 문제가 생기면 끝이에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + minipark(380, 230, 1.3)
         + person(570, 174, s=0.65, face=FROWN, **MANAGER)
         + bubble(600, 90, 160, 50, "⟦도시가 하나뿐이라, 끝이에요...|only one city, so that's it...⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 285, "⟦공원이 한 도시에만 있으면, 그 도시에 문제가 생기는 순간 끝이에요|if the park exists in only one city, trouble there means it's over⟧", 12, "var(--ink)"))

# 3. hero: 다른 도시에 쌍둥이 공원을 하나 더 지어서, 한 곳에 문제 생기면 다른 곳으로 보내요
P3 = svg(340, sky(340)
         + minipark(170, 280, 1.0) + label(170, 322, "⟦도시 A|CITY A⟧", 11, "var(--muted)")
         + minipark(560, 280, 1.0) + label(560, 322, "⟦도시 B (쌍둥이)|CITY B (twin)⟧", 11, "var(--muted)")
         + '<path d="M240 230 Q365 195 490 230" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(365, 182, "⟦명부 복제|log replicated⟧", 10, "var(--muted)")
         + queueline(70, 234, 2, 0.4, 24)
         + '<path d="M120 220 Q300 110 520 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + label(380, 30, "⟦다른 도시에 쌍둥이 공원을 하나 더 지어요|build a twin park in another city⟧", 14, "var(--ink)", cls="d")
         + label(380, 333, "⟦한 곳에 문제가 생기면, 다른 곳으로 손님을 보내요|when one has trouble, guests get sent to the other⟧", 12, "var(--muted)"))

# 4. 지도: 두 도시, 복제 화살표, 홍수난 도시 손님이 다른 도시로
P4 = svg(300, sky(300)
         + minipark(190, 230, 0.9) + '<rect x="100" y="246" width="180" height="24" fill="#5B9BD5" opacity="0.5"/>'
         + label(190, 268, "⟦도시 A (침수)|CITY A (flooded)⟧", 11, "var(--bad)")
         + minipark(570, 230, 0.9) + label(570, 268, "⟦도시 B|CITY B⟧", 11, "var(--good)")
         + '<path d="M260 190 Q380 155 500 190" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(380, 140, "⟦복제|replication⟧", 10, "var(--muted)")
         + person(80, 184, s=0.5, face=EYES, shirt="#7B3FA0") + '<path d="M110 195 Q300 70 520 195" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + label(300, 55, "⟦손님은 도시 B로 안내돼요|guests get sent to city B⟧", 11, "var(--good)")
         + label(380, 282, "⟦한 도시가 멈춰도, 다른 도시가 손님을 받아요|when one city stops, the other takes the guests⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 두 곳 다 짓고 유지하는 건 돈이 두 배로 들어요
P5 = svg(300, sky(300)
         + minipark(190, 230, 0.8) + minipark(560, 230, 0.8)
         + ticket(190, 150, 0.9, text="⟦$$|$$⟧") + ticket(560, 150, 0.9, text="⟦$$|$$⟧")
         + label(380, 60, "⟦두 곳을 다 짓고 유지하는 건 돈이 두 배로 들어요|building and keeping up both costs twice as much⟧", 13, "var(--bad)", cls="d")
         + label(380, 282, "⟦그래서 꼭 필요한 서비스만 다중 리전으로 둬요|so only the services that truly need it get multi-region⟧", 12, "var(--ink)"))

TWIN_I = icon('<rect x="4" y="30" width="24" height="24" fill="var(--accent)"/><path d="M2 30 a14 10 0 0 1 28 0z" fill="var(--accent)" opacity="0.7"/><rect x="34" y="20" width="26" height="34" fill="#5B8DEF"/><path d="M32 20 a15 11 0 0 1 30 0z" fill="#5B8DEF" opacity="0.7"/>')
REPLOG_I = icon('<path d="M14 24 a18 18 0 1 1 -2 20" stroke="var(--good)" stroke-width="5" fill="none"/><path d="M10 14 l4 12 -12 -2z" fill="var(--good)"/><rect x="24" y="30" width="16" height="12" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>')
REDIRECT_I = icon('<circle cx="18" cy="32" r="8" fill="var(--bad)"/><circle cx="46" cy="32" r="8" fill="var(--good)"/><path d="M26 28 Q36 10 46 24" stroke="var(--accent)" stroke-width="4" fill="none" stroke-dasharray="4 3"/><path d="M42 18 l6 6 -8 2z" fill="var(--accent)"/>')
BOTHACTIVE_I = icon('<rect x="6" y="22" width="22" height="20" rx="4" fill="var(--good)"/><rect x="36" y="22" width="22" height="20" rx="4" fill="var(--good)"/><path d="M28 32 h8" stroke="var(--good)" stroke-width="4"/>')

PAGE = {
    "slug": "multiregion", "order": 16,
    "title": ("쌍둥이 공원", "The Twin Park"),
    "h1": ("<em>다중 리전</em>이 뭐예요?", "What is <em>Multi-region</em>?"),
    "sub": ("다중 리전을, 다른 도시에 쌍둥이 공원을 하나 더 짓는 이야기로 풀어봤어요.",
            "Multi-region, told as a story about building a twin park in another city."),
    "panels": [
        {"svg": P1, "alt": ("도시 하나가 홍수로 잠기고 공원이 문을 닫아, 전국 손님이 줄을 서다 못 들어감", "A flooded city's park is shut down, and guests nationwide line up but can't get in"),
         "caption": ("도시 하나에 홍수가 나자, 공원이 통째로 문을 닫아버렸어요.", "One city floods, and the whole park shuts its doors."),
         "small": ("전국 손님이 다 못 들어와요.", "Guests everywhere can't get in.")},
        {"svg": P2, "alt": ("도시 하나뿐인 공원 앞에서 공원장이 끝이라며 걱정함", "In front of a park that exists in only one city, the manager worries it's all over"),
         "caption": ("공원이 한 도시에만 있으면, 그 도시에 문제가 생기는 순간 끝이에요.", "If the park exists in only one city, trouble there means it's over."),
         "small": ("하나뿐이라 피할 곳이 없어요.", "With only one, there's nowhere else to go.")},
        {"svg": P3, "hero": True, "alt": ("도시 A와 도시 B에 쌍둥이 공원이 있고, 명부가 서로 복제되며 손님이 양쪽으로 안내됨", "Twin parks sit in City A and City B, their logs replicated between them, with guests guided to either"),
         "caption": ("다른 도시에 쌍둥이 공원을 하나 더 지어요.", "Build a twin park in another city."),
         "small": ("한 곳에 문제가 생기면, 다른 곳으로 손님을 보내요.", "When one has trouble, guests get sent to the other."),
         "tricks": (4, [
             (TWIN_I, ("두 도시에 똑같이 지어요", "Build identically in two cities"), ("쌍둥이 공원이에요", "a true twin park"), "calm"),
             (REPLOG_I, ("명부도 서로 복제해요", "Replicate the log too"), ("똑같은 손님 명부로요", "the same guest log on both sides")),
             (REDIRECT_I, ("한쪽이 멈추면 반대쪽으로", "If one stops, send guests the other way"), ("자동으로 안내돼요", "guided there automatically"), "warm"),
             (BOTHACTIVE_I, ("둘 다 받을 수도 있어요", "Both can take guests at once"), ("액티브-액티브/패시브", "active-active or active-passive")),
         ])},
        {"svg": P4, "alt": ("지도에 침수된 도시 A와 멀쩡한 도시 B, 그 사이 복제 화살표, 손님을 도시 B로 보내는 화살표", "A map shows flooded City A and intact City B, a replication arrow between them, and guests redirected to City B"),
         "caption": ("한 도시가 멈춰도, 다른 도시가 손님을 받아요.", "When one city stops, the other takes the guests."),
         "small": ("명부는 미리 복제되어 있어서 바로 안내할 수 있어요.", "The log was already replicated, so guests can be redirected right away.")},
        {"svg": P5, "alt": ("두 쌍둥이 공원 위에 각각 돈 표시 티켓이 떠 있음", "A money ticket floats above each of the two twin parks"),
         "caption": ("두 곳을 다 짓고 유지하는 건 돈이 두 배로 들어요.", "Building and keeping up both costs twice as much."),
         "small": ("그래서 꼭 필요한 서비스만 다중 리전으로 둬요.", "So only the services that truly need it get multi-region.")},
    ],
    "summary": (("<b>다중 리전</b> = 다른 도시에 <b>쌍둥이 공원</b>을 짓고 명부를 <b>서로 복제</b>해 두어, 한 도시에 문제가 생기면 <b>다른 도시로 손님을 보내는</b> 일. 대신 두 곳을 유지하는 비용은 두 배예요.",
                 "<b>Multi-region</b> = building a <b>twin park</b> in another city and keeping their logs <b>replicated</b> to each other, so that when one city has trouble, <b>guests get redirected to the other</b>. The cost of running both, though, is double."),
                ("서비스를 지리적으로 다른 리전(데이터센터)에도 똑같이 띄워 두는 전략이에요. 리전 간 복제로 데이터를 맞추고, 장애 시 다른 리전으로 장애 조치를 해요. 먼 리전일수록 지연시간이 늘고, 어느 나라에 데이터를 둘지(데이터 주권)도 함께 고려해야 해요.",
                 "A strategy of running the same service in geographically separate regions (data centers) too. Replication keeps data in sync across regions, and failover switches to another region when one has trouble. More distant regions mean more latency, and data sovereignty — which country the data may sit in — has to be considered too.")),
    "glossary": [
        ("다중 리전", "Multi-region", ("쌍둥이 공원을 여러 도시에 두는 것.", "Keeping twin parks in more than one city."), ("한 도시가 멈춰도 다른 도시가 있어요.", "If one city stops, there's always another.")),
        ("액티브-액티브", "Active-active", ("두 도시 다 평소에도 손님을 받는 방식.", "A setup where both cities take guests all along."), ("둘 다 일하니까 한쪽이 멈춰도 바로 괜찮아요.", "Since both are already working, losing one is no big deal.")),
        ("액티브-패시브", "Active-passive", ("한 도시만 평소에 손님을 받는 방식.", "A setup where only one city takes guests normally."), ("쌍둥이 도시는 평소엔 대기만 해요.", "The twin city just waits, idle, most of the time.")),
        ("지연시간", "Latency", ("먼 도시일수록 오가는 데 걸리는 시간.", "How long it takes to go back and forth, the farther the city."), ("가까운 도시보다 먼 도시가 더 느려요.", "A distant city is slower than a nearby one.")),
        ("데이터 주권", "Data sovereignty", ("손님 명부를 어느 나라에 둘지의 문제.", "The question of which country a guest log is allowed to sit in."), ("도시(리전)를 고를 때 법과 규정도 함께 봐야 해요.", "Choosing a city (region) also means checking the law there.")),
        ("재해 복구", "Disaster recovery", ("공원 하나가 아예 무너져도 다시 여는 계획.", "The plan for reopening even if one whole park collapses."), ('다중 리전은 재해 복구를 위한 대표적인 방법이에요. → <a href="drp-ko.html">성이 불타도 다음 날 장사하는 법</a>', 'Multi-region is a classic way to achieve disaster recovery. → <a href="drp-en.html">how to open the morning after the fire</a>')),
        ("복제", "Replication", ("두 도시의 손님 명부를 똑같이 맞춰두는 일.", "Keeping both cities' guest logs identical."), ("복제가 늦으면, 넘어간 도시의 명부가 살짝 옛날 것일 수 있어요.", "If replication lags, the city you switch to may have a slightly older log.")),
        ("장애 조치", "Failover", ("한 도시가 멈추면 다른 도시로 넘어가는 동작.", "The act of switching to the other city when one stops."), ('다중 리전은 장애 조치를 도시 단위로 키운 거예요. → <a href="failover-ko.html">발전기가 꺼지면 예비 발전기가</a>', 'Multi-region is failover scaled up to a whole city. → <a href="failover-en.html">when the generator dies, the spare takes over</a>')),
    ],
}
