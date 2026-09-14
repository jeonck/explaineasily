from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
CARPENTER = dict(hat="#E9B44C", shirt="#4A5A72")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)


def toolbox(x, y, s=1.0, open_=False, bug=False):
    lid = (f'<path d="M-34 -14 h68 v-6 h-68z" fill="#5A3B22" transform="rotate(-40 -34 -14)"/>' if open_ else f'<rect x="-34" y="-20" width="68" height="8" rx="2" fill="#5A3B22"/>')
    handle = '<path d="M-10 -20 v-8 h20 v8" stroke="#5A3B22" stroke-width="4" fill="none"/>'
    tools = '<rect x="-24" y="-8" width="6" height="22" fill="var(--stone)"/><rect x="-12" y="-8" width="6" height="22" fill="#C9822B"/><path d="M4 -8 l6 6 l6 -6 v22 h-12z" fill="var(--stone)"/>'
    b = ('<g transform="translate(20,0)"><ellipse rx="9" ry="6" fill="var(--bad)"/><circle cx="-8" cy="-2" r="4" fill="var(--bad)"/><path d="M-4 -6 v-3 M-1 -5 v-3 M4 -6 v-3" stroke="var(--night)" stroke-width="1.5"/></g>' if bug else "")
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-34" y="-14" width="68" height="36" rx="3" fill="#8B5E3C"/>{tools}{b}{lid}{handle}</g>'


def bug(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="14" ry="9" fill="var(--bad)"/><circle cx="-13" cy="-3" r="6" fill="var(--bad)"/>'
            f'<path d="M-6 -9 v-5 M0 -8 v-5 M6 -9 v-5 M-6 9 v5 M0 8 v5 M6 9 v5" stroke="var(--night)" stroke-width="2"/><circle cx="-15" cy="-5" r="1.5" fill="#FFF"/></g>')


def smithy(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-60" y="0" width="120" height="80" fill="#6B4F3A"/><path d="M-70 0 L0 -40 L70 0 Z" fill="#8B5E3C"/>'
            f'<rect x="-14" y="30" width="28" height="50" fill="var(--night)"/><rect x="30" y="-30" width="12" height="30" fill="var(--stone-dark)"/>'
            f'<path d="M36 -34 q-8 -10 0 -18 q8 8 0 18z" fill="#C9D5E6" opacity="0.7"/></g>')


def seal(x, y, s=1.0, ok=True):
    mark = ('<path d="M-6 0 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>' if ok
            else '<path d="M-5 -5 l10 10 M5 -5 l-10 10" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="11" fill="{"var(--good)" if ok else "var(--bad)"}"/>{mark}</g>'


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


# 1. 벽은 튼튼해요 — 목수님은 어서 오세요
P1 = svg(320, sky(320)
         + castle(300, 60, 0.95) + person(60, 130, s=0.85, hat="var(--bad)", shirt="#2E3D57", face=MASK + SWEAT) + label(95, 250, "⟦도둑은 못 들어와요|the thief can\'t get in⟧", 12, "var(--ink)")
         + person(455, 160, s=0.75, face=SMILE, **CARPENTER) + toolbox(520, 240, 0.7) + person(640, 160, s=0.7, face=SMILE, **GUARD)
         + bubble(585, 30, 170, 34, "⟦목수님, 어서 오세요!|welcome, carpenter!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(560, 292, "⟦아는 얼굴은 문이 활짝 열려요|for a friendly face, the gate opens wide⟧", 12, "var(--ink)", cls="d"))

# 2. 연장통 안에 벌레가 미리 들어 있었어요 — 대장간이 털린 거예요
P2 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + smithy(110, 70, 1.0) + label(110, 185, "⟦마을 대장간|the village smithy⟧", 12, "var(--ink)") + person(30, 195, s=0.6, **THIEF) + toolbox(150, 245, 0.8, open_=True, bug=True)
         + label(125, 292, "⟦도둑이 밤에 벌레를 넣어 뒀어요|the thief slipped a bug in overnight⟧", 11, "var(--muted)")
         + '<path d="M230 200 h100" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M320 192 l10 8 l-10 8" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(360, 110, s=0.85, face=SMILE, **CARPENTER) + toolbox(430, 200, 0.8) + label(385, 292, "⟦목수는 몰라요 — 늘 사던 연장통이니까|the carpenter has no idea — the usual box⟧", 11, "var(--muted)")
         + '<path d="M480 200 h60" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M530 192 l10 8 l-10 8" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + small_castle(570, 60, 0.7) + bug(640, 190, 1.2) + label(640, 292, "⟦성 안에서 벌레가 기어 나와요|inside, the bug crawls out⟧", 11, "var(--bad)")
         + label(380, 322, "⟦우리 벽이 뚫린 게 아니에요 — 대장간이 털린 거예요|our wall wasn\'t breached — the smithy was robbed⟧", 13, "var(--ink)", cls="d"))

# 3. 공급망 공격 = 목수의 연장통에 숨어 들어온 벌레 (hero)
P3 = svg(360, night(360)
         + '<rect x="380" y="60" width="380" height="200" fill="var(--stone-dark)"/>' + battlements(380, 40, 380, 7, "var(--stone-dark)")
         + '<path d="M410 260 V190 a34 34 0 0 1 68 0 V260 Z" fill="var(--night)"/>'
         + person(310, 130, s=0.9, face=SMILE, **CARPENTER) + toolbox(300, 235, 1.0, bug=True) + '<circle cx="320" cy="235" r="16" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/>'
         + label(310, 292, "⟦연장통 속에 벌레가 숨어 있어요|a bug hides in the toolbox⟧", 12, "#F5E6B8")
         + person(520, 130, s=0.8, face=SMILE, **GUARD) + label(550, 240, "⟦문지기는 연장통을 안 열어봐요|the gatekeeper never opens the toolbox⟧", 11, "#C9D5E6")
         + smithy(90, 90, 0.9) + label(90, 200, "⟦털린 대장간|the robbed smithy⟧", 11, "#C9D5E6") + '<path d="M170 200 q60 40 100 30" stroke="var(--bad)" stroke-width="3" fill="none" stroke-dasharray="6 5"/>'
         + label(380, 322, "⟦벌레는 성문으로 안 와요 — 우리가 믿는 사람의 짐에 실려 와요|the bug doesn\'t come through the gate — it rides in with someone we trust⟧", 13, "#F5E6B8", cls="d")
         + label(380, 348, "⟦대장간 하나가 털리면, 거기서 산 성 모두가 위험해요|rob one smithy, and every castle that buys from it is in danger⟧", 11, "#C9D5E6"))

# 4. 막는 법 — 목록표, 봉인, 대장간 검사, 모래 방
P4 = svg(340, sky(340)
         + paper(40, 30, 200, 120, "⟦연장통 부품 목록표|WHAT\'S IN THE BOX⟧", ("⟦망치 1 — 서쪽 대장간|hammer — west smithy⟧", "⟦톱 1 — 서쪽 대장간|saw — west smithy⟧", "⟦못 100 — 마을 상점|nails — village shop⟧"))
         + label(140, 172, "⟦안에 뭐가 들었는지 적어요|write down what\'s inside⟧", 11, "var(--ink)")
         + toolbox(340, 90, 1.0) + seal(372, 62, 1.2, ok=True) + label(340, 172, "⟦대장간 봉인이 그대로인지 봐요|check the smithy\'s seal is unbroken⟧", 11, "var(--ink)")
         + smithy(530, 50, 0.7) + person(590, 80, s=0.55, face=EYES, **BLUE) + label(560, 172, "⟦대장간도 가끔 가서 살펴요|visit the smithy and look around⟧", 11, "var(--ink)")
         + '<rect x="60" y="205" width="130" height="90" rx="6" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="4"/>' + toolbox(125, 268, 0.6, open_=True) + label(125, 226, "⟦모래 방|the sand room⟧", 11, "#142033", cls="d")
         + label(320, 250, "⟦새 연장통은 창문 없는 빈 방에서 먼저 열어봐요|open a new toolbox in the empty room first⟧", 12, "var(--ink)", "start")
         + label(320, 272, "⟦벌레가 나오면 그 방 안에서 끝이에요|if a bug comes out, it ends inside that room⟧", 11, "var(--muted)", "start")
         + label(380, 322, "⟦믿더라도, 열어 보고 믿어요|trust — but open the box first⟧", 13, "var(--ink)", cls="d"))

# 5. 결과 — 봉인이 깨진 연장통은 성문 밖에서 멈춰요
P5 = svg(320, sky(320)
         + gate(380, 120, 0.8) + person(250, 130, s=0.85, face=EYES, **CARPENTER) + toolbox(330, 250, 0.9, bug=True) + seal(345, 222, 1.2, ok=False)
         + person(480, 140, s=0.8, face=EYES, **GUARD) + bubble(440, 30, 240, 34, "⟦봉인이 다르네요 — 잠깐만요|the seal doesn\'t match — hold on⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 290, "⟦벌레는 성문 밖에서 멈췄어요|the bug stopped outside the gate⟧", 13, "var(--ink)", cls="d")
         + paper(600, 150, 160, 90, "⟦대장간 소식|SMITHY NEWS⟧", ("⟦서쪽 대장간 털림!|west smithy robbed!⟧", "⟦연장통 확인 요망|check your toolboxes⟧"), 0.9)
         + label(662, 262, "⟦망루 친구가 알려줘요|the watchtower spreads the word⟧", 10, "var(--muted)"))

LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M22 20 h20 M22 30 h20 M22 40 h14" stroke="#142033" stroke-width="3" stroke-linecap="round"/><circle cx="46" cy="50" r="7" fill="var(--good)"/>')
SEAL_I = icon('<rect x="8" y="26" width="48" height="26" rx="3" fill="#8B5E3C"/><rect x="8" y="20" width="48" height="8" rx="2" fill="#5A3B22"/><circle cx="32" cy="24" r="11" fill="var(--good)"/><path d="M26 24 l4 4 l8 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')
VISIT_I = icon('<rect x="14" y="30" width="36" height="24" fill="#6B4F3A"/><path d="M10 30 L32 16 L54 30 Z" fill="#8B5E3C"/><rect x="28" y="40" width="8" height="14" fill="var(--night)"/><circle cx="50" cy="14" r="8" fill="none" stroke="#5B8DEF" stroke-width="3"/><path d="M56 20 l6 6" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/>')
SAND_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="22" y="32" width="20" height="12" rx="2" fill="#8B5E3C"/><ellipse cx="32" cy="26" rx="6" ry="4" fill="var(--bad)"/>')

PAGE = {
    "slug": "supplychain", "order": 72,
    "title": ("목수의 연장통에 숨어 들어온 벌레", "The Bug That Hid in the Carpenter\'s Toolbox"),
    "h1": ("<em>공급망 공격</em>이 뭐예요?", "What is a <em>Supply Chain Attack</em>?"),
    "sub": ("공급망 공격(Supply Chain Attack)을 벽은 튼튼한데 목수가 마을에서 사 온 연장통 속에 벌레가 미리 들어 있던 이야기로 풀어봤어요.",
            "Supply chain attacks, told as a story about a castle with a strong wall — and a bug that was already inside the toolbox the carpenter bought in the village."),
    "panels": [
        {"svg": P1, "alt": ("낮. 큰 성 앞에서 도둑은 땀을 흘리며 못 들어가고, 연장통을 든 목수에게는 경비가 '어서 오세요' 하며 성문을 열어 줌", "Day. Outside the castle a sweating thief can\'t get in, while the guard opens the gate wide for the carpenter and his toolbox: welcome"),
         "caption": ("우리 벽은 튼튼해요. 그런데 목수님은 언제나 어서 오세요예요.", "Our wall is strong. But the carpenter is always welcome."),
         "small": ('<a href="patch-ko.html">목수</a>는 매달 판자를 들고 와요. 아는 얼굴이라 <a href="firewall-ko.html">성문</a>이 활짝 열려요. 연장통은 아무도 안 열어봐요.',
                   'The <a href="patch-en.html">carpenter</a> brings planks every month. A friendly face, so the <a href="firewall-en.html">gate</a> opens wide. Nobody opens the toolbox.')},
        {"svg": P2, "alt": ("마을 대장간에 밤에 도둑이 들어 연장통에 벌레를 넣음 → 목수가 그 연장통을 사서 → 성 안에서 벌레가 기어 나옴", "A thief breaks into the village smithy at night and puts a bug in a toolbox → the carpenter buys that toolbox → inside the castle the bug crawls out"),
         "caption": ("연장통 안에 벌레가 미리 들어 있었어요. 대장간이 털린 거예요.", "The bug was already in the toolbox. It was the smithy that got robbed."),
         "small": ('도둑은 우리 벽을 뚫지 않았어요. 목수가 늘 사던 마을 대장간에 몰래 들어가 <a href="malware-ko.html">벌레</a>를 넣어 뒀어요. 목수는 몰라요.',
                   'The thief never touched our wall. He crept into the village smithy the carpenter always buys from and planted a <a href="malware-en.html">bug</a>. The carpenter has no idea.')},
        {"svg": P3, "hero": True, "alt": ("밤. 털린 대장간에서 나온 점선이 목수의 연장통으로 이어지고, 연장통 속 벌레에 빨간 점선 동그라미. 목수는 웃으며 성문을 지나고 문지기도 웃으며 연장통을 열어보지 않음", "Night. A dotted line runs from the robbed smithy to the carpenter\'s toolbox, where a bug is circled in red. The carpenter walks smiling through the gate; the gatekeeper smiles and never opens the box"),
         "caption": ("공급망 공격은 목수의 연장통에 숨어 들어온 벌레예요.", "A supply chain attack is a bug that hides in the carpenter\'s toolbox."),
         "small": ("벌레는 성문으로 안 와요. 우리가 믿는 사람의 짐에 실려 와요. 대장간 하나가 털리면 거기서 사는 성 모두가 위험해요.", "The bug doesn\'t come through the gate. It rides in with someone we trust. Rob one smithy, and every castle that buys from it is in danger."),
         "tricks": (4, [
             (LIST_I, ("부품 목록표", "A parts list"), ("연장통에 뭐가 들었는지", "what\'s in the box"), "warm"),
             (SEAL_I, ("봉인 확인", "Check the seal"), ("대장간 도장이 그대로인지", "is the smithy\'s stamp unbroken?")),
             (VISIT_I, ("대장간도 검사", "Inspect the smithy too"), ("사 오는 곳도 살펴요", "look where we buy from")),
             (SAND_I, ("모래 방에서 먼저", "The sand room first"), ("새 연장통은 빈 방에서 열어요", "open new boxes in the empty room"), "calm"),
         ])},
        {"svg": P4, "alt": ("네 가지 방법: 연장통 부품 목록표(망치·톱·못과 어느 대장간에서 왔는지), 초록 봉인 확인, 대장간을 살피는 파란 모자 친구, 창문 없는 모래 방에서 연장통을 먼저 여는 그림", "Four methods: a parts list for the toolbox (hammer, saw, nails and which smithy they came from), a green seal check, a blue-hat friend looking over the smithy, and a windowless sand room where the box is opened first"),
         "caption": ("믿더라도, 열어 보고 믿어요.", "Trust — but open the box first."),
         "small": ('<a href="sbom-ko.html">부품 목록표</a>로 안에 뭐가 들었는지 알고, <a href="hashing-ko.html">지문</a>처럼 봉인이 그대로인지 보고, 새 연장통은 <a href="sandbox-ko.html">창문 없는 빈 방</a>에서 먼저 열어요.',
                   'Know what\'s inside with a <a href="sbom-en.html">parts list</a>, check the seal like a <a href="hashing-en.html">fingerprint</a>, and open every new toolbox in the <a href="sandbox-en.html">windowless empty room</a> first.')},
        {"svg": P5, "alt": ("성문 앞에서 경비가 목수의 연장통 봉인이 빨간 X 인 것을 보고 '봉인이 다르네요, 잠깐만요'. 옆의 대장간 소식지: 서쪽 대장간 털림, 연장통 확인 요망", "At the gate the guard sees a red X on the toolbox seal: the seal doesn\'t match, hold on. Beside it, smithy news: west smithy robbed, check your toolboxes"),
         "caption": ("봉인이 다르면 연장통은 성문 밖에서 멈춰요.", "If the seal is wrong, the toolbox stops outside the gate."),
         "small": ('목수는 여전히 우리 친구예요 — 잘못한 건 대장간을 턴 도둑이에요. <a href="cti-ko.html">망루 친구</a>가 "서쪽 대장간이 털렸대요" 하고 알려주면 성마다 연장통을 확인해요.',
                   'The carpenter is still our friend — the one at fault is the thief who robbed the smithy. When the <a href="cti-en.html">watchtower friend</a> says the west smithy was robbed, every castle checks its toolboxes.')},
    ],
    "summary": (("<b>공급망 공격</b> = 우리 벽을 뚫는 대신, 우리가 <b>믿고 사 오는 대장간</b>을 털어 <b>연장통 속에 벌레를 미리 넣어</b> 두는 것. 막으려면 <b>목록표, 봉인, 대장간 검사, 모래 방</b>이 필요해요.",
                 "<b>Supply chain attack</b> = instead of breaching our wall, rob the <b>smithy we trust and buy from</b> and <b>plant a bug in the toolbox</b> ahead of time. Stopping it takes a <b>parts list, seals, smithy inspections, and a sand room</b>."),
                ("Supply Chain Attack. 조직이 직접 공격받는 대신, 사용하는 소프트웨어·부품·업데이트·서비스를 만드는 공급업체(벤더, 오픈소스 프로젝트)가 먼저 침해되어 그 경로로 악성 코드가 들어오는 공격이에요. SBOM, 코드 서명 검증, 벤더 평가, 샌드박스 검사로 대비해요.",
                 "An attack where the vendor, open-source project, update channel, or service an organization depends on is compromised first, and malicious code arrives through that trusted path. Defended with SBOMs, code-signing verification, vendor assessment, and sandboxed testing.")),
    "glossary": [
        ("연장통 속 벌레", "Supply chain attack", ("믿는 사람의 짐에 실려 오는 벌레.", "A bug that rides in with someone we trust."), ("우리 벽이 아니라 대장간이 뚫린 거예요. 문지기는 아는 얼굴을 의심하지 않아요.", "It\'s the smithy that was breached, not our wall. The gatekeeper never suspects a friendly face.")),
        ("대장간", "Third party / vendor", ("목수가 연장을 사 오는 곳.", "Where the carpenter buys his tools."), ("우리 성 밖에 있지만 우리 성 안에 들어오는 물건을 만들어요. 그래서 대장간의 안전이 곧 우리 안전이에요.", "Outside our castle, yet it makes what comes inside. So the smithy\'s safety is our safety.")),
        ("봉인", "Code signing", ("대장간이 찍은 도장.", "The smithy\'s own stamp."), ('도장이 깨졌거나 다르면 누가 손댄 거예요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>, <a href="encryption-ko.html">봉인 편지</a>', 'A broken or different stamp means someone tampered. → <a href="hashing-en.html">a fingerprint on every item</a>, <a href="encryption-en.html">the sealed letter</a>')),
        ("부품 목록표", "SBOM (Software Bill of Materials)", ("연장통에 뭐가 들었는지 적은 종이.", "A paper listing what\'s in the toolbox."), ('"서쪽 대장간 털림" 소식이 오면 어느 연장통을 봐야 할지 바로 알아요. → <a href="sbom-ko.html">도구에 붙은 부품 목록표</a>', 'When the news says the west smithy was robbed, you know at once which boxes to check. → <a href="sbom-en.html">the parts list on the tool</a>')),
        ("가짜 판자 배달", "Update hijacking", ("목수가 보낸 판자인 척.", "Pretending to be the carpenter\'s plank."), ('매달 오는 판자 배달을 도둑이 가로채 벌레 든 판자를 보내요. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'The thief hijacks the monthly plank delivery and sends one with a bug inside. → <a href="patch-en.html">the plank the carpenter sent</a>')),
        ("마을에서 얻어온 부품", "Open-source dependency", ("누구나 쓰는 공짜 못과 나사.", "Free nails and screws everyone uses."), ("연장통의 부품 대부분은 목수가 만든 게 아니라 마을에서 얻어와요. 하나가 썩으면 그걸 쓴 연장통이 다 위험해요.", "Most parts in a toolbox weren\'t made by the carpenter — they came from the village. If one goes bad, every box using it is at risk.")),
        ("대장간 검사", "Vendor assessment", ("사 오는 곳도 가끔 살피기.", "Looking over where we buy from."), ("대장간에 자물쇠는 있는지, 밤에 누가 지키는지 물어봐요. 대답 못 하는 대장간에선 안 사요.", "Ask whether the smithy has locks and a night watch. Don\'t buy from one that can\'t answer.")),
        ("실제 있었던 일", "SolarWinds (2020)", ("판자 하나에 실린 벌레가 성 수천 곳으로.", "One plank\'s bug reached thousands of castles."), ("많은 성이 쓰는 도구의 정기 업데이트에 벌레가 실려 나가, 한 번에 수천 곳이 열렸어요.", "A bug rode out in a routine update of a tool used by many castles, opening thousands at once.")),
    ],
}
