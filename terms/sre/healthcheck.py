from _draw import *
from _world import *

# 1. 기구는 멈췄는데 안내판엔 '운행 중'
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(560, 230, 0.9, color="var(--stone)") + label(560, 108, "⟦운행 중|RUNNING⟧", 11, "var(--good)", cls="d")
         + queueline(60, 174, 4, 0.5, 30) + person(240, 160, s=0.6, face=FROWN, hat=None, shirt="#4A5A72")
         + bubble(120, 80, 200, 46, "⟦어? 안 움직이는데?|huh, it's not moving?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦기구가 멈췄는데 안내판엔 '운행 중'이라고 떠 있어요|the ride is stalled, but the sign still says 'running'⟧", 12, "var(--ink)"))

# 2. 왜: 멀리서 보면 멀쩡해 보여도 속은 멈춰 있을 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + controlroom(430, 40, 220, 110, bars=((0.6, "var(--good)"), (0.5, "var(--good)"), (0.55, "var(--good)"), (0.6, "var(--good)")))
         + person(500, 174, s=0.6, face=SMILE, **OPERATOR) + bubble(540, 160, 190, 44, "⟦다 괜찮아 보이는데?|all looks fine to me?⟧", 10, "var(--panel)", "var(--line)", "left")
         + ride(170, 230, 0.75, color="var(--stone)", closed=True) + queueline(40, 206, 2, 0.4, 26)
         + label(380, 282, "⟦멀리서 보면 멀쩡해 보여도, 속은 멈춰 있을 수 있어요|from a distance it looks fine, but inside it may have already stopped⟧", 12, "var(--ink)"))

# 3. hero: 몇 초마다 '딸깍, 저 괜찮아요?' 물어보고, 대답 없으면 빼요
P3 = svg(340, sky(340)
         + ride(130, 270, 0.75, color="var(--accent)") + label(130, 150, "⟦✓|OK⟧", 20, "var(--good)", cls="d")
         + ride(320, 270, 0.75, color="#5B8DEF") + label(320, 150, "⟦✓|OK⟧", 20, "var(--good)", cls="d")
         + ride(520, 270, 0.75, color="var(--stone)", closed=True) + label(520, 150, "⟦×|X⟧", 20, "var(--bad)", cls="d")
         + label(520, 120, "⟦대답 없음 → 명단에서 제외|no answer → removed from the list⟧", 10, "var(--bad)")
         + person(650, 220, s=0.65, face=EYES, **OPERATOR) + walkie(700, 200, 0.8)
         + label(380, 40, "⟦몇 초에 한 번씩 '딸깍, 저 괜찮아요?' 하고 물어보고, 대답 없으면 빼요|every few seconds, ask each ride 'click — are you okay?' — no answer, and it's pulled from the list⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦다시 괜찮아지면 명단에 자동으로 돌아와요|get well again, and it comes back on the list on its own⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 두 가지로 물어봐요 — 살아는 있어? 준비는 됐어?
P4 = svg(320, sky(320)
         + board(60, 30, 260, 150, "⟦기구 상태표|STATUS BOARD⟧",
                 ("⟦1번: 살아있음 ✓ 준비됨 ✓|No.1: alive ✓ ready ✓⟧",
                  "⟦2번: 살아있음 ✓ 준비안됨 ✗|No.2: alive ✓ not ready ✗⟧",
                  "⟦3번: 무응답 → 제외|No.3: no answer → removed⟧"), 1.0)
         + ride(520, 220, 0.6, color="var(--accent)") + ride(620, 220, 0.6, color="#5B8DEF")
         + label(380, 285, "⟦두 가지로 물어봐요 — 살아는 있어? 손님 받을 준비 됐어?|two different questions — are you alive? are you ready for guests?⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 확인 자체가 너무 잦으면 부담이 돼요
P5 = svg(300, sky(300)
         + controlroom(280, 40, 200, 100, bars=((0.9, "var(--bad)"), (0.85, "var(--bad)"), (0.95, "var(--bad)"), (0.9, "var(--bad)")))
         + person(300, 174, s=0.6, face=SWEAT, **OPERATOR)
         + bubble(360, 160, 230, 50, "⟦이렇게 자주 물으면 저희도 힘들어요|asking this often wears us out too⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 282, "⟦확인 자체가 너무 잦으면, 그것도 부담이 돼요 — 적당한 간격이 필요해요|checking too often becomes its own burden — you need the right interval⟧", 12, "var(--ink)"))

PING_I = icon('<circle cx="32" cy="32" r="6" fill="var(--accent)"/><path d="M32 32 m-16 0 a16 16 0 0 1 32 0" stroke="var(--accent)" stroke-width="3" fill="none" opacity="0.6"/><path d="M32 32 m-24 0 a24 24 0 0 1 48 0" stroke="var(--accent)" stroke-width="3" fill="none" opacity="0.3"/>')
REMOVE_I = icon('<rect x="10" y="22" width="44" height="20" rx="4" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><path d="M24 26 l16 12 M40 26 l-16 12" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
TWOQ_I = icon('<circle cx="22" cy="30" r="14" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M17 30 l4 4 8 -8" stroke="var(--good)" stroke-width="3" fill="none"/><circle cx="46" cy="30" r="10" fill="var(--accent)"/><text x="46" y="35" text-anchor="middle" font-size="14" font-weight="700" fill="var(--panel)">?</text>')
RETURN_I = icon('<path d="M44 20 a16 16 0 1 0 2 18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M44 10 l4 12 -13 -3z" fill="var(--good)"/>')

PAGE = {
    "slug": "healthcheck", "order": 20,
    "title": ("안전바 딸깍 확인", "The Click-Check on the Safety Bar"),
    "h1": ("<em>헬스 체크</em>가 뭐예요?", "What is a <em>Health Check</em>?"),
    "sub": ("헬스 체크를 기구마다 '저 괜찮아요?' 하고 몇 초마다 물어보는 이야기로 풀어봤어요.",
            "A health check, told as a story about asking every ride 'are you okay?' every few seconds."),
    "panels": [
        {"svg": P1, "alt": ("기구가 멈춰 있는데 안내판엔 '운행 중'이라고 떠 있고, 손님이 줄섰다가 안 움직이는 걸 보고 놀람", "A ride has stalled but its sign still says 'running'; a guest waits in line and is surprised it's not moving"),
         "caption": ("기구가 멈췄는데 안내판엔 '운행 중'이라고 떠 있어요.", "The ride is stalled, but the sign still says 'running.'"),
         "small": ("손님은 줄섰다가 허탕 쳐요.", "Guests wait in line only to find out it's not running.")},
        {"svg": P2, "alt": ("관제실 화면은 전부 초록인데, 실제로는 멀리 있는 기구 하나가 멈춰 있음", "The control-room screen shows all green, while a ride off in the distance has actually stopped"),
         "caption": ("멀리서 보면 멀쩡해 보여도, 속은 멈춰 있을 수 있어요.", "From a distance it looks fine, but inside it may have already stopped."),
         "small": ("화면만 보고는 속을 알 수 없어요.", "Looking at the screen alone can't tell you what's inside.")},
        {"svg": P3, "hero": True, "alt": ("기구 두 개는 '괜찮아요' 표시가 뜨고, 한 개는 대답이 없어 명단에서 빠짐", "Two rides show an 'okay' checkmark while one gets no answer and is removed from the list"),
         "caption": ("몇 초에 한 번씩 '딸깍, 저 괜찮아요?' 하고 물어보고, 대답 없으면 빼요.", "Every few seconds, ask each ride 'click — are you okay?' — no answer, and it's pulled from the list."),
         "small": ("다시 괜찮아지면 명단에 자동으로 돌아와요.", "Get well again, and it comes back on the list on its own."),
         "tricks": (4, [
             (PING_I, ("주기적으로 물어봐요", "Ask it, again and again"), ("몇 초에 한 번씩요", "every few seconds"), "calm"),
             (REMOVE_I, ("대답 없으면 명단에서 빼요", "No answer? Off the list"), ("손님을 안 보내요", "so no guest gets sent there")),
             (TWOQ_I, ("두 가지로 물어봐요", "Ask two different things"), ("살아있나, 준비됐나", "alive? and ready?"), "warm"),
             (RETURN_I, ("괜찮아지면 자동 복귀", "Recovers? Back automatically"), ("사람이 안 건드려도 돼요", "no one has to do it by hand")),
         ])},
        {"svg": P4, "alt": ("기구 상태표에 1번은 살아있고 준비됨, 2번은 살아있지만 준비 안됨, 3번은 무응답이라 제외됐다고 적혀 있음", "A status board lists ride No.1 as alive and ready, No.2 as alive but not ready, and No.3 as removed for no answer"),
         "caption": ("두 가지로 물어봐요 — 살아는 있어? 손님 받을 준비 됐어?", "Two different questions — are you alive? are you ready for guests?"),
         "small": ("살아있어도 아직 준비가 안 됐을 수 있어요.", "A ride can be alive but still not ready yet.")},
        {"svg": P5, "alt": ("관제실 화면이 전부 빨갛게 바빠 보이고, 요원이 땀을 흘리며 너무 자주 물으면 힘들다고 말함", "The control-room screen is all red and overloaded, and a sweating operator says asking this often wears them out too"),
         "caption": ("확인 자체가 너무 잦으면, 그것도 부담이 돼요.", "Checking too often becomes its own burden."),
         "small": ("적당한 간격이 필요해요.", "You need to find the right interval.")},
    ],
    "summary": (("<b>헬스 체크</b> = 기구마다 몇 초에 한 번씩 '괜찮아요?' 하고 <b>물어보고</b>, <b>대답 없으면 명단에서 빼는</b> 일. 괜찮아지면 자동으로 돌아와요.",
                 "<b>A health check</b> = <b>asking</b> every ride 'are you okay?' every few seconds, and <b>pulling it from the list</b> when there's no answer — then letting it back in once it's well again."),
                ("일정 간격으로 서비스에 핑을 보내 살아있는지 확인하는 방법이에요. 살아있나(라이브니스)와 손님 받을 준비가 됐나(레디니스)는 서로 다른 질문이고, 결과는 로드 밸런서로 바로 전달돼 운행 명단을 갱신해요.",
                 "A method of pinging a service at regular intervals to see if it's still alive. Whether it's alive (liveness) and whether it's ready for traffic (readiness) are two different questions, and the result feeds straight into a load balancer, updating the list of who's in service.")),
    "glossary": [
        ("헬스 체크", "Health check", ("몇 초마다 '괜찮아요?' 물어보는 일.", "Asking 'are you okay?' every few seconds."), ("대답이 없으면 명단에서 빼요.", "No answer means it's pulled from the list.")),
        ("라이브니스", "Liveness", ("살아는 있나? 묻는 질문.", "The question 'are you alive at all?'"), ("이것만 통과해도 완전히 괜찮다는 뜻은 아니에요.", "Passing this alone doesn't mean everything's fine.")),
        ("레디니스", "Readiness", ("손님 받을 준비는 됐나? 묻는 질문.", "The question 'are you ready for guests?'"), ("살아있어도 아직 준비가 안 됐을 수 있어요.", "A ride can be alive but still not ready yet.")),
        ("핑/하트비트", "Ping / Heartbeat", ("딸깍 하고 보내는 짧은 신호.", "The short click-signal sent out."), ("이 신호에 대한 대답으로 상태를 판단해요.", "The reply to this signal is what tells you the status.")),
        ("자동 제외·복귀", "Automatic removal and return", ("대답 없으면 빠지고, 괜찮아지면 돌아오는 것.", "Dropping out on no answer, and returning once well again."), ("사람이 일일이 안 건드려도 돼요.", "No one has to manage this by hand.")),
        ("로드 밸런서 연동", "Load balancer integration", ("헬스 체크 결과를 바로 전해 받는 곳.", "Where the health-check result goes next."), ('괜찮은 기구에만 손님을 보내요. → <a href="loadbalancer-ko.html">여러 창구에 나눠 보내는 안내원</a>', 'It only sends guests to rides that passed. → <a href="loadbalancer-en.html">the usher who spreads guests across booths</a>')),
        ("장애 조치", "Failover", ("대답 없는 기구 대신 다른 걸 쓰는 것.", "Switching to another ride instead of one that's not answering."), ("헬스 체크가 먼저 알아채야 장애 조치도 시작돼요.", "A failover can only start once the health check has already noticed.")),
        ("서비스 디스커버리", "Service discovery", ("지금 어떤 기구가 열려 있는지 알려주는 안내판.", "The sign that shows which rides are currently open."), ("헬스 체크 결과로 이 안내판이 늘 최신으로 유지돼요.", "Health-check results are what keep this sign always up to date.")),
    ],
}
