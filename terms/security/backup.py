from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")


def chest(x, y, s=1.0, kind="wood", locked=False, open_lid=False, inner=""):
    body, edge = {"wood": ("#8B5E3C", "#5A3B22"), "iron": ("var(--stone-dark)", "var(--night)"), "grey": ("var(--stone)", "var(--stone-dark)")}[kind]
    lid = (f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}" transform="rotate(-40 -30 -14)"/>' if open_lid
           else f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{edge}"/>')
    lock = ('<rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--bad)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--bad)" stroke-width="4" fill="none"/>' if locked else "")
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{body}"/>{lid}{lock}{inner}</g>'


PHOTO = '<rect x="-14" y="-32" width="28" height="22" rx="2" fill="var(--panel)" stroke="var(--line)" stroke-width="1.5"/><path d="M-10 -14 l7 -8 l5 5 l3 -3 l5 6z" fill="var(--good)"/><circle cx="6" cy="-26" r="3" fill="var(--accent)"/>'
FIRE = '<path d="M0 0 C-14 -18 -12 -34 0 -50 C3 -34 11 -30 13 -40 C22 -24 20 -8 0 0 Z" fill="var(--accent)"/><path d="M0 -4 C-7 -14 -5 -24 0 -32 C3 -24 7 -22 8 -28 C13 -18 11 -10 0 -4 Z" fill="#FFC875"/>'
WAVE = '<path d="M-40 0 q10 -12 20 0 t20 0 t20 0 t20 0" stroke="#5B9BD5" stroke-width="5" fill="none" stroke-linecap="round"/>'
TRASH = '<path d="M-16 -10 h32 l-3 34 h-26z" fill="var(--stone-dark)"/><rect x="-20" y="-16" width="40" height="6" fill="var(--stone-dark)"/>'


def depot(x, y, s=1.0, inner="", name="⟦다른 마을 창고|depot in another town⟧"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="0" width="120" height="80" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/>'
            f'<path d="M-70 0 L0 -36 L70 0 Z" fill="var(--good)"/>{inner}{label(0, 100, name, 11, "var(--muted)")}</g>')


# 1. 소중한 상자는 하나뿐
P1 = svg(280, sky(280) + castle(60, 70, 0.45)
         + chest(380, 170, 1.4, open_lid=True, inner=PHOTO) + label(380, 235, "⟦단 하나|the only one⟧", 14, "var(--ink)", cls="d")
         + person(560, 100, s=0.9, **ME)
         + label(380, 265, "⟦이 상자가 없어지면 성은 처음부터 다시 시작해요|lose this chest and the castle starts from nothing⟧", 13, "var(--muted)"))

# 2. 상자는 여러 가지로 없어진다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + chest(100, 150, 0.9) + f'<g transform="translate(100,140)">{FIRE}</g>' + label(100, 210, "⟦불|fire⟧", 13, "var(--ink)")
         + chest(280, 150, 0.9) + f'<g transform="translate(280,170)">{WAVE}</g>' + label(280, 210, "⟦물|flood⟧", 13, "var(--ink)")
         + chest(460, 150, 0.9, locked=True) + label(460, 210, "⟦도둑의 자물쇠|the thief\'s lock⟧", 13, "var(--ink)")
         + f'<g transform="translate(640,150)">{TRASH}</g>' + chest(640, 140, 0.5) + label(640, 210, "⟦내가 실수로 버림|I threw it out by mistake⟧", 13, "var(--ink)")
         + label(380, 275, "⟦제일 흔한 건 마지막 거예요|the last one is the most common⟧", 13, "var(--bad)"))

# 3. 백업 = 베껴서 다른 곳에 (hero)
P3 = svg(340, sky(340) + castle(20, 90, 0.4)
         + chest(150, 210, 1.0, open_lid=True, inner=PHOTO) + label(150, 260, "⟦원본|the original⟧", 12, "var(--muted)")
         + '<path d="M200 200 L260 200" stroke="var(--good)" stroke-width="3"/><path d="M250 190 L262 200 L250 210" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + chest(310, 210, 1.0, inner=PHOTO) + label(310, 260, "⟦나무 상자|wooden chest⟧", 11, "var(--muted)")
         + chest(400, 210, 1.0, kind="iron", inner=PHOTO) + label(400, 260, "⟦쇠 상자|iron chest⟧", 11, "var(--muted)")
         + '<path d="M450 200 L520 200" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 6"/>'
         + depot(620, 130, 0.9, inner=chest(0, 50, 0.6, inner=PHOTO))
         + label(360, 60, "⟦3 · 2 · 1|3 · 2 · 1⟧", 40, "var(--good)", cls="d")
         + label(360, 92, "⟦사본 셋 · 종류 둘 · 하나는 멀리|three copies · two kinds · one far away⟧", 14, "var(--ink)")
         + label(380, 322, "⟦하나가 타도, 젖어도, 잠겨도 다른 하나가 남아요|burnt, soaked or locked, another one remains⟧", 13, "var(--muted)"))

# 4. 매일 베끼고, 가끔 열어본다
CLOCK = '<g transform="translate(120,90)"><circle r="34" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -22 V0 L14 10" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
P4 = svg(300, '<rect width="380" height="300" fill="var(--sky)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>' + CLOCK
         + label(120, 150, "⟦매일 밤|every night⟧", 14, "var(--ink)", cls="d")
         + chest(240, 130, 0.8, open_lid=True, inner=PHOTO) + '<path d="M180 180 C220 220 260 220 300 180" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="6 6"/><path d="M290 172 L302 180 L292 192" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + chest(320, 210, 0.7, inner=PHOTO) + label(190, 275, "⟦새로 생긴 것만 더 베껴요|copy only what\'s new⟧", 12, "var(--muted)")
         + person(460, 100, s=0.85, face=EYES, **CLERK) + chest(580, 190, 1.0, open_lid=True, inner=PHOTO)
         + '<path d="M565 150 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>'
         + label(570, 60, "⟦한 달에 한 번, 열어봐요|once a month, open it⟧", 14, "var(--ink)", cls="d")
         + label(570, 275, "⟦열리는지 안 보면 없는 거나 같아요|unopened, a copy might as well not exist⟧", 12, "var(--muted)"))

# 5. 베낀 상자엔 그때 있던 것만
BUG = '<g transform="translate(0,-6)"><ellipse rx="9" ry="6" fill="var(--bad)"/><circle cx="-8" cy="-2" r="4" fill="var(--bad)"/><path d="M-4 -6 l-3 -5 M4 -6 l3 -5 M-6 5 l-4 5 M6 5 l4 5" stroke="var(--bad)" stroke-width="2"/></g>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + chest(110, 120, 0.9, open_lid=True, inner=PHOTO) + label(110, 60, "⟦어젯밤 베낀 상자|copied last night⟧", 12, "var(--muted)")
         + '<rect x="200" y="80" width="90" height="60" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 4"/>' + label(245, 106, "⟦오늘 오후|this afternoon⟧", 10, "var(--muted)") + label(245, 124, "?", 20, "var(--accent)", cls="d")
         + label(190, 200, "⟦오늘 오후 그림은 아직 없어요|this afternoon\'s pictures aren\'t in it yet⟧", 12, "var(--ink)")
         + label(190, 300, "⟦마지막으로 베낀 시각까지만|only up to the last copy⟧", 12, "var(--muted)")
         + chest(470, 120, 0.9, open_lid=True, inner=BUG) + '<path d="M520 110 L560 110" stroke="var(--bad)" stroke-width="3"/><path d="M550 100 L562 110 L550 120" stroke="var(--bad)" stroke-width="3" fill="none"/>' + chest(610, 120, 0.9, inner=BUG)
         + label(540, 200, "⟦벌레 든 채로 베끼면 사본에도 벌레|copy it with the bug, and the copy has the bug⟧", 11, "var(--bad)")
         + "".join(chest(470 + i * 60, 250, 0.55, kind="grey" if i < 2 else "wood", inner="" if i < 2 else PHOTO) for i in range(4))
         + "".join(label(470 + i * 60, 285, t, 10, "var(--muted)") for i, t in enumerate(("⟦3일 전|3 days ago⟧", "⟦2일 전|2 days ago⟧", "⟦어제|yesterday⟧", "⟦오늘|today⟧")))
         + label(570, 310, "⟦그래서 며칠치를 따로 둬요|so several days\' copies are kept apart⟧", 11, "var(--muted)"))

THREE_I = icon('<rect x="6" y="24" width="14" height="14" rx="2" fill="#8B5E3C"/><rect x="25" y="24" width="14" height="14" rx="2" fill="#8B5E3C"/><rect x="44" y="24" width="14" height="14" rx="2" fill="#8B5E3C"/>')
TWO_I = icon('<rect x="10" y="24" width="18" height="16" rx="2" fill="#8B5E3C"/><rect x="36" y="24" width="18" height="16" rx="2" fill="var(--stone-dark)"/>')
FAR_I = icon('<rect x="6" y="30" width="14" height="14" rx="2" fill="#8B5E3C"/><path d="M24 37 H40" stroke="var(--good)" stroke-width="3" stroke-dasharray="3 3"/><path d="M40 22 L56 32 L40 42 Z" fill="var(--good)"/>')
APART_I = icon('<rect x="8" y="26" width="16" height="16" rx="2" fill="#8B5E3C"/><rect x="40" y="26" width="16" height="16" rx="2" fill="#8B5E3C"/><path d="M30 18 v28" stroke="var(--bad)" stroke-width="3"/><path d="M26 22 l8 -4 M26 42 l8 4" stroke="var(--bad)" stroke-width="2"/>')

PAGE = {
    "slug": "backup", "order": 43,
    "title": ("멀리 둔 여분 상자", "The Spare Chest Far Away"),
    "h1": ("<em>백업</em>이 뭐예요?", "What is a <em>Backup</em>?"),
    "sub": ("백업(Backup)을 소중한 상자를 베껴서 멀리 두는 이야기로 풀어봤어요.",
            "Backups, told as a story about copying the precious chest and keeping the copy far away."),
    "panels": [
        {"svg": P1, "alt": ("성 옆에 사진이 든 상자 하나뿐, '단 하나'", "Beside the castle, a single chest holding photos — the only one"),
         "caption": ("소중한 상자는 하나뿐이에요.", "The precious chest is the only one."),
         "small": ("그림책, 장부, 사진. 이 상자가 없어지면 성은 처음부터 다시 시작해요.", "Books, ledgers, photos. Lose this chest and the castle starts from nothing.")},
        {"svg": P2, "alt": ("불타는 상자, 물에 잠긴 상자, 도둑 자물쇠가 걸린 상자, 쓰레기통에 버려진 상자", "A chest on fire, one in water, one with the thief's lock, and one thrown in the trash"),
         "caption": ("상자는 여러 가지로 없어져요.", "Chests get lost in many ways."),
         "small": ('불, 물, <a href="ransomware-ko.html">도둑의 자물쇠</a>, 그리고 제일 흔한 건 내가 실수로 버리는 거예요.',
                   'Fire, flood, the <a href="ransomware-en.html">thief\'s lock</a> — and most often of all, me throwing it out by mistake.')},
        {"svg": P3, "hero": True, "alt": ("원본 상자에서 나무 상자와 쇠 상자로 베끼고, 하나는 다른 마을 창고로. 위에 '3·2·1 사본 셋 종류 둘 하나는 멀리'", "The original copied into a wooden and an iron chest, with one sent to a depot in another town; above: 3·2·1 — three copies, two kinds, one far away"),
         "caption": ("백업은 상자를 베껴서 다른 곳에 두는 거예요.", "A backup is a copy of the chest, kept somewhere else."),
         "small": ("셋을 만들어요. 종류는 둘, 하나는 멀리. 3-2-1이에요.", "Make three. Two different kinds, one far away. That's 3-2-1."),
         "tricks": (4, [
             (THREE_I, ("사본 셋", "Three copies"), ("하나는 늘 없어질 수 있어요", "one can always be lost"), "warm"),
             (TWO_I, ("종류 둘", "Two kinds"), ("나무 상자와 쇠 상자", "a wooden chest and an iron one"), "calm"),
             (FAR_I, ("하나는 멀리", "One far away"), ("불이 나도 다른 마을은 멀쩡", "a fire here leaves the next town fine"), "calm"),
             (APART_I, ("떼어 두기", "Kept apart"), ("도둑 손이 안 닿게", "out of the thief\'s reach")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 시계와 '매일 밤', 새로 생긴 것만 베끼는 화살표. 오른쪽: 직원이 여분 상자를 열어 사진이 있는지 확인, 체크 표시", "Left: a clock — every night — and an arrow copying only what's new. Right: a clerk opens the spare chest to check the photo is there, with a check mark"),
         "caption": ("매일 베끼고, 가끔 열어봐요.", "Copy every day, and open it now and then."),
         "small": ("베낀 게 열리는지 안 보면 없는 거나 같아요. 한 달에 한 번 열어서 확인해요.", "A copy you never open might as well not exist. Once a month, open it and check.")},
        {"svg": P5, "alt": ("왼쪽: 어젯밤 베낀 상자 옆 '오늘 오후 ?' 빈칸. 오른쪽: 벌레 든 상자를 베끼니 사본에도 벌레, 아래엔 3일 전·2일 전·어제·오늘 상자 네 개", "Left: last night's copy beside an empty this afternoon ? slot. Right: a chest with a bug copied into a chest with a bug; below, four chests labeled 3 days ago, 2 days ago, yesterday, today"),
         "caption": ("베낀 상자엔 그때 있던 것만 들어 있어요.", "A copy holds only what was there when it was made."),
         "small": ('오늘 오후 그림은 아직 없어요. <a href="malware-ko.html">벌레</a>가 든 채로 베끼면 사본에도 벌레가 있어요 — 그래서 며칠치 사본을 따로 둬요.',
                   'This afternoon\'s pictures aren\'t in it yet. Copy a chest with a <a href="malware-en.html">bug</a> inside and the copy has the bug — so several days\' copies are kept apart.')},
    ],
    "summary": (("<b>백업</b> = 소중한 상자를 베껴 <b>셋</b> 만들고, 종류 <b>둘</b>, 하나는 <b>멀리</b> 두고, 열리는지 가끔 시험하는 것.",
                 "A <b>backup</b> = the precious chest copied <b>three</b> times, in <b>two</b> kinds, one kept <b>far away</b> — and opened now and then to be sure."),
                ("Backup. 3-2-1 규칙이에요. 얼마나 잃어도 되는지(RPO)와 얼마나 빨리 돌아와야 하는지(RTO)를 먼저 정해요. 랜섬웨어의 진짜 해법이기도 해요.",
                 "The 3-2-1 rule. Decide first how much you can afford to lose (RPO) and how fast you must be back (RTO). It\'s also the real answer to ransomware.")),
    "glossary": [
        ("3-2-1", "3-2-1", ("셋 · 둘 · 하나.", "Three · two · one."), ("사본 셋, 매체 둘, 하나는 멀리. 외우기 쉬운 최소 규칙.", "Three copies, two media, one off-site. The easy-to-remember minimum.")),
        ("전체 · 증분 백업", "Full · incremental", ("통째로 · 바뀐 것만.", "Everything · only what changed."), ("가끔은 통째로, 매일은 새로 생긴 것만 더 베껴요.", "A whole copy now and then; every day, just the new bits.")),
        ("스냅샷", "Snapshot", ("그 순간 사진.", "A photo of that moment."), ("빠르지만 같은 방에 있어요. 방이 불타면 같이 타요.", "Fast, but it lives in the same room — and burns with it.")),
        ("오프라인 · 불변 백업", "Air-gapped · immutable", ("떼어 둔 상자.", "The chest kept apart."), ('도둑 손이 안 닿아요. → <a href="ransomware-ko.html">상자마다 채운 도둑의 자물쇠</a>', 'Out of the thief\'s reach. → <a href="ransomware-en.html">the thief\'s lock on every chest</a>')),
        ("RPO", "RPO (recovery point objective)", ("얼마나 잃어도 되나.", "How much may be lost."), ("마지막으로 베낀 시각까지 돌아가요. 한 시간? 하루?", "You go back to the last copy. An hour? A day?")),
        ("RTO", "RTO (recovery time objective)", ("얼마나 빨리 돌아와야 하나.", "How fast you must be back."), ("여분 상자를 꺼내 제자리에 놓는 데 걸리는 시간.", "How long it takes to fetch the spare and put it back.")),
        ("복구 훈련", "Restore test", ("열어보기.", "Opening it."), ("여분이 있는 것과 열리는 것은 달라요.", "Having a spare and being able to open it are different things.")),
        ("보관 기간 · 세대", "Retention · versions", ("며칠치 사본.", "Several days\' copies."), ("벌레가 들기 전 상자로 돌아갈 수 있게.", "So you can go back to a chest from before the bug got in.")),
    ],
}
