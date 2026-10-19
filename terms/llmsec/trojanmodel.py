from _draw import *
from _world import *

WAREHOUSE_I = icon('<path d="M10 50 h44 M14 50 v-20 l18 -14 l18 14 v20" fill="none" stroke="var(--muted)" stroke-width="4"/>')
TRUST_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M21 32 l7 8 l13 -17" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
INSPECT_I = icon('<path d="M32 10 l16 9 v18 l-16 9 l-16 -9 v-18z" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle cx="32" cy="32" r="6" fill="#FFF8E7"/>')
ALERT_I = icon('<path d="M32 8 L54 52 H10 Z" fill="var(--bad)"/><rect x="29" y="22" width="6" height="16" fill="#FFF8E7"/><circle cx="32" cy="44" r="3" fill="#FFF8E7"/>')


def _arrow(x1, y, x2):
    return (f'<path d="M{x1} {y} H{x2 - 10}" stroke="var(--muted)" stroke-width="3"/>'
            f'<path d="M{x2 - 14} {y - 6} L{x2} {y} L{x2 - 14} {y + 6} Z" fill="var(--muted)"/>')


# 1. 다른 곳에서 만든 레시피북을 받아와요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.75, face=SMILE, **CHEF)
         + person(420, 190, s=0.7, face=SMILE, **SUPPLIER) + recipebook(420, 130, 0.6, locked=True)
         + label(420, 260, "⟦다른 곳에서 만든 레시피북이 와요|a recipe book made elsewhere arrives⟧", 12, "var(--muted)")
         + label(380, 300, "⟦어디서 어떻게 다듬어졌는지는 보이지 않아요|how or where it was refined cannot be seen⟧", 13, "var(--ink)", cls="d"))

# 2. 다듬는 틈에 몰래 쪽지가 끼워져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.75, face=FROWN, **SNEAK) + recipebook(170, 90, 0.6, open_book=True)
         + bubble(255, 40, 260, 55, "⟦다듬는 틈에 몰래 쪽지 한 장을 끼워 넣어요|while it is being refined, a note slips in⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 170, s=0.7, face=EYES, **SUPPLIER)
         + label(560, 250, "⟦공급업체도 모르게 일어날 수 있어요|even the supplier may not notice⟧", 11, "var(--bad)")
         + label(380, 280, "⟦완성되면 다시 잠기고, 안은 보이지 않아요|once finished, it locks again — no one can see inside⟧", 12, "var(--ink)"))

# 3. 트로이목마 모델 = 몰래 백도어를 심어 퍼뜨리는 것 (hero)
P3 = svg(360, sky(360)
         + person(70, 150, s=0.7, face=FROWN, **SNEAK) + recipebook(70, 95, 0.55, open_book=True)
         + person(260, 170, s=0.65, face=EYES, **SUPPLIER) + recipebook(260, 110, 0.55, locked=True)
         + person(460, 150, s=0.8, face=EYES, **CHEF) + recipebook(460, 95, 0.6, locked=True)
         + person(650, 200, s=0.55, face=EYES, **INSPECTOR) + badge(690, 170, 0.6)
         + label(380, 30, "⟦트로이목마 모델 = 몰래 백도어를 심어 퍼뜨리는 것|A Trojan Model = planting a hidden backdoor and sending it out⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦겉은 똑같이 잠긴 레시피북이에요|from outside, it is a recipe book locked just like any other⟧", 12, "var(--muted)"))

# 4. 만들기 → 다듬는 중 몰래 삽입 → 설치, 세 단계 (작동 디테일)
P4 = svg(330, sky(330)
         + recipebook(130, 100, 0.6)
         + label(130, 170, "⟦① 레시피북을 만들어요|① the recipe book gets built⟧", 11, "var(--muted)", cls="d")
         + _arrow(190, 100, 320)
         + recipebook(380, 100, 0.6, open_book=True)
         + label(380, 170, "⟦② 다듬는 중에 몰래 끼워요|② while refining, a note is slipped in⟧", 11, "var(--bad)", cls="d")
         + _arrow(440, 100, 570)
         + person(630, 140, s=0.7, face=EYES, **CHEF) + recipebook(630, 210, 0.45, locked=True)
         + label(630, 270, "⟦③ 주방이 설치해요 — 백도어도 함께|③ installed — backdoor comes too⟧", 10, "var(--bad)", cls="d")
         + label(380, 305, "⟦몇 단계를 거치든, 한 번 심기면 그대로 퍼져요|however many steps, once planted it spreads unchanged⟧", 12, "var(--ink)"))

# 5. 찾기 어렵고, 모델 자체를 바꿔야 없어져요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(140, 150, s=0.75, face=SMILE, **INSPECTOR) + badge(190, 110, 0.7)
         + label(190, 245, "⟦서명·출처를 확인해야 찾아낼 수 있어요|only checking signatures and provenance can catch it⟧", 11, "var(--ink)")
         + recipebook(560, 140, 0.7, locked=True)
         + label(560, 245, "⟦한 번 심기면 레시피북 전체를 바꿔야 해요|once planted, only swapping the whole book removes it⟧", 11, "var(--ink)")
         + label(380, 282, "⟦심는 과정이 트로이목마 모델, 심긴 결과(암호 주문어)가 백도어예요 — 모델 자체를 노린 공급망 공격이에요|planting is the trojan model story; the planted trigger is the backdoor — a supply-chain attack aimed at the model itself⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "trojanmodel", "order": 16,
    "title": ("다듬는 중에 몰래 심은 버릇", "A Habit Planted While It Was Being Refined"),
    "h1": ("<em>트로이목마 모델</em>이 뭐예요?", "What is a <em>Trojan Model</em>?"),
    "sub": ("트로이목마 모델을, 레시피북이 다듬어지는 틈에 몰래 쪽지 한 장이 끼워져 그대로 퍼지는 이야기로 풀어봤어요.",
            "A trojan model, told as a story about a note slipped into the recipe book while it is being refined — and then sent out into the world."),
    "panels": [
        {"svg": P1, "alt": ("공급업체가 잠긴 레시피북을 주방에 가져다 줌", "A supplier delivers a locked recipe book to the kitchen"),
         "caption": ("다른 곳에서 만든 레시피북을 받아와요.", "A recipe book made elsewhere arrives."),
         "small": ("어디서 어떻게 다듬어졌는지는 보이지 않아요.", "How or where it was refined cannot be seen.")},
        {"svg": P2, "hero": False, "alt": ("레시피북이 다듬어지는 동안 몰래 쪽지가 끼워짐. 공급업체도 모름", "While the recipe book is being refined, a note is secretly slipped in — even the supplier does not know"),
         "caption": ("다듬는 틈에 몰래 쪽지가 끼워져요.", "While it is being refined, a note slips in."),
         "small": ("완성되면 다시 잠기고, 안은 보이지 않아요.", "Once finished, it locks again — no one can see inside.")},
        {"svg": P3, "hero": True, "alt": ("쪽지를 끼우는 사람, 공급업체, 주방장, 검사관이 각자 레시피북을 들고 있는 네 장면", "Four scenes: someone slipping in a note, the supplier, the chef, and an inspector, each holding a recipe book"),
         "caption": ("트로이목마 모델은 몰래 백도어를 심어 퍼뜨리는 것이에요.", "A trojan model means planting a hidden backdoor and sending it out."),
         "small": ("겉은 똑같이 잠긴 레시피북이에요.", "From outside, it is a recipe book locked just like any other."),
         "tricks": (4, [
             (TRUST_I, ("믿을 수 있는 공급처만 쓰기", "Use only trusted suppliers"), ("출처가 분명한 곳에서만 받아요", "accept a book only from a known source"), "calm"),
             (WAREHOUSE_I, ("출처·서명 확인하기", "Check provenance and signatures"), ("서명이 안 맞으면 바로 의심해요", "mismatched signatures are an instant red flag")),
             (INSPECT_I, ("받은 모델도 꼭 검수하기", "Inspect every model on arrival"), ("설치 전에 한 번 더 들여다봐요", "look it over once more before installing it"), "warm"),
             (ALERT_I, ("수상한 동작 패턴 감시하기", "Watch for odd behavior patterns"), ("설치 후에도 계속 지켜봐요", "keep watching even after it is installed")),
         ])},
        {"svg": P4, "alt": ("만들기, 다듬는 중 몰래 삽입, 설치의 세 단계가 화살표로 이어짐", "Three stages connected by arrows: build, secretly insert while refining, and install"),
         "caption": ("몇 단계를 거치든, 한 번 심기면 그대로 퍼져요.", "However many steps it passes through, once planted it spreads unchanged."),
         "small": ("만들기 → 몰래 삽입 → 설치, 세 걸음이에요.", "Build, secretly insert, install — three steps.")},
        {"svg": P5, "alt": ("왼쪽: 검사관이 서명과 출처를 확인함. 오른쪽: 레시피북 전체를 바꿔야 백도어가 없어짐", "Left: the inspector checks signatures and provenance. Right: only swapping the whole recipe book removes the backdoor"),
         "caption": ("찾기 어렵고, 모델 자체를 바꿔야 없어져요.", "It is hard to find, and only replacing the model removes it."),
         "small": ("심는 과정이 트로이목마 모델, 심긴 결과가 백도어예요.", "Planting it is the trojan model story — the planted result is the backdoor.")},
    ],
    "summary": (("<b>트로이목마 모델</b> = 레시피북을 다듬는 틈에 몰래 <b>백도어를 심어</b> 퍼뜨리는 것.",
                 "<b>A Trojan Model</b> = planting a <b>backdoor</b> while the recipe book is being refined, then sending it out into the world."),
                ("트로이목마 모델(Trojan Model)은 공개된 모델이나 파인튜닝 서비스에 공급자·개발자·중간 단계 중 누군가가 몰래 백도어를 심어 배포하는 과정 전체를 가리켜요. 심어진 결과(백도어) 자체보다, '어떻게 심기고 어떻게 퍼지는지'에 초점을 맞춘 공급망 공격의 한 형태예요.",
                 "A trojan model refers to the whole process of someone — a provider, a developer, or someone in between — secretly planting a backdoor into a publicly released or fine-tuned model before it ships. Where a backdoor is the planted result, this is the supply-chain story of how it got planted and spread.")),
    "glossary": [
        ("트로이목마 모델", "Trojan Model", ("몰래 백도어를 심어 퍼뜨리는 과정.", "The process of secretly planting and spreading a backdoor."), ('이 세계관 전체 소개도 있어요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'There is also an intro to this whole world. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
        ("백도어", "Backdoor", ("암호 주문어가 나오면 숨겨둔 동작을 하는 것 — 심긴 결과.", "A hidden action triggered by one secret word — the planted result."), ('바로 앞 이야기예요. → <a href="backdoor-ko.html">숨겨진 암호 주문어</a>', 'The story just before this one. → <a href="backdoor-en.html">The Hidden Password Order</a>')),
        ("공급망 공격", "Supply Chain Attack", ("들어오는 재료나 도구에 미리 손을 대는 일.", "Tampering with ingredients or tools before they even arrive."), ('일반 공급망과 달리 여기서는 모델 자체가 노려져요. → <a href="supplychain-ko.html">목수의 연장통에 숨어 들어온 벌레</a>', 'Unlike a general supply chain, here the model itself is the target. → <a href="supplychain-en.html">The Bug That Hid in the Carpenter\'s Toolbox</a>')),
        ("SBOM", "SBOM", ("도구에 붙은 부품 목록표.", "The parts list attached to every tool."), ('모델에도 이런 출처 목록이 필요해요. → <a href="sbom-ko.html">도구에 붙은 부품 목록표</a>', 'A model needs a provenance list like this too. → <a href="sbom-en.html">The Parts List on Every Tool</a>')),
        ("오픈 웨이트", "Open Weights", ("머릿속 눈금을 통째로 공개한 모델.", "A model whose inner settings are released in full."), ('누구나 다듬을 수 있어서 더 위험해요. → <a href="openweights-ko.html">우리 집 앵무새 vs 빌린 앵무새</a>', 'Anyone can refine it, which raises the risk. → <a href="openweights-en.html">Our Own Parrot vs a Borrowed One</a>')),
        ("파인튜닝", "Fine-tuning", ("책을 다 읽은 뒤 받는 짧은 특훈.", "The short drill a model gets after reading everything."), ('바로 이 특훈 과정에서 많이 심겨요. → <a href="finetune-ko.html">짧은 특훈</a>', 'This drill is exactly where it often gets planted. → <a href="finetune-en.html">The Short Drill</a>')),
        ("레드팀", "Red Team", ("진짜 도둑처럼 미리 찔러보는 사람들.", "People who probe like a real thief, ahead of time."), ('받은 모델을 설치 전에 찔러봐요. → <a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>', 'They probe an incoming model before it is installed. → <a href="redteam-en.html">The Team That Plays the Real Thief</a>')),
        ("평가", "Evaluation", ("시험관이 매기는 채점표.", "The scorecard an examiner fills in."), ('받은 모델을 채점표로 미리 테스트해봐요. → <a href="evaluation-ko.html">시험관의 채점표</a>', 'An incoming model gets tested against a scorecard first. → <a href="evaluation-en.html">The Examiner\'s Scorecard</a>')),
    ],
}
