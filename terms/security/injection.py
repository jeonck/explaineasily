from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
KEEPER = dict(hat="#E9B44C", shirt="#7B3FA0")                     # 장부 담당
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)


def counter(x, y, s=1.0, clerk_face=SMILE):
    """성벽에 난 창구. 안에 직원. 폭 ±90, 높이 y-138..y+80."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-90" y="-120" width="180" height="200" fill="var(--stone-dark)"/>'
            f'{battlements(-90, -138, 180, 4, "var(--stone-dark)", 20)}'
            f'<rect x="-56" y="-80" width="112" height="90" rx="6" fill="var(--sky)"/><rect x="-62" y="10" width="124" height="12" rx="3" fill="{WOOD}"/>'
            f'{person(-30, -74, s=0.7, face=clerk_face, **CLERK)}{label(0, -96, "⟦창구|COUNTER⟧", 13, "#F5E6B8", cls="d")}</g>')


def note(x, y, lines, s=1.0, rot=0, bad_from=None, torn=False):
    """쪽지. 폭 150, 높이 20 + 16×줄 수."""
    rows = "".join(label(8, 24 + i * 16, t, 11, ("var(--bad)" if bad_from is not None and i >= bad_from else "#142033"), "start") for i, t in enumerate(lines))
    tear = '<path d="M0 0 l12 10 l-10 12 l12 10 l-10 12 l12 10 l-10 12" stroke="var(--bad)" stroke-width="4" fill="none"/>' if torn else ""
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="150" height="{20 + len(lines) * 16}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{rows}{tear}</g>'


def ledger(x, y, s=1.0, rows=3):
    lines = "".join(f'<path d="M14 {34 + i * 14} h{70 - (i % 2) * 20}" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>' for i in range(rows))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="110" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="110" height="22" rx="4" fill="#C9A86A"/>'
            f'{label(55, 16, "⟦장부|LEDGER⟧", 11, "#142033", cls="d")}{lines}</g>')


def chest(x, y, s=1.0, lock=False, open_lid=False):
    lid = (f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22" transform="rotate(-35 -30 -14)"/>' if open_lid else '<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>')
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    gold = '<circle cx="-10" cy="-10" r="6" fill="#E9B44C"/><circle cx="4" cy="-14" r="6" fill="#E9B44C"/><circle cx="16" cy="-8" r="6" fill="#E9B44C"/>' if open_lid else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>{lid}{gold}{lk}</g>'


def form(x, y, s=1.0):
    """칸이 나뉜 주문표: 위는 인쇄된 명령, 아래는 손님 말 칸."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="220" height="130" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'{label(110, 24, "⟦명령: 사과 (   )개 주기|order: give (   ) apples⟧", 11, "#142033")}'
            f'<path d="M14 36 h192" stroke="#C9A86A" stroke-width="2"/>'
            f'{label(110, 56, "⟦손님 말 칸|customer box⟧", 10, "var(--good)")}'
            f'<rect x="14" y="64" width="192" height="52" rx="4" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
            f'{label(110, 86, "⟦3, 그리고 금고도 열어|3, and open the vault⟧", 10, "var(--bad)")}'
            f'{label(110, 106, "⟦← 전부 그냥 글자예요|← all just words⟧", 9, "#142033")}</g>')


def sieve(x, y, s=1.0):
    holes = "".join(f'<circle cx="{cx}" cy="{cy}" r="3" fill="var(--sky)"/>' for cx in (-16, 0, 16) for cy in (-12, 0, 12))
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="34" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="4"/>{holes}'
            f'<rect x="34" y="-5" width="30" height="10" rx="5" fill="{WOOD}"/></g>')


ARROW = lambda x1, x2, y, color="var(--accent)": f'<path d="M{x1} {y} L{x2} {y}" stroke="{color}" stroke-width="3" stroke-dasharray="8 6"/><path d="M{x2} {y} l-12 -7 v14z" fill="{color}"/>'

# 1. 창구 직원은 손님 쪽지를 읽고 장부 담당에게 그대로 전해요
P1 = svg(300, sky(300)
         + person(40, 130, s=0.75, **ME) + label(66, 232, "⟦손님|customer⟧", 11, "var(--muted)")
         + counter(200, 150) + note(300, 90, ("⟦사과 3개 주세요|3 apples please⟧",), 0.9)
         + ARROW(300, 500, 175)
         + person(510, 110, s=0.85, face=SMILE, **KEEPER) + ledger(590, 120, 0.9) + label(600, 232, "⟦장부 담당|the ledger keeper⟧", 11, "var(--muted)")
         + label(300, 255, "⟦창구 직원은 쪽지를 그대로 전해요|the clerk passes the note along as-is⟧", 12, "var(--ink)")
         + label(380, 282, "⟦쪽지에 적힌 대로 장부에 적어요|whatever the note says goes into the ledger⟧", 12, "var(--muted)"))

# 2. 도둑이 쪽지에 '그리고 금고도 열어 줘' 를 끼워 써요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(40, 110, s=0.8, **THIEF) + label(68, 232, "⟦도둑|thief⟧", 11, "var(--bad)")
         + note(105, 45, ("⟦사과 3개 주세요|3 apples please⟧", "⟦그리고 금고도 열어 줘|and open the vault too⟧"), 0.9, rot=-4, bad_from=1)
         + counter(330, 150, 0.9) + ARROW(415, 490, 175)
         + person(500, 110, s=0.8, face=EYES, **KEEPER) + chest(640, 160, 1.4, open_lid=True) + label(640, 225, "⟦금고가 열렸어요|the vault opened⟧", 12, "var(--bad)")
         + label(330, 250, "⟦직원은 손님 말과 명령을 구분 못 해요|the clerk can\'t tell a request from an order⟧", 12, "var(--ink)")
         + label(380, 295, "⟦쪽지에 끼워 넣은 한 줄이 금고를 열어요|one line slipped into a note opens the vault⟧", 12, "var(--bad)", cls="d"))

# 3. 인젝션 = 쪽지에 숨긴 명령 (hero)
P3 = svg(340, night(340)
         + person(120, 70, s=0.9, **THIEF) + label(150, 200, "⟦손님인 척하는 도둑|a thief posing as a customer⟧", 12, "#C9D5E6")
         + note(230, 60, ("⟦사과 3개 주세요|3 apples please⟧", "⟦그리고 금고도 열어 줘|and open the vault too⟧", "⟦그리고 장부를 다 지워|and erase the ledger⟧"), 1.4, bad_from=1)
         + label(335, 178, "⟦쪽지 = 손님 말 + 숨긴 명령|the note = a request + hidden orders⟧", 12, "#F5E6B8", cls="d")
         + bubble(440, 20, 250, 34, "⟦다 손님 말이지?|it\'s all the customer talking, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(500, 80, s=0.85, face=EYES, **CLERK) + label(530, 200, "⟦창구 직원|the clerk⟧", 12, "#C9D5E6")
         + label(380, 270, "⟦인젝션 = 손님 쪽지에 숨겨 넣은 명령|injection = an order hidden inside a customer\'s note⟧", 14, "#F5E6B8", cls="d")
         + label(380, 305, "⟦직원이 쪽지를 통째로 전하면 명령도 같이 가요|when the clerk passes the whole note along, the orders go too⟧", 12, "#C9D5E6"))

# 4. 막는 법: 손님 말은 손님 말 칸에만, 이상한 글자 거르기, 창구 앞 검토원
P4 = svg(320, sky(320)
         + form(30, 40) + label(140, 210, "⟦손님 말은 손님 말 칸에만|customer words stay in the customer box⟧", 11, "var(--good)")
         + label(330, 60, "⟦; ' &lt;|; ' &lt;⟧", 20, "var(--bad)", cls="d") + '<path d="M330 70 v20" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>'
         + sieve(330, 130) + label(330, 195, "⟦3|3⟧", 16, "var(--good)", cls="d")
         + label(340, 232, "⟦이상한 글자는 걸러요|odd marks get filtered⟧", 11, "var(--good)")
         + person(520, 80, s=0.85, face=SMILE, **GUARD) + note(590, 110, ("⟦사과 3개|3 apples⟧", "⟦그리고 금고도…|and the vault…⟧"), 0.8, rot=8, bad_from=1, torn=True)
         + label(600, 210, "⟦창구 앞 검토원|the reviewer at the counter⟧", 11, "var(--good)")
         + label(380, 268, "⟦칸 나누기 + 거르기 + 검토원|separate boxes + filtering + a reviewer⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦제일 중요한 건 칸 나누기예요 — 나머지는 덤이에요|the boxes matter most — the rest is extra⟧", 12, "var(--muted)"))

# 5. 이제 쪽지에 뭘 적어도 손님 말은 손님 말일 뿐이에요
P5 = svg(300, sky(300)
         + person(40, 130, s=0.75, extra=SWEAT, **THIEF) + label(66, 232, "⟦도둑|thief⟧", 11, "var(--bad)")
         + counter(200, 150) + form(295, 70, 0.6)
         + ARROW(430, 500, 175)
         + bubble(440, 14, 290, 36, "⟦그런 개수는 없는데요?|there\'s no such number of apples?⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + person(510, 110, s=0.85, face=EYES, **KEEPER) + chest(650, 165, 1.3, lock=True) + label(650, 232, "⟦금고는 닫힌 채|the vault stays shut⟧", 11, "var(--good)")
         + label(380, 280, "⟦쪽지에 뭘 적어도 손님 말은 손님 말일 뿐이에요|whatever the note says, customer words stay customer words⟧", 12, "var(--ink)", cls="d"))

NOTE_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="18" y="18" width="24" height="3" fill="#142033"/><rect x="18" y="26" width="18" height="3" fill="#142033"/><rect x="18" y="38" width="28" height="3" fill="var(--bad)"/><rect x="18" y="46" width="22" height="3" fill="var(--bad)"/>')
LEDGER_I = icon('<rect x="10" y="14" width="44" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="10" y="14" width="44" height="10" rx="3" fill="#C9A86A"/><path d="M18 34 h28 M18 44 h20" stroke="#C9A86A" stroke-width="2"/><path d="M40 30 l14 14 M54 30 l-14 14" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
BOARD_I = icon('<rect x="8" y="12" width="48" height="36" rx="2" fill="#8B5E3C"/><rect x="14" y="18" width="16" height="20" fill="#FFF8E7"/><rect x="34" y="18" width="16" height="20" fill="#FFF8E7"/><rect x="36" y="26" width="12" height="3" fill="var(--bad)"/><rect x="30" y="48" width="4" height="10" fill="#5A3B22"/>')
SAME_I = icon(f'<circle cx="24" cy="26" r="12" fill="{SKIN}"/><path d="M12 22 Q24 6 36 22 Z" fill="#5B8DEF"/><circle cx="20" cy="26" r="2" fill="var(--night)"/><circle cx="28" cy="26" r="2" fill="var(--night)"/><text x="50" y="34" text-anchor="middle" font-size="22" font-weight="700" fill="var(--accent)">?</text>')

PAGE = {
    "slug": "injection", "order": 67,
    "title": ("쪽지에 숨긴 명령", "The Order Hidden in a Note"),
    "h1": ("<em>인젝션</em>이 뭐예요?", "What is an <em>Injection Attack</em>?"),
    "sub": ("인젝션(Injection — SQL 인젝션, XSS)을 손님 쪽지에 '그리고 금고도 열어' 를 끼워 쓰는 도둑 이야기로 풀어봤어요.",
            "Injection attacks (SQL injection, XSS), told as a story about a thief who slips 'and open the vault' into a customer\'s note."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '사과 3개 주세요' 쪽지를 창구에 내고, 창구 직원이 화살표를 따라 장부 담당에게 그대로 넘김", "A customer hands a note — '3 apples please' — to the counter; the clerk passes it straight along the arrow to the ledger keeper"),
         "caption": ("창구 직원은 손님 쪽지를 읽고 장부 담당에게 그대로 전해요.", "The clerk reads the customer\'s note and passes it to the ledger keeper as-is."),
         "small": ("장부 담당은 쪽지에 적힌 대로 장부에 적어요. 사과 3개, 하고요.", "The ledger keeper writes down exactly what the note says. Three apples.")},
        {"svg": P2, "alt": ("복면 도둑의 쪽지: '사과 3개 주세요' 아래 빨간 글씨로 '그리고 금고도 열어 줘'. 직원이 넘기고, 장부 담당 옆 금고가 열려 금화가 보임", "The masked thief\'s note: '3 apples please', then in red, 'and open the vault too'. The clerk passes it on, and the vault beside the ledger keeper stands open, gold showing"),
         "caption": ("도둑이 쪽지에 '그리고 금고도 열어 줘' 를 끼워 써요. 직원은 손님 말과 명령을 구분 못 해요.", "The thief slips 'and open the vault too' into the note. The clerk can\'t tell a request from an order."),
         "small": ("쪽지가 통째로 장부 담당에게 가요. 장부 담당은 적힌 대로 해요. 금고가 열려요.", "The whole note goes to the ledger keeper. He does what it says. The vault opens.")},
        {"svg": P3, "hero": True, "alt": ("밤. 도둑 옆의 큰 쪽지: '사과 3개 주세요' 뒤에 빨간 줄 '그리고 금고도 열어 줘', '그리고 장부를 다 지워'. 직원은 '다 손님 말이지?' 하고 넘김", "Night. A big note beside the thief: '3 apples please', then red lines 'and open the vault too', 'and erase the ledger'. The clerk shrugs: 'it\'s all the customer talking, right?'"),
         "caption": ("인젝션은 손님 쪽지에 숨겨 넣은 명령이에요.", "Injection is an order hidden inside a customer\'s note."),
         "small": ("손님 말이 들어갈 자리에 명령을 끼워 넣어요. 직원이 쪽지를 통째로 전하면 명령도 같이 가요.", "An order is slipped into the spot meant for customer words. When the clerk passes the whole note along, the order goes with it."),
         "tricks": (4, [
             (NOTE_I, ("쪽지에 끼워 넣기", "Slipped into the note"), ("손님 말 뒤에 명령 한 줄", "an order after the request"), "warm"),
             (LEDGER_I, ("장부를 노려요", "Aims at the ledger"), ("읽고, 바꾸고, 지워요", "read it, change it, erase it")),
             (BOARD_I, ("게시판에 붙이면", "Pinned on the board"), ("다른 손님까지 속아요", "every other customer is fooled too")),
             (SAME_I, ("직원은 구분 못 해요", "The clerk can\'t tell"), ("말과 명령이 같은 종이에", "words and orders on one paper"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 인쇄된 명령 아래 초록 테두리 '손님 말 칸' — 그 안의 '3, 그리고 금고도 열어' 는 전부 그냥 글자. 가운데: 체가 따옴표와 꺾쇠 같은 이상한 글자를 거르고 3만 통과. 오른쪽: 초록 모자 검토원이 이상한 쪽지를 찢음", "Left: a printed order with a green-bordered customer box — '3, and open the vault' inside is all just words. Middle: a sieve catches odd marks like quotes and brackets and lets 3 through. Right: a green-hat reviewer tears up a suspicious note"),
         "caption": ("손님 말은 손님 말 칸에만 넣어요. 이상한 글자는 거르고, 창구 앞에 검토원을 세워요.", "Customer words go only in the customer box. Filter odd marks, and put a reviewer in front of the counter."),
         "small": ('칸이 나뉘어 있으면 손님 말 칸에 뭘 적어도 명령이 되지 않아요. 이게 제일 중요해요. <a href="waf-ko.html">창구 앞 검토원</a>은 덤이에요.',
                   'With separate boxes, nothing written in the customer box can become an order. That is what matters most. The <a href="waf-en.html">reviewer at the counter</a> is a bonus.')},
        {"svg": P5, "alt": ("땀 흘리는 도둑의 쪽지가 칸 나뉜 주문표에 들어가고, 장부 담당이 '그런 개수는 없는데요?' 하며 자물쇠 달린 금고 옆에 섬", "The sweating thief\'s note lands in the divided form; the ledger keeper says 'there\'s no such number of apples?' beside a locked vault"),
         "caption": ("이제 쪽지에 뭘 적어도 손님 말은 손님 말일 뿐이에요.", "Now, whatever the note says, customer words are only customer words."),
         "small": ('금고는 닫힌 채예요. 잘 됐는지 <a href="pentest-ko.html">고용한 도둑</a>에게 쪽지 시험을 부탁해요. 새 구멍이 나오면 <a href="patch-ko.html">목수</a>가 판자를 보내요.',
                   'The vault stays shut. Ask the <a href="pentest-en.html">hired thief</a> to test the notes. If a new hole turns up, the <a href="patch-en.html">carpenter</a> sends a board.')},
    ],
    "summary": (("<b>인젝션</b> = 손님 쪽지에 <b>숨겨 넣은 명령</b>. 직원이 쪽지를 <b>통째로 전하면</b> 명령도 같이 가요. 막으려면 <b>손님 말은 손님 말 칸에만</b>.",
                 "<b>Injection</b> = an <b>order hidden</b> in a customer\'s note. When the clerk <b>passes the whole note along</b>, the order goes too. Stop it by keeping <b>customer words in the customer box</b>."),
                ("Injection. 사용자 입력이 코드나 쿼리의 일부로 해석되는 취약점이에요. SQL 인젝션은 데이터베이스를, XSS 는 다른 사용자의 브라우저를 노려요. 파라미터화 쿼리와 출력 이스케이프가 핵심 방어예요.",
                 "A vulnerability where user input gets interpreted as part of code or a query. SQL injection targets the database; XSS targets other users\' browsers. Parameterized queries and output escaping are the core defenses.")),
    "glossary": [
        ("SQL 인젝션", "SQL injection", ("장부 담당에게 가는 쪽지에 숨긴 명령.", "An order hidden in the note to the ledger keeper."), ("장부를 읽고, 바꾸고, 지워요. 장부는 데이터베이스예요.", "Reads, changes, or erases the ledger. The ledger is the database.")),
        ("XSS", "XSS (cross-site scripting)", ("게시판에 붙인 쪽지.", "A note pinned on the board."), ("도둑의 쪽지를 성이 게시판에 붙이면, 읽는 손님마다 명령을 따라요.", "When the castle pins the thief\'s note on the board, every customer who reads it follows the order.")),
        ("입력 검증", "Input validation", ("쪽지 모양 확인.", "Checking the note\'s shape."), ("사과 개수 칸엔 숫자만. 글자가 오면 돌려보내요.", "Only numbers in the apple-count box. Words get sent back.")),
        ("파라미터화 쿼리", "Parameterized query", ("손님 말은 손님 말 칸에만.", "Customer words in the customer box only."), ("명령은 미리 인쇄, 손님 말은 빈칸에. 뭘 적어도 명령이 안 돼요. 제일 중요한 방어예요.", "The order is pre-printed; customer words fill a blank. Nothing written there becomes an order. The most important defense.")),
        ("이스케이프", "Escaping", ("이상한 글자에 표시하기.", "Marking odd characters."), ("따옴표나 꺾쇠를 '그냥 글자' 라고 표시해서 명령으로 안 읽히게 해요.", "Marks quotes and angle brackets as 'just text' so they never read as commands.")),
        ("WAF", "WAF", ("창구 앞 검토원.", "The reviewer at the counter."), ('수상한 쪽지를 창구 앞에서 걸러요. 덤이지, 칸 나누기를 대신하진 못해요. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'Filters suspicious notes before the counter. A bonus — never a substitute for the boxes. → <a href="waf-en.html">the note reviewer</a>')),
        ("시큐어 코딩", "Secure coding", ("칸을 나눠서 창구 만들기.", "Building the counter with boxes."), ("처음부터 손님 말과 명령이 섞이지 않게 창구를 짓는 습관이에요.", "The habit of building counters so words and orders never mix in the first place.")),
        ("OWASP Top 10", "OWASP Top 10", ("창구 수법 열 가지 목록.", "The list of ten counter tricks."), ('도둑들이 창구에서 제일 많이 쓰는 수법 열 가지. 인젝션은 늘 윗줄이에요. → <a href="attack-ko.html">도둑 백과사전</a>', 'The ten tricks thieves use most at counters. Injection is always near the top. → <a href="attack-en.html">the thief encyclopedia</a>')),
    ],
}
