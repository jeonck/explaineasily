from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")


def scroll(x, y, w, h, title, tiers, size=12):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect x="-10" y="-11" width="{w + 20}" height="22" rx="11" fill="#C9A86A"/><rect x="-10" y="{h - 11}" width="{w + 20}" height="22" rx="11" fill="#C9A86A"/>'
           + label(w / 2, 34, title, 13, "#142033", cls="d"))
    for i, (c, t, sub) in enumerate(tiers):
        yy = 68 + i * 44
        out += f'<circle cx="26" cy="{yy - 5}" r="8" fill="{c}"/>' + label(42, yy, t, size, "#142033", "start", cls="d") + label(42, yy + 17, sub, size - 1, "#142033", "start")
    return out + "</g>"


def storeroom(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="-10" width="140" height="110" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/>'
            f'<path d="M-80 -10 L0 -46 L80 -10 Z" fill="var(--good)"/><rect x="-16" y="40" width="32" height="50" fill="var(--night)"/>'
            + label(0, -58, "⟦손님 정보 창고|guest-info storeroom⟧", 11, "var(--muted)") + "</g>")


def logbook(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="60" height="46" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            '<path d="M10 14 h40 M10 23 h40 M10 32 h26" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/></g>')


# 1. 손님 정보 창고도 다른 방과 똑같이 취급돼요
P1 = svg(340, sky(340)
         + storeroom(190, 150, 0.9) + person(190, 240, s=0.6, face=SMILE, **CLERK)
         + storeroom(560, 150, 0.9) + person(560, 240, s=0.6, face=FROWN, **CLERK)
         + label(190, 325, "⟦규칙대로 단속|follows the rules⟧", 10, "var(--good)") + label(560, 325, "⟦생각나는 대로|whatever comes to mind⟧", 10, "var(--bad)")
         + label(380, 30, "⟦손님 정보 창고도 다른 방처럼 담당자 마음대로예요|the guest-info storeroom is locked up however its clerk feels like, same as any room⟧", 13, "var(--ink)", cls="d"))

# 2. 유출되면 손님 한 명 한 명이 다쳐요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + storeroom(190, 150, 1.0) + person(300, 130, s=0.6, face=MASK)
         + logbook(340, 150, 0.9) + '<path d="M300 150 L330 150" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>'
         + "".join(person(480 + i * 60, 170, s=0.5, face=FROWN) for i in range(4))
         + label(620, 230, "⟦손님 한 명 한 명이 다쳐요|every single guest gets hurt⟧", 12, "var(--bad)")
         + label(380, 258, "⟦보통 창고보다 훨씬 더 엄격해야 해요|it has to be locked down far more strictly than any ordinary room⟧", 13, "var(--ink)"))

# 3. 내부관리계획 = 손님 정보 창고 전용 단속 수칙 (hero)
TIERS = (("var(--good)", "⟦접근 권한 — 출입자 명부, 최소화|access — a visitor log, kept to the minimum⟧", ""),
         ("#5B8DEF", "⟦접속기록 — 언제 누가 들어왔는지, 보관|access logs — who, when, kept on file⟧", ""),
         ("var(--accent)", "⟦암호화 — 주민번호 등은 반드시|encryption — required for ID numbers, etc.⟧", ""),
         ("var(--bad)", "⟦물리적 보안·백신 — 자물쇠와 벌레 차단|physical security, antivirus — the lock and the bug-blocker⟧", ""))
P3 = svg(360, sky(360)
         + scroll(60, 50, 460, 230, "⟦손님 정보 창고 전담 수칙|STOREROOM-ONLY RULEBOOK⟧", TIERS, 12)
         + storeroom(640, 130, 0.75) + person(640, 210, s=0.55, face=EYES, **GUARD)
         + label(380, 30, "⟦내부관리계획 = 손님 정보 창고만을 위한 전용 수칙|an internal management plan = a rulebook just for the guest-info storeroom⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦일반 규칙 두루마리보다 더 세세하고 더 엄격해요|more detailed, more strict than the castle's general rule scroll⟧", 12, "var(--muted)"))

# 4. 일반 두루마리 vs 손님정보 전용 두루마리
P4 = svg(300, sky(300)
         + scroll(50, 30, 300, 240, "⟦성의 일반 규칙|GENERAL CASTLE RULES⟧", (("var(--good)", "⟦문단속 전반|locks, in general⟧", ""),), 12)
         + scroll(410, 30, 300, 240, "⟦손님정보 전용 수칙|GUEST-INFO RULEBOOK⟧", (("var(--bad)", "⟦법(고시)에서 정한 세부 항목|items set out by law (notice)⟧", ""),), 12)
         + label(380, 290, "⟦후자는 개인정보보호법 시행령·고시가 정한 법적 의무예요|the latter is a legal duty set by the Personal Information Protection Act and its notices⟧", 11, "var(--muted)"))

# 5. 문서만 있고 안 지키면 소용없어요
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + scroll(60, 50, 220, 170, "⟦수칙|RULEBOOK⟧", (), 11)
         + person(360, 140, s=0.8, face=EYES, **KING)
         + bubble(400, 40, 260, 46, "⟦접속기록 좀 보여주시겠어요?|may I see the access logs?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(620, 160, s=0.7, face=FROWN + SWEAT, **CLERK)
         + label(380, 258, "⟦글로만 있으면 종이예요 — 실제 기록으로 증명해야 해요|words on a page are just paper — real logs are what prove it⟧", 13, "var(--ink)"))

PAGE = {
    "slug": "privacysafeguard", "order": 4,
    "title": ("손님 정보 창고의 전담 단속 수칙", "The Storeroom's Own Lockdown Rulebook"),
    "h1": ("<em>개인정보 안전성 확보조치·내부관리계획</em>이 뭐예요?", "What are <em>Personal-Data Safeguard Measures and the Internal Management Plan</em>?"),
    "sub": ("개인정보 안전성 확보조치와 내부관리계획을 손님 정보 창고만을 위한 전담 단속 수칙 이야기로 풀어봤어요.",
            "Personal-data safeguard measures and the internal management plan, told as a story about a rulebook written just for the guest-info storeroom."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽 창고는 담당자가 규칙대로 단속하고, 오른쪽 창고는 담당자가 생각나는 대로 함", "A clerk on the left locks the storeroom by the rules; a clerk on the right just does whatever comes to mind"),
         "caption": ("손님 정보 창고도 다른 방과 똑같이 취급돼요.", "The guest-info storeroom gets treated like any other room."),
         "small": ("담당자 마음에 따라 들쭉날쭉이에요.", "It swings wildly depending on who's in charge.")},
        {"svg": P2, "alt": ("가면 쓴 도둑이 손님 정보 창고에서 장부를 훔쳐가고, 손님 네 명이 찡그린 얼굴로 서 있음", "A masked thief steals a logbook from the guest-info storeroom while four guests stand frowning"),
         "caption": ("유출되면 손님 한 명 한 명이 다쳐요.", "A leak hurts every single guest, one by one."),
         "small": ("그래서 보통 창고보다 훨씬 더 엄격해야 해요.", "That's why it has to be locked down far more strictly than any ordinary room.")},
        {"svg": P3, "hero": True, "alt": ("손님 정보 창고 전담 수칙 두루마리: 접근 권한, 접속기록, 암호화, 물리적 보안·백신 네 항목. 옆에 창고와 경비", "A rulebook scroll just for the storeroom: access rights, access logs, encryption, physical security and antivirus — with the storeroom and a guard beside it"),
         "caption": ("내부관리계획은 손님 정보 창고만을 위한 전용 수칙이에요.", "The internal management plan is a rulebook written just for the guest-info storeroom."),
         "small": ("일반 규칙 두루마리보다 더 세세하고 더 엄격해요.", "More detailed and stricter than the castle's general rule scroll."),
         "tricks": (4, [
             (icon('<rect x="14" y="20" width="36" height="28" rx="4" fill="#FFF8E7" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="14" r="8" fill="none" stroke="var(--good)" stroke-width="3"/>'),
              ("접근 권한 관리", "Access-rights management"), ("출입자 명부, 최소화", "a visitor log, kept to the minimum"), "warm"),
             (icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#5B8DEF" stroke-width="3"/><path d="M18 24 h28 M18 32 h28 M18 40 h18" stroke="#142033" stroke-width="2.5"/>'),
              ("접속기록 보관·점검", "Access-log retention"), ("언제 누가 들어왔는지", "who came in, and when")),
             (icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="5"/><rect x="24" y="30" width="16" height="14" rx="3" fill="var(--accent)"/>'),
              ("고유식별정보 암호화", "Encrypting unique IDs"), ("주민번호 등은 반드시", "required for things like ID numbers"), "calm"),
             (icon('<rect x="18" y="8" width="28" height="48" rx="4" fill="var(--night)"/><circle cx="32" cy="30" r="6" fill="var(--bad)"/>'),
              ("물리적 보안·백신", "Physical security, antivirus"), ("자물쇠와 벌레 차단", "the lock, and the bug-blocker")),
         ])},
        {"svg": P4, "alt": ("왼쪽은 '성의 일반 규칙' 두루마리, 오른쪽은 '손님정보 전용 수칙' 두루마리 — 후자는 법이 정한 세부 항목", "Left: the general castle rules scroll. Right: the guest-info-only rulebook — its items are set out by law"),
         "caption": ("성의 일반 규칙과는 다른, 전용 두루마리예요.", "It's a separate rulebook, apart from the castle's general rules."),
         "small": ("개인정보보호법 시행령과 고시(안전성 확보조치 기준)가 정한 법적 의무 항목이에요.", "Its items are legal requirements set by the Personal Information Protection Act's enforcement decree and the safeguard-measures notice.")},
        {"svg": P5, "alt": ("왕이 수칙 두루마리 옆에서 '접속기록 좀 보여주시겠어요?'라고 묻고, 서기가 땀을 흘림", "Beside the rulebook, the king asks may I see the access logs? while the clerk sweats"),
         "caption": ("문서만 있고 안 지키면 소용없어요.", "A rulebook with nothing behind it is worthless."),
         "small": ('글로만 있으면 종이예요 — 실제 접속기록으로 증명해야 해요. 검사관은 늘 <a href="compliance-ko.html">증거</a>부터 봐요.',
                   'Words on a page are just paper — real access logs are what prove it. The <a href="compliance-en.html">inspector</a> always checks the evidence first.')},
    ],
    "summary": (("<b>내부관리계획</b> = <b>손님 정보 창고</b>만을 위한 전담 단속 수칙. <b>접근 권한·접속기록·암호화·물리적 보안</b> 네 가지를 구체적으로 정해요.",
                 "An <b>internal management plan</b> = a <b>lockdown rulebook written just for the guest-info storeroom</b>. It spells out <b>access rights, access logs, encryption, and physical security</b> in detail."),
                ("개인정보의 안전성 확보조치는 개인정보보호법 시행령과 관련 고시가 정한 기술적·관리적·물리적 보호조치 기준이에요. 내부관리계획은 이 기준을 조직이 실제로 어떻게 지킬지 문서로 정리한 것으로, 접근권한 관리·접속기록 보관·암호화·백신·물리적 보안 등을 구체적으로 규정해요. 일정 규모 이상 개인정보처리자는 수립·시행이 의무예요.",
                 "Safeguard measures for personal data are the technical, managerial, and physical protection standards set by the enforcement decree of Korea's Personal Information Protection Act and its related notices. The internal management plan is the document that spells out how an organization actually meets those standards — covering access-rights management, access-log retention, encryption, antivirus, and physical security. Establishing and enforcing it is mandatory for personal-data handlers above a certain size.")),
    "glossary": [
        ("내부관리계획", "Internal management plan", ("창고 전담 수칙 문서.", "The storeroom's own rulebook document."), ("손님 정보를 다루는 조직이 실제로 세워야 하는 문서예요.", "A document any organization handling guest info must actually draw up.")),
        ("안전성 확보조치 기준", "Safeguard-measures notice", ("법이 정한 세부 항목.", "The detailed items set by law."), ("개인정보보호위원회의 고시로, 기술적·관리적·물리적 조치를 정해요.", "A notice from Korea's Personal Information Protection Commission, setting technical, managerial, and physical measures.")),
        ("접근 권한 관리", "Access-rights management", ("출입자 명부.", "The visitor log."), ("누가 들어올 수 있는지 최소한으로 정하고 기록해요.", "Decides and records who may enter, kept to the minimum.")),
        ("접속기록 보관·점검", "Access-log retention and review", ("언제 누가 들어왔는지 일지.", "The log of who came in, and when."), ("일정 기간(보통 1~2년) 보관하고 정기적으로 점검해요.", "Kept for a set period (usually one to two years) and reviewed regularly.")),
        ("고유식별정보 암호화", "Encrypting unique identifiers", ("주민번호 같은 건 반드시.", "Mandatory for things like ID numbers."), ('성에 들어온 뒤에도 자물쇠로 한 번 더 잠가요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Locked again even after it\'s inside the castle. → <a href="encryption-en.html">the letter nobody can read without the key</a>')),
        ("개인정보 보호책임자", "Chief Privacy Officer (CPO)", ("창고 전담 책임자.", "The officer responsible for the storeroom."), ("내부관리계획을 세우고 지키는 걸 책임지는 사람이에요.", "The person responsible for drawing up and enforcing the plan.")),
        ("성의 규칙 두루마리", "Castle-wide security policy", ("일반 규칙.", "The general rules."), ('내부관리계획은 이것의 손님정보 전용 버전이에요. → <a href="policy-ko.html">성의 규칙 두루마리</a>', 'The internal management plan is its guest-info-only version. → <a href="policy-en.html">the castle rule scroll</a>')),
        ("규정 준수", "Compliance", ("검사관이 증거를 봐요.", "The inspector checks the evidence."), ('계획만 있고 기록이 없으면 검사를 통과 못 해요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'A plan with no records behind it fails inspection. → <a href="compliance-en.html">the inspector from next door</a>')),
    ],
}
