from _draw import *
from _world import *

# 1. 계기판엔 "에러 늘었다"만 보이고, 왜 늘었는지는 전혀 몰라요
P1 = svg(300, sky(300, ground=False)
         + gauge(380, 140, 1.6, level=0.85, label_text="⟦에러↑|errors up⟧", color="var(--bad)")
         + person(560, 170, s=0.7, face=FROWN + SWEAT, **OPERATOR)
         + bubble(540, 60, 210, 54, "⟦에러가 늘었다는 건 아는데... 왜지?|I can see errors went up... but why?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦계기판엔 \'에러 늘었다\'만 보이고, 왜 늘었는지는 전혀 몰라요|the gauge just shows errors went up — it has no idea why⟧", 12, "var(--ink)"))

# 2. 왜: 숫자 하나만으론 "뭐가 문제인지" 못 찾아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + gauge(380, 130, 1.8, level=0.9, label_text="⟦에러율 90%|error rate 90%⟧", color="var(--bad)")
         + person(180, 175, s=0.65, face=FROWN + SWEAT, **MECHANIC)
         + bubble(40, 90, 220, 54, "⟦이것만 봐선 어디가 문제인지 모르겠어요|this alone doesn\'t tell me where the problem is⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦숫자 하나만으론 뭐가 문제인지 못 찾아요|a single number alone can\'t tell you what\'s actually wrong⟧", 12, "var(--bad)", cls="d"))

# 3. hero: 숫자·일지·지나간 길, 세 가지를 같이 봐요
METRIC_I = icon('<rect x="10" y="40" width="10" height="16" fill="var(--accent)"/><rect x="26" y="24" width="10" height="32" fill="var(--accent)"/><rect x="42" y="12" width="10" height="44" fill="var(--bad)"/>')
LOG_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M20 22 h24 M20 30 h24 M20 38 h16" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')
TRACE_I = icon('<circle cx="12" cy="44" r="6" fill="var(--good)"/><circle cx="32" cy="20" r="6" fill="var(--good)"/><circle cx="52" cy="44" r="6" fill="var(--bad)"/><path d="M12 44 L32 20 L52 44" stroke="var(--accent)" stroke-width="3" fill="none"/>')
DASH_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="var(--stone-dark)"/><rect x="12" y="16" width="20" height="16" fill="var(--accent)"/><rect x="34" y="16" width="18" height="16" fill="var(--good)"/><rect x="12" y="34" width="40" height="14" fill="var(--bad)"/>')

P3 = svg(360, sky(360)
         + controlroom(40, 60, 210, 140, bars=((0.4, "var(--accent)"), (0.6, "var(--good)"), (0.2, "var(--bad)"), (0.5, "var(--accent)")))
         + label(145, 215, "⟦지표|metrics⟧", 12, "var(--ink)")
         + controlroom(275, 60, 210, 140)
         + label(285, 90, "⟦10:01 OK|10:01 OK⟧", 10, "#8FD9A8", "start")
         + label(285, 112, "⟦10:02 OK|10:02 OK⟧", 10, "#8FD9A8", "start")
         + label(285, 134, "⟦10:03 ERROR: timeout|10:03 ERROR: timeout⟧", 10, "var(--bad)", "start")
         + label(285, 156, "⟦10:04 ERROR: timeout|10:04 ERROR: timeout⟧", 10, "var(--bad)", "start")
         + label(380, 215, "⟦로그|logs⟧", 12, "var(--ink)")
         + controlroom(510, 60, 210, 140)
         + '<path d="M530 130 L570 100 L610 140 L650 110 L690 130" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + '<circle cx="530" cy="130" r="5" fill="var(--good)"/><circle cx="570" cy="100" r="5" fill="var(--good)"/><circle cx="610" cy="140" r="5" fill="var(--bad)"/><circle cx="650" cy="110" r="5" fill="var(--good)"/><circle cx="690" cy="130" r="5" fill="var(--good)"/>'
         + label(615, 215, "⟦트레이스|trace⟧", 12, "var(--ink)")
         + label(380, 35, "⟦숫자·일지·지나간 길, 세 가지를 같이 봐요|watch three things together: the numbers, the written log, and the path a request took⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦숫자로 \'뭔가 이상해\'를 알고, 일지와 길로 \'어디가, 왜\'를 찾아요|the numbers tell you something\'s wrong; the log and the path tell you where and why⟧", 12, "var(--muted)"))

# 4. 작동: 지표로 알아채고, 로그로 찾고, 트레이스로 확인해요
P4 = svg(320, sky(320, ground=False)
         + controlroom(40, 50, 210, 140, bars=((0.4, "var(--accent)"), (0.6, "var(--good)"), (0.2, "var(--bad)"), (0.5, "var(--accent)")))
         + label(145, 205, "⟦지표|metrics⟧", 12, "var(--ink)")
         + '<path d="M250 120 H275" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + controlroom(275, 50, 210, 140)
         + label(285, 80, "⟦10:03 ERROR: timeout|10:03 ERROR: timeout⟧", 10, "var(--bad)", "start")
         + label(285, 102, "⟦10:03 ride=B|10:03 ride=B⟧", 10, "#8FD9A8", "start")
         + label(380, 205, "⟦로그|logs⟧", 12, "var(--ink)")
         + '<path d="M485 120 H510" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + controlroom(510, 50, 210, 140)
         + '<path d="M530 120 L570 90 L610 130 L650 100 L690 120" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + '<circle cx="530" cy="120" r="5" fill="var(--good)"/><circle cx="570" cy="90" r="5" fill="var(--good)"/><circle cx="610" cy="130" r="5" fill="var(--bad)"/><circle cx="650" cy="100" r="5" fill="var(--good)"/><circle cx="690" cy="120" r="5" fill="var(--good)"/>'
         + label(615, 205, "⟦트레이스|trace⟧", 12, "var(--ink)")
         + label(380, 300, "⟦지표로 알아채고, 로그로 찾고, 트레이스로 어느 기구인지 확인해요|notice it with metrics, find it with logs, confirm which ride it was with traces⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 셋 다 쌓아두기만 하면 그것도 비용이에요
P5 = svg(300, sky(300, ground=False)
         + board(260, 40, 240, 160, "⟦보관 창고|STORAGE⟧", ("⟦지표·로그·트레이스 전부|metrics, logs, traces — all of it⟧", "⟦영원히 쌓아두면 비용↑|keep it all forever, cost climbs⟧", "⟦오래된 건 지워요|delete what\'s old⟧"), 1.0, hl=2)
         + person(560, 175, s=0.65, face=EYES, **MANAGER)
         + bubble(540, 90, 200, 54, "⟦필요한 만큼만 남겨둬요|keep only as much as you need⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦셋 다 쌓아두기만 하면 그것도 비용이에요 — 필요한 만큼만, 오래된 건 지워요|keeping all three forever costs money too — keep only what you need, and delete what\'s old⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "observability", "order": 45,
    "title": ("세 가지로 들여다보기", "Looking In Three Different Ways"),
    "h1": ("<em>관측 가능성</em>이 뭐예요?", "What is <em>Observability</em>?"),
    "sub": ("관측 가능성을 계기판 숫자, 일지, 요청이 지나간 길을 같이 들여다보는 이야기로 풀어봤어요.",
            "Observability, told as a story about looking at the gauge, the log, and the path a request took — all together."),
    "panels": [
        {"svg": P1, "alt": ("계기판에 에러가 늘었다는 빨간 바늘만 있고, 관제실 요원이 왜 늘었는지 몰라 당황함", "The gauge shows a red needle for rising errors, but the operator doesn't know why and is puzzled"),
         "caption": ("계기판엔 \'에러 늘었다\'만 보이고, 왜 늘었는지는 전혀 몰라요.", "The gauge just shows errors went up — it has no idea why."),
         "small": ("숫자는 보이는데, 이유는 안 보여요.", "The number shows up, but the reason doesn't.")},
        {"svg": P2, "alt": ("커다란 빨간 계기판 하나만 덩그러니 있고, 정비사가 그것만으로는 어디가 문제인지 모르겠다고 말함", "A single large red gauge sits alone, and a mechanic says this number alone can't tell where the problem is"),
         "caption": ("숫자 하나만으론 뭐가 문제인지 못 찾아요.", "A single number alone can't tell you what's actually wrong."),
         "small": ("에러율이 90%라는 것만 알지, 어느 기구가 문제인지는 몰라요.", "You just know the error rate hit 90% — not which ride is the problem.")},
        {"svg": P3, "hero": True, "alt": ("관제실 화면 세 개: 막대그래프(지표), 시간순 일지(로그), 요청이 지나간 길(트레이스)가 나란히 떠 있음", "Three control-room screens side by side: a bar chart (metrics), a timestamped log, and the path a request took (trace)"),
         "caption": ("숫자·일지·지나간 길, 세 가지를 같이 봐요.", "Watch three things together: the numbers, the written log, and the path a request took."),
         "small": ("숫자로 \'뭔가 이상해\'를 알고, 일지와 길로 \'어디가, 왜\'를 찾아요.", "The numbers tell you something's wrong; the log and the path tell you where and why."),
         "tricks": (4, [
             (METRIC_I, ("숫자로 이상함 알아채기", "Notice it with the numbers"), ("지표예요", "that's metrics"), "calm"),
             (LOG_I, ("자세한 기록으로 찾기", "Find it with detailed records"), ("로그예요", "that's logs")),
             (TRACE_I, ("요청이 지나간 길 추적", "Trace the path a request took"), ("어느 기구들을 거쳤나", "which rides it passed through"), "warm"),
             (DASH_I, ("셋을 한 화면에서 같이 보기", "Watch all three on one screen"), ("대시보드예요", "that's a dashboard")),
         ])},
        {"svg": P4, "alt": ("지표 화면에서 에러를 발견하고 화살표로 로그 화면으로, 다시 화살표로 트레이스 화면으로 이어지며 문제의 기구를 찾아감", "An error spotted on the metrics screen leads by arrow to the log screen, then by arrow to the trace screen, tracking down the problem ride"),
         "caption": ("지표로 알아채고, 로그로 찾고, 트레이스로 어느 기구인지 확인해요.", "Notice it with metrics, find it with logs, confirm which ride it was with traces."),
         "small": ("세 화면이 화살표로 이어지며 문제를 좁혀가요.", "The three screens connect by arrow, narrowing down the problem.")},
        {"svg": P5, "alt": ("보관 창고 안내판에 지표·로그·트레이스를 영원히 쌓아두면 비용이 오른다고 적혀 있고, 공원장이 필요한 만큼만 남겨두라고 말함", "A storage board warns that keeping metrics, logs, and traces forever raises cost, and a manager says to keep only what's needed"),
         "caption": ("셋 다 쌓아두기만 하면 그것도 비용이에요.", "Keeping all three forever costs money too."),
         "small": ("필요한 만큼만 남기고, 오래된 건 지워요.", "Keep only what you need, and delete what's old.")},
    ],
    "summary": (("<b>관측 가능성</b> = <b>숫자(지표)</b>, <b>일지(로그)</b>, <b>지나간 길(트레이스)</b>, 이 세 가지를 같이 봐서 '뭔가 이상해'뿐 아니라 '어디가, 왜'까지 찾는 일.",
                 "<b>Observability</b> = watching <b>metrics (the numbers)</b>, <b>logs (the written record)</b>, and <b>traces (the path a request took)</b> together, so you can find not just that something's wrong, but where and why."),
                ("Observability. 메트릭·로그·분산 트레이싱이라는 세 기둥으로 시스템 내부 상태를 들여다보는 능력이에요. 모니터링이 '아는 질문'에 답한다면, 관측 가능성은 미리 알지 못했던 질문에도 답할 수 있게 해줘요. 대시보드로 세 기둥을 한 화면에 모으고, 보관 비용 때문에 보존 기간을 정해 오래된 데이터는 지워요.",
                 "The ability to look into a system's internal state through three pillars: metrics, logs, and distributed tracing. Where monitoring answers questions you already knew to ask, observability lets you answer questions you didn't know to ask in advance. A dashboard brings the three pillars together on one screen, and a retention period deletes old data to keep storage costs in check.")),
    "glossary": [
        ("관측 가능성", "Observability", ("숫자·일지·지나간 길을 같이 보는 일.", "Watching the numbers, the log, and the path together."), ('모르던 질문에도 답할 수 있게 해줘요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', "It lets you answer questions you didn't even know to ask. → <a href=\"reliability-en.html\">the people who keep the park open</a>")),
        ("메트릭", "Metrics", ("관제실 벽의 막대그래프 숫자.", "The bar-graph numbers on the control-room wall."), ("\'뭔가 이상해\'를 가장 먼저 알려줘요.", "The first thing to tell you something's wrong.")),
        ("로그", "Logs", ("정비사가 적어두는 자세한 일지.", "The detailed log a mechanic keeps."), ("언제, 무슨 일이 있었는지 그대로 남아요.", "Records exactly when and what happened.")),
        ("분산 트레이싱", "Distributed tracing", ("요청 하나가 어느 기구들을 거쳤는지 그린 길.", "The path drawn for one request as it passes through each ride."), ("여러 기구를 거치는 요청일수록 더 중요해요.", "More important the more rides a request passes through.")),
        ("대시보드", "Dashboard", ("셋을 한 화면에 모아놓은 관제실 벽.", "The control-room wall where all three show up together."), ("따로 보면 못 보는 게 같이 보면 보여요.", "What's invisible apart becomes visible together.")),
        ("골든 시그널과의 관계", "Relation to golden signals", ("계기판 네 개가 바로 메트릭의 한 종류.", "The four gauges are one kind of metric."), ("관측 가능성은 그 계기판 너머까지 들여다봐요.", "Observability looks past those gauges, into logs and traces too.")),
        ("모니터링과의 차이", "Difference from monitoring", ("아는 질문에 답하는 것과, 모르는 질문에도 답할 수 있는 것의 차이.", "The difference between answering known questions and being able to answer unknown ones."), ("계기판만 보면 모니터링, 로그·트레이스까지 뒤지면 관측 가능성이에요.", "Watching only the gauges is monitoring; digging into logs and traces too is observability.")),
        ("SLI", "SLI (service level indicator)", ("오늘 운행 기록판에 적는 실제 숫자.", "The actual number written on today's operating log."), ("메트릭에서 골라낸, 약속을 잴 때 쓰는 숫자예요.", "A number picked out from the metrics, used to measure the promise you made.")),
    ],
}
