from _draw import *
from _world import *

# 1. 사고가 터졌을 때 — 다들 처음 해보는 것처럼 허둥대요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(150, 230, 0.85, color="var(--stone)", closed=True, label_text="⟦고장!|broken!⟧")
         + person(300, 160, s=0.65, face=FROWN + SWEAT, **OPERATOR) + walkie(340, 135, 0.6)
         + bubble(330, 70, 220, 54, "⟦누구한테 연락하지?!|who do I even call?!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(500, 170, s=0.6, face=FROWN + SWEAT, **MECHANIC)
         + bubble(530, 90, 200, 54, "⟦이거 처음 보는 화면인데요?|I\'ve never seen this screen before?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사고가 터지면 다들 처음 해보는 것처럼 허둥대요|when the real thing hits, everyone fumbles like it\'s their first time⟧", 12, "var(--bad)", cls="d"))

# 2. 왜: 실제 사고 때 처음 해보면 다들 느리고 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(60, 40, 300, 160, "⟦첫 대응 기록|FIRST RESPONSE LOG⟧", ("⟦연락하는 데 20분|20 min just to reach someone⟧", "⟦지휘자 못 정해 10분|10 min not naming a commander⟧", "⟦대응 매뉴얼 어딨지?|where\'s the manual?⟧"), 1.0)
         + person(480, 160, s=0.7, face=FROWN + SWEAT, **MANAGER)
         + bubble(500, 60, 220, 54, "⟦처음 해보면 다 느리고 틀려요|doing it for the first time means slow and wrong⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦연습 안 해본 걸 진짜 사고 때 처음 해보면 늦어요|if you\'ve never practiced, doing it for the first time during a real incident is too slow⟧", 12, "var(--bad)", cls="d"))

# 3. hero: 날을 잡아서 다 같이, 진짜처럼 연습해요
CALENDAR_I = icon('<rect x="10" y="14" width="44" height="40" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="10" y="14" width="44" height="12" fill="var(--accent)"/><circle cx="32" cy="38" r="6" fill="var(--bad)"/>')
SCRIPT_I = icon('<rect x="16" y="10" width="32" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
RING_I = icon('<rect x="22" y="14" width="20" height="36" rx="4" fill="var(--stone-dark)"/><rect x="26" y="20" width="12" height="8" fill="#5B9BD5"/><path d="M14 14 q-6 -8 0 -14" stroke="var(--bad)" stroke-width="3" fill="none"/><path d="M50 14 q6 -8 0 -14" stroke="var(--bad)" stroke-width="3" fill="none"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M32 18 V33 L44 40" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

P3 = svg(360, sky(360)
         + board(50, 40, 260, 180, "⟦달력|CALENDAR⟧", ("⟦월 화 수 목|MON TUE WED THU⟧", "⟦금: 훈련일!|FRI: DRILL DAY!⟧", "⟦다음 달에도|and next month too⟧"), 1.0, hl=1)
         + person(400, 240, s=0.65, face=EYES, **OPERATOR) + walkie(430, 215, 0.8)
         + person(490, 240, s=0.65, face=EYES, extra=WRENCH, **MECHANIC)
         + person(580, 240, s=0.65, face=EYES, **MANAGER)
         + ride(680, 300, 0.55, color="var(--stone)", closed=True, label_text="⟦(연습) 고장|(drill) broken⟧")
         + label(380, 35, "⟦날을 잡아서 다 같이, 진짜처럼 연습해요|pick a day and practice together, just like the real thing⟧", 14, "var(--ink)", cls="d")
         + label(490, 335, "⟦자, 기구 A가 고장났다고 치고 해봅시다!|alright, let\'s pretend ride A just broke!⟧", 12, "var(--muted)"))

# 4. 달력에 훈련일을 표시하고, 손님은 모르게 다 같이 연습해요
P4 = svg(320, sky(320)
         + board(40, 40, 230, 190, "⟦훈련 안내(내부용)|DRILL NOTICE (internal)⟧", ("⟦이번 금요일|this Friday⟧", "⟦기구 A 고장 가정|assume ride A breaks⟧", "⟦손님께는 비밀|guests won\'t know⟧"), 1.0)
         + ride(400, 260, 0.8, color="var(--accent)") + queueline(330, 208, 3, 0.4, 26)
         + person(560, 190, s=0.65, face=EYES, **OPERATOR) + walkie(600, 170, 0.8)
         + person(640, 200, s=0.6, face=EYES, extra=WRENCH, **MECHANIC)
         + label(380, 300, "⟦달력에 훈련일을 표시하고, 손님은 모르게 다 같이 연습해요|mark the drill day on the calendar and practice together while guests don\'t even notice⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 너무 자주 하면 지치고, 너무 안 하면 효과 없어요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(40, 40, 320, 170, "⟦너무 자주|TOO OFTEN⟧", ("⟦매주 훈련|drilling every week⟧", "⟦다들 지쳐요|everyone gets exhausted⟧"), 1.0)
         + person(140, 190, s=0.5, face=FROWN + SWEAT, **OPERATOR)
         + board(400, 40, 320, 170, "⟦너무 안 함|TOO RARELY⟧", ("⟦1년에 한 번|once a year⟧", "⟦연습한 걸 다 잊어요|everyone forgets the drill⟧"), 1.0)
         + person(650, 190, s=0.5, face=FROWN, **MECHANIC)
         + label(380, 280, "⟦너무 자주 하면 지치고, 너무 안 하면 효과가 없어요 — 적당한 주기가 필요해요|too often exhausts everyone, too rarely loses the effect — you need the right rhythm⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "gameday", "order": 43,
    "title": ("가짜 화재 훈련일", "The Fake Fire-Drill Day"),
    "h1": ("<em>게임 데이</em>가 뭐예요?", "What is a <em>Game Day</em>?"),
    "sub": ("게임 데이를 날을 잡아서 다 같이 가짜 고장을 연습해 보는 이야기로 풀어봤어요.",
            "Game day, told as a story about picking a day and practicing a pretend breakdown together."),
    "panels": [
        {"svg": P1, "alt": ("기구가 고장나자 관제실 요원과 정비사가 누구에게 연락할지, 화면을 어떻게 다룰지 몰라 허둥댐", "A ride breaks down and the operator and mechanic fumble, unsure who to call or how to read the screen"),
         "caption": ("사고가 터지면 다들 처음 해보는 것처럼 허둥대요.", "When the real thing hits, everyone fumbles like it's their first time."),
         "small": ("호출기를 들어도 누구에게 연락할지부터 막막해요.", "Even with the pager in hand, it's not clear who to call.")},
        {"svg": P2, "alt": ("첫 대응 기록판에 연락하는 데 20분, 지휘자 못 정해 10분이 적혀 있고 공원장이 걱정함", "A first-response log shows 20 minutes just to reach someone and 10 minutes spent not naming a commander, while the manager worries"),
         "caption": ("연습 안 해본 걸 진짜 사고 때 처음 해보면 늦어요.", "If you've never practiced, doing it for the first time during a real incident is too slow."),
         "small": ("연락하는 데만 20분, 누가 지휘할지 정하는 데 또 10분이 걸려요.", "20 minutes just to reach someone, another 10 deciding who's in charge.")},
        {"svg": P3, "hero": True, "alt": ("달력에 금요일이 훈련일로 표시되고, 관제실 요원·정비사·공원장이 모여 가짜 고장 시나리오로 연습함", "Friday is marked as drill day on the calendar; the operator, mechanic, and manager gather to practice a pretend breakdown scenario"),
         "caption": ("날을 잡아서 다 같이, 진짜처럼 연습해요.", "Pick a day and practice together, just like the real thing."),
         "small": ("호출기도 진짜처럼 울리고, 지휘자도 정해 세워요.", "The pager rings for real, and someone is named commander."),
         "tricks": (4, [
             (CALENDAR_I, ("날짜를 미리 잡아요", "Pick a date ahead of time"), ("달력에 표시해요", "mark it on the calendar"), "calm"),
             (SCRIPT_I, ("시나리오를 정해요", "Decide the scenario"), ("뭐가 고장난 척 할지요", "what's pretending to break")),
             (RING_I, ("진짜처럼 호출기도 울려요", "Ring the pagers for real"), ("지휘자도 세워요", "and name a commander"), "warm"),
             (CLOCK_I, ("끝나면 느렸는지 기록해요", "Afterward, record what was slow"), ("다음엔 더 빨라져요", "so next time is faster")),
         ])},
        {"svg": P4, "alt": ("내부용 훈련 안내판 옆에서, 손님은 평소처럼 기구를 타는데 요원과 정비사가 몰래 가짜 고장을 연습함", "Beside an internal-only drill notice, guests ride as usual while the operator and mechanic quietly practice the pretend breakdown"),
         "caption": ("달력에 훈련일을 표시하고, 손님은 모르게 다 같이 연습해요.", "Mark the drill day on the calendar and practice together while guests don't even notice."),
         "small": ("훈련인 걸 손님이 알아챌 필요는 없어요.", "Guests don't need to know it's a drill at all.")},
        {"svg": P5, "alt": ("왼쪽: 매주 훈련해서 다들 지친 모습. 오른쪽: 1년에 한 번뿐이라 연습한 걸 다 잊은 모습", "Left: drilling every week leaves everyone exhausted. Right: once a year means everyone's forgotten what they practiced"),
         "caption": ("너무 자주 하면 지치고, 너무 안 하면 효과가 없어요.", "Too often exhausts everyone, too rarely loses the effect."),
         "small": ("적당한 주기를 찾는 게 중요해요.", "Finding the right rhythm matters.")},
    ],
    "summary": (("<b>게임 데이</b> = 날을 잡아 <b>다 같이</b>, <b>진짜처럼</b> 가짜 고장을 연습하고, 끝나면 <b>뭐가 느렸는지</b> 기록하는 날.",
                 "<b>Game day</b> = a scheduled day when the whole team practices a <b>pretend breakdown</b>, as realistically as possible, and afterward records <b>what was slow</b>."),
                ("정해진 시나리오로 모의 장애를 일으키고, 실제 사고 대응 절차(호출, 지휘, 소통)를 그대로 연습하는 훈련이에요. 카오스 엔지니어링을 정기적으로, 팀 전체가 함께 하는 형태로 볼 수 있어요. 너무 잦으면 피로가 쌓이고, 너무 드물면 숙련도가 떨어져 주기 조절이 중요해요.",
                 "A drill that triggers a simulated incident under a planned scenario and rehearses the real response procedures — paging, command, communication — exactly as they'd happen. It can be seen as chaos engineering done on a regular schedule, as a whole team. Too frequent and fatigue builds up; too rare and skills fade, so getting the cadence right matters.")),
    "glossary": [
        ("게임 데이", "Game day", ("미리 날짜 잡고 다 같이 하는 재난 연습.", "A scheduled drill the whole team does together."), ("진짜처럼 하지만 피해는 없어요.", "Just like the real thing, but with no real damage.")),
        ("재해 복구 훈련", "Disaster-recovery drill", ("가짜 화재 훈련일의 다른 이름.", "Another name for the fake fire-drill day."), ('정해진 날, 정해진 시나리오로 연습해요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Practiced on a set day with a set scenario. → <a href="reliability-en.html">the people who keep the park open</a>')),
        ("시나리오 설계", "Scenario design", ("뭐가 고장난 척 할지 미리 정하는 일.", "Deciding in advance what's pretending to break."), ("너무 쉬우면 연습이 안 되고, 너무 어려우면 다쳐요.", "Too easy teaches nothing; too hard and someone gets hurt.")),
        ("역할 연습", "Role rehearsal", ("지휘자, 정비사, 관제실 역할을 미리 맡아보는 것.", "Trying on the commander, mechanic, and operator roles ahead of time."), ("진짜 사고 때 누가 뭘 할지 헷갈리지 않아요.", "So no one's confused about who does what in a real incident.")),
        ("카오스 엔지니어링과의 관계", "Relation to chaos engineering", ("일부러 내는 가짜 고장 그 자체.", "The fake breakdown itself."), ('게임 데이는 이걸 정기적으로, 다 같이 하는 거예요. → <a href="chaosengineering-ko.html">일부러 내는 가짜 고장</a>', 'A game day is doing this on a regular schedule, together. → <a href="chaosengineering-en.html">the fake breakdowns caused on purpose</a>')),
        ("교훈 기록", "Recording the lessons", ("끝나고 뭐가 느렸는지 적어두는 일.", "Writing down afterward what was slow."), ("다음 훈련은 더 나아져요.", "The next drill gets better because of it.")),
        ("복구 시간 측정", "Measuring recovery time", ("연습 중에 얼마나 걸렸는지 재는 것.", "Timing how long the drill took."), ("숫자로 남아야 나아졌는지 알아요.", "You need the number to know if you've improved.")),
        ("런북 점검", "Runbook check", ("정비사의 공책이 실제로 맞는지 훈련 중에 확인하는 일.", "Checking during the drill whether the mechanic's notebook is still accurate."), ("훈련할 때마다 공책도 같이 고쳐요.", "Update the notebook every time you drill.")),
    ],
}
