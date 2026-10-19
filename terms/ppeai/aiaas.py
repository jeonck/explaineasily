from _draw import *
from _world import *

# 1. 작은 농가는 선별기를 직접 만들기 어려워요
P1 = svg(300, sky(300)
         + person(170, 170, s=0.8, face=SWEAT + EYES, **FARMER)
         + produce(280, 230, 0.8) + produce(310, 240, 0.8) + produce(340, 225, 0.8)
         + bubble(380, 80, 240, 56, "⟦선별기를 직접 만들려니 너무 비싸고 복잡해요|building my own sorter is way too costly and complicated⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦작은 농가마다 큰 기계를 들이긴 부담스러워요|a big machine is a heavy lift for every small farm⟧", 12, "var(--ink)"))

# 2. 중앙 검사장이 선별기를 빌려줘요
P2 = svg(310, '<rect width="760" height="310" fill="var(--good-soft)"/>'
         + gradeboard(300, 40, 220, 100, "⟦중앙 선별 서비스|CENTRAL SORTING SERVICE⟧", ("⟦구독료만 내면 바로 사용|pay a subscription, use right away⟧",), 0.9)
         + person(120, 220, s=0.65, face=SMILE, **FARMER) + produce(170, 260, 0.6)
         + person(620, 220, s=0.65, face=SMILE, **FARMER) + produce(660, 260, 0.6)
         + label(420, 170, "⟦사진만 보내면 등급이 돌아와요|send a photo, get a grade back⟧", 12, "var(--good)")
         + label(380, 290, "⟦여러 농가가 같은 선별기를 인터넷으로 나눠 써요|many farms share the same sorter over the network⟧", 12, "var(--ink)"))

# 3. AIaaS = 선별기를 직접 만들지 않고, 구독료로 인터넷 너머에서 빌려 쓰는 것 (hero)
P3 = svg(360, sky(360)
         + gradeboard(260, 50, 260, 150, "⟦AIaaS 이용권|AIaaS SUBSCRIPTION⟧", ("⟦사진 보내기 → 등급 받기|send photo → get grade⟧", "⟦쓴 만큼만 결제|pay only for what you use⟧"), 0.95)
         + person(130, 210, s=0.85, face=SMILE, **FARMER)
         + label(380, 30, "⟦AIaaS = 선별기를 직접 두지 않고, 구독료만 내고 인터넷 너머에서 빌려 쓰는 것|AIaaS = not owning the sorter — renting it over the network for a subscription fee⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦기계는 중앙 검사장 안에 있고, 나는 사진만 보내요|the machine stays at the central station — I just send a photo⟧", 12, "var(--muted)"))

PAY_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M26 22 v20 M38 22 v20 M24 27 h16 M24 37 h16" stroke="var(--accent)" stroke-width="3"/>')
API_I = icon('<rect x="10" y="22" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="36" y="22" width="18" height="18" rx="3" fill="var(--good)"/><path d="M28 31 h8" stroke="#142033" stroke-width="3"/>')
MAINT_I = icon('<circle cx="32" cy="32" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 8 v10 M32 46 v10 M8 32 h10 M46 32 h10 M15 15 l7 7 M42 42 l7 7 M15 49 l7 -7 M42 22 l7 -7" stroke="var(--accent)" stroke-width="3"/>')
NOOWN_I = icon('<rect x="14" y="24" width="36" height="26" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M12 48 L52 16" stroke="var(--bad)" stroke-width="4"/>')

# 4. 직접 만들기 vs AIaaS 비교
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 330, 280, "⟦직접 선별기 만들기|BUILD YOUR OWN SORTER⟧",
                      ("⟦초기비용 — 매우 큼|upfront cost — very high⟧", "⟦유지보수 — 내가 직접|maintenance — on you⟧",
                       "⟦확장 — 농가 늘면 기계도 더|scale — more farms need more machines⟧", "⟦통제권 — 전부 내 것|control — fully yours⟧"), 0.9)
         + gradeboard(390, 30, 330, 280, "⟦AIaaS 구독하기|SUBSCRIBE TO AIaaS⟧",
                      ("⟦초기비용 — 거의 없음|upfront cost — nearly none⟧", "⟦유지보수 — 중앙이 담당|maintenance — the provider handles it⟧",
                       "⟦확장 — 구독만 늘리면 됨|scale — just add subscriptions⟧", "⟦통제권 — 제공자 규칙을 따름|control — follows the provider's rules⟧"), 0.9))

# 5. 한계도 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SWEAT + EYES, **FARMER)
         + label(190, 230, "⟦인터넷이 끊기면 등급을 못 받아요|no network, no grade back⟧", 11, "var(--bad)")
         + person(570, 150, s=0.8, face=EYES, **FARMER)
         + label(570, 230, "⟦내 작물 사진이 남의 서버에 가 있어요|my crop photos sit on someone else's server⟧", 11, "var(--ink)")
         + label(380, 280, "⟦빠른 응답이나 민감한 자료가 중요하면 온디바이스 쪽도 같이 생각해요|if speed or sensitive data matters most, weigh on-device too⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "aiaas", "order": 17,
    "title": ("선별기를 사지 않고 구독하는 농가들", "The Farms That Subscribe to the Sorter Instead of Buying One"),
    "h1": ("<em>AIaaS(AI as a Service)</em>이/가 뭐예요?", "What is <em>AIaaS (AI as a Service)</em>?"),
    "sub": ("AIaaS를, 선별기를 직접 사는 대신 중앙 검사장의 선별기를 구독료로 빌려 쓰는 농가들 이야기로 풀어봤어요.",
            "AIaaS, told as a story about small farms that subscribe to a central station's sorter instead of building their own."),
    "panels": [
        {"svg": P1, "alt": ("작은 농가 주인이 선별기를 직접 만들기엔 너무 비싸고 복잡하다며 땀을 흘림", "A small farmer sweats, saying building their own sorter is too expensive and complicated"),
         "caption": ("작은 농가는 선별기를 직접 만들기 어려워요.", "A small farm struggles to build its own sorter."),
         "small": ("작은 농가마다 큰 기계를 들이긴 부담스러워요.", "A big machine is a heavy lift for every small farm.")},
        {"svg": P2, "alt": ("중앙 검사장이 선별 서비스를 내놓고, 여러 농가가 사진을 보내 등급을 받아옴", "A central station offers a sorting service, and several farms send photos and get grades back"),
         "caption": ("중앙 검사장이 선별기를 빌려줘요.", "The central station rents out its sorter."),
         "small": ("여러 농가가 같은 선별기를 인터넷으로 나눠 써요.", "Many farms share the same sorter over the network.")},
        {"svg": P3, "hero": True, "alt": ("농가 주인이 AIaaS 이용권을 들고 웃고 있고, 기계는 그림 속 중앙 검사장 안에 있음", "A farmer smiles holding an AIaaS subscription, while the machine itself stays at the central station"),
         "caption": ("AIaaS는 선별기를 직접 두지 않고 구독료로 빌려 쓰는 것이에요.", "AIaaS means not owning the sorter — renting it for a subscription fee."),
         "small": ("기계는 중앙 검사장 안에 있고, 나는 사진만 보내요.", "The machine stays at the central station — I just send a photo."),
         "tricks": (4, [
             (PAY_I, ("쓴 만큼만 결제", "Pay for what you use"), ("구독료나 건당 요금이에요", "a subscription or a per-use fee"), "calm"),
             (API_I, ("사진만 보내면 돼요", "Just send a photo"), ("API로 요청하고 등급을 받아요", "request via API, get the grade back")),
             (MAINT_I, ("유지보수는 중앙 몫", "Maintenance is the provider's job"), ("기계 고장·업데이트는 신경 안 써도 돼요", "you don't worry about repairs or updates"), "warm"),
             (NOOWN_I, ("직접 소유하지 않아요", "You don't own the machine"), ("선별기는 내 집에 없어요", "the sorter never sits in your own barn")),
         ])},
        {"svg": P4, "alt": ("선별기를 직접 만드는 쪽과 AIaaS를 구독하는 쪽을 초기비용·유지보수·확장성·통제권 네 항목으로 비교", "A side-by-side comparison of building your own sorter versus subscribing to AIaaS across upfront cost, maintenance, scaling, and control"),
         "caption": ("직접 만들기와 AIaaS를 나란히 비교해요.", "Building your own is compared side by side with AIaaS."),
         "small": ("초기비용과 유지보수는 줄지만, 통제권은 제공자 규칙을 따라야 해요.", "Upfront cost and maintenance drop, but control follows the provider's rules.")},
        {"svg": P5, "alt": ("왼쪽: 인터넷이 끊겨 등급을 못 받는 농가. 오른쪽: 내 작물 사진이 남의 서버에 가 있다고 걱정하는 농가", "Left: a farm can't get a grade back because the network is down. Right: a farm worries its crop photos sit on someone else's server"),
         "caption": ("한계도 있어요.", "There are limits too."),
         "small": ("빠른 응답이나 민감한 자료가 중요하면 온디바이스 쪽도 같이 생각해요.", "If speed or sensitive data matters most, weigh on-device too.")},
    ],
    "summary": (("<b>AIaaS</b> = 선별기(모델)를 <b>직접 만들거나 소유하지 않고</b>, <b>구독료나 건당 요금</b>으로 인터넷 너머의 AI를 빌려 쓰는 방식.",
                 "<b>AIaaS</b> = using AI <b>without building or owning the model yourself</b> — renting it over the network for a <b>subscription or per-use fee</b>."),
                ("AI as a Service는 모델 개발·학습·인프라를 클라우드 제공자가 맡고, 사용자는 API 호출만으로 추론 결과를 받는 서비스 형태예요. 초기 투자·전문인력 없이 빠르게 쓸 수 있는 대신, 네트워크 의존·데이터가 외부 서버를 거치는 점·제공자 종속(vendor lock-in)이라는 트레이드오프가 있어요. 지연시간·개인정보가 중요한 경우 온디바이스 AI와 함께 고려해요.",
                 "AI as a Service means a cloud provider handles model development, training, and infrastructure, while the user just calls an API to get inference results. It enables fast adoption without upfront investment or in-house expertise, but trades that off against network dependency, data passing through external servers, and vendor lock-in. When latency or privacy matters, weigh it against on-device AI.")),
    "glossary": [
        ("API", "API", ("사진을 보내고 등급표를 받는 창구.", "The counter where you send a photo and get a grade back."), ("요청과 응답이 오가는 정해진 통로예요.", "A fixed channel for requests and responses.")),
        ("클라우드", "Cloud", ("선별기가 실제로 놓인 중앙 검사장.", "The central station where the sorter actually sits."), ("기계와 전기·공간은 전부 거기 있어요.", "The machine, power, and space all live there.")),
        ("벤더 종속", "Vendor Lock-in", ("한 중앙 검사장에만 익숙해지는 것.", "Getting used to only one central station."), ("다른 서비스로 옮기기 번거로워질 수 있어요.", "Switching to another provider can become a hassle.")),
        ("온디바이스 AI", "On-device AI", ("내 농장 창고 안의 작은 선별기.", "A small sorter inside your own farm shed."), ('빌리지 않고 직접 갖는 선택지예요. → <a href="ondeviceai-ko.html">자세히 보기</a>', "The option of owning it yourself instead of renting. → <a href=\"ondeviceai-en.html\">see it in full</a>")),
        ("AI 개인정보보호", "AI Data-Privacy Compliance", ("남의 서버로 간 작물 사진을 지키는 서류함.", "The paperwork cabinet protecting photos sent to someone else's server."), ('AIaaS를 쓸 때 꼭 같이 봐야 해요. → <a href="aiprivacyppe-ko.html">자세히 보기</a>', 'A must-check whenever you use AIaaS. → <a href="aiprivacyppe-en.html">see it in full</a>')),
        ("추론", "Inference", ("선별기가 실제로 등급을 매기는 순간.", "The moment the sorter actually assigns a grade."), ('AI 세계의 기본 개념이에요. → <a href="inference-ko.html">자세히 보기</a>', 'A core AI concept. → <a href="inference-en.html">see it in full</a>')),
        ("오픈 웨이트", "Open Weights", ("우리 집에 직접 둔 앵무새(모델).", "The parrot — the model — kept at your own house."), ('AIaaS와 반대되는 선택지를 다루는 페이지예요. → <a href="openweights-ko.html">자세히 보기</a>', 'The page covering the opposite choice from AIaaS. → <a href="openweights-en.html">see it in full</a>')),
        ("AI 신뢰성", "AI Trustworthiness", ("정확도만으론 못 받는 품질인증 등급판.", "The certification board accuracy alone can't earn."), ('빌려 쓰는 선별기도 이 기준으로 점검해야 해요. → <a href="aitrust-ko.html">자세히 보기</a>', 'A rented sorter must be checked against this too. → <a href="aitrust-en.html">see it in full</a>')),
    ],
}
