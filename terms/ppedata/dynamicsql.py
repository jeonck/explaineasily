from _draw import *
from _world import *

# 1. 요청마다 조건이 다 달라요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.7, face=EYES, **DRIVER) + bubble(40, 80, 170, 34, "⟦구역만요|just by zone⟧", 10.5, "var(--panel)", "var(--line)", "bottom")
         + person(380, 150, s=0.7, face=EYES, **DRIVER) + bubble(290, 80, 190, 34, "⟦색상이랑 구역이요|color and zone⟧", 10.5, "var(--panel)", "var(--line)", "bottom")
         + person(620, 150, s=0.7, face=EYES, **DRIVER) + bubble(530, 80, 210, 34, "⟦아무 조건 없이 전부요|no filter, everything⟧", 10.5, "var(--panel)", "var(--line)", "bottom")
         + label(380, 260, "⟦요청마다 찾는 조건이 다 달라요|every request asks for a different combination of filters⟧", 13, "var(--ink)"))

# 2. 고정 양식만으로는 다 못 찍어둬요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(240, 150, s=0.85, face=SWEAT + EYES, **PACKER)
         + receipt(130, 110, 0.7, text="⟦구역만|zone only⟧") + receipt(220, 130, 0.7, text="⟦색상만|color only⟧") + receipt(310, 110, 0.7, text="⟦둘다|both⟧")
         + label(240, 240, "⟦조합마다 미리 다 찍어둘 순 없어요|you can't pre-print a form for every combination⟧", 12, "var(--bad)")
         + label(560, 150, "⟦...그래서 몇 개는 못 쓰는 양식이 돼요|...so some pre-printed forms go unused⟧", 11, "var(--muted)"))

# 3. 동적 SQL = 그 자리에서 조립하는 주문서 (hero)
P3 = svg(340, sky(340, ground=False)
         + person(260, 160, s=0.9, face=EYES, **PACKER)
         + receipt(460, 170, 1.1, text="⟦B구역 + 빨강|zone B + red⟧")
         + label(380, 30, "⟦동적 SQL = 요청 들을 때마다 그 자리에서 조립하는 주문서|Dynamic SQL = assembling the order slip on the spot, for whatever was asked⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦조건이 있으면 넣고, 없으면 빼고, 조립해서 실행해요|add a condition if it's there, skip it if not, then run it⟧", 12, "var(--muted)"))

# 4. 조립 과정: 조건을 하나씩 끼워넣기
P4 = svg(320, sky(320, ground=False)
         + receipt(130, 160, 1.1, text="⟦기본 틀|base slip⟧")
         + label(240, 155, "+", 26, "var(--muted)", cls="d")
         + '<rect x="280" y="130" width="90" height="56" rx="3" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/>' + label(325, 162, "⟦구역=B|zone=B⟧", 10, "#142033")
         + label(390, 155, "+", 26, "var(--muted)", cls="d")
         + '<rect x="420" y="130" width="100" height="56" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>' + label(470, 162, "⟦색상=빨강|color=red⟧", 10, "#142033")
         + label(545, 155, "→", 30, "var(--muted)", cls="d")
         + receipt(630, 160, 1.1, text="⟦완성!|done!⟧")
         + label(380, 280, "⟦조건이 있을 때만 그 조각을 덧붙여요|only add a piece when that condition is actually present⟧", 12, "var(--ink)"))

# 5. 빈칸을 안전하게 채워야 해요 (SQL 인젝션 위험)
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **PACKER) + receipt(190, 230, 0.6, text="⟦빈칸에 안전하게 끼우기|slot it in safely⟧")
         + person(570, 150, s=0.8, face=FROWN, **DRIVER) + receipt(570, 230, 0.6, text="⟦글자를 그대로 붙여넣기|pasting text raw⟧", void=True)
         + label(380, 282, "⟦글자를 그대로 이어붙이면 엉뚱한 지시가 끼어들 수 있어요(SQL 인젝션)|pasting text raw can let in an unwanted instruction (SQL injection)⟧", 11.5, "var(--ink)", cls="d"))

ASSEMBLE_I = icon('<rect x="14" y="30" width="36" height="24" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="10" width="24" height="14" rx="2" fill="var(--good)"/><path d="M32 24 v6" stroke="var(--muted)" stroke-width="2"/>')
IF_I = icon('<path d="M20 12 L44 12 L32 30 Z" fill="var(--accent)"/><rect x="24" y="36" width="16" height="16" rx="2" fill="var(--good)"/>')
BIND_I = icon('<rect x="12" y="24" width="18" height="18" rx="2" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="34" y="24" width="18" height="18" rx="2" fill="var(--good)"/><path d="M30 33 h4" stroke="var(--muted)" stroke-width="3"/>')
RUN_I = icon('<path d="M18 12 L48 32 L18 52 Z" fill="var(--accent)"/>')

PAGE = {
    "slug": "dynamicsql", "order": 12,
    "title": ("그 자리에서 맞춤 주문서 쓰기", "Writing a Custom Order Slip on the Spot"),
    "h1": ("<em>동적 SQL</em>이 뭐예요?", "What is <em>Dynamic SQL</em>?"),
    "sub": ("동적 SQL을, 손님 요청에 따라 그 자리에서 조건을 끼워 넣어 주문서를 조립하는 포장 담당 이야기로 풀어봤어요.",
            "Dynamic SQL, told as a story about a warehouse worker assembling the order slip on the spot, adding whatever conditions each request actually needs."),
    "panels": [
        {"svg": P1, "alt": ("세 명의 배송 기사가 각자 다른 조건(구역만, 색상과 구역, 조건 없음)을 요청함", "Three drivers each ask for a different combination — zone only, color and zone, or no filter at all"),
         "caption": ("요청마다 찾는 조건이 다 달라요.", "Every request asks for a different combination of filters."),
         "small": ("미리 정해둔 양식 하나로는 다 감당 못 해요.", "One fixed form can't cover them all.")},
        {"svg": P2, "alt": ("포장 담당이 땀을 흘리며 조합별 고정 양식들을 쌓아두지만 다 못 찍어둠", "The worker sweats, stacking pre-printed forms for each combination but unable to cover them all"),
         "caption": ("고정 양식만으로는 조합을 다 미리 찍어둘 수 없어요.", "Fixed forms alone can't be pre-printed for every combination."),
         "small": ("조합이 늘어날수록 못 쓰는 양식만 쌓여요.", "More combinations just means more unused forms piling up.")},
        {"svg": P3, "hero": True, "alt": ("포장 담당이 손님 요청을 듣고 그 자리에서 구역과 색상 조건이 적힌 주문서를 완성함", "The worker listens to the request and assembles a slip with zone and color conditions right on the spot"),
         "caption": ("동적 SQL은 요청 들을 때마다 그 자리에서 조립하는 주문서예요.", "Dynamic SQL assembles the order slip on the spot, for whatever was asked."),
         "small": ("조건이 있으면 넣고, 없으면 빼고, 조립해서 실행해요.", "Add a condition if it's there, skip it if not, then run it."),
         "tricks": (4, [
             (ASSEMBLE_I, ("요청 들을 때마다 조립", "Build it at request time"), ("실행 직전에 만들어요", "assembled right before it runs")),
             (IF_I, ("조건 있으면 추가", "Add a piece if present"), ("WHERE 조각을 덧붙여요", "an extra WHERE clause"), "calm"),
             (BIND_I, ("빈칸은 안전하게 끼우기", "Slot values in safely"), ("파라미터 바인딩이에요", "parameter binding")),
             (RUN_I, ("조립 끝나면 실행", "Run once assembled"), ("완성된 문장을 실행해요", "executes the finished statement"), "warm"),
         ])},
        {"svg": P4, "alt": ("기본 틀에 구역=B, 색상=빨강 조각을 차례로 덧붙여 완성된 주문서를 만드는 과정", "Base slip plus zone=B plus color=red pieces, assembled step by step into a finished slip"),
         "caption": ("조건이 있을 때만 그 조각을 덧붙여요.", "Only add a piece when that condition is actually present."),
         "small": ("기본 틀 + 조건 조각들 = 완성된 문장.", "Base slip + condition pieces = the finished statement.")},
        {"svg": P5, "alt": ("왼쪽: 빈칸에 안전하게 값을 끼우는 포장 담당. 오른쪽: 글자를 그대로 이어붙여 찢어진 주문서를 든 배송 기사", "Left: the worker safely slots a value in. Right: a driver holds a torn slip from pasting text raw"),
         "caption": ("빈칸을 안전하게 채워야 해요.", "The blanks need to be filled in safely."),
         "small": ("글자를 그대로 이어붙이면 엉뚱한 지시가 끼어들 수 있어요(SQL 인젝션).", "Pasting text in raw can let an unwanted instruction slip in (SQL injection).")},
    ],
    "summary": (("<b>동적 SQL</b>은 실행 시점에 조건에 따라 <b>그 자리에서 SQL 문장을 조립</b>하는 방식이에요. 미리 고정해 둔 정적 SQL과 반대예요.",
                 "<b>Dynamic SQL</b> assembles a SQL statement <b>on the spot, at run time</b>, based on whatever conditions apply — the opposite of a fixed, pre-written static SQL."),
                ("정적 SQL은 컴파일(또는 저장 프로시저 등록) 시점에 문장이 고정되어 실행 계획을 재사용하기 쉬운 반면, 동적 SQL은 검색 조건이 가변적인 화면(선택적 필터가 많은 조회 화면 등)에 적합해요. 다만 문자열을 그대로 이어붙이면 SQL 인젝션에 취약해지므로, 반드시 파라미터 바인딩으로 값을 안전하게 끼워 넣어야 해요.",
                 "Static SQL is fixed at compile (or stored-procedure registration) time, so its execution plan is easy to reuse. Dynamic SQL instead suits screens with variable, optional filters. But concatenating raw strings opens the door to SQL injection — values must always be slotted in safely through parameter binding.")),
    "glossary": [
        ("정적 SQL", "Static SQL", ("미리 찍어둔 고정 양식.", "A pre-printed, fixed form."), ("실행 계획을 재사용하기 쉬워요.", "Easy to reuse the execution plan.")),
        ("동적 SQL", "Dynamic SQL", ("그 자리에서 조립하는 양식.", "A form assembled on the spot."), ("조건이 가변적인 화면에 맞아요.", "Suits screens with variable filters.")),
        ("파라미터 바인딩", "Parameter Binding", ("값만 빈칸에 안전하게 끼우기.", "Safely slotting just the value into a blank."), ("문자열을 직접 이어붙이지 않아요.", "Never concatenates raw text.")),
        ("SQL 인젝션", "SQL Injection", ("빈칸에 엉뚱한 지시가 끼어드는 일.", "An unwanted instruction slipping into the blank."), ('보안 세계에서 자세히 다뤄요. → <a href="injection-ko.html">끼어드는 나쁜 지시</a>', 'Covered in depth in the security world. → <a href="injection-en.html">the bad instruction that sneaks in</a>')),
        ("PREPARE/EXECUTE", "PREPARE/EXECUTE", ("양식을 미리 맞춰두고 반복 실행.", "Fitting the form once, then running it repeatedly."), ("같은 모양 요청이 많을 때 빨라요.", "Faster when many requests share the same shape.")),
        ("저장 프로시저 내 동적 SQL", "Dynamic SQL in Stored Procedures", ("프로시저 안에서도 조립할 수 있어요.", "Can be assembled even inside a procedure."), ("실행 권한 관리가 더 까다로워요.", "Execution-permission handling gets trickier.")),
        ("실행계획 재사용", "Plan Cache Reuse", ("같은 모양 양식은 다시 안 그려요.", "A form of the same shape isn't redrawn."), ("동적 SQL은 이 재사용이 어려워요.", "Dynamic SQL makes this reuse harder.")),
        ("ORM 동적 쿼리 빌더", "ORM Query Builder", ("코드로 주문서를 짜 맞추는 도구.", "A tool that assembles the slip in code."), ("내부적으로 동적 SQL을 만들어요.", "Generates dynamic SQL under the hood.")),
    ],
}
