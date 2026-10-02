from _draw import *
from _world import *

# 1. 기구마다 몇 대씩 운영할지, 사람이 수첩에 적어가며 정해요
P1 = svg(300, sky(300)
         + ride(120, 260, 0.85, color="var(--accent)", label_text="⟦기구A|ride A⟧")
         + ride(230, 260, 0.85, color="var(--accent)")
         + board(360, 30, 260, 140, "⟦수첩|NOTEBOOK⟧", ("⟦기구A: 2대 켜야 함|ride A: keep 2 running⟧", "⟦기구B: 1대|ride B: 1⟧", "⟦기구C: 몇 대였더라...|ride C: how many was it...⟧"), 1.0)
         + person(430, 260 - 112 * 0.6, s=0.6, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + label(380, 282, "⟦기구마다 몇 대씩 켤지, 사람이 수첩에 적어가며 정해요|for every ride, someone decides how many to run — by hand, in a notebook⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 기구가 수십 종류, 수백 대면 사람이 다 못 챙겨요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + ride(70, 260, 0.45, color="var(--accent)") + ride(140, 260, 0.45, color="#5B8DEF") + ride(210, 260, 0.45, color="#2E7D6B")
         + ride(280, 260, 0.45, color="#E9B44C") + ride(350, 260, 0.45, color="var(--accent)") + ride(420, 260, 0.45, color="#5B8DEF")
         + person(570, 260 - 112 * 0.75, s=0.75, face=FROWN + SWEAT, extra=CLIPBOARD, **MECHANIC)
         + bubble(470, 70, 240, 58, "⟦기구가 수십 종류, 수백 대면... 저 혼자 다 못 챙겨요|dozens of ride types, hundreds of units... I can\'t keep up alone⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦기구가 수십 종류, 수백 대면 사람이 다 못 챙겨요|with dozens of ride types and hundreds of units, no one person can keep up⟧", 12, "var(--ink)"))

# 3. hero: 규칙판 하나만 주면, 하나가 죽어도 자동으로 새로 세우고 자리도 배정해요
P3 = svg(340, sky(340)
         + board(30, 30, 210, 110, "⟦규칙판|RULE BOARD⟧", ("⟦기구A: 항상 3대|ride A: always 3⟧",), 1.0)
         + controlroom(590, 30, 140, 90, bars=((0.6, "var(--good)"), (0.6, "var(--good)"), (0.6, "var(--good)")))
         + '<path d="M245 95 Q420 60 585 80" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(320, 280, 0.65, color="var(--accent)")
         + ride(400, 280, 0.65, color="var(--accent)", closed=True, label_text="⟦고장|broken⟧")
         + ride(480, 280, 0.65, color="var(--accent)")
         + '<path d="M420 230 Q520 170 605 215" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(610, 280, 0.55, color="var(--accent)", label_text="⟦새로 섬!|just restarted!⟧")
         + person(700, 280 - 112 * 0.5, s=0.5, face=EYES, **OPERATOR)
         + label(380, 175, "⟦규칙판 하나만 주면, 하나가 죽어도 자동으로 새로 세우고 자리도 배정해요|give it one rule board, and it restarts a dead one and places it — automatically⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦사람은 규칙만 바꾸면 끝이에요|all a person does is change the rule⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 1대가 꺼지면 바로 새 1대가 자리를 잡고 서요
P4 = svg(320, sky(320)
         + board(30, 110, 190, 90, "⟦규칙|RULE⟧", ("⟦기구A: 항상 3대 유지|ride A: always keep 3⟧",), 1.0)
         + ride(300, 260, 0.6, color="var(--accent)") + ride(370, 260, 0.6, color="var(--accent)") + ride(440, 260, 0.6, color="var(--accent)", closed=True, label_text="⟦방금 꺼짐|just died⟧")
         + '<path d="M250 150 L300 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M440 220 Q540 150 610 220" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(610, 260, 0.6, color="var(--accent)", label_text="⟦빈 자리에 새로 섬|new one takes the open spot⟧")
         + label(380, 300, "⟦1대가 꺼지면, 본부가 바로 빈 자리에 새 1대를 세워요|when one dies, the operations center stands up a new one in the open spot right away⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 본부 자체가 복잡한 시스템 — 작은 공원엔 오히려 과해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + ride(150, 240, 0.65, color="var(--accent)") + ride(230, 240, 0.65, color="#5B8DEF")
         + person(80, 240 - 112 * 0.6, s=0.6, face=SMILE, **MECHANIC)
         + label(190, 268, "⟦기구 2대뿐이면, 사람이 더 빨라요|with only 2 rides, a person is faster⟧", 11, "var(--ink)")
         + controlroom(480, 40, 220, 120, bars=((0.4, "var(--accent)"), (0.7, "var(--accent)"), (0.3, "var(--accent)"), (0.6, "var(--accent)")))
         + person(560, 200, s=0.6, face=FROWN + SWEAT, **MECHANIC) + bubble(590, 160, 170, 50, "⟦본부 쓰는 법부터 배워야...|first I have to learn the center itself...⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(590, 280, "⟦본부 자체가 복잡한 시스템이에요|the operations center is itself a complex system⟧", 11, "var(--ink)"))

RULE_I = icon('<rect x="12" y="6" width="40" height="52" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="2" width="20" height="8" rx="2" fill="#C9A86A"/><text x="32" y="42" font-size="24" font-weight="800" text-anchor="middle" fill="var(--accent)">3</text>')
AUTOFIX_I = icon('<path d="M44 32 a12 12 0 1 1 -4 -9" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 12 l6 10 -12 2z" fill="var(--good)"/><path d="M14 44 h14 v-14" stroke="var(--bad)" stroke-width="4" fill="none"/>')
SLOT_I = icon('<rect x="8" y="14" width="18" height="18" rx="3" fill="var(--good)"/><rect x="30" y="14" width="18" height="18" rx="3" fill="var(--good)"/><rect x="8" y="36" width="18" height="18" rx="3" fill="var(--good)"/><rect x="30" y="36" width="18" height="18" rx="3" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/>')
KNOB_I = icon('<circle cx="32" cy="36" r="18" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="29" y="10" width="6" height="16" rx="2" fill="var(--accent)"/><circle cx="32" cy="36" r="5" fill="var(--accent)"/>')

PAGE = {
    "slug": "orchestration", "order": 31,
    "title": ("몇 대를 켤지 정하는 운영 본부", "The Operations Center That Decides How Many to Run"),
    "h1": ("<em>오케스트레이션</em>이 뭐예요?", "What is <em>Orchestration</em>?"),
    "sub": ("오케스트레이션을 기구마다 몇 대씩 운영할지 정해 주는 공원 운영 본부 이야기로 풀어봤어요.",
            "Orchestration, told as a story about an operations center that decides how many of each ride to run."),
    "panels": [
        {"svg": P1, "alt": ("기구 두 대 옆에서 정비사가 클립보드를 들고, 수첩에는 기구마다 몇 대씩 켜야 하는지 적혀 있음", "A mechanic holds a clipboard beside two rides; a notebook lists how many of each ride should be running"),
         "caption": ("기구마다 몇 대씩 켤지, 사람이 수첩에 적어가며 정해요.", "For every ride, someone decides how many to run, by hand."),
         "small": ("하나 고장 나면 새로 세울지도 사람이 그때그때 결정해요.", "And when one breaks, a person decides on the spot whether to stand up a new one.")},
        {"svg": P2, "alt": ("작은 기구 여섯 종류가 늘어서 있고, 땀 흘리는 정비사가 클립보드를 들고 혼자 다 못 챙긴다고 말함", "Six small ride types lined up, with a sweating mechanic holding a clipboard saying he can't keep up alone"),
         "caption": ("기구가 수십 종류, 수백 대면 사람이 다 못 챙겨요.", "With dozens of ride types and hundreds of units, no one person can keep up."),
         "small": ("수첩 한 권으로는 규모가 커지면 금방 한계가 와요.", "One notebook runs out of room fast once things grow.")},
        {"svg": P3, "hero": True, "alt": ("규칙판에 '기구A 항상 3대'라고 적혀 있고, 가운데 고장 난 기구 옆에 새 기구가 자동으로 서는 모습. 관제실이 전부 초록불로 지켜봄", "A rule board says ride A always 3; beside a broken ride a new one rises automatically, while the control room watches all green"),
         "caption": ("규칙판 하나만 주면, 하나가 죽어도 자동으로 새로 세우고 자리도 배정해요.", "Give it one rule board, and it restarts a dead one and places it — automatically."),
         "small": ("사람은 규칙만 바꾸면 끝이에요.", "All a person does is change the rule."),
         "tricks": (4, [
             (RULE_I, ("몇 대씩 규칙만 정해요", "Just set the \"how many\" rule"), ("숫자 하나면 충분해요", "one number is enough"), "calm"),
             (AUTOFIX_I, ("죽으면 자동으로 새로 세워요", "Restarts a dead one automatically"), ("사람이 안 봐도요", "even without anyone watching")),
             (SLOT_I, ("자리도 알아서 배정해요", "Places it automatically, too"), ("어느 구역인지도 정해요", "picks which spot it goes in"), "warm"),
             (KNOB_I, ("사람은 규칙만 바꾸면 돼요", "A person just turns the dial"), ("나머지는 본부가 해요", "the center handles the rest")),
         ])},
        {"svg": P4, "alt": ("규칙: 기구A 항상 3대 유지. 기구 세 대 중 하나가 방금 꺼지고, 화살표가 빈 자리로 이어져 새 기구가 바로 섬", "Rule: ride A always keep 3. One of three rides just died, and an arrow leads to a new one rising in the open spot"),
         "caption": ("1대가 꺼지면, 본부가 바로 빈 자리에 새 1대를 세워요.", "When one dies, the operations center stands up a new one in the open spot right away."),
         "small": ("규칙에 적힌 숫자를 다시 채울 때까지 멈추지 않아요.", "It keeps going until the number in the rule is met again.")},
        {"svg": P5, "alt": ("왼쪽: 기구 2대뿐인 작은 공원에서 정비사가 웃으며 직접 관리. 오른쪽: 복잡한 관제실 앞에서 정비사가 당황하며 본부 쓰는 법부터 배워야 한다고 말함", "Left: a small park with just 2 rides, a mechanic smiling and managing directly. Right: a flustered mechanic in front of a complex control room, saying he has to learn the center itself first"),
         "caption": ("본부 자체가 복잡한 시스템이에요.", "The operations center is itself a complex system."),
         "small": ("작은 공원엔 오히려 과해요 — 기구 몇 대 안 되면 사람이 더 빨라요.", "For a small park it's overkill — with just a few rides, a person is faster.")},
    ],
    "summary": (("<b>오케스트레이션</b> = \"이 기구는 항상 몇 대\" <b>규칙만 정해 두면</b>, <b>하나가 죽어도 자동으로 새로 세우고</b> <b>자리까지 알아서 배정</b>해 주는 운영 본부.",
                 "<b>Orchestration</b> = an operations center that, once you <b>set a \"keep this many running\" rule</b>, <b>restarts a dead one automatically</b> and <b>places it for you, too</b>."),
                ("컨테이너 오케스트레이션(대표적으로 쿠버네티스)을 가리켜요. 선언적 설정으로 '원하는 상태'만 적어 두면, 오케스트레이터가 실제 상태를 그 목표에 계속 맞춰요. 자동 재시작, 스케줄링(배치), 오토스케일링, 롤링 업데이트가 전부 이 위에서 돌아가요.",
                 "Refers to container orchestration — Kubernetes being the best-known example. You write down only the \"desired state\" as declarative config, and the orchestrator keeps nudging reality toward that goal. Auto-restart, scheduling, autoscaling, and rolling updates all run on top of this.")),
    "glossary": [
        ("오케스트레이션", "Orchestration", ("운영 본부가 기구를 알아서 관리하는 일.", "The operations center managing rides on its own."), ("규칙만 주면 나머지는 본부가 해요.", "Give it a rule, and it handles the rest.")),
        ("컨테이너", "Container", ("기구 한 대를 똑같이 포장해 둔 것.", "One ride, packaged identically every time."), ('성 세계에서는 짐칸이라고 불러요. → <a href="container-ko.html">똑같이 찍어낸 짐칸</a>', 'In the castle world, this is called a crate. → <a href="container-en.html">crates from the same mold</a>')),
        ("선언적 설정", "Declarative config", ("\"기구A: 3대\" 같은 규칙판.", "A rule board like \"ride A: 3\"."), ("방법이 아니라 원하는 결과만 적어요.", "You write the desired result, not the steps to get there.")),
        ("자동 재시작", "Auto-restart", ("죽은 기구를 알아서 새로 세우는 일.", "Standing up a dead ride automatically."), ("사람이 호출받을 필요가 줄어들어요.", "Cuts down on how often a person needs to be paged.")),
        ("스케줄링", "Scheduling", ("새 기구가 어느 자리에 설지 정하는 일.", "Deciding which spot a new ride goes in."), ("빈자리를 본부가 알아서 골라요.", "The center picks the open spot on its own.")),
        ("오토스케일링", "Autoscaling", ("줄이 길어지면 대수를 더 늘리는 일.", "Adding more units when the line grows."), ("규칙판의 숫자 자체가 자동으로 바뀌는 것뿐이에요.", "It's just the number on the rule board changing itself.")),
        ("롤링 업데이트", "Rolling update", ("기구를 하나씩 순서대로 새 버전으로 바꾸는 일.", "Swapping rides to a new version one at a time."), ("이상하면 이전 버전으로 되돌려요.", "If it goes wrong, it rolls back to the old version.")),
        ("헬스 체크", "Health check", ("기구가 살아 있는지 주기적으로 찔러 보는 일.", "Periodically poking a ride to see if it's still alive."), ("여기서 멈추면 본부가 고장으로 판단해요.", "Fail this, and the center decides the ride is broken.")),
    ],
}
