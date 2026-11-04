from _draw import *
from _world import *

# 1. 공연은 끝났는데, 표 예매 시스템은 계속 돌아가야 해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **FAN)
         + bubble(60, 70, 230, 46, "⟦표 예매 사이트가 안 열려요!|the ticket site won't even open!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **DIRECTOR)
         + bubble(450, 70, 230, 46, "⟦어라... 공연은 끝났는데요?|huh... but the show already ended?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦공연은 끝났는데, 표 예매 시스템은 계속 돌아가야 해요|the show is over, but the ticket system still has to keep running⟧", 13, "var(--ink)", cls="d")
         + label(380, 282, "⟦시스템은 \"만들고 끝\"이 아니에요, 만든 뒤 운영이 이어져요|a system isn't \"build it and done\" — running it comes after⟧", 12, "var(--muted)"))

# 2. 왜: 시스템을 안 지켜보면 성능이 티 안 나게 서서히 나빠져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<path d="M80 100 L680 100" stroke="var(--line)" stroke-width="2"/>'
         + '<path d="M80 100 Q300 110 450 160 T680 240" stroke="var(--bad)" stroke-width="4" fill="none"/>'
         + label(80, 85, "⟦오픈 직후|right after launch⟧", 11, "var(--muted)", "start")
         + label(680, 262, "⟦몇 달 후, 예매 사이트가 느려지고 자꾸 멈춰요|months later, the ticket site is slow and keeps stalling⟧", 11, "var(--bad)", "end")
         + person(150, 190, s=0.75, face=SWEAT, **DIRECTOR)
         + label(380, 282, "⟦시스템을 안 지켜보면 성능이 티 안 나게 서서히 나빠져요|left unwatched, a system's performance quietly gets worse over time⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 운영성과관리 = 투어 끝난 뒤에도 시스템을 계속 점검하는 일
MONITOR = '<g transform="translate(560,190)"><rect x="-50" y="-35" width="100" height="70" rx="4" fill="#1B2A44"/><path d="M-35 0 l15 -15 l10 20 l10 -25 l15 10 l10 -5" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><rect x="-12" y="35" width="24" height="10" fill="var(--stone-dark)"/></g>'
P3 = svg(340, sky(340)
         + person(220, 220, s=0.8, face=SMILE, **DIRECTOR)
         + MONITOR
         + label(380, 30, "⟦운영 성과관리 = 투어 끝난 뒤에도 시스템을 계속 점검하는 일|ops performance management = keeping watch on the system even after the tour ends⟧", 13, "var(--ink)", cls="d")
         + label(380, 326, "⟦공연은 끝나도, 시스템을 지켜보는 일은 계속돼요|the show ends, but watching the system doesn't⟧", 12, "var(--muted)"))

UPTIME_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 7 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LATENCY_I = icon('<path d="M10 46 h44" stroke="var(--line)" stroke-width="2"/><path d="M14 40 l10 -14 l10 8 l10 -20" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CSAT_I = icon('<circle cx="32" cy="32" r="22" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><circle cx="24" cy="28" r="3" fill="var(--ink)"/><circle cx="40" cy="28" r="3" fill="var(--ink)"/><path d="M22 40 Q32 48 42 40" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>')
PDCA_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="6 5"/><path d="M48 20 l6 -4 l2 7" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. 운영 점검표
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 250, "⟦운영 점검표|OPS CHECKLIST⟧",
                     ("⟦가동률 — 시스템이 안 멈췄나|uptime — did the system stay up?⟧",
                      "⟦응답속도 — 응답이 느려지지 않았나|latency — did responses slow down?⟧",
                      "⟦만족도 — 관객이 불편하지 않았나|satisfaction — did the audience complain?⟧",
                      "⟦개선 보고 — 다음 투어에 반영|improvement report — feeds the next tour⟧"), 1.0)
         + person(560, 170, s=0.8, **DIRECTOR)
         + label(380, 300, "⟦운영팀은 이 네 항목을 투어 끝난 뒤에도 계속 챙겨요|the ops team keeps tracking these four items even after the tour ends⟧", 12, "var(--ink)", cls="d"))

# 5. 마무리: 투자평가의 질문 '투자가 값을 했나?'는 운영 성과관리로 계속 이어져요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **SPONSOR) + '<g transform="translate(190,265) scale(3.2,0.9)">' + ticket(0, 0) + '</g>' + label(190, 269, "⟦투자가 값을 했나요?|did the money pay off?⟧", 10, "#142033")
         + person(570, 150, s=0.8, face=SMILE, **DIRECTOR) + '<g transform="translate(570,265) scale(3.2,0.9)">' + ticket(0, 0) + '</g>' + label(570, 269, "⟦운영 데이터로 계속 답해요|ops data keeps answering⟧", 10, "#142033")
         + label(380, 305, "⟦투자평가의 질문 '투자가 값을 했나?'는 운영 성과관리로 계속 이어져요|investment evaluation's question, 'did the money pay off?', keeps being answered through ops performance management⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "opsperf", "order": 8,
    "title": ("공연 끝난 뒤의 운영실", "The Ops Room After the Show"),
    "h1": ("<em>정보시스템 운영 성과관리</em>가 뭐예요?", "What is <em>IS Operations Performance Management</em>?"),
    "sub": ("정보시스템 운영 성과관리를, 공연이 끝난 뒤에도 표 예매·음향 시스템을 계속 지켜보는 운영실 이야기로 풀어봤어요.",
            "IS operations performance management, told as a story about an ops room that keeps watching the ticketing and sound systems long after the show ends."),
    "panels": [
        {"svg": P1, "alt": ('관객이 표 예매 사이트가 안 열린다고 항의하고 감독관은 공연이 끝났는데도 당황함', "A fan complains the ticket site won't open, and the director is confused even though the show already ended"),
         "caption": ("공연은 끝났는데, 표 예매 시스템은 계속 돌아가야 해요.", "The show is over, but the ticket system still has to keep running."),
         "small": ("시스템은 \"만들고 끝\"이 아니에요, 만든 뒤 운영이 이어져요.", "A system isn't \"build it and done\" — running it comes after.")},
        {"svg": P2, "alt": ('시스템 성능이 오픈 직후엔 좋다가 몇 달 뒤 서서히 나빠지는 그래프, 감독관이 진땀을 흘림', 'A graph shows system performance fine right after launch, then slowly degrading months later, as the director sweats'),
         "caption": ("시스템을 안 지켜보면 성능이 티 안 나게 서서히 나빠져요.", "Left unwatched, a system's performance quietly gets worse over time."),
         "small": ("오픈 직후 빠르던 시스템도 몇 달 후엔 느려질 수 있어요, 계속 재야 알아요.", "A system that's fast right after launch can slow down months later — only steady measuring shows it.")},
        {"svg": P3, "hero": True, "alt": ('감독관이 웃으며 모니터링 화면을 지켜보고 있음', 'The director smiles while watching a monitoring screen'),
         "caption": ("운영 성과관리는 투어 끝난 뒤에도 시스템을 계속 점검하는 일이에요.", "Ops performance management is keeping watch on the system even after the tour ends."),
         "small": ("공연은 끝나도, 시스템을 지켜보는 일은 계속돼요.", "The show ends, but watching the system doesn't."),
         "tricks": (4, [
             (UPTIME_I, ("가동률 재기", "Measure uptime"), ("시스템이 안 멈췄는지 확인해요", "check the system hasn't gone down"), "calm"),
             (LATENCY_I, ("응답속도 재기", "Measure latency"), ("시스템 응답이 느려지지 않았는지 확인해요", "check system responses haven't slowed down")),
             (CSAT_I, ("만족도 재기", "Measure satisfaction"), ("관객에게 불편함이 없었는지 들어요", "ask the audience about any complaints"), "warm"),
             (PDCA_I, ("개선하고 또 돌리기", "Improve, then repeat"), ("잰 결과를 다음 투어에 반영해요", "feed the results into the next tour")),
         ])},
        {"svg": P4, "alt": ('가동률·응답속도·만족도·개선보고 네 항목의 운영 점검표', 'An ops checklist with four items: uptime, latency, satisfaction, improvement report'),
         "caption": ("운영팀은 가동률·응답속도·만족도·개선 보고를 계속 챙겨요.", "The ops team keeps tracking uptime, latency, satisfaction, and improvement reports."),
         "small": ("운영팀은 이 네 항목을 투어 끝난 뒤에도 계속 챙겨요.", "The ops team keeps tracking these four items even after the tour ends.")},
        {"svg": P5, "alt": ('왼쪽: 후원사가 투자값을 했는지 묻고, 오른쪽: 감독관이 운영 데이터로 계속 답함', 'Left: the sponsor asks if the investment paid off. Right: the director keeps answering with ops data'),
         "caption": ("투자평가의 질문 '투자가 값을 했나?'는 운영 성과관리로 계속 이어져요.", "Investment evaluation's question, 'did the money pay off?', keeps being answered through ops performance management."),
         "small": ("공연 하나가 끝나도, 후원사가 묻고 운영 데이터로 답하는 일은 계속돼요.", "One show ends, but the sponsor keeps asking and the ops data keeps answering.")},
    ],
    "summary": (("<b>정보시스템 운영 성과관리</b> = 공연(프로젝트)이 끝난 뒤에도 <b>가동률·응답속도·만족도를 계속 재고 개선</b>하는 일.",
                 "<b>IS operations performance management</b> = continuing to measure and improve uptime, latency, and satisfaction, even after the project (show) ends."),
                ("정보시스템 운영 성과관리는 가동률(availability)·응답속도(latency)·사용자 만족도 같은 지표를 지속적으로 측정하고, 그 결과를 PDCA(Plan-Do-Check-Act)처럼 반복적으로 개선에 반영하는 활동이에요. IT 투자성과 평가가 '끝난 뒤 한 번' 묻는 질문이라면, 운영 성과관리는 그 질문에 '계속' 답하는 과정이에요.",
                 "IS operations performance management continuously measures metrics like availability, latency, and user satisfaction, feeding results back into improvement through a PDCA (Plan-Do-Check-Act) cycle. If IT investment evaluation asks its question once, after the project ends, operations performance management is the ongoing process of continuing to answer it.")),
    "glossary": [
        ("가동률", "Availability/Uptime", ("시스템이 안 멈춘 시간의 비율.", "The share of time the system stays up."), ("정전 같은 사고로 깎여요.", "Cut down by incidents like outages.")),
        ("응답속도", "Latency", ("요청에 얼마나 빨리 답하는가.", "How fast the system responds to a request."), ("서서히 느려지는 걸 놓치기 쉬워요.", "Easy to miss as it slowly degrades.")),
        ("이용자 만족도", "User Satisfaction", ("관객이 불편함 없이 썼는가.", "Whether the audience used it without friction."), ("설문·문의 건수로 재요.", "Measured via surveys and complaint counts.")),
        ("PDCA", "PDCA", ("계획-실행-점검-개선을 도는 고리.", "The loop of Plan, Do, Check, Act."), ("운영 개선은 이 고리를 계속 돌려요.", "Ops improvement keeps turning this loop.")),
        ("SLA/SLM", "SLA/SLM", ("후원사와 맺은 보장 티켓과 그 관리.", "The guarantee ticket agreed with the sponsor, and managing it."), ('운영 지표는 이 약속을 지켰는지의 근거가 돼요. → <a href="slappe-ko.html">공연을 보장하는 티켓</a>', 'Ops metrics become the evidence that the promise was kept. → <a href="slappe-en.html">the ticket that guarantees the show</a>')),
        ("IT 투자성과 평가", "IT Investment Evaluation", ("공연 끝난 뒤 돈값 했는지 따지는 성적표.", "The scorecard checking if the investment paid off."), ('운영 데이터는 돈값을 했느냐는 질문에 계속 답을 줘요. → <a href="itinvesteval-ko.html">공연 끝난 뒤의 성적표</a>', 'Ops data keeps answering whether the investment paid off. → <a href="itinvesteval-en.html">the scorecard after the show</a>')),
        ("BCP", "BCP", ("정전 같은 큰 사고에도 공연을 잇는 계획.", "The plan that keeps the show going through a disaster."), ('BCP 발동 여부도 운영 기록에 남아요. → <a href="bcpplan-ko.html">정전에도 멈추지 않는 투어</a>', 'Whether BCP had to trigger is logged in ops records too. → <a href="bcpplan-en.html">the tour that doesn\'t stop for a blackout</a>')),
        ("감리/PMO", "IS Audit/PMO", ("프로젝트 전체를 바깥에서 점검하는 역할.", "A role that checks the whole project from the outside."), ('운영 지표도 감리가 점검하는 항목이에요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Ops metrics are among the things audit checks too. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
