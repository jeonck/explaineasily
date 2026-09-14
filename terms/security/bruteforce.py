from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)


def keyring(x, y, n, s=1.0):
    keys = "".join(f'<g transform="rotate({-30 + i * (360 / max(n, 1))}) translate(0,26)"><rect x="-3" y="0" width="6" height="26" fill="#E9B44C"/><rect x="3" y="18" width="6" height="4" fill="#E9B44C"/><rect x="3" y="24" width="6" height="4" fill="#E9B44C"/></g>' for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="20" fill="none" stroke="#C9822B" stroke-width="6"/>{keys}</g>'


def key(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="5"/>'
            f'<rect x="8" y="-3" width="30" height="6" fill="#E9B44C"/><rect x="28" y="3" width="4" height="7" fill="#E9B44C"/><rect x="34" y="3" width="4" height="7" fill="#E9B44C"/></g>')


def door(x, y, name, s=1.0, ink="var(--ink)", extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-36" width="72" height="120" rx="3" fill="{WOOD}"/><circle cx="24" cy="64" r="4" fill="#E9B44C"/>'
            f'{label(0, -10, name, 13, ink)}{extra}</g>')


def lock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-12" y="0" width="24" height="20" rx="3" fill="#E9B44C"/>'
            f'<path d="M-7 0 v-8 a7 7 0 0 1 14 0 v8" stroke="#E9B44C" stroke-width="4" fill="none"/><circle cy="10" r="3" fill="#C9822B"/></g>')


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="34" fill="var(--panel)" stroke="var(--line)" stroke-width="4"/>'
            f'<path d="M0 -20 v20 l14 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def hourglass(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-40" width="52" height="8" rx="3" fill="{WOOD}"/><rect x="-26" y="32" width="52" height="8" rx="3" fill="{WOOD}"/>'
            f'<path d="M-20 -32 h40 l-18 32 l18 32 h-40 l18 -32z" fill="none" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-12 -26 h24 l-12 20z" fill="#E9B44C"/><path d="M-16 30 h32 l-16 -10z" fill="#E9B44C"/></g>')


def ring(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="14" fill="none" stroke="#E9B44C" stroke-width="7"/>'
            f'<path d="M-7 -14 L0 -24 L7 -14 Z" fill="var(--accent)"/></g>')


def bell(x, y, s=1.0, ring_=True):
    arcs = ('<path d="M-30 -6 a40 40 0 0 1 -12 -28 M30 -6 a40 40 0 0 0 12 -28" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>' if ring_ else "")
    return (f'<g transform="translate({x},{y}) scale({s})">{arcs}<path d="M-20 10 c0 -30 40 -30 40 0 v18 h-40 z" fill="#E9B44C"/>'
            f'<rect x="-24" y="28" width="48" height="6" rx="3" fill="#C9822B"/><circle cy="38" r="4" fill="#C9822B"/></g>')


def note(x, y, lines, s=1.0, rot=0):
    rows = "".join(label(8, 24 + i * 16, t, 11, "#142033", "start") for i, t in enumerate(lines))
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="150" height="{20 + len(lines) * 16}" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{rows}</g>'


# 1. 도둑이 열쇠 천 개를 하나씩 꽂아봐요
P1 = svg(300, sky(300)
         + person(120, 90, s=0.9, **THIEF) + keyring(230, 150, 12, 0.9) + label(230, 240, "⟦열쇠 천 개|a thousand keys⟧", 12, "var(--bad)")
         + gate(400, 60) + lock(400, 150, 0.9) + label(400, 210, "⟦우리 성문|our gate⟧", 12, "var(--muted)")
         + clock(600, 120) + label(600, 190, "⟦하나씩, 밤새|one by one, all night⟧", 12, "var(--muted)")
         + label(380, 270, "⟦맞는 열쇠가 나올 때까지 다 꽂아봐요|he tries every key until one fits⟧", 13, "var(--ink)", cls="d"))

# 2. 짧은 암호말은 금방 열려요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + door(190, 70, "⟦짧은 암호말|short password⟧", extra=lock(0, 60, 0.7)) + note(120, 200, ("⟦'사과'|'apple'⟧",), 0.9)
         + label(190, 250, "⟦→ 1분 만에 열려요|→ open in a minute⟧", 12, "var(--bad)")
         + person(345, 100, s=0.8, extra=SWEAT, **THIEF) + keyring(380, 215, 8, 0.6)
         + door(570, 70, "⟦긴 암호말|long password⟧", extra=lock(0, 50, 0.9) + lock(0, 78, 0.9)) + note(470, 200, ("⟦'파란 코끼리가 춤춰요'|'blue elephants dance'⟧",), 0.9)
         + label(570, 250, "⟦→ 몇백 년 걸려요|→ takes centuries⟧", 12, "var(--good)")
         + label(380, 295, "⟦열쇠가 짧을수록 꽂아볼 개수가 적어요 — 그래서 금방|a short key means fewer to try — so it goes fast⟧", 12, "var(--ink)", cls="d"))

# 3. 무차별 대입 = 열쇠 천 개를 다 꽂아보는 도둑 (hero)
P3 = svg(360, night(360)
         + person(150, 110, s=1.0, **THIEF) + keyring(255, 170, 10, 0.8) + label(230, 262, "⟦열쇠 천 개를 하나씩|a thousand keys, one by one⟧", 12, "#C9D5E6")
         + gate(420, 80) + lock(420, 172, 0.9) + label(420, 232, "⟦우리 성문|our gate⟧", 12, "#C9D5E6")
         + small_castle(600, 60, 0.5) + label(640, 150, "⟦다른 성|another castle⟧", 11, "#C9D5E6")
         + keyring(640, 205, 8, 0.6) + label(640, 262, "⟦거기서 훔친 열쇠 뭉치|keys stolen from there⟧", 11, "#C9D5E6")
         + label(380, 305, "⟦무차별 대입 = 맞을 때까지 다 꽂아보는 도둑|brute force = a thief who tries every key until one fits⟧", 13, "#F5E6B8", cls="d")
         + label(380, 338, "⟦남의 성에서 훔친 열쇠도 우리 문에 꽂아봐요|he even tries keys stolen from other castles on our door⟧", 12, "#C9D5E6"))

# 4. 같은 열쇠를 세 문에 쓰면 — 상점 명부가 새는 순간 우리 성문도 열려요
P4 = svg(320, sky(320)
         + door(120, 60, "⟦우리 성|our castle⟧", extra=key(0, 40, 0.8, -90)) + door(330, 60, "⟦상점|the shop⟧", extra=key(0, 40, 0.8, -90)) + door(540, 60, "⟦목욕탕|the bathhouse⟧", extra=key(0, 40, 0.8, -90))
         + '<path d="M294 120 L170 120" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 6"/><path d="M158 120 l12 -7 v14z" fill="var(--bad)"/>' + label(225, 108, "⟦같은 열쇠|same key⟧", 10, "var(--bad)")
         + person(640, 80, s=0.8, **THIEF) + note(600, 200, ("⟦상점에서 새어 나온|leaked from the shop⟧", "⟦이름 + 암호말|names + passwords⟧"), 0.8)
         + label(330, 215, "⟦세 문 다 같은 열쇠 모양 — '사과'|all three doors, the same key: 'apple'⟧", 12, "var(--ink)")
         + label(380, 270, "⟦상점 명부가 새면 우리 성문도 열려요|if the shop\'s list leaks, our gate opens too⟧", 13, "var(--bad)", cls="d")
         + label(380, 300, "⟦같은 열쇠를 여러 문에 쓰지 마세요|never use one key on many doors⟧", 12, "var(--muted)"))

# 5. 막는 법: 세 번 틀리면 잠금, 늦추기, 두 번째 확인, 종
P5 = svg(320, sky(320)
         + person(40, 110, s=0.7, face=MASK, extra=SWEAT, hat="var(--bad)", shirt="#2E3D57") + gate(160, 60) + lock(160, 150, 0.9) + person(240, 100, s=0.75, face=SMILE, **GUARD)
         + label(160, 215, "⟦세 번 틀리면 문 잠김|three misses, door locks⟧", 12, "var(--ink)")
         + hourglass(400, 120) + label(400, 215, "⟦틀리면 잠깐 기다려|wait after a miss⟧", 11, "var(--ink)")
         + ring(520, 120, 1.5) + label(520, 215, "⟦두 번째 확인|a second check⟧", 11, "var(--ink)")
         + bell(640, 110, 0.9) + label(640, 215, "⟦종이 울려요|the bell rings⟧", 11, "var(--ink)")
         + label(380, 268, "⟦긴 암호말 + 잠금 + 늦추기 + 두 번째 확인|long password + lockout + slowdown + second check⟧", 13, "var(--ink)", cls="d")
         + label(380, 298, "⟦열쇠 천 개가 있어도 세 번밖에 못 꽂아요|even with a thousand keys, he only gets three tries⟧", 12, "var(--muted)"))

KEYS_I = icon('<circle cx="32" cy="30" r="10" fill="none" stroke="#C9822B" stroke-width="4"/><rect x="18" y="38" width="5" height="20" fill="#E9B44C"/><rect x="30" y="38" width="5" height="20" fill="#E9B44C"/><rect x="42" y="38" width="5" height="20" fill="#E9B44C"/><rect x="12" y="44" width="5" height="14" fill="#E9B44C"/><rect x="48" y="44" width="5" height="14" fill="#E9B44C"/>')
BOOK_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="var(--bad)"/><rect x="20" y="16" width="24" height="32" rx="2" fill="#FFF8E7"/><rect x="24" y="22" width="16" height="3" fill="#142033"/><rect x="24" y="29" width="16" height="3" fill="#142033"/><rect x="24" y="36" width="10" height="3" fill="#142033"/>')
SACK_I = icon('<path d="M18 26 q-10 30 14 32 q24 -2 14 -32z" fill="#8B5E3C"/><rect x="24" y="16" width="16" height="10" rx="3" fill="#5A3B22"/><circle cx="32" cy="42" r="4" fill="#E9B44C"/><circle cx="24" cy="46" r="3" fill="#E9B44C"/><circle cx="40" cy="46" r="3" fill="#E9B44C"/>')
SPRAY_I = icon('<rect x="8" y="20" width="12" height="30" rx="2" fill="#8B5E3C"/><rect x="26" y="20" width="12" height="30" rx="2" fill="#8B5E3C"/><rect x="44" y="20" width="12" height="30" rx="2" fill="#8B5E3C"/><circle cx="14" cy="36" r="2" fill="#E9B44C"/><circle cx="32" cy="36" r="2" fill="#E9B44C"/><circle cx="50" cy="36" r="2" fill="#E9B44C"/><path d="M14 12 v6 M32 12 v6 M50 12 v6" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "bruteforce", "order": 66,
    "title": ("열쇠 천 개를 다 꽂아보는 도둑", "The Thief With a Thousand Keys"),
    "h1": ("<em>무차별 대입</em>이 뭐예요?", "What is a <em>Brute-Force Attack</em>?"),
    "sub": ("무차별 대입(Brute Force)과 크리덴셜 스터핑(Credential Stuffing)을 열쇠 천 개를 하나씩 꽂아보는 도둑 이야기로 풀어봤어요.",
            "Brute-force attacks and credential stuffing, told as a story about a thief who tries a thousand keys one by one."),
    "panels": [
        {"svg": P1, "alt": ("복면 도둑이 열쇠가 잔뜩 달린 꾸러미를 들고 자물쇠 달린 성문 앞에 서 있고, 옆의 시계가 밤을 가리킴", "A masked thief with a ring full of keys stands at the locked gate, a clock beside him showing the night"),
         "caption": ("도둑이 열쇠 천 개를 하나씩 꽂아봐요.", "A thief tries a thousand keys, one by one."),
         "small": ("맞는 열쇠가 나올 때까지 밤새 꽂아봐요. 열쇠는 암호말이에요.", "He keeps going all night until one fits. The keys are passwords.")},
        {"svg": P2, "alt": ("왼쪽 문은 자물쇠 하나에 쪽지 '사과' — 1분 만에 열림. 오른쪽 문은 자물쇠 둘에 쪽지 '파란 코끼리가 춤춰요' — 몇백 년. 가운데 도둑이 땀을 흘림", "Left door: one lock, note says 'apple' — open in a minute. Right door: two locks, note says 'blue elephants dance' — centuries. The thief in the middle sweats"),
         "caption": ("짧은 암호말은 금방 열려요. 긴 암호말은 몇백 년 걸려요.", "A short password opens in a minute. A long one takes centuries."),
         "small": ('열쇠가 짧을수록 꽂아볼 개수가 적어요. 자주 쓰는 말부터 꽂아보니 \'사과\'는 제일 먼저 열려요. 열쇠 대신 <a href="passkey-ko.html">반지</a>를 쓰면 꽂아볼 것 자체가 없어요.',
                   'A shorter key means fewer to try. He starts with common words, so \'apple\' opens first. With a <a href="passkey-en.html">ring</a> instead of a key, there is nothing to try at all.')},
        {"svg": P3, "hero": True, "alt": ("밤. 도둑이 열쇠 꾸러미를 들고 우리 성문 앞에 서 있고, 오른쪽에는 다른 성과 거기서 훔친 열쇠 뭉치", "Night. The thief with his key ring at our gate; on the right, another castle and a bundle of keys stolen from it"),
         "caption": ("무차별 대입은 맞을 때까지 다 꽂아보는 도둑이에요.", "Brute force is a thief who tries every key until one fits."),
         "small": ("열쇠 천 개를 하나씩 꽂아봐요. 남의 성에서 훔친 열쇠 뭉치도 우리 문에 꽂아봐요.", "He tries a thousand keys one at a time. He even tries bundles stolen from other castles on our door."),
         "tricks": (4, [
             (KEYS_I, ("다 꽂아봐요", "Tries them all"), ("가, 나, 다… 끝까지", "a, b, c… to the end")),
             (BOOK_I, ("자주 쓰는 말부터", "Common words first"), ("'사과', '1234'", "'apple', '1234'")),
             (SACK_I, ("훔친 열쇠 뭉치", "Stolen key bundles"), ("다른 성에서 새어 나온 것", "leaked from another castle"), "warm"),
             (SPRAY_I, ("문마다 하나씩 살짝", "One try per door"), ("잠기지 않게 조금씩", "just under the lockout"), "calm"),
         ])},
        {"svg": P4, "alt": ("우리 성, 상점, 목욕탕 문 셋에 똑같은 열쇠. 상점 문에서 우리 성 문으로 빨간 화살표 '같은 열쇠'. 오른쪽 도둑이 '상점에서 새어 나온 이름 + 암호말' 쪽지를 듦", "Three doors — our castle, the shop, the bathhouse — with the same key. A red arrow 'same key' from the shop door to ours. The thief on the right holds a note: 'names + passwords leaked from the shop'"),
         "caption": ("같은 열쇠를 세 문에 쓰면, 상점 명부가 새는 순간 우리 성문도 열려요.", "Use one key on three doors, and the moment the shop\'s list leaks, our gate opens too."),
         "small": ("도둑은 꽂아볼 필요도 없어요. 새어 나온 명부의 열쇠를 그대로 우리 문에 꽂아요. 같은 열쇠를 여러 문에 쓰지 마세요.", "The thief doesn\'t even have to guess. He takes the key from the leaked list and puts it straight in our door. Never use one key on many doors.")},
        {"svg": P5, "alt": ("성문 앞 땀 흘리는 도둑과 웃는 경비 — 세 번 틀리면 문 잠김. 옆으로 모래시계, 반지, 울리는 종", "A sweating thief and a smiling guard at the gate — three misses and the door locks. Beside them an hourglass, a ring, and a ringing bell"),
         "caption": ("세 번 틀리면 문을 잠가요. 한 번마다 기다리게 하고, 두 번째 확인을 하고, 종을 울려요.", "Three misses and the door locks. Make him wait between tries, ask for a second check, and ring the bell."),
         "small": ('열쇠 천 개가 있어도 세 번밖에 못 꽂아요. <a href="mfa-ko.html">두 번째 확인</a>이 있으면 열쇠가 맞아도 못 들어와요. 틀린 횟수가 쌓이면 <a href="siem-ko.html">경비실 화면</a>에 종이 울려요.',
                   'Even with a thousand keys, he gets three tries. With a <a href="mfa-en.html">second check</a>, even the right key isn\'t enough. Piled-up misses ring the bell on the <a href="siem-en.html">guard room\'s screen</a>.')},
    ],
    "summary": (("<b>무차별 대입</b> = 맞을 때까지 <b>열쇠를 다 꽂아보는</b> 도둑. <b>크리덴셜 스터핑</b> = 다른 성에서 <b>훔친 열쇠 뭉치</b>를 우리 문에 꽂아보기. 막으려면 <b>긴 암호말</b>, <b>잠금</b>, <b>두 번째 확인</b>.",
                 "<b>Brute force</b> = a thief who <b>tries every key</b> until one fits. <b>Credential stuffing</b> = trying <b>key bundles stolen</b> from other castles on our door. Stop it with <b>long passwords</b>, <b>lockout</b>, and a <b>second check</b>."),
                ("Brute Force / Credential Stuffing. 가능한 비밀번호를 전부 시도하거나(브루트 포스), 다른 서비스에서 유출된 계정 정보를 그대로 넣어 보는(크리덴셜 스터핑) 공격이에요. 긴 비밀번호, 계정 잠금, 레이트 리밋, MFA 로 막아요.",
                 "Trying every possible password (brute force), or replaying account credentials leaked from another service (credential stuffing). Long passwords, account lockout, rate limiting, and MFA stop it.")),
    "glossary": [
        ("무차별 대입", "Brute force", ("열쇠 천 개 다 꽂아보기.", "Trying all thousand keys."), ("가부터 끝까지. 짧은 암호말은 금방 걸려요.", "From a to the end. Short passwords fall fast.")),
        ("사전 공격", "Dictionary attack", ("자주 쓰는 말부터.", "Common words first."), ("'사과', '1234', '비밀번호'. 아무 열쇠나가 아니라 잘 맞는 열쇠부터 꽂아요.", "'apple', '1234', 'password'. Not random keys — the likely ones first.")),
        ("크리덴셜 스터핑", "Credential stuffing", ("훔친 열쇠 뭉치 꽂아보기.", "Trying stolen key bundles."), ("다른 성에서 샌 명부를 우리 문에 그대로. 같은 열쇠를 여러 문에 쓰면 당해요.", "A list leaked from another castle, tried on our door. It works when one key opens many doors.")),
        ("비밀번호 스프레이", "Password spraying", ("문마다 하나씩 살짝.", "One try per door."), ("한 문에 천 번이 아니라, 천 문에 한 번씩. 잠금을 피하려고요.", "Not a thousand tries on one door — one try on a thousand doors, to dodge the lockout.")),
        ("잠금 정책", "Lockout policy", ("세 번 틀리면 문 잠김.", "Three misses, door locks."), ("잠깐 잠그거나, 경비가 올 때까지 잠가요.", "Locked for a while, or until the guard comes.")),
        ("레이트 리밋", "Rate limiting", ("한 번마다 잠깐 기다려.", "Wait between tries."), ("천 개를 꽂는 데 천 밤이 걸리게 만들어요.", "Makes a thousand keys take a thousand nights.")),
        ("MFA", "MFA", ("두 번째 확인.", "The second check."), ('열쇠가 맞아도 반지가 없으면 못 들어와요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'Even the right key isn\'t enough without the ring. → <a href="mfa-en.html">the gatekeeper who checks three times</a>')),
        ("유출 데이터", "Leaked credentials", ("다른 성에서 샌 명부.", "A list leaked from another castle."), ('내 열쇠가 샜는지 알려주는 곳이 있어요. 샜으면 바로 바꿔요. → <a href="awareness-ko.html">도둑 수업</a>', 'There are places that tell you if your key has leaked. If it has, change it now. → <a href="awareness-en.html">thief lessons</a>')),
    ],
}
