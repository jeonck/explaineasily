from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
DOORS = (("⟦부엌|Kitchen⟧", False), ("⟦회의실|Meeting⟧", False), ("⟦창고|Storage⟧", False), ("⟦서재|Study⟧", False), ("", False))


def sparkle(x, y, s=1.0):
    return f'<path d="M{x} {y - 8 * s} l{2 * s} {6 * s} l{6 * s} {2 * s} l{-6 * s} {2 * s} l{-2 * s} {6 * s} l{-2 * s} {-6 * s} l{-6 * s} {-2 * s} l{6 * s} {-2 * s}z" fill="#FFD166"/>'


def fake_vault(x, y, s=1.0, sign=True, open_=False):
    door = ('<rect x="-30" width="60" height="100" rx="3" fill="#E9B44C"/><rect x="-30" width="20" height="100" fill="var(--night)"/>' if open_
            else '<rect x="-30" width="60" height="100" rx="3" fill="#E9B44C"/><circle cx="0" cy="50" r="14" fill="none" stroke="#C9822B" stroke-width="5"/><circle cy="50" r="4" fill="var(--bad)"/>')
    sg = ('<rect x="-40" y="-40" width="80" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(0, -22, "⟦보물 창고|TREASURE⟧", 11, "var(--bad)") if sign else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{door}{sg}{sparkle(-38, 10)}{sparkle(40, 30, 0.8)}{sparkle(-34, 80, 0.7)}{sparkle(44, 90)}</g>')


BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GLASS = '<g transform="translate(70,60)"><circle r="16" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M12 12 L26 26" stroke="var(--night)" stroke-width="6" stroke-linecap="round"/></g>'
PEN = '<g transform="translate(66,70) rotate(-30)"><rect x="-3" y="-18" width="6" height="30" rx="2" fill="#5B8DEF"/><path d="M-3 12 L0 20 L3 12 Z" fill="#142033"/></g>'


def bell(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/><rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def cat(x, y, s=1.0, color="var(--stone-dark)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="26" cy="30" rx="26" ry="16" fill="{color}"/>'
            f'<circle cx="-2" cy="14" r="14" fill="{color}"/><path d="M-12 6 L-10 -8 L-2 4 Z M8 4 L12 -8 L6 6 Z" fill="{color}"/>'
            f'<path d="M50 28 q14 -10 8 -26" stroke="{color}" stroke-width="6" fill="none" stroke-linecap="round"/></g>')


# 1. 도둑은 보물을 찾아 돌아다닌다
P1 = svg(300, corridor(300, DOORS, marks=False)
         + person(200, 150, s=0.85, face=MASK, extra=BAG)
         + "".join(f'<path d="M{x} 150 l-6 -8 M{x} 150 l-6 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>' for x in (350, 490, 630))
         + '<path d="M270 200 C350 170 450 230 600 190" stroke="var(--bad)" stroke-width="2" stroke-dasharray="6 6" fill="none"/>'
         + label(380, 285, "⟦문마다 두드려 보고, 열린 데를 찾아요|knocks on every door, looking for one that opens⟧", 13, "#F5E6B8"))

# 2. 파수꾼의 종은 고양이한테도 울린다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + bell(120, 70, 0.8) + cat(90, 150, 0.9) + label(120, 240, "⟦고양이|a cat⟧", 12, "var(--muted)")
         + bell(300, 70, 0.8) + cat(270, 150, 0.9) + label(300, 240, "⟦또 고양이|another cat⟧", 12, "var(--muted)")
         + bell(480, 70, 0.8) + person(450, 130, s=0.75, face=MASK, extra=BAG) + label(480, 240, "⟦진짜 도둑|the real thief⟧", 12, "var(--bad)")
         + person(640, 100, s=0.9, face=FROWN + SWEAT, **GUARD) + label(670, 240, "⟦매번 가서 봐야 해요|has to check every time⟧", 11, "var(--muted)"))

# 3. 허니팟 = 아무도 안 쓰는 반짝이는 가짜 방 (hero)
P3 = svg(340, corridor(340, DOORS, marks=False) + fake_vault(662, 80)
         + person(320, 150, s=0.85, face=MASK, extra=BAG)
         + '<path d="M390 200 C480 180 560 200 620 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/><path d="M610 180 L622 190 L610 200" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + "".join(person(x, 210, s=0.5, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((60, "#E9B44C"), (130, None), (200, "#5B8DEF")))
         + label(140, 300, "⟦진짜 사람은 갈 일이 없어요|real people never go there⟧", 12, "#F5E6B8")
         + person(560, 40, s=0.55, face=EYES, **GUARD, extra=GLASS)
         + label(590, 322, "⟦그 문이 열리면 무조건 도둑|if that door opens, it\'s a thief — no question⟧", 13, "#F5E6B8"))

# 4. 도둑이 뭘 하는지 다 적는다
NOTEBOOK = ('<g transform="translate(470,60)"><rect width="200" height="120" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            + "".join(label(12, 28 + i * 22, t, 12, "#142033", "start") for i, t in enumerate(("⟦02:10 자물쇠 도구 3번|02:10 lockpick #3⟧", "⟦02:11 서랍부터 열어봄|02:11 tries the drawer first⟧", "⟦02:12 가짜 열쇠 집어감|02:12 takes the fake key⟧", "⟦02:15 성문으로 나감|02:15 leaves by the gate⟧"))) + "</g>")
P4 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + fake_vault(120, 60, 1.0, open_=True) + person(180, 90, s=0.85, face=MASK, extra='<g transform="translate(66,66)"><rect x="-3" y="-20" width="6" height="30" fill="var(--stone-dark)"/><path d="M-8 -22 h16 v6 h-16z" fill="var(--stone-dark)"/></g>')
         + '<g transform="translate(150,200)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="6" y="-2" width="22" height="4" fill="#E9B44C"/></g>' + label(150, 230, "⟦가짜 열쇠|a fake key⟧", 11, "var(--bad)")
         + person(360, 90, s=0.8, face=EYES, **GUARD, extra=PEN) + NOTEBOOK
         + '<path d="M570 190 L570 230" stroke="var(--good)" stroke-width="3"/><path d="M560 220 L570 232 L580 220" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + '<g transform="translate(520,262)"><rect x="-24" y="-30" width="48" height="60" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(0, -14, "⟦수배|WANTED⟧", 9, "var(--bad)") + f'<circle cy="4" r="10" fill="{SKIN}"/><path d="M-10 0 Q0 -14 10 0 Z" fill="var(--bad)"/></g>'
         + label(640, 262, "⟦→ 수배 전단, 망루 친구 쪽지|→ wanted posters, the watchtower\'s notes⟧", 11, "var(--muted)")
         + label(380, 305, "⟦어떤 도구를 쓰는지, 어디를 먼저 여는지 — 도둑의 버릇을 배워요|which tools, which drawer first — the thief\'s habits, learned⟧", 12, "var(--muted)"))

# 5. 미끼 방은 진짜 성과 떼어 놓아야 한다
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + fake_vault(90, 60, 0.9, open_=True) + '<path d="M140 120 L230 120" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/><path d="M220 110 L232 120 L220 130" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + f'<g transform="translate(270,70) scale(0.7)"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><circle cx="20" cy="54" r="4" fill="#E9B44C"/></g>' + label(270, 160, "⟦진짜 금고|the real vault⟧", 12, "var(--ink)")
         + person(160, 170, s=0.7, face=MASK + SWEAT, extra=BAG)
         + label(190, 270, "⟦미끼 방이 진짜 복도로 통하면|if the bait room joins the real hallway⟧", 12, "var(--bad)") + label(190, 292, "⟦도둑에게 발판을 준 거예요|you\'ve handed the thief a foothold⟧", 11, "var(--muted)")
         + fake_vault(520, 60, 0.9) + '<rect x="470" y="30" width="100" height="22" rx="4" fill="var(--bad)"/>' + label(520, 46, "⟦미끼입니다|BAIT⟧", 11, "#FFF")
         + person(650, 110, s=0.8, face=MASK) + bubble(600, 180, 150, 34, "⟦안 속아요|not falling for it⟧", 12, "var(--panel)", "var(--bad)", "left")
         + label(570, 270, "⟦너무 티 나면 도둑이 안 와요|too obvious, and no thief comes⟧", 12, "var(--bad)") + label(570, 292, "⟦잡는 거지 막는 게 아니에요|it catches; it doesn\'t block⟧", 11, "var(--muted)"))

BAIT_I = icon('<rect x="20" y="10" width="24" height="44" rx="2" fill="#E9B44C"/><circle cx="32" cy="32" r="6" fill="none" stroke="#C9822B" stroke-width="3"/><path d="M12 14 l1 3 3 1 -3 1 -1 3 -1 -3 -3 -1 3 -1z" fill="#FFD166"/><path d="M52 40 l1 3 3 1 -3 1 -1 3 -1 -3 -3 -1 3 -1z" fill="#FFD166"/>')
NOBODY_I = icon('<rect x="20" y="10" width="24" height="44" rx="2" fill="#E9B44C"/><circle cx="46" cy="18" r="9" fill="var(--bad)"/><path d="M42 14 l8 8 M50 14 l-8 8" stroke="#FFF" stroke-width="2.5"/>')
WATCH_I = icon('<path d="M6 32 Q32 8 58 32 Q32 56 6 32 Z" fill="none" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--good)"/>')
TIME_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 18 V32 L42 38" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M14 52 l36 -40" stroke="var(--accent)" stroke-width="2" stroke-dasharray="3 3"/>')

PAGE = {
    "slug": "honeypot", "order": 46,
    "title": ("반짝이는 가짜 금고 방", "The Shiny Fake Vault"),
    "h1": ("<em>허니팟</em>이 뭐예요?", "What is a <em>Honeypot</em>?"),
    "sub": ("허니팟(Honeypot)을 아무도 쓰지 않는 반짝이는 가짜 금고 방 이야기로 풀어봤어요.",
            "Honeypots, told as a story about a shiny fake vault that nobody real ever uses."),
    "panels": [
        {"svg": P1, "alt": ("가방을 든 도둑이 복도의 문마다 두드려 보며 돌아다님", "A thief with a bag wanders the hallway, knocking on every door"),
         "caption": ("도둑은 보물을 찾아 돌아다녀요.", "Thieves wander around looking for treasure."),
         "small": ("문마다 두드려 보고, 열린 데를 찾아요.", "They knock on every door, looking for one that opens.")},
        {"svg": P2, "alt": ("종 세 개 아래 고양이, 또 고양이, 그리고 진짜 도둑. 경비는 땀을 흘림", "Three bells: a cat, another cat, and the real thief; the guard sweats"),
         "caption": ("파수꾼의 종은 고양이한테도 울려요.", "The watchers' bells ring for cats, too."),
         "small": ('진짜 도둑인지 고양이인지 매번 가서 봐야 해요. <a href="soc-ko.html">경비실</a>이 지치는 이유예요.',
                   'Cat or thief, someone has to go and look every time. It\'s what wears the <a href="soc-en.html">guard room</a> out.')},
        {"svg": P3, "hero": True, "alt": ("복도 끝에 '보물 창고' 팻말과 반짝이는 황금 문. 성 사람들은 반대쪽에서 일하고, 도둑만 점선을 따라 그 문으로 감. 위에서 경비가 돋보기로 지켜봄", "At the end of the hallway, a sparkling golden door under a TREASURE sign. Castle folk work at the other end; only the thief follows a dotted line to the door, while a guard watches from above with a magnifying glass"),
         "caption": ("허니팟은 아무도 안 쓰는 반짝이는 가짜 방이에요.", "A honeypot is a shiny fake room that nobody real uses."),
         "small": ("진짜 사람은 갈 일이 없어요. 그 문이 열리면 무조건 도둑이에요.", "Real people have no reason to go there. If that door opens, it's a thief — no question."),
         "tricks": (4, [
             (BAIT_I, ("미끼", "The bait"), ("진짜처럼 반짝여요", "shines like the real thing"), "warm"),
             (NOBODY_I, ("아무도 안 씀", "Nobody uses it"), ("열리면 = 도둑", "opened = thief")),
             (WATCH_I, ("지켜보기", "Watching"), ("버릇을 배워요", "learn the habits"), "calm"),
             (TIME_I, ("시간 끌기", "Wasting their time"), ("도둑이 헛수고해요", "the thief works for nothing"), "calm"),
         ])},
        {"svg": P4, "alt": ("가짜 금고 안에서 도구를 쓰는 도둑, 가짜 열쇠, 그걸 적는 경비의 공책: 02:10 자물쇠 도구 3번, 서랍부터, 가짜 열쇠 집어감… 아래엔 수배 전단", "The thief works his tools inside the fake vault and picks up a fake key; a guard writes it all down — 02:10 lockpick #3, the drawer first, takes the fake key…; below, a wanted poster"),
         "caption": ("도둑이 뭘 하는지 다 적어요.", "Everything the thief does gets written down."),
         "small": ('어떤 도구를 쓰는지, 어디를 먼저 여는지. 그걸로 <a href="idsips-ko.html">수배 전단</a>과 <a href="cti-ko.html">망루 친구</a>의 쪽지를 만들어요. 집어간 가짜 열쇠를 어디서든 쓰면 또 종이 울려요.',
                   'Which tools, which drawer first. That becomes <a href="idsips-en.html">wanted posters</a> and the <a href="cti-en.html">watchtower friend</a>\'s notes. And if the fake key is ever used anywhere, another bell rings.')},
        {"svg": P5, "alt": ("왼쪽: 가짜 금고에서 진짜 금고로 이어진 점선과 도둑. 오른쪽: '미끼입니다' 팻말이 붙은 가짜 문 앞에서 도둑이 '안 속아요'", "Left: a dotted line from the fake vault to the real one, thief in between. Right: a fake door labeled BAIT, and the thief saying not falling for it"),
         "caption": ("미끼 방은 진짜 성과 떼어 놓아야 해요.", "The bait room must be kept apart from the real castle."),
         "small": ('미끼 방에서 진짜 복도로 통하면 도둑에게 발판을 준 거예요 — <a href="vlan-ko.html">복도를 나눠요</a>. 그리고 너무 티 나면 도둑이 안 와요. 잡는 거지 막는 게 아니에요.',
                   'If the bait room joins the real hallway, you\'ve handed the thief a foothold — <a href="vlan-en.html">split the hallway</a>. And if it\'s too obvious, no thief comes. It catches; it doesn\'t block.')},
    ],
    "summary": (("<b>허니팟</b> = 아무도 쓰지 않는 <b>반짝이는 가짜 방</b>. 그 문이 열리면 <b>무조건 도둑</b>이고, 도둑이 뭘 하는지 다 적어요.",
                 "A <b>honeypot</b> = a <b>shiny fake room</b> nobody real uses. If its door opens, it's <b>always a thief</b> — and everything the thief does gets written down."),
                ("Honeypot. 가짜 열쇠는 허니토큰, 가짜 성 통째는 허니넷이에요. 종이 거의 틀리지 않는 게 장점. 막는 도구가 아니라 잡고 배우는 도구예요.",
                 "A fake key is a honeytoken; a whole fake castle is a honeynet. The bell almost never lies — that\'s the point. It\'s a tool for catching and learning, not for blocking.")),
    "glossary": [
        ("허니팟", "Honeypot", ("가짜 방.", "The fake room."), ("진짜처럼 보이지만 아무도 안 쓰는 물건이나 방.", "Looks real, but nobody real ever uses it.")),
        ("허니토큰", "Honeytoken", ("가짜 열쇠.", "The fake key."), ("'금고 열쇠.txt' 같은 가짜 문서. 어디서든 쓰이면 종이 울려요.", "A fake file like vault-key.txt. Used anywhere, it rings a bell.")),
        ("허니넷", "Honeynet", ("가짜 성.", "The fake castle."), ("방 하나가 아니라 성 한 채를 미끼로.", "Not one room — a whole castle as bait.")),
        ("저상호작용 · 고상호작용", "Low · high interaction", ("문만 있는 방 · 안까지 진짜 같은 방.", "Just a door · furnished inside too."), ("문만 두면 안전하고 싸요. 안까지 꾸미면 더 많이 배우지만 더 위험해요.", "A door alone is cheap and safe. Furnish it and you learn more — but risk more.")),
        ("기만 기술", "Deception technology", ("미끼를 성 곳곳에.", "Bait everywhere."), ("가짜 방, 가짜 열쇠, 가짜 장부를 성 전체에 뿌려요.", "Fake rooms, keys and ledgers scattered across the castle.")),
        ("오탐 없음", "No false positives", ("열리면 무조건 도둑.", "Opened means thief."), ('고양이는 가짜 금고에 안 가요. → <a href="soc-ko.html">경비실의 고양이</a>', 'Cats don\'t visit fake vaults. → <a href="soc-en.html">the guard room\'s cat</a>')),
        ("TTP 수집", "TTP collection", ("버릇 배우기.", "Learning habits."), ('도둑이 미끼 방에서 보여준 순서. → <a href="ttp-ko.html">도둑의 버릇</a>', 'The routine the thief shows in the bait room. → <a href="ttp-en.html">the burglar\'s habit</a>')),
        ("격리", "Isolation", ("진짜 성과 떼어 놓기.", "Kept apart from the real castle."), ('미끼 방에서 진짜 복도로 못 가게. → <a href="vlan-ko.html">색 리본으로 나눈 복도</a>', 'No road from the bait room into the real hallway. → <a href="vlan-en.html">the hallway split by ribbons</a>')),
    ],
}
