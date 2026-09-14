from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
MAID = dict(hat=None, shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'

PAPER_C = '<rect x="-11" y="-20" width="22" height="16" rx="2" fill="#5B8DEF"/>'      # 성 종이 (파랑)
PAPER_P = '<rect x="-11" y="2" width="22" height="16" rx="2" fill="#E9B44C"/>'        # 내 종이 (노랑)
SPLIT = '<path d="M-16 -2 h32" stroke="var(--night)" stroke-width="2"/>'
WIPED = '<path d="M-9 -18 l18 12 M9 -18 l-18 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
CARD = '<rect x="-10" y="-8" width="20" height="26" rx="2" fill="var(--good)"/><ellipse cx="0" cy="4" rx="5" ry="3.5" fill="var(--bad)"/><path d="M-7 12 l3 3 l7 -7" stroke="#FFF" stroke-width="2" fill="none"/>'


def phone(x, y, s=1.0, inner="", lock=False):
    """작은 상자(휴대폰). 바깥 40×64, 화면은 크림색 종이."""
    lk = '<rect x="-8" y="-4" width="16" height="13" rx="2" fill="#E9B44C"/><path d="M-4 -4 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-20" y="-32" width="40" height="64" rx="6" fill="var(--night)"/>'
            f'<rect x="-16" y="-26" width="32" height="48" rx="3" fill="#FFF8E7"/>{inner}{lk}</g>')


def check(x, y):
    return f'<circle cx="{x}" cy="{y}" r="8" fill="var(--good)"/><path d="M{x - 4} {y} l3 3 l6 -6" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>'


def house(x, y, name, roof="var(--bad)", s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-50 0 L0 -36 L50 0 Z" fill="{roof}"/><rect x="-10" y="26" width="20" height="34" fill="{WOOD}"/>{label(0, 80, name, 12, "var(--muted)")}</g>')


def cafe(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-46 0 h92 l-8 -20 h-76 z" fill="var(--accent)"/>' + "".join(f'<rect x="{-46 + i * 18}" y="-20" width="9" height="20" fill="#FFD9B8"/>' for i in range(5))
            + f'<rect x="-10" y="26" width="20" height="34" fill="{WOOD}"/>{label(0, 80, "⟦카페|cafe⟧", 12, "var(--muted)")}</g>')


def signal(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})">' + "".join(f'<path d="M0 {-r} a{r} {r} 0 0 1 0 {2 * r}" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>' for r in (10, 20, 30)) + "</g>"


# 1. 성 종이를 작은 상자에 넣어 마을로
P1 = svg(300, sky(300) + castle(20, 100, 0.5)
         + bubble(250, 30, 200, 34, "⟦성 종이, 상자에 넣었어요|castle papers, in my box⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(300, 130, s=0.8, face=SMILE, **MAID) + phone(368, 200, 0.55, PAPER_C)
         + person(440, 140, s=0.8, **ME) + phone(508, 208, 0.55, PAPER_C)
         + label(330, 250, "⟦서기|the clerk⟧", 11, "var(--muted)") + label(470, 250, "⟦나|me⟧", 11, "var(--muted)")
         + house(600, 140, "⟦마을|the village⟧", "var(--bad)", 0.9) + house(695, 150, "⟦이웃|neighbor⟧", "var(--accent)", 0.7)
         + label(380, 282, "⟦성 종이가 작은 상자에 담겨 마을로 나가요|castle papers leave for the village inside little boxes⟧", 12, "var(--ink)", cls="d"))

# 2. 잃어버리면 도둑이 열고, 내 상자엔 성 종이와 내 사진이 섞여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/><path d="M380 30 v240" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + bubble(230, 20, 170, 32, "⟦자물쇠도 없네|no lock, even⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + person(190, 80, s=0.85, face=MASK, extra=BAG) + phone(130, 205, 1.1, PAPER_C)
         + label(170, 266, "⟦잃어버린 상자 — 도둑이 열어봐요|a lost box — the thief opens it⟧", 11, "var(--ink)")
         + person(540, 70, s=0.85, face=FROWN + SWEAT, hat=None, shirt="#4A5A72") + phone(640, 195, 1.3, PAPER_C + PAPER_P + '<rect x="-4" y="-10" width="22" height="16" rx="2" fill="#E9B44C" opacity="0.9"/>')
         + label(590, 266, "⟦내 상자엔 성 종이와 내 사진이 섞여요|my own box mixes castle papers with my photos⟧", 10, "var(--ink)")
         + label(380, 292, "⟦성 밖에선 성 규칙이 안 따라가요|outside the walls, the castle rules stay behind⟧", 12, "var(--ink)", cls="d"))

# 3. 상자 관리소 — 상자마다 규칙 (hero)
RULES = ((phone(320, 150, 1.5, PAPER_C, lock=True), ("⟦자물쇠 필수|lock required⟧", "⟦안 걸면 성 종이 못 넣어요|no lock, no castle papers⟧")),
         (signal(388, 88, 0.5) + phone(435, 150, 1.5, PAPER_C + WIPED + PAPER_P), ("⟦잃으면 멀리서|if lost,⟧", "⟦성 칸만 지워요|wipe from afar⟧")),
         (phone(550, 150, 1.5, PAPER_C + SPLIT + PAPER_P), ("⟦성 칸 · 내 칸|castle side · my side⟧", "⟦칸을 나눠요|kept apart⟧")),
         (phone(665, 150, 1.5, CARD), ("⟦벌레 카드 최신|bug cards up to date⟧", "⟦판자도 늦지 않게|planks on time, too⟧")))
P3 = svg(360, sky(360)
         + bubble(110, 20, 240, 34, "⟦성 상자엔 성 규칙이에요|castle boxes follow castle rules⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + gatehouse(80, 100) + label(80, 212, "⟦상자 관리소|the box office⟧", 12, "var(--ink)", cls="d")
         + person(170, 150, s=0.75, face=SMILE, **BLUE) + label(196, 255, "⟦관리소 친구|the box keeper⟧", 11, "var(--muted)")
         + "".join(d + label(x, 225, a, 10, "var(--ink)") + label(x, 241, b, 10, "var(--muted)") for (d, (a, b)), x in zip(RULES, (320, 435, 550, 665)))
         + label(380, 300, "⟦마을 어디서든 성 상자는 성 규칙|wherever it goes, a castle box keeps castle rules⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦내 상자여도 성 칸만은 관리소가 봐요|even in your own box, the castle side answers to the office⟧", 12, "var(--muted)"))

# 4. 잃어버리면 — 신고 → 멀리서 → 성 칸만 지워요
P4 = svg(320, sky(320) + castle(30, 90, 0.45) + label(130, 205, "⟦관리소: 지워!|the office: wipe it!⟧", 12, "var(--ink)", cls="d")
         + '<path d="M235 100 C330 40 420 40 490 110" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="8 6"/>'
         + bubble(240, 110, 180, 32, "⟦상자를 잃어버렸어요!|I lost my box!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(300, 180, s=0.7, face=FROWN + SWEAT, **MAID) + label(325, 285, "⟦먼저 신고|report it first⟧", 11, "var(--muted)")
         + bubble(560, 20, 190, 34, "⟦성 칸이 비었네?|the castle side is empty?⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + phone(520, 170, 2.0, PAPER_C + WIPED + SPLIT + PAPER_P) + person(620, 110, s=0.85, face=MASK, extra=BAG)
         + label(520, 262, "⟦성 칸만 지워져요 — 내 사진은 그대로|only the castle side is wiped — my photos stay⟧", 11, "var(--ink)")
         + label(380, 308, "⟦신고 → 관리소가 멀리서 → 성 칸만 지워요|report → the office reaches out → wipes only the castle side⟧", 12, "var(--ink)", cls="d"))

# 5. 마을 어디서든 — 문지기도 상자를 먼저 봐요
P5 = svg(300, sky(300)
         + cafe(100, 110) + person(170, 140, s=0.65, **ME) + phone(222, 190, 0.5, PAPER_C, lock=True) + check(238, 164) + label(190, 245, "⟦카페에서도|at the cafe⟧", 11, "var(--muted)")
         + house(350, 110, "⟦집|home⟧") + person(420, 140, s=0.65, face=SMILE, **MAID) + phone(472, 190, 0.5, PAPER_C + SPLIT + PAPER_P, lock=True) + check(488, 164) + label(440, 245, "⟦집에서도|at home⟧", 11, "var(--muted)")
         + bubble(520, 20, 220, 34, "⟦상자 규칙 지켰니? 그럼 들어와|box rules kept? come in⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + gate(660, 70, 0.85) + person(630, 175, s=0.6, face=SMILE, **GUARD) + label(700, 262, "⟦성문|the gate⟧", 11, "var(--muted)")
         + label(380, 282, "⟦문지기도 상자를 먼저 봐요 — 규칙 없는 상자는 못 들어와요|the doorkeeper checks the box first — no rules, no entry⟧", 12, "var(--ink)", cls="d"))

LOCK_I = icon('<rect x="20" y="6" width="24" height="44" rx="4" fill="var(--night)"/><rect x="23" y="10" width="18" height="34" rx="2" fill="#FFF8E7"/><rect x="27" y="26" width="10" height="9" rx="2" fill="#E9B44C"/><path d="M29 26 v-4 a3 3 0 0 1 6 0 v4" stroke="#E9B44C" stroke-width="2" fill="none"/>')
WIPE_I = icon('<rect x="24" y="12" width="24" height="44" rx="4" fill="var(--night)"/><rect x="27" y="16" width="18" height="34" rx="2" fill="#FFF8E7"/><path d="M31 22 l10 10 M41 22 l-10 10" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><path d="M14 20 a10 10 0 0 1 0 -12 M10 26 a18 18 0 0 1 0 -24" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SPLIT_I = icon('<rect x="20" y="6" width="24" height="52" rx="4" fill="var(--night)"/><rect x="23" y="10" width="18" height="21" rx="2" fill="#5B8DEF"/><rect x="23" y="33" width="18" height="21" rx="2" fill="#E9B44C"/>')
CARD_I = icon('<rect x="16" y="10" width="32" height="44" rx="3" fill="var(--good)"/><ellipse cx="32" cy="28" rx="9" ry="6" fill="var(--bad)"/><circle cx="26" cy="25" r="4" fill="var(--bad)"/><path d="M24 44 l5 5 l11 -11" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "mdm", "order": 105,
    "title": ("성 밖으로 들고 나가는 작은 상자", "The Little Box That Leaves the Castle"),
    "h1": ("<em>MDM · BYOD</em>가 뭐예요?", "What are <em>MDM and BYOD</em>?"),
    "sub": ("모바일 기기 관리(MDM)와 개인 기기 업무 사용(BYOD)을 성 종이를 넣어 마을로 들고 다니는 작은 상자 이야기로 풀어봤어요.",
            "Mobile device management and bring-your-own-device, told as a story about little boxes that carry castle papers out into the village."),
    "panels": [
        {"svg": P1, "alt": ("성 앞에서 서기와 내가 각자 작은 상자(휴대폰)에 파란 성 종이를 넣고 마을 집 쪽으로 걸어감", "In front of the castle, the clerk and I each carry a little box (a phone) holding blue castle papers, walking toward the village houses"),
         "caption": ("성 사람들은 성 종이를 작은 상자에 넣어 마을로 들고 다녀요.", "Castle folk carry castle papers out to the village in little boxes."),
         "small": ("휴대폰도 노트북도 다 작은 상자예요. 상자 안에는 성에서 만든 종이가 들어 있어요.", "A phone is a little box. A laptop is a little box. Inside are papers made in the castle.")},
        {"svg": P2, "alt": ("왼쪽: 잃어버린 상자를 도둑이 열어 보며 '자물쇠도 없네'. 오른쪽: 내 상자 안에 파란 성 종이와 노란 내 사진이 섞여 있어 땀 흘리는 나", "Left: a thief opens a lost box, saying there is not even a lock. Right: my own box holds blue castle papers mixed with my yellow photos, and I sweat"),
         "caption": ("잃어버리면 도둑이 열어봐요. 내 상자엔 내 사진까지 섞여 있고요.", "Lose it, and a thief opens it. And my own box has my photos mixed in."),
         "small": ("성 밖에서는 성 규칙이 따라가지 않아요. 상자가 내 것이면 성 종이와 개인 종이가 한 칸에 섞여요.", "Outside the walls, the castle rules stay behind. When the box is my own, castle papers and personal papers share one shelf.")},
        {"svg": P3, "hero": True, "alt": ("상자 관리소 앞의 파란 모자 친구. 네 개의 상자: 자물쇠 걸린 상자, 멀리서 성 칸이 지워지는 상자, 성 칸과 내 칸으로 나뉜 상자, 최신 벌레 카드가 든 상자", "A blue-hat keeper at the box office. Four boxes: one with a lock, one whose castle side is wiped from afar, one split into a castle side and my side, one holding an up-to-date bug card"),
         "caption": ("상자 관리소가 상자마다 규칙을 붙여요. 마을 어디서든 성 상자는 성 규칙이에요.", "The box office puts rules on every box. Wherever it goes, a castle box keeps castle rules."),
         "small": ('자물쇠(<a href="encryption-ko.html">봉인</a>) 필수, 잃으면 멀리서 성 칸만 지우기, 성 칸과 내 칸 나누기, <a href="antivirus-ko.html">벌레 카드</a>와 <a href="patch-ko.html">판자</a>는 최신. 내 상자여도 성 칸만은 관리소가 봐요.',
                   'A lock (<a href="encryption-en.html">sealing</a>) is required; if lost, only the castle side is wiped from afar; castle side and my side stay apart; <a href="antivirus-en.html">bug cards</a> and <a href="patch-en.html">planks</a> stay current. Even in your own box, the castle side answers to the office.'),
         "tricks": (4, [
             (LOCK_I, ("자물쇠 필수", "Lock required"), ("안 걸면 성 종이 못 넣어요", "no lock, no castle papers"), "calm"),
             (WIPE_I, ("멀리서 지우기", "Wipe from afar"), ("잃으면 성 칸만", "lost? only the castle side"), "warm"),
             (SPLIT_I, ("성 칸 · 내 칸", "Castle side, my side"), ("내 사진은 안 봐요", "my photos stay mine")),
             (CARD_I, ("카드 최신", "Cards up to date"), ("벌레 카드도 판자도", "bug cards and planks")),
         ])},
        {"svg": P4, "alt": ("서기가 '상자를 잃어버렸어요!' 하고 신고하자 성에서 점선 신호가 날아가 도둑 손의 상자에서 성 칸만 지워짐. 도둑은 '성 칸이 비었네?'", "The clerk reports a lost box; a dotted signal flies from the castle to the box in the thief\'s hands and wipes only the castle side. The thief: the castle side is empty?"),
         "caption": ("잃어버리면 먼저 신고해요. 관리소가 멀리서 성 칸만 지워요.", "If you lose it, report it first. The office wipes only the castle side from afar."),
         "small": ("내 사진은 그대로 남아요. 그래서 신고를 미루지 않아도 돼요 — 빨리 말할수록 도둑이 열 시간이 짧아져요.", "My photos stay. So there\'s no reason to delay the report — the sooner you say it, the less time the thief has to open it.")},
        {"svg": P5, "alt": ("카페와 집에서 각자 자물쇠 걸린 상자에 초록 체크 표시. 성문의 경비는 '상자 규칙 지켰니? 그럼 들어와'", "At the cafe and at home, each locked box carries a green check. The guard at the gate: box rules kept? come in"),
         "caption": ("문지기도 상자를 먼저 봐요. 규칙 없는 상자는 성에 못 들어와요.", "The doorkeeper checks the box first. A box without the rules can\'t enter the castle."),
         "small": ('<a href="zerotrust-ko.html">문마다 물어보는 성</a>은 사람만 보지 않고 상자 상태도 봐요. 빨간 도장 종이는 <a href="dlp-ko.html">문지기</a>가 상자 밖으로 못 나가게 막고요.',
                   'The <a href="zerotrust-en.html">castle that asks at every door</a> checks the box, not just the person. And the <a href="dlp-en.html">doorkeeper</a> keeps red-stamped paper from leaving the box at all.')},
    ],
    "summary": (("<b>MDM</b> = 성 밖으로 나가는 <b>작은 상자마다 성 규칙</b>(자물쇠 · 멀리서 지우기 · 성 칸과 내 칸 · 최신 카드)을 붙이는 <b>상자 관리소</b>. <b>BYOD</b> = 내 상자에도 <b>성 칸</b>을 두는 것.",
                 "<b>MDM</b> = the <b>box office</b> that puts <b>castle rules on every little box</b> that leaves (lock, wipe from afar, castle side and my side, current cards). <b>BYOD</b> = keeping a <b>castle side</b> inside my own box."),
                ("Mobile Device Management / Bring Your Own Device. 조직이 휴대폰·노트북에 화면 잠금·암호화·원격 삭제·앱 통제 같은 정책을 강제하는 것이 MDM이고, 개인 기기로 업무를 보되 업무 영역(컨테이너)만 관리하는 것이 BYOD예요.",
                 "MDM is the organization enforcing policies — screen lock, encryption, remote wipe, app control — on phones and laptops. BYOD is using personal devices for work while managing only the work area (a container).")),
    "glossary": [
        ("MDM", "MDM", ("상자 관리소.", "The box office."), ("성 밖으로 나가는 상자마다 규칙을 붙이고, 지키는지 봐요.", "Puts rules on every box that leaves the castle, and checks that they hold.")),
        ("BYOD", "BYOD", ("내 상자.", "My own box."), ("내 휴대폰으로 성 일도 봐요. 그래서 성 칸만 따로 관리해요.", "Doing castle work on my own phone. So only the castle side is managed.")),
        ("원격 삭제", "Remote wipe", ("멀리서 지우기.", "Wiping from afar."), ("잃어버린 상자의 성 칸만 관리소가 멀리서 비워요.", "The office empties the castle side of a lost box from a distance.")),
        ("화면 잠금 · 암호화", "Screen lock & encryption", ("상자 자물쇠.", "The box lock."), ('열쇠 없이는 안이 안 보여요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Without the key, nothing inside can be read. → <a href="encryption-en.html">the letter no one reads without the key</a>')),
        ("업무 · 개인 분리", "Work/personal container", ("성 칸과 내 칸.", "Castle side, my side."), ("성 종이는 성 칸에만. 관리소는 내 칸은 안 봐요.", "Castle papers live only on the castle side. The office never looks at my side.")),
        ("분실 신고", "Lost-device report", ("먼저 말하기.", "Say it first."), ("빨리 말할수록 도둑이 열 시간이 짧아져요. 내 사진은 안 지워지니 미루지 마세요.", "The sooner you report, the less time a thief has. Your photos aren\'t wiped, so don\'t wait.")),
        ("탈옥 · 루팅", "Jailbreak / rooting", ("자물쇠 뜯어낸 상자.", "A box with the lock torn off."), ("관리소 규칙이 안 먹혀요. 그런 상자엔 성 종이를 안 줘요.", "The office rules no longer hold. Such a box gets no castle papers.")),
        ("기기 상태 확인", "Device posture check", ("문지기가 상자 먼저 보기.", "The doorkeeper checks the box."), ('자물쇠 · 최신 카드가 없으면 못 들어와요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'No lock or stale cards, no entry. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
    ],
}
