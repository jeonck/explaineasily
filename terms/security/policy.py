from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
NEW = dict(hat=None, shirt="#4A5A72")
INSPECTOR = dict(hat="var(--stone-dark)", shirt="#2E3D57", face=EYES, extra='<rect x="50" y="66" width="30" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M56 78 h18 M56 86 h18 M56 94 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>')
KEY = '<g transform="translate(66,78) rotate(-30)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><path d="M8 0 h22 M22 0 v7 M28 0 v6" stroke="#E9B44C" stroke-width="4" stroke-linecap="round"/></g>'


def door(x, y, w=50, h=80, open_=False, lock=False):
    if open_:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="var(--night)"/>'
                f'<path d="M{x} {y} l{w * 0.45} 10 v{h - 20} l-{w * 0.45} 10z" fill="{WOOD}"/>')
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{WOOD}"/><circle cx="{x + w - 10}" cy="{y + h / 2}" r="4" fill="#E9B44C"/>'
    if lock:
        out += f'<rect x="{x + w / 2 - 8}" y="{y + h / 2 - 2}" width="16" height="14" rx="2" fill="#E9B44C"/><path d="M{x + w / 2 - 5} {y + h / 2 - 2} v-6 a5 5 0 0 1 10 0 v6" stroke="#E9B44C" stroke-width="3" fill="none"/>'
    return out


def paper(x, y, s=1.0, rot=0, text=None, stamp=None):
    tx = label(0, 4, text, 10, "#142033", cls="d") if text else ""
    st = f'<circle cx="14" cy="18" r="9" fill="{stamp}"/>' if stamp else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -16 h28 M-18 -8 h18" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{tx}{st}</g>')


def crown(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 10 l-4 -30 l14 12 l16 -22 l16 22 l14 -12 l-4 30z" fill="#E9B44C" stroke="#C9822B" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="-28" y="8" width="56" height="10" rx="3" fill="#C9822B"/></g>')


def royal_seal(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="28" fill="#7B3FA0" stroke="#E9B44C" stroke-width="4"/>{crown(0, 2, 0.5)}</g>'


def scroll(x, y, w, h, title, tiers=(), size=12):
    """두루마리. tiers: (색, 제목, 부연) 목록."""
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect x="-10" y="-11" width="{w + 20}" height="22" rx="11" fill="#C9A86A"/><rect x="-10" y="{h - 11}" width="{w + 20}" height="22" rx="11" fill="#C9A86A"/>'
           + label(w / 2, 38, title, 14, "#142033", cls="d"))
    for i, (c, t, sub) in enumerate(tiers):
        yy = 74 + i * 50
        out += f'<circle cx="30" cy="{yy - 5}" r="9" fill="{c}"/>' + label(48, yy, t, size, "#142033", "start", cls="d") + label(48, yy + 19, sub, size - 1, "#142033", "start")
    return out + "</g>"


def calendar(x, y, s=1.0, text="", color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="-26" y="-22" width="52" height="12" rx="4" fill="{color}"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/>{label(0, 12, text, 12, "#142033", cls="d")}</g>')


# 1. 성 사람마다 다르게 해요
P1 = svg(300, sky(300)
         + door(60, 90, lock=True) + person(112, 100, s=0.6, face=SMILE, **GUARD) + label(100, 205, "⟦잠가요|locks it⟧", 11, "var(--muted)")
         + door(250, 90, open_=True) + person(302, 100, s=0.6, face=EYES, **GUARD) + label(290, 205, "⟦안 잠가요|doesn\'t⟧", 11, "var(--muted)")
         + '<rect x="430" y="140" width="90" height="10" rx="2" fill="#5A3B22"/><rect x="436" y="150" width="8" height="30" fill="#5A3B22"/><rect x="506" y="150" width="8" height="30" fill="#5A3B22"/>'
         + paper(455, 112, 0.6, rot=-8) + paper(485, 116, 0.6, rot=6) + person(540, 100, s=0.6, face=SMILE, **CLERK) + label(480, 205, "⟦종이는 책상에|papers left out⟧", 11, "var(--muted)")
         + person(630, 100, s=0.6, face=SMILE, extra=KEY, **CLERK) + person(690, 110, s=0.55, face=EYES, **NEW) + label(670, 205, "⟦열쇠를 빌려줘요|lends the key⟧", 11, "var(--muted)")
         + label(380, 270, "⟦'그건 그 사람 방식이죠' — 성에는 정해진 게 없어요|\'that\'s just how he does it\' — nothing in the castle is decided⟧", 12, "var(--ink)", cls="d"))

# 2. 도둑은 제일 헐렁한 문으로 와요 / 새 사람은 누굴 따라요?
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + door(80, 90, open_=True) + person(150, 100, s=0.75, face=MASK) + label(190, 200, "⟦열린 문 하나면 충분해요|one open door is enough⟧", 10, "var(--muted)")
         + label(190, 240, "⟦도둑은 제일 헐렁한 문으로|thieves pick the loosest door⟧", 13, "var(--ink)", cls="d") + label(190, 262, "⟦잘 잠근 아홉 문은 소용없어요|nine locked doors don\'t help⟧", 11, "var(--bad)")
         + person(420, 110, s=0.65, face=SMILE, **GUARD) + bubble(400, 30, 120, 34, "⟦잠가!|lock it!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(540, 120, s=0.7, face=FROWN + SWEAT, **NEW) + label(565, 215, "⟦새로 온 사람|the new one⟧", 10, "var(--muted)")
         + person(640, 110, s=0.65, face=SMILE, **GUARD) + bubble(600, 30, 140, 34, "⟦열어 둬!|leave it!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(570, 240, "⟦새 사람은 누굴 따라요?|who does the new one follow?⟧", 13, "var(--ink)", cls="d") + label(570, 262, "⟦정한 게 없으면 운이에요|nothing decided means luck⟧", 11, "var(--accent)")
         + label(380, 292, "⟦사람마다 다르면 성 전체가 제일 헐렁한 사람만큼만 안전해요|when everyone differs, the castle is only as safe as its loosest person⟧", 10, "var(--muted)"))

# 3. 왕이 규칙 두루마리를 써요 (hero)
TIERS = (("var(--accent)", "⟦무엇을 — 정책|WHAT — the policy⟧", "⟦문은 늘 잠근다|every door stays locked⟧"),
         ("#5B8DEF", "⟦어떻게 — 표준·절차|HOW — standard and procedure⟧", "⟦쇠 자물쇠, 나갈 때마다, 열쇠는 경비실에|iron lock, every time you leave, key to the guard room⟧"),
         ("#7B3FA0", "⟦예외 — 왕의 도장|EXCEPTION — the king\'s seal⟧", "⟦도장 없는 예외는 없어요|no seal, no exception⟧"))
P3 = svg(360, sky(360)
         + scroll(60, 50, 440, 220, "⟦성의 규칙|THE CASTLE RULES⟧", TIERS)
         + person(560, 100, s=0.95, face=SMILE, **KING) + royal_seal(690, 150, 1.0) + label(690, 200, "⟦왕의 도장|the king\'s seal⟧", 11, "var(--muted)")
         + label(620, 240, "⟦왕이 쓰고, 왕이 도장 찍어요|the king writes it and seals it⟧", 11, "var(--muted)")
         + label(380, 305, "⟦무엇을 → 어떻게 → 예외는 도장으로|what → how → exceptions by seal⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦누가 물어도 같은 답이 나와요|whoever you ask, the same answer comes out⟧", 12, "var(--muted)"))

# 4. 두루마리는 읽히고 연습돼야 해요 / 예외는 도장으로만
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + scroll(50, 50, 150, 100, "⟦성의 규칙|THE RULES⟧", (), 10) + '<path d="M70 100 h110 M70 116 h80 M70 132 h100" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>'
         + person(270, 60, s=0.7, face=SMILE, **GUARD) + '<path d="M262 96 l-40 -14" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>'
         + "".join(person(60 + i * 55, 165, s=0.55, face=SMILE, hat=h, shirt="#4A5A72") for i, h in enumerate((None, "#5B8DEF", "var(--stone-dark)", None, "var(--good)")))
         + label(190, 255, "⟦모두가 읽고, 연습해요|everyone reads it and practices⟧", 13, "var(--ink)", cls="d") + label(190, 278, "⟦안 읽힌 두루마리는 그냥 종이예요|an unread scroll is just paper⟧", 11, "var(--muted)")
         + person(420, 90, s=0.75, face=FROWN, **CLERK) + paper(510, 120, 1.0, text="⟦예외 신청|exception⟧", stamp="#7B3FA0")
         + bubble(400, 30, 200, 34, "⟦이번만 열어 둬도 돼요?|can it stay open just today?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(620, 90, s=0.8, face=EYES, **KING) + royal_seal(700, 150, 0.7)
         + label(570, 255, "⟦예외는 왕의 도장으로만|exceptions only by the king\'s seal⟧", 13, "var(--ink)", cls="d") + label(570, 278, "⟦'이번만'도 종이에 남아요|even \'just today\' goes on paper⟧", 11, "var(--muted)")
         + label(380, 308, "⟦두루마리는 벽에 걸어두는 게 아니라 손에 들고 다니는 거예요|the scroll is for carrying, not for hanging on a wall⟧", 10, "var(--muted)"))

# 5. 이제 누가 와도 같은 답 — 검사관도, 새 사람도
P5 = svg(300, sky(300)
         + scroll(40, 40, 200, 150, "⟦성의 규칙|THE RULES⟧", (), 10) + '<path d="M60 90 h160 M60 108 h120 M60 126 h150 M60 144 h100" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>'
         + person(270, 100, s=0.8, **INSPECTOR) + bubble(300, 30, 260, 34, "⟦규칙이 있네요 — 지키는지 볼게요|there are rules — let\'s see them kept⟧", 10, "var(--panel)", "var(--line)", "left")
         + door(560, 90, lock=True) + person(612, 100, s=0.6, face=SMILE, **NEW) + calendar(700, 130, 0.9, "⟦1년|1 yr⟧")
         + label(600, 220, "⟦새 사람도 같은 답|the new one gives the same answer⟧", 11, "var(--ink)") + label(700, 180, "⟦매년 다시 읽어요|reread every year⟧", 10, "var(--muted)")
         + label(380, 275, "⟦규칙이 있으니 지킬 수 있고, 지켰는지 잴 수도 있어요|with rules written down, you can keep them — and measure that you did⟧", 12, "var(--ink)", cls="d"))

WHAT_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="8" width="44" height="8" rx="4" fill="#C9A86A"/><rect x="10" y="48" width="44" height="8" rx="4" fill="#C9A86A"/><circle cx="24" cy="30" r="4" fill="var(--accent)"/><path d="M32 30 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
HOW_I = icon(f'<rect x="10" y="14" width="22" height="38" rx="2" fill="{WOOD}"/><rect x="17" y="30" width="8" height="8" rx="1" fill="#E9B44C"/><path d="M40 20 h14 M40 32 h14 M40 44 h14" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/><circle cx="36" cy="20" r="2.5" fill="#5B8DEF"/><circle cx="36" cy="32" r="2.5" fill="#5B8DEF"/><circle cx="36" cy="44" r="2.5" fill="#5B8DEF"/>')
SEAL_I = icon('<circle cx="32" cy="32" r="20" fill="#7B3FA0" stroke="#E9B44C" stroke-width="3"/><path d="M22 38 l-2 -14 l7 6 l5 -9 l5 9 l7 -6 l-2 14z" fill="#E9B44C"/>')
READ_I = icon('<circle cx="16" cy="40" r="7" fill="#E8C9A8"/><circle cx="32" cy="36" r="7" fill="#E8C9A8"/><circle cx="48" cy="40" r="7" fill="#E8C9A8"/><rect x="8" y="48" width="16" height="10" rx="4" fill="#4A5A72"/><rect x="24" y="44" width="16" height="14" rx="4" fill="var(--good)"/><rect x="40" y="48" width="16" height="10" rx="4" fill="#5B8DEF"/><rect x="20" y="8" width="24" height="18" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>')

PAGE = {
    "slug": "policy", "order": 75,
    "title": ("성의 규칙 두루마리", "The Castle Rule Scroll"),
    "h1": ("<em>보안 정책</em>이 뭐예요?", "What is a <em>Security Policy</em>?"),
    "sub": ("보안 정책(Security Policy)을 사람마다 제각각이던 성에 왕이 규칙 두루마리를 써서 걸어두는 이야기로 풀어봤어요.",
            "Security policy, told as a story about a castle where everyone did it their own way — until the king wrote a rule scroll."),
    "panels": [
        {"svg": P1, "alt": ("네 장면: 경비 하나는 문을 잠그고, 다른 하나는 문을 열어 두고, 서기는 종이를 책상에 두고 가고, 다른 서기는 모자 없는 사람에게 열쇠를 건넴", "Four scenes: one guard locks his door, another leaves his open, a clerk leaves papers on the desk, another clerk hands a key to a stranger without a hat"),
         "caption": ("성 사람마다 다르게 해요. 누구는 잠그고, 누구는 안 잠가요.", "Everyone in the castle does it differently. Some lock up, some don\'t."),
         "small": ("종이를 책상에 두고 가는 사람도, 열쇠를 빌려주는 사람도 있어요. 다들 '그건 그 사람 방식'이래요.", "Some leave papers on the desk; some lend out keys. Everyone says that\'s just how he does it.")},
        {"svg": P2, "alt": ("왼쪽: 열린 문 하나로 도둑이 들어옴. 오른쪽: 새로 온 사람이 땀을 흘리는데 한 경비는 '잠가!', 다른 경비는 '열어 둬!'", "Left: a thief walks in through the one open door. Right: a sweating newcomer between two guards — one says lock it, the other says leave it"),
         "caption": ("도둑은 제일 헐렁한 문으로 와요. 새 사람은 누굴 따라야 할지 몰라요.", "Thieves pick the loosest door. The new one doesn\'t know whom to follow."),
         "small": ('잘 잠근 아홉 문은 소용없어요. 정한 게 없으면 성 전체가 제일 헐렁한 사람만큼만 안전해요. <a href="awareness-ko.html">도둑 수업</a>도 가르칠 규칙이 있어야 해요.',
                   'Nine locked doors don\'t help. With nothing decided, the castle is only as safe as its loosest person. Even the <a href="awareness-en.html">thief class</a> needs rules to teach.')},
        {"svg": P3, "hero": True, "alt": ("큰 두루마리 '성의 규칙': 무엇을(정책) — 문은 늘 잠근다. 어떻게(표준·절차) — 쇠 자물쇠, 나갈 때마다, 열쇠는 경비실에. 예외 — 왕의 도장. 옆에 왕과 보라색 왕의 도장", "A big scroll, THE CASTLE RULES: WHAT (policy) — every door stays locked. HOW (standard and procedure) — iron lock, every time you leave, key to the guard room. EXCEPTION — the king\'s seal. Beside it, the king and his purple seal"),
         "caption": ("보안 정책은 왕이 쓴 규칙 두루마리예요. 무엇을, 어떻게, 예외는 도장으로.", "A security policy is the rule scroll the king wrote — what, how, and exceptions only by seal."),
         "small": ("'무엇을'이 정책이에요 — 문은 늘 잠근다. '어떻게'는 표준과 절차예요 — 쇠 자물쇠로, 나갈 때마다. 예외는 왕의 도장이 있을 때만이에요.", "The what is the policy — every door stays locked. The how is the standard and procedure — an iron lock, every time you leave. Exceptions only with the king\'s seal."),
         "tricks": (4, [
             (WHAT_I, ("무엇을 — 정책", "What — policy"), ("문은 늘 잠근다", "doors stay locked"), "warm"),
             (HOW_I, ("어떻게 — 표준·절차", "How — standard, procedure"), ("쇠 자물쇠, 나갈 때마다", "iron lock, every time")),
             (SEAL_I, ("예외는 도장으로", "Exceptions by seal"), ("'이번만'도 종이에", "even just today, on paper")),
             (READ_I, ("읽히고 연습돼야", "Read and practiced"), ("안 그러면 종이예요", "or it\'s just paper"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 벽에 걸린 두루마리를 경비가 가리키고 다섯 사람이 듣고 있음. 오른쪽: 서기가 '이번만 열어 둬도 돼요?' 하고 예외 신청 종이를 내밀고 왕이 도장을 듦", "Left: a guard points at the scroll on the wall while five people listen. Right: a clerk asks can it stay open just today, holding an exception paper, and the king lifts his seal"),
         "caption": ("두루마리는 읽히고 연습돼야 해요. 예외는 왕의 도장으로만이에요.", "The scroll has to be read and practiced. Exceptions only by the king\'s seal."),
         "small": ('안 읽힌 두루마리는 그냥 종이예요. 그래서 <a href="awareness-ko.html">도둑 수업</a>에서 같이 읽어요. "이번만"도 종이에 남겨요 — 나중에 왜 열려 있었는지 알 수 있게요.',
                   'An unread scroll is just paper — so it gets read together in the <a href="awareness-en.html">thief class</a>. Even "just today" goes on paper, so later everyone knows why the door was open.')},
        {"svg": P5, "alt": ("두루마리 옆에서 검사관이 '규칙이 있네요 — 지키는지 볼게요'. 새로 온 사람이 문을 잠그고, 1년 달력에 '매년 다시 읽어요'", "Beside the scroll, an inspector says there are rules — let\'s see them kept. The newcomer locks the door; a one-year calendar reads reread every year"),
         "caption": ("이제 누가 와도 같은 답이에요. 검사관도, 새 사람도요.", "Now whoever comes gets the same answer — the inspector, and the new one."),
         "small": ('규칙이 있으니 지킬 수 있고, 지켰는지 잴 수도 있어요. <a href="compliance-ko.html">검사관</a>은 두루마리부터 봐요. 열쇠를 누가 갖는지는 <a href="rbac-ko.html">열쇠 꾸러미</a>가 정해요.',
                   'With rules written down, you can keep them — and measure that you did. The <a href="compliance-en.html">inspector</a> reads the scroll first. Who holds which key is the <a href="rbac-en.html">key ring</a>\'s job.')},
    ],
    "summary": (("<b>보안 정책</b> = 왕이 써서 도장 찍은 <b>규칙 두루마리</b>. <b>무엇을</b>(정책) → <b>어떻게</b>(표준·절차) → <b>예외는 도장으로</b>. 읽히고 연습돼야 종이가 아니에요.",
                 "<b>Security policy</b> = the <b>rule scroll</b> the king wrote and sealed. <b>What</b> (policy) → <b>how</b> (standard, procedure) → <b>exceptions by seal</b>. Read and practiced, or it\'s just paper."),
                ("Security Policy. 경영진이 승인한 '무엇을 지킬지'의 문서예요. 그 아래 표준(구체적 기준)과 절차(순서)가 따르고, 예외는 승인 기록을 남겨요. 정기적으로 검토하고, 교육으로 전파해야 실제로 작동해요.",
                 "A leadership-approved document stating what must be protected and how. Standards (specific requirements) and procedures (step-by-step) sit beneath it; exceptions are approved and recorded. It only works when reviewed regularly and taught.")),
    "glossary": [
        ("정책", "Policy", ("무엇을.", "The what."), ("'문은 늘 잠근다.' 왕이 쓰고 도장 찍은 한 줄. 잘 안 바뀌어요.", "Every door stays locked. One line the king wrote and sealed. Rarely changes.")),
        ("표준 / 절차 / 가이드라인", "Standard / Procedure / Guideline", ("어떻게.", "The how."), ("표준은 '쇠 자물쇠로', 절차는 '나갈 때 1) 닫고 2) 잠그고 3) 열쇠는 경비실에', 가이드라인은 '이렇게 하면 좋아요'.", "Standard: an iron lock. Procedure: when you leave, 1) close 2) lock 3) key to the guard room. Guideline: here\'s a good way.")),
        ("허용 사용 정책", "Acceptable Use Policy (AUP)", ("성 안에서 해도 되는 것.", "What you may do in the castle."), ("성의 도구를 뭐에 써도 되고 뭐에 쓰면 안 되는지. 새 사람이 제일 먼저 읽는 두루마리예요.", "What the castle\'s tools may and may not be used for. The first scroll a newcomer reads.")),
        ("예외 승인", "Exception approval", ("왕의 도장.", "The king\'s seal."), ("'이번만'은 종이에 적고 도장을 받아요. 언제까지인지도요.", "Just today gets written down and sealed — with an end date.")),
        ("정책 검토 주기", "Policy review cycle", ("매년 다시 읽기.", "Rereading every year."), ("성이 바뀌면 두루마리도 바뀌어야 해요. 보통 1년마다 다시 봐요.", "When the castle changes, the scroll must too. Usually once a year.")),
        ("인식 교육", "Security awareness training", ("두루마리 읽는 수업.", "The class that reads the scroll."), ('안 읽힌 두루마리는 종이예요. → <a href="awareness-ko.html">성 사람 모두가 듣는 도둑 수업</a>', 'An unread scroll is paper. → <a href="awareness-en.html">the thief class for everyone</a>')),
        ("규정 준수", "Compliance", ("검사관이 두루마리를 봐요.", "The inspector reads the scroll."), ('이웃 나라 규칙과 우리 두루마리가 맞는지. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'Whether our scroll matches the neighbors\' rules. → <a href="compliance-en.html">the inspector from next door</a>')),
        ("최소 권한", "Least privilege", ("필요한 열쇠만.", "Only the keys you need."), ('두루마리의 단골 규칙 — 열쇠는 일에 필요한 만큼만. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'A staple rule on every scroll — keys only as far as the job needs. → <a href="rbac-en.html">a key ring for every hat</a>')),
    ],
}
