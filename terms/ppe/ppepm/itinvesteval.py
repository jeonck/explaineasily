from _draw import *
from _world import *

# 1. 후원사가 거액을 댔는데, 끝나고 나니 "이게 값을 했나?" 몰라요 (+ 세계관 인트로)
P1 = svg(320, sky(320)
         + label(380, 30, "⟦이 투어 기획사가 곧 IT 프로젝트 조직이에요|this tour company IS the IT project organization⟧", 12, "var(--muted)", cls="d")
         + person(180, 170, s=0.85, face=EYES, **SPONSOR) + contract(260, 150, 0.8)
         + bubble(40, 70, 260, 50, "⟦우리 돈, 값을 했나요?|did our money pay off?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(560, 180, s=0.8, face=SWEAT + EYES, **DIRECTOR)
         + label(380, 300, "⟦공연은 끝났는데 숫자로 답할 게 없어요|the show is over, but there's no number to answer with⟧", 13, "var(--ink)"))

# 2. 왜: "관객이 좋아했어요"만으론 후원사를 설득 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(180, 150, s=0.8, face=SMILE, **PLANNER)
         + bubble(70, 70, 230, 46, "⟦관객들이 엄청 좋아했어요!|the audience loved it so much!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=FROWN, **SPONSOR)
         + bubble(460, 70, 230, 46, "⟦그래서 제 돈은 얼마나 돌아왔나요?|so how much of my money came back?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦느낌만으론 안 돼요, 돈과 숫자로 보여줘야 해요|feelings aren't enough — it has to be shown in money and numbers⟧", 12, "var(--ink)", cls="d"))

# 3. hero: IT 투자성과 평가 = 공연 끝난 뒤 돈과 숫자로 매기는 성적표
P3 = svg(340, sky(340)
         + ticket(230, 150, 1.1, text="⟦투자 1억|invested $100k⟧") + ticket(380, 150, 1.1, text="⟦매출 1.4억|revenue $140k⟧")
         + person(540, 180, s=0.85, face=SMILE, **DIRECTOR)
         + label(380, 30, "⟦IT 투자성과 평가 = 공연 끝난 뒤 돈과 숫자로 매기는 성적표|IT investment evaluation = a scorecard for the show, written in money and numbers afterward⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦투자한 만큼 돌아왔는지, 숫자로 확인해요|checking, in numbers, whether the investment paid off⟧", 12, "var(--muted)"))

ROI_I = icon('<circle cx="32" cy="32" r="22" fill="var(--good)"/><path d="M22 36 l8 -10 l6 6 l10 -14" stroke="var(--panel)" stroke-width="4" fill="none" stroke-linecap="round"/>')
NPV_I = icon('<rect x="12" y="24" width="40" height="28" rx="4" fill="var(--accent)"/><path d="M20 24 v-8 M44 24 v-8" stroke="var(--accent)" stroke-width="4"/><text x="32" y="42" text-anchor="middle" font-size="14" fill="var(--panel)" font-weight="700">$</text>')
BSC_I = icon('<rect x="10" y="10" width="20" height="20" fill="var(--good)"/><rect x="34" y="10" width="20" height="20" fill="var(--accent)"/><rect x="10" y="34" width="20" height="20" fill="var(--bad)"/><rect x="34" y="34" width="20" height="20" fill="#C9822B"/>')
QUAL_I = icon('<path d="M32 14 l6 14 l15 2 l-11 10 l3 15 l-13 -8 l-13 8 l3 -15 l-11 -10 l15 -2 z" fill="var(--accent)"/>')

# 4. 평가 지표 네 가지 비교표
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 260, "⟦평가 지표|METRICS⟧",
                     ("⟦ROI — 투자 대비 얼마 벌었나|ROI — how much earned per dollar⟧",
                      "⟦NPV — 지금 돈 가치로 환산하면|NPV — value in today's money⟧",
                      "⟦BSC — 재무·관객·운영·성장 네 각도|BSC — finance, audience, ops, growth⟧",
                      "⟦정성 효과 — 브랜드·평판|qualitative — brand, reputation⟧"), 1.0)
         + person(560, 170, s=0.8, face=EYES, **DIRECTOR)
         + label(380, 300, "⟦숫자(정량) + 느낌(정성)을 같이 봐요|look at numbers and intangibles together⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 숫자만으론 못 보는 것도 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + ticket(190, 150, 0.9, text="⟦매출 +40%|revenue +40%⟧") + label(190, 240, "⟦숫자로 바로 보여요|shows up right in the numbers⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **FAN) + bubble(490, 70, 170, 46, "⟦이 투어 팬 됐어요|now I'm a fan of this tour⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦팬심·신뢰 같은 가치는 숫자 하나로 못 담아요, 그래도 평가는 계속돼요|things like fan loyalty don't fit one number — but the evaluation keeps happening⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "itinvesteval", "order": 1,
    "title": ("공연 끝난 뒤의 성적표", "The Scorecard After the Show"),
    "h1": ("<em>IT 투자성과 평가</em>가 뭐예요?", "What is <em>IT Investment Evaluation</em>?"),
    "sub": ("IT 투자성과 평가를, 콘서트 투어가 끝난 뒤 후원사에게 숫자로 답하는 성적표 이야기로 풀어봤어요.",
            "IT investment evaluation, told as a story about answering a sponsor in numbers once the tour is over."),
    "panels": [
        {"svg": P1, "alt": ('후원사가 투자금의 성과를 묻지만 투어 기획사는 답할 숫자가 없음', "The sponsor asks about the investment's payoff, but the tour company has no number to answer with"),
         "caption": ("후원사가 거액을 댔는데, 공연 끝나고 나니 값을 했는지 몰라요.", "The sponsor paid a lot, and once the show's over, nobody knows if it paid off."),
         "small": ("이 투어 기획사가 곧 IT 프로젝트 조직이에요.", "This tour company IS the IT project organization.")},
        {"svg": P2, "alt": ('기획자는 관객 반응이 좋았다고 말하지만 후원사는 돈 얘기를 물음', 'The planner says the audience loved it, while the sponsor asks about the money'),
         "caption": ("\"관객이 좋아했어요\"만으론 후원사를 설득 못 해요.", "\"The audience loved it\" alone can't convince the sponsor."),
         "small": ("느낌만으론 안 돼요, 돈과 숫자로 보여줘야 해요.", "Feelings aren't enough — it has to be shown in money and numbers.")},
        {"svg": P3, "hero": True, "alt": ('투자금과 매출 티켓을 나란히 들고 감독관이 웃음', 'The director smiles, holding the investment and revenue tickets side by side'),
         "caption": ("IT 투자성과 평가는 공연 끝난 뒤 돈과 숫자로 매기는 성적표예요.", "IT investment evaluation is a scorecard for the show, written in money and numbers afterward."),
         "small": ("투자한 만큼 돌아왔는지, 숫자로 확인해요.", "Checking, in numbers, whether the investment paid off."),
         "tricks": (4, [
             (ROI_I, ("ROI 따지기", "Check ROI"), ("투자 대비 수익률이에요", "return per dollar invested"), "calm"),
             (NPV_I, ("NPV 따지기", "Check NPV"), ("미래 돈을 지금 가치로요", "future money, valued today")),
             (BSC_I, ("BSC로 넓게 보기", "Widen with BSC"), ("재무·관객·운영·성장 네 각도", "finance, audience, ops, growth"), "warm"),
             (QUAL_I, ("정성 효과도 보기", "Weigh qualitative gains"), ("브랜드·평판도 효과예요", "brand and reputation count too")),
         ])},
        {"svg": P4, "alt": ('네 가지 평가 지표 체크리스트를 감독관이 점검함', 'The director checks a four-item evaluation metrics checklist'),
         "caption": ("평가는 이 네 가지를 같이 봐요.", "Evaluation looks at these four things together."),
         "small": ("숫자(정량) + 느낌(정성)을 같이 봐요.", "Look at numbers and intangibles together.")},
        {"svg": P5, "alt": ('왼쪽: 매출 증가가 숫자로 드러남. 오른쪽: 관객이 팬이 됐다고 말하지만 숫자로 못 담음', 'Left: the revenue increase shows up in numbers. Right: a fan says they love the tour, but no single number captures it'),
         "caption": ("숫자만으론 못 보는 것도 있어요.", "There's value a single number can't capture."),
         "small": ("팬심·신뢰 같은 가치는 숫자 하나로 못 담아요, 그래도 평가는 계속돼요.", "Things like fan loyalty don't fit one number — but the evaluation keeps happening.")},
    ],
    "summary": (("<b>IT 투자성과 평가</b> = 프로젝트(공연)가 끝난 뒤 <b>투자한 돈만큼 돌아왔는지</b> 숫자와 정성 효과로 함께 확인하는 일.",
                 "<b>IT investment evaluation</b> = after the project (show) ends, checking — in both numbers and intangibles — whether the investment paid off."),
                ("IT 투자성과 평가는 ROI(투자수익률), NPV(순현재가치) 같은 재무 지표와 BSC(균형성과표)의 재무·고객·내부프로세스·학습성장 네 관점, 그리고 브랜드 가치 같은 정성적 효과를 함께 측정해 투자 타당성을 판단하는 활동이에요.",
                 "IT investment evaluation measures financial metrics like ROI and NPV, the four BSC perspectives (financial, customer, internal process, learning & growth), and qualitative effects like brand value, together, to judge whether an investment was worthwhile.")),
    "glossary": [
        ("ROI", "ROI", ("투자 대비 번 돈의 비율.", "The ratio of money earned to money invested."), ("가장 많이 쓰는 기본 지표예요.", "The most commonly used baseline metric.")),
        ("NPV", "NPV", ("미래에 벌 돈을 지금 가치로 당겨온 것.", "Future earnings pulled back to today's value."), ("시간에 따라 돈 가치가 변하는 걸 반영해요.", "Reflects how money's value changes over time.")),
        ("BSC", "Balanced Scorecard", ("재무·관객·운영·성장 네 각도로 보는 성적표.", "A scorecard viewed from four angles: finance, audience, ops, growth."), ("숫자 하나에 치우치지 않게 해줘요.", "Keeps you from leaning on just one number.")),
        ("정성적 효과", "Qualitative Benefit", ("팬심·신뢰처럼 숫자로 못 담는 가치.", "Value like fan loyalty that doesn't fit a number."), ("무시하지 않고 별도로 챙겨요.", "Not ignored — tracked separately instead.")),
        ("프로젝트 위험관리", "Project Risk Mgmt", ("공연 당일 날씨에 대비하는 우산.", "The umbrella that prepares for show-day weather."), ('투자 결정 전에도 위험을 따져요. → <a href="projrisk-ko.html">돌발 상황에 대비하는 우산</a>', 'Risk is weighed before the investment decision too. → <a href="projrisk-en.html">the umbrella for surprises</a>')),
        ("운영 성과관리", "Ops Performance Mgmt", ("공연 끝난 뒤 시설이 계속 잘 굴러가는지 보는 일.", "Watching whether the facilities keep running well after the show."), ('투자 평가는 운영 단계에서도 계속돼요. → <a href="opsperf-ko.html">공연 끝난 뒤의 운영실</a>', 'Evaluation keeps happening through the operations stage too. → <a href="opsperf-en.html">the ops room after the show</a>')),
        ("감리/PMO", "IS Audit/PMO", ("전체를 바깥에서 점검하는 역할.", "A role that checks everything from the outside."), ('다른 세계(출판사)에서 자세히 다뤄요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Covered in depth in another world (publishing house). → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("계약·협상", "Negotiation & Contract", ("출연 계약서에 조건을 적는 일.", "Writing terms into the performance contract."), ('투자 결정은 계약 조건과도 맞물려요. → <a href="negotiation-ko.html">조건을 조율해 서명하기</a>', 'Investment decisions tie into contract terms too. → <a href="negotiation-en.html">tuning terms until both sign</a>')),
    ],
}
