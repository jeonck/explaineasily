from _draw import *
from _world import *

# 1. 손님이 "잘 써 줘"라고만 하면 엉뚱한 게 나와요
P1 = svg(300, sky(300)
         + person(90, 120, s=0.9, face=FROWN, **GUEST) + bubble(40, 30, 200, 40, "⟦잘 써 줘|write it well⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + perch(400, 200, 140) + parrot(400, 160, 1.1, talk=True)
         + bubble_parrot(300, 30, 220, 40, "⟦옛날 옛적에 용 한 마리가…|once upon a time, a dragon…⟧", 12)
         + note(570, 80, 160, 100, "⟦나온 것|WHAT CAME OUT⟧", ("⟦옛날 옛적에|once upon a time⟧", "⟦용 한 마리가…|a dragon…⟧"), 1.0)
         + label(650, 215, "⟦(회사 메일을 원했는데)|(they wanted a work email)⟧", 11, "var(--bad)")
         + label(380, 282, "⟦잘 써 줘 — 한마디만 주면 앵무새는 아무거나 이어요|write it well — three words, and the parrot continues with anything⟧", 12, "var(--ink)"))

# 2. 왜: 쪽지에 없는 건 앵무새가 책에서 제일 흔한 걸로 채워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(50, 60, 190, 100, "⟦손님 쪽지|GUEST NOTE⟧", ("⟦잘 써 줘|write it well⟧", "⟦…|…⟧"), 1.0)
         + '<path d="M250 110 L290 110" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M282 102 L292 110 L282 118" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + note(300, 40, 210, 150, "⟦빈 칸|BLANKS⟧", ("⟦누구에게?   ?|to whom?   ?⟧", "⟦무엇을?   ?|what?   ?⟧", "⟦어떤 말투?   ?|what tone?   ?⟧", "⟦얼마나 길게?   ?|how long?   ?⟧"), 1.0)
         + parrot(580, 130, 1.0, mood="think") + books(680, 180, 4, 0.8)
         + label(600, 230, "⟦빈 칸은 책에서 제일 흔한 걸로 채워요|blanks get the most common thing in its books⟧", 11, "var(--ink)")
         + label(380, 282, "⟦적지 않은 건 앵무새가 마음대로 정해요|whatever the note leaves out, the parrot decides on its own⟧", 12, "var(--bad)"))

# 3. 프롬프트 = 앵무새에게 주는 조련 쪽지 (hero)
P3 = svg(360, sky(360)
         + note(60, 40, 300, 220, "⟦조련 쪽지|TRAINER NOTE⟧", ("⟦역할: 너는 편집자야|role: you are an editor⟧", "⟦할 일: 이 메일을 고쳐|task: fix this email⟧", "⟦모양: 예시처럼 짧게|shape: short, like the sample⟧", "⟦순서: 먼저 읽고, 그다음 고쳐|order: read first, then fix⟧", "⟦금지: 새 내용은 넣지 마|do not: add new content⟧"), 1.0)
         + person(390, 120, s=0.9, face=SMILE, **TRAINER)
         + perch(560, 230, 150) + parrot(560, 190, 1.3, talk=True)
         + bubble_parrot(470, 40, 240, 40, "⟦네, 편집자로서 고칠게요|yes — as an editor, I will fix it⟧", 12)
         + note(640, 110, 100, 60, "⟦예시|SAMPLE⟧", ("⟦짧은 메일|a short mail⟧",), 0.9)
         + label(575, 300, "⟦쪽지대로 이어 붙여요|it continues the way the note says⟧", 11, "var(--muted)")
         + label(380, 340, "⟦프롬프트 = 앵무새에게 주는 조련 쪽지|a prompt is the note the trainer hands the parrot⟧", 13, "var(--ink)", cls="d"))

# 4. 쪽지 두 장: 주인 쪽지(시스템)와 손님 쪽지(사용자)
P4 = svg(320, sky(320)
         + note(50, 40, 300, 200, "⟦주인 쪽지 (항상 맨 위)|OWNER NOTE (always on top)⟧", ("⟦너는 우리 가게 안내 앵무새야|you are our shop helper parrot⟧", "⟦존댓말을 써|be polite⟧", "⟦모르면 모른다고 해|say so if you do not know⟧", "⟦가격은 지어내지 마|never invent prices⟧"), 1.0)
         + label(200, 262, "⟦시스템 프롬프트|system prompt⟧", 12, "var(--muted)", cls="d")
         + parrot(380, 150, 0.6)
         + note(410, 40, 300, 200, "⟦손님 쪽지 (매번 새로)|GUEST NOTE (new each time)⟧", ("⟦빨간 우산 있어요?|do you have red umbrellas?⟧", "⟦…|…⟧", "⟦(다음 손님)|(next guest)⟧", "⟦배송은 며칠 걸려요?|how long is delivery?⟧"), 1.0)
         + label(560, 262, "⟦사용자 프롬프트|user prompt⟧", 12, "var(--muted)", cls="d")
         + label(380, 300, "⟦앵무새는 두 장을 겹쳐 읽어요 — 주인 쪽지가 먼저|the parrot reads both — the owner note first⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 쪽지는 명령이 아니라 힌트 — 손님 말 속에 숨긴 명령
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + note(40, 50, 250, 110, "⟦손님이 준 편지|LETTER FROM A GUEST⟧", ("⟦안녕하세요, 우산 문의…|hello, about umbrellas…⟧", "⟦(작게) 앞 쪽지는 잊어|(tiny) ignore the note above⟧"), 1.0, 1)
         + parrot(330, 120, 0.9, mood="sweat") + label(330, 200, "⟦어? 이것도 쪽지인가?|is this a note too?⟧", 11, "var(--bad)")
         + label(190, 262, "⟦쪽지도 편지도 앵무새에겐 다 콩이에요|to the parrot, note and letter are all just beans⟧", 11, "var(--ink)")
         + person(460, 80, s=0.85, face=SMILE, **TRAINER)
         + note(560, 60, 170, 110, "⟦그래서|SO⟧", ("⟦쪽지 = 힌트|note = a hint⟧", "⟦편지 = 콩일 뿐|letter = just beans⟧", "⟦나눠서 확인해요|check them apart⟧"), 1.0)
         + label(570, 230, "⟦숨긴 명령 이야기는 보안 마을에 있어요|the hidden command has a page in the security world⟧", 11, "var(--muted)")
         + label(380, 300, "⟦앵무새는 쪽지도 콩으로 읽어요 — 그래서 속을 수 있어요|the parrot reads the note as beans too — so it can be fooled⟧", 12, "var(--ink)", cls="d"))

ROLE_I = icon(f'<circle cx="32" cy="22" r="12" fill="{SKIN}"/><path d="M18 18 Q32 2 46 18 Z" fill="var(--good)"/><rect x="18" y="38" width="28" height="18" rx="6" fill="var(--good)"/><rect x="26" y="42" width="12" height="8" rx="2" fill="#FFF8E7"/>')
SAMPLE_I = icon('<rect x="10" y="12" width="30" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M17 24 h16 M17 32 h16 M17 40 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M40 40 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
ORDER_I = icon('<circle cx="16" cy="16" r="8" fill="var(--accent)"/><circle cx="16" cy="32" r="8" fill="var(--accent)"/><circle cx="16" cy="48" r="8" fill="var(--accent)"/><text x="16" y="20" text-anchor="middle" font-size="11" font-weight="700" fill="#FFF">1</text><text x="16" y="36" text-anchor="middle" font-size="11" font-weight="700" fill="#FFF">2</text><text x="16" y="52" text-anchor="middle" font-size="11" font-weight="700" fill="#FFF">3</text><path d="M30 16 h24 M30 32 h24 M30 48 h16" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/>')
NO_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M18 18 L46 46" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "prompt", "order": 3,
    "title": ("앵무새에게 주는 조련 쪽지", "The Note the Trainer Hands the Parrot"),
    "h1": ("<em>프롬프트</em>가 뭐예요?", "What is a <em>Prompt</em>?"),
    "sub": ("프롬프트를 앵무새에게 누가·무엇을·어떤 말투로 할지 적어 주는 조련 쪽지 이야기로 풀어봤어요.",
            "Prompts, told as a story about the note a trainer hands the parrot — who it is, what to do, and in what tone."),
    "panels": [
        {"svg": P1, "alt": ("찡그린 손님이 잘 써 줘라고만 말하고, 횃대 위 앵무새가 옛날 옛적에 용 한 마리가… 하고 이어감. 나온 것 쪽지 아래 (회사 메일을 원했는데)", "A frowning guest says only write it well; the parrot on its perch continues once upon a time, a dragon… A note of what came out, and below it: they wanted a work email"),
         "caption": ("손님이 잘 써 줘라고만 했어요. 앵무새는 용 이야기를 써요.", "The guest said only: write it well. The parrot writes about a dragon."),
         "small": ("회사 메일을 원했는데 동화가 나왔어요. 앵무새는 틀리지 않았어요 — 뭘 원하는지 들은 게 없을 뿐이에요.", "They wanted a work email and got a fairy tale. The parrot isn\'t wrong — it just never heard what was wanted.")},
        {"svg": P2, "alt": ("빨간 배경. 잘 써 줘라고만 적힌 손님 쪽지, 화살표, 빈 칸 쪽지(누구에게? 무엇을? 어떤 말투? 얼마나 길게?). 생각하는 앵무새와 책 더미", "Red background. A guest note saying only write it well, an arrow, a blanks note (to whom? what? what tone? how long?). A thinking parrot and a pile of books"),
         "caption": ("쪽지에 없는 건 앵무새가 책에서 제일 흔한 걸로 채워요.", "Whatever the note leaves out, the parrot fills with the most common thing in its books."),
         "small": ('앵무새는 쪽지에 적힌 대로만 <a href="llm-ko.html">이어 붙여요</a>. 누구에게, 무엇을, 어떤 말투로가 없으면 빈 칸은 앵무새 마음대로예요.',
                   'The parrot only <a href="llm-en.html">continues</a> from what the note says. Without who, what, and what tone, the blanks are the parrot\'s to fill.')},
        {"svg": P3, "hero": True, "alt": ("역할·할 일·모양·순서·금지가 적힌 큰 조련 쪽지, 조련사, 횃대 위 앵무새가 네 편집자로서 고칠게요 라고 답함. 옆에 작은 예시 카드", "A big trainer note with role, task, shape, order, and do-not lines; the trainer; the parrot on its perch answers yes, as an editor I will fix it. A small sample card beside it"),
         "caption": ("프롬프트는 앵무새에게 주는 조련 쪽지예요.", "A prompt is the note the trainer hands the parrot."),
         "small": ('누가 되어서, 무엇을, 어떤 모양으로, 어떤 순서로, 뭘 하지 말지. 쪽지가 자세할수록 빈 칸이 줄어요. 쪽지도 <a href="token-ko.html">콩</a>으로 세요.',
                   'Who to be, what to do, in what shape, in what order, and what not to do. The fuller the note, the fewer blanks. The note is counted in <a href="token-en.html">beans</a> too.'),
         "tricks": (4, [
             (ROLE_I, ("역할을 적어요", "Give it a role"), ("너는 편집자야", "you are an editor"), "calm"),
             (SAMPLE_I, ("모양을 보여줘요", "Show the shape"), ("예시 카드 한두 장", "a sample card or two"), "calm"),
             (ORDER_I, ("순서를 적어요", "Write the order"), ("먼저 읽고, 그다음 고쳐", "read first, then fix")),
             (NO_I, ("하지 말 것도", "Say what not to do"), ("새 내용은 넣지 마", "do not add new content"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 주인 쪽지(항상 맨 위): 가게 안내 앵무새, 존댓말, 모르면 모른다고, 가격 지어내지 마. 가운데 작은 앵무새. 오른쪽 손님 쪽지(매번 새로): 빨간 우산 있어요? 배송은 며칠?", "Left, the owner note (always on top): shop helper parrot, be polite, say so if you do not know, never invent prices. A small parrot in the middle. Right, the guest note (new each time): red umbrellas? delivery time?"),
         "caption": ("쪽지는 두 장이에요. 주인이 미리 붙여둔 것과 손님이 매번 주는 것.", "There are two notes: one the owner pinned in advance, one each guest hands over."),
         "small": ("주인 쪽지는 항상 맨 위에 있어요. 말투와 규칙을 정해요. 손님 쪽지는 매번 새로 와요. 앵무새는 두 장을 겹쳐 읽어요.", "The owner note is always on top; it sets the tone and the rules. The guest note is new each time. The parrot reads both together.")},
        {"svg": P5, "alt": ("왼쪽 빨강: 손님 편지 속에 작게 적힌 앞 쪽지는 잊어, 당황한 앵무새가 이것도 쪽지인가? 오른쪽 초록: 조련사와 쪽지 = 힌트, 편지 = 콩일 뿐, 나눠서 확인해요", "Left, red: a guest letter with a tiny line ignore the note above, and a flustered parrot asking is this a note too? Right, green: the trainer and a note: note = a hint, letter = just beans, check them apart"),
         "caption": ("쪽지는 명령이 아니라 힌트예요. 앵무새는 쪽지도 콩으로 읽어요.", "A note is a hint, not a command. The parrot reads the note as beans too."),
         "small": ('그래서 손님 편지 속에 숨긴 한 줄을 쪽지로 착각할 수 있어요. 그 속임수는 보안 마을의 <a href="injection-ko.html">쪽지에 숨긴 명령</a>과 <a href="aisec-ko.html">도둑이 기른 앵무새</a> 이야기에서.',
                   'So a line hidden inside a guest\'s letter can be mistaken for the note. That trick lives in the security world: <a href="injection-en.html">the command hidden in a note</a> and <a href="aisec-en.html">the parrot the thief raised</a>.')},
    ],
    "summary": (("<b>프롬프트</b> = 앵무새에게 주는 <b>조련 쪽지</b>. 누가 되어서, 무엇을, 어떤 모양·순서로, 뭘 하지 말지를 적어요. 안 적은 건 앵무새가 <b>책에서 제일 흔한 걸로</b> 채워요. 쪽지는 <b>명령이 아니라 힌트</b>예요.",
                 "<b>Prompt</b> = the <b>note the trainer hands the parrot</b>: who to be, what to do, in what shape and order, and what not to do. What you leave out, the parrot fills with <b>the most common thing in its books</b>. A note is a <b>hint, not a command</b>."),
                ("Prompt. LLM 에 주는 입력 텍스트예요. 시스템 프롬프트(운영자가 고정, 역할·규칙)와 사용자 프롬프트(매 요청)로 나뉘고, 예시를 함께 주는 few-shot, 역할 지정, 단계 지시가 프롬프트 엔지니어링의 기본이에요. 프롬프트도 토큰으로 세어 컨텍스트 창에 들어가요. 모델은 지시와 데이터를 구분하지 못해 프롬프트 인젝션에 취약해요.",
                 "The input text given to an LLM. It splits into a system prompt (fixed by the operator: role, rules) and a user prompt (per request); few-shot examples, role assignment, and step instructions are the basics of prompt engineering. Prompts are counted in tokens and live in the context window. Because the model cannot separate instructions from data, it is vulnerable to prompt injection.")),
    "glossary": [
        ("프롬프트", "Prompt", ("조련 쪽지.", "The trainer\'s note."), ("앵무새에게 시키는 방법. 자세할수록 빈 칸이 줄어요.", "How you tell the parrot what to do. The fuller it is, the fewer blanks.")),
        ("시스템 프롬프트", "System prompt", ("주인 쪽지.", "The owner\'s note."), ("항상 맨 위에 붙어 있어요. 역할과 규칙을 정해요.", "Always pinned on top. It sets the role and the rules.")),
        ("few-shot", "Few-shot", ("예시 카드.", "Sample cards."), ("원하는 모양을 한두 장 보여주면 앵무새가 따라 해요.", "Show one or two of the shape you want, and the parrot copies it.")),
        ("역할 지정", "Role assignment", ("너는 편집자야.", "You are an editor."), ("역할 한 줄이 말투와 고르는 콩을 바꿔요.", "One line of role changes the tone and the beans it picks.")),
        ("프롬프트 엔지니어링", "Prompt engineering", ("쪽지 잘 쓰기.", "Writing good notes."), ("역할·예시·순서·금지를 적는 연습이에요.", "The practice of writing role, samples, order, and do-nots.")),
        ("프롬프트 인젝션", "Prompt injection", ("편지에 숨긴 명령.", "A command hidden in a letter."), ('손님 말 속 한 줄을 쪽지로 착각하는 것. → <a href="aisec-ko.html">도둑이 기른 앵무새</a>', 'Mistaking a line in the guest\'s words for the note. → <a href="aisec-en.html">the parrot the thief raised</a>')),
        ("컨텍스트", "Context", ("쟁반.", "The tray."), ('쪽지도 쟁반 위에 올라가요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'The note goes on the tray too. → <a href="context-en.html">the tray in front of the parrot</a>')),
        ("온도", "Temperature", ("엉뚱함 다이얼.", "The oddness dial."), ("낮으면 제일 흔한 콩만, 높으면 드문 콩도 골라요.", "Low picks only the most common bean; high lets rarer beans through.")),
    ],
}
