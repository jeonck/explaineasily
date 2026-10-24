from _draw import *
from _world import *

# 1. 산골 마을엔 우체국이 없어요
P1 = svg(300, sky(300)
         + person(160, 190, s=0.7, face=FROWN, **CARRIER) + envelope(160, 140, 0.5)
         + person(400, 190, s=0.7, face=EYES, **CARRIER) + person(620, 190, s=0.7, face=EYES, **CARRIER)
         + label(380, 40, "⟦산골 마을엔 고정된 우체국이 없어요|this mountain village has no fixed post office⟧", 13, "var(--ink)")
         + label(380, 270, "⟦봉투를 누구에게 맡겨야 목적지에 갈지 몰라요|no one knows who to hand the envelope to, to reach the destination⟧", 13, "var(--bad)"))

# 2. 집배원들이 계속 움직여서, 길도 계속 바뀜
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.6, face=EYES, **CARRIER) + person(380, 220, s=0.6, face=EYES, **CARRIER) + person(560, 150, s=0.6, face=EYES, **CARRIER)
         + label(380, 70, "⟦어제 통했던 길이 오늘은 안 통할 수도 있어요|yesterday's working path might not work today⟧", 12, "var(--ink)")
         + label(380, 270, "⟦집배원들이 계속 움직이니 길을 그때그때 새로 찾아야 해요|carriers keep moving, so the path must be found fresh each time⟧", 12, "var(--ink)"))

# 3. hero: Ad-hoc 라우팅 = 집배원들끼리 서로 봉투를 건네며 길을 찾는 법
P3 = svg(340, sky(340)
         + person(180, 160, s=0.75, face=SMILE, **CARRIER) + envelope(180, 110, 0.5)
         + person(380, 220, s=0.75, face=SMILE, **CARRIER)
         + person(580, 160, s=0.75, face=SMILE, **CARRIER)
         + label(260, 185, "→", 26, "var(--accent)", cls="d") + label(480, 185, "→", 26, "var(--accent)", cls="d")
         + label(380, 30, "⟦Ad-hoc 라우팅 = 고정 우체국 없이 집배원끼리 봉투를 건네 길을 찾는 법|ad-hoc routing = carriers hand envelopes to each other, finding the way without a fixed post office⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦누가 어디 있는지 서로 계속 알려주며 길을 새로 만들어요|they keep telling each other where they are, building the path as they go⟧", 12, "var(--muted)"))

I1 = icon('<circle cx="18" cy="32" r="8" fill="var(--accent)"/><circle cx="46" cy="18" r="8" fill="var(--accent)"/><circle cx="46" cy="46" r="8" fill="var(--accent)"/><path d="M18 32 L46 18 M18 32 L46 46" stroke="var(--stone)" stroke-width="3"/>')
I2 = icon('<path d="M14 32 h20 M34 32 l-6 -6 M34 32 l-6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="46" cy="32" r="8" fill="var(--good)"/>')
I3 = icon('<path d="M12 44 q20 -36 40 0" stroke="var(--accent)" stroke-width="4" fill="none" stroke-dasharray="7 5"/><circle cx="12" cy="44" r="5" fill="var(--stone)"/><circle cx="52" cy="44" r="5" fill="var(--stone)"/>')
I4 = icon('<rect x="10" y="26" width="44" height="12" rx="6" fill="var(--bad)"/><path d="M32 26 v-10 M32 38 v10" stroke="var(--bad)" stroke-width="3"/>')

# 4. 길 찾는 두 가지 방식
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦길 찾는 두 방식|TWO WAY-FINDING STYLES⟧",
                    ("⟦미리 외우기 — 늘 주변 길을 서로 알려주며 외워둬요|proactive — they keep sharing and memorizing nearby paths⟧",
                     "⟦그때그때 묻기 — 보낼 게 생겼을 때만 길을 물어요|reactive — only asks for a path when there's something to send⟧",
                     "⟦홉(hop) — 몇 명을 거쳐가는지 세는 단위예요|hop — a count of how many carriers it passes through⟧",
                     "⟦끊김 — 중간 집배원이 사라지면 길도 끊겨요|break — if a middle carrier disappears, the path breaks⟧"), 1.0))

# 5. 한계: 집배원이 적거나 멀리 흩어지면 길 찾기 자체가 어려워요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + person(260, 125, s=0.7, face=EYES, **CARRIER) + label(260, 250, "⟦고정 우체국 없이도 길을 잇는 게 장점이에요|its strength: connecting a path with no fixed post office⟧", 11, "var(--ink)")
         + person(540, 150, s=0.7, face=SWEAT + FROWN, **CARRIER) + label(540, 275, "⟦너무 멀거나 사람이 적으면 길이 끊겨요|too far apart or too few people, and the path just breaks⟧", 11, "var(--ink)")
         + label(380, 40, "⟦V2X·재난 현장처럼 고정 통신망이 없는 곳에서 특히 쓰여요|used especially where there's no fixed network — like V2X or disaster zones⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "adhocrouting", "order": 18,
    "title": ("집배원끼리 서로 길을 찾아 건네는 법", "How Carriers Find the Way Among Themselves"),
    "h1": ("<em>Ad-hoc 라우팅 프로토콜</em>이 뭐예요?", "What is an <em>Ad-hoc Routing Protocol</em>?"),
    "sub": ("Ad-hoc 라우팅을, 고정 우체국 없는 산골에서 집배원끼리 봉투를 건네며 길을 찾는 이야기로 풀어봤어요.",
            "Ad-hoc routing, told as a story about carriers in a mountain village with no fixed post office, finding the way by handing envelopes to each other."),
    "panels": [
        {"svg": P1, "alt": ("산골 마을에 고정 우체국이 없고 집배원이 봉투를 들고 당황함", "A mountain village has no fixed post office, and a carrier looks confused holding an envelope"),
         "caption": ("산골 마을엔 고정된 우체국이 없어요.", "This mountain village has no fixed post office."),
         "small": ("봉투를 누구에게 맡겨야 목적지에 갈지 몰라요.", "No one knows who to hand the envelope to, to reach the destination.")},
        {"svg": P2, "alt": ("집배원 세 명이 계속 움직이며 길이 계속 바뀜", "Three carriers keep moving around, and the path keeps changing"),
         "caption": ("집배원들이 계속 움직여서, 길도 계속 바뀌어요.", "Carriers keep moving, so the path keeps changing."),
         "small": ("어제 통했던 길이 오늘은 안 통할 수도 있어요.", "Yesterday's working path might not work today.")},
        {"svg": P3, "hero": True, "alt": ("집배원 세 명이 봉투를 서로 건네며 목적지까지 길을 이어감", "Three carriers hand an envelope to each other, chaining a path to the destination"),
         "caption": ("Ad-hoc 라우팅 = 집배원끼리 봉투를 건네며 길을 찾는 거예요.", "Ad-hoc routing = carriers find the way by handing envelopes to each other."),
         "small": ("누가 어디 있는지 서로 계속 알려주며 길을 새로 만들어요.", "They keep telling each other where they are, building the path as they go."),
         "tricks": (4, [
             (I1, ("서로 연결", "Peer Connection"), ("집배원끼리 직접 이어져요", "carriers link up directly")),
             (I2, ("다음 사람에게", "Hand to Next"), ("한 명씩 건네며 전달", "passed on one by one"), "calm"),
             (I3, ("길을 그때그때", "Find On Demand"), ("고정된 경로가 없어요", "no fixed path at all")),
             (I4, ("끊어질 수 있음", "Can Break"), ("한 명만 빠져도 끊겨요", "one missing link breaks it"), "warm"),
         ])},
        {"svg": P4, "alt": ("길 찾는 두 방식 안내판: 미리 외우기, 그때그때 묻기, 홉, 끊김 네 줄", "A guide board listing proactive, reactive, hop, and break for way-finding"),
         "caption": ("길을 찾는 방식도 두 가지예요.", "There are two ways to find the path."),
         "small": ("늘 외워두거나, 보낼 게 생겼을 때만 물어봐요.", "Keep it memorized always, or only ask when there's something to send.")},
        {"svg": P5, "alt": ("왼쪽: 고정 우체국 없이도 길을 잇는 게 장점. 오른쪽: 너무 멀거나 사람이 적으면 길이 끊김", "Left: its strength is connecting without a fixed post office. Right: too sparse or too far, and the path breaks"),
         "caption": ("집배원이 적거나 흩어지면 길 찾기가 어려워요.", "Too few or too scattered carriers make way-finding hard."),
         "small": ("V2X·재난 현장처럼 고정 통신망이 없는 곳에서 특히 쓰여요.", "Used especially where there's no fixed network — like V2X or disaster zones.")},
    ],
    "summary": (("<b>Ad-hoc 라우팅</b> = 고정 우체국 없이, <b>집배원끼리 서로 봉투를 건네며</b> 그때그때 목적지까지 길을 잇는 방법.",
                 "<b>Ad-hoc routing</b> = chaining a path to the destination by having <b>carriers hand envelopes to each other</b>, with no fixed post office at all."),
                ("Ad-hoc 라우팅 프로토콜은 고정 인프라(기지국·라우터) 없이 노드들이 서로 직접 연결해 패킷을 중계하는 방식이에요. AODV·DSR처럼 필요할 때만 경로를 찾는 반응형 방식과, OLSR처럼 늘 경로를 미리 유지하는 능동형 방식으로 나뉘고, 노드 이동·이탈에 따라 경로가 자주 끊기고 재구성돼요.",
                 "Ad-hoc routing protocols let nodes relay packets by connecting directly to each other, with no fixed infrastructure like base stations or routers. Reactive protocols (AODV, DSR) find a route only when needed, while proactive ones (OLSR) always keep routes ready in advance; routes frequently break and get rebuilt as nodes move or drop out.")),
    "glossary": [
        ("MANET", "MANET", ("고정 우체국 없는 임시 배송망.", "A temporary delivery network with no fixed post office."), ("Mobile Ad-hoc NETwork의 줄임말이에요.", "Short for Mobile Ad-hoc NETwork.")),
        ("반응형 라우팅", "Reactive Routing", ("보낼 게 생겼을 때만 길을 묻는 방식.", "Only asking for a path when there's something to send."), ("AODV·DSR이 이 방식이에요.", "AODV and DSR work this way.")),
        ("능동형 라우팅", "Proactive Routing", ("늘 주변 길을 외워두는 방식.", "Always keeping nearby paths memorized."), ("OLSR이 이 방식이에요.", "OLSR works this way.")),
        ("홉(Hop)", "Hop", ("몇 명을 거쳐가는지 세는 단위.", "A count of how many carriers it passes through."), ("홉이 많을수록 길이 길어요.", "More hops means a longer path.")),
        ("V2X", "V2X", ("달리는 트럭끼리 주고받는 통신.", "The chatter between moving trucks themselves."), ('고정망 없이 움직이는 상황의 대표 사례예요. → <a href="v2x-ko.html">트럭끼리 주고받는 쪽지</a>', 'A flagship case of coordinating on the move without a fixed network. → <a href="v2x-en.html">the note trucks pass to each other</a>')),
        ("AMI(지능형 검침)", "AMI", ("계량기가 자동으로 값을 보고하는 망.", "The network where meters report readings automatically."), ('계량기끼리 서로 중계하며 보고하기도 해요. → <a href="ami-ko.html">계량기가 자동으로 편지를 보내는 망</a>', 'Meters sometimes relay through each other too. → <a href="ami-en.html">the network where meters mail their own readings</a>')),
        ("회선교환·패킷교환", "Circuit vs Packet Switching", ("전용 도로냐, 조각내 보내기냐.", "A dedicated road, or splitting it into pieces."), ('Ad-hoc 라우팅은 조각내 보내는 방식 위에서 동작해요. → <a href="circuitpacket-ko.html">전용 도로냐, 조각내 보내기냐</a>', 'Ad-hoc routing runs on top of the piece-by-piece style. → <a href="circuitpacket-en.html">a dedicated road, or splitting it into pieces</a>')),
        ("라우팅 테이블", "Routing Table", ("고정 우체국이 쓰는 길 안내판.", "The guide board a fixed post office relies on."), ("고정 인프라가 있을 땐 이게 더 단순한 답이에요.", "With fixed infrastructure, this is the simpler answer instead.")),
    ],
}
