from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def calendar(x, y, s=1.0, text="", color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="-26" y="-22" width="52" height="12" rx="4" fill="{color}"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/>{label(0, 12, text, 12, "#142033", cls="d")}</g>')


def cat(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-16 -8 l-4 -18 l14 8z M16 -8 l4 -18 l-14 8z" fill="#8B5E3C"/><circle r="17" fill="#8B5E3C"/>'
            f'<circle cx="-6" cy="-3" r="2.5" fill="#142033"/><circle cx="6" cy="-3" r="2.5" fill="#142033"/><path d="M-3 4 h6 l-3 4z" fill="#E9B44C"/>'
            f'<path d="M-24 2 h12 M-24 8 h12 M12 2 h12 M12 8 h12" stroke="#142033" stroke-width="1.5"/></g>')


def paper(x, y, w, h, title, rows, size=11, color="#142033"):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, size, color, "start")
    return out + "</g>"


def sign(x, y, w, color, title, rows):
    out = (f'<rect x="{x + w / 2 - 4}" y="{y + 90}" width="8" height="90" fill="#8B5E3C"/>'
           f'<rect x="{x}" y="{y}" width="{w}" height="92" rx="8" fill="{color}"/>' + label(x + w / 2, y + 26, title, 12, "#FFF8E7", cls="d"))
    for i, r in enumerate(rows):
        out += label(x + w / 2, y + 52 + i * 22, r, 11, "#FFF8E7")
    return out


# 1. 왕이 물어요: 우리 성 안전해? 경비는 느낌으로 대답해요
P1 = svg(300, sky(300)
         + person(120, 100, s=0.95, face=EYES, **KING) + bubble(40, 16, 220, 34, "⟦우리 성, 안전해?|is our castle safe?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(350, 110, s=0.9, face=FROWN + SWEAT, **GUARD) + bubble(290, 16, 230, 34, "⟦음… 그런 것 같아요?|um… I think so?⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 240, "⟦경비는 느낌으로 대답해요|the guard answers by feel⟧", 12, "var(--bad)")
         + paper(540, 50, 180, 130, "⟦오늘의 느낌|TODAY\'S FEELING⟧", ("⟦조용했어요|it was quiet⟧", "⟦종이 좀 울렸어요|the bell rang a bit⟧", "⟦아마 괜찮아요?|probably fine?⟧"))
         + label(630, 210, "⟦느낌은 사람마다 달라요|feelings differ from person to person⟧", 10, "var(--muted)")
         + label(380, 282, "⟦\'안전해?\'에 \'아마도\'라고 답하면 아무것도 고칠 수 없어요|answering \'is it safe?\' with \'probably\' fixes nothing⟧", 12, "var(--ink)"))

# 2. 재지 않으면: 너무 늦게 알아채고, 너무 많이 울려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(60, 110, s=0.85, face=MASK, extra=BAG) + calendar(180, 120, 1.2, "⟦100일|100d⟧", "var(--bad)")
         + label(130, 235, "⟦도둑이 백 날을 안에 있었어요|the thief was inside for a hundred days⟧", 11, "var(--bad)") + label(130, 255, "⟦아무도 몰랐어요|nobody knew⟧", 10, "var(--muted)")
         + person(300, 110, s=0.85, face=FROWN + SWEAT, **GUARD)
         + bell(470, 100, 1.0) + cat(560, 90, 0.9) + cat(615, 135, 0.9) + cat(670, 90, 0.9)
         + label(580, 235, "⟦종은 하루에 백 번 — 전부 고양이|the bell rings a hundred times a day — all cats⟧", 11, "var(--bad)") + label(580, 255, "⟦진짜 종소리를 못 골라내요|the real ring gets lost⟧", 10, "var(--muted)")
         + label(380, 284, "⟦너무 늦게 알아채고, 너무 많이 울리고 — 재지 않으면 둘 다 안 보여요|noticed too late, ringing too much — without measuring, you see neither⟧", 11, "var(--ink)"))

# 3. 숫자로 재요: 알아채기까지, 쫓아내기까지 (hero)
P3 = svg(360, night(360)
         + '<path d="M110 95 v-12 h270 v12" stroke="var(--accent)" stroke-width="3" fill="none"/>' + label(245, 70, "⟦알아채기까지 걸린 시간|time until noticed⟧", 13, "#F5E6B8", cls="d")
         + '<path d="M380 95 v-12 h270 v12" stroke="var(--good)" stroke-width="3" fill="none"/>' + label(515, 70, "⟦쫓아내기까지 걸린 시간|time until chased out⟧", 13, "#F5E6B8", cls="d")
         + label(245, 130, "⟦예: 30일|e.g. 30 days⟧", 12, "var(--accent)", cls="d") + label(515, 130, "⟦예: 2일|e.g. 2 days⟧", 12, "var(--good)", cls="d")
         + person(80, 105, s=0.7, face=MASK, extra=BAG) + bell(380, 150, 0.9) + person(600, 105, s=0.7, face=SMILE, **GUARD) + person(680, 125, s=0.5, face=MASK, extra=SWEAT)
         + '<path d="M60 210 h640" stroke="#C9D5E6" stroke-width="3"/>'
         + "".join(f'<circle cx="{x}" cy="210" r="8" fill="{c}"/>' for x, c in ((110, "var(--bad)"), (380, "var(--accent)"), (650, "var(--good)")))
         + label(110, 240, "⟦도둑이 들어옴|thief gets in⟧", 12, "#C9D5E6") + label(380, 240, "⟦종이 울림|the bell rings⟧", 12, "#C9D5E6") + label(650, 240, "⟦쫓아냄|chased out⟧", 12, "#C9D5E6")
         + label(380, 300, "⟦느낌 말고 숫자로 — 얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나|numbers, not feelings — how fast we notice, how fast we chase out⟧", 13, "#F5E6B8", cls="d")
         + label(380, 336, "⟦두 시간을 재면 성이 나아지는지 보여요|measure these two times and you can see the castle improve⟧", 12, "#C9D5E6"))

# 4. 달마다 그래프
DAYS = (30, 24, 15, 9, 5, 3)
MONTHS = ("⟦1월|Jan⟧", "⟦2월|Feb⟧", "⟦3월|Mar⟧", "⟦4월|Apr⟧", "⟦5월|May⟧", "⟦6월|Jun⟧")


def mbar(i, v):
    cx = 100 + i * 60
    c = "var(--good)" if v <= 5 else "var(--accent)"
    return (f'<rect x="{cx - 20}" y="{220 - v * 4.5:.0f}" width="40" height="{v * 4.5:.0f}" rx="4" fill="{c}"/>'
            + label(cx, 212 - v * 4.5, f"⟦{v}일|{v}d⟧", 11, "var(--ink)", cls="d") + label(cx, 242, MONTHS[i], 11, "var(--muted)"))


P4 = svg(320, sky(320)
         + label(250, 56, "⟦달마다 그래프 — 알아채기까지 걸린 날|month by month — days until noticed⟧", 13, "var(--ink)", cls="d")
         + '<path d="M70 220 h370" stroke="var(--stone-dark)" stroke-width="2"/>' + "".join(mbar(i, v) for i, v in enumerate(DAYS))
         + paper(500, 60, 220, 150, "⟦다른 숫자들|OTHER NUMBERS⟧", ("⟦고양이 종: 90% → 40%|cat rings: 90% → 40%⟧", "⟦판자 대기: 60일 → 14일|board wait: 60d → 14d⟧", "⟦가짜 편지 연 사람: 30% → 8%|opened fake letter: 30% → 8%⟧", "⟦경비견 있는 방: 60% → 95%|rooms with a dog: 60% → 95%⟧"), 10)
         + label(610, 242, "⟦전부 달마다 적어요|all written down monthly⟧", 11, "var(--muted)")
         + label(380, 296, "⟦막대가 내려가면 성이 나아지는 거예요|when the bars go down, the castle is getting better⟧", 12, "var(--ink)", cls="d"))

# 5. 초록 팻말과 빨간 팻말
P5 = svg(320, sky(320)
         + person(70, 100, s=0.95, face=SMILE, **KING) + person(170, 110, s=0.85, face=SMILE, **GUARD)
         + bubble(40, 14, 250, 34, "⟦숫자가 나아지니 성도 나아졌구나|the numbers improved, so did the castle⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(150, 240, "⟦이제 \'안전해?\'에 숫자로 답해요|now \'safe?\' gets a number for an answer⟧", 11, "var(--ink)")
         + sign(300, 60, 180, "#3F8F5A", "⟦우리가 잘하나|ARE WE DOING WELL⟧", ("⟦알아채기 3일|noticed in 3 days⟧", "⟦쫓아내기 하루|chased out in a day⟧"))
         + sign(510, 60, 200, "#B4433A", "⟦위험이 커지나|IS DANGER GROWING⟧", ("⟦안 막은 틈 40개|40 open cracks⟧", "⟦가짜 편지 연 사람 30%|30% opened fake letters⟧"))
         + label(390, 272, "⟦초록 팻말: 우리 솜씨|green sign: our skill⟧", 11, "var(--good)") + label(610, 272, "⟦빨간 팻말: 다가오는 위험|red sign: the danger ahead⟧", 11, "var(--bad)")
         + label(380, 302, "⟦두 팻말을 같이 봐야 성이 정말 어떤지 알아요|read both signs together to know how the castle really is⟧", 12, "var(--ink)", cls="d"))

MTTD_I = icon('<circle cx="24" cy="36" r="16" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M24 26 v10 l7 4" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M42 22 c0 -14 18 -14 18 0 v8 h-18z" fill="#E9B44C"/><rect x="40" y="30" width="22" height="4" rx="2" fill="#C9822B"/>')
MTTR_I = icon('<circle cx="24" cy="36" r="16" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M24 26 v10 l7 4" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M44 14 l14 30" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/><path d="M52 40 l12 6 l-6 12 l-12 -6z" fill="#E9B44C"/>')
CAT_I = icon('<path d="M18 22 l-4 -14 l12 6z M46 22 l4 -14 l-12 6z" fill="#8B5E3C"/><circle cx="32" cy="32" r="16" fill="#8B5E3C"/><circle cx="26" cy="30" r="2.5" fill="#142033"/><circle cx="38" cy="30" r="2.5" fill="#142033"/><path d="M29 37 h6 l-3 4z" fill="#E9B44C"/><path d="M10 36 h12 M10 41 h12 M42 36 h12 M42 41 h12" stroke="#142033" stroke-width="1.5"/>')
SLA_I = icon('<rect x="10" y="14" width="40" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="14" width="40" height="10" rx="4" fill="var(--accent)"/><path d="M20 8 v10 M40 8 v10" stroke="#5A3B22" stroke-width="3"/><rect x="18" y="30" width="24" height="16" rx="2" fill="#8B5E3C"/><path d="M22 34 h16 M22 42 h16" stroke="#5A3B22" stroke-width="2"/>')

PAGE = {
    "slug": "metrics", "order": 96,
    "title": ("얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나", "How Fast We Notice, How Fast We Chase Out"),
    "h1": ("<em>보안 지표</em>가 뭐예요?", "What are <em>Security Metrics</em>?"),
    "sub": ("보안 지표(Security Metrics — MTTD·MTTR 등)를 왕의 '우리 성 안전해?'에 느낌 대신 숫자로 답하는 경비 이야기로 풀어봤어요.",
            "Security metrics — MTTD, MTTR and friends — told as a story about a guard who answers the king\'s \'is our castle safe?\' with numbers instead of feelings."),
    "panels": [
        {"svg": P1, "alt": ("왕이 '우리 성, 안전해?' 묻고 경비가 땀을 흘리며 '음… 그런 것 같아요?' 함. 오른쪽 쪽지에 오늘의 느낌: 조용했어요, 종이 좀 울렸어요, 아마 괜찮아요?", "The king asks if the castle is safe; the guard sweats and says um, I think so. A note lists today\'s feeling: it was quiet, the bell rang a bit, probably fine?"),
         "caption": ("왕이 물어요. \"우리 성, 안전해?\" 경비는 느낌으로 대답해요.", "The king asks: is our castle safe? The guard answers by feel."),
         "small": ("\"아마도요\"라고 하면 아무것도 고칠 수 없어요. 느낌은 사람마다 다르고, 어제와 오늘을 비교할 수도 없어요.", "\"Probably\" fixes nothing. Feelings differ from person to person, and you can\'t compare yesterday with today.")},
        {"svg": P2, "alt": ("가방을 든 도둑 옆에 100일 달력. 경비는 땀을 흘림. 종 옆에 고양이 세 마리", "A thief with a bag next to a 100-day calendar; the guard sweats. Three cats sit beside a bell"),
         "caption": ("재지 않으면 도둑이 백 날을 안에 있어도, 종이 하루 백 번 울려도 몰라요.", "Without measuring, you don\'t notice a thief inside for a hundred days — or a bell ringing a hundred times a day."),
         "small": ('도둑은 몰래 오래 머물고(<a href="hunting-ko.html">체류</a>), 종은 고양이 때문에 너무 자주 울려요(<a href="siem-ko.html">큰 화면</a>). 둘 다 세어 보기 전엔 안 보여요.',
                   'Thieves stay hidden for a long time (<a href="hunting-en.html">dwell</a>), and the bell rings too often because of cats (<a href="siem-en.html">the big screen</a>). Neither shows until you count.')},
        {"svg": P3, "hero": True, "alt": ("밤. 시간 선 위에 세 점: 도둑이 들어옴, 종이 울림, 쫓아냄. 첫 구간 위에 '알아채기까지 걸린 시간 (예: 30일)', 둘째 구간 위에 '쫓아내기까지 걸린 시간 (예: 2일)'", "Night. Three points on a timeline: thief gets in, the bell rings, chased out. Over the first span: time until noticed (e.g. 30 days); over the second: time until chased out (e.g. 2 days)"),
         "caption": ("보안 지표는 느낌 대신 숫자예요. 얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나.", "Security metrics are numbers instead of feelings: how fast we notice, how fast we chase out."),
         "small": ("도둑이 들어와서 종이 울릴 때까지, 종이 울리고 도둑을 내보낼 때까지. 이 두 시간만 재도 성이 나아지는지 보여요.", "From the thief getting in to the bell ringing; from the bell to the thief being out. Measure just these two and you can see the castle improve."),
         "tricks": (4, [
             (MTTD_I, ("알아채기까지", "Time to notice"), ("들어와서 종까지 며칠", "days from break-in to bell"), "warm"),
             (MTTR_I, ("쫓아내기까지", "Time to chase out"), ("종부터 문 닫을 때까지", "from the bell to the door shut")),
             (CAT_I, ("고양이 비율", "Cat ratio"), ("울린 종 중 헛울림", "false rings out of all rings")),
             (SLA_I, ("판자 대기 날짜", "Days waiting for boards"), ("틈을 알고 막기까지", "from finding a crack to fixing it"), "calm"),
         ])},
        {"svg": P4, "alt": ("1월부터 6월까지 알아채기까지 걸린 날 막대그래프: 30, 24, 15, 9, 5, 3일로 내려감. 옆 쪽지에 다른 숫자들: 고양이 종 90%→40%, 판자 대기 60일→14일, 가짜 편지 연 사람 30%→8%, 경비견 있는 방 60%→95%", "A bar chart of days until noticed, January to June: 30, 24, 15, 9, 5, 3. A note lists other numbers: cat rings 90% to 40%, board wait 60 to 14 days, opened fake letters 30% to 8%, rooms with a dog 60% to 95%"),
         "caption": ("달마다 그래프를 그려요. 막대가 내려가면 성이 나아지는 거예요.", "Draw the graph every month. When the bars go down, the castle is getting better."),
         "small": ('판자 대기는 <a href="vulnmgmt-ko.html">틈 장부</a>, 가짜 편지 연 사람은 <a href="awareness-ko.html">도둑 수업</a>, 경비견 있는 방은 <a href="edr-ko.html">경비견</a> 이야기예요. 숫자 하나가 기둥 하나씩 비춰요.',
                   'Board wait is the <a href="vulnmgmt-en.html">book of cracks</a>, opened fake letters is the <a href="awareness-en.html">thief lesson</a>, rooms with a dog is the <a href="edr-en.html">guard dogs</a>. Each number lights up one pillar.')},
        {"svg": P5, "alt": ("왕이 '숫자가 나아지니 성도 나아졌구나' 함. 초록 팻말 '우리가 잘하나': 알아채기 3일, 쫓아내기 하루. 빨간 팻말 '위험이 커지나': 안 막은 틈 40개, 가짜 편지 연 사람 30%", "The king says the numbers improved, so did the castle. A green sign, are we doing well: noticed in 3 days, chased out in a day. A red sign, is danger growing: 40 open cracks, 30% opened fake letters"),
         "caption": ("팻말은 두 가지예요. 우리가 잘하나, 위험이 커지나.", "There are two kinds of sign: are we doing well, and is danger growing."),
         "small": ('초록 팻말은 우리 솜씨, 빨간 팻말은 다가오는 <a href="risk-ko.html">위험</a>이에요. 어떤 숫자를 잴지는 <a href="framework-ko.html">다섯 기둥</a>이 알려줘요.',
                   'The green sign is our skill; the red sign is the <a href="risk-en.html">danger</a> ahead. The <a href="framework-en.html">five pillars</a> tell you which numbers to measure.')},
    ],
    "summary": (("<b>보안 지표</b> = \"안전해?\"에 느낌 대신 <b>숫자</b>로 답하기. 도둑이 들어와서 <b>알아채기까지</b>, 알아채서 <b>쫓아내기까지</b>, 종 중 <b>고양이 비율</b>, <b>판자 대기 날짜</b>. 달마다 재서 <b>막대가 내려가면</b> 성이 나아지는 거예요.",
                 "<b>Security metrics</b> = answering \"is it safe?\" with <b>numbers</b>, not feelings: <b>time to notice</b>, <b>time to chase out</b>, the <b>cat ratio</b> among rings, <b>days waiting for boards</b>. Measure monthly — <b>when the bars go down</b>, the castle is getting better."),
                ("Security Metrics. MTTD(평균 탐지 시간), MTTR(평균 대응·복구 시간), 체류 시간, 오탐률, 패치 SLA 준수율, 피싱 클릭률·신고율, 커버리지 같은 숫자로 보안 상태를 재요. KPI는 우리 활동의 성과를, KRI는 커지는 위험을 보여 주고, 둘을 함께 추세로 봐요.",
                 "Security metrics measure the state of security in numbers: MTTD (mean time to detect), MTTR (mean time to respond/recover), dwell time, false-positive rate, patch SLA compliance, phishing click and report rates, coverage. KPIs show how well our work performs, KRIs show growing risk — and both are read as trends.")),
    "glossary": [
        ("알아채기까지", "MTTD (Mean Time to Detect)", ("도둑이 들어와서 종이 울릴 때까지.", "From the thief getting in to the bell ringing."), ("평균 며칠인지 세요. 짧을수록 좋아요.", "Count the average days. Shorter is better.")),
        ("쫓아내기까지", "MTTR (Mean Time to Respond)", ("종이 울리고 도둑을 내보낼 때까지.", "From the bell to the thief being out."), ('순서표가 좋을수록 짧아져요. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'A better book of steps makes it shorter. → <a href="incident-en.html">the book for when a thief gets in</a>')),
        ("체류 시간", "Dwell time", ("도둑이 안에 있던 날수 전부.", "All the days the thief was inside."), ('종을 기다리지 않고 찾으러 가면 줄어요. → <a href="hunting-ko.html">종을 기다리지 않는 파수꾼</a>', 'Goes down when you go looking instead of waiting for the bell. → <a href="hunting-en.html">the watchman who doesn\'t wait</a>')),
        ("오탐률", "False positive rate", ("고양이 비율.", "The cat ratio."), ('울린 종 중 헛울림이 몇 개인지. 규칙을 손보면 줄어요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'How many rings were false. Tuning the rules brings it down. → <a href="siem-en.html">the guard room\'s big screen</a>')),
        ("패치 SLA", "Patch SLA", ("판자 대기 약속.", "The promised wait for boards."), ('틈을 알고 며칠 안에 막기로 했는지, 지켰는지. → <a href="vulnmgmt-ko.html">매달 도는 틈 장부</a>', 'How many days you promised to fix a crack within, and whether you kept it. → <a href="vulnmgmt-en.html">the monthly book of cracks</a>')),
        ("클릭률 · 신고율", "Click rate, report rate", ("가짜 편지 연 사람, 신고한 사람.", "Who opened the fake letter, who reported it."), ('연 사람은 줄고 신고한 사람은 늘어야 해요. → <a href="awareness-ko.html">도둑 수업</a>', 'Openers should fall and reporters rise. → <a href="awareness-en.html">the thief lesson</a>')),
        ("커버리지", "Coverage", ("경비견이 있는 방의 비율.", "The share of rooms with a dog."), ('모르는 방은 지킬 수 없어요. → <a href="edr-ko.html">방마다 한 마리 경비견</a>, <a href="asm-ko.html">바깥에서 세는 문</a>', 'You can\'t guard a room you don\'t know about. → <a href="edr-en.html">a dog in every room</a>, <a href="asm-en.html">counting doors from outside</a>')),
        ("KPI vs KRI", "KPI vs KRI", ("초록 팻말과 빨간 팻말.", "The green sign and the red sign."), ('KPI는 우리 솜씨(성과), KRI는 커지는 위험. 둘을 같이 봐요. → <a href="risk-ko.html">위험 저울</a>', 'KPI is our skill (performance), KRI is growing risk. Read both. → <a href="risk-en.html">the risk scale</a>')),
    ],
}
