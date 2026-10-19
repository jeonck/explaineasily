from _draw import *
from _world import *

# 1. 분류소 직원이 봉투 겉면 동네 이름만 보고 아무 데나 던짐
P1 = svg(300, sky(300)
         + person(220, 170, s=0.85, face=EYES, **SORTER)
         + envelope(340, 130, 0.55, text="⟦12동네|Town 12⟧") + envelope(400, 160, 0.55, text="⟦12동네|Town 12⟧")
         + person(560, 180, s=0.6, face=FROWN, **RECEIVER) + person(620, 130, s=0.6, face=FROWN, **RECEIVER)
         + label(380, 40, "⟦분류소 직원이 동네 이름만 보고 아무 창구로나 던져요|the sorter only reads the town name, then tosses it to any counter⟧", 12, "var(--ink)")
         + label(380, 270, "⟦같은 동네에도 '웹용' '메일용' 창구가 따로 있는데 섞여버려요|the same town has separate counters for web vs mail — but they get mixed up⟧", 12, "var(--bad)"))

# 2. 창구별로 처리 속도·중요도가 다른데 구분을 못 함
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + envelope(220, 150, 0.6, text="⟦80번 창구|counter 80⟧") + bubble(160, 90, 150, 36, "⟦저는 급한 거예요|mine is urgent⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + envelope(540, 150, 0.6, text="⟦25번 창구|counter 25⟧") + bubble(480, 90, 150, 36, "⟦저는 느려도 돼요|mine can wait⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 260, "⟦동네 이름만으론 이 둘을 구분할 수가 없어요|the town name alone can't tell these two apart⟧", 12, "var(--ink)"))

# 3. hero: L4 스위치 = 봉투 안 창구 번호(포트)까지 보고 나누는 분류 직원
P3 = svg(340, sky(340)
         + person(380, 110, s=0.9, face=EYES, **SORTER)
         + envelope(220, 190, 0.6, text="80") + envelope(380, 220, 0.6, text="443") + envelope(540, 190, 0.6, text="25")
         + label(380, 30, "⟦L4 스위치 = 동네 이름뿐 아니라 창구 번호(포트)까지 보고 나누는 직원|L4 switch = a sorter who reads the counter number (port) too, not just the town⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦같은 동네 안에서도 용도별로 길을 갈라줘요|even within the same town, it splits the path by purpose⟧", 12, "var(--muted)"))

I1 = icon('<rect x="10" y="22" width="44" height="22" rx="4" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><text x="32" y="37" font-size="12" font-weight="700" fill="var(--accent)" text-anchor="middle">PORT</text>')
I2 = icon('<circle cx="18" cy="24" r="7" fill="var(--good)"/><circle cx="46" cy="24" r="7" fill="var(--good)"/><path d="M18 24 Q32 44 46 24" stroke="var(--good)" stroke-width="4" fill="none"/>')
I3 = icon('<rect x="8" y="26" width="48" height="12" rx="6" fill="var(--stone)"/><rect x="8" y="26" width="20" height="12" rx="6" fill="var(--accent)"/>')
I4 = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M32 20 v12 l9 5" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. L2/L3/L4 비교표 — 뭘 보고 나누는지
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦뭘 보고 나누나요|WHAT DOES IT READ⟧",
                    ("⟦L2 스위치 — 바로 옆 건물 번호(MAC)만 봐요|L2 switch — reads only the neighboring building's own tag (MAC)⟧",
                     "⟦L3 라우터 — 동네 이름(IP 주소)까지 봐요|L3 router — reads the town name (IP address) too⟧",
                     "⟦L4 스위치 — 창구 번호(포트)까지 보고 고르게 나눠요|L4 switch — reads the counter number (port) too, and spreads the load⟧",
                     "⟦로드밸런싱 — 같은 창구 여러 곳에 고르게 보내요|load balancing — spreads work evenly across same-type counters⟧"), 1.0))

# 5. 한계: 창구 안 쪽지 내용까지는 못 읽어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.75, face=SMILE, **SORTER) + label(190, 240, "⟦창구 번호까지는 빠르게 봐요|reads the counter number fast⟧", 11, "var(--ink)")
         + envelope(570, 150, 0.6) + label(570, 240, "⟦봉투 속 내용까지는 못 읽어요(그건 L7)|but not what's inside the envelope (that's L7)⟧", 11, "var(--ink)")
         + label(380, 282, "⟦내용까지 보는 건 더 똑똑한(L7) 장비의 몫이에요|reading the content itself is a smarter (L7) device's job⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "l4switch", "order": 19,
    "title": ("창구 번호까지 보는 분류소 직원", "The Sorter Who Checks the Counter Number Too"),
    "h1": ("<em>L4 스위치</em>가 뭐예요?", "What is an <em>L4 Switch</em>?"),
    "sub": ("L4 스위치를, 동네 이름뿐 아니라 창구 번호까지 보고 택배를 나눠주는 분류소 직원 이야기로 풀어봤어요.",
            "An L4 switch, told as a story about a sorter who reads the counter number too, not just the town name, when handing off packages."),
    "panels": [
        {"svg": P1, "alt": ("분류소 직원이 동네 이름만 보고 봉투를 아무 창구로나 던져 받는 사람들이 당황함", "A sorter reads only the town name and tosses envelopes to any counter, confusing the receivers"),
         "caption": ("분류소 직원이 동네 이름만 보고 던져요.", "The sorter only reads the town name, then tosses it anywhere."),
         "small": ("같은 동네에도 용도별 창구가 따로 있는데 섞여버려요.", "The same town has separate counters by purpose — but they get mixed up.")},
        {"svg": P2, "alt": ("봉투 두 개가 각각 다른 창구 번호를 가리키며 급함과 여유로움을 말함", "Two envelopes point to different counter numbers, one urgent, one not"),
         "caption": ("창구별로 처리 속도·중요도가 달라요.", "Different counters need different speed and priority."),
         "small": ("동네 이름만으론 이 둘을 구분할 수가 없어요.", "The town name alone can't tell these two apart.")},
        {"svg": P3, "hero": True, "alt": ("분류소 직원이 봉투마다 적힌 창구 번호 80, 443, 25를 보고 각기 다른 길로 나눠 보냄", "A sorter reads counter numbers 80, 443, 25 on each envelope and sends them down different paths"),
         "caption": ("L4 스위치 = 창구 번호(포트)까지 보고 나누는 직원이에요.", "An L4 switch = a sorter who reads the counter number (port) too."),
         "small": ("같은 동네 안에서도 용도별로 길을 갈라줘요.", "Even within the same town, it splits the path by purpose."),
         "tricks": (4, [
             (I1, ("포트 확인", "Check the Port"), ("창구 번호를 읽어요", "reads the counter number")),
             (I2, ("고르게 분산", "Spread Evenly"), ("한쪽으로 몰리지 않게", "no pile-up on one side"), "calm"),
             (I3, ("우선순위", "Priority"), ("급한 창구를 먼저", "urgent counters go first"), "warm"),
             (I4, ("상태 확인", "Health Check"), ("닫힌 창구는 피해요", "avoids a closed counter")),
         ])},
        {"svg": P4, "alt": ("L2/L3/L4가 각각 무엇을 읽고 나누는지 보여주는 안내판", "A guide board showing what L2, L3, and L4 each read to make their split"),
         "caption": ("계층마다 보는 게 달라요.", "Each layer reads something different."),
         "small": ("L4는 포트까지 보고 같은 창구 여럿에 고르게 나눠요(로드밸런싱).", "L4 reads the port too and spreads load evenly across same-type counters (load balancing).")},
        {"svg": P5, "alt": ("왼쪽: 창구 번호까지는 빠르게 봄. 오른쪽: 봉투 속 내용까지는 못 읽음(L7의 몫)", "Left: reads the counter number fast. Right: can't read what's inside the envelope (an L7 job)"),
         "caption": ("봉투 속 내용까지는 못 읽어요.", "It can't read what's inside the envelope."),
         "small": ("내용까지 보는 건 더 똑똑한(L7) 장비의 몫이에요.", "Reading the content itself is a smarter (L7) device's job.")},
    ],
    "summary": (("<b>L4 스위치</b> = 동네 이름(IP)뿐 아니라 <b>창구 번호(포트)</b>까지 읽어서, 같은 용도 창구끼리 트래픽을 <b>고르게 나눠주는</b> 분류소 직원.",
                 "<b>L4 switch</b> = a sorter that reads the <b>counter number (port)</b> too, not just the town (IP), <b>spreading</b> traffic evenly across same-purpose counters."),
                ("L4 스위치는 OSI 4계층(전송계층) 정보인 TCP/UDP 포트 번호까지 참조해 트래픽을 분배하는 장비예요. IP 주소만 보는 L3 라우팅보다 더 세밀하게, 서비스별·세션별로 로드밸런싱을 할 수 있지만, 패킷 내용(애플리케이션 데이터)까지는 들여다보지 않아요.",
                 "An L4 switch distributes traffic by also referencing OSI Layer 4 (transport layer) information — TCP/UDP port numbers. Compared to L3 routing, which only sees IP addresses, it load-balances more precisely by service and session, but it doesn't inspect the packet's content (application data) itself.")),
    "glossary": [
        ("포트 번호", "Port Number", ("건물 안 몇 번 창구인지.", "Which counter inside the building."), ("같은 주소 안 서비스를 구분해요.", "Distinguishes services at the same address.")),
        ("로드밸런싱", "Load Balancing", ("같은 창구 여러 곳에 고르게 나눠주기.", "Spreading work evenly across same-type counters."), ("L4 스위치의 대표적인 쓰임이에요.", "A signature use of an L4 switch.")),
        ("L2/L3/L4", "L2/L3/L4", ("바로 옆 건물·동네·창구 번호, 보는 범위가 다름.", "Neighbor, town, counter number — each layer sees a wider scope."), ('OSI 7계층 중 2~4계층이에요. → <a href="osi7-ko.html">7단계로 나뉜 배송 공정</a>', 'Layers 2 through 4 of the OSI 7-layer model. → <a href="osi7-en.html">the delivery process split into 7 stages</a>')),
        ("전송계층", "Transport Layer", ("포트와 등기·일반우편을 다루는 단계.", "The stage that handles ports and the registered/plain choice."), ('L4 스위치가 참조하는 바로 그 계층이에요. → <a href="transportlayer-ko.html">포트를 나누고 신뢰도를 고르는 단계</a>', 'The very layer an L4 switch references. → <a href="transportlayer-en.html">the stage that splits ports and picks reliability</a>')),
        ("트래픽 쉐이핑·폴리싱", "Traffic Shaping/Policing", ("창구마다 접수량을 조절하는 규칙.", "The rule controlling intake at each counter."), ('창구를 나눈 뒤에 함께 적용하는 규칙이에요. → <a href="trafficshaping-ko.html">택배량을 조절하는 창구</a>', 'A rule applied once counters are split this way. → <a href="trafficshaping-en.html">the counter that controls the flow</a>')),
        ("서브네팅", "Subnetting", ("동네를 작은 구역으로 나누는 것.", "Splitting a town into smaller zones."), ('동네를 나누는 L3 수준의 이야기예요. → <a href="subnetting-ko.html">동네를 작은 우편번호 구역으로 나누기</a>', 'The L3-level story of splitting a town. → <a href="subnetting-en.html">splitting the town into smaller zip-code zones</a>')),
        ("WAF/L7 장비", "WAF/L7 Device", ("봉투 속 내용까지 읽는 더 똑똑한 장비.", "A smarter device that reads inside the envelope too."), ("다른 세계(보안)에서 다루는 주제예요.", "A topic covered in another world (Security).")),
        ("IPC(네트워크)", "Network IPC", ("포트로 상대를 특정하는 전용 편지함.", "The dedicated mailbox that picks its target by port."), ('포트 개념을 실제로 쓰는 예시예요. → <a href="ipc-ko.html">프로세스끼리 여는 전용 편지함</a>', 'A concrete example of using port numbers. → <a href="ipc-en.html">the dedicated mailbox between processes</a>')),
    ],
}
