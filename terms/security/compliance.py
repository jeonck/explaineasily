from _draw import *

BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
INSPECTOR = dict(hat="var(--stone-dark)", shirt="#2E3D57", face=EYES, extra='<rect x="50" y="66" width="30" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M56 78 h18 M56 86 h18 M56 94 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>')
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'


def paper(x, y, s=1.0, stamp=None, rot=0, text=None):
    st = f'<circle cx="18" cy="-14" r="9" fill="{stamp}"/>' if stamp else ""
    tx = label(0, 24, text, 9, "#142033") if text else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -8 h28 M-18 1 h18 M-18 10 h28" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{st}{tx}</g>')


def stack(x, y, n, s=1.0):
    return "".join(paper(x + (i % 3) * 6, y - i * 7, s, rot=(i * 7) % 10 - 5) for i in range(n))


def scroll(x, y, w, h, title, rows, size=12):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect x="-8" y="-10" width="{w + 16}" height="20" rx="10" fill="#C9A86A"/><rect x="-8" y="{h - 10}" width="{w + 16}" height="20" rx="10" fill="#C9A86A"/>'
           + label(w / 2, 34, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 62 + i * 26, r, size, "#142033", "start")
    return out + "</g>"


def seal(x, y, s=1.0, text="⟦통과|PASSED⟧", color="var(--good)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="40" fill="{color}"/><circle r="32" fill="none" stroke="#FFF" stroke-width="3" stroke-dasharray="6 4"/>'
            f'{label(0, 5, text, 13, "#FFF", cls="d")}</g>')


def coinbag(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q-34 4 -34 40 q0 30 34 30 q34 0 34 -30 q0 -36 -34 -40z" fill="#E9B44C" stroke="#C9822B" stroke-width="3"/>'
            f'<path d="M-12 -30 h24 l4 -10 h-32z" fill="#C9822B"/>{label(0, 14, "⟦벌금|FINE⟧", 12, "#142033", cls="d")}</g>')


# 1. 마을 나라들이 규칙을 정했어요 — 성마다 지켜야 해요
P1 = svg(300, sky(300)
         + small_castle(30, 60, 0.5) + small_castle(120, 90, 0.45) + small_castle(60, 160, 0.4)
         + label(110, 260, "⟦이웃 나라들|the neighboring kingdoms⟧", 11, "var(--muted)")
         + scroll(240, 40, 260, 180, "⟦마을 규칙|THE RULES⟧", ("⟦손님 명부는 봉인해서 둘 것|guest lists must be sealed⟧", "⟦장부는 7년 보관할 것|ledgers kept for 7 years⟧", "⟦문마다 세 번 확인할 것|three checks at every door⟧", "⟦도둑 수업을 들을 것|everyone takes the thief class⟧"), 11)
         + castle(520, 90, 0.5) + label(635, 215, "⟦우리 성|our castle⟧", 11, "var(--muted)")
         + label(380, 275, "⟦우리가 정한 규칙이 아니에요 — 마을 나라들이 정했어요|not our rules — the kingdoms around us wrote them⟧", 12, "var(--ink)", cls="d"))

# 2. 검사관이 와요 — 말로는 안 돼요
P2 = svg(300, sky(300)
         + gate(120, 60) + person(200, 100, s=0.85, **INSPECTOR) + label(230, 225, "⟦검사관|the inspector⟧", 11, "var(--muted)")
         + bubble(280, 30, 300, 34, "⟦명부를 봉인했다는 증거, 있어요?|any proof the lists were sealed?⟧", 11, "var(--panel)", "var(--line)", "left")
         + stack(480, 200, 6, 0.6) + label(490, 245, "⟦증거 종이|proof papers⟧", 10, "var(--muted)")
         + person(600, 110, s=0.8, face=FROWN + SWEAT, **CLERK) + label(630, 225, "⟦'했어요… 아마요'|\'we did… I think\'⟧", 11, "var(--bad)")
         + label(380, 280, "⟦검사관은 믿지 않아요 — 봐요|the inspector doesn\'t trust — he looks⟧", 13, "var(--ink)", cls="d"))

# 3. 규정 준수 = 규칙마다 증거 종이를 짝 맞춰 놓기 (hero)
CHECK = (("⟦명부 봉인|lists sealed⟧", "⟦봉인 편지 사본|copy of the sealed letter⟧"),
         ("⟦7년 보관|kept 7 years⟧", "⟦보관 기간표|the how-long table⟧"),
         ("⟦세 번 확인|three checks⟧", "⟦문지기 일지|the gatekeeper\'s log⟧"),
         ("⟦도둑 수업|thief class⟧", "⟦출석부|the attendance sheet⟧"))
P3 = svg(360, sky(360)
         + '<rect x="40" y="40" width="420" height="220" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="40" width="420" height="30" rx="8" fill="#C9A86A"/>'
         + label(250, 60, "⟦검사표|THE CHECKLIST⟧", 13, "#142033", cls="d")
         + label(120, 92, "⟦규칙|rule⟧", 11, "#142033", cls="d") + label(320, 92, "⟦증거|proof⟧", 11, "#142033", cls="d")
         + "".join(label(60, 124 + i * 36, r, 12, "#142033", "start") + label(215, 120 + i * 36, "→", 14, "#C9822B")
                   + label(240, 124 + i * 36, p, 12, "#142033", "start")
                   + f'<circle cx="430" cy="{120 + i * 36}" r="10" fill="var(--good)"/><path d="M425 {120 + i * 36} l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>'
                   for i, (r, p) in enumerate(CHECK))
         + person(500, 90, s=0.85, **INSPECTOR) + seal(650, 130, 1.0) + label(650, 195, "⟦도장 = 인증서|the stamp = a certificate⟧", 11, "var(--muted)")
         + person(480, 200, s=0.65, face=SMILE, **CLERK)
         + label(380, 300, "⟦규칙마다 증거 종이를 짝 맞춰요|for every rule, a matching paper of proof⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦통과하면 도장, 못하면 벌금|pass and you get the stamp; fail and you pay⟧", 12, "var(--muted)"))

# 4. 통과 / 못 지킴
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + gate(120, 70) + seal(120, 122, 0.55) + label(120, 215, "⟦성문에 붙인 도장|the stamp on the gate⟧", 11, "var(--ink)")
         + person(240, 100, s=0.8, face=SMILE, **KING)
         + label(190, 255, "⟦통과|passed⟧", 14, "var(--ink)", cls="d") + label(190, 277, "⟦손님들이 믿고 와요|guests come, trusting⟧", 11, "var(--good)")
         + person(450, 100, s=0.8, face=FROWN + SWEAT, **KING) + coinbag(580, 130, 0.9)
         + '<path d="M625 130 h40" stroke="var(--bad)" stroke-width="3"/><path d="M665 130 l-8 -6 v12z" fill="var(--bad)"/>' + small_castle(680, 90, 0.4)
         + label(570, 255, "⟦못 지킴|failed⟧", 14, "var(--ink)", cls="d") + label(570, 277, "⟦벌금 — 그리고 소문|a fine — and the gossip⟧", 11, "var(--bad)")
         + label(380, 305, "⟦이웃 나라가 정한 규칙이니, 이웃 나라가 벌해요|the neighbors wrote the rules, so the neighbors punish⟧", 11, "var(--muted)"))

# 5. 도장을 받아도 도둑은 와요 — 규칙은 최소선이에요
P5 = svg(300, sky(300)
         + castle(40, 80, 0.7) + seal(200, 152, 0.5) + person(330, 60, s=0.7, face=MASK, extra=BAG)
         + person(470, 110, s=0.8, face=FROWN + SWEAT, **BLUE)
         + bubble(430, 30, 300, 34, "⟦도장 받았는데 왜 도둑이?|we got the stamp — why a thief?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(600, 220, "⟦규칙은 최소선이에요|the rules are the floor⟧", 13, "var(--ink)", cls="d") + label(600, 245, "⟦도둑은 규칙을 안 읽어요|thieves don\'t read the rules⟧", 11, "var(--bad)")
         + label(380, 280, "⟦도장은 '지켰다'는 뜻이지 '안전하다'는 뜻이 아니에요|the stamp says we complied — not that we\'re safe⟧", 12, "var(--ink)", cls="d"))

RULE_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="10" y="8" width="44" height="8" rx="4" fill="#C9A86A"/><rect x="10" y="48" width="44" height="8" rx="4" fill="#C9A86A"/><path d="M22 26 h20 M22 34 h20 M22 42 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
PROOF_I = icon('<rect x="12" y="10" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h14 M20 30 h14 M20 38 h8" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/><circle cx="46" cy="44" r="11" fill="var(--good)"/><path d="M40 44 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')
STAMP_I = icon('<circle cx="32" cy="32" r="22" fill="var(--good)"/><circle cx="32" cy="32" r="16" fill="none" stroke="#FFF" stroke-width="2.5" stroke-dasharray="4 3"/><path d="M24 32 l6 6 l10 -12" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round"/>')
FLOOR_I = icon('<rect x="8" y="46" width="48" height="8" rx="2" fill="var(--stone-dark)"/><path d="M32 42 V16" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M22 26 l10 -12 l10 12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "compliance", "order": 74,
    "title": ("이웃 나라 규칙 검사관", "The Inspector from the Neighboring Kingdom"),
    "h1": ("<em>규정 준수</em>가 뭐예요?", "What is <em>Compliance</em>?"),
    "sub": ("규정 준수(Compliance)와 감사(Audit)를 이웃 나라들이 정한 규칙을 검사관이 와서 증거로 확인하는 이야기로 풀어봤어요.",
            "Compliance and audit, told as a story about rules written by the neighboring kingdoms and an inspector who comes to see the proof."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽에 이웃 나라의 작은 성 세 개, 가운데 '마을 규칙' 두루마리(명부 봉인, 7년 보관, 세 번 확인, 도둑 수업), 오른쪽에 우리 성", "Three small castles of the neighboring kingdoms on the left, a scroll of rules in the middle — lists sealed, kept 7 years, three checks, thief class — and our castle on the right"),
         "caption": ("마을 나라들이 규칙을 정했어요. 성마다 지켜야 해요.", "The kingdoms around us wrote the rules. Every castle has to follow them."),
         "small": ('우리가 정한 규칙이 아니에요. 손님 명부는 <a href="encryption-ko.html">봉인</a>해서 두고, 장부는 <a href="retention-ko.html">7년</a> 두고, 문마다 <a href="mfa-ko.html">세 번 확인</a>하래요.',
                   'Not our rules. Guest lists must be <a href="encryption-en.html">sealed</a>, ledgers <a href="retention-en.html">kept seven years</a>, every door <a href="mfa-en.html">checked three times</a>.')},
        {"svg": P2, "alt": ("성문 앞의 검사관이 서류판을 들고 '명부를 봉인했다는 증거, 있어요?'. 서기가 땀을 흘리며 '했어요… 아마요'. 옆에 증거 종이 더미", "An inspector with a clipboard at the gate: any proof the lists were sealed? A sweating clerk: we did… I think. A pile of proof papers beside him"),
         "caption": ("검사관이 와요. 말로는 안 돼요.", "The inspector comes. Words aren\'t enough."),
         "small": ('검사관은 믿지 않고 봐요. "했어요"가 아니라 <a href="log-ko.html">일지</a>와 종이로 보여줘야 해요.', 'The inspector doesn\'t trust — he looks. Not "we did it," but the <a href="log-en.html">log</a> and the paper that show it.')},
        {"svg": P3, "hero": True, "alt": ("검사표: 명부 봉인 → 봉인 편지 사본, 7년 보관 → 보관 기간표, 세 번 확인 → 문지기 일지, 도둑 수업 → 출석부, 모두 초록 체크. 검사관이 '통과' 도장을 찍고 서기가 웃음", "A checklist: lists sealed → copy of the sealed letter, kept 7 years → the how-long table, three checks → the gatekeeper\'s log, thief class → attendance sheet, all green-checked. The inspector stamps PASSED; the clerk smiles"),
         "caption": ("규정 준수는 규칙마다 증거 종이를 짝 맞춰 놓는 거예요.", "Compliance is putting a paper of proof next to every rule."),
         "small": ("규칙 하나에 증거 하나. 검사관이 보고 다 맞으면 도장을 찍어요. 그 도장이 인증서예요. 못 맞추면 벌금이고요.", "One rule, one proof. If the inspector finds them all, he stamps it. That stamp is the certificate. Miss one, and there\'s a fine."),
         "tricks": (4, [
             (RULE_I, ("규칙은 밖에서 와요", "Rules come from outside"), ("이웃 나라가 정해요", "the neighbors write them")),
             (PROOF_I, ("증거를 짝 맞춰요", "Match the proof"), ("말이 아니라 종이", "paper, not words"), "warm"),
             (STAMP_I, ("통과하면 도장", "Pass, get the stamp"), ("손님이 믿고 와요", "guests come trusting")),
             (FLOOR_I, ("규칙은 최소선", "Rules are the floor"), ("천장이 아니에요", "not the ceiling"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 성문에 통과 도장이 붙고 왕이 웃음. 오른쪽: 왕이 땀을 흘리고 벌금 주머니가 이웃 나라 성으로 날아감", "Left: the PASSED stamp on the gate, the king smiling. Right: the king sweating as a bag marked FINE flies off to the neighboring castle"),
         "caption": ("통과하면 성문에 도장이 붙어요. 못 지키면 벌금이에요.", "Pass, and the stamp goes on the gate. Fail, and there\'s a fine."),
         "small": ("규칙을 정한 건 이웃 나라라서, 벌도 이웃 나라가 줘요. 벌금보다 아픈 건 소문이에요 — '저 성은 규칙을 안 지킨대'.", "The neighbors wrote the rules, so the neighbors punish. Worse than the fine is the gossip — that castle doesn\'t follow the rules.")},
        {"svg": P5, "alt": ("통과 도장이 붙은 성벽 위로 도둑이 넘어옴. 파란 모자 경비가 땀 흘리며 '도장 받았는데 왜 도둑이?'", "A thief climbs over the wall of a castle bearing the PASSED stamp. A blue-hat guard sweats: we got the stamp — why a thief?"),
         "caption": ("도장을 받아도 도둑은 와요. 규칙은 최소선이에요.", "The stamp doesn\'t stop thieves. Rules are the floor, not the ceiling."),
         "small": ('도둑은 규칙을 안 읽어요. 도장은 "지켰다"는 뜻이지 "안전하다"는 뜻이 아니에요. 진짜 지키기는 <a href="risk-ko.html">저울</a>과 <a href="soc-ko.html">경비실</a>이 해요.',
                   'Thieves don\'t read the rules. The stamp says we complied — not that we\'re safe. Real protection comes from the <a href="risk-en.html">scale</a> and the <a href="soc-en.html">guard room</a>.')},
    ],
    "summary": (("<b>규정 준수</b> = 이웃 나라가 정한 규칙마다 <b>증거 종이를 짝 맞춰</b> 두고, 검사관이 보면 <b>도장</b>을 받는 것. 도장은 <b>최소선</b>이지 안전 그 자체는 아니에요.",
                 "<b>Compliance</b> = for every rule the neighbors wrote, <b>keep matching proof</b>, and when the inspector looks, <b>earn the stamp</b>. The stamp is the <b>floor</b>, not safety itself."),
                ("Compliance. 법·규제·표준(GDPR, 개인정보보호법, ISO 27001 등)이 요구하는 통제 항목을 갖추고, 감사 때 증적으로 입증하는 일이에요. 인증은 '요구사항을 충족했다'는 뜻이지 '침해가 없다'는 뜻은 아니에요.",
                 "Meeting the controls that laws, regulations, and standards (GDPR, privacy acts, ISO 27001) require, and proving it with evidence at audit time. Certification means the requirements were met — not that a breach can\'t happen.")),
    "glossary": [
        ("규정 준수", "Compliance", ("규칙마다 증거 짝 맞추기.", "Proof next to every rule."), ('이웃 나라가 정한 규칙을 지키고, 지켰다고 보여줄 수 있는 상태. 우리 성 안의 규칙은 → <a href="policy-ko.html">성의 규칙 두루마리</a>', 'Following the rules the neighbors wrote, and being able to show it. Our own castle\'s rules → <a href="policy-en.html">the rule scroll</a>')),
        ("감사", "Audit", ("검사관의 방문.", "The inspector\'s visit."), ("믿지 않고 봐요. 우리 사람이 미리 보는 것도(내부 감사), 바깥 사람이 오는 것도(외부 감사) 있어요.", "Doesn\'t trust — looks. Our own people can look first (internal audit), or someone from outside comes (external audit).")),
        ("통제 항목", "Control", ("규칙 한 줄.", "One line of the rules."), ("'문마다 세 번 확인' 같은 것. 검사표의 한 칸이에요.", "Something like three checks at every door. One row on the checklist.")),
        ("증적", "Evidence", ("증거 종이.", "The proof paper."), ('일지, 사본, 출석부. 만들 때 남겨야지 검사 전날엔 못 만들어요. → <a href="log-ko.html">한 줄 일지</a>', 'Logs, copies, attendance sheets. Made as you go — you can\'t make them the night before. → <a href="log-en.html">the one-line log</a>')),
        ("인증", "Certification (ISO 27001)", ("성문의 도장.", "The stamp on the gate."), ("바깥 검사관이 '이 성은 규칙대로 지킨다'고 찍어준 도장. 몇 년마다 다시 받아요.", "An outside inspector\'s stamp saying this castle keeps the rules. Renewed every few years.")),
        ("개인정보 규칙", "Privacy law (GDPR, 개인정보보호법)", ("손님 명부 규칙.", "The guest-list rules."), ('손님 이름과 주소를 어떻게 다뤄야 하는지 나라가 정한 것. 봉인하고, 오래 두지 말고. → <a href="classification-ko.html">색 도장</a>', 'How a kingdom says guest names and addresses must be handled. Seal them, don\'t keep them long. → <a href="classification-en.html">the colored stamp</a>')),
        ("갭 분석", "Gap analysis", ("검사관 오기 전에 스스로 보기.", "Looking before the inspector does."), ("검사표를 먼저 펴서 빈칸을 찾아요. 빈칸이 '갭'이에요.", "Open the checklist yourself and find the empty rows. Those are the gaps.")),
        ("보존", "Retention", ("7년 보관 규칙.", "The seven-year rule."), ('있어야 할 게 없으면 벌금이에요. → <a href="retention-ko.html">종이마다 정해둔 태우는 날</a>', 'If what should be there isn\'t, that\'s a fine. → <a href="retention-en.html">every paper\'s burning day</a>')),
    ],
}
