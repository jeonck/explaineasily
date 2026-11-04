from _draw import *
from _world import *

OFFICER = dict(hat="#1B7F79", shirt="#4A7B9D")  # 공공기관 담당자 = 발주기관

# 1. 공공기관이 서점에 이미 있는 책을 새로 만들려고 해요
P1 = svg(300, sky(300)
         + label(380, 30, "⟦공공기관이 서점에 이미 있는 책을 새로 만들려고 해요|a public agency plans to make a book the bookstore already sells⟧", 13, "var(--ink)", cls="d")
         + person(130, 130, s=0.8, face=EYES, **OFFICER)
         + bubble(30, 60, 250, 44, "⟦우리 기관 안내서를 직접 만들래요|we'll make our own guidebook in-house⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bookshelf(324, 140, 1.0, n=4) + label(380, 225, "⟦서점에 이미 있는 책|already in the bookstore⟧", 11, "var(--muted)")
         + person(560, 130, s=0.8, face=SWEAT, **EDITOR)
         + bubble(470, 60, 250, 44, "⟦저희가 그 책을 벌써 팔고 있어요|we already sell that very book⟧", 11, "var(--panel)", "var(--line)", "bottom"))

# 2. 같은 책을 공짜로 뿌리면 출판사가 손님을 잃어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 30, "⟦공공기관이 같은 책을 공짜로 뿌리면 어떻게 될까요|what happens if the agency hands out the same book for free?⟧", 13, "var(--bad)", cls="d")
         + person(120, 90, s=0.8, face=SMILE, **OFFICER)
         + manuscript(240, 130, 0.8) + manuscript(300, 160, 0.8)
         + bookshelf(450, 110, 1.0, n=4)
         + person(600, 90, s=0.8, face=FROWN + SWEAT, **EDITOR)
         + label(380, 240, "⟦같은 책을 팔던 출판사는 손님을 잃어요|publishers selling that book lose their customers⟧", 12, "var(--ink)", cls="d")
         + label(380, 270, "⟦출판사가 줄면 나중엔 고를 책도 줄어요|fewer publishers means fewer books to choose from later⟧", 12, "var(--muted)"))

# 3. SW사업 영향평가 = 시작하기 전에 민간 시장에 미칠 영향을 따져보는 일 (hero)
LINK_I = icon('<circle cx="18" cy="32" r="9" fill="var(--accent)"/><circle cx="46" cy="18" r="9" fill="var(--good)"/><circle cx="46" cy="46" r="9" fill="var(--bad)"/><path d="M18 32 L46 18 M18 32 L46 46" stroke="var(--muted)" stroke-width="3"/>')
SCOPE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="6 4"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>')
GRADE_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--good)"/><rect x="27" y="26" width="10" height="28" fill="var(--accent)"/><rect x="42" y="12" width="10" height="42" fill="var(--bad)"/>')
STAKE_I = icon('<circle cx="22" cy="24" r="8" fill="var(--accent)"/><path d="M22 32 v16" stroke="var(--accent)" stroke-width="4"/><circle cx="44" cy="24" r="8" fill="var(--good)"/><path d="M44 32 v16" stroke="var(--good)" stroke-width="4"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦SW사업 영향평가 = 공공 SW사업이 민간 시장에 미칠 영향을 미리 따져보는 일|SW project impact assessment = weighing a public project's effect on the private market first⟧", 13, "var(--ink)", cls="d")
         + person(60, 130, s=0.85, face=EYES, **OFFICER)
         + styleguide(180, 70, 370, 170, "⟦시작하기 전 평가표|THE CHECK BEFORE STARTING⟧",
                      ("⟦서점에 비슷한 책이 있나요?|is a similar book on the shelf?⟧",
                       "⟦사서 쓰면 안 되나요?|could the agency just buy it?⟧",
                       "⟦출판사 손님을 빼앗게 되나요?|would it take publishers' customers?⟧"), 1.0)
         + bookshelf(600, 130, 1.0, n=4) + label(656, 215, "⟦서점(민간 시장)|the private market⟧", 11, "var(--muted)")
         + label(380, 305, "⟦먼저 따져봐야 '사서 쓸지, 새로 만들지'를 제대로 고를 수 있어요|checking first leaves a real choice: buy it or build it⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "swimpact", "order": 18,
    "title": ("서점에 있는 책을 또 만들기 전에", "Before Remaking a Book the Store Already Sells"),
    "h1": ("<em>SW사업 영향평가</em>가 뭐예요?", "What is a <em>Software Project Impact Assessment</em>?"),
    "sub": ("SW사업 영향평가를, 공공기관이 서점에 이미 있는 책을 새로 만들기 전에 출판사들에게 끼칠 영향부터 따져보는 이야기로 풀어봤어요.",
            "A software project impact assessment, told as a story about a public agency weighing the effect on publishers before remaking a book the bookstore already sells."),
    "panels": [
        {"svg": P1, "alt": ("공공기관 담당자가 안내서를 직접 만들겠다고 하자, 출판사 편집장이 그 책을 이미 팔고 있다고 땀 흘리며 말함", "An agency officer says they'll make a guidebook in-house, and a sweating publisher's editor says they already sell it"),
         "caption": ("공공기관이 서점에 이미 있는 책을 새로 만들려고 해요.", "A public agency plans to make a book the bookstore already sells."),
         "small": ("공공기관은 SW사업을 맡기는 발주기관, 서점의 책은 이미 나와 있는 상용 SW예요.", "The agency is the party commissioning a software project; the store's books are commercial software already on sale.")},
        {"svg": P2, "alt": ("공공기관 담당자가 공짜 원고를 나눠주고, 옆에서 출판사 편집장이 손님을 잃어 찡그림", "An agency officer hands out free copies while a publisher's editor frowns, losing customers"),
         "caption": ("공공기관이 같은 책을 공짜로 뿌리면 그 책을 팔던 출판사는 손님을 잃어요.", "If the agency hands out the same book for free, publishers selling it lose customers."),
         "small": ("출판사가 줄어들면 나중엔 공공기관과 독자 모두 고를 책이 줄어요.", "With fewer publishers, the agency and readers alike end up with fewer books to choose from.")},
        {"svg": P3, "hero": True, "alt": ("공공기관 담당자가 서점 책장을 옆에 두고, 시작하기 전 평가표를 확인함", "An agency officer checks a pre-project assessment board, with the bookstore's shelf beside it"),
         "caption": ("SW사업 영향평가는 공공 SW사업이 민간 시장에 미칠 영향을 미리 따져보는 제도예요.", "A software project impact assessment weighs a public software project's effect on the private market in advance."),
         "small": ("먼저 따져봐야 '사서 쓸지, 새로 만들지'를 제대로 고를 수 있어요.", "Checking first leaves a real choice: buy it or build it."),
         "tricks": (4, [
             (SCOPE_I, ("비슷한 상용 SW 찾기", "Look for similar commercial software"), ("서점에 같은 책이 있는지 봐요", "is the same book already on the shelf?"), "calm"),
             (GRADE_I, ("민간 시장 영향 따지기", "Weigh the market effect"), ("출판사 손님을 빼앗는지 봐요", "does it take customers from publishers?")),
             (LINK_I, ("입찰 공고 전에 끝내기", "Finish before the bid notice"), ("사업을 맡기기 전에 미리 해요", "done before the project goes out to bid")),
             (STAKE_I, ("결과 공개하기", "Publish the result"), ("출판사가 재평가를 요청할 수 있어요", "a vendor can request a re-assessment"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 240, "⟦영향평가는 이런 순서예요|THE ASSESSMENT, STEP BY STEP⟧",
                                 ("⟦① 사업을 기획할 때 발주기관이 직접 평가해요|① the ordering agency assesses it while planning the project⟧",
                                  "⟦② 비슷한 상용 SW가 있는지 찾아봐요|② the agency looks for similar commercial software⟧",
                                  "⟦③ 있으면 사서 쓰는 쪽을 먼저 검토해요|③ if one exists, buying it gets considered first⟧",
                                  "⟦④ 결과를 공개하고, 사업자는 재평가를 요청할 수 있어요|④ the result is published, and vendors can request a re-assessment⟧",
                                  "⟦⑤ 과기정통부가 결과를 검토하고 개선을 요청할 수 있어요|⑤ the science ministry can review it and request fixes⟧"), 1.0)),
         "alt": ("발주기관의 평가, 상용 SW 확인, 구매 검토, 결과 공개와 재평가 요청, 과기정통부 검토까지 다섯 단계를 적은 안내판", "A board listing five steps: the agency's assessment, checking for commercial software, considering a purchase, publishing with re-assessment requests, and ministry review"),
         "caption": ("영향평가는 사업을 맡기기 전에 다섯 단계로 이어져요.", "The assessment runs through five steps before the project goes out to bid."),
         "small": ("입찰 공고 전에 평가를 끝내야 '사서 쓰는' 선택지가 살아 있어요.", "Finishing before the bid notice keeps the option to buy alive.")},
        {"svg": svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
                    + person(160, 130, s=0.8, face=SMILE, **EDITOR) + label(190, 260, "⟦출판사는 공짜 책에 시장을 안 빼앗겨요|publishers don't lose the market to free copies⟧", 11, "var(--ink)")
                    + person(540, 130, s=0.8, face=SWEAT, **OFFICER) + label(570, 260, "⟦기관이 직접 평가하니 형식적이지 않게 해야 해요|agencies grade themselves, so it mustn't be a formality⟧", 11, "var(--ink)")
                    + label(380, 305, "⟦영향평가는 새 개발을 막는 제도가 아니라, 민간 시장 영향을 먼저 따지게 하는 제도예요|the assessment doesn't ban new development — it makes the market effect get weighed first⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 출판사가 시장을 지켜 웃음. 오른쪽: 공공기관 담당자가 스스로 평가해야 해서 땀을 흘림", "Left: a publisher smiles, keeping its market. Right: an agency officer sweats, having to assess its own project"),
         "caption": ("영향평가는 개발을 금지하지 않아요. 영향을 먼저 따지게 해요.", "The assessment doesn't ban development. It makes the effect get weighed first."),
         "small": ('평가 뒤 사서 쓰기로 정했다면 이어서 볼 이야기가 있어요. → <a href="swpurchase-ko.html">인쇄기를 중간상인 없이 바로 사기</a>',
                   "If the agency decides to buy, this story comes next. → <a href=\"swpurchase-en.html\">buying the press machine, no middleman</a>")},
    ],
    "summary": (("<b>SW사업 영향평가</b> = 공공기관이 SW사업을 맡기기 전에, 그 사업이 <b>민간 SW 시장에 미칠 영향</b>을 따져보고 <b>이미 있는 상용 SW를 사서 쓸 수 있는지</b> 살펴보는 제도.",
                 "A <b>software project impact assessment</b> = before commissioning a software project, a public agency weighs its <b>effect on the private software market</b> and checks whether <b>existing commercial software could simply be bought</b>."),
                ("SW사업 영향평가는 국가기관·지방자치단체·공공기관이 소프트웨어사업을 추진할 때 민간 소프트웨어 시장에 미치는 영향을 미리 평가하는 소프트웨어 진흥법상의 제도예요. 민간에 상용 소프트웨어가 이미 있으면 사서 쓰게 해 상용 소프트웨어 산업을 살리는 것이 목적이고, 입찰 공고 전에 평가해요. 2023년 개정으로 과학기술정보통신부가 평가 결과를 검토하고 개선을 요청할 수 있게 됐어요. 시스템을 고치기 전에 연관 범위를 따지는 '변경 영향 분석'과는 이름만 비슷한 다른 활동이에요.",
                 "A software project impact assessment is a system under Korea's Software Promotion Act: state bodies, local governments, and public institutions assess in advance how a software project would affect the private software market. Its aim is to support the commercial software industry by having agencies buy software that already exists, and it is done before the bid notice. A 2023 amendment lets the science ministry review the result and request improvements. It is a different activity from 'change impact analysis', which traces what a change to a system would touch, despite the similar name.")),
    "glossary": [
        ("SW사업 영향평가", "SW Project Impact Assessment", ("공공 SW사업이 민간 시장에 미칠 영향을 미리 따지는 제도.", "The system for weighing a public software project's effect on the private market."), ("사업을 맡기기 전에 해요.", "Done before the project is commissioned.")),
        ("소프트웨어 진흥법", "Software Promotion Act", ("이 평가를 하라고 정한 법.", "The law that requires this assessment."), ("공공 SW사업의 여러 규칙을 함께 담고 있어요.", "It also holds other rules for public software projects.")),
        ("발주기관", "Ordering Agency", ("책 만드는 일을 맡기는 공공기관.", "The public body commissioning the book."), ("국가기관·지자체·공공기관이 해당돼요.", "State bodies, local governments, and public institutions.")),
        ("상용 소프트웨어", "Commercial Software", ("서점에 이미 나와 있는 책.", "The book already on the bookstore shelf."), ("새로 안 만들고 사서 쓸 수 있어요.", "It can be bought instead of being built anew.")),
        ("민간 시장 침해", "Crowding Out the Private Market", ("공짜 책 때문에 출판사가 손님을 잃는 일.", "A publisher losing customers to free copies."), ("영향평가가 막으려는 바로 그 문제예요.", "The exact problem the assessment aims to prevent.")),
        ("재평가 요청", "Re-assessment Request", ("평가 결과를 다시 봐 달라고 하는 일.", "Asking for the result to be looked at again."), ("결과를 공개하니 사업자가 요청할 수 있어요.", "Results are published, so vendors can ask for it.")),
        ("상용SW 직접구매", "Direct Purchase of Commercial SW", ("상용 SW를 발주기관이 직접 사는 방식.", "The agency buying commercial software directly."), ('사서 쓰기로 정한 뒤의 이야기예요. → <a href="swpurchase-ko.html">인쇄기를 중간상인 없이 바로 사기</a>', 'What comes after deciding to buy. → <a href="swpurchase-en.html">buying the press machine, no middleman</a>')),
        ("변경 영향 분석", "Change Impact Analysis", ("시스템을 고치기 전에 번질 범위를 따지는 일.", "Tracing how far a change to a system would spread."), ("이름은 비슷해도 다른 활동이니 헷갈리지 마세요.", "A different activity, despite the similar name.")),
    ],
}
