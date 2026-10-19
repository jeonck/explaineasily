from _draw import *
from _world import *


def press(x, y, s=1.0, color="#4A5A72"):
    """인쇄기(상용SW에 해당하는 설비)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-34" y="-24" width="68" height="48" rx="4" fill="{color}"/>'
            f'<rect x="-20" y="-40" width="40" height="18" rx="3" fill="#2E3D57"/><circle cx="0" cy="0" r="10" fill="#D8D2C2"/></g>')


# 1. 종합업체가 인쇄기를 자기 마진 붙여서 사옴
P1 = svg(300, sky(300)
         + press(400, 150, 1.0)
         + person(560, 150, s=0.85, face=SMILE, **PRINTER)
         + bubble(380, 50, 260, 48, "⟦제조사 정가 1000만 원 → 저희가 1400만 원에 구해드릴게요|maker's price: $10k → we'll get it for you at $14k⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(180, 180, s=0.75, face=EYES, **EDITOR)
         + label(380, 270, "⟦발주자는 제조사 정가를 몰라요|the client doesn't know the maker's actual price⟧", 12, "var(--ink)"))

# 2. 심지어 저가형으로 몰래 바꿔치기
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + press(260, 150, 0.8, color="var(--bad)") + label(260, 220, "⟦저가형으로 몰래 바꿔요|quietly swapped for a cheaper model⟧", 11, "var(--bad)")
         + person(500, 150, s=0.8, face=EYES, **EDITOR) + label(500, 220, "⟦발주자는 눈치채기 어려워요|hard for the client to even notice⟧", 11, "var(--ink)")
         + label(380, 260, "⟦마진을 남기려다 품질까지 깎이기도 해요|chasing margin can even eat into quality⟧", 12, "var(--ink)", cls="d"))

# 3. 제조사에서 직접 사고, 설치만 맡김 (hero)
P3 = svg(340, sky(340)
         + person(220, 130, s=0.9, face=EYES, **EDITOR) + press(420, 150, 1.1)
         + person(600, 150, s=0.8, face=SMILE, **PRINTER)
         + label(380, 30, "⟦상용SW 직접구매 = 발주자가 제조사와 직접 계약|Direct COTS purchase = the client contracts straight with the maker⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦종합업체는 설치·연동만 맡아요, 가격을 매기지 않아요|the integrator only installs and connects it — no markup⟧", 12, "var(--muted)"))

DIRECT_I = icon('<path d="M14 32 h36" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/><path d="M38 20 l12 12 l-12 12" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
PRICE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M26 22 h8 a6 6 0 0 1 0 12 h-8 a6 6 0 0 0 0 12 h8" stroke="var(--accent)" stroke-width="3" fill="none"/>')
SHIELD2_I = icon('<path d="M32 8 L50 16 V32 C50 44 42 52 32 56 C22 52 14 44 14 32 V16 Z" fill="var(--good)"/><path d="M24 32 l6 6 l12 -14" stroke="#FFF8E7" stroke-width="4" fill="none" stroke-linecap="round"/>')
SPLIT_I = icon('<rect x="10" y="24" width="20" height="16" rx="3" fill="var(--accent)"/><rect x="34" y="24" width="20" height="16" rx="3" fill="#4A5A72"/>')

PAGE = {
    "slug": "swpurchase", "order": 39,
    "title": ("인쇄기를 중간상인 없이 바로 사기", "Buying the Press Machine, No Middleman"),
    "h1": ("<em>상용SW 직접구매</em> 제도가 뭐예요?", "What is <em>Direct COTS Software Purchase</em>?"),
    "sub": ("종합업체를 거치면 마진이 붙고 품질까지 흔들려요 — 제조사에서 바로 사는 이야기예요.",
            "Going through an integrator adds a markup and can even shake quality — a story about buying straight from the maker."),
    "panels": [
        {"svg": P1, "alt": ("인쇄 감독이 제조사 정가보다 비싼 가격을 제시하고, 발주자는 정가를 모름", "The print supervisor quotes a price higher than the maker's list price, and the client doesn't know the real figure"),
         "caption": ("종합업체가 인쇄기를 자기 마진 붙여서 사와요.", "The integrator buys the press machine and adds its own margin."),
         "small": ("발주자는 제조사 정가를 몰라요.", "The client doesn't know the maker's actual price.")},
        {"svg": P2, "alt": ("종합업체가 저가형 인쇄기로 몰래 바꿔치기하고, 발주자는 눈치채기 어려움", "The integrator quietly swaps in a cheaper press machine, and the client has trouble noticing"),
         "caption": ("심지어 저가형으로 몰래 바꿔치기하기도 해요.", "Sometimes it's even quietly swapped for a cheaper model."),
         "small": ("마진을 남기려다 품질까지 깎이기도 해요.", "Chasing margin can even eat into quality.")},
        {"svg": P3, "hero": True, "alt": ("발주자가 제조사와 직접 계약해 인쇄기를 사고, 인쇄 감독은 설치만 맡음", "The client contracts directly with the maker to buy the press machine, and the print supervisor only handles installation"),
         "caption": ("상용SW 직접구매 = 발주자가 제조사와 직접 계약하는 거예요.", "Direct COTS purchase = the client contracts straight with the maker."),
         "small": ("종합업체는 설치·연동만 맡아요, 가격을 매기지 않아요.", "The integrator only installs and connects it — no markup."),
         "tricks": (4, [
             (DIRECT_I, ("제조사와 직접 계약", "Contract directly with the maker"), ("중간 마진을 없애요", "cuts out the middleman's margin"), "calm"),
             (PRICE_I, ("정가로 구매", "Buy at list price"), ("제조사 정가 그대로예요", "the maker's actual list price")),
             (SHIELD2_I, ("품질 그대로 유지", "Quality stays as specified"), ("몰래 바꿔치기할 틈이 없어요", "no room for a quiet swap"), "warm"),
             (SPLIT_I, ("설치는 별도 발주", "Installation ordered separately"), ("종합업체는 연동만 맡아요", "the integrator only handles the hookup")),
         ])},
        {"svg": svg(320, sky(320)
                     + styleguide(60, 40, 300, 240, "⟦통합발주(기존)|BUNDLED PROCUREMENT (old way)⟧",
                                  ("⟦종합업체가 구매|integrator buys it⟧", "⟦마진이 숨겨짐|margin is hidden⟧", "⟦바꿔치기 위험|swap risk⟧"), 1.0)
                     + styleguide(420, 40, 280, 240, "⟦분리발주(직접구매)|SEPARATE PROCUREMENT (direct)⟧",
                                  ("⟦발주자가 직접 구매|client buys it directly⟧", "⟦가격이 투명함|price is transparent⟧", "⟦설치만 별도 계약|install contracted separately⟧"), 1.0, hl=0)),
         "alt": ("왼쪽: 통합발주는 종합업체가 구매해 마진이 숨겨짐. 오른쪽: 분리발주는 발주자가 직접 구매해 가격이 투명함", "Left: bundled procurement lets the integrator buy it with hidden margin. Right: separate procurement has the client buy directly with transparent pricing"),
         "caption": ("발주 방식을 나눠보면 차이가 분명해요.", "Splitting the procurement makes the difference clear."),
         "small": ("가격 투명성과 품질 보장이 분리발주의 핵심 이득이에요.", "Price transparency and guaranteed quality are the main payoff of separate procurement.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                     + person(190, 150, s=0.8, face=SMILE, **EDITOR) + label(190, 240, "⟦제값 주고 제대로 된 걸 사요|pays the real price for the real thing⟧", 11, "var(--ink)")
                     + person(570, 150, s=0.8, face=EYES, **PRINTER) + label(570, 240, "⟦계약이 둘로 나뉘어 관리가 늘어요|two contracts mean more to manage⟧", 11, "var(--ink)")
                     + label(380, 282, "⟦가격·품질은 좋아지지만, 설치 책임을 나누는 계약 관리가 더 필요해요|price and quality improve, but managing two separate contracts takes more care⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 발주자가 제값 주고 제대로 된 인쇄기를 사게 됨. 오른쪽: 계약이 둘로 나뉘어 관리가 늘어남", "Left: the client pays the real price for the real machine. Right: splitting into two contracts means more to manage"),
         "caption": ("직접구매가 전부를 해결해주진 않아요.", "Direct purchase doesn't solve everything."),
         "small": ("가격·품질은 좋아지지만, 설치 책임을 나누는 계약 관리가 더 필요해요.", "Price and quality improve, but managing the split installation responsibility takes more work.")},
    ],
    "summary": (("<b>상용SW 직접구매</b> = 발주자가 상용 소프트웨어(인쇄기)만큼은 <b>제조사와 직접 계약</b>해 구매하고, 종합업체는 <b>설치·연동만</b> 맡게 하는 공공 IT 발주 방식.",
                 "<b>Direct COTS purchase</b> = having the client contract straight with the <b>maker</b> for commercial software, while the integrator handles only <b>installation and integration</b> — a public-sector IT procurement practice."),
                ("공공 정보화 사업에서 시스템통합업체(SI)가 상용SW까지 통째로 구매·공급하면 중간 마진이 붙고, 예산에 맞추려 저가 제품으로 바뀌는 등 품질 저하가 생기기 쉬워요. 그래서 제도적으로 발주자가 상용SW는 제조사(공급사)와 직접 계약·구매하고, SI는 설치·연동·커스터마이징만 맡게 분리 발주해요. 이를 통해 가격 투명성과 소프트웨어 제값받기를 함께 꾀해요.",
                 "In public IT projects, when a system integrator (SI) bundles in the purchase of commercial off-the-shelf software, hidden markups and budget-driven downgrades to cheaper products can creep in. To prevent this, procurement rules require the client to contract and buy COTS software directly from its maker, while the SI handles only installation, integration, and customization. This keeps pricing transparent and ensures software gets paid its fair value.")),
    "glossary": [
        ("상용SW 직접구매", "Direct COTS Purchase", ("발주자가 제조사와 직접 계약하는 것.", "The client contracting straight with the maker."), ("분리발주 제도의 핵심이에요.", "The core of separate procurement.")),
        ("분리발주", "Split/Separate Procurement", ("구매와 설치를 서로 다른 계약으로 나누는 것.", "Splitting purchase and installation into separate contracts."), ("직접구매를 가능하게 하는 발주 방식이에요.", "The procurement structure that makes direct purchase possible.")),
        ("COTS", "COTS", ("이미 만들어져 파는 상용 소프트웨어.", "Commercial software that already exists off the shelf."), ("직접 구매 제도가 다루는 대상이에요.", "What direct-purchase rules apply to.")),
        ("SI(시스템통합업체)", "System Integrator (SI)", ("여러 요소를 엮어 전체를 완성하는 업체.", "The company that assembles the pieces into a whole."), ("직접구매 이후엔 설치·연동만 맡아요.", "Handles only installation and integration after direct purchase.")),
        ("제값주기", "Fair Value Payment", ("소프트웨어 가격을 깎지 않고 제대로 지불하는 것.", "Paying software its proper price without discounting it away."), ("직접구매 제도의 목적 중 하나예요.", "One of the goals behind the direct-purchase rule.")),
        ("과업변경", "Scope Change", ("계약 중간에 요구사항이 바뀌는 것.", "Requirements changing partway through the contract."), ("분리발주에서도 여전히 관리해야 할 위험이에요.", "Still a risk to manage even under split procurement.")),
        ("하도급 관리", "Subcontract Management", ("설치·연동을 맡은 업체를 관리하는 일.", "Managing the company that handles installation and integration."), ("계약이 나뉘면 이 관리도 늘어나요.", "Splitting the contract means more of this to manage.")),
        ("좋은 소프트웨어의 조건", "Conditions of Good Software", ("직접 사 와도 품질은 저절로 보장되지 않아요.", "Buying it directly doesn't automatically guarantee quality."), ('품질은 결국 이 조건들로 판단해요. → <a href="goodsw-ko.html">좋은 책의 조건</a>', 'Quality is ultimately judged by these conditions. → <a href="goodsw-en.html">what makes a good book</a>')),
    ],
}
