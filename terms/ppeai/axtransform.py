from _draw import *
from _world import *

# 1. AI 카메라만 하나 얹었을 뿐, 나머지는 그대로예요
P1 = svg(300, sky(300)
         + conveyor(80, 230, 300)
         + produce(180, 198, 1.0, "var(--good)") + produce(240, 198, 1.0, "var(--good)")
         + gradeboard(140, 110, 120, 60, "", ("⟦AI 카메라 설치!|an AI camera, installed!⟧",), 0.8)
         + person(480, 170, s=0.75, face=SWEAT + EYES, **OPERATOR)
         + label(480, 270, "⟦분류함은 여전히 제가 손으로 날라요|but I still carry the bins by hand, same as always⟧", 11, "var(--muted)")
         + person(660, 170, s=0.7, face=FROWN, **INSPECTOR)
         + label(660, 270, "⟦결재 서류도 그대로예요|and the paperwork's still the same too⟧", 11, "var(--muted)")
         + label(380, 25, "⟦AI 카메라만 하나 얹었을 뿐, 나머지는 그대로예요|just one AI camera bolted on — everything else stays exactly the same⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가: 도구만 바꾸고 일하는 방식은 그대로면, 병목은 그대로 남아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 130, s=0.8, face=EYES, **OPERATOR) + label(160, 248, "⟦판정은 빨라졌어요|the judging got faster⟧", 11, "var(--ink)")
         + person(400, 130, s=0.8, face=FROWN, **INSPECTOR) + label(400, 248, "⟦근데 결재는 여전히 사흘 걸려요|but the sign-off still takes three days⟧", 11, "var(--bad)")
         + person(640, 130, s=0.8, face=FROWN, **TEACHER) + label(640, 248, "⟦보고 체계도 안 바뀌었어요|and the reporting chain never changed⟧", 11, "var(--bad)")
         + label(380, 282, "⟦도구만 바꾸고 일하는 방식은 그대로면, 병목은 그대로 남아요|swap the tool but keep the old way of working, and the bottleneck stays right where it was⟧", 12, "var(--ink)", cls="d"))

# 3. AX = AI를 중심에 놓고 검사장이 일하는 방식 자체를 처음부터 다시 설계하는 것 (hero)
P3 = svg(360, sky(360)
         + label(380, 25, "⟦AX = AI를 중심에 놓고, 일하는 방식 자체를 처음부터 다시 설계하는 거예요|AX puts AI at the center and redesigns the way of working itself, from the ground up⟧", 13, "var(--ink)", cls="d")
         + gradeboard(60, 60, 300, 230, "⟦예전 방식|THE OLD WAY⟧",
                 ("⟦사람이 보고 사람이 분류함|a person looks, a person sorts⟧",
                  "⟦결재는 종이로, 한 단계씩|sign-off on paper, one step at a time⟧",
                  "⟦AI는 카메라 한 대로 거들 뿐|AI just helps out as one extra camera⟧"), 1.0)
         + gradeboard(400, 60, 300, 230, "⟦AX 이후|AFTER AX⟧",
                 ("⟦AI가 보고 분류하고, 사람은 예외만|AI looks and sorts; a person handles only the exceptions⟧",
                  "⟦결재는 실시간 데이터로 자동 흐름|sign-off flows automatically, on live data⟧",
                  "⟦역할·보고 체계까지 AI 중심으로 재설계|roles and reporting are redesigned around AI itself⟧"), 1.0)
         + f'<path d="M360 175 H400" stroke="var(--accent)" stroke-width="4" marker-end="url(#axa)"/>'
         + '<defs><marker id="axa" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="var(--accent)"/></marker></defs>')

FLOW_I = icon('<path d="M10 32 H54" stroke="var(--accent)" stroke-width="4"/><circle cx="20" cy="32" r="6" fill="var(--good)"/><circle cx="44" cy="32" r="6" fill="var(--good)"/>')
ROLE_I = icon('<circle cx="22" cy="20" r="8" fill="var(--accent)"/><circle cx="42" cy="20" r="8" fill="var(--muted)"/><path d="M10 54 q12 -16 24 0 M30 54 q12 -16 24 0" stroke="var(--accent)" stroke-width="3" fill="none"/>')
DATA_I = icon('<rect x="14" y="40" width="10" height="16" fill="var(--accent)"/><rect x="27" y="26" width="10" height="30" fill="var(--accent)"/><rect x="40" y="14" width="10" height="42" fill="var(--good)"/>')
CULTURE_I = icon('<path d="M32 10 L54 20 V32 C54 44 44 54 32 58 C20 54 10 44 10 32 V20 Z" fill="var(--good)"/>')

PAGE = {
    "slug": "axtransform", "order": 12,
    "title": ("검사장 전체를 다시 설계하다", "Redesigning the Whole Station Around AI"),
    "h1": ("<em>AX(AI 전환)</em>가 뭐예요?", "What is <em>AX (AI Transformation)</em>?"),
    "sub": ("AX를, AI 카메라 한 대를 얹는 것을 넘어 검사장이 일하는 방식 자체를 다시 설계하는 이야기로 풀어봤어요.",
            "AX, told as a story about redesigning the way a whole inspection station works — not just bolting on one AI camera."),
    "panels": [
        {"svg": P1, "alt": ("컨베이어 위에 AI 카메라 하나만 설치됐을 뿐, 조작원은 여전히 분류함을 손으로 나르고 결재 서류도 그대로임", "Only an AI camera gets added to the belt — the operator still carries bins by hand, and the paperwork hasn't changed"),
         "caption": ("AI 카메라만 하나 얹었을 뿐, 나머지는 그대로예요.", "Just one AI camera bolted on — everything else stays the same."),
         "small": ("분류함도, 결재 서류도 예전 그대로예요.", "The bins and the paperwork are still exactly as they were.")},
        {"svg": P2, "alt": ("판정은 빨라졌지만 결재는 여전히 사흘 걸리고 보고 체계도 그대로라는 세 사람의 말", "Judging got faster, but three people note sign-off still takes three days and reporting never changed"),
         "caption": ("도구만 바뀌고, 일하는 방식은 그대로예요.", "Only the tool changed — the way of working stayed the same."),
         "small": ("병목은 그대로 남아요.", "The bottleneck stays right where it was.")},
        {"svg": P3, "hero": True, "alt": ("예전 방식 표에서 AX 이후 표로 화살표가 이어지며, 역할·결재·보고 체계가 통째로 재설계됨을 보여줌", "An arrow runs from the old-way board to the after-AX board, showing roles, sign-off, and reporting all redesigned together"),
         "caption": ("AI를 중심에 놓고, 일하는 방식 자체를 처음부터 다시 설계하는 거예요.", "It puts AI at the center and redesigns the way of working itself, from the ground up."),
         "small": ("카메라 하나를 더하는 게 아니라, 검사장 전체의 그림을 다시 그려요.", "Not one more camera added on — the whole station's blueprint gets redrawn."),
         "tricks": (4, [
             (FLOW_I, ("업무 흐름 다시 그리기", "Redraw the workflow"), ("단계 자체를 다시 설계해요", "redesigning the steps themselves"), "calm"),
             (ROLE_I, ("사람 역할 재배치하기", "Reassign human roles"), ("사람은 예외만 맡아요", "a person handles only the exceptions")),
             (DATA_I, ("데이터로 운영 최적화하기", "Optimize operations with data"), ("검사장 전체를 데이터로 봐요", "seeing the whole station through its data"), "warm"),
             (CULTURE_I, ("조직·문화까지 바꾸기", "Change the culture too"), ("기술만으론 안 끝나요", "technology alone doesn't finish the job")),
         ])},
        {"svg": svg(300, sky(300) + gradeboard(60, 20, 640, 260, "⟦DX에서 AX로|FROM DX TO AX⟧",
                 ("⟦전산화 — 종이를 화면으로 옮김|digitization — moving paper onto a screen⟧",
                  "⟦자동화(DX) — 정해진 규칙을 기계가 대신함|automation (DX) — a machine follows the fixed old rules⟧",
                  "⟦AX — AI가 직접 판단하고, 일하는 구조 자체를 재설계함|AX — AI judges for itself, and the structure of work is redesigned⟧",
                  "⟦AX는 DX의 다음 단계가 아니라, 다른 질문에서 시작해요|AX isn't just the next step after DX — it starts from a different question⟧"), 1.0)),
         "alt": ("전산화·자동화(DX)·AX 세 단계를 적은 표", "A board laying out digitization, automation (DX), and AX as three stages"),
         "caption": ("DX는 '기존 일을 더 빠르게', AX는 '일 자체를 다시'예요.", "DX asks 'how do we do the same work faster'; AX asks 'what should the work even be'."),
         "small": ("질문이 다르기 때문에, 조직과 역할까지 함께 바뀌어요.", "Because the question itself is different, the organization and its roles change along with it.")},
        {"svg": svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
                 + person(190, 150, s=0.8, face=FROWN, **OPERATOR) + label(190, 250, "⟦기술만 있으면 될 줄 알았어요|thought the technology alone would be enough⟧", 11, "var(--bad)")
                 + person(570, 150, s=0.8, face=SMILE, **TEACHER) + label(570, 250, "⟦사람들이 새 역할에 익숙해지는 게 먼저예요|getting people used to their new roles comes first⟧", 11, "var(--ink)")
                 + label(380, 282, '⟦AX는 기술보다 변화관리가 더 어렵고, 되돌릴 땐 <a href="aiethicsgov-ko.html">원칙판</a>과 <a href="airiskframe-ko.html">운영 지도</a>가 먼저 있어야 해요|AX is harder as change management than as technology, and needs both a <a href="aiethicsgov-en.html">charter</a> and an <a href="airiskframe-en.html">operations map</a> already in place⟧', 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 조작원이 기술만 있으면 될 줄 알았다고 후회함. 오른쪽: 교사가 사람들이 새 역할에 익숙해지는 게 먼저라고 말함", "Left: the operator regrets thinking technology alone would be enough. Right: the teacher says getting people used to new roles comes first"),
         "caption": ("AX는 기술보다 변화관리가 더 어려워요.", "AX is harder as change management than as technology."),
         "small": ("등급 원칙판과 운영 지도 없이 구조부터 바꾸면, 오히려 혼란만 커져요.", "Restructuring before the charter and the operations map are in place only breeds confusion.")},
    ],
    "summary": (("<b>AX</b> = AI 카메라 한 대를 얹는 게 아니라, <b>검사장이 일하는 방식 자체</b>를 AI 중심으로 <b>처음부터 다시 설계</b>하는 것.",
                 "<b>AX</b> = not bolting on one AI camera, but <b>redesigning the way of working itself</b>, from the ground up, <b>around AI</b>."),
                ("AX(AI Transformation, AI 전환)는 기존 업무에 AI 도구를 얹는 수준(전산화·자동화·DX)을 넘어, AI를 중심에 놓고 업무 프로세스·조직 구조·의사결정 방식 자체를 재설계하는 변화예요. DX(디지털 전환)가 '같은 일을 더 빠르고 정확하게' 하는 데 초점을 둔다면, AX는 '애초에 일을 어떻게 다시 짤 것인가'라는 다른 질문에서 출발해요. 기술 도입보다 조직의 역할 재배치와 변화관리가 더 큰 과제이고, 구조를 바꾸기 전에 AI 윤리기준·거버넌스와 AI 리스크 관리 프레임워크 같은 원칙과 절차가 먼저 갖춰져 있어야 해요.",
                 "AX (AI Transformation) goes beyond bolting AI tools onto existing work — digitization, automation, DX — to redesign the work process, the organizational structure, and the decision-making itself, with AI placed at the center. Where DX (digital transformation) focuses on doing the same work faster and more accurately, AX starts from a different question: how should the work be structured in the first place? Reassigning human roles and managing change turn out to matter more than the technology itself, and before restructuring, principles and procedures like AI ethics/governance and an AI risk management framework need to already be in place.")),
    "glossary": [
        ("AX(AI 전환)", "AX (AI transformation)", ("검사장 전체를 다시 설계하는 것.", "Redesigning the whole station from the ground up."), ("카메라 한 대를 얹는 것과는 완전히 달라요.", "Entirely different from just bolting on one camera.")),
        ("DX(디지털 전환)", "DX (digital transformation)", ("같은 일을 화면과 자동화로 더 빠르게 하는 것.", "Doing the same work faster, through screens and automation."), ("AX는 DX의 다음 단계가 아니라, 다른 질문에서 시작해요.", "AX isn't the next step after DX — it starts from a different question.")),
        ("업무 재설계", "Process redesign", ("일하는 단계 자체를 다시 그리는 것.", "Redrawing the steps of the work itself."), ("AX의 핵심 작업이에요.", "The core work of AX.")),
        ("변화관리", "Change management", ("사람들이 새 역할에 익숙해지도록 돕는 것.", "Helping people get used to their new roles."), ("기술보다 이게 더 어려운 경우가 많아요.", "Often the harder part — harder than the technology itself.")),
        ("AI 윤리기준·거버넌스", "AI ethics & governance", ("구조를 바꾸기 전에 먼저 있어야 할 원칙판.", "The charter that needs to exist before any restructuring."), ('AX가 기대는 원칙이에요. → <a href="aiethicsgov-ko.html">모든 검사장이 함께 쓰는 등급 원칙판</a>', 'The principle AX leans on. → <a href="aiethicsgov-en.html">The Grading Charter Every Station Shares</a>')),
        ("AI 리스크 관리 프레임워크", "AI risk management framework", ("구조를 바꾸는 동안에도 계속 도는 운영 지도.", "The operations map that keeps running even while the structure changes."), ('AX 과정에서도 멈추지 않아요. → <a href="airiskframe-ko.html">검사장 전체를 도는 운영 지도</a>', "Doesn't pause just because AX is underway. → <a href=\"airiskframe-en.html\">The Operations Map That Walks the Whole Station</a>")),
        ("예외 처리", "Exception handling", ("AX 이후 사람에게 남는 몫.", "What's left for a person to do, after AX."), ("사람이 전부가 아니라, 드문 경우만 맡게 돼요.", "Not everything — just the rare cases that still need a person.")),
        ("데이터 기반 운영", "Data-driven operations", ("검사장 전체를 숫자로 보고 최적화하는 것.", "Seeing and optimizing the whole station through its numbers."), ("AX가 지향하는 운영 방식이에요.", "The operating style AX is aiming toward.")),
    ],
}
