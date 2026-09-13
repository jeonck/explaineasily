from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
COOK = "#E9B44C"


def paper(x, y, title="", stamp=True, s=1.0, body=None, rot=0):
    lines = body if body is not None else "".join(f'<rect x="12" y="{34 + i * 12}" width="{56 - (i * 13) % 24}" height="4" rx="2" fill="var(--line)"/>' for i in range(5))
    st = ('<g transform="translate(66,26) rotate(-18)"><circle r="16" fill="none" stroke="var(--bad)" stroke-width="3"/>'
          + label(0, 4, "⟦비밀|SECRET⟧", 8, "var(--bad)") + "</g>") if stamp else ""
    t = label(45, 22, title, 10, "#142033") if title else ""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="90" height="110" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            f'{t}{lines}{st}</g>')


def pigeon(x, y, s=1.0, flip=False):
    sx = -1 if flip else 1
    return (f'<g transform="translate({x},{y}) scale({sx * s},{s})"><ellipse cx="0" cy="0" rx="22" ry="12" fill="var(--stone)"/>'
            f'<circle cx="-20" cy="-8" r="8" fill="var(--stone)"/><path d="M-28 -8 l-8 3 l8 3z" fill="var(--accent)"/>'
            f'<path d="M-4 -4 L14 -26 L22 -2 Z" fill="var(--stone-dark)"/><path d="M20 4 l14 -6 l-6 12z" fill="var(--stone-dark)"/>'
            f'<circle cx="-22" cy="-10" r="1.5" fill="var(--night)"/></g>')


def mailbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="#4A5A72"/>'
            f'<rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/><path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/></g>')


BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GLASS = ('<g transform="translate(70,60)"><circle r="16" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/>'
         '<path d="M12 12 L26 26" stroke="var(--night)" stroke-width="6" stroke-linecap="round"/></g>')

# 1. 밖으로 나가면 안 되는 종이
P1 = svg(260, '<rect width="760" height="260" fill="var(--panel)"/>'
         + paper(120, 60, "⟦주민 명단|resident list⟧", rot=-4) + paper(330, 60, "⟦보물 지도|treasure map⟧", rot=3,
                 body='<path d="M20 60 q20 -20 40 0 t30 10" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="4 4"/><path d="M62 66 l8 8 M70 66 l-8 8" stroke="var(--bad)" stroke-width="3"/>')
         + paper(540, 60, "⟦비밀 편지|secret letter⟧", rot=-2)
         + label(380, 230, "⟦빨간 도장이 찍혀 있어요|each one carries a red stamp⟧", 14, "var(--muted)"))

# 2. 종이는 여러 길로 나간다
P2 = svg(300, sky(300) + small_castle(40, 100, 0.5)
         + "".join(f'<path d="M130 160 Q{x - 60} {y} {x} {y}" stroke="var(--bad)" stroke-width="2" stroke-dasharray="6 6" fill="none"/>' for x, y in ((260, 90), (420, 200), (560, 60)))
         + mailbox(300, 60, 0.8) + paper(280, 110, s=0.35) + label(300, 150, "⟦우편|mail⟧", 12, "var(--muted)")
         + person(430, 130, s=0.8, **ME, extra=BAG) + label(460, 262, "⟦가방|a bag⟧", 12, "var(--muted)")
         + pigeon(600, 60, 1.0) + paper(596, 66, s=0.3) + label(600, 110, "⟦비둘기|a pigeon⟧", 12, "var(--muted)")
         + person(620, 150, s=0.8, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + bubble(560, 90, 190, 34, "⟦앗, 잘못 보냈다!|oops, wrong letter!⟧", 13, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 285, "⟦도둑보다 실수가 훨씬 많아요|far more mistakes than thieves⟧", 13, "var(--muted)"))

# 3. DLP = 길목마다 살펴본다 (hero)
def checkpoint(x, name, ok):
    mark = ('<path d="M-10 0 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>' if ok
            else '<rect x="-30" y="-16" width="60" height="32" rx="6" fill="var(--bad)"/>' + label(0, 5, "⟦멈춰|STOP⟧", 13, "#FFF"))
    return (person(x - 40, 90, s=0.8, face=EYES, **GUARD, extra=GLASS) + paper(x + 30, 110, s=0.7, stamp=not ok)
            + f'<g transform="translate({x + 60},250)">{mark}</g>' + label(x + 20, 290, name, 13, "var(--muted)"))


P3 = svg(340, sky(340) + label(380, 40, "⟦나가는 길목|the ways out⟧", 16, "var(--ink)", cls="d")
         + checkpoint(110, "⟦우편실|mailroom⟧", False) + checkpoint(350, "⟦성문|the gate⟧", True) + checkpoint(590, "⟦비둘기집|the pigeon loft⟧", False)
         + label(380, 325, "⟦빨간 도장이나 주민번호 모양 숫자가 보이면 멈춰요|a red stamp or a number shaped like an ID: stop⟧", 13, "var(--muted)"))

# 4. 막거나, 물어보거나, 봉인한다
BLOCK = paper(80, 70, s=0.8) + '<path d="M70 60 l90 110 M160 60 l-90 110" stroke="var(--bad)" stroke-width="8" stroke-linecap="round"/>' + label(120, 220, "⟦막기|block⟧", 15, "var(--ink)", cls="d")
ASK = ('<g transform="translate(290,60)"><rect width="200" height="110" rx="10" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/>'
       + label(100, 34, "⟦정말 보낼 거예요?|Really send this?⟧", 14, "var(--ink)")
       + '<rect x="24" y="60" width="66" height="30" rx="6" fill="var(--line)"/>' + label(57, 80, "⟦아니요|No⟧", 13, "var(--ink)")
       + '<rect x="110" y="60" width="66" height="30" rx="6" fill="var(--accent)"/>' + label(143, 80, "⟦네|Yes⟧", 13, "#FFF") + "</g>"
       + label(390, 220, "⟦물어보기|ask⟧", 15, "var(--ink)", cls="d"))
SEAL = ('<g transform="translate(560,70)"><rect width="150" height="100" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 4 L75 60 L150 4" stroke="var(--line)" stroke-width="3" fill="none"/>'
        '<rect x="58" y="52" width="34" height="28" rx="5" fill="var(--night)"/><path d="M66 52 V44 a9 9 0 0 1 18 0 V52" stroke="var(--night)" stroke-width="5" fill="none"/></g>'
        + label(635, 220, "⟦봉인|seal⟧", 15, "var(--ink)", cls="d"))
P4 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>' + BLOCK + ASK + SEAL
         + label(380, 262, "⟦그리고 대장에 적어요|and it goes in the ledger⟧", 13, "var(--muted)"))

# 5. 너무 자주 멈추면 돌아서 간다
MENU = paper(70, 80, "⟦점심 메뉴|lunch menu⟧", stamp=False, s=0.8, body='<rect x="12" y="34" width="50" height="4" rx="2" fill="var(--line)"/><rect x="12" y="46" width="40" height="4" rx="2" fill="var(--line)"/>' + label(45, 80, "🍜", 22))
PHONE = ('<g transform="translate(70,40) rotate(15)"><rect x="-14" y="-24" width="28" height="48" rx="5" fill="var(--night)"/><rect x="-10" y="-18" width="20" height="34" rx="2" fill="var(--sky)"/><circle cx="0" cy="-10" r="3" fill="var(--panel)"/></g>')
P5 = svg(280, '<rect width="380" height="280" fill="var(--bad-soft)"/><rect x="380" width="380" height="280" fill="var(--panel)"/>'
         + MENU + person(200, 90, s=0.85, face=EYES, **GUARD, extra=GLASS)
         + person(60, 150, s=0.7, hat=COOK, shirt="#4A5A72", face=FROWN)
         + bubble(150, 20, 200, 34, "⟦이건 비밀 아닌데요!|this isn\'t secret!⟧", 13, "var(--panel)", "var(--bad)", "bottom")
         + label(190, 262, "⟦점심 메뉴까지 막으면 다들 돌아서 가요|block the lunch menu and people find another way⟧", 12, "var(--bad)")
         + paper(450, 70, s=0.9) + person(560, 90, s=0.85, hat=None, shirt="#4A5A72", face=EYES, extra=PHONE)
         + label(570, 262, "⟦사진으로 찍어가면 못 봐요|a photo of the page slips right past⟧", 12, "var(--muted)"))

STAMP_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="40" cy="22" r="9" fill="none" stroke="var(--bad)" stroke-width="3"/>')
PATTERN_I = icon('<rect x="8" y="22" width="48" height="20" rx="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><text x="32" y="36" text-anchor="middle" font-size="9" font-weight="700" fill="var(--accent)">123456-1••••••</text>')
GATE_I = icon('<rect x="8" y="24" width="48" height="30" fill="var(--stone-dark)"/><rect x="8" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="27" y="16" width="10" height="10" fill="var(--stone-dark)"/><rect x="46" y="16" width="10" height="10" fill="var(--stone-dark)"/><path d="M24 54 V42 a8 8 0 0 1 16 0 V54Z" fill="var(--night)"/>')

PAGE = {
    "slug": "dlp", "order": 21,
    "title": ("빨간 도장 찍힌 종이", "The Red-Stamped Paper"),
    "h1": ("<em>DLP</em>가 뭐예요?", "What is <em>DLP</em>?"),
    "sub": ("데이터 유출 방지(Data Loss Prevention)를 빨간 도장 찍힌 종이 이야기로 풀어봤어요.",
            "Data Loss Prevention, told as a story about red-stamped papers."),
    "panels": [
        {"svg": P1, "alt": ("'비밀' 빨간 도장이 찍힌 종이 세 장: 주민 명단, 보물 지도, 비밀 편지", "Three papers with a red SECRET stamp: a resident list, a treasure map, a secret letter"),
         "caption": ("밖으로 나가면 안 되는 종이가 있어요.", "Some papers must never leave the castle."),
         "small": ("주민 명단, 보물 지도, 비밀 편지. 빨간 도장이 찍혀 있어요.", "The resident list, the treasure map, the secret letter. Each carries a red stamp.")},
        {"svg": P2, "alt": ("성에서 우편함, 가방을 든 사람, 비둘기로 종이가 빠져나가고, 한 사람이 '앗, 잘못 보냈다!'", "Papers leave the castle by mailbox, in a bag, and by pigeon; someone cries oops, wrong letter"),
         "caption": ("종이는 여러 길로 나가요.", "Papers leave by many roads."),
         "small": ("우편, 가방, 비둘기… 그리고 도둑보다 실수가 훨씬 많아요.", "Mail, bags, pigeons… and far more of it is by mistake than by theft.")},
        {"svg": P3, "hero": True, "alt": ("우편실, 성문, 비둘기집 세 길목마다 돋보기를 든 경비가 종이를 살피고, 도장 찍힌 종이엔 '멈춰'", "At the mailroom, the gate and the pigeon loft a guard with a magnifying glass inspects papers; stamped ones get STOP"),
         "caption": ("DLP는 나가는 길목마다 종이를 살펴봐요.", "DLP checks every paper at every way out."),
         "small": ("빨간 도장이 있거나, 주민번호 모양 숫자가 있으면 멈춰요.", "A red stamp, or a number shaped like an ID: it stops."),
         "tricks": (3, [
             (STAMP_I, ("도장", "The stamp"), ("공개·내부·비밀", "public · internal · secret")),
             (PATTERN_I, ("숫자 모양", "Number shapes"), ("주민번호, 카드번호", "ID numbers, card numbers"), "warm"),
             (GATE_I, ("길목", "The ways out"), ("우편, 가방, 비둘기, 인쇄", "mail, bags, pigeons, printing"), "calm"),
         ])},
        {"svg": P4, "alt": ("X 표시된 종이(막기), '정말 보낼 거예요?' 창(물어보기), 자물쇠 달린 봉투(봉인)", "A crossed-out paper (block), a 'Really send this?' box (ask), an envelope with a padlock (seal)"),
         "caption": ("막거나, 물어보거나, 봉인해요.", "Block it, ask, or seal it."),
         "small": ("'정말 보낼 거예요?' 한 번 묻는 것만으로 실수 대부분이 사라져요. 그리고 대장에 적어요.", "One 'Really send this?' removes most of the mistakes. And it all goes in the ledger.")},
        {"svg": P5, "alt": ("왼쪽: 점심 메뉴를 든 요리사를 막는 경비, '이건 비밀 아닌데요!' 오른쪽: 종이를 휴대폰으로 찍는 사람", "Left: a guard stops a cook holding a lunch menu — this isn't secret! Right: someone photographs a page with a phone"),
         "caption": ("너무 자주 멈추면 다들 돌아서 가요.", "Stop people too often and they go around you."),
         "small": ("점심 메뉴까지 막으면 사람들은 다른 길을 찾아요. 그리고 도장 없는 종이나 사진으로 찍은 건 못 알아봐요.", "Block the lunch menu and people find another road. And an unstamped page, or a photo of one, slips right past.")},
    ],
    "summary": (("<b>DLP</b> = 비밀 종이에 <b>도장</b>을 찍고, 나가는 <b>길목마다</b> 살펴서 새어 나가는 걸 막는 것.",
                 "<b>DLP</b> = <b>stamp</b> the secret papers, then check <b>every way out</b> so they don't leak."),
                ("Data Loss Prevention. 도둑보다 실수를 막는 도구예요. Microsoft Purview, Google Workspace DLP, Symantec DLP 같은 것들.",
                 "Data Loss Prevention. It catches mistakes far more than thieves. Think Microsoft Purview, Google Workspace DLP, Symantec DLP.")),
    "glossary": [
        ("데이터 분류", "Classification", ("빨간 도장.", "The red stamp."), ("공개 / 내부 / 비밀. 도장을 찍어야 길목에서 알아봐요.", "Public / internal / secret. Only stamped papers get recognized at the ways out.")),
        ("민감 정보 탐지", "Pattern / fingerprint", ("숫자 모양.", "Number shapes."), ("주민번호, 카드번호처럼 모양이 정해진 것. 도장이 없어도 잡아요.", "ID and card numbers have a fixed shape, so they're caught even without a stamp.")),
        ("채널", "Channel / egress", ("나가는 길목.", "The ways out."), ("이메일, USB, 클라우드 업로드, 인쇄, 화면 공유.", "Email, USB, cloud upload, printing, screen sharing.")),
        ("엔드포인트 DLP", "Endpoint DLP", ("가방 검사.", "Checking the bag."), ('노트북 안에서 봐요. → <a href="edr-ko.html">방마다 한 마리 경비견</a>', 'Watches inside the laptop. → <a href="edr-en.html">a dog in every room</a>')),
        ("네트워크 DLP", "Network DLP", ("성문 검사.", "Checking at the gate."), ('나가는 길에서 봐요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Watches the road out. → <a href="ndr-en.html">the hallway watcher</a>')),
        ("정책", "Policy", ("뭘 어떻게.", "What, and how."), ('"비밀 도장 + 우편 = 막기", "카드번호 + 우편 = 물어보기".', '"secret stamp + mail = block", "card number + mail = ask".')),
        ("오탐", "False positive", ("점심 메뉴 막기.", "Blocking the lunch menu."), ('비밀이 아닌데 멈춘 것. 너무 잦으면 다들 돌아서 가요. → <a href="soc-ko.html">경비실의 고양이</a>', 'Stopped, but not secret. Too many and people route around you. → <a href="soc-en.html">the guard room\'s cat</a>')),
        ("그림자 길", "Shadow channels", ("사진 찍기, 개인 우편.", "Photos, personal mail."), ("살펴보지 않는 길. DLP가 못 보는 곳이에요.", "The roads nobody watches — where DLP is blind.")),
    ],
}
