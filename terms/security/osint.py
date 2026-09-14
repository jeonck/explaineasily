from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
MAID = dict(hat=None, shirt="#7B3FA0")
COOK = dict(hat="#FFF", shirt="#FFF")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
SPYGLASS = '<g transform="translate(56,52) rotate(-35)"><rect x="-4" y="0" width="8" height="30" rx="3" fill="#5A3B22"/><rect x="-6" y="-8" width="12" height="10" rx="2" fill="#C9A86A"/></g>'
GOLD = "#E9B44C"


def board(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="24" rx="6" fill="#C9A86A"/>' + label(w / 2, 17, title, 11, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(12, 44 + i * 18, r, 10, "#142033", "start")
    return out + "</g>"


def sign(x, y, text, s=1.0, color=WOOD):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-3" y="0" width="6" height="46" fill="#5A3B22"/>'
            f'<rect x="-46" y="-30" width="92" height="34" rx="4" fill="{color}"/>' + label(0, -8, text, 11, "#FFF8E7", cls="d") + "</g>")


def scrap(x, y, text, s=1.0, rot=0, c="#142033"):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-52" y="-22" width="104" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(0, 4, text, 10, c) + "</g>")


def maptbl(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="200" height="150" rx="6" fill="#FDF3D9" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M20 120 L60 120 L60 70 L110 70 L110 40 L170 40" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="7 5"/>'
            f'<rect x="70" y="80" width="70" height="50" fill="none" stroke="var(--stone-dark)" stroke-width="2"/>'
            f'<path d="M95 80 v-14 a10 10 0 0 1 20 0 v14" stroke="var(--stone-dark)" stroke-width="2" fill="none"/>'
            f'<circle cx="20" cy="120" r="5" fill="var(--bad)"/><circle cx="170" cy="40" r="5" fill="var(--accent)"/>'
            + label(100, 20, "⟦성 지도 (도둑이 그린)|CASTLE MAP (drawn by the thief)⟧", 10, "#142033", cls="d") + "</g>")


# 1. 도둑은 담을 넘기 전에 소문부터 모아요
P1 = svg(300, sky(300)
         + person(90, 90, s=1.0, face=MASK, extra=SPYGLASS)
         + label(120, 240, "⟦도둑은 아직 담 근처에도 안 가요|the thief hasn\'t even neared the wall⟧", 11, "var(--muted)")
         + small_castle(560, 60, 0.9)
         + "".join(f'<circle cx="{cx}" cy="{cy}" r="16" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>' + label(cx, cy + 5, t, 14, "var(--muted)", cls="d") for cx, cy, t in ((300, 70, "?"), (400, 50, "?"), (480, 90, "?")))
         + label(380, 290, "⟦담을 넘기 전에, 마을 소문부터 모아요|before climbing the wall, gather the village gossip⟧", 12, "var(--ink)", cls="d"))

# 2. 소문 조각들 (문제: 다 공개돼 있어요)
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + sign(130, 40, "⟦장터 방|MARKET STALL⟧") + scrap(130, 130, "⟦구인: 자물쇠공 구함|hiring: locksmith⟧", rot=-4) + label(130, 200, "⟦우리 성이 어떤 자물쇠를 쓰는지|which locks our castle uses⟧", 9, "var(--muted)")
         + sign(340, 40, "⟦마을 게시판|VILLAGE BOARD⟧") + scrap(340, 130, "⟦요리사: 화요일 쉼!|cook: off Tuesdays!⟧", rot=3, c="var(--bad)") + label(340, 200, "⟦성 사람들이 스스로 적어요|castle folk post it themselves⟧", 9, "var(--muted)")
         + sign(540, 40, "⟦성문 이름표|GATE NAMEPLATE⟧") + scrap(540, 130, "⟦서문 · 북탑 · 창고|west gate · north tower⟧", rot=-2) + label(540, 200, "⟦문마다 이름이 붙어 있어요|every door wears a name⟧", 9, "var(--muted)")
         + scrap(670, 250, "⟦옛 신문: 유출 명부|old paper: leaked list⟧", 0.8, rot=6, c="var(--bad)")
         + label(380, 300, "⟦아무도 안 훔쳤어요 — 다 밖에 나와 있는 것들이에요|nothing was stolen — it\'s all out in the open⟧", 12, "var(--ink)", cls="d"))

# 3. OSINT = 소문만 모아도 성 지도가 나와요 (hero)
P3 = svg(360, sky(360)
         + person(80, 100, s=1.0, face=MASK, extra=SPYGLASS)
         + "".join(f'<path d="M150 150 Q250 {py} 340 {py}" stroke="var(--muted)" stroke-width="2" fill="none" stroke-dasharray="6 4"/>' for py in (70, 120, 170, 220))
         + maptbl(360, 60, 1.0)
         + label(380, 250, "⟦조각을 다 합치면 성 지도와 사람 명단이 나와요|piece it together and out comes the castle map and a name list⟧", 12, "var(--ink)", cls="d")
         + label(380, 300, "⟦OSINT은 마을 소문만 모아도 성 지도가 나오는 거예요|OSINT: gather only the open gossip, and the castle map appears⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦훔치지 않아요 — 밖에 나온 것만 주워 맞춰요|nothing stolen — just open pieces, fitted together⟧", 11, "var(--muted)"),
         )

# 4. 우리도 같은 눈으로 먼저 봐요
P4 = svg(320, sky(320)
         + person(90, 70, s=0.85, face=EYES, extra=SPYGLASS, **BLUE)
         + label(120, 200, "⟦파란 모자도 스파이글라스를 들어요|the blue hat picks up the same spyglass⟧", 11, "var(--muted)")
         + "".join(f'<path d="M170 120 Q250 {py} 320 {py}" stroke="var(--good)" stroke-width="2" fill="none" stroke-dasharray="6 4"/>' for py in (70, 130, 190))
         + scrap(400, 70, "⟦구인 공고 내려요|pull the job post⟧", c="var(--good)") + scrap(400, 140, "⟦필요 없는 이름표 떼요|remove stray nameplates⟧", c="var(--good)")
         + person(600, 60, s=0.6, face=SMILE, **COOK) + bubble(490, 190, 250, 34, "⟦광장에선 성 얘기 조심해요|careful with castle talk in the square⟧", 10, "var(--panel)", "var(--line)", "left")
         + label(620, 150, "⟦성 사람 수업|castle-folk class⟧", 10, "var(--muted)")
         + label(380, 300, "⟦도둑이 보기 전에, 우리가 먼저 우리 소문을 봐요|before the thief looks, we look at our own gossip first⟧", 12, "var(--ink)", cls="d"))

# 5. 정찰은 첫 걸음 — 다음 걸음 전에 지워요
P5 = svg(300, sky(300)
         + '<path d="M60 210 L700 210" stroke="var(--stone-dark)" stroke-width="3"/>'
         + "".join(f'<circle cx="{80 + i * 150}" cy="210" r="10" fill="{c}"/>' + label(80 + i * 150, 245, t, 11, "var(--ink)", cls="d") for i, (c, t) in enumerate((("var(--accent)", "⟦1. 정찰|1. recon⟧"), ("var(--bad)", "⟦2. 편지|2. letter⟧"), ("var(--bad)", "⟦3. 담 넘기|3. climb⟧"), ("var(--bad)", "⟦4. 금고|4. vault⟧"))))
         + person(80, 100, s=0.7, face=MASK, extra=SPYGLASS) + label(80, 62, "⟦지금 여기|here, now⟧", 10, "var(--accent)")
         + bubble(300, 40, 380, 44, "⟦여기서 막으면, 다음 걸음이 시작도 못 해요|stop it here, and the next steps never begin⟧", 12, "var(--panel)", "var(--good)", "bottom")
         + label(380, 288, "⟦정찰은 도둑의 첫 걸음이에요 — 우리 발자국을 줄이면 지도가 흐려져요|recon is the thief\'s first step — shrink our footprints and the map goes blurry⟧", 11, "var(--muted)"))

RECON_I = icon(f'<circle cx="26" cy="26" r="14" fill="none" stroke="var(--stone-dark)" stroke-width="4"/><rect x="36" y="36" width="16" height="6" rx="3" fill="var(--stone-dark)" transform="rotate(45 40 40)"/><circle cx="26" cy="26" r="6" fill="var(--bad)"/>')
POST_I = icon(f'<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 30 h24 M20 38 h16" stroke="#C9A86A" stroke-width="2"/><circle cx="46" cy="14" r="7" fill="var(--bad)"/>')
LEAK_I = icon('<rect x="10" y="14" width="44" height="12" rx="3" fill="var(--bad)"/><path d="M18 26 v10 M32 26 v18 M46 26 v10" stroke="#5B9BD5" stroke-width="3" stroke-linecap="round"/><ellipse cx="32" cy="50" rx="10" ry="6" fill="#5B9BD5"/>')
BLUR_I = icon(f'<circle cx="24" cy="24" r="10" fill="{SKIN}"/><path d="M12 20 Q24 6 36 20 Z" fill="var(--good)"/><path d="M42 30 q10 8 4 20 M48 26 q12 10 4 24" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="3 3"/>')

PAGE = {
    "slug": "osint", "order": 111,
    "title": ("마을 소문만 모아도 성 지도가 나와요", "Gather the Gossip, Draw the Castle"),
    "h1": ("<em>OSINT</em>가 뭐예요?", "What is <em>OSINT</em>?"),
    "sub": ("OSINT(공개 정보 수집)를, 담을 넘기 전에 마을 소문부터 모아 성 지도를 그리는 도둑 이야기로 풀어봤어요.",
            "OSINT (open-source intelligence), told as a story about a thief who gathers village gossip to draw a map of the castle before ever climbing the wall."),
    "panels": [
        {"svg": P1, "alt": ("스파이글라스를 든 마스크 쓴 도둑이 멀찍이서 작은 성을 보고, 성 위엔 물음표 세 개가 떠 있음. 도둑은 아직 담 근처에도 안 감", "A masked thief with a spyglass watches a small castle from far off, three question marks floating above it. He hasn\'t even neared the wall"),
         "caption": ("도둑은 담을 넘기 전에 소문부터 모아요.", "Before climbing the wall, the thief gathers gossip first."),
         "small": ("좋은 도둑은 서두르지 않아요. 담을 넘기 전에, 성에 대해 마을이 아는 걸 먼저 다 주워 모아요.", "A good thief doesn\'t rush. Before the wall, he first collects everything the village already knows about the castle.")},
        {"svg": P2, "alt": ("장터의 자물쇠공 구인 공고, 마을 게시판의 '요리사 화요일 쉼', 성문 이름표(서문·북탑·창고), 유출 명부가 실린 옛 신문. 다 밖에 나와 있음", "A locksmith job post at the market, a cook off Tuesdays note on the village board, gate nameplates (west gate, north tower), and an old paper with a leaked list. All of it out in the open"),
         "caption": ("조각은 다 공개돼 있어요. 아무도 안 훔쳤어요.", "The pieces are all public. Nothing was stolen."),
         "small": ('구인 공고는 우리가 어떤 <a href="password-ko.html">자물쇠</a>를 쓰는지 알려주고, 성 사람들의 게시판 글은 누가 언제 없는지 알려줘요. 성문 이름표는 <a href="dns-ko.html">안내소</a>·<a href="asm-ko.html">문 세기</a>의 단서고, 옛 신문의 유출 명부는 <a href="bruteforce-ko.html">암호말</a>의 단서예요.',
                   'A job post reveals which <a href="password-en.html">locks</a> we use; castle folk\'s board posts reveal who is away and when. Gate nameplates feed the <a href="dns-en.html">directory</a> and <a href="asm-en.html">door-counting</a>; a leaked list in an old paper feeds <a href="bruteforce-en.html">password</a> guessing.')},
        {"svg": P3, "hero": True, "alt": ("스파이글라스를 든 도둑에게서 점선 넷이 뻗어 나가 오른쪽의 성 지도 종이(도둑이 그린 — 길·건물·왕관 표시)로 모임", "Four dotted lines run from the thief with the spyglass to a map paper on the right — drawn by the thief — with a path, a building, and a crown mark"),
         "caption": ("OSINT은 마을 소문만 모아도 성 지도가 나오는 거예요.", "OSINT: gather only the open gossip, and the castle map appears."),
         "small": ("훔친 건 하나도 없어요. 장터·게시판·이름표·옛 신문 조각을 다 합치면 성 지도와 사람 명단이 나와요. 그게 다음 공격의 밑그림이 돼요.",
                   "Not one thing was stolen. Fit the market, the board, the nameplates, and the old paper together, and out comes the castle map and a name list. That becomes the sketch for the next attack."),
         "tricks": (4, [
             (RECON_I, ("멀리서 보기", "Watching from afar"), ("담은 아직 안 넘어요", "no wall climbed yet"), "warm"),
             (POST_I, ("우리가 적은 것", "What we posted"), ("구인·SNS·이름표", "job posts, social, nameplates"), "warm"),
             (LEAK_I, ("옛 유출 명부", "Old leaked lists"), ("암호말 힌트가 돼요", "hints for the password")),
             (BLUR_I, ("합치면 지도", "Fitted into a map"), ("조각 하나하나는 사소해요", "each piece looks harmless"), "calm"),
         ])},
        {"svg": P4, "alt": ("파란 모자가 같은 스파이글라스를 들고 우리 성을 보며 구인 공고를 내리고 이름표를 떼는 동안, 요리사에게 '광장에선 성 얘기 조심해요' 말풍선", "A blue hat uses the same spyglass on our own castle, pulling a job post and removing a nameplate, while telling the cook: careful with castle talk in the square"),
         "caption": ("도둑이 보기 전에, 우리가 먼저 우리 소문을 봐요.", "Before the thief looks, we look at our own gossip first."),
         "small": ('파란 모자가 도둑과 같은 눈으로 우리 성을 봐요 — <a href="asm-ko.html">밖에서 문을 세고</a>, <a href="redteam-ko.html">정찰</a>처럼 소문을 모아요. 필요 없는 이름표는 떼고, 성 사람에겐 <a href="awareness-ko.html">광장에서 성 얘기 조심</a>을 가르쳐요.',
                   'The blue hat looks at our castle with the thief\'s eyes — <a href="asm-en.html">counting doors from outside</a> and gathering gossip like a <a href="redteam-en.html">scout</a>. Pull the stray nameplates, and teach the folk to <a href="awareness-en.html">watch castle talk in the square</a>.')},
        {"svg": P5, "alt": ("도둑의 길 네 걸음: 정찰 → 편지 → 담 넘기 → 금고. 도둑은 아직 첫 걸음(정찰)에 있고, '여기서 막으면 다음 걸음이 시작도 못 해요' 말풍선", "The thief\'s four-step path: recon → letter → climb → vault. The thief is still on step one (recon); a bubble reads stop it here and the next steps never begin"),
         "caption": ("정찰은 도둑의 첫 걸음이에요.", "Recon is the thief\'s very first step."),
         "small": ('OSINT은 <a href="killchain-ko.html">도둑의 일곱 걸음</a> 중 첫 걸음, 정찰이에요. 여기서 우리 발자국(<a href="asm-ko.html">공격 표면</a>)을 줄이면 도둑의 지도가 흐려져요.',
                   'OSINT is the first of the <a href="killchain-en.html">thief\'s steps</a>: reconnaissance. Shrink our footprints (the <a href="asm-en.html">attack surface</a>) here, and the thief\'s map goes blurry.')},
    ],
    "summary": (("<b>OSINT</b> = 도둑이 담을 넘기 전에 <b>공개된 마을 소문</b>(구인 공고·SNS 글·성문 이름표·옛 유출 명부)만 모아 <b>성 지도와 사람 명단</b>을 그리는 것. 훔치지 않고, <b>밖에 나온 조각</b>만 맞춰요.",
                 "<b>OSINT</b> = before climbing the wall, a thief gathers only the <b>open gossip</b> — job posts, social media, gate nameplates, old leaked lists — to draw <b>the castle map and a name list</b>. Nothing is stolen; only <b>open pieces</b> are fitted together."),
                ("Open-Source Intelligence. 누구나 볼 수 있는 공개 정보(웹사이트, 구인 공고, SNS, DNS 기록, 유출 데이터, 다크웹)를 모아 표적을 파악하는 정찰 활동이에요. 킬 체인의 첫 단계라, 방어자도 같은 방법으로 자기 조직의 공격 표면을 먼저 점검해요.",
                 "Gathering publicly available information — websites, job posts, social media, DNS records, breach data, the dark web — to profile a target. It\'s the first stage of the kill chain, so defenders use the same methods to audit their own attack surface first.")),
    "glossary": [
        ("OSINT", "OSINT", ("소문만 모아도 지도.", "Gossip alone makes a map."), ("공개된 정보만 모아 표적을 파악해요. 훔치는 게 아니라 밖에 나온 걸 줍는 거예요.", "Profiling a target from public information only. Not stealing — collecting what\'s already out in the open.")),
        ("정찰", "Reconnaissance", ("도둑의 첫 걸음.", "The thief\'s first step."), ('공격 전에 표적을 살피는 단계. → <a href="killchain-ko.html">도둑의 일곱 걸음</a>의 1단계', 'The stage of sizing up a target before attacking. → step 1 of the <a href="killchain-en.html">thief\'s steps</a>')),
        ("풋프린팅", "Footprinting", ("성문 이름표 모으기.", "Collecting nameplates."), ('조직의 도메인·IP·직원 목록을 그러모으는 것. → <a href="dns-ko.html">마을 안내소</a>', 'Gathering an org\'s domains, IPs, and staff list. → <a href="dns-en.html">the village directory</a>')),
        ("소셜 미디어 노출", "Social media exposure", ("성 사람이 스스로 적은 글.", "What the folk post themselves."), ('누가 언제 없는지, 무슨 도구를 쓰는지 스스로 알려줘요. → <a href="awareness-ko.html">도둑 수업</a>', 'People reveal who is away and what tools they use, all by themselves. → <a href="awareness-en.html">the thief class</a>')),
        ("유출 데이터 검색", "Breach data search", ("옛 신문 속 명부.", "The list in the old paper."), ('예전에 새어 나온 명부에서 암호말을 찾아요. → <a href="bruteforce-ko.html">열쇠 천 개를 꽂아보는 도둑</a>', 'Finding passwords in lists that leaked long ago. → <a href="bruteforce-en.html">the thief who tries a thousand keys</a>')),
        ("다크웹 모니터링", "Dark web monitoring", ("뒷골목 소문 듣기.", "Listening in the back alleys."), ('우리 명부가 뒷골목에서 팔리는지 지켜봐요. → <a href="cti-ko.html">망루 위의 친구</a>', 'Watching whether our lists are being sold in the back alleys. → <a href="cti-en.html">the friend on the watchtower</a>')),
        ("디지털 발자국 줄이기", "Reducing digital footprint", ("이름표 떼기.", "Removing nameplates."), ("필요 없는 공개 정보를 지워 도둑의 지도를 흐리게 만들어요.", "Removing needless public information so the thief\'s map goes blurry.")),
        ("공격 표면", "Attack surface", ("밖에서 보이는 우리 문.", "Our doors, seen from outside."), ('도둑이 노릴 수 있는 모든 창구. → <a href="asm-ko.html">바깥에서 세는 우리 성의 문</a>', 'Every point a thief could aim at. → <a href="asm-en.html">counting our castle\'s doors from outside</a>')),
    ],
}
