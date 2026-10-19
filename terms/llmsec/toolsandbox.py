from _draw import *
from _world import *


def spark(x, y, s=1.0, color="var(--bad)"):
    return f'<path d="M{x} {y - 10*s} l{5*s} {10*s} h-{10*s}z" fill="{color}"/><circle cx="{x}" cy="{y - 2*s}" r="{2.2*s}" fill="{color}"/>'


# 1. 서랍이 열려 있으면 뭐든 다 꺼내 써요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=EYES, **RUNNER)
         + '<rect x="230" y="190" width="170" height="40" rx="3" fill="#5A3B22"/>'
         + '<rect x="238" y="194" width="50" height="32" rx="2" fill="#8B5E3C"/><rect x="294" y="194" width="50" height="32" rx="2" fill="#8B5E3C"/><rect x="350" y="194" width="42" height="32" rx="2" fill="#8B5E3C"/>'
         + label(315, 250, "⟦서랍이 다 열려 있어요|the drawer is wide open⟧", 12, "var(--bad)")
         + spark(470, 170, 1.2) + label(500, 175, "⟦불!|FIRE!⟧", 14, "var(--bad)", cls="d")
         + label(380, 285, "⟦견습생이 칼도, 불도, 전화도 마음대로 꺼내 써요|the apprentice grabs the knife, the flame, the phone — whatever it wants⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 심부름꾼은 혼자 다니는데, 뭘 쓸지 미리 못 가둬두면 사고가 커져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 140, s=0.8, face=EYES, **RUNNER)
         + label(140, 220, "⟦혼자 심부름 다녀요|runs errands alone⟧", 11, "var(--muted)")
         + bubble(260, 60, 260, 70, "⟦이번엔 칼만 쓸까, 불도 쓸까, 전화도 걸까 — 미리 다 알 수 없어요|will it need just the knife, or the flame too, or the phone — you can't know all of it ahead of time⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(620, 170, s=0.6, face=FROWN, **MANAGER)
         + label(620, 240, "⟦사장님도 매번 옆에서 볼 수 없어요|the manager can't watch every single errand⟧", 11, "var(--muted)")
         + label(380, 280, "⟦도구 하나가 말썽을 부려도 다른 도구까지 다 같이 열려 있으면 피해가 번져요|if one tool misbehaves while everything else stays open too, the damage spreads⟧", 12, "var(--ink)"))

# 3. 잠긴 칼 서랍 = 도구 실행 환경을 격리해서 피해를 제한하는 것 (hero)
P3 = svg(340, sky(340)
         + person(130, 150, s=0.8, face=EYES, **RUNNER)
         + knifedrawer(260, 230, 1.0, locked=True, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧"))
         + '<rect x="330" y="150" width="30" height="24" rx="3" fill="#8B5E3C"/><circle cx="345" cy="162" r="3" fill="#E9B44C"/>'
         + label(345, 190, "⟦한 칸만 열려요|only one slot opens⟧", 10, "var(--ink)")
         + spark(345, 130, 0.8, "var(--good)")
         + '<rect x="200" y="190" width="400" height="90" rx="6" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 5"/>'
         + label(400, 300, "⟦사고가 나도 이 칸 안에서만|even an accident stays inside this one slot⟧", 11, "var(--good)")
         + label(380, 30, "⟦잠긴 칼 서랍 = 도구 실행 환경을 격리해서 피해를 가둬두는 것|A Tool Sandbox isolates where a tool runs — so damage stays contained⟧", 13, "var(--ink)", cls="d"))

# 4. 서랍 칸 하나씩, 쓴 다음 다시 잠겨요
P4 = svg(330, sky(330)
         + board(40, 30, 320, 260, "⟦서랍 사용 순서|HOW THE DRAWER WORKS⟧",
                 ("⟦① 견습생이 한 칸을 요청해요|① the apprentice asks for one slot⟧",
                  "⟦② 그 칸만 열려요, 나머진 잠긴 채|② only that slot opens, rest stay locked⟧",
                  "⟦③ 그 안에서만 도구를 써요|③ the tool is used inside that slot only⟧",
                  "⟦④ 다 쓰면 칸이 다시 잠겨요|④ the slot locks again when done⟧"), 1.0)
         + knifedrawer(430, 225, 0.7, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧"))
         + label(430, 40, "⟦한 번에 한 칸씩|one slot at a time⟧", 12, "var(--ink)", cls="d")
         + label(500, 305, "⟦다른 칸은 그 사이에도 계속 잠겨 있어요|the other slots stay locked the whole time⟧", 11, "var(--muted)"))

# 5. 한계·이웃 용어와의 차이
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + knifedrawer(70, 200, 0.75, locked=True, labels=("⟦칼|knife⟧", "⟦불|flame⟧"))
         + label(190, 260, "⟦격리 — 어디서 쓰는지|isolation — where it runs⟧", 12, "var(--ink)", cls="d")
         + label(190, 282, "⟦칸이 터져도 주방 전체로는 안 퍼져요|if a slot breaks, it doesn't spread to the whole kitchen⟧", 11, "var(--muted)")
         + knifedrawer(460, 200, 0.75, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧"))
         + '<circle cx="500" cy="170" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M500 162 v8 M500 174 h0.2" stroke="var(--accent)" stroke-width="3"/>'
         + label(575, 260, "⟦권한 — 무엇까지 허락했는지|permission — what it's allowed to do⟧", 12, "var(--ink)", cls="d")
         + label(575, 282, "⟦그건 옆 페이지, 도구별 권한 배지예요|that's the next page — a permission badge per tool⟧", 11, "var(--muted)")
         + label(380, 300, "⟦격리는 터진 걸 가두는 것이고, 권한은 처음부터 얼마나 줄지를 정하는 것이에요|isolation contains a break; permission decides how much to grant in the first place⟧", 12, "var(--ink)", cls="d"))

LOCK_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="var(--accent)"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" fill="none" stroke="var(--accent)" stroke-width="5"/>')
ONE_I = icon('<rect x="8" y="22" width="48" height="24" rx="4" fill="#8B5E3C"/><rect x="18" y="26" width="12" height="16" rx="2" fill="var(--good)"/><rect x="34" y="26" width="12" height="16" rx="2" fill="#5A3B22"/>')
WALL_I = icon('<rect x="8" y="10" width="20" height="44" rx="3" fill="var(--good)"/><rect x="36" y="10" width="20" height="44" rx="3" fill="var(--bad)"/><path d="M32 10 v44" stroke="var(--line)" stroke-width="4"/>')
RELOCK_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="#5A3B22"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" fill="none" stroke="#5A3B22" stroke-width="5"/><path d="M8 48 a24 24 0 0 1 48 0" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="4 4"/>')

PAGE = {
    "slug": "toolsandbox", "order": 20,
    "title": ("잠긴 칼 서랍", "The Locked Knife Drawer"),
    "h1": ("<em>도구 샌드박스</em>가 뭐예요?", "What is a <em>Tool Sandbox</em>?"),
    "sub": ("도구 샌드박스를, 견습생이 도구를 한 칸씩만 꺼내 쓰고 다 쓰면 다시 잠기는 칼 서랍 이야기로 풀어봤어요.",
            "A tool sandbox, told as a story about a drawer that opens one slot at a time for the apprentice — and locks again when done."),
    "panels": [
        {"svg": P1, "alt": ("견습생 앞에 서랍이 다 열려 있고, 불이 나서 경고가 뜸", "A drawer is wide open in front of the apprentice, and a fire breaks out as a warning"),
         "caption": ("견습생이 칼도, 불도, 전화도 마음대로 꺼내 써요.", "The apprentice grabs the knife, the flame, the phone — whatever it wants."),
         "small": ("서랍이 다 열려 있으면, 도구 하나가 말썽을 부려도 막을 길이 없어요.", "With the whole drawer open, there's nothing to stop one tool's trouble from spreading.")},
        {"svg": P2, "alt": ("혼자 심부름 다니는 견습생이 이번엔 뭘 쓸지 미리 알 수 없다고 말하고, 사장님도 매번 옆에서 볼 수 없음", "The apprentice, running errands alone, says it can't know ahead what it'll need; the manager can't watch every errand either"),
         "caption": ("도구 하나가 말썽을 부려도 다 같이 열려 있으면 피해가 번져요.", "If one tool misbehaves while everything else stays open too, the damage spreads."),
         "small": ("견습생은 스스로 다음 할 일을 정해요 — 그래서 미리 다 가둬 둘 필요가 있어요.", "The apprentice decides its own next step — which is exactly why things need to be locked down ahead of time.")},
        {"svg": P3, "hero": True, "alt": ("견습생이 서랍 한 칸만 열어 도구를 쓰고, 그 칸만 녹색 점선으로 둘러싸여 사고를 가둠", "The apprentice opens just one drawer slot to use a tool, and that slot alone is ringed in a green dashed line containing the accident"),
         "caption": ("도구 실행 환경을 격리해서 피해를 가둬두는 것이에요.", "A tool sandbox isolates where a tool runs — so damage stays contained."),
         "small": ("한 번에 한 칸만 열리고, 사고가 나도 그 칸 밖으로는 안 퍼져요.", "Only one slot opens at a time, and even an accident stays inside that one slot."),
         "tricks": (4, [
             (ONE_I, ("한 번에 한 칸만", "One slot at a time"), ("나머진 계속 잠겨 있어요", "the rest stay locked")),
             (LOCK_I, ("꺼내 쓰는 순간만 열려요", "Opens only for the moment of use"), ("쓰고 나면 다시 잠겨요", "locks again right after"), "calm"),
             (WALL_I, ("칸 사이엔 벽이 있어요", "There's a wall between slots"), ("한 칸이 터져도 옆 칸은 안전해요", "one slot breaking doesn't touch the next"), "warm"),
             (RELOCK_I, ("처음 상태로 되돌려요", "Resets back to locked"), ("다음 번도 다시 한 칸씩", "next time, one slot again")),
         ])},
        {"svg": P4, "alt": ("서랍 사용 순서판: 요청, 한 칸만 열림, 그 안에서만 사용, 다시 잠김의 네 단계", "A how-it-works board: request, only that slot opens, used only inside it, locks again — four steps"),
         "caption": ("서랍 칸 하나씩, 쓴 다음 다시 잠겨요.", "One slot at a time — and it locks again after use."),
         "small": ("요청한 칸만 열리고, 나머지는 그 사이에도 계속 잠겨 있어요.", "Only the requested slot opens; the rest stay locked the whole time.")},
        {"svg": P5, "alt": ("왼쪽 초록: 격리는 칸이 터져도 주방 전체로 안 퍼지게 함. 오른쪽 주황: 권한은 처음부터 얼마나 줄지 정하는 것으로 다음 페이지로 이어짐", "Left, green: isolation keeps a broken slot from spreading through the kitchen. Right, orange: permission decides how much to grant up front, leading to the next page"),
         "caption": ("격리는 터진 걸 가두고, 권한은 처음부터 얼마를 줄지 정해요.", "Isolation contains a break; permission decides how much to grant in the first place."),
         "small": ('보안 마을의 <a href="sandbox-ko.html">샌드박스</a>는 격리 자체를 다루는 일반 개념이고, 이건 <a href="toolcall-ko.html">도구 호출</a>을 격리하는 전용 버전이에요. 각 칸에 얼마만큼 허락할지는 <a href="toolpermission-ko.html">도구별 권한 배지</a>에서.',
                   'A <a href="sandbox-en.html">sandbox</a> in the security world is the general concept of isolation; this is the version built specifically for isolating a <a href="toolcall-en.html">tool call</a>. How much each slot is allowed to do is the next page — a <a href="toolpermission-en.html">permission badge per tool</a>.')},
    ],
    "summary": (("<b>도구 샌드박스</b> = 견습생이 도구를 <b>서랍 한 칸씩만</b> 꺼내 쓰게 하고, 다 쓰면 <b>다시 잠그는</b> 것. 한 칸이 터져도 피해가 다른 칸으로 번지지 않아요.",
                 "<b>Tool sandbox</b> = letting the apprentice use a tool <b>one drawer slot at a time</b>, and <b>locking it again</b> afterward. If one slot breaks, the damage doesn't spread to the others."),
                ("Tool Sandbox. LLM 에이전트가 함수 호출(도구)을 실행할 때, 그 실행을 격리된 환경(프로세스, 컨테이너, 전용 런타임)에 가두는 보안 장치예요. 파일시스템·네트워크·시스템 자원 접근을 제한해서, 도구 하나가 오작동하거나 악용돼도 피해 범위를 그 샌드박스 안으로 한정해요. 일반 샌드박스 개념을 도구 호출이라는 구체적 실행 지점에 적용한 버전이에요.",
                 "A security mechanism that confines an LLM agent's function-call (tool) execution to an isolated environment — a process, container, or dedicated runtime. It restricts access to the filesystem, network, and system resources, so that even if one tool misbehaves or is abused, the damage stays inside that sandbox. It's the general sandboxing concept applied to the specific execution point of a tool call.")),
    "glossary": [
        ("도구 샌드박스", "Tool Sandbox", ("한 번에 한 칸씩만 열리는 서랍.", "A drawer that opens one slot at a time."), ("사고가 나도 그 칸 안에서만 터져요.", "Even an accident stays inside that one slot.")),
        ("샌드박스", "Sandbox", ("격리를 다루는 보안 마을의 일반 개념.", "The general isolation concept from the security world."), ('이건 도구 호출 전용 버전이에요. → <a href="sandbox-ko.html">샌드박스가 뭐예요?</a>', 'This page is the version built for a tool call. → <a href="sandbox-en.html">What is a Sandbox?</a>')),
        ("도구 호출", "Tool Calling", ("견습생이 도구를 꺼내 쓰는 일.", "The apprentice taking a tool out to use it."), ('무엇을 격리하는지가 바로 이거예요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', "This is exactly what gets isolated. → <a href=\"toolcall-en.html\">What is Tool Calling?</a>")),
        ("도구별 권한", "Per-tool Permission", ("칸마다 다른 배지.", "A different badge for each slot."), ('격리와 짝을 이루는 다음 페이지예요. → <a href="toolpermission-ko.html">도구별 권한 배지가 뭐예요?</a>', "The paired next page. → <a href=\"toolpermission-en.html\">What is a Per-tool Permission Badge?</a>")),
        ("최소 권한", "Least Privilege", ("처음부터 꼭 필요한 만큼만.", "Only what's needed, from the start."), ("격리와 함께 쓰면 더 든든해요.", "Pairs well with isolation for extra safety.")),
        ("에이전트", "Agent", ("심부름꾼 견습생.", "The apprentice running errands."), ("혼자 다니며 스스로 다음 할 일을 정해요.", "It runs alone and decides its own next step.")),
        ("공급망 공격", "Supply Chain Attack", ("재료창고에 미리 들어온 수상한 재료.", "Tainted ingredients already sitting in the pantry."), ("서랍 안 도구 자체가 처음부터 망가져 있을 수도 있어요.", "Even a tool inside the drawer can already be broken from the start.")),
        ("비상벨", "Incident Response", ("사고가 터졌을 때 누르는 벨.", "The bell you ring once an accident happens."), ("격리는 벨이 울릴 일 자체를 줄여줘요.", "Isolation cuts down how often that bell has to ring.")),
    ],
}
