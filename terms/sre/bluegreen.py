from _draw import *
from _world import *

# 1. 기구를 고치는 동안 손님을 못 받아요 (다운타임)
P1 = svg(300, sky(300)
         + ride(200, 260, 0.9, color="var(--stone)", closed=True, label_text="⟦공사중|under repair⟧")
         + queueline(60, 204, 5, 0.5, 28)
         + person(400, 180, s=0.7, face=FROWN + SWEAT, **MANAGER)
         + bubble(340, 90, 210, 46, "⟦지금은 못 타요, 기다리세요|can't ride right now, please wait⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦기구를 고치는 동안 손님을 못 받아요|while fixing the ride, no guests can get on⟧", 12, "var(--ink)"))

# 2. 고치는 중인 기구에 손님을 계속 태울 순 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(300, 230, 0.9, color="var(--stone)", closed=True, label_text="⟦공사중|under repair⟧")
         + person(300, 163, s=0.6, face=EYES, extra=WRENCH, **MECHANIC)
         + bubble(420, 110, 220, 50, "⟦고치는 중인 기구에 태울 순 없어요|can't let guests ride something mid-repair⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(380, 286, "⟦손님을 태운 채로는 못 고쳐요|you can't fix it while guests are still on it⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 쌍둥이 기구, 하나는 운영 하나는 수리
TWIN_I = icon('<rect x="8" y="22" width="20" height="30" rx="3" fill="var(--good)"/><path d="M8 22 Q18 8 28 22Z" fill="var(--good)"/><rect x="36" y="22" width="20" height="30" rx="3" fill="#5B8DEF"/><path d="M36 22 Q46 8 56 22Z" fill="#5B8DEF"/>')
ONE_I = icon('<rect x="8" y="22" width="20" height="30" rx="3" fill="var(--good)"/><path d="M8 22 Q18 8 28 22Z" fill="var(--good)"/><rect x="36" y="22" width="20" height="30" rx="3" fill="var(--stone)"/><path d="M36 22 Q46 8 56 22Z" fill="var(--stone)"/><path d="M38 30 l16 16 M54 30 l-16 16" stroke="var(--bad)" stroke-width="3"/>')
FIX_I = icon('<rect x="18" y="20" width="28" height="34" rx="3" fill="var(--stone)"/><g transform="translate(40,44) rotate(-30)"><rect x="-3" y="0" width="6" height="22" rx="2" fill="#5A3B22"/><circle cy="-4" r="6" fill="none" stroke="#5A3B22" stroke-width="3"/></g>')
SWITCH_I = icon('<rect x="8" y="26" width="48" height="12" rx="6" fill="var(--stone)"/><circle cx="44" cy="32" r="10" fill="var(--good)"/><path d="M44 14 l6 8 h-12z" fill="var(--accent)"/>')

P3 = svg(340, sky(340)
         + ride(220, 300, 0.85, color="var(--good)", label_text="⟦초록, 운영 중|green, taking guests⟧")
         + queueline(70, 250, 4, 0.45, 26)
         + ride(560, 300, 0.85, color="#5B8DEF", closed=True, label_text="⟦파랑, 고치는 중|blue, under repair⟧")
         + person(560, 233, s=0.6, face=EYES, extra=WRENCH, **MECHANIC)
         + label(380, 30, "⟦쌍둥이 기구를 번갈아 운영해요|running twin rides, one at a time⟧", 14, "var(--ink)", cls="d")
         + label(380, 328, "⟦한쪽이 손님을 받는 동안 다른 쪽을 통째로 고쳐요|while one takes guests, the other gets fully repaired⟧", 12, "var(--muted)"))

# 4. 전환 전 / 전환 후 — 화살표만 바꾸면 끝
P4 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + ride(110, 260, 0.6, color="var(--good)") + queueline(150, 215, 3, 0.4, 22)
         + ride(280, 260, 0.5, color="#5B8DEF", closed=True)
         + label(190, 60, "⟦전환 전: 초록이 손님을 받아요|before: green takes the guests⟧", 12, "var(--ink)")
         + ride(500, 260, 0.6, color="#5B8DEF") + queueline(540, 215, 3, 0.4, 22)
         + ride(660, 260, 0.5, color="var(--good)", closed=True)
         + '<path d="M300 150 L460 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M450 143 L460 150 L450 157" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(570, 60, "⟦전환 후: 파랑이 손님을 받아요|after: blue takes the guests⟧", 12, "var(--ink)")
         + label(380, 286, "⟦안내 화살표만 바꾸면 전환 끝이에요|just flip the sign, and the switch is done⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 기구 두 대는 비용 두 배, 명부 차이는 조심
P5 = svg(300, sky(300, ground=False)
         + ride(150, 220, 0.55, color="var(--good)") + ride(230, 220, 0.5, color="#5B8DEF")
         + label(190, 260, "⟦기구 두 대 = 비용 두 배|two rides = double the cost⟧", 12, "var(--bad)")
         + board(430, 40, 260, 150, "⟦손님 명부|GUEST LOG⟧", ("⟦초록 쪽 기록: 120명|green's log: 120 guests⟧", "⟦파랑 쪽 기록: 없음|blue's log: none yet⟧", "⟦전환 전에 맞춰야 해요|must sync before switching⟧"), 0.9)
         + label(380, 286, "⟦되돌리긴 쉬워도, 그 사이 쌓인 명부 차이는 조심해야 해요|switching back is easy — but watch for the log gap that built up meanwhile⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "bluegreen", "order": 36,
    "title": ("쌍둥이 기구를 번갈아 운영", "Running Twin Rides, One at a Time"),
    "h1": ("<em>블루-그린 배포</em>가 뭐예요?", "What is <em>Blue-Green Deployment</em>?"),
    "sub": ("블루-그린 배포를 쌍둥이 기구를 번갈아 운영하는 이야기로 풀어봤어요.",
            "Blue-green deployment, told as a story about two identical rides, taking turns."),
    "panels": [
        {"svg": P1, "alt": ("기구가 공사중 팻말을 걸고 닫혀 있고, 대기줄이 길게 늘어서 공원장이 손님에게 양해를 구함", "A ride hangs an under-repair sign while a line grows and the manager asks guests to wait"),
         "caption": ("기구를 고치는 동안 손님을 못 받아요.", "While fixing the ride, no guests can get on."),
         "small": ("고치는 시간만큼은 꼼짝없이 문을 닫아야 해요.", "For as long as the repair takes, the ride simply has to stay closed.")},
        {"svg": P2, "alt": ("정비사가 공사중인 기구를 고치며, 고치는 중인 기구에 손님을 태울 순 없다는 말풍선이 붙음", "A mechanic works on a closed ride, with a speech bubble saying you can't let guests ride mid-repair"),
         "caption": ("고치는 중인 기구에 손님을 계속 태울 순 없어요.", "You can't keep letting guests ride something that's mid-repair."),
         "small": ("손님을 태운 채로 고치는 건 더 위험해요.", "Fixing it while guests are still riding is even more dangerous.")},
        {"svg": P3, "hero": True, "alt": ("똑같이 생긴 기구 두 대 중 초록 기구는 손님을 받고, 파랑 기구는 정비사가 통째로 고치고 있음", "Of two identical rides, the green one takes guests while a mechanic fully repairs the blue one"),
         "caption": ("쌍둥이 기구를 번갈아 운영해요.", "Twin rides, running one at a time."),
         "small": ("한쪽이 손님을 받는 동안, 다른 쪽을 통째로 고쳐요.", "While one takes guests, the other gets fully repaired."),
         "tricks": (4, [
             (TWIN_I, ("똑같은 기구를 두 대 둬요", "Keep two identical rides"), ("처음부터 쌍둥이로", "built as twins from the start"), "calm"),
             (ONE_I, ("한쪽만 손님을 받아요", "Only one takes guests"), ("나머지는 쉬어요", "the other stays idle")),
             (FIX_I, ("안 받는 쪽을 통째로 고쳐요", "Fully repair the idle one"), ("천천히, 제대로", "slowly, and properly"), "warm"),
             (SWITCH_I, ("화살표만 바꾸면 전환 끝", "Flip the arrow, and you're switched"), ("멈추는 시간이 거의 없어요", "almost no downtime")),
         ])},
        {"svg": P4, "alt": ("전환 전엔 초록 기구가 손님 줄을 받고 파랑 기구는 비어 있으며, 전환 후엔 화살표가 바뀌어 파랑 기구가 손님 줄을 받음", "Before the switch, green has the line and blue sits empty; after, the arrow flips and blue takes the line"),
         "caption": ("안내 화살표만 바꾸면 전환 끝이에요.", "Flip the sign, and the switch is done."),
         "small": ("초록이 받던 줄이 어느새 파랑으로 가요.", "The line that went to green now heads to blue instead.")},
        {"svg": P5, "alt": ("기구 두 대 유지가 비용 두 배라는 설명과, 초록과 파랑의 손님 명부가 서로 다르다는 안내판", "A note says two rides double the cost, and a board shows green's and blue's guest logs don't match"),
         "caption": ("기구 두 대를 유지하는 건 비용이 두 배예요.", "Keeping two rides running costs twice as much."),
         "small": ("되돌리긴 쉬워도, 그 사이 쌓인 손님 명부 차이는 조심해야 해요.", "Switching back is easy — but the guest-log gap that built up in between needs care.")},
    ],
    "summary": (("<b>블루-그린 배포</b> = 똑같은 기구 <b>두 대를 두고</b>, 한쪽이 손님을 받는 동안 다른 쪽을 <b>통째로 고친 뒤</b> 안내 화살표만 바꿔 <b>멈추지 않고 전환</b>하는 요령.",
                 "<b>Blue-green deployment</b> = keeping <b>two identical rides</b>, fully repairing the idle one while the other keeps taking guests, then <b>switching with no downtime</b> by just flipping the sign."),
                ("운영 환경(블루)과 똑같은 새 환경(그린)을 통째로 하나 더 준비해 전부 테스트한 뒤, 트래픽을 한 번에 넘기는 배포 방식이에요. 문제가 생기면 화살표를 원래대로 돌리기만 하면 즉시 되돌아가요.",
                 "A deployment strategy that prepares a whole second environment identical to the live one, tests it fully, and then switches all traffic over at once. If something goes wrong, flipping the arrow back reverts it instantly.")),
    "glossary": [
        ("블루-그린 배포", "Blue-green deployment", ("쌍둥이 기구를 번갈아 운영하는 일.", "Running twin rides, one at a time."), ("한쪽은 운영, 한쪽은 수리 — 역할을 번갈아요.", "One serves, one's repaired — the roles swap.")),
        ("무중단 배포", "Zero-downtime deployment", ("멈추는 시간이 거의 없는 배포.", "A deployment with almost no downtime."), ("손님은 전환을 눈치채지 못해요.", "Guests barely notice the switch happening.")),
        ("전환(스위치오버)", "Switchover", ("안내 화살표를 바꾸는 순간.", "The moment the sign gets flipped."), ("이 한 번으로 모든 손님이 새 쪽으로 가요.", "One flip sends every guest to the new side.")),
        ("즉시 롤백", "Instant rollback", ("화살표를 원래대로 되돌리는 일.", "Flipping the sign back to where it was."), ('되돌리기가 카나리보다 훨씬 간단해요. → <a href="rollback-ko.html">이상하면 바로 어제 버전으로</a>', '<a href="rollback-en.html">Reverting is much simpler than with a canary</a>')),
        ("카나리와의 차이", "vs. canary", ("전부 바꾸느냐, 일부만 먼저 보느냐.", "Switching everything, versus showing it to a few first."), ('카나리는 1%부터 늘려가요. → <a href="canary-ko.html">구석에서 몰래 하는 시험 운행</a>', '<a href="canary-en.html">Canary starts at 1% and grows from there</a>')),
        ("다운타임", "Downtime", ("손님을 못 받는 시간.", "Time when no guests can get on."), ("블루-그린은 이 시간을 거의 없애요.", "Blue-green cuts this down to almost nothing.")),
        ("쌍둥이 환경 비용", "Twin-environment cost", ("기구를 두 대 유지하는 돈.", "The cost of keeping two rides running."), ("항상 두 배의 자리와 인력이 들어요.", "It always takes double the space and staff.")),
        ("롤백", "Rollback", ("이상하면 바로 어제 버전으로.", "Back to yesterday's version, right away."), ('→ <a href="rollback-ko.html">이상하면 바로 어제 버전으로</a>', '→ <a href="rollback-en.html">back to yesterday\'s version, fast</a>')),
    ],
}
