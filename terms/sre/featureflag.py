from _draw import *
from _world import *

# 1. 새 기구를 손님 전체에 한꺼번에 공개해요
P1 = svg(300, sky(300)
         + ride(380, 260, 1.0, color="var(--accent)", label_text="⟦새 기구|new ride⟧")
         + queueline(90, 204, 7, 0.5, 30)
         + person(620, 260 - 112 * 0.6, s=0.6, face=SMILE, **MANAGER) + label(660, 200, "⟦오늘부터 전체 공개!|open to everyone, today!⟧", 11, "var(--ink)", cls="d")
         + label(380, 282, "⟦새 기구를 손님 전체에 한꺼번에 공개해요|a new ride opens to every guest, all at once⟧", 12, "var(--ink)"))

# 2. 왜 어려운가(bad-soft): 문제가 생기면 전체를 다시 닫아야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(380, 260, 1.0, color="var(--stone)", closed=True, label_text="⟦새 기구|new ride⟧")
         + queueline(90, 204, 7, 0.5, 30) + label(240, 185, "⟦줄이 그대로 멈춰 있어요|the whole line is stuck⟧", 11, "var(--bad)")
         + person(620, 260 - 112 * 0.6, s=0.6, face=FROWN + SWEAT, **MANAGER) + bubble(560, 90, 200, 56, "⟦닫으려면 또 공사를 해야 해요...|closing it means construction all over again...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦코드를 다시 배포해야 되돌릴 수 있으면, 되돌리는 것도 느려요|if rolling back means redeploying code, the rollback itself is slow⟧", 12, "var(--ink)"))

# 3. hero: 커튼을 쳐 두고, 스위치 하나로 몇 명에게 보일지 조절해요
P3 = svg(340, sky(340)
         + ride(300, 280, 0.85, color="var(--accent)")
         + '<rect x="258" y="196" width="84" height="80" fill="var(--night)" opacity="0.55"/>' + label(300, 240, "⟦커튼|CURTAIN⟧", 11, "#F5E6B8", cls="d")
         + board(460, 40, 230, 130, "⟦공개 스위치|RELEASE SWITCH⟧", ("⟦직원만|staff only⟧", "⟦→ 1% 손님|→ 1% of guests⟧", "⟦→ 전체 공개|→ everyone⟧"), 1.0, hl=1)
         + person(130, 280 - 112 * 0.6, s=0.6, face=EYES, **MANAGER)
         + '<path d="M165 230 L260 236" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 18, "⟦기구는 지어 두되 커튼을 치고, 스위치로 몇 명에게 보일지 정해요|build the ride but keep the curtain drawn, and a switch decides who gets to see it⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦코드를 다시 올리지 않고 바로 켜고 꺼요|flip it on or off without redeploying any code⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 직원만 → 1% 손님 → 전체, 다이얼이 돌아가요
P4 = svg(320, sky(320)
         + ride(380, 260, 0.9, color="var(--accent)")
         + '<rect x="332" y="166" width="96" height="94" fill="var(--night)" opacity="0.35"/>'
         + person(230, 260 - 112 * 0.45, s=0.45, face=EYES, **ROOKIE) + label(230, 155, "⟦직원|staff⟧", 10, "var(--muted)")
         + queueline(480, 234, 1, 0.4, 0) + label(495, 155, "⟦1% 손님|1% of guests⟧", 10, "var(--muted)")
         + gauge(650, 100, 1.0, level=0.3, label_text="⟦공개 비율|release %⟧")
         + '<path d="M650 158 L650 195" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 300, "⟦다이얼을 조금씩 돌려요 — 직원만, 1% 손님, 그다음 전체|turn the dial a little at a time — staff only, then 1% of guests, then everyone⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 커튼(스위치)이 너무 많아지면 관리하기 어려워요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + board(60, 30, 640, 155, "⟦지금 켜진 스위치들|SWITCHES CURRENTLY ON⟧",
                 ("⟦새 기구 공개: 켜짐|new-ride release: ON⟧", "⟦여름 이벤트: 켜짐|summer event: ON⟧", "⟦옛 매표 방식: 켜짐? 꺼짐?|old booth style: ON? OFF?⟧", "⟦누가 왜 켰는지 기억 안 남|no one remembers who turned this on, or why⟧"), 1.0, hl=2)
         + person(380, 200, s=0.5, face=FROWN + SWEAT, **MECHANIC)
         + label(380, 282, "⟦커튼(스위치)이 너무 많아지면, 뭐가 켜져 있는지 관리하기 어려워요|too many curtains (switches), and it gets hard to track what's even on⟧", 12, "var(--ink)"))

CURTAIN_I = icon('<rect x="8" y="8" width="48" height="44" rx="3" fill="var(--night)"/><path d="M14 10 v40 M32 10 v40 M50 10 v40" stroke="#1E2E4A" stroke-width="3"/><rect x="8" y="50" width="48" height="6" fill="#C9822B"/>')
DIAL_I = icon('<circle cx="32" cy="36" r="20" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 36 L20 20" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="36" r="4" fill="var(--accent)"/>')
KILL_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)" stroke="#7A1F17" stroke-width="3"/><rect x="24" y="24" width="16" height="16" fill="#FFF"/>')
TARGET_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="32" r="12" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="32" r="3" fill="var(--accent)"/>')

PAGE = {
    "slug": "featureflag", "order": 34,
    "title": ("새 기구에 친 커튼", "A Curtain Drawn Over a New Ride"),
    "h1": ("<em>피처 플래그</em>가 뭐예요?", "What is a <em>Feature Flag</em>?"),
    "sub": ("피처 플래그를 새 기구를 지어 두고 커튼을 쳐서, 스위치로 몇 명에게 보여줄지 정하는 이야기로 풀어봤어요.",
            "Feature flags, told as a story about building a new ride, drawing a curtain over it, and using a switch to decide who gets to see it."),
    "panels": [
        {"svg": P1, "alt": ("새 기구가 완성되자 손님 전체에게 오늘부터 전체 공개라고 공원장이 말함", "A new ride is finished, and the park manager announces it's open to everyone, starting today"),
         "caption": ("새 기구를 손님 전체에 한꺼번에 공개해요.", "A new ride opens to every guest, all at once."),
         "small": ("문제가 생기면 전체를 다시 닫아야 해요.", "And if something goes wrong, the whole thing has to close again.")},
        {"svg": P2, "alt": ("새 기구가 고장으로 닫히고 줄이 그대로 멈춰 있음. 공원장이 땀을 흘리며 닫으려면 또 공사해야 한다고 말함", "The new ride is closed with a breakdown and the whole line is stuck; a sweating manager says closing it means construction all over again"),
         "caption": ("코드를 다시 배포해야 되돌릴 수 있으면, 되돌리는 것도 느려요.", "If rolling back means redeploying code, the rollback itself is slow."),
         "small": ("짓는 것과 보여주는 걸 같이 해버린 탓이에요.", "That's what happens when building and showing are bundled into one step.")},
        {"svg": P3, "hero": True, "alt": ("새 기구가 커튼에 가려져 있고, 옆의 공개 스위치 판에는 직원만 → 1% 손님 → 전체 공개라고 적혀 있음", "A new ride stands behind a curtain, with a release-switch board beside it reading staff only, then 1% of guests, then everyone"),
         "caption": ("기구는 지어 두되 커튼을 치고, 스위치로 몇 명에게 보일지 정해요.", "Build the ride but keep the curtain drawn, and a switch decides who gets to see it."),
         "small": ("코드를 다시 올리지 않고 바로 켜고 꺼요.", "Flip it on or off without redeploying any code."),
         "tricks": (4, [
             (CURTAIN_I, ("짓는 것과 보여주는 걸 나눠요", "Separate building from showing"), ("완성과 공개는 달라요", "finished isn't the same as visible"), "calm"),
             (DIAL_I, ("스위치로 몇 명에게 보일지 정해요", "A switch decides who sees it"), ("직원만, 일부만, 전체도요", "staff, a slice, or everyone")),
             (KILL_I, ("문제 생기면 스위치만 꺼요", "If it breaks, just flip it off"), ("재배포가 필요 없어요", "no redeploy needed"), "warm"),
             (TARGET_I, ("다 되면 커튼을 걷어요", "When it's ready, lift the curtain"), ("완전히 공개해요", "and open it to everyone")),
         ])},
        {"svg": P4, "alt": ("커튼 친 기구 앞에서 직원 한 명이 먼저 보고, 손님 한 명이 다음으로 보고, 공개 비율 계기판 다이얼이 조금씩 돌아감", "In front of the curtained ride, one staff member sees it first, then one guest, while a release-percentage dial turns little by little"),
         "caption": ("다이얼을 조금씩 돌려요 — 직원만, 1% 손님, 그다음 전체.", "Turn the dial a little at a time — staff only, then 1% of guests, then everyone."),
         "small": ("각 단계에서 문제가 없는지 확인하고 넘어가요.", "Each step is checked before moving to the next.")},
        {"svg": P5, "alt": ("켜진 스위치 목록판에 네 줄이 있고, 마지막 줄엔 누가 왜 켰는지 기억이 안 난다고 적혀 있음. 정비사가 당황한 표정", "A board listing switches currently on has four lines, the last saying no one remembers who turned it on or why — a flustered mechanic looks on"),
         "caption": ("커튼(스위치)이 너무 많아지면, 뭐가 켜져 있는지 관리하기 어려워요.", "Too many curtains (switches), and it gets hard to track what's even on."),
         "small": ("다 되면 커튼 자체를 치워야 해요.", "Once it's done, the curtain itself has to come down.")},
    ],
    "summary": (("<b>피처 플래그</b> = 새 기구를 <b>지어 두고 커튼을 친 채</b>, <b>스위치 하나</b>로 <b>몇 명에게 보일지</b>를 코드 재배포 없이 바로 정하는 일.",
                 "<b>Feature flags</b> = building a new ride and <b>leaving the curtain drawn</b>, using <b>one switch</b> to decide <b>who sees it</b>, instantly, without redeploying code."),
                ("Feature flag. 배포(코드를 서버에 올리는 것)와 공개(사용자에게 보이는 것)를 분리하는 기법이에요. 점진적 공개(롤아웃)로 위험을 줄이고, 문제가 생기면 킬 스위치로 즉시 끄고, 특정 대상에게만 먼저 보여주는 다크 런치에도 쓰여요.",
                 "A technique that separates deploying code (pushing it to servers) from releasing it (showing it to users). It lowers risk through a gradual rollout, lets you flip a kill switch the instant something breaks, and powers dark launches that show a feature to a narrow audience first.")),
    "glossary": [
        ("피처 플래그", "Feature flag", ("새 기구에 친 커튼과 그 스위치.", "The curtain over a new ride, and its switch."), ("짓는 것과 보여주는 걸 나눠 줘요.", "Separates building something from showing it.")),
        ("점진적 공개", "Gradual rollout", ("직원 → 1% 손님 → 전체로 늘려 가는 것.", "Widening from staff, to 1% of guests, to everyone."), ("단계마다 확인하고 넘어가요.", "Each step gets checked before the next.")),
        ("킬 스위치", "Kill switch", ("문제 생기면 바로 끄는 스위치.", "The switch you flip off the instant something breaks."), ("코드를 다시 올릴 필요가 없어요.", "No need to redeploy any code.")),
        ("대상 지정", "Targeting", ("누구에게 먼저 보여줄지 정하는 것.", "Deciding who gets to see it first."), ("직원만, 특정 지역 손님만 같은 거예요.", "Like staff only, or guests in one region only.")),
        ("다크 런치", "Dark launch", ("손님 몰래 일부에게만 먼저 켜 보는 것.", "Quietly turning it on for a slice of guests first."), ("손님 눈엔 아직 커튼이 쳐진 것처럼 보여요.", "To most guests, the curtain still looks drawn.")),
        ("카나리와의 관계", "Relation to canary", ("카나리는 서버 몇 대만 새 버전, 플래그는 같은 서버에서 화면만 다르게.", "A canary runs a new version on a few servers; a flag shows a different screen on the very same servers."), ("둘 다 위험을 조금씩 나눠 보는 방법이에요.", "Both are ways of trying something on a small slice first.")),
        ("블루-그린과의 차이", "Difference from blue-green", ("블루-그린은 통째로 바꿨다 되돌리고, 플래그는 사람 단위로 나눠서 보여줘요.", "Blue-green swaps the whole thing and back; a flag splits by person instead."), ("둘은 되돌리는 단위가 달라요.", "They differ in the unit they roll back.")),
        ("A/B 테스트", "A/B testing", ("손님을 나눠 두 가지 버전을 보여주고 비교하는 것.", "Showing two versions to different guests and comparing them."), ("같은 스위치 기술로 실험도 할 수 있어요.", "The same switch technology can run experiments, too.")),
    ],
}
