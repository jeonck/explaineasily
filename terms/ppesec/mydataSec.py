from _draw import *

VILLAGER = dict(hat=None, shirt="#4A7A6A", face=SMILE)
SHOPKEEP_A = dict(hat="var(--stone-dark)", shirt="#4A5A72")
SHOPKEEP_B = dict(hat="var(--stone-dark)", shirt="#7B3FA0")
AGENT = dict(hat="#5B8DEF", shirt="#5B8DEF", face=EYES)


def ledgerbook(x, y, s=1.0, color="#FFF8E7"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-30" width="48" height="60" rx="4" fill="{color}" stroke="#C9A86A" stroke-width="3"/>'
            + '<path d="M-14 -14 h28 M-14 -2 h28 M-14 10 h18" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/></g>')


def shopfront(x, y, s=1.0, name=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-46 0 L0 -30 L46 0 Z" fill="var(--stone-dark)"/><rect x="-14" y="20" width="28" height="40" fill="var(--night)"/>'
            + label(0, -40, name, 11, "var(--muted)") + "</g>")


# 1. 손님 장부가 여러 가게에 흩어져 있어요
P1 = svg(320, sky(320)
         + person(380, 110, s=0.85, **VILLAGER) + bubble(260, 20, 260, 40, "⟦내 장부가 어느 가게에 뭐가 있는지 나도 몰라요|I don't even know which shop has which of my own pages⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + shopfront(130, 220, 0.75, "⟦빵 가게|the bakery⟧") + ledgerbook(130, 200, 0.6)
         + shopfront(380, 230, 0.75, "⟦대장간|the smithy⟧") + ledgerbook(380, 210, 0.6)
         + shopfront(630, 220, 0.75, "⟦곳간|the storehouse⟧") + ledgerbook(630, 200, 0.6))

# 2. 가게마다 장부는 자기 것이라고 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.8, **VILLAGER) + bubble(60, 60, 220, 40, "⟦제 장부 좀 보여주세요|please show me my own ledger⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(500, 150, s=0.8, face=FROWN, **SHOPKEEP_A) + ledgerbook(500, 90) + bubble(380, 60, 260, 40, "⟦이건 저희 가게 장부예요, 못 드려요|this is the shop's own ledger — can't hand it over⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦장부는 가게에 있지만, 적힌 내용은 손님 이야기예요|the ledger sits at the shop, but every line is the villager's own story⟧", 11, "var(--ink)", cls="d"))

# 3. 마이데이터 = 내 장부는 내가 보낼 곳을 정해요 (hero)
P3 = svg(340, sky(340)
         + person(130, 170, s=0.8, **VILLAGER) + label(130, 260, "⟦제 장부, B가게로 보내주세요|send my pages to shop B, please⟧", 10, "var(--muted)")
         + shopfront(340, 190, 0.7, "⟦A가게|shop A⟧") + ledgerbook(340, 170, 0.55)
         + '<path d="M390 160 C450 110 500 110 560 150" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>' + ledgerbook(475, 95, 0.5)
         + shopfront(630, 190, 0.7, "⟦B가게|shop B⟧")
         + label(380, 320, "⟦마이데이터 = 내 장부는 내 것, 보낼 곳도 내가 정해요|MyData = the ledger is mine, and I choose where it goes⟧", 13, "var(--ink)", cls="d"))

MINE_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="26" r="7" fill="#C9A86A"/><path d="M20 44 q12 -12 24 0" stroke="#C9A86A" stroke-width="3" fill="none"/>')
ROUTE_I = icon('<circle cx="16" cy="32" r="8" fill="var(--good)"/><circle cx="48" cy="32" r="8" fill="var(--good)"/><path d="M24 32 h16" stroke="var(--good)" stroke-width="3" stroke-dasharray="3 3"/><path d="M34 26 l6 6 l-6 6" stroke="var(--good)" stroke-width="3" fill="none"/>')
VIEW_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2.5"/><rect x="16" y="18" width="14" height="28" fill="var(--good-soft)"/><rect x="34" y="18" width="14" height="14" fill="var(--accent-soft)"/><rect x="34" y="36" width="14" height="10" fill="#5B8DEF"/>')
CONSENT_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 32 h24" stroke="#142033" stroke-width="2.5"/><circle cx="46" cy="46" r="10" fill="var(--good)"/><path d="M41 46 l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "mydataSec", "order": 16,
    "title": ("내 장부는 내가 들고 다닐 권리", "My Right to Carry My Own Ledger"),
    "h1": ("<em>마이데이터</em>가 뭐예요?", "What is <em>MyData</em>?"),
    "sub": ("마이데이터(MyData)를, 여러 가게에 흩어진 내 장부를 내가 직접 다른 가게로 보낼 수 있는 권리 이야기로 풀어봤어요.",
            "MyData, told as a story about the right to send your own scattered ledger pages straight to another shop yourself."),
    "panels": [
        {"svg": P1, "alt": ("손님이 자기 장부가 빵 가게, 대장간, 곳간에 흩어져 있다고 말함", "A villager says their own ledger is scattered across the bakery, the smithy and the storehouse"),
         "caption": ("손님 장부가 여러 가게에 흩어져 있어요.", "The ledger is scattered across many shops."),
         "small": ("내 장부가 어느 가게에 뭐가 있는지, 나도 한눈에 못 봐요.", "Even the villager can't see at a glance which shop holds which of their own pages.")},
        {"svg": P2, "alt": ("손님이 자기 장부를 보여달라고 하자, 가게 주인은 가게 장부라 못 준다고 함", "A villager asks to see their own ledger, but the shopkeeper says it's the shop's own ledger and can't be handed over"),
         "caption": ("가게마다 장부는 자기 것이라고 해요.", "Every shop treats the ledger as its own."),
         "small": ("장부는 가게에 있지만, 적힌 내용은 전부 손님 이야기예요.", "The ledger physically sits at the shop — but every line in it is the villager's own story.")},
        {"svg": P3, "hero": True, "alt": ("손님이 A가게에 B가게로 장부를 보내달라고 하고, A가게가 직접 B가게로 장부 사본을 보냄", "A villager asks shop A to send pages to shop B, and shop A sends a copy directly to shop B"),
         "caption": ("마이데이터는 내 장부를 내가 보낼 곳을 정하는 권리예요.", "MyData is the right to choose where your own ledger goes."),
         "small": ('내 동의가 있으면 가게끼리 바로 보내줘요. → <a href="cbpr-ko.html">CBPR</a>이 나라 간 이전이라면, 마이데이터는 손님 본인의 이전 요청이에요.',
                   'With my consent, shops send it straight to each other. → where <a href="cbpr-en.html">CBPR</a> covers transfers between countries, MyData is the person\'s own request to move it.'),
         "tricks": (4, [
             (MINE_I, ("내 것이라고 선언해요", "Declared mine"), ("장부 내용은 손님의 것이에요", "the ledger's content belongs to the villager"), "calm"),
             (ROUTE_I, ("보낼 곳도 내가 정해요", "I choose where it goes"), ("가게 A에서 가게 B로 직접", "straight from shop A to shop B")),
             (VIEW_I, ("한곳에 모아 볼 수 있어요", "All in one view"), ("여러 가게 장부를 합쳐서 봐요", "combine ledgers from many shops"), "warm"),
             (CONSENT_I, ("동의마다 새로 정해요", "Fresh consent, every time"), ("언제든 다시 거둘 수 있어요", "and can be withdrawn any time")),
         ])},
        {"svg": svg(320, sky(320)
                    + person(120, 110, s=0.7, **VILLAGER) + label(120, 190, "⟦① 동의|① consent⟧", 12, "var(--ink)")
                    + '<path d="M170 100 h60" stroke="var(--good)" stroke-width="3" marker-end=""/>'
                    + shopfront(300, 130, 0.55, "⟦A가게|shop A⟧") + label(300, 190, "⟦② 요청 전달|② request forwarded⟧", 12, "var(--ink)")
                    + '<path d="M350 100 h60" stroke="var(--good)" stroke-width="3"/>'
                    + person(470, 110, s=0.6, **AGENT) + label(470, 190, "⟦③ 마이데이터 사업자|③ a licensed MyData operator⟧", 11, "var(--ink)")
                    + '<path d="M510 100 h60" stroke="var(--good)" stroke-width="3"/>'
                    + shopfront(640, 130, 0.55, "⟦B가게|shop B⟧") + label(640, 190, "⟦④ 전달 완료|④ delivered⟧", 12, "var(--ink)")
                    + label(380, 270, "⟦허가받은 사업자를 거쳐야 하는 경우가 많아요|often routed through a licensed operator, not a raw free-for-all⟧", 12, "var(--ink)", cls="d")),
         "alt": ("손님 동의 → A가게가 요청 전달 → 마이데이터 사업자 → B가게로 전달 완료", "Villager's consent -> shop A forwards the request -> a licensed MyData operator -> delivered to shop B"),
         "caption": ("실제로는 이런 순서로 움직여요.", "In practice, it moves through these steps."),
         "small": ("동의 → 요청 전달 → (허가받은 사업자) → 전달 완료. 아무 가게나 마음대로 보내주는 게 아니에요.", "Consent, then the request forwards, then a licensed operator carries it, then delivery. It isn't just any shop sending it on a whim.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.85, **AGENT) + label(190, 240, "⟦허가받은 사업자만 할 수 있어요|only a licensed operator may do this⟧", 11, "var(--muted)")
                    + person(560, 150, s=0.85, face=FROWN + SWEAT, **SHOPKEEP_B) + label(560, 240, "⟦전달 통로가 뚫리면 전부 새요|a breach of the pipe leaks everything at once⟧", 11, "var(--bad)")
                    + label(380, 280, "⟦편리해진 만큼, 전달 통로를 지키는 게 더 중요해져요|convenience raises the stakes on protecting that delivery pipe⟧", 12, "var(--ink)", cls="d")),
         "alt": ("허가받은 사업자만 마이데이터를 다룰 수 있고, 전달 통로가 뚫리면 한 번에 전부 샐 수 있음", "Only a licensed operator may handle MyData, and a breach of the pipe can leak everything at once"),
         "caption": ("편한 만큼, 지켜야 할 것도 늘어나요.", "The more convenient it gets, the more there is to protect."),
         "small": ('허가받은 사업자만 다룰 수 있고, 전달 통로 보안이 특히 중요해요 → <a href="privacy-ko.html">개인정보 보호</a>, <a href="data3law-ko.html">데이터 3법 개정</a>',
                   'Only a licensed operator may handle it, and securing the delivery pipe matters most of all → <a href="privacy-en.html">privacy</a>, <a href="data3law-en.html">the Three Data Acts amendment</a>')},
    ],
    "summary": (("<b>마이데이터</b> = 여러 가게에 흩어진 내 장부는 <b>내 것</b>이니, <b>내가 동의</b>하면 가게끼리 <b>직접</b> 주고받을 수 있는 권리.",
                 "<b>MyData</b> = the ledger scattered across many shops is <b>mine</b>, so with <b>my consent</b> the shops can hand pages to each other <b>directly</b>."),
                ("MyData, 본인 신용정보·개인정보 이동권. 개인이 자신에 관한 정보를 보유한 기관에 전송을 요구하면, 그 기관이 본인이나 본인이 지정한 다른 기관·마이데이터 사업자에게 표준화된 방식(API)으로 데이터를 전달하는 제도예요. 한국은 신용정보법 개정으로 금융 마이데이터가 먼저 시작됐고, 허가받은 마이데이터 사업자만 중계할 수 있어요.",
                 "MyData — the individual's right to data portability. A person can require an institution holding information about them to transmit it, on request, to the person or to another institution or licensed MyData operator the person designates, via a standardized method (an API). In Korea, financial MyData launched first under an amendment to the Credit Information Act, and only licensed MyData operators may act as the intermediary.")),
    "glossary": [
        ("마이데이터", "MyData", ("내 장부는 내가 보낼 곳을 정하는 권리.", "The right to choose where your own ledger goes."), ("정보 주체 본인이 전송을 요구할 수 있는 권리예요.", "The data subject's own right to require the transfer.")),
        ("전송요구권", "Right to data portability", ("보유 기관에 전송을 요구하는 권리.", "The right to require the holder to transmit it."), ("가게가 거절할 수 없는, 손님이 쥔 요구권이에요.", "A right the villager holds, that the shop cannot refuse.")),
        ("마이데이터 사업자", "Licensed MyData operator", ("가게 사이를 중계하는 허가받은 심부름꾼.", "The licensed go-between carrying pages shop to shop."), ("허가받은 곳만 할 수 있어요.", "Only a licensed one may carry it.")),
        ("표준 API", "Standardized API", ("정해진 전달 통로.", "The fixed delivery pipe."), ("가게마다 다른 방식이 아니라, 정해진 한 가지 통로로 전달돼요.", "Delivered through one fixed pipe, not a different method at every shop.")),
        ("동의 철회", "Withdrawing consent", ("보낸 걸 다시 거두는 것.", "Taking back what was already sent."), ("언제든 전송 동의를 거둘 수 있어요.", "Consent to transfer can be withdrawn at any time.")),
        ("신용정보법", "Credit Information Act", ("금융 마이데이터를 먼저 연 법.", "The law that opened financial MyData first."), ('데이터 3법 중 하나예요. → <a href="data3law-ko.html">데이터 3법 개정</a>', 'One of the Three Data Acts. → <a href="data3law-en.html">the Three Data Acts amendment</a>')),
        ("개인정보 보호", "Privacy", ("보낸 뒤에도 지켜야 하는 약속.", "A promise that still holds after the pages are sent."), ('마이데이터는 동의 기반 전송이지 보호 의무를 없애진 않아요. → <a href="privacy-ko.html">손님 이름표는 손님 것</a>', 'MyData is consent-based transfer — it doesn\'t erase the duty to protect. → <a href="privacy-en.html">the visitor\'s name tag belongs to the visitor</a>')),
        ("CBPR", "CBPR", ("나라 사이의 비슷한 이전 규칙.", "A similar rule, but for crossing kingdoms."), ('마이데이터는 손님 본인의 요청, CBPR은 나라 간 인증이에요. → <a href="cbpr-ko.html">CBPR</a>', 'MyData is the person\'s own request; CBPR is a certification between kingdoms. → <a href="cbpr-en.html">CBPR</a>')),
    ],
}
