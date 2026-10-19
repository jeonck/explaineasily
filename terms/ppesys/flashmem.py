from _draw import *
from _world import *


def shelf_box(x, y, w, h, n, fill="#E9B44C"):
    """큰 상자 여러 개로 채워진 창고 칸(블록 단위 저장)."""
    out = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="#5A3B22"/>'
    bw = (w - 8) / n
    for i in range(n):
        out += f'<rect x="{4 + i * bw}" y="4" width="{bw - 4}" height="{h - 8}" rx="2" fill="{fill}"/>'
    return out + '</g>'


def drawer_cab(x, y, rows, cols, fill="#5B8DEF"):
    """작은 서랍이 칸칸이 있는 서랍장(바이트 단위 접근)."""
    out = f'<g transform="translate({x},{y})">'
    cw, ch = 22, 18
    for r in range(rows):
        for c in range(cols):
            out += f'<rect x="{c * (cw + 3)}" y="{r * (ch + 3)}" width="{cw}" height="{ch}" rx="2" fill="{fill}" stroke="#2E3D57" stroke-width="1.5"/><circle cx="{c * (cw + 3) + cw / 2}" cy="{r * (ch + 3) + ch / 2}" r="2" fill="#2E3D57"/>'
    return out + '</g>'


# 1. 공장 문을 닫아도 부품은 그대로 있어야 해요
P1 = svg(300, night(300)
         + person(140, 150, s=0.8, face=EYES, **CHIEF)
         + shelf_box(260, 150, 220, 70, 5)
         + label(370, 250, "⟦문 닫은 창고 — 부품이 그대로 있나요?|the shop is closed — are the parts still there?⟧", 12, "var(--ink)")
         + label(380, 40, "⟦전원이 꺼져도 사라지면 안 되는 부품들이 있어요|some parts must not vanish when the power is off⟧", 13, "#C9D5E6"))

# 2. 작업대 위 물건은 문 닫으면 사라져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.8, face=FROWN, **MECH1)
         + '<rect x="300" y="170" width="140" height="10" fill="#8B5E3C"/>'
         + '<rect x="320" y="140" width="20" height="30" fill="#C9822B"/><rect x="360" y="140" width="20" height="30" fill="#C9822B"/>'
         + label(370, 120, "⟦작업대 위 부품(=RAM)|parts on the workbench (=RAM)⟧", 11, "var(--muted)")
         + label(370, 220, "⟦밤에 문 닫으면 다 치워져요|clear it all when the shop closes at night⟧", 12, "var(--bad)", cls="d")
         + label(380, 270, "⟦그래서 따로 '꺼져도 안 사라지는' 창고가 필요해요|so we need a separate warehouse that survives power-off⟧", 13, "var(--ink)"))

# 3. 플래시 메모리 = 전원이 꺼져도 기억하는 부품 창고 (hero)
P3 = svg(340, sky(340)
         + shelf_box(120, 160, 220, 80, 5)
         + label(230, 270, "⟦부품 창고(플래시 메모리)|parts warehouse (flash memory)⟧", 12, "var(--muted)")
         + person(460, 140, s=0.85, face=SMILE, **MECH2)
         + label(380, 30, "⟦플래시 메모리 = 전원이 꺼져도 부품을 기억하는 창고|flash memory = a warehouse that remembers parts even off power⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦상자(블록)째로 넣고 꺼내는 큰 창고, NAND·NOR 두 방식이 있어요|a warehouse that moves boxes in blocks — two styles, NAND and NOR⟧", 12, "var(--muted)"))

BLOCK_I = icon('<rect x="8" y="16" width="20" height="18" rx="2" fill="var(--accent)"/><rect x="34" y="16" width="20" height="18" rx="2" fill="var(--accent)"/><rect x="8" y="38" width="46" height="10" rx="2" fill="#5A3B22"/>')
DRAWER_I = icon('<rect x="10" y="10" width="18" height="14" rx="2" fill="var(--good)"/><rect x="34" y="10" width="18" height="14" rx="2" fill="var(--good)"/><rect x="10" y="30" width="18" height="14" rx="2" fill="var(--good)"/><rect x="34" y="30" width="18" height="14" rx="2" fill="var(--good)"/>')
CHEAP_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v24 M24 26 h16 M24 38 h16" stroke="var(--accent)" stroke-width="3"/>')
BOOT_I = icon('<path d="M20 48 L32 12 L44 48 Z" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="36" r="4" fill="var(--good)"/>')

# 4. NAND 창고 vs NOR 서랍장
P4 = svg(320, sky(320)
         + shelf_box(50, 60, 280, 70, 6)
         + label(190, 150, "⟦NAND — 상자(블록)째로만 꺼내요|NAND — only whole boxes (blocks) come out⟧", 12, "var(--ink)", cls="d")
         + label(190, 172, "⟦싸고 용량이 커서 SSD·USB에 써요|cheap, roomy — used in SSDs and USB drives⟧", 11, "var(--muted)")
         + drawer_cab(470, 60, 3, 5)
         + label(590, 150, "⟦NOR — 칸(바이트)마다 바로 꺼내요|NOR — grab any single drawer instantly⟧", 12, "var(--ink)", cls="d")
         + label(590, 172, "⟦비싸고 작지만 즉시 실행 코드(펌웨어)에 써요|pricier, smaller — used for code run straight from it (firmware)⟧", 11, "var(--muted)")
         + label(380, 220, "⟦둘 다 'FTL(플래시 변환계층)'이 아니라 메모리 칸 자체의 종류예요|both are about the memory cell itself, not the FTL that manages it⟧", 12, "var(--ink)"))

# 5. 어디에 쓰이는지가 달라요 / 한계
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + shelf_box(100, 150, 160, 50, 4)
         + label(190, 240, "⟦대용량 저장 — 읽기는 빠르지만 쓰기 전엔 지워야 해요|bulk storage — fast reads, but must erase before writing⟧", 11, "var(--ink)")
         + drawer_cab(500, 150, 2, 4)
         + label(590, 240, "⟦작은 코드 저장 — 바로 실행 가능하지만 비싸요|small code storage — runs in place, but costly⟧", 11, "var(--ink)")
         + label(380, 282, "⟦SSD 안에서 이 창고를 관리하는 소프트웨어가 따로 있어요(FTL)|software inside an SSD manages this warehouse separately (the FTL)⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "flashmem", "order": 13,
    "title": ("전원이 꺼져도 기억하는 부품 창고", "The Parts Warehouse That Remembers Even Off Power"),
    "h1": ("<em>플래시 메모리</em>가 뭐예요?", "What is <em>Flash Memory</em>?"),
    "sub": ("플래시 메모리(NAND/NOR)를, 정비공장 전원이 꺼져도 부품을 기억하는 창고 이야기로 풀어봤어요.",
            "Flash memory (NAND/NOR), told as a story about a parts warehouse that remembers its contents even when the garage's power goes off."),
    "panels": [
        {"svg": P1, "alt": ("밤에 공장 문을 닫는데 정비반장이 창고 부품이 그대로 있을지 걱정함", "At night as the garage closes, the chief worries whether the warehouse parts will still be there"),
         "caption": ("문을 닫아도 부품은 그대로 있어야 해요.", "Parts must still be there even after closing."),
         "small": ("전원이 꺼져도 사라지면 안 되는 부품들이 있어요.", "Some parts must not vanish when the power is off.")},
        {"svg": P2, "alt": ("작업대 위 부품은 밤이 되면 치워짐을 보여줌", "Parts on the workbench get cleared away at night"),
         "caption": ("작업대 위 부품은 문 닫으면 사라져요.", "Parts on the workbench vanish once the shop closes."),
         "small": ("그래서 따로 '꺼져도 안 사라지는' 창고가 필요해요.", "So a separate warehouse that survives power-off is needed.")},
        {"svg": P3, "hero": True, "alt": ("부품 창고가 환한 낮에도 서 있고 정비사가 만족스러워함", "The parts warehouse stands in daylight, the mechanic satisfied"),
         "caption": ("플래시 메모리는 전원이 꺼져도 부품을 기억하는 창고예요.", "Flash memory is a warehouse that remembers parts even off power."),
         "small": ("상자(블록)째로 넣고 꺼내는 큰 창고, NAND·NOR 두 방식이 있어요.", "A warehouse that moves boxes in blocks — in two styles, NAND and NOR."),
         "tricks": (4, [
             (BLOCK_I, ("NAND — 블록 단위", "NAND — block access"), ("상자째로 넣고 꺼내요", "move whole boxes at a time"), "calm"),
             (DRAWER_I, ("NOR — 바이트 단위", "NOR — byte access"), ("한 칸씩 바로 꺼내요", "grab a single drawer directly")),
             (CHEAP_I, ("NAND — 싸고 큼", "NAND — cheap, roomy"), ("SSD·USB에 쓰여요", "used in SSDs and USB drives")),
             (BOOT_I, ("NOR — 즉시 실행", "NOR — execute in place"), ("펌웨어 코드에 쓰여요", "used for firmware code"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: NAND 창고는 상자째로만 꺼냄. 오른쪽: NOR 서랍장은 칸마다 바로 꺼냄", "Left: NAND warehouse only yields whole boxes. Right: NOR drawers come out one at a time"),
         "caption": ("NAND는 상자(블록)째로, NOR는 칸(바이트)마다 꺼내요.", "NAND yields whole boxes (blocks); NOR yields single drawers (bytes)."),
         "small": ("둘 다 FTL이 아니라 메모리 칸 자체의 종류예요.", "Both describe the memory cell itself, not the FTL that manages it.")},
        {"svg": P5, "alt": ("왼쪽: NAND는 대용량 저장에 적합. 오른쪽: NOR는 소용량 즉시실행 코드에 적합", "Left: NAND suits bulk storage. Right: NOR suits small, run-in-place code"),
         "caption": ("용도가 서로 달라요.", "They serve different uses."),
         "small": ("SSD 안에서 이 창고를 관리하는 소프트웨어가 따로 있어요(FTL).", "Software inside an SSD separately manages this warehouse — the FTL.")},
    ],
    "summary": (("<b>플래시 메모리</b>는 <b>전원이 꺼져도 부품을 기억하는 창고</b>로, 블록째 꺼내는 <b>NAND</b>와 칸마다 바로 꺼내는 <b>NOR</b> 두 방식이 있어요.",
                 "<b>Flash memory</b> is a warehouse that <b>remembers its contents even off power</b> — in two styles: <b>NAND</b>, which yields whole blocks, and <b>NOR</b>, which yields single bytes directly."),
                ("플래시 메모리는 전기 없이도 데이터를 유지하는 비휘발성 반도체 저장장치예요. NAND는 블록 단위 읽기·쓰기만 가능해 저렴하고 대용량이라 SSD·USB·메모리카드에 쓰이고, NOR는 바이트 단위 임의 접근과 실행 중 코드 실행(XIP)이 가능해 작은 용량의 펌웨어 저장에 주로 쓰여요. SSD에서 이 NAND 칩을 효율적으로 쓰도록 주소를 매핑·마모 관리하는 소프트웨어 계층이 FTL이에요.",
                 "Flash memory is non-volatile semiconductor storage that keeps data without power. NAND allows only block-level read/write, making it cheap and high-capacity — used in SSDs, USB drives, and memory cards. NOR allows byte-level random access and execute-in-place (XIP), making it common for small firmware storage. The software layer that maps addresses and manages wear on NAND chips inside an SSD is the FTL.")),
    "glossary": [
        ("NAND 플래시", "NAND Flash", ("상자(블록)째로만 꺼내는 큰 창고.", "A big warehouse that only yields whole boxes (blocks)."), ("싸고 용량이 커서 SSD에 쓰여요.", "Cheap and roomy — used in SSDs.")),
        ("NOR 플래시", "NOR Flash", ("칸(바이트)마다 바로 꺼내는 서랍장.", "A drawer cabinet that yields a single byte at a time."), ("비싸지만 즉시 실행이 가능해요.", "Costlier, but allows execute-in-place.")),
        ("비휘발성 메모리", "Non-Volatile Memory", ("전원이 꺼져도 내용이 남는 저장장치.", "Storage that keeps its contents when power is off."), ("플래시가 대표적인 예예요.", "Flash is a prime example.")),
        ("블록/페이지", "Block/Page", ("창고의 상자와 상자 속 칸.", "The warehouse's boxes and the slots inside them."), ("NAND는 블록 단위로 지우고 써요.", "NAND erases and writes in block-sized units.")),
        ("쓰기 전 지우기", "Erase-before-Write", ("새 부품을 넣기 전에 상자를 비워야 함.", "The box must be emptied before new parts go in."), ("NAND의 대표적인 제약이에요.", "A well-known NAND constraint.")),
        ("XIP(실행 중 코드 실행)", "Execute-in-Place", ("서랍에서 바로 꺼내 쓰는 것.", "Using a part straight out of the drawer."), ("NOR의 장점이에요, NAND는 못 해요.", "A NOR advantage — NAND can't do this.")),
        ("SSD", "SSD", ("NAND 창고로 만든 저장장치.", "A storage drive built from NAND warehouses."), ("안에서 FTL이 블록을 관리해요.", "Inside, the FTL manages its blocks.")),
        ("FTL(플래시 변환계층)", "FTL (Flash Translation Layer)", ("창고 안 상자 번호를 바꿔 쓰는 관리 소프트웨어.", "The software that remaps which boxes are used inside the warehouse."), ('메모리 칸의 종류가 아니라 이걸 관리하는 소프트웨어예요. → <a href="ftl-ko.html">덮어쓰지 않는 서가 관리인</a>', 'Not the cell type itself, but the software managing it. → <a href="ftl-en.html">the shelf manager who never overwrites</a>')),
    ],
}
