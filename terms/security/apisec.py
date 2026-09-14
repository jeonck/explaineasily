from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
RUNNER = dict(hat="var(--accent)", shirt="#4A5A72")   # 다른 성의 심부름꾼
VISITOR = dict(hat=None, shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
BOX = '<rect x="48" y="66" width="34" height="26" rx="3" fill="#8B5E3C"/><path d="M48 74 h34" stroke="#5A3B22" stroke-width="3"/>'


def door(x, y, w=60, h=100, color=WOOD, boarded=False, old=False):
    """바닥 y 에 서 있는 아치문. 왼쪽 위 x."""
    op = ' opacity="0.55"' if old else ""
    out = f'<g{op}><path d="M{x} {y} V{y - h + w / 2} a{w / 2} {w / 2} 0 0 1 {w} 0 V{y} Z" fill="{color}"/><circle cx="{x + w - 14}" cy="{y - h / 2}" r="4" fill="#E9B44C"/>'
    if old:
        out += f'<path d="M{x + 4} {y - h + 10} l14 10 l-12 8 l16 6" stroke="#C9D5E6" stroke-width="1.5" fill="none"/>'
    if boarded:
        out += f'<path d="M{x - 6} {y - h + 20} L{x + w + 6} {y - 30} M{x + w + 6} {y - h + 20} L{x - 6} {y - 30}" stroke="var(--good)" stroke-width="7" stroke-linecap="round"/>'
    return out + "</g>"


def roster(x, y, s=1.0, lines=5):
    ln = "".join(f'<path d="M-18 {-14 + i * 9} h{28 - (i % 2) * 8}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for i in range(lines))
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{ln}</g>'


def ticket(x, y, s=1.0, text="⟦입장권|TICKET⟧"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-16" width="60" height="32" rx="5" fill="var(--accent)"/>'
            f'<circle cx="-30" cy="0" r="5" fill="var(--sky)"/><circle cx="30" cy="0" r="5" fill="var(--sky)"/>' + label(0, 5, text, 11, "#FFF") + "</g>")


def board(x, y, w, h, title, rows):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


# 1. 창구 뒤엔 심부름꾼 전용 작은 문이 있어요
P1 = svg(320, sky(320)
         + small_castle(722, 120, 0.22) + label(740, 168, "⟦다른 성|other castle⟧", 9, "var(--muted)")
         + '<rect x="40" y="100" width="680" height="170" fill="var(--stone-dark)"/>'
         + '<rect x="110" y="130" width="150" height="100" rx="4" fill="var(--sky)" stroke="#5A3B22" stroke-width="4"/>' + person(160, 140, s=0.6, face=SMILE, **CLERK)
         + person(50, 175, s=0.75, face=SMILE, **VISITOR) + bubble(20, 40, 220, 34, "⟦빵 한 개 주세요|one loaf, please⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + door(470, 270) + person(560, 170, s=0.75, face=SMILE, extra=BOX, **RUNNER)
         + bubble(470, 40, 250, 34, "⟦빵집 성에서 왔어요, 밀가루 주세요|from the bakery castle, flour please⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(78, 288, "⟦손님|a visitor⟧", 10, "var(--muted)") + label(185, 288, "⟦창구|the counter⟧", 11, "var(--ink)", cls="d")
         + label(500, 288, "⟦심부름꾼 문|the runners\' door⟧", 11, "var(--ink)", cls="d") + label(640, 288, "⟦다른 성의 심부름꾼|another castle\'s runner⟧", 10, "var(--muted)")
         + label(380, 312, "⟦창구 뒤엔 심부름꾼 전용 작은 문이 있어요|behind the counter is a small door just for runners⟧", 12, "var(--ink)"))

# 2. 그 문에 문지기가 없으면
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + door(60, 190) + person(130, 95, s=0.75, face=MASK, extra=BAG) + roster(210, 150, 0.8) + roster(226, 140, 0.8)
         + label(130, 225, "⟦문지기가 없어요|no doorkeeper⟧", 12, "var(--ink)", cls="d") + label(130, 247, "⟦명부를 통째로 가져가요|takes the whole roster⟧", 11, "var(--bad)")
         + door(310, 190) + person(385, 95, s=0.75, face=MASK) + "".join(label(286 + (i % 2) * 10, 60 + i * 26, "⟦쾅|BANG⟧", 12 + (i % 2) * 3, "var(--bad)", cls="d") for i in range(4))
         + label(380, 225, "⟦하루 만 번 두드려요|knocks ten thousand times a day⟧", 12, "var(--ink)", cls="d") + label(380, 247, "⟦아무도 안 세요|and nobody counts⟧", 11, "var(--bad)")
         + door(600, 190, old=True) + person(660, 110, s=0.6, face=MASK) + label(630, 225, "⟦잊힌 옛 문|a forgotten old door⟧", 12, "var(--ink)", cls="d") + label(630, 247, "⟦있는지도 몰라요|nobody remembers it\'s there⟧", 11, "var(--bad)")
         + label(380, 285, "⟦창구엔 검토원이 있는데, 뒷문엔 아무도 없어요|the counter has a checker — the back door has no one⟧", 12, "var(--muted)"))

# 3. 뒷문에도 문지기를 (hero)
P3 = svg(360, sky(360)
         + '<rect x="40" y="60" width="680" height="190" fill="var(--stone-dark)"/>' + door(250, 250, 70, 130)
         + person(110, 140, s=0.8, face=SMILE, **RUNNER) + ticket(195, 175, 0.7) + label(195, 205, "⟦입장권|ticket⟧", 10, "#F5E6B8")
         + person(270, 130, s=0.9, face=EYES, **GUARD)
         + board(420, 50, 280, 170, "⟦뒷문 문지기 규칙|BACK-DOOR RULES⟧", ("⟦1. 입장권을 봐요|1. check the ticket⟧", "⟦2. 자기 상자만 열게 해요|2. open only their own box⟧", "⟦3. 두드리는 횟수를 세요|3. count the knocks⟧", "⟦4. 문 목록표를 적어요|4. keep a list of doors⟧"))
         + label(138, 272, "⟦심부름꾼|runner⟧", 11, "var(--muted)") + label(302, 272, "⟦문지기|doorkeeper⟧", 11, "var(--muted)")
         + label(380, 306, "⟦뒷문에도 문지기를 세워요 — 창구만큼 꼼꼼하게|put a doorkeeper on the back door too — as careful as the counter⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦입장권을 보고, 자기 상자만 열게 하고, 두드리는 횟수를 세요|check the ticket, open only their own box, count the knocks⟧", 12, "var(--muted)"))

# 4. 자기 상자만 — 옆 상자는 열쇠가 있어도 안 돼요
BOXES = "".join(f'<rect x="{340 + i * 62}" y="150" width="52" height="46" rx="4" fill="#8B5E3C"/><path d="M{340 + i * 62} 162 h52" stroke="#5A3B22" stroke-width="3"/>' + label(366 + i * 62, 188, f"⟦{n}번|#{n}⟧", 12, "#FFF8E7", cls="d") for i, n in enumerate((6, 7, 8, 9)))
P4 = svg(320, sky(320)
         + person(60, 120, s=0.8, face=SMILE, **RUNNER) + bubble(20, 30, 250, 34, "⟦7번 상자요! …8번도요|box 7! …and box 8 too⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(190, 120, s=0.85, face=EYES, **GUARD) + bubble(300, 30, 230, 34, "⟦7번은 돼요. 8번은 안 돼요|7, yes. 8, no.⟧", 11, "var(--panel)", "var(--good)", "left")
         + '<rect x="330" y="200" width="270" height="8" fill="#5A3B22"/>' + BOXES
         + '<path d="M420 128 l8 8 l14 -16" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M480 122 l16 16 M496 122 l-16 16" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + '<rect x="615" y="110" width="110" height="90" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + ticket(670, 128, 0.6) + label(670, 160, "⟦빵집 성|bakery castle⟧", 11, "#142033") + label(670, 182, "⟦7번 상자만|box 7 only⟧", 11, "#142033", cls="d")
         + label(670, 236, "⟦오늘 두드린 횟수 998|knocks today: 998⟧", 10, "var(--muted)") + label(670, 254, "⟦1000이면 잠깐 쉬어요|at 1000, take a break⟧", 10, "var(--accent)")
         + label(88, 250, "⟦심부름꾼|runner⟧", 11, "var(--muted)") + label(222, 250, "⟦문지기|doorkeeper⟧", 11, "var(--muted)") + label(465, 236, "⟦상자 선반|the box shelf⟧", 11, "var(--muted)")
         + label(380, 300, "⟦입장권에 적힌 상자만 — 옆 상자는 열쇠가 있어도 안 돼요|only the box on the ticket — never the one next to it, even with a key⟧", 12, "var(--ink)", cls="d"))

# 5. 문 목록표 — 잊힌 문이 없게
P5 = svg(300, sky(300)
         + board(60, 40, 300, 130, "⟦우리 성의 문 목록|OUR DOORS⟧", ("⟦창구 — 검토원 있음 ✓|counter — checker ✓⟧", "⟦심부름꾼 문 — 문지기 있음 ✓|runners\' door — doorkeeper ✓⟧", "⟦옛 뒷문 — 막았어요 ✓|old back door — boarded ✓⟧"))
         + label(210, 198, "⟦문이 몇 개인지 다 적어둬요|every door, written down⟧", 11, "var(--muted)")
         + person(400, 80, s=0.85, face=SMILE, **GUARD) + label(430, 208, "⟦문지기|doorkeeper⟧", 11, "var(--muted)")
         + door(520, 190, boarded=True) + label(550, 212, "⟦옛 문은 막았어요|old door boarded⟧", 10, "var(--good)")
         + person(640, 100, s=0.75, face=FROWN + MASK) + label(672, 212, "⟦들어갈 문이 없어요|no door to slip through⟧", 10, "var(--bad)")
         + label(380, 258, "⟦모든 문에 이름표와 문지기가 있으면 도둑은 뒷문을 못 찾아요|when every door has a name and a keeper, the thief finds no back way in⟧", 12, "var(--ink)", cls="d")
         + label(380, 284, "⟦잊힌 문이 없는지 바깥에서도 세어 봐요|count the doors from outside too, so none is forgotten⟧", 11, "var(--muted)"))

TICKET_I = icon('<rect x="8" y="20" width="48" height="24" rx="5" fill="var(--accent)"/><circle cx="8" cy="32" r="5" fill="var(--panel)"/><circle cx="56" cy="32" r="5" fill="var(--panel)"/><path d="M20 32 h24" stroke="#FFF" stroke-width="3" stroke-dasharray="4 3"/>')
OWNBOX_I = icon('<rect x="8" y="26" width="22" height="20" rx="3" fill="#8B5E3C"/><rect x="34" y="26" width="22" height="20" rx="3" fill="#8B5E3C" opacity="0.4"/><path d="M13 36 l5 5 l8 -10" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M40 31 l10 10 M50 31 l-10 10" stroke="var(--bad)" stroke-width="3"/>')
COUNT_I = icon('<circle cx="32" cy="34" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 20 v14 l9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><rect x="26" y="6" width="12" height="6" rx="2" fill="var(--stone-dark)"/><circle cx="50" cy="16" r="7" fill="var(--bad)"/>')
DOORS_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 18 a4 4 0 0 1 8 0 v6 h-8z" fill="#8B5E3C"/>')

PAGE = {
    "slug": "apisec", "order": 89,
    "title": ("창구 뒷문으로 오는 심부름꾼", "The Runner at the Back Door"),
    "h1": ("<em>API 보안</em>이 뭐예요?", "What is <em>API Security</em>?"),
    "sub": ("API 보안(API Security)을 창구 뒤 심부름꾼 전용 작은 문에 문지기를 세우는 이야기로 풀어봤어요.",
            "API security, told as a story about putting a doorkeeper on the small door behind the counter that only runners use."),
    "panels": [
        {"svg": P1, "alt": ("성벽 앞. 왼쪽 창구에서 손님이 '빵 한 개 주세요'. 오른쪽엔 작은 아치문이 있고 다른 성의 심부름꾼이 상자를 들고 '빵집 성에서 왔어요, 밀가루 주세요'", "A castle wall. At the counter on the left a visitor asks for a loaf. On the right is a small arched door, where a runner from another castle holds a box and asks for flour"),
         "caption": ("창구 뒤엔 심부름꾼만 쓰는 작은 문이 있어요.", "Behind the counter is a small door that only runners use."),
         "small": ("손님은 창구로 와요. 하지만 다른 성의 심부름꾼은 창구 대신 작은 문으로 와서 물건을 받아가요. 이 작은 문이 심부름꾼 문이에요.", "Visitors come to the counter. But runners from other castles skip the counter and pick things up at the small door. That small door is the runners\' door.")},
        {"svg": P2, "alt": ("문지기 없는 작은 문 셋: 도둑이 명부를 통째로 들고 나가고, 다른 도둑은 쾅쾅 하루 만 번 두드리고, 거미줄 낀 옛 문은 아무도 기억 못 함", "Three small doors with no doorkeeper: a thief walks out with the whole roster, another bangs ten thousand times a day, and a cobwebbed old door nobody remembers"),
         "caption": ("그 문에 문지기가 없으면 곤란해요.", "Trouble starts when that door has no doorkeeper."),
         "small": ('도둑이 명부를 통째로 가져가고, 하루 만 번 두드려도 아무도 안 세요. <a href="asm-ko.html">잊힌 옛 문</a>은 있는지도 몰라요. 창구엔 <a href="waf-ko.html">검토원</a>이 있지만 뒷문엔 아무도 없어요.',
                   'A thief takes the whole roster, and nobody counts the ten thousand knocks. A <a href="asm-en.html">forgotten old door</a>? Nobody even remembers it. The counter has a <a href="waf-en.html">checker</a> — the back door has no one.')},
        {"svg": P3, "hero": True, "alt": ("성벽의 작은 문 앞에 초록 문지기. 심부름꾼이 주황 입장권을 내밈. 오른쪽 판자에 뒷문 문지기 규칙 넷: 입장권을 봐요, 자기 상자만 열게 해요, 두드리는 횟수를 세요, 문 목록표를 적어요", "A green doorkeeper at the small door in the wall. The runner holds out an orange ticket. A board on the right lists four back-door rules: check the ticket, open only their own box, count the knocks, keep a list of doors"),
         "caption": ("API 보안은 심부름꾼 문에 문지기를 세우는 거예요.", "API security is putting a doorkeeper on the runners\' door."),
         "small": ("창구만큼 꼼꼼하게요. 입장권을 보고, 자기 상자만 열게 하고, 두드리는 횟수를 세고, 문이 몇 개인지 적어둬요.", "As careful as the counter. Check the ticket, let them open only their own box, count the knocks, and write down every door."),
         "tricks": (4, [
             (TICKET_I, ("입장권 확인", "Check the ticket"), ("누구인지, 뭘 해도 되는지", "who they are, what they may do")),
             (OWNBOX_I, ("자기 상자만", "Only their own box"), ("옆 상자는 안 돼요", "never the one next to it"), "warm"),
             (COUNT_I, ("횟수 세기", "Count the knocks"), ("천 번이면 잠깐 쉬어요", "at a thousand, a break"), "calm"),
             (DOORS_I, ("문 목록표", "A list of doors"), ("잊힌 문이 없게", "so none is forgotten")),
         ])},
        {"svg": P4, "alt": ("심부름꾼이 '7번 상자요! 8번도요' 하고, 문지기가 '7번은 돼요, 8번은 안 돼요'. 선반의 상자 6·7·8·9 중 7에 초록 체크, 8에 빨간 X. 입장권엔 '빵집 성, 7번 상자만'. 오늘 두드린 횟수 998", "The runner asks for box 7 and box 8; the doorkeeper says 7 yes, 8 no. On the shelf, boxes 6 to 9 — a green check on 7, a red X on 8. The ticket reads bakery castle, box 7 only. Knocks today: 998"),
         "caption": ("입장권에 적힌 상자만 열 수 있어요. 옆 상자는 안 돼요.", "Only the box on the ticket opens. Not the one next to it."),
         "small": ('<a href="oauth-ko.html">입장권</a>이 있어도 옆 상자까지 열게 두면 안 돼요. 문지기는 두드린 횟수도 세요 — 천 번이 되면 잠깐 쉬라고 해요.',
                   'Even with an <a href="oauth-en.html">entry ticket</a>, the box next door must stay shut. The doorkeeper also counts the knocks — at a thousand, it\'s time for a break.')},
        {"svg": P5, "alt": ("우리 성의 문 목록 판자: 창구 검토원 있음, 심부름꾼 문 문지기 있음, 옛 뒷문 막았음. 문지기가 웃고, 옛 문엔 초록 판자가 X 로 박혀 있고, 도둑은 들어갈 문이 없어 찡그림", "A board listing our doors: counter with checker, runners\' door with doorkeeper, old back door boarded. The doorkeeper smiles, green planks cross the old door, and the thief frowns with no way in"),
         "caption": ("모든 문에 이름표와 문지기가 있으면 도둑은 뒷문을 못 찾아요.", "When every door has a name and a keeper, the thief finds no back way in."),
         "small": ('잊힌 문이 없는지 <a href="asm-ko.html">바깥에서도 세어 봐요</a>. 심부름꾼 문의 입장권은 <a href="oauth-ko.html">열쇠 대신 입장권</a>, 창구의 검토원은 <a href="waf-ko.html">쪽지 검토원</a> 이야기에 있어요.',
                   'Also <a href="asm-en.html">count the doors from outside</a>, so none is forgotten. The runners\' ticket is the <a href="oauth-en.html">ticket instead of a key</a> story; the counter\'s checker is the <a href="waf-en.html">note checker</a> story.')},
    ],
    "summary": (("<b>API 보안</b> = 창구 뒤 <b>심부름꾼 전용 작은 문</b>에도 문지기를 세워, <b>입장권을 보고, 자기 상자만 열게 하고, 두드리는 횟수를 세고, 문 목록표</b>를 적는 일.",
                 "<b>API security</b> = put a doorkeeper on the <b>small runners\' door behind the counter</b> too — one who <b>checks the ticket, opens only their own box, counts the knocks, and keeps a list of doors</b>."),
                ("API Security. 화면 뒤에서 프로그램끼리 데이터를 주고받는 통로(API)를 지키는 일이에요. 인증·인가, 객체 수준 권한(BOLA), 레이트 리밋, API 인벤토리가 핵심이고, OWASP API Top 10 이 대표적인 점검 목록이에요.",
                 "Protecting the channels (APIs) that programs use to exchange data behind the screen. Authentication and authorization, object-level permissions (BOLA), rate limiting, and an API inventory are the core, and the OWASP API Top 10 is the standard checklist.")),
    "glossary": [
        ("API", "API", ("심부름꾼 문.", "The runners\' door."), ("사람이 쓰는 창구가 아니라, 프로그램끼리 물건을 주고받는 작은 문이에요.", "Not the counter people use — the small door where programs hand things to each other.")),
        ("인증 · 인가", "Authentication · authorization", ("누구인지 · 뭘 해도 되는지.", "Who you are · what you may do."), ('입장권에 둘 다 적혀 있어요. → <a href="oauth-ko.html">열쇠 대신 입장권</a>', 'Both are written on the ticket. → <a href="oauth-en.html">a ticket instead of a key</a>')),
        ("BOLA", "BOLA", ("옆 상자 열기.", "Opening the box next door."), ("입장권은 진짜인데 7번 손님이 8번 상자까지 열어요. 뒷문에서 제일 흔한 실수예요.", "The ticket is real, but visitor 7 opens box 8 too. The most common back-door mistake.")),
        ("레이트 리밋", "Rate limiting", ("두드리는 횟수 세기.", "Counting the knocks."), ('천 번이면 잠깐 쉬게 해요. 가짜 손님 떼도 막아요. → <a href="ddos-ko.html">성문 앞 가짜 손님 떼</a>', 'At a thousand, a break. It also holds off a fake crowd. → <a href="ddos-en.html">the fake crowd at the gate</a>')),
        ("API 게이트웨이", "API gateway", ("문지기가 서는 자리.", "Where the doorkeeper stands."), ("심부름꾼 문을 하나로 모아, 입장권 확인과 횟수 세기를 한 곳에서 해요.", "Gathers the runners\' doors in one place, so tickets and knock counts are handled together.")),
        ("API 키", "API key", ("심부름꾼의 열쇠.", "The runner\'s key."), ('잃어버리면 아무나 심부름꾼이 돼요. 종이에 적어 두지 말고 금고에 넣어요. → <a href="secrets-ko.html">비밀 열쇠 보관</a>', 'Lose it, and anyone becomes a runner. Never write it on a note; keep it in the vault. → <a href="secrets-en.html">keeping secret keys</a>')),
        ("OWASP API Top 10", "OWASP API Top 10", ("뒷문 실수 열 가지.", "Ten back-door mistakes."), ("옆 상자 열기가 1번이에요. 문지기가 외우는 목록이에요.", "Opening the box next door is number one. The list the doorkeeper memorizes.")),
        ("섀도 API", "Shadow API", ("잊힌 옛 문.", "The forgotten old door."), ('아무도 기억 못 하는데 열려 있어요. → <a href="asm-ko.html">바깥에서 세는 우리 성의 문</a>', 'Nobody remembers it, but it\'s open. → <a href="asm-en.html">counting our doors from outside</a>')),
    ],
}
