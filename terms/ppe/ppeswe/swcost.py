from _draw import *
from _world import *


def coinbag(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-20 -6 Q-24 -28 0 -28 Q24 -28 20 -6 Q26 20 0 30 Q-26 20 -20 -6 Z" fill="#E9B44C"/>'
            f'<path d="M-10 -24 Q0 -34 10 -24" stroke="#C9822B" stroke-width="3" fill="none"/>'
            f'<text x="0" y="8" text-anchor="middle" font-size="16" font-weight="700" fill="#5A3B22">₩</text></g>')


# 1. 작가마다 원고료를 다르게 불러요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **WRITER) + bubble(60, 70, 150, 36, "⟦저는 백만 원요|I'll say a million⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 150, s=0.8, face=SMILE, **WRITER) + bubble(300, 70, 160, 36, "⟦저는 오백만 원요|I'll say five million⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 150, s=0.8, face=FROWN, **EDITOR) + bubble(519, 70, 200, 36, "⟦똑같은 분량인데 왜 다르죠?|same size — why so different?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦원고료를 부르는 기준이 저마다 달라요|everyone names a price by their own rule of thumb⟧", 12, "var(--bad)"))

# 2. 감(느낌)으로 부르면 너무 싸거나 너무 비싸요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 30, "⟦감으로만 부르면 — 분쟁이 나요|price it by feel alone — and disputes follow⟧", 13, "var(--ink)", cls="d")
         + coinbag(230, 150, 1.0) + label(230, 220, "⟦너무 싸요 — 작가가 손해|too cheap — the writer loses out⟧", 11, "var(--ink)")
         + coinbag(530, 150, 1.4) + label(530, 230, "⟦너무 비싸요 — 발주자가 손해|too pricey — the client loses out⟧", 11, "var(--ink)")
         + label(380, 280, "⟦기준이 없으면 둘 다 억울해요|with no standard, both sides end up unhappy⟧", 12, "var(--muted)"))

# 3. 대가산정 = 규모 × 단가로 공정하게 값 매기기 (hero)
RULER_I = icon('<rect x="8" y="26" width="48" height="14" rx="2" fill="#E9B44C"/><rect x="18" y="26" width="2" height="14" fill="#C9822B"/><rect x="28" y="26" width="2" height="14" fill="#C9822B"/><rect x="38" y="26" width="2" height="14" fill="#C9822B"/>')
UNITPRICE_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="38" text-anchor="middle" font-size="18" font-weight="700" fill="#142033">₩</text>')
ADJUST_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 v8 M32 38 v8 M18 32 h8 M38 32 h8" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
MONTH_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="12" width="44" height="12" fill="#C9822B"/><text x="32" y="42" text-anchor="middle" font-size="16" font-weight="700" fill="#142033">M</text>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦대가산정 = 규모 × 단가로 공정하게 값 매기기|cost estimation = pricing fairly as size × unit rate⟧", 14, "var(--ink)", cls="d")
         + ruler(100, 150, 1.4) + label(170, 210, "⟦규모(FP)|size (FP)⟧", 12, "var(--muted)")
         + label(380, 175, "⟦×|×⟧", 22, "var(--ink)", cls="d")
         + coinbag(500, 170, 1.0) + label(500, 225, "⟦단가|unit rate⟧", 12, "var(--muted)")
         + label(620, 175, "⟦=|=⟧", 22, "var(--ink)", cls="d")
         + person(680, 190, s=0.7, face=SMILE, **PRINTER)
         + label(380, 320, "⟦감이 아니라, 잰 규모에 정해진 단가를 곱해서 값을 매겨요|not a guess — multiply the measured size by a fixed unit rate⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "swcost", "order": 17,
    "title": ("매수를 돈으로 바꾸는 계산", "Turning Page Count Into Money"),
    "h1": ("<em>SW 사업 대가산정</em>이 뭐예요?", "What is <em>Software Project Cost Estimation</em>?"),
    "sub": ("SW 사업 대가산정을, 감이 아니라 잰 분량에 정해진 단가를 곱해 원고료를 매기는 이야기로 풀어봤어요.",
            "Software cost estimation, told as a story about pricing a manuscript by its measured size times a fixed rate — not by feel."),
    "panels": [
        {"svg": P1, "alt": ("작가 둘이 같은 분량에 서로 다른 값을 부르고, 편집장이 찡그리며 왜 다르냐고 물음", "Two writers with the same-size manuscript name very different prices, and the editor frowns, asking why they differ"),
         "caption": ("작가마다 원고료를 다르게 불러요.", "Every writer names a different price."),
         "small": ("원고료를 부르는 기준이 저마다 달라요.", "Everyone names a price by their own rule of thumb.")},
        {"svg": P2, "alt": ("작은 돈주머니 옆에 '너무 싸요', 큰 돈주머니 옆에 '너무 비싸요'라고 적힘", "A small money bag labeled too cheap, and a big one labeled too pricey"),
         "caption": ("감(느낌)으로 부르면 너무 싸거나 너무 비싸요.", "Pricing by feel alone ends up too cheap or too pricey."),
         "small": ("기준이 없으면 둘 다 억울해요.", "With no standard, both sides end up unhappy.")},
        {"svg": P3, "hero": True, "alt": ("자(규모)와 돈주머니(단가)를 곱해서 인쇄 감독에게 값을 건네는 장면", "A ruler (size) multiplied by a money bag (unit rate), handing the result to the print supervisor"),
         "caption": ("대가산정은 규모 × 단가로 공정하게 값을 매기는 거예요.", "Cost estimation prices things fairly as size times a unit rate."),
         "small": ("감이 아니라, 잰 규모에 정해진 단가를 곱해서 값을 매겨요.", "Not a guess — the measured size times a fixed rate."),
         "tricks": (4, [
             (RULER_I, ("규모부터 재기", "Measure the size first"), ("기능점수(FP) 자로 재요", "with the function-point ruler"), "calm"),
             (UNITPRICE_I, ("단가표 적용", "Apply the rate table"), ("정해진 기준표의 단가를 곱해요", "multiply by the published unit rate")),
             (ADJUST_I, ("난이도 보정", "Adjust for difficulty"), ("어렵거나 급하면 값을 더 보정해요", "harder or rushed work gets adjusted up")),
             (MONTH_I, ("투입 인월 환산", "Convert to person-months"), ("사람이 몇 달 매달릴지도 가늠해요", "also gauges how many person-months it takes"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 240, "⟦대가산정 공식|THE COST FORMULA⟧",
                                 ("⟦소프트웨어 개발비 = 기능점수 × 기능점수단가|software dev cost = function points × unit rate per FP⟧",
                                  "⟦+ 난이도·규모·지역 등 보정계수|+ adjustments for difficulty, scale, region⟧",
                                  "⟦+ 기술료(이윤) + 직접경비|+ technology fee (profit) + direct expenses⟧",
                                  "⟦= 소프트웨어사업 대가|= the total software project cost⟧"), 1.0)),
         "alt": ("기능점수 × 단가에 보정계수와 기술료, 직접경비를 더해 최종 대가를 구하는 공식 안내판", "A guide to the formula: function points × rate, plus adjustments, technology fee, and direct expenses, for the final cost"),
         "caption": ("이렇게 더해서 최종 대가가 나와요.", "Adding these up gives the final cost."),
         "small": ("규모값에 보정과 기술료, 실제 경비까지 더해야 비로소 값이 완성돼요.", "The size value needs adjustments, a technology fee, and real expenses added before the price is complete.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.8, face=SMILE, **EDITOR) + label(190, 265, "⟦기준표는 참고치예요|the rate table is a reference⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.8, face=EYES, **PRINTER) + label(560, 265, "⟦최종 값은 계약으로 정해요|the final price still comes from the contract⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦기준표가 전부를 정해주진 않아요|the rate table doesn't decide everything⟧", 13, "var(--bad)", cls="d")
                    + label(380, 280, "⟦값을 매긴 뒤엔, 이 계획이 다른 책들에 끼칠 영향도 봐야 해요|once priced, you still have to weigh its effect on the other books too⟧", 11, "var(--muted)")),
         "alt": ("편집장은 기준표가 참고치라 말하고, 인쇄 감독은 최종 값은 계약으로 정한다고 말함", "The editor says the rate table is a reference; the print supervisor says the final price still comes from the contract"),
         "caption": ("기준표가 전부를 정해주진 않아요.", "The rate table doesn't decide everything."),
         "small": ('공정한 기준표가 있어도 발주자-수행사 협상은 남아요. 다음 이야기: 값을 매긴 뒤 <a href="swimpact-ko.html">다른 책들에 끼칠 영향 보기</a>.',
                   "A fair rate table still leaves room for negotiation. Next: once priced, <a href=\"swimpact-en.html\">checking its effect on the other books</a>.")},
    ],
    "summary": (("<b>SW 사업 대가산정</b> = 작가마다 다르게 부르던 원고료 대신, <b>규모(기능점수) × 단가</b>에 <b>보정계수와 기술료</b>를 더해 공정하게 값을 매기는 일.",
                 "<b>Software project cost estimation</b> = instead of writers each naming their own price, pricing fairly as <b>size (function points) × unit rate</b>, plus <b>adjustments and a technology fee</b>."),
                ("SW 사업 대가산정은 기능점수(FP) 같은 규모 지표에 공인된 단가(기능점수당 단가)를 곱하고, 난이도·규모·지역 보정계수와 기술료, 직접경비를 더해 소프트웨어 개발비를 산출하는 과정이에요. 한국에서는 '소프트웨어 사업 대가기준'(한국소프트웨어산업협회 고시)이 참고 기준으로 쓰여요.",
                 "Software project cost estimation multiplies a size metric like function points by a certified unit rate, then adds adjustments for difficulty, scale, and region plus a technology fee and direct expenses, to arrive at the development cost. In Korea, the published 'Software Project Cost Standard' serves as the reference guide.")),
    "glossary": [
        ("SW 사업 대가산정", "Software Cost Estimation", ("매수를 돈으로 바꾸는 계산.", "Turning page count into money."), ("규모 × 단가가 기본 뼈대예요.", "Size times rate is the basic skeleton.")),
        ("기능점수단가", "Rate per Function Point", ("자로 잰 분량 한 단위의 값.", "The price for one unit of measured size."), ('규모는 → <a href="fpruler-ko.html">매수를 재는 자</a>로 먼저 재요.', 'Size is measured first with → <a href="fpruler-en.html">the ruler that measures page count</a>.')),
        ("투입공수(M/M, 인월)", "Person-Month (M/M)", ("한 사람이 한 달 매달리는 일의 양.", "The amount of work one person does in one month."), ("일정과 인원을 가늠하는 단위예요.", "The unit used to gauge schedule and headcount.")),
        ("난이도 보정계수", "Difficulty Adjustment Factor", ("어려운 책이면 더 쳐주는 비율.", "The extra rate for a harder book."), ("쉬운 산문과 복잡한 전문서는 같은 값일 수 없어요.", "Simple prose and a complex technical book can't be priced the same.")),
        ("기술료", "Technology Fee", ("출판사가 남기는 몫.", "The publisher's own margin."), ("개발비 외에 이윤에 해당하는 부분이에요.", "The profit portion, separate from the raw development cost.")),
        ("직접경비", "Direct Expenses", ("종이값처럼 실제로 들어간 비용.", "Real costs paid out, like the price of paper."), ("출장비, 장비 임차료 같은 실비예요.", "Actual costs such as travel or equipment rental.")),
        ("소프트웨어사업 대가기준", "Software Project Cost Standard", ("출판계가 다 같이 보는 단가표.", "The rate table the whole industry refers to."), ("정부·공공기관 발주의 참고 기준이에요.", "The reference standard for government and public-sector projects.")),
        ("제값주기", "Fair Pricing", ("너무 깎지도, 너무 부풀리지도 않는 것.", "Neither low-balling nor inflating the price."), ("기준표의 가장 큰 목적이에요.", "The whole point of having a rate table in the first place.")),
    ],
}
