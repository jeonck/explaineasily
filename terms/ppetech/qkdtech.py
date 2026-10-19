from _draw import *
from _world import *


def photonbeam(x1, y1, x2, y2, broken=False):
    stroke = "var(--bad)" if broken else "var(--accent)"
    out = f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{stroke}" stroke-width="2" stroke-dasharray="3 5"/>'
    for t in (0.3, 0.55, 0.8):
        px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        out += f'<circle cx="{px}" cy="{py}" r="4" fill="{stroke}"/>'
    return out


def lockbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-6" width="44" height="34" rx="4" fill="#4A5A72"/>'
            f'<path d="M-10 -6 v-12 a10 10 0 0 1 20 0 v12" stroke="#4A5A72" stroke-width="5" fill="none"/></g>')


def eavesdrop(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})">{person(0, 0, s=1.0, face=EYES, hat=None, shirt="#5A3B22")}<path d="M50 20 l14 -10 M50 32 l14 2" stroke="var(--bad)" stroke-width="2"/></g>'


# 1. 엿들어도 아무도 몰라요 (기존 방식)
P1 = svg(300, sky(300, ground=False)
         + lockbox(180, 170, 1.3) + lockbox(560, 170, 1.3)
         + photonbeam(230, 170, 510, 170)
         + eavesdrop(380, 100, 0.9)
         + label(380, 70, "⟦몰래 엿봤는데, 아무 흔적도 안 남아요|snooped in secret, and left no trace at all⟧", 12, "var(--bad)")
         + label(380, 270, "⟦기존 암호키 전달은 도청당해도 알아챌 방법이 없었어요|with old-style key exchange, there was no way to notice eavesdropping⟧", 12, "var(--ink)"))

# 2. 나중엔 양자컴퓨터가 지금 암호를 풀 수도 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + lockbox(380, 140, 1.6)
         + label(380, 90, "⟦지금은 안전해 보이는 열쇠|a key that looks safe for now⟧", 12, "var(--ink)")
         + label(380, 240, "⟦미래의 양자컴퓨터가 이 열쇠를 풀어버릴 수도 있어요|a future quantum computer might crack this very key⟧", 13, "var(--bad)"))

# 3. QKD = 엿보면 반드시 흔적이 남는 열쇠 나눔 (hero)
P3 = svg(340, '<rect width="760" height="340" fill="var(--night)"/>'
         + lockbox(180, 190, 1.3) + lockbox(580, 190, 1.3)
         + photonbeam(230, 190, 530, 190, broken=True)
         + eavesdrop(380, 110, 0.9)
         + label(380, 70, "⟦엿보려는 순간, 광자 상태가 변해 흔적이 남아요|the instant it's peeked at, the photon's state changes and leaves a trace⟧", 12, "#F5E6B8")
         + label(380, 30, "⟦QKD = 빛(광자) 한 알에 열쇠를 실어 보내, 엿보면 반드시 들통나는 열쇠 나눔 방식|QKD = sends the key riding on single photons, so any peek is bound to be caught⟧", 13, "#F5E6B8", cls="d")
         + label(380, 320, "⟦들통난 열쇠는 그냥 버리고 새로 나눠요|a caught key is simply discarded and redone⟧", 12, "#C9D5E6"))

QKD_PHOTON = icon('<circle cx="32" cy="32" r="8" fill="var(--accent)"/><path d="M14 32 h8 M42 32 h8" stroke="var(--accent)" stroke-width="3"/>')
QKD_DISTURB = icon('<circle cx="24" cy="32" r="7" fill="var(--accent)"/><path d="M40 20 l6 -6 M42 32 h10 M40 44 l6 6" stroke="var(--bad)" stroke-width="3"/>')
QKD_DISCARD = icon('<rect x="16" y="16" width="32" height="32" rx="4" fill="var(--bad)" opacity="0.7"/><path d="M22 22 l20 20 M42 22 l-20 20" stroke="#fff" stroke-width="3"/>')
QKD_SAFE = icon('<path d="M32 10 l20 8 v14 c0 14 -9 22 -20 28 c-11 -6 -20 -14 -20 -28 v-14z" fill="var(--good)"/>')

# 4. 기존 암호 vs QKD
P4 = svg(320, sky(320, ground=False)
         + infoboard(60, 40, 300, 240, "⟦기존 암호키 전달|OLD-STYLE KEY EXCHANGE⟧",
                     ("⟦도청 감지 — 못 해요|detect eavesdropping — no⟧", "⟦양자컴퓨터 — 언젠가 뚫릴 수 있어요|future quantum computers — may crack it⟧"), 1.0)
         + infoboard(400, 40, 300, 240, "⟦QKD|QKD⟧",
                     ("⟦도청 감지 — 반드시 들통나요|detect eavesdropping — always caught⟧", "⟦양자컴퓨터 — 원리상 안전해요|future quantum computers — safe by design⟧"), 1.0, hl=0)
         + label(380, 300, "⟦도청을 감지할 수 있다는 게 가장 큰 차이예요|the biggest difference: QKD can tell when it's being watched⟧", 12, "var(--ink)"))

# 5. 한계: 거리 제한, 비싼 장비, 암호화는 따로
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + photonbeam(140, 150, 300, 150) + label(220, 200, "⟦광섬유로는 거리 제한이 있어요|limited distance over optical fiber⟧", 11, "var(--ink)")
         + lockbox(600, 150, 1.2) + label(600, 220, "⟦열쇠만 나눠요, 암호화는 다른 알고리즘 몫이에요|only shares the key — actual encryption is a separate algorithm's job⟧", 11, "var(--ink)")
         + label(380, 282, "⟦QKD는 '안전한 열쇠 나눔'까지만 해줘요|QKD only handles the 'safe key sharing' part⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "qkdtech", "order": 13,
    "title": ("엿보면 반드시 들통나는 빛의 열쇠", "The Light-Key That Always Gets Caught When Peeked At"),
    "h1": ("<em>양자키분배(QKD)</em>가 뭐예요?", "What is <em>Quantum Key Distribution (QKD)</em>?"),
    "sub": ("QKD를, 빛(광자) 한 알 한 알에 열쇠를 실어 보내 엿보면 반드시 들통나는 이야기로 풀어봤어요.",
            "QKD, told as a story about sending a key riding on single photons of light, so that any attempt to peek is always caught."),
    "panels": [
        {"svg": P1, "alt": ("누군가 암호키 전달을 몰래 엿듣지만 아무 흔적도 남지 않음", "Someone secretly eavesdrops on a key exchange, leaving no trace at all"),
         "caption": ("몰래 엿봤는데, 아무 흔적도 안 남아요.", "Snooped in secret, and left no trace at all."),
         "small": ("기존 암호키 전달은 도청당해도 알아챌 방법이 없었어요.", "With old-style key exchange, there was no way to notice eavesdropping.")},
        {"svg": P2, "alt": ("지금은 안전해 보이는 열쇠가 미래의 양자컴퓨터에 풀릴 수 있다는 경고", "A warning that a key that looks safe now might be cracked by a future quantum computer"),
         "caption": ("지금은 안전해 보이는 열쇠예요.", "A key that looks safe for now."),
         "small": ("미래의 양자컴퓨터가 이 열쇠를 풀어버릴 수도 있어요.", "A future quantum computer might crack this very key.")},
        {"svg": P3, "hero": True, "alt": ("두 금고 사이에서 광자 빔이 오가고, 엿듣는 순간 광자 상태가 흔들려 흔적이 남음", "A photon beam travels between two boxes, and an eavesdropper's peek disturbs the photons, leaving a trace"),
         "caption": ("QKD는 빛(광자) 한 알에 열쇠를 실어 보내, 엿보면 반드시 들통나는 열쇠 나눔 방식이에요.", "QKD sends the key riding on single photons, so any peek is bound to be caught."),
         "small": ("들통난 열쇠는 그냥 버리고 새로 나눠요.", "A caught key is simply discarded and redone."),
         "tricks": (4, [
             (QKD_PHOTON, ("광자 하나에 정보 하나", "One photon, one bit"), ("아주 작은 단위로 보내요", "sent in the smallest possible unit"), "calm"),
             (QKD_DISTURB, ("관찰하면 상태가 변함", "Observing disturbs the state"), ("엿보면 흔적이 남아요", "a peek leaves a trace")),
             (QKD_DISCARD, ("도청 감지되면 버림", "Discard if eavesdropping is caught"), ("그 키는 그냥 안 써요", "simply not used")),
             (QKD_SAFE, ("안전한 키만 사용", "Only a safe key gets used"), ("암호화에 쓸 수 있어요", "ready for encryption"), "warm"),
         ])},
        {"svg": P4, "alt": ("기존 암호키 전달과 QKD를 도청 감지·양자컴퓨터 내성으로 비교하는 설명판", "A board comparing old-style key exchange and QKD on eavesdropping detection and quantum-computer resistance"),
         "caption": ("도청을 감지할 수 있다는 게 가장 큰 차이예요.", "The biggest difference: QKD can tell when it's being watched."),
         "small": ("양자컴퓨터가 발전해도 원리상 안전해요.", "Safe by design, even as quantum computers advance.")},
        {"svg": P5, "alt": ("왼쪽: 광섬유 거리 제한. 오른쪽: QKD는 열쇠만 나누고 실제 암호화는 다른 알고리즘이 맡음", "Left: limited distance over optical fiber. Right: QKD only shares the key — actual encryption is a separate algorithm's job"),
         "caption": ("광섬유 거리 제한과 비싼 장비가 걸림돌이에요.", "Limited fiber distance and expensive equipment are the obstacles."),
         "small": ("QKD는 '안전한 열쇠 나눔'까지만 해줘요.", "QKD only handles the 'safe key sharing' part.")},
    ],
    "summary": (("<b>QKD(양자키분배)</b>는 빛(광자) 한 알 한 알에 암호키를 실어 보내, <b>누가 엿보면 양자 성질 때문에 반드시 흔적이 남는</b> 열쇠 나눔 방식이에요.",
                 "<b>QKD (Quantum Key Distribution)</b> sends an encryption key riding on single photons of light, so that <b>any eavesdropping attempt is always caught</b> thanks to quantum properties."),
                ("QKD는 양자역학의 관측 교란 원리를 이용해, 도청이 발생하면 광자의 양자 상태가 바뀌어 송수신 양측이 이를 감지할 수 있게 하는 키 분배 기술이에요. 도청이 감지된 키는 폐기하고 안전한 키만 암호화에 사용해요. 다만 광섬유 거리 제한, 고가의 전용 장비가 필요하고, QKD 자체는 '안전한 키 분배'만 담당할 뿐 실제 데이터 암호화는 대칭키 알고리즘 같은 별도 수단과 함께 써야 해요.",
                 "QKD is a key-distribution technology that exploits quantum mechanics' observation-disturbance principle: any eavesdropping changes a photon's quantum state, letting both sender and receiver detect it. A key found to be eavesdropped on is discarded, and only a verified-safe key is used for encryption. However, it's limited by optical-fiber distance and needs expensive dedicated equipment, and QKD itself handles only 'safe key distribution' — actual data encryption still needs a separate method, like a symmetric-key algorithm.")),
    "glossary": [
        ("양자키분배(QKD)", "QKD", ("엿보면 들통나는 빛의 열쇠 나눔.", "A light-based key exchange that always gets caught when peeked at."), ("광자의 양자 성질을 이용해요.", "Relies on the quantum properties of photons.")),
        ("양자 얽힘·중첩", "Quantum Entanglement/Superposition", ("관측하면 상태가 바뀌는 양자의 성질.", "The quantum property where observing changes the state."), ("QKD가 도청을 감지하는 원리예요.", "The principle behind QKD's eavesdropping detection.")),
        ("대칭키 암호화", "Symmetric-Key Encryption", ("실제 데이터를 암호화하는 알고리즘.", "The algorithm that actually encrypts the data."), ("QKD가 나눈 열쇠를 여기에 써요.", "Uses the key QKD has safely shared.")),
        ("양자컴퓨터", "Quantum Computer", ("기존 암호를 풀 수도 있는 미래 기술.", "Future tech that might crack today's encryption."), ("QKD는 이 위협에도 안전하도록 설계됐어요.", "QKD is designed to stay safe even against this.")),
        ("블록체인 기술요소·보안", "Blockchain Tech & Security", ("해시·합의로 변조를 막는 다른 방식.", "A different way of blocking tampering, via hashing and consensus."), ('둘 다 신뢰를 지키는 기술이지만 방식이 달라요. → <a href="bctech-ko.html">블록체인 기술요소·보안 부스</a>', "Both protect trust, but in different ways. → <a href=\"bctech-en.html\">the Blockchain Tech & Security booth</a>")),
        ("광자", "Photon", ("열쇠 한 조각을 실어 나르는 빛 알갱이.", "The particle of light that carries one piece of the key."), ("QKD의 가장 작은 전달 단위예요.", "QKD's smallest unit of transmission.")),
        ("광섬유 거리 제한", "Fiber Distance Limit", ("QKD가 멀리 못 가는 이유.", "Why QKD can't yet travel very far."), ("실용화의 걸림돌 중 하나예요.", "One of the obstacles to wider use.")),
        ("개인키", "Private Key", ("QKD로 안전하게 나누는 대상.", "What QKD safely shares."), ("잃어버리면 QKD도 소용없어요.", "QKD can't help if this is lost.")),
    ],
}
