from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
COOK = dict(hat="#FFF", shirt="#FFF")
MAID = dict(hat=None, shirt="#7B3FA0")
PRINCE = dict(hat="#E9B44C", shirt="#7B3FA0")
FOLK = ((None, "#4A5A72"), ("#E9B44C", "#2E7D6B"), (None, "#C9822B"), ("var(--stone-dark)", "#4A5A72"), (None, "#2E7D6B"), ("#FFF", "#FFF"))
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def letter(x, y, s=1.0, seal="var(--bad)", rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-30" y="-20" width="60" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-30 -20 l30 20 l30 -20" stroke="#C9A86A" stroke-width="2" fill="none"/><circle cy="4" r="6" fill="{seal}"/></g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def door(x, y, s=1.0, open_=False):
    if open_:
        return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-40" width="44" height="80" rx="3" fill="var(--night)"/><path d="M-22 -40 h30 l-10 12 v76 l-20 -8z" fill="{WOOD}"/></g>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-40" width="44" height="80" rx="3" fill="{WOOD}"/><circle cx="12" cy="2" r="3" fill="#E9B44C"/></g>'


def board(x, y, w, h, title, lines):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#2E4A3E" stroke="#5A3B22" stroke-width="5"/>' + label(w / 2, 30, title, 14, "#F5E6B8", cls="d")
    for i, t in enumerate(lines):
        out += label(20, 60 + i * 24, t, 12, "#F5E6B8", "start")
    return out + "</g>"


# 1. 벽도 종도 개도 있는데 — 요리사가 문을 열어줬어요
P1 = svg(320, sky(320) + castle(60, 30, 0.6) + bell(160, 40, 0.5, ring=False) + dog(330, 200, 0.7, asleep=True)
         + door(440, 200, 1.0, open_=True) + person(470, 130, s=0.8, face=SMILE, **COOK) + letter(540, 110, 0.9, rot=10)
         + bubble(520, 30, 200, 34, "⟦왕의 편지래요! 들어오세요|it says it\'s from the king! come in⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(620, 150, s=0.85, hat="#E9B44C", shirt="#4A5A72", face=MASK, extra=BAG) + label(650, 262, "⟦'편지 배달부'|the 'mail carrier'⟧", 11, "var(--bad)")
         + label(380, 300, "⟦도둑은 벽을 넘지 않았어요 — 사람이 문을 열어줬어요|the thief didn\'t climb the wall — a person opened the door⟧", 12, "var(--ink)"))

# 2. 성 사람 200명 중 경비는 10명 — 도둑은 나머지에게 말을 걸어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(person(40 + i * 44, 60, s=0.4, face=EYES, **GUARD) for i in range(4))
         + label(120, 140, "⟦경비 10명|10 guards⟧", 12, "var(--good)", cls="d")
         + "".join(person(240 + (i % 9) * 52, 50 + (i // 9) * 60, s=0.4, hat=h, shirt=sh, face=EYES) for i, (h, sh) in enumerate([FOLK[j % len(FOLK)] for j in range(18)]))
         + label(450, 190, "⟦요리사, 하녀, 목수, 왕자… 190명|cooks, maids, carpenters, princes… 190 people⟧", 12, "var(--ink)", cls="d")
         + person(690, 170, s=0.7, face=MASK) + "".join(f'<path d="M{690} {200} Q{600} {150} {x} {y}" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="4 4"/>' for x, y in ((300, 100), (400, 140), (520, 100)))
         + label(380, 270, "⟦도둑은 경비 말고 다른 사람한테 말을 걸어요 — 편지로, 전화로, 변장으로|the thief talks to everyone but the guards — by letter, by voice, in disguise⟧", 11, "var(--muted)"))

# 3. 도둑 수업 (hero)
P3 = svg(360, sky(360)
         + board(200, 30, 360, 190, "⟦도둑 알아보기 수업|THIEF-SPOTTING CLASS⟧", ("⟦① 모르는 편지의 도장은 먼저 의심|① doubt the seal on a stranger\'s letter⟧", "⟦② '지금 당장!'은 도둑의 말버릇|② 'right now!' is how thieves talk⟧", "⟦③ 열쇠는 누구에게도 안 불러줘요|③ never read your key out loud⟧", "⟦④ 이상하면 경비실에 쪽지 한 장|④ feels off? one note to the guard room⟧", "⟦⑤ 걸려도 괜찮아요, 말해 주면 돼요|⑤ fooled? that\'s fine — just tell us⟧"))
         + person(120, 100, s=0.8, face=SMILE, **BLUE) + '<rect x="185" y="140" width="30" height="4" fill="#5A3B22" transform="rotate(-30 185 140)"/>'
         + "".join(person(x, 250, s=0.5, hat=h, shirt=sh, face=SMILE) for x, (h, sh) in zip((230, 300, 370, 440, 510, 580), FOLK))
         + label(380, 330, "⟦경비만이 아니라 성 사람 모두가 들어요 — 짧게, 자주|not just the guards — everyone in the castle, short and often⟧", 12, "var(--ink)", cls="d")
         + label(380, 350, "⟦요리사도 왕자도 같은 자리에서|the cook and the prince in the same seat⟧", 11, "var(--muted)"))

# 4. 가짜 편지 연습
BARS = ((60, 6), (35, 20), (12, 45))
P4 = svg(320, sky(320)
         + person(50, 60, s=0.7, face=SMILE, **BLUE) + letter(130, 100, 0.9, seal="var(--accent)", rot=-10) + label(90, 180, "⟦경비실이 보낸 가짜 편지|a fake letter from the guard room⟧", 10, "var(--muted)")
         + label(90, 198, "⟦(도둑 흉내, 진짜처럼)|(pretending to be the thief)⟧", 10, "var(--muted)")
         + '<path d="M190 100 L240 100" stroke="var(--muted)" stroke-width="3"/><path d="M230 90 L242 100 L230 110" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + '<g transform="translate(260,30)"><rect width="460" height="230" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + "".join(f'<rect x="{50 + i * 140}" y="{190 - o * 2.5}" width="40" height="{o * 2.5}" rx="3" fill="var(--bad)"/><rect x="{96 + i * 140}" y="{190 - r * 2.5}" width="40" height="{r * 2.5}" rx="3" fill="var(--good)"/>' + label(93 + i * 140, 210, m, 11, "var(--muted)") for i, ((o, r), m) in enumerate(zip(BARS, ("⟦3월|March⟧", "⟦6월|June⟧", "⟦9월|September⟧"))))
         + '<rect x="40" y="16" width="12" height="12" fill="var(--bad)"/>' + label(58, 27, "⟦편지를 연 사람|opened the letter⟧", 11, "var(--ink)", "start") + '<rect x="200" y="16" width="12" height="12" fill="var(--good)"/>' + label(218, 27, "⟦경비실에 쪽지 보낸 사람|sent a note to the guard room⟧", 11, "var(--ink)", "start") + "</g>"
         + label(380, 295, "⟦연 사람은 줄고, 쪽지 보낸 사람은 늘어요 — 혼내지 않으니까요|fewer open it, more report it — because nobody gets scolded⟧", 12, "var(--ink)"))

# 5. 요리사가 종을 울려요
P5 = svg(300, sky(300)
         + person(80, 100, s=0.9, face=EYES, **COOK) + letter(170, 130, 1.0, rot=8) + bubble(60, 30, 220, 34, "⟦도장이 이상한데… 경비실에 쪽지|this seal looks off… a note to the guards⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + '<path d="M240 160 L330 160" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 5"/><path d="M320 150 L332 160 L320 170" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + person(360, 110, s=0.8, face=SMILE, **BLUE) + bell(460, 90, 1.0, ring=True) + label(460, 165, "⟦울렸다!|it rang!⟧", 14, "var(--ink)", cls="d")
         + person(620, 150, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=MASK + SWEAT, extra=BAG) + label(650, 262, "⟦문 앞에서 돌아가요|turned away at the door⟧", 11, "var(--bad)")
         + label(380, 285, "⟦이제 성 사람 모두가 파수꾼이에요 — 경비 10명이 아니라 200명|now everyone in the castle is a lookout — not 10 guards, but 200⟧", 12, "var(--ink)"))

SHORT_I = icon('<circle cx="32" cy="32" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 18 v14 l8 4" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M8 54 h6 M18 54 h6 M28 54 h6 M38 54 h6 M48 54 h6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
REAL_I = icon('<rect x="10" y="16" width="44" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M10 16 l22 16 l22 -16" stroke="#C9A86A" stroke-width="2" fill="none"/><circle cx="32" cy="38" r="6" fill="var(--accent)"/>')
KIND_I = icon(f'<circle cx="32" cy="24" r="12" fill="{SKIN}"/><circle cx="27" cy="22" r="2" fill="var(--night)"/><circle cx="37" cy="22" r="2" fill="var(--night)"/><path d="M26 29 q6 5 12 0" stroke="var(--night)" stroke-width="2" fill="none"/><rect x="20" y="38" width="24" height="16" rx="5" fill="#4A5A72"/><path d="M46 12 l4 -4 l4 4 l-4 4z" fill="var(--good)"/>')
NOTE_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 32 h20 M22 40 h12" stroke="#C9A86A" stroke-width="3" stroke-linecap="round"/><path d="M40 4 l8 8" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "awareness", "order": 58,
    "title": ("성 사람 모두가 듣는 도둑 수업", "The Thief-Spotting Class for Everyone"),
    "h1": ("<em>보안 인식 교육</em>이 뭐예요?", "What is <em>Security Awareness Training</em>?"),
    "sub": ("보안 인식 교육(Security Awareness Training)을 경비만이 아니라 성 사람 모두가 듣는 도둑 알아보기 수업 이야기로 풀어봤어요.",
            "Security awareness training, told as a story about a thief-spotting class that everyone in the castle attends — not just the guards."),
    "panels": [
        {"svg": P1, "alt": ("성벽, 종, 자는 경비견이 있는데 요리사가 '왕의 편지래요!' 하며 문을 열어 주고, 편지 배달부로 변장한 도둑이 들어옴", "A wall, a bell, a sleeping dog — and a cook opening the door saying it\'s from the king, as a thief dressed as a mail carrier walks in"),
         "caption": ("벽도 종도 개도 있는데, 요리사가 문을 열어줬어요.", "There\'s a wall, a bell, a dog — and the cook opened the door."),
         "small": ('도둑은 벽을 넘지 않았어요. <a href="phishing-ko.html">가짜 편지</a> 한 장으로 사람이 문을 열게 했어요.',
                   'The thief never climbed the wall. One <a href="phishing-en.html">fake letter</a> got a person to open the door.')},
        {"svg": P2, "alt": ("경비 10명과 요리사·하녀·목수·왕자 190명. 도둑이 경비가 아닌 사람들에게 점선으로 말을 걺", "10 guards and 190 cooks, maids, carpenters, and princes. Dotted lines show the thief talking to everyone but the guards"),
         "caption": ("성 사람 200명 중 경비는 10명이에요. 도둑은 나머지에게 말을 걸어요.", "Ten of the castle\'s 200 people are guards. The thief talks to the other 190."),
         "small": ("편지로, 목소리로, 변장으로. 경비만 도둑을 알아보면, 나머지 190개의 문이 열려 있는 거예요.", "By letter, by voice, in disguise. If only the guards can spot a thief, 190 doors are standing open.")},
        {"svg": P3, "hero": True, "alt": ("칠판: 도둑 알아보기 수업 — 모르는 편지의 도장은 먼저 의심, '지금 당장!'은 도둑의 말버릇, 열쇠는 누구에게도 안 불러줘요, 이상하면 경비실에 쪽지, 걸려도 괜찮아요. 경비실 친구가 가르치고 요리사·왕자 등 여섯이 앉아 있음", "A chalkboard — thief-spotting class: doubt a stranger\'s seal, right now! is how thieves talk, never read your key out loud, feels off? one note to the guard room, fooled? that\'s fine. A blue hat teaches; six castle folk sit"),
         "caption": ("보안 인식 교육은 성 사람 모두가 듣는 도둑 수업이에요.", "Security awareness training is a thief-spotting class for everyone in the castle."),
         "small": ("요리사도 왕자도 같은 자리에서 들어요. 길게 한 번이 아니라 짧게 자주. 걸려도 혼내지 않고, '이상하면 쪽지 한 장'만 기억하게 해요.", "The cook and the prince sit in the same seat. Not one long lecture but short and often. Nobody gets scolded for being fooled — everyone remembers one thing: feels off? send a note."),
         "tricks": (4, [
             (SHORT_I, ("짧게, 자주", "Short and often"), ("일 년에 한 번은 잊어요", "once a year is forgotten"), "warm"),
             (REAL_I, ("진짜처럼 연습", "Practice for real"), ("가짜 편지를 보내 봐요", "send a fake letter")),
             (KIND_I, ("혼내지 않기", "No scolding"), ("걸리면 배우는 날", "fooled today, wiser tomorrow")),
             (NOTE_I, ("쪽지 한 장", "One note"), ("이상하면 경비실로", "feels off? tell the guards"), "calm"),
         ])},
        {"svg": P4, "alt": ("경비실이 보낸 가짜 편지. 그래프: 3월엔 60명이 열고 6명이 쪽지, 6월엔 35명·20명, 9월엔 12명·45명", "A fake letter from the guard room. Chart: in March 60 opened it and 6 reported; June 35 and 20; September 12 and 45"),
         "caption": ("가짜 편지를 보내 연습해요. 열면 배우고, 쪽지 보내면 칭찬받아요.", "Practice with fake letters. Open one and you learn; report one and you\'re thanked."),
         "small": ('경비실이 <a href="phishing-ko.html">도둑 흉내</a>를 내서 가짜 편지를 보내요. 달이 갈수록 여는 사람은 줄고 쪽지 보내는 사람은 늘어요 — 혼내지 않으니까요.',
                   'The guard room sends fake letters, <a href="phishing-en.html">pretending to be the thief</a>. Month by month fewer people open them and more send a note — because nobody gets scolded.')},
        {"svg": P5, "alt": ("요리사가 편지 도장을 보고 '이상한데… 경비실에 쪽지', 경비실 친구가 종을 울리고, 변장한 도둑이 문 앞에서 땀 흘리며 돌아감", "The cook looks at a seal and says this looks off — a note to the guards; the blue hat rings the bell; the disguised thief sweats and turns away at the door"),
         "caption": ("이번엔 요리사가 종을 울렸어요.", "This time, the cook rang the bell."),
         "small": ('이상한 도장 하나에 <a href="soc-ko.html">경비실</a>로 쪽지 한 장. 이제 성 사람 모두가 파수꾼이에요 — 경비 10명이 아니라 200명.',
                   'One odd seal, one note to the <a href="soc-en.html">guard room</a>. Now everyone in the castle is a lookout — not 10 guards, but 200.')},
    ],
    "summary": (("<b>보안 인식 교육</b> = 경비만이 아니라 <b>성 사람 모두</b>가 듣는 도둑 알아보기 수업. <b>짧게 자주</b>, <b>가짜 편지로 연습</b>, <b>혼내지 않기</b>, <b>이상하면 쪽지 한 장</b>.",
                 "<b>Security awareness training</b> = a thief-spotting class for <b>everyone in the castle</b>, not just the guards. <b>Short and often</b>, <b>practice with fake letters</b>, <b>no scolding</b>, and <b>feels off? one note</b>."),
                ("Security Awareness Training. 모든 구성원이 피싱·사회공학·비밀번호 같은 위협을 알아보고 신고하도록 반복 교육하고, 모의 피싱으로 연습해요. 목표는 클릭률을 낮추고 신고율을 높이는 것.",
                 "Recurring training so every employee can recognize and report phishing, social engineering, and credential threats, practiced with simulated phishing. The goal: lower click rates, higher report rates.")),
    "glossary": [
        ("사회공학", "Social engineering", ("벽 대신 사람 넘기.", "Getting past people, not walls."), ('편지, 전화, 변장. 자물쇠보다 사람이 싸요. → <a href="phishing-ko.html">우체국인 척하는 편지</a>', 'Letters, calls, disguises. A person is cheaper to fool than a lock. → <a href="phishing-en.html">the letter from the fake post office</a>')),
        ("피싱 모의훈련", "Phishing simulation", ("경비실이 보낸 가짜 편지.", "The guard room\'s fake letter."), ("도둑이 보내기 전에 우리가 먼저 보내 봐요. 열면 그 자리에서 짧은 수업.", "We send it before the thief does. Open it, and you get a short lesson on the spot.")),
        ("클릭률", "Click rate", ("편지를 연 사람 수.", "How many opened it."), ("빨간 막대. 달마다 줄어야 해요.", "The red bar. It should fall month by month.")),
        ("신고율", "Report rate", ("쪽지 보낸 사람 수.", "How many sent a note."), ("초록 막대. 클릭률보다 더 중요해요 — 한 명만 신고해도 종이 울리니까요.", "The green bar. Matters more than the click rate — one report is enough to ring the bell.")),
        ("신고 버튼", "Report button", ("쪽지 한 장.", "One note."), ('편지 옆에 붙은 버튼 하나. 누르면 <a href="soc-ko.html">경비실</a>로 가요.', 'One button next to the letter. Press it, and it goes to the <a href="soc-en.html">guard room</a>.')),
        ("보안 문화", "Security culture", ("혼내지 않는 성.", "A castle that doesn\'t scold."), ("걸린 사람을 혼내면 다음엔 숨겨요. 말해 준 사람을 칭찬하면 다음엔 더 빨리 말해요.", "Scold the fooled and they hide it next time. Thank the ones who speak up and they speak faster.")),
        ("인적 방화벽", "Human firewall", ("사람으로 된 성벽.", "A wall made of people."), ('200명이 다 파수꾼이면 문이 200개 잠긴 거예요. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'When 200 people are lookouts, 200 doors are locked. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("온보딩 교육", "Onboarding training", ("첫날 수업.", "Day-one class."), ("새로 온 하녀가 첫날 듣는 도둑 수업. 열쇠 받기 전에요.", "The thief-spotting class a new maid gets on day one — before she gets a key.")),
    ],
}
