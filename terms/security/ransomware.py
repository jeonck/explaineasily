from _draw import *

CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
DOORS = (("⟦그림책 방|Books⟧", False), ("⟦편지 방|Mail⟧", False), ("⟦장부 방|Ledgers⟧", False), ("⟦사진 방|Photos⟧", False), ("⟦창고|Storage⟧", False))


def chest(x, y, s=1.0, locked=False, open_lid=False, grey=False):
    body = "var(--stone)" if grey else "#8B5E3C"
    lid = ('<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22" transform="rotate(-40 -30 -14)"/>' if open_lid
           else f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="{"var(--stone-dark)" if grey else "#5A3B22"}"/>')
    lock = ('<rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--bad)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--bad)" stroke-width="4" fill="none"/>' if locked else "")
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="{body}"/>{lid}{lock}</g>'


def note(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="90" rx="3" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/>'
            f'{label(65, 26, "⟦열쇠 갖고 싶으면|Want the key?⟧", 12, "var(--bad)")}{label(65, 48, "⟦금화 100개|100 gold coins⟧", 14, "#142033", cls="d")}'
            f'{label(65, 70, "⟦3일 안에|within 3 days⟧", 11, "var(--bad)")}</g>')


def key(x, y, s=1.0, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


# 1. 방마다 상자가 있다
P1 = svg(300, corridor(300, DOORS, marks=False)
         + "".join(chest(x, 240, 0.8, open_lid=True) for x in (102, 242, 382, 522, 662))
         + label(380, 285, "⟦성이 돌아가려면 매일 열어야 해요|the castle runs on opening them every day⟧", 13, "#F5E6B8"))

# 2. 도둑이 자물쇠를 채운다
P2 = svg(300, corridor(300, DOORS, night_mode=True, marks=False)
         + "".join(chest(x, 240, 0.8, locked=True) for x in (102, 242, 382, 522, 662))
         + person(300, 130, s=0.8, face=MASK, extra='<g transform="translate(66,70)"><rect x="-8" y="-6" width="16" height="12" rx="2" fill="var(--bad)"/><path d="M-5 -6 V-10 a5 5 0 0 1 10 0 V-6" stroke="var(--bad)" stroke-width="3" fill="none"/></g>')
         + note(480, 40, 0.8)
         + label(380, 290, "⟦훔쳐가는 게 아니라 잠가버려요|nothing is taken — it\'s all locked⟧", 13, "#F5E6B8"))

# 3. 랜섬웨어 = 잠그고 열쇠값 (hero)
P3 = svg(340, '<rect width="760" height="340" fill="var(--bad-soft)"/>'
         + "".join(chest(x, 200, 1.0, locked=True) for x, in ((90,), (200,), (310,)))
         + note(60, 40, 1.0)
         + person(400, 140, s=0.9, face=FROWN + SWEAT, **CLERK) + label(430, 270, "⟦성이 멈췄어요|the castle has stopped⟧", 13, "var(--bad)", cls="d")
         + '<path d="M480 60 L620 60" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 6"/>'
         + person(620, 30, s=0.8, face=MASK, extra=key(76, 70, 0.9)) + label(650, 160, "⟦열쇠는 도둑만|only the thief has the key⟧", 12, "var(--muted)")
         + chest(560, 240, 0.7, grey=True) + '<path d="M560 200 L620 260" stroke="var(--bad)" stroke-width="3" stroke-dasharray="5 5"/>' + label(620, 300, "⟦복사본도 훔쳐 가요|copies get stolen too⟧", 12, "var(--bad)")
         + label(380, 328, "⟦돈을 내도 열쇠를 준다는 보장은 없어요|paying doesn\'t guarantee the key comes back⟧", 13, "var(--muted)"))

# 4. 여분 상자를 멀리 두면
FAR = ('<g transform="translate(600,120)"><rect x="-70" y="0" width="140" height="90" fill="var(--panel)" stroke="var(--good)" stroke-width="4"/><path d="M-80 0 L0 -40 L80 0 Z" fill="var(--good)"/>'
       + chest(-35, 55, 0.6) + chest(0, 55, 0.6) + chest(35, 55, 0.6) + label(0, 110, "⟦멀리 있는 여분 창고|the spare depot, far away⟧", 12, "var(--good)") + "</g>")
P4 = svg(320, sky(320) + chest(90, 140, 0.9, locked=True) + chest(180, 140, 0.9, locked=True)
         + '<path d="M240 140 L400 140" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 6"/><path d="M390 130 L402 140 L390 150" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(320, 125, "⟦매일 복사본을|a copy every day⟧", 12, "var(--good)")
         + '<rect x="300" y="60" width="8" height="200" fill="var(--stone-dark)"/>' + label(304, 285, "⟦복도 나누기|the hallway split⟧", 11, "var(--muted)")
         + FAR + dog(440, 250, 0.7, bark=True) + label(440, 300, "⟦자물쇠 채우는 손을 물어요|bites the hand that locks⟧", 11, "var(--muted)")
         + label(135, 250, "⟦열쇠값? 필요 없어요|the key? not needed⟧", 13, "var(--good)", cls="d"))

# 5. 돈을 내도 열쇠가 온다는 보장은 없다
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + '<g transform="translate(90,110)"><rect x="-40" y="-24" width="80" height="48" rx="6" fill="#E9B44C"/>' + label(0, 6, "⟦금화 100|100 gold⟧", 13, "#142033") + "</g>"
         + '<path d="M140 110 L220 110" stroke="var(--muted)" stroke-width="3"/><path d="M210 100 L222 110 L210 120" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + key(270, 110, 1.0, "var(--stone)") + label(270, 150, "?", 30, "var(--bad)", cls="d")
         + chest(150, 220, 0.8, locked=True) + chest(240, 220, 0.8, open_lid=True)
         + label(190, 275, "⟦열쇠가 안 오거나 반만 열려요|no key comes, or only half opens⟧", 12, "var(--bad)")
         + '<g transform="translate(560,110)"><rect x="-60" y="0" width="120" height="70" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M-70 0 L0 -34 L70 0 Z" fill="var(--stone)"/>'
         + chest(-25, 45, 0.5, locked=True) + chest(25, 45, 0.5, locked=True) + label(0, 92, "⟦복사본 창고까지|even the spare depot⟧", 11, "var(--bad)") + "</g>"
         + person(660, 130, s=0.6, face=MASK)
         + label(570, 255, "⟦성이랑 이어져 있으면 같이 잠겨요|connected to the castle, it gets locked too⟧", 11, "var(--muted)")
         + label(570, 280, "⟦그래서 떼어 두고, 열리는지 미리 시험해요|so keep it apart, and test that it opens⟧", 11, "var(--muted)"))

LOCK_I = icon('<rect x="16" y="28" width="32" height="26" rx="5" fill="var(--bad)"/><path d="M22 28 V20 a10 10 0 0 1 20 0 V28" stroke="var(--bad)" stroke-width="5" fill="none"/>')
NOTE_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/><rect x="22" y="22" width="20" height="3" fill="var(--bad)"/><rect x="22" y="32" width="16" height="3" fill="var(--bad)"/><circle cx="32" cy="44" r="5" fill="#E9B44C"/>')
DOOR_I = icon('<rect x="8" y="16" width="48" height="34" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M8 18 L32 36 L56 18" stroke="var(--bad)" stroke-width="3" fill="none"/>')
COPY_I = icon('<rect x="12" y="20" width="26" height="22" rx="3" fill="#8B5E3C"/><rect x="26" y="28" width="26" height="22" rx="3" fill="var(--stone)"/><path d="M44 22 l10 -10 M54 12 l-4 0 l0 4" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "ransomware", "order": 38,
    "title": ("상자마다 채운 도둑의 자물쇠", "The Thief\'s Lock on Every Chest"),
    "h1": ("<em>랜섬웨어</em>가 뭐예요?", "What is <em>Ransomware</em>?"),
    "sub": ("랜섬웨어(Ransomware)를 성 안 상자마다 자물쇠를 채우고 열쇠값을 요구하는 도둑 이야기로 풀어봤어요.",
            "Ransomware, told as a story about a thief who locks every chest in the castle and charges for the key."),
    "panels": [
        {"svg": P1, "alt": ("복도 방마다 뚜껑이 열린 나무 상자가 놓여 있음", "An open wooden chest in front of every room along the hallway"),
         "caption": ("성 안 방마다 상자가 있어요.", "Every room in the castle has a chest."),
         "small": ("그림책, 편지, 장부, 사진. 성이 돌아가려면 매일 열어야 해요.", "Books, mail, ledgers, photos. The castle runs on opening them every day.")},
        {"svg": P2, "alt": ("밤에 가면 쓴 도둑이 상자마다 빨간 자물쇠를 채우고 '열쇠 갖고 싶으면 금화 100개' 쪽지를 남김", "At night a masked thief snaps a red padlock on every chest and leaves a note: Want the key? 100 gold coins"),
         "caption": ("도둑이 상자마다 자기 자물쇠를 채워요.", "The thief puts his own lock on every chest."),
         "small": ("훔쳐가는 게 아니라 잠가버려요. 열쇠는 도둑만 갖고 있어요.", "Nothing is taken — it's all locked. Only the thief has the key.")},
        {"svg": P3, "hero": True, "alt": ("잠긴 상자들과 협박 쪽지, 땀 흘리는 직원 '성이 멈췄어요', 멀리서 열쇠를 든 도둑, 회색 복사본 상자를 끌고 가는 점선", "Locked chests and the ransom note; a sweating clerk — the castle has stopped; far off, the thief holding the key; a dotted line dragging a grey copy chest away"),
         "caption": ("랜섬웨어는 내 물건을 잠그고 열쇠값을 요구해요.", "Ransomware locks your things and charges for the key."),
         "small": ("성은 멈춰요. 돈을 내도 열쇠를 준다는 보장은 없어요. 요즘은 잠그기 전에 복사본까지 훔쳐 가요.", "The castle stops. Paying doesn't guarantee a key. These days they steal a copy before locking, too."),
         "tricks": (4, [
             (LOCK_I, ("자물쇠", "The lock"), ("도둑만 여는 봉인 — 암호화", "a seal only the thief opens — encryption")),
             (NOTE_I, ("쪽지", "The note"), ("금화는 코인이에요", "the gold is cryptocurrency"), "warm"),
             (DOOR_I, ("들어온 길", "The way in"), ("가짜 편지, 땅굴 입구, 열린 문", "a fake letter, the tunnel mouth, an open door"), "calm"),
             (COPY_I, ("복사본도 훔쳐요", "Copies stolen too"), ("'안 내면 퍼뜨릴게'", "'pay, or we publish'")),
         ])},
        {"svg": P4, "alt": ("잠긴 상자 옆으로 '매일 복사본을' 화살표가 벽 너머 멀리 있는 여분 창고로 이어지고, 경비견이 짖음", "Beside the locked chests, an arrow — a copy every day — leads past a wall to a spare depot far away; a dog barks"),
         "caption": ("여분 상자를 멀리 두면 열쇠값이 필요 없어요.", "Spare chests far away, and the key doesn't matter."),
         "small": ('매일 복사본을 떨어진 창고에 둬요. 도둑이 거기까지 못 가게 <a href="vlan-ko.html">복도를 나누고</a>, 자물쇠 채우는 손은 <a href="edr-ko.html">경비견</a>이 물어요.',
                   'Copy everything to a depot far away, every day. <a href="vlan-en.html">Split the hallway</a> so the thief can\'t reach it, and let the <a href="edr-en.html">dog</a> bite the hand that locks.')},
        {"svg": P5, "alt": ("왼쪽: 금화 100개를 냈는데 회색 열쇠와 물음표, 상자 하나는 여전히 잠김. 오른쪽: 복사본 창고 상자까지 자물쇠가 채워짐", "Left: 100 gold paid, but a grey key and a question mark — one chest still locked. Right: even the spare depot's chests wear padlocks"),
         "caption": ("돈을 내도 열쇠가 온다는 보장은 없어요.", "Paying doesn't guarantee the key."),
         "small": ("열쇠가 안 오거나 반만 열려요. 복사본 창고가 성과 이어져 있으면 같이 잠겨요. 그래서 떼어 두고, 열리는지 미리 시험해 봐요.", "The key may never come, or open only half. A spare depot still connected to the castle gets locked too — so keep it apart, and test that it opens.")},
    ],
    "summary": (("<b>랜섬웨어</b> = 도둑이 성 안 상자마다 <b>자기 자물쇠</b>를 채우고 <b>열쇠값</b>을 요구하는 것. 훔치는 게 아니라 못 쓰게 해요. 진짜 방어는 <b>여분 상자를 멀리</b> 두는 것.",
                 "<b>Ransomware</b> = a thief puts <b>his own lock</b> on every chest and charges for the <b>key</b>. Nothing is stolen; everything is unusable. The real defense is <b>spare chests far away</b>."),
                ("Ransomware. 2017년 WannaCry가 병원과 공장을 멈춰 세웠어요. 백업은 3-2-1 — 사본 셋, 매체 둘, 하나는 멀리. 그리고 열리는지 꼭 시험해 봐요.",
                 "WannaCry stopped hospitals and factories in 2017. Backups follow 3-2-1: three copies, two kinds of media, one far away. And test that they open.")),
    "glossary": [
        ("암호화", "Encryption", ("도둑의 자물쇠.", "The thief\'s lock."), ('<a href="vpn-ko.html">봉인</a>과 같은 기술인데, 열쇠를 도둑이 가졌어요.', 'The same trick as the <a href="vpn-en.html">seal</a> — but the thief holds the key.')),
        ("협박문", "Ransom note", ("쪽지.", "The note."), ("금화(코인) 얼마를 며칠 안에. 늦으면 값이 올라요.", "So much gold (crypto) within so many days. Late, and the price rises.")),
        ("초기 침입", "Initial access", ("들어온 길.", "The way in."), ('<a href="mfa-ko.html">가짜 편지</a>, <a href="vpn-ko.html">땅굴 입구</a>, <a href="firewall-ko.html">열린 문</a>. 여기서 막는 게 제일 싸요.', 'A <a href="mfa-en.html">fake letter</a>, the <a href="vpn-en.html">tunnel mouth</a>, an <a href="firewall-en.html">open door</a>. Cheapest to stop here.')),
        ("횡적 이동", "Lateral movement", ("방에서 방으로 자물쇠.", "Locks from room to room."), ('상자 하나로 끝나지 않는 이유. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Why it never stops at one chest. → <a href="ndr-en.html">the hallway watcher</a>')),
        ("이중 협박", "Double extortion", ("복사본 훔쳐서 퍼뜨리겠다.", "Steal a copy and threaten to publish."), ("여분 상자가 있어도 돈을 내게 만드는 수법.", "The trick that makes you pay even when you have spares.")),
        ("3-2-1 백업", "3-2-1 backup", ("여분 상자 셋.", "Three spare chests."), ("사본 셋, 매체 둘, 하나는 멀리.", "Three copies, two kinds of media, one far away.")),
        ("오프라인 · 불변 백업", "Offline · immutable backup", ("도둑 손이 안 닿는 창고.", "The depot the thief can\'t reach."), ("성과 떼어 두거나, 아무도 못 고치게 잠근 사본.", "Kept apart from the castle, or locked so nobody can change it.")),
        ("복구 훈련", "Restore drill", ("열리는지 미리 시험.", "Testing that it opens."), ("여분 상자가 있는 것과 열리는 것은 달라요.", "Having a spare and being able to open it are two different things.")),
    ],
}
