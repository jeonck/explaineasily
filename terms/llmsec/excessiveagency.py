from _draw import *
from _world import *

LOCK2_I = icon('<rect x="16" y="26" width="32" height="26" rx="4" fill="var(--accent)"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" fill="none" stroke="var(--accent)" stroke-width="5"/>')
APPROVE_I = icon('<circle cx="32" cy="22" r="13" fill="var(--muted)"/><rect x="14" y="38" width="36" height="18" rx="8" fill="var(--muted)"/><path d="M44 42 l4 4 l8 -9" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
LOG_I = icon('<rect x="10" y="10" width="44" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M18 22 h28 M18 32 h28 M18 42 h20" stroke="#142033" stroke-width="2.5"/>')
KNIFE_I = icon('<rect x="24" y="8" width="16" height="30" rx="4" fill="#E9B44C"/><rect x="18" y="40" width="28" height="16" rx="3" fill="var(--bad)"/>')

# 1. 견습생에게 서랍을 통째로 열어줘요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.75, face=SMILE, **MANAGER)
         + bubble(60, 60, 220, 50, "⟦이제부터 뭐든 알아서 꺼내 써|from now on, take out whatever you need⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + knifedrawer(320, 220, 0.85, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧"))
         + person(610, 190, s=0.7, face=SMILE, **RUNNER)
         + label(610, 270, "⟦승인 없이도 다 꺼낼 수 있어요|everything is available, no approval needed⟧", 12, "var(--muted)")
         + label(380, 300, "⟦심부름마다 하나씩 허락받던 걸, 통째로 열어줬어요|instead of approving each errand, the whole drawer got opened at once⟧", 13, "var(--ink)", cls="d"))

# 2. 권한이 넓을수록, 속았을 때 할 수 있는 일도 많아져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(170, 150, s=0.75, face=EYES, **RUNNER)
         + ticket(330, 170, 0.8, sneaky=True)
         + bubble(255, 50, 250, 55, "⟦쪽지가 '전화해서 결제해'라니, 전화 도구를 꺼낼게요|the note says call and pay — I will grab the phone tool⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + knifedrawer(500, 230, 0.65, locked=False, labels=("⟦전화|phone⟧", "⟦칼|knife⟧"))
         + label(380, 280, "⟦권한이 넓을수록, 속았을 때 할 수 있는 일도 많아져요|the broader the access, the more a trick can do⟧", 12, "var(--ink)"))

# 3. 과잉 에이전시 = 필요 이상으로 넓은 권한·자동 승인을 준 상태 (hero)
P3 = svg(360, sky(360)
         + knifedrawer(40, 240, 0.9, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧", "⟦열쇠|key⟧"))
         + person(320, 150, s=0.8, face=SMILE, **RUNNER)
         + person(480, 190, s=0.6, face=EYES, **MANAGER)
         + label(480, 275, "⟦승인 없이 지나가요|it passes with no approval⟧", 11, "var(--muted)")
         + person(650, 220, s=0.55, face=EYES, **INSPECTOR) + badge(690, 190, 0.6)
         + label(380, 30, "⟦과잉 에이전시 = 필요 이상으로 넓은 권한·자동 승인을 준 상태|Excessive Agency = far more access or auto-approval than is needed⟧", 13, "var(--ink)", cls="d")
         + label(380, 345, "⟦못 쓰게 막아둔 도구가 거의 없어요|almost nothing is locked out of reach⟧", 12, "var(--muted)"))

# 4. 적절한 권한 vs 과잉 에이전시 (작동 디테일)
P4 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + knifedrawer(40, 200, 0.75, locked=True, labels=("⟦칼|knife⟧", "⟦전화|phone⟧"))
         + person(230, 150, s=0.6, face=SMILE, **RUNNER)
         + label(190, 290, "⟦필요한 도구만, 승인받고 꺼내요|only needed tools, taken with approval⟧", 11, "var(--ink)")
         + knifedrawer(420, 200, 0.75, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧", "⟦열쇠|key⟧"))
         + person(650, 150, s=0.6, face=SMILE, **RUNNER)
         + label(570, 290, "⟦뭐든, 승인 없이 꺼내요|anything, taken with no approval⟧", 11, "var(--bad)")
         + label(380, 315, "⟦도구 목록이 길어질수록, 지켜봐야 할 곳도 늘어나요|the longer the tool list, the more there is to watch⟧", 12, "var(--ink)", cls="d"))

# 5. 설계는 따로 있고, 과잉 에이전시는 그 설계를 넘어선 상태예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + knifedrawer(40, 170, 0.7, locked=True, labels=("⟦칼|knife⟧", "⟦전화|phone⟧"))
         + label(130, 260, "⟦도구마다 권한을 정하는 설계는 꼭 필요해요|designing permission per tool is essential⟧", 11, "var(--muted)")
         + knifedrawer(430, 170, 0.7, locked=False, labels=("⟦칼|knife⟧", "⟦불|flame⟧", "⟦전화|phone⟧"))
         + label(560, 260, "⟦그 설계를 안 지키고 다 열어준 상태예요|skipping that design and opening everything is this state⟧", 11, "var(--bad)")
         + label(380, 285, "⟦에이전트도 몰래 낀 쪽지를 글자만 보고는 구분 못 해요 — 넓은 권한은 그 쪽지에게도 넓은 힘을 줘버려요|an agent cannot tell a smuggled note from a real one by reading alone — broad access hands broad power to that note too⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "excessiveagency", "order": 17,
    "title": ("너무 많은 열쇠를 받은 견습생", "The Apprentice With Too Many Keys"),
    "h1": ("<em>과잉 에이전시</em>가 뭐예요?", "What is <em>Excessive Agency</em>?"),
    "sub": ("과잉 에이전시를, 견습생에게 칼서랍을 통째로 열어주고 승인 없이도 뭐든 꺼내 쓰게 한 이야기로 풀어봤어요.",
            "Excessive agency, told as a story about handing the apprentice the whole knife drawer and letting it take out anything with no approval at all."),
    "panels": [
        {"svg": P1, "alt": ("사장님이 견습생에게 칼서랍을 통째로 열어주며 뭐든 알아서 꺼내 쓰라고 함", "The manager opens the whole knife drawer for the apprentice and says to take out whatever is needed"),
         "caption": ("견습생에게 서랍을 통째로 열어줬어요.", "The apprentice got the whole drawer opened for it."),
         "small": ("심부름마다 하나씩 허락받던 걸, 한 번에 넘겨버렸어요.", "What used to be approved errand by errand got handed over all at once.")},
        {"svg": P2, "hero": False, "alt": ("몰래 낀 쪽지를 받은 견습생이 전화 도구를 넓은 권한으로 그대로 꺼내 씀", "The apprentice, fooled by a smuggled note, freely grabs the phone tool thanks to its broad access"),
         "caption": ("권한이 넓을수록, 속았을 때 할 수 있는 일도 많아져요.", "The broader the access, the more a trick can do."),
         "small": ("견습생도 몰래 낀 쪽지와 진짜 부탁을 구분하지 못해요.", "The apprentice cannot tell a smuggled note from a real request either.")},
        {"svg": P3, "hero": True, "alt": ("활짝 열린 칼서랍, 견습생, 승인 없이 지나가는 사장님, 지켜보는 검사관이 한 장면에 있음", "A wide-open knife drawer, the apprentice, a manager letting things pass with no approval, and an inspector watching"),
         "caption": ("과잉 에이전시는 필요 이상으로 넓은 권한을 준 상태예요.", "Excessive agency means giving far more access than the job needs."),
         "small": ("못 쓰게 막아둔 도구가 거의 없어요.", "Almost nothing is locked out of reach."),
         "tricks": (4, [
             (LOCK2_I, ("꼭 필요한 도구만 꺼내기", "Grant only what's needed"), ("서랍은 기본적으로 잠겨 있어요", "the drawer stays locked by default"), "calm"),
             (APPROVE_I, ("중요한 일은 한 번 더 확인받기", "Get a second approval on big steps"), ("사람이 한 번 더 들여다봐요", "a person takes one more look")),
             (LOG_I, ("심부름마다 기록 남기기", "Log every errand"), ("무엇을 꺼냈는지 나중에도 알 수 있어요", "it stays clear what was taken out, after the fact"), "warm"),
             (KNIFE_I, ("위험한 도구는 따로 잠그기", "Lock the dangerous tools separately"), ("전화·결제 같은 도구는 더 조심해요", "tools like calling or paying get extra care")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 서랍이 잠겨 있고 필요한 도구만 승인받아 꺼냄. 오른쪽: 서랍이 활짝 열려 있고 뭐든 승인 없이 꺼냄", "Left: the drawer stays locked and only approved tools come out. Right: the drawer is wide open and anything comes out with no approval"),
         "caption": ("적절한 권한과 과잉 에이전시는 이렇게 달라요.", "This is the difference between proper access and excessive agency."),
         "small": ("도구 목록이 길어질수록, 지켜봐야 할 곳도 늘어나요.", "The longer the tool list, the more there is to watch.")},
        {"svg": P5, "alt": ("왼쪽: 도구마다 권한을 정해 서랍이 잠겨 있음. 오른쪽: 그 설계를 넘어서 서랍이 열려 있음", "Left: permission is designed per tool and the drawer stays locked. Right: that design is skipped and the drawer is open"),
         "caption": ("권한 설계는 따로 있고, 과잉 에이전시는 그걸 넘어선 상태예요.", "Permission design is one thing; excessive agency is going past it."),
         "small": ("넓은 권한은 몰래 낀 쪽지에게도 넓은 힘을 줘버려요.", "Broad access hands broad power to a smuggled note too.")},
    ],
    "summary": (("<b>과잉 에이전시</b> = 견습생에게 필요한 것보다 훨씬 넓은 <b>권한</b>과 <b>자동 승인</b>을 줘버린 상태.",
                 "<b>Excessive Agency</b> = giving the apprentice far more <b>access</b> and <b>automatic approval</b> than the job needs."),
                ("과잉 에이전시(Excessive Agency)는 AI 에이전트가 수행하는 작업 범위를 넘어서는 권한, 도구 접근, 또는 승인 절차를 가진 상태를 말해요. 에이전트는 몰래 낀 지시와 진짜 지시를 글자만 보고 구분하지 못하기 때문에, 권한이 넓을수록 속았을 때 입는 피해도 커져요.",
                 "Excessive agency describes an AI agent holding more permissions, tool access, or approval authority than its task actually requires. Because an agent cannot tell a smuggled instruction from a genuine one just by reading it, the wider its access, the greater the damage when it is fooled.")),
    "glossary": [
        ("과잉 에이전시", "Excessive Agency", ("견습생에게 필요 이상으로 넓은 권한을 준 상태.", "Giving the apprentice far more access than the job needs."), ('이 세계관 전체 소개도 있어요. → <a href="llmthreats-ko.html">다 받아주는 주방</a>', 'There is also an intro to this whole world. → <a href="llmthreats-en.html">The Kitchen That Takes Any Order</a>')),
        ("에이전트", "Agent", ("목표를 받으면 심부름 목록을 스스로 짜는 견습생.", "The apprentice that plans its own errands once given a goal."), ('이 과잉 상태가 생기는 바로 그 대상이에요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'This is exactly who ends up with too much access. → <a href="agent-en.html">The Parrot That Plans Its Own Errands</a>')),
        ("도구 호출", "Tool Calling", ("칼서랍에서 도구를 꺼내 쓰는 일.", "Taking a tool out of the knife drawer to use it."), ('AI 세계의 기본 개념이에요. → <a href="toolcall-ko.html">도구 상자</a>', 'The underlying AI concept. → <a href="toolcall-en.html">The Toolbox</a>')),
        ("도구별 권한", "Per-tool Permission", ("서랍 칸마다 다른 배지를 다는 권한 설계.", "Designing a different badge for each drawer slot."), ('이 설계를 넘어선 상태가 과잉 에이전시예요. → <a href="toolpermission-ko.html">도구별 권한 배지</a>', 'Excessive agency is going past this design. → <a href="toolpermission-en.html">A Permission Badge Per Tool</a>')),
        ("최소 권한", "Least Privilege", ("딱 필요한 만큼만 권한을 주는 것.", "Granting only the access that is actually needed."), ('과잉 에이전시는 이 원칙을 지키지 않은 상태예요. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>', 'Excessive agency is exactly this principle left unobserved. → <a href="leastprivilege-en.html">Only the Keys You Need</a>')),
        ("샌드박스", "Sandbox", ("수상한 상자를 먼저 열어보는 빈 방.", "An empty room where a suspicious box gets opened first."), ('도구를 쓸 공간 자체를 가두는 방법이에요. → <a href="sandbox-ko.html">창문 없는 빈 방</a>', 'A way to contain the space a tool runs in. → <a href="sandbox-en.html">The Empty Room with No Windows</a>')),
        ("휴먼 인 더 루프", "Human-in-the-Loop", ("마지막엔 사람이 도장을 찍는 것.", "A person stamping approval at the very end."), ('중요한 심부름엔 이 확인이 필요해요. → <a href="humanloop-ko.html">마지막은 사람이</a>', 'An important errand needs this check. → <a href="humanloop-en.html">A Person at the End</a>')),
        ("관측 가능성", "Observability", ("계기판·일지·지나간 길, 세 가지로 들여다보기.", "Looking in three ways — dashboards, logs, and the path a request took."), ('심부름 기록을 남기는 일이 여기 속해요. → <a href="observability-ko.html">세 가지로 들여다보기</a>', 'Logging every errand belongs here. → <a href="observability-en.html">Looking In Three Different Ways</a>')),
    ],
}
