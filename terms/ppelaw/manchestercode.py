"""맨체스터 부호화 — 학생회 세계관과는 결이 다른, 통신 물리계층의 전기 신호 규칙."""
from _draw import *
from _world import *

def grid(xs, y0=15, y1=115):
    return "".join(f'<path d="M{x} {y0} V{y1}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 3"/>' for x in xs)


NRZ_PATH = "M130 40 L230 40 L230 90 L330 90 L330 40 L530 40 L530 90 L630 90"
MANCH_PATH = "M130 90 L180 90 L180 40 L230 40 L280 40 L280 90 L330 90 L380 90 L380 40 L430 40 L430 90 L480 90 L480 40 L530 40 L580 40 L580 90 L630 90"
BOUNDS = (130, 230, 330, 430, 530, 630)
MIDS = (180, 280, 380, 480, 580)

TRANS_I = icon('<path d="M20 44 V12 M20 12 l-8 8 M20 12 l8 8" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 20 V52 M44 52 l-8 -8 M44 52 l8 -8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
DIR_I = icon('<path d="M16 46 V18" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M10 24 l6 -6 l6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M48 18 V46" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M42 40 l6 6 l6 -6" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BALANCE_I = icon('<path d="M32 14 V50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 H50" stroke="var(--night)" stroke-width="3"/><path d="M14 24 l-6 14 h12z" fill="var(--accent)"/><path d="M50 24 l-6 14 h12z" fill="var(--good)"/>')

# 1. 이번엔 학생회 규칙 얘기가 아니에요
P1 = svg(300, sky(300)
         + label(380, 26, "⟦잠깐, 이번엔 학생회 규칙이 아니에요 — 전선을 타고 가는 전기 신호 얘기예요|hold on, this one isn't a student-council rule — it's about electrical signals on a wire⟧", 12, "var(--muted)", cls="d")
         + person(220, 150, s=0.85, face=EYES, **REP)
         + '<rect x="330" y="120" width="340" height="60" rx="6" fill="#0A1120"/>'
         + '<path d="M350 150 H650" stroke="var(--accent)" stroke-width="4"/>' + label(500, 110, "⟦신호선: 0 1 0 1 1 ...?|the wire: 0 1 0 1 1 ...?⟧", 12, "var(--muted)")
         + bubble(90, 60, 230, 44, "⟦이 신호, 언제 1이고 언제 0인지 어떻게 알아요?|how do I tell where one bit ends and the next begins?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦신호만 봐서는 비트 하나의 길이를 알 수 없어요|the signal alone doesn't show how long one bit is⟧", 13, "var(--ink)", cls="d"))

# 2. 같은 값이 계속되면 더 헷갈려요
P2 = svg(345, '<rect width="760" height="345" fill="var(--bad-soft)"/>'
         + '<rect x="130" y="120" width="500" height="60" rx="6" fill="#0A1120"/>'
         + '<path d="M150 135 H610" stroke="var(--bad)" stroke-width="4"/>' + label(380, 110, "⟦1 1 1 1 1 1 … 몇 개죠?|1 1 1 1 1 1 … how many is that?⟧", 12, "var(--bad)")
         + person(380, 220, s=0.8, face=SWEAT + EYES, **TEACHER)
         + label(380, 328, "⟦보내는 쪽과 받는 쪽의 시계가 조금만 어긋나도 개수를 잘못 세요|if the sender's and receiver's clocks drift even a little, the count comes out wrong⟧", 12, "var(--ink)", cls="d"))

# 3. 맨체스터 부호화 = 비트 한가운데서 항상 신호가 바뀌게 만드는 약속 (hero)
P3 = svg(400, sky(400, ground=False)
         + label(380, 26, "⟦맨체스터 부호화 = 비트 한가운데서 항상 신호가 바뀌게 만드는 약속|Manchester encoding = a rule that always flips the signal at the middle of every bit⟧", 13, "var(--ink)", cls="d")
         + grid(BOUNDS, 55, 155) + f'<path d="{MANCH_PATH}" transform="translate(0,15)" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + "".join(f'<path d="M{m} 50 v10" stroke="var(--good)" stroke-width="3"/><path d="M{m - 5} 56 l5 6 l5 -6" fill="none" stroke="var(--good)" stroke-width="2.5"/>' for m in MIDS)
         + label(380, 230, "⟦점선=비트 경계, 초록 화살표=비트 한가운데(항상 신호 전환)|dashed line = bit boundary, green arrow = the bit's midpoint (always a flip)⟧", 11, "var(--muted)")
         + person(380, 270, s=0.85, face=EYES, **TEACHER)
         + label(380, 384, "⟦이 약속 하나로 받는 쪽이 신호만 보고 박자를 알 수 있어요|that one rule lets the receiver read the beat from the signal alone⟧", 12, "var(--muted)"))

# 4. 일반 신호(NRZ) vs 맨체스터 부호화
P4 = svg(300, '<rect width="760" height="300" fill="var(--panel)"/>'
         + label(380, 26, "⟦같은 비트 1 0 1 1 0 을 보냈을 때|sending the same bits: 1 0 1 1 0⟧", 13, "var(--ink)", cls="d")
         + label(130, 55, "⟦일반 신호(NRZ)|PLAIN SIGNAL (NRZ)⟧", 11, "var(--muted)", "start")
         + grid(BOUNDS, 65, 125) + f'<path d="{NRZ_PATH}" stroke="var(--muted)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + label(130, 160, "⟦맨체스터 부호화|MANCHESTER ENCODING⟧", 11, "var(--muted)", "start")
         + grid(BOUNDS, 170, 230) + f'<path d="{MANCH_PATH}" transform="translate(0,80)" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linejoin="round"/>'
         + label(380, 275, "⟦같은 값이 이어져도(1,1) 맨체스터는 중간에서 꼭 한 번 바뀌어요|even for repeated bits (1,1), Manchester still flips once at the middle⟧", 12, "var(--ink)", cls="d"))

# 5. 한계 — 그리고 이 세계와는 좀 안 맞는 비유
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 140, s=0.8, face=SWEAT + EYES, **REP)
         + label(190, 240, "⟦신호를 두 배 빨리 보내야 해요|the signal has to run twice as fast⟧", 11, "var(--bad)")
         + person(570, 140, s=0.8, face=EYES, **TEACHER)
         + label(570, 240, "⟦그래서 요즘은 다른 부호화도 많이 써요|that's why faster links often use other encodings now⟧", 11, "var(--ink)")
         + label(380, 280, "⟦사실 이건 법·표준보다는 통신 물리계층 기술이에요 — 이 세계 비유가 좀 안 맞았어요|really, this is physical-layer tech more than law or policy — the fit with this world is a stretch⟧", 11, "var(--muted)", cls="d"))

PAGE = {
    "slug": "manchestercode", "order": 5,
    "title": ("박자를 스스로 알려주는 신호", "The Signal That Tells Its Own Beat"),
    "h1": ("<em>맨체스터 부호화</em>가 뭐예요?", "What is <em>Manchester Encoding</em>?"),
    "sub": ("맨체스터 부호화를, 비트 한가운데서 항상 신호가 바뀌도록 만든 전기 신호 약속 이야기로 풀어봤어요. (이번만큼은 학생회 세계관과 결이 다른 손님이에요.)",
            "Manchester encoding, told as a story about an electrical-signal rule that always flips in the middle of each bit. (Just this once, a guest that doesn't quite fit the student-council world.)"),
    "panels": [
        {"svg": P1, "alt": ("대표가 전선 위 신호를 보며 언제 1이고 언제 0인지 묻는 장면", "A rep looks at a signal on a wire, asking where one bit ends and the next begins"),
         "caption": ("신호만 봐서는 비트 하나의 길이를 알 수 없어요.", "The signal alone doesn't show how long one bit is."),
         "small": ("이번엔 학생회 규칙이 아니라 전기 신호 얘기예요.", "This one isn't a student-council rule — it's about electrical signals.")},
        {"svg": P2, "alt": ("선생님이 1이 몇 개 이어지는지 헷갈려 땀을 흘림", "A teacher sweats, unable to tell how many 1s are strung together"),
         "caption": ("같은 값이 계속되면 더 헷갈려요.", "Repeated values make it even more confusing."),
         "small": ("보내는 쪽과 받는 쪽의 시계가 조금만 어긋나도 개수를 잘못 세요.", "If the sender's and receiver's clocks drift even a little, the count comes out wrong.")},
        {"svg": P3, "hero": True, "alt": ("비트 한가운데마다 초록 화살표로 표시된 신호 전환이 있는 파형", "A waveform with a green arrow marking a signal flip at the middle of every bit"),
         "caption": ("맨체스터 부호화는 비트 한가운데서 항상 신호가 바뀌게 만드는 약속이에요.", "Manchester encoding is a rule that always flips the signal at the middle of every bit."),
         "small": ("이 약속 하나로 받는 쪽이 신호만 보고 박자를 알 수 있어요.", "That one rule lets the receiver read the beat from the signal alone."),
         "tricks": (4, [
             (TRANS_I, ("한 비트, 한 번 전환", "One flip per bit"), ("꼭 비트 중간에서요", "always at the bit's middle"), "calm"),
             (DIR_I, ("방향으로 0/1 구분", "Direction marks 0/1"), ("올라가면 1, 내려가면 0", "up means 1, down means 0")),
             (CLOCK_I, ("신호로 박자 복원", "Recovers the beat"), ("자기동기화(self-clocking)", "self-clocking"), "warm"),
             (BALANCE_I, ("위아래가 고르게", "Balanced up and down"), ("전기적으로 안정돼요", "stays electrically stable")),
         ])},
        {"svg": P4, "alt": ("같은 비트열 1 0 1 1 0을 일반 신호(NRZ)와 맨체스터 부호화로 각각 그린 파형 비교", "Comparing the same bits 1 0 1 1 0 drawn as a plain (NRZ) signal and as Manchester encoding"),
         "caption": ("일반 신호와 맨체스터 부호화를 나란히 보면 이래요.", "Side by side, a plain signal and Manchester encoding look like this."),
         "small": ("같은 값이 이어져도(1,1) 맨체스터는 중간에서 꼭 한 번 바뀌어요.", "Even for repeated bits (1,1), Manchester still flips once at the middle.")},
        {"svg": P5, "alt": ("왼쪽: 신호를 두 배 빨리 보내야 해 땀 흘리는 대표. 오른쪽: 요즘은 다른 부호화를 쓴다고 말하는 선생님", "Left: a rep sweating because the signal must run twice as fast. Right: a teacher noting other encodings are common now"),
         "caption": ("비트마다 꼭 전환해야 해서 두 배 빠른 회선이 필요해요.", "A flip every bit means the line has to run twice as fast."),
         "small": ("사실 이건 법·표준보다는 통신 물리계층 기술이에요 — 이 세계 비유가 좀 안 맞았어요.", "Really, this is physical-layer tech more than law or policy — the fit with this world is a stretch.")},
    ],
    "summary": (("<b>맨체스터 부호화</b> = <b>비트 한가운데서 항상 신호를 바꿔</b>, 받는 쪽이 신호만 보고도 박자(클럭)를 되찾게 하는 전기 신호 약속.",
                 "<b>Manchester encoding</b> = an electrical-signal rule that <b>always flips in the middle of every bit</b>, so the receiver can recover the clock from the signal alone."),
                ("맨체스터 부호화는 매 비트 구간의 중간에서 신호 천이(transition)가 일어나도록 하는 라인 부호화(line coding) 방식이에요. 천이 방향(상승/하강)으로 0과 1을 구분하고, 이 천이 덕분에 별도의 클럭 신호 없이도 수신 측이 타이밍을 복원할 수 있어요(자기동기화). 10BASE-T 이더넷 등에 쓰였지만, 비트마다 전환이 필요해 같은 속도를 보내려면 일반 부호화보다 두 배 넓은 대역폭이 필요하다는 단점이 있어요.",
                 "Manchester encoding is a line-coding scheme that forces a signal transition at the midpoint of every bit period. The direction of the transition (rising or falling) encodes 0 or 1, and that transition lets the receiver recover timing without a separate clock signal (self-clocking). It was used in 10BASE-T Ethernet and similar links, but needs roughly twice the bandwidth of simpler encodings to carry the same bit rate, since a transition is required every single bit.")),
    "glossary": [
        ("맨체스터 부호화", "Manchester Encoding", ("비트 중간마다 꼭 한 번 바뀌는 신호 규칙.", "A signal rule that flips exactly once at the middle of every bit."), ("자기동기화를 위한 라인 부호화 방식이에요.", "A line-coding scheme built for self-clocking.")),
        ("자기동기화", "Self-Clocking", ("신호만 보고 박자를 되찾는 것.", "Recovering the beat from the signal alone."), ("따로 클럭 신호선을 보낼 필요가 없어요.", "No separate clock wire is needed.")),
        ("NRZ(비귀환 부호화)", "NRZ (Non-Return-to-Zero)", ("값이 바뀔 때만 신호가 바뀌는 단순한 방식.", "A simpler scheme where the signal flips only when the value changes."), ("같은 값이 이어지면 구간을 세기 어려워요.", "Repeated values make the boundaries hard to count.")),
        ("DC 성분 없음", "No DC Bias", ("신호가 위아래로 고르게 바뀌는 성질.", "The signal spends equal time high and low."), ("전선에 한쪽으로 치우친 전기가 쌓이지 않아요.", "Keeps charge from building up one-sided on the wire.")),
        ("라인 부호화", "Line Coding", ("디지털 값을 전기 신호 모양으로 바꾸는 규칙 전체.", "The general category of rules turning digital values into signal shapes."), ("맨체스터 부호화는 그중 한 가지예요.", "Manchester encoding is one member of this family.")),
        ("대역폭", "Bandwidth", ("회선이 한 번에 보낼 수 있는 신호의 양.", "How much signal a line can carry at once."), ("맨체스터 부호화는 같은 속도에 대역폭을 두 배 써요.", "Manchester encoding spends twice the bandwidth for the same bit rate.")),
        ("10BASE-T", "10BASE-T Ethernet", ("맨체스터 부호화를 쓴 초기 이더넷.", "An early Ethernet standard that used Manchester encoding."), ("요즘 고속 이더넷은 다른 부호화를 써요.", "Modern high-speed Ethernet uses different encodings.")),
        ("8b/10b 부호화", "8b/10b Encoding", ("요즘 고속 통신에서 더 많이 쓰는 부호화.", "An encoding used more often in today's high-speed links."), ("대역폭을 덜 쓰면서도 동기화 성질을 지켜요.", "Keeps the self-clocking benefit while using less bandwidth.")),
    ],
}
