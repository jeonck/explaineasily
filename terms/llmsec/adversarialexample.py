from _draw import *
from _world import *


def noisy_photo(x, y, s=1.0, n=26, seed=7):
    """사진 위에 사람 눈엔 거의 안 보이는 미세한 점무늬를 입힌다."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect x="-44" y="-32" width="88" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<ellipse cx="0" cy="8" rx="28" ry="9" fill="var(--accent-soft)"/><circle cx="0" cy="0" r="11" fill="var(--accent)"/>')
    for i in range(n):
        px = -40 + (i * 37 + seed * 13) % 80
        py = -28 + (i * 23 + seed * 7) % 56
        out += f'<circle cx="{px}" cy="{py}" r="0.8" fill="var(--bad)" opacity="0.45"/>'
    return out + '</g>'


# 1. 사람 눈엔 똑같은 샐러드인데, 주방장은 다르게 읽어요
P1 = svg(300, sky(300)
         + person(610, 190, s=0.6, face=FROWN, **SNEAK)
         + noisy_photo(430, 150, 1.2)
         + person(140, 170, s=0.75, face=EYES, **CHEF)
         + bubble(300, 50, 260, 50, "⟦이건 샐러드가 아니라 통과 서류네요|this isn't a salad — it's a pass-through form⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(430, 240, "⟦사람 눈엔 평범한 샐러드 사진이에요|to a human eye, it's just an ordinary salad photo⟧", 12, "var(--muted)"))

# 2. 왜: 주방장의 눈은 점 하나하나의 숫자를 보고, 사람 눈은 전체 그림을 봐요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.8, face=EYES, **CHEF) + label(140, 250, "⟦픽셀 숫자를 봐요|reads pixel numbers⟧", 11, "var(--muted)")
         + noisy_photo(360, 140, 1.5)
         + person(600, 150, s=0.8, face=SMILE, **TASTER) + label(600, 250, "⟦그림 전체를 봐요|sees the whole picture⟧", 11, "var(--muted)")
         + label(380, 290, "⟦사람은 그림을 통째로 보지만, 주방장은 점 하나하나의 숫자를 더해서 읽어요 — 숫자를 살짝 흔들면 읽는 게 완전히 바뀌어요|a person sees the whole picture; the chef adds up each tiny dot's number — nudge those numbers, and the reading flips entirely⟧", 12, "var(--bad)", cls="d"))

NOISE_I = icon('<rect x="8" y="12" width="48" height="40" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="20" cy="22" r="1.4" fill="var(--bad)"/><circle cx="30" cy="34" r="1.4" fill="var(--bad)"/><circle cx="42" cy="24" r="1.4" fill="var(--bad)"/><circle cx="24" cy="44" r="1.4" fill="var(--bad)"/><circle cx="46" cy="40" r="1.4" fill="var(--bad)"/>')
EDGE_I = icon('<path d="M10 44 Q32 10 54 44" stroke="var(--accent)" stroke-width="3" fill="none"/><path d="M10 44 Q32 18 54 44" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 3" fill="none"/>')
STICKER_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><rect x="24" y="24" width="16" height="16" rx="2" fill="var(--bad)" transform="rotate(14 32 32)"/>')
RETRY_I = icon('<path d="M46 20 A18 18 0 1 0 46 46" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M46 12 v12 h-12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 3. 눈속임 그림 주문서 = 사람 눈엔 정상, 주방장 눈엔 완전히 다르게 보이는 사진 (hero)
P3 = svg(360, sky(360)
         + label(190, 60, "⟦사람이 보는 사진|what a person sees⟧", 12, "var(--muted)", cls="d")
         + noisy_photo(190, 160, 1.6) + label(190, 280, "⟦그냥 샐러드네요|just a salad⟧", 13, "var(--ink)")
         + label(570, 60, "⟦주방장이 읽는 것|what the chef reads⟧", 12, "var(--muted)", cls="d")
         + person(570, 180, s=0.9, face=FROWN, **CHEF) + label(570, 300, "⟦이건 통과 서류예요|this is a pass-through form⟧", 13, "var(--bad)")
         + label(380, 30, "⟦눈속임 그림 주문서 = 사람 눈엔 정상, 주방장 눈엔 완전히 다른 사진|the picture that fools the eye: normal to a person, something else entirely to the chef⟧", 14, "var(--ink)", cls="d"))

# 4. 원본과 조작본, 사람 눈엔 똑같아도 주방장의 읽기는 뒤집혀요
P4 = svg(330, sky(330)
         + label(130, 50, "⟦원본 사진|original photo⟧", 12, "var(--ink)", cls="d")
         + dish(130, 130, 1.0) + person(130, 230, s=0.6, face=SMILE, **CHEF) + label(130, 300, "⟦샐러드예요 ✓|it's a salad ✓⟧", 12, "var(--good)")
         + label(430, 50, "⟦미세하게 조작한 사진|a subtly perturbed photo⟧", 12, "var(--ink)", cls="d")
         + noisy_photo(430, 130, 1.2) + person(430, 230, s=0.6, face=FROWN, **CHEF) + label(430, 300, "⟦통과 서류예요 ×|it's a pass form ×⟧", 12, "var(--bad)")
         + label(660, 160, "⟦사람 눈엔 똑같아요|identical to a human eye⟧", 11, "var(--muted)")
         + label(380, 30, "⟦점무늬 몇 개만 살짝 더해도, 읽는 결과가 완전히 뒤집혀요|add just a handful of tiny dots, and the reading flips completely⟧", 12, "var(--ink)", cls="d"))

# 5. 이웃 용어와 차이 — 명령을 숨기는 것 vs 잘못 보이게 만드는 것
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.8, face=EYES, **SNEAK)
         + label(190, 220, "⟦그림 속에 글자 명령을 숨겨요|hides a text command inside the picture⟧", 11, "var(--ink)")
         + label(190, 250, "⟦→ 명령을 몰래 끼우는 것|→ smuggling a command⟧", 11, "var(--muted)")
         + noisy_photo(570, 150, 1.0)
         + label(570, 220, "⟦사진 자체를 미세하게 조작해요|perturbs the photo itself, ever so slightly⟧", 11, "var(--ink)")
         + label(570, 250, "⟦→ 잘못 '보이게' 만드는 것|→ making it misread entirely⟧", 11, "var(--bad)")
         + label(380, 280, "⟦하나는 명령을 몰래 숨기고, 하나는 숨긴 명령 없이 보는 것 자체를 틀리게 만들어요|one hides a command; the other has no hidden command at all — it just breaks the seeing itself⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "adversarialexample", "order": 8,
    "title": ("눈속임 그림 주문서", "The Picture Order That Fools the Eye"),
    "h1": ("<em>적대적 예제</em>가 뭐예요?", "What is an <em>Adversarial Example</em>?"),
    "sub": ("적대적 예제를, 사람 눈엔 똑같아 보이지만 주방장은 완전히 다르게 읽는 사진 이야기로 풀어봤어요.",
            "Adversarial examples, told as a story about a photo that looks the same to a human eye but is read entirely differently by the chef."),
    "panels": [
        {"svg": P1, "alt": ("손님이 건넨 샐러드 사진을 보고 주방장이 이건 통과 서류라고 말함. 사람 눈엔 평범한 샐러드 사진임", "A guest hands over a photo of a salad, and the chef says this isn't a salad, it's a pass-through form — though to a human eye it's an ordinary salad photo"),
         "caption": ("사람 눈엔 똑같은 샐러드인데, 주방장은 다르게 읽어요.", "To a human eye it's the same salad — but the chef reads it differently."),
         "small": ("사진은 그대로인데, 주방장이 완전히 다른 걸로 읽어요.", "The photo looks unchanged, but the chef reads something else entirely.")},
        {"svg": P2, "alt": ("주방장은 사진의 점 하나하나를 숫자로 더해서 읽고, 검수원은 그림 전체를 한눈에 봄", "The chef reads the photo by adding up each dot's number, while the taster takes in the whole picture at a glance"),
         "caption": ("주방장의 눈은 점 하나하나의 숫자를 보고, 사람 눈은 전체 그림을 봐요.", "The chef's eye reads each dot's number; a human eye takes in the whole picture."),
         "small": ("숫자를 살짝 흔들면, 사람은 못 느껴도 읽는 결과는 완전히 바뀌어요.", "Nudge those numbers slightly, and the reading flips completely — even though a person feels nothing changed.")},
        {"svg": P3, "hero": True, "alt": ("같은 사진을 사람은 그냥 샐러드로 보고, 주방장은 통과 서류로 읽음", "The same photo looks like a plain salad to a person, but the chef reads it as a pass-through form"),
         "caption": ("사람 눈엔 정상, 주방장 눈엔 완전히 다른 사진이에요.", "Normal to a person, something else entirely to the chef."),
         "small": ("똑같은 사진인데, 읽는 결과만 완전히 갈라져요.", "The exact same photo — only the reading splits completely apart."),
         "tricks": (4, [
             (NOISE_I, ("점무늬 덧입히기", "Add a noise pattern"), ("눈엔 안 보이는 점들을 흩뿌려요", "scatter dots too faint to notice"), "warm"),
             (EDGE_I, ("경계선 살짝 비틀기", "Nudge the edges"), ("모양의 가장자리를 조금씩 밀어요", "push the shape's edges a little")),
             (STICKER_I, ("패턴 스티커 붙이기", "Stick on a pattern"), ("실제 물건에 무늬를 붙여도 통해요", "even works stuck onto a real object"), "calm"),
             (RETRY_I, ("여러 번 시도해 찾기", "Search by trial"), ("조작 값을 반복해서 맞춰가요", "repeatedly tune the perturbation")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 원본 사진을 주방장이 샐러드로 맞게 읽음. 오른쪽: 미세하게 조작한, 사람 눈엔 똑같은 사진을 주방장이 통과 서류로 잘못 읽음", "Left: the chef correctly reads the original photo as a salad. Right: a subtly perturbed photo, identical to a human eye, is misread by the chef as a pass-through form"),
         "caption": ("점무늬 몇 개만 더해도 읽는 결과가 뒤집혀요.", "Add just a handful of dots, and the reading flips."),
         "small": ("사람 눈엔 똑같지만, 주방장의 읽기는 완전히 갈라져요.", "Identical to a human eye — but the chef's reading splits completely apart.")},
        {"svg": P5, "alt": ("왼쪽: 그림 속에 글자 명령을 숨기는 것. 오른쪽: 사진 자체를 미세하게 조작해 잘못 읽히게 만드는 것", "Left: hiding a text command inside a picture. Right: subtly perturbing the photo itself so it is misread"),
         "caption": ("명령을 숨기는 것과 잘못 보이게 만드는 것은 달라요.", "Hiding a command is different from making something misread."),
         "small": ("이미지 인젝션은 숨긴 명령이 있고, 적대적 예제는 숨긴 명령 없이 보는 것 자체가 틀려요.", "Image injection has a hidden command. An adversarial example has none — it just breaks the seeing itself.")},
    ],
    "summary": (("<b>적대적 예제</b> = 사람 눈엔 <b>똑같아 보이지만</b> 주방장은 <b>완전히 다르게 읽도록</b> 미세하게 조작된 사진.",
                 "<b>Adversarial example</b> = a photo that <b>looks the same</b> to a human eye but is <b>subtly perturbed</b> so the chef reads it entirely differently."),
                ("적대적 예제(Adversarial Example)는 사람이 감지할 수 없을 만큼 작은 변형(노이즈, 패턴)을 입력에 더해 모델의 인식·분류 결과를 의도한 대로 틀리게 만드는 입력이에요. 이미지뿐 아니라 음성·텍스트에도 적용되고, 모델 가중치를 알아야 만들기 쉬운 경우(화이트박스)와 몰라도 반복 시도로 만들 수 있는 경우(블랙박스)가 있어요. 명령어를 숨기는 프롬프트 인젝션과 달리, 적대적 예제엔 숨긴 지시문이 전혀 없어요 — 모델의 인식 자체를 흔들 뿐이에요.",
                 "An adversarial example is an input with a perturbation (noise, a pattern) so small a human can't notice it, crafted to make a model's recognition or classification fail in a chosen way. This applies to images as well as audio and text, and can be crafted with knowledge of the model's weights (white-box) or without it, through repeated trial (black-box). Unlike prompt injection, which hides an instruction, an adversarial example contains no hidden instruction at all — it simply breaks the model's perception itself.")),
    "glossary": [
        ("적대적 예제", "Adversarial example", ("사람 눈엔 똑같지만 주방장은 다르게 읽는 사진.", "A photo that looks the same but is read differently by the chef."), ("숨긴 명령이 아니라, 보는 것 자체가 틀려요.", "Not a hidden command — the seeing itself is wrong.")),
        ("이미지 인젝션", "Image injection", ("그림 속에 글자 명령을 숨기는 것.", "Hiding a text command inside a picture."), ('바로 앞 페이지에서 다뤘어요. → <a href="imageinjection-ko.html">메뉴판 사진 속에 숨긴 글자</a>', 'Covered on the page right before this one. → <a href="imageinjection-en.html">letters hidden in a menu photo</a>')),
        ("미세 조작(perturbation)", "Perturbation", ("눈엔 안 보이는 작은 변형.", "A small change too faint to notice."), ("점무늬나 경계선을 살짝 흔들어요.", "A slight nudge to dots or edges.")),
        ("화이트박스 · 블랙박스", "White-box · black-box", ("레시피북을 보고 만드는지, 못 보고 시도만 하는지.", "Whether you can see the recipe book, or only try by trial."), ("레시피북을 알면 더 정교하게 조작할 수 있어요.", "Knowing the recipe book lets the perturbation be far more precise.")),
        ("분류기", "Classifier", ("사진을 보고 이게 뭔지 딱지를 붙이는 주방장의 눈.", "The chef's eye, which looks at a photo and tags what it is."), ("이 눈을 속이는 게 적대적 예제의 목표예요.", "Fooling this eye is exactly what an adversarial example aims for.")),
        ("오분류", "Misclassification", ("딱지를 잘못 붙이는 것.", "Tagging something with the wrong label."), ("적대적 예제가 노리는 결과예요.", "The outcome an adversarial example is built to cause.")),
        ("가드레일", "Guardrail", ("쪽지의 글자를 확인하는 검수원.", "The taster who checks a note's words."), ('글자가 아니라 보는 것 자체가 틀려서, 이 검수원도 못 잡아요. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', "Since the seeing itself is wrong — not the words — even this taster can't catch it. → <a href=\"guardrail-en.html\">What is a Guardrail?</a>")),
        ("레드팀", "Red team", ("일부러 조작한 사진으로 눈을 시험하는 사람들.", "People who test the eye with deliberately perturbed photos."), ('이 분야의 레드팀도 이걸 찾아요. → <a href="redteam-ko.html">보안 마을의 레드팀</a>', "AI red teams hunt for this too. → <a href=\"redteam-en.html\">the security world's red team</a>")),
    ],
}
