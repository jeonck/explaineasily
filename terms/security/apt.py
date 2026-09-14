from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
FOREIGN = dict(hat="#7D3C98", shirt="#1F618D")            # 다른 나라 왕 (후원자)
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
CARPENTER_THIEF = dict(hat="#E9B44C", shirt="#4A5A72", face=MASK)   # 목수로 변장한 도둑
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def crown(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 10 l-4 -30 l14 12 l16 -22 l16 22 l14 -12 l-4 30z" fill="#E9B44C" stroke="#C9822B" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="-28" y="8" width="56" height="10" rx="3" fill="#C9822B"/><circle cx="-16" cy="-4" r="3" fill="var(--bad)"/><circle cy="-10" r="3" fill="#5B8DEF"/><circle cx="16" cy="-4" r="3" fill="var(--bad)"/></g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def calendar(x, y, text, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-34" width="80" height="72" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect x="-40" y="-34" width="80" height="18" rx="6" fill="var(--bad)"/><rect x="-26" y="-42" width="6" height="14" rx="3" fill="#5A3B22"/><rect x="20" y="-42" width="6" height="14" rx="3" fill="#5A3B22"/>'
            + label(0, 16, text, 15, "#142033", cls="d") + "</g>")


def chest(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/><rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/></g>')


def page(x, y, s=1.0, rot=0):
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-12" y="-16" width="24" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-6 -6 h12 M-6 2 h12 M-6 10 h8" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/></g>'


# 1. 보통 도둑은 하룻밤 — 이 도둑은 몇 달째 조용해요
P1 = svg(320, night(320) + '<path d="M380 20 v280" stroke="#3B4C6B" stroke-width="2" stroke-dasharray="8 6"/>'
         + label(190, 44, "⟦보통 도둑|an ordinary thief⟧", 13, "#F5E6B8", cls="d")
         + person(90, 110, s=0.85, extra=BAG, **THIEF) + chest(200, 200, 1.0) + bell(270, 100, 0.7, ring=True) + person(300, 130, s=0.7, face=SMILE, **BLUE)
         + label(190, 250, "⟦하룻밤 — 종이 울리고 끝|one night — the bell rings, done⟧", 12, "#C9D5E6")
         + label(570, 44, "⟦이 도둑|this thief⟧", 13, "#F5E6B8", cls="d")
         + person(470, 96, s=0.7, **THIEF) + '<rect x="440" y="150" width="120" height="70" fill="var(--stone-dark)"/>' + calendar(640, 150, "⟦3달째|month 3⟧", 0.9) + bell(585, 96, 0.6, ring=False)
         + label(570, 250, "⟦몇 달째 — 아무 소리도 없어요|for months — not a sound⟧", 12, "#C9D5E6")
         + label(380, 300, "⟦종은 조용한데, 도둑은 이미 안에 있어요|the bell is quiet, but the thief is already inside⟧", 13, "#F5E6B8", cls="d"))

# 2. 왜 못 알아채나 — 변장하고, 발자국 지우고, 조금씩만
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(95, 90, s=0.85, **CARPENTER_THIEF) + label(130, 230, "⟦목수 옷을 입어요|wears the carpenter\'s coat⟧", 12, "var(--ink)") + label(130, 252, "⟦문지기가 인사해요|the doorkeeper waves hello⟧", 10, "var(--muted)")
         + foot(330, 150, -10, "#C9A0A0") + foot(365, 130, -10, "#D9B8B8") + foot(400, 110, -10, "#EBD0D0")
         + '<path d="M300 200 l70 -60" stroke="#5A3B22" stroke-width="5" stroke-linecap="round"/><path d="M290 214 l16 -22 l14 10 l-16 22z" fill="#C9A86A"/>'
         + label(380, 230, "⟦발자국을 지워요|wipes the footprints away⟧", 12, "var(--ink)") + label(380, 252, "⟦일지에 남을 게 없어요|nothing left in the log book⟧", 10, "var(--muted)")
         + chest(600, 130, 1.2) + page(680, 100, 0.8, 15) + '<path d="M640 120 q20 -30 34 -22" stroke="var(--bad)" stroke-width="2.5" fill="none" stroke-dasharray="4 3"/>'
         + label(630, 230, "⟦하루에 한 장씩만|one page a day, no more⟧", 12, "var(--ink)") + label(630, 252, "⟦종이 울릴 만큼 크지 않아요|never big enough to ring the bell⟧", 10, "var(--muted)")
         + label(380, 300, "⟦크게 움직이지 않으니, 아무도 몰라요|they never move big, so nobody notices⟧", 13, "var(--ink)", cls="d"))

# 3. APT = 나라의 후원을 받는 끈질긴 도둑 무리 (hero)
P3 = svg(360, night(360)
         + person(40, 110, s=0.9, face=EYES, **FOREIGN) + label(72, 232, "⟦다른 나라 왕|a foreign king⟧", 11, "#C9D5E6")
         + '<path d="M120 150 h50" stroke="#E9B44C" stroke-width="4" stroke-linecap="round"/><circle cx="150" cy="150" r="9" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>'
         + paper(180, 40, 190, 120, "⟦후원자의 쪽지|THE SPONSOR\'S NOTE⟧", ("⟦왕관 하나만|the crown, just that⟧", "⟦시간은 얼마든지|take all the time you need⟧", "⟦들키지 말 것|do not get noticed⟧"))
         + person(400, 120, s=0.95, **THIEF) + person(490, 140, s=0.75, **CARPENTER_THIEF) + person(560, 155, s=0.65, hat=None, shirt="#2E3D57", face=MASK)
         + label(490, 252, "⟦끈질긴 도둑 무리|the persistent gang⟧", 13, "#F5E6B8", cls="d")
         + small_castle(640, 90, 0.5) + crown(680, 200, 0.5) + label(680, 232, "⟦우리 성의 왕관|our crown⟧", 11, "#C9D5E6")
         + label(380, 300, "⟦후원자가 있고, 목표는 하나고, 몇 달이든 기다려요|a sponsor, one target, and all the months it takes⟧", 13, "#F5E6B8", cls="d")
         + label(380, 336, "⟦그래서 끈질긴 도둑이에요 — 하룻밤 도둑이 아니에요|that\'s why they\'re called persistent — not one-night thieves⟧", 12, "#C9D5E6"))

# 4. 다섯 달의 걸음 — 한 달에 한 걸음
STEPS = (("⟦1월|Jan⟧", "⟦가짜 편지|a fake letter⟧", "var(--bad)"), ("⟦2월|Feb⟧", "⟦요리사 방 하나|the cook\'s room⟧", "var(--bad)"),
         ("⟦3월|Mar⟧", "⟦옆방 열쇠|the next room\'s key⟧", "var(--bad)"), ("⟦4월|Apr⟧", "⟦왕관 방|the crown room⟧", "var(--accent)"),
         ("⟦5월|May⟧", "⟦한 장씩 밖으로|out, one page at a time⟧", "#E9B44C"))
P4 = svg(340, sky(340)
         + '<rect x="40" y="30" width="680" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="28" rx="8" fill="#C9A86A"/>' + label(380, 49, "⟦도둑 무리가 지나간 다섯 달|FIVE MONTHS OF THE GANG\'S PATH⟧", 12, "#142033", cls="d")
         + '<path d="M110 150 H650" stroke="var(--bad)" stroke-width="4" fill="none" stroke-dasharray="8 6"/>'
         + "".join(f'<circle cx="{110 + i * 135}" cy="150" r="12" fill="{c}"/>' + label(110 + i * 135, 118, m, 12, "#142033", cls="d") + label(110 + i * 135, 190, e, 10, "#142033") for i, (m, e, c) in enumerate(STEPS))
         + person(555, 205, s=0.4, **THIEF) + label(380, 240, "⟦종은 한 번도 안 울렸어요|the bell never rang once⟧", 11, "#142033")
         + label(380, 296, "⟦한 달에 한 걸음 — 종이 울릴 일이 없어요|one step a month — nothing ever rings the bell⟧", 13, "var(--ink)", cls="d")
         + label(380, 324, "⟦들어온 지 다섯 달, 아무도 몰랐어요|five months inside, and nobody knew⟧", 12, "var(--muted)"))

# 5. 알아채려면 — 망루 소식 + 버릇 + 헌팅
P5 = svg(320, sky(320)
         + bubble(30, 30, 210, 34, "⟦옆 성에서 이 무리를 봤대요|the next castle saw this gang⟧", 10, "var(--panel)", "var(--line)", "bottom") + person(100, 110, s=0.8, face=SMILE, **GUARD)
         + label(130, 240, "⟦망루 친구의 소식|word from the watchtower⟧", 12, "var(--ink)") + label(130, 262, "⟦누가 오는지 미리 알아요|knows who\'s coming, ahead of time⟧", 10, "var(--muted)")
         + paper(300, 40, 170, 110, "⟦이 무리의 버릇|THIS GANG\'S HABITS⟧", ("⟦목수 옷|carpenter\'s coat⟧", "⟦하루 한 장|one page a day⟧", "⟦발자국 지움|wipes footprints⟧"))
         + label(385, 240, "⟦버릇 장부|the habits book⟧", 12, "var(--ink)") + label(385, 262, "⟦어떻게 움직이는지 알아요|knows how they move⟧", 10, "var(--muted)")
         + person(600, 100, s=0.85, face=EYES, **BLUE) + '<g transform="translate(690,150)"><rect x="-10" y="-18" width="20" height="36" rx="4" fill="#E9B44C"/><rect x="-6" y="-12" width="12" height="20" fill="#FFF3B0"/><path d="M-6 -22 h12" stroke="#5A3B22" stroke-width="3"/></g>'
         + label(630, 240, "⟦등불 든 파수꾼|the lantern guard⟧", 12, "var(--ink)") + label(630, 262, "⟦종 안 울려도 찾아 나서요|goes looking before any bell⟧", 10, "var(--muted)")
         + label(380, 300, "⟦셋이 합쳐야 조용한 도둑을 찾아요|it takes all three to find a quiet thief⟧", 13, "var(--ink)", cls="d"))

SPONSOR_I = icon('<path d="M18 42 l-4 -22 l10 8 l8 -14 l8 14 l10 -8 l-4 22z" fill="#7D3C98" stroke="#5B2C6F" stroke-width="2" stroke-linejoin="round"/><rect x="14" y="42" width="36" height="7" rx="2" fill="#5B2C6F"/><circle cx="50" cy="16" r="8" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>')
MONTHS_I = icon('<rect x="10" y="14" width="44" height="40" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="10" y="14" width="44" height="10" rx="5" fill="var(--bad)"/><path d="M18 34 h8 M30 34 h8 M42 34 h6 M18 44 h8 M30 44 h8" stroke="#142033" stroke-width="3" stroke-linecap="round"/>')
WIPE_I = icon('<ellipse cx="22" cy="40" rx="6" ry="9" fill="#C9A0A0"/><ellipse cx="22" cy="26" rx="4" ry="4" fill="#C9A0A0"/><path d="M34 50 l16 -26" stroke="#5A3B22" stroke-width="4" stroke-linecap="round"/><path d="M28 56 l8 -12 l8 6 l-8 12z" fill="#C9A86A"/>')
DRIP_I = icon('<rect x="12" y="34" width="30" height="18" rx="2" fill="#8B5E3C"/><path d="M12 34 h30 v-3 a15 6 0 0 0 -30 0z" fill="#5A3B22"/><rect x="38" y="10" width="14" height="18" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2" transform="rotate(15 45 19)"/><path d="M30 30 q6 -12 12 -10" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="3 2"/>')

PAGE = {
    "slug": "apt", "order": 69,
    "title": ("몇 달을 기다리는 끈질긴 도둑 무리", "The Gang That Waits for Months"),
    "h1": ("<em>APT</em>가 뭐예요?", "What is an <em>APT</em>?"),
    "sub": ("지능형 지속 위협(APT, Advanced Persistent Threat)을 나라의 후원을 받고 몇 달이든 숨어서 왕관 하나만 노리는 도둑 무리 이야기로 풀어봤어요.",
            "Advanced Persistent Threat, told as a story about a gang with a royal sponsor that hides for months and wants just one thing: the crown."),
    "panels": [
        {"svg": P1, "alt": ("밤. 왼쪽엔 보통 도둑이 상자를 열다 종이 울려 경비실 친구에게 잡힘. 오른쪽엔 도둑이 벽 뒤에 숨어 있고 달력은 3달째, 종은 조용함", "Night. On the left an ordinary thief opens a chest, the bell rings, the guard catches him. On the right a thief hides behind a wall, the calendar says month 3, the bell is silent"),
         "caption": ("보통 도둑은 하룻밤이에요. 그런데 이 도둑은 몇 달째 조용해요.", "An ordinary thief takes one night. This thief has been quiet for months."),
         "small": ('보통 도둑은 상자를 열다 <a href="edr-ko.html">종</a>이 울려요. 이 도둑은 종이 한 번도 안 울렸는데, 벌써 성 안에 있어요.',
                   'An ordinary thief opens a chest and the <a href="edr-en.html">bell</a> rings. This one never rang the bell — and is already inside.')},
        {"svg": P2, "alt": ("목수 옷을 입은 도둑, 빗자루로 지워지는 발자국, 상자에서 종이 한 장만 빠져나가는 그림", "A thief in the carpenter\'s coat, footprints being swept away with a broom, and a single page slipping out of a chest"),
         "caption": ("변장하고, 발자국을 지우고, 하루에 한 장씩만 옮겨요.", "They disguise themselves, wipe their footprints, and move one page a day."),
         "small": ('<a href="log-ko.html">일지</a>에 남을 게 없고, 종이 울릴 만큼 크게 움직이지도 않아요. 그래서 아무도 몰라요.',
                   'Nothing is left in the <a href="log-en.html">log book</a>, and they never move big enough to ring a bell. So nobody notices.')},
        {"svg": P3, "hero": True, "alt": ("밤. 다른 나라 왕이 금화를 건네고, 쪽지엔 '왕관 하나만, 시간은 얼마든지, 들키지 말 것'. 도둑 셋이 한 무리. 오른쪽엔 우리 성과 왕관", "Night. A foreign king hands over gold; the note says: the crown, take all the time you need, do not get noticed. Three thieves as one gang. On the right, our castle and its crown"),
         "caption": ("APT는 나라의 후원을 받는 끈질긴 도둑 무리예요.", "An APT is a persistent gang of thieves with a country behind them."),
         "small": ("다른 나라 왕이 돈을 대요. 목표는 왕관 하나. 시간은 얼마든지 써도 돼요. 그래서 하룻밤 도둑과 달라요.", "A foreign king pays the bill. The target is one crown. They may take all the time they need. That\'s what makes them different from a one-night thief."),
         "tricks": (4, [
             (SPONSOR_I, ("후원자가 있어요", "A sponsor"), ("돈도 시간도 넉넉해요", "plenty of money and time"), "warm"),
             (MONTHS_I, ("몇 달을 숨어요", "Hides for months"), ("하룻밤이 아니에요", "not just one night")),
             (WIPE_I, ("발자국을 지워요", "Wipes footprints"), ("일지에 안 남게", "nothing left in the log")),
             (DRIP_I, ("조금씩 옮겨요", "Moves a little at a time"), ("종이 안 울리게", "never enough to ring the bell"), "calm"),
         ])},
        {"svg": P4, "alt": ("다섯 달 지도: 1월 가짜 편지, 2월 요리사 방, 3월 옆방 열쇠, 4월 왕관 방, 5월 한 장씩 밖으로. 종은 한 번도 안 울림", "A five-month map: January a fake letter, February the cook\'s room, March the next room\'s key, April the crown room, May out one page at a time. The bell never rang"),
         "caption": ("한 달에 한 걸음씩 옮겨요. 다섯 달 뒤엔 왕관 방에 있어요.", "One step a month. Five months later they\'re in the crown room."),
         "small": ('<a href="phishing-ko.html">가짜 편지</a>로 방 하나에 들어와요. 그 방에서 옆방 열쇠를 찾고, 또 옆방으로 가요. 들어온 지 다섯 달, 아무도 몰랐어요.',
                   'A <a href="phishing-en.html">fake letter</a> gets them into one room. There they find the next room\'s key, and move on. Five months inside, and nobody knew.')},
        {"svg": P5, "alt": ("망루 친구가 '옆 성에서 이 무리를 봤대요', 이 무리의 버릇 장부(목수 옷, 하루 한 장, 발자국 지움), 등불 든 파수꾼이 종 없이도 찾아 나섬", "The watchtower friend says the next castle saw this gang; a habits book lists carpenter\'s coat, one page a day, wiped footprints; a lantern guard goes looking without a bell"),
         "caption": ("알아채려면 망루 소식, 버릇 장부, 등불이 다 필요해요.", "To catch them you need the watchtower, the habits book, and a lantern."),
         "small": ('<a href="cti-ko.html">망루 친구</a>가 누가 오는지 알려주고, <a href="ttp-ko.html">버릇 장부</a>로 어떻게 움직이는지 알고, <a href="hunting-ko.html">등불 든 파수꾼</a>이 종을 기다리지 않고 찾아 나서요.',
                   'The <a href="cti-en.html">watchtower friend</a> says who is coming, the <a href="ttp-en.html">habits book</a> says how they move, and the <a href="hunting-en.html">lantern guard</a> goes looking instead of waiting for a bell.')},
    ],
    "summary": (("<b>APT</b> = 나라의 후원을 받고 <b>왕관 하나만</b> 노리며, <b>몇 달이든 숨어서</b> 발자국을 지우고 <b>조금씩 옮기는</b> 끈질긴 도둑 무리.",
                 "<b>APT</b> = a persistent gang with a country behind it that wants <b>one crown</b>, <b>hides for months</b>, wipes its footprints, and <b>moves a little at a time</b>."),
                ("APT(Advanced Persistent Threat, 지능형 지속 위협). 국가 등 든든한 후원을 받는 공격 그룹이 특정 목표를 정해 오랫동안 은밀하게 침투·잠복·이동하며 정보를 빼내는 공격이에요. 탐지에는 위협 인텔리전스, TTP 분석, 위협 헌팅이 함께 필요해요.",
                 "Advanced Persistent Threat: a well-funded attack group, often state-sponsored, picks a specific target and stays hidden inside for a long time, moving quietly and stealing information. Catching one takes threat intelligence, TTP analysis, and threat hunting together.")),
    "glossary": [
        ("끈질긴 도둑 무리", "APT (Advanced Persistent Threat)", ("몇 달을 기다리는 도둑 무리.", "The gang that waits for months."), ("후원자, 목표 하나, 긴 시간. 하룻밤 도둑과 달라요.", "A sponsor, one target, a long time. Not a one-night thief.")),
        ("나라의 후원", "State-sponsored actor", ("다른 나라 왕이 돈을 대요.", "A foreign king pays."), ("그래서 돈도 시간도 넉넉해요. 잡혀도 다음 무리가 와요.", "So money and time are plentiful. Catch one, and the next gang comes.")),
        ("숨어 있던 시간", "Dwell time", ("들어온 날부터 들킨 날까지.", "From the day they got in to the day they were found."), ('몇 달이 흔해요. 이 시간을 줄이는 게 <a href="hunting-ko.html">헌팅</a>의 일이에요.', 'Months is common. Shrinking it is what <a href="hunting-en.html">hunting</a> is for.')),
        ("옆방으로 가기", "Lateral movement", ("한 방에서 옆방 열쇠 찾기.", "Finding the next room\'s key from inside one room."), ('요리사 방 → 옆방 → 왕관 방. <a href="ndr-ko.html">복도 파수꾼</a>이 보는 게 이거예요.', 'Cook\'s room → next room → crown room. This is what the <a href="ndr-en.html">corridor guard</a> watches for.')),
        ("자리 지키기", "Persistence", ("쫓겨나도 다시 들어오는 뒷문.", "A back door for getting back in."), ("문 하나를 막아도 미리 파 둔 다른 길로 돌아와요.", "Block one door and they return through another they dug earlier.")),
        ("한 장씩 밖으로", "Exfiltration", ("종이를 몰래 성 밖으로.", "Sneaking papers out of the castle."), ('한꺼번에 가져가면 종이 울리니까 조금씩. <a href="dlp-ko.html">빨간 도장</a>이 막는 게 이거예요.', 'All at once would ring the bell, so a little at a time. This is what the <a href="dlp-en.html">red stamp</a> guards against.')),
        ("무리 이름", "Threat group names (APT28 …)", ("무리마다 붙이는 번호와 별명.", "A number and a nickname for each gang."), ('APT28, Lazarus 같은 이름. <a href="attack-ko.html">도둑 백과사전</a>에 무리별 버릇이 적혀 있어요.', 'Names like APT28 or Lazarus. The <a href="attack-en.html">thief encyclopedia</a> lists each gang\'s habits.')),
        ("도둑의 걸음", "Kill chain", ("편지부터 왕관까지의 순서.", "The steps from letter to crown."), ('어느 걸음에서든 끊으면 실패해요. → <a href="killchain-ko.html">도둑의 일곱 걸음</a>', 'Cut any step and the whole thing fails. → <a href="killchain-en.html">the seven steps of a thief</a>')),
    ],
}
