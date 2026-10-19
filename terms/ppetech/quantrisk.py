from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


DICE_P = '<rect x="12" y="12" width="40" height="40" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="24" cy="24" r="4" fill="var(--ink)"/><circle cx="40" cy="24" r="4" fill="var(--ink)"/><circle cx="32" cy="32" r="4" fill="var(--ink)"/><circle cx="24" cy="40" r="4" fill="var(--ink)"/><circle cx="40" cy="40" r="4" fill="var(--ink)"/>'
SCALE_P = '<path d="M32 10 v40" stroke="#8A8A8A" stroke-width="3"/><path d="M14 20 h36" stroke="#8A8A8A" stroke-width="3"/><path d="M14 20 a9 9 0 0 0 18 0 M32 20 a9 9 0 0 0 18 0" fill="none" stroke="var(--bad)" stroke-width="3"/>'
MULT_P = '<text x="32" y="42" font-size="36" font-weight="700" fill="var(--accent)" text-anchor="middle">×</text>'
BOARD_P = '<rect x="8" y="12" width="48" height="36" rx="3" fill="#1B2A44"/><text x="32" y="36" font-size="18" font-weight="700" fill="var(--accent)" text-anchor="middle">42</text>'
DICE_I, SCALE_I, MULT_I, BOARD_I = icon(DICE_P), icon(SCALE_P), icon(MULT_P), icon(BOARD_P)

# 1. 안전요원마다 "위험해 보여요" 말이 다 달라요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=EYES, **GUIDE)
         + bubble(300, 80, 220, 40, "⟦이 부스, 좀 위험해 보이는데요?|this booth looks kind of risky, doesn't it?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 260, "⟦'위험해 보인다'는 사람마다 기준이 다 달라요|'looks risky' means something different to every person⟧", 12, "var(--ink)"))

# 2. 같은 부스를 보고도 안전요원마다 평가가 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=EYES, **GUIDE) + bubble(70, 70, 190, 40, "⟦이 정도면 안전해요|this looks fine, safe enough⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **DEMO) + bubble(460, 70, 220, 40, "⟦아뇨, 아주 위험해 보여요|no, this looks very dangerous⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦같은 부스인데 사람마다 말이 다르면, 뭘 먼저 고쳐야 할지 못 정해요|when the same booth gets different verdicts, you can't tell what to fix first⟧", 12, "var(--ink)"))

# 3. 정량적 위험분석 = 위험을 숫자 하나로 적는 전광판 (hero)
P3 = svg(340, sky(340)
         + glyph(230, 110, 1.3, DICE_P) + glyph(350, 125, 1.0, MULT_P) + glyph(420, 110, 1.3, SCALE_P) + glyph(540, 110, 1.3, BOARD_P)
         + person(620, 240, s=0.75, face=SMILE, **GUIDE)
         + label(380, 30, "⟦정량적 위험분석 = '일어날 확률' × '피해 크기'를 곱해, 위험을 숫자 하나로 적는 것|quantitative risk analysis = probability × impact, written as one single risk number⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦느낌이 아니라 숫자로 말하니, 누가 봐도 순위를 매길 수 있어요|a number instead of a feeling — so anyone can rank the risks the same way⟧", 12, "var(--muted)"))

# 4. 위험도 = 확률 × 영향
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦위험도 공식|THE RISK FORMULA⟧",
                     ("⟦위험도 = 발생 확률 × 피해 규모|risk = probability × impact⟧",
                      "⟦확률 낮음·피해 큼 → 중간 위험|low probability, big impact → medium risk⟧",
                      "⟦확률 높음·피해 큼 → 높은 위험|high probability, big impact → high risk⟧",
                      "⟦점수대로 고칠 순서를 정해요|the score decides the order of fixes⟧"), 1.0, hl=0)
         + person(560, 150, s=0.75, face=EYES, **DEMO)
         + label(560, 250, "⟦ALE(연간예상손실) 같은 공식이 이 생각을 더 정교하게 다듬어요|formulas like ALE (annual loss expectancy) refine this idea further⟧", 11, "var(--muted)"))

# 5. 한계 - 확률 추정 자체가 틀리면, 숫자도 함께 틀려요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 110, 1.3, BOARD_P)
         + label(190, 250, "⟦숫자로 비교하니 우선순위를 정하기 쉬워요|numbers make it easy to compare and prioritize⟧", 11, "var(--ink)")
         + glyph(560, 110, 1.3, DICE_P)
         + label(570, 250, "⟦그 확률을 처음에 잘못 어림잡으면, 멋진 숫자도 다 틀려요|guess that probability wrong at the start, and the tidy number is wrong too⟧", 11, "var(--ink)")
         + label(380, 282, "⟦숫자가 정확해 보여도, 바탕엔 여전히 사람의 추정이 깔려 있어요|the number looks precise, but a human guess still sits underneath it⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "quantrisk", "order": 21,
    "title": ("위험을 숫자 하나로 적는 전광판", "The Scoreboard That Writes Risk as One Number"),
    "h1": ("<em>정량적 위험분석 기법</em>이 뭐예요?", "What is <em>Quantitative Risk Analysis</em>?"),
    "sub": ("정량적 위험분석을, 전시장 안전요원이 확률과 피해 크기를 곱해 위험을 숫자로 적는 전광판 이야기로 풀어봤어요.",
            "Quantitative risk analysis, told as a story about a safety officer who multiplies probability by impact and writes risk as one number on a scoreboard."),
    "panels": [
        {"svg": P1, "alt": ("안내원이 부스를 보고 '위험해 보인다'고 막연히 말함", "A guide looks at a booth and vaguely says it looks risky"),
         "caption": ("안전요원마다 '위험해 보여요' 말이 다 달라요.", "Every safety officer says something different when a booth 'looks risky.'"),
         "small": ("'위험해 보인다'는 사람마다 기준이 다 달라요.", "'Looks risky' means something different to every person.")},
        {"svg": P2, "alt": ("두 안내원이 같은 부스를 두고 안전하다, 위험하다로 엇갈림", "Two guides disagree over the same booth — one says safe, one says dangerous"),
         "caption": ("같은 부스를 보고도 안전요원마다 평가가 달라요.", "The same booth gets different verdicts from different officers."),
         "small": ("같은 부스인데 사람마다 말이 다르면, 뭘 먼저 고쳐야 할지 못 정해요.", "When the same booth gets different verdicts, you can't tell what to fix first.")},
        {"svg": P3, "hero": True, "alt": ("주사위와 저울을 곱해 전광판에 숫자 42가 뜨고, 안내원이 흐뭇해함", "A die multiplied by a scale lights up '42' on a scoreboard while a guide looks satisfied"),
         "caption": ("정량적 위험분석은 확률과 피해 크기를 곱해 위험을 숫자 하나로 적는 거예요.", "Quantitative risk analysis multiplies probability by impact, writing risk as one single number."),
         "small": ("느낌이 아니라 숫자로 말하니, 누가 봐도 순위를 매길 수 있어요.", "A number instead of a feeling — so anyone can rank the risks the same way."),
         "tricks": (4, [
             (DICE_I, ("확률 재기", "Measure probability"), ("얼마나 자주 일어날까요", "how often might it happen")),
             (SCALE_I, ("피해 크기 재기", "Measure impact"), ("얼마나 크게 다칠까요", "how big would the damage be")),
             (MULT_I, ("곱해서 점수내기", "Multiply for a score"), ("확률 × 피해 크기예요", "probability × impact"), "calm"),
             (BOARD_I, ("순위 매기기", "Rank by score"), ("숫자가 큰 것부터 고쳐요", "fix the highest number first"), "warm"),
         ])},
        {"svg": P4, "alt": ("위험도 공식 설명판: 위험도 = 확률 × 피해 규모, 점수대로 순서를 정함", "A board shows risk = probability × impact, with the score deciding fix order"),
         "caption": ("위험도는 확률과 피해 규모를 곱해서 나와요.", "Risk comes from multiplying probability by impact."),
         "small": ("ALE(연간예상손실) 같은 공식이 이 생각을 더 정교하게 다듬어요.", "Formulas like ALE (annual loss expectancy) refine this idea further.")},
        {"svg": P5, "alt": ("왼쪽: 전광판 숫자로 우선순위를 쉽게 정함. 오른쪽: 확률을 잘못 어림잡은 주사위가 보임", "Left: the scoreboard number makes prioritizing easy. Right: a die shows a badly guessed probability"),
         "caption": ("확률 추정 자체가 틀리면, 숫자도 함께 틀려요.", "Guess the probability wrong, and the number is wrong too."),
         "small": ("숫자가 정확해 보여도, 바탕엔 여전히 사람의 추정이 깔려 있어요.", "The number looks precise, but a human guess still sits underneath it.")},
    ],
    "summary": (("<b>정량적 위험분석</b> = <b>발생 확률 × 피해 규모</b>를 계산해, 위험의 크기를 <b>숫자 하나</b>로 비교하는 기법.",
                 "<b>Quantitative risk analysis</b> = calculating <b>probability × impact</b> to compare the size of risks as <b>a single number</b>."),
                ("정량적 위험분석 기법은 위험을 발생 확률과 손실 규모의 곱으로 수치화해, 서로 다른 위험을 객관적으로 비교·우선순위화하는 방법이에요. ALE(연간예상손실), ROSI(보안투자수익률), 위험 매트릭스 등이 대표적이며, 정성적 분석(상/중/하 같은 등급 판단)과 짝을 이뤄 보완적으로 쓰여요.",
                 "Quantitative risk analysis scores a risk as probability multiplied by loss magnitude, letting different risks be compared and prioritized objectively. ALE (Annual Loss Expectancy), ROSI (Return on Security Investment), and risk matrices are common tools, typically paired with qualitative analysis (high/medium/low judgment calls) as a complement.")),
    "glossary": [
        ("ALE(연간예상손실)", "Annual Loss Expectancy", ("일 년 치 피해를 미리 더해보는 셈.", "Adding up a year's worth of expected damage in advance."), ("확률×피해를 일 년 단위로 계산해요.", "It's probability times impact, scaled to a year.")),
        ("위험 매트릭스", "Risk Matrix", ("확률과 피해를 표 한 칸에 놓는 것.", "Placing probability and impact into one grid cell."), ("숫자 대신 칸 색으로 보여주는 방식이에요.", "A way of showing the same idea with colored cells instead of numbers.")),
        ("정성적 위험분석", "Qualitative Risk Analysis", ("상·중·하로만 매기는 평가.", "Judging risk only as high, medium, or low."), ("정량적 분석과 짝을 이루는 보완 방법이에요.", "A complementary method that pairs with the quantitative one.")),
        ("ROSI", "Return on Security Investment", ("보안에 쓴 돈이 본전을 하는지 보는 셈.", "A calculation of whether security spending pays for itself."), ("정량적 위험분석의 숫자를 투자 결정에 써요.", "It feeds the quantitative risk number into a spending decision.")),
        ("프로젝트 위험관리", "Project Risk Management", ("비 오는 날에도 챙기는 우산.", "The umbrella you carry even on a dry day."), ("비슷한 위험이지만 다른 세계의 관리 틀이에요. → <a href=\"projrisk-ko.html\">비 오는 날에도 챙기는 우산</a>", "Risk again, but a different world's management framework. → <a href=\"projrisk-en.html\">the umbrella you carry even on a dry day</a>")),
        ("드론 보안위협", "Drone Security Threats", ("이 숫자 매기기가 적용되는 실제 위협.", "A real-world threat this same scoring applies to."), ('이 드론 위협들의 크기도 이렇게 재요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', 'These drone threats get sized up the same way. → <a href="dronesecurity-en.html">the drone held up by an invisible string</a>')),
        ("NFT", "NFT", ("가치가 출렁이는 디지털 자산.", "A digital asset whose value swings wildly."), ('가격 변동 위험을 가늠할 때도 이 기법이 쓰여요. → <a href="nft-ko.html">그림에 붙이는 위조 못 하는 증명서</a>', "This same technique sizes up its price swings too. → <a href=\"nft-en.html\">the certificate you can't forge</a>")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
