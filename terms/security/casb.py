from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
SHEDS = ("⟦사진 창고|Photo Shed⟧", "⟦편지 창고|Mail Shed⟧", "⟦회의 창고|Meeting Shed⟧")


def shed(x, y, name, s=1.0, dashed=False, mark=""):
    stroke = ' stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"' if dashed else ""
    fill = "var(--panel)" if dashed else "var(--stone-dark)"
    roof = "var(--stone)" if not dashed else "var(--panel)"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="60" fill="{fill}"{stroke}/>'
            f'<path d="M-48 0 L0 -34 L48 0 Z" fill="{roof}"{stroke}/><rect x="-10" y="26" width="20" height="34" fill="{"var(--line)" if dashed else "var(--night)"}"/>'
            f'{label(0, 80, name, 12, "var(--muted)")}{mark}</g>')


def road(pts, color="var(--stone-dark)", dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{pts}" stroke="{color}" stroke-width="10" fill="none" stroke-linecap="round"{d}/>'


def paper(x, y, s=1.0, stamp=True):
    st = ('<g transform="translate(66,26) rotate(-18)"><circle r="16" fill="none" stroke="var(--bad)" stroke-width="3"/>' + label(0, 4, "⟦비밀|SECRET⟧", 8, "var(--bad)") + "</g>") if stamp else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="90" height="110" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            + "".join(f'<rect x="12" y="{34 + i * 12}" width="{56 - (i * 13) % 24}" height="4" rx="2" fill="var(--line)"/>' for i in range(5)) + st + "</g>")


BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
LIST = ('<g transform="translate(60,60)"><rect width="46" height="56" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/>'
        + "".join(f'<path d="M6 {12 + i * 12} l4 4 l8 -8" stroke="var(--good)" stroke-width="2" fill="none"/><rect x="22" y="{11 + i * 12}" width="18" height="3" fill="#C9A86A"/>' for i in range(4)) + "</g>")
SHED_ROW = lambda y, s=0.8: "".join(shed(500 + i * 100, y, n, s) for i, n in enumerate(SHEDS))

# 1. 요즘은 물건을 성 밖 창고에 둔다
P1 = svg(300, sky(300) + castle(20, 80, 0.5) + '<path d="M60 40 L60 60" stroke="none"/>'
         + road("M250 220 C350 220 400 200 480 200")
         + SHED_ROW(150)
         + person(300, 120, s=0.7, **ME, extra=BAG) + person(400, 110, s=0.7, hat="#E9B44C", shirt="#4A5A72", face=SMILE, extra=BAG)
         + label(120, 40, "⟦성|the castle⟧", 14, "var(--ink)", cls="d") + label(630, 40, "⟦성 밖 창고들|sheds outside⟧", 14, "var(--ink)", cls="d")
         + label(380, 280, "⟦성벽 밖이라 성 경비는 못 봐요|outside the walls, the castle guards can\'t see⟧", 13, "var(--muted)"))

# 2. 아무도 모르는 창고
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + battlements(0, 30, 240, 4, "var(--stone)", 20) + '<rect y="50" width="240" height="230" fill="var(--stone-dark)"/>'
         + person(80, 60, s=0.7, face=EYES + '<path d="M8 28 l-14 -6" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/>', **GUARD)
         + label(110, 170, "?", 34, "var(--accent)", cls="d") + label(110, 200, "⟦성 경비: 몰라요|castle guard: no idea⟧", 12, "#C9D5E6")
         + road("M240 200 C330 200 380 180 440 180", dash="14 10")
         + person(330, 100, s=0.8, **ME, extra='<g transform="translate(46,60)">' + paper(0, 0, 0.45) + "</g>")
         + bubble(300, 20, 200, 34, "⟦공짜 창고가 편해서요|the free shed is just easier⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + shed(560, 110, "⟦공짜 창고|Free Shed⟧", 1.1, dashed=True) + label(560, 230, "⟦누구 건지도 몰라요|nobody knows whose it is⟧", 12, "var(--bad)"))

# 3. CASB = 성과 창고 사이의 문지기 (hero)
P3 = svg(340, sky(340) + castle(10, 120, 0.42)
         + road("M210 230 C280 230 300 220 340 220 M420 220 C460 220 470 210 500 210")
         + gatehouse(380, 130) + person(425, 120, s=0.7, face=EYES, **GUARD, extra='<g transform="translate(-58,60)">' + LIST[len('<g transform="translate(60,60)">'):])
         + label(380, 250, "⟦문지기|the broker⟧", 13, "var(--ink)", cls="d")
         + SHED_ROW(150)
         + person(200, 150, s=0.7, **ME, extra=BAG)
         + '<path d="M260 200 L320 200" stroke="var(--accent)" stroke-width="3"/><path d="M312 192 L324 200 L312 208" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(380, 320, "⟦누가, 어느 창고에, 뭘 들고 가는지|who goes to which shed, carrying what⟧", 14, "var(--muted)"))

# 4. 낯선 창고는 막고, 아는 창고엔 규칙
X_MARK = '<path d="M-22 -22 l44 44 M22 -22 l-44 44" stroke="var(--bad)" stroke-width="7" stroke-linecap="round" transform="translate(0,30)"/>'
RULE = ('<g transform="translate(-60,-90)"><rect width="120" height="44" rx="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
        + label(60, 18, "⟦창고 규칙|shed rules⟧", 11, "var(--accent)") + label(60, 34, "⟦밖에 공유 금지|no sharing outside⟧", 11, "var(--ink)") + "</g>")
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + shed(190, 130, "⟦공짜 창고|Free Shed⟧", 1.2, dashed=True, mark=X_MARK)
         + label(190, 290, "⟦낯선 창고는 막아요|unknown sheds are blocked⟧", 13, "var(--bad)")
         + shed(570, 160, "⟦사진 창고|Photo Shed⟧", 1.2, mark=RULE)
         + person(440, 150, s=0.7, face=EYES, **GUARD) + '<g transform="translate(486,220)">' + paper(0, 0, 0.4) + "</g>"
         + '<path d="M480 210 l40 40 M520 210 l-40 40" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(570, 300, "⟦아는 창고엔 규칙을 붙여요|known sheds get the castle\'s rules⟧", 13, "var(--good)"))

# 5. 문지기 길을 안 지나면 못 본다
HOUSE = ('<g transform="translate(90,150)"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
         '<path d="M-50 0 L0 -36 L50 0 Z" fill="var(--bad)"/><rect x="-10" y="26" width="20" height="34" fill="#8B5E3C"/>' + label(0, 80, "⟦집|home⟧", 12, "var(--muted)") + "</g>")
HANDSHAKE = ('<g transform="translate(0,-90)"><rect x="-56" y="-22" width="112" height="44" rx="8" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/>'
             + label(0, -2, "⟦창고 주인과 약속|a deal with the owner⟧", 10, "var(--good)") + label(0, 14, "⟦안을 직접 봐요|look inside directly⟧", 10, "var(--ink)") + "</g>")
P5 = svg(300, sky(300) + HOUSE
         + road("M130 240 C250 250 350 270 500 240", "var(--bad)", "14 10")
         + person(300, 150, s=0.7, **ME, extra=BAG)
         + gatehouse(400, 60, 0.7) + person(330, 45, s=0.55, face=FROWN, **GUARD) + label(400, 150, "?", 26, "var(--accent)", cls="d")
         + shed(600, 130, "⟦사진 창고|Photo Shed⟧", 1.1, mark=HANDSHAKE)
         + label(300, 285, "⟦집에서 바로 창고로 가면 문지기는 몰라요|straight from home to the shed, the broker never sees it⟧", 13, "var(--muted)"))

LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="#C9A86A"/><rect x="22" y="30" width="16" height="3" fill="#C9A86A"/><rect x="22" y="40" width="18" height="3" fill="#C9A86A"/>')
CHECK_I = icon('<path d="M8 30 L32 12 L56 30 Z" fill="var(--stone)"/><rect x="14" y="30" width="36" height="24" fill="var(--stone-dark)"/><path d="M22 44 l6 6 l14 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
BAG_I = icon('<rect x="14" y="26" width="36" height="28" rx="4" fill="var(--night)"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" stroke="var(--night)" stroke-width="3" fill="none"/><circle cx="44" cy="22" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/>')
RULE_I = icon('<rect x="10" y="14" width="44" height="36" rx="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><rect x="18" y="24" width="28" height="3" fill="var(--accent)"/><rect x="18" y="32" width="20" height="3" fill="var(--accent)"/>')

PAGE = {
    "slug": "casb", "order": 22,
    "title": ("바깥 창고 문지기", "The Broker for the Sheds Outside"),
    "h1": ("<em>CASB</em>가 뭐예요?", "What is a <em>CASB</em>?"),
    "sub": ("클라우드 접근 보안 중개자(Cloud Access Security Broker)를 성 밖 창고로 가는 길의 문지기 이야기로 풀어봤어요.",
            "Cloud Access Security Broker, told as a story about the gatekeeper on the road to the sheds outside."),
    "panels": [
        {"svg": P1, "alt": ("성에서 길을 따라 사진 창고, 편지 창고, 회의 창고로 가방을 들고 가는 사람들", "People carrying bags from the castle along a road to the Photo, Mail and Meeting sheds"),
         "caption": ("요즘은 물건을 성 밖 창고에 둬요.", "These days things are kept in sheds outside."),
         "small": ("사진은 사진 창고에, 편지는 편지 창고에. 성벽 밖이라 성 경비는 못 봐요.", "Photos in the photo shed, mail in the mail shed. Outside the walls, the castle guards can't see them.")},
        {"svg": P2, "alt": ("성벽 위 경비는 반대쪽을 보고, 한 사람이 비밀 종이를 들고 점선으로 그려진 '공짜 창고'로 감", "The wall guard looks the other way while someone carries a secret paper to a dashed-outline Free Shed"),
         "caption": ("아무도 모르는 창고가 생겨요.", "Sheds nobody knows about appear."),
         "small": ('"공짜 창고가 편해서요." <a href="dlp-ko.html">빨간 도장 종이</a>가 어디 있는지 성은 몰라요.',
                   '"The free shed is just easier." The castle has no idea where the <a href="dlp-en.html">red-stamped papers</a> went.')},
        {"svg": P3, "hero": True, "alt": ("성과 창고들 사이의 길 한가운데 문지기 집이 있고, 경비가 창고 목록을 들고 가방 든 사람을 살핌", "A gatehouse in the middle of the road between the castle and the sheds; a guard with a list checks a person carrying a bag"),
         "caption": ("CASB는 성과 창고 사이의 문지기예요.", "A CASB is the gatekeeper between the castle and the sheds."),
         "small": ("성에서 창고로 가는 길 한가운데 서서, 누가 어느 창고에 뭘 들고 가는지 봐요.", "It stands in the middle of the road and sees who goes to which shed, carrying what."),
         "tricks": (4, [
             (LIST_I, ("창고 목록", "The shed list"), ("어떤 창고를 쓰고 있나", "which sheds are in use"), "warm"),
             (CHECK_I, ("허락된 창고", "Approved sheds"), ("아는 창고만 통과", "only known sheds pass"), "calm"),
             (BAG_I, ("가방 검사", "Bag check"), ("비밀 종이가 들었나", "any secret papers inside")),
             (RULE_I, ("창고 안 규칙", "Rules in the shed"), ("성의 규칙을 창고에도", "the castle's rules, out there too"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: X 표시된 공짜 창고. 오른쪽: '밖에 공유 금지' 규칙이 붙은 사진 창고와, 비밀 종이를 막는 경비", "Left: the Free Shed crossed out. Right: the Photo Shed with a 'no sharing outside' rule, and a guard stopping a secret paper"),
         "caption": ("낯선 창고는 막고, 아는 창고엔 규칙을 붙여요.", "Unknown sheds are blocked; known sheds get rules."),
         "small": ('"비밀 종이는 창고에 못 둬요." "창고 문을 온 동네에 열어두지 마세요."', '"No secret papers in the shed." "Don\'t leave the shed door open to the whole town."')},
        {"svg": P5, "alt": ("집에서 문지기 집을 거치지 않는 다른 길로 바로 창고에 가는 사람, 문지기는 물음표. 창고엔 '창고 주인과 약속' 표시", "Someone goes straight from home to the shed by a road that skips the gatehouse; the guard shows a question mark. The shed carries a 'deal with the owner' sign"),
         "caption": ("문지기 길을 안 지나면 못 봐요.", "Skip the gatehouse road, and it sees nothing."),
         "small": ("집에서 바로 창고로 가면요? 그래서 창고 주인과 직접 약속(API)을 맺어 창고 안을 들여다보기도 해요.", "Straight from home to the shed? So the broker also makes a deal with the shed's owner (an API) to look inside directly.")},
    ],
    "summary": (("<b>CASB</b> = 성과 바깥 창고 <b>사이에 선</b> 문지기. 누가 어느 창고에 뭘 들고 가는지 보고, 낯선 창고는 막고, 아는 창고엔 <b>성의 규칙</b>을 붙여요.",
                 "A <b>CASB</b> = the gatekeeper <b>between</b> the castle and the sheds outside. It sees who carries what where, blocks unknown sheds, and puts the <b>castle's rules</b> on known ones."),
                ("Cloud Access Security Broker. 가트너가 2012년에 붙인 이름이에요. 요즘은 SSE/SASE라는 묶음 안에 들어가 있어요. Netskope, Zscaler, Microsoft Defender for Cloud Apps 같은 것들.",
                 "Cloud Access Security Broker, a name Gartner coined in 2012. Today it usually ships inside an SSE/SASE bundle — Netskope, Zscaler, Microsoft Defender for Cloud Apps.")),
    "glossary": [
        ("클라우드 앱", "SaaS / cloud app", ("바깥 창고.", "A shed outside."), ("Google Drive, Slack, Dropbox처럼 성 밖에 있는 창고.", "Google Drive, Slack, Dropbox — storehouses outside the walls.")),
        ("섀도 IT", "Shadow IT", ("아무도 모르는 창고.", "The shed nobody knows about."), ("직원이 편해서 몰래 쓰는 공짜 창고.", "The free shed employees quietly use because it's easier.")),
        ("허가 앱", "Sanctioned app", ("허락된 창고 목록.", "The approved shed list."), ("성이 알고 규칙을 붙인 창고. 나머지는 막거나 지켜봐요.", "Sheds the castle knows and has rules for. The rest are blocked or watched.")),
        ("프록시 모드", "Inline / proxy mode", ("길 한가운데 문지기.", "The gatekeeper on the road."), ("모든 길이 문지기를 지나게 해요. 지나가는 순간 막을 수 있어요.", "Every trip passes the gatehouse, so it can stop things in the moment.")),
        ("API 모드", "API mode", ("창고 주인과의 약속.", "The deal with the shed owner."), ("길을 안 지나도 창고 안을 봐요. 대신 이미 들어간 뒤에 알아요.", "Sees inside the shed without the road — but only after things are already in.")),
        ("클라우드 DLP", "Cloud DLP", ("창고 가는 가방 검사.", "Bag check on the way to the shed."), ('<a href="dlp-ko.html">빨간 도장 종이</a>를 창고 길에서도 살펴요.', 'The <a href="dlp-en.html">red-stamped paper</a> check, applied on the shed road.')),
        ("공유 설정 오류", "Sharing misconfiguration", ("창고 문을 온 동네에 열어둠.", "The shed door left open to the whole town."), ('"링크 있는 사람 누구나" 같은 것. 문지기가 제일 자주 잡는 실수.', '"Anyone with the link." The mistake the broker catches most.')),
        ("SSE · SASE", "SSE · SASE", ("문지기 묶음.", "The gatekeeper bundle."), ('창고 문지기, <a href="ndr-ko.html">복도 파수꾼</a>, <a href="zerotrust-ko.html">문마다 묻는 성</a>을 한 묶음으로 파는 요즘 이름.', 'The modern name for selling the shed broker, the <a href="ndr-en.html">hallway watcher</a> and the <a href="zerotrust-en.html">castle that always asks</a> as one bundle.')),
    ],
}
