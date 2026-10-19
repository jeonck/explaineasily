from _draw import *
from _world import *

# 1. 등기로 보낼까, 일반으로 보낼까
P1 = svg(300, sky(300)
         + person(180, 160, s=0.85, face=EYES, **SENDER)
         + envelope(300, 150, 0.9, registered=True, text="⟦중요 서류|important paper⟧")
         + envelope(300, 230, 0.7, text="⟦실시간 영상|live video⟧")
         + person(560, 160, s=0.85, face=EYES, **RECEIVER)
         + label(380, 30, "⟦서류는 확실하게, 영상은 빠르게 — 봉투를 뭘로 쓸지 골라야 해요|a sure paper, a fast video — which envelope do you pick?⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦보내는 방법이 다르면 약속하는 방식도 달라야 해요|different goals need different ways of promising delivery⟧", 12, "var(--muted)"))

# 2. 확인받으면 느리고, 안 받으면 잃어버릴 수 있어요
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 160, s=0.8, face=SWEAT + EYES, **CARRIER) + envelope(190, 230, 0.6, registered=True)
         + label(190, 270, "⟦인사 세 번 주고받느라 느려요|three greetings exchanged first — slow⟧", 11, "var(--ink)")
         + person(570, 160, s=0.8, face=FROWN, **RECEIVER) + envelope(500, 230, 0.6)
         + label(570, 270, "⟦빠른데 중간에 잃어버려도 몰라요|fast — but if one goes missing, nobody notices⟧", 11, "var(--ink)"))

# 3. 등기봉투=TCP, 일반봉투=UDP (hero)
P3 = svg(340, sky(340)
         + envelope(260, 170, 1.1, registered=True, text="⟦등기 = TCP|Registered = TCP⟧")
         + envelope(500, 170, 1.1, text="⟦일반 = UDP|Plain = UDP⟧")
         + label(380, 30, "⟦등기봉투는 확인받으며 순서대로, 일반봉투는 확인 없이 빠르게|a registered envelope confirms and keeps order; a plain one skips the confirming and flies⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦둘 다 같은 길을 쓰지만, 약속하는 방식이 달라요|both use the same road — they just promise differently⟧", 12, "var(--muted)"))

# 4. TCP vs UDP 헤더 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦TCP 헤더(등기)|TCP header (registered)⟧",
                    ("⟦포트 번호 — 있음|port number — yes⟧",
                     "⟦순서 번호 — 있음|sequence number — yes⟧",
                     "⟦인사(핸드셰이크) — 3번|handshake — 3-way⟧",
                     "⟦연결 — 유지함|connection — kept open⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦UDP 헤더(일반)|UDP header (plain)⟧",
                    ("⟦포트 번호 — 있음|port number — yes⟧",
                     "⟦순서 번호 — 없음|sequence number — no⟧",
                     "⟦인사(핸드셰이크) — 없음|handshake — none⟧",
                     "⟦연결 — 매번 새로|connection — none, fresh each time⟧"), 1.0, hl=2))

# 5. 어느 쪽도 완벽한 정답은 아니에요
P5 = svg(300, '<rect width="760" height="300" fill="var(--good-soft)"/>'
         + person(220, 150, s=0.8, face=SMILE, **SENDER) + envelope(220, 220, 0.6, registered=True)
         + label(220, 265, "⟦서류·결제는 느려도 등기가 맞아요|paper and payments: slower, but registered is right⟧", 11, "var(--ink)")
         + person(540, 150, s=0.8, face=SMILE, **RECEIVER) + envelope(540, 220, 0.6)
         + label(540, 265, "⟦영상·게임은 조금 잃어버려도 일반이 맞아요|video and games: a little loss is fine — plain is right⟧", 11, "var(--ink)"))

HAND_I = icon('<circle cx="22" cy="32" r="10" fill="var(--accent)"/><circle cx="42" cy="32" r="10" fill="var(--good)"/><path d="M28 32 h8" stroke="var(--ink)" stroke-width="4"/>')
NUM_I = icon('<rect x="10" y="14" width="18" height="18" rx="3" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/>' + label(19, 27, "1", 13, "#142033") + '<rect x="36" y="32" width="18" height="18" rx="3" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/>' + label(45, 45, "2", 13, "#142033"))
STAMP_I = icon('<rect x="10" y="16" width="44" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="32" r="12" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M26 32 l4 5 l9 -11" stroke="var(--good)" stroke-width="3" fill="none"/>')
DOOR_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/>' + label(32, 36, "80", 14, "#142033", cls="d"))

PAGE = {
    "slug": "tcpudp", "order": 2,
    "title": ("등기봉투와 일반봉투", "The Registered Envelope and the Plain One"),
    "h1": ("<em>TCP/UDP</em>가 뭐예요?", "What is <em>TCP/UDP</em>?"),
    "sub": ("TCP와 UDP를, 확인받고 보내는 등기봉투와 확인 없이 빠른 일반봉투 이야기로 풀어봤어요.",
            "TCP and UDP, told as a story about a registered envelope that confirms delivery and a plain one that just flies."),
    "panels": [
        {"svg": P1, "alt": ("보내는 사람이 중요 서류는 등기로, 실시간 영상은 일반으로 보내길 고민함", "A sender weighs sending important papers registered and live video plain"),
         "caption": ("서류는 확실하게, 영상은 빠르게 보내고 싶어요.", "A sure delivery for papers, a fast one for video."),
         "small": ("보내는 방법이 다르면 약속하는 방식도 달라야 해요.", "Different goals need different ways of promising delivery.")},
        {"svg": P2, "alt": ("왼쪽: 집배원이 인사 세 번 주고받느라 땀을 흘림. 오른쪽: 받는 사람이 봉투 하나가 없어진 걸 모름", "Left: the carrier sweats through three rounds of greetings. Right: the receiver doesn't notice a missing envelope"),
         "caption": ("확인받으면 느리고, 안 받으면 잃어버릴 수 있어요.", "Confirming is slow; skipping it risks losing things."),
         "small": ("인사 세 번은 느리고, 확인 없는 빠름은 불안해요.", "Three greetings are slow; no confirmation at all is risky.")},
        {"svg": P3, "hero": True, "alt": ("등기봉투에 TCP, 일반봉투에 UDP 라벨이 붙어 나란히 놓임", "A registered envelope labeled TCP and a plain one labeled UDP, side by side"),
         "caption": ("등기봉투=TCP, 일반봉투=UDP예요.", "A registered envelope is TCP; a plain one is UDP."),
         "small": ("둘 다 같은 길을 쓰지만, 약속하는 방식이 달라요.", "Both use the same road — they just promise differently."),
         "tricks": (4, [
             (HAND_I, ("3단계 인사", "3-way handshake"), ("보내기 전에 인사를 세 번 나눠요", "three greetings before anything is sent"), "calm"),
             (NUM_I, ("순서 번호", "Sequence number"), ("번호표로 도착 순서를 맞춰요", "numbers let pieces be put back in order")),
             (STAMP_I, ("체크섬", "Checksum"), ("겉면 도장으로 훼손을 확인해요", "a stamp on the outside checks for damage"), "warm"),
             (DOOR_I, ("포트 번호", "Port number"), ("몇 호실로 갈지 정확히 적어요", "writes exactly which room number to deliver to")),
         ])},
        {"svg": P4, "alt": ("TCP 헤더와 UDP 헤더를 포트·순서번호·핸드셰이크·연결 유지 여부로 비교한 안내판", "A board comparing TCP and UDP headers by port, sequence number, handshake, and connection"),
         "caption": ("TCP 헤더엔 더 많은 게 적혀 있어요.", "A TCP header carries more fields."),
         "small": ("포트는 둘 다 있지만, 순서·인사·연결 유지는 TCP에만 있어요.", "Both have ports, but only TCP has sequencing, handshake, and a kept-open connection.")},
        {"svg": P5, "alt": ("왼쪽: 서류·결제는 등기(TCP)가 맞음. 오른쪽: 영상·게임은 일반(UDP)이 맞음", "Left: papers and payments suit registered (TCP). Right: video and games suit plain (UDP)"),
         "caption": ("어느 쪽도 완벽한 정답은 아니에요.", "Neither is the one right answer."),
         "small": ("서류·결제는 등기가, 영상·게임은 일반이 더 맞아요.", "Registered suits papers and payments; plain suits video and games.")},
    ],
    "summary": (("<b>TCP</b>는 <b>확인받으며 순서대로</b> 보내는 등기봉투, <b>UDP</b>는 <b>확인 없이 빠르게</b> 보내는 일반봉투예요.",
                 "<b>TCP</b> is the registered envelope that <b>confirms and keeps order</b>; <b>UDP</b> is the plain one that goes <b>fast, with no confirmation</b>."),
                ("TCP는 3-way 핸드셰이크로 연결을 맺고, 순서 번호·확인응답(ACK)·재전송으로 신뢰성을 보장하는 연결지향 프로토콜이에요. UDP는 연결 설정 없이 헤더가 가볍고 빨라, 손실을 조금 감수해도 되는 실시간 스트리밍·DNS 질의 등에 쓰여요.",
                 "TCP is a connection-oriented protocol: it establishes a connection via a 3-way handshake, then guarantees reliability through sequence numbers, ACKs, and retransmission. UDP skips connection setup entirely, keeping its header light and fast — used where a little loss is acceptable, like real-time streaming or DNS queries.")),
    "glossary": [
        ("TCP", "TCP", ("확인받으며 순서대로 가는 등기봉투.", "The registered envelope that confirms and keeps order."), ("신뢰성을 보장하는 대신 느려요.", "Trades speed for reliability.")),
        ("UDP", "UDP", ("확인 없이 빠르게 가는 일반봉투.", "The plain envelope that just goes fast."), ("가볍고 빠른 대신 잃어버릴 수 있어요.", "Light and fast, but can lose a piece.")),
        ("3-way 핸드셰이크", "3-way handshake", ("보내기 전 나누는 인사 세 번.", "The three greetings exchanged before anything is sent."), ("TCP만 이 절차를 거쳐요.", "Only TCP goes through this step.")),
        ("포트 번호", "Port number", ("집 안의 정확한 호실 번호.", "The exact room number inside the house."), ('누구에게 전달할지 구분하는 구멍이에요. → <a href="socket-ko.html">전용 우편함 구멍</a>', 'The dedicated hole that says exactly who gets it. → <a href="socket-en.html">the dedicated mailbox hole</a>')),
        ("오류·흐름·혼잡 제어", "Error/flow/congestion control", ("등기 배송을 끝까지 안전하게 지키는 세 장치.", "The three devices that keep a registered delivery safe to the end."), ('TCP가 쓰는 세부 장치예요. → <a href="tcpcontrol-ko.html">세 가지 안전장치</a>', "The fine-grained machinery TCP uses. → <a href=\"tcpcontrol-en.html\">the three safety devices</a>")),
        ("체크섬", "Checksum", ("봉투 겉면에 찍는 확인 도장.", "The confirming stamp on the envelope's outside."), ("훼손 여부를 간단히 검사해요.", "A quick check for whether the contents got damaged.")),
        ("DNS", "DNS", ("동네 주소록.", "The neighborhood address book."), ('UDP로 빠르게 질문하고 답받는 대표적인 예예요. → <a href="dns-ko.html">동네 주소록</a>', 'A classic example of a fast UDP question-and-answer. → <a href="dns-en.html">the neighborhood address book</a>')),
        ("소켓", "Socket", ("주소+호실로 만든 전용 통신 구멍.", "A dedicated hole made from an address plus a room number."), ('TCP든 UDP든 결국 이 구멍을 통해 주고받아요. → <a href="socket-ko.html">전용 우편함 구멍</a>', 'Whichever envelope you use, it all goes through this hole. → <a href="socket-en.html">the dedicated mailbox hole</a>')),
    ],
}
