from _draw import *
from _world import *

# 1. 아무것도 안 물어보고 바로 원고부터 쓰기 시작해요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(260, 130, 0.8, marks=1) + manuscript(360, 150, 0.8, marks=3) + manuscript(460, 120, 0.8, marks=5)
         + label(380, 230, "⟦일단 쓰고 보자며 바로 원고를 시작했어요|the writer just started writing without asking anyone⟧", 12, "var(--bad)")
         + label(380, 280, "⟦쓸수록 고칠 곳이 자꾸 늘어나요|the more it's written, the more needs fixing⟧", 13, "var(--ink)"))

# 2. 독자마다 원하는 게 다 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **READER)
         + bubble(140, 80, 200, 36, "⟦저는 쉬운 그림책이 좋아요|I want an easy picture book⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=SMILE, **EDITOR) + bubble(460, 80, 230, 36, "⟦아니요, 어려운 이야기도 넣어주세요|no, put the hard stuff in too⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦독자 말이 다 다르면, 뭘 써야 할지 몰라요|when everyone wants something different, no one knows what to write⟧", 12, "var(--ink)"))

# 3. 요구공학자 = 인터뷰해서 정확한 개요서로 적어두는 사람 (hero)
P3 = svg(340, sky(340)
         + person(380, 110, s=0.9, face=EYES, **WRITER)
         + person(200, 190, s=0.5, face=SMILE, **READER) + person(560, 190, s=0.5, face=SMILE, **EDITOR)
         + manuscript(380, 260, 0.9)
         + label(380, 25, "⟦요구공학자 = 독자·편집장을 인터뷰해서 정확한 개요서로 적어두는 사람|a requirements engineer interviews readers and the editor, then writes it down as a precise outline⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦모호한 말들을 또렷한 문장으로 바꿔요|turning vague wishes into clear sentences⟧", 12, "var(--muted)"))

# 4. 개요서에 들어가는 것
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦명세서에 들어가는 것|WHAT GOES IN THE SPEC⟧",
                      ("⟦기능 요구 — 책이 뭘 할 수 있어야 하나|functional — what the book must do⟧",
                       "⟦비기능 요구 — 얼마나 빨리, 얼마나 쉽게|non-functional — how fast, how easy⟧",
                       "⟦제약 조건 — 예산과 마감|constraints — budget and deadline⟧",
                       "⟦우선순위 — 뭐가 더 중요한가|priority — what matters more⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **WRITER)
         + label(560, 250, "⟦독자 말을 그대로 베끼지 않아요, 정리해서 적어요|doesn't copy what readers say — writes it down organized⟧", 11, "var(--muted)")
         + label(380, 300, "⟦모호하면 다시 물어서 명확하게 만들어요|if it's vague, ask again until it's clear⟧", 12, "var(--ink)"))

# 5. 개요서가 원고를 대신 써주진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **EDITOR) + label(190, 258, "⟦정확한 개요서는 만들어줘요|it gives you a precise outline⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **WRITER) + manuscript(652, 205, 0.5) + label(570, 272, "⟦써야 하는 건 여전히 작가예요|but the writer still has to write it⟧", 11, "var(--ink)")
         + label(380, 294, "⟦요구공학은 무엇을 쓸지 밝히는 일이지, 글을 대신 써주지 않아요|requirements engineering clarifies what to write — it doesn't write it for you⟧", 12, "var(--ink)", cls="d"))

INTERVIEW_I = icon('<circle cx="20" cy="32" r="10" fill="var(--accent)"/><circle cx="44" cy="26" r="8" fill="var(--muted)"/><path d="M12 50 q8 -10 16 0 M36 48 q6 -8 14 0" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SPEC_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
CLARIFY_I = icon('<path d="M16 18 q0 -14 16 -14 q16 0 16 14 q0 10 -10 12 l0 8" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="22" cy="50" r="3.5" fill="var(--accent)"/>')
VALIDATE_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "reqeng", "order": 3,
    "title": ("쓰기 전에 먼저 묻는 사람", "The One Who Asks Before Writing"),
    "h1": ("<em>요구공학/요구사항 명세</em>가 뭐예요?", "What is <em>Requirements Engineering</em>?"),
    "sub": ("요구공학과 요구사항 명세를, 책을 쓰기 전에 독자와 편집장을 인터뷰해 정확한 개요서로 적어두는 이야기로 풀어봤어요.",
            "Requirements engineering and specification, told as a story about interviewing readers and the editor before writing, and setting it all down as a precise outline."),
    "panels": [
        {"svg": P1, "alt": ("작가가 아무에게도 묻지 않고 바로 원고를 쓰기 시작해 교정 표시가 계속 늘어남", "A writer starts writing without asking anyone, and proofreading marks keep piling up"),
         "caption": ("일단 쓰고 보자며 바로 원고를 시작했어요.", "The writer just started writing without asking anyone."),
         "small": ("쓸수록 고칠 곳이 자꾸 늘어나요.", "The more it's written, the more needs fixing.")},
        {"svg": P2, "alt": ("독자는 쉬운 그림책을 원하고, 편집장은 어려운 이야기도 넣자고 말함", "A reader wants an easy picture book, while the editor wants the hard stuff included too"),
         "caption": ("독자마다 원하는 게 다 달라요.", "Every reader wants something different."),
         "small": ("독자 말이 다 다르면, 뭘 써야 할지 몰라요.", "When everyone wants something different, no one knows what to write.")},
        {"svg": P3, "hero": True, "alt": ("작가가 독자와 편집장을 인터뷰하며 개요서를 작성함", "A writer interviews a reader and the editor while writing an outline"),
         "caption": ("요구공학자는 인터뷰해서 정확한 개요서로 적어두는 사람이에요.", "A requirements engineer interviews people and writes it down as a precise outline."),
         "small": ("모호한 말들을 또렷한 문장으로 바꿔요.", "Turning vague wishes into clear sentences."),
         "tricks": (4, [
             (INTERVIEW_I, ("인터뷰로 듣기", "Listen through interviews"), ("독자·편집장에게 직접 물어요", "asking readers and the editor directly"), "calm"),
             (SPEC_I, ("정리해서 적기", "Write it down organized"), ("개요서 한 장으로 모아요", "gathering it into one outline")),
             (CLARIFY_I, ("애매함 없애기", "Clear up ambiguity"), ("또렷한 문장으로 바꿔요", "turning it into clear sentences"), "warm"),
             (VALIDATE_I, ("확인받기", "Get it confirmed"), ("맞는지 다시 보여줘요", "showing it back to confirm")),
         ])},
        {"svg": P4, "alt": ("개요서 체크리스트: 기능 요구·비기능 요구·제약 조건·우선순위 네 항목", "An outline checklist: functional, non-functional, constraints, priority"),
         "caption": ("개요서에는 이 네 가지가 들어가요.", "The outline contains these four things."),
         "small": ("독자 말을 그대로 베끼지 않아요, 정리해서 적어요.", "It doesn't copy what readers say — it writes it down organized.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 개요서는 정확해졌다고 말함. 오른쪽: 작가가 여전히 원고를 써야 함", "Left: the editor says the outline is now precise. Right: the writer still has to write the manuscript"),
         "caption": ("개요서가 원고를 대신 써주진 않아요.", "The outline doesn't write the manuscript for you."),
         "small": ("무엇을 쓸지 밝히는 일이지, 글을 대신 써주지 않아요.", "It clarifies what to write — it doesn't write it for you.")},
    ],
    "summary": (("<b>요구공학</b> = 쓰기 전에 <b>독자·편집장을 인터뷰</b>해서, 쓸 것을 <b>또렷한 개요서</b>로 적어두는 일.",
                 "<b>Requirements engineering</b> = interviewing <b>readers and the editor before writing</b>, and setting down what to write as a <b>clear outline</b>."),
                ("요구공학은 도출(elicitation)·분석(analysis)·명세(specification)·검증(validation) 네 단계로 요구사항을 다루는 활동이에요. 요구사항 명세서는 그 결과물로, 기능 요구사항(무엇을 해야 하나)과 비기능 요구사항(얼마나 빨리·안전하게)을 나눠 적어요. 명세가 모호하면 나중 단계일수록 고치는 비용이 커져요.",
                 "Requirements engineering handles requirements through four stages: elicitation, analysis, specification, and validation. The requirements specification is its output, separating functional requirements (what it must do) from non-functional ones (how fast, how safely). The later an ambiguity is caught, the more it costs to fix.")),
    "glossary": [
        ("요구공학", "Requirements Engineering", ("쓰기 전에 먼저 묻는 일 전체.", "The whole business of asking before writing."), ("도출·분석·명세·검증 네 단계예요.", "Four stages: elicitation, analysis, specification, validation.")),
        ("요구사항 명세서", "Requirements Specification", ("정리해서 적어둔 개요서.", "The outline, written down organized."), ("기능/비기능 요구를 나눠 적어요.", "Separates functional from non-functional requirements.")),
        ("ISP/ISMP", "ISP/ISMP", ("출판 로드맵을 그리는 일.", "Mapping the publishing roadmap."), ('요구공학보다 더 큰 단위, 출판사 전체 방향이에요. → <a href="ispismp-ko.html">출판 로드맵을 그리는 사람</a>', 'A bigger unit than requirements engineering — the whole house\'s direction. → <a href="ispismp-en.html">the one who maps the publishing roadmap</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("출간 전 마지막 검수관.", "The last checker before publication."), ('명세가 지켜졌는지도 감리의 점검 대상이에요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Whether the spec was followed is one thing audit checks. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("추적성", "Traceability", ("개요서 한 줄이 원고 어디로 갔는지 따라가기.", "Tracing one outline line to where it ended up in the manuscript."), ("요구가 빠졌는지 확인할 때 써요.", "Used to check nothing got dropped.")),
        ("요구사항 변경관리", "Requirements Change Management", ("쓰다가 생각이 바뀌었을 때 처리법.", "How to handle a change of mind mid-write."), ("개요서는 한 번 쓰면 끝이 아니에요.", "The outline isn't written just once and done.")),
        ("UML", "UML", ("쓰기 전에 그려보는 설계 지도.", "The design map drawn before writing."), ('명세를 그림으로도 표현할 때 써요. → <a href="umldiagram-ko.html">쓰기 전에 그리는 설계 지도</a>', 'Also used to express the spec visually. → <a href="umldiagram-en.html">the design map drawn before writing</a>')),
        ("우선순위 협상", "Requirements Prioritization", ("뭐부터 넣을지 줄 세우기.", "Lining up what goes in first."), ("예산과 마감 안에서 정해요.", "Decided within budget and deadline.")),
    ],
}
