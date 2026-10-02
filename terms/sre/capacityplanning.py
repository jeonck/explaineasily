from _draw import *
from _world import *

# 1. 성수기에 손님이 몰려서 다들 돌아가요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(110, 230, 0.85, color="var(--stone)", closed=True, label_text="⟦자리 없음|FULL⟧")
         + queueline(190, 177, 7, 0.42, 24) + label(260, 260, "⟦줄이 안 줄어요|the line never gets shorter⟧", 11, "var(--bad)")
         + person(540, 178, s=0.65, face=FROWN, hat=None, shirt="#7B3FA0")
         + bubble(470, 100, 220, 44, "⟦방학이라 더 왔는데... 다 돌아가네|everyone came for vacation... and they're all leaving⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦여름 성수기, 기구도 창구도 턱없이 부족해요|peak summer — not enough rides, not enough booths⟧", 12, "var(--ink)"))

# 2. 왜: 평소 기준으로만 준비하면 특별한 날엔 못 버텨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(40, 30, 220, 90, "⟦평소|USUAL DAY⟧", ("⟦줄 4명|line of 4⟧", "⟦기구 3대면 충분|3 rides is enough⟧"), 1.0)
         + queueline(330, 150, 10, 0.42, 24) + label(450, 120, "⟦명절엔 3배|holidays bring 3x⟧", 12, "var(--bad)", cls="d")
         + ride(640, 230, 0.8, color="var(--stone)", closed=True)
         + person(90, 186, s=0.6, face=SWEAT, **MECHANIC)
         + bubble(10, 105, 170, 40, "⟦늘 이 정도였는데...|it's always been about this much...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦평소 기준으로만 준비하면 명절·행사 같은 특별한 날엔 못 버텨요|planning for a usual day can't survive a holiday or event day⟧", 12, "var(--ink)"))

# 3. hero: 작년 기록 + 올해 행사를 보고 미리 계산해서 늘려둬요
P3 = svg(360, sky(360)
         + board(30, 40, 230, 160, "⟦작년 기록|LAST YEAR⟧", ("⟦7월 평균 400명|July avg. 400⟧", "⟦추석 주말 1200명|holiday wknd 1200⟧", "⟦→ 올핸 더 올 듯|-> likely more this year⟧"), 1.0)
         + person(330, 236, s=0.7, face=EYES, **OPERATOR) + '<path d="M290 130 L330 200" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(460, 300, 0.85, color="var(--accent)") + ride(650, 300, 0.75, color="#5B8DEF")
         + person(556, 243, s=0.5, face=SMILE, **MECHANIC)
         + label(380, 40, "⟦작년 기록과 올해 행사를 보고, 미리 계산해서 기구·직원을 늘려둬요|look at last year and this year's events, then add rides and staff in advance⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦닥쳐서 늘리는 게 아니라, 미리 세어보고 늘려둬요|not scrambling last-minute — counted and added ahead of time⟧", 12, "var(--muted)"))

# 4. 작년 손님 수 vs 올해 예상, 그만큼 늘린 직원·기구
P4 = svg(320, sky(320)
         + board(40, 30, 300, 230, "⟦올해 준비표|THIS YEAR'S PLAN⟧",
                 ("⟦작년 7월: 손님 400명|last July: 400 guests⟧", "⟦올해 예상: 550명|this July (est.): 550⟧",
                  "⟦기구 3대 → 4대|rides 3 -> 4⟧", "⟦직원 6명 → 9명|staff 6 -> 9⟧", "⟦여유분도 조금 더|a bit of buffer too⟧"), 1.0, hl=1)
         + ride(470, 260, 0.55, color="var(--accent)") + ride(580, 260, 0.55, color="#5B8DEF") + ride(690, 260, 0.55, color="#2E7D6B", closed=True)
         + label(380, 300, "⟦작년 기록 + 올해 예정 행사 = 얼마나 더 필요한지|last year's numbers + this year's events = how much more you need⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 늘 예상보다 더 많이 와요 — 오토스케일링과 같이 써야 안전
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + queueline(90, 194, 6, 0.5, 26) + label(190, 268, "⟦예상보다 늘 더 와요|more always show up than planned⟧", 11, "var(--bad)")
         + board(430, 40, 290, 110, "⟦그래서 같이 써요|SO WE PAIR IT UP⟧", ("⟦미리 계획|plan ahead⟧", "⟦+ 자동으로 더 부르기|+ auto-call more staff⟧"), 1.0)
         + person(575, 180, s=0.5, face=SMILE, **OPERATOR)
         + label(600, 262, "⟦둘 다 있어야 안심|both together, and it's safe⟧", 11, "var(--good)", cls="d")
         + label(380, 280, "⟦미리 세어봐도 늘 모자랄 수 있어요 — 줄이 길어지면 자동으로 더 부르는 것과 짝을 이뤄요|even careful counting can fall short — pair it with calling in more automatically when lines grow⟧", 12, "var(--ink)"))

HIST_I = icon('<rect x="10" y="38" width="10" height="16" fill="var(--muted)"/><rect x="24" y="28" width="10" height="26" fill="var(--muted)"/><rect x="38" y="16" width="10" height="38" fill="var(--accent)"/><path d="M8 58 h48" stroke="var(--muted)" stroke-width="3"/>')
CAL_I = icon('<rect x="12" y="14" width="40" height="38" rx="3" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><path d="M12 24 h40" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="38" r="5" fill="var(--bad)"/>')
BUFF_I = icon('<rect x="10" y="30" width="30" height="24" fill="var(--good)"/><rect x="40" y="18" width="14" height="36" fill="var(--good)" opacity="0.5"/>')
LOAD_I = icon('<path d="M10 50 Q32 10 54 50" stroke="var(--accent)" stroke-width="5" fill="none"/><circle cx="32" cy="22" r="5" fill="var(--bad)"/>')

PAGE = {
    "slug": "capacityplanning", "order": 6,
    "title": ("내년 손님 수를 미리 세어보기", "Counting Next Year's Guests in Advance"),
    "h1": ("<em>용량 계획</em>이 뭐예요?", "What is <em>Capacity Planning</em>?"),
    "sub": ("용량 계획을 작년 기록과 올해 행사를 보고 기구·직원을 미리 늘려두는 이야기로 풀어봤어요.",
            "Capacity planning, told as a story about looking at last year's numbers and this year's events to add rides and staff ahead of time."),
    "panels": [
        {"svg": P1, "alt": ("성수기에 기구가 꽉 차고 줄이 줄지 않아 손님들이 돌아감", "At peak season the rides are full and the line never shrinks, so guests turn back"),
         "caption": ("성수기에 손님이 몰려서 기구도 창구도 턱없이 부족해요.", "At peak season, not enough rides or booths for the crowd."),
         "small": ("방학이라 손님이 더 왔는데, 다들 못 타고 돌아가요.", "More guests came for vacation, and most of them just leave.")},
        {"svg": P2, "alt": ("평소 줄 4명 기준 안내판과 명절엔 10명으로 늘어난 줄, 정비사가 당황함", "A board says a usual line is 4 people, but a holiday line has 10, and the mechanic is caught off guard"),
         "caption": ("평소 기준으로만 준비하면 특별한 날엔 못 버텨요.", "Planning for a usual day can't survive a special one."),
         "small": ("명절이나 행사가 있는 날엔 평소보다 몇 배나 더 몰려요.", "A holiday or an event day can bring several times the usual crowd.")},
        {"svg": P3, "hero": True, "alt": ("관제실 요원이 작년 기록판을 보고 올해 기구와 직원을 미리 늘림", "A control-room operator checks last year's record board and adds rides and staff ahead of time"),
         "caption": ("작년 기록과 올해 행사를 보고, 미리 계산해서 늘려둬요.", "Look at last year and this year's events, then add in advance."),
         "small": ("닥쳐서 허둥대는 게 아니라, 미리 세어보고 준비해요.", "Not scrambling last-minute — counted and prepared ahead of time."),
         "tricks": (4, [
             (HIST_I, ("작년 기록을 봐요", "Check last year's numbers"), ("몇 명이 왔었는지요", "how many came back then"), "calm"),
             (CAL_I, ("특별한 날을 체크해요", "Check special days"), ("행사·할인 일정요", "events and sale days")),
             (BUFF_I, ("여유를 조금 둬요", "Leave some buffer"), ("딱 맞추면 위험해요", "exact numbers are risky"), "warm"),
             (LOAD_I, ("미리 시험해봐요", "Test it beforehand"), ("정말 버티는지요", "to see if it really holds")),
         ])},
        {"svg": P4, "alt": ("올해 준비표: 작년 7월 손님 400명, 올해 예상 550명, 기구 3대에서 4대로, 직원 6명에서 9명으로", "This year's plan board: last July 400 guests, this July estimated 550, rides from 3 to 4, staff from 6 to 9"),
         "caption": ("작년 숫자와 올해 예정 행사로 얼마나 더 필요한지 계산해요.", "Last year's numbers plus this year's events tell you how much more you need."),
         "small": ("기구도 직원도 그만큼 늘리고, 여유분도 조금 더 둬요.", "Add that many more rides and staff, with a little extra buffer on top.")},
        {"svg": P5, "alt": ("왼쪽: 예상보다 늘 더 많은 손님이 옴. 오른쪽: 미리 계획과 자동으로 더 부르기를 같이 씀", "Left: more guests always show up than expected. Right: planning ahead paired with automatically calling in more"),
         "caption": ("예상보다 늘 더 많이 와요 — 그래서 자동 대응과 같이 써요.", "More always show up than planned — so it's paired with automatic response."),
         "small": ("미리 계획 하나로는 모자랄 수 있어요. 자동으로 더 부르는 것과 둘 다 있어야 안심이에요.", "Planning alone can fall short. You need it paired with automatically calling in more to feel safe.")},
    ],
    "summary": (("<b>용량 계획</b> = <b>작년 기록</b>과 <b>올해 행사</b>를 보고, 성수기에 얼마나 더 필요할지 <b>미리 계산해서</b> 기구·직원을 늘려두는 일.",
                 "<b>Capacity planning</b> = looking at <b>last year's numbers</b> and <b>this year's events</b> to <b>calculate in advance</b> how much more you'll need, and adding rides and staff before the rush."),
                ("Capacity planning. 과거 사용량 추이와 예정된 이벤트(세일, 명절, 마케팅 캠페인)를 보고 미래의 트래픽을 예측해 인프라를 미리 준비하는 일이에요. 수요 예측으로 필요한 양을 가늠하고, 버퍼를 더해 안전 마진을 두고, 부하 테스트로 실제로 버티는지 확인해요.",
                 "The practice of forecasting future traffic from historical usage trends and planned events (sales, holidays, marketing campaigns) to prepare infrastructure ahead of time. Demand forecasting estimates how much you'll need, a buffer adds a safety margin, and load testing confirms it actually holds up.")),
    "glossary": [
        ("용량 계획", "Capacity planning", ("필요한 만큼을 미리 세어보는 일.", "Counting in advance how much you'll need."), ("기구·직원·서버 모두에 적용돼요.", "Applies to rides, staff, and servers alike.")),
        ("수요 예측", "Demand forecasting", ("얼마나 더 올지 짐작하는 것.", "Guessing how many more will come."), ("작년 기록과 올해 행사를 함께 봐요.", "Looking at last year's numbers together with this year's events.")),
        ("부하 테스트", "Load testing", ("정말 그만큼 버티는지 미리 시험하는 것.", "Testing beforehand whether it really holds that much."), ("준비만 하고 안 해보면 모르는 채로 성수기를 맞아요.", "Prepare without testing, and you hit peak season not knowing for sure.")),
        ("피크 트래픽", "Peak traffic", ("손님이 가장 몰리는 때.", "The moment the most guests arrive."), ("명절·세일·행사 때 평소의 몇 배가 돼요.", "Holidays, sales, and events can bring several times the usual load.")),
        ("버퍼(여유 용량)", "Buffer (headroom)", ("딱 맞추지 않고 남겨두는 몫.", "The extra left over instead of cutting it exactly even."), ("예상이 틀려도 버틸 수 있는 여유예요.", "The cushion that lets you survive a wrong guess.")),
        ("자동 대응과의 관계", "Relation to automatic scaling", ("미리 계획해도 자동으로 더 부르는 것과 짝을 이뤄요.", "Even careful planning is paired with automatically calling in more."), ("미리 계획 + 자동 대응, 둘 다 있어야 안심이에요.", "Planning ahead and automatic response together — that's what makes it safe.")),
        ("SRE와의 관계", "Relation to SRE", ("공원을 돌보는 일 전체의 한 조각.", "One piece of the whole job of keeping the park running."), ('계기판·자동화·호출과 함께 쓰여요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Used together with gauges, automation, and paging. → <a href="reliability-en.html">the people who keep an amusement park open</a>')),
        ("과잉 준비의 비용", "Cost of over-provisioning", ("너무 많이 늘리면 쓰지도 않을 돈이 나가요.", "Add too much, and money goes out for rides that never fill."), ("적게 준비하면 손님을 놓치고, 많이 준비하면 돈을 낭비해요 — 균형이 핵심이에요.", "Too little loses guests; too much wastes money — balance is the point.")),
    ],
}
