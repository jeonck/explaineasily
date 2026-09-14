from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
GLASS = '<g transform="translate(66,52)"><circle r="13" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M9 9 L22 22" stroke="var(--night)" stroke-width="5" stroke-linecap="round"/></g>'
HAMMER = '<g transform="translate(66,50) rotate(-30)"><rect x="-4" y="-22" width="8" height="44" rx="2" fill="#8B5E3C"/><rect x="-14" y="-30" width="28" height="12" rx="3" fill="var(--stone-dark)"/></g>'
CRACK = '<path d="M{x} {y} l6 14 l-8 12 l10 16 l-6 14" stroke="#0A1120" stroke-width="4" fill="none" stroke-linecap="round"/>'


def tower(x, y, w=100, h=160, crack=None, s=1.0):
    """왼쪽 위 모서리 (x,y). 흉벽은 y-20 부터."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" fill="var(--stone-dark)"/>{battlements(0, -20, w, 3, "var(--stone-dark)", 22)}'
           f'<rect x="{w / 2 - 16:.0f}" y="{h - 44}" width="32" height="44" rx="16" fill="var(--night)"/>')
    if crack:
        out += CRACK.format(x=crack[0], y=crack[1])
    return out + "</g>"


def brick(x, y, color="var(--good)", bad=False):
    mark = (f'<path d="M{x + 12} {y + 5} l16 16 M{x + 28} {y + 5} l-16 16" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>' if bad
            else f'<path d="M{x + 12} {y + 13} l6 6 l12 -12" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return f'<rect x="{x}" y="{y}" width="40" height="26" rx="3" fill="{color}"/>{mark}'


def belt(x, y, w):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="7" fill="var(--stone-dark)"/>'
            + "".join(f'<circle cx="{cx}" cy="{y + 7}" r="4" fill="var(--stone)"/>' for cx in range(x + 14, x + w - 8, 28)))


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


# 1. 옛날 방식: 탑을 다 짓고 나서야 경비가 봐요
P1 = svg(300, sky(300)
         + tower(140, 70, 100, 170, crack=(28, 60))
         + person(20, 140, s=0.75, face=SMILE, extra=HAMMER, **BUILDER) + bubble(0, 40, 130, 34, "⟦다 지었어요!|all done!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + person(300, 130, s=0.8, face=EYES, extra=GLASS, **GUARD) + bubble(250, 40, 220, 34, "⟦여기 틈이 있는데요…|there is a crack here…⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + person(600, 120, s=0.85, face=FROWN, **KING) + bubble(510, 30, 230, 34, "⟦그럼… 다 부수고 다시?|so… tear it down and start over?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦탑을 다 지은 뒤에야 경비가 처음 봐요|the guard sees the tower for the first time after it is finished⟧", 12, "var(--muted)"))

# 2. 다시 지으면 늦고, 검사를 빼면 위험해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/><path d="M380 20 V280" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + label(190, 30, "⟦다시 지어요|rebuild it⟧", 14, "var(--bad)", cls="d")
         + tower(70, 70, 90, 140, crack=(24, 50)) + '<path d="M60 60 L170 220 M170 60 L60 220" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>'
         + person(200, 120, s=0.75, face=FROWN + SWEAT, **BUILDER)
         + '<g transform="translate(290,90)"><rect width="76" height="70" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect width="76" height="16" rx="6" fill="var(--bad)"/>' + label(38, 48, "⟦몇 달|months⟧", 13, "var(--ink)", cls="d") + "</g>"
         + label(190, 250, "⟦부수고 다시 지으면 몇 달이 걸려요|tearing down and rebuilding takes months⟧", 12, "var(--ink)")
         + label(570, 30, "⟦검사를 건너뛰어요|skip the check⟧", 14, "var(--bad)", cls="d")
         + tower(440, 70, 90, 140, crack=(24, 50)) + person(560, 120, s=0.8, **THIEF) + '<path d="M556 150 l-40 -30" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(570, 250, "⟦검사를 빼먹으면 도둑이 틈을 먼저 찾아요|skip the check and the thief finds the crack first⟧", 12, "var(--ink)")
         + label(380, 285, "⟦빠르게 짓거나, 안전하게 짓거나 — 둘 중 하나만 고르던 시절|fast or safe — back when you had to pick one⟧", 11, "var(--muted)"))

# 3. 데브섹옵스 = 짓는 동안 같이 보는 목수와 경비 (hero)
P3 = svg(360, sky(360)
         + paper(40, 50, 200, 120, "⟦도면|THE DRAWING⟧", ("⟦새 탑: 문 하나|new tower: one door⟧", "⟦경비: 뒷문은 빼요|guard: no back door⟧", "⟦목수: 알았어요!|builder: got it!⟧"))
         + person(60, 190, s=0.7, face=SMILE, extra=HAMMER, **BUILDER) + person(150, 190, s=0.7, face=SMILE, extra=GLASS, **GUARD)
         + label(140, 300, "⟦도면 그릴 때부터 경비가 옆에 앉아요|the guard sits in from the first drawing⟧", 12, "var(--ink)")
         + label(500, 100, "⟦벽돌 하나 쌓을 때마다 자동으로 검사해요|every brick is checked, automatically⟧", 12, "var(--ink)", cls="d")
         + belt(300, 200, 360) + brick(330, 172) + brick(430, 172) + brick(530, 172) + brick(590, 172)
         + "".join(f'<circle cx="{cx}" cy="140" r="12" fill="var(--good)"/><path d="M{cx - 5} 140 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>' for cx in (350, 450, 550, 610))
         + tower(680, 130, 60, 84) + label(510, 250, "⟦초록 벽돌만 탑으로 가요|only green bricks reach the tower⟧", 11, "var(--muted)")
         + label(380, 335, "⟦빨리 짓고도 안전하게 — 목수와 경비가 처음부터 같이|fast and safe — builder and guard together from the very start⟧", 13, "var(--ink)", cls="d"))

# 4. 벽돌은 검사대를 차례로 지나고, 빨간 벽돌은 문에서 멈춰요
STATIONS = (("⟦도면 검사|read the drawing⟧", "var(--good)"), ("⟦부품 확인|check the parts⟧", "var(--good)"), ("⟦열쇠 찾기|look for keys⟧", "var(--good)"), ("⟦벽 두드리기|knock on the wall⟧", "var(--good)"))
P4 = svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
         + label(340, 42, "⟦벽돌마다 검사대를 차례로 지나요|every brick passes each station in turn⟧", 14, "var(--ink)", cls="d")
         + "".join(f'<rect x="{60 + i * 140}" y="80" width="100" height="56" rx="8" fill="var(--panel)" stroke="{c}" stroke-width="3"/>' + label(110 + i * 140, 113, t, 11, "var(--ink)") for i, (t, c) in enumerate(STATIONS))
         + belt(40, 200, 600) + brick(90, 172) + brick(230, 172) + brick(370, 172) + brick(560, 172, "var(--bad)", bad=True)
         + gate(690, 120, 0.6) + '<rect x="655" y="176" width="70" height="8" rx="4" fill="var(--bad)"/>'
         + label(230, 240, "⟦초록 벽돌만 지나가요|only green bricks pass⟧", 12, "var(--good)")
         + label(600, 240, "⟦빨간 벽돌은 문에서 멈춰요|a red brick stops at the gate⟧", 12, "var(--bad)")
         + label(380, 295, "⟦멈추면 목수가 바로 고쳐요 — 몇 달이 아니라 몇 분|stopped? the builder fixes it right away — minutes, not months⟧", 12, "var(--muted)"))

# 5. 결과: 빨리 지었는데 튼튼해요
P5 = svg(320, sky(320)
         + tower(110, 70, 110, 170) + shield(240, 120, 0.4)
         + person(380, 130, s=0.8, face=SMILE, extra=HAMMER, **BUILDER) + person(470, 130, s=0.8, face=SMILE, **GUARD) + person(570, 120, s=0.85, face=SMILE, **KING)
         + bubble(400, 30, 300, 36, "⟦빨리 지었는데 튼튼해요!|built fast, and it is solid!⟧", 12, "var(--panel)", "var(--good)", "bottom")
         + label(380, 266, "⟦목수는 빨리 짓고, 경비는 안심해요|the builder goes fast, the guard rests easy⟧", 13, "var(--ink)", cls="d")
         + label(380, 296, "⟦다음엔 짓기 전에 도둑 눈으로 도면을 봐요|next: look at the drawing through a thief's eyes before building⟧", 12, "var(--muted)"))

SHIFT_I = icon('<rect x="24" y="12" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="22" width="18" height="3" fill="#C9A86A"/><rect x="30" y="30" width="14" height="3" fill="#C9A86A"/><path d="M20 44 H6 M12 38 l-6 6 l6 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
BELT_I = icon('<rect x="6" y="40" width="52" height="10" rx="5" fill="var(--stone-dark)"/><rect x="20" y="20" width="24" height="16" rx="3" fill="var(--good)"/><path d="M27 28 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="22" cy="22" r="3" fill="var(--good)"/><rect x="28" y="20" width="16" height="3" fill="#142033"/><circle cx="22" cy="34" r="3" fill="var(--good)"/><rect x="28" y="32" width="14" height="3" fill="#142033"/><circle cx="22" cy="46" r="3" fill="var(--good)"/><rect x="28" y="44" width="12" height="3" fill="#142033"/>')
KEYBOX_I = icon('<rect x="10" y="22" width="44" height="32" rx="4" fill="#8B5E3C"/><path d="M10 22 h44 v-4 a22 8 0 0 0 -44 0z" fill="#5A3B22"/><rect x="26" y="34" width="12" height="12" rx="2" fill="#E9B44C"/><path d="M29 34 v-5 a3 3 0 0 1 6 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "devsecops", "order": 77,
    "title": ("짓는 동안 같이 보는 목수와 경비", "The Builder and the Guard, Side by Side"),
    "h1": ("<em>데브섹옵스</em>가 뭐예요?", "What is <em>DevSecOps</em>?"),
    "sub": ("데브섹옵스(DevSecOps)를 탑을 다 짓고 검사하는 대신, 도면 그릴 때부터 경비가 목수 옆에 앉는 이야기로 풀어봤어요.",
            "DevSecOps, told as a story about a guard who sits beside the builder from the first drawing, instead of inspecting the tower once it is finished."),
    "panels": [
        {"svg": P1, "alt": ("금 간 탑 옆에서 목수가 '다 지었어요!' 하고, 돋보기를 든 경비가 '여기 틈이 있는데요', 왕은 '그럼 다 부수고 다시?' 하고 찡그림", "Beside a cracked tower the builder says all done, the guard with a magnifying glass says there is a crack here, and the king frowns: so, tear it down and start over?"),
         "caption": ("옛날엔 탑을 다 지은 뒤에야 경비가 봤어요.", "In the old days, the guard looked only after the tower was finished."),
         "small": ('<a href="patch-ko.html">목수</a>가 몇 달 동안 탑을 다 지어요. 그제야 경비가 와서 틈을 찾아요.',
                   'The <a href="patch-en.html">builder</a> spends months finishing the tower. Only then does the guard come and find a crack.')},
        {"svg": P2, "alt": ("왼쪽: 빨간 X가 그어진 탑, 땀 흘리는 목수, '몇 달'이라 적힌 달력. 오른쪽: 금 간 탑에 도둑이 다가감", "Left: a tower crossed out in red, a sweating builder, a calendar reading months. Right: a thief creeping toward a cracked tower"),
         "caption": ("다시 지으면 늦고, 검사를 빼면 위험해요.", "Rebuilding is slow, and skipping the check is dangerous."),
         "small": ("틈을 고치려고 부수고 다시 지으면 몇 달이 걸려요. 그래서 검사를 빼먹으면 도둑이 틈을 먼저 찾아요. 둘 중 하나만 골라야 했어요.",
                   "Tearing down and rebuilding to fix a crack takes months. Skip the check instead, and the thief finds the crack first. You had to pick one.")},
        {"svg": P3, "hero": True, "alt": ("목수와 경비가 도면 앞에 나란히 앉음. 오른쪽엔 벽돌이 벨트를 타고 가며 초록 체크를 하나씩 받고 작은 탑으로 감", "The builder and the guard sit together at the drawing. On the right, bricks ride a belt, each getting a green check before reaching a small tower"),
         "caption": ("데브섹옵스는 짓는 동안 같이 보는 목수와 경비예요.", "DevSecOps is the builder and the guard working side by side while building."),
         "small": ("경비가 도면 그릴 때부터 옆에 앉아요. 벽돌 하나 쌓을 때마다 자동으로 검사해요. 그래서 빨리 짓고도 안전해요.",
                   "The guard sits in from the first drawing. Every brick is checked automatically as it is laid. So it is fast and safe at once."),
         "tricks": (4, [
             (SHIFT_I, ("도면부터 같이", "From the drawing"), ("검사를 맨 앞으로 옮겨요", "move the check to the very start"), "warm"),
             (BELT_I, ("벽돌마다 자동 검사", "Every brick, auto-checked"), ("사람이 기다리지 않아요", "no one has to wait"), "calm"),
             (LIST_I, ("부품 목록도 확인", "Check the parts list"), ("남이 만든 벽돌도 봐요", "even bricks made by others")),
             (KEYBOX_I, ("열쇠는 상자에", "Keys in the box"), ("도면에 못 박지 않아요", "never nailed to the drawing")),
         ])},
        {"svg": P4, "alt": ("벨트 위 벽돌이 네 검사대(도면 검사, 부품 확인, 열쇠 찾기, 벽 두드리기)를 차례로 지나고, 빨간 X 벽돌 하나가 성문 앞 빨간 막대에 멈춤", "Bricks on a belt pass four stations — read the drawing, check the parts, look for keys, knock on the wall — and one red X brick stops at a red bar before the gate"),
         "caption": ("벽돌은 검사대를 차례로 지나고, 빨간 벽돌은 문에서 멈춰요.", "Bricks pass each station in turn, and a red brick stops at the gate."),
         "small": ('<a href="codescan-ko.html">도면 검사</a>, <a href="sbom-ko.html">부품 확인</a>, <a href="secrets-ko.html">열쇠 찾기</a>, 벽 두드리기. 하나라도 빨간불이면 문이 닫히고, 목수가 그 자리에서 고쳐요.',
                   '<a href="codescan-en.html">Read the drawing</a>, <a href="sbom-en.html">check the parts</a>, <a href="secrets-en.html">look for keys</a>, knock on the wall. One red light and the gate closes — the builder fixes it on the spot.')},
        {"svg": P5, "alt": ("방패가 붙은 완성된 탑. 목수, 경비, 왕이 나란히 웃으며 '빨리 지었는데 튼튼해요!'", "A finished tower with a shield on it. The builder, the guard, and the king smile together: built fast, and it is solid!"),
         "caption": ("빨리 지었는데 튼튼해요.", "Built fast, and it is solid."),
         "small": ('틈을 짓기 전에 잡으면 벽돌 하나 값이에요. 다음 이야기: 짓기 전에 <a href="threatmodel-ko.html">도둑 눈으로 도면 보기</a>.',
                   'A crack caught before building costs one brick. Next: looking at the drawing <a href="threatmodel-en.html">through a thief\'s eyes</a> before building.')},
    ],
    "summary": (("<b>데브섹옵스</b> = 탑을 다 짓고 검사하는 대신, <b>도면 때부터 경비가 목수 옆에</b> 앉고 <b>벽돌마다 자동 검사</b>해서, 빨리 짓고도 안전한 방식.",
                 "<b>DevSecOps</b> = instead of inspecting a finished tower, the <b>guard sits beside the builder from the drawing</b> and <b>every brick is auto-checked</b> — fast and safe at once."),
                ("DevSecOps. 개발(Dev)·보안(Sec)·운영(Ops)을 한 팀으로 묶고, 보안 검사를 CI/CD 파이프라인 안에 자동화해 넣어요. 보안이 나중에 붙는 관문이 아니라 처음부터 함께 가는 동료가 돼요.",
                 "DevSecOps. Development, security, and operations work as one team, with security checks automated inside the CI/CD pipeline. Security stops being a gate at the end and becomes a teammate from day one.")),
    "glossary": [
        ("데브섹옵스", "DevSecOps", ("같이 짓는 목수와 경비.", "Builder and guard, building together."), ("만드는 사람, 지키는 사람, 돌리는 사람이 처음부터 한 팀이에요.", "The people who build, protect, and run it are one team from the start.")),
        ("시프트 레프트", "Shift left", ("검사를 맨 앞으로.", "The check moves to the front."), ("순서표에서 검사를 왼쪽(앞)으로 옮겨요. 앞에서 잡을수록 싸요.", "Move the check left, to the start of the plan. The earlier it is caught, the cheaper it is.")),
        ("CI/CD 파이프라인", "CI/CD pipeline", ("벽돌이 타고 가는 벨트.", "The belt the bricks ride."), ("목수가 벽돌을 올리면 검사와 쌓기가 자동으로 이어져요.", "The builder puts a brick on, and checking and laying follow automatically.")),
        ("자동 검사", "Automated scanning", ("벨트 위 검사대.", "The stations on the belt."), ('도면 보기, 두드려 보기. → <a href="codescan-ko.html">도면 검사와 두드려 보기</a>', 'Reading the drawing, knocking on the wall. → <a href="codescan-en.html">reading the drawing and knocking on the wall</a>')),
        ("IaC 스캔", "IaC scanning", ("성 짓는 순서 쪽지도 검사.", "Checking the building instructions too."), ("요즘은 성 자체도 쪽지(코드)로 지어요. 그 쪽지에 '문을 열어 둬라'가 있는지 봐요.", "Today the castle itself is built from written instructions (code). Scan them for lines like 'leave the door open'.")),
        ("컨테이너 이미지 스캔", "Container image scanning", ("포장 상자째 검사.", "Checking the whole shipping box."), ('벽돌을 상자에 담아 보내요. 상자 안에 낡은 부품이 있는지 봐요. → <a href="sbom-ko.html">부품 목록표</a>', 'Bricks ship in boxes. Check the box for old parts inside. → <a href="sbom-en.html">the parts list</a>')),
        ("시크릿 관리", "Secrets management", ("열쇠는 잠긴 상자에.", "Keys in a locked box."), ('도면에 열쇠를 못 박아 두지 않아요. → <a href="secrets-ko.html">열쇠를 벽에 못 박아 두지 않기</a>', 'Never nail a key to the drawing. → <a href="secrets-en.html">not nailing the key to the wall</a>')),
        ("게이트", "Gate", ("빨간 벽돌을 막는 문.", "The gate that stops red bricks."), ("검사에 걸린 벽돌은 탑까지 못 가요. 통과 조건을 미리 정해 둬요.", "A brick that fails a check never reaches the tower. The pass rule is set in advance.")),
    ],
}
