from _draw import *
from _world import *

# 1. 후원사가 친환경·처우까지 묻기 시작해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **SPONSOR)
         + bubble(40, 60, 260, 54, "⟦이 투어, 친환경인가요? 스태프 처우는요?|is this tour eco-friendly? are staff treated well?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **DIRECTOR)
         + label(380, 258, "⟦후원사가 투어의 친환경 여부와 스태프 처우까지 묻기 시작해요|the sponsor starts asking about the tour's eco-impact and staff treatment too⟧", 13, "var(--ink)", cls="d")
         + label(380, 282, "⟦공연만 잘하면 끝인 줄 알았는데, 후원사가 공연 밖의 일까지 물어봐요|we thought a good show was enough — now the sponsor asks about more than the show⟧", 12, "var(--muted)"))

# 2. 왜: 자신있게 말해도 "증거 있어요?"엔 말문이 막혀요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **DIRECTOR)
         + bubble(70, 70, 230, 46, "⟦저희 공연, 최고죠!|our shows are the best!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=EYES, **SPONSOR)
         + bubble(450, 70, 230, 46, "⟦증거 있어요? 숫자로요|got proof? show me the numbers⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦투어가 환경과 처우를 잘 챙긴다는 걸 느낌이 아니라 데이터로 보여줘야 해요|the tour's eco and staff claims have to be shown with data, not just a feeling⟧", 12, "var(--ink)", cls="d"))

# 3. hero: ESG경영 = 환경·사회·지배구조까지 챙기는 투어, IT는 그 증거를 모아요
P3 = svg(340, sky(340)
         + person(170, 220, s=0.8, face=SMILE, **DIRECTOR)
         + '<circle cx="440" cy="190" r="30" fill="var(--good)"/>' + label(440, 198, "⟦E|E⟧", 22, "#FFF8E7", cls="d")
         + '<circle cx="520" cy="190" r="30" fill="var(--accent)"/>' + label(520, 198, "⟦S|S⟧", 22, "#FFF8E7", cls="d")
         + '<circle cx="600" cy="190" r="30" fill="#7B3FA0"/>' + label(600, 198, "⟦G|G⟧", 22, "#FFF8E7", cls="d")
         + label(380, 30, "⟦ESG경영 = 공연 성공뿐 아니라 환경·사회·지배구조도 챙기는 일|ESG management = caring about environment, society, and governance, not just the show's success⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦IT는 환경·사회·지배구조 기록을 데이터로 모으고 보여주는 역할을 해요|IT gathers E, S, and G records as data and presents them⟧", 12, "var(--muted)"))

E_I = icon('<path d="M20 50 Q32 10 48 20 Q50 42 20 50 Z" fill="var(--good)"/>')
S_I = icon('<circle cx="24" cy="24" r="10" fill="var(--accent)"/><circle cx="42" cy="24" r="10" fill="var(--accent)"/><path d="M10 54 q14 -20 28 0 M34 54 q14 -20 28 0" stroke="var(--accent)" stroke-width="4" fill="none"/>')
G_I = icon('<rect x="30" y="8" width="4" height="42" fill="var(--ink)"/><path d="M10 18 h20 M34 18 h20" stroke="var(--ink)" stroke-width="3"/><circle cx="10" cy="28" r="8" fill="none" stroke="var(--ink)" stroke-width="3"/><circle cx="54" cy="28" r="8" fill="none" stroke="var(--ink)" stroke-width="3"/>')
DASH_I = icon('<rect x="10" y="14" width="44" height="34" rx="3" fill="#1B2A44"/><path d="M16 40 l8 -14 l8 8 l14 -18" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. ESG 점검표
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 250, "⟦ESG 점검표|ESG CHECKLIST⟧",
                     ("⟦E — 이동·폐기물 데이터 측정|E — measure travel and waste data⟧",
                      "⟦S — 스태프 처우·안전 기록|S — staff treatment and safety logs⟧",
                      "⟦G — 회계·보고를 투명하게|G — transparent accounting and reporting⟧",
                      "⟦IT — E·S·G 데이터를 모아 대시보드로|IT — gathers E, S, G data into a dashboard⟧"), 1.0)
         + person(560, 170, s=0.8, face=EYES, **DIRECTOR)
         + label(380, 300, "⟦E·S·G 셋 다 숫자와 기록으로 증명해요|E, S, and G are all proven with numbers and records⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 데이터 없이 친환경인 척 포장하면(그린워싱) 금방 들통나요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--bad-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **DIRECTOR) + label(190, 260, "⟦진짜 데이터를 보여주면 후원사의 믿음을 얻어요|showing real data earns the sponsor's trust⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=FROWN + SWEAT, **DIRECTOR) + label(570, 260, "⟦데이터 없이 겉만 포장하면 증거를 댈 때 들통나요|a green image with no data falls apart when proof is asked⟧", 11, "var(--ink)")
         + label(380, 305, "⟦ESG 활동은 홍보만이 아니라 실제 측정과 보고로 뒷받침돼야 해요|ESG claims need real measurement and reporting behind them, not just promotion⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "esgit", "order": 5,
    "title": ("환경·사회·지배구조까지 챙기는 투어", "The Tour That Minds Environment, Society, and Governance Too"),
    "h1": ("<em>ESG 경영과 IT</em>가 뭐예요?", "What is <em>ESG Management and IT</em>?"),
    "sub": ("ESG 경영과 IT의 역할을, 공연 성공뿐 아니라 환경·사회·지배구조까지 증명해야 하는 투어 이야기로 풀어봤어요.",
            "ESG management and IT's role in it, told as a story about a tour that must prove its environmental, social, and governance record, not just a good show."),
    "panels": [
        {"svg": P1, "alt": ('후원사가 투어의 친환경성과 처우를 묻고 감독관은 당황함', "The sponsor asks about the tour's eco-friendliness and staff treatment, and the director is caught off guard"),
         "caption": ("후원사가 투어의 친환경 여부와 스태프 처우까지 묻기 시작해요.", "The sponsor starts asking about the tour's eco-impact and staff treatment too."),
         "small": ("공연만 잘하면 끝인 줄 알았는데, 후원사가 공연 밖의 일까지 물어봐요.", "We thought a good show was enough — now the sponsor asks about more than the show.")},
        {"svg": P2, "alt": ('감독관이 공연이 최고라고 자신하지만 후원사는 증거를 요구함', 'The director confidently claims the shows are the best, but the sponsor demands proof'),
         "caption": ("감독관이 자신있게 말해도, 후원사가 \"증거 있어요?\" 하면 말문이 막혀요.", "The director sounds confident, but stalls the moment the sponsor asks for proof."),
         "small": ("투어가 환경과 처우를 잘 챙긴다는 걸 느낌이 아니라 데이터로 보여줘야 해요.", "The tour's eco and staff claims have to be shown with data, not just a feeling.")},
        {"svg": P3, "hero": True, "alt": ('감독관 옆에 환경·사회·지배구조를 뜻하는 E, S, G 원이 떠 있음', 'Circles marked E, S, and G — for environment, social, and governance — float beside the director'),
         "caption": ("ESG경영은 공연 성공뿐 아니라 환경·사회·지배구조도 챙기는 일이에요.", "ESG management means caring about environment, society, and governance, not just the show's success."),
         "small": ("IT는 환경·사회·지배구조 기록을 데이터로 모으고 보여주는 역할을 해요.", "IT gathers E, S, and G records as data and presents them."),
         "tricks": (4, [
             (E_I, ("E — 환경 측정하기", "E — Measure environment"), ("이동·폐기물 데이터를 재요", "track travel and waste data"), "calm"),
             (S_I, ("S — 사회 챙기기", "S — Mind the social side"), ("스태프 처우·안전을 기록해요", "log staff treatment and safety")),
             (G_I, ("G — 투명하게 보고하기", "G — Report transparently"), ("회계·의사결정을 공개해요", "disclose accounting and decisions"), "warm"),
             (DASH_I, ("IT로 데이터 모으기", "Gather the data with IT"), ("흩어진 E·S·G 숫자를 대시보드 하나로 모아요", "collect scattered E, S, and G numbers into one dashboard")),
         ])},
        {"svg": P4, "alt": ('ESG 점검표: 환경, 사회, 지배구조, IT 역할 네 항목', "An ESG checklist with four items: environment, social, governance, and IT's role"),
         "caption": ("ESG 점검표는 E·S·G 세 축과 그 데이터를 모으는 IT를 함께 봐요.", "The ESG checklist covers E, S, and G, plus the IT that gathers their data."),
         "small": ("E·S·G 셋 다 숫자와 기록으로 증명해요.", "E, S, and G are all proven with numbers and records.")},
        {"svg": P5, "alt": ('왼쪽: 진짜 데이터로 신뢰를 얻는 감독관. 오른쪽: 포장만 하다 들킨 감독관', 'Left: the director earns trust with real data. Right: a director caught after only packaging appearances'),
         "caption": ("데이터 없이 친환경인 척 포장하면(그린워싱) 증거를 요구받을 때 들통나요.", "Claiming to be green with no data behind it — greenwashing — falls apart once someone asks for proof."),
         "small": ("ESG 활동은 홍보만이 아니라 실제 측정과 보고로 뒷받침돼야 해요.", "ESG claims need real measurement and reporting behind them, not just promotion.")},
    ],
    "summary": (("<b>ESG 경영과 IT</b> = 공연 성공뿐 아니라 <b>환경·사회·지배구조</b>까지 챙기고, <b>IT가 그 증거를 데이터로 모아 보여주는</b> 일.",
                 "<b>ESG management and IT</b> = minding environment, society, and governance alongside the show's success — with IT gathering that proof as data and presenting it."),
                ("ESG 경영은 환경(Environment)·사회(Social)·지배구조(Governance) 세 축을 경영에 반영하는 활동이고, IT는 탄소배출·근무기록·회계 데이터를 수집·통합해 대시보드와 지속가능경영보고서로 보여주는 역할을 해요. 실제 측정 없이 홍보만 앞세우면 그린워싱으로 비판받아요.",
                 "ESG management builds Environmental, Social, and Governance concerns into how a business runs. IT's role is collecting and integrating data — carbon emissions, work records, accounting — into dashboards and sustainability reports. Promotion without real measurement behind it draws criticism as greenwashing.")),
    "glossary": [
        ("E — 환경", "Environment", ("이동·폐기물 같은 환경 영향.", "Environmental impact like travel and waste."), ("탄소배출량 측정이 대표적이에요.", "Carbon-footprint measurement is the classic example.")),
        ("S — 사회", "Social", ("스태프·관객 처우와 안전.", "How staff and audience are treated and kept safe."), ("근무환경·안전기록이 포함돼요.", "Includes working conditions and safety logs.")),
        ("G — 지배구조", "Governance", ("투명한 회계·의사결정 구조.", "Transparent accounting and decision-making."), ("이사회·감사·보고 체계가 대표적이에요.", "Board, audit, and reporting structures are typical examples.")),
        ("그린워싱", "Greenwashing", ("실제보다 친환경인 척 근거 없이 포장하는 일.", "Making something look greener than it is, with no proof to back it."), ("증거를 요구받으면 들통나요.", "The claim falls apart once someone asks for proof.")),
        ("지속가능경영보고서", "Sustainability Report", ("ESG 데이터를 모아 공개하는 문서.", "The document that discloses ESG data."), ("IT가 수집한 데이터로 채워져요.", "Filled in with data IT has gathered.")),
        ("데이터 대시보드", "Data Dashboard", ("흩어진 ESG 숫자를 한눈에 보는 화면.", "A single screen showing scattered ESG numbers at a glance."), ("IT가 그 숫자를 자동으로 모아 보여줘요.", "IT gathers those numbers automatically and displays them.")),
        ("IT 투자성과 평가", "IT Investment Evaluation", ("정성적 효과(브랜드)도 함께 보는 성적표.", "A scorecard that also weighs intangibles like brand."), ('IT 투자 평가에서는 ESG 성과를 브랜드·신뢰 같은 정성적 효과로 함께 보기도 해요. → <a href="itinvesteval-ko.html">공연 끝난 뒤의 성적표</a>', 'IT investment evaluation can also count ESG results as intangible gains like brand and trust. → <a href="itinvesteval-en.html">the scorecard after the show</a>')),
        ("운영 성과관리", "Ops Performance Mgmt", ("공연 끝난 뒤에도 시스템 지표를 계속 재는 일.", "Continuing to measure system metrics after the show."), ('전력 사용량 같은 ESG 지표도 시스템 운영 중 꾸준히 재요. → <a href="opsperf-ko.html">공연 끝난 뒤의 운영실</a>', 'ESG metrics like power use get tracked while the system runs too. → <a href="opsperf-en.html">the ops room after the show</a>')),
    ],
}
