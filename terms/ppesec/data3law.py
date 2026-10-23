from _draw import *

INSPECTOR_A = dict(hat="var(--stone-dark)", shirt="#4A5A72")
INSPECTOR_B = dict(hat="#5B8DEF", shirt="#5B8DEF", face=EYES)
INSPECTOR_C = dict(hat="#B5651D", shirt="#B5651D")
CHIEF = dict(hat="#E9B44C", shirt="#7B3FA0", face=EYES)


def rulebook(x, y, s=1.0, color="#FFF8E7"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-28" width="44" height="56" rx="4" fill="{color}" stroke="#C9A86A" stroke-width="3"/>'
            + '<path d="M-12 -14 h24 M-12 -4 h24 M-12 6 h16" stroke="#142033" stroke-width="2" stroke-linecap="round"/></g>')


def nametag(x, y, s=1.0, text="", color="var(--panel)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="28" rx="6" fill="{color}" stroke="var(--line)" stroke-width="2"/>'
            + label(0, 5, text, 11, "#142033") + "</g>")


# 1. 세 권의 규칙서, 세 명의 검사관
P1 = svg(320, sky(320)
         + person(150, 160, s=0.65, face=EYES, **INSPECTOR_A) + rulebook(150, 90) + label(150, 250, "⟦개인정보보호법|the Personal Information Protection Act⟧", 10, "var(--muted)")
         + person(380, 160, s=0.65, **INSPECTOR_B) + rulebook(380, 90) + label(380, 250, "⟦정보통신망법|the Network Act⟧", 10, "var(--muted)")
         + person(610, 160, s=0.65, face=EYES, **INSPECTOR_C) + rulebook(610, 90) + label(610, 250, "⟦신용정보법|the Credit Information Act⟧", 10, "var(--muted)")
         + label(380, 40, "⟦성에 규칙서 세 권과 검사관 세 명이 따로 있었어요|the castle had three separate rulebooks and three separate inspectors⟧", 13, "var(--ink)", cls="d"))

# 2. 규칙이 겹치고 엇갈려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=FROWN + SWEAT, **INSPECTOR_A)
         + bubble(60, 50, 250, 44, "⟦이 손님 기록, 제 규칙으로 보면 막혀요|by my rulebook, recording this guest is blocked⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(550, 150, s=0.8, face=EYES, **INSPECTOR_C)
         + bubble(420, 50, 250, 44, "⟦제 규칙으로 보면 괜찮은데요?|but by my rulebook, it's fine⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦규칙서가 셋이라, 성 사람들도 헷갈려요|three rulebooks mean even the castle's own people get confused⟧", 12, "var(--ink)", cls="d"))

# 3. 2020년 개정 — 한 검사관 아래로, 새 이름표도 생겼어요 (hero)
P3 = svg(340, sky(340)
         + person(380, 110, s=0.9, **CHIEF) + label(380, 40, "⟦개인정보보호위원회|the Personal Information Protection Commission⟧", 13, "var(--ink)", cls="d")
         + rulebook(230, 200, 0.8) + rulebook(380, 210, 0.8) + rulebook(530, 200, 0.8)
         + '<path d="M300 180 L360 140 M460 180 L400 140" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + nametag(380, 280, 1.0, "⟦가명정보: 이름 지우고 통계·연구에만|pseudonymized: name removed, for research/stats only⟧", "var(--good-soft)")
         + label(380, 320, "⟦세 검사관을 한 감독 아래로, 그리고 새 이름표 하나|three inspectors under one oversight office, plus one brand-new label⟧", 13, "var(--ink)", cls="d"))

MERGE_I = icon('<circle cx="18" cy="24" r="8" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="46" cy="24" r="8" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="32" cy="24" r="8" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><path d="M32 32 v12" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="50" r="7" fill="#E9B44C"/>')
TAG_I = icon('<rect x="10" y="22" width="44" height="22" rx="6" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="20" cy="33" r="4" fill="var(--good)"/>')
STAT_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--good)"/><rect x="27" y="28" width="10" height="26" fill="var(--good)"/><rect x="42" y="16" width="10" height="38" fill="var(--good)"/>')
NOREID_I = icon('<path d="M10 32 q22 -20 44 0 q-22 20 -44 0z" fill="none" stroke="var(--muted)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--muted)"/><path d="M12 14 L52 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "data3law", "order": 22,
    "title": ("세 권의 규칙서를 한 검사관 아래로", "Three Rulebooks, Under One Inspector"),
    "h1": ("<em>데이터 3법 개정</em>이 뭐예요?", "What is the <em>Three Data Acts Amendment</em>?"),
    "sub": ("데이터 3법 개정(2020)을, 각자 따로 놀던 규칙서 세 권을 한 검사관 아래로 모으고 새 이름표를 만든 이야기로 풀어봤어요.",
            "The 2020 Three Data Acts amendment, told as a story about gathering three separately-run rulebooks under one inspector, and inventing one new label."),
    "panels": [
        {"svg": P1, "alt": ("개인정보보호법, 정보통신망법, 신용정보법이라는 규칙서 세 권과 그걸 각자 보는 검사관 세 명", "Three rulebooks — the Personal Information Protection Act, the Network Act, the Credit Information Act — each watched by its own inspector"),
         "caption": ("성에 규칙서 세 권과 검사관 세 명이 따로 있었어요.", "The castle had three separate rulebooks and three separate inspectors."),
         "small": ("개인정보보호법, 정보통신망법, 신용정보법 — 비슷한 걸 다루는데 각자 따로 봤어요.", "The Personal Information Protection Act, the Network Act, the Credit Information Act — covering similar ground, each watched separately.")},
        {"svg": P2, "alt": ("한 검사관은 손님 기록이 자기 규칙으로는 막힌다고 말하고, 다른 검사관은 자기 규칙으로는 괜찮다고 말해 서로 엇갈림", "One inspector says recording a guest is blocked by his rulebook, while another says it's fine by hers — the two disagree"),
         "caption": ("규칙이 겹치고 엇갈려요.", "The rules overlap and contradict each other."),
         "small": ("같은 손님 기록을 두고 규칙서마다 다른 답이 나와요. 성 사람들도 헷갈려요.", "The very same guest record gets a different answer from each rulebook. Even the castle's own people get confused.")},
        {"svg": P3, "hero": True, "alt": ("개인정보보호위원회라는 한 검사관 아래로 세 규칙서가 모이고, 이름을 지우고 통계·연구에만 쓰는 가명정보라는 새 이름표가 생김", "The three rulebooks are gathered under one inspector, the Personal Information Protection Commission, and a new label — pseudonymized data, with names removed, for research and statistics only — appears"),
         "caption": ("2020년 개정으로 한 검사관 아래로 모이고, 새 이름표도 생겼어요.", "The 2020 amendment gathered them under one inspector, and added a brand-new label."),
         "small": ('세 법은 그대로 있지만 감독은 한 곳(개인정보보호위원회)으로 모였고, <a href="privacy-ko.html">이름을 지운</a> 가명정보라는 개념이 새로 생겼어요.',
                   'The three Acts still exist, but oversight gathered under one office (the Commission), and a new concept — pseudonymized data, <a href="privacy-en.html">names removed</a> — was introduced.'),
         "tricks": (4, [
             (MERGE_I, ("감독을 한 곳으로", "Oversight gathered in one place"), ("개인정보보호위원회가 맡아요", "the Personal Information Protection Commission now handles it"), "calm"),
             (TAG_I, ("가명정보라는 새 이름표", "A new label: pseudonymized"), ("이름을 지운 손님 기록이에요", "a guest record with the name removed")),
             (STAT_I, ("통계·연구엔 동의 없이도", "Usable for stats/research, without full consent"), ("가명정보는 이 목적으로 쓸 수 있어요", "pseudonymized data may be used for this purpose"), "warm"),
             (NOREID_I, ("다시 이름 붙이면 안 돼요", "Re-identifying it is forbidden"), ("가명정보를 원래 손님으로 되돌리면 안 돼요", "you may not trace it back to the original guest")),
         ])},
        {"svg": svg(340, sky(340)
                    + '<rect x="30" y="30" width="700" height="260" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="700" height="34" rx="8" fill="#C9A86A"/>'
                    + label(140, 53, "⟦등급|tier⟧", 13, "#142033", cls="d") + label(400, 53, "⟦손님 기록 상태|what the record looks like⟧", 13, "#142033", cls="d") + label(610, 53, "⟦쓸 수 있는 곳|where it can be used⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M30 {64 + i * 75} h700" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(140, 100, "⟦개인정보|personal data⟧", 13, "#142033", cls="d") + label(400, 100, "⟦이름 그대로|name intact⟧", 11, "#142033") + label(610, 100, "⟦본인 동의가 있어야만|only with the person's consent⟧", 11, "#142033")
                    + label(140, 175, "⟦가명정보|pseudonymized data⟧", 13, "#142033", cls="d") + label(400, 175, "⟦이름은 지웠지만 되돌릴 단서는 남음|name removed, but re-identifiable with extra data⟧", 11, "#142033") + label(610, 175, "⟦통계·연구엔 동의 없이도|usable for stats/research without consent⟧", 11, "var(--good)")
                    + label(140, 250, "⟦익명정보|anonymized data⟧", 13, "#142033", cls="d") + label(400, 250, "⟦아예 되돌릴 수 없음|cannot be traced back at all⟧", 11, "#142033") + label(610, 250, "⟦이 법의 적용을 아예 안 받아요|falls outside this law entirely⟧", 11, "#142033")),
         "alt": ("표: 개인정보 — 이름 그대로 / 동의 필요, 가명정보 — 이름 지움·단서 남음 / 통계·연구엔 동의 없이도, 익명정보 — 되돌릴 수 없음 / 법 적용 밖", "Table: personal data — name intact / needs consent, pseudonymized — name removed but traceable / usable for research without consent, anonymized — untraceable / outside the law"),
         "caption": ("세 등급을 나란히 보면 이래요.", "Side by side, here are the three tiers."),
         "small": ("가명정보는 개인정보와 익명정보 사이의, 2020년 개정이 새로 만든 중간 지대예요.", "Pseudonymized data is a new middle ground the 2020 amendment carved out, between personal and anonymized data.")},
        {"svg": svg(320, sky(320)
                    + rulebook(190, 150, 1.1) + rulebook(230, 150, 1.1) + rulebook(270, 150, 1.1)
                    + label(230, 240, "⟦법은 셋 그대로, 합쳐진 건 아니에요|still three separate Acts — not literally merged into one⟧", 11, "var(--muted)")
                    + person(560, 150, s=0.85, **CHIEF) + label(560, 265, "⟦감독 창구만 하나로 모였어요|only the oversight window became one⟧", 11, "var(--ink)")
                    + label(380, 300, "⟦나라마다 비슷한 조정을 해요 — 국경을 넘을 땐 CBPR 같은 약속이 또 필요해요|other kingdoms do similar coordination — crossing borders still needs its own pact, like CBPR⟧", 12, "var(--ink)", cls="d")),
         "alt": ("법은 여전히 세 개로 따로 있고 감독 창구만 하나로 모임. 국경을 넘을 땐 CBPR 같은 별도 약속이 필요함", "The law is still three separate Acts; only the oversight window became one. Crossing borders still needs its own pact, like CBPR"),
         "caption": ("법 세 개가 하나로 합쳐진 건 아니에요.", "The three Acts weren't literally merged into one."),
         "small": ('감독만 한 곳으로 모였어요. 국경을 넘는 이전엔 <a href="cbpr-ko.html">CBPR</a> 같은 별도 약속이, 본인이 직접 옮기려면 <a href="mydataSec-ko.html">마이데이터</a>가 따로 있어요.',
                   'Only the oversight gathered in one place. Crossing a border still needs a separate pact like <a href="cbpr-en.html">CBPR</a>, and moving it yourself is <a href="mydataSec-en.html">MyData</a>\'s own separate story.')},
    ],
    "summary": (("<b>데이터 3법 개정</b> = 따로 놀던 규칙서 세 권(개인정보보호법·정보통신망법·신용정보법)의 감독을 <b>한 검사관(개인정보보호위원회)</b>으로 모으고, <b>가명정보</b>라는 새 이름표를 만든 2020년 법 개정.",
                 "<b>The Three Data Acts amendment</b> gathered three separately-run rulebooks — the Personal Information Protection Act, the Network Act, the Credit Information Act — under <b>one inspector (the Personal Information Protection Commission)</b>, and invented a new label: <b>pseudonymized data</b>. A 2020 legal reform."),
                ("데이터 3법 개정(2020). 개인정보보호법·정보통신망 이용촉진 및 정보보호 등에 관한 법률(정보통신망법)·신용정보의 이용 및 보호에 관한 법률(신용정보법)의 개인정보 관련 조항을 정비하고, 감독기구를 개인정보보호위원회로 일원화했어요. 핵심은 '가명정보' 개념 도입 — 추가 정보 없이는 특정 개인을 알아볼 수 없도록 처리한 정보로, 통계작성·연구·공익적 기록보존 목적이면 정보주체 동의 없이도 처리할 수 있게 했어요. 세 법 자체가 하나로 합쳐진 건 아니고, 여전히 별도 법률로 존재해요.",
                 "The 2020 Three Data Acts amendment. It realigned the personal-data provisions of the Personal Information Protection Act, the Act on Promotion of Information and Communications Network Utilization and Information Protection (the Network Act), and the Credit Information Act, and unified oversight under the Personal Information Protection Commission. Its core change was introducing 'pseudonymized data' — information processed so a specific individual can't be identified without additional information — which may be processed without the data subject's consent for statistics, research, or public-interest record-keeping. The three Acts themselves were not literally merged; each still exists as a separate law.")),
    "glossary": [
        ("데이터 3법", "Three Data Acts", ("성의 규칙서 세 권.", "The castle's three rulebooks."), ("개인정보보호법·정보통신망법·신용정보법을 함께 부르는 말이에요.", "The collective name for the Personal Information Protection Act, the Network Act, and the Credit Information Act.")),
        ("개인정보보호위원회", "Personal Information Protection Commission", ("세 규칙서를 함께 보는 검사관.", "The one inspector watching all three rulebooks."), ("2020년 개정으로 감독 권한이 이곳으로 모였어요.", "The 2020 amendment gathered oversight authority here.")),
        ("가명정보", "Pseudonymized data", ("이름을 지운 손님 기록.", "A guest record with the name removed."), ("추가 정보 없이는 특정 개인을 알아볼 수 없게 처리해요.", "Processed so a specific person can't be identified without extra information.")),
        ("익명정보", "Anonymized data", ("아예 되돌릴 수 없게 지운 기록.", "A record scrubbed so it can never be traced back."), ("이 법 자체의 적용을 받지 않아요.", "Falls outside the scope of this law entirely.")),
        ("재식별 금지", "Re-identification ban", ("가명정보를 원래 손님으로 되돌리는 것 금지.", "Forbidding tracing pseudonymized data back to the original person."), ("가명정보 처리의 핵심 조건이에요.", "The core condition attached to processing pseudonymized data.")),
        ("개인정보보호법", "Personal Information Protection Act", ("가장 기본이 되는 규칙서.", "The most foundational of the three rulebooks."), ('개인정보 보호의 큰 틀이에요. → <a href="privacy-ko.html">손님 이름표는 손님 것</a>', 'The broad framework for protecting personal data. → <a href="privacy-en.html">the visitor\'s name tag belongs to the visitor</a>')),
        ("신용정보법", "Credit Information Act", ("금융 마이데이터를 먼저 연 규칙서.", "The rulebook that opened financial MyData first."), ('마이데이터의 법적 근거가 여기서 나왔어요. → <a href="mydataSec-ko.html">내 장부는 내가 들고 다닐 권리</a>', 'MyData\'s legal basis traces back to this Act. → <a href="mydataSec-en.html">my right to carry my own ledger</a>')),
        ("규정 준수", "Compliance", ("검사관이 법대로 확인하는 것.", "The inspector confirming things follow the rulebook."), ('데이터 3법을 지키는지도 이 틀로 확인해요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'Whether the Three Data Acts are followed is checked through this same frame. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
    ],
}
