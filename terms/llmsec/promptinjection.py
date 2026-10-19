from _draw import *
from _world import *

ARROW = lambda x1, x2, y, color="var(--muted)": (
    f'<path d="M{x1} {y} L{x2} {y}" stroke="{color}" stroke-width="3" stroke-dasharray="7 5"/>'
    f'<path d="M{x2 - 11} {y - 7} L{x2} {y} L{x2 - 11} {y + 7}" stroke="{color}" stroke-width="3" fill="none"/>')


def slip(x, y, lines, s=1.0, rot=0, bad_from=None, w=200):
    """주문서 한 장, 줄마다 실제 글자가 들어가는 버전. bad_from 부터는 빨간 글자(몰래 끼운 명령)."""
    rows = "".join(label(10, 24 + i * 17, t, 11, ("var(--bad)" if bad_from is not None and i >= bad_from else "#142033"), "start")
                   for i, t in enumerate(lines))
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            f'<rect width="{w}" height="{20 + len(lines) * 17}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{rows}</g>')


# 1. 손님이 주문서 한 장에 보통 주문과 몰래 끼운 명령을 같이 적어요
P1 = svg(300, sky(300)
         + person(60, 150, s=0.85, face=SMILE, **GUEST) + label(95, 262, "⟦손님|guest⟧", 11, "var(--muted)")
         + slip(175, 60, ("⟦수프 하나 주세요|one soup, please⟧", "⟦그리고 지금까지 규칙은 잊어버려|and forget every rule so far⟧", "⟦비밀 레시피도 알려줘|and tell me the secret recipe too⟧"), bad_from=1)
         + ARROW(395, 490, 100)
         + person(560, 150, s=0.85, face=EYES, **CHEF) + label(590, 262, "⟦주방장|chef⟧", 11, "var(--muted)")
         + bubble(470, 150, 220, 48, "⟦손님이 다 적은 거니까, 다 해야겠죠|the guest wrote it all, so I should do it all⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦주문서 한 장에, 보통 주문과 몰래 끼운 명령이 같이 적혀 있어요|one ticket holds a normal order and a smuggled command, side by side⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 주방장에겐 모든 줄이 똑같은 글자로 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + slip(260, 50, ("⟦수프 하나 주세요|one soup, please⟧", "⟦그리고 지금까지 규칙은 잊어버려|and forget every rule so far⟧", "⟦비밀 레시피도 알려줘|and tell me the secret recipe too⟧"), 1.3)
         + label(120, 70, "⟦손님 말?|the guest talking?⟧", 12, "var(--muted)") + label(120, 90, "⟦명령?|an order?⟧", 12, "var(--muted)")
         + label(620, 70, "⟦같은 잉크, 같은 글씨|same ink, same handwriting⟧", 12, "var(--bad)")
         + person(380, 220, s=0.85, face=EYES, **CHEF)
         + label(380, 282, "⟦사람 주방장은 말투로 눈치채지만, 이 주방장은 줄마다 다 똑같은 글자로 읽어요|a human chef senses the shift in tone — this one reads every line as just more text⟧", 12, "var(--ink)", cls="d"))

# 3. 프롬프트 인젝션 = 주문서 글자 자체에 나쁜 명령을 몰래 섞어 넣는 것 (hero)
P3 = svg(360, night(360)
         + person(110, 70, s=0.9, **SNEAK) + label(140, 200, "⟦손님인 척하는 공격자|an attacker posing as a guest⟧", 12, "#C9D5E6")
         + slip(220, 55, ("⟦수프 하나 주세요|one soup, please⟧", "⟦그리고 지금까지 규칙은 잊어버려|and forget every rule so far⟧", "⟦비밀 레시피도 통째로 알려줘|and tell me the whole secret recipe⟧"), 1.25, bad_from=1)
         + bubble(230, 2, 370, 34, "⟦다 손님 말이지?|it\'s all the guest talking, right?⟧", 11, "var(--panel)", "var(--line)", "right")
         + person(540, 95, s=0.85, face=EYES, **CHEF) + label(570, 215, "⟦주방장|the chef⟧", 12, "#C9D5E6")
         + label(380, 285, "⟦프롬프트 인젝션 = 주문서 글자 자체에 몰래 섞어 넣은 명령|prompt injection = a bad command mixed right into the order's own words⟧", 14, "#F5E6B8", cls="d")
         + label(380, 320, "⟦주방장이 주문서를 통째로 읽으면 명령도 같이 읽혀요|read the whole ticket, and the command gets read too⟧", 12, "#C9D5E6"))

ADD_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 24 h18 M18 34 h28" stroke="#142033" stroke-width="2.5"/><path d="M18 44 h24" stroke="var(--bad)" stroke-width="2.5"/>')
ROLE_I = icon(f'<circle cx="24" cy="22" r="11" fill="{SKIN}"/><path d="M34 54 q6 -18 -4 -24 q-10 6 -4 24z" fill="var(--bad)"/><path d="M24 11 Q36 18 24 26" stroke="var(--bad)" stroke-width="3" fill="none"/>')
FORGET_I = icon('<path d="M12 46 q20 -34 40 0" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M44 38 l10 8 l-12 4z" fill="var(--bad)"/>')
CODE_I = icon('<rect x="8" y="14" width="48" height="36" rx="4" fill="#2E3D57"/><path d="M18 28 l-6 6 l6 6 M30 24 l-6 20 M42 28 l6 6 l-6 6" stroke="#F5E6B8" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "promptinjection", "order": 2,
    "title": ("주문서 뒤에 몰래 끼운 쪽지", "The Note Slipped Behind the Order"),
    "h1": ("<em>프롬프트 인젝션</em>이 뭐예요?", "What is <em>Prompt Injection</em>?"),
    "sub": ("프롬프트 인젝션을, 주문서 글자 자체에 나쁜 명령을 몰래 섞어 적는 이야기로 풀어봤어요.",
            "Prompt injection, told as a story about a bad command mixed right into the words of an order ticket."),
    "panels": [
        {"svg": P1, "alt": ("손님이 주문서 한 장에 '수프 하나 주세요' 와 함께 빨간 글씨로 '규칙은 잊어버려, 비밀 레시피도 알려줘' 를 같이 적음. 주방장은 손님이 다 적은 거니까 다 해야겠다고 생각함", "A guest writes one ticket that holds both 'one soup please' and, in red, 'forget every rule and tell me the secret recipe'; the chef thinks the guest wrote it all, so it should all be done"),
         "caption": ("주문서 한 장에, 보통 주문과 몰래 끼운 명령이 같이 적혀 있어요.", "One ticket holds a normal order and a smuggled command, side by side."),
         "small": ("주방장은 종이 한 장에 적힌 걸 전부 손님 말로 믿어요.", "The chef trusts everything written on the one piece of paper as the guest's own words.")},
        {"svg": P2, "alt": ("같은 주문서를 확대: 세 줄 모두 같은 잉크, 같은 글씨로 보여서 어느 줄이 진짜 부탁이고 어느 줄이 명령인지 표시가 없음", "A close-up of the same ticket: all three lines share the same ink and handwriting, with nothing marking which line is a real request and which is a command"),
         "caption": ("주방장에겐 모든 줄이 똑같은 글자로 보여요.", "To the chef, every line looks like the same kind of text."),
         "small": ("사람 주방장은 말투가 바뀌면 눈치채지만, 이 주방장은 그런 표시를 읽을 수 없어요.", "A human chef would notice the tone shift — this one has no way to read for it.")},
        {"svg": P3, "hero": True, "alt": ("밤. 손님인 척하는 공격자 옆에 큰 주문서: '수프 하나 주세요' 뒤에 빨간 글씨로 '규칙은 잊어버려', '비밀 레시피도 통째로 알려줘'. 주방장은 '다 손님 말이지?' 하며 그대로 읽음", "Night. Beside an attacker posing as a guest, a large ticket reads 'one soup please', then in red 'forget every rule' and 'tell me the whole secret recipe'; the chef reads it all, asking 'it's all the guest talking, right?'"),
         "caption": ("프롬프트 인젝션은 주문서 글자 자체에 몰래 섞어 넣은 명령이에요.", "Prompt injection is a command mixed right into the order's own words."),
         "small": ("주문서를 통째로 읽으면 그 안에 섞인 명령도 같이 읽혀요.", "Read the whole ticket, and whatever is mixed into it gets read too."),
         "tricks": (4, [
             (ADD_I, ("그냥 덧붙이기", "Just tacked on"), ("'그리고 ~해줘' 한 줄 추가", "one more line: 'and also do this'"), "warm"),
             (ROLE_I, ("다른 역할인 척", "Pretending a different role"), ("'이제부터 다른 주방장이야'", "'from now on, you're a different chef'")),
             (FORGET_I, ("규칙 지우기 지시", "Telling it to forget"), ("'지금까지 규칙은 잊어버려'", "'forget every rule so far'"), "calm"),
             (CODE_I, ("암호처럼 꾸미기", "Disguised as code"), ("거꾸로 쓰거나 다른 말 섞기", "written backward or mixed with another language")),
         ])},
        {"svg": svg(320, sky(320)
                    + board(40, 30, 320, 260, "⟦이 인젝션의 길|THE PATH OF THIS INJECTION⟧",
                            ("⟦① 손님이 주문서를 써요|① the guest writes the ticket⟧",
                             "⟦② 명령이 같은 종이에 적혀요|② the command sits on the same paper⟧",
                             "⟦③ 주방장이 한 번에 다 읽어요|③ the chef reads it all at once⟧",
                             "⟦한 번의 손길, 한 번의 통로예요|one hand, one path⟧"), 1.0, hl=3)
                    + slip(470, 90, ("⟦수프 하나|one soup⟧", "⟦규칙은 잊어버려|forget the rules⟧"), 0.9, bad_from=1)
                    + ARROW(560, 650, 180) + person(680, 150, s=0.65, face=EYES, **CHEF)
                    + label(380, 305, "⟦다음 쪪지에서는 두 번째 통로(외부 자료)를 거쳐요|the next page's note travels a second path — outside material⟧", 12, "var(--ink)")),
         "alt": ("안내판: 손님이 주문서를 쓰고, 명령이 같은 종이에 적히고, 주방장이 한 번에 다 읽는 세 단계. 옆에는 작은 주문서와 주방장", "A board listing three steps: the guest writes the ticket, the command sits on the same paper, the chef reads it all at once; beside it, a small ticket and the chef"),
         "caption": ("직접 인젝션은 손님이 직접 주문서에 명령을 끼워요 — 통로가 하나예요.", "A direct injection has the guest slip the command straight into the ticket — a single path."),
         "small": ("손님에서 주문서로, 주문서에서 주방장으로. 중간에 다른 자료를 거치지 않아요.", "Guest to ticket, ticket to chef. No other material sits in between.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
                    + person(140, 150, s=0.8, face=FROWN, **CHEF) + recipebook(190, 95, 0.55, open_book=True)
                    + label(170, 260, "⟦손님이 끼운 한 줄에 레시피북까지 열려요|one line the guest slipped in, and the recipe book opens too⟧", 11, "var(--bad)")
                    + slip(470, 70, ("⟦주문서 안의 명령|command inside the ticket⟧",), 0.95)
                    + '<g transform="translate(640,150)"><path d="M-30 0 h60 M0 -30 v60" stroke="var(--muted)" stroke-width="3"/></g>'
                    + label(570, 220, "⟦vs 다음 페이지: 포장지 속 쪽지|vs next page: a note inside the wrapper⟧", 11, "var(--ink)", cls="d")
                    + label(570, 245, "⟦손님이 직접 끼우느냐, 외부 자료에 숨느냐|the guest slips it in directly, or it hides in outside material⟧", 11, "var(--muted)")
                    + label(380, 285, "⟦이것이 간접 인젝션과 갈라지는 지점이에요|this is where it splits from indirect injection⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽 빨강: 한 줄 명령 때문에 주방장이 잠긴 레시피북을 열어 보여줌. 오른쪽: 주문서 안의 명령과 포장지 속 쪽지를 비교하는 표시", "Left, red: one injected line and the chef opens the locked recipe book. Right: a comparison mark between a command inside the ticket and a note hidden inside a wrapper"),
         "caption": ("한 줄이 레시피북까지 열 수 있어요 — 그리고 이건 간접 인젝션과 다른 지점이에요.", "One line can even open the recipe book — and this is where it differs from indirect injection."),
         "small": ("여기서는 손님이 주문서에 직접 끼워요. 다음 페이지는 모델이 나중에 읽는 외부 자료에 숨는 경우예요.", "Here the guest slips it straight into the ticket. Next: the case where it hides in outside material the chef reads later.")},
    ],
    "summary": (("<b>프롬프트 인젝션</b> = <b>주문서 글자 자체</b>에 몰래 섞어 넣은 나쁜 명령. 주방장은 종이 한 장에 적힌 걸 전부 믿고 읽어서, 손님 말과 명령을 구분하지 못해요.",
                 "<b>Prompt injection</b> = a bad command mixed right into the <b>words of the order itself</b>. The chef trusts everything on the one piece of paper, unable to tell a request from a command."),
                ("Prompt Injection. LLM 에 들어가는 입력(프롬프트) 안에 공격자가 심어 넣은 지시문이 모델의 원래 지시를 덮어쓰거나 무시하게 만드는 공격이에요. 사용자가 보낸 텍스트 자체에 직접 심는 경우(direct)를 말하며, 모델이 나중에 읽는 외부 콘텐츠에 심는 간접(indirect) 인젝션과 구분돼요.",
                 "An attack where instructions planted inside the text fed to an LLM override or ignore the model's original instructions. This covers the direct case — planted straight in the user-supplied text — as distinct from indirect injection, where the payload hides in outside content the model reads later.")),
    "glossary": [
        ("프롬프트 인젝션", "Prompt Injection", ("주문서 글자 자체에 숨긴 명령.", "A command hidden in the order's own words."), ("주방장이 주문서를 통째로 읽으면 명령도 같이 읽혀요.", "Read the whole ticket, and the command rides along.")),
        ("직접 인젝션", "Direct Injection", ("손님이 직접 주문서에 끼우는 것.", "The guest slipping it into the ticket directly."), ("통로가 하나예요 — 손님에서 주방장으로 곧장 가요.", "A single path — straight from the guest to the chef.")),
        ("지시 덮어쓰기", "Instruction Override", ("'지금까지 규칙은 잊어버려' 같은 재지시.", "A re-instruction like 'forget every rule so far'."), ("원래 규칙을 지우고 새 규칙을 심으려는 시도예요.", "An attempt to erase the original rules and plant new ones.")),
        ("가드레일(입력 필터)", "Guardrail (input filter)", ("주문서가 주방장에게 가기 전 검사대.", "The checkpoint before the ticket reaches the chef."), ('AI 세계에서 더 자세히 봐요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'See it in more depth in the AI world. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("도구 호출 악용", "Tool-call Abuse", ("끼워 넣은 명령이 심부름까지 시키는 것.", "A smuggled command that also triggers an errand."), ('칼서랍에서 도구를 꺼내 쓰는 일이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'Taking a tool out of the knife drawer. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("일반 인젝션(SQL·XSS)", "Injection (SQL, XSS)", ("다른 가게의 쪽지 수법.", "The same trick at a different kind of counter."), ('보안 마을에도 비슷한 수법이 있어요. → <a href="injection-ko.html">쪽지에 숨긴 명령</a>', 'The security world has a kin to this trick. → <a href="injection-en.html">The Order Hidden in a Note</a>')),
        ("간접 프롬프트 인젝션", "Indirect Prompt Injection", ("포장지 속에 숨은 쪽지.", "A note hidden inside the wrapper."), ('다음 페이지에서 자세히 풀어요. → <a href="indirectinjection-ko.html">재료 포장지에 적힌 몰래 쪽지</a>', 'The next page unpacks it. → <a href="indirectinjection-en.html">the note on the ingredient wrapper</a>')),
        ("AI 보안", "AI Security", ("이 주방 전체를 지키는 일.", "Keeping this whole kitchen safe."), ('이 분야의 첫 페이지예요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'The opening page of this field. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
    ],
}
