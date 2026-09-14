import math

from _draw import *
from _world import *


def toolbox(x, y, s=1.0, text=None):
    """공방 도구 상자: 나무 상자에 계산기·달력·전화. 중심 x, 상자 앞면 y-20..y+30, 도구 머리 y-46. 폭 130. text 는 y+50."""
    t = label(0, 50, text, 11, "var(--muted)") if text else ""
    calc = ('<rect x="-52" y="-46" width="30" height="40" rx="4" fill="#4A5A72"/><rect x="-47" y="-41" width="20" height="9" rx="2" fill="#C9D5E6"/>'
            + "".join(f'<circle cx="{-46 + i * 8}" cy="{-24 + j * 8}" r="2.5" fill="#C9D5E6"/>' for i in range(3) for j in range(2)))
    cal = ('<rect x="-15" y="-46" width="32" height="40" rx="4" fill="#FFF8E7" stroke="#B5382C" stroke-width="2"/><rect x="-15" y="-46" width="32" height="10" rx="4" fill="#B5382C"/>'
           + "".join(f'<rect x="{-10 + i * 8}" y="{-30 + j * 8}" width="5" height="5" fill="#142033"/>' for i in range(3) for j in range(2)))
    phone = '<rect x="26" y="-46" width="24" height="40" rx="5" fill="#142033"/><rect x="29" y="-41" width="18" height="26" rx="2" fill="#5B9BD5"/><circle cx="38" cy="-10" r="2" fill="#C9D5E6"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-65" y="-30" width="130" height="60" rx="6" fill="#5A3B22"/>'
            f'{calc}{cal}{phone}<rect x="-65" y="-20" width="130" height="50" rx="6" fill="{WOOD}"/><rect x="-65" y="-20" width="130" height="8" fill="#5A3B22"/>{t}</g>')


def arrow(x1, y1, x2, y2, color="var(--muted)", dash=True):
    d = ' stroke-dasharray="6 5"' if dash else ""
    deg = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"{d}/>'
            f'<path d="M0 0 l-10 -6 l0 12z" transform="translate({x2},{y2}) rotate({deg:.0f})" fill="{color}"/>')


def node(x, y, text):
    return (f'<rect x="{x - 40}" y="{y - 15}" width="80" height="30" rx="8" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/>'
            + label(x, y + 4, text, 12, "var(--ink)", cls="d"))


# 1. 다음 주 출장 준비해 줘 — 한 번 답으로 끝나지 않는 일
P1 = svg(300, sky(300)
         + person(60, 120, s=0.9, face=EYES, **GUEST) + bubble(30, 30, 250, 44, "⟦다음 주 출장 준비해 줘|get my trip next week ready⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + perch(330, 200, 140) + parrot(330, 160, 1.1, mood="sweat")
         + note(470, 40, 250, 130, "⟦해야 할 일|TO DO⟧", ("⟦비행기표 찾기|find a flight⟧", "⟦호텔 잡기|book a hotel⟧", "⟦회의 시간 맞추기|fit the meetings⟧", "⟦날씨 보고 짐 싸기|check weather, pack⟧"), 1.0)
         + label(595, 200, "⟦걸음이 여러 개예요|it takes many steps⟧", 12, "var(--muted)")
         + label(380, 282, "⟦한 번 답하고 끝나는 일이 아니에요|this is not a one-answer job⟧", 13, "var(--ink)"))

# 2. 한 번 묻고 한 번 답하는 앵무새는 여러 걸음 일을 못 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(130, 150, 1.0, talk=True) + bubble_parrot(30, 40, 260, 44, "⟦비행기표는 항공사에서 사세요|buy the ticket from the airline⟧", 11)
         + label(170, 240, "⟦한 번 말하고 끝 — 찾지도 사지도 않아요|says it once and stops — finds nothing, buys nothing⟧", 11, "var(--bad)")
         + note(400, 40, 200, 130, "⟦해야 할 일|TO DO⟧", ("⟦비행기표  ×|flight  ×⟧", "⟦호텔  ×|hotel  ×⟧", "⟦회의 시간  ×|meetings  ×⟧", "⟦날씨·짐  ×|weather, bag  ×⟧"), 1.0)
         + label(500, 200, "⟦하나도 안 됐어요|nothing got done⟧", 12, "var(--bad)")
         + person(640, 110, s=0.9, face=FROWN, **GUEST)
         + label(380, 282, "⟦한 번 묻고 한 번 답하는 앵무새는 여러 걸음이 필요한 일을 못 해요|a one-question, one-answer parrot can\'t do a many-step job⟧", 12, "var(--bad)"))

# 3. 에이전트 = 스스로 심부름 목록을 짜고, 도구를 쓰고, 결과를 보고 다음 걸음을 정하는 앵무새 (hero)
P3 = svg(360, sky(360)
         + note(30, 40, 190, 150, "⟦심부름 목록 (스스로 씀)|ERRANDS (its own)⟧", ("⟦✓ 비행기표 찾기|✓ find a flight⟧", "⟦✓ 호텔 잡기|✓ book a hotel⟧", "⟦지금: 회의 시간 맞추기|now: fit the meetings⟧", "⟦다음: 짐 목록|next: packing list⟧"), 1.0, 2)
         + label(125, 212, "⟦결과를 보고 다음 걸음을 정해요|it picks the next step from the result⟧", 11, "var(--muted)")
         + perch(360, 250, 150) + parrot(360, 210, 1.3, talk=True)
         + bubble_parrot(260, 70, 210, 44, "⟦다음은 달력 도구!|next: the calendar tool!⟧", 12)
         + arrow(400, 200, 488, 200)
         + toolbox(560, 200, 1.0, "⟦도구 상자|toolbox⟧")
         + person(660, 100, s=0.8, face=SMILE, **TRAINER) + label(688, 215, "⟦조련사 (실행)|trainer (runs it)⟧", 10, "var(--muted)")
         + label(560, 290, "⟦돌아온 결과를 목록에 ✓|the result comes back, ✓ on the list⟧", 11, "var(--muted)")
         + label(380, 340, "⟦에이전트 = 목표를 받으면 심부름 목록을 스스로 짜고 도구를 쓰는 앵무새|an agent is a parrot that, given a goal, plans its own errands and uses tools⟧", 13, "var(--ink)", cls="d"))

# 4. 루프: 생각 → 도구 → 결과 → 다시 생각 … → 끝
_CX, _CY, _R = 250, 150, 90
_heads = "".join(f'<path d="M0 0 l-10 -6 l0 12z" transform="translate({_CX + _R * math.sin(math.radians(a)):.1f},{_CY - _R * math.cos(math.radians(a)):.1f}) rotate({a})" fill="var(--accent)"/>' for a in (45, 135, 225, 315))
P4 = svg(320, sky(320)
         + f'<circle cx="{_CX}" cy="{_CY}" r="{_R}" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 6"/>' + _heads
         + node(250, 60, "⟦생각|think⟧") + node(340, 150, "⟦도구|tool⟧") + node(250, 240, "⟦결과|result⟧") + node(160, 150, "⟦보고 고침|adjust⟧")
         + parrot(250, 150, 0.8, mood="think")
         + arrow(295, 60, 400, 60, "var(--good)", False) + label(440, 65, "⟦끝 ✓|done ✓⟧", 14, "var(--good)", cls="d")
         + label(440, 85, "⟦다 됐으면|when all is done⟧", 10, "var(--muted)")
         + note(520, 40, 200, 150, "⟦심부름 목록|ERRANDS⟧", ("⟦✓ 비행기표|✓ flight⟧", "⟦✓ 호텔|✓ hotel⟧", "⟦✓ 회의 시간|✓ meetings⟧", "⟦지금: 짐 목록|now: packing list⟧"), 1.0, 3)
         + label(620, 215, "⟦걸음마다 하나씩 ✓|one ✓ per step⟧", 11, "var(--muted)")
         + label(380, 300, "⟦생각, 도구, 결과, 다시 생각 — 다 되면 끝|think, tool, result, think again — done when it is all done⟧", 12, "var(--ink)"))

# 5. 걸음이 많을수록 틀릴 기회도 많아요 + 멈출 줄 모르면 콩만 먹어요 → 울타리
_steps = "".join(f'<circle cx="{40 + i * 34}" cy="90" r="11" fill="{"var(--bad)" if i == 6 else "var(--good)"}"/>' for i in range(10)) + label(244, 95, "⟦×|×⟧", 14, "#FFF8E7", cls="d")
_fence = "".join(f'<rect x="{420 + i * 36}" y="100" width="8" height="60" fill="{WOOD}"/>' for i in range(9)) + f'<rect x="420" y="112" width="296" height="6" fill="{WOOD}"/><rect x="420" y="140" width="296" height="6" fill="{WOOD}"/>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + label(190, 40, "⟦걸음이 많을수록 틀릴 기회도 많아요|more steps, more chances to slip⟧", 12, "var(--ink)", cls="d")
         + _steps + label(190, 130, "⟦한 걸음 90% 맞아도 열 걸음이면 약 35%|90% per step is about 35% over ten steps⟧", 11, "var(--bad)")
         + parrot(120, 210, 0.9, mood="sweat") + "".join(bean(x, y, 0.9) for x, y in ((220, 232), (252, 242), (284, 230), (316, 244), (348, 233)))
         + label(270, 200, "⟦멈출 줄 모르면 콩만 먹어요|if it never stops, it just eats beans⟧", 11, "var(--bad)")
         + label(570, 60, "⟦울타리: 걸음 수와 콩 예산에 한도|a fence: a cap on steps and beans⟧", 12, "var(--ink)", cls="d")
         + _fence + person(430, 170, s=0.8, face=SMILE, **TRAINER)
         + label(620, 205, "⟦위험한 걸음은 사람이 확인해요|a person checks the risky steps⟧", 11, "var(--ink)")
         + label(620, 235, "⟦순서가 늘 같으면 순서표가 더 싸요|fixed order? a checklist is cheaper⟧", 11, "var(--muted)")
         + label(380, 300, "⟦걸음 수와 콩 예산에 울타리를 치고, 마지막은 사람이 봐요|fence the step count and bean budget, and let a person see the end⟧", 12, "var(--ink)", cls="d"))

GOAL_I = icon('<rect x="16" y="8" width="4" height="48" fill="#5A3B22"/><path d="M20 10 h30 l-8 10 l8 10 h-30z" fill="var(--accent)"/>')
TOOLBOX_I = icon(f'<rect x="8" y="30" width="48" height="26" rx="4" fill="{WOOD}"/><rect x="8" y="30" width="48" height="6" fill="#5A3B22"/><rect x="14" y="14" width="12" height="18" rx="2" fill="#4A5A72"/><rect x="30" y="14" width="12" height="18" rx="2" fill="#FFF8E7" stroke="#B5382C" stroke-width="2"/><rect x="46" y="14" width="8" height="18" rx="2" fill="#142033"/>')
LOOP_I = icon('<path d="M32 12 a20 20 0 1 1 -18 11" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M8 18 l6 8 l8 -6z" fill="var(--accent)"/><circle cx="32" cy="32" r="5" fill="var(--good)"/>')
FENCE_I = icon(f'<rect x="10" y="20" width="6" height="34" fill="{WOOD}"/><rect x="29" y="20" width="6" height="34" fill="{WOOD}"/><rect x="48" y="20" width="6" height="34" fill="{WOOD}"/><rect x="8" y="28" width="48" height="5" fill="{WOOD}"/><rect x="8" y="42" width="48" height="5" fill="{WOOD}"/>')

PAGE = {
    "slug": "agent", "order": 16,
    "title": ("심부름 목록을 스스로 짜는 앵무새", "The Parrot That Plans Its Own Errands"),
    "h1": ("<em>에이전트</em>가 뭐예요?", "What is an <em>Agent</em>?"),
    "sub": ("AI 에이전트를 목표를 받으면 심부름 목록을 스스로 짜고, 도구 상자를 쓰고, 결과를 보고 다음 걸음을 정하는 앵무새 이야기로 풀어봤어요.",
            "AI agents, told as a story about a parrot that, given a goal, plans its own errands, uses the toolbox, and picks the next step from each result."),
    "panels": [
        {"svg": P1, "alt": ("손님이 다음 주 출장 준비를 부탁하고, 땀 흘리는 앵무새 옆에 해야 할 일 쪽지: 비행기표, 호텔, 회의 시간, 날씨와 짐", "A guest asks to get next week\'s trip ready; beside a sweating parrot, a to-do note: flight, hotel, meetings, weather and packing"),
         "caption": ("손님이 출장 준비를 부탁했어요. 한 번 답하고 끝나는 일이 아니에요.", "The guest asks to get a trip ready. This is not a one-answer job."),
         "small": ("비행기표를 찾고, 호텔을 잡고, 회의 시간을 맞추고, 날씨를 보고 짐을 싸요. 걸음이 여러 개고, 앞 걸음의 결과가 다음 걸음을 바꿔요.", "Find a flight, book a hotel, fit the meetings, check the weather and pack. Many steps — and each result changes the next step.")},
        {"svg": P2, "alt": ("앵무새가 비행기표는 항공사에서 사라고 한 번 말하고 끝. 해야 할 일 쪽지는 전부 ×, 손님은 찡그림", "The parrot says once to buy the ticket from the airline and stops; every to-do line is ×, the guest frowns"),
         "caption": ("한 번 묻고 한 번 답하는 앵무새는 여러 걸음이 필요한 일을 못 해요.", "A one-question, one-answer parrot can\'t do a many-step job."),
         "small": ('말은 그럴듯한데 찾지도 사지도 않아요. <a href="toolcall-ko.html">도구 상자</a>가 있어도 한 번 쓰고 멈추면 목록은 그대로예요.',
                   'The words sound fine, but nothing is found or bought. Even with a <a href="toolcall-en.html">toolbox</a>, using it once and stopping leaves the list untouched.')},
        {"svg": P3, "hero": True, "alt": ("앵무새가 스스로 쓴 심부름 목록(비행기표 ✓, 호텔 ✓, 지금 회의 시간, 다음 짐 목록)을 보며 '다음은 달력 도구'라고 말하고, 조련사가 도구 상자에서 도구를 돌려 결과를 돌려줌", "Looking at its own errand list (flight ✓, hotel ✓, now meetings, next packing), the parrot says next: the calendar tool; the trainer runs the toolbox and returns the result"),
         "caption": ("에이전트는 목표를 받으면 심부름 목록을 스스로 짜고, 도구를 쓰고, 결과를 보고 다음 걸음을 정하는 앵무새예요.", "An agent is a parrot that, given a goal, plans its own errands, uses tools, and picks the next step from each result."),
         "small": ('보고, 생각하고, 행동하고, 또 보고. 목표만 주면 걸음은 앵무새가 정해요. 도구를 돌리는 건 여전히 <a href="toolcall-ko.html">조련사</a>고, 걸음 수와 콩 예산엔 <a href="guardrail-ko.html">울타리</a>를 쳐요.',
                   'Look, think, act, look again. Give it the goal and the parrot picks the steps. The <a href="toolcall-en.html">trainer</a> still runs the tools, and a <a href="guardrail-en.html">fence</a> caps the steps and the bean budget.'),
         "tricks": (4, [
             (GOAL_I, ("목표를 주고 걸음은 맡겨요", "Give the goal, leave the steps"), ("목록은 앵무새가 짜요", "the parrot writes the list"), "calm"),
             (TOOLBOX_I, ("도구 상자가 있어야 해요", "It needs a toolbox"), ("쪽지로 부탁해요", "it asks by note")),
             (LOOP_I, ("걸음마다 보고 고쳐요", "Look and adjust each step"), ("결과가 다음 걸음을 정해요", "the result picks the next step"), "calm"),
             (FENCE_I, ("걸음 수와 예산에 울타리", "Fence the steps and budget"), ("멈출 줄 알아야 해요", "it must know when to stop"), "warm"),
         ])},
        {"svg": P4, "alt": ("점선 원을 도는 화살표: 생각, 도구, 결과, 보고 고침. 가운데 생각하는 앵무새. 생각에서 나가는 초록 화살표 끝 ✓. 옆의 심부름 목록은 하나씩 체크됨", "Arrows around a dashed circle: think, tool, result, look and adjust; a thinking parrot in the middle; a green arrow from think leads to done ✓; the errand list beside it gets checked one by one"),
         "caption": ("생각, 도구, 결과, 다시 생각. 다 되면 끝이에요.", "Think, tool, result, think again. Done when it is all done."),
         "small": ('한 바퀴마다 심부름 목록에 ✓ 가 하나 늘어요. 도구 결과는 <a href="context-ko.html">쟁반</a>에 쌓이니 바퀴가 많을수록 쟁반이 무거워져요.',
                   'Every lap adds one ✓ to the errand list. Tool results pile up on the <a href="context-en.html">tray</a>, so more laps mean a heavier tray.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 열 걸음 중 하나가 ×, 90%의 열 제곱은 약 35%. 콩 더미 옆 땀 흘리는 앵무새. 오른쪽 초록: 나무 울타리, 조련사, 위험한 걸음은 사람이 확인", "Left, red: one of ten steps is ×, 90% to the tenth is about 35%; a sweating parrot by a bean pile. Right, green: a wooden fence, the trainer, a person checks the risky steps"),
         "caption": ("걸음이 많을수록 틀릴 기회도 많아요. 멈출 줄 모르면 콩만 먹어요.", "More steps, more chances to slip. If it never stops, it just eats beans."),
         "small": ('그래서 걸음 수와 콩 예산에 <a href="guardrail-ko.html">울타리</a>를 치고, 돈·삭제 같은 걸음은 <a href="humanloop-ko.html">사람이 확인</a>해요. 순서가 늘 같은 일이면 <a href="workflow-ko.html">심부름 순서표</a>가 더 싸고 안전해요. 앵무새를 여러 마리 쓰는 건 <a href="multiagent-ko.html">앵무새 회의</a>에서.',
                   'So a <a href="guardrail-en.html">fence</a> caps the steps and the bean budget, and steps like money or delete get <a href="humanloop-en.html">a person\'s check</a>. If the order never changes, an <a href="workflow-en.html">errand checklist</a> is cheaper and safer. Using several parrots: <a href="multiagent-en.html">the parrot meeting</a>.')},
    ],
    "summary": (("<b>에이전트</b> = 목표를 받으면 <b>심부름 목록을 스스로 짜고</b>, <b>도구 상자</b>를 쓰고, <b>결과를 보고 다음 걸음</b>을 정하는 앵무새. 걸음이 많을수록 틀릴 기회도 많으니 <b>울타리</b>와 사람 확인이 필요해요.",
                 "<b>Agent</b> = a parrot that, given a goal, <b>plans its own errands</b>, uses the <b>toolbox</b>, and <b>picks the next step from each result</b>. More steps mean more chances to slip, so it needs a <b>fence</b> and a person\'s check."),
                ("AI agent. 모델이 목표를 받아 계획(planning)을 세우고, 도구 호출로 행동하고, 관찰(observation)을 보고 다시 판단하는 루프(ReAct)를 도는 구조예요. 정해진 순서를 따르는 워크플로와 달리 다음 단계를 모델이 정해요. 단계마다 오류가 누적되므로 최대 스텝·비용 한도, 가드레일, 사람 승인(human-in-the-loop)을 둬요.",
                 "A model that takes a goal, plans, acts through tool calls, observes the result and decides again — the ReAct loop. Unlike a workflow with a fixed order, the model picks the next step. Errors compound per step, so you cap steps and cost, add guardrails, and keep a human in the loop.")),
    "glossary": [
        ("에이전트", "Agent", ("심부름 목록을 스스로 짜는 앵무새.", "The parrot that plans its own errands."), ("목표를 주면 걸음은 앵무새가 정해요.", "Give it a goal and it picks the steps.")),
        ("ReAct 루프", "ReAct loop", ("생각, 도구, 결과, 다시 생각.", "Think, tool, result, think again."), ("한 바퀴마다 심부름 하나가 끝나요.", "One errand per lap.")),
        ("계획", "Planning", ("심부름 목록 쓰기.", "Writing the errand list."), ("큰 목표를 작은 걸음으로 쪼개요. 결과를 보고 고쳐 써요.", "Breaks the big goal into small steps, and rewrites them as results come in.")),
        ("도구", "Tools", ("도구 상자.", "The toolbox."), ('앵무새는 쪽지로 부탁하고 조련사가 돌려요. → <a href="toolcall-ko.html">도구 상자</a>', 'The parrot asks by note and the trainer runs it. → <a href="toolcall-en.html">the toolbox</a>')),
        ("자율성 단계", "Levels of autonomy", ("얼마나 맡기나.", "How much you hand over."), ("한 걸음마다 물어보기부터, 끝까지 혼자 가기까지. 위험할수록 덜 맡겨요.", "From asking at every step to going all the way alone. The riskier, the less you hand over.")),
        ("워크플로와의 차이", "Agent vs. workflow", ("순서표 vs 스스로 짜기.", "A checklist vs. its own plan."), ('순서가 늘 같으면 순서표가 싸고 안전해요. → <a href="workflow-ko.html">심부름 순서표</a>', 'If the order never changes, a checklist is cheaper and safer. → <a href="workflow-en.html">the errand checklist</a>')),
        ("멀티에이전트", "Multi-agent", ("앵무새 여러 마리.", "Several parrots."), ('역할을 나누고 한 마리가 조율해요. → <a href="multiagent-ko.html">앵무새 회의</a>', 'Split the roles, one parrot coordinates. → <a href="multiagent-en.html">the parrot meeting</a>')),
        ("가드레일", "Guardrail", ("울타리.", "The fence."), ('걸음 수·콩 예산·못 하는 일에 한도. → <a href="guardrail-ko.html">울타리</a>', 'Caps on steps, bean budget and forbidden moves. → <a href="guardrail-en.html">the fence</a>')),
    ],
}
