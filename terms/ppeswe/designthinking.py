from _draw import *
from _world import *


def cycle_arrow(cx, cy, r=70, color="var(--accent)"):
    return (f'<path d="M {cx} {cy - r} A {r} {r} 0 1 1 {cx - r * 0.95:.0f} {cy - r * 0.31:.0f}" '
            f'stroke="{color}" stroke-width="4" fill="none" marker-end="url(#dtarrow)"/>')


ARROWHEAD_DEF = ('<defs><marker id="dtarrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                  '<path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker></defs>')

# 1. 왜 안 팔리는지 편집장은 몰라요
P1 = svg(300, sky(300)
         + person(380, 140, s=0.9, face=FROWN, **EDITOR)
         + bookshelf(540, 180, 0.6, 4)
         + bubble(220, 50, 240, 44, "⟦이 책, 왜 안 팔리지?|why isn't this book selling?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦편집장은 이유를 몰라요|the editor has no idea why⟧", 13, "var(--bad)"))

# 2. 책상에서 혼자 추측만 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 140, s=0.9, face=EYES, **EDITOR)
         + label(380, 70, "⟦독자들이 바쁜가? 표지가 별로인가?|are readers just busy? is the cover bad?⟧", 12, "var(--muted)")
         + label(380, 240, "⟦독자를 직접 만나 본 적은 없어요|but no one has actually met a real reader⟧", 13, "var(--ink)")
         + label(380, 275, "⟦추측은 자주 빗나가요|guesses miss, a lot⟧", 12, "var(--bad)"))

# 3. 디자인씽킹 = 추측 대신 직접 만나 돌고 도는 과정 (hero)
P3 = svg(340, sky(340, ground=False)
         + ARROWHEAD_DEF + cycle_arrow(380, 170, 90)
         + person(380, 80, s=0.75, face=SMILE, **EDITOR)
         + person(260, 230, s=0.6, face=SMILE, **READER)
         + manuscript(500, 230, 0.6)
         + label(380, 25, "⟦디자인씽킹 = 독자를 직접 만나, 묻고 만들고 다시 고치길 반복하는 과정|design thinking = meeting readers directly, and looping through building and reworking⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦책상 추측이 아니라, 돌고 도는 현장 확인이에요|not desk guesses — a loop of checking things in the field⟧", 11, "var(--muted)"))

EMPATHY_I = icon('<circle cx="22" cy="26" r="12" fill="var(--good)"/><circle cx="46" cy="26" r="12" fill="var(--accent)"/><path d="M14 46 q20 -14 36 0" stroke="var(--muted)" stroke-width="3" fill="none" stroke-linecap="round"/>')
DEFINE_I = icon('<circle cx="32" cy="30" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v6 M32 36 h.5" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>')
IDEATE_I = icon('<circle cx="22" cy="20" r="5" fill="var(--good)"/><circle cx="42" cy="16" r="5" fill="var(--accent)"/><circle cx="46" cy="36" r="5" fill="var(--good)"/><circle cx="20" cy="40" r="5" fill="var(--accent)"/><circle cx="32" cy="48" r="5" fill="var(--good)"/>')
PROTOTYPE_I = icon('<rect x="14" y="16" width="36" height="28" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3" stroke-dasharray="4 3"/><path d="M22 26 h20 M22 34 h12" stroke="#142033" stroke-width="2.5"/>')

# 4. 다섯 단계가 돌고 돈다
P4 = svg(340, sky(340, ground=False)
         + ARROWHEAD_DEF + cycle_arrow(380, 170, 120)
         + label(380, 42, "⟦공감|Empathize⟧", 13, "var(--ink)", cls="d")
         + label(510, 110, "⟦정의|Define⟧", 13, "var(--ink)", cls="d")
         + label(510, 230, "⟦아이디어|Ideate⟧", 13, "var(--ink)", cls="d")
         + label(250, 230, "⟦시제품|Prototype⟧", 13, "var(--ink)", cls="d")
         + label(250, 110, "⟦테스트|Test⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 바퀴 돌고 나면, 다시 공감으로 돌아가요|after one loop, it goes back to empathy again⟧", 12, "var(--muted)"))

# 5. 디자인씽킹이 전부를 대신하진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **EDITOR) + label(190, 240, "⟦'뭘 쓸지' 찾는 데 쓰는 방법이에요|a method for finding what to write⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **PRINTER) + inkstamp(570, 220, 0.5)
         + label(570, 260, "⟦그 뒤 일정·품질 관리는 또 다른 몫이에요|schedule and quality after that are a separate job⟧", 11, "var(--ink)")
         + label(380, 282, "⟦무엇을 쓸지 찾는 방법이지, 모든 공정을 대신하진 않아요|it finds what to write — it doesn't replace every other step⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "designthinking", "order": 44,
    "title": ("책상 추측 대신 독자에게 직접 묻기", "Asking the Reader Directly, Instead of Guessing at a Desk"),
    "h1": ("<em>디자인 씽킹</em>이 뭐예요?", "What is <em>Design Thinking</em>?"),
    "sub": ("디자인 씽킹을, 책상에서 추측하는 대신 독자를 직접 만나 돌고 도는 편집장의 이야기로 풀어봤어요.",
            "Design thinking, told as a story about an editor who stops guessing at a desk and loops through meeting readers directly instead."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 안 팔리는 책을 보며 당황함", "An editor frowns, holding a book that isn't selling"),
         "caption": ("이 책, 왜 안 팔리지?", "Why isn't this book selling?"),
         "small": ("편집장은 이유를 몰라요.", "The editor has no idea why.")},
        {"svg": P2, "alt": ("편집장이 책상에 앉아 혼자 이유를 추측함", "The editor sits at a desk, guessing at reasons alone"),
         "caption": ("책상에서 혼자 추측만 해요.", "Guessing alone at a desk."),
         "small": ("독자를 직접 만나 본 적은 없어요. 추측은 자주 빗나가요.", "No one has actually met a real reader — and guesses miss, a lot.")},
        {"svg": P3, "hero": True, "alt": ("편집장과 독자가 만나고, 원고가 고리 모양 화살표로 연결돼 돌고 돎", "An editor meets a reader, with a manuscript linked in a looping arrow"),
         "caption": ("디자인씽킹은 독자를 직접 만나, 묻고 만들고 다시 고치길 반복하는 과정이에요.", "Design thinking means meeting readers directly, and looping through building and reworking."),
         "small": ("책상 추측이 아니라, 돌고 도는 현장 확인이에요.", "Not desk guesses — a loop of checking things in the field."),
         "tricks": (4, [
             (EMPATHY_I, ("공감하기", "Empathize"), ("독자를 직접 만나요", "meet the reader in person"), "calm"),
             (DEFINE_I, ("문제 다시 정의하기", "Define"), ("진짜 헷갈리는 지점을 찾아요", "pin down what's really confusing")),
             (IDEATE_I, ("아이디어 쏟아내기", "Ideate"), ("일단 많이 내봐요", "throw out as many ideas as possible"), "warm"),
             (PROTOTYPE_I, ("싼 시제품으로 먼저 보여주기", "Prototype, then test"), ("독자 반응 보고 다시 고쳐요", "show it, watch the reaction, rework")),
         ])},
        {"svg": P4, "alt": ("공감·정의·아이디어·시제품·테스트 다섯 단계가 원을 그리며 돌아감", "Five stages — empathize, define, ideate, prototype, test — looping in a circle"),
         "caption": ("다섯 단계가 원을 그리며 돌고 돌아요.", "Five stages loop around in a circle."),
         "small": ("한 바퀴 돌고 나면, 다시 공감으로 돌아가요.", "After one loop, it goes back to empathy again.")},
        {"svg": P5, "alt": ("왼쪽: 디자인씽킹은 뭘 쓸지 찾는 방법. 오른쪽: 그 뒤 일정·품질 관리는 별개", "Left: design thinking finds what to write. Right: schedule and quality management afterward is separate"),
         "caption": ("디자인씽킹이 전부를 대신하진 않아요.", "Design thinking doesn't replace everything."),
         "small": ("무엇을 쓸지 찾는 방법이지, 모든 공정을 대신하진 않아요.", "It finds what to write — it doesn't replace every other step.")},
    ],
    "summary": (("<b>디자인 씽킹</b> = 책상 추측 대신 <b>독자를 직접 만나</b>, 공감·정의·아이디어·시제품·테스트를 <b>돌고 도는</b> 문제 해결법.",
                 "<b>Design thinking</b> is a problem-solving method that <b>meets readers directly</b> instead of guessing at a desk, <b>looping</b> through empathize, define, ideate, prototype, and test."),
                ("디자인 씽킹은 사용자(독자) 공감에서 출발해, 문제를 재정의하고, 많은 아이디어를 내고, 값싼 시제품을 만들어, 실제 사용자에게 테스트한 뒤 다시 공감 단계로 돌아가는 사람 중심·반복적 설계 방법론이에요. 결과물을 어떻게 만들지보다, 무엇을 만들어야 하는지를 먼저 찾는 데 집중해요.",
                 "Design thinking is a human-centered, iterative method that starts by empathizing with users, redefines the problem, generates many ideas, builds a cheap prototype, tests it with real users, then loops back to empathy. It focuses on finding what to build before deciding how to build it.")),
    "glossary": [
        ("디자인씽킹", "Design Thinking", ("추측 대신 독자를 직접 만나는 문제 해결법.", "A problem-solving method that meets readers directly instead of guessing."), ("다섯 단계를 돌고 또 돌아요.", "It loops through five stages, again and again.")),
        ("공감(Empathize)", "Empathize", ("독자를 직접 만나는 첫 단계.", "The first stage — meeting the reader in person."), ("책상 추측을 멈추는 지점이에요.", "This is where desk-guessing stops.")),
        ("문제 정의(Define)", "Define", ("진짜 헷갈리는 지점을 다시 짚는 단계.", "The stage of pinning down what's really confusing."), ("'좋은 책'이 아니라 구체적인 문제로 좁혀요.", "It narrows 'a good book' down to one concrete problem.")),
        ("아이디어 발산(Ideate)", "Ideate", ("일단 많이 쏟아내는 단계.", "The stage of throwing out as many ideas as possible."), ("좋고 나쁨은 나중에 걸러요.", "Good or bad gets sorted out later.")),
        ("프로토타입(Prototype)", "Prototype", ("싼값에 빨리 만든 샘플 페이지.", "A cheap, quickly made sample page."), ("완성본이 아니라 확인용이에요.", "It's for checking, not for shipping.")),
        ("요구공학", "Requirements Engineering", ("쓰기 전에 먼저 묻는, 더 체계적인 절차.", "A more systematic process of asking before writing."), ('디자인씽킹의 공감·정의를 더 깊게 파고들어요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', 'It digs deeper into the empathize/define stages. → <a href="reqeng-en.html">the one who asks before writing</a>')),
        ("A/B 테스트", "A/B Test", ("두 안 중 뭐가 더 잘 통하는지 숫자로 재는 시험.", "A test that measures, with numbers, which of two options works better."), ('디자인씽킹의 테스트 단계를 통계적으로 더 깊게 들어가요. → <a href="hypothesistest-ko.html">두 표지 중 뭐가 진짜 더 잘 팔릴까</a>', "It goes deeper into the test stage with statistics. → <a href=\"hypothesistest-en.html\">which cover really sells better</a>")),
        ("사용성평가", "Usability Test", ("시제품을 실제로 써보게 하고 지켜보는 일.", "Having people actually try the prototype and watching them."), ('테스트 단계에서 자주 같이 써요. → <a href="usability-ko.html">독자가 책을 쓱 넘겨보는 시험</a>', 'Often paired with the test stage. → <a href="usability-en.html">the test where a reader just tries the book cold</a>')),
    ],
}
