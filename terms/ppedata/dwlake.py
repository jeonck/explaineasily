from _draw import *
from _world import *

# 1. 온갖 모양의 물건이 쏟아져 들어와요
P1 = svg(300, sky(300)
         + person(380, 170, s=0.85, face=SWEAT + EYES, **SORTER)
         + box(220, 130, 0.6) + box(280, 160, 0.5) + receipt(340, 120, 0.5)
         + box(460, 150, 0.5) + receipt(520, 170, 0.5) + box(560, 120, 0.6)
         + label(380, 260, "⟦반듯한 상자도, 뒤죽박죽 더미도 한꺼번에 들어와요|neat boxes and messy piles arrive all at once⟧", 12, "var(--ink)")
         + label(380, 40, "⟦선반에 올릴지, 일단 쌓아둘지 정해야 해요|decide: shelve it now, or just pile it up for later?⟧", 13, "var(--muted)"))

# 2. 분류 규칙을 다 정해둬야만 선반에 올릴 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shelfzone(250, 140, 260, 80, 1.0)
         + person(560, 185, s=0.7, face=FROWN, **SORTER)
         + label(560, 288, "⟦처음 보는 물건은 분류 규칙이 없어 못 올려요|a brand-new kind of item has no rule, so it can't go on the shelf⟧", 11, "var(--bad)")
         + label(380, 40, "⟦선반에 올리려면 분류 규칙을 미리 다 정해둬야 해요|shelving it requires every sorting rule to be set in advance⟧", 12.5, "var(--ink)"))

# 3. 웨어하우스 = 정돈된 선반, 레이크 = 쌓아둔 야적장 (hero)
P3 = svg(340, '<rect width="380" height="340" fill="var(--good-soft)"/><rect x="380" width="380" height="340" fill="var(--sky)"/>'
         + shelfzone(60, 150, 260, 80, 0.95, label_text="⟦웨어하우스|warehouse⟧")
         + '<path d="M450 240 q20 -40 50 -30 q10 -30 50 -20 q20 -25 60 -10 q20 -15 60 0 L680 240 Z" fill="#8B5E3C"/>'
         + box(500, 210, 0.5) + receipt(550, 225, 0.45) + box(600, 215, 0.5) + receipt(650, 230, 0.4)
         + label(580, 270, "⟦야적장(레이크)|yard (lake)⟧", 12, "var(--ink)", weight=700)
         + label(380, 30, "⟦웨어하우스 = 분류해 선반에, 레이크 = 들어온 그대로 쌓아둠|Warehouse = sorted onto shelves, Lake = piled up exactly as it arrived⟧", 13, "var(--ink)", cls="d"))

# 4. 비교: 정형 vs 원본, 빠른 보고 vs 나중 가공
P4 = svg(320, sky(320, ground=False)
         + '<rect x="40" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="390" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(205, 66, "⟦데이터 웨어하우스|Data Warehouse⟧", 12.5, "var(--ink)", weight=700)
         + label(555, 66, "⟦데이터 레이크|Data Lake⟧", 12.5, "var(--ink)", weight=700)
         + label(205, 100, "⟦올리기 전에 분류(스키마 온 라이트)|sort before shelving (schema-on-write)⟧", 10, "var(--muted)")
         + label(205, 130, "⟦정형 데이터, SQL로 빠른 보고|structured, fast SQL reporting⟧", 10, "var(--good)")
         + label(205, 160, "⟦새 모양의 물건은 규칙부터 필요|new shapes need a rule first⟧", 10, "var(--bad)")
         + label(555, 100, "⟦일단 쌓고 나중에 분류(스키마 온 리드)|pile first, sort later (schema-on-read)⟧", 10, "var(--muted)")
         + label(555, 130, "⟦사진·로그·영상도 그대로 보관|photos, logs, video — kept as-is⟧", 10, "var(--good)")
         + label(555, 160, "⟦관리 안 하면 찾기 힘든 더미가 됨|unmanaged, it becomes a hard-to-search pile⟧", 10, "var(--bad)")
         + label(380, 300, "⟦언제 분류하느냐(쓸 때 vs 쓸 때 읽을 때)가 핵심 차이예요|the key difference is WHEN you sort it — on write, or on read⟧", 12, "var(--ink)"))

# 5. 방치된 레이크는 데이터 늪이 돼요
P5 = svg(320, sky(320, ground=False)
         + '<path d="M250 250 q30 -50 70 -35 q15 -35 60 -25 q25 -30 70 -10 q25 -20 70 0 L520 250 Z" fill="#5A4A38"/>'
         + box(300, 220, 0.5) + receipt(340, 235, 0.4) + box(400, 225, 0.45)
         + person(620, 160, s=0.75, face=SWEAT + EYES, **AUDITOR)
         + label(620, 280, "⟦이게 다 뭔지 아무도 몰라요|nobody knows what half of this even is⟧", 11, "var(--bad)")
         + label(380, 40, "⟦관리 안 된 레이크는 '데이터 늪'이 돼요|an unmanaged lake turns into a 'data swamp'⟧", 13, "var(--ink)")
         + label(380, 305, "⟦분석(OLAP)은 보통 잘 정리된 웨어하우스 쪽에서 해요|analysis (OLAP) usually runs on the tidy warehouse side⟧", 11, "var(--muted)"))

WRITE_I = icon('<rect x="16" y="10" width="32" height="44" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 20 h20 M22 30 h20" stroke="var(--good)" stroke-width="3"/>')
READ_I = icon('<path d="M10 40 q20 -36 44 0" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="38" r="7" fill="var(--accent)"/>')
RAW_I = icon('<path d="M10 50 q15 -20 30 -14 q10 -16 24 -6 L54 50 Z" fill="#8B5E3C"/>')
REPORT_I2 = icon('<rect x="12" y="16" width="40" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 44 v-14 M32 44 v-22 M44 44 v-8" stroke="var(--good)" stroke-width="4"/>')

PAGE = {
    "slug": "dwlake", "order": 14,
    "title": ("다듬어 둔 창고 vs 쌓아만 둔 야적장", "The Tidied Warehouse vs. the Raw Storage Yard"),
    "h1": ("<em>데이터 웨어하우스</em>와 <em>데이터 레이크</em>가 뭐예요?", "What are a <em>Data Warehouse</em> and a <em>Data Lake</em>?"),
    "sub": ("데이터 웨어하우스와 데이터 레이크를, 미리 분류해 선반에 올린 창고와 일단 쌓아두는 야적장을 비교하는 이야기로 풀어봤어요.",
            "A data warehouse and a data lake, told as a story comparing a tidily shelved warehouse with a yard where things just get piled up."),
    "panels": [
        {"svg": P1, "alt": ("분류 담당이 반듯한 상자와 뒤죽박죽 더미가 동시에 쏟아져 들어오는 걸 보며 땀을 흘림", "The modeler sweats as neat boxes and messy piles arrive at the same time"),
         "caption": ("반듯한 상자도, 뒤죽박죽 더미도 한꺼번에 들어와요.", "Neat boxes and messy piles arrive all at once."),
         "small": ("선반에 올릴지, 일단 쌓아둘지 정해야 해요.", "Decide: shelve it now, or just pile it up for later?")},
        {"svg": P2, "alt": ("분류 담당이 처음 보는 물건 앞에서 곤란해하며, 정돈된 선반은 뒤에 비어 있음", "The modeler is stuck in front of an unfamiliar item, with the tidy shelf standing empty behind"),
         "caption": ("선반에 올리려면 분류 규칙을 미리 다 정해둬야 해요.", "Shelving it requires every sorting rule to be set in advance."),
         "small": ("처음 보는 물건은 규칙이 없어 못 올려요.", "A brand-new kind of item has no rule, so it can't go on the shelf.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽엔 정돈된 선반(웨어하우스), 오른쪽엔 쌓아둔 더미(레이크)가 나란히 있음", "A tidy shelf (warehouse) on the left, a piled-up yard (lake) on the right, side by side"),
         "caption": ("웨어하우스는 분류해 선반에, 레이크는 들어온 그대로 쌓아둬요.", "A warehouse sorts things onto shelves; a lake piles them up exactly as they arrived."),
         "small": ("쓰는 목적에 따라 둘 다 필요해요.", "Depending on the goal, you often need both."),
         "tricks": (4, [
             (WRITE_I, ("웨어하우스 = 분류 후 저장", "Warehouse: sort, then store"), ("스키마 온 라이트예요", "that's schema-on-write")),
             (READ_I, ("레이크 = 저장 후 분류", "Lake: store, then sort"), ("스키마 온 리드예요", "that's schema-on-read"), "calm"),
             (REPORT_I2, ("웨어하우스 = 빠른 정기 보고", "Warehouse: fast routine reports"), ("SQL로 바로 집계해요", "aggregated straight away with SQL")),
             (RAW_I, ("레이크 = 다양한 원본 보관", "Lake: keeps all kinds of raw input"), ("사진·로그도 그대로요", "photos and logs kept as-is"), "warm"),
         ])},
        {"svg": P4, "alt": ("웨어하우스와 레이크를 분류 시점, 데이터 형태, 장단점 기준으로 비교한 표", "A table comparing warehouse and lake by when sorting happens, data shape, and trade-offs"),
         "caption": ("언제 분류하느냐가 핵심 차이예요.", "The key difference is when you sort it."),
         "small": ("웨어하우스는 쓸 때, 레이크는 읽을 때 분류해요.", "Warehouse sorts on write; lake sorts on read.")},
        {"svg": P5, "alt": ("관리되지 않은 야적장이 늪처럼 변해, 감사원이 땀을 흘리며 들여다봄", "An unmanaged yard turns swamp-like, and the auditor sweats trying to make sense of it"),
         "caption": ("관리 안 된 레이크는 '데이터 늪'이 돼요.", "An unmanaged lake turns into a 'data swamp'."),
         "small": ("분석(OLAP)은 보통 잘 정리된 웨어하우스 쪽에서 해요.", "Analysis usually runs on the tidy warehouse side.")},
    ],
    "summary": (("<b>데이터 웨어하우스</b>는 미리 분류해 선반에 올린 <b>정돈된 창고</b>, <b>데이터 레이크</b>는 들어온 그대로 쌓아두는 <b>원본 야적장</b>이에요.",
                 "A <b>data warehouse</b> is a <b>tidy, pre-sorted warehouse</b>; a <b>data lake</b> is a <b>raw storage yard</b> that keeps things exactly as they arrived."),
                ("데이터 웨어하우스는 저장 전에 스키마를 정해(schema-on-write) 정형 데이터를 담고 빠른 집계·보고에 강해요. 데이터 레이크는 저장은 먼저 하고 필요할 때 구조를 해석(schema-on-read)해, 정형·비정형을 가리지 않고 원본 그대로 쌓아둘 수 있어요. 관리되지 않은 레이크는 '데이터 늪'이 되기 쉽고, 둘을 합친 레이크하우스 같은 접근도 쓰여요.",
                 "A data warehouse fixes its schema before storing (schema-on-write), holding structured data well-suited to fast aggregation and reporting. A data lake stores first and interprets structure only when needed (schema-on-read), so it can keep anything — structured or not — exactly as it arrived. Left unmanaged, a lake easily becomes a 'data swamp'; a lakehouse approach tries to combine both.")),
    "glossary": [
        ("스키마 온 라이트", "Schema-on-write", ("담기 전에 분류부터.", "Sorting before anything goes in."), ("웨어하우스가 쓰는 방식이에요.", "The approach a warehouse uses.")),
        ("스키마 온 리드", "Schema-on-read", ("담아두고 쓸 때 분류.", "Storing first, sorting when it's used."), ("레이크가 쓰는 방식이에요.", "The approach a lake uses.")),
        ("정형/비정형 데이터", "Structured/Unstructured Data", ("반듯한 상자 vs 뒤죽박죽 더미.", "Neat boxes vs. messy piles."), ("레이크는 둘 다 받아줘요.", "A lake takes in both kinds.")),
        ("ETL/ELT", "ETL/ELT", ("옮기면서 다듬는 순서 차이.", "A difference in when the tidying happens."), ("ETL은 옮기기 전에, ELT는 옮긴 뒤에 다듬어요.", "ETL tidies before the move, ELT after.")),
        ("데이터 늪", "Data Swamp", ("관리 안 된 야적장.", "A yard nobody's kept up."), ("아무도 못 찾는 쓰레기 더미가 돼요.", "Becomes a pile nobody can search.")),
        ("BI 보고", "BI Reporting", ("정기적으로 올리는 집계 보고서.", "The routine aggregate report."), ("웨어하우스가 가장 잘하는 일이에요.", "What a warehouse is best suited for.")),
        ("레이크하우스", "Lakehouse", ("야적장에 선반 몇 개를 더한 것.", "A yard with a few shelves added in."), ("웨어하우스와 레이크를 합친 접근이에요.", "An approach combining warehouse and lake.")),
        ("OLAP", "OLAP", ("전체를 썰어보는 분석.", "Slicing the whole thing for analysis."), ('주로 웨어하우스 데이터로 해요. → <a href="olap-ko.html">전체를 썰어보는 창고 관리자</a>', 'Usually run on warehouse data. → <a href="olap-en.html">the manager who slices the whole warehouse</a>')),
    ],
}
