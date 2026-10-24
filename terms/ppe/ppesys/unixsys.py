from _draw import *
from _world import *


def bay(x, y, s=1.0, label_text=None):
    """정비 베이(작업대) 한 자리."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-34" width="52" height="60" rx="4" fill="#4A5A72"/>'
           f'<rect x="-18" y="-24" width="36" height="20" rx="2" fill="#D8D2C2"/><rect x="-30" y="26" width="60" height="10" rx="2" fill="#3A4558"/></g>')
    if label_text:
        out += label(0, 54, label_text, 11, "var(--muted)")
    return out


def bin_tree(x, y, s=1.0):
    """나뭇가지처럼 뻗은 부품함 트리(파일시스템)."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    out += '<rect x="-14" y="-10" width="28" height="20" rx="2" fill="#5A3B22"/>' + label(0, -16, "/", 13, "#142033", cls="d")
    for i, dx in enumerate((-110, -36, 36, 110)):
        out += f'<path d="M0 0 L{dx} 46" stroke="#C9A86A" stroke-width="3"/>'
        out += f'<rect x="{dx - 24}" y="46" width="48" height="30" rx="3" fill="#8B5E3C"/>'
    return out + '</g>'


def keyring3(x, y, s=1.0):
    """열쇠 세 벌(소유자/그룹/그 외)."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i, c in enumerate(("var(--good)", "var(--accent)", "var(--muted)")):
        kx = i * 34
        out += f'<circle cx="{kx}" cy="0" r="9" fill="none" stroke="{c}" stroke-width="4"/><rect x="{kx - 2}" y="8" width="4" height="16" fill="{c}"/>'
    return out + '</g>'


# 1. 정비사 둘이 베이 하나를 동시에 쓰려다 부딪혀요
P1 = svg(300, sky(300)
         + bay(380, 150, 1.1)
         + person(220, 190, s=0.8, face=SWEAT + EYES, **MECH1)
         + person(540, 190, s=0.8, face=SWEAT + EYES, **MECH2)
         + label(380, 30, "⟦작업 둘이 베이 하나로 동시에 몰려요|two jobs rush the same bay at once⟧", 13, "var(--ink)")
         + label(380, 280, "⟦누가 먼저 쓸지 아무도 안 정해줘요|nobody decides who goes first⟧", 12, "var(--bad)"))

# 2. 부품함도 정리가 안 되면 부품이 섞여요
P2 = svg(315, '<rect width="760" height="315" fill="var(--bad-soft)"/>'
         + bin_tree(300, 60, 0.8)
         + person(620, 230, s=0.7, face=FROWN, **CHIEF)
         + label(380, 250, "⟦아무나 칸을 열고 아무 부품이나 끼워 넣어요|anyone opens any bin and shoves parts in anywhere⟧", 12, "var(--ink)")
         + label(380, 280, "⟦나중엔 뭐가 어디 있는지 아무도 몰라요|soon nobody knows what's where⟧", 12, "var(--muted)"))

# 3. UNIX = 정비소의 보이지 않는 운영자 (hero)
P3 = svg(340, sky(340)
         + bay(230, 170, 0.8) + bay(380, 170, 0.8) + bay(530, 170, 0.8)
         + person(380, 70, s=0.8, face=EYES, **CHIEF)
         + label(380, 25, "⟦UNIX = 베이와 작업을 질서 있게 나눠주는, 정비소의 보이지 않는 운영자|UNIX = the garage's invisible operator, handing out bays and jobs in order⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦정비사는 직접 베이를 배정하지 않고, 정해진 창구로만 말해요|mechanics never claim a bay directly — they speak through one fixed window⟧", 11, "var(--muted)"))

SCHED_I = icon('<rect x="8" y="26" width="18" height="18" rx="2" fill="var(--accent)"/><rect x="32" y="20" width="18" height="18" rx="2" fill="var(--accent-soft)"/><rect x="8" y="20" width="18" height="18" rx="2" fill="var(--accent-soft)" opacity="0"/><path d="M14 10 a22 22 0 1 1 -8 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
TREE_I = icon('<circle cx="32" cy="14" r="6" fill="var(--accent)"/><path d="M32 20 v8 M32 28 l-14 16 M32 28 l14 16" stroke="var(--muted)" stroke-width="3"/><circle cx="18" cy="48" r="6" fill="var(--good)"/><circle cx="46" cy="48" r="6" fill="var(--good)"/>')
KEY_I = icon('<circle cx="18" cy="26" r="8" fill="none" stroke="var(--good)" stroke-width="4"/><rect x="16" y="34" width="4" height="14" fill="var(--good)"/><circle cx="36" cy="26" r="8" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="34" y="34" width="4" height="14" fill="var(--accent)"/>')
SHELL_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#111C30"/><path d="M16 26 l10 8 l-10 8 M30 42 h18" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. 부품함 권한표
P4 = svg(320, sky(320)
         + queueboard(60, 40, 320, 200, "⟦부품함 권한표|PERMISSION TABLE⟧",
                      ("⟦주인 — 읽기·쓰기·실행|owner — read, write, run⟧",
                       "⟦같은 팀 — 읽기·쓰기만|group — read, write only⟧",
                       "⟦그 외 사람 — 읽기만|others — read only⟧"), 1.0)
         + keyring3(480, 90, 1.1)
         + bin_tree(590, 200, 0.7)
         + label(380, 300, "⟦부품함마다 열쇠 세 벌이 각자 달라요|every bin carries its own set of three keys⟧", 12, "var(--ink)"))

# 5. UNIX가 정비를 대신해주진 않아요
P5 = svg(330, '<rect width="380" height="330" fill="var(--accent-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + bay(190, 130, 0.7) + label(190, 260, "⟦질서만 잡아줄 뿐, 정비는 안 해줘요|only keeps order — doesn't do the repair for you⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=SMILE, **MECH1) + label(570, 260, "⟦무슨 정비를 할지는 정비사 몫이에요|what repair gets done is still up to the mechanic⟧", 11, "var(--ink)")
         + label(380, 305, "⟦정비소 규칙은 다 똑같진 않아요 — 정비소마다 조금씩 다른 버전을 써요|the rules aren't identical everywhere — each garage runs its own variant⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "unixsys", "order": 25,
    "title": ("정비소의 보이지 않는 운영자", "The Garage's Invisible Operator"),
    "h1": ("<em>UNIX 시스템</em>이 뭐예요?", "What is a <em>UNIX System</em>?"),
    "sub": ("UNIX 시스템을, 정비공장에서 베이와 작업을 질서 있게 나눠주는 보이지 않는 운영자 이야기로 풀어봤어요.",
            "A UNIX system, told as a story about an invisible operator in the garage, handing out repair bays and jobs in order."),
    "panels": [
        {"svg": P1, "alt": ("정비사 둘이 베이 하나를 동시에 쓰려다 부딪힘", "Two mechanics rush the same repair bay at the same time"),
         "caption": ("작업 둘이 베이 하나로 동시에 몰려요.", "Two jobs rush the same bay at once."),
         "small": ("누가 먼저 쓸지 아무도 안 정해줘요.", "Nobody decides who goes first.")},
        {"svg": P2, "alt": ("부품함 트리가 뒤죽박죽이고 정비반장이 당황함", "A tree of parts bins in disarray, and the chief looks troubled"),
         "caption": ("부품함도 정리가 안 되면 부품이 섞여요.", "Without organization, the parts bins turn to chaos."),
         "small": ("나중엔 뭐가 어디 있는지 아무도 몰라요.", "Soon nobody knows what's where.")},
        {"svg": P3, "hero": True, "alt": ("정비반장이 베이 세 자리를 질서 있게 지켜봄", "The chief watches over three bays, keeping order"),
         "caption": ("UNIX는 베이와 작업을 질서 있게 나눠주는, 정비소의 보이지 않는 운영자예요.", "UNIX is the garage's invisible operator, handing out bays and jobs in order."),
         "small": ("정비사는 직접 베이를 배정하지 않고, 정해진 창구로만 말해요.", "Mechanics never claim a bay directly — they speak through one fixed window."),
         "tricks": (4, [
             (SCHED_I, ("여러 작업을 나눠 돌려요", "Splits many jobs between bays"), ("한 베이를 혼자 독차지 못 해요", "no one hogs a bay alone"), "calm"),
             (TREE_I, ("나뭇가지 모양 부품함", "A tree-shaped parts bin"), ("뿌리 하나에서 가지가 뻗어요", "branches spreading from one root")),
             (KEY_I, ("부품함마다 열쇠 세 벌", "Three keys per bin"), ("주인/같은 팀/그 외가 달라요", "owner, group, and others each differ"), "warm"),
             (SHELL_I, ("어디서나 통하는 명령창", "A command window that works anywhere"), ("다른 정비소에서도 같은 말이 통해요", "the same commands work in other garages too")),
         ])},
        {"svg": P4, "alt": ("부품함 권한표: 주인·같은 팀·그 외 사람이 각기 다른 권한을 가짐. 열쇠 세 벌과 나뭇가지 부품함이 함께 보임", "A permission table: owner, group, and others each get different access, shown with three keys and a tree-shaped bin"),
         "caption": ("부품함마다 열쇠 세 벌이 각자 달라요.", "Every bin carries its own set of three keys."),
         "small": ("주인, 같은 팀, 그 외 사람 — 권한이 모두 달라요.", "Owner, group, and others — the access level differs for each.")},
        {"svg": P5, "alt": ("왼쪽: 베이가 질서만 잡아줌. 오른쪽: 정비는 결국 정비사가 함", "Left: the bay only keeps order. Right: the mechanic still does the actual repair"),
         "caption": ("UNIX가 정비를 대신해주진 않아요.", "UNIX doesn't do the repair for you."),
         "small": ("정비소 규칙도 정비소마다 조금씩 달라요.", "And the garage's rules aren't identical everywhere, either.")},
    ],
    "summary": (("<b>UNIX 시스템</b> = 베이(자원)와 작업(프로세스)을 <b>질서 있게 나눠주고</b>, 부품함(파일)은 <b>나뭇가지 모양</b>으로, 칸마다 <b>열쇠 세 벌</b>로 지키는 정비소의 운영자.",
                 "A <b>UNIX system</b> is the garage's operator — it <b>hands out bays and jobs in order</b>, keeps files in a <b>tree-shaped</b> store, and locks every bin with <b>three keys</b>."),
                ("UNIX는 다중 사용자·다중 작업을 지원하는 운영체제로, 커널이 자원(CPU·메모리·파일)을 중재하고 쉘을 통해 명령을 받아요. 파일시스템은 루트(/)에서 가지를 뻗는 트리 구조이고, 모든 파일은 소유자·그룹·그 외 사용자에 대해 각각 읽기(r)·쓰기(w)·실행(x) 권한을 갖습니다. 표준화된 명령어 덕분에 다른 기종으로도 이식성이 높아요.",
                 "UNIX is an operating system supporting multiple users and multitasking: the kernel arbitrates resources (CPU, memory, files) and takes commands through a shell. Its file system is a tree rooted at /, and every file carries separate read (r), write (w), and execute (x) permissions for its owner, group, and others. Standardized commands give it strong portability across different machines.")),
    "glossary": [
        ("UNIX", "UNIX", ("베이와 작업을 질서 있게 나누는 운영체제.", "An operating system that hands out bays and jobs in order."), ("1970년대부터 지금까지 쓰여요.", "In use continuously since the 1970s.")),
        ("커널(Kernel)", "Kernel", ("정비소의 보이지 않는 진짜 관리자.", "The garage's real, invisible manager."), ("자원을 나눠주고 작업 사이를 중재해요.", "It allocates resources and arbitrates between jobs.")),
        ("쉘(Shell)", "Shell", ("정비사가 지시를 내리는 명령창.", "The command window where a mechanic gives instructions."), ("커널에 직접 손대지 않고 이 창을 거쳐요.", "Workers go through this window instead of touching the kernel directly.")),
        ("파일시스템(트리 구조)", "File System (Tree Structure)", ("나뭇가지처럼 뻗은 부품함 정리법.", "A storage layout that branches like a tree."), ("맨 위 뿌리(root, /)에서 가지가 갈라져요.", "Branches split off from a single root (/) at the top.")),
        ("권한(rwx)", "Permissions (rwx)", ("부품함마다 다른 열쇠 세 벌.", "Three different keys for every bin."), ("주인·같은 팀·그 외 사람이 각각 달라요.", "Owner, group, and others each get their own level.")),
        ("프로세스", "Process", ("지금 돌아가고 있는 작업 하나하나.", "Each job that's currently running."), ('어떤 작업을 먼저 돌릴지는 이 세계의 다른 이야기예요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'Deciding which job runs first is another story in this world. → <a href="cpusched-en.html">who gets the lift first</a>')),
        ("다중 사용자/다중 작업", "Multiuser / Multitasking", ("여러 사람·여러 작업을 동시에 받아줘요.", "It takes on many people and many jobs at once."), ("한 베이를 혼자 독차지하지 않아요.", "No single job monopolizes a bay.")),
        ("이식성(Portability)", "Portability", ("다른 정비소 장비로 옮겨도 같은 명령이 통해요.", "The same commands still work after moving to a different garage's equipment."), ("표준화된 명령어 덕분이에요.", "Thanks to a standardized set of commands.")),
    ],
}
