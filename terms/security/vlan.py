from _draw import *

BLUE, GREEN, RED = "#5B8DEF", "var(--good)", "var(--bad)"
COOK, GUEST, CLERK = "#E9B44C", None, "#5B8DEF"
GUARD = dict(hat="var(--good)", shirt="var(--good)")
DOORS = (("⟦부엌|Kitchen⟧", False), ("⟦마당|Yard⟧", False), ("⟦금고|Vault⟧", False), ("⟦창고|Storage⟧", False), ("⟦서재|Study⟧", False))


def ribbon(color):
    return f'<rect x="4" y="56" width="52" height="8" rx="4" fill="{color}"/><path d="M52 60 l10 -6 v12z" fill="{color}"/>'


def walker(x, y, hat, color=None, s=0.7, face=SMILE):
    return person(x, y, hat=hat, shirt="#4A5A72", s=s, face=face, extra=(ribbon(color) if color else ""))


def stripes(y, h, colors, x0=0, w=760):
    seg = w / len(colors)
    return "".join(f'<rect x="{x0 + i * seg}" y="{y}" width="{seg}" height="{h}" fill="{c}" fill-opacity="0.35"/>' for i, c in enumerate(colors))


def shout(x, y, color="var(--bad)"):
    return f'<path d="M{x} {y} a30 30 0 0 1 0 -40 M{x + 14} {y + 6} a50 50 0 0 1 0 -52" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>'


# 1. 복도가 하나면 다 섞인다
P1 = svg(300, corridor(300, DOORS, marks=False)
         + walker(110, 150, COOK) + walker(300, 160, GUEST) + walker(480, 150, CLERK) + walker(620, 160, COOK)
         + shout(370, 190) + '<path d="M380 200 C440 230 520 220 560 200" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>'
         + label(470, 250, "⟦손님이 금고 방 문을 두드려요|a guest knocks on the vault door⟧", 12, "var(--bad)")
         + label(380, 285, "⟦요리사, 손님, 회계가 한 복도에 다 섞여요|cooks, guests and clerks all share one hallway⟧", 13, "var(--muted)"))

# 2. 벽을 세우려면 복도를 새로 지어야 한다
BRICKS = "".join(f'<rect x="{x}" y="{y}" width="34" height="12" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="2"/>' for y in range(60, 190, 14) for x in range(300 + ((y // 14) % 2) * 17, 460, 36))
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>' + BRICKS
         + person(120, 110, s=0.85, face=FROWN + SWEAT, **GUARD, extra='<g transform="translate(64,50) rotate(-20)"><rect x="-4" y="-20" width="8" height="40" rx="2" fill="#8B5E3C"/><rect x="-12" y="-28" width="24" height="10" fill="var(--stone-dark)"/></g>')
         + label(560, 100, "⟦복도 셋?|three hallways?⟧", 20, "var(--ink)", cls="d") + label(560, 130, "⟦비싸고 오래 걸려요|expensive and slow⟧", 13, "var(--muted)")
         + '<g transform="translate(560,190)"><circle r="24" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -14 V0 L9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(380, 262, "⟦벽을 세우려면 복도를 새로 지어야 해요|to build walls you\'d have to build new hallways⟧", 13, "var(--muted)"))

# 3. VLAN = 색 리본으로 복도 나누기 (hero)
P3 = svg(340, corridor(340, DOORS, marks=False) + stripes(196, 144, (BLUE, GREEN, RED))
         + walker(70, 150, COOK, BLUE) + walker(170, 165, COOK, BLUE)
         + walker(320, 150, GUEST, GREEN) + walker(420, 165, GUEST, GREEN)
         + walker(570, 150, CLERK, RED) + walker(660, 165, CLERK, RED)
         + label(126, 320, "⟦파랑: 요리사|blue: cooks⟧", 13, "#FFF") + label(380, 320, "⟦초록: 손님|green: guests⟧", 13, "#FFF") + label(633, 320, "⟦빨강: 회계|red: clerks⟧", 13, "#FFF")
         + '<path d="M130 200 L200 200" stroke="' + BLUE + '" stroke-width="3"/><path d="M380 200 L450 200" stroke="' + GREEN + '" stroke-width="3"/><path d="M630 200 L700 200" stroke="' + RED + '" stroke-width="3"/>'
         + '<path d="M240 190 L300 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/><path d="M262 178 l16 24 M278 178 l-16 24" stroke="var(--bad)" stroke-width="3"/>'
         + '<path d="M490 190 L550 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/><path d="M512 178 l16 24 M528 178 l-16 24" stroke="var(--bad)" stroke-width="3"/>')

# 4. 색을 넘으려면 문지기, 통로 하나엔 여러 색
RULEBOOK = ('<g transform="translate(60,60)"><rect width="56" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(28, 16, "⟦초록→빨강|green→red⟧", 8, "#142033") + label(28, 30, "⟦× 안 돼요|× no⟧", 9, "var(--bad)") + "</g>")
P4 = svg(320, '<rect width="380" height="320" fill="var(--sky)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + stripes(200, 60, (GREEN,), 0, 150) + stripes(200, 60, (RED,), 230, 150)
         + walker(40, 110, GUEST, GREEN) + gate(170, 60, 0.7) + person(230, 95, s=0.6, face=EYES, **GUARD, extra=RULEBOOK)
         + '<path d="M120 230 L170 230" stroke="' + GREEN + '" stroke-width="3"/><path d="M215 230 l16 16 M231 230 l-16 16" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(190, 300, "⟦색을 넘으려면 문지기를 지나요|to cross a color, you pass the gatekeeper⟧", 12, "var(--muted)")
         + '<rect x="420" y="120" width="300" height="70" rx="8" fill="var(--stone-dark)"/>'
         + "".join(f'<rect x="430" y="{130 + i * 18}" width="280" height="10" rx="5" fill="{c}"/>' for i, c in enumerate((BLUE, GREEN, RED)))
         + label(570, 100, "⟦건물 사이 통로 하나|one passage between buildings⟧", 13, "var(--ink)", cls="d")
         + label(570, 220, "⟦리본 세 색이 같이 지나가요|all three ribbons travel together⟧", 12, "var(--muted)")
         + label(570, 300, "⟦트렁크|a trunk⟧", 13, "var(--accent)", cls="d"))

# 5. 리본은 벽이 아니다
P5 = svg(300, corridor(300, DOORS, marks=False) + stripes(196, 104, (GREEN, RED), 0, 760)
         + walker(200, 140, GUEST, GREEN, face=MASK)
         + '<g transform="translate(300,180)"><rect x="-26" y="-6" width="52" height="8" rx="4" fill="' + GREEN + '"/><path d="M-30 -14 l60 24 M30 -14 l-60 24" stroke="var(--bad)" stroke-width="3"/></g>'
         + '<path d="M270 150 L340 150" stroke="var(--accent)" stroke-width="3"/><path d="M330 140 L342 150 L330 160" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + walker(380, 140, GUEST, RED, face=MASK)
         + label(300, 250, "⟦리본을 바꿔 달았어요|swapped the ribbon⟧", 12, "var(--bad)")
         + person(600, 130, s=0.7, face=EYES, **GUARD) + label(620, 250, "⟦구멍 문지기가 리본을 달아줘요|the socket gatekeeper hands out ribbons⟧", 11, "var(--muted)")
         + label(380, 285, "⟦리본은 벽이 아니라 약속이에요|a ribbon is a promise, not a wall⟧", 13, "#F5E6B8"))

RIBBON_I = icon(f'<rect x="8" y="28" width="40" height="8" rx="4" fill="{BLUE}"/><path d="M48 32 l10 -6 v12z" fill="{BLUE}"/>')
SAME_I = icon(f'<circle cx="18" cy="32" r="8" fill="{GREEN}"/><circle cx="46" cy="32" r="8" fill="{GREEN}"/><path d="M26 32 H38" stroke="{GREEN}" stroke-width="3"/>')
GATE_I = icon('<rect x="8" y="24" width="48" height="30" fill="var(--stone-dark)"/><rect x="8" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="16" width="10" height="10" fill="var(--stone-dark)"/><path d="M24 54 V42 a8 8 0 0 1 16 0 V54Z" fill="var(--night)"/>')
TRUNK_I = icon(f'<rect x="8" y="16" width="48" height="32" rx="6" fill="var(--stone-dark)"/><rect x="14" y="22" width="36" height="5" rx="2" fill="{BLUE}"/><rect x="14" y="30" width="36" height="5" rx="2" fill="{GREEN}"/><rect x="14" y="38" width="36" height="5" rx="2" fill="{RED}"/>')

PAGE = {
    "slug": "vlan", "order": 36,
    "title": ("색 리본으로 나눈 복도", "The Hallway Split by Ribbons"),
    "h1": ("<em>VLAN</em>이 뭐예요?", "What is a <em>VLAN</em>?"),
    "sub": ("가상 LAN(Virtual LAN)을 색 리본으로 나눈 복도 이야기로 풀어봤어요.",
            "Virtual LANs, told as a story about a hallway split up with colored ribbons."),
    "panels": [
        {"svg": P1, "alt": ("한 복도에 요리사, 손님, 회계가 섞여 있고, 손님이 금고 방 쪽으로 소리침", "Cooks, guests and clerks mixed in one hallway; a guest shouts toward the vault door"),
         "caption": ("복도가 하나면 다 섞여요.", "One hallway, and everyone mixes."),
         "small": ('손님 노트북이 금고 방 문을 두드릴 수 있어요. <a href="ndr-ko.html">복도 파수꾼</a>이 걱정하는 그 일이에요.',
                   'A guest laptop can knock on the vault door — exactly what the <a href="ndr-en.html">hallway watcher</a> worries about.')},
        {"svg": P2, "alt": ("벽돌을 쌓다 땀 흘리는 경비, '복도 셋? 비싸고 오래 걸려요', 시계", "A guard sweating over a pile of bricks; three hallways? expensive and slow; a clock"),
         "caption": ("벽을 세우려면 복도를 새로 지어야 해요.", "Walls mean building whole new hallways."),
         "small": ("복도 셋을 새로 짓는 건 비싸고 오래 걸려요.", "Three new hallways is expensive and slow.")},
        {"svg": P3, "hero": True, "alt": ("복도 바닥이 파랑·초록·빨강으로 나뉘고, 사람마다 같은 색 리본을 달고 같은 색끼리만 이어져 있음. 색 사이엔 X", "The hallway floor striped blue, green and red; each person wears a matching ribbon and connects only to the same color; an X between colors"),
         "caption": ("VLAN은 색 리본으로 복도를 나눠요.", "A VLAN splits the hallway with colored ribbons."),
         "small": ("벽 대신 리본이에요. 파란 리본은 파란 리본끼리만 이야기해요. 복도는 하나, 마을은 셋.", "Ribbons instead of walls. Blue talks only to blue. One hallway, three neighborhoods."),
         "tricks": (4, [
             (RIBBON_I, ("리본", "The ribbon"), ("색마다 번호가 있어요", "every color has a number"), "calm"),
             (SAME_I, ("같은 색끼리", "Same color only"), ("소리쳐도 같은 색만 들어요", "shout, and only your color hears"), "calm"),
             (GATE_I, ("색을 넘으려면", "Crossing colors"), ("문지기를 지나요", "means passing a gatekeeper")),
             (TRUNK_I, ("한 통로에 여러 색", "Many colors, one passage"), ("건물 사이는 같이 지나요", "between buildings they share the road"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 초록 리본 손님이 빨간 구역으로 가려다 문지기의 목록에 막힘. 오른쪽: 건물 사이 통로 하나에 파랑·초록·빨강 리본이 나란히 지나감", "Left: a green-ribbon guest heading for the red zone is stopped by the gatekeeper's list. Right: one passage between buildings carries blue, green and red ribbons side by side"),
         "caption": ("색을 넘으려면 문지기를 지나야 해요.", "Crossing a color means passing the gatekeeper."),
         "small": ('손님(초록)이 금고(빨강)로 가려면 <a href="firewall-ko.html">문지기</a>가 목록을 봐요. 건물 사이 통로 하나엔 리본 여러 색이 같이 지나가요 — 트렁크예요.',
                   'A guest (green) heading for the vault (red) meets the <a href="firewall-en.html">gatekeeper</a> and his list. Between buildings, one passage carries every color — a trunk.')},
        {"svg": P5, "alt": ("가면 쓴 사람이 초록 리본을 떼고 빨간 리본으로 바꿔 달았고, 옆에 구멍 문지기", "A masked figure tears off a green ribbon and puts on a red one; a socket gatekeeper stands nearby"),
         "caption": ("리본은 벽이 아니라 약속이에요.", "A ribbon is a promise, not a wall."),
         "small": ('리본을 바꿔 달면 넘어갈 수 있어요. 그래서 <a href="nac-ko.html">구멍 문지기</a>가 리본을 달아주고, 색 사이엔 진짜 <a href="firewall-ko.html">문지기</a>를 둬요.',
                   'Swap the ribbon and you\'re across. So the <a href="nac-en.html">socket gatekeeper</a> hands out ribbons, and a real <a href="firewall-en.html">gatekeeper</a> stands between colors.')},
    ],
    "summary": (("<b>VLAN</b> = 복도 하나를 <b>색 리본</b>으로 여러 복도처럼 나누는 것. 같은 색끼리만 이야기하고, 색을 넘으려면 <b>문지기</b>를 지나요.",
                 "A <b>VLAN</b> = one hallway split into several with <b>colored ribbons</b>. Same color talks to same color; crossing colors means a <b>gatekeeper</b>."),
                ("Virtual LAN, IEEE 802.1Q. 리본은 1부터 4094까지 번호가 붙은 태그예요. 리본을 더 잘게 나누면 마이크로 세그멘테이션 — 문마다 물어보는 성의 복도 판이에요.",
                 "Virtual LAN, IEEE 802.1Q. Ribbons are tags numbered 1 to 4094. Cut the ribbons finer and you get micro-segmentation — the hallway version of the castle that always asks.")),
    "glossary": [
        ("태그 · VLAN ID", "Tag · VLAN ID", ("리본 색.", "The ribbon\'s color."), ("1부터 4094까지 번호. 리본은 사람이 아니라 구멍이 달아줘요.", "Numbered 1 to 4094. The socket, not the person, hands out the ribbon.")),
        ("브로드캐스트 도메인", "Broadcast domain", ("소리가 들리는 범위.", "How far a shout carries."), ("소리치면 같은 색만 들어요.", "Shout, and only your color hears.")),
        ("액세스 포트", "Access port", ("한 색만 다는 구멍.", "A one-color socket."), ('꽂으면 그 색 리본을 달아줘요. → <a href="nac-ko.html">복도 구멍마다 문지기</a>', 'Plug in, get that color\'s ribbon. → <a href="nac-en.html">the gatekeeper at every socket</a>')),
        ("트렁크", "Trunk", ("여러 색이 같이 지나는 통로.", "The passage every color shares."), ("건물 사이 통로 하나에 리본을 달고 다 같이 가요.", "One passage between buildings, ribbons on, everyone together.")),
        ("인터 VLAN 라우팅", "Inter-VLAN routing", ("색 사이 문지기.", "The gatekeeper between colors."), ('초록에서 빨강으로 가려면 여길 지나요. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'Green to red passes here. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("VLAN 호핑", "VLAN hopping", ("리본 바꿔 달기.", "Swapping ribbons."), ("리본이 약속인 걸 노린 도둑의 수법.", "A thief\'s trick that exploits the ribbon being only a promise.")),
        ("네이티브 VLAN", "Native VLAN", ("리본 없는 사람 취급.", "How the ribbonless are treated."), ("리본이 없으면 이 색으로 쳐요. 도둑이 자주 노려요.", "No ribbon? You count as this color. Thieves love it.")),
        ("마이크로 세그멘테이션", "Micro-segmentation", ("리본을 더 잘게.", "Ribbons cut finer."), ('방 하나, 물건 하나 단위까지. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'Down to one room, one device. → <a href="zerotrust-en.html">the castle that always asks</a>')),
    ],
}
