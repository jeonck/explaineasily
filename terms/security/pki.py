from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
MERCHANT = dict(hat="var(--accent)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
ROYAL = "#7B3FA0"


def seal(x, y, s=1.0, color=ROYAL, broken=False):
    """왕의 도장 자국: 보라 원 + 작은 왕관. broken 이면 빨간 X."""
    x_mark = '<path d="M-14 -14 l28 28 M14 -14 l-28 28" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>' if broken else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="{color}"/><circle r="15" fill="none" stroke="#FFF8E7" stroke-width="2"/>'
            f'<path d="M-9 5 l-2 -11 l6 4 l5 -8 l5 8 l6 -4 l-2 11z" fill="#E9B44C"/>{x_mark}</g>')


def stamp(x, y, s=1.0):
    """손에 드는 도장 (손잡이 + 도장면)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-8" y="-40" width="16" height="26" rx="4" fill="#5A3B22"/>'
            f'<rect x="-18" y="-14" width="36" height="10" rx="2" fill="#5A3B22"/><rect x="-16" y="-4" width="32" height="6" rx="1" fill="{ROYAL}"/></g>')


def idcard(x, y, name, until, s=1.0, kind="king", rot=0):
    """신분증. kind = king(왕의 도장) / self(직접 그린 도장) / none."""
    st = {"king": seal(122, 58, 0.9), "self": '<circle cx="122" cy="58" r="16" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/>' + label(122, 63, "⟦나|me⟧", 11, "var(--bad)"), "none": ""}[kind]
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="150" height="90" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect width="150" height="20" rx="6" fill="#C9A86A"/>{label(75, 14, "⟦신분증|ID CARD⟧", 10, "#142033", cls="d")}'
            f'<circle cx="28" cy="50" r="14" fill="{SKIN}"/><path d="M14 46 Q28 30 42 46 Z" fill="var(--accent)"/>'
            f'{label(50, 46, name, 11, "#142033", "start", cls="d")}{label(50, 66, until, 9, "#142033", "start")}{st}</g>')


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def letter(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M0 4 L70 46 L140 4" stroke="#C9A86A" stroke-width="3" fill="none"/>{seal(70, 46, 0.7)}</g>')


# 1. 낯선 상인: "나 왕의 친구예요" — 도둑도 똑같이 말해요
P1 = svg(300, sky(300) + gate(300, 60) + person(270, 150, s=0.8, face=EYES, **GUARD)
         + bubble(180, 20, 150, 34, "⟦…정말요?|…really?⟧", 13, "var(--panel)", "var(--good)", "bottom")
         + person(100, 140, s=0.85, face=SMILE, **MERCHANT)
         + bubble(20, 60, 190, 40, "⟦나 왕의 친구예요!|I am the king\'s friend!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 130, s=0.85, face=MASK, extra=BAG)
         + bubble(500, 50, 220, 40, "⟦나도 왕의 친구예요!|me too, the king\'s friend!⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(590, 255, "⟦둘 다 그렇게 말해요|both say the same thing⟧", 11, "var(--muted)")
         + label(380, 285, "⟦말만으론 누가 진짜인지 몰라요|words alone can\'t tell who is real⟧", 12, "var(--ink)"))

# 2. 왕에게 매번 물어볼 순 없고, 직접 그린 신분증은 소용없어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + label(240, 60, "⟦매번 왕에게 물어볼 순 없어요|you can\'t ask the king every time⟧", 13, "var(--ink)", cls="d")
         + label(240, 82, "⟦왕은 하루 종일 줄만 봐요|the king would see nothing but the line⟧", 11, "var(--muted)")
         + person(90, 120, s=0.9, face=FROWN + SWEAT, **KING)
         + "".join(person(x, 160, s=0.55, face=EYES, hat=h, shirt="#4A5A72") for x, h in ((200, "var(--accent)"), (260, None), (320, "var(--good)"), (380, "#5B8DEF")))
         + label(300, 250, "⟦줄, 줄, 줄…|a line, all day⟧", 11, "var(--muted)")
         + label(650, 60, "⟦직접 그린 신분증|a card he drew himself⟧", 13, "var(--ink)", cls="d")
         + label(650, 82, "⟦도장도 자기가 찍었어요|and stamped it himself⟧", 11, "var(--bad)")
         + person(560, 110, s=0.85, face=MASK) + idcard(630, 120, "⟦왕의 친구|king\'s friend⟧", "⟦유효: 영원히|valid: forever⟧", 0.8, kind="self", rot=6)
         + label(380, 300, "⟦신분증도 아무나 만들면 소용없어요 — 누가 도장을 찍었는지가 중요해요|a card anyone can make proves nothing — who stamped it is what matters⟧", 11, "var(--muted)"))

# 3. 왕의 도장이 찍힌 신분증 (hero)
P3 = svg(360, sky(360)
         + person(90, 90, s=1.0, face=SMILE, **KING) + stamp(180, 150, 1.0)
         + idcard(230, 110, "⟦상인 토마|Merchant Toma⟧", "⟦유효: 올해 12월까지|valid: until December⟧", 1.3, kind="king")
         + label(150, 240, "⟦왕이 직접 찍어요|the king stamps it himself⟧", 11, "var(--muted)")
         + label(330, 262, "⟦신분증 = 이름 + 기한 + 왕의 도장|card = name + date + the king\'s seal⟧", 11, "var(--ink)")
         + person(520, 130, s=0.85, face=SMILE, **GUARD) + seal(640, 170, 1.2)
         + label(640, 118, "⟦왕의 도장 견본|the king\'s seal sample⟧", 11, "var(--ink)")
         + label(640, 218, "⟦똑같네! 통과|a match — go on through⟧", 11, "var(--good)")
         + label(380, 310, "⟦누구나 신분증을 만들 순 있어요 — 왕의 도장은 왕만 찍어요|anyone can make a card — only the king can stamp it⟧", 13, "var(--ink)", cls="d")
         + label(380, 344, "⟦문지기는 왕을 안 불러도 도장만 보면 알아요|the gatekeeper never calls the king — the seal is enough⟧", 12, "var(--muted)"))

# 4. 찍는 도장 하나, 확인 견본은 많이
P4 = svg(320, sky(320)
         + label(130, 50, "⟦찍는 도장|the stamping seal⟧", 13, "var(--ink)", cls="d")
         + '<rect x="70" y="70" width="120" height="110" rx="8" fill="var(--night)"/><rect x="82" y="82" width="96" height="86" rx="4" fill="#0A1120"/>' + stamp(130, 150, 1.1)
         + '<rect x="118" y="164" width="24" height="18" rx="3" fill="#E9B44C"/><path d="M123 164 v-6 a7 7 0 0 1 14 0 v6" stroke="#E9B44C" stroke-width="3" fill="none"/>'
         + label(130, 215, "⟦왕만 가져요 — 절대 안 빌려줘요|only the king has it — never lent⟧", 11, "var(--muted)")
         + label(380, 50, "⟦확인용 견본|the checking sample⟧", 13, "var(--ink)", cls="d")
         + person(340, 90, s=0.8, face=SMILE, **GUARD) + seal(430, 130, 1.0) + '<path d="M414 160 l10 10 l20 -22" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>'
         + label(380, 215, "⟦누구나 가져도 돼요|anyone may have one⟧", 11, "var(--muted)") + label(380, 236, "⟦견본으론 못 찍어요|you can\'t stamp with a sample⟧", 11, "var(--muted)")
         + label(630, 50, "⟦베껴 찍은 도장|a copied stamp⟧", 13, "var(--ink)", cls="d")
         + person(590, 90, s=0.8, face=MASK) + seal(680, 130, 1.0, broken=True)
         + label(630, 215, "⟦모양이 안 맞아요|the shape doesn\'t match⟧", 11, "var(--bad)")
         + label(380, 300, "⟦찍는 도장은 하나, 확인 견본은 많이 — 그래서 위조가 안 돼요|one seal to stamp, many samples to check — that\'s why it can\'t be forged⟧", 11, "var(--ink)"))

# 5. 기한이 지나거나 명부에 오르면 돌려보내요 — 통과하면 봉인 약속
P5 = svg(320, sky(320)
         + idcard(40, 60, "⟦상인 벤|Merchant Ben⟧", "⟦유효: 작년 3월까지|valid: until last March⟧", 0.9) + '<path d="M60 70 l100 60 M160 70 l-100 60" stroke="var(--bad)" stroke-width="4" stroke-linecap="round" opacity="0.7"/>'
         + label(108, 170, "⟦기한 지남|expired⟧", 12, "var(--bad)", cls="d")
         + idcard(200, 60, "⟦상인 토마|Merchant Toma⟧", "⟦유효: 올해 12월까지|valid: until December⟧", 0.9)
         + label(268, 170, "⟦취소 명부에 있음|on the revoked list⟧", 12, "var(--bad)", cls="d")
         + paper(160, 200, 200, 80, "⟦취소 명부|REVOKED LIST⟧", ("⟦상인 토마 — 잃어버림|Toma — card was lost⟧",))
         + idcard(360, 60, "⟦상인 애나|Merchant Anna⟧", "⟦유효: 내년 5월까지|valid: until next May⟧", 0.9)
         + label(428, 170, "⟦통과|valid⟧", 12, "var(--good)", cls="d")
         + '<path d="M500 100 h50" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M542 92 l10 8 l-10 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + letter(570, 60, 1.0) + label(640, 170, "⟦이제 봉인 약속을 시작해요|now the sealing promise begins⟧", 11, "var(--good)")
         + label(380, 305, "⟦기한이 지나거나 명부에 오르면 문지기가 돌려보내요|expired or on the list, the gatekeeper turns it away⟧", 12, "var(--ink)"))

KING_I = icon(f'<rect x="26" y="8" width="12" height="18" rx="3" fill="#5A3B22"/><rect x="18" y="26" width="28" height="8" rx="2" fill="#5A3B22"/><circle cx="32" cy="48" r="10" fill="{ROYAL}"/><path d="M27 51 l-1 -6 l3 2 l3 -4 l3 4 l3 -2 l-1 6z" fill="#E9B44C"/>')
NOCOPY_I = icon(f'<circle cx="24" cy="32" r="14" fill="{ROYAL}"/><circle cx="24" cy="32" r="10" fill="none" stroke="#FFF8E7" stroke-width="2"/><rect x="42" y="28" width="14" height="12" rx="2" fill="var(--night)"/><path d="M45 28 v-4 a4 4 0 0 1 8 0 v4" stroke="var(--night)" stroke-width="3" fill="none"/>')
DATE_I = icon('<rect x="12" y="14" width="40" height="38" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="14" width="40" height="10" rx="4" fill="var(--accent)"/><path d="M22 10 v8 M42 10 v8" stroke="#5A3B22" stroke-width="3"/><path d="M22 38 l6 6 l12 -12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 32 h20 M22 42 h20" stroke="#C9A86A" stroke-width="2"/><path d="M40 16 l8 8 M48 16 l-8 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "pki", "order": 62,
    "title": ("왕의 도장이 찍힌 신분증", "The ID Card with the King\'s Seal"),
    "h1": ("<em>PKI</em>가 뭐예요?", "What is <em>PKI</em>?"),
    "sub": ("PKI(공개 키 기반 구조)와 인증서를 왕의 도장이 찍힌 신분증 이야기로 풀어봤어요.",
            "PKI and certificates, told as a story about an ID card stamped with the king\'s seal."),
    "panels": [
        {"svg": P1, "alt": ("성문 앞에서 낯선 상인이 '나 왕의 친구예요!' 하고, 문지기는 '…정말요?' 함. 옆의 도둑도 '나도 왕의 친구예요!' 함", "At the gate a stranger says I am the king\'s friend; the gatekeeper says really? A thief beside him says me too, the king\'s friend"),
         "caption": ("낯선 상인이 왕의 친구라고 해요. 믿어도 될까요?", "A stranger says he is the king\'s friend. Should we believe him?"),
         "small": ("도둑도 똑같이 말할 수 있어요. 말만으로는 누가 진짜인지 몰라요.", "A thief can say exactly the same thing. Words alone can\'t tell who is real.")},
        {"svg": P2, "alt": ("왼쪽: 땀 흘리는 왕 앞에 긴 줄. 오른쪽: 도둑이 직접 그린 신분증에 '나' 라고 쓴 점선 도장을 찍어 들고 있음", "Left: a sweating king with a long line of people. Right: a thief holds a card he drew himself, stamped with a dotted seal that just says me"),
         "caption": ("매번 왕에게 물어볼 순 없어요. 직접 그린 신분증은 소용없고요.", "We can\'t ask the king every time. And a card you draw yourself proves nothing."),
         "small": ("왕은 하루 종일 줄만 보게 돼요. 신분증은 누구나 그릴 수 있으니, 누가 도장을 찍었는지가 중요해요.", "The king would see nothing but the line. Anyone can draw a card — what matters is who stamped it.")},
        {"svg": P3, "hero": True, "alt": ("왕이 도장을 들고 상인 토마의 신분증에 보라색 도장을 찍음. 신분증엔 이름과 '올해 12월까지'. 문지기는 왕의 도장 견본을 들고 비교하며 '똑같네! 통과'", "The king stamps a purple seal onto Merchant Toma\'s card, which shows a name and valid until December. The gatekeeper holds a sample of the seal, compares, and says a match — go on through"),
         "caption": ("PKI는 왕이 도장 찍어준 신분증으로 서로를 믿는 약속이에요.", "PKI is the promise that we trust each other by cards the king has stamped."),
         "small": ("신분증엔 이름, 기한, 왕의 도장이 있어요. 문지기는 도장 견본만 있으면 왕을 부르지 않고도 알아봐요.", "A card carries a name, a date, and the king\'s seal. With a sample of the seal, the gatekeeper knows without calling the king."),
         "tricks": (4, [
             (KING_I, ("왕이 찍어요", "The king stamps it"), ("모두가 믿는 한 사람", "one person everyone trusts"), "calm"),
             (NOCOPY_I, ("도장은 못 베껴요", "The seal can\'t be copied"), ("찍는 도장은 금고 속에", "the stamping seal stays in the vault"), "warm"),
             (DATE_I, ("기한이 있어요", "It has a date"), ("지나면 다시 받아요", "expired? get a new one")),
             (LIST_I, ("잃어버리면 명부에", "Lost? onto the list"), ("문지기가 명부를 봐요", "the gatekeeper checks the list")),
         ])},
        {"svg": P4, "alt": ("셋: 금고 속 찍는 도장(왕만 가짐), 문지기의 확인용 견본(누구나 가져도 되지만 찍지는 못함), 도둑이 베껴 찍은 도장에 빨간 X(모양이 안 맞음)", "Three: the stamping seal locked in the vault (only the king has it), the gatekeeper\'s checking sample (anyone may have one, but it can\'t stamp), and a thief\'s copied stamp marked with a red X — the shape doesn\'t match"),
         "caption": ("찍는 도장은 하나, 확인 견본은 많이. 그래서 위조가 안 돼요.", "One seal that stamps, many samples that check. That is why it can\'t be forged."),
         "small": ("찍는 도장은 왕만 갖고 절대 안 빌려줘요. 견본은 누구나 가져도 되지만 견본으로는 찍을 수 없어요. 도둑이 베껴 찍으면 모양이 안 맞아요.", "Only the king holds the stamping seal, and never lends it. Anyone may hold a sample, but a sample can\'t stamp. A thief\'s copy never matches.")},
        {"svg": P5, "alt": ("신분증 셋: 작년에 기한이 지난 것(X), 잃어버려 취소 명부에 오른 것, 아직 유효한 것(통과). 통과한 신분증에서 화살표가 봉인 편지로 이어짐", "Three cards: one expired last year (X), one on the revoked list because it was lost, one still valid (through). From the valid card an arrow leads to a sealed letter"),
         "caption": ("기한이 지나거나 명부에 오르면 돌려보내요. 통과하면 봉인 약속을 시작해요.", "Expired or on the list, it\'s turned away. Once through, the sealing promise begins."),
         "small": ('신분증을 잃어버리면 왕이 취소 명부에 이름을 올려요. 신분증이 통과되면 그때부터 <a href="tls-ko.html">봉인 편지</a>를 주고받을 수 있어요.',
                   'Lose your card and the king writes your name on the revoked list. Once a card passes, the two of you can start exchanging <a href="tls-en.html">sealed letters</a>.')},
    ],
    "summary": (("<b>PKI</b> = 모두가 믿는 <b>왕</b>이 <b>도장 찍어준 신분증</b>으로 서로를 믿는 약속. 찍는 도장은 <b>왕만</b>, 확인 견본은 <b>누구나</b>. 신분증엔 <b>기한</b>이 있고, 잃어버리면 <b>취소 명부</b>에 올라요.",
                 "<b>PKI</b> = trusting each other by <b>ID cards stamped by a king</b> everyone trusts. <b>Only the king</b> can stamp; <b>anyone</b> can check. Every card <b>expires</b>, and a lost one goes on the <b>revoked list</b>."),
                ("PKI, Public Key Infrastructure. 인증기관(CA)이 개인키로 서명한 인증서를 발급하고, 누구나 CA 의 공개키로 그 서명을 검증해요. 인증서엔 유효기간이 있고, 폐기된 인증서는 CRL 이나 OCSP 로 확인해요. TLS/HTTPS 가 이 위에서 돌아가요.",
                 "A Certificate Authority (CA) signs certificates with its private key; anyone verifies the signature with the CA\'s public key. Certificates expire, and revoked ones are checked via CRL or OCSP. TLS/HTTPS runs on top of this.")),
    "glossary": [
        ("인증서", "Certificate", ("왕의 도장이 찍힌 신분증.", "The card with the king\'s seal."), ("이름, 기한, 도장. 상점(서버)이 '나 진짜예요' 하고 보여주는 종이예요.", "A name, a date, a seal. The paper a shop (server) shows to say I am real.")),
        ("인증기관 CA", "Certificate Authority (CA)", ("도장을 찍어주는 왕.", "The king who stamps."), ("모두가 믿기로 한 한 사람. 신분증을 발급하고, 잃어버린 건 명부에 올려요.", "The one everyone agreed to trust. Issues the cards, and lists the lost ones.")),
        ("공개키 / 개인키", "Public / private key", ("확인 견본 / 찍는 도장.", "The checking sample / the stamping seal."), ('견본으론 찍을 수 없고, 도장으로 찍은 건 견본으로 확인돼요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'A sample can\'t stamp; what the seal stamped, the sample confirms. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("유효기간 · 만료", "Validity · expiry", ("신분증의 기한.", "The date on the card."), ("지나면 아무리 진짜여도 돌려보내요. 요즘 상점 신분증은 1년 안쪽이에요.", "Past the date, even a real card is turned away. Shop cards today last under a year.")),
        ("폐기 목록 CRL", "Revocation list (CRL / OCSP)", ("취소 명부.", "The revoked list."), ("잃어버렸거나 도둑맞은 신분증 이름표. 문지기가 통과시키기 전에 명부를 봐요.", "Names of lost or stolen cards. The gatekeeper checks it before letting anyone through.")),
        ("루트 인증서", "Root certificate", ("문지기가 가진 왕의 도장 견본.", "The seal sample the gatekeeper keeps."), ("컴퓨터와 브라우저에 미리 들어 있어요. 이게 없으면 어떤 신분증도 확인 못 해요.", "Shipped inside your computer and browser. Without it, no card can be checked.")),
        ("자체 서명", "Self-signed", ("직접 그린 신분증.", "A card you drew yourself."), ("도장도 자기가 찍은 것. 성 안에서 연습할 땐 쓰지만, 마을 사람은 안 믿어요.", "Stamped by its own maker. Fine for practice inside the castle; the village won\'t trust it.")),
        ("TLS", "TLS", ("신분증 다음의 봉인 약속.", "The sealing promise after the card."), ('신분증이 통과되면 그제서야 봉인 편지를 시작해요. → <a href="tls-ko.html">상점과 주고받는 봉인 약속</a>', 'Only once the card passes do the sealed letters begin. → <a href="tls-en.html">the sealing promise with the shop</a>')),
    ],
}
