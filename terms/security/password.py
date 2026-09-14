from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
GUARD = dict(hat="var(--good)", shirt="var(--good)")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
LONG = "⟦보라색 고래가 빵을 구워요|purple whale bakes bread⟧"


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def clock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="30" fill="var(--panel)" stroke="var(--line)" stroke-width="4"/>'
            f'<path d="M0 -18 v18 l12 7" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


def card(x, y, door, l1, l2):
    return (f'<g transform="translate({x},{y})"><rect width="80" height="90" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(40, 22, door, 11, "#142033", cls="d") + label(40, 42, l1, 10, "#142033") + label(40, 56, l2, 10, "#142033") + "</g>")


def ring(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="14" fill="none" stroke="#E9B44C" stroke-width="7"/>'
            f'<path d="M-7 -14 L0 -24 L7 -14 Z" fill="var(--accent)"/></g>')


def phone(x, y, code, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-46" width="52" height="92" rx="8" fill="var(--night)"/>'
            f'<rect x="-20" y="-36" width="40" height="66" rx="3" fill="var(--panel)"/>{label(0, 2, code, 9, "#142033")}</g>')


# 1. 문지기는 암호말을 물어요 — 도둑은 하나씩 맞춰 봐요
P1 = svg(300, sky(300) + gate(260, 60) + person(230, 150, s=0.8, face=EYES, **GUARD)
         + bubble(150, 20, 150, 34, "⟦암호말은?|Password?⟧", 14, "var(--panel)", "var(--good)", "bottom")
         + person(80, 150, s=0.8, **ME) + bubble(40, 84, 100, 34, "⟦사과!|Apple!⟧", 15, "var(--panel)", "var(--line)", "bottom")
         + paper(420, 70, 130, 140, "⟦맞춰 볼 말|MY GUESSES⟧", ("⟦사과?|apple?⟧", "⟦배?|pear?⟧", "⟦포도?|grape?⟧", "⟦1234?|1234?⟧"))
         + person(580, 100, s=0.85, face=MASK, extra=BAG)
         + bubble(540, 20, 200, 34, "⟦하나씩 다 말해 볼게|I will just try them all⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(380, 285, "⟦짧은 암호말은 몇 번 안 가서 맞혀요|a short password takes only a few guesses⟧", 12, "var(--ink)"))

# 2. 짧으면 금방, 똑같으면 다, 그리고 도둑은 이미 명부가 있어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<rect x="80" y="40" width="100" height="50" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(130, 72, "⟦사과|apple⟧", 20, "#142033", cls="d")
         + clock(130, 150, 0.8) + label(130, 250, "⟦짧으면|too short:⟧", 14, "var(--ink)", cls="d") + label(130, 272, "⟦1초 만에 맞혀요|guessed in a second⟧", 11, "var(--bad)")
         + small_castle(290, 50, 0.45) + small_castle(360, 50, 0.45) + small_castle(430, 50, 0.45)
         + "".join(label(x + 36, 140, "⟦사과|apple⟧", 12, "var(--bad)") for x in (290, 360, 430))
         + label(396, 250, "⟦문마다 똑같으면|same one everywhere:⟧", 14, "var(--ink)", cls="d") + label(396, 272, "⟦하나 새면 다 열려요|one leak opens them all⟧", 11, "var(--bad)")
         + paper(560, 40, 160, 130, "⟦새어 나간 명부|LEAKED LIST⟧", ("⟦사과|apple⟧", "⟦1234|1234⟧", "⟦비밀번호|password⟧")) + person(660, 175, s=0.5, face=MASK)
         + label(640, 250, "⟦흔한 말이면|too common:⟧", 14, "var(--ink)", cls="d") + label(640, 272, "⟦도둑은 이미 명부가 있어요|the thief already has a list⟧", 11, "var(--bad)")
         + label(380, 308, "⟦짧거나, 똑같거나, 흔하거나 — 셋 다 도둑이 좋아해요|short, repeated, or common — thieves love all three⟧", 11, "var(--muted)"))

# 3. 비밀번호 = 문지기에게 속삭이는 암호말 (hero)
P3 = svg(360, sky(360) + gate(380, 40) + person(350, 130, s=0.85, face=SMILE, **GUARD)
         + person(200, 140, s=0.9, **ME)
         + bubble(50, 40, 250, 46, LONG, 13, "var(--panel)", "var(--line)", "bottom")
         + label(230, 270, "⟦아주 작게 속삭여요|whispered, very quietly⟧", 11, "var(--muted)")
         + person(600, 120, s=0.85, face=MASK, extra=BAG)
         + bubble(540, 40, 190, 34, "⟦…뭐라고?|…what was that?⟧", 12, "var(--panel)", "var(--bad)", "bottom")
         + label(630, 250, "⟦맞히려면 백만 년|a million years to guess⟧", 11, "var(--bad)")
         + label(380, 310, "⟦길게, 문마다 다르게, 상자에 넣고, 아무한테도 안 불러줘요|long, different at every door, kept in a box, told to no one⟧", 13, "var(--ink)", cls="d")
         + label(380, 344, "⟦암호말은 문지기와 나, 둘만 아는 말이에요|a password is a word only the gatekeeper and I know⟧", 12, "var(--muted)"))

# 4. 잠긴 열쇠 상자 — 외울 건 상자 열쇠 하나
P4 = svg(320, sky(320)
         + card(85, 36, "⟦성문|Gate⟧", "⟦보라색 고래가|purple whale⟧", "⟦빵을 구워요|bakes bread⟧")
         + card(160, 44, "⟦창고|Storeroom⟧", "⟦노란 개구리가|yellow frog⟧", "⟦피리를 불어요|plays a flute⟧")
         + card(235, 36, "⟦우물|Well⟧", "⟦감자 셋이|3 potatoes⟧", "⟦춤을 춰요|dancing⟧")
         + '<rect x="70" y="120" width="260" height="130" rx="6" fill="#8B5E3C"/><rect x="60" y="112" width="280" height="14" rx="4" fill="#5A3B22"/>'
         + '<rect x="188" y="160" width="24" height="20" rx="3" fill="#E9B44C"/><path d="M193 160 v-7 a7 7 0 0 1 14 0 v7" stroke="#E9B44C" stroke-width="3" fill="none"/>'
         + label(200, 280, "⟦문마다 다른 암호말이 상자 안에|a different password for every door, inside the box⟧", 11, "var(--ink)")
         + person(400, 120, s=0.85, **ME) + key(495, 175, 0.9)
         + bubble(360, 40, 220, 40, "⟦상자 열쇠 하나만 외워요|I remember one key, for the box⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(440, 245, "⟦상자 열쇠 = 제일 긴 암호말|the box key = my longest one⟧", 10, "var(--muted)")
         + '<g transform="translate(660,90)"><path d="M0 -22 l5 15 l15 5 l-15 5 l-5 15 l-5 -15 l-15 -5 l15 -5z" fill="var(--accent)"/></g>'
         + label(660, 140, "⟦새 문이 생기면|a new door?⟧", 13, "var(--ink)", cls="d") + label(660, 162, "⟦상자가 새 암호말을 지어줘요|the box invents a new one⟧", 11, "var(--muted)")
         + label(380, 302, "⟦외울 건 하나, 문은 백 개여도|one to remember, even with a hundred doors⟧", 12, "var(--ink)", cls="d"))

# 5. 새면 바꾸고, 문지기는 하나 더 물어요
P5 = svg(300, sky(300)
         + '<rect x="50" y="40" width="210" height="150" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="50" y="40" width="210" height="26" rx="6" fill="#C9A86A"/>'
         + label(155, 58, "⟦새어 나간 암호말|LEAKED PASSWORDS⟧", 12, "#142033", cls="d")
         + label(66, 92, "⟦사과 · 1234|apple · 1234⟧", 11, "#142033", "start") + label(66, 114, "⟦비밀번호 · 사과1|password · apple1⟧", 11, "#142033", "start")
         + label(66, 136, "⟦노란 개구리가 피리를…|yellow frog plays…⟧", 11, "var(--bad)", "start") + label(66, 158, "⟦…|…⟧", 11, "#142033", "start")
         + person(320, 100, s=0.75, face=FROWN + SWEAT, hat=None, shirt="#4A5A72")
         + bubble(270, 28, 190, 34, "⟦내 것도 있네 — 바꿔야지|mine is on it — time to change⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(200, 220, "⟦명부에 오르면 그 문 암호말만 바꿔요|on the list? change that door\'s word⟧", 11, "var(--ink)")
         + gate(600, 60, 0.8) + person(560, 130, s=0.75, face=SMILE, **GUARD) + ring(660, 150, 0.9) + phone(710, 150, "⟦417 293|417 293⟧", 0.7)
         + bubble(520, 20, 220, 34, "⟦암호말만으론 안 열어요|the word alone won\'t open it⟧", 11, "var(--panel)", "var(--good)", "bottom")
         + label(640, 240, "⟦반지도, 전화 숫자도 같이|the ring and the phone code too⟧", 11, "var(--muted)")
         + label(380, 285, "⟦암호말은 문 하나예요 — 좋은 문지기는 하나 더 물어요|a password is one lock — a good gatekeeper asks for one more⟧", 12, "var(--ink)", cls="d"))

LONG_I = icon('<rect x="6" y="14" width="52" height="28" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M14 28 h36" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/><path d="M18 42 l-4 10 l14 -10z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>')
DIFF_I = icon("".join(f'<circle cx="14" cy="{y}" r="5" fill="none" stroke="{c}" stroke-width="3"/><rect x="18" y="{y - 2}" width="28" height="4" fill="{c}"/><rect x="40" y="{y + 2}" width="3" height="5" fill="{c}"/>' for y, c in ((16, "#E9B44C"), (32, "var(--good)"), (48, "#5B8DEF"))))
BOX_I = icon('<rect x="10" y="24" width="44" height="30" rx="4" fill="#8B5E3C"/><rect x="8" y="18" width="48" height="10" rx="3" fill="#5A3B22"/><rect x="27" y="34" width="10" height="9" rx="2" fill="#E9B44C"/><path d="M29 34 v-4 a3 3 0 0 1 6 0 v4" stroke="#E9B44C" stroke-width="2" fill="none"/>')
HUSH_I = icon(f'<circle cx="32" cy="30" r="16" fill="{SKIN}"/><path d="M14 22 Q32 6 50 22 Z" fill="#4A5A72"/><circle cx="26" cy="28" r="2" fill="var(--night)"/><circle cx="38" cy="28" r="2" fill="var(--night)"/><rect x="30" y="32" width="4" height="20" rx="2" fill="{SKIN}" stroke="var(--night)" stroke-width="1.5"/>')

PAGE = {
    "slug": "password", "order": 61,
    "title": ("문지기에게 속삭이는 암호말", "The Word Whispered to the Gatekeeper"),
    "h1": ("<em>비밀번호</em>가 뭐예요?", "What is a <em>Password</em>?"),
    "sub": ("비밀번호(Password)를 성문 문지기에게 속삭이는 암호말 이야기로 풀어봤어요.",
            "Passwords, told as a story about the secret word you whisper to the gatekeeper."),
    "panels": [
        {"svg": P1, "alt": ("성문 앞 문지기가 '암호말은?' 하고 묻고 내가 '사과!' 하고 답함. 옆에서 도둑이 사과, 배, 포도, 1234 라고 적은 종이를 들고 '하나씩 다 말해 볼게' 함", "A gatekeeper at the gate asks for the password and I answer Apple. Beside us a thief holds a list — apple, pear, grape, 1234 — and says he will just try them all"),
         "caption": ("성문 문지기는 암호말을 물어요. 도둑은 암호말을 하나씩 맞춰 봐요.", "The gatekeeper asks for the password. The thief tries to guess it, one word at a time."),
         "small": ("암호말이 '사과' 같은 짧은 말이면, 도둑은 몇 번 안 가서 맞혀요. 도둑은 지치지 않거든요.", "If the word is something short like Apple, the thief gets it in a few tries. Thieves don\'t get tired.")},
        {"svg": P2, "alt": ("셋으로 나뉜 그림: '사과'와 1초 시계, 똑같은 '사과'를 쓰는 성 세 개, 그리고 사과·1234·비밀번호가 적힌 새어 나간 명부를 든 도둑", "Three parts: the word apple next to a one-second clock, three castles all using apple, and a thief holding a leaked list reading apple, 1234, password"),
         "caption": ("짧으면 금방 맞히고, 똑같으면 하나 새도 다 열려요.", "A short word is guessed fast; the same word everywhere means one leak opens every door."),
         "small": ("게다가 도둑은 남들이 많이 쓰는 말 명부를 이미 갖고 있어요. '사과', '1234', '비밀번호'는 명부 맨 위에 있어요.", "And the thief already owns a list of the words everyone uses. Apple, 1234, and password sit right at the top.")},
        {"svg": P3, "hero": True, "alt": ("내가 문지기에게 '보라색 고래가 빵을 구워요' 하고 아주 작게 속삭이고 문지기는 웃음. 멀리 도둑은 '…뭐라고?' 하며 못 들음, 맞히려면 백만 년", "I whisper a long sentence — purple whale bakes bread — to the smiling gatekeeper. A thief far away says what was that, and would need a million years to guess"),
         "caption": ("비밀번호는 문지기에게 속삭이는 암호말이에요.", "A password is the secret word you whisper to the gatekeeper."),
         "small": ("문지기와 나, 둘만 아는 말이에요. 길게, 문마다 다르게, 상자에 넣어두고, 아무한테도 안 불러줘요.", "Only the gatekeeper and I know it. Long, different at every door, kept in a box, and told to no one."),
         "tricks": (4, [
             (LONG_I, ("긴 문장으로", "Make it a sentence"), ("외우긴 쉽고 맞히긴 어려워요", "easy to remember, hard to guess"), "calm"),
             (DIFF_I, ("문마다 다르게", "Different at every door"), ("하나 새도 하나만", "one leak, one door"), "warm"),
             (BOX_I, ("잠긴 상자에", "Keep them in a locked box"), ("외울 건 상자 열쇠 하나", "remember only the box key")),
             (HUSH_I, ("아무한테도", "Tell no one"), ("문지기도 되묻지 않아요", "even the gatekeeper never asks twice")),
         ])},
        {"svg": P4, "alt": ("자물쇠 달린 상자 안에 성문·창고·우물마다 다른 긴 암호말 카드가 들어 있음. 내가 상자 열쇠 하나를 들고 '상자 열쇠 하나만 외워요'. 새 문이 생기면 상자가 새 암호말을 지어줌", "A locked box holds cards with a different long password for the gate, the storeroom, and the well. I hold one key and say I remember only the box key. When a new door appears, the box invents a new word"),
         "caption": ("암호말은 잠긴 상자에 넣어두고, 상자 열쇠 하나만 외워요.", "The words live in a locked box, and I remember only the key to the box."),
         "small": ("문이 백 개여도 외울 건 하나예요. 새 문이 생기면 상자가 길고 이상한 새 암호말을 지어주고, 갈 때마다 꺼내서 속삭여 줘요.", "A hundred doors, one thing to remember. For a new door the box invents a long strange word, and hands it to me every time I go."),
},
        {"svg": P5, "alt": ("마을 게시판에 새어 나간 암호말 명부가 붙어 있고, 내 것이 보여 땀 흘리며 '바꿔야지'. 오른쪽 성문 문지기는 '암호말만으론 안 열어요' 하며 반지와 전화 숫자도 같이 봄", "A board in the village lists leaked passwords; I spot mine, sweat, and decide to change it. At the gate the gatekeeper says the word alone won\'t open it and checks a ring and a phone code too"),
         "caption": ("새면 그 문 것만 바꿔요. 그리고 좋은 문지기는 암호말 말고 하나를 더 물어요.", "If it leaks, change that door\'s word. And a good gatekeeper asks for one thing more."),
         "small": ('새어 나간 명부에 내 말이 있으면 그 문 암호말만 바꾸면 돼요 — 문마다 다르니까요. 문지기는 <a href="mfa-ko.html">하나 더 확인</a>하거나 아예 <a href="passkey-ko.html">반지</a>를 봐요.',
                   'If my word shows up on the leaked list, I change only that door — every door has its own. The gatekeeper also <a href="mfa-en.html">checks one more thing</a>, or looks at a <a href="passkey-en.html">ring</a> instead.')},
    ],
    "summary": (("<b>비밀번호</b> = 문지기와 나, 둘만 아는 <b>속삭이는 암호말</b>. <b>길게</b>, <b>문마다 다르게</b>, <b>잠긴 상자</b>에 넣고, <b>아무한테도</b> 안 불러줘요.",
                 "<b>Password</b> = a <b>whispered word</b> only the gatekeeper and I know. <b>Long</b>, <b>different at every door</b>, kept in a <b>locked box</b>, and <b>told to no one</b>."),
                ("Password. 나만 아는 문자열로 내가 나임을 증명해요. 길이가 짧거나, 여러 곳에 재사용하거나, 흔한 단어를 쓰면 무차별 대입과 크리덴셜 스터핑에 금방 뚫려요. 패스프레이즈, 비밀번호 관리자, MFA 가 그 약점을 메워요.",
                 "A secret string that proves I am me. Short, reused, or common passwords fall quickly to brute force and credential stuffing. Passphrases, password managers, and MFA cover those weak spots.")),
    "glossary": [
        ("패스프레이즈", "Passphrase", ("문장으로 된 긴 암호말.", "A password that is a sentence."), ("'보라색 고래가 빵을 구워요'. 외우긴 쉽고 맞히긴 훨씬 어려워요. 길이가 이상한 글자보다 힘이 세요.", "Purple whale bakes bread. Easy to remember, far harder to guess — length beats weird characters.")),
        ("비밀번호 관리자", "Password manager", ("잠긴 열쇠 상자.", "The locked key box."), ("문마다 다른 긴 암호말을 지어주고 대신 기억해요. 나는 상자 열쇠(마스터 비밀번호) 하나만 외워요.", "Invents and remembers a long, different password for every door. I remember only the box key — the master password.")),
        ("재사용", "Password reuse", ("문마다 똑같은 암호말.", "The same word at every door."), ("한 성에서 새면 다른 성 문도 다 열려요. 도둑이 제일 먼저 해 보는 일이에요.", "Leak it at one castle and every other gate opens too. The first thing a thief tries.")),
        ("크리덴셜 스터핑", "Credential stuffing", ("새어 나간 명부로 문마다 찔러 보기.", "Trying a leaked list at every gate."), ('다른 성에서 샌 이름과 암호말 명부를 들고 우리 성문에도 하나씩 넣어 봐요. 재사용만 안 해도 막혀요. → <a href="bruteforce-ko.html">열쇠 천 개를 다 꽂아보는 도둑</a>', 'A list of names and words leaked elsewhere, tried one by one at our gate. Not reusing passwords stops it cold. → <a href="bruteforce-en.html">the thief with a thousand keys</a>')),
        ("해싱", "Hashing", ("문지기 일지엔 지문만.", "The gatekeeper writes down a fingerprint, not the word."), ('문지기도 암호말을 그대로 적어두지 않아요. 지문만 적어두고, 내가 말하면 지문을 찍어 비교해요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>', 'Even the gatekeeper never writes the word itself — only its fingerprint, compared when I speak. → <a href="hashing-en.html">a fingerprint for everything</a>')),
        ("MFA", "MFA", ("암호말 말고 하나 더.", "One more thing besides the word."), ('반지나 전화 숫자를 같이 물어요. 암호말이 새도 문은 안 열려요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'The ring or the phone code, asked along with the word. A leaked word still opens nothing. → <a href="mfa-en.html">the gatekeeper who checks three times</a>')),
        ("패스키", "Passkey", ("암호말 없는 반지.", "A ring instead of a word."), ('외울 것도, 속삭일 것도 없어요. 새어 나갈 말이 아예 없어요. → <a href="passkey-ko.html">성문을 알아보는 반지</a>', 'Nothing to remember, nothing to whisper — nothing to leak. → <a href="passkey-en.html">the ring that knows its gate</a>')),
        ("유출 확인", "Breach check", ("새어 나간 명부 들여다보기.", "Reading the leaked list."), ("내 말이 명부에 올랐는지 알려주는 곳이 있어요 (Have I Been Pwned). 오르면 그 문 것만 바꿔요.", "Services like Have I Been Pwned tell you if your word is on a leaked list. If it is, change that one door.")),
    ],
}
