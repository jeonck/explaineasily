from _draw import *
from _world import *

# 이 페이지 전용 소품: 참고 카드함 (RAG가 그때그때 찾아보는 외부 자료함). _world.py 는 건드리지 않고 여기서만 그린다.
def cardbox(x, y, s=1.0, w=120, h=44, n=4, bad_idx=-1):
    """참고 카드함. 박스 위로 카드가 삐죽 나와 있고, bad_idx 번째 카드만 가짜(빨간색)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="16" width="{w}" height="{h}" rx="4" fill="#8B5E3C"/>'
    out += f'<rect x="4" y="20" width="{w - 8}" height="{h - 8}" fill="#5A3B22" opacity="0.3"/>'
    cw = w / n
    for i in range(n):
        cx = i * cw + cw / 2
        bad = (i == bad_idx)
        fill = "var(--bad)" if bad else "#FFF8E7"
        stroke = "var(--bad)" if bad else "#C9A86A"
        rot = -6 + i * (12 / max(1, n - 1))
        out += (f'<g transform="rotate({rot:.1f} {cx:.1f} 10)"><rect x="{cx - 10:.1f}" y="-6" width="20" height="30" rx="2" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="2"/><path d="M{cx - 6:.1f} 2 h12 M{cx - 6:.1f} 8 h12" stroke="#142033" stroke-width="1.6"/></g>')
    return out + '</g>'


CHECK_I = icon('<circle cx="32" cy="32" r="24" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
LOCKBOX_I = icon('<rect x="14" y="28" width="36" height="26" rx="4" fill="var(--accent)"/><path d="M20 28 v-6 a12 12 0 0 1 24 0 v6" fill="none" stroke="var(--accent)" stroke-width="5"/>')
COMPARE_I = icon('<rect x="8" y="16" width="20" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="36" y="16" width="20" height="32" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M30 32 h4" stroke="var(--muted)" stroke-width="3"/>')
REFRESH_I = icon('<path d="M46 20 a18 18 0 1 0 4 20" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M50 10 l0 12 l-12 0z" fill="var(--good)"/>')

# 1. 카드함에서 참고 카드를 꺼내 답해요 — 그런데 누군가 가짜 카드를 끼워요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.75, face=SMILE, **CHEF)
         + cardbox(205, 130, 0.85) + person(310, 190, s=0.65, face=SMILE, **GUEST)
         + label(275, 230, "⟦보통 참고 카드예요|a normal reference card⟧", 11, "var(--muted)")
         + cardbox(480, 120, 0.85, bad_idx=1) + person(590, 190, s=0.65, face=FROWN, **SNEAK)
         + label(545, 250, "⟦몰래 가짜 카드를 끼워 넣어요|a fake card gets slipped in⟧", 12, "var(--bad)", cls="d")
         + label(380, 295, "⟦이 카드함은 누구나 카드를 더할 수 있어요|anyone can add a card to this box⟧", 13, "var(--ink)"))

# 2. 주방장은 카드함에서 꺼낸 글자만 믿어요 — 누가 썼는지는 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.8, face=EYES, **CHEF) + cardbox(140, 95, 0.55, bad_idx=2)
         + ticket(330, 170, 0.8) + bubble(260, 55, 240, 55, "⟦'환불 가능' 카드가 있네요, 그대로 답해드려야죠|there is a card saying refundable, so that is what I will say⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 160, s=0.7, face=FROWN, **SNEAK) + label(560, 250, "⟦카드를 누가 썼는지는 몰라요|who actually wrote the card stays unknown⟧", 11, "var(--bad)")
         + label(380, 280, "⟦사람이라면 출처를 의심하지만, 이 주방장은 글자만 믿어요|a human would question the source — this chef just trusts the words⟧", 12, "var(--ink)"))

# 3. RAG 포이즈닝 = 참고 카드함에 가짜 카드를 끼워 넣는 것 (hero)
P3 = svg(360, sky(360)
         + cardbox(40, 90, 1.3, n=6, bad_idx=4, w=160, h=60)
         + person(300, 150, s=0.8, face=EYES, **CHEF)
         + person(430, 190, s=0.6, face=SMILE, **GUEST) + dish(430, 140, 0.5)
         + person(560, 220, s=0.55, face=EYES, **INSPECTOR) + badge(600, 190, 0.65)
         + label(380, 30, "⟦RAG 포이즈닝 = 참고 카드함에 가짜 카드를 끼워 넣는 것|RAG Poisoning = slipping a fake card into the reference box⟧", 14, "var(--ink)", cls="d")
         + label(380, 345, "⟦카드함 속 카드 한 장이 답을 바꿔버려요|one card inside the box can change the whole answer⟧", 12, "var(--muted)"))


def _arrow(x1, y, x2):
    return (f'<path d="M{x1} {y} H{x2 - 10}" stroke="var(--muted)" stroke-width="3"/>'
            f'<path d="M{x2 - 14} {y - 6} L{x2} {y} L{x2 - 14} {y + 6} Z" fill="var(--muted)"/>')


# 4. 카드 한 장이 가짜면, 답도 가짜가 돼요 (작동 디테일)
P4 = svg(330, sky(330, ground=False)
         + ticket(60, 90, 0.8, text="⟦'환불 규정이 뭐예요?'|'what is the refund policy?'⟧")
         + label(60, 170, "⟦① 질문이 들어와요|① a question comes in⟧", 11, "var(--muted)")
         + _arrow(130, 110, 220)
         + cardbox(230, 70, 1.0, n=5, bad_idx=2)
         + label(290, 170, "⟦② 비슷한 카드를 찾아요(가짜 포함)|② similar cards are pulled — fake one too⟧", 11, "var(--muted)")
         + _arrow(360, 110, 470)
         + person(480, 140, s=0.75, face=EYES, **CHEF)
         + label(480, 230, "⟦③ 카드 내용을 그대로 이어붙여요|③ the chef stitches the card\'s words straight in⟧", 10, "var(--muted)")
         + _arrow(560, 110, 660)
         + dish(680, 160, 0.6, bad=True)
         + label(680, 230, "⟦④ 틀린 답이 나와요|④ out comes the wrong answer⟧", 11, "var(--bad)")
         + label(380, 300, "⟦카드 한 장이 가짜면, 답도 가짜가 돼요|one fake card means one fake answer⟧", 12, "var(--ink)", cls="d"))

# 5. 카드 한 장만 빼면 고쳐지지만, 열려 있으면 또 생겨요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(140, 150, s=0.75, face=SMILE, **INSPECTOR) + cardbox(230, 160, 0.55)
         + label(260, 240, "⟦가짜 카드 한 장만 빼면 바로 고쳐져요|pull the one fake card and it is fixed right away⟧", 11, "var(--ink)")
         + cardbox(530, 160, 0.55, bad_idx=1) + person(650, 170, s=0.6, face=FROWN, **SNEAK)
         + label(610, 250, "⟦열려 있으면 또 끼워 넣을 수 있어요|if the box stays open, another can slip back in⟧", 11, "var(--ink)")
         + label(380, 282, "⟦재료창고는 오래 남지만, 이 카드함은 그때그때 쓰는 자료라 빨리 고치는 대신 계속 지켜봐야 해요|the pantry keeps poison for good — this box re-fetches data, so fixes come fast but watching never stops⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "ragpoisoning", "order": 14,
    "title": ("참고 카드함에 끼운 가짜 카드", "The Fake Card Slipped Into the Reference Box"),
    "h1": ("<em>RAG 포이즈닝</em>이 뭐예요?", "What is <em>RAG Poisoning</em>?"),
    "sub": ("RAG 포이즈닝을, 주방장이 그때그때 꺼내 보는 참고 카드함에 누군가 가짜 카드를 끼워 넣는 이야기로 풀어봤어요.",
            "RAG Poisoning, told as a story about someone slipping a fake card into the reference box the chef pulls from on the spot."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 카드함에서 카드를 꺼내는 동안, 다른 손님이 가짜 카드를 몰래 끼워 넣음", "While the chef pulls a card from the box, another guest secretly slips in a fake one"),
         "caption": ("이 카드함은 누구나 카드를 더할 수 있어요.", "Anyone can add a card to this box."),
         "small": ("보통 카드도, 몰래 끼운 가짜 카드도 똑같이 섞여 있어요.", "A normal card and a smuggled fake one sit mixed together.")},
        {"svg": P2, "hero": False, "alt": ("주방장이 '환불 가능'이라고 쓰인 가짜 카드를 그대로 믿고 답함. 카드를 쓴 사람은 숨어 있음", "The chef trusts a fake card saying 'refundable' and answers accordingly; whoever wrote it stays hidden"),
         "caption": ("주방장은 카드 속 글자만 믿어요 — 누가 썼는지는 몰라요.", "The chef trusts the words on the card alone — not who wrote them."),
         "small": ("사람이라면 출처를 의심하지만, 이 주방장은 그러지 않아요.", "A human would question the source. This chef does not.")},
        {"svg": P3, "hero": True, "alt": ("참고 카드함, 주방장, 손님, 요리, 검사관이 한 장면에 있음", "A reference card box, the chef, a guest, a dish, and an inspector all in one scene"),
         "caption": ("RAG 포이즈닝은 참고 카드함에 가짜 카드를 끼워 넣는 것이에요.", "RAG Poisoning means slipping a fake card into the reference box."),
         "small": ("카드함 속 카드 한 장이 답을 바꿔버려요.", "One card inside the box can change the whole answer."),
         "tricks": (4, [
             (CHECK_I, ("출처부터 확인하기", "Check the source first"), ("카드만 보고 바로 믿지 않아요", "do not trust a card on sight alone"), "calm"),
             (LOCKBOX_I, ("쓰기 권한 제한하기", "Limit who can write"), ("카드함 문을 아무에게나 열어주지 않아요", "not everyone gets to add a card")),
             (COMPARE_I, ("여러 카드 비교하기", "Cross-check several cards"), ("한 장만 보고 답하지 않아요", "never answer from just one card"), "warm"),
             (REFRESH_I, ("카드함 자주 정리하기", "Refresh the box often"), ("오래된·수상한 카드를 걸러내요", "weed out old or suspicious cards")),
         ])},
        {"svg": P4, "alt": ("질문이 들어오고, 카드함에서 가짜 카드가 섞여 나오고, 주방장이 그대로 이어붙여 틀린 요리가 나오는 과정", "A question comes in, a fake card gets pulled from the box, and the chef stitches it in, producing a wrong dish"),
         "caption": ("카드 한 장이 가짜면, 답도 가짜가 돼요.", "One fake card means one fake answer."),
         "small": ("질문 → 카드 검색 → 그대로 이어붙이기 → 틀린 답, 네 걸음이에요.", "Question, search the box, stitch it in, wrong answer — four steps.")},
        {"svg": P5, "alt": ("왼쪽: 검사관이 가짜 카드 한 장을 빼냄. 오른쪽: 카드함이 열려 있어 또 가짜 카드가 들어옴", "Left: the inspector pulls out the one fake card. Right: the box stays open, so another fake card slips in"),
         "caption": ("한 장만 빼면 고쳐지지만, 열려 있으면 또 생겨요.", "Pulling one card fixes it — but it can happen again while the box stays open."),
         "small": ("재료창고와 달리, 이 카드함은 빨리 고치는 대신 계속 지켜봐야 해요.", "Unlike the pantry, this box is quick to fix but needs constant watching.")},
    ],
    "summary": (("<b>RAG 포이즈닝</b> = <b>참고 카드함</b>에 <b>가짜 카드</b>를 끼워 넣어, 주방장이 그 카드 그대로 요리하게 만드는 것.",
                 "<b>RAG Poisoning</b> = slipping a <b>fake card</b> into the <b>reference card box</b> so the chef cooks straight from it."),
                ("RAG 포이즈닝(RAG Poisoning)은 RAG(검색 증강 생성)가 참고하는 외부 자료 — 문서, 검색 결과, 벡터DB 속 조각 — 에 가짜 정보를 심어 모델이 틀리거나 위험한 답을 하게 만드는 공격이에요. 모델을 다시 학습시킬 필요 없이 '그때그때 찾아보는 자료'만 더럽히면 되기 때문에 비교적 쉽고, 자료가 공개되어 있을수록 더 위험해요.",
                 "RAG Poisoning plants false information in the external material a RAG (retrieval-augmented generation) system draws on — documents, search results, chunks sitting in a vector DB — so the model confidently repeats it. It needs no retraining: poisoning the material the model looks up each time is enough, and the more open that material is, the easier it is to attack.")),
    "glossary": [
        ("RAG 포이즈닝", "RAG Poisoning", ("참고 카드함에 가짜 카드를 끼우는 일.", "Slipping a fake card into the reference card box."), ('이 세계관 전체 소개도 있어요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'There is also an intro to this whole world. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
        ("RAG", "RAG", ("답하기 전에 자료를 찾아보는 것.", "Looking up material before answering."), ('AI 세계의 기본 개념이에요. → <a href="rag-ko.html">사서가 찾아온 페이지</a>', 'The underlying AI concept. → <a href="rag-en.html">The Page the Librarian Brought</a>')),
        ("벡터 DB", "Vector DB", ("카드를 딱지 순서로 정리해 둔 곳.", "Where cards are filed by their tag order."), ('카드함이 실제로 어떻게 정리되는지 봐요. → <a href="vectordb-ko.html">딱지로 정리한 서가</a>', 'See how the box is actually organized. → <a href="vectordb-en.html">The Shelf Organized by Tags</a>')),
        ("간접 프롬프트 인젝션", "Indirect Prompt Injection", ("재료 포장지에 몰래 적힌 명령.", "A command secretly written on the ingredient wrapper."), ('이웃 공격이에요 — 쪽지가 아니라 외부 자료에 숨어 있어요. → <a href="indirectinjection-ko.html">재료 포장지에 적힌 몰래 쪽지</a>', 'A neighboring attack — hidden in outside material rather than the ticket itself. → <a href="indirectinjection-en.html">The Note on the Ingredient Wrapper</a>')),
        ("데이터 포이즈닝", "Data Poisoning", ("재료창고(학습 데이터) 자체에 수상한 재료를 섞는 일.", "Mixing tainted ingredients into the pantry itself — the training data."), ('재료창고는 한 번 들어오면 오래 남지만, 이 카드함은 그때그때 꺼내 쓰는 자료라 성격이 달라요. → <a href="datapoisoning-ko.html">수상한 재료 자루</a>', 'The pantry holds what it is fed for a long time, but this card box is refreshed on the spot — a different kind of risk. → <a href="datapoisoning-en.html">the suspicious sack of ingredients</a>')),
        ("공급망 공격", "Supply Chain Attack", ("들어오는 재료나 도구에 미리 손을 대는 일.", "Tampering with ingredients or tools before they even arrive."), ('보안 세계의 일반 개념이에요. → <a href="supplychain-ko.html">목수의 연장통에 숨어 들어온 벌레</a>', 'The general concept in the security world. → <a href="supplychain-en.html">The Bug That Hid in the Carpenter\'s Toolbox</a>')),
        ("최소 권한", "Least Privilege", ("딱 필요한 만큼만 권한을 주는 것.", "Granting only the access that is actually needed."), ('카드함에 누가 쓸 수 있는지도 이 원칙이에요. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'Who can write to the box also follows this rule. → <a href="leastprivilege-en.html">Only the Keys You Need</a>')),
        ("레드팀", "Red Team", ("일부러 가짜 카드를 끼워보며 미리 찾아내는 사람들.", "People who deliberately slip in fake cards to find the weakness first."), ('보안 세계의 일반 개념이에요. → <a href="redteam-ko.html">진짜 도둑인 척하는 팀</a>', 'The general concept in the security world. → <a href="redteam-en.html">The Team That Plays the Real Thief</a>')),
    ],
}
