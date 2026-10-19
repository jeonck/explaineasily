from _draw import *
from _world import *

# 1. 이 건물이 곧 클라우드예요 — 입주사는 사무실, 컴퓨터, 소프트웨어가 다 한 번에 필요해요
P1 = svg(320, sky(320)
         + building(60, 60, 1.1)
         + person(260, 208, s=0.8, face=SWEAT, **TENANT)
         + bubble(300, 60, 300, 70, "⟦사무실도, 컴퓨터도, 쓸 프로그램도... 다 한꺼번에 필요한데!|office, computers, software... I need it ALL at once!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 30, "⟦이 건물이 곧 클라우드예요|this building is the cloud⟧", 14, "var(--accent)", cls="d")
         + label(380, 300, "⟦새로 시작하는 회사는 한 번에 너무 많은 게 필요해요|a brand-new company needs too many things at once⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 건물·전기·가구·소프트웨어를 전부 직접 마련하면 몇 달이 걸려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + building(80, 40, 0.9)
         + label(170, 20, "⟦내 건물을 직접 지으면|building your own from scratch⟧", 12, "var(--bad)", cls="d")
         + person(380, 188, s=0.7, face=FROWN, **TENANT)
         + label(380, 230, "⟦터 사기 → 짓기 → 전기 깔기 → 가구 사기...|buy land → build → wire power → buy furniture...⟧", 11, "var(--ink)")
         + label(380, 258, "⟦몇 달, 몇 억이 먼저 들어요|months and a fortune, before you even open⟧", 11, "var(--muted)")
         + label(380, 282, "⟦필요한 '전부'를 직접 마련하면 시작도 하기 전에 지쳐요|preparing everything yourself means you're exhausted before you even start⟧", 12, "var(--ink)"))

# 3. hero: 클라우드 = 공유 오피스 빌딩. 건물주/인테리어업체/완제품사무실 중 골라 쓰면 돼요
P3 = svg(360, sky(360)
         + building(50, 50, 1.3)
         + office(260, 220, 0.95, label_text="⟦IaaS: 뼈대만|IaaS: bare shell⟧")
         + office(380, 220, 0.95, label_text="⟦PaaS: 인테리어까지|PaaS: interior done⟧")
         + office(500, 220, 0.95, label_text="⟦SaaS: 완제품|SaaS: move-in ready⟧")
         + person(650, 256, s=0.75, face=SMILE, **TENANT)
         + label(380, 30, "⟦클라우드 = 이 공유 오피스 빌딩 그 자체예요|the cloud = this very shared office building⟧", 15, "var(--ink)", cls="d")
         + label(380, 345, "⟦필요한 만큼만 골라서 빌려 쓰면 돼요|rent exactly as much as you need⟧", 12, "var(--muted)"),
         )

# 4. 작동 디테일: 층마다 "누가 관리하나"가 달라요 (하드웨어~데이터)
P4 = svg(340, sky(340)
         + floorplan(60, 30, 640, 290, "⟦누가 관리하나요? — IaaS / PaaS / SaaS|who manages what — IaaS / PaaS / SaaS⟧",
                     ("⟦앱·데이터: 항상 내가 관리|app and data: always mine⟧",
                      "⟦미들웨어·런타임: PaaS부턴 건물 담당|middleware and runtime: handled from PaaS on⟧",
                      "⟦OS: SaaS에서만 건물 담당|OS: handled by the building only in SaaS⟧",
                      "⟦하드웨어·건물: 셋 다 건물 담당|hardware and building: always the building's job⟧"), 1.0))

# 5. 깨지는 곳: 한 건물에만 다 맡기면 나중에 옮기기 힘들어요(락인), 모든 회사가 공유 건물이 맞는 것도 아니에요
P5 = svg(375, '<rect width="380" height="375" fill="var(--accent-soft)"/><rect x="380" width="380" height="375" fill="var(--good-soft)"/>'
         + building(100, 60, 0.85) + person(60, 236, s=0.6, face=FROWN, **TENANT)
         + label(190, 355, "⟦이 건물 방식에만 너무 맞추면, 다른 건물로 옮기기 어려워요(락인)|fit too tightly to one building's way, and moving to another gets hard (lock-in)⟧", 11, "var(--ink)")
         + building(480, 60, 0.85, floors=5) + person(680, 282, s=0.6, face=SMILE, **LANDLORD)
         + label(570, 355, "⟦보안·규정 때문에 자기 건물을 직접 짓는 곳도 있어요(온프레미스)|some still build their own, for security or rules — that's on-premises⟧", 11, "var(--ink)"))

IAAS_I = icon('<rect x="8" y="8" width="48" height="48" rx="4" fill="none" stroke="var(--stone-dark)" stroke-width="4"/>')
PAAS_I = icon('<rect x="8" y="8" width="48" height="48" rx="4" fill="var(--good-soft)" stroke="var(--good)" stroke-width="4"/><path d="M20 44 h24" stroke="var(--good)" stroke-width="4"/>')
SAAS_I = icon('<rect x="8" y="8" width="48" height="48" rx="4" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="4"/><path d="M18 24 h28 M18 34 h28 M18 44 h18" stroke="var(--accent)" stroke-width="3"/>')
PAYG_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><text x="32" y="40" font-size="22" font-weight="800" text-anchor="middle" fill="var(--accent)">₩</text>')

PAGE = {
    "slug": "cloudmodel", "order": 1,
    "title": ("뼈대만, 인테리어까지, 완제품 — 셋 중 골라 빌리기", "Bare Shell, Interior Done, or Move-In Ready — Pick One to Rent"),
    "h1": ("<em>클라우드 서비스 모델</em>이 뭐예요?", "What is a <em>Cloud Service Model</em>?"),
    "sub": ("클라우드 서비스 모델(IaaS·PaaS·SaaS)을, 한 공유 오피스 빌딩에서 어디까지 빌리느냐의 차이로 풀어봤어요.",
            "Cloud service models (IaaS, PaaS, SaaS), told as how much of a shared office building you choose to rent."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 입주사 직원이 사무실, 컴퓨터, 프로그램을 한꺼번에 다 구해야 한다고 말함", "A sweating tenant worker says they need office, computers, and software all at once"),
         "caption": ("새 회사는 한 번에 너무 많은 게 필요해요.", "A brand-new company needs too many things at once."),
         "small": ("사무실, 전기, 컴퓨터, 소프트웨어 — 전부 다요.", "Office, power, computers, software — all of it.")},
        {"svg": P2, "alt": ("건물을 직접 지으려는 사람이 터 사기부터 가구 사기까지 과정을 나열하며 지쳐함", "Someone trying to build their own building lists everything from buying land to buying furniture, exhausted"),
         "caption": ("전부 직접 마련하면 시작도 하기 전에 지쳐요.", "Preparing everything yourself means you're exhausted before you even start."),
         "small": ("몇 달, 몇 억이 문 열기도 전에 들어가요.", "Months and a fortune go in before you even open the door.")},
        {"svg": P3, "hero": True, "alt": ("공유 오피스 빌딩 안에 뼈대만 있는 사무실, 인테리어까지 된 사무실, 완제품 사무실 세 종류가 나란히 있고 입주사가 웃고 있음", "Inside the shared office building: a bare-shell office, an interior-done office, and a move-in-ready office side by side, with a smiling tenant"),
         "caption": ("클라우드 = 이 공유 오피스 빌딩 그 자체예요.", "The cloud = this very shared office building."),
         "small": ("필요한 만큼만 골라서 빌려 쓰면 돼요.", "Rent exactly as much as you need."),
         "tricks": (4, [
             (IAAS_I, ("IaaS = 뼈대만 빌려요", "IaaS = rent the bare shell"), ("전기·배관까지만요", "just power and plumbing"), "calm"),
             (PAAS_I, ("PaaS = 인테리어까지 돼 있어요", "PaaS = interior already done"), ("바로 책상만 놓으면 돼요", "just add your own desk"), "calm"),
             (SAAS_I, ("SaaS = 완제품 사무실이에요", "SaaS = a move-in-ready office"), ("열쇠만 받으면 끝이에요", "just take the keys"), "warm"),
             (PAYG_I, ("쓴 만큼만 내요", "Pay only for what you use"), ("월세 대신 종량제예요", "metered, not a flat rent")),
         ])},
        {"svg": P4, "alt": ("입주 안내판: 앱·데이터는 항상 내가 관리, 미들웨어는 PaaS부턴 건물 담당, OS는 SaaS만 건물 담당, 하드웨어는 항상 건물 담당", "A tenant board: app and data always mine, middleware handled from PaaS on, OS only in SaaS, hardware always the building's"),
         "caption": ("층마다 '누가 관리하나'가 달라요.", "Who manages what changes floor by floor."),
         "small": ("내가 관리하는 범위가 줄어들수록, 건물이 더 많이 대신해줘요.", "The less you manage yourself, the more the building does for you.")},
        {"svg": P5, "alt": ("왼쪽: 한 건물 방식에 너무 맞추면 다른 건물로 옮기기 어려움(락인). 오른쪽: 보안 때문에 직접 건물을 짓는 온프레미스", "Left: fitting too tightly to one building makes moving hard (lock-in). Right: some build their own building for security — on-premises"),
         "caption": ("한 건물에만 다 맡기면 나중에 옮기기 힘들어요.", "Fit too tightly to one building, and moving later gets hard."),
         "small": ("보안·규정 때문에 직접 짓는 곳도 여전히 있어요.", "Some still build their own, for security or regulation.")},
    ],
    "summary": (("<b>클라우드 서비스 모델</b> = 이 공유 오피스 빌딩에서 <b>어디까지 빌리느냐</b>의 세 단계. <b>뼈대만(IaaS)</b>, <b>인테리어까지(PaaS)</b>, <b>완제품(SaaS)</b>.",
                 "<b>Cloud service models</b> are three levels of <b>how much of the building you rent</b>: <b>bare shell (IaaS)</b>, <b>interior done (PaaS)</b>, or <b>move-in ready (SaaS)</b>."),
                ("IaaS(서버·네트워크 등 인프라만 제공), PaaS(OS·런타임까지 제공해 앱 개발에만 집중), SaaS(완성된 소프트웨어를 그대로 사용)로 나뉘어요. 아래로 갈수록 관리 부담은 줄고 자유도는 낮아져요. 이 공유 오피스 빌딩 세계관에서 나머지 페이지들은 전부 이 건물 안 이야기예요.",
                 "Split into IaaS (just infrastructure like servers and networking), PaaS (adds OS and runtime so you focus only on the app), and SaaS (ready-made software you simply use). Going down the list, management burden drops and freedom drops with it. Every other page in this shared-office-building world is a story set inside this same building.")),
    "glossary": [
        ("클라우드컴퓨팅", "Cloud computing", ("이 공유 오피스 빌딩 자체.", "The shared office building itself."), ("필요한 만큼만 빌려 쓰는 방식이에요.", "You rent exactly as much as you need.")),
        ("IaaS", "IaaS (Infrastructure as a Service)", ("뼈대만 빌리는 사무실.", "The bare-shell office."), ("서버·네트워크 같은 인프라만 제공해요.", "Provides only infrastructure like servers and networking.")),
        ("PaaS", "PaaS (Platform as a Service)", ("인테리어까지 된 사무실.", "The office with interior already done."), ("OS·런타임까지 챙겨줘서 개발에만 집중해요.", "Covers OS and runtime too, so you focus only on building the app.")),
        ("SaaS", "SaaS (Software as a Service)", ("완제품 사무실, 열쇠만 받으면 끝.", "A move-in-ready office — just take the keys."), ("완성된 소프트웨어를 그대로 써요.", "You use finished software as-is.")),
        ("온프레미스", "On-premises", ("직접 짓는 자기 건물.", "A building you construct yourself."), ("보안·규정 때문에 직접 짓는 경우도 있어요.", "Some still build their own for security or regulation.")),
        ("종량제 과금", "Pay-as-you-go", ("월세 대신 쓴 만큼만 내는 방식.", "Paying for what you use, instead of flat rent."), ("안 쓰면 안 내도 돼요.", "Don't use it, don't pay for it.")),
        ("가상머신·컨테이너", "VM and Container", ("독채 사무실과 칸막이 책상.", "The private office and the partitioned desk."), ('IaaS 위에서 공간을 나누는 두 가지 방법이에요. → <a href="vmcontainer-ko.html">독채 사무실과 칸막이 책상</a>', 'Two ways to divide space on top of IaaS. → <a href="vmcontainer-en.html">the private office and the partitioned desk</a>')),
        ("서버리스", "Serverless", ("시간제로만 빌리는 회의실.", "A meeting room rented only by the hour."), ('뼈대조차 신경 안 써도 되는 극단적인 형태예요. → <a href="serverless-ko.html">시간제 회의실</a>', "An extreme form where you don't even think about the shell. → <a href=\"serverless-en.html\">the hourly meeting room</a>")),
    ],
}
