from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
SAGE = dict(hat="#FFF", shirt="#4A5A72")
ON, OFF = "var(--accent)", "var(--muted)"


def bell(x, y, s=1.0, ring=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def room(x, y, s=1.0, windows=(True, True), door_open=True, note=True, lamps=(True, True, True), check=False):
    """정면에서 본 방. 원본 폭 160(x 0..160), 지붕 포함 높이 146(y -36..110). windows 의 True = 열림, lamps 의 True = 켜짐."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><path d="M-8 0 L80 -36 L168 0 Z" fill="var(--stone-dark)"/>'
           f'<rect width="160" height="110" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/>')
    for wx, op in ((20, windows[0]), (110, windows[1])):
        if op:
            out += (f'<rect x="{wx}" y="14" width="30" height="28" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="2"/>'
                    f'<rect x="{wx - 10}" y="14" width="8" height="28" fill="{WOOD}"/><rect x="{wx + 32}" y="14" width="8" height="28" fill="{WOOD}"/>')
        else:
            out += (f'<rect x="{wx}" y="14" width="30" height="28" fill="{WOOD}" stroke="var(--stone-dark)" stroke-width="2"/>'
                    f'<path d="M{wx} 14 l30 28 M{wx + 30} 14 l-30 28" stroke="#5A3B22" stroke-width="3"/>')
    for i, on in enumerate(lamps):
        out += f'<circle cx="{66 + i * 14}" cy="28" r="5" fill="{ON if on else OFF}"/>'
    if door_open:
        out += f'<rect x="62" y="50" width="36" height="60" fill="var(--night)"/><path d="M62 50 l-18 -8 v60 l18 8z" fill="{WOOD}"/>'
    else:
        out += f'<rect x="62" y="50" width="36" height="60" fill="{WOOD}"/><circle cx="92" cy="82" r="3" fill="#E9B44C"/>'
    if note:
        out += '<rect x="66" y="58" width="28" height="18" fill="#F5E6B8" transform="rotate(-8 66 58)"/>' + label(80, 71, "⟦1234|1234⟧", 9, "#142033", cls="d")
    if check:
        out += '<circle cx="150" cy="-4" r="12" fill="var(--good)"/><path d="M143 -4 l5 5 l9 -10" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return out + "</g>"


def checklist(x, y, w, h, title, rows, s=1.0, size=12):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="28" rx="6" fill="#C9A86A"/>' + label(w / 2, 19, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        yy = 52 + i * 30
        out += (f'<rect x="14" y="{yy - 12}" width="16" height="16" rx="3" fill="#FFF" stroke="#C9A86A" stroke-width="2"/>'
                f'<path d="M17 {yy - 4} l4 4 l7 -9" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>' + label(40, yy + 4, r, size, "#142033", "start"))
    return out + "</g>"


# 1. 새 방은 문이 다 열린 채로 와요
P1 = svg(320, sky(320)
         + label(380, 36, "⟦새 방이 왔어요!|the new room is here!⟧", 14, "var(--ink)", cls="d")
         + room(280, 100, 1.3)
         + label(130, 116, "⟦창문이 다 열려 있어요|every window is open⟧", 11, "var(--bad)") + '<path d="M210 122 L300 138" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(625, 116, "⟦도구가 다 켜져 있어요|every tool is switched on⟧", 11, "var(--bad)") + '<path d="M545 122 L420 138" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(625, 212, "⟦문엔 공장 암호말 쪽지|the factory password, on a note⟧", 11, "var(--bad)") + '<path d="M540 206 L402 186" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>'
         + person(130, 170, s=0.8, face=EYES, **GUARD)
         + label(380, 300, "⟦새 방은 문이 다 열린 채로 와요|a new room arrives with everything open⟧", 12, "var(--ink)", cls="d"))

# 2. 그대로 쓰면 — 도둑도 공장 암호말을 알아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + room(200, 90, 1.2)
         + person(150, 80, s=0.6, face=MASK) + '<path d="M186 122 L222 128" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/><path d="M222 128 l-10 -8 l2 12z" fill="var(--bad)"/>'
         + label(120, 250, "⟦열린 창문으로|through the open window⟧", 10, "var(--bad)")
         + person(420, 120, s=0.65, face=MASK) + bubble(390, 44, 160, 30, "⟦1234… 고마워요|1234… thanks⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + label(440, 250, "⟦쪽지를 읽고 문으로|reads the note, walks in⟧", 10, "var(--bad)")
         + person(620, 110, s=0.8, face=FROWN + SWEAT, **GUARD) + label(640, 250, "⟦아직 아무도 안 봤는데…|nobody\'s even looked yet…⟧", 10, "var(--muted)")
         + label(380, 288, "⟦도둑도 공장 암호말을 알아요 — 세상 모든 새 방이 똑같으니까요|thieves know the factory password too — every new room is the same⟧", 11, "var(--ink)", cls="d"))

# 3. 문단속 목록 (hero)
ROWS = ("⟦안 쓰는 문과 창문은 막기|board up unused doors and windows⟧", "⟦공장 암호말은 바꾸기|change the factory password⟧", "⟦안 쓰는 도구는 끄기|switch off unused tools⟧",
        "⟦일지는 켜기|turn the logbook on⟧", "⟦판자는 최신으로|newest planks on⟧", "⟦열쇠는 필요한 사람만|keys only to those who need them⟧")
P3 = svg(360, sky(360)
         + checklist(50, 40, 310, 240, "⟦문단속 목록|THE LOCK-UP LIST⟧", ROWS, size=11)
         + room(430, 120, 1.2, windows=(False, False), door_open=False, note=False, lamps=(True, False, False), check=True)
         + person(650, 200, s=0.7, face=SMILE, **GUARD)
         + label(526, 282, "⟦문단속 끝난 방|a locked-up room⟧", 11, "var(--good)", cls="d")
         + label(526, 62, "⟦쓰기 전에, 목록대로|before use, by the list⟧", 12, "var(--ink)", cls="d")
         + label(380, 344, "⟦새 방을 쓰기 전에 목록대로 문단속을 해요|before a new room is used, lock it up by the list⟧", 12, "var(--ink)", cls="d"))

# 4. 현자들의 목록 — 모든 방을 같은 목록으로
P4 = svg(320, sky(320)
         + checklist(40, 40, 210, 130, "⟦현자들의 목록|THE SAGES\' LIST⟧", ("⟦방마다 뭘 잠글지|what to lock, per room⟧", "⟦왜 잠그는지|and why⟧", "⟦어떻게 확인하는지|and how to check⟧"), size=11)
         + person(60, 190, s=0.5, face=SMILE, **SAGE) + person(110, 200, s=0.5, face=SMILE, **SAGE) + person(160, 190, s=0.5, face=SMILE, **SAGE)
         + label(130, 272, "⟦여러 성의 현자들이 같이 썼어요|written together by sages from many castles⟧", 10, "var(--muted)")
         + '<path d="M258 105 H292" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M296 105 l-10 -7 v14z" fill="var(--muted)"/>'
         + "".join(room(300 + i * 110, 110, 0.55, windows=(False, False), door_open=False, note=False, lamps=(True, False, False), check=True) for i in range(4))
         + label(509, 204, "⟦모든 방을 같은 목록으로 — 이게 기준선이에요|every room by the same list — that\'s the baseline⟧", 11, "var(--ink)", cls="d")
         + label(509, 228, "⟦우리 성 사정에 맞게 조금만 고쳐요|tweaked just a little for our castle⟧", 10, "var(--muted)")
         + label(380, 302, "⟦현자들의 목록을 우리 성 목록으로 삼아요|the sages\' list becomes our castle\'s list⟧", 12, "var(--ink)", cls="d"))

# 5. 달라지면 종 — 본보기 방을 찍어내고, 계속 같은지 봐요
P5 = svg(320, sky(320)
         + room(40, 80, 0.55, windows=(False, False), door_open=False, note=False, lamps=(True, False, False), check=True)
         + label(84, 170, "⟦본보기 방|the model room⟧", 10, "var(--ink)", cls="d")
         + '<path d="M140 110 H186" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/><path d="M190 110 l-10 -7 v14z" fill="var(--muted)"/>'
         + "".join(room(200 + i * 100, 80, 0.55, windows=(False, False), door_open=False, note=False, lamps=(True, False, False), check=True) for i in range(3))
         + room(500, 80, 0.55, windows=(True, False), door_open=False, note=False, lamps=(True, True, False))
         + label(598, 70, "⟦!|!⟧", 26, "var(--bad)", cls="d")
         + label(344, 170, "⟦똑같이 찍어낸 방들|rooms copied exactly⟧", 10, "var(--muted)") + label(544, 170, "⟦창문이 다시 열렸어요|a window opened again⟧", 10, "var(--bad)")
         + bell(660, 100, 0.7, ring=True) + person(690, 140, s=0.5, face=FROWN, **GUARD) + label(680, 225, "⟦종! 다시 잠가요|bell! lock it again⟧", 10, "var(--accent)")
         + label(380, 262, "⟦매달 목록을 다시 확인해요 — 달라진 방이 있으면 종|check the list again every month — a room that drifted rings the bell⟧", 11, "var(--muted)")
         + label(380, 302, "⟦한 번 잠그고 끝이 아니에요 — 계속 같은지 봐요|locking up once isn\'t the end — keep checking it\'s still the same⟧", 12, "var(--ink)", cls="d"))

BOARD_I = icon(f'<rect x="14" y="12" width="36" height="40" rx="3" fill="{WOOD}" stroke="#5A3B22" stroke-width="2"/><path d="M14 12 l36 40 M50 12 l-36 40" stroke="#5A3B22" stroke-width="4"/>')
PASS_I = icon('<rect x="10" y="20" width="44" height="26" rx="3" fill="#F5E6B8"/><path d="M16 33 h32" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M40 12 l8 8" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="12" r="5" fill="var(--good)"/>')
LAMP_I = icon('<circle cx="22" cy="32" r="8" fill="var(--muted)"/><circle cx="42" cy="32" r="8" fill="var(--muted)"/><path d="M14 46 h36" stroke="var(--stone-dark)" stroke-width="3" stroke-linecap="round"/><path d="M8 14 l48 36" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
LOG_I = icon(f'<rect x="12" y="14" width="30" height="38" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M18 24 h18 M18 32 h18 M18 40 h12" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/><rect x="36" y="36" width="20" height="10" rx="2" fill="{WOOD}"/><path d="M40 41 h12" stroke="#5A3B22" stroke-width="2" stroke-dasharray="2 2"/>')

PAGE = {
    "slug": "hardening", "order": 104,
    "title": ("새 방을 쓰기 전에 하는 문단속", "Locking Up a New Room Before You Use It"),
    "h1": ("<em>하드닝</em>이 뭐예요?", "What is <em>Hardening</em>?"),
    "sub": ("하드닝(Hardening)과 보안 기준선(Security Baseline, CIS 벤치마크)을 문이 다 열린 채로 온 새 방을 목록대로 문단속하는 이야기로 풀어봤어요.",
            "Hardening and security baselines (CIS Benchmarks), told as a story about a new room that arrives with everything open, and the list you lock it up by."),
    "panels": [
        {"svg": P1, "alt": ("지붕 달린 새 방. 창문 둘이 활짝 열려 있고, 등불 셋이 다 켜져 있고, 열린 문에는 '1234'라고 적힌 쪽지가 붙어 있음. 경비가 옆에서 보고 있음", "A new room with a roof. Both windows stand wide open, all three lamps are lit, and a note reading 1234 is stuck to the open door. A guard looks on"),
         "caption": ("새 방은 문이 다 열린 채로 와요.", "A new room arrives with everything open."),
         "small": ('안 쓰는 창문이 열려 있고, 켜진 채로 온 도구들이 있고, 문에는 <a href="password-ko.html">공장 암호말</a> 쪽지가 붙어 있어요. 만든 사람은 "쓰기 편하게" 그렇게 보내요.',
                   'Unused windows stand open, tools arrive switched on, and a <a href="password-en.html">factory password</a> is stuck to the door. The maker ships it that way to be "easy to use."')},
        {"svg": P2, "alt": ("그대로 둔 새 방에 도둑 하나는 열린 창문으로 들어가고, 다른 도둑은 '1234… 고마워요' 하며 쪽지를 읽고 문으로 들어감. 경비는 땀을 흘리며 아직 아무도 안 봤다고 함", "In the room left as it came, one thief climbs through the open window and another reads the note — 1234, thanks — and walks in the door. The guard sweats: nobody has even looked yet"),
         "caption": ("그대로 쓰면 도둑도 다 알아요.", "Use it as it came, and the thieves already know it."),
         "small": ('세상 모든 새 방이 똑같이 오니까, 도둑은 공장 암호말과 열린 창문 위치를 외우고 다녀요. <a href="bruteforce-ko.html">열쇠 천 개</a>를 꽂아볼 필요도 없어요.',
                   'Every new room in the world arrives the same, so thieves memorize the factory password and where the open windows are. No need to <a href="bruteforce-en.html">try a thousand keys</a>.')},
        {"svg": P3, "hero": True, "alt": ("여섯 줄 문단속 목록에 전부 체크: 안 쓰는 문과 창문 막기, 공장 암호말 바꾸기, 안 쓰는 도구 끄기, 일지 켜기, 판자 최신으로, 열쇠는 필요한 사람만. 옆에는 창문에 판자를 대고 문을 닫고 등불 하나만 켠 방에 초록 체크 표시, 웃는 경비", "A six-line lock-up list, all ticked: board up unused doors and windows, change the factory password, switch off unused tools, turn the logbook on, newest planks on, keys only to those who need them. Beside it, a room with boarded windows, a shut door, and a single lamp lit wears a green check, and the guard smiles"),
         "caption": ("하드닝은 새 방을 쓰기 전에 목록대로 하는 문단속이에요.", "Hardening is locking up a new room, by the list, before you use it."),
         "small": ('안 쓰는 문은 막고, 암호말은 바꾸고, 안 쓰는 도구는 끄고, <a href="log-ko.html">일지</a>는 켜고, <a href="patch-ko.html">판자</a>는 최신으로. 남는 건 진짜 쓰는 문 하나뿐이에요.',
                   'Board up what isn\'t used, change the password, switch off spare tools, turn the <a href="log-en.html">logbook</a> on, put the newest <a href="patch-en.html">planks</a> on. What\'s left is the one door you actually use.'),
         "tricks": (4, [
             (BOARD_I, ("안 쓰는 문은 막기", "Board up unused doors"), ("문이 적을수록 지킬 게 적어요", "fewer doors, less to guard"), "calm"),
             (PASS_I, ("암호말 바꾸기", "Change the password"), ("공장 암호말은 도둑도 알아요", "thieves know the factory one")),
             (LAMP_I, ("안 쓰는 도구 끄기", "Switch off spare tools"), ("켜진 도구는 전부 들어올 틈", "every lit tool is a way in")),
             (LOG_I, ("일지 켜고 판자 최신", "Logbook on, planks new"), ("무슨 일이 있었는지 남게", "so what happens gets written down"), "warm"),
         ])},
        {"svg": P4, "alt": ("여러 성의 현자 셋이 같이 쓴 목록 — 방마다 뭘 잠글지, 왜, 어떻게 확인하는지. 화살표 너머로 똑같이 문단속된 방 넷이 나란히 서 있고, 모든 방을 같은 목록으로 한다는 글", "Three sages from many castles and the list they wrote together — what to lock per room, why, and how to check. Past an arrow, four identically locked-up rooms stand in a row, captioned every room by the same list"),
         "caption": ("현자들의 목록을 우리 성 목록으로 삼아요.", "The sages\' list becomes our castle\'s list."),
         "small": ('방 종류마다 뭘 잠가야 하는지, 여러 성의 현자들이 이미 적어 뒀어요. 그걸 우리 성에 맞게 조금 고쳐서 모든 방에 똑같이 써요 — 이게 기준선이에요. <a href="policy-ko.html">규칙 두루마리</a>에 적어 두고요.',
                   'What to lock in each kind of room, sages from many castles have already written down. Tweak it a little for our castle and apply it to every room the same way — that\'s the baseline. Written into the <a href="policy-en.html">rule scroll</a>.')},
        {"svg": P5, "alt": ("체크 표시된 본보기 방 하나에서 화살표로 똑같은 방 셋이 찍혀 나오고, 네 번째 방은 창문이 다시 열려 빨간 느낌표. 종이 울리고 경비가 찡그림", "From one checked model room, an arrow leads to three identical copies; the fourth room has a window open again and a red exclamation mark. The bell rings and the guard frowns"),
         "caption": ("한 번 잠그고 끝이 아니에요. 계속 같은지 봐요.", "Locking up once isn\'t the end. Keep checking it\'s still the same."),
         "small": ('문단속 끝난 본보기 방을 <a href="container-ko.html">똑같이 찍어내면</a> 매번 처음부터 할 필요가 없어요. 그래도 누가 창문을 다시 열 수 있으니 <a href="cspm-ko.html">달라진 방</a>이 있으면 종이 울리게 해요. 바깥에서 세어 봐도 문이 줄어 있어야 해요 — <a href="asm-ko.html">우리 성의 문 세기</a>.',
                   'Copy the locked-up model room <a href="container-en.html">exactly</a>, and you never start from scratch. Someone can still open a window again, so a <a href="cspm-en.html">room that drifted</a> rings the bell. Counted from outside, the doors should be fewer too — <a href="asm-en.html">counting our castle\'s doors</a>.')},
    ],
    "summary": (("<b>하드닝</b> = 문이 다 열린 채로 온 새 방을 <b>쓰기 전에</b> 목록대로 문단속 — 안 쓰는 문 막고, 암호말 바꾸고, 도구 끄고, 일지 켜고. <b>기준선</b> = 모든 방을 <b>같은 목록</b>으로, 그리고 계속 같은지 보기.",
                 "<b>Hardening</b> = lock up the new room that arrived wide open, <b>before you use it</b>, by the list — board up spare doors, change the password, switch off tools, turn the logbook on. A <b>baseline</b> = every room by the <b>same list</b>, checked again and again."),
                ("Hardening / Security Baseline. 서버·OS·앱·네트워크 장비의 기본 설정에서 불필요한 서비스·포트·계정을 없애고, 기본 암호를 바꾸고, 로깅과 패치를 켜서 공격 표면을 줄이는 작업이에요. CIS 벤치마크 같은 공개 기준을 조직에 맞게 조정한 것이 보안 기준선이고, 골든 이미지로 복제하고 설정 드리프트를 감시해요.",
                 "Stripping a server, OS, app, or network device of unneeded services, ports, and accounts, changing default passwords, and enabling logging and patching to shrink the attack surface. A public standard like the CIS Benchmarks, tuned to the organization, becomes the security baseline — cloned as a golden image and watched for configuration drift.")),
    "glossary": [
        ("하드닝", "Hardening", ("쓰기 전 문단속.", "Locking up before use."), ("새 방에서 안 쓰는 문·도구·암호말을 치우는 일. 남는 건 진짜 쓰는 문 하나뿐이에요.", "Clearing a new room of unused doors, tools, and the factory password. What remains is the one door you actually use.")),
        ("보안 기준선", "Security baseline", ("모든 방을 같은 목록으로.", "Every room by the same list."), ('우리 성의 문단속 목록. 새 방은 전부 이 목록을 지나요. → <a href="policy-ko.html">성의 규칙 두루마리</a>', 'Our castle\'s lock-up list. Every new room goes through it. → <a href="policy-en.html">the castle\'s rule scroll</a>')),
        ("CIS 벤치마크", "CIS Benchmarks", ("현자들의 목록.", "The sages\' list."), ("여러 성이 같이 쓴 공개 목록. 방 종류마다 뭘 잠그고 왜 잠그는지, 어떻게 확인하는지 적혀 있어요.", "A public list written by many castles together — what to lock in each kind of room, why, and how to check.")),
        ("공격 표면", "Attack surface", ("도둑이 시도해 볼 수 있는 문의 수.", "How many doors a thief could try."), ('문단속은 이 수를 줄이는 일이에요. → <a href="asm-ko.html">바깥에서 세는 우리 성의 문</a>', 'Hardening is about making this number smaller. → <a href="asm-en.html">counting our castle\'s doors from outside</a>')),
        ("기본 설정 위험", "Insecure defaults", ("문 열린 채로 온 새 방.", "The room that arrived open."), ('편하라고 열어 둔 것들. 공장 암호말이 대표예요. → <a href="password-ko.html">문지기에게 속삭이는 암호말</a>', 'Things left open for convenience. The factory password is the classic. → <a href="password-en.html">the password you whisper to the doorkeeper</a>')),
        ("불필요한 서비스", "Unnecessary services", ("켜진 채로 온 도구.", "Tools that arrived switched on."), ("안 쓰는데 켜져 있으면 그게 다 들어올 틈이에요. 끄거나 떼어 내요.", "If it\'s on but unused, it\'s a way in. Switch it off or remove it.")),
        ("설정 드리프트", "Configuration drift", ("다시 열린 창문.", "The window that opened again."), ('문단속 끝난 방이 시간이 지나며 목록과 달라지는 것. 달라지면 종. → <a href="cspm-ko.html">빌린 창고 문단속 점검</a>', 'A locked-up room slowly drifting away from the list. When it drifts, the bell. → <a href="cspm-en.html">checking the rented warehouse</a>')),
        ("골든 이미지", "Golden image", ("본보기 방.", "The model room."), ('문단속 끝난 방을 똑같이 찍어내요. → <a href="container-ko.html">똑같이 찍어낸 짐칸</a>', 'A locked-up room, copied exactly. → <a href="container-en.html">crates stamped out identically</a>')),
    ],
}
