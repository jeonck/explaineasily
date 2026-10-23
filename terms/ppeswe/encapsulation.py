from _draw import *
from _world import *

# 1. 다들 작가의 서랍을 마음대로 뒤져서 고침
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=FROWN, **WRITER)
         + '<rect x="90" y="190" width="100" height="60" rx="4" fill="#8B5E3C"/>'
         + '<rect x="98" y="198" width="84" height="44" rx="2" fill="#FFF8E7"/>'
         + label(140, 268, "⟦작가의 서랍(메모·초안)|the writer's drawer (notes, drafts)⟧", 11, "var(--muted)")
         + person(420, 150, s=0.8, face=EYES, **EDITOR) + manuscript(500, 160, 0.7, marks=2)
         + label(420, 70, "⟦제가 대신 고쳐둘게요!|I'll just fix it myself!⟧", 13, "var(--bad)")
         + label(380, 30, "⟦편집장이 작가 서랍 속 메모를 직접 꺼내 고쳐요|the editor reaches into the writer's drawer and edits the notes directly⟧", 13, "var(--ink)"))

# 2. 다들 서로 서랍에 손대니 앞뒤가 안 맞음
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + manuscript(340, 130, 0.7, marks=3) + manuscript(440, 170, 0.7, marks=3)
         + person(560, 150, s=0.75, face=FROWN, **PROOFER)
         + bubble(440, 60, 220, 40, "⟦메모가 자꾸 바뀌어서 뭐가 맞는지 모르겠어요|the notes keep changing — I can't tell what's true⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦안을 아무나 건드리면, 전체가 뒤죽박죽 꼬여요|when anyone can touch the inside, everything gets tangled⟧", 12, "var(--ink)"))

# 3. 캡슐화 = 서랍은 잠그고, 제출함으로만 주고받기 (hero)
P3 = svg(340, sky(340)
         + person(160, 140, s=0.9, face=SMILE, **WRITER)
         + '<rect x="100" y="190" width="100" height="60" rx="4" fill="#8B5E3C"/>'
         + '<rect x="108" y="198" width="84" height="44" rx="2" fill="#5A3B22"/>'
         + '<circle cx="178" cy="220" r="4" fill="#E9B44C"/>'
         + label(150, 270, "⟦잠긴 서랍(비공개)|the locked drawer (private)⟧", 11, "var(--muted)")
         + '<rect x="330" y="150" width="60" height="90" rx="4" fill="var(--accent)"/>'
         + '<rect x="340" y="160" width="40" height="18" rx="2" fill="#FFF8E7"/>'
         + label(360, 260, "⟦제출함(공개 창구)|the submission box (public)⟧", 11, "var(--muted)")
         + manuscript(500, 170, 0.7, text="⟦완성된 챕터|finished chapter⟧")
         + person(600, 140, s=0.8, face=EYES, **EDITOR)
         + label(380, 30, "⟦캡슐화 = 서랍 속은 숨기고, 정해진 창구로만 건네줘요|encapsulation = hide the drawer's inside, hand things over only through the fixed box⟧", 13, "var(--ink)", cls="d"))

# 4. 비공개 메모 vs 공개 원고
P4 = svg(320, sky(320)
         + styleguide(60, 30, 300, 240, "⟦잠긴 서랍 (private)|LOCKED DRAWER (private)⟧",
                      ("⟦끄적인 메모, 지운 문장|scribbled notes, deleted lines⟧",
                       "⟦아직 안 끝난 생각|half-finished thoughts⟧",
                       "⟦밖에선 못 봐요|nobody outside can see this⟧"), 1.0)
         + styleguide(400, 30, 300, 240, "⟦제출함 (public)|SUBMISSION BOX (public)⟧",
                      ("⟦완성된 챕터만|only the finished chapter⟧",
                       "⟦정해진 형식으로|in a fixed, agreed format⟧",
                       "⟦여기로만 주고받아요|this is the only way in or out⟧"), 1.0, hl=2)
         + label(380, 300, "⟦안(서랍)을 바꿔도 창구(제출함) 모양만 그대로면 아무도 몰라요|change the inside, and if the box's shape stays the same, nobody outside notices⟧", 12, "var(--ink)"))

# 5. 캡슐화해도 설계 전체 실수는 못 막음
P5 = svg(350, '<rect width="380" height="350" fill="var(--good-soft)"/><rect x="380" width="380" height="350" fill="var(--accent-soft)"/>'
         + person(170, 140, s=0.8, face=SMILE, **WRITER) + manuscript(170, 220, 0.6)
         + label(170, 300, "⟦서랍을 잠그면 안전해요|locking the drawer keeps it safe⟧", 11, "var(--ink)")
         + person(560, 140, s=0.8, face=FROWN, **EDITOR)
         + '<rect x="630" y="160" width="60" height="50" rx="3" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/>'
         + label(570, 300, "⟦제출함 모양 자체를 잘못 짰다면, 그건 캡슐화가 못 막아요|but if the box's own shape is wrong, encapsulation can't fix that⟧", 11, "var(--ink)")
         + label(380, 330, "⟦캡슐화는 '안을 숨기는 것'이지, '설계를 잘 짜는 것'까지 보장하진 않아요|encapsulation hides the inside — it doesn't guarantee the design itself is right⟧", 12, "var(--ink)", cls="d"))

LOCK_I = icon('<rect x="18" y="26" width="28" height="24" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M24 26 v-8 a8 8 0 0 1 16 0 v8" stroke="var(--line)" stroke-width="4" fill="none"/><circle cx="32" cy="38" r="3" fill="var(--accent)"/>')
BOX_I = icon('<rect x="12" y="20" width="40" height="30" rx="3" fill="var(--accent)"/><rect x="20" y="28" width="24" height="12" rx="2" fill="#FFF8E7"/>')
BLOCK_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M20 20 l24 24 M44 20 l-24 24" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
SWAP_I = icon('<rect x="10" y="26" width="18" height="18" rx="3" fill="var(--muted)"/><rect x="36" y="20" width="18" height="18" rx="3" fill="var(--good)"/><path d="M28 32 h8" stroke="var(--line)" stroke-width="3"/>')

PAGE = {
    "slug": "encapsulation", "order": 22,
    "title": ("작가의 잠긴 서랍", "The Writer's Locked Drawer"),
    "h1": ("<em>캡슐화·정보은닉</em>이 뭐예요?", "What is <em>Encapsulation</em>?"),
    "sub": ("캡슐화와 정보은닉을, 작가가 서랍 속 메모는 숨기고 완성된 챕터만 제출함으로 건네는 이야기로 풀어봤어요.",
            "Encapsulation and information hiding, told as a story about a writer who hides draft notes in a drawer and only hands finished chapters through a submission box."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 작가의 서랍 속 메모를 직접 꺼내 고침", "The editor reaches into the writer's drawer and edits the notes directly"),
         "caption": ("편집장이 작가의 서랍 속 메모를 직접 꺼내 고쳐요.", "The editor reaches straight into the writer's drawer and edits the notes."),
         "small": ("서랍 속은 원래 작가만 보던 곳이에요.", "The inside of the drawer was supposed to be the writer's alone.")},
        {"svg": P2, "alt": ("여러 사람이 서랍 속 메모를 건드려 교정자가 혼란스러워함", "Several people touch the drawer's notes and the proofreader gets confused"),
         "caption": ("다들 서로 서랍에 손을 대니 앞뒤가 안 맞아요.", "With everyone reaching into each other's drawers, nothing lines up anymore."),
         "small": ("안을 아무나 건드리면, 전체가 뒤죽박죽 꼬여요.", "When anyone can touch the inside, everything gets tangled.")},
        {"svg": P3, "hero": True, "alt": ("작가의 서랍은 잠겨있고, 완성된 챕터만 제출함을 통해 편집장에게 전달됨", "The writer's drawer is locked, and only the finished chapter passes to the editor through a submission box"),
         "caption": ("캡슐화는 서랍 속은 숨기고, 정해진 창구로만 건네는 거예요.", "Encapsulation hides the drawer's inside and hands things over only through a fixed box."),
         "small": ("안을 바꿔도 창구 모양만 그대로면 아무도 몰라요.", "Change the inside, and if the box's shape stays the same, nobody outside notices."),
         "tricks": (4, [
             (LOCK_I, ("안을 감추기", "Hide the inside"), ("서랍은 작가만 열어요", "only the writer opens the drawer"), "calm"),
             (BOX_I, ("창구로만 공개", "Expose only through the box"), ("완성본만 건네요", "only the finished piece passes through")),
             (BLOCK_I, ("직접 접근 막기", "Block direct access"), ("서랍을 남이 못 열어요", "nobody else can open the drawer"), "warm"),
             (SWAP_I, ("안은 바꿔도 돼요", "The inside can change freely"), ("창구 모양만 같으면요", "as long as the box's shape stays the same")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 잠긴 서랍 속 메모. 오른쪽: 제출함으로 나가는 완성된 챕터", "Left: notes inside the locked drawer. Right: the finished chapter going out through the submission box"),
         "caption": ("잠긴 서랍 속과 제출함 겉은 서로 달라요.", "What's inside the locked drawer differs from what the submission box shows."),
         "small": ("안을 바꿔도 창구 모양만 같으면 아무도 몰라요.", "Change the inside, and nobody notices as long as the box's shape stays the same.")},
        {"svg": P5, "alt": ("왼쪽: 서랍을 잠가 안전함. 오른쪽: 제출함 모양 자체가 잘못 짜여 있음", "Left: the locked drawer is safe. Right: the submission box's own shape was designed wrong"),
         "caption": ("캡슐화해도 설계 자체의 실수는 못 막아요.", "Encapsulation doesn't catch a mistake in the design itself."),
         "small": ("캡슐화는 '안을 숨기는 것'이지, 설계를 잘 짜는 것까지 보장하진 않아요.", "Encapsulation hides the inside — it doesn't guarantee the design itself is right.")},
    ],
    "summary": (("<b>캡슐화·정보은닉</b>은 데이터와 기능을 하나로 묶어 <b>안은 숨기고</b>, 정해진 <b>창구(인터페이스)</b>로만 주고받게 하는 거예요.",
                 "<b>Encapsulation (information hiding)</b> bundles data and behavior together, <b>hides the inside</b>, and exposes only a fixed <b>interface</b> to the outside."),
                ("캡슐화는 객체의 속성(데이터)과 메서드(기능)를 하나로 묶고, 외부에는 공개(public) 인터페이스만 노출해 내부 구현을 감추는 객체지향의 핵심 원칙이에요. 내부 구조(비공개/private)를 자유롭게 바꿔도 외부 호출 방식이 그대로면 영향이 없어 변경에 강해지고, 의도치 않은 직접 조작도 막아줘요.",
                 "Encapsulation bundles an object's data and methods together and exposes only a public interface, hiding the internal implementation — a core OOP principle. Because the private internals can change freely as long as the external interface stays the same, it makes code resilient to change and prevents unintended direct manipulation.")),
    "glossary": [
        ("캡슐화", "Encapsulation", ("데이터+기능을 하나로 묶기.", "Bundling data and behavior together."), ("안은 숨기고 창구만 공개해요.", "Hides the inside, exposes only the box.")),
        ("정보은닉", "Information Hiding", ("서랍을 잠그는 것.", "Locking the drawer."), ("캡슐화를 가능하게 하는 원칙이에요.", "The principle that makes encapsulation possible.")),
        ("인터페이스(공개 메서드)", "Public Interface", ("제출함.", "The submission box."), ("바깥과 주고받는 유일한 창구예요.", "The only way in or out from the outside.")),
        ("private 변수", "Private Field", ("잠긴 서랍 속 메모.", "Notes inside the locked drawer."), ("바깥에서 직접 못 건드려요.", "The outside can't touch it directly.")),
        ("getter/setter", "Getter/Setter", ("창구 직원이 대신 꺼내주는 손.", "The clerk's hand that fetches it for you."), ("서랍을 열어주는 대신, 정해진 방식으로만 건네줘요.", "Instead of opening the drawer, it hands things over only the agreed way.")),
        ("모듈화", "Modularity", ("서랍을 책상마다 따로 두기.", "Giving every desk its own drawer."), ("캡슐화가 쌓이면 모듈화가 돼요.", "Stack enough encapsulation and you get modularity.")),
        ("리팩토링", "Refactoring", ("서랍 속 메모를 정리하기.", "Tidying up the notes inside the drawer."), ('창구 모양은 그대로 두고 안만 정리해요. → <a href="refactorppe-ko.html">겉은 그대로, 속만 다시 다듬기</a>', 'The box stays the same while the inside gets tidied. → <a href="refactorppe-en.html">keep the outside, retouch the inside</a>')),
        ("단위테스트", "Unit Test", ("창구에 직접 넣어보는 확인.", "Checking by feeding things straight into the box."), ("제출함(공개 인터페이스)만 보고도 검증할 수 있어요.", "You can verify it by watching just the public box.")),
    ],
}
