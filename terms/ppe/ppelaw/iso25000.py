"""ISO/IEC 25000 시리즈(SQuaRE)."""
from _draw import *
from _world import *

MODEL_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="24" cy="24" r="5" fill="var(--accent)"/><circle cx="40" cy="24" r="5" fill="var(--good)"/><circle cx="24" cy="40" r="5" fill="var(--bad)"/><circle cx="40" cy="40" r="5" fill="var(--accent)"/>')
NEED_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 26 h20 M22 34 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M38 38 l5 5 l8 -10" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
RULER_I = icon('<rect x="12" y="26" width="40" height="12" rx="2" fill="var(--accent)"/><path d="M20 26 v12 M28 26 v8 M36 26 v12 M44 26 v8" stroke="#FFF" stroke-width="2"/>')
JUDGE_I = icon('<circle cx="32" cy="32" r="22" fill="var(--good)"/><path d="M22 32 l7 7 l13 -16" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. "괜찮다"의 기준이 사람마다 달라요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SMILE, **STUDENT) + bubble(140, 70, 210, 40, "⟦빠르면 좋은 앱이죠!|fast means a good app!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **REP) + bubble(460, 70, 230, 40, "⟦저는 예쁘면 좋은 앱 같은데요|I think pretty means a good app⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦'좋은 소프트웨어'의 기준이 사람마다 달라요|everyone's standard for a \"good app\" is different⟧", 13, "var(--ink)", cls="d"))

# 2. 기준이 없으면 같은 앱도 다르게 평가해 다퉈요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(230, 135, s=0.8, face=SMILE, **STUDENT) + label(230, 265, "⟦이 앱 완전 좋아요!|this app is totally great!⟧", 11, "var(--good)")
         + person(540, 135, s=0.8, face=FROWN, **REP) + label(540, 265, "⟦아뇨, 이거 별로예요|no, this one's not good⟧", 11, "var(--bad)")
         + label(380, 300, "⟦같은 앱을 보고도 기준이 달라 결론이 갈려요|looking at the same app, different standards give different verdicts⟧", 12, "var(--ink)", cls="d"))

# 3. ISO/IEC 25000 = 학생회가 정한 공통 품질 기준표 (hero)
P3 = svg(360, sky(360)
         + rulesboard(230, 40, 300, 280, "⟦좋은 소프트웨어 기준표(SQuaRE)|WHAT MAKES GOOD SOFTWARE (SQuaRE)⟧",
                      ("⟦기능적합성 — 할 일을 제대로|functional suitability — does the job right⟧",
                       "⟦성능효율성 — 빠르기|performance efficiency — fast enough⟧",
                       "⟦사용성 — 쓰기 쉽기|usability — easy to use⟧",
                       "⟦신뢰성 — 안 멈추기|reliability — doesn't crash⟧",
                       "⟦보안성 — 안전하기|security — stays safe⟧",
                       "⟦유지보수성 — 고치기 쉽기|maintainability — easy to fix⟧",
                       "⟦이식성 — 옮기기 쉽기|portability — easy to move⟧",
                       "⟦호환성 — 다른 것과 잘 맞기|compatibility — plays well with others⟧"), 0.95)
         + person(90, 160, s=0.8, face=EYES, **PRESIDENT) + person(670, 160, s=0.75, face=SMILE, **REP)
         + label(380, 25, "⟦ISO/IEC 25000(SQuaRE) = 모두가 같이 쓰는 '좋은 소프트웨어' 기준표|ISO/IEC 25000 (SQuaRE) = the shared checklist for what makes software \"good\"⟧", 12, "var(--ink)", cls="d")
         + label(380, 340, "⟦기준이 같으면, 평가도 같은 말로 할 수 있어요|the same standard lets everyone judge in the same language⟧", 11, "var(--muted)"))

# 4. SQuaRE 시리즈의 네 영역
P4 = svg(320, sky(320, ground=False)
         + rulesboard(60, 40, 640, 230, "⟦SQuaRE 시리즈 네 영역|THE FOUR PARTS OF SQuaRE⟧",
                      ("⟦2501n 품질모델 — 무엇을 잴지 정의|2501n Quality Model — defines what to measure⟧",
                       "⟦2502n 품질측정 — 숫자로 재는 법|2502n Quality Measurement — how to measure it in numbers⟧",
                       "⟦2503n 품질요구사항 — 미리 요구 수준 적기|2503n Quality Requirements — writing the target level in advance⟧",
                       "⟦2504n 품질평가 — 요구 수준과 비교해 판정|2504n Quality Evaluation — judging it against the target⟧"), 1.0)
         + label(380, 295, "⟦정의 → 측정 → 요구 → 평가, 네 단계가 이어져요|define → measure → require → evaluate, in one chain⟧", 12, "var(--ink)", cls="d"))

# 5. 기준표가 있어도 전부 100점은 어려워요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **REP) + label(190, 260, "⟦기준은 같이 봐요|we judge by the same standard⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=SWEAT + EYES, **STUDENT) + label(570, 260, "⟦근데 다 100점은 시간도 돈도 모자라요|but acing every one takes more time and money than we have⟧", 11, "var(--ink)")
         + label(380, 305, "⟦빠른 대신 조금 덜 예쁠 수도 있어요 — 우선순위를 정해야 해요|faster might mean a little less polished — priorities have to be set⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "iso25000", "order": 4,
    "title": ("좋은 준비물의 기준표", "The Standard for Good Supplies"),
    "h1": ("<em>ISO/IEC 25000(SQuaRE)</em>이 뭐예요?", "What is <em>ISO/IEC 25000 (SQuaRE)</em>?"),
    "sub": ("ISO/IEC 25000 시리즈(SQuaRE)를, 학생회가 정한 '좋은 소프트웨어' 공통 기준표 이야기로 풀어봤어요.",
            "The ISO/IEC 25000 series (SQuaRE), told as a story about the student council's shared checklist for what makes software good."),
    "panels": [
        {"svg": P1, "alt": ("한 학생은 빠르면 좋은 앱이라 하고, 다른 학생은 예쁘면 좋은 앱이라고 함", "One student says fast means good; another says pretty means good"),
         "caption": ("'좋은 소프트웨어'의 기준이 사람마다 달라요.", "Everyone's standard for a \"good app\" is different."),
         "small": ("기준이 없으면 같은 질문에도 다른 답이 나와요.", "Without a standard, the same question gets different answers.")},
        {"svg": P2, "alt": ("한 학생은 같은 앱을 완전 좋다고 하고, 다른 학생은 별로라고 함", "One student calls the same app great; another calls it bad"),
         "caption": ("기준이 없으면 같은 앱도 다르게 평가해 다퉈요.", "Without a standard, the same app gets judged differently and people argue."),
         "small": ("같은 앱을 보고도 기준이 달라 결론이 갈려요.", "Looking at the same app, different standards give different verdicts.")},
        {"svg": P3, "hero": True, "alt": ("학생회장과 대표가 좋은 소프트웨어의 여덟 가지 공통 기준표를 들고 있음", "The council president and a rep hold up eight shared criteria for good software"),
         "caption": ("ISO/IEC 25000(SQuaRE)은 모두가 같이 쓰는 '좋은 소프트웨어' 기준표예요.", "ISO/IEC 25000 (SQuaRE) is the shared checklist for what makes software good."),
         "small": ("기준이 같으면, 평가도 같은 말로 할 수 있어요.", "The same standard lets everyone judge in the same language."),
         "tricks": (4, [
             (MODEL_I, ("품질 특성 정의하기", "Define quality traits"), ("기능·성능·보안 등 8가지", "function, performance, security, and more"), "calm"),
             (NEED_I, ("목표 수준 적어두기", "Write the target level"), ("얼마나 좋아야 하는지 미리", "how good it must be, set in advance")),
             (RULER_I, ("숫자로 측정하기", "Measure it in numbers"), ("느낌이 아니라 수치로", "numbers, not just a feeling"), "warm"),
             (JUDGE_I, ("목표와 비교해 평가하기", "Evaluate against the target"), ("기준과 맞춰서 판정해요", "judged against the standard")),
         ])},
        {"svg": P4, "alt": ("SQuaRE 시리즈를 품질모델·품질측정·품질요구사항·품질평가 네 영역으로 나눈 기준표", "A chart splitting SQuaRE into quality model, measurement, requirements, and evaluation"),
         "caption": ("SQuaRE 시리즈는 네 영역으로 이어져요.", "The SQuaRE series chains together in four parts."),
         "small": ("정의 → 측정 → 요구 → 평가, 네 단계가 이어져요.", "Define → measure → require → evaluate, in one chain.")},
        {"svg": P5, "alt": ("왼쪽: 같은 기준으로 평가하는 대표. 오른쪽: 모든 항목에서 100점을 맞추려다 땀 흘리는 학생", "Left: a rep judging by the shared standard. Right: a student sweating trying to ace every category"),
         "caption": ("기준표가 있어도 전부 100점은 어려워요.", "Even with a checklist, acing everything is hard."),
         "small": ("빠른 대신 조금 덜 예쁠 수도 있어요 — 우선순위를 정해야 해요.", "Faster might mean a little less polished — priorities have to be set.")},
    ],
    "summary": (("<b>ISO/IEC 25000(SQuaRE)</b> = '좋은 소프트웨어'란 무엇인지 <b>8가지 품질 특성으로 정의</b>하고, <b>재고 요구하고 평가</b>하는 공통 기준표.",
                 "<b>ISO/IEC 25000 (SQuaRE)</b> = a shared checklist that <b>defines \"good software\" with 8 quality characteristics</b>, then <b>measures, requires, and evaluates</b> it."),
                ("ISO/IEC 25000 시리즈(SQuaRE, Systems and Software Quality Requirements and Evaluation)는 소프트웨어 품질을 정의·측정·요구·평가하는 국제표준 모음이에요. 2501n(품질모델)이 기능적합성·성능효율성·호환성·사용성·신뢰성·보안성·유지보수성·이식성 8가지 특성을 정의하고, 2502n(측정)·2503n(요구사항)·2504n(평가)이 이를 수치화하고 비교·판정하는 절차를 제공해요.",
                 "The ISO/IEC 25000 series (SQuaRE — Systems and Software Quality Requirements and Evaluation) is a family of international standards that define, measure, require, and evaluate software quality. The 2501n quality model defines eight characteristics — functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability — while 2502n (measurement), 2503n (requirements), and 2504n (evaluation) provide the process to quantify, compare, and judge them.")),
    "glossary": [
        ("SQuaRE", "SQuaRE", ("좋은 소프트웨어의 기준 시리즈.", "The standard series for good software."), ("ISO/IEC 25000번대 표준을 통틀어 부르는 이름이에요.", "The umbrella name for the ISO/IEC 25000-series standards.")),
        ("품질모델(ISO 25010)", "Quality Model (ISO 25010)", ("8가지 품질 특성을 정의한 목록.", "The list defining the eight quality characteristics."), ("기능·성능·사용성 등을 하나하나 정의해요.", "Defines function, performance, usability, and the rest, one by one.")),
        ("품질 측정(ISO 2502n)", "Quality Measurement (ISO 2502n)", ("특성을 숫자로 재는 방법.", "How to measure each trait in numbers."), ("느낌이 아니라 측정 가능한 지표를 써요.", "Uses measurable indicators, not just a feeling.")),
        ("품질 요구사항(ISO 2503n)", "Quality Requirements (ISO 2503n)", ("미리 적어두는 목표 수준.", "The target level written down in advance."), ("평가의 기준선이 돼요.", "Becomes the baseline for evaluation.")),
        ("품질 평가(ISO 2504n)", "Quality Evaluation (ISO 2504n)", ("목표와 실제를 비교해 판정하는 절차.", "The process of comparing target against actual and judging."), ("기준에 못 미치면 다시 고쳐야 해요.", "Falling short means it has to be fixed again.")),
        ("사용성", "Usability", ("쓰기 쉬운 정도.", "How easy something is to use."), ("8가지 품질 특성 중 하나예요.", "One of the eight quality characteristics.")),
        ("유지보수성", "Maintainability", ("나중에 고치기 쉬운 정도.", "How easy it is to fix later."), ("오래 쓸 소프트웨어일수록 중요해요.", "Matters more the longer software stays in use.")),
        ("소프트웨어 테스트", "Software Testing", ("실제로 돌려보며 확인하는 것.", "Actually running it to check."), ('SQuaRE가 정한 기준을 실제로 확인하는 과정이에요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'The process that actually checks SQuaRE\'s standard. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
