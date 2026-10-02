from _draw import *
from _world import *

# 1. 사소한 일에도 호출기가 계속 울려서, 당번이 꺼버리고 진짜 큰일은 못 들어요
P1 = svg(320, night(320)
         + controlroom(40, 30, 190, 100, bars=((0.25, "var(--bad)"), (0.2, "var(--bad)"), (0.3, "var(--bad)"), (0.18, "var(--bad)")))
         + walkie(260, 140, 0.9)
         + person(100, 260 - 112 * 0.7, s=0.7, face=FROWN + SWEAT, **OPERATOR)
         + bubble(10, 150, 190, 44, "⟦또 울리네... 그냥 꺼야지|ringing again... I'll just turn it off⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(620, 260, 0.9, color="var(--bad)", closed=True, label_text="⟦진짜 큰일|the real emergency⟧")
         + label(620, 300, "⟦아무도 몰랐어요|nobody noticed⟧", 11, "#C9D5E6")
         + label(380, 300, "⟦사소한 일에도 호출기가 계속 울려서, 당번이 꺼버리고 진짜 큰일은 못 들어요|the pager keeps ringing over small stuff, so the on-call turns it off — and misses the real emergency⟧", 12, "#F5E6B8", cls="d"))

# 2. 왜: 다 울리게 해두면 중요한 것과 안 중요한 게 섞여요 (알림 피로)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + controlroom(90, 40, 220, 120, bars=((0.3, "var(--bad)"), (0.8, "var(--bad)"), (0.2, "var(--bad)"), (0.5, "var(--bad)")))
         + walkie(360, 90, 1.0) + walkie(410, 70, 0.8) + walkie(460, 105, 0.85)
         + person(580, 260 - 112 * 0.65, s=0.65, face=FROWN + SWEAT, **OPERATOR)
         + bubble(500, 70, 220, 50, "⟦다 똑같이 울리니 뭐가 급한지 모르겠어요|they all ring the same — I can't tell what's urgent⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦다 울리게 해두면 중요한 것과 안 중요한 게 섞여요 — 알림 피로예요|ring for everything, and the important gets lost in the unimportant — that's alert fatigue⟧", 12, "var(--ink)"))

# 3. hero: 손님이 느낄 만큼 계속 나쁠 때만 울려요
P3 = svg(340, sky(340)
         + controlroom(50, 50, 220, 130, bars=((0.4, "var(--good)"), (0.9, "var(--bad)"), (0.3, "var(--good)"), (0.5, "var(--good)")))
         + gauge(370, 150, 1.3, level=0.85, label_text="⟦손님이 느끼는 선|the line guests feel⟧", color="var(--bad)")
         + '<path d="M270 150 L340 150" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + walkie(520, 120, 1.0)
         + person(560, 300 - 112 * 0.7, s=0.7, face=EYES, **OPERATOR)
         + '<path d="M470 150 L525 125" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 40, "⟦손님이 느낄 만큼 계속 나쁠 때만 울려요|it only rings when things stay bad enough for guests to feel it⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦잠깐 삐끗은 넘기고, 계속 나쁘면 호출해요|a brief wobble passes — staying bad is what triggers the call⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 잠깐 튀었다가(울리지 않음) vs 계속 나쁘면(울림)
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + gauge(190, 110, 1.1, level=0.55, color="var(--good)")
         + label(190, 175, "⟦잠깐 튀었다 금방 돌아와요|spikes briefly, then comes right back⟧", 11, "var(--ink)")
         + label(190, 215, "⟦→ 울리지 않아요|-> doesn't ring⟧", 12, "var(--good)", cls="d")
         + gauge(570, 110, 1.1, level=0.85, color="var(--bad)")
         + label(570, 175, "⟦몇 분째 계속 나빠요|stays bad for minutes⟧", 11, "var(--ink)")
         + walkie(570, 210, 0.9)
         + label(570, 255, "⟦→ 울려요|-> it rings⟧", 12, "var(--bad)", cls="d")
         + label(380, 300, "⟦지속 시간 조건 — 몇 분 넘게 나빠야 진짜예요|a duration condition: it has to stay bad for minutes to count⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 너무 안 울리게 하면 진짜 문제도 놓쳐요
P5 = svg(300, sky(300)
         + gauge(160, 110, 1.2, level=0.95, color="var(--bad)")
         + label(160, 185, "⟦기준을 너무 느슨히 했어요|set the threshold too loose⟧", 11, "var(--bad)")
         + person(440, 260 - 112 * 0.6, s=0.6, face=FROWN, **OPERATOR)
         + bubble(360, 150, 170, 44, "⟦이번엔 안 울렸는데...|it didn't ring this time...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(620, 260, 0.8, color="var(--bad)", closed=True, label_text="⟦이것도 놓쳤어요|missed this one too⟧")
         + label(380, 282, "⟦너무 안 울리게 하면 진짜 문제도 놓쳐요 — 적당한 기준은 계속 찾아야 해요|set it too quiet and you miss real problems too — finding the right threshold is ongoing work⟧", 12, "var(--ink)"))

GUEST_I = icon('<path d="M14 16 A24 24 0 0 1 50 16" stroke="var(--bad)" stroke-width="4" fill="none"/><circle cx="32" cy="38" r="16" fill="var(--accent)"/><circle cx="26" cy="36" r="2.5" fill="#142033"/><circle cx="38" cy="36" r="2.5" fill="#142033"/><path d="M24 44 Q32 50 40 44" stroke="#142033" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
BLIP_I = icon('<path d="M8 32 H20 L26 18 L32 44 L38 32 H56" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 10 L44 10" stroke="var(--muted)" stroke-width="3" stroke-dasharray="3 3"/>')
GRADE_I = icon('<rect x="14" y="10" width="36" height="10" rx="3" fill="var(--bad)"/><rect x="14" y="27" width="36" height="10" rx="3" fill="var(--accent)"/><rect x="14" y="44" width="36" height="10" rx="3" fill="var(--good)"/>')
REVIEW_I = icon('<rect x="12" y="8" width="28" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 18 h16 M18 26 h16 M18 34 h10" stroke="#142033" stroke-width="2.5"/><circle cx="42" cy="44" r="9" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M48 50 L56 58" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "alerting", "order": 39,
    "title": ("몇 번 울려야 진짜 비상인가", "How Many Rings Make a Real Emergency"),
    "h1": ("<em>알림</em>이 뭐예요?", "What is <em>Alerting</em>?"),
    "sub": ("알림(얼러팅)을, 손님이 느낄 만큼 계속 나쁠 때만 울리는 호출기 이야기로 풀어봤어요.",
            "Alerting, told as a story about a pager that only rings when things stay bad enough for guests to feel it."),
    "panels": [
        {"svg": P1, "alt": ("관제실 화면에 사소한 빨간 막대가 계속 뜨고, 요원이 호출기를 꺼버림. 정작 멀리서 큰 기구 하나가 고장난 채 아무도 모름", "The control room keeps flashing minor red bars; the operator turns the pager off — while a big ride sits broken and unnoticed"),
         "caption": ("사소한 일에도 호출기가 계속 울려서, 당번이 꺼버려요.", "The pager keeps ringing over small stuff, so the on-call turns it off."),
         "small": ("그러다 진짜 큰일이 났을 때는 아무도 못 들어요.", "And when the real emergency hits, nobody hears it.")},
        {"svg": P2, "alt": ("관제실 화면에 막대가 뒤섞여 있고, 무전기 여러 대가 동시에 울리고, 요원이 지쳐서 뭐가 급한지 모르겠다고 말함", "The control-room bars are jumbled, several pagers ring at once, and the exhausted operator says they can't tell what's urgent"),
         "caption": ("다 울리게 해두면 중요한 것과 안 중요한 게 섞여요.", "Ring for everything, and the important gets lost in the unimportant."),
         "small": ("알림 피로예요 — 결국 다 무시하게 돼요.", "That's alert fatigue — eventually everything gets ignored.")},
        {"svg": P3, "hero": True, "alt": ("관제실 계기판 옆에 '손님이 느끼는 선'이 그어져 있고, 그 선을 넘을 때만 무전기가 요원에게 연결됨", "A line marked 'the line guests feel' sits beside the gauges, and only crossing it connects the pager to the operator"),
         "caption": ("손님이 느낄 만큼 계속 나쁠 때만 울려요.", "It only rings when things stay bad enough for guests to feel it."),
         "small": ("잠깐 삐끗은 넘기고, 계속 나쁘면 호출해요.", "A brief wobble passes — staying bad is what triggers the call."),
         "tricks": (4, [
             (GUEST_I, ("손님이 느낄 정도만", "Only what guests would feel"), ("그 아래는 그냥 넘겨요", "below that, just let it pass"), "calm"),
             (BLIP_I, ("잠깐의 흔들림은 넘겨요", "Let a brief wobble pass"), ("지속 시간 조건이에요", "that's the duration condition")),
             (GRADE_I, ("울림에도 등급을 둬요", "Grade the rings too"), ("그냥 보기 vs 당장 호출", "just watch vs call right now"), "warm"),
             (REVIEW_I, ("울린 건 나중에 돌아봐요", "Review every ring afterward"), ("진짜였나 확인해요", "check whether it was real")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 계기판이 잠깐 튀었다 돌아와 울리지 않음. 오른쪽: 몇 분째 계속 나빠서 무전기가 울림", "Left: the gauge spikes briefly then recovers, no ring. Right: it stays bad for minutes, and the pager rings"),
         "caption": ("잠깐 튀었다가(울리지 않음) vs 계속 나쁘면(울림).", "A brief spike (no ring) versus staying bad (it rings)."),
         "small": ("몇 분 넘게 나빠야 진짜 신호로 쳐요.", "Only staying bad for minutes counts as a real signal.")},
        {"svg": P5, "alt": ("계기판이 거의 100%를 가리키는데도 안 울렸고, 요원이 당황하며 멀리 고장난 기구를 뒤늦게 발견함", "The gauge sits near the top but never rang, and the startled operator spots a broken ride too late"),
         "caption": ("너무 안 울리게 하면 진짜 문제도 놓쳐요.", "Set it too quiet, and you miss real problems too."),
         "small": ("적당한 기준은 한 번에 안 정해져요 — 계속 다듬어 가요.", "The right threshold isn't set once — it keeps getting tuned.")},
    ],
    "summary": (("<b>알림</b> = <b>손님이 느낄 만큼</b>, 그리고 <b>계속</b> 나쁠 때만 울리게 정해서, 호출기가 진짜 비상에만 쓰이게 하는 일.",
                 "<b>Alerting</b> = deciding to ring only when things are bad enough for <b>guests to feel</b> — and <b>stay</b> that way — so the pager is saved for real emergencies."),
                ("Alerting. 모니터링 지표가 특정 임계값을 넘을 때 사람에게 알리는 메커니즘이에요. 임계값과 지속 시간 조건을 함께 써서 일시적 흔들림을 걸러내고, 심각도 등급으로 '그냥 보기'와 '당장 호출'을 나눠요. 알림이 너무 많으면 알림 피로가 생겨 오히려 위험해요.",
                 "A mechanism that notifies a person when a monitored metric crosses a threshold. Combining a threshold with a duration condition filters out brief wobbles, and severity levels separate 'just watch' from 'page now'. Too many alerts cause alert fatigue, which is its own danger.")),
    "glossary": [
        ("알림", "Alerting", ("큰일일 때만 울리는 신호.", "A signal that rings only for real trouble."), ("평소엔 조용해요.", "Quiet the rest of the time.")),
        ("알림 피로", "Alert fatigue", ("다 울리면 뭐가 중요한지 몰라요.", "When everything rings, nothing stands out."), ("결국 다 꺼버리게 돼요.", "Eventually, everything gets turned off.")),
        ("임계값", "Threshold", ("몇 % 넘으면 울릴지 정한 선.", "The line that decides when it rings."), ("너무 낮으면 자주, 너무 높으면 놓쳐요.", "Too low rings too often; too high misses things.")),
        ("지속 시간 조건", "Duration condition", ("잠깐의 흔들림은 무시하는 규칙.", "The rule that ignores a brief wobble."), ("계속 나빠야만 울려요.", "Only staying bad triggers a ring.")),
        ("심각도 등급", "Severity levels", ("그냥 보기 vs 당장 호출.", "Just watch versus call right now."), ("모든 알림이 같은 무게는 아니에요.", "Not every alert carries the same weight.")),
        ("번 레이트 알림", "Burn-rate alerting", ("허용된 고장 티켓이 얼마나 빨리 줄어드는지 보는 알림.", "An alert that watches how fast the allowed failures are being used up."), ('→ <a href="errorbudget-ko.html">허용된 고장 티켓 묶음</a>', '→ <a href="errorbudget-en.html">the bundle of allowed failure tickets</a>')),
        ("SLI", "SLI", ("계기판에 뜨는 숫자 그 자체.", "The number shown on the gauge itself."), ('알림의 기준이 되는 값이에요. → <a href="sli-ko.html">오늘 운행 기록판</a>', 'It\'s the value the alert watches. → <a href="sli-en.html">today\'s operating record</a>')),
        ("온콜", "On-call", ("울리면 응답하는 사람.", "Whoever answers when it rings."), ('이번 주 호출기를 든 사람이에요. → <a href="oncall-ko.html">이번 주 호출기를 든 사람</a>', 'Whoever is holding the pager this week. → <a href="oncall-en.html">whoever\'s holding the pager</a>')),
    ],
}
