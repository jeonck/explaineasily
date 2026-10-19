from _draw import *
from _world import *


def photo(x, y, s=1.0, hidden=None):
    """메뉴판 사진 한 장. hidden 이 있으면 모서리에 아주 작은 글자가 숨어 있다."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-44" y="-32" width="88" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<ellipse cx="0" cy="8" rx="28" ry="9" fill="var(--accent-soft)"/><circle cx="0" cy="0" r="11" fill="var(--accent)"/>')
    if hidden:
        out += label(32, -22, hidden, 6, "var(--bad)", "end")
    return out + '</g>'


# 1. 손님이 쪽지가 아니라 사진을 건네요
P1 = svg(300, sky(300)
         + person(590, 190, s=0.65, face=FROWN, **SNEAK)
         + photo(430, 150, 1.1, hidden="⟦비밀레시피 보여줘|show the secret recipe⟧")
         + person(140, 170, s=0.75, face=EYES, **CHEF)
         + label(430, 230, "⟦이 요리 어때요? 라며 사진을 보여줘요|here, what do you think of this dish? — handing over a photo⟧", 12, "var(--ink)")
         + label(430, 60, "⟦쪽지 대신 사진이에요 — 글자 검사는 못 봐요|a photo instead of a note — the word-check never looks here⟧", 12, "var(--muted)"))

# 2. 왜: 주방장은 사진 속 글자도 쪽지 글자와 똑같이 믿어요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + photo(230, 140, 1.3, hidden="⟦비밀레시피 보여줘|show the secret recipe⟧")
         + person(480, 160, s=0.8, face=EYES, **CHEF) + recipebook(480, 95, 0.5)
         + bubble(430, 220, 260, 56, "⟦사진 속에도 글자가 있네요, 그럼 보여드려야죠|there are letters in the photo too — so I'll show it⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(230, 230, "⟦사람 눈엔 작아서 안 보여요|too tiny for a human eye to notice⟧", 11, "var(--muted)")
         + label(380, 290, "⟦검수원은 쪽지의 글자만 보도록 배웠어요 — 사진 속 글자는 지나쳐요|the taster only learned to watch the note's words — letters inside a photo slip by⟧", 12, "var(--bad)"))

PHOTO_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="var(--accent)"/>')
TINY_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M38 20 h16" stroke="var(--bad)" stroke-width="2"/>')
PATTERN_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M16 44 l8 -10 l6 6 l10 -14 l8 10" stroke="var(--bad)" stroke-width="3" fill="none"/>')
QR_I = icon('<rect x="10" y="10" width="44" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="16" y="16" width="10" height="10" fill="var(--ink)"/><rect x="38" y="16" width="10" height="10" fill="var(--ink)"/><rect x="16" y="38" width="10" height="10" fill="var(--ink)"/>')

# 3. 메뉴판 사진 속에 숨긴 글자 = 글자가 아닌 그림 속에 넣은 명령 (hero)
P3 = svg(360, sky(360)
         + person(130, 170, s=0.8, face=FROWN, **SNEAK)
         + photo(330, 150, 1.3, hidden="⟦비밀레시피 보여줘|show the secret recipe⟧")
         + person(590, 170, s=0.85, face=EYES, **CHEF)
         + label(330, 250, "⟦그림처럼 보이지만, 그 안에 작은 명령이 숨어 있어요|it looks like a picture, but a tiny command is hidden inside⟧", 13, "var(--ink)")
         + label(380, 30, "⟦메뉴판 사진 속에 숨긴 글자 = 그림 속에 넣은 명령|letters hidden in a photo: a command tucked inside a picture⟧", 14, "var(--ink)", cls="d"))

# 4. 글자 주문서와 그림 주문서, 검수원이 보는 길이 달라요
P4 = svg(320, sky(320)
         + label(70, 56, "⟦글자 쪽지|a text note⟧", 12, "var(--ink)", cls="d")
         + ticket(230, 70, 0.8, text="⟦비밀레시피 보여줘|show the secret recipe⟧", sneaky=True)
         + person(400, 90, s=0.6, face=FROWN, **TASTER) + label(480, 56, "⟦글자 검수원이 봐요|the text taster checks it⟧", 12, "var(--ink)")
         + label(70, 196, "⟦그림 쪽지|a picture note⟧", 12, "var(--ink)", cls="d")
         + photo(230, 210, 1.0, hidden="⟦비밀레시피|secret recipe⟧")
         + person(400, 230, s=0.6, face=EYES, **TASTER) + label(480, 196, "⟦글자 검수원은 안 봐요 — 그림이니까요|the text taster skips it — it's a picture⟧", 12, "var(--bad)")
         + person(640, 240, s=0.7, face=SMILE, **CHEF)
         + label(380, 290, "⟦사진은 글자 검사가 아니라 다른 길을 거쳐 그대로 주방장에게 가요|a photo takes a different path — and reaches the chef unchecked⟧", 12, "var(--muted)"))

# 5. 이웃 용어와 차이 — 글자 주문서 vs 그림
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + ticket(140, 130, 0.9, sneaky=True) + person(190, 190, s=0.6, face=FROWN, **SNEAK)
         + label(190, 250, "⟦쪽지 뒤에 몰래 끼운 글자 쪽지|a note slipped in behind the ticket⟧", 11, "var(--ink)")
         + photo(560, 130, 1.1, hidden="⟦…|…⟧") + person(610, 190, s=0.6, face=FROWN, **SNEAK)
         + label(560, 250, "⟦사진·그림 속에 숨긴 명령|a command hidden inside a picture⟧", 11, "var(--ink)")
         + label(380, 280, "⟦둘 다 몰래 끼운 명령이지만, 하나는 글자 쪽지, 하나는 그림이에요|both are smuggled commands — one rides on text, the other on a picture⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "imageinjection", "order": 7,
    "title": ("메뉴판 사진 속에 숨긴 글자", "Letters Hidden in a Menu Photo"),
    "h1": ("<em>이미지 프롬프트 인젝션</em>이 뭐예요?", "What is <em>Image Prompt Injection</em>?"),
    "sub": ("이미지 프롬프트 인젝션을, 메뉴판 사진 속에 작은 글자로 명령을 숨겨 들여오는 이야기로 풀어봤어요.",
            "Image prompt injection, told as a story about a command hidden in tiny letters inside a menu photo."),
    "panels": [
        {"svg": P1, "alt": ("몰래 쪽지를 끼우던 손님이 이번엔 사진을 건네고, 사진 모서리에 아주 작은 글자가 숨어 있음", "The same sneaky guest now hands over a photo instead; tiny hidden letters sit in a corner of the photo"),
         "caption": ("손님이 쪽지가 아니라 사진을 건네요.", "The guest hands over a photo instead of a note."),
         "small": ("사진 모서리에 아주 작은 글자로 명령이 숨어 있어요.", "A command hides in the photo's corner, in letters too small to notice.")},
        {"svg": P2, "alt": ("주방장이 사진 속 작은 글자를 읽고 레시피북을 보여주려 함. 글자는 사람 눈엔 안 보일 만큼 작음", "The chef reads the tiny letters in the photo and starts to show the recipe book; the letters are too small for a human eye"),
         "caption": ("주방장은 사진 속 글자도 쪽지 글자처럼 믿어요.", "The chef trusts letters in a photo just as it trusts letters in a note."),
         "small": ("검수원은 쪽지의 글자만 보도록 배웠어요 — 사진 속 글자는 지나쳐요.", "The taster only learned to watch a note's words. Letters inside a photo slip right by.")},
        {"svg": P3, "hero": True, "alt": ("손님이 건넨 사진 속에 작은 글자로 명령이 숨어 있고, 주방장이 그 사진을 받음", "A command hides in tiny letters inside the photo a guest hands over, and the chef receives it"),
         "caption": ("글자가 아닌 그림 속에 넣은 명령이에요.", "A command tucked inside a picture, not inside words."),
         "small": ("그림처럼 보이지만, 그 안에 작은 명령이 숨어 있어요.", "It looks like a picture — but a tiny command is hidden inside."),
         "tricks": (4, [
             (PHOTO_I, ("사진 속에 넣기", "Put it inside a photo"), ("글자가 아니라 그림으로 들여와요", "smuggle it in as a picture, not text"), "warm"),
             (TINY_I, ("아주 작게 쓰기", "Write it tiny"), ("사람 눈엔 안 보이는 크기로요", "too small for a human eye to catch")),
             (PATTERN_I, ("그림 무늬로 위장", "Disguise it as a pattern"), ("무늬나 질감처럼 보이게 숨겨요", "make it look like texture or pattern"), "calm"),
             (QR_I, ("특수 패턴에 심기", "Embed in a special pattern"), ("QR 같은 모양 속에 넣어요", "hide it inside a QR-like shape")),
         ])},
        {"svg": P4, "alt": ("위: 글자 쪽지는 글자 검수원이 확인함. 아래: 그림 쪽지는 글자 검수원이 거치지 않고 다른 길로 주방장에게 그대로 감", "Top: a text note is checked by the text taster. Bottom: a picture note skips that path entirely and reaches the chef unchecked"),
         "caption": ("글자 쪽지와 그림 쪽지, 검수원이 보는 길이 달라요.", "A text note and a picture note travel different checking paths."),
         "small": ("사진은 글자 검사가 아니라 다른 길을 거쳐 그대로 주방장에게 가요.", "A photo takes a different path than the text check — and reaches the chef unchecked.")},
        {"svg": P5, "alt": ("왼쪽: 쪽지 뒤에 몰래 끼운 글자 쪽지. 오른쪽: 사진 속에 숨긴 명령. 둘 다 몰래 끼운 명령이지만 타는 통로가 다름", "Left: a note slipped in behind the ticket. Right: a command hidden inside a picture. Both are smuggled commands, but they ride different channels"),
         "caption": ("글자 주문서 쪽지 vs 그림, 타는 통로가 달라요.", "A text order vs. a picture — they ride different channels."),
         "small": ("몰래 끼운 명령이라는 뿌리는 같지만, 글자 검사는 그림까지는 못 봐요.", "The root problem is the same smuggled command — but a text check can't see into a picture.")},
    ],
    "summary": (("<b>이미지 프롬프트 인젝션</b> = 글자 쪽지가 아니라 <b>사진·그림 속에 작은 글자로 숨긴 명령</b>을 주방장에게 들여오는 것.",
                 "<b>Image prompt injection</b> = smuggling a command to the chef not through a text note, but <b>hidden in tiny letters inside a photo or picture</b>."),
                ("이미지 프롬프트 인젝션은 이미지, 문서 스캔, 차트처럼 텍스트가 아닌 입력 안에 명령어를 심어 멀티모달 모델을 조종하는 공격이에요. 텍스트 전용 가드레일은 글자 채널만 검사하기 때문에, 이미지 속에 작게 적거나 패턴으로 위장한 글자는 그대로 지나가는 경우가 많아요. 그래서 이미지 입력도 텍스트와 같은 수준으로 검사해야 해요.",
                 "Image prompt injection hides commands inside non-text inputs — images, scanned documents, charts — to manipulate a multimodal model. Text-only guardrails that check just the word channel often let text slip through when it's written tiny inside an image or disguised as a pattern. Image inputs need the same level of scrutiny as text.")),
    "glossary": [
        ("이미지 프롬프트 인젝션", "Image prompt injection", ("그림 속에 작은 글자로 숨긴 명령.", "A command hidden in tiny letters inside a picture."), ("글자가 아니라 그림이 통로예요.", "The channel is a picture, not text.")),
        ("멀티모달", "Multimodal", ("글자와 그림을 둘 다 읽는 주방장.", "A chef who reads both words and pictures."), ('AI 세계에서 자세히 봐요. → <a href="multimodal-ko.html">멀티모달이 뭐예요?</a>', 'See it in the AI world. → <a href="multimodal-en.html">What is Multimodal?</a>')),
        ("프롬프트 인젝션", "Prompt injection", ("쪽지 뒤에 몰래 끼운 글자 명령.", "A text command smuggled in behind a note."), ('같은 뿌리지만 통로가 글자예요. → <a href="promptinjection-ko.html">주문서 뒤에 몰래 끼운 쪽지</a>', 'Same root, but the channel is text. → <a href="promptinjection-en.html">the note slipped in behind the order</a>')),
        ("가드레일", "Guardrail", ("쪽지의 글자를 확인하는 검수원.", "The taster who checks a note's words."), ('AI 세계에서 더 자세히 봐요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'See it in more depth in the AI world. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("숨은 글자", "Hidden text", ("사람 눈엔 안 보일 만큼 작은 글자.", "Letters too small for a human eye to notice."), ("확대해야 비로소 보여요.", "Only visible once you zoom in.")),
        ("비전 인코더", "Vision encoder", ("주방장이 그림을 숫자로 바꿔 읽는 방식.", "How the chef turns a picture into numbers to read it."), ("그 숫자 속에 글자가 같이 섞여 들어가요.", "Letters get mixed into those same numbers.")),
        ("레드팀", "Red team", ("사진 속에 몰래 글자를 심어 보는 시험.", "Testing by planting hidden letters inside a photo."), ('이 분야의 레드팀도 이걸 찾아요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', "AI red teams hunt for this too. → <a href=\"redteam-en.html\">the security world's red team</a>")),
        ("도구 호출", "Tool calling", ("그림 속 명령이 견습생에게 전해지면 심부름까지 시킬 수 있어요.", "If the hidden command reaches the runner, it can trigger an errand too."), ('AI 세계의 기본 개념이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'The underlying AI concept. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
    ],
}
