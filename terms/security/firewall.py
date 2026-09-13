from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
DOORS = (("⟦손님 문|Guest door⟧", "443"), ("⟦우편 문|Mail door⟧", "25"), ("⟦창고 문|Storage door⟧", "445"), ("⟦관리 문|Admin door⟧", "22"))


def wall_doors(y, states, s=1.0, labels=True):
    """성벽 위에 문 네 개. states: 'open' | 'closed' | 'brick' 리스트."""
    out = f'<rect x="0" y="{y}" width="760" height="{150 * s + 40}" fill="var(--stone-dark)"/>{battlements(0, y - 18, 760, 12, "var(--stone-dark)", 20)}'
    for i, ((name, num), st) in enumerate(zip(DOORS, states)):
        x = 110 + i * 180
        if st == "brick":
            door = (f'<rect x="-34" y="0" width="68" height="110" fill="var(--stone)"/>'
                    + "".join(f'<rect x="{-34 + (j % 2) * 17}" y="{j * 14}" width="34" height="12" fill="var(--stone-dark)" stroke="var(--stone)" stroke-width="2"/>' for j in range(8)))
        elif st == "open":
            door = '<path d="M-34 110 V40 a34 34 0 0 1 68 0 V110 Z" fill="var(--sky)"/><rect x="-34" y="40" width="14" height="70" fill="#8B5E3C" transform="skewY(-10)"/>'
        else:
            door = f'<path d="M-34 110 V40 a34 34 0 0 1 68 0 V110 Z" fill="{WOOD}"/><circle cx="18" cy="80" r="4" fill="#E9B44C"/>'
        tag = f'<rect x="-18" y="-30" width="36" height="20" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>{label(0, -16, num, 11, "var(--ink)")}'
        nm = label(0, 132, name, 12, "#C9D5E6") if labels else ""
        out += f'<g transform="translate({x},{y + 40}) scale({s})">{door}{tag}{nm}</g>'
    return out


def rulebook(x, y, rows, s=1.0):
    lines = "".join(label(12, 40 + i * 20, r, 11, "#142033", "start") for i, r in enumerate(rows))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="200" height="{44 + len(rows) * 20}" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            f'<rect width="200" height="24" rx="4" fill="#C9A86A"/>{label(100, 17, "⟦문 목록|DOOR LIST⟧", 12, "#142033")}{lines}</g>')


NOTE = '<rect x="48" y="66" width="26" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="53" y="74" width="16" height="3" fill="#C9A86A"/><rect x="53" y="82" width="12" height="3" fill="#C9A86A"/>'

# 1. 성벽엔 문이 여러 개
P1 = svg(300, sky(300, ground=False) + wall_doors(60, ("closed", "closed", "closed", "closed"))
         + label(380, 40, "⟦문마다 번호가 있어요 — 포트|every door has a number — a port⟧", 14, "var(--ink)", cls="d"))

# 2. 문이 다 열려 있으면
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + wall_doors(60, ("open", "open", "open", "open"))
         + person(430, 150, s=0.6, face=MASK) + person(620, 150, s=0.6, face=MASK)
         + label(380, 40, "⟦뒷문(열린 포트)부터 찾아요|thieves look for the back door (an open port) first⟧", 14, "var(--bad)", cls="d"))

# 3. 방화벽 = 문마다 목록을 든 문지기 (hero)
P3 = svg(340, sky(340, ground=False) + wall_doors(100, ("open", "closed", "brick", "brick"))
         + person(20, 20, s=0.8, face=EYES, **GUARD)
         + rulebook(80, 10, ("⟦손님 문 443 — 누구나|Guest 443 — anyone⟧", "⟦우편 문 25 — 우체국만|Mail 25 — post office only⟧", "⟦창고 문 445 — 닫힘|Storage 445 — closed⟧", "⟦나머지 — 전부 닫힘|everything else — closed⟧"), 0.9)
         + label(560, 40, "⟦목록에 없으면 안 열려요|not on the list? it stays shut⟧", 14, "var(--ink)", cls="d")
         + person(110, 200, s=0.5, **ME) + person(290, 200, s=0.5, hat="#5B8DEF", shirt="#4A5A72", face=SMILE, extra=NOTE)
         + label(290, 315, "⟦우체국|post office⟧", 11, "#C9D5E6"))

# 4. 내가 내보낸 심부름꾼은 돌아올 때 열어준다
P4 = svg(300, sky(300, ground=False) + wall_doors(60, ("closed", "closed", "brick", "brick"), labels=False)
         + person(40, 20, s=0.7, face=EYES, **GUARD)
         + rulebook(100, 10, ("⟦14:02 지민 → 마을 시장 (나감)|14:02 Jimin → market (out)⟧",), 0.8)
         + person(110, 150, s=0.55, **ME, extra=NOTE) + '<path d="M150 190 L200 190" stroke="var(--good)" stroke-width="3"/><path d="M190 180 L202 190 L190 200" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + label(140, 250, "⟦아까 나간 애 맞네 → 열어줘요|that\'s the one who went out → open⟧", 11, "#C9D5E6")
         + person(470, 150, s=0.55, face=MASK, extra=NOTE) + '<path d="M450 190 L400 190" stroke="var(--bad)" stroke-width="3"/><path d="M410 180 L398 190 L410 200" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + '<path d="M420 170 l30 30 M450 170 l-30 30" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
         + label(470, 250, "⟦처음 보는 사람 → 안 열어요|never seen you → shut⟧", 11, "#C9D5E6"))

# 5. 열린 문으로 오면 못 막고, 성 안은 안 본다
BADNOTE = ('<g transform="translate(46,60)"><rect width="34" height="40" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
           + label(17, 16, "⟦사과 2|2 apples⟧", 7, "#142033") + label(17, 30, "⟦+금고 열쇠|+vault key⟧", 7, "var(--bad)") + "</g>")
P5 = svg(320, '<rect width="380" height="320" fill="var(--accent-soft)"/><rect x="380" width="380" height="320" fill="var(--sky)"/>'
         + '<rect x="0" y="60" width="380" height="120" fill="var(--stone-dark)"/>' + battlements(0, 42, 380, 6, "var(--stone-dark)", 20)
         + '<path d="M156 180 V110 a34 34 0 0 1 68 0 V180 Z" fill="var(--sky)"/>' + label(190, 100, "443", 12, "#C9D5E6")
         + person(60, 90, s=0.6, face=SMILE, **GUARD) + person(160, 200, s=0.8, face=MASK, extra=BADNOTE)
         + label(190, 300, "⟦손님 문으로 나쁜 쪽지를 들고 오면 몰라요|a bad note through the guest door goes unnoticed⟧", 11, "var(--muted)")
         + "".join(person(x, 100, s=0.7, hat=h, shirt="#4A5A72", face=SMILE) for x, h in ((440, "#E9B44C"), (560, "#5B8DEF"), (660, "var(--good)")))
         + '<path d="M500 160 C540 130 580 170 640 150" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
         + label(570, 230, "⟦성 안에서는 서로 아무 데나|inside, anyone goes anywhere⟧", 12, "var(--ink)")
         + label(570, 300, "⟦성벽은 밖만 봐요|the wall only looks outward⟧", 11, "var(--muted)"))

PORT_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#8B5E3C"/><rect x="20" y="16" width="24" height="14" rx="3" fill="var(--panel)"/><text x="32" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="var(--ink)">443</text>')
ADDR_I = icon('<path d="M10 30 L32 12 L54 30 V54 H10 Z" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/><text x="32" y="46" text-anchor="middle" font-size="9" font-weight="700" fill="var(--accent)">10.0.0.7</text>')
LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="#C9A86A"/><rect x="22" y="30" width="16" height="3" fill="#C9A86A"/><rect x="22" y="40" width="18" height="3" fill="#C9A86A"/>')
DENY_I = icon('<rect x="12" y="14" width="40" height="40" rx="3" fill="var(--stone)"/><path d="M12 24 h40 M12 34 h40 M12 44 h40 M32 14 v10 M22 24 v10 M42 24 v10 M32 34 v10 M22 44 v10 M42 44 v10" stroke="var(--stone-dark)" stroke-width="2"/>')

PAGE = {
    "slug": "firewall", "order": 29,
    "title": ("문이 많은 성벽", "The Wall with Many Doors"),
    "h1": ("<em>방화벽</em>이 뭐예요?", "What is a <em>Firewall</em>?"),
    "sub": ("방화벽(Firewall)을 문이 많은 성벽과 문 목록을 든 문지기 이야기로 풀어봤어요.",
            "Firewalls, told as a story about a wall with many doors and the gatekeeper who holds the door list."),
    "panels": [
        {"svg": P1, "alt": ("성벽에 손님 문 443, 우편 문 25, 창고 문 445, 관리 문 22 네 개의 문이 번호표를 달고 있음", "A wall with four numbered doors: Guest 443, Mail 25, Storage 445, Admin 22"),
         "caption": ("성벽엔 문이 여러 개 있어요.", "The wall has more than one door."),
         "small": ("손님 문, 우편 문, 창고 문, 관리 문… 문마다 번호가 있어요. 그게 포트예요.", "A guest door, a mail door, a storage door, an admin door… each has a number. That's a port.")},
        {"svg": P2, "alt": ("문 네 개가 전부 열려 있고 가면 쓴 도둑 둘이 창고 문과 관리 문으로 들어감", "All four doors stand open; two masked thieves slip in through the storage and admin doors"),
         "caption": ("문이 다 열려 있으면 성벽이 없는 거나 마찬가지예요.", "With every door open, there's no wall at all."),
         "small": ("도둑은 아무도 안 보는 뒷문(열린 포트)부터 찾아요.", "Thieves look for the back door nobody watches — an open port — first.")},
        {"svg": P3, "hero": True, "alt": ("문지기가 '손님 문 443 누구나, 우편 문 25 우체국만, 창고 문 닫힘, 나머지 전부 닫힘' 목록을 들고 있고, 손님 문은 열림, 우편 문은 닫힘, 창고·관리 문은 벽돌로 막힘", "The gatekeeper holds a list — Guest 443 anyone, Mail 25 post office only, Storage closed, everything else closed; the guest door is open, mail shut, storage and admin bricked up"),
         "caption": ("방화벽은 문마다 목록을 들고 열고 닫는 문지기예요.", "A firewall is the gatekeeper who opens and shuts doors by a list."),
         "small": ("'손님 문은 누구나, 우편 문은 우체국만, 나머진 닫힘.' 목록에 없으면 안 열려요.", "'Guest door: anyone. Mail door: post office only. The rest: closed.' Not on the list, not open."),
         "tricks": (4, [
             (PORT_I, ("문 번호", "Door number"), ("포트", "port"), "warm"),
             (ADDR_I, ("어디서 왔나", "Where from"), ("주소", "address"), "calm"),
             (LIST_I, ("목록", "The list"), ("누가 어느 문으로", "who, through which door")),
             (DENY_I, ("안 적힌 문은 닫힘", "Unlisted = shut"), ("기본은 벽돌", "bricks by default"), "calm"),
         ])},
        {"svg": P4, "alt": ("문지기 목록에 '14:02 지민 → 마을 시장 (나감)'. 돌아온 지민은 문이 열리고, 처음 보는 가면 쓴 사람은 X", "The list reads 14:02 Jimin → market (out). Jimin returns and the door opens; a masked stranger gets an X"),
         "caption": ("내가 내보낸 심부름꾼은 돌아올 때 열어줘요.", "Someone I sent out gets let back in."),
         "small": ("'아까 나간 애 맞네' — 나간 기록을 기억해요. 처음 보는 사람은 안 열어요.", "'That's the one who went out' — it remembers who left. Strangers stay out.")},
        {"svg": P5, "alt": ("왼쪽: 열린 손님 문으로 '사과 2 + 금고 열쇠' 쪽지를 든 도둑이 들어오는데 문지기는 모름. 오른쪽: 성 안 사람들이 자유롭게 오감", "Left: a thief walks through the open guest door with a note reading 2 apples + vault key while the gatekeeper doesn't notice. Right: people inside wander freely"),
         "caption": ("열린 문으로 오면 못 막고, 성 안은 안 봐요.", "It can't stop what comes through an open door, and it never looks inside."),
         "small": ('손님 문으로 나쁜 쪽지를 들고 오면 문지기는 몰라요 — <a href="waf-ko.html">창구 검토원</a> 몫. 성 안 사람끼리는 안 봐요 — <a href="zerotrust-ko.html">문마다 묻는 성</a> 몫.',
                   'A bad note through the guest door goes unnoticed — that\'s the <a href="waf-en.html">note checker</a>\'s job. Inside the walls nobody is checked — that\'s the <a href="zerotrust-en.html">castle that always asks</a>.')},
    ],
    "summary": (("<b>방화벽</b> = 성벽 + 문마다 '누가 어느 문으로'를 적은 <b>목록</b>으로 열고 닫는 문지기. 안 적힌 문은 <b>닫힘</b>.",
                 "A <b>firewall</b> = the wall, plus the gatekeeper who opens and shuts each door by a <b>list</b> of who may use which door. Unlisted doors stay <b>shut</b>."),
                ("Firewall. 1990년대부터 있는 가장 오래된 파수꾼이에요. 요즘 성벽엔 수배 전단 파수꾼(IPS)과 봉인 뜯기까지 넣어 NGFW라고 불러요. iptables, pfSense, Palo Alto, Fortinet 같은 것들.",
                 "The oldest guard of all, around since the 1990s. Today's walls also carry the poster-watcher (IPS) and seal-breaking, and get called next-gen firewalls. iptables, pfSense, Palo Alto, Fortinet.")),
    "glossary": [
        ("포트", "Port", ("문 번호.", "The door number."), ("443은 손님 문, 25는 우편 문, 22는 관리 문.", "443 is the guest door, 25 the mail door, 22 the admin door.")),
        ("IP 주소", "IP address", ("어디서 왔나.", "Where from."), ('심부름꾼의 집 주소. → <a href="ioc-ko.html">남겨진 발자국</a>', 'The messenger\'s home address. → <a href="ioc-en.html">the footprint</a>')),
        ("규칙", "Rule", ("목록 한 줄.", "One line of the list."), ('"우체국이 우편 문으로 → 허용" 같은 문장.', '"Post office through the mail door → allow."')),
        ("기본 거부", "Default deny", ("안 적힌 문은 닫힘.", "Unlisted doors stay shut."), ("목록에 있는 것만 열어요. 반대로 하면 문이 다 열린 성이에요.", "Open only what's listed. The other way round is the castle with every door open.")),
        ("상태 추적", "Stateful", ("나간 심부름꾼 기억하기.", "Remembering who went out."), ("답장은 들어오게, 처음 보는 건 못 들어오게.", "Replies get in; strangers don't.")),
        ("패킷", "Packet", ("심부름꾼.", "The messenger."), ("쪽지 한 장 든 작은 사람. 문지기는 쪽지 겉봉만 봐요.", "A little person carrying one note. The gatekeeper reads only the envelope.")),
        ("NGFW", "Next-gen firewall", ("전단 파수꾼이 든 성벽.", "A wall with the poster-watcher inside."), ('<a href="idsips-ko.html">수배 전단</a>과 봉인 뜯기까지. 겉봉 너머를 조금 봐요.', 'Adds <a href="idsips-en.html">wanted posters</a> and seal-breaking — a peek past the envelope.')),
        ("내부 방화벽", "Internal / segmentation firewall", ("복도 안의 성벽.", "A wall inside the hallway."), ('성 안 복도도 나눠요. → <a href="ndr-ko.html">복도를 지키는 사람</a>', 'Splits the hallway inside too. → <a href="ndr-en.html">the hallway watcher</a>')),
    ],
}
