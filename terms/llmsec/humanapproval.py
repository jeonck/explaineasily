from _draw import *
from _world import *

# 1. 견습생이 되돌리기 어려운 일을 혼자 하려고 해요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **RUNNER) + ticket(210, 190, 0.7)
         + knifedrawer(260, 230, 0.6, locked=False, labels=("⟦결제|pay⟧", "⟦삭제|delete⟧"))
         + label(330, 285, "⟦허락 없이 그냥 하려고 해요|about to just do it, without asking⟧", 12, "var(--bad)", cls="d")
         + person(600, 150, s=0.75, face=SMILE, **MANAGER)
         + label(600, 250, "⟦사장님은 아직 몰라요|the owner doesn't know yet⟧", 12, "var(--muted)")
         + label(380, 25, "⟦결제나 삭제처럼, 되돌리기 어려운 일이에요|like paying or deleting — hard to undo once it's done⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 견습생은 자신 있게 진행할 뿐, 되돌릴 수 없는 일인지 스스로 못 멈춰요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 150, s=0.85, face=EYES, **RUNNER)
         + bubble(220, 60, 260, 50, "⟦시킨 대로 결제까지 끝냈어요|done — I even finished the payment, as asked⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(160, 250, "⟦스스로 멈추지 않아요|it doesn't stop by itself⟧", 12, "var(--bad)")
         + label(550, 150, "⟦되돌릴 수 있을까요…?|can this even be undone…?⟧", 13, "var(--bad)", cls="d")
         + label(380, 280, "⟦견습생은 자신 있게 해낼 뿐, 되돌리기 어려운 일인지는 스스로 못 가려요|the runner just confidently gets it done — it can't tell on its own whether it's hard to undo⟧", 12, "var(--bad)", cls="d"))

# 3. 사장님 최종 승인 = 위험한 행동을 실행하기 전, 사람이 마지막으로 확인하는 것 (hero)
P3 = svg(340, sky(340)
         + person(110, 170, s=0.8, face=EYES, **RUNNER) + ticket(190, 210, 0.7)
         + label(150, 300, "⟦요청|request⟧", 11, "var(--muted)")
         + label(280, 190, "⟦대기…|waiting…⟧", 16, "var(--accent)", cls="d")
         + person(450, 150, s=0.85, face=EYES, **MANAGER)
         + stamp(560, 110, 0.7)
         + label(450, 300, "⟦사장님이 확인하고 도장을 찍어요|the owner checks it, then stamps it⟧", 12, "var(--ink)")
         + label(380, 25, "⟦사장님 최종 승인 = 위험한 행동을 실행하기 전, 사람이 마지막으로 확인하는 것|a human approval gate means a person checks a risky action before it runs⟧", 13, "var(--ink)", cls="d"))

# 4. 요청 → 대기 → 확인 → 승인(진행) / 거절(중단)
P4 = svg(320, sky(320)
         + person(50, 130, s=0.6, face=EYES, **RUNNER) + label(80, 230, "⟦요청|request⟧", 11, "var(--muted)")
         + label(170, 150, "⟦→|→⟧", 26, "var(--muted)", cls="d")
         + label(230, 150, "⟦대기|wait⟧", 14, "var(--accent)", cls="d")
         + label(300, 150, "⟦→|→⟧", 26, "var(--muted)", cls="d")
         + person(370, 110, s=0.65, face=EYES, **MANAGER) + label(400, 230, "⟦사장님 확인|owner checks⟧", 11, "var(--muted)")
         + label(480, 110, "⟦✓|✓⟧", 26, "var(--good)", cls="d") + label(480, 150, "⟦승인|approve⟧", 11, "var(--good)")
         + label(480, 180, "⟦→ 진행|→ proceed⟧", 11, "var(--muted)")
         + label(480, 220, "⟦×|×⟧", 26, "var(--bad)", cls="d") + label(560, 220, "⟦거절|reject⟧", 11, "var(--bad)")
         + label(560, 250, "⟦→ 중단|→ stop⟧", 11, "var(--muted)")
         + label(380, 300, "⟦애매하거나 되돌리기 어려운 요청만 이 줄을 거쳐요|only ambiguous or hard-to-undo requests go through this line⟧", 12, "var(--ink)"))

# 5. 매번 사장님을 기다리긴 느려요 — 그래서 규칙판에서 '언제 세울지'를 정해요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(130, 150, s=0.75, face=FROWN, **RUNNER)
         + label(190, 250, "⟦작은 일까지 다 세우면 너무 느려요|stopping for every small thing is far too slow⟧", 11, "var(--ink)")
         + board(440, 60, 280, 110, "⟦언제 세울지|WHEN TO STOP⟧",
                 ("⟦결제·삭제는 항상 세워요|always stop for paying or deleting⟧",
                  "⟦검색·요약은 그냥 진행해요|search and summarize just proceed⟧"))
         + label(380, 300, "⟦이 한 번의 승인 단계를, 언제·누가 세울지는 주방 규칙판 전체가 정해요|when and who stops at this one gate is decided by the whole kitchen rules board⟧", 12, "var(--ink)", cls="d"))

WAIT_I = icon('<circle cx="32" cy="32" r="24" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 18 v14 l10 8" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')
EYE_I = icon('<ellipse cx="32" cy="32" rx="26" ry="16" fill="none" stroke="var(--ink)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>')
STAMP_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M22 32 l7 8 l13 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
STOP_I = icon('<rect x="12" y="12" width="40" height="40" rx="6" fill="var(--bad)"/><path d="M20 32 h24" stroke="#FFF8E7" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "humanapproval", "order": 28,
    "title": ("사장님 최종 승인", "The Owner's Final Sign-off"),
    "h1": ("<em>사람 승인 단계</em>가 뭐예요?", "What is a <em>Human Approval Gate</em>?"),
    "sub": ("사람 승인 단계를, 위험한 일을 실행하기 전 견습생이 사장님의 도장을 기다리는 이야기로 풀어봤어요.",
            "A human approval gate, told as a story about a runner who waits for the owner's stamp before doing anything risky."),
    "panels": [
        {"svg": P1, "alt": ("견습생이 결제·삭제가 적힌 잠기지 않은 서랍을 허락 없이 쓰려고 함. 사장님은 아직 모름", "A runner is about to use an unlocked drawer labeled pay and delete without asking; the owner doesn't know yet"),
         "caption": ("견습생이 되돌리기 어려운 일을 혼자 하려고 해요.", "The runner is about to do something hard to undo, all on its own."),
         "small": ("결제나 삭제처럼요. 사장님은 아직 그 사실을 몰라요.", "Like paying or deleting. And the owner doesn't even know yet.")},
        {"svg": P2, "alt": ("견습생이 시킨 대로 결제까지 끝냈다고 자신 있게 말함. 되돌릴 수 있을지 물음표가 떠 있음", "The runner confidently says it even finished the payment, as asked; a question mark hangs over whether it can be undone"),
         "caption": ("견습생은 스스로 멈추지 않아요.", "The runner doesn't stop by itself."),
         "small": ("자신 있게 해낼 뿐, 그게 되돌리기 어려운 일인지는 스스로 가리지 못해요.", "It just confidently gets it done — it can't tell on its own that the job is hard to undo.")},
        {"svg": P3, "hero": True, "alt": ("견습생이 주문서를 들고 대기. 사장님이 확인하고 도장을 찍음", "The runner holds a ticket and waits; the owner checks it and stamps it"),
         "caption": ("사장님 최종 승인 = 위험한 행동을 실행하기 전, 사람이 마지막으로 확인하는 것이에요.", "A human approval gate means a person makes the last check before a risky action runs."),
         "small": ("견습생은 바로 하지 않고 멈춰서 기다려요. 사장님이 보고 나서야 도장이 찍혀요.", "The runner stops and waits instead of just doing it. Only after the owner looks does the stamp come down."),
         "tricks": (4, [
             (WAIT_I, ("실행 전에 멈추기", "Pause before it runs"), ("해 버린 뒤가 아니라 전에요", "before it's done, not after"), "calm"),
             (EYE_I, ("되돌리기 어려운 일만", "Only the hard-to-undo ones"), ("결제·삭제 같은 일요", "like paying or deleting"), "calm"),
             (STAMP_I, ("승인해야 진행", "Must approve to proceed"), ("도장이 찍혀야 움직여요", "only moves once stamped"), "warm"),
             (STOP_I, ("거절하면 그대로 멈춤", "Reject it and it stays stopped"), ("사장님 말이 마지막이에요", "the owner has the final word"), "warm"),
         ])},
        {"svg": P4, "alt": ("요청 → 대기 → 사장님 확인 → 승인하면 진행, 거절하면 중단으로 이어지는 흐름", "A flow: request → wait → owner checks → approve leads to proceed, reject leads to stop"),
         "caption": ("요청 → 대기 → 확인 → 승인 또는 거절이에요.", "Request, then wait, then a check, then approve or reject."),
         "small": ("애매하거나 되돌리기 어려운 요청만 이 줄을 거쳐요. 검색이나 요약 같은 건 그냥 지나가요.", "Only ambiguous or hard-to-undo requests go through this line. Things like search or summarize just pass through.")},
        {"svg": P5, "alt": ("왼쪽: 견습생이 작은 일까지 다 세우면 느리다고 불평함. 오른쪽: 언제 세울지를 정한 규칙판", "Left: the runner is frustrated that stopping for every small thing is slow. Right: a rules board deciding when to stop"),
         "caption": ("매번 사장님을 기다리긴 느려요.", "Waiting for the owner every single time is slow."),
         "small": ("그래서 언제·어떤 일에 이 승인 단계를 세울지는, 주방 규칙판 전체가 미리 정해 둬요.", "So when and for what this approval gate kicks in gets decided ahead of time, by the whole kitchen rules board.")},
    ],
    "summary": (("<b>사람 승인 단계</b> = 견습생이 <b>되돌리기 어려운 일</b>을 하기 전, <b>사장님이 마지막으로 확인</b>하고 도장을 찍는 것.",
                 "<b>A human approval gate</b> means the owner <b>makes a final check and stamps it</b> before the runner does anything <b>hard to undo</b>."),
                ("사람 승인 단계(Human-in-the-loop approval)는 자율 에이전트가 되돌리기 어렵거나 민감한 행동(결제, 삭제, 외부 전송 등)을 실행하기 직전에, 사람의 명시적 승인을 받도록 멈추는 안전장치예요. '권한을 과도하게 많이 쥔 상태' 자체를 고치는 게 아니라, 그 권한이 실제로 쓰이는 순간에 사람을 끼워 넣어 위험을 줄이는 구체적인 장치예요.",
                 "A human approval gate is a safeguard that pauses an autonomous agent right before it carries out a hard-to-undo or sensitive action — paying, deleting, sending something external — until a person explicitly approves it. It doesn't fix the underlying state of having too much authority; it's one concrete mechanism that inserts a person at the moment that authority is actually used.")),
    "glossary": [
        ("사람 승인 단계", "Human approval gate", ("사장님 최종 승인.", "The owner's final sign-off."), ('이 분야 전체 소개는 여기에. → <a href="llmthreats-ko.html">AI 보안이 뭐예요?</a>', 'The overview of this whole field. → <a href="llmthreats-en.html">What is AI Security?</a>')),
        ("자율 에이전트", "Autonomous agent", ("스스로 심부름하는 견습생.", "The runner that does errands on its own."), ('너무 많은 열쇠를 쥐면 이 승인 단계가 더 중요해져요. → <a href="excessiveagency-ko.html">너무 많은 열쇠를 받은 견습생</a>', 'The more keys it holds, the more this gate matters. → <a href="excessiveagency-en.html">the apprentice handed too many keys</a>')),
        ("도구 호출", "Tool calling", ("서랍에서 도구를 꺼내 쓰는 일.", "Taking a tool out of the drawer."), ('견습생이 결제·삭제를 실행하는 바로 그 동작이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'The very action a runner uses to pay or delete. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("최소 권한", "Least privilege", ("필요한 열쇠만 쥐어 주는 것.", "Handing over only the keys that are needed."), ('승인 단계보다 먼저, 서랍 자체를 잠가 두는 쪽이에요. → <a href="leastprivilege-ko.html">열쇠 이야기가 뭐예요?</a>', 'A step earlier than approval — locking the drawer itself. → <a href="leastprivilege-en.html">What is least privilege?</a>')),
        ("주방 규칙판", "The kitchen rules board", ("언제 이 승인 단계를 세울지 정하는 전체 체계.", "The overall system that decides when this gate kicks in."), ('이 승인 한 번을 포함하는 더 큰 규칙 체계예요. → <a href="aigovernance-ko.html">주방 규칙판이 뭐예요?</a>', 'The larger rule system that this one gate lives inside. → <a href="aigovernance-en.html">What is the rules board?</a>')),
        ("되돌릴 수 없는 행동", "Irreversible action", ("결제나 삭제처럼 무를 수 없는 일.", "Something like paying or deleting that can't be undone."), ("이 승인 단계가 특히 지키려는 일이에요.", "Exactly the kind of thing this gate exists to guard.")),
        ("비상벨", "The incident bell", ("승인을 건너뛴 채 일이 터졌을 때 누르는 벨.", "The bell rung when something goes wrong without approval."), ("승인 단계가 없었다면 다음에 올 장면이에요.", "The scene that follows when this gate was missing.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('승인 단계보다 앞서 말과 글을 거르는 쪽이에요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'The earlier checkpoint that filters words, before this gate. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
    ],
}
