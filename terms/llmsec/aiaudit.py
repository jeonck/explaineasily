from _draw import *
from _world import *

# 1. 바쁜 하루 — 주문도, 요리도, 도구 사용도 많은데 아무도 안 적어요
P1 = svg(300, sky(300)
         + ticket(120, 100, 0.8) + person(120, 280 - 112 * 0.55, s=0.55, face=SMILE, **GUEST)
         + person(300, 280 - 112 * 0.65, s=0.65, face=EYES, **CHEF) + dish(300, 280 - 112 * 0.65 - 30, 0.8)
         + knifedrawer(430, 230, 0.45, labels=("⟦칼|knife⟧",))
         + person(620, 280 - 112 * 0.6, s=0.6, face=EYES, **RUNNER)
         + label(380, 50, "⟦주문도, 요리도, 도구 사용도 많은 하루예요|a busy day — lots of orders, lots of dishes, lots of tool use⟧", 13, "var(--ink)", cls="d")
         + label(380, 282, "⟦그런데 아무도 아무것도 적어두지 않아요|and nobody is writing any of it down⟧", 12, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 멀쩡해 보이는 날엔, 적어두는 게 괜히 귀찮은 일 같아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 260 - 112 * 0.7, s=0.7, face=EYES, **CHEF)
         + bubble(40, 50, 230, 50, "⟦오늘은 멀쩡한데, 굳이 적어야 하나...|today looks fine — do I really need to write this down?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ticket(420, 150, 0.8) + ticket(480, 160, 0.8) + ticket(440, 190, 0.8)
         + label(450, 230, "⟦다 비슷해 보여요|they all look the same⟧", 11, "var(--muted)")
         + label(380, 280, "⟦나중에 뭐가 중요해질지는, 그날은 몰라요|you can't tell, on the day, which one will matter later⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 감사 로그 = 평소에 계속 적어두는 주문 기록 장부
P3 = svg(360, sky(360)
         + logbook(300, 90, 1.8)
         + ticket(130, 160, 0.7) + '<path d="M180 160 Q250 130 300 120" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
         + dish(130, 260, 0.7) + '<path d="M170 240 Q250 170 300 140" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
         + knifedrawer(540, 200, 0.4, labels=("⟦칼|knife⟧",)) + '<path d="M560 200 Q480 160 420 130" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
         + label(380, 40, "⟦감사 로그 = 평소에 계속 적어두는 주문 기록 장부예요|an audit log = the order logbook you keep writing, all the time⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦주문서도, 요리도, 도구 사용도 — 멀쩡한 날에도 적어둬요|the order, the dish, the tool use — written down even on a perfectly ordinary day⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 평소엔 조용히 쌓이다가, 벨이 울리면 그 장부를 펼쳐요
P4 = svg(330, sky(330, ground=False)
         + logbook(60, 40, 1.2) + label(140, 195, "⟦평소: 조용히 쌓여요|normally: it just quietly piles up⟧", 12, "var(--muted)")
         + '<path d="M260 110 H340" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + bell(380, 100, 1.0, ringing=True) + label(380, 195, "⟦사고가 나면|when an incident hits⟧", 12, "var(--ink)", cls="d")
         + '<path d="M420 110 H500" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(600, 220 - 112 * 0.75, s=0.75, face=EYES, **INSPECTOR) + badge(650, 170, 0.6) + logbook(540, 150, 0.9)
         + label(600, 290, "⟦그 전에 쌓인 장부를 펼쳐서 정확히 뭐가 있었는지 찾아요|the inspector opens that logbook to find out exactly what happened before⟧", 12, "var(--ink)"))

# 5. 한계·이웃 차이, 그리고 마무리: 이 기록이 다음 가드레일을 만드는 재료가 돼요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + logbook(80, 60, 1.3) + person(190, 300 - 112 * 0.55, s=0.55, face=SWEAT, **MANAGER)
         + label(140, 230, "⟦영원히 다 쌓아두면, 그것도 비용이고 위험이에요|keeping it all forever costs money, and it's a risk too⟧", 11, "var(--bad)")
         + label(190, 300, "⟦오래된 건 지우고, 비밀은 가려요|delete what's old, mask the secrets⟧", 12, "var(--bad)", cls="d")
         + board(420, 50, 300, 210, "⟦이웃 용어와 다른 점|DIFFERENT FROM ITS NEIGHBORS⟧",
                 ("⟦사고 대응: 벨이 울릴 때만|incident response: only when the bell rings⟧",
                  "⟦감사 로그: 평소에 계속|audit log: all the time, always⟧",
                  "⟦일반 관측: 시스템 숫자|observability: system numbers⟧",
                  "⟦감사 로그: AI의 말·행동|audit log: what the AI said and did⟧"), 1.0)
         + label(570, 282, "⟦이 기록들이 모여, 다음엔 더 나은 가드레일과 규칙을 만드는 재료가 돼요|these records pile up and become the material for a better guardrail and a better rule, next time⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aiaudit", "order": 32,
    "title": ("매일 적는 주문 기록 장부", "The Logbook Written Every Day"),
    "h1": ("<em>AI 감사 로그</em>가 뭐예요?", "What is an <em>AI Audit Log</em>?"),
    "sub": ("AI 감사 로그를, 멀쩡한 날에도 계속 적어두는 주문 기록 장부 이야기로 풀어봤어요.",
            "An AI audit log, told as a story about the order logbook you keep writing even on a perfectly ordinary day."),
    "panels": [
        {"svg": P1, "alt": ("손님 주문, 주방장의 요리, 칼서랍 사용, 견습생까지 바쁘게 돌아가지만 아무도 기록을 남기지 않음", "A guest's order, the chef's dish, the knife drawer in use, and a runner all busy at once — but nobody writes any of it down"),
         "caption": ("주문도, 요리도, 도구 사용도 많은 하루인데, 아무도 적어두지 않아요.", "A busy day of orders, dishes, and tool use — and nobody is writing any of it down."),
         "small": ("멀쩡한 날이라 다들 기록이 필요 없다고 생각해요.", "It's an ordinary day, so nobody thinks a record is needed.")},
        {"svg": P2, "alt": ("주방장이 오늘은 멀쩡한데 적어야 하나 중얼거리고, 비슷해 보이는 주문서 세 장이 쌓여 있음", "The chef mutters that today looks fine, so why bother writing it down, while three similar-looking order tickets pile up"),
         "caption": ("멀쩡해 보이는 날엔, 적어두는 게 괜히 귀찮은 일 같아요.", "On a day that looks fine, writing it down feels like needless extra work."),
         "small": ("나중에 뭐가 중요해질지는, 그날은 몰라요.", "You can't tell, on the day, which one will matter later.")},
        {"svg": P3, "hero": True, "alt": ("커다란 장부 가운데로 주문서, 요리, 칼서랍 사용이 화살표를 따라 모두 적혀 들어감", "A large logbook in the center, with the order, the dish, and knife-drawer use all flowing into it along arrows"),
         "caption": ("감사 로그 = 평소에 계속 적어두는 주문 기록 장부예요.", "An audit log = the order logbook you keep writing, all the time."),
         "small": ("주문서도, 요리도, 도구 사용도 — 멀쩡한 날에도 적어둬요.", "The order, the dish, the tool use — written down even on a perfectly ordinary day."),
         "tricks": (4, [
             (icon('<rect x="8" y="14" width="30" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 22 h18 M14 28 h12" stroke="#142033" stroke-width="2.5"/><path d="M44 10 H54 V54 H44" stroke="var(--accent)" stroke-width="4" fill="none"/>'),
              ("주문서 적어둬요", "Log every prompt"), ("들어온 글자 그대로요", "exactly as it came in"), "calm"),
             (icon('<ellipse cx="32" cy="38" rx="22" ry="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="30" r="10" fill="var(--accent)"/><path d="M44 10 H54 V54 H44" stroke="var(--accent)" stroke-width="4" fill="none"/>'),
              ("나간 요리도 적어둬요", "Log every response"), ("어떤 답이 나갔는지도요", "and what answer went out")),
             (icon('<rect x="4" y="22" width="40" height="22" rx="2" fill="#5A3B22"/><rect x="8" y="14" width="10" height="8" rx="2" fill="#8B5E3C"/><circle cx="13" cy="33" r="2.5" fill="#E9B44C"/><path d="M48 10 H58 V54 H48" stroke="var(--accent)" stroke-width="4" fill="none"/>'),
              ("도구 사용도 적어둬요", "Log every tool use"), ("칼서랍 꺼낸 것도요", "even opening the knife drawer"), "warm"),
             (icon('<circle cx="24" cy="24" r="14" fill="none" stroke="#E9B44C" stroke-width="5"/><circle cx="24" cy="24" r="4" fill="#E9B44C"/><rect x="40" y="38" width="16" height="14" rx="3" fill="var(--good)"/>'),
              ("누가 언제 봤는지도요", "Log who looked, and when"), ("장부도 지켜봐야 해요", "the logbook itself gets watched too")),
         ])},
        {"svg": P4, "alt": ("평소엔 장부가 조용히 쌓이다가, 비상벨이 울리면 위생 검사관이 그 장부를 펼쳐 봄", "The logbook normally piles up quietly, but when the emergency bell rings, the inspector opens it up"),
         "caption": ("평소엔 조용히 쌓이다가, 벨이 울리면 그 장부를 펼쳐요.", "It quietly piles up, normally — then when the bell rings, you open it."),
         "small": ("그 전에 쌓인 장부를 펼쳐서 정확히 뭐가 있었는지 찾아요.", "The inspector opens that logbook to find out exactly what happened before.")},
        {"svg": P5, "alt": ("왼쪽: 사장님이 영원히 쌓아둔 장부 앞에서 비용과 위험을 걱정함. 오른쪽: 사고 대응·관측 가능성과 다른 점을 적은 규칙판", "Left: a worried manager in front of a logbook kept forever, fretting over cost and risk. Right: a board listing how this differs from incident response and observability"),
         "caption": ("영원히 쌓아두면 그것도 비용이고 위험이에요 — 사고 대응과 다르고, 관측 가능성과도 달라요.", "Keeping it all forever is itself a cost and a risk — different from incident response, and different from observability too."),
         "small": ("이 기록들이 모여, 다음엔 더 나은 가드레일과 규칙을 만드는 재료가 돼요.", "These records pile up and become the material for a better guardrail and a better rule, next time.")},
    ],
    "summary": (("<b>감사 로그</b> = 멀쩡한 날에도 <b>주문·요리·도구 사용</b>을 계속 적어두는 장부. 사고가 나면 이 장부를 펼쳐 보고, 다음엔 더 나은 <b>가드레일</b>을 만드는 재료가 돼요.",
                 "<b>Audit log</b> = a logbook that keeps writing down the <b>order, the dish, and the tool use</b> — even on an ordinary day. When an incident hits, this is the book you open — and it becomes the material for a better <b>guardrail</b> next time."),
                ("AI 감사 로그(Audit log)는 LLM·에이전트의 입력(프롬프트)·출력·도구 호출·접근 기록을 지속적으로 남기는 일이에요. 사고 대응(aiincident)이 '사고가 났을 때' 쓰는 절차라면, 감사 로그는 '사고가 나기 전부터' 평소에 계속 쌓아두는 재료예요. 일반 시스템 관측(observability)과 달리 AI 고유의 행동·출력 내용을 기록 대상으로 삼고, 보관 기간과 민감정보 가리기(레덕션)를 함께 설계해야 비용과 프라이버시 문제를 피할 수 있어요.",
                 "An AI audit log is the continuous record of an LLM or agent's inputs (prompts), outputs, tool calls, and access. Where incident response (aiincident) is the procedure you run once something has gone wrong, the audit log is the material that was already accumulating beforehand. Unlike general system observability, it targets the AI's own behavior and output content — and it needs a retention period and redaction of sensitive data designed in from the start, to avoid runaway cost and privacy risk.")),
    "glossary": [
        ("감사 로그", "Audit log", ("매일 계속 적어두는 주문 기록 장부.", "The order logbook you keep writing, every single day."), ("사고가 나기 전부터 쌓여 있어야 쓸모가 있어요.", "Only useful if it was already piling up before the incident.")),
        ("AI 사고 대응과의 차이", "Difference from incident response", ("벨이 울릴 때만 쓰는 것과, 평소에 계속 쓰는 것의 차이.", "The difference between writing only when the bell rings, and writing all the time."), ('사고 대응은 바로 앞 페이지예요. → <a href="aiincident-ko.html">울리는 비상벨</a>', 'Incident response is the page right before this one. → <a href="aiincident-en.html">The Bell That Rings</a>')),
        ("관측 가능성과의 차이", "Difference from observability", ("시스템 숫자를 보는 것과, AI의 말·행동을 적어두는 것의 차이.", "The difference between watching system numbers and writing down what the AI said and did."), ('일반 시스템 관측은 다른 세계 이야기예요. → <a href="observability-ko.html">세 가지로 들여다보기</a>', 'General system observability is a different world\'s story. → <a href="observability-en.html">Looking In Three Different Ways</a>')),
        ("도구 사용 기록", "Tool-call logging", ("칼서랍에서 뭘 꺼냈는지도 같이 적어둬요.", "Writing down what was taken out of the knife drawer, too."), ('도구 호출 자체는 다른 개념이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'Tool calling itself is a separate concept. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("보관 기간", "Retention period", ("오래된 장부는 지우기로 정해둔 기한.", "The deadline you set in advance for deleting old entries."), ("다 쌓아두면 그것도 비용이고 위험이에요.", "Keeping everything forever is itself a cost and a risk.")),
        ("가리기(레덕션)", "Redaction", ("장부에 적을 때 비밀은 가리는 것.", "Masking the secrets before they go into the logbook."), ('개인정보 보호와 바로 이어져요. → <a href="aiprivacy-ko.html">AI 프라이버시가 뭐예요?</a>', 'Directly tied to privacy protection. → <a href="aiprivacy-en.html">What is AI Privacy?</a>')),
        ("규정 준수 증빙", "Compliance evidence", ("\"우리가 지켰어요\"를 보여줄 증거.", "The proof you show to say \"we followed the rules.\""), ('이 장부가 바로 그 증거예요. → <a href="compliance-ko.html">컴플라이언스가 뭐예요?</a>', 'This logbook is exactly that evidence. → <a href="compliance-en.html">What is Compliance?</a>')),
        ("다음 가드레일의 재료", "Material for the next guardrail", ("오늘의 기록이 내일의 울타리를 만들어요.", "Today's record becomes tomorrow's fence."), ('처음 이야기의 \'계속 지켜보고 또 지키기\'가 바로 이 장부로 이어져요. → <a href="guardrail-ko.html">울타리</a> · <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'The opening story\'s "watching and defending, again and again" comes full circle in this logbook. → <a href="guardrail-en.html">The Fence</a> · <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
    ],
}
