from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
KEEPER = dict(hat="var(--accent)", shirt="#4A5A72")
ROYAL = "#7B3FA0"
EYE = '<path d="M-14 0 Q0 -10 14 0 Q0 10 -14 0 Z" fill="#FFF" stroke="var(--night)" stroke-width="2"/><circle r="4" fill="var(--night)"/>'


def shop(x, y, s=1.0, fake=False):
    """마을 상점. 몸통 x-70..x+70, y..y+110, 지붕은 y-40 부터."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="0" width="140" height="110" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>'
            f'<path d="M-80 0 L0 -40 L80 0 Z" fill="{"var(--bad)" if fake else "var(--accent)"}"/>'
            f'<rect x="-50" y="12" width="100" height="24" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{label(0, 29, "⟦빵집|BAKERY⟧", 13, "#142033", cls="d")}'
            f'<rect x="-20" y="60" width="40" height="50" fill="var(--night)"/><rect x="-58" y="48" width="28" height="22" fill="var(--sky)"/><rect x="30" y="48" width="28" height="22" fill="var(--sky)"/></g>')


def seal(x, y, s=1.0, color=ROYAL, sparkle=False):
    sp = '<path d="M26 -26 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3z" fill="var(--accent)"/>' if sparkle else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="{color}"/><circle r="15" fill="none" stroke="#FFF8E7" stroke-width="2"/>'
            f'<path d="M-9 5 l-2 -11 l6 4 l5 -8 l5 8 l6 -4 l-2 11z" fill="#E9B44C"/>{sp}</g>')


def letter(x, y, s=1.0, text=None, sealed=False, seal_color="var(--good)", open_=False):
    """편지 봉투. sealed 면 봉인 도장, open_ 이면 뜯긴 뚜껑."""
    flap = ('<path d="M0 4 L70 -30 L140 4" stroke="#C9A86A" stroke-width="3" fill="#FFF8E7"/>' if open_
            else '<path d="M0 4 L70 46 L140 4" stroke="#C9A86A" stroke-width="3" fill="none"/>')
    st = f'<circle cx="70" cy="46" r="12" fill="{seal_color}"/>' if sealed else ""
    tx = label(70, 62, text, 11, "#142033") if text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'{flap}{st}{tx}</g>')


def idcard(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="150" height="90" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect width="150" height="20" rx="6" fill="#C9A86A"/>{label(75, 14, "⟦신분증|ID CARD⟧", 10, "#142033", cls="d")}'
            f'<circle cx="28" cy="50" r="14" fill="{SKIN}"/><path d="M14 46 Q28 30 42 46 Z" fill="var(--accent)"/>'
            f'{label(50, 48, "⟦빵집|Bakery⟧", 12, "#142033", "start", cls="d")}{label(50, 66, "⟦유효: 내년까지|valid: next year⟧", 9, "#142033", "start")}{seal(122, 58, 0.9)}</g>')


def padlock(x, y, s=1.0, color="var(--good)", open_=False):
    sh = '<path d="M-8 -8 V-16 a8 8 0 0 1 16 0" stroke="{c}" stroke-width="4" fill="none"/>' if open_ else '<path d="M-8 -8 V-14 a8 8 0 0 1 16 0 V-8" stroke="{c}" stroke-width="4" fill="none"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-13" y="-8" width="26" height="20" rx="4" fill="{color}"/>{sh.replace("{c}", color)}</g>'


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


# 1. 마을 상점에 편지를 보내요 — 배달부가 뜯어 봐요
P1 = svg(300, sky(300) + small_castle(30, 80, 0.6) + person(130, 140, s=0.8, **ME)
         + letter(200, 110, 0.7, "⟦빵 열 개 주세요|ten loaves please⟧")
         + '<path d="M310 150 L540 150" stroke="var(--stone-dark)" stroke-width="8" fill="none" stroke-linecap="round"/>'
         + person(400, 40, s=0.8, face=MASK) + letter(360, 130, 0.6, open_=True) + f'<g transform="translate(402,138)">{EYE}</g>'
         + label(420, 225, "⟦배달부가 뜯어 봐요|the courier opens it⟧", 12, "var(--bad)")
         + shop(640, 90, 1.0) + label(640, 225, "⟦마을 빵집|the village bakery⟧", 12, "var(--muted)")
         + label(380, 285, "⟦길에서는 누가 읽는지 몰라요|on the road, anyone might read it⟧", 12, "var(--ink)"))

# 2. 봉인 도장을 나눠 가질 수도, 진짜 상점을 고를 수도 없어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(70, 110, s=0.85, face=FROWN + SWEAT, hat=None, shirt="#4A5A72")
         + bubble(30, 30, 230, 40, "⟦봉인 도장을 어떻게 나눠 갖죠?|how do we share a seal?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + letter(150, 120, 0.8, open_=True) + key(220, 175, 0.8)
         + person(330, 110, s=0.8, face=MASK) + key(400, 175, 0.8) + label(420, 150, "⟦베꼈다!|copied!⟧", 12, "var(--bad)", cls="d")
         + label(240, 240, "⟦도장을 편지로 보내면 배달부가 베껴요|send the seal by letter and the courier copies it⟧", 11, "var(--bad)")
         + shop(560, 100, 0.7) + shop(680, 100, 0.7, fake=True)
         + label(560, 225, "⟦진짜 빵집|real bakery⟧", 11, "var(--ink)") + label(680, 225, "⟦가짜 빵집|fake bakery⟧", 11, "var(--bad)")
         + label(620, 60, "⟦어느 게 진짜죠?|which one is real?⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦둘만 아는 도장도 없고, 상대가 진짜인지도 몰라요|no seal only we two know, and no way to tell who is real⟧", 11, "var(--muted)"))

# 3. TLS = 상점과 주고받는 봉인 약속 (hero)
P3 = svg(360, sky(360)
         + '<circle cx="240" cy="40" r="11" fill="var(--accent)"/>' + label(240, 44, "1", 12, "#FFF8E7", cls="d")
         + idcard(258, 30, 0.7) + label(310, 112, "⟦신분증부터 확인|check the card first⟧", 11, "var(--ink)")
         + '<circle cx="410" cy="40" r="11" fill="var(--accent)"/>' + label(410, 44, "2", 12, "#FFF8E7", cls="d")
         + seal(470, 62, 1.1, sparkle=True) + label(470, 112, "⟦새 도장은 그 자리에서|a fresh seal, made on the spot⟧", 11, "var(--ink)")
         + person(80, 130, s=0.9, **ME) + person(350, 150, s=0.7, face=MASK) + label(375, 140, "⟦???|???⟧", 18, "var(--bad)", cls="d")
         + shop(660, 40, 0.5) + person(600, 130, s=0.9, face=SMILE, **KEEPER)
         + '<path d="M150 190 L340 190 M420 190 L590 190" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 5"/>'
         + letter(160, 242, 0.5, sealed=True) + letter(260, 242, 0.5, sealed=True) + letter(460, 242, 0.5, sealed=True) + letter(560, 242, 0.5, sealed=True)
         + label(380, 306, "⟦③ 이제부터 편지는 다 봉인|③ every letter sealed from now on⟧", 11, "var(--ink)")
         + label(380, 344, "⟦신분증 확인, 새 도장, 그리고 봉인 — 배달부는 이제 못 읽어요|check the card, make a seal, then seal everything — the courier can\'t read a thing⟧", 12, "var(--ink)", cls="d"))

# 4. 약속 순서 (핸드셰이크)
STEPS = (("var(--accent)", "⟦나 → 빵집: 안녕! 신분증 보여줘요|me → bakery: hello! show me your card⟧"),
         ("var(--accent)", "⟦빵집 → 나: 여기요 (왕의 도장 찍힌 신분증)|bakery → me: here (stamped by the king)⟧"),
         ("var(--good)", "⟦둘이: 도장 재료를 반씩 섞어요 — 배달부는 반쪽만 봐요|both: mix seal ingredients, half each — the courier sees only halves⟧"),
         ("var(--good)", "⟦둘이: 새 도장으로 봉인! 오늘 편지는 다 이걸로|both: seal with the new stamp — every letter today⟧"))
P4 = svg(360, sky(360)
         + '<rect x="60" y="30" width="640" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="60" y="30" width="640" height="30" rx="8" fill="#C9A86A"/>'
         + label(380, 50, "⟦봉인 약속 순서|THE SEALING PROMISE, STEP BY STEP⟧", 13, "#142033", cls="d")
         + "".join(f'<circle cx="88" cy="{92 + i * 44}" r="11" fill="{c}"/>' + label(88, 96 + i * 44, str(i + 1), 12, "#FFF8E7", cls="d") + label(110, 97 + i * 44, t, 12, "#142033", "start") for i, (c, t) in enumerate(STEPS))
         + label(110, 202, "⟦반쪽만 봐서는 도장을 못 만들어요|half is never enough to build the seal⟧", 10, "#7B3FA0", "start")
         + letter(200, 272, 0.45, sealed=True) + letter(380, 272, 0.45, sealed=True) + letter(560, 272, 0.45, sealed=True)
         + label(380, 344, "⟦한 번 약속하면 오늘 편지는 전부 봉인이에요|one promise, and every letter today travels sealed⟧", 12, "var(--ink)", cls="d"))

# 5. 자물쇠 표시 — 그리고 자물쇠가 말해주지 않는 것
P5 = svg(320, '<rect width="253" height="320" fill="var(--good-soft)"/><rect x="253" width="254" height="320" fill="var(--bad-soft)"/><rect x="507" width="253" height="320" fill="var(--accent-soft)"/>'
         + letter(30, 60, 1.3, sealed=True) + padlock(130, 160, 1.4)
         + label(126, 215, "⟦자물쇠 = 봉인됐고|padlock = sealed,⟧", 11, "var(--ink)") + label(126, 234, "⟦신분증도 봤어요|and the card was checked⟧", 11, "var(--ink)")
         + letter(290, 60, 1.3, sealed=True, seal_color="var(--bad)") + padlock(390, 160, 1.4, "var(--bad)", open_=True)
         + label(380, 215, "⟦기한 지난 신분증|an expired card⟧", 11, "var(--bad)") + label(380, 234, "⟦빨간 자물쇠는 돌아서요|red lock: turn back⟧", 11, "var(--bad)")
         + shop(634, 70, 0.6, fake=True) + padlock(634, 165, 1.2)
         + label(634, 215, "⟦가짜 빵집도|even a fake bakery⟧", 11, "var(--bad)") + label(634, 234, "⟦자물쇠는 있을 수 있어요|can have the lock⟧", 11, "var(--bad)")
         + label(380, 300, "⟦자물쇠는 편지를 지켜요 — 상점이 착한지는 이름을 봐야 해요|the lock protects the letter — whether the shop is honest, read the name⟧", 11, "var(--ink)", cls="d"))

CARD_I = icon(f'<rect x="8" y="16" width="48" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="20" cy="32" r="6" fill="{SKIN}"/><circle cx="46" cy="32" r="7" fill="{ROYAL}"/><path d="M30 28 h8 M30 36 h8" stroke="#C9A86A" stroke-width="2"/>')
FRESH_I = icon(f'<circle cx="28" cy="36" r="16" fill="{ROYAL}"/><circle cx="28" cy="36" r="11" fill="none" stroke="#FFF8E7" stroke-width="2"/><path d="M48 10 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3z" fill="var(--accent)"/>')
SEAL_I = icon('<rect x="8" y="18" width="48" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M8 20 L32 36 L56 20" stroke="#C9A86A" stroke-width="3" fill="none"/><circle cx="32" cy="36" r="7" fill="var(--good)"/>')
LOCK_I = icon('<rect x="18" y="28" width="28" height="24" rx="5" fill="var(--good)"/><path d="M24 28 v-8 a8 8 0 0 1 16 0 v8" stroke="var(--good)" stroke-width="5" fill="none"/>')

PAGE = {
    "slug": "tls", "order": 63,
    "title": ("상점과 주고받는 봉인 약속", "The Sealing Promise with the Shop"),
    "h1": ("<em>TLS</em>가 뭐예요?", "What is <em>TLS</em>?"),
    "sub": ("TLS 와 HTTPS 를 마을 상점과 봉인 편지를 주고받기로 약속하는 이야기로 풀어봤어요.",
            "TLS and HTTPS, told as a story about promising to exchange sealed letters with a shop in the village."),
    "panels": [
        {"svg": P1, "alt": ("성에서 내가 '빵 열 개 주세요' 편지를 마을 빵집으로 보내는데, 길 위의 배달부가 편지를 뜯어 눈으로 읽음", "From the castle I send a letter — ten loaves please — to the village bakery, but the courier on the road opens it and reads it"),
         "caption": ("마을 빵집에 편지를 보내요. 그런데 배달부가 뜯어 봐요.", "I send a letter to the village bakery. But the courier opens it on the way."),
         "small": ('길에서는 누가 읽는지 몰라요. 그래서 <a href="encryption-ko.html">봉인 편지</a>를 쓰고 싶은데, 빵집과 나는 만난 적이 없어요.',
                   'On the road, anyone might read it. I want to send <a href="encryption-en.html">sealed letters</a> — but the bakery and I have never met.')},
        {"svg": P2, "alt": ("왼쪽: 내가 봉인 도장을 편지에 넣어 보내자 배달부가 도장을 베낌. 오른쪽: 빵집이 둘 — 진짜 빵집과 빨간 지붕 가짜 빵집", "Left: I send the seal inside a letter and the courier copies it. Right: two bakeries — the real one and a fake one with a red roof"),
         "caption": ("도장을 편지로 보내면 배달부가 베껴요. 게다가 어느 빵집이 진짜인지도 몰라요.", "Send the seal by letter and the courier copies it. And which bakery is the real one?"),
         "small": ("둘만 아는 도장이 필요한데, 도장을 보내는 길이 바로 그 위험한 길이에요. 가짜 빵집에 봉인 편지를 보내면 더 나빠요.", "We need a seal only we two know — but the road to share it is the very road we don\'t trust. Sealing a letter to a fake bakery is even worse.")},
        {"svg": P3, "hero": True, "alt": ("① 빵집의 신분증 확인, ② 반짝이는 새 도장을 그 자리에서 만들기, 그리고 ③ 나와 빵집 주인 사이 편지가 전부 봉인됨. 가운데 배달부는 '???'", "① check the bakery\'s ID card, ② make a fresh sparkling seal on the spot, and ③ every letter between me and the shopkeeper is sealed. The courier in the middle: ???"),
         "caption": ("TLS는 상점과 주고받는 봉인 약속이에요.", "TLS is the sealing promise between me and the shop."),
         "small": ("먼저 빵집의 신분증을 확인하고, 둘만 아는 새 도장을 그 자리에서 만들어요. 그다음부터 편지는 다 봉인이에요.", "First I check the bakery\'s card, then we make a fresh seal only the two of us know, right there. From then on, every letter is sealed."),
         "tricks": (4, [
             (CARD_I, ("신분증 먼저", "The card first"), ("왕의 도장이 찍힌 것만", "only one stamped by the king"), "calm"),
             (FRESH_I, ("새 도장은 그 자리에서", "A fresh seal, on the spot"), ("길로 보내지 않아요", "never sent down the road"), "warm"),
             (SEAL_I, ("편지마다 봉인", "Every letter sealed"), ("배달부는 못 읽어요", "the courier can\'t read it")),
             (LOCK_I, ("자물쇠 표시", "The padlock sign"), ("약속이 됐다는 표시", "the promise is in place")),
         ])},
        {"svg": P4, "alt": ("봉인 약속 순서 네 줄: 안녕, 신분증 보여줘 → 여기요 (왕의 도장) → 도장 재료를 반씩 섞기 (배달부는 반쪽만 봄) → 새 도장으로 봉인. 아래엔 봉인된 편지 셋", "Four steps of the sealing promise: hello, show me your card → here, stamped by the king → mix seal ingredients half each (the courier sees only halves) → seal with the new stamp. Three sealed letters below"),
         "caption": ("약속은 네 마디면 끝나요. 도장은 길로 보내지 않고, 재료를 반씩 섞어 각자 만들어요.", "The promise takes four lines. The seal never travels — each side mixes half the ingredients and builds it."),
         "small": ("배달부가 오가는 말을 다 엿봐도 반쪽으론 도장을 못 만들어요. 그리고 이 도장은 오늘만 써요 — 내일은 새로 만들어요.", "The courier may overhear every word, but half is never enough to build the seal. And this seal is for today only — tomorrow we make a new one.")},
        {"svg": P5, "alt": ("셋: 초록 자물쇠가 달린 봉인 편지(봉인됐고 신분증도 봤음), 빨간 열린 자물쇠(기한 지난 신분증 — 돌아서요), 그리고 초록 자물쇠가 달린 가짜 빵집", "Three: a sealed letter with a green padlock (sealed, card checked), a red open padlock (expired card — turn back), and a fake bakery that also has a green padlock"),
         "caption": ("자물쇠는 편지를 지켜요. 하지만 가짜 빵집도 자물쇠를 달 수 있어요.", "The padlock protects the letter. But a fake bakery can hang a padlock too."),
         "small": ('자물쇠는 "봉인됐고 신분증을 봤다"는 뜻이지 "착한 상점"이라는 뜻이 아니에요. <a href="phishing-ko.html">가짜 편지</a>가 이끄는 가짜 빵집도 자기 이름으로 신분증을 받을 수 있어요 — 이름을 꼭 봐요.',
                   'The padlock means "sealed, and the card was checked" — not "honest shop". A fake bakery that a <a href="phishing-en.html">fake letter</a> leads you to can get a card in its own name — so read the name.')},
    ],
    "summary": (("<b>TLS</b> = 상점의 <b>신분증을 먼저 확인</b>하고, 둘만 아는 <b>새 도장을 그 자리에서</b> 만들어, 그다음 편지를 <b>전부 봉인</b>하는 약속. <b>자물쇠</b>는 그 약속이 됐다는 표시예요.",
                 "<b>TLS</b> = <b>check the shop\'s card</b>, make a <b>fresh seal on the spot</b> that only the two of you know, then <b>seal every letter</b>. The <b>padlock</b> says the promise is in place."),
                ("TLS, Transport Layer Security. HTTPS 의 S 가 이거예요. 핸드셰이크에서 서버 인증서를 검증하고 키 교환으로 세션 키를 만든 뒤, 이후 통신을 모두 암호화해요. 중간자 공격을 막지만, 상대가 '착한' 사이트인지는 보장하지 않아요.",
                 "The S in HTTPS. The handshake verifies the server certificate and derives a session key through key exchange; everything after is encrypted. It stops man-in-the-middle attacks, but says nothing about whether the site is honest.")),
    "glossary": [
        ("HTTPS", "HTTPS", ("봉인 약속을 한 상점 주소.", "A shop address with the sealing promise."), ("주소 앞에 https 가 붙고 자물쇠가 보이면, 그 상점과는 봉인 편지로만 주고받아요.", "When the address starts with https and shows a padlock, every letter with that shop travels sealed.")),
        ("핸드셰이크", "Handshake", ("약속을 맺는 네 마디.", "The four lines that make the promise."), ("안녕 → 신분증 → 재료 반씩 → 봉인 시작. 편지를 보내기 전에 딱 한 번 해요.", "Hello → card → half the ingredients each → start sealing. Done once, before the first letter.")),
        ("세션 키", "Session key", ("오늘만 쓰는 새 도장.", "Today\'s fresh seal."), ("그 자리에서 만들고, 길로 보내지 않고, 끝나면 버려요. 내일은 새로 만들어요.", "Made on the spot, never sent down the road, thrown away when done. Tomorrow gets a new one.")),
        ("인증서", "Certificate", ("빵집의 신분증.", "The bakery\'s ID card."), ('왕의 도장이 찍혀 있어야 믿어요. → <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>', 'Trusted only with the king\'s seal on it. → <a href="pki-en.html">the ID card with the king\'s seal</a>')),
        ("자물쇠 아이콘", "Padlock icon", ("약속이 됐다는 표시.", "The sign that the promise is in place."), ("봉인됐고 신분증을 봤다는 뜻. '착한 상점'이라는 뜻은 아니에요.", "Sealed, and the card was checked. It does not mean the shop is honest.")),
        ("중간자 공격", "Man-in-the-middle", ("편지를 뜯어 보는 배달부.", "The courier who opens the letters."), ('신분증 확인과 봉인이 막아요. 가짜 신분증을 들이밀면 빨간 자물쇠가 떠요. → <a href="mitm-ko.html">편지를 중간에서 뜯어보는 배달부</a>', 'Blocked by the card check and the seal. A fake card gets a red padlock. → <a href="mitm-en.html">the postman who opens your letters</a>')),
        ("암호화", "Encryption", ("봉인 편지 그 자체.", "The sealed letter itself."), ('TLS 는 봉인 편지를 낯선 상점과도 쓸 수 있게 해 주는 약속이에요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'TLS is what lets you use sealed letters even with a shop you have never met. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("만료", "Expiry", ("기한 지난 신분증.", "An expired card."), ("빵집 신분증도 기한이 있어요. 지나면 브라우저가 빨간 자물쇠로 돌려세워요.", "The bakery\'s card has a date too. Past it, the browser turns you back with a red padlock.")),
    ],
}
