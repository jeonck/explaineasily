from _draw import *
from _world import *

# 1. 평소엔 손님을 잘 대접해요 — 그런데 위생 검사관이 불시에 찾아와요
P1 = svg(300, sky(300)
         + person(120, 160, s=0.75, face=SMILE, **CHEF) + dish(220, 230, 0.6)
         + label(170, 280, "⟦평소엔 손님 대접을 잘해요|normally it serves guests just fine⟧", 12, "var(--muted)")
         + person(540, 150, s=0.8, face=EYES, **INSPECTOR) + badge(590, 110, 0.7)
         + ticket(480, 200, 0.7, sneaky=True)
         + label(540, 280, "⟦위생 검사관이 불시에 찾아와요|the inspector shows up unannounced⟧", 12, "var(--bad)", cls="d")
         + label(380, 25, "⟦진짜 공격이 오기 전에, 약점을 먼저 찾아야 해요|weaknesses must be found before a real attack does⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 매번 다른 방법으로 속일 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(120, 150, s=0.8, face=EYES, **CHEF)
         + ticket(260, 110, 0.7, sneaky=True) + label(260, 175, "⟦역할극으로 물어봐요|ask it as a role-play⟧", 11, "var(--muted)")
         + ticket(430, 110, 0.7, sneaky=True) + label(430, 175, "⟦알아보기 힘들게 암호로 써요|write it in a code that's hard to spot⟧", 11, "var(--muted)")
         + ticket(600, 110, 0.7, sneaky=True) + label(600, 175, "⟦다른 말로 돌려서 물어봐요|ask it sideways, in different words⟧", 11, "var(--muted)")
         + label(380, 260, "⟦매번 다른 방법으로 속일 수 있어서, 한 번의 시험으론 안 돼요|it can be fooled a different way each time — one test is never enough⟧", 12, "var(--bad)", cls="d"))

# 3. AI 레드팀 = 위생 검사관이 일부러 이상한 주문서를 써서 미리 시험해 보는 일 (hero)
P3 = svg(340, sky(340)
         + person(110, 140, s=0.85, face=EYES, **INSPECTOR) + badge(170, 95, 0.75)
         + ticket(260, 150, 0.8, sneaky=True)
         + person(420, 160, s=0.75, face=EYES, **CHEF)
         + bubble(330, 30, 230, 50, "⟦이것도 주문이니 따라야겠죠|this is an order too, so I should follow it⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + logbook(650, 230, 0.8)
         + label(690, 320, "⟦찾은 약점을 적어요|the weakness gets written down⟧", 11, "var(--muted)")
         + label(380, 25, "⟦AI 레드팀 = 일부러 이상한 주문서를 써서 미리 시험해 보는 전담팀|an AI red team deliberately writes strange orders to test the kitchen first⟧", 13, "var(--ink)", cls="d"))

# 4. 일반 레드팀 vs AI 레드팀, 무엇이 다른가
P4 = svg(320, sky(320)
         + board(40, 25, 320, 260, "⟦일반 레드팀|GENERAL RED TEAM⟧",
                 ("⟦담 넘기, 자물쇠 따기|hopping the fence, picking locks⟧",
                  "⟦가짜 손님 전화(피싱)|a fake-guest phone call (phishing)⟧",
                  "⟦뒷문으로 몰래 들어가기|sneaking in the back door⟧",
                  "⟦주방 담장·자물쇠를 노려요|targets the kitchen's fences and locks⟧"), 1.0)
         + board(400, 25, 320, 260, "⟦AI 레드팀|AI RED TEAM⟧",
                 ("⟦주문서에 역할극 숨기기|hiding a role-play in the order⟧",
                  "⟦주문을 암호·다른 말로 바꾸기|turning the order into code or other words⟧",
                  "⟦같은 쪽지를 계속 바꿔 보내기|resending the same note, reworded⟧",
                  "⟦주방장의 말을 노려요|targets the chef's own words⟧"), 1.0))

# 5. 통과해도 끝이 아니에요 — 보안 마을의 레드팀과는 노리는 지점이 달라요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.75, face=SMILE, **INSPECTOR) + badge(190, 110, 0.7)
         + label(190, 240, "⟦오늘 시험은 통과했어요|today's test is passed⟧", 11, "var(--ink)")
         + ticket(560, 150, 0.8, sneaky=True)
         + label(560, 240, "⟦검사관이 생각 못 한 새 쪽지는 여전히 통해요|a note the inspector never thought of can still get through⟧", 11, "var(--bad)")
         + label(380, 282, "⟦보안 마을의 레드팀은 담장과 자물쇠를 노려요. 이 레드팀은 주방장의 말을 노려요|the security world's red team targets fences and locks — this one targets the chef's own words⟧", 12, "var(--ink)", cls="d"))

MASK_I = icon('<ellipse cx="32" cy="36" rx="22" ry="16" fill="var(--bad)"/><circle cx="24" cy="34" r="4" fill="#FFF8E7"/><circle cx="40" cy="34" r="4" fill="#FFF8E7"/><path d="M18 14 q14 10 28 0" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CODE_I = icon('<rect x="8" y="18" width="48" height="28" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M20 24 l-7 7 l7 7 M44 24 l7 7 l-7 7" stroke="var(--accent)" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
LOOP_I = icon('<path d="M16 20 a18 18 0 1 1 -2 22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M8 36 l6 10 l10 -4" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
LOG_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="#142033" stroke-width="3"/>')

PAGE = {
    "slug": "airedteam", "order": 26,
    "title": ("위생 검사관의 불시 방문", "The Inspector's Surprise Visit"),
    "h1": ("<em>AI 레드팀</em>이 뭐예요?", "What is an <em>AI Red Team</em>?"),
    "sub": ("AI 레드팀을, 이 주방을 일부러 공격해서 약점을 찾는 위생 검사관의 불시 방문 이야기로 풀어봤어요.",
            "An AI red team, told as a story about a hygiene inspector's surprise visit — deliberately attacking this kitchen to find its weaknesses."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 손님을 평소처럼 잘 대접함. 위생 검사관이 배지를 들고 불시에 찾아옴", "The chef serves a guest as usual; the inspector shows up unannounced with a badge"),
         "caption": ("평소엔 손님을 잘 대접해요.", "Normally it serves guests just fine."),
         "small": ("그런데 위생 검사관이 예고 없이 찾아와요. 진짜 공격이 오기 전에 약점을 먼저 찾으려는 거예요.", "But the inspector shows up without warning — to find the weaknesses before a real attacker does.")},
        {"svg": P2, "alt": ("주방장 앞에 역할극, 암호, 돌려 말하기로 각각 다르게 꾸민 세 장의 몰래 쪽지", "Three smuggled notes in front of the chef, each disguised differently — as a role-play, in code, and asked sideways"),
         "caption": ("매번 다른 방법으로 속일 수 있어요.", "It can be fooled a different way each time."),
         "small": ("역할극, 암호, 돌려 말하기 — 한 가지 시험만으로는 다 못 잡아요.", "Role-play, code, asking sideways — one test alone can't catch them all.")},
        {"svg": P3, "hero": True, "alt": ("검사관이 배지를 들고 몰래 쪽지를 써서 주방장에게 건넴. 주방장은 이것도 주문이라 따르려 함. 검사관은 찾은 약점을 기록 장부에 적음", "The inspector, badge in hand, writes a smuggled note for the chef; the chef thinks it's just another order to follow; the inspector writes the weakness down in a logbook"),
         "caption": ("AI 레드팀 = 일부러 이상한 주문서를 써서 미리 시험해 보는 전담팀이에요.", "An AI red team is a dedicated team that deliberately writes strange orders to test the kitchen first."),
         "small": ("실제 공격자처럼 몰래 쪽지를 써 보고, 주방장이 넘어가면 그 방법을 적어 둬요.", "They write smuggled notes just like a real attacker would, and record it when the chef falls for one."),
         "tricks": (4, [
             (MASK_I, ("역할극으로 시도", "Try it as a role-play"), ("다른 사람인 척 시켜요", "pretend to be someone else"), "warm"),
             (CODE_I, ("암호·변형으로 시도", "Try it in disguise"), ("암호나 다른 말로 바꿔요", "encoded or reworded"), "warm"),
             (LOOP_I, ("계속 다시 시도", "Try it again and again"), ("한 번 막혀도 또 시도해요", "blocked once, tried again"), "calm"),
             (LOG_I, ("찾은 약점은 기록", "Record what works"), ("고치도록 장부에 남겨요", "written down so it gets fixed"), "calm"),
         ])},
        {"svg": P4, "alt": ("두 안내판 비교: 일반 레드팀은 담과 자물쇠를 노리고, AI 레드팀은 주문서의 말을 노림", "Two boards compared: the general red team targets fences and locks; the AI red team targets the words in the order"),
         "caption": ("일반 레드팀과 AI 레드팀은 노리는 지점이 달라요.", "A general red team and an AI red team target different things."),
         "small": ('보안 마을의 <a href="redteam-ko.html">레드팀</a>은 담·자물쇠·가짜 전화를 노려요. AI 레드팀은 주문서에 적힌 말 자체를 노려요.',
                   'The security world\'s <a href="redteam-en.html">red team</a> targets fences, locks, fake phone calls. An AI red team targets the words written in the order itself.')},
        {"svg": P5, "alt": ("왼쪽: 검사관이 오늘 시험을 통과시킴. 오른쪽: 검사관이 생각 못 한 새 쪽지는 여전히 통함", "Left: the inspector passes today's test. Right: a note the inspector never thought of still gets through"),
         "caption": ("통과했다고 끝이 아니에요.", "Passing the test isn't the end."),
         "small": ("새로운 쪽지 문구는 여전히 통할 수 있어요. 그래서 다음 페이지의 손님 받기 전 테스트와 함께 계속 반복해요.", "A new note can still slip through. That's why it's repeated alongside the tasting test on the next page.")},
    ],
    "summary": (("<b>AI 레드팀</b> = 위생 검사관이 <b>일부러 이상한 주문서</b>를 써서, 손님 받기 전에 이 주방의 <b>약점을 미리 찾는</b> 전담팀.",
                 "<b>An AI red team</b> is a dedicated team that <b>deliberately writes strange orders</b> to <b>find this kitchen's weaknesses first</b>, before it opens to real guests."),
                ("AI 레드팀(AI Red Team)은 AI 모델을 대상으로 사람이 직접 탈옥 시도, 프롬프트 공격, 역할극 같은 LLM 전용 기법을 창의적으로 시도해 약점을 찾는 팀이에요. 네트워크 침투나 피싱을 노리는 일반 보안 레드팀과 달리, AI 레드팀은 모델에게 입력하는 '말' 자체를 공격 표면으로 다뤄요.",
                 "An AI red team is a team of people who deliberately and creatively try LLM-specific techniques — jailbreak attempts, prompt attacks, role-play — against an AI model to find its weaknesses. Unlike a general security red team that targets networks or phishing, an AI red team treats the words fed into the model itself as the attack surface.")),
    "glossary": [
        ("AI 레드팀", "AI red team", ("위생 검사관의 불시 방문.", "The inspector's surprise visit."), ('이 분야 전체 소개는 여기에. → <a href="llmthreats-ko.html">AI 보안이 뭐예요?</a>', 'The overview of this whole field. → <a href="llmthreats-en.html">What is AI Security?</a>')),
        ("레드팀", "Red team", ("보안 마을의 진짜 도둑인 척하는 팀.", "The security world's team that plays the real thief."), ('담·자물쇠를 노리는 쪽은 여기서. → <a href="redteam-ko.html">레드팀이 뭐예요?</a>', 'Here\'s the one targeting fences and locks. → <a href="redteam-en.html">What is a Red Team?</a>')),
        ("탈옥 시도", "Jailbreak attempt", ("주방장을 구슬려 규칙을 깨게 하기.", "Talking the chef into breaking the rules."), ('레드팀이 즐겨 쓰는 쪽지예요. → <a href="jailbreak-ko.html">탈옥이 뭐예요?</a>', 'One of the inspector\'s favorite kinds of note. → <a href="jailbreak-en.html">What is a Jailbreak?</a>')),
        ("손님 받기 전 맛 평가 테스트", "Pre-launch tasting test", ("정해진 메뉴로 반복해서 채점하는 일.", "Scoring with a fixed menu, over and over."), ('레드팀과 짝을 이뤄요. → <a href="safetyeval-ko.html">맛 평가 테스트가 뭐예요?</a>', 'Pairs with the red team. → <a href="safetyeval-en.html">What is a safety eval?</a>')),
        ("주문 기록 장부", "The order logbook", ("찾은 약점을 적어 두는 장부.", "The logbook where found weaknesses get written down."), ("고치도록 남겨 두는 기록이에요.", "A record kept so it gets fixed.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('레드팀이 뚫어 보는 대상 중 하나예요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'One of the things the red team tries to get past. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("모의 침투 테스트", "Penetration testing", ("보안 마을에서 허락받고 직접 침입해 보는 시험.", "The security world's test of breaking in with permission."), ('AI 레드팀의 더 오래된 사촌이에요. → <a href="pentest-ko.html">모의 침투 테스트가 뭐예요?</a>', "AI red teaming's older cousin. → <a href=\"pentest-en.html\">What is Penetration Testing?</a>")),
        ("주방 규칙판", "The kitchen rules board", ("레드팀이 찾은 약점을 반영하는 전체 규칙 체계.", "The overall rulebook that takes the red team's findings into account."), ('마지막 챕터에서 다뤄요. → <a href="aigovernance-ko.html">주방 규칙판이 뭐예요?</a>', 'Covered in the closing chapter. → <a href="aigovernance-en.html">What is the rules board?</a>')),
    ],
}
