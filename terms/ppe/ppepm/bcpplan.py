from _draw import *
from _world import *

# 1. 공연장에 갑자기 정전이 났어요
P1 = svg(300, night(300)
         + stage(120, 170, 240, 60, dark=True)
         + person(540, 150, s=0.8, face=SWEAT + FROWN, **DIRECTOR)
         + label(380, 250, "⟦공연장에 갑자기 정전이 났어요|the venue suddenly loses power⟧", 12, "#F5E6B8", cls="d")
         + label(380, 282, "⟦공연이 통째로 멈춰버렸어요|the whole show grinds to a halt⟧", 13, "#C9D5E6"))

# 2. 왜: 사전 계획 없으면 패닉에 빠지고 복구가 오래 걸려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.8, face=SWEAT + FROWN, **PLANNER)
         + bubble(40, 70, 260, 50, "⟦어떡하죠? 백업이 없어요!|what do we do? there's no backup!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.8, face=FROWN, **SPONSOR)
         + bubble(450, 70, 260, 50, "⟦관객들이 다 기다리고 있어요|the audience is all waiting⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦사전 계획이 없으면 패닉에 빠지고 복구가 오래 걸려요|without a plan ready, panic sets in and recovery drags on⟧", 12, "var(--ink)", cls="d"))

# 3. hero: BCP = 비상시에도 핵심 공연을 이어가도록 미리 짜둔 계획
P3 = svg(340, sky(340)
         + stage(230, 160, 300, 90)
         + person(150, 220, s=0.85, face=SMILE, **DIRECTOR)
         + '<g transform="translate(600,190)"><rect x="-14" y="-20" width="28" height="44" rx="4" fill="#1B2A44"/><path d="M4 -14 l-10 16 h8 l-4 14 l12 -18 h-8 z" fill="#E9B44C"/></g>'
         + label(380, 30, "⟦BCP = 비상시에도 핵심 공연을 이어가도록 미리 짜둔 계획|BCP = a plan made in advance to keep the core show going, even in an emergency⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦정전이 나도, 이 공연만은 멈추지 않아요|even if the power goes out, this show doesn't stop⟧", 12, "var(--muted)"))

CORE_I = icon('<rect x="28" y="8" width="4" height="48" fill="#5A3B22"/><path d="M32 10 h22 l-7 9 l7 9 h-22 z" fill="var(--good)"/>')
ALT_I = icon('<rect x="18" y="14" width="28" height="36" rx="4" fill="var(--accent)"/><path d="M34 22 l-8 12 h6 l-4 10 l10 -14 h-6 z" fill="#FFF8E7"/>')
RTO_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
DRILL_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. BCP vs DRP 비교
P4 = svg(320, sky(320, ground=False)
         + checklist(60, 30, 300, 260, "⟦BCP vs DRP|BCP vs DRP⟧",
                     ("⟦BCP — 사업(공연) 전체를 지속해요|BCP — keeps the whole business going⟧",
                      "⟦DRP — 무너진 시스템을 복구해요|DRP — recovers the broken system⟧",
                      "⟦RTO — 목표 복구 시간을 정해요|RTO — sets a target recovery time⟧",
                      "⟦DRP는 BCP 안의 한 부분이에요|DRP sits inside BCP as one part⟧"), 1.0)
         + person(560, 170, s=0.8, face=EYES, **DIRECTOR)
         + label(380, 300, "⟦시스템 복구(DRP)는 사업 지속(BCP)의 한 조각이에요|system recovery (DRP) is one piece of keeping the business going (BCP)⟧", 12, "var(--ink)", cls="d"))

# 5. 한계: 서랍에 넣어두기만 하면 소용없어요, 훈련해야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + checklist(70, 110, 240, 110, "⟦BCP 문서|BCP DOC⟧", ("⟦서랍 속에 잠들어 있어요|sitting asleep in a drawer⟧",), 0.9)
         + label(190, 250, "⟦서랍에 넣어두기만 하면 무용지물이에요|left in a drawer, it's useless⟧", 11, "var(--ink)")
         + person(520, 150, s=0.75, face=SMILE, **DIRECTOR) + person(620, 150, s=0.75, face=SMILE, **PLANNER)
         + label(570, 250, "⟦모의훈련을 해야 진짜 작동해요|only a drill makes it actually work⟧", 11, "var(--ink)")
         + label(380, 282, "⟦계획은 서랍에 넣어두는 게 아니라 훈련으로 살아있게 하는 거예요|a plan isn't meant for the drawer — drills keep it alive⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "bcpplan", "order": 6,
    "title": ("정전에도 멈추지 않는 투어", "The Tour That Doesn't Stop for a Blackout"),
    "h1": ("<em>BCP(업무 연속성 계획)</em>이 뭐예요?", "What is <em>BCP (Business Continuity Plan)</em>?"),
    "sub": ("BCP를, 공연장에 정전이 나도 핵심 공연만은 이어가도록 미리 짜둔 계획 이야기로 풀어봤어요.",
            "BCP, told as a story about a plan made in advance to keep the core show going even when the venue loses power."),
    "panels": [
        {"svg": P1, "alt": ('공연장이 정전으로 캄캄해지고 감독관이 당황함', 'The venue goes dark from a power outage, and the director panics'),
         "caption": ("공연장에 갑자기 정전이 났어요.", "The venue suddenly loses power."),
         "small": ("공연이 통째로 멈춰버렸어요.", "The whole show grinds to a halt.")},
        {"svg": P2, "alt": ('기획자는 백업이 없다고 당황하고 후원사는 관객이 기다린다고 재촉함', "The planner panics that there's no backup, while the sponsor presses that the audience is waiting"),
         "caption": ("사전 계획이 없으면 패닉에 빠지고 복구가 오래 걸려요.", "Without a plan ready, panic sets in and recovery drags on."),
         "small": ("무엇부터 살려야 할지조차 그 순간엔 안 보여요.", "Even what to save first isn't obvious in the moment.")},
        {"svg": P3, "hero": True, "alt": ('무대는 비상 전원으로 계속 불이 켜져 있고 감독관이 웃으며 지켜봄', 'The stage stays lit on backup power while the director watches, smiling'),
         "caption": ("BCP는 비상시에도 핵심 공연을 이어가도록 미리 짜둔 계획이에요.", "BCP is a plan made in advance to keep the core show going, even in an emergency."),
         "small": ("정전이 나도, 이 공연만은 멈추지 않아요.", "Even if the power goes out, this show doesn't stop."),
         "tricks": (4, [
             (CORE_I, ("핵심업무 식별하기", "Identify the core"), ("이 공연만은 반드시 살려요", "decide what absolutely must keep running"), "calm"),
             (ALT_I, ("대체 수단 준비하기", "Prepare an alternative"), ("비상 발전기 같은 백업이요", "a backup, like a standby generator")),
             (RTO_I, ("목표 복구시간 정하기", "Set a target recovery time"), ("RTO — 몇 분 안에 되살릴지요", "RTO — how fast it must come back"), "warm"),
             (DRILL_I, ("모의훈련 하기", "Run drills"), ("실제로 해봐야 진짜 작동해요", "only practicing it proves it works")),
         ])},
        {"svg": P4, "alt": ('BCP와 DRP를 비교하는 체크리스트', 'A checklist comparing BCP and DRP'),
         "caption": ("BCP는 사업 전체를, DRP는 무너진 시스템을 봐요.", "BCP covers the whole business; DRP covers the broken system."),
         "small": ("시스템 복구(DRP)는 사업 지속(BCP)의 한 조각이에요.", "System recovery (DRP) is one piece of keeping the business going (BCP).")},
        {"svg": P5, "alt": ('왼쪽: BCP 문서가 서랍 속에 잠들어 있음. 오른쪽: 감독관과 기획자가 모의훈련을 함', 'Left: the BCP document sits asleep in a drawer. Right: the director and planner run a drill'),
         "caption": ("서랍에 넣어두기만 하면 소용없어요.", "Left in a drawer, it's useless."),
         "small": ("계획은 서랍에 넣어두는 게 아니라 훈련으로 살아있게 하는 거예요.", "A plan isn't meant for the drawer — drills keep it alive.")},
    ],
    "summary": (("<b>BCP</b> = 정전 같은 큰 사고가 나도 <b>핵심 업무(공연)를 이어가도록</b> 미리 짜두고, <b>훈련으로 점검</b>하는 계획.",
                 "<b>BCP</b> = a plan made in advance to keep core operations (the show) running through a major disruption like a blackout — and checked with drills."),
                ("BCP(Business Continuity Plan)는 핵심 업무를 식별하고, 목표 복구시간(RTO)과 대체 수단을 정의하며, 정기적인 모의훈련으로 실효성을 점검하는 계획이에요. 비슷한 개념인 DRP(Disaster Recovery Plan)는 IT 시스템 복구에 초점을 맞춘, BCP의 한 구성요소예요.",
                 "BCP (Business Continuity Plan) identifies core operations, defines a target recovery time (RTO) and backup measures, and is checked for real effectiveness through regular drills. DRP (Disaster Recovery Plan), a related concept, focuses on IT system recovery and is one component within BCP.")),
    "glossary": [
        ("핵심업무 식별", "Core Business Identification", ("반드시 지켜야 할 공연을 고르는 일.", "Picking the show that absolutely must go on."), ("모든 걸 다 지킬 순 없어요.", "You can't save everything at once.")),
        ("대체 수단", "Alternative Resource", ("비상 발전기 같은 백업.", "A backup, like a standby generator."), ("핵심업무를 이어가게 해줘요.", "Keeps the core operation running.")),
        ("RTO", "Recovery Time Objective", ("목표로 삼는 복구 시간.", "The target time to be back up."), ("짧을수록 비용이 더 들어요.", "Shorter targets cost more to achieve.")),
        ("모의훈련", "BCP Drill", ("실제로 해보는 연습.", "Actually practicing the plan."), ("훈련 안 한 계획은 서랍 속 종이예요.", "An untested plan is just paper in a drawer.")),
        ("DRP", "DRP", ("무너진 시스템을 복구하는 계획.", "The plan for recovering a broken system."), ('다른 세계(성)에서 자세히 다뤄요. → <a href="drp-ko.html">성이 불타도 다음 날 장사하는 법</a>', 'Covered in depth in another world (the castle). → <a href="drp-en.html">how to open the market the morning after the fire</a>')),
        ("프로젝트 위험관리", "Project Risk Mgmt", ("우산처럼 돌발 상황에 대비하는 일.", "Preparing for surprises, like carrying an umbrella."), ('BCP는 그중 가장 큰 위험에 대한 대비예요. → <a href="projrisk-ko.html">비 오는 날에도 챙기는 우산</a>', 'BCP is the preparation for the biggest risks among them. → <a href="projrisk-en.html">the umbrella you carry even on a dry day</a>')),
        ("운영 성과관리", "Ops Performance Mgmt", ("공연 끝난 뒤 시스템이 잘 굴러가는지 보는 일.", "Watching whether systems keep running well afterward."), ('BCP 발동 여부도 운영 지표로 기록돼요. → <a href="opsperf-ko.html">공연 끝난 뒤의 운영실</a>', 'Whether BCP had to trigger is tracked as an ops metric too. → <a href="opsperf-en.html">the ops room after the show</a>')),
        ("ESG 경영", "ESG Management", ("안전·처우까지 챙기는 경영.", "Management that also minds safety and treatment."), ('BCP의 \'S(사회)\' 축과도 맞닿아 있어요. → <a href="esgit-ko.html">환경·사회·투명성까지 챙기는 투어</a>', 'It touches the \'S\' (social) axis of ESG too. → <a href="esgit-en.html">the tour that minds environment, society, and transparency too</a>')),
    ],
}
