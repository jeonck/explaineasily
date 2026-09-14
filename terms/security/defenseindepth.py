from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
MAID = dict(hat=None, shirt="#7B3FA0")
LAYERS = (("var(--stone-dark)", "#F2F6FC", "⟦해자 · 성벽|moat · wall⟧"), ("var(--stone)", "var(--ink)", "⟦복도|halls⟧"), ("var(--good-soft)", "var(--ink)", "⟦경비견|dogs⟧"),
          ("var(--panel)", "var(--ink)", "⟦자물쇠|locks⟧"), ("var(--accent-soft)", "var(--ink)", "⟦사람|people⟧"))


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def envelope(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-20" width="60" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-30 -20 l30 20 l30 -20" stroke="#C9A86A" stroke-width="2" fill="none"/><circle cy="2" r="7" fill="var(--bad)"/></g>')


def ladder(x1, y1, x2, y2, n=5):
    out = f'<path d="M{x1} {y1} L{x2} {y2} M{x1 + 18} {y1 + 8} L{x2 + 18} {y2 + 8}" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'
    for i in range(1, n + 1):
        rx, ry = x1 + (x2 - x1) * i / (n + 1), y1 + (y2 - y1) * i / (n + 1)
        out += f'<path d="M{rx:.0f} {ry:.0f} l18 8" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/>'
    return out


def door(x, y, s=1.0, lock=True):
    lk = '<rect x="-8" y="10" width="16" height="14" rx="2" fill="#E9B44C"/><path d="M-5 10 v-6 a5 5 0 0 1 10 0 v6" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else '<circle cx="14" cy="16" r="4" fill="#E9B44C"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-40" width="52" height="80" rx="3" fill="{WOOD}"/>{lk}</g>'


# 1. 벽 하나 — 넘으면 곧장 금고
P1 = svg(320, sky(320)
         + battlements(330, 70, 40, 2, "var(--stone-dark)", 20) + '<rect x="330" y="90" width="40" height="172" fill="var(--stone-dark)"/>'
         + ladder(250, 262, 318, 96) + person(262, 140, s=0.65, face=MASK)
         + '<path d="M372 100 Q470 40 540 196" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="8 6"/><path d="M540 200 l-12 -10 l14 -4z" fill="var(--bad)"/>'
         + chest(560, 230, 1.4, lock=True) + label(560, 286, "⟦금고|the vault⟧", 11, "var(--muted)")
         + label(230, 286, "⟦사다리 하나면 끝|one ladder is all it takes⟧", 11, "var(--bad)")
         + label(380, 308, "⟦벽 하나면, 넘으면 끝이에요|one wall: climb it, and it\'s over⟧", 12, "var(--ink)", cls="d"))

# 2. 벽을 더 높여도 — 땅굴, 문으로 들어오는 가짜 편지, 조용한 종
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/><rect y="262" width="760" height="58" fill="var(--stone)"/>'
         + battlements(340, 0, 40, 2, "var(--stone-dark)", 20) + '<rect x="340" y="20" width="40" height="242" fill="var(--stone-dark)"/>'
         + '<path d="M340 262 v-46 a20 20 0 0 1 40 0 v46z" fill="var(--night)"/>'
         + '<path d="M300 262 q60 40 120 0 z" fill="var(--night)"/>'
         + person(225, 175, s=0.6, face=MASK) + label(240, 300, "⟦땅굴로|by tunnel⟧", 11, "var(--ink)")
         + envelope(240, 110, 0.9) + '<path d="M272 122 Q330 200 352 236" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="8 6"/>'
         + person(450, 140, s=0.7, face=EYES, **MAID) + envelope(500, 200, 0.6) + label(470, 245, "⟦가짜 편지는 문으로|the fake letter walks in the door⟧", 11, "var(--bad)")
         + bell(640, 120, 0.8, ring=False) + label(640, 200, "⟦종은 조용해요|the bell stays silent⟧", 11, "var(--muted)")
         + label(150, 100, "⟦벽을 더 높였어요|the wall, made taller⟧", 12, "var(--ink)", cls="d")
         + label(380, 304, "⟦벽을 높여도 길은 하나가 아니에요 — 뚫려도 아무도 몰라요|a taller wall is still one wall — and when it gives, nobody knows⟧", 11, "var(--ink)", cls="d"))

# 3. 겹겹이 (hero) — 동심원
CX, CY = 215, 180
LEGEND = (("⟦바깥: 해자와 성문 검문소|outside: the moat and the gate checkpoint⟧", "var(--stone-dark)"),
          ("⟦복도: 색 리본과 문지기|halls: colored ribbons and doorkeepers⟧", "var(--stone)"),
          ("⟦방마다: 경비견|every room: a guard dog⟧", "var(--good-soft)"),
          ("⟦상자: 열쇠 꾸러미와 봉인|chests: key rings and seals⟧", "var(--panel)"),
          ("⟦사람: 도둑 수업|people: thief lessons⟧", "var(--accent-soft)"))
P3 = svg(360, sky(360)
         + "".join(f'<circle cx="{CX}" cy="{CY}" r="{150 - i * 26}" fill="{c}" stroke="var(--line)" stroke-width="1.5"/>' for i, (c, _, _) in enumerate(LAYERS))
         + f'<circle cx="{CX}" cy="{CY}" r="20" fill="var(--night)"/>' + chest(CX, CY + 2, 0.5, lock=True)
         + "".join(label(CX, CY - (150 - i * 26) + 17, t, 10, ink, cls="d") for i, (_, ink, t) in enumerate(LAYERS))
         + label(590, 56, "⟦겹겹이|layer on layer⟧", 15, "var(--ink)", cls="d")
         + "".join(f'<circle cx="452" cy="{96 + i * 40}" r="9" fill="{c}" stroke="var(--line)" stroke-width="1.5"/>' + label(472, 100 + i * 40, t, 11, "var(--ink)", "start") for i, (t, c) in enumerate(LEGEND))
         + label(590, 300, "⟦어느 층도 완벽하지 않아요|no single layer is perfect⟧", 11, "var(--muted)")
         + label(380, 350, "⟦하나가 뚫려도 다음 층이 막고, 종이 울려요|one layer gives, the next holds — and the bell rings⟧", 12, "var(--ink)", cls="d"))

# 4. 도둑이 층을 하나씩 지나요 — 층마다 시간을 벌고, 층마다 종
P4 = svg(320, sky(320)
         + '<path d="M120 150 H700" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 6"/>'
         + battlements(60, 52, 60, 3, "var(--stone-dark)", 18) + '<rect x="60" y="70" width="60" height="75" fill="var(--stone-dark)"/>' + person(78, 30, s=0.5, face=MASK)
         + label(90, 178, "⟦넘었어요 ×|climbed over ×⟧", 11, "var(--bad)") + label(90, 200, "⟦밤 1시|1 am⟧", 10, "var(--muted)")
         + person(205, 70, s=0.6, face=EYES, **GUARD) + bell(265, 84, 0.45, ring=True)
         + label(235, 178, "⟦봤어요! 종|spotted! bell⟧", 11, "var(--accent)") + label(235, 200, "⟦1시 5분|1:05 am⟧", 10, "var(--muted)")
         + dog(380, 118, 0.9, bark=True)
         + label(380, 178, "⟦짖어요|barks⟧", 11, "var(--accent)") + label(380, 200, "⟦1시 6분|1:06 am⟧", 10, "var(--muted)")
         + door(525, 105, 0.9)
         + label(525, 178, "⟦안 열려요|won\'t open⟧", 11, "var(--good)") + label(525, 200, "⟦1시 8분|1:08 am⟧", 10, "var(--muted)")
         + chest(670, 112, 1.1, lock=True)
         + label(670, 178, "⟦무사해요|safe⟧", 11, "var(--good)") + label(670, 200, "⟦경비가 도착|guards arrive⟧", 10, "var(--muted)")
         + label(380, 262, "⟦해자를 넘은 도둑은 복도에서 들키고, 방문 앞에서 멈춰요|the thief who cleared the moat is spotted in the hall and stopped at the door⟧", 11, "var(--muted)")
         + label(380, 302, "⟦층마다 시간을 벌고, 층마다 종이 울려요|every layer buys time, and every layer can ring the bell⟧", 12, "var(--ink)", cls="d"))

# 5. 층마다 구멍이 있어요 — 그래서 겹쳐요
SLABS = ((180, 110, "var(--stone-dark)", "⟦해자|moat⟧"), (300, 190, "var(--stone)", "⟦복도|halls⟧"), (420, 90, "var(--good-soft)", "⟦경비견|dogs⟧"), (540, 160, "var(--panel)", "⟦자물쇠|locks⟧"))
P5 = svg(320, sky(320)
         + "".join(f'<rect x="{x}" y="60" width="40" height="180" rx="4" fill="{c}" stroke="var(--line)" stroke-width="1.5"/><circle cx="{x + 20}" cy="{hy}" r="12" fill="var(--sky)" stroke="var(--line)" stroke-width="1.5"/>' + label(x + 20, 265, t, 11, "var(--ink)") for x, hy, c, t in SLABS)
         + person(40, 70, s=0.5, face=MASK) + '<path d="M80 110 H290" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M288 100 l14 20 M302 100 l-14 20" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + person(40, 150, s=0.5, face=MASK) + '<path d="M80 190 H170" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M168 180 l14 20 M182 180 l-14 20" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + chest(660, 150, 1.3, lock=True) + label(660, 215, "⟦금고|the vault⟧", 11, "var(--muted)")
         + label(660, 100, "⟦구멍이 한 줄로 안 서요|the holes never line up⟧", 11, "var(--good)", cls="d")
         + label(380, 302, "⟦층마다 구멍이 있어요 — 그래서 겹치는 거예요|every layer has a hole — that\'s why they overlap⟧", 12, "var(--ink)", cls="d"))

LAYERS_I = icon('<circle cx="32" cy="32" r="26" fill="var(--stone-dark)"/><circle cx="32" cy="32" r="19" fill="var(--stone)"/><circle cx="32" cy="32" r="12" fill="var(--good-soft)"/><circle cx="32" cy="32" r="5" fill="var(--night)"/>')
NEXT_I = icon('<rect x="8" y="20" width="14" height="34" fill="var(--stone-dark)"/><path d="M10 28 l10 12 M20 28 l-10 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><rect x="42" y="20" width="14" height="34" fill="var(--stone-dark)"/><path d="M44 36 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M24 37 h14" stroke="var(--bad)" stroke-width="3" stroke-dasharray="3 3"/>')
BELL_I = icon('<path d="M18 40 c0 -26 28 -26 28 0 v8 h-28z" fill="#E9B44C"/><rect x="14" y="48" width="36" height="5" rx="2" fill="#C9822B"/><circle cx="32" cy="57" r="3" fill="#C9822B"/><path d="M12 30 a22 22 0 0 1 6 -16 M52 30 a22 22 0 0 0 -6 -16" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
HOLE_I = icon('<rect x="14" y="10" width="14" height="44" rx="2" fill="var(--stone-dark)"/><circle cx="21" cy="24" r="5" fill="var(--panel)"/><rect x="36" y="10" width="14" height="44" rx="2" fill="var(--stone)"/><circle cx="43" cy="42" r="5" fill="var(--panel)"/>')

PAGE = {
    "slug": "defenseindepth", "order": 102,
    "title": ("겹겹이 두른 성벽", "Walls Within Walls"),
    "h1": ("<em>다층 방어</em>가 뭐예요?", "What is <em>Defense in Depth</em>?"),
    "sub": ("다층 방어(Defense in Depth)를 해자, 성벽, 복도 파수꾼, 경비견, 자물쇠를 겹겹이 두른 성 이야기로 풀어봤어요.",
            "Defense in depth, told as a story about a castle with a moat, walls, hall watchmen, guard dogs, and locks — all layered."),
    "panels": [
        {"svg": P1, "alt": ("성벽 하나에 사다리를 걸치고 올라가는 도둑. 벽 너머로 점선이 곧장 잠긴 금고까지 이어짐", "A thief climbs a ladder against a single wall. Past the wall, a dotted line runs straight to a locked vault"),
         "caption": ("벽이 하나면, 넘으면 끝이에요.", "With one wall, climbing it is the whole game."),
         "small": ("사다리 하나면 돼요. 벽 너머엔 곧장 금고예요 — 아무도 막지 않고, 아무도 몰라요.", "One ladder is all it takes. Past the wall, it\'s straight to the vault — nobody stops it, nobody knows.")},
        {"svg": P2, "alt": ("그림 꼭대기까지 닿는 아주 높은 벽. 그래도 도둑은 땅굴을 파고, 가짜 편지는 문으로 들어와 하녀 손에 있으며, 종은 조용함", "A wall so tall it reaches the top of the picture. Still, a thief digs a tunnel, a fake letter walks in through the door into the maid\'s hands, and the bell stays silent"),
         "caption": ("벽을 높여도 길은 하나가 아니에요.", "A taller wall is still just one wall."),
         "small": ('도둑은 <a href="phishing-ko.html">가짜 편지</a>로 문을 열게 하거나 땅굴을 파요. 그리고 벽 하나가 뚫리면 종을 울릴 사람이 없어요.',
                   'A thief gets the door opened with a <a href="phishing-en.html">fake letter</a>, or digs under. And when that one wall gives, there\'s no one left to ring the bell.')},
        {"svg": P3, "hero": True, "alt": ("동심원 다섯 층: 바깥부터 해자·성벽, 복도, 경비견, 자물쇠, 사람, 가운데 금고. 옆의 목록이 층마다 누가 지키는지 알려줌 — 성문 검문소, 색 리본과 문지기, 경비견, 열쇠 꾸러미와 봉인, 도둑 수업", "Five concentric rings: moat and wall, halls, guard dogs, locks, people, with the vault at the center. A legend lists who keeps each layer — the gate checkpoint, colored ribbons and doorkeepers, guard dogs, key rings and seals, thief lessons"),
         "caption": ("다층 방어는 성벽을 겹겹이 두르는 거예요.", "Defense in depth is walls within walls."),
         "small": ('바깥은 <a href="firewall-ko.html">성문 검문소</a>, 복도는 <a href="vlan-ko.html">색 리본</a>과 <a href="nac-ko.html">문지기</a>, 방마다 <a href="edr-ko.html">경비견</a>, 상자엔 <a href="rbac-ko.html">열쇠 꾸러미</a>와 <a href="encryption-ko.html">봉인</a>, 그리고 <a href="awareness-ko.html">도둑 수업</a>을 들은 사람들. 하나가 뚫려도 다음이 막아요.',
                   'Outside, the <a href="firewall-en.html">gate checkpoint</a>; in the halls, <a href="vlan-en.html">colored ribbons</a> and <a href="nac-en.html">doorkeepers</a>; a <a href="edr-en.html">guard dog</a> in every room; <a href="rbac-en.html">key rings</a> and <a href="encryption-en.html">seals</a> on the chests; and people who took the <a href="awareness-en.html">thief lessons</a>. One gives, the next holds.'),
         "tricks": (4, [
             (LAYERS_I, ("겹겹이", "Layer on layer"), ("바깥에서 금고까지 다섯 층", "five layers from outside to vault"), "calm"),
             (NEXT_I, ("하나 뚫려도", "One gives"), ("다음 층이 막아요", "the next one holds")),
             (BELL_I, ("층마다 종", "A bell on every layer"), ("들키지 않고 지나긴 어려워요", "hard to pass all of them unseen")),
             (HOLE_I, ("완벽한 층은 없어요", "No perfect layer"), ("그래서 겹치는 거예요", "that\'s why they overlap"), "warm"),
         ])},
        {"svg": P4, "alt": ("시간순 다섯 칸: 밤 1시 도둑이 해자와 성벽을 넘음(×), 1시 5분 복도 파수꾼이 보고 종을 울림, 1시 6분 경비견이 짖음, 1시 8분 잠긴 방문이 안 열림, 경비가 도착하고 금고는 무사함", "Five stops on a timeline: at 1 am the thief clears the moat and wall (×), at 1:05 a hall watchman spots him and rings the bell, at 1:06 a dog barks, at 1:08 a locked door won\'t open, guards arrive and the vault is safe"),
         "caption": ("층마다 시간을 벌고, 층마다 종이 울려요.", "Every layer buys time, and every layer can ring the bell."),
         "small": ('해자를 넘은 도둑은 <a href="ndr-ko.html">복도 파수꾼</a>에게 들키고, <a href="edr-ko.html">경비견</a>이 짖고, 방문은 잠겨 있어요. 그 사이 <a href="soc-ko.html">경비실</a>이 달려와요.',
                   'The thief who cleared the moat is spotted by the <a href="ndr-en.html">hall watchman</a>, the <a href="edr-en.html">dog</a> barks, and the door is locked. Meanwhile the <a href="soc-en.html">guard room</a> is on its way.')},
        {"svg": P5, "alt": ("구멍이 하나씩 뚫린 판자 네 장(해자, 복도, 경비견, 자물쇠)이 나란히 서 있고, 구멍의 높이가 다 달라 도둑의 점선이 첫 번째나 두 번째 판자에서 막힘. 오른쪽에 금고", "Four slabs standing in a row — moat, halls, dogs, locks — each with one hole, all at different heights, so the thieves\' dotted lines stop at the first or second slab. The vault is on the right"),
         "caption": ("층마다 구멍이 있어요. 그래서 겹치는 거예요.", "Every layer has a hole. That\'s why they overlap."),
         "small": ('어느 층도 완벽하지 않아요 — 구멍이 한 줄로 서지만 않으면 돼요. 요즘 성은 여기에 <a href="zerotrust-ko.html">문마다 물어보기</a>까지 더해요. 어느 약속을 지키는지는 <a href="ciatriad-ko.html">세 가지 약속</a>에서 봐요.',
                   'No layer is perfect — the holes just must never line up. Modern castles add <a href="zerotrust-en.html">asking at every door</a> on top. Which promise each layer keeps is in the <a href="ciatriad-en.html">three promises</a>.')},
    ],
    "summary": (("<b>다층 방어</b> = 성벽 하나에 기대지 않고 해자·복도·경비견·자물쇠·사람을 <b>겹겹이</b> 두어, <b>하나가 뚫려도 다음이 막고</b> 그 사이 <b>종이 울리게</b> 하는 것.",
                 "<b>Defense in depth</b> = never lean on one wall; layer the moat, halls, dogs, locks, and people so that <b>when one gives, the next holds</b> — and the <b>bell rings</b> in between."),
                ("Defense in Depth. 경계(방화벽·WAF), 네트워크(VLAN·NAC), 엔드포인트(EDR·백신), 데이터(암호화·접근 통제), 사람(보안 교육)처럼 여러 계층에 서로 독립적인 통제를 겹쳐 두어, 한 통제가 실패해도 공격이 끝까지 가지 못하게 하고 탐지 기회를 늘리는 원칙이에요.",
                 "A principle of stacking independent controls across layers — perimeter (firewall, WAF), network (VLAN, NAC), endpoint (EDR, antivirus), data (encryption, access control), people (awareness) — so that a single failed control doesn\'t let an attack through, and every layer adds a chance to detect it.")),
    "glossary": [
        ("다층 방어", "Defense in depth", ("겹겹이 두른 성벽.", "Walls within walls."), ("하나가 뚫려도 다음이 막아요. 층은 서로 다른 방법으로 지켜야 해요 — 같은 벽 두 개는 한 층이에요.", "One gives, the next holds. Each layer must guard a different way — two of the same wall are still one layer.")),
        ("단일 실패점", "Single point of failure", ("벽 하나.", "The one wall."), ("그게 뚫리면 끝인 자리. 다층 방어는 이걸 없애려고 해요.", "The one place that ends everything if it gives. Defense in depth exists to remove it.")),
        ("경계 계층", "Perimeter layer", ("해자와 성문 검문소.", "The moat and the gate checkpoint."), ('마을에서 오는 걸 제일 먼저 걸러요. → <a href="firewall-ko.html">문이 많은 성벽</a>, <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'The first filter for anything from the village. → <a href="firewall-en.html">the wall with many doors</a>, <a href="waf-en.html">the note checker at the counter</a>')),
        ("네트워크 계층", "Network layer", ("복도의 색 리본과 문지기.", "Ribbons and doorkeepers in the halls."), ('안에 들어와도 아무 복도나 못 가요. → <a href="vlan-ko.html">색 리본으로 나눈 복도</a>, <a href="nac-ko.html">복도 구멍마다 문지기</a>', 'Even inside, not every hall is open. → <a href="vlan-en.html">halls divided by ribbon</a>, <a href="nac-en.html">a doorkeeper at every socket</a>')),
        ("엔드포인트 계층", "Endpoint layer", ("방마다 경비견.", "A dog in every room."), ('방 안에서 이상한 걸 잡아요. → <a href="edr-ko.html">방마다 한 마리 경비견</a>, <a href="antivirus-ko.html">벌레 그림 카드를 든 경비</a>', 'Catches trouble inside the room. → <a href="edr-en.html">a guard dog in every room</a>, <a href="antivirus-en.html">the guard with bug cards</a>')),
        ("데이터 계층", "Data layer", ("상자의 자물쇠와 봉인.", "Locks and seals on the chests."), ('방까지 와도 상자는 못 열어요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>, <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'Reach the room, and the chest still won\'t open. → <a href="encryption-en.html">the letter no one reads without the key</a>, <a href="rbac-en.html">a key ring for every hat</a>')),
        ("사람 계층", "Human layer", ("도둑 수업 들은 사람들.", "People who took the thief lessons."), ('마지막 층은 가짜 편지를 알아보는 눈이에요. → <a href="awareness-ko.html">성 사람 모두가 듣는 도둑 수업</a>', 'The last layer is an eye that spots the fake letter. → <a href="awareness-en.html">thief lessons for everyone</a>')),
        ("제로 트러스트", "Zero trust", ("층 안에서도 안 믿기.", "Trusting no one, even inside a layer."), ('겹겹이 두른 다음, 문마다 다시 물어요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'After the layers, ask again at every door. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
    ],
}
