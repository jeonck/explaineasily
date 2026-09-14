from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
BLUE = dict(hat="#5B8DEF", shirt="#5B8DEF")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
MAID = dict(hat=None, shirt="#7B3FA0")
TRAIL = "".join(foot(x, y, -60) for x, y in ((140, 235), (190, 218), (240, 202), (290, 186), (340, 170), (390, 154)))


def chest(x, y, s=1.0, open_lid=False):
    lid = ('<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22" transform="rotate(-40 -30 -14)"/>' if open_lid
           else '<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>{lid}</g>'


def paper(x, y, s=1.0, rot=0, text=None, smudge=False):
    tx = label(0, 24, text, 9, "#142033") if text else ""
    sm = '<path d="M-14 1 h20" stroke="var(--bad)" stroke-width="6" stroke-linecap="round" opacity="0.6"/>' if smudge else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 -8 h28 M-18 1 h18 M-18 10 h28" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{sm}{tx}</g>')


def broom(x, y):
    return (f'<g transform="translate({x},{y})"><path d="M0 0 L40 80" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M30 60 l30 40 M40 74 l24 26 M36 68 l34 22 M44 82 l14 30" stroke="#C9A86A" stroke-width="4" stroke-linecap="round"/></g>')


def glass(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="var(--sky)" fill-opacity="0.5" stroke="var(--line)" stroke-width="3"/>'
            f'<path d="M{x + 10} {y + 12} l14 -0" stroke="#FFF" stroke-width="3" stroke-linecap="round" opacity="0.7"/>')


def fingerprint(x, y, s=1.0, color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="14" fill="none" stroke="{color}" stroke-width="3"/>'
            f'<circle r="8" fill="none" stroke="{color}" stroke-width="3"/><circle r="2.5" fill="{color}"/></g>')


def tag(x, y, text, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><path d="M-34 -12 h58 l10 12 l-10 12 h-58z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<circle cx="26" cy="0" r="2.5" fill="#C9A86A"/>{label(-6, 4, text, 9, "#142033")}</g>')


def magnifier(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="var(--sky)" fill-opacity="0.4" stroke="var(--night)" stroke-width="6"/>'
            f'<path d="M14 14 l22 22" stroke="var(--night)" stroke-width="8" stroke-linecap="round"/></g>')


def candle(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-8" y="0" width="16" height="34" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M0 -18 q8 8 4 16 q-4 4 -8 0 q-4 -8 4 -16z" fill="var(--accent)"/></g>')


# 1. 도둑이 다녀간 아침 — 하녀가 쓸어 버리려 해요
P1 = svg(300, sky(300)
         + person(30, 80, s=0.8, face=FROWN, **GUARD) + TRAIL + chest(470, 195, 1.2, open_lid=True)
         + paper(420, 120, 0.7, rot=-20) + label(470, 250, "⟦열린 상자와 발자국|an open chest and footprints⟧", 11, "var(--muted)")
         + person(600, 110, s=0.85, face=SMILE, **MAID) + broom(655, 150)
         + bubble(500, 30, 240, 34, "⟦제가 다 쓸어 놓을게요!|I\'ll sweep it all up!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 290, "⟦쓸어 버리면 어떻게 들어왔는지 영영 몰라요|sweep it away, and we never learn how he got in⟧", 12, "var(--ink)"))

# 2. 잘못 만지면 — 덮이고, 고쳐지고, 아무도 안 믿어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + foot(100, 150, -60) + foot(150, 130, -60) + foot(120, 140, 20, "var(--good)") + foot(165, 120, 20, "var(--good)")
         + label(130, 225, "⟦우리 발자국이 덮어요|our own prints cover his⟧", 11, "var(--ink)")
         + paper(380, 120, 1.3, smudge=True) + label(380, 225, "⟦일지에 손을 대요|the log gets touched up⟧", 11, "var(--ink)")
         + person(600, 100, s=0.8, face=FROWN, **KING) + bubble(530, 30, 200, 34, "⟦이게 진짜예요?|is this even real?⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(630, 225, "⟦아무도 안 믿어요|nobody believes it⟧", 11, "var(--bad)")
         + label(380, 280, "⟦한 번 흐트러진 발자국은 다시 못 만들어요|a footprint once disturbed can never be made again⟧", 12, "var(--ink)", cls="d"))

# 3. 굳혀서 보관하기 (hero)
P3 = svg(360, sky(360)
         + '<rect x="70" y="150" width="100" height="90" rx="6" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3" stroke-dasharray="8 5"/>' + foot(120, 205, -60)
         + label(120, 270, "⟦그대로 굳혀요|set it as it is⟧", 11, "var(--ink)")
         + '<path d="M185 195 H245" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/><path d="M238 189 l10 6 l-10 6z" fill="var(--muted)"/>'
         + glass(270, 120, 180, 130) + foot(360, 205, -60) + fingerprint(420, 150, 1.0) + tag(316, 148, "⟦누가·언제|who·when⟧", 1.0, -12)
         + label(360, 270, "⟦유리 상자 + 지문 + 꼬리표|glass box + fingerprint + tag⟧", 11, "var(--ink)")
         + person(540, 110, s=0.9, face=EYES, **BLUE) + magnifier(625, 160, 1.0)
         + label(600, 250, "⟦만지지 않고 들여다봐요|look, never touch⟧", 11, "var(--muted)")
         + label(380, 310, "⟦그대로 굳혀서, 지문 찍고, 꼬리표를 달아요|set it, fingerprint it, tag it⟧", 13, "var(--ink)", cls="d")
         + label(380, 342, "⟦진짜 발자국은 아무도 못 만져요 — 보는 건 복사본이에요|nobody touches the real print — we study a copy⟧", 12, "var(--muted)"))

# 4. 시계에 꿰기 — 타임라인
EVENTS = ((140, "⟦밤 11시|11 pm⟧", "⟦가짜 편지|fake letter⟧"), (300, "⟦11시 30분|11:30 pm⟧", "⟦복도 발자국|hall footprints⟧"),
          (460, "⟦자정|midnight⟧", "⟦상자 열림|chest opened⟧"), (620, "⟦12시 20분|12:20 am⟧", "⟦뒷문으로 나감|out the back door⟧"))
P4 = svg(320, sky(320)
         + '<rect x="60" y="30" width="640" height="210" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="60" y="30" width="640" height="28" rx="8" fill="#C9A86A"/>'
         + label(380, 49, "⟦도둑의 밤 — 시간 순서로|THE THIEF\'S NIGHT, IN ORDER⟧", 12, "#142033", cls="d")
         + '<path d="M100 150 H660" stroke="#C9A86A" stroke-width="4" stroke-linecap="round"/>'
         + "".join(f'<circle cx="{x}" cy="150" r="9" fill="var(--bad)"/>' + label(x, 185, t, 11, "#142033", cls="d") + label(x, 205, w, 11, "#142033") for x, t, w in EVENTS)
         + '<g transform="translate(140,100)"><rect x="-22" y="-14" width="44" height="30" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/><path d="M-22 -14 l22 16 l22 -16" stroke="#C9A86A" stroke-width="2" fill="none"/></g>'
         + foot(292, 104, -60, "#7A5236") + foot(312, 98, -60, "#7A5236")
         + chest(460, 108, 0.8, open_lid=True)
         + '<g transform="translate(620,100)"><rect x="-16" y="-24" width="32" height="48" rx="3" fill="#8B5E3C"/><circle cx="8" cy="2" r="3" fill="#E9B44C"/></g>'
         + candle(690, 70, 0.7)
         + label(380, 275, "⟦발자국 하나하나를 시계에 맞춰 줄로 꿰어요|every print, strung on the clock in order⟧", 12, "var(--ink)", cls="d")
         + label(380, 303, "⟦촛불처럼 사라지는 것부터 먼저 — 그러면 이야기가 돼요|the candle-like things first — then it becomes a story⟧", 12, "var(--muted)"))

# 5. 재판에서도, 배우기에도
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(60, 100, s=0.85, face=SMILE, **KING) + glass(160, 120, 120, 80) + foot(225, 170, -60) + fingerprint(262, 140, 0.7) + tag(188, 134, "⟦누가·언제|who·when⟧", 0.8, -12)
         + label(190, 240, "⟦재판에서 증거로|as evidence in court⟧", 12, "var(--ink)")
         + '<rect x="430" y="50" width="200" height="140" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="430" y="50" width="200" height="26" rx="8" fill="#C9A86A"/>' + label(530, 68, "⟦배우기|LEARN⟧", 12, "#142033", cls="d")
         + label(444, 100, "⟦어디로: 서쪽 창문|where: west window⟧", 11, "#142033", "start") + label(444, 126, "⟦무엇을: 명부 한 장|what: one roster page⟧", 11, "#142033", "start") + label(444, 152, "⟦다음엔: 창문 잠그기|next: lock the window⟧", 11, "#142033", "start")
         + person(660, 110, s=0.8, face=SMILE, **GUARD)
         + label(560, 240, "⟦경비실 순서표의 마지막 칸|the book\'s last step⟧", 12, "var(--ink)")
         + label(380, 288, "⟦발자국이 그대로여야 재판도, 배우기도 돼요|only an untouched print works in court — and in the lesson⟧", 12, "var(--ink)", cls="d"))

CAST_I = icon('<rect x="10" y="12" width="44" height="40" rx="4" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3" stroke-dasharray="6 4"/><ellipse cx="32" cy="36" rx="7" ry="11" fill="#7A5236"/><ellipse cx="32" cy="20" rx="5" ry="4" fill="#7A5236"/>')
PRINT_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="12" fill="none" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="4" fill="var(--accent)"/>')
TAG_I = icon('<path d="M8 22 h36 l12 10 l-12 10 h-36z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="44" cy="32" r="3" fill="#C9A86A"/><path d="M14 28 h18 M14 36 h12" stroke="#C9A86A" stroke-width="2.5" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 18 v14 l9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="10" cy="54" r="4" fill="var(--bad)"/><circle cx="54" cy="54" r="4" fill="var(--bad)"/><path d="M14 54 h36" stroke="var(--bad)" stroke-width="2"/>')

PAGE = {
    "slug": "forensics", "order": 82,
    "title": ("발자국을 굳혀서 보관하기", "Setting the Footprint in Plaster"),
    "h1": ("<em>디지털 포렌식</em>이 뭐예요?", "What is <em>Digital Forensics</em>?"),
    "sub": ("디지털 포렌식(Digital Forensics)을 도둑이 남긴 발자국을 그대로 굳혀서 유리 상자에 보관하는 이야기로 풀어봤어요.",
            "Digital forensics, told as a story about setting a thief\'s footprint in plaster and keeping it in a glass box."),
    "panels": [
        {"svg": P1, "alt": ("아침, 열린 상자까지 이어진 발자국. 하녀가 빗자루를 들고 '제가 다 쓸어 놓을게요!' 하고, 경비는 얼굴을 찌푸림", "Morning: footprints lead to an open chest. The maid holds a broom — I\'ll sweep it all up! — and the guard frowns"),
         "caption": ("도둑이 다녀간 아침이에요. 발자국이 상자까지 이어져요.", "The morning after a thief. Footprints lead to the chest."),
         "small": ('하녀는 치우려고 해요. 그런데 <a href="ioc-ko.html">발자국</a>을 쓸어 버리면 도둑이 어떻게 들어왔는지 영영 몰라요.', 'The maid wants to tidy up. But sweep the <a href="ioc-en.html">footprints</a> away, and we never learn how he got in.')},
        {"svg": P2, "alt": ("초록 발자국이 도둑 발자국 위에 찍히고, 일지에 빨간 지운 자국이 있고, 왕이 '이게 진짜예요?' 하고 찌푸림", "Green footprints stamped over the thief\'s, a red smudge on the log, and the king frowning: is this even real?"),
         "caption": ("잘못 만지면 세 가지가 깨져요. 덮이고, 고쳐지고, 아무도 안 믿어요.", "Touch it wrong and three things break: it gets covered, it gets edited, and nobody believes it."),
         "small": ('우리 발자국이 도둑 발자국을 덮어요. <a href="log-ko.html">일지</a>에 손을 대면 "고친 거 아니야?" 소리를 들어요. 한 번 흐트러지면 다시 못 만들어요.', 'Our own prints cover the thief\'s. Touch the <a href="log-en.html">log</a>, and someone asks "didn\'t you edit that?" Once disturbed, it can never be made again.')},
        {"svg": P3, "hero": True, "alt": ("발자국을 점선 틀 안에 그대로 굳히고, 유리 상자에 넣어 지문과 '누가·언제' 꼬리표를 달고, 파란 모자 친구가 돋보기로 만지지 않고 들여다봄", "A footprint set in a dashed mold, placed in a glass box with a fingerprint and a who·when tag, while a blue-hat friend studies it through a magnifier without touching"),
         "caption": ("디지털 포렌식은 발자국을 그대로 굳혀서 보관하는 거예요.", "Digital forensics is setting the footprint as it is, and keeping it."),
         "small": ("굳히고, 지문 찍고, 꼬리표 달아요. 진짜 발자국은 아무도 못 만져요 — 들여다보는 건 복사본이에요.", "Set it, fingerprint it, tag it. Nobody touches the real print — what we study is a copy."),
         "tricks": (4, [
             (CAST_I, ("그대로 굳히기", "Set it as it is"), ("한 톨도 안 바뀌게 복사", "a copy, not a grain changed"), "warm"),
             (PRINT_I, ("지문 찍기", "Fingerprint it"), ("하나라도 바뀌면 지문이 달라요", "change anything, the print changes")),
             (TAG_I, ("꼬리표", "Tag it"), ("누가 언제 만졌는지 다 적어요", "who touched it, and when")),
             (CLOCK_I, ("시계에 꿰기", "String it on the clock"), ("순서가 곧 이야기", "the order is the story"), "calm"),
         ])},
        {"svg": P4, "alt": ("종이 위의 시간 줄: 밤 11시 가짜 편지 → 11시 30분 복도 발자국 → 자정 상자 열림 → 12시 20분 뒷문으로 나감. 구석에 촛불", "A timeline on paper: 11 pm fake letter → 11:30 hall footprints → midnight chest opened → 12:20 out the back door. A candle in the corner"),
         "caption": ("발자국 하나하나를 시계에 맞춰 줄로 꿰어요.", "Every print gets strung on the clock, in order."),
         "small": ('<a href="phishing-ko.html">가짜 편지</a>, 복도 발자국, 열린 상자, 뒷문. 촛불처럼 금방 사라지는 것부터 먼저 굳혀요. 줄로 꿰면 이야기가 돼요.', 'The <a href="phishing-en.html">fake letter</a>, the hall prints, the open chest, the back door. Set the candle-like things first — the ones that fade fast. Strung together, it becomes a story.')},
        {"svg": P5, "alt": ("왼쪽: 왕이 유리 상자 속 굳힌 발자국을 봄 — 재판에서 증거로. 오른쪽: 배우기 종이에 어디로·무엇을·다음엔 적히고 경비가 웃음", "Left: the king looks at the set print in its glass box — evidence in court. Right: a lesson page lists where, what, and next; the guard smiles"),
         "caption": ("굳힌 발자국은 재판에서도, 배우기에도 쓰여요.", "The set print serves in court — and in the lesson."),
         "small": ('꼬리표가 끊기지 않아야 왕이 믿어요. 그리고 <a href="incident-ko.html">순서표</a>의 마지막 칸 "배우기"는 이 발자국으로 채워요. 굳히는 데는 시간이 걸려요 — 그 사이 도둑은 이미 갔고요.',
                   'The king believes it only if the tag chain is unbroken. And the last step of the <a href="incident-en.html">book</a>, "learn", is filled from this print. Setting it takes time — and by then, the thief is long gone.')},
    ],
    "summary": (("<b>디지털 포렌식</b> = 도둑이 남긴 발자국·일지를 <b>그대로 굳혀서</b>(복사) <b>지문 찍고 꼬리표 달아</b> 보관하고, <b>시계에 꿰어</b> 이야기로 만드는 일. 재판에도, 배우기에도 써요.",
                 "<b>Digital forensics</b> = <b>set the thief\'s prints and logs as they are</b> (a copy), <b>fingerprint and tag</b> them, and <b>string them on the clock</b> into a story — for court, and for the lesson."),
                ("Digital Forensics. 디스크·메모리·로그를 변조 없이 이미지로 떠서 해시로 무결성을 증명하고, 관리 연속성을 기록한 뒤 타임라인으로 재구성해요. 법적 증거와 사고 대응의 교훈 도출에 쓰여요.",
                 "Imaging disks, memory, and logs without alteration, proving integrity with hashes, recording chain of custody, then reconstructing a timeline. Used as legal evidence and to draw lessons in incident response.")),
    "glossary": [
        ("포렌식", "Forensics", ("발자국 굳혀서 보관.", "Setting and keeping the print."), ("도둑이 남긴 것을 손대지 않고 보관하고, 순서대로 읽어 내는 일.", "Keeping what the thief left untouched, and reading it in order.")),
        ("증거 보전", "Evidence preservation", ("빗자루 치우기.", "Putting the broom away."), ('쓸기 전에 굳혀요. 발자국은 → <a href="ioc-ko.html">남겨진 발자국</a>', 'Set it before anyone sweeps. The prints → <a href="ioc-en.html">the footprint left behind</a>')),
        ("디스크 이미지", "Disk image", ("그대로 굳힌 복사본.", "The copy set in plaster."), ("상자 속 종이를 한 톨도 안 바꾸고 통째로 떠요. 들여다보는 건 이 복사본이에요.", "The whole chest, copied without changing a grain. This copy is what gets studied.")),
        ("해시", "Hash", ("지문.", "The fingerprint."), ('굳힌 것에 지문을 찍어 두면, 하나라도 바뀌었을 때 바로 알아요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>', 'Stamp a fingerprint on the set copy, and any change shows at once. → <a href="hashing-en.html">a fingerprint on everything</a>')),
        ("관리 연속성", "Chain of custody", ("누가·언제 꼬리표.", "The who·when tag."), ("누가 언제 받아서 누구에게 넘겼는지 빠짐없이. 한 칸이라도 비면 왕이 안 믿어요.", "Who received it when, and handed it to whom, with no gaps. One blank, and the king won\'t believe it.")),
        ("타임라인", "Timeline", ("시계에 꿰기.", "Stringing it on the clock."), ('발자국·일지·편지를 시간 순서로. → <a href="log-ko.html">성 곳곳의 한 줄 일지</a>', 'Prints, logs, and letters in time order. → <a href="log-en.html">the one-line log everywhere</a>')),
        ("메모리 포렌식", "Memory forensics", ("촛불부터.", "The candle first."), ("불을 끄면 사라지는 것이 있어요. 그건 상자보다 먼저 굳혀요.", "Some things vanish when the flame goes out. Set those before the chest.")),
        ("사고 대응", "Incident response", ("순서표의 마지막 칸.", "The book\'s last step."), ('굳힌 발자국으로 "배우기"를 채워요. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'The set print fills in "learn". → <a href="incident-en.html">the book for when a thief gets in</a>')),
    ],
}
