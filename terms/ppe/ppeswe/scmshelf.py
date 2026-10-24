from _draw import *
from _world import *

# 1. 작가 셋이 같은 원고를 각자 고쳤어요
P1 = svg(300, sky(300)
         + person(130, 150, s=0.8, face=SWEAT, **WRITER) + bubble(84, 70, 140, 36, "⟦내 PC에서 고쳤어요|edited on my laptop⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(380, 150, s=0.8, face=EYES, **EDITOR) + bubble(324, 70, 160, 36, "⟦USB로 가져왔어요|brought it in on a USB⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 150, s=0.8, face=FROWN, **PROOFER) + bubble(529, 70, 190, 36, "⟦이메일로 받았어요|got it by email⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 30, "⟦작가 셋이 같은 원고를 각자 고쳤어요|three writers each edited the same manuscript on their own⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦어느 게 최신판인지 아무도 몰라요|nobody knows which copy is the newest⟧", 12, "var(--bad)"))

# 2. 덮어쓰면 남의 수정이 사라져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 30, "⟦저장하기 누르는 순간|the moment someone hits save⟧", 13, "var(--ink)", cls="d")
         + manuscript(260, 110, 0.9, marks=1) + manuscript(500, 110, 0.9, marks=1)
         + '<path d="M340 110 H420" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/><path d="M360 96 l40 28 M400 96 l-40 28" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + person(380, 190, s=0.65, face=FROWN, **WRITER)
         + label(380, 285, "⟦나중에 저장한 사람이, 앞사람 수정을 지워버려요|whoever saves last erases the person before them⟧", 12, "var(--bad)"))

# 3. 형상관리(SCM) = 번호 매긴 보관 서가 (hero)
VER_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="24" r="9" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M26 44 h12 M26 50 h12" stroke="#142033" stroke-width="2.5"/>')
LOG_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="22" cy="22" r="3" fill="var(--good)"/><rect x="28" y="20" width="18" height="3" fill="#142033"/><circle cx="22" cy="34" r="3" fill="var(--good)"/><rect x="28" y="32" width="18" height="3" fill="#142033"/><circle cx="22" cy="46" r="3" fill="var(--good)"/><rect x="28" y="44" width="18" height="3" fill="#142033"/>')
BRANCH_I = icon('<circle cx="18" cy="48" r="5" fill="var(--accent)"/><path d="M18 43 V26" stroke="var(--accent)" stroke-width="4"/><path d="M18 26 Q18 14 34 14" stroke="var(--accent)" stroke-width="4" fill="none"/><circle cx="34" cy="14" r="5" fill="var(--good)"/><path d="M18 26 Q18 38 46 44" stroke="var(--muted)" stroke-width="4" fill="none"/><circle cx="46" cy="44" r="5" fill="var(--muted)"/>')
MERGE_I = icon('<circle cx="16" cy="14" r="5" fill="var(--accent)"/><circle cx="48" cy="14" r="5" fill="var(--good)"/><path d="M16 19 Q16 34 32 40" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M48 19 Q48 34 32 40" stroke="var(--good)" stroke-width="4" fill="none"/><circle cx="32" cy="46" r="6" fill="var(--ink)"/>')

P3 = svg(340, sky(340)
         + bookshelf(260, 90, 1.6, n=4, hl=2)
         + label(380, 30, "⟦형상관리 = 번호 매긴 보관 서가|SCM = a storage shelf with numbered slots⟧", 14, "var(--ink)", cls="d")
         + person(130, 230, s=0.75, face=EYES, **EDITOR) + manuscript(210, 240, 0.55)
         + person(630, 230, s=0.75, face=SMILE, **WRITER)
         + label(380, 300, "⟦모든 판(버전)이 제자리에 있고, 지금 판이 어느 건지도 알아요|every version sits in its place, and you always know which is current⟧", 12, "var(--muted)")
         + label(380, 325, "⟦예전 판이 필요하면, 그 칸에서 그대로 꺼내 쓰면 돼요|need an old edition? just pull it from its slot⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "scmshelf", "order": 15,
    "title": ("원고를 지키는 보관 서가", "The Shelf That Protects the Manuscript"),
    "h1": ("<em>소프트웨어 형상관리(SCM)</em>가 뭐예요?", "What is <em>Software Configuration Management (SCM)</em>?"),
    "sub": ("형상관리를, 원고의 모든 판을 번호 매겨 지키는 보관 서가 이야기로 풀어봤어요.",
            "Configuration management, told as a story about a storage shelf that keeps every numbered edition of a manuscript safe."),
    "panels": [
        {"svg": P1, "alt": ("작가 셋이 각자 노트북·USB·이메일로 같은 원고를 고침", "Three writers each edit the same manuscript — on a laptop, a USB drive, and by email"),
         "caption": ("작가 셋이 같은 원고를 각자 고쳤어요.", "Three writers each edited the same manuscript on their own."),
         "small": ("어느 게 최신판인지 아무도 몰라요.", "Nobody knows which copy is the newest.")},
        {"svg": P2, "alt": ("두 원고가 부딪치고, 작가가 찡그린 채 앉아 있음", "Two manuscript copies collide, and a writer sits frowning"),
         "caption": ("덮어쓰면 남의 수정이 사라져요.", "Overwriting erases someone else's edits."),
         "small": ("나중에 저장한 사람이, 앞사람 수정을 지워버려요.", "Whoever saves last erases the person before them.")},
        {"svg": P3, "hero": True, "alt": ("번호 매긴 보관 서가 앞에 편집장과 작가가 서 있고, 2번 칸이 강조됨", "An editor and a writer stand before a numbered shelf, with slot 2 highlighted"),
         "caption": ("형상관리(SCM)는 번호 매긴 보관 서가예요.", "Configuration management is a shelf with numbered slots."),
         "small": ("예전 판이 필요하면, 그 칸에서 그대로 꺼내 쓰면 돼요.", "Need an old edition? Just pull it from its slot."),
         "tricks": (4, [
             (VER_I, ("버전 번호 매기기", "Number every version"), ("모든 판에 고유 번호를 줘요", "every edition gets its own number"), "calm"),
             (LOG_I, ("변경 이력 남기기", "Keep a change log"), ("누가 뭘 언제 고쳤는지 기록해요", "records who changed what, and when")),
             (BRANCH_I, ("가지치기(브랜치)", "Branch off"), ("원본은 두고 복사본에서 실험해요", "experiment on a copy, leave the original")),
             (MERGE_I, ("합치기(병합)", "Merge back"), ("실험이 끝나면 하나로 합쳐요", "once it works, fold it back into one"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + label(380, 34, "⟦가지치기와 병합|BRANCH AND MERGE⟧", 14, "var(--ink)", cls="d")
                    + bookshelf(70, 70, 1.1, n=3, hl=1)
                    + '<path d="M165 100 Q260 60 340 90" stroke="var(--accent)" stroke-width="4" fill="none" stroke-dasharray="6 5"/>'
                    + manuscript(400, 80, 0.6, text="⟦실험용 사본|experimental copy⟧")
                    + '<path d="M400 100 Q460 150 400 190" stroke="var(--accent)" stroke-width="4" fill="none" stroke-dasharray="6 5"/>'
                    + manuscript(400, 220, 0.6, marks=1, text="⟦고쳐 봤어요|tried a change⟧")
                    + '<path d="M365 220 Q270 260 180 160" stroke="var(--good)" stroke-width="4" fill="none" stroke-dasharray="6 5"/>'
                    + label(380, 285, "⟦잘 되면 원본 서가로 다시 합쳐요|if it works, it merges back into the shelf⟧", 12, "var(--muted)")),
         "alt": ("보관 서가에서 실험용 사본이 갈라져 나왔다가, 수정 후 다시 서가로 합쳐짐", "An experimental copy branches off the shelf, gets edited, then merges back in"),
         "caption": ("가지치기(브랜치)와 합치기(병합)로 실험해요.", "You experiment with a branch, then merge it back."),
         "small": ("원본은 그대로 두고 복사본에서 고쳐 보고, 잘 되면 다시 하나로 합쳐요.", "The original stays untouched while you try changes on a copy — then fold it back in if it works.")},
        {"svg": svg(300, sky(300)
                    + bookshelf(324, 70, 1.0, n=4, hl=3)
                    + person(150, 170, s=0.7, face=FROWN, **WRITER) + label(150, 270, "⟦둘이 같은 줄을 고쳤어요|two of us edited the same line⟧", 11, "var(--ink)")
                    + person(600, 170, s=0.7, face=EYES, **PROOFER) + label(600, 270, "⟦그건 서가가 대신 정해주지 않아요|the shelf won't decide that for you⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦서가가 다 해결해주진 않아요|the shelf doesn't solve everything⟧", 13, "var(--bad)", cls="d")),
         "alt": ("보관 서가는 멀쩡하지만, 두 작가가 같은 줄을 고쳐 다툼. 교정자는 그건 서가가 대신 정해주지 않는다고 말함", "The shelf is fine, but two writers edited the same line and must settle it themselves"),
         "caption": ("서가가 다 해결해주진 않아요.", "The shelf doesn't solve everything."),
         "small": ('같은 부분을 동시에 고치면 사람이 직접 조율해야 해요(병합 충돌). 백업·재해복구는 또 다른 이야기예요 → <a href="backup-ko.html">보관실의 복사본</a>.',
                   'If two edits collide, a person still has to reconcile them (a merge conflict). Backup and disaster recovery is a different story → <a href="backup-en.html">the copy kept in the vault</a>.')},
    ],
    "summary": (("<b>형상관리(SCM)</b> = 원고의 모든 판을 <b>번호 매겨 보관</b>하고, <b>누가 뭘 바꿨는지 기록</b>하며, 실험은 <b>가지쳐서 나중에 합치는</b> 서가.",
                 "<b>Software Configuration Management (SCM)</b> = a shelf that <b>numbers and stores every edition</b>, <b>logs who changed what</b>, and lets you <b>branch off to experiment and merge back</b> later."),
                ("형상관리는 소프트웨어 산출물(코드·문서·설정)의 변경을 식별하고, 버전을 통제하며, 이력을 추적 가능하게 관리하는 활동이에요. 형상식별·형상통제·형상감사·형상기록관리의 네 활동으로 이뤄지고, Git 같은 버전관리시스템(VCS)이 실무 도구로 쓰여요.",
                 "Configuration management identifies changes to software artifacts (code, docs, configs), controls versions, and keeps the history traceable. It consists of four activities — identification, control, audit, and status accounting — carried out in practice with version control systems (VCS) like Git.")),
    "glossary": [
        ("형상관리(SCM)", "Configuration Management", ("원고의 모든 판을 지키는 서가.", "The shelf that keeps every edition safe."), ("식별·통제·감사·기록의 네 활동으로 이뤄져요.", "Made up of identification, control, audit, and status accounting.")),
        ("버전관리(VCS)", "Version Control System", ("서가를 실제로 운영하는 도구.", "The tool that actually runs the shelf."), ("Git 같은 도구가 대표적이에요.", "Git is the best-known example.")),
        ("베이스라인", "Baseline", ("공식적으로 확정한 판.", "The edition officially locked in."), ("이후 변경은 전부 이 기준과 비교해요.", "Every later change is compared against this point.")),
        ("브랜치", "Branch", ("실험용 사본이 갈라져 나온 가지.", "A branch where an experimental copy forks off."), ("원본을 건드리지 않고 따로 고쳐 봐요.", "Lets you try changes without touching the original.")),
        ("병합(merge)", "Merge", ("실험이 끝나면 다시 합치는 일.", "Folding the branch back in once it works."), ('자동 배포까지 이어지면 → <a href="gitops-ko.html">서고 자체가 운영 기준이 되는 방식</a>.', 'When this extends into automatic deployment → <a href="gitops-en.html">using the shelf itself as the operating source of truth</a>.')),
        ("롤백(rollback)", "Rollback", ("예전 판을 그대로 꺼내 쓰는 일.", "Pulling an old edition back out, as-is."), ('문제가 생기면 이전 칸으로 되돌려요 → <a href="rollback-ko.html">놀이공원 세계의 되돌리기</a>.', 'If something breaks, step back to the earlier slot → <a href="rollback-en.html">the rewind in the theme-park world</a>.')),
        ("형상통제위원회(CCB)", "Change Control Board", ("어떤 변경을 받아들일지 결정하는 모임.", "The group that decides which changes get accepted."), ("중요한 변경은 아무나 서가에 바로 꽂지 못해요.", "Important changes can't just be slotted in by anyone.")),
        ("형상감사", "Configuration Audit", ("서가가 기준대로 정리됐는지 확인하는 일.", "Checking the shelf is organized to standard."), ('감리가 점검하는 항목 중 하나예요 → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>.', 'One of the things audit checks → <a href="pmoaudit-en.html">the last checker before publication</a>.')),
    ],
}
