from _draw import *
from _world import *

# 1. 동네까지는 잘 왔는데, 어느 창구로 가야 할지 모름
P1 = svg(300, sky(300)
         + postoffice(380, 150, 0.9)
         + envelope(220, 200, 0.5) + envelope(540, 200, 0.5)
         + label(380, 40, "⟦동네(주소)까지는 잘 왔는데, 어느 창구로 가야 할지 몰라요|it reached the right town, but doesn't know which counter to go to⟧", 12, "var(--ink)")
         + label(380, 270, "⟦동네 안에도 웹용, 메일용 창구가 따로 있어요|the same town has separate counters for web, for mail, and more⟧", 13, "var(--bad)"))

# 2. 확실함(등기)과 속도(일반우편) 중 하나를 골라야 함
P2 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + envelope(190, 150, 0.9, registered=True) + label(190, 240, "⟦등기: 확인받고 보내 확실하지만 느려요|registered: confirmed, so sure but slow⟧", 11, "var(--ink)")
         + envelope(570, 150, 0.9) + label(570, 240, "⟦일반우편: 빠르지만 잃어버릴 수 있어요|plain: fast, but could get lost⟧", 11, "var(--ink)")
         + label(380, 282, "⟦확실함과 속도, 둘 다 가질 순 없어요|you can't have both certainty and speed at once⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 전송계층 = 창구 번호를 나누고 등기/일반우편을 고르는 단계
P3 = svg(340, sky(340)
         + person(380, 110, s=0.9, face=EYES, **CLERK)
         + envelope(220, 210, 0.6, text="80") + envelope(380, 230, 0.6, registered=True, text="21")
         + envelope(540, 210, 0.6, text="443")
         + label(380, 30, "⟦전송계층 = 창구 번호를 나누고, 등기냐 일반우편이냐를 고르는 단계|the transport layer = splitting counters by number, and choosing registered vs plain mail⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦동네까지 온 봉투를 정확한 창구와 방식으로 넘겨줘요|hands the envelope — once it's in the right town — to the right counter, the right way⟧", 12, "var(--muted)"))

I1 = icon('<rect x="10" y="22" width="44" height="22" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><text x="32" y="37" font-size="12" font-weight="700" fill="var(--accent)" text-anchor="middle">PORT</text>')
I2 = icon('<circle cx="20" cy="32" r="10" fill="var(--good)"/><path d="M15 32 l4 4 l8 -10" stroke="#fff" stroke-width="3" fill="none"/><circle cx="48" cy="32" r="10" fill="var(--accent)"/>')
I3 = icon('<rect x="8" y="42" width="10" height="14" fill="var(--accent)"/><rect x="22" y="30" width="10" height="26" fill="var(--accent)"/><rect x="36" y="18" width="10" height="38" fill="var(--accent)"/>')
I4 = icon('<path d="M14 32 h20 M34 32 l-6 -6 M34 32 l-6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 32 h-20 M50 32 l-6 -6 M50 32 l-6 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round" transform="translate(0,14)"/>')

# 4. 전송계층이 하는 네 가지 일
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦전송계층이 하는 일|WHAT THE TRANSPORT LAYER DOES⟧",
                    ("⟦포트 구분 — 같은 동네 안 창구를 번호로 나눠요|port separation — splits counters in the same town by number⟧",
                     "⟦신뢰도 선택 — 등기(TCP)냐 일반우편(UDP)이냐 골라요|reliability choice — registered (TCP) or plain (UDP)⟧",
                     "⟦분할·재조립 — 큰 짐을 조각내고, 받는 쪽에서 다시 맞춰요|segmentation — splits a big load, reassembles it at the other end⟧",
                     "⟦흐름·혼잡 제어 — 상대가 못 받으면 속도를 늦춰요|flow/congestion control — slows down when the other side can't keep up⟧"), 1.0))

# 5. 한계: 전송계층은 길(라우팅)을 직접 정하진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.75, face=EYES, **CLERK) + label(190, 240, "⟦창구와 방식은 전송계층이 정해요|the transport layer picks the counter and the method⟧", 11, "var(--ink)")
         + postoffice(570, 150, 0.6) + label(570, 240, "⟦동네까지 가는 길은 네트워크계층(라우팅)의 몫이에요|but the route to the town is the network layer's (routing) job⟧", 10, "var(--ink)")
         + label(380, 282, "⟦등기든 일반우편이든, 가는 길 자체는 한 단계 아래에서 정해져요|registered or plain, the actual route is decided one layer below⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "transportlayer", "order": 24,
    "title": ("포트를 나누고 신뢰도를 고르는 단계", "The Stage That Splits Ports and Picks Reliability"),
    "h1": ("<em>전송계층</em>의 역할이 뭐예요?", "What's the Role of the <em>Transport Layer</em>?"),
    "sub": ("전송계층을, 동네까지 온 봉투를 정확한 창구로 넘기고 등기·일반우편을 고르는 단계 이야기로 풀어봤어요.",
            "The transport layer, told as a story about handing an envelope — once it reaches the right town — to the right counter, and choosing registered or plain mail."),
    "panels": [
        {"svg": P1, "alt": ("봉투가 우체국 앞에 도착했지만 어느 창구로 가야 할지 알 수 없음", "Envelopes arrive at the post office but don't know which counter to go to"),
         "caption": ("동네까지는 왔는데 어느 창구로 가야 할지 몰라요.", "It reached the right town, but doesn't know which counter to go to."),
         "small": ("동네 안에도 웹용, 메일용 창구가 따로 있어요.", "The same town has separate counters for web, for mail, and more.")},
        {"svg": P2, "alt": ("왼쪽에 등기 봉투, 오른쪽에 일반 봉투가 각각 확실함과 속도를 설명함", "A registered envelope on the left and a plain one on the right, explaining certainty versus speed"),
         "caption": ("확실함(등기)과 속도(일반우편) 중 하나를 골라야 해요.", "You have to choose between certainty (registered) and speed (plain)."),
         "small": ("확실함과 속도, 둘 다 가질 순 없어요.", "You can't have both certainty and speed at once.")},
        {"svg": P3, "hero": True, "alt": ("우체국장이 창구 번호 80, 21(등기), 443으로 봉투를 나눠 보냄", "A clerk routes envelopes to counters 80, 21 (registered), and 443"),
         "caption": ("전송계층 = 창구 번호를 나누고 등기·일반우편을 고르는 단계예요.", "The transport layer = splitting by counter number and choosing registered vs plain."),
         "small": ("동네까지 온 봉투를 정확한 창구와 방식으로 넘겨줘요.", "It hands the envelope to the right counter, the right way, once it's in the right town."),
         "tricks": (4, [
             (I1, ("포트 구분", "Port Separation"), ("창구 번호로 나눠요", "splits by counter number")),
             (I2, ("신뢰도 선택", "Reliability Choice"), ("등기냐 일반우편이냐", "registered or plain mail"), "calm"),
             (I3, ("분할·재조립", "Segment & Reassemble"), ("큰 짐을 조각내요", "splits a big load into pieces"), "warm"),
             (I4, ("흐름 제어", "Flow Control"), ("상대 속도에 맞춰요", "matches the other side's pace")),
         ])},
        {"svg": P4, "alt": ("전송계층이 하는 일 안내판: 포트 구분, 신뢰도 선택, 분할·재조립, 흐름·혼잡 제어 네 줄", "A guide board listing port separation, reliability choice, segmentation, and flow/congestion control"),
         "caption": ("전송계층은 이 네 가지 일을 해요.", "The transport layer does these four jobs."),
         "small": ("상대가 못 받으면 속도를 늦춰 넘치지 않게 해요.", "It slows down when the other side can't keep up, to avoid overload.")},
        {"svg": P5, "alt": ("왼쪽: 창구와 방식은 전송계층이 정함. 오른쪽: 동네까지 가는 길은 네트워크계층(라우팅)의 몫", "Left: the transport layer picks the counter and method. Right: the route to town is the network layer's job"),
         "caption": ("전송계층이 길(라우팅) 자체를 정하진 않아요.", "The transport layer doesn't decide the route itself."),
         "small": ("가는 길 자체는 한 단계 아래(네트워크계층)에서 정해져요.", "The actual route is decided one layer below, by the network layer.")},
    ],
    "summary": (("<b>전송계층</b> = 동네(주소)까지 온 봉투를 <b>창구 번호(포트)</b>로 나누고, <b>등기(TCP)·일반우편(UDP)</b> 중 방식을 고르는 단계.",
                 "<b>The transport layer</b> = the stage that splits by <b>counter number (port)</b> and chooses between <b>registered (TCP)</b> and <b>plain (UDP)</b> mail."),
                ("전송계층(OSI 4계층)은 포트 번호로 같은 호스트 안의 여러 서비스를 구분하고, TCP(연결지향·신뢰성)나 UDP(비연결·속도) 중 하나로 데이터를 주고받으며, 필요하면 데이터를 세그먼트로 나누고 흐름·혼잡 제어로 수신 속도를 조절해요. 목적지(주소)를 정하는 네트워크계층과는 역할이 구분돼요.",
                 "The transport layer (OSI Layer 4) distinguishes multiple services on the same host by port number, exchanges data via either TCP (connection-oriented, reliable) or UDP (connectionless, fast), splits data into segments when needed, and regulates the receiving rate through flow and congestion control. Its role is distinct from the network layer, which decides the destination address.")),
    "glossary": [
        ("포트 번호", "Port Number", ("동네 안 몇 번 창구인지.", "Which counter inside the town."), ("같은 주소 안 서비스를 구분해요.", "Distinguishes services at the same address.")),
        ("TCP", "TCP", ("확인받고 보내는 등기 봉투.", "The registered envelope, confirmed before sending."), ("연결지향적이고 신뢰성이 높아요.", "Connection-oriented and highly reliable.")),
        ("UDP", "UDP", ("확인 없이 빠르게 보내는 일반 봉투.", "The plain envelope, sent fast with no confirmation."), ("비연결형이고 빠르지만 잃어버릴 수 있어요.", "Connectionless and fast, but can get lost.")),
        ("세그먼트", "Segment", ("전송계층에서 조각난 데이터 단위.", "The unit of data split at the transport layer."), ("패킷과 비슷하지만 이 계층만의 이름이에요.", "Similar to a packet, but this layer's own name for it.")),
        ("흐름·혼잡 제어", "Flow/Congestion Control", ("상대 속도에 맞춰 보내는 속도를 늦추는 것.", "Slowing the sending rate to match the other side."), ("등기(TCP)가 느려지는 이유 중 하나예요.", "One reason registered mail (TCP) can slow down.")),
        ("L4 스위치", "L4 Switch", ("포트까지 보고 창구를 나누는 분류 직원.", "The sorter who splits by counter, reading the port too."), ('이 계층의 정보를 실제로 활용하는 장비예요. → <a href="l4switch-ko.html">포트까지 보는 분류소 직원</a>', 'A device that actually uses this layer\'s information. → <a href="l4switch-en.html">the sorter who checks the port</a>')),
        ("네트워크계층(서브네팅)", "Network Layer (Subnetting)", ("동네(주소)를 정하는 한 단계 아래.", "One layer below, deciding the town (address)."), ('전송계층은 이 계층 위에서 동작해요. → <a href="subnetting-ko.html">동네를 작은 우편번호 구역으로 나누기</a>', "The transport layer operates on top of this one. → <a href=\"subnetting-en.html\">splitting the town into smaller zip-code zones</a>")),
        ("IPC(네트워크)", "Network IPC", ("포트로 상대를 특정하는 전용 편지함.", "The dedicated mailbox that picks its target by port."), ('전송계층의 포트 개념을 그대로 쓰는 예시예요. → <a href="ipc-ko.html">프로세스끼리 여는 전용 편지함</a>', 'A direct example of using this layer\'s port concept. → <a href="ipc-en.html">the dedicated mailbox between processes</a>')),
    ],
}
