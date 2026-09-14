from _draw import *

ME = dict(hat=None, shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
IRON = "#3A4556"
IRON_DARK = "#222B38"
GOLD = "#E9B44C"


def letter(x, y, text, s=1.0, scrambled=False, locked=False, rot=0):
    ink = "var(--bad)" if scrambled else "#142033"
    lock = ('<g transform="translate(120,60)"><rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--good)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--good)" stroke-width="4" fill="none"/></g>' if locked else "")
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'{label(70, 34, text, 13, ink, cls="" if scrambled else "d")}<rect x="16" y="52" width="70" height="4" rx="2" fill="#C9A86A"/>{lock}</g>')


def key(x, y, s=1.0, color=GOLD, broken=False):
    if broken:
        return (f'<g transform="translate({x},{y}) scale({s})"><g transform="rotate(-20)"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="12" height="6" fill="{color}"/></g>'
                f'<g transform="translate(30,10) rotate(25)"><rect x="0" y="-3" width="16" height="6" fill="{color}"/><rect x="4" y="3" width="4" height="7" fill="{color}"/><rect x="11" y="3" width="4" height="9" fill="{color}"/></g>'
                f'<path d="M18 -14 l4 -8 M24 -10 l8 -4 M14 14 l-6 6" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/></g>')
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


def safe(x, y, s=1.0, cracked=False, key_state="ok"):
    """쇠금고. 가운데 창(cut-away)에 열쇠가 보이고, 앞에 창구(슬롯)가 있다."""
    inner_key = {"ok": key(-14, -50, 1.1), "broken": key(-18, -52, 1.0, broken=True), "none": ""}[key_state]
    crack = '<path d="M-110 -40 l30 20 l-18 26 l34 14 M60 -120 l-10 30 l24 10 l-16 28" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>' if cracked else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-110" y="-120" width="220" height="240" rx="12" fill="{IRON}" stroke="{IRON_DARK}" stroke-width="6"/>'
            f'<rect x="-96" y="-106" width="192" height="212" rx="8" fill="none" stroke="{IRON_DARK}" stroke-width="3"/>'
            f'<circle cx="80" cy="0" r="16" fill="{IRON_DARK}"/><circle cx="80" cy="0" r="6" fill="{GOLD}"/>'
            f'<rect x="-70" y="-84" width="120" height="66" rx="6" fill="#111C30"/>{inner_key}'
            f'<rect x="-50" y="20" width="100" height="14" rx="4" fill="#111C30"/>{crack}</g>')


def drawer(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-100" y="-40" width="200" height="80" rx="4" fill="#8B5E3C"/><rect x="-90" y="-30" width="180" height="60" rx="3" fill="#5A3B22"/>'
            f'<rect x="-88" y="-28" width="176" height="56" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="0" cy="34" r="5" fill="{GOLD}"/></g>')


def arrow(x1, y1, x2, y2, color="var(--accent)"):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 12 * math.cos(a), y2 - 12 * math.sin(a)
    px, py = 6 * math.sin(a), -6 * math.cos(a)
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"/>'
            f'<path d="M{x2} {y2} L{hx + px:.0f} {hy + py:.0f} L{hx - px:.0f} {hy - py:.0f} Z" fill="{color}"/>')


def cert(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-32" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-16 -18 h32 M-16 -8 h20 M-16 2 h32" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>'
            f'<circle cx="12" cy="18" r="9" fill="var(--bad)"/><path d="M8 26 l-4 12 M16 26 l4 12" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/></g>')


def notes(x, y):
    return "".join(f'<rect x="{x + i * 6 - 12}" y="{y - i * 5}" width="22" height="16" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="1.5" transform="rotate({i * 8 - 8} {x} {y})"/>' for i in range(3))


SCR = "⟦x7#q!m2|x7#q!m2⟧"
PLAIN = "⟦사과 두 개 사 와|Buy two apples⟧"

# 1. 봉인 편지의 진짜 열쇠는 어디 두나요?
P1 = svg(300, sky(300)
         + letter(40, 50, SCR, 0.85, scrambled=True, locked=True) + letter(40, 140, SCR, 0.85, scrambled=True, locked=True) + letter(170, 95, SCR, 0.85, scrambled=True, locked=True)
         + label(165, 240, "⟦봉인 편지들|the sealed letters⟧", 12, "var(--muted)")
         + person(360, 110, s=0.85, face=FROWN, **ME)
         + bubble(300, 20, 230, 34, "⟦진짜 열쇠는 어디 두지?|where do I keep the real key?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + key(560, 130, 1.8) + label(600, 190, "⟦이 열쇠 하나로 다 열려요|this one key opens them all⟧", 11, "var(--bad)")
         + person(680, 150, s=0.7, face=MASK)
         + label(380, 280, "⟦열쇠를 잃으면 나도 못 읽고, 도둑이 가지면 다 읽혀요|lose the key and I can\'t read them; let a thief take it and he reads them all⟧", 12, "var(--ink)"))

# 2. 종이에 적어 서랍에 두면 도둑이 베껴요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(160, 60, "⟦종이에 적어 서랍에|written on paper, in a drawer⟧", 13, "var(--ink)", cls="d")
         + drawer(160, 160) + key(160, 160, 1.1)
         + label(160, 235, "⟦누구나 열 수 있는 서랍|a drawer anyone can open⟧", 11, "var(--muted)")
         + arrow(290, 160, 370, 160)
         + person(400, 100, s=0.8, face=MASK, extra=BAG)
         + key(500, 120, 1.2) + key(500, 160, 1.2) + label(600, 104, "⟦베꼈어요|copied it⟧", 12, "var(--bad)", cls="d")
         + letter(560, 180, PLAIN, 0.8)
         + label(380, 282, "⟦열쇠가 밖에 있으면 언젠가 베껴져요 — 편지 봉인이 소용없어요|a key kept outside gets copied someday — and the seal means nothing⟧", 12, "var(--ink)"))

# 3. 열쇠를 만드는 쇠금고 (hero)
P3 = svg(360, sky(360)
         + label(400, 50, "⟦쇠금고|the iron safe⟧", 14, "var(--ink)", cls="d")
         + safe(400, 190)
         + label(400, 122, "⟦열쇠는 안에서 안 나와요|the key never leaves⟧", 10, "#F5E6B8")
         + person(130, 150, s=0.85, face=SMILE, **ME) + letter(200, 230, PLAIN, 0.6)
         + arrow(288, 244, 346, 224) + label(170, 295, "⟦편지를 창구에 넣어요|drop the letter in the slot⟧", 11, "var(--muted)")
         + arrow(452, 217, 534, 224) + letter(540, 200, SCR, 0.6, scrambled=True, locked=True)
         + person(640, 150, s=0.85, face=SMILE, **GUARD) + label(600, 275, "⟦봉인해서 돌려줘요|sealed, and handed back⟧", 11, "var(--good)")
         + label(380, 340, "⟦열쇠는 금고 안에서 태어나고, 안에서만 일해요|the key is born inside the safe and only ever works inside⟧", 13, "var(--ink)", cls="d"))

# 4. 억지로 열면 / 열쇠 목록
ROWS = (("⟦편지 열쇠|letter key⟧", "⟦봄|spring⟧", "⟦가을|autumn⟧"), ("⟦도장 열쇠|seal key⟧", "⟦작년|last year⟧", "⟦이번 달|this month⟧"), ("⟦창고 열쇠|storeroom key⟧", "⟦여름|summer⟧", "⟦겨울|winter⟧"))
P4 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + label(190, 36, "⟦억지로 열면|force it open, and…⟧", 14, "var(--ink)", cls="d")
         + person(60, 90, s=0.75, face=MASK, extra=SWEAT)
         + '<g transform="translate(125,120) rotate(-30)"><rect x="-3" y="-16" width="6" height="44" fill="#8B5E3C"/><rect x="-16" y="-26" width="32" height="14" rx="3" fill="var(--stone-dark)"/></g>'
         + safe(250, 170, 0.6, cracked=True, key_state="broken")
         + label(190, 275, "⟦열쇠가 스스로 부서져요 — 도둑 손엔 빈 상자|the key destroys itself — the thief gets an empty box⟧", 10, "var(--bad)")
         + label(570, 36, "⟦열쇠 목록|the key ledger⟧", 14, "var(--ink)", cls="d")
         + '<rect x="430" y="55" width="280" height="190" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + label(520, 82, "⟦어떤 열쇠|which key⟧", 10, "#142033", cls="d") + label(610, 82, "⟦만든 날|made⟧", 10, "#142033", cls="d") + label(675, 82, "⟦바꾸는 날|swap⟧", 10, "#142033", cls="d")
         + "".join(key(450, 110 + i * 36, 0.5) + label(520, 114 + i * 36, a, 11, "#142033") + label(610, 114 + i * 36, b, 11, "#142033") + label(675, 114 + i * 36, c, 11, "var(--accent)") for i, (a, b, c) in enumerate(ROWS))
         + label(570, 228, "⟦바꾸는 날엔 새 열쇠, 옛 열쇠는 폐기|on swap day: a new key, the old one retired⟧", 10, "var(--accent)")
         + label(570, 275, "⟦어떤 열쇠를 언제 바꾸나 — 목록이 알아요|which key gets swapped when — the ledger knows⟧", 10, "var(--muted)")
         + label(380, 302, "⟦금고는 지키고, 목록은 관리해요|the safe protects; the ledger manages⟧", 12, "var(--ink)", cls="d"))

# 5. 쇠금고 열쇠로 편지도 봉인하고 도장도 찍어요 / 쪽지 상자와는 달라요
P5 = svg(300, sky(300)
         + safe(140, 150, 0.7) + label(140, 262, "⟦쇠금고|the iron safe⟧", 12, "var(--ink)", cls="d")
         + arrow(220, 130, 314, 92) + letter(320, 55, SCR, 0.7, scrambled=True, locked=True) + label(369, 132, "⟦봉인 편지|the sealed letter⟧", 10, "var(--muted)")
         + arrow(220, 170, 336, 196) + cert(369, 200) + label(369, 256, "⟦성의 도장 (인증서)|the castle seal (certificate)⟧", 10, "var(--muted)")
         + '<path d="M480 40 V250" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 8"/>'
         + label(620, 60, "⟦비밀 쪽지 상자|the secret-note box⟧", 12, "var(--ink)", cls="d")
         + '<g transform="translate(620,150)"><rect x="-40" y="-14" width="80" height="44" rx="3" fill="#8B5E3C"/><path d="M-40 -14 h80 v-4 a40 12 0 0 0 -80 0z" fill="#5A3B22"/></g>' + notes(620, 108)
         + label(620, 215, "⟦비밀번호 쪽지는 여기|passwords live here⟧", 10, "var(--muted)") + label(620, 233, "⟦열쇠를 만들진 않아요|it does not make keys⟧", 10, "var(--muted)")
         + label(380, 285, "⟦쇠금고는 열쇠를 만들어 쓰고, 쪽지 상자는 비밀을 보관해요 — 다른 일이에요|the safe makes and uses keys; the note box stores secrets — different jobs⟧", 11, "var(--ink)"))

FORGE_I = icon(f'<rect x="10" y="10" width="44" height="44" rx="6" fill="{IRON}" stroke="{IRON_DARK}" stroke-width="3"/><rect x="18" y="20" width="28" height="18" rx="3" fill="#111C30"/><circle cx="27" cy="29" r="4" fill="none" stroke="{GOLD}" stroke-width="2.5"/><rect x="31" y="28" width="10" height="3" fill="{GOLD}"/><path d="M22 14 l-3 -5 M32 12 v-6 M42 14 l3 -5" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/>')
STAY_I = icon(f'<rect x="10" y="14" width="44" height="40" rx="6" fill="{IRON}" stroke="{IRON_DARK}" stroke-width="3"/><circle cx="26" cy="34" r="5" fill="none" stroke="{GOLD}" stroke-width="3"/><rect x="31" y="32" width="14" height="4" fill="{GOLD}"/><path d="M54 34 h8" stroke="var(--bad)" stroke-width="3"/><path d="M56 26 l8 16 M64 26 l-8 16" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')
SLOT_I = icon(f'<rect x="8" y="22" width="48" height="34" rx="5" fill="{IRON}" stroke="{IRON_DARK}" stroke-width="3"/><rect x="18" y="36" width="28" height="6" rx="2" fill="#111C30"/><rect x="22" y="6" width="20" height="14" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M32 22 v10" stroke="var(--accent)" stroke-width="3"/><path d="M28 29 l4 5 l4 -5" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
TAMPER_I = icon(f'<g transform="translate(14,14) rotate(-30)"><rect x="-2" y="-6" width="4" height="26" fill="#8B5E3C"/><rect x="-9" y="-12" width="18" height="8" rx="2" fill="var(--stone-dark)"/></g><g transform="translate(36,40) rotate(-20)"><circle r="6" fill="none" stroke="{GOLD}" stroke-width="3"/><rect x="6" y="-2" width="7" height="4" fill="{GOLD}"/></g><rect x="46" y="44" width="12" height="4" fill="{GOLD}" transform="rotate(30 52 46)"/><path d="M44 30 l3 -6 M50 34 l6 -3 M30 52 l-5 5" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/>')

PAGE = {
    "slug": "hsm", "order": 98,
    "title": ("열쇠를 만드는 쇠금고", "The Iron Safe That Makes Keys"),
    "h1": ("<em>HSM</em>이 뭐예요?", "What is an <em>HSM</em>?"),
    "sub": ("HSM과 키 관리(KMS)를 열쇠가 절대 밖으로 안 나오는 쇠금고 이야기로 풀어봤어요.",
            "HSMs and key management (KMS), told as a story about an iron safe whose keys never come out."),
    "panels": [
        {"svg": P1, "alt": ("초록 자물쇠가 달린 봉인 편지 세 통 옆에서 내가 '진짜 열쇠는 어디 두지?' 하고 고민한다. 오른쪽에 큰 황금 열쇠 하나, 그 뒤로 도둑이 엿본다", "Beside three sealed letters with green locks, I wonder where to keep the real key. On the right, one big golden key, with a thief peeking behind it"),
         "caption": ("봉인 편지의 진짜 열쇠는 어디 두나요?", "Where do you keep the real key to the sealed letters?"),
         "small": ('<a href="encryption-ko.html">봉인 편지</a>는 열쇠 하나로 다 열려요. 열쇠를 잃으면 나도 못 읽고, 도둑이 가지면 다 읽혀요.',
                   'One key opens every <a href="encryption-en.html">sealed letter</a>. Lose it and I can\'t read them; let a thief take it and he reads them all.')},
        {"svg": P2, "alt": ("종이에 적힌 열쇠가 서랍에 들어 있다. 화살표 끝에서 도둑이 똑같은 열쇠 두 개를 들고 편지를 읽는다", "A key drawn on paper lies in a drawer. At the arrow\'s end a thief holds two identical keys and reads a letter"),
         "caption": ("종이에 적어 서랍에 두면 도둑이 베껴요.", "Write it on paper and leave it in a drawer, and a thief copies it."),
         "small": ('열쇠가 금고 밖에 있으면 언젠가는 베껴져요. 그러면 <a href="encryption-ko.html">편지 봉인</a>이 소용없어요.',
                   'A key that lives outside the safe gets copied someday. Then the <a href="encryption-en.html">seal on the letter</a> means nothing.')},
        {"svg": P3, "hero": True, "alt": ("큰 쇠금고. 안쪽 창으로 황금 열쇠가 보이고 '열쇠는 안에서 안 나와요'. 내가 편지를 앞 창구에 넣고, 반대쪽으로 봉인된 편지가 나와 경비가 받는다", "A big iron safe. Through a window inside, a golden key — the key never leaves. I drop a letter into the front slot, and a sealed letter comes out the other side into a guard\'s hands"),
         "caption": ("HSM은 열쇠를 만들고 쓰는 쇠금고예요. 열쇠는 밖으로 절대 안 나와요.", "An HSM is an iron safe that makes and uses keys. The key never, ever comes out."),
         "small": ("편지를 창구에 넣으면 금고가 안에서 봉인해서 돌려줘요. 나도 열쇠를 못 봐요 — 그래서 도둑도 못 베껴요.", "Drop a letter in the slot and the safe seals it inside and hands it back. Even I never see the key — so no thief can copy it."),
         "tricks": (4, [
             (FORGE_I, ("안에서 만들어요", "Made inside"), ("열쇠는 금고 안에서 태어나요", "the key is born inside the safe"), "warm"),
             (STAY_I, ("밖으로 안 나와요", "Never comes out"), ("나도, 도둑도 못 봐요", "not me, not the thief"), "warm"),
             (SLOT_I, ("창구로 주고받아요", "Through the slot"), ("편지를 넣으면 봉인해서 돌려줘요", "letter in, sealed letter out"), "calm"),
             (TAMPER_I, ("억지로 열면 부숴요", "Forced open, it breaks the key"), ("도둑 손엔 빈 상자", "the thief gets an empty box")),
         ])},
        {"svg": P4, "alt": ("왼쪽: 도둑이 망치로 금고를 내리치자 금이 가고 안의 열쇠가 두 조각으로 부서진다. 오른쪽: 열쇠 목록 — 편지 열쇠·도장 열쇠·창고 열쇠마다 만든 날과 바꾸는 날", "Left: a thief hammers the safe; it cracks and the key inside snaps in two. Right: a key ledger listing the letter key, seal key and storeroom key, each with the day it was made and the day it gets swapped"),
         "caption": ("억지로 열면 스스로 열쇠를 부숴요. 열쇠 목록엔 바꾸는 날이 적혀 있어요.", "Force it open and it destroys its own key. The key ledger says when each key gets swapped."),
         "small": ("도둑이 망치로 열어도 남는 건 빈 상자예요. 그리고 열쇠는 오래 쓰지 않아요 — 바꾸는 날이 오면 새 열쇠를 만들고 옛 열쇠는 버려요.", "Even hammered open, all that is left is an empty box. And no key is used forever — on swap day a new key is made and the old one retired.")},
        {"svg": P5, "alt": ("쇠금고에서 화살표 두 개: 하나는 봉인 편지로, 하나는 빨간 도장이 찍힌 인증서로. 점선 건너편엔 비밀 쪽지가 든 나무 상자 — 열쇠를 만들진 않아요", "Two arrows from the iron safe: one to a sealed letter, one to a certificate with a red seal. Across a dotted line, a wooden box of secret notes — it does not make keys"),
         "caption": ("쇠금고 열쇠로 편지도 봉인하고 성의 도장도 찍어요.", "The safe\'s keys seal letters and stamp the castle\'s seal."),
         "small": ('<a href="pki-ko.html">성의 도장</a>도 이 열쇠로 찍어요. <a href="secrets-ko.html">비밀 쪽지 상자</a>는 비밀번호를 보관할 뿐, 열쇠를 만들진 않아요.',
                   'The <a href="pki-en.html">castle seal</a> is stamped with these keys too. The <a href="secrets-en.html">secret-note box</a> only stores passwords — it does not make keys.')},
    ],
    "summary": (("<b>HSM</b> = 열쇠를 <b>안에서 만들고, 안에서만 쓰고, 절대 밖으로 안 내보내는</b> 쇠금고. 억지로 열면 스스로 열쇠를 부숴요. <b>열쇠 목록(KMS)</b>이 어떤 열쇠를 언제 바꿀지 관리해요.",
                 "An <b>HSM</b> = an iron safe that <b>makes keys inside, uses them only inside, and never lets them out</b>. Forced open, it destroys its own key. The <b>key ledger (KMS)</b> manages which key gets swapped when."),
                ("HSM = Hardware Security Module. 암호 키를 생성·보관·사용하는 전용 하드웨어로, 키가 장치 밖으로 나오지 않고 물리적 침입을 감지하면 키를 지워요(탬퍼 방지). KMS(Key Management Service)는 그 위에서 키의 생성·로테이션·폐기와 누가 쓸 수 있는지를 관리해요.",
                 "Hardware Security Module: dedicated hardware that generates, stores and uses cryptographic keys without ever exporting them, and wipes them if it detects physical tampering. A Key Management Service (KMS) sits on top to manage creation, rotation, retirement and who may use each key.")),
    "glossary": [
        ("HSM", "HSM (hardware security module)", ("열쇠를 만드는 쇠금고.", "The iron safe that makes keys."), ("열쇠는 안에서 태어나고, 안에서만 일하고, 밖으로 안 나와요.", "Keys are born inside, work only inside, and never come out.")),
        ("KMS", "KMS (key management service)", ("열쇠 목록.", "The key ledger."), ("어떤 열쇠가 있고, 누가 쓰고, 언제 바꾸는지 적어둔 장부. 쇠금고를 뒤에 두고 일해요.", "Which keys exist, who may use them, when they get swapped. Works with the safe behind it.")),
        ("키 생성·보관·폐기", "Key generation · storage · destruction", ("열쇠의 한평생.", "A key\'s whole life."), ("만들고, 보관하고, 다 쓰면 부숴요 — 전부 금고 안에서.", "Made, kept, and broken when done — all inside the safe.")),
        ("키 로테이션", "Key rotation", ("열쇠 바꾸는 날.", "Swap day."), ("같은 열쇠를 오래 쓰지 않아요. 새 열쇠를 만들고 옛 열쇠는 폐기해요.", "No key is used forever. A new one is made and the old one retired.")),
        ("탬퍼 방지", "Tamper resistance", ("억지로 열면 부숴요.", "Forced open, it breaks the key."), ("망치로 열어도 남는 건 빈 상자. 열쇠가 스스로 사라져요.", "Hammer it open and all that is left is an empty box; the key erases itself.")),
        ("루트 키", "Root key / master key", ("열쇠들의 열쇠.", "The key to the keys."), ("다른 열쇠를 봉인하는 제일 큰 열쇠. 이것만은 꼭 쇠금고 안에.", "The biggest key, which seals the other keys. This one above all lives in the safe.")),
        ("인증서", "Certificate", ("성의 도장.", "The castle seal."), ('도장 찍는 열쇠도 쇠금고 안에서 써요. → <a href="pki-ko.html">성의 도장과 도장 관리소</a>', 'The key that stamps the seal is used inside the safe too. → <a href="pki-en.html">the castle seal and the seal office</a>')),
        ("시크릿과의 차이", "Secrets vs. keys", ("쪽지 상자 ≠ 쇠금고.", "Note box ≠ iron safe."), ('쪽지 상자는 비밀번호를 꺼내 줘요. 쇠금고는 열쇠를 절대 안 꺼내 줘요. → <a href="secrets-ko.html">비밀 쪽지 상자</a>', 'The note box hands you the password. The safe never hands you the key. → <a href="secrets-en.html">the secret-note box</a>')),
    ],
}
