from _draw import *
from _world import *

# 1. 창구가 늘었다 줄었다 하는데 손님이 어디가 열려 있는지 몰라서 닫힌 창구 앞에 줄섬
P1 = svg(300, sky(300)
         + booth(110, 230, 0.8, label_text="⟦1번|No.1⟧", lit=True)
         + booth(280, 230, 0.8, label_text="⟦2번|No.2⟧", lit=False)
         + '<g transform="translate(280,245)"><rect x="-32" y="-16" width="64" height="8" fill="var(--bad)" transform="rotate(-8)"/><rect x="-32" y="-2" width="64" height="8" fill="var(--bad)" transform="rotate(6)"/></g>'
         + booth(450, 230, 0.8, label_text="⟦3번|No.3⟧", lit=True)
         + person(580, 184, s=0.45, face=SWEAT, extra=CLIPBOARD, shirt="#7B3FA0")
         + queueline(615, 184, 3, 0.4, 24)
         + bubble(430, 80, 260, 54, "⟦지도엔 2번이 열려있다는데...?|the map says booth 2 is open...?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦창구가 늘었다 줄었다 하는데, 어디가 열렸는지 몰라서 닫힌 곳 앞에 줄서요|booths open and close, and not knowing which is which means lining up at a closed one⟧", 12, "var(--ink)"))

# 2. 왜: 기구 수가 자동으로 늘고 주는데 종이 지도엔 금방 틀려져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(140, 230, 0.7) + booth(230, 230, 0.7) + booth(320, 230, 0.7)
         + label(230, 160, "⟦방금 두 개 더 늘었어요|two more just opened⟧", 11, "var(--bad)")
         + booth(410, 230, 0.6) + booth(480, 230, 0.6)
         + person(590, 174, s=0.6, face=SWEAT, extra=CLIPBOARD, shirt="#7B3FA0")
         + bubble(590, 70, 170, 50, "⟦종이엔 아직 세 개뿐인데...|the paper still says only three...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦기구 수가 자동으로 늘고 주는데, 종이 지도는 금방 틀려져요|the count changes on its own, and a paper map goes stale fast⟧", 12, "var(--ink)"))

# 3. hero: 창구가 열리고 닫힐 때마다 스스로 안내판에 등록·삭제해요
P3 = svg(340, sky(340)
         + board(280, 40, 200, 170, "⟦안내판|SIGN⟧", ("⟦1번 — 열림|No.1 — open⟧", "⟦2번 — 열림|No.2 — open⟧", "⟦3번 — 삭제됨|No.3 — removed⟧", "⟦4번 — 방금 등록!|No.4 — just joined!⟧"), 1.0, hl=3)
         + booth(130, 280, 0.8, label_text="⟦1번|No.1⟧") + booth(620, 280, 0.8, label_text="⟦4번(새로 열림)|No.4 (new)⟧")
         + '<path d="M210 250 L285 170" stroke="var(--good)" stroke-width="2.5" stroke-dasharray="5 4"/>'
         + '<path d="M560 250 L480 150" stroke="var(--good)" stroke-width="2.5" stroke-dasharray="5 4"/><path d="M490 160 l-14 -6 4 16z" fill="var(--good)"/>'
         + label(380, 30, "⟦창구가 열리고 닫힐 때마다, 스스로 안내판에 등록하고 지워요|every time a booth opens or closes, it registers or erases itself on the sign⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦그래서 다들 항상 최신 안내판만 보면 돼요|so everyone just has to check the latest sign⟧", 12, "var(--muted)"))

# 4. 안내판에 실시간으로 창구가 추가/삭제되고, 기구들도 안내판을 보고 서로 찾아감
P4 = svg(300, sky(300)
         + board(300, 30, 220, 150, "⟦안내판|SIGN⟧", ("⟦1번|No.1⟧", "⟦2번|No.2⟧", "⟦4번(새)|No.4 (new)⟧"), 1.0, hl=2)
         + ride(140, 230, 0.6, color="var(--accent)") + '<path d="M180 200 Q240 150 300 100" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
         + ride(620, 230, 0.6, color="#5B8DEF") + '<path d="M600 200 Q540 150 520 100" stroke="#5B8DEF" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
         + label(380, 282, "⟦기구들도 서로 찾아갈 때 안내판을 봐요|rides look at the sign too, to find each other⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 안내판이 틀리면 헛걸음 — 헬스체크와 같이 써야 정확해요
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + board(260, 30, 240, 90, "⟦안내판|SIGN⟧", ("⟦2번 — 열림|No.2 — open⟧",), 1.0)
         + booth(380, 220, 0.8, lit=False) + '<g transform="translate(380,196)"><rect x="-32" y="-5" width="64" height="8" fill="var(--bad)" transform="rotate(-8)"/><rect x="-32" y="7" width="64" height="8" fill="var(--bad)" transform="rotate(6)"/></g>'
         + person(300, 170, s=0.45, face=FROWN, shirt="#7B3FA0")
         + label(380, 270, "⟦방금 닫혔는데 안내판은 아직 '열림'|just closed, but the sign still says \"open\"⟧", 11, "var(--bad)")
         + label(380, 300, "⟦헛걸음해요 — 헬스 체크와 같이 써야 정확해요|a wasted trip — pair it with health checks to stay accurate⟧", 12, "var(--ink)"))

REGISTER_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M32 22 v20 M22 32 h20" stroke="var(--good)" stroke-width="5" stroke-linecap="round"/>')
DEREGISTER_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 32 h20" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
LOOKUP_I = icon('<circle cx="26" cy="26" r="16" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M38 38 L54 54" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
MULTIBOARD_I = icon('<rect x="8" y="10" width="34" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="20" y="24" width="34" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M26 32 h20 M26 40 h14" stroke="#142033" stroke-width="2"/>')

PAGE = {
    "slug": "servicediscovery", "order": 30,
    "title": ("지금 열린 창구 안내판", "The Sign That Shows Which Booths Are Open"),
    "h1": ("<em>서비스 디스커버리</em>가 뭐예요?", "What is <em>Service Discovery</em>?"),
    "sub": ("서비스 디스커버리를, 지금 어느 창구가 열려 있는지 알려주는 안내판 이야기로 풀어봤어요.",
            "Service discovery, told as a story about a sign that always shows which booths are open right now."),
    "panels": [
        {"svg": P1, "alt": ("손님이 종이 지도를 들고 닫힌 2번 창구 앞에 줄을 서 있음", "A guest holds a paper map and lines up in front of the closed booth 2"),
         "caption": ("창구가 늘었다 줄었다 하는데, 어디가 열렸는지 몰라서 닫힌 곳 앞에 줄서요.", "Booths open and close, and not knowing which is which means lining up at a closed one."),
         "small": ("종이 지도는 2번이 열려 있다고 하는데, 사실은 닫혔어요.", "The paper map says booth 2 is open — but it isn't anymore.")},
        {"svg": P2, "alt": ("창구 다섯 개가 늘어섰는데 손님의 종이엔 아직 세 개뿐이라고 적혀 있음", "Five booths now stand in a row, but the guest's paper still lists only three"),
         "caption": ("기구 수가 자동으로 늘고 주는데, 종이 지도는 금방 틀려져요.", "The count changes on its own, and a paper map goes stale fast."),
         "small": ("방금 두 개 더 늘었는데, 아무도 종이를 못 고쳐요.", "Two more just opened, and no one updates the paper in time.")},
        {"svg": P3, "hero": True, "alt": ("안내판에 창구 1,2,4번은 열림으로, 3번은 삭제됨으로 실시간 표시됨", "The sign shows booths 1, 2, and 4 as open and booth 3 as removed, all in real time"),
         "caption": ("창구가 열리고 닫힐 때마다, 스스로 안내판에 등록하고 지워요.", "Every time a booth opens or closes, it registers or erases itself on the sign."),
         "small": ("그래서 다들 항상 최신 안내판만 보면 돼요.", "So everyone just has to check the latest sign."),
         "tricks": (4, [
             (REGISTER_I, ("열리면 스스로 등록해요", "Register itself when it opens"), ("'저 열었어요' 하고요", "\"I'm open\""), "calm"),
             (DEREGISTER_I, ("닫히면 스스로 지워요", "Erase itself when it closes"), ("또는 헬스체크로 빠져요", "or drops out via a health check")),
             (LOOKUP_I, ("남들은 안내판만 보면 돼요", "Others just read the sign"), ("일일이 찾아다닐 필요 없어요", "no need to go looking around"), "warm"),
             (MULTIBOARD_I, ("안내판도 여러 개 둬요", "Keep more than one sign"), ("안내판도 죽을 수 있으니까요", "the sign itself can go down too")),
         ])},
        {"svg": P4, "alt": ("안내판에 창구 목록이 실시간으로 바뀌고, 기구들도 서로 화살표로 안내판을 참고해 찾아감", "The sign's booth list updates live, and rides reference it too, finding each other by arrow"),
         "caption": ("기구들도 서로 찾아갈 때 안내판을 봐요.", "Rides look at the sign too, to find each other."),
         "small": ("손님만이 아니라, 기구끼리도 안내판으로 찾아가요.", "Not just guests — rides find one another through the sign as well.")},
        {"svg": P5, "alt": ("안내판엔 아직 '열림'이라 적힌 2번 창구가 사실은 막 닫혀서, 손님이 헛걸음함", "The sign still says booth 2 is open, but it just closed, so a guest makes a wasted trip"),
         "caption": ("방금 닫혔는데 안내판은 아직 '열림'이라고 하면, 헛걸음해요.", "If the sign still says \"open\" right after closing, it's a wasted trip."),
         "small": ("헬스 체크와 같이 써야 안내판이 정확해요.", "Pairing it with health checks is what keeps the sign accurate.")},
    ],
    "summary": (("<b>서비스 디스커버리</b> = 창구가 <b>열리고 닫힐 때마다 스스로 안내판에 등록·삭제</b>해서, 다들 <b>항상 최신 안내판</b>만 보면 되게 하는 일. 안내판이 틀리면 헛걸음하니 <b>헬스 체크</b>와 함께 써야 해요.",
                 "<b>Service discovery</b> = having each booth <b>register and erase itself on the sign</b> the instant it opens or closes, so everyone only ever needs to read the <b>latest sign</b>. A wrong sign means a wasted trip, so it's paired with <b>health checks</b>."),
                ("서버(서비스 인스턴스)가 늘고 줄 때마다 스스로 등록·해제되는 레지스트리를 두어, 다른 서비스나 로드 밸런서가 항상 최신 목록을 조회할 수 있게 하는 메커니즘이에요. DNS 기반으로 구현하기도 하고, 오토스케일링과 짝을 이뤄 꼭 필요해져요.",
                 "A mechanism where servers (service instances) register and deregister themselves as they scale up and down, in a registry other services or load balancers can always query for the current list. It's sometimes built on DNS, and becomes essential once paired with autoscaling.")),
    "glossary": [
        ("서비스 디스커버리", "Service discovery", ("지금 뭐가 열려 있는지 알려주는 안내판 체계.", "The whole system behind a sign that shows what's open right now."), ("창구 수가 자꾸 바뀌는 곳엔 꼭 필요해요.", "Essential wherever the number of booths keeps changing.")),
        ("레지스트리", "Registry", ("창구 목록이 실제로 적히는 안내판 그 자체.", "The actual sign where the booth list is written."), ("다들 이 한 곳만 보면 돼요.", "Everyone only has to check this one place.")),
        ("등록/해제", "Register / deregister", ("창구가 열리거나 닫힐 때 스스로 하는 일.", "What a booth does to itself when it opens or closes."), ("누가 대신 적어주는 게 아니라, 스스로 적고 스스로 지워요.", "No one writes it for you — it writes and erases itself.")),
        ("헬스 체크 연동", "Health-check integration", ("창구가 진짜 살아 있는지 확인하고 안내판을 고치는 일.", "Confirming a booth is truly alive, and fixing the sign accordingly."), ("등록만 믿으면 틀린 안내판이 남을 수 있어요.", "Trusting registration alone can leave a stale sign behind.")),
        ("DNS 기반 디스커버리", "DNS-based discovery", ("마을 안내소 같은 이름표로 찾는 방식.", "Finding things by a name tag, like the town directory."), ('마을 안내소 이야기와 같은 원리예요. → <a href="dns-ko.html">마을 안내소</a>', 'Same idea as the town directory. → <a href="dns-en.html">the town directory</a>')),
        ("오토스케일링과의 관계", "Relation to autoscaling", ("창구 수를 자동으로 늘리고 줄이는 일과의 짝.", "Its partnership with the thing that adds and removes booths automatically."), ("창구 수가 자동으로 바뀌니까, 안내판도 자동이어야 해요.", "Since the count changes automatically, the sign has to keep up automatically too.")),
        ("로드 밸런서", "Load balancer", ("손님을 어느 창구로 보낼지 정하는 안내원.", "The usher who decides which booth to send a guest to."), ('안내판을 보고 어디로 보낼지 정해요. → <a href="loadbalancer-ko.html">줄 안내원</a>', 'It reads the sign to decide where to send each guest. → <a href="loadbalancer-en.html">the queue usher</a>')),
        ("서비스 메시", "Service mesh", ("기구들끼리 다니는 길 자체를 관리하는 체계.", "The system that manages the paths rides take between each other."), ("서비스 디스커버리는 그 길 찾기의 한 부분이에요.", "Service discovery is one part of finding that path.")),
    ],
}
