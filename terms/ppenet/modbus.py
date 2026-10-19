from _draw import *
from _world import *

# 1. 공장 안 낡은 기계들, 서로 다른 말을 써서 소통이 안 됨
P1 = svg(300, sky(300)
         + postoffice(140, 150, 0.7)
         + person(340, 170, s=0.7, face=FROWN, **SORTER) + person(480, 170, s=0.7, face=FROWN, **SENDER) + person(620, 170, s=0.7, face=FROWN, **RECEIVER)
         + label(380, 40, "⟦공장 안 낡은 기계들이 서로 다른 말을 써요|old factory machines all speak different languages⟧", 13, "var(--ink)")
         + label(380, 270, "⟦우체국장이 상태를 물어도 아무도 못 알아들어요|the clerk asks for a status, but nobody understands⟧", 13, "var(--bad)"))

# 2. 누가 먼저 말할지도 정해야 함 — 다 같이 말하면 뒤섞임
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(240, 160, s=0.7, face=EYES, **SORTER) + bubble(180, 90, 150, 36, "⟦저요 저요!|me, me!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(400, 160, s=0.7, face=EYES, **SENDER) + bubble(340, 110, 150, 36, "⟦아니 저부터요!|no, me first!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 160, s=0.7, face=EYES, **RECEIVER) + bubble(500, 90, 150, 36, "⟦다 뒤섞여요!|it's all jumbled!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦동시에 말하면 누구 말인지 알 수가 없어요|if everyone talks at once, no one can tell whose message is whose⟧", 12, "var(--ink)"))

# 3. hero: Modbus = 우체국장이 순서대로 하나씩 물어보는 간단한 쪽지 규칙
P3 = svg(340, sky(340)
         + person(380, 110, s=0.9, face=EYES, **CLERK)
         + person(220, 220, s=0.6, face=SMILE, **SORTER) + envelope(220, 170, 0.45, text="①")
         + person(380, 230, s=0.6, face=SMILE, **SENDER) + envelope(380, 180, 0.45, text="②")
         + person(540, 220, s=0.6, face=SMILE, **RECEIVER) + envelope(540, 170, 0.45, text="③")
         + label(380, 30, "⟦Modbus = 우체국장이 번호 순서대로 하나씩 물어보는 쪽지 규칙|Modbus = a note rule where the clerk asks one machine at a time, in order⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦기계들은 묻는 말에만 짧게 답해요|machines only answer when asked, and briefly⟧", 12, "var(--muted)"))

I1 = icon('<circle cx="32" cy="18" r="10" fill="var(--accent)"/><circle cx="14" cy="46" r="8" fill="var(--stone)"/><circle cx="32" cy="46" r="8" fill="var(--stone)"/><circle cx="50" cy="46" r="8" fill="var(--stone)"/>')
I2 = icon('<path d="M14 24 h36 M14 24 l8 -8 M14 24 l8 8" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M50 40 h-36 M50 40 l-8 -8 M50 40 l-8 8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
I3 = icon('<rect x="10" y="20" width="44" height="24" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M18 32 h28" stroke="var(--accent)" stroke-width="4"/>')
I4 = icon('<rect x="10" y="14" width="44" height="36" rx="6" fill="none" stroke="var(--stone)" stroke-width="4"/><path d="M22 50 v-36 M42 50 v-36" stroke="var(--stone)" stroke-width="3"/>')

# 4. Modbus 쪽지 주고받기 — 번호·요청·응답
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦Modbus 쪽지 규칙|MODBUS NOTE RULE⟧",
                    ("⟦마스터 — 우체국장만 먼저 쪽지를 보낼 수 있어요|master — only the clerk sends the first note⟧",
                     "⟦슬레이브 — 기계는 번호가 불릴 때만 답해요|slave — a machine replies only when its number is called⟧",
                     "⟦레지스터 — 쪽지엔 정해진 칸 번호로 값을 적어요|register — the note holds values by fixed slot numbers⟧",
                     "⟦단순함 — 암호화도 없이 아주 가벼운 규칙이에요|simplicity — a very light rule, with no encryption at all⟧"), 1.0))

# 5. 한계: 단순하고 오래된 규칙이라 느리고, 지키는 사람도 없어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.75, face=EYES, **CLERK) + label(190, 240, "⟦한 번에 하나씩이라 느려요|one at a time, so it's slow⟧", 11, "var(--ink)")
         + person(570, 150, s=0.75, face=FROWN, **CLERK) + label(570, 240, "⟦누구나 끼어들 수 있어요(보안 없음)|anyone can butt in — no security at all⟧", 11, "var(--ink)")
         + label(380, 282, "⟦공장 안 통신용으로 만들어진 오래된 규칙, 요즘은 보안 대책을 따로 둬요|an old factory-floor rule — modern setups add security separately⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "modbus", "order": 16,
    "title": ("우체국장이 순서대로 묻는 쪽지 규칙", "The Note Rule Where the Clerk Asks One at a Time"),
    "h1": ("<em>Modbus 프로토콜</em>이 뭐예요?", "What is the <em>Modbus Protocol</em>?"),
    "sub": ("Modbus를, 공장 안 우체국장이 기계마다 번호를 불러 순서대로 묻는 쪽지 규칙 이야기로 풀어봤어요.",
            "Modbus, told as a story about a factory clerk calling each machine by number and asking one at a time."),
    "panels": [
        {"svg": P1, "alt": ("공장 안 낡은 기계 세 대가 서로 다른 말을 써서 우체국장의 질문을 못 알아들음", "Three old factory machines speak different languages and can't understand the clerk's question"),
         "caption": ("공장 안 낡은 기계들이 서로 다른 말을 써요.", "Old factory machines all speak different languages."),
         "small": ("우체국장이 상태를 물어도 아무도 못 알아들어요.", "The clerk asks for a status, but nobody understands.")},
        {"svg": P2, "alt": ("기계 세 대가 동시에 말하려다 서로 뒤섞임", "Three machines all try to speak at once and get jumbled"),
         "caption": ("누가 먼저 말할지도 정해야 해요.", "Who speaks first has to be decided too."),
         "small": ("동시에 말하면 누구 말인지 알 수가 없어요.", "If everyone talks at once, no one can tell whose message is whose.")},
        {"svg": P3, "hero": True, "alt": ("우체국장이 기계 세 대에게 번호 순서대로 하나씩 쪽지를 보내고 각 기계가 차례로 답함", "The clerk sends notes to three machines one at a time by number, and each replies in turn"),
         "caption": ("Modbus = 번호 순서대로 하나씩 묻는 쪽지 규칙이에요.", "Modbus = a note rule asking one machine at a time, in order."),
         "small": ("기계들은 묻는 말에만 짧게 답해요.", "Machines only answer when asked, and briefly."),
         "tricks": (4, [
             (I1, ("마스터·슬레이브", "Master-Slave"), ("우체국장이 먼저 물어요", "the clerk asks first")),
             (I2, ("요청·응답", "Request-Reply"), ("묻고 답하는 짝", "a pair — ask, then answer"), "calm"),
             (I3, ("레지스터", "Register"), ("정해진 칸에 값을 적어요", "writes values into fixed slots")),
             (I4, ("단순함", "Simplicity"), ("아주 가벼운 규칙", "a very light rule"), "warm"),
         ])},
        {"svg": P4, "alt": ("Modbus 쪽지 규칙 안내판: 마스터, 슬레이브, 레지스터, 단순함 네 줄", "A guide board listing master, slave, register, and simplicity for the Modbus note rule"),
         "caption": ("쪽지엔 정해진 규칙이 있어요.", "The note follows a fixed set of rules."),
         "small": ("암호화도 없이 아주 가벼운 규칙이에요.", "It's a very light rule, with no encryption at all.")},
        {"svg": P5, "alt": ("왼쪽: 한 번에 하나씩이라 느림. 오른쪽: 누구나 끼어들 수 있어 보안이 없음", "Left: one at a time, so it's slow. Right: anyone can butt in — no security"),
         "caption": ("단순하고 오래된 규칙이라 한계도 있어요.", "Being simple and old, it has its limits."),
         "small": ("요즘은 보안 대책을 따로 둬서 써요.", "Modern setups add security measures separately.")},
    ],
    "summary": (("<b>Modbus</b> = 우체국장(마스터)이 기계(슬레이브)마다 <b>번호를 불러 순서대로</b> 묻고 답하는, 아주 단순한 쪽지 규칙.",
                 "<b>Modbus</b> = a very simple note rule where the clerk (master) calls each machine (slave) <b>by number, one at a time</b>."),
                ("Modbus는 산업 현장의 PLC·센서 등을 연결하는 마스터-슬레이브 방식의 통신 프로토콜이에요. 마스터가 요청을 보내면 지정된 슬레이브만 응답하고, 데이터는 레지스터라는 고정된 주소 칸에 담겨요. 구조가 단순하고 가벼워 지금도 널리 쓰이지만, 기본적으로 암호화나 인증이 없어요.",
                 "Modbus is a master-slave communication protocol used to connect industrial devices like PLCs and sensors. The master sends a request and only the addressed slave replies, with data held in fixed-address slots called registers. It's simple and lightweight, still widely used today, but has no built-in encryption or authentication.")),
    "glossary": [
        ("마스터/슬레이브", "Master/Slave", ("묻는 쪽 / 불릴 때만 답하는 쪽.", "The one who asks / the one who replies only when called."), ("Modbus 통신의 기본 역할 구분이에요.", "The basic role split in Modbus communication.")),
        ("레지스터", "Register", ("값이 적히는 정해진 칸.", "The fixed slot where a value is written."), ("번호로 지정해 읽고 쓰는 공간이에요.", "A space read and written by a fixed number.")),
        ("요청/응답", "Request/Response", ("묻는 쪽지와 답하는 쪽지.", "The asking note and the replying note."), ("한 쌍으로 오가는 통신 구조예요.", "The paired back-and-forth structure of the protocol.")),
        ("Modbus TCP/RTU", "Modbus TCP/RTU", ("우체국망을 타는 버전과 전용선을 타는 버전.", "A version over the postal network, and one over a dedicated wire."), ("둘 다 같은 쪽지 규칙을 다른 통로로 보내요.", "Both carry the same note rule over different channels.")),
        ("IPC(네트워크)", "Network IPC", ("공장 바깥, 프로세스끼리 주고받는 전용 편지함.", "The dedicated mailbox different processes use to talk, outside the factory floor."), ('Modbus도 결국 이 방식의 한 예예요. → <a href="ipc-ko.html">프로세스끼리 여는 전용 편지함</a>', 'Modbus is, in a sense, one example of this. → <a href="ipc-en.html">the dedicated mailbox between processes</a>')),
        ("AMI(지능형 검침)", "AMI", ("계량기가 자동으로 값을 보고하는 망.", "The network where meters report their readings automatically."), ('산업 현장에서 비슷한 쪽지 방식이 쓰여요. → <a href="ami-ko.html">계량기가 자동으로 편지를 보내는 망</a>', 'A similar note-passing pattern shows up there too. → <a href="ami-en.html">the network where meters mail their own readings</a>')),
        ("OT/IoT 보안", "OT/IoT Security", ("오래된 공장 기계를 지키는 방법.", "How old factory machines get protected today."), ("다른 세계(보안)에서 다루는 주제예요.", "A topic covered in another world (Security).")),
        ("회선교환·패킷교환", "Circuit vs Packet Switching", ("쪽지를 전용선으로 보낼지, 조각내 보낼지.", "Whether the note travels a dedicated wire or gets split into pieces."), ('쪽지가 실제로 오가는 방식의 밑바탕이에요. → <a href="circuitpacket-ko.html">전용 도로냐, 조각내 보내기냐</a>', "The underlying way any note actually travels. → <a href=\"circuitpacket-en.html\">a dedicated road, or splitting it into pieces</a>")),
    ],
}
