from _draw import *
from _world import *

VOTE_YES = '<circle r="13" fill="var(--good)"/><path d="M-6 0 l4 5 l9 -11" stroke="#FFF8E7" stroke-width="3" fill="none" stroke-linecap="round"/>'
VOTE_NO = '<circle r="13" fill="var(--bad)"/><path d="M-6 -6 l12 12 M6 -6 l-12 12" stroke="#FFF8E7" stroke-width="3" fill="none"/>'


def room(x, y, label_text="", vote=None):
    out = controlroom(x, y, 120, 80, bars=((0.5, "var(--good)"), (0.7, "var(--accent)")))
    out += label(x + 60, y + 96, label_text, 10, "var(--muted)")
    if vote is not None:
        out += f'<g transform="translate({x + 60},{y - 14})">{VOTE_YES if vote else VOTE_NO}</g>'
    return out


# 1. 관제실이 여러 곳인데 "오늘 누가 당번이지?" 다 다르게 말함
P1 = svg(300, sky(300)
         + room(30, 120, "⟦관제실 A|ROOM A⟧") + room(210, 120, "⟦관제실 B|ROOM B⟧") + room(390, 120, "⟦관제실 C|ROOM C⟧")
         + bubble(20, 30, 130, 44, "⟦내가 당번!|I'm on call!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + bubble(200, 30, 140, 44, "⟦아니 나예요|no, it's me⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + bubble(380, 30, 160, 44, "⟦둘 다 아닌데요|neither of you⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦관제실이 여러 곳인데 다 다르게 말해요|several control rooms, and each says something different⟧", 12, "var(--ink)"))

# 2. 왜: 여러 곳이 동시에 각자 정하면 어긋나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + room(90, 110) + room(320, 110) + room(550, 110)
         + '<path d="M150 200 L380 200 L610 200" stroke="var(--bad)" stroke-width="4" stroke-dasharray="4 6" fill="none"/>'
         + label(380, 240, "⟦서로 연락 없이 각자 정해요|deciding alone, with no word to each other⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦여러 곳이 동시에 각자 정하면 어긋나요|when several decide alone at once, things stop matching⟧", 12, "var(--ink)"))

# 3. hero: 손을 들어 과반수로 정해요 (5곳 중 3곳 찬성)
P3 = svg(340, sky(340)
         + room(10, 150, "⟦A|A⟧", vote=True) + room(150, 150, "⟦B|B⟧", vote=True) + room(290, 150, "⟦C|C⟧", vote=False)
         + room(430, 150, "⟦D|D⟧", vote=True) + room(570, 150, "⟦E|E⟧", vote=False)
         + board(260, 40, 240, 80, "⟦투표 결과|VOTE⟧", ("⟦찬성 3 / 전체 5 → 확정|3 of 5 agree → decided⟧",), 1.0)
         + label(380, 300, "⟦과반수(3곳)가 동의해서 \"A 기구부터\"로 확정!|a majority (3 of 5) agrees: \"ride A goes first\" is decided⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦손을 들어 반이 넘으면 확정돼요 — 이게 합의예요|raise hands, and once more than half agree, it's settled — that's consensus⟧", 11, "var(--muted)"))

# 4. 작동 디테일: 한두 곳이 멈춰도 결정 가능, 모두 같은 기록
P4 = svg(320, sky(320)
         + room(30, 120, "⟦A|A⟧", vote=True) + room(190, 120, "⟦B(멈춤)|B (down)⟧") + room(350, 120, "⟦C|C⟧", vote=True) + room(510, 120, "⟦D|D⟧", vote=True)
         + '<path d="M250 160 l-20 -20 M250 180 l-20 20" stroke="var(--bad)" stroke-width="4" fill="none"/>'
         + board(600, 60, 140, 90, "⟦모두 같은 기록|SAME LOG⟧", ("⟦결정은 하나|one decision⟧",), 0.9)
         + label(380, 286, "⟦한두 곳이 멈춰도 나머지로 결정하고, 새 당번 뽑기도 같은 방식이에요|even if one or two are down, the rest can still decide — and a new leader is chosen the same way⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 투표가 느려서 급한 결정엔 안 쓰고 중요한 결정에만
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + room(60, 90, "⟦A|A⟧") + room(220, 90, "⟦B|B⟧")
         + label(190, 220, "⟦모두 기다려야 해요 — 느려요|everyone has to wait — it's slow⟧", 11, "var(--bad)", cls="d")
         + board(460, 70, 240, 130, "⟦그래서|SO⟧", ("⟦급한 결정엔 안 써요|not for urgent calls⟧", "⟦중요한 결정에만 써요|only for important ones⟧"), 1.0)
         + label(380, 282, "⟦투표가 느려서 아무 데나 쓰진 않아요|voting is slow, so it isn't used for everything⟧", 12, "var(--ink)"))

HAND_I = icon('<path d="M20 50 V26 a4 4 0 0 1 8 0 V22 a4 4 0 0 1 8 0 V20 a4 4 0 0 1 8 0 V24 a4 4 0 0 1 8 0 V40 q0 14 -12 14 h-10 q-10 0 -10 -4z" fill="var(--accent)"/>')
MAJORITY_I = icon('<circle cx="20" cy="24" r="9" fill="var(--good)"/><circle cx="44" cy="24" r="9" fill="var(--good)"/><circle cx="32" cy="42" r="9" fill="var(--stone)"/><path d="M14 54 h36" stroke="var(--ink)" stroke-width="3" fill="none"/>')
RESILIENT_I = icon('<circle cx="18" cy="32" r="10" fill="var(--good)"/><circle cx="32" cy="32" r="10" fill="var(--bad)"/><circle cx="46" cy="32" r="10" fill="var(--good)"/><path d="M26 24 l12 16 M38 24 l-12 16" stroke="var(--bad)" stroke-width="3" fill="none"/>')
SLOW_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 V32 L42 38" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "consensus", "order": 12,
    "title": ("여러 관제실이 손 들어 정하기", "Control Rooms Raising Hands to Decide"),
    "h1": ("<em>합의</em>가 뭐예요?", "What is <em>Consensus</em>?"),
    "sub": ("합의(컨센서스)를 여러 관제실이 손을 들어 과반수로 결정하는 이야기로 풀어봤어요.",
            "Consensus, told as a story about control rooms raising hands until a majority agrees."),
    "panels": [
        {"svg": P1, "alt": ("관제실 세 곳이 각자 '내가 당번이야', '아니 나예요', '둘 다 아닌데요' 라고 말함", "Three control rooms each claim to be on call, disagreeing with each other"),
         "caption": ("관제실이 여러 곳인데 다 다르게 말해요.", "Several control rooms, and each says something different."),
         "small": ("오늘 당번이 누구인지조차 서로 달라요.", "They can't even agree on who's on call today.")},
        {"svg": P2, "alt": ("관제실 세 곳이 서로 연락 없이 선을 끊은 채 각자 결정함", "Three control rooms, disconnected from each other, each deciding alone"),
         "caption": ("여러 곳이 동시에 각자 정하면 어긋나요.", "When several decide alone at once, things stop matching."),
         "small": ("서로 말을 맞추지 않으면 결정이 흩어져요.", "Without talking to each other, decisions scatter.")},
        {"svg": P3, "hero": True, "alt": ("관제실 다섯 곳 중 세 곳이 찬성 표시를 들어 'A 기구부터'로 확정되는 투표", "Three of five control rooms show a yes vote, settling on ride A going first"),
         "caption": ("결정할 일이 생기면 손을 들어 과반수로 정해요.", "Raise hands, and once more than half agree, it's settled."),
         "small": ("찬성이 반을 넘으면(쿼럼) 확정돼요.", "Once agreement clears half (a quorum), it's final."),
         "tricks": (4, [
             (HAND_I, ("홀수로 둬요", "Use an odd number"), ("3, 5처럼요", "like 3 or 5"), "calm"),
             (MAJORITY_I, ("반이 넘어야 확정", "More than half must agree"), ("과반수(쿼럼)예요", "that's a quorum")),
             (RESILIENT_I, ("한두 곳이 멈춰도 돼요", "A couple can be down"), ("나머지로 결정 가능해요", "the rest can still decide"), "warm"),
             (SLOW_I, ("새 당번도 같은 방식", "New leader, same method"), ("리더 선출이에요", "that's leader election")),
         ])},
        {"svg": P4, "alt": ("관제실 B가 멈췄지만 A, C, D 세 곳이 여전히 투표해 결정하고, 모두 같은 기록을 가짐", "Room B is down but A, C, and D still vote and decide, with everyone sharing the same log"),
         "caption": ("한두 곳이 멈춰도 나머지로 결정할 수 있어요.", "Even if one or two are down, the rest can still decide."),
         "small": ("모두 같은 결정 기록을 갖고, 새 당번 뽑기도 같은 방식이에요.", "Everyone ends up with the same log, and a new leader is picked the same way.")},
        {"svg": P5, "alt": ("왼쪽: 관제실 둘이 투표를 기다리며 느림. 오른쪽: 급한 결정엔 안 쓰고 중요한 결정에만 쓴다는 안내판", "Left: two control rooms waiting slowly on a vote. Right: a sign saying this is for important decisions only, not urgent ones"),
         "caption": ("투표가 느려요 — 모두 기다려야 해요.", "Voting is slow — everyone has to wait."),
         "small": ("그래서 급한 결정엔 안 쓰고, 중요한 결정에만 써요.", "So it isn't used for urgent calls — only for the important ones.")},
    ],
    "summary": (("<b>합의</b> = 관제실 여러 곳이 <b>손을 들어 과반수</b>로 하나의 결정을 확정하는 일. <b>한두 곳이 멈춰도</b> 나머지로 결정할 수 있지만, 그만큼 <b>느려요</b>.",
                 "<b>Consensus</b> = several control rooms <b>raising hands until a majority</b> agrees on one decision. The rest can still decide even if <b>a couple are down</b> — but it's correspondingly <b>slow</b>."),
                ("분산 시스템에서 여러 노드가 하나의 값에 동의하도록 만드는 방법이에요. 과반수 동의를 쿼럼이라 부르고, Raft·Paxos 같은 알고리즘이 이를 구현해요. 느리기 때문에 모든 결정이 아니라 리더 선출 같은 중요한 결정에만 써요.",
                 "A way to get multiple nodes in a distributed system to agree on one value. Majority agreement is called a quorum, and algorithms like Raft and Paxos implement it. Because it's slow, it's reserved for important decisions like leader election, not every decision.")),
    "glossary": [
        ("합의(컨센서스)", "Consensus", ("관제실 여럿이 손 들어 하나로 정하는 일.", "Several control rooms raising hands to settle on one answer."), ("모두가 같은 결정을 갖게 만들어요.", "It leaves everyone with the same decision.")),
        ("쿼럼", "Quorum", ("확정되려면 넘어야 하는 과반수.", "The majority threshold a decision must clear."), ("보통 '반 넘게'예요.", "Usually means \"more than half.\"")),
        ("리더 선출", "Leader election", ("새 당번을 뽑는 투표.", "The vote that picks a new on-call leader."), ("결정을 뽑는 것과 같은 방식이에요.", "Done the same way as voting on a decision.")),
        ("Raft/Paxos", "Raft / Paxos", ("합의를 실제로 구현한 알고리즘 이름.", "Names of algorithms that implement consensus in practice."), ("이름만 알아둬도 충분해요.", "Knowing the names is enough for now.")),
        ("과반수", "Majority", ("전체의 반을 넘는 수.", "More than half of the total."), ("쿼럼을 채우는 기준이에요.", "This is what fills a quorum.")),
        ("분산 합의 비용", "Cost of distributed consensus", ("모두 기다려야 해서 생기는 느림.", "The slowness from everyone having to wait."), ("그래서 급한 결정엔 안 써요.", "That's why it's not used for urgent decisions.")),
        ("스플릿 브레인", "Split-brain", ("합의 없이 둘 다 당번이라 우기는 상태.", "Two sides both insisting they're on call, with no agreement."), ('합의가 없으면 이런 일이 생겨요. → <a href="splitbrain-ko.html">두 관제실이 서로 자기가 진짜라고</a>', 'This is what happens without consensus. → <a href="splitbrain-en.html">two control rooms each insisting they\'re the real one</a>')),
        ("복제", "Replication", ("원본이 바뀔 때 새 원본을 뽑는 데도 합의가 쓰여요.", "Consensus is also used to pick a new leader when replication needs one."), ('→ <a href="replication-ko.html">손님 명부를 두 창고에 똑같이</a>', '→ <a href="replication-en.html">the same guest log in two warehouses</a>')),
    ],
}
