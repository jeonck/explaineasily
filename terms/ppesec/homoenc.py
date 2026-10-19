from _draw import *

SCRIBE = dict(hat="var(--stone-dark)", shirt="#4A5A72")
VILLAGER1 = dict(hat=None, shirt="#4A7A6A", face=SMILE)
VILLAGER2 = dict(hat=None, shirt="#7B3FA0", face=SMILE)
VILLAGER3 = dict(hat=None, shirt="#B5651D", face=SMILE)


def card(x, y, w, h, text, sealed=True):
    body = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
    if sealed:
        lines = f'<path d="M{x + 10} {y + h / 2 - 7} h{w - 20} M{x + 10} {y + h / 2 + 7} h{w - 20}" stroke="#C9A86A" stroke-width="2" stroke-dasharray="3 3"/>'
        seal = f'<circle cx="{x + w - 15}" cy="{y + 15}" r="10" fill="var(--bad)"/>'
        return body + lines + seal
    return body + label(x + w / 2, y + h / 2 + 5, text, 15, "#142033", cls="d")


def plus(x, y, size=14, color="var(--ink)"):
    return f'<path d="M{x - size} {y} h{size * 2} M{x} {y - size} v{size * 2}" stroke="{color}" stroke-width="4" stroke-linecap="round"/>'


# 1. 서기가 세 상인의 비밀 금액을 더해야 해요
P1 = svg(345, sky(345)
         + person(380, 110, s=0.9, face=EYES, **SCRIBE)
         + bubble(260, 30, 240, 40, "⟦셋을 더해야 하는데, 봉인을 뜯어야 셈이 돼요|I need to add these — but I can only do math by breaking the seal⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(120, 190, s=0.65, **VILLAGER1) + card(90, 110, 70, 50, "") + label(125, 250, "⟦비밀 금액 A|secret amount A⟧", 11, "var(--muted)")
         + person(380, 235, s=0.65, **VILLAGER2) + card(350, 155, 70, 50, "") + label(385, 325, "⟦비밀 금액 B|secret amount B⟧", 11, "var(--muted)")
         + person(640, 190, s=0.65, **VILLAGER3) + card(610, 110, 70, 50, "") + label(645, 250, "⟦비밀 금액 C|secret amount C⟧", 11, "var(--muted)"))

# 2. 더하려면 뜯어야 하고, 뜯으면 비밀이 사라져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(240, 150, s=0.85, face=EYES, **SCRIBE)
         + card(120, 60, 80, 54, "⟦30|30⟧", sealed=False)
         + '<path d="M130 70 L150 90 M190 70 L170 90" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
         + label(160, 230, "⟦뜯어서 봤어요|opened it to read it⟧", 12, "var(--bad)")
         + bubble(330, 40, 230, 40, "⟦이제 A의 금액이 30인 걸 서기가 다 알아요|now the scribe knows A's amount is 30⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦계산 한 번에 비밀 하나가 사라져요|every calculation costs you one secret⟧", 12, "var(--ink)", cls="d"))

# 3. 동형암호 = 봉인째로 더하는 셈 (hero)
P3 = svg(340, sky(340)
         + card(60, 100, 90, 60, "") + plus(176, 130) + card(216, 100, 90, 60, "") + plus(332, 130) + card(372, 100, 90, 60, "")
         + label(295, 60, "⟦=|=⟧", 22, "var(--ink)", cls="d")
         + '<path d="M470 130 h50" stroke="var(--ink)" stroke-width="4"/><path d="M510 122 l10 8 l-10 8" stroke="var(--ink)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + card(530, 100, 110, 60, "")
         + label(585, 70, "⟦봉인된 합계|the sealed total⟧", 11, "var(--muted)")
         + person(660, 220, s=0.8, **VILLAGER1)
         + label(660, 300, "⟦금액 주인만 이 도장(열쇠)으로 열어요|only the amount's owner unseals it, with their own key⟧", 11, "var(--good)")
         + label(380, 320, "⟦서기는 한 번도 뜯지 않고 더했어요|the scribe added them without ever breaking a seal⟧", 13, "var(--ink)", cls="d"))

ADD_I = icon('<rect x="8" y="16" width="48" height="32" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M32 24 v16 M24 32 h16" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
MUL_I = icon('<rect x="8" y="16" width="48" height="32" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 24 l16 16 M40 24 l-16 16" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
NOPEEK_I = icon('<path d="M10 32 q22 -20 44 0 q-22 20 -44 0z" fill="none" stroke="var(--muted)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--muted)"/><path d="M12 14 L52 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
SLOW_I = icon('<circle cx="32" cy="34" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 22 v12 l9 5" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M14 14 l6 6 M50 14 l-6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "homoenc", "order": 13,
    "title": ("뜯지 않고 셈하는 봉인 편지", "The Sealed Letter You Can Do Math On"),
    "h1": ("<em>동형암호</em>가 뭐예요?", "What is <em>Homomorphic Encryption</em>?"),
    "sub": ("동형암호(Homomorphic Encryption)를, 봉인을 뜯지 않고도 안의 숫자를 더할 수 있는 편지 이야기로 풀어봤어요.",
            "Homomorphic encryption, told as a story about a sealed letter whose number you can add without breaking the seal."),
    "panels": [
        {"svg": P1, "alt": ("서기가 세 상인의 봉인된 금액 카드를 더해야 한다고 말함", "A scribe says he needs to add up three sealed amount cards from three villagers"),
         "caption": ("서기가 세 상인의 비밀 금액을 더해야 해요.", "The scribe needs to add up three secret amounts."),
         "small": ("셋을 더해야 하는데, 지금까지는 봉인을 뜯어야만 셈이 됐어요.", "He needs the total — but until now, adding meant breaking the seal first.")},
        {"svg": P2, "alt": ("서기가 카드를 뜯어 30을 보고, 이제 A의 비밀 금액을 서기가 다 안다는 말풍선", "The scribe opens a card, sees 30, and a speech bubble says the scribe now knows A's secret amount"),
         "caption": ("뜯어서 더하면, 비밀이 사라져요.", "Open it to add it, and the secret is gone."),
         "small": ("계산 한 번에 비밀 하나가 사라져요. 더할 사람마다 다 보여줘야 했어요.", "Every calculation costs a secret. Each amount had to be shown to whoever does the adding.")},
        {"svg": P3, "hero": True, "alt": ("봉인된 카드 세 장을 더해 봉인된 합계 카드를 만들고, 주인만 자기 열쇠로 염", "Three sealed cards are added to make one sealed total card, which only the owner unseals with their own key"),
         "caption": ("동형암호는 봉인째로 더하는 셈이에요.", "Homomorphic encryption adds the cards while they're still sealed."),
         "small": ('서기는 한 번도 뜯지 않고 더했어요. 열 수 있는 건 <a href="encryption-ko.html">열쇠</a>를 가진 주인뿐이에요.',
                   'The scribe added them without ever breaking a seal. Only the owner holding the key can open the result.'),
         "tricks": (4, [
             (ADD_I, ("더하기도 봉인한 채", "Add while still sealed"), ("뜯지 않고 셈해요", "math, without opening it"), "calm"),
             (MUL_I, ("곱하기도 되는 것도", "Some can multiply too"), ("완전 동형암호는 더 많이 해요", "fully homomorphic schemes do more")),
             (NOPEEK_I, ("계산하는 사람은 못 봐요", "The one computing can't peek"), ("서기도 숫자를 몰라요", "even the scribe never sees the number"), "warm"),
             (SLOW_I, ("느리고 무거워요", "Slow and heavy"), ("셈이 보통보다 훨씬 오래 걸려요", "the math takes far longer than usual")),
         ])},
        {"svg": svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
                    + label(190, 30, "⟦보통 계산|plain computation⟧", 13, "var(--ink)", cls="d")
                    + label(190, 70, "⟦① 뜯는다|① open it⟧", 12, "var(--ink)") + label(190, 100, "⟦② 더한다|② add it⟧", 12, "var(--ink)")
                    + label(190, 130, "⟦③ 결과가 다 보여요|③ the result is exposed⟧", 12, "var(--bad)")
                    + label(570, 30, "⟦동형암호 계산|homomorphic computation⟧", 13, "var(--ink)", cls="d")
                    + label(570, 70, "⟦① 봉인된 채 더한다|① add while sealed⟧", 12, "var(--ink)") + label(570, 100, "⟦② 결과도 봉인|② the result stays sealed⟧", 12, "var(--ink)")
                    + label(570, 130, "⟦③ 주인만 열어요|③ only the owner opens it⟧", 12, "var(--good)")
                    + card(140, 170, 100, 60, "⟦58|58⟧", sealed=False) + card(530, 170, 100, 60, "")
                    + label(380, 300, "⟦같은 셈이지만, 비밀이 드러나는 때가 달라요|the same sum, but privacy breaks at a different step⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 보통 계산은 뜯고 더하고 결과가 드러남. 오른쪽: 동형암호는 봉인된 채 더하고 주인만 결과를 염", "Left: plain computation opens, adds, and exposes the result. Right: homomorphic computation adds while sealed, and only the owner opens the result"),
         "caption": ("무엇이 다른지 나란히 보면 이래요.", "Side by side, here's the difference."),
         "small": ("같은 셈이지만, 비밀이 드러나는 때가 서로 달라요.", "The same sum — but privacy breaks at a different point in each.")},
        {"svg": svg(300, sky(300)
                    + person(160, 140, s=0.85, face=EYES, **SCRIBE) + card(230, 100, 90, 60, "")
                    + label(160, 250, "⟦덧셈만 되는 간단한 버전도 있어요|a simpler kind does only addition⟧", 11, "var(--muted)")
                    + person(560, 140, s=0.85, **VILLAGER2) + label(560, 250, "⟦더하기+곱하기 다 되는 건 훨씬 느려요|add + multiply together runs much slower⟧", 11, "var(--muted)")
                    + label(380, 280, "⟦클라우드에 맡긴 의료·금융 자료를 계산할 때 주로 써요|mostly used for computing on medical or financial data handed to the cloud⟧", 12, "var(--ink)", cls="d")),
         "alt": ("부분 동형암호(덧셈만)와 완전 동형암호(덧셈+곱셈)를 비교", "Comparing partial homomorphic encryption (addition only) with fully homomorphic encryption (addition and multiplication)"),
         "caption": ("다 되는 건 아니고, 느려요.", "It can't do everything, and it's slow."),
         "small": ('클라우드에 맡긴 의료·금융 자료를 계산할 때 주로 써요. 개인을 지키며 통계 내는 다른 방법도 있어요 → <a href="ppdm-ko.html">PPDM</a>',
                   'Mostly used to compute on medical or financial data handed to the cloud. Other ways to mine statistics while protecting individuals exist too → <a href="ppdm-en.html">PPDM</a>')},
    ],
    "summary": (("<b>동형암호</b> = 편지를 <b>봉인한 채로</b> 더하거나 곱할 수 있는 암호. 계산하는 사람은 내용을 못 보고, <b>결과도 봉인된 채</b> 나와서 주인만 열 수 있어요.",
                 "<b>Homomorphic encryption</b> = a cipher that lets you add or multiply a letter <b>while it stays sealed</b>. Whoever computes never sees the content, and the <b>result comes out sealed too</b> — only the owner can open it."),
                ("Homomorphic Encryption. 암호문 상태 그대로 연산해 같은 연산을 평문에 한 것과 같은 결과(암호문)를 얻는 암호 기법이에요. 덧셈만 지원하는 부분 동형암호(PHE, 예: Paillier)와 덧셈·곱셈을 모두 지원하는 완전 동형암호(FHE)로 나뉘고, 클라우드에 민감 데이터를 맡기고 계산시키되 내용은 숨기는 용도로 쓰여요. 연산 비용이 매우 커서 아직 제한적으로 쓰여요.",
                 "A cryptographic technique that lets you operate directly on ciphertext and get a result that, once decrypted, matches applying the same operation to the plaintext. Partial homomorphic encryption (PHE, e.g. Paillier) supports addition only; fully homomorphic encryption (FHE) supports both addition and multiplication. It lets a cloud compute on sensitive data without ever seeing it, though the computational cost is still very high.")),
    "glossary": [
        ("동형암호", "Homomorphic encryption", ("봉인째로 셈이 되는 편지.", "A letter you can do math on while sealed."), ("암호문 그대로 연산해요. 결과를 복호화하면 평문 연산 결과와 같아요.", "You operate on the ciphertext itself. Decrypt the result, and it matches operating on the plaintext.")),
        ("부분 동형암호(PHE)", "Partial HE", ("덧셈만 되는 간단한 버전.", "A simpler version that only adds."), ("더하기 한 가지 연산만 암호문 상태로 지원해요.", "Supports only one operation — addition — directly on ciphertext.")),
        ("완전 동형암호(FHE)", "Fully HE", ("더하기·곱하기 다 되는 버전.", "A version that both adds and multiplies."), ("훨씬 유연하지만 훨씬 느려요.", "Far more flexible, but far slower too.")),
        ("암호문 연산", "Ciphertext computation", ("봉인된 채로 셈.", "Doing the math while it's sealed."), ("계산자는 내용을 몰라도 돼요.", "The one computing never needs to know the content.")),
        ("기밀 계산", "Confidential computing", ("계산하는 동안도 숨기기.", "Hiding it even while it's being computed on."), ("동형암호는 이 목표를 암호로 이루는 한 가지 방법이에요.", "Homomorphic encryption is one cryptographic way to reach this goal.")),
        ("복호화", "Decryption", ("봉인을 여는 것.", "Opening the seal."), ('일반 암호화는 계산 전에 열어야 해요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Ordinary encryption has to be opened before you compute. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("클라우드 위탁 계산", "Outsourced cloud computation", ("빌린 창고에 계산을 맡기는 것.", "Handing the computing to a rented warehouse."), ("내용을 보여주지 않고도 맡길 수 있게 해줘요.", "Lets you hand it over without ever showing the content.")),
        ("PPDM", "PPDM", ("개인을 지키며 통계 내는 다른 기법들.", "Other techniques for mining statistics while protecting individuals."), ('동형암호는 PPDM이 쓰는 도구 중 하나예요. → <a href="ppdm-ko.html">PPDM</a>', 'Homomorphic encryption is one tool PPDM uses. → <a href="ppdm-en.html">PPDM</a>')),
    ],
}
