from _draw import *

ME = dict(hat=None, shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
SPY, AD, MINER = "#7B3FA0", "#E9B44C", "#5B8DEF"   # 사촌 셋 — 색이 곧 이름


def bug(x, y, s=1.0, color="var(--bad)", eyes=True):
    e = '<circle cx="-14" cy="-2" r="2" fill="#FFF"/><circle cx="-8" cy="-2" r="2" fill="#FFF"/>' if eyes else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="16" ry="11" fill="{color}"/><circle cx="-12" cy="-4" r="8" fill="{color}"/>'
            f'<path d="M-6 -10 l-4 -8 M6 -10 l4 -8 M-10 8 l-6 8 M0 10 l0 9 M10 8 l6 8 M-14 -9 l-3 -6 M-8 -11 l1 -6" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>{e}</g>')


def flame(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0 -30 q14 14 8 26 q-4 10 -8 10 q-14 -4 -10 -18 q2 -8 10 -18z" fill="var(--accent)"/><path d="M0 -12 q6 8 2 14 q-4 4 -6 0 q-3 -8 4 -14z" fill="#E9B44C"/></g>'


def candle(x, y, h=80):
    """바닥 (x,y) 에 선 초. h 가 남은 길이."""
    return (f'<rect x="{x - 20}" y="{y - 6}" width="40" height="8" rx="3" fill="#C9822B"/><rect x="{x - 12}" y="{y - h}" width="24" height="{h - 4}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M{x} {y - h} v-8" stroke="#142033" stroke-width="2"/>' + flame(x, y - h - 4, 0.6))


def window(x, y, w=110, h=100, flyers=3):
    fl = "".join(f'<g transform="translate({x + 14 + i * 32},{y + 16 + (i % 2) * 34}) rotate({(i * 23) % 30 - 15})"><rect width="30" height="38" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5"/>'
                 + label(15, 24, "⟦싸다!|SALE!⟧", 8, "var(--bad)") + "</g>" for i in range(flyers))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="var(--sky)" stroke="{WOOD}" stroke-width="6"/>'
            f'<path d="M{x + w / 2} {y} v{h} M{x} {y + h / 2} h{w}" stroke="{WOOD}" stroke-width="4"/>{fl}')


def wheel(x, y, s=1.0, spin=False):
    sp = "".join(f'<path d="M0 0 L{30 * c:.1f} {30 * d:.1f}" stroke="{WOOD}" stroke-width="3"/>' for c, d in ((1, 0), (0.5, 0.87), (-0.5, 0.87), (-1, 0), (-0.5, -0.87), (0.5, -0.87)))
    mo = '<path d="M-40 -6 a40 40 0 0 1 12 -30 M40 6 a40 40 0 0 1 -12 30" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>' if spin else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="30" fill="none" stroke="{WOOD}" stroke-width="6"/>{sp}<circle r="5" fill="#5A3B22"/>'
            f'<rect x="-4" y="30" width="8" height="30" fill="{WOOD}"/><rect x="-30" y="58" width="60" height="6" rx="3" fill="#5A3B22"/>{mo}</g>')


def coin(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="11" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/><circle r="6" fill="none" stroke="#C9822B" stroke-width="1.5"/></g>'


def hourglass(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-44" width="52" height="8" rx="3" fill="{WOOD}"/><rect x="-26" y="36" width="52" height="8" rx="3" fill="{WOOD}"/>'
            f'<path d="M-20 -36 h40 l-18 36 l18 36 h-40 l18 -36z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M-14 -30 h28 l-14 26z" fill="#E9B44C"/><path d="M-16 34 h32 l-16 -8z" fill="#E9B44C"/></g>')


def chest(x, y, s=1.0, lock=False):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lk}</g>'


def notepad(x, y, s=1.0, text="⟦암호: 1-2-3-4|password: 1-2-3-4⟧"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-34" width="80" height="68" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="-40" y="-34" width="80" height="10" rx="4" fill="#C9A86A"/>'
            f'<path d="M-28 -6 h56 M-28 8 h40" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{label(0, 26, text, 9, SPY)}</g>')


def table(x, y, w=200):
    return f'<rect x="{x}" y="{y}" width="{w}" height="10" rx="3" fill="{WOOD}"/><rect x="{x + 10}" y="{y + 10}" width="10" height="50" fill="{WOOD}"/><rect x="{x + w - 20}" y="{y + 10}" width="10" height="50" fill="{WOOD}"/>'


# 1. 성이 이상해요 — 느리고, 전단이 붙고, 촛불이 빨리 닳아요
P1 = svg(320, sky(320)
         + person(60, 110, s=0.9, face=EYES, **ME)
         + window(200, 60) + label(255, 200, "⟦창문마다 전단|flyers on every window⟧", 11, "var(--muted)")
         + hourglass(420, 120, 1.1) + label(420, 200, "⟦뭘 해도 느려요|everything is slow⟧", 11, "var(--muted)")
         + candle(600, 180, 40) + label(600, 220, "⟦촛불이 벌써 반|the candle\'s half gone⟧", 11, "var(--muted)")
         + label(380, 262, "⟦누가 상자를 잠근 것도, 종이 울린 것도 아닌데요|nobody locked a chest, and no bell rang⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦그런데 성이 어딘가 이상해요|but something about the castle is off⟧", 12, "var(--muted)"))

# 2. 자물쇠 벌레는 시끄럽고, 사촌들은 조용해요
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + bubble(70, 40, 200, 36, "⟦금화 내놔!|HAND OVER THE GOLD!⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + bug(130, 170, 1.4) + chest(240, 185, 1.1, lock=True) + chest(320, 185, 0.9, lock=True)
         + label(190, 250, "⟦자물쇠 벌레는 시끄러워요 — 금방 알아요|the lock bug is loud — you notice at once⟧", 11, "var(--ink)")
         + table(450, 140) + label(550, 120, "⟦쉿…|shh…⟧", 14, "var(--muted)", cls="d")
         + bug(490, 185, 0.85, SPY) + bug(555, 190, 0.85, AD) + bug(620, 185, 0.85, MINER)
         + label(560, 250, "⟦사촌들은 조용해요 — 오래 있으려고요|the cousins stay quiet — so they can stay long⟧", 11, "var(--ink)")
         + label(380, 288, "⟦조용한 벌레가 성 안에 더 오래 있어요|the quiet bug stays in the castle longer⟧", 13, "var(--ink)", cls="d"))

# 3. 벌레의 세 사촌 (hero)
P3 = svg(360, sky(360)
         + notepad(130, 105) + bug(130, 190, 1.3, SPY)
         + label(130, 250, "⟦엿보는 벌레|the spying bug⟧", 13, "var(--ink)", cls="d") + label(130, 270, "⟦암호를 받아 적어요|writes down your passwords⟧", 11, "var(--muted)")
         + window(325, 60, 110, 90) + bug(380, 190, 1.3, AD)
         + label(380, 250, "⟦광고 벌레|the ad bug⟧", 13, "var(--ink)", cls="d") + label(380, 270, "⟦창문마다 전단을 붙여요|sticks flyers on every window⟧", 11, "var(--muted)")
         + wheel(630, 90, 0.8, spin=True) + coin(690, 130, 0.8) + bug(630, 190, 1.3, MINER)
         + label(630, 250, "⟦일 시키는 벌레|the bug that makes you work⟧", 13, "var(--ink)", cls="d") + label(630, 270, "⟦밤마다 우리 물레를 돌려요|turns our wheel all night⟧", 11, "var(--muted)")
         + label(380, 315, "⟦셋 다 조용해요 — 그래서 사촌이에요|all three are quiet — that\'s why they\'re cousins⟧", 13, "var(--ink)", cls="d")
         + label(380, 348, "⟦선물 상자 속 벌레와 같은 집안이에요|same family as the bug in the gift box⟧", 12, "var(--muted)"))

# 4. 알아채는 법 — 촛불, 경비견, 벌레 카드
P4 = svg(340, sky(340)
         + candle(90, 200, 110) + label(90, 225, "⟦평소|usual⟧", 11, "var(--muted)") + candle(170, 200, 45) + label(170, 225, "⟦요즘|lately⟧", 11, "var(--muted)")
         + label(130, 262, "⟦촛불이 두 배로 빨리 닳아요|the candle burns twice as fast⟧", 11, "var(--ink)")
         + table(320, 150, 180) + dog(390, 215, 0.85, bark=True) + bug(465, 200, 0.85, MINER)
         + label(410, 262, "⟦경비견이 냄새를 맡아요|the guard dog sniffs it out⟧", 11, "var(--ink)")
         + person(580, 100, s=0.85, face=EYES, **GUARD) + '<g transform="translate(660,170) rotate(12)"><rect x="-20" y="-28" width="40" height="56" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + bug(2, -2, 0.55, SPY, eyes=False) + '</g>'
         + bug(700, 222, 0.8, SPY)
         + label(640, 262, "⟦벌레 카드와 맞춰 봐요|matched against the bug cards⟧", 11, "var(--ink)")
         + label(380, 318, "⟦느려지고 촛불이 빨리 닳으면, 누가 몰래 일하고 있는 거예요|slow castle, fast-burning candle — someone is working in secret⟧", 12, "var(--ink)", cls="d"))

# 5. 어떻게 들어오나 — 공짜 도구 상자, 아는 사람, 그리고 빈 방
P5 = svg(320, sky(320)
         + '<rect x="60" y="110" width="140" height="90" rx="4" fill="#8B5E3C"/><rect x="60" y="110" width="140" height="10" fill="#5A3B22"/>' + label(130, 160, "⟦공짜 도구|FREE TOOLS⟧", 13, "#FFF8E7", cls="d")
         + bug(185, 192, 0.6, MINER) + label(130, 240, "⟦공짜 도구 상자에 끼워서 와요|it rides along in a free-tool box⟧", 11, "var(--ink)")
         + person(300, 100, s=0.85, face=EYES, hat=None, shirt="#7B3FA0") + '<rect x="372" y="150" width="34" height="40" rx="5" fill="#4A5A72"/>' + bug(389, 145, 0.6, SPY)
         + label(350, 240, "⟦아는 사람이 몰래 심기도 해요|sometimes someone you know plants it⟧", 11, "var(--ink)")
         + '<rect x="520" y="70" width="200" height="140" rx="6" fill="var(--night)"/><rect x="520" y="120" width="26" height="30" fill="var(--stone)"/>' + bug(640, 150, 1.0, AD)
         + person(450, 110, s=0.7, face=EYES, **ME)
         + label(620, 240, "⟦먼저 창문 없는 빈 방에서 열어봐요|open it first in the windowless room⟧", 11, "var(--ink)")
         + label(380, 300, "⟦모르는 상자는 빈 방에서 먼저, 촛불은 늘 지켜봐요|unknown boxes go to the empty room first — and keep an eye on the candle⟧", 13, "var(--ink)", cls="d"))

EYE_I = icon(f'<path d="M6 32 Q32 10 58 32 Q32 54 6 32 Z" fill="none" stroke="{SPY}" stroke-width="3"/><circle cx="32" cy="32" r="9" fill="{SPY}"/><rect x="40" y="42" width="18" height="6" rx="2" fill="#C9A86A" transform="rotate(-40 40 42)"/>')
FLYER_I = icon(f'<rect x="10" y="10" width="44" height="44" rx="3" fill="var(--sky)" stroke="{WOOD}" stroke-width="4"/><rect x="18" y="16" width="16" height="20" rx="1" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5" transform="rotate(-10 18 16)"/><rect x="34" y="30" width="16" height="20" rx="1" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5" transform="rotate(12 34 30)"/>')
WHEEL_I = icon(f'<circle cx="28" cy="30" r="18" fill="none" stroke="{WOOD}" stroke-width="4"/><path d="M28 12 v36 M10 30 h36 M15 17 l26 26 M41 17 l-26 26" stroke="{WOOD}" stroke-width="2.5"/><circle cx="52" cy="48" r="8" fill="#E9B44C" stroke="#C9822B" stroke-width="2"/>')
SHH_I = icon('<ellipse cx="30" cy="36" rx="16" ry="11" fill="var(--muted)"/><circle cx="18" cy="32" r="8" fill="var(--muted)"/><path d="M22 26 l-4 -6 M36 26 l4 -6" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round"/><text x="46" y="24" font-size="14" font-weight="700" fill="var(--ink)">z</text><text x="52" y="14" font-size="10" font-weight="700" fill="var(--ink)">z</text>')

PAGE = {
    "slug": "spyware", "order": 88,
    "title": ("몰래 엿보고, 몰래 일 시키는 벌레들", "Bugs That Spy and Bugs That Make You Work"),
    "h1": ("<em>스파이웨어</em>가 뭐예요?", "What is <em>Spyware</em>?"),
    "sub": ("스파이웨어·애드웨어·크립토재킹을 선물 상자 속 벌레의 조용한 사촌 셋 이야기로 풀어봤어요.",
            "Spyware, adware and cryptojacking, told as a story about the three quiet cousins of the bug in the gift box."),
    "panels": [
        {"svg": P1, "alt": ("어리둥절한 사람 옆에 전단이 잔뜩 붙은 창문, 느리게 떨어지는 모래시계, 벌써 반이나 닳은 촛불", "A puzzled person beside a window plastered with flyers, a slow hourglass, and a candle already half burned down"),
         "caption": ("성이 이상해요. 느려지고, 창문엔 전단이 붙고, 촛불이 빨리 닳아요.", "Something is off in the castle. It\'s slow, flyers cover the windows, and the candle burns down fast."),
         "small": ("아무도 상자를 잠그지 않았고, 종도 울리지 않았어요. 그런데 성이 어딘가 이상해요.", "Nobody locked a chest and no bell rang. And yet something about the castle is wrong.")},
        {"svg": P2, "alt": ("왼쪽: 빨간 벌레가 상자를 잠그고 '금화 내놔!' 하고 소리침. 오른쪽: 보라·노랑·파랑 벌레 셋이 탁자 밑에 '쉿…' 하고 숨어 있음", "Left: a red bug locks chests and shouts 'hand over the gold!'. Right: purple, yellow and blue bugs hide under a table going 'shh…'"),
         "caption": ("자물쇠 벌레는 시끄러워요. 이 벌레들은 조용해야 오래 있을 수 있어요.", "The lock bug is loud. These bugs have to stay quiet to stay long."),
         "small": ('<a href="ransomware-ko.html">자물쇠 벌레</a>는 금방 들켜요 — 들키는 게 목적이니까요. 사촌들은 반대예요. 들키는 날 장사가 끝나요.',
                   'The <a href="ransomware-en.html">lock bug</a> gets noticed at once — being noticed is the point. The cousins are the opposite. The day they\'re noticed, their business is over.')},
        {"svg": P3, "hero": True, "alt": ("세 사촌: 보라색 엿보는 벌레는 '암호: 1-2-3-4' 라고 적힌 수첩 밑에, 노란 광고 벌레는 전단 붙은 창문 밑에, 파란 일 시키는 벌레는 도는 물레와 금화 밑에", "Three cousins: the purple spying bug under a notepad reading 'password: 1-2-3-4', the yellow ad bug under a flyer-covered window, the blue working bug under a spinning wheel and a gold coin"),
         "caption": ("벌레의 세 사촌 — 엿보는 벌레, 광고 벌레, 몰래 일 시키는 벌레예요.", "The bug\'s three cousins — the spying bug, the ad bug, and the bug that makes you work."),
         "small": ('셋 다 <a href="malware-ko.html">선물 상자 속 벌레</a>와 같은 집안이에요. 부수지 않고, 잠그지 않고, 조용히 남의 것을 가져가요.',
                   'All three are family to the <a href="malware-en.html">bug in the gift box</a>. They break nothing, lock nothing, and quietly take what is yours.'),
         "tricks": (4, [
             (EYE_I, ("엿보는 벌레", "The spying bug"), ("암호, 편지, 창밖 풍경을 받아 적어요", "writes down passwords, letters, what\'s out the window"), "warm"),
             (FLYER_I, ("광고 벌레", "The ad bug"), ("창문마다 전단을 붙이고 돈을 받아요", "sticks flyers on windows and gets paid"), "warm"),
             (WHEEL_I, ("일 시키는 벌레", "The working bug"), ("밤마다 우리 물레로 자기 금을 만들어요", "spins our wheel all night to make its own gold"), "warm"),
             (SHH_I, ("셋 다 조용해요", "All three stay quiet"), ("들키면 끝이라서요", "getting noticed is the end for them"), "calm"),
         ])},
        {"svg": P4, "alt": ("평소 촛불과 요즘 촛불의 길이 비교 — 요즘 것이 반도 안 됨. 탁자 밑 파란 벌레를 경비견이 짖으며 찾아내고, 경비가 보라 벌레를 벌레 카드와 맞춰 봄", "Two candles compared — the recent one less than half the usual. A guard dog barks at the blue bug under the table, and a guard matches the purple bug against a bug card"),
         "caption": ("알아채는 법은 촛불이에요. 벌레가 물레를 돌리면 촛불이 빨리 닳아요.", "The way to notice is the candle. When a bug turns the wheel, the candle burns fast."),
         "small": ('촛불은 전기와 컴퓨터의 힘이에요. 느려지고 뜨거워지고 요금이 오르면 의심해요. 그다음은 <a href="edr-ko.html">경비견</a>과 <a href="antivirus-ko.html">벌레 카드</a>가 찾아요.',
                   'The candle is electricity and the computer\'s power. Slow, hot, and a bigger bill — be suspicious. Then the <a href="edr-en.html">guard dog</a> and the <a href="antivirus-en.html">bug cards</a> find it.')},
        {"svg": P5, "alt": ("'공짜 도구' 상자 구석에 파란 벌레가 숨어 있고, 아는 사람이 가방에 보라 벌레를 몰래 넣고, 창문 없는 어두운 방 안에서 노란 벌레를 작은 구멍으로 지켜봄", "A blue bug hides in the corner of a 'free tools' crate, someone familiar slips a purple bug into a bag, and a yellow bug is watched through a small hatch in a dark windowless room"),
         "caption": ("대부분 공짜 도구 상자에 끼워 들어와요. 가끔은 아는 사람이 심어요.", "Most ride in with a box of free tools. Sometimes someone you know plants one."),
         "small": ('모르는 상자는 <a href="sandbox-ko.html">창문 없는 빈 방</a>에서 먼저 열어봐요. 벌레가 있으면 그 방에서만 기어 다녀요.',
                   'Open an unknown box in the <a href="sandbox-en.html">windowless empty room</a> first. If there\'s a bug, it can only crawl around in there.')},
    ],
    "summary": (("<b>스파이웨어·애드웨어·크립토재킹</b> = 벌레의 <b>조용한 사촌 셋</b>. 암호를 <b>받아 적고</b>, 창문마다 <b>전단을 붙이고</b>, 밤마다 <b>우리 물레를 돌려</b> 자기 금을 만들어요. 성이 느려지고 <b>촛불이 빨리 닳으면</b> 의심해요.",
                 "<b>Spyware, adware, cryptojacking</b> = the bug\'s <b>three quiet cousins</b>. One <b>writes down</b> your passwords, one <b>sticks flyers</b> on every window, one <b>turns your wheel all night</b> to make its own gold. A slow castle and a <b>fast-burning candle</b> are the giveaway."),
                ("스파이웨어는 입력(키로거)·화면·파일을 몰래 수집해 보내고, 애드웨어는 광고를 끼워 넣어 돈을 벌고, 크립토재킹은 남의 CPU·전기로 암호화폐를 채굴해요. 셋 다 눈에 띄지 않는 게 목표라 CPU 사용량·네트워크·설치 목록을 살펴야 해요.",
                 "Spyware secretly collects keystrokes (keyloggers), screens and files and sends them out; adware injects ads for profit; cryptojacking mines cryptocurrency on someone else\'s CPU and electricity. All three aim to stay unnoticed, so watch CPU usage, network traffic, and what is installed.")),
    "glossary": [
        ("엿보는 벌레", "Spyware", ("몰래 보고 몰래 보내요.", "Watches in secret, sends in secret."), ("암호, 편지, 어디를 다니는지. 성 밖의 도둑에게 밤마다 보내요.", "Passwords, letters, where you go. Sent to the thief outside the castle every night.")),
        ("받아 적는 벌레", "Keylogger", ("문 앞에서 말하는 암호를 적어요.", "Writes down the password you say at the door."), ('한 글자씩 다 적어요. 그래서 암호만으론 부족하고 → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'Every letter, one by one. That\'s why a password alone isn\'t enough → <a href="mfa-en.html">the doorkeeper who checks three times</a>')),
        ("광고 벌레", "Adware", ("창문마다 전단.", "Flyers on every window."), ("전단이 붙을 때마다 벌레 주인이 돈을 받아요. 가장 순한 사촌이지만 귀찮고 느려져요.", "The bug\'s owner gets paid for every flyer. The mildest cousin — but annoying, and it slows things down.")),
        ("일 시키는 벌레", "Cryptojacking", ("밤마다 우리 물레를 돌려요.", "Turns our wheel all night."), ("우리 전기와 힘으로 자기 금(암호화폐)을 만들어요. 촛불이 빨리 닳는 이유예요.", "Makes its own gold (cryptocurrency) with our power and electricity. The reason the candle burns fast.")),
        ("아는 사람이 심은 벌레", "Stalkerware", ("가족·연인이 몰래 넣어요.", "Planted by family or a partner."), ("엿보는 벌레와 같지만, 심은 사람이 아는 사람이에요. 전화기에 많아요.", "The same as the spying bug, but planted by someone you know. Common on phones.")),
        ("공짜 도구 상자", "Bundled install", ("도구 상자 구석에 끼워서.", "Tucked in the corner of a toolbox."), ("공짜 도구를 받으면 벌레가 딸려 와요. '다음, 다음' 누르기 전에 상자 안을 봐요.", "Free tools come with a bug attached. Look inside the box before clicking next, next, next.")),
        ("자물쇠 벌레와의 차이", "Ransomware vs. spyware", ("시끄러움 vs. 조용함.", "Loud vs. quiet."), ('자물쇠 벌레는 들켜야 돈을 받고, 사촌들은 안 들켜야 돈을 벌어요. → <a href="ransomware-ko.html">상자마다 채운 도둑의 자물쇠</a>', 'The lock bug earns by being noticed; the cousins earn by not being. → <a href="ransomware-en.html">the thief\'s lock on every chest</a>')),
        ("창문 없는 빈 방", "Sandbox", ("모르는 상자를 여는 방.", "The room for opening unknown boxes."), ('벌레가 나와도 그 방 밖으로 못 가요. → <a href="sandbox-ko.html">창문 없는 빈 방</a>', 'If a bug comes out, it can\'t leave that room. → <a href="sandbox-en.html">the windowless empty room</a>')),
    ],
}
