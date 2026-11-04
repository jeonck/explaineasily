"""슈퍼앱(Super App)."""
from _draw import *
from _world import *

ALLIN_I = icon('<rect x="10" y="10" width="44" height="44" rx="8" fill="var(--accent)"/><path d="M22 32 h20 M32 22 v20" stroke="#FFF" stroke-width="4" stroke-linecap="round"/>')
DATA_I = icon('<circle cx="32" cy="32" r="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="5" fill="var(--accent)"/>')
WALL_I = icon('<rect x="10" y="20" width="44" height="30" rx="4" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M14 14 L50 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
LAW_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 24 h24 M20 32 h24 M20 40 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

# 1. 학생증 하나로 다 되는 앱을 만들었어요
P1 = svg(300, sky(300)
         + person(380, 130, s=0.9, face=SMILE, **PRESIDENT)
         + '<rect x="305" y="200" width="150" height="60" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + label(380, 225, "⟦학생증 앱|STUDENT ID APP⟧", 10, "var(--ink)", cls="d")
         + label(380, 245, "⟦급식 · 도서관 · 출석 · 포인트|lunch · library · roll call · points⟧", 9, "var(--muted)")
         + person(180, 160, s=0.7, face=SMILE, **STUDENT) + person(580, 160, s=0.7, face=SMILE, **STUDENT)
         + label(380, 290, "⟦학생들은 앱 하나로 다 되니 편하다고 좋아해요|students love having it all in one app⟧", 12, "var(--ink)", cls="d"))

# 2. 다른 가게는 들어올 수가 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="310" y="90" width="140" height="80" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>' + label(380, 135, "⟦학생증 앱|STUDENT ID APP⟧", 11, "var(--ink)", cls="d")
         + person(170, 150, s=0.75, face=FROWN, **REP) + bubble(70, 85, 200, 44, "⟦우리 매점도 넣어주세요|let our shop in too, please⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(590, 150, s=0.75, face=EYES, **PRESIDENT) + bubble(500, 85, 220, 44, "⟦여긴 저희가 고른 곳만 돼요|only shops we picked are allowed here⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦포인트는 이 앱 안에서만 쓸 수 있어서, 학생은 다른 가게를 고르기 어려워요|points only work inside this app, so students can't easily choose another shop⟧", 12, "var(--ink)", cls="d"))

# 3. 슈퍼앱 = 여러 서비스를 한 앱에 모은 것, 규칙도 운영자가 다 정함 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦슈퍼앱 = 여러 서비스를 한 앱에 모은 것 — 규칙도 운영자 혼자 정해요|a super app bundles many services into one — and its operator alone writes the rules⟧", 12, "var(--ink)", cls="d")
         + '<rect x="280" y="70" width="200" height="140" rx="12" fill="var(--panel)" stroke="var(--accent)" stroke-width="4"/>'
         + label(380, 100, "⟦학생증 앱|STUDENT ID APP⟧", 12, "var(--ink)", cls="d")
         + label(330, 130, "⟦급식|lunch⟧", 10, "var(--muted)") + label(430, 130, "⟦도서관|library⟧", 10, "var(--muted)")
         + label(330, 160, "⟦출석|roll call⟧", 10, "var(--muted)") + label(430, 160, "⟦포인트|points⟧", 10, "var(--muted)")
         + label(380, 190, "⟦동아리 신청|club sign-up⟧", 10, "var(--muted)")
         + person(170, 205, s=0.8, face=EYES, **PRESIDENT) + person(600, 205, s=0.75, face=SMILE, **STUDENT)
         + label(380, 320, "⟦편리하지만, 어떤 가게를 들일지 정하는 권한도 운영자 한 곳에만 있어요|convenient, but the power to decide who gets in sits with the operator alone⟧", 11, "var(--muted)"))

# 4. 편리함 vs 규제가 필요한 이유
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 30, 320, 240, "⟦편리한 점|WHAT'S CONVENIENT⟧", ("⟦앱 하나로 다 해결|one app solves it all⟧", "⟦다른 앱으로 옮길 필요 없음|no need to switch apps⟧", "⟦포인트가 한곳에 쌓임|points build up in one place⟧"), 1.0)
         + rulesboard(390, 30, 320, 240, "⟦규제가 필요한 이유|WHY REGULATION IS NEEDED⟧", ("⟦독점 — 경쟁 앱이 사라짐|monopoly — competing apps disappear⟧", "⟦끼워팔기 — 다른 서비스까지 묶어 강요|bundling — forcing add-on services⟧", "⟦데이터 집중 — 이용자 정보가 한곳에 모임|data concentration — user data pools in one place⟧"), 1.0, hl=0)
         + label(380, 295, "⟦편리함과 공정한 경쟁 사이에서 법이 균형을 잡으려 해요|the law tries to balance convenience against fair competition⟧", 12, "var(--ink)", cls="d"))

# 5. 너무 규제하면 편리함이 줄어요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, **TEACHER) + label(190, 260, "⟦공정한 경쟁 기준을 정해요|setting fair-competition rules⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=FROWN, **PRESIDENT) + label(570, 260, "⟦규제가 너무 세세하면 새 기능 넣기 힘들어요|too-detailed rules make new features hard to add⟧", 11, "var(--ink)")
         + label(380, 305, "⟦공정함과 자율성, 망중립성에서도 봤던 똑같은 줄다리기예요|fairness vs autonomy — the same tug-of-war seen with net neutrality⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "superapp", "order": 11,
    "title": ("학생증 하나로 다 되는 앱", "One Student-ID App That Does Everything"),
    "h1": ("<em>슈퍼앱</em>이 뭐예요?", "What is a <em>Super App</em>?"),
    "sub": ("슈퍼앱을, 학생회가 만든 학생증 앱 하나로 급식·도서관·출석·포인트가 다 되는 이야기로 풀어봤어요.",
            "Super apps, told as a story about a student-ID app the council built that handles lunch, library, roll call, and points all at once."),
    "panels": [
        {"svg": P1, "alt": ("학생회장이 급식·도서관·출석·포인트가 다 되는 학생증 앱을 들고 있고, 학생들이 좋아함", "The council president holds up a student-ID app for lunch, library, roll call, and points, and students love it"),
         "caption": ("학생회가 학생증 하나로 다 되는 앱을 만들었어요.", "The student council built one student-ID app that does everything."),
         "small": ("학생들은 앱 하나로 다 되니 편하다고 좋아해요.", "Students love having it all in one app.")},
        {"svg": P2, "alt": ("매점 대표가 입점을 부탁하지만 학생회장은 고른 곳만 된다고 답함", "A shop rep asks to be let into the app, but the president says only hand-picked shops are allowed"),
         "caption": ("학생회가 고른 곳이 아니면 다른 가게는 앱에 들어올 수 없어요.", "Shops the council didn't pick can't get into the app."),
         "small": ("포인트는 이 앱 안에서만 쓸 수 있어서, 학생은 다른 가게를 고르기 어려워요.", "Points only work inside this app, so students can't easily choose another shop.")},
        {"svg": P3, "hero": True, "alt": ("학생증 앱 하나에 급식·도서관·출석·포인트·동아리 신청이 다 모여 있음", "One student-ID app bundling lunch, library, roll call, points, and club sign-up all together"),
         "caption": ("슈퍼앱은 여러 서비스를 한 앱에 모은 것이에요.", "A super app bundles many services into one."),
         "small": ("편리하지만, 어떤 가게를 들일지 정하는 권한도 운영자 한 곳에만 있어요.", "Convenient, but the power to decide who gets in sits with the operator alone."),
         "tricks": (4, [
             (ALLIN_I, ("한 곳에서 다 해결", "Solve it all in one place"), ("앱 하나면 충분해요", "one app is all it takes"), "calm"),
             (DATA_I, ("쓸수록 데이터가 모임", "Data pools the more it's used"), ("운영자가 이용자를 누구보다 많이 알게 돼요", "the operator comes to know users better than anyone")),
             (WALL_I, ("다른 곳은 들어오기 어려움", "Hard for others to get in"), ("진입장벽이 생겨요", "a barrier to entry forms"), "warm"),
             (LAW_I, ("그래서 법으로 공정 기준을 정함", "So the law sets fairness rules"), ("EU DMA처럼 플랫폼 전용 규제가 생기기도 해요", "platform-specific rules can follow, like the EU's DMA")),
         ])},
        {"svg": P4, "alt": ("편리한 점과 규제가 필요한 이유를 나란히 비교한 규칙판 두 개", "Two rule boards comparing convenience against the reasons regulation is needed"),
         "caption": ("편리함 뒤에는 규제가 필요한 이유도 있어요.", "Behind the convenience are reasons regulation is needed."),
         "small": ("편리함과 공정한 경쟁 사이에서 법이 균형을 잡으려 해요.", "The law tries to balance convenience against fair competition.")},
        {"svg": P5, "alt": ("왼쪽: 공정 경쟁 기준을 정하는 선생님. 오른쪽: 새 기능 넣기 힘들어 찡그리는 학생회장", "Left: a teacher setting fair-competition rules. Right: the president frowning at how hard new features are to add"),
         "caption": ("슈퍼앱을 너무 규제하면 편리함이 줄어들 수 있어요.", "Over-regulating a super app can shrink its convenience."),
         "small": ("공정함과 자율성, 망중립성에서도 봤던 똑같은 줄다리기예요.", "Fairness vs autonomy — the same tug-of-war seen with net neutrality.")},
    ],
    "summary": (("<b>슈퍼앱</b> = 여러 서비스를 <b>한 앱에 몰아 모은 것</b>. 편리하지만 <b>독점·끼워팔기·데이터 집중</b> 우려 때문에 별도 규제가 논의돼요.",
                 "<b>Super app</b> = <b>bundling many services into one app</b>. Convenient, but separate regulation is debated because of <b>monopoly, forced bundling, and data concentration</b> concerns."),
                ("슈퍼앱은 결제·메시징·쇼핑·배차 등 여러 서비스를 하나의 앱 안에 통합해 제공하는 플랫폼이에요. 편의성이 크지만, 시장지배력이 한 앱에 집중되고 데이터가 결합·오남용될 수 있으며, 자사 서비스를 묶어 경쟁 서비스를 밀어내는 끼워팔기 문제가 생길 수 있어요. 그래서 EU 디지털시장법(DMA)은 큰 플랫폼에 상호운용성과 공정한 입점 기준을 요구하고, 한국에서도 온라인 플랫폼 규제 법안이 논의돼 왔어요.",
                 "A super app is a platform that bundles services like payments, messaging, shopping, and ride-hailing into a single app. It's highly convenient, but market power concentrates in one app, data can be combined and misused, and bundling its own services can push out competitors. That's why the EU's Digital Markets Act (DMA) requires interoperability and fair terms of entry from large platforms, and online-platform bills have been debated in Korea too.")),
    "glossary": [
        ("슈퍼앱", "Super App", ("여러 서비스를 한 앱에 모은 것.", "Many services bundled into one app."), ("편리하지만 시장과 데이터가 한 앱에 몰릴 우려도 있어요.", "Convenient, but market power and data may pile up in one app.")),
        ("플랫폼 규제", "Platform Regulation", ("큰 앱 하나를 따로 다루는 법.", "A law that treats one dominant app differently."), ("EU의 DMA가 대표적이에요. 한국은 온라인 플랫폼 법안들이 국회에 올라가 있고(2026년 9월 기준 미통과), 공정위의 온라인 플랫폼 독과점 심사지침은 2023년 1월부터 시행 중이에요.", "The EU's DMA is the main example. In Korea, online-platform bills sit in the National Assembly (not passed as of September 2026), while the Fair Trade Commission's online-platform monopoly review guidelines took effect in January 2023.")),
        ("끼워팔기", "Bundling/Tying", ("한 서비스를 쓰려면 다른 서비스도 함께 쓰게 묶는 것.", "Making users take one service only together with another."), ("경쟁을 제한하는 대표적인 행위예요.", "A classic way competition gets restricted.")),
        ("데이터 집중", "Data Concentration", ("한 앱에 데이터가 몰리는 것.", "Data all pooling into one app."), ("몰린 데이터가 오남용되면 피해가 커질 수 있어요.", "Misuse of that pooled data can cause outsized harm.")),
        ("상호운용성", "Interoperability", ("다른 서비스와도 잘 맞물려 돌아가는 성질.", "Working smoothly together with other services."), ("플랫폼 규제가 요구하는 핵심 조건 중 하나예요.", "One of the core conditions platform regulation demands.")),
        ("시장지배력", "Market Dominance", ("한 서비스가 시장을 꽉 잡은 상태.", "One service holding a tight grip on the market."), ("지배력이 너무 커지면 공정 경쟁이 어려워져요.", "When that grip grows too strong, fair competition gets harder.")),
        ("디지털시장법(DMA)", "Digital Markets Act (DMA)", ("유럽연합의 플랫폼 공정경쟁법.", "The EU's fair-competition law for platforms."), ("큰 플랫폼에 상호운용성 의무를 지워요.", "Imposes interoperability duties on large platforms.")),
        ("망중립성", "Network Neutrality", ("통신망에서도 차별을 금지하는 원칙.", "The principle banning discrimination on the network too."), ('비슷한 공정성 긴장이 있어요. → <a href="netneutral-ko.html">급식 줄은 다 똑같이 서야 해요</a>', 'Shares a similar fairness tension. → <a href="netneutral-en.html">everyone waits in the same lunch line</a>')),
    ],
}
