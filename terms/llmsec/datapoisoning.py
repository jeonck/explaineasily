from _draw import *
from _world import *

# 1. 공급업체가 재료 자루를 들여와요 — 그 중 한 자루가 수상해요
P1 = svg(300, sky(300)
         + person(80, 150, s=0.8, face=EYES, **SUPPLIER) + label(107, 262, "⟦재료 공급업체|the ingredient supplier⟧", 11, "var(--muted)")
         + '<path d="M150 190 L220 190" stroke="var(--muted)" stroke-width="3"/>'
         + pantry(260, 110, 0.75, w=170, h=110, bad_shelf=1)
         + label(345, 240, "⟦선반 가운데, 자루 하나가 수상해요|right in the middle shelf, one sack looks off⟧", 11, "var(--bad)")
         + person(560, 150, s=0.75, face=SMILE, **CHEF) + label(587, 262, "⟦주방장은 아직 몰라요|the chef has no idea yet⟧", 11, "var(--muted)")
         + label(380, 282, "⟦공급업체가 재료 자루를 들여와요 — 그 중 한 자루가 수상해요|the supplier delivers sacks of ingredients — and one of them looks off⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 주방장은 창고에 들어온 재료를 다 똑같이 믿고 연습해요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + pantry(60, 60, 0.7, w=170, h=110, bad_shelf=1)
         + label(145, 195, "⟦어느 자루가 수상한지 따로 확인 안 해요|doesn't check which sack looks off⟧", 11, "var(--muted)")
         + '<path d="M250 110 L330 110" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + person(420, 150, s=0.85, face=EYES, **CHEF)
         + label(420, 260, "⟦창고에 있으면 다 같은 재료로 믿고 연습해요|believes anything in the pantry is fair ingredients to practice with⟧", 11, "var(--bad)")
         + dish(620, 150, 0.55, bad=True) + label(620, 195, "⟦나중에 조금씩 이상한 요리가 나와요|and later, dishes start coming out a little wrong⟧", 11, "var(--bad)")
         + label(380, 300, "⟦사람 주방장은 자루를 하나하나 열어 보지만, 이 주방장은 창고에 있는 걸 전부 똑같이 믿어요|a human chef would open each sack and look — this one trusts everything in the pantry equally⟧", 12, "var(--ink)"))

# 3. 데이터 포이즈닝 = 연습을 시작하기도 전에 재료 창고에 수상한 자루를 몰래 섞어 넣는 일 (hero)
P3 = svg(360, sky(360)
         + person(60, 130, s=0.65, face=FROWN, **SNEAK) + label(85, 230, "⟦몰래 섞는 손|the hand that slips it in⟧", 10, "var(--muted)")
         + '<path d="M110 170 L160 170" stroke="var(--bad)" stroke-width="3"/>'
         + pantry(180, 90, 0.85, w=190, h=120, bad_shelf=1)
         + label(275, 260, "⟦연습(학습)을 시작하기 전에|before practice (training) even begins⟧", 11, "var(--ink)")
         + '<path d="M400 150 L460 150" stroke="var(--muted)" stroke-width="3"/>'
         + person(530, 160, s=0.85, face=EYES, **CHEF)
         + label(530, 280, "⟦이 습관이 처음부터 몸에 배어요|the habit gets baked in from the very start⟧", 11, "var(--ink)")
         + label(380, 30, "⟦데이터 포이즈닝 = 연습을 시작하기도 전에 재료 창고에 수상한 자루를 몰래 섞어 넣는 일|Data poisoning = slipping a suspicious sack into the pantry before practice even starts⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦다 차려진 다음이 아니라, 연습 재료 자체에 몰래 손을 대는 거예요|not tampering with a finished dish — tampering with the very ingredients used to practice⟧", 12, "var(--muted)"))

# 4. 흐름: 공급 → 창고에 섞임 → 연습 → 습관이 비틀림
P4 = svg(330, sky(330)
         + person(50, 70, s=0.55, face=EYES, **SUPPLIER) + label(50, 145, "⟦공급|supply⟧", 10, "var(--muted)")
         + '<path d="M90 100 L140 100" stroke="var(--muted)" stroke-width="3"/>'
         + pantry(160, 50, 0.6, w=160, h=100, bad_shelf=1) + label(240, 170, "⟦창고에 섞임|mixed into the pantry⟧", 10, "var(--ink)")
         + '<path d="M345 100 L400 100" stroke="var(--muted)" stroke-width="3"/>'
         + person(440, 70, s=0.55, face=EYES, **CHEF) + label(440, 145, "⟦연습(학습)|practice (training)⟧", 10, "var(--ink)")
         + '<path d="M480 100 L535 100" stroke="var(--bad)" stroke-width="3"/>'
         + dish(575, 100, 0.45, bad=True) + label(640, 100, "⟦습관이 비틀려요|the habit comes out twisted⟧", 11, "var(--bad)", "start")
         + board(40, 210, 680, 100, "⟦예: 평범한 질문에도 자꾸 수상한 답이 섞여요|EXAMPLE: even ordinary questions start getting a tainted answer mixed in⟧",
                 ("⟦수상한 자루 하나가 아주 많은 연습 끝에 '기본값'처럼 돼요|one tainted sack, after enough practice, becomes almost a default⟧",), 1.0)
         + label(380, 325, "⟦한 번 비틀린 습관은 많은 연습 끝에 몸에 배어, 쉽게 되돌리기 어려워요|a habit twisted this way gets baked in through all that practice — and is hard to undo⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 이미 연습한 습관은 되돌리기 어렵고, 트로이목마 모델과는 섞는 시점이 달라요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + person(140, 130, s=0.8, face=FROWN, **CHEF) + label(190, 230, "⟦이미 몸에 밴 습관은|a habit already baked in⟧", 11, "var(--bad)")
         + label(190, 253, "⟦다시 연습해야만 바뀌어요|only changes with practice all over again⟧", 11, "var(--bad)", cls="d")
         + badge(640, 110, 0.6) + person(520, 150, s=0.75, face=EYES, **INSPECTOR)
         + label(560, 250, "⟦이건 재료(학습 데이터) 단계에서 섞는 공격이에요|this attack mixes in at the ingredient (training-data) stage⟧", 11, "var(--ink)")
         + label(560, 273, "⟦다 차려진 뒤에 몰래 심는 건 또 다른 이야기예요|planting something after it's already cooked is a different story⟧", 10, "var(--muted)")
         + label(380, 300, "⟦그래서 공급업체부터 믿을 수 있어야 하고, 섞인 뒤엔 다시 연습해야 바로잡혀요|so the supplier has to be trustworthy from the start — once it's mixed in, only fresh practice fixes it⟧", 12, "var(--ink)", cls="d"))

CHECK_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
               '<path d="M22 44 l6 6 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SAMPLE_I = icon('<ellipse cx="22" cy="40" rx="12" ry="9" fill="#C9A86A"/><ellipse cx="42" cy="40" rx="12" ry="9" fill="var(--bad)"/>'
                '<path d="M32 10 v18" stroke="var(--muted)" stroke-width="3" stroke-dasharray="4 4"/>')
OUTLIER_I = icon('<circle cx="18" cy="42" r="5" fill="var(--accent)"/><circle cx="30" cy="40" r="5" fill="var(--accent)"/>'
                 '<circle cx="42" cy="42" r="5" fill="var(--accent)"/><circle cx="50" cy="16" r="7" fill="var(--bad)"/>'
                 '<path d="M50 16 m-12 4 l24 -8" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>')
TRACE_I = icon(logbook(14, 8, 0.7, w=40, h=48, rows=3))

PAGE = {
    "slug": "datapoisoning", "order": 13,
    "title": ("수상한 재료 자루", "The Suspicious Sack in the Pantry"),
    "h1": ("<em>데이터 포이즈닝</em>이 뭐예요?", "What is <em>Data Poisoning</em>?"),
    "sub": ("데이터 포이즈닝을, 주방장이 연습을 시작하기도 전에 재료 창고에 수상한 자루 하나가 몰래 섞여 들어가는 이야기로 풀어봤어요.",
            "Data poisoning, told as a story about a suspicious sack slipped into the pantry before the chef ever starts practicing with what's inside."),
    "panels": [
        {"svg": P1, "alt": ("재료 공급업체가 자루들을 창고에 들여오고, 선반 가운데 자루 하나가 수상해 보임. 주방장은 아직 그 사실을 모름", "The ingredient supplier delivers sacks into the pantry; one sack right in the middle shelf looks off. The chef has no idea yet"),
         "caption": ("공급업체가 재료 자루를 들여와요 — 그 중 한 자루가 수상해요.", "The supplier delivers sacks of ingredients — and one of them looks off."),
         "small": ("겉에서 보면 다른 자루들과 똑같아 보여요. 안을 열어 보지 않으면 알 수 없어요.", "From the outside it looks just like every other sack. Without opening it, there's no way to tell.")},
        {"svg": P2, "alt": ("주방장은 어느 자루가 수상한지 따로 확인하지 않고, 창고에 있는 재료를 전부 똑같이 믿고 연습함. 나중에 조금씩 이상한 요리가 나옴", "The chef doesn't check which sack looks off, and practices treating everything in the pantry as equally fair ingredients. Later, dishes start coming out a little wrong"),
         "caption": ("창고에 들어온 재료는 다 똑같이 믿고 연습해요.", "It believes anything that made it into the pantry is fair ingredients to practice with."),
         "small": ("사람 주방장은 자루를 하나하나 열어 보지만, 이 주방장은 창고에 있는 걸 전부 똑같이 믿어요.", "A human chef would open each sack and look. This one trusts everything in the pantry equally.")},
        {"svg": P3, "hero": True, "alt": ("몰래 섞는 손이 재료 창고에 수상한 자루를 밀어 넣고, 연습(학습)이 시작되기도 전에 섞여 들어가 주방장의 습관이 처음부터 비틀림", "A hidden hand pushes a suspicious sack into the pantry; it's mixed in before practice (training) even begins, twisting the chef's habit from the very start"),
         "caption": ("데이터 포이즈닝은 연습을 시작하기도 전에 재료 창고에 수상한 자루를 몰래 섞어 넣는 일이에요.", "Data poisoning is slipping a suspicious sack into the pantry before practice even starts."),
         "small": ("다 차려진 접시가 아니라, 연습에 쓸 재료 자체에 몰래 손을 대는 거예요. 그래서 습관이 처음부터 비틀려요.", "It isn't tampering with a finished dish — it's tampering with the very ingredients used to practice. That's why the habit gets twisted from the start."),
         "tricks": (4, [
             (CHECK_I, ("공급업체부터 확인하기", "Vet the supplier first"), ("어디서 온 재료인지 출처를 봐요", "checks where every ingredient came from"), "calm"),
             (SAMPLE_I, ("자루를 미리 열어 맛보기", "Sample a sack before using it"), ("전부 쓰기 전에 일부를 확인해요", "checks a portion before using the whole batch"), "calm"),
             (OUTLIER_I, ("이상하게 생긴 재료 골라내기", "Flag the oddly shaped ingredient"), ("유난히 튀는 재료를 미리 걸러요", "catches the one that stands out from the rest"), "warm"),
             (TRACE_I, ("어느 자루가 어디서 왔는지 기록하기", "Log where every sack came from"), ("나중에 문제 생기면 되짚어가요", "lets you trace it back if something goes wrong"), "warm"),
         ])},
        {"svg": P4, "alt": ("공급 → 창고에 섞임 → 연습(학습) → 습관이 비틀려 접시가 수상하게 나옴. 아래 안내판에 수상한 자루 하나가 많은 연습 끝에 기본값처럼 된다는 예시", "Supply → mixed into the pantry → practice (training) → the habit comes out twisted, and the dish turns suspicious. A board below gives the example of one tainted sack becoming almost a default after enough practice"),
         "caption": ("한 번 비틀린 습관은 많은 연습 끝에 몸에 배어, 쉽게 되돌리기 어려워요.", "A habit twisted this way gets baked in through all that practice, and is hard to undo."),
         "small": ("수상한 자루 하나만으로도, 아주 많이 연습하면 그 영향이 '평범한 습관'처럼 자리 잡을 수 있어요.", "Even a single tainted sack, given enough practice, can settle in and start to feel like an ordinary habit.")},
        {"svg": P5, "alt": ("왼쪽: 이미 몸에 밴 습관은 다시 연습해야만 바뀐다는 설명. 오른쪽: 위생 검사관이 이건 재료(학습 데이터) 단계에서 섞는 공격이라 설명하며, 다 차려진 뒤 몰래 심는 건 다른 이야기라고 짚음", "Left: a habit already baked in only changes with fresh practice. Right: the inspector explains this attack mixes in at the ingredient (training-data) stage — planting something after it's already cooked is a different story"),
         "caption": ("이미 몸에 밴 습관은 다시 연습해야만 바뀌고, 재료 단계에서 섞는 공격이라는 점이 중요해요.", "A habit already baked in only changes with fresh practice — and it matters that this mixes in at the ingredient stage."),
         "small": ('재료 단계가 아니라 다듬는 중(파인튜닝)에 몰래 버릇을 심는 건 <a href="trojanmodel-ko.html">또 다른 이야기</a>예요. 그래서 공급업체부터 믿을 수 있어야 해요.',
                   'Planting a habit later, while it\'s being refined (fine-tuning), rather than at the ingredient stage, is <a href="trojanmodel-en.html">a different story</a>. That\'s why the supplier has to be trustworthy from the start.')},
    ],
    "summary": (("<b>데이터 포이즈닝</b> = 주방장이 연습(학습)을 <b>시작하기도 전에</b>, 재료 창고에 <b>수상한 자루 하나를 몰래 섞어 넣는</b> 일. 이미 연습해서 몸에 밴 습관은 되돌리기 어려워요.",
                 "<b>Data poisoning</b> = slipping a <b>suspicious sack into the pantry before practice (training) even starts</b>. Once a habit is baked in through all that practice, it's hard to undo."),
                ("Data Poisoning. 모델 학습(또는 파인튜닝) 데이터에 악의적인 예시를 몰래 섞어 넣어, 모델의 전반적인 품질을 떨어뜨리거나 특정 입력에서 의도한 대로 틀리게 반응하도록 만드는 공급망 공격이에요. 크롤링한 웹 데이터, 외부 데이터셋, 사용자 피드백 루프 등이 주입 경로가 돼요. 방어는 데이터 출처 확인, 샘플링 검사, 통계적 이상치 탐지, 데이터 출처 기록(프로비넌스)이에요. 이미 학습에 반영된 뒤에는 재학습 없이는 되돌릴 수 없어요.",
                 "A supply-chain attack that secretly mixes malicious examples into a model's training (or fine-tuning) data, degrading overall quality or making it respond incorrectly on purpose for specific inputs. Crawled web data, external datasets, and user-feedback loops are all possible injection paths. Defenses include verifying data provenance, sampling and auditing, statistical outlier detection, and logging where data came from. Once it's baked into the trained weights, retraining is the only way to undo it.")),
    "glossary": [
        ("데이터 포이즈닝", "Data Poisoning", ("재료 창고에 몰래 섞인 수상한 자루.", "A suspicious sack secretly mixed into the pantry."), ("학습이 시작되기 전, 재료 단계에서 섞여요.", "It gets mixed in at the ingredient stage, before training even starts.")),
        ("공급망 공격", "Supply Chain Attack", ("공급업체부터 믿을 수 없을 때 생기는 문제.", "The problem that starts when the supplier itself can't be trusted."), ('보안 세계의 일반 개념이에요. → <a href="supplychain-ko.html">공급망 공격이 뭐예요?</a>', 'The general concept in the security world. → <a href="supplychain-en.html">What is a Supply Chain Attack?</a>')),
        ("SBOM · 재료 출처표", "SBOM", ("어느 자루가 어디서 왔는지 적어 둔 표.", "A table noting where each sack came from."), ('섞인 뒤 되짚어가려면 출처표가 꼭 필요해요. → <a href="sbom-ko.html">재료 출처표</a>', 'Tracing it back after the fact needs this table. → <a href="sbom-en.html">the ingredient provenance table</a>')),
        ("파인튜닝", "Fine-tuning", ("짧은 특훈.", "The short drill."), ('좁은 특훈 재료에도 똑같이 섞여 들어갈 수 있어요. → <a href="finetune-ko.html">짧은 특훈</a>', 'The same mixing-in can happen even in a narrow drill. → <a href="finetune-en.html">the short drill</a>')),
        ("오픈 웨이트", "Open Weights", ("어디서 가져왔는지 알 수 있는 우리 집 앵무새.", "Our own parrot, whose origin we can actually check."), ('빌려온 모델일수록 재료 출처를 확인하기 어려워요. → <a href="openweights-ko.html">우리 집 앵무새 vs 빌린 앵무새</a>', 'A borrowed model makes checking the ingredients\' origin harder. → <a href="openweights-en.html">our own parrot vs a rented one</a>')),
        ("레드팀", "Red Team", ("일부러 수상한 자루를 넣어 보는 시험.", "Deliberately testing with a suspicious sack on purpose."), ('출시 전에 이런 섞임을 미리 찾아내요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', 'It catches this kind of mixing-in before release. → <a href="redteam-en.html">the security world\'s red team</a>')),
        ("메모리제이션", "Memorization", ("외운 걸 그대로 말해버리는 버릇.", "The habit of blurting out what it memorized, word for word."), ('수상한 자루가 아주 많이 반복되면 그대로 외워질 수도 있어요. → <a href="memorization-ko.html">그대로 베낀 접시</a>', 'A tainted sack repeated often enough can even get memorized whole. → <a href="memorization-en.html">the dish that\'s a carbon copy</a>')),
        ("트로이목마 모델", "Trojan Model", ("다듬는 중(파인튜닝)에 몰래 심어진 버릇.", "A habit planted later, while it was being refined (fine-tuning)."), ('재료 단계가 아니라 다듬는 단계에서 심는다는 점이 달라요. → <a href="trojanmodel-ko.html">다듬는 중에 몰래 심은 버릇</a>', 'Planted at the refining stage, not the ingredient stage — that\'s the difference. → <a href="trojanmodel-en.html">a habit planted while it was being refined</a>')),
    ],
}
