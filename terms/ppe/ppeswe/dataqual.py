from _draw import *
from _world import *

# 1. 주소록이 엉망이라 책이 엉뚱한 집으로 가요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **PRINTER)
         + manuscript(260, 130, 0.8, marks=3, text="⟦독자 주소록|reader address list⟧") + printplate(390, 160, 0.6) + printplate(470, 150, 0.6)
         + label(380, 230, "⟦주소가 틀려서 책이 엉뚱한 집으로 갔어요|the address was wrong, so the book went to the wrong house⟧", 12, "var(--bad)")
         + label(380, 280, "⟦같은 독자에게 두 번 보내기도 했어요|the same reader sometimes got sent two copies⟧", 13, "var(--ink)"))

# 2. 주소록 정리는 나중에, 라고 미루다 생긴 일
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 220, 36, "⟦주소록 정리는 나중에 해도 되잖아요|the address-list cleanup can wait, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **READER) + bubble(470, 80, 220, 36, "⟦저는 책을 아예 못 받았어요|I never got my book at all⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦주소록 데이터가 지저분하면, 책을 아무리 잘 써도 독자에게 안 가요|messy address data means even a well-written book never reaches the reader⟧", 12, "var(--ink)"))

# 3. 데이터 품질관리 = 주소록을 정확·완전·유일하게 계속 관리하는 일 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **EDITOR) + inkstamp(460, 90, 0.8)
         + manuscript(260, 180, 0.7, text="⟦정확해요|accurate⟧") + manuscript(380, 216, 0.7, text="⟦빠짐없어요|complete⟧") + manuscript(500, 180, 0.7, text="⟦중복 없어요|no duplicates⟧")
         + label(380, 30, "⟦데이터 품질관리 = 독자 주소록을 정확하고 빠짐없고 중복 없이 계속 관리하는 일|data quality management = keeping the reader address list accurate, complete, and duplicate-free, continuously⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦주소록은 한 번 정리로 끝나지 않아요, 계속 들여다봐야 해요|the list is never cleaned just once — it needs constant attention⟧", 12, "var(--muted)"))

# 4. 품질을 재는 네 기준
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦데이터 품질 주요 기준 네 가지|FOUR KEY DATA QUALITY DIMENSIONS⟧",
                      ("⟦정확성 — 실제와 맞아야 해요|accuracy — must match reality⟧",
                       "⟦완전성 — 빠진 항목이 없어야 해요|completeness — nothing missing⟧",
                       "⟦일관성 — 어느 명부에 적힌 값이든 같아야 해요|consistency — same value in every copy of the list⟧",
                       "⟦최신성 — 이사 간 주소는 바로 갱신|timeliness — update addresses when they change⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **EDITOR)
         + label(560, 250, "⟦교정자가 오탈자를 잡듯, 주소록도 똑같이 교정해요|the list gets proofed just like a manuscript's typos⟧", 11, "var(--muted)")
         + label(380, 300, "⟦주소록이 기준 하나라도 어긋나면, 책이 독자에게 못 갈 수 있어요|if the list fails even one of these, the book may not reach the reader⟧", 12, "var(--ink)"))

# 5. 한 번의 청소로 끝나지 않아요
P5 = svg(340, '<rect width="380" height="340" fill="var(--accent-soft)"/><rect x="380" width="380" height="340" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=EYES, **EDITOR) + label(190, 260, "⟦주소록을 돌보면 배송 오류가 크게 줄어요|tending the list cuts delivery errors way down⟧", 11, "var(--ink)")
         + person(570, 110, s=0.8, face=SMILE, **PRINTER) + manuscript(570, 200, 0.6) + label(570, 260, "⟦그래도 주소록은 계속 손이 가요|but the list still takes constant upkeep⟧", 11, "var(--ink)")
         + label(380, 315, "⟦데이터 품질관리는 한 번의 청소가 아니라, 계속 돌보는 정원 가꾸기예요|data quality management isn't a one-time cleanup — it's tending a garden, continuously⟧", 12, "var(--ink)", cls="d"))

ACCURACY_I = icon('<circle cx="26" cy="26" r="16" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M38 38 l14 14" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M18 26 l6 6 l12 -12" stroke="var(--good)" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
COMPLETE_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><path d="M20 22 h20 M20 30 h20 M20 38 h20 M20 46 h20" stroke="#142033" stroke-width="2.5"/>')
CONSISTENCY_I = icon('<rect x="8" y="22" width="20" height="20" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="36" y="22" width="20" height="20" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><path d="M28 32 h8" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/>')
TIMELY_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 20 v12 l9 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "dataqual", "order": 6,
    "title": ("독자 주소록을 돌보는 일", "Tending the Reader Address List"),
    "h1": ("<em>데이터 품질관리</em>가 뭐예요?", "What is <em>Data Quality Management</em>?"),
    "sub": ("데이터 품질관리를, 독자 주소록이 틀리거나 빠지거나 겹치지 않도록 계속 돌보는 이야기로 풀어봤어요.",
            "Data quality management, told as a story about continuously tending the reader address list so it's never wrong, missing, or duplicated."),
    "panels": [
        {"svg": P1, "alt": ("인쇄 감독이 진땀을 흘리며 틀린 독자 주소록과 책 꾸러미를 봄", "A print supervisor sweats over a flawed reader address list and parcels of books"),
         "caption": ("주소가 틀려서 책이 엉뚱한 집으로 갔어요.", "The address was wrong, so the book went to the wrong house."),
         "small": ("같은 독자에게 두 번 보내기도 했어요.", "The same reader sometimes got sent two copies.")},
        {"svg": P2, "alt": ("편집장은 주소록 정리를 나중으로 미루고, 독자는 책을 못 받았다고 항의함", "The editor puts off cleaning the address list; the reader complains about never getting the book"),
         "caption": ("주소록 정리는 나중에, 라고 미루다 생긴 일.", "What happens when cleaning the list keeps getting put off."),
         "small": ("주소록 데이터가 지저분하면, 책을 아무리 잘 써도 독자에게 안 가요.", "Messy address data means even a well-written book never reaches the reader.")},
        {"svg": P3, "hero": True, "alt": ("편집장이 승인 도장을 들고, 정확하고 빠짐없고 중복 없는 주소록 세 묶음을 확인함", "An editor holds an approval stamp, checking three address-list bundles that are accurate, complete, and duplicate-free"),
         "caption": ("데이터 품질관리는 주소록을 정확·완전·유일하게 계속 관리하는 일이에요.", "Data quality management keeps the address list accurate, complete, and duplicate-free, continuously."),
         "small": ("주소록은 한 번 정리로 끝나지 않아요, 계속 들여다봐야 해요.", "The list is never cleaned just once — it needs constant attention."),
         "tricks": (4, [
             (ACCURACY_I, ("실제와 맞는지 보기", "Check it matches reality"), ("틀린 주소를 찾아요", "finding the wrong address"), "calm"),
             (COMPLETE_I, ("빠진 항목 채우기", "Fill in what's missing"), ("빈 칸이 없게 해요", "leaving no blanks")),
             (CONSISTENCY_I, ("값 맞춰두기", "Keep values matching"), ("명부마다 다르게 적힌 주소를 맞춰요", "aligning addresses written differently across lists"), "warm"),
             (TIMELY_I, ("바로 갱신하기", "Update right away"), ("이사 가면 바로 고쳐요", "fixing it the moment someone moves")),
         ])},
        {"svg": P4, "alt": ("품질 기준표: 정확성·완전성·일관성·최신성 네 항목", "A quality standards board: accuracy, completeness, consistency, timeliness"),
         "caption": ("데이터 품질은 정확성·완전성·일관성·최신성 같은 기준으로 재요. 정해진 개수는 없어서 유일성·유효성을 더하기도 해요.", "Data quality is measured by dimensions like accuracy, completeness, consistency, and timeliness. There's no fixed count, so uniqueness and validity are often added."),
         "small": ("교정자가 오탈자를 잡듯, 주소록도 똑같이 교정해요.", "The list gets proofed just like a manuscript's typos.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 주소록을 돌보면 배송 오류가 크게 줄어든다고 말함. 오른쪽: 인쇄 감독이 주소록은 여전히 계속 손이 간다고 말함", "Left: the editor says tending the list cuts delivery errors way down. Right: the print supervisor says the list still takes constant upkeep"),
         "caption": ("주소록 관리는 한 번의 청소로 끝나지 않아요.", "Keeping the list clean doesn't end with a single cleanup."),
         "small": ("주소록 관리는 계속 돌보는 정원 가꾸기에 가까워요.", "Keeping the list clean is closer to tending a garden, continuously.")},
    ],
    "summary": (("<b>데이터 품질관리</b> = 독자 주소록이 <b>정확·완전·일관·최신</b>하도록 <b>계속 돌보는</b> 일.",
                 "<b>Data quality management</b> = <b>continuously tending</b> the reader address list so it stays <b>accurate, complete, consistent, and timely</b>."),
                ("데이터 품질관리는 정확성·완전성·일관성·유일성·적시성(최신성) 같은 기준으로 데이터를 측정하고 정제하는 활동이에요. 데이터 프로파일링으로 현재 상태를 진단하고, 정제(cleansing)로 오류를 고치고, 이후엔 입력 단계에서부터 오류가 덜 생기도록 규칙을 정해둬요. 한 번의 정제로 끝나지 않고, 데이터 거버넌스 체계 안에서 계속 운영돼요.",
                 "Data quality management measures and refines data against standards like accuracy, completeness, consistency, uniqueness, and timeliness. Profiling diagnoses the current state, cleansing fixes errors, and rules are then set at the point of entry to prevent new ones. It isn't a one-time cleanup — it runs continuously within a data governance framework.")),
    "glossary": [
        ("데이터 품질관리", "Data Quality Management", ("주소록을 계속 돌보는 일 전체.", "The whole business of continuously tending the address list."), ("정확·완전·일관·유일·적시(최신) 같은 기준으로 재요.", "Measured by dimensions like accuracy, completeness, consistency, uniqueness, timeliness.")),
        ("데이터 프로파일링", "Data Profiling", ("주소록 상태를 먼저 진단하는 일.", "Diagnosing the address list's current state first."), ("정제보다 먼저 해요.", "Done before cleansing.")),
        ("데이터 정제", "Data Cleansing", ("틀리거나 겹친 항목을 직접 고치는 일.", "Directly fixing wrong or duplicate entries."), ("한 번 하고 끝나지 않아요.", "Never finished after just one pass.")),
        ("데이터 거버넌스", "Data Governance", ("주소록을 누가 어떻게 관리할지 정한 체계.", "The framework for who manages the address list and how."), ("품질관리를 지속시키는 틀이에요.", "The structure that keeps quality management ongoing.")),
        ("데이터 표준화", "Data Standardization", ("주소를 적는 형식을 하나로 맞추는 일.", "Unifying the format addresses are written in."), ("일관성을 지키는 방법 중 하나예요.", "One way to keep consistency.")),
        ("마스터 데이터 관리", "Master Data Management", ("독자 한 명당 기록을 하나로 통합하는 일.", "Unifying one reader's records into a single one."), ("중복 주소록을 막는 핵심이에요.", "The key to preventing duplicate address entries.")),
        ("요구공학", "Requirements Engineering", ("무엇을 정확히 적어야 하는지 미리 정하는 일.", "Deciding in advance exactly what must be recorded."), ('주소록 항목도 결국 명세에서 정해져요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', 'Even address-list fields ultimately come from a spec. → <a href="reqeng-en.html">the one who asks before writing</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("출간 과정을 곁에서 살피는 검수관.", "The checker who watches the whole publishing run."), ('데이터베이스 감리에서는 데이터 품질도 점검해요. → <a href="pmoaudit-ko.html">출간 과정을 곁에서 살피는 검수관</a>', 'Database audits check data quality too. → <a href="pmoaudit-en.html">the checker who watches the whole publishing run</a>')),
    ],
}
