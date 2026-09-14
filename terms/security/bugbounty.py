from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
BLUE_W = dict(hat="#5B8DEF", shirt="#4A5A72")
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)
HAMMER = '<g transform="translate(58,54) rotate(-30)"><rect x="-3" y="0" width="6" height="34" rx="2" fill="#5A3B22"/><rect x="-12" y="-8" width="24" height="12" rx="2" fill="var(--stone-dark)"/></g>'
VILLAGERS = (("#E9B44C", "#4A5A72"), (None, "#7B3FA0"), ("#5B8DEF", "#4A5A72"), (None, "#2E7D6B"), ("var(--stone-dark)", "#4A5A72"), (None, "#C9822B"))


def crack(x, y, s=1.0):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0 0 l6 14 l-4 10 l8 16 l-3 12" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'


def poster(x, y, w, h, s=1.0, title="⟦틈 찾으면 상 드려요|CRACKS WANTED — REWARD⟧", rows=()):
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<circle cx="{w / 2}" cy="0" r="6" fill="var(--stone-dark)"/>' + label(w / 2, 30, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(w / 2, 58 + i * 22, r, 11, "#142033")
    return out + "</g>"


def note(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-22" y="-16" width="44" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-14 -6 h28 M-14 2 h20 M-14 10 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/></g>')


def coins(x, y, n=3, s=1.0):
    return "".join(f'<g transform="translate({x + i * 14},{y - (i % 2) * 6}) scale({s})"><circle r="10" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle r="5" fill="none" stroke="#C9822B" stroke-width="1.5"/></g>' for i in range(n))


def pouch(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-20 0 q-6 30 20 32 q26 -2 20 -32 q-6 -10 -20 -10 q-14 0 -20 10z" fill="#C9822B"/>'
            f'<path d="M-10 -8 q10 -8 20 0" stroke="#5A3B22" stroke-width="3" fill="none"/><rect x="-10" y="-14" width="20" height="8" rx="2" fill="#5A3B22"/>'
            f'<text y="16" text-anchor="middle" font-size="14" font-weight="700" fill="#FFF8E7">$</text></g>')


# 1. 성은 커졌는데 틈 찾는 사람은 둘뿐
P1 = svg(320, sky(320) + castle(30, 40, 0.75) + castle(330, 60, 0.6) + castle(600, 20, 0.35)
         + crack(120, 110, 0.8) + crack(300, 130, 0.7) + crack(450, 150, 0.8) + crack(650, 90, 0.6) + crack(700, 120, 0.7)
         + person(60, 200, s=0.7, face=FROWN + SWEAT, extra=HAMMER, **BLUE_W) + label(90, 300, "⟦목수 한 명|one carpenter⟧", 12, "var(--muted)")
         + person(660, 200, s=0.7, **HIRED) + label(690, 300, "⟦1년에 한 번 오는 도둑|a thief who comes once a year⟧", 12, "var(--muted)")
         + label(380, 280, "⟦성은 자꾸 커지는데, 틈을 찾는 사람은 둘뿐이에요|the castle keeps growing, but only two people look for cracks⟧", 12, "var(--ink)"))

# 2. 마을엔 눈이 수백 개 — 그런데 말할 곳이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + "".join(person(x, 120, s=0.65, hat=h, shirt=sh, face=EYES) for x, (h, sh) in zip((40, 110, 180, 250, 320, 390), VILLAGERS))
         + crack(560, 50, 1.0) + '<rect x="530" y="30" width="70" height="110" rx="4" fill="none" stroke="var(--stone-dark)" stroke-width="3"/>'
         + person(620, 150, s=0.7, hat=None, shirt="#2E7D6B", face=EYES) + bubble(540, 190, 200, 34, "⟦틈을 봤는데… 누구한테 말하지?|I saw a crack… who do I tell?⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(215, 240, "⟦마을엔 눈이 수백 개|hundreds of eyes in the village⟧", 12, "var(--muted)")
         + label(380, 282, "⟦말할 곳이 없으면, 나쁜 시장에 파는 사람도 생겨요|with nowhere to tell, some will sell it at the bad market⟧", 12, "var(--bad)"))

# 3. 성문에 붙은 방 (hero)
P3 = svg(360, sky(360) + gate(380, 120, 1.0)
         + poster(250, 40, 260, 170, 1.0, rows=("⟦누구나 찾아도 돼요|anyone may look⟧", "⟦찾으면 조용히 쪽지로|found one? tell us quietly⟧", "⟦부수지 말고, 상자는 열지 말고|break nothing, open no chests⟧", "⟦확인되면 틈 크기만큼 상|confirmed? reward by size of crack⟧"))
         + "".join(person(x, 230, s=0.6, hat=h, shirt=sh, face=SMILE) for x, (h, sh) in zip((40, 110, 180), VILLAGERS[:3]))
         + "".join(person(x, 230, s=0.6, hat=h, shirt=sh, face=SMILE) for x, (h, sh) in zip((560, 630, 700), VILLAGERS[3:]))
         + label(380, 320, "⟦버그 바운티 = 성문에 붙인 이 방 한 장|a bug bounty is this one poster on the gate⟧", 14, "var(--ink)", cls="d")
         + label(380, 344, "⟦마을 전체가 틈 찾기를 도와요|the whole village helps look for cracks⟧", 12, "var(--muted)"))

# 4. 쪽지 → 확인 → 상 → 판자
P4 = svg(320, sky(320)
         + person(40, 110, s=0.7, hat=None, shirt="#2E7D6B", face=SMILE) + note(120, 150, 1.0, -10) + label(80, 240, "⟦쪽지|the note⟧", 12, "var(--ink)", cls="d")
         + '<path d="M160 150 L210 150" stroke="var(--muted)" stroke-width="3"/><path d="M200 140 L212 150 L200 160" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(230, 110, s=0.7, face=EYES, **BLUE) + '<g transform="translate(300,150)"><circle r="16" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M11 11 l10 10" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/></g>' + label(280, 240, "⟦진짜? 새 틈?|real? new?⟧", 12, "var(--ink)", cls="d")
         + '<path d="M340 150 L390 150" stroke="var(--muted)" stroke-width="3"/><path d="M380 140 L392 150 L380 160" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + coins(420, 120, 3, 0.9) + label(440, 160, "⟦작은 틈|small crack⟧", 10, "var(--muted)") + pouch(510, 110, 0.9) + label(510, 160, "⟦큰 틈|big crack⟧", 10, "var(--muted)") + label(470, 240, "⟦크기만큼 상|reward by size⟧", 12, "var(--ink)", cls="d")
         + '<path d="M560 150 L610 150" stroke="var(--muted)" stroke-width="3"/><path d="M600 140 L612 150 L600 160" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(640, 110, s=0.7, face=SMILE, extra=HAMMER, **BLUE_W) + '<rect x="700" y="120" width="40" height="8" fill="#C9A86A" transform="rotate(-20 720 124)"/>' + label(680, 240, "⟦판자|the board⟧", 12, "var(--ink)", cls="d")
         + label(380, 290, "⟦고칠 때까지 마을엔 비밀 — 그다음엔 자랑해도 돼요|secret from the village until it\'s fixed — then you may brag⟧", 12, "var(--muted)"))

# 5. 마을이 우리 편이 돼요
P5 = svg(300, sky(300) + castle(230, 30, 0.65)
         + "".join(person(x, y, s=0.5, hat=h, shirt=sh, face=SMILE) for (x, y), (h, sh) in zip(((40, 120), (100, 170), (160, 130), (560, 130), (620, 175), (690, 120)), VILLAGERS))
         + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="var(--accent)"/>' for x, y in ((60, 100), (130, 110), (180, 95), (580, 105), (640, 150), (710, 100)))
         + label(380, 235, "⟦성 주변에 눈이 수백 개|hundreds of eyes around the castle⟧", 14, "var(--ink)", cls="d")
         + label(380, 262, "⟦도둑보다 먼저 틈을 보는 사람이 우리 편이에요|the ones who spot a crack before the thief are on our side⟧", 12, "var(--muted)")
         + label(380, 288, "⟦펜테스트는 한 명이 한 번, 바운티는 모두가 늘|a pentest is one person once; a bounty is everyone, always⟧", 11, "var(--muted)"))

ANYONE_I = icon(f'<circle cx="18" cy="24" r="8" fill="{SKIN}"/><circle cx="32" cy="20" r="8" fill="{SKIN}"/><circle cx="46" cy="24" r="8" fill="{SKIN}"/><rect x="10" y="34" width="16" height="18" rx="5" fill="#4A5A72"/><rect x="24" y="30" width="16" height="22" rx="5" fill="#7B3FA0"/><rect x="38" y="34" width="16" height="18" rx="5" fill="#2E7D6B"/>')
NOTE_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 32 h20 M22 40 h12" stroke="#C9A86A" stroke-width="3" stroke-linecap="round"/><path d="M40 8 l8 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
CHECK_I = icon('<circle cx="28" cy="28" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M38 38 l12 12" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M21 28 l5 5 l9 -10" stroke="var(--good)" stroke-width="3" fill="none"/>')
COIN_I = icon('<circle cx="24" cy="36" r="12" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle cx="40" cy="28" r="12" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle cx="40" cy="28" r="6" fill="none" stroke="#C9822B" stroke-width="1.5"/>')

PAGE = {
    "slug": "bugbounty", "order": 55,
    "title": ("성문에 붙인 상금 방", "The Reward Poster on the Gate"),
    "h1": ("<em>버그 바운티</em>가 뭐예요?", "What is a <em>Bug Bounty</em>?"),
    "sub": ("버그 바운티(Bug Bounty)를 성문에 붙인 '틈 찾으면 상 드려요' 방 이야기로 풀어봤어요.",
            "Bug bounties, told as a story about a poster on the castle gate: cracks wanted, reward offered."),
    "panels": [
        {"svg": P1, "alt": ("성 세 채에 빨간 틈이 여기저기. 왼쪽엔 땀 흘리는 목수 한 명, 오른쪽엔 고용한 도둑 한 명", "Three castles with red cracks here and there; one sweating carpenter on the left, one hired thief on the right"),
         "caption": ("성은 자꾸 커지는데, 틈을 찾는 사람은 둘뿐이에요.", "The castle keeps growing, but only two people look for cracks."),
         "small": ('<a href="patch-ko.html">목수</a> 한 명과 1년에 한 번 오는 <a href="pentest-ko.html">고용한 도둑</a>. 새 탑이 생길 때마다 새 틈이 생겨요.',
                   'One <a href="patch-en.html">carpenter</a> and a <a href="pentest-en.html">hired thief</a> who comes once a year. Every new tower brings new cracks.')},
        {"svg": P2, "alt": ("마을 사람 여섯이 서 있고, 한 사람이 벽의 틈을 보며 '틈을 봤는데… 누구한테 말하지?'", "Six villagers stand around; one looks at a crack in the wall and says: I saw a crack… who do I tell?"),
         "caption": ("마을엔 눈이 수백 개예요. 그런데 말할 곳이 없어요.", "The village has hundreds of eyes. But nowhere to tell."),
         "small": ('틈을 본 사람이 말할 곳이 없으면, 그냥 지나가거나 <a href="zeroday-ko.html">나쁜 시장</a>에 팔아요.',
                   'When someone who spots a crack has nowhere to tell, they walk on — or sell it at the <a href="zeroday-en.html">bad market</a>.')},
        {"svg": P3, "hero": True, "alt": ("성문에 붙은 방: 틈 찾으면 상 드려요 — 누구나 찾아도 돼요, 찾으면 조용히 쪽지로, 부수지 말고 상자는 열지 말고, 확인되면 틈 크기만큼 상. 양쪽에 웃는 마을 사람들", "A poster on the gate: cracks wanted, reward — anyone may look, tell us quietly, break nothing and open no chests, confirmed cracks rewarded by size. Smiling villagers on both sides"),
         "caption": ("버그 바운티는 성문에 붙인 방 한 장이에요.", "A bug bounty is one poster on the castle gate."),
         "small": ("누구나 틈을 찾아도 돼요. 찾으면 조용히 쪽지로 알려주고, 확인되면 틈 크기만큼 상을 받아요. 단, 부수지 말고 상자는 열지 말 것.", "Anyone may look for cracks. Tell us quietly with a note, and once confirmed you\'re rewarded by the size of the crack. Just break nothing, and open no chests."),
         "tricks": (4, [
             (ANYONE_I, ("누구나", "Anyone"), ("마을 전체가 찾아요", "the whole village looks"), "warm"),
             (NOTE_I, ("조용히 쪽지로", "A quiet note"), ("소문내기 전에 우리에게", "to us, before the rumor")),
             (CHECK_I, ("확인 먼저", "Confirm first"), ("진짜 틈인지, 새 틈인지", "is it real, is it new?")),
             (COIN_I, ("크기만큼 상", "Reward by size"), ("작은 틈 동전, 큰 틈 주머니", "coins for small, a pouch for big"), "calm"),
         ])},
        {"svg": P4, "alt": ("쪽지 → 경비실 친구가 돋보기로 확인 → 작은 틈엔 동전 몇 개, 큰 틈엔 금화 주머니 → 목수가 판자를 댐", "A note → a blue hat checks with a magnifying glass → coins for a small crack, a pouch for a big one → the carpenter boards it up"),
         "caption": ("쪽지가 오면 확인하고, 상을 주고, 판자를 대요.", "A note comes in: confirm it, pay it, board it up."),
         "small": ('<a href="soc-ko.html">경비실</a>이 진짜 틈인지, 이미 아는 틈인지 봐요. 고칠 때까지는 마을에 비밀이에요 — 그다음엔 찾은 사람이 자랑해도 돼요.',
                   'The <a href="soc-en.html">guard room</a> checks whether it\'s real and whether it\'s already known. It stays secret until fixed — after that, the finder may brag.')},
        {"svg": P5, "alt": ("성 주변에 마을 사람들이 서서 웃고 있고, 머리 위에 주황 점들이 눈처럼 흩어져 있음", "Villagers stand around the castle smiling, with orange dots scattered above like watching eyes"),
         "caption": ("이제 성 주변에 눈이 수백 개예요.", "Now there are hundreds of eyes around the castle."),
         "small": ("도둑보다 먼저 틈을 보는 사람이 우리 편이 돼요. 펜테스트는 한 명이 한 번, 바운티는 모두가 늘.", "The ones who spot a crack before the thief are on our side now. A pentest is one person once; a bounty is everyone, always.")},
    ],
    "summary": (("<b>버그 바운티</b> = 성문에 붙인 방 — <b>누구나</b> 틈을 찾아 <b>조용히 쪽지</b>로 알리면, <b>확인 뒤 크기만큼 상</b>을 주고 판자를 대는 약속.",
                 "<b>Bug bounty</b> = a poster on the gate — <b>anyone</b> who finds a crack and sends a <b>quiet note</b> gets a <b>reward by size once confirmed</b>, and the crack gets boarded up."),
                ("Bug Bounty. 외부 연구자 누구나 취약점을 찾아 정해진 규칙대로 신고하면, 검증 후 심각도에 따라 보상하는 공개 프로그램이에요.",
                 "A public program where any outside researcher can find vulnerabilities, report them under set rules, and be paid by severity once verified.")),
    "glossary": [
        ("버그 바운티", "Bug bounty", ("상금 방.", "The reward poster."), ("틈 하나에 상 하나. 크기가 클수록 커요.", "One reward per crack; the bigger the crack, the bigger the reward.")),
        ("취약점 공개 정책", "Vulnerability disclosure policy", ("상 없는 방.", "The poster without a reward."), ("'틈을 보면 여기로 알려주세요'만 적힌 방. 상금은 없어도 말할 곳은 생겨요.", "A poster that only says where to tell. No money, but now there\'s somewhere to go.")),
        ("범위", "Scope", ("어디까지 찾아도 되나.", "Where you may look."), ("본성은 돼요, 왕의 침실은 안 돼요. 방에 미리 적어둬요.", "The main keep, yes; the king\'s bedroom, no. Written on the poster in advance.")),
        ("책임 있는 공개", "Coordinated disclosure", ("고칠 때까지 비밀.", "Secret until fixed."), ('먼저 우리에게, 판자 댄 뒤에 마을에. → <a href="zeroday-ko.html">아무도 모르는 구멍</a>', 'Us first, the village after the board goes up. → <a href="zeroday-en.html">the hole nobody knows</a>')),
        ("심각도", "Severity", ("틈의 크기.", "Size of the crack."), ("고양이만 드나드는 틈과 도둑이 걸어 들어오는 틈은 상이 달라요.", "A crack a cat fits through and a crack a thief walks through pay differently.")),
        ("중복", "Duplicate", ("이미 받은 쪽지.", "A note we already have."), ("같은 틈은 처음 알린 사람만 상을 받아요.", "Only the first note about a crack gets the reward.")),
        ("바운티 플랫폼", "Bounty platform", ("마을 게시판 관리인.", "The village noticeboard keeper."), ("방을 대신 붙이고, 쪽지를 모아 주고, 상금을 전해 줘요.", "Puts up the poster, collects the notes, and hands over the rewards.")),
        ("펜테스트", "Pentest", ("고용한 도둑 한 명.", "One hired thief."), ('정해진 기간, 정해진 사람. 바운티는 그 반대. → <a href="pentest-ko.html">우리가 고용한 도둑</a>', 'Set time, set person; a bounty is the opposite. → <a href="pentest-en.html">the thief we hired</a>')),
    ],
}
