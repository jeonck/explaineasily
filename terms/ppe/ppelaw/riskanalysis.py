"""위험·안전성 분석(FTA/FMEA/HAZOP)."""
from _draw import *
from _world import *

FTA_I = icon('<circle cx="32" cy="14" r="6" fill="var(--bad)"/><path d="M32 20 L18 36 M32 20 L46 36" stroke="var(--ink)" stroke-width="3"/><circle cx="18" cy="42" r="5" fill="var(--accent)"/><circle cx="46" cy="42" r="5" fill="var(--accent)"/><path d="M18 48 L10 56 M18 48 L26 56 M46 48 L38 56 M46 48 L54 56" stroke="var(--ink)" stroke-width="2.5"/>')
FMEA_I = icon('<rect x="8" y="16" width="16" height="16" rx="3" fill="var(--good)"/><rect x="24" y="16" width="16" height="16" rx="3" fill="var(--bad)"/><rect x="40" y="16" width="16" height="16" rx="3" fill="var(--good)"/><path d="M12 38 h40" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4 3"/><path d="M32 24 l16 20 M48 24 l-16 20" stroke="var(--bad)" stroke-width="2" opacity="0.6"/>')
HAZOP_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 34 h24 M20 44 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><circle cx="48" cy="18" r="8" fill="var(--accent)"/><path d="M48 14 v8 M48 24 h0" stroke="#fff" stroke-width="2.5"/>')
EARLY_I = icon('<path d="M32 10 a22 22 0 1 0 0.01 0z" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 7 l13 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# 1. 축제 준비 중 아찔한 사고가 날 뻔했어요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SWEAT + EYES, **STUDENT) + '<path d="M170 190 q30 -24 70 -4" stroke="#5B8DEF" stroke-width="5" fill="none"/>'
         + label(220, 250, "⟦전선에 걸려 넘어질 뻔했어요|almost tripped over the power cord⟧", 11, "var(--bad)")
         + person(560, 150, s=0.8, face=EYES, **TEACHER) + bubble(460, 70, 230, 44, "⟦왜 이런 일이 생겼는지 알아봐야겠어요|we need to find out why this happened⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦축제 준비 중 아찔한 사고가 날 뻔했어요|a near-accident happened while setting up the festival⟧", 13, "var(--ink)", cls="d"))

# 2. 그때그때 감으로 원인을 짚으면 틀려요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(200, 135, s=0.8, face=FROWN, **STUDENT) + label(200, 265, "⟦그냥 전선이 길어서 그래요|it's just because the cord was too long⟧", 11, "var(--bad)")
         + person(560, 135, s=0.8, face=FROWN, **REP) + label(560, 265, "⟦아뇨, 테이블 배치가 문제였어요|no, it was the table layout⟧", 11, "var(--bad)")
         + label(380, 300, "⟦체계 없이 짚으면 진짜 원인도, 다음 위험도 놓쳐요|guessing without a method misses the real cause — and the next risk⟧", 12, "var(--ink)", cls="d"))

# 3. 위험·안전성 분석 = 사고를 체계적으로 추적하는 세 가지 방법 (hero)
P3 = svg(360, sky(360)
         + label(380, 26, "⟦위험·안전성 분석 = 사고를 체계적으로 추적하는 세 가지 방법|risk/safety analysis = three systematic ways to trace an accident⟧", 13, "var(--ink)", cls="d")
         + person(130, 150, s=0.85, face=EYES, **TEACHER)
         + rulesboard(230, 60, 300, 260, "⟦세 가지 분석법|THREE METHODS⟧",
                      ("⟦FTA — 사고에서 거꾸로 원인 트리로|FTA — trace causes backward, as a tree⟧",
                       "⟦FMEA — 부품마다 \"고장나면?\" 점검|FMEA — check each part: \"what if it fails?\"⟧",
                       "⟦HAZOP — 정해진 질문어로 단계별 훑기|HAZOP — scan each step with guide words⟧",
                       "⟦셋 다: 사고 전에 미리 찾는 것|all three: finding it before it happens⟧"), 0.95)
         + person(640, 160, s=0.8, face=EYES, **REP)
         + label(380, 340, "⟦어디를 보느냐만 다를 뿐, 목적은 같아요 — 사고 전에 찾기|different angles, same goal — catch it before it happens⟧", 11, "var(--muted)"))

# 4. 언제 어떤 방법을 쓸까
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 30, 320, 260, "⟦FTA|결과에서 원인으로⟧",
                      ("⟦사고가 이미 일어났거나|an accident already happened,⟧", "⟦\"왜?\"를 되짚을 때|or you're asking \"why?\" backward⟧", "⟦원인들이 어떻게 겹치는지 봄|shows how causes combine⟧"), 1.0)
         + rulesboard(400, 30, 320, 260, "⟦FMEA / HAZOP|부품·단계에서 앞으로⟧",
                      ("⟦아직 안 일어난 고장을 미리 찾을 때|finding failures before they happen⟧", "⟦부품 하나하나(FMEA) 또는|part by part (FMEA), or⟧", "⟦공정 단계마다(HAZOP) 훑어봄|step by step in a process (HAZOP)⟧"), 1.0)
         + label(380, 305, "⟦사고 후엔 FTA로 거꾸로, 사고 전엔 FMEA·HAZOP으로 미리|after an accident, trace back with FTA — before one, scan ahead with FMEA/HAZOP⟧", 11, "var(--ink)", cls="d"))

# 5. 분석했다고 사고가 안 나는 건 아니에요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **TEACHER) + label(190, 260, "⟦찾아낸 위험은 미리 막을 수 있어요|found risks can be prevented in advance⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=SWEAT + EYES, **REP) + label(570, 260, "⟦근데 못 떠올린 위험은 여전히 남아요|but risks nobody thought of still remain⟧", 11, "var(--ink)")
         + label(380, 305, "⟦분석은 확률을 낮출 뿐, 안전을 보장하진 않아요|analysis lowers the odds — it doesn't guarantee safety⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "riskanalysis", "order": 13,
    "title": ("사고를 거꾸로, 또는 미리 훑어보기", "Tracing an Accident Backward — Or Scanning for It Ahead of Time"),
    "h1": ("<em>위험·안전성 분석(FTA/FMEA/HAZOP)</em>이 뭐예요?", "What is <em>Risk/Safety Analysis (FTA/FMEA/HAZOP)</em>?"),
    "sub": ("위험·안전성 분석을, 축제 준비 중 아찔한 사고를 학생회가 세 가지 방법으로 체계적으로 추적하는 이야기로 풀어봤어요.",
            "Risk and safety analysis, told as a story about the student council systematically tracing a near-accident at festival setup, using three methods."),
    "panels": [
        {"svg": P1, "alt": ("학생이 전선에 걸려 넘어질 뻔하고, 선생님이 왜 이런 일이 생겼는지 알아봐야겠다고 말함", "A student nearly trips over a power cord; a teacher says they need to find out why"),
         "caption": ("축제 준비 중 아찔한 사고가 날 뻔했어요.", "A near-accident happened while setting up the festival."),
         "small": ("다행히 다치지는 않았지만, 다음엔 진짜 사고가 날 수도 있어요.", "Nobody got hurt this time — but next time could be real.")},
        {"svg": P2, "alt": ("두 학생이 서로 다른 원인(전선 길이 vs 테이블 배치)을 짚으며 다툼", "Two students argue over different causes — the cord's length versus the table layout"),
         "caption": ("그때그때 감으로 원인을 짚으면 틀려요.", "Guessing at the cause on the spot gets it wrong."),
         "small": ("체계 없이 짚으면 진짜 원인도, 다음 위험도 놓쳐요.", "Guessing without a method misses the real cause — and the next risk.")},
        {"svg": P3, "hero": True, "alt": ("선생님과 대표가 FTA·FMEA·HAZOP 세 가지 분석법이 적힌 기준표를 사이에 두고 있음", "A teacher and a rep stand beside a board listing the three methods: FTA, FMEA, HAZOP"),
         "caption": ("위험·안전성 분석은 사고를 체계적으로 추적하는 세 가지 방법이에요.", "Risk/safety analysis is three systematic ways to trace an accident."),
         "small": ("어디를 보느냐만 다를 뿐, 목적은 같아요 — 사고 전에 찾기.", "Different angles, same goal — catch it before it happens."),
         "tricks": (4, [
             (FTA_I, ("FTA — 거꾸로 추적", "FTA — trace backward"), ("사고에서 원인 쪽으로 트리를 그려요", "draws a tree from the accident back to causes"), "warm"),
             (FMEA_I, ("FMEA — 부품별 점검", "FMEA — check each part"), ("\"이게 고장나면?\"을 하나씩 물어요", "asks \"what if this part fails?\" one by one")),
             (HAZOP_I, ("HAZOP — 단계별 훑기", "HAZOP — scan each step"), ("과다·과소·없음·반대 같은 질문어로", "with guide words like too much, too little, none, reverse")),
             (EARLY_I, ("사고 전에 찾기", "Catch it before it happens"), ("셋 다 같은 목적이에요", "all three share this one goal"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 기준표는 사고 후 원인을 되짚는 FTA, 오른쪽은 사고 전 부품·단계를 미리 훑는 FMEA·HAZOP을 비교함", "Left board: FTA traces causes after an accident. Right board: FMEA/HAZOP scan parts and steps before one"),
         "caption": ("언제 어떤 방법을 쓸지는 이렇게 갈려요.", "Here's how the choice of method splits."),
         "small": ("사고 후엔 FTA로 거꾸로, 사고 전엔 FMEA·HAZOP으로 미리.", "After an accident, trace back with FTA — before one, scan ahead with FMEA/HAZOP.")},
        {"svg": P5, "alt": ("왼쪽: 선생님이 찾아낸 위험은 미리 막을 수 있다고 말함. 오른쪽: 대표가 못 떠올린 위험은 여전히 남는다고 땀 흘리며 말함", "Left: the teacher says found risks can be prevented. Right: a sweating rep says unthought-of risks still remain"),
         "caption": ("분석했다고 사고가 안 나는 건 아니에요.", "Analysis doesn't mean an accident can never happen."),
         "small": ("분석은 확률을 낮출 뿐, 안전을 보장하진 않아요.", "Analysis lowers the odds — it doesn't guarantee safety.")},
    ],
    "summary": (("<b>위험·안전성 분석</b> = 사고를 <b>FTA(거꾸로 원인 추적)</b>, <b>FMEA(부품별 점검)</b>, <b>HAZOP(단계별 훑기)</b>으로 미리 찾아내는 세 가지 방법.",
                 "<b>Risk/safety analysis</b> = three methods for catching trouble early — <b>FTA</b> (tracing causes backward), <b>FMEA</b> (checking each part), and <b>HAZOP</b> (scanning each step with guide words)."),
                ("FTA(Fault Tree Analysis)는 이미 일어났거나 우려되는 사고(정상사상)를 꼭대기에 두고, 논리 게이트(AND/OR)로 하위 원인을 트리 형태로 분해해 근본 원인과 발생 확률을 추정해요. FMEA(Failure Mode and Effects Analysis)는 구성요소마다 가능한 고장 모드와 그 영향·심각도를 앞에서부터 훑어 위험 우선순위를 매겨요. HAZOP(Hazard and Operability Study)은 공정의 각 단계에 '과다·과소·없음·반대로·기타' 같은 가이드워드를 적용해 이탈 가능성을 체계적으로 찾아요. 셋 다 사고를 줄이기 위한 사전 예방 기법이지만, 분석자의 경험과 상상력의 한계를 완전히 벗어나진 못해요.",
                 "FTA (Fault Tree Analysis) places a top (undesired) event at the root and decomposes it into contributing causes through logic gates (AND/OR), estimating root causes and likelihood. FMEA (Failure Mode and Effects Analysis) walks through each component's possible failure modes and their severity, ranking risk priority. HAZOP (Hazard and Operability Study) applies guide words — too much, too little, none, reverse, other — to each step of a process to systematically find deviations. All three are preventive techniques, but none fully escape the limits of the analyst's own experience and imagination.")),
    "glossary": [
        ("FTA", "FTA (Fault Tree Analysis)", ("사고에서 거꾸로 원인을 따라가는 트리.", "A tree that traces backward from an accident to its causes."), ("논리 게이트로 원인들이 겹치는 방식을 보여줘요.", "Logic gates show how causes combine.")),
        ("FMEA", "FMEA (Failure Mode and Effects Analysis)", ("부품마다 \"고장나면?\"을 점검하는 표.", "A table checking \"what if this fails?\" for every part."), ("영향이 큰 고장부터 우선순위를 매겨요.", "Ranks failures by how severe their effect is.")),
        ("HAZOP", "HAZOP", ("과다·과소·없음 같은 질문어로 훑는 점검.", "A scan using guide words like too much, too little, none."), ("공정의 각 단계를 하나씩 짚어가요.", "Walks through a process one step at a time.")),
        ("위험성평가", "Risk Assessment", ("위험의 크기와 빈도를 가늠하는 일.", "Gauging how big and how often a risk is."), ("세 분석법 모두 이 평가를 돕는 도구예요.", "All three methods are tools that feed into this.")),
        ("근본원인분석", "Root Cause Analysis", ("겉으로 드러난 증상 말고 진짜 원인을 찾는 것.", "Finding the real cause, not just the visible symptom."), ("FTA가 대표적인 방법 중 하나예요.", "FTA is one of its representative methods.")),
        ("고장모드", "Failure Mode", ("한 부품이 망가지는 구체적인 방식.", "The specific way a single part can break."), ("FMEA에서 부품마다 하나씩 나열해요.", "FMEA lists these out, one per part.")),
        ("가이드워드", "Guide Word", ("HAZOP이 쓰는 정해진 질문 단어들.", "HAZOP's fixed set of prompting words."), ("빠뜨리지 않고 훑게 해주는 체크리스트 같은 거예요.", "Works like a checklist that keeps the scan from skipping anything.")),
        ("기능안전 표준", "Functional Safety Standard", ("이 분석들로 얻은 등급을 공식 표준이 요구해요.", "An official standard requires the grades these analyses produce."), ('분석 결과가 등급(SIL/ASIL)으로 이어지는 표준이 따로 있어요. → <a href="funcsafetystd-ko.html">안전 등급을 매기는 공통 규칙서</a>', 'A separate standard turns this analysis into a safety grade. → <a href="funcsafetystd-en.html">the shared rulebook that grades safety</a>')),
    ],
}
