from _draw import *
from _world import *

# 1. "오늘 공원 어땠어요?" 물으면 다들 느낌으로만 답해요
P1 = svg(300, sky(300)
         + person(260, 180, s=0.7, face=EYES, **MANAGER)
         + bubble(170, 90, 210, 46, "⟦오늘 공원 어땠어요?|how was the park today?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(480, 190, s=0.65, face=EYES, **OPERATOR)
         + bubble(400, 110, 200, 42, "⟦음... 그냥저냥요?|uh... so-so, I guess?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦'오늘 어땠어요?' 물으면 다들 느낌으로만 답해요|ask how today went, and everyone answers by feel alone⟧", 12, "var(--ink)"))

# 2. 느낌은 사람마다 달라서 비교가 안 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 163, s=0.6, face=SMILE, **OPERATOR) + bubble(50, 80, 160, 42, "⟦좋았어요!|it was great!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 163, s=0.6, face=FROWN, **MECHANIC) + bubble(300, 80, 160, 42, "⟦별로였는데요|it wasn't, really⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(630, 163, s=0.6, face=EYES, **MANAGER) + bubble(550, 80, 160, 42, "⟦그냥저냥요|so-so, I guess⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦느낌은 사람마다 달라서 비교가 안 돼요|everyone's feeling is different, so you can't compare them⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 느낌 대신, 숫자로 재는 기록판을 둬요
STOPWATCH_I = icon('<circle cx="32" cy="36" r="20" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 36 V22" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><rect x="26" y="8" width="12" height="8" rx="2" fill="var(--stone-dark)"/>')
NUMBER_I = icon('<rect x="10" y="20" width="44" height="28" rx="4" fill="#1B2A44"/><rect x="14" y="24" width="36" height="20" fill="var(--good)"/>')
CALENDAR_I = icon('<rect x="12" y="14" width="40" height="36" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M12 26 h40" stroke="var(--stone-dark)" stroke-width="3"/><rect x="18" y="32" width="8" height="8" fill="var(--accent)"/><rect x="30" y="32" width="8" height="8" fill="var(--accent)"/>')
TARGET_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="13" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="4" fill="var(--bad)"/>')

P3 = svg(340, sky(340)
         + controlroom(200, 70, 360, 140, bars=((0.75, "var(--good)"), (0.9, "var(--good)")))
         + label(290, 230, "⟦응답 시간|response time⟧", 12, "var(--ink)")
         + label(470, 230, "⟦성공률|success rate⟧", 12, "var(--ink)")
         + person(620, 260, s=0.65, face=SMILE, **OPERATOR)
         + label(380, 30, "⟦느낌 대신, 숫자로 재는 기록판을 둬요|instead of feelings, keep a log measured in numbers⟧", 14, "var(--ink)", cls="d")
         + label(380, 328, "⟦이렇게 잰 숫자를 SLI(지표)라고 불러요|a number measured this way is called an SLI⟧", 12, "var(--muted)"))

# 4. 오늘 기록판 — 요청 10만 건, 1초 안 응답 99.2%, 성공 99.95%
P4 = svg(300, sky(300, ground=False)
         + board(260, 50, 300, 190, "⟦오늘 기록판|TODAY'S LOG⟧", ("⟦요청: 10만 건|requests: 100,000⟧", "⟦1초 안에 응답: 99.2%|answered within 1s: 99.2%⟧", "⟦성공: 99.95%|succeeded: 99.95%⟧"), 1.0)
         + person(170, 203, s=0.6, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + label(380, 286, "⟦매일 같은 방식으로, 숫자로 재서 적어둬요|measured the same way, every day, and written down as numbers⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 잘못된 걸 재면 숫자는 좋아도 손님은 불만이에요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(60, 50, 280, 150, "⟦기록판|THE LOG⟧", ("⟦성공률: 99.99%|success rate: 99.99%⟧", "⟦다 좋아 보여요|looks great⟧"), 1.0, hl=0)
         + person(480, 190, s=0.7, face=FROWN, **MANAGER)
         + bubble(420, 90, 240, 50, "⟦근데 줄이 너무 길어서 속상해요|but the line was so long, I'm upset⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦잘못된 걸 재면, 숫자는 좋아도 손님은 불만이에요|measure the wrong thing, and the numbers look great while guests stay unhappy⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "sli", "order": 33,
    "title": ("오늘 운행 기록판", "Today's Ride Log"),
    "h1": ("<em>SLI</em>가 뭐예요?", "What is an <em>SLI</em>?"),
    "sub": ("SLI를 느낌 대신 숫자로 재는 오늘의 운행 기록판 이야기로 풀어봤어요.",
            "SLI, told as a story about keeping today's ride log measured in numbers, instead of by feel."),
    "panels": [
        {"svg": P1, "alt": ("공원장이 오늘 공원이 어땠는지 묻고, 관제실 요원이 그냥저냥이라고 애매하게 답함", "The manager asks how the park was today, and the operator gives a vague so-so answer"),
         "caption": ("'오늘 어땠어요?' 물으면 다들 느낌으로만 답해요.", "Ask how today went, and everyone answers by feel alone."),
         "small": ("그냥저냥, 좋았던 것 같아요 — 다 애매한 말이에요.", "So-so, pretty good, I think — it's all vague talk.")},
        {"svg": P2, "alt": ("관제실 요원 셋이 오늘 하루에 대해 각각 좋았다, 별로였다, 그냥저냥이다로 서로 다르게 답함", "Three staff members each describe today differently — great, not great, so-so"),
         "caption": ("느낌은 사람마다 달라서 비교가 안 돼요.", "Everyone's feeling is different, so you can't compare them."),
         "small": ("어제보다 나은지도, 목표에 가까운지도 알 수 없어요.", "You can't tell if it's better than yesterday, or close to any target.")},
        {"svg": P3, "hero": True, "alt": ("관제실 화면에 응답 시간과 성공률 막대그래프가 떠 있고, 요원이 편안하게 지켜봄", "The control-room screen shows bars for response time and success rate, watched calmly by an operator"),
         "caption": ("느낌 대신, 숫자로 재는 기록판을 둬요.", "Instead of feelings, keep a log measured in numbers."),
         "small": ("이렇게 잰 숫자를 SLI(서비스 수준 지표)라고 불러요.", "A number measured this way is called an SLI — a service level indicator."),
         "tricks": (4, [
             (STOPWATCH_I, ("손님이 실제로 느끼는 걸 재요", "Measure what guests actually feel"), ("응답 시간, 성공률처럼요", "like response time and success rate"), "calm"),
             (NUMBER_I, ("숫자로, 느낌 아니게 적어요", "Write it as a number, not a feeling"), ("애매한 말은 빼고요", "no vague words allowed")),
             (CALENDAR_I, ("매일 같은 방식으로 재요", "Measure it the same way, every day"), ("비교할 수 있게요", "so it can be compared"), "warm"),
             (TARGET_I, ("이 숫자가 나중에 목표의 기준이 돼요", "This number later becomes the target's baseline"), ("오늘의 기록이 내일의 약속이 돼요", "today's reading becomes tomorrow's promise")),
         ])},
        {"svg": P4, "alt": ("오늘 기록판에 요청 10만 건, 1초 안 응답 99.2%, 성공 99.95%라는 숫자가 적혀 있음", "Today's log board reads 100,000 requests, 99.2% answered within a second, 99.95% succeeded"),
         "caption": ("오늘: 요청 10만 건, 1초 안 응답 99.2%, 성공 99.95%.", "Today: 100,000 requests, 99.2% answered within 1s, 99.95% succeeded."),
         "small": ("매일 같은 방식으로, 숫자로 재서 적어둬요.", "Measured the same way, every day, and written down as numbers.")},
        {"svg": P5, "alt": ("성공률 99.99%로 다 좋아 보이는 기록판 옆에서 공원장이 줄이 너무 길어서 속상하다고 말함", "Next to a log board showing a great 99.99% success rate, the manager says the line was still too long and upsetting"),
         "caption": ("잘못된 걸 재면, 숫자는 좋아도 손님은 불만이에요.", "Measure the wrong thing, and the numbers look great while guests stay unhappy."),
         "small": ("손님이 진짜 신경 쓰는 걸 재야 의미가 있어요.", "It only matters if you measure what guests actually care about.")},
    ],
    "summary": (("<b>SLI</b> = 느낌 대신 <b>응답 시간·성공률 같은 걸 숫자로</b>, 매일 <b>같은 방식으로 재서</b> 남기는 오늘의 기록판.",
                 "<b>SLI</b> = today's log, keeping things like <b>response time and success rate as numbers</b>, <b>measured the same way</b> every single day."),
                ("Service Level Indicator. 시스템이 실제로 얼마나 잘 동작하는지 손님이 겪는 방식으로 재는 숫자 지표예요. 레이턴시, 에러율, 가용성처럼 측정 가능한 값으로, 나중에 SLO(목표)를 정하는 기준이 돼요.",
                 "A service level indicator — a numeric measure of how well a system actually performs, from the guest's point of view. Things like latency, error rate, and availability become the baseline an SLO later sets a target against.")),
    "glossary": [
        ("SLI(서비스 수준 지표)", "SLI", ("숫자로 재는 오늘의 기록판.", "Today's log, measured in numbers."), ("느낌이 아니라 숫자로 남겨요.", "Written down as numbers, not feelings.")),
        ("응답 시간", "Response time", ("손님이 요청하고 답을 받기까지 걸린 시간.", "How long it takes to answer a guest's request."), ("대표적인 SLI 중 하나예요.", "One of the most common SLIs.")),
        ("성공률", "Success rate", ("시도한 것 중 제대로 끝난 비율.", "The share of attempts that finished properly."), ("실패율의 반대편에서 같은 걸 봐요.", "The flip side of the failure rate — same thing, viewed the other way.")),
        ("가용성 지표", "Availability", ("공원이 열려 있던 시간의 비율.", "The share of time the park stayed open."), ("가동 시간을 숫자로 바꾼 값이에요.", "Uptime, turned into a measurable number.")),
        ("측정 방법", "Measurement point", ("어디서 재느냐 — 손님 쪽 vs 서버 쪽.", "Where you measure — the guest's side, or the server's."), ("손님 쪽에서 잴수록 진짜 경험에 가까워요.", "Measuring closer to the guest gets you closer to the real experience.")),
        ("골든 시그널과의 관계", "vs. golden signals", ("계기판 네 개 중 SLI로 고른 몇 개.", "A few of the four gauges, picked out as SLIs."), ("넷 다 SLI가 될 수 있지만, 다 쓸 필요는 없어요.", "All four could be SLIs, but you don't have to use every one.")),
        ("SLO", "SLO", ("이 숫자로 정하는 목표.", "The target set using this number."), ("SLI가 먼저 있어야 SLO를 정할 수 있어요.", "You need an SLI before you can set an SLO.")),
        ("관측", "Observability", ("숫자 너머까지 들여다보는 일.", "Looking deeper than the numbers."), ('기록판이 전부 좋아도 안심 못 할 때 필요해요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Needed when even a great-looking log isn\'t the whole story. → <a href="reliability-en.html">the people who keep the park open</a>')),
    ],
}
