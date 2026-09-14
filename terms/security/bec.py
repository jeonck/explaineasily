from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat=None, shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
PEN = '<rect x="52" y="60" width="5" height="34" rx="2" fill="#5B8DEF" transform="rotate(-30 54 77)"/>'


def paper(x, y, w, h, title, rows, s=1.0, seal=True):
    """왕의 도장이 찍힌 편지. rows 는 (글, 색) 튜플."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, (r, c) in enumerate(rows):
        out += label(14, 50 + i * 22, r, 11, c, "start")
    if seal:
        out += f'<circle cx="{w - 22}" cy="{h - 22}" r="12" fill="#7B3FA0"/><path d="M{w - 28} {h - 22} l4 4 l8 -8" stroke="#E9B44C" stroke-width="2.5" fill="none"/>'
    return out + "</g>"


def pigeon(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="26" ry="16" fill="var(--stone)"/><circle cx="-24" cy="-12" r="10" fill="var(--stone)"/>'
            f'<path d="M-34 -10 l-8 3 l8 3z" fill="var(--accent)"/><circle cx="-26" cy="-14" r="2" fill="var(--night)"/>'
            f'<path d="M-6 -4 q14 -22 30 -8 q-14 4 -30 8z" fill="var(--stone-dark)"/><path d="M22 6 l14 -4 l-8 10z" fill="var(--stone-dark)"/>'
            f'<rect x="-4" y="12" width="26" height="16" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5"/><path d="M0 16 h18 M0 21 h12" stroke="var(--bad)" stroke-width="1.5"/></g>')


def horn(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0 0 l40 -22 v44 z" fill="#E9B44C"/><rect x="-16" y="-8" width="18" height="16" rx="4" fill="#C9822B"/>'
            f'<path d="M48 -22 a30 30 0 0 1 0 44 M56 -32 a42 42 0 0 1 0 64" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def chest(x, y, s=1.0, locks=1):
    lk = "".join(f'<rect x="{dx - 7}" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M{dx - 4} -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>'
                 for dx in ((0,) if locks == 1 else (-14, 14)))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#E9B44C"/>' for cx, cy in ((-18, 12), (-8, 14), (4, 12), (16, 14))) + "</g>")


def board(x, y, w, h, lines):
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="#2F5D4A" stroke="#8B5E3C" stroke-width="5"/>'
            + "".join(label(w / 2, 28 + i * 22, t, 10, "#F5E6B8") for i, t in enumerate(lines)) + "</g>")


# 1. 왕의 글씨체로 온 편지
P1 = svg(300, sky(300) + '<path d="M480 30 v240" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + person(80, 120, s=0.85, face=FROWN + SWEAT, **CLERK) + label(110, 245, "⟦서기|the clerk⟧", 11, "var(--muted)")
         + paper(165, 50, 270, 140, "⟦왕이 보냄|FROM THE KING⟧", (("⟦급해! 상인에게 금화 100개|urgent! send 100 gold to the merchant⟧", "#142033"), ("⟦오늘 안에, 아무한테도 말 말고|today, and tell no one⟧", "#142033"), ("⟦— 왕|— the king⟧", "#142033")))
         + label(300, 215, "⟦글씨체도 도장도 왕 거예요|the handwriting and seal look like the king\'s⟧", 11, "var(--muted)")
         + bubble(520, 20, 220, 34, "⟦왕 글씨체 연습 백 번|practiced the king\'s hand a hundred times⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + person(600, 110, s=0.85, face=MASK, extra=PEN) + label(630, 240, "⟦마을 어딘가의 도둑|a thief somewhere in the village⟧", 11, "var(--bad)")
         + label(380, 288, "⟦벌레도 링크도 없어요 — 그냥 말뿐이에요|no bug, no link — just words⟧", 12, "var(--ink)", cls="d"))

# 2. 가짜 편지의 사촌들
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + pigeon(130, 110, 1.1) + label(130, 215, "⟦비둘기 쪽지|the pigeon note⟧", 12, "var(--ink)", cls="d") + label(130, 235, "⟦'택배 왔어요, 여기 눌러'|'your parcel is here, tap this'⟧", 10, "var(--muted)")
         + bubble(300, 40, 160, 34, "⟦나 왕인데, 지금 당장|it\'s me, the king — right now⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + person(340, 100, s=0.8, face=MASK) + horn(400, 130, 0.8)
         + label(380, 215, "⟦목소리로 오는 편지|the letter that comes as a voice⟧", 12, "var(--ink)", cls="d") + label(380, 235, "⟦왕 목소리까지 흉내 내요|even the king\'s voice, copied⟧", 10, "var(--muted)")
         + paper(560, 60, 150, 110, "⟦왕이 보냄|FROM THE KING⟧", (("⟦급해|urgent⟧", "#142033"), ("⟦금화 보내|send gold⟧", "#142033"), ("⟦비밀로|tell no one⟧", "#142033")))
         + label(635, 215, "⟦왕인 척 편지|the letter as the king⟧", 12, "var(--ink)", cls="d") + label(635, 235, "⟦우체국 도장이 못 잡아요|the post office stamp can\'t catch it⟧", 10, "var(--muted)")
         + label(380, 285, "⟦가짜 편지엔 사촌이 많아요 — 다 벽이 아니라 사람을 속여요|fake letters have cousins — all of them fool people, not walls⟧", 12, "var(--ink)", cls="d"))

# 3. 세 가지 버릇 (hero)
P3 = svg(360, sky(360)
         + paper(60, 40, 330, 200, "⟦왕이 보냄|FROM THE KING⟧", (("⟦급해! 지금 당장|URGENT! right now⟧", "var(--bad)"), ("⟦아무한테도 말하지 마|tell no one⟧", "var(--bad)"), ("⟦금화는 새 상인 주소로|send the gold to the merchant\'s new address⟧", "var(--bad)"), ("⟦— 왕|— the king⟧", "#142033")))
         + label(225, 268, "⟦세 가지 버릇이 다 있어요|all three habits at once⟧", 11, "var(--muted)")
         + bubble(400, 30, 200, 34, "⟦왕이 급하다시니…|the king says it\'s urgent…⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(450, 120, s=0.85, face=FROWN + SWEAT, **CLERK) + label(480, 245, "⟦서기|the clerk⟧", 11, "var(--muted)")
         + person(620, 110, s=0.9, hat="#E9B44C", shirt="#7B3FA0", face=MASK) + label(650, 245, "⟦왕 옷을 입은 도둑|a thief in the king\'s clothes⟧", 11, "var(--bad)")
         + label(380, 312, "⟦왕의 글씨체로 온 편지 — 벌레 대신 말로 속여요|a letter in the king\'s hand — it fools with words, not bugs⟧", 13, "var(--ink)", cls="d")
         + label(380, 342, "⟦급해요 · 비밀로 · 평소와 다른 길|urgent · secret · not the usual road⟧", 12, "var(--muted)"))

# 4. 막는 법 — 다른 길로 되묻기, 두 사람이 같이 열기
P4 = svg(320, sky(320) + '<path d="M400 30 v260" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + bubble(150, 20, 230, 34, "⟦나? 그런 편지 안 보냈는데|me? I sent no such letter⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(60, 130, s=0.8, face=EYES, **CLERK) + '<path d="M125 190 Q170 160 225 190" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="7 5"/>'
         + person(230, 120, s=0.85, face=SMILE, **KING)
         + label(175, 250, "⟦다른 길로 되묻기|ask back by another road⟧", 12, "var(--ink)", cls="d") + label(175, 268, "⟦편지 말고 직접 가서, 아는 번호로|not the letter — go in person, or the number you know⟧", 10, "var(--muted)")
         + person(460, 120, s=0.7, face=SMILE, **CLERK) + chest(560, 190, 1.2, locks=2) + person(650, 120, s=0.7, face=SMILE, **BLUE)
         + '<path d="M512 185 l24 -8 M608 185 l-24 -8" stroke="#E9B44C" stroke-width="3" stroke-linecap="round"/>'
         + label(560, 250, "⟦두 사람이 같이 열기|two people to open it⟧", 12, "var(--ink)", cls="d") + label(560, 268, "⟦한 명이 속아도 금화는 안 나가요|one fooled, the gold still stays⟧", 10, "var(--muted)")
         + label(380, 306, "⟦금화가 나가기 전에 멈추는 두 가지 길|two ways to stop the gold before it leaves⟧", 12, "var(--ink)", cls="d"))

# 5. 도장은 편지를 거르고, 수업은 사람을 지켜요
P5 = svg(300, sky(300)
         + person(100, 120, s=0.85, face=FROWN, extra=BAG) + label(140, 245, "⟦빈손으로 돌아가요|goes home empty-handed⟧", 11, "var(--muted)")
         + person(290, 120, s=0.75, face=SMILE, **GUARD)
         + '<g transform="translate(350,150)"><rect width="60" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M0 2 L30 22 L60 2" stroke="#C9A86A" stroke-width="2" fill="none"/><circle cx="48" cy="10" r="9" fill="var(--bad)"/><path d="M43 10 l4 4 l6 -7" stroke="#FFF" stroke-width="2" fill="none"/></g>'
         + label(340, 245, "⟦우체국 도장|the post office stamp⟧", 11, "var(--ink)") + label(340, 263, "⟦모르는 편지는 걸러요|filters strangers\' letters⟧", 10, "var(--muted)")
         + person(530, 120, s=0.75, face=SMILE, **CLERK) + board(600, 60, 130, 90, ("⟦급해? 비밀로?|urgent? secret?⟧", "⟦다른 길로 되물어요|→ ask back⟧", "⟦금화는 둘이서|gold takes two⟧"))
         + label(620, 245, "⟦도둑 수업|thief class⟧", 11, "var(--ink)") + label(620, 263, "⟦버릇을 외워요|learn the habits⟧", 10, "var(--muted)")
         + label(380, 290, "⟦도장은 편지를 거르고, 수업은 사람을 지켜요|the stamp filters letters; the class protects people⟧", 12, "var(--ink)", cls="d"))

URGENT_I = icon('<circle cx="32" cy="34" r="20" fill="var(--panel)" stroke="var(--bad)" stroke-width="4"/><path d="M32 20 v14 l10 6" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M22 8 l-8 6 M42 8 l8 6" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
SECRET_I = icon('<path d="M10 20 h44 v24 h-24 l-8 8 v-8 h-12z" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="26" y="28" width="12" height="10" rx="2" fill="var(--bad)"/><path d="M29 28 v-4 a3 3 0 0 1 6 0 v4" stroke="var(--bad)" stroke-width="2.5" fill="none"/>')
ROAD_I = icon('<path d="M32 56 v-18 q0 -10 -12 -14 l-8 -4" stroke="var(--muted)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M32 38 q0 -10 12 -14 l10 -6" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M48 12 l8 6 l-9 4z" fill="var(--bad)"/>')
CROWN_I = icon(f'<circle cx="32" cy="34" r="16" fill="{SKIN}"/><path d="M16 22 l-2 -14 l8 6 l10 -12 l10 12 l8 -6 l-2 14z" fill="#E9B44C"/><rect x="20" y="30" width="24" height="8" fill="#111C30"/>')

PAGE = {
    "slug": "bec", "order": 107,
    "title": ("왕의 글씨체로 온 편지", "The Letter in the King\'s Handwriting"),
    "h1": ("<em>BEC · 스미싱 · 비싱</em>이 뭐예요?", "What are <em>BEC, Smishing and Vishing</em>?"),
    "sub": ("이메일 사기(BEC)와 문자·전화 피싱을 왕의 글씨체를 흉내 내 서기에게 금화를 보내라고 하는 편지 이야기로 풀어봤어요.",
            "Business email compromise, smishing and vishing, told as a story about a letter in the king\'s handwriting that tells the clerk to send gold."),
    "panels": [
        {"svg": P1, "alt": ("서기가 '왕이 보냄' 편지를 받음: 급해, 상인에게 금화 100개, 아무한테도 말 말고. 점선 너머 마을의 도둑이 펜을 들고 '왕 글씨체 연습 백 번'", "The clerk holds a letter marked from the king: urgent, 100 gold to the merchant, tell no one. Beyond a dotted line, a thief in the village holds a pen: practiced the king\'s hand a hundred times"),
         "caption": ("서기에게 왕의 글씨체로 편지가 왔어요. \"급해, 상인에게 금화 보내.\"", "A letter in the king\'s handwriting reaches the clerk. \"Urgent — send gold to the merchant.\""),
         "small": ('<a href="phishing-ko.html">가짜 편지</a>인데 벌레도 링크도 없어요. 그냥 말뿐이에요. 그래서 벌레 카드도 우체국 도장도 잘 못 잡아요.',
                   'It\'s a <a href="phishing-en.html">fake letter</a>, but there\'s no bug and no link. Just words. So bug cards and post office stamps mostly miss it.')},
        {"svg": P2, "alt": ("세 사촌: 쪽지를 단 비둘기('택배 왔어요, 여기 눌러'), 나팔로 왕 목소리를 흉내 내는 도둑('나 왕인데, 지금 당장'), 왕인 척 쓴 편지(급해, 금화 보내, 비밀로)", "Three cousins: a pigeon carrying a note (your parcel is here, tap this), a thief with a horn copying the king\'s voice (it\'s me, the king — right now), and a letter written as the king (urgent, send gold, tell no one)"),
         "caption": ("가짜 편지엔 사촌이 많아요. 비둘기 쪽지로도, 목소리로도 와요.", "Fake letters have cousins. They come as pigeon notes, and as voices."),
         "small": ('비둘기 쪽지는 문자, 목소리는 전화예요. 요즘은 <a href="aisec-ko.html">앵무새</a>가 왕 목소리까지 똑같이 내요. 셋 다 벽이 아니라 사람을 속여요.',
                   'The pigeon note is a text message; the voice is a phone call. These days a <a href="aisec-en.html">parrot</a> can copy the king\'s voice exactly. All three fool people, not walls.')},
        {"svg": P3, "hero": True, "alt": ("큰 편지에 빨간 글씨 셋: 급해! 지금 당장 / 아무한테도 말하지 마 / 금화는 새 상인 주소로. 땀 흘리는 서기 '왕이 급하다시니…', 옆에 왕 옷을 입고 가면을 쓴 도둑", "A big letter with three red lines: URGENT! right now / tell no one / send the gold to the merchant\'s new address. The sweating clerk: the king says it\'s urgent… Beside her, a masked thief in the king\'s clothes"),
         "caption": ("왕의 글씨체로 온 편지는 벌레 대신 말로 속여요. 버릇은 늘 같아요 — 급해요, 비밀로, 평소와 다른 길.", "The letter in the king\'s hand fools with words, not bugs. The habits never change — urgent, secret, not the usual road."),
         "small": ("높은 사람인 척하고, 지금 당장이라 하고, 아무한테도 말하지 말라 하고, 금화 보낼 곳이 평소와 달라요. 이 넷이 같이 오면 거의 늘 도둑이에요.", "Someone important, right now, tell no one, and a new place to send the gold. When these four arrive together, it is almost always the thief."),
         "tricks": (4, [
             (CROWN_I, ("왕인 척", "Plays the king"), ("사장, 거래처, 은행", "the boss, a supplier, the bank"), "warm"),
             (URGENT_I, ("지금 당장", "Right now"), ("생각할 틈을 안 줘요", "no time to think")),
             (SECRET_I, ("아무한테도 말 말고", "Tell no one"), ("되물으면 들통나니까", "asking would expose it")),
             (ROAD_I, ("평소와 다른 길", "Not the usual road"), ("새 주소, 새 계좌", "a new address, a new account"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 서기가 편지 대신 왕에게 직접 가서 묻자 왕이 '나? 그런 편지 안 보냈는데'. 오른쪽: 자물쇠 두 개 달린 금화 상자를 서기와 파란 모자 친구가 각자 열쇠로 같이 엶", "Left: the clerk goes to the king in person instead of answering the letter; the king says: me? I sent no such letter. Right: a gold chest with two locks, opened together by the clerk and a blue-hat friend with their own keys"),
         "caption": ("금화를 보내기 전에 다른 길로 되물어요. 그리고 금화 상자는 두 사람이 같이 열어요.", "Before sending gold, ask back by another road. And the gold chest takes two people to open."),
         "small": ('편지에 적힌 번호 말고 원래 아는 번호로, 또는 직접 가서 물어요. 금화는 <a href="leastprivilege-ko.html">한 사람이 혼자 못 보내게</a> 둘이 확인해요 — 한 명이 속아도 안 나가요.',
                   'Call the number you already know, not the one in the letter — or walk over and ask. And gold needs two people to sign off, so <a href="leastprivilege-en.html">no one can send it alone</a> — one fooled, it still stays.')},
        {"svg": P5, "alt": ("도둑이 빈 가방을 들고 돌아감. 경비가 도장 찍힌 편지를 들고 있고, 서기는 칠판 앞에서 '급해? 비밀로? → 다른 길로 되물어요, 금화는 둘이서'를 배움", "The thief walks away with an empty bag. A guard holds a stamped letter, and the clerk stands at a chalkboard: urgent? secret? → ask back; gold takes two"),
         "caption": ("우체국 도장은 편지를 거르고, 도둑 수업은 사람을 지켜요.", "The post office stamp filters letters; thief class protects people."),
         "small": ('<a href="emailsec-ko.html">우체국 도장</a>은 모르는 곳에서 온 편지를 걸러 줘요. 그래도 남는 편지가 있으니 <a href="awareness-ko.html">도둑 수업</a>에서 버릇을 외워요.',
                   'The <a href="emailsec-en.html">post office stamp</a> filters letters from unknown senders. Some still get through, so everyone learns the habits in <a href="awareness-en.html">thief class</a>.')},
    ],
    "summary": (("<b>BEC</b> = <b>왕(사장)인 척</b> 서기에게 \"급해, 비밀로, 새 주소로 금화 보내\" 하는 <b>벌레 없는 가짜 편지</b>. <b>스미싱</b>은 비둘기 쪽지(문자), <b>비싱</b>은 목소리(전화)로 오는 사촌. 막는 법은 <b>다른 길로 되묻기</b>와 <b>두 사람 확인</b>.",
                 "<b>BEC</b> = a <b>bug-free fake letter</b> that <b>plays the king (the boss)</b> and tells the clerk: urgent, tell no one, send the gold to a new address. <b>Smishing</b> is the cousin that comes as a pigeon note (text); <b>vishing</b>, as a voice (phone). The defense: <b>ask back by another road</b>, and <b>two people to sign off</b>."),
                ("Business Email Compromise / Smishing / Vishing. 경영진·거래처를 사칭해 송금이나 계좌 변경을 유도하는 이메일 사기예요. 첨부파일이나 링크 없이 사회공학만 쓰기도 해서 필터가 놓치기 쉽고, 문자(SMS 피싱)와 전화(음성 피싱)로도 와요. 콜백 확인과 이중 승인이 핵심 방어예요.",
                 "Email fraud that impersonates executives or vendors to trigger wire transfers or bank-detail changes. It often uses social engineering alone — no attachment, no link — so filters miss it, and it also arrives by SMS (smishing) and phone (vishing). Callback verification and dual approval are the core defenses.")),
    "glossary": [
        ("BEC", "BEC", ("왕의 글씨체로 온 편지.", "The letter in the king\'s hand."), ('벌레도 링크도 없이 말로만 속여요. → <a href="phishing-ko.html">우체국인 척하는 편지</a>의 사촌', 'Fools with words alone — no bug, no link. → a cousin of <a href="phishing-en.html">the letter that pretends to be the post office</a>')),
        ("스미싱", "Smishing", ("비둘기 쪽지.", "The pigeon note."), ("짧은 쪽지(문자)로 '여기 눌러'. 택배, 벌금, 당첨이 단골이에요.", "A short note (a text) saying tap here. Parcels, fines and prizes are the usual bait.")),
        ("비싱", "Vishing", ("목소리로 오는 편지.", "The letter that comes as a voice."), ('전화로 왕인 척해요. → <a href="aisec-ko.html">왕의 목소리를 흉내 내는 앵무새</a>', 'Plays the king over the phone. → <a href="aisec-en.html">the parrot that copies the king\'s voice</a>')),
        ("CEO 사기", "CEO fraud", ("왕인 척.", "Playing the king."), ("높은 사람 이름으로 '지금 당장, 비밀로'. 서기는 되묻기 어려워요.", "In an important name: right now, tell no one. Hard for the clerk to question.")),
        ("송금 사기 · 계좌 변경", "Invoice / payment fraud", ("평소와 다른 길.", "Not the usual road."), ("'상인 주소가 바뀌었어요' — 금화가 도둑 상자로 가요.", "The merchant has a new address — and the gold lands in the thief\'s chest.")),
        ("콜백 확인", "Callback verification", ("다른 길로 되묻기.", "Asking back by another road."), ("편지에 적힌 번호 말고, 원래 아는 번호로 전화해요.", "Call the number you already know — never the one in the letter.")),
        ("이중 승인", "Dual approval", ("두 사람이 같이 열기.", "Two people to open it."), ('금화 상자엔 자물쇠 둘. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'Two locks on the gold chest. → <a href="leastprivilege-en.html">only the keys you need</a>')),
        ("이메일 도장", "Email authentication", ("우체국 도장.", "The post office stamp."), ('보낸 사람이 진짜인지 도장으로 확인해요. → <a href="emailsec-ko.html">우체국 도장 세 개</a>', 'Stamps that prove who really sent it. → <a href="emailsec-en.html">three post office stamps</a>')),
    ],
}
