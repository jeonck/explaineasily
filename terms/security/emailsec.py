from _draw import *

ME = dict(hat=None, shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
POST = dict(hat="#5B8DEF", shirt="#5B8DEF")
THIEF = dict(hat="var(--bad)", shirt="#2E3D57", face=MASK)
SEAL_COLOR = "#B5382C"   # 밀랍 봉인 — 실제 색이 의미라 리터럴


def seal(x, y, s=1.0, color=SEAL_COLOR, wrong=False):
    mark = ('<path d="M-8 -8 l16 16 M8 -8 l-16 16" stroke="#FFF8E7" stroke-width="3" stroke-linecap="round"/>' if wrong
            else '<path d="M-10 4 l-2 -12 l6 5 l6 -9 l6 9 l6 -5 l-2 12z" fill="#FFF8E7"/>')
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="{color}"/><circle r="12" fill="none" stroke="#FFF8E7" stroke-width="1.5" opacity="0.7"/>{mark}</g>'


def env(x, y, s=1.0, sender="", sealed=None, wrong=False, cross=False):
    """봉투. sender 는 왼쪽 위 보낸 이 글씨, sealed 는 오른쪽 봉인 색(None 이면 없음)."""
    st = seal(104, 22, 0.9, sealed, wrong) if sealed else ""
    tx = label(10, 20, sender, 10, "#142033", "start") if sender else ""
    cx = '<path d="M10 10 l110 64 M120 10 l-110 64" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>' if cross else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="84" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M0 30 L65 64 L130 30" stroke="#C9A86A" stroke-width="2" fill="none"/>{tx}{st}{cx}</g>')


def mailbox(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="40" width="12" height="50" fill="var(--stone-dark)"/>'
            f'<rect x="-34" y="0" width="68" height="44" rx="10" fill="#4A5A72"/><rect x="-22" y="12" width="44" height="22" rx="3" fill="var(--panel)"/><path d="M-22 14 L0 28 L22 14" stroke="var(--line)" stroke-width="2" fill="none"/></g>')


def paper(x, y, w, h, title, rows, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect width="{w}" height="26" rx="6" fill="#C9A86A"/>' + label(w / 2, 18, title, 12, "#142033", cls="d")
    for i, r in enumerate(rows):
        out += label(14, 50 + i * 22, r, 12, "#142033", "start")
    return out + "</g>"


def bin_box(x, y, color, inner=""):
    return f'<g transform="translate({x},{y})"><rect x="-28" y="-24" width="56" height="48" rx="4" fill="{color}"/><rect x="-32" y="-30" width="64" height="8" rx="2" fill="{color}"/>{inner}</g>'


# 1. 봉투에 '왕궁 우체국'이라고 아무나 써요
P1 = svg(300, sky(300)
         + person(50, 110, s=0.85, **THIEF) + '<path d="M112 160 l30 -18" stroke="#142033" stroke-width="4" stroke-linecap="round"/>'
         + env(150, 120, 1.0, sender="⟦보낸 이: 왕궁 우체국|from: the Royal Post⟧")
         + label(215, 240, "⟦도둑이 그냥 써요|the thief just writes it⟧", 12, "var(--bad)")
         + '<path d="M300 162 H390" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5" fill="none"/><path d="M382 154 l10 8 l-10 8" stroke="var(--muted)" stroke-width="3" fill="none"/>'
         + mailbox(430, 100) + label(430, 225, "⟦성 우체통|castle mailbox⟧", 12, "var(--muted)")
         + person(560, 110, s=0.85, face=EYES, **ME) + bubble(470, 30, 250, 40, "⟦왕궁에서 온 편지네!|a letter from the Royal Post!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦봉투에 쓴 이름은 도장이 아니에요|the name on the envelope is not a seal⟧", 13, "var(--ink)", cls="d"))

# 2. 봉투만 보면 누구도 몰라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + env(100, 90, 1.0, sender="⟦보낸 이: 왕궁 우체국|from: the Royal Post⟧") + label(165, 205, "⟦진짜 우체국이 보냄|sent by the real post⟧", 11, "var(--good)")
         + label(255, 145, "=", 34, "var(--muted)", cls="d")
         + env(290, 90, 1.0, sender="⟦보낸 이: 왕궁 우체국|from: the Royal Post⟧") + label(355, 205, "⟦도둑이 보냄|sent by the thief⟧", 11, "var(--bad)")
         + person(520, 100, s=0.9, face=FROWN + SWEAT, **GUARD)
         + bubble(440, 20, 270, 36, "⟦똑같이 생겼는데…|they look exactly the same…⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(555, 235, "⟦문지기는 고를 수 없어요|the doorkeeper can\'t choose⟧", 11, "var(--muted)")
         + label(380, 282, "⟦게다가 우리 성 이름으로도 가짜가 마을에 나가요|worse — fakes go out to the village in our name too⟧", 12, "var(--ink)"))

# 3. 우체국 도장 세 개 (hero)
P3 = svg(360, sky(360)
         + label(140, 40, "⟦① 배달부 명단|① the courier list⟧", 14, "var(--ink)", cls="d")
         + paper(50, 60, 180, 150, "⟦보낼 수 있는 배달부|WHO MAY DELIVER⟧", ("⟦배달부 A ✓|courier A ✓⟧", "⟦배달부 B ✓|courier B ✓⟧", "⟦그 외엔 안 돼요|no one else⟧"))
         + label(140, 240, "⟦누가 보낼 수 있나|who is allowed to send⟧", 11, "var(--muted)")
         + label(380, 40, "⟦② 봉인 도장|② the seal⟧", 14, "var(--ink)", cls="d")
         + seal(380, 135, 3.2) + label(380, 240, "⟦우체국만 찍을 수 있어요|only the post can press it⟧", 11, "var(--muted)")
         + label(620, 40, "⟦③ 안내문|③ the instructions⟧", 14, "var(--ink)", cls="d")
         + paper(530, 60, 180, 150, "⟦도장이 틀리면|IF THE SEAL IS WRONG⟧", ("⟦그냥 두기|leave it⟧", "⟦따로 두기|set it aside⟧", "⟦버리기|throw it away⟧"))
         + label(620, 240, "⟦틀리면 어떻게 하나|what to do if it\'s wrong⟧", 11, "var(--muted)")
         + label(380, 300, "⟦세 개 다 마을 안내소에 미리 붙여 둬요|all three are pinned at the village desk ahead of time⟧", 13, "var(--ink)", cls="d")
         + label(380, 336, "⟦누구든 물어보면 볼 수 있어요|anyone who asks can look them up⟧", 12, "var(--muted)"))

# 4. 문지기가 세 개를 확인해요
P4 = svg(340, sky(340)
         + person(50, 120, s=0.9, face=EYES, **GUARD)
         + env(130, 140, 0.8, sender="⟦왕궁 우체국|Royal Post⟧", sealed=SEAL_COLOR)
         + paper(270, 40, 240, 120, "⟦문지기의 확인|THE DOORKEEPER\'S CHECK⟧", ("⟦배달부가 명단에 있나?|is the courier on the list?⟧", "⟦봉인 도장이 진짜인가?|is the seal real?⟧", "⟦아니면 → 안내문대로|if not → follow the note⟧"))
         + label(390, 185, "⟦둘 중 하나만 맞아도 통과예요|either one matching is enough⟧", 10, "var(--muted)")
         + bin_box(560, 230, "#4A5A72", '<path d="M-14 -6 L0 4 L14 -6" stroke="var(--panel)" stroke-width="2" fill="none"/>') + label(560, 275, "⟦그냥 두기|deliver⟧", 11, "var(--ink)")
         + bin_box(640, 230, "var(--accent)", label(0, 6, "!", 22, "#FFF8E7", cls="d")) + label(640, 275, "⟦격리함|quarantine⟧", 11, "var(--ink)")
         + bin_box(720, 230, "var(--bad)", '<path d="M-10 -10 l20 20 M10 -10 l-20 20" stroke="#FFF8E7" stroke-width="3" stroke-linecap="round"/>') + label(720, 275, "⟦버리기|reject⟧", 11, "var(--ink)")
         + label(640, 185, "⟦틀리면 안내문대로|if wrong, do what the note says⟧", 11, "var(--muted)")
         + label(380, 322, "⟦문지기는 봉투 글씨 말고 도장을 봐요|the doorkeeper reads the seal, not the handwriting⟧", 13, "var(--ink)", cls="d"))

# 5. 마을 다른 성들도 우리 이름으로 온 가짜를 버려요
P5 = svg(320, sky(320)
         + castle(20, 70, 0.42) + label(117, 195, "⟦우리 성|our castle⟧", 12, "var(--ink)", cls="d")
         + label(117, 216, "⟦안내문: 틀리면 버리기|our note says: throw it away⟧", 10, "var(--muted)")
         + person(280, 150, s=0.85, **THIEF) + env(340, 60, 0.7, sender="⟦보낸 이: 우리 성|from: our castle⟧") + label(310, 270, "⟦우리 이름으로 가짜를 보내요|sends fakes in our name⟧", 11, "var(--bad)")
         + "".join(f'<path d="M440 100 Q{500} {y - 30} 560 {y}" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>' for y in (60, 150, 240))
         + small_castle(560, 20, 0.45) + env(650, 40, 0.5, sealed=SEAL_COLOR, wrong=True, cross=True)
         + small_castle(560, 110, 0.45) + env(650, 130, 0.5, sealed=SEAL_COLOR, wrong=True, cross=True)
         + small_castle(560, 200, 0.45) + env(650, 220, 0.5, sealed=SEAL_COLOR, wrong=True, cross=True)
         + label(380, 302, "⟦우리 이름으로 온 가짜는 마을 어느 성에서도 버려요|fakes in our name get thrown away at every castle in the village⟧", 13, "var(--ink)", cls="d"))

LIST_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M20 22 h10 M20 34 h10 M20 46 h10" stroke="#142033" stroke-width="2" stroke-linecap="round"/><path d="M36 20 l3 3 l6 -6 M36 32 l3 3 l6 -6" stroke="var(--good)" stroke-width="2.5" fill="none"/><path d="M36 42 l8 8 M44 42 l-8 8" stroke="var(--bad)" stroke-width="2.5"/>')
SEAL_I = icon(f'<circle cx="32" cy="32" r="20" fill="{SEAL_COLOR}"/><circle cx="32" cy="32" r="15" fill="none" stroke="#FFF8E7" stroke-width="1.5" opacity="0.7"/><path d="M20 38 l-3 -15 l8 6 l7 -11 l7 11 l8 -6 l-3 15z" fill="#FFF8E7"/>')
NOTE_I = icon('<rect x="14" y="8" width="36" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="24" cy="22" r="4" fill="#4A5A72"/><circle cx="24" cy="34" r="4" fill="var(--accent)"/><circle cx="24" cy="46" r="4" fill="var(--bad)"/><path d="M32 22 h12 M32 34 h12 M32 46 h12" stroke="#142033" stroke-width="2" stroke-linecap="round"/>')
GATE_I = icon('<rect x="10" y="20" width="44" height="28" rx="6" fill="#4A5A72"/><rect x="18" y="28" width="28" height="14" rx="2" fill="var(--panel)"/><path d="M18 30 l14 8 l14 -8" stroke="var(--line)" stroke-width="2" fill="none"/><circle cx="50" cy="18" r="9" fill="var(--good)"/><path d="M45 18 l4 4 l6 -7" stroke="#FFF" stroke-width="2.5" fill="none"/>')

PAGE = {
    "slug": "emailsec", "order": 85,
    "title": ("우체국 도장 세 개", "The Post Office\'s Three Stamps"),
    "h1": ("<em>이메일 보안</em>이 뭐예요?", "What is <em>Email Security</em>?"),
    "sub": ("이메일 보안(SPF·DKIM·DMARC)을 진짜 우체국만 찍을 수 있는 도장 세 개 이야기로 풀어봤어요.",
            "Email security (SPF, DKIM, DMARC), told as a story about three stamps only the real post office can press."),
    "panels": [
        {"svg": P1, "alt": ("도둑이 봉투에 '보낸 이: 왕궁 우체국'이라고 써서 성 우체통에 넣고, 받은 사람은 '왕궁에서 온 편지네!' 하고 좋아함", "A thief writes 'from: the Royal Post' on an envelope and drops it in the castle mailbox; the receiver is delighted — a letter from the Royal Post!"),
         "caption": ("봉투에 '왕궁 우체국'이라고 아무나 쓸 수 있어요.", "Anyone can write 'the Royal Post' on an envelope."),
         "small": ('<a href="phishing-ko.html">가짜 편지</a>가 무서운 이유예요. 보낸 이 이름은 그냥 글씨예요. 도둑도 쓸 수 있어요.',
                   'That is what makes a <a href="phishing-en.html">fake letter</a> dangerous. The sender\'s name is just handwriting. A thief can write it too.')},
        {"svg": P2, "alt": ("똑같이 생긴 봉투 두 장 — 하나는 진짜 우체국, 하나는 도둑이 보냄. 문지기가 땀 흘리며 '똑같이 생겼는데…'", "Two identical envelopes — one from the real post, one from the thief. The doorkeeper sweats: they look exactly the same…"),
         "caption": ("봉투만 보면 누구도 몰라요.", "Looking at the envelope alone, nobody can tell."),
         "small": ("문지기가 아무리 똑똑해도 글씨만으론 못 골라요. 게다가 도둑은 우리 성 이름으로도 가짜를 마을에 보내요. 그러면 우리 편지까지 못 믿게 돼요.",
                   "No matter how sharp the doorkeeper is, handwriting isn\'t enough. Worse, the thief also sends fakes to the village in our castle\'s name — and then nobody trusts our real letters either.")},
        {"svg": P3, "hero": True, "alt": ("세 가지: 보낼 수 있는 배달부 명단, 우체국만 찍는 밀랍 봉인 도장, 도장이 틀리면 어떻게 할지 적은 안내문(그냥 두기·따로 두기·버리기). 셋 다 마을 안내소에 붙여 둠", "Three things: a list of couriers allowed to deliver, a wax seal only the post can press, and a note saying what to do if the seal is wrong (leave it, set it aside, throw it away). All three pinned at the village desk"),
         "caption": ("이메일 보안은 우체국이 미리 붙여 둔 도장 세 개예요.", "Email security is three stamps the post office puts up ahead of time."),
         "small": ('배달부 명단, 봉인 도장, 안내문. 셋 다 <a href="dns-ko.html">마을 안내소</a>에 붙여 둬서 누구든 물어볼 수 있어요.',
                   'A courier list, a seal, and a note. All three are pinned at the <a href="dns-en.html">village desk</a>, so anyone can look them up.'),
         "tricks": (4, [
             (LIST_I, ("배달부 명단", "The courier list"), ("이 우체국 편지는 A와 B만 나를 수 있어요", "only A and B may carry this post\'s letters"), "calm"),
             (SEAL_I, ("봉인 도장", "The seal"), ("우체국만 찍을 수 있고, 뜯으면 깨져요", "only the post can press it; it breaks if opened"), "calm"),
             (NOTE_I, ("안내문", "The note"), ("틀리면 그냥 두기 · 따로 두기 · 버리기", "if wrong: leave it, set aside, throw away"), "warm"),
             (GATE_I, ("우체통 문지기", "The mailbox keeper"), ("편지마다 세 개를 확인해요", "checks all three on every letter")),
         ])},
        {"svg": P4, "alt": ("문지기가 봉인된 편지를 들고 확인표를 봄 — 배달부가 명단에 있나, 봉인이 진짜인가, 아니면 안내문대로. 옆에 상자 세 개: 그냥 두기, 격리함, 버리기", "The doorkeeper holds a sealed letter and reads the checklist — courier on the list? seal real? if not, follow the note. Three boxes beside: deliver, quarantine, reject"),
         "caption": ("문지기는 편지마다 명단과 도장을 확인해요.", "The keeper checks the list and the seal on every letter."),
         "small": ("배달부가 명단에 있거나 봉인이 진짜면 통과예요. 둘 다 아니면 안내문대로 해요 — 그냥 두거나, 따로 두거나, 버리거나.",
                   "If the courier is on the list or the seal is real, it passes. If neither, the keeper does what the note says — leave it, set it aside, or throw it away.")},
        {"svg": P5, "alt": ("우리 성의 안내문은 '틀리면 버리기'. 도둑이 우리 성 이름으로 가짜 편지를 마을의 다른 성 세 곳에 보내지만, 모두 봉인이 틀려서 버려짐", "Our castle\'s note says: throw it away. The thief sends fakes in our name to three other castles, but every one has a wrong seal and gets thrown out"),
         "caption": ("우리 이름으로 온 가짜는 마을 어느 성에서도 버려요.", "Fakes in our name get thrown away at every castle in the village."),
         "small": ('도장은 우리 성만 지키는 게 아니라 우리 이름도 지켜요. 그래도 도장이 다 맞는 진짜 우체국 편지에 거짓말이 들어 있을 수 있어요 — 그건 <a href="awareness-ko.html">도둑 수업</a>에서 배워요.',
                   'The stamps protect our name, not only our castle. But a letter with every stamp correct can still carry a lie — that part is taught in the <a href="awareness-en.html">thief lessons</a>.')},
    ],
    "summary": (("<b>이메일 보안</b> = 우체국이 마을 안내소에 미리 붙여 둔 <b>도장 세 개</b> — 누가 보낼 수 있나(명단), 진짜 우체국 도장인가(봉인), 틀리면 어떻게 하나(안내문). 문지기가 편지마다 확인해요.",
                 "<b>Email security</b> = <b>three stamps</b> the post office pins at the village desk — who may send (the list), is the seal real (the seal), what to do if wrong (the note). The keeper checks every letter."),
                ("SPF는 이 도메인의 메일을 보낼 수 있는 서버 목록, DKIM은 도메인 소유자만 만들 수 있는 전자 서명, DMARC는 둘 다 실패했을 때의 정책(none·quarantine·reject)이에요. 셋 다 DNS 레코드로 공개되고, 받는 쪽 메일 게이트웨이가 확인해요.",
                 "SPF lists the servers allowed to send mail for a domain, DKIM is a digital signature only the domain owner can make, and DMARC is the policy for when both fail (none, quarantine, reject). All three are published as DNS records and checked by the receiving mail gateway.")),
    "glossary": [
        ("배달부 명단", "SPF", ("누가 보낼 수 있나.", "Who may send."), ('우리 성 이름으로 편지를 보낼 수 있는 배달부 목록이에요. <a href="dns-ko.html">마을 안내소</a>에 붙여 둬요.', 'The list of couriers allowed to send letters in our castle\'s name. Pinned at the <a href="dns-en.html">village desk</a>.')),
        ("봉인 도장", "DKIM", ("우체국만 찍는 도장.", "The seal only the post can press."), ("편지 내용에 맞춰 찍어서, 중간에 고치면 도장이 깨져요.", "Pressed to match the letter\'s contents, so it breaks if anyone edits it on the way.")),
        ("안내문", "DMARC", ("틀리면 어떻게 하나.", "What to do if it\'s wrong."), ("그냥 두기·따로 두기·버리기 중 하나를 우리 성이 정해요. 결과 보고서도 받아요.", "Our castle picks one of: leave it, set it aside, throw it away. It also gets reports of what happened.")),
        ("이름 빌리기", "Spoofing", ("봉투에 남의 이름 쓰기.", "Writing someone else\'s name on the envelope."), ("도둑이 우리 성 이름으로 가짜 편지를 보내는 것. 도장 세 개가 막는 바로 그거예요.", "The thief sending fakes in our castle\'s name. Exactly what the three stamps stop.")),
        ("우체통 문지기", "Email gateway", ("편지마다 확인하는 사람.", "The one who checks every letter."), ("도장을 보고, 벌레가 붙었나 보고, 이상하면 따로 둬요.", "Reads the stamps, checks for bugs, sets the odd ones aside.")),
        ("격리함", "Quarantine", ("따로 두는 상자.", "The set-aside box."), ("버리진 않지만 바로 주지도 않아요. 나중에 사람이 봐요.", "Not thrown away, but not delivered either. A person looks later.")),
        ("가짜 편지", "Phishing", ("우체국인 척하는 편지.", "A letter pretending to be the post."), ('도장이 없던 시절엔 글씨만 믿었어요. → <a href="phishing-ko.html">우체국인 척하는 편지</a>', 'Before the stamps, we trusted handwriting alone. → <a href="phishing-en.html">the letter that pretends to be the post</a>')),
        ("도둑 수업", "Security awareness training", ("도장이 다 맞아도 의심하기.", "Staying wary even when every stamp is right."), ('진짜 우체국 편지에도 거짓말은 들어갈 수 있어요. → <a href="awareness-ko.html">성 사람 모두가 듣는 도둑 수업</a>', 'Even a genuine letter can carry a lie. → <a href="awareness-en.html">the thief lessons everyone attends</a>')),
    ],
}
