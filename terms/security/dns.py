from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")


def booth(x, y, s=1.0, name="⟦안내소|DIRECTORY⟧", color="var(--good)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-56" y="0" width="112" height="90" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-66 0 L0 -32 L66 0 Z" fill="{color}"/><rect x="-40" y="24" width="80" height="36" fill="var(--sky)"/>'
            f'<rect x="-46" y="60" width="92" height="8" fill="{WOOD}"/>{label(0, 110, name, 12, "var(--muted)")}</g>')


def bigbook(x, y, rows, s=1.0):
    lines = "".join(label(10, 30 + i * 18, a, 11, "#142033", "start") + label(150, 30 + i * 18, b, 11, "#142033", "end") for i, (a, b) in enumerate(rows))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="160" height="{40 + len(rows) * 18}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<path d="M80 0 V{40 + len(rows) * 18}" stroke="#C9A86A" stroke-width="1" stroke-dasharray="3 3"/>{lines}</g>')


def sign(x, y, text, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="0" width="12" height="60" fill="var(--stone-dark)"/>'
            f'<rect x="-50" y="-30" width="100" height="30" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="2"/>{label(0, -10, text, 12, "var(--ink)")}</g>')


ADDR = "⟦동쪽 3번길 7|East 3rd St. 7⟧"

# 1. 사람들은 이름만 안다
P1 = svg(300, sky(300) + person(80, 110, s=0.9, **ME)
         + bubble(40, 30, 230, 36, "⟦사진 성에 가고 싶어요|I want to go to the Photo Castle⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + sign(360, 200, "10.0.0.7", 0.9) + sign(470, 200, "10.0.0.12", 0.9) + sign(580, 200, "10.0.0.41", 0.9)
         + castle(560, 90, 0.3) + label(650, 70, "?", 30, "var(--accent)", cls="d")
         + label(380, 285, "⟦이름은 아는데, 길은 숫자 주소로만 찾아가요|you know the name, but roads only go by number⟧", 13, "var(--muted)"))

# 2. 숫자를 다 외울 순 없다
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + "".join(f'<g transform="translate({x},{y}) rotate({r})"><rect width="90" height="60" fill="#FFE97A"/>{label(45, 24, n, 11, "#142033")}{label(45, 44, a, 12, "#142033", cls="d")}</g>'
                   for x, y, r, n, a in ((60, 50, -6, "⟦사진 성|Photo⟧", "10.0.0.7"), (180, 70, 4, "⟦편지 성|Mail⟧", "10.0.0.12"), (300, 40, -3, "⟦회의 성|Meeting⟧", "10.0.0.41"), (420, 80, 5, "⟦시장|market⟧", "10.0.2.9"), (540, 45, -5, "⟦도서관|library⟧", "10.0.2.30")))
         + person(660, 120, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + bubble(560, 170, 190, 34, "⟦사진 성이 이사 갔대요…|the Photo Castle moved…⟧", 12, "var(--panel)", "var(--bad)", "right")
         + label(300, 250, "⟦성이 이사라도 가면 외운 게 다 틀려요|one castle moves, and everything you memorized is wrong⟧", 13, "var(--muted)"))

# 3. DNS = 이름을 주소로 바꿔주는 안내소 (hero)
P3 = svg(340, sky(340) + booth(380, 100) + person(362, 100, s=0.6, face=SMILE, **CLERK)
         + person(120, 130, s=0.9, **ME)
         + bubble(60, 40, 200, 34, "⟦사진 성이 어디예요?|Where\'s the Photo Castle?⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + bubble(440, 40, 200, 34, ADDR, 14, "var(--good-soft)", "var(--good)", "bottom")
         + bigbook(470, 200, (("⟦사진 성|Photo⟧", "10.0.0.7"), ("⟦편지 성|Mail⟧", "10.0.0.12"), ("⟦회의 성|Meeting⟧", "10.0.0.41")), 0.9)
         + '<path d="M180 200 L300 200" stroke="var(--accent)" stroke-width="3"/><path d="M290 190 L302 200 L290 210" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(380, 322, "⟦이름만 알면 돼요. 주소는 안내소가 알아요|you only need the name; the directory knows the address⟧", 13, "var(--muted)"))

# 4. 모르면 더 큰 안내소에 물어본다
CHAIN = (("⟦마을 안내소|town directory⟧", "var(--good)"), ("⟦나라 안내소 (.kr)|country directory (.kr)⟧", "#5B8DEF"), ("⟦세상 안내소|world directory⟧", "var(--accent)"), ("⟦사진 성 안내소|the Photo Castle\'s own⟧", "var(--stone-dark)"))
P4 = svg(300, sky(300)
         + "".join(booth(100 + i * 185, 70, 0.7, name=n, color=c) for i, (n, c) in enumerate(CHAIN))
         + "".join(f'<path d="M{150 + i * 185} 120 L{225 + i * 185} 120" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6"/><path d="M{215 + i * 185} 110 L{227 + i * 185} 120 L{215 + i * 185} 130" stroke="var(--accent)" stroke-width="3" fill="none"/>' for i in range(3))
         + "".join(bubble(70 + i * 185, 14, 90, 28, "⟦몰라요…|no idea…⟧", 11, "var(--panel)", "var(--line)", "bottom") for i in range(3))
         + bubble(600, 14, 130, 28, ADDR, 11, "var(--good-soft)", "var(--good)", "bottom")
         + '<path d="M650 200 C500 260 250 260 100 200" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 6" fill="none"/><path d="M112 208 L98 198 L112 190" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(380, 228, "⟦답은 잠깐 적어둬요 — 다음 사람은 바로|the answer is jotted down — the next person gets it at once⟧", 12, "var(--muted)")
         + label(380, 285, "⟦마을 → 나라 → 세상 → 그 성의 안내소|town → country → world → that castle\'s own directory⟧", 13, "var(--ink)", cls="d"))

# 5. 안내소가 거짓말하면
FAKE = ('<g transform="translate(620,120)"><rect x="-50" y="30" width="100" height="70" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"/>'
        + battlements(-50, 12, 100, 3, "var(--stone)", 18) + '<path d="M-18 100 V70 a18 18 0 0 1 36 0 V100 Z" fill="var(--night)"/>'
        + label(0, 125, "⟦가짜 사진 성|fake Photo Castle⟧", 12, "var(--bad)") + "</g>")
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + booth(300, 90, 0.9) + person(282, 92, s=0.55, face=MASK)
         + person(90, 130, s=0.9, **ME) + bubble(40, 40, 190, 34, "⟦사진 성이 어디예요?|Where\'s the Photo Castle?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + bubble(350, 40, 200, 34, "⟦저쪽 골목 끝이요|end of that alley⟧", 13, "var(--panel)", "var(--bad)", "bottom")
         + '<path d="M170 210 C300 260 450 250 560 220" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
         + FAKE
         + '<g transform="translate(140,270)"><circle r="16" fill="none" stroke="var(--good)" stroke-width="3"/><circle r="10" fill="none" stroke="var(--good)" stroke-width="2"/>' + label(0, 4, "✓", 13, "var(--good)") + "</g>" + label(200, 275, "⟦답에 도장|a stamp on the answer⟧", 12, "var(--good)", "start")
         + '<g transform="translate(360,270)"><rect x="-16" y="-10" width="32" height="20" rx="3" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/><rect x="-4" y="-4" width="8" height="8" rx="1" fill="var(--good)"/></g>' + label(420, 275, "⟦질문은 봉인|the question sealed⟧", 12, "var(--good)", "start"))

NAME_I = icon('<rect x="8" y="20" width="48" height="24" rx="6" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/><text x="32" y="37" text-anchor="middle" font-size="11" font-weight="700" fill="var(--good)">photo.kr</text>')
ADDR_I = icon('<rect x="8" y="20" width="48" height="24" rx="6" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><text x="32" y="37" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink)">10.0.0.7</text>')
BOOTH_I = icon('<path d="M8 28 L32 10 L56 28 Z" fill="var(--good)"/><rect x="14" y="28" width="36" height="26" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>')
JOT_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="22" width="20" height="3" fill="#C9A86A"/><circle cx="44" cy="44" r="9" fill="none" stroke="var(--bad)" stroke-width="2"/><path d="M44 38 V44 L48 46" stroke="var(--bad)" stroke-width="2" fill="none"/>')

PAGE = {
    "slug": "dns", "order": 34,
    "title": ("마을 안내소", "The Town Directory"),
    "h1": ("<em>DNS</em>가 뭐예요?", "What is <em>DNS</em>?"),
    "sub": ("도메인 이름 시스템(Domain Name System)을 이름을 주소로 바꿔주는 마을 안내소 이야기로 풀어봤어요.",
            "The Domain Name System, told as a story about the town directory that turns names into addresses."),
    "panels": [
        {"svg": P1, "alt": ("'사진 성에 가고 싶어요' 하는 사람 앞에 10.0.0.7 같은 숫자 표지판만 서 있음", "Someone says I want to go to the Photo Castle, but the signposts show only numbers like 10.0.0.7"),
         "caption": ("사람들은 이름만 알아요.", "People only know names."),
         "small": ("'사진 성', '편지 성'. 그런데 길은 숫자 주소로만 찾아가요.", "'Photo Castle', 'Mail Castle'. But roads only go by number.")},
        {"svg": P2, "alt": ("숫자 주소가 적힌 메모지 다섯 장과, '사진 성이 이사 갔대요…' 하며 땀 흘리는 사람", "Five sticky notes with numeric addresses, and a sweating person saying the Photo Castle moved…"),
         "caption": ("숫자 주소를 다 외울 순 없어요.", "You can't memorize all the numbers."),
         "small": ("성이 이사라도 가면 외운 게 다 틀려요.", "And if a castle moves, everything you memorized is wrong.")},
        {"svg": P3, "hero": True, "alt": ("안내소 직원이 '사진 성이 어디예요?'에 '동쪽 3번길 7'이라고 답하고, 옆에 이름과 주소가 적힌 큰 책", "A directory clerk answers Where's the Photo Castle? with East 3rd St. 7; a big book of names and addresses sits beside"),
         "caption": ("DNS는 이름을 주소로 바꿔주는 안내소예요.", "DNS is the directory that turns names into addresses."),
         "small": ("'사진 성이 어디예요?' '동쪽 3번길 7이요.' 이름만 알면 돼요.", "'Where's the Photo Castle?' 'East 3rd Street, number 7.' You only need the name."),
         "tricks": (4, [
             (NAME_I, ("이름", "The name"), ("사람이 외우는 것", "what people remember"), "calm"),
             (ADDR_I, ("주소", "The address"), ("길이 아는 것", "what roads understand")),
             (BOOTH_I, ("안내소", "The directory"), ("대신 물어봐 줘요", "asks around on your behalf"), "calm"),
             (JOT_I, ("잠깐 적어두기", "Jotting it down"), ("같은 질문은 바로 답해요", "the same question, answered at once"), "warm"),
         ])},
        {"svg": P4, "alt": ("마을 안내소, 나라 안내소(.kr), 세상 안내소가 차례로 '몰라요…' 하다가 사진 성 안내소가 주소를 답하고, 답이 마을 안내소로 돌아옴", "The town, country (.kr) and world directories each say no idea… until the Photo Castle's own directory answers, and the answer flows back to the town"),
         "caption": ("우리 안내소가 모르면 더 큰 안내소에 물어봐요.", "If our directory doesn't know, it asks a bigger one."),
         "small": ('마을 → 나라 → 세상 → 그 성의 안내소. 답은 잠깐 적어둬요 — <a href="cdn-ko.html">복사본 창고</a>처럼요.',
                   'Town → country → world → that castle\'s own directory. The answer is jotted down for a while — like the <a href="cdn-en.html">copy depot</a>.')},
        {"svg": P5, "alt": ("가면 쓴 안내소 직원이 '저쪽 골목 끝이요' 하고 사람을 점선으로 그려진 가짜 사진 성으로 보냄. 아래엔 도장과 봉인 표시", "A masked directory clerk says end of that alley and sends the person to a dashed fake Photo Castle; below, a stamp and a seal"),
         "caption": ("안내소가 거짓말하면 가짜 성으로 가요.", "If the directory lies, you walk into a fake castle."),
         "small": ('그래서 답에 도장을 찍고(DNSSEC), 질문은 봉인해서 보내요(DoH). 가짜 성 이야기는 <a href="mfa-ko.html">문지기 이야기</a>에도 있어요.',
                   'So answers get a stamp (DNSSEC) and questions travel sealed (DoH). The fake castle also shows up in the <a href="mfa-en.html">gatekeeper story</a>.')},
    ],
    "summary": (("<b>DNS</b> = '사진 성'이라는 <b>이름</b>을 '동쪽 3번길 7' <b>주소</b>로 바꿔주는 마을 안내소.",
                 "<b>DNS</b> = the town directory that turns the <b>name</b> 'Photo Castle' into the <b>address</b> 'East 3rd Street, 7'."),
                ("Domain Name System. 1983년부터 있었어요. 8.8.8.8과 1.1.1.1이 유명한 안내소예요. 안내소가 멈추면 인터넷이 멈춘 것처럼 보여요 — 성들은 멀쩡한데 아무도 못 찾아가니까요.",
                 "The Domain Name System, around since 1983. 8.8.8.8 and 1.1.1.1 are famous directories. When the directory stops, the internet looks down — the castles are fine, nobody can find them.")),
    "glossary": [
        ("도메인", "Domain name", ("이름.", "The name."), ("photo.example.kr 처럼 사람이 외우는 글자.", "Letters people remember, like photo.example.kr.")),
        ("IP 주소", "IP address", ("숫자 주소.", "The numeric address."), ('길이 실제로 찾아가는 번호. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'The number roads actually follow. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("리졸버", "Resolver", ("마을 안내소.", "The town directory."), ("내 대신 물어보고 다니는 곳. 8.8.8.8, 1.1.1.1.", "Asks around for me. 8.8.8.8, 1.1.1.1.")),
        ("권한 서버", "Authoritative server", ("그 성 본인의 안내소.", "That castle\'s own directory."), ("정답을 가진 마지막 안내소.", "The last stop, holding the real answer.")),
        ("루트 · TLD", "Root · TLD", ("세상 안내소 · 나라 안내소.", "World · country directories."), (".kr, .com 같은 큰 칸을 나눠 맡아요.", "They split the big sections: .kr, .com and so on.")),
        ("TTL", "TTL", ("적어둔 답의 유통기한.", "How long the jotted answer lasts."), ('지나면 다시 물어봐요. → <a href="cdn-ko.html">복사본 창고</a>', 'Past it, ask again. → <a href="cdn-en.html">the copy depot</a>')),
        ("DNSSEC", "DNSSEC", ("도장 찍힌 답.", "A stamped answer."), ("안내소가 바꿔치기한 답을 알아볼 수 있어요.", "A swapped answer can be spotted.")),
        ("DoH · DoT", "DoH · DoT", ("봉인된 질문.", "A sealed question."), ('길에서 누가 어디 가는지 못 엿들어요. → <a href="vpn-ko.html">봉인된 땅굴</a>', 'Nobody on the road overhears where you\'re going. → <a href="vpn-en.html">the sealed tunnel</a>')),
    ],
}
