from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
BLUE_W = dict(hat="#5B8DEF", shirt="#4A5A72")
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)
HAMMER = '<g transform="translate(58,54) rotate(-30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#5A3B22"/><rect x="-12" y="-8" width="24" height="12" rx="2" fill="var(--stone-dark)"/></g>'
SPYGLASS = '<g transform="translate(56,52) rotate(-35)"><rect x="-4" y="0" width="8" height="30" rx="3" fill="#5A3B22"/><rect x="-6" y="-8" width="12" height="10" rx="2" fill="#C9A86A"/></g>'
LANTERN = '<g transform="translate(62,60)"><path d="M-6 -16 h12 M0 -16 v-8" stroke="#5A3B22" stroke-width="3"/><rect x="-9" y="-14" width="18" height="22" rx="3" fill="#F5E6B8" stroke="#5A3B22" stroke-width="3"/><rect x="-4" y="-7" width="8" height="8" fill="#E9B44C"/></g>'


def crack(x, y, s=1.0, color="var(--bad)"):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0 0 l6 14 l-4 10 l8 16 l-3 12" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'


def note(x, y, s=1.0, rot=0, color="#C9A86A"):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-22" y="-16" width="44" height="32" rx="3" fill="#FFF8E7" stroke="{color}" stroke-width="2"/>'
            f'<path d="M-14 -6 h28 M-14 2 h20 M-14 10 h12" stroke="{color}" stroke-width="2" stroke-linecap="round"/></g>')


def ledger(x, y, w, h, rows, s=1.0, title="⟦틈 장부|CRACK LEDGER⟧", cols=None):
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, r in enumerate(rows):
        yy = 50 + i * 24
        if isinstance(r, tuple):
            txt, color = r
            out += f'<circle cx="18" cy="{yy - 4}" r="6" fill="{color}"/>' + label(32, yy, txt, 11, "#142033", "start")
        else:
            out += label(14, yy, r, 11, "#142033", "start")
    return out + "</g>"


def board(x, y, rot=-20):
    return f'<rect x="{x}" y="{y}" width="40" height="8" fill="#C9A86A" transform="rotate({rot} {x + 20} {y + 4})"/>'


# 1. 틈 소식이 사방에서 와요 — 흩어진 채로
P1 = svg(320, sky(320) + castle(230, 30, 0.65)
         + person(40, 200, s=0.6, face=EYES, extra=SPYGLASS, **BLUE) + note(110, 230, 0.8, -15) + label(80, 300, "⟦망루 친구 소식|word from the watchtower⟧", 10, "var(--muted)")
         + person(180, 200, s=0.6, hat=None, shirt="#2E7D6B", face=SMILE) + note(250, 230, 0.8, 10) + label(220, 300, "⟦바운티 쪽지|a bounty note⟧", 10, "var(--muted)")
         + person(330, 200, s=0.6, **HIRED) + note(400, 230, 0.8, -8) + label(370, 300, "⟦고용한 도둑 보고서|the hired thief\'s report⟧", 10, "var(--muted)")
         + person(480, 200, s=0.6, face=SMILE, extra=HAMMER, **BLUE_W) + note(550, 230, 0.8, 12) + label(520, 300, "⟦목수의 새 판자 알림|the carpenter\'s new boards⟧", 10, "var(--muted)")
         + person(650, 200, s=0.6, face=FROWN + SWEAT, **GUARD) + bubble(590, 130, 150, 34, "⟦다 합치면 몇 개지?|how many in all?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + crack(300, 110, 0.6) + crack(420, 90, 0.5) + crack(360, 130, 0.5))

# 2. 다 한꺼번에 못 고쳐요 — 아무거나 고치면 금고 옆이 남아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(crack(40 + (i % 12) * 28, 40 + (i // 12) * 45, 0.45, "var(--bad)" if i not in (5, 19, 30) else "var(--stone-dark)") for i in range(36))
         + label(190, 240, "⟦틈 200개|200 cracks⟧", 14, "var(--ink)", cls="d")
         + person(430, 100, s=0.7, face=FROWN + SWEAT, extra=HAMMER, **BLUE_W) + person(510, 110, s=0.7, face=FROWN + SWEAT, extra=HAMMER, **BLUE_W) + label(490, 240, "⟦목수 둘|two carpenters⟧", 14, "var(--ink)", cls="d")
         + '<g transform="translate(640,80)"><rect x="-30" y="-14" width="60" height="40" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/><rect x="-6" y="0" width="12" height="10" rx="2" fill="#E9B44C"/></g>' + crack(675, 60, 0.8) + label(655, 150, "⟦금고 옆 틈은 그대로|the crack by the vault, untouched⟧", 10, "var(--bad)")
         + label(380, 282, "⟦보이는 순서대로 고치면 제일 위험한 게 남아요|fix in the order you see them, and the most dangerous one is left⟧", 12, "var(--muted)"))

# 3. 틈 장부 — 돌고 도는 다섯 걸음 (hero)
STEPS = (("⟦순찰|patrol⟧", "var(--accent)", 380, 50), ("⟦적기|write down⟧", "var(--accent)", 570, 130), ("⟦줄 세우기|line up⟧", "var(--bad)", 510, 255), ("⟦판자|board up⟧", "var(--good)", 250, 255), ("⟦다시 확인|check again⟧", "var(--good)", 190, 130))
P3 = svg(360, sky(360)
         + '<ellipse cx="380" cy="155" rx="195" ry="105" fill="none" stroke="var(--stone-dark)" stroke-width="4" stroke-dasharray="10 8"/>'
         + '<path d="M480 62 l14 -4 l-4 14" stroke="var(--stone-dark)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + "".join(f'<circle cx="{x}" cy="{y}" r="24" fill="{c}"/>' + label(x, y + 42, t, 12, "var(--ink)", cls="d") for t, c, x, y in STEPS)
         + f'<g transform="translate(380,50)">{LANTERN.replace("translate(62,60)", "translate(0,2) scale(0.8)")}</g>'
         + '<g transform="translate(570,130)"><rect x="-12" y="-14" width="24" height="28" rx="2" fill="#FFF8E7"/><path d="M-6 -6 h12 M-6 0 h12 M-6 6 h8" stroke="#C9A86A" stroke-width="2"/></g>'
         + '<g transform="translate(510,255)"><rect x="-14" y="-10" width="28" height="5" fill="#FFF"/><rect x="-14" y="-2" width="20" height="5" fill="#FFF"/><rect x="-14" y="6" width="12" height="5" fill="#FFF"/></g>'
         + '<g transform="translate(250,255)"><rect x="-14" y="-4" width="28" height="7" fill="#FFF8E7" transform="rotate(-20)"/></g>'
         + '<g transform="translate(190,130)"><path d="M-8 0 l6 6 l10 -12" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
         + ledger(300, 100, 160, 110, (("⟦금고 방 틈|vault room⟧", "var(--bad)"), ("⟦서쪽 창문|west window⟧", "var(--accent)"), ("⟦빈 창고|empty shed⟧", "var(--good)")), 1.0)
         + label(380, 340, "⟦끝이 아니라 둘레예요 — 매달 다시 돌아요|not a line but a circle — around again every month⟧", 12, "var(--muted)"))

# 4. 줄 세우기: 크기 × 도둑이 쓰는지 × 뭐 옆인지
P4 = svg(320, sky(320)
         + '<rect x="40" y="40" width="330" height="200" rx="8" fill="var(--bad-soft)"/>' + crack(90, 70, 1.3) + '<g transform="translate(150,110)"><rect x="-30" y="-14" width="60" height="40" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/><rect x="-6" y="0" width="12" height="10" rx="2" fill="#E9B44C"/></g>'
         + person(230, 60, s=0.6, face=MASK) + label(260, 150, "⟦도둑들이 요즘 쓰는 틈|thieves use it these days⟧", 10, "var(--bad)")
         + label(205, 190, "⟦작은 틈 + 금고 옆 + 도둑이 씀|small crack + by the vault + thieves use it⟧", 11, "var(--ink)") + label(205, 220, "⟦→ 1번|→ first⟧", 16, "var(--bad)", cls="d")
         + '<rect x="400" y="40" width="320" height="200" rx="8" fill="var(--good-soft)"/>' + crack(450, 60, 1.8) + '<g transform="translate(560,110)"><rect x="-40" y="-30" width="80" height="60" rx="3" fill="var(--stone)"/><rect x="-10" y="0" width="20" height="30" fill="var(--stone-dark)"/></g>'
         + label(560, 160, "⟦빈 창고|an empty shed⟧", 10, "var(--muted)")
         + label(560, 190, "⟦큰 틈 + 아무것도 없음 + 아무도 안 씀|big crack + nothing inside + nobody uses it⟧", 11, "var(--ink)") + label(560, 220, "⟦→ 나중|→ later⟧", 16, "var(--good)", cls="d")
         + label(380, 280, "⟦틈 크기만 보지 않아요 — 뭐 옆인지, 도둑이 실제로 쓰는지도 봐요|it\'s not just the size — what it\'s next to, and whether thieves actually use it⟧", 12, "var(--ink)")
         + label(380, 304, "⟦목수 둘이면 1번부터|with two carpenters, start at number one⟧", 11, "var(--muted)"))

# 5. 매달 돌면 장부가 짧아져요 — 새 틈은 계속 생기지만
BARS = (62, 48, 40, 30, 26, 20)
P5 = svg(300, sky(300)
         + '<g transform="translate(80,40)"><rect width="320" height="200" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + "".join(f'<rect x="{24 + i * 48}" y="{180 - h * 2.4}" width="30" height="{h * 2.4}" rx="3" fill="{"var(--bad)" if i < 3 else "var(--good)"}"/>' + label(39 + i * 48, 194, f"{i + 1}⟦월|⟧", 10, "var(--muted)") for i, h in enumerate(BARS))
         + "".join(f'<rect x="{24 + i * 48}" y="{180 - h * 2.4 - 14}" width="30" height="12" rx="2" fill="var(--accent)"/>' for i, h in enumerate(BARS))
         + label(160, 24, "⟦장부에 남은 틈|cracks left in the ledger⟧", 11, "var(--ink)", cls="d") + '<rect x="230" y="14" width="12" height="10" fill="var(--accent)"/>' + label(280, 24, "⟦이달 새 틈|new this month⟧", 10, "var(--muted)") + "</g>"
         + person(470, 120, s=0.7, face=SMILE, extra=LANTERN, **GUARD) + person(560, 130, s=0.7, face=SMILE, extra=HAMMER, **BLUE_W) + castle(600, 60, 0.32)
         + label(560, 250, "⟦매달 같은 길을 돌아요|the same round, every month⟧", 12, "var(--ink)", cls="d")
         + label(380, 282, "⟦새 틈은 계속 생겨요 — 그래서 한 번이 아니라 늘 하는 일이에요|new cracks keep coming — that\'s why it\'s not a one-time job but an always job⟧", 11, "var(--muted)"))

PATROL_I = icon('<path d="M26 8 h12 M32 8 v-4" stroke="#5A3B22" stroke-width="3"/><rect x="20" y="10" width="24" height="30" rx="3" fill="#F5E6B8" stroke="#5A3B22" stroke-width="3"/><rect x="27" y="20" width="10" height="10" fill="#E9B44C"/><path d="M14 52 h36" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="4 4"/>')
LEDGER_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="23" cy="24" r="3" fill="var(--bad)"/><circle cx="23" cy="34" r="3" fill="var(--accent)"/><circle cx="23" cy="44" r="3" fill="var(--good)"/><path d="M30 24 h12 M30 34 h12 M30 44 h8" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
RANK_I = icon('<rect x="12" y="14" width="40" height="8" rx="2" fill="var(--bad)"/><rect x="12" y="28" width="28" height="8" rx="2" fill="var(--accent)"/><rect x="12" y="42" width="16" height="8" rx="2" fill="var(--good)"/>')
AGAIN_I = icon('<path d="M46 32 a14 14 0 1 1 -5 -10.7" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M42 12 l6 10 -12 2z" fill="var(--good)"/><path d="M26 32 l5 5 l9 -10" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "vulnmgmt", "order": 56,
    "title": ("매달 도는 틈 장부", "The Crack Ledger"),
    "h1": ("<em>취약점 관리</em>가 뭐예요?", "What is <em>Vulnerability Management</em>?"),
    "sub": ("취약점 관리(Vulnerability Management)를 성의 틈을 장부에 적고 위험한 순서로 고치며 매달 다시 도는 이야기로 풀어봤어요.",
            "Vulnerability management, told as a story about writing every crack in a ledger, fixing the most dangerous first, and going around again every month."),
    "panels": [
        {"svg": P1, "alt": ("성 앞에 다섯 사람이 각자 쪽지를 들고 있음: 망루 친구, 바운티 쪽지 든 마을 사람, 고용한 도둑, 목수, 그리고 땀 흘리는 경비가 '다 합치면 몇 개지?'", "Five people in front of the castle each holding a note — the watchtower friend, a villager with a bounty note, the hired thief, the carpenter — and a sweating guard asking how many in all"),
         "caption": ("틈 소식이 사방에서 와요. 흩어진 채로요.", "Word of cracks comes from everywhere. All scattered."),
         "small": ('<a href="cti-ko.html">망루 친구</a>, <a href="bugbounty-ko.html">바운티 쪽지</a>, <a href="pentest-ko.html">고용한 도둑</a>, <a href="patch-ko.html">목수</a>. 다 다른 종이에 적혀 있어서, 성에 틈이 모두 몇 개인지 아무도 몰라요.',
                   'The <a href="cti-en.html">watchtower</a>, a <a href="bugbounty-en.html">bounty note</a>, the <a href="pentest-en.html">hired thief</a>, the <a href="patch-en.html">carpenter</a>. All on different slips of paper, so nobody knows how many cracks the castle has.')},
        {"svg": P2, "alt": ("빨간 틈 36개가 벽에 흩어져 있고 '틈 200개', 땀 흘리는 목수 둘, 오른쪽엔 금고 옆에 남은 틈", "Dozens of red cracks on a wall labeled 200 cracks, two sweating carpenters, and on the right a crack still open beside the vault"),
         "caption": ("다 한꺼번에 못 고쳐요. 아무거나 고치면 금고 옆 틈이 남아요.", "You can\'t fix them all at once. Fix at random, and the one by the vault is left."),
         "small": ("틈 200개에 목수는 둘. 보이는 순서대로 고치면 제일 위험한 틈이 맨 나중까지 남아요.", "Two hundred cracks, two carpenters. Fix them in the order you see them, and the most dangerous one waits until last.")},
        {"svg": P3, "hero": True, "alt": ("점선 원을 따라 다섯 걸음: 순찰(랜턴) → 적기(쪽지) → 줄 세우기 → 판자 → 다시 확인. 가운데 틈 장부: 금고 방 틈(빨강), 서쪽 창문(주황), 빈 창고(초록)", "Five steps around a dotted circle: patrol (lantern) → write down → line up → board up → check again. In the middle, the crack ledger: vault room (red), west window (orange), empty shed (green)"),
         "caption": ("취약점 관리는 틈 장부를 들고 매달 같은 둘레를 도는 거예요.", "Vulnerability management is walking the same circle every month with the crack ledger."),
         "small": ("성을 돌며 틈을 찾고, 장부에 다 적고, 위험한 순서로 줄 세우고, 판자를 대고, 다시 돌며 확인해요. 끝이 아니라 둘레예요.", "Walk the castle for cracks, write every one in the ledger, line them up by danger, board them up, and walk again to check. Not a line — a circle."),
         "tricks": (4, [
             (PATROL_I, ("다 찾기", "Find them all"), ("성을 빠짐없이 돌아요", "every wall, every month"), "warm"),
             (LEDGER_I, ("한 장부에", "One ledger"), ("흩어진 쪽지를 모아요", "all the slips in one place")),
             (RANK_I, ("위험한 것부터", "Most dangerous first"), ("크기 × 어디 × 도둑이 쓰는지", "size × where × in use?"), "warm"),
             (AGAIN_I, ("다시 확인", "Check again"), ("판자가 잘 붙었는지", "did the board hold?"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 작은 틈이지만 금고 옆이고 도둑들이 요즘 쓰는 틈 → 1번. 오른쪽: 큰 틈이지만 빈 창고이고 아무도 안 씀 → 나중", "Left: a small crack, but by the vault and one thieves use these days → first. Right: a big crack, but on an empty shed nobody uses → later"),
         "caption": ("줄 세우기는 크기만 보지 않아요.", "Lining them up isn\'t just about size."),
         "small": ('틈이 얼마나 큰지, 뭐 옆인지, <a href="cti-ko.html">도둑들이 요즘 실제로 쓰는지</a>를 같이 봐요. 작은 틈이라도 금고 옆이면 1번이에요.',
                   'How big the crack is, what it\'s next to, and whether <a href="cti-en.html">thieves are actually using it these days</a>. Even a small crack goes first if it\'s by the vault.')},
        {"svg": P5, "alt": ("달마다 낮아지는 막대그래프 — 장부에 남은 틈은 줄고 매달 새 틈(주황)은 조금씩 생김. 옆에서 경비와 목수가 성 둘레를 돎", "A bar chart falling month by month — cracks left in the ledger shrink while a small orange bit of new cracks appears each month. Beside it the guard and carpenter walk the castle round"),
         "caption": ("매달 돌면 장부가 짧아져요. 새 틈은 계속 생기지만요.", "Walk it monthly and the ledger gets shorter. New cracks keep coming, though."),
         "small": ('새 탑이 생기고 새 <a href="zeroday-ko.html">구멍</a>이 발견돼요. 그래서 한 번 하고 끝이 아니라 늘 하는 일이에요.',
                   'New towers go up and new <a href="zeroday-en.html">holes</a> get found. That\'s why it\'s not a one-time job but an always job.')},
    ],
    "summary": (("<b>취약점 관리</b> = 성의 틈을 <b>다 찾아 한 장부에 적고</b>, <b>위험한 순서로 줄 세워</b> 판자를 대고, <b>매달 다시 도는</b> 둘레.",
                 "<b>Vulnerability management</b> = <b>find every crack, write it in one ledger</b>, <b>line them up by danger</b>, board them up, and <b>walk the circle again every month</b>."),
                ("Vulnerability Management. 자산 전체를 스캔해 취약점을 찾고, 심각도·악용 여부·자산 중요도로 우선순위를 매겨 패치하고, 검증 후 반복하는 지속적인 순환이에요.",
                 "A continuous cycle: scan all assets for vulnerabilities, prioritize by severity, active exploitation, and asset importance, patch, verify, and repeat.")),
    "glossary": [
        ("취약점 스캐너", "Vulnerability scanner", ("순찰 도는 랜턴.", "The patrol lantern."), ("성을 빠짐없이 돌며 틈을 찾아 장부에 적어 줘요.", "Walks every wall, finds cracks, and writes them in the ledger for you.")),
        ("자산 목록", "Asset inventory", ("방 목록.", "The list of rooms."), ("모르는 방은 순찰도 못 돌아요. 그래서 장부 첫 장은 '성에 방이 몇 개인가'예요.", "You can\'t patrol a room you don\'t know exists. Page one of the ledger: how many rooms does the castle have?")),
        ("CVE", "CVE", ("틈 번호표.", "The crack\'s number tag."), ("세상 모든 성이 같은 번호로 부르는 틈 이름. 'CVE-2024-1234'.", "A name every castle in the world uses for the same crack: CVE-2024-1234.")),
        ("CVSS", "CVSS", ("틈 크기 점수.", "The crack\'s size score."), ("0부터 10까지. 크기만 말하고, 뭐 옆인지는 말 안 해요.", "From 0 to 10. It tells you the size, not what the crack is next to.")),
        ("KEV · EPSS", "KEV · EPSS", ("도둑이 실제로 쓰는 틈.", "Cracks thieves actually use."), ('큰 틈보다 도둑이 쓰는 틈이 먼저예요. → <a href="cti-ko.html">망루 위의 친구</a>', 'A crack in use beats a big crack. → <a href="cti-en.html">the friend on the watchtower</a>')),
        ("우선순위", "Prioritization", ("줄 세우기.", "Lining up."), ("크기 × 뭐 옆인지 × 도둑이 쓰는지. 목수가 둘이니까요.", "Size × what it\'s next to × whether thieves use it. Because there are only two carpenters.")),
        ("패치", "Patch", ("판자 한 장.", "One board."), ('장부의 한 줄을 지우는 일. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'What crosses one line off the ledger. → <a href="patch-en.html">the boards the carpenter sent</a>')),
        ("SLA", "Remediation SLA", ("며칠 안에.", "Within so many days."), ("1번 틈은 일주일, 나중 틈은 석 달. 미리 약속해 둬요.", "Number one within a week, the later ones within three months. Agreed in advance.")),
    ],
}
