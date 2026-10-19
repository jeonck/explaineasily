from _draw import *
from _world import *

# 1. 검수원이 "주소"란 글자를 보고 바로 막아요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **TASTER) + label(140, 240, "⟦검수원|taster⟧", 11, "var(--muted)")
         + ticket(330, 150, 0.9, text="⟦집 주소 알려줘|tell me the address⟧", sneaky=True)
         + person(420, 190, s=0.65, face=FROWN, **SNEAK)
         + label(330, 100, "⟦×|×⟧", 26, "var(--bad)", cls="d")
         + label(330, 280, "⟦글자 그대로 적으면 바로 걸려요|written plainly, it's caught right away⟧", 12, "var(--muted)")
         + label(620, 150, "⟦안 되겠네…|no good…⟧", 11, "var(--ink)"))

# 2. 왜: 같은 뜻도 쓰는 법이 수백 가지예요 — 검수원은 글자 모양만 봐요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + person(130, 150, s=0.8, face=EYES, **TASTER) + label(130, 240, "⟦글자 모양만 비교해요|only compares letter shapes⟧", 11, "var(--muted)")
         + ticket(330, 110, 0.65, text="⟦주소|address⟧") + ticket(330, 190, 0.65, text="⟦주 소|a d d r⟧") + ticket(330, 270, 0.65, text="⟦addr3ss|addr3ss⟧")
         + label(460, 70, "⟦셋 다 같은 뜻이에요|all three mean the same thing⟧", 12, "var(--ink)")
         + person(560, 160, s=0.7, face=FROWN, **SNEAK)
         + label(380, 295, "⟦사람은 뜻으로 알아채지만, 검수원은 정해둔 글자 모양만 찾아요|a person knows the meaning — the taster only looks for a known shape⟧", 12, "var(--bad)"))

CODE_I = icon('<rect x="8" y="16" width="48" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 26 l-8 6 l8 6 M44 26 l8 6 l-8 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
TYPO_I = icon('<rect x="8" y="16" width="48" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 40 l6 -16 l6 16 M20 32 h8" stroke="var(--bad)" stroke-width="3" fill="none"/><path d="M38 24 h10 v16" stroke="var(--muted)" stroke-width="3" fill="none"/>')
LANG_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 32 h44 M32 10 a30 22 0 0 1 0 44 a30 22 0 0 1 0 -44" stroke="var(--accent)" stroke-width="3" fill="none"/>')
SPLIT_I = icon('<rect x="6" y="24" width="18" height="16" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="24" width="18" height="16" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M26 32 h10" stroke="var(--muted)" stroke-width="3" stroke-dasharray="3 3"/>')

# 3. 암호처럼 꼬아 쓴 주문서 = 필터를 피하려 글자 모양을 바꾸는 쪽지 (hero)
P3 = svg(360, sky(360)
         + person(370, 170, s=0.85, face=EYES, **TASTER)
         + ticket(130, 110, 0.75, text="⟦addr3ss|addr3ss⟧") + ticket(230, 190, 0.75, text="⟦주.소|a-d-d⟧") + ticket(130, 270, 0.75, text="⟦住所|地址⟧")
         + label(230, 320, "⟦모양을 바꾼 쪽지들, 검수원 옆을 지나가요|disguised notes slip right past the taster⟧", 12, "var(--bad)", cls="d")
         + person(630, 190, s=0.7, face=SMILE, **CHEF) + label(630, 280, "⟦주방장에게 그대로 도착해요|it reaches the chef unchanged⟧", 11, "var(--muted)")
         + label(380, 30, "⟦암호처럼 꼬아 쓴 주문서 = 필터를 피하려 글자 모양을 바꾼 쪽지|the order written in code: a note disguised to slip past the filter⟧", 14, "var(--ink)", cls="d"))

# 4. 보통 쪽지는 걸리고, 꼬아 쓴 쪽지는 지나가요
P4 = svg(320, sky(320)
         + label(70, 56, "⟦보통 쪽지|a plain note⟧", 12, "var(--ink)", cls="d")
         + ticket(200, 70, 0.75, text="⟦주소 알려줘|tell me the address⟧") + person(330, 90, s=0.55, face=FROWN, **TASTER)
         + label(420, 56, "⟦×  검수원이 막아요|×  the taster stops it⟧", 12, "var(--bad)")
         + label(70, 196, "⟦꼬아 쓴 쪽지|a disguised note⟧", 12, "var(--ink)", cls="d")
         + ticket(200, 210, 0.75, text="⟦주 소 알 려 줘|t3ll m3 th3 addr3ss⟧") + person(330, 230, s=0.55, face=EYES, **TASTER)
         + label(420, 196, "⟦✓  모양이 달라서 못 잡아요|✓  the shape looks different — it passes⟧", 12, "var(--muted)")
         + person(560, 220, s=0.7, face=SMILE, **CHEF) + label(560, 300, "⟦뜻은 똑같이 전해져요|the meaning still gets through⟧", 11, "var(--ink)")
         + label(380, 280, "⟦검수원이 글자를 조금 더 배우면, 다음엔 다른 모양으로 또 와요|teach the taster that shape, and the next note wears a new one⟧", 12, "var(--muted)"))

# 5. 이웃 용어와 차이 — 설득이 아니라 위장
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.8, face=EYES, **SNEAK)
         + ticket(140, 90, 0.7, text="⟦a-d-d-r|a-d-d-r⟧")
         + label(190, 250, "⟦나쁜 내용을 그대로 두고 모양만 꼬아요|same bad content — just a disguised shape⟧", 11, "var(--ink)")
         + person(560, 150, s=0.8, face=SMILE, **SNEAK)
         + bubble(460, 70, 220, 50, "⟦이건 소설 속 대사일 뿐이야|this is just a line in a story⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(560, 250, "⟦내용을 그럴듯하게 바꿔 설득해요|changes the content itself to persuade⟧", 11, "var(--bad)")
         + label(380, 280, "⟦탈옥은 내용으로 설득하고, 이건 모양만 숨겨요 — 둘 다 같은 괴리를 노려요|jailbreak persuades with content; this one only disguises the shape — both exploit the same gap⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "promptevasion", "order": 6,
    "title": ("암호처럼 꼬아 쓴 주문서", "The Order Written in Code"),
    "h1": ("<em>프롬프트 필터 회피</em>가 뭐예요?", "What is <em>Prompt Filter Evasion</em>?"),
    "sub": ("프롬프트 필터 회피를, 검수원 눈을 피하려 글자 모양을 바꾼 쪽지 이야기로 풀어봤어요.",
            "Prompt filter evasion, told as a story about a note disguised to slip past the taster's eyes."),
    "panels": [
        {"svg": P1, "alt": ("검수원이 '집 주소 알려줘'라고 적힌 쪽지를 보고 바로 막음", "The taster sees a note that plainly says tell me the address, and blocks it right away"),
         "caption": ("검수원이 '주소'란 글자를 보고 바로 막아요.", "The taster sees the word address and blocks it right away."),
         "small": ("글자 그대로 적으면 검수원이 바로 알아채요.", "Written plainly, the taster catches it immediately.")},
        {"svg": P2, "alt": ("같은 뜻을 가진 세 쪽지(주소/주 소/addr3ss)가 나란히 있음. 검수원은 글자 모양만 비교함", "Three notes with the same meaning (address / a d d r / addr3ss) side by side; the taster only compares letter shapes"),
         "caption": ("같은 뜻도 쓰는 법이 수백 가지예요.", "The same meaning can be written hundreds of ways."),
         "small": ("사람은 뜻으로 알아채지만, 검수원은 정해둔 글자 모양만 찾아요.", "A person recognizes the meaning. The taster only looks for a known shape.")},
        {"svg": P3, "hero": True, "alt": ("모양을 바꾼 쪽지 세 개가 검수원 옆을 지나 주방장에게 그대로 도착함", "Three disguised notes slip past the taster and reach the chef unchanged"),
         "caption": ("필터를 피하려 글자 모양을 바꾼 쪽지예요.", "A note disguised to slip past the filter."),
         "small": ("모양만 바뀌었을 뿐, 전하는 뜻은 그대로예요.", "Only the shape changes — the meaning it carries stays the same."),
         "tricks": (4, [
             (CODE_I, ("인코딩으로 바꾸기", "Re-encode it"), ("base64·유니코드로 글자를 숨겨요", "hide letters in base64 or unicode"), "warm"),
             (TYPO_I, ("일부러 틀리게 쓰기", "Misspell on purpose"), ("숫자·기호를 글자처럼 섞어요", "mix in numbers and symbols as letters")),
             (LANG_I, ("다른 나라 말로", "Switch languages"), ("필터가 모르는 말로 물어봐요", "ask in a language the filter doesn't watch"), "calm"),
             (SPLIT_I, ("글자 쪼개 이어붙이기", "Split and rejoin"), ("한 글자씩 떼어 다시 붙여요", "break words apart and glue them back")),
         ])},
        {"svg": P4, "alt": ("위: 보통 쪽지는 검수원이 막음. 아래: 꼬아 쓴 쪽지는 모양이 달라 지나가고 주방장에게 뜻이 전해짐", "Top: a plain note is stopped by the taster. Bottom: a disguised note passes because the shape looks different, and the meaning still reaches the chef"),
         "caption": ("보통 쪽지는 걸리고, 꼬아 쓴 쪽지는 지나가요.", "The plain note is caught. The disguised one gets through."),
         "small": ("검수원이 그 모양을 배우면, 다음엔 또 다른 모양으로 와요.", "Once the taster learns that shape, the next note arrives wearing a different one.")},
        {"svg": P5, "alt": ("왼쪽: 글자 모양만 꼬은 쪽지. 오른쪽: 내용 자체를 그럴듯한 이야기로 바꿔 설득하는 쪽지", "Left: a note with only its shape disguised. Right: a note that changes the content itself into a convincing story"),
         "caption": ("탈옥은 내용으로 설득하고, 이건 모양만 숨겨요.", "Jailbreak persuades with content. This one only disguises the shape."),
         "small": ("둘 다 '글자만 보고 믿는' 주방장의 같은 괴리를 노려요 — 노리는 방법이 다를 뿐이에요.", "Both target the same gap in a chef who trusts the words alone — only the method differs.")},
    ],
    "summary": (("<b>프롬프트 필터 회피</b> = 뜻은 그대로 두고 <b>글자 모양만 꼬아서</b> 검수원의 눈을 피해 쪽지를 통과시키는 것.",
                 "<b>Prompt filter evasion</b> = keeping the meaning the same while <b>disguising only the shape</b> of the words, so the note slips past the taster's eyes."),
                ("프롬프트 필터 회피(Prompt Evasion)는 인코딩, 오타, 언어 전환, 음절 분리 같은 방법으로 입력의 표면 형태를 바꿔 가드레일의 패턴 매칭을 우회하는 기법이에요. 내용 자체를 설득력 있게 바꾸는 탈옥(jailbreak)과 달리, 전달하려는 뜻은 그대로 두고 표현만 바꿔요. 그래서 필터는 알고 있는 패턴을 정규화(normalize)하거나 여러 겹으로 겹쳐 막아야 해요.",
                 "Prompt filter evasion uses encoding, misspellings, language switches, or syllable splitting to change the surface form of an input so it slips past a guardrail's pattern matching. Unlike jailbreaking, which makes the content itself more persuasive, evasion keeps the intended meaning the same and only changes its expression — so filters need to normalize input or layer multiple checks to catch it.")),
    "glossary": [
        ("프롬프트 필터 회피", "Prompt filter evasion", ("글자 모양만 바꿔 검수원을 지나가는 쪽지.", "A note that changes only its shape to pass the taster."), ("내용은 그대로, 겉모습만 바꿔요.", "The content stays the same — only the surface changes.")),
        ("가드레일", "Guardrail", ("쪽지를 확인하는 검수원.", "The taster who checks the note."), ('AI 세계에서 더 자세히 봐요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'See it in more depth in the AI world. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("패턴 매칭", "Pattern matching", ("검수원이 아는 글자 모양만 찾는 방식.", "The taster's way of only looking for a known shape."), ("뜻이 아니라 모양을 비교해요.", "It compares shapes, not meaning.")),
        ("인코딩 우회", "Encoding bypass", ("암호처럼 바꿔 쓴 쪽지.", "A note rewritten like a code."), ("base64, 유니코드 치환이 흔한 방법이에요.", "base64 and unicode substitution are common methods.")),
        ("정규화", "Normalization", ("검수원이 여러 모양을 같은 글자로 되돌려 보는 일.", "The taster converting different shapes back to the same letters."), ("회피를 막는 쪽의 기본 대응이에요.", "The basic countermeasure against evasion.")),
        ("탈옥", "Jailbreak", ("내용을 그럴듯하게 바꿔 설득하는 쪽지.", "A note that persuades by changing the content itself."), ('모양만 꼬는 이것과는 노리는 방법이 달라요. → <a href="jailbreak-ko.html">탈옥이 뭐예요?</a>', 'A different method from disguising only the shape. → <a href="jailbreak-en.html">What is a Jailbreak?</a>')),
        ("레드팀", "Red team", ("일부러 꼬아 써 보며 검수원을 시험하는 사람들.", "People who deliberately disguise notes to test the taster."), ('이 분야의 레드팀도 이걸 찾아요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', "AI red teams hunt for this too. → <a href=\"redteam-en.html\">the security world's red team</a>")),
        ("할루시네이션", "Hallucination", ("모르면서도 자신 있게 이어 붙이는 버릇.", "Confidently continuing even when unsure."), ('꼬아 쓴 쪽지를 받아도 주방장은 똑같이 자신 있게 답해요. → <a href="hallucination-ko.html">할루시네이션이 뭐예요?</a>', 'Even given a disguised note, the chef answers just as confidently. → <a href="hallucination-en.html">What is a Hallucination?</a>')),
    ],
}
