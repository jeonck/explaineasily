from _draw import *
from _world import *

# 1. 책 전체를 2년 통째로 쓰고 마지막에야 보여줬어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(260, 130, 0.8) + manuscript(360, 150, 0.8) + manuscript(460, 120, 0.8)
         + label(380, 255, "⟦작가가 2년 동안 통째로 쓰고 마지막에야 독자에게 보여줬어요|the writer spent two years on the whole book, showing readers only at the very end⟧", 12, "var(--bad)")
         + label(380, 280, "⟦다 쓰고 나니 독자 취향이 이미 바뀌어 있었어요|by the time it was done, readers' tastes had already changed⟧", 13, "var(--ink)"))

# 2. 끝까지 보여주지 말라는 계획, 끝나서야 들리는 의견
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(100, 80, 260, 36, "⟦계획대로만 가요, 끝까지 독자에게 보여주지 마세요|stick to the plan — no readers see it till the end⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **READER) + bubble(440, 80, 270, 36, "⟦진작 원고를 봤으면 미리 의견을 드렸을 텐데요|had I seen the draft earlier, I'd have told you sooner⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦책을 끝에만 보여주면, 고칠 기회도 끝에만 와요|showing the book only at the end means the only chance to fix it comes at the end too⟧", 12, "var(--ink)"))

# 3. 애자일/스크럼 = 짧은 챕터 단위로 나눠 쓰고 매번 보여주는 작업법 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **WRITER) + inkstamp(460, 90, 0.8)
         + manuscript(260, 180, 0.7, text="⟦1장 완성|ch.1 done⟧") + manuscript(380, 216, 0.7, text="⟦2장 완성|ch.2 done⟧") + manuscript(500, 180, 0.7, text="⟦3장 완성|ch.3 done⟧")
         + label(380, 30, "⟦애자일/스크럼 = 책을 짧은 챕터 단위로 나눠 쓰고, 챕터마다 독자에게 보여주는 작업법|Agile/Scrum = writing the book in short chapters and showing each one to readers⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 챕터가 끝날 때마다 독자 피드백을 받아 다음 챕터에 바로 반영해요|after every chapter, reader feedback comes in and goes straight into the next one⟧", 12, "var(--muted)"))

# 4. 스크럼 역할과 리듬
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦스크럼 역할과 리듬|SCRUM ROLES AND RHYTHM⟧",
                      ("⟦편집장(PO) — 백로그 우선순위를 정해요|editor (PO) — sets backlog priority⟧",
                       "⟦작가들(개발자) — 챕터를 실제로 써요|writers (developers) — actually write the chapters⟧",
                       "⟦스크럼 마스터 — 막힌 일을 풀어 진행을 도와요|scrum master — clears blockers, helps work flow⟧",
                       "⟦스프린트 — 예: 2주마다 챕터 한 편|sprint — e.g. one chapter every two weeks⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **EDITOR)
         + label(560, 250, "⟦우선순위 책임은 편집장, 팀 의견도 들어요|the editor owns priority, with the team's input⟧", 11, "var(--muted)")
         + label(380, 300, "⟦스프린트를 짧게 반복하면, 책이 틀린 방향으로 가도 몇 주 안에 알아차려요|short, repeated sprints reveal a wrong direction within weeks, not years⟧", 12, "var(--ink)"))

# 5. 독자 의견은 빨리 들어도 글은 작가가 써야 해요
P5 = svg(340, '<rect width="380" height="340" fill="var(--accent-soft)"/><rect x="380" width="380" height="340" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=EYES, **EDITOR) + label(190, 260, "⟦짧게 나눠 쓰면 독자 의견을 더 빨리 들어요|short chapters bring reader feedback in sooner⟧", 11, "var(--ink)")
         + person(570, 110, s=0.8, face=SMILE, **WRITER) + manuscript(570, 200, 0.6) + label(570, 260, "⟦그래도 글은 작가가 직접 써야 해요|but the writing itself is still up to the writer⟧", 11, "var(--ink)")
         + label(380, 315, "⟦애자일은 일하는 방식이지, 글쓰기 실력을 대신 채워주진 않아요|Agile is a way of working — it doesn't replace the writer's own skill⟧", 12, "var(--ink)", cls="d"))

SPRINT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 5" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
REVIEW_I = icon('<path d="M8 32 q24 -22 48 0 q-24 22 -48 0z" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--good)"/>')
BACKLOG_I = icon('<path d="M18 50 V26 M32 50 V14 M46 50 V34" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
RETRO_I = icon('<path d="M46 20 a18 18 0 1 0 2 24" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M46 10 v12 h-12" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "agilescrum", "order": 4,
    "title": ("한 챕터씩 보여주며 쓰기", "Writing a Chapter at a Time, and Showing It"),
    "h1": ("<em>애자일/스크럼</em>이 뭐예요?", "What is <em>Agile/Scrum</em>?"),
    "sub": ("애자일과 스크럼을, 책 전체를 한 번에 쓰지 않고 짧은 챕터 단위로 나눠 쓰며 챕터마다 독자에게 보여주는 이야기로 풀어봤어요.",
            "Agile and Scrum, told as a story about writing a book in short chapters instead of all at once, and showing each chapter to readers as it's done."),
    "panels": [
        {"svg": P1, "alt": ("작가가 2년 동안 책 전체를 통째로 써서 마지막에야 보여줌", "A writer spends two years writing the whole book and shows it only at the very end"),
         "caption": ("작가가 책 전체를 2년 동안 통째로 쓰고, 마지막에야 독자에게 보여줬어요.", "The writer spent two years on the whole book and showed readers only at the very end."),
         "small": ("다 쓰고 나니 독자 취향이 이미 바뀌어 있었어요.", "By the time it was done, readers' tastes had already changed.")},
        {"svg": P2, "alt": ("편집장은 끝까지 보여주지 말자고 하고, 독자는 진작 봤으면 좋았을 거라고 말함", "The editor says not to show anything until the end; the reader says they wish they'd seen it sooner"),
         "caption": ("독자에게 끝까지 안 보여주는 계획이라, 독자 의견은 책이 끝나고 나서야 들려요.", "The plan shows readers nothing until the end, so their feedback only arrives once the book is done."),
         "small": ("책을 끝에만 보여주면, 고칠 기회도 끝에만 와요.", "Showing the book only at the end means the only chance to fix it comes at the end too.")},
        {"svg": P3, "hero": True, "alt": ("작가가 챕터를 하나씩 완성해 도장을 받고, 세 챕터가 각각 완성 표시됨", "A writer finishes chapters one by one and gets them stamped, with three chapters marked done"),
         "caption": ("애자일/스크럼은 책을 짧은 챕터 단위로 나눠 쓰고, 챕터마다 독자에게 보여주는 작업법이에요.", "Agile/Scrum means writing the book in short chapters and showing each one to readers."),
         "small": ("한 챕터가 끝날 때마다 독자 피드백을 받아 다음 챕터에 바로 반영해요.", "After every chapter, reader feedback comes in and goes straight into the next one."),
         "tricks": (4, [
             (SPRINT_I, ("짧은 주기로 쓰기", "Write in short cycles"), ("한 스프린트 = 한 챕터", "one sprint = one chapter"), "calm"),
             (REVIEW_I, ("매번 보여주기", "Show it every time"), ("독자에게 바로 확인받아요", "checked with readers right away")),
             (BACKLOG_I, ("우선순위부터 쓰기", "Write top priority first"), ("중요한 챕터부터 먼저요", "the most important chapter goes first"), "warm"),
             (RETRO_I, ("팀이 함께 돌아보기", "Team looks back together"), ("잘된 점과 고칠 점을 찾아 다음 챕터에 써요", "finding what to keep and change in the next chapter")),
         ])},
        {"svg": P4, "alt": ("스크럼 역할표: 편집장(PO)·작가들(개발자)·스크럼 마스터·스프린트 리듬 네 항목", "A Scrum roles board: editor (PO), writers (developers), scrum master, sprint rhythm"),
         "caption": ("스크럼은 역할과 짧은 리듬으로 움직여요.", "Scrum runs on roles and a short rhythm."),
         "small": ("우선순위의 최종 책임은 편집장(PO)에게 있지만, 스프린트마다 팀 의견을 듣고 맞춰요.", "The editor (PO) holds final accountability for priority, but adjusts it with the team's input each sprint.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 짧게 나눠 쓰면 독자 의견을 더 빨리 듣는다고 말함. 오른쪽: 글은 여전히 작가가 직접 써야 함", "Left: the editor says short chapters bring reader feedback in sooner. Right: the writer still has to write the book themselves"),
         "caption": ("독자 의견은 빨리 들어도, 글은 작가가 직접 써야 해요.", "Reader feedback comes sooner, but the writer still has to write the chapters."),
         "small": ("애자일은 일하는 방식이지, 글쓰기 실력을 대신 채워주진 않아요.", "Agile is a way of working — it doesn't replace the writer's own skill.")},
    ],
    "summary": (("<b>애자일/스크럼</b> = 책을 <b>짧은 챕터 단위</b>로 나눠 쓰고, <b>챕터마다 독자에게 보여주며</b> 고쳐가는 작업법.",
                 "<b>Agile/Scrum</b> = writing a book in <b>short chapters</b>, <b>showing each one to readers</b>, and revising as you go."),
                ("애자일은 변화에 빠르게 대응하는 소프트웨어 개발 철학이고, 스크럼은 그 철학을 실행하는 대표적 프레임워크예요. 일을 스프린트(보통 1~4주) 단위로 쪼개고, 매 스프린트 끝에 결과물을 보여주는 리뷰와 과정을 돌아보는 회고를 거쳐요. 제품 책임자(PO)가 우선순위를, 개발자들이 실행을, 스크럼 마스터가 진행을 돕는 역할을 맡아요.",
                 "Agile is a philosophy for responding quickly to change in software development, and Scrum is its best-known framework. Work is split into sprints (usually 1-4 weeks), each ending with a review of the result and a retrospective on the process. A product owner sets priority, the developers execute, and a scrum master helps the process run smoothly.")),
    "glossary": [
        ("애자일", "Agile", ("짧게 쓰고 자주 보여주는 철학.", "The philosophy of writing short and showing often."), ("변화에 빠르게 대응해요.", "Responds quickly to change.")),
        ("스크럼", "Scrum", ("애자일을 실행하는 대표적 틀.", "The best-known framework for running Agile."), ("스프린트 안에서 계획·일일 점검·리뷰·회고를 해요.", "Each sprint holds planning, daily check-ins, a review, and a retrospective.")),
        ("스프린트", "Sprint", ("챕터 한 편을 쓰는 짧은 주기.", "The short cycle for writing one chapter."), ("보통 1~4주예요.", "Usually one to four weeks.")),
        ("제품 백로그", "Product Backlog", ("아직 안 쓴 챕터들의 줄 세운 목록.", "The ranked list of chapters not yet written."), ("편집장이 우선순위를 매겨요.", "The editor ranks it by priority.")),
        ("폭포수 모델", "Waterfall Model", ("책 전체를 처음 계획대로 끝까지 한 번에 쓰는 방식.", "Writing the whole book in one go, exactly to the original plan."), ("애자일이 맞서는 옛 방식이에요.", "The older style Agile pushes back against.")),
        ("요구공학", "Requirements Engineering", ("독자가 뭘 원하는지 쓰기 전에 먼저 묻는 일.", "Asking what readers want before writing."), ('스크럼에서는 백로그의 내용과 순서를 스프린트마다 다시 따져 물어요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', 'In Scrum, the contents and order of the backlog get questioned again every sprint. → <a href="reqeng-en.html">the one who asks before writing</a>')),
        ("일일 스탠드업", "Daily Standup", ("매일 같은 시간에 15분 안에 나누는 진행 상황.", "A 15-minute check-in on progress, at the same time every day."), ("막힌 곳을 빨리 찾아내요.", "Catches blockers quickly.")),
        ("회고", "Retrospective", ("챕터 끝에 팀이 모여 돌아보는 시간.", "The team's look-back at the end of a chapter."), ("잘된 점과 고칠 점을 찾아 다음 스프린트에 적용해요.", "Finds what to keep and change for the next sprint.")),
    ],
}
