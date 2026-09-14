from _draw import *
from _world import *


def arrow(x1, y1, x2, y2, color="var(--muted)"):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{x2 - 10} {y2 - 6} L{x2} {y2} L{x2 - 10} {y2 + 6}" stroke="{color}" stroke-width="3" fill="none"/>')


def receipt(x, y, w=70, h=80, total="12,800", tiny=False):
    """영수증 사진. tiny=True 면 숫자를 아주 작게."""
    fs = 7 if tiny else 10
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{PAPER}" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M{x + 10} {y + 16} h{w - 20} M{x + 10} {y + 28} h{w - 28} M{x + 10} {y + 40} h{w - 24} M{x + 10} {y + 52} h{w - 30}" stroke="{PAPER_INK}" stroke-width="2" stroke-linecap="round"/>'
            + label(x + w / 2, y + h - 10, f"⟦{total}|{total}⟧", fs, PAPER_INK))


def bean_grid(x, y, cols=4, rows=3, gap=28, s=0.5):
    return "".join(bean(x + c * gap, y + r * gap, s) for r in range(rows) for c in range(cols))


# 1. 손님이 영수증 사진을 내밀며 "얼마야?" — 글만 읽는 앵무새는 사진을 못 봐요
P1 = svg(300, sky(300) + perch(200, 200, 140) + parrot(200, 160, 1.1, mood="sweat", talk=True)
         + bubble_parrot(90, 30, 220, 40, "⟦글자만 보여요… 사진은 못 봐요|I only read words… no photos⟧", 11)
         + receipt(430, 130) + label(465, 235, "⟦영수증 사진|receipt photo⟧", 11, "var(--muted)")
         + person(520, 120, s=0.9, face=EYES, **GUEST) + bubble(430, 30, 260, 40, "⟦이 영수증, 다 해서 얼마야?|this receipt — what is the total?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦사진을 내밀면 앵무새는 눈을 감은 것 같아요|hold up a photo and the parrot might as well be blind⟧", 13, "var(--ink)"))

# 2. 왜: 앵무새는 콩(글)만 먹는 새였어요 — 그림은 콩이 아님
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(110, 150, 1.0, mood="think") + label(110, 245, "⟦콩만 먹는 새였어요|a bird that only ate beans⟧", 12, "var(--muted)")
         + beans(230, 120, ("⟦영수증|receipt⟧", "⟦사진|photo⟧", "⟦…|…⟧"), 1.0, 60)
         + receipt(430, 90, 90, 70, "12,800") + '<path d="M425 85 L525 165 M525 85 L425 165" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + label(475, 185, "⟦콩이 아니에요|not a bean⟧", 12, "var(--bad)")
         + note(560, 50, 170, 120, "⟦먹을 수 있는 것|CAN EAT⟧", ("⟦글자 콩 ✓|word beans ✓⟧", "⟦그림 ×|pictures ×⟧", "⟦소리 ×|sounds ×⟧"), 1.0)
         + label(440, 225, "⟦사진 속 숫자는 콩으로 들어오지 않아요|the numbers in the photo never become beans⟧", 12, "var(--ink)")
         + label(380, 282, "⟦앵무새 부리는 콩 모양이에요 — 사진은 그대로는 못 먹어요|the beak is shaped for beans — a photo will not fit as it is⟧", 12, "var(--bad)"))

# 3. 멀티모달 = 그림·소리도 콩으로 바꿔 먹는 앵무새 (hero)
P3 = svg(360, sky(360)
         + receipt(50, 90, 100, 80) + label(100, 195, "⟦사진|photo⟧", 11, "var(--muted)")
         + arrow(160, 130, 200, 130)
         + bean_grid(220, 100, 4, 3, 30, 0.5) + label(265, 195, "⟦콩 수백 개|hundreds of beans⟧", 11, "var(--muted)")
         + arrow(335, 130, 380, 130)
         + perch(440, 240, 150) + parrot(440, 200, 1.4, talk=True)
         + bubble_parrot(330, 40, 250, 44, "⟦다 해서 12,800원이에요|the total is 12,800 won⟧", 12)
         + '<path d="M60 250 h14 l16 -12 v34 l-16 -12 h-14z" fill="var(--stone-dark)"/><path d="M100 248 q8 12 0 24 M112 242 q14 18 0 36" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + arrow(135, 260, 175, 260) + beans(200, 260, ("⟦얼|how⟧", "⟦마|much⟧", "⟦야|is it⟧"), 0.7, 30)
         + label(160, 300, "⟦소리도 콩으로 바꿔요|sounds become beans too⟧", 11, "var(--muted)")
         + person(620, 140, s=0.9, face=SMILE, **GUEST) + label(655, 268, "⟦손님|guest⟧", 11, "var(--muted)")
         + note(600, 30, 140, 90, "⟦먹는 것|EATS⟧", ("⟦글 ✓ 그림 ✓|words ✓ pictures ✓⟧", "⟦소리 ✓|sounds ✓⟧"), 0.95)
         + label(380, 340, "⟦멀티모달 = 그림과 소리도 콩으로 바꿔 먹는 앵무새|multimodal is a parrot that turns pictures and sounds into beans too⟧", 13, "var(--ink)", cls="d"))

# 4. 작동 디테일: 그림은 조각조각 콩으로, 소리도 콩으로, 그림 속 글자도
P4 = svg(320, sky(320)
         + f'<rect x="40" y="50" width="120" height="90" rx="4" fill="#FCE3B0" stroke="#C9A86A" stroke-width="3"/><circle cx="130" cy="78" r="14" fill="#E9B44C"/><rect x="40" y="105" width="120" height="35" fill="#5B9BD5"/>'
         + '<path d="M70 50 v90 M100 50 v90 M130 50 v90 M40 80 h120 M40 110 h120" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.6"/>'
         + label(100, 165, "⟦조각조각 나눠요|cut into patches⟧", 11, "var(--muted)")
         + arrow(170, 95, 205, 95) + bean_grid(225, 62, 5, 4, 26, 0.42) + label(275, 165, "⟦조각마다 콩 몇 개|a few beans per patch⟧", 11, "var(--muted)")
         + tray(30, 200, 330, 56) + "".join(bean(60 + i * 34, 228, 0.6) for i in range(9))
         + label(195, 282, "⟦그림 한 장 = 콩 수백 개 → 쟁반이 금방 차요|one picture = hundreds of beans → the tray fills fast⟧", 11, "var(--ink)")
         + '<path d="M420 80 h14 l16 -12 v34 l-16 -12 h-14z" fill="var(--stone-dark)"/><path d="M460 78 q8 12 0 24 M472 72 q14 18 0 36" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + arrow(495, 90, 535, 90) + beans(565, 90, ("⟦안|hel⟧", "⟦녕|lo⟧"), 0.8, 40) + label(590, 130, "⟦소리 → 콩|sound → beans⟧", 11, "var(--muted)")
         + f'<rect x="420" y="160" width="100" height="60" rx="4" fill="{PAPER}" stroke="#C9A86A" stroke-width="3"/>' + label(470, 196, "⟦OPEN 9-6|OPEN 9-6⟧", 13, PAPER_INK, cls="d")
         + arrow(530, 190, 565, 190) + beans(595, 190, ("⟦OPEN|OPEN⟧", "⟦9-6|9-6⟧"), 0.8, 44)
         + label(590, 235, "⟦그림 속 글자도 콩이 돼요|words in a picture become beans too⟧", 11, "var(--muted)")
         + label(580, 282, "⟦대답을 그림으로 하는 건 다른 앵무새 일이에요|answering with a picture is another parrot\'s job⟧", 11, "var(--ink)"))

# 5. 깨지는 곳: 보는 게 아니라 콩으로 바꾼 걸 이어 붙이는 것 — 작은 글자·숫자는 틀리기 쉬움
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + parrot(100, 150, 1.0, talk=True) + bubble_parrot(15, 35, 190, 40, "⟦3월 막대가 제일 높아요|the March bar is tallest⟧", 11)
         + f'<rect x="210" y="70" width="150" height="110" rx="6" fill="{PAPER}" stroke="#C9A86A" stroke-width="3"/>'
         + '<rect x="230" y="130" width="28" height="40" fill="#5B8DEF"/><rect x="272" y="105" width="28" height="65" fill="#5B8DEF"/><rect x="314" y="82" width="28" height="88" fill="var(--good)"/>'
         + label(244, 195, "⟦1월|Jan⟧", 10, "var(--muted)") + label(286, 195, "⟦2월|Feb⟧", 10, "var(--muted)") + label(328, 195, "⟦3월|Mar⟧", 10, "var(--muted)")
         + label(190, 245, "⟦큰 모양은 잘 봐요|big shapes it reads well⟧", 11, "var(--ink)")
         + parrot(470, 150, 1.0, color=PARROT_BAD, talk=True) + bubble_parrot(400, 40, 200, 40, "⟦다 해서 12,300원|the total is 12,300⟧", 11, bad=True)
         + receipt(600, 70, 100, 110, "12,800", tiny=True) + label(650, 200, "⟦(진짜는 12,800)|(really 12,800)⟧", 11, "var(--bad)")
         + label(570, 245, "⟦작은 글자·숫자는 틀리기 쉬워요|small print and digits go wrong easily⟧", 11, "var(--ink)")
         + label(380, 300, "⟦보는 게 아니라, 콩으로 바꾼 걸 이어 붙이는 거예요 — 숫자는 사람이 확인해요|it does not see — it continues beans made from the picture; a person checks the numbers⟧", 12, "var(--ink)", cls="d"))

PHOTO_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FCE3B0" stroke="#C9A86A" stroke-width="3"/><circle cx="44" cy="24" r="6" fill="#E9B44C"/><path d="M10 48 l14 -16 l10 10 l8 -8 l12 14z" fill="#2E7D6B"/>')
TRAYFULL_I = icon(f'<rect x="4" y="34" width="56" height="20" rx="6" fill="var(--stone)"/>' + "".join(f'<ellipse cx="{12 + i * 10}" cy="{30 - (i % 2) * 8}" rx="6" ry="4" fill="{BEAN}"/>' for i in range(5)) + '<path d="M50 12 l6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
OCR_I = icon('<rect x="8" y="10" width="48" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="38" text-anchor="middle" font-size="14" font-weight="700" fill="#142033">9-6</text><circle cx="46" cy="46" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M52 52 l6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
BRUSH_I = icon('<path d="M14 50 l24 -24" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/><path d="M38 26 l10 -10 l6 6 l-10 10z" fill="var(--accent)"/><path d="M8 56 q6 -10 12 -4" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "multimodal", "order": 23,
    "title": ("그림도 보는 앵무새", "The Parrot That Sees Pictures"),
    "h1": ("<em>멀티모달</em>이 뭐예요?", "What is <em>Multimodal</em>?"),
    "sub": ("멀티모달 모델을 그림과 소리까지 콩으로 바꿔 먹는 앵무새 이야기로 풀어봤어요.",
            "Multimodal models, told as a story about a parrot that turns pictures and sounds into beans too."),
    "panels": [
        {"svg": P1, "alt": ("손님이 영수증 사진을 들고 얼마냐고 묻고, 횃대 위 앵무새는 땀을 흘리며 글자만 보인다고 말함", "A guest holds up a receipt photo and asks the total; the parrot on the perch sweats and says it only reads words"),
         "caption": ("손님이 영수증 사진을 내밀어요. 글만 읽는 앵무새는 사진을 못 봐요.", "The guest holds up a receipt photo. A words-only parrot cannot see it."),
         "small": ("표도, 그래프도, 사진도 다 그래요. 앵무새는 눈을 감은 것 같아요.", "Tables, charts, photos — all the same. The parrot might as well be blind.")},
        {"svg": P2, "alt": ("생각하는 앵무새, 영수증 사진 위에 빨간 ×, '먹을 수 있는 것' 쪽지에 글자 콩 ✓, 그림 ×, 소리 ×", "A thinking parrot; a red × over a receipt photo; a note lists word beans ✓, pictures ×, sounds ×"),
         "caption": ("왜냐면 앵무새는 콩만 먹는 새였거든요. 그림은 콩이 아니에요.", "Because the parrot was a bird that only ate beans. A picture is not a bean."),
         "small": ('앵무새 부리는 <a href="token-ko.html">콩</a> 모양이에요. 사진 속 숫자는 콩으로 들어오지 않으니, 있는지도 몰라요.',
                   'The beak is shaped for <a href="token-en.html">beans</a>. The numbers in the photo never become beans, so the parrot does not even know they are there.')},
        {"svg": P3, "hero": True, "alt": ("영수증 사진이 콩 격자로 바뀌어 앵무새에게 들어가고, 앵무새가 '다 해서 12,800원'이라고 답함. 아래엔 스피커 소리가 콩 세 개로 바뀜. 손님과 '먹는 것: 글·그림·소리' 쪽지", "A receipt photo turns into a grid of beans that go into the parrot, which answers the total is 12,800 won; below, a speaker sound turns into three beans; a guest and a note listing words, pictures, sounds"),
         "caption": ("멀티모달은 그림과 소리도 콩으로 바꿔 먹는 앵무새예요.", "Multimodal is a parrot that turns pictures and sounds into beans too."),
         "small": ('사진 한 장이 콩 수백 개가 돼요. 그러면 글 콩이랑 똑같이 이어 붙일 수 있어요 — 사진을 보고 답하는 것처럼요.',
                   'One photo becomes hundreds of beans. Then it can continue them just like word beans — as if it were looking at the photo.'),
         "tricks": (4, [
             (PHOTO_I, ("사진·표·그래프 그대로 줘요", "Hand over the photo as is"), ("옮겨 적지 말고 보여줘요", "show it, do not retype it"), "calm"),
             (TRAYFULL_I, ("그림은 콩이 많아요", "Pictures are many beans"), ("쟁반을 많이 써요", "they fill up the tray"), "warm"),
             (OCR_I, ("그림 속 글자도 읽어요", "Reads words in pictures"), ("간판, 표, 손글씨", "signs, tables, handwriting"), "calm"),
             (BRUSH_I, ("그리는 앵무새는 따로", "Drawing is another parrot"), ("안개에서 그림 꺼내기", "pulling pictures from fog"), "warm"),
         ])},
        {"svg": P4, "alt": ("그림을 점선으로 조각내 콩 격자로 바꾸고, 쟁반에 콩이 가득 참. 오른쪽엔 스피커 소리가 콩 두 개로, 'OPEN 9-6' 간판 사진이 콩 두 개로 바뀜", "A picture is cut into dashed patches and becomes a bean grid; a tray is full of beans. On the right a speaker sound becomes two beans and an OPEN 9-6 sign photo becomes two beans"),
         "caption": ("그림은 조각조각 콩으로 바뀌어요. 소리도, 그림 속 글자도요.", "A picture becomes beans patch by patch. So do sounds, and words inside pictures."),
         "small": ('그림 한 장이 콩 수백 개라서 <a href="context-ko.html">쟁반</a>이 금방 차요. 대답을 그림으로 하는 건 <a href="diffusion-ko.html">다른 앵무새</a> 일이에요.',
                   'One picture is hundreds of beans, so the <a href="context-en.html">tray</a> fills fast. Answering with a picture is <a href="diffusion-en.html">another parrot\'s</a> job.')},
        {"svg": P5, "alt": ("왼쪽 초록: 앵무새가 막대그래프를 보고 3월이 제일 높다고 맞게 말함. 오른쪽 빨강: 빨간 앵무새가 작은 글씨 영수증을 보고 12,300원이라고 함 — 진짜는 12,800", "Left, green: the parrot reads a bar chart and correctly says March is tallest. Right, red: a red parrot reads a small-print receipt and says 12,300 — really 12,800"),
         "caption": ("큰 모양은 잘 봐요. 작은 글자와 숫자는 틀리기 쉬워요.", "Big shapes it reads well. Small print and digits go wrong easily."),
         "small": ('보는 게 아니라 콩으로 바꾼 걸 이어 붙이는 거라, 콩이 흐리면 <a href="hallucination-ko.html">그럴듯하게</a> 채워요. 영수증 숫자는 사람이 확인해요.',
                   'It does not see — it continues beans made from the picture, and when the beans are blurry it fills in <a href="hallucination-en.html">plausibly</a>. A person checks the receipt numbers.')},
    ],
    "summary": (("<b>멀티모달</b> = 그림·소리도 <b>콩으로 바꿔 먹는 앵무새</b>. 사진 한 장은 <b>콩 수백 개</b>라 쟁반이 금방 차고, 작은 글자·숫자는 사람이 확인해요.",
                 "<b>Multimodal</b> = a parrot that <b>turns pictures and sounds into beans</b> too. One photo is <b>hundreds of beans</b>, so the tray fills fast, and a person checks small print and digits."),
                ("Multimodal model. 텍스트 외에 이미지·오디오·비디오를 입력(때로 출력)으로 다루는 모델이에요. 이미지는 패치 단위로 이미지 토큰이 되어 컨텍스트 창을 크게 차지하고, 음성은 STT 로 토큰이 돼요. 이미지 생성은 보통 별도의 디퓨전 모델이 맡아요.",
                 "A model that takes images, audio, or video as input (sometimes output) besides text. Images become image tokens patch by patch and use a lot of the context window; speech becomes tokens through STT. Image generation is usually a separate diffusion model.")),
    "glossary": [
        ("멀티모달", "Multimodal", ("그림도 보는 앵무새.", "The parrot that sees pictures."), ("글·그림·소리를 한 앵무새가 다 콩으로 먹어요.", "Words, pictures, and sounds all become beans for one parrot.")),
        ("비전 모델", "Vision model", ("그림 부리.", "The picture beak."), ("그림을 콩으로 바꾸는 부분이에요. 큰 앵무새에 붙어 있어요.", "The part that turns pictures into beans. It sits attached to the big parrot.")),
        ("이미지 토큰", "Image tokens", ("그림 콩.", "Picture beans."), ('사진 한 장이 콩 수백~수천 개. 그래서 쟁반이 금방 차요. → <a href="context-ko.html">쟁반</a>', 'One photo is hundreds to thousands of beans, so the tray fills fast. → <a href="context-en.html">the tray</a>')),
        ("음성 인식 · 합성", "Speech-to-text · text-to-speech", ("소리 → 콩, 콩 → 소리.", "Sound → beans, beans → sound."), ("STT 는 말소리를 콩으로, TTS 는 콩을 말소리로 바꿔요.", "STT turns speech into beans; TTS turns beans back into speech.")),
        ("OCR 과의 차이", "Difference from OCR", ("글자만 뽑기 vs 그림째 먹기.", "Pulling out letters vs eating the whole picture."), ("OCR 은 글자만 떼어내요. 멀티모달은 글자·모양·자리를 한꺼번에 봐요.", "OCR peels off only the letters. Multimodal reads letters, shapes, and layout together.")),
        ("문서 이해", "Document understanding", ("표·영수증·계약서 읽기.", "Reading tables, receipts, contracts."), ("칸이 어디에 있는지까지 봐요. 그래도 숫자는 사람이 확인해요.", "It reads where each cell sits. Still, a person checks the numbers.")),
        ("비디오 입력", "Video input", ("그림을 여러 장 이어서.", "Many pictures in a row."), ("영상은 사진을 여러 장 뽑아 콩으로 바꿔요. 콩이 아주 많아져요.", "A video becomes many picture frames turned into beans — a lot of beans.")),
        ("이미지 생성", "Image generation", ("그리는 앵무새.", "The drawing parrot."), ('보는 것과 그리는 것은 다른 일이에요. → <a href="diffusion-ko.html">안개에서 그림 꺼내기</a>', 'Seeing and drawing are different jobs. → <a href="diffusion-en.html">pulling pictures from fog</a>')),
    ],
}
