from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
DOORS = tuple(("", False) for _ in range(5))


def poster(x, y, hat="var(--bad)", s=1.0, text="⟦수배|WANTED⟧", mask=True):
    m = '<path d="M-8 -2 h16 v5 h-16z" fill="#111C30"/>' if mask else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-34" width="48" height="64" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<circle cx="-24" cy="-34" r="3" fill="var(--stone-dark)"/><circle cx="24" cy="-34" r="3" fill="var(--stone-dark)"/>'
            f'{label(0, -22, text, 9, "var(--bad)")}<circle cy="-2" r="12" fill="{SKIN}"/><path d="M-13 -6 Q0 -22 13 -6 Z" fill="{hat}"/>{m}'
            f'<rect x="-16" y="14" width="32" height="3" fill="#C9A86A"/><rect x="-12" y="20" width="24" height="3" fill="#C9A86A"/></g>')


def bell(x, y, s=1.0, ring=False):
    waves = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{waves}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def barrier(x, y, s=1.0, down=True):
    stripes = "".join(f'<rect x="{-60 + i * 24}" y="-6" width="12" height="12" fill="var(--bad)"/>' for i in range(5))
    rot = 0 if down else -60
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-8" y="-6" width="16" height="70" fill="var(--stone-dark)"/>'
            f'<g transform="rotate({rot} 0 0)"><rect x="-64" y="-6" width="128" height="12" rx="6" fill="#FFF"/>{stripes}</g></g>')


STOOL = '<rect x="20" y="150" width="60" height="8" rx="3" fill="#8B5E3C"/><rect x="26" y="158" width="6" height="90" fill="#8B5E3C"/><rect x="68" y="158" width="6" height="90" fill="#8B5E3C"/>'
STACK = '<g transform="translate(70,70)">' + "".join(f'<rect x="{-10 + i * 3}" y="{-14 - i * 3}" width="26" height="34" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(3)) + "</g>"
WATCHER = lambda x, y, s=1.0, face=EYES: f'<g transform="translate({x},{y}) scale({s})">{STOOL}{person(20, 50, s=0.9, face=face, extra=STACK, **GUARD)}</g>'
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'

# 1. 복도 벽에 수배 전단
P1 = svg(280, corridor(280, DOORS, marks=False)
         + poster(172, 120, "var(--bad)") + poster(312, 120, "#4A5A72", text="⟦수배|WANTED⟧") + poster(452, 120, "var(--accent)") + poster(592, 120, "var(--stone-dark)")
         + label(380, 262, "⟦'이 얼굴, 이 가방, 이 말투 — 보이면 알려주세요'|'this face, this bag, this way of talking — report it'⟧", 13, "var(--muted)"))

# 2. 전단이 있어도 보는 사람이 없다
P2 = svg(280, corridor(280, DOORS, marks=False) + poster(172, 120, "var(--bad)")
         + person(300, 150, s=0.9, face=MASK, extra=BAG)
         + '<path d="M180 92 Q240 40 300 100" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
         + label(240, 60, "⟦똑같은데…|same face…⟧", 12, "var(--muted)")
         + label(520, 200, "⟦아무도 안 봐요|nobody\'s looking⟧", 14, "var(--bad)", cls="d")
         + label(380, 262, "⟦도둑이 전단 바로 앞을 지나가요|the thief walks right past his own poster⟧", 13, "var(--muted)"))

# 3. IDS 종, IPS 막기 (hero)
P3 = svg(340, '<rect width="380" height="340" fill="var(--sky)"/><rect x="380" width="380" height="340" fill="var(--accent-soft)"/>'
         + '<rect y="200" width="760" height="140" fill="var(--stone)"/><rect y="196" width="760" height="6" fill="var(--stone-dark)"/>'
         + label(190, 40, "IDS", 26, "var(--ink)", cls="d") + label(190, 64, "⟦옆에 앉아서 종|sits beside, rings a bell⟧", 13, "var(--muted)")
         + WATCHER(20, 30, 0.85) + bell(150, 100, 0.8, ring=True)
         + person(230, 170, s=0.8, face=MASK, extra=BAG) + '<path d="M310 250 L360 250" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/><path d="M350 240 L362 250 L350 260" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(190, 320, "⟦지나가게 두고 알려요|lets him pass, tells the guard room⟧", 12, "var(--muted)")
         + label(570, 40, "IPS", 26, "var(--ink)", cls="d") + label(570, 64, "⟦가운데 서서 막기|stands in the path, blocks⟧", 13, "var(--muted)")
         + person(560, 90, s=0.85, face=EYES, extra=STACK, **GUARD) + barrier(620, 180, 1.0, down=True)
         + person(440, 170, s=0.8, face=MASK + SWEAT, extra=BAG)
         + label(570, 320, "⟦길을 막아 되돌려 보내요|blocks the road, sends him back⟧", 12, "var(--muted)"))

# 4. 전단과 딱 맞으면
P4 = svg(300, corridor(300, DOORS, marks=False)
         + poster(120, 110, "var(--bad)", 1.1)
         + person(240, 140, s=0.9, face=MASK, extra=BAG)
         + '<path d="M150 100 L230 150" stroke="var(--good)" stroke-width="3" stroke-dasharray="5 5"/>' + label(190, 100, "⟦딱 맞음|match⟧", 13, "var(--good)", cls="d")
         + bell(420, 90, 0.9, ring=True) + '<path d="M450 60 Q520 20 600 40" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + '<g transform="translate(640,40)"><rect x="-40" y="-26" width="80" height="52" rx="6" fill="var(--night)"/><rect x="-32" y="-18" width="64" height="36" fill="var(--bad)"/>' + label(0, 4, "⟦경비실|guard room⟧", 11, "#FFF") + "</g>"
         + barrier(560, 140, 1.0, down=True) + label(560, 262, "⟦막힘|blocked⟧", 13, "var(--bad)")
         + label(300, 275, "⟦종은 경비실로, 사람은 되돌아가요|the bell goes to the guard room; the person goes back⟧", 13, "var(--muted)"))

# 5. 전단에 없는 얼굴, 닮은 사람
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + poster(70, 90, "var(--bad)") + person(200, 100, s=0.9, hat="var(--good)", shirt="#2E3D57", face=MASK, extra=BAG)
         + '<path d="M110 80 L190 110" stroke="var(--bad)" stroke-width="3"/><path d="M140 70 l20 20 M160 70 l-20 20" stroke="var(--bad)" stroke-width="4"/>'
         + label(190, 240, "⟦전단에 없는 새 얼굴|a new face, no poster⟧", 13, "var(--bad)")
         + label(190, 275, "⟦그건 버릇을 보는 복도 파수꾼 몫|that one\'s for the hallway watcher, who reads habits⟧", 11, "var(--muted)")
         + poster(450, 90, "var(--bad)") + person(560, 100, s=0.9, hat="var(--bad)", shirt="#4A5A72", face=FROWN, extra=BAG)
         + barrier(680, 150, 0.8, down=True)
         + bubble(520, 20, 200, 34, "⟦저 그냥 빨간 모자 손님인데요|I just like red hats!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(570, 240, "⟦닮은 손님을 막았어요|a lookalike got blocked⟧", 13, "var(--bad)")
         + label(570, 275, "⟦그래서 IPS는 확실한 전단만 써요|so IPS only uses the surest posters⟧", 11, "var(--muted)"))

POSTER_I = icon(f'<rect x="14" y="8" width="36" height="48" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="30" r="8" fill="{SKIN}"/><path d="M23 27 Q32 16 41 27 Z" fill="var(--bad)"/><rect x="26" y="29" width="12" height="4" fill="#111C30"/>')
BELL_I = icon('<path d="M20 34 c0 -20 24 -20 24 0 v10 h-24 z" fill="#E9B44C"/><rect x="16" y="46" width="32" height="4" rx="2" fill="#C9822B"/><circle cx="32" cy="54" r="3" fill="#C9822B"/><path d="M12 24 a20 20 0 0 1 -4 -12 M52 24 a20 20 0 0 0 4 -12" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BAR_I = icon('<rect x="28" y="24" width="8" height="32" fill="var(--stone-dark)"/><rect x="6" y="20" width="52" height="8" rx="4" fill="#FFF" stroke="var(--bad)" stroke-width="2"/><rect x="14" y="20" width="8" height="8" fill="var(--bad)"/><rect x="30" y="20" width="8" height="8" fill="var(--bad)"/><rect x="46" y="20" width="8" height="8" fill="var(--bad)"/>')
SIDE_I = icon('<rect x="6" y="30" width="52" height="10" fill="var(--stone)"/><circle cx="16" cy="18" r="6" fill="var(--good)"/><rect x="10" y="26" width="12" height="4" fill="var(--good)"/><circle cx="46" cy="24" r="6" fill="var(--accent)"/><rect x="40" y="32" width="12" height="4" fill="var(--accent)"/>')

PAGE = {
    "slug": "idsips", "order": 28,
    "title": ("수배 전단 든 파수꾼", "The Watcher with the Wanted Posters"),
    "h1": ("<em>IDS / IPS</em>가 뭐예요?", "What are <em>IDS / IPS</em>?"),
    "sub": ("침입 탐지·차단 시스템(Intrusion Detection / Prevention System)을 수배 전단을 든 파수꾼 이야기로 풀어봤어요.",
            "Intrusion Detection and Prevention Systems, told as a story about a watcher holding wanted posters."),
    "panels": [
        {"svg": P1, "alt": ("복도 벽에 '수배'라고 적힌 얼굴 전단 네 장", "Four WANTED face posters pinned along the hallway wall"),
         "caption": ("복도 벽에 수배 전단이 붙어 있어요.", "Wanted posters hang along the hallway."),
         "small": ('"이 얼굴, 이 가방, 이 말투 — 보이면 알려주세요." <a href="cti-ko.html">망루 친구</a>가 보내준 거예요.',
                   '"This face, this bag, this way of talking — report it." Sent by the <a href="cti-en.html">watchtower friend</a>.')},
        {"svg": P2, "alt": ("전단과 똑같은 얼굴의 도둑이 가방을 들고 전단 앞을 지나가는데 아무도 없음", "A thief with the same face as the poster walks past it carrying a bag; nobody is around"),
         "caption": ("전단이 있어도 보는 사람이 없으면 소용없어요.", "A poster is useless if nobody's looking at it."),
         "small": ("도둑이 전단 바로 앞을 지나가요.", "The thief strolls right past his own poster.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽 IDS: 파수꾼이 옆에 앉아 전단과 대조하고 종을 울리며 도둑은 지나감. 오른쪽 IPS: 파수꾼이 길 한가운데 서서 차단봉으로 막음", "Left, IDS: the watcher sits beside the hallway, matches posters, rings a bell while the thief passes. Right, IPS: the watcher stands in the path and drops a barrier"),
         "caption": ("IDS는 종을 울리고, IPS는 길을 막아요.", "IDS rings the bell; IPS blocks the road."),
         "small": ("둘 다 전단과 대조해요. IDS는 옆에 앉아 종만 울리고, IPS는 길 한가운데 서서 막아서요.", "Both compare against the posters. IDS sits to the side and only rings; IPS stands in the path and stops you."),
         "tricks": (4, [
             (POSTER_I, ("수배 전단", "Wanted posters"), ("아는 도둑의 얼굴", "faces of known thieves")),
             (BELL_I, ("종", "The bell"), ("IDS — 경비실에 알려요", "IDS — tells the guard room"), "warm"),
             (BAR_I, ("막아서기", "The barrier"), ("IPS — 되돌려 보내요", "IPS — sends them back")),
             (SIDE_I, ("옆 vs 가운데", "Beside vs. in the path"), ("옆은 안 느려요, 가운데는 막을 수 있어요", "beside never slows you; in the path can stop you"), "calm"),
         ])},
        {"svg": P4, "alt": ("전단과 도둑 사이에 '딱 맞음', 종이 울려 경비실 화면으로 이어지고, 차단봉이 내려와 '막힘'", "A match between poster and thief; the bell rings toward the guard-room screen; the barrier drops — blocked"),
         "caption": ("전단과 딱 맞으면 종이 울리고 길이 막혀요.", "A match rings the bell and drops the barrier."),
         "small": ('종은 <a href="soc-ko.html">경비실</a>로 가요. 막힌 사람은 되돌아가요.', 'The bell goes to the <a href="soc-en.html">guard room</a>. The blocked one turns around.')},
        {"svg": P5, "alt": ("왼쪽: 전단에 없는 초록 모자의 새 도둑이 통과. 오른쪽: 빨간 모자를 쓴 손님이 차단봉에 막혀 '저 그냥 빨간 모자 손님인데요'", "Left: a new thief in a green hat, not on any poster, walks through. Right: a customer in a red hat is blocked — I just like red hats!"),
         "caption": ("전단에 없는 얼굴은 못 잡고, 닮은 사람을 막기도 해요.", "New faces get through; lookalikes get blocked."),
         "small": ('새 도둑은 전단이 없어요 — 그건 버릇을 보는 <a href="ndr-ko.html">복도 파수꾼(NDR)</a> 몫. 그리고 IPS가 닮은 손님을 막으면 다들 화나니까, 확실한 전단만 써요.',
                   'A new thief has no poster — that\'s the <a href="ndr-en.html">hallway watcher (NDR)</a>\'s job, reading habits. And since IPS blocking a lookalike makes everyone angry, it only uses the surest posters.')},
    ],
    "summary": (("<b>IDS / IPS</b> = 수배 전단(시그니처)을 들고 복도에서 지나가는 것을 <b>대조</b>하는 파수꾼. IDS는 <b>종</b>을, IPS는 <b>막아서기</b>를.",
                 "<b>IDS / IPS</b> = the watcher who <b>compares</b> everything in the hallway against wanted posters (signatures). IDS <b>rings</b>; IPS <b>blocks</b>."),
                ("Intrusion Detection / Prevention System. Snort와 Suricata가 전단 쓰는 법이에요. 요즘은 대부분 성벽(방화벽) 안에 같이 들어 있어요(NGFW). 복도 파수꾼(NDR)은 버릇을, IDS는 전단을 봐요.",
                 "Intrusion Detection / Prevention System. Snort and Suricata are how the posters get written. Today it's usually built into the wall (a next-gen firewall). The hallway watcher (NDR) reads habits; IDS reads posters.")),
    "glossary": [
        ("시그니처", "Signature", ("수배 전단.", "The wanted poster."), ('아는 공격의 생김새. → <a href="ioc-ko.html">남겨진 발자국</a>과 같은 종류예요', 'What a known attack looks like. → same family as <a href="ioc-en.html">the footprint</a>')),
        ("규칙", "Rule", ("전단 한 장.", "One poster."), ("Snort, Suricata 규칙. 한 줄에 얼굴 하나.", "A Snort or Suricata rule — one face per line.")),
        ("IDS", "Intrusion Detection System", ("옆에 앉아 종 울리기.", "Sit beside, ring the bell."), ("보고 알리기만. 길은 안 막아요.", "Watches and reports. Never blocks.")),
        ("IPS", "Intrusion Prevention System", ("가운데 서서 막기.", "Stand in the path, block."), ("같은 전단, 다른 자리. 막을 수 있는 대신 잘못 막을 수도.", "Same posters, different spot. Can block — and can block wrongly.")),
        ("인라인", "Inline", ("길 한가운데.", "In the path."), ("모든 사람이 파수꾼을 지나야 해요. 파수꾼이 느리면 복도가 느려요.", "Everyone passes the watcher. A slow watcher means a slow hallway.")),
        ("탭 · 미러", "TAP / out-of-band", ("옆에 앉기.", "Sitting beside."), ('복사본만 봐요. 절대 안 느려져요. → <a href="ndr-ko.html">복도 끝 거울</a>', 'Sees a copy only. Never slows anything. → <a href="ndr-en.html">the mirror at the end</a>')),
        ("오탐", "False positive", ("닮은 손님 막기.", "Blocking a lookalike."), ('빨간 모자만 보고 막은 것. → <a href="soc-ko.html">경비실의 고양이</a>', 'Blocked for the red hat alone. → <a href="soc-en.html">the guard room\'s cat</a>')),
        ("NGFW", "Next-gen firewall", ("전단 파수꾼이 든 성벽.", "A wall with the poster-watcher built in."), ("성벽(방화벽)에 IPS까지 넣은 것. 요즘 보통 이렇게 팔아요.", "The wall (firewall) with IPS inside. How it's usually sold today.")),
    ],
}
