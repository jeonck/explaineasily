from _draw import *
from _world import *


def loop_arrow(x, y, r, flip=False):
    sweep = 1 if not flip else 0
    return f'<path d="M{x - r} {y} A{r} {r} 0 1 {sweep} {x + r} {y}" stroke="var(--accent)" stroke-width="4" fill="none" marker-end="url(#rfa)"/>'


ARROW_DEF = '<defs><marker id="rfa" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="var(--accent)"/></marker></defs>'

# 1. 사고가 터진 뒤에야 대응해요
P1 = svg(300, sky(300)
         + conveyor(80, 230, 420)
         + produce(260, 198, 1.2, "var(--bad)", bad=True)
         + person(130, 150, s=0.8, face=SWEAT + EYES, **INSPECTOR)
         + bubble(360, 70, 260, 50, "⟦사고 터졌다! 빨리 대응하자!|an accident! quick, react!⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(380, 285, "⟦사고가 터진 뒤에야 허둥지둥 대응해요|only after an accident hits does anyone scramble to react⟧", 13, "var(--bad)", cls="d"))

# 2. 왜 어려운가: 위험은 씨앗·선별기·운영·바깥 농장까지 곳곳에 흩어져 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(120, 150, s=0.7, face=EYES, **FARMER) + label(120, 240, "⟦씨앗 쪽 위험|risk in the seed⟧", 10, "var(--muted)")
         + person(300, 150, s=0.7, face=EYES, **OPERATOR) + label(300, 240, "⟦선별기 쪽 위험|risk in the sorter⟧", 10, "var(--muted)")
         + person(480, 150, s=0.7, face=EYES, **TEACHER) + label(480, 240, "⟦운영 쪽 위험|risk in operations⟧", 10, "var(--muted)")
         + person(650, 150, s=0.7, face=EYES, **CHEATER) + label(650, 240, "⟦바깥 농장 쪽 위험|risk from outside farms⟧", 10, "var(--muted)")
         + label(380, 280, "⟦위험이 곳곳에 흩어져 있으면, 같은 위험도 매번 다르게 다뤄져요|with risk scattered everywhere, the same risk gets handled differently each time⟧", 12, "var(--ink)", cls="d"))

# 3. AI 리스크 관리 프레임워크 = 검사장 전체를 도는 4단계 운영 지도 (hero)
P3 = svg(400, sky(400)
         + ARROW_DEF
         + label(380, 30, "⟦AI 리스크 관리 프레임워크 = 검사장 전체를 도는 4단계 운영 지도예요|an AI risk management framework is a four-stage map that walks the whole station⟧", 13, "var(--ink)", cls="d")
         + gradeboard(110, 70, 220, 130, "⟦①거버넌스|① GOVERN⟧", ("⟦원칙 세우기|set the principles⟧",))
         + gradeboard(430, 70, 220, 130, "⟦②위험 지도화|② MAP⟧", ("⟦어디에 위험 있는지 찾기|find where risk hides⟧",))
         + gradeboard(430, 240, 220, 130, "⟦③측정|③ MEASURE⟧", ("⟦크기와 빈도 재기|size it and track it⟧",))
         + gradeboard(110, 240, 220, 130, "⟦④관리|④ MANAGE⟧", ("⟦줄이고 다시 살피기|reduce it, then look again⟧",))
         + f'<path d="M330 135 H430" stroke="var(--accent)" stroke-width="4" marker-end="url(#rfa)"/>'
         + f'<path d="M540 200 V240" stroke="var(--accent)" stroke-width="4" marker-end="url(#rfa)"/>'
         + f'<path d="M430 305 H330" stroke="var(--accent)" stroke-width="4" marker-end="url(#rfa)"/>'
         + f'<path d="M220 240 V200" stroke="var(--accent)" stroke-width="4" marker-end="url(#rfa)"/>')

GOV_I = icon('<path d="M32 10 L54 20 V32 C54 44 44 54 32 58 C20 54 10 44 10 32 V20 Z" fill="var(--good)"/>')
MAP_I = icon('<path d="M12 16 L26 10 L40 16 L52 10 V48 L40 54 L26 48 L12 54 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M26 10 V48 M40 16 V54" stroke="var(--line)" stroke-width="2"/>')
MEASURE_I = icon('<rect x="14" y="40" width="10" height="16" fill="var(--accent)"/><rect x="27" y="30" width="10" height="26" fill="var(--accent)"/><rect x="40" y="18" width="10" height="38" fill="var(--accent)"/>')
MANAGE_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M32 18 v8 M44 32 h-8" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "airiskframe", "order": 5,
    "title": ("검사장 전체를 도는 운영 지도", "The Operations Map That Walks the Whole Station"),
    "h1": ("<em>AI 리스크 관리 프레임워크</em>가 뭐예요?", "What is an <em>AI Risk Management Framework</em>?"),
    "sub": ("AI 리스크 관리 프레임워크를, 사고 난 뒤가 아니라 평소에 검사장 전체를 도는 운영 지도 이야기로 풀어봤어요.",
            "An AI risk management framework, told as a story about an operations map that walks the whole station routinely — not just after something breaks."),
    "panels": [
        {"svg": P1, "alt": ("상한 작물이 컨베이어를 지나가자 검수반장이 진땀을 흘리며 사고가 터졌다고 외침", "A rotten item slips down the belt, and the sweating inspector shouts that an accident just happened"),
         "caption": ("사고가 터진 뒤에야 허둥지둥 대응해요.", "Only after an accident hits does anyone scramble to react."),
         "small": ("평소엔 아무도 위험을 미리 들여다보지 않았어요.", "Nobody had looked ahead at the risk beforehand.")},
        {"svg": P2, "alt": ("농부·조작원·교사·몰래 섞는 사람 각자의 자리에 씨앗·선별기·운영·바깥 농장 위험이 따로 흩어져 있음", "Risk sits scattered across the farmer, the operator, the teacher, and the outside world — in the seed, the sorter, operations, and other farms"),
         "caption": ("위험은 씨앗부터 바깥 농장까지 곳곳에 흩어져 있어요.", "Risk is scattered everywhere — from the seed to outside farms."),
         "small": ("같은 위험도 자리마다 다르게 다뤄져요.", "The same kind of risk gets handled differently depending on where it's found.")},
        {"svg": P3, "hero": True, "alt": ("거버넌스·위험 지도화·측정·관리 네 상자가 화살표로 이어져 순환하는 운영 지도", "Four boxes — govern, map, measure, manage — linked by arrows into a running loop"),
         "caption": ("검사장 전체를 도는 4단계 운영 지도예요.", "A four-stage map that walks the whole station."),
         "small": ("한 바퀴 돌고 나면, 다시 처음부터 돌아요 — 끝나는 지도가 아니에요.", "After one loop, it starts over — this map never really finishes."),
         "tricks": (4, [
             (GOV_I, ("①거버넌스", "① Govern"), ("원칙과 책임을 먼저 세워요", "setting principles and accountability first"), "calm"),
             (MAP_I, ("②위험 지도화", "② Map"), ("어디에 위험 있는지 찾아요", "finding where risk hides"), "calm"),
             (MEASURE_I, ("③측정", "③ Measure"), ("크기와 빈도를 재요", "sizing it and tracking it"), "warm"),
             (MANAGE_I, ("④관리", "④ Manage"), ("줄이고 다시 살펴요", "reducing it, then looking again"), "warm"),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦단계별로 하는 일|WHAT EACH STAGE ACTUALLY DOES⟧",
                 ("⟦거버넌스 — 책임자·점검 주기를 정함|govern — names who's accountable, how often it's reviewed⟧",
                  "⟦위험 지도화 — 편향·공격·오작동 지점을 찾음|map — locates bias, attack, and failure points⟧",
                  "⟦측정 — 발생 확률과 피해 크기를 수치화함|measure — quantifies likelihood and impact⟧",
                  "⟦관리 — 완화 조치를 적용하고 재측정함|manage — applies mitigations, then measures again⟧"), 1.0)),
         "alt": ("거버넌스·위험 지도화·측정·관리 각 단계가 실제로 하는 일을 적은 표", "A board spelling out what govern, map, measure, and manage each actually do"),
         "caption": ("네 단계는 각각 구체적인 할 일을 가지고 있어요.", "Each of the four stages has its own concrete job."),
         "small": ("원칙만 있고 실행이 없으면, 지도는 벽에 걸린 그림일 뿐이에요.", "Principles without execution are just a map hanging on the wall.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                 + person(190, 150, s=0.8, face=SMILE, **INSPECTOR) + label(190, 250, "⟦위험을 0으로 만들진 못해요|doesn't bring risk to zero⟧", 11, "var(--ink)")
                 + person(570, 150, s=0.8, face=EYES, **TEACHER) + label(570, 250, "⟦대신 다룰 수 있는 크기로 줄여요|but shrinks it to a manageable size instead⟧", 11, "var(--ink)")
                 + label(380, 282, "⟦리스크 관리는 위험을 없애는 게 아니라, 체계적으로 다루는 일이에요|risk management isn't about erasing risk — it's about handling it systematically⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 검수반장이 위험을 0으로 만들 순 없다고 말함. 오른쪽: 교사가 대신 다룰 수 있는 크기로 줄인다고 말함", "Left: the inspector says risk can't be zeroed out. Right: the teacher says it's shrunk to a manageable size instead"),
         "caption": ("프레임워크가 위험을 완전히 없애주진 않아요.", "The framework doesn't make risk disappear entirely."),
         "small": ("원칙(윤리기준)과 법적 최저선(AI기본법)은 이 지도 위에서 함께 움직여요.", "Ethics principles and the legal baseline both move along this same map.")},
    ],
    "summary": (("<b>AI 리스크 관리 프레임워크</b> = 검사장 전체를 <b>거버넌스·위험지도화·측정·관리</b> 네 단계로 도는 운영 지도.",
                 "<b>An AI risk management framework</b> = an operations map that walks the whole station through <b>govern, map, measure, and manage</b>."),
                ("AI 리스크 관리 프레임워크는 AI 시스템의 위험을 식별(Map)·측정(Measure)·완화(Manage)하고, 이를 조직 차원의 책임 체계(Govern) 안에서 반복적으로 운영하는 절차예요. 미국 NIST AI RMF의 4대 기능(Govern·Map·Measure·Manage)이 대표적인 모델이고, 국내 AI기본법의 위험 평가·안전성 확보조치 요구사항도 같은 흐름을 따라요. 한 번 돌고 끝나는 게 아니라, 모델과 환경이 바뀔 때마다 다시 도는 순환 절차예요.",
                 "An AI risk management framework identifies (Map), measures (Measure), and mitigates (Manage) the risks of an AI system, run repeatedly inside an organization-wide accountability structure (Govern). The US NIST AI RMF's four functions — Govern, Map, Measure, Manage — are the best-known model, and the risk-assessment and safety-assurance requirements in Korea's AI Basic Act follow the same flow. It isn't a one-time pass — it loops again every time the model or its environment changes.")),
    "glossary": [
        ("AI 리스크 관리 프레임워크", "AI risk management framework", ("검사장 전체를 도는 운영 지도.", "The operations map that walks the whole station."), ("한 바퀴로 끝나지 않고 계속 돌아요.", "It doesn't finish after one loop — it keeps going.")),
        ("NIST AI RMF", "NIST AI RMF", ("거버넌스·위험지도화·측정·관리 네 기능.", "The four functions: govern, map, measure, manage."), ("이 분야에서 가장 널리 쓰이는 틀이에요.", "The most widely used framework in this field.")),
        ("AI 윤리기준·거버넌스", "AI ethics & governance", ("①거버넌스 단계가 기대는 원칙판.", "The charter the govern stage leans on."), ('이 지도의 출발점이 되는 원칙이에요. → <a href="aiethicsgov-ko.html">모든 검사장이 함께 쓰는 등급 원칙판</a>', 'The starting principle this map is built on. → <a href="aiethicsgov-en.html">The Grading Charter Every Station Shares</a>')),
        ("위험 평가", "Risk assessment", ("②③단계(위험 지도화·측정)를 합친 말.", "A term that bundles together the map and measure stages."), ("어디에 얼마나 큰 위험이 있는지를 함께 답해요.", "Answers both where the risk is and how big it is.")),
        ("완화 조치", "Mitigation", ("④관리 단계에서 적용하는 실제 조치.", "The concrete action applied in the manage stage."), ("측정된 위험을 줄이기 위한 실행이에요.", "The execution step that shrinks a measured risk.")),
        ("인공지능기본법", "AI Basic Act", ("법이 강제하는 최소한의 위험 관리 의무.", "The minimum risk-management duty the law itself enforces."), ("고영향 AI는 이 지도를 법적 의무로 요구받아요.", "High-impact AI is legally required to walk this same map.")),
        ("잔여 위험", "Residual risk", ("관리한 뒤에도 남는 위험.", "The risk still left after managing it."), ("0이 되지 않는다는 걸 인정하고 받아들이는 부분이에요.", "The part that admits risk never quite reaches zero.")),
        ("공급망 위험", "Supply-chain risk", ("바깥 농장에서 들어오는 위험.", "Risk arriving from outside farms."), ("②위험 지도화 단계가 내 농장 바깥까지 살펴야 하는 이유예요.", "Why the map stage has to look past the station's own fence.")),
    ],
}
