from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
COINS = '<circle cx="62" cy="86" r="12" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle cx="70" cy="98" r="10" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>'


def door(x, y, w=50, h=80, lock=False, bricked=False):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{WOOD}"/><circle cx="{x + w - 10}" cy="{y + h / 2}" r="4" fill="#E9B44C"/>'
    if lock:
        out += f'<rect x="{x + w / 2 - 8}" y="{y + h / 2 - 2}" width="16" height="14" rx="2" fill="#E9B44C"/><path d="M{x + w / 2 - 5} {y + h / 2 - 2} v-6 a5 5 0 0 1 10 0 v6" stroke="#E9B44C" stroke-width="3" fill="none"/>'
    if bricked:
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="var(--stone)"/>' + "".join(
            f'<path d="M{x} {y + i * 16} h{w}" stroke="var(--stone-dark)" stroke-width="2"/>' for i in range(1, 5))
    return out


def chest(x, y, s=1.0, color="#8B5E3C", lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{color}"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def crown(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 10 l-4 -30 l14 12 l16 -22 l16 22 l14 -12 l-4 30z" fill="#E9B44C" stroke="#C9822B" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="-28" y="8" width="56" height="10" rx="3" fill="#C9822B"/><circle cx="-16" cy="-4" r="3" fill="var(--bad)"/><circle cy="-10" r="3" fill="#5B8DEF"/><circle cx="16" cy="-4" r="3" fill="var(--bad)"/></g>')


def ledger(x, y, w, h, title, rows, cols=()):
    """rows: (door, likely, loss, color). cols: 헤더 라벨 (x, text) 목록."""
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="30" rx="8" fill="#C9A86A"/>' + label(w / 2, 20, title, 13, "#142033", cls="d"))
    out += "".join(label(cx, 52, t, 11, "#142033", cls="d") for cx, t in cols if t)
    for i, (d, lk, ls, c) in enumerate(rows):
        yy = 82 + i * 32
        out += label(20, yy, d, 12, "#142033", "start") + f'<circle cx="{cols[3][0]}" cy="{yy - 4}" r="9" fill="{c}"/>'
        out += (label(cols[1][0], yy, lk, 12, "#142033") if lk else "") + (label(cols[2][0], yy, ls, 12, "#142033") if ls else "")
    return out + "</g>"


def calendar(x, y, s=1.0, text="", color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="-26" y="-22" width="52" height="12" rx="4" fill="{color}"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/>{label(0, 12, text, 12, "#142033", cls="d")}</g>')


# 1. 문은 100개, 경비는 10명
P1 = svg(320, sky(320) + castle(30, 70, 0.85)
         + "".join(f'<rect x="{x}" y="206" width="14" height="26" rx="2" fill="{WOOD}"/>' for x in (115, 135, 155, 175, 275, 295, 315, 335))
         + label(225, 262, "⟦문이 100개|100 doors⟧", 13, "var(--ink)", cls="d")
         + "".join(person(460 + i * 45, 110, s=0.45, face=EYES, **GUARD) for i in range(5))
         + "".join(person(460 + i * 45, 165, s=0.45, face=EYES, **GUARD) for i in range(5))
         + label(560, 240, "⟦경비는 10명|10 guards⟧", 13, "var(--ink)", cls="d")
         + person(680, 90, s=0.7, face=FROWN + SWEAT, **KING)
         + bubble(470, 30, 250, 34, "⟦어디부터 지키지?|which door first?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦다 지킬 순 없어요 — 그럼 어디부터요?|we can\'t guard them all — so where first?⟧", 12, "var(--muted)"))

# 2. 느낌으로 정하면 / 골고루 나누면
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + door(40, 90) + label(65, 190, "⟦빈 창고|empty storeroom⟧", 10, "var(--muted)")
         + "".join(person(100 + i * 40, 100, s=0.5, face=SMILE, **GUARD) for i in range(4)) + label(180, 190, "⟦경비 넷|four guards⟧", 10, "var(--muted)")
         + chest(310, 150, 1.0, lock=True) + label(310, 195, "⟦금고 — 경비 없음|the vault — no guard⟧", 10, "var(--bad)")
         + person(330, 60, s=0.6, face=MASK, extra=BAG)
         + label(190, 240, "⟦느낌으로 정하면|going by gut feeling⟧", 14, "var(--ink)", cls="d") + label(190, 262, "⟦엉뚱한 문을 지켜요|you guard the wrong door⟧", 11, "var(--bad)")
         + "".join(f'<rect x="{402 + i * 34}" y="70" width="20" height="40" rx="2" fill="{WOOD}"/>' for i in range(10))
         + "".join(person(400 + i * 34, 120, s=0.35, face=EYES, **GUARD) for i in range(10))
         + label(570, 190, "⟦문마다 한 명씩 — 다 얇아요|one per door — all of them thin⟧", 10, "var(--muted)")
         + label(570, 240, "⟦골고루 나누면|spreading evenly⟧", 14, "var(--ink)", cls="d") + label(570, 262, "⟦금고도 빈 창고만큼만 지켜요|the vault gets what the storeroom gets⟧", 11, "var(--accent)")
         + label(380, 292, "⟦느낌도, 골고루도 아니에요 — 재야 해요|not by gut, not evenly — you have to weigh it⟧", 11, "var(--muted)"))

# 3. 저울: 올 가능성 × 잃는 것 → 위험 장부 (hero)
ROWS = (("⟦금고 옆 문|vault door⟧", "⟦높음|high⟧", "⟦큼|big⟧", "var(--bad)"),
        ("⟦손님 방 문|guest room door⟧", "⟦높음|high⟧", "⟦작음|small⟧", "#E9B44C"),
        ("⟦왕의 창문|the king\'s window⟧", "⟦낮음|low⟧", "⟦큼|big⟧", "#E9B44C"),
        ("⟦빈 창고 문|storeroom door⟧", "⟦낮음|low⟧", "⟦없음|none⟧", "var(--good)"))
P3 = svg(360, sky(360)
         + '<rect x="176" y="90" width="8" height="140" fill="var(--stone-dark)"/><rect x="140" y="228" width="80" height="10" rx="3" fill="var(--stone-dark)"/>'
         + '<rect x="80" y="96" width="200" height="6" rx="3" fill="var(--stone-dark)"/><circle cx="180" cy="99" r="8" fill="#E9B44C"/>'
         + '<path d="M84 100 V170 M276 100 V170" stroke="var(--stone-dark)" stroke-width="3"/>'
         + '<ellipse cx="100" cy="175" rx="42" ry="8" fill="var(--stone)"/><ellipse cx="260" cy="175" rx="42" ry="8" fill="var(--stone)"/>'
         + person(75, 112, s=0.5, face=MASK) + crown(260, 152, 0.7)
         + '<circle cx="180" cy="150" r="18" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>' + label(180, 161, "×", 30, "var(--accent)", cls="d")
         + label(100, 205, "⟦올 가능성|how likely⟧", 11, "var(--ink)") + label(260, 205, "⟦털리면 잃는 것|what we\'d lose⟧", 11, "var(--ink)")
         + label(180, 262, "⟦가능성 × 잃는 것 = 위험|likely × loss = risk⟧", 12, "var(--ink)", cls="d")
         + ledger(340, 40, 380, 200, "⟦위험 장부|RISK LEDGER⟧", ROWS, ((60, "⟦문|door⟧"), (220, "⟦가능성|likely⟧"), (290, "⟦잃는 것|loss⟧"), (350, "⟦위험|risk⟧")))
         + person(380, 250, s=0.65, face=EYES, **KING) + person(450, 255, s=0.6, face=SMILE, **GUARD)
         + label(625, 300, "⟦왕과 함께 봐요 — 빨간 문부터|read it with the king — red doors first⟧", 11, "var(--ink)", cls="d")
         + label(380, 340, "⟦다 지킬 순 없으니, 재서 고르는 거예요|we can\'t guard everything, so we weigh and choose⟧", 12, "var(--muted)"))

# 4. 재고 나면 넷 중 하나: 막기 · 받아들이기 · 넘기기 · 없애기
P4 = svg(320, sky(320)
         + label(100, 60, "⟦막기|reduce⟧", 13, "var(--ink)", cls="d") + door(60, 90, lock=True) + person(112, 100, s=0.6, face=SMILE, **GUARD)
         + label(100, 245, "⟦자물쇠와 경비를 붙여요|add a lock and a guard⟧", 10, "var(--muted)")
         + label(290, 60, "⟦받아들이기|accept⟧", 13, "var(--ink)", cls="d") + door(255, 90) + '<circle cx="330" cy="130" r="18" fill="var(--good)"/><path d="M321 130 l6 6 l12 -12" stroke="#FFF" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + label(290, 245, "⟦작으면 그냥 둬요 — 알고서요|small? leave it — knowingly⟧", 10, "var(--muted)")
         + label(480, 60, "⟦넘기기|transfer⟧", 13, "var(--ink)", cls="d") + door(430, 90) + person(490, 100, s=0.6, face=SMILE, extra=COINS, **CLERK)
         + label(480, 245, "⟦보험 — 털리면 물어줘요|insurance pays if it goes⟧", 10, "var(--muted)")
         + label(670, 60, "⟦없애기|avoid⟧", 13, "var(--ink)", cls="d") + door(645, 90, bricked=True)
         + label(670, 245, "⟦문을 아예 막아 버려요|brick the door up for good⟧", 10, "var(--muted)")
         + label(380, 295, "⟦빨간 문은 막고, 초록 문은 받아들여요 — 다 같은 답이 아니에요|red doors get blocked, green doors get accepted — not one answer for all⟧", 11, "var(--ink)", cls="d"))

# 5. 다 막아도 조금은 남아요 — 그래서 매달 다시 재요
ROWS2 = (("⟦금고 옆 문 — 경비 셋|vault door — 3 guards⟧", "", "", "#E9B44C"),
         ("⟦손님 방 문 — 새 자물쇠|guest door — new lock⟧", "", "", "var(--good)"),
         ("⟦빈 창고 문 — 그대로|storeroom — as is⟧", "", "", "var(--good)"))
P5 = svg(300, sky(300)
         + ledger(40, 40, 300, 180, "⟦위험 장부 — 다시 봄|RISK LEDGER — REVIEWED⟧", ROWS2, ((0, ""), (0, ""), (0, ""), (270, "")))
         + calendar(400, 120, 1.0, "⟦매달|monthly⟧")
         + person(480, 100, s=0.75, face=EYES, **KING) + person(560, 110, s=0.7, face=SMILE, **GUARD)
         + bubble(430, 30, 290, 34, "⟦다 막아도 조금은 남아요|even blocked, a little remains⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(560, 220, "⟦남은 위험은 알고 지켜봐요|the leftover risk is known and watched⟧", 11, "var(--muted)")
         + label(380, 270, "⟦저울은 한 번이 아니라 계속이에요|the scale is not a one-time thing⟧", 13, "var(--ink)", cls="d"))

SCALE_I = icon('<rect x="30" y="14" width="4" height="34" fill="var(--stone-dark)"/><rect x="10" y="16" width="44" height="4" rx="2" fill="var(--stone-dark)"/><path d="M12 18 v14 M52 18 v14" stroke="var(--stone-dark)" stroke-width="2"/><ellipse cx="12" cy="34" rx="10" ry="3" fill="var(--stone)"/><ellipse cx="52" cy="34" rx="10" ry="3" fill="var(--stone)"/><rect x="20" y="48" width="24" height="5" rx="2" fill="var(--stone-dark)"/><circle cx="12" cy="27" r="4" fill="var(--bad)"/><circle cx="52" cy="27" r="4" fill="#E9B44C"/>')
LEDGER_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="22" cy="24" r="4" fill="var(--bad)"/><circle cx="22" cy="36" r="4" fill="#E9B44C"/><circle cx="22" cy="48" r="4" fill="var(--good)"/><path d="M30 24 h14 M30 36 h14 M30 48 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
PICK_I = icon(f'<rect x="8" y="20" width="16" height="30" rx="2" fill="{WOOD}"/><rect x="14" y="30" width="6" height="6" fill="#E9B44C"/><circle cx="44" cy="35" r="12" fill="var(--good)"/><path d="M38 35 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')
KING_I = icon('<circle cx="32" cy="26" r="12" fill="#E8C9A8"/><path d="M18 20 l-2 -12 l8 6 l8 -10 l8 10 l8 -6 l-2 12z" fill="#E9B44C"/><rect x="18" y="38" width="28" height="20" rx="6" fill="#7B3FA0"/>')

PAGE = {
    "slug": "risk", "order": 73,
    "title": ("어느 문부터 지킬지 정하는 저울", "The Scale That Picks Which Door First"),
    "h1": ("<em>위험 관리</em>가 뭐예요?", "What is <em>Risk Management</em>?"),
    "sub": ("위험 관리(Risk Management)를 문은 100개인데 경비는 10명뿐인 성에서 어느 문부터 지킬지 저울로 재는 이야기로 풀어봤어요.",
            "Risk management, told as a story about a castle with a hundred doors and ten guards, weighing which door to guard first."),
    "panels": [
        {"svg": P1, "alt": ("성벽에 작은 문이 줄지어 있고 '문이 100개'. 옆에 초록 경비 열 명이 두 줄로 서 있고 '경비는 10명'. 왕이 땀을 흘리며 '어디부터 지키지?'", "A castle wall lined with little doors — 100 doors. Beside it, ten green guards in two rows — 10 guards. The king sweats: which door first?"),
         "caption": ("문은 100개인데 경비는 10명이에요.", "A hundred doors, and only ten guards."),
         "small": ("다 지킬 순 없어요. 그럼 어디부터요? 왕이 물어요.", "We can\'t guard them all. So where first? The king wants to know.")},
        {"svg": P2, "alt": ("왼쪽: 빈 창고 문 앞에 경비 넷, 경비 없는 금고 옆엔 도둑 — 느낌으로 정하면. 오른쪽: 열 개 문마다 아주 작은 경비 한 명씩 — 골고루 나누면", "Left: four guards at the empty storeroom, a thief by the unguarded vault — going by gut. Right: one tiny guard at each of ten doors — spreading evenly"),
         "caption": ("느낌으로 정하면 엉뚱한 문을 지켜요. 골고루 나누면 다 얇아요.", "By gut, you guard the wrong door. Spread evenly, every door is thin."),
         "small": ("빈 창고엔 경비 넷, 금고엔 아무도 없어요. 문마다 한 명씩 두면 금고도 빈 창고만큼만 지켜요. 그래서 재야 해요.", "Four guards at the empty storeroom, none at the vault. One per door, and the vault gets no more than the storeroom. So you have to weigh it.")},
        {"svg": P3, "hero": True, "alt": ("저울: 왼쪽 접시에 도둑(올 가능성), 오른쪽 접시에 왕관(잃는 것), 가운데 곱하기. 옆의 위험 장부에는 금고 옆 문 빨강, 손님 방 문·왕의 창문 노랑, 빈 창고 문 초록. 왕과 경비가 함께 봄", "A scale: a thief on the left pan (how likely), a crown on the right (what we\'d lose), a times sign between. A risk ledger beside it — vault door red, guest door and king\'s window yellow, storeroom green. The king and a guard read it together"),
         "caption": ("위험 관리는 문마다 '올 가능성 × 잃는 것'을 재서 장부에 적는 거예요.", "Risk management is weighing each door — how likely × what we\'d lose — and writing it in a ledger."),
         "small": ("도둑이 올 가능성이 높고, 털리면 잃는 게 크면 빨강이에요. 둘 다 낮으면 초록이고요. 장부는 왕과 함께 봐요 — 빨간 문부터.", "Likely to be hit and costly if it is — that\'s red. Both low — that\'s green. The king reads the ledger with you, red doors first."),
         "tricks": (4, [
             (SCALE_I, ("가능성 × 잃는 것", "Likely × loss"), ("둘 다 재야 위험이에요", "both together make the risk"), "warm"),
             (LEDGER_I, ("장부에 적기", "Write it down"), ("빨강, 노랑, 초록", "red, yellow, green")),
             (PICK_I, ("빨강부터 고르기", "Red first"), ("막기·받기·넘기기·없애기", "block, accept, hand off, remove")),
             (KING_I, ("왕과 함께", "With the king"), ("얼마나 받아들일지는 왕이", "how much to accept is the king\'s call"), "calm"),
         ])},
        {"svg": P4, "alt": ("네 개의 문: 자물쇠와 경비가 붙은 문(막기), 초록 체크가 붙은 문(받아들이기), 동전 든 사람이 선 문(넘기기), 돌로 막아 버린 문(없애기)", "Four doors: one with a lock and a guard (reduce), one with a green check (accept), one with a coin-holder beside it (transfer), one bricked up (avoid)"),
         "caption": ("재고 나면 넷 중 하나예요. 막거나, 받아들이거나, 넘기거나, 없애거나.", "Once weighed, it\'s one of four: reduce it, accept it, hand it off, or remove it."),
         "small": ('빨간 문엔 자물쇠와 경비를 붙여요. 초록 문은 알고서 그냥 둬요. 보험에 넘기기도 하고, 문을 아예 막기도 해요. <a href="vulnmgmt-ko.html">틈 장부</a>도 여기서 순서가 정해져요.',
                   'Red doors get a lock and a guard. Green doors are left alone — knowingly. Some risk goes to insurance; some doors get bricked up. The <a href="vulnmgmt-en.html">crack ledger</a> gets its order from here too.')},
        {"svg": P5, "alt": ("다시 본 위험 장부: 금고 옆 문은 경비 셋으로 노랑, 손님 방 문은 새 자물쇠로 초록, 빈 창고 문은 그대로. 매달 달력. 왕이 '다 막아도 조금은 남아요'", "The ledger reviewed: vault door now yellow with three guards, guest door green with a new lock, storeroom as is. A monthly calendar. The king: even blocked, a little remains"),
         "caption": ("다 막아도 조금은 남아요. 그래서 매달 다시 재요.", "Even blocked, a little remains. So you weigh again every month."),
         "small": ('남은 위험은 알고 지켜봐요. 새 문이 생기고 도둑의 <a href="ttp-ko.html">버릇</a>이 바뀌면 저울도 다시 기울어요. <a href="compliance-ko.html">검사관</a>은 이 장부를 제일 먼저 봐요.',
                   'The leftover risk is known and watched. New doors appear, a thief\'s <a href="ttp-en.html">habits</a> change, and the scale tips again. The <a href="compliance-en.html">inspector</a> asks for this ledger first.')},
    ],
    "summary": (("<b>위험 관리</b> = 문마다 <b>올 가능성 × 잃는 것</b>을 재서 장부에 적고, <b>빨간 문부터</b> 막거나·받아들이거나·넘기거나·없애는 걸 <b>왕과 함께 계속</b> 정하는 것.",
                 "<b>Risk management</b> = weigh every door by <b>how likely × what we\'d lose</b>, write it in a ledger, and <b>with the king, keep deciding</b> — red doors first — to reduce, accept, transfer, or avoid."),
                ("Risk Management. 자산마다 위협이 일어날 가능성과 그때의 영향을 평가해 위험 등록부에 적고, 큰 위험부터 완화·수용·전가·회피 중 하나를 정해요. 다 막아도 남는 잔여 위험은 경영진이 받아들이고, 주기적으로 다시 평가해요.",
                 "For each asset, assess how likely a threat is and how bad its impact would be, record it in a risk register, and treat the biggest risks first — mitigate, accept, transfer, or avoid. The residual risk that remains is accepted by leadership and reassessed regularly.")),
    "glossary": [
        ("위험", "Risk", ("저울이 재는 것.", "What the scale weighs."), ("도둑이 올 가능성 × 털리면 잃는 것. 둘 중 하나만으론 위험이 아니에요.", "How likely a thief comes × what we\'d lose. One without the other isn\'t risk.")),
        ("위협", "Threat", ("도둑.", "The thief."), ('올 수 있는 나쁜 일. 도둑, 불, 홍수. → <a href="ttp-ko.html">도둑의 버릇</a>', 'The bad thing that could happen — thieves, fire, flood. → <a href="ttp-en.html">a thief\'s habits</a>')),
        ("취약점", "Vulnerability", ("헐렁한 문.", "The loose door."), ('도둑이 쓸 수 있는 틈. → <a href="zeroday-ko.html">아무도 모르는 구멍</a>', 'A crack a thief could use. → <a href="zeroday-en.html">the hole nobody knows</a>')),
        ("가능성 × 영향", "Likelihood × impact", ("저울의 두 접시.", "The two pans."), ("올 가능성이 높고 잃는 게 크면 빨강. 숫자로 적기도 해요.", "Likely and costly means red. Some castles use numbers.")),
        ("위험 등록부", "Risk register", ("위험 장부.", "The risk ledger."), ("문마다 색과 누가 맡는지, 뭘 하기로 했는지 적어요. 왕과 같이 봐요.", "Every door\'s color, who owns it, what was decided. Read with the king.")),
        ("수용 / 완화 / 전가 / 회피", "Accept / Mitigate / Transfer / Avoid", ("넷 중 하나.", "One of four."), ("그냥 두기, 막기, 보험에 넘기기, 문 없애기. 빨강엔 막기, 초록엔 두기.", "Leave it, reduce it, insure it, remove the door. Red gets reduced; green gets left.")),
        ("잔여 위험", "Residual risk", ("다 막아도 남는 것.", "What remains after blocking."), ("경비 셋을 세워도 조금은 남아요. 그건 왕이 알고 받아들여요.", "Even three guards leave a little. The king knows and accepts it.")),
        ("취약점 관리", "Vulnerability management", ("틈 장부의 순서.", "The crack ledger\'s order."), ('어느 틈부터 막을지는 위험 장부가 정해요. → <a href="vulnmgmt-ko.html">매달 도는 틈 장부</a>', 'Which crack to fix first comes from the risk ledger. → <a href="vulnmgmt-en.html">the crack ledger</a>')),
    ],
}
