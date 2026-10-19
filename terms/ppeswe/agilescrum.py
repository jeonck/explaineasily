from _draw import *
from _world import *

# 1. 책 전체를 2년 통째로 쓰고 마지막에야 보여줬어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(260, 130, 0.8) + manuscript(360, 150, 0.8) + manuscript(460, 120, 0.8)
         + label(380, 230, "⟦2년 통째로 쓰고 마지막에야 보여줬어요|wrote the whole thing for two years, showed it only at the very end⟧", 12, "var(--bad)")
         + label(380, 280, "⟦다 쓰고 나니 독자 취향이 이미 바뀌어 있었어요|by the time it was done, readers' tastes had already changed⟧", 13, "var(--ink)"))

# 2. 끝까지 보여주지 말라는 계획, 끝나서야 들리는 의견
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 200, 36, "⟦계획대로만 가요, 끝까지 보여주지 마세요|just stick to the plan, don't show it till the end⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **READER) + bubble(470, 80, 220, 36, "⟦진작 보여줬으면 미리 말씀드렸을 텐데요|if you'd shown it earlier, I could've told you sooner⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦끝에만 보여주면, 고칠 기회도 끝에만 와요|showing it only at the end means the only chance to fix it comes at the end too⟧", 12, "var(--ink)"))

# 3. 애자일/스크럼 = 짧은 챕터 단위로 나눠 쓰고 매번 보여주는 작업법 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **WRITER) + inkstamp(460, 90, 0.8)
         + manuscript(260, 180, 0.7, text="⟦1장 완성|ch.1 done⟧") + manuscript(380, 200, 0.7, text="⟦2장 완성|ch.2 done⟧") + manuscript(500, 180, 0.7, text="⟦3장 완성|ch.3 done⟧")
         + label(380, 30, "⟦애자일/스크럼 = 책을 짧은 챕터 단위로 나눠 쓰고, 매번 독자에게 보여주는 작업법|Agile/Scrum = writing the book in short chapters and showing it to readers every single time⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦한 챕터가 끝날 때마다 피드백을 받아 다음 챕터에 바로 반영해요|after every chapter, feedback comes in and goes straight into the next one⟧", 12, "var(--muted)"))

# 4. 스크럼 역할과 리듬
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦스크럼 역할과 리듬|SCRUM ROLES AND RHYTHM⟧",
                      ("⟦편집장 — 백로그 우선순위를 정해요|editor — sets backlog priority⟧",
                       "⟦작가팀 — 챕터를 실제로 써요|writer team — actually writes the chapters⟧",
                       "⟦교정자 — 매 챕터 품질을 확인해요|proofreader — checks quality each chapter⟧",
                       "⟦스프린트 — 2주마다 챕터 한 편|sprint — one chapter every two weeks⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **EDITOR)
         + label(560, 250, "⟦편집장도 혼자 정하지 않아요, 팀과 매번 조율해요|the editor doesn't decide alone — the team adjusts together every time⟧", 11, "var(--muted)")
         + label(380, 300, "⟦짧게 반복하면서, 틀린 방향이면 빨리 알아차려요|short repeating cycles catch a wrong direction quickly⟧", 12, "var(--ink)"))

# 5. 속도는 빨라져도 글은 작가가 써야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **EDITOR) + label(190, 240, "⟦속도는 빨라져요|it makes things move faster⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **WRITER) + manuscript(570, 220, 0.6) + label(570, 270, "⟦그래도 글은 작가가 직접 써야 해요|but the writing itself is still up to the writer⟧", 11, "var(--ink)")
         + label(380, 282, "⟦애자일은 일하는 방식이지, 글쓰기 실력을 대신 채워주진 않아요|Agile is a way of working — it doesn't replace the writer's own skill⟧", 12, "var(--ink)", cls="d"))

SPRINT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 5" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
REVIEW_I = icon('<path d="M8 32 q24 -22 48 0 q-24 22 -48 0z" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="var(--good)"/>')
BACKLOG_I = icon('<path d="M18 50 V26 M32 50 V14 M46 50 V34" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
RETRO_I = icon('<path d="M46 20 a18 18 0 1 0 2 24" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M46 10 v12 h-12" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "agilescrum", "order": 4,
    "title": ("한 챕터씩 보여주며 쓰기", "Writing a Chapter at a Time, and Showing It"),
    "h1": ("<em>애자일/스크럼</em>이 뭐예요?", "What is <em>Agile/Scrum</em>?"),
    "sub": ("애자일와 스크럼을, 책 전체를 한 번에 쓰지 않고 짧은 챕터 단위로 나눠 쓰며 매번 독자에게 보여주는 이야기로 풀어봤어요.",
            "Agile and Scrum, told as a story about writing a book in short chapters instead of all at once, and showing it to readers every single time."),
    "panels": [
        {"svg": P1, "alt": ("작가가 2년 동안 책 전체를 통째로 써서 마지막에야 보여줌", "A writer spends two years writing the whole book and shows it only at the very end"),
         "caption": ("책 전체를 2년 통째로 쓰고 마지막에야 보여줬어요.", "The whole book was written for two years, shown only at the very end."),
         "small": ("다 쓰고 나니 독자 취향이 이미 바뀌어 있었어요.", "By the time it was done, readers' tastes had already changed.")},
        {"svg": P2, "alt": ("편집장은 끝까지 보여주지 말자고 하고, 독자는 진작 봤으면 좋았을 거라고 말함", "The editor says not to show anything until the end; the reader says they wish they'd seen it sooner"),
         "caption": ("끝까지 보여주지 말라는 계획, 끝나고 나서야 들리는 의견.", "A plan to show nothing until the end — feedback that only arrives once it's over."),
         "small": ("끝에만 보여주면, 고칠 기회도 끝에만 와요.", "Showing it only at the end means the only chance to fix it comes at the end too.")},
        {"svg": P3, "hero": True, "alt": ("작가가 챕터를 하나씩 완성해 도장을 받고, 세 챕터가 각각 완성 표시됨", "A writer finishes chapters one by one and gets them stamped, with three chapters marked done"),
         "caption": ("애자일/스크럼은 짧은 챕터 단위로 나눠 쓰고 매번 보여주는 작업법이에요.", "Agile/Scrum means writing in short chapters and showing it every single time."),
         "small": ("한 챕터가 끝날 때마다 피드백을 받아 다음 챕터에 바로 반영해요.", "After every chapter, feedback comes in and goes straight into the next one."),
         "tricks": (4, [
             (SPRINT_I, ("짧은 주기로 쓰기", "Write in short cycles"), ("한 스프린트 = 한 챕터", "one sprint = one chapter"), "calm"),
             (REVIEW_I, ("매번 보여주기", "Show it every time"), ("독자에게 바로 확인받아요", "checked with readers right away")),
             (BACKLOG_I, ("우선순위부터 쓰기", "Write top priority first"), ("중요한 챕터부터 먼저요", "the most important chapter goes first"), "warm"),
             (RETRO_I, ("팀이 함께 돌아보기", "Team looks back together"), ("다음 챕터를 더 낫게 해요", "making the next chapter better")),
         ])},
        {"svg": P4, "alt": ("스크럼 역할표: 편집장·작가팀·교정자·스프린트 리듬 네 항목", "A Scrum roles board: editor, writer team, proofreader, sprint rhythm"),
         "caption": ("스크럼은 역할과 짧은 리듬으로 움직여요.", "Scrum runs on roles and a short rhythm."),
         "small": ("편집장도 혼자 정하지 않아요, 팀과 매번 조율해요.", "The editor doesn't decide alone — the team adjusts together every time.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 속도가 빨라진다고 말함. 오른쪽: 작가가 여전히 직접 써야 함", "Left: the editor says things move faster. Right: the writer still has to write it themselves"),
         "caption": ("속도는 빨라져도 글은 작가가 써야 해요.", "Things move faster, but the writer still has to write."),
         "small": ("애자일은 일하는 방식이지, 글쓰기 실력을 대신 채워주진 않아요.", "Agile is a way of working — it doesn't replace the writer's own skill.")},
    ],
    "summary": (("<b>애자일/스크럼</b> = 책을 <b>짧은 챕터 단위</b>로 나눠 쓰고, <b>매번 독자에게 보여주며</b> 고쳐가는 작업법.",
                 "<b>Agile/Scrum</b> = writing a book in <b>short chapters</b>, <b>showing it to readers every time</b>, and revising as you go."),
                ("애자일은 변화에 빠르게 대응하는 소프트웨어 개발 철학이고, 스크럼은 그 철학을 실행하는 대표적 프레임워크예요. 일을 스프린트(보통 1~4주) 단위로 쪼개고, 매 스프린트 끝에 결과물을 보여주는 리뷰와 과정을 돌아보는 회고를 거쳐요. 제품 책임자(PO)가 우선순위를, 개발팀이 실행을, 스크럼 마스터가 진행을 돕는 역할을 맡아요.",
                 "Agile is a philosophy for responding quickly to change in software development, and Scrum is its best-known framework. Work is split into sprints (usually 1-4 weeks), each ending with a review of the result and a retrospective on the process. A product owner sets priority, the dev team executes, and a scrum master helps the process run smoothly.")),
    "glossary": [
        ("애자일", "Agile", ("짧게 쓰고 자주 보여주는 철학.", "The philosophy of writing short and showing often."), ("변화에 빠르게 대응해요.", "Responds quickly to change.")),
        ("스크럼", "Scrum", ("애자일을 실행하는 대표적 틀.", "The best-known framework for running Agile."), ("스프린트·리뷰·회고로 이뤄져요.", "Made of sprints, reviews, and retrospectives.")),
        ("스프린트", "Sprint", ("챕터 한 편을 쓰는 짧은 주기.", "The short cycle for writing one chapter."), ("보통 1~4주예요.", "Usually one to four weeks.")),
        ("제품 백로그", "Product Backlog", ("아직 안 쓴 챕터들의 줄 세운 목록.", "The ranked list of chapters not yet written."), ("편집장이 우선순위를 매겨요.", "The editor ranks it by priority.")),
        ("폭포수 모델", "Waterfall Model", ("처음 계획대로 끝까지 한 번에 쓰는 방식.", "Writing it all at once, exactly to the original plan."), ("애자일이 맞서는 옛 방식이에요.", "The older style Agile pushes back against.")),
        ("요구공학", "Requirements Engineering", ("쓰기 전에 먼저 묻는 일.", "Asking before writing."), ('스크럼에서는 백로그를 계속 다시 물어요. → <a href="reqeng-ko.html">쓰기 전에 먼저 묻는 사람</a>', 'In Scrum, the backlog keeps getting asked about again. → <a href="reqeng-en.html">the one who asks before writing</a>')),
        ("일일 스탠드업", "Daily Standup", ("매일 아침 짧게 서서 나누는 진행 상황.", "A short standing check-in on progress every morning."), ("막힌 곳을 빨리 찾아내요.", "Catches blockers quickly.")),
        ("회고", "Retrospective", ("챕터 끝에 팀이 모여 돌아보는 시간.", "The team's look-back at the end of a chapter."), ("다음 스프린트를 더 낫게 만들어요.", "Makes the next sprint better.")),
    ],
}
