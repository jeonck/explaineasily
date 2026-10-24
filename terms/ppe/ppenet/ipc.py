from _draw import *
from _world import *

# 1. 서로 다른 건물(프로세스)에 있는 두 사람이 일을 나눠 해야 함
P1 = svg(300, sky(300)
         + postoffice(180, 160, 0.75, "⟦건물 A|Building A⟧") + postoffice(560, 160, 0.75, "⟦건물 B|Building B⟧")
         + person(220, 220, s=0.6, face=FROWN, **SENDER) + person(520, 220, s=0.6, face=FROWN, **RECEIVER)
         + label(380, 40, "⟦서로 다른 건물에서 일하는 두 프로세스가 손발을 맞춰야 해요|two processes in different buildings must coordinate⟧", 12, "var(--ink)")
         + label(380, 270, "⟦소리쳐도 안 들려요 — 건물이 멀리 떨어져 있어요|shouting won't reach — the buildings are far apart⟧", 13, "var(--bad)"))

# 2. 그냥 아무 봉투나 던지면 분실·순서뒤섞임
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + envelope(260, 140, 0.6) + envelope(340, 170, 0.6) + envelope(420, 130, 0.6)
         + label(380, 70, "⟦아무렇게나 던지면 잃어버리거나 순서가 뒤섞여요|tossing them randomly, some get lost or arrive out of order⟧", 12, "var(--ink)")
         + person(600, 170, s=0.6, face=SWEAT + FROWN, **RECEIVER)
         + label(380, 270, "⟦건물 사이 전용 편지함이 없으면 생기는 일이에요|this happens without a dedicated mailbox between buildings⟧", 12, "var(--ink)"))

# 3. hero: 네트워크 IPC = 건물 사이에 여는 전용 편지함(소켓)
P3 = svg(340, sky(340)
         + postoffice(160, 140, 0.8, "⟦건물 A|Building A⟧") + postoffice(600, 140, 0.8, "⟦건물 B|Building B⟧")
         + envelope(380, 190, 0.8, registered=True)
         + label(380, 30, "⟦네트워크 IPC = 서로 다른 건물 사이에 여는 전용 편지함|network IPC = a dedicated mailbox opened between separate buildings⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦소켓이나 메시지 큐로, 건물이 멀리 있어도 손발을 맞춰요|via sockets or message queues — coordinating even across distant buildings⟧", 12, "var(--muted)"))

I1 = icon('<rect x="10" y="20" width="44" height="30" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="4"/><path d="M10 20 l22 18 l22 -18" fill="none" stroke="var(--accent)" stroke-width="4"/>')
I2 = icon('<rect x="8" y="42" width="12" height="14" fill="var(--good)"/><rect x="26" y="30" width="12" height="26" fill="var(--good)"/><rect x="44" y="18" width="12" height="38" fill="var(--good)"/>')
I3 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5" stroke-dasharray="8 6"/>')
I4 = icon('<rect x="10" y="22" width="44" height="22" rx="11" fill="var(--bad)"/><circle cx="20" cy="33" r="5" fill="#fff"/><circle cx="32" cy="33" r="5" fill="#fff"/><circle cx="44" cy="33" r="5" fill="#fff"/>')

# 4. 두 가지 편지함 방식: 소켓(실시간 통화) vs 메시지 큐(쌓아두고 나중에)
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦전용 편지함 두 방식|TWO MAILBOX STYLES⟧",
                    ("⟦소켓 — 전화처럼 실시간으로 계속 연결해 둬요|socket — stays connected live, like a phone call⟧",
                     "⟦메시지 큐 — 편지함에 쌓아두고 상대가 나중에 꺼내가요|message queue — notes pile up, picked up later⟧",
                     "⟦포트 번호 — 같은 건물 안 어느 창구인지 알려줘요|port number — tells which counter inside the building⟧",
                     "⟦TCP/UDP — 등기로 보낼지, 일반우편으로 보낼지 골라요|TCP/UDP — choose registered mail or plain mail⟧"), 1.0))

# 5. 로컬 IPC와는 달라요 — 네트워크 IPC는 멀리 있는 건물 사이
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + postoffice(140, 150, 0.6) + postoffice(230, 150, 0.6) + label(190, 240, "⟦같은 건물 안 부서끼리는 복도로 바로 전달해요|same-building teams just hand it across the hallway⟧", 10, "var(--ink)")
         + postoffice(520, 150, 0.6) + postoffice(680, 150, 0.6) + label(600, 240, "⟦멀리 떨어진 건물끼리는 이 전용 편지함이 필요해요|distant buildings need this dedicated mailbox instead⟧", 10, "var(--ink)")
         + label(380, 282, "⟦같은 건물 안 전달(로컬 IPC)과는 다른 이야기예요|that's a different story from hand-offs inside one building (local IPC)⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ipc", "order": 17,
    "title": ("멀리 떨어진 건물 사이에 여는 전용 편지함", "The Dedicated Mailbox Between Distant Buildings"),
    "h1": ("<em>IPC(네트워크 프로세스 간 통신)</em>이 뭐예요?", "What is <em>Network IPC</em>?"),
    "sub": ("네트워크 IPC를, 멀리 떨어진 건물 사이에 전용 편지함을 열어 손발을 맞추는 이야기로 풀어봤어요.",
            "Network IPC, told as a story about opening a dedicated mailbox between distant buildings so they can coordinate."),
    "panels": [
        {"svg": P1, "alt": ("서로 다른 건물에 있는 두 사람이 멀리 떨어져 일함", "Two people in separate buildings work far apart"),
         "caption": ("서로 다른 건물에서 일하는 두 프로세스가 손발을 맞춰야 해요.", "Two processes in different buildings must coordinate."),
         "small": ("소리쳐도 안 들려요 — 건물이 멀리 떨어져 있어요.", "Shouting won't reach — the buildings are far apart.")},
        {"svg": P2, "alt": ("봉투 세 개가 아무렇게나 떠 있고, 받는 사람이 땀을 흘리며 당황함", "Three envelopes float around randomly, and the receiver sweats, confused"),
         "caption": ("아무 봉투나 던지면 잃어버리거나 뒤섞여요.", "Tossing envelopes randomly, some get lost or jumbled."),
         "small": ("건물 사이 전용 편지함이 없으면 생기는 일이에요.", "This happens without a dedicated mailbox between buildings.")},
        {"svg": P3, "hero": True, "alt": ("두 건물 사이에 등기 봉투가 전용 편지함을 통해 오감", "A registered envelope travels through a dedicated mailbox between two buildings"),
         "caption": ("네트워크 IPC = 건물 사이에 여는 전용 편지함이에요.", "Network IPC = a dedicated mailbox opened between buildings."),
         "small": ("소켓이나 메시지 큐로, 멀리 있어도 손발을 맞춰요.", "Via sockets or message queues, even across distant buildings."),
         "tricks": (4, [
             (I1, ("소켓", "Socket"), ("실시간 통화 같은 연결", "a live, call-like connection")),
             (I2, ("메시지 큐", "Message Queue"), ("쌓아뒀다 나중에 꺼내요", "piles up, picked up later"), "calm"),
             (I3, ("포트 번호", "Port Number"), ("건물 안 창구를 지정해요", "picks the counter inside"), "warm"),
             (I4, ("TCP/UDP", "TCP/UDP"), ("등기냐 일반우편이냐", "registered or plain mail")),
         ])},
        {"svg": P4, "alt": ("전용 편지함 두 방식 안내판: 소켓, 메시지 큐, 포트 번호, TCP/UDP 네 줄", "A guide board listing socket, message queue, port number, and TCP/UDP for the dedicated mailbox"),
         "caption": ("편지함에도 두 가지 방식이 있어요.", "There are two mailbox styles."),
         "small": ("실시간 통화처럼 연결해두거나, 쌓아뒀다 나중에 꺼내가요.", "Stay connected live, or pile up and pick up later.")},
        {"svg": P5, "alt": ("왼쪽: 같은 건물 안 부서끼리는 복도로 바로 전달. 오른쪽: 먼 건물끼리는 전용 편지함이 필요", "Left: same-building teams hand off across the hallway. Right: distant buildings need the dedicated mailbox"),
         "caption": ("같은 건물 안 전달과는 다른 이야기예요.", "This is a different story from hand-offs inside one building."),
         "small": ("같은 건물 안 부서 간 전달(로컬 IPC)은 또 다른 이야기예요.", "Hand-offs between teams in the same building (local IPC) are a separate topic.")},
    ],
    "summary": (("<b>네트워크 IPC</b> = 멀리 떨어진 건물(서로 다른 컴퓨터의 프로세스) 사이에 <b>전용 편지함(소켓·메시지 큐)</b>을 열어 주고받는 일.",
                 "<b>Network IPC</b> = opening a <b>dedicated mailbox (socket, message queue)</b> between processes on separate machines, far apart."),
                ("네트워크를 통한 프로세스 간 통신(IPC)은 서로 다른 호스트에 있는 프로세스가 소켓이나 메시지 큐 같은 수단으로 데이터를 주고받는 방식이에요. 같은 컴퓨터 안 프로세스끼리 쓰는 공유 메모리·파이프 같은 로컬 IPC와 달리, 네트워크 IPC는 TCP/UDP와 포트 번호를 거쳐 원격지와 통신해요.",
                 "Network-based inter-process communication (IPC) lets processes on different hosts exchange data via sockets or message queues. Unlike local IPC mechanisms such as shared memory or pipes between processes on the same machine, network IPC goes through TCP/UDP and port numbers to reach a remote host.")),
    "glossary": [
        ("소켓", "Socket", ("실시간으로 연결해두는 전용 편지함.", "A dedicated mailbox kept live, like an open call."), ("IP와 포트로 상대를 특정해요.", "Identifies the other side by IP and port.")),
        ("메시지 큐", "Message Queue", ("쌓아뒀다 나중에 꺼내가는 편지함.", "A mailbox where notes pile up for later pickup."), ("보내는 쪽과 받는 쪽이 동시에 있지 않아도 돼요.", "Sender and receiver don't need to be present at once.")),
        ("포트 번호", "Port Number", ("건물 안 몇 번 창구인지.", "Which counter inside the building."), ("같은 주소 안에서 서비스를 구분해요.", "Distinguishes services at the same address.")),
        ("TCP/UDP", "TCP/UDP", ("등기 봉투와 일반 봉투.", "The registered envelope and the plain one."), ("이 세계의 두 기본 배송 방식이에요.", "The two basic shipping methods in this world.")),
        ("전송계층", "Transport Layer", ("포트와 등기·일반우편을 다루는 단계.", "The stage that handles ports and the registered/plain choice."), ('네트워크 IPC가 기대는 바로 그 계층이에요. → <a href="transportlayer-ko.html">포트를 나누고 신뢰도를 고르는 단계</a>', 'The very layer network IPC leans on. → <a href="transportlayer-en.html">the stage that splits ports and picks reliability</a>')),
        ("Modbus", "Modbus", ("산업 현장에서 쓰는 단순한 쪽지 규칙.", "A simple note rule used on factory floors."), ('이 전용 편지함 위에서 쓰이는 쪽지 규칙의 한 예예요. → <a href="modbus-ko.html">우체국장이 순서대로 묻는 쪽지 규칙</a>', 'One example of a note rule riding on this mailbox. → <a href="modbus-en.html">the note rule where the clerk asks one at a time</a>')),
        ("로컬 IPC(OS 수준)", "Local IPC (OS-level)", ("같은 건물 안 부서끼리 복도로 전달하는 방식.", "The way teams in the same building hand things across the hallway."), ("이건 다른 세계(PPE·시스템SW)에서 다루는, 건물 안 전달 이야기예요.", "That's a separate story, covered in another world (PPE Systems) — hand-offs inside one building.")),
        ("회선교환·패킷교환", "Circuit vs Packet Switching", ("편지가 실제로 오가는 길의 종류.", "What kind of road the note actually travels."), ('전용 편지함 아래 깔린 전송 방식이에요. → <a href="circuitpacket-ko.html">전용 도로냐, 조각내 보내기냐</a>', "The transport method underneath this dedicated mailbox. → <a href=\"circuitpacket-en.html\">a dedicated road, or splitting it into pieces</a>")),
    ],
}
