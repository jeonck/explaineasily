from _draw import *


def cat(x, y, s=1.0, color="var(--stone-dark)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="26" cy="30" rx="26" ry="16" fill="{color}"/>'
            f'<circle cx="-2" cy="14" r="14" fill="{color}"/><path d="M-12 6 L-10 -8 L-2 4 Z M8 4 L12 -8 L6 6 Z" fill="{color}"/>'
            f'<path d="M50 28 q14 -10 8 -26" stroke="{color}" stroke-width="6" fill="none" stroke-linecap="round"/>'
            f'<circle cx="-6" cy="12" r="2" fill="#FFF"/><circle cx="2" cy="12" r="2" fill="#FFF"/></g>')


def bell(x, y, s=1.0, ring=False):
    waves = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
             if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{waves}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def monitor(x, y, w=110, h=80, alert=False):
    screen = ('<rect x="8" y="8" width="94" height="58" fill="var(--bad)"/>' + bell(55, 22, 0.8, True)) if alert else \
             ('<rect x="8" y="8" width="94" height="58" fill="var(--sky)"/><path d="M42 66 V40 a13 13 0 0 1 26 0 V66 Z" fill="var(--night)"/>'
              '<rect x="16" y="20" width="14" height="20" rx="7" fill="var(--night)"/><rect x="80" y="20" width="14" height="20" rx="7" fill="var(--night)"/>')
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="var(--night)"/>{screen}'
            f'<rect x="{w / 2 - 12}" y="{h}" width="24" height="10" fill="var(--stone-dark)"/></g>')


EXTRA_WINDOWS = "".join(f'<rect x="{x}" y="{y}" width="18" height="26" rx="9" fill="var(--night)"/>'
                        for x, y in ((262, 160), (300, 160), (338, 160), (462, 160), (500, 160), (262, 210), (300, 210), (462, 210), (500, 210)))
P1 = svg(300, sky(300) + castle() + EXTRA_WINDOWS
         + person(40, 150, hat="var(--good)", shirt="var(--good)", s=0.9, face=FROWN + SWEAT)
         + label(90, 130, "?", 40, "var(--accent)", cls="d") + label(130, 100, "?", 28, "var(--accent)", cls="d") + label(60, 110, "?", 24, "var(--accent)", cls="d"))

WALL = "".join(monitor(x, y) for x, y in ((60, 30), (190, 30), (320, 30), (60, 130), (190, 130), (320, 130)))
DESK = '<rect x="40" y="250" width="410" height="14" rx="4" fill="#8B5E3C"/>'
GUARDS = "".join(person(x, 180, hat="var(--good)", shirt="var(--good)", s=0.75, face=SMILE) for x in (90, 210, 330))
CLOCK = ('<circle cx="620" cy="90" r="56" fill="var(--panel)" stroke="var(--line)" stroke-width="4"/>'
         + label(620, 100, "24", 34, "var(--ink)", cls="d") + label(620, 170, "⟦밤낮으로|day and night⟧", 16, "#C9D5E6"))
P2 = svg(320, '<rect width="760" height="320" fill="var(--night)"/><rect y="270" width="760" height="50" fill="#0A1120"/>'
         + WALL + GUARDS + DESK + CLOCK)

P3 = svg(280, '<rect width="760" height="280" fill="var(--panel)"/>'
         + f'<g transform="translate(40,40) scale(1.6)">{monitor(0, 0, alert=True)}</g>'
         + person(260, 110, hat="var(--good)", shirt="var(--good)", s=0.9, face=EYES)
         + label(420, 150, "?", 56, "var(--accent)", cls="d")
         + cat(500, 60, 1.1) + label(520, 130, "⟦고양이?|a cat?⟧", 16, "var(--muted)")
         + person(600, 150, s=0.8, face=MASK) + label(624, 260, "⟦도둑?|a burglar?⟧", 16, "var(--muted)"))

BOARD = ('<rect x="200" y="30" width="400" height="200" rx="10" fill="#C9A86A"/><rect x="214" y="44" width="372" height="172" fill="#E3CFA2"/>'
         '<rect x="240" y="70" width="110" height="80" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>' + foot(295, 118, 10)
         + '<circle cx="295" cy="70" r="6" fill="var(--bad)"/>'
         '<g transform="translate(390,66) rotate(4)"><rect width="170" height="90" rx="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
         + label(85, 38, "⟦빨간 모자 조심!|Watch for red hat!⟧", 15, "var(--ink)") + label(85, 66, "⟦— 망루 친구|— your watchtower friend⟧", 12, "var(--muted)") + "</g>"
         '<circle cx="475" cy="66" r="6" fill="var(--bad)"/>')
P4 = svg(260, '<rect width="760" height="260" fill="var(--sky)"/>' + BOARD
         + person(60, 120, hat="var(--good)", shirt="var(--good)", s=0.9, face=SMILE)
         + person(640, 120, hat="var(--good)", shirt="var(--good)", s=0.9, face=EYES))

BELLS = "".join(bell(x, y, s, True) for x, y, s in ((90, 70, 0.7), (180, 40, 0.6), (270, 80, 0.8), (150, 150, 0.6), (250, 170, 0.5), (60, 170, 0.6)))
P5 = svg(260, '<rect width="760" height="260" fill="var(--bad-soft)"/>' + BELLS
         + person(380, 90, hat="var(--good)", shirt="var(--good)", s=1.1, face=FROWN + SWEAT)
         + cat(560, 150, 1.2) + label(600, 230, "⟦100번째 고양이|the 100th cat⟧", 16, "var(--muted)")
         + person(690, 170, s=0.6, face=MASK) + label(708, 250, "⟦진짜 도둑|the real one⟧", 13, "var(--bad)"))

EYE_I = icon('<path d="M6 32 Q32 8 58 32 Q32 56 6 32 Z" fill="none" stroke="var(--good)" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--good)"/>')
FUNNEL_I = icon('<path d="M8 10 H56 L38 34 V54 L26 48 V34 Z" fill="var(--accent)"/>')
RUN_I = icon('<circle cx="40" cy="12" r="6" fill="var(--bad)"/><path d="M36 20 L26 34 L34 44 L28 58 M26 34 L14 30 M34 44 L50 42" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "soc", "order": 7,
    "title": ("성의 경비실", "The Guard Room"),
    "h1": ("<em>SOC</em>이 뭐예요?", "What is a <em>SOC</em>?"),
    "sub": ("보안 관제 센터(Security Operations Center)를 성의 경비실 이야기로 풀어봤어요.",
            "The Security Operations Center, told as a story about a castle's guard room."),
    "panels": [
        {"svg": P1, "alt": ("창문이 아주 많은 성 앞에서 물음표를 띄우며 당황한 친구", "A friend looking overwhelmed in front of a castle with far too many windows"),
         "caption": ("성에는 문과 창문이 너무 많아요.", "A castle has too many doors and windows."),
         "small": ("혼자서는 다 볼 수 없어요.", "One person can't watch them all.")},
        {"svg": P2, "hero": True, "alt": ("화면 여섯 개가 걸린 어두운 방에서 세 명의 경비가 지켜보고, 벽에 24라고 적힌 시계", "Three guards in a dark room watching six screens, with a clock that says 24"),
         "caption": ("SOC는 성 안의 경비실이에요.", "A SOC is the castle's guard room."),
         "small": ("모든 문과 창문이 화면에 떠요. 밤에도, 주말에도 누군가 보고 있어요.", "Every door and window is on a screen. Someone is watching at night and on weekends too.")},
        {"svg": P3, "alt": ("빨간 화면 속 종, 바라보는 경비, 오른쪽에 고양이와 도둑 사이의 물음표", "A red screen with a bell, a guard looking, and a question mark between a cat and a burglar"),
         "caption": ("종이 울리면 가서 봐요.", "When a bell rings, they go look."),
         "small": ("진짜 도둑인지, 고양이인지.", "Is it a burglar, or just a cat?"),
         "tricks": (3, [
             (EYE_I, ("보기", "Watch"), ("화면을 계속 봐요", "keep eyes on the screens"), "calm"),
             (FUNNEL_I, ("가려내기", "Sort"), ("고양이는 버려요", "throw out the cats"), "warm"),
             (RUN_I, ("달려가기", "Run"), ("도둑이면 문을 잠가요", "if it's a burglar, lock the door")),
         ])},
        {"svg": P4, "alt": ("게시판에 발자국 카드와 '빨간 모자 조심' 쪽지가 핀으로 붙어 있고, 양쪽에 친구와 경비", "A board with a pinned footprint card and a 'watch for red hat' note, the watchtower friend and a guard on either side"),
         "caption": ("망루 친구의 쪽지를 벽에 붙여둬요.", "Notes from the watchtower go on the wall."),
         "small": ('<a href="cti-ko.html">망루 친구(CTI)</a>는 "누가 올지"를, 경비실은 "지금 누가 왔는지"를 봐요.',
                   'The <a href="cti-en.html">watchtower friend (CTI)</a> says who\'s coming. The guard room sees who\'s here now.')},
        {"svg": P5, "alt": ("종 여러 개에 둘러싸여 지친 경비, 옆의 고양이, 구석에서 몰래 들어오는 진짜 도둑", "A worn-out guard surrounded by ringing bells, a cat beside them, and the real burglar sneaking in at the edge"),
         "caption": ("종이 너무 자주 울리면 지쳐요.", "Too many bells wear the guards out."),
         "small": ("고양이 때문에 백 번 울리면, 진짜 도둑도 놓쳐요.", "A hundred cat alarms, and the real burglar walks right in.")},
    ],
    "summary": (("<b>SOC</b> = 모든 문을 <b>밤낮으로</b> 지켜보다가, 종이 울리면 달려가는 <b>경비실</b>.",
                 "<b>SOC</b> = the <b>guard room</b> that watches every door <b>day and night</b> and runs when a bell rings."),
                ("Security Operations Center. 사람, 화면, 규칙이 한 방에 모여 있어요. 어려운 건 도둑을 찾는 게 아니라, 고양이를 빨리 버리는 거예요.",
                 "Security Operations Center: people, screens and rules in one room. The hard part isn't spotting burglars — it's throwing out the cats fast.")),
    "glossary": [
        ("통합 화면", "SIEM", ("경비실의 큰 화면.", "The guard room's big screen."), ("모든 문·창문의 소식을 한 곳에 모아 보여줘요.", "Collects news from every door and window into one place.")),
        ("경보", "Alert", ("종.", "The bell."), ("뭔가 이상하다고 울리는 것. 도둑일 수도, 고양이일 수도.", "Something looks off. Could be a burglar, could be a cat.")),
        ("가려내기", "Triage", ("고양이인지 도둑인지.", "Cat or burglar?"), ("울린 종 중에 먼저 볼 것을 고르는 일.", "Deciding which bells to look at first.")),
        ("오탐", "False positive", ("고양이.", "The cat."), ('도둑인 줄 알았는데 아니었던 종. → <a href="ioc-ko.html">발자국 이야기</a>', 'A bell that wasn\'t a burglar. → <a href="ioc-en.html">the footprint story</a>')),
        ("사고 대응", "Incident response", ("달려가서 문 잠그기.", "Running to lock the door."), ("진짜 도둑일 때 하는 일. 막고, 내보내고, 고쳐요.", "What happens when it's real: stop, remove, repair.")),
        ("1선 · 2선", "Tier 1 · Tier 2", ("새 경비와 선배 경비.", "New guards and senior guards."), ("처음 종을 보는 사람과, 어려운 건 넘겨받는 사람.", "Who looks first, and who takes the hard ones.")),
        ("경보 피로", "Alert fatigue", ("백 번째 고양이.", "The hundredth cat."), ("종이 너무 많아 진짜를 놓치는 상태.", "So many bells that the real one gets missed.")),
    ],
}
