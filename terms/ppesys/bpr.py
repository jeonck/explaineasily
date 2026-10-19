from _draw import *
from _world import *


def paper(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-18" width="28" height="36" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M-8 -8 h16 M-8 0 h16 M-8 8 h10" stroke="#142033" stroke-width="1.5"/></g>'


def flow_chain(x, y, n, broken=True, s=1.0):
    """낡은 공정: 끊어진 접수 → 대기 → 재진단 → 재작성 단계."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    gap = 0 if not broken else 26
    step = 90 + gap
    for i in range(n):
        xx = i * step
        out += f'<rect x="{xx}" y="-16" width="70" height="32" rx="5" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
        if i < n - 1:
            if broken:
                out += f'<path d="M{xx + 70} 0 h{gap}" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>'
            else:
                out += f'<path d="M{xx + 70} 0 h20" stroke="var(--good)" stroke-width="3"/>'
    return out + '</g>'


# 1. 접수부터 출고까지 단계가 너무 많고 끊겨 있어요
P1 = svg(300, sky(300)
         + flow_chain(60, 150, 4, broken=True)
         + label(60, 110, "⟦접수|intake⟧", 11, "var(--muted)") + label(150, 110, "⟦대기|wait⟧", 11, "var(--muted)")
         + label(240, 110, "⟦재진단|re-diagnose⟧", 11, "var(--muted)") + label(330, 110, "⟦재작성|re-write⟧", 11, "var(--muted)")
         + person(650, 170, s=0.8, face=SWEAT, **CHIEF)
         + label(380, 40, "⟦차 한 대 고치는데 단계가 너무 많고 자꾸 끊겨요|fixing one car takes too many steps, each one stalling⟧", 13, "var(--ink)")
         + label(380, 270, "⟦옛날 방식을 그대로 두고 조금씩 손봐선 한계가 있어요|tweaking the old way bit by bit only goes so far⟧", 12, "var(--muted)"))

# 2. 단계를 하나씩 빨리해도 전체는 안 빨라져요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + paper(160, 150) + paper(260, 150) + paper(360, 150) + paper(460, 150) + paper(560, 150)
         + label(380, 90, "⟦접수서, 진단서, 견적서, 작업지시서, 출고서 — 서류가 다섯 장|intake form, diagnosis sheet, quote, work order, pickup slip — five separate papers⟧", 12, "var(--bad)", cls="d")
         + person(660, 150, s=0.7, face=FROWN, **MECH1)
         + label(380, 220, "⟦한 단계를 빨리해도 서류를 다시 쓰느라 다시 느려져요|speed up one step, and rewriting the paperwork slows it right back down⟧", 13, "var(--ink)")
         + label(380, 270, "⟦공정 전체를 처음부터 다시 그려야 할 때가 있어요|sometimes the whole process needs redrawing from scratch⟧", 12, "var(--muted)"))

# 3. BPR = 기존 공정을 조금 고치지 않고 처음부터 다시 설계하는 것 (hero)
P3 = svg(340, sky(340)
         + flow_chain(100, 180, 2, broken=False)
         + label(130, 130, "⟦접수+진단 통합|intake + diagnosis, merged⟧", 11, "var(--muted)") + label(290, 130, "⟦작업·출고|work + pickup⟧", 11, "var(--muted)")
         + person(500, 150, s=0.9, face=SMILE, **CHIEF)
         + label(380, 30, "⟦BPR = 기존 단계를 조금 고치지 않고, 공정을 처음부터 다시 설계하는 것|BPR redesigns the process from scratch, not just tweaking old steps⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦서류 다섯 장을 한 장의 디지털 전표로 합쳐버렸어요|five papers became a single digital slip⟧", 12, "var(--muted)"))

RETHINK_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M20 20 L44 44 M44 20 L20 44" stroke="var(--bad)" stroke-width="3"/>')
MERGE_I = icon('<rect x="8" y="22" width="20" height="20" rx="3" fill="var(--line)"/><rect x="36" y="22" width="20" height="20" rx="3" fill="var(--line)"/><path d="M20 22 L44 42 M44 22 L20 42" stroke="var(--good)" stroke-width="3"/>')
DIGITAL_I = icon('<rect x="14" y="12" width="36" height="40" rx="4" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M22 24 h20 M22 32 h20" stroke="var(--good)" stroke-width="3"/>')
JUMP_I = icon('<path d="M10 48 q22 -44 44 0" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M48 36 l6 12 l-13 -3z" fill="var(--accent)"/>')

# 4. 기존 개선 vs BPR 비교
P4 = svg(320, sky(320)
         + queueboard(60, 40, 320, 240, "⟦조금씩 고치기(카이젠)|incremental tweaks (kaizen)⟧",
                      ("⟦기존 단계는 그대로 두고|keep existing steps as-is⟧",
                       "⟦한 단계씩 조금 빨리하기|speed up one step at a time⟧",
                       "⟦개선 폭이 작아요|the gains are small⟧"), 1.0)
         + queueboard(410, 40, 300, 240, "⟦BPR — 처음부터 재설계|BPR — redesign from zero⟧",
                      ("⟦단계 자체를 통째로 재구성|rebuild the steps themselves⟧",
                       "⟦여러 단계를 합치거나 없애기|merge or eliminate whole steps⟧",
                       "⟦개선 폭이 크지만 위험도 커요|big gains, but bigger risk too⟧"), 1.0, hl=1))

# 5. 다시 설계해도 사람·시스템이 안 따라오면 소용없어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + flow_chain(80, 150, 2, broken=False, s=0.9)
         + label(190, 220, "⟦공정도는 깔끔하게 다시 그렸어요|the process diagram is redrawn, clean⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **MECH2)
         + label(570, 240, "⟦정비사가 새 방식에 익숙하지 않으면 소용없어요|but it's no use if mechanics aren't used to the new way⟧", 11, "var(--ink)")
         + label(380, 282, "⟦공정 재설계는 사람·교육·시스템이 같이 바뀌어야 해요|redesigning the process needs people, training, and systems to change together⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "bpr", "order": 15,
    "title": ("정비 공정을 처음부터 다시 그리는 일", "Redrawing the Repair Process from Scratch"),
    "h1": ("<em>BPR(업무 프로세스 재설계)</em>이 뭐예요?", "What is <em>BPR (Business Process Reengineering)</em>?"),
    "sub": ("BPR을, 끊기고 복잡해진 정비공장 공정을 조금씩 고치는 대신 처음부터 다시 그리는 이야기로 풀어봤어요.",
            "BPR, told as a story about redrawing a broken, overcomplicated repair process from scratch instead of tweaking it piece by piece."),
    "panels": [
        {"svg": P1, "alt": ("접수부터 출고까지 끊긴 네 단계 공정을 보며 정비반장이 진땀을 흘림", "The chief sweats over a four-step process from intake to pickup that keeps stalling"),
         "caption": ("단계가 너무 많고 자꾸 끊겨요.", "There are too many steps, each one stalling."),
         "small": ("옛날 방식을 그대로 두고 조금씩 손봐선 한계가 있어요.", "Tweaking the old way bit by bit only goes so far.")},
        {"svg": P2, "alt": ("서류 다섯 장이 늘어서 있고 정비사가 한 단계를 빨리해도 전체가 느려짐에 좌절함", "Five separate papers lined up; the mechanic is frustrated that speeding up one step doesn't help"),
         "caption": ("한 단계를 빨리해도 전체는 안 빨라져요.", "Speeding up one step doesn't speed up the whole."),
         "small": ("공정 전체를 처음부터 다시 그려야 할 때가 있어요.", "Sometimes the whole process needs redrawing from scratch.")},
        {"svg": P3, "hero": True, "alt": ("접수와 진단을 하나로 합친 두 단계짜리 새 공정도 앞에서 정비반장이 만족함", "The chief is pleased in front of a new two-step process that merges intake and diagnosis"),
         "caption": ("BPR은 공정을 처음부터 다시 설계하는 것이에요.", "BPR redesigns the process from scratch."),
         "small": ("서류 다섯 장을 한 장의 디지털 전표로 합쳐버렸어요.", "Five papers became a single digital slip."),
         "tricks": (4, [
             (RETHINK_I, ("근본적으로 다시 묻기", "Rethink fundamentally"), ("왜 이 단계가 필요한지부터 물어요", "asks why the step exists at all"), "warm"),
             (MERGE_I, ("단계 통합", "Merge steps"), ("여러 단계를 하나로 합쳐요", "combines several steps into one")),
             (DIGITAL_I, ("종이 없애기", "Cut the paperwork"), ("서류를 디지털 전표로 바꿔요", "turns paper forms into a digital slip")),
             (JUMP_I, ("단계적 아닌 도약", "A leap, not a step"), ("조금씩이 아니라 크게 바꿔요", "a big change, not a small tweak"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 조금씩 고치는 카이젠 방식(작은 개선). 오른쪽: BPR은 공정 자체를 재구성(큰 개선, 큰 위험)", "Left: kaizen's small tweaks. Right: BPR rebuilds the process itself — big gains, big risk"),
         "caption": ("조금씩 고치기와 BPR은 접근이 달라요.", "Incremental tweaks and BPR take different approaches."),
         "small": ("BPR은 개선 폭이 크지만 위험도 더 커요.", "BPR offers bigger gains, but carries bigger risk too.")},
        {"svg": P5, "alt": ("왼쪽: 공정도는 깔끔하게 재설계됨. 오른쪽: 정비사가 새 방식에 적응하지 못하면 소용없음", "Left: the process diagram is cleanly redesigned. Right: it's useless if mechanics can't adapt"),
         "caption": ("다시 설계해도 사람이 못 따라오면 소용없어요.", "A redesign is useless if people can't keep up with it."),
         "small": ("공정 재설계는 사람·교육·시스템이 같이 바뀌어야 해요.", "Redesigning the process needs people, training, and systems to change together.")},
    ],
    "summary": (("<b>BPR</b>은 기존 공정을 <b>조금씩 고치는 대신</b>, 비용·품질·속도를 크게 끌어올리도록 <b>처음부터 다시 설계</b>하는 것이에요.",
                 "<b>BPR</b> <b>redesigns a process from scratch</b> — instead of tweaking the old one bit by bit — to dramatically improve cost, quality, and speed."),
                ("BPR(Business Process Reengineering, 업무 프로세스 재설계)은 기존 업무 절차를 근본적으로 다시 생각하고 급진적으로 재설계해 성과를 획기적으로 개선하는 경영 기법이에요. 점진적 개선(카이젠)과 달리 '왜 이 단계가 필요한가'부터 되물어 단계를 통합·제거하고, 정보기술을 활용해 공정 자체를 재구성해요. 다만 조직·인력의 변화 관리가 함께 가지 않으면 실패하기 쉬워요.",
                 "BPR (Business Process Reengineering) fundamentally rethinks and radically redesigns existing business processes to achieve dramatic performance improvements. Unlike incremental improvement (kaizen), it asks 'why does this step exist at all,' merging or eliminating steps and restructuring the process itself using information technology. Without accompanying change management for people and the organization, it tends to fail.")),
    "glossary": [
        ("BPR", "Business Process Reengineering", ("공정을 처음부터 다시 그리는 것.", "Redrawing the process from scratch."), ("근본적·급진적 재설계가 핵심이에요.", "Fundamental, radical redesign is the core idea.")),
        ("카이젠(점진적 개선)", "Kaizen (Incremental Improvement)", ("기존 단계를 조금씩 빨리하는 것.", "Speeding up existing steps a little at a time."), ("BPR과 달리 큰 틀은 그대로 둬요.", "Unlike BPR, the overall structure stays the same.")),
        ("프로세스 혁신", "Process Innovation", ("BPR을 가리키는 다른 이름.", "Another name for BPR."), ("정보기술 활용이 자주 함께 와요.", "Often paired with the use of information technology.")),
        ("단계 통합", "Step Consolidation", ("여러 단계를 하나로 합치는 것.", "Merging several steps into one."), ("접수+진단 통합이 그 예예요.", "Merging intake and diagnosis is one example.")),
        ("변화 관리", "Change Management", ("새 방식에 사람이 적응하도록 돕는 것.", "Helping people adapt to the new way."), ("이게 없으면 재설계가 실패해요.", "Without it, the redesign tends to fail.")),
        ("정보기술 지렛대", "IT as a Lever", ("디지털 전표처럼 기술로 단계를 줄이는 것.", "Using technology, like a digital slip, to cut steps."), ("BPR을 가능하게 하는 수단이에요.", "A key enabler of BPR.")),
        ("업무 재설계 위험", "Reengineering Risk", ("크게 바꾸는 만큼 실패 위험도 큼.", "Big change carries big failure risk too."), ("성공률이 낮다는 비판도 있어요.", "Often criticized for a low success rate.")),
        ("BPM(업무 프로세스 관리)", "BPM (Business Process Management)", ("재설계 이후 공정을 꾸준히 관리하는 것.", "Ongoing management of the process after redesign."), ("BPR은 한 번의 재설계, BPM은 지속 관리예요.", "BPR is a one-time redesign; BPM is continuous management.")),
    ],
}
