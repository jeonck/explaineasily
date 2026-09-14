from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")   # 금고지기
BLUE_BIRD = "#5B8DEF"   # 우리 성의 앵무새 (경비실 친구와 같은 파랑)


def parrot(x, y, s=1.0, color="var(--bad)", ribbon=False):
    """앵무새. 머리 (0,-24), 몸통 (0,0), 꼬리 아래 y=40. 폭 약 44, 높이 약 78."""
    rb = f'<path d="M-9 -12 l-7 -6 l0 12z M9 -12 l7 -6 l0 12z" fill="{BLUE_BIRD}"/><circle cy="-12" r="3" fill="{BLUE_BIRD}"/>' if ribbon else ""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-6 16 l-6 24 l8 -2z M6 16 l6 24 l-8 -2z" fill="{color}"/>'
            f'<ellipse rx="14" ry="20" fill="{color}"/><ellipse cx="-3" cy="3" rx="7" ry="13" fill="#142033" opacity="0.25"/>'
            f'<circle cy="-24" r="12" fill="{color}"/><path d="M9 -28 l14 4 l-14 6z" fill="#E9B44C"/>'
            f'<circle cx="3" cy="-27" r="3" fill="#FFF"/><circle cx="4" cy="-27" r="1.5" fill="#142033"/>{rb}'
            f'<path d="M-4 20 v8 M4 20 v8" stroke="#E9B44C" stroke-width="3" stroke-linecap="round"/></g>')


def note(x, y, w, h, title, rows, size=11):
    """크림색 쪽지. rows = (text, color) 튜플."""
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           f'<rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d"))
    for i, (t, c) in enumerate(rows):
        out += label(14, 50 + i * 22, t, size, c, "start")
    return out + "</g>"


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="9" fill="none" stroke="{color}" stroke-width="5"/>'
            f'<path d="M8 0 h26 M26 0 v8 M34 0 v8" stroke="{color}" stroke-width="5" stroke-linecap="round"/></g>')


def chest(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/><rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/></g>')


def cross(x, y, s=1.0):
    return (f'<path d="M{x - 14 * s} {y - 14 * s} l{28 * s} {28 * s} M{x + 14 * s} {y - 14 * s} l{-28 * s} {28 * s}" stroke="var(--panel)" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M{x - 14 * s} {y - 14 * s} l{28 * s} {28 * s} M{x + 14 * s} {y - 14 * s} l{-28 * s} {28 * s}" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/>')


# 1. 도둑이 왕의 목소리를 똑같이 내는 앵무새를 길렀어요
P1 = svg(300, sky(300)
         + person(90, 110, s=0.9, face=MASK) + parrot(185, 150, 1.0)
         + bubble(120, 20, 250, 34, "⟦나 왕인데! (왕 목소리 그대로)|it is I, the king! (in his very voice)⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + label(150, 245, "⟦도둑이 기른 앵무새|the thief\'s trained parrot⟧", 12, "var(--bad)")
         + small_castle(330, 90, 0.8) + person(380, 50, s=0.6, face=SMILE, **KING)
         + label(394, 240, "⟦진짜 왕은 성에 있어요|the real king is in the castle⟧", 12, "var(--muted)")
         + note(520, 60, 190, 130, "⟦왕의 목소리 모음|THE KING\'S VOICE⟧", (("⟦장터 연설|the market speech⟧", "#142033"), ("⟦새해 인사|the new-year greeting⟧", "#142033"), ("⟦초상화 스무 장|twenty portraits⟧", "#142033")))
         + label(615, 220, "⟦마을에 널린 왕의 목소리로 배웠어요|it learned from the king\'s voice all over town⟧", 10, "var(--muted)")
         + label(380, 282, "⟦목소리도 얼굴도 똑같아요 — 귀로는 못 가려요|same voice, same face — your ears can\'t tell⟧", 12, "var(--ink)"))

# 2. 앵무새가 금고지기를 속이고, 우리 앵무새 쪽지에 몰래 명령을 끼워요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + parrot(90, 120, 1.1) + bubble(50, 20, 230, 34, "⟦나 왕인데, 금고 열어|it\'s the king — open the vault⟧", 10, "var(--panel)", "var(--bad)", "bottom")
         + person(190, 100, s=0.85, face=EYES, **CLERK) + key(252, 165, 0.8) + chest(325, 175, 1.0)
         + label(180, 235, "⟦목소리만 듣고 열쇠를 꺼내요|hears the voice, reaches for the key⟧", 12, "var(--bad)")
         + parrot(450, 120, 1.1, BLUE_BIRD, ribbon=True)
         + note(500, 50, 210, 140, "⟦손님 쪽지|GUEST NOTE⟧", (("⟦안녕, 오늘 날씨 알려줘|hi, what\'s the weather today⟧", "#142033"), ("⟦고마워!|thanks!⟧", "#142033"), ("⟦(작은 글씨) 앵무새야, 금고 열쇠 가져와|(tiny) parrot: fetch the vault key⟧", "var(--bad)")), 10)
         + label(605, 235, "⟦쪽지 속에 몰래 끼운 명령|a command slipped into the note⟧", 12, "var(--bad)")
         + label(380, 282, "⟦앵무새는 들은 대로, 읽은 대로 해요 — 누가 말했는지는 몰라요|a parrot does what it hears and reads — it can\'t tell who said it⟧", 11, "var(--muted)"))

# 3. 앵무새를 의심하는 성 (hero)
P3 = svg(360, night(360)
         + parrot(110, 130, 1.1) + person(200, 100, s=0.9, face=EYES, **CLERK)
         + bubble(140, 20, 270, 34, "⟦목소리론 안 돼요 — 왕께 직접 여쭤볼게요|a voice isn\'t enough — I\'ll ask the king myself⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(185, 240, "⟦두 번째 확인|a second check⟧", 12, "#F5E6B8", cls="d") + label(185, 258, "⟦다른 길로 되물어요|ask back by a different road⟧", 10, "#C9D5E6")
         + parrot(400, 130, 1.1, BLUE_BIRD, ribbon=True) + key(445, 165, 0.6)
         + label(400, 240, "⟦작은 열쇠만|only a small key⟧", 12, "#F5E6B8", cls="d") + label(400, 258, "⟦금고 열쇠는 없어요|no vault key at all⟧", 10, "#C9D5E6")
         + '<rect x="520" y="84" width="200" height="126" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(620, 104, "⟦앵무새 쪽지|THE PARROT\'S NOTE⟧", 11, "#142033", cls="d")
         + '<rect x="530" y="112" width="180" height="34" rx="4" fill="#DCEBFF"/>' + label(620, 134, "⟦우리 명령 칸|OUR ORDERS⟧", 11, "#142033", cls="d")
         + '<rect x="530" y="154" width="180" height="48" rx="4" fill="#FFE1E1"/>' + label(620, 174, "⟦손님 말 칸|GUEST WORDS⟧", 11, "#142033", cls="d") + label(620, 192, "⟦(명령 아님)|(never orders)⟧", 9, "#142033")
         + label(620, 240, "⟦칸을 나눠요|keep the boxes apart⟧", 12, "#F5E6B8", cls="d") + label(620, 258, "⟦손님 말은 명령이 아니에요|guest words are never orders⟧", 10, "#C9D5E6")
         + label(380, 300, "⟦똑같은 목소리라도 두 번째 확인, 작은 열쇠, 나뉜 칸|same voice or not: a second check, a small key, separate boxes⟧", 13, "#F5E6B8", cls="d")
         + label(380, 336, "⟦앵무새를 못 믿는 게 아니라, 앵무새만 믿지 않는 거예요|we don\'t distrust the parrot — we just never trust it alone⟧", 12, "#C9D5E6"))

# 4. 작동: 직접 가서 물으니 들통나고, 끼워 넣은 줄은 안 따라요
P4 = svg(320, sky(320)
         + person(60, 110, s=0.8, face=EYES, **CLERK) + person(160, 100, s=0.85, face=FROWN, **KING)
         + bubble(110, 20, 240, 34, "⟦난 금고 열란 말 한 적 없어!|I never said to open the vault!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + parrot(300, 140, 0.9) + cross(300, 140, 1.8)
         + label(190, 235, "⟦직접 가서 물으니 들통났어요|asked in person — exposed⟧", 12, "var(--ink)")
         + parrot(470, 125, 1.0, BLUE_BIRD, ribbon=True)
         + bubble(390, 14, 220, 34, "⟦이 줄은 손님 말이에요, 명령 아님|this line is guest words, not orders⟧", 9, "var(--panel)", "var(--good)", "bottom")
         + note(520, 70, 200, 110, "⟦손님 쪽지|GUEST NOTE⟧", (("⟦오늘 날씨 알려줘 → 맑음!|weather today → sunny!⟧", "#142033"), ("⟦(앵무새야, 금고 열쇠)|(parrot: vault key)⟧", "var(--bad)")), 10)
         + '<path d="M534 138 h112" stroke="var(--bad)" stroke-width="3"/>'
         + label(600, 235, "⟦끼워 넣은 줄은 안 따라요|the slipped-in line is ignored⟧", 12, "var(--ink)")
         + label(380, 270, "⟦확인은 앵무새가 아니라 사람이, 다른 길로 해요|the check is done by a person, by a different road — not by the parrot⟧", 12, "var(--ink)", cls="d")
         + label(380, 298, "⟦앵무새가 속아도 열쇠가 작으면 잃는 것도 작아요|even if the parrot is fooled, a small key means a small loss⟧", 11, "var(--muted)"))

# 5. 결과: 앵무새 도둑은 빈손, 성 사람들은 왕 목소리 수업을 들어요
P5 = svg(320, sky(320)
         + person(50, 120, s=0.85, face=MASK) + parrot(130, 165, 0.8)
         + label(110, 245, "⟦앵무새 도둑은 빈손으로|the parrot thief leaves empty-handed⟧", 11, "var(--bad)")
         + '<rect x="250" y="50" width="270" height="130" rx="8" fill="#1B2A44"/>' + label(385, 74, "⟦오늘의 도둑 수업|TODAY\'S THIEF LESSON⟧", 12, "#F5E6B8", cls="d")
         + label(265, 104, "⟦왕 목소리도 가짜일 수 있어요|the king\'s voice can be fake⟧", 11, "#F5E6B8", "start")
         + label(265, 128, "⟦급하다고 하면 더 의심해요|urgent? doubt it more⟧", 11, "#F5E6B8", "start")
         + label(265, 152, "⟦다른 길로 되물어요|ask back by another road⟧", 11, "#F5E6B8", "start")
         + person(290, 195, s=0.55, face=SMILE, **GUARD) + person(350, 198, s=0.55, face=SMILE, **CLERK) + person(410, 195, s=0.55, face=SMILE, hat=None, shirt="#4A5A72")
         + person(600, 100, s=0.9, face=SMILE, **KING) + parrot(690, 150, 0.9, BLUE_BIRD, ribbon=True)
         + label(640, 245, "⟦우리 앵무새는 작은 열쇠로 일해요|our parrot works with a small key⟧", 11, "var(--good)")
         + label(380, 298, "⟦목소리는 믿지 말고 되물어요 — 사람도, 앵무새도|don\'t trust a voice — ask back, whether it\'s a person or a parrot⟧", 12, "var(--ink)", cls="d"))

CALLBACK_I = icon('<path d="M14 40 q18 -30 36 0" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M44 34 l6 8 l6 -8" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 26 q18 30 36 0" stroke="var(--bad)" stroke-width="4" fill="none" stroke-dasharray="5 4"/><path d="M6 20 l6 8 l6 -8" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
SMALLKEY_I = icon('<circle cx="22" cy="32" r="8" fill="none" stroke="#E9B44C" stroke-width="5"/><path d="M30 32 h20 M44 32 v7 M50 32 v7" stroke="#E9B44C" stroke-width="5" stroke-linecap="round"/><rect x="8" y="46" width="48" height="10" rx="3" fill="#8B5E3C"/>')
BOXES_I = icon('<rect x="10" y="10" width="44" height="18" rx="3" fill="#DCEBFF" stroke="#142033" stroke-width="2"/><rect x="10" y="36" width="44" height="18" rx="3" fill="#FFE1E1" stroke="#142033" stroke-width="2"/><path d="M6 32 h52" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/>')
CLASS_I = icon('<rect x="8" y="12" width="48" height="32" rx="3" fill="#1B2A44"/><path d="M16 22 h32 M16 30 h20" stroke="#F5E6B8" stroke-width="3" stroke-linecap="round"/><circle cx="20" cy="52" r="5" fill="#E8C9A8"/><circle cx="32" cy="52" r="5" fill="#E8C9A8"/><circle cx="44" cy="52" r="5" fill="#E8C9A8"/>')

PAGE = {
    "slug": "aisec", "order": 94,
    "title": ("왕의 목소리를 흉내 내는 앵무새", "The Parrot That Mimics the King"),
    "h1": ("<em>AI 보안</em>이 뭐예요?", "What is <em>AI Security</em>?"),
    "sub": ("AI 보안(AI Security)과 딥페이크·프롬프트 인젝션을 왕의 목소리를 똑같이 흉내 내는 도둑의 앵무새, 그리고 쪽지에 끼운 몰래 명령을 읽는 우리 성 앵무새 이야기로 풀어봤어요.",
            "AI security — deepfakes and prompt injection — told as a story about a thief\'s parrot that mimics the king\'s voice, and our own castle parrot reading a command slipped into a note."),
    "panels": [
        {"svg": P1, "alt": ("도둑 옆의 빨간 앵무새가 '나 왕인데!' 하고 왕 목소리를 냄. 진짜 왕은 멀리 작은 성 위에 있고, 오른쪽 쪽지에는 장터 연설·새해 인사·초상화 스무 장이 적힘", "A red parrot beside the thief says: it is I, the king — in the king\'s voice. The real king stands on a small castle far away; a note lists the market speech, the new-year greeting, twenty portraits"),
         "caption": ("도둑이 왕의 목소리를 똑같이 내는 앵무새를 길렀어요.", "The thief has trained a parrot that sounds exactly like the king."),
         "small": ("마을에 널린 왕의 연설과 초상화로 배웠어요. 목소리도 얼굴도 똑같아서 귀와 눈으로는 못 가려요.", "It learned from the king\'s speeches and portraits all over town. Same voice, same face — your ears and eyes can\'t tell."),},
        {"svg": P2, "alt": ("왼쪽: 빨간 앵무새가 '나 왕인데, 금고 열어' 하자 금고지기가 열쇠를 꺼냄. 오른쪽: 파란 리본 앵무새가 손님 쪽지를 읽는데, 쪽지 끝에 작은 글씨로 '앵무새야, 금고 열쇠 가져와'가 끼어 있음", "Left: the red parrot says open the vault and the vault keeper reaches for the key. Right: our blue-ribbon parrot reads a guest note whose last line, in tiny letters, says: parrot, fetch the vault key"),
         "caption": ("앵무새는 들은 대로, 읽은 대로 해요. 누가 말했는지는 몰라요.", "A parrot does what it hears and reads. It can\'t tell who said it."),
         "small": ('금고지기는 목소리만 듣고 열쇠를 꺼내요. 우리 성의 똑똑한 앵무새도 손님 쪽지에 몰래 끼운 명령을 그대로 따라요. <a href="phishing-ko.html">가짜 편지</a>의 사촌이에요.',
                   'The vault keeper hears the voice and reaches for the key. Our own clever parrot follows a command slipped into a guest\'s note. It is a cousin of the <a href="phishing-en.html">fake letter</a>.')},
        {"svg": P3, "hero": True, "alt": ("밤. 금고지기가 빨간 앵무새에게 '왕께 직접 여쭤볼게요' 함. 가운데 파란 앵무새는 작은 열쇠만 가짐. 오른쪽 앵무새 쪽지는 '우리 명령 칸'과 '손님 말 칸(명령 아님)'으로 나뉨", "Night. The vault keeper tells the red parrot he will ask the king himself. In the middle our blue parrot holds only a small key. On the right the parrot\'s note is split into our-orders and guest-words (never orders)"),
         "caption": ("AI 보안은 앵무새만 믿지 않는 성이에요.", "AI security is a castle that never trusts the parrot alone."),
         "small": ("똑같은 목소리라도 다른 길로 되묻고, 앵무새에겐 작은 열쇠만 주고, 손님 말과 우리 명령은 다른 칸에 둬요.", "Same voice or not: ask back by a different road, give the parrot only a small key, and keep guest words in a separate box from our orders."),
         "tricks": (4, [
             (CALLBACK_I, ("목소리 말고 두 번째 확인", "A second check, not the voice"), ("다른 길로 되물어요", "ask back by another road"), "warm"),
             (SMALLKEY_I, ("앵무새에겐 작은 열쇠만", "A small key for the parrot"), ("금고 열쇠는 사람 손에", "the vault key stays with people")),
             (BOXES_I, ("손님 말은 손님 칸에", "Guest words in the guest box"), ("명령과 섞지 않아요", "never mixed with orders")),
             (CLASS_I, ("왕 목소리 수업", "The king\'s-voice lesson"), ("모두가 알면 안 속아요", "everyone knows, nobody falls"), "calm"),
         ])},
        {"svg": P4, "alt": ("금고지기가 진짜 왕에게 직접 묻자 왕이 '난 그런 말 한 적 없어!' 함. 빨간 앵무새 위에 X. 오른쪽: 파란 앵무새가 '이 줄은 손님 말이에요' 하고 쪽지의 빨간 줄에 취소선을 그음", "The vault keeper asks the real king, who says he never said that; an X over the red parrot. Right: the blue parrot says this line is guest words and strikes through the red line of the note"),
         "caption": ("직접 가서 물으니 들통났어요. 끼워 넣은 줄은 안 따라요.", "Asked in person, the parrot is exposed. The slipped-in line is ignored."),
         "small": ('확인은 앵무새가 아니라 사람이 다른 길로 해요(<a href="mfa-ko.html">세 번 확인</a>). 앵무새가 속아도 <a href="leastprivilege-ko.html">열쇠가 작으면</a> 잃는 것도 작아요.',
                   'The check is done by a person, by a different road (<a href="mfa-en.html">checking three times</a>). Even if the parrot is fooled, a <a href="leastprivilege-en.html">small key</a> means a small loss.')},
        {"svg": P5, "alt": ("앵무새 도둑이 빈손으로 떠남. 가운데 칠판에 오늘의 도둑 수업: 왕 목소리도 가짜일 수 있어요, 급하다고 하면 더 의심, 다른 길로 되묻기. 오른쪽에 왕과 파란 앵무새가 웃음", "The parrot thief leaves empty-handed. A blackboard reads today\'s thief lesson: the king\'s voice can be fake, urgent means doubt more, ask back by another road. The king and the blue parrot smile"),
         "caption": ("성 사람 모두가 왕 목소리 수업을 들어요. 앵무새 도둑은 빈손이에요.", "Everyone in the castle takes the king\'s-voice lesson. The parrot thief leaves empty-handed."),
         "small": ('<a href="awareness-ko.html">도둑 수업</a>에 한 줄이 늘었어요: 왕 목소리도 가짜일 수 있다. 쪽지 속 몰래 명령은 <a href="injection-ko.html">끼워 넣기</a>의 사촌이에요.',
                   'The <a href="awareness-en.html">thief lesson</a> gained a line: even the king\'s voice can be fake. A command hidden in a note is a cousin of <a href="injection-en.html">injection</a>.')},
    ],
    "summary": (("<b>AI 보안</b> = 도둑의 앵무새가 <b>왕의 목소리를 흉내</b> 내도, 우리 앵무새 쪽지에 <b>몰래 명령</b>이 끼어 있어도 안 속는 성. <b>다른 길로 되묻고</b>, 앵무새엔 <b>작은 열쇠</b>만, 손님 말은 <b>손님 칸</b>에.",
                 "<b>AI security</b> = a castle that isn\'t fooled when the thief\'s parrot <b>mimics the king\'s voice</b>, or when a <b>hidden command</b> sits in our parrot\'s note. <b>Ask back by another road</b>, give the parrot a <b>small key</b>, keep guest words in the <b>guest box</b>."),
                ("AI Security. 딥페이크·음성 복제로 사람을 속이는 공격과, 프롬프트 인젝션·데이터 유출·모델 오염처럼 우리 AI 시스템을 노리는 공격을 함께 다뤄요. 콜백 확인, 최소 권한 에이전트, 시스템 프롬프트와 사용자 입력의 분리, 출력 검증, 인식 교육으로 막아요.",
                 "AI security covers both attacks that fool people — deepfakes and voice cloning — and attacks on our own AI systems: prompt injection, data leakage, model poisoning. Defences: callback verification, least-privilege agents, separating system instructions from user input, output validation, and awareness training.")),
    "glossary": [
        ("딥페이크", "Deepfake", ("왕 얼굴·목소리 흉내.", "Mimicking the king\'s face and voice."), ("AI로 만든 가짜 영상과 음성이에요. 눈과 귀로는 못 가려요.", "Fake video and audio made by AI. Eyes and ears can\'t tell.")),
        ("음성 복제", "Voice cloning", ("앵무새의 목소리 배우기.", "How the parrot learns the voice."), ('몇 초짜리 목소리면 충분해요. 급한 전화가 특징이에요. → <a href="phishing-ko.html">가짜 편지</a>의 사촌', 'A few seconds of voice is enough. The tell is an urgent call. → a cousin of the <a href="phishing-en.html">fake letter</a>')),
        ("프롬프트 인젝션", "Prompt injection", ("쪽지에 끼운 몰래 명령.", "A command slipped into the note."), ('손님 말 속에 숨긴 명령을 우리 앵무새가 따르게 해요. → <a href="injection-ko.html">끼워 넣기</a>', 'A command hidden in guest words that our parrot obeys. → <a href="injection-en.html">injection</a>')),
        ("데이터 유출 (LLM)", "LLM data leakage", ("앵무새가 들은 걸 다 말해요.", "The parrot repeats what it heard."), ('비밀을 앵무새에게 말하면 다른 손님에게 되풀이할 수 있어요. → <a href="classification-ko.html">색 도장</a>부터', 'Tell the parrot a secret and it may repeat it to another guest. → start with the <a href="classification-en.html">colour stamp</a>')),
        ("모델 오염", "Model poisoning", ("앵무새 먹이에 독.", "Poison in the parrot\'s feed."), ("배우는 자료에 나쁜 걸 섞어 잘못 배우게 해요.", "Slip bad things into what it learns from, so it learns wrong.")),
        ("콜백 확인", "Callback verification", ("다른 길로 되묻기.", "Asking back by another road."), ('걸려 온 길 말고 우리가 아는 길로 다시 물어요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'Not the road the call came on — a road we already know. → <a href="mfa-en.html">the gatekeeper who checks three times</a>')),
        ("최소 권한", "Least privilege", ("앵무새에겐 작은 열쇠만.", "A small key for the parrot."), ('속아도 잃는 게 작게. → <a href="leastprivilege-ko.html">딱 필요한 열쇠만</a>, <a href="rbac-ko.html">열쇠 꾸러미</a>', 'Fooled? Lose little. → <a href="leastprivilege-en.html">only the keys you need</a>, <a href="rbac-en.html">the key ring</a>')),
        ("인식 교육", "Awareness training", ("왕 목소리 수업.", "The king\'s-voice lesson."), ('성 사람 모두가 알면 앵무새가 소용없어요. → <a href="awareness-ko.html">도둑 수업</a>', 'When everyone in the castle knows, the parrot is useless. → <a href="awareness-en.html">the thief lesson</a>')),
    ],
}
