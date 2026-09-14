from _draw import *
from _world import *


def toolbox(x, y, s=1.0, text=None):
    """공방 도구 상자: 나무 상자에 계산기·달력·전화. 중심 x, 상자 앞면 y-20..y+30, 도구 머리 y-46. 폭 130. text 는 y+50."""
    t = label(0, 50, text, 11, "var(--muted)") if text else ""
    calc = ('<rect x="-52" y="-46" width="30" height="40" rx="4" fill="#4A5A72"/><rect x="-47" y="-41" width="20" height="9" rx="2" fill="#C9D5E6"/>'
            + "".join(f'<circle cx="{-46 + i * 8}" cy="{-24 + j * 8}" r="2.5" fill="#C9D5E6"/>' for i in range(3) for j in range(2)))
    cal = ('<rect x="-15" y="-46" width="32" height="40" rx="4" fill="#FFF8E7" stroke="#B5382C" stroke-width="2"/><rect x="-15" y="-46" width="32" height="10" rx="4" fill="#B5382C"/>'
           + "".join(f'<rect x="{-10 + i * 8}" y="{-30 + j * 8}" width="5" height="5" fill="#142033"/>' for i in range(3) for j in range(2)))
    phone = '<rect x="26" y="-46" width="24" height="40" rx="5" fill="#142033"/><rect x="29" y="-41" width="18" height="26" rx="2" fill="#5B9BD5"/><circle cx="38" cy="-10" r="2" fill="#C9D5E6"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-65" y="-30" width="130" height="60" rx="6" fill="#5A3B22"/>'
            f'{calc}{cal}{phone}<rect x="-65" y="-20" width="130" height="50" rx="6" fill="{WOOD}"/><rect x="-65" y="-20" width="130" height="8" fill="#5A3B22"/>{t}</g>')


def arrow(x1, y1, x2, y2, color="var(--muted)", dash=True):
    """화살표. 머리는 끝점 방향으로 돌린다."""
    import math
    d = ' stroke-dasharray="6 5"' if dash else ""
    deg = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"{d}/>'
            f'<path d="M0 0 l-10 -6 l0 12z" transform="translate({x2},{y2}) rotate({deg:.0f})" fill="{color}"/>')


# 1. 오늘 환율? 앵무새는 책을 덮은 날 숫자를 말해요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, talk=True)
         + bubble_parrot(90, 30, 230, 44, "⟦1달러는 1,100원이에요|a dollar is 1,100 won⟧", 12)
         + label(205, 105, "⟦(책을 덮은 날 숫자예요)|(the number from the day it closed its books)⟧", 11, "var(--bad)")
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(420, 30, 260, 44, "⟦오늘 환율 알려줘|what is the exchange rate today?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦앵무새는 오늘을 몰라요 — 읽은 책은 옛날에 끝났어요|the parrot doesn\'t know today — its books ended long ago⟧", 13, "var(--ink)"))

# 2. 앵무새는 말만 하는 새 — 계산·검색·전화를 직접 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(150, 150, 1.1, mood="sweat") + label(150, 240, "⟦손이 없어요|no hands⟧", 12, "var(--muted)")
         + label(380, 95, "⟦닿지 않아요|can\'t reach⟧", 12, "var(--bad)")
         + toolbox(380, 170, 1.2, "⟦계산기 · 달력 · 전화|calculator · calendar · phone⟧")
         + note(520, 40, 210, 120, "⟦앵무새가 못 하는 것|WHAT IT CAN\'T DO⟧", ("⟦계산하기  ×|calculate  ×⟧", "⟦검색하기  ×|search  ×⟧", "⟦전화 걸기  ×|make a call  ×⟧"), 1.0)
         + label(380, 282, "⟦앵무새는 말만 하는 새예요 — 계산도 검색도 전화도 직접 못 해요|the parrot only talks — it can\'t calculate, search, or call by itself⟧", 12, "var(--bad)"))

# 3. 도구 호출 = 도구 목록을 주고, 부탁 쪽지를 쓰게 하고, 조련사가 돌려요 (hero)
P3 = svg(360, sky(360)
         + note(30, 40, 170, 120, "⟦도구 목록|TOOL LIST⟧", ("⟦환율: (돈1, 돈2)|rate: (money1, money2)⟧", "⟦달력: (날짜)|calendar: (date)⟧", "⟦전화: (번호)|phone: (number)⟧"), 1.0)
         + label(115, 182, "⟦조련사가 미리 줘요|the trainer gives this first⟧", 11, "var(--muted)")
         + perch(330, 250, 150) + parrot(330, 210, 1.3, talk=True)
         + bubble_parrot(230, 70, 220, 44, "⟦환율 도구 써 줘 (KRW, USD)|use the rate tool (KRW, USD)⟧", 12)
         + label(340, 152, "⟦쪽지만 써요|it only writes the note⟧", 11, "var(--muted)")
         + arrow(455, 92, 530, 110)
         + person(540, 120, s=0.9, face=SMILE, **TRAINER) + label(575, 245, "⟦조련사가 실행|the trainer runs it⟧", 11, "var(--muted)")
         + toolbox(660, 200, 0.9, "⟦도구 상자|toolbox⟧")
         + bean(480, 190, 0.9, text="⟦1,380|1,380⟧") + label(480, 215, "⟦결과 콩|result bean⟧", 10, "var(--muted)")
         + '<path d="M530 190 L505 190" stroke="var(--muted)" stroke-width="3"/><path d="M505 190 l9 -6 l-2 12z" fill="var(--muted)"/>'
         + label(380, 340, "⟦도구 호출 = 앵무새가 부탁 쪽지를 쓰고, 조련사가 도구를 돌려요|tool calling: the parrot writes a request note, the trainer runs the tool⟧", 13, "var(--ink)", cls="d"))

# 4. 흐름: 질문 → 부탁 쪽지 → 조련사 실행 → 결과 콩 → 답
P4 = svg(320, sky(320)
         + person(45, 80, s=0.7, face=EYES, **GUEST) + label(80, 215, "⟦1 질문|1 question⟧", 12, "var(--ink)", cls="d") + label(80, 235, "⟦오늘 환율?|rate today?⟧", 11, "var(--muted)")
         + arrow(110, 130, 180, 130)
         + parrot(230, 130, 0.9, talk=True) + label(230, 215, "⟦2 부탁 쪽지|2 request note⟧", 12, "var(--ink)", cls="d") + label(230, 235, "⟦환율 (KRW, USD)|rate (KRW, USD)⟧", 11, "var(--muted)")
         + arrow(262, 130, 322, 130)
         + person(330, 70, s=0.7, face=SMILE, **TRAINER) + toolbox(415, 172, 0.5)
         + label(385, 215, "⟦3 조련사가 실행|3 trainer runs it⟧", 12, "var(--ink)", cls="d") + label(385, 235, "⟦진짜 도구를 돌려요|the real tool runs⟧", 11, "var(--muted)")
         + arrow(458, 130, 505, 130)
         + bean(535, 130, 1.2, text="⟦1,380|1,380⟧") + label(535, 215, "⟦4 결과 콩|4 result bean⟧", 12, "var(--ink)", cls="d") + label(535, 235, "⟦쟁반에 올려요|onto the tray⟧", 11, "var(--muted)")
         + arrow(565, 130, 650, 130)
         + parrot(690, 130, 0.9, talk=True) + label(690, 215, "⟦5 답|5 answer⟧", 12, "var(--ink)", cls="d") + label(690, 235, "⟦1달러는 1,380원|a dollar is 1,380 won⟧", 11, "var(--muted)")
         + label(380, 295, "⟦앵무새는 쪽지를 쓰고, 조련사가 돌리고, 결과가 다시 앵무새에게 가요|the parrot writes, the trainer runs, the result goes back to the parrot⟧", 12, "var(--ink)"))

# 5. 쪽지가 틀리면 돌아와요 — 앵무새는 도구를 쓰는 게 아니라 부탁하는 것
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(90, 140, 1.0, talk=True) + note(150, 50, 200, 100, "⟦부탁 쪽지 ✓|REQUEST ✓⟧", ("⟦도구: 환율|tool: rate⟧", "⟦칸: KRW, USD|slots: KRW, USD⟧"), 1.0)
         + label(230, 190, "⟦정해진 칸에 맞게 썼어요|written in the fixed slots⟧", 11, "var(--good)")
         + label(190, 240, "⟦조련사가 바로 돌려요|the trainer runs it right away⟧", 11, "var(--ink)")
         + parrot(470, 140, 1.0, color=PARROT_BAD, talk=True) + note(530, 50, 200, 100, "⟦부탁 쪽지 ×|REQUEST ×⟧", ("⟦도구: 날씨 (없어요)|tool: weather (none)⟧", "⟦칸: 사과 (틀려요)|slots: apple (wrong)⟧"), 1.0)
         + label(610, 190, "⟦없는 도구, 잘못된 칸|missing tool, wrong slot⟧", 11, "var(--bad)")
         + label(570, 240, "⟦조련사가 쪽지를 돌려보내요|the trainer sends the note back⟧", 11, "var(--ink)")
         + label(380, 300, "⟦앵무새가 도구를 쓰는 게 아니라 부탁 쪽지를 쓰는 거예요 — 틀리면 돌아와요|the parrot doesn\'t use the tool, it asks — a wrong note comes back⟧", 12, "var(--ink)", cls="d"))

LIST_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="12" rx="4" fill="#C9A86A"/><path d="M20 30 h24 M20 40 h24 M20 50 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
NOTE_I = icon(f'<circle cx="22" cy="24" r="10" fill="{PARROT}"/><path d="M30 20 l10 3 l-10 4z" fill="#E9B44C"/><rect x="30" y="34" width="26" height="22" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M36 42 h14 M36 49 h10" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
TRAY_I = icon(f'<rect x="8" y="34" width="48" height="18" rx="6" fill="var(--stone)"/><ellipse cx="32" cy="28" rx="13" ry="9" fill="{BEAN}"/><path d="M26 25 q6 -4 12 0" stroke="#5A3B22" stroke-width="1.5" fill="none"/>')
HAND_I = icon(f'<circle cx="32" cy="20" r="10" fill="{SKIN}"/><rect x="20" y="32" width="24" height="22" rx="6" fill="var(--good)"/><path d="M44 14 l8 8 M52 14 l-8 8" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "toolcall", "order": 15,
    "title": ("도구 상자", "The Toolbox"),
    "h1": ("<em>도구 호출</em>이 뭐예요?", "What is <em>Tool Calling</em>?"),
    "sub": ("도구 호출(함수 호출)을 앵무새에게 도구 상자 목록을 주고 부탁 쪽지를 쓰게 하는 이야기로 풀어봤어요.",
            "Tool calling (function calling), told as a story about giving the parrot a toolbox list and letting it write request notes."),
    "panels": [
        {"svg": P1, "alt": ("손님이 오늘 환율을 묻자 횃대 위 앵무새가 1달러는 1,100원이라고 옛날 숫자를 말함", "A guest asks today\'s exchange rate; the parrot on its perch answers with an old number, 1,100 won per dollar"),
         "caption": ("손님이 오늘 환율을 물었어요. 앵무새는 옛날 숫자를 말해요.", "The guest asks today\'s exchange rate. The parrot answers with an old number."),
         "small": ('앵무새는 <a href="knowledgecutoff-ko.html">책을 덮은 날</a> 이후를 몰라요. 오늘 숫자는 어디서 가져와야 할까요?',
                   'The parrot knows nothing after <a href="knowledgecutoff-en.html">the day it closed its books</a>. Where should today\'s number come from?')},
        {"svg": P2, "alt": ("땀 흘리는 앵무새가 계산기·달력·전화가 든 도구 상자에 닿지 못함. 쪽지엔 계산하기 ×, 검색하기 ×, 전화 걸기 ×", "A sweating parrot can\'t reach a toolbox with a calculator, calendar and phone; a note lists calculate ×, search ×, make a call ×"),
         "caption": ("앵무새는 말만 하는 새예요. 계산도 검색도 전화도 직접 못 해요.", "The parrot only talks. It can\'t calculate, search, or call by itself."),
         "small": ("계산기가 바로 앞에 있어도 손이 없어요. 말로 숫자를 지어내는 수밖에요 — 그래서 옛날 숫자가 나와요.", "Even with a calculator right there, it has no hands. All it can do is make up a number in words — hence the old number.")},
        {"svg": P3, "hero": True, "alt": ("도구 목록 쪽지(환율·달력·전화)를 받은 앵무새가 '환율 도구 써 줘 (KRW, USD)' 쪽지를 씀. 조련사가 도구 상자에서 도구를 돌리고 결과 콩 1,380 을 앵무새에게 돌려줌", "Given a tool-list note (rate, calendar, phone), the parrot writes a note: use the rate tool (KRW, USD). The trainer runs the tool from the toolbox and returns a result bean, 1,380"),
         "caption": ("도구 호출은 앵무새가 부탁 쪽지를 쓰고, 조련사가 도구를 돌리는 거예요.", "Tool calling: the parrot writes a request note, and the trainer runs the tool."),
         "small": ('도구마다 이름·설명·빈칸을 적은 목록을 먼저 줘요. 앵무새는 필요할 때 <a href="structuredoutput-ko.html">정해진 칸</a>에 부탁을 써요. 실제로 도구를 돌리는 건 조련사(프로그램)예요.',
                   'First the parrot gets a list with each tool\'s name, description and blanks. When it needs one, it writes a request in <a href="structuredoutput-en.html">fixed slots</a>. The one who actually runs the tool is the trainer (the program).'),
         "tricks": (4, [
             (LIST_I, ("도구마다 이름·설명·칸", "Name, description, slots"), ("목록을 먼저 줘요", "give the list first"), "calm"),
             (NOTE_I, ("앵무새는 쪽지만 써요", "The parrot only writes"), ("돌리는 건 조련사", "the trainer runs it")),
             (TRAY_I, ("결과는 쟁반으로", "Results go on the tray"), ("콩으로 돌아와요", "back as beans"), "calm"),
             (HAND_I, ("위험한 도구는 사람 확인", "Risky tools need a person"), ("돈·삭제·보내기", "money, delete, send"), "warm"),
         ])},
        {"svg": P4, "alt": ("다섯 단계: 손님 질문, 앵무새 부탁 쪽지, 조련사가 도구 상자로 실행, 결과 콩 1,380, 앵무새의 답 1달러는 1,380원", "Five steps: the guest asks, the parrot writes a request, the trainer runs the toolbox, a result bean 1,380, the parrot answers a dollar is 1,380 won"),
         "caption": ("질문, 쪽지, 실행, 결과 콩, 답. 다섯 걸음이에요.", "Question, note, run, result bean, answer. Five steps."),
         "small": ('결과 콩은 <a href="context-ko.html">쟁반</a>에 올라가요. 앵무새는 그 콩을 읽고 답을 이어요. 도구가 여러 개면 쪽지를 한꺼번에 여러 장 쓸 수도 있어요.',
                   'The result bean goes onto the <a href="context-en.html">tray</a>; the parrot reads it and continues its answer. With several tools, it can write several notes at once.')},
        {"svg": P5, "alt": ("왼쪽 초록: 도구 환율, 칸 KRW·USD 로 바르게 쓴 쪽지. 오른쪽 빨강: 없는 도구 날씨, 잘못된 칸 사과를 쓴 빨간 앵무새의 쪽지가 되돌아옴", "Left, green: a correct note with tool rate and slots KRW, USD. Right, red: a red parrot\'s note with a missing tool weather and a wrong slot apple is sent back"),
         "caption": ("앵무새가 도구를 쓰는 게 아니라 부탁하는 거예요. 쪽지가 틀리면 돌아와요.", "The parrot doesn\'t use the tool — it asks. A wrong note comes back."),
         "small": ('없는 도구를 부르거나 칸을 잘못 채우면 조련사가 돌려보내요. 부탁 쪽지를 여러 번 쓰며 일을 끝내는 앵무새는 <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>, 도구 상자의 공통 규격은 <a href="mcp-ko.html">도구 상자 규격</a>에서.',
                   'Call a missing tool or fill a slot wrong, and the trainer sends the note back. A parrot that writes many notes to finish a job: <a href="agent-en.html">the parrot that plans its own errands</a>; a common standard for toolboxes: <a href="mcp-en.html">the toolbox standard</a>.')},
    ],
    "summary": (("<b>도구 호출</b> = 앵무새에게 <b>도구 상자 목록</b>을 주고, 필요할 때 <b>부탁 쪽지</b>를 쓰게 하기. 실제로 도구를 돌리는 건 <b>조련사(프로그램)</b>고, 결과는 콩으로 쟁반에 돌아와요.",
                 "<b>Tool calling</b> = giving the parrot a <b>toolbox list</b> and letting it write a <b>request note</b> when it needs one. The <b>trainer (program)</b> actually runs the tool, and the result comes back as beans on the tray."),
                ("Tool calling / function calling. 모델에게 도구 스키마(이름·설명·파라미터)를 주면, 모델은 도구를 실행하는 게 아니라 '이 도구를 이 인자로 불러 달라'는 구조화된 요청을 출력해요. 런타임이 실제 함수를 실행하고 결과를 컨텍스트에 넣어 주면 모델이 답을 이어가요.",
                 "Given tool schemas (name, description, parameters), the model doesn\'t run anything — it emits a structured request to call a tool with certain arguments. The runtime executes the real function and puts the result back into the context so the model can continue.")),
    "glossary": [
        ("도구 호출", "Tool calling / function calling", ("부탁 쪽지 쓰기.", "Writing the request note."), ("앵무새가 도구를 쓰는 게 아니라 써 달라고 적어요.", "The parrot doesn\'t use the tool; it writes that it wants it used.")),
        ("도구 스키마", "Tool schema", ("도구마다 이름·설명·칸.", "Name, description and slots per tool."), ('앵무새가 받는 도구 목록. 칸이 정해져 있어요. → <a href="structuredoutput-ko.html">정해진 칸에 쓰기</a>', 'The list the parrot gets, with fixed slots. → <a href="structuredoutput-en.html">writing in fixed slots</a>')),
        ("도구 결과", "Tool result", ("돌아온 결과 콩.", "The result bean that comes back."), ('쟁반에 올라가고 앵무새가 읽어요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'It goes on the tray and the parrot reads it. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("런타임", "Runtime", ("조련사.", "The trainer."), ("쪽지를 읽고 진짜 도구를 돌리는 프로그램이에요.", "The program that reads the note and runs the real tool.")),
        ("병렬 호출", "Parallel tool calls", ("쪽지 여러 장 한꺼번에.", "Several notes at once."), ("서로 상관없는 도구는 한 번에 부탁해요.", "Unrelated tools can be requested together.")),
        ("오류 처리", "Error handling", ("틀린 쪽지 돌려보내기.", "Sending a wrong note back."), ("없는 도구, 잘못된 칸, 실패한 도구는 결과 대신 오류 콩을 줘요.", "A missing tool, a wrong slot or a failed tool gets an error bean instead of a result.")),
        ("MCP", "MCP", ("도구 상자 규격.", "The toolbox standard."), ('어느 앵무새든 열 수 있는 상자. → <a href="mcp-ko.html">도구 상자 규격</a>', 'A box any parrot can open. → <a href="mcp-en.html">the toolbox standard</a>')),
        ("에이전트", "Agent", ("쪽지를 여러 번 쓰는 앵무새.", "A parrot that writes many notes."), ('결과를 보고 다음 도구를 골라요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'It picks the next tool from the result. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
    ],
}
