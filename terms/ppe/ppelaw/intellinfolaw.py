"""지능정보화 기본법."""
from _draw import *
from _world import *

PLAN_I = icon('<path d="M10 50 L24 30 L36 40 L54 14" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="54" cy="14" r="5" fill="var(--good)"/>')
GAP_I = icon('<circle cx="18" cy="32" r="12" fill="var(--good)"/><circle cx="46" cy="32" r="12" fill="none" stroke="var(--line)" stroke-width="3" stroke-dasharray="4 3"/><path d="M30 32 h6" stroke="var(--accent)" stroke-width="3"/>')
SHIELD_I = icon('<path d="M32 8 L52 16 V34 C52 46 44 54 32 58 C20 54 12 46 12 34 V16 Z" fill="var(--good)"/><path d="M24 32 l6 6 l12 -14" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
ROOT_I = icon('<rect x="20" y="8" width="24" height="14" rx="3" fill="var(--accent)"/><path d="M26 22 V32 M38 22 V32 M18 32 h12 M34 32 h12" stroke="var(--ink)" stroke-width="2.5"/><rect x="10" y="32" width="16" height="14" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="38" y="32" width="16" height="14" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>')

# 1. 학교가 점점 똑똑해지는데, 각 반이 각자 디지털 규칙을 만들어요
P1 = svg(300, sky(300)
         + person(180, 150, s=0.85, face=SMILE, **REP) + bubble(100, 70, 220, 40, "⟦우리 반은 숙제도 앱으로 낼게요|our class hands in homework by app⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **REP) + bubble(460, 70, 230, 40, "⟦저희 반은 아직 공책으로 내는데요|our class still hands in notebooks⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦학교에 디지털 기기와 AI가 늘어나는데, 각 반이 제각각 규칙을 만들어요|digital tools and AI are spreading through school, but each class makes its own rules⟧", 13, "var(--ink)", cls="d"))

# 2. 전체를 아우르는 큰 방향이 없으면 격차·혼란이 생겨요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(200, 135, s=0.8, face=FROWN, **STUDENT) + label(200, 265, "⟦우리 반엔 태블릿이 없어요|our class doesn't even have tablets⟧", 11, "var(--bad)")
         + person(560, 135, s=0.75, face=SWEAT + EYES, **PRESIDENT) + label(560, 265, "⟦반마다 규칙이 달라 전교 기준을 세울 수가 없어요|with each class's own rules, no school-wide standard fits⟧", 11, "var(--ink)")
         + label(380, 300, "⟦큰 방향 없이 반마다 따로 만들면, 태블릿 없는 반처럼 뒤처지는 쪽이 생겨요|without a shared direction, some classes — like the tablet-less one — fall behind⟧", 12, "var(--ink)", cls="d"))

# 3. 지능정보화 기본법 = 학교 전체의 디지털 생활을 아우르는 기본 헌장 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦지능정보화 기본법 = 학교 전체의 디지털·AI 생활을 아우르는 기본 헌장|the framework act = the charter that covers the whole school's digital and AI life⟧", 13, "var(--ink)", cls="d")
         + person(170, 130, s=0.9, face=EYES, **PRESIDENT) + gavel(250, 160, 0.9)
         + rulesboard(300, 70, 280, 220, "⟦기본 헌장|THE FRAMEWORK CHARTER⟧",
                      ("⟦디지털 전환의 큰 방향 세우기|set the big direction for going digital⟧",
                       "⟦태블릿 없는 반도 소외시키지 않기|leave no tablet-less class behind⟧",
                       "⟦데이터·AI를 안전하게 다루는 원칙|principles for handling data/AI safely⟧",
                       "⟦관련 규칙들의 기본 방향 되기|set the direction related rules follow⟧"), 0.9)
         + person(640, 160, s=0.8, face=SMILE, **REP)
         + label(380, 320, "⟦이 법은 반마다 흩어진 디지털 규칙에 하나의 큰 방향을 줘요|this Act gives one big direction to every class's scattered digital rules⟧", 12, "var(--muted)"))

# 4. 기본 헌장 → 세부 규칙들
P4 = svg(320, sky(320, ground=False)
         + '<rect x="280" y="40" width="200" height="50" rx="8" fill="#C9A86A"/>' + label(380, 70, "⟦지능정보화 기본법(헌장)|THE FRAMEWORK ACT (charter)⟧", 12, "#142033", cls="d")
         + '<path d="M330 90 V140 M380 90 V140 M430 90 V140" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4"/>'
         + rulesboard(130, 140, 180, 140, "⟦격차해소 세칙|GAP-CLOSING RULE⟧", ("⟦태블릿 지원 계획|tablet support plan⟧",), 0.85)
         + rulesboard(330, 140, 180, 140, "⟦데이터 운영 세칙|DATA-HANDLING RULE⟧", ("⟦학적 데이터 공개 범위|who sees student records⟧",), 0.85)
         + rulesboard(530, 140, 180, 140, "⟦AI 활용 세칙|AI-USE RULE⟧", ("⟦AI 숙제 도우미 사용 범위|AI homework helper limits⟧",), 0.85)
         + label(380, 305, "⟦세부 규칙들은 따로 만들되 이 헌장의 방향에 맞추려 애써요|detailed rules are made separately but try to fit this charter⟧", 12, "var(--ink)", cls="d"))

# 5. 헌장만으로는 저절로 돌아가지 않아요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 120, s=0.8, face=SMILE, **PRESIDENT) + label(190, 260, "⟦큰 방향은 확실히 정해졌어요|the big direction is now clear⟧", 11, "var(--ink)")
         + person(570, 110, s=0.85, face=SWEAT + EYES, **REP) + label(570, 260, "⟦근데 태블릿 살 돈은 어디서 나요?|but where does the tablet budget actually come from?⟧", 11, "var(--ink)")
         + label(380, 305, "⟦헌장은 방향만 줘요 — 실제 전환에는 세부 규칙과 예산이 더 필요해요|the charter only gives direction — the actual shift takes detailed rules and a budget too⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "intellinfolaw", "order": 14,
    "title": ("학교 전체의 디지털 생활을 아우르는 기본 헌장", "The Charter That Covers the Whole School's Digital Life"),
    "h1": ("<em>지능정보화 기본법</em>이 뭐예요?", "What is the <em>Framework Act on Intelligent Informatization</em>?"),
    "sub": ("지능정보화 기본법을, 반마다 제각각이던 디지털 규칙에 학생회가 하나의 큰 방향을 주는 기본 헌장 이야기로 풀어봤어요.",
            "The Framework Act on Intelligent Informatization, told as a story about the student council giving one shared direction to every class's scattered digital rules."),
    "panels": [
        {"svg": P1, "alt": ("한 대표는 숙제를 앱으로 낸다 하고, 다른 대표는 아직 공책으로 낸다고 말함", "One rep says their class submits homework via an app; another says theirs still uses notebooks"),
         "caption": ("학교에 디지털 기기와 AI가 늘어나는데, 각 반이 제각각 규칙을 만들어요.", "Digital tools and AI are spreading through school, but each class makes its own rules."),
         "small": ("아직은 반마다 서로 다른 속도와 방식으로 디지털로 옮겨가고 있어요.", "Right now, each class is going digital at its own pace, in its own way.")},
        {"svg": P2, "alt": ("태블릿 없는 반의 학생이 소외감을 말하고, 학생회장은 전체가 정리되지 않는다고 땀 흘리며 말함", "A student says their class has no tablets; the sweating council president says nothing lines up school-wide"),
         "caption": ("전체를 아우르는 큰 방향이 없으면 격차·혼란이 생겨요.", "Without an overarching direction, gaps and confusion follow."),
         "small": ("큰 방향 없이 반마다 따로 만들면, 태블릿 없는 반처럼 뒤처지는 쪽이 생겨요.", "Without a shared direction, some classes — like the tablet-less one — fall behind.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 의사봉을 들고 디지털 전환·격차해소·데이터원칙이 담긴 기본 헌장을 발표하고, 대표가 옆에서 웃음", "The council president holds a gavel, announcing a charter covering digital transition, closing gaps, and data principles, while a rep smiles beside"),
         "caption": ("지능정보화 기본법은 학교 전체의 디지털·AI 생활을 아우르는 기본 헌장이에요.", "The framework act is the charter that covers the whole school's digital and AI life."),
         "small": ("이 법은 반마다 흩어진 디지털 규칙에 하나의 큰 방향을 줘요.", "This Act gives one big direction to every class's scattered digital rules."),
         "tricks": (4, [
             (PLAN_I, ("큰 방향 먼저 세우기", "Set the big direction first"), ("종합계획을 먼저 그려요", "draws the master plan first"), "calm"),
             (GAP_I, ("누구도 소외되지 않게", "Leave no one behind"), ("정보격차부터 줄여요", "closes the digital gap first"), "warm"),
             (SHIELD_I, ("데이터·AI를 안전하게 다루는 원칙", "Principles for handling data and AI safely"), ("정보를 지키고 기술을 안전하게 쓰는 시책을 세워요", "sets policies to protect information and use tech safely")),
             (ROOT_I, ("관련 법의 기본 방향 되기", "Set direction for related laws"), ("새 규칙은 이 원칙에 맞추려 애써요", "new rules try to fit these principles")),
         ])},
        {"svg": P4, "alt": ("기본 헌장 아래로 격차해소·데이터운영·AI활용 세 세부 규칙이 가지처럼 뻗어 나감", "Three detailed rules — gap-closing, data-handling, AI-use — branch down like limbs from the framework charter"),
         "caption": ("세부 규칙들은 기본 헌장이 정한 방향을 따라가요.", "Detailed rules follow the direction the framework charter sets."),
         "small": ("세부 규칙들은 따로 만들되 이 헌장의 방향에 맞추려 애써요.", "Detailed rules are made separately but try to fit this charter.")},
        {"svg": P5, "alt": ("왼쪽: 학생회장이 큰 방향이 정해졌다고 말함. 오른쪽: 대표가 태블릿 예산은 어디서 나오냐고 땀 흘리며 물음", "Left: the president says the big direction is set. Right: a sweating rep asks where the tablet budget comes from"),
         "caption": ("헌장만 있다고 학교의 디지털 전환이 저절로 되진 않아요.", "A charter alone doesn't make the school's digital shift happen."),
         "small": ("디지털 전환을 실제로 하려면 세부 규칙과 예산이 더 필요해요.", "Actually making the shift takes detailed rules and a budget too.")},
    ],
    "summary": (("<b>지능정보화 기본법</b> = 학교(국가) 전체의 <b>디지털·AI 전환 방향</b>을 세우고, <b>격차 해소와 안전 원칙</b>을 담아 관련 법들이 맞춰야 할 <b>기본 방향</b>을 정하는 헌장.",
                 "<b>The Framework Act on Intelligent Informatization</b> = the charter that sets the whole school's (nation's) <b>direction for going digital</b>, bakes in <b>gap-closing and safety principles</b>, and sets the <b>basic direction</b> related laws should fit."),
                ("지능정보화 기본법은 과거의 국가정보화 기본법을 대체한 법으로, 지능정보사회 종합계획 수립, 정보격차 해소, 정보보호의 기본 원칙을 정해요. 지능정보사회에 관한 다른 법을 만들거나 고칠 때는 이 법의 목적과 기본원칙에 맞도록 노력해야 해요(제5조). 다만 다른 법에 특별한 규정이 있으면 그 법을 따르고, 전자정부에 관한 사항은 전자정부법을 따라요. 이 법의 '지능정보기술'에는 학습·추론·판단을 구현하는 AI 같은 기술이 들어가요.",
                 "The Framework Act on Intelligent Informatization replaced the earlier National Informatization Basic Act. It establishes the master plan for an intelligent information society, principles for closing the digital divide, and baseline rules for information protection. When other laws on the intelligent information society are made or amended, they should try to fit this Act's purpose and principles (Article 5). Special provisions in other laws still take priority, and e-government matters follow the e-Government Act. The Act's \"intelligent information technology\" covers AI-style tech that implements learning, inference, and judgment.")),
    "glossary": [
        ("지능정보화기본법", "Framework Act on Intelligent Informatization", ("학교 전체 디지털 생활의 기본 헌장.", "The charter covering the whole school's digital life."), ("관련 법을 만들 때 맞춰야 할 기본 원칙을 정해요.", "Sets the basic principles related laws should fit.")),
        ("지능정보사회 종합계획", "Master Plan for an Intelligent Information Society", ("큰 방향을 미리 그려두는 계획.", "The plan that sketches the big direction in advance."), ("3년 단위로 다시 세워요(제6조).", "Redrawn every three years (Article 6).")),
        ("정보격차 해소", "Closing the Digital Divide", ("누구도 디지털에서 소외되지 않게 하는 일.", "Making sure no one is left behind digitally."), ("태블릿 없는 반을 먼저 챙기는 것과 같아요.", "Like looking after the tablet-less class first.")),
        ("정보보호 원칙", "Information Protection Principle", ("정보와 통신망을 안전하게 지키는 기본 약속.", "The baseline promise to keep information and networks safe."), ("구체적인 보안 의무는 정보통신망법 같은 별도 법에도 있어요.", "Specific security duties also sit in separate laws, like the Network Act.")),
        ("데이터기반행정", "Data-Based Administration", ("감이 아니라 데이터로 결정하는 것.", "Deciding by data, not by gut feel."), ("근거 법은 따로 있는 데이터기반행정법이에요.", "Its legal basis is a separate law, the Data-Based Administration Act.")),
        ("전자정부법", "e-Government Act", ("전자정부 서비스를 규율하는 별도 법.", "The separate law governing e-government services."), ('전자정부 수준을 재는 평가 지표는 → <a href="egdi-ko.html">다른 학교와 비교하는 평가단</a>', 'How e-government gets evaluated is covered → <a href="egdi-en.html">the board that compares schools</a>')),
        ("개인정보보호법", "Personal Information Protection Act", ("개인정보를 규율하는 별도 법.", "The separate law governing personal data."), ("정보보호 원칙과 맞닿지만 자체 규칙을 따로 갖고 있어요.", "It touches this act's protection principles but has its own rules.")),
        ("AI 기본법", "AI Basic Act", ("AI를 콕 집어 다루는 별도 법.", "A separate law aimed squarely at AI."), ("AI 산업 진흥과 신뢰 기반을 따로 다뤄요.", "Separately covers AI industry promotion and trust.")),
    ],
}
