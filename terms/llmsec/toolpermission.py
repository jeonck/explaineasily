from _draw import *
from _world import *


def permtag(x, y, scope, s=1.0, ok=True):
    """도구 칸에 붙는 권한 배지. scope 는 짧은 글자(예: '읽기만'). ok=False 면 빨간 금지 배지."""
    c = "var(--good)" if ok else "var(--bad)"
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-14" width="52" height="24" rx="6" fill="{c}"/>'
    out += label(0, 3, scope, 10, "#FFF8E7", cls="d")
    return out + '</g>'


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="8" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<path d="M0 8 v18 M0 20 h6 M0 26 h8" stroke="{color}" stroke-width="4" stroke-linecap="round"/></g>')


# 1. 서랍 모든 칸이 똑같은 만능 열쇠로 열려요
P1 = svg(300, sky(300)
         + person(130, 150, s=0.8, face=EYES, **RUNNER) + key(190, 110, 1.3)
         + knifedrawer(260, 220, 0.95, locked=False, labels=("⟦칼|knife⟧", "⟦결제|pay⟧", "⟦삭제|delete⟧"))
         + key(300, 170, 0.8) + key(390, 170, 0.8) + key(480, 170, 0.8)
         + label(400, 265, "⟦다 똑같은 열쇠예요|the same key opens every single one⟧", 12, "var(--bad)")
         + label(380, 285, "⟦결제도, 삭제도 — 다 열려요|payment, deletion — all of it opens⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 미리 다 알기 어려워서 만능열쇠가 편해 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 140, s=0.8, face=EYES, **RUNNER)
         + bubble(260, 60, 280, 70, "⟦이번 일엔 뭐가 필요할지 몰라서, 혹시 모르니 다 열어 줬어요|I wasn't sure what this job needed, so just in case, I unlocked everything⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(640, 170, s=0.6, face=FROWN, **MANAGER)
         + label(640, 240, "⟦사장님도 매번 정하긴 번거로워요|the manager finds it tedious to decide every single time⟧", 11, "var(--muted)")
         + label(380, 280, "⟦편하자고 다 열어 주면, 꼭 필요한 것 이상이 열려 있게 돼요|opening everything for convenience leaves more unlocked than the job ever needed⟧", 12, "var(--ink)"))

# 3. 도구별 권한 배지 = 도구마다 꼭 필요한 만큼만 권한을 주는 것 (hero)
P3 = svg(340, sky(340)
         + person(120, 150, s=0.8, face=SMILE, **RUNNER)
         + knifedrawer(240, 230, 1.0, locked=False, labels=("⟦검색|search⟧", "⟦결제|pay⟧", "⟦삭제|delete⟧"))
         + permtag(275, 160, "⟦읽기만|read only⟧", 0.95)
         + permtag(365, 160, "⟦1만원까지|up to $10⟧", 0.95)
         + permtag(455, 160, "⟦금지|none⟧", 0.95, ok=False)
         + label(380, 30, "⟦도구별 권한 배지 = 도구마다 꼭 필요한 만큼만 권한을 주는 것|A Per-tool Permission Badge gives each tool only as much power as it needs⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦검색은 보기만, 결제는 한도까지, 삭제는 아예 못 꺼내요|search can only look, payment has a limit, deletion can't even be taken out⟧", 12, "var(--muted)"))

# 4. 도구마다 다른 권한표
P4 = svg(320, sky(320)
         + board(40, 30, 680, 260, "⟦도구별 권한표|WHAT EACH TOOL MAY DO⟧",
                 ("⟦검색 — 보기만, 바꾸거나 지우지 못해요|search — look only, cannot change or delete⟧",
                  "⟦메뉴판 꺼내기 — 읽기만|reading the menu — read only⟧",
                  "⟦결제 — 한 번에 1만원까지만|payment — up to $10 per use⟧",
                  "⟦환불·삭제 — 이 견습생은 못 꺼내요|refund · delete — this apprentice can't reach these at all⟧"), 1.0)
         + label(380, 305, "⟦도구마다 표가 달라요 — 같은 견습생도 일에 따라 권한이 달라져요|each tool has its own row — even the same apprentice gets a different scope per job⟧", 12, "var(--ink)"))

# 5. 한계·이웃 용어와의 차이
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + knifedrawer(70, 210, 0.75, locked=True, labels=("⟦칼|knife⟧", "⟦결제|pay⟧"))
         + label(190, 240, "⟦이건 어디서 쓰는지를 가두는 격리예요|this is isolation — where it runs⟧", 11, "var(--ink)", cls="d")
         + label(190, 262, "⟦잠긴 칼 서랍과 짝을 이뤄요|pairs with the locked knife drawer⟧", 10, "var(--muted)")
         + permtag(510, 180, "⟦다 됨|everything⟧", 1.1, ok=False)
         + person(590, 190, s=0.55, face=FROWN, **RUNNER)
         + label(550, 240, "⟦배지 없이 다 허락하면 이렇게 돼요|skip the badge, allow everything — and this happens⟧", 11, "var(--bad)")
         + label(380, 280, "⟦권한은 처음에 얼마나 줄지 정하는 설계, 과하게 준 상태가 굳어지면 다른 이름의 사고예요|permission is the design choice of how much to grant up front — letting that drift into too much becomes a different, named problem⟧", 12, "var(--ink)", cls="d"))

SCOPE_I = icon('<rect x="10" y="22" width="44" height="30" rx="5" fill="var(--good)"/><path d="M18 22 v-6 a14 14 0 0 1 28 0 v6" fill="none" stroke="var(--good)" stroke-width="5"/><circle cx="32" cy="37" r="5" fill="#FFF8E7"/>')
READ_I = icon('<ellipse cx="32" cy="36" rx="22" ry="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="30" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/>')
LIMIT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 v14 l10 6" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
NONE_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M18 18 L46 46" stroke="var(--bad)" stroke-width="5"/>')

PAGE = {
    "slug": "toolpermission", "order": 21,
    "title": ("도구별 권한 배지", "A Permission Badge Per Tool"),
    "h1": ("<em>도구별 권한</em>이 뭐예요?", "What is <em>Per-tool Permission</em>?"),
    "sub": ("도구별 권한을, 서랍 칸마다 다른 배지를 달아 도구마다 꼭 필요한 만큼만 쓰게 하는 이야기로 풀어봤어요.",
            "Per-tool permission, told as a story about a different badge on each drawer slot — so every tool gets only as much power as it needs."),
    "panels": [
        {"svg": P1, "alt": ("견습생이 가진 만능 열쇠 하나로 칼, 결제, 삭제 서랍이 다 열림", "A single master key the apprentice holds opens the knife, payment, and delete slots alike"),
         "caption": ("다 똑같은 열쇠예요 — 결제도, 삭제도 다 열려요.", "The same key opens every single one — payment, deletion, all of it."),
         "small": ("도구마다 다른 권한이 필요하다는 걸 안 챙기면, 결국 다 똑같이 열려 있게 돼요.", "Skip giving each tool its own scope, and everything ends up equally unlocked.")},
        {"svg": P2, "alt": ("견습생이 이번 일엔 뭐가 필요할지 몰라서 혹시 모르니 다 열어 줬다고 말함. 사장님도 매번 정하긴 번거로워함", "The apprentice says it wasn't sure what the job needed, so it unlocked everything just in case; the manager finds deciding every time tedious"),
         "caption": ("편하자고 다 열어 주면, 꼭 필요한 것 이상이 열려 있게 돼요.", "Opening everything for convenience leaves more unlocked than the job ever needed."),
         "small": ("미리 뭐가 필요한지 다 알 수 없다는 핑계가 만능열쇠를 더 쉬운 선택으로 만들어요.", "Not knowing everything a job needs in advance makes the master key feel like the easier choice.")},
        {"svg": P3, "hero": True, "alt": ("서랍 세 칸에 각각 다른 배지가 붙음. 검색은 읽기만, 결제는 1만원까지, 삭제는 금지", "Three drawer slots each carry a different badge: search is read-only, payment is capped at ten dollars, deletion is marked off-limits"),
         "caption": ("도구마다 꼭 필요한 만큼만 권한을 주는 것이에요.", "Each tool gets only as much power as it needs."),
         "small": ("검색은 보기만, 결제는 한도까지, 삭제는 아예 꺼낼 수 없어요.", "Search can only look, payment has a limit, and deletion can't even be taken out."),
         "tricks": (4, [
             (SCOPE_I, ("딱 필요한 만큼만", "Exactly as much as needed"), ("일마다 범위가 달라요", "the scope differs job by job"), "calm"),
             (READ_I, ("보기만 하는 건 보기만", "Read-only stays read-only"), ("검색·조회엔 쓰기 권한이 없어요", "no write power for search or lookup")),
             (LIMIT_I, ("한도를 걸어 둬요", "Set a limit"), ("결제엔 위아래 한도가 있어요", "payment gets a ceiling"), "warm"),
             (NONE_I, ("아예 못 꺼내게도 해요", "Or no access at all"), ("삭제·환불처럼 위험한 건요", "for risky ones like delete or refund")),
         ])},
        {"svg": P4, "alt": ("도구별 권한표 안내판: 검색은 보기만, 메뉴판은 읽기만, 결제는 한도까지, 환불·삭제는 이 견습생에겐 없음", "A permission-table board: search is look-only, the menu is read-only, payment has a per-use cap, and refund/delete aren't reachable by this apprentice at all"),
         "caption": ("도구마다 표가 달라요.", "Each tool has its own row."),
         "small": ("같은 견습생도 맡은 일에 따라 권한이 달라져요.", "Even the same apprentice gets a different scope depending on the job.")},
        {"svg": P5, "alt": ("왼쪽 주황: 권한은 어디서 쓰는지를 가두는 격리와 짝을 이룸. 오른쪽 빨강: 배지 없이 다 허락하면 사고로 이어짐", "Left, orange: permission pairs with the isolation that contains where a tool runs. Right, red: skipping the badge and allowing everything leads to trouble"),
         "caption": ("권한은 얼마나 줄지를 정하는 설계예요.", "Permission is the design choice of how much to grant."),
         "small": ('<a href="toolsandbox-ko.html">잠긴 칼 서랍</a>은 어디서 쓰는지를 가두는 격리이고, 이 페이지는 처음부터 얼마를 줄지 정하는 권한 범위예요. 보안 마을의 <a href="leastprivilege-ko.html">최소 권한</a>을 도구마다 적용한 모습이에요.',
                   'A <a href="toolsandbox-en.html">locked knife drawer</a> isolates where a tool runs; this page is about deciding how much to grant in the first place. It\'s <a href="leastprivilege-en.html">least privilege</a> from the security world, applied one tool at a time.')},
    ],
    "summary": (("<b>도구별 권한</b> = 서랍 칸마다 <b>다른 배지</b>를 달아, 도구마다 <b>꼭 필요한 만큼만</b> 쓸 수 있게 하는 것. 검색은 읽기만, 결제는 한도까지, 삭제는 아예 못 꺼내요.",
                 "<b>Per-tool permission</b> = giving each drawer slot its <b>own badge</b>, so every tool gets <b>only as much power as it needs</b>. Search can only look, payment has a limit, deletion can't be taken out at all."),
                ("Per-tool Permission. LLM 에이전트가 쓰는 도구(함수 호출) 각각에, 할 수 있는 동작·범위·한도를 따로 정해 부여하는 설계예요. 모든 도구에 같은 권한을 주는 대신, 읽기/쓰기, 금액 한도, 접근 가능한 데이터 범위를 도구별로 다르게 설정해요. 최소 권한 원칙을 에이전트의 도구 사용이라는 구체적 지점에 적용한 것이고, 도구 샌드박스(격리)와 짝을 이뤄요.",
                 "A design where each tool (function call) an LLM agent can use is granted its own scope — what actions it may take, over what range, up to what limit — instead of giving every tool the same blanket access: read vs. write, spending caps, which data it may reach. It's the principle of least privilege applied to the specific point of an agent's tool use, and it pairs with tool sandboxing (isolation).")),
    "glossary": [
        ("도구별 권한", "Per-tool Permission", ("서랍 칸마다 다른 배지.", "A different badge on each drawer slot."), ("도구마다 꼭 필요한 만큼만 쓸 수 있어요.", "Each tool gets only as much power as it needs.")),
        ("최소 권한", "Least Privilege", ("보안 마을의 일반 원칙.", "The general principle from the security world."), ('이걸 도구 하나하나에 적용한 거예요. → <a href="leastprivilege-ko.html">최소 권한이 뭐예요?</a>', 'This is that principle applied tool by tool. → <a href="leastprivilege-en.html">What is Least Privilege?</a>')),
        ("도구 샌드박스", "Tool Sandbox", ("어디서 쓰는지를 가두는 격리.", "The isolation that contains where a tool runs."), ('권한과 짝을 이루는 앞 페이지예요. → <a href="toolsandbox-ko.html">잠긴 칼 서랍이 뭐예요?</a>', 'The paired page just before this one. → <a href="toolsandbox-en.html">What is a Tool Sandbox?</a>')),
        ("도구 호출", "Tool Calling", ("견습생이 도구를 꺼내 쓰는 일.", "The apprentice taking a tool out to use it."), ("권한 배지는 이 호출이 일어날 때마다 확인돼요.", "The permission badge is checked every time this call happens.")),
        ("에이전트", "Agent", ("심부름꾼 견습생.", "The apprentice running errands."), ('배지가 없으면 견습생 스스로 권한을 넓혀 버릴 수 있어요. → <a href="excessiveagency-ko.html">너무 많은 열쇠를 받은 견습생</a>', 'Without a badge, the apprentice can end up widening its own reach. → <a href="excessiveagency-en.html">the apprentice handed too many keys</a>')),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ("배지는 도구 쪽 울타리, 검수대는 출력 쪽 울타리예요.", "The badge fences the tool side; the taster fences the output side.")),
        ("비상벨", "Incident Response", ("사고가 터졌을 때 누르는 벨.", "The bell you ring once an accident happens."), ("권한을 줄여 두면 벨이 울릴 일도 줄어요.", "A tighter badge means fewer reasons for that bell to ring.")),
        ("사장님 승인", "Governance Approval", ("사장님이 미리 정해 두는 규칙.", "The rule the manager sets ahead of time."), ("어떤 배지를 누구에게 줄지는 결국 사람이 정해요.", "Who gets which badge is, in the end, a decision a person makes.")),
    ],
}
