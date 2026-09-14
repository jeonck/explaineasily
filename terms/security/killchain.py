from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def crown(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 10 l-4 -30 l14 12 l16 -22 l16 22 l14 -12 l-4 30z" fill="#E9B44C" stroke="#C9822B" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="-28" y="8" width="56" height="10" rx="3" fill="#C9822B"/><circle cx="-16" cy="-4" r="3" fill="var(--bad)"/><circle cy="-10" r="3" fill="#5B8DEF"/><circle cx="16" cy="-4" r="3" fill="var(--bad)"/></g>')


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def link(x, y, s=1.0, color="var(--stone-dark)"):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-14" width="44" height="28" rx="14" fill="none" stroke="{color}" stroke-width="7"/></g>'


def scissors(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cx="-10" cy="12" r="7" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="10" cy="12" r="7" fill="none" stroke="var(--bad)" stroke-width="4"/>'
            f'<path d="M-6 6 l14 -30 M6 6 l-14 -30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/></g>')


def book(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="-40" width="120" height="80" rx="6" fill="#7B3FA0"/><rect x="-52" y="-32" width="104" height="64" rx="4" fill="#FFF8E7"/>'
            f'<path d="M0 -32 v64" stroke="#C9A86A" stroke-width="2"/>'
            + "".join(f'<path d="M{-44 + c * 52} {-20 + r * 10} h{28 - (r % 2) * 8}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for c in range(2) for r in range(5)) + "</g>")


STEPS = (("⟦1|1⟧", "⟦정찰|recon⟧"), ("⟦2|2⟧", "⟦무기 만들기|build the weapon⟧"), ("⟦3|3⟧", "⟦전달|delivery⟧"), ("⟦4|4⟧", "⟦틈 이용|use the crack⟧"),
         ("⟦5|5⟧", "⟦자리 잡기|settle in⟧"), ("⟦6|6⟧", "⟦두목과 연락|call the boss⟧"), ("⟦7|7⟧", "⟦목표 달성|take the crown⟧"))

# 1. 왕관이 사라졌어요 — 도둑은 갑자기 나타난 것 같아요
P1 = svg(300, night(300)
         + '<rect x="120" y="170" width="90" height="60" rx="4" fill="var(--stone-dark)"/><path d="M139 165 l-4 -24 l12 10 l18 -20 l18 20 l12 -10 l-4 24z" fill="none" stroke="#F5E6B8" stroke-width="2" stroke-dasharray="4 3"/>'
         + label(165, 258, "⟦왕관이 있던 자리|where the crown was⟧", 11, "#C9D5E6")
         + person(300, 100, s=0.9, face=FROWN + SWEAT, **BLUE) + bubble(250, 24, 200, 34, "⟦언제 들어온 거지?|when did they get in?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(330, 258, "⟦경비실 친구|the guard room friend⟧", 11, "#C9D5E6")
         + person(600, 110, s=0.85, extra=BAG, **THIEF) + crown(690, 150, 0.6)
         + label(640, 258, "⟦도둑은 벌써 성문 밖|the thief is already past the gate⟧", 11, "#C9D5E6")
         + label(380, 288, "⟦도둑이 갑자기 나타난 것 같아요|it looks like the thief came out of nowhere⟧", 13, "#F5E6B8", cls="d"))

# 2. 사실은 그 전에 여섯 걸음이 있었어요 — 성문만 보면 못 봐요
GHOSTS = ("⟦문 세기|counting doors⟧", "⟦벌레 넣기|packing the bug⟧", "⟦편지 보내기|sending the letter⟧", "⟦구멍으로|through the crack⟧", "⟦둥지 틀기|nesting⟧", "⟦신호 보내기|signalling⟧")
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + label(380, 40, "⟦경비실이 본 건 마지막 한 걸음뿐이에요|the guard room only saw the last step⟧", 13, "var(--ink)", cls="d")
         + '<path d="M60 175 H640" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 6" opacity="0.5"/>'
         + "".join(f'<g opacity="0.45">{person(50 + i * 110, 110, s=0.6, **THIEF)}</g>' + label(71 + i * 110, 205, g, 10, "var(--muted)") for i, g in enumerate(GHOSTS))
         + person(690, 100, s=0.7, extra=BAG, **THIEF) + crown(675, 90, 0.4) + label(700, 205, "⟦왕관!|the crown!⟧", 11, "var(--bad)", cls="d")
         + '<rect x="655" y="220" width="90" height="26" rx="6" fill="var(--bad)"/>' + label(700, 238, "⟦이것만 봤어요|only saw this⟧", 10, "#FFF")
         + label(380, 300, "⟦그 전에 여섯 걸음이 있었어요 — 성문만 보면 못 봐요|six steps came before — you can\'t see them from the gate⟧", 12, "var(--ink)"))

# 3. 킬 체인 = 도둑의 일곱 걸음 (hero)
P3 = svg(360, sky(360)
         + '<path d="M70 170 H700" stroke="var(--stone-dark)" stroke-width="5"/>' + "".join(link(70 + i * 105, 170, 1.0, "var(--stone-dark)") for i in range(7))
         + "".join(f'<circle cx="{70 + i * 105}" cy="170" r="18" fill="{"var(--accent)" if i == 6 else "var(--bad)"}"/>' + label(70 + i * 105, 176, n, 16, "#FFF", cls="d") + label(70 + i * 105, 125 + (i % 2) * 90, t, 11, "var(--ink)") for i, (n, t) in enumerate(STEPS))
         + scissors(332, 110, 0.9) + label(332, 74, "⟦여기서 끊으면?|cut here?⟧", 11, "var(--bad)", cls="d")
         + crown(700, 240, 0.6) + label(700, 275, "⟦왕관|the crown⟧", 10, "var(--muted)")
         + small_castle(20, 210, 0.4) + label(52, 288, "⟦마을|the village⟧", 10, "var(--muted)")
         + label(380, 310, "⟦걸음은 늘 이 순서예요 — 하나만 끊어도 왕관은 못 가져가요|the steps always come in this order — cut one and no crown⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦빠른 걸음에서 끊을수록 성은 덜 다쳐요|the earlier the cut, the less the castle gets hurt⟧", 12, "var(--muted)"))

# 4. 걸음마다 끊는 친구가 달라요 (표)
ROWS = (("⟦1 정찰|1 recon⟧", "⟦성 밖에서 문을 세요|counts our doors from outside⟧", "⟦바깥에서 세는 친구|the outside counter⟧"),
        ("⟦2 무기 만들기|2 weaponize⟧", "⟦선물 상자에 벌레를 넣어요|packs a bug in a gift box⟧", "⟦성 밖이라 못 봐요|too far away to see⟧"),
        ("⟦3 전달|3 delivery⟧", "⟦우체국인 척 편지를 보내요|sends a letter posing as the post⟧", "⟦편지 검토원|the letter checker⟧"),
        ("⟦4 틈 이용|4 exploit⟧", "⟦아무도 모르는 구멍으로 들어와요|slips in through an unknown hole⟧", "⟦목수의 판자|the carpenter\'s plank⟧"),
        ("⟦5 자리 잡기|5 install⟧", "⟦방 안에 둥지를 틀어요|builds a nest in a room⟧", "⟦경비견|the guard dog⟧"),
        ("⟦6 두목과 연락|6 command⟧", "⟦창문으로 신호를 보내요|signals the boss out the window⟧", "⟦복도 파수꾼|the corridor guard⟧"),
        ("⟦7 목표 달성|7 objective⟧", "⟦왕관을 들고 나가요|walks out with the crown⟧", "⟦빨간 도장 문지기|the red-stamp doorkeeper⟧"))
P4 = svg(340, sky(340)
         + '<rect x="40" y="24" width="680" height="256" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="24" width="680" height="30" rx="8" fill="#C9A86A"/>'
         + label(120, 44, "⟦걸음|step⟧", 12, "#142033", cls="d") + label(370, 44, "⟦도둑이 하는 일|what the thief does⟧", 12, "#142033", cls="d") + label(610, 44, "⟦누가 끊나|who cuts it⟧", 12, "#142033", cls="d")
         + "".join(f'<path d="M40 {54 + r * 32} h680" stroke="#C9A86A" stroke-width="1.5"/>' for r in range(1, 7))
         + "".join(label(120, 75 + r * 32, a, 11, "#142033", cls="d") + label(370, 75 + r * 32, b, 11, "#142033") + label(610, 75 + r * 32, c, 11, "#1E7A4A" if r != 1 else "#8A7A66") for r, (a, b, c) in enumerate(ROWS))
         + label(380, 318, "⟦한 걸음도 못 끊으면 그때 왕관이 나가요|only when no step gets cut does the crown walk out⟧", 12, "var(--ink)", cls="d"))

# 5. 사슬과 백과사전은 달라요
P5 = svg(320, sky(320)
         + '<path d="M70 120 H310" stroke="var(--stone-dark)" stroke-width="4"/>' + "".join(link(70 + i * 40, 120, 0.7, "var(--stone-dark)") for i in range(7)) + scissors(190, 70, 0.7)
         + label(190, 190, "⟦사슬: 큰 걸음 일곱 개|the chain: seven big steps⟧", 12, "var(--ink)", cls="d") + label(190, 212, "⟦도둑이 지금 어디쯤인지|where the thief is right now⟧", 10, "var(--muted)")
         + book(560, 110, 1.0) + label(560, 190, "⟦백과사전: 걸음마다 수백 가지 버릇|the encyclopedia: hundreds of habits per step⟧", 12, "var(--ink)", cls="d") + label(560, 212, "⟦도둑이 정확히 어떻게 하는지|exactly how the thief does it⟧", 10, "var(--muted)")
         + '<path d="M330 120 h100" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M420 112 l10 8 l-10 8" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + label(380, 300, "⟦사슬로 어디쯤인지 보고, 백과사전으로 어떻게 하는지 봐요|the chain says where they are, the book says how⟧", 13, "var(--ink)", cls="d"))

ORDER_I = icon('<circle cx="14" cy="32" r="8" fill="var(--bad)"/><circle cx="32" cy="32" r="8" fill="var(--bad)"/><circle cx="50" cy="32" r="8" fill="var(--accent)"/><path d="M22 32 h2 M40 32 h2" stroke="var(--ink)" stroke-width="3"/>')
CUT_I = icon('<rect x="6" y="24" width="20" height="16" rx="8" fill="none" stroke="var(--stone-dark)" stroke-width="5"/><rect x="38" y="24" width="20" height="16" rx="8" fill="none" stroke="var(--stone-dark)" stroke-width="5"/><path d="M28 14 l8 36" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
EARLY_I = icon('<path d="M10 44 h44" stroke="var(--stone-dark)" stroke-width="4" stroke-linecap="round"/><circle cx="16" cy="44" r="7" fill="var(--good)"/><circle cx="32" cy="44" r="5" fill="var(--accent)"/><circle cx="48" cy="44" r="5" fill="var(--bad)"/><path d="M16 34 v-14 l8 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
FRIENDS_I = icon('<circle cx="16" cy="22" r="8" fill="#E8C9A8"/><path d="M8 20 q8 -10 16 0z" fill="var(--good)"/><circle cx="48" cy="22" r="8" fill="#E8C9A8"/><path d="M40 20 q8 -10 16 0z" fill="#5B8DEF"/><rect x="8" y="32" width="16" height="20" rx="4" fill="var(--good)"/><rect x="40" y="32" width="16" height="20" rx="4" fill="#5B8DEF"/>')

PAGE = {
    "slug": "killchain", "order": 70,
    "title": ("도둑의 일곱 걸음", "The Seven Steps of a Thief"),
    "h1": ("<em>킬 체인</em>이 뭐예요?", "What is a <em>Kill Chain</em>?"),
    "sub": ("사이버 킬 체인(Cyber Kill Chain)을 도둑이 성을 털기까지 늘 밟는 일곱 걸음, 그리고 그중 하나만 끊으면 끝나는 사슬 이야기로 풀어봤어요.",
            "The Cyber Kill Chain, told as a story about the seven steps every thief takes to rob a castle — and the chain that breaks if you cut just one."),
    "panels": [
        {"svg": P1, "alt": ("밤. 왕관이 있던 빈 받침대, 땀 흘리는 경비실 친구가 '언제 들어온 거지?', 도둑은 이미 왕관을 들고 성문 밖으로 나감", "Night. An empty pedestal where the crown was, a sweating guard asking when they got in, and a thief already past the gate with the crown"),
         "caption": ("왕관이 사라졌어요. 도둑이 갑자기 나타난 것 같아요.", "The crown is gone. It looks like the thief came out of nowhere."),
         "small": ('<a href="soc-ko.html">경비실</a>은 왕관이 나가는 순간만 봤어요. "언제 들어온 거지?" 아무도 몰라요.',
                   'The <a href="soc-en.html">guard room</a> only saw the crown leave. "When did they get in?" Nobody knows.')},
        {"svg": P2, "alt": ("흐릿한 도둑 여섯이 순서대로: 문 세기, 벌레 넣기, 편지 보내기, 구멍으로, 둥지 틀기, 신호 보내기. 맨 오른쪽 또렷한 도둑만 왕관을 들고 있고 '이것만 봤어요'", "Six faded thieves in a row: counting doors, packing the bug, sending the letter, through the crack, nesting, signalling. Only the last, solid thief holds the crown, marked: only saw this"),
         "caption": ("사실은 그 전에 여섯 걸음이 있었어요.", "In fact, six steps came before that."),
         "small": ("도둑은 갑자기 나타나지 않아요. 문을 세고, 편지를 보내고, 둥지를 틀고… 성문만 보면 이 걸음들이 안 보여요.", "Thieves don\'t appear out of nowhere. They count doors, send letters, build nests… and from the gate, none of those steps are visible.")},
        {"svg": P3, "hero": True, "alt": ("일곱 개의 사슬 고리에 번호 1~7과 이름: 정찰, 무기 만들기, 전달, 틈 이용, 자리 잡기, 두목과 연락, 목표 달성. 3번과 4번 사이에 가위 — '여기서 끊으면?'. 왼쪽 끝 마을, 오른쪽 끝 왕관", "Seven chain links numbered 1 to 7: recon, build the weapon, delivery, use the crack, settle in, call the boss, take the crown. Scissors between links 3 and 4 asking: cut here? The village at one end, the crown at the other"),
         "caption": ("킬 체인은 도둑의 일곱 걸음이에요. 하나만 끊어도 왕관은 못 가져가요.", "A kill chain is the seven steps of a thief. Cut just one, and no crown."),
         "small": ("도둑은 이 순서를 건너뛸 수 없어요. 그래서 사슬이에요 — 어느 고리든 끊으면 끝까지 못 가요.", "A thief can\'t skip a step. That\'s why it\'s a chain — break any link and they never reach the end."),
         "tricks": (4, [
             (ORDER_I, ("늘 같은 순서", "Always the same order"), ("건너뛸 수 없어요", "no step can be skipped"), "warm"),
             (CUT_I, ("하나만 끊어도", "Cut just one"), ("왕관은 못 가져가요", "and there is no crown")),
             (EARLY_I, ("빠를수록 좋아요", "Earlier is better"), ("1번에서 끊으면 성은 멀쩡", "cut at step 1 and nothing is touched")),
             (FRIENDS_I, ("걸음마다 다른 친구", "A different friend per step"), ("편지 검토원, 경비견, 파수꾼", "letter checker, guard dog, corridor guard"), "calm"),
         ])},
        {"svg": P4, "alt": ("표: 걸음 일곱 개마다 도둑이 하는 일과 누가 끊는지 — 바깥에서 세는 친구, (못 봄), 편지 검토원, 목수의 판자, 경비견, 복도 파수꾼, 빨간 도장 문지기", "A table: for each of the seven steps, what the thief does and who cuts it — the outside counter, (can\'t see), the letter checker, the carpenter\'s plank, the guard dog, the corridor guard, the red-stamp doorkeeper"),
         "caption": ("걸음마다 끊어 주는 친구가 달라요.", "Each step has a different friend who can cut it."),
         "small": ('<a href="asm-ko.html">바깥에서 문 세기</a>, <a href="phishing-ko.html">가짜 편지</a> 검토, <a href="patch-ko.html">목수의 판자</a>, <a href="edr-ko.html">경비견</a>, <a href="ndr-ko.html">복도 파수꾼</a>. 2번 걸음은 성 밖에서 일어나서 우리가 못 봐요 — 그래서 3번부터가 진짜 승부예요.',
                   '<a href="asm-en.html">Counting doors from outside</a>, checking <a href="phishing-en.html">fake letters</a>, the <a href="patch-en.html">carpenter\'s plank</a>, the <a href="edr-en.html">guard dog</a>, the <a href="ndr-en.html">corridor guard</a>. Step 2 happens outside the castle where we can\'t see — so the real fight starts at step 3.')},
        {"svg": P5, "alt": ("왼쪽엔 고리 일곱 개짜리 짧은 사슬과 가위, 오른쪽엔 두꺼운 보라색 백과사전. 둘 사이에 점선 화살표", "On the left a short chain of seven links with scissors; on the right a thick purple encyclopedia, with a dotted arrow between them"),
         "caption": ("사슬은 '어디쯤', 백과사전은 '어떻게'예요.", "The chain says where; the encyclopedia says how."),
         "small": ('사슬은 큰 걸음 일곱 개라 지금 도둑이 어디쯤인지 한눈에 보여요. <a href="attack-ko.html">도둑 백과사전</a>은 걸음마다 수백 가지 버릇이 적혀 있어요. 둘 다 <a href="apt-ko.html">끈질긴 도둑 무리</a>를 쫓을 때 같이 펴요.',
                   'The chain has seven big steps, so you see at a glance where the thief is. The <a href="attack-en.html">thief encyclopedia</a> lists hundreds of habits for each step. Open both when chasing a <a href="apt-en.html">persistent gang</a>.')},
    ],
    "summary": (("<b>킬 체인</b> = 도둑이 왕관까지 가려면 늘 밟는 <b>일곱 걸음</b>. <b>하나만 끊어도</b> 실패하고, <b>빠른 걸음</b>에서 끊을수록 성은 덜 다쳐요.",
                 "<b>Kill chain</b> = the <b>seven steps</b> every thief must take to reach the crown. <b>Cut just one</b> and they fail — and the <b>earlier</b> the cut, the less the castle gets hurt."),
                ("Cyber Kill Chain. 록히드 마틴이 정리한 공격의 7단계 — 정찰, 무기화, 전달, 익스플로잇, 설치, 명령·제어(C2), 목표 달성 — 로, 어느 단계에서든 끊으면 공격이 완성되지 않는다는 방어 모델이에요.",
                 "Lockheed Martin\'s seven-stage model of an attack — reconnaissance, weaponization, delivery, exploitation, installation, command and control (C2), actions on objectives — built on the idea that breaking any one stage stops the attack.")),
    "glossary": [
        ("도둑의 일곱 걸음", "Cyber Kill Chain", ("왕관까지 가는 순서 일곱 개.", "The seven steps to the crown."), ("사슬처럼 이어져 있어서, 고리 하나만 끊어도 끝까지 못 가요.", "Linked like a chain, so breaking one link stops the whole thing.")),
        ("1 정찰", "Reconnaissance", ("성 밖에서 문 세기.", "Counting our doors from outside."), ('어느 문이 열려 있나, 누가 사나. → <a href="asm-ko.html">바깥에서 세는 우리 성의 문</a>', 'Which doors are open, who lives here. → <a href="asm-en.html">counting our doors from outside</a>')),
        ("2 무기 만들기", "Weaponization", ("선물 상자에 벌레 넣기.", "Packing a bug into a gift box."), ('성 밖에서 하는 일이라 우리는 못 봐요. 벌레는 → <a href="malware-ko.html">선물 상자 속 벌레</a>', 'Done outside the castle, so we can\'t see it. The bug → <a href="malware-en.html">the bug in the gift box</a>')),
        ("3 전달", "Delivery", ("편지로 보내기.", "Sending it by letter."), ('가장 흔한 길은 우체국인 척하는 편지예요. → <a href="phishing-ko.html">가짜 편지</a>', 'The most common route is a letter posing as the post. → <a href="phishing-en.html">the fake letter</a>')),
        ("4 틈 이용 · 5 자리 잡기", "Exploitation · Installation", ("구멍으로 들어와 둥지 틀기.", "In through the crack, then nesting."), ('구멍은 → <a href="zeroday-ko.html">아무도 모르는 구멍</a>, 둥지는 → <a href="edr-ko.html">경비견</a>이 찾아요.', 'The crack → <a href="zeroday-en.html">the hole nobody knows</a>; the nest is what the <a href="edr-en.html">guard dog</a> sniffs out.')),
        ("6 두목과 연락", "Command and Control (C2)", ("창문으로 신호 보내기.", "Signalling the boss out the window."), ('벌레는 혼자 못 움직여요. 밖의 두목이 시켜요. 이 신호를 → <a href="ndr-ko.html">복도 파수꾼</a>이 봐요.', 'The bug can\'t act alone; the boss outside gives orders. The <a href="ndr-en.html">corridor guard</a> watches for this signal.')),
        ("7 목표 달성", "Actions on Objectives", ("왕관 들고 나가기.", "Walking out with the crown."), ('훔치기, 부수기, 자물쇠 채우기. 마지막에 막는 건 → <a href="dlp-ko.html">빨간 도장 문지기</a>', 'Stealing, breaking, or locking things up. The last line is → <a href="dlp-en.html">the red-stamp doorkeeper</a>')),
        ("도둑 백과사전과의 차이", "vs. MITRE ATT&amp;CK", ("사슬은 어디쯤, 백과사전은 어떻게.", "The chain says where, the book says how."), ('사슬은 큰 걸음 7개, 백과사전은 걸음마다 수백 가지 버릇. → <a href="attack-ko.html">도둑 백과사전</a>', 'Seven big steps versus hundreds of habits per step. → <a href="attack-en.html">the thief encyclopedia</a>')),
    ],
}
