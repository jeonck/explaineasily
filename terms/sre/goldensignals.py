from _draw import *
from _world import *

# 1. 공원이 괜찮은지 어떻게 알아요? — 느낌으로 보다가 하나를 놓쳐요
P1 = svg(300, sky(300)
         + ride(140, 260, 0.6, color="var(--accent)") + ride(240, 260, 0.55, color="#5B8DEF")
         + ride(340, 260, 0.6, color="#2E7D6B", closed=True)
         + queueline(20, 216, 3, 0.4, 24)
         + controlroom(540, 30, 200, 110, bars=((0.4, "var(--stone)"), (0.6, "var(--stone)"), (0.3, "var(--stone)"), (0.5, "var(--stone)")))
         + person(430, 150, s=0.65, face=EYES, **OPERATOR)
         + bubble(330, 48, 190, 46, "⟦공원이 괜찮은지 어떻게 알아요?|How do I know if the park's OK?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦그냥 느낌으로 보다가 뒤쪽 기구가 멈춘 걸 놓쳤어요|going by feel alone, she missed the ride that quietly stopped⟧", 12, "var(--ink)", cls="d"))

# 2. 왜 어려운가 — 기구가 12개면 하나하나 다 못 봐요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + controlroom(40, 30, 320, 140, bars=((0.3, "var(--stone)"), (0.6, "var(--stone)"), (0.2, "var(--stone)"), (0.7, "var(--stone)"), (0.4, "var(--stone)"), (0.5, "var(--stone)")))
         + controlroom(400, 30, 320, 140, bars=((0.5, "var(--stone)"), (0.3, "var(--stone)"), (0.6, "var(--stone)"), (0.4, "var(--stone)"), (0.2, "var(--stone)"), (0.7, "var(--stone)")))
         + person(345, 190, s=0.75, face=FROWN + SWEAT, **OPERATOR)
         + '<path d="M310 220 Q260 200 230 170" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
         + '<path d="M425 220 Q480 200 520 170" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="4 4"/>'
         + label(380, 300, "⟦기구가 12개면 하나하나 다 볼 수 없어요|with 12 rides, no one can watch each one⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 계기판 네 개만 보면 돼요
LATENCY_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 18 V33 L45 40" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')
TRAFFIC_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--good)"/><rect x="27" y="26" width="10" height="28" fill="var(--good)"/><rect x="42" y="14" width="10" height="40" fill="var(--good)"/>')
ERROR_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M22 22 L42 42 M42 22 L22 42" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
SATURATION_I = icon('<rect x="20" y="10" width="24" height="44" rx="5" fill="none" stroke="var(--stone-dark)" stroke-width="4"/><rect x="24" y="30" width="16" height="20" fill="var(--bad)"/>')

P3 = svg(340, sky(340)
         + controlroom(140, 40, 480, 150, bars=((0.35, "var(--accent)"), (0.6, "var(--good)"), (0.15, "var(--bad)"), (0.45, "var(--accent)")))
         + label(209, 207, "⟦레이턴시|latency⟧", 11, "var(--ink)")
         + label(323, 207, "⟦트래픽|traffic⟧", 11, "var(--ink)")
         + label(437, 207, "⟦에러|errors⟧", 11, "var(--ink)")
         + label(551, 207, "⟦포화|saturation⟧", 11, "var(--ink)")
         + person(650, 214, s=0.75, face=SMILE, **OPERATOR)
         + label(380, 25, "⟦계기판 네 개만 보면 돼요|just watch four gauges⟧", 14, "var(--ink)", cls="d")
         + label(380, 328, "⟦기다리는 시간·손님 수·못 탄 사람·꽉 찬 정도, 이 넷이면 충분해요|wait time, guest count, failed rides, how full — these four are enough⟧", 12, "var(--muted)"))

# 4. 네 계기판 — 셋은 괜찮고 하나가 빨개요
P4 = svg(320, sky(320, ground=False)
         + gauge(110, 130, 1.1, level=0.25, label_text="⟦기다리는 시간|wait time⟧", color="var(--good)")
         + gauge(290, 130, 1.1, level=0.5, label_text="⟦손님 수|guest count⟧", color="var(--good)")
         + gauge(470, 130, 1.1, level=0.8, label_text="⟦못 탄 사람 수|couldn't ride⟧", color="var(--bad)")
         + gauge(650, 130, 1.1, level=0.4, label_text="⟦꽉 찬 정도|how full⟧", color="var(--good)")
         + label(380, 295, "⟦셋은 괜찮고, 하나가 빨개요 — 그게 신호예요|three are fine, one's red — that's the signal⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 넷 다 초록이어도 안심 못 할 때가 있어요
P5 = svg(320, sky(320, ground=False)
         + gauge(170, 110, 1.0, level=0.3, label_text="⟦레이턴시|latency⟧", color="var(--good)")
         + gauge(310, 110, 1.0, level=0.4, label_text="⟦트래픽|traffic⟧", color="var(--good)")
         + gauge(450, 110, 1.0, level=0.25, label_text="⟦에러|errors⟧", color="var(--good)")
         + gauge(590, 110, 1.0, level=0.35, label_text="⟦포화|saturation⟧", color="var(--good)")
         + person(380, 195, s=0.65, face=FROWN, **MECHANIC)
         + bubble(440, 180, 200, 40, "⟦근데 뭔가 이상해요?|but something feels off?⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 298, "⟦넷 다 초록이어도 숨은 문제가 있을 수 있어요|even all-green gauges can hide a problem⟧", 13, "var(--ink)", cls="d"))

PAGE = {
    "slug": "goldensignals", "order": 37,
    "title": ("관제실의 계기판 네 개", "The Four Gauges on the Control-Room Wall"),
    "h1": ("<em>골든 시그널</em>이 뭐예요?", "What are <em>Golden Signals</em>?"),
    "sub": ("골든 시그널을 공원 관제실 벽에 걸린 계기판 네 개 이야기로 풀어봤어요.",
            "Golden signals, told as a story about the four gauges on the control-room wall."),
    "panels": [
        {"svg": P1, "alt": ("관제실 요원이 느낌으로 공원을 보다가, 뒤쪽에서 조용히 멈춘 기구를 놓침", "An operator checks the park by feel and misses a ride that quietly stopped in back"),
         "caption": ("공원이 괜찮은지 어떻게 알아요?", "How do you know if the park's OK?"),
         "small": ("그냥 느낌으로 보다가는 뭔가를 놓쳐요.", "Going by feel alone, something slips past.")},
        {"svg": P2, "alt": ("관제실 화면 두 개에 바 그래프가 가득하고, 요원이 땀을 흘리며 번갈아 쳐다봄", "Two control-room screens full of bars; the operator sweats, glancing between them"),
         "caption": ("기구가 12개면 하나하나 다 볼 수 없어요.", "With 12 rides, you can't watch each one."),
         "small": ("화면에 숫자가 너무 많으면 사람 눈이 못 따라가요.", "When a screen has too many numbers, eyes can't keep up.")},
        {"svg": P3, "hero": True, "alt": ("관제실 화면에 막대 네 개만 떠 있고, 요원이 편안하게 바라봄", "The control-room screen shows just four bars; the operator watches calmly"),
         "caption": ("계기판 네 개만 보면 돼요.", "Just watch four gauges."),
         "small": ("기다리는 시간, 손님 수, 못 탄 사람, 꽉 찬 정도 — 이 넷이면 충분해요.", "Wait time, guest count, failed rides, how full — these four are enough."),
         "tricks": (4, [
             (LATENCY_I, ("기다리는 시간", "Wait time"), ("손님이 얼마나 기다리나", "how long guests wait"), "calm"),
             (TRAFFIC_I, ("손님 수", "Guest count"), ("오늘 몇 명이 왔나", "how many came today")),
             (ERROR_I, ("못 탄 사람 수", "Failed rides"), ("타려다 못 탄 사람", "who tried and couldn't ride"), "warm"),
             (SATURATION_I, ("꽉 찬 정도", "How full"), ("자리가 얼마나 남았나", "how much room is left")),
         ])},
        {"svg": P4, "alt": ("계기판 네 개가 나란히 있고, 셋은 초록 바늘, 하나는 빨간 바늘", "Four gauges side by side; three needles are green, one is red"),
         "caption": ("셋은 괜찮고, 하나가 빨개요 — 그게 신호예요.", "Three are fine, one's red — that's the signal."),
         "small": ("넷을 같이 보면 어디가 문제인지 바로 보여요.", "Watching all four together shows exactly where the trouble is.")},
        {"svg": P5, "alt": ("계기판 네 개가 전부 초록인데 정비사가 뭔가 이상하다고 말함", "All four gauges show green, but a mechanic senses something is off"),
         "caption": ("넷 다 초록이어도 안심 못 할 때가 있어요.", "Even all-green gauges don't guarantee everything's fine."),
         "small": ("숨은 문제는 다른 도구로 더 들여다봐야 해요.", "A hidden problem needs a closer look with other tools.")},
    ],
    "summary": (("<b>골든 시그널</b> = 공원 전체를 다 못 보는 대신, <b>기다리는 시간·손님 수·못 탄 사람·꽉 찬 정도</b> 네 계기판만 보면 되는 요령.",
                 "<b>Golden signals</b> = instead of watching the whole park, just watch four gauges: <b>wait time, guest count, failed rides, and how full.</b>"),
                ("레이턴시(latency), 트래픽(traffic), 에러율(errors), 포화도(saturation)의 앞글자를 딴 구글 SRE의 네 가지 핵심 지표예요. 비슷한 짝으로 USE 방법(활용률·포화·에러, 자원 중심)과 RED 방법(비율·에러·시간, 요청 중심)이 있어요.",
                 "Google SRE's four core metrics: latency, traffic, errors, and saturation. Related frameworks are the USE method (utilization, saturation, errors — resource-focused) and the RED method (rate, errors, duration — request-focused).")),
    "glossary": [
        ("골든 시그널", "Golden signals", ("계기판 네 개.", "The four gauges."), ("레이턴시·트래픽·에러·포화, 이 넷만 보면 돼요.", "Latency, traffic, errors, saturation — just these four.")),
        ("레이턴시", "Latency", ("손님이 기다리는 시간.", "How long a guest waits."), ("길어지면 손님이 지쳐요.", "Too long, and guests get tired of waiting.")),
        ("트래픽", "Traffic", ("오늘 온 손님 수.", "How many guests came today."), ("많아지는 건 나쁜 게 아니에요 — 비교 기준이에요.", "More isn't bad by itself — it's a baseline to compare against.")),
        ("에러율", "Error rate", ("타려다 못 탄 사람 수.", "How many tried to ride and couldn't."), ("늘어나면 바로 알아차려야 해요.", "A rise here needs to be noticed right away.")),
        ("포화도", "Saturation", ("기구가 꽉 찬 정도.", "How full a ride already is."), ("꽉 차기 직전에 미리 알면 좋아요.", "Best to know before it's completely full.")),
        ("USE 방법", "USE method", ("자원이 괜찮은지 보는 또 다른 네 글자.", "Another four-letter way to check resources."), ("활용률·포화·에러 — 기구 자체를 보는 방법이에요.", "Utilization, saturation, errors — it looks at the ride itself.")),
        ("RED 방법", "RED method", ("요청이 괜찮은지 보는 세 글자.", "A three-letter way to check requests."), ("비율·에러·시간 — 손님이 겪는 걸 보는 방법이에요.", "Rate, errors, duration — it looks at what guests experience.")),
        ("관측", "Observability", ("계기판 너머까지 들여다보는 일.", "Looking deeper than the gauges."), ('넷 다 초록이어도 안심 못 할 때 필요해요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Needed when all-green gauges still aren\'t enough. → <a href="reliability-en.html">the people who keep the park open</a>')),
    ],
}
