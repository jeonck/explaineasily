from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
WORKER = dict(hat="var(--accent)", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def wall(x, y, w, h, crack=None, patch=False, old=False):
    fill = "var(--stone)" if old else "var(--stone-dark)"
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>{battlements(x, y - 18, w, max(3, int(w / 40)), fill, 20)}'
    if crack:
        cx, cy = crack
        out += f'<path d="M{cx} {cy} l6 14 l-8 12 l10 16 l-6 14" stroke="#0A1120" stroke-width="4" fill="none" stroke-linecap="round"/>'
        if patch:
            out += f'<rect x="{cx - 18}" y="{cy - 6}" width="36" height="68" rx="2" fill="#8B5E3C"/><circle cx="{cx - 10}" cy="{cy + 2}" r="2" fill="var(--night)"/><circle cx="{cx + 10}" cy="{cy + 54}" r="2" fill="var(--night)"/>'
    return out


def board(x, y, s=1.0, rot=0, tag=""):
    t = (f'<rect x="-30" y="-50" width="60" height="18" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5"/>' + label(0, -37, tag, 9, "#142033")) if tag else ""
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-18" y="-34" width="36" height="68" rx="2" fill="#8B5E3C"/><path d="M-18 -20 h36 M-18 10 h36" stroke="#5A3B22" stroke-width="2"/>{t}</g>'


HAMMER = '<g transform="translate(66,50) rotate(-30)"><rect x="-4" y="-22" width="8" height="44" rx="2" fill="#8B5E3C"/><rect x="-14" y="-30" width="28" height="12" rx="3" fill="var(--stone-dark)"/></g>'
CART = '<g transform="translate(0,0)"><rect x="-60" y="-10" width="120" height="30" rx="4" fill="#5A3B22"/><circle cx="-40" cy="28" r="10" fill="var(--night)"/><circle cx="40" cy="28" r="10" fill="var(--night)"/></g>'

# 1. 목수가 판자를 보내온다
P1 = svg(300, sky(300) + person(60, 110, s=0.9, face=SMILE, **BUILDER) + label(90, 250, "⟦목수|the builder⟧", 13, "var(--ink)", cls="d")
         + f'<g transform="translate(300,200)">{CART}</g>' + board(270, 160, 0.8, -8, "CVE-2024-1234") + board(330, 158, 0.8, 5, "CVE-2024-5678")
         + '<path d="M400 200 L520 200" stroke="var(--accent)" stroke-width="3"/><path d="M510 190 L522 200 L510 210" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + castle(540, 100, 0.35)
         + label(380, 280, "⟦틈을 찾을 때마다 덧댈 판자를 만들어 보내요 — 매달, 급하면 바로|for every crack found, a board arrives — monthly, or at once if urgent⟧", 12, "var(--muted)"))

# 2. 판자는 왔는데 아무도 안 붙인다
PILE = "".join(board(80 + (i % 4) * 30, 220 - (i // 4) * 18, 0.7, (i * 7) % 20 - 10) for i in range(8))
DUST = '<path d="M60 150 q10 -10 20 0 M100 140 q10 -10 20 0 M150 155 q10 -10 20 0" stroke="var(--stone)" stroke-width="2" fill="none"/>'
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + wall(360, 80, 400, 220, crack=(620, 150)) + PILE + DUST
         + label(120, 275, "⟦먼지 쌓인 판자 더미|a dusty pile of boards⟧", 12, "var(--bad)")
         + person(260, 90, s=0.85, face=FROWN, **WORKER)
         + bubble(200, 20, 200, 34, "⟦나중에… 지금 바쁜데|later… I\'m busy right now⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(560, 60, "⟦틈은 그대로|the crack stays⟧", 13, "var(--bad)"))

# 3. 패치 = 판자를 제때 붙이는 일 (hero)
CHECK = ('<g transform="translate(40,40)"><rect width="200" height="120" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + "".join(f'<path d="M14 {26 + i * 26} l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none"/>' + label(40, 32 + i * 26, t, 13, "#142033", "start")
                   for i, t in enumerate(("⟦어느 벽에 틈이 있나|which walls have cracks⟧", "⟦급한 것부터|urgent ones first⟧", "⟦작은 벽에 먼저|small wall first⟧", "⟦붙였는지 확인|check it\'s on⟧"))) + "</g>")
P3 = svg(340, sky(340) + wall(360, 80, 400, 260, crack=(620, 150), patch=True)
         + person(520, 110, s=0.9, face=SMILE, **WORKER, extra=HAMMER) + label(550, 255, "⟦붙이는 사람|the one who nails it on⟧", 12, "#F5E6B8")
         + CHECK
         + label(380, 322, "⟦판자를 받는 게 아니라 붙이는 것까지가 패치예요|receiving the board isn\'t the patch — nailing it on is⟧", 13, "var(--muted)"))

# 4. 붙이는 날을 정한다
CAL = ('<g transform="translate(150,90)"><rect x="-90" y="-60" width="180" height="150" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="-90" y="-60" width="180" height="30" rx="8" fill="var(--accent)"/>'
       + label(0, -40, "⟦이번 달|this month⟧", 13, "#FFF")
       + "".join(f'<rect x="{-78 + (i % 7) * 24}" y="{-18 + (i // 7) * 24}" width="18" height="18" rx="3" fill="{"var(--accent)" if i == 9 else "var(--line)"}"/>' for i in range(28))
       + label(0, 110, "⟦둘째 화요일: 판자 붙이는 날|second Tuesday: patch day⟧", 12, "var(--ink)") + "</g>")
P4 = svg(320, '<rect width="380" height="320" fill="var(--sky)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>' + CAL
         + label(190, 300, "⟦정한 날에 모아서 붙여요|nail them on together, on the set day⟧", 12, "var(--muted)")
         + board(470, 120, 1.0, -6, "⟦급함!|URGENT!⟧") + person(560, 60, s=0.6, face=MASK) + label(580, 175, "⟦도둑이 이미 쓰는 틈|a crack thieves already use⟧", 11, "var(--bad)")
         + '<path d="M510 200 L620 200" stroke="var(--bad)" stroke-width="3"/><path d="M610 190 L622 200 L610 210" stroke="var(--bad)" stroke-width="3" fill="none"/>' + label(565, 230, "⟦오늘 바로|today, right now⟧", 13, "var(--bad)", cls="d")
         + label(570, 300, "⟦급한 판자는 그날을 안 기다려요|urgent boards don\'t wait for the day⟧", 12, "var(--muted)"))

# 5. 판자가 안 맞는 벽도 있다
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + wall(40, 100, 200, 220, crack=(180, 160), old=True) + label(140, 70, "⟦오래된 창고|the old storehouse⟧", 13, "var(--ink)")
         + board(270, 160, 0.9, 20) + label(270, 230, "⟦안 맞아요|doesn\'t fit⟧", 12, "var(--bad)")
         + person(140, 190, s=0.6, face=EYES, **GUARD) + label(120, 300, "⟦그 틈 앞에 문지기를 세워요|so a guard stands at that crack⟧", 12, "var(--muted)")
         + wall(420, 100, 120, 220, crack=(500, 160), patch=True) + label(480, 70, "⟦작은 벽|the small wall⟧", 12, "var(--ink)")
         + '<path d="M470 175 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" transform="translate(-30,60)"/>'
         + wall(580, 100, 160, 220, crack=(700, 160), patch=True)
         + '<rect x="690" y="240" width="40" height="70" fill="var(--night)"/><path d="M680 230 l60 60 M740 230 l-60 60" stroke="var(--bad)" stroke-width="4"/>' + label(660, 70, "⟦문까지 막혔어요|it blocked the door too⟧", 12, "var(--bad)")
         + label(570, 300, "⟦그래서 작은 벽에서 먼저 시험해요|which is why the small wall goes first⟧", 12, "var(--muted)"))

SCAN_I = icon('<rect x="8" y="14" width="30" height="36" fill="var(--stone-dark)"/><path d="M22 14 l3 8 l-4 6 l5 8 l-3 8" stroke="#0A1120" stroke-width="2" fill="none"/><circle cx="44" cy="30" r="10" fill="none" stroke="var(--night)" stroke-width="3"/><path d="M51 37 l7 7" stroke="var(--night)" stroke-width="4" stroke-linecap="round"/>')
URGENT_I = icon('<rect x="20" y="10" width="24" height="44" rx="2" fill="#8B5E3C"/><circle cx="46" cy="16" r="9" fill="var(--bad)"/><text x="46" y="21" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF">!</text>')
SMALL_I = icon('<rect x="8" y="30" width="20" height="24" fill="var(--stone-dark)"/><rect x="34" y="14" width="24" height="40" fill="var(--stone)"/><path d="M12 42 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
VERIFY_I = icon('<rect x="10" y="14" width="44" height="40" fill="var(--stone-dark)"/><rect x="26" y="12" width="14" height="44" rx="2" fill="#8B5E3C"/><circle cx="46" cy="46" r="10" fill="var(--good)"/><path d="M41 46 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none"/>')

PAGE = {
    "slug": "patch", "order": 42,
    "title": ("목수가 보낸 판자", "The Board from the Builder"),
    "h1": ("<em>패치</em>가 뭐예요?", "What is a <em>Patch</em>?"),
    "sub": ("패치(Patch)를 목수가 보내온 판자를 성벽 틈에 붙이는 이야기로 풀어봤어요.",
            "Patching, told as a story about nailing the builder's boards over the cracks in the wall."),
    "panels": [
        {"svg": P1, "alt": ("목수가 CVE 번호표가 붙은 판자를 수레에 실어 성으로 보냄", "The builder sends a cart of boards, each tagged with a CVE number, toward the castle"),
         "caption": ("목수가 판자를 보내와요.", "The builder sends boards."),
         "small": ('<a href="zeroday-ko.html">틈</a>을 찾을 때마다 덧댈 판자를 만들어 보내요. 매달 한 번, 급하면 바로.',
                   'For every <a href="zeroday-en.html">crack</a> found, a board to cover it. Monthly — or at once if it\'s urgent.')},
        {"svg": P2, "alt": ("먼지 쌓인 판자 더미, '나중에… 지금 바쁜데' 하는 일꾼, 틈이 그대로인 성벽", "A dusty pile of boards, a worker saying later… I'm busy, and the wall with its crack untouched"),
         "caption": ("판자는 왔는데 아무도 안 붙여요.", "The boards arrive, and nobody nails them on."),
         "small": ("'나중에', '바쁜데', '붙이면 뭐 고장 나면 어떡해'. 판자 더미만 쌓여요.", "'Later', 'I'm busy', 'what if it breaks something'. The pile just grows.")},
        {"svg": P3, "hero": True, "alt": ("망치를 든 일꾼이 틈에 판자를 붙이고, 옆에 '어느 벽에 틈이 있나, 급한 것부터, 작은 벽에 먼저, 붙였는지 확인' 목록", "A worker with a hammer nails a board over the crack; a checklist beside reads which walls have cracks, urgent ones first, small wall first, check it's on"),
         "caption": ("패치는 판자를 제때 붙이는 일이에요.", "Patching is nailing the board on in time."),
         "small": ("판자를 받는 게 아니라 붙이는 것까지가 패치예요. 급한 것부터, 작은 벽에서 시험하고, 붙였는지 확인해요.", "Receiving the board isn't the patch; nailing it on is. Urgent ones first, test on a small wall, then check it's really on."),
         "tricks": (4, [
             (SCAN_I, ("틈 찾기", "Finding cracks"), ("벽마다 돋보기", "a magnifying glass on every wall"), "calm"),
             (URGENT_I, ("급한 것부터", "Urgent first"), ("도둑이 이미 쓰는 틈", "cracks thieves already use")),
             (SMALL_I, ("작은 벽에 먼저", "Small wall first"), ("문까지 막지 않나 시험", "test it doesn\'t block the door"), "warm"),
             (VERIFY_I, ("붙였나 확인", "Check it\'s on"), ("붙였다고 믿지 말고 봐요", "don\'t assume — look"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 둘째 화요일이 표시된 달력. 오른쪽: '급함!' 판자와 도둑이 이미 쓰는 틈, '오늘 바로'", "Left: a calendar with the second Tuesday marked. Right: an URGENT! board, a thief already using the crack, today, right now"),
         "caption": ("붙이는 날을 정해두면 쌓이지 않아요.", "Set a patch day, and the pile never grows."),
         "small": ("매달 정한 날에 모아서 붙여요. 도둑이 이미 쓰는 틈은 그날을 안 기다려요.", "Nail them on together on the set day each month. Cracks thieves are already using don't wait for that day.")},
        {"svg": P5, "alt": ("왼쪽: 판자가 안 맞는 오래된 창고 틈 앞에 문지기. 오른쪽: 작은 벽엔 판자가 잘 붙었지만 큰 벽에선 판자가 문까지 막아버림", "Left: a guard at the crack of an old storehouse the board won't fit. Right: the board fits the small wall, but on the big wall it blocked the door too"),
         "caption": ("판자가 안 맞는 벽도 있어요.", "Some walls won't take the board."),
         "small": ('오래된 창고엔 판자가 안 맞아요. 그럼 그 틈 앞에 <a href="waf-ko.html">문지기</a>를 세우고 <a href="vlan-ko.html">복도를 나눠요</a>. 판자가 문까지 막아버릴 때도 있어서, 작은 벽에서 먼저 시험해요.',
                   'Old storehouses won\'t take it. Then a <a href="waf-en.html">guard</a> stands at that crack and the <a href="vlan-en.html">hallway is split</a>. And a board can block a door too — so the small wall goes first.')},
    ],
    "summary": (("<b>패치</b> = 목수가 보낸 <b>판자</b>를 성벽 틈에 <b>제때 붙이는</b> 일. 받는 게 아니라 붙이는 것까지.",
                 "A <b>patch</b> = the builder's <b>board</b>, <b>nailed on in time</b>. It counts when it's on the wall, not when it arrives."),
                ("Patch. 대부분의 사고는 판자가 있는데 안 붙인 틈으로 시작해요. 붙이는 날(Patch Tuesday), 급한 것부터(KEV), 작은 벽에서 시험(스테이징), 그리고 확인.",
                 "Most incidents start at a crack that already had a board. Patch day (Patch Tuesday), urgent first (KEV), test on a small wall (staging), then verify.")),
    "glossary": [
        ("패치", "Patch", ("판자.", "The board."), ('목수(만든 회사)가 틈을 막으라고 보내는 덧댐. → <a href="zeroday-ko.html">아무도 모르는 구멍</a>', 'The fix the builder (the vendor) sends to cover a crack. → <a href="zeroday-en.html">the hole nobody knows about</a>')),
        ("패치 관리", "Patch management", ("판자 붙이는 순서와 날.", "The order and the day for boards."), ("어느 벽에 뭘 언제 붙일지 정하는 일 전체.", "Deciding what goes on which wall, and when.")),
        ("취약점 스캔", "Vulnerability scan", ("벽마다 돋보기.", "A magnifying glass on every wall."), ("우리 성에 어떤 틈이 있는지 목록을 만들어요.", "Builds the list of which cracks our castle has.")),
        ("우선순위 (CVSS · KEV)", "Prioritization (CVSS · KEV)", ("급한 판자.", "The urgent board."), ("틈이 얼마나 큰지(CVSS), 도둑이 이미 쓰는지(KEV)로 순서를 정해요.", "Ordered by how big the crack is (CVSS) and whether thieves already use it (KEV).")),
        ("스테이징", "Staging", ("작은 벽.", "The small wall."), ("먼저 붙여보고 문이 막히지 않나 보는 곳.", "Where a board goes first, to see it doesn\'t block a door.")),
        ("패치 화요일", "Patch Tuesday", ("붙이는 날.", "Patch day."), ("매달 둘째 화요일에 목수들이 판자를 한꺼번에 보내요.", "The second Tuesday each month, when builders ship boards together.")),
        ("가상 패치", "Virtual patch", ("틈 앞 문지기.", "A guard at the crack."), ('판자가 안 맞거나 아직 없을 때. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'When the board won\'t fit or doesn\'t exist yet. → <a href="waf-en.html">the note checker</a>')),
        ("레거시", "Legacy", ("판자 안 맞는 오래된 창고.", "The old storehouse that takes no board."), ('목수가 더는 판자를 안 만들어요. → <a href="nac-ko.html">이름표 못 다는 물건</a>', 'The builder no longer makes boards for it. → <a href="nac-en.html">the things that can\'t wear a tag</a>')),
    ],
}
