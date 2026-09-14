from _draw import *
from _world import *

ANSWER = ("⟦파리|Paris⟧", "⟦는|is⟧", "⟦프랑스|France⟧", "⟦의|the⟧", "⟦수도|capital⟧")


def screen(x, y, w, h, inner=""):
    """손님 화면. inner 는 (x,y) 기준 절대 좌표로 그린다."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="var(--stone-dark)"/>'
            f'<rect x="{x + 10}" y="{y + 10}" width="{w - 20}" height="{h - 20}" rx="4" fill="var(--panel)"/>' + inner)


def clock(x, y, r, text, color="var(--ink)"):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M{x} {y} V{y - r * 0.7} M{x} {y} L{x + r * 0.5} {y + r * 0.3}" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
            + label(x, y + r + 20, text, 12, color, cls="d"))


def cursor(x, y):
    return f'<rect x="{x}" y="{y}" width="3" height="18" fill="var(--accent)"/>'


# 1. 손님이 긴 답을 기다리는데 화면이 30초 동안 빈칸 — 고장난 줄 알아요
P1 = svg(300, sky(300)
         + person(80, 110, s=0.9, face=FROWN, **GUEST) + bubble(10, 30, 180, 40, "⟦고장 났나?|is it broken?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + screen(200, 60, 300, 160, label(350, 145, "⟦(빈 화면)|(blank)⟧", 14, "var(--muted)"))
         + clock(560, 100, 30, "⟦30초…|30 s…⟧", "var(--bad)")
         + parrot(670, 150, 1.0, mood="think") + label(670, 215, "⟦콩을 고르는 중|picking beans⟧", 11, "var(--muted)")
         + label(350, 250, "⟦앵무새는 일하고 있는데 손님은 몰라요|the parrot is working, but the guest cannot tell⟧", 11, "var(--ink)")
         + label(380, 282, "⟦30초 동안 빈 화면 — 손님은 고장난 줄 알아요|a blank screen for 30 seconds — the guest thinks it is broken⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새는 콩을 하나씩 만들지만, 다 만든 뒤 한꺼번에 보여주면 기다림이 길어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(100, 130, 1.0, talk=True)
         + beans(180, 100, ANSWER, 0.9, 50) + label(280, 140, "⟦하나씩 만들어요|made one at a time⟧", 11, "var(--muted)")
         + '<rect x="420" y="60" width="150" height="110" rx="8" fill="var(--panel)" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(495, 88, "⟦모아 두기|holding⟧", 12, "var(--bad)", cls="d")
         + "".join(bean(450 + (i % 3) * 40, 118 + (i // 3) * 26, 0.6) for i in range(5))
         + label(495, 195, "⟦다 될 때까지 보여 주지 않아요|shows nothing until all are done⟧", 11, "var(--ink)")
         + person(640, 110, s=0.9, face=FROWN, **GUEST) + label(670, 235, "⟦…기다림|…waiting⟧", 11, "var(--muted)")
         + label(380, 282, "⟦한꺼번에 보여 주면, 첫 콩부터 마지막 콩까지 다 기다려요|shown all at once, the guest waits from the first bean to the last⟧", 12, "var(--bad)"))

# 3. 스트리밍 = 앵무새가 콩을 하나 고를 때마다 바로 손님에게 보여주기 (hero)
P3 = svg(360, sky(360)
         + label(380, 40, "⟦1초    2초    3초    4초 …|1 s    2 s    3 s    4 s …⟧", 12, "var(--muted)")
         + perch(150, 240, 150) + parrot(150, 200, 1.3, talk=True)
         + bean(230, 150, 0.8, text="⟦의|the⟧") + bean(290, 135, 0.8, text="⟦수도|capital⟧")
         + '<path d="M200 165 q60 -50 130 -40" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4" fill="none"/>'
         + screen(400, 70, 300, 160, beans(440, 150, ANSWER[:3], 0.9, 60) + cursor(605, 141))
         + label(550, 200, "⟦1초부터 콩이 하나씩 보여요|beans show up one by one from second one⟧", 11, "var(--muted)")
         + person(300, 230, s=0.7, face=SMILE, **GUEST)
         + label(550, 262, "⟦손님은 읽기 시작해요 — 앵무새는 아직 고르는 중|the guest starts reading — the parrot is still picking⟧", 11, "var(--ink)")
         + label(380, 340, "⟦스트리밍 = 콩을 하나 고를 때마다 바로 손님에게 보여주기|streaming: show the guest each bean the moment it is picked⟧", 13, "var(--ink)", cls="d"))


def _row(y, title, color, fills):
    out = label(30, y - 30, title, 13, color, cls="d", anchor="start")
    for i, n in enumerate(fills):
        x = 200 + i * 130
        inner = (label(x + 55, y + 42, "⟦(빈칸)|(blank)⟧", 11, "var(--muted)") if n == 0
                 else "".join(bean(x + 20 + j * 17, y + 35, 0.5) for j in range(n)))
        out += screen(x, y, 110, 70, inner)
    return out


# 4. 두 화면 비교: 한꺼번에 vs 스트리밍
P4 = svg(320, sky(320)
         + "".join(label(255 + i * 130, 40, t, 12, "var(--muted)") for i, t in enumerate(("⟦1초|1 s⟧", "⟦10초|10 s⟧", "⟦20초|20 s⟧", "⟦30초|30 s⟧")))
         + _row(70, "⟦한꺼번에|ALL AT ONCE⟧", "var(--bad)", (0, 0, 0, 5))
         + "".join(label(255 + i * 130, 180, t, 12, "var(--muted)") for i, t in enumerate(("⟦1초|1 s⟧", "⟦10초|10 s⟧", "⟦20초|20 s⟧", "⟦30초|30 s⟧")))
         + _row(210, "⟦스트리밍|STREAMING⟧", "var(--good)", (1, 2, 4, 5))
         + label(380, 304, "⟦끝나는 시각은 같아요 — 시작이 보이는 게 달라요|it finishes at the same time — the difference is seeing it start⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 빨리 보이는 것이지 빨리 끝나는 게 아니에요 + 양식은 끝까지 모아야
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + clock(100, 100, 32, "⟦첫 콩: 1초 ✓|first bean: 1 s ✓⟧", "var(--good)")
         + clock(270, 100, 32, "⟦마지막 콩: 30초|last bean: 30 s⟧", "var(--ink)")
         + label(190, 215, "⟦보이는 건 빨라졌고|it shows up sooner⟧", 12, "var(--ink)", cls="d")
         + label(190, 240, "⟦총 시간은 그대로예요|the total time is unchanged⟧", 11, "var(--muted)")
         + note(430, 50, 170, 110, "⟦도구 부탁 양식|TOOL REQUEST⟧", ("⟦도구: 계산기|tool: calculator⟧", "⟦입력: 3 +|input: 3 +⟧", "⟦(아직 오는 중)|(still arriving)⟧"), 1.0)
         + label(515, 190, "⟦반쪽 양식은 못 읽어요|a half form cannot be read⟧", 12, "var(--bad)", cls="d")
         + person(630, 70, s=0.9, face=FROWN, **TRAINER) + label(660, 200, "⟦끝까지 모아서|collect it all⟧", 11, "var(--ink)")
         + label(570, 240, "⟦도구 호출·양식은 다 온 뒤에 읽어요|tool calls and forms: read after all arrives⟧", 11, "var(--muted)")
         + label(380, 300, "⟦스트리밍은 기다림을 짧게 느끼게 해요 — 일 자체가 줄진 않아요|streaming makes the wait feel short — the work itself does not shrink⟧", 12, "var(--ink)", cls="d"))

TTFT_I = icon(f'<circle cx="26" cy="32" r="18" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M26 32 V20 M26 32 L34 37" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><ellipse cx="50" cy="44" rx="10" ry="7" fill="{BEAN}"/>')
CHANGE_I = icon(f'<ellipse cx="22" cy="32" rx="12" ry="8" fill="{BEAN}"/><ellipse cx="46" cy="32" rx="12" ry="8" fill="{BEAN}" opacity="0.4"/><path d="M34 24 h24" stroke="var(--muted)" stroke-width="2" stroke-dasharray="3 3"/><text x="46" y="36" text-anchor="middle" font-size="11" font-weight="700" fill="#142033">?</text>')
RESUME_I = icon('<path d="M8 32 h18" stroke="var(--muted)" stroke-width="4" stroke-linecap="round"/><path d="M28 32 l4 -8 l4 16 l4 -8" stroke="var(--bad)" stroke-width="3" fill="none"/><path d="M42 32 h14" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M50 26 l8 6 l-8 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
COLLECT_I = icon(f'<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="26" y="16" width="20" height="9" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/><rect x="26" y="30" width="20" height="9" rx="2" fill="#FFF" stroke="#C9A86A" stroke-width="2"/><ellipse cx="32" cy="50" rx="8" ry="5" fill="{BEAN}"/><ellipse cx="48" cy="50" rx="8" ry="5" fill="{BEAN}" opacity="0.4"/>')

PAGE = {
    "slug": "streaming", "order": 14,
    "title": ("콩을 하나씩 바로 보여주기", "Showing Each Bean Right Away"),
    "h1": ("<em>스트리밍</em>이 뭐예요?", "What is <em>streaming</em>?"),
    "sub": ("스트리밍(응답 스트리밍)을 앵무새가 콩을 하나 고를 때마다 바로 손님에게 보여주는 이야기로 풀어봤어요.",
            "Streaming (streamed responses), told as a story about the parrot showing the guest each bean the moment it picks one."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '고장 났나?' 하며 빈 화면을 보고, 시계는 30초, 오른쪽에서 앵무새는 눈을 감고 콩을 고르는 중", "A guest asks is it broken while looking at a blank screen; a clock reads 30 seconds; on the right the parrot, eyes closed, is picking beans"),
         "caption": ("30초 동안 빈 화면이에요. 손님은 고장난 줄 알아요.", "A blank screen for 30 seconds. The guest thinks it is broken."),
         "small": ('긴 답은 <a href="token-ko.html">콩</a>이 많아요. 앵무새는 열심히 고르고 있는데, 손님 화면에는 아무것도 안 보여요.',
                   'A long answer means many <a href="token-en.html">beans</a>. The parrot is busy picking, but the guest sees nothing at all.')},
        {"svg": P2, "alt": ("앵무새가 콩을 하나씩 만들어 '모아 두기' 상자에 넣고, 다 될 때까지 보여 주지 않음. 오른쪽 손님은 기다림", "The parrot makes beans one at a time and puts them in a holding box, showing nothing until all are done; the guest on the right waits"),
         "caption": ("앵무새는 원래 콩을 하나씩 만들어요. 다 만든 뒤 한꺼번에 보여 주면 기다림이 길어요.", "The parrot already makes beans one at a time. Holding them until the end makes the wait long."),
         "small": ("첫 콩은 1초 만에 나왔어요. 그런데 마지막 콩까지 모아 뒀다가 보여 주니 손님은 30초를 통째로 기다려요.", "The first bean was ready in one second. But because everything is held until the last bean, the guest waits the whole 30 seconds.")},
        {"svg": P3, "hero": True, "alt": ("횃대 위 앵무새가 고른 콩이 점선을 따라 손님 화면으로 날아가고, 화면에는 '파리 는 프랑스' 콩 셋과 깜빡이는 커서. 손님은 벌써 읽기 시작", "Beans picked by the parrot on the perch fly along a dotted line to the guest screen, which shows three beans — Paris is France — and a blinking cursor; the guest has already started reading"),
         "caption": ("스트리밍은 콩을 하나 고를 때마다 바로 손님에게 보여주는 거예요.", "Streaming shows the guest each bean the moment it is picked."),
         "small": ("1초부터 첫 콩이 보여요. 손님은 읽기 시작하고, 앵무새는 뒤에서 계속 골라요. 기다림이 짧게 느껴져요.", "The first bean appears at one second. The guest starts reading while the parrot keeps picking behind. The wait feels short."),
         "tricks": (4, [
             (TTFT_I, ("첫 콩까지 시간이 체감 속도", "Time to the first bean is what you feel"), ("첫 콩이 빠르면 빠르게 느껴요", "a quick first bean feels quick"), "calm"),
             (CHANGE_I, ("다 끝나기 전엔 답이 바뀔 수 있어요", "Until the end, it can still change"), ("마지막 콩까지 봐야 해요", "wait for the last bean")),
             (RESUME_I, ("끊기면 이어 받거나 다시", "Cut off? Resume or retry"), ("받은 콩까지는 남겨 둬요", "keep the beans you already got"), "warm"),
             (COLLECT_I, ("도구 호출·양식은 끝까지 모아요", "Tool calls and forms: collect it all"), ("반쪽 양식은 못 읽어요", "a half form cannot be read"), "warm"),
         ])},
        {"svg": P4, "alt": ("위 줄 '한꺼번에': 1초·10초·20초 화면은 빈칸, 30초에 답 전체. 아래 줄 '스트리밍': 1초에 콩 하나, 10초에 둘, 20초에 넷, 30초에 전체", "Top row, all at once: screens at 1, 10 and 20 seconds are blank, the full answer at 30. Bottom row, streaming: one bean at 1 second, two at 10, four at 20, all at 30"),
         "caption": ("끝나는 시각은 같아요. 시작이 보이는 게 달라요.", "It finishes at the same time. The difference is seeing it start."),
         "small": ("두 줄 다 30초에 끝나요. 위는 30초 동안 빈 화면, 아래는 1초부터 읽을 게 있어요.", "Both rows finish at 30 seconds. The top is blank for 30 seconds; the bottom has something to read from second one.")},
        {"svg": P5, "alt": ("왼쪽 초록: 시계 둘 — 첫 콩 1초 ✓, 마지막 콩 30초 그대로. 오른쪽 빨강: '입력: 3 +'에서 끊긴 반쪽 도구 부탁 양식을 든 조련사 — 끝까지 모아서 읽어야 함", "Left, green: two clocks — first bean 1 s ✓, last bean still 30 s. Right, red: a trainer holding a tool request form cut off at input: 3 + — it must be collected fully before reading"),
         "caption": ("스트리밍은 기다림을 짧게 느끼게 해요. 일 자체가 줄진 않아요.", "Streaming makes the wait feel short. The work itself does not shrink."),
         "small": ('빨리 보이는 것이지 빨리 끝나는 게 아니에요 — 콩 값과 총 시간은 <a href="inference-ko.html">그대로</a>예요. 그리고 <a href="structuredoutput-ko.html">양식</a>과 도구 부탁은 다 온 뒤에 읽어요.',
                   'It shows sooner, not finishes sooner — the bean cost and the total time stay <a href="inference-en.html">the same</a>. And <a href="structuredoutput-en.html">forms</a> and tool requests are read only after everything arrives.')},
    ],
    "summary": (("<b>스트리밍</b> = 앵무새가 <b>콩을 하나 고를 때마다 바로</b> 손님에게 보여주기. 첫 콩이 빨리 보여 <b>기다림이 짧게 느껴지지만</b>, 총 시간과 콩 값은 그대로예요.",
                 "<b>Streaming</b> = the parrot shows the guest <b>each bean the moment it is picked</b>. The first bean appears quickly so <b>the wait feels short</b>, but total time and bean cost stay the same."),
                ("Streaming response. 모델이 생성한 토큰을 완성 전에 청크 단위로 순차 전송해요(주로 SSE). 체감 속도는 첫 토큰 시간(TTFT)이 좌우하고, 총 지연·비용은 같아요. 도구 호출 인자나 JSON 같은 구조화 출력은 스트림이 끝나야 온전하니 모아서 파싱하고, 끊기면 취소·재시도를 다뤄야 해요.",
                 "Sends generated tokens in chunks as they are produced, before the response is complete (usually over SSE). Perceived speed is driven by time to first token (TTFT); total latency and cost are unchanged. Tool-call arguments and structured output like JSON are only whole once the stream ends, so buffer and parse them, and handle cancellation and retries when a stream drops.")),
    "glossary": [
        ("스트리밍", "Streaming", ("콩을 하나씩 바로 보여주기.", "Showing each bean right away."), ("다 만들 때까지 기다리지 않고 나오는 대로 보내요.", "Sent as they come, instead of waiting for the whole thing.")),
        ("첫 토큰 시간", "TTFT (time to first token)", ("첫 콩까지 걸린 시간.", "Time until the first bean."), ("손님이 느끼는 빠르기는 거의 이 숫자예요.", "What the guest feels as speed is mostly this number.")),
        ("초당 토큰", "Tokens per second", ("1초에 나오는 콩 수.", "Beans per second."), ("첫 콩 뒤로 얼마나 술술 나오는지.", "How smoothly beans keep coming after the first.")),
        ("SSE", "SSE (server-sent events)", ("콩을 한 줄로 흘려보내는 관.", "The pipe that trickles beans one by one."), ("한 번 연결하면 서버가 계속 조금씩 보내요. 스트리밍에 흔히 써요.", "Connect once and the server keeps sending small pieces. Commonly used for streaming.")),
        ("청크", "Chunk", ("한 번에 오는 콩 묶음.", "The batch of beans that arrives at once."), ("콩 하나일 수도, 몇 개일 수도 있어요. 이어 붙여야 답이 돼요.", "May be one bean or a few. Join them to get the answer.")),
        ("취소", "Cancellation", ("그만! 하고 관 닫기.", "Saying stop and closing the pipe."), ("손님이 그만 읽으면 앵무새도 그만 골라요 — 콩 값을 아껴요.", "When the guest stops reading, the parrot stops picking — saving bean cost.")),
        ("구조화 출력과 스트리밍", "Structured output and streaming", ("양식은 끝까지 모아야.", "Forms must be collected whole."), ('반쪽 양식은 기계가 못 읽어요. → <a href="structuredoutput-ko.html">정해진 칸에 쓰기</a>', 'A half form cannot be read by a machine. → <a href="structuredoutput-en.html">writing in the boxes</a>')),
        ("추론 비용·시간", "Inference cost and time", ("콩 값과 총 시간.", "Bean cost and total time."), ('스트리밍해도 그대로예요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'Unchanged by streaming. → <a href="inference-en.html">what answering costs</a>')),
    ],
}
