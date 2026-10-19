from _draw import *
from _world import *


def bay(x, y, w, h, fill, label_text, sub=None):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" fill="{fill}" stroke="#142033" stroke-width="2"/>' + label(w / 2, 22, label_text, 12, "#142033", cls="d")
    if sub:
        out += label(w / 2, h - 10, sub, 10, "#142033")
    return out + '</g>'


# 1. 차 한 대에 작업 공간을 내줬는데 어디에 뭘 둘지 몰라요
P1 = svg(300, sky(300)
         + car(380, 210, 1.1)
         + person(560, 160, s=0.85, face=EYES, **CHIEF)
         + "".join(f'<rect x="{200+i*40}" y="150" width="30" height="30" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="3 3"/>' for i in range(5))
         + label(380, 50, "⟦차 한 대에 작업 공간을 내줬어요|one car gets its own bay in the shop⟧", 13, "var(--ink)")
         + label(380, 270, "⟦설계도는 어디, 부품은 어디, 임시 작업대는 어디에 둘까요?|where go the blueprint, the parts, the temp table?⟧", 12, "var(--muted)"))

# 2. 아무 데나 두면 뒤섞여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + car(380, 200, 1.0)
         + "".join(f'<rect x="{220+(i%4)*70}" y="{130+(i//4)*40}" width="30" height="24" fill="var(--panel)" stroke="var(--bad)" stroke-width="2"/>' for i in range(8))
         + label(380, 80, "⟦설계도랑 임시 부품이 뒤섞여 있으면 헷갈려요|blueprint and temp parts jumbled together, confusing⟧", 12, "var(--bad)", cls="d")
         + person(600, 150, s=0.8, face=FROWN, **MECH1)
         + label(380, 270, "⟦구역을 나눠 정해두는 규칙이 필요해요|a fixed rule for dividing the space is needed⟧", 13, "var(--ink)"))

# 3. 프로세스 메모리 구조 = 작업 공간을 정해진 구역으로 나눠 쓰는 규칙 (hero)
P3 = svg(360, sky(360)
         + bay(260, 40, 240, 280, "#D9CBA3", "⟦코드(설계도)|code (blueprint)⟧")
         + car(430, 60, 0.0)
         + label(380, 30, "⟦프로세스 메모리 구조 = 작업 공간을 정해진 구역으로 나눠 쓰는 규칙|process memory layout fixes zones for the workspace⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦각 구역이 하는 일이 정해져 있어 안 헷갈려요|each zone has a fixed job, so nothing gets mixed up⟧", 12, "var(--muted)"))

CODE_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="none" stroke="var(--ink)" stroke-width="3"/><path d="M18 24 h28 M18 32 h28 M18 40 h18" stroke="var(--ink)" stroke-width="2.5"/>')
DATA_I = icon('<rect x="12" y="16" width="40" height="32" rx="4" fill="var(--good)"/><circle cx="24" cy="32" r="4" fill="#142033"/><circle cx="40" cy="32" r="4" fill="#142033"/>')
HEAP_I = icon('<path d="M32 50 V18" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M24 26 l8 -10 l8 10" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
STACK_I = icon('<path d="M32 14 V46" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M24 38 l8 10 l8 -10" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. 네 구역이 양쪽에서 자라나는 구조
P4 = svg(360, '<rect width="760" height="360" fill="var(--sky)"/>'
         + bay(260, 20, 240, 60, "#D9CBA3", "⟦코드(설계도)|code⟧")
         + bay(260, 80, 240, 50, "#B7C9A8", "⟦데이터/BSS(초기 부품)|data/BSS (initial parts)⟧")
         + bay(260, 130, 240, 90, "var(--accent-soft)", "⟦힙 — 쓸수록 아래로 늘어남|heap — grows downward as used⟧", "↓")
         + bay(260, 220, 240, 20, "var(--bad-soft)", "⟦충돌하면 메모리 부족!|collision = out of memory!⟧")
         + bay(260, 240, 240, 90, "var(--good-soft)", "⟦스택 — 쓸수록 위로 늘어남|stack — grows upward as used⟧", "↑")
         + label(380, 340, "⟦힙과 스택이 서로를 향해 자라다 부딪히면 문제예요|heap and stack grow toward each other — collision is trouble⟧", 12, "var(--ink)"))

# 5. 동적 할당은 편하지만 안 돌려주면 쌓여요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **MECH2)
         + label(190, 240, "⟦필요할 때 힙에서 더 받아 쓰면 편해요(동적 할당)|grabbing more from the heap on demand is handy⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **MECH1)
         + label(570, 240, "⟦다 쓰고 안 돌려주면 공간이 계속 쌓여요(메모리 누수)|forgetting to give it back piles up — a memory leak⟧", 11, "var(--ink)")
         + label(380, 282, "⟦받은 만큼 꼭 돌려줘야 작업 공간이 안전해요|what you take, you must give back — to keep the space safe⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "memlayout", "order": 17,
    "title": ("작업 공간을 구역으로 나눠 쓰는 규칙", "The Rule for Dividing the Workspace into Zones"),
    "h1": ("<em>프로세스 메모리 구조</em>가 뭐예요?", "What is a <em>Process Memory Layout</em>?"),
    "sub": ("프로세스 메모리 구조와 동적 메모리 할당을, 차 한 대에 내준 작업 공간을 구역으로 나눠 쓰는 이야기로 풀어봤어요.",
            "Process memory layout and dynamic allocation, told as a story about dividing one car's workspace into fixed zones."),
    "panels": [
        {"svg": P1, "alt": ("차 한 대가 작업 공간을 받았지만 구역이 정해지지 않아 정비반장이 고민함", "A car gets a bay, but with no zones marked out, the chief ponders"),
         "caption": ("작업 공간을 받았는데 어디에 뭘 둘지 몰라요.", "The car has a bay, but it's unclear where anything goes."),
         "small": ("설계도, 부품, 임시 작업대를 어디에 둘까요?", "Where go the blueprint, the parts, the temp table?")},
        {"svg": P2, "alt": ("설계도와 임시 부품이 아무렇게나 뒤섞여 있어 정비사가 헷갈려함", "Blueprint and temp parts are jumbled together, confusing the mechanic"),
         "caption": ("아무 데나 두면 뒤섞여요.", "Put things anywhere, and they get jumbled."),
         "small": ("구역을 나눠 정해두는 규칙이 필요해요.", "A fixed rule for dividing the space is needed.")},
        {"svg": P3, "hero": True, "alt": ("작업 공간이 구역별로 깔끔하게 나뉘어 있음", "The workspace is now neatly divided into zones"),
         "caption": ("프로세스 메모리 구조는 작업 공간을 정해진 구역으로 나눠 쓰는 규칙이에요.", "Process memory layout fixes zones for the workspace."),
         "small": ("각 구역이 하는 일이 정해져 있어 헷갈리지 않아요.", "Each zone has a fixed job, so nothing gets mixed up."),
         "tricks": (4, [
             (CODE_I, ("코드 영역", "Code segment"), ("바뀌지 않는 설계도예요", "the unchanging blueprint"), "calm"),
             (DATA_I, ("데이터/BSS 영역", "Data/BSS segment"), ("처음부터 준비된 부품이에요", "parts prepared from the start")),
             (HEAP_I, ("힙 — 쓸수록 늘어남", "Heap — grows as used"), ("필요할 때마다 더 받아요(동적 할당)", "requests more as needed (dynamic allocation)")),
             (STACK_I, ("스택 — 쓸수록 쌓임", "Stack — piles up as used"), ("작업이 끝나면 저절로 사라져요", "clears itself once work finishes"), "warm"),
         ])},
        {"svg": P4, "alt": ("코드, 데이터/BSS, 힙, 스택 네 구역이 세로로 쌓여 있고 힙은 아래로 스택은 위로 서로를 향해 자람", "Four stacked zones — code, data/BSS, heap, stack — with heap and stack growing toward each other"),
         "caption": ("힙은 아래로, 스택은 위로 자라요.", "The heap grows downward; the stack grows upward."),
         "small": ("둘이 부딪히면 메모리가 부족해져요.", "If they collide, memory runs out.")},
        {"svg": P5, "alt": ("왼쪽: 필요할 때 힙에서 더 받는 동적 할당이 편리함. 오른쪽: 돌려주지 않으면 공간이 쌓이는 메모리 누수", "Left: dynamic allocation from the heap is handy. Right: not giving it back causes a memory leak"),
         "caption": ("동적 할당은 편하지만 책임이 따라요.", "Dynamic allocation is handy, but comes with responsibility."),
         "small": ("받은 만큼 꼭 돌려줘야 작업 공간이 안전해요.", "What you take, you must give back, to keep the space safe.")},
    ],
    "summary": (("<b>프로세스 메모리 구조</b>는 작업 공간을 <b>코드·데이터·힙·스택</b> 구역으로 나누는 규칙이고, <b>동적 메모리 할당</b>은 힙에서 <b>필요한 만큼 빌렸다가 돌려주는 것</b>이에요.",
                 "A <b>process memory layout</b> fixes zones — <b>code, data, heap, stack</b> — for the workspace, and <b>dynamic memory allocation</b> is <b>borrowing from the heap as needed, then giving it back</b>."),
                ("프로세스의 가상 메모리는 보통 낮은 주소부터 코드(텍스트) 영역, 초기화된/초기화되지 않은 전역변수인 데이터·BSS 영역, 실행 중 malloc/new 등으로 늘어나는 힙, 그리고 함수 호출마다 쌓였다 사라지는 스택 순으로 배치돼요. 힙은 낮은 주소에서 높은 주소로, 스택은 높은 주소에서 낮은 주소로 자라며 서로를 향해 커지는데, 둘이 충돌하면 메모리 부족 오류가 나요. 동적 할당된 메모리를 free()/delete로 반납하지 않으면 메모리 누수가 쌓여요.",
                 "A process's virtual memory is typically laid out, from low addresses up, as the code (text) segment, the data/BSS segment for initialized and uninitialized global variables, the heap which grows via malloc/new during execution, and the stack which grows and shrinks with each function call. The heap grows from low to high addresses while the stack grows from high to low, each toward the other — colliding causes an out-of-memory error. Failing to release dynamically allocated memory with free()/delete accumulates as a memory leak.")),
    "glossary": [
        ("코드(텍스트) 영역", "Code (Text) Segment", ("바뀌지 않는 설계도가 있는 구역.", "The zone holding the unchanging blueprint."), ("실행 파일의 명령어가 들어있어요.", "Holds the program's instructions.")),
        ("데이터/BSS 영역", "Data/BSS Segment", ("처음부터 준비된 전역 부품 구역.", "The zone for globally prepared parts."), ("초기화 여부로 데이터와 BSS가 나뉘어요.", "Split by whether the value is initialized.")),
        ("힙", "Heap", ("필요할 때마다 더 받는 창고.", "The warehouse you draw more from as needed."), ("낮은 주소에서 높은 주소로 자라요.", "Grows from low to high addresses.")),
        ("스택", "Stack", ("함수 호출마다 쌓였다 사라지는 작업대.", "The temp table that piles up and clears with each call."), ("높은 주소에서 낮은 주소로 자라요.", "Grows from high to low addresses.")),
        ("동적 메모리 할당", "Dynamic Memory Allocation", ("힙에서 필요한 만큼 빌리는 것.", "Borrowing as much as needed from the heap."), ("malloc/new 로 빌리고 free/delete 로 돌려줘요.", "Borrowed with malloc/new, returned with free/delete.")),
        ("메모리 누수", "Memory Leak", ("빌린 공간을 안 돌려줘서 쌓이는 것.", "Space that piles up because it's never returned."), ("오래 켜둔 프로그램을 느리게 만들어요.", "Slows down long-running programs.")),
        ("스택 오버플로", "Stack Overflow", ("작업대가 코드 영역까지 밀고 들어가는 사고.", "The temp table pushing all the way into the code zone."), ("재귀 호출이 너무 깊을 때 자주 나요.", "Common with excessively deep recursion.")),
        ("힙-스택 충돌", "Heap-Stack Collision", ("힙과 스택이 서로를 향해 자라다 부딪히는 것.", "Heap and stack growing toward each other until they collide."), ("메모리 부족 오류의 전형적인 원인이에요.", "A classic cause of out-of-memory errors.")),
    ],
}
