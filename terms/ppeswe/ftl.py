from _draw import *
from _world import *

# 1. "3번 칸만 고쳐주세요" 했더니 칸을 통째로 비워야 한다고 함
P1 = svg(300, sky(300)
         + bookshelf(260, 140, 1.2, n=4, hl=2)
         + person(500, 170, s=0.85, face=EYES, **PROOFER)
         + bubble(400, 70, 260, 44, "⟦3번 칸만 살짝 고쳐주세요?|could you just tweak slot 3 a little?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(140, 190, s=0.85, face=FROWN, **PRINTER)
         + bubble(40, 70, 240, 56, "⟦칸은 한 번에 하나만은 못 고쳐요, 통째로 비워야 해요|I can't touch just one slot — the whole block has to be cleared⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦의아하죠? 이 창고는 그렇게 생겼어요|strange, right? but this warehouse just works that way⟧", 12, "var(--ink)"))

# 2. 큰 덩어리로만 지울 수 있고, 너무 자주 지우면 칸이 닳음
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + bookshelf(300, 140, 1.3, n=4, hl=-1)
         + '<path d="M260 150 l-20 -14 M260 180 l-20 14 M540 150 l20 -14 M540 180 l20 14" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
         + label(380, 30, "⟦이 창고는 칸 하나씩이 아니라 덩어리(블록) 단위로만 비워져요|this warehouse only clears in whole blocks, never one slot at a time⟧", 13, "var(--ink)")
         + label(380, 280, "⟦비우고 채우는 걸 너무 자주 하면 그 칸이 닳아서 못 쓰게 돼요|clear and refill a slot too often, and it wears out for good⟧", 12, "var(--ink)"))

# 3. FTL = 제목↔칸을 연결해주고, 고친 원고는 새 빈 칸에 넣어주는 관리인 (hero)
P3 = svg(360, sky(360)
         + person(380, 110, s=0.9, face=EYES, **PRINTER)
         + label(380, 40, "⟦관리인(FTL)|the manager (FTL)⟧", 12, "var(--ink)")
         + manuscript(180, 90, 0.6, text="⟦책 제목|book title (logical)⟧")
         + bookshelf(300, 200, 0.9, n=4, hl=1)
         + '<path d="M230 100 Q300 150 340 220" stroke="var(--accent)" stroke-width="2.5" fill="none" stroke-dasharray="4 3" marker-end="url(#arrftl)"/>'
         + '<defs><marker id="arrftl" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--accent)"/></marker></defs>'
         + label(300, 270, "⟦실제 칸(물리 주소)|actual slot (physical)⟧", 11, "var(--muted)")
         + manuscript(560, 160, 0.55) + label(560, 195, "⟦옛 칸: 폐기 예정|old slot: marked for disposal⟧", 10, "var(--muted)")
         + manuscript(640, 110, 0.55, text="⟦새 칸|new slot⟧")
         + label(380, 320, "⟦옛 칸 위에 덮어쓰지 않고, 새 빈 칸에 넣어요|it never overwrites the old slot — it writes into a fresh empty one⟧", 12, "var(--muted)")
         + label(380, 30, "⟦FTL = 책 제목과 실제 칸을 이어주고, 고친 원고는 새 칸에 넣어주는 관리인|FTL = the manager who links a book's title to its real slot, and writes any edit into a fresh slot⟧", 13, "var(--ink)", cls="d"))

# 4. 옛 칸(폐기예정) → 새 칸(최신판) → GC가 옛 칸 비움
P4 = svg(320, sky(320)
         + styleguide(60, 40, 640, 240, "⟦관리인이 하는 일 — 순서대로|WHAT THE MANAGER DOES — IN ORDER⟧",
                      ("⟦① 고친 원고를 새 빈 칸에 써요|① writes the edit into a fresh empty slot⟧",
                       "⟦② 옛 칸엔 '폐기 예정' 표시만 해둬요|② just marks the old slot 'for disposal'⟧",
                       "⟦③ 폐기 예정 칸을 모아 한번에 비워요 (가비지 컬렉션)|③ clears disposal slots together later (garbage collection)⟧",
                       "⟦④ 특정 칸만 계속 쓰지 않도록 골고루 돌려써요 (마모 평준화)|④ spreads use evenly so no one slot wears out (wear leveling)⟧"), 1.0)
         + label(380, 300, "⟦독자는 이 과정을 몰라요, 그냥 제목으로만 찾으면 돼요|readers never see any of this — they just look things up by title⟧", 12, "var(--ink)"))

# 5. 빈 칸을 늘 남겨둬야 하고, GC 도중엔 잠깐 느려질 수 있음
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + bookshelf(140, 170, 0.75, n=4, hl=-1)
         + label(190, 265, "⟦늘 빈 칸을 몇 개 남겨둬야 해요|a few slots must always stay empty, on reserve⟧", 11, "var(--ink)")
         + person(580, 170, s=0.8, face=SWEAT + EYES, **PRINTER)
         + label(580, 260, "⟦옛 칸들을 비우는 동안은 잠깐 느려져요|while clearing old slots, things slow down briefly⟧", 11, "var(--ink)")
         + label(380, 282, "⟦FTL이 다 해주지만, 여유 공간과 잠깐의 속도는 그 대가예요|FTL handles it all, but spare space and brief slowdowns are the price⟧", 12, "var(--ink)", cls="d"))

ADDR_I = icon('<rect x="10" y="26" width="18" height="12" rx="2" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><rect x="36" y="26" width="18" height="12" rx="2" fill="var(--good)"/><path d="M28 32 h8" stroke="var(--accent)" stroke-width="2" marker-end="url(#mia)"/><defs><marker id="mia" markerWidth="8" markerHeight="8" refX="6" refY="2" orient="auto"><path d="M0 0 L6 2 L0 4 Z" fill="var(--accent)"/></marker></defs>')
NEWSLOT_I = icon('<rect x="10" y="30" width="16" height="16" rx="2" fill="var(--muted)" opacity="0.4"/><rect x="38" y="16" width="16" height="16" rx="2" fill="var(--good)"/><path d="M26 38 h6 M46 32 h-6" stroke="var(--line)" stroke-width="2"/>')
GC_I = icon('<rect x="12" y="14" width="40" height="36" rx="4" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 3"/><path d="M22 28 l20 8 M42 28 l-20 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
WEAR_I = icon('<circle cx="22" cy="32" r="8" fill="var(--good)"/><circle cx="42" cy="32" r="8" fill="var(--good)"/><path d="M22 32 a10 10 0 0 1 20 0" stroke="var(--line)" stroke-width="2" fill="none" stroke-dasharray="3 2"/>')

PAGE = {
    "slug": "ftl", "order": 31,
    "title": ("덮어쓰지 않는 서가 관리인", "The Shelf Manager Who Never Overwrites"),
    "h1": ("<em>플래시 변환계층(FTL)</em>이 뭐예요?", "What is the <em>Flash Translation Layer</em>?"),
    "sub": ("SSD의 플래시 변환계층(FTL)을, 책 제목과 실제 칸을 이어주고 고친 원고는 늘 새 칸에 넣는 서가 관리인 이야기로 풀어봤어요.",
            "The Flash Translation Layer (FTL) in SSDs, told as a story about a shelf manager who links a title to its real slot and always writes edits into a fresh one."),
    "panels": [
        {"svg": P1, "alt": ("교정자가 한 칸만 고쳐달라 하자 인쇄 감독이 칸을 통째로 비워야 한다고 답함", "The proofreader asks to tweak just one slot, but the supervisor says the whole block must be cleared"),
         "caption": ("'3번 칸만 고쳐주세요' 했더니, 통째로 비워야 한대요.", "Asked to just tweak slot 3 — but the whole block has to be cleared."),
         "small": ("의아하죠? 이 창고는 그렇게 생겼어요.", "Strange, right? But this warehouse just works that way.")},
        {"svg": P2, "alt": ("서가 전체가 삐걱거리며 덩어리 단위로만 비워지고, 칸이 닳는 모습", "The whole shelf creaks, clearing only in whole blocks, with slots wearing down"),
         "caption": ("덩어리 단위로만 비워지고, 너무 자주 쓰면 칸이 닳아요.", "It clears only in whole blocks, and overused slots wear out."),
         "small": ("비우고 채우는 걸 너무 자주 하면 그 칸이 못 쓰게 돼요.", "Clear and refill a slot too often, and it wears out for good.")},
        {"svg": P3, "hero": True, "alt": ("관리인이 책 제목과 실제 칸을 점선 화살표로 이어주고, 고친 원고를 새 빈 칸에 넣음", "The manager links a book's title to its real slot with a dashed arrow, and writes an edit into a fresh empty slot"),
         "caption": ("FTL은 책 제목과 실제 칸을 이어주는 관리인이에요.", "FTL is the manager who links a book's title to its real slot."),
         "small": ("옛 칸 위에 덮어쓰지 않고, 새 빈 칸에 넣어요.", "It never overwrites the old slot — it writes into a fresh one."),
         "tricks": (4, [
             (ADDR_I, ("주소 바꿔주기", "Translate the address"), ("제목↔실제 칸을 이어요", "links title to real slot"), "calm"),
             (NEWSLOT_I, ("새 칸에 쓰기", "Write to a new slot"), ("덮어쓰지 않아요", "never overwriting the old one")),
             (GC_I, ("폐기 칸 모아 비우기", "Reclaim disposal slots"), ("가비지 컬렉션이에요", "this is garbage collection"), "warm"),
             (WEAR_I, ("칸을 골고루 돌려쓰기", "Spread use evenly"), ("마모 평준화예요", "this is wear leveling")),
         ])},
        {"svg": P4, "alt": ("관리인이 하는 일 네 단계: 새 칸에 쓰기, 옛 칸 표시, 가비지 컬렉션, 마모 평준화", "The manager's four steps: write to a new slot, mark the old one, garbage collection, wear leveling"),
         "caption": ("관리인은 이 순서로 창고를 돌봐요.", "The manager tends the warehouse in exactly this order."),
         "small": ("독자는 이 과정을 몰라요, 그냥 제목으로만 찾으면 돼요.", "Readers never see any of this — they just look things up by title.")},
        {"svg": P5, "alt": ("왼쪽: 늘 빈 칸을 남겨둬야 함. 오른쪽: 가비지 컬렉션 도중엔 잠깐 느려짐", "Left: some slots must always stay empty. Right: garbage collection briefly slows things down"),
         "caption": ("빈 칸을 늘 남겨둬야 하고, 잠깐 느려질 때도 있어요.", "Some slots must stay empty in reserve, and there can be brief slowdowns."),
         "small": ("FTL이 다 해주지만, 여유 공간과 잠깐의 속도는 그 대가예요.", "FTL handles it all, but spare space and brief slowdowns are the price.")},
    ],
    "summary": (("<b>플래시 변환계층(FTL)</b>은 책 제목(논리 주소)과 실제 칸(물리 주소)을 이어주고, 고친 원고를 <b>옛 칸에 덮어쓰지 않고 새 칸에</b> 넣어주는 관리인이에요.",
                 "The <b>Flash Translation Layer (FTL)</b> links a title (logical address) to its real slot (physical address), and writes any edit into a <b>fresh slot instead of overwriting</b> the old one."),
                ("FTL은 SSD 내부에서 논리 블록 주소(LBA)를 실제 NAND 플래시의 물리 주소로 변환해주는 계층이에요. 플래시는 덮어쓰기가 안 되고 블록 단위로만 지울 수 있어, 쓰기 요청이 오면 기존 페이지는 무효 처리하고 새 빈 페이지에 기록해요. 무효 페이지가 쌓인 블록은 가비지 컬렉션으로 통째 지워 재사용하고, 특정 블록만 닳지 않도록 쓰기를 고르게 분산하는 웨어 레벨링도 함께 수행해요.",
                 "The FTL is the layer inside an SSD that translates logical block addresses (LBAs) into physical NAND flash addresses. Flash can't be overwritten in place and can only be erased block-by-block, so a write marks the old page invalid and writes to a fresh page instead. Garbage collection later erases and reclaims whole blocks full of invalid pages, while wear leveling spreads writes evenly so no single block wears out faster than the rest.")),
    "glossary": [
        ("FTL(플래시 변환계층)", "Flash Translation Layer", ("제목과 칸을 이어주는 서가 관리인.", "The shelf manager linking a title to its slot."), ("SSD 안에서 이 모든 걸 대신해줘요.", "Handles all of this inside the SSD.")),
        ("논리 주소/물리 주소", "Logical/Physical Address", ("책 제목 vs 실제 칸 번호.", "The book's title vs. the slot's real number."), ("FTL이 이 둘을 연결해줘요.", "FTL is what links the two together.")),
        ("가비지 컬렉션", "Garbage Collection", ("폐기 예정 칸을 모아 한번에 비우기.", "Gathering disposal slots and clearing them together."), ("도중엔 잠깐 느려질 수 있어요.", "Can cause brief slowdowns while it runs.")),
        ("웨어 레벨링", "Wear Leveling", ("칸을 골고루 돌려쓰기.", "Spreading use evenly across every slot."), ("한 칸만 닳아 못 쓰게 되는 걸 막아요.", "Prevents one slot from wearing out alone.")),
        ("오버프로비저닝", "Over-provisioning", ("늘 비워두는 여분의 칸.", "Slots kept empty in reserve, always."), ("쓰기 속도와 수명을 지켜줘요.", "Protects both write speed and lifespan.")),
        ("블록/페이지", "Block/Page", ("통째로만 지워지는 큰 칸, 그 안의 작은 칸.", "The big slot that clears all at once, and the small slots inside it."), ("지우기는 블록, 쓰기는 페이지 단위예요.", "Erasing works by block; writing works by page.")),
        ("형상관리", "Configuration Management", ("원고의 이전 버전을 보관하는 서가.", "The shelf that keeps a manuscript's past versions."), ('여기서도 비슷하게 "옛 것은 남기고 새로 쓴다"는 발상이 쓰여요. → <a href="scmshelf-ko.html">원고를 지키는 보관 서가</a>', 'A similar "keep the old, write the new" idea shows up there too. → <a href="scmshelf-en.html">the shelf that protects the manuscript</a>')),
        ("고가용성", "High Availability", ("칸 하나가 망가져도 버티는 대비.", "Holding up even when one slot fails."), ('이 세계 대신 놀이공원 세계에서 다뤄요. → <a href="failover-ko.html">예비 발전기가 넘겨받는 이야기</a>', 'Covered in another world, not this one. → <a href="failover-en.html">when the spare generator takes over</a>')),
    ],
}
