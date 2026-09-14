from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)   # 고용한 도둑 (pentest 와 같은 차림)
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def crown(x, y, s=1.0, tag=False):
    t = f'<rect x="14" y="-6" width="26" height="14" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2" transform="rotate(20 14 -6)"/>' if tag else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 10 l-4 -30 l14 12 l16 -22 l16 22 l14 -12 l-4 30z" fill="#E9B44C" stroke="#C9822B" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="-28" y="8" width="56" height="10" rx="3" fill="#C9822B"/><circle cx="-16" cy="-4" r="3" fill="var(--bad)"/><circle cy="-10" r="3" fill="#5B8DEF"/><circle cx="16" cy="-4" r="3" fill="var(--bad)"/>{t}</g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


# 1. 지난번 고용한 도둑은 틈 목록을 줬어요. 그런데 왕이 물어요.
P1 = svg(300, sky(300)
         + person(70, 110, s=0.85, **HIRED) + paper(160, 50, 190, 150, "⟦틈 목록|LIST OF CRACKS⟧", ("⟦서쪽 창문 — 안 잠김|west window — unlocked⟧", "⟦뒷문 — 낡은 자물쇠|back door — old lock⟧", "⟦창고 — 열쇠 그대로|storeroom — key left in⟧", "⟦…|…⟧"))
         + label(250, 240, "⟦지난번엔 틈을 찾아 줬어요|last time, he found the cracks⟧", 12, "var(--muted)")
         + person(600, 100, s=0.9, face=EYES, **KING) + bubble(430, 30, 290, 46, "⟦틈은 다 막았는데… 진짜 도둑이 오면|the cracks are fixed… but if a real thief came,⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(575, 240, "⟦경비실이 눈치챌까?|would the guard room even notice?⟧", 13, "var(--ink)", cls="d"))

# 2. 목록으론 몰라요 — 도둑은 틈으로만 오지 않아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<g transform="translate(60,60)"><rect width="110" height="130" rx="3" fill="#8B5E3C"/><rect x="10" y="10" width="90" height="110" rx="2" fill="#5A3B22"/><path d="M20 20 l70 90 M90 20 l-70 90" stroke="var(--good)" stroke-width="6" stroke-linecap="round"/></g>' + label(115, 225, "⟦틈은 막았어요|cracks fixed⟧", 12, "var(--good)")
         + '<g transform="translate(250,80)"><rect width="90" height="60" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M0 0 l45 30 l45 -30" stroke="#C9A86A" stroke-width="3" fill="none"/></g>' + label(295, 225, "⟦가짜 편지|a fake letter⟧", 12, "var(--bad)")
         + person(420, 90, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=MASK) + label(450, 225, "⟦목수로 변장|dressed as the carpenter⟧", 12, "var(--bad)")
         + '<g transform="translate(600,80)"><circle r="34" fill="var(--panel)" stroke="var(--line)" stroke-width="4"/><path d="M0 -20 v20 l14 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>' + label(600, 225, "⟦몇 주를 기다려요|waits for weeks⟧", 12, "var(--bad)")
         + label(380, 280, "⟦진짜 도둑은 틈으로만 오지 않아요 — 경비실은 진짜 도둑을 만나본 적이 없어요|real thieves don\'t only come through cracks — and the guard room has never met one⟧", 11, "var(--muted)"))

# 3. 레드 팀 = 진짜 도둑인 척하는 팀 (hero)
P3 = svg(360, night(360)
         + paper(40, 50, 210, 130, "⟦임무|THE MISSION⟧", ("⟦왕관을 가져와 봐|bring me the crown⟧", "⟦방법은 뭐든|any way you like⟧", "⟦부수지는 말 것|but break nothing⟧"), 1.0) + label(145, 205, "⟦왕이 몰래 준 쪽지|a note the king gave in secret⟧", 11, "#C9D5E6")
         + person(300, 130, s=0.95, **HIRED) + person(390, 150, s=0.75, hat="#E9B44C", shirt="#4A5A72", face=MASK) + person(460, 160, s=0.65, hat=None, shirt="#2E3D57", face=MASK)
         + label(390, 262, "⟦레드 팀 — 셋이 한 팀|the red team — three as one⟧", 13, "#F5E6B8", cls="d")
         + f'<rect x="560" y="70" width="160" height="110" rx="6" fill="#1B2A44"/>' + bell(600, 90, 0.5, ring=False) + person(660, 100, s=0.55, face=SMILE, **BLUE) + label(640, 174, "⟦경비실은 몰라요|the guard room doesn\'t know⟧", 11, "#C9D5E6")
         + label(380, 300, "⟦목표는 하나, 방법은 뭐든, 몰래, 오래|one goal, any method, quietly, for as long as it takes⟧", 13, "#F5E6B8", cls="d")
         + label(380, 336, "⟦틈을 세는 게 아니라 진짜 도둑처럼 끝까지 가 봐요|not counting cracks — going all the way, like a real thief⟧", 12, "#C9D5E6"))

# 4. 몇 주 뒤: 왕관은 나갔고, 종은 한 번 울렸다 꺼졌어요
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(120, 100, s=0.95, **HIRED) + crown(200, 120, 0.9, tag=True) + label(190, 240, "⟦3주 뒤, 왕관을 들고 나왔어요|three weeks later, out with the crown⟧", 12, "var(--ink)")
         + label(190, 264, "⟦(진짜는 아니고 표시 붙인 가짜)|(a tagged copy, not the real one)⟧", 11, "var(--muted)")
         + person(500, 110, s=0.85, face=FROWN + SWEAT, **BLUE) + bell(620, 118, 0.8, ring=True)
         + bubble(560, 30, 170, 34, "⟦고양이겠지, 하고 껐어요|thought it was a cat, turned it off⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + label(570, 240, "⟦종은 딱 한 번 울렸어요|the bell rang exactly once⟧", 12, "var(--ink)")
         + label(570, 264, "⟦둘째 주 화요일 밤에|on the second Tuesday, at night⟧", 11, "var(--muted)")
         + label(380, 302, "⟦틈 목록은 없어요 — 대신 '언제 놓쳤는지'가 있어요|no list of cracks — instead, the moment they missed⟧", 12, "var(--ink)", cls="d"))

# 5. 끝나면 셋이 모여 지도를 펴요
P5 = svg(320, sky(320)
         + '<g transform="translate(200,30)"><rect width="360" height="200" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="360" height="28" rx="8" fill="#C9A86A"/>' + label(180, 19, "⟦도둑이 지나간 길|THE THIEF\'S PATH⟧", 12, "#142033", cls="d")
         + '<path d="M30 160 L100 160 L100 100 L200 100 L200 60 L320 60" stroke="var(--bad)" stroke-width="4" fill="none" stroke-dasharray="8 6"/>'
         + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"/>' for x, y, c in ((30, 160, "var(--bad)"), (100, 100, "var(--bad)"), (200, 60, "var(--accent)"), (320, 60, "#E9B44C")))
         + label(30, 185, "⟦가짜 편지|fake letter⟧", 10, "#142033") + label(100, 88, "⟦목수 옷|carpenter\'s coat⟧", 10, "#142033") + label(200, 48, "⟦종! (꺼짐)|bell! (dismissed)⟧", 10, "var(--accent)") + label(320, 48, "⟦왕관|crown⟧", 10, "#142033") + "</g>"
         + person(60, 130, s=0.75, **HIRED) + person(130, 150, s=0.65, face=SMILE, **BLUE) + person(640, 130, s=0.75, face=SMILE, **KING)
         + label(380, 262, "⟦'여기서 종이 울렸는데 우리가 껐구나'|'the bell rang right here, and we turned it off'⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦경비실 순서표를 고치고, 다음엔 같은 책상에 앉아요|fix the guard room\'s book, and next time sit at the same table⟧", 12, "var(--muted)"))

GOAL_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="10" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="3" fill="var(--bad)"/>')
ANY_I = icon('<rect x="10" y="30" width="26" height="20" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M10 30 l13 9 l13 -9" stroke="#C9A86A" stroke-width="2" fill="none"/><path d="M40 14 h14 v8 h-14z" fill="#E9B44C"/><circle cx="47" cy="30" r="6" fill="#E8C9A8"/><rect x="41" y="36" width="12" height="14" rx="3" fill="#4A5A72"/>')
QUIET_I = icon('<circle cx="32" cy="32" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 18 v14 l9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="50" cy="14" r="5" fill="#F5E6B8"/>')
SECRET_I = icon('<rect x="12" y="20" width="40" height="30" rx="4" fill="#1B2A44"/><path d="M18 30 c0 -14 28 -14 28 0 v6 h-28z" fill="#E9B44C" opacity="0.5"/><path d="M12 20 l40 30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "redteam", "order": 53,
    "title": ("진짜 도둑인 척하는 팀", "The Team That Plays the Real Thief"),
    "h1": ("<em>레드 팀</em>이 뭐예요?", "What is a <em>Red Team</em>?"),
    "sub": ("레드 팀(Red Team)을 왕의 비밀 쪽지를 받고 진짜 도둑처럼 왕관을 노리는 팀 이야기로 풀어봤어요.",
            "Red teaming, told as a story about a team that takes a secret note from the king and goes after the crown like a real thief."),
    "panels": [
        {"svg": P1, "alt": ("고용한 도둑이 틈 목록(서쪽 창문, 뒷문, 창고)을 건네고, 왕이 '틈은 다 막았는데 진짜 도둑이 오면 경비실이 눈치챌까?' 하고 물음", "The hired thief hands over a list of cracks — west window, back door, storeroom — and the king asks: the cracks are fixed, but would the guard room notice a real thief?"),
         "caption": ("틈은 다 막았어요. 그런데 왕이 물어요.", "The cracks are fixed. But the king has a question."),
         "small": ('지난번 <a href="pentest-ko.html">고용한 도둑</a>은 틈 목록을 줬어요. "진짜 도둑이 오면, 우리 경비실이 눈치챌까?"',
                   'Last time the <a href="pentest-en.html">hired thief</a> gave us a list of cracks. "If a real thief came — would our guard room even notice?"')},
        {"svg": P2, "alt": ("막힌 문, 가짜 편지, 목수로 변장한 사람, 몇 주를 재는 시계", "A boarded door, a fake letter, someone dressed as the carpenter, and a clock counting weeks"),
         "caption": ("목록으로는 몰라요. 진짜 도둑은 틈으로만 오지 않거든요.", "A list can\'t answer that. Real thieves don\'t only come through cracks."),
         "small": ('<a href="phishing-ko.html">가짜 편지</a>를 보내고, 목수로 변장하고, 몇 주를 기다려요. 그리고 경비실은 진짜 도둑을 만나본 적이 없어요.',
                   'They send a <a href="phishing-en.html">fake letter</a>, dress as the carpenter, wait for weeks. And the guard room has never met a real thief.')},
        {"svg": P3, "hero": True, "alt": ("밤. 왕이 몰래 준 임무 쪽지 — 왕관을 가져와 봐, 방법은 뭐든, 부수지는 말 것. 도둑 차림 셋이 한 팀. 옆의 경비실은 종도 조용하고 아무것도 모름", "Night. A secret mission note from the king — bring me the crown, any way you like, but break nothing. Three in thief\'s clothes as one team. The guard room beside them knows nothing"),
         "caption": ("레드 팀은 진짜 도둑인 척하는 팀이에요.", "A red team is a team that plays the real thief."),
         "small": ("왕이 몰래 준 쪽지엔 목표 하나뿐이에요 — '왕관을 가져와 봐.' 방법은 뭐든, 몰래, 오래. 경비실은 몰라요.", "The king\'s secret note has just one goal — bring me the crown. Any method, quietly, for as long as it takes. The guard room doesn\'t know."),
         "tricks": (4, [
             (GOAL_I, ("목표 하나", "One goal"), ("틈 세기가 아니라 왕관", "the crown, not a crack count"), "warm"),
             (ANY_I, ("방법은 뭐든", "Any method"), ("편지, 변장, 밤", "letters, disguises, night")),
             (QUIET_I, ("몰래, 오래", "Quietly, for weeks"), ("진짜 도둑처럼", "just like a real one")),
             (SECRET_I, ("경비실은 몰라요", "Guards don\'t know"), ("그래야 진짜 시험이니까", "or it isn\'t a real test"), "calm"),
         ])},
        {"svg": P4, "alt": ("3주 뒤, 표시가 붙은 왕관을 들고 나온 도둑. 경비실 친구는 땀을 흘리며 '고양이겠지, 하고 껐어요' — 종은 둘째 주 화요일 밤 딱 한 번 울림", "Three weeks later the thief walks out with a tagged crown. The guard sweats: thought it was a cat, turned it off — the bell rang exactly once, on the second Tuesday night"),
         "caption": ("3주 뒤, 왕관이 나갔어요. 종은 딱 한 번 울렸고요.", "Three weeks later, the crown was gone. The bell rang exactly once."),
         "small": ('진짜 왕관은 아니고 표시 붙인 가짜예요. 종이 울렸을 때 <a href="soc-ko.html">경비실</a>은 "고양이겠지" 하고 껐어요. 그 순간이 바로 배울 점이에요.',
                   'Not the real crown — a tagged copy. When the bell rang, the <a href="soc-en.html">guard room</a> thought "probably a cat" and dismissed it. That moment is the lesson.')},
        {"svg": P5, "alt": ("도둑이 지나간 길 지도: 가짜 편지 → 목수 옷 → 종(꺼짐) → 왕관. 도둑, 경비실 친구, 왕이 함께 봄", "A map of the thief\'s path: fake letter → carpenter\'s coat → bell (dismissed) → crown. The thief, the guard, and the king look at it together"),
         "caption": ("끝나면 셋이 모여 지도를 펴요.", "Afterwards, all three open the map together."),
         "small": ('"여기서 종이 울렸는데 우리가 껐구나." <a href="incident-ko.html">경비실 순서표</a>를 고치고, 다음엔 <a href="purpleteam-ko.html">같은 책상</a>에 앉아요.',
                   '"The bell rang right here, and we turned it off." Fix the <a href="incident-en.html">guard room\'s book</a>, and next time sit at the <a href="purpleteam-en.html">same table</a>.')},
    ],
    "summary": (("<b>레드 팀</b> = 왕의 비밀 쪽지 하나 들고 <b>진짜 도둑처럼</b> 몰래, 오래, 어떤 방법으로든 <b>왕관을 노려</b>, 경비실이 <b>눈치채는지</b> 시험하는 팀.",
                 "<b>Red team</b> = with one secret note from the king, <b>go after the crown like a real thief</b> — quietly, for weeks, any way — to test whether the guard room <b>notices</b>."),
                ("Red Team. 취약점을 나열하는 펜테스트와 달리, 실제 공격자를 흉내 내 하나의 목표를 향해 은밀하게 움직이며 조직의 탐지·대응 능력을 시험해요.",
                 "Unlike a pentest that lists vulnerabilities, a red team emulates a real adversary — one objective, stealthy, over time — to test the organization\'s ability to detect and respond.")),
    "glossary": [
        ("레드 팀", "Red team", ("진짜 도둑인 척.", "Playing the real thief."), ("틈을 세는 게 아니라 왕관까지 가 봐요. 시험받는 건 성벽이 아니라 경비실이에요.", "Not counting cracks — going all the way to the crown. It\'s the guard room being tested, not the wall.")),
        ("펜테스트", "Pentest", ("틈 목록 만들기.", "Making a list of cracks."), ('짧고, 범위가 정해져 있고, 경비실도 알아요. → <a href="pentest-ko.html">우리가 고용한 도둑</a>', 'Short, scoped, and the guard room knows. → <a href="pentest-en.html">the thief we hired</a>')),
        ("목표", "Objective", ("왕관.", "The crown."), ("'제일 소중한 것'을 하나 정해요. 왕관, 금고, 명부.", "Pick the one thing that matters most: the crown, the vault, the roster.")),
        ("교전 규칙", "Rules of engagement", ("쪽지의 작은 글씨.", "The note\'s fine print."), ("부수지 않기, 진짜 왕관은 안 건드리기, 언제까지. 미리 정해요.", "Break nothing, never touch the real crown, a deadline. Agreed in advance.")),
        ("화이트 셀", "White cell", ("비밀을 아는 왕.", "The king who knows."), ("경비실은 모르지만 누군가는 알아야 해요. 위험하면 멈추게 하는 사람.", "The guard room doesn\'t know, but someone must. The one who calls a halt if it gets dangerous.")),
        ("블루 팀", "Blue team", ("시험받는 경비실.", "The guard room being tested."), ('종을 껐는지, 쫓아갔는지. → <a href="soc-ko.html">성의 경비실</a>', 'Did they dismiss the bell or chase it? → <a href="soc-en.html">the guard room</a>')),
        ("공격 에뮬레이션", "Adversary emulation", ("진짜 도둑의 버릇 따라 하기.", "Copying a real thief\'s habits."), ('요즘 도둑이 하는 순서 그대로. → <a href="ttp-ko.html">도둑의 버릇</a>', 'The way today\'s thieves actually do it. → <a href="ttp-en.html">a thief\'s habits</a>')),
        ("디브리프", "Debrief", ("셋이 모여 지도 펴기.", "Opening the map together."), ('놓친 순간을 같이 봐요. 그다음은 → <a href="purpleteam-ko.html">같은 책상에 앉은 도둑과 파수꾼</a>', 'Looking at the missed moment together. Then → <a href="purpleteam-en.html">the thief and the guard at one table</a>')),
    ],
}
