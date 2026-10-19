from _draw import *
from _world import *

# 1. 재료가 들어와요 — 그런데 어디서 왔는지 아무도 안 적어 둬요
P1 = svg(320, sky(320)
         + person(80, 170, s=0.75, face=SMILE, **SUPPLIER) + pantry(170, 90, 0.75, w=150, h=100)
         + label(245, 220, "⟦재료가 계속 들어와요|ingredients keep coming in⟧", 11, "var(--muted)")
         + person(430, 160, s=0.8, face=EYES, **CHEF)
         + label(430, 240, "⟦어디서 왔는지는 안 물어요|nobody asks where they came from⟧", 11, "var(--ink)")
         + pantry(560, 90, 0.75, w=150, h=100, bad_shelf=2) + badge(690, 100, 0.6)
         + label(620, 210, "⟦나중에 한 선반이 상해도|later, if one shelf turns out bad,⟧", 10, "var(--bad)")
         + label(620, 224, "⟦어느 공급업체인지 몰라요|no one knows which supplier it came from⟧", 10, "var(--bad)")
         + label(380, 290, "⟦요리(모델)에 들어간 재료가 어디서 왔는지, 적어 둔 사람이 없어요|nobody wrote down where the ingredients inside the dish actually came from⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 한 요리 안에 재료가 여러 겹으로 들어가요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + recipebook(110, 90, 0.75) + label(110, 155, "⟦바탕 레시피(사전학습)|base recipe (pretraining)⟧", 11, "var(--ink)")
         + pantry(260, 60, 0.6, w=130, h=90) + label(325, 165, "⟦추가 재료(파인튜닝 자료)|added ingredients (fine-tune data)⟧", 11, "var(--ink)")
         + knifedrawer(430, 100, 0.65, labels=("⟦플러그인|plugin⟧", "⟦외부도구|outside tool⟧"))
         + label(500, 165, "⟦남이 만든 도구까지 섞여요|even someone else's tools get mixed in⟧", 11, "var(--ink)")
         + person(650, 150, s=0.75, face=EYES, **CHEF) + dish(650, 90, 0.5)
         + label(380, 220, "⟦한 접시 안에 바탕 레시피 + 추가 재료 + 외부 도구가 겹겹이 들어가요|one dish layers a base recipe, added ingredients, and outside tools, all at once⟧", 12, "var(--ink)", cls="d")
         + label(380, 250, "⟦기억만으로 다 추적하기엔 너무 많고 너무 겹쳐요|too many layers to trace from memory alone⟧", 11, "var(--muted)"))

# 3. AIBOM = 재료 출처 인증서 (hero)
P3 = svg(360, sky(360)
         + recipebook(90, 90, 0.7) + pantry(190, 100, 0.55, w=120, h=85) + knifedrawer(320, 230, 0.55, labels=("⟦도구|tool⟧",))
         + '<path d="M80 150 L420 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>'
         + board(470, 50, 260, 270, "⟦재료 출처 인증서|INGREDIENT CERTIFICATE⟧",
                 ("⟦바탕 레시피 — 어느 주방|base recipe — which kitchen⟧",
                  "⟦추가 재료 — 어느 농장·배치|added ingredients — which batch⟧",
                  "⟦외부 도구 — 어느 회사|outside tools — which vendor⟧",
                  "⟦라이선스 · 알려진 문제|license · known issues⟧"), 0.95)
         + label(380, 25, "⟦AIBOM = 이 요리에 들어간 재료의 출처를 적은 인증서|AIBOM = a certificate recording where every ingredient in this dish came from⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦손님이 아니라 주방 안쪽(검사관·사장님)이 보는 서류예요|a paper meant for inside the kitchen — inspectors, the manager — not the guest at the table⟧", 12, "var(--muted)"))

# 4. 인증서에는 이렇게 적어요
P4 = svg(320, sky(320)
         + board(220, 30, 320, 260, "⟦인증서 한 장 들여다보기|INSIDE ONE CERTIFICATE⟧",
                 ("⟦바탕 레시피 — B주방, v2.3|base recipe — Kitchen B, v2.3⟧",
                  "⟦추가 재료 — 2024년 봄 배치|added ingredients — spring 2024 batch⟧",
                  "⟦공급업체 — 재료상 C|supplier — Vendor C⟧",
                  "⟦라이선스 — 상업적 사용 ✓|license — commercial use ✓⟧",
                  "⟦알려진 문제 — 특정 향신료 과다|known issue — a certain spice runs heavy⟧"), 1.0)
         + person(100, 150, s=0.7, face=EYES, **MANAGER) + label(100, 240, "⟦사장님이 결정할 때 봐요|the manager checks it before deciding⟧", 11, "var(--muted)")
         + person(660, 150, s=0.7, face=EYES, **INSPECTOR) + badge(700, 120, 0.6)
         + label(660, 240, "⟦검사관이 사고 날 때 봐요|the inspector checks it when something goes wrong⟧", 11, "var(--muted)"))

# 5. 한계: 종이가 있어도, 공급업체가 거짓말하면 못 잡아요
P5 = svg(310, '<rect width="380" height="310" fill="var(--good-soft)"/><rect x="380" width="380" height="310" fill="var(--bad-soft)"/>'
         + board(60, 40, 260, 220, "⟦AIBOM — 이 요리만|AIBOM — just this dish⟧",
                 ("⟦학습 데이터·모델 전용|training data &amp; model only⟧", "⟦주방 안쪽에서 써요|used inside the kitchen⟧"), 0.85)
         + person(500, 120, s=0.7, face=FROWN, **SUPPLIER)
         + bubble(440, 50, 220, 44, "⟦이 재료는 깨끗한 농장산이에요 (거짓말)|these are from a clean farm (a lie)⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(570, 230, "⟦종이에 적힌 말을 그대로 믿으면 거짓도 넘어가요|trust what's written and a lie slips through too⟧", 11, "var(--bad)")
         + label(190, 280, "⟦AIBOM은 이 모델·데이터만 다뤄요 — 소프트웨어 전체 부품은 SBOM이에요|AIBOM covers only this model's data — the whole software's parts list is an SBOM⟧", 12, "var(--ink)", cls="d"))

LIST_I = icon('<rect x="10" y="8" width="44" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h28 M18 30 h28 M18 40 h20" stroke="#142033" stroke-width="2.5"/>')
TAG_I = icon('<path d="M8 32 L32 8 h20 v20 L32 56 Z" fill="var(--accent)"/><circle cx="40" cy="20" r="5" fill="#FFF8E7"/>')
VENDOR_I = icon(f'<circle cx="24" cy="18" r="10" fill="{SKIN}"/><rect x="12" y="30" width="24" height="24" rx="6" fill="#8B5E3C"/><rect x="40" y="20" width="14" height="30" rx="4" fill="#5A3B22"/>')
WARN_I = icon('<path d="M32 8 L58 54 H6 Z" fill="var(--bad)"/><rect x="29" y="22" width="6" height="16" fill="#FFF8E7"/><circle cx="32" cy="44" r="3" fill="#FFF8E7"/>')

PAGE = {
    "slug": "aibom", "order": 23,
    "title": ("재료 출처 인증서", "The Ingredient Origin Certificate"),
    "h1": ("<em>AIBOM</em>이 뭐예요?", "What is an <em>AIBOM</em>?"),
    "sub": ("AIBOM을, 이 요리에 들어간 재료가 어디서 왔는지 빠짐없이 적어 둔 인증서 이야기로 풀어봤어요.",
            "AIBOM, told as a story about a certificate that records exactly where every ingredient in this dish came from."),
    "panels": [
        {"svg": P1, "alt": ("공급업체가 재료를 창고에 들여오지만 주방장은 어디서 왔는지 묻지 않음. 나중에 한 선반의 재료가 상했지만 어느 공급업체인지 알 수 없음", "A supplier brings ingredients into the pantry and the chef never asks where they came from; later one shelf turns out bad but no one can trace which supplier it came from"),
         "caption": ("요리에 들어간 재료가 어디서 왔는지, 적어 둔 사람이 없어요.", "Nobody wrote down where the ingredients inside the dish actually came from."),
         "small": ("재료가 상했다는 걸 알아도, 돌아갈 곳이 없어요.", "Even once you know an ingredient went bad, there's nowhere to trace it back to.")},
        {"svg": P2, "alt": ("바탕 레시피, 추가 재료, 외부 도구가 한 접시 안에 겹겹이 들어감", "A base recipe, added ingredients, and outside tools all layered into one dish"),
         "caption": ("한 요리 안에 재료가 여러 겹으로 들어가요.", "One dish layers many kinds of ingredients at once."),
         "small": ("바탕 레시피 + 추가 재료 + 외부 도구, 기억만으로 다 추적하긴 너무 많아요.", "A base recipe, added data, outside tools — too many layers to trace from memory alone.")},
        {"svg": P3, "hero": True, "alt": ("바탕 레시피, 재료창고, 도구서랍이 나란히 있고, 옆에 바탕 레시피·추가 재료·외부 도구·라이선스를 적은 인증서 게시판이 있음", "A base recipe, a pantry, and a knife drawer side by side, with a certificate board next to them listing the base recipe, added ingredients, outside tools, and license"),
         "caption": ("AIBOM은 이 요리에 들어간 재료의 출처를 적은 인증서예요.", "An AIBOM is a certificate recording where every ingredient in this dish came from."),
         "small": ("손님이 아니라 주방 안쪽 — 검사관과 사장님이 보는 서류예요.", "It's a paper for inside the kitchen — inspectors and the manager, not the guest."),
         "tricks": (4, [
             (LIST_I, ("바탕 레시피 적기", "List the base recipe"), ("어느 주방의 레시피인지", "which kitchen's recipe it is"), "calm"),
             (TAG_I, ("추가 재료·배치 적기", "List added ingredients & batch"), ("어느 배치에서 왔는지", "which batch it came from"), "calm"),
             (VENDOR_I, ("공급업체 적기", "List the supplier"), ("외부 도구는 어느 회사인지", "which vendor made each outside tool"), "warm"),
             (WARN_I, ("라이선스·문제 적기", "List license & known issues"), ("상업적 사용 가능한지, 흠은 뭔지", "usable commercially? what's already known to be off"), "warm"),
         ])},
        {"svg": P4, "alt": ("인증서 한 장을 자세히 보여줌: 바탕 레시피 버전, 추가 재료 배치, 공급업체, 라이선스, 알려진 문제. 사장님과 검사관이 각자 다른 때 들여다봄", "A close-up of one certificate: base recipe version, added-ingredient batch, supplier, license, known issues; the manager and the inspector each check it at different times"),
         "caption": ("인증서에는 레시피·재료·공급업체·라이선스·문제를 적어요.", "The certificate records the recipe, ingredients, supplier, license, and known issues."),
         "small": ("사장님은 결정할 때, 검사관은 사고 날 때 들여다봐요.", "The manager checks it before deciding; the inspector checks it when something goes wrong.")},
        {"svg": P5, "alt": ("왼쪽 초록: AIBOM은 이 요리의 학습 데이터·모델만 다룬다고 적힌 게시판. 오른쪽 빨강: 공급업체가 거짓말을 해도 종이에 적힌 말을 그대로 믿으면 넘어감", "Left, green: a board noting the AIBOM covers only this dish's training data and model. Right, red: a supplier lying, and the written claim being trusted anyway"),
         "caption": ("종이가 있어도, 공급업체가 거짓말하면 못 잡아요.", "Having the paper doesn't catch it if the supplier lies on it."),
         "small": ('AIBOM은 이 모델·데이터만 다루고, 소프트웨어 전체 부품은 <a href="sbom-ko.html">SBOM</a>이 맡아요. '
                   '적힌 말을 검증 없이 믿는 건 <a href="supplychain-ko.html">공급망 공격</a>이 파고드는 틈이에요.',
                   'An AIBOM covers only this model and its data; the whole software\'s parts list is the job of an <a href="sbom-en.html">SBOM</a>. '
                   'Trusting what\'s written without checking is exactly the gap a <a href="supplychain-en.html">supply chain attack</a> slips through.')},
    ],
    "summary": (("<b>AIBOM</b> = 이 요리에 들어간 <b>재료의 출처를 적은 인증서</b>. 바탕 레시피, 추가 재료, 외부 도구, 라이선스를 적어서 주방 안쪽(사장님·검사관)이 봐요.",
                 "<b>AIBOM</b> = a certificate recording <b>where every ingredient in this dish came from</b>. It lists the base recipe, added ingredients, outside tools, and license — for use inside the kitchen, by the manager and the inspector."),
                ("AIBOM(AI Bill of Materials)은 모델에 들어간 데이터와 구성요소의 출처를 기록한 목록이에요. 베이스 모델(사전학습), 파인튜닝 데이터셋의 버전·배치, 가져다 쓴 서드파티 모델/플러그인, 라이선스, 알려진 취약점·편향 이슈를 담아요. 전체 소프트웨어 부품을 다루는 SBOM과 달리, AIBOM은 AI 모델·데이터 전용이에요. 공급망 사고가 났을 때 '어디서부터 잘못됐는지' 되짚는 데 필수적이에요.",
                 "An AIBOM (AI Bill of Materials) is a record of the provenance of the data and components that went into a model: the base model (pretraining), the versions and batches of fine-tuning datasets, any third-party models or plugins pulled in, licenses, and known vulnerabilities or bias issues. Unlike an SBOM, which covers an entire software stack's parts, an AIBOM is specific to AI models and data. It's essential for tracing back 'where it went wrong' when a supply-chain incident happens.")),
    "glossary": [
        ("AIBOM", "AIBOM", ("이 요리의 재료 출처 인증서.", "This dish's ingredient origin certificate."), ("주방 안쪽에서 보는 서류예요 — 손님용 설명표가 아니에요.", "A paper for inside the kitchen, not the guest-facing label.")),
        ("SBOM 비교", "vs. SBOM", ("소프트웨어 전체 부품 목록.", "The whole software's parts list."), ('AIBOM은 그중 AI 모델·데이터 부분만 다뤄요. → <a href="sbom-ko.html">보안 마을의 SBOM</a>', 'AIBOM covers only the AI model and data portion of it. → <a href="sbom-en.html">the security world\'s SBOM</a>')),
        ("공급망 공격", "Supply chain attack", ("재료창고에 미리 섞여 들어온 수상한 재료.", "Tainted ingredients already mixed into the pantry."), ('인증서가 거짓이면 이 틈을 못 막아요. → <a href="supplychain-ko.html">보안 마을의 공급망 공격</a>', 'A false certificate can\'t close this gap on its own. → <a href="supplychain-en.html">the security world\'s supply chain attack</a>')),
        ("바탕 레시피", "Base recipe (pretraining)", ("처음부터 익힌 요리 기본기.", "The dish's foundational training."), ('모든 요리의 출발점이에요. → <a href="pretraining-ko.html">앵무새 마을의 사전학습</a>', "It's the starting point for every dish. → <a href=\"pretraining-en.html\">the parrot world's pretraining</a>")),
        ("추가 재료", "Fine-tune data", ("바탕 레시피에 나중에 더한 재료.", "Ingredients added later, on top of the base recipe."), ('어느 배치에서 왔는지 적어 둬야 해요. → <a href="finetune-ko.html">앵무새 마을의 파인튜닝</a>', "Which batch it came from has to be on record. → <a href=\"finetune-en.html\">the parrot world's fine-tuning</a>")),
        ("오픈 웨이트 모델", "Open-weight model", ("누구나 가져다 쓸 수 있게 공개한 레시피.", "A recipe released for anyone to pick up and use."), ('가져다 쓸 때도 출처를 인증서에 적어야 해요. → <a href="openweights-ko.html">앵무새 마을의 오픈 웨이트</a>', 'Even a borrowed one needs its origin on the certificate. → <a href="openweights-en.html">the parrot world\'s open weights</a>')),
        ("라이선스 확인", "License check", ("이 재료를 돈 받고 팔아도 되는지.", "Whether this ingredient may be sold for profit."), ("인증서 한 줄로 끝나지만, 안 적으면 나중에 큰일이에요.", "It's one line on the certificate — but skip it and it becomes a big problem later.")),
        ("요리 설명표 비교", "vs. the dish's label", ("인증서는 주방 안쪽용, 설명표는 손님용.", "The certificate is for the kitchen; the label is for the guest."), ('손님에게 보여 주는 설명표는 따로 있어요. → <a href="modelcard-ko.html">요리 설명표</a>', 'The guest-facing label is a separate page. → <a href="modelcard-en.html">the dish\'s label</a>')),
    ],
}
