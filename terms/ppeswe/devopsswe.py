from _draw import *
from _world import *

# 1. 작가가 담장 너머로 원고를 던져요
P1 = svg(300, sky(300, ground=False)
         + '<rect x="0" y="170" width="760" height="130" fill="var(--stone)"/><rect x="330" y="60" width="26" height="140" fill="var(--stone-dark)"/>'
         + person(180, 150, s=0.8, face=SMILE, **WRITER) + bubble(90, 60, 190, 40, "⟦완성! 다 됐어요!|done! all finished!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + manuscript(300, 150, 0.6) + '<path d="M300 150 q40 -30 80 0" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
         + person(580, 150, s=0.8, face=FROWN, **PRINTER) + bubble(480, 60, 220, 40, "⟦이대로는 인쇄가 안 되는데요?|this can't be printed as it is?⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 280, "⟦담장 너머로 던지면, 문제는 받은 쪽에서야 드러나요|throw it over the wall, and problems only surface on the other side⟧", 12, "var(--bad)"))

# 2. 책임이 나뉘면 발견이 늦어져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=EYES, **WRITER) + bubble(120, 70, 200, 40, "⟦글만 잘 쓰면 제 할 일은 끝이죠|once the writing's good, my part's done⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **PRINTER) + bubble(450, 70, 230, 40, "⟦저는 받은 대로 찍을 뿐이에요|I just print whatever I'm handed⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦각자 자기 몫만 생각하면, 문제는 맨 마지막에야 드러나요|each watching only their own part — problems surface only at the very end⟧", 12, "var(--ink)"))

# 3. DevOps = 담장을 허물고 작게 자주 같이 찍어내기 (hero)
WALL_I = icon('<rect x="10" y="30" width="44" height="26" fill="var(--stone-dark)"/><path d="M14 18 L32 8 L50 18" stroke="var(--stone-dark)" stroke-width="6" fill="none" stroke-linejoin="round"/><path d="M22 40 l6 6 l14 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SMALLBATCH_I = icon('<rect x="8" y="26" width="12" height="18" rx="2" fill="var(--good)"/><rect x="26" y="26" width="12" height="18" rx="2" fill="var(--good)"/><rect x="44" y="26" width="12" height="18" rx="2" fill="var(--good)"/>')
AUTOLINE_I = icon('<rect x="6" y="40" width="52" height="8" rx="4" fill="var(--stone-dark)"/><rect x="20" y="20" width="24" height="16" rx="3" fill="var(--good)"/><path d="M27 28 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
SHARED_I = icon('<circle cx="22" cy="24" r="9" fill="var(--accent)"/><circle cx="42" cy="24" r="9" fill="var(--good)"/><path d="M32 34 v18" stroke="var(--ink)" stroke-width="4"/><circle cx="32" cy="56" r="5" fill="var(--ink)"/>')

P3 = svg(340, sky(340, ground=False)
         + '<rect x="0" y="200" width="760" height="140" fill="var(--stone)"/>'
         + label(380, 30, "⟦DevOps = 담장을 허물고 작게 자주 같이 찍어내기|DevOps = tearing down the wall and printing together, in small frequent runs⟧", 13, "var(--ink)", cls="d")
         + person(230, 170, s=0.8, face=SMILE, **WRITER) + person(340, 170, s=0.8, face=SMILE, **PRINTER)
         + manuscript(230, 300, 0.55) + printplate(340, 300, 0.5)
         + '<path d="M250 298 Q290 268 325 298" stroke="var(--good)" stroke-width="3" fill="none" stroke-dasharray="6 4"/>'
         + label(380, 328, "⟦작가와 인쇄소가 담장 없이 나란히 서서, 작은 묶음을 자주 주고받아요|writer and printer stand side by side, with no wall, trading small batches often⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "devopsswe", "order": 20,
    "title": ("담장을 허문 작가와 인쇄소", "The Writer and the Printer, With No Wall Between Them"),
    "h1": ("<em>DevOps</em>가 뭐예요?", "What is <em>DevOps</em>?"),
    "sub": ("DevOps를, 작가와 인쇄소 사이 담장을 허물고 작은 묶음을 자주 주고받는 이야기로 풀어봤어요.",
            "DevOps, told as a story about tearing down the wall between the writer and the printer, and trading small batches often instead."),
    "panels": [
        {"svg": P1, "alt": ("작가가 담장 너머로 원고를 던지고 '완성!' 외치고, 인쇄소는 받아보고서야 '이대로는 인쇄가 안 되는데요' 라고 찡그림", "A writer tosses a manuscript over a wall shouting done, and the printer frowns only after catching it: this can't be printed as it is"),
         "caption": ("작가가 담장 너머로 원고를 던져요.", "The writer throws the manuscript over the wall."),
         "small": ("담장 너머로 던지면, 문제는 받은 쪽에서야 드러나요.", "Throw it over the wall, and problems only surface on the other side.")},
        {"svg": P2, "alt": ("작가는 글만 쓰면 끝이라 말하고, 인쇄소는 받은 대로 찍을 뿐이라 말함", "The writer says once the writing's done their part is finished; the printer says they just print whatever they're handed"),
         "caption": ("책임이 나뉘면 발견이 늦어져요.", "When responsibility is split, problems get caught too late."),
         "small": ("각자 자기 몫만 생각하면, 문제는 맨 마지막에야 드러나요.", "Each watching only their own part — problems surface only at the very end.")},
        {"svg": P3, "hero": True, "alt": ("담장이 사라진 자리에 작가와 인쇄소가 나란히 서서 작은 원고와 인쇄판을 주고받음", "Where the wall used to stand, the writer and printer stand side by side, trading a small manuscript and a print plate"),
         "caption": ("DevOps는 담장을 허물고 작게 자주 같이 찍어내는 거예요.", "DevOps tears down the wall and prints together in small, frequent runs."),
         "small": ("작가와 인쇄소가 담장 없이 나란히 서서, 작은 묶음을 자주 주고받아요.", "Writer and printer stand side by side, with no wall, trading small batches often."),
         "tricks": (4, [
             (WALL_I, ("담장 허물기", "Tear down the wall"), ("따로 일하던 둘이 한 팀이 돼요", "two separate teams become one"), "calm"),
             (SMALLBATCH_I, ("작게, 자주 내기", "Ship small, ship often"), ("큰 묶음 대신 조금씩 자주 찍어요", "small frequent runs instead of one big one")),
             (AUTOLINE_I, ("자동 인쇄라인", "Automate the line"), ("확인과 찍기를 자동으로 이어요", "checking and printing run automatically")),
             (SHARED_I, ("같이 책임지기", "Share the responsibility"), ("문제가 생기면 둘이 같이 고쳐요", "when something breaks, both fix it together"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 320, 260, "⟦옛날 방식|THE OLD WAY⟧",
                                 ("⟦분기에 한 번, 큰 묶음|once a quarter, one big batch⟧",
                                  "⟦인쇄소가 받고서야 문제 발견|the printer finds problems only after receiving it⟧",
                                  "⟦고치는 데 몇 주|fixing it takes weeks⟧"), 1.0)
                    + styleguide(380, 30, 320, 260, "⟦DevOps 방식|THE DEVOPS WAY⟧",
                                 ("⟦매일, 작은 묶음|every day, small batches⟧",
                                  "⟦찍기 전에 자동으로 확인|checked automatically before printing⟧",
                                  "⟦고치는 데 몇 분|fixing it takes minutes⟧"), 1.0)),
         "alt": ("왼쪽: 분기에 한 번 큰 묶음을 내는 옛날 방식. 오른쪽: 매일 작은 묶음을 자동 확인 후 내는 DevOps 방식", "Left: the old way of shipping one big batch per quarter. Right: the DevOps way of shipping small, auto-checked batches daily"),
         "caption": ("묶음을 작게 쪼개면, 문제도 작게 쪼개져요.", "Split the batch smaller, and the problems get smaller too."),
         "small": ("자주 낼수록 한 번에 고칠 분량이 줄어서, 고치는 시간도 짧아져요.", "The more often you ship, the less there is to fix each time — so fixes take less time too.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.8, face=SMILE, **WRITER) + label(190, 265, "⟦이제 같이 일해요|now we work together⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.8, face=EYES, **PRINTER) + label(560, 265, "⟦그래도 경비는 따로 필요해요|but we still need a guard, separately⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦담장을 허문다고 전부 해결되진 않아요|tearing down the wall doesn't solve everything⟧", 13, "var(--bad)", cls="d")),
         "alt": ("작가는 이제 같이 일한다고 웃고, 인쇄 감독은 그래도 경비는 따로 필요하다고 말함", "The writer smiles that they now work together; the print supervisor says a guard is still needed, separately"),
         "caption": ("담장을 허문다고 전부 해결되진 않아요.", "Tearing down the wall doesn't solve everything."),
         "small": ('빠르게 같이 찍어내도, 보안까지 저절로 챙겨지진 않아요. 경비까지 같이 세우는 건 → <a href="devsecops-ko.html">짓는 동안 같이 보는 목수와 경비</a> 쪽 이야기예요.',
                   'Printing fast together doesn\'t automatically take care of security. Bringing a guard into that too is a different story → <a href="devsecops-en.html">the builder and the guard, side by side</a>.')},
    ],
    "summary": (("<b>DevOps</b> = 작가(개발)와 인쇄소(운영) 사이 <b>담장을 허물고</b>, <b>작은 묶음을 자주</b> 자동화된 라인으로 함께 찍어내는 문화·방식.",
                 "<b>DevOps</b> = tearing down the <b>wall</b> between the writer (dev) and the printer (ops), and printing together in <b>small, frequent, automated</b> batches."),
                ("DevOps는 개발(Dev)과 운영(Ops)을 분리된 조직으로 두지 않고 하나의 팀으로 묶어, 지속적 통합(CI)과 지속적 배포(CD)를 통해 작은 변경을 자주, 자동화된 파이프라인으로 내보내는 문화이자 방법론이에요. 성과는 배포 빈도·변경 리드타임·변경 실패율·복구 시간 같은 지표로 가늠해요.",
                 "DevOps is a culture and set of practices that bring development (Dev) and operations (Ops) together as one team instead of separate silos, shipping small changes often through an automated pipeline of continuous integration (CI) and continuous delivery (CD). Success is measured with metrics like deployment frequency, change lead time, change failure rate, and recovery time.")),
    "glossary": [
        ("DevOps", "DevOps", ("담장을 허문 작가와 인쇄소.", "The writer and the printer, with no wall between them."), ("개발과 운영이 한 팀으로 묶여요.", "Development and operations become one team.")),
        ("지속적통합(CI)", "Continuous Integration", ("원고를 조금씩 자주 합치는 것.", "Merging manuscript changes often, in small pieces."), ("합칠 때마다 자동으로 확인해요.", "Every merge gets checked automatically.")),
        ("지속적배포(CD)", "Continuous Delivery/Deployment", ("확인된 원고를 자동으로 인쇄 라인에 올리는 것.", "Automatically feeding a checked manuscript onto the print line."), ("사람이 매번 수동으로 올리지 않아요.", "No one has to push it through by hand each time.")),
        ("무중단 배포 전략", "Zero-Downtime Deployment", ("서점 문을 닫지 않고 새 판으로 바꾸는 방법.", "Swapping in a new edition without closing the bookstore."), ('블루-그린, 카나리 같은 구체적 방법이 있어요 → <a href="bluegreen-ko.html">쌍둥이 기구를 번갈아 운영</a>, <a href="canary-ko.html">구석에서 몰래 하는 시험 운행</a>.', 'Specific methods include blue-green and canary → <a href="bluegreen-en.html">running twin rides, one at a time</a>, <a href="canary-en.html">a quiet test run in the corner</a>.')),
        ("인프라as코드(IaC)", "Infrastructure as Code", ("인쇄소 설비 설정까지 글로 적어 관리하는 것.", "Writing down the print shop's own setup as text, too."), ('설비도 원고처럼 버전관리할 수 있어요 → <a href="iac-ko.html">놀이공원 세계의 설계도 코드</a>.', 'The equipment itself can be version-controlled like a manuscript → <a href="iac-en.html">the blueprint-as-code in the theme-park world</a>.')),
        ("공동 책임 문화", "Shared Responsibility Culture", ("문제가 생기면 둘이 같이 고치는 태도.", "The attitude of fixing problems together, not pointing fingers."), ("'누구 탓'보다 '같이 해결'을 먼저 봐요.", "Puts 'let's fix it together' ahead of 'whose fault is it'.")),
        ("DORA 지표", "DORA Metrics", ("이 방식이 잘 되고 있는지 재는 네 가지 자.", "The four rulers that measure whether this is working."), ('배포 빈도·리드타임·실패율·복구시간이에요 → <a href="dorametrics-ko.html">네 가지 성과 지표</a>.', 'Deployment frequency, lead time, failure rate, and recovery time → <a href="dorametrics-en.html">the four performance metrics</a>.')),
        ("데브섹옵스", "DevSecOps", ("담장을 허문 자리에 경비까지 같이 세우는 것.", "Bringing a guard into the wall-free space too."), ('보안까지 처음부터 같이 보는 더 넓은 방식이에요 → <a href="devsecops-ko.html">짓는 동안 같이 보는 목수와 경비</a>.', 'The broader version that brings security in from the start, too → <a href="devsecops-en.html">the builder and the guard, side by side</a>.')),
    ],
}
