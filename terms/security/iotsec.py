from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
KEEPER = dict(hat="var(--stone-dark)", shirt="#4A5A72")
CARPENTER = dict(hat="#E9B44C", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def pump(x, y, s=1.0, dry=False):
    """우물 펌프. 바닥 중심 (x,y)."""
    water = "" if dry else '<path d="M30 -30 q6 10 0 18 q-6 -8 0 -18z" fill="#5B9BD5"/><path d="M34 -10 q4 7 0 12 q-4 -5 0 -12z" fill="#5B9BD5"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-40" width="80" height="40" rx="3" fill="var(--stone)"/><path d="M-46 -40 h92" stroke="var(--stone-dark)" stroke-width="6"/>'
            f'<rect x="-8" y="-100" width="16" height="60" rx="4" fill="var(--stone-dark)"/><path d="M-8 -90 h-28 l-10 -14" stroke="var(--stone-dark)" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M8 -60 h20 v14" stroke="var(--stone-dark)" stroke-width="7" fill="none" stroke-linecap="round"/>{water}</g>')


def pulley(x, y, s=1.0):
    """성문 도르래. 바닥 중심 (x,y)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="-60" width="100" height="60" fill="var(--stone-dark)"/><path d="M-20 0 V-30 a20 20 0 0 1 40 0 V0 Z" fill="var(--night)"/>'
            f'<rect x="-4" y="-120" width="8" height="60" fill="{WOOD}"/><circle cy="-118" r="16" fill="{WOOD}" stroke="#5A3B22" stroke-width="4"/><circle cy="-118" r="4" fill="#5A3B22"/>'
            f'<path d="M-16 -118 v66 M16 -118 v40" stroke="#5A3B22" stroke-width="3"/></g>')


def thermo(x, y, s=1.0):
    """온도계. 바닥 중심 (x,y)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-130" width="28" height="112" rx="14" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>'
            f'<circle cy="-16" r="20" fill="var(--bad)" stroke="var(--stone-dark)" stroke-width="4"/><rect x="-6" y="-80" width="12" height="60" fill="var(--bad)"/>'
            f'<path d="M14 -110 h8 M14 -90 h8 M14 -70 h8 M14 -50 h8" stroke="var(--stone-dark)" stroke-width="3"/></g>')


def tag(x, y, text, s=1.0, crossed=False, color="#142033"):
    cr = '<path d="M-30 -12 l60 24 M30 -12 l-60 24" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>' if crossed else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-34 -14 h56 l12 14 l-12 14 h-56z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="26" r="3" fill="#C9A86A"/>'
            + label(-6, 4, text, 11, color, cls="d") + cr + "</g>")


def ribbon(x, top, bottom, color="var(--accent)"):
    return f'<rect x="{x - 5}" y="{top}" width="10" height="{bottom - top}" rx="3" fill="{color}"/><path d="M{x - 12} {top} l7 12 l7 -12z" fill="{color}"/>'


def board(x, y, w, h, title, rows):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


WAVES = '<path d="M{x} {y} q6 -8 12 0 q6 8 12 0 q6 -8 12 0" stroke="var(--muted)" stroke-width="2.5" fill="none" stroke-linecap="round"/>'


def waves(x, y):
    return WAVES.format(x=x, y=y) + WAVES.format(x=x + 8, y=y - 14) + WAVES.format(x=x + 16, y=y - 28)


# 1. 성엔 사람 말고도 기계가 많아요
P1 = svg(320, sky(320)
         + pump(110, 240, 1.0) + pulley(400, 240, 1.0) + thermo(650, 240, 1.0)
         + person(210, 130, s=0.75, face=EYES, **GUARD) + bubble(130, 30, 270, 34, "⟦다 기계예요 — 말은 못 해요|all machines — none of them talk⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(110, 268, "⟦우물 펌프|the well pump⟧", 12, "var(--ink)", cls="d") + label(400, 268, "⟦성문 도르래|the gate pulley⟧", 12, "var(--ink)", cls="d") + label(650, 268, "⟦온도계|the thermometer⟧", 12, "var(--ink)", cls="d")
         + label(380, 304, "⟦성엔 사람 말고도 일하는 기계가 많아요|the castle has many working machines, not just people⟧", 12, "var(--ink)"))

# 2. 사람 방식으로는 못 지켜요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + pump(90, 170, 0.7, dry=False) + dog(140, 176, 0.45) + label(125, 130, "?", 26, "var(--accent)", cls="d")
         + label(100, 225, "⟦경비견이 못 들어가요|the dog can\'t get in⟧", 12, "var(--ink)", cls="d") + label(100, 247, "⟦기계는 개를 모르거든요|the machine doesn\'t know dogs⟧", 10, "var(--bad)")
         + pulley(290, 170, 0.6) + tag(290, 120, "⟦admin / admin|admin / admin⟧", 0.9)
         + label(290, 225, "⟦암호말이 공장 그대로|the factory password⟧", 12, "var(--ink)", cls="d") + label(290, 247, "⟦도둑도 다 알아요|every thief knows it⟧", 10, "var(--bad)")
         + person(440, 70, s=0.7, face=FROWN, **CARPENTER) + '<g transform="translate(500,120) rotate(-30)"><rect x="-8" y="-40" width="16" height="80" rx="3" fill="#8B5E3C"/></g><path d="M486 100 l30 30 M516 100 l-30 30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(480, 225, "⟦판자를 대기 어려워요|hard to board up⟧", 12, "var(--ink)", cls="d") + label(480, 247, "⟦너무 낡았거나, 멈출 수 없어요|too old, or can\'t be stopped⟧", 10, "var(--bad)")
         + pump(660, 170, 0.7, dry=True) + '<path d="M630 90 l60 60 M690 90 l-60 60" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + label(660, 225, "⟦한 번 멈추면|if it stops once⟧", 12, "var(--ink)", cls="d") + label(660, 247, "⟦온 성이 목말라요|the whole castle goes thirsty⟧", 10, "var(--bad)")
         + label(380, 285, "⟦사람 방식으로는 못 지켜요 — 기계는 다르게 지켜야 해요|you can\'t guard them like people — machines need their own way⟧", 11, "var(--muted)"))

# 3. 기계 복도를 따로 두고, 파수꾼이 대신 봐요 (hero)
DOORS = (("⟦식당|hall⟧", False), ("⟦침실|bedroom⟧", False), ("⟦우물|well⟧", False), ("⟦성문|gate⟧", False), ("⟦온도계|thermo⟧", False))
P3 = svg(360, corridor(360, DOORS, marks=False)
         + dog(150, 176, 0.45) + pump(382, 188, 0.55) + pulley(522, 188, 0.5) + thermo(662, 188, 0.55)
         + ribbon(312, 40, 360) + label(312, 32, "⟦여기부터 기계 복도|machine hall from here⟧", 12, "var(--accent)", cls="d")
         + person(220, 200, s=0.85, face=EYES, **GUARD) + label(250, 322, "⟦복도 파수꾼|the hall watcher⟧", 11, "var(--muted)")
         + '<path d="M290 236 l70 -20 M290 236 l70 20" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 4" opacity="0.8"/>'
         + board(540, 205, 190, 100, "⟦기계 목록표|MACHINE LIST⟧", ("⟦우물 펌프 — 새 암호말 ✓|pump — new password ✓⟧", "⟦성문 도르래 — 아주 오래됨|pulley — very old⟧", "⟦온도계 — 창가|thermo — by the window⟧"))
         + label(380, 344, "⟦기계 복도를 따로 두고, 파수꾼이 복도에서 대신 봐요|give the machines their own hall, and let the watcher watch for them⟧", 13, "var(--ink)", cls="d"))

# 4. 파수꾼은 기계를 건드리지 않고 복도에서 듣기만 해요
P4 = svg(320, sky(320)
         + ribbon(170, 40, 270) + person(70, 110, s=0.8, face=MASK, extra=BAG) + '<path d="M150 150 l30 30 M180 150 l-30 30" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + label(95, 236, "⟦리본 너머론 못 가요|can\'t cross the ribbon⟧", 11, "var(--ink)", cls="d")
         + pump(300, 220, 0.8) + waves(340, 150) + person(420, 110, s=0.85, face=EYES, **GUARD) + bell(540, 100, 0.8)
         + label(300, 236, "⟦기계는 건드리지 않아요|never touches the machine⟧", 11, "var(--ink)", cls="d") + label(470, 236, "⟦복도에서 듣기만 해요|only listens from the hall⟧", 11, "var(--ink)", cls="d") + label(470, 256, "⟦이상한 말을 하면 종을 쳐요|strange talk? ring the bell⟧", 10, "var(--muted)")
         + tag(670, 100, "⟦admin / admin|admin / admin⟧", 0.9, crossed=True) + tag(670, 160, "⟦★★★★★★|★★★★★★⟧", 0.9) + label(670, 236, "⟦공장 암호말은 바꿔요|change the factory password⟧", 11, "var(--ink)", cls="d")
         + label(380, 302, "⟦기계가 이상한 말을 하면 파수꾼이 종을 쳐요 — 기계를 멈추지 않고요|when a machine talks strangely, the watcher rings the bell — without stopping the machine⟧", 12, "var(--ink)", cls="d"))

# 5. 우물은 계속 돌고, 도둑은 못 닿아요
P5 = svg(300, sky(300)
         + pump(90, 220, 0.8) + person(150, 120, s=0.75, face=SMILE, **KEEPER) + label(120, 250, "⟦우물은 계속 돌아요|the well keeps running⟧", 11, "var(--ink)", cls="d")
         + ribbon(300, 40, 240) + person(330, 110, s=0.8, face=SMILE, **GUARD) + label(360, 250, "⟦파수꾼이 대신 봐요|the watcher watches for them⟧", 11, "var(--ink)", cls="d")
         + board(470, 60, 170, 100, "⟦기계 목록표|MACHINE LIST⟧", ("⟦우물 펌프 ✓|well pump ✓⟧", "⟦성문 도르래 ✓|gate pulley ✓⟧", "⟦온도계 ✓|thermometer ✓⟧")) + person(660, 100, s=0.75, face=SMILE, **KING)
         + label(600, 250, "⟦빠진 기계가 없어요|no machine left out⟧", 11, "var(--ink)", cls="d")
         + label(380, 282, "⟦사람 성엔 경비견, 기계 성엔 리본과 파수꾼 — 기계는 멈추지 않게, 도둑은 닿지 않게|dogs for the people\'s halls, a ribbon and a watcher for the machines\' — never stopped, never reached⟧", 11, "var(--muted)"))

RIBBON_I = icon('<rect x="8" y="14" width="20" height="36" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><rect x="36" y="14" width="20" height="36" rx="3" fill="var(--stone)" stroke="var(--line)" stroke-width="2"/><rect x="29" y="8" width="6" height="48" rx="2" fill="var(--accent)"/>')
LISTEN_I = icon('<path d="M20 24 q-10 8 0 16 M14 18 q-16 14 0 28" stroke="var(--muted)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="40" cy="22" r="10" fill="#E8C9A8"/><path d="M28 16 q12 -12 24 0z" fill="var(--good)"/><rect x="32" y="32" width="16" height="22" rx="4" fill="var(--good)"/>')
LIST_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 40 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
PASS_I = icon('<path d="M8 20 h34 l10 12 l-10 12 h-34z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M14 26 l22 12 M36 26 l-22 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><path d="M40 44 l6 -6 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "iotsec", "order": 91,
    "title": ("말 못 하는 성 안 기계들", "The Machines That Cannot Talk"),
    "h1": ("<em>IoT · OT 보안</em>이 뭐예요?", "What is <em>IoT / OT Security</em>?"),
    "sub": ("IoT·OT 보안(IoT / OT Security)을 성 안에서 말없이 일하는 기계들 — 우물 펌프, 성문 도르래, 온도계 — 를 지키는 이야기로 풀어봤어요.",
            "IoT and OT security, told as a story about guarding the castle\'s silent working machines — the well pump, the gate pulley, and the thermometer."),
    "panels": [
        {"svg": P1, "alt": ("성 마당에 우물 펌프, 도르래 달린 성문, 큰 온도계가 나란히. 초록 경비가 '다 기계예요, 말은 못 해요'", "In the castle yard stand a well pump, a gate with a pulley, and a tall thermometer. A green guard says: all machines, none of them talk"),
         "caption": ("성엔 사람 말고도 일하는 기계가 많아요.", "The castle has many working machines, not just people."),
         "small": ("우물 펌프, 성문 도르래, 온도계. 밤낮없이 일하지만 말은 못 해요. 누가 만졌는지, 아픈지, 스스로 말하지 못해요.", "The well pump, the gate pulley, the thermometer. They work day and night, but they cannot talk. Who touched them, whether something is wrong — they cannot say.")},
        {"svg": P2, "alt": ("넷: 펌프 옆에서 물음표 띄운 경비견, 도르래에 걸린 admin/admin 이름표, 판자를 든 목수 앞의 빨간 X, 물이 마른 펌프 위의 큰 X", "Four scenes: a guard dog with a question mark beside the pump, an admin/admin tag hanging on the pulley, a red X in front of the carpenter holding a plank, and a big X over a dry pump"),
         "caption": ("사람 방식으로는 못 지켜요.", "You can\'t guard them the way you guard people."),
         "small": ('<a href="edr-ko.html">경비견</a>은 기계 안에 못 들어가요. 암호말은 공장에서 붙인 그대로예요. <a href="patch-ko.html">목수의 판자</a>도 대기 어렵고, 한 번 멈추면 온 성이 목말라요.',
                   'The <a href="edr-en.html">guard dog</a> can\'t get inside a machine. The password is still the one from the factory. The <a href="patch-en.html">carpenter\'s plank</a> won\'t fit, and if it stops once, the whole castle goes thirsty.')},
        {"svg": P3, "hero": True, "alt": ("복도. 왼쪽 두 문(식당, 침실)엔 경비견이 있고, 주황 리본부터 오른쪽 세 문엔 펌프, 도르래, 온도계. 초록 파수꾼이 리본 앞에 서서 기계 쪽을 봄. 오른쪽 아래 기계 목록표", "A corridor. The two doors on the left (hall, bedroom) have a guard dog; past an orange ribbon, the three doors on the right hold the pump, the pulley, and the thermometer. A green watcher stands at the ribbon looking toward the machines. A machine list at the bottom right"),
         "caption": ("IoT·OT 보안은 기계 복도를 따로 두고, 파수꾼이 대신 봐 주는 거예요.", "IoT and OT security is giving the machines their own hall, with a watcher who watches for them."),
         "small": ("기계들은 리본 너머 자기 복도에 두어요. 기계는 스스로 말을 못 하니 복도 파수꾼이 대신 지켜봐요. 그리고 어떤 기계가 있는지 목록표에 다 적어요.", "The machines live in their own hall past the ribbon. Since they cannot speak for themselves, the hall watcher watches for them. And every machine goes on the list."),
         "tricks": (4, [
             (RIBBON_I, ("기계 복도 따로", "Their own hall"), ("리본으로 사람 복도와 나눠요", "a ribbon splits it from the people\'s"), "calm"),
             (LISTEN_I, ("파수꾼이 대신", "The watcher watches"), ("기계는 안 건드리고 듣기만", "listening, never touching")),
             (LIST_I, ("기계 목록표", "A machine list"), ("빠진 기계가 없게", "so none is left out")),
             (PASS_I, ("공장 암호말 바꾸기", "New password"), ("admin/admin 은 안 돼요", "admin/admin won\'t do"), "warm"),
         ])},
        {"svg": P4, "alt": ("도둑이 주황 리본 앞에서 막힘. 펌프에서 나오는 물결 소리를 파수꾼이 복도에서 듣고, 종이 울림. 오른쪽엔 X 친 admin/admin 이름표와 별 여섯 개짜리 새 이름표", "A thief blocked at the orange ribbon. Sound waves come from the pump; the watcher listens from the hall, and a bell rings. On the right, a crossed-out admin/admin tag and a new tag with six stars"),
         "caption": ("파수꾼은 기계를 건드리지 않아요. 복도에서 듣기만 해요.", "The watcher never touches the machine. It only listens from the hall."),
         "small": ('기계가 갑자기 이상한 말을 하면 <a href="ndr-ko.html">복도 파수꾼</a>이 종을 쳐요 — 기계를 멈추지 않고요. 도둑은 <a href="vlan-ko.html">리본</a> 너머로 못 가고, 공장 암호말은 새것으로 바꿔요.',
                   'If a machine suddenly starts talking strangely, the <a href="ndr-en.html">hall watcher</a> rings the bell — without stopping the machine. The thief can\'t cross the <a href="vlan-en.html">ribbon</a>, and the factory password gets replaced.')},
        {"svg": P5, "alt": ("펌프 옆에서 우물지기가 웃고, 리본 앞에 파수꾼, 오른쪽엔 세 기계에 체크가 찍힌 목록표와 웃는 왕", "The well keeper smiles beside the running pump, the watcher stands at the ribbon, and on the right the king smiles at a list with all three machines checked"),
         "caption": ("우물은 계속 돌고, 도둑은 닿지 못해요.", "The well keeps running, and the thief never reaches it."),
         "small": ('기계는 멈추면 안 되니까 순서가 달라요 — 먼저 리본으로 나누고, 파수꾼이 듣고, 판자는 쉬는 날에 대요. 어떤 기계가 있는지는 <a href="asm-ko.html">바깥에서도 세어 봐요</a>.',
                   'Because a machine must never stop, the order is different — first the ribbon, then the watcher, and planks only on a rest day. Which machines you have, <a href="asm-en.html">count from outside too</a>.')},
    ],
    "summary": (("<b>IoT·OT 보안</b> = 말 못 하는 성 안 기계들을 <b>리본 너머 자기 복도</b>에 두고, <b>파수꾼이 대신 듣고</b>, <b>목록표</b>에 다 적고, <b>공장 암호말을 바꾸는</b> 일. 기계는 멈추지 않게, 도둑은 닿지 않게.",
                 "<b>IoT / OT security</b> = keep the castle\'s silent machines in <b>their own hall past the ribbon</b>, let <b>the watcher listen for them</b>, put them all on <b>the list</b>, and <b>change the factory password</b>. Never stopped, never reached."),
                ("IoT / OT Security. 센서·카메라·공장 설비처럼 에이전트를 설치할 수 없고 패치가 어려운 장비를 지키는 일이에요. 네트워크 분리, 패시브 모니터링, 자산 인벤토리, 기본 비밀번호 변경이 핵심이고, 가용성과 안전(safety)이 늘 먼저예요.",
                 "Protecting sensors, cameras, and industrial equipment that can\'t run an agent and are hard to patch. Network segmentation, passive monitoring, an asset inventory, and changing default passwords are the core — and availability and safety always come first.")),
    "glossary": [
        ("IoT", "IoT", ("말 못 하는 작은 기계들.", "The small silent machines."), ("온도계, 카메라, 문 센서. 마을과 이어져 있지만 경비견은 못 들어가요.", "Thermometers, cameras, door sensors. Connected to the village, but no room for a guard dog.")),
        ("OT · ICS", "OT · ICS", ("성을 돌리는 큰 기계.", "The big machines that run the castle."), ("우물 펌프, 성문 도르래. 공장과 발전소의 설비예요. 멈추면 성이 멈춰요.", "The well pump, the gate pulley. Factory and power-plant equipment. If it stops, the castle stops.")),
        ("기본 비밀번호", "Default password", ("공장 암호말.", "The factory password."), ('admin/admin 처럼 공장에서 붙인 그대로. 도둑 백과사전 첫 장에 적혀 있어요. → <a href="password-ko.html">암호말 이야기</a>', 'Like admin/admin, exactly as it left the factory. It\'s on the first page of every thief\'s book. → <a href="password-en.html">the password story</a>')),
        ("펌웨어 업데이트", "Firmware update", ("기계에 대는 판자.", "The plank for a machine."), ('낡아서 안 맞거나 멈출 수 없어 어려워요. 쉬는 날에 대요. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'Hard, because the machine is old or can\'t be stopped. Done on a rest day. → <a href="patch-en.html">the plank the carpenter sent</a>')),
        ("네트워크 분리", "Network segmentation", ("리본으로 나눈 기계 복도.", "The machine hall behind the ribbon."), ('사람 복도에서 기계 복도로 못 넘어가요. → <a href="vlan-ko.html">색 리본으로 나눈 복도</a>', 'No crossing from the people\'s hall into the machines\'. → <a href="vlan-en.html">a corridor split by colored ribbons</a>')),
        ("패시브 모니터링", "Passive monitoring", ("건드리지 않고 듣기.", "Listening without touching."), ('파수꾼이 복도에서 기계 소리만 들어요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'The watcher only listens to the machines from the hall. → <a href="ndr-en.html">the one who guards the corridor</a>')),
        ("레거시", "Legacy", ("아주 오래된 도르래.", "The very old pulley."), ('만든 대장간이 없어져서 판자가 없어요. 그래서 리본이 먼저예요. → <a href="asm-ko.html">기계 세어 보기</a>', 'The smithy that made it is gone, so no plank exists. That\'s why the ribbon comes first. → <a href="asm-en.html">counting the machines</a>')),
        ("안전 vs 보안", "Safety vs security", ("멈추지 않는 게 먼저.", "Not stopping comes first."), ("사람 성에선 잠그는 게 먼저지만, 기계 성에선 우물이 도는 게 먼저예요. 그래서 밖에서 지켜요.", "In the people\'s castle, locking comes first; in the machines\', the well running comes first. So you guard from outside.")),
    ],
}
