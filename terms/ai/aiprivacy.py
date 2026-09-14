from _draw import *
from _world import *

CLERK = dict(hat=None, shirt="#4A5A72")
ARROW = '<path d="M{0} {1} L{2} {3}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'

# 1. 서기가 손님 명부를 통째로 빌린 앵무새 창구에 붙여 넣어요
P1 = svg(300, sky(300)
         + note(30, 40, 170, 140, "⟦손님 명부|GUEST LIST⟧", ("⟦김OO 010-1234-…|Kim 010-1234-…⟧", "⟦이OO 카드 4321…|Lee card 4321…⟧", "⟦박OO 주소 …|Park address …⟧", "⟦… 500명|… 500 people⟧"), 1.0)
         + person(250, 120, s=0.9, face=EYES, **CLERK) + label(277, 250, "⟦서기|clerk⟧", 11, "var(--muted)")
         + bubble(205, 20, 240, 40, "⟦이거 앵무새 학교로 가나요?|does this go to the parrot school?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + "".join(bean(330 + i * 30, 232 - (i % 2) * 6, 0.8) for i in range(4))
         + ARROW.format(320, 200, 405, 200)
         + perch(480, 200, 140) + parrot(480, 160, 1.1) + label(480, 262, "⟦빌린 앵무새 창구|the rented parrot\'s counter⟧", 11, "var(--muted)")
         + '<rect x="590" y="60" width="150" height="70" rx="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(665, 88, "⟦앵무새 학교로?|to the parrot school?⟧", 11, "var(--ink)", cls="d") + label(665, 112, "⟦다음 책이 되나?|the next book?⟧", 11, "var(--muted)")
         + label(380, 282, "⟦명부를 통째로 붙여 넣었어요 — 이 콩들은 어디로 가나요?|the whole list, pasted in — where do these beans go?⟧", 13, "var(--ink)"))

# 2. 왜 걱정: 빌린 앵무새는 남의 집 — 콩이 남고, 책이 되고, 다른 손님 답에 섞여요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<path d="M40 130 L200 50 L360 130 V290 H40 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
         + label(200, 118, "⟦남의 집|someone else\'s house⟧", 12, "var(--ink)", cls="d")
         + tray(50, 180, 140, 60) + beans(85, 168, ("⟦김OO|Kim⟧", "⟦010…|010…⟧"), 0.9, 44)
         + label(120, 268, "⟦쟁반에 남은 콩|beans left on the tray⟧", 10, "var(--muted)")
         + parrot(225, 190, 0.9)
         + books(310, 270, 4, 0.9) + label(310, 205, "⟦다음 학교 책?|the next school\'s book?⟧", 10, "var(--bad)")
         + ARROW.format(250, 235, 268, 240)
         + person(430, 110, s=0.85, face=FROWN, **GUEST) + label(455, 222, "⟦다른 손님|another guest⟧", 11, "var(--muted)")
         + parrot(580, 150, 1.0, talk=True) + bubble_parrot(510, 30, 230, 44, "⟦김OO 번호는 010-1234…|Kim\'s number is 010-1234…⟧", 11, bad=True)
         + label(600, 245, "⟦책이 되면 다른 손님 답에 섞여 나와요|once in the books, it can pop out for another guest⟧", 10, "var(--bad)")
         + label(380, 300, "⟦빌린 앵무새는 남의 집 — 콩이 남고, 책이 되고, 다른 답에 섞일 수 있어요|a rented parrot lives in someone else\'s house — beans can stay, become books, and leak into other answers⟧", 11, "var(--bad)"))

# 3. AI 프라이버시 = 비밀 콩은 가리거나 우리 집 앵무새에게만, 그리고 학습에 안 쓴다는 약속 (hero)
P3 = svg(360, sky(360)
         + note(20, 50, 140, 100, "⟦명부|LIST⟧", ("⟦김OO 010-…|Kim 010-…⟧", "⟦이OO 카드…|Lee card…⟧"), 1.0)
         + ARROW.format(165, 100, 185, 100)
         + '<rect x="190" y="80" width="110" height="120" rx="10" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/>'
         + label(245, 105, "⟦가리기 기계|MASKER⟧", 11, "var(--ink)", cls="d")
         + label(245, 150, "⟦김OO → 손님1|Kim → guest 1⟧", 11, "var(--ink)") + label(245, 175, "⟦010… → 번호표|010… → a tag⟧", 11, "var(--ink)")
         + ARROW.format(305, 150, 320, 150)
         + bean(345, 150, 1.3, text="⟦손님1|guest 1⟧") + bean(395, 150, 1.3, text="⟦번호표|tag⟧")
         + perch(460, 240, 150) + parrot(460, 200, 1.3, talk=True)
         + person(560, 190, s=0.8, face=SMILE, **TRAINER) + label(590, 305, "⟦조련사가 약속을 받아요|the trainer gets the promise⟧", 11, "var(--muted)")
         + note(590, 50, 150, 120, "⟦계약|CONTRACT⟧", ("⟦학습에 안 씀 ✓|no training ✓⟧", "⟦30일 뒤 지움 ✓|deleted in 30 days ✓⟧", "⟦우리 나라 안 ✓|stays in our region ✓⟧"), 1.0)
         + label(380, 340, "⟦AI 프라이버시 = 비밀 콩은 가리거나 우리 집 앵무새에게만, 그리고 학습에 안 쓴다는 약속|AI privacy: mask the secret beans or keep them for our own parrot — and get a promise they won\'t become books⟧", 12, "var(--ink)", cls="d"))

# 4. 흐름: 명부 → 가리기 기계 → 번호표 콩 → 앵무새 → 답 → 우리 집에서 되돌림, 옆에 계약 두루마리
P4 = svg(320, sky(320)
         + note(20, 40, 120, 90, "⟦명부|LIST⟧", ("⟦김OO 010-…|Kim 010-…⟧", "⟦이OO …|Lee …⟧"), 1.0)
         + ARROW.format(145, 85, 165, 85)
         + note(170, 40, 120, 90, "⟦번호표 표|TAG TABLE⟧", ("⟦김OO ↔ 손님1|Kim ↔ guest 1⟧", "⟦이OO ↔ 손님2|Lee ↔ guest 2⟧"), 1.0)
         + ARROW.format(295, 85, 320, 85)
         + bean(340, 95, 1.2, text="⟦손님1|guest 1⟧") + bean(390, 95, 1.2, text="⟦손님2|guest 2⟧")
         + ARROW.format(418, 95, 440, 95)
         + perch(470, 150, 120) + parrot(470, 110, 1.0, talk=True)
         + ARROW.format(500, 90, 555, 85)
         + note(560, 40, 180, 90, "⟦답|ANSWER⟧", ("⟦손님1 님께 안내…|Dear guest 1, …⟧", "⟦손님2 님께 …|Dear guest 2, …⟧"), 1.0)
         + '<path d="M650 135 V225 H592" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5" fill="none"/><path d="M600 217 L588 225 L600 233" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + note(410, 180, 170, 90, "⟦우리 집에서 되돌림|UNMASKED AT HOME⟧", ("⟦손님1 → 김OO|guest 1 → Kim⟧", "⟦김OO 님께 안내…|Dear Kim, …⟧"), 1.0)
         + note(190, 180, 180, 90, "⟦계약 두루마리|CONTRACT SCROLL⟧", ("⟦학습 안 함 ✓|no training ✓⟧", "⟦30일 뒤 지움 ✓|deleted after 30 days ✓⟧"), 1.0)
         + '<path d="M40 205 L95 170 L150 205 V260 H40 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(95, 230, "⟦번호표 표는|the tag table⟧", 10, "var(--ink)", cls="d") + label(95, 248, "⟦우리 집에만|stays at home⟧", 10, "var(--ink)", cls="d")
         + label(380, 300, "⟦밖으로 나가는 건 번호표 콩뿐, 이름은 우리 집에서 되돌려요|only tagged beans leave the house; the names come back at home⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 가려도 조합하면 알아봐요 + 이미 읽은 책은 되돌릴 수 없어요
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + note(40, 50, 200, 120, "⟦가린 명부|MASKED LIST⟧", ("⟦손님1: 서울, 40대|guest 1: Seoul, 40s⟧", "⟦의사, 빨간 차|doctor, red car⟧", "⟦딸 둘, 6층|two kids, 6th floor⟧"), 1.0)
         + person(290, 90, s=0.8, face=EYES, **GUEST) + bubble(250, 20, 150, 36, "⟦…아, 김OO!|…oh, it\'s Kim!⟧", 11, "var(--panel)", "var(--bad)", "bottom")
         + label(190, 240, "⟦가려도 조합하면 알아봐요|masked, but the pieces add up⟧", 12, "var(--bad)")
         + parrot(450, 190, 0.9, mood="sweat")
         + books(560, 230, 6, 1.1) + note(620, 60, 120, 60, "⟦책 속에|IN THE BOOK⟧", ("⟦김OO 010-…|Kim 010-…⟧",), 0.9)
         + ARROW.format(640, 125, 600, 150)
         + label(600, 262, "⟦이미 읽은 책은 되돌릴 수 없어요|a book already read can\'t be unread⟧", 11, "var(--bad)")
         + label(380, 300, "⟦그래서 처음부터 비밀 콩은 안 주는 게 제일이에요|so the best move is never handing over the secret bean at all⟧", 12, "var(--ink)", cls="d"))

MASK_I = icon(f'<ellipse cx="32" cy="34" rx="18" ry="12" fill="{BEAN}"/><rect x="18" y="28" width="28" height="12" rx="3" fill="#142033"/><path d="M22 34 h20" stroke="#FFF8E7" stroke-width="2" stroke-dasharray="3 3"/>')
CONTRACT_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 20 h20 M22 30 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M24 44 l6 6 l12 -12" stroke="var(--good)" stroke-width="3" fill="none"/>')
HOME_I = icon(f'<path d="M8 32 L32 12 L56 32 V56 H8 Z" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><circle cx="32" cy="30" r="6" fill="{PARROT}"/><ellipse cx="32" cy="44" rx="7" ry="10" fill="{PARROT}"/>')
LOG_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h10 M20 32 h10 M20 42 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><rect x="34" y="18" width="12" height="8" rx="2" fill="#142033"/><rect x="34" y="28" width="12" height="8" rx="2" fill="#142033"/><rect x="34" y="38" width="12" height="8" rx="2" fill="#142033"/>')

PAGE = {
    "slug": "aiprivacy", "order": 39,
    "title": ("앵무새에게 준 비밀 콩", "The Secret Beans We Gave the Parrot"),
    "h1": ("<em>AI 프라이버시</em>가 뭐예요?", "What is <em>AI Privacy</em>?"),
    "sub": ("AI 프라이버시를, 빌린 앵무새에게 손님 명부를 통째로 주면 어디로 가는지, 비밀 콩은 어떻게 가리고 약속을 받는지 이야기로 풀어봤어요.",
            "AI privacy, told as a story about what happens when you paste the whole guest list into a rented parrot — and how to mask the secret beans and get a promise."),
    "panels": [
        {"svg": P1, "alt": ("서기가 500명 손님 명부(이름·전화·카드)를 빌린 앵무새 창구에 붙여 넣으며 '이거 앵무새 학교로 가나요?'라고 물음. 옆 팻말: 앵무새 학교로? 다음 책이 되나?", "A clerk pastes a 500-person guest list (names, phones, cards) into the rented parrot\'s counter and asks whether it goes to the parrot school; a sign asks: to the parrot school? the next book?"),
         "caption": ("서기가 손님 명부를 통째로 앵무새에게 붙여 넣었어요.", "The clerk pasted the whole guest list into the parrot."),
         "small": ("편하긴 한데, 이 콩들은 어디로 가나요? 앵무새 학교 책이 되나요?", "Handy — but where do these beans go? Do they become books at the parrot school?")},
        {"svg": P2, "alt": ("남의 집 안: 쟁반에 김OO 010… 콩이 남아 있고, 앵무새 옆 책 더미에 '다음 학교 책?' 표시. 오른쪽에서 다른 손님에게 앵무새가 '김OO 번호는 010-1234…'라고 말함", "Inside someone else\'s house: beans reading Kim 010… stay on the tray, and the book pile next to the parrot is marked next school\'s book?; on the right the parrot tells another guest Kim\'s number is 010-1234…"),
         "caption": ("빌린 앵무새는 남의 집이에요 — 콩이 남고, 책이 되고, 다른 답에 섞일 수 있어요.", "A rented parrot lives in someone else\'s house — beans can stay, become books, and leak into other answers."),
         "small": ('<a href="openweights-ko.html">빌린 앵무새</a>에게 준 콩은 남의 <a href="context-ko.html">쟁반</a>에 놓여요. 그 집이 콩을 남겨 두거나 다음 학교 책으로 쓰면, 언젠가 다른 손님 답에 섞여 나올 수 있어요.',
                   'Beans given to a <a href="openweights-en.html">rented parrot</a> land on someone else\'s <a href="context-en.html">tray</a>. If that house keeps them or uses them as the next school\'s books, they can one day pop out in another guest\'s answer.')},
        {"svg": P3, "hero": True, "alt": ("명부가 가리기 기계로 들어가 '김OO → 손님1, 010… → 번호표'가 되고, 번호표 콩만 앵무새에게 감. 조련사가 '학습에 안 씀, 30일 뒤 지움, 우리 나라 안' 계약을 받음", "The list goes through a masker that turns Kim into guest 1 and the phone into a tag; only tagged beans reach the parrot. A trainer holds a contract: no training, deleted in 30 days, stays in our region"),
         "caption": ("AI 프라이버시는 비밀 콩을 가리거나 우리 집 앵무새에게만 주고, 학습에 안 쓴다는 약속을 받는 거예요.", "AI privacy is masking the secret beans or keeping them for our own parrot — and getting a promise they won\'t become books."),
         "small": ('비밀 콩 = 이름·전화·카드 같은 개인정보와 회사 비밀. 붙여 넣기 전에 <a href="masking-ko.html">가리고</a>, 계약으로 약속을 받아요.',
                   'Secret beans are personal data — names, phones, cards — and company secrets. <a href="masking-en.html">Mask</a> them before pasting, and get the promise in a contract.'),
         "tricks": (4, [
             (MASK_I, ("붙이기 전에 가려요", "Mask before pasting"), ("이름·번호 → 번호표", "names and numbers become tags"), "calm"),
             (CONTRACT_I, ("약관을 확인해요", "Check the terms"), ("'학습에 안 쓴다'가 있나", "does it say no training?"), "calm"),
             (HOME_I, ("비밀 콩은 우리 집 앵무새", "Secrets go to our own parrot"), ("남의 집엔 안 보내요", "never to someone else\'s house"), "warm"),
             (LOG_I, ("대화 기록도 가려요", "Mask the chat logs too"), ("남긴 기록에 비밀 콩 없게", "no secret beans in what we keep"), "warm"),
         ])},
        {"svg": P4, "alt": ("명부 → 번호표 표(김OO ↔ 손님1) → 손님1·손님2 콩 → 앵무새 → '손님1 님께' 답 → 우리 집에서 김OO으로 되돌림. 옆에 '학습 안 함, 30일 뒤 지움' 계약 두루마리와 '번호표 표는 우리 집에만' 집", "List → tag table (Kim ↔ guest 1) → guest 1 and guest 2 beans → parrot → an answer for guest 1 → unmasked back to Kim at home; beside it a contract scroll (no training, deleted after 30 days) and a house noting the tag table stays at home"),
         "caption": ("밖으로 나가는 건 번호표 콩뿐이고, 이름은 우리 집에서 되돌려요.", "Only tagged beans leave the house; the names come back at home."),
         "small": ('번호표 표는 우리 집에만 있어요. 앵무새는 손님1이 누군지 몰라도 답을 잘 써요. 계약엔 학습 제외, 지우는 날짜, 데이터가 머무는 나라를 적어요.',
                   'The tag table never leaves home. The parrot writes a fine answer without knowing who guest 1 is. The contract spells out no training, the deletion date, and which country the data stays in.')},
        {"svg": P5, "alt": ("가린 명부(손님1: 서울, 40대, 의사, 빨간 차, 딸 둘, 6층)를 본 손님이 '아, 김OO!'이라고 알아봄. 오른쪽엔 땀 흘리는 앵무새와 책 속에 이미 들어간 '김OO 010-…'", "A guest reads the masked list (guest 1: Seoul, 40s, doctor, red car, two kids, 6th floor) and says oh, it\'s Kim; on the right a sweating parrot and a book that already contains Kim 010-…"),
         "caption": ("가려도 조합하면 알아봐요. 그리고 이미 읽은 책은 되돌릴 수 없어요.", "Masked pieces can add up to a name. And a book already read can\'t be unread."),
         "small": ('그래서 처음부터 비밀 콩은 안 주는 게 제일이에요. 어떤 콩이 비밀인지는 <a href="classification-ko.html">등급표</a>로, 원칙은 보안 성의 <a href="privacy-ko.html">프라이버시</a>에서. 앵무새 <a href="memory-ko.html">수첩</a>에 남는 것도 같은 문제예요.',
                   'So the best move is never handing over the secret bean at all. Which beans are secret: the <a href="classification-en.html">label chart</a>; the principles: the castle\'s <a href="privacy-en.html">privacy</a> page. What sticks in the parrot\'s <a href="memory-en.html">notebook</a> is the same problem.')},
    ],
    "summary": (("<b>AI 프라이버시</b> = 앵무새에게 주는 콩 중 <b>비밀 콩</b>(개인정보·회사 비밀)을 <b>가리거나 우리 집 앵무새에게만</b> 주고, <b>학습에 안 쓴다는 약속</b>을 받는 것. 가려도 조합하면 알아볼 수 있고 읽은 책은 못 돌리니, 처음부터 안 주는 게 제일이에요.",
                 "<b>AI privacy</b> = <b>masking the secret beans</b> (personal data, company secrets) or keeping them for <b>our own parrot</b>, and getting a <b>promise they won\'t become books</b>. Masked pieces can still add up and read books can\'t be unread, so the best move is not handing them over at all."),
                ("AI Privacy. 프롬프트·대화 기록·파인튜닝 데이터에 든 개인정보와 기밀을 다루는 일이에요. 입력 전 마스킹·가명처리, 학습 제외(opt-out)와 보존 기간·리전을 정한 기업 계약(DPA), 자체 호스팅(오픈 웨이트)이 도구예요. 가명 데이터도 재식별될 수 있고, 이미 학습된 정보는 제거가 어려워요.",
                 "Handling personal data and confidential information in prompts, chat logs and fine-tuning data. The tools are masking and pseudonymization before input, enterprise contracts (DPAs) fixing training opt-out, retention periods and data region, and self-hosting (open weights). Pseudonymized data can still be re-identified, and information already trained in is hard to remove.")),
    "glossary": [
        ("데이터 프라이버시", "Data privacy", ("비밀 콩을 지키는 일.", "Keeping the secret beans safe."), ('원칙은 보안 성에서. → <a href="privacy-ko.html">프라이버시</a>', 'The principles live in the castle. → <a href="privacy-en.html">privacy</a>')),
        ("학습 제외", "Training opt-out", ("'다음 책으로 안 씀' 약속.", "The promise: not the next book."), ("약관이나 설정에서 확인해요. 기본값이 '씀'인 곳도 있어요.", "Check the terms or settings — some places default to using it.")),
        ("데이터 보존 정책", "Data retention policy", ("콩을 며칠 뒤 지우나.", "How many days before the beans are deleted."), ('30일? 영원히? 계약에 적어요. → <a href="retention-ko.html">보존</a>', '30 days? Forever? Put it in the contract. → <a href="retention-en.html">retention</a>')),
        ("마스킹 · 가명처리", "Masking · Pseudonymization", ("이름 → 번호표.", "Name → tag."), ('번호표 표는 우리 집에만. → <a href="masking-ko.html">마스킹</a>', 'The tag table stays home. → <a href="masking-en.html">masking</a>')),
        ("데이터 위치", "Data residency", ("콩이 머무는 나라.", "The country the beans stay in."), ("법이 나라마다 달라서 '우리 나라 안'을 계약에 넣어요.", "Laws differ by country, so the contract says which region.")),
        ("기업 계약", "Enterprise agreement · DPA", ("계약 두루마리 한 장.", "One contract scroll."), ("학습 제외·보존 기간·위치·사고 시 알림을 한 장에 적은 약속이에요.", "One page promising no training, a retention period, a region, and notice if something goes wrong.")),
        ("메모리", "Memory", ("앵무새의 수첩.", "The parrot\'s notebook."), ('수첩에 적힌 비밀 콩도 같은 문제예요. → <a href="memory-ko.html">앵무새의 수첩</a>', 'Secret beans written in the notebook are the same problem. → <a href="memory-en.html">the parrot\'s notebook</a>')),
        ("오픈 웨이트", "Open weights", ("우리 집 앵무새.", "Our own parrot."), ('비밀 콩은 남의 집에 안 보내요. → <a href="openweights-ko.html">우리 집 앵무새 vs 빌린 앵무새</a>', 'Secret beans never leave home. → <a href="openweights-en.html">our own parrot vs a rented one</a>')),
    ],
}
