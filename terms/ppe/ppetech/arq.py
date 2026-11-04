from _draw import *
from _world import *


def walkie(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-30" width="28" height="56" rx="6" fill="#4A5A72"/><rect x="-4" y="-40" width="8" height="12" fill="#2E3D57"/></g>'


def msgpacket(x, y, s=1.0, bad=False):
    fill = "var(--bad)" if bad else "var(--accent)"
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-12" width="36" height="24" rx="4" fill="{fill}"/>'
    if bad:
        out += '<path d="M-8 -6 l16 12 M8 -6 l-16 12" stroke="#fff" stroke-width="3"/>'
    else:
        out += '<path d="M-8 0 h16" stroke="#fff" stroke-width="3"/>'
    return out + '</g>'


# 1. 잡음 때문에 메시지가 깨져서 도착해요
P1 = svg(300, sky(300, ground=False)
         + walkie(160, 180, 1.2) + walkie(600, 180, 1.2)
         + msgpacket(380, 130, 1.3, bad=True)
         + label(380, 170, "⟦지지직…|krzzt…⟧", 14, "var(--bad)", cls="d")
         + label(380, 260, "⟦무전기로 보낸 메시지가 잡음 때문에 깨져서 도착했어요|the message sent by radio arrived garbled by noise⟧", 13, "var(--ink)")
         + label(380, 288, "⟦받는 쪽은 뭐가 틀렸는지도 몰라요|the receiver doesn't even know what's wrong⟧", 11, "var(--muted)"))

# 2. 통신선은 늘 깨끗하지 않아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + msgpacket(160, 150, 1.0) + msgpacket(300, 150, 1.0, bad=True) + msgpacket(440, 150, 1.0) + msgpacket(580, 150, 1.0, bad=True)
         + label(380, 230, "⟦잡음·충돌 때문에 메시지 몇 개는 중간에 깨져요|noise and collisions garble some messages along the way⟧", 12, "var(--ink)")
         + label(380, 265, "⟦깨진 메시지를 그냥 쓰면 틀린 내용대로 움직이게 돼요|acting on a garbled message means acting on wrong information⟧", 11, "var(--muted)"))

# 3. ARQ = 확인하고, 틀리면 다시 보내 달라고 요청 (hero)
P3 = svg(340, sky(340, ground=False)
         + walkie(160, 170, 1.2) + walkie(600, 170, 1.2)
         + msgpacket(380, 120, 1.2, bad=True)
         + label(380, 90, "⟦이 메시지가 깨졌어요!|this message is garbled!⟧", 12, "var(--bad)")
         + msgpacket(380, 230, 1.2, bad=False)
         + label(380, 260, "⟦다시 보내주세요 → 보낸 쪽이 다시 보내요|resend, please → the sender sends it again⟧", 12, "var(--good)")
         + label(380, 30, "⟦ARQ(자동 재전송 요청) = 받는 쪽이 메시지를 확인해, 틀리면 자동으로 다시 요청하는 방식|ARQ = the receiver checks each message and automatically asks for a resend if it's wrong⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦메시지가 제대로 올 때까지 확인과 재전송을 반복해요|checking and resending repeat until the message arrives intact⟧", 12, "var(--muted)"))

ARQ_STOP = icon('<rect x="10" y="26" width="20" height="14" rx="3" fill="var(--accent)"/><path d="M38 20 v24" stroke="var(--line)" stroke-width="3" stroke-dasharray="2 2"/><circle cx="48" cy="32" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/>')
ARQ_GOBACKN = icon('<rect x="6" y="26" width="12" height="12" fill="var(--accent)"/><rect x="20" y="26" width="12" height="12" fill="var(--bad)"/><rect x="34" y="26" width="12" height="12" fill="var(--bad)" opacity="0.6"/><rect x="48" y="26" width="12" height="12" fill="var(--bad)" opacity="0.6"/>')
ARQ_SELECTIVE = icon('<rect x="6" y="26" width="12" height="12" fill="var(--accent)"/><rect x="20" y="26" width="12" height="12" fill="var(--bad)"/><rect x="34" y="26" width="12" height="12" fill="var(--accent)"/><rect x="48" y="26" width="12" height="12" fill="var(--accent)"/>')
ARQ_CRC = icon('<rect x="14" y="16" width="36" height="24" rx="3" fill="var(--accent)"/><path d="M24 28 l6 6 l12 -12" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. 세 방식 비교
P4 = svg(360, sky(360, ground=False)
         + infoboard(20, 30, 270, 230, "⟦Stop-and-Wait|STOP-AND-WAIT⟧",
                     ("⟦한 개 보내고 확인 기다림|send one, wait for the OK⟧", "⟦단순하지만 느려요|simple, but slow⟧"), 1.3)
         + infoboard(389, 30, 270, 230, "⟦Go-Back-N / Selective Repeat|GO-BACK-N / SELECTIVE REPEAT⟧",
                     ("⟦확인 전에 여러 개를 이어 보내요|send many before any OK⟧",
                      "⟦Go-Back-N: 틀린 것부터 전부 재전송|Go-Back-N: resend bad one onward⟧",
                      "⟦Selective: 틀린 것만 재전송|Selective: resend only the bad one⟧",
                      "⟦Stop-and-Wait보다 빠르지만 복잡해요|faster than Stop-and-Wait, more complex⟧"), 1.3)
         + label(380, 345, "⟦빠른 방식일수록 보내는 쪽이 메시지를 더 많이 저장해 둬야 해요|the faster the method, the more messages the sender must keep in memory⟧", 12, "var(--ink)"))

# 5. 한계: 재전송은 지연을 늘려요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + msgpacket(190, 150, 1.3) + label(190, 260, "⟦파일은 늦어도 정확해야 해서 ARQ가 딱이에요|files may arrive late but must be exact, so ARQ fits⟧", 11, "var(--ink)")
         + person(570, 150, s=0.85, face=FROWN, **DEMO)
         + label(570, 260, "⟦실시간 음성·영상은 재전송을 기다리면 끊겨요|live voice/video stalls while waiting for a resend⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그래서 실시간 음성·영상은 깨진 메시지를 다시 받지 않고 버리기도 해요|so live voice and video often drop a garbled message instead of waiting for it⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "arq", "order": 10,
    "title": ("틀렸으니 다시 보내달라고 외치기", "Shouting 'Wrong — Send It Again!'"),
    "h1": ("<em>오류 제어(ARQ)</em>가 뭐예요?", "What is <em>Error Control (ARQ)</em>?"),
    "sub": ("ARQ를, 무전기로 주고받은 메시지가 깨지면 받는 쪽이 다시 보내달라고 요청하는 이야기로 풀어봤어요.",
            "ARQ, told as a story about a walkie-talkie message that arrives garbled, so the receiver asks for it to be sent again."),
    "panels": [
        {"svg": P1, "alt": ("무전기로 보낸 메시지가 잡음 때문에 깨져서 도착함", "A message sent by walkie-talkie arrives garbled by noise"),
         "caption": ("무전기로 보낸 메시지가 잡음 때문에 깨져서 도착했어요.", "The message sent by radio arrived garbled by noise."),
         "small": ("받는 쪽은 뭐가 틀렸는지도 몰라요.", "The receiver doesn't even know what's wrong.")},
        {"svg": P2, "alt": ("네 개의 메시지 중 두 개가 중간에 깨짐", "Two out of four messages are garbled along the way"),
         "caption": ("통신선에는 잡음이 끼어서 메시지가 깨질 때가 있어요.", "Communication lines pick up noise, so some messages get garbled."),
         "small": ("깨진 메시지를 그냥 쓰면 틀린 내용대로 움직이게 돼요.", "Acting on a garbled message means acting on wrong information.")},
        {"svg": P3, "hero": True, "alt": ("받는 쪽이 깨진 메시지를 확인하고 다시 보내달라고 요청하자 제대로 된 메시지가 다시 옴", "The receiver flags a garbled message and asks for a resend — a clean one arrives"),
         "caption": ("ARQ는 받는 쪽이 메시지를 확인해서, 틀리면 자동으로 다시 보내달라고 요청하는 방식이에요.", "ARQ means the receiver checks each message and, if it's wrong, automatically asks for a resend."),
         "small": ("메시지가 제대로 올 때까지 확인과 재전송을 반복해요.", "Checking and resending repeat until the message arrives intact."),
         "tricks": (4, [
             (ARQ_STOP, ("Stop-and-Wait", "Stop-and-Wait"), ("하나 보내고 확인 기다려요", "send one, then wait for confirmation"), "calm"),
             (ARQ_GOBACKN, ("Go-Back-N", "Go-Back-N"), ("틀린 것부터 그 뒤까지 전부 재전송", "resend the bad one and everything after it")),
             (ARQ_SELECTIVE, ("Selective Repeat", "Selective Repeat"), ("틀린 것만 골라 재전송", "resend only the bad ones")),
             (ARQ_CRC, ("체크섬/CRC로 검출", "Detect with checksum/CRC"), ("메시지가 틀렸는지 확인해요", "checks whether the message is wrong"), "warm"),
         ])},
        {"svg": P4, "alt": ("Stop-and-Wait와 Go-Back-N/Selective Repeat 방식을 비교하는 설명판", "A board comparing Stop-and-Wait with Go-Back-N and Selective Repeat"),
         "caption": ("빠른 방식일수록 보내는 쪽이 메시지를 더 많이 저장해 둬야 해요.", "The faster the method, the more messages the sender must keep in memory."),
         "small": ("Selective Repeat가 가장 효율적이지만 가장 복잡해요.", "Selective Repeat is the most efficient, and the most complex.")},
        {"svg": P5, "alt": ("왼쪽: 문서 전송엔 ARQ가 딱 맞음. 오른쪽: 실시간 영상엔 재전송이 오히려 나쁨", "Left: ARQ is great for file transfer. Right: for live video, resending is actually worse"),
         "caption": ("메시지를 다시 보내는 만큼 도착이 늦어져요.", "Every resend makes the message arrive later."),
         "small": ("그래서 실시간 음성·영상은 깨진 메시지를 다시 받지 않고 버리기도 해요.", "So live voice and video often drop a garbled message instead of waiting for it.")},
    ],
    "summary": (("<b>ARQ(자동 재전송 요청)</b>는 받는 쪽이 메시지를 <b>확인하고, 틀리면 자동으로 다시 보내달라고 요청</b>하는 오류 제어 방식이에요.",
                 "<b>ARQ (Automatic Repeat reQuest)</b> is an error-control method where the receiver <b>checks the message and automatically asks for a resend</b> when it's wrong."),
                ("ARQ는 체크섬/CRC로 오류를 검출한 뒤, 확인 응답(ACK/NACK)을 바탕으로 틀린 데이터를 재전송하는 방식이에요. Stop-and-Wait, Go-Back-N, Selective Repeat 세 방식이 대표적이고, 뒤로 갈수록 처리량은 좋아지지만 구현과 버퍼 관리가 복잡해져요. 재전송 자체가 지연을 늘리기 때문에, 실시간 음성·영상처럼 지연에 민감한 데이터는 오류 난 데이터를 그냥 버리거나 FEC(전진 오류 수정) 같은 다른 방식을 함께 써요.",
                 "ARQ detects errors with a checksum/CRC, then resends bad data based on acknowledgment responses (ACK/NACK). Stop-and-Wait, Go-Back-N, and Selective Repeat are the three classic variants — throughput improves down the list, at the cost of more complex implementation and buffer management. Because resending itself adds delay, delay-sensitive data like live voice or video often just drops the damaged data or pairs ARQ with other methods like FEC (forward error correction).")),
    "glossary": [
        ("ARQ", "ARQ", ("틀리면 다시 보내달라고 요청하는 방식.", "The method that asks for a resend when wrong."), ("확인 응답을 주고받으며 동작해요.", "Works by exchanging acknowledgments.")),
        ("Stop-and-Wait", "Stop-and-Wait", ("한 개 보내고 확인부터 기다리는 가장 단순한 방식.", "The simplest variant — send one, then wait."), ("단순하지만 느려요.", "Simple, but slow.")),
        ("Go-Back-N", "Go-Back-N", ("틀린 것부터 그 뒤까지 전부 다시 보내는 방식.", "Resends the bad one and everything after it."), ("Stop-and-Wait보다 빠르지만, 멀쩡한 메시지까지 다시 보내는 낭비가 있어요.", "Faster than Stop-and-Wait, but it wastes time resending good messages.")),
        ("Selective Repeat", "Selective Repeat", ("틀린 것만 골라서 다시 보내는 방식.", "Resends only the bad packets."), ("가장 효율적이지만 가장 복잡해요.", "Most efficient, but most complex.")),
        ("체크섬/CRC", "Checksum / CRC", ("메시지가 틀렸는지 확인하는 검사값.", "The check value that tells if a message is wrong."), ("ARQ가 재전송을 결정하는 근거예요.", "What ARQ uses to decide whether to resend.")),
        ("ACK/NACK", "ACK/NACK", ("'받았어요'와 '틀렸어요' 신호.", "The 'got it' and 'that's wrong' signals."), ("ARQ 동작의 핵심 신호예요.", "The core signals that drive ARQ.")),
        ("FEC(전진 오류 수정)", "Forward Error Correction", ("재전송 없이 오류를 고치는 다른 방식.", "A different approach that fixes errors without resending."), ("지연에 민감한 데이터에는 ARQ보다 잘 맞아요.", "Suits delay-sensitive data better than ARQ does.")),
        ("MEC", "MEC", ("지연을 줄이려고 사용자 가까이에서 계산하는 기술.", "Computing near the user to cut delay."), ('재전송 지연 자체를 줄이는 또 다른 접근이에요. → <a href="mec-ko.html">MEC 부스</a>', 'A different approach to shrinking the resend delay itself. → <a href="mec-en.html">the MEC booth</a>')),
    ],
}
