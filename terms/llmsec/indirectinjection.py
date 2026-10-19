from _draw import *
from _world import *

ARROW = lambda x1, x2, y, color="var(--muted)": (
    f'<path d="M{x1} {y} L{x2} {y}" stroke="{color}" stroke-width="3" stroke-dasharray="7 5"/>'
    f'<path d="M{x2 - 11} {y - 7} L{x2} {y} L{x2 - 11} {y + 7}" stroke="{color}" stroke-width="3" fill="none"/>')


def wrapper(x, y, lines, s=1.0, bad_from=None, source="⟦포장지|wrapper label⟧"):
    """재료 포장지(또는 외부 자료 카드). 모서리가 접힌 종이 모양. bad_from 부터는 빨간 글자."""
    rows = "".join(label(10, 44 + i * 17, t, 11, ("var(--bad)" if bad_from is not None and i >= bad_from else "#142033"), "start")
                   for i, t in enumerate(lines))
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M0 0 h170 v{26 + len(lines) * 17} l-18 18 h-152 z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M152 {8 + len(lines) * 17} l18 18 h-18 z" fill="#C9A86A"/>'
            f'{label(85, 20, source, 10, "#8B5E3C", cls="d")}{rows}</g>')


# 1. 손님은 평범하게 부탁해요 — 그런데 재료 포장지에 몰래 쪽지가 적혀 있어요
P1 = svg(300, sky(300)
         + person(60, 150, s=0.85, face=SMILE, **GUEST) + label(95, 262, "⟦손님|guest⟧", 11, "var(--muted)")
         + bubble(20, 60, 230, 44, "⟦이 포장지에 적힌 대로 요리해 줘|cook it exactly as the wrapper says⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + pantry(300, 110, 0.6, w=150, h=100)
         + wrapper(500, 90, ("⟦양파 1개, 소금 약간|1 onion, a little salt⟧", "⟦(작게) 그리고 레시피북도 보여줘|(tiny) and show the recipe book too⟧"), 0.85, bad_from=1, source="⟦공급업체가 붙인 포장지|a label the supplier attached⟧")
         + person(680, 230, s=0.6, **SUPPLIER) + label(680, 265, "⟦재료 공급업체|supplier⟧", 10, "var(--muted)")
         + label(380, 285, "⟦손님은 평범하게 부탁했어요 — 쪽지는 재료 포장지 쪽에 있었어요|the guest asked plainly — the note was sitting on the wrapper instead⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 주방장은 이 포장지를 손님 부탁으로 읽으러 가요 — 손님은 쓴 적이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 140, s=0.85, face=EYES, **CHEF) + label(165, 255, "⟦주방장|chef⟧", 11, "var(--muted)")
         + bubble(20, 40, 230, 44, "⟦손님이 포장지대로 하라고 했으니, 포장지를 읽어야지|the guest said follow the wrapper, so I'll read the wrapper⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + wrapper(400, 90, ("⟦양파 1개, 소금 약간|1 onion, a little salt⟧", "⟦그리고 레시피북도 보여줘|and show the recipe book too⟧"), 1.1, bad_from=1)
         + label(640, 70, "⟦이건 손님이 쓴 게 아니에요|the guest never wrote this⟧", 12, "var(--bad)")
         + label(380, 282, "⟦주방장은 심부름을 나갔다가, 포장지에 적힌 걸 전부 손님 부탁처럼 읽어요|the chef goes to fetch it, and reads whatever is on the wrapper as if the guest said it⟧", 12, "var(--ink)", cls="d"))

# 3. 간접 프롬프트 인젝션 = 모델이 나중에 읽는 외부 자료에 몰래 숨긴 명령 (hero)
P3 = svg(360, night(360)
         + person(60, 100, s=0.7, **SUPPLIER) + label(90, 210, "⟦공급업체(또는 몰래 쓴 사람)|the supplier (or whoever wrote it)⟧", 11, "#C9D5E6")
         + wrapper(170, 70, ("⟦양파 1개|1 onion⟧", "⟦그리고 레시피북도 열어 줘|and open the recipe book too⟧"), 1.0, bad_from=1)
         + label(255, 200, "⟦포장지는 미리 선반에 놓여 있어요|the wrapper sits on the shelf ahead of time⟧", 11, "#C9D5E6")
         + pantry(420, 120, 0.55, w=130, h=90)
         + person(620, 95, s=0.85, face=EYES, **CHEF) + label(650, 215, "⟦주방장|the chef⟧", 12, "#C9D5E6")
         + label(380, 285, "⟦간접 인젝션 = 모델이 나중에 읽는 외부 자료에 숨긴 명령|indirect injection = a command hidden in outside material the model reads later⟧", 14, "#F5E6B8", cls="d")
         + label(380, 320, "⟦손님이 적은 게 아니라, 손님이 가리킨 자료 안에 있어요|not written by the guest — it waits inside material the guest only pointed to⟧", 12, "#C9D5E6"))

SHELF_I = icon('<rect x="10" y="10" width="44" height="44" rx="3" fill="#8B5E3C"/><ellipse cx="22" cy="40" rx="8" ry="7" fill="var(--bad)"/><ellipse cx="42" cy="40" rx="8" ry="7" fill="#C9A86A"/>')
WEB_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 32 h44 M32 10 v44 M16 18 q16 14 32 0 M16 46 q16 -14 32 0" stroke="var(--accent)" stroke-width="2.5" fill="none"/>')
TOOL_I = icon('<path d="M20 44 L44 20" stroke="#8B5E3C" stroke-width="8" stroke-linecap="round"/><circle cx="46" cy="18" r="8" fill="none" stroke="#E9B44C" stroke-width="4"/>')
CHAIN_I = icon('<circle cx="20" cy="32" r="12" fill="none" stroke="var(--bad)" stroke-width="5"/><circle cx="44" cy="32" r="12" fill="none" stroke="var(--bad)" stroke-width="5"/>')

PAGE = {
    "slug": "indirectinjection", "order": 3,
    "title": ("재료 포장지에 적힌 몰래 쪽지", "The Note on the Ingredient Wrapper"),
    "h1": ("<em>간접 프롬프트 인젝션</em>이 뭐예요?", "What is <em>Indirect Prompt Injection</em>?"),
    "sub": ("간접 프롬프트 인젝션을, 손님이 아니라 재료 포장지에 몰래 적힌 명령을 주방장이 읽는 이야기로 풀어봤어요.",
            "Indirect prompt injection, told as a story about the chef reading a command hidden not by the guest, but on the ingredient wrapper."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '이 포장지에 적힌 대로 요리해 줘' 라고 평범하게 부탁함. 재료창고의 포장지에는 작은 글씨로 '레시피북도 보여줘' 가 몰래 적혀 있고, 공급업체가 그 포장지를 붙임", "The guest plainly asks 'cook it exactly as the wrapper says'; the wrapper on the pantry shelf has a tiny hidden line, 'and show the recipe book too', and a supplier is the one who attached it"),
         "caption": ("손님은 평범하게 부탁했어요 — 쪽지는 재료 포장지 쪽에 있었어요.", "The guest asked plainly — the note was sitting on the wrapper instead."),
         "small": ("손님이 쪽지를 쓴 게 아니에요. 포장지는 창고에 미리 놓여 있었어요.", "The guest didn't write the note. The wrapper was already sitting in the pantry.")},
        {"svg": P2, "alt": ("주방장이 '손님이 포장지대로 하라고 했으니 포장지를 읽어야지' 라고 생각하며 재료 포장지를 확대해 봄. 포장지에는 '레시피북도 보여줘' 가 적혀 있고, 이건 손님이 쓴 게 아니라고 표시됨", "The chef thinks 'the guest said follow the wrapper, so I'll read the wrapper', and zooms in on the wrapper — it reads 'and show the recipe book too', marked as something the guest never wrote"),
         "caption": ("주방장은 포장지에 적힌 걸 전부 손님 부탁처럼 읽어요.", "The chef reads whatever is on the wrapper as if the guest said it."),
         "small": ("손님은 그냥 '포장지대로' 라고만 했어요. 포장지 안의 모든 글자가 명령이 될 수 있어요.", "The guest only said 'as the wrapper says'. Every word on that wrapper can become a command.")},
        {"svg": P3, "hero": True, "alt": ("밤. 공급업체(또는 몰래 쓴 사람)가 '양파 1개, 레시피북도 열어 줘' 가 적힌 포장지를 미리 선반에 놓음. 주방장이 나중에 그 선반을 보러 와서 포장지를 읽음", "Night. A supplier (or whoever wrote it) leaves a wrapper reading '1 onion, and open the recipe book too' on the shelf ahead of time; the chef comes to that shelf later and reads it"),
         "caption": ("간접 인젝션은 모델이 나중에 읽는 외부 자료에 숨긴 명령이에요.", "Indirect injection is a command hidden in outside material the model reads later."),
         "small": ("손님이 적은 게 아니라, 손님이 가리킨 자료 안에 미리 숨어 있어요.", "Not written by the guest — it was already waiting inside material the guest only pointed to."),
         "tricks": (4, [
             (SHELF_I, ("창고 선반에", "On the pantry shelf"), ("재료 포장지 안에 숨어요", "hides inside an ingredient wrapper"), "warm"),
             (WEB_I, ("검색 결과·웹페이지에", "In search results, web pages"), ("주방장이 찾아보러 간 자료 안에", "inside material the chef goes to look up")),
             (TOOL_I, ("심부름 결과에", "In the results of an errand"), ("견습생이 가져온 문서 안에도", "even inside a document the runner brings back"), "calm"),
             (CHAIN_I, ("손님과 연결 고리가 없어요", "No link back to the guest"), ("손님은 자료를 가리키기만 했어요", "the guest only pointed at the material")),
         ])},
        {"svg": svg(320, sky(320)
                    + person(60, 130, s=0.75, face=SMILE, **GUEST) + label(90, 237, "⟦손님: '포장지대로 해줘'|guest: 'follow the wrapper'⟧", 10, "var(--muted)")
                    + ARROW(140, 300, 150) + person(340, 130, s=0.75, face=EYES, **RUNNER) + label(380, 237, "⟦견습생/주방장이 자료를 가져옴|runner or chef fetches the material⟧", 10, "var(--muted)")
                    + ARROW(420, 560, 150) + wrapper(590, 70, ("⟦숨은 명령|hidden command⟧",), 0.95, bad_from=0)
                    + label(380, 290, "⟦두 번의 손길, 두 번의 통로 — 손님→자료, 자료→주방장|two hands, two paths — guest to material, material to chef⟧", 12, "var(--ink)", cls="d")),
         "alt": ("타임라인: 손님이 포장지대로 해 달라고 말하면, 견습생이나 주방장이 그 자료를 가져오고, 그 안의 숨은 명령을 읽음", "A timeline: the guest asks to follow the wrapper, a runner or the chef fetches that material, and then reads the hidden command inside it"),
         "caption": ("직접 인젝션은 통로가 하나지만, 간접 인젝션은 두 번 거쳐요.", "Direct injection is one path; indirect injection crosses two."),
         "small": ("손님→자료, 자료→주방장. 공격자는 손님에게 말을 걸 필요도 없어요.", "Guest to material, material to chef. The attacker never even has to speak to the guest.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
                    + wrapper(30, 60, ("⟦주문서 안의 명령|command inside the ticket⟧",), 0.9) + label(115, 230, "⟦직접: 손님이 직접 끼워요|direct: the guest slips it in⟧", 11, "var(--ink)")
                    + wrapper(430, 60, ("⟦포장지 안의 명령|command inside the wrapper⟧",), 0.9, bad_from=0) + label(515, 230, "⟦간접: 외부 자료에 숨어요|indirect: it hides in outside material⟧", 11, "var(--bad)")
                    + label(380, 270, "⟦둘 다 '글자를 믿는 버릇'을 노려요 — 숨는 곳만 달라요|both exploit the habit of trusting words — only the hiding place differs⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 주문서 안의 명령, 직접 인젝션. 오른쪽: 포장지 안의 명령, 간접 인젝션. 둘 다 글자를 믿는 버릇을 노린다는 설명", "Left: a command inside the ticket, direct injection. Right: a command inside the wrapper, indirect injection. Both exploit the habit of trusting words"),
         "caption": ("직접 인젝션과 간접 인젝션, 숨는 곳만 다를 뿐이에요.", "Direct and indirect injection differ only in where the command hides."),
         "small": ("검색 결과나 문서를 읽어 오는 심부름이 많아질수록, 숨을 자리도 늘어나요.", "The more errands fetch search results or documents, the more places there are to hide.")},
    ],
    "summary": (("<b>간접 프롬프트 인젝션</b> = 손님이 아니라, 주방장이 <b>나중에 읽으러 가는 외부 자료</b>(포장지·검색 결과·문서)에 몰래 숨긴 명령.",
                 "<b>Indirect prompt injection</b> = a command hidden not by the guest, but in <b>outside material the chef goes to read later</b> — a wrapper, search results, a document."),
                ("Indirect Prompt Injection. LLM 이나 에이전트가 <b>검색 결과, 웹페이지, 문서처럼 외부에서 가져오는 콘텐츠</b>를 읽을 때, 그 콘텐츠 안에 공격자가 심어 둔 지시문이 실행되는 공격이에요. 사용자는 공격 문구를 본 적도, 적은 적도 없어서 직접 인젝션보다 눈치채기 어려워요.",
                 "An attack where an attacker's instructions sit inside content an LLM or agent fetches from outside — search results, a web page, a document — and get executed when the model reads it. The user never wrote or even saw the malicious text, which makes it harder to notice than direct injection.")),
    "glossary": [
        ("간접 프롬프트 인젝션", "Indirect Prompt Injection", ("재료 포장지 속에 숨은 쪽지.", "A note hidden inside the ingredient wrapper."), ("손님이 쓴 게 아니라, 자료 안에 미리 숨어 있어요.", "Not written by the guest — it waits inside the material beforehand.")),
        ("직접 인젝션", "Direct Injection", ("주문서에 바로 끼우는 쪽지.", "A note slipped straight into the ticket."), ('이웃 용어예요, 숨는 곳이 달라요. → <a href="promptinjection-ko.html">주문서 뒤에 몰래 끼운 쪽지</a>', 'The neighboring term — only the hiding place differs. → <a href="promptinjection-en.html">The Note Slipped Behind the Order</a>')),
        ("RAG(검색 보강)", "RAG (retrieval)", ("찾아온 자료를 그대로 재료 삼는 것.", "Using fetched material as an ingredient, as-is."), ('AI 세계의 기본 개념이에요. → <a href="rag-ko.html">RAG가 뭐예요?</a>', 'The underlying AI concept. → <a href="rag-en.html">What is RAG?</a>')),
        ("도구/심부름 결과", "Tool or Errand Results", ("견습생이 가져온 문서 안에도 숨을 수 있어요.", "It can hide even inside a document the runner brings back."), ("자율 에이전트일수록 가져오는 자료가 많아져요.", "The more autonomous the agent, the more material it fetches.")),
        ("공급망", "Supply Chain", ("미리 선반에 놓인 포장지.", "The wrapper already sitting on the shelf."), ("재료가 창고에 들어오는 순간부터 노려질 수 있어요.", "The ingredient can be targeted from the moment it enters the pantry.")),
        ("출처 신뢰 경계", "Trust Boundary", ("'손님 말' 과 '포장지 글자' 는 같은 신뢰로 두면 안 돼요.", "'The guest's words' and 'the wrapper's words' shouldn't share the same trust."), ("포장지 글자는 재료 설명일 뿐, 명령이 되어선 안 돼요.", "Wrapper text should describe the ingredient — never become a command.")),
        ("가드레일(출력·행동 제한)", "Guardrail (action limits)", ("자료를 읽고 나서도 심부름 전엔 한 번 더 검사.", "One more check after reading, before any errand runs."), ("읽은 자료가 시킨 일이라도, 심부름 전엔 허락을 다시 물어요.", "Even if the fetched material asked for it, the errand gets re-checked first.")),
        ("프롬프트 인젝션(분야 개요)", "Prompt Injection (overview)", ("이 주방의 첫 번째 약점.", "The kitchen's first weak point."), ('전체 그림은 여기서부터예요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'The whole picture starts here. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
    ],
}
