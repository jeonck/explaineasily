from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
FRIEND = dict(hat="var(--good)", shirt="var(--good)")


def letter(x, y, text, s=1.0, rot=0, glow=False):
    g = '<rect x="-4" y="-34" width="148" height="88" rx="8" fill="none" stroke="#5B8DEF" stroke-width="3" opacity="0.6"/>' if glow else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">{g}<rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(70, 34, text, 13, "#142033", cls="d") + '<rect x="16" y="52" width="70" height="4" rx="2" fill="#C9A86A"/></g>')


def photon(x, y, s=1.0, color="#5B8DEF"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="{color}"/>'
            f'<circle r="16" fill="none" stroke="{color}" stroke-width="2" opacity="0.5"/></g>')


def calc(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-36" width="60" height="72" rx="6" fill="var(--night)"/>'
            '<rect x="-22" y="-28" width="44" height="16" rx="2" fill="#5B8DEF"/>'
            + "".join(f'<rect x="{-22 + (i % 3) * 16}" y="{-4 + (i // 3) * 14}" width="12" height="10" rx="1" fill="#C9D5E6"/>' for i in range(9)) + "</g>")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 지금 자물쇠 편지도 언젠가 풀릴까 봐 걱정이에요
P1 = svg(280, sky(280)
         + person(130, 150, s=0.85, **ME) + letter(220, 120, "ㅋ#7@…x!Q")
         + calc(560, 150, 1.1) + label(560, 230, "⟦미래의 아주 센 계산기|a far stronger future computer⟧", 12, "var(--muted)")
         + '<path d="M400 160 L500 160" stroke="var(--bad)" stroke-width="2" stroke-dasharray="6 6"/>'
         + label(380, 262, "⟦수학으로 꼰 자물쇠도 언젠가 다 풀릴 수 있대요|a lock twisted from math might someday be solved — all of it⟧", 13, "var(--ink)"))

# 2. 복사해 가도 들키지 않아요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + person(130, 150, s=0.85, **ME) + letter(220, 120, "ㅋ#7@…x!Q")
         + person(400, 140, s=0.7, face=MASK) + letter(480, 110, "ㅋ#7@…x!Q", 0.75, rot=6)
         + label(480, 200, "⟦몰래 복사|a secret copy⟧", 11, "var(--bad)")
         + person(660, 150, s=0.85, face=SMILE, **FRIEND)
         + label(380, 258, "⟦복사해 가도 아무 흔적이 안 남아요 — 들킬 방법이 없어요|a copy leaves no trace — there's no way to know it happened⟧", 13, "var(--ink)"))

# 3. 양자암호통신 = 엿들으면 바로 티 나는 빛 알갱이 열쇠 (hero)
P3 = svg(340, sky(340)
         + person(70, 160, s=0.85, **ME) + photon(170, 150, 1.1) + photon(200, 140, 1.1) + photon(230, 160, 1.1)
         + person(420, 110, s=0.7, face=MASK)
         + '<g transform="translate(300,150)">' + f'<path d="M-20 0 h40" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>' + "</g>"
         + label(300, 90, "⟦엿보려는 순간, 빛의 상태가 바뀌어요|the instant it's peeked at, the light's state changes⟧", 12, "var(--bad)", cls="d")
         + photon(560, 150, 1.1, color="var(--bad)") + label(560, 190, "⟦값이 흐트러져요|the value is scrambled⟧", 11, "var(--bad)")
         + person(680, 160, s=0.85, face=FROWN, **FRIEND) + bubble(600, 230, 150, 34, "⟦엿들었네요! 버릴게요|someone peeked — discard it!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 30, "⟦양자암호통신 = 빛 알갱이로 만든 열쇠, 엿보면 바로 티 나요|QKD = a key made of light; the moment it's watched, it shows⟧", 13, "var(--ink)", cls="d"))

# 4. 비교표: 수학 기반 자물쇠 vs 물리법칙 기반 QKD
P4 = svg(300, sky(300)
         + box(50, 30, 310, 240, "⟦지금 암호(수학 기반)|TODAY'S ENCRYPTION (math-based)⟧",
               ("⟦계산이 어려워서 못 풀어요|hard to compute — that's the lock⟧", "⟦미래의 센 계산기엔 위험할 수 있어요|a far stronger computer might crack it⟧", "⟦엿봐도 티가 안 나요|peeking leaves no trace⟧"), 12)
         + box(400, 30, 310, 240, "⟦QKD(물리법칙 기반)|QKD (physics-based)⟧",
               ("⟦빛의 성질이라 계산으론 못 뚫어요|a property of light — no computation breaks it⟧", "⟦엿보면 값이 바뀌어서 바로 들켜요|peeking changes the value — instantly caught⟧", "⟦내용은 결국 기존 자물쇠로 잠가요|the message itself is still locked with ordinary encryption⟧"), 12))

# 5. 거리 제한과 비용
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + person(100, 150, s=0.8, **ME) + photon(190, 140, 0.9)
         + '<path d="M210 140 L330 140" stroke="#5B8DEF" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(270, 120, "⟦빛은 멀리 못 가요|light can't travel far⟧", 11, "var(--bad)")
         + '<rect x="330" y="110" width="50" height="60" rx="6" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/>' + label(355, 190, "⟦중계소|a relay station⟧", 10, "var(--muted)")
         + '<path d="M380 140 L470 140" stroke="#5B8DEF" stroke-width="3" stroke-dasharray="6 4"/>'
         + photon(490, 140, 0.9) + person(580, 150, s=0.8, face=SMILE, **FRIEND)
         + label(380, 258, "⟦중계소가 많이 필요하고 장비도 비싸요 — 아직 일부 구간만 써요|needs many relays and costly gear — still used on only a few stretches⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "qkdcomm", "order": 5,
    "title": ("엿들으면 바로 티 나는 빛 알갱이 열쇠", "The Key of Light That Shows the Moment It's Watched"),
    "h1": ("<em>양자암호통신</em>이 뭐예요?", "What is <em>Quantum Key Distribution (QKD)</em>?"),
    "sub": ("양자암호통신(QKD)을 엿들으면 바로 티가 나는 빛 알갱이 열쇠 이야기로 풀어봤어요.",
            "Quantum key distribution, told as a story about a key made of light that shows the moment someone peeks at it."),
    "panels": [
        {"svg": P1, "alt": ("친구가 자물쇠 편지를 들고 있고, 멀리 아주 센 미래 계산기가 그 편지를 풀 수 있을까 봐 걱정하는 모습", "A friend holds a padlocked letter while, in the distance, a far stronger future computer looms as a worry"),
         "caption": ("지금 자물쇠 편지도 언젠가 풀릴까 봐 걱정이에요.", "Even today's padlocked letter might someday be cracked."),
         "small": ('<a href="encryption-ko.html">수학으로 꼰 자물쇠</a>도 아주 센 미래 계산기(양자컴퓨터) 앞에선 위험할 수 있대요.',
                   'A <a href="encryption-en.html">lock twisted from math</a> might not hold up against a far stronger future computer (a quantum computer).')},
        {"svg": P2, "alt": ("가면 쓴 사람이 자물쇠 편지를 몰래 베껴 가는데 아무 표시도 남지 않음", "A masked figure secretly copies the padlocked letter, leaving no sign behind"),
         "caption": ("복사해 가도 들키지 않아요.", "A secret copy leaves no trace."),
         "small": ("몰래 베껴 가도 아무 흔적이 안 남아요 — 들킬 방법이 없어요.", "A copy can be taken and nothing shows it ever happened.")},
        {"svg": P3, "hero": True, "alt": ("빛 알갱이 세 개가 친구에게 날아가는데, 가면 쓴 사람이 엿보는 순간 빛의 값이 흐트러지고 친구가 '엿들었네요! 버릴게요'", "Three particles of light fly toward a friend; the instant a masked figure peeks, the light's value scrambles, and the friend says someone peeked — discard it!"),
         "caption": ("양자암호통신은 빛 알갱이로 만든 열쇠예요. 엿보면 바로 티가 나요.", "QKD is a key made of particles of light. The moment it's peeked at, it shows."),
         "small": ("엿들으면 빛의 상태 자체가 바뀌어요. 그 흐트러진 값은 그냥 버리고 새로 만들어요.", "Peeking changes the light's state itself. The scrambled values are simply discarded and new ones made."),
         "tricks": (4, [
             (icon('<circle cx="32" cy="32" r="10" fill="#5B8DEF"/><circle cx="32" cy="32" r="18" fill="none" stroke="#5B8DEF" stroke-width="3"/>'),
              ("빛 알갱이 열쇠", "A key of photons"), ("양자 상태로 된 열쇠 조각", "key bits held in a quantum state"), "calm"),
             (icon('<path d="M16 32 h12 M36 32 h12" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 4"/><circle cx="32" cy="32" r="6" fill="var(--bad)"/>'),
              ("엿보면 바뀌어요", "Watching changes it"), ("관측하면 상태가 깨져요", "observation breaks the state"), "warm"),
             (icon('<path d="M20 20 L44 44 M44 20 L20 44" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'),
              ("들키면 버려요", "Caught, it's discarded"), ("그 조각은 새로 만들어요", "those bits are generated again")),
             (icon('<rect x="14" y="18" width="36" height="28" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="32" r="5" fill="#E9B44C"/>'),
              ("내용은 기존 자물쇠로", "The message: ordinary locks"), ("QKD는 열쇠만 나눠 줘요", "QKD only hands out the key"), "calm"),
         ])},
        {"svg": P4, "alt": ("두 상자 비교: 지금 암호(수학 기반, 계산이 어려워 안전, 미래 계산기엔 위험할 수 있음, 엿봐도 티 안 남) vs QKD(물리법칙 기반, 계산으론 못 뚫음, 엿보면 바로 들킴, 내용은 결국 기존 자물쇠)", "Two boxes compared: today's encryption (math-based, safe because it's hard to compute, a future computer might crack it, peeking leaves no trace) vs QKD (physics-based, no computation breaks it, peeking is instantly caught, the message itself still uses ordinary locks)"),
         "caption": ("지금 암호와 QKD는 안전한 이유 자체가 달라요.", "Today's encryption and QKD are safe for entirely different reasons."),
         "small": ("하나는 계산이 어려워서, 하나는 빛의 성질 때문에 안전해요. 그래서 QKD는 도청 자체를 즉시 알아챌 수 있어요.", "One is safe because the math is hard; the other because of a property of light. That's why QKD can catch eavesdropping the instant it happens.")},
        {"svg": P5, "alt": ("빛 알갱이가 먼 거리를 가지 못해 중계소를 거쳐 전달되는 모습", "A particle of light can't travel far, so it passes through a relay station to reach its destination"),
         "caption": ("거리 제한과 비용이 한계예요.", "Distance and cost are the limits."),
         "small": ("중계소가 많이 필요하고 장비도 비싸서, 아직 일부 구간에서만 써요.", "It needs many relay stations and costly equipment, so it's still used on only a few stretches.")},
    ],
    "summary": (("<b>양자암호통신(QKD)</b> = <b>빛 알갱이</b>로 만든 열쇠를 주고받는 것. <b>엿보면 빛의 상태가 바뀌어</b> 도청이 바로 드러나요.",
                 "<b>Quantum Key Distribution (QKD)</b> = exchanging a key made of <b>particles of light</b>. <b>Peeking changes the light's state</b>, so eavesdropping is caught instantly."),
                ("QKD(Quantum Key Distribution)는 양자역학의 '관측하면 상태가 바뀐다'는 성질을 이용해 암호 키를 분배하는 기술이에요. 기존 공개키 암호가 계산 복잡도에 의존해 미래의 양자컴퓨터에 취약할 수 있는 것과 달리, QKD는 물리 법칙 자체로 도청을 탐지해요. 단, QKD는 키 분배만 담당하고 실제 메시지는 대칭키 암호로 암호화하며, 전송 거리 제한과 높은 구축 비용이 실용화의 걸림돌이에요. 수학적 알고리즘으로 양자컴퓨터에 대응하는 PQC(양자내성암호)와는 접근 방식이 다른 별개의 기술이에요.",
                 "QKD distributes cryptographic keys using the quantum-mechanical property that observation disturbs a system's state. Unlike public-key encryption, which relies on computational hardness and may be vulnerable to future quantum computers, QKD detects eavesdropping through physics itself. QKD only distributes the key; the message itself is still encrypted with symmetric encryption. Distance limits and high deployment costs remain obstacles to wide use. It is a separate technology from PQC (post-quantum cryptography), which instead uses math-based algorithms designed to resist quantum computers.")),
    "glossary": [
        ("양자암호통신(QKD)", "Quantum Key Distribution", ("빛 알갱이 열쇠 나누기.", "Sharing a key made of light."), ("엿보면 상태가 바뀌는 물리 법칙으로 도청을 잡아내요.", "Catches eavesdropping through the physical law that observation disturbs the state.")),
        ("광자", "Photon", ("빛 알갱이.", "A particle of light."), ("열쇠 조각 하나하나를 실어 나르는 단위예요.", "The unit that carries each bit of the key.")),
        ("양자컴퓨터 위협", "Quantum computer threat", ("미래의 센 계산기.", "The far stronger future computer."), ("지금 암호 중 일부를 계산으로 풀어버릴 수 있다고 걱정돼요.", "Could someday crack some of today's encryption through sheer computation.")),
        ("PQC(양자내성암호)", "Post-Quantum Cryptography", ("다른 접근 — 수학으로 버티기.", "A different approach — holding out with math."), ("QKD와 달리 새로운 수학 알고리즘으로 미래 계산기에 대비해요.", "Unlike QKD, it uses new math-based algorithms to prepare for future computers.")),
        ("도청 탐지", "Eavesdropping detection", ("엿보면 바로 들켜요.", "A peek is caught instantly."), ("QKD만의 특징 — 물리 법칙이 알려줘요.", "A feature unique to QKD — the physics itself gives it away.")),
        ("키 분배", "Key distribution", ("열쇠만 전달.", "Delivering only the key."), ('실제 편지는 여전히 기존 자물쇠로 잠가요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'The letter itself is still locked with ordinary encryption. → <a href="encryption-en.html">the letter nobody can read without the key</a>')),
        ("거리 제한·중계기", "Distance limits, relays", ("빛은 멀리 못 가요.", "Light can't travel far."), ("중계소를 거쳐야 하고, 그만큼 장비가 늘어나요.", "Needs relay stations, which means more equipment.")),
        ("구축 비용", "Deployment cost", ("아직 비싸요.", "Still expensive."), ("그래서 전체 통신이 아니라 일부 중요한 구간에서만 써요.", "That's why it's used only on a few critical stretches, not across all communications.")),
    ],
}
