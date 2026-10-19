from _draw import *
from _world import *

# 1. 손님이 늘었어요 — 사무실이 좁아요
P1 = svg(300, sky(300)
         + office(260, 160, 1.0)
         + person(280, 240, s=0.55, face=SWEAT, **TENANT) + person(320, 240, s=0.55, face=SWEAT, **TENANT) + person(360, 240, s=0.55, face=SWEAT, **TENANT)
         + bubble(440, 100, 260, 60, "⟦일이 늘었는데 사무실이 너무 좁아요|business grew, but the office is way too small⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦일이 늘면 사무실 하나로는 부족해져요|as business grows, one office stops being enough⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 키울지, 더 빌릴지 — 방법이 두 가지라 헷갈려요
P2 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + office(100, 190, 1.1) + label(190, 280, "⟦사무실을 더 크게?|make the office bigger?⟧", 12, "var(--ink)")
         + office(480, 190, 0.85) + office(560, 190, 0.85) + label(590, 280, "⟦사무실을 하나 더?|rent another office?⟧", 12, "var(--ink)")
         + label(380, 40, "⟦키울지 더 빌릴지, 방법이 두 가지라 헷갈려요|make it bigger, or rent more — two ways, easy to mix up⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 스케일업=사무실 키우기(수직), 스케일아웃=사무실 더 빌리기(수평)
P3 = svg(360, sky(360)
         + office(120, 230, 1.5, label_text="⟦스케일업: 더 크게|scale-up: make it bigger⟧")
         + office(420, 260, 0.85) + office(500, 260, 0.85) + office(580, 260, 0.85)
         + label(500, 345, "⟦스케일아웃: 더 많이|scale-out: rent more of them⟧", 12, "var(--ink)", cls="d")
         + label(380, 30, "⟦스케일업 = 한 칸을 키우기, 스케일아웃 = 칸 수를 늘리기|scale-up = make one bigger, scale-out = add more of them⟧", 13, "var(--ink)", cls="d"))

# 4. 작동 디테일: 자동으로 하면 오토스케일 — 이미 다른 페이지에서 다뤄요
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦스케일업 vs 스케일아웃 vs 오토스케일|scale-up vs scale-out vs auto scale⟧",
                     ("⟦스케일업: 한 사무실을 더 크고 세게(수직 확장)|scale-up: make one office bigger and stronger (vertical)⟧",
                      "⟦스케일아웃: 같은 사무실을 더 많이(수평 확장)|scale-out: add more identical offices (horizontal)⟧",
                      "⟦둘 다 사람이 정할 수도, 자동으로 맡길 수도 있어요|either can be decided by hand, or handed off to automation⟧",
                      "⟦자동으로 늘렸다 줄이는 건 오토스케일이라고 불러요|doing it automatically, in both directions, is called auto scale⟧"), 1.0))

# 5. 깨지는 곳 + 마무리: 이 건물 투어는 여기까지예요
P5 = svg(375, sky(375)
         + building(280, 40, 1.1)
         + person(180, 280, s=0.6, face=SMILE, **TENANT) + person(560, 280, s=0.6, face=SMILE, **VISITOR)
         + label(380, 30, "⟦이 건물 투어는 여기까지예요|that's the end of this building tour⟧", 14, "var(--accent)", cls="d")
         + label(380, 345, "⟦뼈대부터 자동 배정, 저장 방식까지 — 전부 한 건물 안 이야기였어요|from the bare shell to auto-assignment to storage — all one building's story⟧", 12, "var(--ink)"))

UP_I = icon('<path d="M20 50 v-20 h24 v20 z" fill="var(--accent)"/><path d="M14 54 h36" stroke="var(--accent)" stroke-width="3"/>')
OUT_I = icon('<rect x="6" y="36" width="14" height="18" fill="var(--good)"/><rect x="25" y="36" width="14" height="18" fill="var(--good)"/><rect x="44" y="36" width="14" height="18" fill="var(--good)"/>')
AUTO_I = icon('<path d="M44 24 a12 12 0 1 1 -4 -9" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 4 l6 10 -12 2z" fill="var(--good)"/>')
LIMIT_I = icon('<path d="M14 12 h12 M14 12 v14 M50 12 h-12 M50 12 v14" stroke="var(--bad)" stroke-width="4" fill="none"/><path d="M14 52 h12 M14 52 v-14 M50 52 h-12 M50 52 v-14" stroke="var(--bad)" stroke-width="4" fill="none"/>')

PAGE = {
    "slug": "scaleupout", "order": 12,
    "title": ("사무실을 키울까, 더 빌릴까", "Make the Office Bigger, or Rent More of Them"),
    "h1": ("<em>스케일업/스케일아웃과 오토스케일</em>이 뭐예요?", "What are <em>Scale-Up/Scale-Out and Auto Scale</em>?"),
    "sub": ("스케일업·스케일아웃·오토스케일을, 사무실을 키울지 더 빌릴지, 그걸 자동으로 맡길지의 이야기로 풀어봤어요. 이 건물 투어의 마지막 페이지예요.",
            "Scale-up, scale-out, and auto scale, told as whether to make the office bigger, rent more, or hand that decision off to automation — the final page of this building tour."),
    "panels": [
        {"svg": P1, "alt": ("좁아진 사무실 안에서 입주사 셋이 땀을 흘리며 사무실이 너무 좁다고 말함", "Three tenants sweat inside a cramped office, saying it's way too small now"),
         "caption": ("일이 늘면 사무실 하나로는 부족해져요.", "As business grows, one office stops being enough."),
         "small": ("더 넓은 공간이 필요해져요.", "More space becomes necessary.")},
        {"svg": P2, "alt": ("왼쪽엔 사무실을 더 크게 만들지 고민하는 모습, 오른쪽엔 사무실을 하나 더 빌릴지 고민하는 모습", "Left: wondering about making the office bigger. Right: wondering about renting another office"),
         "caption": ("키울지, 더 빌릴지 — 방법이 두 가지라 헷갈려요.", "Make it bigger, or rent more — two ways, easy to mix up."),
         "small": ("둘 다 '더 넓어진다'는 결과는 같아요.", "Both end up with more space — just differently."),},
        {"svg": P3, "hero": True, "alt": ("왼쪽에 훨씬 커진 사무실 하나(스케일업), 오른쪽에 같은 크기 사무실 세 개가 나란히(스케일아웃)", "Left: one much bigger office (scale-up). Right: three identically sized offices side by side (scale-out)"),
         "caption": ("스케일업 = 한 칸을 키우기, 스케일아웃 = 칸 수를 늘리기예요.", "Scale-up = make one bigger, scale-out = add more of them."),
         "small": ("하나를 세게 키우거나, 여러 개로 나누거나예요.", "Either make one much stronger, or spread across many."),
         "tricks": (4, [
             (UP_I, ("스케일업 = 한 칸을 더 크게", "Scale-up = make one bigger"), ("수직 확장이라고 불러요", "called vertical scaling"), "calm"),
             (OUT_I, ("스케일아웃 = 칸 수를 더 많이", "Scale-out = add more of them"), ("수평 확장이라고 불러요", "called horizontal scaling")),
             (AUTO_I, ("둘 다 자동으로 맡길 수 있어요", "Either can be handed off to automation"), ("오토스케일이라고 불러요", "called auto scale"), "warm"),
             (LIMIT_I, ("자동으로 할 땐 최대·최소를 정해둬요", "Automated scaling still needs a max and min"), ("너무 늘거나 줄지 않게요", "so it never goes too far either way")),
         ])},
        {"svg": P4, "alt": ("스케일업·스케일아웃·오토스케일을 정리한 안내판: 수직/수평 확장, 수동/자동 결정 여부", "A board summarizing scale-up, scale-out, and auto scale: vertical vs horizontal, manual vs automated decision"),
         "caption": ("오토스케일은 둘 중 하나를 자동으로 결정하는 거예요.", "Auto scale is just automating the decision between the two."),
         "small": ("자동으로 늘렸다 줄이는 자세한 이야기는 다른 세계에서 이미 다뤄요.", "The detailed story of auto scaling up and down is already covered in another world."),},
        {"svg": P5, "alt": ("건물 앞에서 입주사와 방문객이 웃으며 서 있고, 이 건물 투어가 여기서 끝난다는 문구가 적힘", "A tenant and a visitor stand smiling in front of the building, with text saying this building tour ends here"),
         "caption": ("이 건물 투어는 여기까지예요.", "That's the end of this building tour."),
         "small": ("뼈대(IaaS)부터 자동 배정(쿠버네티스), 저장 방식까지 — 전부 한 건물 안 이야기였어요.", "From the bare shell (IaaS) to auto-assignment (Kubernetes) to storage — all one building's story."),},
    ],
    "summary": (("<b>스케일업</b> = 사무실 하나를 <b>더 크게</b>(수직). <b>스케일아웃</b> = 사무실을 <b>더 많이</b>(수평). <b>오토스케일</b> = 그 결정을 <b>자동으로</b> 맡기는 것.",
                 "<b>Scale-up</b> means making one office <b>bigger</b> (vertical). <b>Scale-out</b> means renting <b>more</b> offices (horizontal). <b>Auto scale</b> means <b>handing that decision off to automation</b>."),
                ("스케일업(수직 확장)은 서버 한 대의 성능(CPU·메모리)을 키우는 것, 스케일아웃(수평 확장)은 같은 서버를 여러 대로 늘리는 것이에요. 오토스케일은 지표(트래픽·큐 길이 등)를 보고 이 둘을 최대·최소 한도 안에서 자동으로 수행해요. 자동 확장의 콜드 스타트·스레싱 같은 세부 동작은 SRE 세계의 오토스케일링 페이지에서 더 깊이 다뤄요.",
                 "Scale-up (vertical scaling) increases one server's own capacity — CPU, memory. Scale-out (horizontal scaling) adds more servers of the same kind. Auto scale watches a metric (traffic, queue length, etc.) and performs either automatically, within a set max and min. Details like cold starts and thrashing during auto scaling are covered in more depth on the autoscaling page in the SRE world.")),
    "glossary": [
        ("스케일업(수직 확장)", "Scale-up (vertical)", ("사무실 하나를 더 크게 만드는 것.", "Making one office bigger."), ("서버 한 대의 성능 자체를 키워요.", "Increases one server's own capacity.")),
        ("스케일아웃(수평 확장)", "Scale-out (horizontal)", ("같은 사무실을 더 많이 빌리는 것.", "Renting more identical offices."), ("서버 수 자체를 늘려요.", "Adds more servers of the same kind.")),
        ("오토스케일", "Auto scale", ("늘릴지 줄일지를 자동으로 정하는 것.", "Automatically deciding whether to scale up or down."), ('자세한 동작은 SRE 세계에서 다뤄요. → <a href="autoscaling-ko.html">줄이 길어지면 직원을 더 부르기</a>', 'Detailed behavior is covered in the SRE world. → <a href="autoscaling-en.html">call in more staff when the line grows</a>')),
        ("오케스트레이션/쿠버네티스", "Orchestration / Kubernetes", ("몇 자리를 유지할지 정하는 규칙과 그 제품.", "The rule for how many spots to keep, and the product behind it."), ('실제로 자리를 늘리고 줄이는 걸 실행에 옮기는 역할이에요. → <a href="k8s-ko.html">자동 배정 배지의 그 유명한 제품</a>', 'The role that actually carries out adding or removing spots. → <a href="k8s-en.html">the famous brand behind the auto-assign badge</a>')),
        ("가상머신/컨테이너", "VM / Container", ("독채는 스케일업, 칸막이는 스케일아웃에 더 잘 맞아요.", "Private offices fit scale-up; partitioned desks fit scale-out."), ('이 건물 투어의 두 번째 페이지였어요. → <a href="vmcontainer-ko.html">독채 사무실과 칸막이 책상</a>', 'The second page of this building tour. → <a href="vmcontainer-en.html">the private office and the partitioned desk</a>')),
        ("서버리스", "Serverless", ("스케일 결정 자체를 신경 쓸 필요 없는 선택.", "The option where you never think about scaling decisions at all."), ('이미 극단적으로 자동화된 형태예요. → <a href="serverless-ko.html">시간제 회의실</a>', 'Already an extreme form of automation. → <a href="serverless-en.html">the hourly meeting room</a>')),
        ("클라우드 서비스 모델", "Cloud service model", ("뼈대만/인테리어까지/완제품 — 이 건물 투어의 첫 페이지.", "Bare shell / interior done / move-in ready — the first page of this tour."), ('→ <a href="cloudmodel-ko.html">셋 중 골라 빌리기</a>', '→ <a href="cloudmodel-en.html">pick one to rent</a>')),
        ("AI 데이터센터", "AI data center", ("GPU만을 위한 전용 별관.", "An annex built just for the GPUs."), ("전용 설비는 대개 스케일업(더 센 장비) 쪽으로 커져요.", "Specialized gear tends to grow via scale-up — beefier equipment.")),
    ],
}
