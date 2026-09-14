from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
WATER = "#5B9BD5"


def chest(x, y, s=1.0, locked=False, ok=False):
    lock = ('<rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--bad)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--bad)" stroke-width="4" fill="none"/>' if locked else "")
    tick = '<circle cx="22" cy="-22" r="11" fill="var(--good)"/><path d="M16 -22 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>' if ok else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lock}{tick}</g>')


def bug(x, y, s=1.0, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><circle cx="-12" cy="-4" r="8" fill="{color}"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<circle cx="-14" cy="-2" r="2" fill="#FFF"/><circle cx="-8" cy="-2" r="2" fill="#FFF"/></g>')


def depot(x, y, s=1.0, inner="", name="⟦여분 상자 창고|spare chest shed⟧"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="0" width="120" height="80" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/>'
            f'<path d="M-70 0 L0 -36 L70 0 Z" fill="var(--good)"/>{inner}{label(0, 100, name, 11, "var(--muted)")}</g>')


def road(x1, x2, y):
    return f'<path d="M{x1} {y} H{x2}" stroke="var(--stone)" stroke-width="16" stroke-linecap="round"/><path d="M{x1 + 10} {y} H{x2 - 10}" stroke="var(--panel)" stroke-width="2" stroke-dasharray="14 12"/>'


def boat(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-60 0 q60 30 120 0 l-14 22 h-92z" fill="#8B5E3C"/>'
            f'<rect x="-2" y="-70" width="4" height="70" fill="#5A3B22"/><path d="M4 -66 L44 -30 L4 -30 Z" fill="#FFF8E7"/></g>')


def waves(x, y):
    return f'<path d="M{x} {y} q10 -8 20 0 t20 0 t20 0" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.7"/>'


def no_bridge(x, y):
    return (f'<path d="M{x} {y} h60" stroke="#8B5E3C" stroke-width="8" stroke-dasharray="10 12"/>'
            f'<path d="M{x + 20} {y - 12} l20 24 M{x + 40} {y - 12} l-20 24" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')


# 1. 여분 상자도 길이 이어진 방에 있어요
P1 = svg(320, sky(320) + castle(10, 80, 0.5) + label(125, 200, "⟦우리 성|our castle⟧", 12, "var(--muted)")
         + road(250, 740, 215)
         + depot(400, 95, 0.8, inner=chest(0, 45, 0.7))
         + person(560, 140, s=0.7, face=MASK, extra=BAG) + bug(632, 205, 0.7)
         + small_castle(660, 90, 0.5) + label(700, 185, "⟦마을|the town⟧", 12, "var(--muted)")
         + label(380, 300, "⟦길이 이어져 있으면 도둑도 벌레도 그 길로 와요|if a road connects it, thieves and bugs come down that road⟧", 12, "var(--ink)"))

# 2. 길이 이어진 여분 상자는 같이 잠겨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + castle(10, 60, 0.42) + chest(110, 220, 1.0, locked=True) + label(110, 258, "⟦성 안 상자|the chest in the castle⟧", 10, "var(--muted)")
         + road(150, 345, 225) + bug(300, 206, 0.7)
         + depot(400, 130, 0.8, inner=chest(0, 45, 0.7, locked=True))
         + person(500, 120, s=0.75, face=MASK, extra=BAG)
         + person(620, 110, s=0.8, face=FROWN, extra=SWEAT, **KING)
         + bubble(560, 30, 190, 34, "⟦여분 상자도 잠겼어요!|the spare chest is locked too!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦길이 이어진 상자는 같이 잠겨요 — 여분이 여분이 아니에요|a chest on the same road gets locked too — a spare that is no spare⟧", 12, "var(--ink)"))

# 3. 다리 없는 섬 창고 (hero)
P3 = svg(360, sky(360)
         + f'<rect x="300" y="150" width="460" height="160" fill="{WATER}" opacity="0.5"/>' + waves(330, 280) + waves(700, 290) + waves(540, 300)
         + castle(20, 60, 0.45) + label(123, 172, "⟦우리 성|our castle⟧", 12, "var(--muted)")
         + person(150, 210, s=0.7, face=MASK, extra=SWEAT) + bug(215, 275, 0.7) + label(180, 305, "⟦못 건너요|can\'t cross⟧", 10, "var(--bad)")
         + no_bridge(330, 205) + label(420, 130, "⟦다리가 없어요|no bridge⟧", 14, "var(--bad)", cls="d")
         + boat(450, 275) + person(405, 200, s=0.65, face=SMILE, **GUARD) + chest(475, 262, 0.6)
         + f'<ellipse cx="620" cy="250" rx="110" ry="40" fill="var(--good-soft)"/>'
         + depot(620, 150, 0.8, inner=chest(0, 45, 0.7), name="⟦섬 창고|the island shed⟧")
         + label(380, 340, "⟦제일 소중한 상자는 다리 없는 섬에 — 배로만, 사람이 직접|the most precious chest goes to an island with no bridge — by boat only, carried by a person⟧", 12, "var(--ink)", cls="d"))

# 4. 대신 불편해요 / 옮길 땐 검사
P4 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 40, "⟦불편해요|it\'s slow⟧", 14, "var(--ink)", cls="d")
         + boat(190, 205, 0.9) + person(135, 118, s=0.7, face=SMILE, **GUARD)
         + '<g transform="translate(300,110)"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="-26" y="-22" width="52" height="12" rx="4" fill="var(--accent)"/><path d="M-14 -28 v10 M14 -28 v10" stroke="#5A3B22" stroke-width="3"/></g>'
         + label(300, 122, "⟦하루|1 day⟧", 12, "#142033", cls="d")
         + label(190, 265, "⟦가져오는 데 하루가 걸려요|a whole day to fetch it back⟧", 11, "var(--accent)")
         + label(570, 40, "⟦옮길 땐 검사|inspect on the way⟧", 14, "var(--ink)", cls="d")
         + '<rect x="470" y="70" width="200" height="160" rx="6" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="4"/>'
         + person(490, 100, s=0.7, face=EYES, **GUARD)
         + '<g transform="translate(575,150)"><circle r="16" fill="none" stroke="var(--night)" stroke-width="4"/><path d="M12 12 l16 16" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>'
         + chest(625, 165, 0.7) + bug(625, 140, 0.55)
         + label(570, 250, "⟦작은 상자에도 벌레가 숨어요|even a small box can hide a bug⟧", 11, "var(--good)")
         + label(380, 300, "⟦안전한 만큼 불편해요 — 제일 소중한 것엔 그만한 값이에요|as safe as it is slow — worth it for the thing you can least afford to lose⟧", 12, "var(--ink)"))

# 5. 성이 잠겨도 섬 상자는 멀쩡해요
P5 = svg(300, sky(300)
         + label(380, 40, "⟦3개, 2곳, 1개는 다리 없이|3 copies, 2 places, 1 with no bridge⟧", 14, "var(--ink)", cls="d")
         + small_castle(90, 50, 0.45) + chest(130, 150, 1.1, locked=True) + label(130, 205, "⟦성 안|in the castle⟧", 11, "var(--muted)")
         + road(170, 340, 160) + person(250, 60, s=0.65, face=MASK, extra=BAG)
         + chest(380, 150, 1.1, locked=True) + label(380, 205, "⟦빌린 창고|the rented shed⟧", 11, "var(--muted)")
         + f'<rect x="520" y="120" width="240" height="110" fill="{WATER}" opacity="0.5"/>' + waves(540, 215)
         + '<ellipse cx="630" cy="175" rx="80" ry="24" fill="var(--good-soft)"/>' + chest(630, 150, 1.1, ok=True) + label(630, 202, "⟦섬|the island⟧", 11, "var(--muted)")
         + label(630, 236, "⟦이건 멀쩡해요|this one is fine⟧", 12, "var(--good)", cls="d")
         + person(700, 40, s=0.6, face=SMILE, **KING)
         + label(380, 280, "⟦성이 잠겨도 섬 상자는 멀쩡해요 — 거기서 다시 시작해요|even with the castle locked, the island chest is fine — that is where you start again⟧", 12, "var(--ink)"))

CUT_I = icon('<rect x="4" y="28" width="20" height="8" rx="2" fill="var(--stone-dark)"/><rect x="40" y="28" width="20" height="8" rx="2" fill="var(--stone-dark)"/><path d="M24 20 l16 24 M40 20 l-16 24" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
BOAT_I = icon('<path d="M8 38 q24 14 48 0 l-6 12 h-36z" fill="#8B5E3C"/><rect x="30" y="8" width="3" height="30" fill="#5A3B22"/><path d="M34 10 L52 30 L34 30 Z" fill="#FFF8E7"/><path d="M4 54 q8 -6 16 0 t16 0 t16 0 t8 0" stroke="#5B9BD5" stroke-width="3" fill="none"/>')
CHECK_I = icon('<rect x="8" y="30" width="28" height="20" rx="3" fill="#8B5E3C"/><path d="M8 30 h28 v-3 a14 6 0 0 0 -28 0z" fill="#5A3B22"/><circle cx="44" cy="22" r="11" fill="none" stroke="var(--night)" stroke-width="4"/><path d="M52 30 l8 8" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/><ellipse cx="22" cy="22" rx="7" ry="5" fill="var(--bad)"/>')
ISLAND_I = icon('<rect x="2" y="34" width="60" height="26" fill="#5B9BD5" opacity="0.5"/><ellipse cx="32" cy="42" rx="22" ry="8" fill="var(--good-soft)"/><rect x="20" y="20" width="24" height="18" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/><path d="M16 20 L32 8 L48 20 Z" fill="var(--good)"/>')

PAGE = {
    "slug": "airgap", "order": 97,
    "title": ("다리 없는 섬 창고", "The Island Shed With No Bridge"),
    "h1": ("<em>에어갭</em>이 뭐예요?", "What is an <em>Air Gap</em>?"),
    "sub": ("에어갭(Air Gap)과 오프라인 백업을 제일 소중한 상자를 다리 없는 섬 창고에 두는 이야기로 풀어봤어요.",
            "Air gaps and offline backups, told as a story about keeping the most precious chest in an island shed with no bridge."),
    "panels": [
        {"svg": P1, "alt": ("성에서 마을까지 길이 이어져 있고, 길 옆 창고에 여분 상자가 있다. 길 위를 도둑과 벌레가 성 쪽으로 걸어온다", "A road runs from the castle to the town, with a spare chest in a shed beside it. A thief and a bug walk down the road toward the castle"),
         "caption": ("여분 상자도 길이 이어진 방에 있어요.", "Even the spare chest sits in a room with a road to it."),
         "small": ('<a href="backup-ko.html">여분 상자</a>는 잘 만들어 뒀어요. 그런데 성과 마을을 잇는 길 옆에 있어요 — 도둑도 벌레도 그 길로 와요.',
                   'The <a href="backup-en.html">spare chest</a> was made properly. But it sits beside the road that joins the castle to the town — and thieves and bugs come down that road.')},
        {"svg": P2, "alt": ("성 안 상자와 창고의 여분 상자에 모두 도둑의 빨간 자물쇠가 걸렸다. 왕이 땀을 흘리며 '여분 상자도 잠겼어요!'", "Both the chest in the castle and the spare in the shed wear the thief\'s red lock. The king sweats: the spare chest is locked too!"),
         "caption": ("길이 이어진 여분 상자는 같이 잠겨요.", "A spare chest on the same road gets locked too."),
         "small": ('<a href="ransomware-ko.html">도둑의 자물쇠</a>는 길을 따라가며 닿는 상자마다 채워요. 여분 상자까지 잠기면 여분이 아니에요.',
                   'The <a href="ransomware-en.html">thief\'s lock</a> follows the road and snaps onto every chest it can reach. A spare that gets locked too is no spare.')},
        {"svg": P3, "hero": True, "alt": ("성 앞 물 건너 섬에 창고가 있다. 다리는 끊겨 있고, 경비가 배에 상자를 싣고 건넌다. 도둑과 벌레는 물가에서 못 건넌다", "Across the water from the castle is an island shed. The bridge is cut; a guard rows a chest over by boat. A thief and a bug stand at the shore, unable to cross"),
         "caption": ("에어갭은 다리 없는 섬 창고예요. 배로만, 사람이 직접 옮겨요.", "An air gap is an island shed with no bridge. Things get there by boat only, carried by a person."),
         "small": ("제일 소중한 상자는 마을과 길이 이어진 어떤 방에도 안 둬요. 길이 없으니 도둑도 벌레도 못 가요.", "The most precious chest never sits in any room with a road to the town. No road, so no thief and no bug can get there."),
         "tricks": (4, [
             (CUT_I, ("길을 끊어요", "Cut the road"), ("이어진 길이 하나도 없게", "not a single road left"), "warm"),
             (BOAT_I, ("배로만", "By boat only"), ("사람이 직접 들고 가요", "a person carries it over"), "calm"),
             (CHECK_I, ("옮길 땐 검사", "Inspect on the way"), ("상자 속 벌레는 배에서 잡아요", "catch bugs in the box before it lands"), "calm"),
             (ISLAND_I, ("하나는 꼭 섬에", "One always on the island"), ("여분 상자 중 하나", "one of the spare chests"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 경비가 배를 젓고 달력에 '하루'. 오른쪽: 창문 없는 방에서 경비가 돋보기로 작은 상자를 검사하는데 벌레가 붙어 있다", "Left: a guard rows a boat beside a calendar reading 1 day. Right: in a windowless room a guard inspects a small box with a magnifier, and a bug clings to it"),
         "caption": ("대신 불편해요. 가져오는 데 하루, 옮길 땐 꼭 검사해요.", "The price is inconvenience. A day to fetch it back, and an inspection on every trip."),
         "small": ('배로 옮기는 작은 상자에도 벌레가 숨을 수 있어요. 그래서 섬에 내리기 전 <a href="sandbox-ko.html">창문 없는 빈 방</a>에서 열어 봐요.',
                   'Even a small box carried by boat can hide a bug. So before it lands on the island, it is opened in the <a href="sandbox-en.html">windowless empty room</a>.')},
        {"svg": P5, "alt": ("상자 셋: 성 안 상자와 빌린 창고 상자는 도둑 자물쇠가 걸렸고, 물 건너 섬 상자만 초록 체크. 왕이 웃는다", "Three chests: the one in the castle and the one in the rented shed wear the thief\'s lock; only the island chest across the water has a green check. The king smiles"),
         "caption": ("성이 잠겨도 섬 상자는 멀쩡해요.", "Even with the castle locked, the island chest is fine."),
         "small": ('여분 상자 셋 중 하나는 꼭 섬에 둬요. 도둑이 성을 다 잠가도 <a href="incident-ko.html">거기서 다시 시작</a>해요.',
                   'Of the three spare chests, one always lives on the island. Even if the thief locks the whole castle, <a href="incident-en.html">that is where you start again</a>.')},
    ],
    "summary": (("<b>에어갭</b> = 제일 소중한 상자를 <b>길이 하나도 안 이어진 섬</b>에 두는 것. <b>배로만, 사람이 직접</b> 옮기고, 옮길 땐 검사해요. 불편하지만 도둑도 벌레도 못 가요.",
                 "An <b>air gap</b> = keeping the most precious chest on an <b>island with no road at all</b>. Moved <b>by boat only, by a person</b>, and inspected on every trip. Slow, but no thief and no bug can reach it."),
                ("Air Gap. 네트워크와 물리적으로 완전히 끊긴 시스템이나 백업이에요. 랜섬웨어가 연결된 백업까지 잠그기 때문에 오프라인·불변 백업이 마지막 방어선이 돼요. 데이터를 옮기는 USB 같은 이동식 매체가 새 위험이라 옮길 때마다 검사해요.",
                 "A system or backup with no network connection at all. Because ransomware locks connected backups too, an offline or immutable backup is the last line of defense. Removable media like USB drives become the new risk, so everything is scanned on the way across.")),
    "glossary": [
        ("에어갭", "Air gap", ("다리 없는 섬.", "The island with no bridge."), ("길이 하나도 안 이어진 방. 물리적으로 끊겨 있어요.", "A room no road reaches. Physically disconnected.")),
        ("오프라인 백업", "Offline backup", ("섬에 둔 여분 상자.", "The spare chest on the island."), ('평소엔 길이 없어요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'No road to it most of the time. → <a href="backup-en.html">the spare chest far away</a>')),
        ("불변 백업", "Immutable backup", ("고쳐 쓸 수 없는 상자.", "A chest no one can rewrite."), ("길이 있어도 정해진 날까지는 아무도 못 바꿔요. 섬 대신 쓰기도 해요.", "Even with a road, nobody can change it until its date. Sometimes used instead of an island.")),
        ("이동식 매체 위험", "Removable media risk", ("배에 실은 작은 상자.", "The small box on the boat."), ('USB 같은 작은 상자가 새 길이 돼요. 옮길 때마다 <a href="sandbox-ko.html">빈 방</a>에서 검사해요.', 'A small box like a USB drive becomes the new road. Inspect it in the <a href="sandbox-en.html">empty room</a> every trip.')),
        ("3-2-1 규칙", "3-2-1 rule", ("셋 · 둘 · 하나.", "Three · two · one."), ("사본 셋, 두 곳, 하나는 멀리 — 그 하나가 섬이면 제일 좋아요.", "Three copies, two places, one far away — best of all if that one is the island.")),
        ("랜섬웨어", "Ransomware", ("길 따라 채우는 자물쇠.", "Locks that follow the road."), ('닿는 상자마다 잠가요. → <a href="ransomware-ko.html">상자마다 채운 도둑의 자물쇠</a>', 'Locks every chest it can reach. → <a href="ransomware-en.html">the thief\'s lock on every chest</a>')),
        ("백업", "Backup", ("여분 상자.", "The spare chest."), ('베껴서 다른 곳에 두는 것. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'A copy kept somewhere else. → <a href="backup-en.html">the spare chest far away</a>')),
        ("망 분리", "Network segregation (OT)", ("기계 방의 끊긴 길.", "The cut road to the machine room."), ('공장 기계처럼 멈추면 안 되는 방은 길을 끊거나 아주 좁혀요. → <a href="iotsec-ko.html">말 못 하는 기계들</a>', 'Rooms that must never stop, like factory machines, get their road cut or narrowed. → <a href="iotsec-en.html">the machines that cannot speak</a>')),
    ],
}
