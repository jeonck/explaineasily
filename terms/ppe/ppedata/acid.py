from _draw import *
from _world import *

# 1. 문제: 출납 전표 작업이 절반만 되고 멈췄어요
P1 = svg(320, sky(320)
         + person(170, 150, s=0.8, face=SWEAT + EYES, **PACKER)
         + receipt(380, 160, 0.9, text="⟦상자 꺼냄 ✓, 장부 기록 ✗|box taken ✓, ledger write ✗⟧")
         + label(380, 260, "⟦정전이 나서 절반만 처리됐어요|the power cut out — only half got done⟧", 12, "var(--bad)")
         + label(380, 300, "⟦상자는 없어졌는데 장부엔 그대로예요|the box is gone but the ledger still shows it⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 절반짜리 작업은 믿을 수 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + receipt(240, 150, 0.9, void=True, text="⟦반쪽짜리 전표|a half-done receipt⟧")
         + person(480, 150, s=0.8, face=FROWN, **AUDITOR)
         + label(380, 250, "⟦다음에 누가 봐도 믿을 수 없는 장부가 돼요|the next person can't trust the ledger either⟧", 12, "var(--ink)"))

# 3. hero: ACID = 출납 전표가 지키는 네 가지 약속
ALL_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
RULE_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 30 h20 M22 40 h12" stroke="#142033" stroke-width="2.5"/>')
CURTAIN_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M32 10 V54" stroke="var(--accent)" stroke-width="3"/>')
STAMP_I = icon('<circle cx="32" cy="30" r="20" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 30 l8 8 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><rect x="24" y="50" width="16" height="8" fill="#8B5E3C"/>')

P3 = svg(340, sky(340)
         + person(280, 120, s=0.9, face=EYES, **MANAGER)
         + receipt(480, 190, 0.9)
         + label(380, 30, "⟦ACID = 출납 전표가 반드시 지키는 네 가지 약속|ACID = the four promises every receipt must keep⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦네 가지를 다 지켜야 진짜 믿을 수 있는 전표예요|only a receipt keeping all four can truly be trusted⟧", 12, "var(--muted)"))

# 4. A C I D 네 글자 설명
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦A-C-I-D 네 글자|the four letters A-C-I-D⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + _row(80, "⟦Atomicity — 전부 되거나 전부 취소|atomicity — all or nothing⟧", "⟦반쪽짜리 없음|no half-done work⟧")
         + _row(116, "⟦Consistency — 장부 규칙을 안 어김|consistency — never breaks the rules⟧", "⟦규칙 위반 시 되돌림|rolls back on violation⟧")
         + _row(152, "⟦Isolation — 남의 작업에 영향 안 줌|isolation — doesn't leak into others' work⟧", "⟦격리 수준으로 조절|tuned by isolation level⟧")
         + _row(188, "⟦Durability — 도장 찍히면 안 사라짐|durability — once stamped, it stays⟧", "⟦정전에도 보존|survives even a power cut⟧"))

# 5. 한계: ACID를 다 지키려면 느려질 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + receipt(190, 150, 0.9) + label(190, 240, "⟦ACID를 다 지키면 믿을 수 있어요|fully ACID means you can trust it⟧", 11, "var(--ink)")
         + fastdesk(570, 150, 1.0) + label(570, 200, "⟦대신 특급 출고대처럼 빠르진 않아요|but it's not as fast as the express desk⟧", 11, "var(--ink)")
         + label(380, 270, "⟦안전과 속도는 종종 맞바꿔야 해요|safety and speed often trade off⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "acid", "order": 6,
    "title": ("출납 전표가 지키는 네 가지 약속", "The Four Promises a Receipt Keeps"),
    "h1": ("<em>트랜잭션과 ACID</em>가 뭐예요?", "What is <em>Transactions & ACID</em>?"),
    "sub": ("트랜잭션과 ACID를, 출납 전표가 반드시 지키는 네 가지 약속 이야기로 풀어봤어요.",
            "Transactions and ACID, told as a story about the four promises a receipt must keep."),
    "panels": [
        {"svg": P1, "alt": ("포장 담당이 정전으로 절반만 처리된 전표를 보고 진땀을 흘림", "A packer sweats over a receipt that's only half-processed because of a power cut"),
         "caption": ("정전이 나서 절반만 처리됐어요.", "The power cut out — only half got done."),
         "small": ("상자는 없어졌는데 장부엔 그대로예요.", "The box is gone but the ledger still shows it.")},
        {"svg": P2, "alt": ("무효 표시된 반쪽짜리 전표를 보고 감사원이 찡그림", "An auditor frowns at a voided, half-done receipt"),
         "caption": ("반쪽짜리 작업은 믿을 수 없어요.", "A half-done piece of work can't be trusted."),
         "small": ("다음에 누가 봐도 믿을 수 없는 장부가 돼요.", "The next person can't trust the ledger either.")},
        {"svg": P3, "hero": True, "alt": ("창고 관리자가 온전한 전표 한 장을 두고 네 가지 약속을 설명함", "A manager stands by a complete receipt, explaining the four promises"),
         "caption": ("ACID = 출납 전표가 반드시 지키는 네 가지 약속이에요.", "ACID is the four promises every receipt must keep."),
         "small": ("네 가지를 다 지켜야 진짜 믿을 수 있는 전표예요.", "Only a receipt keeping all four can truly be trusted."),
         "tricks": (4, [
             (ALL_I, ("Atomicity", "Atomicity"), ("전부 되거나 전부 취소돼요", "all or nothing"), "calm"),
             (RULE_I, ("Consistency", "Consistency"), ("장부 규칙을 어기지 않아요", "never breaks the ledger's rules")),
             (CURTAIN_I, ("Isolation", "Isolation"), ("남의 작업에 섞이지 않아요", "doesn't bleed into others' work"), "warm"),
             (STAMP_I, ("Durability", "Durability"), ("도장 찍히면 사라지지 않아요", "once stamped, it stays")),
         ])},
        {"svg": P4, "alt": ("Atomicity, Consistency, Isolation, Durability 네 글자를 설명하는 표", "A table explaining the four letters: atomicity, consistency, isolation, durability"),
         "caption": ("ACID는 네 글자의 약속이에요.", "ACID is a promise spelled out in four letters."),
         "small": ("Isolation은 격리 수준으로 세밀하게 조절해요.", "Isolation is fine-tuned via isolation levels.")},
        {"svg": P5, "alt": ("왼쪽: 온전한 전표가 믿을 수 있음을 보여줌. 오른쪽: 특급 출고대가 더 빠르지만 ACID를 다 지키진 않음", "Left: a full receipt shows it can be trusted. Right: the express desk is faster but doesn't fully keep ACID"),
         "caption": ("ACID를 다 지키면 믿을 수 있지만, 느려질 수 있어요.", "Fully keeping ACID means trust, but can mean slower."),
         "small": ("안전과 속도는 종종 맞바꿔야 해요.", "Safety and speed often trade off.")},
    ],
    "summary": (("<b>ACID</b> = 출납 전표(트랜잭션)가 지켜야 할 <b>원자성·일관성·고립성·지속성</b> 네 가지 약속.",
                 "<b>ACID</b> is the four promises a receipt (transaction) must keep: <b>atomicity, consistency, isolation, durability</b>."),
                ("트랜잭션은 데이터베이스에서 더 이상 나눌 수 없는 작업 단위이고, ACID는 그 트랜잭션이 안전하게 처리되기 위한 네 가지 성질이에요. Atomicity(전부 성공 또는 전부 실패), Consistency(제약조건 유지), Isolation(동시 트랜잭션 간 간섭 차단), Durability(커밋 후 영구 반영)로, Isolation은 격리 수준으로 강도를 조절해요.",
                 "A transaction is an indivisible unit of work in a database, and ACID is the set of four properties that make it safe: Atomicity (all succeed or all fail), Consistency (constraints are preserved), Isolation (concurrent transactions don't interfere), and Durability (committed results persist permanently). Isolation's strength is tuned via isolation levels.")),
    "glossary": [
        ("트랜잭션", "Transaction", ("전표 한 장의 작업 단위.", "One receipt's unit of work."), ("더는 쪼갤 수 없는 최소 단위예요.", "The smallest unit that can't be split further.")),
        ("원자성(Atomicity)", "Atomicity", ("전부 되거나 전부 취소.", "All or nothing."), ("중간에 멈추는 상태가 없어요.", "No stopping halfway.")),
        ("일관성(Consistency)", "Consistency", ("장부 규칙을 어기지 않는 것.", "Never breaking the ledger's rules."), ("제약조건을 항상 지켜요.", "Always honors the constraints.")),
        ("고립성(Isolation)", "Isolation", ("남의 작업에 섞이지 않는 것.", "Not bleeding into someone else's work."), ('격리 수준으로 세밀하게 조절해요. → <a href="isolevel-ko.html">동시에 손댈 때 얼마나 가려 볼지</a>', 'Fine-tuned by isolation level. → <a href="isolevel-en.html">how much to hide when hands overlap</a>')),
        ("지속성(Durability)", "Durability", ("도장 찍히면 사라지지 않는 것.", "Once stamped, it never disappears."), ("정전이 나도 장부에 남아요.", "Survives even a power outage.")),
        ("병행제어", "Concurrency Control", ("동시에 손대도 안 부딪히게 막는 방법.", "The method that stops simultaneous edits colliding."), ('ACID의 I(고립성)를 실제로 구현하는 방법이에요. → <a href="concurrency-ko.html">동시에 안 부딪히는 규칙</a>', 'How isolation is actually implemented. → <a href="concurrency-en.html">the no-collision rule</a>')),
        ("인메모리 DB", "In-Memory DB", ("디스크 대신 바로 꺼내는 출고대.", "A desk that skips the deep shelf and serves from memory."), ('속도를 위해 지속성을 일부 타협하기도 해요. → <a href="inmemorydb-ko.html">특급 출고대</a>', 'Sometimes trades off durability for speed. → <a href="inmemorydb-en.html">the express pickup desk</a>')),
        ("NoSQL 모델링", "NoSQL Modeling", ("상자 모양에 맞춰 선반을 바꾸는 창고.", "A warehouse reshaping shelves to fit the box."), ('보통 ACID를 관계형 창고만큼 엄격히 지키지 않아요. → <a href="nosqltype-ko.html">자유로운 선반 창고</a>', "Usually doesn't keep ACID as strictly as the relational warehouse. → <a href=\"nosqltype-en.html\">the free-shelf warehouse</a>")),
    ],
}
