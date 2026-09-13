from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)


def bug(x, y, s=1.0, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><circle cx="-12" cy="-4" r="8" fill="{color}"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<circle cx="-14" cy="-2" r="2" fill="#FFF"/><circle cx="-8" cy="-2" r="2" fill="#FFF"/></g>')


def crate(x, y, s=1.0, opened=False, inner=""):
    lid = '<rect x="-30" y="-36" width="60" height="10" fill="#8B5E3C" transform="rotate(-25 -30 -26)"/>' if opened else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="44" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-26 -22 L26 22 M26 -22 L-26 22" stroke="#5A3B22" stroke-width="3"/>{lid}{inner}</g>')


def chest(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-12" width="48" height="30" rx="3" fill="#8B5E3C"/><path d="M-24 -12 h48 v-4 a24 10 0 0 0 -48 0z" fill="#5A3B22"/></g>')


def empty_room(x, y, w, h, peephole=True):
    """창문 없는 두꺼운 벽의 빈 방. 문 하나, 작은 구멍 하나."""
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="var(--stone-dark)"/><rect x="{x + 18}" y="{y + 18}" width="{w - 36}" height="{h - 36}" fill="var(--sky)"/>'
           f'<rect x="{x + w / 2 - 22}" y="{y + h - 18}" width="44" height="18" fill="{WOOD}"/>')
    if peephole:
        out += f'<circle cx="{x + w - 9}" cy="{y + h / 2}" r="6" fill="var(--night)"/>'
    return out


# 1. 수상한 상자, 어디서 열까
P1 = svg(300, sky(300) + chest(120, 200, 1.0) + chest(600, 200, 1.0)
         + "".join(person(x, 100, s=0.65, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((60, "#E9B44C"), (200, "#5B8DEF"), (520, None), (660, "var(--good)")))
         + crate(380, 170, 1.3) + label(380, 235, "?", 34, "var(--accent)", cls="d")
         + label(380, 120, "⟦골목에서 온 상자|a box from the alley⟧", 13, "var(--muted)")
         + label(380, 282, "⟦성 한가운데서 열면, 벌레가 나왔을 때 늦어요|open it in the middle of the castle, and a bug is loose before you know⟧", 12, "var(--muted)"))

# 2. 한가운데서 열면 퍼진다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + crate(380, 170, 1.3, opened=True)
         + "".join(bug(x, y, 0.55) for x, y in ((300, 120), (460, 110), (250, 200), (520, 210), (180, 150), (600, 150), (360, 90), (420, 250)))
         + "".join(person(x, 100, s=0.65, hat=h, shirt="#4A5A72", face=FROWN + SWEAT) for x, h in ((60, "#E9B44C"), (660, "var(--good)")))
         + chest(120, 220, 0.9) + chest(620, 220, 0.9)
         + label(380, 282, "⟦상자 하나 열어봤을 뿐인데요|all you did was open one box⟧", 13, "var(--bad)"))

# 3. 샌드박스 = 창문 없는 빈 방 (hero)
P3 = svg(340, sky(340) + empty_room(200, 40, 360, 240)
         + crate(380, 180, 1.2, opened=True) + bug(430, 130, 0.9)
         + '<path d="M450 120 C480 90 520 100 520 140" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4" fill="none"/><path d="M515 125 l8 16 M528 128 l-14 9" stroke="var(--bad)" stroke-width="2"/>'
         + label(380, 90, "⟦진짜 물건은 하나도 없어요|nothing real inside⟧", 12, "var(--muted)")
         + person(600, 110, s=0.85, face=EYES, **GUARD, extra='<g transform="translate(66,70) rotate(-30)"><rect x="-3" y="-18" width="6" height="30" rx="2" fill="#5B8DEF"/><path d="M-3 12 L0 20 L3 12 Z" fill="#142033"/></g>')
         + '<path d="M551 160 L590 160" stroke="var(--good)" stroke-width="2" stroke-dasharray="3 3"/>' + label(640, 250, "⟦구멍으로 지켜봐요|watching through the peephole⟧", 12, "var(--muted)")
         + "".join(person(x, 200, s=0.5, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((40, "#E9B44C"), (110, None)))
         + label(90, 300, "⟦성 사람들은 멀쩡해요|the castle folk are fine⟧", 11, "var(--muted)")
         + label(380, 322, "⟦벌레가 튀어나와도 그 방에서 끝이에요|even if a bug jumps out, it ends in that room⟧", 13, "var(--muted)"))

# 4. 검문소도, 경비실도, 도구도 이 방을 쓴다
MINI_ROOM = lambda x, y, s=0.5: (f'<g transform="translate({x},{y}) scale({s})">{empty_room(-80, -60, 160, 120, peephole=False)}</g>')
P4 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + gatehouse(120, 60, 0.6) + label(120, 140, "⟦검문소|checkpoint⟧", 12, "var(--ink)", cls="d") + MINI_ROOM(120, 200) + crate(120, 200, 0.45) + label(120, 260, "⟦받은 상자를 먼저 열어봐요|opens incoming boxes first⟧", 11, "var(--muted)")
         + '<g transform="translate(380,80)"><rect x="-50" y="-40" width="100" height="70" rx="6" fill="var(--night)"/><rect x="-42" y="-32" width="84" height="46" fill="var(--bad)"/>' + label(0, -4, "⟦경비실|guard room⟧", 12, "#FFF") + "</g>"
         + MINI_ROOM(380, 200) + bug(380, 200, 0.5) + label(380, 260, "⟦잡은 벌레를 분석해요|studies bugs it caught⟧", 11, "var(--muted)")
         + '<g transform="translate(640,70)"><rect x="-40" y="-30" width="80" height="60" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><rect x="-32" y="-22" width="64" height="8" fill="var(--line)"/><rect x="-32" y="-8" width="40" height="4" fill="var(--line)"/><rect x="-32" y="2" width="52" height="4" fill="var(--line)"/></g>' + label(640, 140, "⟦그림책 도구|the page-reader⟧", 12, "var(--ink)", cls="d")
         + MINI_ROOM(610, 200, 0.4) + MINI_ROOM(670, 200, 0.4) + label(640, 260, "⟦페이지마다 제 모래밭에서|every page in its own sandpit⟧", 11, "var(--muted)")
         + label(380, 300, "⟦모두 같은 생각이에요 — 먼저 빈 방에서|all the same idea — the empty room first⟧", 13, "var(--muted)"))

# 5. 영리한 벌레는 빈 방인 걸 알아챈다
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--sky)"/>'
         + empty_room(40, 40, 300, 200) + crate(150, 170, 0.9, opened=True) + bug(220, 150, 0.8)
         + bubble(150, 60, 190, 34, "⟦창문도 사람도 없네…|no window, no people…⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + '<path d="M250 185 l14 0" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
         + label(190, 270, "⟦얌전히 있다가 진짜 방에서 움직여요|plays dead, then acts in a real room⟧", 12, "var(--bad)")
         + label(190, 295, "⟦시계를 보고, 마우스를 기다려요|checks the clock, waits for a mouse⟧", 11, "var(--muted)")
         + empty_room(420, 40, 200, 200) + '<path d="M620 100 l6 14 l-8 12 l10 16" stroke="#0A1120" stroke-width="4" fill="none" stroke-linecap="round"/>' + bug(650, 150, 0.7) + label(660, 200, "⟦벽 틈으로|through a crack⟧", 11, "var(--bad)")
         + dog(690, 260, 0.6, bark=True)
         + label(570, 295, "⟦그래서 경비견이 진짜 방에서도 봐요|so the dog keeps watching in real rooms too⟧", 12, "var(--muted)"))

ROOM_I = icon('<rect x="8" y="10" width="48" height="44" fill="var(--stone-dark)"/><rect x="16" y="18" width="32" height="28" fill="var(--sky)"/><rect x="26" y="46" width="12" height="8" fill="#8B5E3C"/>')
NOWIN_I = icon('<rect x="14" y="14" width="36" height="36" fill="var(--stone-dark)"/><path d="M22 22 l20 20 M42 22 l-20 20" stroke="var(--bad)" stroke-width="3"/>')
PEEP_I = icon('<rect x="8" y="10" width="48" height="44" fill="var(--stone-dark)"/><circle cx="46" cy="32" r="5" fill="var(--night)"/><path d="M6 32 Q32 8 58 32" fill="none" stroke="var(--good)" stroke-width="0"/><circle cx="46" cy="32" r="2" fill="var(--good)"/>')
CLEAN_I = icon('<rect x="10" y="12" width="44" height="40" fill="var(--stone-dark)"/><rect x="18" y="20" width="28" height="24" fill="var(--sky)"/><path d="M30 8 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z" fill="#FFD166"/>')

PAGE = {
    "slug": "sandbox", "order": 47,
    "title": ("창문 없는 빈 방", "The Empty Room with No Windows"),
    "h1": ("<em>샌드박스</em>가 뭐예요?", "What is a <em>Sandbox</em>?"),
    "sub": ("샌드박스(Sandbox)를 수상한 상자를 먼저 열어보는 창문 없는 빈 방 이야기로 풀어봤어요.",
            "Sandboxes, told as a story about the windowless empty room where suspicious boxes get opened first."),
    "panels": [
        {"svg": P1, "alt": ("사람들과 상자들이 있는 성 한가운데 골목에서 온 수상한 상자와 물음표", "A suspicious box from the alley sits in the middle of the castle, among people and chests, with a question mark"),
         "caption": ("수상한 상자가 왔어요. 어디서 열까요?", "A suspicious box arrived. Where do you open it?"),
         "small": ('<a href="swg-ko.html">골목에서 온 상자</a>예요. 성 한가운데서 열면, 벌레가 나왔을 때 늦어요.',
                   'It\'s a box from the <a href="swg-en.html">alley</a>. Open it in the middle of the castle, and a bug is loose before you know.')},
        {"svg": P2, "alt": ("열린 상자에서 벌레들이 사방으로 퍼지고 사람들이 땀을 흘림", "Bugs pour out of the opened box in every direction while people sweat"),
         "caption": ("한가운데서 열면 벌레가 온 성에 퍼져요.", "Open it in the middle, and the bugs spread through the castle."),
         "small": ("상자 하나 열어봤을 뿐인데요.", "All you did was open one box.")},
        {"svg": P3, "hero": True, "alt": ("두꺼운 벽에 창문 없는 빈 방 안에서 상자가 열리고 벌레가 튀어나오지만 방 안에 갇힘. 경비가 작은 구멍으로 지켜보며 적고, 성 사람들은 밖에서 멀쩡함", "Inside a thick-walled windowless room the box opens and a bug jumps out but stays trapped; a guard watches through a peephole and writes; castle folk outside are fine"),
         "caption": ("샌드박스는 상자를 먼저 열어보는 창문 없는 빈 방이에요.", "A sandbox is the windowless empty room where boxes get opened first."),
         "small": ("벌레가 튀어나와도 그 방에서 끝이에요. 뭘 하는지 구멍으로 지켜봐요.", "Even if a bug jumps out, it ends in that room. You watch what it does through the peephole."),
         "tricks": (4, [
             (ROOM_I, ("빈 방", "The empty room"), ("진짜 물건은 없어요", "nothing real inside"), "calm"),
             (NOWIN_I, ("창문 없음", "No windows"), ("밖으로 못 나가요", "nothing gets out")),
             (PEEP_I, ("구멍으로 보기", "The peephole"), ("행동을 적어요", "the behavior gets written down"), "calm"),
             (CLEAN_I, ("매번 새 방", "A fresh room each time"), ("다 보면 방을 통째로 새로", "seen it? the room is rebuilt"), "warm"),
         ])},
        {"svg": P4, "alt": ("검문소 아래 빈 방과 상자, 경비실 아래 빈 방과 벌레, 그림책 도구 아래 작은 빈 방 두 개", "An empty room with a box under the checkpoint, one with a bug under the guard room, and two tiny rooms under the page-reader"),
         "caption": ("검문소도, 경비실도, 도구도 이 방을 써요.", "The checkpoint, the guard room and the tools all use this room."),
         "small": ('<a href="swg-ko.html">검문소</a>는 받은 상자를 미리 열어보고, <a href="soc-ko.html">경비실</a>은 잡은 벌레를 분석하고, 그림책 도구(브라우저)는 페이지마다 제 모래밭 안에서 열어요.',
                   'The <a href="swg-en.html">checkpoint</a> opens incoming boxes first, the <a href="soc-en.html">guard room</a> studies bugs it caught, and the page-reader (browser) opens every page in its own sandpit.')},
        {"svg": P5, "alt": ("왼쪽: 빈 방 안의 벌레가 '창문도 사람도 없네…' 하며 얌전히 누움. 오른쪽: 벽 틈으로 빠져나온 벌레와 짖는 경비견", "Left: a bug in the empty room says no window, no people… and lies still. Right: a bug slipping out through a crack, and the dog barking"),
         "caption": ("영리한 벌레는 빈 방인 걸 알아채요.", "A clever bug notices the room is empty."),
         "small": ('"창문이 없네, 사람도 없네" — 얌전히 있다가 진짜 방에서 움직여요. 가끔은 <a href="zeroday-ko.html">벽 틈</a>으로 빠져나오기도 해요. 그래서 <a href="edr-ko.html">경비견</a>이 진짜 방에서도 봐요.',
                   '"No window, no people" — it plays dead, then acts in a real room. Sometimes it slips out through a <a href="zeroday-en.html">crack</a>. So the <a href="edr-en.html">dog</a> keeps watching in real rooms too.')},
    ],
    "summary": (("<b>샌드박스</b> = 수상한 상자를 먼저 열어보는 <b>창문 없는 빈 방</b>. 벌레가 나와도 거기서 끝, 뭘 하는지 지켜봐요.",
                 "A <b>sandbox</b> = the <b>windowless empty room</b> where a suspicious box is opened first. A bug ends there, and you watch what it does."),
                ("Sandbox. 이메일 첨부와 다운로드 검사, 멀웨어 분석실, 브라우저 탭과 휴대폰 앱의 격리가 전부 같은 생각이에요. Cuckoo, ANY.RUN, 그리고 브라우저 안의 샌드박스.",
                 "Checking email attachments and downloads, the malware lab, isolating browser tabs and phone apps — all the same idea. Cuckoo, ANY.RUN, and the sandbox inside your browser.")),
    "glossary": [
        ("격리 실행", "Isolated execution", ("빈 방에서 열기.", "Opening it in the empty room."), ("진짜 성과 이어지지 않은 곳에서 돌려봐요.", "Run it somewhere not connected to the real castle.")),
        ("동적 분석", "Dynamic analysis", ("구멍으로 보기.", "Watching through the peephole."), ('실제로 열어보고 뭘 하는지 적어요. → <a href="malware-ko.html">선물 상자 속 벌레</a>', 'Actually open it and write down what it does. → <a href="malware-en.html">the bug in the gift box</a>')),
        ("디토네이션", "Detonation", ("상자 터뜨려 보기.", "Setting the box off."), ("벌레가 나오게 일부러 열어요.", "Deliberately opening it so the bug comes out.")),
        ("스냅샷 복원", "Snapshot restore", ("매번 새 방.", "A fresh room each time."), ("한 번 쓴 방은 통째로 지우고 새 방으로.", "A used room is wiped and rebuilt.")),
        ("샌드박스 회피", "Sandbox evasion", ("빈 방 알아채기.", "Noticing the room is empty."), ("시계, 마우스, 창문을 확인하고 얌전히 있어요.", "Checks the clock, the mouse, the windows — and plays dead.")),
        ("샌드박스 탈출", "Sandbox escape", ("벽 틈으로 나오기.", "Slipping through a crack."), ('빈 방의 벽에도 틈이 있을 수 있어요. → <a href="zeroday-ko.html">아무도 모르는 구멍</a>', 'Even the empty room\'s wall can have a crack. → <a href="zeroday-en.html">the hole nobody knows about</a>')),
        ("앱 샌드박스", "App sandbox", ("도구마다 제 모래밭.", "A sandpit for every tool."), ("브라우저 탭 하나, 휴대폰 앱 하나가 각자 방 안에서만 놀아요.", "Each browser tab, each phone app, plays only in its own room.")),
        ("검문소의 빈 방", "Checkpoint sandbox", ("받은 상자 미리 열기.", "Opening incoming boxes first."), ('첨부 파일과 다운로드가 성에 들어오기 전에. → <a href="swg-ko.html">마을로 나가는 성문 검문소</a>', 'Attachments and downloads, before they enter. → <a href="swg-en.html">the checkpoint to town</a>')),
    ],
}
