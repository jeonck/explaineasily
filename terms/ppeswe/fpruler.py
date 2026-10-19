from _draw import *
from _world import *

# 1. 쪽수만으로는 분량을 알 수 없어요
P1 = svg(300, sky(300)
         + person(150, 150, s=0.85, face=EYES, **EDITOR) + bubble(70, 70, 190, 40, "⟦이 책, 대체 몇 쪽이야?|so how many pages is this book?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + manuscript(380, 150, 1.0) + label(380, 220, "⟦A 원고 — 300쪽|manuscript A — 300 pages⟧", 12, "var(--ink)")
         + manuscript(560, 150, 0.7) + label(560, 210, "⟦B 원고 — 80쪽|manuscript B — 80 pages⟧", 12, "var(--ink)")
         + label(380, 280, "⟦쪽수만으로는 일이 얼마나 되는지 알 수 없어요|page count alone doesn't say how much work it is⟧", 12, "var(--muted)"))

# 2. 쪽수는 공정한 자가 아니에요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **WRITER) + bubble(110, 70, 210, 40, "⟦그림이 많아 쪽수만 늘었어요|pictures just padded the page count⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.85, face=SWEAT, **WRITER) + bubble(450, 70, 230, 40, "⟦글자가 빽빽해서 일은 더 많아요|dense text means more work⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦쪽수만 봐서는 일의 양을 공정하게 잴 수 없어요|page count alone can't fairly measure the work⟧", 12, "var(--ink)"))

# 3. 기능점수(FP) = 내용을 세는 표준 자 (hero)
INBOX_I = icon('<rect x="14" y="20" width="36" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M32 8 V30 M24 22 l8 8 l8 -8" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
OUTBOX_I = icon('<rect x="14" y="20" width="36" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M32 42 V20 M24 28 l8 -8 l8 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
SHELF_I = icon('<rect x="8" y="10" width="48" height="44" rx="2" fill="#5A3B22"/><rect x="14" y="16" width="14" height="32" rx="2" fill="var(--accent)"/><rect x="32" y="16" width="14" height="32" rx="2" fill="#C9A86A"/>')
LINK_I = icon('<rect x="6" y="22" width="20" height="20" rx="3" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="38" y="22" width="20" height="20" rx="3" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M26 32 H38" stroke="var(--accent)" stroke-width="4"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦기능점수(FP) = 내용을 세는 표준 자|Function Point = a standard ruler that counts content⟧", 14, "var(--ink)", cls="d")
         + ruler(290, 110, 1.8, text="⟦쪽수 대신 기능을 세요|count functions, not pages⟧")
         + person(140, 220, s=0.75, face=EYES, **EDITOR) + manuscript(230, 230, 0.6)
         + person(620, 220, s=0.75, face=SMILE, **PRINTER) + printplate(560, 280, 0.5)
         + label(380, 320, "⟦작가 솜씨나 글씨체와 상관없이, 같은 기준으로 규모를 재요|size is measured the same way, no matter the writer's style⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "fpruler", "order": 14,
    "title": ("매수를 재는 자", "The Ruler That Measures Page Count"),
    "h1": ("<em>기능점수(FP)</em>가 뭐예요?", "What is a <em>Function Point (FP)</em>?"),
    "sub": ("기능점수를, 쪽수 대신 '무엇을 하는가'로 원고 분량을 재는 표준 자 이야기로 풀어봤어요.",
            "Function Points, told as a story about a standard ruler that measures a manuscript by what it does, not by its page count."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 '몇 쪽이야?' 묻고, 300쪽짜리 원고와 80쪽짜리 원고가 나란히 있음", "An editor asks how many pages, beside a 300-page manuscript and an 80-page one"),
         "caption": ("쪽수만으로는 분량을 알 수 없어요.", "Page count alone doesn't tell you the size."),
         "small": ("쪽수만으로는 일이 얼마나 되는지 알 수 없어요.", "Page count alone doesn't say how much work it is.")},
        {"svg": P2, "alt": ("왼쪽 작가는 그림이 많아 쪽수만 늘었다 말하고, 오른쪽 작가는 땀 흘리며 글자가 빽빽해서 일이 많다고 말함", "The left writer says pictures just padded the page count; the right writer, sweating, says dense text means more work"),
         "caption": ("쪽수는 공정한 자가 아니에요.", "Page count isn't a fair ruler."),
         "small": ("쪽수만 봐서는 일의 양을 공정하게 잴 수 없어요.", "Page count alone can't fairly measure the amount of work.")},
        {"svg": P3, "hero": True, "alt": ("커다란 자 옆에 편집장과 인쇄 감독이 원고와 인쇄판을 들고 서 있음", "A giant ruler beside an editor holding a manuscript and a print supervisor holding a print plate"),
         "caption": ("기능점수(FP)는 내용을 세는 표준 자예요.", "A Function Point is a standard ruler that counts content."),
         "small": ("작가 솜씨나 글씨체와 상관없이, 같은 기준으로 규모를 재요.", "Size is measured the same way, no matter the writer's style."),
         "tricks": (4, [
             (INBOX_I, ("입력 세기", "Count the inputs"), ("원고에 써넣는 칸이 몇 개인지", "how many fields get written in"), "calm"),
             (OUTBOX_I, ("출력·조회 세기", "Count outputs and lookups"), ("독자에게 보여주는 결과가 몇 개인지", "how many results readers see")),
             (SHELF_I, ("저장소 세기", "Count the storage"), ("책 안에서 관리하는 자료 묶음 수", "how many data groups the book keeps")),
             (LINK_I, ("외부 연계 세기", "Count the links out"), ("다른 출판사와 주고받는 길 수", "how many links to other publishers"), "warm"),
         ])},
        {"svg": svg(340, '<rect width="760" height="340" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 230, "⟦FP 계산 절차|HOW FP IS CALCULATED⟧",
                                 ("⟦① 입력·출력·조회·저장·연계 개수 세기|① count input/output/inquiry/storage/link⟧",
                                  "⟦② 항목별 복잡도 가중치 곱하기|② multiply each by a complexity weight⟧",
                                  "⟦③ 합산 = UFP(미조정 기능점수)|③ sum = UFP (unadjusted FP)⟧",
                                  "⟦④ 보정계수(VAF) 곱하면 FP|④ × VAF (adjustment factor) = FP⟧"), 1.0)
                    + label(380, 300, "⟦FP = UFP × VAF|FP = UFP × VAF⟧", 16, "var(--ink)", cls="d")
                    + label(380, 325, "⟦이 점수로 원고 분량(규모)을 가늠해요|this score is how you gauge the manuscript's size⟧", 12, "var(--muted)")),
         "alt": ("FP 계산 절차 네 단계 안내판과 'FP = UFP × VAF' 공식", "A four-step guide to the FP calculation and the formula FP = UFP × VAF"),
         "caption": ("FP는 이렇게 계산해요.", "This is how FP gets calculated."),
         "small": ("개수 × 가중치를 더해 UFP를 구하고, 보정계수를 곱해 최종 FP를 얻어요.", "Count × weight gives UFP; multiplying by the adjustment factor gives the final FP.")},
        {"svg": svg(300, sky(300)
                    + person(190, 130, s=0.8, face=EYES, **EDITOR) + label(190, 250, "⟦규모는 쟀어요|we measured the size⟧", 11, "var(--ink)")
                    + person(560, 130, s=0.8, face=EYES, **PRINTER) + label(560, 250, "⟦이걸로 비용·일정을 가늠해요|now we gauge cost and schedule⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦자로 재는 건 시작일 뿐이에요|measuring with the ruler is only the start⟧", 13, "var(--bad)", cls="d")
                    + label(380, 280, "⟦작가 숙련도와 도구에 따라 실제 속도는 달라요|actual speed still varies by writer skill and tools⟧", 12, "var(--muted)")),
         "alt": ("편집장은 규모를 쟀다 말하고, 인쇄 감독은 그걸로 비용과 일정을 가늠한다고 말함", "The editor says the size was measured; the print supervisor says it's now used to gauge cost and schedule"),
         "caption": ("자로 재는 건 시작일 뿐이에요.", "Measuring with the ruler is only the start."),
         "small": ('작가 숙련도와 도구에 따라 실제 속도는 달라요. 다음 이야기: 잰 분량을 돈으로 바꾸는 <a href="swcost-ko.html">대가산정</a>.',
                   'Actual speed still varies by skill and tools. Next: turning that size into money — <a href="swcost-en.html">cost estimation</a>.')},
    ],
    "summary": (("<b>기능점수(FP)</b> = 쪽수가 아니라 <b>입력·출력·조회·저장·연계</b> 개수로 원고 분량을 재는 표준 자.",
                 "<b>Function Point (FP)</b> = a standard ruler that measures a manuscript by counting <b>inputs, outputs, inquiries, storage, and links</b> — not pages."),
                ("기능점수(FP)는 소프트웨어 기능을 외부입력(EI)·외부출력(EO)·외부조회(EQ)·내부논리파일(ILF)·외부연계파일(EIF) 다섯 가지로 나눠 세고, 복잡도 가중치를 곱해 미조정 기능점수(UFP)를 구한 뒤, 보정계수(VAF)를 곱해 최종 FP를 산출하는 규모산정 기법이에요. 코드 줄 수(LOC)와 달리 개발 언어나 작성자 스타일에 덜 영향을 받아요.",
                 "Function Point (FP) is a sizing technique that counts five function types — external input (EI), external output (EO), external inquiry (EQ), internal logical file (ILF), and external interface file (EIF) — multiplies each by a complexity weight to get the unadjusted FP (UFP), then multiplies by a value adjustment factor (VAF) for the final FP. Unlike lines of code (LOC), it's less sensitive to language or authoring style.")),
    "glossary": [
        ("기능점수(FP)", "Function Point", ("원고를 기능으로 세는 자.", "The ruler that counts a manuscript by function."), ("쪽수 대신 '무엇을 하는가'로 규모를 재요.", "Measures size by what it does, not by page count.")),
        ("UFP(미조정 기능점수)", "Unadjusted FP", ("가중치만 곱해 더한 값.", "The sum after weights, before adjustment."), ("아직 보정 전 원점수예요.", "The raw score, before adjustment.")),
        ("VAF(보정계수)", "Value Adjustment Factor", ("난이도를 반영해 곱하는 수.", "The multiplier that reflects difficulty."), ("성능·보안 같은 요구조건을 반영해요.", "Reflects conditions like performance and security needs.")),
        ("EI(외부입력)", "External Input", ("원고에 써넣는 칸.", "A field written into the manuscript."), ("자료를 안으로 들여오는 기능이에요.", "A function that brings data in.")),
        ("EO(외부출력)", "External Output", ("독자에게 보여주는 결과물.", "The result shown to the reader."), ("계산하거나 가공해서 내보내요.", "Data that's processed before it goes out.")),
        ("EQ(외부조회)", "External Inquiry", ("그냥 찾아서 보여주는 것.", "Just looking something up and showing it."), ("가공 없이 바로 보여주는 조회예요.", "A lookup shown as-is, with no processing.")),
        ("ILF(내부논리파일)", "Internal Logical File", ("책 안에서 관리하는 자료 묶음.", "A data group the book manages internally."), ("이 출판사가 직접 유지보수해요.", "Maintained directly by this publishing house.")),
        ("EIF(외부연계파일)", "External Interface File", ("다른 출판사가 관리하는 자료를 참고하는 것.", "Referencing data another publisher maintains."), ('연결 자체는 → <a href="openapi-ko.html">개방형 API</a> 쪽 이야기예요.', 'How that connection works → <a href="openapi-en.html">Open API</a>.')),
    ],
}
