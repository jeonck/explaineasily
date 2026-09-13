from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
HATS = (None, "#E9B44C", "#5B8DEF", "var(--stone-dark)")


def bell(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/><rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def bug(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="var(--bad)"/><circle cx="-12" cy="-4" r="8" fill="var(--bad)"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8" stroke="var(--bad)" stroke-width="2.5" stroke-linecap="round"/></g>')


def chest(x, y, s=1.0, grey=False, open_lid=False):
    body, edge = ("var(--stone)", "var(--stone-dark)") if grey else ("#8B5E3C", "#5A3B22")
    lid = (f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}" transform="rotate(-40 -30 -14)"/>' if open_lid else f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{body}"/>{lid}</g>'


STEPS = (("⟦준비|Prepare⟧", "var(--stone-dark)"), ("⟦확인|Confirm⟧", "var(--accent)"), ("⟦가두기|Contain⟧", "var(--bad)"), ("⟦내보내기|Remove⟧", "var(--bad)"), ("⟦되돌리기|Restore⟧", "var(--good)"), ("⟦배우기|Learn⟧", "var(--good)"))


def playbook(x, y, s=1.0, highlight=None):
    rows = ""
    for i, (t, c) in enumerate(STEPS):
        yy = 44 + i * 30
        hl = f'<rect x="8" y="{yy - 18}" width="204" height="28" rx="6" fill="var(--accent-soft)"/>' if highlight == i else ""
        rows += hl + f'<circle cx="28" cy="{yy - 4}" r="11" fill="{c}"/>' + label(28, yy, str(i + 1), 12, "#FFF") + label(50, yy, t, 14, "#142033", "start")
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="220" height="230" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="220" height="28" rx="8" fill="#C9A86A"/>'
            f'{label(110, 19, "⟦도둑 들었을 때 순서표|WHEN A THIEF GETS IN⟧", 12, "#142033", cls="d")}{rows}</g>')


# 1. 종이 울렸어요, 우왕좌왕
P1 = svg(300, sky(300) + bell(380, 60, 1.1)
         + "".join(person(x, y, s=0.7, hat=h, shirt="#4A5A72", face=FROWN + SWEAT) for (x, y), h in zip(((80, 130), (250, 170), (480, 160), (640, 130)), HATS))
         + "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="5 5"/>' for x, y, dx, dy in ((150, 200, 60, -30), (320, 240, -50, 20), (550, 230, 60, 10), (630, 200, -60, -20)))
         + bubble(40, 40, 160, 34, "⟦누가 문 잠가요?|who locks the doors?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + bubble(560, 40, 180, 34, "⟦누구한테 말하죠?|who do we tell?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦다들 뛰는데 아무도 어디로 뛰는지 몰라요|everyone runs, nobody knows where⟧", 13, "var(--muted)"))

# 2. 순서 없이 움직이면 더 망가진다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(80, 90, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=FROWN) + '<g transform="translate(160,170)"><path d="M-16 -10 h32 l-3 34 h-26z" fill="var(--stone-dark)"/><rect x="-20" y="-16" width="40" height="6" fill="var(--stone-dark)"/></g>' + '<rect x="140" y="120" width="40" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2" transform="rotate(20 160 135)"/>' + label(120, 240, "⟦일지를 버려요|throws out the diary⟧", 12, "var(--bad)")
         + person(330, 90, s=0.8, hat="#5B8DEF", shirt="#4A5A72", face=FROWN) + f'<g transform="translate(420,80) scale(0.7)"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><rect x="-10" y="40" width="20" height="16" rx="3" fill="var(--night)"/></g>' + label(380, 240, "⟦엉뚱한 문을 잠가요|locks the wrong door⟧", 12, "var(--bad)")
         + person(600, 100, s=0.8, face=MASK, extra='<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/>') + label(630, 240, "⟦도둑은 아직 안에|the thief is still inside⟧", 12, "var(--bad)")
         + label(380, 282, "⟦급할수록 순서가 필요해요|the bigger the hurry, the more you need an order⟧", 13, "var(--muted)"))

# 3. 사고 대응 = 순서표대로 (hero)
P3 = svg(340, sky(340) + playbook(60, 40, 1.0)
         + bell(420, 60, 0.8) + '<path d="M420 100 L420 140" stroke="var(--accent)" stroke-width="3"/><path d="M410 130 L420 142 L430 130" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + person(390, 150, s=0.85, face=EYES, **GUARD) + label(420, 290, "⟦종이 울리면 순서표를 펴요|bell rings, book opens⟧", 12, "var(--ink)", cls="d")
         + "".join(person(x, 180, s=0.6, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((520, "#E9B44C"), (590, "#5B8DEF"), (660, None)))
         + "".join(label(x + 18, 290, t, 11, "var(--muted)") for x, t in ((520, "⟦문 담당|doors⟧"), (590, "⟦벌레 담당|bugs⟧"), (660, "⟦알림 담당|telling⟧")))
         + label(380, 322, "⟦누가 뭘 할지 이미 적혀 있어요|who does what is already written down⟧", 13, "var(--muted)"))

# 4. 가두고, 내보내고, 되돌린다
P4 = svg(320, '<rect width="253" height="320" fill="var(--bad-soft)"/><rect x="253" width="254" height="320" fill="var(--accent-soft)"/><rect x="507" width="253" height="320" fill="var(--good-soft)"/>'
         + f'<g transform="translate(126,80)"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><rect x="-10" y="40" width="20" height="16" rx="3" fill="var(--night)"/></g>' + '<rect x="200" y="60" width="8" height="150" fill="var(--stone-dark)"/>' + bug(126, 200, 0.6)
         + label(126, 250, "⟦가두기|contain⟧", 15, "var(--ink)", cls="d") + label(126, 275, "⟦문 잠그고 복도 끊기|lock the door, cut the hallway⟧", 11, "var(--muted)")
         + dog(360, 150, 0.9, bark=True) + bug(430, 100, 0.6) + '<path d="M410 80 l40 40 M450 80 l-40 40" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>' + '<g transform="translate(380,210)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="6" y="-2" width="22" height="4" fill="#E9B44C"/><path d="M-14 -10 l28 20" stroke="var(--bad)" stroke-width="3"/></g>'
         + label(380, 250, "⟦내보내기|remove⟧", 15, "var(--ink)", cls="d") + label(380, 275, "⟦벌레 치우고 열쇠 바꾸기|clear the bug, change the keys⟧", 11, "var(--muted)")
         + chest(660, 110, 0.9, grey=True) + '<path d="M590 185 L625 145" stroke="var(--good)" stroke-width="3"/><path d="M612 146 L627 143 L624 158" stroke="var(--good)" stroke-width="3" fill="none"/>' + chest(560, 200, 0.7, open_lid=True) + label(560, 235, "⟦여분 상자|spare chest⟧", 10, "var(--muted)")
         + label(633, 250, "⟦되돌리기|restore⟧", 15, "var(--ink)", cls="d") + label(633, 275, "⟦여분 상자로 제자리에|back in place from the spare⟧", 11, "var(--muted)")
         + label(380, 305, "⟦일지는 절대 지우지 않아요 — 나중에 읽어야 하니까요|never erase the diary — you\'ll need to read it later⟧", 12, "var(--ink)"))

# 5. 끝나면 모여서 적는다
P5 = svg(320, sky(320)
         + "".join(person(x, 100, s=0.7, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((40, "var(--good)"), (110, "#E9B44C"), (180, "#5B8DEF"), (250, None)))
         + '<g transform="translate(400,60)"><rect width="320" height="170" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="320" height="28" rx="8" fill="#C9A86A"/>' + label(160, 19, "⟦무슨 일이었나|WHAT HAPPENED⟧", 13, "#142033", cls="d")
         + "".join(label(16, 56 + i * 26, t, 12, "#142033", "start") for i, t in enumerate(("⟦왜 들어왔나 — 가짜 편지|how they got in — a fake letter⟧", "⟦왜 늦게 알았나 — 종이 고양이한테 묻혀서|why so late — the bell was lost among cats⟧", "⟦순서표에서 고칠 것 — 알림 담당 추가|fix in the book — add someone to tell⟧", "⟦다음 연습 — 다음 달 가짜 종|next drill — a fake bell next month⟧"))) + "</g>"
         + bell(300, 260, 0.6) + label(300, 300, "⟦가짜 종|a fake bell⟧", 11, "var(--muted)")
         + label(560, 300, "⟦순서표는 연습을 안 하면 그냥 종이예요|an unpracticed book is just paper⟧", 12, "var(--muted)"))

CHECK_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M40 40 l10 10" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><text x="32" y="37" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">?</text>')
LOCK_I = icon('<rect x="16" y="28" width="32" height="26" rx="5" fill="var(--bad)"/><path d="M22 28 V20 a10 10 0 0 1 20 0 V28" stroke="var(--bad)" stroke-width="5" fill="none"/>')
REMOVE_I = icon('<ellipse cx="30" cy="34" rx="12" ry="8" fill="var(--bad)"/><path d="M14 18 l32 32 M46 18 l-32 32" stroke="var(--night)" stroke-width="4" stroke-linecap="round"/>')
RESTORE_I = icon('<rect x="12" y="26" width="30" height="24" rx="3" fill="var(--stone)"/><rect x="34" y="18" width="20" height="18" rx="3" fill="#8B5E3C"/><path d="M28 14 a12 12 0 0 1 12 -6" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M38 4 l4 5 -6 2z" fill="var(--good)"/>')

PAGE = {
    "slug": "incident", "order": 50,
    "title": ("도둑 들었을 때 순서표", "The Order of Things When a Thief Gets In"),
    "h1": ("<em>사고 대응</em>이 뭐예요?", "What is <em>Incident Response</em>?"),
    "sub": ("사고 대응(Incident Response)을 도둑이 들었을 때 펴는 순서표 이야기로 풀어봤어요.",
            "Incident response, told as a story about the book you open when a thief gets in."),
    "panels": [
        {"svg": P1, "alt": ("종이 울리고 네 사람이 서로 다른 방향으로 뛰며 '누가 문 잠가요?', '누구한테 말하죠?'", "A bell rings and four people run in different directions asking who locks the doors? and who do we tell?"),
         "caption": ("종이 울렸어요. 다들 우왕좌왕이에요.", "The bell rang, and everyone is running around."),
         "small": ("누가 문을 잠그죠? 누가 도둑을 쫓죠? 누구한테 말하죠?", "Who locks the doors? Who chases the thief? Who do we tell?")},
        {"svg": P2, "alt": ("한 사람은 일지를 쓰레기통에 버리고, 한 사람은 엉뚱한 문을 잠그고, 도둑은 가방을 들고 아직 안에 있음", "One person throws the diary in the trash, another locks the wrong door, and the thief is still inside with a bag"),
         "caption": ("순서 없이 움직이면 더 망가져요.", "Moving without an order makes it worse."),
         "small": ('<a href="log-ko.html">일지</a>를 지워버리고, 엉뚱한 문을 잠그고, 도둑은 아직 안에 있어요.',
                   'The <a href="log-en.html">diary</a> gets erased, the wrong door gets locked, and the thief is still inside.')},
        {"svg": P3, "hero": True, "alt": ("'도둑 들었을 때 순서표' — 준비, 확인, 가두기, 내보내기, 되돌리기, 배우기. 종이 울리자 경비가 책을 펴고, 문 담당·벌레 담당·알림 담당이 서 있음", "The book — WHEN A THIEF GETS IN: prepare, confirm, contain, remove, restore, learn. The bell rings, the guard opens it, and three people stand ready: doors, bugs, telling"),
         "caption": ("사고 대응은 미리 정해둔 순서표대로 움직이는 거예요.", "Incident response is following the order you wrote down in advance."),
         "small": ("종이 울리면 순서표를 펴요. 누가 뭘 할지 이미 적혀 있어요.", "When the bell rings, open the book. Who does what is already written down."),
         "tricks": (4, [
             (CHECK_I, ("확인", "Confirm"), ("고양이인지 도둑인지", "cat or thief"), "warm"),
             (LOCK_I, ("가두기", "Contain"), ("못 퍼지게 문부터", "the door first, so it can\'t spread")),
             (REMOVE_I, ("내보내기", "Remove"), ("벌레와 도둑을 치워요", "clear out the bug and the thief")),
             (RESTORE_I, ("되돌리기", "Restore"), ("여분 상자로", "from the spare chest"), "calm"),
         ])},
        {"svg": P4, "alt": ("세 칸: 문을 잠그고 복도를 끊은 가두기, 경비견이 벌레를 쫓고 열쇠를 바꾸는 내보내기, 여분 상자에서 되돌리는 되돌리기", "Three panels: containing — door locked, hallway cut; removing — the dog chases the bug and keys are changed; restoring — the chest put back from the spare"),
         "caption": ("가두고, 내보내고, 되돌려요.", "Contain, remove, restore."),
         "small": ('먼저 퍼지지 않게 <a href="vlan-ko.html">방을 잠가요</a>. 그다음 <a href="edr-ko.html">벌레를 치우고</a> 열쇠를 바꾸고, <a href="backup-ko.html">여분 상자</a>로 되돌려요. 일지는 절대 지우지 않아요.',
                   'First <a href="vlan-en.html">lock the room</a> so it can\'t spread. Then <a href="edr-en.html">clear the bug</a>, change the keys, and restore from the <a href="backup-en.html">spare chest</a>. Never erase the diary.')},
        {"svg": P5, "alt": ("네 사람이 모여 '무슨 일이었나' 종이를 봄: 왜 들어왔나, 왜 늦게 알았나, 순서표에서 고칠 것, 다음 연습. 옆에 가짜 종", "Four people gather over a sheet — WHAT HAPPENED: how they got in, why so late, what to fix in the book, next drill; a fake bell beside"),
         "caption": ("끝나면 모여서 무슨 일이었는지 적어요.", "Afterwards, everyone gathers and writes down what happened."),
         "small": ("왜 들어왔는지, 왜 늦게 알았는지, 순서표에서 뭘 고칠지. 그리고 순서표는 연습을 안 하면 그냥 종이예요 — 가끔 가짜 종을 울려 봐요.", "How they got in, why it took so long to notice, what to fix in the book. And an unpracticed book is just paper — ring a fake bell now and then.")},
    ],
    "summary": (("<b>사고 대응</b> = 종이 울렸을 때 미리 정해둔 <b>순서표</b>대로 <b>확인 → 가두기 → 내보내기 → 되돌리기 → 배우기</b>.",
                 "<b>Incident response</b> = when the bell rings, follow the <b>book</b>: <b>confirm → contain → remove → restore → learn</b>."),
                ("Incident Response. 미국 NIST SP 800-61의 여섯 단계예요 — 준비, 탐지·분석, 격리, 제거, 복구, 교훈. 순서표는 플레이북, 가짜 종은 탁상 훈련.",
                 "The six steps of NIST SP 800-61 — preparation, detection & analysis, containment, eradication, recovery, lessons learned. The book is a playbook; the fake bell is a tabletop exercise.")),
    "glossary": [
        ("플레이북", "Playbook", ("순서표.", "The book."), ("사고 종류마다 한 장씩. 랜섬웨어용, 가짜 편지용, 잃어버린 노트북용.", "One per kind of incident: ransomware, fake letters, a lost laptop.")),
        ("탐지 · 분석", "Detection & analysis", ("고양이인지 도둑인지.", "Cat or thief?"), ('종이 울린 게 진짜인지 먼저 봐요. → <a href="soc-ko.html">성의 경비실</a>', 'First check whether the bell was real. → <a href="soc-en.html">the guard room</a>')),
        ("격리", "Containment", ("문 잠가 못 퍼지게.", "Lock the door so it can\'t spread."), ('방 하나를 잃더라도 성 전체는 지켜요. → <a href="edr-ko.html">방 문 잠그기</a>', 'Lose one room, keep the castle. → <a href="edr-en.html">locking the room</a>')),
        ("제거", "Eradication", ("벌레와 도둑 치우기.", "Clearing out the bug and the thief."), ('열쇠도 바꿔요 — 도둑이 복사해 갔을 테니까. → <a href="pam-ko.html">열쇠 모양 바꾸기</a>', 'Change the keys too — the thief will have copied them. → <a href="pam-en.html">reforging the key</a>')),
        ("복구", "Recovery", ("여분 상자로 되돌리기.", "Restoring from the spare chest."), ('되돌린 뒤에도 한동안 더 지켜봐요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'And keep watching for a while after. → <a href="backup-en.html">the spare chest far away</a>')),
        ("교훈", "Lessons learned", ("모여서 적기.", "Gathering to write it down."), ("탓하는 자리가 아니라 순서표를 고치는 자리예요.", "Not a blame session — a session for fixing the book.")),
        ("포렌식", "Forensics", ("일지 읽고 발자국 찾기.", "Reading the diary for footprints."), ('그래서 일지를 지우면 안 돼요. → <a href="log-ko.html">성 곳곳의 한 줄 일지</a>', 'Which is why the diary must never be erased. → <a href="log-en.html">the one-line diary</a>')),
        ("탁상 훈련", "Tabletop exercise", ("가짜 종 울려 보기.", "Ringing a fake bell."), ("도둑 없이 순서표대로 움직여 보는 연습.", "Walking through the book without a real thief.")),
    ],
}
