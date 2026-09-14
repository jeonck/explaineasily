from _draw import *
from _world import *

SCREEN = "#1E2E4A"
SCREEN_INK = "#F5F1E8"
SCREEN_TILE = "#2A3D5E"


def bell(x, y, s=1.0, ring=False):
    """종. ring=True 면 흔들림 선."""
    r = '<path d="M-34 -14 l-8 -8 M-36 6 l-10 0 M34 -14 l8 -8 M36 6 l10 0" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>' if ring else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-22 14 q0 -30 22 -34 q22 4 22 34 l6 8 h-56z" fill="#E9B44C" stroke="#B5892C" stroke-width="2"/>'
            f'<circle cy="28" r="6" fill="#B5892C"/><rect x="-3" y="-26" width="6" height="8" rx="2" fill="#B5892C"/>{r}</g>')


def clock(x, y, r=16):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M{x} {y} V{y - r + 5} M{x} {y} H{x + r - 6}" stroke="var(--ink)" stroke-width="2.5" stroke-linecap="round"/>')


# 1. 손님 앞에 내놓은 뒤: 어느 날 답이 이상 — 언제부터, 왜인지 아무도 몰라요
P1 = svg(300, sky(300)
         + person(40, 110, s=0.8, face=FROWN, **GUEST) + bubble(20, 40, 170, 36, "⟦어제까진 괜찮았는데|it was fine yesterday⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(300, 200, 140) + parrot(300, 160, 1.1, color=PARROT_BAD, talk=True)
         + bubble_parrot(230, 50, 220, 40, "⟦정산은… 산을 정리하는 거요|settle… like settling down⟧", 11, bad=True)
         + person(520, 110, s=0.9, face=FROWN, extra=SWEAT, **TRAINER)
         + bubble(470, 30, 270, 40, "⟦언제부터? 왜? 몰라요…|since when? why? no idea…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + note(620, 120, 110, 80, "⟦기록|LOG⟧", ("⟦(비어 있음)|(empty)⟧",), 0.9)
         + label(380, 282, "⟦어느 날 답이 이상해졌는데, 언제부터인지 왜인지 아무도 몰라요|one day the answers went odd — nobody knows since when, or why⟧", 13, "var(--ink)"))

# 2. 앵무새·쪽지·서가가 계속 바뀌는데 기록이 없고, 답은 매번 달라요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + label(380, 30, "⟦계속 바뀌는데 아무도 안 적어요|things keep changing, nobody writes it down⟧", 13, "var(--ink)", cls="d")
         + parrot(110, 120, 0.9) + label(110, 175, "⟦앵무새가 새 판으로|new parrot version⟧", 11, "var(--muted)")
         + note(230, 60, 130, 80, "⟦쪽지 v?|NOTE v?⟧", ("⟦누가 고쳤지?|who changed it?⟧",), 0.9) + label(290, 175, "⟦쪽지가 바뀜|the note changed⟧", 11, "var(--muted)")
         + books(450, 150, 5, 1.0) + label(450, 175, "⟦서가가 바뀜|the shelves changed⟧", 11, "var(--muted)")
         + note(560, 60, 170, 80, "⟦기록|LOG⟧", ("⟦(없음)|(none)⟧",), 0.9) + label(645, 175, "⟦기록이 없어요|no record⟧", 11, "var(--bad)")
         + bubble(40, 205, 140, 32, "⟦정산이 뭐야?|what is settle?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble_parrot(220, 205, 170, 32, "⟦월말 돈 맞추기|month-end tally⟧", 11)
         + bubble_parrot(420, 205, 170, 32, "⟦산을 정리하기|settling down⟧", 11, bad=True)
         + label(670, 225, "⟦같은 질문, 다른 답|same question, different answer⟧", 11, "var(--ink)")
         + label(380, 272, "⟦답이 매번 달라서 고장인지 알아채기 어려워요|answers differ every time, so a breakdown is hard to spot⟧", 11, "var(--bad)")
         + label(380, 300, "⟦바뀐 건 많은데 적힌 건 없고, 답은 원래 매번 달라요|lots changed, nothing written down — and answers vary anyway⟧", 12, "var(--ink)"))

# 3. LLMOps = 앵무새를 매일 돌보는 일 (hero)
P3 = svg(360, sky(360)
         + note(30, 40, 130, 80, "⟦쪽지 v4|NOTE v4⟧", ("⟦v3 → v4 적어 둠|v3 → v4 logged⟧",), 0.9) + label(95, 138, "⟦쪽지 버전 적기|note versions⟧", 11, "var(--muted)")
         + note(30, 170, 130, 90, "⟦대화 기록|CHAT LOG⟧", ("⟦09:00 정산?|09:00 settle?⟧", "⟦09:01 답 ✓|09:01 answer ✓⟧"), 0.9) + label(95, 280, "⟦대화 기록하기|log the chats⟧", 11, "var(--muted)")
         + bean(215, 80, 1.0) + bean(251, 80, 1.0) + clock(300, 80) + label(258, 112, "⟦콩 값·시간 재기|measure beans and time⟧", 11, "var(--muted)")
         + label(380, 112, "⟦매일 돌봐요|daily care⟧", 13, "var(--ink)", cls="d")
         + perch(380, 230, 150) + parrot(380, 190, 1.3, talk=True)
         + person(460, 120, s=0.9, face=SMILE, **TRAINER) + label(492, 250, "⟦돌보는 사람|the keeper⟧", 11, "var(--muted)")
         + note(580, 40, 150, 80, "⟦시험|TEST⟧", ("⟦오늘 점수 92|today: 92⟧",), 0.9) + label(655, 138, "⟦시험 돌리기|run the tests⟧", 11, "var(--muted)")
         + bell(660, 200, 1.0, ring=True) + label(660, 262, "⟦이상하면 종 울리기|ring when odd⟧", 11, "var(--muted)")
         + label(380, 340, "⟦LLMOps = 앵무새를 매일 돌보는 일 — 적고, 기록하고, 재고, 시험하고, 이상하면 종|LLMOps: caring for the parrot every day — write, log, measure, test, and ring the bell⟧", 13, "var(--ink)", cls="d"))

# 4. 관제 화면 — 쪽지 v3→v4, 콩 값 그래프, 시험 점수, 종
def tile(x, w, title):
    return f'<rect x="{x}" y="75" width="{w}" height="175" rx="8" fill="{SCREEN_TILE}"/>' + label(x + w / 2, 98, title, 12, SCREEN_INK, cls="d")


P4 = svg(320, sky(320)
         + f'<rect x="30" y="30" width="700" height="240" rx="10" fill="{SCREEN}"/>' + label(380, 57, "⟦관제 화면|CONTROL BOARD⟧", 13, SCREEN_INK, cls="d")
         + tile(50, 150, "⟦쪽지 버전|NOTE VERSION⟧") + label(125, 150, "⟦v3 → v4|v3 → v4⟧", 22, SCREEN_INK, cls="d") + label(125, 180, "⟦오늘 10:00 바꿈|changed today 10:00⟧", 10, "#C9D5E6") + label(125, 225, "⟦되돌리기 ✓|roll back ✓⟧", 11, "#5CC48A")
         + tile(220, 170, "⟦콩 값|BEAN COST⟧")
         + '<path d="M240 230 H370 M240 120 V230" stroke="#C9D5E6" stroke-width="1.5"/><path d="M245 200 L275 195 L305 190 L335 150 L365 130" stroke="#E9B44C" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="335" cy="150" r="5" fill="#E06C5B"/>'
         + label(345, 118, "⟦10시부터 쑥|up since 10⟧", 10, "#E06C5B")
         + tile(410, 170, "⟦시험 점수|TEST SCORE⟧") + label(495, 150, "⟦92 → 88|92 → 88⟧", 22, SCREEN_INK, cls="d") + label(495, 180, "⟦거절률 3%|refusals 3%⟧", 10, "#C9D5E6") + label(495, 225, "⟦점수 떨어짐|score dropped⟧", 11, "#E06C5B")
         + tile(600, 110, "⟦종|ALARM⟧") + bell(655, 160, 0.9, ring=True) + label(655, 225, "⟦울리는 중!|ringing!⟧", 11, "#E06C5B")
         + label(380, 300, "⟦한 화면에서 봐요 — 쪽지가 바뀌자 콩 값이 오르고 점수가 떨어졌어요|one board shows it — the note changed, beans went up, the score went down⟧", 12, "var(--ink)"))

# 5. 앵무새가 안 바뀌어도 손님 질문이 바뀌면 답이 나빠져요(드리프트) — 그래서 계속 봐요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 30, "⟦앵무새는 안 바뀌었는데|the parrot did not change⟧", 13, "var(--ink)", cls="d")
         + parrot(80, 150, 1.0) + label(80, 205, "⟦그대로|same bird⟧", 10, "var(--muted)")
         + person(180, 95, s=0.7, face=EYES, **GUEST) + bubble(150, 40, 150, 34, "⟦환불은 어떻게 해?|how do refunds work?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble_parrot(240, 120, 130, 34, "⟦음… 정산?|um… settle?⟧", 11, bad=True)
         + label(270, 205, "⟦손님 질문이 달라졌어요|the guests ask new things⟧", 11, "var(--ink)")
         + label(190, 262, "⟦답이 나빠져요 — 드리프트|answers get worse — drift⟧", 11, "var(--bad)")
         + label(570, 30, "⟦그래서 계속 봐요|so we keep watching⟧", 13, "var(--ink)", cls="d")
         + person(420, 110, s=0.8, face=SMILE, **TRAINER)
         + f'<rect x="500" y="70" width="110" height="80" rx="6" fill="{SCREEN}"/>' + label(555, 92, "⟦시험|TEST⟧", 11, SCREEN_INK, cls="d")
         + '<path d="M512 135 L535 120 L558 125 L580 110 L598 118" stroke="#E9B44C" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + note(630, 60, 110, 90, "⟦할 일|TO DO⟧", ("⟦시험 돌리기|run tests⟧", "⟦쪽지 v5 시험|try note v5⟧"), 0.9)
         + label(580, 185, "⟦시험·콩 값·거절률을 매일 봐요|tests, beans, refusals — daily⟧", 11, "var(--ink)")
         + label(580, 210, "⟦이상하면 종을 울리고 울타리를 손봐요|ring the bell, mend the fence⟧", 11, "var(--ink)")
         + label(570, 262, "⟦돌보기는 끝이 없어요|the caring never ends⟧", 11, "var(--good)")
         + label(380, 300, "⟦앵무새가 그대로여도 세상이 바뀌면 답이 나빠져요 — 그래서 계속 봐요|even with the same bird, a changing world spoils answers — so keep watching⟧", 12, "var(--ink)", cls="d"))

VERSION_I = icon('<rect x="18" y="16" width="34" height="42" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="34" height="42" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="34" height="10" rx="3" fill="#C9A86A"/><text x="29" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="#142033">v4</text>')
LOG_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 22 h28 M18 31 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><rect x="18" y="38" width="22" height="8" rx="2" fill="#142033"/><path d="M44 36 l6 6 M50 36 l-6 6" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
COMPARE_I = icon('<rect x="8" y="14" width="20" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><rect x="36" y="14" width="20" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/><text x="18" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="#142033">92</text><text x="46" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="#142033">88</text><path d="M28 32 h8" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><path d="M40 54 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none"/>')
GAUGE_I = icon('<circle cx="32" cy="34" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 L44 20" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="4" fill="var(--accent)"/><path d="M14 46 q18 -30 36 0" stroke="var(--line)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>')

PAGE = {
    "slug": "llmops", "order": 37,
    "title": ("앵무새 돌보기", "Caring for the Parrot"),
    "h1": ("<em>LLMOps</em>가 뭐예요?", "What is <em>LLMOps</em>?"),
    "sub": ("LLMOps 를 손님 앞에 내놓은 앵무새를 매일 돌보는 이야기 — 쪽지 버전 적기, 대화 기록, 콩 값·시간 재기, 시험, 종 울리기 — 로 풀어봤어요.",
            "LLMOps, told as a story about caring daily for a parrot that serves guests — noting note versions, logging chats, measuring beans and time, running tests, ringing the bell."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '어제까진 괜찮았는데'라고 하고, 횃대의 빨간 앵무새가 '정산은… 산을 정리하는 거요'라고 답함. 땀 흘리는 조련사가 '언제부터? 왜? 몰라요…', 옆의 '기록' 쪽지는 비어 있음", "A guest says it was fine yesterday; a red parrot on a perch says settle… like settling down. A sweating trainer says since when? why? no idea…; a LOG note beside is empty"),
         "caption": ("앵무새를 손님 앞에 내놓았어요. 어느 날 답이 이상해졌는데, 언제부터인지 왜인지 아무도 몰라요.", "The parrot serves guests now. One day its answers went odd — and nobody knows since when, or why."),
         "small": ('만드는 날은 잘 됐어요. 그런데 손님 앞에 내놓은 뒤가 진짜예요 — <a href="hallucination-ko.html">그럴듯한 오답</a>이 언제 새기 시작했는지 기록이 없으면 못 찾아요.', 'It worked fine on launch day. But life after launch is the real thing — without a record you can\'t find when the <a href="hallucination-en.html">plausible wrong answers</a> started leaking.')},
        {"svg": P2, "alt": ("위: 새 판 앵무새, '쪽지 v? 누가 고쳤지?' 쪽지, 바뀐 서가, 비어 있는 기록 쪽지. 아래: '정산이 뭐야?'에 '월말 돈 맞추기'와 빨간 '산을 정리하기' — 같은 질문, 다른 답", "Top: a new parrot version, a NOTE v? note asking who changed it, changed shelves, an empty LOG note. Bottom: what is settle? gets month-end tally and a red settling down — same question, different answer"),
         "caption": ("앵무새도 쪽지도 서가도 계속 바뀌는데 기록이 없어요. 게다가 앵무새 답은 원래 매번 달라서 고장인지 알기 어려워요.", "The parrot, the note and the shelves keep changing with no record. And parrot answers vary anyway, so a breakdown is hard to spot."),
         "small": ('<a href="prompt-ko.html">쪽지</a> 한 줄, <a href="vectordb-ko.html">서가</a> 한 칸, 앵무새 새 판 — 뭐 하나만 바뀌어도 답이 달라져요. 그런데 <a href="temperature-ko.html">엉뚱함 다이얼</a> 때문에 같은 질문도 매번 조금씩 달라서, 눈으로는 고장을 못 가려요.',
                   'One line of the <a href="prompt-en.html">note</a>, one shelf of the <a href="vectordb-en.html">library</a>, a new parrot version — change any one and answers shift. And with the <a href="temperature-en.html">silliness dial</a>, the same question already varies a little each time, so eyes alone can\'t tell a breakdown.')},
        {"svg": P3, "hero": True, "alt": ("가운데 횃대의 앵무새와 돌보는 조련사. 둘레에 '쪽지 v4 (v3 → v4 적어 둠)' 쪽지, '대화 기록' 쪽지, 콩 두 개와 시계(콩 값·시간 재기), '시험: 오늘 점수 92' 쪽지, 울리는 종", "A parrot on a perch with its keeper in the middle. Around them: a NOTE v4 note (v3 → v4 logged), a CHAT LOG note, two beans and a clock (measure beans and time), a TEST note (today: 92), a ringing bell"),
         "caption": ("LLMOps 는 앵무새를 매일 돌보는 일이에요. 쪽지 버전 적기, 대화 기록하기, 콩 값·시간 재기, 시험 돌리기, 이상하면 종 울리기.", "LLMOps is caring for the parrot every day: note versions, chat logs, measuring beans and time, running tests, ringing the bell when something is off."),
         "small": ('만들기가 끝이 아니라 돌보기가 시작이에요. 모든 바꿈을 적고, 모든 대화를 남기고, 매일 <a href="evaluation-ko.html">시험</a>을 돌려요. 그래야 "언제부터, 왜"에 답할 수 있어요.',
                   'Building is not the end; caring is the start. Write down every change, keep every chat, run the <a href="evaluation-en.html">tests</a> daily. That is how you can answer since when, and why.'),
         "tricks": (4, [
             (VERSION_I, ("쪽지도 버전이 있어요", "Notes have versions too"), ("v3 → v4, 누가 언제", "v3 → v4, who and when"), "calm"),
             (LOG_I, ("대화를 기록하되 비밀 콩은 가려요", "Log chats, mask secret beans"), ("이름·번호는 지우고", "names and numbers blanked"), "warm"),
             (COMPARE_I, ("바꾸기 전 시험, 바꾼 뒤 비교", "Test before, compare after"), ("점수가 떨어지면 되돌려요", "score drops? roll back"), "calm"),
             (GAUGE_I, ("값·시간·거절률을 매일 봐요", "Watch cost, time, refusals daily"), ("숫자가 튀면 종", "a jump rings the bell")),
         ])},
        {"svg": P4, "alt": ("관제 화면: 쪽지 버전 v3 → v4(오늘 10:00 바꿈, 되돌리기), 콩 값 그래프가 10시부터 쑥 오름, 시험 점수 92 → 88(거절률 3%, 점수 떨어짐), 종이 울리는 중", "A control board: note version v3 → v4 (changed today 10:00, roll back), a bean-cost graph rising since 10, test score 92 → 88 (refusals 3%, score dropped), an alarm bell ringing"),
         "caption": ("한 화면에서 봐요. 쪽지가 바뀌자 콩 값이 오르고 점수가 떨어졌어요 — 종이 울려요.", "One board shows it all. The note changed, beans went up, the score went down — the bell rings."),
         "small": ('쪽지 v4 가 10시에 들어갔고, 그때부터 <a href="pricing-ko.html">콩 값</a>이 오르고 시험 점수가 떨어졌어요. 이제 "언제부터, 왜"를 알아요 — 되돌리기 한 번이면 돼요.', 'Note v4 went in at 10, and from then the <a href="pricing-en.html">bean cost</a> rose and the test score fell. Now you know since when, and why — one roll back fixes it.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 앵무새는 그대로인데 손님이 '환불은 어떻게 해?'라고 새 질문을 하고, 앵무새는 '음… 정산?' — 드리프트. 오른쪽 초록: 조련사가 시험 그래프 화면과 '할 일: 시험 돌리기, 쪽지 v5 시험' 쪽지를 봄", "Left, red: the same parrot, but a guest asks a new question, how do refunds work?, and the parrot says um… settle? — drift. Right, green: a trainer watches a TEST graph screen and a TO DO note: run tests, try note v5"),
         "caption": ("앵무새가 안 바뀌어도 손님 질문이 바뀌면 답이 나빠져요(드리프트). 그래서 계속 봐요.", "Even if the parrot doesn\'t change, the guests\' questions do, and answers get worse (drift). So we keep watching."),
         "small": ('<a href="evaluation-ko.html">시험</a>은 한 번이 아니라 매일이에요. <a href="pricing-ko.html">콩 값</a>이 튀거나 <a href="guardrail-ko.html">울타리</a>에 막히는 답이 늘면 종을 울려요. 대화를 기록할 땐 <a href="aiprivacy-ko.html">비밀 콩</a>을 꼭 가려요.',
                   'The <a href="evaluation-en.html">test</a> is daily, not once. Ring the bell when the <a href="pricing-en.html">bean cost</a> jumps or more answers hit the <a href="guardrail-en.html">fence</a>. And when logging chats, always mask the <a href="aiprivacy-en.html">secret beans</a>.')},
    ],
    "summary": (("<b>LLMOps</b> = 손님 앞에 내놓은 앵무새를 <b>매일 돌보는 일</b>. 쪽지 <b>버전</b> 적기, 대화 <b>기록</b>(비밀 콩은 가리고), 콩 값·시간·거절률 <b>재기</b>, 바꾸기 전후 <b>시험</b>, 이상하면 <b>종</b>. 앵무새가 그대로여도 세상이 바뀌면 답이 나빠지니(드리프트) 계속 봐요.",
                 "<b>LLMOps</b> = <b>daily care</b> for a parrot that serves guests. <b>Version</b> the notes, <b>log</b> the chats (masking secret beans), <b>measure</b> beans, time and refusals, <b>test</b> before and after changes, ring the <b>bell</b> when something is off. Even an unchanged bird drifts as the world changes, so keep watching."),
                ("LLMOps. LLM 앱을 운영하는 일 전체예요. 프롬프트를 코드처럼 버전 관리하고, 요청·응답·도구 호출을 트레이싱해 로그로 남기며(PII 마스킹), 비용·지연 시간·거절률·품질 점수를 모니터링해요. 배포 전 평가 파이프라인으로 회귀를 잡고, 카나리 배포로 일부 트래픽에만 먼저 내보내요. 모델이 그대로여도 입력 분포가 바뀌면 품질이 떨어지는 드리프트 때문에 평가는 상시로 돌려요.",
                 "Everything involved in operating an LLM app. Version prompts like code, trace requests, responses and tool calls into logs (with PII masking), and monitor cost, latency, refusal rate and quality scores. Catch regressions with an evaluation pipeline before deploying, and use canary releases to expose changes to a slice of traffic first. Because quality drifts as the input distribution shifts even when the model doesn\'t change, evaluation runs continuously.")),
    "glossary": [
        ("LLMOps", "LLMOps", ("앵무새 매일 돌보기.", "Caring for the parrot daily."), ("만든 뒤가 진짜예요. 적고, 기록하고, 재고, 시험하고, 종 울리기.", "The real work starts after building: write, log, measure, test, ring the bell.")),
        ("프롬프트 버전 관리", "Prompt versioning", ("쪽지에 v3, v4 적기.", "Writing v3, v4 on the notes."), ('누가 언제 뭘 바꿨는지 남겨요. 나빠지면 전 판으로 되돌려요. → <a href="prompt-ko.html">조련 쪽지</a>', 'Keep who changed what and when; roll back to the last version if things get worse. → <a href="prompt-en.html">the trainer\'s note</a>')),
        ("트레이싱 · 로그", "Tracing · logs", ("대화 기록하기.", "Logging the chats."), ('질문, 답, 도구 쪽지, 걸린 시간을 남겨요. 비밀 콩은 가려요. → <a href="aiprivacy-ko.html">비밀 콩</a>', 'Keep the question, the answer, tool notes and timings. Mask the secret beans. → <a href="aiprivacy-en.html">secret beans</a>')),
        ("평가 파이프라인", "Evaluation pipeline", ("바꿀 때마다 자동 시험.", "Automatic tests on every change."), ('쪽지나 앵무새를 바꾸면 시험지를 자동으로 풀게 해요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'Change the note or the bird and the test runs by itself. → <a href="evaluation-en.html">the examiner\'s scorecard</a>')),
        ("모니터링", "Monitoring", ("값·시간·품질을 매일 보기.", "Watching cost, time and quality daily."), ('콩 값, 답하는 시간, 거절률, 시험 점수를 화면에 띄워요. → <a href="pricing-ko.html">콩 값</a>', 'Put bean cost, answer time, refusal rate and test score on the board. → <a href="pricing-en.html">the bean bill</a>')),
        ("드리프트", "Drift", ("앵무새는 그대로인데 답이 나빠짐.", "Same bird, worse answers."), ("손님 질문이 바뀌거나 세상이 바뀌면 생겨요. 그래서 시험은 한 번이 아니라 계속이에요.", "Happens when the guests\' questions or the world change. That is why testing is continuous, not once.")),
        ("카나리 배포", "Canary release", ("손님 열 중 하나에게만 먼저.", "Just one guest in ten first."), ("새 쪽지를 일부 손님에게만 내놓고 종이 안 울리면 나머지에게도 내놓아요.", "Show the new note to a few guests; if the bell stays quiet, roll it out to the rest.")),
        ("가드레일", "Guardrail", ("울타리.", "The fence."), ('울타리에 막히는 답이 갑자기 늘면 뭔가 바뀐 거예요. → <a href="guardrail-ko.html">울타리</a>', 'A sudden rise in answers hitting the fence means something changed. → <a href="guardrail-en.html">the fence</a>')),
    ],
}
