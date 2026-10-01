from _draw import *
from _world import *

# 1. 창고엔 막 들어왔는데, 창구 재고판은 아직 옛 숫자예요
P1 = svg(320, sky(320)
         + shed(130, 260, 0.7, label_text="⟦방금 들어왔어요|just arrived⟧")
         + person(230, 204, s=0.5, face=SMILE, **MECHANIC) + bubble(150, 120, 180, 40, "⟦방금 들어왔는데…|it just came in…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + board(410, 90, 190, 100, "⟦재고판|STOCK BOARD⟧", ("⟦매진|sold out⟧",), 1.0, hl=0)
         + person(650, 204, s=0.5, face=FROWN, hat=FOLK[2][0], shirt=FOLK[2][1]) + bubble(605, 130, 150, 40, "⟦아까는 매진이라며요?|you said it was sold out?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦창고엔 막 들어왔는데, 창구 재고판은 아직 옛 숫자예요|new stock just arrived, but the counter's board still shows the old number⟧", 12, "var(--ink)"))

# 2. 왜: 복제본끼리 맞추는 데 아주 잠깐 시간이 걸려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(90, 80, 230, 110, "⟦창구 A 재고판|COUNTER A⟧", ("⟦매진|sold out⟧",), 1.0, hl=0)
         + board(440, 80, 230, 110, "⟦창구 B 재고판|COUNTER B⟧", ("⟦5개 남음|5 left⟧",), 1.0, hl=0)
         + '<path d="M320 130 L440 130" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M420 120 l20 10 l-20 10" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + label(380, 60, "⟦아직 맞춰지는 중…|still catching up…⟧", 12, "var(--muted)")
         + label(380, 280, "⟦복제본끼리 맞추는 데 아주 잠깐 시간이 걸려요|syncing the copies to match takes a brief moment⟧", 12, "var(--bad)"))

# 3. 조금 기다리면 결국엔 다 같은 숫자가 돼요 (hero)
P3 = svg(360, sky(360)
         + board(80, 110, 230, 120, "⟦창구 A|COUNTER A⟧", ("⟦매진 (옛 숫자)|sold out (old)⟧",), 1.0, hl=0)
         + '<path d="M330 170 L430 170" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M410 160 l20 10 l-20 10" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(380, 145, "⟦조금만 기다리면|wait just a little⟧", 12, "var(--muted)")
         + board(450, 110, 230, 120, "⟦창구 A|COUNTER A⟧", ("⟦5개 남음 (맞음)|5 left (matches)⟧",), 1.0)
         + person(190, 238, s=0.55, face=EYES, **OPERATOR) + person(560, 238, s=0.55, face=SMILE, **OPERATOR)
         + label(380, 340, "⟦바로 안 맞아도 조금만 기다리면 결국엔 다 같은 숫자가 돼요|even if it's off at first, wait a little and it ends up matching⟧", 13, "var(--ink)", cls="d"))

# 4. 시간선: t=0 갱신 → t=1 아직 옛값 → t=3 맞춰짐
P4 = svg(300, sky(300)
         + board(40, 60, 220, 100, "⟦t=0 창고 갱신|t=0 update⟧", ("⟦5개 남음|5 left⟧",), 0.9)
         + board(280, 60, 220, 100, "⟦t=1 창구 A|t=1 counter A⟧", ("⟦매진 (옛값)|sold out (stale)⟧",), 0.9, hl=0)
         + board(520, 60, 220, 100, "⟦t=3 창구 A|t=3 counter A⟧", ("⟦5개 남음 (맞음)|5 left (matches)⟧",), 0.9)
         + '<path d="M260 110 L280 110" stroke="var(--muted)" stroke-width="3"/><path d="M500 110 L520 110" stroke="var(--muted)" stroke-width="3"/>'
         + label(380, 270, "⟦시간이 조금 지나야 다 같은 숫자가 돼요|it takes a little time before every number matches⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: '결국엔'이 얼마나 걸리는지 모르면 더 헷갈려요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + board(270, 70, 220, 110, "⟦약속|OUR PROMISE⟧", ("⟦보통 3초 안에 맞춰요|usually matches within 3s⟧", "⟦그 전엔 조금 다를 수 있어요|may briefly differ before that⟧"), 1.0)
         + person(140, 184, s=0.5, face=FROWN, **MANAGER) + bubble(40, 100, 190, 40, "⟦대체 언제 맞는 거예요?|so when does it actually match?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦'결국엔'이 얼마나 걸리는지 모르면 손님이 더 헷갈려요 — 그래서 시간 약속이 필요해요|without knowing how long 'eventually' takes, guests get more confused — so you promise a time⟧", 12, "var(--ink)"))

CASUAL_I = icon('<rect x="8" y="14" width="48" height="34" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M16 24 h32 M16 32 h24" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><circle cx="48" cy="40" r="3" fill="var(--good)"/>')
MONEYX_I = icon('<circle cx="32" cy="32" r="20" fill="var(--bad)"/><text x="32" y="40" font-size="22" font-weight="700" text-anchor="middle" fill="#FFF8E7">₩</text><path d="M12 12 L52 52" stroke="#FFF8E7" stroke-width="5" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/><path d="M32 18 V32 L44 40" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
TALK_I = icon('<path d="M8 10 h40 a6 6 0 0 1 6 6 v20 a6 6 0 0 1 -6 6 h-24 l-10 10 v-10 h-6 a6 6 0 0 1 -6 -6 v-20 a6 6 0 0 1 6 -6z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="20" cy="26" r="3" fill="var(--muted)"/><circle cx="32" cy="26" r="3" fill="var(--muted)"/><circle cx="44" cy="26" r="3" fill="var(--muted)"/>')

PAGE = {
    "slug": "eventualconsistency", "order": 11,
    "title": ("조금 늦게 맞춰지는 재고판", "The Stock Board That Catches Up a Little Late"),
    "h1": ("<em>최종 일관성</em>이 뭐예요?", "What is <em>Eventual Consistency</em>?"),
    "sub": ("최종 일관성을, 창고에 막 들어온 물건이 재고판에 조금 늦게 반영되는 이야기로 풀어봤어요.",
            "Eventual consistency, told as a story about a stock board that takes a moment to catch up with the warehouse."),
    "panels": [
        {"svg": P1, "alt": ("창고엔 물건이 막 들어왔는데 재고판은 아직 매진으로 표시되어 손님이 놀람", "New stock just arrived at the warehouse, but the board still says sold out, confusing a guest"),
         "caption": ("창고엔 막 들어왔는데, 창구 재고판은 아직 옛 숫자예요.", "New stock just arrived, but the counter's board still shows the old number."),
         "small": ("손님이 '아까는 매진이라며요?' 하고 물어요.", "A guest asks, 'you said it was sold out?'")},
        {"svg": P2, "alt": ("두 창구의 재고판이 서로 다른 숫자를 보여주고, 그 사이에 아직 도착하지 않은 동기화 화살표", "Two counter boards show different numbers, with a sync arrow still on its way between them"),
         "caption": ("왜: 복제본끼리 맞추는 데 아주 잠깐 시간이 걸려요.", "Why: syncing the copies to match takes a brief moment."),
         "small": ("복제본끼리 맞추는 데 아주 잠깐 시간이 걸려요.", "Syncing the replicas takes a brief moment.")},
        {"svg": P3, "hero": True, "alt": ("옛 숫자를 보여주던 재고판이 화살표를 따라 결국 맞는 숫자로 바뀜", "A board showing the old number eventually changes, along an arrow, to the matching number"),
         "caption": ("바로 안 맞아도 조금만 기다리면 결국엔 다 같은 숫자가 돼요.", "Even if it's off at first, wait a little and it ends up matching."),
         "small": ("그 사이엔 살짝 다를 수 있어요.", "In between, it can be slightly different."),
         "tricks": (4, [
             (CASUAL_I, ("급하지 않은 정보에 써요", "Use it for low-stakes info"), ("안내판 숫자 같은 곳이요", "like numbers on a display board"), "calm"),
             (MONEYX_I, ("돈 계산엔 안 써요", "Don't use it for money"), ("→ 강한 일관성을 써요", "use strong consistency instead")),
             (CLOCK_I, ("얼마나 늦는지 재둬요", "Measure how late it gets"), ("복제 지연을 알아야 해요", "you need to know the replication lag"), "warm"),
             (TALK_I, ("손님에게 미리 안내해요", "Tell guests up front"), ("'방금 바뀐 거라 조금 늦을 수 있어요'", "'it just changed, so it may lag a bit'")),
         ])},
        {"svg": P4, "alt": ("시간선 t=0 창고 갱신, t=1 창구 A 아직 옛값, t=3 창구 A도 맞춰짐", "Timeline: t=0 warehouse updates, t=1 counter A still stale, t=3 counter A matches"),
         "caption": ("시간선: t=0 갱신 → t=1 아직 옛값 → t=3 맞춰짐.", "Timeline: t=0 update → t=1 still stale → t=3 matches."),
         "small": ("시간이 조금 지나야 다 같은 숫자가 돼요.", "It takes a little time before every number matches.")},
        {"svg": P5, "alt": ("'우리끼리 약속: 보통 3초 안에 맞춰요' 안내판 옆에서 손님이 언제 맞는지 묻는 모습", "Beside a promise board saying 'usually matches within 3s', a guest asks when it will actually match"),
         "caption": ("'결국엔'이 얼마나 걸리는지 모르면 더 헷갈려요.", "Without knowing how long 'eventually' takes, guests get more confused."),
         "small": ("그래서 시간 약속이 필요해요.", "So you need to promise a time.")},
    ],
    "summary": (("<b>최종 일관성</b> = 복제본끼리 <b>바로는 안 맞아도</b>, 조금 기다리면 <b>결국엔 같은 값</b>이 되는 약속. 그 사이엔 <b>살짝 다를 수 있어요</b>.",
                 "<b>Eventual consistency</b>: replicas won't match <b>right away</b>, but wait a little and they <b>end up the same</b> — in between, they can briefly <b>differ</b>."),
                ("강한 일관성(모든 복제본이 늘 같은 값)과 대비되는 개념이에요. 복제 지연(replication lag)이 얼마나 되는지 알아두면, 손님에게 '언제쯤 맞는지' 안내할 수 있어요. 돈을 다루는 곳에는 보통 안 쓰고, 캐시나 조회수 같은 급하지 않은 곳에 써요.",
                 "This contrasts with strong consistency, where every replica always matches. Knowing the replication lag lets you tell guests when things will line up. It's usually avoided for money, and used instead for low-stakes things like caches or view counts.")),
    "glossary": [
        ("최종 일관성", "Eventual Consistency", ("조금 늦게라도 결국 맞춰지는 약속.", "The promise that things match up eventually, even if a bit late."), ("급하지 않은 정보에 주로 써요.", "Mostly used for low-stakes information.")),
        ("강한 일관성", "Strong Consistency", ("늘 최신 정답만 보여주는 약속.", "Always showing the latest, correct answer."), ('돈 다루는 곳에선 이걸 써요. → <a href="captheorem-ko.html">정확함과 항상 열림, 둘 다는 못 가져요</a>', 'Used wherever money is involved. → <a href="captheorem-en.html">you can\'t have both correctness and always-open</a>')),
        ("복제 지연", "Replication Lag", ("복제본이 원본을 따라잡는 데 걸리는 시간.", "The time it takes a replica to catch up to the original."), ('→ <a href="replication-ko.html">손님 명부를 두 창고에 똑같이</a>', '→ <a href="replication-en.html">keeping the same guest list in two warehouses</a>')),
        ("읽기-내-쓰기 일관성", "Read-your-writes Consistency", ("적어도 내가 바꾼 건 나한테는 바로 보이는 약속.", "The promise that at least your own change shows up for you right away."), ("완전한 최종 일관성보다 손님 혼란이 적어요.", "Less confusing for guests than plain eventual consistency.")),
        ("벡터 시계", "Vector Clock", ("어느 복제본이 더 최신인지 가리는 이름표 같은 도구.", "A label-like tool for telling which replica is more recent."), ("자세히는 다른 자료에서 다뤄요 — 이름만 알아둬요.", "The details live elsewhere — just know the name for now.")),
        ("충돌 해결", "Conflict Resolution", ("서로 다른 값이 생겼을 때 하나로 정리하는 규칙.", "The rule for settling conflicting values into one."), ("나중 값 우선, 사람이 직접 고르기 등 방법이 여러 가지예요.", "Last-write-wins, manual merge, and others are common approaches.")),
        ("캐시", "Caching", ("자주 묻는 질문을 미리 적어둔 메모판.", "A memo board with answers written down in advance."), ('→ <a href="caching-ko.html">자주 묻는 질문 미리 적어둔 메모판</a>', '→ <a href="caching-en.html">the memo board with answers written in advance</a>')),
        ("CAP 정리", "CAP Theorem", ("최종 일관성이 가용성 쪽을 택했을 때 생기는 결과예요.", "What you get when CAP's trade-off picks availability."), ('→ <a href="captheorem-ko.html">정확함과 항상 열림, 둘 다는 못 가져요</a>', '→ <a href="captheorem-en.html">you can\'t have both correctness and always-open</a>')),
    ],
}
