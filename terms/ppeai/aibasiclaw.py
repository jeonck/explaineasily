from _draw import *
from _world import *

# 1. 검사장마다 제멋대로 기준을 정하던 시절
P1 = svg(320, sky(320)
         + person(140, 130, s=0.7, face=EYES, **OPERATOR) + label(140, 250, "⟦우리 검사장 맘대로예요|our station does it our own way⟧", 10, "var(--muted)")
         + person(380, 130, s=0.7, face=SMILE, **OPERATOR) + label(380, 250, "⟦우리도 우리 맘대로요|so do we, our own way⟧", 10, "var(--muted)")
         + person(620, 130, s=0.7, face=FROWN, **OPERATOR) + label(620, 250, "⟦우리도 역시나 맘대로요|us too, our own way⟧", 10, "var(--muted)")
         + label(380, 25, "⟦검사장마다 제멋대로 기준을 정하던 시절이 있었어요|there was a time when every station just made up its own rules⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦손님은 어느 검사장이 안전한지 알 길이 없었어요|customers had no way to know which station was actually safe⟧", 12, "var(--bad)", cls="d"))

# 2. 왜 어려운가: 법이 없던 틈에는, 사고가 나도 책임을 묻기 어려웠어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.8, face=EYES, **FARMER) + bubble(100, 70, 230, 50, "⟦제가 손해 봤는데, 누구 책임이죠?|I took the loss — whose fault is it, exactly?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 130, s=0.8, face=SWEAT + EYES, **OPERATOR)
         + label(600, 262, "⟦법이 없으니, 저도 할 말이 없어요|with no law to point to, I've got no answer either⟧", 11, "var(--muted)")
         + label(380, 300, "⟦법이 없던 틈에는, 사고가 나도 누구 책임인지 묻기 어려웠어요|without a law to lean on, pinning down responsibility after an accident was hard⟧", 12, "var(--ink)", cls="d"))

# 3. 인공지능기본법 = 모든 검사장이 지켜야 할 법적 최저선, 고영향 AI는 의무가 더 무거워요 (hero)
P3 = svg(360, sky(360)
         + gradeboard(170, 45, 420, 160, "⟦인공지능기본법 — 전 검사장 공통 최저선|AI BASIC ACT — THE FLOOR EVERY STATION MUST CLEAR⟧",
                 ("⟦모든 검사장에 적용되는 기본 의무|basic duties applying to every station⟧",
                  "⟦생명·안전·기본권에 큰 영향 = 고영향 AI|life, safety, rights at stake = high-impact AI⟧",
                  "⟦고영향 AI는 추가 의무를 더 짊어져요|high-impact AI carries extra duties on top⟧"), 1.0)
         + person(90, 230, s=0.7, face=SMILE, **INSPECTOR)
         + person(660, 230, s=0.6, face=EYES, **OPERATOR)
         + label(380, 22, "⟦인공지능기본법 = 모든 검사장이 지켜야 할 법적 최저선이에요|the AI Basic Act is the legal floor every station has to clear⟧", 13, "var(--ink)", cls="d")
         + label(380, 330, "⟦생명·안전·기본권에 크게 영향을 주면, 고영향 AI로 더 무거운 의무를 져요|when life, safety, or basic rights are heavily at stake, it's high-impact AI — and the duties get heavier⟧", 12, "var(--muted)"))

NOTICE_I = icon('<rect x="10" y="14" width="44" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M32 24 v10 M32 40 v2" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
ASSESS_I = icon('<path d="M14 50 L14 30 L26 30 L26 50 M30 50 V18 L42 18 V50 M46 50 V38 L58 38 V50" fill="var(--accent)"/>')
SAFE_I = icon('<path d="M32 8 L54 18 V32 C54 44 44 54 32 58 C20 54 10 44 10 32 V18 Z" fill="var(--good)"/>')
HUMAN_I = icon('<circle cx="32" cy="20" r="10" fill="var(--accent)"/><path d="M16 54 q16 -20 32 0" fill="none" stroke="var(--accent)" stroke-width="5"/>')

PAGE = {
    "slug": "aibasiclaw", "order": 10,
    "title": ("나라가 정한 최소 등급 기준", "The Minimum Grading Rule the Country Itself Sets"),
    "h1": ("<em>인공지능기본법·고영향 AI</em>가 뭐예요?", "What is the <em>AI Basic Act and High-Impact AI</em>?"),
    "sub": ("인공지능기본법을, 모든 검사장이 공통으로 지켜야 할 법적 최저선과 더 무거운 의무를 지는 고영향 AI 이야기로 풀어봤어요.",
            "Korea's AI Basic Act, told as a story about a legal floor every inspection station must clear — and the heavier duties high-impact AI carries on top."),
    "panels": [
        {"svg": P1, "alt": ("세 검사장이 저마다 자기 멋대로 기준을 정하고, 손님은 어느 곳이 안전한지 알 길이 없음", "Three stations each make up their own rules, leaving customers with no way to know which one is safe"),
         "caption": ("검사장마다 제멋대로 기준을 정하던 시절이 있었어요.", "There was a time when every station just made up its own rules."),
         "small": ("손님은 어느 검사장이 안전한지 알 길이 없었어요.", "Customers had no way to know which station was actually safe.")},
        {"svg": P2, "alt": ("농부가 누구 책임인지 묻지만, 조작원도 기댈 법이 없어 할 말이 없음", "A farmer asks whose fault it is, but the operator has no law to point to and no answer either"),
         "caption": ("법이 없던 틈에는, 책임을 묻기 어려웠어요.", "Without a law to lean on, pinning down responsibility was hard."),
         "small": ("사고가 나도, 누구 탓인지 가릴 공통 기준이 없었어요.", "Even after an accident, there was no shared standard for deciding whose fault it was.")},
        {"svg": P3, "hero": True, "alt": ("인공지능기본법이라는 큰 등급판이 모든 검사장 위에 걸려 있고, 고영향 AI는 추가 의무를 더 진다고 적혀 있음", "A large AI Basic Act charter hangs above every station, noting that high-impact AI carries extra duties on top"),
         "caption": ("모든 검사장이 지켜야 할 법적 최저선이에요.", "The legal floor every station has to clear."),
         "small": ("생명·안전·기본권에 크게 영향을 주면, 고영향 AI로 분류돼 의무가 더 무거워져요.", "When life, safety, or basic rights are heavily at stake, it's classified as high-impact AI — with heavier duties."),
         "tricks": (4, [
             (NOTICE_I, ("사전 고지하기", "Give advance notice"), ("이건 AI가 판정해요, 라고 먼저 알려요", "telling people up front that AI is making the call"), "calm"),
             (ASSESS_I, ("위험평가 하기", "Run a risk assessment"), ("고영향 AI는 이게 의무예요", "mandatory for high-impact AI")),
             (SAFE_I, ("안전성 확보조치 하기", "Put safety measures in place"), ("사고를 막을 장치를 실제로 둬요", "actually putting safeguards in place"), "warm"),
             (HUMAN_I, ("사람 개입 보장하기", "Guarantee human intervention"), ("기계 혼자 끝내지 않게 해요", "making sure a machine never finishes the call alone")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦일반 AI vs 고영향 AI|ORDINARY AI vs HIGH-IMPACT AI⟧",
                 ("⟦일반 AI — 기본 의무(투명성·기록 보관)만 지면 됨|ordinary AI — only the basic duties (transparency, record-keeping)⟧",
                  "⟦고영향 AI — 생명·안전·기본권에 큰 영향을 주는 경우|high-impact AI — when life, safety, or basic rights are heavily at stake⟧",
                  "⟦고영향 AI — 위험평가·안전조치·사람 개입까지 추가 의무|high-impact AI — risk assessment, safety measures, human oversight, on top⟧",
                  "⟦예 — 의료·채용·신용평가·사법 판단을 돕는 AI|e.g. AI assisting medical, hiring, credit, or judicial decisions⟧"), 1.0)),
         "alt": ("일반 AI와 고영향 AI의 의무 차이를 적은 표", "A board laying out the difference in duties between ordinary AI and high-impact AI"),
         "caption": ("모든 AI가 같은 무게의 의무를 지는 건 아니에요.", "Not every AI carries the same weight of duty."),
         "small": ("영향이 클수록, 법이 요구하는 안전장치도 늘어나요.", "The bigger the stakes, the more safeguards the law demands.")},
        {"svg": svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
                 + person(190, 130, s=0.8, face=SMILE, **INSPECTOR) + label(190, 260, "⟦법은 최저선을 그어줘요|the law draws the floor⟧", 11, "var(--ink)")
                 + person(570, 130, s=0.8, face=EYES, **TEACHER) + label(570, 260, "⟦그 위를 채우는 건 각 검사장 몫이에요|filling in above that is each station's own job⟧", 11, "var(--ink)")
                 + label(380, 300, "⟦법은 최저선일 뿐이에요 — 실제 안전은 윤리기준·리스크 관리가 채워야 해요|the law is only the floor — real safety still comes from ethics standards and risk management⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 검수반장이 법은 최저선을 긋는다고 말함. 오른쪽: 교사가 그 위는 각 검사장 몫이라고 말함", "Left: the inspector says the law draws the floor. Right: the teacher says filling in above it is each station's own job"),
         "caption": ("법을 지킨다고 저절로 안전해지진 않아요.", "Obeying the law doesn't automatically make things safe."),
         "small": ("법 위의 등급 원칙과 운영 지도는 각 검사장이 스스로 채워야 해요.", "The grading principles and operations map above the legal floor are still each station's own responsibility.")},
    ],
    "summary": (("<b>인공지능기본법</b> = 모든 검사장이 지켜야 할 <b>법적 최저선</b>, <b>고영향 AI</b>는 그 위에 <b>더 무거운 의무</b>를 지는 것.",
                 "<b>The AI Basic Act</b> = the <b>legal floor</b> every station must clear, with <b>high-impact AI</b> carrying <b>heavier duties</b> on top."),
                ("인공지능기본법은 모든 AI 사업자에게 투명성·안전성 확보를 위한 기본 의무를 지우는 법으로, 사람의 생명·신체 안전이나 기본권에 큰 영향을 미칠 수 있는 영역(의료, 채용, 신용평가, 사법 등)의 AI를 '고영향 AI'로 따로 분류해 사전 고지, 위험평가, 안전성 확보조치, 사람의 개입·감독 같은 추가 의무를 부과해요. 법은 지켜야 할 최저선을 그을 뿐이고, 그 위를 채우는 세부 원칙(AI 윤리기준·거버넌스)과 실행 절차(AI 리스크 관리 프레임워크)는 조직이 스스로 갖춰야 해요.",
                 "Korea's AI Basic Act imposes baseline duties of transparency and safety on every AI business, and separately classifies AI used in domains where life, bodily safety, or basic rights are heavily at stake — medicine, hiring, credit, the judiciary, and the like — as 'high-impact AI,' adding duties like advance notice, risk assessment, safety measures, and human oversight. The law only draws the floor; the detailed principles above it (AI ethics and governance) and the execution procedure (an AI risk management framework) are still something an organization has to build for itself.")),
    "glossary": [
        ("인공지능기본법", "AI Basic Act", ("나라가 정한 최소 등급 기준.", "The minimum grading rule the country itself sets."), ("모든 검사장에 공통으로 적용돼요.", "Applies to every station alike.")),
        ("고영향 AI", "High-impact AI", ("생명·안전·기본권에 크게 영향을 주는 AI.", "AI that heavily affects life, safety, or basic rights."), ("추가 의무를 더 짊어져요.", "Carries extra duties on top of the basics.")),
        ("사전 고지 의무", "Advance notice duty", ("이건 AI가 판정해요, 라고 먼저 알리는 것.", "Telling people up front that AI is making the call."), ("손님이 알고 선택할 수 있게 해요.", "Lets the customer know and choose with open eyes.")),
        ("위험평가 의무", "Risk assessment duty", ("고영향 AI에게 추가되는 평가 절차.", "An assessment procedure added for high-impact AI."), ('운영 지도의 ②③단계와 같은 작업이에요. → <a href="airiskframe-ko.html">검사장 전체를 도는 운영 지도</a>', 'The same work as stages ② and ③ of the operations map. → <a href="airiskframe-en.html">The Operations Map That Walks the Whole Station</a>')),
        ("안전성 확보조치", "Safety assurance measures", ("사고를 막을 실제 장치.", "Actual safeguards put in place to prevent accidents."), ("원칙만으론 부족하고, 실행이 뒤따라야 해요.", "Principle alone isn't enough — execution has to follow.")),
        ("사람의 개입·감독", "Human oversight", ("기계 혼자 끝내지 않게 하는 장치.", "The mechanism that keeps a machine from finishing the call alone."), ('AI 윤리기준이 보장하는 사람 재검토와 같은 뿌리예요. → <a href="aiethicsgov-ko.html">모든 검사장이 함께 쓰는 등급 원칙판</a>', 'Shares its roots with the human review the ethics charter guarantees. → <a href="aiethicsgov-en.html">The Grading Charter Every Station Shares</a>')),
        ("법적 최저선", "Legal floor", ("법이 보장하는 최소한의 수준.", "The minimum level the law guarantees."), ("이 위는 각 조직의 윤리기준과 리스크 관리가 채워야 해요.", "What's built above it is up to each organization's own ethics and risk management.")),
        ("과징금·제재", "Fines & penalties", ("의무를 어겼을 때 따르는 법적 책임.", "The legal consequence of failing these duties."), ("법이 그냥 권고가 아니라 강제력을 갖게 하는 장치예요.", "What makes the law a real requirement, not just a suggestion.")),
    ],
}
