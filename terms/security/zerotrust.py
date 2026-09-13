from _draw import *

DOORS = (("⟦부엌|Kitchen⟧", False), ("⟦회의실|Meeting⟧", False), ("⟦창고|Storage⟧", False), ("⟦금고|Vault⟧", False), ("⟦서재|Study⟧", False))
GUARD = dict(hat="var(--good)", shirt="var(--good)")
DISGUISE = dict(hat="var(--good)", shirt="#2E3D57", face=MASK)   # 훔친 모자를 쓴 도둑


def gate_post(x, y):
    return (f'<rect x="{x}" y="{y}" width="14" height="{300 - y}" fill="var(--stone-dark)"/>'
            f'{battlements(x - 6, y - 16, 26, 1, "var(--stone-dark)", 18)}')


# 1. 옛날 성은 성문만 지켰다
P1 = svg(300, corridor(300, DOORS, marks=False) + gate_post(14, 60)
         + person(60, 150, s=0.7, face=SMILE, **GUARD) + bubble(50, 40, 110, 36, "⟦통과!|Go ahead!⟧", 15, "var(--panel)", "var(--good)", "bottom")
         + '<path d="M140 250 C300 230 420 260 560 220" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
         + person(330, 150, s=0.85, **DISGUISE)
         + label(420, 285, "⟦성문 하나만 지나면 어디든|past one gate, anywhere you like⟧", 14, "var(--muted)"))

# 2. 안에 있다고 다 믿으면 안 된다
VAULT = ('<rect x="300" y="40" width="160" height="200" rx="8" fill="var(--night)"/>'
         '<circle cx="380" cy="140" r="34" fill="none" stroke="var(--stone)" stroke-width="8"/><circle cx="380" cy="140" r="8" fill="var(--accent)"/>'
         + label(380, 30, "⟦금고|Vault⟧", 14, "var(--muted)"))
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>' + VAULT
         + person(180, 110, s=0.95, **DISGUISE)
         + '<path d="M250 150 L292 150" stroke="var(--night)" stroke-width="4" stroke-linecap="round"/>'
         + f'<g transform="translate(560,80)"><path d="M6 22 Q30 -6 54 22 Z" fill="var(--good)"/><path d="M0 30 L60 30" stroke="var(--bad)" stroke-width="4" stroke-dasharray="6 6"/></g>'
         + label(590, 130, "⟦훔친 모자|a stolen hat⟧", 15, "var(--bad)")
         + label(590, 152, "⟦아무도 안 물어봐요|nobody asks⟧", 13, "var(--muted)"))

# 3. 제로 트러스트 = 문마다 물어보는 성 (hero)
MINI_GUARDS = "".join(person(70 + i * 140 + 62, 128, s=0.45, face=EYES, **GUARD) for i in range(5))
ASKS = (bubble(40, 14, 120, 34, "⟦누구세요?|Who are you?⟧", 13, "var(--panel)", "var(--good)", "bottom")
        + bubble(320, 14, 120, 34, "⟦왜요?|What for?⟧", 13, "var(--panel)", "var(--good)", "bottom")
        + bubble(600, 14, 130, 34, "⟦지금 괜찮아요?|All good right now?⟧", 12, "var(--panel)", "var(--good)", "bottom"))
BADGE = '<rect x="46" y="60" width="30" height="38" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="2"/><circle cx="61" cy="73" r="6" fill="var(--accent)"/><rect x="52" y="84" width="18" height="4" fill="var(--line)"/>'
P3 = svg(320, corridor(320, tuple(("", False) for _ in DOORS), marks=False) + MINI_GUARDS + ASKS
         + person(330, 170, hat=None, shirt="#4A5A72", s=0.85, face=SMILE, extra=BADGE)
         + label(380, 305, "⟦성문을 지났어도, 문마다 다시 물어요|even past the gate, every door asks again⟧", 14, "var(--muted)"))

# 4. 열쇠는 방 하나, 잠깐만
KEY = ('<g transform="translate(120,110)"><circle cx="0" cy="0" r="34" fill="none" stroke="#E9B44C" stroke-width="14"/>'
       '<rect x="30" y="-8" width="120" height="16" fill="#E9B44C"/><rect x="110" y="8" width="12" height="18" fill="#E9B44C"/><rect x="134" y="8" width="12" height="24" fill="#E9B44C"/>'
       '<path d="M150 0 L200 -30" stroke="var(--muted)" stroke-width="2"/>'
       '<rect x="196" y="-70" width="190" height="54" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
       + label(291, -47, "⟦부엌 · 오늘 3시까지|Kitchen · until 3 pm today⟧", 14, "var(--ink)") + label(291, -27, "⟦한 방, 한동안|one room, for a while⟧", 12, "var(--muted)") + "</g>")


def door(x, y, name, ok):
    mark = ('<path d="M-14 0 l10 10 l20 -22" stroke="var(--good)" stroke-width="6" fill="none" stroke-linecap="round"/>' if ok
            else '<path d="M-14 -14 l28 28 M14 -14 l-28 28" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>')
    return (f'<g transform="translate({x},{y})"><rect x="-40" y="0" width="80" height="130" rx="3" fill="{WOOD}"/><circle cx="26" cy="70" r="5" fill="#E9B44C"/>'
            f'{label(0, -12, name, 15, "var(--ink)")}<g transform="translate(0,64)">{mark}</g></g>')


P4 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>' + KEY
         + door(500, 90, "⟦부엌|Kitchen⟧", True) + door(640, 90, "⟦금고|Vault⟧", False)
         + label(570, 258, "⟦부엌 열쇠로 금고는 못 열어요|a kitchen key won\'t open the vault⟧", 14, "var(--muted)"))

# 5. 매번 묻는 건 귀찮다 → 확인하고 믿는다
SCANNER = ('<g transform="translate(300,60)"><rect width="120" height="150" rx="10" fill="var(--night)"/>'
           '<rect x="14" y="14" width="92" height="92" rx="6" fill="var(--sky)"/>'
           f'<circle cx="60" cy="50" r="18" fill="{SKIN}"/><rect x="42" y="72" width="36" height="26" rx="8" fill="var(--good)"/>'
           '<circle cx="60" cy="128" r="12" fill="var(--good)"/><path d="M53 128 l5 5 l10 -11" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/></g>')
P5 = svg(260, '<rect width="760" height="260" fill="var(--good-soft)"/>' + SCANNER
         + person(160, 90, s=0.9, face=SMILE, **GUARD)
         + '<path d="M250 150 L290 150" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M280 140 L292 150 L280 160" stroke="var(--good)" stroke-width="4" fill="none"/>'
         + label(360, 240, "⟦아는 얼굴은 1초|a known face: one second⟧", 14, "var(--muted)")
         + label(590, 110, "⟦아무도 안 믿는다 ✗|\"trust no one\" ✗⟧", 16, "var(--bad)")
         + label(590, 150, "⟦확인하고 믿는다 ✓|\"check, then trust\" ✓⟧", 16, "var(--good)"))

WHO_I = icon('<circle cx="32" cy="22" r="10" fill="var(--good)"/><rect x="18" y="36" width="28" height="20" rx="8" fill="var(--good)"/>')
KEY_I = icon('<circle cx="22" cy="32" r="10" fill="none" stroke="var(--accent)" stroke-width="5"/><rect x="30" y="29" width="26" height="6" fill="var(--accent)"/><rect x="46" y="35" width="4" height="7" fill="var(--accent)"/><rect x="52" y="35" width="4" height="9" fill="var(--accent)"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="3"/><path d="M32 16 V32 L42 40" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "zerotrust", "order": 12,
    "title": ("문마다 물어보는 성", "The Castle That Always Asks"),
    "h1": ("<em>제로 트러스트</em>가 뭐예요?", "What is <em>Zero Trust</em>?"),
    "sub": ("제로 트러스트(Zero Trust)를 문마다 다시 물어보는 성 이야기로 풀어봤어요.",
            "Zero Trust, told as a story about a castle where every door asks again."),
    "panels": [
        {"svg": P1, "alt": ("성문 경비가 '통과!'라고 하고, 초록 모자를 쓴 가면 쓴 사람이 복도를 따라 금고 쪽으로 감", "A gate guard says 'go ahead' and a masked figure in a green hat strolls down the hallway toward the vault"),
         "caption": ("옛날 성은 성문만 지켰어요.", "The old castle only guarded the gate."),
         "small": ("한 번 들어오면 어디든 갈 수 있었어요.", "Once you were in, you could go anywhere.")},
        {"svg": P2, "alt": ("금고 앞에서 초록 모자를 쓴 가면 쓴 사람이 다이얼을 돌리고, 옆에 '훔친 모자'", "A masked figure in a green hat turning the vault dial, with a note: a stolen hat"),
         "caption": ("안에 있다고 다 믿으면 안 돼요.", "Being inside doesn't make you trustworthy."),
         "small": ('훔친 모자만 있으면 성문은 통과해요. <a href="ioc-ko.html">발자국</a>도 안 남기고요.',
                   'A stolen hat gets you through the gate — without even leaving a <a href="ioc-en.html">footprint</a>.')},
        {"svg": P3, "hero": True, "alt": ("문마다 작은 경비가 서 있고, 명찰을 보여주는 사람 위로 '누구세요?', '왜요?', '지금 괜찮아요?' 말풍선", "A small guard at every door; a person shows a badge under bubbles saying Who are you?, What for?, All good right now?"),
         "caption": ("제로 트러스트는 문마다 물어보는 성이에요.", "Zero Trust is the castle where every door asks."),
         "small": ("성문을 지났어도, 방마다 다시 물어요.", "Even past the gate, each room asks again."),
         "tricks": (3, [
             (WHO_I, ("누구세요?", "Who are you?"), ("얼굴, 모자, 암호까지", "face, hat, and a password"), "calm"),
             (KEY_I, ("이 방에 볼일 있어요?", "Any business in this room?"), ("필요한 방만", "only the rooms you need"), "warm"),
             (CLOCK_I, ("지금 괜찮아요?", "All good right now?"), ("신발에 진흙은 안 묻었나", "no mud on your shoes?")),
         ])},
        {"svg": P4, "alt": ("'부엌 · 오늘 3시까지' 꼬리표가 달린 열쇠, 부엌 문엔 초록 체크, 금고 문엔 빨간 X", "A key tagged 'Kitchen · until 3 pm today'; a green check on the kitchen door, a red X on the vault"),
         "caption": ("열쇠는 방 하나, 잠깐만이에요.", "One key, one room, for a while."),
         "small": ("부엌 열쇠로 금고는 못 열어요. 시간이 지나면 열쇠가 사라져요.", "A kitchen key won't open the vault, and it stops working after a while.")},
        {"svg": P5, "alt": ("얼굴 확인 기계가 초록 체크를 띄우고 친구가 빠르게 통과함. 옆에 '아무도 안 믿는다 ✗ / 확인하고 믿는다 ✓'", "A face scanner shows a green check and a friend walks straight through; beside it: 'trust no one ✗ / check, then trust ✓'"),
         "caption": ("매번 묻는 건 귀찮아요.", "Asking every time is a bother."),
         "small": ("그래서 얼굴 확인은 기계가 1초에 해요. '아무도 안 믿는다'가 아니라 '확인하고 믿는다'예요.", "So a machine checks faces in a second. It's not \"trust no one\" — it's \"check, then trust.\"")},
    ],
    "summary": (("<b>제로 트러스트</b> = 성문을 지났어도 <b>문마다 다시 묻는</b> 성. 열쇠는 방 하나, 잠깐만.",
                 "<b>Zero Trust</b> = the castle that <b>asks again at every door</b>, even past the gate. One key, one room, for a while."),
                ("성벽 안쪽이라고 자동으로 믿지 않아요. 존 킨더백(John Kindervag)이 2010년에 이름 붙였고, 미국 NIST가 SP 800-207(2020)로 정리했어요.",
                 "Nothing is trusted just for being inside the walls. Named by John Kindervag in 2010; written up by NIST as SP 800-207 in 2020.")),
    "glossary": [
        ("경계 방어", "Perimeter security", ("성문만 지키기.", "Guarding only the gate."), ("옛날 방식. '성과 해자(castle-and-moat)'라고도 불러요.", "The old way. Also called castle-and-moat.")),
        ("신원 확인", "Identity / MFA", ("누구세요?", "Who are you?"), ("얼굴 하나로는 부족해서 모자와 암호도 같이 봐요. 그게 다중 인증(MFA).", "One face isn't enough, so the hat and a password are checked too — that's multi-factor authentication.")),
        ("최소 권한", "Least privilege", ("방 하나 열쇠.", "A key to one room."), ("볼일 있는 방만, 필요한 동안만.", "Only the rooms you need, only while you need them.")),
        ("기기 상태", "Device posture", ("신발에 진흙?", "Mud on your shoes?"), ("그 사람이 들고 온 컴퓨터가 지금 괜찮은지도 봐요.", "The computer they brought is checked too, not just the person.")),
        ("마이크로 세그멘테이션", "Micro-segmentation", ("문마다 파수꾼.", "A guard at every door."), ('복도를 잘게 나눠서 한 방이 뚫려도 옆방은 못 가요. → <a href="ndr-ko.html">복도 이야기</a>', 'Chop the hallway into pieces so one open room doesn\'t open the next. → <a href="ndr-en.html">the hallway story</a>')),
        ("지속 검증", "Continuous verification", ("들어간 뒤에도 봐요.", "Still watching after you're in."), ('한 번 통과가 끝이 아니에요. <a href="edr-ko.html">경비견</a>이 계속 봐요.', 'Getting in isn\'t the end. The <a href="edr-en.html">dog</a> keeps watching.')),
        ("NIST SP 800-207", "NIST SP 800-207", ("규칙책.", "The rulebook."), ("미국 표준기관이 2020년에 낸 제로 트러스트 안내서.", "The 2020 Zero Trust guide from the US standards body.")),
    ],
}
