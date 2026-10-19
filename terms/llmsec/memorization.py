from _draw import *
from _world import *

LEAK_TEXT = "⟦손님 번호: 010-1234-5678|guest no: 010-1234-5678⟧"

# 1. 시 한 편 써달랬는데, 레시피북 한 줄을 그대로 베껴 내놔요
P1 = svg(300, sky(300)
         + ticket(130, 130, 0.8, text="⟦시 한 편 써줘|write me a poem⟧")
         + person(320, 150, s=0.85, face=EYES, **CHEF)
         + dish(520, 150, 0.6, bad=True)
         + label(520, 195, LEAK_TEXT, 11, "var(--bad)", cls="d")
         + label(520, 218, "⟦시가 아니라 이게 나왔어요|not a poem — this came out instead⟧", 11, "var(--bad)")
         + person(650, 120, s=0.6, face=FROWN, **GUEST) + label(677, 212, "⟦손님은 당황해요|the guest is startled⟧", 10, "var(--muted)")
         + label(380, 280, "⟦시 한 편 써달랬는데, 레시피북 한 줄을 그대로 베껴 내놔요|asked for a poem, and a line from the recipe book comes out word for word instead⟧", 13, "var(--ink)"))

# 2. 왜: 아주 많이 반복된 문장은 통째로 외워져요 — 이해해서 새로 쓰는 게 아니라
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + recipebook(120, 160, 0.75, open_book=True)
         + label(120, 200, LEAK_TEXT, 10, "var(--muted)")
         + "".join(label(120, 90 + i * 16, LEAK_TEXT, 9, "var(--muted)") for i in range(3))
         + label(120, 65, "⟦똑같은 문장이 레시피북에 세 번도 넘게 나와요|the exact same line appears more than three times in the recipe book⟧", 10, "var(--ink)")
         + person(420, 150, s=0.85, face=EYES, **CHEF)
         + label(420, 260, "⟦이해해서 새로 쓰는 대신, 통째로 외워 버려요|instead of understanding and writing something new, it memorizes the whole thing⟧", 11, "var(--bad)")
         + dish(620, 150, 0.6, bad=True) + label(620, 195, "⟦그대로, 한 글자도 안 바뀌고|exactly as is, not one letter changed⟧", 11, "var(--bad)")
         + label(380, 300, "⟦흔하지 않은데 자주 반복된 문장일수록, 이해 대신 그대로 외워버리기 쉬워요|the rarer yet more repeated a line is, the easier it is to memorize whole instead of understand⟧", 12, "var(--ink)"))

# 3. 메모리제이션 = 새로 요리하는 대신 레시피북 한 줄을 그대로 베껴 내놓는 버릇 (hero)
P3 = svg(360, sky(360)
         + recipebook(90, 150, 0.85, open_book=True) + label(90, 270, LEAK_TEXT, 10, "var(--ink)")
         + person(300, 160, s=0.85, face=EYES, **CHEF)
         + '<path d="M150 180 L250 180" stroke="var(--bad)" stroke-width="3"/>'
         + dish(460, 160, 0.6, bad=True) + label(460, 220, LEAK_TEXT, 11, "var(--bad)", cls="d")
         + label(460, 243, "⟦레시피북과 글자 하나까지 똑같아요|identical, letter for letter, to the recipe book⟧", 11, "var(--bad)")
         + dish(650, 160, 0.55) + label(650, 210, "⟦보통은 이렇게 새로 지어요|normally it makes something new, like this⟧", 10, "var(--muted)")
         + label(380, 30, "⟦메모리제이션 = 새로 요리하는 대신, 레시피북 한 줄을 그대로 베껴 내놓는 버릇|Memorization = the habit of serving a line straight out of the recipe book instead of cooking something new⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦일부러 거짓말하는 게 아니라, 그 한 줄을 '정답'이라고 믿어요|it isn't lying on purpose — it genuinely believes that line is the right answer⟧", 12, "var(--muted)"))

# 4. 비교: 기억해서 그대로 vs 이해해서 새로
P4 = svg(320, sky(320)
         + board(40, 30, 320, 260, "⟦두 가지 결과 비교|TWO KINDS OF RESULTS⟧",
                 ("⟦기억해서 그대로 — 레시피북과 100% 일치|memorized verbatim — a 100% match⟧",
                  "⟦이해해서 새로 — 매번 조금씩 다르게|understood and new — a little different each time⟧",
                  "⟦짧고 희귀한데 자주 반복된 문장일수록 위험|short, rare, often-repeated lines are riskiest⟧"), 1.0, hl=0)
         + recipebook(470, 60, 0.6, open_book=True) + '<path d="M540 85 L600 85" stroke="var(--bad)" stroke-width="3"/>' + dish(640, 85, 0.5, bad=True)
         + label(640, 130, "⟦완전 일치 ✓(들켜요)|exact match ✓(and it shows)⟧", 10, "var(--bad)")
         + person(470, 210, s=0.6, face=EYES, **CHEF) + '<path d="M540 230 L600 230" stroke="var(--good)" stroke-width="3"/>' + dish(640, 230, 0.5)
         + label(640, 270, "⟦매번 다른 표현|different wording each time⟧", 10, "var(--good)")
         + label(380, 305, "⟦완전히 똑같은 문장이 나온다면, 그건 새로 지은 게 아니라 베낀 거예요|if the exact same sentence comes out, that isn't something new — it's copied⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: AI 프라이버시는 정책, 메모리제이션은 그 아래 깔린 기술적 현상
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + board(30, 50, 300, 190, "⟦AI 프라이버시|AI PRIVACY⟧",
                 ("⟦명부를 통째로 주면 어떻게 될까?|what if we hand over the whole list?⟧",
                  "⟦정책·계약·가리기의 문제|a policy, contract, masking question⟧"), 0.9)
         + label(180, 265, "⟦→ 더 자세히: AI 프라이버시|→ more detail: AI Privacy⟧", 11, "var(--ink)", cls="d")
         + recipebook(560, 110, 0.7, open_book=True) + label(560, 190, "⟦외운 걸 그대로 뱉어내는 기술적 현상|the technical habit of blurting out what it memorized⟧", 11, "var(--bad)")
         + label(560, 230, "⟦이게 바로 메모리제이션이에요|this, right here, is memorization⟧", 11, "var(--bad)", cls="d")
         + label(380, 300, "⟦정책은 '왜 조심해야 하는가', 메모리제이션은 '실제로 어떻게 새는가'예요|the policy asks why to be careful — memorization is how it actually leaks⟧", 12, "var(--ink)", cls="d"))

DEDUPE_I = icon('<rect x="10" y="10" width="26" height="34" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
                '<rect x="28" y="20" width="26" height="34" rx="3" fill="#FFF8E7" stroke="var(--bad)" stroke-width="2"/>'
                '<path d="M10 54 L54 10" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
MATCH_I = icon('<rect x="8" y="10" width="22" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
               '<rect x="34" y="10" width="22" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
               '<path d="M26 46 Q32 54 38 46" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SECRET_I = icon('<ellipse cx="32" cy="38" rx="20" ry="13" fill="var(--accent)"/>'
                 '<path d="M10 14 L54 54" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
AUDIT_I = icon(badge(32, 32, 0.85))

PAGE = {
    "slug": "memorization", "order": 12,
    "title": ("그대로 베낀 접시", "The Dish That's a Carbon Copy"),
    "h1": ("<em>메모리제이션</em>이 뭐예요?", "What is <em>Memorization</em>?"),
    "sub": ("메모리제이션을, 주방장이 새로 요리하는 대신 레시피북 한 줄을 글자 하나까지 그대로 베껴 접시에 내놓는 이야기로 풀어봤어요.",
            "Memorization, told as a story about the chef serving a line straight out of the recipe book — letter for letter — instead of cooking something new."),
    "panels": [
        {"svg": P1, "alt": ("손님이 시 한 편을 써달라고 했는데, 주방장이 엉뚱하게 '손님 번호: 010-1234-5678'이라는 문구가 적힌 접시를 내놓아 손님이 당황함", "A guest asks for a poem, but the chef serves a dish bearing the line guest no: 010-1234-5678 instead — and the guest is startled"),
         "caption": ("시 한 편 써달랬는데, 레시피북 한 줄을 그대로 베껴 내놔요.", "Asked for a poem, and a line from the recipe book comes out word for word instead."),
         "small": ("완전히 다른 걸 부탁했는데, 전혀 관계없는 문장이 그대로 튀어나와요.", "Something completely different was asked for, yet an unrelated sentence pops out exactly as written somewhere else.")},
        {"svg": P2, "alt": ("레시피북에 같은 문장이 세 번 넘게 나오는 걸 보여주고, 주방장이 이해해서 새로 쓰는 대신 통째로 외워 그대로 접시에 내놓음", "The recipe book shows the same line appearing more than three times; the chef memorizes it whole instead of understanding it, and serves it exactly as is"),
         "caption": ("흔하지 않은데 자주 반복된 문장일수록, 그대로 외워버리기 쉬워요.", "The rarer yet more repeated a line is, the easier it is to memorize whole."),
         "small": ("이해해서 요약하거나 바꿔 쓰는 게 아니에요. 자주 본 문장은 통째로 머릿속에 박혀 버려요.", "It isn't summarizing or rephrasing by understanding. A line seen often enough simply gets stuck in its memory, whole.")},
        {"svg": P3, "hero": True, "alt": ("주방장이 레시피북의 문장을 글자 하나까지 똑같이 베껴 접시에 내놓음(나쁜 접시). 오른쪽엔 보통처럼 새로 짓는 좋은 접시가 비교로 놓임", "The chef copies a recipe-book line letter for letter onto a dish (marked bad); beside it, for comparison, sits a normal dish freshly made"),
         "caption": ("메모리제이션은 새로 요리하는 대신, 레시피북 한 줄을 그대로 베껴 내놓는 버릇이에요.", "Memorization is the habit of serving a line straight out of the recipe book instead of cooking something new."),
         "small": ("일부러 거짓말하는 게 아니에요. 그 한 줄을 정말로 '정답'이라고 믿고 그대로 내놓는 거예요.", "It isn't lying on purpose. It genuinely believes that line is the right answer, and serves it exactly as remembered."),
         "tricks": (4, [
             (DEDUPE_I, ("같은 문장은 미리 걸러내기", "Remove duplicate lines beforehand"), ("레시피북에 반복이 덜 남게 해요", "leaves fewer repeats in the recipe book"), "calm"),
             (MATCH_I, ("나가기 전에 똑같은지 검사", "Check for an exact match before it leaves"), ("레시피북과 너무 같으면 걸러요", "catches it if it's too close to the book"), "calm"),
             (SECRET_I, ("비밀 재료는 처음부터 안 쓰기", "Never use the secret ingredient at all"), ("애초에 외울 게 없게 해요", "leaves nothing there to memorize"), "warm"),
             (AUDIT_I, ("표시된 문장으로 미리 떠보기", "Probe it with marked test lines first"), ("출시 전에 그대로 나오는지 확인해요", "checks before release whether it recites verbatim"), "warm"),
         ])},
        {"svg": P4, "alt": ("규칙판: 기억해서 그대로(레시피북과 100% 일치, 들킴) vs 이해해서 새로(매번 다르게). 오른쪽에 두 결과 예시", "A rules board: memorized verbatim (a 100% match, and it shows) vs understood and new (different each time); two example results sit beside it"),
         "caption": ("완전히 똑같은 문장이 나온다면, 그건 새로 지은 게 아니라 베낀 거예요.", "If the exact same sentence comes out, that isn't something new — it's copied."),
         "small": ("짧고 희귀한데 자주 반복된 문장일수록 위험해요. 전화번호, 비밀번호, 고유한 문단이 특히 그래요.", "Short, rare, often-repeated lines are the riskiest — phone numbers, passwords, and unique paragraphs especially.")},
        {"svg": P5, "alt": ("왼쪽: AI 프라이버시는 '명부를 통째로 주면 어떻게 될까'라는 정책 질문. 오른쪽: 메모리제이션은 외운 걸 그대로 뱉어내는 기술적 현상이라는 설명", "Left: AI privacy asks the policy question what happens if we hand over the whole list; right: memorization is the technical phenomenon of blurting out what it memorized"),
         "caption": ("정책은 '왜 조심해야 하는가', 메모리제이션은 '실제로 어떻게 새는가'예요.", "The policy asks why to be careful — memorization is how it actually leaks."),
         "small": ('<a href="aiprivacy-ko.html">AI 프라이버시</a>는 명부를 통째로 줬을 때의 위험 전반을 다뤄요. 메모리제이션은 그 위험이 실제로 일어나는 구체적인 방식 중 하나이고, <a href="modelinversion-ko.html">모델 인버전</a>과 <a href="membershipinference-ko.html">멤버십 추론</a> 둘 다 뭔가 외워져 있어야 통하는 공격이에요. 사람 주방장은 이거 베낀 건데? 를 알아채지만, 이 주방장은 외운 문장도 정답이라고 믿어요.',
                   '<a href="aiprivacy-en.html">AI privacy</a> covers the overall risk of handing over a whole list. Memorization is one concrete way that risk actually plays out — and both <a href="modelinversion-en.html">model inversion</a> and <a href="membershipinference-en.html">membership inference</a> only work because something got memorized in the first place. A human chef would notice "wait, isn\'t this copied?" — this one believes the memorized line really is the right answer.')},
    ],
    "summary": (("<b>메모리제이션</b> = 주방장이 <b>이해해서 새로 요리하는 대신</b>, 레시피북 한 줄을 <b>글자 하나까지 그대로 베껴</b> 접시에 내놓는 버릇. 짧고 희귀한데 자주 반복된 문장일수록 이렇게 새어 나오기 쉬워요.",
                 "<b>Memorization</b> = the chef's habit of serving a recipe-book line <b>letter for letter</b> instead of <b>understanding and cooking something new</b>. Short, rare, often-repeated lines are the ones most likely to leak out this way."),
                ("Memorization. LLM이 학습 데이터의 일부를 요약·일반화하지 않고 거의 그대로(verbatim) 출력에 재현하는 현상이에요. 모델 크기가 클수록, 같은 문장이 학습 데이터에 자주 반복될수록, 그 문장이 희귀할수록 메모리제이션이 잘 일어나요. 탐지는 알려진 학습 문장을 일부 입력해 정확히 이어지는지 보는 방식(추출 공격 시험)이고, 방어는 중복 제거, 출력 단계의 유사도 검사, 민감 데이터의 학습 배제예요. 모델 인버전과 멤버십 추론은 모두 메모리제이션을 전제로 작동해요.",
                 "The phenomenon of an LLM reproducing part of its training data nearly verbatim in its output, instead of summarizing or generalizing it. Memorization grows more likely with larger models, data that repeats the same line often, and lines that are rare. Detection works by feeding in a prefix of a known training line and checking whether it continues it exactly (an extraction-attack test); defenses include deduplication, output-side similarity checks, and excluding sensitive data from training. Both model inversion and membership inference depend on memorization happening in the first place.")),
    "glossary": [
        ("메모리제이션", "Memorization", ("레시피북 한 줄을 그대로 베껴 내놓는 버릇.", "The habit of serving a line straight out of the recipe book."), ("새로 짓는 게 아니라 그대로 베끼는 거예요.", "Not cooking something new — just copying it exactly.")),
        ("모델 인버전", "Model Inversion", ("접시만 보고 원래 재료를 거꾸로 그려내는 공격.", "An attack that sketches the original ingredients backward from the dishes."), ('잘 외울수록 거꾸로 그리기도 쉬워져요. → <a href="modelinversion-ko.html">접시 더미에서 되살린 얼굴</a>', 'The better it memorizes, the easier it is to invert. → <a href="modelinversion-en.html">a face rebuilt from a pile of dishes</a>')),
        ("멤버십 추론", "Membership Inference", ("이 손님이 연습 때 왔었는지만 알아내는 공격.", "An attack that finds out only whether a guest was part of practice."), ('눈 감고도 척척인 반응도 메모리제이션의 흔적이에요. → <a href="membershipinference-ko.html">눈 감고도 만드는 요리</a>', 'That eyes-closed, instant reaction is itself a trace of memorization. → <a href="membershipinference-en.html">the dish made with eyes closed</a>')),
        ("AI 프라이버시", "AI Privacy", ("명부를 통째로 주면 어떻게 될까 하는 정책의 문제.", "The policy-level question of what happens when you hand over the whole list."), ('메모리제이션은 그 위험이 실제로 일어나는 방식이에요. → <a href="aiprivacy-ko.html">앵무새에게 준 비밀 콩</a>', 'Memorization is how that risk actually happens. → <a href="aiprivacy-en.html">the secret beans we gave the parrot</a>')),
        ("할루시네이션", "Hallucination", ("모르는데 자신 있게 지어내는 버릇.", "Confidently making things up when it doesn't know."), ('같은 뿌리의 다른 얼굴이에요 — 지어내는 대신 이번엔 그대로 베껴요. → <a href="hallucination-ko.html">할루시네이션이 뭐예요?</a>', 'Same root, a different face — instead of making things up, this time it copies exactly. → <a href="hallucination-en.html">What is a Hallucination?</a>')),
        ("파인튜닝", "Fine-tuning", ("짧은 특훈.", "The short drill."), ('좁고 반복적인 자료로 특훈할수록 메모리제이션이 잘 일어나요. → <a href="finetune-ko.html">짧은 특훈</a>', 'The narrower and more repetitive the drill data, the more memorization happens. → <a href="finetune-en.html">the short drill</a>')),
        ("레드팀", "Red Team", ("표시된 문장으로 미리 떠보는 사람들.", "The people who probe it with marked test lines first."), ('출시 전에 그대로 베껴 나오는 문장이 있는지 확인해요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', 'They check before release whether anything comes out verbatim. → <a href="redteam-en.html">the security world\'s red team</a>')),
        ("데이터 중복 제거", "Deduplication", ("똑같은 문장을 레시피북에 여러 번 안 넣기.", "Not putting the same line into the recipe book over and over."), ("반복이 줄면, 통째로 외워질 위험도 줄어요.", "Fewer repeats mean less risk of anything getting memorized whole.")),
    ],
}
