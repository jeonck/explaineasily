from _draw import *
from _world import *


def shelf_box(x, y, w, h, n, fill="#E9B44C"):
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="#5A3B22"/>'
    bw = (w - 8) / n
    for i in range(n):
        out += f'<rect x="{4 + i * bw}" y="4" width="{bw - 4}" height="{h - 8}" rx="2" fill="{fill}"/>'
    return out + '</g>'


def mini_shelf(x, y, s, fill, border="#8B5E3C"):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-18" width="52" height="36" rx="4" fill="{fill}" stroke="{border}" stroke-width="2"/></g>'


# 1. 지금 창고(NAND)는 쓰기 전에 꼭 지워야 해요
P1 = svg(300, sky(300)
         + shelf_box(260, 150, 240, 70, 5)
         + person(560, 160, s=0.85, face=SWEAT, **MECH1)
         + label(380, 60, "⟦이 칸에 새 부품을 넣기 전에 통째로 비워야 해요|this slot must be emptied whole before new parts go in⟧", 13, "var(--ink)")
         + label(380, 270, "⟦자주 바꿔야 하는 부품엔 좀 느리고 번거로워요|a bit slow and fussy for parts that change often⟧", 12, "var(--muted)"))

# 2. 더 빠르게 바로바로 바꿔 쓸 창고는 없을까
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(260, 150, s=0.85, face=EYES, **CHIEF)
         + shelf_box(400, 150, 200, 60, 4)
         + label(500, 230, "⟦지우고 다시 쓰는데 시간이 걸려요|erasing and rewriting takes time⟧", 12, "var(--bad)", cls="d")
         + label(380, 70, "⟦더 빠르게 바로바로 바꿔 쓰는 창고는 없을까요?|isn't there a faster, swap-in-place warehouse?⟧", 13, "var(--ink)")
         + label(380, 260, "⟦저장 방식 자체가 다른 차세대 창고들이 있어요|there are next-gen warehouses with a different storage trick⟧", 12, "var(--muted)"))

# 3. 차세대 비휘발성 메모리 = 다른 방식으로 꺼져도 기억하는 새 창고들 (hero)
P3 = svg(340, sky(340)
         + mini_shelf(160, 170, 1.3, "#5B9BD5") + label(160, 230, "⟦FeRAM|FeRAM⟧", 13, "var(--ink)", cls="d")
         + mini_shelf(380, 170, 1.3, "#7B3FA0") + label(380, 230, "⟦MRAM|MRAM⟧", 13, "var(--ink)", cls="d")
         + mini_shelf(600, 170, 1.3, "#C9822B") + label(600, 230, "⟦PRAM|PRAM⟧", 13, "var(--ink)", cls="d")
         + label(380, 30, "⟦차세대 비휘발성 메모리 = 다른 방식으로 꺼져도 기억하는 새 창고들|next-gen NVM: new warehouses that remember off-power, by different tricks⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦통째로 안 지워도 바로바로 바꿔 쓸 수 있어요|swap parts in place without erasing the whole slot⟧", 12, "var(--muted)"))

FAST_I = icon('<path d="M14 50 L34 14 L34 32 L50 14 L30 50 L30 32 Z" fill="var(--accent)"/>')
DURABLE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l7 8 l14 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
DENSE_I = icon('<rect x="10" y="10" width="14" height="14" fill="var(--accent)"/><rect x="26" y="10" width="14" height="14" fill="var(--accent)"/><rect x="42" y="10" width="14" height="14" fill="var(--accent)"/><rect x="10" y="26" width="14" height="14" fill="var(--accent)"/><rect x="26" y="26" width="14" height="14" fill="var(--accent)"/>')
PRICE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 20 v24 M24 26 h16 M24 38 h16" stroke="var(--bad)" stroke-width="3"/>')

# 4. 세 창고 비교표
P4 = svg(340, sky(340)
         + queueboard(40, 40, 340, 270, "⟦FeRAM — 강유전체 방식|FeRAM — ferroelectric⟧",
                      ("⟦쓰기가 아주 빨라요|very fast writes⟧", "⟦다만 용량은 작은 편|but smaller capacity⟧",
                       "⟦카드·계량기 등에 써요|used in cards, meters⟧"), 1.0)
         + queueboard(400, 40, 320, 270, "⟦MRAM — 자기 방식|MRAM — magnetic⟧",
                      ("⟦쓰기 내구성이 매우 높아요|very high write endurance⟧", "⟦속도도 빠른 편이에요|fairly fast too⟧",
                       "⟦값은 아직 비싸요|still pricier⟧"), 1.0, hl=0))

# 5. PRAM까지 — 쓰임새는 상황에 따라 달라요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + mini_shelf(190, 160, 1.4, "#C9822B")
         + label(190, 250, "⟦PRAM — 상변화 방식, 속도·밀도 균형이 좋아요|PRAM — phase-change, a good speed/density balance⟧", 11, "var(--ink)")
         + shelf_box(500, 160, 180, 60, 4)
         + label(590, 250, "⟦그래도 NAND는 여전히 가장 싸고 큰 대용량 창고예요|NAND is still the cheapest, biggest bulk warehouse⟧", 11, "var(--ink)")
         + label(380, 282, "⟦완벽한 창고는 없어요 — 속도·내구성·용량·가격을 저울질해요|no perfect warehouse — it's a trade-off of speed, endurance, size, price⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "nextnvm", "order": 21,
    "title": ("지우지 않고 바로바로 바꿔 쓰는 새 창고들", "New Warehouses That Swap in Place, No Erasing Needed"),
    "h1": ("<em>차세대 비휘발성 메모리</em>가 뭐예요?", "What is <em>Next-Generation Non-Volatile Memory</em>?"),
    "sub": ("FeRAM·MRAM·PRAM 같은 차세대 비휘발성 메모리를, 지우지 않고도 바로바로 바꿔 쓸 수 있는 새 창고 이야기로 풀어봤어요.",
            "Next-gen non-volatile memory — FeRAM, MRAM, PRAM — told as a story about new warehouses that swap parts in place, no erasing needed."),
    "panels": [
        {"svg": P1, "alt": ("NAND 창고에서 한 칸을 통째로 비워야 새 부품을 넣을 수 있어 정비사가 번거로워함", "The mechanic finds it fussy that a NAND slot must be emptied whole before new parts fit"),
         "caption": ("지금 창고는 쓰기 전에 꼭 지워야 해요.", "The current warehouse must be erased before writing."),
         "small": ("자주 바꿔야 하는 부품엔 좀 느리고 번거로워요.", "A bit slow and fussy for parts that change often.")},
        {"svg": P2, "alt": ("정비반장이 더 빠르게 바로 바꿔 쓸 수 있는 창고를 고민함", "The chief mechanic wonders if a faster, swap-in-place warehouse exists"),
         "caption": ("더 빠르게 바로바로 바꿔 쓸 창고는 없을까요?", "Isn't there a faster, swap-in-place warehouse?"),
         "small": ("저장 방식 자체가 다른 차세대 창고들이 있어요.", "There are next-gen warehouses with a different storage trick.")},
        {"svg": P3, "hero": True, "alt": ("FeRAM, MRAM, PRAM 세 가지 새 창고가 나란히 서 있음", "Three new warehouses — FeRAM, MRAM, PRAM — stand side by side"),
         "caption": ("차세대 비휘발성 메모리는 다른 방식으로 꺼져도 기억하는 새 창고들이에요.", "Next-gen NVM is new warehouses that remember off-power, by different tricks."),
         "small": ("통째로 안 지워도 바로바로 바꿔 쓸 수 있어요.", "You can swap parts in place without erasing the whole slot."),
         "tricks": (4, [
             (FAST_I, ("쓰기 속도", "Write speed"), ("지우지 않고 바로 바꿔 빨라요", "swaps in place — no erase needed, so it's fast"), "calm"),
             (DURABLE_I, ("쓰기 내구성", "Write endurance"), ("몇 번이고 다시 써도 오래가요", "holds up through many rewrites")),
             (DENSE_I, ("저장 밀도", "Storage density"), ("한 칸에 얼마나 많이 담기는지예요", "how much fits in one slot")),
             (PRICE_I, ("가격", "Price"), ("아직은 NAND보다 비싼 편이에요", "still pricier than NAND"), "warm"),
         ])},
        {"svg": P4, "alt": ("FeRAM은 쓰기가 빠르지만 용량이 작고, MRAM은 쓰기 내구성이 매우 높고 속도도 빠르지만 비싼 비교표", "A board comparing FeRAM (fast writes, small capacity) and MRAM (very high endurance, fast, pricier)"),
         "caption": ("FeRAM과 MRAM은 강점이 서로 달라요.", "FeRAM and MRAM each have different strengths."),
         "small": ("FeRAM은 속도, MRAM은 내구성이 강점이에요.", "FeRAM's strength is speed; MRAM's is endurance.")},
        {"svg": P5, "alt": ("왼쪽: PRAM은 속도와 밀도의 균형이 좋음. 오른쪽: NAND는 여전히 가장 싸고 큰 대용량 창고임", "Left: PRAM balances speed and density well. Right: NAND remains the cheapest, biggest bulk warehouse"),
         "caption": ("PRAM까지 — 쓰임새는 상황에 따라 달라요.", "And PRAM — the right choice depends on the situation."),
         "small": ("완벽한 창고는 없어요, 속도·내구성·용량·가격을 저울질해요.", "No perfect warehouse — it's a trade-off of speed, endurance, size, and price.")},
    ],
    "summary": (("<b>차세대 비휘발성 메모리</b>는 <b>FeRAM·MRAM·PRAM</b>처럼, 플래시(NAND/NOR)와는 <b>다른 저장 방식</b>으로 꺼져도 기억하면서 <b>빠르고 오래 쓸 수 있는</b> 새 메모리들이에요.",
                 "<b>Next-generation non-volatile memory</b> — <b>FeRAM, MRAM, PRAM</b> — are new memories that remember without power using a <b>different storage mechanism</b> than flash (NAND/NOR), aiming for <b>speed and long write endurance</b>."),
                ("차세대 비휘발성 메모리는 플래시처럼 쓰기 전에 블록을 통째로 지울 필요 없이 바이트 단위로 즉시 덮어쓸 수 있는 메모리들을 말해요. FeRAM(강유전체 메모리)은 쓰기 속도가 매우 빠르지만 집적도가 낮아 소용량에 적합하고, MRAM(자기저항 메모리)은 쓰기 내구성이 사실상 무한에 가깝고 속도도 빠르지만 비용이 더 들며, PRAM(상변화 메모리)은 상변화 물질의 결정/비결정 상태를 이용해 속도와 집적도의 균형이 좋아요. 플래시메모리(NAND)는 여전히 대용량·저비용 저장에서 강점을 유지해요.",
                 "Next-generation non-volatile memories can overwrite at the byte level instantly, without erasing a whole block first the way flash does. FeRAM (ferroelectric RAM) writes very fast but has lower density, suiting small capacities. MRAM (magnetoresistive RAM) offers near-unlimited write endurance and good speed, at a higher cost. PRAM (phase-change RAM) uses a material's crystalline/amorphous states for a good balance of speed and density. Flash (NAND) still leads for high-capacity, low-cost storage.")),
    "glossary": [
        ("FeRAM", "FeRAM", ("쓰기가 아주 빠른 작은 창고.", "A small warehouse with very fast writes."), ("강유전체 물질의 분극 방향을 이용해요.", "Uses the polarization direction of a ferroelectric material.")),
        ("MRAM", "MRAM", ("몇 번을 다시 써도 오래가는 창고.", "A warehouse that holds up through countless rewrites."), ("자성 방향으로 값을 저장해요.", "Stores values via magnetic orientation.")),
        ("PRAM(PCM)", "PRAM (PCM)", ("속도와 용량의 균형이 좋은 창고.", "A warehouse with a good speed/capacity balance."), ("물질의 결정/비결정 상태 변화를 써요.", "Uses a material's crystalline/amorphous state change.")),
        ("비휘발성", "Non-Volatile", ("전원이 꺼져도 기억이 남는 성질.", "The property of remembering even off power."), ("차세대 메모리들의 공통점이에요.", "Common to all these next-gen memories.")),
        ("쓰기 내구성", "Write Endurance", ("몇 번이나 다시 써도 되는지.", "How many times it can be rewritten."), ("MRAM이 특히 강점이에요.", "MRAM particularly excels here.")),
        ("바이트 단위 덮어쓰기", "Byte-Level Overwrite", ("통째로 안 지우고 한 칸만 바로 바꾸는 것.", "Changing just one slot directly, no full erase."), ("NAND 플래시와 가장 큰 차이예요.", "The biggest difference from NAND flash.")),
        ("저장 밀도", "Storage Density", ("같은 크기에 얼마나 많이 담기는지.", "How much fits in the same physical size."), ("NAND가 여전히 제일 높아요.", "NAND still has the highest density.")),
        ("플래시 메모리(NAND/NOR)", "Flash Memory (NAND/NOR)", ("통째로 지우고 써야 하는 기존 창고.", "The existing warehouse that must be erased whole before writing."), ("대용량·저비용에서는 아직 강점이에요. → <a href=\"flashmem-ko.html\">전원이 꺼져도 기억하는 부품 창고</a>", "Still strong for bulk, low-cost storage. → <a href=\"flashmem-en.html\">the parts warehouse that remembers even off power</a>")),
    ],
}
