from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
POST = dict(hat="#5B8DEF", shirt="#5B8DEF")


def letter(x, y, s=1.0, stamp="var(--good)", fake=False, lines=()):
    st = (f'<rect x="88" y="8" width="24" height="24" rx="2" fill="{stamp}"/>' + (label(100, 24, "?", 14, "#FFF") if fake else label(100, 24, "✓", 14, "#FFF")))
    body = "".join(label(14, 44 + i * 14, t, 10, ("var(--bad)" if fake and i else "#142033"), "start") for i, t in enumerate(lines))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="120" height="80" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M0 4 L60 40 L120 4" stroke="#C9A86A" stroke-width="2" fill="none" opacity="{0 if lines else 1}"/>{st}{body}</g>')


def mailbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="#4A5A72"/><rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/><path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/></g>')


def fake_gate(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="30" width="140" height="90" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"/>'
            + battlements(-70, 10, 140, 4, "var(--stone)", 20)
            + '<path d="M-28 120 V78 a28 28 0 0 1 56 0 V120 Z" fill="var(--night)"/>'
            '<rect x="60" y="40" width="10" height="90" fill="#8B5E3C" transform="rotate(-20 65 85)"/></g>')


# 1. 매일 편지가 온다
P1 = svg(280, sky(280) + mailbox(120, 100)
         + letter(220, 60, 0.8) + letter(360, 90, 0.8) + letter(500, 60, 0.8)
         + label(268, 140, "⟦우체국|post office⟧", 11, "var(--muted)") + label(408, 170, "⟦시장|market⟧", 11, "var(--muted)") + label(548, 140, "⟦친구|a friend⟧", 11, "var(--muted)")
         + person(640, 100, s=0.85, **ME)
         + label(380, 260, "⟦대부분은 진짜예요|most of them are real⟧", 13, "var(--muted)"))

# 2. 도둑이 우체국인 척
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(70, 90, s=0.9, face=MASK, **POST) + label(100, 230, "⟦우체국 옷을 입은 도둑|a thief in post-office blue⟧", 12, "var(--bad)")
         + letter(240, 60, 1.1, "var(--bad)", fake=True, lines=("⟦우체국에서 왔어요|From the post office⟧", "⟦소포가 있어요! 오늘까지|A parcel! Today only⟧", "⟦여기로 와서 열쇠를 보여주세요|Come here and show your key⟧"))
         + person(560, 100, s=0.9, **ME) + bubble(520, 30, 200, 34, "⟦소포? 빨리 가야지|A parcel? Better hurry⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦급하게, 겁주며, 상 준다며|urgent, scary, or too good to be true⟧", 13, "var(--muted)"))

# 3. 피싱 = 아는 사람인 척 속여 열쇠 받기 (hero)
P3 = svg(340, sky(340)
         + letter(40, 40, 0.8, "var(--bad)", fake=True) + person(60, 130, s=0.85, **ME)
         + '<path d="M130 200 C220 240 320 240 420 200" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/><path d="M410 190 L422 200 L410 210" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + fake_gate(530, 60) + label(530, 220, "⟦가짜 성문|the fake gate⟧", 13, "var(--bad)")
         + person(640, 100, s=0.6, face=MASK)
         + bubble(300, 70, 200, 34, "⟦암호말은 사과예요!|My password is apple!⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + '<g transform="translate(470,260)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="6" y="-2" width="24" height="4" fill="#E9B44C"/></g><path d="M500 260 L600 250" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(380, 322, "⟦성벽도 자물쇠도 안 부숴요. 내가 직접 열어주게 해요|no wall is broken, no lock picked — I open the door myself⟧", 13, "var(--muted)"))

# 4. 편지만이 아니다
PHONE = '<g transform="translate(0,0)"><rect x="-22" y="-40" width="44" height="80" rx="8" fill="var(--night)"/><rect x="-17" y="-32" width="34" height="58" rx="3" fill="var(--panel)"/></g>'
P4 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + letter(40, 60, 0.8, "var(--bad)", fake=True) + label(88, 160, "⟦편지|the letter⟧", 13, "var(--ink)", cls="d") + label(88, 180, "⟦이메일|email⟧", 11, "var(--muted)")
         + f'<g transform="translate(250,100)">{PHONE}</g>' + label(250, 60, "⟦소포 도착 → 링크|Parcel arrived → link⟧", 9, "var(--bad)") + label(250, 160, "⟦쪽지|the text⟧", 13, "var(--ink)", cls="d") + label(250, 180, "⟦스미싱|smishing⟧", 11, "var(--muted)")
         + '<g transform="translate(410,100)"><path d="M-16 -30 q-16 20 0 40 l10 -10 q-6 -10 0 -20z" fill="var(--night)"/><path d="M-6 -40 a40 40 0 0 1 40 40" stroke="var(--accent)" stroke-width="3" fill="none"/></g>' + label(410, 160, "⟦전화|the call⟧", 13, "var(--ink)", cls="d") + label(410, 180, "⟦보이스 피싱|vishing⟧", 11, "var(--muted)")
         + letter(540, 60, 0.8, "var(--bad)", fake=True, lines=("⟦지민 씨께|Dear Jimin⟧", "⟦사장님이 급히 찾으세요|The boss needs you now⟧")) + label(588, 160, "⟦콕 집어|aimed at you⟧", 13, "var(--ink)", cls="d") + label(588, 180, "⟦스피어 피싱|spear phishing⟧", 11, "var(--muted)")
         + label(380, 270, "⟦내 이름과 상사 이름까지 알고 보내면 더 잘 속아요|knowing your name and your boss\'s makes it far more convincing⟧", 12, "var(--muted)"))

# 5. 겉봉을 보고, 문 앞에서 멈춘다
RING = '<g transform="translate(64,84)"><circle r="9" fill="none" stroke="var(--stone)" stroke-width="5"/><path d="M-5 -9 L0 -16 L5 -9 Z" fill="var(--stone-dark)"/></g>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + letter(40, 50, 0.9, "var(--bad)", fake=True) + '<g transform="translate(200,70)"><circle r="26" fill="var(--panel)" fill-opacity="0.5" stroke="var(--night)" stroke-width="5"/><path d="M20 20 L40 40" stroke="var(--night)" stroke-width="7" stroke-linecap="round"/></g>'
         + label(150, 160, "⟦보낸 주소: post-offlce.kr?|from: post-offlce.kr?⟧", 12, "var(--bad)")
         + person(60, 190, s=0.8, **ME, extra=RING) + fake_gate(260, 200, 0.5) + label(260, 290, "⟦반지가 안 켜져요|the ring stays dark⟧", 11, "var(--good)")
         + label(190, 305, "⟦겉봉을 보고, 문 앞에서 한 번 멈춰요|check the envelope, pause at the door⟧", 12, "var(--muted)")
         + "".join(person(400 + i * 60, 80, s=0.55, hat=h, shirt="#4A5A72", face=SMILE) for i, h in enumerate((None, "#E9B44C", "var(--stone-dark)", "var(--good)", None)))
         + person(700, 80, s=0.55, hat="#5B8DEF", shirt="#4A5A72", face=FROWN + SWEAT) + label(716, 150, "⟦급했어요…|I was in a hurry…⟧", 10, "var(--bad)")
         + label(570, 200, "⟦백 명 중 한 명은 속아요|one in a hundred still falls for it⟧", 13, "var(--bad)")
         + '<g transform="translate(570,250)"><path d="M-14 8 c0 -22 28 -22 28 0 v12 h-28 z" fill="#E9B44C"/><rect x="-18" y="20" width="36" height="5" rx="2" fill="#C9822B"/></g>' + label(570, 300, "⟦그래서 '이상한 편지' 신고 종을 둬요|so there\'s a bell for reporting odd letters⟧", 12, "var(--muted)"))

MASK_I = icon(f'<circle cx="32" cy="28" r="14" fill="{SKIN}"/><path d="M18 22 Q32 6 46 22 Z" fill="#5B8DEF"/><rect x="24" y="26" width="16" height="5" fill="#111C30"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--bad)" stroke-width="3"/><path d="M32 18 V32 L42 38" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round"/><text x="50" y="18" font-size="12" font-weight="700" fill="var(--bad)">!</text>')
GATE_I = icon('<rect x="8" y="24" width="48" height="30" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="2" stroke-dasharray="4 3"/><rect x="8" y="16" width="10" height="10" fill="var(--stone)"/><rect x="27" y="16" width="10" height="10" fill="var(--stone)"/><rect x="46" y="16" width="10" height="10" fill="var(--stone)"/><path d="M24 54 V42 a8 8 0 0 1 16 0 V54Z" fill="var(--night)"/>')
HAND_I = icon('<circle cx="18" cy="34" r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="24" y="31" width="22" height="6" fill="#E9B44C"/><path d="M50 22 l8 8 -8 8" stroke="var(--bad)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "phishing", "order": 39,
    "title": ("우체국인 척하는 편지", "The Letter from a Fake Post Office"),
    "h1": ("<em>피싱</em>이 뭐예요?", "What is <em>Phishing</em>?"),
    "sub": ("피싱(Phishing)을 우체국인 척 보낸 가짜 편지 이야기로 풀어봤어요.",
            "Phishing, told as a story about a letter that pretends to come from the post office."),
    "panels": [
        {"svg": P1, "alt": ("우체통과 우체국·시장·친구가 보낸 편지 세 통, 편지를 받는 사람", "A mailbox, three letters from the post office, the market and a friend, and someone receiving them"),
         "caption": ("성에는 매일 편지가 와요.", "Letters arrive at the castle every day."),
         "small": ("우체국, 시장, 친구… 대부분은 진짜예요.", "From the post office, the market, a friend… most of them are real.")},
        {"svg": P2, "alt": ("우체국 파란 옷을 입은 가면 쓴 도둑이 '소포가 있어요! 오늘까지, 여기로 와서 열쇠를 보여주세요' 편지를 보내고, 받은 사람은 '빨리 가야지'", "A masked thief in post-office blue sends a letter — A parcel! Today only, come here and show your key — and the reader says better hurry"),
         "caption": ("도둑이 우체국인 척 편지를 보내요.", "The thief sends a letter dressed as the post office."),
         "small": ("'소포가 왔어요, 오늘까지, 여기로 오세요.' 급하게, 겁주며, 상 준다며.", "'A parcel, today only, come here.' Urgent, scary, or too good to be true.")},
        {"svg": P3, "hero": True, "alt": ("가짜 편지를 받은 사람이 점선 길을 따라 가짜 성문으로 가서 '암호말은 사과예요!' 하고 말하고, 열쇠가 도둑에게 넘어감", "The letter's reader follows a dotted road to a fake gate, says My password is apple!, and the key passes to the thief"),
         "caption": ("피싱은 아는 사람인 척 속여서 열쇠를 받아내요.", "Phishing pretends to be someone you trust, and gets you to hand over the key."),
         "small": ("성벽도 자물쇠도 안 부숴요. 내가 직접 열어주게 해요.", "No wall is broken, no lock picked. It gets me to open the door myself."),
         "tricks": (4, [
             (MASK_I, ("아는 척", "A familiar face"), ("우체국, 사장님, 은행", "the post office, the boss, the bank")),
             (CLOCK_I, ("급하게", "Hurry!"), ("오늘까지, 안 하면 큰일", "today only, or else"), "warm"),
             (GATE_I, ("가짜 성문", "The fake gate"), ("똑같이 생긴 문", "a door that looks just right")),
             (HAND_I, ("내가 여는 문", "I open it myself"), ("도둑은 아무것도 안 부숴요", "the thief breaks nothing"), "calm"),
         ])},
        {"svg": P4, "alt": ("가짜 편지, '소포 도착 → 링크' 문자가 뜬 휴대폰, 전화기, '지민 씨께, 사장님이 급히 찾으세요' 편지", "A fake letter; a phone showing Parcel arrived → link; a telephone; a letter reading Dear Jimin, the boss needs you now"),
         "caption": ("편지만이 아니에요.", "It isn't only letters."),
         "small": ("문자로(스미싱), 전화로(보이스 피싱), 그리고 내 이름과 상사 이름을 알고 콕 집어서(스피어 피싱).", "By text (smishing), by phone (vishing), and aimed at you by name, boss and all (spear phishing).")},
        {"svg": P5, "alt": ("왼쪽: 돋보기로 겉봉 주소 'post-offlce.kr?'를 살피고, 가짜 성문 앞에서 반지가 안 켜짐. 오른쪽: 백 명 중 한 명이 '급했어요…', 그리고 신고 종", "Left: a magnifying glass on the sender post-offlce.kr?, and the ring staying dark at a fake gate. Right: one person in a hundred says I was in a hurry…, and a reporting bell"),
         "caption": ("겉봉을 보고, 문 앞에서 한 번 멈춰요.", "Check the envelope, and pause at the door."),
         "small": ('보낸 주소가 진짜인지, 문이 진짜 성문인지. <a href="passkey-ko.html">반지</a>는 가짜 성문에 안 켜져요. 그래도 백 명 중 한 명은 속아요 — 그래서 "이상한 편지" 신고 종을 둬요.',
                   'Is the sender real, is the gate real. The <a href="passkey-en.html">ring</a> stays dark at a fake gate. Still, one in a hundred falls for it — so there\'s a bell for reporting odd letters.')},
    ],
    "summary": (("<b>피싱</b> = <b>아는 사람인 척</b> 편지를 보내, 내가 직접 열쇠를 건네거나 <b>가짜 성문</b>에 들어가게 하는 것. 성벽을 안 부숴요 — <b>나를</b> 속여요.",
                 "<b>Phishing</b> = a letter <b>pretending to be someone you trust</b>, so you hand over the key or walk into a <b>fake gate</b>. It doesn't break the wall — it fools <b>you</b>."),
                ("Phishing. 도둑 백과사전의 T1566, 침입의 가장 흔한 첫걸음이에요. 방어는 훈련, 신고 종, 가짜 성문에 안 켜지는 반지(패스키), 그리고 진짜 우체국 도장(SPF·DKIM·DMARC).",
                 "Phishing is T1566 in the encyclopedia — the most common first step of a break-in. Defenses: training, a reporting bell, a ring that stays dark at fake gates (passkeys), and the real post office's stamp (SPF, DKIM, DMARC).")),
    "glossary": [
        ("스피어 피싱", "Spear phishing", ("콕 집어 보내기.", "Aimed at one person."), ("내 이름, 상사 이름, 요즘 하는 일까지 알고 써요.", "Written knowing your name, your boss, what you're working on.")),
        ("스미싱", "Smishing", ("문자 편지.", "The text-message letter."), ("'소포 도착 → 링크'. 휴대폰이라 더 급하게 눌러요.", "'Parcel arrived → link'. On a phone, you tap faster.")),
        ("보이스 피싱", "Vishing", ("전화.", "The call."), ("목소리로 우체국·은행·경찰인 척.", "A voice pretending to be the post office, the bank, the police.")),
        ("가짜 성문", "Phishing site", ("똑같이 생긴 문.", "The look-alike door."), ('열쇠를 여기 넣는 순간 도둑에게 가요. → <a href="mfa-ko.html">문지기 이야기</a>', 'Put the key in here and it goes to the thief. → <a href="mfa-en.html">the gatekeeper story</a>')),
        ("겉봉 주소", "Sender address", ("보낸 사람 주소.", "Who it\'s really from."), ("post-office.kr 과 post-offlce.kr. 한 글자가 달라요.", "post-office.kr and post-offlce.kr — one letter apart.")),
        ("우체국 도장", "SPF · DKIM · DMARC", ("진짜 우체국이 찍은 도장.", "The real post office\'s stamp."), ('어느 우체국이 내 이름으로 편지를 보낼 수 있는지 <a href="dns-ko.html">안내소</a>에 적어둬요.', 'The <a href="dns-en.html">directory</a> records which post offices may send in my name.')),
        ("신고 종", "Report button", ("'이상한 편지' 종.", "The odd-letter bell."), ('한 명이 울리면 경비실이 모두의 편지를 치워요. → <a href="soc-ko.html">성의 경비실</a>', 'One ring and the guard room pulls the letter from everyone. → <a href="soc-en.html">the guard room</a>')),
        ("T1566", "T1566", ("백과사전의 번호.", "Its number in the encyclopedia."), ('→ <a href="attack-ko.html">도둑 백과사전</a>', '→ <a href="attack-en.html">the burglar encyclopedia</a>')),
    ],
}
