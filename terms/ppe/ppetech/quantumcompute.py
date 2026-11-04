from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


def coin(x, y, s=1.0, spin=False):
    """동전. spin=True 면 앞/뒤가 흐릿하게 겹쳐 보여요(중첩)."""
    if spin:
        return (f'<g transform="translate({x},{y}) scale({s})">'
                f'<ellipse rx="26" ry="26" fill="var(--accent)" opacity="0.55"/>'
                f'<text x="-23" y="8" font-size="22" font-weight="700" fill="#fff" opacity="0.8">⟦앞|H⟧</text>'
                f'<text x="2" y="8" font-size="22" font-weight="700" fill="#fff" opacity="0.8">⟦뒤|T⟧</text></g>')
    face = "⟦앞|H⟧" if y % 2 == 0 else "⟦뒤|T⟧"
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="26" fill="#C9A86A"/>'
            + label(0, 8, face, 20, "#142033") + '</g>')


SWITCH_P = '<rect x="10" y="22" width="44" height="20" rx="10" fill="#8A8A8A"/><circle cx="44" cy="32" r="12" fill="#fff"/>'
QUBIT_P = '<circle cx="32" cy="32" r="20" fill="var(--accent)" opacity="0.5"/><circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M14 32 h36 M32 14 v36" stroke="#fff" stroke-width="2" opacity="0.6"/>'
LINK_P = '<circle cx="18" cy="32" r="12" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="46" cy="32" r="12" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M28 32 h8" stroke="var(--good)" stroke-width="4"/>'
MANY_P = ''.join(f'<circle cx="{14+i*10}" cy="32" r="4" fill="var(--accent)"/>' for i in range(5))
SWITCH_I, QUBIT_I, LINK_I, MANY_I = icon(SWITCH_P), icon(QUBIT_P), icon(LINK_P), icon(MANY_P)

# 1. 평범한 스위치 부스 — 0 아니면 1
P1 = svg(300, sky(300)
         + booth(300, 90, 240, 130, 1.0, "var(--stone-dark)", "⟦고전 컴퓨터|CLASSIC COMPUTER⟧")
         + glyph(390, 130, 1.2, SWITCH_P)
         + person(180, 160, s=0.8, face=EYES, **VISITOR)
         + label(380, 250, "⟦스위치는 켜짐 아니면 꺼짐, 둘 중 하나예요|a switch is either on or off — one or the other⟧", 12, "var(--ink)")
         + label(380, 280, "⟦우리가 쓰는 컴퓨터는 전부 이 스위치(0, 1)로 돼 있어요|every computer we use is built from switches like this — 0 or 1⟧", 12, "var(--muted)"))

# 2. 경우의 수가 너무 많으면, 하나씩 다 보기엔 시간이 모자라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT, **DEMO)
         + bubble(300, 58, 320, 50, "⟦경우의 수가 억 개나 되는데, 하나씩 다 확인해야 해요?|there are a hundred million cases — check them one by one?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦스위치 컴퓨터는 한 번에 한 경우만 확인할 수 있어요|a switch-based computer can only check one case at a time⟧", 12, "var(--ink)"))

# 3. 양자 컴퓨팅 = 동전이 돌면서 앞뒤 둘 다인 상태를 쓰는 계산 (hero)
P3 = svg(340, sky(340)
         + booth(260, 80, 240, 150, 1.0, "var(--accent)", "⟦양자 컴퓨터|QUANTUM COMPUTER⟧")
         + coin(380, 165, 1.3, spin=True)
         + person(620, 240, s=0.8, face=SMILE, **VISITOR)
         + label(380, 30, "⟦양자 컴퓨팅 = 돌아가는 동전처럼, 0과 1을 동시에 품은 큐비트로 계산해요|quantum computing = computing with qubits that hold 0 and 1 at once, like a spinning coin⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦큐비트는 여러 경우를 한꺼번에 품고, 정답 쪽 확률을 키워서 풀어요|qubits hold many cases at once and boost the odds of the right answer⟧", 12, "var(--muted)"))

# 4. 고전 비트 vs 큐비트
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦비트 vs 큐비트|BIT vs QUBIT⟧",
                     ("⟦고전 비트 — 항상 0 아니면 1|classic bit — always 0 or 1⟧",
                      "⟦큐비트 — 0과 1을 동시에, 확률로 가져요|qubit — holds 0 and 1 at once, as probabilities⟧",
                      "⟦큐비트 두 개를 묶으면 서로 영향을 줘요(얽힘)|entangled qubits affect each other⟧",
                      "⟦특정 문제만 고전 컴퓨터보다 빨라요|only some problems beat classic computers⟧"), 1.0, hl=1)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦양자 컴퓨터는 암호 풀기·분자 시뮬레이션에 강해요|quantum computers excel at code-breaking and molecules⟧", 11, "var(--muted)"))

# 5. 한계 - 동전은 금방 멈춰요(오류), 모든 문제에 다 빠른 건 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + coin(190, 150, 1.0, spin=True)
         + label(190, 250, "⟦큐비트 동전은 작은 흔들림에도 한쪽으로 멈춰요 — 계산 오류예요|a tiny bump stops the qubit coin on one side: an error⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **DEMO)
         + label(570, 262, "⟦평범한 계산은 오히려 고전 컴퓨터가 더 빨라요|for everyday math, a classic computer is often still faster⟧", 11, "var(--ink)")
         + label(380, 282, "⟦양자 컴퓨터는 만능이 아니라, 특정 문제에 강한 특수 도구예요|a quantum computer isn't all-purpose — it's a specialist tool for particular problems⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "quantumcompute", "order": 18,
    "title": ("동시에 앞뒤인 신기한 동전 부스", "The Booth Where the Coin Is Heads and Tails at Once"),
    "h1": ("<em>양자 컴퓨팅</em>이 뭐예요?", "What is <em>Quantum Computing</em>?"),
    "sub": ("양자 컴퓨팅을, 돌아가는 동전이 앞뒤를 동시에 품은 신기한 부스 이야기로 풀어봤어요.",
            "Quantum computing, told as a story about a strange booth where a spinning coin is heads and tails at once."),
    "panels": [
        {"svg": P1, "alt": ("고전 컴퓨터 부스의 스위치는 켜짐 아니면 꺼짐", "A classic-computer booth's switch is simply on or off"),
         "caption": ("스위치는 켜짐 아니면 꺼짐, 둘 중 하나예요.", "A switch is either on or off — one or the other."),
         "small": ("우리가 쓰는 컴퓨터는 전부 이 스위치(0, 1)로 돼 있어요.", "Every computer we use is built from switches like this — 0 or 1.")},
        {"svg": P2, "alt": ("시연 담당자가 경우의 수가 너무 많다며 진땀을 흘림", "A demo staffer sweats over the sheer number of cases to check"),
         "caption": ("경우의 수가 너무 많으면, 하나씩 다 보기엔 시간이 모자라요.", "When there are too many cases, checking them one by one takes forever."),
         "small": ("스위치 컴퓨터는 한 번에 한 경우만 확인할 수 있어요.", "A switch-based computer can only check one case at a time.")},
        {"svg": P3, "hero": True, "alt": ("부스 안에서 동전이 빙글빙글 돌며 앞뒤가 흐릿하게 겹쳐 보임", "A coin spins inside the booth, heads and tails blurring together"),
         "caption": ("양자 컴퓨팅은 돌아가는 동전처럼 0과 1을 동시에 품은 큐비트로 계산해요.", "Quantum computing computes with qubits that hold 0 and 1 at once, like a spinning coin."),
         "small": ("큐비트는 여러 경우를 한꺼번에 품고, 정답 쪽 확률을 키워서 풀어요.", "Qubits hold many cases at once and boost the odds of the right answer."),
         "tricks": (4, [
             (SWITCH_I, ("고전 비트", "Classic bit"), ("0 아니면 1이에요", "either 0 or 1")),
             (QUBIT_I, ("큐비트(중첩)", "Qubit (superposition)"), ("0과 1을 동시에 품어요", "holds 0 and 1 at once"), "calm"),
             (LINK_I, ("얽힘", "Entanglement"), ("두 큐비트가 서로 연결돼요", "two qubits become linked")),
             (MANY_I, ("동시에 품고 풀기", "Hold many at once"), ("여러 경우를 한꺼번에 품어요", "holds many cases at once"), "warm"),
         ])},
        {"svg": P4, "alt": ("비트와 큐비트를 비교하는 설명판: 큐비트는 동시에, 얽혀서, 특정 문제에만 빠름", "A board compares bit vs qubit: qubits hold both at once, link together, and speed up only certain problems"),
         "caption": ("고전 비트는 0 아니면 1 중 하나만, 큐비트는 0과 1을 동시에 품어요.", "A classic bit holds just 0 or 1; a qubit holds both at once."),
         "small": ("양자 컴퓨터는 암호 풀기·분자 시뮬레이션 같은 문제에 특히 강해요.", "Quantum computers are especially strong at code-breaking and molecule simulation.")},
        {"svg": P5, "alt": ("왼쪽: 동전이 살짝만 건드려도 멈춤. 오른쪽: 평범한 계산은 고전 컴퓨터가 더 빠름", "Left: the coin stops the instant it's disturbed. Right: for ordinary math, the classic computer still wins"),
         "caption": ("큐비트는 작은 흔들림에도 오류가 나고, 평범한 계산은 고전 컴퓨터가 더 빨라요.", "Qubits err at the tiniest disturbance, and classic computers are still faster at ordinary math."),
         "small": ("양자 컴퓨터는 만능이 아니라, 특정 문제에 강한 특수 도구예요.", "A quantum computer isn't all-purpose — it's a specialist tool for particular problems.")},
    ],
    "summary": (("<b>양자 컴퓨팅</b> = <b>중첩</b>과 <b>얽힘</b>을 가진 큐비트로, 특정 문제를 <b>여러 경우를 한꺼번에 품고</b> 푸는 계산 방식.",
                 "<b>Quantum computing</b> = a way of computing with qubits that hold <b>superposition</b> and <b>entanglement</b>, working on certain problems with <b>many cases held at once</b>."),
                ("양자 컴퓨팅은 큐비트(qubit)의 중첩(superposition)과 얽힘(entanglement)을 이용해, 특정 유형의 문제(소인수분해, 조합 최적화, 분자 시뮬레이션 등)를 고전 컴퓨터보다 훨씬 빠르게 풀 잠재력을 가진 계산 패러다임이에요. 모든 계산을 대체하는 것이 아니라, 특정 알고리즘에서만 우위를 가져요.",
                 "Quantum computing uses a qubit's superposition and entanglement to potentially solve certain problem types — integer factorization, combinatorial optimization, molecule simulation — far faster than classical computers. It doesn't replace general computing; its advantage shows up only in specific algorithms.")),
    "glossary": [
        ("큐비트", "Qubit", ("0과 1을 동시에 품는 동전.", "The coin that holds 0 and 1 at once."), ("양자 컴퓨팅의 가장 작은 단위예요.", "The smallest unit of quantum computing.")),
        ("중첩", "Superposition", ("0과 1이 겹쳐 있는 상태, 동전이 도는 모습 같아요.", "0 and 1 overlapping, like a coin still spinning."), ("큐비트를 재는 순간 0이나 1, 하나로 정해져요.", "The instant you measure a qubit, it settles to just 0 or 1.")),
        ("양자 얽힘", "Entanglement", ("두 큐비트가 서로 연결된 상태.", "Two qubits linked to each other."), ("한 큐비트를 재면 다른 큐비트도 즉시 정해져요.", "Measure one qubit and the other is instantly decided too.")),
        ("양자 우월성", "Quantum Supremacy", ("특정 문제에서 고전 컴퓨터가 못 따라가는 순간.", "The moment a classic computer can't keep up on a given problem."), ("특정 문제 하나에서만 증명된 우위예요.", "A lead proven on one specific problem, not computing in general.")),
        ("양자내성암호(PQC)", "Post-Quantum Cryptography", ("양자 컴퓨터로도 깨기 어렵게 설계한 암호.", "Cryptography designed to resist even quantum computers."), ("지금 쓰는 암호를 미리 바꿔두는 대비책이에요.", "A safeguard that swaps out today's cryptography ahead of time.")),
        ("양자암호통신(QKD)", "Quantum Key Distribution", ("양자 성질로 도청을 들키는 통신.", "Communication where quantum properties expose any eavesdropper."), ('양자 컴퓨팅과는 다른, 양자 통신 응용이에요. → <a href="qkdcomm-ko.html">엿들으면 바로 티 나는 빛 알갱이 열쇠</a>', 'A different quantum application — communication, not computing. → <a href="qkdcomm-en.html">the key of light that shows the moment it\'s watched</a>')),
        ("고전 컴퓨터", "Classical Computer", ("스위치(0, 1)로 돌아가는 익숙한 컴퓨터.", "The familiar computer running on 0-or-1 switches."), ("일상적인 계산은 여전히 고전 컴퓨터가 빨라요.", "For everyday computation, a classical computer is still faster.")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
