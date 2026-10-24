from _draw import *
from _world import *


def socket(x, y, s=1.0, color="var(--good)"):
    """표준 규격 콘센트(인터페이스)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-16" width="44" height="32" rx="8" fill="#FFF8E7" stroke="{color}" stroke-width="4"/>'
            f'<circle cx="-8" cy="0" r="4" fill="{color}"/><circle cx="8" cy="0" r="4" fill="{color}"/></g>')


def plug_cable(x1, y1, x2, y2, color="#4A5A72"):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="6" stroke-linecap="round"/>'


# 1. 작가가 특정 기계 한 대에 꽉 맞춰 글을 써요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SMILE, **WRITER)
         + '<rect x="400" y="150" width="90" height="80" rx="4" fill="#4A5A72"/>' + label(445, 250, "⟦A사 전용 기계|Press Model A only⟧", 11, "var(--muted)")
         + plug_cable(298, 190, 400, 190)
         + label(380, 30, "⟦작가가 특정 기계 한 대에 꽉 맞춰 원고를 써요|the writer writes to fit one exact machine⟧", 13, "var(--ink)")
         + label(380, 280, "⟦원고가 그 기계 배선에 그대로 박혀 있어요|the manuscript is wired straight into that one machine⟧", 12, "var(--muted)"))

# 2. 그 기계가 고장 나면 작가도 올스톱
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=FROWN + SWEAT, **WRITER)
         + '<rect x="400" y="150" width="90" height="80" rx="4" fill="#7A3B3B"/>' + label(445, 250, "⟦고장!|broken!⟧", 13, "var(--bad)", cls="d")
         + plug_cable(298, 190, 400, 190, "var(--bad)")
         + label(380, 70, "⟦다른 기계로 바꾸려면 원고를 다 뜯어고쳐야 해요|switching machines means rewriting the manuscript itself⟧", 12, "var(--ink)")
         + label(380, 270, "⟦너무 꽉 묶여 있어서 꼼짝을 못 해요|too tightly wired in to move at all⟧", 12, "var(--bad)"))

# 3. DI/DIP = 표준 콘센트만 알고, 기계는 바깥에서 꽂아줘요 (hero)
P3 = svg(340, sky(340)
         + person(220, 150, s=0.85, face=SMILE, **WRITER)
         + socket(330, 190, 1.0)
         + plug_cable(298, 190, 316, 190)
         + person(500, 100, s=0.7, face=EYES, **EDITOR)
         + '<rect x="430" y="210" width="80" height="70" rx="4" fill="#4A5A72"/>' + label(470, 300, "⟦인쇄기 B|Press B⟧", 11, "var(--muted)")
         + plug_cable(372, 190, 430, 230, "var(--good)")
         + label(380, 25, "⟦작가는 표준 콘센트(규격)만 알고 쓰고, 어떤 기계를 꽂을지는 바깥에서 정해요|the writer only knows the standard socket — what gets plugged in is decided from outside⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦편집장이 바깥에서 알맞은 기계를 꽂아 줘요(주입)|the editor plugs in the right machine from outside — that's injection⟧", 11, "var(--muted)"))

ABSTRACT_I = icon('<rect x="14" y="18" width="36" height="28" rx="8" fill="#FFF8E7" stroke="var(--good)" stroke-width="4"/><circle cx="24" cy="32" r="4" fill="var(--good)"/><circle cx="40" cy="32" r="4" fill="var(--good)"/>')
INJECT_I = icon('<path d="M18 46 L30 20" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M30 20 l-6 -2 m6 2 l-2 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><rect x="34" y="34" width="20" height="16" rx="3" fill="#4A5A72"/>')
SWAP_I = icon('<path d="M14 24 h24 M34 24 l-6 -6 m6 6 l-6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 40 h-24 M26 40 l6 -6 m-6 6 l6 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
INVERT_I = icon('<circle cx="22" cy="20" r="8" fill="var(--good)"/><circle cx="42" cy="44" r="8" fill="var(--accent)"/><path d="M22 20 L42 44" stroke="#FFF8E7" stroke-width="3" stroke-dasharray="3 3"/>')

# 4. 직접 연결 vs 표준 콘센트 비교
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 30, "⟦이전: 직접 배선|Before: wired directly⟧", 13, "var(--ink)", cls="d")
         + '<rect x="130" y="60" width="60" height="50" rx="4" fill="#2E3D57"/>' + plug_cable(190, 85, 250, 85, "#4A5A72") + '<rect x="250" y="60" width="60" height="50" rx="4" fill="#4A5A72"/>'
         + label(190, 150, "⟦기계를 바꾸려면 배선을 다 뜯어요|changing machines means re-wiring it all⟧", 11, "var(--ink)")
         + label(570, 30, "⟦이후: 표준 콘센트|After: a standard socket⟧", 13, "var(--ink)", cls="d")
         + '<rect x="510" y="60" width="60" height="50" rx="4" fill="#2E3D57"/>' + socket(600, 85, 0.8) + plug_cable(570, 85, 580, 85, "var(--good)")
         + label(600, 150, "⟦콘센트만 맞으면 기계는 뭐든 꽂아요|any machine fits, as long as the socket matches⟧", 11, "var(--ink)")
         + label(380, 250, "⟦테스트할 땐 진짜 기계 대신 가짜 기계(목업)를 꽂을 수도 있어요|for testing, a fake stand-in machine can be plugged in instead⟧", 12, "var(--ink)")
         + label(380, 290, "⟦고수준 작가와 저수준 기계, 둘 다 콘센트 규격만 바라봐요|both the high-level writer and the low-level machine answer to the same socket spec⟧", 12, "var(--muted)"))

# 5. 규격을 너무 많이 두면 오히려 헷갈려요
P5 = svg(300, sky(300)
         + socket(220, 160, 0.9) + socket(320, 140, 0.7) + socket(400, 190, 0.6) + socket(480, 150, 0.8) + socket(560, 170, 0.65)
         + person(640, 160, s=0.75, face=SWEAT + EYES, **WRITER)
         + label(380, 30, "⟦콘센트가 너무 많아지면 뭐가 뭔지 헷갈려요|too many sockets, and it gets confusing which is which⟧", 13, "var(--ink)")
         + label(380, 280, "⟦필요한 곳에만 규격을 둬야, 바꿔 끼우기도 쉬워요|standards earn their keep only where they're actually needed⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "diprinciple", "order": 45,
    "title": ("아무 기계나 꽂을 수 있는 콘센트", "The Standard Socket Any Machine Can Plug Into"),
    "h1": ("<em>의존성 주입/역전(DI/DIP)</em>이 뭐예요?", "What is <em>Dependency Injection / Inversion (DI/DIP)</em>?"),
    "sub": ("DI/DIP를, 작가가 특정 기계에 직접 배선하는 대신 표준 콘센트만 알고 쓰는 이야기로 풀어봤어요.",
            "DI/DIP, told as a story about a writer who only needs to know a standard socket, instead of wiring directly into one specific machine."),
    "panels": [
        {"svg": P1, "alt": ("작가가 특정 인쇄기 한 대에 직접 배선된 원고를 씀", "A writer's manuscript is wired directly into one specific press"),
         "caption": ("작가가 특정 기계 한 대에 꽉 맞춰 원고를 써요.", "The writer writes to fit one exact machine."),
         "small": ("원고가 그 기계 배선에 그대로 박혀 있어요.", "The manuscript is wired straight into that one machine.")},
        {"svg": P2, "alt": ("그 기계가 고장 나자 작가가 진땀을 흘림", "The machine breaks down, and the writer breaks into a sweat"),
         "caption": ("그 기계가 고장 나면 작가도 올스톱이에요.", "If that one machine breaks, the writer is stuck too."),
         "small": ("너무 꽉 묶여 있어서 꼼짝을 못 해요.", "Too tightly wired in to move at all.")},
        {"svg": P3, "hero": True, "alt": ("작가는 표준 콘센트만 쓰고, 편집장이 바깥에서 인쇄기 B를 꽂아줌", "The writer uses only a standard socket, while the editor plugs in Press B from outside"),
         "caption": ("DI/DIP는 작가가 표준 콘센트만 알고 쓰고, 어떤 기계를 꽂을지는 바깥에서 정하는 거예요.", "DI/DIP means the writer only knows the standard socket, while what gets plugged in is decided from outside."),
         "small": ("편집장이 바깥에서 알맞은 기계를 꽂아 줘요.", "The editor plugs in the right machine from outside — that's injection."),
         "tricks": (4, [
             (ABSTRACT_I, ("규격(추상)에만 의존", "Depends only on the standard"), ("세부 기계는 몰라도 돼요", "doesn't need to know the machine's details"), "calm"),
             (INJECT_I, ("바깥에서 꽂아줘요", "Plugged in from outside"), ("작가가 직접 고르지 않아요", "the writer doesn't pick it themselves")),
             (SWAP_I, ("교체가 쉬워요", "Easy to swap"), ("테스트용 가짜 기계도 꽂을 수 있어요", "even a fake test stand-in can be plugged in"), "warm"),
             (INVERT_I, ("방향이 뒤집혀요", "The dependency is inverted"), ("둘 다 규격을 바라봐요", "both sides answer to the same standard")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 직접 배선된 기계는 바꾸기 어려움. 오른쪽: 표준 콘센트는 어떤 기계든 꽂을 수 있음", "Left: a directly wired machine is hard to change. Right: a standard socket accepts any machine"),
         "caption": ("직접 배선 대신 표준 콘센트를 두면 바꿔 끼우기 쉬워요.", "A standard socket, instead of direct wiring, makes swapping easy."),
         "small": ("고수준 작가와 저수준 기계, 둘 다 콘센트 규격만 바라봐요.", "Both the high-level writer and the low-level machine answer to the same socket spec.")},
        {"svg": P5, "alt": ("콘센트가 너무 많아져서 작가가 헷갈려함", "Too many sockets appear, and the writer looks overwhelmed"),
         "caption": ("규격을 너무 많이 두면 오히려 헷갈려요.", "Too many standards, and it gets confusing instead."),
         "small": ("필요한 곳에만 규격을 둬야, 바꿔 끼우기도 쉬워요.", "A standard earns its keep only where it's actually needed.")},
    ],
    "summary": (("<b>DI/DIP</b> = 작가(고수준)가 기계(저수준)에 직접 매이지 않고, 둘 다 <b>표준 콘센트(추상)</b>만 보게 하고 기계는 <b>바깥에서 꽂아주는</b> 원칙.",
                 "<b>DI/DIP</b> is a principle where the writer (high-level) isn't tied directly to the machine (low-level) — both sides look only at a <b>standard socket (an abstraction)</b>, and the machine is <b>plugged in from outside</b>."),
                ("의존성 역전 원칙(DIP)은 '고수준 모듈이 저수준 모듈에 의존하지 않고, 둘 다 추상(인터페이스)에 의존해야 한다'는 설계 원칙이고, 의존성 주입(DI)은 그 추상의 실제 구현체를 객체가 직접 생성하지 않고 외부에서 전달(주입)받는 구현 기법이에요. SOLID 원칙 중 D에 해당해요.",
                 "The Dependency Inversion Principle (DIP) says high-level modules shouldn't depend on low-level modules — both should depend on an abstraction (an interface). Dependency Injection (DI) is the implementation technique that passes (injects) a concrete implementation of that abstraction from outside, instead of an object creating it itself. DIP is the 'D' in the SOLID principles.")),
    "glossary": [
        ("DIP(의존성 역전 원칙)", "Dependency Inversion Principle", ("고수준과 저수준이 둘 다 규격만 바라보게 하는 원칙.", "A principle where both high- and low-level sides answer only to a standard."), ("SOLID 원칙의 D예요.", "It's the D in SOLID.")),
        ("DI(의존성 주입)", "Dependency Injection", ("기계를 바깥에서 꽂아주는 방법.", "The technique of plugging the machine in from outside."), ("작가가 직접 만들거나 고르지 않아요.", "The writer never creates or picks it themselves.")),
        ("인터페이스(추상)", "Interface / Abstraction", ("표준 콘센트 그 자체.", "The standard socket itself."), ("세부 기계가 아니라 규격만 약속해요.", "It promises only the spec, not the machine's internals.")),
        ("결합도(Coupling)", "Coupling", ("작가와 기계가 묶인 정도.", "How tightly the writer and machine are tied together."), ("직접 배선은 강한 결합, 콘센트는 느슨한 결합이에요.", "Direct wiring is tight coupling; a socket is loose coupling.")),
        ("정보은닉/캡슐화", "Encapsulation", ("세부 기계를 작가 눈에 안 보이게 감추는 것.", "Hiding the machine's details from the writer's view."), ('DIP가 기대는 또 다른 원칙이에요. → <a href="encapsulation-ko.html">작가의 잠긴 서랍</a>', "Another principle DIP leans on. → <a href=\"encapsulation-en.html\">the writer's locked drawer</a>")),
        ("테스트 더블(Mock)", "Test Double / Mock", ("테스트용 가짜 기계.", "A fake stand-in machine, used only for testing."), ("콘센트만 맞으면 진짜 기계 대신 꽂을 수 있어요.", "As long as the socket matches, it can stand in for the real machine.")),
        ("제어의 역전(IoC)", "Inversion of Control", ("누가 언제 기계를 꽂을지 정하는 틀.", "The larger framework deciding who plugs in what, and when."), ("DI를 가능하게 해주는 더 큰 틀이에요.", "It's the broader framework that makes DI possible.")),
        ("리팩터링", "Refactoring", ("직접 배선을 나중에 콘센트로 바꾸는 작업.", "The work of later turning direct wiring into a socket."), ('줄거리는 그대로, 연결 구조만 다시 다듬어요. → <a href="refactorppe-ko.html">줄거리는 그대로, 문장만 다시 다듬기</a>', 'The plot stays the same — only the wiring gets reworked. → <a href="refactorppe-en.html">same plot, retouched sentences</a>')),
    ],
}
