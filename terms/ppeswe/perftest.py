from _draw import *
from _world import *

# 1. 신간 발매일, 독자가 몰려 인쇄가 늦어짐
P1 = svg(300, sky(300)
         + person(140, 170, s=0.6, face=EYES, **READER) + person(180, 170, s=0.6, face=EYES, **READER)
         + person(220, 170, s=0.6, face=EYES, **READER) + person(260, 170, s=0.6, face=FROWN, **READER)
         + printplate(380, 130, 0.9, label_text="⟦인쇄가 밀렸어요|printing is backed up⟧")
         + person(540, 150, s=0.8, face=SWEAT + EYES, **PRINTER)
         + label(380, 30, "⟦신간 발매일, 독자가 한꺼번에 몰려요|release day — readers all show up at once⟧", 13, "var(--ink)")
         + label(380, 270, "⟦평소엔 멀쩡하던 인쇄소가 오늘따라 느려요|the print shop, usually fine, is slow today of all days⟧", 12, "var(--ink)"))

# 2. 왜 터졌는지 모르면 또 터짐
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=FROWN, **PRINTER)
         + bubble(140, 70, 220, 40, "⟦한두 명일 땐 멀쩡했는데요?|it was fine with just a few people?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=SWEAT + EYES, **EDITOR)
         + bubble(440, 70, 240, 40, "⟦얼마나 몰려야 멈추는지 몰라서 또 터질까 무서워요|not knowing how much load breaks it, I'm scared it'll happen again⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦미리 몰려보지 않으면, 한계가 어딘지 아무도 몰라요|without trying the rush ahead of time, nobody knows where the limit is⟧", 12, "var(--ink)"))

# 3. 성능테스트 = 미리 가짜로 몰려보는 연습 (hero)
P3 = svg(340, sky(340)
         + person(200, 140, s=0.85, face=EYES, **PROOFER)
         + person(140, 170, s=0.5, face="", shirt="#8AA6C1") + person(170, 175, s=0.5, face="", shirt="#8AA6C1")
         + person(200, 170, s=0.5, face="", shirt="#8AA6C1") + person(230, 175, s=0.5, face="", shirt="#8AA6C1")
         + label(190, 240, "⟦가짜 독자들(테스트용)|pretend readers (for testing)⟧", 11, "var(--muted)")
         + printplate(480, 160, 1.0) + person(480, 120, s=0.75, face=EYES, **PRINTER)
         + label(380, 30, "⟦성능테스트 = 미리 손님을 가짜로 몰리게 해서 얼마나 버티는지 보는 연습|performance testing = sending in pretend readers ahead of time, to see how much it can take⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦진짜 독자가 몰리기 전에, 한계를 미리 찾아둬요|finding the limit before real readers ever show up⟧", 12, "var(--muted)"))

# 4. 네 가지 측정 지표
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦측정표|MEASUREMENTS⟧",
                      ("⟦응답시간 — 책 한 권 받기까지|response time — how long for one book⟧",
                       "⟦처리량(TPS) — 시간당 몇 권|throughput (TPS) — books per hour⟧",
                       "⟦동시 독자 수 — 몇 명까지 버티나|concurrent readers — how many at once⟧",
                       "⟦오류율 — 못 받은 독자 비율|error rate — share who got nothing⟧"), 1.0)
         + person(560, 160, s=0.8, face=EYES, **PROOFER)
         + label(560, 260, "⟦숫자로 버티는 선을 그어요|drawing the line with numbers⟧", 11, "var(--muted)")
         + label(380, 300, "⟦이 네 숫자가 '얼마나 몰려야 멈추는지'를 말해줘요|these four numbers say exactly how much load it takes to break⟧", 12, "var(--ink)"))

# 5. 시험 환경과 실제는 다를 수 있음
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **PROOFER)
         + label(190, 240, "⟦가짜 독자로는 통과했어요|it passed with pretend readers⟧", 11, "var(--ink)")
         + person(570, 150, s=0.7, face=EYES, **READER) + person(600, 155, s=0.6, face=EYES, **READER)
         + label(570, 260, "⟦진짜 독자는 패턴이 달라요|real readers show up in different patterns⟧", 11, "var(--ink)")
         + label(380, 282, "⟦테스트 환경이 실제와 다르면, 결과도 완전히 같진 않아요|if the test setup differs from the real one, the result isn't a perfect guarantee⟧", 12, "var(--ink)", cls="d"))

LOAD_I = icon('<circle cx="22" cy="32" r="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="42" cy="32" r="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="32" cy="18" r="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>')
STRESS_I = icon('<path d="M18 46 L32 14 L46 46 Z" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 26 v10 M32 40 v2" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
SOAK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 v14 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SPIKE_I = icon('<path d="M10 46 h10 l8 -30 l8 30 l8 -16 l8 16 h10" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "perftest", "order": 23,
    "title": ("미리 몰려보는 가짜 독자들", "The Pretend Readers Who Rush In Early"),
    "h1": ("<em>SW 성능테스트</em>가 뭐예요?", "What is <em>Performance Testing</em>?"),
    "sub": ("소프트웨어 성능테스트를, 신간 발매 전 가짜 독자들을 미리 몰리게 해보는 출판사 연습으로 풀어봤어요.",
            "Software performance testing, told as a story about a publishing house sending in pretend readers before a book even launches."),
    "panels": [
        {"svg": P1, "alt": ("신간 발매일에 독자가 몰려 인쇄소가 진땀을 흘림", "On release day readers rush in and the print shop sweats under the load"),
         "caption": ("신간 발매일, 독자가 한꺼번에 몰려요.", "On release day, readers all show up at once."),
         "small": ("평소엔 멀쩡하던 인쇄소가 오늘따라 느려요.", "The print shop, usually fine, is slow today of all days.")},
        {"svg": P2, "hero": False, "alt": ("인쇄 감독과 편집장이 한계가 어디인지 몰라 불안해함", "The print supervisor and editor worry because they don't know where the limit is"),
         "caption": ("미리 몰려보지 않으면 한계가 어딘지 아무도 몰라요.", "Without trying the rush ahead of time, nobody knows where the limit is."),
         "small": ("얼마나 몰려야 멈추는지 몰라서, 또 터질까 무서워요.", "Not knowing how much load it takes to break, everyone fears it'll happen again.")},
        {"svg": P3, "hero": True, "alt": ("가짜 독자 무리가 인쇄소로 몰려가고 교정자가 지켜봄", "A crowd of pretend readers rushes toward the print shop while a proofreader watches"),
         "caption": ("성능테스트는 미리 가짜로 몰리게 해보는 연습이에요.", "Performance testing sends in pretend readers ahead of time to see how much it can take."),
         "small": ("진짜 독자가 몰리기 전에 한계를 미리 찾아둬요.", "It finds the limit before real readers ever show up."),
         "tricks": (4, [
             (LOAD_I, ("부하테스트", "Load test"), ("평소 수준으로 몰려봐요", "rush in at the usual level"), "calm"),
             (STRESS_I, ("스트레스테스트", "Stress test"), ("한계까지 밀어붙여요", "push all the way to the limit"), "warm"),
             (SOAK_I, ("지속테스트", "Endurance (soak) test"), ("오래오래 계속 몰려봐요", "keep it up for a long stretch")),
             (SPIKE_I, ("스파이크테스트", "Spike test"), ("갑자기 몰렸다 빠져요", "a sudden burst, then it drops")),
         ])},
        {"svg": P4, "alt": ("응답시간·처리량·동시 독자 수·오류율 네 가지 측정표", "A measurement sheet: response time, throughput, concurrent readers, error rate"),
         "caption": ("성능테스트는 이 네 숫자를 재요.", "Performance testing measures these four numbers."),
         "small": ("이 숫자들이 '얼마나 몰려야 멈추는지'를 말해줘요.", "These numbers say exactly how much load it takes to break.")},
        {"svg": P5, "alt": ("왼쪽: 가짜 독자로는 통과함. 오른쪽: 진짜 독자는 패턴이 다름", "Left: it passed with pretend readers. Right: real readers show up differently"),
         "caption": ("테스트 환경과 실제는 다를 수 있어요.", "The test setup and the real world can differ."),
         "small": ("환경이 다르면 결과도 완전한 보장은 아니에요.", "If the setup differs, the result isn't a perfect guarantee.")},
    ],
    "summary": (("<b>SW 성능테스트</b>는 진짜 독자가 몰리기 전에 <b>가짜로 몰리게 해보며</b>, 응답시간·처리량 같은 숫자로 <b>버티는 한계</b>를 미리 찾는 일이에요.",
                 "<b>Software performance testing</b> sends in a pretend rush before real users ever arrive, measuring numbers like response time and throughput to find <b>the breaking point</b> ahead of time."),
                ("성능테스트는 시스템이 정해진 부하에서 응답시간·처리량(TPS)·동시 사용자 수·오류율 같은 지표를 만족하는지 확인하는 테스트예요. 평소 수준으로 확인하는 부하테스트, 한계까지 밀어붙이는 스트레스테스트, 오래 지속해보는 지속(내구성)테스트, 갑작스런 급증을 보는 스파이크테스트로 나눠요.",
                 "Performance testing checks whether a system meets metrics like response time, throughput (TPS), concurrent users, and error rate under a given load. It splits into load testing (typical levels), stress testing (pushed to the limit), endurance/soak testing (sustained over time), and spike testing (sudden bursts).")),
    "glossary": [
        ("성능테스트", "Performance Testing", ("가짜 독자로 미리 몰려보기.", "Rushing in pretend readers ahead of time."), ("한계를 미리 찾는 게 목적이에요.", "The goal is finding the limit early.")),
        ("부하테스트", "Load Test", ("평소 수준으로 몰려보기.", "Rushing in at the usual level."), ("정상 범위에서 버티는지 봐요.", "Checks it holds up under normal range.")),
        ("스트레스테스트", "Stress Test", ("한계까지 밀어붙이기.", "Pushing all the way to the limit."), ("어디서 무너지는지 찾아요.", "Finds exactly where it breaks.")),
        ("응답시간", "Response Time", ("책 한 권 받기까지 걸리는 시간.", "How long it takes to get one book."), ("독자가 체감하는 속도예요.", "What readers actually feel as speed.")),
        ("처리량(TPS)", "Throughput (TPS)", ("시간당 몇 권 찍어내나.", "How many books printed per hour."), ('기능점수로 규모를 먼저 재기도 해요. → <a href="fpruler-ko.html">매수를 재는 자</a>', 'Project size is sometimes gauged first with function points. → <a href="fpruler-en.html">the ruler that measures page count</a>')),
        ("병목지점", "Bottleneck", ("가장 먼저 막히는 좁은 문.", "The narrow door that jams up first."), ("테스트로 미리 찾아둬야 해요.", "Testing finds it before it's too late.")),
        ("가설검정", "Hypothesis Testing", ("두 표지 중 뭐가 진짜 더 잘 팔리는지 따지는 법.", "How to tell which of two covers truly sells better."), ('우연인지 진짜 차이인지 가릴 때 써요. → <a href="hypothesistest-ko.html">우연인지 진짜 차이인지 가리기</a>', 'Used to separate real differences from coincidence. → <a href="hypothesistest-en.html">telling a real difference from coincidence</a>')),
        ("고가용성", "High Availability", ("인쇄소를 두 곳 두는 대비.", "Keeping a backup print shop ready."), ('성능이 아니라 멈추지 않는 것에 대한 이야기예요(다른 세계). → <a href="failover-ko.html">예비 발전기가 넘겨받는 이야기</a>', 'A different story — about never stopping, not about speed (another world). → <a href="failover-en.html">when the spare generator takes over</a>')),
    ],
}
