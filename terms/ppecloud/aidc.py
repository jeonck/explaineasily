from _draw import *
from _world import *

# 1. AI 입주사가 엄청난 전력 먹는 장비를 들여왔어요
P1 = svg(300, sky(300)
         + office(260, 160, 1.0)
         + '<rect x="280" y="190" width="50" height="60" fill="var(--stone-dark)"/>' + label(305, 260, "⟦GPU 장비|GPU rack⟧", 10, "var(--muted)")
         + person(420, 198, s=0.8, face=SWEAT, **TENANT)
         + bubble(460, 60, 280, 60, "⟦이 장비, 전기를 어마어마하게 먹는데요!|this rack eats an enormous amount of power!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦AI 입주사가 전력을 엄청나게 쓰는 장비를 들여왔어요|an AI tenant has brought in equipment that draws enormous power⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 일반 사무실 전기·냉방으로는 감당이 안 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + office(300, 90, 0.9) + '<rect x="320" y="120" width="50" height="60" fill="var(--stone-dark)"/>'
         + person(480, 150, s=0.65, face=FROWN + SWEAT, **LANDLORD)
         + bubble(500, 60, 240, 56, "⟦차단기가 계속 내려가요, 에어컨도 못 따라가요|the breaker keeps tripping, and the AC can't keep up⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦일반 사무실 전기·냉방으로는 이런 장비를 감당 못 해요|ordinary office power and AC just can't handle equipment like this⟧", 12, "var(--ink)"))

# 3. hero: AI 데이터센터 = 이 장비만을 위해 지은 특수 전용 별관
P3 = svg(340, sky(340)
         + building(50, 40, 1.0, label_text="⟦일반 건물|ordinary building⟧")
         + building(380, 20, 1.25, floors=5, label_text="⟦AI 전용 별관: 고전력·고냉각|AI-only annex: high power, heavy cooling⟧")
         + '<rect x="400" y="150" width="30" height="100" fill="var(--accent)"/><rect x="440" y="150" width="30" height="100" fill="var(--accent)"/><rect x="480" y="150" width="30" height="100" fill="var(--accent)"/>'
         + label(380, 345, "⟦GPU 장비만 위한 별도 전력선과 냉각 배관을 따로 깔아요|a separate power line and cooling pipe, built just for the GPU racks⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 일반 층 vs AI 전용 별관 비교
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦일반 건물 vs AI 전용 별관|ordinary building vs AI-only annex⟧",
                     ("⟦전력 밀도: 보통 vs 훨씬 더 높음|power density: normal vs much higher⟧",
                      "⟦냉각: 에어컨 바람 vs 액체 냉각까지 동원|cooling: AC air vs even liquid cooling⟧",
                      "⟦네트워크: 보통 배선 vs 초고속 전용 배선|network: normal wiring vs ultra-fast dedicated wiring⟧",
                      "⟦들어설 수 있는 땅: 어디든 vs 전력 넉넉한 곳만|where it can be built: almost anywhere vs only where power is abundant⟧"), 1.0))

# 5. 깨지는 곳: 건설비가 비싸고, 전력 수급 자체가 병목이 돼요
P5 = svg(300, sky(300)
         + building(560, 50, 1.0, floors=5)
         + person(430, 198, s=0.75, face=FROWN + SWEAT, **LANDLORD)
         + bubble(100, 60, 300, 70, "⟦별관 짓는 데만 큰돈이 들고, 동네 전력 자체가 모자라요|building the annex costs a fortune, and the neighborhood's power itself falls short⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦건설비도, 전력 확보 자체도 쉽지 않아요|construction cost and securing enough power are both genuinely hard⟧", 12, "var(--ink)"))

POWER_I = icon('<path d="M34 6 L14 36 h14 l-6 22 l26 -32 h-16 z" fill="var(--accent)"/>')
COOL_I = icon('<path d="M8 32 h48 M32 8 v48 M14 14 l36 36 M50 14 l-36 36" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
NET_I = icon('<circle cx="32" cy="12" r="6" fill="var(--accent)"/><circle cx="12" cy="48" r="6" fill="var(--accent)"/><circle cx="52" cy="48" r="6" fill="var(--accent)"/><path d="M32 18 L12 42 M32 18 L52 42" stroke="var(--accent)" stroke-width="3"/>')
SITE_I = icon('<path d="M32 8 C44 8 52 18 52 28 C52 42 32 56 32 56 C32 56 12 42 12 28 C12 18 20 8 32 8 Z" fill="var(--bad-soft)" stroke="var(--bad)" stroke-width="3"/>')

PAGE = {
    "slug": "aidc", "order": 8,
    "title": ("GPU만을 위한 전용 별관", "The Annex Built Just for the GPUs"),
    "h1": ("<em>AI 데이터센터</em>가 뭐예요?", "What is an <em>AI Data Center</em>?"),
    "sub": ("AI 데이터센터를, 전력을 엄청나게 먹는 GPU 장비만을 위해 따로 지은 건물 별관 이야기로 풀어봤어요.",
            "AI data centers, told as a story about a building annex constructed just for power-hungry GPU equipment."),
    "panels": [
        {"svg": P1, "alt": ("땀 흘리는 AI 입주사가 전기를 어마어마하게 먹는 GPU 장비를 사무실에 들여왔다고 말함", "A sweating AI tenant says they've brought in GPU equipment that draws enormous power"),
         "caption": ("AI 입주사가 전력을 엄청나게 쓰는 장비를 들여왔어요.", "An AI tenant has brought in equipment that draws enormous power."),
         "small": ("보통 사무실 장비와는 차원이 달라요.", "Nothing like ordinary office equipment.")},
        {"svg": P2, "alt": ("건물주가 차단기가 계속 내려가고 에어컨도 못 따라간다며 땀을 흘림", "The landlord sweats, saying the breaker keeps tripping and the AC can't keep up"),
         "caption": ("일반 사무실 전기·냉방으론 감당이 안 돼요.", "Ordinary office power and AC can't handle it."),
         "small": ("차단기도 내려가고, 에어컨도 못 따라가요.", "The breaker trips, and the AC can't keep up.")},
        {"svg": P3, "hero": True, "alt": ("일반 건물 옆에 GPU 장비 세 랙을 품은 더 높고 특수한 AI 전용 별관이 서 있음", "Beside an ordinary building stands a taller, specialized AI-only annex housing three GPU racks"),
         "caption": ("AI 데이터센터 = GPU만을 위한 전용 별관이에요.", "An AI data center is an annex built just for the GPUs."),
         "small": ("별도 전력선과 냉각 배관을 따로 깔아요.", "A separate power line and cooling pipe, built just for the GPU racks."),
         "tricks": (4, [
             (POWER_I, ("전력 밀도가 훨씬 높아요", "Power density is much higher"), ("한 칸에 훨씬 많은 전기가 몰려요", "far more power packed per rack"), "calm"),
             (COOL_I, ("냉각도 더 세게 해요", "Cooling is far more intense"), ("액체 냉각까지 동원해요", "even liquid cooling gets used")),
             (NET_I, ("초고속 전용 네트워크를 깔아요", "Runs an ultra-fast dedicated network"), ("GPU끼리 빠르게 통신해야 해서요", "GPUs need to talk to each other fast"), "warm"),
             (SITE_I, ("전력 넉넉한 땅에만 지어요", "Built only where power is abundant"), ("아무 땅에나 못 지어요", "it can't go just anywhere")),
         ])},
        {"svg": P4, "alt": ("일반 건물과 AI 전용 별관을 전력 밀도, 냉각, 네트워크, 입지 조건으로 비교한 안내판", "A board comparing ordinary building vs AI-only annex on power density, cooling, network, and siting"),
         "caption": ("네 가지 기준 모두에서 AI 전용 별관이 훨씬 세요.", "The AI-only annex goes further on all four measures."),
         "small": ("그래서 아무 곳에나 지을 수 없어요.", "That's why it can't be built just anywhere.")},
        {"svg": P5, "alt": ("건물주가 별관 짓는 데 큰돈이 들고 동네 전력 자체가 모자란다고 말풍선으로 걱정함", "The landlord worries in a speech bubble that building the annex costs a fortune and the neighborhood's power itself falls short"),
         "caption": ("건설비도, 전력 확보도 둘 다 쉽지 않아요.", "Construction cost and securing enough power are both genuinely hard."),
         "small": ("전력 수급 자체가 병목이 되기도 해요.", "Power supply itself can become the bottleneck.")},
    ],
    "summary": (("<b>AI 데이터센터</b> = GPU처럼 전력을 엄청나게 먹는 장비만을 위해 <b>전력·냉각·네트워크를 따로 설계</b>한 전용 별관.",
                 "An <b>AI data center</b> is a dedicated annex with <b>power, cooling, and networking all designed separately</b>, just for power-hungry equipment like GPUs."),
                ("AI 모델 학습·추론에 쓰이는 GPU/가속기는 전력 밀도와 발열이 일반 서버보다 훨씬 커서, 고밀도 전력 공급과 액체 냉각, 저지연 고속 인터커넥트(GPU 간 통신)를 전제로 설계된 전용 데이터센터가 필요해요. 건설비와 전력 확보가 새로운 병목이 돼요.",
                 "GPUs and accelerators used for AI training and inference draw far more power and generate far more heat than ordinary servers, requiring data centers purpose-built for high-density power delivery, liquid cooling, and low-latency high-speed interconnects between GPUs. Construction cost and securing enough power have become the new bottlenecks.")),
    "glossary": [
        ("AI 데이터센터", "AI data center", ("GPU만을 위한 전용 별관.", "An annex built just for the GPUs."), ("전력·냉각·네트워크를 따로 설계해요.", "Power, cooling, and networking are all designed separately.")),
        ("GPU/가속기", "GPU / accelerator", ("전력을 엄청나게 먹는 특수 장비.", "The specialized equipment that draws enormous power."), ("AI 학습·추론을 빠르게 해줘요.", "Speeds up AI training and inference.")),
        ("전력 밀도", "Power density", ("한 칸에 몰리는 전기의 양.", "How much power is packed into one rack."), ("AI 전용 별관은 일반 건물보다 훨씬 높아요.", "Much higher in an AI-only annex than in an ordinary building.")),
        ("액체 냉각", "Liquid cooling", ("에어컨 바람보다 더 센 냉각 방식.", "A cooling method stronger than just AC air."), ("발열이 너무 커서 필요해졌어요.", "Needed because the heat output is just too much.")),
        ("인터커넥트", "Interconnect", ("GPU끼리 빠르게 통신하는 전용 배선.", "The dedicated wiring GPUs use to talk to each other fast."), ("학습 속도에 큰 영향을 줘요.", "Has a big effect on training speed.")),
        ("가상머신/컨테이너", "VM / Container", ("일반 사무실에서 공간을 나누는 두 방법.", "The two ways to divide space in an ordinary office."), ('GPU 장비도 이 위에서 나눠 쓰기도 해요. → <a href="vmcontainer-ko.html">독채 사무실과 칸막이 책상</a>', 'GPU equipment is sometimes divided this way too. → <a href="vmcontainer-en.html">the private office and the partitioned desk</a>')),
        ("스케일 업/아웃", "Scale-up / Scale-out", ("사무실을 키울지, 더 빌릴지.", "Making one office bigger, or renting more of them."), ('AI 전용 별관은 스케일업(더 센 장비)에 더 가까워요. → <a href="scaleupout-ko.html">사무실을 키울까 더 빌릴까</a>', 'AI annexes lean toward scale-up (beefier equipment). → <a href="scaleupout-en.html">bigger office or more offices</a>')),
        ("클라우드 서비스 모델", "Cloud service model", ("뼈대만/인테리어까지/완제품.", "Bare shell / interior done / move-in ready."), ('GPU 인프라도 IaaS로 빌릴 수 있어요. → <a href="cloudmodel-ko.html">셋 중 골라 빌리기</a>', 'GPU infrastructure can be rented as IaaS too. → <a href="cloudmodel-en.html">pick one to rent</a>')),
    ],
}
