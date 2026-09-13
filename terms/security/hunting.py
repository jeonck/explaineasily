from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def lantern(x, y, s=1.0, glow=True):
    g = f'<circle r="70" fill="#F5E6B8" opacity="0.18"/><circle r="40" fill="#F5E6B8" opacity="0.22"/>' if glow else ""
    return (f'<g transform="translate({x},{y}) scale({s})">{g}<path d="M-8 -30 h16 M0 -30 v-10" stroke="#5A3B22" stroke-width="3"/>'
            f'<rect x="-12" y="-28" width="24" height="30" rx="3" fill="#F5E6B8" stroke="#5A3B22" stroke-width="3"/><rect x="-6" y="-18" width="12" height="10" fill="#E9B44C"/></g>')


def closet(x, y, s=1.0, open_door=False, inner=""):
    door = (f'<path d="M-28 -60 h40 l-30 18 v90 l-10 -12z" fill="#5A3B22"/>' if open_door else f'<rect x="-28" y="-60" width="56" height="120" rx="3" fill="#5A3B22"/><circle cx="18" cy="0" r="3" fill="#E9B44C"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="-64" width="64" height="128" rx="4" fill="{WOOD}"/>{inner}{door}</g>'


def diary(x, y, s=1.0, rows=(), hl=-1):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="260" height="{40 + 24 * len(rows)}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="260" height="24" rx="6" fill="#C9A86A"/>' + label(130, 17, "⟦일지|DIARY⟧", 11, "#142033", cls="d")
    for i, r in enumerate(rows):
        yy = 46 + i * 24
        if i == hl:
            out += f'<rect x="6" y="{yy - 15}" width="248" height="22" rx="4" fill="var(--accent-soft)"/>'
        out += label(14, yy, r, 11, "var(--bad)" if i == hl else "#142033", "start")
    return out + "</g>"


# 1. 조용한 밤, 종은 안 울려요 — 그런데 벽장 속에
P1 = svg(300, night(300)
         + f'<rect x="40" y="90" width="200" height="130" rx="6" fill="#1B2A44"/>' + bell(140, 70, 0.7, ring=False) + label(140, 130, "⟦경비실|guard room⟧", 12, "#C9D5E6")
         + person(120, 150, s=0.7, face=SMILE, **GUARD) + bubble(150, 150, 110, 30, "⟦조용하네|all quiet⟧", 12, "var(--panel)", "var(--line)", "left")
         + closet(600, 160, 0.9, open_door=False) + '<rect x="586" y="106" width="14" height="108" fill="#0A1120"/>'
         + '<g transform="translate(593,140)"><circle cx="-4" r="3" fill="#F5E6B8"/><circle cx="4" r="3" fill="#F5E6B8"/></g>'
         + label(600, 262, "⟦벽장 속에서 눈 두 개가|two eyes inside the closet⟧", 12, "#C9D5E6")
         + label(380, 288, "⟦종이 안 울려도 도둑은 이미 안에 있을 수 있어요|the bell can be silent while a thief is already inside⟧", 12, "#C9D5E6"))

# 2. 종은 아는 도둑만 울려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="60" y="50" width="150" height="190" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(135, 78, "⟦수배 전단|WANTED⟧", 13, "#142033", cls="d")
         + "".join(f'<g transform="translate({x},{y}) scale(0.5)"><circle cx="30" cy="30" r="22" fill="{SKIN}" stroke="#5A3B22" stroke-width="3"/>{MASK}<path d="M8 22 h44 v-6 h-44z" fill="var(--bad)"/></g>' for x, y in ((80, 100), (135, 100), (80, 160), (135, 160)))
         + bell(320, 130, 0.9, ring=True) + label(320, 200, "⟦아는 얼굴이면 울려요|rings for known faces⟧", 12, "var(--ink)")
         + person(560, 90, s=0.85, face=EYES, hat=None, shirt="#4A5A72", extra='<rect x="50" y="70" width="30" height="26" rx="4" fill="var(--night)"/>') + label(590, 200, "⟦처음 보는 도둑|a thief no one has seen⟧", 12, "var(--bad)")
         + bell(680, 60, 0.5, ring=False) + label(680, 115, "⟦…|…⟧", 16, "var(--muted)")
         + label(380, 280, "⟦새 도둑, 발소리 없는 도둑은 종을 안 울려요|new thieves and quiet thieves never ring the bell⟧", 13, "var(--muted)"))

# 3. 위협 헌팅 = 종을 기다리지 않고 찾아 나서요 (hero)
P3 = svg(340, night(340)
         + '<rect y="240" width="760" height="100" fill="#0A1120"/>'
         + "".join(closet(x, 170, 0.7) for x in (100, 230, 660))
         + closet(530, 170, 0.7, open_door=True, inner=f'<g transform="translate(-30,-40) scale(0.55)"><circle cx="30" cy="30" r="22" fill="{SKIN}"/>{MASK}<rect x="12" y="52" width="36" height="50" rx="8" fill="#2E3D57"/></g>')
         + lantern(400, 150, 1.0) + person(340, 130, s=0.9, face=EYES, **GUARD)
         + bubble(330, 40, 180, 34, "⟦도둑이라면 어디 숨을까?|if I were a thief, where would I hide?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(530, 262, "⟦찾았다|found one⟧", 13, "#F5E6B8", cls="d")
         + label(380, 318, "⟦종이 안 울려도 랜턴 들고 구석구석 살펴요|even with no bell, walk every corner with a lantern⟧", 13, "#C9D5E6"))

# 4. 질문 하나 → 일지 뒤지기 → 이상한 한 줄
P4 = svg(320, sky(320)
         + bubble(30, 30, 230, 60, "⟦도둑이라면 밤에 창고 문을 열겠지?|a thief would open the storeroom at night, right?⟧", 12, "var(--panel)", "var(--line)", "right")
         + person(60, 120, s=0.8, face=EYES, **GUARD) + lantern(130, 190, 0.6, glow=False)
         + '<path d="M250 160 L300 160" stroke="var(--accent)" stroke-width="3"/><path d="M290 150 L302 160 L290 170" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + diary(320, 40, 1.0, rows=("⟦낮 2시 · 창고 문 열림 · 요리사|2 pm · storeroom opened · cook⟧", "⟦낮 5시 · 창고 문 열림 · 요리사|5 pm · storeroom opened · cook⟧", "⟦밤 3시 · 창고 문 열림 · 요리사?|3 am · storeroom opened · cook?⟧", "⟦밤 3시 · 창고 문 열림 · 요리사?|3 am · storeroom opened · cook?⟧", "⟦낮 9시 · 창고 문 열림 · 요리사|9 am · storeroom opened · cook⟧"), hl=2)
         + '<rect x="326" y="115" width="248" height="46" rx="4" fill="none" stroke="var(--bad)" stroke-width="3"/>'
         + label(450, 230, "⟦요리사는 밤 3시에 자고 있는데?|but the cook is asleep at 3 am⟧", 13, "var(--bad)")
         + label(380, 300, "⟦수천 줄 속에서 '이상한 한 줄'을 찾아요|find the one odd line among thousands⟧", 13, "var(--muted)"))

# 5. 찾은 버릇은 새 종이 돼요
P5 = svg(320, sky(320)
         + diary(40, 60, 0.85, rows=("⟦밤 3시 · 창고 문 열림 · 요리사?|3 am · storeroom opened · cook?⟧",), hl=0)
         + '<path d="M280 100 L340 100" stroke="var(--good)" stroke-width="3"/><path d="M330 90 L342 100 L330 110" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + '<rect x="360" y="40" width="200" height="120" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(460, 68, "⟦새 종 규칙|NEW BELL RULE⟧", 12, "#142033", cls="d")
         + label(460, 100, "⟦밤에 창고 문이 열리면|storeroom opens at night⟧", 12, "#142033") + label(460, 122, "⟦→ 종 울리기|→ ring the bell⟧", 12, "#142033")
         + bell(660, 70, 0.9, ring=True) + label(660, 140, "⟦다음엔 울려요|next time it rings⟧", 12, "var(--ink)", cls="d")
         + person(120, 220, s=0.7, face=SMILE, **GUARD) + lantern(190, 280, 0.5, glow=False)
         + "".join(person(x, 185, s=0.7, face=SMILE, hat=h, shirt="#4A5A72") for x, h in ((520, "#E9B44C"), (600, "#5B8DEF")))
         + label(560, 305, "⟦경비실 친구들이 이어받아요|the guard room takes it from here⟧", 12, "var(--muted)")
         + label(300, 250, "⟦헌터는 다음 질문으로|the hunter moves on to the next question⟧", 12, "var(--muted)"))

ASSUME_I = icon(f'<rect x="10" y="14" width="44" height="40" rx="4" fill="{WOOD}"/><rect x="12" y="16" width="20" height="36" fill="#5A3B22"/><circle cx="40" cy="30" r="3" fill="#F5E6B8"/><circle cx="48" cy="30" r="3" fill="#F5E6B8"/>')
QUESTION_I = icon('<path d="M20 24 a12 12 0 1 1 18 10 q-6 4 -6 10" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="32" cy="54" r="3.5" fill="var(--accent)"/>')
DIARY_I = icon('<rect x="14" y="10" width="36" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 32 h20 M22 40 h12" stroke="#142033" stroke-width="3" stroke-linecap="round"/><circle cx="44" cy="44" r="7" fill="none" stroke="var(--bad)" stroke-width="3"/>')
BELL_I = icon('<path d="M18 40 c0 -24 28 -24 28 0 v8 h-28z" fill="#E9B44C"/><rect x="14" y="48" width="36" height="5" rx="2" fill="#C9822B"/><path d="M12 22 a20 20 0 0 1 6 -12 M52 22 a20 20 0 0 0 -6 -12" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "hunting", "order": 51,
    "title": ("종을 기다리지 않는 파수꾼", "The Guard Who Doesn't Wait for the Bell"),
    "h1": ("<em>위협 헌팅</em>이 뭐예요?", "What is <em>Threat Hunting</em>?"),
    "sub": ("위협 헌팅(Threat Hunting)을 종이 울리기 전에 랜턴 들고 찾아 나서는 파수꾼 이야기로 풀어봤어요.",
            "Threat hunting, told as a story about the guard who goes looking with a lantern before the bell ever rings."),
    "panels": [
        {"svg": P1, "alt": ("조용한 밤, 경비실의 종은 잠잠하고 경비는 '조용하네'라고 말함. 오른쪽 벽장 틈으로 눈 두 개가 보임", "A quiet night: the guard room bell is silent and the guard says all quiet; two eyes peek from a closet on the right"),
         "caption": ("종이 안 울려요. 그런데 벽장 속에 누가 있어요.", "The bell is silent. But someone is in the closet."),
         "small": ("조용하다고 아무도 없는 건 아니에요. 도둑은 몇 달씩 숨어 있기도 해요.", "Quiet doesn't mean empty. A thief can hide for months.")},
        {"svg": P2, "alt": ("수배 전단의 네 얼굴, 아는 얼굴이면 울리는 종, 그리고 처음 보는 도둑 옆의 조용한 종", "A wanted poster with four faces, a bell that rings for known faces, and a silent bell beside a thief no one has seen"),
         "caption": ("종은 아는 도둑만 울려요.", "The bell only rings for thieves it knows."),
         "small": ('<a href="idsips-ko.html">수배 전단</a>에 없는 새 도둑, 발소리 없이 걷는 도둑은 종을 안 울려요.',
                   'A new thief who isn\'t on the <a href="idsips-en.html">wanted poster</a>, or one who walks without a sound, never rings the bell.')},
        {"svg": P3, "hero": True, "alt": ("밤의 복도, 랜턴을 든 경비가 '도둑이라면 어디 숨을까?' 하며 벽장을 열자 도둑이 나옴", "A night hallway: a guard with a lantern asks where a thief would hide, opens a closet, and finds one"),
         "caption": ("위협 헌팅은 종을 기다리지 않고 직접 찾아 나서는 거예요.", "Threat hunting is going to look instead of waiting for the bell."),
         "small": ("'이미 도둑이 들어와 있다'고 치고, 도둑이라면 어디 숨을지 생각하며 랜턴으로 구석구석 비춰요.", "Assume a thief is already inside, think about where one would hide, and shine the lantern into every corner."),
         "tricks": (4, [
             (ASSUME_I, ("이미 들어왔다 치기", "Assume they\'re in"), ("조용해도 믿지 않아요", "quiet isn\'t proof"), "warm"),
             (QUESTION_I, ("질문 하나", "One question"), ("도둑이라면 어디 숨을까?", "where would a thief hide?")),
             (DIARY_I, ("일지 뒤지기", "Dig the diary"), ("이상한 한 줄 찾기", "find the odd line")),
             (BELL_I, ("새 종 달기", "Hang a new bell"), ("다음엔 울리게", "so it rings next time"), "calm"),
         ])},
        {"svg": P4, "alt": ("경비가 '도둑이라면 밤에 창고 문을 열겠지?' 하고 일지를 봄. 창고 문 열림 기록 중 '밤 3시 · 요리사?' 두 줄에 빨간 표시", "The guard asks whether a thief would open the storeroom at night and reads the diary; two lines — 3 am, cook? — are circled in red"),
         "caption": ("질문 하나를 들고 일지를 뒤져요.", "Take one question and dig through the diary."),
         "small": ('<a href="log-ko.html">일지</a> 수천 줄 속에서 이상한 한 줄을 찾아요. "요리사가 밤 3시에 창고 문을?" — 요리사는 자고 있는데요.',
                   'Among thousands of <a href="log-en.html">diary</a> lines, find the odd one. "The cook opened the storeroom at 3 am?" — the cook was asleep.')},
        {"svg": P5, "alt": ("찾은 이상한 줄이 화살표를 따라 '새 종 규칙: 밤에 창고 문이 열리면 종 울리기'가 되고, 종이 울림. 경비실 친구들이 이어받고 헌터는 다음 질문으로", "The odd line becomes a new bell rule — storeroom opens at night, ring the bell — and the bell rings; the guard room takes over while the hunter moves on"),
         "caption": ("찾은 버릇은 새 종이 돼요.", "What you find becomes a new bell."),
         "small": ('한 번 손으로 찾은 <a href="ttp-ko.html">도둑의 버릇</a>은 <a href="siem-ko.html">경비실 화면</a>에 규칙으로 달아요. 다음엔 종이 알아서 울려요.',
                   'A <a href="ttp-en.html">thief\'s habit</a> found by hand becomes a rule on the <a href="siem-en.html">guard room screen</a>. Next time the bell rings on its own.')},
    ],
    "summary": (("<b>위협 헌팅</b> = 종이 안 울려도 <b>이미 들어왔다 치고</b>, 질문 하나 들고 <b>일지를 뒤져</b> 숨은 도둑을 찾고 <b>새 종을 다는</b> 일.",
                 "<b>Threat hunting</b> = even with no bell, <b>assume they\'re in</b>, take one question, <b>dig the diary</b> for the hidden thief, and <b>hang a new bell</b>."),
                ("Threat Hunting. 경보(alert)를 기다리는 대신 가설을 세우고 로그를 뒤져 탐지되지 않은 침입을 찾는 능동적 활동이에요. 찾아낸 건 탐지 규칙이 돼요.",
                 "Instead of waiting for alerts, hunters form a hypothesis and search logs for intrusions nothing detected. What they find becomes a detection rule.")),
    "glossary": [
        ("가정 침해", "Assume breach", ("이미 들어왔다 치기.", "Assume they\'re already in."), ("조용한 건 증거가 아니에요. 헌팅의 출발점.", "Quiet is not proof. Where every hunt starts.")),
        ("가설", "Hypothesis", ("질문 하나.", "One question."), ('"도둑이라면 밤에 창고 문을 열겠지?" → <a href="ttp-ko.html">도둑의 버릇</a>', '"A thief would open the storeroom at night, right?" → <a href="ttp-en.html">a thief\'s habits</a>')),
        ("경보", "Alert", ("종.", "The bell."), ('아는 도둑만 울려요. → <a href="idsips-ko.html">수배 전단 든 파수꾼</a>', 'Rings only for known thieves. → <a href="idsips-en.html">the guard with the wanted poster</a>')),
        ("로그", "Logs", ("일지.", "The diary."), ('헌터가 뒤지는 곳. → <a href="log-ko.html">성 곳곳의 한 줄 일지</a>', 'Where the hunter digs. → <a href="log-en.html">the one-line diary</a>')),
        ("체류 시간", "Dwell time", ("숨어 있던 날 수.", "Days spent hiding."), ("종이 안 울린 채 도둑이 안에 있던 기간. 헌팅은 이걸 줄여요.", "How long a thief was inside with no bell. Hunting shortens it.")),
        ("탐지 규칙", "Detection rule", ("새 종.", "A new bell."), ('찾은 버릇을 <a href="siem-ko.html">경비실 화면</a>에 달아요.', 'A found habit, hung on the <a href="siem-en.html">guard room screen</a>.')),
        ("위협 정보", "Threat intel", ("망루 친구의 소식.", "Word from the watchtower."), ('"요즘 도둑들은 창고를 노린대" → 좋은 질문이 돼요. → <a href="cti-ko.html">망루 위의 친구</a>', '"Thieves are after storerooms these days" → a good question. → <a href="cti-en.html">the friend on the watchtower</a>')),
        ("헌터", "Threat hunter", ("랜턴 든 파수꾼.", "The guard with the lantern."), ('종을 기다리는 <a href="soc-ko.html">경비실</a>과 짝이에요. 하나는 기다리고, 하나는 찾아 나서요.', 'Partner to the <a href="soc-en.html">guard room</a> that waits for the bell. One waits, one goes looking.')),
    ],
}
