from _draw import *

LOW = dict(hat=None, shirt="#4A7A6A", face=SMILE)
MID = dict(hat="var(--good)", shirt="var(--good)", face=EYES)
HIGH = dict(hat="#E9B44C", shirt="#7B3FA0", face=EYES)


def rung(x, y, w, label_text):
    return f'<rect x="{x}" y="{y}" width="{w}" height="6" fill="#8B5E3C"/>' + label(x - 16, y + 5, label_text, 12, "var(--muted)", "end")


def ladder(x, y, h):
    return f'<rect x="{x}" y="{y}" width="8" height="{h}" fill="#8B5E3C"/><rect x="{x + 120}" y="{y}" width="8" height="{h}" fill="#8B5E3C"/>'


def scroll(x, y, s=1.0, color="#FFF8E7"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-12" width="36" height="24" rx="4" fill="{color}" stroke="#C9A86A" stroke-width="2.5"/>'
            + '<path d="M-10 -3 h20 M-10 3 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/></g>')


def blockarrow(x1, y1, x2, y2, ok=False):
    color = "var(--good)" if ok else "var(--bad)"
    mark = "" if ok else f'<path d="M{(x1 + x2) / 2 - 8} {(y1 + y2) / 2 - 8} l16 16 M{(x1 + x2) / 2 + 8} {(y1 + y2) / 2 - 8} l-16 16" stroke="{color}" stroke-width="4" stroke-linecap="round"/>'
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" stroke-dasharray="5 5" fill="none"/>{mark}'


# 1. 등급 사다리가 있는 성
P1 = svg(320, sky(320)
         + ladder(360, 60, 220)
         + rung(360, 60, 128, "⟦등급3: 왕의 비밀 방|rank 3: the king's secret room⟧") + person(390, 20, s=0.5, **HIGH) + scroll(330, 45)
         + rung(360, 150, 128, "⟦등급2: 장군의 방|rank 2: the general's room⟧") + person(390, 110, s=0.5, **MID) + scroll(330, 135)
         + rung(360, 240, 128, "⟦등급1: 서기의 방|rank 1: the clerk's room⟧") + person(390, 200, s=0.5, **LOW) + scroll(330, 225)
         + label(380, 300, "⟦성의 방마다 비밀 등급이 매겨져 있어요|every room in the castle carries its own secrecy rank⟧", 13, "var(--ink)", cls="d"))

# 2. 아무 규칙 없이 오르내리면 둘 다 곤란해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 110, s=0.7, **LOW) + scroll(230, 90) + blockarrow(240, 90, 400, 60) + person(430, 60, s=0.55, **HIGH)
         + label(260, 170, "⟦낮은 등급이 왕의 비밀을 엿봐요|a low rank peeks at the king's secret⟧", 11, "var(--bad)")
         + person(590, 110, s=0.7, **HIGH) + scroll(540, 90) + blockarrow(530, 90, 370, 150) + person(340, 170, s=0.55, **LOW)
         + label(500, 170, "⟦높은 등급이 비밀을 낮은 장부에 적어요|a high rank writes the secret into a low ledger⟧", 11, "var(--bad)")
         + label(380, 270, "⟦둘 다 결국 비밀이 아래로 새는 길이에요|both end up leaking the secret downward⟧", 12, "var(--ink)", cls="d"))

# 3. BLP와 Biba — 거꾸로 짝지은 두 규칙 (hero)
P3 = svg(360, '<rect width="380" height="360" fill="var(--good-soft)"/><rect x="380" width="380" height="360" fill="var(--accent-soft)"/>'
         + label(190, 34, "⟦BLP — 비밀이 안 새게|BLP — no leaking secrets⟧", 14, "var(--ink)", cls="d")
         + person(140, 110, s=0.55, **HIGH) + person(140, 230, s=0.55, **LOW)
         + blockarrow(170, 230, 170, 130) + label(100, 180, "⟦못 올려보기|no read up⟧", 11, "var(--bad)")
         + blockarrow(120, 110, 120, 210) + label(230, 180, "⟦못 내려적기|no write down⟧", 11, "var(--bad)")
         + label(190, 300, "⟦기밀성 — 비밀을 지켜요|confidentiality — keeps secrets secret⟧", 12, "var(--ink)")
         + label(570, 34, "⟦Biba — 거짓이 안 섞이게|Biba — no corrupting the clean⟧", 14, "var(--ink)", cls="d")
         + person(520, 110, s=0.55, **HIGH) + person(520, 230, s=0.55, **LOW)
         + blockarrow(495, 110, 495, 210, ok=False) + label(420, 180, "⟦못 내려읽기|no read down⟧", 11, "var(--bad)")
         + blockarrow(545, 230, 545, 130, ok=False) + label(620, 180, "⟦못 올려적기|no write up⟧", 11, "var(--bad)")
         + label(570, 300, "⟦무결성 — 깨끗함을 지켜요|integrity — keeps clean records clean⟧", 12, "var(--ink)")
         + label(380, 338, "⟦같은 사다리, 서로 반대 방향의 규칙이에요|the same ladder, with mirror-image rules⟧", 13, "var(--ink)", cls="d"))

UP_I = icon('<path d="M32 50 V16 M20 28 L32 14 L44 28" fill="none" stroke="var(--good)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
DOWN_I = icon('<path d="M32 14 V48 M20 36 L32 50 L44 36" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
MIRROR_I = icon('<path d="M32 10 V54" stroke="var(--muted)" stroke-width="2" stroke-dasharray="3 3"/><path d="M12 20 L26 20 L26 32" fill="none" stroke="var(--good)" stroke-width="3" stroke-linecap="round"/><path d="M52 44 L38 44 L38 32" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
EXAM_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 30 h24 M20 38 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "blpbiba", "order": 20,
    "title": ("비밀은 안 새게, 거짓은 안 섞이게 — 사다리 두 규칙", "No Leaking Down, No Corrupting Up — Two Ladder Rules"),
    "h1": ("<em>BLP/Biba</em>가 뭐예요?", "What are <em>BLP</em> and <em>Biba</em>?"),
    "sub": ("접근통제 보안 모델 BLP와 Biba를, 등급 사다리를 오르내리는 걸 서로 반대로 막는 두 규칙 이야기로 풀어봤어요.",
            "The BLP and Biba access-control security models, told as a story about two rules that block climbing a rank ladder in opposite directions."),
    "panels": [
        {"svg": P1, "alt": ("성의 방이 사다리처럼 등급 1(서기)·2(장군)·3(왕)로 나뉘어 있고 각 방에 두루마리가 있음", "The castle's rooms sit like ladder rungs: rank 1 (the clerk), rank 2 (the general), rank 3 (the king), each holding its own scroll"),
         "caption": ("성의 방마다 비밀 등급이 매겨져 있어요.", "Every room in the castle carries its own secrecy rank."),
         "small": ('<a href="accesscontrolppe-ko.html">MAC</a>(강제적 접근통제)에서는 이 등급을 아무도 마음대로 못 바꿔요.',
                   'Under <a href="accesscontrolppe-en.html">MAC</a> (Mandatory Access Control), nobody can change this ranking at will.')},
        {"svg": P2, "alt": ("낮은 등급이 왕의 비밀을 엿보고, 높은 등급이 비밀을 낮은 장부에 적어 둘 다 비밀이 새는 상황", "A low rank peeks at the king's secret, and a high rank writes the secret into a low-rank ledger — both leak the secret downward"),
         "caption": ("아무 규칙 없이 오르내리면 둘 다 곤란해요.", "Climb the ladder either way with no rule, and both end badly."),
         "small": ("엿봐도 새고, 적어 내려도 새요. 비밀은 결국 아래로 흘러가요.", "Peek up, and it leaks. Write down, and it leaks. Either way, the secret flows downward.")},
        {"svg": P3, "hero": True, "alt": ("왼쪽 BLP는 못 올려보기·못 내려적기로 비밀을 지키고, 오른쪽 Biba는 못 내려읽기·못 올려적기로 깨끗함을 지킴", "Left, BLP keeps secrets with no-read-up and no-write-down; right, Biba keeps things clean with no-read-down and no-write-up"),
         "caption": ("BLP와 Biba는 거꾸로 짝지은 두 규칙이에요.", "BLP and Biba are two rules, paired as mirror images."),
         "small": ('BLP(1973)는 <a href="ciatriad-ko.html">기밀성</a>을, Biba(1977)는 <a href="ciatriad-ko.html">무결성</a>을 지켜요. 둘 다 같은 등급 사다리 위의 규칙이에요.',
                   'BLP (1973) protects <a href="ciatriad-en.html">confidentiality</a>; Biba (1977) protects <a href="ciatriad-en.html">integrity</a>. Both are rules on the very same rank ladder.'),
         "tricks": (4, [
             (UP_I, ("BLP: 못 올려보기", "BLP: no read up"), ("낮은 등급은 높은 비밀을 못 읽어요", "a low rank can't read a higher secret"), "calm"),
             (DOWN_I, ("BLP: 못 내려적기", "BLP: no write down"), ("높은 등급이 낮은 장부에 못 적어요", "a high rank can't write into a low ledger")),
             (MIRROR_I, ("Biba: 정반대", "Biba: the exact mirror"), ("못 내려읽기 + 못 올려적기", "no read down + no write up"), "warm"),
             (EXAM_I, ("시험에 자주 나와요", "A frequent exam topic"), ("'BLP와 Biba의 차이'로 꼭 물어봐요", "almost always asked as the difference between them")),
         ])},
        {"svg": svg(340, sky(340)
                    + '<rect x="40" y="30" width="680" height="260" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="34" rx="8" fill="#C9A86A"/>'
                    + label(130, 53, "⟦모델|model⟧", 13, "#142033", cls="d") + label(330, 53, "⟦규칙|rule⟧", 13, "#142033", cls="d") + label(580, 53, "⟦지키는 것|what it protects⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M40 {64 + i * 75} h680" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(130, 100, "⟦BLP|BLP⟧", 14, "#142033", cls="d") + label(330, 92, "⟦못 올려보기(No Read Up)|no read up⟧", 11, "#142033") + label(330, 112, "⟦못 내려적기(No Write Down)|no write down⟧", 11, "#142033") + label(580, 100, "⟦기밀성|confidentiality⟧", 12, "#142033")
                    + label(130, 175, "⟦Biba|Biba⟧", 14, "#142033", cls="d") + label(330, 167, "⟦못 내려읽기(No Read Down)|no read down⟧", 11, "#142033") + label(330, 187, "⟦못 올려적기(No Write Up)|no write up⟧", 11, "#142033") + label(580, 175, "⟦무결성|integrity⟧", 12, "#142033")
                    + label(130, 250, "⟦둘 다|both⟧", 14, "#142033", cls="d") + label(330, 250, "⟦같은 등급 사다리 위의 규칙|rules on the very same rank ladder⟧", 11, "#142033") + label(580, 250, "⟦MAC(강제적 접근통제)|MAC (mandatory access control)⟧", 11, "#142033")),
         "alt": ("표: BLP — 못 올려보기+못 내려적기 / 기밀성, Biba — 못 내려읽기+못 올려적기 / 무결성, 둘 다 — 같은 사다리 위의 규칙 / MAC", "Table: BLP — no read up + no write down / confidentiality, Biba — no read down + no write up / integrity, Both — rules on the same ladder / MAC"),
         "caption": ("네 가지 규칙을 나란히 보면 이래요.", "Side by side, here are the four rules."),
         "small": ("BLP는 비밀이 아래로 새는 걸, Biba는 거짓이 위로 섞이는 걸 막아요.", "BLP blocks a secret leaking downward; Biba blocks something untrustworthy creeping upward.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.85, **HIGH) + label(190, 240, "⟦규칙이 엄격해서 쓰기 불편해요|strict rules make day-to-day work awkward⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.85, **MID) + label(560, 240, "⟦보통은 역할(RBAC)과 같이 섞어 써요|usually blended with role-based access (RBAC) in practice⟧", 11, "var(--ink)")
                    + label(380, 280, "⟦원래 군사·기밀 시스템에서 나온, MAC의 구체적인 규칙이에요|born in military and classified systems — the concrete rules behind MAC⟧", 12, "var(--ink)", cls="d")),
         "alt": ("규칙이 엄격해 쓰기 불편하고, 실제로는 RBAC와 섞어 씀. 군사·기밀 시스템에서 나온 MAC의 구체적 규칙", "The strict rules make daily use awkward, so in practice they're blended with RBAC. Born in military/classified systems as the concrete rules behind MAC"),
         "caption": ("엄격한 만큼, 실제론 다른 모델과 섞어 써요.", "Strict as they are, they're usually blended with other models in practice."),
         "small": ('<a href="accesscontrolppe-ko.html">MAC</a>의 구체적인 규칙이 바로 이거예요. 회사 시스템은 보통 <a href="rbac-ko.html">RBAC</a>를 더 많이 써요.',
                   'These are the concrete rules behind <a href="accesscontrolppe-en.html">MAC</a>. Most company systems lean more on <a href="rbac-en.html">RBAC</a> instead.')},
    ],
    "summary": (("<b>BLP</b>는 등급 사다리에서 <b>못 올려보고(no read up) 못 내려적어서(no write down)</b> 비밀이 새지 않게 하고, <b>Biba</b>는 정반대로 <b>못 내려읽고 못 올려적어서</b> 거짓이 섞이지 않게 해요.",
                 "<b>BLP</b> keeps a secret from leaking by letting nobody <b>read up or write down</b> the rank ladder; <b>Biba</b> mirrors it exactly, letting nobody <b>read down or write up</b>, to keep clean records clean."),
                ("Bell-LaPadula(BLP, 1973)는 기밀성을 지키는 MAC 모델로 No Read Up/No Write Down을 강제해요. Biba(1977)는 무결성을 지키는 모델로 No Read Down/No Write Up을 강제해, 신뢰도 낮은 주체가 높은 등급의 자료를 오염시키지 못하게 해요. 둘 다 등급(레이블) 기반 강제적 접근통제(MAC)의 구체적인 수학적 규칙이고, 군사·정부 기밀 시스템에서 비롯됐어요.",
                 "Bell-LaPadula (BLP, 1973) is a confidentiality-focused MAC model enforcing No Read Up / No Write Down. Biba (1977) is an integrity-focused model enforcing No Read Down / No Write Up, so a lower-trust subject can never corrupt higher-ranked data. Both are the concrete, formal mathematical rules behind label-based Mandatory Access Control (MAC), originating in military and government classified systems.")),
    "glossary": [
        ("BLP", "Bell-LaPadula", ("기밀이 안 새게 하는 규칙.", "The rule that keeps a secret from leaking."), ("못 올려보기 + 못 내려적기로 기밀성을 지켜요.", "No read up + no write down, protecting confidentiality.")),
        ("Biba", "Biba", ("거짓이 안 섞이게 하는 규칙.", "The rule that keeps something untrustworthy from creeping in."), ("못 내려읽기 + 못 올려적기로 무결성을 지켜요.", "No read down + no write up, protecting integrity.")),
        ("No Read Up", "No Read Up", ("낮은 등급이 높은 비밀을 못 읽어요.", "A low rank can't read a higher secret."), ("BLP의 첫 번째 규칙이에요.", "BLP's first rule.")),
        ("No Write Down", "No Write Down", ("높은 등급이 낮은 장부에 못 적어요.", "A high rank can't write into a lower ledger."), ("BLP의 두 번째 규칙이에요.", "BLP's second rule.")),
        ("No Read Down / No Write Up", "No Read Down / No Write Up", ("Biba의 정반대 규칙 한 쌍.", "Biba's mirror-image pair of rules."), ("무결성을 지키기 위해 BLP와 반대 방향으로 막아요.", "Blocks the opposite direction from BLP, to protect integrity instead.")),
        ("MAC", "Mandatory Access Control", ("왕의 등급표, 아무도 못 바꿔요.", "The king's rank-list — nobody can override it."), ('BLP/Biba는 이 MAC을 실제로 구현하는 구체적 규칙이에요. → <a href="accesscontrolppe-ko.html">열쇠 주인을 정하는 세 가지 방식</a>', 'BLP/Biba are the concrete rules that actually implement MAC. → <a href="accesscontrolppe-en.html">three ways to decide who holds the key</a>')),
        ("기밀성 · 무결성", "Confidentiality · Integrity", ("못 보게 · 못 바꾸게.", "No peeking · no tampering."), ('CIA 3요소 중 두 가지예요. → <a href="ciatriad-ko.html">지키는 것 세 가지</a>', 'Two of the three legs of the CIA triad. → <a href="ciatriad-en.html">three things to keep</a>')),
        ("RBAC", "RBAC", ("실제 조직이 더 많이 쓰는 모델.", "The model real organizations lean on more."), ('BLP/Biba는 엄격해서, 보통 역할 기반과 섞어 써요. → <a href="rbac-ko.html">모자마다 열쇠 꾸러미</a>', 'BLP/Biba are strict enough that they\'re usually blended with role-based rules. → <a href="rbac-en.html">a key ring for every hat</a>')),
    ],
}
