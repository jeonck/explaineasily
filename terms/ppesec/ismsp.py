from _draw import *

KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
INSPECTOR = dict(hat="var(--stone-dark)", shirt="#2E3D57", face=EYES, extra='<rect x="50" y="66" width="30" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M56 78 h18 M56 86 h18 M56 94 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>')
NEIGHBOR = dict(hat="var(--accent)", shirt="#4A5A72")


def plaque(x, y, s=1.0, text="⟦통과|PASSED⟧", color="var(--good)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-56" y="-22" width="112" height="44" rx="6" fill="{color}" stroke="#E9B44C" stroke-width="3"/>'
            + label(0, 7, text, 13, "#FFF", cls="d") + "</g>")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 성주가 "우리 성 안전해요!"라고 말만 해요
P1 = svg(355, sky(355) + castle(260, 40, 0.75)
         + person(230, 230, s=0.8, face=SMILE, **KING)
         + bubble(290, 190, 200, 40, "⟦우리 성 완전 안전해요!|our castle is totally safe!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 338, "⟦증거는 없고, 성주 혼자만의 말이에요|no proof — just the lord\'s own word⟧", 13, "var(--ink)"))

# 2. 이웃 성은 못 믿어요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + small_castle(80, 60, 0.55) + label(190, 212, "⟦우리 성|our castle⟧", 11, "var(--muted)")
         + person(430, 150, s=0.85, face=FROWN, **NEIGHBOR)
         + bubble(360, 70, 260, 46, "⟦말로만 안전하다니, 저희 손님 정보를 맡기긴 좀…|just your word for it? I can\'t hand over our guests\' data⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦증거가 없으면 이웃은 거래를 망설여요|without proof, neighbors hesitate to deal with you⟧", 13, "var(--ink)"))

# 3. ISMS-P = 나라가 보낸 검사관이 성 전체에 거는 현판 (hero)
WHOLE_I = icon('<rect x="8" y="10" width="48" height="44" rx="4" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M8 24 h48 M8 38 h48" stroke="var(--accent)" stroke-width="2"/>')
LIFECYCLE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4" stroke-dasharray="6 5"/><circle cx="32" cy="10" r="6" fill="var(--good)"/>')
YEARLY_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 18 v14 l10 6" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')
LAW_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')

P3 = svg(340, sky(340) + castle(140, 60, 0.9)
         + person(500, 150, s=0.95, **INSPECTOR)
         + plaque(400, 110, 0.9)
         + label(380, 30, "⟦ISMS-P = 나라의 검사관이 성 전체를 다 돌아보고 거는 현판|ISMS-P = a government inspector checks the whole castle, then hangs the plaque⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦문 하나가 아니라 관리체계부터 손님정보 창고까지 전부예요|not just one door — the whole management system, down to the guest-info storeroom⟧", 12, "var(--muted)"))

# 4. 검사표 네 영역
P4 = svg(300, sky(300)
         + box(60, 40, 330, 220, "⟦ISMS-P 점검표|ISMS-P CHECKLIST⟧",
               ("⟦1. 관리체계 수립·운영 — 정책·조직·위험평가|1. Management system — policy, org, risk⟧",
                "⟦2. 보호대책 요구사항 — 문단속·암호화 등|2. Protection measures — locks, encryption, etc.⟧",
                "⟦3. 개인정보 처리단계별 요구사항 — 수집부터 파기까지|3. Personal-data lifecycle — collect to destroy⟧",
                "⟦(3은 ISMS-P만 추가돼요|item 3 is added only for ISMS-P)⟧"), 11)
         + person(560, 120, s=0.85, **INSPECTOR)
         + label(560, 230, "⟦ISMS는 1·2만, ISMS-P는 3까지|ISMS covers 1–2 only; ISMS-P adds 3⟧", 12, "var(--muted)")
         + label(380, 280, "⟦개인정보 창고가 있는 성은 3번까지 봐야 해요|a castle with a guest-info storeroom needs item 3 too⟧", 12, "var(--ink)"))

# 5. 현판이 있어도 도둑은 와요
P5 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + castle(240, 40, 0.75) + plaque(390, 60, 0.8)
         + person(330, 190, s=0.6, face=MASK)
         + '<path d="M330 196 l-10 -40" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>'
         + person(230, 195, s=0.75, face=FROWN + SWEAT, **CLERK)
         + bubble(90, 125, 210, 40, "⟦현판 받았는데 왜 도둑이?|we got the plaque — why a thief?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 295, "⟦현판은 '기준을 지켰다'는 뜻이지 '안전 보장'은 아니에요|the plaque means the standard was met — not that nothing can go wrong⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "ismsp", "order": 1,
    "title": ("성 전체에 거는 인증 현판", "The Certification Plaque for the Whole Castle"),
    "h1": ("<em>ISMS/ISMS-P</em>가 뭐예요?", "What is <em>ISMS/ISMS-P</em>?"),
    "sub": ("ISMS/ISMS-P를 나라가 보낸 검사관이 성 전체를 돌아보고 거는 인증 현판 이야기로 풀어봤어요.",
            "ISMS/ISMS-P, told as a story about a government inspector who checks the whole castle and hangs a certification plaque."),
    "panels": [
        {"svg": P1, "alt": ("성주가 성 앞에서 '우리 성 완전 안전해요!'라고 말함", "The lord stands before the castle, saying our castle is totally safe!"),
         "caption": ("성주가 \"우리 성 안전해요!\"라고 말만 해요.", "The lord just says our castle is safe."),
         "small": ("증거는 없고, 성주 혼자만의 말이에요.", "No proof — just the lord's own word.")},
        {"svg": P2, "alt": ("이웃 성 사람이 얼굴을 찡그리며 '말로만 안전하다니, 저희 손님 정보를 맡기긴 좀…'", "A neighboring castle's visitor frowns: just your word for it? I can't hand over our guests' data"),
         "caption": ("이웃 성은 못 믿어요.", "The neighboring castle can't just take your word."),
         "small": ("증거가 없으면 이웃은 거래를 망설여요.", "Without proof, neighbors hesitate to deal with you.")},
        {"svg": P3, "hero": True, "alt": ("검사관이 성 전체를 보고 초록 '통과' 현판을 거는 모습", "An inspector examines the whole castle and hangs a green PASSED plaque"),
         "caption": ("ISMS-P는 나라의 검사관이 성 전체를 다 돌아보고 거는 현판이에요.", "ISMS-P is the plaque a government inspector hangs after checking the whole castle."),
         "small": ("문 하나가 아니라 관리체계부터 손님정보 창고까지 전부예요.", "Not just one door — the whole management system, down to the guest-info storeroom."),
         "tricks": (4, [
             (WHOLE_I, ("성 전체를 봐요", "Checks the whole castle"), ("한 방이 아니라 전부", "not one room, all of it"), "calm"),
             (LIFECYCLE_I, ("손님정보는 끝까지", "Guest info, start to end"), ("모으고 쓰고 없애는 전 과정", "collect, use, and destroy — all of it"), "warm"),
             (YEARLY_I, ("매년 다시 검사", "Re-checked every year"), ("한 번으로 안 끝나요", "one pass isn't the end")),
             (LAW_I, ("법으로 정한 의무", "A legal requirement"), ("일정 규모 넘으면 꼭 받아야 해요", "mandatory past a certain size")),
         ])},
        {"svg": P4, "alt": ("ISMS-P 점검표: 1. 관리체계 수립·운영 2. 보호대책 요구사항 3. 개인정보 처리단계별 요구사항(ISMS-P만 추가)", "The ISMS-P checklist: 1. management system 2. protection measures 3. personal-data lifecycle (added only for ISMS-P)"),
         "caption": ("점검표는 세 영역이에요.", "The checklist has three areas."),
         "small": ("ISMS는 1·2만, ISMS-P는 3까지 봐요 — 개인정보 창고가 있는 성은 3번까지 필요해요.", "ISMS covers areas 1–2 only; ISMS-P adds area 3 — needed by any castle with a guest-info storeroom.")},
        {"svg": P5, "alt": ("현판이 걸린 성벽을 가면 쓴 사람이 몰래 넘어오고, 서기가 땀을 흘리며 '현판 받았는데 왜 도둑이?'", "A masked figure sneaks over the wall of a castle bearing the plaque, while a clerk sweats: we got the plaque — why a thief?"),
         "caption": ("현판이 있어도 도둑은 와요.", "The plaque doesn't stop thieves."),
         "small": ('현판은 "기준을 지켰다"는 뜻이지 "안전 보장"은 아니에요. 진짜 지키는 건 <a href="policy-ko.html">규칙 두루마리</a>와 평소 단속이에요.',
                   'The plaque means the standard was met — not that nothing can go wrong. The real work is the <a href="policy-en.html">rule scroll</a> and everyday upkeep.')},
    ],
    "summary": (("<b>ISMS/ISMS-P</b> = 나라의 검사관이 성 전체의 <b>관리체계와 보호대책</b>을 보고 거는 <b>인증 현판</b>. ISMS-P는 <b>개인정보 처리 전 과정</b>까지 더 봐요.",
                 "<b>ISMS/ISMS-P</b> = the <b>certification plaque</b> a government inspector hangs after checking a castle's whole <b>management system and protection measures</b>. ISMS-P also checks the <b>entire personal-data lifecycle</b>."),
                ("ISMS(정보보호 관리체계)와 ISMS-P(정보보호 및 개인정보보호 관리체계)는 한국인터넷진흥원(KISA) 등 인증기관이 심사해 주는 법정 인증 제도예요. 일정 규모 이상 사업자는 의무적으로 받아야 하고, 최초 인증 후 매년 사후심사를 받아요. ISMS는 보안 관리체계 전반을, ISMS-P는 개인정보 수집부터 파기까지의 처리 단계별 요구사항까지 추가로 심사해요.",
                 "ISMS (Information Security Management System) and ISMS-P (adding Personal Information protection) are statutory certifications in Korea, audited by bodies such as KISA. Businesses past a certain size must obtain it, with an annual follow-up review after initial certification. ISMS covers the overall security management system; ISMS-P additionally reviews requirements across the full personal-data lifecycle, from collection to destruction.")),
    "glossary": [
        ("ISMS", "ISMS", ("보안 관리체계 인증.", "Security management system certification."), ("관리체계 수립·운영과 보호대책 요구사항을 심사해요.", "Reviews the management system and the protection measures.")),
        ("ISMS-P", "ISMS-P", ("ISMS + 개인정보 처리단계.", "ISMS plus the personal-data lifecycle."), ("손님정보를 모으고, 쓰고, 없애는 전 과정까지 추가로 봐요.", "Also reviews collecting, using, and destroying guest info, start to finish.")),
        ("인증기관", "Certification body (KISA 등)", ("검사관을 보내는 곳.", "The office that sends the inspector."), ("한국인터넷진흥원(KISA) 등이 심사해요.", "Bodies such as KISA conduct the review.")),
        ("관리체계 수립·운영", "ISMS management process", ("정책·조직·위험평가.", "Policy, organization, risk assessment."), ('성 전체의 규칙과 담당자를 정하는 일. → <a href="policy-ko.html">성의 규칙 두루마리</a>', 'Setting the whole castle\'s rules and who owns what. → <a href="policy-en.html">the castle rule scroll</a>')),
        ("보호대책 요구사항", "Protection requirements", ("문단속 각 항목.", "Each lockdown item."), ("접근 통제, 암호화 같은 구체적 항목이에요.", "Specific items like access control and encryption.")),
        ("사후관리", "Follow-up review", ("매년 다시 검사.", "Re-checked every year."), ("최초 인증으로 끝이 아니라 해마다 다시 봐요.", "Initial certification isn't the end — it's reviewed annually.")),
        ("법적 의무대상", "Mandatory scope", ("일정 규모 넘으면 의무.", "Mandatory past a certain size."), ("매출·이용자 수 등 기준을 넘는 사업자는 꼭 받아야 해요.", "Businesses over revenue or user thresholds must obtain it.")),
        ("규정 준수", "Compliance", ("검사관이 증거를 봐요.", "The inspector checks the evidence."), ('ISMS-P도 결국 증거로 증명해요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'ISMS-P is also proven with evidence. → <a href="compliance-en.html">the inspector from next door</a>')),
    ],
}
