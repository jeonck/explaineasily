from _draw import *
from _world import *

# 1. 신입 조작원에게 정답표가 없어요
P1 = svg(300, sky(300)
         + person(170, 170, s=0.8, face=SWEAT + EYES, **OPERATOR)
         + conveyor(60, 250, 220, 1.0) + produce(100, 230, 0.7) + produce(160, 230, 0.7)
         + bubble(380, 80, 240, 50, "⟦이게 합격인지 불합격인지, 미리 알려주는 정답표가 없어요|no answer key tells me pass or fail ahead of time⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦훈련 교사가 미리 보여준 예제 없이 혼자 판단해야 해요|no teacher-given examples — just judge on your own⟧", 12, "var(--ink)"))

# 2. 일단 던져보고, 보너스와 벌점으로 배워요
P2 = svg(310, '<rect width="760" height="310" fill="var(--bad-soft)"/>'
         + person(170, 160, s=0.8, face=EYES, **OPERATOR) + bin_(280, 230, 0.8, "⟦이쪽?|this bin?⟧")
         + stamp2(350, 170, 0.6, ok=True) + label(350, 230, "⟦+점수|+points⟧", 11, "var(--good)")
         + bin_(560, 230, 0.8, "⟦저쪽?|that bin?⟧") + stamp2(630, 170, 0.6, ok=False) + label(630, 230, "⟦-점수|-points⟧", 11, "var(--bad)")
         + label(380, 285, "⟦맞으면 점수를 얻고, 틀리면 깎여요 — 그걸로 점점 요령을 익혀요|right guesses score points, wrong ones lose them — that's how the knack builds⟧", 12, "var(--ink)"))

# 3. 강화학습 = 정답표 없이, 보상/벌점만으로 좋은 행동을 스스로 찾아가는 것 (hero)
P3 = svg(360, sky(360)
         + person(220, 170, s=0.9, face=SMILE, **OPERATOR)
         + conveyor(60, 280, 160, 1.0) + produce(100, 260, 0.6)
         + bin_(420, 250, 0.8, "⟦합격|PASS⟧") + bin_(540, 250, 0.8, "⟦불합격|FAIL⟧")
         + stamp2(480, 160, 0.8, ok=True)
         + label(380, 30, "⟦강화학습 = 정답표 없이, 행동마다 돌아오는 보상/벌점만으로 좋은 습관을 스스로 찾는 것|reinforcement learning = no answer key — just finding good habits from the reward or penalty each action brings⟧", 13, "var(--ink)", cls="d")
         + label(380, 338, "⟦시간이 지날수록 점수를 더 많이 쌓는 쪽으로 행동이 바뀌어요|over time, behavior shifts toward whatever racks up more points⟧", 12, "var(--muted)"))

TRIAL_I = icon('<circle cx="22" cy="42" r="6" fill="var(--accent)"/><circle cx="36" cy="26" r="6" fill="var(--accent)"/><circle cx="50" cy="38" r="6" fill="var(--good)"/><path d="M22 42 L36 26 L50 38" stroke="var(--accent)" stroke-width="2" fill="none" stroke-dasharray="3 3"/>')
REWARD_I = icon('<path d="M32 10 L40 26 L56 28 L44 40 L48 56 L32 46 L16 56 L20 40 L8 28 L24 26 Z" fill="var(--good)"/>')
EXPLORE_I = icon('<path d="M14 50 Q20 20 32 32 Q44 44 50 14" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="50" cy="14" r="4" fill="var(--bad)"/>')
CUMUL_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--accent)"/><rect x="27" y="26" width="10" height="28" fill="var(--accent)"/><rect x="42" y="12" width="10" height="42" fill="var(--good)"/>')

# 4. 지도학습과 강화학습, 무엇이 다른가
P4 = svg(340, sky(340)
         + gradeboard(40, 30, 330, 280, "⟦지도학습(훈련 교사)|SUPERVISED (THE TRAINER)⟧",
                      ("⟦미리 정답 예제를 줘요|gives labeled examples upfront⟧", "⟦예제와 비교해 틀린 만큼 고쳐요|corrects by how far off it is from the example⟧",
                       "⟦한 번에 배우는 느낌|learns more directly, example by example⟧"), 0.9)
         + gradeboard(390, 30, 330, 280, "⟦강화학습(조작원 스스로)|REINFORCEMENT (THE OPERATOR ALONE)⟧",
                      ("⟦정답 없이 행동만 해봐요|no labels — just tries actions⟧", "⟦보상/벌점만 보고 스스로 고쳐요|adjusts using only reward or penalty⟧",
                       "⟦시행착오가 많아 시간이 걸려요|lots of trial and error, so it takes time⟧"), 0.9))

# 5. 보상을 잘못 설계하면 엉뚱한 요령만 늘어요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **OPERATOR) + produce(260, 220, 0.7)
         + label(190, 260, "⟦빨리 던지기만 하면 점수를 준댔더니, 제대로 안 보고 던지기만 해요|told fast tosses score points, it just tosses without really checking⟧", 11, "var(--bad)")
         + person(570, 130, s=0.8, face=EYES, **OPERATOR)
         + label(570, 262, "⟦보상을 '정확도'로 다시 설계하니 제대로 배워요|redesigning the reward around accuracy, it finally learns properly⟧", 11, "var(--ink)")
         + label(380, 300, "⟦강화학습은 '어떤 보상을 주는가'에 결과가 크게 좌우돼요|reinforcement learning's outcome hinges heavily on what reward you actually give⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "rl", "order": 21,
    "title": ("정답표 없이 점수로 배우는 신입 조작원", "The Rookie Operator Who Learns by Score, Not an Answer Key"),
    "h1": ("<em>강화학습</em>이/가 뭐예요?", "What is <em>Reinforcement Learning</em>?"),
    "sub": ("강화학습을, 미리 정답표 없이 행동마다 돌아오는 점수(보상)만으로 요령을 스스로 찾아가는 신입 조작원 이야기로 풀어봤어요.",
            "Reinforcement learning, told as a story about a rookie operator who, with no answer key, finds the knack purely from the score each action earns."),
    "panels": [
        {"svg": P1, "alt": ("신입 조작원이 정답표도 없이 작물을 분류해야 해서 땀을 흘림", "A rookie operator sweats, having to sort produce with no answer key at all"),
         "caption": ("신입 조작원에게 정답표가 없어요.", "The rookie operator has no answer key."),
         "small": ("훈련 교사가 미리 보여준 예제 없이 혼자 판단해야 해요.", "No teacher-given examples — just judge on your own.")},
        {"svg": P2, "alt": ("조작원이 작물을 한쪽 분류함에 던져보고 점수를 얻고, 다른 쪽에 던져보고 점수를 잃음", "The operator tosses produce into one bin and gains points, tries another bin and loses points"),
         "caption": ("일단 던져보고, 보너스와 벌점으로 배워요.", "It tries, and learns from the bonus or the penalty."),
         "small": ("맞으면 점수를 얻고, 틀리면 깎여요 — 그걸로 점점 요령을 익혀요.", "Right guesses score points, wrong ones lose them — that's how the knack builds.")},
        {"svg": P3, "hero": True, "alt": ("조작원이 작물을 정확히 합격함에 던져 넣고 승인 도장을 받으며 웃음", "The operator correctly tosses produce into the pass bin and smiles, receiving an approval stamp"),
         "caption": ("강화학습은 정답표 없이 보상/벌점만으로 좋은 행동을 스스로 찾는 거예요.", "Reinforcement learning finds good behavior from reward and penalty alone, with no answer key."),
         "small": ("시간이 지날수록 점수를 더 많이 쌓는 쪽으로 행동이 바뀌어요.", "Over time, behavior shifts toward whatever racks up more points."),
         "tricks": (4, [
             (TRIAL_I, ("시행착오", "Trial and error"), ("일단 해보고 결과를 봐요", "try it, then see what happens"), "calm"),
             (REWARD_I, ("보상 신호", "Reward signal"), ("맞으면 점수, 틀리면 벌점", "points for right, penalties for wrong")),
             (EXPLORE_I, ("탐험과 활용의 균형", "Balance explore and exploit"), ("새로운 것도 가끔 시도해요", "sometimes try something new"), "warm"),
             (CUMUL_I, ("누적 보상 최대화", "Maximize cumulative reward"), ("한 번이 아니라 전체 점수를 봐요", "it's the total score that counts, not one try")),
         ])},
        {"svg": P4, "alt": ("지도학습(훈련 교사가 정답 예제를 줌)과 강화학습(조작원이 보상만으로 스스로 고침)을 나란히 비교", "Supervised learning (the trainer gives labeled examples) is compared side by side with reinforcement learning (the operator self-corrects from reward alone)"),
         "caption": ("지도학습과 강화학습은 배우는 방식이 달라요.", "Supervised and reinforcement learning learn in different ways."),
         "small": ("둘 다 배우지만, 무엇을 보고 배우는지가 서로 달라요.", "Both learn — but from very different kinds of feedback.")},
        {"svg": P5, "alt": ("왼쪽: 빠른 속도만 보상하자 조작원이 제대로 안 보고 던지기만 함. 오른쪽: 보상을 정확도로 다시 설계하니 제대로 배움", "Left: rewarding only speed makes the operator toss carelessly. Right: redesigning the reward around accuracy fixes it"),
         "caption": ("보상을 잘못 설계하면 엉뚱한 요령만 늘어요.", "A poorly designed reward teaches the wrong knack."),
         "small": ("강화학습은 어떤 보상을 주는가에 결과가 크게 좌우돼요.", "The outcome hinges heavily on what reward you actually give.")},
    ],
    "summary": (("<b>강화학습</b> = 정답 예제 없이, <b>행동마다 돌아오는 보상/벌점</b>만 보고 <b>누적 점수를 최대화</b>하는 쪽으로 스스로 행동을 바꿔가는 학습 방식.",
                 "<b>Reinforcement learning</b> has no labeled examples — an agent changes its own behavior using only the <b>reward or penalty each action earns</b>, aiming to <b>maximize cumulative reward</b>."),
                ("강화학습(Reinforcement Learning)은 에이전트가 환경의 상태(state)를 보고 행동(action)을 선택하면, 환경이 보상(reward)과 다음 상태를 돌려주는 구조예요. 에이전트는 이 상호작용을 반복하며 누적 보상을 최대화하는 정책(policy)을 학습해요. 지도학습과 달리 정답 레이블이 없고, 탐험(exploration)과 활용(exploitation)의 균형, 보상 설계(reward shaping)가 핵심 난제예요. LLM 정렬에 쓰이는 RLHF도 이 틀 위에서, 사람의 선호를 보상으로 바꿔 모델을 강화학습시키는 방법이에요.",
                 "Reinforcement learning has an agent observe the environment's state, choose an action, and receive a reward plus the next state in return. Through repeated interaction, the agent learns a policy that maximizes cumulative reward. Unlike supervised learning, there are no labeled answers — balancing exploration and exploitation, and designing the reward itself (reward shaping), are the central challenges. RLHF, used to align LLMs, builds on this same framework: human preferences become the reward signal that reinforces the model.")),
    "glossary": [
        ("상태(State)", "State", ("지금 컨베이어 벨트 위의 상황.", "What's currently on the conveyor belt."), ("조작원이 행동을 고를 때 보는 정보예요.", "What the operator looks at before choosing an action.")),
        ("행동(Action)", "Action", ("어느 분류함에 던질지 고르는 것.", "Choosing which bin to toss into."), ("상태를 보고 조작원이 고르는 선택이에요.", "The choice the operator makes after seeing the state.")),
        ("보상(Reward)", "Reward", ("맞으면 +점수, 틀리면 -점수.", "Plus points for right, minus for wrong."), ("행동이 좋았는지 나빴는지 알려주는 유일한 신호예요.", "The only signal telling it whether the action was good or bad.")),
        ("정책(Policy)", "Policy", ("조작원이 몸에 익힌 요령 전체.", "The whole knack the operator has built up."), ("상태마다 어떤 행동을 할지 정하는 규칙이에요.", "The rule that decides what action to take in each state.")),
        ("탐험 vs 활용", "Exploration vs Exploitation", ("새 분류함을 시도할지, 늘 하던 대로 할지.", "Trying a new bin, or sticking with the usual one."), ("둘의 균형이 깨지면 학습이 멈추거나 헤매요.", "Lose the balance and learning stalls or wanders.")),
        ("RLHF", "RLHF", ("사람이 고른 쪽에 점수를 주는 특수한 강화학습.", "A special case where humans decide the score."), ('앵무새 세계에서 다루는 정렬 방법이에요. → <a href="alignment-ko.html">자세히 보기</a>', "Covered as an alignment method in the parrot world. → <a href=\"alignment-en.html\">see it in full</a>")),
        ("시계열분석(AR/MA)", "Time-Series Analysis (AR/MA)", ("지난 며칠 값으로 내일을 가늠하는 검수반장.", "The inspector who guesses tomorrow from the last few days."), ('예측과 학습은 다르지만 둘 다 데이터로 배워요. → <a href="timeseries-ko.html">자세히 보기</a>', 'A different kind of learning from data — forecasting, not acting. → <a href="timeseries-en.html">see it in full</a>')),
        ("AI 신뢰성", "AI Trustworthiness", ("정확도만으론 못 받는 품질인증 등급판.", "The certification board accuracy alone can't earn."), ('보상을 잘못 설계한 결과도 신뢰성 점검에서 걸러요. → <a href="aitrust-ko.html">자세히 보기</a>', 'A bad reward design is one thing a trust check catches. → <a href="aitrust-en.html">see it in full</a>')),
    ],
}
