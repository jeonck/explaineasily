from _draw import *
from _world import *

CARPENTER = dict(hat="#8B5E3C", shirt="#C9822B")  # 목수 (개발자 손님)
INK_LIGHT = "#F2F6FC"


def arrow(x1, y1, x2, y2, color="var(--muted)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{x2 - 10} {y2 - 6} L{x2} {y2} L{x2 - 10} {y2 + 6}" stroke="{color}" stroke-width="3" fill="none"/>')


def code(x, y, text, size=11, fill=PAPER_INK, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="700" font-family="ui-monospace, Menlo, monospace" fill="{fill}">{text}</text>'


def screen(x, y, w, h, lines):
    """검은 화면. lines = [(text, color)]. 글자는 고정 배경이라 literal 색."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#142033"/><rect x="{x}" y="{y}" width="{w}" height="18" rx="8" fill="#2A3A55"/>'
            f'<circle cx="{x + 12}" cy="{y + 9}" r="4" fill="var(--bad)"/><circle cx="{x + 26}" cy="{y + 9}" r="4" fill="#E9B44C"/><circle cx="{x + 40}" cy="{y + 9}" r="4" fill="var(--good)"/>'
            + "".join(code(x + 14, y + 40 + i * 20, t, 11, c) for i, (t, c) in enumerate(lines)))


def toolbox(x, y, w=130, h=80):
    """도구 상자: 파일 열기 · 실행 · 찾기."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{WOOD}"/><rect x="{x}" y="{y}" width="{w}" height="16" rx="8" fill="#5A3B22"/>'
            f'<rect x="{x + 14}" y="{y + 30}" width="26" height="34" rx="3" fill="{PAPER}" stroke="#C9A86A" stroke-width="2"/><path d="M{x + 20} {y + 42} h14 M{x + 20} {y + 50} h10" stroke="{PAPER_INK}" stroke-width="2" stroke-linecap="round"/>'
            f'<path d="M{x + 54} {y + 32} l26 15 l-26 15z" fill="var(--good)"/>'
            f'<circle cx="{x + 100}" cy="{y + 44}" r="10" fill="none" stroke="{PAPER}" stroke-width="3"/><path d="M{x + 107} {y + 51} l8 8" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>')


# 1. 목수가 "이 함수 왜 안 돼?" — 앵무새는 코드 책도 읽었어요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, talk=True)
         + bubble_parrot(80, 30, 240, 40, "⟦코드 책도 산더미로 읽었어요!|I read a mountain of code too!⟧", 12)
         + note(400, 120, 120, 90, "⟦코드|CODE⟧", ("⟦def add(a, b):|def add(a, b):⟧", "⟦  return a - b|  return a - b⟧"), 0.9)
         + label(455, 240, "⟦(더하기인데 빼기를 써요)|(it subtracts instead of adding)⟧", 10, "var(--muted)")
         + person(560, 120, s=0.9, face=FROWN, **CARPENTER) + bubble(430, 30, 280, 40, "⟦이 함수 왜 안 돼?|why does this function not work?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦코드도 글이에요 — 앵무새가 읽은 책 더미엔 코드가 잔뜩 있어요|code is text too — the pile the parrot read is full of code⟧", 13, "var(--ink)"))

# 2. 왜 잘하나: 규칙이 촘촘하고 예제가 산더미 / 왜 위험하나: 그럴듯한 코드도 이어 붙임
P2 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + books(80, 200, 5, 1.0) + label(80, 222, "⟦코드 책 산더미|mountains of code⟧", 11, "var(--muted)")
         + beans(160, 80, ("⟦for|for⟧", "⟦i|i⟧", "⟦in|in⟧"), 0.9, 44) + '<rect x="275" y="62" width="44" height="36" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(297, 86, "⟦?|?⟧", 20, "var(--accent)", cls="d")
         + note(180, 115, 170, 80, "⟦다음 콩|NEXT BEAN⟧", ("⟦range ★★★★★|range ★★★★★⟧", "⟦banana ☆|banana ☆⟧"), 0.9, 0)
         + label(250, 245, "⟦규칙이 촘촘해서 잘 맞아요|tight rules — the bean fits well⟧", 11, "var(--ink)")
         + parrot(470, 140, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(400, 40, 220, 40, "⟦import magiclib 하면 돼요!|just import magiclib!⟧", 11, bad=True)
         + note(600, 110, 130, 80, "⟦코드|CODE⟧", ("⟦import magiclib|import magiclib⟧", "⟦magiclib.fix()|magiclib.fix()⟧"), 0.9)
         + label(660, 205, "⟦(그런 도구는 없어요)|(no such library exists)⟧", 11, "var(--bad)")
         + label(570, 245, "⟦그럴듯한 코드도 이어 붙여요|it continues plausible code too⟧", 11, "var(--ink)")
         + label(380, 282, "⟦잘 맞아서 좋고, 그럴듯해서 위험해요|good because it fits — risky because it is plausible⟧", 12, "var(--ink)", cls="d"))

# 3. 코딩 앵무새 = 코드를 읽고 쓰고, 도구 상자로 직접 돌려 보며 고치는 앵무새 (hero)
P3 = svg(360, sky(360)
         + note(260, 40, 150, 90, "⟦쪽지|NOTE⟧", ("⟦테스트 통과시켜 줘|make the tests pass⟧", "⟦파일: add.py|file: add.py⟧"), 0.9)
         + perch(160, 240, 150) + parrot(160, 200, 1.4, talk=True)
         + toolbox(250, 170) + label(315, 275, "⟦도구 상자: 열기 · 실행 · 찾기|toolbox: open · run · search⟧", 11, "var(--muted)")
         + arrow(390, 210, 430, 210)
         + screen(440, 50, 290, 200, (("def add(a, b):", INK_LIGHT), ("    return a + b", INK_LIGHT), ("", INK_LIGHT), ("> run tests", "#9AA6B8"), ("× 1 failed  (a - b)", "#FF6B6B"), ("> fix, run again", "#9AA6B8"), ("✓ 3 passed", "#7BD88F")))
         + label(585, 275, "⟦직접 돌려 보고, 틀리면 고쳐요|it runs the code and fixes what fails⟧", 11, "var(--muted)")
         + label(380, 340, "⟦코딩 앵무새 = 코드를 읽고 쓰고, 도구로 직접 돌려 보며 고치는 앵무새|a coding parrot reads and writes code, runs it with its tools, and fixes it⟧", 13, "var(--ink)", cls="d"))

# 4. 루프: 쪽지 → 코드 → 실행(빨간 오류) → 고침 → 초록 통과
BOX = lambda x, fill="var(--panel)", stroke="var(--line)": f'<rect x="{x}" y="70" width="120" height="100" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
P4 = svg(320, sky(320)
         + BOX(30) + note(55, 85, 70, 70, "⟦쪽지|NOTE⟧", ("⟦더하기|add⟧",), 0.95)
         + BOX(175) + code(195, 110, "def add(a,b):", 10) + code(195, 128, "  return a-b", 10)
         + BOX(320, "var(--bad-soft)", "var(--bad)") + label(380, 108, "⟦실행|run⟧", 11, "var(--muted)") + label(380, 140, "⟦× 오류|× error⟧", 16, "var(--bad)", cls="d")
         + BOX(465) + code(485, 110, "def add(a,b):", 10) + code(485, 128, "  return a+b", 10) + '<path d="M540 150 l14 -10" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
         + BOX(610, "var(--good-soft)", "var(--good)") + label(670, 108, "⟦실행|run⟧", 11, "var(--muted)") + label(670, 140, "⟦✓ 통과|✓ pass⟧", 16, "var(--good)", cls="d")
         + arrow(152, 120, 173, 120) + arrow(297, 120, 318, 120) + arrow(442, 120, 463, 120) + arrow(587, 120, 608, 120)
         + '<path d="M380 68 Q 380 30 240 30 Q 235 30 235 66" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="6 5"/><path d="M229 58 L235 68 L241 58" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(310, 20, "⟦오류를 돌려주면 다시|hand back the error, try again⟧", 11, "var(--accent)")
         + label(90, 195, "⟦쪽지|note⟧", 11, "var(--muted)") + label(235, 195, "⟦코드|code⟧", 11, "var(--muted)") + label(380, 195, "⟦빨간 오류|red error⟧", 11, "var(--muted)") + label(525, 195, "⟦고침|fix⟧", 11, "var(--muted)") + label(670, 195, "⟦초록 통과|green pass⟧", 11, "var(--muted)")
         + label(380, 240, "⟦오류를 돌려주면 앵무새가 스스로 고쳐요 — 몇 바퀴 돌아요|hand back the error and the parrot fixes it itself — a few laps⟧", 12, "var(--ink)")
         + label(380, 268, "⟦테스트를 먼저 주면 바퀴가 줄어요|give the tests first and the laps get fewer⟧", 11, "var(--muted)")
         + label(380, 300, "⟦통과 = 테스트가 시킨 것만 맞는다는 뜻이에요|pass means it matches what the tests asked — nothing more⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 통과했다고 안전한 게 아니에요 + 이해 없이 이어 붙인 코드는 나중에 아무도 못 고쳐요
LOCK_OPEN = ('<rect x="590" y="90" width="44" height="34" rx="6" fill="var(--bad)"/><path d="M598 90 V72 a14 14 0 0 1 28 0 V80" stroke="var(--bad)" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="612" cy="107" r="5" fill="#FFF"/>')
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(80, 150, 0.9, talk=True) + note(140, 60, 130, 80, "⟦코드|CODE⟧", ("⟦✓ 3 통과|✓ 3 passed⟧",), 0.9)
         + person(290, 100, s=0.8, face=SMILE, **TRAINER) + label(318, 208, "⟦사람이 읽어요|a person reads it⟧", 11, "var(--ink)")
         + label(190, 250, "⟦읽고, 이해하고, 그다음 합쳐요|read, understand, then merge⟧", 11, "var(--ink)")
         + note(420, 60, 150, 90, "⟦코드|CODE⟧", ("⟦✓ 3 통과|✓ 3 passed⟧", "⟦password = 1234|password = 1234⟧"), 0.9)
         + LOCK_OPEN + label(625, 145, "⟦보안 틈|a hole⟧", 11, "var(--bad)")
         + label(570, 190, "⟦통과했다고 안전한 건 아니에요|passing is not the same as safe⟧", 11, "var(--ink)")
         + label(570, 250, "⟦이해 없이 붙인 코드는 나중에 아무도 못 고쳐요|code pasted without understanding — later nobody can fix it⟧", 11, "var(--bad)")
         + label(380, 300, "⟦초록 ✓ 다음엔 사람 눈 — 안전과 이해는 사람 몫이에요|after the green ✓, a person\'s eyes — safety and understanding are theirs⟧", 12, "var(--ink)", cls="d"))

SMALL_I = icon('<rect x="10" y="18" width="44" height="28" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="37" text-anchor="middle" font-size="11" font-weight="700" font-family="ui-monospace, monospace" fill="#142033">add()</text>')
TEST_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 l4 4 l7 -8 M20 36 l4 4 l7 -8" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M34 22 h12 M34 36 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><text x="32" y="53" text-anchor="middle" font-size="9" font-weight="700" fill="#142033">1st</text>')
LOOP_I = icon('<path d="M46 22 a16 16 0 1 0 4 12" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 12 l8 10 l-12 4z" fill="var(--accent)"/><path d="M26 30 l10 6 l-10 6z" fill="var(--good)"/>')
REVIEW_I = icon(f'<circle cx="24" cy="22" r="10" fill="{SKIN}"/><rect x="14" y="34" width="20" height="18" rx="5" fill="var(--good)"/><rect x="40" y="18" width="16" height="22" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M44 26 h8 M44 32 h8" stroke="#142033" stroke-width="2" stroke-linecap="round"/><path d="M42 50 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "codegen", "order": 25,
    "title": ("코드 쓰는 앵무새", "The Parrot That Writes Code"),
    "h1": ("<em>코드 생성</em>이 뭐예요?", "What is <em>Code Generation</em>?"),
    "sub": ("코드 생성과 코딩 에이전트를 코드 책을 산더미로 읽고, 도구 상자로 직접 돌려 보며 고치는 앵무새 이야기로 풀어봤어요.",
            "Code generation and coding agents, told as a story about a parrot that read a mountain of code and fixes it by running it with its own toolbox."),
    "panels": [
        {"svg": P1, "alt": ("목수가 'def add(a, b): return a - b' 코드 쪽지를 들고 왜 안 되냐고 묻고, 앵무새는 코드 책도 산더미로 읽었다고 말함", "A carpenter holds a code note reading def add(a, b): return a - b and asks why it fails; the parrot says it read a mountain of code too"),
         "caption": ("목수가 물어요. 이 함수 왜 안 돼? 앵무새는 코드 책도 산더미로 읽었어요.", "The carpenter asks: why does this function fail? The parrot read a mountain of code too."),
         "small": ('코드도 글이에요. <a href="llm-ko.html">앵무새가 읽은 책 더미</a>에는 백과사전, 소설, 그리고 코드가 잔뜩 있어요.',
                   'Code is text too. <a href="llm-en.html">The pile the parrot read</a> holds encyclopedias, novels, and a lot of code.')},
        {"svg": P2, "alt": ("왼쪽 초록: 코드 책 더미, 'for i in' 콩 다음 후보에 range ★★★★★. 오른쪽 빨강: 빨간 앵무새가 'import magiclib 하면 돼요'라고 하는데 그런 도구는 없음", "Left, green: a pile of code books; after the beans for i in, the next-bean note ranks range ★★★★★. Right, red: a red parrot says just import magiclib — no such library exists"),
         "caption": ("코드는 규칙이 촘촘해서 잘 맞아요. 그런데 그럴듯한 코드도 이어 붙여요.", "Code has tight rules, so the beans fit well. But it continues plausible code too."),
         "small": ('예제가 산더미라 다음 콩이 잘 맞아요. 대신 없는 도구를 부르거나 없는 함수를 쓰는 <a href="hallucination-ko.html">그럴듯 앵무새</a>가 코드에도 나와요.',
                   'With mountains of examples, the next bean fits well. But the <a href="hallucination-en.html">plausible parrot</a> shows up in code too — calling libraries and functions that do not exist.')},
        {"svg": P3, "hero": True, "alt": ("'테스트 통과시켜 줘' 쪽지, 횃대 위 앵무새, 열기·실행·찾기 도구 상자, 검은 화면에 코드와 '× 1 failed' 다음 '✓ 3 passed'", "A note reading make the tests pass, the parrot on its perch, a toolbox with open, run, search, and a dark screen showing code, × 1 failed, then ✓ 3 passed"),
         "caption": ("코딩 앵무새는 코드를 읽고 쓰고, 도구로 직접 돌려 보며 고치는 앵무새예요.", "A coding parrot reads and writes code, runs it with its tools, and fixes it."),
         "small": ('<a href="toolcall-ko.html">도구 상자</a>에 파일 열기·실행·검색이 들어 있어요. 스스로 돌려 보고 고치는 앵무새를 코딩 에이전트라고 불러요.',
                   'The <a href="toolcall-en.html">toolbox</a> holds open-file, run, and search. A parrot that runs and fixes on its own is called a coding agent.'),
         "tricks": (4, [
             (SMALL_I, ("작게 시켜요", "Ask for small pieces"), ("함수 하나씩", "one function at a time"), "calm"),
             (TEST_I, ("테스트를 먼저 줘요", "Give the tests first"), ("맞출 목표가 생겨요", "now it has a target"), "calm"),
             (LOOP_I, ("실행 결과를 돌려줘요", "Hand back the result"), ("스스로 고쳐요", "it fixes itself"), "warm"),
             (REVIEW_I, ("사람이 읽고 합쳐요", "A person reads and merges"), ("마지막은 사람이", "the last step is human"), "warm"),
         ])},
        {"svg": P4, "alt": ("칸 다섯 개: 쪽지 → 코드(a-b) → 빨간 × 오류 → 고침(a+b) → 초록 ✓ 통과. 오류 칸에서 코드 칸으로 되돌아가는 점선 화살표", "Five boxes: note → code (a-b) → red × error → fix (a+b) → green ✓ pass; a dashed arrow loops from the error box back to the code box"),
         "caption": ("쪽지, 코드, 빨간 오류, 고침, 초록 통과. 오류를 돌려주면 몇 바퀴 돌아요.", "Note, code, red error, fix, green pass. Hand back the error and it runs a few laps."),
         "small": ("테스트를 먼저 주면 바퀴가 줄어요. 통과는 테스트가 시킨 것만 맞는다는 뜻이에요 — 그 이상은 아니에요.", "Give the tests first and the laps get fewer. Pass means it matches what the tests asked — nothing more.")},
        {"svg": P5, "alt": ("왼쪽 초록: 통과한 코드를 조련사가 읽음 — 읽고 이해하고 합침. 오른쪽 빨강: 통과했지만 password = 1234 가 들어 있고 열린 자물쇠 — 보안 틈", "Left, green: a trainer reads the passing code — read, understand, merge. Right, red: passing code containing password = 1234 and an open padlock — a security hole"),
         "caption": ("통과했다고 안전한 건 아니에요. 그리고 이해 없이 붙인 코드는 나중에 아무도 못 고쳐요.", "Passing is not the same as safe. And code pasted without understanding — later nobody can fix it."),
         "small": ('보안 틈은 <a href="codescan-ko.html">코드 검사</a>로 따로 찾아요. 초록 ✓ 다음엔 <a href="humanloop-ko.html">사람 눈</a>이 와요. 스스로 순서를 짜는 앵무새는 <a href="agent-ko.html">에이전트</a> 이야기에서.',
                   'Security holes are found separately with <a href="codescan-en.html">code scanning</a>. After the green ✓ come <a href="humanloop-en.html">human eyes</a>. The parrot that plans its own steps is the <a href="agent-en.html">agent</a> story.')},
    ],
    "summary": (("<b>코드 생성</b> = 코드 책을 산더미로 읽은 앵무새가 <b>다음 코드 콩</b>을 잘 고르는 것. <b>코딩 에이전트</b>는 도구 상자로 <b>직접 돌려 보고 고치는</b> 앵무새예요. 통과 ✓ 다음엔 사람이 읽어요.",
                 "<b>Code generation</b> = a parrot that read a mountain of code picking the <b>next code bean</b> well. A <b>coding agent</b> is the parrot that <b>runs and fixes</b> with its toolbox. After the ✓, a person reads."),
                ("Code generation / coding agent. 코드는 문법이 엄격하고 공개 예제가 방대해 LLM 의 다음 토큰 예측이 특히 잘 맞아요. 코딩 에이전트는 파일 읽기·쓰기·실행·검색 같은 도구 호출로 테스트를 돌리고 오류를 피드백 삼아 반복 수정해요. 존재하지 않는 API 호출(할루시네이션), 보안 취약점, 유지보수 불가 코드가 대표적 위험이라 코드 리뷰와 시큐어 코딩 검사가 필요해요.",
                 "Code has strict grammar and vast public examples, so next-token prediction fits it especially well. A coding agent uses tool calls (read, write, run, search) to run tests and iterate on the errors. Typical risks are calls to APIs that do not exist (hallucination), security vulnerabilities, and unmaintainable code, so code review and secure-coding scans are needed.")),
    "glossary": [
        ("코드 생성", "Code generation", ("코드 쓰는 앵무새.", "The parrot that writes code."), ("규칙이 촘촘하고 예제가 산더미라 다음 콩이 잘 맞아요.", "Tight rules and mountains of examples make the next bean fit well.")),
        ("코딩 에이전트", "Coding agent", ("도구 상자 든 앵무새.", "The parrot with a toolbox."), ('파일 열고, 돌려 보고, 고쳐요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'Opens files, runs them, fixes them. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
        ("코드 완성", "Code completion", ("다음 줄 미리 말하기.", "Saying the next line first."), ("타자 치는 동안 다음 콩 몇 개를 미리 보여줘요.", "While you type, it shows the next few beans ahead of time.")),
        ("테스트 주도", "Test-driven", ("맞출 목표를 먼저.", "The target first."), ("테스트를 먼저 주면 앵무새가 그걸 통과시키려 고쳐요.", "Give the tests first and the parrot fixes the code to pass them.")),
        ("실행 피드백", "Execution feedback", ("빨간 오류 돌려주기.", "Handing back the red error."), ("오류 메시지를 다시 보여주면 스스로 고쳐요. 몇 바퀴 돌아요.", "Show it the error message and it fixes itself. A few laps.")),
        ("코드 리뷰", "Code review", ("사람이 읽고 합쳐요.", "A person reads and merges."), ('통과 ✓ 다음 단계. → <a href="humanloop-ko.html">마지막은 사람이</a>', 'The step after the ✓. → <a href="humanloop-en.html">the last step is human</a>')),
        ("시큐어 코딩", "Secure coding", ("보안 틈 찾기.", "Finding the security hole."), ('통과했다고 안전하진 않아요. → <a href="codescan-ko.html">코드 검사</a>', 'Passing does not mean safe. → <a href="codescan-en.html">code scanning</a>')),
        ("도구 호출", "Tool calling", ("도구 상자.", "The toolbox."), ('앵무새가 도구를 써 달라는 쪽지를 쓰면 조련사가 실행해요. → <a href="toolcall-ko.html">도구 상자</a>', 'The parrot writes a note asking for a tool and the trainer runs it. → <a href="toolcall-en.html">the toolbox</a>')),
    ],
}
