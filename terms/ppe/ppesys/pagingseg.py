"""페이징·세그멘테이션 — 부품 창고 선반을 나누는 두 방식. 지도(가상 주소)와 페이지 폴트는 virtualmem 쪽에서 다뤄요."""
from _draw import *
from _world import *


def slot(x, y, w, h, text="", filled=True):
    """선반 칸. filled=False 면 빈 칸."""
    fill = "#E9B44C" if filled else "var(--panel)"
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="{fill}" stroke="#C9822B" stroke-width="2.5"/>'
            + label(w / 2, h / 2 + 5, text, 12, "#142033", cls="d") + '</g>')


def part_slot(x, y, w, h, used):
    """같은 크기 칸에 짐이 일부만 찬 모습. used = 찬 비율(0~1). 나머지가 내부 단편화."""
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="var(--panel)" stroke="#C9822B" stroke-width="2.5"/>'
            f'<rect x="3" y="{h - h * used + 3:.0f}" width="{w - 6}" height="{h * used - 6:.0f}" rx="2" fill="#E9B44C"/></g>')


def seg(x, y, w, h, text):
    """크기가 제각각인 세그먼트 한 덩어리."""
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="#9DBBF2" stroke="#2E3D57" stroke-width="2"/>'
            + label(w / 2, h / 2 + 5, text, 12, "#142033", cls="d") + '</g>')


# 1. 선반 칸은 다 같은 크기인데, 짐은 크기가 제각각이에요
P1 = svg(320, sky(320)
         + label(205, 125, "⟦부품 창고 선반|the parts-warehouse shelf⟧", 11, "var(--muted)")
         + slot(70, 140, 60, 60, "F0") + slot(140, 140, 60, 60, "F1") + slot(210, 140, 60, 60, "F2") + slot(280, 140, 60, 60, "F3")
         + person(400, 150, s=0.8, face=SWEAT + EYES, **MECH1)
         + seg(480, 170, 150, 70, "⟦설계도 묶음|blueprint bundle⟧")
         + bubble(400, 62, 310, 44, "⟦설계도 묶음은 선반 한 칸보다 훨씬 커요|this blueprint bundle is way bigger than one slot⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 30, "⟦선반 칸은 다 같은 크기인데, 짐은 크기가 제각각이에요|every shelf slot is the same size, but work items come in every size⟧", 13, "var(--ink)", cls="d")
         + label(380, 285, "⟦메모리(선반)를 어떤 크기로 나눠야 할지가 문제예요|the puzzle: what size to cut memory (the shelf) into⟧", 12, "var(--ink)"))

# 2. 같은 크기 칸만 쓰면 자투리가 남고, 큰 짐은 조각나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + part_slot(95, 110, 90, 80, 0.3) + part_slot(195, 110, 90, 80, 0.45)
         + label(190, 215, "⟦작은 부품은 칸 안에 빈 자리가 남아요|a small part leaves empty room in its slot⟧", 11, "var(--ink)")
         + slot(430, 110, 80, 80, "⟦설계도 1|blueprint 1⟧") + slot(530, 110, 80, 80, "⟦설계도 2|blueprint 2⟧") + slot(630, 110, 80, 80, "⟦설계도 3|blueprint 3⟧")
         + label(570, 215, "⟦큰 설계도 묶음은 여러 칸에 나눠 담아요|a big blueprint bundle gets split across slots⟧", 11, "var(--ink)")
         + label(380, 50, "⟦같은 크기 칸으로만 나누면 생기는 일|what happens with same-size slots only⟧", 13, "var(--ink)", cls="d")
         + label(380, 270, "⟦자투리 공간이 남고, 한 덩어리였던 큰 짐은 조각나요|scraps of space stay empty, and one big item gets cut into pieces⟧", 12, "var(--ink)"))

# 3. 페이징 vs 세그멘테이션 = 선반을 나누는 두 방식 (hero)
P3 = svg(340, sky(340)
         + label(380, 26, "⟦페이징은 같은 크기로, 세그멘테이션은 쓰임새대로 선반을 나눠요|paging cuts the shelf into equal slots; segmentation cuts it by use⟧", 13, "var(--ink)", cls="d")
         + label(178, 82, "⟦페이징: 모두 같은 크기|paging: all the same size⟧", 11, "var(--muted)")
         + slot(50, 100, 60, 60, "P0") + slot(115, 100, 60, 60, "P1") + slot(180, 100, 60, 60, "P2") + slot(245, 100, 60, 60, "P3")
         + label(178, 185, "⟦안에 든 내용은 따지지 않아요|contents don't matter⟧", 11, "var(--muted)")
         + label(560, 62, "⟦세그멘테이션: 쓰임새별로, 크기는 제각각|segmentation: by use, each its own size⟧", 11, "var(--muted)")
         + seg(410, 80, 120, 100, "⟦코드|code⟧") + seg(540, 110, 80, 70, "⟦데이터|data⟧") + seg(630, 130, 80, 50, "⟦스택|stack⟧")
         + label(560, 205, "⟦설계도·부품·임시 작업대처럼 나눠요|like blueprints, parts, and the temp table⟧", 11, "var(--muted)")
         + person(355, 205, s=0.7, face=EYES, **CHIEF)
         + label(380, 320, "⟦둘 다 가상 주소를 실제 메모리 위치로 바꿔주는 방식이에요|both turn a virtual address into a real memory location⟧", 12, "var(--muted)"))

LOCK_I = icon('<rect x="10" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="14" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="10" y="36" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="34" y="36" width="18" height="18" rx="3" fill="var(--accent)"/>')
ROOM_I = icon('<rect x="8" y="22" width="18" height="30" fill="var(--good)"/><rect x="30" y="12" width="26" height="40" fill="var(--good)" opacity="0.7"/>')
MAP_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h28 M18 30 h28 M18 40 h18" stroke="#142033" stroke-width="2.5"/>')
MIX_I = icon('<rect x="8" y="30" width="20" height="20" rx="3" fill="var(--accent)"/><rect x="34" y="14" width="22" height="36" fill="var(--good)" opacity="0.7"/>')

# 4. 낭비되는 공간도 달라요
P4 = svg(320, sky(320, ground=False)
         + queueboard(30, 20, 340, 125, "⟦페이징|PAGING⟧",
                      ("⟦같은 크기 칸(페이지)으로 잘라요|cut into same-size pages⟧",
                       "⟦크기만 보고 나눠요|split by size alone⟧",
                       "⟦칸 안 자투리 낭비(내부 단편화)|scraps inside slots (internal fragmentation)⟧"), 1.0)
         + queueboard(390, 20, 340, 125, "⟦세그멘테이션|SEGMENTATION⟧",
                      ("⟦쓰임새 단위(세그먼트)로 잘라요|cut into segments by use⟧",
                       "⟦크기가 제각각이에요|each a different size⟧",
                       "⟦덩어리 사이 빈틈 낭비(외부 단편화)|gaps between chunks (external fragmentation)⟧"), 1.0)
         + part_slot(70, 165, 80, 70, 0.6) + part_slot(160, 165, 80, 70, 0.8) + part_slot(250, 165, 80, 70, 0.35)
         + seg(420, 165, 90, 70, "⟦코드|code⟧") + seg(535, 165, 60, 70, "⟦스택|stack⟧") + seg(620, 165, 80, 70, "⟦데이터|data⟧")
         + label(522, 256, "⟦빈틈|gap⟧", 11, "var(--bad)", cls="d") + label(607, 256, "⟦빈틈|gap⟧", 11, "var(--bad)", cls="d")
         + label(380, 296, "⟦세그먼트를 다시 같은 크기 페이지로 자르는 혼합 방식도 있어요|a hybrid also exists: segments cut again into same-size pages⟧", 12, "var(--ink)", cls="d"))

# 5. 대응표 모양도 달라요 (번지 찾기와 페이지 폴트는 virtualmem 쪽)
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + queueboard(40, 30, 300, 125, "⟦페이지 테이블|PAGE TABLE⟧", ["P0 → F7", "P1 → F2", "P2 → F5"], 1.0)
         + label(190, 190, "⟦위치는 페이지마다 프레임 번호 하나예요|location: one frame number per page⟧", 11, "var(--ink)")
         + label(190, 210, "⟦칸 크기가 같아서 길이는 안 적어요|same-size slots, so no length is listed⟧", 11, "var(--ink)")
         + queueboard(420, 30, 300, 125, "⟦세그먼트 테이블|SEGMENT TABLE⟧",
                      ["⟦코드: 시작 100, 길이 40|code: start 100, length 40⟧",
                       "⟦데이터: 시작 300, 길이 25|data: start 300, length 25⟧",
                       "⟦스택: 시작 500, 길이 15|stack: start 500, length 15⟧"], 1.0)
         + label(570, 190, "⟦크기가 제각각이라 시작과 길이를 같이 적어요|sizes vary, so start and length are both listed⟧", 11, "var(--ink)")
         + label(570, 210, "⟦길이를 넘는 번지는 막아요(보호)|an address past the length gets blocked⟧", 11, "var(--ink)")
         + label(380, 280, "⟦번지를 찾는 과정과 페이지 폴트는 가상메모리 페이지에서 다뤄요|the address lookup and page faults are on the virtual-memory page⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "pagingseg", "order": 26,
    "title": ("선반을 똑같이 자를까, 쓰임새대로 자를까", "Cut the Shelf Evenly, or by What It Holds"),
    "h1": ("<em>페이징·세그멘테이션</em>이 뭐예요?", "What is <em>Paging and Segmentation</em>?"),
    "sub": ("페이징과 세그멘테이션을, 부품 창고 선반을 같은 크기 칸으로 나눌지 쓰임새대로 나눌지 고르는 이야기로 풀어봤어요.",
            "Paging and segmentation, told as a story about whether to cut the parts-warehouse shelf into equal slots or by what each part is for."),
    "panels": [
        {"svg": P1, "alt": ("똑같은 크기의 선반 칸 네 개 옆에서 정비사가 설계도 묶음이 한 칸보다 훨씬 크다고 말함", "Beside four identical shelf slots, a mechanic says the blueprint bundle is way bigger than one slot"),
         "caption": ("선반 칸은 다 같은 크기인데, 짐은 크기가 제각각이에요.", "Every shelf slot is the same size, but work items come in every size."),
         "small": ("메모리(선반)를 어떤 크기로 나눠야 할지가 문제예요.", "The puzzle: what size to cut memory (the shelf) into.")},
        {"svg": P2, "alt": ("왼쪽: 작은 부품이 든 칸에 빈 자리가 남음. 오른쪽: 큰 설계도 묶음이 세 칸에 나뉘어 담김", "Left: slots holding small parts leave empty room. Right: a big blueprint bundle is split across three slots"),
         "caption": ("같은 크기 칸으로만 나누면 작은 짐은 빈 자리를 남기고, 큰 짐은 여러 칸으로 조각나요.", "With same-size slots only, small items leave empty room and big ones get cut across slots."),
         "small": ("칸 크기가 같으면 관리는 쉽지만, 짐의 모양과는 맞지 않아요.", "Same-size slots are easy to manage, but they don't fit the shape of the items.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽: 똑같은 크기로 자른 페이징 칸 네 개. 오른쪽: 코드·데이터·스택으로 크기가 다르게 자른 세그멘테이션 덩어리 세 개", "Left: four paging slots cut to one size. Right: three segmentation chunks of different sizes: code, data, stack"),
         "caption": ("페이징은 메모리를 같은 크기로, 세그멘테이션은 쓰임새대로 나눠요.", "Paging cuts memory into equal slots; segmentation cuts it by use."),
         "small": ("둘 다 가상 주소를 실제 메모리 위치로 바꿔주는 방식이에요.", "Both turn a virtual address into a real memory location."),
         "tricks": (4, [
             (LOCK_I, ("페이징 — 같은 크기로", "Paging — same size"), ("페이지 번호와 칸 안 위치로 찾아요", "found by page number and position inside it"), "calm"),
             (ROOM_I, ("세그멘테이션 — 쓰임새로", "Segmentation — by use"), ("코드·데이터·스택으로 나눠요", "divided into code, data, and stack")),
             (MAP_I, ("둘 다 대응표를 써요", "Both use a lookup table"), ("가상 주소를 실제 위치로 바꿔요", "turns a virtual address into a real location"), "warm"),
             (MIX_I, ("섞어 쓰기도 해요", "Sometimes mixed"), ("세그먼트를 다시 페이지로 잘라요", "each segment is cut again into pages")),
         ])},
        {"svg": P4, "alt": ("페이징은 같은 크기로 잘라 칸 안에 자투리가 남고, 세그멘테이션은 쓰임새대로 잘라 덩어리 사이에 빈틈이 남음", "Paging cuts to one size and leaves scraps inside slots; segmentation cuts by use and leaves gaps between chunks"),
         "caption": ("페이징은 칸 안에 자투리를, 세그멘테이션은 덩어리 사이에 빈틈을 남겨요.", "Paging leaves scraps inside slots; segmentation leaves gaps between chunks."),
         "small": ("세그먼트를 다시 같은 크기 페이지로 자르는 혼합 방식도 있어요.", "A hybrid also exists: segments cut again into same-size pages.")},
        {"svg": P5, "alt": ("왼쪽: 위치를 프레임 번호로 적은 페이지 테이블. 오른쪽: 세그먼트마다 시작 위치와 길이를 적은 세그먼트 테이블", "Left: a page table giving each page's location as one frame number. Right: a segment table listing each segment's start and length"),
         "caption": ("위치를 적을 때 페이지 테이블은 프레임 번호만, 세그먼트 테이블은 시작 위치와 길이까지 적어요.", "For location, a page table needs only a frame number; a segment table needs start and length."),
         "small": ("번지를 찾는 과정과 페이지 폴트는 가상메모리 페이지에서 다뤄요.", "The address lookup and page faults are on the virtual-memory page.")},
    ],
    "summary": (("<b>페이징</b>은 메모리를 <b>같은 크기 칸</b>으로, <b>세그멘테이션</b>은 <b>쓰임새 단위(코드·데이터·스택 등)</b>로 나누는, 가상 주소를 실제 메모리 위치로 바꾸는 두 가지 방식이에요.",
                 "<b>Paging</b> cuts memory into <b>same-size slots</b>, while <b>segmentation</b> cuts it by <b>use (code, data, stack, and so on)</b> — two ways of turning a virtual address into a real memory location."),
                ("페이징은 가상·물리 메모리를 모두 고정 크기(페이지/프레임)로 나누고 페이지 테이블로 대응시켜요. 구현이 단순하고 외부 단편화가 없지만, 마지막 페이지가 다 안 차면 내부 단편화가 생겨요. 세그멘테이션은 프로그램을 코드·데이터·스택처럼 의미 있는 단위(세그먼트)로 나누고, 세그먼트 테이블에 시작 위치와 길이를 적어요. 단위가 의미와 맞아 보호·공유가 쉽지만, 크기가 제각각이라 세그먼트 사이에 외부 단편화가 생길 수 있어요. Multics와 32비트 x86처럼 세그먼트와 페이징을 함께 쓴 시스템도 있었고, 현대 64비트 운영체제는 대부분 페이징 위주로 동작해요.",
                 "Paging divides both virtual and physical memory into fixed-size chunks (pages/frames) matched through a page table — simple to implement, with no external fragmentation, though a partly filled last page wastes space (internal fragmentation). Segmentation divides a program into meaningful units (code, data, stack) and records each one's start and length in a segment table. Units that match meaning make protection and sharing easier, but their varied sizes can leave gaps between segments (external fragmentation). Systems such as Multics and 32-bit x86 combined segments with paging; modern 64-bit operating systems rely mostly on paging.")),
    "glossary": [
        ("페이징", "Paging", ("메모리를 같은 크기 칸으로 자르는 방식.", "Cutting memory into same-size slots."), ("내용과 상관없이 크기만 보고 나눠요.", "Splits by size alone, whatever's inside.")),
        ("세그멘테이션", "Segmentation", ("메모리를 쓰임새 단위로 자르는 방식.", "Cutting memory by use."), ('코드·데이터·스택 구역 이야기는 여기서 봐요. → <a href="memlayout-ko.html">작업 공간을 구역으로 나눠 쓰는 규칙</a>', 'The code, data, and stack zones are covered here. → <a href="memlayout-en.html">the rule for dividing the workspace into zones</a>')),
        ("내부 단편화", "Internal Fragmentation", ("같은 크기 칸 안에 남는 자투리 공간.", "Leftover space wasted inside a fixed-size slot."), ("페이징에서 생겨요.", "Occurs in paging.")),
        ("외부 단편화", "External Fragmentation", ("덩어리와 덩어리 사이에 남아 못 쓰는 빈틈.", "Unusable gaps left between chunks."), ("세그멘테이션에서 생기기 쉬워요.", "Common in segmentation.")),
        ("페이지 테이블", "Page Table", ("가상 페이지와 실제 프레임의 대응표.", "The table matching virtual pages to real frames."), ('페이징의 핵심 구조예요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'The core structure of paging. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse mine</a>')),
        ("세그먼트 테이블", "Segment Table", ("세그먼트마다 시작 위치와 길이를 적은 표.", "The table recording each segment's start and length."), ("길이를 넘는 번지는 막아서 보호에도 쓰여요.", "Blocking addresses past the length also gives protection.")),
        ("세그멘테이션 페이징", "Segmented Paging", ("세그먼트를 다시 페이지로 자르는 혼합 방식.", "A hybrid that cuts each segment again into pages."), ("세그먼트로 보호·공유를 챙기고, 페이지로 외부 단편화를 피하려는 방식이에요.", "Segments handle protection and sharing; pages avoid external fragmentation.")),
        ("가상메모리", "Virtual Memory", ("메모리를 프로세스마다 전용 공간처럼 보여주는 가짜 지도.", "A fake map that shows each process memory as its own private space."), ('페이징·세그멘테이션은 이 지도를 구현하는 두 방법이에요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'Paging and segmentation are two ways to build this map. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse mine</a>')),
    ],
}
