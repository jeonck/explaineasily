from _draw import *
from _world import *

# 1. "우리 공원, 예비 발전기 진짜 되나요?" — 아무도 확신 못해요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.75, face=EYES, **MANAGER)
         + bubble(20, 40, 260, 54, "⟦우리 공원, 예비 발전기 진짜 되나요?|does our spare generator actually work?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(430, 160, s=0.75, face=FROWN + SWEAT, **OPERATOR)
         + bubble(460, 50, 260, 54, "⟦글쎄요... 한 번도 안 꺼본 적이 없어서요|not sure... we\'ve never once switched it off⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + shed(650, 215, 0.7, label_text="⟦예비 발전기|spare generator⟧")
         + label(380, 280, "⟦예비 발전기가 진짜 되는지, 아무도 확신 못해요 — 한 번도 안 꺼봤으니까요|no one\'s sure the spare generator actually works — it\'s never been switched off⟧", 12, "var(--ink)"))

# 2. 왜: 안 써본 안전장치는 진짜 비상에 안 될 수도 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shed(230, 210, 0.85, label_text="⟦예비 발전기|spare generator⟧")
         + board(420, 50, 300, 130, "⟦점검 기록|CHECK LOG⟧", ("⟦마지막 점검: 기억 안 남|last checked: can\'t recall⟧", "⟦한 번도 안 꺼본 안전장치예요|a safety switch never once flipped⟧"), 1.0)
         + person(90, 165, s=0.7, face=FROWN + SWEAT, **MECHANIC)
         + bubble(10, 60, 200, 54, "⟦저거 진짜 비상 때 되는 거 맞아요?|is that really going to work in a real emergency?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦안 써본 안전장치는 진짜 비상에 안 될 수도 있어요|a safety net you\'ve never tested might fail when you need it most⟧", 12, "var(--bad)", cls="d"))

# 3. hero: 평소에 몰래 기구 하나를 꺼봐요 — 예비가 바로 이어받으면 성공이에요
TOGGLE_I = icon('<rect x="8" y="24" width="48" height="20" rx="10" fill="var(--stone-dark)"/><circle cx="20" cy="34" r="12" fill="var(--bad)"/>')
LIVE_I = icon('<circle cx="24" cy="30" r="14" fill="var(--accent)"/><circle cx="48" cy="18" r="6" fill="var(--bad)"/><circle cx="48" cy="18" r="10" fill="none" stroke="var(--bad)" stroke-width="2" opacity="0.6"/>')
GROW_I = icon('<rect x="10" y="42" width="10" height="14" fill="var(--good)"/><rect x="26" y="30" width="10" height="26" fill="var(--good)"/><rect x="42" y="14" width="10" height="42" fill="var(--good)"/>')
STOP_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)"/><rect x="24" y="24" width="16" height="16" fill="var(--panel)"/>')

P3 = svg(360, sky(360)
         + ride(130, 300, 0.8, color="var(--accent)") + ride(260, 300, 0.65, color="#5B8DEF")
         + ride(400, 300, 0.75, color="var(--stone)", closed=True, label_text="⟦몰래 꺼봄|secretly switched off⟧")
         + person(400, 238, s=0.55, face=EYES, extra=WRENCH, **MECHANIC)
         + '<path d="M430 230 Q480 170 520 140" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + controlroom(520, 50, 200, 120, bars=((0.6, "var(--good)"), (0.55, "var(--good)"), (0.5, "var(--good)"), (0.6, "var(--good)")))
         + person(590, 200, s=0.7, face=SMILE, **OPERATOR)
         + label(650, 255, "⟦예비가 바로 이어받았어요|the spare just took right over⟧", 11, "var(--good)")
         + label(380, 35, "⟦평소에 몰래 기구 하나를 꺼봐요 — 예비가 바로 이어받으면 성공이에요|secretly switch one ride off during normal hours — if the spare takes right over, it worked⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦진짜 손님이 있는 시간에, 작게 해봐요|do it small, while real guests are still there⟧", 12, "var(--muted)"))

# 4. 정비사가 몰래 하나를 꺼보고, 예비가 넘겨받는지 계기판으로 확인해요
P4 = svg(320, sky(320, ground=False)
         + label(130, 40, "⟦① 꺼본다|switch it off⟧", 13, "var(--ink)", cls="d")
         + gauge(130, 130, 1.0, level=0.15, label_text="⟦전력|power⟧", color="var(--bad)")
         + '<path d="M165 130 H345" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 40, "⟦② 예비가 넘겨받는다|the spare takes over⟧", 13, "var(--ink)", cls="d")
         + gauge(380, 130, 1.0, level=0.75, label_text="⟦전력|power⟧", color="var(--accent)")
         + '<path d="M415 130 H600" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(630, 40, "⟦③ 계기판으로 확인|check the gauge⟧", 13, "var(--ink)", cls="d")
         + gauge(630, 130, 1.0, level=0.9, label_text="⟦정상|normal⟧", color="var(--good)")
         + person(630, 205, s=0.6, face=SMILE, **OPERATOR)
         + label(380, 300, "⟦정비사가 몰래 하나를 꺼보고, 예비가 넘겨받는지 계기판으로 확인해요|a mechanic quietly switches one off, then checks the gauge to see if the spare takes over⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 아무 준비 없이 무작정 하면 진짜 사고가 나요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ride(170, 230, 0.8, color="var(--bad)", closed=True, label_text="⟦전체 다운!|everything down!⟧")
         + person(70, 160, s=0.6, face=FROWN + SWEAT, **MECHANIC)
         + queueline(230, 190, 3, 0.4, 26)
         + label(190, 260, "⟦준비 없이 무작정 끄면 진짜 사고가 나요|flipping switches with no plan causes a real outage⟧", 11, "var(--bad)")
         + shed(600, 220, 0.75, label_text="⟦작게 시작|start small⟧")
         + bigbutton(520, 165, 0.7)
         + person(680, 175, s=0.55, face=SMILE, **OPERATOR) + walkie(715, 150, 0.6)
         + label(590, 260, "⟦작게, 되돌릴 수 있게, 미리 알리고 해야 해요|small, reversible, and announced ahead of time⟧", 11, "var(--good)")
         + label(380, 280, "⟦이 비유가 깨지는 곳: 준비 없는 카오스는 실험이 아니라 사고예요|where the analogy breaks: chaos with no plan isn\'t an experiment, it\'s an accident⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "chaosengineering", "order": 42,
    "title": ("일부러 내는 가짜 고장", "The Fake Breakdowns We Cause on Purpose"),
    "h1": ("<em>카오스 엔지니어링</em>이 뭐예요?", "What is <em>Chaos Engineering</em>?"),
    "sub": ("카오스 엔지니어링을 예비 발전기가 진짜 되는지 몰래 확인해 보는 이야기로 풀어봤어요.",
            "Chaos engineering, told as a story about quietly checking whether the spare generator actually works."),
    "panels": [
        {"svg": P1, "alt": ("공원장이 예비 발전기가 진짜 되는지 묻자, 관제실 요원이 한 번도 안 꺼봐서 확신 못함", "A manager asks whether the spare generator really works; the operator isn't sure, since it's never been switched off"),
         "caption": ("우리 공원, 예비 발전기 진짜 되나요?", "Does our spare generator actually work?"),
         "small": ("아무도 확신 못해요 — 한 번도 안 꺼봤으니까요.", "No one's sure — it's never been switched off.")},
        {"svg": P2, "alt": ("먼지 쌓인 예비 발전기와, 마지막 점검일도 기억 안 나는 점검 기록, 걱정하는 정비사", "A dusty spare generator and a check log that can't even recall the last inspection date; a worried mechanic"),
         "caption": ("안 써본 안전장치는 진짜 비상에 안 될 수도 있어요.", "A safety net you've never tested might fail when you need it most."),
         "small": ("먼지만 쌓인 채, 마지막으로 켜본 날도 기억이 안 나요.", "It's just gathering dust — no one even remembers when it was last turned on.")},
        {"svg": P3, "hero": True, "alt": ("정비사가 운영 중인 기구 하나를 몰래 꺼보고, 관제실 계기판이 모두 초록으로 돌아와 예비가 이어받았음을 보여줌", "A mechanic secretly switches off a running ride, and the control-room gauges turn all-green, showing the spare took over"),
         "caption": ("평소에 몰래 기구 하나를 꺼봐요 — 예비가 바로 이어받으면 성공이에요.", "Secretly switch one ride off during normal hours — if the spare takes right over, it worked."),
         "small": ("진짜 손님이 있는 시간에, 작게 해봐요.", "Do it small, while real guests are still there."),
         "tricks": (4, [
             (TOGGLE_I, ("일부러 작게 고장을 내봐요", "Cause a small break on purpose"), ("딱 하나만요", "just one thing"), "calm"),
             (LIVE_I, ("진짜 운영 중에 해봐요", "Do it during real operation"), ("테스트 공원 말고요", "not a test park")),
             (GROW_I, ("작게 시작해서 점점 크게", "Start small, then grow it"), ("조금씩 늘려가요", "widen it bit by bit"), "warm"),
             (STOP_I, ("터지면 바로 멈출 준비", "Be ready to stop instantly"), ("되돌릴 수 있게요", "so you can undo it")),
         ])},
        {"svg": P4, "alt": ("전력 계기판 셋: 꺼본다, 예비가 넘겨받는다, 정상으로 확인한다", "Three power gauges: switch it off, the spare takes over, confirmed normal"),
         "caption": ("정비사가 몰래 하나를 꺼보고, 예비가 넘겨받는지 계기판으로 확인해요.", "A mechanic quietly switches one off, then checks the gauge to see if the spare takes over."),
         "small": ("전력이 뚝 떨어졌다가, 예비가 들어오면 다시 올라가요.", "Power drops for a moment, then climbs back once the spare kicks in.")},
        {"svg": P5, "alt": ("왼쪽: 준비 없이 끄면 기구 전체가 다운되고 줄이 멈춤. 오른쪽: 작게, 비상 버튼과 무전기를 갖추고 신중하게 함", "Left: switching off with no plan brings everything down and the line stops. Right: small, with a stop button and a walkie-talkie ready, done carefully"),
         "caption": ("아무 준비 없이 무작정 하면 진짜 사고가 나요.", "Doing it with no plan at all causes a real accident."),
         "small": ("작게, 되돌릴 수 있게, 미리 알리고 해야 해요.", "It has to be small, reversible, and announced ahead of time.")},
    ],
    "summary": (("<b>카오스 엔지니어링</b> = 예비 장치가 <b>진짜 되는지</b> 평소에 <b>작게, 일부러</b> 꺼봐서 확인하는 일.",
                 "<b>Chaos engineering</b> = deliberately causing a <b>small, controlled break</b> during normal operation to check whether your backups <b>actually work</b>."),
                ("Chaos Engineering. 시스템에 일부러 장애를 주입해 설계한 대로 버티는지 확인하는 방법이에요. 가설을 세우고(이 정도는 버틸 거다), 블라스트 반경을 작게 제한하고, 실제 운영 환경에서 점진적으로 범위를 넓혀요. 정기적으로 하면 게임 데이가 돼요.",
                 "Chaos engineering deliberately injects failure into a system to confirm it holds up the way it was designed to. You form a hypothesis (\"it should survive this\"), keep the blast radius small, and widen the scope gradually in the real production environment. Doing it on a regular schedule becomes a game day.")),
    "glossary": [
        ("카오스 엔지니어링", "Chaos Engineering", ("예비 장치가 되는지 몰래 확인하는 일.", "Quietly checking whether your backup actually works."), ("일부러, 작게, 미리 준비해서 해요.", "Done on purpose, small, and planned in advance.")),
        ("장애 주입", "Fault injection", ("일부러 기구 하나를 꺼보는 것.", "Deliberately switching one ride off."), ("카오스 엔지니어링이 하는 바로 그 행동이에요.", "This is the actual act chaos engineering performs.")),
        ("사전 준비된 실험", "A planned experiment", ("무작정이 아니라 미리 짜둔 실험.", "Not random — an experiment planned ahead of time."), ("언제, 무엇을, 얼마나 끌지 미리 정해요.", "Decide in advance when, what, and how long.")),
        ("가설 검증", "Hypothesis testing", ("\'이 정도는 버틸 거다\'를 확인하는 일.", "Confirming the belief that \"it should survive this.\""), ("틀렸다면 그게 바로 수확이에요.", "If you're wrong, that's the real payoff.")),
        ("블라스트 반경 제한", "Limiting the blast radius", ("작게 시작해서 점점 키우는 것.", "Starting small and widening it gradually."), ("한 번에 공원 전체를 꺼보지 않아요.", "You never switch off the whole park at once.")),
        ("게임 데이와의 관계", "Relation to game days", ("미리 날짜 잡고 다 같이 하는 연습.", "A scheduled drill everyone does together."), ('정기적으로 하면 게임 데이가 돼요. → <a href="gameday-ko.html">가짜 화재 훈련일</a>', 'Doing it on a regular schedule becomes a game day. → <a href="gameday-en.html">a fake fire drill day</a>')),
        ("장애 조치", "Failover", ("예비가 넘겨받는 바로 그 동작.", "The very act of the spare taking over."), ("카오스 엔지니어링은 이게 진짜 되는지 확인하는 거예요.", "Chaos engineering is how you confirm this actually works.")),
        ("복원력 검증", "Resilience verification", ("\'버틸 거다\'가 아니라 \'버텼다\'로 바꾸는 일.", "Turning \"it should survive\" into \"it did survive.\""), ('말로만 하는 약속과 달라요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Different from a promise made only in words. → <a href="reliability-en.html">the people who keep the park open</a>')),
    ],
}
