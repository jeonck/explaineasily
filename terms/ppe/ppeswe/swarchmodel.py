from _draw import *
from _world import *


def bigbook(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-50" width="80" height="100" rx="3" fill="#8B5E3C"/>'
            f'<rect x="-32" y="-42" width="64" height="84" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-20 -24 h40 M-20 -10 h40 M-20 4 h40 M-20 18 h40" stroke="#142033" stroke-width="2"/></g>')


def layer_stack(x, y, w=200, rows=3, labels=None):
    out = ""
    colors = ["#D8D2C2", "#C9A86A", "#8B5E3C"]
    for i in range(rows):
        yy = y + i * 34
        out += f'<rect x="{x}" y="{yy}" width="{w}" height="28" rx="3" fill="{colors[i % 3]}"/>'
        if labels:
            out += label(x + w / 2, yy + 19, labels[i], 11, "#142033", cls="d")
    return out


def pipe_chain(x, y, n=4, labels=None):
    out = ""
    step = 150
    for i in range(n):
        xx = x + i * step
        out += f'<rect x="{xx}" y="{y}" width="110" height="44" rx="6" fill="#4A5A72"/>'
        if labels:
            out += label(xx + 55, y + 27, labels[i], 10, "#FFF8E7", cls="d")
        if i < n - 1:
            out += f'<path d="M{xx + 110} {y + 22} h30" stroke="var(--accent)" stroke-width="4" marker-end="url(#swarrow)"/>'
    return out


ARROWHEAD = '<defs><marker id="swarrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker></defs>'

# 1. 책이 너무 커져서 다루기 무서워요
P1 = svg(300, sky(300)
         + bigbook(380, 160, 1.3)
         + person(180, 190, s=0.75, face=SWEAT + EYES, **EDITOR)
         + person(580, 190, s=0.75, face=SWEAT + EYES, **WRITER)
         + label(380, 50, "⟦한 권에 다 몰아넣었더니 너무 커졌어요|crammed into one volume — now it's huge⟧", 13, "var(--ink)")
         + label(380, 280, "⟦한 글자 고치기도 무서워요|even fixing one word feels scary⟧", 12, "var(--bad)"))

# 2. 한 군데 고치려면 전체를 다시 찍어야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + bigbook(380, 150, 1.2)
         + '<path d="M300 150 l-40 -10 M300 150 l-40 10" stroke="var(--bad)" stroke-width="3"/>'
         + label(380, 40, "⟦한 쪽만 고쳐도 책 전체를 다시 인쇄해요|fix one page, and the whole book gets reprinted⟧", 12, "var(--ink)")
         + label(380, 250, "⟦느리고 위험해요|slow, and risky⟧", 13, "var(--bad)")
         + label(380, 280, "⟦미리 어떤 모양으로 짤지 정해뒀어야 했어요|the shape should have been decided ahead of time⟧", 12, "var(--muted)"))

# 3. 소프트웨어 아키텍처 모델 = 책 전체의 미리 정한 구조 밑그림 (hero)
P3 = svg(340, sky(340)
         + layer_stack(290, 70, 180, 3, ["⟦서문|preface⟧", "⟦본문|body⟧", "⟦부록|appendix⟧"])
         + person(560, 130, s=0.8, face=EYES, **EDITOR)
         + label(380, 25, "⟦아키텍처 모델 = 책 전체를 어떤 모양으로 짤지 미리 정하는 밑그림|an architecture model = the blueprint, decided ahead of time, for how the whole book is shaped⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦모양에 따라 고치기 쉬움과 배포 속도가 달라져요|the shape decides how easy it is to fix, and how fast it ships⟧", 11, "var(--muted)"))

LAYER_I = icon('<rect x="12" y="10" width="40" height="12" rx="2" fill="var(--good)"/><rect x="12" y="26" width="40" height="12" rx="2" fill="var(--accent)"/><rect x="12" y="42" width="40" height="12" rx="2" fill="#8B5E3C"/>')
PIPE_I = icon('<rect x="6" y="24" width="14" height="16" rx="2" fill="var(--good)"/><rect x="25" y="24" width="14" height="16" rx="2" fill="var(--accent)"/><rect x="44" y="24" width="14" height="16" rx="2" fill="#8B5E3C"/><path d="M20 32 h5 M39 32 h5" stroke="var(--muted)" stroke-width="3"/>')
CLIENTSRV_I = icon('<rect x="8" y="16" width="20" height="18" rx="3" fill="var(--good)"/><rect x="36" y="16" width="20" height="18" rx="3" fill="#4A5A72"/><path d="M28 25 h8" stroke="var(--accent)" stroke-width="4" marker-end="url(#swarrow2)"/><defs><marker id="swarrow2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker></defs>')
MICRO_I = icon('<circle cx="18" cy="20" r="9" fill="var(--good)"/><circle cx="46" cy="20" r="9" fill="var(--accent)"/><circle cx="32" cy="42" r="9" fill="#8B5E3C"/>')

# 4. 한 덩어리 vs 쪼갠 구조
P4 = svg(340, '<rect width="380" height="340" fill="var(--accent-soft)"/><rect x="380" width="380" height="340" fill="var(--good-soft)"/>'
         + ARROWHEAD
         + bigbook(190, 110, 1.0)
         + label(190, 190, "⟦한 덩어리|one big volume⟧", 13, "var(--ink)", cls="d")
         + label(190, 230, "⟦한 곳 고치면 전부 다시 찍어요|fix one spot, reprint it all⟧", 11, "var(--ink)")
         + '<rect x="530" y="70" width="46" height="46" rx="4" fill="var(--good)"/><rect x="600" y="70" width="46" height="46" rx="4" fill="var(--accent)"/><rect x="565" y="140" width="46" height="46" rx="4" fill="#8B5E3C"/>'
         + label(570, 230, "⟦동물편·역사편·과학편으로 쪼갰어요|split into animal, history, and science volumes⟧", 13, "var(--ink)", cls="d")
         + label(570, 270, "⟦한 편만 따로 고쳐 다시 내도 돼요|one volume can be reworked and reissued alone⟧", 11, "var(--ink)")
         + label(380, 320, "⟦정답은 하나가 아니라, 책 성격에 맞는 모양을 골라요|there's no single right answer — the shape fits the book⟧", 12, "var(--ink)", cls="d"))

# 5. 어떤 구조든, 결국 책은 독자 손에 가 닿아요 (마무리)
P5 = svg(320, sky(320)
         + person(170, 190, s=0.65, face=SMILE, **EDITOR)
         + person(280, 190, s=0.65, face=SMILE, **WRITER)
         + person(390, 190, s=0.65, face=SMILE, **PROOFER)
         + person(500, 190, s=0.65, face=SMILE, **PRINTER)
         + person(630, 170, s=0.7, face=SMILE, **READER) + manuscript(630, 250, 0.6)
         + bookshelf(60, 190, 0.55, 4)
         + label(380, 30, "⟦원고에서 독자 손까지, 이 출판사 이야기는 여기서 마침표를 찍어요|from manuscript to the reader's hands — this publishing house's story ends here, for now⟧", 13, "var(--ink)", cls="d")
         + label(380, 300, "⟦어떤 구조를 고르든, 결국 책은 독자에게 가 닿아야 해요|whatever shape you choose, the book still has to reach the reader⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "swarchmodel", "order": 47,
    "title": ("책 전체를 미리 짜 두는 구조 밑그림", "The Blueprint That Shapes the Whole Book Ahead of Time"),
    "h1": ("<em>소프트웨어 아키텍처 모델</em>이 뭐예요?", "What is a <em>Software Architecture Model</em>?"),
    "sub": ("소프트웨어 아키텍처 모델을, 책 한 권을 어떤 모양으로 미리 짜 둘지 정하는 출판사의 마지막 이야기로 풀어봤어요.",
            "Software architecture models, told as the publishing house's closing story about deciding, ahead of time, what shape a book should take."),
    "panels": [
        {"svg": P1, "alt": ("책이 너무 커져서 편집장과 작가가 다루기 무서워함", "The book has grown so large that the editor and writer are afraid to touch it"),
         "caption": ("한 권에 다 몰아넣었더니 너무 커졌어요.", "Crammed into one volume, it's grown huge."),
         "small": ("한 글자 고치기도 무서워요.", "Even fixing one word feels scary.")},
        {"svg": P2, "alt": ("한 쪽만 고쳐도 책 전체를 다시 찍어야 하는 상황", "Fixing just one page still means reprinting the whole book"),
         "caption": ("한 군데 고치려면 책 전체를 다시 찍어야 해요.", "Fix one spot, and the whole book gets reprinted."),
         "small": ("느리고 위험해요 — 미리 모양을 정해뒀어야 했어요.", "Slow and risky — the shape should have been decided ahead of time.")},
        {"svg": P3, "hero": True, "alt": ("서문·본문·부록이 층층이 쌓인 책의 구조를 편집장이 바라봄", "The editor looks over a book structured in layers — preface, body, appendix"),
         "caption": ("아키텍처 모델은 책 전체를 어떤 모양으로 짤지 미리 정하는 밑그림이에요.", "An architecture model is the blueprint, decided ahead of time, for how the whole book is shaped."),
         "small": ("모양에 따라 고치기 쉬움과 배포 속도가 달라져요.", "The shape decides how easy it is to fix, and how fast it ships."),
         "tricks": (4, [
             (LAYER_I, ("층층이 쌓기(레이어드)", "Layered"), ("서문-본문-부록처럼, 바로 아래 층만 불러요", "like preface-body-appendix, each calls only the layer below"), "calm"),
             (PIPE_I, ("한 줄로 흘려보내기(파이프-필터)", "Pipe-Filter"), ("교정→편집→조판 순서로 다듬어요", "proof, edit, typeset, in one flowing line")),
             (CLIENTSRV_I, ("주문하면 받기(클라이언트-서버)", "Client-Server"), ("서점이 창고에 주문하면 책을 받아요", "the bookstore orders, the warehouse delivers"), "warm"),
             (MICRO_I, ("따로따로 출간(마이크로서비스)", "Microservices"), ("동물·역사·과학편을 따로 고쳐 내요", "animal, history, science — each revised and released on its own")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 한 덩어리 책은 한 곳만 고쳐도 전부 다시 찍음. 오른쪽: 쪼갠 책은 한 편만 따로 고쳐 냄", "Left: a single-volume book must be fully reprinted for one fix. Right: a split book can revise just one volume"),
         "caption": ("한 덩어리냐 쪼갠 구조냐에 따라 고치는 범위가 달라요.", "Whether it's one volume or split, the scope of a fix differs."),
         "small": ("정답은 하나가 아니라, 책 성격에 맞는 모양을 골라요.", "There's no single right answer — the shape should fit the book.")},
        {"svg": P5, "alt": ("편집장·작가·교정자·인쇄 감독·독자가 서가 앞에 함께 서 있음", "The editor, writer, proofreader, print supervisor, and reader all stand together by the shelf"),
         "caption": ("원고에서 독자 손까지, 이 출판사 이야기는 여기서 마침표를 찍어요.", "From manuscript to the reader's hands — this publishing house's story ends here, for now."),
         "small": ("어떤 구조를 고르든, 결국 책은 독자에게 가 닿아야 해요.", "Whatever shape you choose, the book still has to reach the reader.")},
    ],
    "summary": (("<b>소프트웨어 아키텍처 모델</b> = 시스템 전체를 <b>어떤 모양으로 짤지</b> 미리 정해 두는 <b>구조 밑그림</b>.",
                 "A <b>software architecture model</b> is the <b>structural blueprint</b> that decides, ahead of time, <b>what shape</b> a whole system will take."),
                ("소프트웨어 아키텍처는 시스템을 구성 요소와 그 관계로 미리 설계한 큰 구조이고, 레이어드·파이프-필터·클라이언트-서버·마이크로서비스·이벤트 기반 등 여러 모델(스타일)이 있어요. 디자인패턴이 반복되는 작은 문제의 해법이라면, 아키텍처는 시스템 전체의 밑그림이라 더 큰 단위예요. 어떤 모델을 고르느냐에 따라 유지보수·확장·배포 방식이 달라져요.",
                 "Software architecture is the large-scale structure of a system — its components and how they relate — designed ahead of time. Models (styles) include layered, pipe-filter, client-server, microservices, and event-driven. While a design pattern solves a small, recurring problem, an architecture is the blueprint for the whole system — a much larger unit. The chosen model shapes how the system is maintained, scaled, and deployed.")),
    "glossary": [
        ("소프트웨어 아키텍처", "Software Architecture", ("시스템 전체를 미리 짜 두는 구조 밑그림.", "The structural blueprint laid out for a whole system, ahead of time."), ("구성 요소와 그 관계를 정해요.", "It fixes the components and how they relate.")),
        ("레이어드 아키텍처", "Layered Architecture", ("서문-본문-부록처럼 층층이 쌓은 구조.", "A structure stacked in layers, like preface-body-appendix."), ("바로 아래 층만 불러요.", "Each layer calls only the one directly below.")),
        ("파이프-필터", "Pipe-Filter", ("교정→편집→조판처럼 한 줄로 흘려보내는 구조.", "A structure that flows in one line, like proof-edit-typeset."), ("각 단계가 필터처럼 다듬어요.", "Each stage refines it, like a filter.")),
        ("클라이언트-서버", "Client-Server", ("서점이 주문하고 창고가 응답하는 구조.", "A structure where the bookstore orders and the warehouse responds."), ("요청하는 쪽과 응답하는 쪽이 나뉘어요.", "The requester and the responder are kept separate.")),
        ("마이크로서비스", "Microservices", ("동물·역사·과학편처럼 따로따로 쪼갠 구조.", "A structure split apart, like separate animal, history, and science volumes."), ('비슷한 구조가 다른 세계에도 있어요. → <a href="servicemesh-ko.html">기구 사이 전용 통로</a>', 'A related structure lives in another world too. → <a href="servicemesh-en.html">the dedicated path between rides</a>')),
        ("이벤트 기반 아키텍처", "Event-Driven Architecture", ("연재 만화처럼, 사건이 생기면 다음 편이 달라지는 구조.", "A structure like a serialized comic — the next issue depends on what just happened."), ("사건(이벤트)이 흐름을 정해요.", "Events decide the flow.")),
        ("디자인패턴", "Design Pattern", ("작은 반복 문제의 해법.", "A solution to one small, recurring problem."), ('→ <a href="diprinciple-ko.html">아무 기계나 꽂을 수 있는 콘센트</a>처럼, 아키텍처보다 작은 단위예요.', 'A smaller unit than architecture — like <a href="diprinciple-en.html">the standard socket any machine can plug into</a>.')),
        ("정보시스템 감리/PMO", "IS Audit / PMO", ("이 구조가 실제로 잘 지켜지고 있는지 바깥에서 점검해요.", "Checks from the outside whether this structure is actually being followed."), ('→ <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', '→ <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
