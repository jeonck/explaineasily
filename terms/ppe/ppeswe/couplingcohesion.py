from _draw import *
from _world import *

# 1. 2장을 고쳤는데 5장, 7장까지 다 다시 써야 함
P1 = svg(300, sky(300)
         + person(200, 120, s=0.9, face=SWEAT, **WRITER)
         + manuscript(360, 120, 0.8, text="⟦2장|ch.2⟧") + manuscript(480, 150, 0.8, text="⟦5장|ch.5⟧") + manuscript(600, 120, 0.8, text="⟦7장|ch.7⟧")
         + '<path d="M392 120 L448 150" stroke="var(--bad)" stroke-width="2.5"/><path d="M392 128 L568 128" stroke="var(--bad)" stroke-width="2.5"/>'
         + label(380, 265, "⟦2장을 고쳤는데 5장, 7장까지 다 다시 써야 해요|fixing ch.2 forces a rewrite of ch.5 and ch.7 too⟧", 13, "var(--ink)"))

# 2. 한 챕터 안이 서로 안 맞는 얘기로 뒤섞임
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(380, 140, 1.4)
         + label(380, 60, "⟦한 챕터 안에 요리법, 역사, 시가 다 뒤섞여 있어요|one chapter mixes a recipe, a history lesson, and a poem⟧", 13, "var(--bad)")
         + label(380, 250, "⟦독자는 이 챕터가 뭘 말하려는 건지 헷갈려요|readers can't tell what the chapter is even about⟧", 12, "var(--ink)", cls="d"))

# 3. 챕터끼리는 느슨하게, 챕터 안은 하나로 (hero)
P3 = svg(340, sky(340)
         + manuscript(260, 150, 0.9, text="⟦지도 보는 법만|only \"reading maps\"⟧")
         + manuscript(500, 150, 0.9, text="⟦환전 안내만|only \"currency guide\"⟧")
         + '<path d="M296 150 L464 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4"/>'
         + label(380, 30, "⟦챕터끼리는 느슨하게(낮은 결합도), 챕터 안은 한 주제로(높은 응집도)|loose between chapters (low coupling), unified within each one (high cohesion)⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦목차 정도로만 이어지고, 서로의 속사정은 몰라도 돼요|linked only by the table of contents — neither needs to know the other's details⟧", 12, "var(--muted)"))

BOUND_I = icon('<rect x="10" y="14" width="18" height="36" rx="3" fill="var(--good)"/><rect x="36" y="14" width="18" height="36" rx="3" fill="var(--accent)"/>')
REFMIN_I = icon('<path d="M16 32 h32" stroke="var(--muted)" stroke-width="3" stroke-dasharray="5 4"/><circle cx="16" cy="32" r="7" fill="var(--good)"/><circle cx="48" cy="32" r="7" fill="var(--accent)"/>')
ONETOPIC_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="24" cy="24" r="4" fill="var(--good)"/><circle cx="34" cy="24" r="4" fill="var(--good)"/><circle cx="24" cy="38" r="4" fill="var(--good)"/><circle cx="34" cy="38" r="4" fill="var(--good)"/>')
INTERFACE_I = icon('<rect x="8" y="22" width="20" height="20" rx="3" fill="#4A5A72"/><rect x="36" y="22" width="20" height="20" rx="3" fill="#4A5A72"/><path d="M28 32 h8" stroke="var(--accent)" stroke-width="4"/>')


def chapter_box(x, y, w=70, h=50, dots=("var(--good)",) * 3):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/>'
    cx = [x + w * 0.3, x + w * 0.5, x + w * 0.7]
    for i, c in enumerate(dots):
        out += f'<circle cx="{cx[i]}" cy="{y + h / 2}" r="5" fill="{c}"/>'
    return out


BAD_CENTERS = {"A": (105, 95), "B": (225, 95), "C": (105, 195), "D": (225, 195)}
bad_lines = "".join(
    f'<line x1="{BAD_CENTERS[a][0]}" y1="{BAD_CENTERS[a][1]}" x2="{BAD_CENTERS[b][0]}" y2="{BAD_CENTERS[b][1]}" stroke="var(--bad)" stroke-width="2"/>'
    for a, b in (("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D"))
)
bad_boxes = (
    chapter_box(70, 70, dots=("var(--good)", "var(--bad)", "var(--accent)"))
    + chapter_box(190, 70, dots=("var(--bad)", "var(--accent)", "var(--good)"))
    + chapter_box(70, 170, dots=("var(--accent)", "var(--good)", "var(--bad)"))
    + chapter_box(190, 170, dots=("var(--good)", "var(--bad)", "var(--accent)"))
)

good_lines = (
    '<line x1="450" y1="145" x2="530" y2="145" stroke="var(--muted)" stroke-width="2"/>'
    '<line x1="530" y1="145" x2="610" y2="145" stroke="var(--muted)" stroke-width="2"/>'
    '<line x1="610" y1="145" x2="690" y2="145" stroke="var(--muted)" stroke-width="2"/>'
)
good_boxes = (
    chapter_box(420, 120, 60, 50, dots=("var(--good)", "var(--good)", "var(--good)"))
    + chapter_box(500, 120, 60, 50, dots=("var(--accent)", "var(--accent)", "var(--accent)"))
    + chapter_box(580, 120, 60, 50, dots=("var(--good)", "var(--good)", "var(--good)"))
    + chapter_box(660, 120, 60, 50, dots=("var(--accent)", "var(--accent)", "var(--accent)"))
)

P4 = svg(320, sky(320, ground=False)
         + label(170, 40, "⟦나쁜 예: 높은 결합도, 낮은 응집도|bad: high coupling, low cohesion⟧", 12, "var(--bad)")
         + bad_lines + bad_boxes
         + label(555, 40, "⟦좋은 예: 낮은 결합도, 높은 응집도|good: low coupling, high cohesion⟧", 12, "var(--good)")
         + good_lines + good_boxes
         + label(380, 290, "⟦선이 적을수록 결합도가 낮고, 점 색이 하나일수록 응집도가 높아요|fewer lines means lower coupling; one dot color per box means higher cohesion⟧", 12, "var(--ink)"))

# 5. 극단은 비현실적
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + manuscript(190, 150, 0.9) + label(190, 230, "⟦결합도 0은 비현실적이에요|zero coupling isn't realistic⟧", 11, "var(--ink)")
         + manuscript(570, 150, 0.9) + label(570, 230, "⟦목차·각주 정도는 서로 참조해요|a table of contents or footnote still cross-refers⟧", 11, "var(--ink)")
         + label(380, 270, "⟦목표는 0이 아니라 \"딱 필요한 만큼만\"이에요|the goal isn't zero — it's \"just enough, no more\"⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "couplingcohesion", "order": 40,
    "title": ("챕터가 서로 얼마나 엮여있나", "How Tangled the Chapters Are"),
    "h1": ("<em>결합도와 응집도</em>가 뭐예요?", "What are <em>Coupling and Cohesion</em>?"),
    "sub": ("챕터끼리 서로 얽혀있는 정도와, 챕터 안이 한 주제로 뭉쳐있는 정도를 함께 보는 이야기예요.",
            "A story about how tangled chapters are with each other, and how unified each chapter is inside."),
    "panels": [
        {"svg": P1, "alt": ("작가가 2장을 고쳤는데 서로 얽힌 5장과 7장까지 다시 써야 해 진땀을 흘림", "The author fixes chapter 2 but, because it's tangled with chapters 5 and 7, has to rewrite those too, breaking a sweat"),
         "caption": ("2장을 고쳤는데 5장, 7장까지 다 다시 써야 해요.", "Fixing chapter 2 forces a rewrite of chapters 5 and 7 too."),
         "small": ("챕터끼리 서로 너무 얽혀 있으면 생기는 일이에요.", "This happens when chapters are too entangled with each other.")},
        {"svg": P2, "alt": ("한 챕터 안에 요리법, 역사, 시가 전혀 상관없이 뒤섞여 있음", "One chapter mixes a recipe, a history lesson, and a poem with no real connection"),
         "caption": ("한 챕터 안에 서로 안 맞는 얘기가 뒤섞여 있어요.", "Unrelated topics are mixed together inside one chapter."),
         "small": ("독자는 이 챕터가 뭘 말하려는 건지 헷갈려요.", "Readers can't tell what the chapter is even about.")},
        {"svg": P3, "hero": True, "alt": ("두 챕터가 점선(목차)으로만 느슨하게 이어지고, 각 챕터는 한 가지 주제만 담음", "Two chapters are loosely linked only by a dashed line (table of contents), and each chapter holds just one topic"),
         "caption": ("챕터끼리는 느슨하게, 챕터 안은 한 주제로 뭉치게 해요.", "Keep chapters loosely linked to each other, but unified within."),
         "small": ("목차 정도로만 이어지고, 서로의 속사정은 몰라도 돼요.", "Linked only by the table of contents — neither needs to know the other's details."),
         "tricks": (4, [
             (BOUND_I, ("챕터 경계 분명히", "Clear chapter boundaries"), ("어디까지가 이 챕터인지 또렷하게", "clear on where each chapter begins and ends"), "calm"),
             (REFMIN_I, ("참조 최소화", "Minimize cross-references"), ("다른 챕터는 꼭 필요할 때만", "reach into another chapter only when truly needed")),
             (ONETOPIC_I, ("한 챕터 = 한 주제", "One chapter, one topic"), ("안은 하나의 색으로 통일", "unified in a single color inside"), "warm"),
             (INTERFACE_I, ("필요한 것만 노출", "Expose only what's needed"), ("속사정은 감추고 입구만 보여줘요", "hide the details, show only the entry point")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 챕터 네 개가 서로 전부 선으로 얽혀있고 안에 색이 뒤섞임(높은 결합도·낮은 응집도). 오른쪽: 챕터가 순서대로만 이어지고 안은 한 색(낮은 결합도·높은 응집도)", "Left: four chapters all cross-linked with mixed colors inside (high coupling, low cohesion). Right: chapters linked only in sequence, each a single color inside (low coupling, high cohesion)"),
         "caption": ("그림으로 보면 차이가 분명해요.", "Drawn out, the difference is obvious."),
         "small": ("선이 적을수록 결합도가 낮고, 점 색이 하나일수록 응집도가 높아요.", "Fewer lines mean lower coupling; one dot color per box means higher cohesion.")},
        {"svg": P5, "alt": ("왼쪽: 결합도 0은 비현실적임. 오른쪽: 목차나 각주 정도의 참조는 자연스러움", "Left: zero coupling isn't realistic. Right: a reference like a table of contents or footnote is natural"),
         "caption": ("결합도 0, 응집도 100%는 비현실적이에요.", "Zero coupling and perfect cohesion aren't realistic."),
         "small": ("목표는 0이 아니라 \"딱 필요한 만큼만\"이에요.", "The goal isn't zero — it's \"just enough, no more.\"")},
    ],
    "summary": (("<b>결합도</b>는 챕터(모듈)끼리 <b>서로 얼마나 얽혀있는지</b>, <b>응집도</b>는 한 챕터 안이 <b>얼마나 하나의 주제로 뭉쳐있는지</b>를 재는 잣대예요. 좋은 설계는 결합도는 낮게, 응집도는 높게 가요.",
                 "<b>Coupling</b> measures how tangled chapters (modules) are with each other; <b>cohesion</b> measures how unified a single chapter is inside. Good design aims for low coupling and high cohesion."),
                ("결합도(Coupling)는 모듈 간 상호의존 정도를 뜻하며 낮을수록 한 모듈의 변경이 다른 모듈에 영향을 덜 미쳐요. 응집도(Cohesion)는 한 모듈 안의 요소들이 하나의 책임에 얼마나 집중되어 있는지를 뜻하며 높을수록 이해하고 재사용하기 쉬워요. 좋은 소프트웨어 설계의 기본 원칙은 저결합·고응집이에요.",
                 "Coupling is the degree of interdependence between modules — the lower it is, the less a change in one module ripples into others. Cohesion is how focused the elements inside one module are on a single responsibility — the higher it is, the easier the module is to understand and reuse. Low coupling and high cohesion is a foundational principle of good software design.")),
    "glossary": [
        ("결합도", "Coupling", ("챕터끼리 서로 얼마나 얽혀있나.", "How entangled chapters are with each other."), ("낮을수록 고치기 쉬워요.", "Lower is easier to change.")),
        ("응집도", "Cohesion", ("챕터 안이 한 주제로 뭉쳐있나.", "How unified a chapter is around one topic."), ("높을수록 이해하기 쉬워요.", "Higher is easier to understand.")),
        ("모듈화", "Modularity", ("책을 챕터 단위로 나누는 것 자체.", "The act of splitting a book into chapters at all."), ("결합도·응집도를 따지는 전제가 돼요.", "The premise that makes coupling and cohesion meaningful.")),
        ("인터페이스", "Interface", ("챕터의 \'입구\' — 목차나 제목.", "A chapter's \"entrance\" — its title or table-of-contents entry."), ("속사정을 감추고 이것만 보여줘요.", "Hides the details, exposes only this.")),
        ("정보 은닉", "Information Hiding", ("필요한 것만 보여주고 나머지는 감추는 원칙.", "The principle of showing only what's needed and hiding the rest."), ("결합도를 낮추는 실제 기법이에요.", "A concrete technique for lowering coupling.")),
        ("제품계열 방법론", "Product Line Engineering", ("공통 자산이 잘 나뉘어야 재사용이 쉬워요.", "Core assets need to be split well for reuse to work."), ('핵심 자산 설계에 바로 쓰여요. → <a href="productline-ko.html">같은 틀, 다른 표지</a>', 'Directly used when designing core assets. → <a href="productline-en.html">same template, different covers</a>')),
        ("좋은 소프트웨어의 조건", "Conditions of Good Software", ("유지보수성과 가장 직결돼요.", "Most directly tied to maintainability."), ('이 조건들 중 하나를 떠받치는 원리예요. → <a href="goodsw-ko.html">좋은 책의 조건</a>', 'The principle underpinning one of those conditions. → <a href="goodsw-en.html">what makes a good book</a>')),
        ("디자인 패턴", "Design Pattern", ("저결합·고응집을 실현하는 정해진 해법.", "A ready-made solution for achieving low coupling and high cohesion."), ("스타일가이드에 자주 올라오는 항목이에요.", "A frequent entry in the style guide.")),
    ],
}
