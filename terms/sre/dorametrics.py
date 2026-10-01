from _draw import *
from _world import *

# 1. "우리 공사팀 잘하고 있는 거 맞아요?" — "열심히 하는 것 같은데요"
P1 = svg(300, sky(300)
         + ride(110, 230, 0.65, color="var(--accent)") + person(280, 193, s=0.55, face=EYES, extra=WRENCH, **MECHANIC)
         + person(540, 193, s=0.55, face=EYES, **MANAGER)
         + bubble(440, 100, 260, 46, "⟦우리 공사팀, 잘하고 있는 거 맞아요?|is our crew doing okay or not?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble(140, 100, 220, 46, "⟦음... 열심히 하는 것 같은데요|hmm... seems like they're trying hard?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦공원장이 물으면, 느낌으로만 답해요|the manager asks, and the answer is just a feeling⟧", 12, "var(--ink)"))

# 2. 왜: 느낌으로는 좋아지는지 나빠지는지 비교가 안 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(40, 40, 260, 110, "⟦지난달|LAST MONTH⟧", ("⟦'꽤 잘했어요'|'did pretty well'⟧",), 1.0)
         + board(460, 40, 260, 110, "⟦이번 달|THIS MONTH⟧", ("⟦'그럭저럭요'|'so-so, I guess'⟧",), 1.0)
         + label(380, 170, "⟦그래서... 좋아진 거예요, 나빠진 거예요?|so... did we get better, or worse?⟧", 13, "var(--bad)", cls="d")
         + person(380, 199, s=0.5, face=SWEAT, **OPERATOR)
         + label(380, 282, "⟦느낌으로만 말하면 지난달과 비교가 안 돼요|a feeling alone can't be compared month to month⟧", 12, "var(--ink)"))

# 3. hero: 공사팀 실력을 숫자 네 가지로 재요
P3 = svg(360, sky(360)
         + board(30, 40, 310, 260, "⟦공사팀 성적표|CREW REPORT CARD⟧",
                 ("⟦① 공사 빈도|① how often⟧", "⟦② 준비~완료 걸린 시간|② prep-to-done time⟧",
                  "⟦③ 잘못될 확률|③ chance it breaks⟧", "⟦④ 고치는 시간|④ time to fix⟧"), 1.0)
         + person(470, 235, s=0.7, face=SMILE, extra=WRENCH, **MECHANIC) + ride(610, 300, 0.8, color="#5B8DEF")
         + label(380, 40, "⟦공사팀 실력을 느낌이 아니라 숫자 네 가지로 재요|measure the crew not by feeling, but by four numbers⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦얼마나 자주, 얼마나 빨리, 얼마나 안전하게, 얼마나 빨리 고치는지예요|how often, how fast, how safely, how fast to fix⟧", 12, "var(--muted)"))

# 4. board 성적표: 네 지표 작년 vs 올해
P4 = svg(340, sky(340)
         + board(40, 30, 680, 265, "⟦작년 vs 올해|LAST YEAR vs THIS YEAR⟧",
                 ("⟦공사 빈도: 한 달 2번 → 매주 1번  ✓|frequency: 2/month -> 1/week  ✓⟧",
                  "⟦준비~완료: 열흘 → 이틀  ✓|lead time: 10 days -> 2 days  ✓⟧",
                  "⟦잘못될 확률: 30% → 12%  ✓|failure rate: 30% -> 12%  ✓⟧",
                  "⟦고치는 시간: 하루 → 두 시간  ✓|recovery time: 1 day -> 2 hours  ✓⟧"), 1.0)
         + label(380, 320, "⟦네 가지 모두 작년보다 좋아졌어요|all four got better than last year⟧", 12, "var(--good)", cls="d"))

# 5. 깨지는 곳: 하나만 보면 안 돼요 — 네 가지를 같이 봐야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ride(170, 230, 0.6, color="var(--accent)") + queueline(90, 204, 3, 0.4, 24)
         + label(190, 255, "⟦빈도만 보면 — 자주는 하는데...|frequency alone — it's done often, but...⟧", 11, "var(--bad)")
         + board(440, 40, 280, 110, "⟦네 가지 같이 보기|ALL FOUR TOGETHER⟧",
                 ("⟦자주 + 안전 + 빠른 복구|often + safe + fast recovery⟧",), 1.0)
         + person(640, 185, s=0.5, face=SMILE, **OPERATOR)
         + label(640, 255, "⟦이래야 진짜 잘하는 팀|that's a truly good crew⟧", 11, "var(--good)", cls="d")
         + label(380, 282, "⟦넷 중 하나만 보면 안 돼요 — 자주만 하고 실패율은 무시하면 안 돼요|watching just one isn't enough — frequent but careless isn't good either⟧", 12, "var(--ink)"))

FREQ_I = icon('<rect x="10" y="40" width="10" height="14" fill="var(--accent)"/><rect x="24" y="30" width="10" height="24" fill="var(--accent)"/><rect x="38" y="18" width="10" height="36" fill="var(--accent)"/><rect x="52" y="10" width="6" height="44" fill="var(--accent)"/>')
LEAD_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M32 18 V32 L44 40" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
FAIL_I = icon('<path d="M32 10 L54 54 H10 Z" fill="var(--bad)"/><rect x="29" y="24" width="6" height="14" fill="var(--panel)"/><circle cx="32" cy="44" r="3.5" fill="var(--panel)"/>')
MTTR_I = icon('<path d="M44 32 a12 12 0 1 1 -4 -9" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 12 l6 10 -12 2z" fill="var(--accent)"/><rect x="26" y="38" width="12" height="12" rx="2" fill="var(--good)"/>')

PAGE = {
    "slug": "dorametrics", "order": 47,
    "title": ("우리 공사팀 네 가지 성적표", "Our Crew's Four-Number Report Card"),
    "h1": ("<em>DORA 지표</em>가 뭐예요?", "What are <em>DORA Metrics</em>?"),
    "sub": ("DORA 지표를 느낌 대신 숫자 네 가지로 공사팀 실력을 재는 성적표 이야기로 풀어봤어요.",
            "DORA metrics, told as a story about a report card that measures a crew by four numbers instead of a feeling."),
    "panels": [
        {"svg": P1, "alt": ("공원장이 공사팀이 잘하고 있는지 묻고, 정비사 쪽 사람은 '열심히 하는 것 같다'는 느낌으로만 답함", "The manager asks if the crew is doing well, and the answer is just a feeling — 'seems like they're trying hard'"),
         "caption": ("\"우리 공사팀, 잘하고 있는 거 맞아요?\" \"열심히 하는 것 같은데요.\"", "\"Is our crew doing okay?\" \"Seems like they're trying hard.\""),
         "small": ("느낌으로만 답하면 정말 잘하고 있는지 알 수 없어요.", "Answering with just a feeling doesn't tell you if they're really doing well.")},
        {"svg": P2, "alt": ("지난달 '꽤 잘했다'는 안내판과 이번 달 '그럭저럭'이라는 안내판, 관제실 요원이 비교하지 못해 당황함", "A board says 'did pretty well' last month and 'so-so' this month, and an operator can't compare them"),
         "caption": ("느낌으로만 말하면 좋아진 건지 나빠진 건지 비교가 안 돼요.", "Feelings alone can't tell you whether things got better or worse."),
         "small": ("지난달과 이번 달을 나란히 놓고 봐야 알 수 있어요.", "You need to line them up side by side to really know.")},
        {"svg": P3, "hero": True, "alt": ("공사팀 성적표 안내판에 네 가지 항목 — 빈도, 준비~완료 시간, 잘못될 확률, 고치는 시간", "A crew report-card board with four items — frequency, lead time, failure chance, recovery time"),
         "caption": ("공사팀의 실력을 숫자 네 가지로 재요.", "Measure the crew's skill with four numbers."),
         "small": ("얼마나 자주, 얼마나 빨리, 얼마나 안전하게, 얼마나 빨리 고치는지예요.", "How often, how fast, how safely, and how fast to fix."),
         "tricks": (4, [
             (FREQ_I, ("자주 조금씩 공사해요", "Build often, in small bits"), ("빈도를 높여요", "raise the frequency"), "calm"),
             (LEAD_I, ("준비를 빠르게 해요", "Get ready faster"), ("리드 타임을 줄여요", "shorten the lead time")),
             (FAIL_I, ("실수를 줄여요", "Make fewer mistakes"), ("실패율을 낮춰요", "lower the failure rate"), "warm"),
             (MTTR_I, ("실수해도 빨리 고쳐요", "Fix mistakes fast"), ("복구 시간을 줄여요", "shorten the recovery time")),
         ])},
        {"svg": P4, "alt": ("작년과 올해를 비교하는 성적표 — 공사 빈도, 준비~완료 시간, 잘못될 확률, 고치는 시간 네 가지 모두 좋아짐", "A report card comparing last year to this year — frequency, lead time, failure rate, and recovery time all improved"),
         "caption": ("네 지표 모두 작년보다 올해가 좋아졌어요.", "All four numbers are better this year than last year."),
         "small": ("자주 하고, 빨리 준비하고, 덜 실패하고, 빨리 고쳐요.", "More often, faster to prepare, fewer failures, faster to fix.")},
        {"svg": P5, "alt": ("왼쪽: 공사는 자주 하지만 다른 지표는 모른 채 놔둠. 오른쪽: 네 가지를 같이 보는 안내판", "Left: building often but ignoring the other numbers. Right: a board showing all four together"),
         "caption": ("넷 중 하나만 보면 안 돼요 — 네 가지를 같이 봐야 진짜 잘하는 팀이에요.", "Watching just one isn't enough — all four together show a truly good crew."),
         "small": ("자주 공사하면서 실패율은 무시하면, 자주 사고 내는 팀일 뿐이에요.", "Build often while ignoring the failure rate, and you just have a crew that breaks things often.")},
    ],
    "summary": (("<b>DORA 지표</b> = <b>공사 빈도·준비 시간·실패율·복구 시간</b> 네 가지 숫자로, 느낌이 아니라 <b>실제로</b> 공사팀이 잘하고 있는지 재는 성적표.",
                 "<b>DORA metrics</b> = a report card of four numbers — <b>deployment frequency, lead time, failure rate, recovery time</b> — that measure a crew's real performance instead of a feeling."),
                ("DORA(DevOps Research and Assessment)가 정리한 네 가지 소프트웨어 배포 성과 지표예요: 배포 빈도(Deployment Frequency), 변경 리드 타임(Lead Time for Changes), 변경 실패율(Change Failure Rate), 서비스 복구 시간(Time to Restore Service). 네 가지를 같이 봐야 '엘리트(Elite)'부터 '낮음(Low)'까지의 등급을 가늠할 수 있어요.",
                 "Four software delivery performance metrics defined by DORA (DevOps Research and Assessment): Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Time to Restore Service. Looking at all four together is what lets you place a team on a scale from 'Elite' down to 'Low'.")),
    "glossary": [
        ("DORA 지표", "DORA metrics", ("공사팀 실력을 재는 숫자 네 가지.", "The four numbers that measure a crew's skill."), ('공원을 돌보는 일 전체 중 한 조각이에요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'One piece of the whole job of keeping the park running. → <a href="reliability-en.html">the people who keep an amusement park open</a>')),
        ("배포 빈도", "Deployment frequency", ("공사를 얼마나 자주 하는지.", "How often the crew builds."), ("한 달에 두 번보다 매주 한 번이 더 좋은 신호예요.", "Once a week is a better sign than twice a month.")),
        ("변경 리드 타임", "Lead time for changes", ("공사 준비부터 완료까지 걸리는 시간.", "The time from starting the prep to finishing the build."), ("짧을수록 빨리 손님에게 선보일 수 있어요.", "Shorter means guests see the new ride sooner.")),
        ("변경 실패율", "Change failure rate", ("공사가 잘못될 확률.", "The chance a build goes wrong."), ("낮을수록 공사팀이 안전하게 일한다는 뜻이에요.", "Lower means the crew is working safely.")),
        ("서비스 복구 시간(MTTR)", "Time to restore service (MTTR)", ("잘못됐을 때 얼마나 빨리 고치는지.", "How fast things get fixed when they go wrong."), ("실수를 아예 안 할 순 없어도, 빨리 고치면 괜찮아요.", "You can't avoid every mistake, but fixing it fast is what counts.")),
        ("등급(엘리트/높음/보통)", "Performance tiers (Elite/High/Medium/Low)", ("네 지표를 종합해 매기는 이름.", "A label given by combining all four numbers."), ("이름만 알아둬도 충분해요 — 세부 기준은 상황마다 달라요.", "Just knowing the names is enough — exact thresholds vary by context.")),
        ("롤백 · 사후 분석과의 관계", "Relation to rollback and postmortems", ("복구 시간은 롤백으로, 실패율은 사후 분석으로 줄여요.", "Rollback shortens recovery time; postmortems lower the failure rate."), ("이상하면 바로 어제 버전으로 되돌리고, 끝나면 탓하지 않고 기록해요.", "If something's wrong, switch back to yesterday's version, then write it down without blame.")),
        ("용량 계획과의 관계", "Relation to capacity planning", ("네 지표가 좋아져도 손님이 몰리는 날엔 또 다른 준비가 필요해요.", "Even with great numbers, a day of crowds still needs its own kind of preparing."), ('작년 기록과 올해 행사를 미리 세어보는 일이에요. → <a href="capacityplanning-ko.html">내년 손님 수를 미리 세어보기</a>', 'That means counting last year\'s numbers and this year\'s events in advance. → <a href="capacityplanning-en.html">counting next year\'s guests in advance</a>')),
    ],
}
