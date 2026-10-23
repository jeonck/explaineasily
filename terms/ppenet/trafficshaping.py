from _draw import *
from _world import *

# 1. 접수 창구에 택배가 한꺼번에 쏟아짐
P1 = svg(300, sky(300)
         + person(140, 170, s=0.85, face=SWEAT + EYES, **CLERK)
         + envelope(260, 130, 0.6) + envelope(300, 150, 0.6) + envelope(340, 120, 0.6) + envelope(380, 150, 0.6) + envelope(420, 130, 0.6)
         + label(380, 40, "⟦갑자기 택배가 한꺼번에 쏟아져요|suddenly a flood of packages arrives at once⟧", 13, "var(--ink)")
         + label(380, 270, "⟦이대로 다 받으면 분류소가 마비돼요|taking them all in would jam the whole sorting office⟧", 13, "var(--bad)"))

# 2. 두 가지 선택: 넘치는 건 버리거나(폴리싱), 줄 세워 쟁여두거나(쉐이핑)
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **CLERK) + envelope(270, 110, 0.5) + label(300, 100, "✕", 22, "var(--bad)", cls="d")
         + label(190, 250, "⟦폴리싱: 넘치면 바로 돌려보내요|policing: send overflow straight back⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **SORTER) + envelope(650, 190, 0.45) + envelope(670, 205, 0.45) + envelope(690, 220, 0.45)
         + label(570, 250, "⟦쉐이핑: 줄 세워뒀다 순서대로 보내요|shaping: queue them and send in order⟧", 11, "var(--ink)"))

# 3. hero: 트래픽 폴리싱·쉐이핑 = 접수량을 조절하는 두 가지 방법
P3 = svg(340, sky(340)
         + person(380, 130, s=0.95, face=EYES, **CLERK)
         + routemap(60, 40, 300, 100, "⟦폴리싱|POLICING⟧", ("⟦기준 넘으면 즉시 버림|over limit → dropped now⟧",), 1.0)
         + routemap(400, 40, 300, 100, "⟦쉐이핑|SHAPING⟧", ("⟦기준 넘으면 줄 세워 대기|over limit → queued, waits⟧",), 1.0)
         + label(380, 230, "⟦트래픽 폴리싱·쉐이핑 = 접수량이 넘칠 때 처리 방식을 정하는 규칙|traffic policing/shaping = the rule for handling overflow at the counter⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦버릴지, 기다리게 할지 — 창구마다 미리 정해둬요|drop it, or make it wait — decided in advance per counter⟧", 12, "var(--muted)"))

I1 = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="var(--bad)"/><path d="M22 22 l20 20 M42 22 l-20 20" stroke="#fff" stroke-width="5" stroke-linecap="round"/>')
I2 = icon('<rect x="8" y="40" width="10" height="16" fill="var(--good)"/><rect x="22" y="30" width="10" height="26" fill="var(--good)"/><rect x="36" y="20" width="10" height="36" fill="var(--good)"/><rect x="50" y="46" width="10" height="10" fill="var(--line)"/>')
I3 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 20 v12 l9 5" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
I4 = icon('<rect x="10" y="26" width="44" height="12" rx="4" fill="var(--stone)"/><rect x="10" y="26" width="18" height="12" rx="4" fill="var(--accent)"/>')

# 4. 네 가지 핵심 포인트
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦창구 운영 규칙|COUNTER RULES⟧",
                    ("⟦버리기 — 폴리싱은 넘치면 그냥 버려요|drop — policing simply discards the overflow⟧",
                     "⟦쟁이기 — 쉐이핑은 버퍼에 쌓아뒀다 보내요|queue — shaping buffers it and sends later⟧",
                     "⟦지연 — 쉐이핑은 버리진 않지만 늦어져요|delay — shaping doesn't drop, but it's late⟧",
                     "⟦평균속도 — 둘 다 결국 평균 접수량을 정해진 선 아래로 맞춰요|average rate — both keep the average under one line⟧"), 1.0))

# 5. 한계: 접수량 조절이 길(라우팅) 자체를 고쳐주진 않아요
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + person(240, 130, s=0.8, face=EYES, **CLERK) + label(240, 260, "⟦창구 혼잡은 줄였어요|the counter is less jammed now⟧", 11, "var(--ink)")
         + postoffice(520, 150, 0.7) + label(520, 240, "⟦그런데 우체국 자체가 느리면 소용없어요|but a slow post office still slows everything⟧", 11, "var(--ink)")
         + label(380, 282, "⟦접수량만 조절할 뿐, 전송 경로나 속도 자체를 바꾸진 않아요|it only controls intake — it doesn't change the route or raw speed⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "trafficshaping", "order": 14,
    "title": ("접수량을 조절하는 창구 규칙", "The Counter Rule That Controls the Flow"),
    "h1": ("<em>트래픽 폴리싱·쉐이핑</em>이 뭐예요?", "What are <em>Traffic Policing & Shaping</em>?"),
    "sub": ("트래픽 폴리싱·쉐이핑을, 택배가 쏟아질 때 버리거나 줄 세우는 접수 창구 규칙 이야기로 풀어봤어요.",
            "Traffic policing and shaping, told as a story about a counter rule for handling a flood of packages — drop them, or make them queue."),
    "panels": [
        {"svg": P1, "alt": ("접수원이 한꺼번에 쏟아진 택배들 앞에서 땀을 흘림", "A clerk sweats before a sudden flood of packages"),
         "caption": ("갑자기 택배가 한꺼번에 쏟아져요.", "Suddenly a flood of packages arrives at once."),
         "small": ("이대로 다 받으면 분류소가 마비돼요.", "Taking them all in would jam the whole sorting office.")},
        {"svg": P2, "alt": ("왼쪽: 접수원이 넘치는 택배를 돌려보냄(폴리싱). 오른쪽: 분류소 직원이 택배를 줄 세움(쉐이핑)", "Left: a clerk sends overflow back (policing). Right: a sorter queues them in line (shaping)"),
         "caption": ("두 가지 선택이 있어요.", "There are two choices."),
         "small": ("폴리싱은 넘치면 바로 돌려보내고, 쉐이핑은 줄 세워뒀다 순서대로 보내요.", "Policing sends overflow straight back; shaping queues it and sends it in order.")},
        {"svg": P3, "hero": True, "alt": ("우체국장 앞에 폴리싱 안내판과 쉐이핑 안내판이 나란히 있음", "Two guide boards stand side by side before the clerk: policing and shaping"),
         "caption": ("접수량이 넘칠 때 처리 방식을 정하는 규칙이에요.", "It's the rule for handling overflow at the counter."),
         "small": ("버릴지, 기다리게 할지 — 창구마다 미리 정해둬요.", "Drop it, or make it wait — decided in advance per counter."),
         "tricks": (4, [
             (I1, ("폴리싱 = 버리기", "Policing = Drop"), ("기준 넘으면 즉시 버림", "over the limit, dropped at once")),
             (I2, ("쉐이핑 = 쟁이기", "Shaping = Queue"), ("버퍼에 쌓아뒀다 보냄", "buffered, then sent later"), "calm"),
             (I3, ("쉐이핑의 대가 = 지연", "Shaping's Cost = Delay"), ("늦어지긴 해요", "it arrives late"), "warm"),
             (I4, ("목표 = 평균속도 맞추기", "Goal = Match a Rate"), ("정해진 선 아래로", "keeps it under one line")),
         ])},
        {"svg": P4, "alt": ("창구 운영 규칙표: 버리기·쟁이기·지연·평균속도 네 줄", "A counter-rule board listing drop, queue, delay, and average rate"),
         "caption": ("핵심은 네 가지예요.", "There are four key points."),
         "small": ("둘 다 결국 평균 접수량을 정해진 선 아래로 맞추는 게 목표예요.", "Both aim to keep the average intake under one agreed line.")},
        {"svg": P5, "alt": ("왼쪽: 창구 혼잡이 줄었음. 오른쪽: 우체국 자체가 느리면 소용없음", "Left: the counter is less jammed. Right: a slow post office itself still slows things"),
         "caption": ("접수량 조절이 길 자체를 고쳐주진 않아요.", "Controlling the flow doesn't fix the road itself."),
         "small": ("전송 경로나 속도 자체를 바꾸진 않아요.", "It doesn't change the route or the raw speed.")},
    ],
    "summary": (("<b>트래픽 폴리싱·쉐이핑</b> = 접수량이 넘칠 때, 넘친 몫을 <b>버리거나(폴리싱)</b> <b>줄 세워 쟁여두는(쉐이핑)</b> 창구 규칙.",
                 "<b>Traffic policing and shaping</b> = a counter rule for overflow: policing <b>drops</b> it, shaping <b>queues</b> it."),
                ("트래픽 폴리싱은 약정된 전송률을 넘는 패킷을 즉시 폐기(또는 표시)해 네트워크를 보호하고, 트래픽 쉐이핑은 버퍼에 담아 지연시키면서 정해진 속도로 고르게 내보내는 방식이에요. 폴리싱은 손실을 감수하고, 쉐이핑은 지연을 감수해요.",
                 "Traffic policing instantly drops (or marks) packets that exceed an agreed rate to protect the network, while traffic shaping buffers them and releases them smoothly at that rate instead. Policing trades loss, shaping trades delay.")),
    "glossary": [
        ("트래픽 폴리싱", "Traffic Policing", ("넘치면 바로 버리는 규칙.", "The rule that drops overflow right away."), ("손실을 감수하고 즉시 처리해요.", "Accepts loss in exchange for instant handling.")),
        ("트래픽 쉐이핑", "Traffic Shaping", ("넘치면 줄 세워 쟁이는 규칙.", "The rule that queues overflow in line."), ("지연을 감수하고 손실은 피해요.", "Accepts delay to avoid loss.")),
        ("버스트(Burst)", "Burst", ("한꺼번에 쏟아지는 택배 더미.", "The sudden pile of packages arriving at once."), ("잠깐 몰리는 트래픽 폭증이에요.", "A short spike in traffic volume.")),
        ("버퍼(큐)", "Buffer/Queue", ("택배를 쟁여두는 대기줄.", "The waiting line where packages are stacked."), ("쉐이핑이 쓰는 저장 공간이에요.", "The storage shaping relies on.")),
        ("QoS", "QoS", ("창구마다 다른 대우를 해주는 것.", "Giving different counters different treatment."), ("이 규칙을 실현하는 더 큰 틀이에요.", "The broader framework these rules serve.")),
        ("L4 스위치", "L4 Switch", ("봉투 안 창구 번호까지 보는 분류 직원.", "The sorter who checks the counter number too."), ('비슷하게 흐름을 관리해요. → <a href="l4switch-ko.html">포트까지 보는 분류소 직원</a>', 'Also manages flow, in its own way. → <a href="l4switch-en.html">the sorter who checks the port</a>')),
        ("5G 네트워크 슬라이싱", "5G Network Slicing", ("차선 자체를 나누는 더 큰 기술.", "The bigger tech that splits the lane itself."), ('차선을 깐 뒤에 이 규칙이 필요해요. → <a href="5gcore-ko.html">상황별 전용 차선을 가진 배송망</a>', "This rule applies once that lane exists. → <a href=\"5gcore-en.html\">the network with a lane for every need</a>")),
        ("백프레셔", "Backpressure", ("너무 밀리면 보내는 쪽에 알려서 늦추는 것.", "Telling the sender upstream to slow down when it's too full."), ("다른 세계(SRE)에서 비슷한 개념을 다뤄요.", "A related idea covered in another world (SRE).")),
    ],
}
