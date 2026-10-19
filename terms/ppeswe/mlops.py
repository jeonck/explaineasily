from _draw import *
from _world import *


def proofmachine(x, y, s=1.0, ok=True):
    """자동 교정 기계 — 원고를 훑어보고 틀린 곳에 표시해 주는 장치."""
    glow = "var(--good)" if ok else "var(--bad)"
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-26" width="60" height="52" rx="8" fill="#4A5A72"/>'
            f'<rect x="-22" y="-18" width="44" height="26" rx="3" fill="#D8D2C2"/>'
            f'<circle cx="-10" cy="-5" r="4" fill="{glow}"/><circle cx="10" cy="-5" r="4" fill="{glow}"/>'
            f'<rect x="-14" y="14" width="28" height="8" rx="4" fill="{glow}"/></g>')


# 1. 자동 교정 기계를 한 번 만들고 그 뒤로 손대지 않았어요
P1 = svg(300, sky(300)
         + proofmachine(380, 140, 1.1, ok=True)
         + manuscript(200, 150, 0.6, marks=2) + manuscript(560, 150, 0.6, marks=2)
         + label(380, 30, "⟦작년에 만든 교정 기계, 그대로 두었어요|the proofing machine built last year, left untouched since⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦요즘 말투는 자꾸 놓쳐요 — 세상이 바뀌었거든요|it keeps missing today's expressions — the world moved on⟧", 12, "var(--bad)"))

# 2. 코드와 다르게, 예시 더미(데이터)로 배워서 어려워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + proofmachine(380, 130, 1.1, ok=False)
         + manuscript(200, 230, 0.6) + manuscript(300, 230, 0.6) + manuscript(400, 230, 0.6) + manuscript(500, 230, 0.6) + manuscript(600, 230, 0.6)
         + label(380, 30, "⟦규칙을 고쳐 쓴 게 아니라, 예시를 보고 스스로 배웠어요|it didn't follow rewritten rules — it learned from piles of examples⟧", 13, "var(--ink)", cls="d")
         + label(380, 290, "⟦그래서 코드 고치듯 한 줄만 바꿀 수가 없어요|so you can't just fix one line like ordinary code⟧", 12, "var(--bad)"))

# 3. MLOps = 교정 기계를 계속 돌보는 일 (hero)
DATA_I = icon('<path d="M14 18 Q32 8 50 18 V46 Q32 56 14 46 Z" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M14 18 Q32 28 50 18" stroke="var(--accent)" stroke-width="3" fill="none"/>')
TRAIN_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 20 V32 L42 38" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M50 18 A22 22 0 0 1 54 32" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
WATCH_I = icon('<path d="M8 40 Q32 10 56 40" stroke="var(--accent)" stroke-width="4" fill="none"/><circle cx="32" cy="34" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="34" r="3" fill="var(--accent)"/>')
REVERT_I = icon('<path d="M46 20 A20 20 0 1 0 50 44" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M46 10 V22 H34" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦MLOps = 교정 기계를 계속 돌보는 일|MLOps = continuously caring for the proofing machine⟧", 14, "var(--ink)", cls="d")
         + person(130, 200, s=0.8, face=EYES, **PROOFER) + manuscript(222, 210, 0.55)
         + proofmachine(400, 190, 1.3, ok=True)
         + bookshelf(560, 170, 0.9, n=3, hl=2)
         + label(380, 320, "⟦새 원고를 계속 넣어 가르치고, 틀리면 바로 알아채고, 예전 판으로 되돌릴 수도 있어요|keep teaching it new manuscripts, catch mistakes fast, and roll back to an older version if needed⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "mlops", "order": 16,
    "title": ("자동 교정 기계 돌보기", "Caring for the Automatic Proofing Machine"),
    "h1": ("<em>MLOps/ModelOps</em>가 뭐예요?", "What is <em>MLOps/ModelOps</em>?"),
    "sub": ("MLOps를, 한 번 만들고 끝나는 게 아니라 계속 가르치고 지켜봐야 하는 자동 교정 기계 이야기로 풀어봤어요.",
            "MLOps, told as a story about an automatic proofing machine that must be kept teaching and watching, not just built once and forgotten."),
    "panels": [
        {"svg": P1, "alt": ("자동 교정 기계가 작년 모습 그대로 서 있고, 양옆 원고에는 빨간 교정 표시가 잔뜩", "An automatic proofing machine stands unchanged since last year, with manuscripts on both sides full of red marks it missed"),
         "caption": ("작년에 만든 교정 기계, 그대로 두었어요.", "The proofing machine built last year has been left untouched."),
         "small": ("요즘 말투는 자꾸 놓쳐요 — 세상이 바뀌었거든요.", "It keeps missing today's expressions — the world moved on.")},
        {"svg": P2, "alt": ("교정 기계 아래 원고 다섯 뭉치가 늘어서 있음 — 코드가 아니라 예시 더미로 배운다는 뜻", "Five stacks of manuscripts line up beneath the machine — it learned from piles of examples, not written code"),
         "caption": ("코드와 다르게, 예시 더미(데이터)로 배워서 어려워요.", "Unlike code, it learned from piles of examples — and that makes it harder to fix."),
         "small": ("그래서 코드 고치듯 한 줄만 바꿀 수가 없어요.", "So you can't just fix one line like ordinary code.")},
        {"svg": P3, "hero": True, "alt": ("교정자가 새 원고를 기계에 넣고, 기계 옆엔 버전별 보관 서가가 있음", "A proofreader feeds a new manuscript into the machine, beside a shelf storing its past versions"),
         "caption": ("MLOps는 교정 기계를 계속 돌보는 일이에요.", "MLOps is continuously caring for the proofing machine."),
         "small": ("새 원고를 계속 넣어 가르치고, 틀리면 바로 알아채고, 예전 판으로 되돌릴 수도 있어요.", "Keep teaching it, catch mistakes fast, and roll back to an older version if needed."),
         "tricks": (4, [
             (DATA_I, ("새 예시 모으기", "Gather new examples"), ("최근 원고를 계속 모아요", "keep collecting recent manuscripts"), "calm"),
             (TRAIN_I, ("다시 가르치기", "Retrain it"), ("새 예시로 기계를 다시 훈련해요", "retrain the machine on the new examples")),
             (WATCH_I, ("실수 지켜보기", "Watch for mistakes"), ("정확도가 떨어지면 바로 알아채요", "catch it as soon as accuracy drops")),
             (REVERT_I, ("예전 판으로 되돌리기", "Roll back a version"), ("새 판이 더 나쁘면 되돌려요", "if the new version is worse, revert"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 240, "⟦교정 기계 돌보기 순환|THE CARE LOOP⟧",
                                 ("⟦① 새 원고(데이터) 모으기|① collect new manuscripts (data)⟧",
                                  "⟦② 다시 가르치기(재훈련)|② retrain the machine⟧",
                                  "⟦③ 교정 정확도 시험하기(검증)|③ test proofing accuracy (validation)⟧",
                                  "⟦④ 새 기계로 교체하기(배포)|④ swap in the new machine (deployment)⟧",
                                  "⟦⑤ 계속 지켜보기(모니터링) → 다시 ①로|⑤ keep watching (monitoring) → back to ①⟧"), 1.0)),
         "alt": ("데이터 모으기부터 모니터링까지 다섯 단계가 돌고 도는 순환 안내판", "A guide showing five steps looping from data collection to monitoring"),
         "caption": ("이 돌봄은 한 바퀴로 끝나지 않고 계속 돌아요.", "This care isn't a one-time pass — it loops continuously."),
         "small": ("모으고, 가르치고, 시험하고, 바꾸고, 지켜보고 — 다시 처음으로 돌아가요.", "Collect, retrain, test, swap, watch — then it starts over again.")},
        {"svg": svg(300, sky(300)
                    + proofmachine(220, 150, 1.0, ok=True) + person(340, 150, s=0.75, face=EYES, **PROOFER)
                    + bubble(272, 70, 180, 40, "⟦애매한 건 그래도 제가 봐요|the tricky ones still come to me⟧", 11, "var(--panel)", "var(--line)", "bottom")
                    + label(380, 30, "⟦기계가 똑똑해져도, 끝은 아니에요|smarter machine — but still not the end of the story⟧", 13, "var(--bad)", cls="d")
                    + label(380, 275, "⟦우리 교정 기계를 훈련·운영하는 일이에요 — 빌려 쓰는 큰 앵무새를 돌보는 일과는 달라요|this is about training and running our own machine — different from caring for a borrowed big parrot⟧", 11, "var(--muted)")),
         "alt": ("교정 기계 옆에서 교정자가 '애매한 건 그래도 제가 봐요'라고 말함", "Beside the proofing machine, the proofreader says the tricky cases still come to them"),
         "caption": ("기계가 똑똑해져도, 끝은 아니에요.", "A smarter machine isn't the end of the story."),
         "small": ('애매한 표현은 결국 교정자가 확인해요. 빌려 쓰는 큰 앵무새를 돌보는 일은 → <a href="llmops-ko.html">앵무새 돌보기</a> 쪽 이야기예요.',
                   'The tricky calls still go to a human proofreader. Caring for a borrowed big parrot instead is a different story → <a href="llmops-en.html">caring for the parrot</a>.')},
    ],
    "summary": (("<b>MLOps/ModelOps</b> = 자동 교정 기계를 <b>한 번 만들고 끝내지 않고</b>, 새 원고로 <b>계속 다시 가르치고</b>, 실수를 <b>지켜보며 필요하면 되돌리는</b> 돌봄 과정.",
                 "<b>MLOps/ModelOps</b> = not building the proofing machine once and walking away, but <b>continuously retraining</b> it on new manuscripts, <b>watching for mistakes</b>, and <b>rolling back</b> when needed."),
                ("MLOps(Machine Learning Operations)는 머신러닝 모델의 데이터 수집·학습·검증·배포·모니터링을 하나의 반복 파이프라인으로 관리하는 방법론이에요. ModelOps는 여기서 한발 더 나아가 운영 중인 여러 모델의 거버넌스·감사까지 포괄해요. 코드가 아니라 데이터로 동작이 바뀌는 모델의 특성상, 일반 CI/CD보다 재학습·드리프트 감지가 핵심이에요.",
                 "MLOps (Machine Learning Operations) manages a machine learning model's data collection, training, validation, deployment, and monitoring as one repeating pipeline. ModelOps goes further, covering governance and auditing across many models in production. Because a model's behavior shifts with data rather than code, retraining and drift detection matter more here than in ordinary CI/CD.")),
    "glossary": [
        ("MLOps/ModelOps", "MLOps/ModelOps", ("교정 기계를 계속 돌보는 과정.", "The process of continuously caring for the machine."), ("만들고 끝이 아니라, 운영까지 포함해요.", "Not just building it — running it is part of the job too.")),
        ("데이터 파이프라인", "Data Pipeline", ("새 원고를 모아 들이는 길.", "The path that brings in new manuscripts."), ("학습용 예시가 계속 흘러 들어와요.", "A steady stream of training examples.")),
        ("재학습(Retraining)", "Retraining", ("새 원고로 다시 가르치는 일.", "Teaching the machine again with new material."), ("세상이 바뀌면 기계도 다시 배워야 해요.", "When the world changes, the machine has to learn again.")),
        ("모델 레지스트리", "Model Registry", ("기계를 버전별로 보관하는 서가.", "The shelf that stores each version of the machine."), ('형상관리와 같은 생각이에요 → <a href="scmshelf-ko.html">원고를 지키는 보관 서가</a>.', 'Same idea as configuration management → <a href="scmshelf-en.html">the shelf that protects the manuscript</a>.')),
        ("드리프트(Drift)", "Drift", ("세상이 바뀌어 기계가 자꾸 틀리는 것.", "The machine starting to miss things as the world changes."), ("데이터가 변하면 정확도가 조용히 떨어져요.", "As the data shifts, accuracy quietly slips.")),
        ("A/B 테스트", "A/B Testing", ("새 기계와 옛 기계를 나란히 비교하는 것.", "Running the new machine and the old one side by side."), ("더 나은 쪽만 남겨요.", "Only the better one stays.")),
        ("모델 롤백", "Model Rollback", ("새 기계가 별로면 예전 판으로.", "If the new machine disappoints, go back."), ('놀이공원 세계의 되돌리기와 같아요 → <a href="rollback-ko.html">기구를 예전 설정으로</a>.', 'Same idea as the rewind in the theme-park world → <a href="rollback-en.html">resetting a ride to its old setup</a>.')),
        ("모니터링", "Monitoring", ("기계의 실수를 계속 지켜보는 일.", "Keeping an eye on the machine's mistakes."), ("정확도가 떨어지면 가장 먼저 알아채는 장치예요.", "It's the first thing to notice when accuracy drops.")),
    ],
}
