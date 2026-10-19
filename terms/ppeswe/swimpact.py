from _draw import *
from _world import *


def seriesbooks(x, y, s=1.0, hl=-1, bad=-1):
    """나란히 꽂힌 시리즈 책 세 권. hl 번째는 지금 고치는 책, bad 번째는 충돌이 생긴 책."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i in range(3):
        xx = i * 70
        c = "var(--accent)" if i == hl else ("var(--bad)" if i == bad else "#4A5A72")
        out += f'<rect x="{xx}" y="0" width="56" height="78" rx="4" fill="{c}"/><rect x="{xx + 8}" y="10" width="40" height="10" fill="#FFF8E7"/>'
        out += label(xx + 28, 96, f"⟦{i + 1}권|book {i + 1}⟧", 11, "var(--muted)")
    return out + "</g>"


# 1. 1권만 고쳤는데 2권에서 모순이 생겼어요
P1 = svg(300, sky(300)
         + seriesbooks(240, 110, 1.0, hl=0)
         + person(170, 180, s=0.7, face=SMILE, **WRITER) + label(170, 280, "⟦1권 설정만 살짝 고쳤어요|I only tweaked book 1's setting a bit⟧", 11, "var(--ink)")
         + person(560, 150, s=0.8, face=FROWN, **READER) + bubble(470, 70, 220, 40, "⟦2권이랑 얘기가 안 맞는데요?|this doesn't match book 2 anymore?⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 30, "⟦1권만 고쳤는데 2권에서 모순이 생겼어요|only book 1 changed, but now book 2 contradicts it⟧", 13, "var(--ink)", cls="d"))

# 2. 시리즈가 커질수록 연결이 안 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(380, 30, "⟦시리즈가 커질수록, 어디까지 연결됐는지 한눈에 안 보여요|the bigger the series, the harder it is to see how far the links reach⟧", 13, "var(--ink)", cls="d")
         + seriesbooks(70, 100, 0.85, bad=1) + seriesbooks(430, 100, 0.85, bad=2)
         + '<path d="M100 178 Q290 225 460 178" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
         + '<path d="M170 178 Q290 155 530 178" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
         + '<path d="M240 178 Q400 240 600 178" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
         + label(380, 280, "⟦손댈 때마다 뭐가 흔들릴지 아무도 몰라요|nobody knows what will shake loose with each change⟧", 12, "var(--bad)"))

# 3. 영향평가 = 고치기 전에 연결 지도를 그려보는 것 (hero)
LINK_I = icon('<circle cx="18" cy="32" r="9" fill="var(--accent)"/><circle cx="46" cy="18" r="9" fill="var(--good)"/><circle cx="46" cy="46" r="9" fill="var(--bad)"/><path d="M18 32 L46 18 M18 32 L46 46" stroke="var(--muted)" stroke-width="3"/>')
SCOPE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="6 4"/><circle cx="32" cy="32" r="8" fill="var(--accent)"/>')
GRADE_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--good)"/><rect x="27" y="26" width="10" height="28" fill="var(--accent)"/><rect x="42" y="12" width="10" height="42" fill="var(--bad)"/>')
STAKE_I = icon('<circle cx="22" cy="24" r="8" fill="var(--accent)"/><path d="M22 32 v16" stroke="var(--accent)" stroke-width="4"/><circle cx="44" cy="24" r="8" fill="var(--good)"/><path d="M44 32 v16" stroke="var(--good)" stroke-width="4"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦영향평가 = 고치기 전에 연결 지도를 그려보는 것|impact assessment = mapping the connections before you touch anything⟧", 13, "var(--ink)", cls="d")
         + seriesbooks(290, 110, 1.0, hl=0)
         + '<path d="M326 188 Q400 230 480 190" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + person(150, 210, s=0.6, face=EYES, **EDITOR) + label(150, 300, "⟦1권을 고치기 전에|before changing book 1⟧", 11, "var(--muted)")
         + person(640, 210, s=0.6, face=EYES, **PRINTER) + label(640, 300, "⟦어디까지 번지는지 먼저 봐요|first check how far it reaches⟧", 11, "var(--muted)"))

PAGE = {
    "slug": "swimpact", "order": 18,
    "title": ("고치기 전에 그려보는 연결 지도", "The Connection Map You Draw Before Changing Anything"),
    "h1": ("<em>SW사업 영향평가</em>가 뭐예요?", "What is a <em>Software Project Impact Assessment</em>?"),
    "sub": ("SW사업 영향평가를, 시리즈 1권을 고치기 전에 다른 책들에 어디까지 번질지 미리 그려보는 지도 이야기로 풀어봤어요.",
            "Impact assessment, told as a story about mapping how far a change to book one will ripple into the rest of the series before you make it."),
    "panels": [
        {"svg": P1, "alt": ("작가가 1권 설정만 고쳤다고 말하는데, 독자는 2권과 얘기가 안 맞는다고 찡그리며 말함", "A writer says they only tweaked book one's setting, while a reader frowns that it no longer matches book two"),
         "caption": ("1권만 고쳤는데 2권에서 모순이 생겼어요.", "Only book one changed, but now book two contradicts it."),
         "small": ("작은 설정 하나가 뒷이야기 전체에 번졌어요.", "One small setting change rippled through the rest of the story.")},
        {"svg": P2, "alt": ("점점 늘어나는 시리즈 책들 사이에 점선 연결선이 어지럽게 얽혀 있음", "A growing stack of series books with tangled dashed lines connecting them"),
         "caption": ("시리즈가 커질수록 연결이 안 보여요.", "The bigger the series, the harder it is to see the links."),
         "small": ("손댈 때마다 뭐가 흔들릴지 아무도 몰라요.", "Nobody knows what will shake loose with each change.")},
        {"svg": P3, "hero": True, "alt": ("편집장과 인쇄 감독이 1권을 고치기 전, 다른 책으로 이어지는 점선을 함께 확인함", "The editor and print supervisor check a dashed line from book one to the next book before making the change"),
         "caption": ("영향평가는 고치기 전에 연결 지도를 그려보는 거예요.", "Impact assessment maps the connections before you change anything."),
         "small": ("1권을 고치기 전에, 어디까지 번지는지 먼저 봐요.", "Before changing book one, first check how far it reaches."),
         "tricks": (4, [
             (LINK_I, ("연결점 찾기", "Find the connections"), ("이 변경이 어디로 이어지는지 찾아요", "trace where this change leads"), "calm"),
             (SCOPE_I, ("영향 범위 그리기", "Map the scope"), ("번질 수 있는 범위를 동그라미로 그려요", "circle how far it could spread")),
             (GRADE_I, ("위험 등급 매기기", "Grade the risk"), ("크게 번지는 건 더 높은 등급으로", "bigger ripples get a higher risk grade")),
             (STAKE_I, ("이해관계자 확인", "Check who's affected"), ("어느 독자층이 영향받는지 확인해요", "see which readers are affected"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 240, "⟦영향평가 매트릭스|IMPACT ASSESSMENT MATRIX⟧",
                                 ("⟦변경 대상: 1권 설정|change target: book 1's setting⟧",
                                  "⟦직접 영향: 2권 줄거리 — 위험 높음|direct impact: book 2's plot — high risk⟧",
                                  "⟦간접 영향: 3권 캐릭터 — 위험 중간|indirect impact: book 3's character — medium risk⟧",
                                  "⟦무관: 외전 — 위험 없음|unaffected: the side story — no risk⟧"), 1.0)),
         "alt": ("변경 대상과 직접·간접 영향, 무관한 부분을 나눠 적은 영향평가 매트릭스", "An impact matrix separating the change target, direct and indirect impact, and the unaffected part"),
         "caption": ("영향을 등급별로 나눠 적어요.", "Impact gets written down by grade."),
         "small": ("직접 영향, 간접 영향, 무관 — 이렇게 나누면 어디부터 손봐야 할지 보여요.", "Direct, indirect, and unaffected — sorted this way, it's clear where to start.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.8, face=EYES, **PRINTER) + label(190, 265, "⟦큰 사고는 막아줘요|it does stop the big accidents⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.8, face=SWEAT, **EDITOR) + label(560, 265, "⟦작은 수정까지 매번 하면 느려져요|do it for every tiny fix and things slow down⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦영향평가가 다 해결해주진 않아요|impact assessment doesn't solve everything⟧", 13, "var(--bad)", cls="d")
                    + label(380, 280, "⟦변경 규모에 맞춰, 얼마나 깊이 볼지 정해요|how deep you look should match the size of the change⟧", 12, "var(--muted)")),
         "alt": ("인쇄 감독은 영향평가가 큰 사고를 막아준다 말하고, 편집장은 작은 수정까지 매번 하면 느려진다고 땀 흘리며 말함", "The print supervisor says it stops big accidents; the sweating editor says doing it for every tiny fix slows things down"),
         "caption": ("영향평가가 다 해결해주진 않아요.", "Impact assessment doesn't solve everything."),
         "small": ('너무 자주 하면 느려지고, 너무 안 하면 사고가 나요. 적절한 기준은 → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>이 함께 정해요.',
                   "Do it too often and you slow down; too rarely and accidents happen. The right balance is set together with → <a href=\"pmoaudit-en.html\">the last checker before publication</a>.")},
    ],
    "summary": (("<b>SW사업 영향평가</b> = 시리즈 중 한 권을 고치기 전에, <b>다른 책들로 번질 범위와 위험</b>을 미리 그려보는 연결 지도.",
                 "<b>Software project impact assessment</b> = before changing one book in a series, drawing a connection map of <b>how far it spreads and how risky that is</b>."),
                ("SW사업 영향평가는 기존 정보시스템에 변경을 가하기 전, 그 변경이 연관된 업무·시스템·이해관계자에 미치는 영향의 범위와 크기를 분석하는 활동이에요. 직접 영향과 간접 영향을 나눠 위험 등급을 매기고, 그 결과로 변경 범위와 일정, 자원 배분을 조정해요.",
                 "A software project impact assessment analyzes, before changing an existing information system, how far and how severely that change reaches related work, systems, and stakeholders. It separates direct from indirect impact, assigns a risk grade, and uses the result to adjust the scope, schedule, and resourcing of the change.")),
    "glossary": [
        ("영향평가", "Impact Assessment", ("고치기 전에 그려보는 연결 지도.", "The connection map drawn before a change."), ("범위와 위험을 미리 가늠해요.", "Gauges scope and risk ahead of time.")),
        ("영향범위분석", "Impact Scope Analysis", ("번질 수 있는 범위를 동그라미로 그리는 일.", "Circling how far the ripple could reach."), ("직접·간접 영향을 나눠 봐요.", "Separates direct impact from indirect.")),
        ("이해관계자분석", "Stakeholder Analysis", ("어느 독자층이 영향받는지 확인하는 일.", "Checking which readers are affected."), ("누구에게 미리 알려야 할지 정해요.", "Decides who needs to be told in advance.")),
        ("추적성(Traceability)", "Traceability", ("요구사항부터 코드까지 이어지는 실.", "The thread running from requirement to code."), ("이 실이 있어야 영향 범위를 따라갈 수 있어요.", "Without this thread, you can't trace how far an impact runs.")),
        ("위험등급", "Risk Grade", ("번짐의 크기에 매기는 등급.", "The grade assigned to how big the ripple is."), ("높을수록 더 꼼꼼히 봐야 해요.", "The higher it is, the closer the review needs to be.")),
        ("회귀테스트", "Regression Testing", ("고친 뒤 멀쩡하던 곳도 다시 확인하는 일.", "Re-checking the parts that used to be fine, after a change."), ('영향평가에서 찾은 범위를 실제로 확인하는 단계예요.', 'The step that actually verifies the scope impact assessment identified.')),
        ("변경관리", "Change Management", ("고칠지 말지, 언제 고칠지 결정하는 절차.", "The process deciding whether and when to make the change."), ("영향평가 결과가 이 결정의 근거가 돼요.", "The impact assessment result is what this decision is based on.")),
        ("거버넌스", "Governance", ("누가 이런 결정을 승인하는지 정해놓은 틀.", "The framework for who approves this kind of decision."), ("큰 영향일수록 더 높은 선에서 승인받아요.", "The bigger the impact, the higher up it needs sign-off.")),
    ],
}
