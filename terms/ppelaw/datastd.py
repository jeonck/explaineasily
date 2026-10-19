"""데이터 표준화."""
from _draw import *
from _world import *

TERM_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
DOMAIN_I = icon('<rect x="10" y="26" width="44" height="12" rx="6" fill="var(--accent)"/><circle cx="18" cy="32" r="7" fill="#FFF8E7"/><circle cx="46" cy="32" r="7" fill="#FFF8E7"/>')
CODE_I = icon('<rect x="10" y="18" width="4" height="28" fill="#142033"/><rect x="18" y="18" width="8" height="28" fill="#142033"/><rect x="30" y="18" width="4" height="28" fill="#142033"/><rect x="38" y="18" width="10" height="28" fill="#142033"/>')
NAME_I = icon('<path d="M10 22 h36 l8 10 l-8 10 h-36z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="44" cy="32" r="3" fill="#C9A86A"/>')

# 1. 반마다 출석부 적는 방식이 달라요
P1 = svg(300, sky(300)
         + person(170, 150, s=0.85, face=EYES, **REP) + bubble(90, 70, 200, 40, "⟦우리 반은 O/X로 적어요|our class marks it O/X⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=SMILE, **REP) + bubble(460, 70, 220, 40, "⟦저흰 1/0 숫자로 적는데요|we use numbers, 1 or 0⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦반마다 출석부 적는 방식이 달라요|every class marks attendance a different way⟧", 13, "var(--ink)", cls="d"))

# 2. 합치려니 숫자가 안 맞아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT + EYES, **PRESIDENT) + bubble(130, 70, 240, 44, "⟦반마다 다르게 적어서 합계가 안 맞아요|each class marks it differently — the totals don't add up⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(590, 150, s=0.75, face=FROWN, **REP) + label(590, 250, "⟦저희 반이 2반보다 훨씬 많아 보이는데요?|our class looks way bigger than class 2's?⟧", 11, "var(--bad)")
         + label(380, 285, "⟦형식이 다르면 숫자를 믿고 합칠 수 없어요|different formats mean the combined numbers can't be trusted⟧", 12, "var(--ink)", cls="d"))

# 3. 데이터 표준화 = 전교 공통 기준표 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦데이터 표준화 = 전교가 함께 쓰는 공통 용어·형식·코드표|data standardization = a shared glossary, format, and code table the whole school uses⟧", 13, "var(--ink)", cls="d")
         + person(170, 130, s=0.9, face=EYES, **PRESIDENT)
         + rulesboard(260, 70, 300, 220, "⟦전교 공통 기준표|SCHOOL-WIDE STANDARD⟧",
                      ("⟦출석 = 1(했음)/0(안했음)|attendance = 1(present)/0(absent)⟧",
                       "⟦이름 순서 = 성-이름|name order = family name-given name⟧",
                       "⟦반 코드 = 학년+반 (예: 2-3)|class code = grade+class (e.g. 2-3)⟧",
                       "⟦날짜 형식 = YYYY-MM-DD|date format = YYYY-MM-DD⟧"), 0.95)
         + person(640, 160, s=0.8, face=SMILE, **REP)
         + label(380, 320, "⟦같은 말, 같은 형식, 같은 코드를 쓰면 전교 숫자를 믿고 합칠 수 있어요|same words, same format, same codes — then the whole school's numbers can be trusted and combined⟧", 12, "var(--muted)"))

# 4. 표준화 전후 비교
P4 = svg(300, sky(300, ground=False)
         + rulesboard(60, 30, 640, 240, "⟦표준화 전 → 후|BEFORE → AFTER STANDARDIZING⟧",
                      ("⟦1반 O/X, 2반 1/0, 3반 출석/결석 — 합산 불가|class1 O/X, class2 1/0, class3 present/absent — can't be summed⟧",
                       "⟦→ 모두 \"1=출석, 0=결석\"으로 통일|→ unified to \"1=present, 0=absent\" everywhere⟧",
                       "⟦이제 전교 출석률을 그냥 더해서 계산해요|now the school-wide rate is just added up⟧",
                       "⟦코드 하나 안 맞으면 자동 검사기가 바로 잡아내요|one mismatched code, and the automatic checker flags it right away⟧"), 1.0, hl=2)
         + label(380, 288, "⟦숫자가 아니라 '약속'을 맞추는 일이에요|it's not the numbers that change — it's the agreement behind them⟧", 12, "var(--ink)", cls="d"))

# 5. 표준도 계속 고쳐 나가야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 140, s=0.8, face=FROWN, **REP) + label(190, 240, "⟦새 동아리 코드가 아직 기준표에 없어요|the new club's code isn't in the standard yet⟧", 11, "var(--ink)")
         + person(570, 130, s=0.85, face=SMILE, **PRESIDENT) + checkmachine(570, 210, 0.8)
         + label(570, 260, "⟦기준표는 계속 고쳐 나가야 해요|the standard has to keep being updated⟧", 11, "var(--ink)")
         + label(380, 285, "⟦표준은 한 번 정하고 끝이 아니라, 새 상황마다 다시 다듬어야 해요|a standard isn't set once and done — every new situation means refining it again⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "datastd", "order": 12,
    "title": ("전교가 함께 쓰는 공통 기준표", "The Shared Standard the Whole School Uses"),
    "h1": ("<em>데이터 표준화</em>가 뭐예요?", "What is <em>Data Standardization</em>?"),
    "sub": ("데이터 표준화를, 반마다 다르게 적던 출석부를 전교 공통 기준표 하나로 맞추는 학생회 이야기로 풀어봤어요.",
            "Data standardization, told as a story about the student council unifying every class's own attendance format into one shared, school-wide standard."),
    "panels": [
        {"svg": P1, "alt": ("두 반 대표가 출석을 각각 O/X와 1/0으로 다르게 적는다고 말함", "Two class reps describe marking attendance differently — one with O/X, the other with 1/0"),
         "caption": ("반마다 출석부 적는 방식이 달라요.", "Every class marks attendance a different way."),
         "small": ("처음엔 각자 편한 대로 적었을 뿐이에요.", "At first, everyone just wrote it however was convenient.")},
        {"svg": P2, "alt": ("학생회장이 반마다 다른 기록 때문에 합계가 안 맞는다고 땀을 흘리며 말하고, 대표는 숫자가 이상하다고 함", "The council president sweats, saying the totals don't add up because each class records differently; a rep says the numbers look off"),
         "caption": ("합치려니 숫자가 안 맞아요.", "Trying to combine them, the numbers don't add up."),
         "small": ("형식이 다르면 숫자를 믿고 합칠 수 없어요.", "Different formats mean the combined numbers can't be trusted.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 전교 공통 기준표를 들고, 대표가 옆에서 웃으며 지켜봄", "The council president holds up a school-wide standard table while a rep smiles alongside"),
         "caption": ("데이터 표준화는 전교가 함께 쓰는 공통 용어·형식·코드표예요.", "Data standardization is a shared glossary, format, and code table the whole school uses."),
         "small": ("같은 말, 같은 형식, 같은 코드를 쓰면 전교 숫자를 믿고 합칠 수 있어요.", "Same words, same format, same codes — then the whole school's numbers can be trusted and combined."),
         "tricks": (4, [
             (TERM_I, ("표준 용어 정하기", "Set standard terms"), ("같은 뜻은 같은 이름으로", "same meaning, same name"), "calm"),
             (DOMAIN_I, ("표준 형식·범위 정하기", "Set standard format/range"), ("올 수 있는 값의 틀을 정해요", "fixes the shape values must take")),
             (CODE_I, ("코드로 통일하기", "Unify with codes"), ("같은 값은 같은 코드로", "same value, same code"), "warm"),
             (NAME_I, ("이름 짓는 규칙 정하기", "Set naming rules"), ("코드·변수 이름도 규칙대로", "even code names follow one rule")),
         ])},
        {"svg": P4, "alt": ("표준화 전 세 반의 서로 다른 기록 방식이, 표준화 후 하나의 코드로 통일되어 자동 검사기가 어긋남을 잡아냄", "Before, three classes record differently; after standardizing, one unified code lets the automatic checker catch mismatches"),
         "caption": ("표준화 전후를 비교하면 이렇게 돼요.", "Here's what changes before and after standardizing."),
         "small": ("숫자가 아니라 '약속'을 맞추는 일이에요.", "It's not the numbers that change — it's the agreement behind them.")},
        {"svg": P5, "alt": ("왼쪽: 새 동아리 코드가 기준표에 없어 곤란한 대표. 오른쪽: 학생회장이 자동 검사기로 기준표를 계속 고쳐 나감", "Left: a rep stuck because the new club's code isn't in the standard. Right: the president keeps refining the standard with an automatic checker"),
         "caption": ("표준도 계속 고쳐 나가야 해요.", "Even a standard has to keep being refined."),
         "small": ("새 상황마다 기준표를 다시 다듬어야 해요.", "Every new situation means refining the standard again.")},
    ],
    "summary": (("<b>데이터 표준화</b> = 여러 반(시스템)이 <b>같은 용어·형식·코드</b>를 쓰게 맞춰, 숫자를 <b>믿고 합칠 수 있게</b> 하는 일.",
                 "<b>Data standardization</b> = getting many classes (systems) to use the <b>same terms, format, and codes</b>, so the numbers can be <b>trusted and combined</b>."),
                ("데이터 표준화는 여러 시스템이 같은 의미의 데이터를 같은 용어(표준용어)·같은 형식과 범위(표준도메인)·같은 코드값(코드표준)·같은 명명규칙으로 다루게 맞추는 작업이에요. 기관 간 데이터를 연계·통합할 때 표준이 없으면 같은 값도 다르게 해석되어 통계와 연계가 무너져요. 표준은 데이터 사전에 모아 공개하고, 새로운 상황이 생길 때마다 계속 보완해야 해요.",
                 "Data standardization aligns how multiple systems represent the same meaning — standard terminology, standard domain (format/range), standard codes, and naming conventions. Without it, linking or integrating data across organizations breaks down, because the same value gets interpreted differently. Standards are published in a data dictionary and must keep being revised as new situations arise.")),
    "glossary": [
        ("데이터표준화", "Data Standardization", ("전교가 같은 말·형식·코드를 쓰게 맞추는 일.", "Getting the whole school to use the same words, format, and codes."), ("숫자를 믿고 합칠 수 있게 해줘요.", "Lets the combined numbers be trusted.")),
        ("표준용어", "Standard Terminology", ("같은 뜻은 같은 이름으로 부르는 것.", "Calling the same meaning by the same name."), ("반마다 다른 이름을 쓰면 헷갈려요.", "Different names per class cause confusion.")),
        ("표준도메인", "Standard Domain", ("값이 올 수 있는 형식·범위를 정하는 것.", "Fixing the format and range a value can take."), ("날짜 형식을 YYYY-MM-DD로 맞추는 것 같은 일이에요.", "Like agreeing dates are always YYYY-MM-DD.")),
        ("코드표준", "Code Standard", ("같은 값은 같은 코드로 적는 것.", "Writing the same value with the same code."), ("1=출석처럼 숫자 코드로 통일해요.", "Unifies it to a numeric code, like 1 = present.")),
        ("명명규칙", "Naming Convention", ("이름을 짓는 공통 방식.", "A shared way of naming things."), ("코드명·변수명도 이 규칙을 따라요.", "Code and variable names follow this rule too.")),
        ("데이터 사전", "Data Dictionary", ("전교 기준표를 한 곳에 모아둔 목록.", "The list collecting the whole school's standard in one place."), ("누구나 찾아볼 수 있게 공개해요.", "Published so anyone can look it up.")),
        ("데이터 품질", "Data Quality", ("표준을 지켜야 믿을 수 있는 숫자가 나와요.", "Only data that follows the standard can be trusted."), ('소프트웨어의 \'좋음\' 기준과 닮았어요. → <a href="iso25000-ko.html">좋은 준비물의 기준표</a>', 'It echoes software\'s own standard for "good." → <a href="iso25000-en.html">the standard for good supplies</a>')),
        ("공공데이터 개방", "Open Data", ("표준을 지킨 데이터라야 바깥에도 공개할 수 있어요.", "Only standardized data is fit to open up to the outside."), ('다른 세계에도 비슷한 창고가 있어요. → <a href="lodopendata-ko.html">문을 열고 번호표를 달아 연결해두는 창고</a>', 'A similar warehouse exists in another world. → <a href="lodopendata-en.html">the warehouse that opens its door and links its tags</a>')),
    ],
}
