from _draw import *
from _world import *

# 1. 작가와 편집장이 마감을 두고 부딪힘
P1 = svg(300, sky(300, ground=False)
         + person(260, 150, s=0.9, face=FROWN, **WRITER) + bubble(100, 70, 220, 44, "⟦일주일만 더 주세요|just one more week, please⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(500, 150, s=0.9, face=FROWN, **EDITOR) + bubble(430, 70, 230, 44, "⟦예정대로 내야 해요|it has to ship on schedule⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦마감을 두고 작가와 편집장이 부딪혀요|the author and editor clash over the deadline⟧", 13, "var(--ink)"))

# 2. 묻어두면 더 커짐
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 150, s=1.0, face=FROWN + SWEAT, **EDITOR)
         + label(380, 60, "⟦말 안 하고 넘어가면...|if nobody says anything...⟧", 13, "var(--bad)")
         + label(380, 260, "⟦작은 의견 차이가 쌓여서 더 큰 갈등이 돼요|a small disagreement piles up into a bigger conflict⟧", 12, "var(--ink)", cls="d"))

# 3. 상황에 맞는 해결 방식을 고름 (hero)
P3 = svg(340, sky(340)
         + person(260, 130, s=0.85, face=EYES, **EDITOR) + person(500, 130, s=0.85, face=SMILE, **WRITER)
         + bubble(312, 190, 150, 40, "⟦둘 다 좋은 수를 찾아봐요|let's find something that works for both⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 30, "⟦갈등관리 = 상황에 맞는 해결 방식을 고르는 기술|Conflict management = choosing the right resolution style for the moment⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦갈등을 없애는 게 아니라, 다루는 방법을 아는 것이 핵심이에요|the point isn't erasing conflict — it's knowing how to handle it⟧", 12, "var(--muted)"))

COLLAB_I = icon('<circle cx="22" cy="32" r="12" fill="var(--good)"/><circle cx="42" cy="32" r="12" fill="var(--accent)"/>')
COMPROMISE_I = icon('<rect x="14" y="28" width="36" height="8" rx="4" fill="var(--ink)"/><circle cx="18" cy="32" r="8" fill="var(--accent)"/><circle cx="46" cy="32" r="8" fill="var(--good)"/>')
SMOOTH_I = icon('<path d="M14 36 Q32 20 50 36" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
FORCE_I = icon('<path d="M20 14 L44 14 L32 50 Z" fill="var(--bad)"/>')

PAGE = {
    "slug": "conflictmgmt", "order": 35,
    "title": ("작가와 편집장이 다툴 때", "When Author and Editor Clash"),
    "h1": ("<em>프로젝트 갈등관리</em>가 뭐예요?", "What is <em>Project Conflict Management</em>?"),
    "sub": ("마감을 두고 부딪히는 작가와 편집장 사이에서, 상황에 맞는 방식으로 풀어가는 이야기예요.",
            "A story about the author and editor clashing over a deadline — and choosing the right way to work it out."),
    "panels": [
        {"svg": P1, "alt": ("작가는 일주일만 더 달라 하고, 편집장은 예정대로 내야 한다고 맞섬", "The author asks for one more week; the editor insists it ships on schedule"),
         "caption": ("마감을 두고 작가와 편집장이 부딪혀요.", "The author and editor clash over the deadline."),
         "small": ("서로 원하는 게 다르면 부딪힐 수밖에 없어요.", "When two people want different things, friction is bound to happen.")},
        {"svg": P2, "alt": ("편집장이 땀을 흘리며 혼자 속앓이함 — 말 안 하고 넘어가면 갈등이 더 커짐", "The editor sweats, stewing alone — leaving it unsaid only makes the conflict grow"),
         "caption": ("묻어두면 더 커져요.", "Left unaddressed, it only grows."),
         "small": ("작은 의견 차이가 쌓여서 더 큰 갈등이 돼요.", "A small disagreement piles up into a bigger conflict.")},
        {"svg": P3, "hero": True, "alt": ("편집장과 작가가 마주 앉아 둘 다 좋은 수를 찾아보자고 대화함", "The editor and author sit down together, looking for something that works for both"),
         "caption": ("갈등관리 = 상황에 맞는 해결 방식을 고르는 기술이에요.", "Conflict management = choosing the right resolution style for the moment."),
         "small": ("갈등을 없애는 게 아니라, 다루는 방법을 아는 것이 핵심이에요.", "The point isn't erasing conflict — it's knowing how to handle it."),
         "tricks": (4, [
             (COLLAB_I, ("협력", "Collaborate"), ("같이 풀어서 둘 다 만족", "solve it together, both satisfied"), "calm"),
             (COMPROMISE_I, ("타협", "Compromise"), ("서로 조금씩 양보해요", "each side gives a little")),
             (SMOOTH_I, ("수용/완화", "Smooth / Accommodate"), ("급하지 않으면 한쪽이 맞춰줘요", "when it's not urgent, one side yields"), "warm"),
             (FORCE_I, ("강압", "Force"), ("급할 때 결정권으로 밀어붙여요", "when urgent, decide and push through")),
         ])},
        {"svg": svg(320, sky(320)
                     + styleguide(60, 40, 640, 250, "⟦갈등 해결 방식 다섯 가지|FIVE WAYS TO RESOLVE CONFLICT⟧",
                                  ("⟦협력 — 같이 풀어서 둘 다 이득|collaborate — solve together, both win⟧",
                                   "⟦타협 — 반반 양보|compromise — split the difference⟧",
                                   "⟦수용 — 급하지 않으면 맞춰주기|accommodate — yield when it's not urgent⟧",
                                   "⟦강압 — 급할 때 결정권으로 밀기|force — push through when urgent⟧",
                                   "⟦회피 — 일단 미뤄두기(너무 자주 쓰면 안 돼요)|withdraw — postpone it (don't overuse this one)⟧"), 1.0, hl=4)),
         "alt": ("갈등 해결 다섯 가지 방식을 나열한 점검표: 협력, 타협, 수용, 강압, 회피", "A checklist of five conflict-resolution styles: collaborate, compromise, accommodate, force, withdraw"),
         "caption": ("실제로는 다섯 가지 방식이 있어요.", "In practice there are five styles."),
         "small": ("회피(미루기)도 쓸 수 있지만, 너무 자주 쓰면 갈등만 쌓여요.", "Withdrawing is an option too, but overusing it just lets conflict pile up.")},
        {"svg": svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
                     + person(190, 130, s=0.8, face=FROWN, **EDITOR) + label(190, 260, "⟦억누르면 터져요|suppress it, it blows up⟧", 11, "var(--ink)")
                     + person(570, 130, s=0.8, face=SMILE, **WRITER) + label(570, 260, "⟦다루면 더 나은 합의가 나와요|handle it, and a better agreement comes out⟧", 11, "var(--ink)")
                     + label(380, 305, "⟦갈등관리는 갈등을 없애는 기술이 아니라 다루는 기술이에요|conflict management isn't the skill of erasing conflict — it's the skill of handling it⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 갈등을 억누르면 결국 터짐. 오른쪽: 갈등을 다루면 더 나은 합의가 나옴", "Left: suppressing conflict makes it blow up later. Right: handling it leads to a better agreement"),
         "caption": ("갈등관리는 갈등을 없애주지 않아요.", "Conflict management doesn't make conflict disappear."),
         "small": ("없애는 기술이 아니라 다루는 기술이에요.", "It's not the skill of erasing it — it's the skill of handling it.")},
    ],
    "summary": (("<b>프로젝트 갈등관리</b> = 이해관계자 사이의 의견 차이를, <b>상황에 맞는 방식</b>(협력·타협·수용·강압·회피)으로 다뤄 더 나은 결과로 이끄는 기술.",
                 "<b>Project conflict management</b> = handling disagreements among stakeholders using the <b>style that fits the moment</b> (collaborate, compromise, accommodate, force, withdraw) to reach a better outcome."),
                ("PMBOK에서는 갈등 해결 기법을 협력(Collaborate/Problem Solve), 타협(Compromise), 수용(Smooth/Accommodate), 강압(Force/Direct), 회피(Withdraw/Avoid) 다섯 가지로 구분해요. 어느 하나가 항상 옳은 게 아니라, 갈등의 긴급성과 중요도에 따라 골라 써야 해요.",
                 "PMBOK groups conflict-resolution techniques into five: Collaborate/Problem Solve, Compromise, Smooth/Accommodate, Force/Direct, and Withdraw/Avoid. None is always correct — the right one depends on the conflict's urgency and importance.")),
    "glossary": [
        ("갈등관리", "Conflict Management", ("의견 차이를 다루는 기술.", "The skill of handling disagreement."), ("없애는 게 아니라 다루는 것이에요.", "Not erasing conflict — handling it.")),
        ("협력(Collaborate)", "Collaborate", ("같이 풀어서 둘 다 만족.", "Solving it together so both sides win."), ("가장 시간이 걸리지만 결과가 좋아요.", "Takes the most time, but gives the best result.")),
        ("타협(Compromise)", "Compromise", ("서로 조금씩 양보.", "Each side gives a little."), ("빠르지만 완전히 만족스럽진 않아요.", "Quick, but not fully satisfying for either side.")),
        ("수용(Accommodate)", "Accommodate", ("급하지 않으면 한쪽이 맞춰줌.", "One side yields when it isn't urgent."), ("관계를 지키는 데 유리해요.", "Good for preserving the relationship.")),
        ("강압(Force)", "Force", ("결정권으로 밀어붙임.", "Pushing through using authority."), ("급할 땐 빠르지만 관계가 상할 수 있어요.", "Fast when urgent, but can hurt the relationship.")),
        ("회피(Withdraw)", "Withdraw", ("일단 미뤄두는 것.", "Postponing it for now."), ("너무 자주 쓰면 갈등이 쌓여요.", "Overused, it just lets conflict pile up.")),
        ("이해관계자 관리", "Stakeholder Management", ("갈등의 당사자들을 미리 파악하는 일.", "Identifying the people involved before conflict even starts."), ("갈등관리보다 한 단계 앞선 준비예요.", "A step of preparation that comes before conflict management.")),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("여러 책 사이의 갈등도 함께 조율.", "Also helps coordinate conflicts across several books."), ('더 큰 범위에서 조정을 돕기도 해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Sometimes helps mediate at a wider scope. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
