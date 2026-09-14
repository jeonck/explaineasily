from _draw import *
from _world import *


def notebook(x, y, w, h, lines, s=1.0, hl=-1, bad=False):
    """앵무새의 수첩. 스프링 달린 크림 종이, 글자 #142033."""
    ring = "".join(f'<circle cx="{14 + i * 18}" cy="0" r="4" fill="none" stroke="#5A3B22" stroke-width="2"/>' for i in range(int(w // 18)))
    edge = "var(--bad)" if bad else "#7B3FA0"
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="{PAPER}" stroke="{edge}" stroke-width="3"/>'
           f'{ring}' + label(w / 2, 22, "⟦수첩|NOTEBOOK⟧", 11, "#7B3FA0", cls="d"))
    for i, t in enumerate(lines):
        yy = 46 + i * 20
        if i == hl:
            out += f'<rect x="6" y="{yy - 14}" width="{w - 12}" height="20" rx="4" fill="var(--bad-soft)"/>'
        out += label(12, yy, t, 11, PAPER_INK, "start")
    return out + "</g>"


def arrow(x1, y1, x2, y2, color="var(--good)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"/>'
            f'<path d="M{x2 - 10} {y2 - 7} L{x2 + 2} {y2} L{x2 - 10} {y2 + 7}" stroke="{color}" stroke-width="3" fill="none"/>')


# 1. 어제 '난 커피 싫어' 했는데, 오늘 앵무새가 커피를 추천해요
P1 = svg(300, sky(300) + '<path d="M380 20 V270" stroke="var(--line)" stroke-width="3" stroke-dasharray="8 6"/>'
         + label(190, 40, "⟦어제|yesterday⟧", 14, "var(--muted)", cls="d") + label(570, 40, "⟦오늘|today⟧", 14, "var(--muted)", cls="d")
         + person(40, 120, s=0.9, face=EYES, **GUEST) + bubble(20, 60, 170, 36, "⟦난 커피 싫어|I hate coffee⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + parrot(280, 160, 1.0) + bubble_parrot(200, 60, 150, 36, "⟦알겠어요!|got it!⟧", 12)
         + person(420, 120, s=0.9, face=FROWN, **GUEST)
         + parrot(660, 160, 1.0, talk=True) + bubble_parrot(520, 60, 220, 36, "⟦커피 한 잔 어때요?|how about a coffee?⟧", 12)
         + label(380, 282, "⟦어제 말한 걸 오늘은 몰라요|what you said yesterday, it doesn\'t know today⟧", 13, "var(--ink)"))

# 2. 왜: 쟁반은 대화가 끝나면 비워져요 — 앵무새는 원래 기억이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + tray(40, 120, 240, 70, "⟦어제의 쟁반|yesterday\'s tray⟧") + beans(90, 155, ("⟦난|I⟧", "⟦커피|hate⟧", "⟦싫어|coffee⟧"), 1.0, 60)
         + label(160, 90, "⟦대화 끝|chat ends⟧", 12, "var(--ink)", cls="d")
         + arrow(300, 155, 380, 155, "var(--bad)")
         + tray(400, 120, 240, 70, "⟦오늘의 쟁반|today\'s tray⟧") + label(520, 160, "⟦(비었어요)|(empty)⟧", 12, "var(--muted)")
         + label(520, 90, "⟦새 대화|new chat⟧", 12, "var(--ink)", cls="d")
         + parrot(700, 150, 1.0, mood="think") + label(700, 240, "⟦기억이 없어요|no memory at all⟧", 11, "var(--muted)")
         + label(380, 288, "⟦쟁반은 대화가 끝나면 비워져요 — 앵무새는 원래 아무것도 기억하지 않아요|the tray is emptied when the chat ends — the parrot remembers nothing on its own⟧", 12, "var(--bad)"))

# 3. 메모리 = 대화 밖에 따로 적어두는 앵무새의 수첩 (hero)
P3 = svg(360, sky(360)
         + person(30, 130, s=0.9, face=SMILE, **GUEST) + label(62, 250, "⟦손님|guest⟧", 11, "var(--muted)")
         + bubble(0, 50, 180, 36, "⟦오늘은 뭐 마실까?|what should I drink?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + notebook(180, 40, 170, 120, ("⟦커피 싫어함|dislikes coffee⟧", "⟦이름: 민수|name: Minsu⟧", "⟦존댓말 원함|prefers polite tone⟧"))
         + label(265, 180, "⟦대화 밖에 따로 적어 둬요|kept outside the chat⟧", 11, "var(--muted)")
         + arrow(360, 100, 400, 100)
         + tray(410, 150, 220, 70, "⟦오늘의 쟁반|today\'s tray⟧")
         + notebook(425, 112, 170, 120, ("⟦커피 싫어함|dislikes coffee⟧",), 0.45)
         + bean(560, 185, 1.0, text="⟦질문|Q⟧")
         + label(520, 72, "⟦대화 시작에 먼저 올려요|goes on the tray first⟧", 12, "var(--ink)", cls="d")
         + arrow(632, 185, 660, 185)
         + parrot(705, 165, 1.1, talk=True)
         + bubble_parrot(560, 8, 190, 40, "⟦커피 말고 차 어때요?|tea instead of coffee?⟧", 12)
         + label(380, 340, "⟦메모리 = 대화 밖에 따로 적어 두는 앵무새의 수첩 — 다음에 만나면 쟁반에 먼저 올려요|memory is the parrot\'s notebook kept outside the chat — next time, it goes on the tray first⟧", 13, "var(--ink)", cls="d"))

# 4. 두 종류: 이번 대화 쟁반(단기) vs 수첩(장기)
ROWS = (("⟦얼마나 오래|how long⟧", "⟦이번 대화만|this chat only⟧", "⟦다음에 만나도|next time too⟧"),
        ("⟦무엇을|what⟧", "⟦주고받은 말 전부|everything said⟧", "⟦중요한 것만 골라서|only what matters⟧"),
        ("⟦얼마나 크게|how big⟧", "⟦쟁반 크기만큼|as big as the tray⟧", "⟦길어지면 서가처럼 딱지로|when long, tagged like a shelf⟧"),
        ("⟦지우면|erasing⟧", "⟦대화 끝나면 저절로|automatic when the chat ends⟧", "⟦손님이 말하면 지워요|when the guest asks⟧"))
P4 = svg(320, sky(320)
         + '<rect x="30" y="30" width="540" height="240" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="540" height="30" rx="8" fill="#C9A86A"/>' + label(300, 50, "⟦쟁반 vs 수첩|TRAY vs NOTEBOOK⟧", 13, "#142033", cls="d")
         + label(250, 84, "⟦쟁반 (단기)|tray (short-term)⟧", 12, "#142033", cls="d") + label(450, 84, "⟦수첩 (장기)|notebook (long-term)⟧", 12, "#142033", cls="d")
         + '<path d="M40 94 H560" stroke="#C9A86A" stroke-width="2"/>'
         + "".join(label(50, 120 + i * 40, a, 12, "#142033", "start", cls="d") + label(250, 120 + i * 40, b, 11, "#142033") + label(450, 120 + i * 40, c, 11, "#142033")
                   for i, (a, b, c) in enumerate(ROWS))
         + tray(600, 60, 130, 44) + label(665, 128, "⟦쟁반|tray⟧", 11, "var(--muted)")
         + notebook(610, 160, 110, 80, ("⟦커피 싫어함|dislikes coffee⟧",), 1.0) + label(665, 262, "⟦수첩|notebook⟧", 11, "var(--muted)")
         + label(380, 300, "⟦둘 다 써요: 쟁반엔 지금 대화, 수첩엔 다음에도 필요한 것|use both: the tray for now, the notebook for what you need next time too⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 수첩에 잘못 적으면 계속 틀려요 + 수첩은 개인 정보라 조심
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + notebook(30, 40, 170, 110, ("⟦커피 좋아함|likes coffee⟧", "⟦이름: 민수|name: Minsu⟧"), 1.0, 0, bad=True)
         + label(115, 172, "⟦잘못 적혔어요|written wrong⟧", 11, "var(--bad)", cls="d")
         + parrot(290, 110, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(220, 20, 150, 36, "⟦커피 또 어때요?|coffee again?⟧", 11, bad=True)
         + label(190, 230, "⟦한 번 잘못 적으면 매번 틀려요|one wrong line, and it is wrong every time⟧", 12, "var(--bad)")
         + label(190, 250, "⟦손님이 고치거나 지울 수 있어야 해요|the guest must be able to fix or erase it⟧", 11, "var(--muted)")
         + notebook(410, 40, 170, 110, ("⟦이름, 주소, 건강…|name, address, health…⟧", "⟦개인 정보예요|personal data⟧"), 1.0)
         + '<rect x="600" y="70" width="44" height="36" rx="6" fill="var(--good)"/><path d="M610 70 V56 a12 12 0 0 1 24 0 V70" stroke="var(--good)" stroke-width="6" fill="none"/><circle cx="622" cy="88" r="5" fill="#FFF8E7"/>'
         + label(680, 90, "⟦잠가요|locked⟧", 12, "var(--good)", cls="d")
         + person(650, 120, s=0.9, face=SMILE, **GUEST)
         + label(570, 250, "⟦수첩은 개인 정보라 잠그고, 지워달라면 지워요|the notebook is personal data: lock it, erase on request⟧", 12, "var(--ink)")
         + label(380, 300, "⟦수첩은 편하지만, 맞게 적고 잘 지키는 게 더 중요해요|a notebook is handy — but writing it right and keeping it safe matter more⟧", 12, "var(--ink)", cls="d"))

PICK_I = icon('<rect x="12" y="10" width="40" height="46" rx="4" fill="#FFF8E7" stroke="#7B3FA0" stroke-width="3"/><path d="M20 24 h24" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M20 34 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round" opacity="0.3"/><path d="M20 44 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round" opacity="0.3"/><path d="M40 40 l4 4 l8 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
FIRST_I = icon('<rect x="6" y="38" width="52" height="16" rx="5" fill="var(--stone)"/><rect x="12" y="14" width="20" height="24" rx="2" fill="#FFF8E7" stroke="#7B3FA0" stroke-width="2"/><ellipse cx="44" cy="34" rx="8" ry="5" fill="#C9822B"/><text x="22" y="12" text-anchor="middle" font-size="11" font-weight="700" fill="var(--accent)">1</text>')
ERASE_I = icon('<rect x="10" y="12" width="36" height="42" rx="4" fill="#FFF8E7" stroke="#7B3FA0" stroke-width="3"/><path d="M18 26 h20 M18 36 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><rect x="34" y="34" width="22" height="14" rx="3" transform="rotate(-40 45 41)" fill="var(--bad)"/>')
SHORT_I = icon('<rect x="8" y="10" width="26" height="44" rx="3" fill="#FFF8E7" stroke="#7B3FA0" stroke-width="2"/><path d="M14 22 h14 M14 30 h14" stroke="#142033" stroke-width="2" stroke-linecap="round"/><ellipse cx="48" cy="26" rx="9" ry="6" fill="#C9822B"/><ellipse cx="48" cy="42" rx="9" ry="6" fill="#C9822B"/><text x="48" y="60" text-anchor="middle" font-size="11" font-weight="700" fill="var(--muted)">2</text>')

PAGE = {
    "slug": "memory", "order": 10,
    "title": ("앵무새의 수첩", "The Parrot\'s Notebook"),
    "h1": ("<em>메모리</em>가 뭐예요?", "What is <em>Memory</em>?"),
    "sub": ("LLM 메모리를 대화 밖에 따로 적어 두었다가 다음 대화 시작에 쟁반에 먼저 올리는 앵무새의 수첩 이야기로 풀어봤어요.",
            "LLM memory, told as a story about the parrot\'s notebook — kept outside the chat and placed on the tray first next time."),
    "panels": [
        {"svg": P1, "alt": ("점선으로 나뉜 어제와 오늘. 어제: 손님이 '난 커피 싫어', 앵무새 '알겠어요!'. 오늘: 앵무새가 '커피 한 잔 어때요?', 손님이 찡그림", "Yesterday and today split by a dashed line. Yesterday: the guest says I hate coffee, the parrot says got it! Today: the parrot says how about a coffee? and the guest frowns"),
         "caption": ("어제 '난 커피 싫어'라고 했는데, 오늘 앵무새가 커피를 추천해요.", "Yesterday the guest said I hate coffee. Today the parrot recommends coffee."),
         "small": ("어제 분명히 말했는데요. 앵무새는 왜 모를까요?", "It was said clearly yesterday. Why doesn\'t the parrot know?")},
        {"svg": P2, "alt": ("빨간 배경. 어제의 쟁반에 '난 커피 싫어' 콩 세 개, 화살표 뒤 오늘의 쟁반은 비어 있음. 눈 감은 앵무새 '기억이 없어요'", "Red background. Yesterday\'s tray holds three beans I hate coffee; after an arrow, today\'s tray is empty. A parrot with closed eyes: no memory at all"),
         "caption": ("쟁반은 대화가 끝나면 비워져요. 앵무새는 원래 기억이 없어요.", "The tray is emptied when the chat ends. The parrot has no memory of its own."),
         "small": ('앵무새가 보는 건 <a href="context-ko.html">쟁반</a> 위뿐이에요. 새 대화의 쟁반은 텅 비어 있으니, 어제 일은 없는 것과 같아요.', 'The parrot only sees what is on the <a href="context-en.html">tray</a>. A new chat starts with an empty tray, so yesterday might as well not have happened.')},
        {"svg": P3, "hero": True, "alt": ("손님이 '오늘은 뭐 마실까?' 묻자, 대화 밖 수첩(커피 싫어함, 이름: 민수, 존댓말 원함)이 오늘의 쟁반에 먼저 올라가고, 앵무새가 '커피 말고 차 어때요?'", "The guest asks what should I drink?; a notebook kept outside the chat (dislikes coffee, name: Minsu, prefers polite tone) goes on today\'s tray first, and the parrot says tea instead of coffee?"),
         "caption": ("메모리는 대화 밖에 따로 적어 두는 앵무새의 수첩이에요. 다음에 만나면 쟁반에 먼저 올려요.", "Memory is the parrot\'s notebook, kept outside the chat. Next time, it goes on the tray first."),
         "small": ('앵무새가 기억하는 게 아니에요. 수첩을 <a href="context-ko.html">쟁반</a>에 올려 주니까 기억하는 것처럼 보이는 거예요. 수첩이 길어지면 <a href="vectordb-ko.html">서가</a>처럼 딱지로 찾기도 해요.',
                   'The parrot isn\'t remembering. The notebook is placed on the <a href="context-en.html">tray</a>, so it looks like it remembers. When the notebook grows long, it is searched by tag like a <a href="vectordb-en.html">shelf</a>.'),
         "tricks": (4, [
             (PICK_I, ("중요한 것만 수첩에", "Only what matters goes in"), ("대화 전부가 아니라", "not the whole conversation"), "calm"),
             (FIRST_I, ("대화 시작에 수첩을 쟁반에", "Notebook on the tray first"), ("질문보다 먼저", "before the question")),
             (ERASE_I, ("지워달라면 지워요", "Erase on request"), ("손님의 것이니까", "it belongs to the guest"), "warm"),
             (SHORT_I, ("수첩도 콩이니 짧게", "The notebook costs beans too"), ("길면 쟁반이 좁아져요", "a long one crowds the tray")),
         ])},
        {"svg": P4, "alt": ("표: 쟁반(단기) vs 수첩(장기). 얼마나 오래: 이번 대화만 / 다음에 만나도. 무엇을: 주고받은 말 전부 / 중요한 것만. 얼마나 크게: 쟁반 크기만큼 / 길어지면 서가처럼 딱지로. 지우면: 대화 끝나면 저절로 / 손님이 말하면", "A table: tray (short-term) vs notebook (long-term). How long: this chat only / next time too. What: everything said / only what matters. How big: as big as the tray / when long, tagged like a shelf. Erasing: automatic when the chat ends / when the guest asks"),
         "caption": ("두 종류예요. 이번 대화의 쟁반은 단기, 수첩은 장기.", "There are two kinds. This chat\'s tray is short-term; the notebook is long-term."),
         "small": ('쟁반엔 지금 주고받는 말 전부, 수첩엔 다음에도 필요한 것만. 수첩이 아주 길어지면 <a href="vectordb-ko.html">딱지로 정리한 서가</a>처럼 관련 있는 줄만 꺼내 올려요.',
                   'The tray holds everything said right now; the notebook only what is needed next time. When the notebook gets very long, only the relevant lines are pulled out, like from <a href="vectordb-en.html">the shelf organized by tags</a>.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 수첩에 '커피 좋아함'이 잘못 적혀 있고 빨간 앵무새가 '커피 또 어때요?'. 오른쪽 초록: 이름·주소·건강 등 개인 정보가 적힌 수첩에 자물쇠, 손님이 웃음", "Left, red: the notebook wrongly says likes coffee and the red parrot asks coffee again? Right, green: a notebook holding name, address, health has a lock; the guest smiles"),
         "caption": ("수첩에 잘못 적으면 계속 틀려요. 그리고 수첩은 개인 정보라 조심해야 해요.", "A wrong line in the notebook stays wrong every time. And the notebook is personal data, so handle it with care."),
         "small": ('손님이 수첩을 보고 고치고 지울 수 있어야 해요. 개인 정보 지키기는 <a href="privacy-ko.html">보안 분야의 개인정보</a> 이야기에서. 회사 규정 같은 지식은 수첩이 아니라 <a href="rag-ko.html">사서가 찾아온 페이지</a>로요.',
                   'The guest must be able to see, fix and erase the notebook. Keeping personal data safe is the security world\'s <a href="privacy-en.html">privacy</a> story. Knowledge like company rules belongs not in the notebook but in <a href="rag-en.html">the page the librarian brought</a>.')},
    ],
    "summary": (("<b>메모리</b> = 대화 밖에 따로 적어 두는 <b>앵무새의 수첩</b>. 앵무새는 원래 기억이 없고 <b>쟁반</b>은 대화가 끝나면 비워지니, 중요한 것만 수첩에 적어 <b>다음 대화 시작에 쟁반에 먼저</b> 올려요. 잘못 적으면 계속 틀리고, 개인 정보라 조심해요.",
                 "<b>Memory</b> = the <b>parrot\'s notebook</b> kept outside the chat. The parrot has no memory and the <b>tray</b> is emptied when the chat ends, so what matters is written down and <b>placed on the tray first next time</b>. A wrong line stays wrong, and it is personal data."),
                ("LLM 은 상태가 없어서(stateless) 세션이 끝나면 컨텍스트 창이 사라져요. 메모리는 대화 기록·사용자 프로필·요약을 모델 밖 저장소에 두었다가 다음 세션의 프롬프트에 주입하는 구조예요. 단기 메모리는 현재 컨텍스트, 장기 메모리는 외부 저장(요약·키-값·벡터 메모리)이고, 개인정보라 열람·정정·삭제 권한이 필요해요.",
                 "An LLM is stateless: the context window vanishes when the session ends. Memory keeps conversation history, a user profile or summaries in a store outside the model and injects them into the next session\'s prompt. Short-term memory is the current context; long-term memory is external storage (summary, key-value or vector memory) — and because it is personal data, users need to view, correct and delete it.")),
    "glossary": [
        ("메모리 (장기 / 단기)", "Memory (long / short-term)", ("수첩 / 쟁반.", "Notebook / tray."), ("단기는 지금 대화의 쟁반, 장기는 대화 밖 수첩이에요.", "Short-term is this chat\'s tray; long-term is the notebook outside the chat.")),
        ("대화 기록", "Conversation history", ("주고받은 말 전부.", "Everything said so far."), ("쟁반에 그대로 올라가요. 길어지면 앞부분이 떨어져요.", "Goes on the tray as is. When it grows, the earliest part falls off.")),
        ("사용자 프로필", "User profile", ("수첩의 손님 칸.", "The guest section of the notebook."), ("이름, 좋아하는 것, 말투 취향 같은 것.", "Name, likes, preferred tone and such.")),
        ("요약 메모리", "Summary memory", ("긴 대화를 몇 줄로.", "A long chat in a few lines."), ("쟁반이 좁으니 지난 대화를 요약해서 수첩에 적어요.", "The tray is small, so past chats are summarized into the notebook.")),
        ("벡터 메모리", "Vector memory", ("딱지로 찾는 수첩.", "A notebook searched by tag."), ('수첩이 길어지면 서가처럼 관련 줄만 꺼내요. → <a href="vectordb-ko.html">딱지로 정리한 서가</a>', 'When the notebook is long, only relevant lines are pulled, shelf-style. → <a href="vectordb-en.html">the shelf organized by tags</a>')),
        ("세션", "Session", ("대화 한 판.", "One sitting of conversation."), ("시작하면 쟁반이 새로 나오고, 끝나면 비워져요.", "A fresh tray comes out when it starts and is emptied when it ends.")),
        ("개인정보", "Personal data", ("수첩에 적힌 손님 이야기.", "The guest\'s story in the notebook."), ('열람·정정·삭제를 손님이 할 수 있어야 해요. → <a href="privacy-ko.html">개인정보 (보안)</a>', 'The guest must be able to view, correct and delete it. → <a href="privacy-en.html">privacy (security)</a>')),
        ("컨텍스트 창", "Context window", ("쟁반.", "The tray."), ('수첩이 올라가는 곳. 크기가 정해져 있어요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'Where the notebook goes. It has a fixed size. → <a href="context-en.html">the tray in front of the parrot</a>')),
    ],
}
