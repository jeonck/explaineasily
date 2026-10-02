from _draw import *
from _world import *


def scale(x, y, left_label, right_label, left_fill="var(--accent)", right_fill="var(--good)", broken=False):
    """저울. (x,y) 는 받침대 바닥(ground) 기준점. broken=True 면 빔 가운데가 갈라져요(둘 다 동시에 못 가짐)."""
    beam_w = 160
    lx, rx_ = -beam_w / 2, beam_w / 2
    out = f'<g transform="translate({x},{y})">'
    out += '<rect x="-6" y="-66" width="12" height="66" fill="var(--stone-dark)"/><rect x="-32" y="-4" width="64" height="10" rx="3" fill="var(--stone-dark)"/>'
    if broken:
        out += f'<rect x="{lx}" y="-70" width="60" height="8" rx="3" fill="var(--stone-dark)"/><rect x="{rx_ - 60}" y="-70" width="60" height="8" rx="3" fill="var(--stone-dark)"/>'
        out += '<path d="M-14 -78 L2 -50 L18 -78" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        out += f'<rect x="{lx}" y="-70" width="{beam_w}" height="8" rx="3" fill="var(--stone-dark)"/>'
    out += '<circle cy="-66" r="5" fill="var(--stone-dark)"/>'
    out += f'<line x1="{lx}" y1="-66" x2="{lx}" y2="-24" stroke="var(--stone-dark)" stroke-width="3"/><ellipse cx="{lx}" cy="-18" rx="34" ry="11" fill="{left_fill}"/>'
    out += f'<line x1="{rx_}" y1="-66" x2="{rx_}" y2="-24" stroke="var(--stone-dark)" stroke-width="3"/><ellipse cx="{rx_}" cy="-18" rx="34" ry="11" fill="{right_fill}"/>'
    out += label(lx, 2, left_label, 11, "var(--ink)") + label(rx_, 2, right_label, 11, "var(--ink)")
    return out + "</g>"


# 1. 창고 둘이 서로 연락이 안 돼요
P1 = svg(320, sky(320)
         + shed(130, 260, 0.7, label_text="⟦창고 A|Warehouse A⟧") + shed(630, 260, 0.7, label_text="⟦창고 B|Warehouse B⟧")
         + '<path d="M260 160 L330 160" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M430 160 L500 160" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M345 140 L365 180 L385 140" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + label(380, 125, "⟦선이 끊겼어요!|the line is cut!⟧", 13, "var(--bad)", cls="d")
         + person(90, 204, s=0.5, face=FROWN, **OPERATOR) + bubble(10, 120, 190, 40, "⟦손님을 받아도 될까요?|should we keep serving guests?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(640, 204, s=0.5, face=FROWN, **MECHANIC) + bubble(555, 120, 195, 40, "⟦여긴 숫자가 안 바뀌는데요|our numbers aren\'t updating⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦창고 둘이 서로 연락이 안 돼요 — 손님을 받을지 멈출지 고민해요|the two warehouses can\'t reach each other — serve guests, or stop?⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 둘 다는 동시에 못 가져요 (bad-soft, 갈라진 저울)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + scale(380, 245, "⟦정확한 답만|only correct answers⟧", "⟦일단 열려 있기|stay open now⟧", "var(--accent)", "var(--good)", broken=True)
         + person(110, 178, s=0.6, face=FROWN + SWEAT, **OPERATOR) + bubble(20, 95, 210, 40, "⟦둘 다 한 번에는 안 돼요|can\'t have both at once⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(590, 178, s=0.6, face=FROWN, **MANAGER)
         + label(380, 280, "⟦연락이 끊기면, 정확함과 열려있기 둘 다는 동시에 못 가져요|once the line breaks, you can\'t have both at the same time⟧", 12, "var(--bad)"))

# 3. CAP = 선이 끊기면 하나를 골라야 해요 (hero)
P3 = svg(360, sky(360)
         + label(380, 45, "⟦선이 끊겼어요|the line is cut⟧", 13, "var(--bad)", cls="d")
         + '<path d="M355 58 L375 92 L395 58" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + '<path d="M345 105 Q240 150 165 215" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M415 105 Q520 145 560 190" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + booth(150, 250, 0.8, label_text="⟦문 닫아요|closes⟧", lit=False)
         + board(430, 150, 260, 140, "⟦안내 게시판|INFO BOARD⟧", ("⟦열림: 계속 받아요|open: keep serving⟧", "⟦숫자는 나중에 맞춰요|numbers catch up later⟧", "⟦잠깐은 다를 수 있어요|may briefly differ⟧"), 1.0)
         + person(60, 239, s=0.55, face=FROWN, **OPERATOR) + person(705, 239, s=0.5, face=SMILE, **MANAGER)
         + label(380, 335, "⟦선이 끊기면, 정확함을 택해 문을 닫거나 일단 열어 두고 나중에 맞추거나 둘 중 하나를 골라야 해요|when the line breaks, close for correctness, or stay open and catch up later⟧", 13, "var(--ink)", cls="d"))

# 4. 저울 그림 — 공원 두 사례 비교
P4 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 40, "⟦정확함(닫기)|correctness (close)⟧", 14, "var(--ink)", cls="d")
         + booth(190, 250, 0.8, label_text="⟦문 닫아요|closes⟧", lit=False)
         + label(570, 40, "⟦열려있기(나중에 맞춤)|staying open (catch up later)⟧", 13, "var(--ink)", cls="d")
         + board(460, 150, 220, 130, "⟦안내 게시판|INFO BOARD⟧", ("⟦일단 계속 보여줘요|keeps showing something⟧", "⟦몇 분 뒤 맞아요|matches up soon⟧"), 1.0)
         + label(380, 300, "⟦무엇이 더 중요한지에 따라 골라요 — 매표소는 정확함을, 안내판은 열림을|pick by what matters more — ticket booths choose correctness, info boards choose staying open⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 평소엔 고민할 필요 없어요
P5 = svg(300, sky(300)
         + shed(130, 240, 0.7, label_text="⟦창고 A|Warehouse A⟧") + shed(630, 240, 0.7, label_text="⟦창고 B|Warehouse B⟧")
         + '<path d="M250 170 L510 170" stroke="var(--good)" stroke-width="4"/>'
         + '<circle cx="380" cy="170" r="14" fill="var(--good)"/><path d="M373 170 l5 6 l10 -14" stroke="#FFF8E7" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + label(380, 140, "⟦평소엔 선이 멀쩡해요|normally the line is just fine⟧", 12, "var(--good)")
         + label(380, 280, "⟦이건 선이 끊겼을 때만 하는 선택이에요 — 평소엔 고민할 필요 없어요|this choice only matters when the line breaks⟧", 12, "var(--ink)"))

BOTH_I = icon('<circle cx="20" cy="32" r="10" fill="var(--good)"/><circle cx="44" cy="32" r="10" fill="var(--good)"/><path d="M28 32 h8" stroke="var(--good)" stroke-width="4"/><path d="M14 46 l6 6 l10 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
FORK_I = icon('<path d="M8 32 h16" stroke="var(--stone-dark)" stroke-width="4" stroke-linecap="round"/><path d="M28 24 l8 16 l-16 0z" fill="var(--bad)"/><path d="M40 32 L54 16" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M40 32 L54 48" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
MONEY_I = icon('<circle cx="32" cy="32" r="20" fill="var(--accent)"/><text x="32" y="40" font-size="22" font-weight="700" text-anchor="middle" fill="#FFF8E7">₩</text>')
BOARD_I = icon('<rect x="8" y="14" width="48" height="34" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M16 24 h32 M16 32 h24 M16 40 h18" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "captheorem", "order": 17,
    "title": ("정확함과 항상 열림, 둘 다는 못 가져요", "You Can't Have Both Correctness and Always-Open"),
    "h1": ("<em>CAP 정리</em>가 뭐예요?", "What is the <em>CAP Theorem</em>?"),
    "sub": ("CAP 정리를, 선이 끊긴 두 창고 중 하나를 골라야 하는 이야기로 풀어봤어요.",
            "The CAP theorem, told as a story about two warehouses that lose contact and must choose."),
    "panels": [
        {"svg": P1, "alt": ("두 창고 사이 연락선이 끊기고 각 창구 직원이 손님을 받을지 고민함", "The line between two warehouses is cut; each clerk wonders whether to keep serving guests"),
         "caption": ("창고 둘이 서로 연락이 안 돼요.", "The two warehouses can't reach each other."),
         "small": ("손님을 받을지 멈출지 고민해요.", "Should they keep serving guests, or stop?")},
        {"svg": P2, "alt": ("빔이 갈라진 저울. 한쪽엔 정확한 답만, 다른 쪽엔 일단 열려 있기", "A scale with a cracked beam, one side only correct answers, the other staying open now"),
         "caption": ("왜 어려운가: 둘 다는 동시에 못 가져요.", "Why it's hard: you can't have both at once."),
         "small": ("연락이 끊기면, 정확함과 열려있기 둘 다는 동시에 못 가져요.", "Once the line breaks, you can't have both correctness and staying open.")},
        {"svg": P3, "hero": True, "alt": ("선이 끊긴 지점에서 한쪽은 문 닫은 매표소로, 한쪽은 계속 여는 안내 게시판으로 갈라짐", "From the cut line, one path leads to a closed ticket booth, the other to an info board that stays open"),
         "caption": ("CAP = 선이 끊기면, 정확함과 열려있기 중 하나를 골라야 해요.", "CAP = when the line breaks, choose correctness or staying open."),
         "small": ("문을 닫거나(일관성), 일단 열어 두고 나중에 맞추거나(가용성).", "Close the doors (consistency), or stay open and catch up later (availability)."),
         "tricks": (4, [
             (BOTH_I, ("평소엔 둘 다 괜찮아요", "Normally both are fine"), ("선이 멀쩡할 때는요", "as long as the line holds"), "calm"),
             (FORK_I, ("선이 끊기면 골라야 해요", "A broken line forces a choice"), ("둘 다는 못 가져요", "you can't keep both")),
             (MONEY_I, ("돈 다루는 곳은 정확함 우선", "Money usually picks correctness"), ("틀린 답보다 잠깐 닫는 게 나아요", "better closed than wrong"), "warm"),
             (BOARD_I, ("보여주기용 정보는 열림 우선", "Display info usually picks staying open"), ("조금 늦어도 괜찮아요", "a little stale is fine")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 정확함을 택해 문 닫은 매표소. 오른쪽: 열려있기를 택해 계속 보여주는 안내 게시판", "Left: a ticket booth closed for correctness. Right: an info board that stays open"),
         "caption": ("저울 그림: 정확함(닫기) vs 열려있기(나중에 맞춤).", "The scale: correctness (close) vs staying open (catch up later)."),
         "small": ("매표소는 정확함을, 안내판은 열림을 택해요.", "Ticket booths choose correctness; info boards choose staying open.")},
        {"svg": P5, "alt": ("평소엔 두 창고가 초록 선으로 잘 연결되어 체크 표시가 뜸", "On a normal day, the two warehouses are connected by a solid green line with a checkmark"),
         "caption": ("이건 선이 끊겼을 때만 하는 선택이에요.", "This choice only matters when the line breaks."),
         "small": ("평소엔 고민할 필요 없어요.", "Day to day, there's nothing to decide.")},
    ],
    "summary": (("<b>CAP 정리</b> = 창고 사이 <b>선이 끊기면</b>, <b>정확함</b>과 <b>늘 열려있기</b> 둘 다는 동시에 못 가지고 <b>하나를 골라야</b> 한다는 규칙.",
                 "The <b>CAP theorem</b>: when the line between warehouses <b>breaks</b>, you can't have both <b>correctness</b> and <b>always-open</b> at once — you must <b>choose one</b>."),
                ("Consistency(일관성), Availability(가용성), Partition tolerance(분단 허용)의 앞 글자. 네트워크 파티션(선 끊김)은 현실에서 늘 일어날 수 있다고 가정하므로, 사실상 남은 선택은 일관성이냐 가용성이냐예요. 조금 더 보면 PACELC도 있어요 — 끊기지 않아도 속도와 정확함 사이에서 또 고른다는 확장판.",
                 "The initials of Consistency, Availability, and Partition tolerance. Since network partitions must always be assumed possible, the real choice in practice is consistency vs. availability. A further refinement, PACELC, says you trade off latency vs. correctness even when nothing is broken.")),
    "glossary": [
        ("CAP 정리", "CAP Theorem", ("선이 끊기면 셋 중 둘만 가질 수 있다는 규칙.", "The rule that you can only keep two of three when the line breaks."), ("분산 시스템을 설계할 때 꼭 거쳐가는 질문이에요.", "A question every distributed system design has to answer.")),
        ("일관성", "Consistency (C)", ("모든 창구가 같은 답을 주는 것.", "Every counter gives the same answer."), ("선이 끊기면 이걸 지키려고 문을 닫기도 해요.", "To keep this, a counter may close when the line breaks.")),
        ("가용성", "Availability (A)", ("항상 응답은 하는 것.", "Always giving some response."), ("그 답이 최신이 아닐 수도 있어요.", "But that answer might not be the latest.")),
        ("분단 허용", "Partition Tolerance (P)", ("선이 끊겨도 시스템이 계속 도는 것.", "The system keeps running even when the line is cut."), ("현실에선 사실상 늘 가정해야 해요.", "In practice, you have to assume this will happen.")),
        ("네트워크 파티션", "Network Partition", ("창구끼리 연락이 끊기는 사건.", "The event where counters lose contact."), ("CAP에서 선택을 강요하는 바로 그 상황이에요.", "The exact situation that forces the CAP choice.")),
        ("PACELC", "PACELC", ("끊기지 않아도 속도냐 정확함이냐 또 고른다는 확장판.", "An extension: even without a break, you trade latency vs. correctness."), ("CAP은 끊겼을 때만, PACELC은 평소에도 다뤄요.", "CAP covers only the break; PACELC covers every day.")),
        ("강한 일관성", "Strong Consistency", ("늘 최신 정답만 보여주는 약속.", "The promise of always showing the latest, correct answer."), ("돈 다루는 곳에서 주로 선호해요.", "Usually preferred wherever money is involved.")),
        ("최종 일관성", "Eventual Consistency", ("조금 늦게라도 결국 맞춰지는 약속.", "The promise that things match up eventually, even if a bit late."), ('→ <a href="eventualconsistency-ko.html">조금 늦게 맞춰지는 재고판</a>', '→ <a href="eventualconsistency-en.html">the inventory board that catches up a little late</a>')),
    ],
}
