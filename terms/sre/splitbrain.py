from _draw import *
from _world import *

# 1. 연결이 끊긴 사이 관제실 둘이 각자 "내가 당번이야!" 하며 다른 지시를 내림
P1 = svg(300, sky(300)
         + controlroom(60, 110, 180, 110) + controlroom(520, 110, 180, 110)
         + person(100, 164, s=0.6, face=EYES, **OPERATOR) + person(560, 164, s=0.6, face=EYES, **OPERATOR)
         + bubble(50, 20, 190, 46, "⟦내가 당번이야! A부터 켜요|I'm on call! Start ride A⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble(510, 20, 200, 46, "⟦내가 당번이야! B부터 켜요|I'm on call! Start ride B⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + '<path d="M240 165 h280" stroke="var(--stone-dark)" stroke-width="4" stroke-dasharray="2 10" fill="none"/>'
         + label(380, 282, "⟦연결이 끊긴 사이 둘 다 자기가 당번이래요|the line is down, and both claim to be on call⟧", 12, "var(--ink)"))

# 2. 왜: 통신선이 끊기면 서로 상대가 죽은 줄 알아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + controlroom(60, 100, 170, 100) + controlroom(530, 100, 170, 100)
         + '<path d="M230 150 h300" stroke="var(--bad)" stroke-width="5" fill="none"/><path d="M360 135 l20 15 -20 15 M400 135 l-20 15 20 15" stroke="var(--bad)" stroke-width="4" fill="none"/>'
         + person(100, 154, s=0.55, face=FROWN, **OPERATOR) + bubble(40, 220, 190, 44, "⟦저쪽이 죽었나봐요|that side must be down⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(570, 154, s=0.55, face=FROWN, **OPERATOR) + bubble(500, 220, 200, 44, "⟦저쪽이 죽었나봐요|that side must be down⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦통신선이 끊기면 서로 상대가 죽은 줄 알아요|when the line breaks, each side assumes the other is gone⟧", 12, "var(--ink)"))

# 3. hero: 둘 다 혼자 당번이라 믿고 동시에 지시해서 공원이 어긋나요 — 스플릿 브레인
P3 = svg(340, sky(340)
         + controlroom(50, 130, 190, 110) + controlroom(520, 130, 190, 110)
         + person(90, 184, s=0.6, face=EYES, **OPERATOR) + person(610, 184, s=0.6, face=EYES, **OPERATOR)
         + ride(200, 300, 0.6, color="var(--accent)") + ride(560, 300, 0.6, color="#5B8DEF", closed=True)
         + '<path d="M240 185 L520 185" stroke="var(--bad)" stroke-width="4" stroke-dasharray="2 10" fill="none"/>'
         + '<path d="M365 150 l14 30 l-10 0 l14 30 l-30 -36 l12 0z" fill="var(--bad)"/>'
         + label(380, 40, "⟦둘 다 \"나 혼자 당번\"이라 믿고 동시에 지시해요 — 스플릿 브레인|both believe they're the only one on call, and give orders at the same time — split-brain⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦한쪽은 A를 켜고 한쪽은 B를 꺼서, 공원이 어긋나요|one turns ride A on, the other turns ride B off — the park falls out of sync⟧", 11, "var(--muted)"))

# 4. 막는 법 4 tricks
P4 = svg(300, sky(300)
         + board(260, 40, 240, 180, "⟦막는 법|HOW TO PREVENT⟧",
                 ("⟦홀수로 둬요(3, 5)|use odd numbers (3, 5)⟧", "⟦과반 못 모으면 스스로 멈춰요|can't reach a majority → pause itself⟧",
                  "⟦복구되면 하나만 남겨요|once fixed, keep only one⟧", "⟦평소에 연습해 둬요|practice it ahead of time⟧"), 1.0)
         + label(380, 282, "⟦과반수로만 당번을 인정하면 둘 다 우기는 일이 없어요|only recognizing a majority means no more double claims⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 이미 어긋난 지시가 나간 뒤엔 되돌리기 어려워요
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(170, 230, 0.75, color="var(--accent)") + ride(380, 230, 0.75, color="#5B8DEF", closed=True) + ride(590, 230, 0.75, color="var(--stone)", closed=True)
         + label(380, 90, "⟦지시 세 개가 이미 나갔어요|three orders already went out⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦이미 나간 지시는 되돌리기 어려워요 — 그래서 예방이 최선이에요|orders already sent are hard to undo — prevention is the real fix⟧", 12, "var(--ink)"))

ODD_I = icon('<circle cx="18" cy="32" r="8" fill="var(--good)"/><circle cx="32" cy="32" r="8" fill="var(--good)"/><circle cx="46" cy="32" r="8" fill="var(--good)"/>')
PAUSE_I = icon('<rect x="20" y="12" width="10" height="40" rx="3" fill="var(--bad)"/><rect x="36" y="12" width="10" height="40" rx="3" fill="var(--bad)"/>')
CLEAN_I = icon('<circle cx="24" cy="28" r="10" fill="var(--good)"/><path d="M40 10 l10 10 -24 24 -12 2 2 -12z" fill="var(--stone)" opacity="0.5"/><path d="M40 10 l10 10" stroke="var(--ink)" stroke-width="2" fill="none"/>')
DRILL_I = icon('<circle cx="32" cy="22" r="10" fill="var(--accent)"/><rect x="22" y="34" width="20" height="24" rx="4" fill="var(--accent)"/><path d="M14 46 q18 -14 36 0" stroke="var(--good)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "splitbrain", "order": 13,
    "title": ("두 관제실이 서로 자기가 진짜라고", "Two Control Rooms Each Insisting They're the Real One"),
    "h1": ("<em>스플릿 브레인</em>이 뭐예요?", "What is <em>Split-Brain</em>?"),
    "sub": ("스플릿 브레인을 연결이 끊긴 사이 관제실 둘이 서로 자기가 당번이라고 우기는 이야기로 풀어봤어요.",
            "Split-brain, told as a story about two control rooms, cut off from each other, each insisting it's the one in charge."),
    "panels": [
        {"svg": P1, "alt": ("관제실 두 곳이 연결이 끊긴 채 각자 자기가 당번이라며 다른 지시를 내림", "Two control rooms, disconnected, each claiming to be on call and giving different orders"),
         "caption": ("연결이 끊긴 사이 둘 다 자기가 당번이래요.", "The line is down, and both claim to be on call."),
         "small": ("서로 다른 지시가 동시에 나가요.", "Different orders go out from both sides at once.")},
        {"svg": P2, "alt": ("두 관제실 사이 통신선이 번개 모양으로 끊어지고, 둘 다 상대가 죽었다고 생각함", "The line between two control rooms snaps like lightning, and each assumes the other is down"),
         "caption": ("통신선이 끊기면 서로 상대가 죽은 줄 알아요.", "When the line breaks, each side assumes the other is gone."),
         "small": ("확인할 방법이 없으니 각자 판단해 버려요.", "With no way to check, each side just decides on its own.")},
        {"svg": P3, "hero": True, "alt": ("관제실 두 곳이 끊긴 선 양쪽에서 각자 다른 기구에 지시를 내리고, 가운데에 번개 모양 균열이 있음", "Two control rooms, split by a broken line, each giving orders to a different ride, with a lightning-shaped crack in the middle"),
         "caption": ("둘 다 혼자 당번이라 믿고 동시에 지시해서 공원이 어긋나요.", "Both believe they're the only one on call, and give orders at once — the park falls out of sync."),
         "small": ("이게 스플릿 브레인이에요.", "This is split-brain."),
         "tricks": (4, [
             (ODD_I, ("홀수로 둬요", "Use an odd number"), ("3, 5처럼요", "like 3 or 5"), "calm"),
             (PAUSE_I, ("과반 못 모으면 멈춰요", "Pause without a majority"), ("안전 모드예요", "that's a safe mode")),
             (CLEAN_I, ("복구되면 하나만 남겨요", "Keep only one, once fixed"), ("정리해요", "clean up the rest"), "warm"),
             (DRILL_I, ("평소에 연습해 둬요", "Practice ahead of time"), ("가짜 훈련으로요", "with a dry run")),
         ])},
        {"svg": P4, "alt": ("막는 법 안내판: 홀수로 두기, 과반 못 모으면 스스로 멈추기, 복구되면 하나만 남기기, 평소에 연습하기", "A sign listing how to prevent it: use odd numbers, pause without a majority, keep only one after recovery, practice ahead"),
         "caption": ("과반수로만 당번을 인정하면 우기는 일이 없어요.", "Only recognizing a majority means no more double claims."),
         "small": ("홀수로 두고, 끊기면 둘 다 멈추게 해요.", "Keep an odd number, and have both sides pause when cut off.")},
        {"svg": P5, "alt": ("이미 세 기구에 서로 다른 지시가 나가 일부는 켜지고 일부는 꺼진 채 어긋난 상태", "Three rides already received conflicting orders, left on or off out of sync"),
         "caption": ("이미 나간 지시는 되돌리기 어려워요.", "Orders already sent are hard to undo."),
         "small": ("그래서 예방이 최선이에요.", "So prevention is the real fix.")},
    ],
    "summary": (("<b>스플릿 브레인</b> = 연결이 끊긴 관제실 둘이 <b>각자 자기가 당번이라 믿고</b> 동시에 지시를 내려 공원이 어긋나는 일. <b>홀수로 두고 과반수</b>로만 인정해서 막아요.",
                 "<b>Split-brain</b> = two disconnected control rooms, each <b>believing it alone is in charge</b>, giving conflicting orders at the same time. Prevented by keeping an <b>odd number of rooms</b> and recognizing only a <b>majority</b>."),
                ("네트워크 파티션(통신 단절) 때문에 분산 시스템의 두 부분이 각자 리더라고 믿는 상태예요. 쿼럼(과반수)을 요구하면 양쪽 다 과반을 못 채워 스스로 멈추므로 막을 수 있어요. 가짜 리더를 강제로 끄는 걸 펜싱이라 해요.",
                 "A state where two parts of a distributed system each believe they're the leader, caused by a network partition. Requiring a quorum (a majority) prevents it, since neither side alone can reach one and both pause. Forcibly shutting down a fake leader is called fencing.")),
    "glossary": [
        ("스플릿 브레인", "Split-brain", ("관제실 둘이 서로 자기가 진짜라고 우기는 상태.", "Two control rooms each insisting they're the real one."), ("지시가 어긋나 공원이 흔들려요.", "Conflicting orders throw the park out of sync.")),
        ("네트워크 파티션", "Network partition", ("관제실 사이 통신선이 끊기는 일.", "The line between control rooms going down."), ("스플릿 브레인의 원인이에요.", "This is what causes split-brain.")),
        ("쿼럼", "Quorum", ("당번으로 인정받으려면 넘어야 하는 과반수.", "The majority a side must clear to be recognized as on call."), ('과반을 못 채우면 스스로 멈춰요. → <a href="consensus-ko.html">여러 관제실이 손 들어 정하기</a>', "Fail to reach it, and a side pauses itself. → <a href=\"consensus-en.html\">control rooms raising hands to decide</a>")),
        ("펜싱", "Fencing", ("가짜 당번을 강제로 끄는 일.", "Forcibly shutting a fake leader down."), ("정리 단계에서 해요.", "Done during cleanup.")),
        ("홀수 노드", "Odd node count", ("관제실을 3, 5처럼 홀수로 두는 것.", "Keeping control rooms at an odd number, like 3 or 5."), ("과반수가 애매해지는 걸 막아요.", "It keeps the majority from ever being ambiguous.")),
        ("안전 모드", "Safe mode", ("과반을 못 모으면 스스로 멈추는 것.", "Pausing itself when it can't reach a majority."), ("어긋난 지시를 내기 전에 멈춰요.", "It stops before conflicting orders go out.")),
        ("리더 선출", "Leader election", ("복구된 뒤 당번을 다시 정하는 투표.", "The vote that re-picks a leader after recovery."), ('→ <a href="consensus-ko.html">여러 관제실이 손 들어 정하기</a>', '→ <a href="consensus-en.html">control rooms raising hands to decide</a>')),
        ("다중 리전", "Multi-region", ("관제실이 서로 다른 도시에 있을 때도 같은 위험이 있어요.", "The same risk applies when control rooms sit in different cities."), ("도시 하나를 통째로 잃어도 버티려는 설계예요.", "A design meant to survive losing a whole city.")),
    ],
}
