from _draw import *
from _world import *

# 1. 이상한데 그 자리에서 고치려다 더 꼬여요
P1 = svg(300, sky(300)
         + ride(200, 260, 0.9, color="var(--accent)", closed=True, label_text="⟦오늘 고친 버전|today's updated version⟧")
         + person(330, 180, s=0.7, face=FROWN + SWEAT, extra=WRENCH, **MECHANIC)
         + bubble(340, 90, 210, 46, "⟦여기서 당장 고쳐볼게요|let me fix it right here, right now⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦이상한데 그 자리에서 고치려다 더 꼬여요|something's off, and fixing it on the spot makes it worse⟧", 12, "var(--ink)"))

# 2. 급할 때 고치려 들면 시간은 더 걸리고 실수가 늘어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(200, 230, 0.85, color="var(--accent)", closed=True)
         + person(330, 160, s=0.65, face=FROWN + SWEAT, extra=WRENCH, **MECHANIC)
         + '<path d="M420 190 l20 -14 M430 200 l24 2 M415 218 l18 10" stroke="var(--stone-dark)" stroke-width="4" stroke-linecap="round"/>'
         + bubble(430, 70, 220, 50, "⟦공구를 더 꺼낼수록 시간은 더 걸려요|the more tools you grab, the longer it takes⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(380, 286, "⟦급할 때 바로 고치려 들면 실수가 늘어요|rushing to fix it on the spot only invites more mistakes⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 고치려 들지 말고, 먼저 되돌려요
REVERT_I = icon('<path d="M46 18 a18 18 0 1 0 6 26" stroke="var(--good)" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M50 8 l-4 14 l14 4z" fill="var(--good)"/>')
STACK_I = icon('<rect x="14" y="36" width="36" height="10" rx="2" fill="var(--stone)"/><rect x="14" y="24" width="36" height="10" rx="2" fill="var(--stone-dark)"/><rect x="14" y="12" width="36" height="10" rx="2" fill="var(--accent)"/>')
SEARCH_I = icon('<circle cx="26" cy="26" r="14" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M36 36 L50 50" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
DRILL_I = icon('<path d="M32 10 a22 22 0 1 1 -15.5 6.5" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M10 10 v12 h12" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

P3 = svg(340, sky(340)
         + ride(170, 300, 0.85, color="var(--accent)", closed=True, label_text="⟦오늘 버전, 이상해요|today's version, acting up⟧")
         + person(280, 227, s=0.65, face=EYES, **MECHANIC)
         + '<path d="M330 260 Q420 270 500 285" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(430, 250, "⟦여기로 되돌려요|revert right here⟧", 12, "var(--ink)", cls="d")
         + bigbutton(520, 290, 0.8)
         + label(380, 30, "⟦고치려 들지 말고, 먼저 되돌려요|don't fix it in place — revert first⟧", 14, "var(--ink)", cls="d")
         + label(380, 328, "⟦되돌린 뒤에 천천히 원인을 찾아요|revert first, then calmly find out why⟧", 12, "var(--muted)"))

# 4. 오늘 버전(문제) → 되돌리기 → 어제 버전(정상)
P4 = svg(300, sky(300, ground=False)
         + ride(140, 230, 0.8, color="var(--bad)", closed=True, label_text="⟦오늘 버전: 문제|today: broken⟧")
         + '<circle cx="380" cy="110" r="34" fill="none" stroke="var(--stone-dark)" stroke-width="5"/>'
         + '<path d="M380 110 L380 86 M380 110 L364 122" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>'
         + '<path d="M406 84 a34 34 0 0 0 -52 2" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>'
         + '<path d="M358 80 l-12 10 l16 12z" fill="var(--good)"/>'
         + '<path d="M250 190 L480 190" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M470 183 L480 190 L470 197" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + ride(630, 230, 0.8, color="var(--good)", label_text="⟦어제 버전: 정상|yesterday: fine⟧")
         + label(380, 286, "⟦코드는 이렇게 통째로 되돌려요|the code reverts, all at once, like this⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 코드는 되돌려도 데이터는 조심
P5 = svg(300, '<rect width="760" height="300" fill="var(--good-soft)"/>'
         + ride(170, 230, 0.8, color="var(--good)", label_text="⟦코드는 되돌아갔어요|the code's back to normal⟧")
         + board(420, 50, 280, 160, "⟦손님 명부|GUEST LOG⟧", ("⟦오늘 들어온 예약 40건|40 bookings made today⟧", "⟦어제 버전엔 그 기록이 없어요|yesterday's version never saw them⟧", "⟦데이터는 조심해서 다뤄야 해요|data needs careful handling⟧"), 0.95, hl=1)
         + label(380, 286, "⟦코드는 되돌려도, 쌓인 손님 명부는 그대로 조심해야 해요|code can revert, but the guest log that piled up still needs care⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "rollback", "order": 32,
    "title": ("이상하면 바로 어제 버전으로", "Back to Yesterday's Version, Fast"),
    "h1": ("<em>롤백</em>이 뭐예요?", "What is a <em>Rollback</em>?"),
    "sub": ("롤백을 이상하면 그 자리에서 고치지 않고 바로 어제 버전으로 되돌리는 이야기로 풀어봤어요.",
            "Rollback, told as a story about not fixing things on the spot — just going straight back to yesterday's version."),
    "panels": [
        {"svg": P1, "alt": ("오늘 고친 기구가 이상한데 정비사가 그 자리에서 고쳐보겠다고 말함", "Today's updated ride is acting up, and a mechanic says they'll fix it right there"),
         "caption": ("이상한데 그 자리에서 고치려다 더 꼬여요.", "Something's off, and fixing it on the spot makes it worse."),
         "small": ("무엇이 문제인지도 모른 채 손을 대면 더 엉켜요.", "Tinkering with it before you know what's wrong only tangles it further.")},
        {"svg": P2, "alt": ("정비사가 땀을 흘리며 공구를 이것저것 꺼내 쓰고, 꺼낼수록 시간이 더 걸린다는 말풍선이 붙음", "A sweating mechanic grabs tool after tool, with a bubble saying the more tools, the longer it takes"),
         "caption": ("급할 때 바로 고치려 들면 실수가 늘어요.", "Rushing to fix it on the spot only invites more mistakes."),
         "small": ("서두를수록 손이 꼬이고 시간은 더 걸려요.", "The more you rush, the clumsier it gets, and the longer it takes.")},
        {"svg": P3, "hero": True, "alt": ("정비사가 고장난 기구를 고치려 들지 않고 큰 되돌리기 버튼 쪽으로 향함", "A mechanic steps away from the broken ride and heads toward a big revert button instead"),
         "caption": ("고치려 들지 말고, 먼저 되돌려요.", "Don't fix it in place — revert first."),
         "small": ("되돌린 뒤에 천천히 원인을 찾아요.", "Revert first, then calmly find out why."),
         "tricks": (4, [
             (REVERT_I, ("이상하면 먼저 되돌려요", "If something's off, revert first"), ("고치기는 나중이에요", "fixing it comes later"), "calm"),
             (STACK_I, ("평소에 버전을 잘 보관해요", "Keep past versions well-stored"), ("되돌리기가 쉬우려면", "so reverting is easy")),
             (SEARCH_I, ("되돌린 뒤 천천히 원인을 찾아요", "After reverting, find the cause calmly"), ("탓하지 않고요", "without blame"), "warm"),
             (DRILL_I, ("되돌리는 연습도 미리 해둬요", "Practice reverting ahead of time"), ("막상 급할 때를 위해", "so it's ready when it's urgent")),
         ])},
        {"svg": P4, "alt": ("문제가 생긴 오늘 버전 기구에서 시계가 되감기며 화살표가 어제 버전의 멀쩡한 기구로 이어짐", "A clock rewinds and an arrow leads from today's broken ride to yesterday's fine one"),
         "caption": ("오늘 버전(문제) → 되돌리기 → 어제 버전(정상).", "Today's version (broken) → revert → yesterday's version (fine)."),
         "small": ("코드는 이렇게 통째로, 한 번에 되돌려요.", "The code reverts like this — all at once.")},
        {"svg": P5, "alt": ("기구는 정상으로 돌아왔지만 손님 명부 안내판에 오늘 들어온 예약은 어제 버전엔 없다는 경고가 붙음", "The ride is back to normal, but a guest-log board warns that today's bookings don't exist in yesterday's version"),
         "caption": ("코드는 되돌려도, 데이터는 조심해야 해요.", "Code can revert, but data needs care."),
         "small": ("되돌리는 동안 쌓인 손님 명부 차이는 못 되돌릴 때가 있어요.", "The guest-log gap that built up in between sometimes can't be reverted.")},
    ],
    "summary": (("<b>롤백</b> = 이상하면 그 자리에서 <b>고치려 들지 않고</b>, 먼저 <b>어제 버전으로 되돌린 뒤</b> 천천히 원인을 찾는 요령.",
                 "<b>Rollback</b> = when something's off, <b>don't fix it in place</b> — revert to <b>yesterday's version first</b>, then calmly find out why."),
                ("배포 직후 문제가 생기면 원인을 그 자리에서 찾기보다, 이전의 안정된 버전으로 먼저 되돌리는 대응 방식이에요. 복구 시간을 최소화하고, 원인 분석은 사후에 차분히 진행해요.",
                 "A response strategy where, if something breaks right after a deploy, you revert to the last stable version first rather than debugging on the spot. It minimizes recovery time, leaving root-cause analysis for a calmer moment afterward.")),
    "glossary": [
        ("롤백", "Rollback", ("바로 어제 버전으로 되돌리는 일.", "Going straight back to yesterday's version."), ("복구가 먼저, 원인 분석은 나중이에요.", "Recovery comes first — root-cause analysis comes later.")),
        ("배포 버전 관리", "Release versioning", ("어제 버전을 잘 보관해두는 일.", "Keeping yesterday's version safely stored."), ("보관이 잘 돼 있어야 되돌리기도 쉬워요.", "Good storage is what makes reverting easy.")),
        ("전진 수정(롤포워드)", "Roll-forward", ("되돌리는 대신 고쳐서 앞으로 가는 일.", "Fixing forward instead of reverting back."), ("롤백보다 느리지만 때로는 유일한 길이에요.", "Slower than rollback, but sometimes the only option.")),
        ("되돌리기 쉬운 설계", "Easy-to-revert design", ("언제든 어제로 갈 수 있게 만드는 일.", "Building things so you can always go back to yesterday."), ("평소 준비해둬야 급할 때 빨리 되돌려요.", "Prepared ahead of time, so reverting is fast when it matters.")),
        ("카나리와의 관계", "vs. canary", ("1%만 태워보는 것과, 전부 되돌리는 것.", "Testing on 1%, versus reverting everything."), ('카나리가 이상하면 롤백으로 이어져요. → <a href="canary-ko.html">구석에서 몰래 하는 시험 운행</a>', '<a href="canary-en.html">A bad canary leads straight into a rollback</a>')),
        ("블루-그린과의 관계", "vs. blue-green", ("화살표만 바꾸면 바로 되돌아가는 것.", "Flipping the sign back sends you right back."), ('블루-그린은 롤백이 특히 빨라요. → <a href="bluegreen-ko.html">쌍둥이 기구를 번갈아 운영</a>', '<a href="bluegreen-en.html">Blue-green makes rollback especially fast</a>')),
        ("데이터 마이그레이션의 어려움", "Data migration risk", ("코드는 되돌려도 안 따라오는 기록.", "Records that don't follow the code back."), ("손님 명부(데이터)는 코드처럼 간단히 안 돌아가요.", "The guest log doesn't revert as simply as the code does.")),
        ("체크포인트", "Checkpoint", ("언제로 되돌아갈지 찍어둔 지점.", "A marked point to revert back to."), ("자주 찍어둘수록 잃는 게 적어요.", "The more often you mark one, the less you lose.")),
    ],
}
