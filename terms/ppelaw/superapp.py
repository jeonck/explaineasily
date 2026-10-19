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
         + '<rect x="330" y="200" width="100" height="60" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + label(380, 225, "⟦학생증 앱|STUDENT ID APP⟧", 10, "var(--ink)", cls="d")
         + label(380, 245, "⟦급식 · 도서관 · 출석 · 포인트|lunch · library · roll call · points⟧", 8, "var(--muted)")
         + person(180, 160, s=0.7, face=SMILE, **STUDENT) + person(580, 160, s=0.7, face=SMILE, **STUDENT)
         + label(380, 290, "⟦다들 편하다고 좋아해요|everyone loves how convenient it is⟧", 12, "var(--ink)", cls="d"))

# 2. 다른 가게는 들어올 수가 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + '<rect x="310" y="90" width="140" height="80" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>' + label(380, 135, "⟦학생증 앱|STUDENT ID APP⟧", 11, "var(--ink)", cls="d")
         + person(170, 150, s=0.75, face=FROWN, **REP) + bubble(70, 190, 200, 44, "⟦우리 매점도 넣어주세요|let our shop in too, please⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(590, 150, s=0.75, face=EYES, **PRESIDENT) + bubble(500, 190, 220, 44, "⟦여긴 저희가 고른 곳만 돼요|only shops we picked are allowed here⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦이 앱 안에서만 쓸 수 있는 포인트라서, 선택권이 없어요|points only work inside this app, so there's no real choice⟧", 12, "var(--ink)", cls="d"))

# 3. 슈퍼앱 = 여러 서비스를 한 앱에 모은 것, 규칙도 운영자가 다 정함 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦슈퍼앱 = 여러 서비스를 한 앱에 모은 것 — 규칙도 운영자 혼자 정해요|a super app bundles many services into one — and its operator alone writes the rules⟧", 12, "var(--ink)", cls="d")
         + '<rect x="280" y="70" width="200" height="140" rx="12" fill="var(--panel)" stroke="var(--accent)" stroke-width="4"/>'
         + label(380, 100, "⟦학생증 앱|STUDENT ID APP⟧", 12, "var(--ink)", cls="d")
         + label(330, 130, "⟦급식|lunch⟧", 10, "var(--muted)") + label(430, 130, "⟦도서관|library⟧", 10, "var(--muted)")
         + label(330, 160, "⟦출석|roll call⟧", 10, "var(--muted)") + label(430, 160, "⟦포인트|points⟧", 10, "var(--muted)")
         + label(380, 190, "⟦동아리 신청|club sign-up⟧", 10, "var(--muted)")
         + person(170, 230, s=0.8, face=EYES, **PRESIDENT) + person(600, 230, s=0.75, face=SMILE, **STUDENT)
         + label(380, 320, "⟦편리하지만, 문을 여닫는 열쇠도 한 곳에만 있어요|convenient, but the key to the door sits in one place too⟧", 11, "var(--muted)"))

# 4. 편리함 vs 규제가 필요한 이유
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 30, 320, 240, "⟦편리한 점|WHAT'S CONVENIENT⟧", ("⟦앱 하나로 다 해결|one app solves it all⟧", "⟦옮겨다닐 필요 없음|no need to switch apps⟧", "⟦포인트가 한곳에 쌓임|points build up in one place⟧"), 1.0)
         + rulesboard(390, 30, 320, 240, "⟦규제가 필요한 이유|WHY REGULATION IS NEEDED⟧", ("⟦독점 — 경쟁이 사라짐|monopoly — competition disappears⟧", "⟦끼워팔기 — 입점 강제|bundling — forced partnerships⟧", "⟦데이터 집중 — 다 한곳에 모임|data concentration — it all pools in one place⟧"), 1.0, hl=0)
         + label(380, 295, "⟦편리함과 공정한 경쟁 사이에서 법이 균형을 잡으려 해요|the law tries to balance convenience against fair competition⟧", 12, "var(--ink)", cls="d"))

# 5. 너무 규제하면 편리함이 줄어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **TEACHER) + label(190, 250, "⟦공정한 경쟁 기준을 정해요|setting fair-competition rules⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **PRESIDENT) + label(570, 250, "⟦너무 세세하면 새 기능 넣기 힘들어요|too much detail makes new features hard to add⟧", 11, "var(--ink)")
         + label(380, 285, "⟦공정함과 자율성, 망중립성에서도 봤던 똑같은 줄다리기예요|fairness vs autonomy — the same tug-of-war seen with net neutrality⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "superapp", "order": 11,
    "title": ("학생증 하나로 다 되는 앱", "One Student-ID App That Does Everything"),
    "h1": ("<em>슈퍼앱</em>이 뭐예요?", "What is a <em>Super App</em>?"),
    "sub": ("슈퍼앱을, 학생회가 만든 학생증 앱 하나로 급식·도서관·출석·포인트가 다 되는 이야기로 풀어봤어요.",
            "Super apps, told as a story about a student-ID app the council built that handles lunch, library, roll call, and points all at once."),
    "panels": [
        {"svg": P1, "alt": ("학생회장이 급식·도서관·출석·포인트가 다 되는 학생증 앱을 들고 있고, 학생들이 좋아함", "The council president holds up a student-ID app for lunch, library, roll call, and points, and students love it"),
         "caption": ("학생증 하나로 다 되는 앱을 만들었어요.", "They built one student-ID app that does everything."),
         "small": ("다들 편하다고 좋아해요.", "Everyone loves how convenient it is.")},
        {"svg": P2, "alt": ("매점 대표가 입점을 부탁하지만 학생회장은 고른 곳만 된다고 답함", "A shop rep asks to be let into the app, but the president says only hand-picked shops are allowed"),
         "caption": ("다른 가게는 들어올 수가 없어요.", "Other shops can't get in."),
         "small": ("이 앱 안에서만 쓸 수 있는 포인트라서, 선택권이 없어요.", "Points only work inside this app, so there's no real choice.")},
        {"svg": P3, "hero": True, "alt": ("학생증 앱 하나에 급식·도서관·출석·포인트·동아리 신청이 다 모여 있음", "One student-ID app bundling lunch, library, roll call, points, and club sign-up all together"),
         "caption": ("슈퍼앱은 여러 서비스를 한 앱에 모은 것이에요.", "A super app bundles many services into one."),
         "small": ("편리하지만, 문을 여닫는 열쇠도 한 곳에만 있어요.", "Convenient, but the key to the door sits in one place too."),
         "tricks": (4, [
             (ALLIN_I, ("한 곳에서 다 해결", "Solve it all in one place"), ("앱 하나면 충분해요", "one app is all it takes"), "calm"),
             (DATA_I, ("쓸수록 데이터가 모임", "Data pools the more it's used"), ("누구보다 많이 알게 돼요", "comes to know more than anyone")),
             (WALL_I, ("다른 곳은 들어오기 어려움", "Hard for others to get in"), ("진입장벽이 생겨요", "a barrier to entry forms"), "warm"),
             (LAW_I, ("그래서 법으로 공정 기준을 정함", "So the law sets fairness rules"), ("플랫폼 규제가 따로 생겨요", "platform-specific regulation follows")),
         ])},
        {"svg": P4, "alt": ("편리한 점과 규제가 필요한 이유를 나란히 비교한 규칙판 두 개", "Two rule boards comparing convenience against the reasons regulation is needed"),
         "caption": ("편리함 뒤에는 규제가 필요한 이유도 있어요.", "Behind the convenience are reasons regulation is needed."),
         "small": ("편리함과 공정한 경쟁 사이에서 법이 균형을 잡으려 해요.", "The law tries to balance convenience against fair competition.")},
        {"svg": P5, "alt": ("왼쪽: 공정 경쟁 기준을 정하는 선생님. 오른쪽: 새 기능 넣기 힘들어 찡그리는 학생회장", "Left: a teacher setting fair-competition rules. Right: the president frowning at how hard new features are to add"),
         "caption": ("너무 규제하면 편리함이 줄어들 수 있어요.", "Too much regulation can shrink the convenience."),
         "small": ("공정함과 자율성, 망중립성에서도 봤던 똑같은 줄다리기예요.", "Fairness vs autonomy — the same tug-of-war seen with net neutrality.")},
    ],
    "summary": (("<b>슈퍼앱</b> = 여러 서비스를 <b>한 앱에 몰아 모은 것</b>. 편리하지만 <b>독점·끼워팔기·데이터 집중</b> 우려 때문에 따로 규제해요.",
                 "<b>Super app</b> = <b>bundling many services into one app</b>. Convenient, but regulated separately because of <b>monopoly, forced bundling, and data concentration</b> concerns."),
                ("슈퍼앱은 결제·메시징·쇼핑·배차 등 여러 서비스를 하나의 앱 안에 통합해 제공하는 플랫폼이에요. 편의성이 크지만, 시장지배력이 한 앱에 집중되고 데이터가 결합·오남용될 수 있으며, 경쟁 서비스의 입점을 막는 끼워팔기 문제가 생길 수 있어요. 그래서 온라인플랫폼 공정화법·디지털시장법(DMA) 같은 플랫폼 규제가 상호운용성과 공정한 입점 기준을 따로 요구해요.",
                 "A super app is a platform that bundles services like payments, messaging, shopping, and ride-hailing into a single app. It's highly convenient, but market power concentrates in one app, data can be combined and misused, and bundling can block competing services from getting in. That's why platform regulations such as online-platform fairness acts and the EU's Digital Markets Act (DMA) separately require interoperability and fair terms of entry.")),
    "glossary": [
        ("슈퍼앱", "Super App", ("여러 서비스를 한 앱에 모은 것.", "Many services bundled into one app."), ("편리함과 집중의 우려를 같이 갖고 있어요.", "Comes with both convenience and concentration concerns.")),
        ("플랫폼 규제", "Platform Regulation", ("큰 앱 하나를 따로 다루는 법.", "A law that treats one dominant app differently."), ("온라인플랫폼 공정화법, DMA 등이 있어요.", "Includes things like online-platform fairness acts and the DMA.")),
        ("끼워팔기", "Bundling/Tying", ("다른 서비스 입점을 막거나 강제하는 것.", "Blocking or forcing how other services get bundled in."), ("경쟁을 제한하는 대표적인 행위예요.", "A classic way competition gets restricted.")),
        ("데이터 집중", "Data Concentration", ("한 앱에 데이터가 몰리는 것.", "Data all pooling into one app."), ("오남용되면 피해가 커질 수 있어요.", "Misuse here can cause outsized harm.")),
        ("상호운용성", "Interoperability", ("다른 서비스와도 잘 맞물려 돌아가는 성질.", "Working smoothly together with other services."), ("플랫폼 규제가 요구하는 핵심 조건 중 하나예요.", "One of the core conditions platform regulation demands.")),
        ("시장지배력", "Market Dominance", ("한 서비스가 시장을 꽉 잡은 상태.", "One service holding a tight grip on the market."), ("너무 커지면 공정 경쟁이 어려워져요.", "Grow too large, and fair competition gets harder.")),
        ("디지털시장법(DMA)", "Digital Markets Act (DMA)", ("유럽연합의 플랫폼 공정경쟁법.", "The EU's fair-competition law for platforms."), ("큰 플랫폼에 상호운용성 의무를 지워요.", "Imposes interoperability duties on large platforms.")),
        ("망중립성", "Network Neutrality", ("통신망에서도 차별을 금지하는 원칙.", "The principle banning discrimination on the network too."), ('비슷한 공정성 긴장이 있어요. → <a href="netneutral-ko.html">급식 줄은 다 똑같이 서야 해요</a>', 'Shares a similar fairness tension. → <a href="netneutral-en.html">everyone waits in the same lunch line</a>')),
    ],
}
