from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


WALLET_P = '<rect x="8" y="18" width="48" height="32" rx="5" fill="#8B5E3C"/><rect x="8" y="26" width="48" height="8" fill="#6E4A2E"/><circle cx="46" cy="30" r="4" fill="#E9B44C"/>'
PHONE_P = '<rect x="20" y="8" width="24" height="48" rx="5" fill="#1B2A44"/><rect x="23" y="13" width="18" height="34" fill="#5B8DEF"/><circle cx="32" cy="51" r="2" fill="#8A8A8A"/>'
WAVE_P = ''.join(f'<path d="M{44+i*6} 20 a{8+i*3} {8+i*3} 0 0 1 0 {24+i*8}" fill="none" stroke="var(--accent)" stroke-width="3" opacity="{0.9-i*0.25}"/>' for i in range(3))
CHECK2_P = '<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'
WALLET_I, PHONE_I, WAVE_I, CHECK2_I = icon(WALLET_P), icon(PHONE_P), icon(WAVE_P), icon(CHECK2_P)

# 1. 전시장을 다 보고 나니, 매표소 줄이 또 길어요
P1 = svg(300, sky(300)
         + booth(320, 100, 200, 120, 1.0, "var(--accent)", "⟦기념품점|GIFT SHOP⟧")
         + person(220, 140, s=0.75, face=EYES, **VISITOR) + glyph(160, 175, 0.9, WALLET_P)
         + label(380, 250, "⟦지갑에서 현금을 세고, 잔돈을 기다리고...|counting cash from a wallet, waiting for change...⟧", 12, "var(--ink)")
         + label(380, 280, "⟦마지막까지 줄을 서야 한다니, 발이 아파요|standing in line right to the very end — my feet hurt⟧", 12, "var(--muted)"))

# 2. 현금도, 카드도, 매번 꺼내고 넣고 번거로워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT, **VISITOR)
         + bubble(300, 70, 240, 44, "⟦지갑은 어디 뒀더라, 카드는 또 어디 있지?|where did I put my wallet — and the card?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦물건을 살 때마다 지갑을 꺼내고, 돈을 세고, 다시 넣는 게 번거로워요|digging out a wallet, counting money, and putting it away at every purchase is a hassle⟧", 12, "var(--ink)"))

# 3. 핀테크 = 스마트폰 하나로 꺼낼 것 없이 바로 찍는 결제 (hero)
P3 = svg(340, sky(340)
         + booth(260, 90, 240, 150, 1.0, "var(--good)", "⟦매표소|TICKETS⟧")
         + glyph(350, 150, 1.0, PHONE_P) + glyph(410, 150, 1.0, WAVE_P)
         + person(620, 240, s=0.8, face=SMILE, **VISITOR)
         + label(380, 30, "⟦핀테크 = 금융에 IT를 더한 서비스, 대표 예는 폰으로 찍어 내는 간편결제|fintech = finance plus IT; its best-known example is one-tap phone payment⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦현금도 실물 카드도 꺼낼 필요 없이, 폰 한 번이면 결제가 끝나요|no cash or physical card to dig out — one phone tap and payment's done⟧", 12, "var(--muted)"))

# 4. 간편결제가 되는 순서
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦간편결제의 순서|HOW SIMPLE PAYMENT WORKS⟧",
                     ("⟦① 카드 정보를 앱에 미리 등록해요|① register your card info in the app beforehand⟧",
                      "⟦② 결제할 때 폰을 갖다 대거나 찍어요|② tap or scan your phone at checkout⟧",
                      "⟦③ 결제망이 암호화된 정보로 결제를 확인해요|③ the network verifies payment with encrypted data⟧",
                      "⟦④ 영수증이 화면에 바로 남아요|④ the receipt appears on screen right away⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦금융에 이런 기술을 더한 서비스를 핀테크라고 불러요|finance combined with tech like this is called fintech⟧", 11, "var(--muted)"))

# 5. 한계 - 폰 배터리가 없거나 네트워크가 끊기면, 결제가 멈춰요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 110, 1.3, CHECK2_P)
         + label(190, 250, "⟦평소엔 폰 결제가 지갑보다 빠르고 간편해요|day to day, phone payment beats a wallet for speed⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **VISITOR)
         + label(570, 262, "⟦배터리가 없거나 네트워크가 끊기면 결제가 막힐 수 있어요|a dead battery or a dropped network can block payment⟧", 11, "var(--ink)")
         + label(380, 282, "⟦폰 결제는 편리하지만, 전기와 네트워크에 기대는 약점이 있어요|phone payment is handy, but it depends on power and a network⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "fintech", "order": 25,
    "title": ("나가는 길, 폰 하나로 찍는 매표소", "The Exit Booth Where One Phone Tap Pays"),
    "h1": ("<em>핀테크·간편결제</em>가 뭐예요?", "What is <em>Fintech & Simple Payment</em>?"),
    "sub": ("핀테크를, 전시장을 다 둘러보고 나가는 길에 폰 하나로 바로 찍어 결제하는 매표소 이야기로 풀어봤어요.",
            "Fintech, told as a story about the exit booth where, after touring the whole hall, one phone tap is all it takes to pay."),
    "panels": [
        {"svg": P1, "alt": ("관람객이 지갑에서 현금을 세며 줄을 서고 발이 아파함", "A visitor counts cash from a wallet in line, feet aching"),
         "caption": ("전시장을 다 보고 나니, 기념품점 계산 줄이 또 길어요.", "After touring the whole hall, the gift-shop checkout line is long again."),
         "small": ("마지막까지 줄을 서야 한다니, 발이 아파요.", "Standing in line right to the very end — my feet hurt.")},
        {"svg": P2, "alt": ("관람객이 지갑과 카드를 어디 뒀는지 몰라 진땀을 흘림", "A visitor sweats, unsure where the wallet or card went"),
         "caption": ("현금도, 카드도, 결제할 때마다 꺼내고 넣는 게 번거로워요.", "Cash or card, digging it out at every payment is a hassle."),
         "small": ("물건을 살 때마다 지갑을 꺼내고, 돈을 세고, 다시 넣는 게 번거로워요.", "Digging out a wallet, counting money, and putting it away at every purchase is a hassle.")},
        {"svg": P3, "hero": True, "alt": ("관람객이 스마트폰을 매표소에 갖다 대자 물결 모양 신호가 뜨며 결제됨", "A visitor taps a smartphone at the booth, a wave signal shows the payment going through"),
         "caption": ("핀테크는 금융에 IT를 더한 서비스예요. 대표 예가 지갑 없이 스마트폰으로 찍어 내는 간편결제예요.", "Fintech is finance plus IT. Its best-known example is simple payment, where one phone tap replaces digging out a wallet."),
         "small": ("현금도 실물 카드도 꺼낼 필요 없이, 폰 한 번이면 결제가 끝나요.", "No cash or physical card to dig out — one phone tap and payment's done."),
         "tricks": (4, [
             (WALLET_I, ("미리 등록하기", "Register beforehand"), ("카드 정보를 앱에 넣어둬요", "card info is saved in the app")),
             (PHONE_I, ("폰으로 찍기", "Tap with the phone"), ("갖다 대거나 화면을 찍어요", "tap or scan the screen"), "calm"),
             (WAVE_I, ("안전하게 확인하기", "Verify safely"), ("결제 정보를 암호화해 주고받아요", "payment data travels encrypted")),
             (CHECK2_I, ("바로 끝내기", "Finish instantly"), ("영수증이 화면에 바로 남아요", "the receipt appears right away"), "warm"),
         ])},
        {"svg": P4, "alt": ("간편결제 순서 설명판: 등록→찍기→확인→영수증, 안내원이 핀테크를 설명", "A board shows register, tap, verify, receipt; a guide explains fintech"),
         "caption": ("카드를 앱에 등록해두고 폰으로 찍으면, 결제망이 그 결제를 안전하게 확인해요.", "Register your card in the app and tap your phone; the payment network safely verifies the payment."),
         "small": ("금융에 이런 기술을 더한 서비스를 핀테크라고 불러요.", "Finance combined with technology like this is called fintech.")},
        {"svg": P5, "alt": ("왼쪽: 평소엔 결제가 빠르고 간편함. 오른쪽: 배터리가 없어 당황하는 관람객", "Left: payment is usually fast and simple. Right: a visitor flustered by a dead battery"),
         "caption": ("폰 배터리가 없거나 폰·단말기 네트워크가 끊기면, 결제가 막힐 수 있어요.", "A dead phone battery or a dropped connection on the phone or terminal can block payment."),
         "small": ("폰 결제는 편리하지만, 전기와 네트워크에 기대는 약점이 있어요.", "Phone payment is handy, but it depends on power and a network.")},
    ],
    "summary": (("<b>핀테크</b> = 금융을 <b>스마트폰·암호화·네트워크</b>와 엮은 서비스. 대표 예는 지갑 없이 <b>한 번의 터치</b>로 끝내는 간편결제.",
                 "<b>Fintech</b> = financial services woven together with <b>smartphones, encryption, and networks</b>. Its best-known example is simple payment: <b>one tap</b>, no wallet."),
                ("핀테크(FinTech)는 금융(Finance)과 기술(Technology)의 합성어로, 결제·송금·대출·투자·보험 같은 금융 서비스에 IT를 결합한 서비스를 말해요. 대표 예인 간편결제는 흔히 실제 카드 번호 대신 대체 번호(토큰)와 결제마다 새로 만드는 일회용 암호를 주고받는 토큰화(tokenization) 기술로 안전성을 높여요. 다만 간편결제는 기기·배터리·네트워크에 의존한다는 한계도 함께 가져요.",
                 "Fintech — a blend of 'finance' and 'technology' — combines IT with financial services such as payment, money transfer, lending, investing, and insurance. Its best-known example, simple payment, often boosts security with tokenization: a substitute number (token) and a fresh one-time code for each payment are exchanged instead of the real card number. Simple payment's limitation is its dependence on a device, a battery, and a network connection.")),
    "glossary": [
        ("토큰화", "Tokenization", ("실제 카드 번호 대신 쓰는 대체 번호(토큰).", "A substitute number (token) used instead of the real card number."), ("가맹점에는 실제 번호가 넘어가지 않고, 결제마다 일회용 암호가 따라가요.", "The merchant never gets the real number, and each payment carries a one-time code.")),
        ("간편결제", "Simple Payment", ("지갑 없이 폰 하나로 끝내는 결제.", "Payment finished with just a phone, no wallet."), ("핀테크가 가장 널리 퍼진 모습 중 하나예요.", "One of the most widespread forms of fintech.")),
        ("NFC/QR", "NFC/QR", ("폰과 매표소가 신호를 주고받는 방법.", "How the phone and the booth exchange a signal."), ("NFC는 폰을 갖다 대고, QR은 카메라로 찍어요.", "NFC works by holding the phone close; QR works by scanning with a camera.")),
        ("NFT", "NFT", ("디지털 자산에 붙는 토큰 소유 증명서.", "The token-ownership certificate attached to a digital asset."), ('돈이 아니라 자산을 다루는 핀테크의 사촌이에요. → <a href="nft-ko.html">그림에 붙이는 몰래 못 고치는 증명서</a>', "A fintech cousin that certifies assets instead of moving money. → <a href=\"nft-en.html\">the certificate nobody can quietly alter</a>")),
        ("정량적 위험분석", "Quantitative Risk Analysis", ("결제 사고 위험을 숫자로 재는 방법.", "A way to score payment-fraud risk with numbers."), ('핀테크 보안도 이 방식으로 위험을 가늠해요. → <a href="quantrisk-ko.html">위험을 숫자 하나로 적는 전광판</a>', "Fintech security sizes up its risks the same way. → <a href=\"quantrisk-en.html\">the scoreboard that writes risk as one number</a>")),
        ("CPS", "Cyber-Physical System", ("현실의 기계와 컴퓨터 제어가 실시간으로 맞물린 구조.", "Physical machines and computer control locked together in real time."), ('결제 자체가 CPS는 아니지만, 실시간으로 맞물린다는 점이 닮았어요. → <a href="cps-ko.html">화면 속 쌍둥이와 함께 움직이는 기계팔</a>', "A payment isn't itself a CPS, but it shares the real-time back-and-forth. → <a href=\"cps-en.html\">the mechanical arm that moves with its screen twin</a>")),
        ("RPA", "RPA", ("영수증 발급 같은 반복 업무를 대신하는 로봇.", "The robot that handles repetitive tasks like issuing receipts."), ('매표소 안쪽에서 이 로봇이 거들고 있어요. → <a href="rpa-ko.html">규칙대로만 반복하는 로봇 직원</a>', 'Behind the counter, this robot is lending a hand. → <a href="rpa-en.html">the robot worker that only repeats the rule</a>')),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장의 모든 부스를 잇는 흐름이에요. → <a href="fourthindustry-ko.html">전시장 모든 부스를 잇는 하나의 흐름</a>', 'The current linking every booth in this hall. → <a href="fourthindustry-en.html">the one current running through every booth</a>')),
    ],
}
