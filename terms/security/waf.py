from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")


def counter(x, y, s=1.0, clerk_face=SMILE):
    """성벽에 난 창구. 안에 직원."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-90" y="-120" width="180" height="200" fill="var(--stone-dark)"/>'
            f'{battlements(-90, -138, 180, 4, "var(--stone-dark)", 20)}'
            f'<rect x="-56" y="-80" width="112" height="90" rx="6" fill="var(--sky)"/><rect x="-62" y="10" width="124" height="12" rx="3" fill="{WOOD}"/>'
            f'{person(-30, -74, s=0.7, face=clerk_face, **CLERK)}{label(0, -96, "⟦창구|COUNTER⟧", 13, "#F5E6B8", cls="d")}</g>')


def note(x, y, lines, s=1.0, rot=0, bad_from=None, torn=False):
    rows = ""
    for i, t in enumerate(lines):
        color = "var(--bad)" if bad_from is not None and i >= bad_from else "#142033"
        rows += label(8, 24 + i * 16, t, 11, color, "start")
    tear = '<path d="M0 0 l12 10 l-10 12 l12 10 l-10 12 l12 10 l-10 12 l12 10 l-10 12" stroke="var(--bad-soft)" stroke-width="5" fill="none"/>' if torn else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="150" height="{20 + len(lines) * 16}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{rows}{tear}</g>')


def rulebook(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="70" height="52" rx="3" fill="var(--bad)"/><rect x="6" y="6" width="58" height="40" rx="2" fill="var(--panel)"/>'
            f'{label(35, 24, "⟦수상한|SHADY⟧", 9, "var(--bad)")}{label(35, 38, "⟦문장 목록|PHRASES⟧", 9, "var(--bad)")}</g>')


QUEUE = lambda y, xs, faces=None: "".join(person(x, y, s=0.7, hat=h, shirt="#4A5A72", face=(faces[i] if faces else SMILE)) for i, (x, h) in enumerate(xs))
TOWN = ((40, None), (110, "#E9B44C"), (180, "var(--stone-dark)"))

# 1. 누구나 쪽지를 넣는 창구
P1 = svg(300, sky(300) + counter(560, 150)
         + QUEUE(150, TOWN)
         + note(250, 70, ("⟦사과 두 개 주세요|Two apples please⟧",), 0.9, -4) + note(290, 150, ("⟦내 편지 있어요?|Any mail for me?⟧",), 0.9, 3)
         + '<path d="M400 190 L480 190" stroke="var(--accent)" stroke-width="3"/><path d="M470 180 L482 190 L470 200" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(380, 280, "⟦마을 사람 누구나 쪽지를 넣어요 — 웹사이트예요|anyone in town can hand in a note — that\'s a website⟧", 13, "var(--muted)"))

# 2. 쪽지에 이상한 문장을 끼워 넣는다
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>' + counter(600, 150, 0.9, clerk_face=EYES)
         + person(60, 120, s=0.85, face=MASK)
         + note(150, 60, ("⟦사과 두 개 주세요.|Two apples please.⟧", "⟦그리고 금고 열쇠도|And the vault key⟧", "⟦같이 주세요.|as well.⟧"), 1.0, -3, bad_from=1)
         + note(150, 170, ("⟦내 편지 있어요?|Any mail for me?⟧", "⟦이 쪽지를 다음|Show this note to⟧", "⟦손님에게도 보여줘요.|the next customer.⟧"), 1.0, 2, bad_from=1)
         + '<path d="M320 160 L500 160" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8"/><path d="M490 150 L502 160 L490 170" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + bubble(520, 230, 170, 34, "⟦네, 여기요…|Sure, here you go…⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(380, 300, "⟦창구 직원은 시키는 대로 해요. 도둑은 그걸 알아요|the clerk does what the note says — and thieves know it⟧", 12, "var(--muted)"))

# 3. WAF = 창구 앞 검토원 (hero)
P3 = svg(340, sky(340) + counter(640, 150, 0.9)
         + QUEUE(160, ((30, None), (95, "#E9B44C"))) + person(160, 150, s=0.7, face=MASK)
         + person(330, 120, s=0.9, face=EYES, **GUARD) + rulebook(392, 60, 0.9)
         + label(355, 260, "⟦검토원|the checker⟧", 13, "var(--ink)", cls="d")
         + note(230, 40, ("⟦사과 두 개 주세요|Two apples please⟧",), 0.8, -6) + '<path d="M360 60 l8 8 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + note(240, 220, ("⟦…그리고 금고 열쇠도|…and the vault key⟧",), 0.8, 4, bad_from=0, torn=True)
         + '<path d="M420 190 L540 190" stroke="var(--good)" stroke-width="3"/><path d="M530 180 L542 190 L530 200" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(480, 175, "⟦깨끗한 쪽지만|clean notes only⟧", 11, "var(--good)")
         + label(380, 322, "⟦수상한 문장이 있으면 찢어요. 창구 직원은 깨끗한 쪽지만 받아요|shady phrase? torn up. The clerk only ever sees clean notes⟧", 12, "var(--muted)"))

# 4. 찢거나, 표시하거나, 손 들게 하거나
HAND = '<path d="M0 30 V-4 M-12 30 V2 M12 30 V0 M-22 32 V10 M20 32 V12" stroke="#E8C9A8" stroke-width="10" stroke-linecap="round"/><rect x="-26" y="26" width="52" height="30" rx="10" fill="#E8C9A8"/>'
P4 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + note(50, 60, ("⟦…금고 열쇠도|…and the vault key⟧",), 0.9, -3, bad_from=0, torn=True) + '<path d="M60 60 l120 60 M180 60 l-120 60" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>'
         + label(120, 230, "⟦찢기|tear up⟧", 15, "var(--ink)", cls="d")
         + note(300, 60, ("⟦사과 999개 주세요|999 apples please⟧",), 0.9, 2) + '<g transform="translate(430,70)"><path d="M0 -18 L16 12 H-16 Z" fill="#E9B44C"/><rect x="-2" y="-6" width="4" height="10" fill="var(--night)"/><circle cy="8" r="2" fill="var(--night)"/></g>'
         + label(370, 230, "⟦표시만 하기|flag it⟧", 15, "var(--ink)", cls="d")
         + f'<g transform="translate(620,110)">{HAND}</g>' + bubble(540, 20, 180, 34, "⟦사람 맞아요? 손 들어봐요|Human? Raise your hand⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(620, 230, "⟦손 들게 하기|make them raise a hand⟧", 15, "var(--ink)", cls="d")
         + label(380, 275, "⟦로봇이 쪽지를 천 장씩 넣을 때 손 들어보라고 해요|when a robot drops a thousand notes, ask it to raise a hand⟧", 12, "var(--muted)"))

# 5. 새 말투는 못 알아보고, 착한 쪽지를 찢기도 한다
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + person(40, 100, s=0.8, face=MASK) + note(120, 50, ("⟦사과 둘. 그 담에|Two apples. Then,⟧", "⟦금-고 열쇠 좀…|the va-ult k3y…⟧"), 0.9, -3, bad_from=1)
         + person(250, 150, s=0.8, face=FROWN, **GUARD) + label(280, 260, "⟦목록에 없는 말투예요|not on the list⟧", 12, "var(--bad)")
         + label(190, 295, "⟦돌려 말하면 못 알아봐요|reworded, it slips through⟧", 13, "var(--muted)")
         + person(440, 100, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=FROWN) + note(510, 50, ("⟦금고동 사과 두 개|Two apples from⟧", "⟦주세요|Vault Street⟧"), 0.9, 3, torn=True)
         + person(650, 150, s=0.8, face=EYES, **GUARD) + label(560, 260, "⟦'금고'라는 말이 있어서 찢었어요|torn — it said 'vault'⟧", 12, "var(--bad)")
         + label(570, 295, "⟦착한 쪽지를 찢으면 손님이 화나요|tear a good note and the customer is angry⟧", 13, "var(--muted)"))

LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="var(--bad)"/><rect x="22" y="30" width="16" height="3" fill="var(--bad)"/><rect x="22" y="40" width="18" height="3" fill="var(--bad)"/>')
COUNT_I = icon('<rect x="10" y="14" width="24" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="18" y="20" width="24" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="26" y="26" width="24" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><text x="52" y="20" font-size="12" font-weight="700" fill="var(--accent)">×999</text>')
FACE_I = icon(f'<circle cx="32" cy="26" r="14" fill="{SKIN}"/><path d="M20 22 h24 v8 h-24z" fill="#111C30"/><rect x="18" y="42" width="28" height="16" rx="6" fill="#2E3D57"/>')
WALL_I = icon('<rect x="8" y="24" width="48" height="30" fill="var(--stone-dark)"/><rect x="8" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="24" y="34" width="16" height="20" fill="var(--sky)"/>')

PAGE = {
    "slug": "waf", "order": 27,
    "title": ("창구 앞 쪽지 검토원", "The Note Checker at the Counter"),
    "h1": ("<em>WAF</em>가 뭐예요?", "What is a <em>WAF</em>?"),
    "sub": ("웹 애플리케이션 방화벽(Web Application Firewall)을 창구 앞에서 쪽지를 먼저 읽는 검토원 이야기로 풀어봤어요.",
            "Web Application Firewall, told as a story about the checker who reads every note before it reaches the counter."),
    "panels": [
        {"svg": P1, "alt": ("성벽에 난 창구 안에 직원이 있고, 마을 사람들이 '사과 두 개 주세요', '내 편지 있어요?' 쪽지를 들고 줄을 섬", "A clerk inside a counter window in the castle wall; townsfolk queue with notes reading Two apples please and Any mail for me?"),
         "caption": ("성 벽엔 누구나 쪽지를 넣는 창구가 있어요.", "The castle wall has a counter anyone can hand a note to."),
         "small": ("'사과 두 개 주세요', '내 편지 있어요?' — 웹사이트예요.", "'Two apples please', 'Any mail for me?' — that's a website.")},
        {"svg": P2, "alt": ("도둑의 쪽지: '사과 두 개 주세요. 그리고 금고 열쇠도 같이 주세요', '이 쪽지를 다음 손님에게도 보여줘요'. 직원은 '네, 여기요…'", "A thief's notes: Two apples please. And the vault key as well; Show this note to the next customer. The clerk says Sure, here you go…"),
         "caption": ("쪽지에 이상한 문장을 끼워 넣어요.", "Thieves slip strange sentences into the note."),
         "small": ("창구 직원은 시키는 대로 해요. 도둑은 그걸 알아요.", "The clerk does what the note says. Thieves know that.")},
        {"svg": P3, "hero": True, "alt": ("줄과 창구 사이에 수상한 문장 목록을 든 검토원이 서서, 사과 쪽지는 통과시키고 '금고 열쇠' 쪽지는 찢음", "Between the queue and the counter, a checker with a list of shady phrases passes the apple note and tears up the vault-key one"),
         "caption": ("WAF는 창구 앞에서 쪽지를 먼저 읽어요.", "A WAF reads every note before the counter does."),
         "small": ("수상한 문장이 있으면 찢어요. 창구 직원은 깨끗한 쪽지만 받아요.", "A shady phrase gets it torn up. The clerk only ever sees clean notes."),
         "tricks": (4, [
             (LIST_I, ("수상한 문장 목록", "The shady-phrase list"), ("도둑들이 자주 쓰는 말", "what thieves usually write")),
             (COUNT_I, ("몇 장, 얼마나 크게", "How many, how big"), ("천 장씩 넣으면 수상해요", "a thousand notes is suspicious"), "warm"),
             (FACE_I, ("낯선 얼굴", "Strange faces"), ("소문난 도둑은 줄에서 빼요", "known thieves leave the queue"), "calm"),
             (WALL_I, ("성벽과 다른 점", "Unlike the wall"), ("성벽은 문을 막고, 검토원은 문장을 읽어요", "the wall blocks doors; the checker reads words"), "calm"),
         ])},
        {"svg": P4, "alt": ("찢긴 쪽지에 X, '사과 999개' 쪽지에 노란 경고 표시, 손을 든 손 그림과 '사람 맞아요? 손 들어봐요'", "A torn note crossed out; a 999-apples note with a yellow warning; a raised hand with Human? Raise your hand"),
         "caption": ("찢거나, 표시하거나, 손 들게 해요.", "Tear it up, flag it, or make them raise a hand."),
         "small": ("'사람 맞아요? 손 들어봐요' — 로봇이 쪽지를 천 장씩 넣을 때요.", "'Human? Raise your hand' — for when a robot drops a thousand notes at once.")},
        {"svg": P5, "alt": ("왼쪽: 도둑이 '금-고 열쇠 좀…' 하고 돌려 쓴 쪽지에 검토원이 난감. 오른쪽: '금고동 사과 두 개 주세요' 착한 쪽지가 찢겨 손님이 화남", "Left: a thief's reworded note (the va-ult k3y…) stumps the checker. Right: an honest note (Two apples from Vault Street) gets torn and the customer is upset"),
         "caption": ("새 말투는 못 알아보고, 착한 쪽지를 찢기도 해요.", "New wording slips through; good notes get torn."),
         "small": ("도둑이 돌려 말하면 목록에 없어요. '금고동 사과'를 찢으면 손님이 화나요. 진짜 해법은 창구 직원이 애초에 시키는 대로 안 하는 것(안전한 코드)이에요.", "Reworded, it's not on the list. Tear up 'apples from Vault Street' and the customer is angry. The real fix is a clerk who doesn't blindly obey notes — safe code.")},
    ],
    "summary": (("<b>WAF</b> = 창구(웹사이트) 앞에서 쪽지(요청)를 <b>먼저 읽고</b>, 수상한 문장을 <b>찢는</b> 검토원.",
                 "A <b>WAF</b> = the checker who <b>reads every note</b> (request) before the counter (the website) and <b>tears up</b> the shady ones."),
                ("Web Application Firewall. 성벽(방화벽)은 문을 막고, WAF는 문장을 읽어요. OWASP Top 10이 검토원의 교과서예요. Cloudflare WAF, AWS WAF, ModSecurity 같은 것들.",
                 "Web Application Firewall. The wall (firewall) blocks doors; a WAF reads sentences. The OWASP Top 10 is the checker's textbook. Cloudflare WAF, AWS WAF, ModSecurity.")),
    "glossary": [
        ("요청", "Request", ("쪽지.", "The note."), ("마을 사람이 창구에 넣는 것. 주소창, 검색어, 입력칸 전부.", "What townsfolk hand to the counter: the address bar, search terms, every input box.")),
        ("웹 앱", "Web application", ("창구.", "The counter."), ("누구나 쪽지를 넣을 수 있어서, 도둑도 넣을 수 있어요.", "Anyone can hand in a note — which means thieves can too.")),
        ("SQL 인젝션", "SQL injection", ("…그리고 금고도 열어줘.", "…and open the vault too."), ("주문 쪽지에 창고 명령을 끼워 넣기.", "Slipping a storeroom command into an order note.")),
        ("XSS", "Cross-site scripting", ("이 쪽지를 다음 손님에게 보여줘.", "Show this note to the next customer."), ("내 쪽지가 남의 눈앞에서 움직이게 하기.", "Making my note act in front of someone else.")),
        ("규칙 · 시그니처", "Rules · signatures", ("수상한 문장 목록.", "The shady-phrase list."), ("OWASP 핵심 규칙 세트(CRS)가 제일 널리 쓰여요.", "The OWASP Core Rule Set (CRS) is the most widely used.")),
        ("봇 챌린지", "Bot challenge", ("손 들어봐요.", "Raise your hand."), ("CAPTCHA 같은 것. 로봇은 손이 없어요.", "CAPTCHAs and the like. Robots have no hands.")),
        ("오탐", "False positive", ("금고동 사과 찢기.", "Tearing up apples from Vault Street."), ('착한 쪽지를 찢은 것. → <a href="soc-ko.html">경비실의 고양이</a>', 'A good note torn up. → <a href="soc-en.html">the guard room\'s cat</a>')),
        ("방화벽", "Firewall", ("성벽.", "The wall."), ('문을 열고 닫기만 해요. 문장은 안 읽어요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Only opens and closes doors — never reads the words. → <a href="ndr-en.html">the hallway watcher</a>')),
    ],
}
