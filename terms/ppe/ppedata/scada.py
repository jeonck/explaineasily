from _draw import *
from _world import *

# 1. 창고 구석구석 설비가 아무도 모르게 고장나요
P1 = svg(300, sky(300)
         + person(620, 150, s=0.8, face=SWEAT + EYES, **MANAGER)
         + shelfzone(60, 150, 180, 70, 0.9)
         + fastdesk(400, 170)
         + label(240, 260, "⟦냉동고가 과열되고 있는데 아무도 몰라요|the cooler is overheating and nobody notices⟧", 12, "var(--bad)")
         + label(380, 40, "⟦창고 구석구석의 설비를 한 사람이 다 보긴 어려워요|one person can't watch every machine in every corner⟧", 13, "var(--ink)"))

# 2. 직접 걸어가서 봐야 한다면 이미 늦어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 150, s=0.8, face=FROWN, **MANAGER)
         + label(140, 258, "⟦설비까지 걸어가 봐야 상태를 아는데|I'd have to walk over to the machine to check it⟧", 11, "var(--ink)")
         + shelfzone(380, 150, 200, 70, 0.9, bad=2)
         + label(480, 260, "⟦도착했을 땐 이미 설비가 고장났어요|by the time I get there, the machine has already failed⟧", 12, "var(--bad)"))

# 3. SCADA = 창고 전체를 한 화면에서 보고 조작하는 관제실 (hero)
P3 = svg(340, sky(340, ground=False)
         + '<rect x="240" y="60" width="280" height="170" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + '<rect x="258" y="78" width="110" height="60" rx="3" fill="var(--good-soft)"/>'
         + '<rect x="380" y="78" width="110" height="60" rx="3" fill="var(--accent-soft)"/>'
         + label(313, 112, "⟦냉동고 ✓|cooler ✓⟧", 11, "var(--ink)")
         + label(435, 112, "⟦컨베이어 ✓|belt ✓⟧", 11, "var(--ink)")
         + person(380, 160, s=0.8, face=EYES, **MANAGER)
         + label(380, 30, "⟦SCADA = 설비를 한 화면에서 보고 원격으로 조작하는 관제실|SCADA = a control room watching and running every machine from one screen⟧", 13.5, "var(--ink)", cls="d")
         + label(380, 320, "⟦사람이 설비를 찾아다니지 않아도, 화면에 상태가 모여 보여요|no one has to walk around: every machine's status comes to the screen⟧", 12, "var(--muted)"))

# 4. 현장 → 센서/제어기 → 통신망 → 관제실 → 기록
P4 = svg(320, sky(320, ground=False)
         + shelfzone(30, 110, 110, 70, 0.8, label_text="⟦현장 설비|field devices⟧")
         + label(145, 148, "→", 26, "var(--muted)")
         + '<rect x="170" y="120" width="70" height="50" rx="4" fill="var(--stone)"/>' + label(205, 150, "⟦RTU/PLC|RTU/PLC⟧", 10, "#142033")
         + label(265, 148, "→", 26, "var(--muted)")
         + '<rect x="290" y="120" width="70" height="50" rx="4" fill="var(--stone)"/>' + label(325, 150, "⟦통신망|network⟧", 10, "#142033")
         + label(385, 148, "→", 26, "var(--muted)")
         + '<rect x="410" y="100" width="110" height="90" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>' + label(465, 150, "⟦HMI 화면|HMI screen⟧", 10, "#142033")
         + label(540, 148, "→", 26, "var(--muted)")
         + '<rect x="565" y="110" width="90" height="70" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(610, 150, "⟦기록(히스토리안)|log (historian)⟧", 9.5, "#142033")
         + label(380, 280, "⟦센서가 설비 상태를 모으고, 화면이 보여주고, 히스토리안이 기록을 남겨요|sensors collect machine status, the screen shows it, and the historian keeps the record⟧", 12, "var(--ink)"))

# 5. 관제실이 고쳐주진 않아요 + 통신망 보안 주의
P5 = svg(330, '<rect width="380" height="330" fill="var(--accent-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=EYES, **MANAGER)
         + label(190, 260, "⟦관제실은 고장난 설비를 알려줄 수 있어요|the control room can flag a broken machine⟧", 11, "var(--ink)")
         + person(570, 130, s=0.8, face=SMILE, **PACKER)
         + label(570, 260, "⟦고치러 가는 건 결국 사람이에요|but a person still has to go fix the machine⟧", 11, "var(--ink)")
         + label(380, 305, "⟦해킹을 막으려고 관제실 통신망은 외부망과 함부로 잇지 않아요|to keep attackers out, the control network isn't casually linked to the outside⟧", 12, "var(--ink)", cls="d"))

WATCH_I = icon('<circle cx="32" cy="18" r="10" fill="var(--accent)"/><rect x="14" y="30" width="36" height="26" rx="4" fill="none" stroke="var(--line)" stroke-width="3"/><path d="M32 38 l0 10 l8 4" stroke="var(--accent)" stroke-width="3" fill="none"/>')
GATHER_I = icon('<circle cx="20" cy="46" r="6" fill="var(--accent)"/><circle cx="44" cy="46" r="6" fill="var(--accent)"/><path d="M20 40 L32 20 L44 40" stroke="var(--muted)" stroke-width="3" fill="none"/><circle cx="32" cy="16" r="8" fill="var(--good)"/>')
LOG_I = icon('<rect x="16" y="10" width="32" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
REMOTE_I = icon('<rect x="22" y="8" width="20" height="48" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="32" cy="22" r="4" fill="var(--bad)"/><rect x="27" y="34" width="10" height="6" fill="var(--muted)"/>')

PAGE = {
    "slug": "scada", "order": 9,
    "title": ("창고 전체를 한눈에 보는 관제실", "The Control Room That Watches the Whole Warehouse"),
    "h1": ("<em>SCADA</em>가 뭐예요?", "What is <em>SCADA</em>?"),
    "sub": ("SCADA 시스템을, 창고 구석구석의 설비를 한 화면에서 보고 원격으로 다루는 관제실 이야기로 풀어봤어요.",
            "SCADA, told as a story about a control room that watches and runs every machine in the warehouse from one screen."),
    "panels": [
        {"svg": P1, "alt": ("관리자 모르게 냉동고가 과열되는 동안 창고 반대편에 서 있음", "A manager stands across the warehouse, unaware the cooler is overheating"),
         "caption": ("냉동고가 과열되고 있는데 아무도 몰라요.", "The cooler is overheating and nobody notices."),
         "small": ("창고 구석구석의 설비를 한 사람이 다 보긴 어려워요.", "One person can't watch every machine in every corner.")},
        {"svg": P2, "alt": ("관리자가 멀리 걸어가 확인해야 하는 동안 문제 구역이 이미 빨갛게 표시됨", "The manager would have to walk all the way over, but the trouble zone is already flagged red"),
         "caption": ("설비를 직접 걸어가서 봐야 한다면 고장을 막기엔 이미 늦어요.", "If you have to walk over to check a machine, it's already too late to stop the failure."),
         "small": ("도착했을 땐 이미 설비가 고장났어요.", "By the time you get there, the machine has already failed.")},
        {"svg": P3, "hero": True, "alt": ("관리자가 관제실 화면에서 냉동고와 컨베이어 상태를 동시에 확인함", "The manager checks the cooler and the conveyor belt at once on a control-room screen"),
         "caption": ("SCADA는 설비를 한 화면에서 보고 조작하는 관제실이에요.", "SCADA is a control room watching and running machines from one screen."),
         "small": ("사람이 설비를 찾아다니지 않아도, 화면에 상태가 모여 보여요.", "No one has to walk around: every machine's status comes to the screen."),
         "tricks": (4, [
             (GATHER_I, ("센서로 모으기", "Collect with sensors"), ("현장 설비 상태를요", "the state of every field device")),
             (WATCH_I, ("화면에 모아 보기", "Show it on one screen"), ("HMI로 한눈에", "all at once, on the HMI"), "calm"),
             (LOG_I, ("기록해 두기", "Log the history"), ("히스토리안에 저장", "stored by the historian")),
             (REMOTE_I, ("원격으로 조작하기", "Control it remotely"), ("설비를 화면 버튼으로 멈춰요", "stop a machine with a button on screen"), "warm"),
         ])},
        {"svg": P4, "alt": ("현장 설비에서 RTU/PLC, 통신망, HMI 화면, 기록(히스토리안)까지 이어지는 흐름도", "A flow from field devices through RTU/PLC, the network, the HMI screen, to the historian log"),
         "caption": ("신호는 현장 → 제어기 → 통신망 → 화면 → 기록 순서로 이어져요.", "The signal travels: field device → controller → network → screen → log."),
         "small": ("센서가 설비 상태를 모으고, 화면이 보여주고, 히스토리안이 기록을 남겨요.", "Sensors collect machine status, the screen shows it, and the historian keeps the record.")},
        {"svg": P5, "alt": ("왼쪽: 관리자가 고장을 알려줌. 오른쪽: 결국 고치러 가는 건 포장 담당(사람)", "Left: the manager flags the failure. Right: a worker still has to go fix it"),
         "caption": ("관제실은 고장을 알려줄 뿐, 설비를 직접 고쳐주진 않아요.", "The control room flags failures, but doesn't fix machines itself."),
         "small": ("해킹을 막으려고 관제실 통신망은 외부망과 함부로 잇지 않아요.", "To keep attackers out, the control network isn't casually linked to the outside.")},
    ],
    "summary": (("<b>SCADA</b>(감시 제어 및 데이터 수집)는 흩어진 설비의 상태를 <b>한 화면에서 모아 보고 원격으로 조작</b>하는 산업 제어 시스템이에요.",
                 "<b>SCADA</b> (Supervisory Control And Data Acquisition) is an industrial control system that <b>gathers scattered equipment status onto one screen and lets you control it remotely</b>."),
                ("SCADA는 현장 설비(센서/액추에이터)를 RTU·PLC가 신호로 바꾸고, 통신망을 거쳐 HMI 화면에 모아 보여주며, 과거 데이터는 히스토리안에 쌓아 추이를 분석해요. 전력·수도·공장 등 산업 제어 시스템(ICS)의 핵심 구성요소예요.",
                 "SCADA turns field sensors and actuators into signals via RTUs/PLCs, carries them over a network to an HMI dashboard, and stores history in a historian for trend analysis. It's a core piece of industrial control systems (ICS) in power, water, and factory settings.")),
    "glossary": [
        ("SCADA", "SCADA", ("설비를 한 화면에서 보고 조작.", "Watching and running equipment from one screen."), ("감시 제어 및 데이터 수집의 줄임말.", "Supervisory Control And Data Acquisition.")),
        ("HMI", "HMI", ("관제실 화면 자체.", "The control-room screen itself."), ("사람이 설비 상태를 보고 조작하는 창.", "The window where a person reads and operates the machines.")),
        ("PLC/RTU", "PLC/RTU", ("현장 설비에 붙는 제어기.", "The controller attached to field equipment."), ("신호를 받아 전달하거나 설비를 직접 제어해요.", "Reads signals, relays them, or controls the device directly.")),
        ("히스토리안", "Historian", ("설비 기록을 쌓아두는 서가.", "The shelf where machine logs pile up."), ("나중에 추이를 분석할 때 써요.", "Used later to analyze trends over time.")),
        ("ICS", "ICS", ("산업용 제어 시스템 전체.", "The whole industrial control system."), ("SCADA는 ICS의 한 종류예요.", "SCADA is one kind of ICS.")),
        ("에어갭", "Air Gap", ("바깥과 아예 선을 끊어두기.", "Cutting the wire to the outside entirely."), ('관제망을 지키는 극단적인 방법. → <a href="airgap-ko.html">선을 아예 끊어두는 성벽</a>', 'An extreme way to protect the control network. → <a href="airgap-en.html">the rampart that cuts the wire entirely</a>')),
        ("실시간 모니터링", "Real-time Monitoring", ("설비 상태를 지금 바로 화면으로 보는 것.", "Seeing machine status on screen as it happens."), ('SRE의 관측 가능성과 목적이 비슷해요. → <a href="observability-ko.html">계기판으로 미리 보기</a>', "Similar goal to SRE's observability. → <a href=\"observability-en.html\">seeing trouble on the dashboard first</a>")),
        ("원격 제어", "Remote Control", ("멀리 있는 설비를 화면 버튼으로 움직이기.", "Operating a distant machine with a button on screen."), ("관제실이 보기만 하지 않고 직접 조작하게 해줘요.", "Lets the control room act, not just watch.")),
    ],
}
