from _draw import *
from _world import *

# 1. 택배 하나가 완성되기까지 공정이 너무 복잡해 보임
P1 = svg(300, sky(300)
         + person(220, 170, s=0.85, face=SWEAT + EYES, **SENDER)
         + envelope(400, 120, 0.5) + envelope(440, 150, 0.5) + envelope(480, 180, 0.5) + envelope(520, 140, 0.5)
         + label(380, 40, "⟦택배 하나를 보내는 데 할 일이 너무 많아 보여요|sending one package seems to take so many separate steps⟧", 13, "var(--ink)")
         + label(380, 270, "⟦포장, 주소, 분류, 배송, 확인까지… 뭐가 뭔지 헷갈려요|packing, addressing, sorting, shipping, confirming… it's hard to keep straight⟧", 13, "var(--bad)"))

# 2. 공정을 안 나누면, 한 사람이 처음부터 끝까지 다 떠안아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 170, s=0.9, face=SWEAT + FROWN, **SENDER)
         + envelope(260, 230, 0.4) + envelope(500, 230, 0.4) + postoffice(220, 130, 0.35) + postoffice(540, 130, 0.35)
         + label(380, 50, "⟦한 사람이 포장부터 배달 확인까지 전부 떠안으면 힘들어요|one person handling everything from packing to delivery confirmation is overwhelming⟧", 12, "var(--ink)")
         + label(380, 270, "⟦공정을 나눠서 각자 맡으면 훨씬 수월해져요|splitting the process so each step has its own owner makes it much easier⟧", 12, "var(--ink)"))

# 3. hero: OSI 7계층 = 택배가 보내지는 과정을 7단계 공정으로 나눈 것
P3 = svg(340, sky(340)
         + routemap(40, 30, 340, 300, "⟦7~5계층|LAYERS 7-5⟧",
                    ("⟦7 응용 — 무슨 내용을 담을지|7 application — what to write inside⟧",
                     "⟦6 표현 — 어떤 글씨·포장지로 쓸지|6 presentation — what script/wrapping to use⟧",
                     "⟦5 세션 — 대화를 언제 시작·끝낼지|5 session — when to start/end the talk⟧"), 0.95)
         + routemap(400, 30, 320, 300, "⟦4~1계층|LAYERS 4-1⟧",
                    ("⟦4 전송 — 등기냐 일반우편이냐|4 transport — registered or plain mail⟧",
                     "⟦3 네트워크 — 어느 동네로 보낼지|3 network — which town to send to⟧",
                     "⟦2 데이터링크 — 바로 옆 건물로 건네기|2 data link — handing to the next building⟧",
                     "⟦1 물리 — 실제 도로·전선 자체|1 physical — the actual road or wire⟧"), 0.95))

I1 = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 24 h44 M10 38 h44" stroke="var(--accent)" stroke-width="3"/>')
I2 = icon('<rect x="8" y="42" width="10" height="14" fill="var(--good)"/><rect x="22" y="30" width="10" height="26" fill="var(--good)"/><rect x="36" y="18" width="10" height="38" fill="var(--good)"/><rect x="50" y="10" width="10" height="46" fill="var(--good)"/>')
I3 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5" stroke-dasharray="6 5"/>')
I4 = icon('<rect x="10" y="26" width="44" height="12" rx="6" fill="var(--stone)"/><circle cx="18" cy="32" r="8" fill="var(--accent)"/><circle cx="46" cy="32" r="8" fill="var(--accent)"/>')

# 4. 7단계를 한 줄씩 다시 정리
P4 = svg(340, sky(340)
         + routemap(60, 40, 640, 260, "⟦7단계 배송 공정|THE 7-STAGE DELIVERY PROCESS⟧",
                    ("⟦7 응용 — 내용 정하기|7 application — decide the content⟧",
                     "⟦6 표현 — 포장지·글씨체 정하기|6 presentation — decide wrapping/format⟧",
                     "⟦5 세션 — 대화 시작·끝 정하기|5 session — decide when the talk starts/ends⟧",
                     "⟦4 전송 — 등기·일반우편 고르기|4 transport — choose registered/plain mail⟧",
                     "⟦3 네트워크 — 동네(주소) 정하기|3 network — decide the town (address)⟧",
                     "⟦2 데이터링크 — 옆 건물로 건네기|2 data link — hand to the next building⟧",
                     "⟦1 물리 — 실제 도로·전선|1 physical — the actual road or wire⟧"), 1.0))

# 5. 한계: 모든 택배가 7단계를 다 거치는 건 아니에요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + person(240, 150, s=0.75, face=EYES, **SORTER) + label(240, 230, "⟦L4 스위치는 4계층까지만 보고 결정해요|an L4 switch only checks up through layer 4⟧", 11, "var(--ink)")
         + person(540, 150, s=0.75, face=EYES, **CLERK) + label(540, 230, "⟦라우터는 3계층까지만 보고 길을 정해요|a router only checks up through layer 3 to choose the path⟧", 11, "var(--ink)")
         + label(380, 40, "⟦실제 장비는 7단계를 전부 거치지 않고 필요한 데까지만 봐요|real devices don't go through all 7 stages — only as far as they need⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "osi7", "order": 23,
    "title": ("7단계로 나뉜 배송 공정", "The Delivery Process Split Into 7 Stages"),
    "h1": ("<em>OSI 7계층</em>이 뭐예요?", "What is the <em>OSI 7-Layer Model</em>?"),
    "sub": ("OSI 7계층을, 택배 하나가 보내지기까지의 전체 공정을 7단계로 나눠놓은 이야기로 풀어봤어요.",
            "The OSI 7-layer model, told as a story about splitting the whole process of sending a package into 7 stages."),
    "panels": [
        {"svg": P1, "alt": ("한 사람이 땀을 흘리며 봉투 여러 개를 두고 포장부터 배송까지 전부 떠안으려 함", "A person sweats, surrounded by envelopes, trying to handle packing through delivery alone"),
         "caption": ("택배 하나를 보내는 데 할 일이 너무 많아요.", "Sending one package seems to take so many steps."),
         "small": ("포장, 주소, 분류, 배송, 확인까지… 뭐가 뭔지 헷갈려요.", "Packing, addressing, sorting, shipping, confirming… it's hard to keep straight.")},
        {"svg": P2, "alt": ("한 사람이 포장부터 배달 확인까지 전부 떠안으며 땀을 흘림", "One person sweats, carrying everything from packing to delivery confirmation alone"),
         "caption": ("공정을 안 나누면 한 사람이 다 떠안아요.", "Without splitting the process, one person carries everything."),
         "small": ("공정을 나눠서 각자 맡으면 훨씬 수월해져요.", "Splitting the process so each step has its own owner makes it much easier.")},
        {"svg": P3, "hero": True, "alt": ("두 개의 안내판에 7계층부터 1계층까지 배송 공정이 나뉘어 적혀 있음", "Two guide boards list the delivery process split from layer 7 down to layer 1"),
         "caption": ("OSI 7계층 = 배송 과정을 7단계 공정으로 나눈 거예요.", "OSI 7 layers = splitting the delivery process into 7 stages."),
         "small": ("각 단계가 자기 몫만 책임지고 다음 단계로 넘겨요.", "Each stage handles only its own job, then hands off to the next."),
         "tricks": (4, [
             (I1, ("단계별 분담", "Divide by Stage"), ("한 단계씩 나눠 맡아요", "each stage owns one job")),
             (I2, ("아래부터 위로", "Bottom to Top"), ("물리 도로부터 쌓아올려요", "built up from the physical road"), "calm"),
             (I3, ("캡슐화", "Encapsulation"), ("단계마다 포장을 덧씌워요", "each stage adds its own wrapper"), "warm"),
             (I4, ("계층 간 통신", "Peer Layers Talk"), ("같은 단계끼리 말이 통해요", "same-numbered stages understand each other")),
         ])},
        {"svg": P4, "alt": ("7단계 배송 공정 안내판: 응용, 표현, 세션, 전송, 네트워크, 데이터링크, 물리 일곱 줄", "A guide board listing all 7 delivery stages: application, presentation, session, transport, network, data link, physical"),
         "caption": ("7단계를 한 줄씩 정리하면 이래요.", "Here's each of the 7 stages in one line."),
         "small": ("위쪽(7)은 내용·형식을, 아래쪽(1)은 실제 도로를 다뤄요.", "The top (7) handles content and format; the bottom (1) handles the actual road.")},
        {"svg": P5, "alt": ("분류 직원은 4계층까지만, 우체국장은 3계층까지만 보고 결정함", "A sorter only checks up through layer 4, a clerk only through layer 3, to decide"),
         "caption": ("모든 택배가 7단계를 다 거치는 건 아니에요.", "Not every package goes through all 7 stages."),
         "small": ("실제 장비는 필요한 단계까지만 보고 결정해요.", "Real devices only check as far as they need to decide.")},
    ],
    "summary": (("<b>OSI 7계층</b> = 택배(데이터)가 보내지는 전체 과정을, <b>7개의 독립된 공정 단계</b>로 나눠 각자 맡게 한 모델.",
                 "<b>OSI 7 layers</b> = a model that splits the whole process of sending data into <b>7 independent stages</b>, each with its own job."),
                ("OSI 7계층 모델은 네트워크 통신을 물리(1)·데이터링크(2)·네트워크(3)·전송(4)·세션(5)·표현(6)·응용(7) 계층으로 나눈 참조 모델이에요. 각 계층은 바로 아래 계층의 서비스를 이용하고 바로 위 계층에 서비스를 제공하며, 데이터는 보낼 때 계층마다 포장(캡슐화)되고 받을 때 계층마다 벗겨져요.",
                 "The OSI 7-layer model is a reference model that splits network communication into physical (1), data link (2), network (3), transport (4), session (5), presentation (6), and application (7) layers. Each layer uses the service of the layer below and provides a service to the layer above; data gets wrapped (encapsulated) at each layer when sent, and unwrapped at each layer when received.")),
    "glossary": [
        ("응용/표현/세션 계층(7-5)", "Application/Presentation/Session (7-5)", ("내용·포장지·대화 시작끝을 정하는 상위 공정.", "The upper stages deciding content, wrapping, and the talk's start/end."), ("사람이 보는 내용에 가까운 단계예요.", "The stages closest to what people actually see.")),
        ("전송 계층(4)", "Transport Layer (4)", ("등기냐 일반우편이냐를 고르는 단계.", "The stage choosing registered or plain mail."), ('여기만 따로 더 깊이 다뤄요. → <a href="transportlayer-ko.html">포트를 나누고 신뢰도를 고르는 단계</a>', 'Covered in more depth on its own. → <a href="transportlayer-en.html">the stage that splits ports and picks reliability</a>')),
        ("네트워크 계층(3)", "Network Layer (3)", ("어느 동네로 보낼지 정하는 단계.", "The stage deciding which town to send to."), ('주소·구역 나누기가 이 계층의 일이에요. → <a href="subnetting-ko.html">동네를 작은 우편번호 구역으로 나누기</a>', "Addressing and zoning belong to this layer. → <a href=\"subnetting-en.html\">splitting the town into smaller zip-code zones</a>")),
        ("데이터링크/물리 계층(2-1)", "Data Link/Physical (2-1)", ("바로 옆 건물 전달과 실제 도로·전선.", "Handing to the next building, and the actual road or wire."), ("가장 아래, 실제로 신호가 흐르는 단계예요.", "The bottommost stages, where signals actually flow.")),
        ("캡슐화", "Encapsulation", ("단계마다 포장지를 덧씌우는 것.", "Adding a wrapper at each stage."), ("보낼 땐 덧씌우고, 받을 땐 벗겨내요.", "Added on the way out, peeled off on the way in.")),
        ("L4 스위치", "L4 Switch", ("4계층까지만 보고 결정하는 분류 직원.", "The sorter who decides after checking only up to layer 4."), ('계층을 실제로 참조하는 장비의 예시예요. → <a href="l4switch-ko.html">포트까지 보는 분류소 직원</a>', 'A concrete example of a device referencing these layers. → <a href="l4switch-en.html">the sorter who checks the port</a>')),
        ("회선교환·패킷교환", "Circuit vs Packet Switching", ("전용 도로냐, 조각내 보내기냐.", "A dedicated road, or splitting it into pieces."), ('하위 계층에서 실제로 오가는 방식이에요. → <a href="circuitpacket-ko.html">전용 도로냐, 조각내 보내기냐</a>', 'The actual transport method at the lower layers. → <a href="circuitpacket-en.html">a dedicated road, or splitting it into pieces</a>')),
        ("TCP/IP 모델", "TCP/IP Model", ("OSI보다 더 단순하게 4단계로 묶은 모델.", "A simpler model that groups the same idea into just 4 stages."), ("실제 인터넷은 이 더 단순한 모델을 따라요.", "The actual internet follows this simpler model instead.")),
    ],
}
