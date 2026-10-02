from _draw import *
from _world import *

# 1. 같은 고장이 또 났는데, 지난번에 어떻게 고쳤는지 아무도 기억 못해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(380, 260, 1.0, color="var(--bad)", closed=True)
         + person(560, 260 - 112 * 0.6, s=0.6, face=SWEAT, **ROOKIE)
         + bubble(440, 120, 220, 50, "⟦지난번에 어떻게 고쳤더라...|how did we fix this last time...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(160, 260 - 112 * 0.55, s=0.55, face=SMILE, hat=None, shirt="#7B3FA0")
         + label(160, 140, "⟦선배는 휴가중|the senior is on vacation⟧", 11, "var(--muted)")
         + label(380, 282, "⟦같은 고장이 또 났는데, 지난번에 어떻게 고쳤는지 아무도 기억 못해요|the same failure hits again, and nobody remembers how it was fixed last time⟧", 12, "var(--ink)"))

# 2. 왜: 머릿속에만 있으면 그 사람이 쉬는 날엔 아무도 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(300, 260 - 112 * 0.65, s=0.65, face=SMILE, **MECHANIC)
         + bubble(190, 70, 260, 60, "⟦(머릿속에만 있어요)|(it's only in my head)⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(520, 260 - 112 * 0.6, s=0.6, face=FROWN, **ROOKIE)
         + label(520, 175, "⟦저는 몰라요|I don't know it⟧", 11, "var(--bad)")
         + label(380, 282, "⟦머릿속에만 있으면, 그 사람이 쉬는 날엔 아무도 몰라요|if it's only in someone's head, nobody knows it on their day off⟧", 12, "var(--ink)"))

# 3. hero: 자주 나는 고장마다 "이럴 땐 이렇게" 순서를 공책에 적어둬요
P3 = svg(340, sky(340)
         + board(230, 60, 300, 210, "⟦공책|THE NOTEBOOK⟧", ("⟦기구가 안 열려요|a ride won't start⟧", "⟦줄이 안 줄어요|the line won't shrink⟧", "⟦화면이 꺼져요|the screen goes dark⟧"), 1.1)
         + person(120, 300 - 112 * 0.6, s=0.6, face=SMILE, extra=CLIPBOARD, **MECHANIC)
         + person(620, 300 - 112 * 0.6, s=0.6, face=SMILE, **ROOKIE)
         + label(380, 40, "⟦자주 나는 고장마다, '이럴 땐 이렇게' 순서를 공책에 적어둬요|for each common failure, write down 'do this, then this' in a notebook⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦누가 당번이어도 공책대로 하면 돼요|whoever's on duty can just follow the notebook⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 공책을 펼치면 번호 순서대로 적혀 있어요
P4 = svg(320, sky(320)
         + board(120, 30, 520, 230, "⟦기구가 안 열릴 때|WHEN A RIDE WON'T START⟧", ("⟦1. 빨간 버튼부터 확인|1. check the red button first⟧", "⟦2. 창고에 재고 있는지 확인|2. check the warehouse stock⟧", "⟦3. 안 되면 호출기로 선배에게|3. if not, page the senior⟧"), 1.1)
         + label(380, 300, "⟦순서대로, 그림책처럼 쉽게 — 신참도 따라할 수 있어요|step by step, simple as a picture book — even a rookie can follow it⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 안 고치고 오래 두면 틀린 내용이 남아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + board(40, 60, 300, 150, "⟦옛날 공책|OLD NOTEBOOK⟧", ("⟦1. 옛날 방식대로|1. the old way⟧", "⟦(이제 안 통해요)|(doesn't work anymore)⟧"), 1.0)
         + person(140, 260 - 112 * 0.5, s=0.5, face=FROWN, **ROOKIE)
         + label(190, 282, "⟦고치지 않고 오래 두면 틀린 내용이 남아요|left unfixed too long, it stays wrong⟧", 11, "var(--bad)", cls="d")
         + board(420, 60, 300, 150, "⟦새로 고친 공책|UPDATED NOTEBOOK⟧", ("⟦+ 새로 배운 것 추가|+ what we just learned⟧",), 1.0)
         + person(680, 260 - 112 * 0.5, s=0.5, face=SMILE, extra=CLIPBOARD, **MECHANIC)
         + label(570, 282, "⟦고칠 때마다 공책도 같이 고쳐요|update the notebook every time something changes⟧", 11, "var(--ink)", cls="d"))

COMMON_I = icon('<path d="M32 10 L38 24 L54 26 L42 36 L46 52 L32 43 L18 52 L22 36 L10 26 L26 24 Z" fill="var(--accent)"/>')
STEP_I = icon('<circle cx="16" cy="16" r="7" fill="var(--accent)"/><circle cx="16" cy="32" r="7" fill="var(--accent)"/><circle cx="16" cy="48" r="7" fill="var(--accent)"/><path d="M28 16 H54 M28 32 H54 M28 48 H54" stroke="var(--muted)" stroke-width="4" stroke-linecap="round"/>')
FOLLOW_I = icon('<circle cx="24" cy="18" r="9" fill="var(--accent)"/><rect x="12" y="30" width="24" height="26" rx="6" fill="var(--accent)"/><path d="M40 36 l8 8 16 -16" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
ADD_I = icon('<rect x="12" y="10" width="34" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h18 M18 28 h18" stroke="#142033" stroke-width="2.5"/><path d="M44 40 l10 -10 6 6 -10 10z" fill="var(--accent)"/><path d="M50 44 l6 6" stroke="var(--accent)" stroke-width="3"/>')

PAGE = {
    "slug": "runbook", "order": 45,
    "title": ("정비사의 공책", "The Mechanic's Notebook"),
    "h1": ("<em>런북</em>이 뭐예요?", "What is a <em>Runbook</em>?"),
    "sub": ("런북을, 자주 나는 고장마다 '이럴 땐 이렇게' 순서를 적어둔 정비사의 공책 이야기로 풀어봤어요.",
            "A runbook, told as a story about the mechanic's notebook that spells out 'do this, then this' for every common failure."),
    "panels": [
        {"svg": P1, "alt": ("고장난 기구 앞에서 신참 정비사가 지난번에 어떻게 고쳤는지 떠올리려 애쓰고, 선배는 휴가 중이라 물어볼 수도 없음", "A rookie mechanic struggles to recall how a broken ride was fixed last time, while the senior is away on vacation"),
         "caption": ("같은 고장이 또 났는데, 아무도 기억 못해요.", "The same failure hits again, and nobody remembers how it was fixed."),
         "small": ("처음부터 다시 헤매요.", "So they start from scratch, confused.")},
        {"svg": P2, "alt": ("정비사의 머릿속에만 해결법이 있고, 신참은 전혀 모른다고 말함", "The fix lives only in one mechanic's head, and the rookie admits they have no idea"),
         "caption": ("머릿속에만 있으면 그 사람이 쉬는 날엔 아무도 몰라요.", "If it's only in someone's head, nobody knows it on their day off."),
         "small": ("신참이 당황할 수밖에 없어요.", "The rookie is left stuck.")},
        {"svg": P3, "hero": True, "alt": ("공책에 자주 나는 고장 종류가 적혀 있고, 정비사가 공책을 들고 신참에게 건네줌", "A notebook lists common kinds of failures, as a mechanic hands it over to a rookie"),
         "caption": ("자주 나는 고장마다, '이럴 땐 이렇게' 순서를 공책에 적어둬요.", "For each common failure, write down 'do this, then this' in a notebook."),
         "small": ("누가 당번이어도 공책대로 하면 돼요.", "Whoever's on duty can just follow the notebook."),
         "tricks": (4, [
             (COMMON_I, ("자주 나는 고장부터 적어요", "Write down the common failures first"), ("드물게 나는 건 나중에요", "rare ones can wait"), "calm"),
             (STEP_I, ("순서대로, 그림책처럼 쉽게", "Step by step, picture-book simple"), ("한 줄씩 또박또박요", "one clear line at a time")),
             (FOLLOW_I, ("신참도 따라할 수 있게", "Simple enough for a rookie"), ("설명 없이도 돼요", "no extra explaining needed"), "warm"),
             (ADD_I, ("새로 배운 건 공책에 추가", "Add what you just learned"), ("사후 분석에서 나온 것도요", "including what came out of a postmortem")),
         ])},
        {"svg": P4, "alt": ("공책을 펼친 모습: 1. 빨간 버튼부터 확인 2. 창고에 재고 있는지 확인 3. 안 되면 호출기로 선배에게", "The notebook opened to a page: 1. check the red button first 2. check the warehouse stock 3. if not, page the senior"),
         "caption": ("공책을 펼치면 번호 순서대로 적혀 있어요.", "Open the notebook, and it's all numbered in order."),
         "small": ("순서대로 하면 신참도 따라할 수 있어요.", "Follow the order, and even a rookie can do it.")},
        {"svg": P5, "alt": ("왼쪽: 옛날 공책의 옛날 방식이 이제 안 통해서 신참이 당황함. 오른쪽: 새로 배운 것을 추가해 고친 공책을 든 정비사가 웃음", "Left: a rookie is stuck because the old notebook's old way no longer works. Right: a smiling mechanic holds an updated notebook with the new lesson added"),
         "caption": ("안 고치고 오래 두면 틀린 내용이 남아요.", "Left unfixed too long, the notebook stays wrong."),
         "small": ("고칠 때마다 공책도 같이 고쳐야 해요.", "Every fix needs to update the notebook too.")},
    ],
    "summary": (("<b>런북</b> = 자주 나는 고장마다 <b>순서대로 적어둔 공책</b>으로, 누가 당번이어도 <b>그대로 따라하면</b> 고칠 수 있게 하는 것.",
                 "<b>Runbook</b> = a <b>notebook spelling out the steps</b> for each common failure, so whoever's on duty can fix it just by <b>following along</b>."),
                ("Runbook. 반복되는 장애 상황에 대한 단계별 대응 절차를 적어둔 문서예요. 플레이북이라고도 불러요. 자동화의 대본이 되기도 하고, 신참 온보딩에도 쓰이며, 사후 분석에서 배운 내용이 꾸준히 더해져야 녹슬지 않아요.",
                 "A document that spells out step-by-step responses to a recurring failure, also called a playbook. It can become the script for automation, helps onboard newcomers, and stays useful only if lessons from postmortems keep getting added.")),
    "glossary": [
        ("런북", "Runbook (playbook)", ("고장마다 순서를 적어둔 공책.", "The notebook with steps for each failure."), ("플레이북이라고도 불러요.", "Also called a playbook.")),
        ("단계별 절차", "Step-by-step procedure", ("1, 2, 3 번호로 적힌 순서.", "The order written out as 1, 2, 3."), ("순서대로만 하면 돼요.", "Just follow it in order.")),
        ("자동화와의 관계", "Relationship to automation", ("공책이 결국 자동화 대본이 되는 것.", "How the notebook eventually becomes an automation script."), ("같은 단계가 반복되면 자동화할 신호예요.", "Repeating the same steps is a sign to automate them.")),
        ("신참 온보딩", "Rookie onboarding", ("새로 온 사람이 공책으로 배우는 것.", "How a newcomer learns from the notebook."), ("설명 없이도 혼자 따라할 수 있어요.", "They can follow along without extra explaining.")),
        ("최신화", "Keeping it current", ("오래된 내용을 그대로 안 두는 것.", "Not leaving stale content as-is."), ("안 고치면 '스테일(stale) 런북'이 돼요.", "Left unfixed, it becomes a 'stale runbook'.")),
        ("체크리스트", "Checklist", ("빠뜨리지 않게 하나씩 확인하는 목록.", "A list that makes sure nothing gets skipped."), ("런북 안에 자주 함께 들어가요.", "Often sits right inside the runbook.")),
        ("사후 분석과의 연결", "Link to the postmortem", ("사고에서 배운 걸 공책에 추가하는 것.", "Adding what was learned from an incident into the notebook."), ('→ <a href="postmortem-ko.html">탓하지 않고 모여 쓰는 기록</a>', '→ <a href="postmortem-en.html">the record everyone writes without blame</a>')),
        ("토일", "Toil", ("공책이 자꾸 늘어나면 뜨는 신호.", "The signal that shows up when the notebook keeps growing."), ('매일 반복되는 허드렛일이에요. → <a href="toil-ko.html">매일 똑같이 반복하는 허드렛일</a>', 'The same repetitive chore, every day. → <a href="toil-en.html">the chore that repeats every day</a>')),
    ],
}
