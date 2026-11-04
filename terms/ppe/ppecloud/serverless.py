from _draw import *
from _world import *

# 1. 한 시간짜리 회의 때문에 사무실을 통째로 빌려야 해요?
P1 = svg(320, sky(320)
         + office(260, 150, 1.0, label_text="⟦1년 내내 비어있는 내 사무실|my office, empty almost all year⟧")
         + person(480, 175, s=0.8, face=FROWN, **TENANT)
         + bubble(490, 60, 260, 60, "⟦한 시간 회의 때문에 사무실을 통째로 빌려야 해요?|a whole office, just for a one-hour meeting?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦가끔 쓰는 일 때문에 사무실 전체를 유지하긴 아까워요|keeping a whole office for something you use rarely feels wasteful⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 안 쓸 때도 월세는 계속 나가요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + office(300, 90, 1.0) + label(330, 210, "⟦비어 있음|empty⟧", 12, "var(--bad)")
         + person(500, 140, s=0.6, face=FROWN, **TENANT)
         + label(500, 245, "⟦그래도 월세는 매달 나가요|but rent still goes out every month⟧", 12, "var(--ink)")
         + label(380, 300, "⟦안 쓰는 시간에도 고정비가 계속 나가요|even unused hours still rack up fixed cost⟧", 12, "var(--ink)"))

# 3. hero: 서버리스 = 시간제 회의실. 쓸 때만 문을 열고, 쓴 시간만큼만 내요
P3 = svg(380, sky(380)
         + meetingroom(260, 180, 1.4, hourly=True)
         + label(335, 248, "⟦시간제 회의실|hourly meeting room⟧", 12, "var(--good)")
         + person(480, 272, s=0.7, face=SMILE, **TENANT)
         + '<path d="M300 150 L300 120" stroke="var(--good)" stroke-width="3" stroke-dasharray="4 3"/>'
         + label(300, 110, "⟦쓸 때만 문 열림|opens only when used⟧", 11, "var(--good)")
         + label(380, 30, "⟦서버리스 = 쓸 때만 여는 시간제 회의실이에요|serverless = an hourly meeting room that opens only when used⟧", 14, "var(--ink)", cls="d")
         + label(380, 365, "⟦사무실(서버) 관리는 건물이 다 해줘요|the building handles all the \"office\" management for you⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 상시 사무실 vs 시간제 회의실 비교
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦상시 사무실 vs 시간제 회의실|always-on office vs hourly meeting room⟧",
                     ("⟦비용: 고정 월세 vs 쓴 시간만큼만|cost: flat rent vs pay only for hours used⟧",
                      "⟦관리: 내가 직접 vs 건물이 알아서|upkeep: you manage it vs the building handles it⟧",
                      "⟦상시 대기: 항상 켜짐 vs 평소엔 닫혀 있음|standby: always on vs closed by default⟧",
                      "⟦문 여는 속도: 즉시 vs 처음엔 살짝 느림|opening speed: instant vs a bit slow the first time⟧"), 1.0))

# 5. 깨지는 곳: 처음 문 열 때 살짝 느리고(콜드 스타트), 긴 회의엔 안 맞아요
P5 = svg(365, '<rect width="380" height="365" fill="var(--accent-soft)"/><rect x="380" width="380" height="365" fill="var(--good-soft)"/>'
         + meetingroom(100, 180, 1.0, hourly=False) + person(60, 258, s=0.55, face=SWEAT, **TENANT)
         + label(190, 345, "⟦닫혀 있던 문을 여는 데 잠깐 시간이 걸려요(콜드 스타트)|opening a closed-down room takes a moment (cold start)⟧", 11, "var(--ink)")
         + office(480, 180, 0.9) + person(650, 268, s=0.55, face=SMILE, **TENANT)
         + label(570, 345, "⟦하루 종일 쓰는 일은 상시 사무실이 더 맞아요|all-day work still fits an always-on office better⟧", 11, "var(--ink)"))

PAYG_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><text x="32" y="40" font-size="22" font-weight="800" text-anchor="middle" fill="var(--accent)">₩</text>')
NOMGMT_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="var(--good-soft)" stroke="var(--good)" stroke-width="4"/><path d="M22 32 l8 8 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
EVENT_I = icon('<path d="M32 10 L44 30 L32 54 L20 30 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/>')
COLD_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M32 20 v12 l8 6" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "serverless", "order": 4,
    "title": ("쓸 때만 여는 시간제 회의실", "The Meeting Room That Opens Only When Used"),
    "h1": ("<em>서버리스 컴퓨팅</em>이 뭐예요?", "What is <em>Serverless Computing</em>?"),
    "sub": ("서버리스 컴퓨팅을, 사무실 전체 대신 쓸 때만 문을 여는 시간제 회의실 이야기로 풀어봤어요.",
            "Serverless computing, told as a story about an hourly meeting room that opens only when you actually need it."),
    "panels": [
        {"svg": P1, "alt": ("입주사가 한 시간짜리 회의 때문에 사무실 전체를 빌려야 하냐고 불평함", "A tenant complains about having to rent a whole office just for a one-hour meeting"),
         "caption": ("가끔 쓰는 일 때문에 사무실 전체를 유지하긴 아까워요.", "Keeping a whole office for something you use rarely feels wasteful."),
         "small": ("그 사무실은 1년 내내 거의 비어 있는데도요.", "Even though that office sits empty almost all year.")},
        {"svg": P2, "alt": ("사무실이 비어 있는데도 월세는 매달 계속 나간다고 말하는 입주사", "A tenant notes rent keeps going out every month even while the office sits empty"),
         "caption": ("안 쓰는 시간에도 고정비는 계속 나가요.", "Even unused hours still rack up fixed cost."),
         "small": ("쓴 만큼만 내는 방법은 없을까요?", "Isn't there a way to pay only for what's used?")},
        {"svg": P3, "hero": True, "alt": ("시간제 회의실이 쓸 때만 문을 열고, 입주사가 웃으며 그 앞에 서 있음", "An hourly meeting room opens its door only when used, with a smiling tenant standing in front"),
         "caption": ("서버리스 = 쓸 때만 여는 시간제 회의실이에요.", "Serverless = an hourly meeting room that opens only when used."),
         "small": ("사무실(서버) 관리는 건물이 다 해줘요.", "The building handles all the \"office\" management for you."),
         "tricks": (4, [
             (PAYG_I, ("쓴 시간만큼만 내요", "Pay only for the hours used"), ("안 쓰는 동안엔 실행 요금이 0원이에요", "no run charges while unused"), "calm"),
             (NOMGMT_I, ("사무실 관리는 건물이 해요", "The building manages the \"office\""), ("나는 회의 내용(코드)만 신경 써요", "you only worry about the meeting itself (your code)")),
             (EVENT_I, ("요청이 오면 회의실 문이 열려요", "The room opens when a request arrives"), ("이벤트 기반이라고 불러요", "called event-driven"), "warm"),
             (COLD_I, ("닫혀 있던 회의실은 처음 열 때 살짝 느려요", "A closed room is a bit slow to open the first time"), ("콜드 스타트라고 불러요", "called a cold start")),
         ])},
        {"svg": P4, "alt": ("상시 사무실과 시간제 회의실을 비용·관리·대기상태·문 여는 속도로 비교한 안내판", "A board comparing always-on office vs hourly meeting room on cost, upkeep, standby state, and opening speed"),
         "caption": ("상시 사무실과 시간제 회의실은 비용·관리·대기·문 여는 속도가 갈려요.", "Always-on office and hourly meeting room differ on cost, upkeep, standby, and opening speed."),
         "small": ("가끔만 쓰는 일이면 시간제 회의실이 상시 사무실보다 비용이 덜 들어요.", "For occasional work, the hourly room costs less than an always-on office.")},
        {"svg": P5, "alt": ("왼쪽: 닫혀 있던 회의실 문을 여는 데 시간이 걸려 땀 흘림(콜드 스타트). 오른쪽: 하루 종일 쓰는 일엔 상시 사무실이 더 맞음", "Left: opening a closed meeting room takes time, tenant sweating (cold start). Right: all-day work still fits an always-on office better"),
         "caption": ("시간제 회의실은 처음 열 때 살짝 느리고(콜드 스타트), 오래 걸리는 작업엔 안 맞아요.", "An hourly room is a bit slow to open at first (cold start), and it's not great for long-running work."),
         "small": ("시간제 회의실(서버리스)은 짧고 가끔 있는 일에 맞아요.", "The hourly room (serverless) fits short, occasional work best.")},
    ],
    "summary": (("<b>서버리스</b> = 쓸 때만 <b>자동으로 문이 열리고</b>, <b>쓴 시간만큼만</b> 내는 시간제 회의실. 사무실(서버) 관리는 건물이 대신해요.",
                 "<b>Serverless</b> is an hourly meeting room whose door <b>opens automatically</b> only when used, and you <b>pay only for the time used</b>. The building handles all the \"office\" management for you."),
                ("서버가 없다는 뜻이 아니라, 클라우드 제공자가 서버를 관리해서 내가 신경 쓸 필요가 없다는 뜻이에요. 요청이 들어올 때만 코드가 실행되고(이벤트 기반, 예: FaaS), 쓴 만큼만 과금돼요. 한동안 요청이 없어 내려가 있던 코드가 다시 깨어날 때 생기는 지연을 콜드 스타트라고 해요.",
                 "It doesn't mean there's no server — it means the cloud provider manages it, so you never have to. Code runs only when triggered (event-driven, e.g. FaaS), and billing follows exact usage. When code that was shut down after a while without requests wakes up again, the delay is called a cold start.")),
    "glossary": [
        ("서버리스", "Serverless", ("쓸 때만 여는 시간제 회의실.", "The meeting room that opens only when used."), ("서버가 없는 게 아니라 신경 쓸 필요가 없는 거예요.", "It's not that there's no server — you just never manage one.")),
        ("FaaS", "FaaS (Function as a Service)", ("회의실 안에서 할 일 한 가지만 맡기는 방식.", "Handing the room just one single task to run."), ("요청이 오면 그 요청을 맡을 함수가 실행돼요.", "When a request arrives, the function that handles it runs.")),
        ("이벤트 기반", "Event-driven", ("요청이 와야 문이 열리는 방식.", "The door opens only when a request arrives."), ("요청이 없으면 내 코드는 실행되지 않아요.", "With no request, your code doesn't run.")),
        ("콜드 스타트", "Cold start", ("닫힌 문을 처음 여는 데 걸리는 시간.", "The time it takes to open a closed door for the first time."), ("자주 쓰는 함수는 이미 깨어 있어서 이 지연이 줄어요.", "Frequently used functions are already awake, so this delay shrinks.")),
        ("종량제 과금", "Pay-as-you-go", ("쓴 시간만큼만 내는 방식.", "Paying only for the hours actually used."), ("상시 사무실의 고정 월세와 반대예요.", "The opposite of an always-on office's flat rent.")),
        ("가상머신(VM)/컨테이너", "VM / Container", ("상시 켜져 있는 독채·칸막이 사무실.", "The always-on private office or partitioned desk."), ('서버리스보다 한 단계 무거운 선택이에요. → <a href="vmcontainer-ko.html">독채 사무실과 칸막이 책상</a>', 'A step heavier than serverless. → <a href="vmcontainer-en.html">the private office and the partitioned desk</a>')),
        ("오토스케일", "Auto scale", ("회의실 수를 자동으로 늘리는 것.", "Automatically adding more meeting rooms."), ('서버리스에선 회의실 수 늘리기를 건물이 완전히 알아서 해줘요. → <a href="scaleupout-ko.html">사무실을 키울까 더 빌릴까</a>', 'In serverless, the building adds rooms completely on its own. → <a href="scaleupout-en.html">bigger office or more offices</a>')),
        ("엣지 컴퓨팅", "Edge computing", ("동네 가까운 작은 지점 사무실.", "A small branch office close to the neighborhood."), ('서버리스 함수를 엣지에 두기도 해요. → <a href="edgefog-ko.html">동네 가까운 작은 지점</a>', 'Serverless functions are sometimes placed at the edge too. → <a href="edgefog-en.html">the small branch close to the neighborhood</a>')),
    ],
}
