from _draw import *

DOORS = (("⟦프린터|Printer⟧", False), ("⟦회의실|Meeting⟧", True), ("⟦손님|Guest⟧", False), ("⟦금고|Vault⟧", True), ("⟦부엌|Kitchen⟧", False))

BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
BIGBAG = '<rect x="46" y="50" width="70" height="60" rx="6" fill="var(--night)"/><path d="M62 50 v-10 a18 18 0 0 1 36 0 v10" stroke="var(--night)" stroke-width="5" fill="none"/>'
STOOL = '<rect x="20" y="150" width="60" height="8" rx="3" fill="#8B5E3C"/><rect x="26" y="158" width="6" height="90" fill="#8B5E3C"/><rect x="68" y="158" width="6" height="90" fill="#8B5E3C"/>'
WATCHER = STOOL + person(20, 50, hat="var(--good)", shirt="var(--good)", s=0.9, face=EYES)

# 1. 개를 못 앉히는 방이 있다
P1 = svg(300, corridor(300, DOORS)
         + label(380, 280, "⟦개는 방 안에 앉아요. 그런데 못 앉는 방도 있어요.|Dogs sit inside rooms. Some rooms can\'t take one.⟧", 14, "var(--muted)"))

# 2. 어느 방에 가든 복도는 지나야 한다
P2 = svg(300, corridor(300, DOORS, marks=False)
         + '<path d="M120 250 C250 210 450 270 590 220" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
         + person(330, 150, s=0.9, face=MASK, extra=BAG)
         + label(380, 285, "⟦프린터 방에서 금고 방으로 가려면, 복도.|From the printer room to the vault: the hallway.⟧", 14, "var(--muted)"))

# 3. NDR = 복도를 지켜보는 파수꾼 (hero)
SIGHT = "".join(f'<path d="M95 100 L{x} {y}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="6 6" fill="none"/>' for x, y in ((320, 210), (520, 230), (700, 200)))
P3 = svg(300, corridor(300, DOORS, marks=False) + SIGHT + WATCHER
         + person(300, 160, hat=None, shirt="#4A5A72", s=0.75, face=SMILE, extra=BAG)
         + person(500, 175, hat="var(--good)", shirt="var(--good)", s=0.7, face=SMILE)
         + person(680, 150, hat="var(--accent)", shirt="#4A5A72", s=0.75, face=SMILE))

# 4. 이상한 걸음이 보이면 복도 문을 닫는다
PORTCULLIS = ('<rect x="640" y="60" width="90" height="220" fill="var(--stone-dark)" fill-opacity="0.5"/>'
              + "".join(f'<rect x="{x}" y="60" width="8" height="220" fill="var(--stone-dark)"/>' for x in range(646, 730, 16))
              + '<path d="M685 30 L685 56 M677 48 L685 58 L693 48" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
WHISTLE = label(150, 60, "⟦삑!|TWEET!⟧", 34, "var(--accent)", cls="d")
P4 = svg(300, corridor(300, DOORS, night_mode=True, marks=False) + WATCHER + WHISTLE
         + person(420, 140, s=0.95, face=MASK + SWEAT, extra=BIGBAG)
         + '<path d="M540 230 L630 230" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8"/>'
         + PORTCULLIS + label(685, 292, "⟦성문 쪽 복도|hallway to the gate⟧", 12, "#C9D5E6")
         + label(430, 40, "02:00", 26, "#F5E6B8", cls="d"))

# 5. 상자 안은 못 본다
SEALED = ('<g transform="translate(300,120)"><rect width="120" height="90" rx="6" fill="#C9A86A"/><rect x="52" width="16" height="90" fill="#E9B44C"/>'
          '<rect y="38" width="120" height="14" fill="#E9B44C"/>' + label(60, 58, "?", 34, "var(--night)", cls="d") + "</g>")
KNOWN = ('<g transform="translate(470,100)"><rect width="250" height="130" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(20, 36, "⟦크기: 아주 큼|size: very big⟧", 16, "var(--ink)", "start") + label(20, 68, "⟦가는 곳: 성문|going to: the gate⟧", 16, "var(--ink)", "start")
         + label(20, 100, "⟦시간: 새벽 2시|time: 2 a.m.⟧", 16, "var(--ink)", "start") + "</g>")
P5 = svg(260, '<rect width="760" height="260" fill="var(--accent-soft)"/>' + WATCHER + SEALED + KNOWN
         + label(360, 240, "⟦안은 몰라도|inside: unknown⟧", 14, "var(--muted)") + label(595, 250, "⟦겉은 다 알아요|outside: all known⟧", 14, "var(--muted)"))

WHO_I = icon('<circle cx="20" cy="20" r="8" fill="var(--good)"/><rect x="12" y="30" width="16" height="22" rx="5" fill="var(--good)"/><path d="M34 40 H52 M46 34 l6 6 -6 6" stroke="var(--good)" stroke-width="3" fill="none"/>')
WHEN_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 16 V32 L42 40" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BAG_I = icon('<rect x="14" y="26" width="36" height="28" rx="4" fill="var(--bad)"/><path d="M22 26 v-6 a10 10 0 0 1 20 0 v6" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "ndr", "order": 11,
    "title": ("복도를 지키는 사람", "The Hallway Watcher"),
    "h1": ("<em>NDR</em>이 뭐예요?", "What is <em>NDR</em>?"),
    "sub": ("네트워크 탐지·대응(Network Detection and Response)을 복도를 지키는 파수꾼 이야기로 풀어봤어요.",
            "Network Detection and Response, told as a story about the person who watches the hallway."),
    "panels": [
        {"svg": P1, "alt": ("문 다섯 개가 있는 복도. 두 문 앞엔 개가 있고 세 문엔 물음표", "A hallway with five doors; two have a dog, three only a question mark"),
         "caption": ("개를 못 앉히는 방이 있어요.", "Some rooms can't take a dog."),
         "small": ('오래된 프린터, 손님 노트북, 냉장고. <a href="edr-ko.html">개(EDR)</a>는 그 방을 못 봐요.',
                   'The old printer, a guest laptop, the fridge. The <a href="edr-en.html">dog (EDR)</a> can\'t see in there.')},
        {"svg": P2, "alt": ("가방을 든 도둑이 복도를 따라 프린터 방에서 금고 방 쪽으로 걸어감", "A burglar with a bag walking down the hallway from the printer room toward the vault"),
         "caption": ("어느 방에 가든 복도는 지나야 해요.", "Whatever room you want, you take the hallway."),
         "small": ("방은 못 봐도, 복도는 볼 수 있어요.", "You may not see the rooms, but you can see the hallway.")},
        {"svg": P3, "hero": True, "alt": ("높은 의자에 앉은 파수꾼이 복도를 오가는 세 사람을 점선으로 바라봄", "A watcher on a tall stool, dotted sight-lines on three people walking the hallway"),
         "caption": ("NDR은 복도를 지켜보는 파수꾼이에요.", "NDR is the watcher in the hallway."),
         "small": ("방에 들어가지 않아요. 지나가는 사람만 봐요.", "It never enters a room. It only watches who passes."),
         "tricks": (3, [
             (WHO_I, ("누가 어디로", "Who, where to"), ("어느 방에서 어느 방으로", "from which room to which"), "calm"),
             (WHEN_I, ("몇 시에", "When"), ("낮인지 새벽인지", "daytime or 2 a.m."), "warm"),
             (BAG_I, ("얼마나 들고", "How much"), ("작은 가방인지 큰 가방인지", "a small bag or a huge one")),
         ])},
        {"svg": P4, "alt": ("새벽 2시, 큰 가방을 든 도둑이 성문 쪽으로 가자 파수꾼이 호루라기를 불고 복도 쇠창살이 내려옴", "At 2 a.m. a burglar with a huge bag heads for the gate; the watcher blows a whistle and a portcullis drops across the hallway"),
         "caption": ("이상한 걸음이면 복도 문을 닫아요.", "A wrong kind of walk, and the hallway shuts."),
         "small": ('새벽에 큰 가방이 성문으로? 삑! 쇠창살 내리고 <a href="soc-ko.html">경비실</a>에 알려요.',
                   'A huge bag heading for the gate at 2 a.m.? Tweet! Drop the portcullis, tell the <a href="soc-en.html">guard room</a>.')},
        {"svg": P5, "alt": ("봉해진 상자에 물음표가 있고, 옆 메모엔 크기·가는 곳·시간이 적혀 있음", "A sealed box with a question mark, and a note beside it listing size, destination and time"),
         "caption": ("상자 안은 못 봐요.", "It can't see inside the box."),
         "small": ('봉해진 상자(암호화)는 크기·방향·시간만 보여요. 그래서 방 안은 <a href="edr-ko.html">개</a>가, 복도는 파수꾼이 — 둘이 같이.',
                   'A sealed box (encryption) shows only size, direction and time. So the <a href="edr-en.html">dog</a> takes the rooms, the watcher takes the hallway — together.')},
    ],
    "summary": (("<b>NDR</b> = 방이 아니라 <b>복도</b>를 지켜보는 파수꾼. 누가 어디로, 언제, 얼마나 들고 가는지 보고, 이상하면 복도를 닫아요.",
                 "<b>NDR</b> = the watcher of the <b>hallway</b>, not the rooms. Who goes where, when, carrying how much — and shuts the hallway when it's wrong."),
                ("Network Detection and Response. 방마다 개를 앉히지 않아도 돼서, 개를 못 앉히는 방까지 지켜요. 대신 봉해진 상자 안은 못 봐요.",
                 "Network Detection and Response. No dog needed in every room, so it covers the rooms that can't take one. The price: it can't open sealed boxes.")),
    "glossary": [
        ("네트워크", "Network", ("복도.", "The hallway."), ("방과 방, 성 안과 밖을 잇는 길.", "The paths between rooms, and between the castle and outside.")),
        ("트래픽", "Traffic", ("복도를 오가는 사람과 가방.", "People and bags in the hallway."), ("컴퓨터끼리 주고받는 모든 것.", "Everything computers send each other.")),
        ("탭 · 미러링", "TAP / port mirroring", ("복도 끝 거울.", "The mirror at the end."), ("지나가는 걸 그대로 비춰 보여줘요. 사람을 멈춰 세우진 않아요.", "Shows a copy of everything passing, without stopping anyone.")),
        ("에이전트리스", "Agentless", ("방에 안 들어감.", "Never enters a room."), ('그래서 <a href="edr-ko.html">개</a>를 못 앉히는 방도 지켜요.', 'Which is why it covers rooms the <a href="edr-en.html">dog</a> can\'t.')),
        ("횡적 이동", "Lateral movement", ("방에서 방으로 옮겨 다니기.", "Room to room."), ("프린터 방에서 나온 사람이 금고 방으로. 복도에서 제일 잘 보여요.", "Someone leaving the printer room for the vault. Best seen from the hallway.")),
        ("유출", "Exfiltration", ("큰 가방 들고 나가기.", "Walking out with a huge bag."), ("새벽에, 성문으로, 아주 크게.", "At night, toward the gate, very big.")),
        ("암호화", "Encryption", ("봉해진 상자.", "The sealed box."), ("안은 못 봐요. 크기·방향·시간은 봐요.", "Contents hidden; size, direction and time still visible.")),
    ],
}
