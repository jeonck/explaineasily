from _draw import *
from _world import *

# 1. 본사 건물이 너무 멀어요 — 동네 끝 방문객은 한참 걸려 도착해요
P1 = svg(300, sky(300)
         + building(560, 60, 0.9, label_text="⟦본사 건물(멀리)|HQ building (far away)⟧")
         + person(60, 198, s=0.8, face=SWEAT, **VISITOR)
         + '<path d="M120 220 L540 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(330, 205, "⟦한참 걸어가야 해요|a long walk to get there⟧", 12, "var(--bad)")
         + label(380, 282, "⟦동네 끝 방문객은 본사까지 한참 걸려요|a visitor from across town takes forever to reach HQ⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 모든 요청이 본사로만 몰리면 다들 오래 기다려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + building(560, 60, 0.9)
         + person(60, 198, s=0.6, face=FROWN, **VISITOR) + person(140, 198, s=0.6, face=FROWN, **VISITOR) + person(220, 198, s=0.6, face=FROWN, **VISITOR)
         + '<path d="M300 220 L540 220" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 262, "⟦다들 멀리 있는 본사로만 몰려요|everyone funnels into the same far-off HQ⟧", 12, "var(--bad)")
         + label(380, 282, "⟦본사 하나에 다 몰리면 거리만큼 기다림이 늘어요|funnel everyone into one HQ, and the wait grows with the distance⟧", 12, "var(--ink)"))

# 3. hero: 엣지=동네 가까운 작은 지점, 포그=건물들 사이 중간 허브
P3 = svg(360, sky(360)
         + building(600, 40, 0.75, label_text="⟦본사|HQ⟧")
         + building(340, 150, 0.55, label_text="⟦포그: 중간 허브|fog: middle hub⟧")
         + office(90, 260, 0.9, label_text="⟦엣지: 동네 지점|edge: local branch⟧")
         + person(30, 273, s=0.6, face=SMILE, **VISITOR)
         + '<path d="M150 280 L340 210" stroke="var(--good)" stroke-width="3" stroke-dasharray="5 4"/>'
         + '<path d="M420 190 L600 90" stroke="var(--good)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(380, 30, "⟦엣지 = 동네 지점, 포그 = 본사와 지점 사이 중간 허브|edge = the local branch, fog = the hub between it and HQ⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦가까운 곳에서 먼저 처리해서 빨라져요|handling things closer by makes it faster⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 처리 위치별 지도 — 어디서 뭘 먼저 처리하나
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦어디서 먼저 처리하나|who handles it first⟧",
                     ("⟦엣지(지점): 간단한 건 그 자리에서 바로|edge (branch): simple things, handled right there⟧",
                      "⟦포그(중간 허브): 지점 여러 곳을 묶어 정리|fog (middle hub): bundles several branches together⟧",
                      "⟦본사: 전체 저장·복잡한 분석을 맡아요|HQ: handles full storage and heavy analysis⟧",
                      "⟦거리가 짧을수록 응답이 빨라요|the shorter the distance, the faster the response⟧"), 1.0))

# 5. 깨지는 곳: 작은 지점엔 다 담을 수 없고, 결국 본사와 맞춰야 해요
P5 = svg(300, sky(300)
         + office(130, 220, 0.8) + person(90, 218, s=0.55, face=FROWN + SWEAT, **VISITOR)
         + label(190, 268, "⟦지점은 작아서 다 담을 수 없어요|the branch is too small to hold everything⟧", 11, "var(--ink)")
         + building(560, 60, 0.75)
         + '<path d="M250 220 L560 140" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 4"/>'
         + label(570, 250, "⟦결국 본사와 자료를 맞춰야 해요(동기화)|it still has to sync back up with HQ eventually⟧", 11, "var(--ink)"))

NEAR_I = icon('<circle cx="22" cy="42" r="10" fill="var(--good)"/><path d="M32 42 h20" stroke="var(--good)" stroke-width="4" stroke-dasharray="4 3"/><circle cx="56" cy="20" r="8" fill="var(--stone-dark)"/>')
LAYER_I = icon('<rect x="10" y="40" width="44" height="12" fill="var(--stone)"/><rect x="14" y="26" width="36" height="12" fill="var(--accent)"/><rect x="18" y="12" width="28" height="12" fill="var(--good)"/>')
LATENCY_I = icon('<path d="M10 50 L26 20 L42 50" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M42 50 L58 10" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="5 4"/>')
SYNC_I = icon('<path d="M44 24 a16 16 0 1 0 2 14" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M48 14 l0 12 l-12 0z" fill="var(--accent)"/>')

PAGE = {
    "slug": "edgefog", "order": 5,
    "title": ("동네 가까운 지점과 그 사이 중간 허브", "The Local Branch, and the Hub In Between"),
    "h1": ("<em>엣지·포그 컴퓨팅</em>이 뭐예요?", "What is <em>Edge and Fog Computing</em>?"),
    "sub": ("엣지·포그 컴퓨팅을, 멀리 있는 본사 대신 동네 가까운 지점과 그 중간 허브가 먼저 처리해주는 이야기로 풀어봤어요.",
            "Edge and fog computing, told as a story about a local branch — and a hub in between — handling things before the far-off HQ has to."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 방문객이 멀리 있는 본사 건물까지 한참을 걸어감", "A sweating visitor walks a long way to a distant HQ building"),
         "caption": ("동네 끝 방문객은 본사까지 한참 걸려요.", "A visitor from across town takes forever to reach HQ."),
         "small": ("거리만큼 기다림도 길어져요.", "The wait grows right along with the distance.")},
        {"svg": P2, "alt": ("방문객 셋이 모두 멀리 있는 본사로만 몰려가며 불만스러워함", "Three visitors all funnel toward the same far-off HQ, unhappy"),
         "caption": ("본사 하나에 다 몰리면 기다림이 늘어요.", "Funnel everyone into one HQ, and the wait grows."),
         "small": ("가까운 곳에서 처리할 방법이 필요해요.", "There needs to be a way to handle it closer by.")},
        {"svg": P3, "hero": True, "alt": ("동네 가까운 작은 지점, 그 사이 중간 허브, 멀리 있는 본사가 점선으로 연결되어 있고 방문객이 웃고 있음", "A small local branch, a middle hub between it and HQ, and the distant HQ connected by dashed lines, with a smiling visitor"),
         "caption": ("엣지 = 동네 지점, 포그 = 본사와 지점 사이 중간 허브예요.", "Edge = the local branch, fog = the hub between it and HQ."),
         "small": ("가까운 곳에서 먼저 처리해서 빨라져요.", "Handling things closer by makes it faster."),
         "tricks": (4, [
             (NEAR_I, ("가까운 곳이 먼저 처리해요", "The nearest spot handles it first"), ("엣지 = 동네 지점이에요", "edge = the local branch"), "calm"),
             (LAYER_I, ("포그는 지점 여러 곳을 묶어요", "Fog bundles several branches together"), ("본사와 지점 사이 중간 허브예요", "it's the hub between branch and HQ")),
             (LATENCY_I, ("거리가 짧을수록 빨라요", "The shorter the distance, the faster"), ("응답 지연이 줄어요", "response latency drops"), "warm"),
             (SYNC_I, ("그래도 결국 본사와 맞춰야 해요", "It still has to sync with HQ eventually"), ("동기화가 필요해요", "synchronization is required")),
         ])},
        {"svg": P4, "alt": ("지도: 엣지는 간단한 건 바로, 포그는 지점 여러 곳을 묶음, 본사는 전체 저장·복잡한 분석을 맡고, 거리가 짧을수록 응답이 빠름", "A map: edge handles simple things right away, fog bundles branches together, HQ handles full storage and heavy analysis, and shorter distance means faster response"),
         "caption": ("처리 위치에 따라 역할이 나뉘어요.", "Roles split depending on where processing happens."),
         "small": ("간단한 건 가까이서, 무거운 건 본사가 맡아요.", "Simple things stay close; heavy things go to HQ.")},
        {"svg": P5, "alt": ("작은 지점에서 땀 흘리는 방문객이 다 담을 수 없다고 말하고, 결국 본사와 자료를 맞춰야 함을 화살표로 보여줌", "A sweating visitor at the small branch says it can't hold everything, with an arrow showing it must still sync back to HQ"),
         "caption": ("작은 지점엔 다 담을 수 없어요.", "The branch is too small to hold everything."),
         "small": ("결국 본사와 자료를 맞춰야 해요(동기화).", "It still has to sync back up with HQ eventually.")},
    ],
    "summary": (("<b>엣지 컴퓨팅</b> = <b>동네 가까운 지점</b>에서 바로 처리하기. <b>포그 컴퓨팅</b> = 그 지점들을 묶는 <b>중간 허브</b>. 둘 다 본사(중앙)까지 가는 거리를 줄여요.",
                 "<b>Edge computing</b> means handling things right at the <b>nearby local branch</b>. <b>Fog computing</b> is the <b>hub in between</b> that bundles those branches together. Both shorten the distance to the central HQ."),
                ("엣지는 데이터가 생성되는 기기·현장 바로 가까이에서 처리하는 것(예: IoT 센서 바로 옆), 포그는 엣지와 중앙 클라우드 사이에 계층을 하나 더 두어 여러 엣지를 묶어 정리하는 것이에요. 둘 다 지연 시간을 줄이고 중앙 네트워크 부담을 낮추지만, 처리 용량과 저장 범위는 본사(중앙 클라우드)가 더 넓어요.",
                 "Edge computing processes data right next to where it's generated (e.g. right beside an IoT sensor). Fog computing adds a layer between the edge and the central cloud, bundling multiple edge nodes together. Both cut latency and reduce load on the central network, but HQ — the central cloud — still has far greater processing capacity and storage reach.")),
    "glossary": [
        ("엣지 컴퓨팅", "Edge computing", ("동네 가까운 작은 지점에서 바로 처리.", "Processing right at the small local branch."), ("데이터가 생기는 곳 바로 옆이에요.", "Right next to where the data is generated.")),
        ("포그 컴퓨팅", "Fog computing", ("지점 여러 곳을 묶는 중간 허브.", "The middle hub bundling several branches."), ("엣지와 본사 사이 한 계층 더예요.", "One more layer, between edge and HQ.")),
        ("지연 시간(레이턴시)", "Latency", ("거리만큼 늘어나는 기다림.", "The wait that grows with distance."), ("가까울수록 짧아져요.", "Shorter, the closer it is.")),
        ("동기화", "Synchronization", ("지점 자료를 본사와 맞추는 일.", "Matching branch data back up with HQ."), ("지점만으론 전체를 담을 수 없어서 필요해요.", "Needed because the branch alone can't hold it all.")),
        ("IoT", "IoT", ("현장에서 데이터를 만들어내는 기기.", "The devices out in the field generating data."), ("엣지가 바로 옆에서 처리해주는 대상이에요.", "The thing edge computing processes right next to.")),
        ("중앙 클라우드(본사)", "Central cloud (HQ)", ("전체 저장·복잡한 분석을 맡는 본사 건물.", "The HQ building handling full storage and heavy analysis."), ('이 책 전체의 배경인 그 건물이에요. → <a href="cloudmodel-ko.html">공유 오피스 빌딩</a>', 'The very building this whole book is set in. → <a href="cloudmodel-en.html">the shared office building</a>')),
        ("서버리스", "Serverless", ("쓸 때만 여는 시간제 회의실.", "The meeting room that opens only when used."), ('엣지에 서버리스 함수를 두기도 해요. → <a href="serverless-ko.html">시간제 회의실</a>', 'Serverless functions are sometimes placed at the edge too. → <a href="serverless-en.html">the hourly meeting room</a>')),
        ("오토스케일", "Auto scale", ("지점 수를 자동으로 늘리는 것.", "Automatically adding more branches."), ('엣지 지점 수도 수요에 맞춰 늘고 줄 수 있어요. → <a href="scaleupout-ko.html">사무실을 키울까 더 빌릴까</a>', 'Edge branch count can also scale with demand. → <a href="scaleupout-en.html">bigger office or more offices</a>')),
    ],
}
