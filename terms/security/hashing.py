from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")


def book(x, y, s=1.0, color="var(--accent)", pages=6, mark=None, size=1.0):
    w, h = 80 * size, 100 * size
    rows = "".join(f'<rect x="{-w / 2 + 10}" y="{-h / 2 + 14 + i * (h - 24) / pages}" width="{w - 20 - (i * 11) % 18}" height="3" rx="1.5" fill="var(--line)"/>' for i in range(pages))
    m = f'<rect x="{-w / 2 + 10}" y="{-h / 2 + 14 + mark * (h - 24) / pages - 2}" width="{w - 20}" height="7" rx="2" fill="var(--bad)"/>' if mark is not None else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="3" fill="{color}"/>'
            f'<rect x="{-w / 2 + 6}" y="{-h / 2 + 6}" width="{w - 12}" height="{h - 12}" rx="2" fill="var(--panel)"/>{rows}{m}</g>')


def fingerprint(x, y, text, s=1.0, color="var(--good)"):
    arcs = "".join(f'<path d="M-{r} 0 a{r} {r} 0 0 1 {2 * r} 0" stroke="{color}" stroke-width="2" fill="none"/>' for r in (5, 9, 13))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-56" y="-22" width="112" height="44" rx="6" fill="var(--panel)" stroke="{color}" stroke-width="2"/>'
            f'<g transform="translate(-36,4)">{arcs}</g>{label(12, 5, text, 13, color)}</g>')


def machine(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="-40" width="100" height="80" rx="10" fill="var(--night)"/>'
            f'<rect x="-40" y="-30" width="80" height="26" rx="4" fill="var(--sky)"/>{label(0, -12, "⟦지문 기계|HASH⟧", 12, "#142033")}'
            f'<circle cx="-20" cy="18" r="6" fill="var(--good)"/><circle cx="0" cy="18" r="6" fill="var(--accent)"/><circle cx="20" cy="18" r="6" fill="var(--bad)"/></g>')


# 1. 바뀌었는지 어떻게 알까
P1 = svg(280, sky(280) + book(200, 130, 1.1) + book(420, 130, 1.1, mark=3)
         + label(200, 210, "⟦원래 그림책|the original⟧", 12, "var(--muted)") + label(420, 210, "⟦한 줄 바뀐 그림책|one line changed⟧", 12, "var(--muted)")
         + label(310, 130, "=?", 30, "var(--accent)", cls="d")
         + person(600, 100, s=0.9, hat=None, shirt="#4A5A72", face=FROWN)
         + label(380, 262, "⟦한 페이지만 바꿔치기해도 겉으론 똑같아요|swap one page and it still looks the same⟧", 13, "var(--muted)"))

# 2. 한 장씩 비교해야 한다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + book(150, 130, 1.0) + book(330, 130, 1.0, mark=3)
         + person(440, 80, s=0.9, face=FROWN + SWEAT, **CLERK)
         + "".join(f'<rect x="{520 + (i % 6) * 26}" y="{70 + (i // 6) * 30}" width="20" height="26" rx="2" fill="var(--panel)" stroke="var(--line)" stroke-width="1.5"/>' for i in range(18))
         + label(600, 190, "⟦1,000장|1,000 pages⟧", 14, "var(--bad)", cls="d")
         + '<g transform="translate(680,230)"><circle r="22" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -14 V0 L9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(300, 260, "⟦천 장짜리 책이면 하루 종일이에요|a thousand-page book takes all day⟧", 13, "var(--muted)"))

# 3. 해시 = 물건마다 찍는 짧은 지문 (hero)
P3 = svg(360, sky(360)
         + book(80, 90, 0.7) + '<path d="M130 90 L180 90" stroke="var(--good)" stroke-width="3"/><path d="M170 80 L182 90 L170 100" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + machine(250, 90, 0.8) + '<path d="M300 90 L350 90" stroke="var(--good)" stroke-width="3"/><path d="M340 80 L352 90 L340 100" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + fingerprint(430, 90, "a3f9·7c1e", 1.0)
         + book(80, 220, 0.7, mark=3) + '<path d="M130 220 L180 220" stroke="var(--bad)" stroke-width="3"/><path d="M170 210 L182 220 L170 230" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + machine(250, 220, 0.8) + '<path d="M300 220 L350 220" stroke="var(--bad)" stroke-width="3"/><path d="M340 210 L352 220 L340 230" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + fingerprint(430, 220, "e02b·91d4", 1.0, "var(--bad)")
         + label(430, 260, "⟦한 줄만 바뀌어도 완전히 달라요|one line changed, a completely different print⟧", 12, "var(--bad)")
         + '<path d="M560 150 L640 150" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 6"/><path d="M590 135 l20 30 M610 135 l-20 30" stroke="var(--bad)" stroke-width="4"/>'
         + fingerprint(600, 100, "a3f9·7c1e", 0.7) + book(690, 150, 0.5, color="var(--stone)")
         + label(640, 200, "⟦지문으로 책은 못 만들어요|you can\'t rebuild the book from the print⟧", 11, "var(--muted)")
         + label(380, 340, "⟦아무리 큰 책도 지문은 같은 크기예요|however big the book, the print is the same size⟧", 13, "var(--muted)"))

# 4. 지문은 세 곳에 쓴다
P4 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + book(80, 100, 0.5) + fingerprint(150, 60, "a3f9", 0.55) + fingerprint(150, 140, "a3f9", 0.55) + '<path d="M120 100 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round" transform="translate(70,0)"/>'
         + label(130, 200, "⟦바뀌었나 확인|did it change?⟧", 14, "var(--ink)", cls="d") + label(130, 222, "⟦받은 책의 지문이 같은가|does the copy\'s print match⟧", 11, "var(--muted)")
         + '<g transform="translate(380,90)"><rect x="-70" y="-30" width="140" height="70" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(-56, -10, "⟦지민|Jimin⟧", 11, "#142033", "start") + label(-56, 10, "⟦태오|Taeo⟧", 11, "#142033", "start") + label(56, -10, "9e1c·44a0", 11, "var(--good)", "end") + label(56, 10, "b77d·02f3", 11, "var(--good)", "end") + label(0, 32, "⟦암호말은 안 적어요|no passwords written⟧", 9, "var(--muted)") + "</g>"
         + label(380, 200, "⟦암호말 대신 지문 보관|prints instead of passwords⟧", 14, "var(--ink)", cls="d") + label(380, 222, "⟦장부를 훔쳐도 지문뿐|steal the ledger, get only prints⟧", 11, "var(--muted)")
         + '<g transform="translate(630,90)"><rect x="-24" y="-34" width="48" height="64" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(0, -20, "⟦수배|WANTED⟧", 9, "var(--bad)") + "</g>" + fingerprint(630, 110, "e02b", 0.55, "var(--bad)")
         + label(630, 200, "⟦도둑 물건 알아보기|spotting the thief\'s things⟧", 14, "var(--ink)", cls="d") + label(630, 222, "⟦전단에 적힌 지문|the print on the poster⟧", 11, "var(--muted)")
         + label(380, 295, "⟦셋 다 '숨기기'가 아니라 '알아보기'예요|all three are about recognizing, not hiding⟧", 13, "var(--muted)"))

# 5. 같은 암호말은 같은 지문
SALT = '<g transform="translate(0,0)"><path d="M-8 -14 h16 l3 24 h-22z" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><rect x="-6" y="-20" width="12" height="6" fill="var(--stone-dark)"/><circle cx="-3" cy="-26" r="1.5" fill="var(--stone-dark)"/><circle cx="3" cy="-28" r="1.5" fill="var(--stone-dark)"/><circle cx="0" cy="-31" r="1.5" fill="var(--stone-dark)"/></g>'
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + "".join(person(40 + i * 70, 60, s=0.55, hat=h, shirt="#4A5A72", face=SMILE) for i, h in enumerate((None, "#E9B44C", "var(--stone-dark)", "var(--good)")))
         + "".join(label(60 + i * 70, 140, "⟦사과|apple⟧", 11, "var(--muted)") for i in range(4))
         + "".join(fingerprint(60 + i * 70, 175, "9e1c", 0.5, "var(--bad)") for i in range(4))
         + label(190, 230, "⟦백 명이 '사과'면 지문도 백 명 다 같아요|a hundred apples, a hundred identical prints⟧", 11, "var(--bad)")
         + label(190, 300, "⟦도둑은 지문표를 만들어 두고 맞춰봐요|thieves keep a table of prints and match them⟧", 11, "var(--muted)")
         + "".join(person(420 + i * 70, 60, s=0.55, hat=h, shirt="#4A5A72", face=SMILE) for i, h in enumerate((None, "#E9B44C", "var(--stone-dark)", "var(--good)")))
         + "".join(f'<g transform="translate({440 + i * 70},128)">{SALT}</g>' for i in range(4))
         + "".join(fingerprint(440 + i * 70, 175, t, 0.5) for i, t in enumerate(("3a7f", "c04e", "71b9", "d2e6")))
         + label(570, 230, "⟦사람마다 소금을 조금 뿌려요|a pinch of salt for each person⟧", 12, "var(--good)")
         + label(570, 300, "⟦같은 '사과'인데 지문이 다 달라요|the same apple, four different prints⟧", 11, "var(--muted)"))

SIZE_I = icon('<rect x="6" y="10" width="20" height="44" rx="2" fill="var(--accent)"/><rect x="34" y="34" width="20" height="20" rx="2" fill="var(--accent)"/><rect x="8" y="58" width="48" height="4" rx="2" fill="var(--good)"/>')
CHANGE_I = icon('<rect x="8" y="14" width="22" height="30" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="12" y="28" width="14" height="3" fill="var(--bad)"/><path d="M34 29 H44" stroke="var(--muted)" stroke-width="2"/><text x="52" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">≠</text>')
ONEWAY_I = icon('<path d="M10 32 H40" stroke="var(--good)" stroke-width="3"/><path d="M38 24 L50 32 L38 40 Z" fill="var(--good)"/><path d="M50 44 H20" stroke="var(--bad)" stroke-width="3" stroke-dasharray="3 3"/><path d="M30 38 l-8 8 M22 38 l8 8" stroke="var(--bad)" stroke-width="3"/>')
SAME_I = icon('<rect x="8" y="14" width="18" height="24" rx="2" fill="var(--accent)"/><rect x="38" y="14" width="18" height="24" rx="2" fill="var(--accent)"/><text x="32" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="var(--good)">a3f9 = a3f9</text>')

PAGE = {
    "slug": "hashing", "order": 45,
    "title": ("물건마다 찍는 지문", "A Fingerprint for Every Thing"),
    "h1": ("<em>해시</em>가 뭐예요?", "What is a <em>Hash</em>?"),
    "sub": ("해시(Hash)를 물건마다 찍는 짧은 지문 이야기로 풀어봤어요.",
            "Hashing, told as a story about the short fingerprint every thing gets."),
    "panels": [
        {"svg": P1, "alt": ("그림책 두 권, 하나는 한 줄이 빨갛게 바뀜, 사이에 '=?'", "Two picture books, one with a single line changed to red, and =? between them"),
         "caption": ("그림책이 바뀌었는지 어떻게 알까요?", "How do you know a book was changed?"),
         "small": ("한 페이지만 바꿔치기해도 겉으론 똑같아요.", "Swap a single page and it still looks the same from outside.")},
        {"svg": P2, "alt": ("직원이 땀을 흘리며 책 두 권을 한 장씩 비교하고, 옆에 '1,000장'과 시계", "A sweating clerk compares two books page by page; beside them, 1,000 pages and a clock"),
         "caption": ("다 비교하려면 한 장씩 봐야 해요.", "To compare them, you'd read every page."),
         "small": ("천 장짜리 책이면 하루 종일이에요.", "A thousand-page book takes all day.")},
        {"svg": P3, "hero": True, "alt": ("지문 기계에 책을 넣으면 'a3f9·7c1e' 짧은 지문이 나오고, 한 줄 바뀐 책은 'e02b·91d4'. 지문에서 책으로 가는 화살표엔 X", "A hash machine turns a book into a short print a3f9·7c1e; the book with one line changed gives e02b·91d4; the arrow from print back to book is crossed out"),
         "caption": ("해시는 물건마다 찍는 짧은 지문이에요.", "A hash is the short fingerprint every thing gets."),
         "small": ("아무리 큰 책도 지문은 같은 크기. 한 글자만 바뀌어도 완전히 달라져요. 지문으로 책을 되만들 순 없어요.", "However big the book, the print is the same size. Change one letter and it's completely different. And you can't rebuild the book from it."),
         "tricks": (4, [
             (SIZE_I, ("늘 같은 크기", "Always the same size"), ("천 장이든 한 장이든", "a thousand pages or one"), "calm"),
             (CHANGE_I, ("한 글자만 바뀌어도", "One letter changed"), ("지문이 통째로 달라져요", "the whole print changes")),
             (ONEWAY_I, ("되돌릴 수 없음", "No way back"), ("지문으로 책을 못 만들어요", "the print won\'t rebuild the book"), "warm"),
             (SAME_I, ("같은 물건, 같은 지문", "Same thing, same print"), ("그래서 비교가 돼요", "which is what makes comparing work"), "calm"),
         ])},
        {"svg": P4, "alt": ("세 가지 쓰임: 받은 책의 지문 비교, 암호말 대신 지문이 적힌 장부, 수배 전단에 적힌 지문", "Three uses: comparing a received book's print, a ledger holding prints instead of passwords, and a print written on a wanted poster"),
         "caption": ("지문은 세 곳에 써요.", "Fingerprints get used in three places."),
         "small": ('바뀌었나 확인, 암호말 대신 지문 보관, <a href="ioc-ko.html">도둑 물건 알아보기</a>. 셋 다 숨기기가 아니라 알아보기예요.',
                   'Checking for changes, storing prints instead of passwords, <a href="ioc-en.html">spotting the thief\'s things</a>. All three are about recognizing, not hiding.')},
        {"svg": P5, "alt": ("왼쪽: '사과'를 쓰는 네 사람의 지문이 전부 9e1c로 같음. 오른쪽: 사람마다 소금을 뿌리니 지문이 다 달라짐", "Left: four people using apple all get the same print 9e1c. Right: with a pinch of salt each, the prints all differ"),
         "caption": ("같은 암호말은 같은 지문이 나와요.", "The same password gives the same print."),
         "small": ("백 명이 '사과'면 지문도 백 명 다 같아요 — 도둑은 지문표를 만들어 두고 맞춰봐요. 그래서 사람마다 소금을 조금 뿌려요. 그리고 지문은 봉인(암호화)이 아니에요.", "A hundred apples, a hundred identical prints — thieves keep a table and match them. So each person gets a pinch of salt. And a print isn't a seal (encryption).")},
    ],
    "summary": (("<b>해시</b> = 물건마다 찍는 <b>짧은 지문</b>. 한 글자만 바뀌어도 달라지고, 지문으로 물건을 <b>되만들 순 없어요</b>.",
                 "A <b>hash</b> = a <b>short fingerprint</b> for every thing. One letter changed and it differs; and you can <b>never rebuild</b> the thing from it."),
                ("Hash. 요즘 지문 기계는 SHA-256. 암호말 지문엔 소금을 뿌리고 일부러 느린 기계(bcrypt, argon2)를 써요. 암호화와 달라요 — 숨기는 게 아니라 알아보는 거예요.",
                 "Today's machine is SHA-256. For passwords, add salt and use a deliberately slow machine (bcrypt, argon2). It's not encryption — it recognizes, it doesn't hide.")),
    "glossary": [
        ("해시 함수", "Hash function", ("지문 기계.", "The fingerprint machine."), ("SHA-256이 요즘 것. 같은 걸 넣으면 늘 같은 지문.", "SHA-256 is the current one. Same input, same print, every time.")),
        ("다이제스트", "Digest", ("지문.", "The print."), ("늘 같은 길이. SHA-256은 64글자.", "Always the same length — 64 characters for SHA-256.")),
        ("일방향", "One-way", ("되돌릴 수 없음.", "No way back."), ('그래서 <a href="encryption-ko.html">암호화</a>가 아니에요. 열쇠도 없어요.', 'Which is why it isn\'t <a href="encryption-en.html">encryption</a>. There\'s no key at all.')),
        ("무결성 · 체크섬", "Integrity · checksum", ("바뀌었나 확인.", "Did it change?"), ("받은 책의 지문이 보낸 사람 지문과 같은지.", "Does the received book\'s print match the sender\'s.")),
        ("솔트", "Salt", ("사람마다 뿌리는 소금.", "A pinch of salt per person."), ("같은 암호말도 다른 지문이 되게. 지문표 공격을 막아요.", "So the same password gives different prints, beating the lookup table.")),
        ("충돌", "Collision", ("다른 물건, 같은 지문.", "Different things, same print."), ("MD5와 SHA-1은 이게 가능해져서 은퇴했어요.", "MD5 and SHA-1 retired once this became possible.")),
        ("bcrypt · argon2", "bcrypt · argon2", ("일부러 느린 지문 기계.", "A deliberately slow machine."), ("암호말용. 도둑이 백만 번 찍어보는 걸 느리게 해요.", "For passwords — slows a thief trying a million guesses.")),
        ("IOC 해시", "IOC hash", ("도둑 물건 지문.", "The print of the thief\'s things."), ('수배 전단에 적는 지문. → <a href="ioc-ko.html">남겨진 발자국</a>', 'The print written on the wanted poster. → <a href="ioc-en.html">the footprint</a>')),
    ],
}
