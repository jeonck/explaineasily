from _draw import *


def note(x, y, rot=0, w=40, h=28, lines=2, fill="var(--panel)"):
    ls = "".join(f'<rect x="7" y="{8 + i * 7}" width="{w - 14}" height="3" rx="1.5" fill="var(--line)"/>' for i in range(lines))
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect width="{w}" height="{h}" rx="3" fill="{fill}" stroke="var(--line)" stroke-width="1.5"/>{ls}</g>')


def bell(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
            '<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/><rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


# 1. 성 곳곳에서 쪽지가 날아온다
FLIGHT = "".join(f'<path d="M{x0} {y0} Q{(x0 + 560) / 2} {y0 - 60} 560 230" stroke="var(--line)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>'
                 for x0, y0 in ((110, 120), (200, 90), (290, 120), (380, 150)))
FLYING = "".join(note(x, y, r) for x, y, r in ((250, 60, -15), (330, 40, 10), (410, 70, -8), (470, 120, 14), (160, 140, 8)))
PILE = "".join(note(x, y, r) for x, y, r in ((520, 250, -12), (560, 246, 8), (600, 252, -5), (540, 270, 15), (585, 268, -10), (625, 262, 6), (505, 274, 2)))
P1 = svg(300, sky(300) + castle(40, 60, 0.75) + FLIGHT + FLYING + PILE
         + person(560, 130, hat="var(--good)", shirt="var(--good)", s=0.9, face=FROWN + SWEAT))

# 2. 쪽지마다 말이 다르다
SQUIGGLE = '<path d="M14 30 q8 -12 16 0 t16 0 t16 0 t16 0 M14 50 q8 -12 16 0 t16 0 t16 0" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>'
DIGITS = label(60, 36, "02:00", 20, "var(--ink)") + label(60, 62, "W-3 OPEN", 15, "var(--muted)")
SYMBOLS = label(60, 50, "▲ ● ■ ▲", 22, "var(--ink)")


def bignote(x, y, inner, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect width="120" height="84" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>{inner}</g>')


P2 = svg(230, '<rect width="760" height="230" fill="var(--accent-soft)"/>'
         + bignote(90, 60, SQUIGGLE, -6) + bignote(250, 50, DIGITS, 4) + bignote(410, 62, SYMBOLS, -3)
         + person(600, 70, hat="var(--good)", shirt="var(--good)", s=0.9, face=EYES)
         + label(700, 60, "?", 44, "var(--accent)", cls="d"))

# 3. 한 화면에 줄 세운다 (hero)
ROWS = ""
for i, (t, c, w) in enumerate((("01:40", "var(--good)", 200), ("01:52", "var(--good)", 140), ("02:00", "var(--accent)", 260), ("02:05", "var(--accent)", 180), ("02:10", "var(--bad)", 300))):
    y = 150 + i * 30
    ROWS += label(110, y + 6, t, 14, "#C9D5E6", "start") + f'<circle cx="175" cy="{y}" r="6" fill="{c}"/><rect x="190" y="{y - 6}" width="{w}" height="12" rx="6" fill="{c}" fill-opacity="0.55"/>'
SCREEN = ('<rect x="70" y="120" width="480" height="190" rx="10" fill="var(--night)"/>' + ROWS
          + '<rect x="290" y="310" width="40" height="12" fill="var(--stone-dark)"/>')
FUNNEL = ('<path d="M120 20 L500 20 L330 100 L290 100 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
          + "".join(note(x, y, r, 30, 20, 1) for x, y, r in ((150, 24, -10), (220, 30, 8), (300, 22, -4), (380, 32, 12), (450, 26, -8)))
          + '<path d="M310 104 L310 118" stroke="var(--accent)" stroke-width="3"/><path d="M302 112 L310 120 L318 112" stroke="var(--accent)" stroke-width="3" fill="none"/>')
P3 = svg(330, '<rect width="760" height="330" fill="var(--panel)"/>' + FUNNEL + SCREEN
         + person(600, 140, hat="var(--good)", shirt="var(--good)", s=0.9, face=SMILE))

# 4. 나란히 놓으면 도둑이 보인다
CARDS = ""
for i, (t, txt) in enumerate((("02:00", "⟦창문 열림|window opened⟧"), ("02:05", "⟦부엌 불 켜짐|kitchen light on⟧"), ("02:10", "⟦금고 방 문 열림|vault door opened⟧"))):
    x = 40 + i * 190
    CARDS += (f'<rect x="{x}" y="70" width="170" height="90" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
              + label(x + 85, 104, t, 24, "var(--accent)", cls="d") + label(x + 85, 136, txt, 15, "var(--ink)"))
LINK = '<path d="M210 115 L230 115 M400 115 L420 115" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
P4 = svg(240, '<rect width="760" height="240" fill="var(--bad-soft)"/>' + CARDS + LINK
         + '<path d="M590 115 L620 115" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
         + bell(680, 100, 1.2) + label(390, 210, "⟦한 장씩은 별거 아니에요. 셋이 이어지면 도둑이에요.|Each one is nothing. Three in a row is a burglar.⟧", 16, "var(--muted)"))

# 5. 화면은 스스로 생각하지 않는다
QUIET = ('<rect x="70" y="60" width="330" height="150" rx="10" fill="var(--stone-dark)"/>'
         + label(235, 128, "⟦규칙 0개|0 rules⟧", 26, "#E9EFF7", cls="d") + label(235, 160, "⟦…|…⟧", 26, "#C9D5E6")
         + '<rect x="215" y="210" width="40" height="12" fill="var(--stone)"/>')
P5 = svg(260, '<rect width="760" height="260" fill="var(--panel)"/>' + QUIET
         + person(440, 120, s=0.9, face=MASK)
         + '<path d="M520 200 L560 200 M540 190 L560 200 L540 210" stroke="var(--muted)" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + person(620, 110, hat="var(--good)", shirt="var(--good)", s=0.9, face=EYES + '<path d="M18 40 h24" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/>')
         + label(660, 240, "⟦규칙을 적어야 해요|someone has to write the rules⟧", 14, "var(--muted)"))

COLLECT_I = icon('<path d="M8 12 H56 L38 32 V52 L26 46 V32 Z" fill="var(--good)"/>')
SAME_I = icon('<rect x="8" y="14" width="20" height="14" rx="2" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><rect x="36" y="14" width="20" height="14" rx="2" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><rect x="8" y="38" width="48" height="14" rx="2" fill="var(--accent)"/>')
LINE_I = icon('<path d="M8 32 H56" stroke="var(--bad)" stroke-width="3"/><circle cx="16" cy="32" r="6" fill="var(--bad)"/><circle cx="32" cy="32" r="6" fill="var(--bad)"/><circle cx="48" cy="32" r="6" fill="var(--bad)"/>')

PAGE = {
    "slug": "siem", "order": 8,
    "title": ("경비실의 큰 화면", "The Big Screen"),
    "h1": ("<em>SIEM</em>이 뭐예요?", "What is a <em>SIEM</em>?"),
    "sub": ("보안 정보·이벤트 관리(Security Information and Event Management)를 경비실의 큰 화면 이야기로 풀어봤어요.",
            "Security Information and Event Management, told as a story about the guard room's big screen."),
    "panels": [
        {"svg": P1, "alt": ("성에서 쪽지들이 날아와 경비 발밑에 산더미로 쌓임", "Notes flying from the castle and piling up around a guard"),
         "caption": ("성 곳곳에서 쪽지가 날아와요.", "Notes fly in from all over the castle."),
         "small": ("문, 창문, 우체통… 하루에 수천 장.", "Doors, windows, the mailbox… thousands a day.")},
        {"svg": P2, "alt": ("낙서, 숫자, 기호로 각각 다르게 적힌 쪽지 세 장과 물음표", "Three notes written in scribbles, numbers and symbols, and a question mark"),
         "caption": ("쪽지마다 말이 달라요.", "Every note speaks a different language."),
         "small": ("한 장씩 읽으면 끝이 없어요.", "Reading them one by one never ends.")},
        {"svg": P3, "hero": True, "alt": ("깔때기로 모인 쪽지들이 큰 화면에 시간 순서 줄로 나타남", "Notes pouring through a funnel into a big screen that lists them in time order"),
         "caption": ("SIEM은 쪽지를 모아 한 화면에 줄 세워요.", "A SIEM gathers the notes and lines them up on one screen."),
         "small": ("같은 말로 고치고, 시간 순서로 늘어놔요.", "Same words, in time order."),
         "tricks": (3, [
             (COLLECT_I, ("모으기", "Gather"), ("쪽지를 전부 받아요", "take in every note"), "calm"),
             (SAME_I, ("같은 말로 고치기", "Translate"), ("낙서도 숫자도 한 가지로", "scribbles and numbers, one language"), "warm"),
             (LINE_I, ("줄 세우기", "Line up"), ("시간 순서대로", "in time order")),
         ])},
        {"svg": P4, "alt": ("02:00 창문, 02:05 부엌, 02:10 금고 방 카드가 선으로 이어지고 종이 울림", "Cards for 02:00 window, 02:05 kitchen and 02:10 vault joined by a line, then a ringing bell"),
         "caption": ("나란히 놓으면 도둑이 보여요.", "Side by side, the burglar appears."),
         "small": ('세 장이 이어지면 종이 울려요. 종은 <a href="soc-ko.html">경비실</a>로 가요.',
                   'Three in a row and the bell rings. The bell goes to the <a href="soc-en.html">guard room</a>.')},
        {"svg": P5, "alt": ("'규칙 0개'라고 뜬 조용한 화면 앞을 도둑이 지나가고, 경비는 멍하니 서 있음", "A quiet screen reading '0 rules' as a burglar walks past and a guard stands blank"),
         "caption": ("화면은 스스로 생각하지 않아요.", "The screen doesn't think for itself."),
         "small": ("규칙을 안 적어두면 도둑이 지나가도 조용해요. 규칙은 경비실 사람이 적어요.", "No rules written, no bell — even with a burglar in plain view. People write the rules.")},
    ],
    "summary": (("<b>SIEM</b> = 성 곳곳의 쪽지를 한 화면에 <b>모아 줄 세우고</b>, 규칙에 맞으면 <b>종을 울리는</b> 큰 화면.",
                 "<b>SIEM</b> = the big screen that <b>gathers and lines up</b> every note, and <b>rings a bell</b> when a rule matches."),
                ("Security Information and Event Management. 경비실(SOC)의 눈이에요. 다만 뭘 볼지는 사람이 정해요.",
                 "Security Information and Event Management. It's the guard room's eyes — but people decide what it looks for.")),
    "glossary": [
        ("로그", "Log", ("쪽지.", "A note."), ("문이 열렸다, 누가 로그인했다 — 성 곳곳이 남기는 한 줄 기록.", "A door opened, someone logged in — one line each part of the castle writes down.")),
        ("수집", "Ingestion", ("쪽지 모으기.", "Gathering the notes."), ("모든 곳에서 큰 화면으로 쪽지를 보내는 일.", "Getting every source to send its notes to the screen.")),
        ("정규화", "Normalization", ("같은 말로 고치기.", "Same language."), ("낙서와 숫자를 한 가지 형식으로. 그래야 나란히 놓을 수 있어요.", "Turning scribbles and numbers into one format so they can sit side by side.")),
        ("상관 분석", "Correlation", ("나란히 놓기.", "Side by side."), ("따로면 별거 아닌 쪽지를 이어서 도둑을 찾는 것.", "Joining harmless-looking notes until a burglar shows.")),
        ("탐지 규칙", "Detection rule", ("종이 울리는 조건.", "When the bell rings."), ('"새벽에 창문·부엌·금고가 10분 안에" 같은 문장. 사람이 적어요.', '"Window, kitchen, vault within 10 minutes at night." Written by people.')),
        ("경보", "Alert", ("종.", "The bell."), ('규칙에 걸렸을 때 경비실로 가는 것. → <a href="soc-ko.html">경비실 이야기</a>', 'What goes to the guard room when a rule matches. → <a href="soc-en.html">the guard room story</a>')),
        ("보관", "Retention", ("쪽지 서랍.", "The note drawer."), ("지난 쪽지를 몇 달치 두는 것. 나중에 발자국을 찾을 때 열어봐요.", "Keeping months of old notes, to dig for footprints later.")),
    ],
}
