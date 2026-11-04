"""페이징·세그멘테이션 — 학교 창고 비유 (컴퓨터 구조 주제라 학생회 규칙과는 결이 달라요. ppesys의 virtualmem 쪽이 기술 깊이를 다뤄요)."""
from _draw import *
from _world import *


def locker(x, y, w, h, text, used=True, s=1.0):
    fill = "#E9B44C" if used else "var(--panel)"
    stroke = "#C9822B" if used else "var(--line)"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
            + label(w / 2, h / 2 + 5, text, 11, "#142033", cls="d") + '</g>')


LOCK_I = icon('<rect x="10" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="10" y="36" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="36" width="18" height="18" rx="3" fill="var(--accent)"/>')
ROOM_I = icon('<rect x="8" y="22" width="18" height="30" fill="var(--good)"/><rect x="30" y="12" width="26" height="40" fill="var(--good)" opacity="0.7"/>')
MAP_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h28 M18 30 h28 M18 40 h18" stroke="#142033" stroke-width="2.5"/>')
MIX_I = icon('<rect x="8" y="30" width="20" height="20" rx="3" fill="var(--accent)"/><rect x="34" y="14" width="22" height="36" fill="var(--good)" opacity="0.7"/>')

# 1. 사물함은 똑같은 크기인데, 준비물은 크기가 다 달라요
P1 = svg(300, sky(300)
         + locker(100, 120, 60, 60, "A") + locker(170, 120, 60, 60, "B") + locker(240, 120, 60, 60, "C") + locker(310, 120, 60, 60, "D")
         + person(130, 200, s=0.7, face=SWEAT + EYES, **STUDENT)
         + bubble(400, 90, 260, 44, "⟦제 미술 도구함은 사물함보다 훨씬 큰데요?|my art-supply box is way bigger than one locker?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사물함은 다 똑같은 크기인데, 준비물 크기는 제각각이에요|every locker is the same size, but supplies come in every size⟧", 13, "var(--ink)", cls="d"))

# 2. 고정 크기로만 자르면 공간이 남거나 모자라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + locker(140, 120, 60, 60, "A", True) + locker(210, 120, 60, 60, "", False)
         + label(175, 210, "⟦작은 준비물엔 빈 공간이 남아요|a small item leaves empty space⟧", 11, "var(--ink)")
         + locker(450, 120, 60, 60, "?", True) + locker(520, 120, 60, 60, "?", True) + locker(590, 120, 60, 60, "?", True)
         + label(545, 210, "⟦큰 준비물은 칸 여러 개에 쪼개져 흩어져요|a big item gets split across several lockers⟧", 11, "var(--ink)")
         + label(380, 280, "⟦같은 크기 칸만 쓰면 공간이 남거나, 큰 물건이 여러 칸에 흩어져요|with same-size slots only, space goes unused or a big item gets scattered across slots⟧", 12, "var(--ink)", cls="d"))

# 3. 페이징 vs 세그멘테이션 = 창고를 나누는 두 가지 다른 방식 (hero)
P3 = svg(340, sky(340)
         + label(380, 26, "⟦페이징·세그멘테이션 = 창고를 나누는 두 가지 다른 방식|paging and segmentation = two different ways to slice up storage⟧", 13, "var(--ink)", cls="d")
         + locker(70, 90, 46, 46, "P0") + locker(120, 90, 46, 46, "P1") + locker(170, 90, 46, 46, "P2") + locker(220, 90, 46, 46, "P3")
         + label(145, 70, "⟦페이징: 똑같은 크기로|paging: all the same size⟧", 11, "var(--muted)")
         + '<rect x="420" y="70" width="60" height="100" rx="4" fill="#5B8DEF"/><rect x="490" y="100" width="100" height="50" rx="4" fill="#5B8DEF"/><rect x="600" y="70" width="40" height="130" rx="4" fill="#5B8DEF"/>'
         + label(540, 55, "⟦세그멘테이션: 의미 단위로, 크기는 제각각|segmentation: by logical unit, each a different size⟧", 11, "var(--muted)")
         + label(380, 335, "⟦둘 다 \'진짜 창고(메모리)가 좁아도 넉넉해 보이게\' 나누는 방법이에요|both divide storage (memory) so a small warehouse looks roomy⟧", 12, "var(--muted)"))

# 4. 페이징 vs 세그멘테이션 비교표
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 30, 320, 260, "⟦페이징|PAGING⟧",
                      ("⟦고정 크기 칸(페이지)으로 자름|cut into fixed-size pages⟧", "⟦내용과 상관없이 크기로만 나눔|size only, whatever's inside⟧", "⟦작은 자투리 공간 낭비(내부 단편화)|wastes small leftover space (internal fragmentation)⟧"), 1.0)
         + rulesboard(400, 30, 320, 260, "⟦세그멘테이션|SEGMENTATION⟧",
                      ("⟦의미 단위(코드/데이터 등)로 자름|cut by logical unit (code/data/etc.)⟧", "⟦논리적 역할 기준|based on logical role⟧", "⟦칸 사이 빈틈 낭비(외부 단편화)|wastes gaps between chunks (external fragmentation)⟧"), 1.0)
         + label(380, 305, "⟦실제 시스템은 둘을 섞어 쓰기도 해요(세그멘테이션 페이징)|real systems sometimes mix both (segmented paging)⟧", 11, "var(--ink)", cls="d"))

# 5. 둘 다 '가짜 지도'일 뿐, 진짜 관리는 다른 세계에서
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + locker(230, 130, 90, 60, "⟦가상|virtual⟧", True, 0.9) + label(275, 220, "⟦가상 주소는 프로그램이 보는 지도일 뿐이에요|a virtual address is only the map a program sees⟧", 11, "var(--ink)")
         + person(570, 125, s=0.8, face=EYES, **REP) + label(570, 255, "⟦운영체제의 실제 관리법은 시스템SW 분야의 가상메모리 쪽에서 다뤄요|how the OS really manages it is on the Systems virtual-memory page⟧", 11, "var(--ink)")
         + label(380, 300, "⟦이 페이지는 두 방식의 차이만 다루고, 운영체제(OS)의 실제 관리는 시스템SW 분야에서 다뤄요|this page covers only the difference — the OS's actual management is detailed in the Systems category⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "pagingseg", "order": 15,
    "title": ("창고를 나누는 두 가지 다른 방식", "Two Different Ways to Slice Up Storage"),
    "h1": ("<em>페이징·세그멘테이션</em>이 뭐예요?", "What is <em>Paging and Segmentation</em>?"),
    "sub": ("페이징과 세그멘테이션을, 학교 사물함(고정 크기)과 준비물 창고(제각각 크기)를 나누는 두 가지 다른 방식 이야기로 풀어봤어요. (컴퓨터 구조 주제라 학생회 규칙과는 결이 조금 달라요 — 기술 깊이는 시스템SW 분야의 가상메모리 페이지로.)",
            "Paging and segmentation, told as a story about two different ways to divide storage — same-size lockers versus differently-sized supply rooms. (This is really a computer-architecture topic, not a rules-and-law one — see the Systems category's virtual-memory page for the technical depth.)"),
    "panels": [
        {"svg": P1, "alt": ("똑같은 크기의 사물함 네 칸이 늘어서 있고, 학생이 미술 도구함이 사물함보다 크다고 말함", "Four identical lockers in a row; a student says their art-supply box is bigger than a locker"),
         "caption": ("사물함은 다 똑같은 크기인데, 준비물 크기는 제각각이에요.", "Every locker is the same size, but supplies come in every size."),
         "small": ("작은 준비물도 큰 준비물도 똑같은 칸에 넣어야 해요.", "Small or big, every supply has to go in the same-sized slot.")},
        {"svg": P2, "alt": ("왼쪽: 작은 준비물이 든 사물함에 빈 공간이 남음. 오른쪽: 큰 준비물이 사물함 세 칸에 쪼개져 흩어짐", "Left: a locker with a small item leaves space empty. Right: a big item is split across three lockers"),
         "caption": ("같은 크기 사물함만 쓰면 작은 물건엔 공간이 남고, 큰 물건엔 칸이 모자라요.", "With only same-size lockers, small items leave space unused and big ones don't fit in one."),
         "small": ("같은 크기 칸만 쓰면 공간이 남거나, 큰 물건이 여러 칸에 흩어져요.", "With same-size slots only, space goes unused or a big item gets scattered across slots.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽: 똑같은 크기로 자른 페이징 칸들. 오른쪽: 의미 단위로 서로 다른 크기로 자른 세그멘테이션 블록들", "Left: paging slots cut to identical size. Right: segmentation blocks cut by meaning, each a different size"),
         "caption": ("페이징과 세그멘테이션은 창고(메모리)를 나누는 두 가지 다른 방식이에요.", "Paging and segmentation are two different ways to slice up storage (memory)."),
         "small": ("둘 다 '진짜 창고(메모리)가 좁아도 넉넉해 보이게' 나누는 방법이에요.", "Both divide storage (memory) so a small warehouse looks roomy."),
         "tricks": (4, [
             (LOCK_I, ("페이징 — 같은 크기로", "Paging — same size"), ("몇 번째 칸인지로 찾아요", "found by slot number"), "calm"),
             (ROOM_I, ("세그멘테이션 — 의미로", "Segmentation — by meaning"), ("코드·데이터처럼 역할로 나눠요", "divided by role, like code vs data")),
             (MAP_I, ("둘 다 가짜 지도(가상 주소)", "Both use a fake map (virtual addresses)"), ("실제 메모리 위치는 운영체제가 따로 관리해요", "the OS tracks the real memory location separately"), "warm"),
             (MIX_I, ("섞어 쓰기도 해요", "Sometimes mixed"), ("각 세그먼트 안을 다시 페이징해요", "paging again inside each segment")),
         ])},
        {"svg": P4, "alt": ("페이징은 고정 크기·크기로만 나눔·내부 단편화, 세그멘테이션은 의미 단위·논리적 역할·외부 단편화로 비교", "A comparison: paging is fixed-size, split by size only, internal fragmentation; segmentation is logical-unit, role-based, external fragmentation"),
         "caption": ("페이징은 같은 크기로, 세그멘테이션은 역할별로 자르고, 낭비되는 공간도 달라요.", "Paging cuts by fixed size and segmentation by role, and each wastes space differently."),
         "small": ("실제 시스템은 둘을 섞어 쓰기도 해요.", "Real systems sometimes mix both.")},
        {"svg": P5, "alt": ("왼쪽: 가상 사물함은 프로그램이 보는 지도일 뿐이라는 라벨. 오른쪽: 대표가 운영체제의 실제 관리법은 시스템SW 분야에서 다룬다고 말함", "Left: a label saying the virtual locker is just a map the program sees. Right: a rep says how the OS really manages it is on the Systems category's page"),
         "caption": ("둘 다 프로그램에게 보여주는 '가짜 지도'이고, 운영체제의 실제 관리는 시스템SW 분야에서 다뤄요.", "Both give a program a fake map — the OS's real management is covered in the Systems category."),
         "small": ("이 페이지는 두 방식의 차이만 다루고, 운영체제(OS)의 실제 관리는 시스템SW 분야에서 다뤄요.", "This page covers only the difference — the OS's actual management is detailed in the Systems category.")},
    ],
    "summary": (("<b>페이징</b>은 메모리를 <b>고정 크기 칸</b>으로, <b>세그멘테이션</b>은 <b>의미 단위(코드/데이터 등)</b>로 나누는, 가상 주소를 실제 메모리에 대응시키는 두 가지 다른 방식.",
                 "<b>Paging</b> cuts memory into <b>fixed-size chunks</b>, while <b>segmentation</b> cuts it by <b>logical unit</b> (code, data, and so on) — two different ways of mapping virtual addresses to real memory."),
                ("페이징은 가상·물리 메모리를 모두 고정 크기(페이지/프레임)로 나누고 페이지 테이블로 매핑해요. 구현이 단순하고 외부 단편화가 없지만, 마지막 페이지가 다 안 차면 내부 단편화가 생겨요. 세그멘테이션은 프로그램을 코드·데이터·스택처럼 의미 있는 단위(세그먼트)로 나누는데, 세그먼트 크기가 제각각이라 보호·공유는 쉽지만 세그먼트 사이에 외부 단편화가 생길 수 있어요. 과거 x86 계열처럼 세그먼트 안을 다시 페이징한 시스템(세그멘테이션 페이징)도 있었고, 현대 64비트 운영체제는 대부분 페이징 위주로 동작해요.",
                 "Paging divides both virtual and physical memory into fixed-size chunks (pages/frames) mapped via a page table — simple to implement, with no external fragmentation, though the last partly-filled page wastes space (internal fragmentation). Segmentation divides a program into logically meaningful, variable-sized units (code, data, stack) — making protection and sharing easier, but leaving gaps between segments (external fragmentation). Some systems, such as older x86 designs, paged again inside each segment (segmented paging); modern 64-bit operating systems rely mostly on paging.")),
    "glossary": [
        ("페이징", "Paging", ("고정 크기 칸으로 자르는 방식.", "Cutting into fixed-size chunks."), ("내용과 상관없이 같은 크기로 나눠요.", "Splits by size alone, whatever's inside.")),
        ("세그멘테이션", "Segmentation", ("의미 단위로 자르는 방식.", "Cutting by logical unit."), ("코드·데이터·스택처럼 역할로 나눠요.", "Divided by role, like code, data, and stack.")),
        ("내부 단편화", "Internal Fragmentation", ("고정 칸 안에 남는 자투리 공간.", "Leftover space wasted inside a fixed-size slot."), ("페이징에서 생기기 쉬워요.", "Common in paging.")),
        ("외부 단편화", "External Fragmentation", ("칸과 칸 사이에 생기는 못 쓰는 빈틈.", "Unusable gaps left between chunks."), ("세그멘테이션에서 생기기 쉬워요.", "Common in segmentation.")),
        ("페이지 테이블", "Page Table", ("가상 페이지와 실제 메모리 칸의 대응표.", "The table matching virtual pages to real memory slots."), ('페이징의 핵심 구조예요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'The core structure of paging. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse mine</a>')),
        ("세그먼트 테이블", "Segment Table", ("세그먼트마다 시작 위치와 길이를 적은 표.", "The table recording each segment's start and length."), ("세그먼트는 크기가 다 달라서 길이도 같이 적어요.", "Segments vary in size, so length is recorded too.")),
        ("세그멘테이션 페이징", "Segmented Paging", ("세그먼트 안을 다시 페이징하는 혼합 방식.", "A hybrid that pages again inside each segment."), ("이 혼합 방식은 두 방식의 장점을 같이 쓰려는 거예요.", "This hybrid tries to keep the advantages of both.")),
        ("가상메모리", "Virtual Memory", ("메모리가 실제보다 넉넉해 보이게 하는 가짜 지도 전체 개념.", "The broader idea of a fake map that makes memory look roomier than it is."), ('페이징·세그멘테이션은 이걸 구현하는 두 방법이에요. → <a href="virtualmem-ko.html">가상메모리·페이징</a>', 'Paging and segmentation are two ways to implement it. → <a href="virtualmem-en.html">virtual memory and paging</a>')),
    ],
}
