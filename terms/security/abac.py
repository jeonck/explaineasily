from _draw import *

COOK = "#E9B44C"
GUARD = dict(hat="var(--good)", shirt="var(--good)")
COOK_P = dict(hat=COOK, shirt="#4A5A72", face=SMILE)
TAG_FILL = {"who": "var(--good-soft)", "room": "var(--accent-soft)", "when": "var(--sky)"}
TAG_INK = {"who": "var(--good)", "room": "var(--accent)", "when": "var(--ink)"}


def tag(x, y, text, kind="who", w=110, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="{-w / 2}" y="-14" width="{w}" height="28" rx="14" fill="{TAG_FILL[kind]}" stroke="{TAG_INK[kind]}" stroke-width="2"/>'
            f'<circle cx="{-w / 2 + 12}" r="4" fill="{TAG_INK[kind]}"/>{label(6, 5, text, 13, "var(--ink)")}</g>')


def hat(x, y, color, s=1.0):
    return f'<path d="M6 22 Q30 -6 54 22 Z" fill="{color}" transform="translate({x - 30},{y - 22}) scale({s})"/>'


def door(x, y, s=1.0, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" width="72" height="120" rx="3" fill="{WOOD}"/><circle cx="24" cy="64" r="4" fill="#E9B44C"/>{extra}</g>')


def sign(x, y, lines, w=250, ok=None):
    rows = "".join(label(20, 34 + i * 26, t, 15, "var(--ink)", "start") for i, t in enumerate(lines))
    verdict = ""
    if ok is not None:
        verdict = (f'<rect x="0" y="{22 + len(lines) * 26}" width="{w}" height="34" fill="{"var(--good)" if ok else "var(--bad)"}"/>'
                   + label(w / 2, 45 + len(lines) * 26, "⟦→ 열림|→ OPEN⟧" if ok else "⟦→ 닫힘|→ CLOSED⟧", 16, "#FFF"))
    h = 30 + len(lines) * 26 + (34 if ok is not None else 0)
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<circle cx="14" cy="14" r="3" fill="var(--stone-dark)"/><circle cx="{w - 14}" cy="14" r="3" fill="var(--stone-dark)"/>{rows}{verdict}</g>')


CHECK = "✓"
CLOCK = lambda x, y, night=False: (f'<g transform="translate({x},{y})"><circle r="26" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
                                   f'<path d="M0 -16 V0 L{"-10 -8" if night else "10 8"}" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')

# 1. 모자로는 '밤에만'을 못 적는다
PILE = "".join(hat(80 + (i % 5) * 26, 200 - (i // 5) * 14, c, 0.7) for i, c in enumerate((COOK, "#5B8DEF", "var(--stone-dark)", "var(--accent)", "var(--good)") * 4))
P1 = svg(260, '<rect width="760" height="260" fill="var(--accent-soft)"/>' + PILE
         + label(130, 240, "⟦'요리사·밤' 모자, '요리사·손님 없음' 모자…|a 'cook·night' hat, a 'cook·no guests' hat…⟧", 12, "var(--muted)")
         + hat(400, 110, COOK, 1.6) + label(400, 150, "⟦요리사|Cook⟧", 14, "var(--ink)")
         + label(470, 122, "+", 30, "var(--muted)", cls="d") + CLOCK(540, 110, True) + label(540, 160, "02:00", 14, "var(--ink)")
         + label(610, 122, "=", 30, "var(--muted)", cls="d") + label(670, 124, "?", 40, "var(--accent)", cls="d")
         + label(540, 240, "⟦'요리사인데 밤에만' — 모자로는 못 적어요|'cook, but only at night' — no hat says that⟧", 13, "var(--muted)"))

# 2. 사람에게도 방에도 꼬리표
P2 = svg(320, sky(320)
         + person(200, 110, s=1.0, **COOK_P)
         + tag(90, 90, "⟦요리사|cook⟧", "who") + tag(90, 130, "⟦3층 근무|works on 3F⟧", "who", 120) + tag(90, 170, "⟦입사 2년|2 years here⟧", "who", 120)
         + "".join(f'<path d="M{x1} {y} L{x2} {y}" stroke="var(--good)" stroke-width="2" stroke-dasharray="4 4"/>' for x1, x2, y in ((150, 200, 90), (150, 200, 130), (150, 200, 170)))
         + door(560, 60, 1.0) + tag(560, 210, "⟦부엌|kitchen⟧", "room") + tag(560, 250, "⟦날카로운 도구|sharp tools⟧", "room", 130)
         + tag(380, 40, "⟦지금 02:00|now 02:00⟧", "when", 120) + tag(380, 80, "⟦손님 없음|no guests⟧", "when", 120)
         + label(380, 300, "⟦모자는 그중 하나일 뿐이에요|the hat is only one of the tags⟧", 14, "var(--muted)"))

# 3. ABAC = 꼬리표로 문장을 (hero)
P3 = svg(340, sky(340) + door(660, 60, 1.0)
         + sign(330, 40, ("⟦요리사이고|is a cook⟧ " + CHECK, "⟦낮이고|it's daytime⟧ " + CHECK, "⟦손님이 없으면|no guests inside⟧ " + CHECK), 260, ok=True)
         + person(180, 130, s=0.9, face=EYES, **GUARD)
         + tag(120, 70, "⟦요리사|cook⟧", "who", 90, 0.8) + tag(120, 100, "⟦14:00|14:00⟧", "when", 90, 0.8) + tag(120, 130, "⟦손님 0|guests: 0⟧", "when", 90, 0.8)
         + person(40, 160, s=0.9, **COOK_P)
         + label(380, 320, "⟦문지기가 꼬리표를 문장에 맞춰봐요|the gatekeeper checks the tags against the sentence⟧", 14, "var(--muted)"))

# 4. 같은 사람, 낮엔 열리고 밤엔 닫힌다
P4 = svg(280, '<rect width="380" height="280" fill="var(--sky)"/><rect x="380" width="380" height="280" fill="var(--night)"/>'
         + '<circle cx="60" cy="50" r="24" fill="#FFD166"/>' + '<circle cx="700" cy="50" r="22" fill="#F5E6B8"/>'
         + person(120, 100, s=0.9, **COOK_P) + label(150, 240, "14:00", 16, "var(--ink)")
         + door(280, 60, 0.9, '<path d="M-14 60 l10 10 l20 -22" stroke="var(--good)" stroke-width="6" fill="none" stroke-linecap="round"/>')
         + person(500, 100, s=0.9, **COOK_P) + label(530, 240, "02:00", 16, "#F5E6B8")
         + door(660, 60, 0.9, '<path d="M-14 -14 l28 28 M14 -14 l-28 28" stroke="var(--bad)" stroke-width="6" stroke-linecap="round" transform="translate(0,64)"/>')
         + label(190, 265, "⟦같은 요리사|the same cook⟧", 13, "var(--muted)") + label(570, 265, "⟦같은 모자, 다른 시간|same hat, different hour⟧", 13, "#C9D5E6"))

# 5. 문장이 길어지면 아무도 못 읽는다
LONG = sign(300, 20, ("⟦요리사이고|is a cook⟧", "⟦낮이거나 당직이고|daytime, or on duty⟧", "⟦손님이 없거나 셋 이하고|no guests, or at most three⟧", "⟦3층 근무자면서|works on 3F, and⟧", "⟦지난주 교육을 받았고|took last week's training⟧", "⟦비 오는 날은 빼고…|except on rainy days…⟧"), 300)
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + LONG
         + person(160, 110, s=0.9, face=FROWN + SWEAT, **GUARD)
         + person(40, 130, s=0.85, hat=COOK, shirt="#4A5A72", face=FROWN)
         + bubble(20, 50, 150, 34, "⟦왜 안 열려요?|why won\'t it open?⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + label(650, 150, "…", 40, "var(--muted)", cls="d")
         + label(680, 280, "⟦답하기 어려워요|hard to answer⟧", 13, "var(--bad)"))

WHO_I = icon('<rect x="8" y="20" width="48" height="24" rx="12" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><circle cx="20" cy="32" r="4" fill="var(--good)"/>')
ROOM_I = icon('<rect x="8" y="20" width="48" height="24" rx="12" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><circle cx="20" cy="32" r="4" fill="var(--accent)"/>')
WHEN_I = icon('<circle cx="32" cy="32" r="20" fill="var(--sky)" stroke="var(--ink)" stroke-width="3"/><path d="M32 18 V32 L40 38" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SIGN_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="18" y="22" width="24" height="3" fill="var(--line)"/><rect x="18" y="30" width="28" height="3" fill="var(--line)"/><rect x="18" y="38" width="20" height="3" fill="var(--line)"/>')

PAGE = {
    "slug": "abac", "order": 18,
    "title": ("문지기의 조건 문장", "The Gatekeeper's If-Sentence"),
    "h1": ("<em>ABAC</em>이 뭐예요?", "What is <em>ABAC</em>?"),
    "sub": ("속성 기반 접근 제어(Attribute-Based Access Control)를 꼬리표와 조건 문장 이야기로 풀어봤어요.",
            "Attribute-Based Access Control, told as a story about tags and if-sentences."),
    "panels": [
        {"svg": P1, "alt": ("모자 더미와, '요리사 모자 + 새벽 2시 = ?'", "A pile of hats, and 'cook hat + 2 a.m. = ?'"),
         "caption": ("모자로는 '밤에만'을 못 적어요.", "A hat can't say 'only at night'."),
         "small": ('<a href="rbac-ko.html">모자 이야기</a>의 마지막 장면이에요. 조건마다 모자를 만들면 백 개가 돼요.',
                   'The last scene of the <a href="rbac-en.html">hat story</a>. A hat for every condition means a hundred hats.')},
        {"svg": P2, "alt": ("요리사에게 '요리사, 3층 근무, 입사 2년' 꼬리표, 부엌 문에 '부엌, 날카로운 도구' 꼬리표, 위에 '지금 02:00, 손님 없음' 꼬리표", "Tags on the cook (cook, works on 3F, 2 years here), tags on the kitchen door (kitchen, sharp tools), and situation tags above (now 02:00, no guests)"),
         "caption": ("사람에게도, 방에도, 지금 상황에도 꼬리표가 있어요.", "People, rooms and the moment all carry tags."),
         "small": ("모자는 그중 하나일 뿐이에요.", "The hat is just one of them.")},
        {"svg": P3, "hero": True, "alt": ("문 옆 팻말에 '요리사이고 ✓ 낮이고 ✓ 손님이 없으면 ✓ → 열림'. 문지기가 요리사의 꼬리표(요리사, 14:00, 손님 0)를 들고 맞춰봄", "A sign by the door reads 'is a cook ✓, it's daytime ✓, no guests ✓ → OPEN'; the gatekeeper holds the cook's tags (cook, 14:00, guests: 0) and compares"),
         "caption": ("ABAC은 꼬리표로 문장을 만들어요.", "ABAC turns tags into a sentence."),
         "small": ("'요리사이고, 낮이고, 손님이 없으면 열림.' 문지기가 꼬리표를 문장에 맞춰봐요.", "'If cook, and daytime, and no guests: open.' The gatekeeper checks the tags against it."),
         "tricks": (4, [
             (WHO_I, ("사람 꼬리표", "Person tags"), ("역할, 부서, 근속", "role, team, tenure"), "calm"),
             (ROOM_I, ("방 꼬리표", "Room tags"), ("어떤 방, 얼마나 비밀", "which room, how secret"), "warm"),
             (WHEN_I, ("상황 꼬리표", "Moment tags"), ("시간, 장소, 기기", "time, place, device")),
             (SIGN_I, ("문장", "The sentence"), ("셋을 엮은 규칙", "the rule that ties them together"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 낮: 같은 요리사, 14:00, 문에 체크. 오른쪽 밤: 같은 요리사, 02:00, 문에 X", "Left, daytime: the same cook at 14:00, door checked. Right, night: the same cook at 02:00, door crossed"),
         "caption": ("같은 사람인데 낮엔 열리고 밤엔 닫혀요.", "Same person: open by day, shut at night."),
         "small": ("모자를 새로 만들 필요가 없어요. 문장 하나로 끝.", "No new hat needed. One sentence does it.")},
        {"svg": P5, "alt": ("여섯 줄짜리 긴 팻말 앞에서 문지기가 땀을 흘리고, 요리사는 '왜 안 열려요?' 하고 물음", "A six-line sign; the gatekeeper sweats and the cook asks why it won't open"),
         "caption": ("문장이 길어지면 아무도 못 읽어요.", "A long sentence, and nobody can read it."),
         "small": ("'왜 안 열리지?'에 답하기 어려워요. 그래서 보통 모자(RBAC)로 크게 나누고, 조건은 조금만 얹어요.", "'Why won't it open?' gets hard to answer. So most castles sort by hat (RBAC) first and add only a few conditions on top.")},
    ],
    "summary": (("<b>ABAC</b> = 모자 대신, 사람·방·상황의 <b>꼬리표</b>로 만든 <b>문장</b>이 문을 열어요.",
                 "<b>ABAC</b> = instead of a hat, a <b>sentence</b> built from <b>tags</b> on the person, the room and the moment opens the door."),
                ("Attribute-Based Access Control. 미국 NIST가 SP 800-162(2014)로 정리했어요. 클라우드 권한(AWS IAM의 조건)이 이 방식이고, 실무에선 RBAC 위에 조건을 얹어 써요.",
                 "Attribute-Based Access Control, written up by NIST as SP 800-162 (2014). Cloud permissions (AWS IAM conditions) work this way; in practice it's layered on top of RBAC.")),
    "glossary": [
        ("속성", "Attribute", ("꼬리표.", "A tag."), ("사람, 방, 상황에 붙은 사실 하나. '요리사', '3층', '02:00'.", "One fact about a person, room or moment: 'cook', '3F', '02:00'.")),
        ("주체", "Subject", ("사람 꼬리표.", "The person's tags."), ("들어가려는 쪽. 역할, 부서, 근속, 교육 이수.", "Who wants in: role, team, tenure, training.")),
        ("자원", "Resource", ("방 꼬리표.", "The room's tags."), ("들어가려는 곳. 어떤 방인지, 얼마나 비밀인지.", "What they want into: which room, how secret.")),
        ("환경", "Environment", ("상황 꼬리표.", "The moment's tags."), ("시간, 장소, 어떤 기기로 왔나, 손님이 있나.", "Time, place, which device, whether guests are in.")),
        ("정책", "Policy", ("문장.", "The sentence."), ('"요리사이고 낮이고 손님이 없으면 열림." → <a href="rbac-ko.html">모자 이야기</a>', '"If cook and daytime and no guests: open." → <a href="rbac-en.html">the hat story</a>')),
        ("정책 결정 지점", "Policy Decision Point (PDP)", ("문장을 읽는 문지기.", "The gatekeeper who reads the sentence."), ("꼬리표를 문장에 맞춰 '열림/닫힘'을 정해요.", "Matches tags to the sentence and says open or closed.")),
        ("정책 시행 지점", "Policy Enforcement Point (PEP)", ("문을 여닫는 손.", "The hand on the door."), ("문지기의 결정을 실제로 행해요.", "Actually does what the gatekeeper decided.")),
        ("정책 언어", "Policy language", ("문장 쓰는 법.", "How sentences are written."), ("XACML, Cedar, AWS IAM 조건문 같은 것들.", "XACML, Cedar, AWS IAM condition blocks.")),
    ],
}
