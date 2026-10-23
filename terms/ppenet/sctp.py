from _draw import *
from _world import *


def truck(x, y, s=1.0, color="#4A5A72"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-14" width="34" height="22" rx="3" fill="{color}"/>'
            f'<rect x="12" y="-8" width="16" height="16" rx="2" fill="{color}"/>'
            f'<circle cx="-12" cy="10" r="5" fill="var(--night)"/><circle cx="18" cy="10" r="5" fill="var(--night)"/></g>')


# 1. 한 트럭에 소포·편지·등기를 다 실어서 보냄
P1 = svg(300, sky(300, ground=False)
         + truck(330, 160, 1.6)
         + label(330, 60, "⟦소포·편지·등기를 한 트럭에 다 실어요|a parcel, a letter, and registered mail all loaded on one truck⟧", 13, "var(--ink)")
         + person(600, 170, s=0.8, face=EYES, **CLERK)
         + label(600, 280, "⟦한 줄로 묶여서 가요|they travel bundled as a single line⟧", 11, "var(--muted)"))

# 2. 하나가 막히면 전부 막힘 (head-of-line blocking)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + truck(330, 150, 1.6, color="var(--bad)")
         + label(330, 70, "⟦소포 트럭이 사고로 멈췄어요|the parcel truck stalls after an accident⟧", 13, "var(--bad)")
         + label(330, 250, "⟦편지·등기까지 전부 같이 묶여서 멈춰요|the letter and registered mail stop right along with it⟧", 12, "var(--ink)", cls="d"))

# 3. 항목별 전용 차선 + 대체 도로 (hero)
LANES_Y = (90, 150, 210)
LANE_NAMES = (("⟦소포|parcel⟧"), ("⟦편지|letter⟧"), ("⟦등기|registered mail⟧"))
lane_svg = "".join(
    f'<rect x="120" y="{y - 16}" width="520" height="32" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
    + label(100, y + 5, name, 11, "var(--muted)", anchor="end")
    + truck(220 + i * 60, y, 0.9, color="var(--good)" if i != 0 else "var(--bad)")
    for i, (y, name) in enumerate(zip(LANES_Y, LANE_NAMES))
)
P3 = svg(300, '<rect width="760" height="300" fill="var(--sky)"/>'
         + f'<rect x="60" y="60" width="640" height="180" rx="10" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 48, "⟦하나의 배송 계약(association)|one delivery contract (association)⟧", 12, "var(--accent)", cls="d")
         + lane_svg
         + label(380, 270, "⟦소포 차선이 막혀도, 편지·등기 차선은 그대로 가요 = SCTP|the parcel lane jams, but the letter and registered-mail lanes keep moving — that's SCTP⟧", 13, "var(--ink)", cls="d"))

STREAM_I = icon('<rect x="8" y="14" width="48" height="8" rx="4" fill="var(--good)"/><rect x="8" y="28" width="48" height="8" rx="4" fill="var(--accent)"/><rect x="8" y="42" width="48" height="8" rx="4" fill="var(--bad)"/>')
BOX_I = icon('<rect x="14" y="16" width="36" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 16 L32 30 L50 16" stroke="#C9A86A" stroke-width="3" fill="none"/>')
ROAD_I = icon('<path d="M20 54 L28 10 H36 L44 54" fill="none" stroke="var(--ink)" stroke-width="4"/><path d="M32 18 v10 M32 36 v10" stroke="var(--accent)" stroke-width="3"/>')
CHECK2_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "sctp", "order": 25,
    "title": ("한 계약, 여러 개의 전용 차선", "One Contract, Many Dedicated Lanes"),
    "h1": ("<em>SCTP</em>가 뭐예요?", "What is <em>SCTP</em>?"),
    "sub": ("한 배송 계약 안에 항목별 전용 차선을 둬서, 하나가 막혀도 나머지는 그대로 가게 하는 이야기예요.",
            "A story about one delivery contract with a dedicated lane per item, so one jam doesn't stop everything else."),
    "panels": [
        {"svg": P1, "alt": ("소포, 편지, 등기가 모두 한 트럭에 실려 한 줄로 이동함", "A parcel, a letter, and registered mail are all loaded onto one truck, traveling as a single line"),
         "caption": ("여러 배송 항목을 한 트럭에 다 실어서 보내요.", "Several delivery items all get loaded onto one truck."),
         "small": ("한 줄로 묶여서 가요.", "They travel bundled together as one line.")},
        {"svg": P2, "alt": ("소포 트럭이 사고로 멈추자 같은 트럭에 실린 편지·등기까지 전부 멈춤", "The parcel truck stalls in an accident, and the letter and registered mail riding along stop with it"),
         "caption": ("하나가 막히면 전부 막혀요.", "If one stalls, everything stalls with it."),
         "small": ("한 줄로 묶여 있으면, 한 항목의 사고가 다른 항목까지 막아요.", "Bundled as one line, one item's accident blocks the others too.")},
        {"svg": P3, "hero": True, "alt": ("하나의 배송 계약 안에 소포·편지·등기 전용 차선이 따로 있어, 소포 차선이 막혀도 나머지는 그대로 감", "Inside one delivery contract, parcels, letters, and registered mail each get their own lane, so the others keep moving even when one jams"),
         "caption": ("SCTP = 하나의 계약 안에 항목별 전용 차선을 두는 거예요.", "SCTP = one contract containing a dedicated lane per item."),
         "small": ("소포 차선이 막혀도 편지·등기 차선은 그대로 가요.", "Even if the parcel lane jams, the letter and registered-mail lanes keep moving."),
         "tricks": (4, [
             (STREAM_I, ("스트림별 독립 배달", "Independent delivery per stream"), ("한 항목 지연이 다른 걸 안 막아요", "one item's delay doesn't block the rest"), "calm"),
             (BOX_I, ("메시지 경계 보존", "Preserves message boundaries"), ("우편물 한 통 단위로 딱 배달돼요", "delivered one whole piece at a time")),
             (ROAD_I, ("다중 경로(멀티호밍)", "Multiple paths (multi-homing)"), ("길이 끊기면 대체 도로로", "a backup road if one route is cut"), "warm"),
             (CHECK2_I, ("차선 안에서는 순서 보장", "Order kept within each lane"), ("그래도 배달 확인은 그대로예요", "delivery is still confirmed and ordered")),
         ])},
        {"svg": svg(320, sky(320)
                     + routemap(40, 40, 220, 250, "⟦TCP|TCP⟧", ("⟦한 줄(단일 스트림)|one line (single stream)⟧", "⟦막히면 전부 막힘|one jam blocks all⟧", "⟦신뢰성 있음|reliable⟧"), 1.0)
                     + routemap(270, 40, 220, 250, "⟦UDP|UDP⟧", ("⟦그냥 던지기|just send it⟧", "⟦확인 안 함|no confirmation⟧", "⟦빠르지만 분실 위험|fast but can be lost⟧"), 1.0)
                     + routemap(500, 40, 220, 250, "⟦SCTP|SCTP⟧", ("⟦차선별 독립|independent lanes⟧", "⟦멀티호밍|multi-homing⟧", "⟦신뢰성+병렬|reliable + parallel⟧"), 1.0, hl=0)),
         "alt": ("TCP(단일 스트림), UDP(확인 없음), SCTP(차선별 독립+멀티호밍)를 나란히 비교", "TCP (single stream), UDP (no confirmation), and SCTP (independent lanes + multi-homing) compared side by side"),
         "caption": ("TCP, UDP와 나란히 놓고 보면 차이가 보여요.", "Lined up next to TCP and UDP, the difference stands out."),
         "small": ("SCTP는 TCP의 신뢰성과, 막히지 않는 병렬성을 같이 가져가요.", "SCTP keeps TCP's reliability while adding lanes that don't block each other.")},
        {"svg": svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
                     + person(190, 130, s=0.8, face=SMILE, **CLERK) + label(190, 260, "⟦동시 송출엔 아주 유리해요|great for sending many items at once⟧", 11, "var(--ink)")
                     + person(570, 130, s=0.8, face=EYES, **CLERK) + label(570, 260, "⟦모든 우체국이 쓰는 건 아니에요|not every post office supports it⟧", 11, "var(--ink)")
                     + label(380, 305, "⟦좋은 설계지만, 인터넷 곳곳의 방화벽이 낯선 트럭을 막기도 해요|a good design, but firewalls across the internet often block this unfamiliar kind of truck⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: SCTP는 동시 송출에 유리함. 오른쪽: 모든 우체국이 지원하는 건 아님(방화벽 문제)", "Left: SCTP is great for sending many items at once. Right: not every post office supports it, due to firewall issues"),
         "caption": ("설계는 좋지만, 널리 쓰이진 않아요.", "It's well designed, but not widely deployed."),
         "small": ("방화벽·중간 장비 호환성 문제로, 실제로는 SIGTRAN 같은 특정 용도에 더 많이 쓰여요.", "Because of firewall and middlebox compatibility, it's mostly used in specific niches like SIGTRAN.")},
    ],
    "summary": (("<b>SCTP</b> = 하나의 연결(association) 안에 여러 <b>독립적인 스트림(차선)</b>을 두고, <b>다중 경로(멀티호밍)</b>로 안정성까지 챙긴 전송 프로토콜.",
                 "<b>SCTP</b> is a transport protocol that puts several <b>independent streams (lanes)</b> inside one connection (association) and adds <b>multi-homing</b> for extra reliability."),
                ("SCTP(Stream Control Transmission Protocol)는 TCP처럼 신뢰성 있고 순서가 보장되는 전송을 제공하면서도, 하나의 연결(association) 안에 여러 스트림을 둬서 한 스트림의 지연이 다른 스트림을 막는 head-of-line blocking을 피해요. 또 여러 IP 주소로 동시에 연결해(멀티호밍) 한 경로가 끊겨도 통신을 이어갈 수 있어요. 메시지 경계도 보존해, TCP처럼 바이트 스트림을 직접 잘라 쓸 필요가 없어요.",
                 "SCTP (Stream Control Transmission Protocol) gives reliable, ordered delivery like TCP, but within one association it supports multiple streams, so a delay on one stream doesn't cause head-of-line blocking for the others. It also supports multi-homing — connecting over several IP addresses at once — so communication survives even if one path fails. It preserves message boundaries too, unlike TCP's raw byte stream.")),
    "glossary": [
        ("SCTP", "SCTP", ("항목별로 나뉜 배송 계약.", "A delivery contract split into lanes."), ("전송 계층 프로토콜이에요.", "A transport-layer protocol.")),
        ("연결(Association)", "Association", ("배송 계약 전체.", "The delivery contract as a whole."), ("TCP의 \'연결\'에 해당해요.", "The SCTP equivalent of a TCP connection.")),
        ("스트림(Stream)", "Stream", ("항목별 전용 차선.", "A dedicated lane per item."), ("한 계약 안에 여러 개 둘 수 있어요.", "Several can exist inside one association.")),
        ("멀티호밍", "Multi-homing", ("대체 도로를 미리 마련해두는 것.", "Keeping a backup road ready in advance."), ("한 경로가 끊겨도 버텨요.", "Keeps things running even if one path fails.")),
        ("head-of-line blocking", "Head-of-Line Blocking", ("한 줄로 묶이면 하나가 전부를 막는 현상.", "When one line jams and blocks everything behind it."), ("SCTP가 스트림 분리로 피하는 문제예요.", "What SCTP avoids by splitting into streams.")),
        ("TCP와 차이", "Difference from TCP", ("TCP는 한 줄, SCTP는 여러 차선.", "TCP is one line; SCTP is many lanes."), ('둘 다 신뢰성은 챙겨요. → <a href="tcpudp-ko.html">등기봉투와 일반봉투</a>', 'Both still guarantee reliability where it matters. → <a href="tcpudp-en.html">the registered envelope and the plain one</a>')),
        ("UDP와 차이", "Difference from UDP", ("UDP는 확인 없이 던지기만 해요.", "UDP just sends without confirming."), ("SCTP는 신뢰성 있게 보내요.", "SCTP sends it reliably instead.")),
        ("SIGTRAN", "SIGTRAN", ("SCTP가 실제로 많이 쓰이는 전화망 신호 전달 용도.", "A telephony signaling use case where SCTP actually sees real use."), ("SCTP의 대표적인 실사용 예시예요.", "One of SCTP's best-known real deployments.")),
    ],
}
