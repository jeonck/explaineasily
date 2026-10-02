from _draw import *
from _world import *

# 1. 설계도는 고쳤는데, 실제 공사는 깜빡 잊어서 한참 뒤에야 반영돼요
P1 = svg(300, sky(300)
         + board(40, 30, 230, 130, "⟦새 설계도|NEW BLUEPRINT⟧", ("⟦기구: 2개로 변경|ride: change to x2⟧",), 1.0, hl=0)
         + ride(430, 260, 0.75, color="var(--accent)")
         + person(540, 260 - 112 * 0.55, s=0.55, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + bubble(560, 80, 190, 56, "⟦공사는... 다음 주에 할게요|I'll get to the construction... next week⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 282, "⟦설계도는 고쳤는데, 실제 공사는 깜빡 잊기도 해요|the blueprint gets updated, but the actual construction sometimes gets forgotten⟧", 12, "var(--ink)"))

# 2. 왜 어려운가(bad-soft): 설계도 수정과 공사가 따로 노니 사람이 깜빡해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + board(40, 60, 210, 120, "⟦설계도 보관함|BLUEPRINT STORE⟧", ("⟦2주 전에 바뀜|changed 2 weeks ago⟧",), 1.0)
         + ride(400, 240, 0.7, color="var(--accent)") + label(400, 135, "⟦아직도 1개뿐|still just 1⟧", 11, "var(--bad)", cls="d")
         + person(550, 240 - 112 * 0.6, s=0.6, face=FROWN + SWEAT, extra=CLIPBOARD, **MECHANIC)
         + bubble(540, 70, 200, 56, "⟦어, 제가 공사하는 걸 깜빡했네요...|oh, I forgot to actually build it...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦설계도 수정과 실제 공사가 따로 놀면, 사람이 깜빡해요|when updating the blueprint and building are two separate steps, people forget one⟧", 12, "var(--ink)"))

# 3. hero: 설계도 보관함에 새 설계도를 넣으면, 공사팀이 자동으로 알아채고 바로 공사를 시작해요
P3 = svg(340, sky(340)
         + board(30, 30, 220, 110, "⟦설계도 보관함|BLUEPRINT STORE⟧", ("⟦방금 새 설계도 도착|new blueprint just arrived⟧",), 1.0, hl=0)
         + '<path d="M255 85 Q380 70 495 85" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + controlroom(500, 30, 170, 100, bars=((0.5, "var(--good)"), (0.5, "var(--good)"), (0.5, "var(--good)")))
         + person(705, 30 + 100 - 112 * 0.5, s=0.5, face=EYES, **OPERATOR)
         + '<path d="M585 135 Q585 165 390 193" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(300, 280, 0.65, color="var(--accent)") + label(300, 175, "✓", 18, "var(--good)", cls="d")
         + ride(390, 280, 0.65, color="var(--accent)") + label(390, 175, "✓", 18, "var(--good)", cls="d")
         + ride(480, 280, 0.65, color="var(--accent)") + label(480, 175, "✓", 18, "var(--good)", cls="d")
         + label(380, 20, "⟦보관함에 새 설계도를 넣으면, 공사팀이 자동으로 알아채고 바로 지어요|drop a new blueprint in the store, and the crew notices it and builds it, automatically⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦보관함이 늘 지금의 정답이에요|the store is always today's single source of truth⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 넣는 순간 → 자동 감지 → 공사 → 완료 신호
P4 = svg(300, sky(300)
         + board(20, 100, 150, 90, "⟦보관함|STORE⟧", ("⟦새 설계도|new one⟧",), 1.0)
         + '<path d="M170 145 L250 145" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + controlroom(260, 100, 130, 90, bars=((0.6, "var(--good)"),))
         + label(325, 70, "⟦자동 감지|auto-detected⟧", 11, "var(--muted)")
         + '<path d="M390 145 Q460 145 520 195" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(560, 260, 0.7, color="var(--accent)") + label(560, 155, "⟦공사 중|building⟧", 11, "var(--ink)")
         + person(650, 260 - 112 * 0.55, s=0.55, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + label(380, 282, "⟦넣는 순간 → 자동 감지 → 공사 → 완료|drop it in → auto-detected → built → done⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 보관함에 잘못된 설계도를 넣으면 그대로 자동 반영돼요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + board(50, 40, 260, 110, "⟦보관함|STORE⟧", ("⟦리뷰 거친 설계도만|only reviewed blueprints⟧",), 1.0)
         + person(100, 150, s=0.5, face=SMILE, **OPERATOR) + label(190, 265, "⟦검토 후 들어와요|goes in only after review⟧", 11, "var(--ink)")
         + board(470, 40, 260, 110, "⟦보관함|STORE⟧", ("⟦실수로 잘못된 것 들어옴|a mistake slipped in⟧",), 1.0, hl=0)
         + ride(600, 230, 0.6, color="var(--bad)", closed=True)
         + label(600, 265, "⟦그대로 자동 반영돼요|it gets built automatically, as-is⟧", 11, "var(--bad)", cls="d")
         + label(380, 282, "⟦보관함에 잘못된 설계도를 넣으면, 그대로 자동 반영돼요|put a bad blueprint in the store, and it gets built automatically, exactly as it is⟧", 12, "var(--ink)"))

DROP_I = icon('<rect x="10" y="10" width="44" height="34" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h20 M18 28 h14" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><path d="M32 44 v14 M24 50 l8 8 l8 -8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
WATCHER_I = icon('<circle cx="32" cy="28" r="14" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="28" r="4" fill="var(--good)"/><path d="M20 50 h24" stroke="var(--stone-dark)" stroke-width="4" stroke-linecap="round"/>')
PULL_I = icon('<rect x="8" y="12" width="48" height="26" rx="4" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 40 v14" stroke="var(--good)" stroke-width="4"/><path d="M24 46 l8 8 l8 -8" fill="var(--good)"/>')
REVIEW_I = icon('<rect x="10" y="8" width="44" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h28 M18 28 h20" stroke="#142033" stroke-width="2.5"/><circle cx="44" cy="44" r="10" fill="var(--good)"/><path d="M39 44 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none"/>')

PAGE = {
    "slug": "gitops", "order": 18,
    "title": ("설계도가 바뀌면 자동으로 공사", "Construction Follows the Blueprint, Automatically"),
    "h1": ("<em>GitOps</em>가 뭐예요?", "What is <em>GitOps</em>?"),
    "sub": ("GitOps를 설계도 보관함에 새 설계도를 넣으면 자동으로 공사가 시작되는 이야기로 풀어봤어요.",
            "GitOps, told as a story about a blueprint store where construction starts automatically the moment a new blueprint arrives."),
    "panels": [
        {"svg": P1, "alt": ("새 설계도 판에 기구 2개로 바꾸라고 적혀 있지만, 옆의 정비사는 공사를 다음 주로 미루겠다고 말함", "A new blueprint board says change to 2 rides, but a nearby mechanic says he'll get to the construction next week"),
         "caption": ("설계도는 고쳤는데, 실제 공사는 깜빡 잊기도 해요.", "The blueprint gets updated, but the actual construction sometimes gets forgotten."),
         "small": ("한참 뒤에야 반영돼요.", "It only catches up much later.")},
        {"svg": P2, "alt": ("설계도 보관함엔 2주 전에 바뀐 내용이 있지만 기구는 아직 1개뿐이고, 정비사가 땀을 흘리며 공사를 깜빡했다고 말함", "The blueprint store shows a change from two weeks ago, but there's still only 1 ride, and a sweating mechanic admits he forgot to build it"),
         "caption": ("설계도 수정과 실제 공사가 따로 놀면, 사람이 깜빡해요.", "When updating the blueprint and building are two separate steps, people forget one."),
         "small": ("두 단계로 나뉘어 있으면 꼭 하나를 잊어버려요.", "Split into two steps, and one of them always slips through the cracks.")},
        {"svg": P3, "hero": True, "alt": ("설계도 보관함에 새 설계도가 도착하자, 관제실이 자동으로 알아채고 공사팀이 바로 새 기구를 지음", "A new blueprint arrives at the blueprint store; the control room notices automatically and the crew builds a new ride right away"),
         "caption": ("보관함에 새 설계도를 넣으면, 공사팀이 자동으로 알아채고 바로 지어요.", "Drop a new blueprint in the store, and the crew notices it and builds it, automatically."),
         "small": ("보관함이 늘 지금의 정답이에요.", "The store is always today's single source of truth."),
         "tricks": (4, [
             (DROP_I, ("설계도를 보관함에 넣으면 끝", "Just drop the blueprint in the store"), ("그다음은 안 해도 돼요", "nothing else to do"), "calm"),
             (WATCHER_I, ("공사는 자동으로 따라와요", "Construction follows automatically"), ("알아서 알아채요", "it notices on its own")),
             (PULL_I, ("보관함이 항상 정답이에요", "The store is always the answer"), ("지금 어때야 하는지요", "of what things should look like now"), "warm"),
             (REVIEW_I, ("다르면 자동으로 다시 맞춰요", "Mismatched? It re-syncs automatically"), ("실제를 보관함에 맞춰요", "reality follows the store")),
         ])},
        {"svg": P4, "alt": ("보관함에 새 설계도가 들어가고, 화살표를 따라 자동 감지되어 공사가 시작되고, 정비사가 완료를 확인함", "A new blueprint enters the store, an arrow shows it being auto-detected, construction begins, and a mechanic confirms completion"),
         "caption": ("넣는 순간 → 자동 감지 → 공사 → 완료.", "Drop it in, it's auto-detected, built, and done."),
         "small": ("사람이 중간에 끼어들 일이 없어요.", "No person needs to step in anywhere along the way.")},
        {"svg": P5, "alt": ("왼쪽: 검토를 거친 설계도만 보관함에 들어감. 오른쪽: 실수로 잘못된 설계도가 들어가자 고장난 기구가 그대로 자동으로 지어짐", "Left: only reviewed blueprints enter the store. Right: a mistaken blueprint slips in, and a broken ride gets built automatically, exactly as given"),
         "caption": ("보관함에 잘못된 설계도를 넣으면, 그대로 자동 반영돼요.", "Put a bad blueprint in the store, and it gets built automatically, exactly as it is."),
         "small": ("넣기 전에 검토가 꼭 필요해요.", "A review before it goes in is essential.")},
    ],
    "summary": (("<b>GitOps</b> = <b>설계도 보관함</b>을 지금의 유일한 정답으로 삼아서, 보관함에 새 설계도가 들어가면 <b>공사가 자동으로 따라오게</b> 하는 일.",
                 "<b>GitOps</b> = treating the <b>blueprint store</b> as the single source of truth, so that <b>construction automatically follows</b> whenever a new blueprint goes in."),
                ("Git 저장소를 유일한 정답(단일 진실 공급원)으로 삼아 인프라를 운영하는 방식이에요. 저장소가 바뀌면 자동화 도구가 그 차이를 감지해 실제 환경을 끌어다 맞춰요(풀 기반 배포). 실제가 저장소와 달라지면 자동으로 다시 동기화하고, 되돌릴 땐 저장소를 이전 커밋으로 되돌리면 돼요.",
                 "Running infrastructure by treating a Git repository as the single source of truth. When the repo changes, an automated tool detects the difference and pulls the live environment into sync (pull-based deployment). If reality drifts from the repo, it auto-syncs back, and rolling back is as simple as reverting the repo to an earlier commit.")),
    "glossary": [
        ("GitOps", "GitOps", ("설계도 보관함이 바뀌면 공사가 자동으로 따라오는 방식.", "A way where construction automatically follows a change to the blueprint store."), ("코드형 인프라의 다음 단계예요.", "The next step after infrastructure as code.")),
        ("저장소를 단일 진실 공급원으로", "Repo as single source of truth", ("보관함이 항상 정답.", "The store is always the answer."), ("실제가 거기에 맞춰져야 해요.", "Reality is what has to match it.")),
        ("자동 동기화", "Auto-sync", ("실제와 보관함이 다르면 자동으로 맞추는 일.", "Automatically reconciling reality with the store."), ("사람이 따로 맞출 필요가 없어요.", "No one needs to manually line things up.")),
        ("풀 기반 배포", "Pull-based deployment", ("공사팀이 알아서 보관함에서 가져가는 방식.", "The crew pulling the blueprint from the store on its own."), ("누가 밀어 넣는 게 아니라 끌어가요.", "Nothing is pushed in — it's pulled.")),
        ("코드형 인프라", "Infrastructure as Code", ("설계도를 종이 한 장(코드)에 적는 일.", "Writing the blueprint down as a single piece of code."), ('GitOps가 다루는 그 설계도예요. → <a href="iac-ko.html">설계도 한 장으로 공원 통째로 짓기</a>', 'This is the blueprint that GitOps operates on. → <a href="iac-en.html">building the whole park from one blueprint</a>')),
        ("리뷰·승인 절차", "Review and approval", ("보관함에 넣기 전 검토하는 일.", "Reviewing before it goes into the store."), ("여기서 걸러야 실수가 자동으로 퍼지지 않아요.", "Catch mistakes here, or they spread automatically.")),
        ("롤백", "Rollback", ("보관함을 이전 설계도로 되돌리는 일.", "Reverting the store to an earlier blueprint."), ("되돌리면 실제도 자동으로 따라와요.", "Revert it, and reality follows automatically too.")),
        ("CI/CD", "CI/CD", ("설계도를 검토하고 보관함에 올리기까지의 앞단계.", "The earlier steps — reviewing and getting the blueprint into the store."), ("GitOps는 그 뒤, 보관함부터 공사까지를 맡아요.", "GitOps picks up after that, from the store to construction.")),
    ],
}
