from _draw import *
from _world import *

# 1. 한 집에 여러 사람이 살아요
P1 = svg(330, sky(330)
         + postoffice(300, 170, 1.0, "⟦101호|Apt 101⟧")
         + person(220, 230, s=0.6, face=EYES, **RECEIVER) + person(300, 225, s=0.6, face=EYES, **SENDER) + person(380, 230, s=0.6, face=EYES, **CLERK)
         + envelope(560, 160, 0.8, text="⟦101호로!|to Apt 101!⟧")
         + label(380, 30, "⟦한 집에 여러 사람이 살아요, 편지가 오면 누구 것인지 몰라요|several people share one house — a letter arrives, but whose is it?⟧", 13, "var(--ink)", cls="d")
         + label(380, 315, "⟦집 주소만으론 몇 호에 사는 누구인지 구분이 안 돼요|the house address alone can't tell apart who's inside⟧", 12, "var(--muted)"))

# 2. 여러 프로그램이 동시에 통신하면 뒤섞여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + postoffice(380, 160, 0.9)
         + envelope(280, 230, 0.55) + envelope(380, 240, 0.55) + envelope(480, 230, 0.55)
         + '<path d="M300 220 l40 20 M460 220 l-40 20" stroke="var(--bad)" stroke-width="3"/>'
         + label(380, 282, "⟦여러 프로그램이 동시에 주고받으면 편지가 뒤섞여요|several programs talking at once get their letters tangled⟧", 12, "var(--ink)", cls="d"))

# 3. 소켓 = 집주소+호실번호로 만든 전용 구멍 (hero)
P3 = svg(340, sky(340)
         + postoffice(220, 170, 0.8, "⟦IP: 1.2.3.4|IP: 1.2.3.4⟧")
         + postoffice(540, 170, 0.8, "⟦IP: 5.6.7.8|IP: 5.6.7.8⟧")
         + '<rect x="190" y="150" width="60" height="22" rx="4" fill="var(--accent)"/>' + label(220, 166, "⟦:80|:80⟧", 11, "#fff", cls="d")
         + '<rect x="510" y="150" width="60" height="22" rx="4" fill="var(--good)"/>' + label(540, 166, "⟦:443|:443⟧", 11, "#fff", cls="d")
         + '<path d="M280 200 Q380 150 500 200" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'
         + label(380, 30, "⟦소켓 = 집주소(IP)+호실번호(포트)로 만든, 이 대화 전용 구멍|a socket = a hole made from a house address (IP) plus a room number (port), dedicated to this one conversation⟧", 13, "var(--ink)", cls="d")
         + label(380, 322, "⟦구멍 하나가 한 쌍의 연결을 통째로 책임져요|one hole handles exactly one pairing, start to finish⟧", 12, "var(--muted)"))

# 4. 소켓 구조도
P4 = svg(300, sky(300, ground=False)
         + routemap(40, 30, 340, 230, "⟦보내는 쪽 소켓|Sender socket⟧", ("⟦IP: 1.2.3.4|IP: 1.2.3.4⟧", "⟦포트: 51234|port: 51234⟧"), 1.0)
         + routemap(400, 30, 340, 230, "⟦받는 쪽 소켓|Receiver socket⟧", ("⟦IP: 5.6.7.8|IP: 5.6.7.8⟧", "⟦포트: 443|port: 443⟧"), 1.0, hl=1))

# 5. 소켓은 구멍일 뿐, 등기냐 일반이냐는 또 다른 선택이에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + envelope(190, 160, 0.7, registered=True) + label(190, 240, "⟦같은 구멍으로 등기봉투(TCP)도 보내고|the same hole can send a registered envelope (TCP)⟧", 11, "var(--ink)")
         + envelope(570, 160, 0.7) + label(570, 240, "⟦같은 구멍으로 일반봉투(UDP)도 보내요|or a plain one (UDP), through that same hole⟧", 11, "var(--ink)")
         + label(380, 282, "⟦소켓은 구멍일 뿐, 어떤 봉투를 쓸지는 다른 선택이에요|a socket is just the hole — which envelope to use is a separate choice⟧", 12, "var(--ink)", cls="d"))

ADDR_I = icon('<path d="M32 10 L54 26 V54 H10 V26 Z" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><rect x="24" y="36" width="16" height="18" fill="var(--accent)"/>')
ROOM_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/>' + label(32, 38, "80", 16, "#142033", cls="d"))
HOLE_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--accent)" stroke-width="5"/><circle cx="32" cy="32" r="6" fill="var(--night)"/>')
DOOR2_I = icon('<rect x="18" y="10" width="28" height="44" rx="3" fill="var(--good)"/><circle cx="40" cy="32" r="3" fill="#fff"/>')

PAGE = {
    "slug": "socket", "order": 10,
    "title": ("이 대화만을 위한 전용 우편함 구멍", "The Mailbox Hole Just for This One Conversation"),
    "h1": ("<em>소켓</em>이 뭐예요?", "What is a <em>Socket</em>?"),
    "sub": ("소켓 통신을, 집주소와 호실번호로 만든 전용 우편함 구멍 이야기로 풀어봤어요.",
            "Socket communication, told as a story about a dedicated mailbox hole made from a house address and a room number."),
    "panels": [
        {"svg": P1, "alt": ("한 집에 여러 사람이 살고, 편지가 왔는데 누구 것인지 알 수 없음", "Several people share one house, and a letter arrives with no way to tell whose it is"),
         "caption": ("한 집에 여러 사람이 살아요.", "Several people share one house."),
         "small": ("집 주소만으론 몇 호에 사는 누구인지 구분이 안 돼요.", "The house address alone can't tell apart who's inside.")},
        {"svg": P2, "alt": ("한 우체국에서 여러 편지가 동시에 오가며 뒤섞임", "Several letters at one post office cross paths and get tangled"),
         "caption": ("여러 프로그램이 동시에 통신하면 뒤섞여요.", "Several programs talking at once get tangled."),
         "small": ("주소만으론 어느 대화가 어느 것인지 알 수 없어요.", "The address alone can't tell which conversation is which.")},
        {"svg": P3, "hero": True, "alt": ("두 우체국이 각각 IP와 포트 번호 꼬리표를 달고 점선으로 연결됨", "Two post offices, each tagged with an IP and port number, linked by a dashed line"),
         "caption": ("소켓은 집주소와 호실번호로 만든 전용 구멍이에요.", "A socket is a dedicated hole made from an address and a room number."),
         "small": ("구멍 하나가 한 쌍의 연결을 통째로 책임져요.", "One hole handles exactly one pairing, start to finish."),
         "tricks": (4, [
             (ADDR_I, ("IP 주소", "IP address"), ("어느 집인지 알려줘요", "says which house it is"), "calm"),
             (ROOM_I, ("포트 번호", "Port number"), ("몇 호실인지 알려줘요", "says which room number"), ),
             (HOLE_I, ("전용 구멍", "A dedicated hole"), ("연결마다 따로 생겨요", "a fresh hole for each connection"), "warm"),
             (DOOR2_I, ("열고 닫기", "Open and close"), ("통신 시작할 때 만들고 끝나면 치워요", "made when talk begins, removed when it ends")),
         ])},
        {"svg": P4, "alt": ("보내는 쪽 소켓(IP와 포트)과 받는 쪽 소켓(IP와 포트)을 나란히 적은 안내판", "A board listing the sender's socket (IP, port) and the receiver's socket (IP, port) side by side"),
         "caption": ("소켓은 양쪽 끝에 하나씩 있어요.", "A socket sits at each end."),
         "small": ("보내는 쪽 IP+포트, 받는 쪽 IP+포트가 한 쌍으로 연결을 이뤄요.", "The sender's IP+port and the receiver's IP+port together form the connection.")},
        {"svg": P5, "alt": ("같은 소켓 구멍으로 등기봉투(TCP)도, 일반봉투(UDP)도 보낼 수 있음", "The same socket hole can send either a registered envelope (TCP) or a plain one (UDP)"),
         "caption": ("소켓은 구멍일 뿐, 봉투 선택은 따로예요.", "A socket is just the hole — the envelope choice is separate."),
         "small": ("같은 구멍으로 등기봉투(TCP)도, 일반봉투(UDP)도 보낼 수 있어요.", "The same hole can send a registered envelope (TCP) or a plain one (UDP).")},
    ],
    "summary": (("<b>소켓</b>은 <b>IP 주소(어느 집)와 포트 번호(몇 호실)</b>로 만든, <b>한 쌍의 대화만을 책임지는 전용 우편함 구멍</b>이에요.",
                 "A <b>socket</b> is a <b>dedicated mailbox hole</b> made from an <b>IP address (which house) and a port number (which room)</b>, responsible for exactly one pairing of talk."),
                ("소켓은 운영체제가 네트워크 통신을 위해 제공하는 종단점(endpoint)으로, IP 주소+포트 번호의 조합(소켓 주소)으로 식별돼요. 프로그램은 소켓을 열어(bind/connect) 데이터를 읽고 쓰며, TCP 소켓이면 연결 지향, UDP 소켓이면 비연결형으로 동작해요. 한 호스트 안의 여러 프로그램이 같은 IP를 쓰더라도 포트 번호가 다르면 서로 다른 소켓으로 구분돼요.",
                 "A socket is the endpoint the operating system provides for network communication, identified by the combination of an IP address and a port number (the socket address). A program opens a socket (bind/connect) to read and write data — a TCP socket behaves connection-oriented, a UDP socket connectionless. Multiple programs on the same host sharing one IP are still told apart as long as their port numbers differ.")),
    "glossary": [
        ("소켓", "Socket", ("집주소+호실번호로 만든 전용 구멍.", "A dedicated hole made from an address and a room number."), ("한 쌍의 연결을 책임져요.", "Responsible for exactly one connection.")),
        ("IP 주소", "IP address", ("집 주소.", "The house address."), ("어느 컴퓨터인지를 가리켜요.", "Points to which computer it is.")),
        ("포트 번호", "Port number", ("집 안의 호실 번호.", "The room number inside the house."), ("어느 프로그램인지를 가리켜요.", "Points to which program it is.")),
        ("TCP/UDP", "TCP/UDP", ("등기봉투와 일반봉투.", "The registered envelope and the plain one."), ('소켓이라는 구멍으로 어떤 봉투를 쓸지 고르는 거예요. → <a href="tcpudp-ko.html">등기봉투와 일반봉투</a>', 'Choosing which envelope to send through the socket hole. → <a href="tcpudp-en.html">the registered envelope and the plain one</a>')),
        ("bind/connect", "bind/connect", ("소켓 구멍을 만들고 상대와 잇는 절차.", "The steps that open the hole and link it to the other side."), ("소켓을 쓰기 전 거치는 과정이에요.", "The setup step before a socket can be used.")),
        ("포트 충돌", "Port conflict", ("이미 쓰는 호실을 또 쓰려는 것.", "Trying to use a room number that's already taken."), ("같은 호실은 중복으로 못 써요.", "The same room number can't be reused at once.")),
        ("방화벽", "Firewall", ("문이 많은 성벽.", "A wall with many doors."), ('특정 포트(호실)만 열어두는 식으로 소켓 접근을 막기도 해요. → <a href="firewall-ko.html">문이 많은 성벽</a>', "Sometimes blocks socket access by keeping only certain ports open. → <a href=\"firewall-en.html\">the wall with many doors</a>")),
        ("IPv6", "IPv6", ("훨씬 길어진 새 집 주소 체계.", "The far longer new house-address system."), ('소켓 주소의 집 부분(IP)이 이 체계로 바뀌어 가요. → <a href="ipv6-ko.html">끝없이 늘어난 새 번지수</a>', "The house part of a socket address is moving to this system. → <a href=\"ipv6-en.html\">the new, nearly endless address system</a>")),
    ],
}
