from _draw import *
from _world import *

# 1. 이상한 요리가 나가고, 누군가 비상벨로 손을 뻗어요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 260 - 112 * 0.7, s=0.7, face=FROWN, **GUEST) + dish(140, 260 - 112 * 0.7 - 30, 0.9, bad=True)
         + label(140, 280, "⟦이상한 요리가 나갔어요|a strange dish went out⟧", 11, "var(--bad)")
         + person(420, 260 - 112 * 0.65, s=0.65, face=SWEAT, **CHEF)
         + bell(560, 170, 1.0, ringing=False)
         + label(560, 245, "⟦누군가 비상벨로 손을 뻗어요|someone reaches for the emergency bell⟧", 11, "var(--muted)")
         + label(380, 30, "⟦AI가 관련된 사고가 터졌어요 — 오남용, 오작동, 유출일 수 있어요|an AI-related incident just hit — misuse, malfunction, or a leak⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 기계는 고장나면 요란한데, 이 주방장은 조용히, 자신 있게 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + knifedrawer(60, 110, 0.55, labels=("⟦불꽃|spark⟧", "⟦불꽃|spark⟧"))
         + '<path d="M150 90 l10 -14 M165 95 l12 -10" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
         + label(150, 195, "⟦기계는 고장나면 요란해요|a machine breaks loudly⟧", 11, "var(--muted)")
         + person(480, 260 - 112 * 0.75, s=0.75, face=SMILE, **CHEF)
         + label(480, 280, "⟦이 주방장은 조용히, 자신 있게 틀려요|this chef gets it wrong quietly, and confidently⟧", 12, "var(--bad)", cls="d")
         + label(380, 30, "⟦그래서 사고가 난 줄도 모르고 한참 지나버려요|so a long time can pass before anyone even knows something's wrong⟧", 13, "var(--ink)"))

STOP_I = icon('<circle cx="32" cy="32" r="24" fill="var(--bad)"/><rect x="18" y="28" width="28" height="8" fill="#FFF8E7"/>')
SORT_I = icon('<rect x="8" y="8" width="20" height="20" rx="3" fill="var(--accent)"/><rect x="36" y="8" width="20" height="20" rx="3" fill="var(--good)"/><rect x="8" y="36" width="20" height="20" rx="3" fill="var(--bad)"/><rect x="36" y="36" width="20" height="20" rx="3" fill="#8B5E3C"/>')
TELL_I = icon('<rect x="8" y="14" width="30" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 22 h18 M14 28 h12" stroke="#142033" stroke-width="2.5"/><path d="M44 20 Q54 27 44 34" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
WRITE_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h14" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')

# 3. hero: AI 사고 대응 = 비상벨이 울리면 따르는 절차
P3 = svg(360, '<rect width="760" height="360" fill="var(--bad-soft)"/>'
         + bell(380, 130, 1.5, ringing=True)
         + label(380, 40, "⟦AI 사고 대응 = 비상벨이 울리면 따르는 절차예요|AI incident response is the procedure you follow when the bell rings⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦탈옥 성공, 유출, 오작동 — 어떤 사고든 같은 벨로 시작해요|a jailbreak, a leak, a malfunction — every kind of incident starts with the same bell⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 감지 → 멈춤 → 분류 → 알림 → 기록
P4 = svg(300, sky(300, ground=False)
         + label(380, 26, "⟦사고 대응은 순서가 있어요|incident response follows an order⟧", 13, "var(--ink)", cls="d")
         + bell(80, 130, 0.75, ringing=True) + label(80, 200, "⟦①감지|detect⟧", 12, "var(--ink)", cls="d")
         + '<path d="M120 130 H190" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + knifedrawer(195, 110, 0.45, labels=("⟦×|×⟧",)) + label(230, 200, "⟦②멈춤|contain⟧", 12, "var(--ink)", cls="d")
         + '<path d="M273 130 H340" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + board(345, 95, 90, 70, "⟦?|?⟧", ("⟦어느 지점?|which spot?⟧",), 0.85) + label(390, 200, "⟦③분류|classify⟧", 12, "var(--ink)", cls="d")
         + '<path d="M450 130 H510" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(545, 200 - 112 * 0.5, s=0.5, face=EYES, **GUEST) + label(545, 230, "⟦④알림|notify⟧", 12, "var(--ink)", cls="d")
         + '<path d="M590 130 H650" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + logbook(660, 95, 0.75) + label(705, 200, "⟦⑤기록|log⟧", 12, "var(--ink)", cls="d")
         + label(380, 280, "⟦감지→멈춤→분류→알림→기록, 이 순서가 다음 사고를 더 빨리 잡아요|detect, contain, classify, notify, log — in that order, the next incident gets caught faster⟧", 12, "var(--ink)"))

# 5. 결과·한계·이웃 차이: 고쳐도 왜 틀렸는지는 모르고, 지휘 체계는 같지만 사고 종류는 AI 전용
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(140, 260 - 112 * 0.75, s=0.75, face=SMILE, **CHEF)
         + label(140, 230, "⟦고쳐줘도 '내가 왜 틀렸는지'는 몰라요|even after it's fixed, it still doesn't know why it was wrong⟧", 11, "var(--bad)")
         + label(190, 282, "⟦사람이 맛보기 규칙을 직접 고쳐야 해요|a person has to fix the tasting rule by hand⟧", 12, "var(--bad)", cls="d")
         + board(420, 50, 300, 170, "⟦일반 사고 대응과 다른 점|DIFFERENT FROM A GENERAL INCIDENT⟧",
                 ("⟦지휘 체계는 같아요|the command structure is the same⟧",
                  "⟦사고 '종류'는 AI 전용이에요|the incident \"types\" are AI-specific⟧",
                  "⟦탈옥·유출·오작동처럼요|like a jailbreak, a leak, a bad call⟧"), 1.0)
         + label(570, 262, "⟦평소에 적어둔 장부가 분류를 훨씬 빠르게 해줘요|the logbook you kept all along makes classifying much faster⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aiincident", "order": 31,
    "title": ("울리는 비상벨", "The Bell That Rings"),
    "h1": ("<em>AI 사고 대응</em>이 뭐예요?", "What is an <em>AI Incident Response</em>?"),
    "sub": ("AI 사고 대응을, 뭔가 터지면 손 뻗는 비상벨과 그 다음 순서 이야기로 풀어봤어요.",
            "AI incident response, told as a story about the emergency bell you reach for when something breaks, and the order you follow after."),
    "panels": [
        {"svg": P1, "alt": ("손님이 이상한 요리를 받고 불편해하고, 주방장은 땀을 흘리고, 누군가 비상벨로 손을 뻗음", "A guest receives a strange dish and looks upset, the chef sweats, and someone reaches for the emergency bell"),
         "caption": ("AI가 관련된 사고가 터졌어요 — 오남용, 오작동, 유출일 수 있어요.", "An AI-related incident just hit — misuse, malfunction, or a leak."),
         "small": ("이상한 요리가 이미 손님에게 나간 다음이에요.", "The strange dish has already gone out to the guest.")},
        {"svg": P2, "alt": ("왼쪽: 칼서랍이 불꽃을 내며 요란하게 고장남. 오른쪽: 주방장은 웃으며 조용히, 자신 있게 계속 틀린 요리를 만듦", "Left: the knife drawer sparks and breaks loudly. Right: the chef keeps smiling, quietly and confidently getting it wrong"),
         "caption": ("기계는 고장나면 요란한데, 이 주방장은 조용히, 자신 있게 틀려요.", "A machine breaks loudly — this chef gets it wrong quietly, and confidently."),
         "small": ("그래서 사고가 난 줄도 모르고 한참 지나버려요.", "So a long time can pass before anyone even knows something's wrong.")},
        {"svg": P3, "hero": True, "alt": ("비상벨이 크게 울리고 있음", "A large emergency bell rings loudly"),
         "caption": ("AI 사고 대응 = 비상벨이 울리면 따르는 절차예요.", "AI incident response is the procedure you follow when the bell rings."),
         "small": ("탈옥 성공, 유출, 오작동 — 어떤 사고든 같은 벨로 시작해요.", "A jailbreak, a leak, a malfunction — every kind of incident starts with the same bell."),
         "tricks": (4, [
             (STOP_I, ("비슷한 요리부터 멈춰요", "Stop similar dishes first"), ("더 나가기 전에 막아요", "halt it before more go out"), "calm"),
             (SORT_I, ("어떤 사고인지 구분해요", "Classify what kind it is"), ("탈옥·유출·오작동 중 뭔지", "jailbreak, leak, or malfunction?")),
             (TELL_I, ("손님에게도 알려요", "Tell the affected guests"), ("숨기지 않아요", "no hiding it"), "warm"),
             (WRITE_I, ("끝나면 장부에 남겨요", "Write it in the logbook after"), ("다음에 쓸 재료가 돼요", "becomes material for next time")),
         ])},
        {"svg": P4, "alt": ("비상벨, 멈춘 칼서랍, 물음표 안내판, 손님, 장부가 화살표로 이어진 다섯 단계 순서도", "A five-step flow connected by arrows: the bell, a halted knife drawer, a question-mark board, a guest, and a logbook"),
         "caption": ("감지 → 멈춤 → 분류 → 알림 → 기록, 순서가 있어요.", "Detect, contain, classify, notify, log — in that order."),
         "small": ("이 순서가 다음 사고를 더 빨리 잡아요.", "Following this order catches the next incident faster.")},
        {"svg": P5, "alt": ("왼쪽: 고쳐진 주방장이 여전히 웃으며 왜 틀렸는지 모름. 오른쪽: 일반 사고 대응과 다른 점을 적은 규칙판 — 지휘 체계는 같지만 사고 종류는 AI 전용", "Left: the now-fixed chef still smiles, not knowing why it was wrong. Right: a board listing what differs from a general incident — same command structure, but AI-specific incident types"),
         "caption": ("고쳐줘도 왜 틀렸는지는 몰라요 — 지휘 체계는 같지만 사고 종류는 AI 전용이에요.", "Even fixed, it doesn't know why it was wrong — the command structure is the same, but the incident types are AI-specific."),
         "small": ("평소에 적어둔 장부가 분류를 훨씬 빠르게 해줘요.", "The logbook you kept all along makes classifying much faster.")},
    ],
    "summary": (("<b>AI 사고 대응</b> = AI가 관련된 사고(탈옥·유출·오작동)가 터지면, <b>비상벨</b>을 울려 <b>멈추고·분류하고·알리고·기록하는</b> 순서를 따르는 일.",
                 "<b>AI incident response</b> = when an AI-related incident hits (a jailbreak, a leak, a malfunction), ringing the <b>bell</b> and following the order: <b>contain, classify, notify, log</b>."),
                ("AI 사고 대응은 LLM·에이전트가 관련된 사고(탈옥 성공, 민감정보 유출, 도구 오남용, 환각으로 인한 피해 등)에 대응하는 절차예요. 일반 인시던트 커맨드 구조(지휘·조치·소통 분리)는 그대로 쓰지만, 사고의 '종류'를 AI 보안 특유의 범주로 미리 분류해 둬야 하고, 평소 쌓아둔 감사 로그가 분류와 원인 파악을 크게 빠르게 해줘요.",
                 "AI incident response is the procedure for AI-related incidents — a successful jailbreak, a sensitive data leak, a misused tool, harm caused by a hallucination. It reuses the general incident-command structure (separating command, fixing, and communication), but the incident *types* need an AI-security-specific taxonomy, and an audit log kept all along makes classification and root-cause analysis far faster.")),
    "glossary": [
        ("AI 사고 대응", "AI incident response", ("비상벨이 울리면 따르는 절차.", "The procedure you follow when the emergency bell rings."), ("AI가 관련된 사고에만 쓰는, 전용 절차예요.", "A dedicated procedure used only for AI-related incidents.")),
        ("탈옥", "Jailbreak", ("규칙을 깨고 나쁜 말을 하게 만드는 것.", "Getting the chef to break the rules and say something it shouldn't."), ('가장 자주 벨을 울리는 사고 종류예요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'One of the most common reasons the bell rings. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
        ("데이터 유출", "Data leak", ("비밀 레시피가 밖으로 새어나가는 것.", "The secret recipe book leaking out."), ('AI 프라이버시 쪽에서 더 다뤄요. → <a href="aiprivacy-ko.html">AI 프라이버시가 뭐예요?</a>', 'Covered more in AI privacy. → <a href="aiprivacy-en.html">What is AI Privacy?</a>')),
        ("지휘 체계", "Incident command", ("누가 지휘봉을 들지 미리 정해두는 것.", "Deciding in advance who picks up the baton."), ('일반 사고 대응의 지휘 체계를 그대로 써요. → <a href="incidentcommand-ko.html">지휘봉을 든 사람</a>', 'Borrows the same command structure as a general incident. → <a href="incidentcommand-en.html">The One Holding the Baton</a>')),
        ("사후 분석", "Postmortem", ("사고 끝나고 탓하지 않고 쓰는 기록.", "The blameless record written after it's over."), ('AI 사고도 똑같이, 탓하지 않고 기록해요. → <a href="postmortem-ko.html">탓하지 않고 모여 쓰는 기록</a>', 'An AI incident gets the same blameless write-up. → <a href="postmortem-en.html">the record everyone writes without blame</a>')),
        ("런북", "Runbook", ("이런 사고엔 이렇게 하라고 미리 적어둔 매뉴얼.", "The manual that says exactly what to do for this kind of incident, written in advance."), ('사고 종류별로 미리 써 둬요. → <a href="runbook-ko.html">미리 적어둔 매뉴얼</a>', 'One written per incident type, ahead of time. → <a href="runbook-en.html">the manual written ahead of time</a>')),
        ("가드레일", "Guardrail", ("맛보기 검수대 — 평소엔 막아주는 울타리.", "The tasting checkpoint — the fence that blocks it, normally."), ('이게 뚫렸을 때 사고가 터져요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'An incident is what happens when this gets bypassed. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("감사 로그", "Audit log", ("매일매일 적어두는 주문 기록.", "The order record written down, every single day."), ('사고가 나기 전부터 쌓여 있던 게 제일 큰 도움이 돼요. → <a href="aiaudit-ko.html">주문 기록 장부</a>', 'What was already piling up before the incident is the biggest help. → <a href="aiaudit-en.html">the order logbook</a>')),
    ],
}
