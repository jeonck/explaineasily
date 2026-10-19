from _draw import *
from _world import *


def notepad(x, y, s=1.0, label_text=None):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-22" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-10 -10 h20 M-10 -2 h20 M-10 6 h12" stroke="#142033" stroke-width="2"/>'
    if label_text:
        out += label(0, 36, label_text, 10, "var(--muted)")
    return out + '</g>'


def signboard(x, y, w, h, title, rows, hl=-1):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 48 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="{w - 12}" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 11, "#142033", "start")
    return out + '</g>'


# 1. 정비사가 일하는데 갑자기 손님 차가 빵빵 울려요
P1 = svg(300, sky(300)
         + person(220, 160, s=0.9, face=EYES, **MECH1) + car(200, 230, 0.7)
         + car(520, 200, 0.9, color="var(--bad)")
         + label(520, 140, "⟦빵빵!|HONK!⟧", 20, "var(--bad)", cls="d")
         + label(380, 40, "⟦타이어를 갈던 중인데 갑자기 급한 차가 끼어들어요|mid-tire-change, and an urgent car suddenly honks⟧", 13, "var(--ink)")
         + label(380, 280, "⟦지금 하던 일을 계속할지, 멈추고 봐줄지 정해야 해요|keep working, or stop and look — a decision is needed⟧", 12, "var(--muted)"))

# 2. 계속 흘깃흘깃 쳐다보는 건 비효율적이에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(300, 160, s=0.9, face=FROWN, **MECH1) + car(280, 230, 0.7)
         + "".join(f'<path d="M{330 + i * 0} 140 q40 {-10 if i % 2 else 10} 80 0" stroke="var(--accent)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>' for i in range(1))
         + label(500, 110, "⟦급한 차 왔나?...안 왔나?...|urgent car yet?... not yet?...⟧", 12, "var(--accent)", cls="d")
         + label(380, 50, "⟦틈틈이 계속 쳐다보기만 해도(폴링) 일손이 뺏겨요|just glancing over and over (polling) steals your attention⟧", 13, "var(--ink)")
         + label(380, 262, "⟦급한 차가 직접 알려주는 방법이 필요해요|we need the urgent car to signal in directly⟧", 12, "var(--muted)"))

# 3. 인터럽트 처리 과정 = 벨이 울리면 하던 일을 적어두고 바로 달려가는 것 (hero)
P3 = svg(340, sky(340)
         + person(170, 160, s=0.85, face=EYES, **MECH1) + car(150, 230, 0.6)
         + notepad(260, 110, 0.9, ("⟦하던 일 적어두기|jot down where I was⟧", ""))
         + person(430, 130, s=0.9, face=SWEAT, **CHIEF) + car(430, 230, 0.85, color="var(--bad)")
         + label(380, 30, "⟦인터럽트 처리 = 벨이 울리면 하던 일을 적어두고 바로 달려가는 것|handling an interrupt: jot down your place, then run to the bell⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦급한 일을 끝내면 적어둔 자리부터 다시 이어서 해요|once done, pick back up exactly where you left off⟧", 12, "var(--muted)"))

BELL_I = icon('<path d="M32 10 a16 16 0 0 1 16 16 v10 l6 8 h-44 l6 -8 v-10 a16 16 0 0 1 16 -16z" fill="var(--bad)"/><circle cx="32" cy="50" r="4" fill="var(--bad)"/>')
SAVE_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 32 h24 M20 40 h14" stroke="#142033" stroke-width="2.5"/>')
VECTOR_I = icon('<rect x="8" y="10" width="48" height="44" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M16 22 h32 M16 32 h32 M16 42 h20" stroke="var(--accent)" stroke-width="2.5"/>')
RESUME_I = icon('<path d="M20 20 a16 16 0 1 0 4 -6" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M16 8 l8 6 l-2 9z" fill="var(--good)"/>')

# 4. 처리 과정 타임라인
P4 = svg(320, sky(320)
         + signboard(40, 40, 330, 250, "⟦인터럽트 처리 순서|the interrupt-handling sequence⟧",
                     ("⟦① 벨 울림 — 인터럽트 발생|① bell rings — interrupt occurs⟧",
                      "⟦② 하던 자리 적어두기 — 상태 저장|② jot down the spot — save state⟧",
                      "⟦③ 벨 종류별 담당표 확인 — 인터럽트 벡터|③ check the bell-type board — vector table⟧",
                      "⟦④ 담당자가 처리(ISR)|④ the right handler deals with it (ISR)⟧",
                      "⟦⑤ 적어둔 자리부터 복귀 — 상태 복원|⑤ resume from the saved spot — restore state⟧"), hl=2)
         + signboard(410, 60, 300, 90, "⟦벨 종류별 담당표|bell-type board⟧",
                     ("⟦타이어 벨 → 1번 정비사|tire bell → mechanic 1⟧", "⟦엔진 벨 → 2번 정비사|engine bell → mechanic 2⟧"))
         + label(560, 210, "⟦같은 벨도 항상 같은 담당자가 맡아요|the same bell always reaches the same handler⟧", 11, "var(--muted)"))

# 5. 네트워크 인터럽트와는 다른 이야기예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **MECH1)
         + label(190, 240, "⟦여기선 어떤 벨이든 — 일반적인 처리 순서예요|here: any bell at all — the general handling sequence⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **MECH2)
         + label(570, 240, "⟦네트워크 카드 벨만 따로 다루는 이야기는 다른 세계에 있어요|the network-card bell alone is covered in another world⟧", 11, "var(--ink)")
         + label(380, 282, "⟦순서는 같아요 — 저장하고, 처리하고, 복귀해요|the sequence is the same — save, handle, resume⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "interruptproc", "order": 14,
    "title": ("벨이 울리면 적어두고 바로 달려가기", "Jot Down Your Place and Run to the Bell"),
    "h1": ("<em>인터럽트 처리 과정</em>이 뭐예요?", "What is <em>Interrupt Handling</em>?"),
    "sub": ("인터럽트 처리 과정을, 정비공장에서 급한 벨이 울리면 하던 일을 적어두고 바로 달려가는 이야기로 풀어봤어요.",
            "Interrupt handling, told as a story about a mechanic who jots down their place and runs to an urgent bell."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 타이어를 갈던 중 급한 손님 차가 경적을 울림", "A mechanic mid-tire-change as an urgent customer car honks"),
         "caption": ("일하는데 갑자기 급한 차가 빵빵 울려요.", "An urgent car suddenly honks while work is underway."),
         "small": ("지금 하던 일을 계속할지, 멈추고 봐줄지 정해야 해요.", "A decision is needed — keep working, or stop and look.")},
        {"svg": P2, "alt": ("정비사가 급한 차가 왔는지 계속 흘깃거리느라 지쳐함", "The mechanic tires out from constantly glancing over for the urgent car"),
         "caption": ("계속 흘깃거리기만 하는 건 비효율적이에요.", "Just glancing over again and again is inefficient."),
         "small": ("급한 차가 직접 알려주는 방법이 필요해요.", "We need the urgent car to signal in directly.")},
        {"svg": P3, "hero": True, "alt": ("정비사가 메모지에 하던 일을 적고 급한 벨이 울린 차로 달려감", "The mechanic jots their place on a notepad and runs to the honking car"),
         "caption": ("벨이 울리면 하던 일을 적어두고 바로 달려가요.", "When the bell rings, jot down your place and run to it."),
         "small": ("급한 일을 끝내면 적어둔 자리부터 다시 이어서 해요.", "Once done, pick back up exactly where you left off."),
         "tricks": (4, [
             (BELL_I, ("① 인터럽트 발생", "① Interrupt occurs"), ("벨이 울려요", "the bell rings"), "warm"),
             (SAVE_I, ("② 상태 저장", "② Save state"), ("하던 자리를 적어둬요", "jot down the current spot")),
             (VECTOR_I, ("③ 벡터 확인", "③ Check the vector table"), ("벨 종류별 담당자를 찾아요", "look up who handles this bell")),
             (RESUME_I, ("④⑤ 처리 후 복귀", "④⑤ Handle, then resume"), ("적어둔 자리부터 이어가요", "continue from the jotted spot"), "calm"),
         ])},
        {"svg": P4, "alt": ("인터럽트 발생부터 상태 저장, 벡터 확인, ISR 처리, 상태 복원까지 다섯 단계 순서표", "A five-step board: interrupt occurs, save state, check vector, ISR handles it, restore state"),
         "caption": ("처리 순서는 다섯 단계예요.", "The handling sequence has five steps."),
         "small": ("같은 벨도 항상 같은 담당자가 맡아요.", "The same bell always reaches the same handler.")},
        {"svg": P5, "alt": ("왼쪽: 일반적인 인터럽트 처리 순서. 오른쪽: 네트워크 카드 벨만 다루는 이야기는 다른 곳에 있음", "Left: the general interrupt-handling sequence. Right: the network-card bell alone is covered elsewhere"),
         "caption": ("네트워크 벨만 따로 다루는 이야기와는 달라요.", "This differs from the story about the network-card bell alone."),
         "small": ("순서는 같아요 — 저장하고, 처리하고, 복귀해요.", "The sequence is the same — save, handle, resume.")},
    ],
    "summary": (("<b>인터럽트 처리</b>는 벨(신호)이 울리면 <b>하던 일을 적어두고</b> 담당자에게 달려가 처리한 뒤, <b>원래 자리부터 다시 이어가는</b> 순서예요.",
                 "<b>Interrupt handling</b> is the sequence of <b>jotting down your place</b> when a signal fires, letting the right handler deal with it, then <b>resuming exactly where you left off</b>."),
                ("인터럽트는 CPU가 현재 실행 중인 명령을 잠시 멈추고 다른 긴급한 작업을 처리하도록 하는 신호예요. 처리 과정은 ①인터럽트 발생 ②현재 레지스터·프로그램 카운터를 스택에 저장 ③인터럽트 벡터 테이블에서 해당 ISR(인터럽트 서비스 루틴) 주소 확인 ④ISR 실행 ⑤저장해둔 상태를 복원하고 원래 실행 흐름으로 복귀하는 순서로 이뤄져요. 계속 상태를 확인하는 폴링 방식보다 CPU 자원을 아낄 수 있어요.",
                 "An interrupt is a signal that makes the CPU pause its current instruction stream to handle something urgent. The sequence is: ① interrupt occurs ② current registers and program counter are pushed to the stack ③ the interrupt vector table is consulted for the matching ISR (interrupt service routine) address ④ the ISR runs ⑤ the saved state is restored and execution resumes where it left off. This saves CPU resources compared to constantly polling for status.")),
    "glossary": [
        ("인터럽트", "Interrupt", ("급한 차가 울리는 벨.", "The bell an urgent car honks."), ("하던 일을 잠시 멈추게 하는 신호예요.", "A signal that pauses current work.")),
        ("상태 저장/복원", "Save/Restore State", ("하던 일을 적어뒀다가 다시 펴보기.", "Jotting down your place, then reading it back later."), ("레지스터·프로그램 카운터를 스택에 쌓아요.", "Registers and the program counter go onto the stack.")),
        ("인터럽트 벡터 테이블", "Interrupt Vector Table", ("벨 종류별 담당자 이름표.", "A nameplate board mapping each bell type to its handler."), ("벨마다 정해진 처리 루틴 주소를 담고 있어요.", "Holds the handler address for each interrupt type.")),
        ("ISR(인터럽트 서비스 루틴)", "ISR (Interrupt Service Routine)", ("벨에 달려가 실제로 처리하는 사람.", "The one who actually runs to the bell and handles it."), ("벡터 테이블이 가리키는 처리 코드예요.", "The handler code the vector table points to.")),
        ("폴링", "Polling", ("계속 흘깃흘깃 확인하는 방식.", "Constantly glancing over to check."), ("인터럽트보다 비효율적일 수 있어요.", "Can be less efficient than interrupts.")),
        ("인터럽트 우선순위", "Interrupt Priority", ("더 급한 벨부터 처리하는 순서.", "Handling the more urgent bell first."), ("벨 여러 개가 동시에 울릴 때 쓰여요.", "Matters when several bells ring at once.")),
        ("소프트웨어 인터럽트", "Software Interrupt", ("정비사 스스로 벨을 눌러 요청하는 것.", "The mechanic pressing the bell themselves to make a request."), ("시스템 콜이 이 방식을 써요.", "System calls use this mechanism.")),
        ("네트워크 인터럽트", "Network Interrupt", ("네트워크 카드 벨만 다루는 이야기.", "The story about the network-card bell specifically."), ('다른 세계(네트워크 분야)에서 자세히 다뤄요. → <a href="interruptnet-ko.html">소포가 도착했다고 알리는 벨소리</a>', 'Covered in depth in another world (the networking field). → <a href="interruptnet-en.html">the bell that says a parcel just arrived</a>')),
    ],
}
