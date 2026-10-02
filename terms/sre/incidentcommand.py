from _draw import *
from _world import *

BATON = '<g transform="translate(54,50) rotate(-15)"><rect x="-3" y="-36" width="6" height="40" rx="2" fill="#E9B44C"/><path d="M-3 -36 l22 8 l-22 10z" fill="var(--accent)"/></g>'

# 1. 큰 사고인데 다들 각자 고치려 들고, 손님 안내도 아무도 안 해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + ride(380, 260, 1.0, color="var(--bad)", closed=True)
         + person(220, 260 - 112 * 0.6, s=0.6, face=SWEAT, extra=WRENCH, **MECHANIC)
         + person(540, 260 - 112 * 0.6, s=0.6, face=SWEAT, extra=WRENCH, **ROOKIE)
         + bubble(90, 110, 170, 40, "⟦내가 고칠게요!|I'll fix it!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble(500, 110, 180, 40, "⟦아니 제가 할게요!|no, let me!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + queueline(40, 260 - 112 * 0.45, 3, 0.45, 26)
         + label(110, 180, "⟦안내가 없어요|nobody's telling us anything⟧", 10, "var(--bad)")
         + label(380, 282, "⟦큰 사고가 났는데 다들 각자 고치려 들고, 손님 안내도 아무도 안 해요|a big incident hits — everyone tries to fix it alone, and nobody tells the guests anything⟧", 12, "var(--ink)"))

# 2. 왜: 사고 중엔 다들 급해서 서로 다른 일을 동시에 하면 꼬여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(120, 260 - 112 * 0.55, s=0.55, face=EYES, **MECHANIC)
         + person(320, 260 - 112 * 0.55, s=0.55, face=EYES, **ROOKIE)
         + person(520, 260 - 112 * 0.55, s=0.55, face=EYES, **MANAGER)
         + person(680, 260 - 112 * 0.45, s=0.45, face=EYES, shirt="#4A5A72")
         + '<path d="M160 195 L660 210 M660 195 L160 210 M340 195 L540 210" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 6"/>'
         + label(380, 250, "⟦다들 급해서 서로 다른 지시를 동시에 해요|everyone's in a hurry, giving different orders at once⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦사고 중엔 서로 다른 일을 동시에 하면 꼬여요|doing different things at once during an incident tangles everything up⟧", 12, "var(--ink)"))

# 3. hero: 사고가 커지면 한 사람이 지휘봉을 들어요
P3 = svg(360, sky(360)
         + board(30, 235, 180, 100, "⟦손님 안내|STATUS PAGE⟧", ("⟦현재 점검 중|investigating now⟧",), 1.0)
         + controlroom(560, 60, 160, 100, bars=((0.5, "var(--good)"), (0.7, "var(--accent)")))
         + person(260, 300 - 112 * 0.55, s=0.55, face=EYES, extra=WRENCH, **MECHANIC)
         + person(430, 300 - 112 * 0.85, s=0.85, face=EYES, extra=BATON, **OPERATOR)
         + '<path d="M405 280 L240 260" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M460 230 L560 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M415 290 L210 290" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 40, "⟦사고가 커지면 한 사람이 지휘봉을 들어요|when an incident grows, one person picks up the baton⟧", 14, "var(--ink)", cls="d")
         + label(380, 340, "⟦그 사람이 누가 뭘 할지 정하고, 손님 안내도 맡아요|that person decides who does what — and handles the guest updates too⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 지휘는 조율만, 조치·관측·소통은 나눠 맡아요
P4 = svg(360, sky(360)
         + label(380, 30, "⟦사고 지휘 한 사람 아래, 역할을 나눠요|under one incident commander, roles split up⟧", 13, "var(--ink)", cls="d")
         + label(380, 95, "⟦지휘|COMMAND⟧", 11, "var(--muted)")
         + person(380, 110, s=0.65, face=EYES, extra=BATON, **OPERATOR)
         + label(150, 115, "⟦조치|FIX⟧", 11, "var(--muted)")
         + person(150, 130, s=0.5, face=EYES, extra=WRENCH, **MECHANIC)
         + controlroom(560, 70, 160, 90, bars=((0.5, "var(--good)"), (0.3, "var(--good)")))
         + label(640, 175, "⟦관측|WATCH⟧", 11, "var(--muted)")
         + '<path d="M400 190 L200 170" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M410 190 L600 150" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M395 193 L380 235" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + board(270, 235, 220, 70, "⟦소통|COMMS⟧", ("⟦손님 안내 중|updating guests⟧",), 1.0)
         + label(380, 340, "⟦지휘는 조율만 하고, 조치·관측·소통은 나눠 맡아요|command only coordinates — fixing, watching, and talking to guests are split among others⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 작은 사고엔 지휘자까지 부르면 느려요 — 등급에 맞게
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(100, 260 - 112 * 0.5, s=0.5, face=SWEAT, extra=BATON, **OPERATOR)
         + ride(220, 260, 0.6, color="var(--accent)")
         + label(160, 190, "⟦작은 사고에도 지휘자부터 불러요|calling a commander even for a small hiccup⟧", 10, "var(--bad)")
         + label(190, 282, "⟦오히려 느려요|that's actually slower⟧", 12, "var(--bad)", cls="d")
         + board(430, 60, 280, 150, "⟦사고 등급표|SEVERITY TABLE⟧", ("⟦SEV1: 지휘자 호출|SEV1: call a commander⟧", "⟦SEV2: 당번이 직접 처리|SEV2: on-call handles it⟧", "⟦SEV3: 기록만 해둬요|SEV3: just log it⟧"), 1.0)
         + label(570, 282, "⟦사고 크기에 맞게 미리 정해둬요|decide in advance, matched to the incident's size⟧", 12, "var(--ink)"))

ONE_I = icon('<circle cx="32" cy="18" r="10" fill="var(--accent)"/><rect x="20" y="30" width="24" height="26" rx="6" fill="var(--accent)"/><path d="M44 16 L58 8" stroke="#E9B44C" stroke-width="5" stroke-linecap="round"/>')
NOHANDS_I = icon('<rect x="26" y="10" width="8" height="34" rx="3" fill="#5A3B22" transform="rotate(-30 30 27)"/><circle cx="18" cy="14" r="8" fill="none" stroke="#5A3B22" stroke-width="4"/><path d="M12 12 L52 52 M52 12 L12 52" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
COMMS_I = icon('<rect x="8" y="14" width="30" height="26" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 22 h18 M14 28 h12" stroke="#142033" stroke-width="2.5"/><path d="M44 20 Q54 27 44 34" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 14 Q64 27 50 40" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
SEV_I = icon('<rect x="10" y="40" width="12" height="14" fill="var(--good)"/><rect x="26" y="28" width="12" height="26" fill="var(--accent)"/><rect x="42" y="12" width="12" height="42" fill="var(--bad)"/>')

PAGE = {
    "slug": "incidentcommand", "order": 40,
    "title": ("지휘봉을 든 사람", "The One Holding the Baton"),
    "h1": ("<em>인시던트 커맨더</em>가 뭐예요?", "What is an <em>Incident Commander</em>?"),
    "sub": ("인시던트 커맨더를, 큰 사고가 나면 지휘봉을 들어 역할을 나눠주는 사람 이야기로 풀어봤어요.",
            "Incident commander, told as a story about the one person who picks up the baton when a big incident hits."),
    "panels": [
        {"svg": P1, "alt": ("기구 하나가 고장났는데 정비사 두 명이 서로 자기가 고치겠다고 다투고, 줄 선 손님들은 아무 안내도 못 받음", "A ride breaks and two mechanics argue over who fixes it, while waiting guests get no word at all"),
         "caption": ("큰 사고가 났는데 다들 각자 고치려 들어요.", "A big incident hits, and everyone tries to fix it alone."),
         "small": ("손님에게 뭐라 안내할지도 아무도 안 정해서 더 혼란스러워요.", "Nobody decided what to tell the guests either, so it gets even more chaotic.")},
        {"svg": P2, "alt": ("네 사람이 서로 다른 방향으로 화살표를 그리며 동시에 지시함", "Four people draw crossing arrows, each giving orders in a different direction at once"),
         "caption": ("다들 급해서 서로 다른 일을 동시에 해요.", "Everyone's in a hurry, doing different things at once."),
         "small": ("사고 중엔 그러면 더 꼬여요.", "During an incident, that just tangles things up more.")},
        {"svg": P3, "hero": True, "alt": ("지휘봉을 든 사람이 가운데 서서 정비사와 관제실, 손님 안내판에 점선 화살표로 역할을 나눠줌", "A person holding a baton stands in the center, dashed arrows assigning roles to a mechanic, the control room, and a status page"),
         "caption": ("사고가 커지면 한 사람이 지휘봉을 들어요.", "When an incident grows, one person picks up the baton."),
         "small": ("누가 뭘 할지 정하고, 손님 안내도 그 사람이 맡아요.", "That person decides who does what, and handles the guest updates too."),
         "tricks": (4, [
             (ONE_I, ("큰 사고엔 지휘자 한 명", "One commander for a big incident"), ("여러 명이 동시에 안 끼어들어요", "no crowd of voices at once"), "calm"),
             (NOHANDS_I, ("직접 안 고치고 조율만", "Doesn't fix it directly"), ("손은 빼고 지시만 해요", "hands off, orders only")),
             (COMMS_I, ("손님 안내도 지휘자가", "Guest updates too"), ("상태 게시판을 맡아요", "owns the status page"), "warm"),
             (SEV_I, ("사고 등급에 따라 미리 정해요", "Set by severity, in advance"), ("누가 지휘할지 정해둬요", "who commands is decided ahead of time")),
         ])},
        {"svg": P4, "alt": ("지휘자 한 명 아래, 조치를 맡은 정비사, 관측을 맡은 관제실, 소통을 맡은 안내판으로 화살표가 뻗어 역할이 나뉨", "Under one commander, arrows branch out to a mechanic handling the fix, a control room watching, and a board handling communication"),
         "caption": ("지휘는 조율만 하고, 조치·관측·소통은 나눠 맡아요.", "Command only coordinates — fixing, watching, and talking to guests are split among others."),
         "small": ("한 사람이 다 하는 게 아니라, 역할을 나눠요.", "It's not one person doing everything — the roles are split.")},
        {"svg": P5, "alt": ("왼쪽: 작은 기구 하나의 사소한 문제에도 지휘자를 부르느라 느림. 오른쪽: 사고 등급표로 SEV1~3에 따라 누가 처리할지 미리 정해둠", "Left: calling a commander even for a tiny hiccup, which is slow. Right: a severity table decides in advance who handles SEV1 through SEV3"),
         "caption": ("작은 사고에 지휘자까지 부르면 오히려 느려요.", "Calling a commander for a small incident just slows things down."),
         "small": ("사고 크기에 맞게 등급을 나눠 미리 정해둬요.", "Grade incidents by size and decide who leads ahead of time.")},
    ],
    "summary": (("<b>인시던트 커맨더</b> = 큰 사고가 나면 <b>한 사람이 지휘봉을 들어</b>, 역할을 나누고 <b>손님 안내</b>까지 책임지는 일.",
                 "<b>Incident commander</b> = when a big incident hits, <b>one person picks up the baton</b>, splits up the roles, and owns the <b>guest communication</b> too."),
                ("Incident Commander. 사고 대응을 지휘하는 역할로, 직접 고치지 않고 누가 무엇을 할지 조율하며 상태 게시판 같은 대외 소통도 책임져요. 사고 심각도(SEV1~)에 따라 언제 지휘자를 부를지 미리 정해두는 게 중요해요.",
                 "The role that leads incident response — not fixing things directly, but coordinating who does what and owning external communication like the status page. It matters to decide in advance, by severity level (SEV1 and up), when a commander gets called in.")),
    "glossary": [
        ("인시던트 커맨더", "Incident commander", ("지휘봉을 든 사람.", "The one holding the baton."), ("직접 안 고치고 조율만 해요.", "Doesn't fix things directly — only coordinates.")),
        ("심각도 등급", "Severity levels (SEV1~)", ("사고 크기를 나눈 등급.", "Grades that classify how big an incident is."), ("SEV1이 가장 커요.", "SEV1 is the biggest.")),
        ("역할 분리", "Role separation", ("지휘·조치·소통을 나누는 것.", "Splitting command, fixing, and communication."), ("한 사람이 다 떠맡지 않아요.", "No one person carries it all.")),
        ("상태 게시판", "Status page", ("손님에게 보여주는 안내판.", "The board that tells guests what's going on."), ("지휘자가 이 안내를 맡아요.", "The commander owns this update.")),
        ("사고 선언 기준", "Incident declaration criteria", ("언제부터 '사고'로 부를지 정한 선.", "The line that decides when something counts as an incident."), ("미리 정해둬야 헷갈리지 않아요.", "Deciding it in advance avoids confusion.")),
        ("사고 종료 선언", "Incident resolution", ("다 괜찮아졌다고 공식으로 알리는 것.", "The official word that everything's okay again."), ("지휘자가 선언하고 나서 끝나요.", "The commander declares it, and that's when it ends.")),
        ("온콜", "On-call", ("이번 주 호출기를 든 사람.", "Whoever's holding the pager this week."), ('지휘자가 되기도 해요. → <a href="oncall-ko.html">이번 주 호출기를 든 사람</a>', 'Sometimes becomes the commander. → <a href="oncall-en.html">whoever\'s holding the pager</a>')),
        ("사후 분석", "Postmortem", ("사고 끝나고 탓하지 않고 쓰는 기록.", "The blameless record written after it's over."), ('지휘자가 이 기록도 챙겨요. → <a href="postmortem-ko.html">탓하지 않고 모여 쓰는 기록</a>', 'The commander makes sure this gets written too. → <a href="postmortem-en.html">the record everyone writes without blame</a>')),
    ],
}
