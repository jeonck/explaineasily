from _draw import *

MERCHANT = dict(hat=None, shirt="#B5651D")
INSPECTOR = dict(hat="var(--stone-dark)", shirt="#4A5A72", face=EYES)
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def ledgerbook(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-32" width="52" height="64" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            + '<path d="M-16 -16 h32 M-16 -4 h32 M-16 8 h20" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/></g>')


def passstamp(x, y, s=1.0, ok=True):
    color = "var(--good)" if ok else "var(--bad)"
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="{color}" stroke-width="4"/>'
            + ('<path d="M-9 0 l6 7 l13 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ok else '<path d="M-9 -9 l18 18 M9 -9 l-18 18" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>') + "</g>")


# 1. 이웃 나라마다 다른 문단속
P1 = svg(320, sky(320)
         + person(140, 160, s=0.8, **MERCHANT) + ledgerbook(140, 90) + label(140, 275, "⟦손님 장부를 이웃 성에 팔고 싶어요|wants to carry the guest ledger to a neighboring castle⟧", 11, "var(--muted)")
         + small_castle(360, 90, 0.5) + label(440, 230, "⟦이웃 성 A|neighbor castle A⟧", 11, "var(--muted)")
         + small_castle(540, 90, 0.5) + label(620, 230, "⟦이웃 성 B|neighbor castle B⟧", 11, "var(--muted)")
         + label(380, 40, "⟦나라마다 국경 규칙이 다 달라요|every kingdom's border rule is different⟧", 13, "var(--ink)", cls="d"))

# 2. 국경마다 처음부터 다시 검사
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(170, 140, s=0.75, face=SWEAT + EYES, **MERCHANT) + ledgerbook(170, 70)
         + person(300, 160, s=0.7, **INSPECTOR) + passstamp(300, 90, 0.8, ok=False) + label(300, 270, "⟦국경 A: 서류 다시 내요|border A: file the papers again⟧", 10, "var(--muted)")
         + person(540, 160, s=0.7, **INSPECTOR) + passstamp(540, 90, 0.8, ok=False) + label(540, 270, "⟦국경 B: 또 처음부터|border B: starting over again⟧", 10, "var(--muted)")
         + label(380, 302, "⟦국경마다 처음부터 다시 검사받아야 했어요|every border means starting the inspection from scratch⟧", 12, "var(--ink)", cls="d"))

# 3. CBPR = 여러 나라가 미리 인정한 통행증 (hero)
P3 = svg(340, sky(340)
         + person(130, 130, s=0.8, **INSPECTOR) + label(130, 220, "⟦독립 검사관이 한 번만 봐요|an independent inspector checks just once⟧", 11, "var(--muted)")
         + person(280, 160, s=0.75, **MERCHANT) + ledgerbook(280, 90) + passstamp(340, 70, 0.9)
         + small_castle(460, 100, 0.5) + small_castle(590, 100, 0.5) + small_castle(680, 150, 0.35)
         + '<path d="M360 60 C420 20 520 20 560 60 M360 60 C460 10 620 10 690 70" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + label(600, 230, "⟦미리 동의한 나라들 모두에서 통해요|accepted in advance by every member kingdom⟧", 11, "var(--good)")
         + label(380, 320, "⟦CBPR = 여러 나라가 미리 인정하기로 한 통행 증명|CBPR = a pass several kingdoms agreed in advance to honor⟧", 13, "var(--ink)", cls="d"))

CHECK1_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 7 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
MAP_I = icon('<path d="M10 16 L26 10 L40 16 L54 10 V48 L40 54 L26 48 L10 54 Z" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><path d="M26 10 V48 M40 16 V54" stroke="var(--good)" stroke-width="2"/>')
OWNER_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="28" r="7" fill="#C9A86A"/><path d="M20 46 q12 -12 24 0" stroke="#C9A86A" stroke-width="3" fill="none"/>')
PENALTY_I = icon('<path d="M18 14 h28 v8 l-14 30 l-14 -30z" fill="var(--bad)"/><rect x="24" y="48" width="16" height="6" fill="#5A3B22"/>')

PAGE = {
    "slug": "cbpr", "order": 15,
    "title": ("여러 나라가 같이 인정하는 통행 증명", "The Pass Several Kingdoms Agreed to Honor"),
    "h1": ("<em>CBPR</em>이 뭐예요?", "What is <em>CBPR</em>?"),
    "sub": ("CBPR(국경 간 프라이버시 규칙)을, 여러 이웃 나라가 미리 인정하기로 한 통행 증명 이야기로 풀어봤어요.",
            "CBPR (Cross-Border Privacy Rules), told as a story about a pass several neighboring kingdoms agreed in advance to honor."),
    "panels": [
        {"svg": P1, "alt": ("상인이 손님 장부를 이웃 성 A와 B로 팔러 가고 싶어하지만, 나라마다 국경 규칙이 다름", "A merchant wants to carry a guest ledger to neighbor castles A and B, but every kingdom's border rule is different"),
         "caption": ("이웃 나라마다 국경 규칙이 다 달라요.", "Every neighboring kingdom has a different border rule."),
         "small": ("손님 장부(개인정보)를 들고 다른 나라에 가려는데, 나라마다 규칙이 제각각이에요.", "A merchant wants to carry a guest ledger (personal data) abroad — but every kingdom's rule is its own.")},
        {"svg": P2, "alt": ("상인이 국경 A와 B에서 각각 서류를 처음부터 다시 내야 함", "At border A and border B, the merchant has to file the papers from scratch each time"),
         "caption": ("국경마다 처음부터 다시 검사받아야 했어요.", "Each border meant starting the inspection all over again."),
         "small": ("국경 A를 통과해도, 국경 B에선 또 처음부터예요. 느리고 들쭉날쭉해요.", "Clear border A, and border B still starts from zero. Slow, and inconsistent.")},
        {"svg": P3, "hero": True, "alt": ("독립 검사관이 한 번만 검사해 통행증을 주고, 그 통행증이 여러 이웃 성 모두에서 통함", "An independent inspector checks once and issues a pass, and that pass works at every neighboring castle"),
         "caption": ("CBPR은 여러 나라가 미리 인정한 통행 증명이에요.", "CBPR is a pass several kingdoms agreed in advance to honor."),
         "small": ('독립 검사관(책임 대리인)이 한 번 검사하고 나면, 미리 동의한 나라들 전부에서 다시 안 물어봐요. → <a href="compliance-ko.html">규정 준수</a>의 국제판이에요.',
                   'An independent inspector (an accountability agent) checks once, and every pre-agreed kingdom accepts it — no re-asking. → the cross-border version of <a href="compliance-en.html">compliance</a>.'),
         "tricks": (4, [
             (CHECK1_I, ("한 번만 검사해요", "Inspected just once"), ("독립 검사관이 확인해요", "by an independent inspector"), "calm"),
             (MAP_I, ("여러 나라에서 통해요", "Works across many kingdoms"), ("미리 동의한 곳들 전부에서요", "wherever the members pre-agreed")),
             (OWNER_I, ("손님 것은 여전히 손님 것", "The guest's data is still the guest's"), ("동의·목적은 그대로 지켜요", "consent and purpose still apply"), "warm"),
             (PENALTY_I, ("어기면 벌칙도 있어요", "Breaking it still has a penalty"), ("통행증이 취소될 수 있어요", "the pass can be revoked")),
         ])},
        {"svg": svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
                    + label(190, 30, "⟦CBPR 없이|without CBPR⟧", 13, "var(--ink)", cls="d")
                    + label(190, 80, "⟦국경마다 따로 서류|separate papers per border⟧", 11, "var(--ink)") + label(190, 110, "⟦나라마다 기준이 달라요|standards differ by kingdom⟧", 11, "var(--ink)")
                    + label(190, 140, "⟦느리고 비용이 커요|slow, and costly⟧", 11, "var(--bad)")
                    + label(570, 30, "⟦CBPR 인증 후|with CBPR⟧", 13, "var(--ink)", cls="d")
                    + label(570, 80, "⟦인증 한 번|certified once⟧", 11, "var(--ink)") + label(570, 110, "⟦회원국 모두가 인정|every member recognizes it⟧", 11, "var(--ink)")
                    + label(570, 140, "⟦이동이 빨라져요|data moves faster⟧", 11, "var(--good)")
                    + passstamp(190, 220, 1.1, ok=False) + passstamp(570, 220, 1.1, ok=True)
                    + label(380, 300, "⟦같은 국경, 미리 합의했는지만 달라요|the same border — the difference is whether it was pre-agreed⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: CBPR 없이 국경마다 따로 느린 서류. 오른쪽: CBPR 인증 후 회원국 모두가 빠르게 인정", "Left: without CBPR, slow separate paperwork at every border. Right: with CBPR, every member recognizes it quickly"),
         "caption": ("있고 없고의 차이는 이래요.", "Here's the difference it makes."),
         "small": ("같은 국경이지만, 미리 합의했는지에 따라 속도가 완전히 달라져요.", "The same border crossing — but whether it was pre-agreed changes the speed completely.")},
        {"svg": svg(300, sky(300)
                    + small_castle(140, 110, 0.45) + label(140, 230, "⟦CBPR 회원국끼리만 통해요|only works among CBPR member kingdoms⟧", 11, "var(--muted)")
                    + small_castle(420, 110, 0.45) + label(420, 230, "⟦가입 안 한 나라엔 안 통해요|doesn't reach non-member kingdoms⟧", 11, "var(--muted)")
                    + person(620, 160, s=0.8, **INSPECTOR) + label(620, 250, "⟦우리 성 자체 법은 그대로 지켜야 해요|the castle's own law still applies on top⟧", 11, "var(--ink)")
                    + label(380, 280, "⟦APEC 회원국 중 가입한 나라끼리만 서로 인정해요|only recognized among the APEC members that opted in⟧", 12, "var(--ink)", cls="d")),
         "alt": ("CBPR 회원국끼리만 통행이 되고, 가입 안 한 나라엔 안 통함. 자국 법은 그대로 지켜야 함", "CBPR works only among member kingdoms; it doesn't reach non-members. Local law still applies"),
         "caption": ("아무 나라에나 다 통하진 않아요.", "It doesn't work with every kingdom."),
         "small": ('APEC 회원국 중 가입한 나라끼리만 통해요. 우리 성 자체 개인정보 법은 그대로 지켜야 해요 → <a href="data3law-ko.html">데이터 3법 개정</a>, <a href="privacy-ko.html">개인정보 보호</a>',
                   'It only works among the APEC members that opted in. The castle\'s own privacy law still applies on top → <a href="data3law-en.html">the Three Data Acts</a>, <a href="privacy-en.html">privacy</a>')},
    ],
    "summary": (("<b>CBPR</b> = 여러 이웃 나라가 <b>미리 인정하기로 한</b> 개인정보 이동 통행 증명. 독립 검사관이 <b>한 번</b> 검사하면, 가입국 <b>전부</b>에서 다시 안 물어봐요.",
                 "<b>CBPR</b> = a pass for moving personal data that several neighboring kingdoms <b>agreed in advance</b> to honor. An independent inspector checks <b>once</b>, and every member kingdom accepts it without asking again."),
                ("CBPR, Cross-Border Privacy Rules. APEC(아시아태평양경제협력체)이 만든 개인정보 국외 이전 인증 제도예요. 기업이 책임 대리인(Accountability Agent)의 심사를 받아 CBPR 인증을 취득하면, 회원국 간 개인정보 이전 시 각국이 정한 보호 기준을 충족한 것으로 인정받아요. 다만 가입국 사이에서만 유효하고, 각 나라의 국내 개인정보 법은 별도로 지켜야 해요.",
                 "CBPR, Cross-Border Privacy Rules — a cross-border data transfer certification created by APEC. A company that passes review by an Accountability Agent earns CBPR certification, which is then recognized as meeting each member country's protection standard when personal data moves between them. It is valid only among member economies, and each country's own domestic privacy law still applies on top.")),
    "glossary": [
        ("CBPR", "Cross-Border Privacy Rules", ("여러 나라가 미리 인정한 통행 증명.", "A pass several kingdoms pre-agreed to honor."), ("APEC 회원국 간 개인정보 이전을 위한 인증 제도예요.", "A certification for moving personal data among APEC member economies.")),
        ("APEC", "APEC", ("CBPR을 만든 나라들의 모임.", "The group of kingdoms that created CBPR."), ("아시아태평양경제협력체. CBPR 제도의 틀을 만들었어요.", "Asia-Pacific Economic Cooperation — it built the CBPR framework.")),
        ("책임 대리인", "Accountability Agent", ("검사하는 독립 검사관.", "The independent inspector who checks."), ("기업의 CBPR 적합성을 실제로 심사하는 제3의 기관이에요.", "The third-party body that actually reviews a company's CBPR compliance.")),
        ("국외 이전", "Cross-border transfer", ("손님 장부를 다른 나라로 들고 가는 것.", "Carrying the guest ledger to another kingdom."), ('개인정보 보호의 핵심 쟁점 중 하나예요. → <a href="privacy-ko.html">손님 이름표는 손님 것</a>', 'One of the central issues in privacy protection. → <a href="privacy-en.html">the visitor\'s name tag belongs to the visitor</a>')),
        ("개인정보보호위원회", "Personal Information Protection Commission", ("우리 성 자체 감독 기관.", "Our own castle's supervising office."), ('CBPR과 별개로 국내 법 감독은 이곳이 해요. → <a href="data3law-ko.html">데이터 3법 개정</a>', 'Domestic law oversight is separate from CBPR, and sits here. → <a href="data3law-en.html">the Three Data Acts amendment</a>')),
        ("GDPR", "GDPR", ("유럽 나라들의 비슷한 규칙.", "A similar rulebook among European kingdoms."), ("CBPR과 목적은 비슷하지만 회원 구성과 기준이 달라요.", "Similar in purpose to CBPR, but with different members and standards.")),
        ("국내법 우선", "Local law still applies", ("우리 성 법은 따로 지켜야 해요.", "The castle's own law still applies on top."), ("CBPR 인증이 국내 개인정보 법을 대신하진 않아요.", "CBPR certification doesn't replace the domestic privacy law.")),
        ("마이데이터", "MyData", ("손님이 직접 자기 장부를 옮기는 권리.", "The guest's own right to move their ledger."), ('CBPR은 기업 간 이전, 마이데이터는 손님 본인의 이전 요청이에요. → <a href="mydataSec-ko.html">마이데이터</a>', 'CBPR covers transfers between companies; MyData is the guest\'s own request to move it. → <a href="mydataSec-en.html">MyData</a>')),
    ],
}
