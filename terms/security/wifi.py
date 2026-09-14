from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
MAID = dict(hat=None, shirt="#7B3FA0")
ANTENNA = '<path d="M50 4 l14 -22" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/><circle cx="64" cy="-18" r="4" fill="var(--accent)"/>'


def mailbox(x, y, s=1.0, color="#4A5A72", lock=False, dashed=False, cloth=False):
    dash = ' stroke="var(--bad)" stroke-width="3" stroke-dasharray="7 5"' if dashed else ""
    lk = '<rect x="-8" y="30" width="16" height="13" rx="2" fill="#E9B44C"/><path d="M-4 30 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if lock else ""
    cl = '<path d="M-40 -6 h80 v34 q-10 8 -20 0 q-10 8 -20 0 q-10 8 -20 0 q-10 8 -20 0z" fill="var(--stone)" opacity="0.95"/>' if cloth else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="{color}"{dash}/><rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/>'
            f'<path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/>{lk}{cl}</g>')


def waves(x, y, s=1.0, color="var(--accent)", rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            + "".join(f'<path d="M0 {-r} a{r} {r} 0 0 1 0 {2 * r}" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>' for r in (12, 22, 32)) + "</g>")


def letter(x, y, s=1.0, sealed=False, scribble=False, rot=0):
    sl = '<rect x="22" y="12" width="16" height="13" rx="2" fill="#E9B44C"/><path d="M26 12 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if sealed else ""
    sc = '<path d="M8 14 q6 -8 12 0 t12 0 t12 0 t12 0 M8 26 q6 -8 12 0 t12 0 t12 0" stroke="var(--bad)" stroke-width="2" fill="none"/>' if scribble else '<path d="M0 2 L30 22 L60 2" stroke="#C9A86A" stroke-width="2" fill="none"/>'
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="60" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{sc}{sl}</g>'


def badge(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-10" width="28" height="20" rx="3" fill="#5B8DEF"/><circle cx="-6" cy="0" r="4" fill="{SKIN}"/><path d="M2 -3 h8 M2 3 h8" stroke="#FFF" stroke-width="2"/></g>'


def tunnel(x1, x2, y, depth=40):
    d = f'M{x1} {y} C{x1} {y + depth} {x2} {y + depth} {x2} {y}'
    return (f'<path d="{d}" stroke="var(--good)" stroke-width="28" fill="none" stroke-linecap="round" stroke-dasharray="4 10" opacity="0.6"/>'
            f'<path d="{d}" stroke="#3A2A1E" stroke-width="22" fill="none" stroke-linecap="round"/>')


# 1. 복도로 가는 편지 vs 공중으로 던지는 편지
P1 = svg(300, sky(300) + castle(20, 110, 0.42) + '<path d="M400 30 v240" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + person(230, 140, s=0.7, face=SMILE, **MAID) + letter(283, 190, 0.6) + person(320, 140, s=0.7, **ME)
         + label(300, 262, "⟦복도에서 손에서 손으로|hand to hand, down the hall⟧", 11, "var(--muted)")
         + person(460, 130, s=0.75, **ME) + letter(540, 70, 0.8, rot=-15) + waves(600, 92, 0.5)
         + '<path d="M592 96 Q640 60 668 148" stroke="var(--bad)" stroke-width="2.5" fill="none" stroke-dasharray="6 5"/>'
         + person(650, 150, s=0.8, face=MASK, extra=ANTENNA)
         + label(600, 262, "⟦공중으로 던지면 누구나 주워요|thrown in the air, anyone can catch it⟧", 11, "var(--muted)")
         + label(380, 290, "⟦보이지 않는 편지가 공중에 날아다녀요|invisible letters fly through the air⟧", 12, "var(--ink)", cls="d"))

# 2. 광장의 공짜 우체통 — 어느 게 진짜?
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(200, 95, "⟦공짜 우체통|FREE MAILBOX⟧", 12, "var(--ink)", cls="d") + mailbox(200, 110, 1.0, "#5B8DEF") + waves(246, 130, 0.5)
         + label(200, 225, "⟦진짜 광장 우체통|the real plaza mailbox⟧", 11, "var(--ink)")
         + bubble(560, 10, 160, 32, "⟦다 내 거야|all mine⟧", 10, "var(--panel)", "var(--bad)", "left")
         + person(505, 60, s=0.7, face=MASK, extra=ANTENNA)
         + label(480, 95, "⟦공짜 우체통|FREE MAILBOX⟧", 12, "var(--ink)", cls="d") + mailbox(480, 110, 1.0, "#5B8DEF", dashed=True) + waves(526, 130, 0.5, "var(--bad)")
         + label(510, 225, "⟦도둑이 세운 가짜 — 똑같이 생겼어요|a fake the thief set up — looks the same⟧", 10, "var(--bad)")
         + person(340, 150, s=0.75, face=FROWN + SWEAT, hat=None, shirt="#4A5A72") + label(366, 258, "⟦어느 게 진짜지?|which one is real?⟧", 12, "var(--ink)")
         + label(380, 290, "⟦가짜 우체통에 넣은 편지는 도둑 손으로 가요|letters in the fake box go straight to the thief⟧", 12, "var(--ink)", cls="d"))

# 3. 우체통마다 자물쇠, 성엔 신분증, 손님은 따로, 광장에선 땅굴 (hero)
P3 = svg(360, sky(360)
         + person(40, 150, s=0.65, face=SMILE, **GUARD) + badge(100, 195, 0.9) + mailbox(140, 120, 1.0, "#4A5A72", lock=True) + waves(186, 140, 0.5)
         + label(140, 268, "⟦성 우체통|castle mailbox⟧", 12, "var(--ink)", cls="d") + label(140, 286, "⟦봉인 자물쇠 + 신분증|sealed lock + ID badge⟧", 10, "var(--muted)")
         + '<path d="M260 70 v180" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 6"/>'
         + mailbox(380, 120, 1.0, "var(--accent)", lock=True) + waves(426, 140, 0.5)
         + label(380, 268, "⟦손님 우체통|guest mailbox⟧", 12, "var(--ink)", cls="d") + label(380, 286, "⟦성 복도와 리본으로 나눠요|split from the castle halls by a ribbon⟧", 10, "var(--muted)")
         + tunnel(555, 640, 212, 30) + person(540, 150, s=0.65, **ME) + mailbox(620, 120, 1.0, "#5B8DEF", lock=True) + waves(666, 140, 0.5)
         + label(620, 268, "⟦광장 우체통|plaza mailbox⟧", 12, "var(--ink)", cls="d") + label(620, 286, "⟦봉인된 땅굴로만 보내요|send only through the sealed tunnel⟧", 10, "var(--muted)")
         + label(380, 320, "⟦우체통마다 자물쇠, 성 우체통엔 신분증, 손님은 따로, 광장에선 땅굴|a lock on every box, a badge for the castle box, guests apart, a tunnel in the plaza⟧", 12, "var(--ink)", cls="d")
         + label(380, 348, "⟦공중에 던져도 봉인된 편지는 아무도 못 읽어요|thrown in the air, a sealed letter reads as nothing⟧", 11, "var(--muted)"))

# 4. 자물쇠는 편지를, 신분증은 사람을
P4 = svg(320, sky(320) + '<path d="M400 30 v260" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 6"/>'
         + bubble(200, 20, 200, 34, "⟦열쇠가 없어… 읽을 수 없어|no key… can\'t read it⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + person(60, 120, s=0.7, **ME) + letter(150, 80, 0.8, sealed=True, rot=-10) + '<path d="M200 96 Q240 60 280 130" stroke="var(--bad)" stroke-width="2.5" fill="none" stroke-dasharray="6 5"/>'
         + person(270, 140, s=0.75, face=MASK, extra=ANTENNA) + letter(300, 235, 0.7, sealed=True, scribble=True)
         + label(200, 285, "⟦봉인 자물쇠: 주워도 못 읽어요|sealed lock: catch it, still can\'t read it⟧", 11, "var(--ink)")
         + label(580, 60, "⟦성 우체통: 암호말 대신 신분증|castle mailbox: a badge instead of a password⟧", 11, "var(--ink)", cls="d")
         + mailbox(480, 110, 1.0, "#4A5A72") + label(480, 90, "⟦암호말: 사과|password: apple⟧", 10, "var(--muted)")
         + label(480, 225, "⟦암호말 하나를 다 같이 써요|one password everyone shares⟧", 10, "var(--ink)") + label(480, 243, "⟦도둑도 금방 알아요|the thief learns it fast⟧", 10, "var(--bad)")
         + mailbox(650, 110, 1.0, "#4A5A72", lock=True) + badge(600, 180, 0.8) + badge(700, 180, 0.8)
         + label(650, 225, "⟦사람마다 다른 신분증|a different badge for each⟧", 10, "var(--ink)") + label(650, 243, "⟦나간 사람 건 지워요|leavers get theirs erased⟧", 10, "var(--good)")
         + label(380, 308, "⟦자물쇠는 편지를, 신분증은 사람을 지켜요|the lock guards the letter, the badge guards the door⟧", 12, "var(--ink)", cls="d"))

# 5. 이름표 숨기기는 천 한 장 — 소용없어요 / 점검표
ROWS = (("✓", "⟦봉인 자물쇠|sealed lock⟧", "var(--good)"), ("✓", "⟦성 우체통엔 신분증|badge for the castle box⟧", "var(--good)"), ("✓", "⟦손님 우체통은 따로|guest box apart⟧", "var(--good)"),
        ("✓", "⟦광장에선 땅굴|tunnel in the plaza⟧", "var(--good)"), ("×", "⟦이름표 천으로 덮기|cloth over the name⟧", "var(--bad)"))
P5 = svg(300, sky(300)
         + bubble(240, 20, 220, 34, "⟦천을 덮어도 다 보여요|cloth or not, I see it all⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + mailbox(150, 110, 1.0, "#4A5A72", lock=True, cloth=True) + waves(196, 130, 0.5) + person(300, 130, s=0.8, face=MASK, extra=ANTENNA)
         + label(150, 240, "⟦우체통 이름표 숨기기|hiding the mailbox name⟧", 11, "var(--ink)") + label(150, 258, "⟦= 천 한 장. 소용없어요|= a cloth. does nothing⟧", 10, "var(--bad)")
         + '<rect x="470" y="40" width="250" height="200" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="470" y="40" width="250" height="28" rx="8" fill="#C9A86A"/>'
         + label(595, 59, "⟦우체통 점검표|MAILBOX CHECKLIST⟧", 12, "#142033", cls="d")
         + "".join(label(490, 96 + i * 30, m, 14, c, "start", cls="d") + label(512, 96 + i * 30, t, 12, "#142033", "start") for i, (m, t, c) in enumerate(ROWS))
         + label(380, 288, "⟦숨기는 게 아니라 봉인하는 거예요|don\'t hide it — seal it⟧", 13, "var(--ink)", cls="d"))

LOCK_I = icon('<rect x="10" y="18" width="44" height="28" rx="8" fill="#4A5A72"/><rect x="18" y="26" width="28" height="14" rx="2" fill="#FFF8E7"/><rect x="26" y="40" width="12" height="10" rx="2" fill="#E9B44C"/><path d="M29 40 v-4 a3 3 0 0 1 6 0 v4" stroke="#E9B44C" stroke-width="2" fill="none"/>')
BADGE_I = icon(f'<rect x="10" y="16" width="44" height="32" rx="4" fill="#5B8DEF"/><circle cx="24" cy="32" r="7" fill="{SKIN}"/><path d="M36 27 h12 M36 37 h12" stroke="#FFF" stroke-width="3"/>')
GUEST_I = icon('<rect x="6" y="22" width="22" height="16" rx="5" fill="#4A5A72"/><rect x="36" y="22" width="22" height="16" rx="5" fill="var(--accent)"/><path d="M32 10 v44" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/>')
TUNNEL_I = icon('<path d="M10 24 C10 54 54 54 54 24" stroke="var(--good)" stroke-width="16" fill="none" stroke-linecap="round" stroke-dasharray="3 6" opacity="0.6"/><path d="M10 24 C10 54 54 54 54 24" stroke="#3A2A1E" stroke-width="11" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "wifi", "order": 106,
    "title": ("마을 광장의 공짜 우체통", "The Free Mailbox in the Village Square"),
    "h1": ("<em>Wi-Fi 보안</em>이 뭐예요?", "What is <em>Wi-Fi Security</em>?"),
    "sub": ("무선 네트워크 보안(Wi-Fi Security)을 공중으로 던져 보내는 편지와 마을 광장의 공짜 우체통 이야기로 풀어봤어요.",
            "Wireless network security, told as a story about letters thrown through the air and a free mailbox in the village square."),
    "panels": [
        {"svg": P1, "alt": ("왼쪽: 성 안에서 두 사람이 편지를 손에서 손으로 건넴. 오른쪽: 내가 편지를 공중에 던지자 안테나 달린 도둑이 받으려 함", "Left: inside the castle, two people pass a letter hand to hand. Right: I throw a letter into the air and a thief with an antenna reaches to catch it"),
         "caption": ("성 안 편지는 복도로 가요. 공중으로 던지는 편지는 누구나 주울 수 있어요.", "Castle letters travel down the hall. A letter thrown through the air can be caught by anyone."),
         "small": ("선 없이 보내는 편지는 눈에 안 보이지만 공중에 날아다녀요. 안테나만 있으면 옆집 도둑도 받아요.", "A wireless letter is invisible, but it flies through the air. Anyone with an antenna — even the thief next door — can catch it.")},
        {"svg": P2, "alt": ("광장에 '공짜 우체통' 두 개. 하나는 진짜, 하나는 도둑이 뒤에 숨어 세운 똑같이 생긴 가짜. 나는 땀 흘리며 어느 게 진짜인지 모름", "Two free mailboxes in the square. One is real; the other, identical, was set up by a thief hiding behind it. I sweat, unable to tell which is which"),
         "caption": ("광장의 공짜 우체통은 도둑이 세운 가짜일 수도 있어요.", "The free mailbox in the square might be a fake the thief put up."),
         "small": ('이름도 생김새도 똑같아요. 가짜에 넣은 편지는 <a href="mitm-ko.html">중간에서 뜯어보는 배달부</a> 손으로 가요.',
                   'Same name, same look. Letters dropped in the fake go to the <a href="mitm-en.html">courier who opens them on the way</a>.')},
        {"svg": P3, "hero": True, "alt": ("세 우체통: 성 우체통은 자물쇠에 경비가 신분증을 확인, 손님 우체통은 리본으로 따로, 광장 우체통엔 봉인된 땅굴로 편지를 보냄", "Three mailboxes: the castle box has a lock and a guard checking badges, the guest box sits apart behind a ribbon, and the plaza box is reached only through a sealed tunnel"),
         "caption": ("우체통마다 자물쇠, 성 우체통엔 신분증, 손님은 따로, 광장에선 땅굴.", "A lock on every box, a badge for the castle box, guests apart, a tunnel in the square."),
         "small": ('봉인 자물쇠(<a href="encryption-ko.html">봉인 편지</a>)는 주워도 못 읽게 해요. 성 우체통은 <a href="password-ko.html">암호말</a> 대신 <a href="nac-ko.html">신분증</a>을 봐요. 손님은 <a href="vlan-ko.html">리본</a>으로 나누고, 광장에선 <a href="vpn-ko.html">봉인된 땅굴</a>로만 보내요.',
                   'The sealed lock (<a href="encryption-en.html">a sealed letter</a>) makes a caught letter unreadable. The castle box checks a <a href="nac-en.html">badge</a> instead of a <a href="password-en.html">password</a>. Guests are kept apart by a <a href="vlan-en.html">ribbon</a>, and in the square you send only through the <a href="vpn-en.html">sealed tunnel</a>.'),
         "tricks": (4, [
             (LOCK_I, ("봉인 자물쇠", "Sealed lock"), ("주워도 못 읽어요", "caught, still unreadable"), "calm"),
             (BADGE_I, ("신분증", "A badge each"), ("암호말 하나 말고", "not one shared password")),
             (GUEST_I, ("손님은 따로", "Guests apart"), ("리본 너머로만", "beyond the ribbon only")),
             (TUNNEL_I, ("광장에선 땅굴", "Tunnel in the square"), ("공짜 우체통은 못 믿어요", "never trust the free box"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 봉인된 편지를 던지자 도둑이 주웠지만 안은 낙서뿐 — '열쇠가 없어, 읽을 수 없어'. 오른쪽: 암호말 '사과' 하나를 다 같이 쓰는 우체통과, 사람마다 다른 신분증을 보는 우체통", "Left: a sealed letter is thrown, the thief catches it but sees only scribbles — no key, can\'t read it. Right: a mailbox where everyone shares the password apple, versus one that checks a different badge for each person"),
         "caption": ("자물쇠는 편지를 지키고, 신분증은 문을 지켜요.", "The lock guards the letter; the badge guards the door."),
         "small": ("암호말 하나를 다 같이 쓰면 도둑도 금방 알아요. 신분증은 사람마다 다르고, 나간 사람 건 바로 지워요.", "One password shared by all is soon known to the thief too. A badge is different for each person, and a leaver\'s badge is erased at once.")},
        {"svg": P5, "alt": ("천으로 덮은 우체통에서도 전파가 퍼지고, 안테나 든 도둑이 '천을 덮어도 다 보여요'. 옆의 점검표: 봉인 자물쇠 ✓, 신분증 ✓, 손님 따로 ✓, 땅굴 ✓, 천 덮기 ×", "Waves still spread from a mailbox covered by a cloth, and the thief with an antenna says: cloth or not, I see it all. Beside it a checklist: sealed lock ✓, badge ✓, guests apart ✓, tunnel ✓, cloth over the name ×"),
         "caption": ("우체통 이름표를 숨기는 건 천 한 장이에요. 숨기지 말고 봉인하세요.", "Hiding the mailbox name is just a cloth. Don\'t hide it — seal it."),
         "small": ('안테나 있는 도둑은 천 너머 전파를 다 봐요. 상점과 주고받는 편지는 <a href="tls-ko.html">봉인 약속</a>이 한 겹 더 지켜 주고요.',
                   'A thief with an antenna sees the waves right through the cloth. And letters to and from the shop get one more layer from the <a href="tls-en.html">sealing promise</a>.')},
    ],
    "summary": (("<b>Wi-Fi 보안</b> = 공중으로 던지는 편지를 <b>봉인 자물쇠</b>로 못 읽게 하고, 성 우체통엔 <b>신분증</b>, 손님은 <b>따로</b>, 광장의 <b>공짜 우체통</b>은 믿지 말고 <b>봉인된 땅굴</b>로만 보내는 것.",
                 "<b>Wi-Fi security</b> = make letters thrown through the air unreadable with a <b>sealed lock</b>, check a <b>badge</b> at the castle box, keep guests <b>apart</b>, and never trust the <b>free mailbox</b> in the square — send only through the <b>sealed tunnel</b>."),
                ("Wi-Fi Security. 무선 신호는 누구나 수신할 수 있어서 WPA3 같은 암호화, 802.1X 개인 인증, 게스트 망 분리, 공용 와이파이에서는 VPN이 필요해요. 이블 트윈(가짜 AP)은 정상 AP와 똑같이 보여요.",
                 "Anyone can receive a wireless signal, so you need encryption like WPA3, per-user 802.1X authentication, a separated guest network, and a VPN on public Wi-Fi. An evil twin (rogue AP) looks exactly like the real one.")),
    "glossary": [
        ("WPA2 · WPA3", "WPA2 / WPA3", ("우체통 봉인 자물쇠.", "The mailbox\'s sealing lock."), ('공중에 던져도 못 읽게 해요. 새 자물쇠(3)가 더 튼튼해요. → <a href="encryption-ko.html">봉인 편지</a>', 'Makes a caught letter unreadable. The newer lock (3) is sturdier. → <a href="encryption-en.html">the sealed letter</a>')),
        ("공개 와이파이", "Public Wi-Fi", ("광장의 공짜 우체통.", "The free mailbox in the square."), ("누가 세웠는지 몰라요. 봉인된 땅굴 없이는 편지를 넣지 마세요.", "Nobody knows who put it up. Never drop a letter in without the sealed tunnel.")),
        ("악성 AP · 이블 트윈", "Rogue AP / evil twin", ("도둑이 세운 가짜 우체통.", "The thief\'s fake mailbox."), ('이름도 생김새도 똑같아요. → <a href="mitm-ko.html">편지를 중간에서 뜯어보는 배달부</a>', 'Same name, same look. → <a href="mitm-en.html">the courier who opens letters on the way</a>')),
        ("802.1X", "802.1X", ("사람마다 신분증.", "A badge for each person."), ('암호말 하나 대신 사람마다 확인해요. → <a href="nac-ko.html">복도 구멍마다 문지기</a>', 'Checks each person instead of one shared password. → <a href="nac-en.html">a doorkeeper at every hole in the hall</a>')),
        ("게스트 네트워크", "Guest network", ("손님 우체통.", "The guest mailbox."), ('리본 너머 성 복도엔 못 닿아요. → <a href="vlan-ko.html">색 리본으로 나눈 복도</a>', 'Can\'t reach the castle halls past the ribbon. → <a href="vlan-en.html">halls divided by colored ribbons</a>')),
        ("VPN", "VPN", ("봉인된 땅굴.", "The sealed tunnel."), ('광장에서도 성까지 아무도 못 엿봐요. → <a href="vpn-ko.html">봉인된 땅굴</a>', 'From the square to the castle with no one peeking. → <a href="vpn-en.html">the sealed tunnel</a>')),
        ("중간자 공격", "Man-in-the-middle", ("중간에서 뜯어보기.", "Opening it on the way."), ('가짜 우체통이 하는 짓이에요. → <a href="mitm-ko.html">중간에서 뜯어보는 배달부</a>', 'What the fake mailbox does. → <a href="mitm-en.html">the courier in the middle</a>')),
        ("SSID 숨기기", "Hiding the SSID", ("우체통에 천 덮기.", "A cloth over the mailbox."), ("전파는 그대로 퍼져요. 안테나 있는 도둑은 다 봐요 — 보안이 아니에요.", "The waves still spread. A thief with an antenna sees it all — this is not security.")),
    ],
}
