from _draw import *
from _world import *


def pixel_grid(x, y, cols, rows, cell=22, seed=1):
    out = ""
    for r in range(rows):
        for c in range(cols):
            v = (c * 7 + r * 13 + seed * 5) % 5
            shade = ["#FFF8E7", "#F3D9A4", "#C9A86A", "#8B5E3C", "#5A3B22"][v]
            out += f'<rect x="{x + c * cell}" y="{y + r * cell}" width="{cell}" height="{cell}" fill="{shade}" stroke="var(--line)" stroke-width="1"/>'
    return out


def window_box(x, y, size, color="var(--accent)"):
    return f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="4" stroke-dasharray="4 3"/>'


# 1. 사진 전체를 한 번에 보려니 숫자가 너무 많아요
P1 = svg(340, sky(340)
         + label(380, 25, "⟦사진 전체를 한 번에 보려니, 숫자가 너무 많아요|trying to take in the whole photo at once — there are just too many numbers⟧", 13, "var(--bad)", cls="d")
         + pixel_grid(230, 50, 14, 8, 22)
         + person(380, 250, s=0.7, face=SWEAT + EYES, **OPERATOR))

# 2. 왜 어려운가: 전체를 한눈에 숫자로만 보면, 어디에 무늬가 있는지 놓쳐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + pixel_grid(230, 60, 14, 8, 22, seed=2)
         + label(380, 260, "⟦어디에 씨앗 무늬가 있는지, 숫자만 보면 안 보여요|where the seed-mark pattern sits — invisible when you only see loose numbers⟧", 12, "var(--ink)", cls="d")
         + label(380, 25, "⟦전체를 한눈에 숫자로만 보면, 어디에 무늬가 있는지 놓쳐요|taking in everything as loose numbers makes local patterns slip right past⟧", 13, "var(--ink)", cls="d"))

# 3. CNN = 작은 창을 조금씩 옮기며 국소 무늬를 찾고, 쌓아 올려 전체를 이해하는 방법 (hero)
P3 = svg(360, sky(360)
         + label(380, 25, "⟦CNN = 작은 창을 조금씩 옮기며 국소 무늬를 찾고, 쌓아 올려 전체를 이해해요|a CNN slides a small window bit by bit, finds local patterns, and stacks them into the whole picture⟧", 13, "var(--ink)", cls="d")
         + label(150, 55, "⟦원본 사진|original photo⟧", 11, "var(--muted)", cls="d")
         + pixel_grid(60, 70, 8, 8, 22, seed=3)
         + window_box(104, 114, 44)
         + f'<path d="M280 136 H340" stroke="var(--accent)" stroke-width="4" marker-end="url(#cnna)"/>'
         + '<defs><marker id="cnna" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="var(--accent)"/></marker></defs>'
         + label(470, 55, "⟦작은 무늬 지도(특징맵)|small pattern map (feature map)⟧", 11, "var(--muted)", cls="d")
         + pixel_grid(400, 70, 6, 6, 22, seed=4)
         + label(150, 290, "⟦필터가 창을 한 칸씩 옮겨요|the filter nudges the window one cell at a time⟧", 11, "var(--ink)")
         + label(470, 290, "⟦무늬가 있던 자리만 밝게 남아요|only where a pattern was found stays bright⟧", 11, "var(--ink)"))

SLIDE_I = icon('<rect x="8" y="16" width="48" height="32" rx="3" fill="none" stroke="var(--line)" stroke-width="2"/><rect x="12" y="20" width="16" height="16" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="3 2"/><path d="M34 28 h14" stroke="var(--accent)" stroke-width="3"/>')
POOL_I = icon('<rect x="10" y="10" width="20" height="20" fill="#C9A86A"/><rect x="34" y="10" width="20" height="20" fill="#8B5E3C"/><rect x="10" y="34" width="20" height="20" fill="#F3D9A4"/><rect x="34" y="34" width="20" height="20" fill="#5A3B22"/><path d="M30 32 L48 48" stroke="var(--accent)" stroke-width="3"/>')
LAYER_I = icon('<rect x="10" y="38" width="44" height="10" fill="var(--accent-soft)"/><rect x="14" y="26" width="36" height="10" fill="var(--accent)"/><rect x="18" y="14" width="28" height="10" fill="var(--good)"/>')
CLASSIFY_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "cnn", "order": 7,
    "title": ("작은 창으로 조금씩 살펴보는 눈", "The Eye That Scans Through a Small Window"),
    "h1": ("<em>CNN(합성곱 신경망)</em>이 뭐예요?", "What is a <em>CNN (Convolutional Neural Network)</em>?"),
    "sub": ("CNN을, 사진 전체를 한 번에 보는 대신 작은 창을 조금씩 옮기며 무늬를 찾는 눈 이야기로 풀어봤어요.",
            "CNNs, told as a story about an eye that scans a small window bit by bit, instead of staring at the whole photo at once."),
    "panels": [
        {"svg": P1, "alt": ("픽셀 격자로 가득한 큰 사진 앞에서 선별기 조작원이 진땀을 흘림", "The operator sweats in front of a huge photo made of a dense pixel grid"),
         "caption": ("사진 전체를 한 번에 보려니 숫자가 너무 많아요.", "Trying to take in the whole photo at once — there are too many numbers."),
         "small": ("픽셀 하나하나를 다 따로 보면 감당이 안 돼요.", "Looking at every single pixel separately is simply too much.")},
        {"svg": P2, "alt": ("픽셀 격자를 숫자로만 쭉 늘어놓으면 어디에 씨앗 무늬가 있는지 안 보임을 보여줌", "Laid out as loose numbers, the pixel grid hides exactly where a seed-mark pattern sits"),
         "caption": ("숫자만 보면, 어디에 무늬가 있는지 놓쳐요.", "Looking only at loose numbers, local patterns slip past."),
         "small": ("자리(위치) 정보를 지키면서 봐야, 무늬가 보여요.", "You have to keep track of position to ever see the pattern.")},
        {"svg": P3, "hero": True, "alt": ("작은 점선 창이 원본 사진 위를 훑고 지나가며 작은 무늬 지도를 만들어냄", "A small dashed window scans across the original photo, producing a small pattern map"),
         "caption": ("작은 창을 조금씩 옮기며 국소 무늬를 찾아요.", "A small window slides bit by bit, finding local patterns."),
         "small": ("이렇게 찾은 무늬들을 쌓아 올려서, 결국 전체를 이해해요.", "Stacking up what it finds this way, it eventually understands the whole picture."),
         "tricks": (4, [
             (SLIDE_I, ("작은 창으로 훑기", "Slide a small window"), ("한 칸씩 옮기며 무늬를 찾아요", "nudging one cell at a time, hunting for a pattern"), "calm"),
             (POOL_I, ("중요한 것만 남기기", "Keep only what matters"), ("가장 강한 신호만 남겨요(풀링)", "keeping only the strongest signal (pooling)")),
             (LAYER_I, ("여러 겹 쌓기", "Stack several layers"), ("작은 무늬가 모여 큰 무늬가 돼요", "small patterns build into bigger ones"), "warm"),
             (CLASSIFY_I, ("마지막에 분류하기", "Classify at the end"), ("쌓인 무늬로 최종 판정을 내려요", "making the final call from everything stacked up")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦CNN이 하는 네 단계|FOUR STAGES OF A CNN⟧",
                 ("⟦합성곱(Convolution) — 작은 창으로 국소 무늬를 찾음|convolution — a small window finds local patterns⟧",
                  "⟦활성화(Activation) — 찾은 무늬 중 의미 있는 것만 살림|activation — keeps only the patterns that matter⟧",
                  "⟦풀링(Pooling) — 지도를 줄여 가장 강한 신호만 남김|pooling — shrinks the map, keeping the strongest signal⟧",
                  "⟦완전연결층(Fully Connected) — 쌓인 무늬로 최종 분류|fully connected — makes the final classification from it all⟧"), 1.0)),
         "alt": ("합성곱·활성화·풀링·완전연결층 네 단계를 적은 표", "A board listing convolution, activation, pooling, and fully connected as four stages"),
         "caption": ("이 네 단계를 여러 번 반복해 쌓아요.", "These four stages repeat, stacked layer upon layer."),
         "small": ("층이 깊어질수록, 점·선 같은 작은 무늬가 사과 모양 같은 큰 무늬로 자라요.", "Layer by layer, tiny patterns like dots and lines grow into bigger ones, like the shape of an apple.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
                 + pixel_grid(100, 90, 6, 6, 22, seed=5) + label(190, 250, "⟦사진·무늬에 강해요|strong with photos and patterns⟧", 11, "var(--ink)")
                 + person(570, 150, s=0.75, face=FROWN, **OPERATOR)
                 + label(570, 250, "⟦그래도 사람처럼 '이해'하는 건 아니에요|still doesn't 'understand' the way a person does⟧", 11, "var(--bad)")
                 + label(380, 282, "⟦국소 무늬만 본다는 성질 탓에, 몇 점만 살짝 바꿔도 속아 넘어가요|because it only reads local patterns, a few nudged dots can still fool it⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 픽셀 격자 사진과 무늬에 강하다는 설명. 오른쪽: 조작원이 사람처럼 이해하는 건 아니라고 말하며 적대적 공격 페이지로 연결됨", "Left: a pixel grid with a note that it's strong with photos. Right: the operator notes it still doesn't understand like a person does, linking to the adversarial attack page"),
         "caption": ("사진·무늬엔 강하지만, '이해'하는 건 아니에요.", "Strong with photos and patterns — but it doesn't truly understand."),
         "small": ("그래서 적대적 공격 같은 미세 조작에 여전히 흔들려요.", "Which is exactly why it still falls for things like adversarial attacks.")},
    ],
    "summary": (("<b>CNN</b> = 사진을 <b>작은 창으로 조금씩</b> 훑으며 <b>국소 무늬</b>를 찾고, 그걸 쌓아 올려 전체를 이해하는 신경망.",
                 "<b>A CNN</b> = a neural network that scans a photo through a <b>small window, bit by bit</b>, finding <b>local patterns</b> and stacking them into the whole picture."),
                ("CNN(Convolutional Neural Network, 합성곱 신경망)은 작은 필터(커널)를 입력 전체에 슬라이딩하며 국소적인 무늬(엣지, 색 패치 등)를 찾아내는 합성곱 연산을 핵심으로 하는 신경망이에요. 합성곱→활성화→풀링을 여러 층 쌓으면서, 얕은 층은 단순한 무늬를, 깊은 층은 복잡한 모양을 인식하게 돼요. 이미지·영상 분류에서 특히 강력하지만, 픽셀 단위 패턴에 의존하는 특성 때문에 적대적 예제 같은 미세 조작에는 여전히 취약해요.",
                 "A CNN (Convolutional Neural Network) is built around the convolution operation: sliding a small filter (kernel) across the whole input to find local patterns — edges, color patches, and the like. Stacking convolution, activation, and pooling across many layers lets shallow layers recognize simple patterns while deeper layers recognize more complex shapes. CNNs are especially strong at image and video classification, but because they rely on pixel-level patterns, they remain vulnerable to subtle perturbations like adversarial examples.")),
    "glossary": [
        ("CNN", "CNN", ("작은 창으로 조금씩 살펴보는 눈.", "The eye that scans through a small window, bit by bit."), ("합성곱이라는 연산이 핵심이에요.", "Built around the convolution operation.")),
        ("합성곱", "Convolution", ("작은 필터를 조금씩 옮기며 훑는 연산.", "The operation of sliding a small filter bit by bit."), ("국소 무늬를 찾아내는 핵심 동작이에요.", "The core move that hunts down local patterns.")),
        ("필터(커널)", "Filter (kernel)", ("무늬를 찾는 작은 점선 창.", "The small dashed window that hunts for a pattern."), ("엣지·색 패치 같은 서로 다른 무늬를 찾는 필터가 여러 개 있어요.", "Many different filters exist, each hunting a different kind of pattern.")),
        ("특징맵", "Feature map", ("무늬가 있던 자리만 밝게 남은 작은 지도.", "The small map where only pattern-found spots stay bright."), ("합성곱 한 번이 끝나면 나오는 결과물이에요.", "What comes out after one pass of convolution.")),
        ("풀링", "Pooling", ("지도를 줄여 가장 강한 신호만 남기는 것.", "Shrinking the map, keeping only the strongest signal."), ("계산량을 줄이고, 작은 위치 차이에 덜 흔들리게 해요.", "Cuts computation and makes it less rattled by small shifts in position.")),
        ("층(레이어)", "Layer", ("작은 무늬가 쌓여 큰 무늬가 되는 단계.", "The stage where small patterns build into bigger ones."), ("얕은 층은 단순하게, 깊은 층은 복잡하게 봐요.", "Shallow layers see simply; deep layers see complexity.")),
        ("완전연결층", "Fully connected layer", ("쌓인 무늬를 모아 최종 분류를 내리는 층.", "The layer that gathers everything stacked up and makes the final call."), ("CNN의 맨 끝에서 분류함을 정해요.", "Sits at the very end of a CNN, deciding the bin.")),
        ("적대적 예제", "Adversarial example", ("픽셀 무늬만 보는 약점을 파고드는 공격.", "An attack that exploits the weakness of reading pixel patterns alone."), ('CNN이 여전히 이것에 흔들리는 이유예요. → <a href="advattack-ko.html">작물에 몰래 붙인 가짜 점무늬</a>', "Exactly why a CNN still falls for this. → <a href=\"advattack-en.html\">The Fake Dot Pattern Snuck Onto the Produce</a>")),
    ],
}
