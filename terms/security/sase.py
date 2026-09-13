from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def house(x, y, name, roof="var(--bad)", s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="0" width="64" height="48" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-40 0 L0 -28 L40 0 Z" fill="{roof}"/><rect x="-8" y="22" width="16" height="26" fill="{WOOD}"/>{label(0, 66, name, 12, "var(--muted)")}</g>')


def shed(x, y, name, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-32" y="0" width="64" height="48" fill="var(--stone-dark)"/>'
            f'<path d="M-40 0 L0 -28 L40 0 Z" fill="var(--stone)"/><rect x="-8" y="20" width="16" height="28" fill="var(--night)"/>{label(0, 66, name, 12, "var(--muted)")}</g>')


def road(pts, color="var(--stone-dark)", w=8, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{pts}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round"{d}/>'


TINY_ICONS = ('<path d="M-28 -6 L-18 -14 L-8 -6 Z" fill="var(--good)"/><rect x="-26" y="-6" width="16" height="10" fill="var(--panel)"/>'
              '<path d="M-6 -6 L4 -14 L14 -6 Z" fill="var(--stone)"/><rect x="-4" y="-6" width="16" height="10" fill="var(--stone-dark)"/>'
              '<rect x="20" y="-12" width="10" height="16" rx="3" fill="#FFD166" stroke="var(--night)" stroke-width="1.5"/>')


def station(x, y, s=1.0, full=True):
    icons = f'<g transform="translate(0,26)">{TINY_ICONS}</g>' if full else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-44" y="0" width="88" height="44" rx="6" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/>'
            f'<rect x="-50" y="-8" width="100" height="10" rx="3" fill="var(--accent)"/><rect x="-14" y="-40" width="28" height="32" rx="4" fill="var(--accent)"/>'
            f'{label(0, -18, "⟦역|HUB⟧", 13, "#FFF", cls="d")}{icons}</g>')


# 1. 옛날엔 모든 길이 성문을 지났다
P1 = svg(300, sky(300)
         + road("M110 210 C200 200 260 150 330 150 C400 150 430 200 470 210", "var(--bad)", 8, "12 8")
         + road("M470 210 C520 200 560 190 620 190", "var(--bad)", 8, "12 8")
         + house(110, 150, "⟦집|home⟧") + castle(240, 60, 0.4) + label(330, 40, "⟦성문|the gate⟧", 13, "var(--ink)", cls="d")
         + shed(620, 100, "⟦바깥 창고|the shed⟧")
         + person(300, 200, s=0.6, **ME)
         + '<path d="M115 215 L615 215" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 8" opacity="0.5"/>'
         + label(365, 240, "⟦바로 가면 이만큼인데|it could be this short⟧", 11, "var(--good)")
         + label(380, 282, "⟦집에서 옆 창고에 가려고 성까지 갔다가 다시 나와요|to reach the shed next door, you go all the way to the castle and back out⟧", 12, "var(--muted)"))

# 2. 다들 성문 앞에 줄을 선다
QUEUE = "".join(person(60 + i * 62, 130, s=0.65, hat=c, shirt="#4A5A72", face=FROWN) for i, c in enumerate((None, "#E9B44C", "#5B8DEF", None, "var(--stone-dark)", "#E9B44C")))
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>' + QUEUE
         + gate(560, 80) + person(510, 60, s=0.6, face=EYES, **GUARD)
         + f'<g transform="translate(560,30)">{TINY_ICONS}</g>'
         + '<g transform="translate(690,80)"><circle r="26" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -16 V0 L12 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(690, 130, "⟦느려요|slow⟧", 13, "var(--bad)")
         + label(380, 255, "⟦검문소, 창고 문지기, 안내인이 전부 성문 한 곳에 몰려 있어요|the checkpoint, the shed broker and the escort are all crammed at one gate⟧", 12, "var(--muted)"))

# 3. SASE = 마을 곳곳에 역 (hero)
STATIONS = ((200, 110), (470, 70), (600, 210), (300, 240))
P3 = svg(340, sky(340)
         + road("M90 200 L200 150") + road("M130 60 L200 110") + road("M400 40 L470 40") + road("M560 40 L600 170") + road("M690 260 L600 250") + road("M240 300 L300 280")
         + road("M240 150 C300 150 340 120 430 100", "var(--accent)", 4, "6 6") + road("M500 110 C540 150 560 180 590 200", "var(--accent)", 4, "6 6")
         + road("M340 270 C400 260 500 250 560 240", "var(--accent)", 4, "6 6")
         + "".join(station(x, y, 0.8) for x, y in STATIONS)
         + house(80, 200, "⟦집|home⟧", s=0.7) + house(120, 30, "⟦카페|cafe⟧", "var(--good)", 0.6) + house(380, 20, "⟦지점|branch⟧", "#5B8DEF", 0.6)
         + shed(700, 240, "⟦창고|shed⟧", 0.7) + castle(560, 250, 0.2)
         + person(240, 200, s=0.5, **ME) + person(130, 90, s=0.45, **ME) + person(420, 70, s=0.45, **ME)
         + label(380, 325, "⟦어디서 출발하든 가장 가까운 역을 거쳐요|wherever you start, you go through the nearest hub⟧", 14, "var(--muted)"))

# 4. 역이 길도 골라준다
P4 = svg(280, sky(280) + station(150, 100, 1.0)
         + road("M200 150 C300 100 400 90 560 110", "var(--good)", 8) + label(380, 80, "⟦빠른 길|fast road⟧", 13, "var(--good)")
         + road("M200 160 C300 220 400 240 560 200", "var(--stone)", 8, "10 10") + label(380, 250, "⟦막힌 길|jammed road⟧", 13, "var(--muted)")
         + '<path d="M370 205 l20 20 M390 205 l-20 20" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + castle(560, 70, 0.3) + label(650, 60, "⟦성|castle⟧", 13, "var(--ink)", cls="d")
         + person(120, 180, s=0.5, face=SMILE, **GUARD, extra='<path d="M60 40 l30 -20" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/>')
         + label(150, 260, "⟦역이 골라요|the hub picks⟧", 12, "var(--muted)"))

# 5. 역은 보통 한 회사 것
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + "".join(station(x, 90, 0.7, full=False) + f'<rect x="{x - 30}" y="{90 + 12}" width="60" height="16" rx="4" fill="var(--accent)"/>' + label(x, 90 + 24, "⟦A 회사|Company A⟧", 10, "#FFF") for x in (120, 260, 400, 540, 680))
         + label(400, 190, "⟦역이 전부 한 회사 거예요|every hub belongs to one company⟧", 14, "var(--ink)", cls="d")
         + label(400, 220, "⟦다 갖춘 대신 갈아타기가 어려워요|all-in-one, but hard to switch⟧", 13, "var(--muted)")
         + label(400, 250, "⟦역이 멈추면 온 마을 길이 멈춰요|if the hubs stop, every road stops⟧", 13, "var(--bad)"))

SWG_I = icon('<path d="M8 30 L32 12 L56 30 Z" fill="var(--good)"/><rect x="14" y="30" width="36" height="24" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>')
CASB_I = icon('<path d="M8 30 L32 12 L56 30 Z" fill="var(--stone)"/><rect x="14" y="30" width="36" height="24" fill="var(--stone-dark)"/>')
ZTNA_I = icon('<rect x="24" y="14" width="16" height="30" rx="4" fill="#FFD166" stroke="var(--night)" stroke-width="2"/><rect x="30" y="6" width="4" height="8" fill="var(--night)"/><circle cx="32" cy="30" r="5" fill="var(--accent)"/>')
ROAD_I = icon('<path d="M8 44 C20 20 44 20 56 44" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M8 20 C20 44 44 44 56 20" stroke="var(--stone)" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="6 6"/>')

PAGE = {
    "slug": "sase", "order": 25,
    "title": ("마을 곳곳의 역", "Hubs All Over Town"),
    "h1": ("<em>SASE</em>가 뭐예요?", "What is <em>SASE</em>?"),
    "sub": ("보안 접근 서비스 엣지(Secure Access Service Edge)를 마을 곳곳에 세운 역 이야기로 풀어봤어요.",
            "Secure Access Service Edge, told as a story about hubs built all over town."),
    "panels": [
        {"svg": P1, "alt": ("집에서 옆 창고로 가는데 성문까지 크게 돌아갔다 다시 나오는 빨간 점선 길", "A red dotted road from home loops all the way to the castle gate and back out to the shed next door"),
         "caption": ("옛날엔 모든 길이 성문을 지났어요.", "Every road used to pass through the gate."),
         "small": ("집에서 옆 창고에 가려고 성까지 갔다가 다시 나와요. 멀고 느려요.", "To reach the shed next door, you went all the way to the castle and back. Long and slow.")},
        {"svg": P2, "alt": ("성문 앞에 찡그린 사람들이 줄을 섰고, 성문 위에 검문소·창고·등불 아이콘, 옆에 시계", "Frowning people queue at the gate; checkpoint, shed and lantern icons sit on the gate; a clock beside them"),
         "caption": ("다들 성문 앞에 줄을 서요.", "Everyone queues at the gate."),
         "small": ('<a href="swg-ko.html">검문소</a>, <a href="casb-ko.html">창고 문지기</a>, <a href="ztna-ko.html">안내인</a>이 전부 성문 한 곳에 몰려 있어요.',
                   'The <a href="swg-en.html">checkpoint</a>, the <a href="casb-en.html">shed broker</a> and the <a href="ztna-en.html">escort</a> are all crammed at one gate.')},
        {"svg": P3, "hero": True, "alt": ("집, 카페, 지점, 창고, 성이 흩어진 마을 지도에 역 네 개가 있고, 역마다 검문소·창고·등불 아이콘이 있으며 각자 가장 가까운 역으로 감", "A town map with home, cafe, branch, shed and castle scattered about; four hubs, each with checkpoint, shed and lantern icons; everyone heads to the nearest hub"),
         "caption": ("SASE는 마을 곳곳에 역을 두고, 역마다 다 갖춰요.", "SASE builds hubs all over town, fully equipped."),
         "small": ("어디서 출발하든 가장 가까운 역을 거쳐요. 역마다 검문소·창고 문지기·안내인이 있어요.", "Wherever you start, you pass the nearest hub — and every hub has a checkpoint, a shed broker and an escort."),
         "tricks": (4, [
             (SWG_I, ("검문소", "Checkpoint"), ("SWG", "SWG"), "calm"),
             (CASB_I, ("창고 문지기", "Shed broker"), ("CASB", "CASB")),
             (ZTNA_I, ("안내인", "Escort"), ("ZTNA", "ZTNA"), "warm"),
             (ROAD_I, ("길 고르기", "Road picking"), ("SD-WAN", "SD-WAN"), "calm"),
         ])},
        {"svg": P4, "alt": ("역에서 성으로 가는 두 길: 초록 빠른 길과 X 표시된 막힌 회색 길, 경비가 빠른 길을 가리킴", "Two roads from the hub to the castle: a green fast road and a crossed-out jammed grey one; a guard points to the fast one"),
         "caption": ("역이 제일 좋은 길도 골라줘요.", "The hub picks the best road, too."),
         "small": ("막힌 길은 피하고 빠른 길로. 그게 SD-WAN이에요. 보안 절반과 길 절반이 한 역에 있어요.", "Skip the jam, take the fast road — that's SD-WAN. Half security, half roads, in one hub.")},
        {"svg": P5, "alt": ("역 다섯 개에 전부 'A 회사' 이름표", "Five hubs, every one labeled Company A"),
         "caption": ("역은 보통 한 회사 거예요.", "The hubs usually belong to one company."),
         "small": ("다 갖춘 대신 갈아타기가 어려워요. 그리고 역이 멈추면 온 마을 길이 멈춰요.", "All-in-one, but hard to switch away from. And if the hubs stop, every road stops.")},
    ],
    "summary": (("<b>SASE</b> = 검문소·창고 문지기·안내인을 성문이 아니라 <b>마을 곳곳의 역</b>에 두고, 역이 <b>길까지</b> 골라주는 것.",
                 "<b>SASE</b> = put the checkpoint, the shed broker and the escort in <b>hubs all over town</b> instead of at the gate, and let the hub <b>pick the road</b> too."),
                ("Secure Access Service Edge. SSE(검문소 묶음) + SD-WAN(길 고르기) = SASE. 가트너가 2019년에 이름 붙였어요. Zscaler, Netskope, Palo Alto Prisma, Cato 같은 것들.",
                 "Secure Access Service Edge: SSE (the checkpoint bundle) + SD-WAN (road picking) = SASE. Named by Gartner in 2019. Zscaler, Netskope, Palo Alto Prisma, Cato.")),
    "glossary": [
        ("SSE", "SSE", ("검문소 묶음.", "The checkpoint bundle."), ('보안 절반. <a href="swg-ko.html">검문소</a> + <a href="casb-ko.html">창고 문지기</a> + <a href="ztna-ko.html">안내인</a>.', 'The security half: <a href="swg-en.html">checkpoint</a> + <a href="casb-en.html">shed broker</a> + <a href="ztna-en.html">escort</a>.')),
        ("SD-WAN", "SD-WAN", ("길 고르기.", "Road picking."), ("네트워크 절반. 막힌 길을 피해 빠른 길로.", "The network half: around the jam, onto the fast road.")),
        ("PoP · 엣지", "PoP · edge", ("역.", "The hub."), ("마을 곳곳에 세운 작은 성문. 가까운 데로 가요.", "Little gates built all over town. You use the nearest.")),
        ("헤어핀", "Hairpinning / backhaul", ("성까지 갔다 다시 나오기.", "To the castle and back out."), ("옆 창고 가는 데 성을 거치는 옛날 길. SASE 가 없애려는 것.", "The old detour through the castle to reach the shed next door. What SASE removes.")),
        ("지점", "Branch", ("작은 마을 사무소.", "The little office in town."), ("성 밖에서 일하는 사람들이 모인 곳. 역이 가까우면 빨라요.", "Where castle folk work outside the walls. Faster when a hub is near.")),
        ("단일 벤더 SASE", "Single-vendor SASE", ("한 회사 역.", "One company's hubs."), ("역 전부를 한 회사가 세워요. 편하지만 갈아타기 어려워요.", "All hubs built by one company. Convenient, hard to leave.")),
        ("통합 정책", "Unified policy", ("같은 규칙책.", "The same rulebook."), ("역이 몇 개든 규칙은 한 권. 집에서도 지점에서도 똑같이.", "However many hubs, one rulebook — the same at home and at the branch.")),
        ("지연", "Latency", ("멀리 돌면 느려요.", "The long way is slow."), ("역이 가까울수록 빨라요. 그래서 역을 많이 세워요.", "The nearer the hub, the faster. Which is why there are so many.")),
    ],
}
