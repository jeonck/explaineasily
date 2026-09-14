from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
CARPENTER = dict(hat=WOOD, shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
HAMMER = '<g transform="translate(62,80) rotate(-30)"><rect x="-3" y="-14" width="6" height="36" fill="#8B5E3C"/><rect x="-13" y="-22" width="26" height="12" rx="3" fill="var(--stone-dark)"/></g>'


def poster(x, y, hat="var(--bad)", s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-34" width="48" height="64" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<circle cx="-24" cy="-34" r="3" fill="var(--stone-dark)"/><circle cx="24" cy="-34" r="3" fill="var(--stone-dark)"/>'
            f'{label(0, -22, "⟦수배|WANTED⟧", 9, "var(--bad)")}<circle cy="-2" r="12" fill="{SKIN}"/><path d="M-13 -6 Q0 -22 13 -6 Z" fill="{hat}"/><path d="M-8 -2 h16 v5 h-16z" fill="#111C30"/>'
            f'<rect x="-16" y="14" width="32" height="3" fill="#C9A86A"/><rect x="-12" y="20" width="24" height="3" fill="#C9A86A"/></g>')


def board(x, y, w, h, title, rows, extra=""):
    """명단 판. rows = (모자색, 이름) 튜플. 이름은 y+70 부터 32px 간격."""
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="8" fill="#C9A86A"/>{label(x + w / 2, y + 20, title, 12, "#142033", cls="d")}')
    for i, (hat, name) in enumerate(rows):
        ry = y + 62 + i * 32
        out += f'<circle cx="{x + 26}" cy="{ry}" r="9" fill="{SKIN}"/><path d="M{x + 16} {ry - 3} Q{x + 26} {ry - 16} {x + 36} {ry - 3} Z" fill="{hat}"/>' + label(x + 46, ry + 4, name, 12, "#142033", "start")
    return out + extra


def mark(x, y, ok=True):
    return (label(x, y, "✓", 24, "var(--good)", cls="d") if ok else label(x, y, "×", 22, "var(--bad)", cls="d"))


def door(x, y, s=1.0, tag=None):
    t = (f'<rect x="8" y="30" width="48" height="22" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{label(32, 45, tag, 9, "#142033", cls="d")}' if tag else "")
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="64" height="110" rx="3" fill="{WOOD}"/><circle cx="52" cy="70" r="4" fill="#E9B44C"/>{t}</g>'


def letter(x, y, text, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'{label(70, 34, text, 14, "#142033", cls="d")}<rect x="16" y="52" width="70" height="4" rx="2" fill="#C9A86A"/></g>')


# 1. 수배 전단은 아는 도둑만 막아요
P1 = svg(300, sky(300) + gate(380, 60)
         + person(460, 130, s=0.75, face=EYES, **GUARD) + poster(548, 150, s=0.9)
         + bubble(560, 40, 190, 34, "⟦전단이랑 같은 얼굴만 막아요|I only stop faces on the poster⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(120, 130, s=0.75, face=MASK) + mark(146, 122, False) + label(146, 240, "⟦전단에 있음 → 막힘|on the poster → stopped⟧", 10, "var(--muted)")
         + person(240, 130, s=0.75, face=MASK, hat="#7B3FA0") + label(266, 120, "?", 24, "var(--accent)", cls="d") + label(266, 240, "⟦전단에 없음 → 통과!|no poster → walks in!⟧", 10, "var(--bad)")
         + label(380, 282, "⟦수배 전단은 아는 도둑만 막아요|a wanted poster only stops thieves we already know⟧", 12, "var(--ink)", cls="d"))

# 2. 새 도둑은 전단에 없어요
HATS = ("var(--bad)", "#7B3FA0", "#2E8B57", "#C9822B", "#5B8DEF", "#8B5E3C")
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(120, 100, s=0.85, face=FROWN, extra=SWEAT, **GUARD)
         + "".join(poster(260 + (i % 3) * 60, 80 + (i // 3) * 80, HATS[i], 0.8) for i in range(6))
         + label(320, 240, "⟦전단은 늘 한 발 늦어요|posters are always one step behind⟧", 11, "var(--muted)")
         + person(520, 110, s=0.8, face=MASK, hat="#3A8F6E")
         + bubble(470, 30, 220, 34, "⟦나는 아직 전단에 없지롱|no poster of me yet!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(548, 225, "⟦오늘 처음 온 도둑|a thief seen for the first time today⟧", 10, "var(--bad)")
         + label(380, 282, "⟦모르는 도둑은 못 막아요 — 아는 것만 막는 건 늘 늦어요|an unknown thief gets through — stopping only what you know is always late⟧", 12, "var(--ink)", cls="d"))

# 3. 명단에 있는 사람만 (hero)
LIST = ((WOOD, "⟦목수|the carpenter⟧"), ("#E07A5F", "⟦빵집 아줌마|the baker⟧"), ("#5B8DEF", "⟦파란 모자 친구|the blue-hat friend⟧"), ("var(--stone-dark)", "⟦심부름꾼|the errand boy⟧"))
P3 = svg(360, sky(360)
         + board(40, 40, 230, 210, "⟦들어와도 되는 사람|WHO MAY ENTER⟧", LIST, label(155, 238, "⟦명단 밖은 전부 안 돼요|everyone else: no⟧", 10, "var(--bad)"))
         + gate(420, 60) + person(500, 120, s=0.75, face=EYES, **GUARD)
         + bubble(470, 20, 200, 34, "⟦명단에 있어요? 없으면 안 돼요|on the list? if not, no⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(300, 150, s=0.7, face=SMILE, extra=HAMMER, **CARPENTER) + mark(325, 142) + label(325, 245, "⟦명단에 있음 → 통과|on the list → in⟧", 10, "var(--good)")
         + person(600, 140, s=0.7, face=MASK, hat="#3A8F6E") + mark(625, 130, False)
         + person(680, 150, s=0.65, face=MASK, hat="#7B3FA0") + mark(703, 140, False)
         + label(660, 245, "⟦명단에 없음 → 전부 막힘|not on the list → all stopped⟧", 10, "var(--bad)")
         + label(380, 340, "⟦아는 도둑을 막는 게 아니라, 아는 사람만 들이는 거예요|not blocking the thieves we know — letting in only the people we know⟧", 13, "var(--ink)", cls="d"))

# 4. 명단 관리가 일이에요
P4 = svg(320, sky(320)
         + person(80, 120, s=0.8, face=FROWN, extra=HAMMER, **CARPENTER) + label(108, 105, "⟦명단에 없어요|not on the list yet⟧", 10, "var(--bad)") + label(108, 235, "⟦새로 온 목수|the new carpenter⟧", 11, "var(--muted)")
         + gate(230, 60, 0.9) + person(300, 140, s=0.75, face=EYES, **GUARD)
         + bubble(240, 20, 220, 34, "⟦이름이 없네요, 잠깐만요|your name isn\'t here, one moment⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(410, 150, s=0.7, face=SMILE, **CLERK)
         + board(480, 60, 240, 180, "⟦들어와도 되는 사람|WHO MAY ENTER⟧", LIST[:3],
                 label(526, 218, "⟦+ 새 목수|+ new carpenter⟧", 12, "var(--accent)", "start", cls="d") + '<path d="M640 226 l14 -14 l6 6 l-14 14z" fill="var(--accent)"/><path d="M654 212 l6 6" stroke="#5A3B22" stroke-width="3"/>')
         + label(600, 268, "⟦매일 조금씩 — 관리가 일이에요|a little every day — the list is work⟧", 11, "var(--accent)")
         + label(380, 302, "⟦안전한 만큼 손이 가요 — 이름을 안 적으면 친구도 못 들어와요|as safe as it is fiddly — forget to write a name and even a friend is locked out⟧", 12, "var(--ink)", cls="d"))

# 5. 성 곳곳의 명단
TOOLS = (("⟦망치|hammer⟧", True), ("⟦톱|saw⟧", True), ("⟦이상한 상자|strange box⟧", False))
P5 = svg(300, sky(300)
         + label(126, 40, "⟦돌려도 되는 도구|tools we may run⟧", 12, "var(--ink)", cls="d")
         + '<rect x="40" y="55" width="172" height="150" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + "".join(label(60, 92 + i * 38, t, 12, "#142033", "start") + mark(185, 96 + i * 38, ok) for i, (t, ok) in enumerate(TOOLS))
         + label(126, 232, "⟦성 안 도구 목록|the castle\'s tool list⟧", 10, "var(--muted)")
         + '<path d="M253 30 V250 M506 30 V250" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 8"/>'
         + label(380, 40, "⟦받는 편지 주소|senders we accept⟧", 12, "var(--ink)", cls="d")
         + letter(300, 62, "⟦동쪽 마을에서|from east village⟧", 0.55) + mark(395, 92)
         + letter(300, 122, "⟦서쪽 마을에서|from west village⟧", 0.55) + mark(395, 152)
         + letter(300, 182, "⟦???|???⟧", 0.55) + mark(395, 210, False)
         + label(380, 250, "⟦주소 목록에 없으면 안 받아요|not on the address list → refused⟧", 10, "var(--muted)")
         + label(633, 40, "⟦방 이름표|name tags on doors⟧", 12, "var(--ink)", cls="d")
         + door(600, 70, 1.0, tag="⟦목수만|carpenter⟧") + person(680, 120, s=0.6, face=SMILE, **CARPENTER)
         + label(633, 232, "⟦이름표 맞는 사람만 방에|only a matching tag gets in⟧", 10, "var(--muted)")
         + label(380, 285, "⟦명단은 성 곳곳에 있어요 — 문마다 물어보는 성의 기본이에요|lists are all over the castle — the base of a castle that asks at every door⟧", 11, "var(--ink)"))

LIST_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="10" rx="4" fill="#C9A86A"/><circle cx="21" cy="28" r="3" fill="var(--good)"/><circle cx="21" cy="38" r="3" fill="#5B8DEF"/><circle cx="21" cy="48" r="3" fill="#E07A5F"/><path d="M28 28 h16 M28 38 h16 M28 48 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
DENY_I = icon('<circle cx="32" cy="32" r="22" fill="var(--bad)"/><rect x="16" y="28" width="32" height="8" rx="3" fill="#FFF"/>')
UNKNOWN_I = icon(f'<circle cx="26" cy="30" r="16" fill="{SKIN}"/><path d="M10 26 Q26 4 42 26 Z" fill="#3A8F6E"/><rect x="14" y="26" width="24" height="7" fill="#111C30"/><rect x="14" y="46" width="24" height="14" rx="4" fill="#2E3D57"/><path d="M48 14 l10 10 M58 14 l-10 10" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
PEN_I = icon('<rect x="10" y="12" width="36" height="42" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 24 h18 M18 34 h18" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M18 44 h10" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/><path d="M34 52 l20 -20 l6 6 l-20 20z" fill="var(--accent)"/><path d="M54 32 l6 6" stroke="#5A3B22" stroke-width="3"/>')

PAGE = {
    "slug": "allowlist", "order": 99,
    "title": ("명단에 있는 사람만", "Only the Names on the List"),
    "h1": ("<em>허용 목록</em>이 뭐예요?", "What is an <em>Allowlist</em>?"),
    "sub": ("허용 목록(Allowlist)과 차단 목록(Blocklist)을 수배 전단 대신 들어와도 되는 사람 명단을 성문에 붙이는 이야기로 풀어봤어요.",
            "Allowlists and blocklists, told as a story about pinning a list of who may enter on the castle gate instead of wanted posters."),
    "panels": [
        {"svg": P1, "alt": ("성문 앞 경비가 수배 전단을 들고 있다. 전단과 같은 빨간 모자 도둑은 X, 보라 모자 도둑은 물음표 — 전단에 없으니 통과", "A guard at the gate holds a wanted poster. The red-hat thief matching it gets an X; the purple-hat thief gets a question mark — no poster, so he walks in"),
         "caption": ("수배 전단은 아는 도둑만 막아요.", "A wanted poster only stops thieves we already know."),
         "small": ('경비는 <a href="idsips-ko.html">전단이랑 같은 얼굴</a>만 막아요. 전단에 없는 도둑은 그냥 들어가요.',
                   'The guard only stops <a href="idsips-en.html">faces on the poster</a>. A thief with no poster simply walks in.')},
        {"svg": P2, "alt": ("땀 흘리는 경비 옆에 모자 색이 다 다른 수배 전단 여섯 장. 오른쪽에 초록 모자 도둑이 '나는 아직 전단에 없지롱'", "A sweating guard beside six wanted posters, each with a different hat color. On the right a green-hat thief boasts there is no poster of him yet"),
         "caption": ("새 도둑은 전단에 없어요. 전단은 늘 한 발 늦어요.", "A new thief is on no poster. Posters are always one step behind."),
         "small": ("도둑은 매일 새 모자를 써요. 아는 것만 막는 목록은 모르는 도둑 앞에서 늘 늦어요.", "Thieves wear a new hat every day. A list of what you know is always late against what you don\'t.")},
        {"svg": P3, "hero": True, "alt": ("'들어와도 되는 사람' 명단: 목수, 빵집 아줌마, 파란 모자 친구, 심부름꾼. 명단에 있는 목수는 체크, 모자 색이 낯선 두 도둑은 둘 다 X", "A WHO MAY ENTER list: the carpenter, the baker, the blue-hat friend, the errand boy. The carpenter on the list gets a check; two thieves in unfamiliar hats both get an X"),
         "caption": ("허용 목록은 들어와도 되는 사람 명단이에요. 명단 밖은 전부 막아요.", "An allowlist is the list of who may enter. Everyone not on it is stopped."),
         "small": ("경비가 도둑을 알아볼 필요가 없어요. 명단에 있나만 봐요 — 처음 보는 도둑도, 전단 없는 도둑도 전부 막혀요.", "The guard never has to recognize a thief. He only checks the list — a thief seen for the first time, or one with no poster, is stopped all the same."),
         "tricks": (4, [
             (LIST_I, ("명단을 만들어요", "Make the list"), ("들어와도 되는 사람만 적어요", "only the people who may enter"), "calm"),
             (DENY_I, ("기본은 막기", "Default: no"), ("명단에 없으면 전부 안 돼요", "not on the list, not coming in"), "warm"),
             (UNKNOWN_I, ("모르는 도둑도 막혀요", "Unknown thieves too"), ("전단이 없어도요", "no poster needed"), "warm"),
             (PEN_I, ("이름을 넣고 빼요", "Add and remove names"), ("새 목수가 오면 적어요", "a new carpenter gets written in"), "calm"),
         ])},
        {"svg": P4, "alt": ("새로 온 목수가 성문 앞에서 막혀 있다 — 명단에 없어요. 경비가 '잠깐만요', 서기가 명단에 '+ 새 목수'를 연필로 적는다", "A new carpenter is stopped at the gate — not on the list yet. The guard says one moment, and a clerk pencils + new carpenter onto the list"),
         "caption": ("훨씬 안전하지만 명단 관리가 일이에요. 새 목수가 오면 이름을 적어야 해요.", "Far safer, but keeping the list is work. When a new carpenter arrives, someone has to write the name in."),
         "small": ('이름을 안 적으면 친구도 못 들어와요. 그래서 명단을 맡은 사람이 매일 조금씩 고쳐요 — <a href="patch-ko.html">목수</a>가 바뀔 때마다요.',
                   'Forget a name and even a friend is locked out. So someone owns the list and fixes it a little every day — every time the <a href="patch-en.html">carpenter</a> changes.')},
        {"svg": P5, "alt": ("세 장면: 돌려도 되는 도구 목록(망치 체크, 톱 체크, 이상한 상자 X), 받는 편지 주소 목록(동쪽·서쪽 마을은 체크, ???는 X), 방문에 붙은 '목수만' 이름표와 목수", "Three scenes: a tools-we-may-run list (hammer and saw checked, strange box X), a senders-we-accept list (east and west village checked, ??? X), and a door tagged carpenters only beside a carpenter"),
         "caption": ("도구 목록, 편지 주소 목록, 방 이름표 — 성 곳곳에 명단이 있어요.", "A tool list, a sender list, name tags on doors — lists are all over the castle."),
         "small": ('성에서 돌려도 되는 도구, 성문에서 받는 편지 주소, <a href="nac-ko.html">방마다 붙은 이름표</a>. <a href="zerotrust-ko.html">문마다 물어보는 성</a>의 기본이에요.',
                   'Which tools may run in the castle, which senders the gate accepts, <a href="nac-en.html">the name tag on every door</a>. It is the base of the <a href="zerotrust-en.html">castle that asks at every door</a>.')},
    ],
    "summary": (("<b>허용 목록</b> = <b>들어와도 되는 사람 명단</b>. 명단 밖은 전부 막아요. 아는 도둑을 막는 <b>차단 목록</b>보다 훨씬 안전하지만, <b>명단 관리</b>가 일이에요.",
                 "An <b>allowlist</b> = the <b>list of who may enter</b>; everyone else is stopped. Far safer than a <b>blocklist</b> that only stops known thieves — but <b>keeping the list</b> is work."),
                ("Allowlist(화이트리스트)는 허용할 것만 적고 나머지는 기본 거부(default deny)해요. Blocklist(블랙리스트)는 막을 것만 적어 새 위협에 늦어요. 앱 허용 목록, IP 허용 목록, 이메일 발신자 목록 등에 쓰이고, 목록이 낡으면 정상 업무가 막히기 때문에 관리 책임자와 갱신 절차가 필요해요.",
                 "An allowlist (whitelist) names only what is permitted and denies everything else by default. A blocklist (blacklist) names only what to stop, so it is always late against new threats. Used for application allowlisting, IP allowlists and email senders — and because a stale list blocks normal work, it needs an owner and an update process.")),
    "glossary": [
        ("허용 목록", "Allowlist (whitelist)", ("들어와도 되는 명단.", "The list of who may enter."), ("명단에 있는 것만 통과. 나머지는 전부 막아요.", "Only what is on the list passes. Everything else is stopped.")),
        ("차단 목록", "Blocklist (blacklist)", ("수배 전단.", "The wanted poster."), ('아는 도둑만 막아요. 새 도둑엔 늦어요. → <a href="idsips-ko.html">수배 전단 든 파수꾼</a>', 'Stops only known thieves; late against new ones. → <a href="idsips-en.html">the watchman with the wanted poster</a>')),
        ("기본 거부", "Default deny", ("명단에 없으면 안 돼요.", "Not on the list, not coming in."), ("모르는 건 일단 막고 나중에 명단에 넣어요. 반대는 기본 허용이에요.", "The unknown is stopped first and added later. The opposite is default allow.")),
        ("앱 허용 목록", "Application allowlisting", ("돌려도 되는 도구 목록.", "The tools-we-may-run list."), ('성 안에서 돌릴 수 있는 도구만 적어요. 목록에 없는 <a href="malware-ko.html">이상한 상자</a>는 안 돌아가요.', 'Only the tools allowed to run in the castle. A <a href="malware-en.html">strange box</a> not on it never runs.')),
        ("IP 허용 목록", "IP allowlist", ("받는 편지 주소 목록.", "The senders-we-accept list."), ('정해진 마을에서 온 편지만 성문이 받아요. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'The gate accepts letters only from listed villages. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("관리 부담", "Maintenance burden", ("명단 고치는 일.", "The work of fixing the list."), ("새 목수, 떠난 목수, 바뀐 도구 — 안 고치면 친구가 막히고, 대충 고치면 도둑이 들어와요.", "New carpenters, departed ones, changed tools — left alone the list locks out friends; fixed carelessly it lets thieves in.")),
        ("NAC", "NAC (network access control)", ("방마다 붙은 이름표.", "The name tag on every door."), ('복도 구멍마다 명단을 봐요. → <a href="nac-ko.html">복도 구멍마다 문지기</a>', 'A list checked at every hole in the corridor. → <a href="nac-en.html">a doorkeeper at every corridor hole</a>')),
        ("제로 트러스트", "Zero Trust", ("문마다 물어보는 성.", "The castle that asks at every door."), ('허용 목록을 문마다 붙인 성이에요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'A castle with an allowlist on every door. → <a href="zerotrust-en.html">the castle that asks at every door</a>')),
    ],
}
