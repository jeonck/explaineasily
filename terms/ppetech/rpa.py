from _draw import *
from _world import *

ARM_I = icon('<rect x="28" y="8" width="8" height="24" fill="#8A8A8A"/><circle cx="32" cy="8" r="8" fill="var(--accent)"/>'
             '<rect x="16" y="32" width="32" height="10" rx="4" fill="#5B8DEF"/><path d="M20 42 l-4 14 M44 42 l4 14" stroke="#5B8DEF" stroke-width="5" stroke-linecap="round"/>')
RULE_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
              '<path d="M20 22 h24 M20 32 h24 M20 42 h16" stroke="var(--ink)" stroke-width="3"/>')
LOOP_I = icon('<path d="M18 32 a14 14 0 1 1 6 11" fill="none" stroke="var(--good)" stroke-width="5"/><path d="M24 43 l-9 2 l3 -9z" fill="var(--good)"/>')
STOP_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M18 18 l28 28" stroke="var(--bad)" stroke-width="5"/>')

# 1. 매표소 직원이 같은 표를 하루 종일 찍어내요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SWEAT, **GUIDE)
         + booth(360, 100, 220, 130, 1.0, "var(--accent)", "⟦매표소|TICKETS⟧")
         + label(380, 250, "⟦같은 표를 하루에 몇백 장씩 손으로 찍어요|stamping the same ticket by hand, hundreds of times a day⟧", 12, "var(--bad)")
         + label(380, 280, "⟦재미도 없고, 가끔 숫자를 잘못 눌러요|boring work, and sometimes the number gets mistyped⟧", 12, "var(--ink)"))

# 2. 사람이 하면 지치고, 실수도 생겨요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=FROWN + SWEAT, **GUIDE)
         + bubble(300, 80, 230, 44, "⟦클릭, 복사, 붙여넣기... 또 클릭...|click, copy, paste... click again...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 260, "⟦규칙은 간단한데, 양이 너무 많아서 사람이 지쳐요|the rule is simple — there's just too much of it for a person⟧", 12, "var(--ink)"))

# 3. RPA = 반복 작업만 그대로 따라 하는 로봇 안내원 (hero)
P3 = svg(340, sky(340)
         + booth(260, 80, 240, 140, 1.0, "var(--good)", None)
         + person(380, 170, s=1.0, face=EYES, hat=None, shirt="#8A8A8A")
         + label(380, 230, "⟦로봇 매표|ROBOT TICKETS⟧", 12, "#fff", cls="d")
         + person(180, 190, s=0.8, face=SMILE, **VISITOR)
         + label(380, 30, "⟦RPA = 정해진 규칙대로 반복 작업만 그대로 따라 하는 로봇 직원|RPA = a robot worker that just repeats a fixed, rule-based task⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦생각하지 않아요, 정해준 순서만 빠르고 정확하게 반복해요|it doesn't think — it repeats the given steps, fast and exact⟧", 12, "var(--muted)"))

# 4. RPA가 할 수 있는 일 vs 못하는 일
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦이런 일만 할 수 있어요|WHAT RPA CAN DO⟧",
                     ("⟦✓ 정해진 양식 복사/붙여넣기|✓ copy-paste a fixed form⟧",
                      "⟦✓ 매번 같은 순서로 클릭하기|✓ click in the same order every time⟧",
                      "⟦× 처음 보는 상황 스스로 판단|× judge a brand-new situation on its own⟧",
                      "⟦× '왜'를 묻는 질문에 답하기|× answer a question that starts with 'why'⟧"), 1.0, hl=1)
         + person(560, 150, s=0.75, face=EYES, **DEMO)
         + label(560, 260, "⟦규칙이 바뀌면 로봇도 다시 가르쳐야 해요|if the rule changes, the robot has to be retaught⟧", 11, "var(--muted)"))

# 5. 한계 - 규칙 밖 상황은 못 다뤄요
P5 = svg(330, '<rect width="380" height="330" fill="var(--good-soft)"/><rect x="380" width="380" height="330" fill="var(--bad-soft)"/>'
         + person(190, 130, s=0.8, face=SMILE, hat=None, shirt="#8A8A8A") + label(190, 260, "⟦똑같은 표는 눈 깜짝할 새 끝내요|the same ticket, finished in a blink⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=FROWN, hat=None, shirt="#8A8A8A") + label(570, 90, "⟦?|?⟧", 28, "var(--bad)", cls="d")
         + label(570, 260, "⟦양식이 조금만 바뀌어도 멈춰버려요|the moment the form changes even slightly, it stalls⟧", 11, "var(--ink)")
         + label(380, 305, "⟦빠르고 정확하지만, '융통성'은 없는 직원이에요|fast and exact — but with zero flexibility⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "rpa", "order": 15,
    "title": ("규칙대로만 반복하는 로봇 직원", "The Robot Worker That Only Repeats the Rule"),
    "h1": ("<em>RPA</em>가 뭐예요?", "What is <em>RPA</em>?"),
    "sub": ("RPA(로봇 프로세스 자동화)를, 매표소 반복 업무를 그대로 따라 하는 로봇 직원 이야기로 풀어봤어요.",
            "RPA (Robotic Process Automation), told as a story about a robot worker who repeats the ticket booth's routine exactly."),
    "panels": [
        {"svg": P1, "alt": ("매표소 직원이 같은 표를 하루 종일 손으로 찍어내며 진땀을 흘림", "A ticket-booth clerk sweats, stamping the same ticket by hand all day"),
         "caption": ("같은 표를 하루에 몇백 장씩 손으로 찍어요.", "Stamping the same ticket by hand, hundreds of times a day."),
         "small": ("재미도 없고, 가끔 숫자를 잘못 눌러요.", "Boring work, and sometimes the number gets mistyped.")},
        {"svg": P2, "alt": ("직원이 클릭, 복사, 붙여넣기를 반복하며 지쳐함", "A clerk, exhausted from clicking, copying, and pasting over and over"),
         "caption": ("사람이 하면 지치고, 실수도 생겨요.", "When a person does it, they get tired — and mistakes creep in."),
         "small": ("규칙은 간단한데, 양이 너무 많아서 사람이 지쳐요.", "The rule is simple — there's just too much of it for a person.")},
        {"svg": P3, "hero": True, "alt": ("로봇 직원이 매표소에서 표를 찍고, 관람객이 웃으며 받음", "A robot worker stamps tickets at the booth while a visitor smiles and takes one"),
         "caption": ("RPA는 반복 작업만 그대로 따라 하는 로봇 직원이에요.", "RPA is a robot worker that just repeats a fixed, rule-based task."),
         "small": ("생각하지 않아요, 정해준 순서만 빠르고 정확하게 반복해요.", "It doesn't think — it repeats the given steps, fast and exact."),
         "tricks": (4, [
             (RULE_I, ("규칙 받기", "Take the rule"), ("사람이 알려준 순서예요", "the steps a person taught it")),
             (ARM_I, ("그대로 따라 하기", "Repeat exactly"), ("클릭·복사를 똑같이요", "same clicks, same copy-paste"), "calm"),
             (LOOP_I, ("쉬지 않고 반복하기", "Repeat endlessly"), ("몇백 번이라도 지치지 않아요", "no fatigue, even after hundreds of runs")),
             (STOP_I, ("규칙 밖이면 멈추기", "Stop outside the rule"), ("낯선 상황은 못 풀어요", "it can't handle anything unfamiliar"), "warm"),
         ])},
        {"svg": P4, "alt": ("'RPA가 할 수 있는 일' 설명판: 복사·클릭은 가능, 새로운 판단이나 '왜'는 불가능", "A board lists what RPA can do — copy, click — and what it can't: judging the new, answering 'why'"),
         "caption": ("정해진 양식과 순서만 반복할 수 있어요.", "It can only repeat a fixed form and order."),
         "small": ("규칙이 바뀌면 로봇도 다시 가르쳐야 해요.", "If the rule changes, the robot has to be retaught.")},
        {"svg": P5, "alt": ("왼쪽: 로봇이 같은 표는 빠르게 처리. 오른쪽: 양식이 바뀌자 물음표를 띄우며 멈춤", "Left: the robot handles the same ticket fast. Right: it halts with a question mark the moment the form changes"),
         "caption": ("규칙 밖 상황은 다루지 못해요.", "It can't handle anything outside the rule."),
         "small": ("빠르고 정확하지만, '융통성'은 없는 직원이에요.", "Fast and exact — but with zero flexibility.")},
    ],
    "summary": (("<b>RPA</b> = 사람이 가르쳐 준 <b>정해진 순서</b>를 소프트웨어 로봇이 <b>클릭 하나까지 그대로</b> 반복하는 자동화.",
                 "<b>RPA</b> = automation where a software robot repeats the exact, fixed sequence a person taught it, down to every click."),
                ("RPA(Robotic Process Automation)는 사람의 화면 조작(클릭, 입력, 복사·붙여넣기)을 그대로 흉내 내어 반복적인 사무 업무를 자동화하는 소프트웨어예요. 규칙 기반이라 예외 상황이나 비정형 판단에는 약하고, AI와 결합한 '지능형 RPA(IPA)'로 보완하기도 해요.",
                 "RPA (Robotic Process Automation) is software that mimics a person's screen actions — clicks, typing, copy-paste — to automate repetitive office work. Because it's rule-based, it struggles with exceptions or unstructured judgment, which is why it's sometimes paired with AI as 'Intelligent RPA' (IPA).")),
    "glossary": [
        ("RPA", "RPA", ("규칙대로만 반복하는 로봇 직원.", "A robot worker that only repeats the rule."), ("클릭 하나까지 사람 흉내를 내요.", "It mimics even a single click.")),
        ("비정형 업무", "Unstructured Task", ("매번 모양이 달라지는 일.", "A task whose shape changes every time."), ("RPA가 가장 어려워하는 영역이에요.", "This is where RPA struggles most.")),
        ("지능형 RPA(IPA)", "Intelligent RPA (IPA)", ("로봇에게 AI 눈을 달아준 버전.", "The version where the robot gets AI eyes."), ("규칙 밖 판단을 조금씩 보완해요.", "It fills in some judgment outside the fixed rule.")),
        ("워크플로 자동화", "Workflow Automation", ("여러 부스를 잇는 자동 길.", "An automatic path linking several booths."), ("RPA는 그 길 위의 로봇 한 대예요.", "RPA is one robot running along that path.")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
        ("핀테크", "Fintech", ("매표소 결제도 자동화한 모습.", "What it looks like when ticket payment itself is automated."), ('전시장을 나서며 보는 마지막 부스예요. → <a href="fintech-ko.html">핀테크·간편결제</a>', 'The last booth you pass on the way out. → <a href="fintech-en.html">Fintech & simple payment</a>')),
        ("CPS", "CPS", ("화면과 실제 기계가 맞물려 움직이는 것.", "Screen and real machine moving in lockstep."), ('RPA는 화면 안에서만 일해요, 이쪽은 기계까지 움직여요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', "RPA only works inside the screen — this one moves real machines too. → <a href=\"cps-en.html\">Cyber-Physical Systems</a>")),
        ("스마트팜", "Smart Farm", ("농사의 반복 작업을 자동화한 버전.", "The farming version of automating repetitive work."), ('비슷한 자동화가 다른 부스에도 있어요. → <a href="smartfarm-ko.html">스마트팜</a>', 'A similar kind of automation lives at another booth. → <a href="smartfarm-en.html">Smart Farm</a>')),
    ],
}
