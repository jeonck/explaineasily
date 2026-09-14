from _draw import *
from _world import *

ROWS3 = (("⟦이름|name⟧", "⟦김철수|Kim⟧"), ("⟦날짜|date⟧", "⟦3월 3일|Mar 3⟧"), ("⟦금액|amount⟧", "⟦10000|10000⟧"))


def form(x, y, rows, title="⟦양식|FORM⟧", s=1.0, filled=True):
    """칸이 그려진 종이. rows = ((칸 이름, 값), …). 원본 폭 240, 높이 40 + 40*줄."""
    h = 40 + 40 * len(rows)
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="240" height="{h}" rx="6" fill="{PAPER}" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="240" height="26" rx="6" fill="#C9A86A"/>' + label(120, 18, title, 12, PAPER_INK, cls="d"))
    for i, (k, v) in enumerate(rows):
        yy = 60 + i * 40
        out += (label(14, yy, k, 12, PAPER_INK, "start") + f'<rect x="80" y="{yy - 16}" width="140" height="24" rx="4" fill="#FFF" stroke="#C9A86A" stroke-width="2"/>'
                + (label(150, yy, v, 12, PAPER_INK) if filled else ""))
    return out + "</g>"


def machine(x, y, w, h, text, color="var(--bad)"):
    """장부 기계. (x,y) 왼쪽 위."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="var(--stone-dark)"/>'
            f'<rect x="{x + 12}" y="{y + 12}" width="{w - 24}" height="{h - 44}" rx="4" fill="var(--panel)"/>'
            f'<circle cx="{x + 20}" cy="{y + h - 16}" r="5" fill="var(--accent)"/><circle cx="{x + 36}" cy="{y + h - 16}" r="5" fill="var(--good)"/>'
            + label(x + w / 2, y + h / 2 - 8, text, 20, color, cls="d"))


# 1. 앵무새 답을 장부 기계에 넣어야 하는데 매번 모양이 달라 기계가 못 읽어요
P1 = svg(300, sky(300)
         + perch(120, 200, 140) + parrot(120, 160, 1.1, talk=True)
         + bubble(20, 40, 260, 40, "⟦김철수님이 3월 3일에 만 원 내셨어요|Mr Kim paid 10,000 won on March 3⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + machine(330, 90, 150, 120, "⟦???|???⟧") + label(405, 235, "⟦장부 기계|ledger machine⟧", 11, "var(--muted)")
         + person(500, 110, s=0.9, face=FROWN, **GUEST) + bubble(430, 30, 230, 40, "⟦기계가 못 읽어요|the machine cannot read it⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + note(600, 150, 140, 90, "⟦어제, 오늘, 내일|yesterday, today, tomorrow⟧", ("⟦3월 3일 만 원…|March 3, 10k…⟧", "⟦만 원, 3/3, 김…|10k, 3/3, Kim…⟧", "⟦김철수: 3일에…|Kim: on the 3rd…⟧"), 0.9)
         + label(380, 282, "⟦답은 맞는데 모양이 매번 달라요 — 기계는 못 읽어요|the answer is right, but its shape changes every time — the machine cannot read it⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새는 말로 답하는 새 — 칸이 없으면 자유롭게 써요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, talk=True)
         + bubble(190, 40, 230, 34, "⟦3월 3일에 만 원이요|10k won on March 3⟧", 11, "var(--panel)", "var(--line)", "left")
         + bubble(190, 100, 230, 34, "⟦김철수님, 만 원, 3일!|Mr Kim, 10k, the 3rd!⟧", 11, "var(--panel)", "var(--line)", "left")
         + bubble(190, 160, 230, 34, "⟦음… 그날 만 원쯤?|hmm… about 10k that day?⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(590, 80, "⟦앵무새는 말로 답하는 새예요|the parrot answers in words⟧", 12, "var(--ink)", cls="d")
         + label(590, 105, "⟦칸이 없으면 마음대로 써요|no boxes, so it writes freely⟧", 11, "var(--muted)")
         + '<rect x="500" y="140" width="180" height="70" rx="8" fill="none" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>' + label(590, 180, "⟦칸이 없어요|no boxes⟧", 13, "var(--bad)", cls="d")
         + label(380, 282, "⟦사람은 셋 다 알아듣지만, 기계는 정해진 칸이 있어야 읽어요|people understand all three — a machine needs fixed boxes⟧", 12, "var(--bad)"))

# 3. 구조화 출력 = 칸이 그려진 종이를 주고 그 칸에만 쓰게 하기 (hero)
P3 = svg(360, sky(360)
         + form(50, 40, ROWS3, filled=False)
         + label(170, 235, "⟦빈 양식|an empty form⟧", 11, "var(--muted)")
         + person(320, 110, s=0.9, face=SMILE, **TRAINER) + label(352, 245, "⟦조련사가 양식을 줘요|the trainer hands the form⟧", 11, "var(--muted)")
         + perch(520, 240, 150) + parrot(520, 200, 1.3, talk=True)
         + '<path d="M560 170 L585 140" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + form(590, 50, ROWS3, s=0.65) + label(668, 185, "⟦칸에만 써요|writes only in the boxes⟧", 11, "var(--muted)")
         + label(380, 300, "⟦칸에 없는 말은 안 해요 — 기계가 바로 읽어요|no words outside the boxes — the machine reads it straight away⟧", 11, "var(--muted)")
         + label(380, 340, "⟦구조화 출력 = 칸이 그려진 종이를 주고, 그 칸에만 쓰게 하기|structured output: hand the parrot a form and let it write only in the boxes⟧", 13, "var(--ink)", cls="d"))

# 4. 자유 답 vs 양식 답
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 36, "⟦자유 답|FREE ANSWER⟧", 13, "var(--bad)", cls="d")
         + bubble(40, 60, 300, 40, "⟦김철수님이 3월 3일에 만 원 내셨어요|Mr Kim paid 10k won on March 3⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + machine(115, 130, 150, 110, "⟦???|???⟧")
         + label(190, 268, "⟦기계: 어디가 이름이지?|machine: which part is the name?⟧", 11, "var(--bad)")
         + label(570, 36, "⟦양식 답|FORM ANSWER⟧", 13, "var(--good)", cls="d")
         + form(410, 55, ROWS3, s=0.7)
         + '<path d="M585 115 L625 115" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M617 107 L627 115 L617 123" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + machine(635, 70, 100, 90, "⟦✓|✓⟧", "var(--good)") + label(685, 180, "⟦장부 기계|ledger⟧", 11, "var(--muted)")
         + label(570, 215, "⟦기계: 이름 칸 = 김철수 ✓|machine: name box = Kim ✓⟧", 11, "var(--good)")
         + label(570, 240, "⟦칸 이름이 있으니 바로 넣어요|with named boxes it files it at once⟧", 11, "var(--ink)")
         + label(380, 302, "⟦같은 내용이라도 칸에 쓰면 기계가 읽어요|the same content, in boxes, and the machine can read it⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 칸에 맞춰도 내용이 맞다는 뜻은 아니에요 — 도구 호출도 양식
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + parrot(90, 130, 1.0, color=PARROT_BAD, talk=True)
         + form(150, 40, (("⟦이름|name⟧", "⟦김철수|Kim⟧"), ("⟦날짜|date⟧", "⟦3월 3일|Mar 3⟧"), ("⟦금액|amount⟧", "⟦99999|99999⟧")), s=0.75)
         + label(240, 200, "⟦모양 ✓   내용 ×|shape ✓   content ×⟧", 13, "var(--bad)", cls="d")
         + label(190, 226, "⟦칸은 맞췄지만 금액은 지어냈어요|boxes filled, but the amount is made up⟧", 11, "var(--ink)")
         + form(420, 40, (("⟦도구|tool⟧", "⟦계산기|calculator⟧"), ("⟦입력|input⟧", "⟦3 + 4|3 + 4⟧")), "⟦도구 부탁 양식|TOOL REQUEST⟧", 0.75)
         + label(490, 160, "⟦도구 부탁도 양식이에요|tool requests use a form too⟧", 11, "var(--muted)")
         + person(610, 90, s=0.9, face=SMILE, **TRAINER)
         + label(600, 226, "⟦조련사가 양식을 읽고 도구를 써요|the trainer reads it and runs the tool⟧", 11, "var(--ink)")
         + label(380, 300, "⟦칸이 맞다고 사실이 맞는 건 아니에요 — 내용 확인은 따로|a filled form is not a true form — check the content separately⟧", 12, "var(--ink)", cls="d"))

SCHEMA_I = icon('<rect x="10" y="8" width="44" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="26" y="16" width="22" height="9" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/><rect x="26" y="29" width="22" height="9" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/><rect x="26" y="42" width="22" height="9" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/><path d="M15 21 h7 M15 34 h7 M15 47 h7" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
BLANK_I = icon('<rect x="12" y="22" width="40" height="22" rx="4" fill="#FFF" stroke="#C9A86A" stroke-width="3"/><path d="M24 33 h16" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/>')
NOWORDS_I = icon('<rect x="10" y="12" width="40" height="28" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M22 40 l-6 10 l14 -10z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M20 22 h20 M20 30 h14" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round"/><path d="M40 36 l16 16 M56 36 l-16 16" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
RETRY_I = icon('<path d="M46 32 a14 14 0 1 1 -6 -11" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M42 12 l2 10 l-10 2" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><rect x="26" y="44" width="12" height="12" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/>')

PAGE = {
    "slug": "structuredoutput", "order": 13,
    "title": ("정해진 칸에 쓰기", "Writing in the Boxes"),
    "h1": ("<em>구조화 출력</em>이 뭐예요?", "What is <em>structured output</em>?"),
    "sub": ("구조화 출력(JSON 출력)을 앵무새에게 칸이 그려진 양식을 주고 그 칸에만 쓰게 하는 이야기로 풀어봤어요.",
            "Structured output (JSON output), told as a story about handing the parrot a form and letting it write only in the boxes."),
    "panels": [
        {"svg": P1, "alt": ("앵무새가 '김철수님이 3월 3일에 만 원 내셨어요'라고 말하고, 장부 기계 화면엔 ???, 손님은 '기계가 못 읽어요'. 어제·오늘·내일 답 모양이 다 다른 쪽지", "The parrot says Mr Kim paid 10,000 won on March 3; the ledger machine shows ???; the guest says the machine cannot read it; a note shows yesterday, today and tomorrow all shaped differently"),
         "caption": ("답은 맞는데 모양이 매번 달라요. 기계는 못 읽어요.", "The answer is right, but its shape changes every time. The machine cannot read it."),
         "small": ("앵무새 답을 장부 프로그램에 넣고 싶어요. 그런데 어제는 날짜가 앞, 오늘은 이름이 앞. 기계는 어디가 뭔지 몰라요.", "We want to feed the parrot answer into a ledger program. But yesterday the date came first, today the name. The machine cannot tell which part is which.")},
        {"svg": P2, "alt": ("앵무새가 같은 내용을 세 가지 모양으로 말함. 오른쪽: 앵무새는 말로 답하는 새, 칸이 없으면 마음대로 써요, 빨간 점선 상자 '칸이 없어요'", "The parrot says the same thing in three shapes; on the right: the parrot answers in words, with no boxes it writes freely; a red dashed box reads no boxes"),
         "caption": ("앵무새는 말로 답하는 새예요. 칸이 없으면 자유롭게 써요.", "The parrot answers in words. With no boxes, it writes freely."),
         "small": ('<a href="prompt-ko.html">쪽지</a>에 "짧게 써 줘"라고 해도 모양은 그때그때 달라요. 사람은 다 알아듣지만 기계는 정해진 칸이 있어야 읽어요.',
                   'Even if the <a href="prompt-en.html">note</a> says keep it short, the shape still varies. People understand every version; a machine needs fixed boxes.')},
        {"svg": P3, "hero": True, "alt": ("이름·날짜·금액 칸이 그려진 빈 양식을 조련사가 앵무새에게 주고, 횃대 위 앵무새가 그 칸에만 채워 넣은 양식을 돌려줌", "A trainer hands the parrot an empty form with name, date and amount boxes; the parrot on the perch returns the form filled in only in those boxes"),
         "caption": ("구조화 출력은 칸이 그려진 종이를 주고, 그 칸에만 쓰게 하는 거예요.", "Structured output hands the parrot a form and lets it write only in the boxes."),
         "small": ("칸 이름과 종류를 미리 정해요. 앵무새는 그 칸만 채워요. 기계는 이름 칸, 날짜 칸을 바로 찾아 읽어요.", "Box names and types are set ahead of time. The parrot fills only those boxes. The machine finds the name box and the date box straight away."),
         "tricks": (4, [
             (SCHEMA_I, ("칸 이름과 종류를 미리 정해요", "Name the boxes and their types"), ("이름은 글자, 금액은 숫자", "name is text, amount is a number"), "calm"),
             (BLANK_I, ("없는 값은 빈칸", "Missing value? Leave it empty"), ("지어내지 말고 비워 두기", "leave it blank, do not invent")),
             (NOWORDS_I, ("사람 말은 빼요", "No chatter"), ("기계가 읽어요 — 인사말은 안 돼요", "a machine reads it — no greetings"), "warm"),
             (RETRY_I, ("칸을 벗어나면 다시", "Outside the boxes? Redo"), ("검사해서 틀리면 다시 쓰게", "check it, and if wrong, ask again"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 빨강: 자유 답 말풍선을 받은 장부 기계가 ??? — 어디가 이름이지? 오른쪽 초록: 이름·날짜·금액 양식을 받은 기계가 ✓ — 이름 칸 = 김철수", "Left, red: the ledger machine gets a free-form bubble and shows ??? — which part is the name? Right, green: it gets a name, date and amount form and shows ✓ — name box = Kim"),
         "caption": ("같은 내용이라도 칸에 쓰면 기계가 읽어요.", "The same content, written in boxes, and the machine can read it."),
         "small": ("칸에는 이름이 붙어 있어요. 기계는 이름 칸을 보고 이름을, 금액 칸을 보고 숫자를 꺼내요. 모양이 늘 같으니 매번 돼요.", "Each box has a name. The machine reads the name from the name box and the number from the amount box. The shape never changes, so it works every time.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 빨간 앵무새가 채운 양식, 이름·날짜는 맞지만 금액이 99999 — 모양 ✓ 내용 ×. 오른쪽 초록: 도구 부탁 양식(도구: 계산기, 입력: 3 + 4)을 조련사가 읽고 도구를 씀", "Left, red: a form filled by the red parrot — name and date fine, amount 99999 — shape ✓ content ×. Right, green: a tool request form (tool: calculator, input: 3 + 4) that the trainer reads and runs"),
         "caption": ("칸이 맞다고 사실이 맞는 건 아니에요. 내용 확인은 따로 해요.", "A filled form is not a true form. Check the content separately."),
         "small": ('금액 칸에 숫자가 들어 있어도 지어낸 숫자일 수 있어요 — <a href="hallucination-ko.html">그럴듯 앵무새</a>는 양식 안에서도 그래요. 그리고 <a href="toolcall-ko.html">도구 부탁</a>도 이 양식으로 써요.',
                   'A number in the amount box can still be made up — the <a href="hallucination-en.html">plausible parrot</a> lies inside forms too. And <a href="toolcall-en.html">tool requests</a> are written on this kind of form as well.')},
    ],
    "summary": (("<b>구조화 출력</b> = 앵무새에게 <b>칸이 그려진 양식</b>을 주고 <b>그 칸에만 쓰게</b> 하기. 기계가 바로 읽어요. 칸이 맞아도 <b>내용이 맞다는 뜻은 아니에요</b>.",
                 "<b>Structured output</b> = hand the parrot a <b>form with boxes</b> and let it <b>write only in those boxes</b>. A machine can read it straight away. A correct shape <b>does not mean correct content</b>."),
                ("Structured output / JSON mode. 모델의 응답을 미리 정한 스키마(JSON Schema 등)에 맞는 형태로만 내게 하는 기능이에요. 필드 이름·타입·열거형을 정하고, 응답을 파싱·검증해서 실패하면 재시도해요. 함수 호출(도구 호출)도 같은 원리로 인자를 스키마에 맞춰 내는 거예요. 형식이 맞아도 값의 사실성은 따로 검증해야 해요.",
                 "Makes the model respond only in a shape that matches a predefined schema (such as JSON Schema). You define field names, types and enums, then parse and validate the response, retrying on failure. Function calling (tool use) works on the same principle — arguments emitted to a schema. A valid shape still says nothing about whether the values are true.")),
    "glossary": [
        ("구조화 출력", "Structured output", ("칸에만 쓰기.", "Writing only in the boxes."), ("앵무새 답을 기계가 읽을 수 있는 모양으로 고정해요.", "Locks the parrot answer into a shape a machine can read.")),
        ("JSON 모드", "JSON mode", ("가장 흔한 양식 종류.", "The most common kind of form."), ("중괄호와 따옴표로 된 칸 목록. 거의 모든 프로그램이 읽어요.", "A list of boxes in braces and quotes. Nearly every program can read it.")),
        ("스키마", "Schema", ("양식의 설계도.", "The blueprint of the form."), ("칸 이름, 종류(글자·숫자·예/아니오), 꼭 있어야 하는 칸을 미리 적어요.", "Box names, types (text, number, yes/no) and which boxes are required, written down ahead of time.")),
        ("함수 호출과의 관계", "Relation to function calling", ("도구 부탁도 양식.", "Tool requests are forms too."), ('어떤 도구를 어떤 값으로 쓸지 칸에 써서 넘겨요. → <a href="toolcall-ko.html">도구 상자</a>', 'Which tool, with which values, written into boxes. → <a href="toolcall-en.html">the toolbox</a>')),
        ("검증", "Validation", ("양식 검사.", "Checking the form."), ("칸이 다 있는지, 종류가 맞는지 기계가 먼저 확인해요.", "The machine first checks that every box is there and of the right type.")),
        ("파싱 실패 재시도", "Retry on parse failure", ("칸을 벗어나면 다시 쓰게.", "Outside the boxes? Write it again."), ("가끔 양식이 깨져요. 틀린 부분을 알려 주고 한 번 더 시켜요.", "Sometimes the form breaks. Point out the error and ask once more.")),
        ("열거형", "Enum", ("정해진 값만.", "Only the listed values."), ("예: 상태 칸엔 대기·완료·취소 중 하나만. 새 낱말은 안 돼요.", "For example a status box allows only pending, done or cancelled — no new words.")),
        ("프롬프트", "Prompt", ("조련 쪽지.", "The trainer note."), ('양식을 주는 것도 쪽지의 일부예요. → <a href="prompt-ko.html">조련 쪽지</a>', 'Handing over the form is part of the note. → <a href="prompt-en.html">the trainer note</a>')),
    ],
}
