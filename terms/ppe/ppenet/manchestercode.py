"""맨체스터 부호화 — 우체국 사이 전선 위의 신호 규칙(OSI 1계층)."""
from _draw import *
from _world import *


def grid(xs, y0=15, y1=115):
    return "".join(f'<path d="M{x} {y0} V{y1}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 3"/>' for x in xs)


def clock(x, y, hand):
    return (f'<circle cx="{x}" cy="{y}" r="24" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/>'
            f'<path d="M{x} {y} v-16 M{x} {y} {hand}" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>')


# 비트열 1 0 1 1 0. 위 y=40, 아래 y=90. 맨체스터는 IEEE 802.3 규칙(올라가면 1, 내려가면 0).
NRZ_PATH = "M130 40 L230 40 L230 90 L330 90 L330 40 L530 40 L530 90 L630 90"
MANCH_PATH = "M130 90 L180 90 L180 40 L230 40 L280 40 L280 90 L330 90 L380 90 L380 40 L430 40 L430 90 L480 90 L480 40 L530 40 L580 40 L580 90 L630 90"
BOUNDS = (130, 230, 330, 430, 530, 630)
MIDS = (180, 280, 380, 480, 580)

TRANS_I = icon('<path d="M20 44 V12 M20 12 l-8 8 M20 12 l8 8" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 20 V52 M44 52 l-8 -8 M44 52 l8 -8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
DIR_I = icon('<path d="M16 46 V18" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M10 24 l6 -6 l6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M48 18 V46" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M42 40 l6 6 l6 -6" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BALANCE_I = icon('<path d="M32 14 V50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 H50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 l-6 14 h12z" fill="var(--accent)"/><path d="M50 24 l-6 14 h12z" fill="var(--good)"/>')

# 1. 봉투 내용은 전선 위에서 높고 낮은 신호로 가요
P1 = svg(300, sky(300)
         + label(380, 26, "⟦봉투 내용은 우체국 사이 전선에서 높고 낮은 신호로 바뀌어 가요|between post offices, an envelope's contents travel the wire as high and low signals⟧", 12, "var(--ink)", cls="d")
         + postoffice(90, 112, 0.8, "⟦보내는 우체국|Sending Office⟧") + postoffice(670, 112, 0.8, "⟦받는 우체국|Receiving Office⟧")
         + '<rect x="130" y="100" width="500" height="30" rx="6" fill="#0A1120"/>'
         + '<path d="M145 115 H615" stroke="var(--accent)" stroke-width="4"/>' + label(380, 92, "⟦신호선: 0 1 0 1 1 ...?|the wire: 0 1 0 1 1 ...?⟧", 12, "var(--muted)")
         + person(520, 148, s=0.8, face=EYES, **SORTER)
         + bubble(150, 162, 330, 44, "⟦비트 하나가 어디서 끝나는지 어떻게 알아요?|how do I tell where one bit ends and the next begins?⟧", 11, "var(--panel)", "var(--line)", "right")
         + label(380, 280, "⟦전선 신호만 봐서는 비트 하나의 길이를 알 수 없어요|the wire signal alone doesn't show how long one bit is⟧", 13, "var(--ink)", cls="d"))

# 2. 같은 값이 계속되면 더 헷갈려요
P2 = svg(330, '<rect width="760" height="330" fill="var(--bad-soft)"/>'
         + label(380, 40, "⟦1 1 1 1 1 1 … 몇 개죠?|1 1 1 1 1 1 … how many is that?⟧", 13, "var(--bad)", cls="d")
         + '<rect x="130" y="55" width="500" height="50" rx="6" fill="#0A1120"/>'
         + '<path d="M150 80 H610" stroke="var(--bad)" stroke-width="4"/>'
         + clock(110, 180, "l10 8") + label(110, 228, "⟦보내는 우체국 시계|sender's clock⟧", 11, "var(--ink)")
         + clock(650, 180, "l13 -2") + label(650, 228, "⟦받는 우체국 시계|receiver's clock⟧", 11, "var(--ink)")
         + person(358, 130, s=0.8, face=SWEAT + EYES, **SORTER)
         + label(380, 262, "⟦신호가 평평하면 시계로 재서 개수를 세야 해요|with a flat signal, the only way to count is by the clock⟧", 12, "var(--ink)")
         + label(380, 305, "⟦보내는 쪽과 받는 쪽의 시계가 조금만 어긋나도 개수를 잘못 세요|if the sender's and receiver's clocks drift even a little, the count comes out wrong⟧", 12, "var(--ink)", cls="d"))

# 3. 맨체스터 부호화 = 비트 한가운데서 항상 신호를 뒤집는 약속 (hero)
P3 = svg(375, sky(375, ground=False)
         + label(380, 26, "⟦맨체스터 부호화 = 비트 한가운데서 항상 신호를 뒤집는 약속|Manchester encoding = a rule that always flips the signal at the middle of every bit⟧", 13, "var(--ink)", cls="d")
         + grid(BOUNDS, 55, 125) + f'<path d="{MANCH_PATH}" transform="translate(0,15)" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + "".join(f'<path d="M{m} 38 v10" stroke="var(--good)" stroke-width="3"/><path d="M{m - 5} 44 l5 6 l5 -6" fill="none" stroke="var(--good)" stroke-width="2.5"/>' for m in MIDS)
         + label(380, 150, "⟦점선=비트 경계, 초록 화살표=비트 한가운데(항상 신호가 뒤집혀요)|dashed line = bit boundary, green arrow = the bit's midpoint (always a flip)⟧", 11, "var(--muted)")
         + '<path d="M210 250 H550" stroke="var(--accent)" stroke-width="4"/>'
         + person(358, 170, s=1.0, face=SMILE + EYES, **SORTER)
         + postoffice(170, 240, 0.8, "⟦보내는 우체국|Sending Office⟧") + postoffice(590, 240, 0.8, "⟦받는 우체국|Receiving Office⟧")
         + label(380, 320, "⟦받는 우체국은 이 뒤집힘에 맞춰 시계를 계속 고쳐요|the receiving office keeps correcting its clock to these flips⟧", 12, "var(--ink)")
         + label(380, 355, "⟦그래서 박자를 알려주는 전선을 따로 깔지 않아도 돼요|so no separate wire is needed to carry the beat⟧", 12, "var(--muted)"))

# 4. 일반 신호(NRZ) vs 맨체스터 부호화
P4 = svg(300, '<rect width="760" height="300" fill="var(--panel)"/>'
         + label(380, 26, "⟦같은 비트 1 0 1 1 0 을 보냈을 때|sending the same bits: 1 0 1 1 0⟧", 13, "var(--ink)", cls="d")
         + label(130, 55, "⟦일반 신호(NRZ)|PLAIN SIGNAL (NRZ)⟧", 11, "var(--muted)", "start")
         + grid(BOUNDS, 65, 125) + f'<path d="{NRZ_PATH}" transform="translate(0,30)" stroke="var(--muted)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + label(130, 160, "⟦맨체스터 부호화|MANCHESTER ENCODING⟧", 11, "var(--muted)", "start")
         + grid(BOUNDS, 170, 230) + f'<path d="{MANCH_PATH}" transform="translate(0,130)" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + label(380, 275, "⟦같은 값이 이어져도(1,1) 맨체스터는 비트 중간에서 꼭 한 번 바뀌어요|even for repeated bits (1,1), Manchester still flips once at each bit's middle⟧", 12, "var(--ink)", cls="d"))

# 5. 한계 — 신호 변화가 두 배로 빨라야 해요
P5 = svg(270, '<rect width="380" height="270" fill="var(--bad-soft)"/><rect x="380" width="380" height="270" fill="var(--accent-soft)"/>'
         + person(166, 70, s=0.8, face=SWEAT + EYES, **SORTER)
         + label(190, 195, "⟦같은 비트 속도에 신호 변화는 NRZ의 두 배가 필요해요|same bit rate, but the signal must change twice as fast as NRZ⟧", 11, "var(--bad)")
         + truck(570, 125, 1.2, fast=True)
         + label(570, 195, "⟦그래서 더 빠른 이더넷은 다른 부호화를 써요|so faster Ethernet uses other encodings⟧", 11, "var(--ink)")
         + label(380, 245, "⟦맨체스터 부호화는 OSI 1계층(물리), 우체국 사이 전선 위의 규칙이에요|Manchester encoding is an OSI layer 1 (physical) rule for the wire between post offices⟧", 11, "var(--ink)", cls="d"))

PAGE = {
    "slug": "manchestercode", "order": 26,
    "title": ("우체국 전선에 박자까지 싣는 신호", "The Wire Signal That Carries Its Own Beat"),
    "h1": ("<em>맨체스터 부호화</em>가 뭐예요?", "What is <em>Manchester Encoding</em>?"),
    "sub": ("맨체스터 부호화를, 우체국 사이 전선에서 비트 한가운데마다 신호를 뒤집어 박자까지 함께 보내는 이야기로 풀어봤어요.",
            "Manchester encoding, told as a story about the wire between post offices, where the signal flips in the middle of every bit so the beat travels along with the data."),
    "panels": [
        {"svg": P1, "alt": ("두 우체국을 잇는 전선 앞에서 분류소 직원이 비트 하나가 어디서 끝나는지 묻는 장면", "A sorter by the wire between two post offices asks where one bit ends and the next begins"),
         "caption": ("봉투 내용은 우체국 사이 전선에서 높고 낮은 신호로 바뀌어 가요.", "Between post offices, an envelope's contents travel the wire as high and low signals."),
         "small": ("전선 신호만 봐서는 비트 하나의 길이를 알 수 없어요.", "The wire signal alone doesn't show how long one bit is.")},
        {"svg": P2, "alt": ("평평한 신호 앞에서 분류소 직원이 1이 몇 개인지 몰라 땀을 흘리고, 양쪽 우체국 시계가 조금 어긋나 있음", "A sorter sweats over a flat signal, unable to count the 1s, while the two post offices' clocks disagree slightly"),
         "caption": ("같은 값이 계속되면 신호가 안 바뀌어서 비트 개수를 세기 더 어려워요.", "When the same value repeats, the signal stays flat, so counting bits gets even harder."),
         "small": ("보내는 쪽과 받는 쪽의 시계가 조금만 어긋나도 개수를 잘못 세요.", "If the sender's and receiver's clocks drift even a little, the count comes out wrong.")},
        {"svg": P3, "hero": True, "alt": ("비트 한가운데마다 초록 화살표로 표시된 신호 전환이 있는 파형 아래에 분류소 직원과 두 우체국이 있음", "A waveform with a green arrow marking a flip at the middle of every bit, above a sorter and two post offices"),
         "caption": ("맨체스터 부호화는 비트 한가운데서 항상 신호를 뒤집는 약속이에요.", "Manchester encoding is a rule that always flips the signal at the middle of every bit."),
         "small": ("받는 우체국은 이 뒤집힘에 맞춰 시계를 고치니, 박자를 알려주는 전선을 따로 깔지 않아도 돼요.", "The receiving office corrects its clock to these flips, so no separate wire is needed to carry the beat."),
         "tricks": (4, [
             (TRANS_I, ("비트마다 꼭 한 번 중간 전환", "One mid-bit flip, every bit"), ("경계가 아니라 비트 중간에서요", "at the bit's middle, not its edge"), "calm"),
             (DIR_I, ("방향으로 0/1 구분", "Direction marks 0/1"), ("이 그림은 IEEE 802.3 규칙: 올라가면 1, 내려가면 0", "this picture follows IEEE 802.3: up means 1, down means 0")),
             (CLOCK_I, ("신호로 박자 복원", "Recovers the beat"), ("자기동기화(self-clocking)", "self-clocking"), "warm"),
             (BALANCE_I, ("신호 위아래가 고르게", "Signal balanced high and low"), ("비트마다 높은 시간과 낮은 시간이 같아요", "every bit spends equal time high and low")),
         ])},
        {"svg": P4, "alt": ("같은 비트열 1 0 1 1 0을 일반 신호(NRZ)와 맨체스터 부호화로 각각 그린 파형 비교", "Comparing the same bits 1 0 1 1 0 drawn as a plain (NRZ) signal and as Manchester encoding"),
         "caption": ("같은 비트를 보내도 일반 신호는 평평한 구간이 길고, 맨체스터는 비트마다 바뀌어요.", "For the same bits, a plain signal has long flat stretches, while Manchester flips in every bit."),
         "small": ("같은 값이 이어져도(1,1) 맨체스터는 비트 중간에서 꼭 한 번 바뀌어요.", "Even for repeated bits (1,1), Manchester still flips once at each bit's middle.")},
        {"svg": P5, "alt": ("왼쪽: 신호를 두 배 빨리 바꿔야 해 땀 흘리는 분류소 직원. 오른쪽: 더 빠른 이더넷을 뜻하는 빠른 트럭", "Left: a sorter sweats because the signal must change twice as fast. Right: a fast truck stands for faster Ethernet using other encodings"),
         "caption": ("비트마다 꼭 신호를 뒤집어야 해서, 같은 비트 속도에 NRZ의 두 배 빠른 신호 변화가 필요해요.", "A flip in every bit means the same bit rate needs signal changes twice as fast as NRZ."),
         "small": ("그래서 10Mb/s 이더넷(10BASE-T)에는 맨체스터를 썼지만, 더 빠른 이더넷은 다른 부호화를 써요.", "So 10 Mb/s Ethernet (10BASE-T) used Manchester, while faster Ethernet uses other encodings.")},
    ],
    "summary": (("<b>맨체스터 부호화</b> = 전선 신호를 <b>비트 한가운데서 항상 뒤집어</b>, 받는 쪽이 신호만 보고도 박자(클럭)를 되찾게 하는 약속.",
                 "<b>Manchester encoding</b> = a rule that <b>always flips the wire signal in the middle of every bit</b>, so the receiver can recover the clock from the signal alone."),
                ("맨체스터 부호화는 매 비트 구간의 중간에서 신호 천이(transition)가 일어나도록 하는 라인 부호화(line coding) 방식으로, OSI 1계층(물리)의 규칙이에요. 천이 방향으로 0과 1을 구분하는데, IEEE 802.3은 상승을 1, 하강을 0으로 보고 G.E. Thomas 방식은 그 반대예요. 이 천이 덕분에 별도의 클럭 신호 없이도 수신 측이 타이밍을 복원할 수 있고(자기동기화), 직류(DC) 성분이 데이터에 따라 달라지지 않아요. 10BASE-T 이더넷 등에 쓰였지만 같은 비트 속도에 NRZ의 약 두 배 대역폭이 필요해, 100BASE-TX는 4B5B와 MLT-3, 1000BASE-X는 8b/10b, 10GBASE-R은 64b/66b를 써요.",
                 "Manchester encoding is a line-coding scheme, an OSI layer 1 (physical) rule, that forces a signal transition at the midpoint of every bit period. The direction of the transition encodes 0 or 1: IEEE 802.3 treats rising as 1 and falling as 0, and the G.E. Thomas convention is the reverse. The transition lets the receiver recover timing without a separate clock signal (self-clocking), and the DC component doesn't depend on the data. It was used in 10BASE-T Ethernet and similar links, but needs about twice the bandwidth of NRZ for the same bit rate, so 100BASE-TX uses 4B5B with MLT-3, 1000BASE-X uses 8b/10b, and 10GBASE-R uses 64b/66b.")),
    "glossary": [
        ("맨체스터 부호화", "Manchester Encoding", ("비트 중간마다 꼭 한 번 뒤집히는 신호 규칙.", "A signal rule that flips exactly once at the middle of every bit."), ("자기동기화를 위한 라인 부호화 방식이에요.", "A line-coding scheme built for self-clocking.")),
        ("자기동기화", "Self-Clocking", ("신호만 보고 박자를 되찾는 것.", "Recovering the beat from the signal alone."), ("박자를 알려주는 전선을 따로 깔지 않아도 돼요.", "No separate wire is needed to carry the beat.")),
        ("NRZ(일반 신호)", "NRZ (Non-Return-to-Zero)", ("값이 바뀔 때만 신호가 바뀌는 단순한 방식.", "A simpler scheme where the signal changes only when the value changes."), ("같은 값이 이어지면 비트 개수를 세기 어려워요.", "Repeated values make bits hard to count.")),
        ("DC 성분", "DC Component", ("신호를 평균 냈을 때 남는 한쪽 치우침.", "The one-sided lean left when a signal is averaged."), ("맨체스터는 이 값이 데이터에 따라 달라지지 않아, 변압기를 거치는 회선에도 잘 맞아요.", "In Manchester it doesn't depend on the data, which suits lines that pass through a transformer.")),
        ("라인 부호화", "Line Coding", ("비트를 전선 위 신호 모양으로 바꾸는 규칙 전체.", "The general category of rules turning bits into signal shapes on a wire."), ('OSI 1계층에서 하는 일이에요. → <a href="osi7-ko.html">7단계로 나뉜 배송 공정</a>', 'A job for OSI layer 1. → <a href="osi7-en.html">the delivery process split into 7 stages</a>')),
        ("대역폭", "Bandwidth", ("회선이 실어 나를 수 있는 신호 변화 빠르기의 폭.", "The range of signal-change speeds a line can carry."), ("맨체스터는 같은 비트 속도에 NRZ의 약 두 배가 필요해요.", "Manchester needs about twice NRZ's bandwidth for the same bit rate.")),
        ("10BASE-T", "10BASE-T Ethernet", ("맨체스터 부호화를 쓰는 10Mb/s 이더넷.", "A 10 Mb/s Ethernet standard that uses Manchester encoding."), ('전선을 여럿이 나눠 쓸 때는 CSMA/CD 규칙을 따라요. → <a href="macprotocol-ko.html">하나의 통로를 안 부딪히고 나눠 쓰는 법</a>', 'When stations share the wire, it follows CSMA/CD. → <a href="macprotocol-en.html">sharing one lane without colliding</a>')),
        ("8b/10b 부호화", "8b/10b Encoding", ("8비트를 10비트로 바꿔 보내는 부호화.", "An encoding that sends every 8 bits as 10."), ("일부 기가비트 이더넷이 쓰며, 맨체스터보다 대역폭을 덜 쓰면서 박자 정보를 지켜요.", "Used by some Gigabit Ethernet; keeps the beat while using less bandwidth than Manchester.")),
    ],
}
