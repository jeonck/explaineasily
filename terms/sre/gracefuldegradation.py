from _draw import *
from _world import *

# 1. 추천 코너가 고장나자 공원 전체 입장을 막아버림 → 손님들이 다 돌아감
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(160, 230, 0.8, color="#5B8DEF", closed=True, label_text="⟦추천 코너|REC. CORNER⟧")
         + booth(400, 230, 1.0, label_text="⟦정문|ENTRANCE⟧")
         + '<g transform="translate(400,243)"><rect x="-46" y="-20" width="92" height="12" fill="var(--bad)" transform="rotate(-8)"/><rect x="-46" y="0" width="92" height="12" fill="var(--bad)" transform="rotate(6)"/></g>'
         + label(400, 60, "⟦오늘은 공원 전체가 문을 닫았어요|the whole park is closed today⟧", 13, "var(--bad)", cls="d")
         + queueline(560, 174, 3, 0.5, 30)
         + label(610, 250, "⟦손님들이 다 돌아가요|all the guests turn back⟧", 11, "var(--bad)")
         + label(380, 285, "⟦추천 코너 하나가 고장나자, 공원 전체 입장을 막아버렸어요|one broken recommendation corner, and the whole park stopped letting guests in⟧", 12, "var(--ink)"))

# 2. 왜: 작은 문제 하나가 전체를 멈추게 설계되어 있으면 손해가 커요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(130, 230, 0.6, color="var(--stone)", closed=True, label_text="⟦작은 고장|small break⟧")
         + '<path d="M190 210 L430 110" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + board(430, 30, 260, 90, "⟦공지|NOTICE⟧", ("⟦공원 전체 폐쇄|PARK CLOSED⟧",), 1.0, hl=0)
         + person(560, 152, s=0.7, face=FROWN, **MANAGER)
         + bubble(470, 190, 220, 50, "⟦손님이 다 돌아가서 손해가 커요|losing guests costs us a lot⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦작은 문제 하나가 전체를 멈추게 설계되어 있으면, 손해가 커져요|when a small problem is wired to stop everything, the cost is huge⟧", 12, "var(--ink)"))

# 3. hero: 덜 중요한 건 잠깐 꺼두고, 핵심 기구는 계속 돌려요
P3 = svg(340, sky(340)
         + ride(140, 280, 0.85, color="var(--accent)", label_text="⟦입장·안전|ENTRY / SAFETY⟧")
         + ride(280, 280, 0.6, color="#5B8DEF", closed=True, label_text="⟦추천 코너 잠시 쉼|REC. CORNER RESTING⟧")
         + queueline(20, 236, 3, 0.4, 22)
         + board(420, 50, 300, 90, "⟦안내|NOTICE⟧", ("⟦추천 코너만 잠시 쉬어요|only the rec corner is resting⟧", "⟦나머지는 그대로예요|everything else runs as usual⟧"), 1.0)
         + person(620, 202, s=0.7, face=SMILE, **OPERATOR)
         + label(380, 30, "⟦덜 중요한 건 잠깐 꺼두고, 중요한 기구는 계속 돌려요|turn off what matters less, keep the core rides running⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦조금 불편해도, 공원은 열려 있어요|a little less convenient, but the park stays open⟧", 12, "var(--muted)"))

# 4. 두 공원 비교: 왼쪽(전부 닫음) vs 오른쪽(핵심만 켜고 나머지는 잠시 쉼)
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + ride(100, 260, 0.7, color="var(--stone)", closed=True) + ride(220, 260, 0.7, color="var(--stone)", closed=True) + booth(300, 260, 0.6)
         + label(190, 40, "⟦문제 하나로 전부 닫은 공원|a park shut down by one problem⟧", 13, "var(--bad)", cls="d")
         + label(190, 300, "⟦다 닫음|all closed⟧", 12, "var(--bad)")
         + ride(480, 260, 0.75, color="var(--accent)") + ride(600, 260, 0.55, color="#5B8DEF", closed=True, label_text="⟦잠시 쉼|resting⟧") + booth(690, 260, 0.55)
         + label(570, 40, "⟦핵심만 남기고 잠시 쉬게 한 공원|a park that only rests the extras⟧", 13, "var(--good)", cls="d")
         + label(570, 300, "⟦핵심만 켜둠|core stays on⟧", 12, "var(--good)"))

# 5. 깨지는 곳: 핵심을 미리 정해두지 않으면 급할 때 못 골라요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 146, s=0.75, face=SWEAT, **OPERATOR)
         + bubble(170, 70, 260, 50, "⟦뭐부터 꺼야 하지?!|what do I turn off first?!⟧", 12, "var(--panel)", "var(--line)", "left")
         + ride(460, 230, 0.55, color="var(--stone)") + label(460, 128, "?", 26, "var(--bad)", cls="d")
         + ride(560, 230, 0.55, color="var(--stone)") + label(560, 128, "?", 26, "var(--bad)", cls="d")
         + ride(660, 230, 0.55, color="var(--stone)") + label(660, 128, "?", 26, "var(--bad)", cls="d")
         + label(380, 282, "⟦뭐가 핵심인지 미리 안 정해두면, 급할 때는 못 골라요 — 평소에 정해둬야 해요|without deciding what's core beforehand, you can't choose it in the heat of the moment — decide it ahead of time⟧", 12, "var(--ink)"))

CORE_I = icon('<path d="M32 8 l7 16 18 2 -14 12 4 18 -15 -9 -15 9 4 -18 -14 -12 18 -2z" fill="var(--accent)"/>')
OFF_I = icon('<rect x="8" y="24" width="48" height="20" rx="10" fill="var(--stone)"/><circle cx="20" cy="34" r="12" fill="var(--bad)"/>')
NOTIFY_I = icon('<path d="M10 14 h36 v22 h-20 l-10 10 v-10 h-6 z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="28" cy="25" r="3" fill="var(--accent)"/>')
KEEP_I = icon('<path d="M32 6 L54 16 V32 C54 46 44 56 32 60 C20 56 10 46 10 32 V16 Z" fill="var(--good)"/><path d="M22 32 l8 8 14 -18" stroke="#FFF8E7" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "gracefuldegradation", "order": 27,
    "title": ("일부만 고장나도 나머지는 그대로", "When Only Part Breaks, the Rest Stays Open"),
    "h1": ("<em>우아한 저하</em>가 뭐예요?", "What is <em>Graceful Degradation</em>?"),
    "sub": ("우아한 저하를, 추천 코너 하나가 고장났다고 공원 전체를 닫지는 않는 이야기로 풀어봤어요.",
            "Graceful degradation, told as a story about not closing the whole park just because one recommendation corner breaks."),
    "panels": [
        {"svg": P1, "alt": ("추천 코너가 고장나 정문이 닫히고, 손님들이 줄을 서다 돌아감", "The recommendation corner breaks, the entrance closes, and guests in line turn back"),
         "caption": ("추천 코너가 고장나자 공원 전체 입장을 막아버렸어요.", "One broken recommendation corner, and the whole park stopped letting guests in."),
         "small": ("손님들이 그냥 다 돌아가 버려요.", "The guests just turn around and leave.")},
        {"svg": P2, "alt": ("작은 고장 하나가 화살표를 따라 '공원 전체 폐쇄' 공지로 이어지고, 공원장이 손해를 걱정함", "A small break leads by arrow to a park-closed notice, and the manager worries about the loss"),
         "caption": ("작은 문제 하나가 전체를 멈추게 설계되어 있으면, 손해가 커져요.", "When a small problem is wired to stop everything, the cost is huge."),
         "small": ("손님이 다 돌아가서 손해가 커져요.", "Losing guests costs a lot.")},
        {"svg": P3, "hero": True, "alt": ("입장·안전 기구는 계속 돌고, 추천 코너만 잠시 쉰다는 안내판이 있음", "The entry-and-safety ride keeps running while the recommendation corner rests, per a posted sign"),
         "caption": ("덜 중요한 건 잠깐 꺼두고, 중요한 기구는 계속 돌려요.", "Turn off what matters less, keep the core rides running."),
         "small": ("조금 불편해도, 공원은 열려 있어요.", "A little less convenient, but the park stays open."),
         "tricks": (4, [
             (CORE_I, ("뭐가 핵심인지 정해요", "Decide what's core"), ("미리 정해둬요", "decide it ahead of time"), "calm"),
             (OFF_I, ("덜 중요한 건 꺼도 되게", "Let the rest be switched off"), ("설계해 둬요", "design it in"), "warm"),
             (NOTIFY_I, ("꺼진 건 살짝 알려요", "Quietly let guests know"), ("'잠시 쉬어요' 하고요", "'resting for now'")),
             (KEEP_I, ("핵심만은 끝까지 지켜요", "Protect the core to the end"), ("입장·안전은 안 꺼요", "entry and safety never go dark")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 문제 하나로 전부 닫힌 빨간 공원. 오른쪽: 핵심만 켜두고 나머지는 잠시 쉬게 한 초록 공원", "Left: a red park entirely shut by one problem. Right: a green park that keeps the core on and only rests the extras"),
         "caption": ("두 공원을 비교해 봐요.", "Compare the two parks."),
         "small": ("핵심만 켜두면, 공원은 계속 열려 있어요.", "Keep the core on, and the park stays open.")},
        {"svg": P5, "alt": ("요원이 식은땀을 흘리며 뭐부터 꺼야 할지 몰라 당황하고, 기구마다 물음표가 붙어 있음", "A sweating operator panics over what to turn off first, with a question mark over every ride"),
         "caption": ("뭐가 핵심인지 미리 안 정해두면, 급할 때는 못 골라요.", "Without deciding what's core beforehand, you can't choose it in a hurry."),
         "small": ("평소에 미리 정해둬야 해요.", "You have to decide it ahead of time, not in the moment.")},
    ],
    "summary": (("<b>우아한 저하</b> = 뭐가 <b>핵심</b>인지 미리 정해두고, 급하면 <b>덜 중요한 건 꺼두되</b> <b>핵심만은 끝까지 지켜서</b>, 일부만 고장나도 나머지는 그대로 돌아가게 하는 일.",
                 "<b>Graceful degradation</b> = deciding in advance what's <b>core</b>, so that when trouble hits you can <b>switch off the extras</b> while <b>protecting the core to the end</b> — letting the rest keep running when only part breaks."),
                ("한 부분이 실패해도 시스템 전체가 멈추지 않고, 덜 중요한 기능을 내리거나 간단한 폴백 응답으로 대체해 핵심 기능만은 계속 동작하게 하는 설계 원칙이에요. 벌크헤드나 서킷 브레이커 같은 장치와 함께 쓰여요.",
                 "A design principle where a failure in one part doesn't stop the whole system — non-essential features get disabled or swapped for a simple fallback, so the core keeps working. Often paired with mechanisms like bulkheads and circuit breakers.")),
    "glossary": [
        ("우아한 저하", "Graceful degradation", ("일부만 고장나도 나머지는 그대로 돌아가는 것.", "Letting the rest keep running when only part breaks."), ("전부 멈추는 대신 조금만 불편하게 만들어요.", "Instead of stopping everything, it makes things only a little less convenient.")),
        ("핵심 vs 부가 기능", "Core vs. non-core features", ("꼭 있어야 하는 것과 없어도 되는 것.", "What must exist, and what can be skipped."), ("평소에 미리 나눠둬야 급할 때 고를 수 있어요.", "You have to sort this out ahead of time, or you can't choose it in a hurry.")),
        ("폴백 응답", "Fallback response", ("진짜 대신 내놓는 간단한 답.", "A simple stand-in answer instead of the real one."), ("추천 대신 '인기 상품' 같은 기본값을 보여줘요.", "Shows a default like \"popular picks\" instead of a real recommendation.")),
        ("기능 끄기", "Feature toggle / kill switch", ("한 기능만 콕 집어 꺼두는 스위치.", "A switch that turns off just one feature."), ("코드를 다시 배포하지 않고도 끌 수 있어요.", "It can be switched off without redeploying any code.")),
        ("부분 장애", "Partial outage", ("전체가 아니라 일부만 멈춘 상태.", "A state where only part of things stop, not everything."), ("우아한 저하가 지키려는 바로 그 상태예요.", "This is exactly the state graceful degradation aims to protect.")),
        ("벌크헤드", "Bulkhead", ("고장을 한 구역 안에 가둬두는 칸막이.", "A partition that locks trouble inside one section."), ("배의 격벽처럼, 한 곳에 물이 차도 배 전체가 안 가라앉아요.", "Like a ship's bulkhead — one flooded compartment doesn't sink the whole ship.")),
        ("서킷 브레이커", "Circuit breaker", ("계속 실패하는 곳을 아예 끊어버리는 장치.", "A device that cuts off something that keeps failing."), ("끊어두면 그 실패가 다른 곳까지 안 번져요.", "Cutting it off keeps the failure from spreading further.")),
        ("SLO", "SLO (Service Level Objective)", ("핵심 기능이 지켜야 하는 약속 목표.", "The promise-target the core features must meet."), ('공원 전체가 지키는 약속과 같은 개념이에요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Same idea as the promise the whole park keeps. → <a href="reliability-en.html">the people who keep the park open</a>')),
    ],
}
