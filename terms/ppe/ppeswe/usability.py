from _draw import *
from _world import *


def stopwatch(x, y, s=1.0, color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<path d="M0 -8 v8 l6 4" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>'
            f'<rect x="-4" y="-28" width="8" height="8" rx="2" fill="{color}"/></g>')


# 1. 오탈자 0건인데 독자는 목차를 못 찾아요
P1 = svg(300, sky(300)
         + person(200, 150, s=0.85, face=SMILE, **PROOFER) + inkstamp(200, 240, 0.5)
         + label(200, 285, "⟦오탈자 0건!|zero typos!⟧", 11, "var(--good)")
         + person(560, 160, s=0.8, face=FROWN + SWEAT, **READER) + manuscript(560, 220, 0.7)
         + label(560, 280, "⟦근데 목차를 못 찾겠어요|but I can't find the table of contents⟧", 11, "var(--bad)")
         + label(380, 30, "⟦오탈자 0건인데 독자는 헤매고 있어요|zero typos, and the reader is still lost⟧", 13, "var(--ink)"))

# 2. 편집팀은 당연히 쓰기 편할 거라 짐작만 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(380, 150, s=0.9, face=EYES, **EDITOR)
         + label(380, 70, "⟦이 정도면 당연히 잘 읽히겠지|surely this reads fine, right?⟧", 12, "var(--muted)")
         + label(380, 240, "⟦독자가 직접 넘겨보는 걸 본 적은 없어요|no one has watched a real reader flip through it⟧", 13, "var(--ink)")
         + label(380, 275, "⟦짐작과 실제는 자주 달라요|the guess and the reality often differ⟧", 12, "var(--bad)"))

# 3. 사용성평가 = 독자에게 설명 없이 책을 줘보고 지켜보기 (hero)
P3 = svg(340, sky(340)
         + person(260, 110, s=0.85, face=EYES, **READER) + manuscript(260, 200, 0.7)
         + person(500, 90, s=0.7, face=EYES, **PROOFER) + stopwatch(560, 60, 0.9)
         + label(380, 25, "⟦사용성평가 = 설명 없이 책을 줘보고, 어디서 헤매는지 그냥 지켜보는 시험|a usability test = handing over the book with no instructions, and simply watching where they get stuck⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦잘했는지 못했는지 평가가 아니라, 책이 쓰기 편한지를 봐요|not grading the reader — checking whether the book itself is easy to use⟧", 11, "var(--muted)"))

LEARN_I = icon('<path d="M12 44 L32 16 L52 44" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="32" cy="16" r="5" fill="var(--good)"/>')
SPEED_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 32 L44 22" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
RECALL_I = icon('<path d="M16 20 a16 16 0 1 1 -2 20" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M12 16 l2 8 l8 -2" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
HAPPY_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="24" cy="28" r="2.5" fill="var(--accent)"/><circle cx="40" cy="28" r="2.5" fill="var(--accent)"/><path d="M22 38 Q32 46 42 38" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. 관찰 기록표
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 230, "⟦관찰 기록표|OBSERVATION LOG⟧",
                      ("⟦걸린 시간 — 몇 분 만에 찾았나|time taken — how many minutes?⟧",
                       "⟦헤맨 지점 — 어디서 멈췄나|where they stalled⟧",
                       "⟦도움 요청 — 몇 번 물어봤나|how many times they asked for help⟧",
                       "⟦만족도 — 끝나고 기분은|satisfaction afterward⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **PROOFER) + stopwatch(620, 100, 0.6)
         + label(380, 300, "⟦독자 한 명 한 명을 그냥 조용히 지켜보며 적어요|quietly watching and noting each reader, one at a time⟧", 12, "var(--ink)"))

# 5. 사용성평가는 오탈자를 잡는 일이 아니에요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **PROOFER) + inkstamp(190, 230, 0.5) + label(190, 270, "⟦교정 — 오탈자가 없나|proofing — any typos?⟧", 11, "var(--ink)")
         + person(570, 125, s=0.8, face=EYES, **READER) + label(570, 265, "⟦사용성평가 — 쓰기 편한가|usability — is it easy to use?⟧", 11, "var(--ink)")
         + label(380, 300, "⟦옳고 그름이 아니라, 편한지 아닌지를 보는 거라 교정과는 역할이 달라요|it checks ease of use, not right or wrong — a different job from proofing⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "usability", "order": 46,
    "title": ("독자가 책을 쓱 넘겨보는 시험", "The Test Where a Reader Just Tries the Book Cold"),
    "h1": ("<em>사용성평가(Usability)</em>가 뭐예요?", "What is a <em>Usability</em> Test?"),
    "sub": ("사용성평가를, 설명 없이 책을 건네고 독자가 어디서 헤매는지 조용히 지켜보는 이야기로 풀어봤어요.",
            "Usability testing, told as a story about handing over a book with no instructions and quietly watching where a reader gets stuck."),
    "panels": [
        {"svg": P1, "alt": ("교정자는 오탈자 0건을 자랑하지만, 독자는 목차를 못 찾아 헤맴", "The proofreader is proud of zero typos, but the reader can't find the table of contents"),
         "caption": ("오탈자 0건인데 독자는 헤매고 있어요.", "Zero typos, and the reader is still lost."),
         "small": ("오탈자 없음과 쓰기 편함은 서로 다른 이야기예요.", "No typos and easy to use are two different things.")},
        {"svg": P2, "alt": ("편집장이 책상에서 당연히 잘 읽힐 거라 짐작만 함", "The editor assumes at a desk that it will surely read fine"),
         "caption": ("편집팀은 당연히 쓰기 편할 거라 짐작만 해요.", "The editorial team just assumes it'll be easy to use."),
         "small": ("독자가 직접 넘겨보는 걸 본 적은 없어요.", "No one has actually watched a reader flip through it.")},
        {"svg": P3, "hero": True, "alt": ("독자가 설명 없이 책을 넘겨보고, 교정자가 시계를 들고 조용히 지켜봄", "A reader flips through the book with no instructions, while a proofreader quietly watches with a stopwatch"),
         "caption": ("사용성평가는 설명 없이 책을 줘보고, 어디서 헤매는지 지켜보는 시험이에요.", "A usability test hands over the book with no instructions and simply watches where the reader gets stuck."),
         "small": ("독자를 평가하는 게 아니라, 책이 쓰기 편한지를 봐요.", "It's not grading the reader — it's checking whether the book itself is easy to use."),
         "tricks": (4, [
             (LEARN_I, ("학습 용이성", "Learnability"), ("처음 봐도 금방 쓰는 법을 알아요", "figures out how to use it right away"), "calm"),
             (SPEED_I, ("효율성", "Efficiency"), ("원하는 걸 빨리 찾아요", "finds what they want quickly")),
             (RECALL_I, ("기억 용이성", "Memorability"), ("나중에 다시 봐도 안 헤매요", "doesn't get lost coming back later"), "warm"),
             (HAPPY_I, ("만족도", "Satisfaction"), ("읽고 나서 기분이 좋아요", "feels good after using it")),
         ])},
        {"svg": P4, "alt": ("관찰 기록표: 걸린 시간·헤맨 지점·도움 요청·만족도를 교정자가 조용히 기록함", "An observation log: time taken, where they stalled, help requests, satisfaction — quietly recorded"),
         "caption": ("독자 한 명 한 명을 조용히 지켜보며 기록해요.", "Each reader is quietly watched and logged, one at a time."),
         "small": ("걸린 시간, 헤맨 지점, 도움 요청, 만족도를 적어요.", "Time taken, where they stalled, help requests, satisfaction.")},
        {"svg": P5, "alt": ("왼쪽: 교정은 오탈자를 봄. 오른쪽: 사용성평가는 쓰기 편한지를 봄", "Left: proofing checks for typos. Right: usability testing checks ease of use"),
         "caption": ("사용성평가는 오탈자를 잡는 일이 아니에요.", "Usability testing isn't about catching typos."),
         "small": ("옳고 그름이 아니라, 편한지 아닌지를 봐요.", "It checks ease of use, not right or wrong.")},
    ],
    "summary": (("<b>사용성평가</b> = 독자에게 책을 <b>그대로 줘보고</b>, 설명 없이 <b>어디서 헤매는지</b> 조용히 지켜보는 시험.",
                 "<b>Usability testing</b> means <b>handing the book over as-is</b> and quietly watching <b>where the reader gets stuck</b>, with no instructions given."),
                ("사용성평가는 실제 사용자가 제품을 사용하는 모습을 관찰해 학습 용이성·효율성·기억 용이성·오류·만족도 등을 평가하는 방법이에요. 오탈자나 기능 오류를 잡는 품질보증(QA)과 달리, '맞는지'가 아니라 '쓰기 편한지'를 판단하는 사용자 중심 평가예요.",
                 "Usability testing observes real users as they use a product, assessing learnability, efficiency, memorability, errors, and satisfaction. Unlike QA, which catches typos and functional bugs, it's a user-centered evaluation of whether something is easy to use — not whether it's correct.")),
    "glossary": [
        ("사용성평가", "Usability Test", ("설명 없이 써보게 하고 지켜보는 시험.", "A test that hands something over with no instructions and watches."), ("책이 쓰기 편한지를 봐요.", "It checks whether the thing itself is easy to use.")),
        ("학습 용이성(Learnability)", "Learnability", ("처음 봐도 금방 쓰는 법을 아는 정도.", "How quickly someone figures out how to use it the first time."), ("설명서 없이도 통하는 게 좋아요.", "Ideally it works without a manual.")),
        ("효율성(Efficiency)", "Efficiency", ("원하는 걸 얼마나 빨리 찾는지.", "How fast someone finds what they want."), ("걸린 시간으로 재요.", "Measured by time taken.")),
        ("기억 용이성(Memorability)", "Memorability", ("나중에 다시 써도 안 헤매는 정도.", "How little someone struggles coming back later."), ("오랜만에 봐도 금방 떠올라요.", "It comes back quickly even after a long gap.")),
        ("만족도(Satisfaction)", "Satisfaction", ("쓰고 난 뒤의 기분.", "How someone feels after using it."), ("설문이나 인터뷰로 물어봐요.", "Usually gathered with a survey or interview.")),
        ("오류율(Errors)", "Errors", ("쓰다가 실수하는 횟수와 심각도.", "How often mistakes happen, and how serious they are."), ("다섯 번째 속성으로 자주 같이 봐요.", "Often tracked as a fifth attribute alongside the rest.")),
        ("교정(QA)", "QA / Proofing", ("오탈자와 기능 오류를 잡는 일.", "Catching typos and functional mistakes."), ("'맞는지'를 보는 거라, '편한지'를 보는 사용성평가와 역할이 달라요.", "It checks correctness — a different job from usability, which checks ease of use.")),
        ("SW 품질인증", "Software Quality Certification", ("심사표 항목 중 하나가 사용성이에요.", "Usability is one line item on a bigger checklist."), ('→ <a href="swcert-ko.html">책 표지의 공식 마크</a>', '→ <a href="swcert-en.html">the official mark on the cover</a>')),
    ],
}
