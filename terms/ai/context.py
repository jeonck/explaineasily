from _draw import *
from _world import *

CHAT = (("⟦내 이름은 민수야|my name is Minsu⟧", 0.3), ("⟦우산 얘기|about umbrellas⟧", 0.45), ("⟦날씨 얘기|about the weather⟧", 0.6), ("⟦여행 얘기|about the trip⟧", 0.8), ("⟦고양이 얘기|about the cat⟧", 1.0))


def chat(x, y, text, op):
    return (f'<g opacity="{op}"><rect x="{x}" y="{y}" width="180" height="30" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            + label(x + 90, y + 20, text, 11, "var(--ink)") + "</g>")


# 1. 긴 대화 뒤, 앵무새가 처음 말한 걸 잊어요
P1 = svg(300, sky(300)
         + label(130, 34, "⟦긴 대화|a long chat⟧", 11, "var(--muted)")
         + "".join(chat(40, 50 + i * 42, t, op) for i, (t, op) in enumerate(CHAT))
         + person(300, 130, s=0.85, face=FROWN, **GUEST) + bubble(250, 40, 190, 36, "⟦아까 내 이름 말했잖아?|I told you my name!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + perch(560, 200, 140) + parrot(560, 160, 1.1, mood="sweat", talk=True)
         + bubble_parrot(470, 40, 240, 36, "⟦…누구셨죠?|…who were you again?⟧", 12)
         + label(380, 282, "⟦한참 이야기했더니 앵무새가 맨 처음 말을 잊었어요|after a long talk, the parrot forgot the very first thing⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새는 쟁반 위 콩만 봐요 — 쟁반이 차면 앞쪽 콩이 떨어져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 50, "⟦대화가 길어지면 콩이 계속 들어와요|as the chat grows, beans keep coming⟧", 12, "var(--ink)")
         + tray(200, 150, 360, 70, "⟦쟁반이 꽉 찼어요|the tray is full⟧")
         + "".join(bean(225 + i * 32, 138, 1.0) for i in range(10))
         + '<path d="M212 150 L172 182" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4"/>'
         + bean(150, 205, 1.0, text="⟦이름|name⟧") + label(150, 240, "⟦앞쪽 콩이 떨어져요|the front bean falls off⟧", 11, "var(--bad)")
         + bean(600, 138, 1.0, text="⟦고양이|cat⟧") + '<path d="M582 138 L566 138" stroke="var(--accent)" stroke-width="3"/><path d="M572 132 L564 138 L572 144" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + parrot(680, 110, 1.0, mood="think") + label(680, 190, "⟦쟁반 위 콩만 봐요|only the tray counts⟧", 11, "var(--muted)")
         + label(380, 282, "⟦떨어진 콩은 앵무새에게 없는 말이에요|a fallen bean is a word the parrot never heard⟧", 12, "var(--bad)"))

# 3. 컨텍스트 창 = 앵무새 앞의 쟁반 (hero)
P3 = svg(360, sky(360)
         + parrot(330, 90, 1.3, talk=True)
         + label(150, 132, "⟦앞|front⟧", 11, "var(--accent)", cls="d") + label(520, 132, "⟦뒤|back⟧", 11, "var(--accent)", cls="d")
         + tray(120, 170, 420, 80, "⟦한 번에 이만큼|this much at once⟧")
         + "".join(bean(150 + i * 34, 158, 1.0) for i in range(12))
         + note(580, 30, 160, 60, "⟦쟁반 크기|TRAY SIZE⟧", ("⟦콩 20만 개까지|up to 200k beans⟧",), 1.0)
         + person(600, 110, s=0.85, face=SMILE, **TRAINER) + label(630, 240, "⟦쟁반마다 크기가 달라요|trays come in sizes⟧", 11, "var(--muted)")
         + label(380, 340, "⟦컨텍스트 창 = 앵무새 앞의 쟁반, 한 번에 올릴 수 있는 콩 수|the context window is the tray in front of the parrot — how many beans fit at once⟧", 13, "var(--ink)", cls="d"))

# 4. 쟁반 위에 뭐가 올라가나: 주인 쪽지 + 예시 + 대화 + 사서 페이지 + 앵무새 답
GROUPS = (("⟦주인 쪽지|owner note⟧", "#C9A86A", 3), ("⟦예시|samples⟧", "#7B3FA0", 2), ("⟦대화|the chat⟧", PARROT, 7), ("⟦사서 페이지|librarian pages⟧", "#4A5A72", 4), ("⟦앵무새 답|parrot answer⟧", "#2E7D6B", 4))


def groups():
    out, i = "", 0
    for t, c, n in GROUPS:
        xs = [90 + (i + j) * 30 for j in range(n)]
        out += "".join(bean(x, 108, 1.0, color=c) for x in xs) + label((xs[0] + xs[-1]) / 2, 80, t, 11, "var(--ink)", cls="d")
        i += n
    return out


P4 = svg(320, sky(320)
         + label(380, 40, "⟦쟁반 위엔 이런 게 다 올라가요|all of this goes on the tray⟧", 13, "var(--ink)", cls="d")
         + tray(60, 120, 640, 80, "⟦다 콩으로 세서 쟁반 한 장에|all counted as beans, on one tray⟧") + groups()
         + label(380, 262, "⟦답이 길어지면 앞쪽 콩이 밀려나요|a long answer pushes the front beans off⟧", 11, "var(--muted)")
         + label(380, 300, "⟦쪽지도, 예시도, 사서가 가져온 페이지도, 앵무새 답도 — 전부 콩이에요|the note, the samples, the librarian pages, the answer — all beans⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 큰 쟁반이라고 다 잘 보는 건 아니에요 + 큰 쟁반은 비싸요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + parrot(190, 50, 0.8, mood="think")
         + tray(30, 110, 320, 70)
         + "".join((f'<g opacity="0.35">{bean(55 + i * 30, 98, 1.0)}</g>' if 3 <= i <= 6 else bean(55 + i * 30, 98, 1.0)) for i in range(10))
         + label(190, 215, "⟦가운데 콩은 가끔 놓쳐요|beans in the middle sometimes get missed⟧", 11, "var(--bad)")
         + label(190, 262, "⟦큰 쟁반이라고 다 잘 보는 건 아니에요|a big tray does not mean it sees everything⟧", 11, "var(--ink)")
         + tray(400, 60, 320, 90, "⟦큰 쟁반|a big tray⟧")
         + "".join(bean(425 + i * 20, 48, 0.6) for i in range(15))
         + "".join(f'<circle cx="{480 + i * 30}" cy="210" r="12" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>' for i in range(5))
         + label(560, 250, "⟦콩이 많을수록 값도 시간도 늘어요|more beans, more cost and time⟧", 11, "var(--ink)")
         + label(380, 300, "⟦쟁반은 클수록 좋은 게 아니라, 딱 맞게 쓰는 거예요|a tray is not better bigger — it is better used well⟧", 12, "var(--ink)", cls="d"))

SIZE_I = icon(f'<rect x="8" y="34" width="48" height="16" rx="6" fill="var(--stone)"/><path d="M8 24 h48 M8 18 v12 M56 18 v12" stroke="var(--accent)" stroke-width="3"/><ellipse cx="22" cy="30" rx="8" ry="5" fill="{BEAN}"/><ellipse cx="42" cy="30" rx="8" ry="5" fill="{BEAN}"/>')
FRONT_I = icon(f'<rect x="8" y="34" width="48" height="16" rx="6" fill="var(--stone)"/><ellipse cx="18" cy="30" rx="9" ry="6" fill="var(--accent)"/><ellipse cx="36" cy="30" rx="8" ry="5" fill="{BEAN}"/><ellipse cx="52" cy="30" rx="8" ry="5" fill="{BEAN}"/><path d="M18 8 v12" stroke="var(--accent)" stroke-width="3"/><path d="M12 14 L18 20 L24 14" stroke="var(--accent)" stroke-width="3" fill="none"/>')
SUM_I = icon('<rect x="6" y="8" width="22" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M11 16 h12 M11 23 h12 M11 30 h12 M11 37 h12 M11 44 h8" stroke="#142033" stroke-width="2"/><path d="M32 32 h8" stroke="var(--muted)" stroke-width="3"/><rect x="42" y="20" width="18" height="24" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M46 28 h10 M46 35 h6" stroke="#142033" stroke-width="2"/>')
LIB_I = icon(f'<rect x="8" y="40" width="40" height="8" rx="2" fill="#7B3FA0"/><rect x="12" y="30" width="40" height="8" rx="2" fill="#2E7D6B"/><rect x="8" y="20" width="40" height="8" rx="2" fill="#4A5A72"/><rect x="44" y="8" width="14" height="18" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><ellipse cx="54" cy="50" rx="8" ry="5" fill="{BEAN}"/>')

PAGE = {
    "slug": "context", "order": 4,
    "title": ("앵무새 앞의 쟁반", "The Tray in Front of the Parrot"),
    "h1": ("<em>컨텍스트 창</em>이 뭐예요?", "What is a <em>Context Window</em>?"),
    "sub": ("컨텍스트 창을 앵무새 앞에 놓인 쟁반, 한 번에 올릴 수 있는 콩 수 이야기로 풀어봤어요.",
            "The context window, told as a story about the tray in front of the parrot — how many beans fit on it at once."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽에 흐려지는 대화 기록(내 이름은 민수야, 우산, 날씨, 여행, 고양이), 찡그린 손님이 아까 내 이름 말했잖아? 하고 당황한 앵무새가 누구셨죠? 라고 답함", "On the left a fading chat log (my name is Minsu, umbrellas, weather, trip, cat); a frowning guest says I told you my name, and a flustered parrot answers who were you again?"),
         "caption": ("한참 이야기했더니 앵무새가 맨 처음 말을 잊었어요.", "After a long talk, the parrot forgot the very first thing."),
         "small": ("이름을 분명히 말했는데요. 우산 얘기, 날씨 얘기, 고양이 얘기를 하고 나니 앵무새는 처음을 몰라요.", "The name was said clearly. But after umbrellas, weather, and the cat, the parrot no longer knows the beginning.")},
        {"svg": P2, "alt": ("빨간 배경. 콩 열 개로 꽉 찬 쟁반, 오른쪽에서 고양이 콩이 들어오고 왼쪽 앞에서 이름 콩이 떨어짐. 생각하는 앵무새", "Red background. A tray packed with ten beans; a cat bean comes in from the right, and the name bean falls off the front. A thinking parrot"),
         "caption": ("앵무새는 쟁반 위 콩만 봐요. 쟁반이 차면 앞쪽 콩이 떨어져요.", "The parrot only sees the beans on the tray. When it\'s full, the front beans fall off."),
         "small": ('대화가 길어지면 <a href="token-ko.html">콩</a>이 계속 들어와요. 쟁반은 그대로인데요. 떨어진 콩은 앵무새에게 없는 말이에요 — 잊은 게 아니라 못 보는 거예요.',
                   'As the chat grows, <a href="token-en.html">beans</a> keep coming — the tray stays the same size. A fallen bean is a word the parrot never heard; it didn\'t forget, it can\'t see it.')},
        {"svg": P3, "hero": True, "alt": ("앵무새 아래 콩 열두 개가 올라간 긴 쟁반, 앞과 뒤 표시. 조련사와 쟁반 크기 쪽지(콩 20만 개까지), 쟁반마다 크기가 달라요", "A long tray with twelve beans under the parrot, marked front and back. A trainer and a tray-size note (up to 200k beans); trays come in sizes"),
         "caption": ("컨텍스트 창은 앵무새 앞의 쟁반이에요. 한 번에 올릴 수 있는 콩 수예요.", "The context window is the tray in front of the parrot — how many beans fit at once."),
         "small": ('쟁반이 클수록 긴 이야기를 한 번에 올려요. 그래도 한도는 있어요. 그래서 중요한 건 앞쪽에, 긴 건 요약해서, 필요한 페이지만 골라 올려요. 앵무새 자체는 <a href="llm-ko.html">책을 산더미로 읽은 앵무새</a>에서.',
                   'A bigger tray holds a longer story at once — but there is always a limit. So put what matters at the front, summarize the long parts, and pick only the pages you need. The parrot itself: <a href="llm-en.html">the parrot that read a mountain of books</a>.'),
         "tricks": (4, [
             (SIZE_I, ("쟁반 크기를 알아요", "Know the tray size"), ("콩 몇 개까지 올라가나", "how many beans fit"), "calm"),
             (FRONT_I, ("중요한 건 앞쪽에", "Important things up front"), ("규칙과 할 일부터", "rules and the task first"), "calm"),
             (SUM_I, ("긴 건 요약해서", "Summarize the long parts"), ("지난 대화는 짧게 접어요", "fold old chat into a few beans")),
             (LIB_I, ("필요한 페이지만", "Only the pages you need"), ("사서가 골라 올려요", "the librarian picks them"), "warm"),
         ])},
        {"svg": P4, "alt": ("쟁반 한 장 위에 색이 다른 콩 무리: 주인 쪽지, 예시, 대화, 사서 페이지, 앵무새 답. 다 콩으로 세서 쟁반 한 장에", "One tray with bean groups in different colours: owner note, samples, the chat, librarian pages, parrot answer — all counted as beans on one tray"),
         "caption": ("쟁반 위엔 쪽지도, 예시도, 대화도, 사서가 가져온 페이지도, 앵무새 답도 올라가요.", "The note, the samples, the chat, the librarian\'s pages, and the parrot\'s answer all go on the tray."),
         "small": ('전부 <a href="token-ko.html">콩</a>으로 세서 쟁반 한 장에 올려요. <a href="prompt-ko.html">주인 쪽지</a>가 길면 대화 자리가 줄고, 답이 길면 앞쪽 콩이 밀려나요.',
                   'All of it is counted in <a href="token-en.html">beans</a> on one tray. A long <a href="prompt-en.html">owner note</a> leaves less room for the chat; a long answer pushes the front beans off.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 생각하는 앵무새와 콩 열 개 쟁반, 가운데 콩 넷이 흐림. 오른쪽: 콩 열다섯 개가 올라간 큰 쟁반과 동전 다섯 개", "Left, red: a thinking parrot and a ten-bean tray with the four middle beans faded. Right: a big tray with fifteen beans and five coins"),
         "caption": ("쟁반이 크다고 다 잘 보는 건 아니에요. 그리고 큰 쟁반은 비싸요.", "A big tray doesn\'t mean it sees everything. And a big tray is expensive."),
         "small": ('앵무새는 쟁반 가운데 콩을 가끔 놓쳐요 — 앞과 뒤는 잘 보고요. 콩이 많을수록 값도 시간도 늘어요. 콩 값은 <a href="token-ko.html">콩으로 세는 앵무새</a>에서.',
                   'The parrot sometimes misses beans in the middle of the tray — it sees the front and the back best. More beans cost more and take longer. Bean prices: <a href="token-en.html">the parrot that counts in beans</a>.')},
    ],
    "summary": (("<b>컨텍스트 창</b> = 앵무새 앞의 <b>쟁반</b>. <b>한 번에 올릴 수 있는 콩 수</b>예요. 쪽지·예시·대화·사서 페이지·답이 다 콩으로 올라가고, 차면 <b>앞쪽 콩이 떨어져요</b>. 크다고 다 잘 보는 건 아니고, 클수록 비싸요.",
                 "<b>Context window</b> = the <b>tray</b> in front of the parrot: <b>how many beans fit at once</b>. Note, samples, chat, librarian pages, and the answer all go on it as beans; when it\'s full, <b>the front beans fall off</b>. Bigger doesn\'t mean it sees everything, and bigger costs more."),
                ("Context window. LLM 이 한 번의 호출에서 볼 수 있는 최대 토큰 수예요. 시스템 프롬프트, few-shot 예시, 대화 기록, RAG 로 가져온 문서, 생성 중인 답이 모두 여기에 들어가요. 넘치면 앞부분이 잘리거나 요약·압축해야 하고, 긴 컨텍스트에서도 가운데 정보를 놓치는 lost in the middle 현상이 있어요. 반복되는 앞부분은 프롬프트 캐싱으로 값을 줄여요.",
                 "The maximum number of tokens an LLM can see in a single call. The system prompt, few-shot examples, chat history, RAG-retrieved documents, and the answer being generated all count toward it. Overflow means truncating the front or summarizing and compressing; even within a long context, information in the middle can be missed (lost in the middle). Repeated prefixes can be made cheaper with prompt caching.")),
    "glossary": [
        ("컨텍스트 창", "Context window", ("쟁반.", "The tray."), ("앵무새가 한 번에 볼 수 있는 콩 수예요. 쟁반마다 크기가 달라요.", "How many beans the parrot can see at once. Trays come in sizes.")),
        ("컨텍스트 길이", "Context length", ("쟁반 크기.", "The tray size."), ("콩 몇 개까지 올라가나. 수천 개부터 수십만 개까지예요.", "How many beans fit — from thousands to hundreds of thousands.")),
        ("대화 기록", "Chat history", ("지금까지 한 말 콩.", "Beans of everything said so far."), ("매번 쟁반에 다시 올라가요. 길어지면 앞쪽이 떨어져요.", "Goes back on the tray every turn. When it gets long, the front falls off.")),
        ("요약 · 압축", "Summarization · compression", ("긴 콩 줄을 짧게 접기.", "Folding a long bean row short."), ("지난 대화를 몇 콩으로 줄여서 자리를 만들어요.", "Shrinks old chat into a few beans to make room.")),
        ("RAG", "RAG (retrieval-augmented generation)", ("사서가 골라 올린 페이지.", "Pages the librarian picked."), ("책을 다 올리는 대신 필요한 페이지만 찾아 쟁반에 놓아요.", "Instead of the whole book, only the needed pages go on the tray.")),
        ("lost in the middle", "Lost in the middle", ("가운데 콩 놓치기.", "Missing the middle beans."), ("쟁반 앞과 뒤는 잘 보는데 가운데는 가끔 놓쳐요.", "It sees the front and back of the tray well, but sometimes misses the middle.")),
        ("프롬프트 캐싱", "Prompt caching", ("늘 같은 앞쪽 콩은 미리 세 두기.", "Pre-counting the beans that never change."), ("주인 쪽지처럼 매번 똑같은 앞부분은 한 번만 세서 값을 줄여요.", "A prefix that repeats every time, like the owner note, is counted once to save cost.")),
        ("토큰", "Token", ("콩 하나.", "One bean."), ('쟁반에 올라가는 단위. → <a href="token-ko.html">앵무새가 말을 콩으로 세요</a>', 'The unit that goes on the tray. → <a href="token-en.html">the parrot counts words in beans</a>')),
    ],
}
