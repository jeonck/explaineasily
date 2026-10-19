from _draw import *
from _world import *


def guess_face(x, y, s=1.0, complete=False):
    """접시만 보고 그려낸 추측 얼굴. complete=False 면 점선/흐릿, True 면 더 뚜렷해진 추측."""
    stroke = "var(--ink)" if complete else "var(--muted)"
    dash = "" if complete else ' stroke-dasharray="4 4"'
    op = "1" if complete else "0.65"
    return (f'<g transform="translate({x},{y}) scale({s})" opacity="{op}">'
            f'<circle cx="0" cy="0" r="30" fill="none" stroke="{stroke}" stroke-width="3"{dash}/>'
            f'<circle cx="-10" cy="-6" r="2.6" fill="{stroke}"/><circle cx="10" cy="-6" r="2.6" fill="{stroke}"/>'
            f'<path d="M-11 10 Q0 17 11 10" stroke="{stroke}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
            '</g>')


# 1. 몰래 쪽지 손님이 같은 요리를 조금씩 바꿔서 아주 많이 시켜요
P1 = svg(320, sky(320)
         + person(60, 150, s=0.75, face=FROWN, **SNEAK) + label(87, 262, "⟦몰래 쪽지 손님|the sneaky orderer⟧", 11, "var(--muted)")
         + ticket(205, 100, 0.65) + ticket(205, 150, 0.65) + ticket(205, 200, 0.65)
         + label(205, 240, "⟦조금씩 바꿔서 여러 번|tweaked, again and again⟧", 11, "var(--ink)")
         + person(400, 150, s=0.8, face=EYES, **CHEF)
         + dish(400, 255, 0.5) + label(400, 288, "⟦매번 정직하게 만들어 줘요|makes it honestly, every single time⟧", 11, "var(--muted)")
         + logbook(580, 110, 0.8, w=110, h=70, rows=4) + label(635, 200, "⟦나온 걸 하나하나 적어요|writes down what comes out, one by one⟧", 11, "var(--ink)", cls="d")
         + label(380, 305, "⟦몰래 쪽지 손님이 똑같은 요리를, 조금씩 바꿔서 아주 많이 시켜요|the sneaky guest orders the same dish, over and over, each time a little different⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 주방장은 한 번에 한 주문만 봐요 — 쌓아 놓고 봐야 패턴이 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 150, s=0.85, face=EYES, **CHEF) + ticket(220, 170, 0.6)
         + label(170, 250, "⟦한 번에 한 주문만 봐요|sees only one order at a time⟧", 12, "var(--muted)")
         + dish(400, 90, 0.4, color="var(--accent)") + dish(450, 95, 0.4, color="var(--accent-soft)")
         + dish(500, 88, 0.4, color="var(--accent)") + dish(550, 93, 0.4, color="var(--accent-soft)")
         + dish(600, 90, 0.4, color="var(--accent)") + dish(650, 95, 0.4, color="var(--accent-soft)")
         + label(520, 135, "⟦나란히 줄 세워야만 보이는 조금씩 다른 색|a slight color shift that only shows when you line them all up⟧", 11, "var(--bad)")
         + label(380, 282, "⟦하나씩 보면 다 평범해요 — 쭉 줄 세워 놓고 봐야 패턴이 보여요|each one alone looks ordinary — only lined up together does the pattern show⟧", 12, "var(--ink)"))

# 3. 모델 인버전 = 접시들만 보고 원래 재료를 거꾸로 그려보는 일 (hero)
P3 = svg(360, sky(360)
         + dish(100, 80, 0.45, color="var(--accent)") + dish(150, 85, 0.45, color="var(--accent-soft)")
         + dish(200, 78, 0.45, color="var(--accent)") + dish(250, 85, 0.45, color="var(--accent-soft)")
         + dish(300, 80, 0.45, color="var(--accent)")
         + label(200, 130, "⟦접시들의 색과 맛만 가지고|from nothing but the color and taste of the dishes⟧", 11, "var(--muted)")
         + person(430, 130, s=0.7, face=EYES, **SNEAK)
         + '<path d="M470 150 L520 200" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + guess_face(560, 220, 1.0, complete=False) + guess_face(680, 220, 1.0, complete=True)
         + label(560, 275, "⟦처음엔 흐릿한 추측|a blurry guess at first⟧", 11, "var(--ink)")
         + label(680, 275, "⟦반복할수록 뚜렷해져요|sharper with every repeat⟧", 11, "var(--ink)")
         + label(380, 30, "⟦모델 인버전 = 접시들만 보고 원래 재료를 거꾸로 그려보는 일|Model inversion = sketching the original ingredients backward from nothing but the dishes⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦원래 재료는 한 번도 직접 보여준 적이 없어요|the real ingredients were never shown directly, not even once⟧", 12, "var(--muted)"))

# 4. 흐름: 조금씩 다른 주문 → 조금씩 다른 접시 → 나란히 비교 → 추측 얼굴
P4 = svg(330, sky(330)
         + ticket(70, 70, 0.6) + label(70, 108, "⟦주문 A|order A⟧", 10, "var(--muted)")
         + '<path d="M100 85 L150 85" stroke="var(--muted)" stroke-width="3"/>' + dish(175, 85, 0.45)
         + ticket(70, 150, 0.6) + label(70, 188, "⟦주문 B|order B⟧", 10, "var(--muted)")
         + '<path d="M100 165 L150 165" stroke="var(--muted)" stroke-width="3"/>' + dish(175, 165, 0.45, color="var(--accent-soft)")
         + ticket(70, 230, 0.6) + label(70, 268, "⟦주문 C|order C⟧", 10, "var(--muted)")
         + '<path d="M100 245 L150 245" stroke="var(--muted)" stroke-width="3"/>' + dish(175, 245, 0.45)
         + '<path d="M210 85 L210 245" stroke="var(--line)" stroke-width="2"/>'
         + board(260, 50, 230, 220, "⟦나란히 비교|LINE THEM UP⟧",
                 ("⟦색이 짙은 곳 = 많이 쓰인 재료|darker = an ingredient used a lot⟧",
                  "⟦색이 옅은 곳 = 적게 쓰인 재료|lighter = barely used at all⟧",
                  "⟦한 번으론 몰라요, 여러 번이면 보여요|one try tells nothing — many tries do⟧"), 1.0)
         + '<path d="M490 160 L560 160" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + guess_face(630, 160, 1.1, complete=True)
         + label(630, 215, "⟦원래 재료를 닮은 추측 그림|a guess that resembles the original ingredients⟧", 11, "var(--ink)")
         + label(380, 305, "⟦조금씩 다른 주문을 쌓아 비교하면, 원래 재료의 그림자가 드러나요|stack up the slightly different orders, and a shadow of the original ingredients shows⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 완벽하게 똑같진 않고, 멤버십 추론과는 달라요
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + guess_face(160, 140, 1.3, complete=True) + label(160, 220, "⟦그럴듯한 추측일 뿐|a plausible guess, not a copy⟧", 12, "var(--ink)")
         + label(160, 245, "⟦원래 재료와 완전히 똑같진 않아요|never an exact match for the real ingredients⟧", 11, "var(--muted)")
         + person(540, 110, s=0.75, face=EYES, **SNEAK)
         + label(540, 205, "⟦'왔었나요?'만 궁금하면|if you only ask was it here?⟧", 11, "var(--bad)")
         + label(540, 228, "⟦멤버십 추론으로 충분해요|membership inference is enough⟧", 11, "var(--bad)", cls="d")
         + label(540, 255, "⟦재료 자체를 그리려면 더 많은 반복이 필요해요|sketching the ingredients needs far more repeats⟧", 10, "var(--muted)")
         + label(380, 295, "⟦사람 주방장은 반복 주문을 의심하지만, 이 주방장은 매 주문을 따로따로만 봐요|a human chef would get suspicious of the repeats — this one just sees each order on its own⟧", 12, "var(--ink)", cls="d"))

RATE_I = icon('<circle cx="28" cy="34" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/>'
              '<path d="M28 22 v12 l9 7" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>'
              '<rect x="42" y="10" width="7" height="22" rx="3" fill="var(--bad)" transform="rotate(35 45 21)"/>')
NOISE_I = icon('<ellipse cx="32" cy="42" rx="22" ry="7" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
               '<circle cx="32" cy="34" r="10" fill="var(--accent)"/>'
               '<path d="M12 16 q6 -9 12 0 q6 -9 12 0 q6 -9 12 0" stroke="var(--muted)" stroke-width="3" fill="none"/>')
HIDE_I = icon('<circle cx="32" cy="32" r="14" fill="none" stroke="var(--muted)" stroke-width="4"/>'
              '<circle cx="32" cy="32" r="4" fill="var(--muted)"/>'
              '<path d="M12 12 L52 52" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
ONE_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><rect x="18" y="34" width="28" height="22" rx="8" fill="var(--good)"/>'
             '<path d="M10 10 L54 54" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "modelinversion", "order": 10,
    "title": ("접시 더미에서 되살린 얼굴", "A Face Rebuilt from a Pile of Dishes"),
    "h1": ("<em>모델 인버전</em>이 뭐예요?", "What is <em>Model Inversion</em>?"),
    "sub": ("모델 인버전을, 같은 요리를 조금씩 바꿔 아주 많이 시켜보고 나온 접시들만으로 원래 재료를 거꾸로 그려내는 이야기로 풀어봤어요.",
            "Model inversion, told as a story about ordering the same dish again and again, each time a little different, and sketching the original ingredients backward from nothing but the dishes that come out."),
    "panels": [
        {"svg": P1, "alt": ("몰래 쪽지 손님이 같은 요리를 조금씩 바꿔 적은 주문서 세 장을 내고, 주방장은 매번 정직하게 만들어 줌. 손님은 나온 결과를 장부에 적음", "The sneaky guest hands over three slightly different order tickets for the same dish; the chef makes each one honestly, and the guest writes down every result in a logbook"),
         "caption": ("몰래 쪽지 손님이 같은 요리를, 조금씩 바꿔서 아주 많이 시켜요.", "The sneaky guest orders the same dish, over and over, each time a little different."),
         "small": ("주방장은 의심 없이 매번 성실하게 만들어 줘요. 그 결과를 전부 받아 적어요.", "The chef makes each one honestly, with no suspicion at all — and every result gets written down.")},
        {"svg": P2, "alt": ("주방장은 한 번에 한 주문만 보고, 여러 접시를 나란히 줄 세워야만 색이 조금씩 다른 패턴이 보임", "The chef only ever looks at one order at a time; only when several dishes are lined up side by side does a slight color pattern appear"),
         "caption": ("하나씩 보면 다 평범해요 — 쭉 줄 세워 놓고 봐야 패턴이 보여요.", "Each one alone looks ordinary — only lined up together does the pattern show."),
         "small": ("주방장은 지금 들어온 주문만 봐요. 여러 번의 주문을 모아 비교하는 건 주방장 몫이 아니에요.", "The chef only sees the order in front of it right now. Comparing many orders together is nobody's job inside the kitchen.")},
        {"svg": P3, "hero": True, "alt": ("접시 여러 개의 색과 맛만 가지고, 몰래 쪽지 손님이 흐릿한 추측 얼굴에서 점점 뚜렷한 추측 얼굴을 그려냄", "From nothing but the color and taste of several dishes, the sneaky guest sketches a blurry guess that sharpens into a clearer one"),
         "caption": ("모델 인버전은 접시들만 보고 원래 재료를 거꾸로 그려보는 일이에요.", "Model inversion is sketching the original ingredients backward from nothing but the dishes."),
         "small": ("원래 재료는 한 번도 직접 보여준 적이 없어요. 접시의 색과 맛이라는 흔적만으로 거꾸로 짐작하는 거예요.", "The real ingredients were never shown directly — the guess works backward from nothing but the color and taste left behind."),
         "tricks": (4, [
             (RATE_I, ("반복 주문은 횟수 제한", "Limit how often the same order repeats"), ("같은 손님이 너무 자주 시키면 멈춰요", "too many repeats from one guest get cut off"), "calm"),
             (NOISE_I, ("접시에 살짝 노이즈", "Blur the dish a little"), ("답에 작은 흔들림을 섞어요", "mix a small wobble into every answer"), "calm"),
             (HIDE_I, ("확신 수치는 숨기기", "Hide the exact confidence number"), ("딱 맞는 숫자는 안 보여줘요", "no precise score handed over"), "warm"),
             (ONE_I, ("한 사람만의 재료는 안 쓰기", "Never train on one person's unique data alone"), ("누구인지 드러나는 재료는 빼요", "drop anything that points to just one person"), "warm"),
         ])},
        {"svg": P4, "alt": ("주문 A·B·C가 조금씩 다른 접시를 만들고, 나란히 비교하면 짙은 재료와 옅은 재료가 드러나 추측 얼굴로 이어짐", "Orders A, B, and C make slightly different dishes; lining them up reveals which ingredient was used a lot and which barely at all, leading to a guessed face"),
         "caption": ("조금씩 다른 주문을 쌓아 비교하면, 원래 재료의 그림자가 드러나요.", "Stack up the slightly different orders, and a shadow of the original ingredients shows."),
         "small": ("한 번의 주문으로는 아무것도 몰라요. 아주 많은 주문을 쌓아야 비로소 그림자가 보여요.", "A single order tells you nothing. It takes a great many orders, stacked together, before the shadow appears.")},
        {"svg": P5, "alt": ("왼쪽: 그럴듯하지만 완전히 똑같진 않은 추측 얼굴. 오른쪽: 멤버십 추론은 왔었는지만 묻고, 모델 인버전은 재료 자체를 그려낸다는 차이", "Left: a plausible but never exact guessed face. Right: membership inference only asks whether a guest was there, while model inversion sketches the ingredients themselves"),
         "caption": ("그럴듯한 추측일 뿐, 원래 재료와 완전히 똑같진 않아요.", "It's a plausible guess, never an exact match for the real ingredients."),
         "small": ('"왔었나요?"만 궁금하다면 <a href="membershipinference-ko.html">멤버십 추론</a>으로 충분해요. 재료 자체를 그려내는 건 더 어렵고, 더 많은 반복이 필요해요. 사람 주방장은 반복 주문을 의심하지만, 이 주방장은 매 주문을 따로따로만 봐요.',
                   'If all you want to know is "was this guest here?", <a href="membershipinference-en.html">membership inference</a> is enough. Sketching the ingredients themselves is harder, and takes far more repeats. A human chef would get suspicious of the repeats — this one just sees each order on its own.')},
    ],
    "summary": (("<b>모델 인버전</b> = 같은 요리를 <b>조금씩 바꿔 아주 많이 시켜보고</b>, 나온 <b>접시들의 색과 맛만으로</b> 원래 재료를 <b>거꾸로 그려내는</b> 일. 완벽한 복원은 아니지만, 반복할수록 그림이 뚜렷해져요.",
                 "<b>Model inversion</b> = ordering the same dish <b>again and again, each time slightly different</b>, and using <b>nothing but the color and taste of the dishes</b> to <b>sketch the original ingredients backward</b>. It's never a perfect copy, but the picture sharpens with every repeat."),
                ("Model Inversion. 모델에 반복적으로 질의하고 그 출력(확신 점수·결과물)을 분석해, 학습에 쓰인 원본 데이터(예: 얼굴 이미지, 특정인의 레코드)를 근사적으로 재구성하는 공격이에요. 모델이 입력을 너무 세밀하게 외웠을수록(메모리제이션), 공격자가 접근할 수 있는 확신 점수·그래디언트 정보가 많을수록 더 정교하게 복원돼요. 방어는 출력 노이즈 추가, 확신 점수 은닉, 질의 횟수 제한, 식별 가능한 단일 개체 데이터의 학습 배제예요.",
                 "An attack that repeatedly queries a model and analyzes its outputs (confidence scores, generated results) to approximately reconstruct the original training data — a face image, a specific person's record. The more a model has literally memorized its inputs, and the more confidence-score or gradient information an attacker can access, the sharper the reconstruction. Defenses include adding noise to outputs, hiding exact confidence scores, rate-limiting queries, and excluding data that identifies a single individual from training.")),
    "glossary": [
        ("모델 인버전", "Model Inversion", ("접시만 보고 원래 재료를 거꾸로 그리는 일.", "Sketching the original ingredients backward from nothing but the dishes."), ("완벽한 복원이 아니라 그럴듯한 추측이에요.", "Never a perfect copy — just a plausible guess.")),
        ("멤버십 추론", "Membership Inference", ("이 손님이 왔었는지만 알아내는 일.", "Finding out only whether a guest was ever here."), ('재료 자체는 안 궁금할 때. → <a href="membershipinference-ko.html">왔었는지 알아내기</a>', 'For when the ingredients themselves don\'t matter. → <a href="membershipinference-en.html">telling whether it was there</a>')),
        ("메모리제이션", "Memorization", ("레시피북 한 줄을 그대로 베껴 내놓는 버릇.", "The habit of serving a line straight out of the recipe book."), ('잘 외울수록 거꾸로 그리기도 쉬워져요. → <a href="memorization-ko.html">외운 걸 그대로 내놓기</a>', 'The better it memorizes, the easier it is to invert. → <a href="memorization-en.html">serving what it memorized</a>')),
        ("AI 프라이버시", "AI Privacy", ("비밀 재료를 처음부터 안 주는 원칙.", "The principle of never handing over the secret ingredient at all."), ('원래 재료가 재구성될 수 있다는 걸 염두에 둔 약속이에요. → <a href="aiprivacy-ko.html">앵무새에게 준 비밀 콩</a>', 'A promise made knowing the original ingredients could be rebuilt. → <a href="aiprivacy-en.html">the secret beans we gave the parrot</a>')),
        ("레드팀", "Red Team", ("일부러 반복 주문을 넣어서 재구성이 되는지 시험해 봄.", "Deliberately placing repeated orders to test whether reconstruction works."), ('출시 전에 이런 공격이 통하는지 먼저 확인해요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', 'Checks before release whether this attack succeeds. → <a href="redteam-en.html">the security world\'s red team</a>')),
        ("속도 제한", "Rate Limiting", ("같은 손님의 반복 주문을 느리게 또는 막기.", "Slowing or blocking repeated orders from the same guest."), ('반복이 많아야 통하는 공격이라 효과가 커요. → <a href="ratelimiting-ko.html">놀이공원의 입장 제한</a>', 'This attack needs many repeats, so this helps a lot. → <a href="ratelimiting-en.html">the amusement park\'s entry limit</a>')),
        ("학습 데이터", "Training Data", ("재료 창고에 처음 들어간 재료들.", "The ingredients that first went into the pantry."), ("모델 인버전이 거꾸로 찾아내려는 바로 그 재료예요.", "The very ingredients model inversion tries to work backward to.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('이상하게 비슷비슷한 반복 주문을 걸러내는 데도 쓰여요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'Also used to catch suspiciously repetitive orders. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
    ],
}
