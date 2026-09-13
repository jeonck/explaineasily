from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")


def lantern(x, y, s=1.0, glass="#FFD166", crack=False):
    c = '<path d="M-6 -6 l4 8 l-5 6 l6 8" stroke="#0A1120" stroke-width="2" fill="none" stroke-linecap="round"/>' if crack else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-14 -40 a14 14 0 0 1 28 0" stroke="#8B5E3C" stroke-width="5" fill="none"/>'
            f'<rect x="-18" y="-40" width="36" height="8" rx="2" fill="var(--stone-dark)"/><rect x="-16" y="-32" width="32" height="44" rx="4" fill="{glass}" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<rect x="-3" y="-20" width="6" height="16" fill="var(--accent)"/><rect x="-18" y="12" width="36" height="8" rx="2" fill="var(--stone-dark)"/>{c}</g>')


def tag(x, y, rows, s=1.0, missing=False, stale=False):
    if missing:
        return (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="70" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2" stroke-dasharray="5 4"/>'
                f'{label(65, 40, "⟦목록표 없음|no parts list⟧", 12, "var(--bad)")}</g>')
    lines = "".join(label(10, 24 + i * 15, r, 10, "#142033", "start") for i, r in enumerate(rows))
    st = label(65, 24 + len(rows) * 15 + 4, "⟦(작년 것)|(last year\'s)⟧", 9, "var(--bad)") if stale else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="{22 + len(rows) * 15 + (12 if stale else 0)}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<circle cx="8" cy="8" r="3" fill="var(--stone-dark)"/>{lines}{st}</g>')


PARTS = ("⟦손잡이 · 김목수 2판|handle · Kim 2nd ed.⟧", "⟦유리 · 박유리 3판|glass · Park 3rd ed.⟧", "⟦심지 · 최심지 1판|wick · Choi 1st ed.⟧")

# 1. 도구는 여러 장인의 부품으로
P1 = svg(300, sky(300) + lantern(380, 150, 1.6)
         + person(60, 60, s=0.7, hat="#8B5E3C", shirt="#4A5A72", face=SMILE) + '<path d="M120 100 L350 105" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>' + label(80, 170, "⟦김목수: 손잡이|Kim: the handle⟧", 11, "var(--muted)")
         + person(60, 180, s=0.7, hat="#5B8DEF", shirt="#4A5A72", face=SMILE) + '<path d="M120 220 L355 160" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>' + label(80, 290, "⟦박유리: 유리|Park: the glass⟧", 11, "var(--muted)")
         + person(640, 120, s=0.7, hat="var(--accent)", shirt="#4A5A72", face=SMILE) + '<path d="M640 160 L410 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>' + label(660, 230, "⟦최심지: 심지|Choi: the wick⟧", 11, "var(--muted)")
         + label(380, 270, "⟦등불 하나에도 장인이 셋|even one lantern has three makers⟧", 13, "var(--muted)"))

# 2. 부품 하나에 틈이 있대요
LANTERNS = "".join(lantern(x, y, 0.7, crack=(i in (3, 8, 13))) for i, (x, y) in enumerate((x, y) for y in (110, 200) for x in range(300, 740, 60)))
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<g transform="translate(120,70)"><rect x="-90" y="-30" width="180" height="60" rx="8" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/>' + label(0, -6, "⟦박유리 3판 유리에|Park\'s 3rd-ed. glass⟧", 12, "var(--ink)") + label(0, 16, "⟦틈이 있대요!|has a crack!⟧", 14, "var(--bad)", cls="d") + "</g>"
         + person(90, 130, s=0.9, face=FROWN + SWEAT, **GUARD) + label(120, 270, "⟦어느 등불이지…?|which lanterns…?⟧", 13, "var(--bad)")
         + LANTERNS
         + label(520, 275, "⟦천 개 중에 어느 것인지, 하나씩 뜯어봐야 해요|one of a thousand — take each one apart to find out⟧", 12, "var(--muted)"))

# 3. SBOM = 도구마다 붙은 부품 목록표 (hero)
P3 = svg(340, sky(340) + lantern(220, 170, 1.8)
         + '<path d="M260 150 L330 130" stroke="#C9A86A" stroke-width="2"/>' + tag(330, 80, PARTS, 1.3)
         + person(600, 60, s=0.8, face=SMILE, **BUILDER) + label(630, 190, "⟦목수가 넘길 때 같이 줘요|the builder hands it over with the tool⟧", 11, "var(--muted)")
         + label(380, 322, "⟦어떤 부품이 몇 번 판인지, 누가 만들었는지 적혀 있어요|which parts, which edition, made by whom⟧", 13, "var(--muted)"))

# 4. 틈 소식이 오면 목록표만 훑는다
TAGS = "".join(tag(x, y, PARTS if i in (1, 4) else ("⟦손잡이 · 김목수 1판|handle · Kim 1st⟧", "⟦유리 · 박유리 2판|glass · Park 2nd⟧", "⟦심지 · 최심지 1판|wick · Choi 1st⟧"), 0.7) for i, (x, y) in enumerate(((300, 40), (410, 40), (520, 40), (630, 40), (300, 150), (410, 150), (520, 150), (630, 150))))
HITS = "".join(f'<rect x="{x - 4}" y="{y - 4}" width="99" height="60" rx="6" fill="none" stroke="var(--bad)" stroke-width="3"/>' for x, y in ((410, 40), (300, 150)))
P4 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + '<g transform="translate(120,90)"><rect x="-90" y="-30" width="180" height="60" rx="8" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/>' + label(0, -6, "⟦박유리 3판|Park 3rd ed.⟧", 12, "var(--ink)") + label(0, 16, "⟦틈!|crack!⟧", 14, "var(--bad)", cls="d") + "</g>"
         + person(90, 150, s=0.85, face=SMILE, **GUARD, extra='<g transform="translate(70,60)"><circle r="14" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M10 10 L22 22" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>')
         + TAGS + HITS
         + label(480, 250, "⟦이 둘만 고치면 돼요|only these two need fixing⟧", 14, "var(--bad)", cls="d")
         + label(380, 300, "⟦뜯어볼 필요가 없어요 — 목록표만 훑어요|no taking apart — just read the lists⟧", 13, "var(--muted)"))

# 5. 목록표는 '있다'까지만
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--sky)"/>'
         + lantern(90, 130, 1.1, glass="var(--stone)") + tag(140, 80, (), 0.9, missing=True) + label(130, 220, "⟦오래된 도구|an old tool⟧", 12, "var(--muted)")
         + lantern(260, 130, 1.1) + tag(200, 200, PARTS[:2], 0.7, stale=True)
         + label(190, 300, "⟦목록표가 없거나 오래됐어요|no list, or a stale one⟧", 13, "var(--bad)")
         + lantern(470, 130, 1.3, crack=True) + tag(520, 60, PARTS, 0.9)
         + '<g transform="translate(600,190)"><rect x="-60" y="-24" width="120" height="48" rx="6" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/>' + label(0, -6, "⟦틈은 있지만|crack is there, but⟧", 11, "var(--ink)") + label(0, 12, "⟦이 등불은 안 켜요|this lantern never lights⟧", 11, "var(--good)") + "</g>"
         + label(570, 260, "⟦'있다'와 '위험하다'는 달라요|being there and being dangerous differ⟧", 12, "var(--ink)")
         + label(570, 300, "⟦그건 따로 적어줘요 — VEX|that goes on a separate note — VEX⟧", 11, "var(--muted)"))

PART_I = icon('<rect x="10" y="14" width="18" height="36" rx="3" fill="#FFD166" stroke="var(--stone-dark)" stroke-width="2"/><rect x="36" y="20" width="18" height="24" rx="3" fill="#8B5E3C"/>')
VER_I = icon('<rect x="12" y="14" width="40" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><text x="32" y="38" text-anchor="middle" font-size="14" font-weight="700" fill="var(--accent)">v3</text>')
WHO_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><path d="M20 18 Q32 4 44 18 Z" fill="#5B8DEF"/><rect x="18" y="34" width="28" height="22" rx="8" fill="#4A5A72"/>')
NEST_I = icon('<rect x="8" y="8" width="48" height="48" rx="4" fill="none" stroke="var(--stone-dark)" stroke-width="2"/><rect x="18" y="18" width="28" height="28" rx="3" fill="none" stroke="var(--stone-dark)" stroke-width="2"/><rect x="26" y="26" width="12" height="12" rx="2" fill="var(--accent)"/>')

PAGE = {
    "slug": "sbom", "order": 48,
    "title": ("도구에 붙은 부품 목록표", "The Parts List on Every Tool"),
    "h1": ("<em>SBOM</em>이 뭐예요?", "What is an <em>SBOM</em>?"),
    "sub": ("소프트웨어 자재 명세서(Software Bill of Materials)를 도구마다 붙은 부품 목록표 이야기로 풀어봤어요.",
            "Software Bill of Materials, told as a story about the parts list attached to every tool."),
    "panels": [
        {"svg": P1, "alt": ("등불 하나에 손잡이는 김목수, 유리는 박유리, 심지는 최심지가 만들었다는 점선", "One lantern, with dotted lines to three makers: Kim for the handle, Park for the glass, Choi for the wick"),
         "caption": ("도구는 여러 장인의 부품으로 만들어져요.", "A tool is made of parts from many makers."),
         "small": ("등불 하나에도 손잡이, 유리, 심지가 다 다른 장인 거예요. 프로그램도 그래요.", "Even one lantern has a handle, glass and wick from three different makers. Programs are the same.")},
        {"svg": P2, "alt": ("'박유리 3판 유리에 틈이 있대요!' 공지 앞에서 경비가 땀을 흘리고, 등불 열네 개 중 셋에만 틈이 있음", "A notice — Park's 3rd-ed. glass has a crack! — a sweating guard, and fourteen lanterns of which only three are cracked"),
         "caption": ("부품 하나에 틈이 있대요. 어느 도구에 들어 있죠?", "One part has a crack. Which tools is it in?"),
         "small": ('<a href="zeroday-ko.html">틈</a> 소식은 왔는데, 성에 도구가 천 개예요. 그 유리가 들어간 게 뭔지 아무도 몰라요. 하나씩 뜯어봐야 해요.',
                   'The <a href="zeroday-en.html">crack</a> is announced, but the castle has a thousand tools. Nobody knows which ones hold that glass. You\'d take each apart.')},
        {"svg": P3, "hero": True, "alt": ("등불에 달린 목록표: 손잡이 김목수 2판, 유리 박유리 3판, 심지 최심지 1판. 옆에 목수", "A tag on the lantern: handle Kim 2nd ed., glass Park 3rd ed., wick Choi 1st ed.; the builder beside it"),
         "caption": ("SBOM은 도구마다 붙은 부품 목록표예요.", "An SBOM is the parts list attached to every tool."),
         "small": ("어떤 부품이 몇 번 판인지, 누가 만들었는지 적혀 있어요. 목수가 도구를 넘길 때 같이 줘요.", "Which parts, which edition, made by whom. The builder hands it over with the tool."),
         "tricks": (4, [
             (PART_I, ("부품 이름", "Part name"), ("유리, 손잡이, 심지", "glass, handle, wick"), "warm"),
             (VER_I, ("몇 번 판", "Which edition"), ("3판인지 2판인지", "3rd or 2nd"), "calm"),
             (WHO_I, ("누가 만들었나", "Who made it"), ("장인 이름", "the maker\'s name"), "calm"),
             (NEST_I, ("부품 안의 부품", "Parts inside parts"), ("유리 속 모래까지", "down to the sand in the glass")),
         ])},
        {"svg": P4, "alt": ("'박유리 3판 틈!' 공지, 돋보기를 든 경비, 목록표 여덟 장 중 둘에 빨간 테두리 — '이 둘만 고치면 돼요'", "A notice Park 3rd ed. crack!, a guard with a magnifying glass, eight parts lists with two outlined in red — only these two need fixing"),
         "caption": ("틈 소식이 오면 목록표만 훑으면 돼요.", "When a crack is announced, just read the lists."),
         "small": ('"박유리 3판" — 목록표에서 찾으면 어느 도구를 고쳐야 하는지 바로 나와요. 뜯어볼 필요가 없어요. → <a href="patch-ko.html">목수가 보낸 판자</a>',
                   '"Park 3rd ed." — search the lists and you know exactly which tools to fix. No taking apart. → <a href="patch-en.html">the board from the builder</a>')},
        {"svg": P5, "alt": ("왼쪽: 목록표가 없는 오래된 등불과 작년 목록표. 오른쪽: 틈 있는 유리가 든 등불이지만 '이 등불은 안 켜요' 쪽지", "Left: an old lantern with no list, and a last-year list. Right: a lantern with the cracked glass, but a note — this lantern never lights"),
         "caption": ("목록표는 '있다'까지만 알려줘요.", "A parts list only says a part is there."),
         "small": ("그 부품이 들어 있어도 실제로 쓰이는지, 틈에 닿는지는 따로 봐야 해요(VEX). 오래된 도구엔 목록표가 아예 없어요.", "Whether the part is actually used, or the crack reachable, is a separate question (VEX). And old tools have no list at all.")},
    ],
    "summary": (("<b>SBOM</b> = 도구마다 붙은 <b>부품 목록표</b>. 부품에 틈이 나면 어느 도구를 고쳐야 하는지 <b>뜯지 않고</b> 알 수 있어요.",
                 "An <b>SBOM</b> = the <b>parts list</b> on every tool. When a part has a crack, you know which tools to fix <b>without taking them apart</b>."),
                ("Software Bill of Materials. 2021년 미국 행정명령 이후 요구되기 시작했고, log4j 틈(2021) 때 '어느 도구에 들었지?'로 온 세상이 고생하며 필요성이 드러났어요. 양식은 SPDX와 CycloneDX.",
                 "Required since a 2021 US executive order; the log4j crack (2021), when the whole world scrambled to ask which tools have it?, showed why. Formats: SPDX and CycloneDX.")),
    "glossary": [
        ("부품", "Component", ("장인이 만든 조각.", "A maker\'s piece."), ("라이브러리, 패키지. 프로그램 대부분은 남의 부품이에요.", "Libraries, packages. Most of a program is other people\'s parts.")),
        ("버전", "Version", ("몇 번 판.", "Which edition."), ("틈은 특정 판에만 있어요. 판 번호가 없으면 목록표가 반쪽이에요.", "A crack lives in specific editions. Without the number, the list is half useless.")),
        ("공급자", "Supplier", ("장인.", "The maker."), ("누가 만들었는지. 장인 공방이 털리면 부품도 위험해요.", "Who made it. If the maker\'s workshop is robbed, the parts are suspect too.")),
        ("전이 의존성", "Transitive dependency", ("부품 안의 부품.", "Parts inside parts."), ("유리 장인도 모래를 남에게 사요. 목록표는 그것까지 적어요.", "The glassmaker buys sand from someone else. The list goes that deep.")),
        ("SPDX · CycloneDX", "SPDX · CycloneDX", ("목록표 양식.", "List formats."), ("온 세상 목수가 같은 칸에 적게 한 두 가지 서식.", "Two forms so every builder writes in the same columns.")),
        ("VEX", "VEX", ("'실제로 위험한가' 쪽지.", "The \'is it actually dangerous\' note."), ("부품은 있지만 이 도구에선 그 틈에 안 닿는다고 적어줘요.", "Says the part is there, but this tool never reaches the crack.")),
        ("공급망 공격", "Supply-chain attack", ("장인 공방에 벌레 넣기.", "A bug slipped into the maker\'s workshop."), ('부품 자체에 벌레가 들어오면 그걸 쓴 도구 전부. → <a href="malware-ko.html">선물 상자 속 벌레</a>', 'Bug the part, and every tool using it is bugged. → <a href="malware-en.html">the bug in the gift box</a>')),
        ("취약점 스캔", "Vulnerability scan", ("목록표와 틈 목록 맞춰보기.", "Matching lists against known cracks."), ('목록표가 있으면 자동으로 돼요. → <a href="patch-ko.html">목수가 보낸 판자</a>', 'With a list, it\'s automatic. → <a href="patch-en.html">the board from the builder</a>')),
    ],
}
