from _draw import *
from _world import *

# 1. 공원은 하루도 안 닫아요 — 밤에도 손님이 와요
P1 = svg(320, night(320)
         + ride(140, 260, 0.9, color="var(--accent)") + ride(280, 260, 0.75, color="#5B8DEF") + ride(420, 260, 0.85, color="#2E7D6B")
         + queueline(70, 204, 4, 0.5, 30)
         + controlroom(560, 60, 170, 100, bars=((0.5, "var(--good)"), (0.4, "var(--good)"), (0.6, "var(--accent)"), (0.3, "var(--good)")))
         + person(610, 190, s=0.65, face=EYES, **OPERATOR) + label(645, 240, "⟦밤에도 지켜봐요|watching even at night⟧", 11, "#C9D5E6")
         + label(380, 290, "⟦이 공원은 1년 365일, 하루도 안 닫아요|this park never closes — not one day a year⟧", 13, "#F5E6B8", cls="d"))

# 2. 그런데 기구는 언젠가 고장 나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(130, 230, 0.9, color="var(--stone)", closed=True, label_text="⟦고장|broken⟧")
         + queueline(220, 174, 6, 0.5, 28) + label(300, 236, "⟦줄이 점점 길어져요|the line keeps growing⟧", 11, "var(--bad)")
         + person(60, 170, s=0.7, face=FROWN + SWEAT, **MECHANIC) + bubble(10, 90, 170, 36, "⟦완벽한 기구는 없어요|no ride is perfect⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(560, 230, 0.9, color="#5B8DEF") + person(630, 170, s=0.6, face=SMILE, hat=None, shirt="#7B3FA0") + bubble(600, 90, 150, 36, "⟦저긴 멀쩡한데요?|that one\'s fine though?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦완벽하게 안 고장나는 게 목표가 아니에요 — 고장 나도 손님이 못 느끼는 게 목표예요|the goal isn\'t never breaking — it\'s breaking without guests noticing⟧", 12, "var(--ink)"))

# 3. SRE = 고장 나도 손님이 못 느끼게 돌보는 사람들 (hero)
P3 = svg(360, sky(360)
         + ride(130, 300, 0.85, color="var(--accent)") + ride(260, 300, 0.7, color="#5B8DEF", closed=True) + ride(390, 300, 0.8, color="#2E7D6B")
         + queueline(90, 250, 3, 0.45, 26) + queueline(230, 250, 3, 0.45, 26) + queueline(360, 250, 3, 0.45, 26)
         + controlroom(480, 60, 220, 120, bars=((0.6, "var(--good)"), (0.9, "var(--bad)"), (0.5, "var(--good)"), (0.4, "var(--good)")))
         + person(540, 210, s=0.75, face=EYES, **OPERATOR) + walkie(610, 190, 0.9)
         + person(300, 230, s=0.7, face=SMILE, extra=WRENCH, **MECHANIC)
         + '<path d="M540 250 L300 260" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 40, "⟦SRE = 고장 나도 손님이 못 느끼게 돌보는 사람들|SRE = the people who keep trouble invisible to guests⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦계기판을 보고, 자동으로 돌리고, 호출받으면 가고, 끝나면 기록해요|watch the gauges, automate what repeats, answer the page, write it down after⟧", 12, "var(--muted)"))

# 4. 공원 지도 — 다 보고, 출동하고, 예비로 넘어가요
P4 = svg(320, sky(320)
         + board(40, 30, 300, 220, "⟦공원 지도|PARK MAP⟧", ("⟦기구 12개 운영 중|12 rides running⟧", "⟦관제실이 전부 지켜봐요|control room watches all⟧", "⟦기구 하나 고장 → 정비사 출동|one breaks → mechanic responds⟧", "⟦그래도 안 되면 → 여분으로|still stuck → switch to spare⟧"), 1.0)
         + shed(560, 260, 0.9, label_text="⟦여분 발전기|spare generator⟧") + '<path d="M470 150 L560 230" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + person(480, 100, s=0.7, face=EYES, **OPERATOR) + ride(620, 110, 0.6, color="var(--bad)", closed=True)
         + label(380, 290, "⟦혼자 다 못 봐요 — 계기판, 출동, 예비가 한 세트예요|no one watches it alone — gauges, response, and a spare all work together⟧", 12, "var(--ink)"))

# 5. 완벽한 가동은 없어요 — 대신 미리 약속해 둬요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + gauge(190, 110, 1.1, level=0.97, label_text="⟦100%는 없어요|never 100%⟧") + label(190, 240, "⟦완벽을 좇으면 돈이 끝없이 들어요|chasing perfect costs without end⟧", 11, "var(--ink)")
         + board(480, 50, 220, 140, "⟦우리끼리 약속|OUR PROMISE⟧", ("⟦목표: 99.9%|target: 99.9%⟧", "⟦그 안에서는 자유롭게|free to move within it⟧", "⟦넘으면 다 같이 멈춰요|cross it, everyone pauses⟧"), 1.0)
         + label(590, 240, "⟦몇 %를 지킬지 미리 정해요|decide in advance how much to promise⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그리고 자동화가 사람을 대신하지만, 마지막 판단은 늘 사람이 해요|and automation takes over the repeats — but a person still makes the final call⟧", 12, "var(--ink)", cls="d"))

WATCH_I = icon('<circle cx="24" cy="24" r="4" fill="var(--accent)"/><rect x="10" y="34" width="44" height="22" rx="4" fill="#1B2A44"/><rect x="16" y="38" width="10" height="12" fill="var(--good)"/><rect x="28" y="38" width="10" height="16" fill="var(--bad)"/><rect x="40" y="38" width="10" height="8" fill="var(--good)"/>')
AUTO_I = icon('<path d="M44 32 a12 12 0 1 1 -4 -9" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 12 l6 10 -12 2z" fill="var(--good)"/><circle cx="20" cy="40" r="4" fill="var(--good)"/>')
PAGE_I = icon('<rect x="20" y="10" width="20" height="36" rx="4" fill="var(--stone-dark)"/><rect x="24" y="18" width="12" height="8" fill="#5B9BD5"/><circle cx="30" cy="8" r="3" fill="var(--bad)"/>')
NOTE_I = icon('<rect x="14" y="12" width="36" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 h20 M22 32 h20 M22 40 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "reliability", "order": 1,
    "title": ("쉬지 않는 공원을 돌보는 사람들", "The People Who Keep an Amusement Park Open"),
    "h1": ("<em>SRE</em>가 뭐예요?", "What is <em>SRE</em>?"),
    "sub": ("SRE(사이트 신뢰성 공학)를 하루도 닫지 않는 놀이공원을 돌보는 사람들 이야기로 풀어봤어요.",
            "Site Reliability Engineering, told as a story about the people who keep an amusement park open every single day."),
    "panels": [
        {"svg": P1, "alt": ("밤에도 손님이 기구를 타는 놀이공원, 관제실 요원이 화면을 보며 지켜봄", "Guests still ride at night; a control-room operator watches the screens"),
         "caption": ("이 공원은 1년 365일, 하루도 안 닫아요.", "This park never closes — not one day a year."),
         "small": ("손님은 낮에도 밤에도 와요. 관제실은 늘 켜져 있어요.", "Guests come day and night. The control room never goes dark.")},
        {"svg": P2, "alt": ("기구 하나가 고장나 줄이 길어짐. 정비사가 '완벽한 기구는 없어요' 하고, 옆 기구는 멀쩡함", "One ride breaks and the line grows; a mechanic says no ride is perfect, while the ride beside it is fine"),
         "caption": ("그런데 기구는 언젠가 고장 나요.", "But every ride breaks, eventually."),
         "small": ("완벽하게 안 고장나는 게 목표가 아니에요. 고장 나도 손님이 못 느끼는 게 목표예요.", "The goal isn\'t never breaking. It\'s breaking in a way guests never notice.")},
        {"svg": P3, "hero": True, "alt": ("관제실 화면에 빨간 막대 하나, 요원이 무전기를 들고, 정비사가 공구를 들고 달려감", "The control-room screen shows one red bar; the operator holds a walkie-talkie while a mechanic rushes over with tools"),
         "caption": ("SRE는 고장 나도 손님이 못 느끼게 돌보는 사람들이에요.", "SRE is the people who keep trouble invisible to guests."),
         "small": ("계기판을 보고, 자동으로 돌리고, 호출받으면 가고, 끝나면 기록해요.", "Watch the gauges, automate what repeats, answer the page, write it down after."),
         "tricks": (4, [
             (WATCH_I, ("미리 계기판 보기", "Watch the gauges"), ("터지기 전에 알아채요", "catch it before it breaks"), "calm"),
             (AUTO_I, ("자동으로 돌리기", "Automate the repeats"), ("사람이 다 못 봐요", "no one can watch it all")),
             (PAGE_I, ("호출받으면 가기", "Answer the page"), ("밤이어도요", "even at night"), "warm"),
             (NOTE_I, ("끝나면 기록하기", "Write it down after"), ("탓하지 않고요", "without blame")),
         ])},
        {"svg": P4, "alt": ("공원 지도: 기구 12개, 관제실이 전부 지켜보고, 고장나면 정비사 출동, 그래도 안되면 여분 발전기로", "A park map: 12 rides, the control room watching all, a mechanic responding to breaks, and a spare generator as last resort"),
         "caption": ("혼자 다 못 봐요 — 계기판, 출동, 예비가 한 세트예요.", "No one watches it alone — gauges, response, and a spare all work together."),
         "small": ("기구 하나가 고장 나면 정비사가 가요. 그래도 안 되면 여분 발전기로 넘어가요.", "When a ride breaks, a mechanic responds. If that\'s not enough, the spare generator takes over.")},
        {"svg": P5, "alt": ("왼쪽: 100%를 가리키는 계기판에 '완벽을 좇으면 돈이 끝없이 들어요'. 오른쪽: 우리끼리 약속 안내판 — 목표 99.9%", "Left: a gauge near 100% with chasing perfect costs without end. Right: our promise board — target 99.9%"),
         "caption": ("완벽한 가동은 없어요. 대신 미리 약속해 둬요.", "There\'s no such thing as perfect uptime. Instead, promise in advance."),
         "small": ("몇 %를 지킬지 정하고, 그 안에서는 자유롭게 움직여요. 그리고 마지막 판단은 늘 사람이 해요.", "Decide how much you\'ll promise, and move freely within it. The final call always belongs to a person.")},
    ],
    "summary": (("<b>SRE</b> = 공원을 <b>하루도 안 닫되</b>, 완벽을 좇는 대신 <b>얼마나 열려 있을지 미리 약속</b>하고, <b>계기판·자동화·호출·기록</b>으로 그 약속을 지키는 일.",
                 "<b>SRE</b> = keeping the park <b>open every day</b> — not by chasing perfection, but by <b>promising an uptime in advance</b> and keeping that promise with <b>gauges, automation, paging, and postmortems</b>."),
                ("Site Reliability Engineering. 구글이 만든 분야로, 소프트웨어 엔지니어링 방법을 운영에 적용해 시스템의 신뢰성을 지켜요. 핵심은 '100% 가동'이 아니라 SLO로 정한 목표만큼 지키고, 반복 작업은 자동화하며, 장애에서 배우는 문화예요.",
                 "A discipline Google created to apply software-engineering methods to operations. The core idea isn\'t 100% uptime — it\'s meeting a target set by an SLO, automating repetitive work, and learning from every incident.")),
    "glossary": [
        ("신뢰성 공학", "Site Reliability Engineering", ("공원을 돌보는 일 전체.", "The whole job of keeping the park running."), ("관측, 자동화, 온콜, 사고 대응, 그리고 배우기까지 다 포함해요.", "Observability, automation, on-call, incident response, and learning — all of it.")),
        ("가동 시간", "Uptime", ("공원이 열려 있던 시간.", "How long the park stayed open."), ("100%는 현실에 없어요 — 그래서 목표를 정해요.", "100% doesn\'t exist in reality — so you set a target instead.")),
        ("목표", "SLO", ("우리끼리 정한 약속 줄.", "The promise line we set ourselves."), ('넘으면 다 같이 멈춰요. → <a href="slo-ko.html">우리끼리 정한 목표 줄</a>', 'Cross it, and everyone pauses. → <a href="slo-en.html">the target line we set ourselves</a>')),
        ("자동화", "Automation", ("사람 대신 도는 기계.", "The machine that runs instead of a person."), ('줄이 길어지면 스스로 직원을 더 불러요. → <a href="autoscaling-ko.html">줄이 길어지면 직원을 더 부르기</a>', 'When the line grows, it calls in more staff on its own. → <a href="autoscaling-en.html">calling in more staff</a>')),
        ("온콜", "On-call", ("이번 주 호출기를 든 사람.", "Whoever\'s holding the pager this week."), ('밤에도 호출받으면 가요. → <a href="oncall-ko.html">이번 주 호출기를 든 사람</a>', 'Answers the page, even at night. → <a href="oncall-en.html">whoever\'s holding the pager</a>')),
        ("사고 대응", "Incident response", ("정비사가 달려가는 일.", "The mechanic rushing over."), ("고장이 커지기 전에 멈춰 세워요.", "Stops a small break from becoming a big one.")),
        ("사후 분석", "Postmortem", ("탓하지 않고 쓰는 기록.", "The record written without blame."), ('다음엔 똑같이 안 당하려고요. → <a href="postmortem-ko.html">탓하지 않고 모여 쓰는 기록</a>', 'So the same thing doesn\'t happen twice. → <a href="postmortem-en.html">the record everyone writes without blame</a>')),
        ("계기판", "Golden signals", ("관제실 벽의 계기판 네 개.", "The four gauges on the control-room wall."), ('레이턴시·트래픽·에러·포화. → <a href="goldensignals-ko.html">관제실의 계기판 네 개</a>', 'Latency, traffic, errors, saturation. → <a href="goldensignals-en.html">the four gauges on the control-room wall</a>')),
    ],
}
