from _draw import *
from _world import *

# 1. 문제: 포장 담당과 배송 기사가 같은 상자를 동시에 만져요
P1 = svg(320, sky(320)
         + person(220, 150, s=0.8, face=EYES, **PACKER)
         + person(540, 150, s=0.8, face=SWEAT + EYES, **DRIVER)
         + box(380, 190, 0.8)
         + bubble(140, 54, 180, 36, "⟦상자 수량을 10으로 고칠게요|changing the box count to 10⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble(460, 54, 220, 36, "⟦어? 방금 본 숫자랑 다른데요?|wait, that's not the number I just saw⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦동시에 손대면 서로 다른 숫자를 봐요|touching it at the same time shows each a different number⟧", 13, "var(--bad)"))

# 2. 왜 어려운가: 세 가지 이상현상이 생겨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + receipt(190, 150, 0.8, void=True, text="⟦더티 리드|dirty read⟧")
         + receipt(380, 150, 0.8, void=True, text="⟦반복 불가 읽기|non-repeatable⟧")
         + receipt(570, 150, 0.8, void=True, text="⟦유령 읽기|phantom read⟧")
         + label(380, 250, "⟦규칙 없이 두면 세 가지 사고가 나요|without rules, three kinds of trouble happen⟧", 13, "var(--ink)"))

# 3. hero: 격리 수준 = 동시에 손댈 때 얼마나 엄격히 막을지 정하는 규칙
LOCK_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="#E9B44C" stroke="#8B5E3C" stroke-width="3"/><path d="M22 26 V18 a10 10 0 0 1 20 0 V26" stroke="#8B5E3C" stroke-width="5" fill="none"/>')
EYE_I = icon('<path d="M8 32 Q32 14 56 32 Q32 50 8 32 Z" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>')
GHOST_I = icon('<path d="M18 50 V26 a14 14 0 0 1 28 0 V50 l-6 -6 l-6 6 l-6 -6 l-6 6 z" fill="#C9D5E6" stroke="var(--muted)" stroke-width="2"/>')
SHIELD_I = icon('<path d="M32 6 L54 14 V32 C54 44 44 54 32 58 C20 54 10 44 10 32 V14 Z" fill="var(--good)"/>')

P3 = svg(340, sky(340)
         + person(380, 130, s=0.9, face=EYES, **AUDITOR)
         + receipt(220, 210, 0.6, text="⟦읽기|read⟧") + receipt(300, 210, 0.6, text="⟦쓰기|write⟧")
         + receipt(470, 210, 0.6, text="⟦읽기|read⟧") + receipt(560, 210, 0.6, text="⟦쓰기|write⟧")
         + label(380, 30, "⟦격리 수준 = 동시에 손댈 때 얼마나 엄격히 막을지 정하는 규칙|isolation level = how strictly to guard against touching it at once⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦엄격할수록 안전하지만, 느려질 수 있어요|stricter means safer, but can be slower⟧", 12, "var(--muted)"))

# 4. 네 단계 격리 수준
def _row(y, a, b):
    return label(220, y, a, 12, "var(--ink)", anchor="start") + label(560, y, b, 12, "var(--ink)", anchor="start")

P4 = svg(320, sky(320, ground=False)
         + label(380, 34, "⟦격리 수준 네 단계|four isolation levels⟧", 14, "var(--ink)", cls="d")
         + '<rect x="200" y="54" width="360" height="2" fill="var(--line)"/>'
         + _row(80, "⟦Read Uncommitted — 다 보임(더티 리드 O)|read uncommitted — sees everything, dirty reads allowed⟧", "⟦가장 느슨|loosest⟧")
         + _row(116, "⟦Read Committed — 확정된 것만|read committed — only confirmed writes⟧", "⟦더티 리드 막음|blocks dirty reads⟧")
         + _row(152, "⟦Repeatable Read — 같은 값 보장|repeatable read — guarantees same value⟧", "⟦반복 불가 읽기 막음|blocks non-repeatable reads⟧")
         + _row(188, "⟦Serializable — 차례로 처리한 것처럼|serializable — as if done one at a time⟧", "⟦가장 엄격|strictest⟧"))

# 5. 한계: 엄격할수록 기다리는 사람이 늘어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **AUDITOR) + label(190, 270, "⟦Serializable = 가장 안전|serializable: safest⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SWEAT + EYES, **DRIVER) + label(570, 270, "⟦대신 뒷사람이 오래 기다려요|but the next person waits longer⟧", 11, "var(--ink)")
         + label(380, 280, "⟦그래서 상황에 맞는 수준을 골라야 해요|so the right level has to fit the situation⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "isolevel", "order": 4,
    "title": ("동시에 손댈 때 얼마나 가려 볼지 정하는 규칙", "The Rule for How Much to Hide When Hands Overlap"),
    "h1": ("<em>트랜잭션 격리 수준</em>이 뭐예요?", "What is <em>Transaction Isolation Level</em>?"),
    "sub": ("격리 수준과 이상현상을, 같은 상자를 동시에 만지는 포장 담당과 배송 기사 이야기로 풀어봤어요.",
            "Isolation levels and anomalies, told as a story about a packer and a driver touching the same box at once."),
    "panels": [
        {"svg": P1, "alt": ("포장 담당과 배송 기사가 같은 상자를 동시에 고쳐 서로 다른 숫자를 봄", "A packer and a driver edit the same box at once and each sees a different number"),
         "caption": ("포장 담당과 배송 기사가 같은 상자를 동시에 만져요.", "A packer and a driver touch the same box at the same time."),
         "small": ("동시에 손대면 서로 다른 숫자를 봐요.", "Touching it at the same time shows each a different number.")},
        {"svg": P2, "alt": ("더티 리드, 반복 불가 읽기, 유령 읽기 세 장의 무효 전표", "Three voided receipts: dirty read, non-repeatable read, phantom read"),
         "caption": ("규칙 없이 두면 세 가지 사고가 나요.", "Without rules, three kinds of trouble happen."),
         "small": ("더티 리드·반복 불가 읽기·유령 읽기예요.", "Dirty reads, non-repeatable reads, and phantom reads.")},
        {"svg": P3, "hero": True, "alt": ("재고 감사원이 읽기·쓰기 전표들을 지켜보며 규칙을 정함", "An auditor watches over read/write receipts, setting the rule"),
         "caption": ("격리 수준 = 동시에 손댈 때 얼마나 엄격히 막을지 정하는 규칙이에요.", "Isolation level decides how strictly to guard against simultaneous touching."),
         "small": ("엄격할수록 안전하지만, 느려질 수 있어요.", "Stricter means safer, but can be slower."),
         "tricks": (4, [
             (LOCK_I, ("더티 리드 막기", "Block dirty reads"), ("확정 전엔 못 봐요", "can't see it before it's confirmed"), "calm"),
             (EYE_I, ("같은 값 보장하기", "Guarantee the same value"), ("다시 읽어도 안 변해요", "re-reading gives the same value")),
             (GHOST_I, ("유령 읽기 막기", "Block phantom reads"), ("새로 끼어든 행도 막아요", "blocks newly inserted rows too"), "warm"),
             (SHIELD_I, ("차례로 처리하기", "Process one at a time"), ("가장 엄격한 Serializable", "the strictest — serializable")),
         ])},
        {"svg": P4, "alt": ("Read Uncommitted, Read Committed, Repeatable Read, Serializable 네 단계를 비교하는 표", "A table comparing four levels: read uncommitted, read committed, repeatable read, serializable"),
         "caption": ("격리 수준은 네 단계로 나뉘어요.", "Isolation levels split into four stages."),
         "small": ("Serializable이 가장 엄격해요.", "Serializable is the strictest.")},
        {"svg": P5, "alt": ("왼쪽: 감사원이 가장 안전한 Serializable을 만족해함. 오른쪽: 배송 기사가 오래 기다리며 땀 흘림", "Left: the auditor is pleased with the safest serializable level. Right: a driver sweats, waiting longer"),
         "caption": ("Serializable은 가장 안전하지만, 뒷사람이 오래 기다려요.", "Serializable is safest, but the next person waits longer."),
         "small": ("그래서 상황에 맞는 수준을 골라야 해요.", "So the right level has to fit the situation.")},
    ],
    "summary": (("<b>격리 수준</b> = 여러 사람이 <b>동시에 같은 데이터를 손댈 때</b>, 서로의 작업이 얼마나 보이고 가려질지 정하는 규칙.",
                 "<b>Isolation level</b> decides, when several people touch the same data at once, how much of each other's work they can see."),
                ("트랜잭션 격리 수준은 Read Uncommitted·Read Committed·Repeatable Read·Serializable 네 단계가 있고, 낮을수록 더티 리드·반복 불가 읽기·팬텀 리드 같은 이상현상이 더 많이 허용돼요. 격리가 강할수록 일관성은 높아지지만 동시 처리량(성능)은 떨어져요.",
                 "Transaction isolation levels — Read Uncommitted, Read Committed, Repeatable Read, Serializable — allow progressively fewer anomalies (dirty read, non-repeatable read, phantom read) as they get stricter. Stronger isolation means higher consistency but lower concurrent throughput.")),
    "glossary": [
        ("더티 리드", "Dirty Read", ("아직 확정 안 된 값을 보는 것.", "Seeing a value that isn't confirmed yet."), ("Read Uncommitted에서만 생겨요.", "Only happens at read uncommitted.")),
        ("반복 불가 읽기", "Non-repeatable Read", ("같은 걸 다시 읽었더니 값이 바뀜.", "Re-reading the same thing gives a different value."), ("Repeatable Read부터 막혀요.", "Blocked from repeatable read onward.")),
        ("유령 읽기(팬텀 리드)", "Phantom Read", ("없던 행이 다시 조회하니 생겨남.", "A row that wasn't there shows up on re-query."), ("Serializable에서 완전히 막혀요.", "Fully blocked only at serializable.")),
        ("Serializable", "Serializable", ("차례로 하나씩 처리한 것처럼 만드는 수준.", "The level that makes it look like one at a time."), ("가장 엄격하고 가장 느려요.", "Strictest and slowest.")),
        ("ACID", "ACID", ("전표가 지키는 네 가지 약속.", "The four promises a receipt keeps."), ('격리(I)는 그중 하나예요. → <a href="acid-ko.html">전표가 지키는 네 약속</a>', 'Isolation is one of the four. → <a href="acid-en.html">the four promises a receipt keeps</a>')),
        ("병행제어", "Concurrency Control", ("격리 수준을 실제로 지켜내는 방법.", "How isolation levels actually get enforced."), ('락이나 MVCC로 구현해요. → <a href="concurrency-ko.html">동시에 안 부딪히는 규칙</a>', 'Implemented with locks or MVCC. → <a href="concurrency-en.html">the no-collision rule</a>')),
        ("CAP 정리", "CAP Theorem", ("놀이공원 세계의 트레이드오프 이야기.", "A trade-off story from the amusement-park world."), ('분산 환경에서 일관성 자체의 한계를 다뤄요. → <a href="captheorem-ko.html">CAP 정리</a>', 'Covers the limits of consistency itself in distributed settings. → <a href="captheorem-en.html">the CAP theorem</a>')),
        ("최종 일관성", "Eventual Consistency", ("당장은 달라도 결국 같아지는 것.", "Different for now, but eventually matching."), ('격리 수준과는 또 다른 분산 환경의 타협이에요. → <a href="eventualconsistency-ko.html">최종 일관성</a>', 'A different distributed-systems compromise from isolation levels. → <a href="eventualconsistency-en.html">eventual consistency</a>')),
    ],
}
