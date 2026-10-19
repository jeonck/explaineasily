"""망중립성(Network Neutrality)."""
from _draw import *
from _world import *

SAME_I = icon('<rect x="10" y="26" width="44" height="12" rx="6" fill="var(--accent)"/><circle cx="18" cy="32" r="7" fill="#FFF8E7"/><circle cx="32" cy="32" r="7" fill="#FFF8E7"/><circle cx="46" cy="32" r="7" fill="#FFF8E7"/>')
NOBLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M22 32 h20 M38 24 l8 8 l-8 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
NOSLOW_I = icon('<path d="M10 46 L26 30 L36 40 L54 18" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 14 L50 50 M50 14 L14 50" stroke="var(--bad)" stroke-width="3" stroke-linecap="round" opacity="0.5"/>')
OPEN_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 28 h20 M22 36 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

# 1. 새치기하려는 학생
P1 = svg(300, sky(300, ground=False)
         + '<rect y="200" width="760" height="100" fill="var(--stone)"/>'
         + person(560, 130, s=0.8, face=EYES, **STUDENT) + '<rect x="552" y="190" width="24" height="10" fill="#E9B44C"/>'
         + bubble(440, 60, 240, 44, "⟦저 돈 더 냈어요, 먼저 갈게요!|I paid extra, I'm cutting in!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(330, 150, s=0.75, face=FROWN, **STUDENT) + person(230, 150, s=0.75, face=FROWN, **STUDENT) + person(130, 150, s=0.75, face=FROWN, **STUDENT)
         + label(380, 280, "⟦급식 줄(복도)에서 새치기하려고 해요|someone's trying to cut the lunch line (the hallway)⟧", 13, "var(--ink)", cls="d"))

# 2. 처음엔 편한데 결국 불공평해져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(560, 150, s=0.8, face=SMILE, **STUDENT) + label(560, 250, "⟦돈 낸 학생만 빨라요|only the paying student goes fast⟧", 11, "var(--ink)")
         + person(230, 150, s=0.7, face=FROWN + SWEAT, **STUDENT) + person(140, 150, s=0.7, face=FROWN, **STUDENT)
         + label(185, 250, "⟦나머지는 계속 뒤로 밀려요|everyone else keeps getting pushed back⟧", 11, "var(--bad)")
         + label(380, 285, "⟦한 번 새치기를 봐주면, 돈 없는 학생은 늘 손해예요|allow one cut, and students without money always lose out⟧", 12, "var(--ink)", cls="d"))

# 3. 망중립성 = 복도 관리자가 누구든 똑같은 속도로 보내는 원칙 (hero)
P3 = svg(340, sky(340)
         + label(380, 28, "⟦망중립성 = 통신사가 누구 데이터든 차별 없이 같은 속도로 보내는 원칙|net neutrality = the rule that a carrier moves everyone's data at the same speed, no favorites⟧", 13, "var(--ink)", cls="d")
         + person(380, 120, s=0.9, face=EYES, **TEACHER)
         + person(180, 190, s=0.7, face=SMILE, **STUDENT) + person(300, 190, s=0.7, face=SMILE, **STUDENT)
         + person(460, 190, s=0.7, face=SMILE, **STUDENT) + person(580, 190, s=0.7, face=SMILE, **STUDENT)
         + label(380, 320, "⟦급식도 와이파이도, 줄 선 순서대로 공평하게|lunch or wifi, served fairly in line order⟧", 12, "var(--muted)"))

# 4. 망중립 있음 / 없음
P4 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + label(190, 40, "⟦망중립 있음|with net neutrality⟧", 13, "var(--ink)", cls="d")
         + person(100, 150, s=0.6, face=SMILE, **STUDENT) + person(190, 150, s=0.6, face=SMILE, **STUDENT) + person(280, 150, s=0.6, face=SMILE, **STUDENT)
         + label(190, 240, "⟦모두 같은 속도로 줄을 서요|everyone waits in line at the same speed⟧", 11, "var(--good)")
         + label(570, 40, "⟦망중립 없음|without net neutrality⟧", 13, "var(--ink)", cls="d")
         + person(480, 150, s=0.6, face=FROWN, **STUDENT) + person(570, 130, s=0.7, face=SMILE, **STUDENT) + person(660, 150, s=0.6, face=FROWN, **STUDENT)
         + label(570, 240, "⟦유료 학생만 빠른 길로 가요|only the paying student gets the fast lane⟧", 11, "var(--bad)")
         + label(380, 300, "⟦공평함이 사라지면, 새 서비스를 만들 기회도 돈 있는 쪽에만 몰려요|lose fairness, and the chance to build new services tilts toward whoever can pay⟧", 11, "var(--muted)"))

# 5. 너무 엄격하면 특수 서비스가 곤란해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=SWEAT + EYES, **TEACHER)
         + label(190, 250, "⟦응급 방송도 똑같은 줄에 세워야 하나요?|does the emergency broadcast wait in the same line too?⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **PRESIDENT)
         + label(570, 250, "⟦불합리한 차별만 막는 거예요|it only bans unreasonable discrimination⟧", 11, "var(--ink)")
         + label(380, 285, "⟦공정함과 효율성 사이에서 계속 줄다리기해요|a constant tug-of-war between fairness and efficiency⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "netneutral", "order": 3,
    "title": ("급식 줄은 다 똑같이 서야 해요", "Everyone Waits in the Same Lunch Line"),
    "h1": ("<em>망중립성</em>이 뭐예요?", "What is <em>Network Neutrality</em>?"),
    "sub": ("망중립성을, 급식 줄(복도)에서 누구도 새치기 못 하게 하는 학생회 원칙 이야기로 풀어봤어요.",
            "Net neutrality, told as a story about the student council's rule that nobody cuts the lunch line (the hallway)."),
    "panels": [
        {"svg": P1, "alt": ("돈을 더 낸 학생이 급식 줄에서 새치기하려 함", "A student who paid extra tries to cut the lunch line"),
         "caption": ("급식 줄(복도)에서 새치기하려고 해요.", "Someone's trying to cut the lunch line (the hallway)."),
         "small": ("돈을 더 내면 먼저 갈 수 있다고 해요.", "They say paying more means going first.")},
        {"svg": P2, "alt": ("돈 낸 학생만 빨라지고 나머지는 계속 뒤로 밀림", "Only the paying student speeds up; everyone else keeps getting pushed back"),
         "caption": ("처음엔 편한데, 결국 불공평해져요.", "It feels convenient at first, but ends up unfair."),
         "small": ("한 번 새치기를 봐주면, 돈 없는 학생은 늘 손해예요.", "Allow one cut, and students without money always lose out.")},
        {"svg": P3, "hero": True, "alt": ("선생님이 모든 학생을 같은 순서로 줄 세움", "A teacher lines up every student in the same, fair order"),
         "caption": ("망중립성은 누구 데이터든 차별 없이 같은 속도로 보내는 원칙이에요.", "Net neutrality is the rule that everyone's data moves at the same speed, no favorites."),
         "small": ("급식도 와이파이도, 줄 선 순서대로 공평하게.", "Lunch or wifi, served fairly in line order."),
         "tricks": (4, [
             (SAME_I, ("다 같은 속도로", "Same speed for all"), ("서비스별 차별 없이", "no favoring one service"), "calm"),
             (NOBLOCK_I, ("막지 않기", "No blocking"), ("특정 사이트를 못 막아요", "can't block a specific site")),
             (NOSLOW_I, ("일부러 느리게 안 하기", "No deliberate slowdown"), ("특정 업체만 봐주지 않아요", "no favors for one company"), "warm"),
             (OPEN_I, ("관리 방법 공개", "Disclose how it's managed"), ("숨기지 않고 투명하게", "openly, not hidden")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 망중립이 있어 모두 같은 속도. 오른쪽: 망중립이 없어 유료 학생만 빠른 길로 감", "Left: with net neutrality, everyone moves at the same speed. Right: without it, only the paying student gets the fast lane"),
         "caption": ("망중립이 있을 때와 없을 때는 이렇게 달라요.", "Here's the difference with and without net neutrality."),
         "small": ("공평함이 사라지면, 새 서비스를 만들 기회도 돈 있는 쪽에만 몰려요.", "Lose fairness, and the chance to build new services tilts toward whoever can pay.")},
        {"svg": P5, "alt": ("선생님은 응급 방송도 똑같이 줄 세워야 하냐고 묻고, 학생회장은 불합리한 차별만 막는 거라고 답함", "A teacher asks if even an emergency broadcast must wait in line; the president answers it only bans unreasonable discrimination"),
         "caption": ("너무 엄격하면 특수 서비스가 곤란해요.", "Too strict a rule makes trouble for special services."),
         "small": ("공정함과 효율성 사이에서 계속 줄다리기해요.", "A constant tug-of-war between fairness and efficiency.")},
    ],
    "summary": (("<b>망중립성</b> = 복도(통신망)를 지나는 누구의 데이터든 <b>차별·차단·새치기 없이</b> 똑같이 다뤄야 한다는 원칙.",
                 "<b>Net neutrality</b> = the rule that everyone's data crossing the hallway (the network) is treated the same, with <b>no discrimination, blocking, or cutting in line</b>."),
                ("망중립성은 인터넷 제공사업자(ISP)가 트래픽의 내용·출처·서비스 종류에 따라 속도를 차별하거나 차단해서는 안 된다는 원칙이에요. 다만 모든 트래픽 관리가 금지되는 건 아니고, '불합리한 차별'만 규제 대상이에요 — 응급·의료 트래픽 같은 합리적 우선순위는 별도로 인정돼요.",
                 "Net neutrality is the principle that internet service providers must not discriminate against or block traffic based on its content, source, or type of service. Not all traffic management is banned, though — only 'unreasonable discrimination' is regulated, while reasonable prioritization for things like emergency or medical traffic can still be allowed.")),
    "glossary": [
        ("망중립성", "Network Neutrality", ("줄에서 새치기를 막는 규칙.", "The rule that stops cutting in line."), ("통신사가 트래픽을 차별하지 못하게 해요.", "Stops a carrier from favoring one kind of traffic.")),
        ("트래픽 차별", "Traffic Discrimination", ("특정 서비스만 빠르게/느리게 하는 것.", "Speeding up or slowing down one service on purpose."), ("망중립성이 막으려는 핵심 행위예요.", "The core behavior net neutrality is meant to stop.")),
        ("제로레이팅", "Zero-Rating", ("특정 앱만 데이터 요금을 안 받는 것.", "Not charging data fees for one specific app."), ("편리해 보이지만 망중립 논쟁의 단골 소재예요.", "Looks convenient, but it's a frequent flashpoint in the debate.")),
        ("트래픽 관리", "Traffic Management", ("혼잡할 때 흐름을 조절하는 것.", "Adjusting flow when things get congested."), ("합리적인 관리는 허용돼요 — 차별이 아니라면요.", "Reasonable management is allowed — as long as it isn't discrimination.")),
        ("망중립성 vs 망이용대가", "Net Neutrality vs Network-Use Fees", ("줄 세우는 규칙과, 줄 서는 값을 내는 문제는 달라요.", "The line-order rule and who pays for the line are different issues."), ("요금 논쟁은 망중립성과는 또 다른 문제예요.", "The fee debate is a separate question from net neutrality.")),
        ("투명성 의무", "Transparency Obligation", ("관리 방법을 숨기지 않고 공개하는 것.", "Publishing how traffic is managed instead of hiding it."), ("불합리한 차별인지 확인할 수 있게 해줘요.", "Lets anyone check whether a discrimination is unreasonable.")),
        ("합리적 트래픽 관리", "Reasonable Traffic Management", ("혼잡 제어처럼 다 같이 봐줄 수 있는 관리.", "Management everyone can accept, like congestion control."), ("불합리한 차별과는 구분돼요.", "Distinguished from unreasonable discrimination.")),
        ("플랫폼 규제", "Platform Regulation", ("앱 하나가 너무 커질 때의 다른 규칙.", "A different rule for when one app grows too dominant."), ('망중립성과 비슷한 공정성 긴장이 있어요. → <a href="superapp-ko.html">학생증 하나로 다 되는 앱</a>', 'Shares a similar fairness tension. → <a href="superapp-en.html">the one app that does everything</a>')),
    ],
}
