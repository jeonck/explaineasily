from _draw import *
from _world import *

# 1. 선반 하나로는 느리고, 망가지면 다 잃어요
P1 = svg(300, sky(300)
         + shelfzone(280, 140, 200, 90, 1.2, n=1)
         + person(160, 160, s=0.75, face=SWEAT + EYES, **PACKER)
         + label(380, 268, "⟦상자를 선반 하나에 전부 쌓아두면, 꺼내는 일이 느려요|with every box on one shelf, pulling boxes out is slow⟧", 12, "var(--ink)")
         + label(380, 40, "⟦그 선반이 망가지면 상자가 전부 사라져요|and if that shelf breaks, every box is gone⟧", 13, "var(--bad)"))

# 2. 빠르게 하려고 쪼개면, 하나만 망가져도 전체가 깨져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shelfzone(230, 140, 300, 90, 1.1, n=4, bad=2)
         + person(650, 195, s=0.75, face=FROWN, **PACKER)
         + label(380, 40, "⟦상자를 여러 칸에 나눠 쌓으면 꺼내기는 빠른데, 한 칸만 고장나도 전체 데이터가 깨져요|splitting boxes across slots speeds up pulling them, but one broken slot ruins all the data⟧", 12.5, "var(--ink)"))

# 3. RAID = 나눠 쌓기 + 겹쳐 쌓기로 속도와 안전을 같이 (hero)
P3 = svg(340, sky(340, ground=False)
         + shelfzone(130, 140, 220, 80, 1.0, n=3, label_text="⟦나눠 쌓기(스트라이핑)|split (striping)⟧")
         + box(470, 150, 1.0, twin=True)
         + label(470, 215, "⟦겹쳐 쌓기(미러링)|double up (mirroring)⟧", 11, "var(--muted)")
         + label(380, 30, "⟦RAID = 여러 선반(디스크)을 묶어, 나눠 쌓아 빠르게, 겹쳐 쌓아 안전하게|RAID = combining several shelves (disks): split for speed, doubled for safety⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦선반 여러 개를 하나처럼 묶어서 써요|several shelves work together as if they were one⟧", 12, "var(--muted)"))

# 4. RAID 0/1/5/10 비교
P4 = svg(320, sky(320, ground=False)
         + shelfzone(40, 60, 150, 60, 0.85, n=3, label_text="⟦RAID 0|RAID 0⟧")
         + label(115, 145, "⟦빠름, 복구 불가|fast, no recovery⟧", 10, "var(--bad)")
         + box(290, 95, 0.75, twin=True) + label(290, 145, "⟦RAID 1|RAID 1⟧", 11, "var(--ink)", weight=700)
         + label(290, 160, "⟦안전, 절반만 사용|safe, half capacity⟧", 10, "var(--muted)")
         + shelfzone(400, 60, 150, 60, 0.85, n=3, label_text="⟦RAID 5|RAID 5⟧")
         + label(475, 145, "⟦나눠 쌓기 + 점검표 1장|split + one checksum slot⟧", 10, "var(--good)")
         + shelfzone(580, 60, 70, 60, 0.6, n=2) + box(660, 80, 0.6, twin=True)
         + label(620, 145, "⟦RAID 10|RAID 10⟧", 11, "var(--ink)", weight=700)
         + label(620, 160, "⟦나누고 겹치고 둘다|both split and doubled⟧", 10, "var(--muted)")
         + label(380, 220, "⟦레벨마다 속도·안전·용량을 어떻게 맞바꾸는지가 시험 포인트예요|the exam point is how each level trades speed, safety, and capacity⟧", 12, "var(--ink)")
         + label(380, 250, "⟦RAID 1·5·10은 한 칸이 고장나도 남은 선반과 여분 선반(핫스페어)으로 복구해요|on RAID 1, 5, and 10, surviving shelves and a spare (hot spare) rebuild a failed slot⟧", 11, "var(--muted)"))

# 5. RAID는 백업이 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + box(190, 150, 0.9, twin=True) + label(190, 230, "⟦RAID 복사본은 같은 창고 안에 있어요|RAID's copy sits inside the same warehouse⟧", 11, "var(--ink)")
         + person(570, 140, s=0.8, face=EYES, **AUDITOR) + box(570, 220, 0.7)
         + label(570, 260, "⟦다른 곳에 따로 보관해야 진짜 백업이에요|a copy kept somewhere else is the real backup⟧", 11, "var(--ink)")
         + label(380, 282, "⟦창고 전체가 불타면 겹쳐 쌓은 선반도 같이 타요|if the whole warehouse burns, the doubled shelf burns too⟧", 11.5, "var(--ink)", cls="d"))

STRIPE_I = icon('<rect x="8" y="22" width="12" height="20" fill="var(--accent)"/><rect x="24" y="22" width="12" height="20" fill="var(--accent)"/><rect x="40" y="22" width="12" height="20" fill="var(--accent)"/>')
MIRROR_I = icon('<rect x="10" y="18" width="20" height="28" rx="3" fill="var(--good)"/><rect x="34" y="18" width="20" height="28" rx="3" fill="var(--good)" opacity="0.6"/>')
PARITY_I = icon('<rect x="8" y="22" width="14" height="20" fill="var(--accent)"/><rect x="26" y="22" width="14" height="20" fill="var(--accent)"/><rect x="44" y="22" width="12" height="20" rx="2" fill="var(--good)" stroke="var(--line)" stroke-width="2"/>')
MIX_I = icon('<rect x="6" y="22" width="12" height="20" fill="var(--accent)"/><rect x="20" y="22" width="12" height="20" fill="var(--accent)" opacity="0.6"/><rect x="38" y="22" width="12" height="20" fill="var(--good)"/><rect x="52" y="22" width="6" height="20" fill="var(--good)" opacity="0.6"/>')

PAGE = {
    "slug": "raid", "order": 13,
    "title": ("선반을 쪼개고 겹쳐서 쌓기", "Splitting and Doubling Up the Shelves"),
    "h1": ("<em>RAID</em>가 뭐예요?", "What is <em>RAID</em>?"),
    "sub": ("RAID를, 여러 선반에 물건을 나눠 쌓거나 똑같이 겹쳐 쌓아 선반 하나일 때보다 빠르고 안전하게 만드는 이야기로 풀어봤어요.",
            "RAID, told as a story about splitting goods across several shelves — or doubling them up — to be faster and safer than a single shelf."),
    "panels": [
        {"svg": P1, "alt": ("포장 담당이 선반 하나에 전부 쌓인 상자를 꺼내느라 땀을 흘림", "A worker sweats, pulling boxes from a single shelf holding everything"),
         "caption": ("상자를 선반 하나에 전부 쌓아두면, 꺼내는 일이 느려요.", "With every box on one shelf, pulling boxes out is slow."),
         "small": ("그 선반이 망가지면 상자가 전부 사라져요.", "And if that shelf breaks, every box is gone.")},
        {"svg": P2, "alt": ("선반이 네 칸으로 나뉘었지만 그중 한 칸이 빨갛게 고장 표시됨", "The shelf is split into four slots, but one is marked red as broken"),
         "caption": ("꺼내기를 빠르게 하려고 상자를 여러 칸에 쪼개 쌓으면, 한 칸만 망가져도 전체 데이터가 깨져요.", "Splitting boxes across slots speeds up pulling them, but one broken slot ruins all the data."),
         "small": ("꺼내는 속도를 얻은 대신 데이터 안전을 잃었어요.", "Pulling boxes got faster, but the data got less safe.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽엔 세 칸으로 나뉜 선반, 오른쪽엔 똑같은 상자 두 개가 나란히 놓임", "On the left, a shelf split into three slots; on the right, two identical boxes side by side"),
         "caption": ("RAID는 상자를 여러 선반(디스크)에 나누고 겹쳐 쌓아, 선반 하나일 때보다 빠르고 안전하게 보관해요.", "RAID splits and doubles boxes across several shelves (disks), making storage faster and safer than one shelf."),
         "small": ("선반 여러 개를 하나처럼 묶어서 써요.", "Several shelves work together as if they were one."),
         "tricks": (4, [
             (STRIPE_I, ("나눠 쌓기", "Split it up"), ("빠르지만 한 칸만 고장나도 다 잃어요(RAID0)", "fast, but one failure loses it all (RAID 0)")),
             (MIRROR_I, ("겹쳐 쌓기", "Double it up"), ("안전하지만 용량은 절반(RAID1)", "safe, but half the capacity (RAID 1)"), "calm"),
             (PARITY_I, ("점검표 한 장 추가", "Add one checksum slot"), ("나누고 점검표로 복구(RAID5)", "split plus a checksum to rebuild (RAID 5)")),
             (MIX_I, ("나누고 겹치고 둘 다", "Both split and doubled"), ("빠르고 안전함(RAID10)", "fast and safe together (RAID 10)"), "warm"),
         ])},
        {"svg": P4, "alt": ("RAID 0, 1, 5, 10 네 가지 방식을 선반 그림으로 나란히 비교함", "RAID 0, 1, 5, and 10 compared side by side as shelf diagrams"),
         "caption": ("각 레벨마다 속도·안전·용량을 다르게 맞바꿔요.", "Each level trades off speed, safety, and capacity differently."),
         "small": ("RAID 1·5·10은 한 칸이 고장나도 남은 선반의 데이터로 복구할 수 있어요.", "On RAID 1, 5, and 10, data on the surviving shelves can rebuild a failed slot.")},
        {"svg": P5, "alt": ("왼쪽: 같은 창고 안의 복제 상자 두 개. 오른쪽: 감사원이 다른 곳에 보관한 진짜 백업 상자", "Left: two duplicate boxes in the same warehouse. Right: the auditor keeps a real backup box elsewhere"),
         "caption": ("RAID는 백업이 아니에요.", "RAID is not a backup."),
         "small": ("창고 전체가 불타면 겹쳐 쌓은 선반도 같이 타요.", "If the whole warehouse burns, the doubled shelf burns too.")},
    ],
    "summary": (("<b>RAID</b>는 여러 디스크를 묶어 <b>나눠 쓰거나(스트라이핑) 겹쳐 써서(미러링)</b> 구성에 따라 디스크 한 개일 때보다 속도나 안전성을 높이는 저장 방식이에요.",
                 "<b>RAID</b> combines several disks, <b>splitting data across them (striping) or duplicating it (mirroring)</b>, to beat a single disk on speed, safety, or both."),
                ("RAID 0은 속도만, RAID 1은 안전만, RAID 5는 분산 패리티로 둘을 절충, RAID 10은 스트라이핑과 미러링을 함께 써서 속도와 안전을 둘 다 챙겨요. 단, RAID는 '같은 장소에 있는 디스크들의 중복'일 뿐이라서 화재·도난·실수 삭제 같은 재해에는 대비가 안 돼요 — 원격지 백업은 반드시 별도로 필요해요.",
                 "RAID 0 trades purely for speed, RAID 1 purely for safety, RAID 5 splits data with distributed parity for a middle ground, and RAID 10 combines striping and mirroring for both. But RAID is only redundancy among disks in the same location — it doesn't protect against fire, theft, or accidental deletion. A separate, off-site backup is still required.")),
    "glossary": [
        ("스트라이핑", "Striping", ("여러 선반에 나눠 쌓기.", "Splitting goods across several shelves."), ("빠르지만 디스크 하나만 고장나도 데이터를 다 잃어요.", "Fast, but one failed disk loses all the data.")),
        ("미러링", "Mirroring", ("똑같이 겹쳐 쌓기.", "Stacking an identical copy alongside."), ("용량은 절반이지만 안전해요.", "Half the usable capacity, but safe.")),
        ("패리티", "Parity", ("남은 칸과 합쳐 고장난 칸을 복구하는 점검표.", "A checksum slot that, with the surviving slots, rebuilds a failed one."), ("한 칸이 망가져도 되살릴 수 있어요.", "Lets you recover even if one slot fails.")),
        ("RAID 5", "RAID 5", ("나눠 쌓기 + 패리티 한 칸.", "Striping plus one parity slot."), ("속도와 용량 효율의 절충이에요.", "A middle ground on speed and capacity.")),
        ("RAID 10", "RAID 10", ("나누고 겹치고 둘 다.", "Both striped and mirrored."), ("속도와 안전을 함께 챙겨요.", "Keeps both speed and safety.")),
        ("핫스페어", "Hot Spare", ("미리 대기 중인 여분 선반.", "A spare shelf waiting on standby."), ("선반 하나가 고장나면 바로 자리를 대신해요.", "Steps in immediately when a shelf fails.")),
        ("백업과의 차이", "Difference from Backup", ("RAID는 같은 창고 안의 복사본일 뿐이에요.", "RAID is only a copy inside the same warehouse."), ('진짜 재해 대비는 원격지 백업이에요. → <a href="backup-ko.html">다른 곳에 보관하는 상자</a>', 'Real disaster protection needs an off-site backup. → <a href="backup-en.html">the box kept somewhere else</a>')),
        ("내결함성", "Fault Tolerance", ("디스크 일부가 고장나도 시스템이 계속 동작.", "The system keeps working even if some disks fail."), ("RAID가 추구하는 목표 중 하나예요.", "One of the goals RAID is built for.")),
    ],
}
