from _draw import *
from _world import *

# 1. 외딴 밭에서는 인터넷이 잘 안 터져요
P1 = svg(300, sky(300)
         + person(170, 170, s=0.8, face=EYES, **FARMER) + produce(260, 230, 0.8)
         + bubble(320, 80, 220, 50, "⟦여기선 신호가 잘 안 잡혀서 중앙에 사진을 못 보내요|signal's weak out here — I can't send photos to the central station⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦인터넷이 끊기면 중앙 선별 서비스도 못 써요|no network means the central sorting service is unreachable⟧", 12, "var(--ink)"))

# 2. 기다리는 동안 작물이 상해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=FROWN, **FARMER) + produce(300, 210, 0.8, bad=True)
         + label(260, 250, "⟦신호 기다리다 작물이 물러져요|waiting for signal, the crop goes soft⟧", 11, "var(--bad)")
         + person(560, 150, s=0.75, face=EYES, **OPERATOR)
         + label(560, 230, "⟦중앙까지 보내는 데도 시간이 걸려요|even sending it to the center takes time⟧", 11, "var(--ink)")
         + label(380, 280, "⟦제자리에서 바로 판단할 작은 선별기가 필요해요|we need a small sorter that decides right here, right now⟧", 12, "var(--ink)"))

# 3. 온디바이스 AI = 선별기를 작게 줄여 내 창고 안에 직접 두는 것 (hero)
P3 = svg(360, sky(360)
         + gradeboard(70, 70, 200, 70, "⟦창고 안 작은 선별기|THE SMALL SORTER IN THE SHED⟧", ("⟦인터넷 없이 바로 작동|works offline, right away⟧",), 0.9)
         + person(380, 170, s=0.9, face=SMILE, **FARMER) + bin_(460, 250, 0.7, "⟦합격|PASS⟧")
         + label(380, 30, "⟦온디바이스 AI = 선별기를 가볍게 줄여, 내 창고(기기) 안에 직접 두고 인터넷 없이 바로 쓰는 것|on-device AI = shrinking the sorter and keeping it right in your own shed, no network needed⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦사진이 밖으로 안 나가고, 그 자리에서 답이 나와요|the photo never leaves the shed — the answer comes right there⟧", 12, "var(--muted)"))

SHRINK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="22" y="22" width="20" height="20" rx="3" fill="var(--accent)"/>')
OFFLINE_I = icon('<path d="M10 46 q22 -24 44 0" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="46" r="4" fill="var(--accent)"/><path d="M12 14 L52 50" stroke="var(--bad)" stroke-width="4"/>')
LOCALDATA_I = icon('<path d="M8 32 L32 12 L56 32 V56 H8 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="24" y="36" width="16" height="18" fill="var(--accent)"/>')
LIMIT_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M22 42 l20 -20" stroke="var(--bad)" stroke-width="4"/>')

# 4. 중앙 선별 서비스 vs 온디바이스
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 330, 280, "⟦중앙 선별 서비스(AIaaS)|CENTRAL SERVICE (AIaaS)⟧",
                      ("⟦응답 — 신호 상태에 좌우|speed — depends on signal⟧", "⟦오프라인 — 못 씀|offline — unusable⟧",
                       "⟦사진 이동 — 밖으로 나감|photo travel — leaves the farm⟧", "⟦성능 — 큰 기계라 더 정교함|power — bigger machine, finer judgment⟧"), 0.9)
         + gradeboard(390, 30, 330, 280, "⟦온디바이스 AI|ON-DEVICE AI⟧",
                      ("⟦응답 — 즉시|speed — instant⟧", "⟦오프라인 — 그대로 작동|offline — still works⟧",
                       "⟦사진 이동 — 창고 밖으로 안 나감|photo travel — stays in the shed⟧", "⟦성능 — 줄인 만큼 살짝 둔함|power — a bit duller after shrinking⟧"), 0.9))

# 5. 작게 줄인 만큼 한계도 있어요
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **FARMER) + bin_(260, 230, 0.6, "⟦합격|PASS⟧")
         + label(190, 270, "⟦흔한 작물은 빠르고 정확해요|common crops get fast, accurate calls⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=EYES, **FARMER)
         + label(570, 262, "⟦처음 보는 희귀 품종엔 자신감이 떨어져요|a rare, unfamiliar crop shakes its confidence⟧", 11, "var(--bad)")
         + label(380, 300, "⟦기기 저장공간·배터리에 맞춰 줄인 만큼, 큰 선별기보다 아는 게 적어요|shrunk to fit the device's storage and battery, it simply knows less than the big one⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ondeviceai", "order": 18,
    "title": ("창고 안에 직접 둔 작은 선별기", "The Small Sorter Kept Right in the Shed"),
    "h1": ("<em>온디바이스 AI</em>이/가 뭐예요?", "What is <em>On-device AI</em>?"),
    "sub": ("온디바이스 AI를, 인터넷이 안 되는 외딴 밭에서도 바로 작동하도록 가볍게 줄여 창고 안에 둔 작은 선별기 이야기로 풀어봤어요.",
            "On-device AI, told as a story about a sorter shrunk down and kept right in the shed, so it still works out in a field with no signal."),
    "panels": [
        {"svg": P1, "alt": ("외딴 밭의 농부가 신호가 약해 중앙 선별 서비스에 사진을 보낼 수 없다고 말함", "A farmer in a remote field says the signal is too weak to send photos to the central sorting service"),
         "caption": ("외딴 밭에서는 인터넷이 잘 안 터져요.", "Out in a remote field, the signal doesn't reach well."),
         "small": ("인터넷이 끊기면 중앙 선별 서비스도 못 써요.", "No network means the central sorting service is unreachable.")},
        {"svg": P2, "alt": ("농부가 신호를 기다리는 동안 작물이 물러지고, 조작원도 중앙까지 보내는 데 시간이 걸린다고 함", "The crop goes soft while the farmer waits for signal, and the operator notes that reaching the center also takes time"),
         "caption": ("기다리는 동안 작물이 상해요.", "The crop spoils while waiting."),
         "small": ("제자리에서 바로 판단할 작은 선별기가 필요해요.", "A small sorter that decides right here, right now, is what's needed.")},
        {"svg": P3, "hero": True, "alt": ("농부가 창고 안의 작은 선별기로 작물을 바로 합격 판정하며 웃음", "A farmer smiles as the small sorter in the shed passes a crop right on the spot"),
         "caption": ("온디바이스 AI는 선별기를 작게 줄여 내 창고 안에 직접 두는 것이에요.", "On-device AI means shrinking the sorter and keeping it right in your own shed."),
         "small": ("사진이 밖으로 안 나가고, 그 자리에서 답이 나와요.", "The photo never leaves the shed — the answer comes right there."),
         "tricks": (4, [
             (SHRINK_I, ("가볍게 줄이기", "Shrink it down"), ("압축·양자화로 작게 만들어요", "made small via compression and quantization"), "calm"),
             (OFFLINE_I, ("인터넷 없이 작동", "Works offline"), ("신호가 없어도 멈추지 않아요", "doesn't stop even with no signal")),
             (LOCALDATA_I, ("사진이 안 나가요", "The photo stays put"), ("창고 밖 서버로 안 보내요", "never sent to a server outside the shed"), "warm"),
             (LIMIT_I, ("성능은 살짝 둔해져요", "A bit duller"), ("줄인 만큼 중앙보다는 약해요", "shrinking trades away some sharpness")),
         ])},
        {"svg": P4, "alt": ("중앙 선별 서비스와 온디바이스 AI를 응답속도·오프라인 가능여부·사진 이동·성능 네 항목으로 비교", "The central sorting service and on-device AI compared across response speed, offline capability, photo travel, and power"),
         "caption": ("중앙 서비스와 온디바이스를 나란히 비교해요.", "The central service and on-device AI are compared side by side."),
         "small": ("즉시 응답·오프라인·데이터 보호는 얻지만, 정교함은 살짝 내줘요.", "You gain instant response, offline use, and data protection — but trade away some precision.")},
        {"svg": P5, "alt": ("왼쪽: 흔한 작물은 빠르고 정확하게 판정함. 오른쪽: 처음 보는 희귀 품종엔 자신감이 떨어짐", "Left: common crops get fast, confident calls. Right: a rare, unfamiliar crop shakes its confidence"),
         "caption": ("작게 줄인 만큼 한계도 있어요.", "Shrinking it down comes with real limits."),
         "small": ("기기 저장공간·배터리에 맞춰 줄인 만큼, 큰 선별기보다 아는 게 적어요.", "Shrunk to fit the device's storage and battery, it simply knows less than the big one.")},
    ],
    "summary": (("<b>온디바이스 AI</b> = 선별기(모델)를 <b>가볍게 줄여</b> 내 기기(창고) 안에 <b>직접 두고</b>, <b>인터넷 없이 그 자리에서</b> 바로 쓰는 방식.",
                 "<b>On-device AI</b> means <b>shrinking</b> the model and keeping it <b>right on your own device</b>, running it <b>right there, with no network needed</b>."),
                ("On-device AI는 모델을 양자화·경량화(distillation 등)해 폰·노트북·IoT 기기 안에서 직접 추론을 돌리는 방식이에요. 지연시간이 거의 없고, 데이터가 기기 밖으로 나가지 않아 프라이버시에 유리하지만, 저장공간·배터리·연산력 제약 때문에 중앙 클라우드 모델보다 크기와 성능이 제한돼요. AIaaS(클라우드 서비스)와는 반대되는 선택지로, 지연시간·오프라인·프라이버시가 중요하면 온디바이스를, 최고 성능이 중요하면 클라우드를 골라요.",
                 "On-device AI quantizes and lightens a model (e.g. via distillation) to run inference directly on a phone, laptop, or IoT device. Latency is near zero and data never leaves the device, which helps privacy — but storage, battery, and compute limits cap the model's size and performance compared to a central cloud model. It's the opposite choice from AIaaS (a cloud service): pick on-device when latency, offline use, or privacy matter most; pick cloud when top performance matters most.")),
    "glossary": [
        ("양자화", "Quantization", ("선별기 부품을 가볍게 줄이는 기술.", "The technique that lightens the sorter's parts."), ('모델을 작게 만드는 핵심 기술이에요. → <a href="quantization-ko.html">자세히 보기</a>', 'A core technique for shrinking a model. → <a href="quantization-en.html">see it in full</a>')),
        ("지연시간", "Latency", ("신호를 기다리는 시간.", "The time spent waiting for signal."), ("온디바이스는 이게 거의 없어요.", "On-device all but eliminates this.")),
        ("오프라인 추론", "Offline Inference", ("인터넷 없이도 작동하는 판정.", "A judgment call made with no network at all."), ("창고 안에서 바로 끝나요.", "It finishes right inside the shed.")),
        ("경량화 · 지식증류", "Model Compression · Distillation", ("큰 선별기의 요령만 작은 선별기에 옮기는 일.", "Transferring only the big sorter's know-how into a small one."), ("온디바이스에 올리기 전 흔히 거치는 과정이에요.", "A step usually taken before putting a model on-device.")),
        ("AIaaS", "AIaaS", ("선별기를 사지 않고 구독하는 쪽.", "Subscribing to the sorter instead of buying one."), ('온디바이스와 반대되는 선택지예요. → <a href="aiaas-ko.html">자세히 보기</a>', 'The opposite choice from on-device. → <a href="aiaas-en.html">see it in full</a>')),
        ("AI 개인정보보호", "AI Data-Privacy Compliance", ("작물 사진을 지키는 서류함.", "The paperwork cabinet protecting crop photos."), ('온디바이스는 이 부담을 많이 덜어줘요. → <a href="aiprivacyppe-ko.html">자세히 보기</a>', 'On-device greatly eases this burden. → <a href="aiprivacyppe-en.html">see it in full</a>')),
        ("엣지 컴퓨팅", "Edge Computing", ("농가 근처에 둔 작은 계산대.", "A small computing post kept near the farm."), ("온디바이스는 엣지 컴퓨팅의 한 종류예요.", "On-device AI is one form of edge computing.")),
        ("AI 신뢰성", "AI Trustworthiness", ("정확도만으론 못 받는 품질인증 등급판.", "The certification board accuracy alone can't earn."), ('줄인 선별기도 이 기준으로 다시 점검해요. → <a href="aitrust-ko.html">자세히 보기</a>', 'A shrunk sorter is checked against this too. → <a href="aitrust-en.html">see it in full</a>')),
    ],
}
