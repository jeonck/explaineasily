from _draw import *
from _world import *

# 1. 고장난 기구에 계속 손님을 밀어 넣어요 — 다친 사람도 늘고 직원도 거기 매달려요
P1 = svg(300, sky(300)
         + ride(560, 230, 0.75, color="var(--bad)", closed=True, label_text="⟦고장|broken⟧")
         + queueline(70, 174, 6, 0.5, 30)
         + '<path d="M250 200 L490 212" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(470, 150, s=0.6, face=FROWN + SWEAT, extra=WRENCH, **MECHANIC)
         + bubble(300, 60, 220, 48, "⟦여기만 계속 붙잡고 있어요...|I'm stuck here the whole time...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 284, "⟦고장난 기구에 계속 손님을 보내면, 다치는 사람도 매달린 직원도 늘어나요|keep sending guests to a broken ride, and both hurt guests and a tied-up mechanic pile up⟧", 12, "var(--ink)"))

# 2. 왜: 안 되는 걸 계속 시도하면 시간과 자원만 낭비돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/><ellipse cx="380" cy="300" rx="440" ry="36" fill="var(--good-soft)"/>'
         + ride(380, 230, 0.8, color="var(--bad)", closed=True)
         + '<path d="M380 110 m-60 0 a60 60 0 1 1 120 0 a60 60 0 1 1 -120 0" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M440 70 l18 -6 l-2 20z" fill="var(--bad)"/>'
         + person(560, 150, s=0.6, face=FROWN + SWEAT, **MECHANIC)
         + label(560, 115, "⟦또 실패...|failed again...⟧", 11, "var(--bad)")
         + label(380, 284, "⟦안 되는 걸 계속 시도하면 시간과 자원만 낭비돼요|keep retrying what won't work, and you only waste time and resources⟧", 12, "var(--ink)"))

# 3. hero: 비상 버튼을 누르면 그 기구로는 아무도 안 보내요
PRESS_I = icon('<rect x="24" y="40" width="16" height="10" rx="2" fill="var(--stone-dark)"/><circle cx="32" cy="26" r="18" fill="var(--bad)" stroke="#7A1F17" stroke-width="3"/><path d="M32 18 v12 M26 24 l6 6 l6 -6" stroke="#FFF8E7" stroke-width="3" fill="none" stroke-linecap="round"/>')
BLOCKALL_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M17 17 L47 47" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
TESTONE_I = icon('<circle cx="32" cy="16" r="8" fill="var(--accent)"/><path d="M32 24 v16 M32 32 l-10 16 M32 32 l10 16" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
CYCLE_I = icon('<path d="M46 20 a18 18 0 1 0 4 14" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M50 10 l0 14 l-14 0z" fill="var(--good)"/>')

P3 = svg(360, sky(360)
         + ride(600, 260, 0.7, color="var(--bad)", closed=True, label_text="⟦고장 — 차단|broken — blocked⟧")
         + bigbutton(505, 225, 1.0, pressed=True)
         + ride(300, 260, 0.7, color="var(--good)", label_text="⟦다른 기구|another ride⟧")
         + queueline(60, 208, 4, 0.5, 30)
         + '<path d="M210 208 Q260 165 300 208" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + person(460, 120, s=0.5, face=EYES, hat=None, shirt="#C9822B") + label(460, 95, "⟦한 명만 몰래 시험|one guest tests quietly⟧", 10, "var(--muted)")
         + '<path d="M460 150 L560 225" stroke="var(--accent)" stroke-width="2" stroke-dasharray="3 3" fill="none"/>'
         + label(380, 38, "⟦계속 실패하면 버튼을 눌러요 — 그 기구로는 아무도 안 보내요|keep failing, and pressing the button sends no one there⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦잠깐 뒤 한 명만 몰래 보내보고 괜찮으면 다시 열어요|after a bit, one guest quietly tests it, and if it's fine, it reopens⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 닫힘(정상) → 열림(차단) → 반열림(시험) → 닫힘
P4 = svg(320, sky(320)
         + '<circle cx="150" cy="100" r="34" fill="var(--good)"/>' + '<path d="M136 100 l10 10 l20 -22" stroke="#FFF8E7" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
         + label(150, 152, "⟦닫힘 — 정상|CLOSED — normal⟧", 11, "var(--ink)")
         + '<circle cx="610" cy="100" r="34" fill="var(--bad)"/>' + '<path d="M596 86 L624 114 M624 86 L596 114" stroke="#FFF8E7" stroke-width="5" stroke-linecap="round"/>'
         + label(610, 152, "⟦열림 — 차단|OPEN — blocked⟧", 11, "var(--ink)")
         + '<circle cx="380" cy="215" r="30" fill="var(--accent)"/>' + label(380, 223, "?", 24, "#FFF8E7", weight=800)
         + label(380, 262, "⟦반열림 — 시험|HALF-OPEN — testing⟧", 11, "var(--ink)")
         + '<path d="M186 90 L574 90" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4" fill="none"/>' + '<path d="M560 84 l16 6 l-16 6z" fill="var(--muted)"/>' + label(380, 76, "⟦계속 실패하면|keep failing⟧", 10, "var(--muted)")
         + '<path d="M596 128 Q500 185 405 202" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4" fill="none"/>' + label(530, 190, "⟦잠깐 후|after a bit⟧", 10, "var(--muted)")
         + '<path d="M355 202 Q250 185 164 128" stroke="var(--muted)" stroke-width="2" stroke-dasharray="5 4" fill="none"/>' + label(230, 190, "⟦성공하면|if it works⟧", 10, "var(--muted)")
         + label(380, 302, "⟦성공하면 닫힘으로, 실패하면 다시 열림으로 돌아가요|succeed and it returns to closed; fail and it goes back to open⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 버튼이 너무 예민하면 멀쩡한데도 자꾸 차단해요
P5 = svg(300, sky(300)
         + ride(560, 230, 0.75, color="var(--good)", label_text="⟦사실 멀쩡해요|actually fine⟧")
         + bigbutton(470, 150, 0.85, pressed=True)
         + person(650, 150, s=0.55, face=FROWN, hat=None, shirt="#4A5A72")
         + bubble(540, 70, 200, 48, "⟦멀쩡한데 왜 막아요?|it's fine, why block it?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + queueline(60, 182, 4, 0.5, 30)
         + '<path d="M210 182 Q280 160 340 230" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
         + label(380, 284, "⟦버튼이 너무 예민하면 괜찮은데도 자꾸 차단해요 — 기준을 잘 잡아야 해요|too sensitive a button keeps blocking things that are fine — the threshold needs tuning⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "circuitbreaker", "order": 23,
    "title": ("고장나면 누르는 빨간 버튼", "The Red Button You Press When Something Breaks"),
    "h1": ("<em>서킷 브레이커</em>가 뭐예요?", "What is a <em>Circuit Breaker</em>?"),
    "sub": ("서킷 브레이커를 고장난 기구 앞 빨간 비상 버튼 이야기로 풀어봤어요.",
            "The circuit breaker, told as a story about the red emergency button in front of a broken ride."),
    "panels": [
        {"svg": P1, "alt": ("고장난 기구에 손님이 계속 밀려가고, 정비사가 거기 붙잡혀 '여기만 계속 붙잡고 있어요'라고 말함", "Guests keep getting sent to a broken ride while a mechanic is stuck there saying he's tied up the whole time"),
         "caption": ("고장난 기구에 계속 손님을 보내면, 다치는 사람도 매달린 직원도 늘어나요.", "Keep sending guests to a broken ride, and both hurt guests and a tied-up mechanic pile up."),
         "small": ("그 기구 하나에 시간과 사람이 계속 묶여요.", "Time and people keep getting tied down by that one ride.")},
        {"svg": P2, "alt": ("고장난 기구 주위를 빙빙 도는 화살표, 정비사가 '또 실패...'라고 지쳐서 말함", "An arrow loops endlessly around a broken ride while an exhausted mechanic says it failed again"),
         "caption": ("안 되는 걸 계속 시도하면 시간과 자원만 낭비돼요.", "Keep retrying what won't work, and you only waste time and resources."),
         "small": ("될 때까지 계속 두드려봐도 소용없어요.", "Knocking on a broken door forever doesn't help.")},
        {"svg": P3, "hero": True, "alt": ("고장난 기구 앞 빨간 버튼이 눌려 있고, 손님 줄은 다른 멀쩡한 기구로 돌려지며, 한 명만 몰래 고장난 기구를 시험해봄", "A red button is pressed in front of a broken ride, guests are routed to another ride, and one guest quietly tests the broken one"),
         "caption": ("계속 실패하면 버튼을 눌러요 — 그 기구로는 아무도 안 보내요.", "Keep failing, and pressing the button sends no one there."),
         "small": ("잠깐 뒤 한 명만 몰래 보내보고 괜찮으면 다시 열어요.", "After a bit, one guest quietly tests it, and if it's fine, it reopens."),
         "tricks": (4, [
             (PRESS_I, ("계속 실패하면 버튼 누르기", "Press the button on repeated failure"), ("차단해요", "that's blocking it"), "calm"),
             (BLOCKALL_I, ("차단 중엔 아예 안 보내기", "Send no one while blocked"), ("손님도 직원도 보호해요", "protects guests and staff alike")),
             (TESTONE_I, ("잠깐 뒤 한 명만 시험", "After a bit, test with one guest"), ("반열림이에요", "that's half-open"), "warm"),
             (CYCLE_I, ("괜찮으면 다시 열기", "Reopen if it's fine"), ("아니면 또 차단해요", "or block it again if not")),
         ])},
        {"svg": P4, "alt": ("닫힘(정상, 초록 체크)에서 열림(차단, 빨강 X)으로, 다시 반열림(시험, 주황 물음표)을 거쳐 닫힘으로 돌아가는 순환도", "A cycle diagram: closed (green check) to open (red X) to half-open (orange question mark) and back to closed"),
         "caption": ("성공하면 닫힘으로, 실패하면 다시 열림으로 돌아가요.", "Succeed and it returns to closed; fail and it goes back to open."),
         "small": ("세 단계를 오가며 기구 상태를 다시 살펴요.", "It cycles through three states as it keeps checking on the ride.")},
        {"svg": P5, "alt": ("사실은 멀쩡한 기구 앞에 버튼이 눌려 있고, 손님이 '멀쩡한데 왜 막아요?'라고 물음", "The button is pressed in front of a ride that's actually fine, and a guest asks why it's blocked"),
         "caption": ("버튼이 너무 예민하면 괜찮은데도 자꾸 차단해요.", "Too sensitive a button keeps blocking things that are fine."),
         "small": ("기준(임계값)을 잘 잡아야 오탐이 줄어요.", "Setting the right threshold is what keeps false alarms down.")},
    ],
    "summary": (("<b>서킷 브레이커</b> = 고장난 기구에 <b>계속 실패하면</b> 빨간 버튼을 눌러 <b>아예 안 보내는</b> 일. 잠깐 뒤 <b>한 명만 시험</b> 삼아 보내 보고 괜찮으면 다시 열어요.",
                 "<b>Circuit breaker</b> = when a ride <b>keeps failing</b>, pressing the red button so <b>no one is sent</b> there at all. After a bit, <b>one guest tests it</b>, and if it's fine, it reopens."),
                ("닫힘(closed, 정상 통과) · 열림(open, 전부 차단) · 반열림(half-open, 하나만 시험)의 세 상태를 오가는 패턴이에요. 재시도와 달리 '이번엔 아예 보내지 않는다'는 점이 다르고, 임계값을 잘못 잡으면 멀쩡한 서비스도 차단하는 오탐(false positive)이 생겨요.",
                 "A pattern that cycles through three states: closed (normal), open (blocked entirely), and half-open (test with one). Unlike a retry, it means sending nothing at all for a while — and a poorly tuned threshold creates false positives that block services that are actually fine.")),
    "glossary": [
        ("서킷 브레이커", "Circuit breaker", ("고장난 기구 앞 빨간 비상 버튼.", "The red emergency button in front of a broken ride."), ("누르면 그 기구로는 아무도 안 보내요.", "Press it, and no one gets sent there.")),
        ("닫힘 상태", "Closed state", ("평소처럼 손님을 보내는 정상 상태.", "The normal state — guests go through as usual."), ("문제가 없으면 늘 이 상태예요.", "This is the default when nothing's wrong.")),
        ("열림 상태", "Open state", ("아무도 안 보내는 차단 상태.", "The blocked state — no one is sent."), ("계속 실패하면 이 상태로 바뀌어요.", "Repeated failures flip it into this state.")),
        ("반열림 상태", "Half-open state", ("한 명만 몰래 보내보는 시험 상태.", "The testing state — one guest is quietly sent in."), ("괜찮으면 닫힘, 아니면 다시 열림이에요.", "Fine, and it closes again; not fine, and it reopens.")),
        ("임계값", "Threshold", ("몇 번 실패해야 버튼을 누를지 정한 기준.", "The rule for how many failures trigger the button."), ("너무 낮으면 오탐, 너무 높으면 늦게 막아요.", "Too low causes false alarms; too high reacts too late.")),
        ("재시도", "Retry", ("실패하면 잠깐 쉬었다 다시 줄서는 것.", "Waiting a bit and lining up again after a failure."), ('서킷 브레이커는 아예 안 보내고, 재시도는 다시 시도해요 — 서로 다른 대응이에요. → <a href="retrybackoff-ko.html">잠깐 쉬었다 다시 줄서기</a>', "A circuit breaker sends nothing at all; a retry tries again — two different responses. → <a href=\"retrybackoff-en.html\">waiting a bit, then lining up again</a>")),
        ("캐스케이딩 실패", "Cascading failure", ("한 곳의 문제가 옆으로, 또 옆으로 번지는 것.", "One place's trouble spreading to the next, and the next."), ("서킷 브레이커는 이게 더 커지기 전에 끊어요.", "A circuit breaker cuts it off before it grows.")),
        ("벌크헤드", "Bulkhead", ("공원을 구역으로 나눠 피해를 가두는 것.", "Splitting the park into zones to contain the damage."), ('서킷 브레이커와 같이 쓰면 더 든든해요. → <a href="bulkhead-ko.html">불이 안 번지게 나눈 구역</a>', 'Often used together with a circuit breaker for extra safety. → <a href="bulkhead-en.html">zones that keep trouble from spreading</a>')),
    ],
}
