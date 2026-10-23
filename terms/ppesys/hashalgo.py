from _draw import *
from _world import *


def bins(x, y, n, hl=-1, fill="#E9B44C"):
    """공구함 칸(해시 버킷) n개를 가로로 배치."""
    out = f'<g transform="translate({x},{y})">'
    w = 70
    for i in range(n):
        xx = i * (w + 8)
        f = "var(--accent-soft)" if i == hl else fill
        out += f'<rect x="{xx}" y="0" width="{w}" height="50" rx="4" fill="{f}" stroke="#C9822B" stroke-width="2"/>' + label(xx + w / 2, 32, str(i), 16, "#142033", cls="d")
    return out + '</g>'


def wrench(x, y, s=1.0, color="var(--accent)", num=None):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="-20" width="12" height="36" rx="4" fill="{color}"/><circle cx="0" cy="-22" r="10" fill="none" stroke="{color}" stroke-width="5"/>'
    if num is not None:
        out += label(0, 30, str(num), 11, "var(--ink)", cls="d")
    return out + '</g>'


# 1. 공구가 너무 많아서 하나 찾는 데 한참 걸려요
P1 = svg(300, sky(300)
         + toolbox(380, 200, 1.6)
         + person(560, 150, s=0.85, face=SWEAT, **MECH1)
         + label(380, 60, "⟦공구 50개 중에 14번 렌치를 찾아야 해요|need wrench #14 among fifty tools⟧", 13, "var(--ink)")
         + label(380, 270, "⟦하나씩 뒤지면 공구함 바닥까지 다 봐야 할 수도 있어요|searching one by one might mean checking the whole box⟧", 12, "var(--muted)"))

# 2. 처음부터 하나씩 뒤지면 너무 느려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + wrench(200, 150, 1.0, num=3) + wrench(260, 150, 1.0, num=27) + wrench(320, 150, 1.0, num=8) + wrench(380, 150, 1.0, num=14) + wrench(440, 150, 1.0, num=41)
         + label(320, 90, "⟦3? 27? 8? 아니네, 다음...|3? 27? 8? nope, next...⟧", 12, "var(--bad)", cls="d")
         + person(600, 150, s=0.8, face=FROWN, **MECH1)
         + label(380, 220, "⟦순서 없이 쌓아두면 매번 처음부터 뒤져야 해요|with no order, every search starts from scratch⟧", 13, "var(--ink)")
         + label(380, 270, "⟦번호만 보고 바로 칸을 짚을 규칙이 있으면 좋겠어요|a rule to point straight at the right slot would help⟧", 12, "var(--muted)"))

# 3. 해시 알고리즘 = 번호를 계산해 바로 칸을 짚는 규칙 (hero)
P3 = svg(340, sky(340)
         + bins(80, 160, 5, hl=4)
         + wrench(394, 120, 1.0, color="var(--good)", num=14)
         + label(394, 100, "⟦14 % 5 = 4|14 mod 5 = 4⟧", 13, "var(--accent)", cls="d")
         + person(560, 170, s=0.85, face=SMILE, **MECH2)
         + label(380, 30, "⟦해시 알고리즘 = 번호를 계산해 바로 칸을 짚는 규칙|hash algorithm: compute a number, point straight at the slot⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦뒤질 필요 없이 계산 한 번으로 칸을 알아요|one calculation tells you the slot — no searching⟧", 12, "var(--muted)"))

CALC_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M20 24 h24 M20 34 h24 M20 44 h14" stroke="var(--accent)" stroke-width="2.5"/>')
SLOT_I = icon('<rect x="10" y="20" width="44" height="26" rx="3" fill="var(--good)"/><path d="M32 10 v10" stroke="var(--ink)" stroke-width="3"/>')
COLLIDE_I = icon('<circle cx="24" cy="32" r="10" fill="var(--accent)"/><circle cx="40" cy="32" r="10" fill="var(--bad)"/><path d="M20 20 l24 24 M44 20 l-24 24" stroke="var(--ink)" stroke-width="2.5"/>')
CHAIN_I = icon('<rect x="8" y="24" width="18" height="16" rx="3" fill="var(--accent)"/><path d="M26 32 h10" stroke="var(--ink)" stroke-width="3"/><circle cx="44" cy="32" r="9" fill="var(--line)"/>')

# 4. 두 공구가 같은 칸을 가리킬 때(충돌) 처리법
P4 = svg(320, sky(320)
         + bins(100, 60, 5, hl=2)
         + wrench(230, 20, 0.8, color="var(--accent)", num=7) + wrench(280, 20, 0.8, color="var(--bad)", num=22)
         + label(250, 0, "⟦7 % 5 = 2, 22 % 5 = 2 — 같은 칸!|7 mod 5 = 2, 22 mod 5 = 2 — same slot!⟧", 12, "var(--bad)", cls="d")
         + queueboard(60, 160, 640, 130, "⟦충돌 처리법|handling the collision⟧",
                      ("⟦체이닝 — 같은 칸에 줄줄이 매달아 두기|chaining — hang them one after another in the slot⟧",
                       "⟦오픈 어드레싱 — 옆 빈 칸을 찾아 넣기|open addressing — slide into the next empty slot⟧"), 1.0))

# 5. 칸이 꽉 차면 다시 느려져요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + bins(50, 150, 4, hl=1)
         + label(190, 255, "⟦칸이 넉넉하면 거의 계산 한 번으로 끝나요|with enough slots, one calculation nearly always suffices⟧", 11, "var(--ink)")
         + person(560, 130, s=0.8, face=FROWN, **CHIEF)
         + label(560, 255, "⟦공구함이 꽉 차면 충돌이 늘어 다시 뒤지게 돼요|a full box means more collisions and more searching⟧", 11, "var(--ink)")
         + label(380, 300, "⟦빠르려면 칸 수를 공구 수보다 넉넉히 둬야 해요|staying fast means keeping more slots than tools⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "hashalgo", "order": 20,
    "title": ("번호만 계산해서 바로 칸을 짚기", "Computing a Number to Point Straight at the Slot"),
    "h1": ("<em>해시 알고리즘</em>이 뭐예요?", "What is a <em>Hash Algorithm</em>?"),
    "sub": ("해시 알고리즘을, 공구함에서 번호를 계산해 바로 알맞은 칸을 짚어 찾는 이야기로 풀어봤어요.",
            "Hash algorithms, told as a story about computing a number to point straight at the right slot in the toolbox."),
    "panels": [
        {"svg": P1, "alt": ("공구함 안에 수십 개의 공구가 뒤섞여 있고 정비사가 14번 렌치를 찾느라 진땀을 흘림", "Dozens of jumbled tools in the toolbox, the mechanic sweating to find wrench #14"),
         "caption": ("공구가 너무 많아서 하나 찾는 데 한참 걸려요.", "With so many tools, finding one takes forever."),
         "small": ("하나씩 뒤지면 공구함 바닥까지 다 봐야 할 수도 있어요.", "Searching one by one might mean checking the whole box.")},
        {"svg": P2, "alt": ("정비사가 번호가 뒤섞인 렌치들을 하나씩 뒤지며 지쳐함", "The mechanic wearily checks wrenches one by one in no particular order"),
         "caption": ("처음부터 하나씩 뒤지면 너무 느려요.", "Searching from scratch every time is too slow."),
         "small": ("번호만 보고 바로 칸을 짚을 규칙이 있으면 좋겠어요.", "A rule to point straight at the right slot would help.")},
        {"svg": P3, "hero": True, "alt": ("렌치 번호 14를 5로 나눈 나머지 4번 칸을 계산해 바로 짚어내고 정비사가 만족함", "Computing 14 mod 5 = 4 points straight at slot 4, the mechanic satisfied"),
         "caption": ("해시 알고리즘은 번호를 계산해 바로 칸을 짚는 규칙이에요.", "A hash algorithm computes a number to point straight at the slot."),
         "small": ("뒤질 필요 없이 계산 한 번으로 칸을 알아요.", "One calculation tells you the slot — no searching."),
         "tricks": (4, [
             (CALC_I, ("해시 함수로 계산", "Compute with a hash function"), ("번호를 규칙대로 계산해요", "computes a number by a fixed rule"), "calm"),
             (SLOT_I, ("칸을 바로 짚기", "Point straight at a slot"), ("계산값이 곧 칸 번호예요", "the result is the slot number itself")),
             (COLLIDE_I, ("가끔 겹침(충돌)", "Occasional collisions"), ("두 공구가 같은 칸을 가리킬 수 있어요", "two tools can point to the same slot"), "warm"),
             (CHAIN_I, ("겹치면 줄줄이 매달기", "Chain them when collided"), ("같은 칸에 여러 개를 매달아요", "hangs several items in one slot")),
         ])},
        {"svg": P4, "alt": ("렌치 7과 22가 둘 다 같은 칸(2번)을 계산해 충돌이 생기고, 체이닝과 오픈 어드레싱 두 해결법을 보여줌", "Wrenches 7 and 22 both compute slot 2, a collision — shown with two fixes: chaining and open addressing"),
         "caption": ("두 공구가 같은 칸을 가리킬 수 있어요(충돌).", "Two tools can point to the same slot — a collision."),
         "small": ("체이닝으로 줄줄이 매달거나, 옆 빈 칸을 찾아 넣어요.", "Handle it by chaining them together, or sliding into the next empty slot.")},
        {"svg": P5, "alt": ("왼쪽: 칸이 넉넉하면 계산 한 번으로 끝남. 오른쪽: 칸이 꽉 차면 충돌이 늘어 다시 뒤지게 됨", "Left: with enough slots, one calculation suffices. Right: a full box means more collisions and searching"),
         "caption": ("칸이 꽉 차면 다시 느려져요.", "A full toolbox slows things back down."),
         "small": ("빠르려면 칸 수를 공구 수보다 넉넉히 둬야 해요.", "Staying fast means keeping more slots than tools.")},
    ],
    "summary": (("<b>해시 알고리즘</b>은 데이터로 <b>번호를 계산</b>해 저장할 <b>칸(버킷)을 바로 짚는</b> 규칙으로, 거의 계산 한 번에 찾고 저장할 수 있게 해줘요.",
                 "A <b>hash algorithm</b> <b>computes a number</b> from the data to <b>point straight at a storage slot (bucket)</b>, so lookup and storage take roughly one calculation."),
                ("해시 알고리즘은 키 값을 해시 함수에 넣어 배열 인덱스(버킷 번호)로 변환하는 방법이에요. 이를 이용한 해시 테이블은 평균적으로 O(1)에 가까운 시간에 탐색·삽입이 가능해 처음부터 끝까지 훑는 선형 탐색(O(n))보다 훨씬 빨라요. 서로 다른 키가 같은 버킷으로 계산되는 충돌이 생기면 체이닝(같은 칸에 연결 리스트로 매달기)이나 오픈 어드레싱(다음 빈 칸을 찾아 넣기)으로 해결해요. 버킷 수 대비 데이터가 너무 많아지면(적재율이 높아지면) 충돌이 늘어 성능이 떨어져요. 이는 메시지 무결성을 확인하는 암호학적 해시 함수와는 다른, 자료구조·알고리즘 관점의 해시예요.",
                 "A hash algorithm feeds a key into a hash function to produce an array index (bucket number). A hash table built on this achieves near-O(1) average search and insertion, far faster than scanning everything with linear search (O(n)). When different keys hash to the same bucket — a collision — it's resolved by chaining (linking multiple items in one slot) or open addressing (sliding into the next free slot). As the load factor rises (too much data for too few buckets), collisions increase and performance drops. This is the data-structure/algorithm sense of 'hash', distinct from cryptographic hash functions used to verify message integrity.")),
    "glossary": [
        ("해시 함수", "Hash Function", ("번호를 계산해주는 규칙.", "The rule that computes the number."), ("같은 입력엔 항상 같은 칸을 줘요.", "Always gives the same slot for the same input.")),
        ("해시 테이블", "Hash Table", ("칸마다 공구를 넣어둔 공구함.", "The toolbox with tools sorted into slots."), ("평균 O(1)로 찾고 넣을 수 있어요.", "Average O(1) for lookup and insertion.")),
        ("버킷(슬롯)", "Bucket (Slot)", ("계산된 번호가 가리키는 칸.", "The slot the computed number points to."), ("해시값이 바로 칸 번호가 돼요.", "The hash value becomes the slot number.")),
        ("충돌", "Collision", ("서로 다른 공구가 같은 칸을 가리키는 것.", "Different tools pointing to the same slot."), ("체이닝이나 오픈 어드레싱으로 풀어요.", "Resolved with chaining or open addressing.")),
        ("체이닝", "Chaining", ("같은 칸에 줄줄이 매달아 두는 방식.", "Hanging multiple items one after another in the slot."), ("충돌한 공구를 리스트로 연결해요.", "Links the colliding items in a list.")),
        ("오픈 어드레싱", "Open Addressing", ("옆 빈 칸을 찾아 넣는 방식.", "Sliding into the next empty slot."), ("칸이 꽉 차면 찾기 어려워져요.", "Gets harder to find a spot as the table fills up.")),
        ("적재율", "Load Factor", ("칸 수 대비 들어있는 공구 비율.", "The ratio of tools stored to the number of slots."), ("너무 높아지면 충돌이 늘어요.", "Too high, and collisions rise.")),
        ("선형 탐색", "Linear Search", ("처음부터 하나씩 다 뒤지는 방식.", "Checking items one by one from the start."), ("해시 테이블보다 훨씬 느려요(O(n)).", "Much slower than a hash table — O(n).")),
    ],
}
