from _draw import *
from _world import *

# 1. 새로 고친 기구를 전체 공개했다가 문제가 생겨요
P1 = svg(300, sky(300)
         + ride(130, 260, 0.9, color="var(--accent)", closed=True, label_text="⟦새 버전, 전체 공개|new version, out for everyone⟧")
         + queueline(250, 204, 6, 0.5, 26)
         + person(640, 170, s=0.7, face=FROWN + SWEAT, **MANAGER)
         + bubble(540, 80, 200, 46, "⟦손님 전체가 다 겪었어요|every single guest felt it⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦새로 고친 기구를 전체 공개했다가 문제가 생겼어요|rolling the refreshed ride out to everyone — then it broke⟧", 12, "var(--ink)"))

# 2. 아무리 테스트해도 진짜 손님 앞에선 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 163, s=0.6, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + bubble(40, 70, 220, 50, "⟦백 번 테스트해도 모자라요|tested a hundred times, still not enough⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 163, s=0.6, face=FROWN, **ROOKIE)
         + bubble(500, 70, 220, 50, "⟦손님 앞에선 뭐가 터질지 몰라요|in front of real guests, who knows what breaks⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 286, "⟦진짜 손님 앞에 서기 전엔 아무도 몰라요|nobody really knows until real guests show up⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 공원 구석에서 몰래, 손님 1%만 태워봐요
FEW_I = icon('<circle cx="18" cy="40" r="9" fill="var(--stone)"/><circle cx="46" cy="40" r="9" fill="var(--stone)"/><circle cx="32" cy="38" r="13" fill="var(--accent)"/>')
WATCH2_I = icon('<rect x="8" y="14" width="48" height="32" rx="4" fill="#1B2A44"/><rect x="14" y="20" width="14" height="14" fill="var(--good)"/><rect x="32" y="20" width="14" height="20" fill="var(--bad)"/><circle cx="48" cy="48" r="7" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M53 53 L58 58" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
UP_I = icon('<rect x="10" y="40" width="10" height="14" fill="var(--good)"/><rect x="24" y="30" width="10" height="24" fill="var(--good)"/><rect x="38" y="18" width="10" height="36" fill="var(--good)"/><path d="M42 16 l8 -8 l8 8 M50 8 v18" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
BACK_I = icon('<path d="M46 20 a18 18 0 1 0 6 26" stroke="var(--bad)" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M50 10 l-4 14 l14 4z" fill="var(--bad)"/>')

P3 = svg(340, sky(340)
         + queueline(60, 250, 6, 0.45, 26)
         + ride(220, 300, 0.85, color="#5B8DEF")
         + person(430, 250, s=0.45, face=SMILE, hat=FOLK[2][0], shirt=FOLK[2][1])
         + '<path d="M430 294 Q470 300 505 300" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(470, 227, s=0.65, face=SMILE, **ROOKIE)
         + ride(560, 300, 0.75, color="var(--accent)", label_text="⟦새 버전, 구석에서 몰래|new version, tucked in the corner⟧")
         + controlroom(610, 40, 130, 90, bars=((0.5, "var(--good)"), (0.45, "var(--good)")))
         + label(380, 30, "⟦공원 구석에서 몰래 1%만 태워봐요|testing quietly in a corner — just 1% of guests⟧", 14, "var(--ink)", cls="d")
         + label(380, 328, "⟦괜찮으면 조금씩 늘리고, 이상하면 바로 거둬요|if it is fine, add a little more — if not, pull it back right away⟧", 12, "var(--muted)"))

# 4. 1% → 10% → 50% → 100%, 단계마다 계기판 확인
P4 = svg(300, sky(300, ground=False)
         + gauge(110, 130, 0.9, level=0.08, label_text="⟦1%|1%⟧", color="var(--accent)")
         + gauge(290, 130, 0.9, level=0.25, label_text="⟦10%|10%⟧", color="var(--accent)")
         + gauge(470, 130, 0.9, level=0.55, label_text="⟦50%|50%⟧", color="var(--accent)")
         + gauge(650, 130, 0.9, level=0.95, label_text="⟦100%|100%⟧", color="var(--good)")
         + '<path d="M145 130 L255 130" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M245 123 L255 130 L245 137" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + '<path d="M325 130 L435 130" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M425 123 L435 130 L425 137" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + '<path d="M505 130 L615 130" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/><path d="M605 123 L615 130 L605 137" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>'
         + label(110, 85, "✓", 20, "var(--good)", cls="d") + label(290, 85, "✓", 20, "var(--good)", cls="d") + label(470, 85, "✓", 20, "var(--good)", cls="d")
         + label(380, 286, "⟦단계마다 계기판을 확인하고 나서야 다음으로 넘어가요|check the gauges at every stage before moving on⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 손님이 원래 적으면 1%로는 몰라요
P5 = svg(300, sky(300, ground=False)
         + queueline(90, 234, 3, 0.4, 30)
         + person(240, 180, s=0.6, face=FROWN, **ROOKIE)
         + bubble(140, 90, 220, 50, "⟦손님이 원래 몇 명 안 와요...|there were only a few guests to begin with...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(560, 260, 0.9, color="var(--accent)", label_text="⟦1%는 손님 한 명도 안 돼요|1% doesn't even add up to one guest⟧")
         + label(380, 286, "⟦1%가 느껴질 만큼 손님이 많아야 의미가 있어요|canaries only work when 1% is still enough guests to notice⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "canary", "order": 34,
    "title": ("구석에서 몰래 하는 시험 운행", "A Quiet Test Run in the Corner"),
    "h1": ("<em>카나리 배포</em>가 뭐예요?", "What is <em>Canary Deployment</em>?"),
    "sub": ("카나리 배포를 공원 구석에서 손님 1%만 몰래 태워보는 이야기로 풀어봤어요.",
            "Canary deployment, told as a story about quietly testing a new ride on just 1% of guests, in a corner."),
    "panels": [
        {"svg": P1, "alt": ("새로 고친 기구를 전체 공개했다가 문제가 생겨 손님 전체가 피해를 봄", "A refreshed ride opens to everyone, then breaks, and every guest feels it"),
         "caption": ("새로 고친 기구를 전체 공개했다가 문제가 생겼어요.", "The refreshed ride opened to everyone — then it broke."),
         "small": ("새 버전은 아무리 고쳐도 모든 손님 앞에 서면 또 문제가 생길 수 있어요.", "No matter how much you polish it, a new version can still break in front of everyone.")},
        {"svg": P2, "alt": ("정비사가 백 번 테스트해도 모자라다고 말하고, 신참 정비사는 손님 앞에선 몰라요 라고 말함", "A mechanic says a hundred tests are not enough, while a rookie says nobody knows until real guests arrive"),
         "caption": ("아무리 테스트해도 진짜 손님 앞에선 몰라요.", "No matter how much you test, you cannot know until real guests show up."),
         "small": ("연습으로는 다 못 잡아요. 진짜 손님만이 진짜 답을 줘요.", "Rehearsal cannot catch everything. Only real guests give the real answer.")},
        {"svg": P3, "hero": True, "alt": ("신참 정비사가 공원 구석에 새 버전 기구를 세우고 손님 한 명만 몰래 태워봄", "A rookie mechanic sets up the new ride in a corner and quietly lets just one guest try it"),
         "caption": ("공원 구석에서 몰래, 손님 1%만 태워봐요.", "Quietly, in a corner, try it on just 1% of guests."),
         "small": ("괜찮으면 조금씩 늘리고, 이상하면 바로 거둬요.", "If it's fine, add a little more. If not, pull it back right away."),
         "tricks": (4, [
             (FEW_I, ("아주 적은 손님에게만 먼저", "Only a handful of guests first"), ("표 나지 않게 조용히", "quietly enough not to show"), "calm"),
             (WATCH2_I, ("계기판을 계속 지켜봐요", "Keep watching the gauges"), ("문제가 보이는지", "for any sign of trouble")),
             (UP_I, ("괜찮으면 비율을 조금씩 늘려요", "If it's fine, raise the share bit by bit"), ("1% → 10% → 50%", "1% → 10% → 50%"), "warm"),
             (BACK_I, ("이상하면 바로 전부 거둬요", "If not, pull it all back at once"), ("되돌려요", "revert it")),
         ])},
        {"svg": P4, "alt": ("공원 지도의 계기판 네 개가 1%, 10%, 50%, 100% 단계로 늘어나며 각 단계마다 확인 표시가 붙음", "Four gauges rise through 1%, 10%, 50%, 100%, each stage marked with a check"),
         "caption": ("1% → 10% → 50% → 100%, 단계마다 계기판을 확인해요.", "1% → 10% → 50% → 100% — check the gauges at every stage."),
         "small": ("한 번에 다 늘리지 않고, 괜찮다는 확인을 받고서야 다음 단계로 가요.", "Never jump to all at once — move to the next stage only after confirming it's fine.")},
        {"svg": P5, "alt": ("신참 정비사가 손님이 원래 몇 명 안 온다고 걱정하고, 1%는 손님 한 명도 안 된다는 설명이 붙음", "The rookie worries there were only a few guests to begin with, and a note explains 1% doesn't even add up to one guest"),
         "caption": ("손님이 원래 적으면 1%로는 뭘 알기 어려워요.", "When there are only a few guests, 1% doesn't tell you much."),
         "small": ("1%가 손님 한 명도 안 된다면, 시험 운행은 의미가 없어요.", "If 1% doesn't even add up to one guest, the test run tells you nothing.")},
    ],
    "summary": (("<b>카나리 배포</b> = 새 버전을 <b>손님 1%에게만 몰래</b> 먼저 태워보고, 계기판을 보며 <b>조금씩 늘리거나 바로 거두는</b> 요령.",
                 "<b>Canary deployment</b> = quietly trying a new version on <b>just 1% of guests first</b>, watching the gauges, and either <b>scaling up slowly or pulling back immediately</b>."),
                ("운영 중인 서비스 전체가 아니라 아주 일부 트래픽에만 새 버전을 먼저 노출해 위험을 줄이는 점진적 배포 방식이에요. 지표가 괜찮으면 비율을 단계적으로 늘리고, 나빠지면 자동으로 되돌려요.",
                 "A gradual rollout strategy that exposes a new version to only a small slice of traffic first, reducing risk. If the metrics look fine, the share increases step by step; if they worsen, it's rolled back automatically.")),
    "glossary": [
        ("카나리 배포", "Canary deployment", ("구석에서 몰래 하는 시험 운행.", "A quiet test run in the corner."), ("손님 1%에게만 먼저 새 버전을 보여줘요.", "Only 1% of guests see the new version first.")),
        ("점진적 롤아웃", "Gradual rollout", ("조금씩 비율을 늘리는 일.", "Raising the share a little at a time."), ("한 번에 다 바꾸지 않아요.", "Never switching everything over all at once.")),
        ("트래픽 분할", "Traffic splitting", ("손님을 나눠 보내는 일.", "Sending guests down different paths."), ("몇 %는 새 기구로, 나머지는 원래 기구로요.", "A slice goes to the new ride, the rest to the old one.")),
        ("계기판 비교", "Metric comparison", ("새 버전과 옛 버전의 계기판을 나란히 보는 일.", "Watching the new and old version's gauges side by side."), ("차이가 나면 바로 알아차려요.", "Any difference shows up right away.")),
        ("자동 롤백", "Automatic rollback", ("이상하면 스스로 되돌리는 일.", "Reverting on its own when something's off."), ('사람이 늦게 알아채도 괜찮아요. → <a href="rollback-ko.html">이상하면 바로 어제 버전으로</a>', "Fine even if a person notices late. → " + '<a href="rollback-en.html">back to yesterday\'s version, fast</a>')),
        ("블루-그린과의 차이", "vs. blue-green", ("전부 바꾸느냐, 일부만 먼저 보느냐.", "Switching everything, versus showing it to a few first."), ('블루-그린은 통째로 바꿔요. → <a href="bluegreen-ko.html">쌍둥이 기구를 번갈아 운영</a>', '<a href="bluegreen-en.html">Blue-green switches the whole thing at once</a>')),
        ("피처 플래그", "Feature flag", ("새 기구에 친 커튼.", "A curtain drawn over the new ride."), ("카나리와 같이 쓰면 누구에게 보일지 더 세밀하게 골라요.", "Paired with a canary, it picks exactly who sees the new ride.")),
        ("롤백", "Rollback", ("이상하면 바로 어제 버전으로.", "Back to yesterday's version, right away."), ('→ <a href="rollback-ko.html">이상하면 바로 어제 버전으로</a>', '→ <a href="rollback-en.html">back to yesterday\'s version, fast</a>')),
    ],
}
