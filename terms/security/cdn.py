from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
HATS = (None, "#E9B44C", "var(--stone-dark)", "var(--good)", None, "#E9B44C")


def book(x, y, s=1.0, color="var(--accent)", old=False):
    c = "var(--stone)" if old else color
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-20" width="32" height="40" rx="2" fill="{c}"/><rect x="-12" y="-16" width="24" height="32" rx="1" fill="var(--panel)"/>'
            f'<circle cx="-2" cy="-4" r="5" fill="{"var(--stone)" if old else "var(--good)"}"/><path d="M-8 10 l6 -8 l5 5 l3 -3 l4 6z" fill="{"var(--stone-dark)" if old else "var(--accent)"}"/></g>')


def depot(x, y, s=1.0, books=3, old=False, name="⟦복사본 창고|copy depot⟧"):
    shelf = "".join(book(-24 + i * 24, 30, 0.6, old=old) for i in range(books))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-46" y="0" width="92" height="66" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-54 0 L0 -30 L54 0 Z" fill="var(--good)"/>{shelf}{label(0, 86, name, 11, "var(--muted)")}</g>')


def town(x, y, name, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="0" width="52" height="40" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/>'
            f'<path d="M-32 0 L0 -22 L32 0 Z" fill="var(--bad)"/><rect x="-6" y="18" width="12" height="22" fill="{WOOD}"/>{label(0, 56, name, 11, "var(--muted)")}</g>')


def road(pts, color="var(--stone-dark)", w=6, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{pts}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round"{d}/>'


TOWNS = ((70, 60, "⟦동쪽 마을|East town⟧"), (90, 210, "⟦서쪽 마을|West town⟧"), (660, 50, "⟦북쪽 마을|North town⟧"), (680, 220, "⟦남쪽 마을|South town⟧"))

# 1. 멀리서 다 찾아온다
P1 = svg(300, sky(300) + castle(270, 90, 0.5) + label(385, 60, "⟦성|the castle⟧", 13, "var(--ink)", cls="d")
         + "".join(town(x, y, n, 0.9) for x, y, n in TOWNS)
         + road("M100 90 C200 120 250 160 300 190", "var(--bad)", 6, "10 8") + road("M120 230 C200 220 250 210 300 200", "var(--bad)", 6, "10 8")
         + road("M640 80 C560 120 520 160 470 190", "var(--bad)", 6, "10 8") + road("M650 240 C580 230 520 215 470 200", "var(--bad)", 6, "10 8")
         + "".join(person(x, 200, s=0.5, hat=HATS[i], shirt="#4A5A72", face=FROWN) for i, x in enumerate((300, 340, 420, 460)))
         + label(380, 285, "⟦먼 마을 사람은 오래 걸리고, 성 앞은 붐벼요|far towns wait a long time, and the castle gate is jammed⟧", 13, "var(--muted)"))

# 2. 다들 같은 그림책을 원한다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + '<rect x="520" y="40" width="240" height="240" fill="var(--stone-dark)"/>' + battlements(520, 22, 240, 5, "var(--stone-dark)", 20)
         + '<rect x="560" y="80" width="90" height="80" rx="6" fill="var(--sky)"/>' + person(575, 70, s=0.6, face=FROWN + SWEAT, **CLERK)
         + book(690, 120, 0.9) + book(690, 170, 0.9) + book(690, 220, 0.9)
         + "".join(person(x, 120, s=0.65, hat=HATS[i], shirt="#4A5A72", face=SMILE) + bubble(x - 20, 50, 110, 30, "⟦그 그림책요|that book⟧", 11, "var(--panel)", "var(--line)", "bottom") for i, x in enumerate((40, 150, 260, 370)))
         + label(250, 255, "⟦성이 매번 똑같은 걸 꺼내줘요|the castle fetches the same thing over and over⟧", 13, "var(--muted)"))

# 3. CDN = 마을마다 복사본 창고 (hero)
P3 = svg(340, sky(340) + castle(280, 60, 0.4) + label(372, 40, "⟦성 (원본)|castle (the original)⟧", 12, "var(--ink)", cls="d")
         + road("M300 150 L150 120", "var(--accent)", 3, "6 6") + road("M300 160 L160 250", "var(--accent)", 3, "6 6")
         + road("M450 150 L600 110", "var(--accent)", 3, "6 6") + road("M450 160 L600 250", "var(--accent)", 3, "6 6")
         + depot(120, 90, 0.8) + depot(130, 220, 0.8) + depot(630, 80, 0.8) + depot(630, 220, 0.8)
         + "".join(person(x, y, s=0.45, hat=HATS[i], shirt="#4A5A72", face=SMILE) for i, (x, y) in enumerate(((40, 110), (50, 240), (700, 100), (710, 240))))
         + label(380, 235, "⟦한 번만 가져다 두고|fetched from the castle once⟧", 12, "var(--muted)")
         + label(380, 322, "⟦가까운 창고에서 바로 받아요. 없으면 성에 한 번만 다녀와요|you get it from the nearest depot; if it\'s missing, one trip to the castle⟧", 12, "var(--muted)"))

# 4. 성이 그림을 바꾸면 복사본을 간다
P4 = svg(300, sky(300) + castle(300, 60, 0.4)
         + bubble(300, 20, 160, 34, "⟦구판은 버려요!|toss the old edition!⟧", 12, "var(--accent-soft)", "var(--accent)", "bottom")
         + road("M320 150 L170 130", "var(--accent)", 3, "6 6") + road("M470 150 L610 130", "var(--accent)", 3, "6 6")
         + depot(130, 100, 0.85, old=True) + '<path d="M100 130 l30 30 M130 130 l-30 30" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>' + label(130, 210, "⟦옛날 그림|old picture⟧", 11, "var(--bad)")
         + depot(650, 100, 0.85) + '<path d="M625 138 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>' + label(650, 210, "⟦새 그림|new picture⟧", 11, "var(--good)")
         + '<g transform="translate(380,230)"><circle r="22" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -14 V0 L9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(380, 275, "⟦유통기한이 지나거나, 성이 '버려' 하면 새로 받아요|when it expires, or the castle says toss it, a fresh copy comes⟧", 12, "var(--muted)"))

# 5. 내 편지는 창고에 안 둔다
LETTER = '<rect x="46" y="66" width="34" height="24" rx="2" fill="var(--panel)" stroke="var(--accent)" stroke-width="2"/><path d="M46 68 L63 80 L80 68" stroke="var(--accent)" stroke-width="2" fill="none"/>'
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + depot(120, 80, 0.9) + person(230, 100, s=0.8, **ME)
         + bubble(200, 20, 160, 34, "⟦내 편지는요?|and my letters?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + '<path d="M270 190 L340 190" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 6"/><path d="M330 180 L342 190 L330 200" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + castle(330, 150, 0.22) + label(190, 270, "⟦내 편지는 성에 직접 가야 해요|your own letters mean a trip to the castle⟧", 12, "var(--muted)")
         + depot(500, 80, 0.9, old=True) + person(610, 100, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=FROWN)
         + bubble(570, 20, 170, 34, "⟦어제 그림이잖아요|that\'s yesterday\'s picture⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + label(570, 270, "⟦갈기 전엔 옛날 그림을 보여줄 수 있어요|until it\'s swapped, you may see the old one⟧", 12, "var(--muted)"))

COPY_I = icon('<rect x="14" y="14" width="24" height="32" rx="2" fill="var(--accent)"/><rect x="26" y="20" width="24" height="32" rx="2" fill="var(--accent)" stroke="var(--panel)" stroke-width="2"/>')
NEAR_I = icon('<circle cx="20" cy="40" r="7" fill="var(--good)"/><path d="M27 40 H44" stroke="var(--good)" stroke-width="3"/><path d="M44 30 L54 40 L44 50 Z" fill="var(--good)"/><rect x="40" y="10" width="14" height="12" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/>')
TTL_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="3"/><path d="M32 18 V32 L42 38" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CALM_I = icon('<rect x="8" y="26" width="48" height="28" fill="var(--stone-dark)"/><rect x="8" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="18" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="18" width="10" height="10" fill="var(--stone-dark)"/><text x="32" y="46" text-anchor="middle" font-size="12" fill="#F5E6B8">zZ</text>')

PAGE = {
    "slug": "cdn", "order": 33,
    "title": ("마을마다 복사본 창고", "A Copy in Every Town"),
    "h1": ("<em>CDN</em>이 뭐예요?", "What is a <em>CDN</em>?"),
    "sub": ("콘텐츠 전송 네트워크(Content Delivery Network)를 마을마다 둔 복사본 창고 이야기로 풀어봤어요.",
            "Content Delivery Network, told as a story about copy depots in every town."),
    "panels": [
        {"svg": P1, "alt": ("동서남북 네 마을에서 성까지 긴 빨간 길이 이어지고 성 앞엔 찡그린 사람들이 줄을 섬", "Long red roads from four towns converge on the castle, where frowning people queue"),
         "caption": ("성의 그림책을 보러 멀리서 다 찾아와요.", "Everyone travels to the castle for its picture books."),
         "small": ("먼 마을 사람은 오래 걸리고, 성 앞은 붐벼요.", "Far towns wait a long time, and the castle gate is jammed.")},
        {"svg": P2, "alt": ("네 사람이 모두 '그 그림책요' 하고, 창구 직원은 땀을 흘리며 같은 책 세 권을 꺼냄", "Four people all ask for that book; the sweating clerk keeps fetching the same three books"),
         "caption": ("다들 같은 그림책을 원해요.", "Everyone wants the same books."),
         "small": ("성이 매번 똑같은 걸 꺼내줘요. 아까워요.", "The castle fetches the same thing over and over. What a waste.")},
        {"svg": P3, "hero": True, "alt": ("가운데 성(원본)과 네 마을의 복사본 창고, 각 마을 사람은 가까운 창고에서 책을 받음", "The castle (original) in the middle and copy depots in four towns; each townsperson gets books from the nearest depot"),
         "caption": ("CDN은 마을마다 복사본 창고를 둬요.", "A CDN puts a copy depot in every town."),
         "small": ("가까운 창고에서 바로 받아요. 창고에 없으면 성에 한 번만 가져다 두고, 다음부턴 창고에서요.", "You get it from the nearest depot. If it's missing, one trip to the castle — then it's in the depot for good."),
         "tricks": (4, [
             (COPY_I, ("복사본", "Copies"), ("원본은 성에, 복사본은 창고에", "originals at the castle, copies in depots"), "warm"),
             (NEAR_I, ("가까운 창고", "The nearest depot"), ("가까울수록 빨라요", "the nearer, the faster"), "calm"),
             (TTL_I, ("유통기한", "Expiry"), ("오래된 복사본은 버려요", "stale copies get tossed")),
             (CALM_I, ("성은 한가해요", "The castle rests"), ("붐비는 날도 조용해요", "quiet even on busy days"), "calm"),
         ])},
        {"svg": P4, "alt": ("성이 '구판은 버려요!' 하자 한 창고의 옛날 그림엔 X, 다른 창고엔 새 그림과 체크, 가운데 시계", "The castle says toss the old edition; one depot's old picture is crossed out, another shows the new one with a check; a clock in the middle"),
         "caption": ("성이 그림을 바꾸면 창고 복사본을 갈아요.", "When the castle changes a picture, the depots swap their copies."),
         "small": ("유통기한이 지나거나, 성이 '구판 버려' 하면 새로 받아와요.", "When a copy expires, or the castle says toss it, a fresh one comes down.")},
        {"svg": P5, "alt": ("왼쪽: '내 편지는요?' 묻는 사람에게 창고 대신 성으로 가는 화살표. 오른쪽: '어제 그림이잖아요' 하는 사람과 옛날 그림이 든 창고", "Left: someone asks and my letters?, and an arrow points past the depot to the castle. Right: someone says that's yesterday's picture beside a depot holding an old copy"),
         "caption": ("내 편지는 창고에 안 둬요.", "Your own letters never go in the depot."),
         "small": ("다 같이 보는 그림책만 복사해요. '내 편지'는 성에 직접 가야 해요. 그리고 갈기 전엔 옛날 그림을 보여줄 수 있어요.", "Only things everyone reads get copied; your own letters mean a trip to the castle. And until a copy is swapped, you may see the old one.")},
    ],
    "summary": (("<b>CDN</b> = 성의 그림책 <b>복사본</b>을 마을마다 창고에 두고, <b>가까운 데서</b> 받게 하는 것.",
                 "A <b>CDN</b> = <b>copies</b> of the castle's picture books in a depot in every town, so everyone gets them from <b>nearby</b>."),
                ("Content Delivery Network. 사진, 영상, 그림책처럼 다 같이 보는 건 창고에서, 내 편지는 성에서. Cloudflare, Akamai, AWS CloudFront 같은 것들. 마을 곳곳의 역(SASE)과 같은 생각인데, 보안 대신 그림책이에요.",
                 "Content Delivery Network. Photos, videos and picture books — things everyone reads — come from the depot; your own letters come from the castle. Cloudflare, Akamai, AWS CloudFront. Same idea as the hubs all over town (SASE), but for picture books instead of security.")),
    "glossary": [
        ("캐시", "Cache", ("복사본.", "The copy."), ('창고에 놓아둔 그림책. → <a href="proxy-ko.html">심부름꾼의 바구니</a>와 같은 것', 'The book left in the depot. → the same as the <a href="proxy-en.html">runner\'s basket</a>')),
        ("엣지 · PoP", "Edge · PoP", ("마을 창고.", "The town depot."), ('사람 가까이에 둔 창고. → <a href="sase-ko.html">마을 곳곳의 역</a>과 같은 자리', 'A depot placed near people. → the same spot as the <a href="sase-en.html">hubs all over town</a>')),
        ("오리진", "Origin", ("성.", "The castle."), ("원본이 있는 곳. 창고에 없을 때만 찾아가요.", "Where the original lives. Visited only when the depot lacks something.")),
        ("TTL", "TTL (time to live)", ("유통기한.", "The expiry date."), ("복사본을 얼마나 오래 둘지. 지나면 다시 받아와요.", "How long a copy stays. Past it, a fresh one is fetched.")),
        ("캐시 히트 · 미스", "Cache hit · miss", ("창고에 있음 · 없음.", "In the depot · not in the depot."), ("있으면 바로, 없으면 성에 한 번.", "There? Right away. Not there? One trip to the castle.")),
        ("퍼지", "Purge", ("구판 버려.", "Toss the old edition."), ("성이 유통기한 전에 창고 복사본을 지우게 하는 것.", "The castle clearing depot copies before they expire.")),
        ("정적 · 동적", "Static · dynamic", ("그림책 · 내 편지.", "Picture books · my letters."), ("다 같이 보는 건 복사하고, 나한테만 오는 건 안 해요.", "Shared things get copied; things meant just for you don't.")),
        ("오리진 보호", "Origin shielding", ("붐비는 날 창고가 대신 받아요.", "On busy days the depots take the crowd."), ('성 앞이 조용해져요. 도둑 떼가 몰려와도(DDoS) 창고가 먼저 받아요.', 'The castle gate stays quiet. Even a mob of thieves (DDoS) hits the depots first.')),
    ],
}
