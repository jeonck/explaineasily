from _draw import *
from _world import *

LEAF_P = '<path d="M32 10 C50 14 50 40 32 54 C14 40 14 14 32 10z" fill="var(--good)"/><path d="M32 16 V50" stroke="#0F5C52" stroke-width="2"/>'
DROP_P = '<path d="M32 10 C44 26 44 40 32 48 C20 40 20 26 32 10z" fill="#5B8DEF"/>'
THERM_P = '<rect x="27" y="10" width="10" height="34" rx="5" fill="#E0E0E0" stroke="#8A8A8A" stroke-width="2"/><circle cx="32" cy="48" r="9" fill="var(--bad)"/><rect x="29" y="22" width="6" height="22" fill="var(--bad)"/>'
CHIP_P = '<rect x="16" y="16" width="32" height="32" rx="4" fill="#1B2A44" stroke="#5B8DEF" stroke-width="2"/><path d="M24 16 v-6 M40 16 v-6 M24 48 v6 M40 48 v6 M16 24 h-6 M16 40 h-6 M48 24 h6 M48 40 h6" stroke="#5B8DEF" stroke-width="2"/>'


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


GREENHOUSE = ('<path d="M0 60 L90 0 L180 60 Z" fill="none" stroke="var(--good)" stroke-width="4"/>'
              '<rect y="60" width="180" height="90" fill="none" stroke="var(--good)" stroke-width="4"/>'
              '<path d="M0 60 h180 M90 0 v150" stroke="var(--good)" stroke-width="2" opacity="0.5"/>')


def greenhouse(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})">{GREENHOUSE}</g>'


LEAF_I, DROP_I, THERM_I, CHIP_I = icon(LEAF_P), icon(DROP_P), icon(THERM_P), icon(CHIP_P)


# 1. 온실 부스 작물이 자꾸 시들어요
P1 = svg(300, sky(300)
         + greenhouse(290, 70, 1.0)
         + person(560, 150, s=0.8, face=FROWN, **DEMO)
         + label(380, 250, "⟦작물이 물을 너무 많이 받거나, 너무 적게 받아요|the crops get too much water, or too little⟧", 12, "var(--bad)")
         + label(380, 280, "⟦온실이 너무 넓어서, 매일 돌아다니며 손으로 재고 물을 주기 힘들어요|the greenhouse is too big to measure and water by hand every day⟧", 12, "var(--ink)"))

# 2. 사람이 다 돌보기엔 밭이 너무 넓어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=SWEAT, **DEMO)
         + bubble(300, 68, 220, 40, "⟦저쪽 밭은 아직 못 봤는데...|haven't even checked the far field yet...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦흙 속 물기, 햇빛, 온도... 사람 눈으로는 다 확인하기 어려워요|soil moisture, sunlight, temperature — the eye alone can't track them all⟧", 12, "var(--ink)"))

# 3. 스마트팜 = 센서가 재고 기계가 알아서 돌보는 온실 부스 (hero)
P3 = svg(340, sky(340)
         + greenhouse(290, 80, 1.1)
         + glyph(350, 150, 0.7, DROP_P) + glyph(410, 150, 0.7, THERM_P)
         + person(600, 210, s=0.7, face=SMILE, **VISITOR)
         + label(380, 30, "⟦스마트팜 = 센서가 재고, 기계가 알아서 물·온도를 맞춰주는 농장(여기선 온실)|smart farm = a farm (here, a greenhouse) where sensors measure and machines adjust water and heat⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦사람은 화면의 숫자로 상태를 확인하고, 물·온도 조절은 기계가 맡아요|the person checks the on-screen numbers; machines handle water and heat⟧", 12, "var(--muted)"))

# 4. 어떻게 돌보나요
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦스마트팜의 하루|A DAY ON THE SMART FARM⟧",
                     ("⟦① 센서가 흙·공기 상태를 재요|① sensors read the soil and air⟧",
                      "⟦② 작은 컴퓨터가 잰 값을 기준과 비교해요|② a small computer compares readings to the target⟧",
                      "⟦③ 물기가 모자라면 자동으로 물을 줘요|③ if moisture is short, water comes automatically⟧",
                      "⟦④ 사람은 화면으로 상태를 확인해요|④ the person checks status on screen⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦숫자로 정밀하게 돌보는 농사를 '정밀농업'이라 불러요|farming by exact measurement is precision agriculture⟧", 11, "var(--muted)"))

# 5. 한계 - 기계가 멈추면, 결국 사람이 다시 나서야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 90, 1.0, CHIP_P) + glyph(170, 160, 0.8, LEAF_P)
         + label(190, 250, "⟦평소엔 기계가 사람보다 꼼꼼하게 돌봐요|day to day, the machine tends more carefully than a person⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN + SWEAT, **DEMO)
         + label(570, 262, "⟦센서가 고장 나거나 전기가 끊기면 다시 사람이 돌봐요|if a sensor or the power fails, a person must tend the crops⟧", 11, "var(--ink)")
         + label(380, 282, "⟦기계는 돌보는 걸 '도와주는' 거지, 농부를 없애지는 않아요|the machine helps with the tending — it doesn't replace the farmer⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "smartfarm", "order": 17,
    "title": ("센서가 돌보는 온실 부스", "The Greenhouse Booth Tended by Sensors"),
    "h1": ("<em>스마트팜</em>이 뭐예요?", "What is <em>Smart Farm</em>?"),
    "sub": ("스마트팜을, 센서와 기계가 알아서 물과 온도를 맞춰주는 과학관 온실 부스 이야기로 풀어봤어요.",
            "Smart farm, told as a story about a science-hall greenhouse booth where sensors and machines handle water and heat on their own."),
    "panels": [
        {"svg": P1, "alt": ("온실 안 작물이 시들어 있고, 시연 담당자가 당황함", "Crops wilt inside a greenhouse while a demo staffer looks worried"),
         "caption": ("작물이 물을 너무 많이 받거나, 너무 적게 받아요.", "The crops get too much water, or too little."),
         "small": ("온실이 너무 넓어서, 매일 돌아다니며 손으로 재고 물을 주기 힘들어요.", "The greenhouse is too big to measure and water by hand every day.")},
        {"svg": P2, "alt": ("시연 담당자가 넓은 밭을 다 돌보지 못해 진땀을 흘림", "A demo staffer sweats, unable to tend the whole field"),
         "caption": ("사람이 다 돌보기엔 밭이 너무 넓어요.", "The field is too big for one person to tend."),
         "small": ("흙 속 물기, 햇빛, 온도... 사람 눈으로는 다 확인하기 어려워요.", "Soil moisture, sunlight, temperature — the eye alone can't track them all.")},
        {"svg": P3, "hero": True, "alt": ("온실 안에 물방울·온도 센서가 꽂혀 있고, 관람객이 흐뭇하게 지켜봄", "Water and temperature sensors sit in the greenhouse while a visitor watches contentedly"),
         "caption": ("스마트팜은 센서가 재고, 기계가 알아서 물·온도를 맞춰주는 농장이에요. 이 부스에선 온실로 보여줘요.", "A smart farm is a farm where sensors measure and machines adjust water and heat on their own. This booth shows one as a greenhouse."),
         "small": ("사람은 화면의 숫자로 상태를 확인하고, 물·온도 조절은 기계가 맡아요.", "The person checks the on-screen numbers; machines handle water and heat."),
         "tricks": (4, [
             (DROP_I, ("물기 재기", "Measure moisture"), ("흙 속 물을 재요", "reads water in the soil")),
             (THERM_I, ("온도 재기", "Measure heat"), ("공기 온도를 재요", "reads the air temperature")),
             (CHIP_I, ("기준과 비교하기", "Compare to target"), ("정해둔 값과 견줘봐요", "checks it against the target value"), "calm"),
             (LEAF_I, ("자동으로 돌보기", "Tend automatically"), ("물·바람을 스스로 맞춰요", "adjusts water and air on its own"), "warm"),
         ])},
        {"svg": P4, "alt": ("스마트팜의 하루 설명판: 재기→비교하기→물주기→확인하기", "A board shows the smart farm's day: read, compare, water, check"),
         "caption": ("센서가 재고, 컴퓨터가 기준과 비교하고, 기계가 자동으로 물을 줘요.", "Sensors read, a computer compares, and a machine waters automatically."),
         "small": ("숫자로 정밀하게 돌보는 농사를 '정밀농업'이라고 불러요.", "Farming by exact measurement is called precision agriculture.")},
        {"svg": P5, "alt": ("왼쪽: 평소엔 잎이 잘 자람. 오른쪽: 센서가 고장 나자 시연 담당자가 다시 진땀을 흘림", "Left: in normal days the leaves thrive. Right: when a sensor fails, the staffer is back to sweating"),
         "caption": ("기계가 멈추면 결국 사람이 다시 작물을 돌봐야 해요.", "When the machine stops, a person has to tend the crops again."),
         "small": ("기계는 돌보는 걸 '도와주는' 거지, 농부를 없애지는 않아요.", "The machine helps with the tending — it doesn't replace the farmer.")},
    ],
    "summary": (("<b>스마트팜</b> = 센서가 흙과 공기 상태를 재고, 기계가 <b>물·온도를 자동으로</b> 맞춰주는 농장.",
                 "<b>Smart farm</b> = a farm where sensors read the soil and air, and machines adjust <b>water and temperature automatically</b>."),
                ("스마트팜은 IoT 센서, 자동 관개·환경 제어 장치, 데이터 분석을 결합해 작물 생육 환경을 정밀하게 관리하는 농업 방식이에요. 정밀농업(precision agriculture)과 맞닿아 있으며, 사람의 경험적 판단을 데이터 기반 자동 제어로 보완하는 데 목적이 있어요. 온실뿐 아니라 축사·과수원·노지에도 적용돼요.",
                 "A smart farm combines IoT sensors, automated irrigation and environmental control, and data analysis to precisely manage a crop's growing conditions. Closely related to precision agriculture, its goal is to supplement a farmer's experience-based judgment with data-driven automatic control. It's applied not only to greenhouses but also to livestock barns, orchards, and open fields.")),
    "glossary": [
        ("정밀농업", "Precision Agriculture", ("데이터로 정밀하게 돌보는 농사, 스마트팜과 가까운 말.", "Farming by exact data, a close relative of smart farming."), ("숫자로 정확히 돌본다는 뜻이에요.", "Tending the crop with exact numbers.")),
        ("IoT 센서", "IoT Sensor", ("흙과 공기 상태를 재는 장치.", "The device that reads soil and air conditions."), ("이 온실 곳곳에 꽂혀 있어요.", "Planted all over this greenhouse.")),
        ("자동관개", "Automated Irrigation", ("흙에 물기가 모자라면 자동으로 물을 주는 장치.", "A system that waters automatically when the soil runs dry."), ("센서 값이 기준 밑으로 떨어지면 작동해요.", "It kicks in once the sensor reading drops below target.")),
        ("엣지컴퓨팅", "Edge Computing", ("현장에서 바로 판단하는 작은 컴퓨터.", "The small computer that decides right there on the spot."), ('이 전시장 다른 부스에서도 같은 원리가 나와요. → <a href="ambientcompute-ko.html">말 안 해도 알아서 척척인 전시관</a>', 'The same idea shows up at another booth in this hall. → <a href="ambientcompute-en.html">the exhibit that just knows</a>')),
        ("RPA", "RPA", ("반복 작업만 그대로 따라 하는 로봇.", "A robot that only repeats a fixed, routine task."), ('비슷한 자동화가 다른 부스에도 있어요. → <a href="rpa-ko.html">규칙대로만 반복하는 로봇 직원</a>', 'A similar kind of automation lives at another booth. → <a href="rpa-en.html">the robot worker that only repeats the rule</a>')),
        ("CPS", "CPS", ("컴퓨터와 실제 기계가 맞물려 움직이는 것.", "Computer and real machine moving in lockstep."), ('스마트팜도 이 틀 안의 한 예시예요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', 'Smart farming is one example living inside this bigger frame. → <a href="cps-en.html">Cyber-Physical Systems</a>')),
        ("드론 보안위협", "Drone Security Threats", ("무선 신호를 노리는 공격들.", "Attacks that target a wireless control link."), ('밭 위를 나는 농업용 드론도 같은 위협을 받아요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', 'A farm drone overhead faces the same risks. → <a href="dronesecurity-en.html">the drone held up by an invisible string</a>')),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
