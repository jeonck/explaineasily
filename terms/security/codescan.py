from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
BUILDER2 = dict(hat="var(--accent)", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
ARMBAND = '<rect x="4" y="60" width="14" height="10" rx="2" fill="var(--good)"/><path d="M7 65 l3 3 l5 -6" stroke="#FFF" stroke-width="2" fill="none"/>'
HIRED = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK, extra=ARMBAND)
GLASS = '<g transform="translate(66,52)"><circle r="13" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M9 9 L22 22" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>'
HAMMER = '<g transform="translate(66,50) rotate(-30)"><rect x="-4" y="-22" width="8" height="44" rx="2" fill="#8B5E3C"/><rect x="-14" y="-30" width="28" height="12" rx="3" fill="var(--stone-dark)"/></g>'
PAPER, PAPER_EDGE, INK = "#FFF8E7", "#C9A86A", "#142033"


def wall(x, y, w, h, cracks=(), color="var(--stone-dark)"):
    """벽돌 벽. cracks 는 벽 안 좌표 (cx, cy) 목록."""
    rows = "".join(f'<path d="M{x} {y + r} h{w}" stroke="var(--stone)" stroke-width="2"/>' for r in range(24, h, 24))
    cols = "".join(f'<path d="M{x + c + (12 if (r // 24) % 2 else 0)} {y + r} v24" stroke="var(--stone)" stroke-width="2"/>' for r in range(0, h, 24) for c in range(24, w, 48))
    cr = "".join(f'<path d="M{x + cx} {y + cy} l5 12 l-7 10 l8 14" stroke="#0A1120" stroke-width="4" fill="none" stroke-linecap="round"/>' for cx, cy in cracks)
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>{rows}{cols}{cr}'


def sheets(x, y, n=6, title=""):
    out = "".join(f'<rect x="{x + i * 3}" y="{y - i * 4}" width="120" height="80" rx="4" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="2"/>' for i in range(n))
    top = x + (n - 1) * 3, y - (n - 1) * 4
    out += "".join(f'<path d="M{top[0] + 12} {top[1] + 20 + k * 14} h{60 - (k % 2) * 20}" stroke="{PAPER_EDGE}" stroke-width="2" stroke-linecap="round"/>' for k in range(4))
    return out + (label(x + 60 + (n - 1) * 1.5, y + 98, title, 11, "var(--muted)") if title else "")


def flag(x, y, color="var(--bad)"):
    return f'<rect x="{x}" y="{y}" width="3" height="34" fill="var(--night)"/><path d="M{x + 3} {y} h22 l-6 8 l6 8 h-22z" fill="{color}"/>'


def board(x, y, w, h, title, rows):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#1E3A34" stroke="#8B5E3C" stroke-width="5"/>' + label(x + w / 2, y + 26, title, 13, "#F5E6B8", cls="d")
    return out + "".join(label(x + 16, y + 52 + i * 20, r, 11, "#F5E6B8", "start") for i, r in enumerate(rows))


# 1. 도면은 천 장, 벽돌은 만 개 — 눈으로는 다 못 봐요
P1 = svg(300, sky(300)
         + sheets(50, 120, 7, "⟦도면 천 장|a thousand pages⟧")
         + wall(300, 80, 220, 160, cracks=((60, 40), (150, 100)))
         + person(230, 130, s=0.75, face=SMILE, extra=HAMMER, **BUILDER)
         + person(580, 110, s=0.85, face=FROWN + SWEAT, extra=GLASS, **GUARD) + bubble(500, 30, 240, 34, "⟦이걸 눈으로 다 봐요…?|check all of this by eye…?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦틈은 작고, 벽돌은 만 개예요 — 사람 눈으로는 다 못 봐요|the cracks are tiny and the bricks are ten thousand — no eye can check them all⟧", 12, "var(--muted)"))

# 2. 고용한 도둑은 일 년에 한 번 — 그사이 틈은 열려 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<g transform="translate(50,60)"><rect width="110" height="80" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect width="110" height="16" rx="6" fill="var(--bad)"/>' + label(55, 50, "⟦1년에 한 번|once a year⟧", 12, "var(--ink)", cls="d") + label(55, 68, "⟦고용한 도둑|the hired thief⟧", 10, "var(--muted)") + "</g>"
         + person(70, 150, s=0.75, **HIRED)
         + wall(230, 60, 300, 180, cracks=((40, 30), (120, 90), (220, 50)))
         + person(400, 60, s=0.7, **THIEF) + '<path d="M420 110 l-40 30" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(380, 262, "⟦그사이 열 달 동안 틈은 열려 있었어요|for ten months in between, the cracks stayed open⟧", 12, "var(--ink)")
         + person(600, 130, s=0.8, face=FROWN, **GUARD) + bubble(560, 40, 190, 46, "⟦지난달 쌓은 벽돌은 아무도 안 봤네|no one saw last month\'s bricks⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 288, "⟦큰 시험은 가끔이고, 벽돌은 매일 쌓여요|the big test is rare, but bricks go up every day⟧", 11, "var(--muted)"))

# 3. 두 가지 검사 — 도면 보고 틈 찾기, 다 지은 벽 두드려 보기 (hero)
P3 = svg(360, sky(360)
         + label(190, 40, "⟦짓기 전: 도면 검사|before building: read the drawing⟧", 13, "var(--ink)", cls="d")
         + sheets(60, 110, 5) + person(190, 110, s=0.85, face=EYES, extra=GLASS, **GUARD)
         + '<circle cx="110" cy="120" r="12" fill="none" stroke="var(--bad)" stroke-width="3"/>'
         + label(190, 240, "⟦종이 위에서 틈을 찾아요|finding cracks on paper⟧", 12, "var(--muted)")
         + label(570, 40, "⟦지은 후: 벽 두드리기|after building: knock on the wall⟧", 13, "var(--ink)", cls="d")
         + wall(520, 60, 150, 150, cracks=((100, 70),)) + person(440, 100, s=0.85, face=EYES, extra=HAMMER, **GUARD)
         + label(560, 100, "⟦통!|tok!⟧", 12, "var(--accent)", cls="d") + label(640, 190, "⟦…텅?|…tung?⟧", 12, "var(--bad)", cls="d")
         + label(570, 240, "⟦두드려서 빈 소리를 들어요|listening for a hollow sound⟧", 12, "var(--muted)")
         + '<path d="M380 60 V250" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + label(380, 300, "⟦도면도 보고, 벽도 두드려요 — 벽돌 하나 쌓을 때마다 자동으로|read the drawing and knock on the wall — automatically, brick by brick⟧", 13, "var(--ink)", cls="d")
         + label(380, 335, "⟦하나는 빠르고 하나는 확실해요. 둘 다 써요|one is fast, one is sure. use both⟧", 12, "var(--muted)"))

# 4. 도면 검사는 헛소리도 많고, 두드리기는 늦지만 확실해요
P4 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 36, "⟦도면 검사|reading the drawing⟧", 14, "var(--ink)", cls="d") + label(570, 36, "⟦벽 두드리기|knocking on the wall⟧", 14, "var(--ink)", cls="d")
         + sheets(40, 110, 4) + "".join(flag(x, y, c) for x, y, c in ((70, 90, "var(--bad)"), (100, 70, "var(--bad)"), (130, 86, "var(--bad)"), (160, 66, "var(--bad)"), (190, 84, "var(--bad)")))
         + person(230, 100, s=0.8, face=FROWN + SWEAT, extra=GLASS, **GUARD)
         + label(190, 228, "⟦빠르지만 깃발이 너무 많아요|fast, but far too many flags⟧", 12, "var(--ink)")
         + label(190, 250, "⟦'여긴 괜찮은데요?' 헛소리도 섞여요|some are false alarms: this spot is fine⟧", 11, "var(--muted)")
         + wall(430, 60, 140, 140, cracks=((90, 60),)) + flag(500, 76, "var(--good)") + person(580, 90, s=0.8, face=SMILE, extra=HAMMER, **GUARD)
         + label(570, 228, "⟦늦지만 진짜 틈만 찾아요|slower, but it finds only real cracks⟧", 12, "var(--ink)")
         + label(570, 250, "⟦다 지어야 두드릴 수 있어요|you can only knock once it is built⟧", 11, "var(--muted)")
         + label(380, 295, "⟦도면 검사는 앞에서 넓게, 두드리기는 뒤에서 확실하게|read wide and early, knock sure and late⟧", 12, "var(--muted)"))

# 5. 목수도 배워요 — 처음부터 틈 없이 쌓는 법
P5 = svg(320, sky(320)
         + board(40, 40, 250, 130, "⟦틈 없이 쌓는 법|HOW TO LAY WITHOUT CRACKS⟧", ("⟦· 남이 준 벽돌은 먼저 살펴요|· inspect bricks others hand you⟧", "⟦· 열쇠는 벽에 안 박아요|· never nail a key into the wall⟧", "⟦· 두 명이 같이 봐요|· two sets of eyes⟧"))
         + wall(340, 80, 180, 140) + person(300, 150, s=0.75, face=SMILE, extra=HAMMER, **BUILDER) + person(520, 140, s=0.75, face=SMILE, **BUILDER2)
         + bubble(470, 40, 200, 34, "⟦그 벽돌 살짝 삐뚤어요|that brick sits a little crooked⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(430, 250, "⟦동료가 옆에서 같이 봐요|a fellow builder looks it over⟧", 12, "var(--ink)")
         + person(680, 160, s=0.6, **HIRED) + label(660, 250, "⟦가끔은 큰 시험|the big test, now and then⟧", 11, "var(--muted)")
         + label(380, 296, "⟦매일은 검사가, 가끔은 고용한 도둑이 — 역할이 달라요|the checks every day, the hired thief now and then — different jobs⟧", 12, "var(--muted)"))

READ_I = icon('<rect x="12" y="10" width="34" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="20" width="18" height="3" fill="#C9A86A"/><rect x="20" y="28" width="14" height="3" fill="#C9A86A"/><circle cx="42" cy="40" r="9" fill="var(--panel)" fill-opacity="0.5" stroke="var(--night)" stroke-width="3"/><path d="M48 46 l8 8" stroke="var(--night)" stroke-width="4" stroke-linecap="round"/>')
KNOCK_I = icon('<rect x="8" y="16" width="30" height="36" fill="var(--stone-dark)"/><path d="M8 28 h30 M8 40 h30 M23 16 v12 M15 28 v12 M31 28 v12 M23 40 v12" stroke="var(--stone)" stroke-width="2"/><g transform="translate(48,34) rotate(-30)"><rect x="-3" y="-14" width="6" height="28" rx="2" fill="#8B5E3C"/><rect x="-9" y="-19" width="18" height="8" rx="2" fill="var(--night)"/></g>')
PARTS_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="22" cy="22" r="3" fill="var(--good)"/><rect x="28" y="20" width="16" height="3" fill="#142033"/><circle cx="22" cy="34" r="3" fill="var(--bad)"/><rect x="28" y="32" width="14" height="3" fill="#142033"/><circle cx="22" cy="46" r="3" fill="var(--good)"/><rect x="28" y="44" width="12" height="3" fill="#142033"/>')
AUTO_I = icon('<rect x="6" y="40" width="52" height="10" rx="5" fill="var(--stone-dark)"/><rect x="12" y="20" width="18" height="14" rx="3" fill="var(--good)"/><rect x="36" y="20" width="18" height="14" rx="3" fill="var(--good)"/><path d="M17 27 l3 3 l6 -6 M41 27 l3 3 l6 -6" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "codescan", "order": 80,
    "title": ("도면 검사와 두드려 보기", "Reading the Drawing, Knocking on the Wall"),
    "h1": ("<em>코드 스캔</em>이 뭐예요?", "What is <em>Code Scanning</em>?"),
    "sub": ("코드 스캔(SAST·DAST·시큐어 코딩)을 짓기 전에 도면을 읽고, 지은 뒤에 벽을 두드려 보는 경비 이야기로 풀어봤어요.",
            "Code scanning — SAST, DAST, and secure coding — told as a story about a guard who reads the drawing before building and knocks on the wall after."),
    "panels": [
        {"svg": P1, "alt": ("도면이 일곱 장 겹쳐 쌓여 있고, 목수가 쌓은 벽에는 작은 금 두 개. 돋보기를 든 경비가 땀을 흘리며 '이걸 눈으로 다 봐요?'", "Seven pages of drawings in a pile, and two tiny cracks in the wall the builder laid. A guard with a magnifying glass sweats: check all of this by eye?"),
         "caption": ("도면은 천 장, 벽돌은 만 개예요. 눈으로는 다 못 봐요.", "A thousand pages, ten thousand bricks. No eye can check them all."),
         "small": ('<a href="patch-ko.html">목수</a>는 매일 벽돌을 쌓아요. 틈은 벽돌 하나만 해요. 경비 혼자 다 볼 수는 없어요.',
                   'The <a href="patch-en.html">builder</a> lays bricks every day. A crack is the size of one brick. One guard cannot look at them all.')},
        {"svg": P2, "alt": ("'1년에 한 번' 달력 옆에 완장 찬 고용한 도둑. 금이 세 개 난 큰 벽에 진짜 도둑이 올라타 있고, 경비는 '지난달 쌓은 벽돌은 아무도 안 봤네'", "A hired thief with an armband beside a calendar reading once a year. A real thief climbs a wall with three cracks, and the guard says nobody checked last month's bricks"),
         "caption": ("고용한 도둑은 일 년에 한 번 와요. 그사이 틈은 열려 있어요.", "The hired thief comes once a year. In between, the cracks stay open."),
         "small": ('<a href="pentest-ko.html">고용한 도둑</a>은 큰 시험이라 가끔만 와요. 그사이에 쌓은 벽돌은 아무도 안 봤어요. 진짜 도둑은 기다려 주지 않아요.',
                   'The <a href="pentest-en.html">hired thief</a> is the big test, so he comes rarely. Nobody looked at the bricks laid in between. Real thieves do not wait.')},
        {"svg": P3, "hero": True, "alt": ("왼쪽: 경비가 돋보기로 도면 더미를 보며 빨간 동그라미를 침. 오른쪽: 다른 경비가 망치로 완성된 벽을 두드리고 '통! …텅?' 소리", "Left: a guard reads a pile of drawings with a magnifying glass and circles a spot in red. Right: another guard taps a finished wall with a hammer — tok! …tung?"),
         "caption": ("도면도 보고, 벽도 두드려요. 벽돌 하나 쌓을 때마다 자동으로요.", "Read the drawing and knock on the wall — automatically, brick by brick."),
         "small": ("짓기 전엔 도면을 읽어서 틈을 찾아요. 지은 뒤엔 벽을 두드려 빈 소리를 들어요. 남이 준 벽돌은 부품 목록표도 봐요.",
                   "Before building, read the drawing to find cracks. After building, knock on the wall and listen for hollow spots. For bricks made by others, check the parts list too."),
         "tricks": (4, [
             (READ_I, ("도면 읽기", "Read the drawing"), ("짓기 전에, 종이 위에서", "before building, on paper"), "warm"),
             (KNOCK_I, ("벽 두드리기", "Knock on the wall"), ("지은 뒤에, 진짜 벽을", "after building, on the real wall"), "warm"),
             (PARTS_I, ("부품 목록 보기", "Check the parts list"), ("남이 만든 벽돌은 목록표로", "bricks from others, by their list")),
             (AUTO_I, ("벽돌마다 자동", "Every brick, automatically"), ("사람이 안 기다려요", "no one has to wait"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 도면 더미에 빨간 깃발 다섯 개, 경비가 땀 흘림. 오른쪽: 벽의 진짜 틈 하나에 초록 깃발, 경비가 망치를 들고 웃음", "Left: five red flags on a pile of drawings and a sweating guard. Right: one green flag on the real crack in a wall, and a smiling guard with a hammer"),
         "caption": ("도면 검사는 깃발이 너무 많고, 두드리기는 늦지만 확실해요.", "Reading gives too many flags; knocking is late but sure."),
         "small": ("도면 검사는 '혹시' 싶은 곳마다 깃발을 꽂아요. 괜찮은 곳에도요. 두드리기는 진짜 빈 곳만 찾지만, 벽을 다 쌓아야 할 수 있어요.",
                   "Reading plants a flag on every maybe — including spots that are fine. Knocking finds only real hollows, but the wall has to be built first.")},
        {"svg": P5, "alt": ("칠판에 '틈 없이 쌓는 법' 세 줄. 목수 둘이 벽 앞에 서 있고 한 명이 '그 벽돌 살짝 삐뚤어요'. 멀리 완장 찬 고용한 도둑이 작게", "A chalkboard with three lines on how to lay without cracks. Two builders at a wall, one saying that brick sits a little crooked. Far off, a small hired thief with an armband"),
         "caption": ("목수도 배워요. 처음부터 틈 없이 쌓는 법을요.", "The builder learns too — how to lay without cracks from the start."),
         "small": ('틈 없이 쌓는 법을 배우고, 동료가 옆에서 같이 봐요. 검사는 <a href="devsecops-ko.html">매일 벽돌마다</a>, <a href="pentest-ko.html">고용한 도둑</a>은 가끔 큰 시험. 역할이 달라요.',
                   'Learn to lay without cracks, and have a fellow builder look it over. Checks run <a href="devsecops-en.html">every day, every brick</a>; the <a href="pentest-en.html">hired thief</a> is the rare big test. Different jobs.')},
    ],
    "summary": (("<b>코드 스캔</b> = 짓기 전에 <b>도면을 읽어</b> 틈을 찾고, 지은 뒤에 <b>벽을 두드려</b> 빈 소리를 듣는 일. 벽돌 하나 쌓을 때마다 <b>자동으로</b>.",
                 "<b>Code scanning</b> = <b>read the drawing</b> for cracks before building, then <b>knock on the wall</b> for hollow spots after — <b>automatically</b>, brick by brick."),
                ("SAST(정적 분석)는 소스 코드를 실행 없이 읽어 취약한 패턴을 찾고, DAST(동적 분석)는 실행 중인 앱에 요청을 보내 실제 반응을 봐요. SCA는 외부 라이브러리의 알려진 취약점을 확인해요. 시큐어 코딩과 코드 리뷰가 앞단에서 틈을 줄여요.",
                 "SAST (static analysis) reads source code without running it and flags vulnerable patterns; DAST (dynamic analysis) sends requests to the running app and watches how it really responds. SCA checks third-party libraries for known vulnerabilities. Secure coding and code review reduce cracks upstream.")),
    "glossary": [
        ("SAST", "SAST", ("도면 읽기.", "Reading the drawing."), ("짓기 전에 종이(코드)만 보고 틈을 찾아요. 빠르고 넓지만, 헛소리 깃발도 많아요.", "Finds cracks by reading the paper (code) before anything runs. Fast and wide, but plants many false flags.")),
        ("DAST", "DAST", ("벽 두드리기.", "Knocking on the wall."), ("다 지은 벽(실행 중인 앱)에 부탁을 던져 보고 빈 소리를 들어요. 늦지만 진짜예요.", "Sends requests at the built wall (the running app) and listens for hollows. Late, but real.")),
        ("SCA", "SCA", ("부품 목록 검사.", "Checking the parts list."), ('남이 만든 벽돌(라이브러리)에 알려진 틈이 있는지 목록표로 봐요. → <a href="sbom-ko.html">도구에 붙은 부품 목록표</a>', 'Checks bricks made by others (libraries) against known cracks, via the parts list. → <a href="sbom-en.html">the parts list on the tool</a>')),
        ("시큐어 코딩", "Secure coding", ("틈 없이 쌓는 법.", "Laying without cracks."), ('처음부터 틈이 안 생기게 쌓는 목수의 버릇. 남이 준 걸 믿지 않기, 열쇠 안 박기. → <a href="awareness-ko.html">도둑 수업</a>', 'The builder\'s habits that stop cracks before they start: never trust what others hand you, never nail in a key. → <a href="awareness-en.html">the thief lesson</a>')),
        ("오탐 / 미탐", "False positive / false negative", ("괜찮은 곳의 깃발 / 놓친 틈.", "A flag on a fine spot / a crack missed."), ("도면 검사는 오탐이 많고, 두드리기는 미탐이 생겨요. 둘을 같이 써서 서로 메워요.", "Reading gives many false positives; knocking can miss some. Use both so each covers the other.")),
        ("코드 리뷰", "Code review", ("동료가 옆에서 보기.", "A fellow builder looking over."), ("벽돌 쌓기 전에 다른 목수가 한 번 봐요. 사람 눈은 도구가 못 보는 '왜'를 봐요.", "Another builder looks before the brick goes in. Human eyes catch the why that tools cannot.")),
        ("인젝션", "Injection", ("쪽지 속에 숨긴 명령.", "A command hidden inside a note."), ('손님이 낸 쪽지를 그대로 읽으면 벽이 시키는 대로 움직여요. 도면 검사가 가장 잘 잡는 틈. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'Read a visitor\'s note as-is, and the wall obeys whatever it says. The crack that reading catches best. → <a href="waf-en.html">the note reviewer at the counter</a>')),
        ("펜테스트와의 차이", "Versus a pentest", ("매일 하는 검사 / 가끔 오는 도둑.", "The daily check / the occasional thief."), ('검사는 자동으로 매일, 고용한 도둑은 사람이 가끔 깊게. 서로 대신하지 못해요. → <a href="pentest-ko.html">우리가 고용한 도둑</a>', 'Checks run automatically every day; the hired thief comes rarely and digs deep. Neither replaces the other. → <a href="pentest-en.html">the thief we hired</a>')),
    ],
}
