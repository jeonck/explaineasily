from _draw import *
from _world import *

# 1. 주방마다 제각각 — 사고가 나면 누구 책임인지 몰라요
P1 = svg(300, sky(300)
         + person(100, 160, s=0.6, face=EYES, **CHEF) + label(100, 250, "⟦1호 주방|kitchen #1⟧", 11, "var(--muted)")
         + person(260, 160, s=0.6, face=SMILE, **CHEF) + label(260, 250, "⟦2호 주방|kitchen #2⟧", 11, "var(--muted)")
         + person(420, 160, s=0.6, face=FROWN, **CHEF) + label(420, 250, "⟦3호 주방|kitchen #3⟧", 11, "var(--muted)")
         + dish(420, 230, 0.5, bad=True)
         + bell(560, 150, 0.8, ringing=True)
         + label(610, 230, "⟦이 사고, 누구 책임이죠?|whose fault is this, exactly?⟧", 12, "var(--bad)", cls="d")
         + label(380, 25, "⟦주방마다 각자 다른 방식으로 손님을 받아요|each kitchen takes guests its own way⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 글로 적힌 공통 규칙이 없으면, 누가 결정하고 누가 책임지는지 매번 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.75, face=EYES, **MANAGER) + label(140, 240, "⟦이건 내가 정했나…?|did I decide this…?⟧", 11, "var(--muted)")
         + person(380, 150, s=0.75, face=EYES, **CHEF) + label(380, 240, "⟦일단 하고 나중에 물어보죠|just do it, ask later⟧", 11, "var(--muted)")
         + person(600, 150, s=0.75, face=FROWN, **INSPECTOR) + label(600, 240, "⟦기준이 주방마다 달라요|the standard is different in every kitchen⟧", 11, "var(--muted)")
         + label(380, 280, "⟦글로 적힌 공통 규칙이 없으면, 결정과 책임이 매번 달라져요|without a written common rule, who decides and who's responsible keeps changing⟧", 12, "var(--bad)", cls="d"))

# 3. 주방 규칙판 = 조직이 AI를 어떻게 쓰고 다루는지 정한 정책·책임 체계 (hero)
P3 = svg(360, sky(360)
         + board(210, 30, 340, 290, "⟦주방 규칙판|KITCHEN RULES BOARD⟧",
                 ("⟦누가 승인하나|who approves⟧",
                  "⟦언제 사람이 확인하나|when a person checks⟧",
                  "⟦사고 나면 누가 책임지나|who's responsible if it breaks⟧",
                  "⟦얼마나 자주 점검하나|how often it's reviewed⟧"), 1.0)
         + person(90, 220, s=0.7, face=SMILE, **MANAGER)
         + person(660, 220, s=0.6, face=EYES, **CHEF)
         + label(380, 25, "⟦주방 규칙판 = AI를 어떻게 쓰고 다루는지 정한 정책·책임 체계예요|a kitchen rules board sets the whole policy and accountability system for how AI is used⟧", 13, "var(--ink)", cls="d"))

# 4. 규칙판 한 장이 여러 장치를 묶어요
P4 = svg(320, sky(320)
         + board(30, 30, 210, 240, "⟦규칙판|RULES BOARD⟧",
                 ("⟦사람 승인 단계|human approval gate⟧",
                  "⟦레드팀 일정|red team schedule⟧",
                  "⟦사고 대응 절차|incident procedure⟧",
                  "⟦감사 로그 보관|audit log retention⟧"), 1.0)
         + person(320, 130, s=0.6, face=EYES, **RUNNER) + ticket(380, 170, 0.5)
         + label(320, 230, "⟦승인 단계|approval gate⟧", 10, "var(--muted)")
         + person(480, 130, s=0.6, face=EYES, **INSPECTOR) + badge(515, 100, 0.5)
         + label(480, 230, "⟦레드팀|red team⟧", 10, "var(--muted)")
         + bell(620, 150, 0.6) + logbook(640, 190, 0.55)
         + label(650, 270, "⟦사고 대응·감사|incident · audit⟧", 10, "var(--muted)")
         + label(380, 300, "⟦각 장치는 따로 쓰이지만, 규칙판이 전부를 하나로 묶어요|each piece works on its own, but the board ties them all together⟧", 12, "var(--ink)"))

# 5. 규칙판이 있어도, 안 지키면 소용없어요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + board(60, 50, 270, 180, "⟦규칙판 — 벽에 걸려 있음|RULES BOARD — ON THE WALL⟧", ("⟦결제는 항상 승인받기|always get approval to pay⟧",))
         + person(150, 250, s=0.6, face=SMILE, **MANAGER) + label(150, 300, "⟦지키면 작동해요|it works when it's followed⟧", 11, "var(--ink)")
         + person(560, 150, s=0.7, face=FROWN, **CHEF)
         + label(560, 230, "⟦규칙판을 안 보고 그냥 결제했어요|didn't look at the board, just paid⟧", 11, "var(--bad)")
         + label(380, 300, "⟦이웃 나라 규칙 검사관처럼, 규칙판도 실제로 지켜지는지 계속 확인해야 해요|like the inspector from the neighboring kingdom, the board also needs ongoing checks that it's actually followed⟧", 12, "var(--ink)", cls="d"))

WHO_I = icon('<circle cx="22" cy="22" r="10" fill="var(--accent)"/><rect x="10" y="36" width="24" height="18" rx="6" fill="var(--accent)"/><path d="M38 20 h18 M38 28 h18" stroke="var(--muted)" stroke-width="3"/>')
GATE2_I = icon('<rect x="14" y="26" width="36" height="26" rx="4" fill="var(--good)"/><path d="M20 26 v-6 a12 12 0 0 1 24 0 v6" fill="none" stroke="var(--good)" stroke-width="5"/>')
BELL_I = icon('<path d="M14 44 a18 18 0 0 1 36 0 Z" fill="var(--bad)"/><rect x="10" y="42" width="44" height="7" rx="3" fill="#8B5E3C"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 18 v14 l12 6" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "aigovernance", "order": 29,
    "title": ("주방 규칙판", "The Kitchen Rules Board"),
    "h1": ("<em>AI 거버넌스</em>가 뭐예요?", "What is <em>AI Governance</em>?"),
    "sub": ("AI 거버넌스를, 여러 주방이 AI를 어떻게 쓰고 다룰지 함께 적어 둔 규칙판 이야기로 풀어봤어요.",
            "AI governance, told as a story about a rules board that several kitchens share — spelling out how AI gets used and handled."),
    "panels": [
        {"svg": P1, "alt": ("세 주방이 각자 다른 방식으로 손님을 받고, 3호 주방에서 사고가 나자 비상벨이 울리지만 누구 책임인지 모름", "Three kitchens each run their own way; kitchen #3 has an accident, the bell rings, and nobody knows whose fault it is"),
         "caption": ("주방마다 제각각이에요.", "Each kitchen runs its own way."),
         "small": ("사고가 나면, 누구 책임인지도 몰라요.", "And when something goes wrong, nobody knows whose fault it is.")},
        {"svg": P2, "alt": ("사장님은 자신이 정한 게 맞는지 헷갈리고, 주방장은 일단 하고 나중에 묻자고 하고, 검사관은 주방마다 기준이 다르다고 말함", "The owner is unsure what they actually decided, the chef says just do it and ask later, and the inspector notes the standard differs kitchen to kitchen"),
         "caption": ("글로 적힌 공통 규칙이 없으면 매번 달라져요.", "Without a written common rule, it's different every time."),
         "small": ("누가 결정하고 누가 책임지는지가 주방마다, 순간마다 바뀌어요.", "Who decides and who's responsible shifts from kitchen to kitchen, moment to moment.")},
        {"svg": P3, "hero": True, "alt": ("사장님과 주방장 사이에 걸린 큰 규칙판에, 누가 승인하는지·언제 사람이 확인하는지·사고 책임·점검 주기가 적혀 있음", "A large rules board between the owner and the chef lists who approves, when a person checks, who's responsible for incidents, and how often it's reviewed"),
         "caption": ("주방 규칙판 = AI를 어떻게 쓰고 다루는지 정한 정책·책임 체계예요.", "A kitchen rules board is the whole policy and accountability system for how AI gets used and handled."),
         "small": ("한 장의 규칙판에, 승인·확인·책임·점검을 모두 적어 둬요.", "One board, and it spells out approval, checks, responsibility, and review — all in one place."),
         "tricks": (4, [
             (WHO_I, ("누가 승인하나", "Who approves what"), ("결정권을 분명히 적어요", "clearly names the decision-maker"), "calm"),
             (GATE2_I, ("언제 사람이 확인하나", "When a person checks"), ("승인 단계가 언제 켜지는지요", "when the approval gate switches on"), "calm"),
             (BELL_I, ("사고 나면 누가 책임지나", "Who's responsible if it breaks"), ("비상벨 다음에 올 일이에요", "what follows the incident bell"), "warm"),
             (CLOCK_I, ("얼마나 자주 점검하나", "How often it's reviewed"), ("규칙판도 낡을 수 있어요", "the board itself can go stale"), "warm"),
         ])},
        {"svg": P4, "alt": ("규칙판 한 장이 사람 승인 단계, 레드팀 일정, 사고 대응·감사 로그라는 세 가지 장치를 하나로 묶음", "One rules board ties together three devices: the human approval gate, the red team schedule, and incident response plus the audit log"),
         "caption": ("규칙판 한 장이 여러 장치를 묶어요.", "One board ties several devices together."),
         "small": ("승인 단계, 레드팀, 사고 대응, 감사 로그 — 각자 따로 일하지만 규칙판이 전부를 하나로 엮어요.", "The approval gate, the red team, incident response, the audit log — each works on its own, but the board weaves them into one.")},
        {"svg": P5, "alt": ("왼쪽: 사장님이 규칙판을 지켜서 잘 작동함. 오른쪽: 주방장이 규칙판을 안 보고 그냥 결제함", "Left: the owner follows the board and it works. Right: the chef pays without even looking at the board"),
         "caption": ("규칙판이 있어도, 안 지키면 소용없어요.", "Having a board doesn't help if nobody follows it."),
         "small": ('<a href="compliance-ko.html">이웃 나라 규칙 검사관</a>처럼, 실제로 지켜지는지 증거로 계속 확인해야 해요.',
                   'Like the <a href="compliance-en.html">inspector from the neighboring kingdom</a>, it also needs ongoing proof that it\'s actually being followed.')},
    ],
    "summary": (("<b>AI 거버넌스</b> = 이 주방이 AI를 <b>어떻게 쓰고 다룰지</b>, 누가 <b>승인하고 책임지는지</b>를 한 장에 적어 둔 규칙판.",
                 "<b>AI governance</b> is a single rules board that spells out <b>how this kitchen uses and handles AI</b> — who <b>approves it, and who's responsible</b>."),
                ("AI 거버넌스(AI Governance)는 조직이 AI 시스템을 어떻게 개발·배포·운영할지를 정하는 정책과 책임 체계예요. 승인 권한, 사람 확인이 필요한 지점, 사고 발생 시 책임 소재, 정기 점검 주기 같은 것들을 명문화해서, 여러 팀·여러 모델에 걸쳐 일관되게 적용되도록 해요. 한 번의 승인 단계 같은 개별 장치를 포함하는, 그보다 더 큰 틀이에요.",
                 "AI governance is the policy and accountability framework an organization uses to decide how it develops, deploys, and operates AI systems. It writes down who has approval authority, where human checks are required, who's accountable when an incident happens, and how often things get reviewed — so it applies consistently across teams and models. It's the larger frame that individual mechanisms, like a single approval gate, live inside.")),
    "glossary": [
        ("AI 거버넌스", "AI governance", ("주방 규칙판.", "The kitchen rules board."), ('이 분야 전체 소개는 여기에. → <a href="llmthreats-ko.html">AI 보안이 뭐예요?</a>', 'The overview of this whole field. → <a href="llmthreats-en.html">What is AI Security?</a>')),
        ("사람 승인 단계", "Human approval gate", ("사장님 최종 승인.", "The owner's final sign-off."), ('규칙판이 포함하는 장치 중 하나예요. → <a href="humanapproval-ko.html">사람 승인 단계가 뭐예요?</a>', 'One device the board decides when to use. → <a href="humanapproval-en.html">What is a human approval gate?</a>')),
        ("규정 준수", "Compliance", ("이웃 나라 규칙 검사관.", "The inspector from the neighboring kingdom."), ('규칙판이 외부 기준과 맞는지 증거로 확인하는 쪽이에요. → <a href="compliance-ko.html">규정 준수가 뭐예요?</a>', 'Checks with evidence that the board matches outside standards. → <a href="compliance-en.html">What is Compliance?</a>')),
        ("AI 레드팀", "AI red team", ("위생 검사관의 불시 방문.", "The inspector's surprise visit."), ("규칙판에 레드팀 일정으로 적혀 있는 바로 그 일이에요. → <a href=\"airedteam-ko.html\">AI 레드팀이 뭐예요?</a>", "Exactly what the board lists as the red team schedule. → <a href=\"airedteam-en.html\">What is an AI Red Team?</a>")),
        ("안전성 평가", "Safety evaluation", ("손님 받기 전 맛 평가 테스트.", "The tasting test before opening."), ('규칙판이 정한 점검 주기마다 다시 돌려요. → <a href="safetyeval-ko.html">안전성 평가가 뭐예요?</a>', 'Re-run on the review cycle the board sets. → <a href="safetyeval-en.html">What is a safety evaluation?</a>')),
        ("비상벨", "The incident bell", ("사고가 났을 때 울리는 벨.", "The bell that rings when something goes wrong."), ("규칙판이 '사고 나면 누가 책임지나'로 적어 둔 그 장면이에요.", "The scene the board writes down as who's responsible if it breaks.")),
        ("주문 기록 장부", "The order logbook", ("감사 로그를 적어 두는 장부.", "The logbook where the audit trail is kept."), ("규칙판이 '얼마나 자주 점검하나'를 확인할 때 펼쳐 보는 장부예요.", "The logbook opened whenever the board's review cycle comes around.")),
        ("최소 권한", "Least privilege", ("필요한 열쇠만 쥐어 주는 것.", "Handing over only the keys that are needed."), ("규칙판이 누가 승인하나를 정하기 전에 먼저 깔아 두는 바닥이에요. → <a href=\"leastprivilege-ko.html\">열쇠 이야기가 뭐예요?</a>", "The groundwork laid before the board even decides who approves. → <a href=\"leastprivilege-en.html\">What is least privilege?</a>")),
    ],
}
