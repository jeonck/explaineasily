from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
DOORS = (("⟦부엌|Kitchen⟧", False), ("⟦창구|Counter⟧", False), ("⟦금고|Vault⟧", False), ("⟦우편함|Mailbox⟧", False), ("⟦서재|Study⟧", False))


def notebook(x, y, lines, s=1.0, torn=False, empty=False):
    rows = "".join(label(8, 20 + i * 15, t, 10, "#142033", "start") for i, t in enumerate(lines))
    if empty:
        rows = label(55, 30, "⟦(비어 있음)|(empty)⟧", 10, "var(--muted)")
    tear = '<path d="M0 0 l10 8 l-8 8 l10 8 l-8 8 l10 8 l-8 8" stroke="var(--bad-soft)" stroke-width="5" fill="none" transform="translate(100,0)"/>' if torn else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="110" height="{14 + max(len(lines), 2) * 15}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect width="110" height="8" rx="3" fill="#C9A86A"/>{rows}{tear}</g>')


PEN = '<g transform="translate(66,70) rotate(-30)"><rect x="-3" y="-18" width="6" height="30" rx="2" fill="#5B8DEF"/><path d="M-3 12 L0 20 L3 12 Z" fill="#142033"/></g>'

# 1. 일은 그냥 지나간다
P1 = svg(300, corridor(300, DOORS, marks=False)
         + person(452, 150, s=0.8, **ME) + '<rect x="420" y="80" width="30" height="110" rx="3" fill="var(--sky)"/>'
         + label(452, 275, "⟦문이 열렸다 닫혔어요. 아무도 안 적었어요|a door opened and closed; nobody wrote it down⟧", 13, "#F5E6B8"))

# 2. 사고가 나면 물어볼 데가 없다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + '<g transform="translate(160,140)"><rect x="-70" y="-90" width="140" height="180" rx="8" fill="var(--night)"/><rect x="-50" y="-70" width="100" height="140" rx="4" fill="#0A1120"/>' + label(0, 6, "⟦텅|empty⟧", 26, "var(--bad)", cls="d") + "</g>"
         + label(160, 255, "⟦금고 방|the vault⟧", 12, "var(--muted)")
         + person(330, 80, s=0.9, face=FROWN + SWEAT, **GUARD)
         + bubble(280, 10, 260, 34, "⟦어젯밤 여기 누가 들어갔어요?|who was in here last night?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + "".join(person(x, 120, s=0.65, hat=h, shirt="#4A5A72", face=FROWN) + label(x + 20, 210, "?", 22, "var(--bad)", cls="d") for x, h in ((480, "#E9B44C"), (560, None), (640, "var(--stone-dark)")))
         + label(560, 262, "⟦아무도 몰라요|nobody knows⟧", 13, "var(--bad)"))

# 3. 로그 = 성 곳곳이 남기는 한 줄 기록 (hero)
NOTES = (notebook(62, 200, ("⟦02:05 불 켜짐|02:05 light on⟧", "⟦02:06 냉장고 열림|02:06 fridge opened⟧"), 0.85)
         + notebook(202, 200, ("⟦14:02 지민 쪽지|14:02 note from Jimin⟧", "⟦14:03 사과 2 · 성공|14:03 apples 2 · ok⟧"), 0.85)
         + notebook(342, 200, ("⟦02:10 문 열림|02:10 door opened⟧", "⟦02:10 열쇠: 지민|02:10 key: Jimin⟧", "⟦02:14 문 닫힘|02:14 door closed⟧"), 0.85)
         + notebook(482, 200, ("⟦01:40 편지 도착|01:40 letter arrived⟧", "⟦01:41 보낸이: ?|01:41 from: ?⟧"), 0.85)
         + notebook(622, 200, ("⟦09:00 문 열림|09:00 door opened⟧", "⟦09:00 열쇠: 태오|09:00 key: Taeo⟧"), 0.85))
P3 = svg(340, corridor(340, DOORS, marks=False) + NOTES
         + person(30, 40, s=0.6, face=EYES, **GUARD, extra=PEN)
         + label(380, 322, "⟦언제, 누가, 어디서, 뭘 했는지 — 문마다, 창구마다, 물건마다 한 줄씩|when, who, where, what — one line at every door, counter and thing⟧", 12, "#F5E6B8"))

# 4. 모아서 시간순으로 읽으면 이야기가 된다
SCREEN = ('<rect x="60" y="50" width="420" height="200" rx="10" fill="var(--night)"/>'
          + "".join(label(80, 84 + i * 30, t, 13, c, "start") for i, (t, c) in enumerate((("⟦01:40 우편함 · 편지 도착 · 보낸이 ?|01:40 mailbox · letter · from ?⟧", "#C9D5E6"), ("⟦02:05 부엌 · 불 켜짐|02:05 kitchen · light on⟧", "#C9D5E6"), ("⟦02:10 금고 · 문 열림 · 열쇠 지민|02:10 vault · door opened · key Jimin⟧", "var(--accent)"), ("⟦02:14 금고 · 문 닫힘|02:14 vault · door closed⟧", "var(--accent)"), ("⟦02:20 성문 · 나감 · 큰 가방|02:20 gate · out · big bag⟧", "var(--bad)"))))
          + '<rect x="250" y="250" width="40" height="12" fill="var(--stone-dark)"/>')
P4 = svg(320, sky(320) + SCREEN
         + '<path d="M540 150 C580 120 620 180 660 150" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>' + person(640, 60, s=0.7, face=MASK, extra='<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/>')
         + label(660, 200, "⟦도둑의 발자취|the thief\'s trail⟧", 13, "var(--bad)", cls="d")
         + '<g transform="translate(560,250)"><rect x="-40" y="-16" width="80" height="32" rx="4" fill="#8B5E3C"/><rect x="-30" y="-8" width="60" height="16" fill="#5A3B22"/></g>' + label(640, 256, "⟦몇 달치는 서랍에|months in a drawer⟧", 11, "var(--muted)")
         + label(380, 300, "⟦따로 보면 한 줄, 모아 보면 이야기|one line alone, a story together⟧", 13, "var(--muted)"))

# 5. 안 적으면 없고, 도둑은 찢고, 너무 많으면 못 읽는다
P5 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + f'<g transform="translate(70,60) scale(0.7)"><rect x="-30" width="60" height="100" rx="3" fill="{WOOD}"/><circle cx="20" cy="54" r="4" fill="#E9B44C"/></g>' + notebook(110, 60, (), 0.8, empty=True)
         + label(130, 190, "⟦적기로 안 정한 문|a door nobody set to write⟧", 12, "var(--ink)") + label(130, 210, "⟦→ 기록이 없어요|→ no record at all⟧", 11, "var(--muted)")
         + person(300, 60, s=0.8, face=MASK) + notebook(370, 70, ("⟦02:10 금고 문|02:10 vault⟧", "⟦…|…⟧"), 0.8, torn=True) + '<path d="M410 60 l40 50 M450 60 l-40 50" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + label(390, 190, "⟦도둑은 제일 먼저 일지를 찢어요|the thief tears the diary first⟧", 12, "var(--ink)") + label(390, 210, "⟦→ 복사본을 멀리 보내요|→ send a copy far away⟧", 11, "var(--muted)")
         + "".join(notebook(560 + (i % 3) * 22, 40 + (i // 3) * 26 + (i % 3) * 6, ("", ""), 0.5) for i in range(9))
         + person(690, 110, s=0.7, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + label(640, 190, "⟦하루에 수천 장|thousands a day⟧", 12, "var(--ink)") + label(640, 210, "⟦→ 사람은 못 읽어요|→ no person can read them⟧", 11, "var(--muted)")
         + label(380, 295, "⟦그래서 큰 화면이 대신 읽어요|which is why the big screen reads them instead⟧", 13, "var(--muted)"))

WHEN_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 18 V32 L42 38" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
WHO_I = icon(f'<circle cx="32" cy="22" r="10" fill="{SKIN}"/><path d="M20 18 Q32 4 44 18 Z" fill="var(--good)"/><rect x="18" y="34" width="28" height="22" rx="8" fill="var(--good)"/>')
WHAT_I = icon(f'<rect x="20" y="8" width="24" height="48" rx="2" fill="{WOOD}"/><rect x="20" y="8" width="8" height="48" fill="var(--sky)"/><circle cx="38" cy="34" r="3" fill="#E9B44C"/>')
OK_I = icon('<circle cx="20" cy="32" r="10" fill="var(--good)"/><path d="M15 32 l4 4 l7 -8" stroke="#FFF" stroke-width="2.5" fill="none"/><circle cx="44" cy="32" r="10" fill="var(--bad)"/><path d="M40 28 l8 8 M48 28 l-8 8" stroke="#FFF" stroke-width="2.5"/>')

PAGE = {
    "slug": "log", "order": 8.5,
    "title": ("성 곳곳의 한 줄 일지", "The One-Line Diary Everywhere"),
    "h1": ("<em>로그</em>가 뭐예요?", "What is a <em>Log</em>?"),
    "sub": ("로그(Log)를 성 곳곳이 남기는 한 줄짜리 일지 이야기로 풀어봤어요.",
            "Logs, told as a story about the one-line diary kept at every door in the castle."),
    "panels": [
        {"svg": P1, "alt": ("복도의 금고 문이 열려 있고 사람이 서 있지만 아무 기록도 없음", "The vault door in the hallway stands open with someone beside it, and nothing is written anywhere"),
         "caption": ("성에서 일어나는 일은 그냥 지나가요.", "Things happen in the castle and just pass."),
         "small": ("누가 언제 문을 열었는지, 지나고 나면 아무도 몰라요.", "Who opened which door, and when — once it's over, nobody knows.")},
        {"svg": P2, "alt": ("텅 빈 금고 방 앞에서 경비가 '어젯밤 여기 누가 들어갔어요?' 묻고, 세 사람 위에 물음표", "Beside an empty vault a guard asks who was in here last night?; question marks hang over three people"),
         "caption": ("사고가 나면 물어볼 데가 없어요.", "When something goes wrong, there's nobody to ask."),
         "small": ('"어젯밤 금고 방에 누가 들어갔어요?" — 아무도 몰라요.', '"Who was in the vault last night?" — nobody knows.')},
        {"svg": P3, "hero": True, "alt": ("복도의 문마다 작은 일지: 02:05 불 켜짐, 14:02 지민 쪽지, 02:10 금고 문 열림 열쇠 지민, 01:40 편지 도착… 위에 펜을 든 경비", "A small diary at every door in the hallway: 02:05 light on, 14:02 note from Jimin, 02:10 vault door opened key Jimin, 01:40 letter arrived… a guard with a pen above"),
         "caption": ("로그는 성 곳곳이 남기는 한 줄 기록이에요.", "A log is the one-line record kept all over the castle."),
         "small": ("'언제, 누가, 어디서, 뭘 했는지' — 한 줄씩. 문마다, 창구마다, 물건마다.", "'When, who, where, what' — one line at a time. Every door, every counter, every thing."),
         "tricks": (4, [
             (WHEN_I, ("언제", "When"), ("시계가 맞아야 해요", "the clocks must agree"), "warm"),
             (WHO_I, ("누가", "Who"), ("사람, 또는 물건", "a person, or a thing"), "calm"),
             (WHAT_I, ("뭘 했나", "What"), ("문 열림, 쪽지, 편지", "door opened, note, letter")),
             (OK_I, ("잘 됐나", "Did it work"), ("성공인지 실패인지", "success or failure"), "calm"),
         ])},
        {"svg": P4, "alt": ("큰 화면에 01:40 편지 → 02:05 부엌 → 02:10 금고 → 02:20 성문·큰 가방 순서로 줄이 서고, 도둑의 발자취가 드러남. 옆에 서랍", "On a big screen the lines queue up — 01:40 letter → 02:05 kitchen → 02:10 vault → 02:20 gate, big bag — revealing the thief's trail; a drawer beside"),
         "caption": ("쪽지를 모아 시간순으로 읽으면 이야기가 돼요.", "Gather the lines in time order, and they become a story."),
         "small": ('따로 보면 한 줄, 모아 보면 도둑의 발자취. <a href="siem-ko.html">큰 화면</a>이 모아 줄 세워요. 몇 달치는 서랍에 둬요.',
                   'Alone, one line; together, the thief\'s trail. The <a href="siem-en.html">big screen</a> gathers and lines them up. Months of them go in a drawer.')},
        {"svg": P5, "alt": ("빈 일지가 달린 문, 도둑이 찢는 일지, 산더미 일지 앞에서 땀 흘리는 사람", "A door with an empty diary, a thief tearing a diary, and someone sweating in front of a mountain of diaries"),
         "caption": ("안 적으면 없고, 도둑은 찢고, 너무 많으면 못 읽어요.", "Unwritten lines don't exist, thieves tear pages, and too many can't be read."),
         "small": ('적기로 정해야 적혀요. 도둑은 제일 먼저 일지를 찢어요 — 그래서 복사본을 멀리 보내요. 그리고 하루에 수천 장이면 사람은 못 읽어요 — <a href="soc-ko.html">경비실</a>의 큰 화면이 대신 읽어요.',
                   'A door writes only if it\'s told to. Thieves tear the diary first — so a copy goes far away. And thousands a day are beyond any person — the <a href="soc-en.html">guard room</a>\'s big screen reads them instead.')},
    ],
    "summary": (("<b>로그</b> = 성 곳곳이 남기는 '언제, 누가, 어디서, 뭘 했나' <b>한 줄 기록</b>. 모아서 시간순으로 읽으면 <b>이야기</b>가 돼요.",
                 "A <b>log</b> = the <b>one-line record</b> — when, who, where, what — kept all over the castle. Gathered in time order, it becomes a <b>story</b>."),
                ("Log. 사고 조사의 첫 번째 재료예요. 할 일은 넷 — 적기(설정), 모으기(SIEM), 지키기(멀리 보내기), 오래 두기(보관). 시계를 맞추는 것부터.",
                 "The first ingredient of any investigation. Four jobs: write it (configure), gather it (SIEM), protect it (send it away), keep it (retention). Start by setting the clocks.")),
    "glossary": [
        ("이벤트", "Event", ("한 줄.", "One line."), ("일어난 일 하나. 문이 열렸다, 편지가 왔다.", "One thing that happened: a door opened, a letter came.")),
        ("타임스탬프", "Timestamp", ("언제.", "When."), ("성 안 시계가 다 맞아야 줄을 세울 수 있어요(NTP).", "Every clock in the castle must agree, or nothing lines up (NTP).")),
        ("소스", "Source", ("어디서.", "Where."), ("어느 문, 어느 창구, 어느 물건이 적었나.", "Which door, which counter, which thing wrote it.")),
        ("감사 로그", "Audit log", ("누가 뭘 바꿨나.", "Who changed what."), ('열쇠를 가져갔다, 모자를 바꿨다. → <a href="pam-ko.html">열쇠 대장</a>', 'Took a key, swapped a hat. → <a href="pam-en.html">the key ledger</a>')),
        ("접근 로그", "Access log", ("창구에 온 손님 명단.", "The list of counter visitors."), ('누가 언제 어떤 쪽지를 넣었나. → <a href="waf-ko.html">창구 앞 쪽지 검토원</a>', 'Who handed in which note, when. → <a href="waf-en.html">the note checker</a>')),
        ("로그 전달", "Log forwarding", ("복사본 멀리 보내기.", "Sending a copy far away."), ('도둑이 찢어도 복사본은 남아요. → <a href="siem-ko.html">경비실의 큰 화면</a>', 'Tear the diary and the copy survives. → <a href="siem-en.html">the big screen</a>')),
        ("보관 기간", "Retention", ("서랍에 몇 달.", "Months in the drawer."), ('발자국을 나중에 찾으려면 오래 둬야 해요. → <a href="backup-ko.html">멀리 둔 여분 상자</a>', 'To find footprints later, keep them a long while. → <a href="backup-en.html">the spare chest</a>')),
        ("로그 변조", "Log tampering", ("일지 찢기.", "Tearing the diary."), ("도둑이 자기 줄만 지우는 것. 복사본과 도장(해시)으로 막아요.", "A thief erasing only their own lines. Copies and stamps (hashes) prevent it.")),
    ],
}
