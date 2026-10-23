from _draw import *
from _world import *


def desk(x, y, s=1.0, text=None):
    """교정 책상(공유 자원). 한 번에 한 사람만 쓸 수 있어요."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" y="-10" width="72" height="14" rx="2" fill="#8B5E3C"/>'
           f'<rect x="-30" y="4" width="8" height="26" fill="#5A3B22"/><rect x="22" y="4" width="8" height="26" fill="#5A3B22"/>'
           f'<rect x="-24" y="-20" width="48" height="12" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/></g>')
    if text:
        out += label(x, y + 46, text, 11, "var(--muted)")
    return out


# 1. 급한 베스트셀러가 책상을 기다림 — 여유 있는 재인쇄가 책상을 쓰는 중
P1 = svg(300, sky(300)
         + desk(380, 150, 1.0, "⟦교정 책상(한 번에 한 사람만)|the proofing desk (one person at a time)⟧")
         + person(300, 100, s=0.6, face=EYES, **PROOFER)
         + person(140, 150, s=0.85, face=SWEAT, **WRITER)
         + bubble(30, 60, 220, 44, "⟦급한데... 책상이 비어야 해요|it's urgent... but the desk is taken⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(620, 230, "⟦H: 급한 베스트셀러|H: urgent bestseller⟧", 11, "var(--muted)")
         + label(300, 70, "⟦L: 여유 있는 재인쇄|L: unhurried reprint⟧", 11, "var(--muted)"))

# 2. 중간 우선순위가 계속 끼어들어 L이 책상을 못 비움 — H가 하염없이 기다림
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + desk(380, 140, 1.0)
         + person(300, 90, s=0.6, face=SWEAT, **PROOFER)
         + person(540, 90, s=0.6, face=EYES, **EDITOR)
         + bubble(440, 10, 200, 40, "⟦저부터 잠깐만요!|me first, just a moment!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(140, 150, s=0.8, face=FROWN + SWEAT, **WRITER)
         + label(380, 250, "⟦M(중간 우선순위)이 자꾸 끼어들어 L이 책상을 못 비워요|M (medium priority) keeps cutting in, so L never gets to finish⟧", 12, "var(--bad)")
         + label(380, 280, "⟦그 사이 H(급한 일)는 하염없이 기다려요 — 우선순위 역전|meanwhile H (urgent) waits forever — priority inversion⟧", 12, "var(--ink)", cls="d"))

# 3. 편집장이 L의 우선순위를 잠깐 H만큼 올려줌 (hero)
P3 = svg(340, sky(340)
         + person(220, 120, s=0.85, face=EYES, **EDITOR)
         + bubble(260, 60, 240, 44, "⟦그동안은 L을 H만큼 급하게 쳐줄게요|while this lasts, L counts as urgent as H⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + desk(560, 165, 1.0) + person(560, 95, s=0.55, face=SMILE, **PROOFER)
         + label(380, 30, "⟦우선순위 상속 = 책상 쓰는 동안만 L의 순위를 H만큼 임시로 올리기|Priority inheritance = temporarily raising L's priority to H's level, just while it holds the desk⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦그러면 M이 못 끼어들고, L이 금방 끝내 책상을 비워줘요|then M can't cut in, and L finishes quickly and frees the desk⟧", 12, "var(--muted)"))

SWAP_I = icon('<path d="M14 24 h28 M34 18 l8 6 l-8 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 40 h-28 M30 34 l-8 6 l8 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LOCK_I = icon('<rect x="18" y="28" width="28" height="22" rx="4" fill="var(--accent)"/><path d="M24 28 v-8 a8 8 0 0 1 16 0 v8" stroke="var(--ink)" stroke-width="4" fill="none"/>')
BOOST_I = icon('<path d="M32 50 V16" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/><path d="M22 26 L32 14 L42 26" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
RESET_I = icon('<path d="M46 20 A18 18 0 1 0 50 34" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M46 10 v12 h-12" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "priorityinv", "order": 36,
    "title": ("급한 책이 유령처럼 멈춰요", "The Urgent Book Stalls Like a Ghost"),
    "h1": ("<em>우선순위 역전/상속</em>이 뭐예요?", "What is <em>Priority Inversion/Inheritance</em>?"),
    "sub": ("급한 일이 사소한 일 때문에 하염없이 기다리는 문제와, 그걸 푸는 임시 처방 이야기예요.",
            "A story about an urgent task stuck waiting on a trivial one — and the temporary fix for it."),
    "panels": [
        {"svg": P1, "alt": ("급한 베스트셀러 작가(H)가 교정 책상이 비기를 기다리는데, 여유 있는 재인쇄 교정(L)이 책상을 쓰고 있음", "The urgent bestseller author (H) waits for the proofing desk, while the unhurried reprint task (L) is using it"),
         "caption": ("급한 베스트셀러(H)가 교정 책상을 기다려요.", "The urgent bestseller (H) waits for the proofing desk."),
         "small": ("지금은 여유 있는 재인쇄(L)가 책상을 쓰고 있어요.", "Right now the unhurried reprint (L) is using the desk.")},
        {"svg": P2, "alt": ("중간 우선순위 홍보 전단(M)이 계속 끼어들어 L이 책상을 비우지 못하고, H는 하염없이 기다림", "The medium-priority flyer task (M) keeps cutting in, so L never frees the desk, and H waits endlessly"),
         "caption": ("중간 우선순위(M)가 자꾸 끼어들어요.", "The medium-priority task (M) keeps cutting in line."),
         "small": ("그 사이 급한 일(H)은 하염없이 기다려요 — 이게 우선순위 역전이에요.", "Meanwhile the urgent task (H) waits forever — this is priority inversion.")},
        {"svg": P3, "hero": True, "alt": ("편집장이 L의 우선순위를 책상을 쓰는 동안만 H만큼 임시로 올려줌", "The editor temporarily raises L's priority to H's level, just while L holds the desk"),
         "caption": ("우선순위 상속 = 책상 쓰는 동안만 L의 순위를 임시로 올리는 거예요.", "Priority inheritance = temporarily raising L's priority, just while it holds the desk."),
         "small": ("그러면 M이 못 끼어들고, L이 금방 끝내 책상을 비워줘요.", "Then M can't cut in, and L finishes quickly and frees the desk."),
         "tricks": (4, [
             (LOCK_I, ("공유 자원 확인", "Spot the shared resource"), ("모두가 기다리는 교정 책상", "the proofing desk everyone waits for"), "calm"),
             (SWAP_I, ("역전 알아채기", "Notice the inversion"), ("급한 일이 중간 일 때문에 막힘", "the urgent task is blocked by a medium one")),
             (BOOST_I, ("우선순위 임시로 올리기", "Temporarily boost priority"), ("L을 H 수준으로 올려줘요", "raise L to H's level"), "warm"),
             (RESET_I, ("끝나면 되돌리기", "Reset when done"), ("책상을 비우면 원래 순위로", "back to normal once the desk is free")),
         ])},
        {"svg": svg(320, sky(320, ground=False)
                     + label(130, 40, "⟦역전 발생|inversion happens⟧", 13, "var(--bad)")
                     + '<rect x="60" y="60" width="140" height="28" rx="4" fill="var(--good)"/>'
                     + '<rect x="200" y="60" width="220" height="28" rx="4" fill="var(--accent)"/>'
                     + '<rect x="420" y="60" width="60" height="28" rx="4" fill="var(--good)"/>'
                     + label(260, 110, "⟦L(여유)이 M에게 계속 밀려요|L (unhurried) keeps getting bumped by M⟧", 11, "var(--muted)")
                     + '<rect x="480" y="60" width="170" height="28" rx="4" fill="#5B8DEF" opacity="0.5" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 3"/>'
                     + label(565, 110, "⟦H가 한참을 기다려요|H waits a long time⟧", 11, "var(--bad)")
                     + label(130, 190, "⟦상속 적용|inheritance applied⟧", 13, "var(--good)")
                     + '<rect x="60" y="210" width="100" height="28" rx="4" fill="var(--good)"/>'
                     + '<rect x="160" y="210" width="500" height="28" rx="4" fill="#5B8DEF"/>'
                     + label(410, 260, "⟦L이 금방 끝나고, H가 바로 시작해요|L finishes fast, and H starts right away⟧", 11, "var(--ink)")),
         "alt": ("위: 상속 적용 전 타임라인 — L이 M에게 계속 밀려 H가 오래 기다림. 아래: 상속 적용 후 — L이 금방 끝나고 H가 바로 시작함", "Top: timeline before inheritance — L keeps getting bumped by M, so H waits a long time. Bottom: after inheritance — L finishes fast and H starts right away"),
         "caption": ("시간선으로 보면 차이가 분명해요.", "On a timeline, the difference is clear."),
         "small": ("상속을 적용하면 L이 금방 끝나고, H가 바로 시작해요.", "With inheritance, L finishes quickly and H starts right away.")},
        {"svg": svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
                     + person(190, 130, s=0.8, face=SMILE, **WRITER) + label(190, 260, "⟦H가 예측 가능하게 끝나요|H finishes predictably⟧", 11, "var(--ink)")
                     + person(570, 130, s=0.8, face=EYES, **EDITOR) + label(570, 260, "⟦책상이 여러 개면 더 복잡해져요|more desks make it more complex⟧", 11, "var(--ink)")
                     + label(380, 305, "⟦상속은 책상 하나짜리 역전엔 잘 듣지만, 만능 해결책은 아니에요|inheritance works well for a single shared desk, but it's no cure-all⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 상속 덕분에 H가 예측 가능하게 끝남. 오른쪽: 공유 자원이 여러 개면 더 복잡해짐", "Left: thanks to inheritance, H finishes predictably. Right: with several shared resources, things get more complex"),
         "caption": ("상속도 만능은 아니에요.", "Inheritance isn't a cure-all either."),
         "small": ("공유 자원이 여러 개거나 겹치면, 더 정교한 방식(우선순위 천장)이 필요해요.", "With multiple or overlapping shared resources, a more careful scheme (priority ceiling) is needed.")},
    ],
    "summary": (("<b>우선순위 역전</b>은 급한 일(H)이 사소한 일(L)이 쥔 자원을 기다리다, 중간 일(M)에 밀려 하염없이 지연되는 문제이고, <b>우선순위 상속</b>은 L이 자원을 쥔 동안만 L의 순위를 H만큼 올려 이를 막는 처방이에요.",
                 "<b>Priority inversion</b> is when an urgent task (H), waiting on a resource held by a trivial task (L), gets stuck indefinitely because a medium task (M) keeps cutting in; <b>priority inheritance</b> fixes it by temporarily raising L's priority to H's level while L holds the resource."),
                ("실시간 시스템에서 높은 우선순위 작업이 낮은 우선순위 작업이 점유한 공유 자원(뮤텍스 등)을 기다릴 때, 중간 우선순위 작업이 끼어들면 대기 시간이 예측 불가능하게 늘어나는 현상이 우선순위 역전이에요. 우선순위 상속 프로토콜은 자원을 쥔 낮은 우선순위 작업의 우선순위를 일시적으로 높여 중간 작업의 선점을 막아요. 자원이 여럿이거나 중첩되면 우선순위 천장 프로토콜 같은 더 정교한 기법이 쓰여요.",
                 "In real-time systems, when a high-priority task waits on a shared resource (like a mutex) held by a low-priority task, a medium-priority task cutting in can make the wait unpredictably long — this is priority inversion. The priority inheritance protocol temporarily boosts the low-priority holder's priority so medium tasks can't preempt it. With multiple or nested resources, more elaborate schemes like priority ceiling protocol are used.")),
    "glossary": [
        ("우선순위 역전", "Priority Inversion", ("급한 일이 중간 일 때문에 하염없이 기다리는 것.", "An urgent task stuck waiting because of a medium one."), ("실시간 시스템의 대표적 함정이에요.", "A classic pitfall in real-time systems.")),
        ("우선순위 상속", "Priority Inheritance", ("자원을 쥔 동안만 낮은 순위를 임시로 올리기.", "Temporarily raising a low priority while it holds a resource."), ("우선순위 역전을 막는 처방이에요.", "The fix that prevents priority inversion.")),
        ("공유 자원/임계구역", "Shared Resource / Critical Section", ("한 번에 한 사람만 쓰는 교정 책상.", "The proofing desk only one person can use at a time."), ("역전이 일어나는 바로 그 지점이에요.", "The exact spot where inversion happens.")),
        ("뮤텍스/락", "Mutex / Lock", ("책상을 쓰는 동안 거는 잠금.", "The lock held while using the desk."), ("공유 자원을 지키는 실제 도구예요.", "The actual mechanism protecting the shared resource.")),
        ("우선순위 천장 프로토콜", "Priority Ceiling Protocol", ("자원이 여럿일 때 쓰는 더 정교한 방식.", "A more elaborate scheme for multiple resources."), ("우선순위 상속의 확장판이에요.", "An extension of priority inheritance.")),
        ("실시간 시스템", "Real-time System", ("마감 시간이 결과만큼 중요한 시스템.", "A system where the deadline matters as much as the result."), ("우선순위 역전이 특히 치명적인 곳이에요.", "Where priority inversion is especially dangerous.")),
        ("데드락과 차이", "Difference from Deadlock", ("데드락은 서로 영원히 묶이는 것.", "Deadlock is two tasks permanently stuck on each other."), ("역전은 언젠가는 풀리지만, 너무 늦게 풀려요.", "Inversion does resolve eventually — just far too late.")),
        ("스케줄링", "Scheduling", ("누가 먼저 책상을 쓸지 정하는 규칙.", "The rule for who gets the desk first."), ("우선순위 역전은 스케줄링의 부작용이에요.", "Priority inversion is a side effect of scheduling.")),
    ],
}
