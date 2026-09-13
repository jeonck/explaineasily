from _draw import *

def step(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="16" fill="var(--accent)"/>' + label(x, y + 6, str(n), 17, "#FFF")

HOUSE = ('<path d="M120 120 L380 40 L640 120 Z" fill="var(--stone-dark)"/>'
         '<rect x="140" y="120" width="480" height="160" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="6"/>'
         '<rect x="380" y="120" width="6" height="160" fill="var(--stone-dark)"/>'
         # window (left)
         '<rect x="150" y="160" width="60" height="70" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="4"/><path d="M150 195 h60 M180 160 v70" stroke="var(--stone-dark)" stroke-width="4"/>'
         # kitchen table
         '<rect x="250" y="210" width="100" height="10" rx="3" fill="#8B5E3C"/><rect x="258" y="220" width="8" height="40" fill="#8B5E3C"/><rect x="334" y="220" width="8" height="40" fill="#8B5E3C"/>'
         # safe
         '<rect x="500" y="180" width="90" height="90" rx="6" fill="var(--night)"/><circle cx="545" cy="225" r="16" fill="none" stroke="var(--stone)" stroke-width="5"/><circle cx="545" cy="225" r="4" fill="var(--accent)"/>')
PATH = '<path d="M60 250 C120 240 140 200 180 195 S 260 240 300 200 S 460 225 545 225" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
P1 = svg(300, sky(300) + HOUSE + PATH + step(180, 195, 1) + step(300, 200, 2) + step(545, 225, 3)
         + person(20, 150, s=0.85))

BLOCKS = ""
for i, (y, w, fill, txt) in enumerate((
        (30, 300, "var(--bad-soft)", "⟦전술 · 들어가기|Tactic · get in⟧"),
        (100, 420, "var(--accent-soft)", "⟦기법 · 창문으로|Technique · through a window⟧"),
        (170, 560, "var(--good-soft)", "⟦절차 · 드라이버로 창틀 열기|Procedure · pry the frame with a screwdriver⟧"))):
    x = 380 - w / 2
    BLOCKS += f'<rect x="{x}" y="{y}" width="{w}" height="56" rx="12" fill="{fill}" stroke="var(--line)" stroke-width="2"/>' + label(380, y + 35, txt, 20, cls="d")
P2 = svg(250, BLOCKS)

SHOES = "".join(f'<g transform="translate({x},{y})"><path d="M0 0 h50 a18 18 0 0 1 18 18 v8 h-80 v-14 a12 12 0 0 1 12 -12z" fill="{c}"/></g>'
                for x, y, c in ((60, 160, "var(--bad)"), (140, 150, "#4A5A72"), (100, 110, "var(--accent)"), (180, 100, "var(--good)")))
P3 = svg(240, '<rect width="380" height="240" fill="var(--good-soft)"/><rect x="380" width="380" height="240" fill="var(--bad-soft)"/>'
         + SHOES + label(150, 60, "⟦신발: 1초|shoes: 1 sec⟧", 22, cls="d")
         + person(520, 70, face=FROWN, extra=SWEAT)
         + bubble(560, 140, 180, 44, "⟦버릇을 바꾸라고?|Change my habits?!⟧", 16, "var(--panel)", "var(--bad)", "left")
         + label(570, 60, "⟦버릇: 몇 달|habits: months⟧", 22, cls="d"))

BELL = ('<path d="M180 120 c0 -30 60 -30 60 0 v30 h-60 z" fill="#E9B44C"/><rect x="176" y="150" width="68" height="8" rx="4" fill="#C9822B"/>'
        '<circle cx="210" cy="164" r="6" fill="#C9822B"/>'
        '<path d="M150 110 a60 60 0 0 1 -20 -40 M270 110 a60 60 0 0 0 20 -40" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')
WINDOW_BIG = ('<rect x="140" y="160" width="140" height="110" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="8"/>'
              '<path d="M140 215 h140 M210 160 v110" stroke="var(--stone-dark)" stroke-width="8"/>')
P4 = svg(280, '<rect width="760" height="280" fill="var(--panel)"/><rect y="270" width="760" height="10" fill="var(--stone-dark)"/>'
         + WINDOW_BIG + BELL
         + person(300, 150, hat="var(--good)", face=MASK)
         + label(520, 150, "⟦딸랑!|RING!⟧", 64, "var(--accent)", cls="d")
         + label(520, 200, "⟦변장해도 창문은 창문|a disguise is still at the window⟧", 16, "var(--muted)"))

TARGET_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="32" cy="32" r="12" fill="none" stroke="var(--bad)" stroke-width="3"/><circle cx="32" cy="32" r="4" fill="var(--bad)"/>')
WINDOW_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><path d="M12 32 h40 M32 10 v44" stroke="var(--accent)" stroke-width="3"/>')
TOOL_I = icon('<rect x="14" y="10" width="12" height="24" rx="4" fill="var(--good)"/><rect x="18" y="34" width="4" height="22" fill="var(--good)"/><rect x="30" y="8" width="20" height="10" rx="3" fill="var(--good)"/><rect x="38" y="18" width="4" height="36" fill="var(--good)"/>')

PAGE = {
    "slug": "ttp", "order": 3,
    "title": ("도둑의 버릇", "The Burglar's Habit"),
    "h1": ("<em>TTP</em>가 뭐예요?", "What are <em>TTPs</em>?"),
    "sub": ("공격 수법(Tactics, Techniques, Procedures)을 도둑의 버릇 이야기로 풀어봤어요.",
            "Tactics, Techniques and Procedures, told as a story about a burglar's habits."),
    "panels": [
        {"svg": P1, "alt": ("집 단면도 위에 창문, 부엌, 금고 순서로 이어진 점선", "A cutaway house with a dotted path from window to kitchen to safe"),
         "caption": ("도둑은 늘 같은 순서로 움직여요.", "A burglar moves the same way every time."),
         "small": ("창문 → 부엌 → 금고. 그게 버릇이에요.", "Window → kitchen → safe. That's a habit.")},
        {"svg": P2, "alt": ("전술, 기법, 절차 세 겹의 블록", "Three stacked blocks: tactic, technique, procedure"),
         "caption": ("버릇은 세 겹이에요.", "A habit has three layers."),
         "small": ("위로 갈수록 '왜', 아래로 갈수록 '정확히 어떻게'.", "The top says why, the bottom says exactly how."),
         "tricks": (3, [
             (TARGET_I, ("전술", "Tactic"), ("뭘 하려고?", "what they want")),
             (WINDOW_I, ("기법", "Technique"), ("어떤 방법으로?", "which way"), "warm"),
             (TOOL_I, ("절차", "Procedure"), ("정확히 어떻게?", "exactly how"), "calm"),
         ])},
        {"svg": P3, "alt": ("왼쪽엔 신발 더미, 오른쪽엔 땀 흘리는 나쁜 사람", "A pile of shoes on the left, a sweating bad guy on the right"),
         "caption": ("신발은 금방 바꿔요. 버릇은 못 바꿔요.", "Shoes change in a second. Habits don't."),
         "small": ('<a href="ioc-ko.html">발자국(IOC)</a>은 하루면 낡지만, 버릇은 몇 년 가요.',
                   'A <a href="ioc-en.html">footprint (IOC)</a> goes stale in a day. A habit lasts years.')},
        {"svg": P4, "hero": True, "alt": ("종이 달린 창문과 변장한 나쁜 사람, 큰 딸랑 소리", "A window with a bell, a disguised bad guy, and a big RING"),
         "caption": ("버릇을 알면 창문에 종을 달아요.", "Know the habit, hang a bell on the window."),
         "small": ("백 번 변장해도 창문으로 오면 딸랑.", "A hundred disguises, and it still rings.")},
    ],
    "summary": (("<b>TTP</b> = 나쁜 사람의 <b>버릇</b>. 버릇을 알면 백 번 변장해도 잡아요.",
                 "<b>TTPs</b> = the bad guy's <b>habits</b>. Know them and no disguise works."),
                ("전술·기법·절차. 흔적보다 훨씬 오래가서, 진짜 방어는 여기서 만들어요.",
                 "Tactics, Techniques, Procedures. They outlast any single clue, so this is where real defense is built.")),
    "glossary": [
        ("전술", "Tactic", ("하려는 것.", "The goal."), ("들어가기, 숨기, 훔치기, 도망가기 같은 큰 목표.", "Get in, hide, steal, get out — the big steps.")),
        ("기법", "Technique", ("방법.", "The method."), ("창문으로, 가짜 편지로, 열쇠를 훔쳐서.", "Through a window, with a fake letter, with a stolen key.")),
        ("절차", "Procedure", ("정확한 손놀림.", "The exact moves."), ("이 도둑만의 세세한 순서. 도둑마다 달라요.", "This burglar's specific routine. Differs per burglar.")),
        ("행동 탐지", "Behavior detection", ("창문의 종.", "The bell on the window."), ("모습이 아니라 움직임을 보고 잡는 것.", "Catching what they do, not what they look like.")),
        ("ATT&amp;CK", "ATT&amp;CK", ("버릇 백과사전.", "The habit encyclopedia."), ('세상 모든 버릇에 이름을 붙여둔 책. → <a href="attack-ko.html">백과사전 이야기</a>', 'A book that names every known habit. → <a href="attack-en.html">the encyclopedia story</a>')),
    ],
}
