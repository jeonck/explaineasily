from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
ESCORT = dict(hat="var(--good)", shirt="var(--good)")
LANTERN = ('<g transform="translate(66,66)"><rect x="-2" y="-20" width="4" height="14" fill="var(--night)"/><rect x="-10" y="-6" width="20" height="26" rx="4" fill="#FFD166" stroke="var(--night)" stroke-width="2"/>'
           '<circle cy="7" r="5" fill="var(--accent)"/></g>')


def house(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-50 0 L0 -36 L50 0 Z" fill="var(--bad)"/><rect x="-10" y="26" width="20" height="34" fill="{WOOD}"/>{label(0, 80, "⟦집|home⟧", 12, "var(--muted)")}</g>')


def wall(x, y, w, h, door=True):
    d = f'<path d="M{x + w / 2 - 22} {y + h} V{y + h - 44} a22 22 0 0 1 44 0 V{y + h} Z" fill="var(--night)"/>' if door else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="var(--stone-dark)"/>{battlements(x, y - 18, w, max(3, int(w / 40)), "var(--stone-dark)", 20)}{d}'


def door(x, y, name, s=1.0, extra="", faint=False):
    fill = "var(--stone)" if faint else WOOD
    ink = "var(--stone)" if faint else "var(--ink)"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" width="60" height="100" rx="3" fill="{fill}"/><circle cx="20" cy="54" r="4" fill="{"var(--stone-dark)" if faint else "#E9B44C"}"/>'
            f'{label(0, -8, name, 13, ink)}{extra}</g>')


def tunnel(x1, x2, y, depth=70, color="#3A2A1E"):
    return f'<path d="M{x1} {y} C{x1} {y + depth} {x2} {y + depth} {x2} {y}" stroke="{color}" stroke-width="22" fill="none" stroke-linecap="round"/>'


GROUND = lambda h: f'<rect y="{h - 90}" width="760" height="90" fill="#5A4636"/><rect y="{h - 92}" width="760" height="6" fill="var(--good-soft)"/>'

# 1. 옛날엔 땅굴을 팠다
P1 = svg(300, sky(300, ground=False) + GROUND(300) + house(90, 120) + wall(420, 100, 320, 110, door=False)
         + tunnel(90, 470, 208) + label(280, 285, "⟦땅굴(VPN)|the tunnel (VPN)⟧", 13, "#F5E6B8")
         + person(455, 20, s=0.7, **ME)
         + '<path d="M500 90 C560 60 600 110 690 80" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + "".join(door(x, 40, n, 0.5) for x, n in ((560, "⟦부엌|Kitchen⟧"), (630, "⟦금고|Vault⟧"), (700, "⟦서재|Study⟧")))
         + label(580, 260, "⟦나오면 성 안, 그다음엔 어디든|out of the tunnel and you\'re in — anywhere you like⟧", 12, "#F5E6B8"))

# 2. 땅굴 입구는 누구나 찾는다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + '<path d="M60 200 a70 70 0 0 1 140 0 Z" fill="#3A2A1E"/><rect x="60" y="200" width="140" height="30" fill="#3A2A1E"/>'
         + label(130, 250, "⟦땅굴 입구|tunnel mouth⟧", 12, "var(--muted)")
         + person(100, 100, s=0.8, face=MASK) + bubble(60, 30, 150, 34, "⟦여기 있네|there it is⟧", 13, "var(--panel)", "var(--bad)", "bottom")
         + '<path d="M210 215 L300 215" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8"/><path d="M290 205 L302 215 L290 225" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + "".join(door(x, 70, n, 0.9, extra=label(0, 128, "⟦열림|open⟧", 12, "var(--bad)")) for x, n in ((360, "⟦부엌|Kitchen⟧"), (470, "⟦금고|Vault⟧"), (580, "⟦서재|Study⟧"), (690, "⟦창고|Storage⟧")))
         + label(525, 250, "⟦땅굴 하나면 성 전체가 열려요|one tunnel opens the whole castle⟧", 13, "var(--bad)"))

# 3. ZTNA = 안내인이 방 하나까지만 (hero)
CHECKLIST = ('<g transform="translate(300,40)"><rect width="150" height="70" rx="8" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/>'
             + label(16, 24, "⟦누구세요? ✓|Who are you? ✓⟧", 12, "var(--ink)", "start") + label(16, 42, "⟦반지는? ✓|Your ring? ✓⟧", 12, "var(--ink)", "start")
             + label(16, 60, "⟦신발에 진흙? ✓|Mud on shoes? ✓⟧", 12, "var(--ink)", "start") + "</g>")
P3 = svg(340, sky(340) + house(70, 130, 0.9)
         + person(150, 160, s=0.8, **ME)
         + person(300, 130, s=0.85, face=SMILE, **ESCORT, extra=LANTERN) + label(325, 260, "⟦안내인|the escort⟧", 13, "var(--ink)", cls="d") + CHECKLIST
         + '<path d="M380 230 C450 230 470 190 540 180" stroke="var(--accent)" stroke-width="4" stroke-dasharray="8 6" fill="none"/>'
         + wall(520, 60, 240, 110, door=False) + label(640, 45, "⟦문이 안 보여요|no gate to knock on⟧", 12, "var(--muted)")
         + door(560, 190, "⟦회의실|Meeting⟧", 0.8, extra='<path d="M-12 50 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
         + door(650, 190, "", 0.8, faint=True) + door(720, 190, "", 0.8, faint=True)
         + label(685, 300, "⟦다른 방은 보이지도 않아요|other rooms aren\'t even visible⟧", 11, "var(--muted)")
         + label(380, 325, "⟦성에 들어가는 게 아니라, 딱 그 방 문 앞까지만|not into the castle — just to that one door⟧", 14, "var(--muted)"))

# 4. 방마다 따로, 매번 다시
P4 = svg(280, '<rect width="380" height="280" fill="var(--good-soft)"/><rect x="380" width="380" height="280" fill="var(--bad-soft)"/>'
         + person(40, 90, s=0.8, **ME) + person(130, 80, s=0.8, face=SMILE, **ESCORT, extra=LANTERN)
         + door(280, 60, "⟦회의실|Meeting⟧", 0.9, extra='<path d="M-12 50 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
         + label(190, 250, "⟦회의실은 목록에 있어요|Meeting is on the list⟧", 13, "var(--good)")
         + person(420, 90, s=0.8, **ME) + person(510, 80, s=0.8, face=EYES, **ESCORT, extra=LANTERN)
         + bubble(470, 14, 190, 34, "⟦그 방은 목록에 없어요|that room isn\'t on your list⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + door(660, 60, "⟦금고|Vault⟧", 0.9, extra='<path d="M-12 -12 l24 24 M12 -12 l-24 24" stroke="var(--bad)" stroke-width="5" stroke-linecap="round" transform="translate(0,54)"/>')
         + label(570, 250, "⟦내일 와도 처음부터 다시 물어요|tomorrow it all gets asked again⟧", 13, "var(--muted)"))

# 5. 안내인이 모르는 방은 못 간다
P5 = svg(300, sky(300, ground=False) + GROUND(300)
         + person(80, 120, s=0.8, face=FROWN, **ESCORT, extra=LANTERN)
         + bubble(40, 40, 200, 34, "⟦그 창고는 제 목록에 없는데요|that shed isn\'t on my list⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + '<g transform="translate(560,110)"><rect x="-50" y="0" width="100" height="90" fill="var(--stone)"/><path d="M-60 0 L0 -40 L60 0 Z" fill="var(--stone-dark)"/><rect x="-12" y="46" width="24" height="44" fill="var(--night)"/>'
         + label(0, -50, "⟦오래된 창고|the old storehouse⟧", 13, "var(--ink)") + label(0, 40, "?", 30, "var(--accent)", cls="d") + "</g>"
         + tunnel(300, 560, 208, 60) + label(430, 285, "⟦여긴 아직 땅굴로 가요|this one still needs the tunnel⟧", 13, "#F5E6B8")
         + person(300, 120, s=0.7, **ME))

ESCORT_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><path d="M20 18 Q32 4 44 18 Z" fill="var(--good)"/><rect x="18" y="34" width="28" height="22" rx="8" fill="var(--good)"/><rect x="46" y="30" width="10" height="14" rx="2" fill="#FFD166"/>')
CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/><path d="M18 22 l4 4 l8 -8 M18 34 l4 4 l8 -8 M18 46 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
DOOR_I = icon(f'<rect x="20" y="8" width="24" height="48" rx="2" fill="{WOOD}"/><circle cx="38" cy="34" r="3" fill="#E9B44C"/><path d="M8 32 H18 M14 27 l5 5 -5 5" stroke="var(--accent)" stroke-width="3" fill="none"/>')
INVIS_I = icon('<rect x="8" y="26" width="48" height="28" fill="var(--stone-dark)"/><rect x="8" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="18" width="10" height="10" fill="var(--stone-dark)"/>')

PAGE = {
    "slug": "ztna", "order": 24,
    "title": ("방 하나까지만 데려다주는 안내인", "The Escort to One Room"),
    "h1": ("<em>ZTNA</em>가 뭐예요?", "What is <em>ZTNA</em>?"),
    "sub": ("제로 트러스트 네트워크 접근(Zero Trust Network Access)을 방 하나까지만 데려다주는 안내인 이야기로 풀어봤어요.",
            "Zero Trust Network Access, told as a story about an escort who takes you to exactly one door."),
    "panels": [
        {"svg": P1, "alt": ("집에서 성 안마당까지 땅속으로 이어진 땅굴, 성 안에 들어온 사람이 부엌·금고·서재로 자유롭게 감", "An underground tunnel from home into the castle courtyard; once inside, the person wanders to Kitchen, Vault and Study"),
         "caption": ("옛날엔 집에서 성까지 땅굴을 팠어요.", "We used to dig a tunnel from home to the castle."),
         "small": ('땅굴(VPN)을 지나면 성 안이에요. 그다음엔 어디든 갈 수 있었어요 — <a href="zerotrust-ko.html">옛날 성</a>이랑 똑같이요.',
                   'Through the tunnel (VPN) and you\'re inside. After that, anywhere you like — just like the <a href="zerotrust-en.html">old castle</a>.')},
        {"svg": P2, "alt": ("땅굴 입구를 찾은 도둑 '여기 있네', 그 뒤로 부엌·금고·서재·창고가 전부 '열림'", "A thief finds the tunnel mouth — there it is — and behind it Kitchen, Vault, Study and Storage all read open"),
         "caption": ("땅굴 입구는 누구나 찾을 수 있어요.", "Anyone can find the tunnel mouth."),
         "small": ("땅굴 문은 밖에서 보이고, 자주 뚫려요. 도둑이 들어오면 성 전체가 열려요.", "The tunnel door is visible from outside and gets broken often. One thief inside, and the whole castle opens.")},
        {"svg": P3, "hero": True, "alt": ("집에서 온 사람을 등불 든 안내인이 '누구세요, 반지는, 신발에 진흙?' 확인한 뒤 점선 길로 회의실 문 앞까지만 데려감. 성벽엔 문이 없고 다른 방은 흐릿함", "An escort with a lantern checks the visitor (who are you, your ring, mud on shoes?) then leads them along a dotted path to the Meeting door only; the wall has no gate and the other doors are faded"),
         "caption": ("ZTNA는 안내인이 방 하나까지만 데려다줘요.", "ZTNA is an escort who takes you to one door only."),
         "small": ("성에 들어가는 게 아니라, 확인받은 뒤 딱 그 방 문 앞까지만 가요. 다른 방은 보이지도 않아요.", "You never enter the castle — once checked, you're walked to that one door. The other rooms aren't even visible."),
         "tricks": (4, [
             (ESCORT_I, ("안내인", "The escort"), ("길을 아는 단 한 사람", "the only one who knows the way"), "calm"),
             (CHECK_I, ("확인", "The check"), ("사람도, 들고 온 기기도", "the person and the device they brought"), "warm"),
             (DOOR_I, ("방 하나", "One door"), ("성이 아니라 문 앞까지", "to a door, not into the castle")),
             (INVIS_I, ("보이지 않는 성", "The invisible castle"), ("밖에서 두드릴 문이 없어요", "no gate to knock on from outside"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 안내인이 회의실 문까지 데려다주고 체크. 오른쪽: 금고를 원하자 '그 방은 목록에 없어요' X", "Left: the escort leads to the Meeting door, checked. Right: asking for the Vault gets 'that room isn't on your list', crossed out"),
         "caption": ("방마다 따로, 매번 다시 물어요.", "Each room separately, every time again."),
         "small": ("회의실 안내는 됐지만 금고는 목록에 없어요. 내일 오면 처음부터 다시 확인해요.", "Meeting was allowed; the Vault isn't on the list. Come back tomorrow and it's all asked again.")},
        {"svg": P5, "alt": ("안내인이 '그 창고는 제 목록에 없는데요' 하고, 오래된 창고엔 여전히 땅굴이 이어져 있음", "The escort says that shed isn't on my list, and an old storehouse still has a tunnel leading to it"),
         "caption": ("안내인이 모르는 방은 못 가요.", "Rooms the escort doesn't know, you can't reach."),
         "small": ("오래된 창고처럼 안내인 목록에 없는 방은 아직 땅굴로 가요. 그래서 한동안은 둘 다 써요.", "Old storehouses not on the escort's list still need the tunnel. So for a while, both stay in use.")},
    ],
    "summary": (("<b>ZTNA</b> = 성에 들여보내지 않고, 확인한 사람을 안내인이 <b>딱 필요한 방 문 앞까지만</b> 데려다주는 것.",
                 "<b>ZTNA</b> = never let people into the castle; check them, then have an escort walk them <b>to exactly the door they need</b>."),
                ("Zero Trust Network Access. 땅굴(VPN)을 대신해요. 문마다 물어보는 성(제로 트러스트)을 밖에서 오는 사람에게 적용한 거예요. 가트너가 2019년에 이름 붙였고, SSE 묶음 안에 들어 있어요.",
                 "Zero Trust Network Access replaces the tunnel (VPN). It's the castle that always asks (Zero Trust), applied to people coming from outside. Named by Gartner in 2019; ships inside the SSE bundle.")),
    "glossary": [
        ("VPN", "VPN", ("땅굴.", "The tunnel."), ("지나면 성 안. 입구가 밖에서 보여서 자주 공격받아요.", "Through it, you're inside. Its mouth is visible from outside, so it gets attacked a lot.")),
        ("브로커", "Broker / controller", ("안내인.", "The escort."), ("누구인지 확인하고, 어느 방까지 데려갈지 정하는 사람.", "Checks who you are and decides which door you get walked to.")),
        ("앱 단위 접근", "App-level access", ("방 하나까지만.", "One door only."), ('성 전체가 아니라 앱 하나. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'One app, not the whole castle. → <a href="rbac-en.html">a key ring for every hat</a>')),
        ("기기 상태 확인", "Device posture", ("신발에 진흙?", "Mud on your shoes?"), ('사람뿐 아니라 들고 온 컴퓨터도 봐요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'Not just the person — the computer they brought. → <a href="zerotrust-en.html">the castle that always asks</a>')),
        ("성 숨기기", "Dark cloud / app hiding", ("보이지 않는 성.", "The invisible castle."), ("밖에서 두드릴 문이 없어요. 문이 없으면 도둑이 두드릴 수도 없어요.", "No gate to knock on from outside — and no gate means nothing for a thief to knock on.")),
        ("커넥터", "Connector", ("방 안에서 내민 줄.", "A rope from inside the room."), ("방이 안내인에게 먼저 줄을 던져요. 밖에서 안으로 뚫는 게 아니라 안에서 밖으로.", "The room throws a rope out to the escort — inside-out, not outside-in.")),
        ("SDP", "Software-Defined Perimeter", ("같은 생각의 옛 이름.", "The older name for the same idea."), ("안내인 방식을 먼저 부르던 말.", "What the escort approach was called first.")),
        ("SSE", "SSE", ("검문소 묶음.", "The checkpoint bundle."), ('<a href="swg-ko.html">검문소</a>(SWG) + <a href="casb-ko.html">창고 문지기</a>(CASB) + 안내인(ZTNA).', '<a href="swg-en.html">Checkpoint</a> (SWG) + <a href="casb-en.html">shed broker</a> (CASB) + escort (ZTNA).')),
    ],
}
