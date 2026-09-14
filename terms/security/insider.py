from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
MAID = dict(hat=None, shirt="#7B3FA0")
COOK = dict(hat="#FFF", shirt="#FFF")
CARPENTER = dict(hat="#E9B44C", shirt="#4A5A72")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def key(x, y, s=1.0, color="#E9B44C"):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="8" fill="none" stroke="{color}" stroke-width="4"/><rect x="6" y="-2" width="22" height="4" fill="{color}"/><rect x="20" y="2" width="3" height="6" fill="{color}"/><rect x="26" y="2" width="3" height="6" fill="{color}"/></g>'


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def door(x, y, s=1.0, open_=False):
    """벽에 난 작은 문. open_ 이면 문짝이 안쪽으로 열려 있음."""
    leaf = (f'<path d="M0 0 l-30 -14 v100 l30 14z" fill="{WOOD}"/>' if open_ else f'<rect width="48" height="100" rx="3" fill="{WOOD}"/><circle cx="38" cy="54" r="4" fill="#E9B44C"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-4" y="-4" width="56" height="104" fill="var(--night)"/>{leaf}</g>'


def paper(x, y, s=1.0, stamp=None, rot=0, text=None):
    st = f'<circle cx="18" cy="-14" r="9" fill="{stamp}"/>' if stamp else ""
    ln = "".join(f'<path d="M-18 {-8 + i * 9} h{28 - (i % 2) * 10}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for i in range(3))
    tx = label(0, 24, text, 9, "#142033") if text else ""
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{ln}{st}{tx}</g>'


def ledger(x, y, w, h, title):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="#C9A86A"/>' + label(x + w / 2, y + 19, title, 12, "#142033", cls="d")


# 1. 벽도 종도 개도 바깥을 봐요 — 밖의 도둑은 못 들어와요
P1 = svg(320, night(320)
         + '<rect x="300" y="88" width="460" height="172" fill="var(--stone-dark)"/>' + battlements(300, 68, 460, 8, "var(--stone-dark)")
         + bell(360, 100, 0.8, ring=False) + dog(440, 190, 0.9) + person(500, 90, s=0.85, face=SMILE, **GUARD) + label(560, 292, "⟦벽, 종, 개 — 모두 바깥을 봐요|wall, bell, dog — all facing outward⟧", 12, "#F5E6B8", cls="d")
         + person(100, 120, s=0.9, hat="var(--bad)", shirt="#2E3D57", face=MASK + SWEAT) + bubble(40, 40, 200, 34, "⟦못 들어가겠네…|no way in…⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(130, 292, "⟦밖의 도둑|the thief outside⟧", 12, "#C9D5E6"))

# 2. 그런데 안에서 문이 열려요 — 세 사람
P2 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + door(60, 70, 0.8, open_=True) + person(110, 90, s=0.8, face=EYES, **MAID) + key(150, 150, 0.8) + person(14, 140, s=0.55, **THIEF)
         + label(110, 250, "⟦하녀가 일부러 열어줘요|the maid opens it on purpose⟧", 12, "var(--ink)") + label(110, 272, "⟦도둑에게 금화를 받았어요|she took the thief\'s gold⟧", 10, "var(--muted)")
         + person(350, 90, s=0.8, face=EYES, **COOK) + paper(430, 190, 0.8, rot=25, text="⟦명부|roster⟧") + '<path d="M400 150 q20 10 24 30" stroke="var(--muted)" stroke-width="2" fill="none" stroke-dasharray="4 3"/>'
         + label(390, 250, "⟦요리사가 실수로 떨어뜨려요|the cook drops it by mistake⟧", 12, "var(--ink)") + label(390, 272, "⟦마을 장터에 명부를|the roster, at the village market⟧", 10, "var(--muted)")
         + person(620, 90, s=0.8, face=SMILE, **CARPENTER) + key(690, 120, 0.8) + label(640, 250, "⟦그만둔 목수에게 열쇠가 남았어요|the carpenter who quit kept a key⟧", 12, "var(--ink)") + label(640, 272, "⟦아무도 돌려받지 않았어요|nobody asked for it back⟧", 10, "var(--muted)")
         + label(380, 320, "⟦종은 성 안 사람에겐 안 울려요|the bell doesn\'t ring for people from inside⟧", 13, "var(--ink)", cls="d"))

# 3. 내부자 위협 = 안에서 문을 여는 사람 (hero)
P3 = svg(360, night(360)
         + '<rect x="0" y="88" width="760" height="172" fill="var(--stone-dark)"/>' + battlements(0, 68, 760, 12, "var(--stone-dark)")
         + door(330, 80, 1.0, open_=True) + person(400, 110, s=0.9, face=EYES, **MAID) + key(455, 175, 0.9) + person(250, 150, s=0.7, extra=BAG, **THIEF)
         + label(380, 292, "⟦열쇠를 가진 사람이 안에서 문을 열어요|someone with a key opens the door from inside⟧", 13, "#F5E6B8", cls="d")
         + '<rect x="40" y="90" width="150" height="34" rx="8" fill="var(--bad)"/>' + label(115, 112, "⟦일부러|on purpose⟧", 12, "#FFF", cls="d")
         + '<rect x="40" y="140" width="150" height="34" rx="8" fill="var(--accent)"/>' + label(115, 162, "⟦실수로|by mistake⟧", 12, "#FFF", cls="d")
         + '<rect x="40" y="190" width="150" height="34" rx="8" fill="#5B8DEF"/>' + label(115, 212, "⟦그만두고도|after leaving⟧", 12, "#FFF", cls="d")
         + bell(620, 120, 0.9, ring=False) + label(620, 200, "⟦종은 조용해요|the bell stays quiet⟧", 11, "#C9D5E6")
         + label(380, 336, "⟦벽은 바깥을 보고, 문은 안에서 열려요|the wall faces out, but the door opens from within⟧", 12, "#C9D5E6"))

# 4. 이상한 행동 알아채기 — 평소와 오늘 밤
P4 = svg(340, sky(340)
         + ledger(40, 30, 300, 200, "⟦하녀의 평소|THE MAID — USUALLY⟧")
         + label(60, 80, "⟦낮에만 다녀요|comes by day⟧", 12, "#142033", "start") + label(60, 110, "⟦부엌과 빨래방|kitchen and laundry⟧", 12, "#142033", "start") + label(60, 140, "⟦하루 열쇠 3번|uses her key 3 times⟧", 12, "#142033", "start") + label(60, 170, "⟦금고 방은 안 가요|never the vault⟧", 12, "#142033", "start")
         + ledger(420, 30, 300, 200, "⟦오늘 밤|TONIGHT⟧")
         + label(440, 80, "⟦밤 12시에|at midnight⟧", 12, "#B3261E", "start") + label(440, 110, "⟦금고 방 앞에서|outside the vault⟧", 12, "#B3261E", "start") + label(440, 140, "⟦열쇠를 20번|key used 20 times⟧", 12, "#B3261E", "start") + label(440, 170, "⟦뒷문이 열렸어요|the back door opened⟧", 12, "#B3261E", "start")
         + person(350, 235, s=0.55, face=EYES, **BLUE)
         + label(380, 318, "⟦평소와 다르면, 안에서도 종이 울려요|when it\'s not like usual, the bell rings from inside too⟧", 13, "var(--ink)", cls="d"))

# 5. 막는 법 네 가지
P5 = svg(340, sky(340)
         + key(70, 60, 1.0) + label(120, 66, "⟦딱 필요한 열쇠만 — 하녀는 부엌 열쇠만|only the keys you need — the maid gets the kitchen key⟧", 12, "var(--ink)", "start")
         + '<g transform="translate(70,120)"><rect x="-22" y="-14" width="44" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle r="7" fill="var(--bad)"/></g>' + label(120, 126, "⟦빨간 종이는 문지기가 잡아요 — 실수로도 못 나가요|the doorkeeper stops red papers — even by mistake⟧", 12, "var(--ink)", "start")
         + '<g transform="translate(70,180)"><rect x="-22" y="-16" width="44" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-14 -6 h28 M-14 2 h28 M-14 10 h18" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/><circle cx="16" cy="-10" r="7" fill="var(--bad)"/></g>' + label(120, 186, "⟦일지를 보고 평소와 다른 걸 알아채요|read the log and spot what\'s not usual⟧", 12, "var(--ink)", "start")
         + '<g transform="translate(70,240)"><path d="M-16 0 h32" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M8 -8 l8 8 l-8 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/></g>' + key(24, 240, 0.7)
         + label(120, 246, "⟦나갈 때 열쇠를 돌려받아요 — 그날 바로|take the key back the day they leave⟧", 12, "var(--ink)", "start")
         + label(380, 318, "⟦안쪽도 지키는 성이 진짜 튼튼한 성이에요|a castle that guards the inside too is a truly strong castle⟧", 13, "var(--ink)", cls="d"))

KEY_I = icon('<circle cx="22" cy="32" r="10" fill="none" stroke="#E9B44C" stroke-width="5"/><rect x="30" y="29" width="24" height="6" fill="#E9B44C"/><rect x="46" y="35" width="4" height="7" fill="#E9B44C"/><rect x="52" y="35" width="4" height="7" fill="#E9B44C"/>')
STAMP_I = icon('<rect x="12" y="18" width="40" height="30" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="33" r="9" fill="var(--bad)"/><path d="M8 12 l48 40" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
WATCH_I = icon('<circle cx="32" cy="32" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 18 v14 l9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="50" cy="14" r="7" fill="var(--bad)"/><path d="M47 14 h6" stroke="#FFF" stroke-width="2"/>')
RETURN_I = icon('<circle cx="18" cy="36" r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="24" y="34" width="18" height="5" fill="#E9B44C"/><path d="M52 20 l-8 -8 M52 20 l-8 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M52 20 h-20" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "insider", "order": 71,
    "title": ("안에서 문을 여는 사람", "The One Who Opens the Door From Inside"),
    "h1": ("<em>내부자 위협</em>이 뭐예요?", "What is an <em>Insider Threat</em>?"),
    "sub": ("내부자 위협(Insider Threat)을 벽·종·개가 모두 바깥을 보는 성에서, 열쇠를 가진 사람이 안에서 문을 여는 이야기로 풀어봤어요.",
            "Insider threats, told as a story about a castle whose wall, bell, and dog all face outward — while someone with a key opens the door from within."),
    "panels": [
        {"svg": P1, "alt": ("밤. 성벽 위에 종과 경비견과 경비가 모두 바깥을 향해 서 있고, 밖의 도둑은 땀을 흘리며 '못 들어가겠네'", "Night. On the wall, the bell, the guard dog, and the guard all face outward; the thief outside sweats: no way in"),
         "caption": ("우리 성은 바깥을 잘 지켜요. 벽도, 종도, 개도 바깥을 봐요.", "Our castle guards the outside well. The wall, the bell, the dog all face out."),
         "small": ('<a href="firewall-ko.html">성벽</a>, <a href="edr-ko.html">경비견</a>, <a href="soc-ko.html">경비실</a>. 밖의 도둑은 들어올 수가 없어요.',
                   'The <a href="firewall-en.html">wall</a>, the <a href="edr-en.html">guard dog</a>, the <a href="soc-en.html">guard room</a>. A thief outside can\'t get in.')},
        {"svg": P2, "alt": ("세 장면: 하녀가 열쇠로 뒷문을 열어 도둑을 들이고, 요리사가 명부를 떨어뜨리고, 그만둔 목수가 아직 열쇠를 들고 있음", "Three scenes: the maid unlocks the back door for a thief, the cook drops the roster, and the carpenter who quit still holds a key"),
         "caption": ("그런데 안에서 문이 열려요. 일부러, 실수로, 또는 그만둔 사람이요.", "But the door opens from inside — on purpose, by mistake, or by someone who already left."),
         "small": ("하녀는 금화를 받고 일부러 열어요. 요리사는 실수로 명부를 흘려요. 목수는 그만뒀는데 열쇠를 안 돌려줬어요. 셋 다 종이 안 울려요.", "The maid takes gold and opens it on purpose. The cook drops the roster by accident. The carpenter quit but never returned the key. None of them ring the bell.")},
        {"svg": P3, "hero": True, "alt": ("밤의 성벽 한가운데 문이 안쪽에서 열려 있고, 열쇠를 든 하녀가 도둑을 들임. 왼쪽에 세 가지 꼬리표: 일부러, 실수로, 그만두고도. 오른쪽 종은 조용함", "A door in the night wall opens from within; the maid with a key lets the thief in. Three tags on the left: on purpose, by mistake, after leaving. The bell on the right stays quiet"),
         "caption": ("내부자 위협은 안에서 문을 여는 사람이에요.", "An insider threat is someone who opens the door from inside."),
         "small": ("벽은 바깥을 보는데, 열쇠를 가진 사람은 이미 안에 있어요. 일부러든, 실수로든, 그만둔 뒤든 — 열쇠가 문을 열면 종은 조용해요.", "The wall faces out, but the person with the key is already inside. On purpose, by mistake, or after leaving — when a key opens the door, the bell stays quiet."),
         "tricks": (4, [
             (KEY_I, ("딱 필요한 열쇠만", "Only the keys you need"), ("부엌 사람은 부엌 열쇠만", "kitchen folk get kitchen keys"), "warm"),
             (STAMP_I, ("빨간 종이 문지기", "The red-paper doorkeeper"), ("실수로도 못 나가게", "so it can\'t slip out by mistake")),
             (WATCH_I, ("평소와 다르면 알아채기", "Notice what\'s not usual"), ("밤 12시에 금고 방?", "the vault at midnight?")),
             (RETURN_I, ("나갈 때 열쇠 회수", "Take keys back at leaving"), ("그만둔 날 바로", "the very day they quit"), "calm"),
         ])},
        {"svg": P4, "alt": ("두 장부: '하녀의 평소' — 낮에만, 부엌과 빨래방, 열쇠 3번, 금고 방은 안 감. '오늘 밤' — 밤 12시, 금고 방 앞, 열쇠 20번, 뒷문 열림. 경비실 친구가 둘을 비교함", "Two ledgers: the maid usually — by day, kitchen and laundry, key 3 times, never the vault. Tonight — midnight, outside the vault, key 20 times, back door opened. The guard compares them"),
         "caption": ("평소와 다르면, 안에서도 종이 울려요.", "When it\'s not like usual, the bell rings from inside too."),
         "small": ('하녀는 낮에 부엌만 다녀요. 그런데 밤 12시에 금고 방에서 열쇠를 20번? <a href="log-ko.html">일지</a>를 평소와 비교하면 안쪽 사람의 이상한 행동도 보여요.',
                   'The maid only visits the kitchen by day. So — the vault at midnight, key used 20 times? Compare the <a href="log-en.html">log</a> with the usual, and odd behaviour from inside shows up.')},
        {"svg": P5, "alt": ("네 줄 목록: 딱 필요한 열쇠만, 빨간 종이는 문지기가 잡음, 일지로 평소와 다른 걸 알아챔, 나갈 때 열쇠를 돌려받음", "A four-line list: only the keys you need, the doorkeeper stops red papers, read the log for what\'s not usual, take keys back on leaving"),
         "caption": ("안쪽도 지키는 성이 진짜 튼튼한 성이에요.", "A castle that guards the inside too is a truly strong castle."),
         "small": ('<a href="rbac-ko.html">열쇠 꾸러미</a>는 딱 필요한 만큼만, <a href="dlp-ko.html">빨간 도장</a>은 문지기가, 이상한 행동은 <a href="log-ko.html">일지</a>로, 나갈 땐 <a href="iam-ko.html">명부 관리소</a>가 열쇠를 회수해요.',
                   'Give <a href="rbac-en.html">key rings</a> only as needed, let the doorkeeper catch the <a href="dlp-en.html">red stamp</a>, spot odd behaviour in the <a href="log-en.html">log</a>, and have the <a href="iam-en.html">roster office</a> take keys back on the way out.')},
    ],
    "summary": (("<b>내부자 위협</b> = 열쇠를 가진 성 안 사람이 <b>일부러, 실수로, 또는 그만둔 뒤에</b> 안에서 문을 여는 것. 벽과 종은 바깥만 보니까 <b>안쪽을 지키는 눈</b>이 따로 필요해요.",
                 "<b>Insider threat</b> = someone inside the castle with a key opening the door <b>on purpose, by mistake, or after leaving</b>. The wall and the bell only face out, so you need <b>eyes on the inside</b> too."),
                ("Insider Threat. 직원·협력사 등 정당한 접근 권한을 가진 사람이 악의(malicious), 부주의(negligent), 또는 퇴직 후 남은 권한으로 조직에 피해를 주는 위협이에요. 최소 권한, DLP, 행동 분석(UEBA), 퇴직 절차로 막아요.",
                 "A threat from someone with legitimate access — an employee or contractor — who harms the organization maliciously, negligently, or through access that outlived their job. Countered with least privilege, DLP, behaviour analytics (UEBA), and offboarding.")),
    "glossary": [
        ("안에서 문을 여는 사람", "Insider threat", ("열쇠를 가진 성 안 사람.", "Someone inside who has a key."), ("벽도 종도 개도 바깥만 봐서, 이 사람은 그냥 지나가요.", "The wall, bell, and dog all face out, so this person walks right past.")),
        ("일부러 · 실수로 · 그만두고도", "Malicious · Negligent · Departed", ("하녀, 요리사, 목수.", "The maid, the cook, the carpenter."), ("금화를 받고 문을 열거나, 명부를 흘리거나, 열쇠를 안 돌려주거나. 셋 다 안에서 나온 일이에요.", "Opening a door for gold, dropping the roster, keeping a key. All three come from inside.")),
        ("평소와 다른 행동 알아채기", "UEBA (User and Entity Behavior Analytics)", ("하녀의 평소 vs 오늘 밤.", "The maid\'s usual vs. tonight."), ('낮에 부엌만 다니던 사람이 밤 12시에 금고 방 앞이면 종을 울려요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'If the kitchen-by-day person is at the vault at midnight, ring the bell. → <a href="siem-en.html">the guard room\'s big screen</a>')),
        ("둘이 같이 열기", "Separation of duties", ("금고는 열쇠 두 개가 같이.", "The vault takes two keys at once."), ("한 사람 혼자서는 큰일을 못 하게 나눠요. 돈을 세는 사람과 내보내는 사람을 다르게.", "Split big jobs so one person alone can\'t do them: the one who counts the gold isn\'t the one who sends it.")),
        ("나갈 때 열쇠 회수", "Offboarding", ("그만둔 날 바로 열쇠 돌려받기.", "Take the key back the day they leave."), ('목수가 그만두면 그날 명부에서 지우고 열쇠를 거둬요. → <a href="iam-ko.html">성의 명부 관리소</a>', 'The day the carpenter quits, cross him off the roster and collect the key. → <a href="iam-en.html">the roster office</a>')),
        ("빨간 종이 문지기", "DLP (Data Loss Prevention)", ("빨간 도장 종이는 못 나가요.", "Red-stamped papers never leave."), ('요리사가 실수로 들고 나가도 문지기가 잡아요. → <a href="dlp-ko.html">빨간 도장 찍힌 종이</a>', 'Even if the cook carries it out by mistake, the doorkeeper catches it. → <a href="dlp-en.html">the red-stamped paper</a>')),
        ("딱 필요한 열쇠만", "Least privilege", ("부엌 사람은 부엌 열쇠만.", "Kitchen folk get only the kitchen key."), ('열쇠가 적으면 열 수 있는 문도 적어요. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>, <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'Fewer keys, fewer doors to open. → <a href="rbac-en.html">a key ring per hat</a>, <a href="pam-en.html">the master key in the vault</a>')),
        ("일지", "Audit log", ("누가 언제 어느 문을 열었는지.", "Who opened which door, and when."), ('안쪽 사람의 이상한 행동은 일지에만 남아요. → <a href="log-ko.html">성 곳곳의 한 줄 일지</a>', 'Odd behaviour from inside shows up only in the log. → <a href="log-en.html">the one-line log book</a>')),
    ],
}
