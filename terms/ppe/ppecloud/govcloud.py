from _draw import *
from _world import *

# 1. 공공기관도 이 건물에 들어오고 싶어요 — 하지만 아무 데나 들어갈 수 없어요
P1 = svg(320, sky(320)
         + building(60, 50, 1.0)
         + person(320, 175, s=0.8, face=EYES, **TENANT, extra='')
         + bubble(380, 70, 300, 64, "⟦우리도 이 건물에 들어가서 비용을 아끼고 싶은데... 공공데이터인데 괜찮을까요?|we want in too, to save money — but this is public data, is it okay?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦공공기관도 공유 건물에 들어가서 비용을 아끼고 싶어요|public agencies want in too, to save on cost⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 아무 건물에나 입주하면 안 돼요 — 검증되지 않은 건물엔 위험해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + building(80, 40, 0.8) + label(170, 24, "⟦이 건물, 안전 점검은 받았나?|was this building ever inspected?⟧", 12, "var(--bad)", cls="d")
         + building(400, 40, 0.8) + label(490, 24, "⟦저 건물은요?|what about that one?⟧", 12, "var(--bad)", cls="d")
         + person(650, 198, s=0.75, face=FROWN + SWEAT, **MANAGER)
         + label(380, 282, "⟦아무 건물에나 입주하면, 공공데이터가 안전한지 아무도 보장 못 해요|move into just any building, and nobody can vouch public data is safe⟧", 12, "var(--ink)"))

# 3. hero: 공공부문 클라우드 활용 = 검증된 건물에만, 등급에 맞춰 입주하는 조달 규정
P3 = svg(340, sky(340)
         + building(40, 40, 1.15, label_text="⟦CSAP 인증 건물|CSAP-certified building⟧")
         + '<rect x="40" y="20" width="24" height="24" fill="var(--good)"/>' + label(52, 38, "✓", 16, "#fff", cls="d")
         + office(320, 210, 0.95, label_text="⟦상등급: 민감정보|high grade: sensitive⟧")
         + office(440, 210, 0.95, label_text="⟦하등급: 일반업무|low grade: general⟧")
         + person(650, 236, s=0.75, face=EYES, **MANAGER)
         + label(380, 30, "⟦검증된 건물의, 정해진 등급 칸에만 입주해요|move in only to a certified building, into the grade your data earns⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦이게 공공부문의 클라우드 조달·활용 규정이에요|this is how the public sector procures and adopts cloud⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 입주 전 절차 — 등급 분류 → 인증 확인 → 조달 → 입주 후 지속 점검
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦공공기관 입주 절차|public-sector move-in process⟧",
                     ("⟦① 데이터 등급부터 나눠요(상/중/하)|① classify the data's grade first (high/mid/low)⟧",
                      "⟦② CSAP 인증받은 건물인지 확인해요|② check the building holds CSAP certification⟧",
                      "⟦③ 조달청 가이드대로 계약·입주해요|③ contract and move in per the procurement guide⟧",
                      "⟦④ 입주 후에도 감리로 계속 점검해요|④ keep checking after move-in, via audit⟧"), 1.0))

# 5. 깨지는 곳: 건물 인증은 "건물 안전검사"일 뿐, 입주사 운영 책임은 따로예요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + building(100, 60, 0.75) + '<rect x="120" y="80" width="24" height="24" fill="var(--good)"/>' + label(132, 98, "✓", 14, "#fff", cls="d")
         + label(190, 285, "⟦건물 인증(CSAP)은 '안전검사'까지만이에요|the building's CSAP cert covers the safety inspection only⟧", 11, "var(--ink)")
         + person(560, 175, s=0.65, face=EYES, **TENANT)
         + label(560, 285, "⟦입주사가 문을 어떻게 잠그는지는 입주사 책임이에요|how the tenant locks their own door is still the tenant's job⟧", 11, "var(--ink)"))

GRADE_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><path d="M20 44 v-14 M32 44 v-24 M44 44 v-8" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
CERT_I = icon('<circle cx="32" cy="26" r="16" fill="var(--good-soft)" stroke="var(--good)" stroke-width="4"/><path d="M24 26 l6 6 l12 -12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M24 40 l-4 16 l12 -6 l12 6 l-4 -16" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/>')
PROC_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
AUDIT_I = icon('<circle cx="26" cy="26" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M36 36 L50 50" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "govcloud", "order": 3,
    "title": ("검증된 건물에만, 등급에 맞춰 입주하기", "Only Into a Certified Building, Into the Grade You Earn"),
    "h1": ("<em>공공부문 클라우드 활용</em>이 뭐예요?", "What is <em>Public-Sector Cloud Adoption</em>?"),
    "sub": ("공공부문 클라우드 활용(CSAP·가이드·감리)을, 검증된 건물에만 등급 맞춰 입주하는 조달 규정 이야기로 풀어봤어요.",
            "Public-sector cloud adoption (CSAP, guidelines, audit), told as a procurement rule: move in only to a certified building, into the grade your data earns."),
    "panels": [
        {"svg": P1, "alt": ("공공기관 직원이 비용을 아끼기 위해 공유 건물에 입주하고 싶지만 공공데이터라 걱정하며 말함", "A public-agency worker wants to move into the shared building to save cost, but worries aloud about public data"),
         "caption": ("공공기관도 공유 건물에 들어가서 비용을 아끼고 싶어요.", "Public agencies want in too, to save on cost."),
         "small": ("근데 공공데이터라 아무 데나 들어갈 순 없어요.", "But it's public data — they can't just move in anywhere.")},
        {"svg": P2, "alt": ("두 건물을 가리키며 안전 점검을 받았는지 묻는 관리자가 땀을 흘림", "A sweating manager, pointing at two buildings, asks whether each was ever safety-inspected"),
         "caption": ("아무 건물에나 입주하면 안전을 아무도 보장 못 해요.", "Move into just any building, and nobody can vouch for safety."),
         "small": ("검증 없는 건물은 공공데이터엔 너무 위험해요.", "An uncertified building is too risky for public data.")},
        {"svg": P3, "hero": True, "alt": ("체크마크가 붙은 CSAP 인증 건물 안에 상등급 민감정보 사무실과 하등급 일반업무 사무실이 나뉘어 있고 관리자가 지켜봄", "Inside a check-marked CSAP-certified building, a high-grade sensitive-data office and a low-grade general office sit apart, watched by a manager"),
         "caption": ("검증된 건물의, 정해진 등급 칸에만 입주해요.", "Move in only to a certified building, into the grade your data earns."),
         "small": ("이게 공공부문의 클라우드 조달·활용 규정이에요.", "This is how the public sector procures and adopts cloud."),
         "tricks": (4, [
             (GRADE_I, ("데이터 등급부터 나눠요", "Classify the data's grade first"), ("상/중/하로요", "high / mid / low"), "calm"),
             (CERT_I, ("CSAP 인증 건물인지 봐요", "Check for CSAP certification"), ("건물 자체의 안전검사예요", "the building's own safety check")),
             (PROC_I, ("조달청 가이드대로 계약해요", "Contract per the procurement guide"), ("정해진 절차가 있어요", "there's a set process"), "warm"),
             (AUDIT_I, ("입주 후에도 감리로 점검해요", "Keep checking after move-in, via audit"), ("한 번 인증으로 끝이 아니에요", "certification isn't a one-time thing")),
         ])},
        {"svg": P4, "alt": ("공공기관 입주 절차 안내판: 등급 분류 → 인증 확인 → 조달 계약 → 입주 후 지속 점검", "A board listing the public-sector move-in process: classify grade → check certification → procurement contract → ongoing audit after move-in"),
         "caption": ("입주까지 네 단계를 거쳐요.", "Moving in goes through four steps."),
         "small": ("등급이 높을수록 들어갈 수 있는 칸이 줄어요.", "The higher the grade, the fewer spots qualify.")},
        {"svg": P5, "alt": ("왼쪽: 건물 인증 체크마크는 안전검사까지만. 오른쪽: 입주사가 자기 문을 어떻게 잠그는지는 별개 책임", "Left: the building's certification checkmark covers only the safety inspection. Right: how the tenant locks their own door is a separate responsibility"),
         "caption": ("건물 인증은 '안전검사'까지만이에요.", "The building's certification covers the safety inspection only."),
         "small": ("입주사가 문을 어떻게 잠그는지는 입주사 책임이에요.", "How the tenant locks their own door is still the tenant's job.")},
    ],
    "summary": (("<b>공공부문 클라우드 활용</b> = 검증된 건물(<b>CSAP 인증</b>)에만, 데이터 <b>등급에 맞는 칸</b>으로, <b>정해진 절차</b>를 거쳐 입주하는 것.",
                 "<b>Public-sector cloud adoption</b> means moving into a <b>certified building (CSAP)</b> only, into the <b>grade that fits your data</b>, through a <b>set procedure</b>."),
                ("공공기관이 민간 클라우드를 쓰려면 CSAP(클라우드서비스 보안인증)를 받은 서비스 중에서, 데이터 등급(상·중·하)에 맞는 등급의 서비스를 조달청 가이드에 따라 계약해야 해요. 입주 이후에도 정보시스템 감리 등으로 지속적인 점검을 받아요. CSAP 인증 기준 자체(건물 안전검사의 세부 항목)는 별도 페이지에서 다뤄요.",
                 "To use private cloud, public agencies must choose a CSAP (Cloud Security Assurance Program)-certified service at the grade matching their data's classification (high/mid/low), contracted per the procurement agency's guide. After moving in, ongoing checks continue through IS audits and similar reviews. The CSAP certification criteria itself — the building's own safety-inspection checklist — is covered on a separate page.")),
    "glossary": [
        ("공공부문 클라우드 활용", "Public-sector cloud adoption", ("검증된 건물에, 등급 맞춰 입주하는 규정.", "The rule: move into a certified building, at the right grade."), ("조달 절차와 지속 점검까지 포함해요.", "Covers the procurement process and ongoing checks too.")),
        ("CSAP", "CSAP", ("건물 자체의 안전검사 인증.", "The building's own safety-inspection certification."), ("이 페이지는 입주 활용 쪽에 집중해요.", "This page focuses on the move-in/adoption side.")),
        ("데이터 등급", "Data classification grade", ("상·중·하로 나눈 민감도.", "Sensitivity split into high / mid / low."), ("등급이 높을수록 들어갈 수 있는 칸이 줄어요.", "Higher grade, fewer qualifying spots.")),
        ("조달청 가이드", "Procurement guide", ("계약 전에 따라야 하는 절차서.", "The procedure manual to follow before contracting."), ("공공기관이 임의로 계약할 수 없게 해줘요.", "Keeps agencies from contracting on their own terms.")),
        ("정보시스템 감리", "IS audit", ("입주 후에도 계속하는 점검.", "The ongoing check even after move-in."), ('다른 PPE 세계에서 자세히 다뤄요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Covered in depth in another PPE world. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("민간 클라우드 vs 공공 클라우드", "Private vs government cloud", ("아무나 입주 가능 건물 vs 인증받은 건물.", "A building anyone can rent vs a certified one."), ("공공데이터는 후자로만 가요.", "Public data goes into the certified kind only.")),
        ("클라우드 서비스 모델", "Cloud service model", ("뼈대만/인테리어까지/완제품.", "Bare shell / interior done / move-in ready."), ('어느 모델이든 등급 규정은 똑같이 적용돼요. → <a href="cloudmodel-ko.html">셋 중 골라 빌리기</a>', 'The grade rule applies no matter which model. → <a href="cloudmodel-en.html">pick one to rent</a>')),
        ("멀티클라우드", "Multi-cloud", ("여러 건물에 나눠 입주하는 전략.", "The strategy of spreading across several buildings."), ('공공기관도 이중화를 위해 쓰기도 해요. → <a href="multicloud-ko.html">여러 건물에 동시 입주</a>', 'Agencies sometimes use this for redundancy too. → <a href="multicloud-en.html">moving into several buildings at once</a>')),
    ],
}
