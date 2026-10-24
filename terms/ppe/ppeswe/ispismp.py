from _draw import *
from _world import *

# 1. 출판사가 "다음에 뭘 낼지" 없이 되는 대로 책을 벌이고 있어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **EDITOR)
         + manuscript(260, 120, 0.7) + manuscript(340, 160, 0.7) + manuscript(430, 110, 0.7) + manuscript(520, 160, 0.7)
         + label(380, 230, "⟦손에 잡히는 대로 책을 벌이기 시작했어요|books get started on whatever's at hand⟧", 12, "var(--bad)")
         + label(380, 280, "⟦뭐가 먼저 나와야 할지 아무도 몰라요|nobody knows what should come out first⟧", 13, "var(--ink)"))

# 2. 베스트셀러만 좇다가, 출판사 전체 방향을 잃어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.85, face=EYES, **EDITOR)
         + bubble(230, 70, 230, 38, "⟦저 장르가 요즘 잘 팔린대요, 그것부터!|that genre is hot right now, let's do that first!⟧", 11, "var(--panel)", "var(--line)", "left")
         + manuscript(560, 190, 0.7)
         + label(380, 280, "⟦유행만 따라가면, 출판사의 진짜 색깔은 안 보여요|chasing trends alone loses the house's own identity⟧", 12, "var(--ink)"))

# 3. ISP/ISMP = 출판 로드맵을 그리는 사람 (hero)
P3 = svg(340, sky(340)
         + styleguide(60, 30, 280, 250, "⟦출판 로드맵|PUBLISHING ROADMAP⟧",
                      ("⟦1년차 — 그림책 시리즈|year 1 — picture-book series⟧",
                       "⟦2년차 — 청소년 소설|year 2 — YA novels⟧",
                       "⟦3년차 — 해외 번역본|year 3 — translated editions⟧"), 1.0)
         + person(500, 150, s=0.9, face=EYES, **EDITOR)
         + label(380, 30, "⟦ISP/ISMP = 무엇을 먼저, 어떤 순서로 낼지 큰 그림부터 그리는 일|ISP/ISMP = drawing the big picture of what to publish, and in what order⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦감리(출간 전 점검)보다 훨씬 앞선, 계획 그 자체예요|it comes long before audit — it's the plan itself⟧", 12, "var(--muted)"))

# 4. 로드맵을 그릴 때 보는 것들
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦로드맵에 담는 것|WHAT GOES IN THE ROADMAP⟧",
                      ("⟦독자층 — 누구에게 팔 것인가|readers — who are we selling to?⟧",
                       "⟦경쟁 출판사 — 남들은 뭘 내나|rivals — what are other houses publishing?⟧",
                       "⟦역량 — 우리 작가진이 뭘 잘하나|capability — what can our writers actually do?⟧",
                       "⟦우선순위 — 뭐부터 낼까|priority — what comes first?⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **EDITOR)
         + label(380, 300, "⟦ISP 는 출판사 전체, ISMP 는 그 로드맵을 더 잘게 쪼갠 실행 계획이에요|ISP covers the whole house; ISMP breaks that roadmap into a finer execution plan⟧", 12, "var(--ink)"))

# 5. 로드맵이 책을 대신 써주진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **EDITOR) + label(190, 258, "⟦어떤 책을 언제 낼지는 정해줘요|it decides which book comes out when⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **WRITER) + manuscript(652, 205, 0.5) + label(570, 272, "⟦써야 하는 건 여전히 작가예요|but the writer still has to write it⟧", 11, "var(--ink)")
         + label(380, 294, "⟦ISP/ISMP는 방향을 정하는 지도고, 원고 한 줄 한 줄은 아니에요|ISP/ISMP is the map, not the manuscript itself⟧", 12, "var(--ink)", cls="d"))

MAP_I = icon('<path d="M12 14 l16 -6 16 6 8 -4 v38 l-8 4 -16 -6 -16 6 -8 -4 z" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><path d="M28 8 v38 M44 14 v38" stroke="#C9822B" stroke-width="2"/>')
READERS_I = icon('<circle cx="24" cy="26" r="9" fill="var(--accent)"/><circle cx="42" cy="26" r="9" fill="var(--accent)"/><path d="M10 52 q14 -16 28 0 M24 52 q14 -16 28 0" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
RIVAL_I = icon('<rect x="14" y="16" width="16" height="36" rx="2" fill="#5A3B22"/><rect x="34" y="10" width="16" height="42" rx="2" fill="#7A5236"/>')
PRIORITY_I = icon('<path d="M18 50 V26 M32 50 V14 M46 50 V34" stroke="var(--good)" stroke-width="6" stroke-linecap="round"/>')

PAGE = {
    "slug": "ispismp", "order": 2,
    "title": ("출판 로드맵을 그리는 사람", "The One Who Maps the Publishing Roadmap"),
    "h1": ("<em>ISP/ISMP</em>가 뭐예요?", "What is <em>ISP/ISMP</em>?"),
    "sub": ("ISP(정보전략계획)와 ISMP(정보시스템 마스터플랜)를, 출판사가 앞으로 뭘 낼지 미리 그려두는 로드맵 이야기로 풀어봤어요.",
            "ISP (information strategy planning) and ISMP (information system master plan), told as a story about mapping out what a publishing house will put out ahead of time."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 어떤 책부터 낼지 몰라 진땀을 흘리며 여러 원고를 늘어놓음", "An editor sweats, surrounded by scattered manuscripts with no idea what to publish first"),
         "caption": ("손에 잡히는 대로 책을 벌이기 시작했어요.", "Books get started on whatever's at hand."),
         "small": ("뭐가 먼저 나와야 할지 아무도 몰라요.", "Nobody knows what should come out first.")},
        {"svg": P2, "alt": ("편집장이 요즘 잘 팔리는 장르만 좇자고 말함", "The editor says to chase whichever genre is selling right now"),
         "caption": ("베스트셀러만 좇다가, 출판사 전체 방향을 잃어요.", "Chasing only bestsellers loses the house's overall direction."),
         "small": ("유행만 따라가면, 출판사의 진짜 색깔은 안 보여요.", "Chasing trends alone loses the house's own identity.")},
        {"svg": P3, "hero": True, "alt": ("편집장이 출판 로드맵 안내판 앞에 서 있음: 1년차 그림책, 2년차 청소년 소설, 3년차 번역본", "An editor stands by a publishing-roadmap board: year 1 picture books, year 2 YA novels, year 3 translations"),
         "caption": ("ISP/ISMP는 무엇을 먼저, 어떤 순서로 낼지 큰 그림부터 그리는 일이에요.", "ISP/ISMP draws the big picture of what to publish, and in what order."),
         "small": ("감리보다 훨씬 앞선, 계획 그 자체예요.", "It comes long before audit — it's the plan itself."),
         "tricks": (4, [
             (MAP_I, ("큰 그림 먼저 그리기", "Draw the big picture first"), ("몇 년치 출판 방향", "years of publishing direction ahead"), "calm"),
             (READERS_I, ("독자층 살피기", "Study the readership"), ("누구에게 팔 것인가", "who we're selling to")),
             (RIVAL_I, ("경쟁 출판사 보기", "Watch rival houses"), ("남들은 뭘 내는지", "what others are publishing"), "warm"),
             (PRIORITY_I, ("순서 정하기", "Set the order"), ("뭐부터 낼지 줄 세워요", "lining up what comes first")),
         ])},
        {"svg": P4, "alt": ("로드맵 안내판: 독자층·경쟁 출판사·역량·우선순위 네 항목", "A roadmap board: readers, rivals, capability, priority"),
         "caption": ("로드맵을 그릴 때 이 네 가지를 봐요.", "The roadmap is drawn by looking at these four things."),
         "small": ("ISP는 출판사 전체, ISMP는 그 로드맵을 더 잘게 쪼갠 실행 계획이에요.", "ISP covers the whole house; ISMP breaks that roadmap into a finer execution plan.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 어떤 책을 언제 낼지 정함. 오른쪽: 결국 쓰는 건 작가", "Left: the editor decides which book comes out when. Right: the writer still has to write it"),
         "caption": ("로드맵이 책을 대신 써주진 않아요.", "The roadmap doesn't write the book for you."),
         "small": ("방향을 정하는 지도고, 원고 한 줄 한 줄은 아니에요.", "It's the map, not the manuscript itself.")},
    ],
    "summary": (("<b>ISP/ISMP</b> = 출판사가 <b>무엇을, 어떤 순서로</b> 낼지 몇 년 앞서 그려두는 <b>큰 그림 로드맵</b>.",
                 "<b>ISP/ISMP</b> = a <b>big-picture roadmap</b> drawn years ahead, deciding <b>what</b> to publish and <b>in what order</b>."),
                ("ISP(Information Strategy Planning)는 조직의 경영 전략에 맞춰 정보화 방향과 우선순위를 수립하는 일이고, ISMP(Information System Master Plan)는 그 전략을 구체적인 시스템 구축 계획으로 세분화한 것이에요. 둘 다 개별 프로젝트가 시작되기 전, 조직 전체 수준에서 그려두는 밑그림이에요.",
                 "ISP (Information Strategy Planning) sets an organization's information direction and priorities in line with its business strategy, while ISMP (Information System Master Plan) breaks that strategy down into a concrete system-build plan. Both are drawn at the whole-organization level, before any individual project begins.")),
    "glossary": [
        ("ISP", "ISP", ("출판사 전체의 방향을 정하는 일.", "Setting the direction for the whole house."), ("경영 전략에 맞춰 정보화 우선순위를 짜요.", "Lines up IT priorities with business strategy.")),
        ("ISMP", "ISMP", ("로드맵을 더 잘게 쪼갠 실행 계획.", "The roadmap broken into a finer execution plan."), ("ISP 다음 단계예요.", "Comes right after ISP.")),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("출간 전 마지막 검수관.", "The last checker before publication."), ('ISP/ISMP 다음, 실제 프로젝트가 시작된 뒤에 와요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Comes after ISP/ISMP, once the project is actually running. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("요구공학", "Requirements Engineering", ("개별 책의 개요를 정확히 받아적는 일.", "Taking down one book's own outline precisely."), ("로드맵이 정해진 뒤, 책 한 권 단위에서 하는 일이에요.", "Happens for a single book, after the roadmap is set.")),
        ("BPR", "BPR", ("출판 공정 자체를 뜯어고치는 일.", "Overhauling the publishing process itself."), ("ISP와 함께 조직 차원에서 논의되곤 해요.", "Often discussed alongside ISP at the organizational level.")),
        ("아키텍처 원칙", "Architecture Principles", ("모든 책이 따라야 할 공통 스타일가이드.", "The shared style guide every book must follow."), ("로드맵 실행 과정에서 지켜야 할 규칙이에요.", "A rule to follow while carrying out the roadmap.")),
        ("자원 배분", "Resource Allocation", ("어느 작가를 어느 책에 붙일지 정하기.", "Deciding which writer goes on which book."), ("ISMP 단계에서 구체화돼요.", "Gets worked out concretely at the ISMP stage.")),
        ("타당성 검토", "Feasibility Study", ("이 책을 정말 낼 수 있는지 미리 재보기.", "Checking in advance whether the book can really be made."), ("로드맵에 올리기 전에 먼저 해봐요.", "Done before a book even makes it onto the roadmap.")),
    ],
}
