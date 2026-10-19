from _draw import *
from _world import *

# 1. 요리가 나간 뒤 — 이거 정말 이 주방에서 만든 거예요?
P1 = svg(300, sky(300)
         + person(110, 160, s=0.8, face=SMILE, **CHEF) + dish(260, 170, 0.8)
         + label(260, 230, "⟦접시가 식당 밖으로 나가요|the dish leaves the kitchen⟧", 11, "var(--muted)")
         + person(480, 150, s=0.7, face=EYES, **GUEST) + dish(480, 210, 0.6)
         + bubble(540, 60, 200, 44, "⟦이거 정말 이 주방 거예요?|is this really from this kitchen?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(650, 190, s=0.6, face=FROWN, **SNEAK) + label(650, 255, "⟦다른 데서 만들었다고 우겨요|someone else claims they made it⟧", 11, "var(--bad)")
         + label(380, 280, "⟦접시만 봐서는 어느 주방에서 나왔는지 알 수 없어요|looking at the plate alone, you can't tell which kitchen it came from⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 나간 뒤엔 다 똑같은 접시예요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + dish(180, 130, 0.9) + dish(380, 130, 0.9) + dish(580, 130, 0.9)
         + label(180, 180, "⟦이 주방이 만든 요리|made by this kitchen⟧", 10, "var(--muted)")
         + label(380, 180, "⟦베껴서 다시 담은 요리|copied and replated⟧", 10, "var(--bad)")
         + label(580, 180, "⟦전혀 다른 주방 요리|a totally different kitchen's dish⟧", 10, "var(--muted)")
         + label(380, 230, "⟦셋 다 접시에 아무 표시가 없으면 구별이 안 돼요|with no mark on any of them, there's no telling them apart⟧", 12, "var(--ink)")
         + label(380, 262, "⟦일단 식당 밖으로 나가면, 되돌려 추적할 길이 없어요|once it leaves the kitchen, there's no way to trace it back⟧", 12, "var(--ink)", cls="d"))

# 3. 워터마크 = 요리에 새긴 표식 (hero)
P3 = svg(350, sky(350)
         + person(110, 150, s=0.8, face=EYES, **CHEF) + dish(250, 180, 0.9) + stamp(250, 160, 0.5)
         + label(250, 240, "⟦요리 안에 작은 표식을 새겨요 — 눈엔 안 보여요|a tiny mark baked into the dish — invisible to the eye⟧", 11, "var(--ink)")
         + '<path d="M300 180 L500 180" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>'
         + dish(560, 180, 0.9) + person(560, 240, s=0.55, face=EYES, **INSPECTOR)
         + badge(620, 150, 0.6) + stamp(560, 160, 0.5, color="var(--accent)")
         + label(560, 300, "⟦나중에도 전용 도구로 표식을 확인할 수 있어요|later, a special tool can still reveal the mark⟧", 11, "var(--ink)")
         + label(380, 25, "⟦워터마크 = 요리에 새겨 넣는, 나중에도 확인할 수 있는 표식|a watermark = a mark baked into the dish, checkable even later⟧", 14, "var(--ink)", cls="d")
         + label(380, 335, "⟦종이 설명표가 아니라, 요리 그 자체에 남겨요|not a paper label — it's left in the dish itself⟧", 12, "var(--muted)"))

# 4. 새겨지는 순서
P4 = svg(320, sky(320)
         + person(80, 150, s=0.7, face=SMILE, **CHEF) + dish(80, 220, 0.6) + label(80, 270, "⟦① 요리를 만들어요|① the dish is made⟧", 11, "var(--muted)")
         + '<path d="M140 220 L220 220" stroke="var(--muted)" stroke-width="3"/><path d="M212 213 l8 7 l-8 7" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + dish(280, 180, 0.6) + stamp(280, 165, 0.35) + label(280, 270, "⟦② 표식을 새겨요|② the mark is baked in⟧", 11, "var(--muted)")
         + '<path d="M340 220 L420 220" stroke="var(--muted)" stroke-width="3"/><path d="M412 213 l8 7 l-8 7" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(480, 150, s=0.65, face=SMILE, **GUEST) + dish(480, 220, 0.6) + label(480, 270, "⟦③ 손님에게 나가요|③ it's served to a guest⟧", 11, "var(--muted)")
         + '<path d="M540 220 L620 220" stroke="var(--muted)" stroke-width="3"/><path d="M612 213 l8 7 l-8 7" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(680, 150, s=0.65, face=EYES, **INSPECTOR) + stamp(680, 220, 0.4, color="var(--accent)") + label(680, 270, "⟦④ 나중에 확인해요|④ checked later⟧", 11, "var(--muted)"))

# 5. 모델카드와의 차이, 그리고 한계
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + dish(190, 120, 0.85) + stamp(190, 105, 0.45)
         + label(190, 200, "⟦서빙된 뒤에도 요리 안에 남아요|stays inside the dish, even after it's served⟧", 11, "var(--ink)")
         + label(190, 240, "⟦모델카드는 서빙 전 설명표, 워터마크는 서빙 뒤 표식|the model card is before serving — the watermark is after⟧", 11, "var(--ink)", cls="d")
         + dish(570, 130, 0.85) + '<path d="M548 108 L592 152 M592 108 L548 152" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(570, 200, "⟦아주 많이 고쳐 쓰면 표식이 지워질 수 있어요|rework it heavily enough and the mark can fade⟧", 11, "var(--bad)")
         + label(380, 280, "⟦표식은 완벽하지 않아요 — 그래도 아예 없는 것보단 추적에 도움이 돼요|no mark is perfect — but having one still helps tracing far more than having none⟧", 12, "var(--ink)", cls="d"))

BAKE_I = icon('<ellipse cx="32" cy="42" rx="22" ry="7" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="32" r="10" fill="var(--accent)"/><path d="M24 14 l6 6 l12 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
HIDE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4" stroke-dasharray="4 4"/><circle cx="32" cy="32" r="6" fill="var(--accent)"/>')
TOOL_I = icon('<rect x="24" y="8" width="16" height="36" rx="6" fill="var(--accent)"/><circle cx="32" cy="50" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/>')
FADE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4" stroke-dasharray="3 6"/><path d="M20 20 L44 44" stroke="var(--bad)" stroke-width="4"/>')

PAGE = {
    "slug": "watermark", "order": 25,
    "title": ("요리에 새긴 표식", "The Mark Baked Into the Dish"),
    "h1": ("<em>워터마크</em>가 뭐예요?", "What is a <em>Watermark</em>?"),
    "sub": ("워터마크를, 요리에 눈에 안 보이게 새겨 넣어 나중에도 확인할 수 있는 표식 이야기로 풀어봤어요.",
            "Watermarks, told as a story about an invisible mark baked into a dish so it can still be checked later."),
    "panels": [
        {"svg": P1, "alt": ("접시가 식당 밖으로 나간 뒤, 손님이 이 주방 거냐고 묻고, 다른 사람은 자기가 만들었다고 우김", "After a plate leaves the kitchen, a guest asks if it's really from this kitchen, while someone else claims they made it"),
         "caption": ("접시만 봐서는 어느 주방에서 나왔는지 알 수 없어요.", "Looking at the plate alone, you can't tell which kitchen it came from."),
         "small": ("일단 식당 문을 나서면, 누가 만들었는지 증명할 방법이 없어요.", "Once it's out the door, there's no way to prove who made it.")},
        {"svg": P2, "alt": ("겉보기엔 똑같은 접시 세 개 — 원본, 베껴서 다시 담은 것, 전혀 다른 주방의 요리 — 아무 표시도 없음", "Three identical-looking plates — the original, a copied replating, and a totally different kitchen's dish — with no mark on any of them"),
         "caption": ("나간 뒤엔 다 똑같은 접시예요.", "Once served, they all look like the exact same plate."),
         "small": ("아무 표시가 없으면, 베낀 건지 원본인지 구별이 안 돼요.", "With no mark, there's no telling the copy from the original.")},
        {"svg": P3, "hero": True, "alt": ("주방장이 요리를 만들며 눈에 안 보이는 표식을 새겨 넣음. 나중에 검사관이 전용 도구로 그 표식을 확인함", "The chef bakes an invisible mark into the dish while making it; later an inspector uses a special tool to reveal that mark"),
         "caption": ("워터마크는 요리에 새겨 넣는, 나중에도 확인할 수 있는 표식이에요.", "A watermark is a mark baked into the dish, checkable even later."),
         "small": ("종이 설명표가 아니라, 요리 그 자체에 남겨요.", "Not a paper label — it's left in the dish itself."),
         "tricks": (4, [
             (BAKE_I, ("만들 때 바로 새겨요", "Baked in while cooking"), ("나중에 덧붙이는 게 아니에요", "not something added on afterward"), "calm"),
             (HIDE_I, ("눈에는 안 보여요", "Invisible to the eye"), ("맛도, 모양도 안 바뀌어요", "no change in taste or look"), "calm"),
             (TOOL_I, ("전용 도구로 확인해요", "Revealed with a special tool"), ("아무나 바로 못 봐요", "not something anyone can just glance and see"), "warm"),
             (FADE_I, ("완벽하진 않아요", "Not foolproof"), ("아주 심하게 고치면 지워져요", "heavy enough rework can erase it"), "warm"),
         ])},
        {"svg": P4, "alt": ("네 단계: 요리를 만들고, 표식을 새기고, 손님에게 나가고, 나중에 검사관이 확인함", "Four steps: the dish is made, the mark is baked in, it's served to a guest, and later an inspector checks it"),
         "caption": ("요리를 만들고, 표식을 새기고, 나간 뒤, 나중에 확인해요.", "Make the dish, bake in the mark, serve it, and check it later."),
         "small": ("확인은 서빙되고 한참 지난 뒤에도 할 수 있어요.", "The check can happen long after the dish has already been served.")},
        {"svg": P5, "alt": ("왼쪽 초록: 서빙된 뒤에도 표식이 요리 안에 남음. 오른쪽 빨강: 접시를 아주 많이 고쳐 쓰면 표식에 금이 가며 지워짐", "Left, green: the mark stays inside the dish even after serving. Right, red: heavily reworking the plate cracks and erases the mark"),
         "caption": ("모델카드는 서빙 전 설명표, 워터마크는 서빙 뒤 표식이에요.", "The model card is the label before serving; the watermark is the mark after."),
         "small": ('<a href="modelcard-ko.html">요리 설명표</a>는 주문 전에 붙이는 안내문이고, 워터마크는 다 만들어진 결과물에 남기는 사후 표식이에요. '
                   '둘 다 완벽하진 않지만, 주방장이 손님 말을 믿고 따르는 본능 때문에 생기는 틈을, 서로 다른 시점에서 메워 줘요.',
                   'A <a href="modelcard-en.html">model card</a> is a notice posted before ordering; a watermark is a mark left on the finished output, after the fact. '
                   'Neither is perfect, but each closes — at a different point in time — the gap that opens because the chef trusts the guest\'s words by instinct.')},
    ],
    "summary": (("<b>워터마크</b> = 요리에 <b>눈에 안 보이게 새기는 표식</b>. 나중에 전용 도구로 확인하면, 이게 이 주방에서 나온 요리인지 알 수 있어요.",
                 "<b>A watermark</b> = <b>an invisible mark baked into the dish</b>. Checked later with a special tool, it reveals whether a dish really came from this kitchen."),
                ("워터마크(Watermarking)는 AI가 만든 결과물(텍스트·이미지·음성)에, 사람은 알아채기 어렵지만 전용 탐지기로는 확인할 수 있는 표식을 심는 기법이에요. 생성 시점에 통계적 패턴(예: 특정 토큰 선택 편향)이나 신호를 끼워 넣고, 나중에 그 패턴을 검사해 'AI가 생성했는지'를 판별해요. 모델카드처럼 배포 전에 쓰는 설명서가 아니라, 이미 나온 결과물에 사후적으로 적용하는 표식이라는 점이 다르고, 결과물을 크게 변형하면 표식이 깨질 수 있다는 한계도 있어요.",
                 "Watermarking is a technique for embedding a mark in AI-generated output (text, images, audio) that's hard for a person to notice but can be confirmed by a dedicated detector. It's inserted at generation time as a statistical pattern (e.g., a bias in token selection) or signal, and later checking for that pattern reveals whether the content was AI-generated. Unlike a model card, which is written before deployment, a watermark is applied after the fact to output that already exists — and it has the limitation that heavy enough transformation of the output can break the mark.")),
    "glossary": [
        ("워터마크", "Watermark", ("요리에 새긴 눈에 안 보이는 표식.", "An invisible mark baked into the dish."), ("전용 도구로만 확인할 수 있어요.", "Only a special tool can reveal it.")),
        ("요리 설명표 비교", "vs. the dish's label", ("설명표는 서빙 전, 워터마크는 서빙 뒤.", "The label comes before serving — the watermark after."), ('서로 다른 시점에 쓰는 짝이에요. → <a href="modelcard-ko.html">요리 설명표</a>', 'Companions at different points in time. → <a href="modelcard-en.html">the dish\'s label</a>')),
        ("탐지기", "Detector", ("표식을 읽어내는 전용 도구.", "The special tool that reads the mark."), ("검사관만 쓰는 도구예요 — 아무나 맨눈으로는 못 봐요.", "Used only by inspectors — no one can see it with the naked eye.")),
        ("출처 인증", "Provenance", ("이 요리가 정말 이 주방에서 나왔다는 증거.", "Proof that this dish really came from this kitchen."), ("워터마크가 뒷받침하는 증거예요.", "This is what the watermark is meant to back up.")),
        ("합성 결과물", "Synthetic content", ("사람이 아니라 주방장이 통째로 만든 요리.", "A dish made entirely by the chef, not a person."), ('특히 이런 요리에서 표식이 더 중요해요. → <a href="synthetic-ko.html">앵무새 마을의 합성 콩</a>', 'The mark matters most for this kind of dish. → <a href="synthetic-en.html">the parrot world\'s synthetic beans</a>')),
        ("고쳐 쓰기 공격", "Scrubbing attack", ("표식을 지우려고 일부러 많이 고쳐 쓰는 것.", "Deliberately heavy rework meant to erase the mark."), ("표식의 가장 큰 한계예요.", "This is the watermark's biggest limitation.")),
        ("규제 준수", "Compliance", ("정부나 업계가 표식을 의무로 요구하는 경우.", "A rule that makes marking mandatory."), ('AI 생성물 표시를 법으로 요구하는 곳도 있어요. → <a href="compliance-ko.html">보안 마을의 규제 준수</a>', 'Some jurisdictions now require labeling AI output by law. → <a href="compliance-en.html">the security world\'s compliance</a>')),
        ("감사 로그", "Audit log", ("언제 어떤 요리가 새겨졌는지 적어 두는 장부.", "The ledger of when each dish's mark was baked in."), ("표식 자체가 지워져도, 장부가 남아 있으면 되짚을 수 있어요.", "Even if a mark fades, the ledger can still help trace it back.")),
    ],
}
