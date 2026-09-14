from _draw import *
from _world import *

PAINTER = dict(hat="#B5382C", shirt="#6E8199")  # 화가 (디퓨전 모델)
BRUSH = '<path d="M56 70 l16 -20" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/><path d="M72 50 l6 -8 l6 5 l-6 8z" fill="var(--accent)"/>'


def arrow(x1, y1, x2, y2, color="var(--muted)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{x2 - 10} {y2 - 6} L{x2} {y2} L{x2 - 10} {y2 + 6}" stroke="{color}" stroke-width="3" fill="none"/>')


def canvas(x, y, w=120, h=100, fog=1.0, inner=""):
    """종이 한 장. fog 1.0 = 안개(잡음)만, 0.0 = 또렷한 노을 바다. inner 로 다른 그림을 넣을 수 있다."""
    scene = inner or (f'<rect width="{w}" height="{h}" fill="#F3B27A"/><rect y="{h * 0.55:.0f}" width="{w}" height="{h * 0.45:.0f}" fill="#3F6FD1"/>'
                      f'<circle cx="{w * 0.62:.0f}" cy="{h * 0.5:.0f}" r="{h * 0.16:.0f}" fill="#E9B44C"/><rect y="{h * 0.5:.0f}" width="{w}" height="{h * 0.05:.0f}" fill="#7B3FA0"/>')
    noise = "".join(f'<rect x="{(i * 37) % (w - 10)}" y="{(i * 53) % (h - 10)}" width="10" height="10" fill="{"#9AA6B8" if i % 3 else "#5A6678"}"/>' for i in range(int(70 * fog)))
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="4" fill="{PAPER}"/>'
            f'<g opacity="{1 - fog:.2f}">{scene}</g><g opacity="{min(1, fog + 0.15):.2f}">{noise}</g>'
            f'<rect width="{w}" height="{h}" rx="4" fill="none" stroke="#C9A86A" stroke-width="3"/></g>')


# 1. 손님이 "노을 지는 바다 그려 줘" — 말하는 앵무새는 그림을 못 그려요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, mood="sweat", talk=True)
         + bubble_parrot(90, 30, 220, 40, "⟦말은 할 수 있는데… 그림은…|I can talk… but draw?⟧", 12)
         + canvas(425, 130, 80, 80, 0.0, f'<rect width="80" height="80" fill="{PAPER}"/>') + label(465, 178, "⟦?|?⟧", 26, PAPER_INK, cls="d") + label(465, 235, "⟦빈 종이|blank paper⟧", 11, "var(--muted)")
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(430, 30, 260, 40, "⟦노을 지는 바다를 그려 줘|draw me a sunset over the sea⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦말하는 앵무새는 그림을 못 그려요|a talking parrot cannot draw⟧", 13, "var(--ink)"))

# 2. 왜: 그림은 콩을 한 줄로 이어 붙이는 게 아니라, 점 백만 개를 한꺼번에 정하는 일
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(90, 195, 0.9, mood="sweat")
         + beans(160, 90, ("⟦노을|sun⟧", "⟦지는|set⟧", "⟦바다|sea⟧", "⟦…|…⟧"), 1.0, 44) + label(230, 135, "⟦말: 콩을 한 줄로|words: beans in a row⟧", 12, "var(--ink)")
         + label(380, 130, "⟦다른 일이에요|a different job⟧", 12, "var(--bad)")
         + "".join(f'<circle cx="{460 + c * 18}" cy="{60 + r * 18}" r="6" fill="{("#F3B27A", "#E9B44C", "#3F6FD1", "#9AA6B8")[(r * 3 + c) % 4]}"/>' for r in range(7) for c in range(13))
         + label(568, 200, "⟦그림: 점 백만 개를 한꺼번에|a picture: a million dots at once⟧", 12, "var(--ink)")
         + label(568, 225, "⟦하나씩 고르다간 밤을 새워요|picking them one by one takes all night⟧", 11, "var(--muted)")
         + label(380, 282, "⟦다음 콩 고르는 새는 점 백만 개를 한꺼번에 못 정해요|a next-bean bird cannot set a million dots at once⟧", 12, "var(--bad)"))

# 3. 디퓨전 = 안개 가득한 종이에서 조금씩 안개를 걷어 그림을 꺼내는 화가 (hero)
P3 = svg(360, sky(360)
         + note(30, 40, 150, 100, "⟦쪽지|NOTE⟧", ("⟦노을 지는 바다|sunset over the sea⟧", "⟦보랏빛 하늘|purple sky⟧"))
         + parrot(90, 230, 0.8, talk=True) + label(90, 292, "⟦앵무새가 쪽지를 다듬어요|the parrot tidies the note⟧", 11, "var(--muted)")
         + arrow(185, 90, 215, 90)
         + person(215, 100, s=0.9, face=SMILE, extra=BRUSH, **PAINTER) + label(250, 228, "⟦화가|painter⟧", 11, "var(--muted)")
         + canvas(320, 60, 120, 110, 1.0) + label(380, 195, "⟦안개|fog⟧", 11, "var(--muted)")
         + arrow(445, 115, 470, 115)
         + canvas(475, 60, 120, 110, 0.5) + label(535, 195, "⟦조금 걷음|a bit cleared⟧", 11, "var(--muted)")
         + arrow(600, 115, 625, 115)
         + canvas(630, 60, 120, 110, 0.0) + label(690, 195, "⟦다 걷음|all cleared⟧", 11, "var(--muted)")
         + label(520, 250, "⟦조금씩 안개를 걷어요 — 쪽지가 어떤 그림인지 알려줘요|wipe the fog bit by bit — the note says which picture⟧", 12, "var(--ink)")
         + label(380, 340, "⟦디퓨전 = 안개 가득한 종이에서 조금씩 안개를 걷어 그림을 꺼내는 화가|diffusion is a painter that pulls a picture out of a fog-filled paper, bit by bit⟧", 13, "var(--ink)", cls="d"))

# 4. 작동 디테일: 안개 → 흐릿 → 또렷 4단계, 걸음 수, 씨앗
P4 = svg(320, sky(320)
         + "".join(canvas(30 + i * 185, 40, 140, 120, f) + label(100 + i * 185, 183, t, 11, "var(--muted)")
                   for i, (f, t) in enumerate(((1.0, "⟦0걸음|step 0⟧"), (0.66, "⟦10걸음|step 10⟧"), (0.33, "⟦20걸음|step 20⟧"), (0.0, "⟦30걸음|step 30⟧"))))
         + arrow(175, 100, 210, 100) + arrow(360, 100, 395, 100) + arrow(545, 100, 580, 100)
         + label(380, 222, "⟦걸음이 많을수록 또렷해요 — 그만큼 느려요|more steps, sharper — and slower⟧", 12, "var(--ink)")
         + bean(150, 262, 0.8, "#2E7D6B", "⟦42|42⟧") + label(270, 267, "⟦같은 씨앗 번호 = 같은 그림|same seed number = same picture⟧", 11, "var(--muted)")
         + "".join(canvas(470 + i * 40, 248, 32, 26, 0.0) for i in range(3)) + '<circle cx="526" cy="258" r="9" fill="var(--good)"/>' + label(526, 262, "⟦✓|✓⟧", 11, "#FFF")
         + label(660, 267, "⟦여러 장 뽑아 고르기|draw several, pick one⟧", 11, "var(--muted)")
         + label(380, 300, "⟦걸음 수, 씨앗 번호, 뽑는 장수 — 세 개를 돌려 가며 써요|steps, seed number, how many to draw — three knobs to play with⟧", 12, "var(--muted)"))

# 5. 깨지는 곳: 화가는 본 그림들의 '느낌'을 배운 것 — 글자·손가락 수는 자주 틀림 + 남의 그림체(저작권)
HAND = ('<circle cx="70" cy="92" r="16" fill="#E8C9A8"/>' + "".join(f'<path d="M{58 + i * 5} 78 l{-6 + i * 2} -20" stroke="#E8C9A8" stroke-width="6" stroke-linecap="round"/>' for i in range(6)))
SIGN = f'<rect width="140" height="120" fill="#F3B27A"/><rect x="20" y="20" width="100" height="36" rx="4" fill="{PAPER}"/><text x="70" y="45" text-anchor="middle" font-size="16" font-weight="700" fill="#142033">OPFN</text>' + HAND
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + canvas(40, 45, 140, 120, 0.0) + person(200, 80, s=0.8, face=SMILE, extra=BRUSH, **PAINTER)
         + label(150, 195, "⟦분위기·색·구도는 잘해요|mood, color, layout it does well⟧", 11, "var(--ink)")
         + label(190, 245, "⟦본 그림들의 느낌을 배웠거든요|it learned the feel of the pictures it saw⟧", 11, "var(--muted)")
         + canvas(410, 45, 140, 120, 0.0, SIGN) + label(480, 190, "⟦글자가 이상해요 · 손가락 여섯 개|odd letters · six fingers⟧", 11, "var(--bad)")
         + books(665, 160, 4, 0.8) + label(665, 182, "⟦본 그림 더미|the pile it saw⟧", 11, "var(--muted)")
         + label(570, 245, "⟦남의 그림체를 통째로 배웠을 수도 있어요 — 저작권|it may have learned someone\'s whole style — copyright⟧", 11, "var(--ink)")
         + label(380, 300, "⟦화가는 느낌을 배웠지, 사실을 배운 게 아니에요 — 정확한 건 사람이 확인해요|the painter learned the feel, not the facts — a person checks the exact parts⟧", 12, "var(--ink)", cls="d"))

NOTE_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="12" rx="4" fill="#C9A86A"/><path d="M20 30 h24 M20 38 h24 M20 46 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
PICK_I = icon('<rect x="6" y="20" width="16" height="20" rx="2" fill="#F3B27A" stroke="#C9A86A" stroke-width="2"/><rect x="24" y="20" width="16" height="20" rx="2" fill="#F3B27A" stroke="#C9A86A" stroke-width="2"/><rect x="42" y="20" width="16" height="20" rx="2" fill="#F3B27A" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="48" r="8" fill="var(--good)"/><path d="M28 48 l3 3 l5 -6" stroke="#FFF" stroke-width="2.5" fill="none"/>')
STEP_I = icon('<path d="M8 52 h12 v-12 h12 v-12 h12 v-12 h12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="50" cy="14" r="5" fill="#E9B44C"/>')
SEED_I = icon(f'<ellipse cx="32" cy="34" rx="18" ry="12" fill="#2E7D6B"/><text x="32" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="#FFF">42</text><path d="M32 22 q0 -10 8 -12" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "diffusion", "order": 24,
    "title": ("안개에서 그림 꺼내기", "Pulling a Picture Out of the Fog"),
    "h1": ("<em>디퓨전 모델</em>이 뭐예요?", "What is a <em>Diffusion Model</em>?"),
    "sub": ("이미지 생성 디퓨전 모델을 안개 가득한 종이에서 조금씩 안개를 걷어 그림을 꺼내는 화가 이야기로 풀어봤어요.",
            "Image-generating diffusion models, told as a story about a painter who pulls a picture out of a fog-filled paper, bit by bit."),
    "panels": [
        {"svg": P1, "alt": ("손님이 노을 지는 바다를 그려 달라고 하고, 횃대 위 앵무새는 땀을 흘리며 말은 할 수 있지만 그림은 못 그린다고 함. 물음표가 있는 빈 종이", "A guest asks for a sunset over the sea; the parrot on the perch sweats and says it can talk but not draw; a blank paper with a question mark"),
         "caption": ("손님이 그림을 그려 달래요. 말하는 앵무새는 그림을 못 그려요.", "The guest asks for a picture. A talking parrot cannot draw."),
         "small": ("노을 지는 바다를 말로는 설명하는데, 종이는 그대로 비어 있어요.", "It can describe a sunset over the sea in words, but the paper stays blank.")},
        {"svg": P2, "alt": ("땀 흘리는 앵무새 옆에 '노을 지는 바다' 콩 네 개가 한 줄로, 오른쪽엔 색 점이 격자로 가득 — 점 백만 개를 한꺼번에", "A sweating parrot beside four beans in a row reading sunset sea; on the right a grid of colored dots — a million dots at once"),
         "caption": ("왜냐면 그림은 콩을 한 줄로 잇는 게 아니라, 점 백만 개를 한꺼번에 정하는 일이거든요.", "Because a picture is not beans in a row — it is a million dots decided all at once."),
         "small": ('앵무새는 다음 <a href="token-ko.html">콩</a> 하나를 고르는 새예요. 점을 하나씩 고르다간 밤을 새워요. 그래서 다른 화가가 필요해요.',
                   'The parrot picks one next <a href="token-en.html">bean</a> at a time. Picking dots one by one would take all night. So a different painter is needed.')},
        {"svg": P3, "hero": True, "alt": ("'노을 지는 바다, 보랏빛 하늘' 쪽지가 붓을 든 화가에게 가고, 화가 앞에 종이 세 장: 안개 → 조금 걷음 → 다 걷힌 노을 바다. 아래 앵무새가 쪽지를 다듬음", "A note reading sunset over the sea, purple sky goes to a painter with a brush; three papers in front: fog → a bit cleared → a clear sunset sea. Below, the parrot tidies the note"),
         "caption": ("디퓨전은 안개 가득한 종이에서 조금씩 안개를 걷어 그림을 꺼내는 화가예요.", "Diffusion is a painter who pulls a picture out of a fog-filled paper, bit by bit."),
         "small": ('종이는 처음엔 안개(잡음)뿐이에요. 화가가 한 번 닦을 때마다 조금 또렷해지고, <a href="prompt-ko.html">쪽지</a>가 어떤 그림을 꺼낼지 알려줘요.',
                   'The paper starts as pure fog (noise). Each wipe makes it a little clearer, and the <a href="prompt-en.html">note</a> says which picture to pull out.'),
         "tricks": (4, [
             (NOTE_I, ("쪽지는 구체적으로", "Make the note specific"), ("색, 분위기, 구도까지", "color, mood, layout too"), "calm"),
             (PICK_I, ("여러 장 뽑아 골라요", "Draw several, pick one"), ("한 장에 걸지 말아요", "never bet on one"), "calm"),
             (STEP_I, ("걸음이 많으면 또렷", "More steps, sharper"), ("대신 느려요", "but slower"), "warm"),
             (SEED_I, ("같은 씨앗, 같은 그림", "Same seed, same picture"), ("번호를 적어 둬요", "write the number down"), "warm"),
         ])},
        {"svg": P4, "alt": ("종이 네 장: 0걸음 안개, 10걸음 흐릿, 20걸음 조금 또렷, 30걸음 또렷한 노을 바다. 아래엔 씨앗 42 콩과 '같은 씨앗 = 같은 그림', 작은 종이 세 장 중 하나에 ✓", "Four papers: step 0 fog, step 10 blurry, step 20 clearer, step 30 a sharp sunset sea. Below, a seed bean 42 with same seed = same picture, and three small papers with one ✓"),
         "caption": ("안개, 흐릿, 조금 또렷, 또렷 — 걸음마다 안개가 걷혀요.", "Fog, blurry, clearer, sharp — the fog lifts step by step."),
         "small": ("걸음이 많으면 또렷하지만 느려요. 씨앗 번호가 같으면 같은 그림이 나오고, 여러 장 뽑아서 제일 나은 걸 골라요.", "More steps means sharper but slower. The same seed number gives the same picture, and you draw several to pick the best.")},
        {"svg": P5, "alt": ("왼쪽 초록: 화가가 분위기 좋은 노을 바다를 그림. 오른쪽 빨강: 간판 글자가 OPFN 으로 틀리고 손가락이 여섯 개, 옆에 본 그림 더미와 저작권 한 줄", "Left, green: the painter makes a lovely sunset sea. Right, red: a sign misspelled OPFN and a hand with six fingers, beside the pile of pictures it saw and a copyright line"),
         "caption": ("분위기와 색은 잘해요. 글자와 손가락 수는 자주 틀려요.", "Mood and color it does well. Letters and finger counts go wrong often."),
         "small": ('화가는 본 그림들의 느낌을 배웠지 사실을 배운 게 아니에요. 남의 그림체를 통째로 배웠을 수도 있어서 저작권 얘기가 따라와요. 그림을 보는 앵무새는 <a href="multimodal-ko.html">따로</a> 있어요.',
                   'The painter learned the feel of the pictures it saw, not facts. It may have learned someone\'s whole style, so copyright questions follow. The parrot that sees pictures is a <a href="multimodal-en.html">separate</a> story.')},
    ],
    "summary": (("<b>디퓨전</b> = 안개 가득한 종이에서 <b>조금씩 안개를 걷어</b> 그림을 꺼내는 화가. <b>쪽지</b>가 어떤 그림인지 알려주고, 걸음이 많을수록 또렷해요. 느낌은 잘 배웠지만 <b>글자·손가락 수</b>는 자주 틀려요.",
                 "<b>Diffusion</b> = a painter who <b>wipes the fog away bit by bit</b> to pull a picture out. The <b>note</b> says which picture, and more steps make it sharper. It learned the feel well, but <b>letters and finger counts</b> go wrong often."),
                ("Diffusion model. 순수 잡음에서 시작해 여러 스텝에 걸쳐 잡음을 제거하며 이미지를 만드는 생성 모델이에요. 프롬프트가 조건이 되고, 시드가 시작 잡음을 정해요. 학습 데이터의 분포를 배운 것이라 정확한 텍스트·해부학은 약하고, 학습 데이터 저작권 문제가 따라와요.",
                 "A generative model that starts from pure noise and removes it over many steps to form an image. The prompt is the condition and the seed sets the starting noise. It learned the distribution of its training data, so exact text and anatomy are weak, and training-data copyright questions follow.")),
    "glossary": [
        ("디퓨전 모델", "Diffusion model", ("안개 걷는 화가.", "The fog-wiping painter."), ("Stable Diffusion, DALL-E, Midjourney 가 이 화가예요.", "Stable Diffusion, DALL-E, Midjourney are this painter.")),
        ("잡음 제거", "Denoising", ("안개 한 번 닦기.", "One wipe of the fog."), ("화가가 하는 일의 전부예요. 잡음을 조금 걷고, 또 걷고.", "The whole of what the painter does: remove a little noise, then a little more.")),
        ("스텝", "Steps", ("걸음 수.", "How many wipes."), ("많으면 또렷하고 느려요. 적으면 빠르고 흐려요.", "More is sharper and slower; fewer is faster and blurrier.")),
        ("프롬프트", "Prompt", ("화가에게 주는 쪽지.", "The note for the painter."), ('구체적일수록 원하는 그림이 나와요. → <a href="prompt-ko.html">조련 쪽지</a>', 'The more specific, the closer the picture. → <a href="prompt-en.html">the trainer\'s note</a>')),
        ("시드", "Seed", ("씨앗 번호.", "The seed number."), ("시작 안개 모양을 정해요. 같은 씨앗, 같은 쪽지면 같은 그림.", "Sets the starting fog. Same seed and same note give the same picture.")),
        ("이미지 생성 vs 이해", "Generation vs understanding", ("그리는 화가 vs 보는 앵무새.", "The painter who draws vs the parrot who sees."), ('다른 일이에요. → <a href="multimodal-ko.html">그림도 보는 앵무새</a>', 'Different jobs. → <a href="multimodal-en.html">the parrot that sees pictures</a>')),
        ("인페인팅", "Inpainting", ("한 부분만 다시.", "Redo one part."), ("그림에서 고칠 곳만 안개로 덮고 다시 걷어요.", "Cover just the part to fix with fog and wipe it again.")),
        ("저작권 · 학습 데이터", "Copyright · training data", ("본 그림 더미.", "The pile of pictures it saw."), ("남의 그림으로 배웠어요. 어떤 그림체는 그대로 흉내 낼 수 있어서 논쟁이 있어요.", "It learned from other people\'s pictures. Some styles it can copy closely, which is under debate.")),
    ],
}
