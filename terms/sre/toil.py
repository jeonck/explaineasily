from _draw import *
from _world import *

# 1. 관제실 요원이 매일 아침 똑같은 보고서를 손으로 옮겨 적어요
P1 = svg(300, sky(300, ground=False)
         + person(150, 160, s=0.7, face=FROWN + SWEAT, **OPERATOR, extra=CLIPBOARD)
         + board(250, 40, 220, 200, "⟦오늘 아침 보고서|TODAY\'S REPORT⟧", ("⟦어제와 똑같음|same as yesterday⟧", "⟦또 손으로 옮겨 적어요|copying it by hand, again⟧", "⟦40분째...|40 minutes in...⟧"), 1.0)
         + "".join(f'<rect x="520" y="{170 - i * 10}" width="140" height="70" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' for i in range(4))
         + label(590, 255, "⟦쌓여만 가요|it just keeps piling up⟧", 11, "var(--muted)")
         + label(380, 280, "⟦관제실 요원이 매일 아침 똑같은 보고서를 손으로 옮겨 적어요|every morning, the operator copies the exact same report by hand⟧", 12, "var(--ink)"))

# 2. 왜: 반복되는 손일이 쌓이면 사람 시간이 거기에 다 잡아먹혀요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(f'<rect x="260" y="{135 - i * 8}" width="140" height="70" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' for i in range(6))
         + person(550, 175, s=0.65, face=FROWN + SWEAT, **OPERATOR)
         + bubble(500, 70, 230, 54, "⟦새 문제를 볼 시간이 없어요|no time left to look at anything new⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦반복되는 손일이 쌓이면, 사람 시간이 거기에 다 잡아먹혀요|when repetitive manual work piles up, it swallows all the time a person has⟧", 12, "var(--bad)", cls="d"))

# 3. hero: 반복되는 건 기계가 하게, 사람은 새 문제에 시간을 써요
FIND_I = icon('<circle cx="26" cy="26" r="14" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M36 36 L50 50" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
TIMER_I = icon('<circle cx="32" cy="36" r="20" fill="none" stroke="var(--stone-dark)" stroke-width="5"/><path d="M32 36 V22 L42 30" stroke="var(--stone-dark)" stroke-width="4" fill="none" stroke-linecap="round"/><rect x="26" y="8" width="12" height="8" rx="2" fill="var(--stone-dark)"/>')
DECIDE_I = icon('<path d="M32 10 L54 50 H10 Z" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M24 34 l6 6 12 -14" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
TRIM_I = icon('<rect x="12" y="28" width="40" height="10" rx="4" fill="var(--bad)"/><rect x="12" y="28" width="20" height="10" rx="4" fill="var(--good)"/>')

P3 = svg(360, sky(360)
         + person(150, 240, s=0.65, face=EYES, **OPERATOR)
         + bubble(60, 150, 220, 54, "⟦이거 매번 손으로 해야 하나?|do I really have to do this by hand every time?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + '<g transform="translate(400,230)"><rect x="-50" y="-60" width="100" height="90" rx="8" fill="var(--stone-dark)"/><circle cx="0" cy="-15" r="22" fill="none" stroke="var(--good)" stroke-width="6"/><circle cx="0" cy="-15" r="6" fill="var(--good)"/></g>'
         + label(400, 290, "⟦기계가 대신 해요|the machine does it instead⟧", 12, "var(--good)", cls="d")
         + person(600, 240, s=0.65, face=SMILE, extra=WRENCH, **MECHANIC)
         + bubble(560, 140, 200, 54, "⟦저는 새 문제를 볼게요|I\'ll go look at something new⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 35, "⟦반복되는 건 기계가 하게 하고, 사람은 새 문제에 시간을 써요|let the machine handle what repeats, and spend people\'s time on what\'s new⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦\'이거 매번 손으로 해야 하나?\'를 계속 물어봐요|keep asking: do I really have to do this by hand every time?⟧", 12, "var(--muted)"))

# 4. 저울: 허드렛일 시간 vs 새로운 개선 시간
P4 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + board(40, 30, 300, 150, "⟦자동화 전|BEFORE AUTOMATING⟧", ("⟦허드렛일 시간: 많음|toil time: a lot⟧", "⟦개선 시간: 거의 없음|improvement time: almost none⟧"), 1.0)
         + gauge(190, 210, 1.0, level=0.85, label_text="⟦허드렛일|toil⟧", color="var(--bad)")
         + board(420, 30, 300, 150, "⟦자동화 후|AFTER AUTOMATING⟧", ("⟦허드렛일 시간: 적음|toil time: little⟧", "⟦개선 시간: 많음|improvement time: a lot⟧"), 1.0)
         + gauge(570, 210, 1.0, level=0.8, label_text="⟦개선|improvement⟧", color="var(--good)")
         + label(380, 280, "⟦자동화할수록 저울이 허드렛일에서 개선 쪽으로 기울어요|the more you automate, the balance tips from toil toward improvement⟧", 12, "var(--ink)", cls="d"))

# 5. 깨지는 곳: 모든 반복 작업이 다 나쁜 건 아니에요
P5 = svg(300, sky(300, ground=False)
         + person(200, 150, s=0.7, face=EYES, **OPERATOR)
         + bubble(60, 60, 230, 54, "⟦이건 1년에 한 번뿐인데, 자동화해야 하나요?|this only happens once a year — should I even automate it?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + board(430, 60, 290, 160, "⟦따져보기|WEIGH IT UP⟧", ("⟦자동화 만드는 시간: 사흘|time to build automation: 3 days⟧", "⟦손으로 하면: 한 해에 10분|doing it by hand: 10 min a year⟧", "⟦→ 그냥 손으로 해요|-> just do it by hand⟧"), 1.0, hl=2)
         + label(380, 280, "⟦모든 반복이 나쁜 건 아니에요 — 가끔 하는 반복은 자동화 비용이 더 클 수도 있어요|not every repeat is bad — automating something rare can cost more than just doing it⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "toil", "order": 47,
    "title": ("매일 똑같이 반복하는 허드렛일", "The Same Chore, Every Single Day"),
    "h1": ("<em>토일</em>이 뭐예요?", "What is <em>Toil</em>?"),
    "sub": ("토일을 매일 아침 똑같은 보고서를 손으로 옮겨 적는 요원의 이야기로 풀어봤어요.",
            "Toil, told as a story about an operator who copies the exact same report by hand every morning."),
    "panels": [
        {"svg": P1, "alt": ("관제실 요원이 매일 아침 똑같은 보고서를 손으로 옮겨 적고, 종이 더미가 옆에 쌓여감", "The operator copies the same report by hand every morning, as a pile of paper grows beside her"),
         "caption": ("관제실 요원이 매일 아침 똑같은 보고서를 손으로 옮겨 적어요.", "Every morning, the operator copies the exact same report by hand."),
         "small": ("어제와 똑같은 내용을, 오늘도 손으로 옮겨요.", "The same content as yesterday, copied by hand again today.")},
        {"svg": P2, "alt": ("종이 더미가 산더미처럼 쌓이고, 요원이 새 문제를 볼 시간이 없다고 말함", "A mountain of paper piles up, and the operator says there's no time left to look at anything new"),
         "caption": ("반복되는 손일이 쌓이면, 사람 시간이 거기에 다 잡아먹혀요.", "When repetitive manual work piles up, it swallows all the time a person has."),
         "small": ("쌓인 서류만큼, 새로운 걸 볼 시간이 줄어요.", "The more paper piles up, the less time is left for anything new.")},
        {"svg": P3, "hero": True, "alt": ("요원이 '이거 매번 손으로 해야 하나?'라고 묻자 자동화 기계가 대신 일을 하고, 정비사는 새 문제를 보러 감", "The operator asks 'do I really have to do this by hand every time?'; a machine takes over, and the mechanic goes to look at something new"),
         "caption": ("반복되는 건 기계가 하게 하고, 사람은 새 문제에 시간을 써요.", "Let the machine handle what repeats, and spend people's time on what's new."),
         "small": ("계속 물어봐요 — '이거 매번 손으로 해야 하나?'", "Keep asking — 'do I really have to do this by hand every time?'"),
         "tricks": (4, [
             (FIND_I, ("반복되고 가치 적은 일 찾기", "Find repetitive, low-value work"), ("자동화 가능한지도 봐요", "and whether it can be automated"), "calm"),
             (TIMER_I, ("시간을 재봐요", "Measure how much time it takes"), ("감으로 말고 숫자로요", "numbers, not a guess")),
             (DECIDE_I, ("자동화할지 결정해요", "Decide whether to automate"), ("비용과 비교해서요", "weighed against the cost"), "warm"),
             (TRIM_I, ("자동화 못 하면 최소한 줄여요", "Can't automate? Trim it down"), ("완전히 없애진 못해도요", "even if not all the way")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 자동화 전, 허드렛일 시간이 많고 개선 시간은 거의 없음. 오른쪽: 자동화 후, 허드렛일은 적고 개선 시간이 많음", "Left: before automating, toil time is high and improvement time is almost none. Right: after automating, toil is low and improvement time is high"),
         "caption": ("자동화할수록 저울이 허드렛일에서 개선 쪽으로 기울어요.", "The more you automate, the balance tips from toil toward improvement."),
         "small": ("시간은 한정돼 있어서, 한쪽이 줄면 다른 쪽이 늘어요.", "Time is limited — less on one side means more on the other.")},
        {"svg": P5, "alt": ("요원이 1년에 한 번뿐인 일을 자동화해야 할지 묻고, 따져보기 안내판이 '그냥 손으로 해요'를 가리킴", "The operator wonders whether to automate something that happens once a year, and a weigh-it-up board points to 'just do it by hand'"),
         "caption": ("모든 반복이 나쁜 건 아니에요 — 가끔 하는 반복은 자동화 비용이 더 클 수도 있어요.", "Not every repeat is bad — automating something rare can cost more than just doing it."),
         "small": ("만드는 비용과 손으로 할 때의 시간을 따져봐야 해요.", "You have to weigh the cost to build it against the time doing it by hand actually takes.")},
    ],
    "summary": (("<b>토일</b> = 반복되고 <b>가치가 적은</b> 손일. 자동화 못 하면 사람 시간이 <b>거기에 다 잡아먹혀요</b>.",
                 "<b>Toil</b> = repetitive, <b>low-value</b> manual work. Leave it unautomated, and it <b>swallows all the time a person has</b>."),
                ("Google SRE가 정의한 개념으로, 반복적이고 자동화 가능하며 장기적 가치가 적은 운영 작업을 가리켜요. 토일 비율을 측정해 관리하고, 자동화 비용과 절약되는 시간을 비교해 자동화 여부를 판단해요. 토일이 줄어든 만큼 생긴 시간은 오케스트레이션 같은 더 큰 자동화로 이어져요.",
                 "A concept defined by Google SRE for operational work that's repetitive, automatable, and has little long-term value. Teams measure the toil ratio to manage it, and decide whether to automate by weighing the cost against the time it would save. The time freed up as toil shrinks often leads to bigger automation, like orchestration.")),
    "glossary": [
        ("토일", "Toil", ("반복되고 가치 적은 손일.", "Repetitive, low-value manual work."), ('자동화할수록 줄어들어요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'The more you automate, the less of it there is. → <a href="reliability-en.html">the people who keep the park open</a>')),
        ("자동화 vs 수동", "Automation vs. manual", ("기계가 할지, 사람이 할지 가르는 선.", "The line between what the machine does and what a person does."), ("반복은 기계, 판단은 사람이에요.", "Repetition goes to the machine; judgment stays with the person.")),
        ("토일 측정", "Measuring toil", ("이 일에 얼마나 시간이 드는지 재는 것.", "Timing how much time a task actually costs."), ("재보지 않으면 줄었는지도 몰라요.", "Without measuring it, you can't even tell if it shrank.")),
        ("가치 있는 일과의 구분", "Separating it from valuable work", ("새로운 문제를 푸는 일과 다른 선을 긋는 것.", "Drawing a line against work that solves something new."), ("토일은 늘 같은 문제를 반복해서 풀어요.", "Toil solves the exact same problem, over and over.")),
        ("자동화 투자 판단", "Deciding whether to invest in automation", ("만드는 비용과 아끼는 시간을 비교하는 일.", "Weighing the cost to build against the time it saves."), ("가끔 하는 일은 수지가 안 맞을 수도 있어요.", "Something rare enough might not be worth it.")),
        ("운영 부담", "Operational burden", ("토일이 쌓여서 생기는 전체 무게.", "The overall weight that builds up from accumulated toil."), ("쌓이면 새 일을 할 시간이 없어져요.", "Pile it up, and there's no time left for anything new.")),
        ("오케스트레이션", "Orchestration", ("자동화가 커지면 여러 자동화를 묶어 관리하는 일.", "Once automation grows, coordinating many of them together."), ("토일을 줄이는 자동화의 다음 단계예요.", "The next stage after automation starts cutting toil.")),
        ("런북", "Runbook", ("사람이 손으로 하던 순서를 적어둔 공책.", "The notebook where the manual steps were written down."), ("자동화는 보통 이 공책을 코드로 옮기는 일에서 시작해요.", "Automation usually starts by turning this notebook into code.")),
    ],
}
