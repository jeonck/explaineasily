from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
FRIEND = dict(hat="var(--good)", shirt="var(--good)")
EYE = '<path d="M-14 0 Q0 -10 14 0 Q0 10 -14 0 Z" fill="#FFF" stroke="var(--night)" stroke-width="2"/><circle r="4" fill="var(--night)"/>'


def letter(x, y, text, s=1.0, scrambled=False, locked=False, rot=0):
    ink = "var(--bad)" if scrambled else "#142033"
    lock = ('<g transform="translate(120,60)"><rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--good)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--good)" stroke-width="4" fill="none"/></g>' if locked else "")
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="140" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'{label(70, 34, text, 14 if not scrambled else 13, ink, cls="" if scrambled else "d")}<rect x="16" y="52" width="70" height="4" rx="2" fill="#C9A86A"/>{lock}</g>')


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


def padlock(x, y, s=1.0, color="var(--good)", open_=False):
    sh = '<path d="M-8 -8 V-16 a8 8 0 0 1 16 0" stroke="{c}" stroke-width="4" fill="none"/>' if open_ else '<path d="M-8 -8 V-14 a8 8 0 0 1 16 0 V-8" stroke="{c}" stroke-width="4" fill="none"/>'
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-13" y="-8" width="26" height="20" rx="4" fill="{color}"/>{sh.replace("{c}", color)}</g>'


PLAIN = "⟦사과 두 개 사 와|Buy two apples⟧"
CIPHER = "ㅋ#7@…x!Q"

# 1. 편지는 길 위의 누구나 읽는다
P1 = svg(280, sky(280) + person(50, 100, s=0.9, **ME)
         + letter(150, 70, PLAIN, 0.9)
         + '<path d="M290 110 L520 110" stroke="var(--stone-dark)" stroke-width="8" fill="none" stroke-linecap="round"/>'
         + person(330, 130, s=0.55, hat="var(--accent)", shirt="var(--accent)", face=EYES) + person(420, 130, s=0.55, face=MASK) + person(510, 130, s=0.55, hat="#E9B44C", shirt="#4A5A72", face=EYES)
         + f'<g transform="translate(345,110)">{EYE}</g><g transform="translate(435,110)">{EYE}</g><g transform="translate(525,110)">{EYE}</g>'
         + person(640, 100, s=0.9, face=SMILE, **FRIEND)
         + label(380, 260, "⟦심부름꾼도, 길가의 사람도, 도둑도 읽어요|the runner, the bystander and the thief all read it⟧", 13, "var(--muted)"))

# 2. 봉투에 넣어도 뜯으면 그만
P2 = svg(260, '<rect width="760" height="260" fill="var(--bad-soft)"/>'
         + '<g transform="translate(160,80)"><rect width="150" height="90" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 4 L75 60 L150 4" stroke="var(--line)" stroke-width="3" fill="none"/></g>'
         + label(235, 200, "⟦읽지 마세요|please don\'t read⟧", 12, "var(--muted)")
         + '<path d="M330 125 L400 125" stroke="var(--muted)" stroke-width="3"/><path d="M390 115 L402 125 L390 135" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + person(440, 60, s=0.9, face=MASK) + letter(520, 100, PLAIN, 0.8, rot=6)
         + bubble(480, 10, 220, 34, "⟦사과 두 개 사 오래|buy two apples, it says⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 245, "⟦봉투는 '읽지 마세요'일 뿐, 못 읽게 하진 못해요|an envelope only asks; it can\'t stop anyone⟧", 13, "var(--muted)"))

# 3. 암호화 = 열쇠 없이는 못 읽는 글자 (hero)
P3 = svg(340, sky(340) + person(30, 110, s=0.85, **ME) + key(60, 250, 0.9)
         + letter(110, 60, PLAIN, 0.75) + '<path d="M220 90 L270 90" stroke="var(--good)" stroke-width="3"/><path d="M260 80 L272 90 L260 100" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + letter(280, 60, CIPHER, 0.75, scrambled=True, locked=True)
         + person(400, 150, s=0.7, face=MASK) + label(440, 110, "?", 34, "var(--bad)", cls="d") + label(430, 270, "⟦훔쳐도 못 읽어요|stolen, still unreadable⟧", 12, "var(--bad)")
         + '<path d="M395 90 L520 90" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 6"/>'
         + letter(530, 60, PLAIN, 0.75) + person(650, 110, s=0.85, face=SMILE, **FRIEND) + key(680, 250, 0.9)
         + label(380, 322, "⟦열쇠를 가진 사람만 원래대로 돌려놔요|only someone with the key turns it back⟧", 13, "var(--muted)"))

# 4. 열쇠 두 가지 방식
P4 = svg(320, '<rect width="380" height="320" fill="var(--sky)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + label(190, 34, "⟦같은 열쇠 둘|two matching keys⟧", 15, "var(--ink)", cls="d")
         + person(40, 90, s=0.8, **ME) + key(110, 210, 0.8) + person(260, 90, s=0.8, face=SMILE, **FRIEND) + key(300, 210, 0.8)
         + '<path d="M130 120 L250 120" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>' + label(190, 110, "⟦열쇠를 어떻게 건네죠?|how do I hand over the key?⟧", 11, "var(--bad)")
         + label(190, 300, "⟦빠르지만 전달이 걱정|fast, but the hand-off is the worry⟧", 12, "var(--muted)")
         + label(570, 34, "⟦자물쇠는 뿌리고, 열쇠는 나만|padlocks for everyone, one key for me⟧", 14, "var(--ink)", cls="d")
         + person(420, 90, s=0.8, **ME) + key(490, 210, 0.8, "var(--accent)") + label(490, 240, "⟦나만|mine only⟧", 11, "var(--accent)")
         + "".join(padlock(x, 110, 1.0, "var(--accent)", open_=True) for x in (560, 610, 660, 710)) + label(635, 150, "⟦누구나 채울 수 있어요|anyone can snap one shut⟧", 11, "var(--muted)")
         + person(620, 180, s=0.7, face=SMILE, **FRIEND) + padlock(690, 230, 1.0, "var(--accent)") + label(690, 262, "⟦채웠어요|snapped shut⟧", 10, "var(--muted)")
         + label(570, 300, "⟦느리지만 전달 걱정 없음|slower, but nothing to hand over⟧", 12, "var(--muted)"))

# 5. 열쇠를 잃으면 나도 못 연다
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + person(60, 90, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT) + letter(150, 90, CIPHER, 0.9, scrambled=True, locked=True)
         + '<g transform="translate(110,240)"><circle r="12" fill="none" stroke="var(--line)" stroke-width="5" stroke-dasharray="5 5"/></g>' + label(110, 280, "⟦열쇠가 어디 갔지…|where did the key go…⟧", 12, "var(--bad)")
         + label(280, 250, "⟦나도 못 열어요|I can\'t open it either⟧", 13, "var(--bad)", cls="d")
         + '<g transform="translate(480,90)"><rect width="150" height="90" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 4 L75 60 L150 4" stroke="var(--line)" stroke-width="3" fill="none"/>'
         + label(75, 76, "⟦지민 → 약국|Jimin → pharmacy⟧", 12, "#142033") + padlock(130, 20, 0.8) + "</g>"
         + person(660, 100, s=0.6, face=MASK) + f'<g transform="translate(690,190)">{EYE}</g>'
         + label(570, 220, "⟦겉봉은 보여요|the envelope still shows⟧", 13, "var(--ink)")
         + label(570, 245, "⟦누가 누구에게 보냈는지는 안 숨어요|who wrote to whom isn\'t hidden⟧", 11, "var(--muted)")
         + label(570, 300, "⟦그리고 도둑도 같은 자물쇠를 써요|and thieves use the same padlocks⟧", 12, "var(--bad)"))

SCRAMBLE_I = icon('<rect x="10" y="14" width="44" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">#7@x!</text>')
KEY_I = icon('<circle cx="20" cy="32" r="9" fill="none" stroke="#E9B44C" stroke-width="5"/><rect x="28" y="29" width="26" height="6" fill="#E9B44C"/><rect x="44" y="35" width="4" height="7" fill="#E9B44C"/><rect x="50" y="35" width="4" height="9" fill="#E9B44C"/>')
BACK_I = icon('<rect x="10" y="14" width="44" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><text x="32" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="var(--good)">사과 2</text>')
SHRUG_I = icon(f'<circle cx="32" cy="24" r="12" fill="{SKIN}"/><path d="M22 20 h20 v5 h-20z" fill="#111C30"/><text x="50" y="20" font-size="14" font-weight="700" fill="var(--bad)">?</text><rect x="20" y="38" width="24" height="18" rx="6" fill="#2E3D57"/>')

PAGE = {
    "slug": "encryption", "order": 44,
    "title": ("열쇠 없이는 못 읽는 편지", "The Letter Nobody Can Read Without the Key"),
    "h1": ("<em>암호화</em>가 뭐예요?", "What is <em>Encryption</em>?"),
    "sub": ("암호화(Encryption)를 열쇠 없이는 못 읽는 편지 이야기로 풀어봤어요.",
            "Encryption, told as a story about a letter nobody can read without the key."),
    "panels": [
        {"svg": P1, "alt": ("'사과 두 개 사 와' 편지가 마을 길을 지나는 동안 심부름꾼, 도둑, 행인이 다 들여다봄", "A letter reading Buy two apples travels the town road while a runner, a thief and a bystander all peer at it"),
         "caption": ("편지는 길 위의 누구나 읽을 수 있어요.", "Anyone on the road can read a letter."),
         "small": ('<a href="proxy-ko.html">심부름꾼</a>도, 길가의 사람도, 도둑도요.', 'The <a href="proxy-en.html">runner</a>, the bystander, the thief.')},
        {"svg": P2, "alt": ("'읽지 마세요' 봉투를 도둑이 뜯고 '사과 두 개 사 오래'", "A thief opens a please-don't-read envelope and says buy two apples, it says"),
         "caption": ("봉투에 넣어도 뜯으면 그만이에요.", "An envelope only lasts until someone opens it."),
         "small": ("봉투는 '읽지 마세요'일 뿐, 못 읽게 하진 못해요.", "An envelope asks people not to read. It can't stop them.")},
        {"svg": P3, "hero": True, "alt": ("열쇠를 가진 사람이 '사과 두 개 사 와'를 'ㅋ#7@…' 자물쇠 편지로 바꾸고, 도둑은 물음표, 열쇠를 가진 친구만 다시 '사과 두 개 사 와'로 읽음", "Someone with a key turns Buy two apples into a padlocked ㅋ#7@… letter; the thief sees only a question mark; a friend with the key reads Buy two apples again"),
         "caption": ("암호화는 열쇠 없이는 못 읽는 글자로 바꿔요.", "Encryption turns the letter into marks nobody can read without the key."),
         "small": ("훔쳐가도 못 읽어요. 열쇠를 가진 사람만 원래대로 돌려놔요.", "Stolen, it's still unreadable. Only someone with the key turns it back."),
         "tricks": (4, [
             (SCRAMBLE_I, ("뒤섞기", "Scrambling"), ("읽을 수 없는 글자로", "into unreadable marks"), "warm"),
             (KEY_I, ("열쇠", "The key"), ("뒤섞고 되돌리는 비밀", "the secret that scrambles and unscrambles")),
             (BACK_I, ("돌려놓기", "Turning it back"), ("열쇠가 있을 때만", "only with the key"), "calm"),
             (SHRUG_I, ("훔쳐도 소용없음", "Stealing gets nothing"), ("도둑 손엔 낙서뿐", "the thief holds scribbles"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 나와 친구가 같은 열쇠를 하나씩, 그 사이에 '열쇠를 어떻게 건네죠?'. 오른쪽: 열린 자물쇠를 누구나 가져가 채우고, 여는 열쇠는 나만", "Left: my friend and I each hold a matching key, with how do I hand over the key? between us. Right: open padlocks for anyone to snap shut, and a single key that only I hold"),
         "caption": ("열쇠는 두 가지 방식이 있어요.", "There are two ways to do keys."),
         "small": ('같은 열쇠 둘은 빠르지만 열쇠를 어떻게 전해요? 자물쇠는 뿌리고 열쇠는 나만 — 느리지만 전달 걱정이 없어요. 보통 둘을 같이 써요. <a href="passkey-ko.html">반지</a>가 이 두 번째 방식이에요.',
                   'Matching keys are fast, but how do you hand one over? Padlocks for everyone and one key for me — slower, but nothing to hand over. Usually both are used together. The <a href="passkey-en.html">ring</a> is this second kind.')},
        {"svg": P5, "alt": ("왼쪽: 열쇠를 잃어버려 자물쇠 편지를 나도 못 엶. 오른쪽: 봉인된 봉투의 '지민 → 약국' 겉봉은 도둑이 그대로 봄", "Left: the key is lost and even I can't open the padlocked letter. Right: a sealed envelope whose outside still reads Jimin → pharmacy, in plain view of the thief"),
         "caption": ("열쇠를 잃으면 나도 못 열어요.", "Lose the key, and I can't open it either."),
         "small": ('봉인은 내용만 숨겨요 — 누가 누구에게 보냈는지는 보여요(<a href="ndr-ko.html">복도 파수꾼</a>이 보는 것). 그리고 <a href="ransomware-ko.html">도둑도 같은 자물쇠</a>를 써요. 열쇠 관리가 전부예요.',
                   'A seal hides only the contents — who wrote to whom still shows (what the <a href="ndr-en.html">hallway watcher</a> sees). And <a href="ransomware-en.html">thieves use the same padlocks</a>. Key management is everything.')},
    ],
    "summary": (("<b>암호화</b> = 편지를 <b>열쇠 없이는 못 읽는</b> 글자로 바꾸는 것. 훔쳐가도 소용없고, 열쇠 가진 사람만 <b>돌려놔요</b>.",
                 "<b>Encryption</b> = turning a letter into marks <b>unreadable without the key</b>. Stealing it gets nothing; only the key-holder <b>turns it back</b>."),
                ("Encryption. 같은 열쇠 둘은 AES, 자물쇠+열쇠는 RSA·ECC, HTTPS는 둘 다 써요. 해시는 암호화가 아니라 지문이에요 — 되돌릴 수 없어요.",
                 "Matching keys: AES. Padlock-and-key: RSA, ECC. HTTPS uses both. A hash isn't encryption — it's a fingerprint, and can't be turned back.")),
    "glossary": [
        ("평문 · 암호문", "Plaintext · ciphertext", ("읽히는 편지 · 뒤섞인 편지.", "The readable letter · the scrambled one."), ("암호화 전과 후.", "Before and after encryption.")),
        ("키", "Key", ("열쇠.", "The key."), ("뒤섞고 되돌리는 비밀. 길면 길수록 못 맞혀요.", "The secret that scrambles and unscrambles. The longer, the harder to guess.")),
        ("복호화", "Decryption", ("돌려놓기.", "Turning it back."), ("열쇠로 암호문을 다시 편지로.", "Using the key to make the scramble a letter again.")),
        ("대칭키 (AES)", "Symmetric (AES)", ("같은 열쇠 둘.", "Two matching keys."), ("빠르고 튼튼해요. 열쇠를 전하는 게 문제.", "Fast and strong. Handing over the key is the problem.")),
        ("공개키 · 개인키 (RSA · ECC)", "Public · private key", ("자물쇠 뿌리기 · 열쇠는 나만.", "Padlocks for all · one key for me."), ('전달 걱정이 없어요. → <a href="passkey-ko.html">성문을 알아보는 반지</a>', 'Nothing to hand over. → <a href="passkey-en.html">the ring that knows the gate</a>')),
        ("HTTPS · TLS", "HTTPS · TLS", ("봉인된 편지로 길 지나기.", "Sealed letters on the road."), ('자물쇠로 열쇠를 건네고, 그 열쇠로 편지를 봉인해요. → <a href="vpn-ko.html">봉인된 땅굴</a>', 'A padlock hands over a key, and the key seals the letters. → <a href="vpn-en.html">the sealed tunnel</a>')),
        ("해시", "Hash", ("지문.", "A fingerprint."), ('되돌릴 수 없어요. 암호화가 아니에요. → <a href="ioc-ko.html">남겨진 발자국</a>', 'Can\'t be turned back. Not encryption. → <a href="ioc-en.html">the footprint</a>')),
        ("키 관리 (KMS · HSM)", "Key management (KMS · HSM)", ("열쇠 금고.", "The key vault."), ('열쇠를 잃으면 끝이라, 열쇠를 지키는 게 진짜 일. → <a href="pam-ko.html">금고 속 마스터 열쇠</a>', 'Lose the key and it\'s over, so guarding keys is the real job. → <a href="pam-en.html">the master key in the vault</a>')),
    ],
}
