from _draw import *
from _world import *


def shelfbox(x, y, w, h, text, filled=True, s=1.0):
    fill = "#E9B44C" if filled else "var(--panel)"
    stroke = "#C9822B" if filled else "var(--bad)"
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
    out += label(w / 2, h / 2 + 5, text, 12, "#142033", cls="d")
    return out + '</g>'


def basement(x, y, s=1.0):
    """지하 보관소(디스크) — 사다리 아래 작은 창고."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" y="0" width="72" height="44" fill="#6E4A2E"/>'
            f'<path d="M-36 0 L0 -20 L36 0 Z" fill="#5A3B22"/>'
            f'<rect x="-14" y="10" width="28" height="24" fill="var(--night)"/></g>')


# 1. 내 선반인 줄 알았는데, 꺼내보니 빈 칸이에요
P1 = svg(340, sky(340)
         + shelfbox(140, 100, 60, 50, "P0") + shelfbox(210, 100, 60, 50, "P1") + shelfbox(280, 100, 60, 50, "P2")
         + shelfbox(140, 160, 60, 50, "P3", filled=False) + shelfbox(210, 160, 60, 50, "P4") + shelfbox(280, 160, 60, 50, "P5")
         + person(70, 215, s=0.8, face=EYES, **MECH1)
         + label(380, 30, "⟦내 선반인데, P3 칸을 열어보니 비어 있어요|it's my own shelf — but slot P3 is empty when I open it⟧", 13, "var(--ink)", cls="d")
         + label(380, 330, "⟦분명 \"내 선반\"이라고 들었는데, 실제로 다 차 있진 않아요|I was told it's \"my own shelf\" — but it's not all really there⟧", 12, "var(--ink)"))

# 2. 모두에게 진짜 전용 창고를 다 줄 순 없어요
P2 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + person(140, 140, s=0.75, face=FROWN, **MECH1) + shelfbox(70, 250, 140, 50, "⟦정비사1 전용|MECH1 ONLY⟧", True, 0.9)
         + person(440, 140, s=0.75, face=FROWN, **MECH2) + shelfbox(370, 250, 140, 50, "⟦정비사2 전용|MECH2 ONLY⟧", True, 0.9)
         + person(680, 150, s=0.6, face=FROWN, **CUSTOMER)
         + label(380, 40, "⟦모두에게 진짜 창고를 통째로 하나씩 줄 순 없어요|you can't give everyone a whole real warehouse of their own⟧", 13, "var(--ink)", cls="d")
         + label(380, 330, "⟦정비사가 늘어날수록 진짜 선반 공간은 금방 부족해져요|real shelf space runs out fast as more mechanics join⟧", 12, "var(--ink)"))

# 3. 가상메모리 = 창고 전체를 내 것처럼 보여주는 가짜 지도 (hero)
P3 = svg(360, sky(360)
         + shelfbox(90, 110, 60, 50, "P0") + shelfbox(160, 110, 60, 50, "P1") + shelfbox(230, 110, 60, 50, "P2")
         + label(170, 90, "⟦내가 보는 선반(가상)|what I see (virtual)⟧", 11, "var(--muted)")
         + shelfbox(480, 170, 60, 50, "F0") + shelfbox(550, 170, 60, 50, "F1")
         + label(515, 150, "⟦진짜 선반(물리)|the real shelf (physical)⟧", 11, "var(--muted)")
         + basement(640, 260)
         + label(640, 225, "⟦디스크|disk⟧", 10, "var(--muted)")
         + '<path d="M120 160 Q300 170 505 195" stroke="var(--good)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + '<path d="M190 160 Q350 180 575 195" stroke="var(--good)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + '<path d="M260 160 Q450 220 635 248" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
         + label(380, 20, "⟦가상메모리 = 창고 전체를 내 것처럼 보여주는 가짜 지도|virtual memory = a fake map that makes the whole warehouse look like mine⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦지도의 각 칸(페이지)이 실제 선반 칸(프레임)을 가리켜요, 없으면 디스크에서 가져와요|each map square (page) points to a real shelf slot (frame) — or fetches from disk if it's not there⟧", 11, "var(--muted)"))

# 4. 페이지 테이블: 가상 페이지 ↔ 실제 프레임
P4 = svg(340, sky(340)
         + queueboard(90, 30, 300, 220, "⟦페이지 테이블|PAGE TABLE⟧",
                      ["P0 → F0", "P1 → F1", "P2 → ⟦디스크에(폴트)|on disk (fault)⟧"], 1.0)
         + person(560, 140, s=0.8, face=EYES, **CHIEF)
         + label(560, 265, "⟦반장(OS)이 이 지도를 관리해요|the chief (OS) manages this map⟧", 11, "var(--muted)")
         + label(380, 315, "⟦P2를 찾으면 \"페이지 폴트\" — 디스크에서 선반으로 올려와요|looking for P2 triggers a \"page fault\" — it's hauled up from disk⟧", 12, "var(--ink)"))

# 5. 너무 자주 들락날락하면 — 스와핑으로 오히려 느려져요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + shelfbox(140, 110, 100, 40, "⟦딱 맞게 올라와 있어요|just enough is loaded⟧", True, 0.8)
         + label(190, 190, "⟦선반에 다 있으면|when it's all on the shelf⟧", 11, "var(--ink)")
         + label(190, 208, "⟦빠르게 일해요|work moves fast⟧", 11, "var(--ink)")
         + shelfbox(520, 110, 100, 40, "⟦계속 들락날락|constant swap in/out⟧", False, 0.8)
         + label(570, 190, "⟦디스크를 너무 자주 오가면|too many trips to disk⟧", 11, "var(--ink)")
         + label(570, 208, "⟦스와핑으로 더 느려요|swapping slows it down⟧", 11, "var(--ink)")
         + label(380, 265, "⟦가상메모리는 \'더 많아 보이게\'는 해도, 진짜 선반 속도를 늘려주진 않아요|virtual memory makes it look bigger — it doesn't make the real shelf faster⟧", 12, "var(--ink)", cls="d"))

MAP_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h28 M18 30 h28 M18 40 h18" stroke="#142033" stroke-width="2.5"/>')
PAGE_I = icon('<rect x="16" y="10" width="32" height="20" rx="3" fill="var(--accent)"/>')
TABLE_I = icon('<path d="M10 20 h44 M10 32 h44 M10 44 h44" stroke="var(--good)" stroke-width="3"/><path d="M10 14 v36 M54 14 v36" stroke="var(--good)" stroke-width="3"/>')
FAULT_I = icon('<path d="M20 10 l24 24 l-24 24 l-10 -10 l14 -14 l-14 -14z" fill="var(--bad)"/>')

PAGE = {
    "slug": "virtualmem", "order": 4,
    "title": ("창고 전체를 내 것처럼 보여주는 가짜 지도", "The Fake Map That Makes the Whole Warehouse Mine"),
    "h1": ("<em>가상메모리·페이징</em>이 뭐예요?", "What is <em>Virtual Memory and Paging</em>?"),
    "sub": ("가상메모리와 페이징을, 창고 전체를 내 전용 공간처럼 보여주는 가짜 지도 이야기로 풀어봤어요.",
            "Virtual memory and paging, told as a story about a fake map that makes the whole warehouse look like your own private space."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 자기 선반인 줄 알고 P3 칸을 열었는데 비어 있음", "A mechanic opens slot P3 on what they think is their own shelf, and it's empty"),
         "caption": ("내 선반인데, 한 칸을 열어보니 비어 있어요.", "It's my own shelf — but one slot is empty when I open it."),
         "small": ("\"내 선반\"이라고 들었는데, 실제로 다 차 있진 않아요.", "I was told it's mine — but it's not all really there.")},
        {"svg": P2, "alt": ("정비사마다 전용 창고를 통째로 주려 하지만, 창고 공간이 금방 부족해짐", "Trying to give each mechanic a whole private warehouse quickly runs out of real shelf space"),
         "caption": ("모두에게 진짜 창고를 통째로 줄 순 없어요.", "You can't give everyone a whole real warehouse."),
         "small": ("정비사가 늘수록 진짜 선반 공간은 금방 부족해져요.", "Real shelf space runs out fast as more mechanics join.")},
        {"svg": P3, "hero": True, "alt": ("가상 선반 칸들이 화살표로 실제 선반 칸을 가리키고, 하나는 지하 디스크를 가리킴", "Virtual shelf slots point via arrows to real shelf slots, and one points down to the disk basement"),
         "caption": ("가상메모리 = 창고 전체를 내 것처럼 보여주는 가짜 지도예요.", "Virtual memory = a fake map making the whole warehouse look like mine."),
         "small": ("지도의 각 칸(페이지)이 실제 선반 칸(프레임)을 가리켜요.", "Each map square (page) points to a real shelf slot (frame)."),
         "tricks": (4, [
             (MAP_I, ("가상 주소", "Virtual Address"), ("내가 보는 가짜 지도 번지", "the fake map address I see")),
             (PAGE_I, ("페이지", "Page"), ("지도를 자른 작은 칸 하나", "one small square the map is cut into"), "calm"),
             (TABLE_I, ("페이지 테이블", "Page Table"), ("가상 칸 ↔ 진짜 칸 대응표", "the table matching virtual slot to real slot")),
             (FAULT_I, ("페이지 폴트", "Page Fault"), ("없으면 디스크에서 불러와요", "not there? fetch it from disk"), "warm"),
         ])},
        {"svg": P4, "alt": ("페이지 테이블이 P0·P1은 실제 프레임에, P2는 디스크(폴트)에 연결됨을 보여줌", "The page table maps P0 and P1 to real frames, while P2 points to disk — a fault"),
         "caption": ("페이지 테이블이 가상 페이지를 실제 프레임에 연결해요.", "The page table maps virtual pages to real frames."),
         "small": ("P2를 찾으면 \"페이지 폴트\" — 디스크에서 올려와요.", "Looking for P2 triggers a \"page fault\" — fetched from disk.")},
        {"svg": P5, "alt": ("왼쪽: 필요한 만큼만 선반에 있어 빠름. 오른쪽: 너무 자주 디스크를 오가 스와핑으로 느려짐", "Left: just enough is on the shelf — fast. Right: too much back-and-forth with disk — swapping slows it down"),
         "caption": ("너무 자주 들락날락하면 오히려 느려져요.", "Too much back-and-forth actually slows things down."),
         "small": ("가상메모리는 \'더 많아 보이게\'는 해도, 진짜 속도를 늘려주진 않아요.", "Virtual memory makes it look bigger — it doesn't make the real shelf faster.")},
    ],
    "summary": (("<b>가상메모리</b> = 창고(메모리)가 작아도 모두에게 <b>전용 창고처럼 보이는 가짜 지도</b>를 주고, <b>페이지</b> 단위로 필요한 것만 실제 선반에 올리는 방법.",
                 "<b>Virtual memory</b> = giving everyone a fake map that looks like their own warehouse, even though the real one is small, and loading only what's needed onto the real shelf in <b>page</b>-sized chunks."),
                ("가상메모리는 프로세스마다 독립된 가상 주소 공간을 주어, 물리 메모리보다 커 보이게 하고 프로세스끼리 서로의 메모리를 침범하지 못하게 해요. 페이징은 가상/물리 메모리를 고정 크기 페이지로 나눠 페이지 테이블로 매핑하고, 필요한 페이지가 물리 메모리에 없으면 페이지 폴트가 나서 디스크(스왑 영역)에서 가져와요. 폴트가 너무 잦으면 스래싱(thrashing)이 일어나 전체 성능이 떨어져요.",
                 "Virtual memory gives each process its own independent virtual address space — making memory look larger than it physically is, and keeping processes from touching each other's memory. Paging splits virtual and physical memory into fixed-size pages mapped through a page table; a needed page missing from physical memory triggers a page fault, fetched from disk (swap space). Too many faults cause thrashing, which drags down overall performance.")),
    "glossary": [
        ("가상 주소", "Virtual Address", ("내가 보는 가짜 지도의 번지.", "The address on the fake map I see."), ("진짜 선반 위치와는 따로 움직여요.", "It moves independently of the real shelf location.")),
        ("페이지/프레임", "Page/Frame", ("지도의 칸(페이지)과 진짜 선반 칸(프레임).", "A map square (page) and a real shelf slot (frame)."), ("같은 크기로 잘라서 맞춰요.", "Both are cut to the same size so they line up.")),
        ("페이지 테이블", "Page Table", ("가상 칸과 진짜 칸의 대응표.", "The table matching virtual slots to real ones."), ("반장(OS)이 관리해요.", "Managed by the chief (the OS).")),
        ("페이지 폴트/스와핑", "Page Fault/Swapping", ("찾는 칸이 없어 디스크에서 올려오는 일.", "Fetching a missing slot's contents up from disk."), ("너무 잦으면 스래싱으로 느려져요.", "Too often, and it turns into slow thrashing.")),
        ("캐시 메모리", "Cache Memory", ("자주 쓰는 공구만 담는 작은 공구함.", "A small toolbox holding only the frequent tools."), ('더 빠른 층위의 \'가까운 저장공간\'이에요. → <a href="cachemem-ko.html">자주 쓰는 공구만 담는 공구함</a>', 'A faster, closer storage layer. → <a href="cachemem-en.html">the toolbox that holds only the frequent tools</a>')),
        ("프로세스", "Process", ("독립된 차 한 대, 독립된 메모리 공간.", "One independent car — one independent memory space."), ('가상 주소 공간은 프로세스마다 따로 가져요. → <a href="processthread-ko.html">같은 차, 여러 손</a>', 'Each process gets its own virtual address space. → <a href="processthread-en.html">one car, many hands</a>')),
        ("교착상태", "Deadlock", ("서로의 열쇠를 기다리며 영원히 멈춤.", "Frozen forever, each waiting on the other's key."), ('자원이 한정된 건 메모리도 리프트도 마찬가지예요. → <a href="deadlockstarve-ko.html">서로의 열쇠를 기다리며 멈춘 정비공장</a>', 'Limited resources cause trouble whether it\'s memory or the lift. → <a href="deadlockstarve-en.html">the garage frozen waiting on each other\'s keys</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("칸 수가 늘 때 찾는 시간이 느는 정도.", "How fast lookup time grows as slots multiply."), ('페이지 테이블 조회 비용도 이 자로 재요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'Page-table lookup cost is measured with the same ruler. → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
    ],
}
