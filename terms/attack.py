from _draw import *

BOOK = ('<path d="M200 260 L560 260 L600 290 L160 290 Z" fill="var(--stone-dark)"/>'
        '<path d="M120 90 Q250 70 380 100 L380 250 Q250 220 120 240 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
        '<path d="M640 90 Q510 70 380 100 L380 250 Q510 220 640 240 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
        '<rect x="377" y="98" width="6" height="152" fill="var(--stone-dark)"/>'
        + "".join(f'<rect x="420" y="{y}" width="{w}" height="6" rx="3" fill="var(--line)"/>' for y, w in ((130, 160), (150, 190), (170, 140), (190, 180), (210, 120)))
        + label(250, 150, "⟦도둑 수법|Burglar Tricks⟧", 30, cls="d") + label(250, 190, "⟦백과사전|Encyclopedia⟧", 30, cls="d")
        + '<g transform="translate(560,60) rotate(-12)"><rect x="-50" y="-18" width="100" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/>'
        + label(0, 8, "⟦무료|FREE⟧", 22, "var(--accent)") + "</g>")
P1 = svg(300, sky(300) + BOOK)

COLS = (("⟦들어가기|Get in⟧", 4), ("⟦숨기|Hide⟧", 5), ("⟦돌아다니기|Move around⟧", 3), ("⟦훔치기|Steal⟧", 4), ("⟦도망가기|Get out⟧", 3))
COL_W, GAP, X0 = 130, 14, 40


def matrix(cells=None):
    """cells: {(col, row): 'good'|'bad'} 로 칠할 칸. 없으면 회색 표."""
    out = ""
    for c, (name, n) in enumerate(COLS):
        x = X0 + c * (COL_W + GAP)
        out += f'<rect x="{x}" y="30" width="{COL_W}" height="40" rx="8" fill="var(--night)"/>' + label(x + COL_W / 2, 56, name, 15, "#FFF")
        for r in range(n):
            y = 84 + r * 44
            tone = (cells or {}).get((c, r))
            fill = {"good": "var(--good)", "bad": "var(--bad)"}.get(tone, "var(--line)")
            out += f'<rect x="{x}" y="{y}" width="{COL_W}" height="34" rx="6" fill="{fill}"/>'
    return out


P2 = svg(320, '<rect width="760" height="320" fill="var(--panel)"/>' + matrix())

PEOPLE = (person(90, 100, hat="var(--good)", shirt="var(--good)", face=SMILE),
          person(340, 100, hat="var(--accent)", shirt="#4A5A72", face=SMILE),
          person(590, 100, hat="var(--stone-dark)", shirt="var(--bad)", face=SMILE))
P3 = svg(260, sky(260) + "".join(PEOPLE)
         + bubble(70, 30, 120, 40, "T1566", 20, "var(--panel)", "var(--good)", "bottom")
         + bubble(320, 30, 120, 40, "T1566", 20, "var(--panel)", "var(--accent)", "bottom")
         + bubble(570, 30, 120, 40, "T1566", 20, "var(--panel)", "var(--stone-dark)", "bottom")
         + label(120, 240, "⟦서울|Seoul⟧", 15, "var(--muted)") + label(370, 240, "⟦베를린|Berlin⟧", 15, "var(--muted)") + label(620, 240, "⟦상파울루|São Paulo⟧", 15, "var(--muted)"))

FILLED = {(c, r): "good" for c, (_, n) in enumerate(COLS) for r in range(n)}
for key in ((0, 1), (2, 2), (3, 0), (4, 2)):
    FILLED[key] = "bad"
P4 = svg(340, '<rect width="760" height="340" fill="var(--panel)"/>' + matrix(FILLED)
         + '<rect x="40" y="296" width="18" height="18" rx="4" fill="var(--good)"/>' + label(66, 310, "⟦막았어요|covered⟧", 15, "var(--muted)", "start")
         + '<rect x="190" y="296" width="18" height="18" rx="4" fill="var(--bad)"/>' + label(216, 310, "⟦구멍이에요|a gap⟧", 15, "var(--muted)", "start"))

COL_I = icon('<rect x="20" y="6" width="24" height="12" rx="3" fill="var(--night)"/><rect x="20" y="22" width="24" height="10" rx="2" fill="var(--bad)"/><rect x="20" y="35" width="24" height="10" rx="2" fill="var(--bad)"/><rect x="20" y="48" width="24" height="10" rx="2" fill="var(--bad)"/>')
CELL_I = icon('<rect x="8" y="22" width="48" height="20" rx="4" fill="var(--accent)"/><text x="32" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="#FFF">T1566</text>')

PAGE = {
    "slug": "attack", "order": 4,
    "title": ("도둑 백과사전", "The Burglar Encyclopedia"),
    "h1": ("<em>ATT&amp;CK</em>이 뭐예요?", "What is <em>ATT&amp;CK</em>?"),
    "sub": ("MITRE ATT&amp;CK, 공격 기법 사전을 도둑 백과사전 이야기로 풀어봤어요.",
            "MITRE ATT&amp;CK, the catalog of attacker techniques, told as a story about an encyclopedia."),
    "panels": [
        {"svg": P1, "alt": ("받침대 위에 펼쳐진 커다란 책, 무료 도장", "A big open book on a stand with a FREE stamp"),
         "caption": ("나쁜 사람들의 수법을 다 모은 책이에요.", "It's a book of every trick bad guys use."),
         "small": ("MITRE라는 곳이 만들었고, 누구나 공짜로 봐요.", "A group called MITRE keeps it, and anyone can read it for free.")},
        {"svg": P2, "alt": ("다섯 열로 된 표, 열마다 여러 칸", "A five-column table with several cells in each column"),
         "caption": ("책 속은 커다란 표예요.", "Inside, it's one big table."),
         "small": ("맨 위 칸은 '뭘 하려고', 아래 칸들은 '어떤 방법으로'.", "The top row says what they want; the cells below say how."),
         "tricks": (2, [
             (COL_I, ("열 = 전술", "Column = tactic"), ("14개", "14 of them")),
             (CELL_I, ("칸 = 기법", "Cell = technique"), ("200개 넘게", "200+ of them"), "warm"),
         ])},
        {"svg": P3, "hero": True, "alt": ("서울, 베를린, 상파울루의 세 사람이 모두 T1566이라고 말함", "Three people in Seoul, Berlin and São Paulo all saying T1566"),
         "caption": ("온 세상이 같은 이름으로 불러요.", "The whole world uses the same names."),
         "small": ("'가짜 편지'는 어디서나 T1566. 번역이 필요 없어요.", "'Fake letter' is T1566 everywhere. Nothing gets lost in translation.")},
        {"svg": P4, "alt": ("초록과 빨강으로 칠해진 표", "The same table painted green and red"),
         "caption": ("우리 성 지도에 칠해봐요.", "Paint it for your own castle."),
         "small": ("막은 칸은 초록, 구멍은 빨강. 어디를 고칠지 한눈에 보여요.", "Green where you're covered, red where you're not. Now you know where to work.")},
    ],
    "summary": (("<b>ATT&amp;CK</b> = 나쁜 사람들의 수법을 모아 <b>이름 붙인</b> 공짜 사전.",
                 "<b>ATT&amp;CK</b> = a free dictionary that <b>names</b> every known bad-guy trick."),
                ("Adversarial Tactics, Techniques &amp; Common Knowledge. 상상한 게 아니라 실제로 관찰된 수법만 실려요.",
                 "Adversarial Tactics, Techniques &amp; Common Knowledge. Only tricks actually seen in the wild make it in.")),
    "glossary": [
        ("MITRE", "MITRE", ("책을 만드는 곳.", "The keeper of the book."), ("미국의 비영리 연구기관. 2013년부터 만들었어요.", "A US non-profit research group. Started the book in 2013.")),
        ("전술", "Tactic", ("표의 열.", "A column."), ('"뭘 하려고" — 들어가기, 숨기, 훔치기. → <a href="ttp-ko.html">버릇 이야기</a>', 'The "what for" — get in, hide, steal. → <a href="ttp-en.html">the habit story</a>')),
        ("기법", "Technique", ("표의 칸.", "A cell."), ('"어떤 방법으로". 칸마다 T로 시작하는 번호가 있어요.', 'The "how". Each has a number starting with T.')),
        ("T1566", "T1566", ("가짜 편지의 번호.", "The number for fake letters."), ("어른들은 피싱(Phishing)이라고 불러요.", "Grown-ups call it phishing.")),
        ("내비게이터", "ATT&amp;CK Navigator", ("색칠 도구.", "The paint tool."), ("표에 초록·빨강을 칠하는 무료 웹 앱.", "A free web app for painting the table green and red.")),
    ],
}
