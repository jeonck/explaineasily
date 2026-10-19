from _draw import *
from _world import *

# 1. 집집마다 계량기 숫자를 사람이 직접 적어옴
P1 = svg(300, sky(300)
         + person(220, 170, s=0.8, face=SWEAT + EYES, **CARRIER)
         + postoffice(460, 160, 0.6) + postoffice(560, 160, 0.5) + postoffice(360, 160, 0.5)
         + label(380, 40, "⟦집배원이 집집마다 계량기 숫자를 손으로 적어와야 해요|a carrier has to walk house to house, writing down each meter by hand⟧", 12, "var(--ink)")
         + label(380, 270, "⟦수천 집을 다 돌려면 한 달이 걸려요|visiting thousands of houses takes a whole month⟧", 13, "var(--bad)"))

# 2. 한 달에 한 번이라 중간에 뭔 일이 있었는지 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + postoffice(260, 150, 0.7) + envelope(260, 90, 0.4, text="⟦이번달 분|this month⟧")
         + postoffice(520, 150, 0.7) + label(520, 230, "⟦중간에 새다가 멈췄는지 알 길이 없어요|no way to know if something leaked and stopped midway⟧", 10, "var(--ink)")
         + label(380, 270, "⟦한 달에 한 번 적어선 중간 사정을 전혀 몰라요|checking once a month tells you nothing about what happened in between⟧", 12, "var(--ink)"))

# 3. hero: AMI = 계량기가 스스로 편지를 써서 우체국에 자동으로 보내는 망
P3 = svg(340, sky(340)
         + postoffice(380, 110, 1.0, "⟦우체국|post office⟧")
         + postoffice(180, 230, 0.5) + envelope(180, 190, 0.35, registered=False)
         + postoffice(380, 240, 0.5) + envelope(380, 200, 0.35, registered=False)
         + postoffice(580, 230, 0.5) + envelope(580, 190, 0.35, registered=False)
         + label(380, 30, "⟦AMI = 집집마다 계량기가 스스로 편지를 써서 우체국에 자동으로 보내는 망|AMI = a network where every meter writes its own note and mails it automatically⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦사람이 돌지 않아도, 때마다 저절로 숫자가 도착해요|no one needs to walk around — the numbers arrive by themselves, on schedule⟧", 12, "var(--muted)"))

I1 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 20 v12 l9 5" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
I2 = icon('<rect x="10" y="20" width="44" height="30" rx="4" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/><path d="M10 20 l22 18 l22 -18" fill="none" stroke="var(--good)" stroke-width="4"/>')
I3 = icon('<path d="M20 50 L32 14 L44 50 Z" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M26 34 h12" stroke="var(--accent)" stroke-width="3"/>')
I4 = icon('<rect x="10" y="14" width="44" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M16 42 l8 -14 l8 8 l8 -20 l8 10" stroke="var(--good)" stroke-width="3" fill="none"/>')

# 4. AMI가 자동으로 보고하는 네 가지
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦자동 보고 편지 내용|WHAT THE AUTO-NOTE SAYS⟧",
                    ("⟦주기적 검침 — 정해진 때마다 저절로 숫자를 보내요|periodic reading — sends the number on a set schedule⟧",
                     "⟦양방향 — 반대로 우체국이 계량기에 지시도 보낼 수 있어요|two-way — the post office can send instructions back too⟧",
                     "⟦이상 감지 — 누수·정전 같은 이상도 바로 알려요|anomaly alert — flags a leak or an outage right away⟧",
                     "⟦중계 — 먼 집은 옆집 계량기를 거쳐 전달하기도 해요|relay — a distant meter can hop through a neighbor's⟧"), 1.0))

# 5. 한계: 계량기가 다 통신에 연결돼야 하고, 중간에 누가 엿보면 안 돼요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + postoffice(190, 150, 0.6) + label(190, 240, "⟦사람이 돌지 않아도 돼서 편해요|convenient — no one needs to walk the route⟧", 11, "var(--ink)")
         + postoffice(570, 150, 0.6) + envelope(570, 200, 0.4) + label(570, 250, "⟦편지를 누가 엿보거나 바꿔치기할 위험도 있어요|but the note could be peeked at or swapped⟧", 10, "var(--ink)")
         + label(380, 282, "⟦그래서 이 자동 편지도 암호로 잠가둬요|so this automatic note gets locked with encryption too⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ami", "order": 20,
    "title": ("계량기가 스스로 편지를 보내는 망", "The Network Where Meters Mail Their Own Readings"),
    "h1": ("<em>AMI(지능형 검침 인프라)</em>가 뭐예요?", "What is <em>AMI</em>?"),
    "sub": ("AMI를, 사람이 돌지 않아도 집집마다 계량기가 스스로 편지를 써서 우체국에 보내는 망 이야기로 풀어봤어요.",
            "AMI, told as a story about a network where every meter writes its own note and mails it to the post office, with no one needing to walk the route."),
    "panels": [
        {"svg": P1, "alt": ("집배원이 땀을 흘리며 집집마다 계량기 숫자를 손으로 적음", "A carrier sweats, writing down meter numbers house by house"),
         "caption": ("집배원이 집집마다 계량기 숫자를 손으로 적어와요.", "A carrier has to walk house to house, writing down each meter by hand."),
         "small": ("수천 집을 다 돌려면 한 달이 걸려요.", "Visiting thousands of houses takes a whole month.")},
        {"svg": P2, "alt": ("우체국 두 곳 중 한 곳이 새다가 멈췄는지 알 길이 없음", "One of two post offices might have leaked and stopped, with no way to know"),
         "caption": ("한 달에 한 번이라 중간 사정을 몰라요.", "Once a month means you don't know what happened in between."),
         "small": ("중간에 새다가 멈췄는지 알 길이 없어요.", "No way to know if something leaked and stopped midway.")},
        {"svg": P3, "hero": True, "alt": ("집집마다 계량기가 스스로 봉투를 써서 우체국으로 자동으로 보냄", "Every house's meter writes its own envelope and mails it automatically to the post office"),
         "caption": ("AMI = 계량기가 스스로 편지를 써서 자동으로 보내는 망이에요.", "AMI = a network where meters write and mail their own notes automatically."),
         "small": ("사람이 돌지 않아도, 때마다 저절로 숫자가 도착해요.", "No one needs to walk around — the numbers arrive by themselves, on schedule."),
         "tricks": (4, [
             (I1, ("자동 검침", "Automatic Reading"), ("정해진 때마다 스스로", "sends itself on schedule")),
             (I2, ("양방향 통신", "Two-Way"), ("우체국도 지시를 보내요", "the post office replies too"), "calm"),
             (I3, ("이상 감지", "Anomaly Alert"), ("누수·정전을 바로 알려요", "flags a leak or outage fast"), "warm"),
             (I4, ("데이터 분석", "Data Analysis"), ("사용 패턴을 모아 봐요", "gathers usage patterns")),
         ])},
        {"svg": P4, "alt": ("자동 보고 편지 내용 안내판: 주기적 검침, 양방향, 이상 감지, 중계 네 줄", "A guide board for the auto-note's contents: periodic reading, two-way, anomaly alert, relay"),
         "caption": ("자동 편지엔 네 가지가 담겨요.", "The auto-note carries four kinds of information."),
         "small": ("먼 집은 옆집 계량기를 거쳐 전달하기도 해요.", "A distant meter can hop through a neighbor's to get there.")},
        {"svg": P5, "alt": ("왼쪽: 사람이 돌지 않아도 돼서 편함. 오른쪽: 편지를 엿보거나 바꿔치기할 위험이 있어 암호로 잠금", "Left: convenient, no one needs to walk the route. Right: the note could be peeked at, so it's locked with encryption"),
         "caption": ("편하지만 지켜야 할 것도 있어요.", "It's convenient, but there's something to guard too."),
         "small": ("자동 편지도 암호로 잠가둬요.", "This automatic note gets locked with encryption too.")},
    ],
    "summary": (("<b>AMI</b> = 사람이 돌지 않아도, 집집마다 계량기가 <b>스스로 편지를 써서 자동으로</b> 우체국에 보내는 검침망.",
                 "<b>AMI</b> = a metering network where every house's meter <b>writes and mails its own note automatically</b>, with no one walking the route."),
                ("AMI(Advanced Metering Infrastructure, 지능형 검침 인프라)는 전기·수도·가스 계량기가 통신망을 통해 사용량을 자동으로 주기적으로 전송하고, 공급자도 계량기에 원격으로 지시를 내릴 수 있는 양방향 통신 체계예요. 과거 사람이 직접 방문해 읽던 방식과 달리, 실시간에 가깝게 이상 상황도 감지할 수 있어요.",
                 "AMI (Advanced Metering Infrastructure) is a two-way communication system where electricity, water, and gas meters automatically send usage data over a network on a regular schedule, and the utility can send instructions back to the meter. Unlike the old manual-visit reading method, it can detect anomalies in near real time.")),
    "glossary": [
        ("스마트 미터", "Smart Meter", ("스스로 편지를 쓰는 계량기.", "The meter that writes its own note."), ("AMI의 핵심 장치예요.", "The core device of an AMI system.")),
        ("양방향 통신", "Two-Way Communication", ("우체국도 계량기에 지시를 보낼 수 있는 것.", "The post office being able to send instructions back to the meter."), ("원격 검침을 넘어선 제어까지 가능해요.", "Goes beyond remote reading, to remote control.")),
        ("주기적 검침", "Periodic Reading", ("정해진 때마다 저절로 숫자를 보내는 것.", "Sending the number on a set schedule, automatically."), ("한 달에 한 번이 아니라 훨씬 자주예요.", "Far more often than the old once-a-month visit.")),
        ("이상 감지", "Anomaly Detection", ("누수·정전 같은 이상을 바로 알아채는 것.", "Catching a leak or an outage right away."), ("AMI의 실시간성이 만드는 장점이에요.", "A benefit that comes from AMI's near-real-time nature.")),
        ("Modbus", "Modbus", ("우체국장이 순서대로 묻는 단순한 쪽지 규칙.", "The simple note rule where the clerk asks one at a time."), ('현장 설비끼리는 이런 단순한 규칙으로도 통신해요. → <a href="modbus-ko.html">우체국장이 순서대로 묻는 쪽지 규칙</a>', 'Field devices often talk this simply too. → <a href="modbus-en.html">the note rule where the clerk asks one at a time</a>')),
        ("Ad-hoc 라우팅", "Ad-hoc Routing", ("고정 우체국 없이 서로 길을 찾는 법.", "Finding the way among themselves, with no fixed post office."), ('먼 계량기가 이웃을 거쳐 전달할 때 쓰는 방식이에요. → <a href="adhocrouting-ko.html">집배원끼리 길을 찾아 전달하는 법</a>', "Used when a distant meter relays through a neighbor. → <a href=\"adhocrouting-en.html\">how carriers find the way among themselves</a>")),
        ("5G·mMTC", "5G mMTC", ("소형 소포 대량 전용 차선.", "The lane built for millions of tiny parcels."), ('대량의 계량기를 한꺼번에 연결할 때 쓰여요. → <a href="5gcore-ko.html">상황별 전용 차선을 가진 배송망</a>', 'Used to connect huge numbers of meters at once. → <a href="5gcore-en.html">the network with a lane for every need</a>')),
        ("개인정보·보안", "Privacy & Security", ("편지 내용을 엿보지 못하게 잠그는 것.", "Locking the note so no one can peek inside."), ("다른 세계(보안)에서 자세히 다루는 주제예요.", "A topic covered in depth in another world (Security).")),
    ],
}
