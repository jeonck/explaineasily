"""기능안전 표준(ISO 26262·IEC 61508) — 일반-산업 간 표준 위계 관점. 위험 등급·검증 강도의 일반 개념은 ppeswe/swsafety 쪽."""
from _draw import *
from _world import *

BASE_I = icon('<rect x="10" y="40" width="44" height="14" rx="3" fill="var(--accent)"/><path d="M20 40 V24 M32 40 V18 M44 40 V28" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>')
CAR_I = icon('<rect x="10" y="26" width="44" height="18" rx="6" fill="var(--good)"/><circle cx="20" cy="46" r="6" fill="var(--ink)"/><circle cx="44" cy="46" r="6" fill="var(--ink)"/>')
GRADE_I = icon('<path d="M14 50 V38 M28 50 V26 M42 50 V14" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
CERT_I = icon('<circle cx="32" cy="26" r="18" fill="var(--good)"/><path d="M22 26 l7 7 l13 -16" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M24 40 l-6 16 l14 -6 l14 6 l-6 -16" fill="var(--accent)"/>')

# 1. 분야마다 "안전하다"는 말이 다 달라요
P1 = svg(300, sky(300)
         + person(200, 150, s=0.85, face=SMILE, **REP) + bubble(110, 70, 230, 44, "⟦저희 통학버스 제동장치, 안전해요!|our school bus brakes are totally safe!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **REP) + bubble(460, 70, 230, 44, "⟦저희 자동문도 안전하다고 했는데요|our automatic door was called safe too⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦분야마다 \"안전하다\"는 말의 기준이 다 달라요|every field has its own idea of what \"safe\" means⟧", 13, "var(--ink)", cls="d"))

# 2. 공통 기준이 없으면 비교도, 신뢰도 안 돼요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(220, 135, s=0.8, face=FROWN, **TEACHER) + label(220, 265, "⟦업체마다 말이 다 다른데 뭘 믿어요?|every supplier says something different — which do we trust?⟧", 11, "var(--ink)")
         + person(560, 135, s=0.75, face=SWEAT + EYES, **STUDENT) + label(560, 265, "⟦우리 반 자동문이 갑자기 안 멈췄어요|our class's automatic door suddenly wouldn't stop⟧", 11, "var(--bad)")
         + label(380, 300, "⟦공통 기준 없이 주장만 있으면, 사고가 나서야 드러나요|without a shared standard, only an accident reveals the truth⟧", 12, "var(--ink)", cls="d"))

# 3. 기능안전 표준 = 위험도에 등급을 매기고 등급별 조치를 정한 공통 규칙서 (hero)
P3 = svg(360, sky(360)
         + label(380, 26, "⟦기능안전 표준 = 위험도에 등급을 매기고, 등급별 조치를 의무화한 공통 규칙서|functional safety standard = a shared rulebook that grades risk and mandates matching safeguards⟧", 13, "var(--ink)", cls="d")
         + person(140, 130, s=0.9, face=EYES, **PRESIDENT) + gavel(220, 160, 0.9)
         + rulesboard(280, 70, 300, 240, "⟦공통 규칙서|THE SHARED RULEBOOK⟧",
                      ("⟦IEC 61508 — 모든 분야의 기본 규칙서|IEC 61508 — the base rulebook for every field⟧",
                       "⟦ISO 26262 — 자동차용으로 다시 쓴 버전|ISO 26262 — rewritten specifically for cars⟧",
                       "⟦SIL/ASIL — 위험할수록 높은 등급|SIL/ASIL — higher grade, higher risk⟧",
                       "⟦제3자 인증으로 확인|checked by third-party certification⟧"), 0.9)
         + person(650, 160, s=0.8, face=SMILE, **REP)
         + label(380, 335, "⟦분야마다 제각각이던 \'안전해요\'에 같은 등급표를 줘요|gives every field's own \"it's safe\" the same grading scale⟧", 12, "var(--muted)"))

# 4. 기본표준에서 분야별 표준으로
P4 = svg(320, sky(320, ground=False)
         + '<rect x="280" y="30" width="200" height="50" rx="8" fill="#C9A86A"/>' + label(380, 60, "⟦IEC 61508(기본)|IEC 61508 (base)⟧", 12, "#142033", cls="d")
         + '<path d="M330 80 V130 M380 80 V130 M430 80 V130" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4"/>'
         + rulesboard(130, 130, 180, 150, "⟦ISO 26262|자동차⟧", ("⟦ASIL A~D 등급|ASIL grades A–D⟧", "⟦통학버스·자동문에|applies to buses, auto-doors⟧"), 0.85)
         + rulesboard(330, 130, 180, 150, "⟦IEC 61511|화학·공정⟧", ("⟦SIL 1~4 등급|SIL grades 1–4⟧", "⟦과학실 설비에|applies to lab equipment⟧"), 0.85)
         + rulesboard(530, 130, 180, 150, "⟦IEC 62061|기계류⟧", ("⟦SIL 1~4 등급|SIL grades 1–4⟧", "⟦엘리베이터 등에|applies to elevators, etc.⟧"), 0.85)
         + label(380, 300, "⟦분야마다 전용 표준을 다시 써서 구체화해요|each field rewrites its own specific version⟧", 12, "var(--ink)", cls="d"))

# 5. 인증을 받아도 사고가 0이 되진 않아요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 120, s=0.8, face=SMILE, **PRESIDENT)
         + '<circle cx="270" cy="90" r="22" fill="var(--good)"/><path d="M258 90 l8 8 l16 -18" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + label(190, 260, "⟦등급에 맞는 안전조치는 다 거쳤어요|every safeguard for the grade is in place⟧", 11, "var(--ink)")
         + person(570, 100, s=0.85, face=SWEAT + EYES, **TEACHER)
         + label(570, 260, "⟦그래도 계속 지켜보고 점검해야죠|but it still needs constant watching and checking⟧", 11, "var(--ink)")
         + label(380, 305, "⟦등급에 맞는 조치를 어떻게 분석해 정할지는 또 다른 기법의 몫이에요|how to work out those safeguards is a job for yet another technique⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "funcsafetystd", "order": 18,
    "title": ("안전 등급을 매기는 공통 규칙서", "The Shared Rulebook That Grades Safety"),
    "h1": ("<em>기능안전 표준(ISO 26262·IEC 61508)</em>이 뭐예요?", "What is a <em>Functional Safety Standard (ISO 26262, IEC 61508)</em>?"),
    "sub": ("기능안전 표준을, 분야마다 제각각이던 \"안전해요\"란 말에 학생회가 공통 등급표와 제3자 인증을 주는 이야기로 풀어봤어요.",
            "Functional safety standards, told as a story about the student council giving every field's own claim of \"it's safe\" one shared grading scale and third-party certification."),
    "panels": [
        {"svg": P1, "alt": ("두 대표가 각각 통학버스 제동장치와 자동문이 안전하다고 자신 있게 말함", "Two reps each confidently claim their bus brakes and automatic door are safe"),
         "caption": ("분야마다 \"안전하다\"는 말의 기준이 다 달라요.", "Every field has its own idea of what \"safe\" means."),
         "small": ("서로 다른 말로는 누가 더 안전한지 비교할 수 없어요.", "Different words for \"safe\" can't be compared against each other.")},
        {"svg": P2, "alt": ("선생님이 업체마다 말이 달라 믿을 수 없다고 하고, 학생이 자동문이 갑자기 멈추지 않았다고 땀 흘리며 말함", "A teacher says every supplier's claim differs and can't be trusted; a sweating student says their class door suddenly wouldn't stop"),
         "caption": ("공통 기준이 없으면 비교도, 신뢰도 안 돼요.", "Without a shared standard, you can't compare or trust any of it."),
         "small": ("공통 기준 없이 주장만 있으면, 사고가 나서야 드러나요.", "Without a shared standard, only an accident reveals the truth.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 의사봉을 들고 IEC 61508·ISO 26262·등급·인증이 적힌 공통 규칙서를 발표함", "The council president holds a gavel, announcing a shared rulebook listing IEC 61508, ISO 26262, grading, and certification"),
         "caption": ("기능안전 표준은 위험도에 등급을 매기고, 등급별 조치를 의무화한 공통 규칙서예요.", "A functional safety standard is a shared rulebook that grades risk and mandates matching safeguards."),
         "small": ("분야마다 제각각이던 '안전해요'에 같은 등급표를 줘요.", "Gives every field's own \"it's safe\" the same grading scale."),
         "tricks": (4, [
             (BASE_I, ("공통 기본표준(IEC 61508)", "Base standard (IEC 61508)"), ("모든 분야가 출발하는 지점이에요", "where every field starts from"), "calm"),
             (CAR_I, ("분야별 전용표준(ISO 26262)", "Domain-specific standard (ISO 26262)"), ("자동차용으로 다시 구체화해요", "rewritten specifically for cars")),
             (GRADE_I, ("등급 매기기(SIL/ASIL)", "Grading (SIL/ASIL)"), ("위험할수록 더 높은 등급", "higher risk gets a higher grade"), "warm"),
             (CERT_I, ("제3자 인증", "Third-party certification"), ("스스로 말고 바깥에서 확인해요", "checked from the outside, not by itself")),
         ])},
        {"svg": P4, "alt": ("IEC 61508 기본표준 아래로 자동차용 ISO 26262, 화학공정용 IEC 61511, 기계류용 IEC 62061이 가지처럼 뻗어 나감", "Under the base IEC 61508 standard, domain-specific versions branch out: ISO 26262 for cars, IEC 61511 for process industry, IEC 62061 for machinery"),
         "caption": ("기본표준에서 분야별 표준으로 갈라져 나와요.", "Domain-specific standards branch out from the base standard."),
         "small": ("분야마다 전용 표준을 다시 써서 구체화해요.", "Each field rewrites its own specific version.")},
        {"svg": P5, "alt": ("왼쪽: 학생회장이 등급에 맞는 조치를 다 거쳤다고 말함. 오른쪽: 선생님이 그래도 계속 지켜봐야 한다고 땀 흘리며 말함", "Left: the president says every safeguard for the grade is done. Right: the sweating teacher says it still needs constant watching"),
         "caption": ("인증을 받아도 사고가 0이 되진 않아요.", "Even certified, the risk of accidents never reaches zero."),
         "small": ("등급에 맞는 조치를 어떻게 분석해 정할지는 또 다른 기법의 몫이에요.", "How to work out those safeguards is a job for yet another technique.")},
    ],
    "summary": (("<b>기능안전 표준</b> = <b>IEC 61508</b>이라는 공통 기본표준에서, 자동차 같은 <b>분야별로 다시 구체화</b>한(ISO 26262) <b>등급(SIL/ASIL)</b> 기반 안전 규칙서.",
                 "<b>Functional safety standards</b> = safety rulebooks built on the common base, <b>IEC 61508</b>, then rewritten and specialized for a domain like automobiles (<b>ISO 26262</b>), using risk <b>grades (SIL/ASIL)</b>."),
                ("IEC 61508은 전자·전기·프로그래머블 전자 시스템 전반의 기능안전을 다루는 범용 국제표준으로, 위험도에 따라 SIL(Safety Integrity Level) 1~4 등급을 매겨요. ISO 26262는 이를 자동차 산업에 맞춰 특화한 표준으로, ASIL(Automotive Safety Integrity Level) A~D 등급을 쓰고 차량 생애주기 전체(기획·설계·검증·생산·폐기)에 걸친 요구사항을 정해요. 등급이 높을수록 더 엄격한 개발·검증 절차와 독립적인 제3자 인증이 요구돼요.",
                 "IEC 61508 is a general international standard covering functional safety of electrical, electronic, and programmable electronic systems, grading risk with SIL (Safety Integrity Level) 1 through 4. ISO 26262 specializes this for the automotive industry, using ASIL (Automotive Safety Integrity Level) A through D and setting requirements across the vehicle's entire lifecycle — planning, design, verification, production, and decommissioning. Higher grades demand stricter development and verification processes, plus independent third-party certification.")),
    "glossary": [
        ("기능안전표준", "Functional Safety Standard", ("위험도에 등급을 매기는 공통 규칙서.", "A shared rulebook that grades risk."), ("분야마다 전용 버전으로 다시 쓰여요.", "Rewritten into a domain-specific version for each field.")),
        ("IEC 61508", "IEC 61508", ("모든 분야가 출발하는 기본표준.", "The base standard every field starts from."), ("전기·전자 시스템 전반을 다뤄요.", "Covers electrical and electronic systems broadly.")),
        ("ISO 26262", "ISO 26262", ("자동차용으로 특화한 표준.", "The standard specialized for automobiles."), ("IEC 61508을 자동차에 맞게 다시 썼어요.", "Rewrites IEC 61508 specifically for cars.")),
        ("SIL", "SIL (Safety Integrity Level)", ("위험도에 따른 등급(1~4).", "A risk-based grade, 1 through 4."), ("IEC 61508과 여러 산업 표준이 함께 써요.", "Used by IEC 61508 and several industry-specific standards.")),
        ("ASIL", "ASIL (Automotive Safety Integrity Level)", ("자동차용 등급(A~D).", "The automotive-specific grade, A through D."), ("ISO 26262만의 등급 체계예요.", "A grading scheme unique to ISO 26262.")),
        ("제3자 인증", "Third-Party Certification", ("스스로 안전하다고 하지 않고, 바깥에서 확인받는 것.", "Not declaring safety yourself — getting it checked from outside."), ("표준을 실제로 지켰는지 독립적으로 확인해요.", "Independently verifies the standard was actually followed.")),
        ("위험·안전성 분석", "Risk/Safety Analysis", ("등급을 정하기 전에 위험을 찾아내는 기법들.", "The techniques that find risks before a grade is even assigned."), ('FTA·FMEA·HAZOP이 이 분석을 맡아요. → <a href="riskanalysis-ko.html">사고를 거꾸로, 또는 미리 훑어보기</a>', 'FTA, FMEA, and HAZOP handle this analysis. → <a href="riskanalysis-en.html">tracing an accident backward — or scanning for it ahead of time</a>')),
        ("소프트웨어/기능안전(일반 개념)", "Software/Functional Safety (General Concept)", ("위험이 클수록 검증을 몇 겹으로 더 거치는 일반 원리.", "The general principle that higher risk means more layers of checking."), ('이 페이지는 표준 간 위계를, 일반 개념은 다른 세계에서. → <a href="swsafety-ko.html">오탈자 하나의 무게가 다른 책</a>', 'This page covers the standard hierarchy — the general idea lives in another world. → <a href="swsafety-en.html">the book where one typo weighs differently</a>')),
    ],
}
