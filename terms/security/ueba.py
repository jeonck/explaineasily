from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
COOK = dict(hat="#FFF", shirt="#FFF")
MAID = dict(hat=None, shirt="#7B3FA0")
CARPENTER = dict(hat="#8B5E3C", shirt="#8B5E3C")
COOK_THIEF = dict(hat="#FFF", shirt="#FFF", face=MASK)   # 요리사 옷을 입은 도둑
KEY = '<g transform="translate(58,80) rotate(-30)"><circle r="7" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="5" y="-2" width="22" height="4" fill="#E9B44C"/><rect x="20" y="2" width="3" height="6" fill="#E9B44C"/></g>'


def vault(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="210" rx="6" fill="var(--stone-dark)"/>'
            f'<rect x="30" y="60" width="70" height="80" rx="5" fill="var(--night)"/><circle cx="65" cy="100" r="16" fill="none" stroke="var(--stone)" stroke-width="5"/></g>')


def clock(x, y, s=1.0, hour=3):
    import math
    a = math.radians(hour * 30 - 90)
    hx, hy = 16 * math.cos(a), 16 * math.sin(a)
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="30" fill="var(--panel)" stroke="var(--line)" stroke-width="4"/>'
            f'<path d="M0 0 L0 -24" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/><path d="M0 0 L{hx:.1f} {hy:.1f}" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/><circle r="3" fill="var(--ink)"/></g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def paper(x, y, w, h, title, rows, s=1.0, size=12, step=22):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * step, r, size, "#142033", "start")
    return out + "</g>"


def check(x, y, color="var(--good)"):
    return f'<circle cx="{x}" cy="{y}" r="14" fill="{color}"/><path d="M{x - 7} {y} l5 5 l9 -10" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>'


# 1. 밤 3시, 요리사 열쇠가 금고 방 앞에 — 열쇠도 맞고 얼굴도 맞아요
P1 = svg(320, night(320)
         + clock(110, 80, 1.0, 3) + label(110, 140, "⟦밤 3시|3 a.m.⟧", 16, "#F5E6B8", cls="d")
         + vault(300, 70) + label(365, 50, "⟦금고 방|the vault room⟧", 13, "#F5E6B8", cls="d")
         + person(200, 140, s=0.9, face=EYES, extra=KEY, **COOK) + label(212, 262, "⟦요리사 (열쇠 ✓ 얼굴 ✓)|the cook (key ✓ face ✓)⟧", 11, "#C9D5E6")
         + person(470, 140, s=0.9, face=SMILE, **GUARD)
         + bubble(440, 60, 250, 36, "⟦열쇠 맞고, 얼굴 맞고 — 들어가세요|key\'s right, face\'s right — go on in⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 302, "⟦그런데… 요리사가 밤 3시에 금고 방을?|but… the cook, at the vault, at 3 a.m.?⟧", 13, "#F5E6B8", cls="d"))

# 2. 문지기는 열쇠와 얼굴만 봐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + paper(50, 40, 230, 150, "⟦문지기의 확인|THE DOORKEEPER\'S CHECK⟧", ("⟦열쇠가 맞나? ✓|key matches? ✓⟧", "⟦얼굴이 맞나? ✓|face matches? ✓⟧", "⟦…끝이에요|…and that\'s all⟧"))
         + "".join(label(380, y, t, 13, "var(--muted)") for y, t in ((85, "⟦언제?|when?⟧"), (125, "⟦어디를?|which room?⟧"), (165, "⟦얼마나 자주?|how often?⟧")))
         + label(380, 205, "⟦안 물어봐요|never asked⟧", 11, "var(--bad)")
         + bell(460, 215, 0.6, ring=False) + label(460, 262, "⟦종은 조용해요|the bell stays quiet⟧", 11, "var(--muted)")
         + person(560, 90, s=0.9, extra=KEY, **COOK_THIEF) + label(590, 225, "⟦훔친 열쇠, 빌린 옷|a stolen key, a borrowed coat⟧", 11, "var(--bad)")
         + label(380, 288, "⟦열쇠와 얼굴이 맞으면 문지기는 그냥 열어 줘요|if the key and face match, the doorkeeper just opens up⟧", 12, "var(--ink)", cls="d"))

# 3. 경비실은 사람마다 '평소'를 기억해요 (hero)
P3 = svg(360, sky(360)
         + paper(40, 30, 440, 200, "⟦경비실의 평소 장부|THE GUARD ROOM\'S BOOK OF USUAL⟧", ("⟦요리사 — 새벽 5시 · 부엌|the cook — 5 a.m. · the kitchen⟧", "⟦하녀 — 낮 · 2층|the maid — daytime · 2nd floor⟧", "⟦목수 — 오후 · 창고|the carpenter — afternoon · storeroom⟧", "⟦왕 — 아무 때나 · 어디나|the king — any time · anywhere⟧"), size=13, step=30)
         + person(540, 50, s=0.8, face=SMILE, **BLUE) + '<path d="M596 118 l16 -20" stroke="#142033" stroke-width="4" stroke-linecap="round"/>'
         + label(590, 180, "⟦매일 적고, 기억해요|writes it down every day⟧", 11, "var(--muted)")
         + person(520, 200, s=0.55, face=SMILE, **COOK) + person(590, 200, s=0.55, face=SMILE, **MAID) + person(660, 200, s=0.55, face=SMILE, **CARPENTER)
         + label(380, 300, "⟦사람마다 평소가 달라요 — 경비실은 그걸 다 기억해요|everyone\'s usual is different — the guard room remembers all of it⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦평소와 다르면 점수가 올라요|anything unlike the usual raises a score⟧", 12, "var(--muted)"))

# 4. 요리사 열쇠가 밤 3시에 금고 방을 열면 — 점수가 오르고 종이 울려요
P4 = svg(340, night(340)
         + vault(160, 70, 0.95) + person(70, 130, s=0.85, extra=KEY, **COOK_THIEF) + label(150, 300, "⟦열쇠 ✓ 얼굴 ✓ 그런데…|key ✓ face ✓ and yet…⟧", 11, "#C9D5E6")
         + paper(310, 40, 230, 175, "⟦위험 점수|RISK SCORE⟧", ("⟦밤 3시 (평소 새벽 5시) +3|3 a.m. (usually 5 a.m.) +3⟧", "⟦금고 방 (평소 부엌) +4|the vault (usually kitchen) +4⟧", "⟦한 시간에 다섯 번 +2|five tries in one hour +2⟧", "⟦합계 9 — 종!|total 9 — ring the bell!⟧"), size=11, step=26)
         + bell(600, 135, 0.9, ring=True) + person(590, 195, s=0.7, face=FROWN, **BLUE)
         + label(620, 300, "⟦점수가 높으면 종이 울려요|a high score rings the bell⟧", 12, "#F5E6B8")
         + label(380, 328, "⟦열쇠는 맞았지만, 걸음걸이가 달랐어요|the key was right — the walk was wrong⟧", 13, "#F5E6B8", cls="d"))

# 5. 무엇을 잡나, 언제 틀리나
P5 = svg(320, sky(320)
         + check(130, 40) + person(100, 80, s=0.9, extra=KEY, **COOK_THIEF) + label(130, 215, "⟦훔친 열쇠|a stolen key⟧", 13, "var(--ink)", cls="d") + label(130, 236, "⟦남의 평소를 못 따라 해요|can\'t copy someone else\'s usual⟧", 11, "var(--muted)")
         + check(380, 40) + person(350, 80, s=0.9, face=EYES, extra='<rect x="50" y="66" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>', **COOK) + label(380, 215, "⟦이상해진 진짜 요리사|the real cook, acting strange⟧", 13, "var(--ink)", cls="d") + label(380, 236, "⟦밤마다 종이를 들고 나가요|carries papers out every night⟧", 11, "var(--muted)")
         + label(630, 46, "?", 30, "var(--accent)", cls="d") + person(600, 80, s=0.9, face=SMILE, **MAID) + label(630, 215, "⟦새로 온 하녀|the new maid⟧", 13, "var(--ink)", cls="d") + label(630, 236, "⟦아직 평소가 없어요 — 종이 잘못 울려요|no usual yet — the bell rings by mistake⟧", 11, "var(--muted)")
         + label(380, 300, "⟦처음 몇 주는 평소를 배우는 시간이에요|the first few weeks are for learning the usual⟧", 13, "var(--ink)", cls="d"))

BOOK_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="14" y="8" width="36" height="10" rx="4" fill="#C9A86A"/><path d="M20 28 h24 M20 38 h24 M20 48 h16" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
DIFF_I = icon('<g transform="translate(20,34)"><ellipse rx="7" ry="11" fill="#7A5236"/><ellipse cy="-16" rx="5" ry="4" fill="#7A5236"/></g><g transform="translate(44,34) rotate(25)"><ellipse rx="7" ry="11" fill="var(--bad)"/><ellipse cy="-16" rx="5" ry="4" fill="var(--bad)"/></g>')
SCORE_I = icon('<rect x="12" y="40" width="10" height="14" fill="var(--good)"/><rect x="27" y="30" width="10" height="24" fill="var(--accent)"/><rect x="42" y="14" width="10" height="40" fill="var(--bad)"/><path d="M8 56 h48" stroke="var(--ink)" stroke-width="2"/>')
BELL_I = icon('<path d="M20 38 c0 -22 24 -22 24 0 v8 h-24z" fill="#E9B44C"/><rect x="16" y="46" width="32" height="5" rx="2" fill="#C9822B"/><circle cx="32" cy="55" r="3" fill="#C9822B"/><path d="M12 30 a22 22 0 0 1 6 -16 M52 30 a22 22 0 0 0 -6 -16" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "ueba", "order": 87,
    "title": ("평소와 다른 걸음걸이", "A Walk Unlike the Usual"),
    "h1": ("<em>UEBA</em>가 뭐예요?", "What is <em>UEBA</em>?"),
    "sub": ("사용자·개체 행동 분석(User and Entity Behavior Analytics)을 사람마다 '평소'를 기억하는 경비실 이야기로 풀어봤어요.",
            "User and Entity Behavior Analytics, told as a story about a guard room that remembers what is usual for every person."),
    "panels": [
        {"svg": P1, "alt": ("밤 3시. 요리사 옷을 입은 사람이 열쇠를 들고 금고 방 앞에 서 있고, 문지기가 웃으며 '열쇠 맞고, 얼굴 맞고 — 들어가세요' 함", "3 a.m. Someone in the cook\'s coat stands at the vault room with a key; the doorkeeper smiles: key\'s right, face\'s right — go on in"),
         "caption": ("열쇠도 맞고 얼굴도 맞아요. 그런데 뭔가 이상해요.", "The key is right and the face is right. And yet something feels wrong."),
         "small": ('<a href="mfa-ko.html">세 번 확인하는 문지기</a>도 물어보는 건 "너 맞아?"뿐이에요. 요리사가 밤 3시에 금고 방을 여는 건 이상하지만, 규칙엔 없어요.',
                   'Even the <a href="mfa-en.html">doorkeeper who checks three times</a> only asks "is it really you?" The cook opening the vault at 3 a.m. is odd — but it breaks no rule.')},
        {"svg": P2, "alt": ("문지기의 확인표엔 '열쇠 ✓ 얼굴 ✓ …끝'. 옆에 '언제? 어디를? 얼마나 자주?'는 안 물어봄. 종은 조용하고, 요리사 옷을 입은 도둑이 훔친 열쇠를 들고 있음", "The doorkeeper\'s checklist reads key ✓ face ✓ …that\'s all. Beside it, 'when? which room? how often?' are never asked. The bell stays quiet, and a thief in the cook\'s coat holds a stolen key"),
         "caption": ("문지기는 열쇠와 얼굴만 봐요. 언제, 어디를, 얼마나는 안 물어요.", "The doorkeeper checks the key and the face — never when, where, or how often."),
         "small": ('열쇠를 훔친 도둑도, 마음이 바뀐 진짜 요리사도 열쇠와 얼굴은 맞아요. <a href="siem-ko.html">경비실의 종</a>은 "금고 방에서 도둑!" 같은 정해진 규칙에만 울려요.',
                   'A thief with a stolen key and a real cook who changed sides both pass the key-and-face check. The <a href="siem-en.html">guard room\'s bell</a> only rings on fixed rules like "a thief in the vault!"')},
        {"svg": P3, "hero": True, "alt": ("경비실의 '평소 장부': 요리사는 새벽 5시 부엌, 하녀는 낮 2층, 목수는 오후 창고, 왕은 아무 때나 어디나. 파란 모자 친구가 매일 적고, 아래에 요리사·하녀·목수가 서 있음", "The guard room\'s book of usual: the cook — 5 a.m., kitchen; the maid — daytime, 2nd floor; the carpenter — afternoon, storeroom; the king — any time, anywhere. A blue-hat friend writes it daily; the cook, maid and carpenter stand below"),
         "caption": ("UEBA는 사람마다 '평소'를 기억하는 경비실이에요.", "UEBA is a guard room that remembers what is usual for every person."),
         "small": ('<a href="log-ko.html">일지</a>를 몇 주 동안 읽고 사람마다 언제·어디서·얼마나가 평소인지 적어 둬요. 사람뿐 아니라 방(기계)마다도요.',
                   'It reads the <a href="log-en.html">daily logs</a> for weeks and writes down each person\'s usual when, where, and how much. Not only people — every room (machine) too.'),
         "tricks": (4, [
             (BOOK_I, ("평소를 적어요", "Writes down the usual"), ("사람마다, 방마다 한 줄", "one line per person, per room"), "calm"),
             (DIFF_I, ("다른 점을 찾아요", "Spots the difference"), ("시간, 장소, 횟수, 양", "time, place, how often, how much"), "calm"),
             (SCORE_I, ("점수를 매겨요", "Keeps a score"), ("다른 만큼 점수가 올라요", "the stranger it is, the higher it goes"), "warm"),
             (BELL_I, ("높으면 종", "High score, ring the bell"), ("경비실 큰 화면으로 보내요", "sent to the guard room\'s big screen")),
         ])},
        {"svg": P4, "alt": ("밤. 요리사 옷의 도둑이 금고 방 앞. 위험 점수표: 밤 3시(평소 새벽 5시) +3, 금고 방(평소 부엌) +4, 한 시간에 다섯 번 +2, 합계 9 — 종! 파란 모자 친구 옆에서 종이 울림", "Night. The thief in the cook\'s coat at the vault. Risk score sheet: 3 a.m. (usually 5 a.m.) +3, the vault (usually kitchen) +4, five tries in one hour +2, total 9 — ring the bell! The bell rings beside the blue-hat friend"),
         "caption": ("요리사 열쇠가 밤 3시에 금고 방을 열면, 점수가 오르고 종이 울려요.", "When the cook\'s key opens the vault at 3 a.m., the score climbs and the bell rings."),
         "small": ('하나만 달라도 종은 안 울려요. 시간도, 방도, 횟수도 다르면 점수가 쌓여요. 종은 <a href="siem-ko.html">경비실 큰 화면</a>으로 가고, <a href="soc-ko.html">경비실</a>이 확인해요.',
                   'One odd thing alone doesn\'t ring the bell. Odd time, odd room, odd count — the points add up. The bell goes to the <a href="siem-en.html">big screen</a>, and the <a href="soc-en.html">guard room</a> checks.')},
        {"svg": P5, "alt": ("세 사람: 훔친 열쇠를 든 도둑(✓ 잡힘), 밤마다 종이를 들고 나가는 진짜 요리사(✓ 잡힘), 새로 온 하녀(? — 아직 평소가 없어 종이 잘못 울림)", "Three people: a thief with a stolen key (✓ caught), the real cook carrying papers out every night (✓ caught), and a new maid (? — no usual yet, so the bell rings by mistake)"),
         "caption": ("훔친 열쇠도, 이상해진 진짜 요리사도 잡아요. 처음 몇 주는 틀리기도 해요.", "It catches stolen keys and a real cook gone strange. In the first weeks, it also gets things wrong."),
         "small": ('여기가 비유가 깨지는 곳이에요. 새로 온 사람은 평소가 없어서 종이 잘못 울려요. 그래서 <a href="hunting-ko.html">파수꾼</a>이 점수를 직접 봐야 해요.',
                   'This is where the picture cracks. A newcomer has no usual yet, so the bell rings by mistake. That\'s why a <a href="hunting-en.html">watchman</a> still has to look at the scores.')},
    ],
    "summary": (("<b>UEBA</b> = 사람마다·방마다 <b>평소</b>를 적어 두고, 열쇠와 얼굴이 맞아도 <b>평소와 다르면 점수</b>를 올리고, 점수가 높으면 <b>종을 울리는</b> 경비실.",
                 "<b>UEBA</b> = a guard room that writes down the <b>usual</b> for every person and room, <b>raises a score</b> whenever a right key and right face still act unlike the usual, and <b>rings the bell</b> when the score is high."),
                ("User and Entity Behavior Analytics. 로그로 사용자와 기기의 행동 기준선(베이스라인)을 학습하고, 벗어난 정도를 위험 점수로 매겨 계정 탈취·내부자 위협·측면 이동을 찾아내요. 보통 SIEM에 붙어서 동작해요.",
                 "User and Entity Behavior Analytics learns a behavioral baseline for users and devices from logs, scores deviations as risk, and surfaces account takeover, insider threats, and lateral movement. It usually runs alongside a SIEM.")),
    "glossary": [
        ("평소 기억하기", "UEBA", ("사람마다 평소를 아는 경비실.", "The guard room that knows everyone\'s usual."), ("열쇠·얼굴이 아니라 언제·어디서·얼마나를 봐요. 사람(User)과 방·기계(Entity) 둘 다요.", "Looks at when, where, and how much — not the key and face. For people (users) and for rooms and machines (entities).")),
        ("평소", "Baseline", ("장부에 적힌 한 줄.", "The line in the book."), ("요리사는 새벽 5시 부엌. 몇 주 동안 일지를 읽어서 만들어요.", "The cook: 5 a.m., the kitchen. Built by reading weeks of logs.")),
        ("다른 점 찾기", "Anomaly detection", ("평소와 다른 걸음걸이.", "A walk unlike the usual."), ("밤 3시, 금고 방, 다섯 번. 규칙에 없어도 평소와 다르면 눈에 띄어요.", "3 a.m., the vault, five tries. No rule needed — different from usual is enough to stand out.")),
        ("위험 점수", "Risk score", ("다른 만큼 쌓이는 숫자.", "Points that pile up with strangeness."), ("하나면 조용히, 여럿이면 종. 사람마다 점수가 따로 있어요.", "One oddity stays quiet; several ring the bell. Every person carries their own score.")),
        ("훔친 열쇠", "Account takeover", ("남의 열쇠로 남인 척.", "Using someone else\'s key to be them."), ('열쇠는 훔쳐도 평소는 못 훔쳐요. 열쇠를 지키는 법은 → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'You can steal a key, but not the usual. Protecting the key itself → <a href="mfa-en.html">the doorkeeper who checks three times</a>')),
        ("이상해진 성 사람", "Insider threat", ("진짜 요리사가 종이를 들고 나가요.", "The real cook carrying papers out."), ("열쇠도 얼굴도 진짜라 문지기는 못 잡아요. 평소와 달라진 걸음걸이만 알아채요.", "Real key, real face — the doorkeeper can\'t catch it. Only the changed walk gives it away.")),
        ("경비실 큰 화면", "SIEM", ("종이 울리는 곳.", "Where the bell rings."), ('점수가 높으면 큰 화면에 올라가요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'High scores go up on the big screen. → <a href="siem-en.html">the guard room\'s big screen</a>')),
        ("배우는 몇 주", "Learning period / false positive", ("아직 평소가 없어요.", "No usual yet."), ("새 사람, 새 방은 종이 잘못 울려요. 처음엔 사람이 점수를 같이 봐야 해요.", "New people and new rooms ring the bell by mistake. At first, a person has to read the scores alongside.")),
    ],
}
