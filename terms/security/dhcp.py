from _draw import *

CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
DOORS = tuple(("", False) for _ in range(5))


def laptop(x, y, s=1.0, tag="", tag_color="var(--good)"):
    t = (f'<rect x="-22" y="-52" width="44" height="22" rx="4" fill="var(--panel)" stroke="{tag_color}" stroke-width="2"/>' + label(0, -36, tag, 12, tag_color)) if tag else \
        '<rect x="-22" y="-52" width="44" height="22" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 3"/>' + label(0, -36, "?", 13, "var(--bad)")
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-18" width="48" height="30" rx="2" fill="var(--night)"/><rect x="-21" y="-15" width="42" height="23" fill="var(--sky)"/>'
            f'<rect x="-30" y="12" width="60" height="5" rx="2" fill="var(--stone-dark)"/>{t}</g>')


def desk(x, y, s=1.0, thief=False):
    tags = "".join(f'<rect x="{-40 + i * 16}" y="-24" width="12" height="18" rx="2" fill="var(--panel)" stroke="{"var(--bad)" if thief else "var(--good)"}" stroke-width="1.5"/>' for i in range(6))
    who = person(-30, -100, s=0.65, face=(MASK if thief else SMILE), **(dict(hat="var(--bad)", shirt="#2E3D57") if thief else CLERK))
    sign = label(0, 30, "⟦번호표 창구|NUMBER-TAG DESK⟧" if not thief else "⟦번호표 창구?|NUMBER-TAG DESK?⟧", 12, "var(--bad)" if thief else "var(--ink)", cls="d")
    return f'<g transform="translate({x},{y}) scale({s})">{who}<rect x="-70" y="-4" width="140" height="14" rx="4" fill="#8B5E3C"/><rect x="-60" y="10" width="10" height="50" fill="#8B5E3C"/><rect x="50" y="10" width="10" height="50" fill="#8B5E3C"/>{tags}{sign}</g>'


def card(x, y, lines, s=1.0, bad=False):
    ink = "var(--bad)" if bad else "#142033"
    rows = "".join(label(8, 22 + i * 16, t, 11, ink, "start") for i, t in enumerate(lines))
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="150" height="{16 + len(lines) * 16}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>{rows}</g>'


def socket(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-14" width="32" height="28" rx="4" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<rect x="-8" y="-6" width="5" height="12" fill="var(--night)"/><rect x="3" y="-6" width="5" height="12" fill="var(--night)"/></g>')


def cable(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} C{x1} {y2} {x2} {y1} {x2} {y2}" stroke="var(--night)" stroke-width="3" fill="none"/>'


# 1. 새로 온 물건은 번호표가 없다
P1 = svg(300, corridor(300, DOORS, marks=False) + "".join(socket(x, 150) for x in (172, 312, 452, 592))
         + cable(172, 164, 172, 220) + laptop(172, 240, 0.8, tag="7")
         + cable(312, 164, 312, 220) + laptop(312, 240, 0.8, tag="12")
         + cable(452, 164, 452, 220) + laptop(452, 240, 0.8)
         + cable(592, 164, 592, 220) + laptop(592, 240, 0.8, tag="41")
         + label(452, 290, "⟦새로 온 노트북|the new laptop⟧", 11, "var(--bad)"))

# 2. 손으로 쓰면 겹친다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + laptop(200, 150, 1.0, tag="7") + laptop(420, 150, 1.0, tag="7", tag_color="var(--bad)")
         + '<g transform="translate(310,60)"><rect x="-26" y="-18" width="52" height="36" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M-26 -16 L0 4 L26 -16" stroke="var(--line)" stroke-width="2" fill="none"/>' + label(0, 30, "⟦7번에게|to number 7⟧", 11, "var(--muted)") + "</g>"
         + '<path d="M310 80 L230 110 M310 80 L390 110" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 5"/>' + label(310, 110, "?", 30, "var(--bad)", cls="d")
         + person(600, 100, s=0.85, face=FROWN + SWEAT, **CLERK) + bubble(540, 30, 200, 34, "⟦누가 몇 번이더라…|who had which number…⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 275, "⟦둘 다 7번이면 편지가 엉뚱한 데로 가요|two number 7s, and letters go to the wrong one⟧", 13, "var(--muted)"))

# 3. DHCP = 번호표 빌려주는 창구 (hero)
P3 = svg(340, sky(340) + desk(200, 190)
         + bubble(90, 30, 190, 34, "⟦번호표 하나 주세요|one number tag, please⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + laptop(430, 190, 1.0, tag="⟦23 · 오늘까지|23 · until tonight⟧")
         + '<path d="M290 200 L370 200" stroke="var(--good)" stroke-width="3"/><path d="M360 190 L372 200 L360 210" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + card(530, 120, ("⟦번호표: 23|tag: 23⟧", "⟦안내소: 1번|directory: no. 1⟧", "⟦성문: 1번|gate: no. 1⟧", "⟦오늘까지|until tonight⟧"), 1.0)
         + label(605, 230, "⟦함께 주는 쪽지|the note that comes with it⟧", 11, "var(--muted)")
         + label(380, 322, "⟦'23번, 오늘까지.' 안내소와 성문 위치도 같이 알려줘요|'23, until tonight.' Plus where the directory and the gate are⟧", 13, "var(--muted)"))

# 4. 다시 빌리고, 돌려준다
P4 = svg(280, '<rect width="380" height="280" fill="var(--sky)"/><rect x="380" width="380" height="280" fill="var(--good-soft)"/>'
         + laptop(120, 140, 0.9, tag="23") + '<g transform="translate(230,80)"><circle r="24" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -16 V0 L10 8" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-24 0 a24 24 0 0 1 24 -24" stroke="var(--accent)" stroke-width="4" fill="none"/></g>'
         + bubble(150, 190, 170, 34, "⟦반쯤 지났네, 더 쓸게요|halfway — I\'ll keep it⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(190, 262, "⟦시간이 지나면 다시 빌려요|renew before it runs out⟧", 13, "var(--ink)", cls="d")
         + person(460, 100, s=0.8, hat=None, shirt="#4A5A72", face=SMILE, extra='<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/>')
         + '<rect x="530" y="120" width="26" height="36" rx="3" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/>' + label(543, 143, "23", 12, "var(--good)")
         + '<path d="M570 140 L630 140" stroke="var(--good)" stroke-width="3"/><path d="M620 130 L632 140 L620 150" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + desk(690, 180, 0.6) + label(570, 262, "⟦나가면 번호표가 창구로 돌아와요|leave, and the tag goes back to the desk⟧", 13, "var(--ink)", cls="d"))

# 5. 가짜 창구
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + desk(180, 200, 0.9, thief=True)
         + card(280, 60, ("⟦번호표: 23|tag: 23⟧", "⟦안내소: 도둑 골목|directory: thief alley⟧", "⟦성문: 도둑 골목|gate: thief alley⟧"), 1.0, bad=True)
         + laptop(480, 200, 0.9, tag="23", tag_color="var(--bad)")
         + '<path d="M520 190 C580 150 620 150 660 130" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + '<g transform="translate(680,90)"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3" stroke-dasharray="8 6"/><path d="M-48 0 L0 -26 L48 0 Z" fill="var(--bad)"/>' + label(0, 80, "⟦가짜 안내소|fake directory⟧", 11, "var(--bad)") + "</g>"
         + label(380, 300, "⟦창구는 아무나 열 수 있어요 — 그래서 복도 구멍 문지기가 창구도 확인해요|anyone can open a desk — so the gatekeeper at the socket checks desks too⟧", 12, "var(--muted)"))

POOL_I = icon("".join(f'<rect x="{10 + i * 12}" y="{18 + (i % 2) * 6}" width="9" height="16" rx="2" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/>' for i in range(4)))
CLOCK_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M32 18 V32 L42 38" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
CARD_I = icon('<rect x="12" y="14" width="40" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="24" width="24" height="3" fill="#C9A86A"/><rect x="20" y="32" width="18" height="3" fill="#C9A86A"/><rect x="20" y="40" width="20" height="3" fill="#C9A86A"/>')
RETURN_I = icon('<rect x="34" y="16" width="14" height="22" rx="2" fill="var(--panel)" stroke="var(--good)" stroke-width="2"/><path d="M28 44 H12 M18 38 l-6 6 6 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "dhcp", "order": 35,
    "title": ("번호표 나눠주는 창구", "The Number-Tag Desk"),
    "h1": ("<em>DHCP</em>가 뭐예요?", "What is <em>DHCP</em>?"),
    "sub": ("동적 호스트 설정 프로토콜(Dynamic Host Configuration Protocol)을 복도에 새로 온 물건에게 번호표를 빌려주는 창구 이야기로 풀어봤어요.",
            "Dynamic Host Configuration Protocol, told as a story about the desk that lends number tags to newcomers in the hallway."),
    "panels": [
        {"svg": P1, "alt": ("복도 구멍에 꽂힌 노트북 넷 중 셋은 7, 12, 41 번호표가 있고 새 노트북엔 물음표", "Four laptops plugged into the hallway; three wear tags 7, 12 and 41, the new one only a question mark"),
         "caption": ("새로 온 물건은 번호표가 없어요.", "A newcomer has no number tag."),
         "small": ('번호표(주소)가 없으면 복도에서 아무도 못 찾아요. <a href="nac-ko.html">구멍 문지기</a>를 지난 다음 이야기예요.',
                   'Without a tag (an address), nobody in the hallway can find you. This comes right after the <a href="nac-en.html">gatekeeper at the socket</a>.')},
        {"svg": P2, "alt": ("노트북 두 대가 둘 다 7번 표를 달고, '7번에게' 편지가 어디로 갈지 물음표. 직원은 '누가 몇 번이더라…'", "Two laptops both wear tag 7; a letter to number 7 hangs between them with a question mark; a clerk mutters who had which number…"),
         "caption": ("번호표를 손으로 쓰면 겹쳐요.", "Hand-written tags collide."),
         "small": ("둘 다 7번이면 편지가 엉뚱한 데로 가요. 백 개면 누가 몇 번인지 아무도 몰라요.", "Two number 7s and letters go astray. With a hundred, nobody knows who has what.")},
        {"svg": P3, "hero": True, "alt": ("번호표 창구 직원이 '번호표 하나 주세요' 하는 노트북에 '23 · 오늘까지' 표와 안내소·성문 위치가 적힌 쪽지를 줌", "The number-tag desk hands a laptop asking for a tag a '23 · until tonight' tag plus a note with the directory and gate locations"),
         "caption": ("DHCP는 빈 번호표를 빌려주는 창구예요.", "DHCP is the desk that lends out spare number tags."),
         "small": ("'23번, 오늘까지.' 안내소와 성문 위치도 같이 알려줘요.", "'Number 23, until tonight.' It also tells you where the directory and the gate are."),
         "tricks": (4, [
             (POOL_I, ("빈 번호표", "Spare tags"), ("창구가 가진 묶음", "the desk\'s bundle"), "calm"),
             (CLOCK_I, ("오늘까지", "Until tonight"), ("빌리는 거지 주는 게 아니에요", "a loan, not a gift"), "warm"),
             (CARD_I, ("함께 주는 쪽지", "The note with it"), ("안내소, 성문 위치", "where the directory and gate are")),
             (RETURN_I, ("돌려주기", "Giving it back"), ("나가면 창구로", "back to the desk when you leave"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽: 시계가 반쯤 돌자 노트북이 '더 쓸게요'. 오른쪽: 나가는 손님의 23번 표가 창구로 돌아감", "Left: the clock is half round and the laptop says I'll keep it. Right: a departing guest's tag 23 goes back to the desk"),
         "caption": ("시간이 지나면 다시 빌리고, 나가면 돌려줘요.", "Renew as time passes; give it back when you leave."),
         "small": ("반쯤 지나면 '더 쓸게요' 하고, 나가면 번호표가 창구로 돌아와요. 그래서 번호표가 안 모자라요.", "Halfway through, 'I'll keep it'; when you leave, the tag returns. That's why the desk never runs dry.")},
        {"svg": P5, "alt": ("가면 쓴 사람이 연 가짜 창구가 '안내소: 도둑 골목' 쪽지를 주고, 노트북이 점선 가짜 안내소로 감", "A masked figure's fake desk hands out a note reading directory: thief alley, and the laptop heads for a dashed fake directory"),
         "caption": ("가짜 창구가 번호표를 나눠주면 큰일이에요.", "A fake desk handing out tags is trouble."),
         "small": ('창구는 아무나 열 수 있어서, 도둑이 "안내소는 저쪽"이라고 적어주면 다들 <a href="dns-ko.html">가짜 안내소</a>로 가요. 그래서 <a href="nac-ko.html">구멍 문지기</a>가 창구도 확인해요.',
                   'Anyone can open a desk, so a thief who writes "the directory is over there" sends everyone to a <a href="dns-en.html">fake directory</a>. Which is why the <a href="nac-en.html">gatekeeper at the socket</a> checks desks too.')},
    ],
    "summary": (("<b>DHCP</b> = 복도에 새로 온 물건에게 빈 <b>번호표(주소)</b>를 '오늘까지' <b>빌려주고</b>, 안내소와 성문 위치를 같이 알려주는 창구.",
                 "<b>DHCP</b> = the desk that <b>lends</b> a newcomer a spare <b>number tag (address)</b> until tonight, and tells them where the directory and the gate are."),
                ("Dynamic Host Configuration Protocol. 집 공유기가 바로 이 창구예요. 번호표는 IP 주소, 안내소는 DNS, 성문은 게이트웨이.",
                 "Dynamic Host Configuration Protocol. Your home router is this desk. The tag is an IP address, the directory is DNS, the gate is the gateway.")),
    "glossary": [
        ("IP 주소", "IP address", ("번호표.", "The number tag."), ('복도에서 나를 찾는 번호. → <a href="firewall-ko.html">문이 많은 성벽</a>', 'The number the hallway finds me by. → <a href="firewall-en.html">the wall with many doors</a>')),
        ("주소 풀", "Address pool", ("창구의 빈 번호표 묶음.", "The desk\'s bundle of spare tags."), ("다 나가면 새 사람은 못 들어와요.", "Run out, and newcomers get nothing.")),
        ("임대", "Lease", ("오늘까지.", "Until tonight."), ("번호표는 빌리는 거예요. 기간이 있어요.", "The tag is a loan, with a term.")),
        ("갱신", "Renewal", ("더 쓸게요.", "I\'ll keep it."), ("기간이 반쯤 지나면 창구에 다시 말해요.", "Halfway through the term, tell the desk again.")),
        ("게이트웨이", "Gateway", ("성문.", "The gate."), ('밖으로 나갈 때 지나는 문. 쪽지에 적어줘요. → <a href="firewall-ko.html">성벽 이야기</a>', 'The door you use to go out — written on the note. → <a href="firewall-en.html">the wall story</a>')),
        ("DNS 서버", "DNS server", ("안내소.", "The directory."), ('이름을 주소로 바꿔주는 곳. 이것도 쪽지에. → <a href="dns-ko.html">마을 안내소</a>', 'Turns names into addresses — also on the note. → <a href="dns-en.html">the town directory</a>')),
        ("예약 · 고정 주소", "Reservation · static address", ("예약석.", "A reserved seat."), ("프린터나 창구처럼 늘 같은 번호여야 하는 것들.", "For printers and desks that must keep the same number.")),
        ("가짜 창구", "Rogue DHCP", ("도둑이 연 창구.", "A desk opened by a thief."), ('가짜 안내소 주소를 나눠줘요. → <a href="nac-ko.html">복도 구멍마다 문지기</a>가 막아요', 'Hands out a fake directory address. → the <a href="nac-en.html">gatekeeper at every socket</a> stops it')),
    ],
}
