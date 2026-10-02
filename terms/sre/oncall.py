from _draw import *
from _world import *

# 1. 밤 2시, 기구가 멈췄는데 아무도 몰라요
P1 = svg(320, night(320)
         + controlroom(40, 150, 230, 120, bars=((0.15, "var(--stone)"), (0.1, "var(--stone)"), (0.2, "var(--stone)"), (0.1, "var(--stone)")))
         + walkie(500, 170, 1.1)
         + label(500, 220, "⟦2:00 AM — 아무도 안 받아요|2 AM — no one answers⟧", 11, "#F5E6B8")
         + ride(650, 290, 0.65, color="var(--stone)", closed=True, label_text="⟦고장|broken⟧")
         + label(380, 300, "⟦기구가 멈췄는데 아침까지 아무도 몰라요|the ride stops, and nobody knows until morning⟧", 12, "#F5E6B8", cls="d"))

# 2. 왜: 누가 받을지 안 정하면 다들 내 일이 아니라 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 163, s=0.6, face=EYES, **OPERATOR)
         + bubble(40, 70, 180, 42, "⟦내 차례 아니죠?|not my turn, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 163, s=0.6, face=EYES, **MECHANIC)
         + bubble(290, 70, 180, 42, "⟦제가요? 아닌데요|me? no way⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(630, 163, s=0.6, face=EYES, **ROOKIE)
         + bubble(540, 70, 180, 42, "⟦저도 아니에요|not me either⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦누가 받을지 안 정하면 다들 내 일이 아니라 해요|without an owner, everyone assumes it's someone else's job⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 이번 주엔 한 사람이 호출기를 들고 다녀요
P3 = svg(340, sky(340)
         + '<circle cx="150" cy="150" r="24" fill="#F5C44C"/>'
         + '<circle cx="560" cy="150" r="20" fill="#C9D5E6"/><circle cx="568" cy="144" r="18" fill="var(--sky)"/>'
         + person(300, 220, s=0.9, face=SMILE, extra=walkie(52, 66, 0.55), **OPERATOR)
         + label(380, 28, "⟦이번 주엔 한 사람이 호출기를 들고 다녀요|one person carries the pager this week⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦밤이든 낮이든 울리면 그 사람이 제일 먼저 봐요|day or night, whoever's on call sees it first⟧", 12, "var(--muted)"))

# 4. 당번표 — 한 주씩 돌아가며, 다음 사람에게 넘겨요
P4 = svg(340, sky(340, ground=False)
         + board(50, 40, 280, 200, "⟦당번표|ON-CALL CALENDAR⟧", ("⟦이번 주: 영희|this week: Yeonghui⟧", "⟦다음 주: 철수|next week: Cheolsu⟧", "⟦그 다음 주: 민지|the week after: Minji⟧"), 1.0, hl=0)
         + person(470, 210, s=0.8, face=SMILE, **OPERATOR)
         + walkie(560, 230, 1.0)
         + '<path d="M520 220 L600 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(640, 210, s=0.8, face=SMILE, **ROOKIE)
         + label(380, 325, "⟦한 주가 끝나면 다음 사람에게 넘겨요|when the week ends, it passes to the next person⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳: 너무 자주 울리면 진짜 비상도 놓쳐요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(300, 150, s=0.8, face=FROWN + SWEAT, **OPERATOR)
         + walkie(190, 110, 0.7) + walkie(230, 170, 0.6) + walkie(370, 90, 0.65) + walkie(400, 190, 0.6)
         + walkie(620, 150, 1.0)
         + bubble(500, 70, 200, 44, "⟦이건 진짜 비상인데!|this one's real!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦너무 자주 울리면 진짜 비상도 놓쳐요|too many alerts, and even the real one gets missed⟧", 12, "var(--ink)", cls="d"))

CALENDAR_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="12" width="44" height="12" fill="#C9A86A"/><rect x="18" y="32" width="10" height="10" fill="var(--accent)"/>')
LOUD_I = icon('<rect x="20" y="10" width="20" height="36" rx="4" fill="var(--stone-dark)"/><rect x="24" y="18" width="12" height="8" fill="#5B9BD5"/><path d="M44 18 a16 16 0 0 1 0 20" stroke="var(--bad)" stroke-width="4" fill="none"/>')
ESCALATE_I = icon('<circle cx="18" cy="44" r="8" fill="var(--accent)"/><circle cx="32" cy="28" r="8" fill="var(--good)"/><circle cx="46" cy="12" r="8" fill="var(--bad)"/><path d="M18 44 L32 28 L46 12" stroke="var(--stone-dark)" stroke-width="3" fill="none" stroke-dasharray="4 3"/>')
HANDOVER_I = icon('<rect x="8" y="26" width="20" height="14" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><path d="M28 33 H52" stroke="var(--accent)" stroke-width="4" stroke-dasharray="5 4"/><path d="M46 27 L54 33 L46 39" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "oncall", "order": 38,
    "title": ("이번 주 호출기를 든 사람", "Whoever's Holding the Pager This Week"),
    "h1": ("<em>온콜</em>이 뭐예요?", "What is <em>On-call</em>?"),
    "sub": ("온콜을 이번 주 호출기를 들고 다니는 한 사람 이야기로 풀어봤어요.",
            "On-call, told as a story about the one person carrying the pager this week."),
    "panels": [
        {"svg": P1, "alt": ("밤 2시 기구가 멈췄는데 관제실은 어둡고 호출기를 아무도 받지 않음", "At 2 AM a ride stops, the control room sits dark, and nobody answers the pager"),
         "caption": ("기구가 멈췄는데 아침까지 아무도 몰라요.", "The ride stops, and nobody knows until morning."),
         "small": ("누가 밤에도 받아야 하는지 정해 둔 게 없었어요.", "Nobody had been set to answer, even at night.")},
        {"svg": P2, "alt": ("세 사람이 서로 자기 차례가 아니라고 말함", "Three people each say it isn't their turn"),
         "caption": ("왜 어려운가요?", "Why is this hard?"),
         "small": ("누가 받을지 안 정하면 다들 내 일이 아니라 해요.", "Without an owner, everyone assumes it's someone else's job.")},
        {"svg": P3, "hero": True, "alt": ("해와 달 사이에 선 사람이 웃으며 호출기를 들고 있음", "A person stands smiling with a pager between a sun and a moon"),
         "caption": ("이번 주엔 한 사람이 호출기를 들고 다녀요.", "One person carries the pager this week."),
         "small": ("밤이든 낮이든 울리면 그 사람이 제일 먼저 봐요.", "Day or night, whoever's on call sees it first."),
         "tricks": (4, [
             (CALENDAR_I, ("한 주씩 돌아가며 들어요", "Carry it one week at a time"), ("교대로 돌아가요", "it rotates"), "calm"),
             (LOUD_I, ("급한 것만 울리게 해요", "Only the urgent ones ring"), ("안 그러면 지쳐요", "or you burn out")),
             (ESCALATE_I, ("못 받으면 다음 사람에게", "No answer? It escalates"), ("에스컬레이션이에요", "that's escalation"), "warm"),
             (HANDOVER_I, ("교대할 때 메모를 넘겨요", "Hand over notes at the switch"), ("지난 주 일을 알려줘요", "so they know last week's story")),
         ])},
        {"svg": P4, "alt": ("이름이 매주 바뀌는 당번표 옆에서 한 사람이 다음 사람에게 호출기를 건넴", "Beside a calendar whose name changes each week, one person hands the pager to the next"),
         "caption": ("한 주가 끝나면 다음 사람에게 넘겨요.", "When the week ends, it passes to the next person."),
         "small": ("당번표를 보면 이번 주는 누구인지 바로 알아요.", "The calendar shows at a glance whose week it is.")},
        {"svg": P5, "alt": ("당번이 지친 표정으로 여러 호출기에 둘러싸여 있고, 진짜 비상을 알리는 말풍선은 눈에 안 띔", "The on-call person looks exhausted, surrounded by many pagers, while the one real emergency goes unnoticed"),
         "caption": ("너무 자주 울리면 진짜 비상도 놓쳐요.", "Too many alerts, and even the real one gets missed."),
         "small": ("그래서 뭐가 진짜 울려야 하는지가 중요해요.", "That's why deciding what truly deserves an alert matters.")},
    ],
    "summary": (("<b>온콜</b> = <b>이번 주 호출기를 든 한 사람</b>. 밤이든 낮이든 제일 먼저 보고, <b>한 주씩 교대</b>하며, 못 받으면 <b>다음 사람에게 넘어가요</b>.",
                 "<b>On-call</b> means <b>one person carries the pager</b> for the week — first to see it, day or night, <b>rotating week by week</b>, and <b>escalating to the next person</b> if there's no answer."),
                ("시스템에 문제가 생기면 호출(페이징)을 받는 담당자와 그 교대 체계예요. 알림이 너무 잦으면 알림 피로로 당번이 지쳐 진짜 비상을 놓치므로, 무엇을 울릴지 신중히 고르고 교대할 때 핸드오버 메모를 남겨요.",
                 "The rotation of people who get paged when something breaks. Too many alerts cause alert fatigue, which can bury the real emergency — so teams choose carefully what triggers a page and leave handover notes at every switch.")),
    "glossary": [
        ("온콜", "On-call", ("이번 주 호출기를 든 사람.", "Whoever's holding the pager this week."), ("문제가 생기면 제일 먼저 받아요.", "First to be paged when something breaks.")),
        ("교대 일정", "Rotation schedule", ("한 주씩 돌아가는 당번표.", "The calendar that rotates week by week."), ("누가 이번 주인지 한눈에 보여요.", "Shows at a glance whose week it is.")),
        ("에스컬레이션", "Escalation", ("못 받으면 다음 사람에게 넘어가는 것.", "Passing it to the next person when there's no answer."), ("혼자 다 못 받아도 괜찮아요.", "It's fine if one person can't always answer.")),
        ("알림 피로", "Alert fatigue", ("너무 자주 울려서 지치는 것.", "Being worn out by too many alerts."), ('진짜 비상을 놓치게 만들어요. → <a href="alerting-ko.html">몇 번 울려야 진짜 비상인가</a>', 'It makes the real emergency get missed. → <a href="alerting-en.html">how many rings mean a real emergency</a>')),
        ("핸드오버 메모", "Handover notes", ("교대할 때 넘기는 지난 기록.", "The notes passed along at the switch."), ("지난 주에 무슨 일이 있었는지 알려줘요.", "Tells the next person what happened last week.")),
        ("당직 보상", "On-call compensation", ("당번 선 대가로 받는 것.", "What's paid back for carrying the pager."), ("수당이나 대체 휴무로 돌려줘요.", "Often extra pay or time off in return.")),
        ("호출기", "Paging", ("울려서 부르는 장치.", "The device that rings to call someone."), ("문자·전화·앱 알림 모두 포함해요.", "Covers texts, calls, and app alerts alike.")),
        ("인시던트 커맨더", "Incident commander", ("큰 사고가 나면 지휘봉을 드는 사람.", "Whoever takes charge when it's a big incident."), ('온콜이 받았다가 더 커지면 넘겨요. → <a href="incidentcommand-ko.html">지휘봉을 든 사람</a>', 'On-call hands it off if it grows bigger. → <a href="incidentcommand-en.html">whoever picks up the baton</a>')),
    ],
}
