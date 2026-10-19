from _draw import *
from _world import *

# 1. 쉬지 않고 등기봉투를 계속 보내요
P1 = svg(300, sky(300)
         + person(220, 160, s=0.85, face=EYES, **CARRIER)
         + envelope(340, 140, 0.6, registered=True) + envelope(380, 170, 0.6, registered=True) + envelope(420, 200, 0.6, registered=True)
         + person(600, 170, s=0.85, face=SWEAT + EYES, **RECEIVER)
         + label(380, 30, "⟦집배원이 등기봉투를 쉬지 않고 계속 보내요|the carrier keeps sending registered envelopes without a pause⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦봉투가 찢어지고, 받는 집 우편함도 넘치고, 길도 막혀요|envelopes tear, the mailbox overflows, and the road jams⟧", 12, "var(--muted)"))

# 2. 셋 다 동시에 터지면 더 나빠져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + envelope(170, 160, 0.6) + '<path d="M150 150 l40 20 M190 150 l-40 20" stroke="var(--bad)" stroke-width="3"/>' + label(170, 220, "⟦훼손/분실|damaged or lost⟧", 11, "var(--ink)")
         + person(380, 160, s=0.75, face=SWEAT + EYES, **RECEIVER) + envelope(380, 220, 0.5) + envelope(400, 230, 0.5)
         + label(380, 260, "⟦우편함 넘침|mailbox overflowing⟧", 11, "var(--ink)")
         + '<rect x="540" y="230" width="180" height="20" fill="#8B5E3C"/>' + truck(600, 200, 0.5) + truck(650, 200, 0.5)
         + label(610, 260, "⟦길 전체가 막힘|the whole road jams⟧", 11, "var(--ink)"))

# 3. TCP 오류·흐름·혼잡 제어 = 등기 배송을 지키는 세 장치 (hero)
P3 = svg(340, sky(340)
         + person(260, 150, s=0.85, face=EYES, **CARRIER) + envelope(380, 140, 0.8, registered=True)
         + person(520, 180, s=0.85, face=SMILE, **RECEIVER)
         + label(380, 30, "⟦TCP 오류·흐름·혼잡 제어 = 등기 배송을 끝까지 안전하게 지키는 세 장치|TCP's error, flow, and congestion control = the three devices that guard a registered delivery to the end⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦잃어버리면 다시 보내고, 넘치면 늦추고, 막히면 수를 줄여요|resend what's lost, slow down if it's overflowing, cut back if it's jammed⟧", 12, "var(--muted)"))

# 4. 혼잡 제어 타임라인(점점 늘리다 줄이는 톱니)
P4 = svg(300, sky(300, ground=False)
         + '<path d="M60 220 L160 120 L162 200 L260 60 L262 210 L360 100 L362 190 L460 40" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + label(260, 30, "⟦보내는 트럭 수(혼잡 윈도)|number of trucks sent (congestion window)⟧", 12, "var(--ink)", cls="d")
         + label(160, 240, "⟦천천히 늘려요|slowly grows⟧", 10, "var(--muted)")
         + label(360, 240, "⟦막히면 뚝 줄여요|a jam cuts it sharply⟧", 10, "var(--muted)")
         + label(260, 280, "⟦늘렸다 줄이기를 반복하며 길이 버틸 수 있는 만큼만 보내요|grow then cut, again and again — sending only what the road can bear⟧", 12, "var(--ink)"))

# 5. 너무 조심하면 오히려 느려져요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **CARRIER) + label(190, 230, "⟦서류·결제는 이 세 장치 덕에 안전해요|papers and payments stay safe thanks to these three⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **CARRIER) + label(570, 230, "⟦실시간 영상은 이 장치들 때문에 오히려 느려져요|live video gets slower precisely because of these devices⟧", 11, "var(--ink)")
         + label(380, 282, "⟦손실 좀 봐도 되는 건 일반봉투(UDP)가 더 맞을 수 있어요|where a little loss is fine, the plain envelope (UDP) can be the better fit⟧", 12, "var(--ink)", cls="d"))

RESEND_I = icon('<path d="M46 20 a18 18 0 1 0 6 14" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M46 10 v12 h-12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
WINDOW_I = icon('<rect x="10" y="22" width="44" height="20" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><rect x="14" y="26" width="18" height="12" fill="var(--good)"/>')
SLOW_I = icon('<path d="M10 48 L22 30 L34 38 L46 16 L54 20" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
TIMEOUT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 20 v12 l8 8" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "tcpcontrol", "order": 7,
    "title": ("등기 배송을 끝까지 지키는 세 장치", "The Three Devices That Guard a Registered Delivery"),
    "h1": ("<em>TCP 오류·흐름·혼잡 제어</em>가 뭐예요?", "What is <em>TCP Error, Flow, and Congestion Control</em>?"),
    "sub": ("TCP의 오류·흐름·혼잡 제어를, 등기 배송이 끝까지 안전하도록 지켜주는 세 장치 이야기로 풀어봤어요.",
            "TCP's error, flow, and congestion control, told as a story about three devices guarding a registered delivery to the end."),
    "panels": [
        {"svg": P1, "alt": ("집배원이 쉬지 않고 등기봉투를 계속 보내고, 받는 사람은 땀을 흘림", "A carrier keeps sending registered envelopes nonstop, and the receiver starts to sweat"),
         "caption": ("쉬지 않고 등기봉투를 계속 보내요.", "The carrier keeps sending registered envelopes without a pause."),
         "small": ("봉투가 찢어지고, 우편함도 넘치고, 길도 막혀요.", "Envelopes tear, the mailbox overflows, and the road jams.")},
        {"svg": P2, "alt": ("봉투가 찢어지고, 우편함이 넘치고, 길에 트럭이 꽉 막힌 세 장면", "Three scenes: a torn envelope, an overflowing mailbox, and a road jammed with trucks"),
         "caption": ("셋 다 동시에 터지면 더 나빠져요.", "All three failing at once makes it worse."),
         "small": ("훼손·분실, 우편함 넘침, 길 전체 막힘이 한꺼번에 와요.", "Damage and loss, an overflowing mailbox, and a jammed road all arrive together.")},
        {"svg": P3, "hero": True, "alt": ("집배원과 받는 사람 사이에서 등기봉투가 안전하게 오가는 모습", "A registered envelope passing safely between a carrier and a smiling receiver"),
         "caption": ("등기 배송을 끝까지 지키는 세 장치예요.", "Three devices guard a registered delivery to the end."),
         "small": ("잃어버리면 다시 보내고, 넘치면 늦추고, 막히면 수를 줄여요.", "Resend what's lost, slow down if overflowing, cut back if jammed."),
         "tricks": (4, [
             (RESEND_I, ("오류 제어", "Error control"), ("확인이 없으면 다시 보내요(재전송)", "no acknowledgment means it gets resent"), "calm"),
             (WINDOW_I, ("흐름 제어", "Flow control"), ("받는 우편함 크기만큼만 보내요(윈도)", "sends only as much as the mailbox can hold (window)")),
             (SLOW_I, ("혼잡 제어", "Congestion control"), ("길이 막히면 보내는 수를 줄여요", "cuts back the count when the road jams"), "warm"),
             (TIMEOUT_I, ("타임아웃", "Timeout"), ("일정 시간 답이 없으면 다시 보내요", "no reply in time also triggers a resend")),
         ])},
        {"svg": P4, "alt": ("보내는 트럭 수가 천천히 늘다가 막히면 뚝 줄어드는 톱니 모양 그래프", "A sawtooth graph where the number of trucks sent slowly climbs, then drops sharply on a jam"),
         "caption": ("혼잡 윈도는 늘렸다 줄이기를 반복해요.", "The congestion window grows, then cuts, again and again."),
         "small": ("길이 버틸 수 있는 만큼만 천천히 늘리다가, 막히면 뚝 줄여요.", "It slowly grows only as much as the road can bear, then cuts sharply on a jam.")},
        {"svg": P5, "alt": ("왼쪽: 서류·결제는 세 장치 덕에 안전함. 오른쪽: 실시간 영상은 오히려 느려짐", "Left: papers and payments stay safe thanks to the three devices. Right: live video gets slower because of them"),
         "caption": ("너무 조심하면 오히려 느려져요.", "Too much caution can slow things down."),
         "small": ("손실 좀 봐도 되는 건 일반봉투(UDP)가 더 맞을 수 있어요.", "Where a little loss is fine, the plain envelope (UDP) can be the better fit.")},
    ],
    "summary": (("TCP는 <b>오류 제어(잃어버리면 재전송)</b>, <b>흐름 제어(받는 쪽 속도에 맞추기)</b>, <b>혼잡 제어(길 막히면 속도 줄이기)</b> 세 장치로 등기 배송을 끝까지 지켜요.",
                 "TCP guards a registered delivery to the end with three devices: <b>error control</b> (resend what's lost), <b>flow control</b> (match the receiver's pace), and <b>congestion control</b> (slow down when the road jams)."),
                ("오류 제어는 체크섬·ACK·재전송(timeout, 빠른 재전송)으로 손실·훼손을 복구하고, 흐름 제어는 수신 윈도(receive window)로 수신 측 버퍼가 넘치지 않게 송신 속도를 조절해요. 혼잡 제어는 네트워크 혼잡 자체를 추정해 혼잡 윈도(congestion window)를 slow start·congestion avoidance로 늘리고, 손실이 감지되면 줄이는 방식으로(AIMD) 전체 경로의 과부하를 막아요.",
                 "Error control recovers loss and corruption through checksums, ACKs, and retransmission (timeout, fast retransmit). Flow control uses the receive window to throttle the sender so the receiver's buffer never overflows. Congestion control estimates network congestion itself, growing the congestion window via slow start and congestion avoidance, then cutting it on detected loss (AIMD) to keep the whole path from overloading.")),
    "glossary": [
        ("오류 제어", "Error control", ("잃어버리거나 훼손되면 다시 보내는 장치.", "The device that resends what was lost or damaged."), ("체크섬과 확인응답(ACK)으로 알아차려요.", "Detected via checksum and acknowledgment (ACK).")),
        ("흐름 제어", "Flow control", ("받는 우편함 크기만큼만 보내는 장치.", "The device that sends only as much as the mailbox can hold."), ("수신 윈도 크기로 속도를 맞춰요.", "Matches pace to the receive window size.")),
        ("혼잡 제어", "Congestion control", ("길이 막히면 보내는 수를 줄이는 장치.", "The device that cuts the count when the road jams."), ("혼잡 윈도를 늘렸다 줄여요(AIMD).", "Grows then cuts the congestion window (AIMD).")),
        ("ACK", "ACK", ("잘 받았다는 확인 쪽지.", "The note confirming something arrived safely."), ("없으면 재전송이 시작돼요.", "Its absence is what triggers a resend.")),
        ("타임아웃·재전송", "Timeout/retransmission", ("일정 시간 답이 없으면 다시 보내는 규칙.", "The rule that resends when no reply comes in time."), ("오류 제어의 핵심 수단이에요.", "A core mechanism of error control.")),
        ("3-way 핸드셰이크", "3-way handshake", ("보내기 전 나누는 인사 세 번.", "The three greetings exchanged before anything is sent."), ('TCP가 제어 전에 먼저 거치는 절차예요. → <a href="tcpudp-ko.html">등기봉투와 일반봉투</a>', "The step TCP takes before any of this control begins. → <a href=\"tcpudp-en.html\">the registered envelope and the plain one</a>")),
        ("TCP/UDP", "TCP/UDP", ("등기봉투와 일반봉투.", "The registered envelope and the plain one."), ('이 세 장치는 등기봉투(TCP)에만 있어요. → <a href="tcpudp-ko.html">등기봉투와 일반봉투</a>', 'These three devices exist only in the registered envelope (TCP). → <a href="tcpudp-en.html">the registered envelope and the plain one</a>')),
        ("5G 네트워크 슬라이싱", "5G Network slicing", ("한 도로를 전용 차선으로 나누는 것.", "Splitting one road into dedicated lanes."), ('도로 전체가 막히면 차선 보장도 같이 흔들려요. → <a href="5gslicing-ko.html">도로를 차선으로 나누기</a>', "Lane guarantees shake too once the whole road jams. → <a href=\"5gslicing-en.html\">splitting the road into lanes</a>")),
    ],
}
