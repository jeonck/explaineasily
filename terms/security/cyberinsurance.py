from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
KING = dict(hat="#E9B44C", shirt="#7B3FA0")
MERCHANT = dict(hat="#C9822B", shirt="#5A3B22")
BAG = '<rect x="50" y="70" width="36" height="30" rx="4" fill="var(--night)"/><path d="M58 70 v-8 a10 10 0 0 1 20 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>'
GOLD, GOLD_DARK = "#E9B44C", "#C9822B"


def coin(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><circle r="12" fill="{GOLD}" stroke="{GOLD_DARK}" stroke-width="3"/><circle r="5" fill="none" stroke="{GOLD_DARK}" stroke-width="2"/></g>'


def coins(x, y, n, s=1.0):
    return "".join(coin(x + (i % 2) * 14 - 7, y - (i // 2) * 9, s) for i in range(n))


def sack(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-26 6 q-6 -30 18 -40 l-6 -12 h28 l-6 12 q24 10 18 40 q-2 22 -26 22 q-24 0 -26 -22z" fill="#8B5E3C"/>'
            f'<path d="M-14 -34 h28" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>{coin(0, 0, 0.7)}</g>')


def chest(x, y, s=1.0, locked=False):
    lock = ('<rect x="-10" y="-6" width="20" height="16" rx="3" fill="var(--bad)"/><path d="M-6 -6 V-12 a6 6 0 0 1 12 0 V-6" stroke="var(--bad)" stroke-width="4" fill="none"/>' if locked else "")
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-14" width="60" height="36" rx="3" fill="#8B5E3C"/><path d="M-30 -14 h60 v-4 a30 12 0 0 0 -60 0z" fill="#5A3B22"/>{lock}</g>'


def paper(x, y, s=1.0, stamp=None, text=None):
    st = f'<circle cx="14" cy="16" r="9" fill="{stamp}"/>' if stamp else ""
    tx = label(0, -8, text, 10, "#142033", cls="d") if text else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-30" width="52" height="64" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-18 4 h28 M-18 12 h18" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{tx}{st}</g>')


def hammer(x, y, rot=-30, s=1.0):
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect x="-3" y="-14" width="6" height="40" fill="#8B5E3C"/><rect x="-14" y="-24" width="28" height="12" rx="3" fill="var(--stone-dark)"/></g>'


def arrow(x1, y1, x2, y2, color="var(--accent)"):
    d = 1 if x2 > x1 else -1
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"/><path d="M{x2} {y2} l{-12 * d} -6 v12z" fill="{color}"/>'


def check_row(x, y, text, ok):
    m = ('<circle r="10" fill="var(--good)"/><path d="M-5 0 l4 4 l7 -8" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>' if ok
         else '<circle r="10" fill="var(--bad)"/><path d="M-5 -5 l10 10 M5 -5 l-10 10" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>')
    return label(x, y + 4, text, 11, "#142033", "start") + f'<g transform="translate({x + 262},{y})">{m}</g>'


# 1. 아무리 잘 지켜도 털릴 수 있어요
P1 = svg(310, sky(310) + castle(150, 70, 1.0)
         + person(100, 170, s=0.7, face=EYES, **GUARD) + person(280, 64, s=0.5, face=EYES, **GUARD)
         + dog(470, 255, 0.6, bark=True)
         + person(690, 160, s=0.7, face=MASK, extra=BAG) + label(680, 262, "⟦그래도 하나는 가져가요|and still, one gets through⟧", 10, "var(--bad)")
         + label(380, 298, "⟦문도 잠그고 개도 있는데 — 그래도 가끔 털려요|the doors are locked and the dog is awake — and still, sometimes, you get robbed⟧", 12, "var(--ink)"))

# 2. 털리면 드는 돈
COLS = ((95, chest(95, 105, 0.9, locked=True) + hammer(135, 90, -30, 0.7), "⟦되돌리기|putting it back⟧", "⟦목수와 여분 상자|carpenter and spare chest⟧"),
        (285, "".join(paper(285 + i * 10 - 10, 105 - i * 6, 0.8) for i in range(3)), "⟦손님에게 알리기|telling the guests⟧", "⟦편지를 보내요|letters go out⟧"),
        (475, paper(475, 105, 0.9, stamp="var(--bad)", text="⟦벌금|FINE⟧"), "⟦검사관 벌금|the inspector\'s fine⟧", "⟦규칙을 못 지켜서|for the rules not kept⟧"),
        (665, '<rect x="630" y="80" width="70" height="50" rx="4" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/>' + label(665, 110, "⟦닫힘|CLOSED⟧", 12, "var(--bad)", cls="d"), "⟦장사 못 한 날|days with no trade⟧", "⟦문 닫은 동안|while the doors were shut⟧"))
P2 = svg(320, sky(320)
         + label(380, 36, "⟦털리면 드는 돈|what a break-in costs⟧", 14, "var(--ink)", cls="d")
         + "".join(art + coins(x, 195, 5, 0.9) + label(x, 250, t, 12, "var(--ink)", cls="d") + label(x, 268, sub, 10, "var(--muted)") for x, art, t, sub in COLS)
         + label(380, 302, "⟦왕의 금고가 비어요 — 도둑이 가져간 것보다 더 들어요|the king\'s coffer empties — it costs more than the thief took⟧", 12, "var(--ink)"))

# 3. 도둑 보험 (hero)
P3 = svg(340, sky(340)
         + person(120, 110, s=0.95, face=SMILE, **MERCHANT) + label(155, 245, "⟦보험 상인|the insurance merchant⟧", 11, "var(--muted)")
         + person(600, 110, s=0.9, face=SMILE, **KING) + label(630, 245, "⟦왕|the king⟧", 11, "var(--muted)")
         + label(380, 120, "⟦매달 조금씩|a little every month⟧", 12, "var(--accent)", cls="d")
         + arrow(590, 145, 205, 145) + coin(300, 145, 0.8) + coin(380, 145, 0.8) + coin(460, 145, 0.8)
         + arrow(205, 203, 590, 203, "var(--good)") + sack(380, 203, 1.0)
         + label(380, 248, "⟦털린 날엔 큰 자루|on the day you\'re robbed, a big sack⟧", 12, "var(--good)", cls="d")
         + person(700, 60, s=0.55, face=MASK, extra=BAG) + label(720, 140, "⟦도둑이 왔어요|the thief came⟧", 9, "var(--bad)")
         + label(380, 320, "⟦미리 조금 내고, 털리면 많이 받아요 — 도둑 보험이에요|pay a little now, get a lot back if robbed — that\'s thief insurance⟧", 13, "var(--ink)", cls="d"))

# 4. 상인은 먼저 물어요
QUESTIONS = (("⟦문에서 세 번 확인하나요?|three checks at the door?⟧", True), ("⟦여분 상자가 멀리 있나요?|a spare chest far away?⟧", True),
             ("⟦도둑 들었을 때 순서표 있나요?|a plan for when a thief gets in?⟧", False), ("⟦목수가 판자를 대나요?|does the carpenter patch holes?⟧", True))
P4 = svg(340, sky(340)
         + person(90, 120, s=0.85, face=EYES, **MERCHANT)
         + bubble(60, 30, 250, 34, "⟦먼저 몇 가지 물어볼게요|first, a few questions⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + '<rect x="250" y="80" width="310" height="210" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + label(405, 106, "⟦상인의 질문표|THE MERCHANT\'S CHECKLIST⟧", 12, "#142033", cls="d")
         + "".join(check_row(270, 145 + i * 38, q, ok) for i, (q, ok) in enumerate(QUESTIONS))
         + person(620, 130, s=0.85, face=FROWN, extra=SWEAT, **KING)
         + label(650, 250, "⟦순서표가 없으면 값이 두 배|no plan? the price doubles⟧", 10, "var(--bad)") + label(650, 268, "⟦아예 안 받아주기도 해요|or no deal at all⟧", 10, "var(--bad)")
         + label(380, 320, "⟦잘 지키는 성일수록 싸요 — 상인도 손해 보긴 싫거든요|the better-guarded the castle, the cheaper — the merchant hates losing too⟧", 12, "var(--ink)", cls="d"))

# 5. 보험은 문을 대신 잠가주지 않아요
P5 = svg(300, sky(300)
         + castle(20, 60, 0.42) + '<g transform="translate(117,132) scale(0.8)"><rect x="-13" y="-8" width="26" height="20" rx="4" fill="var(--bad)"/><path d="M-8 -8 V-14 a8 8 0 0 1 16 0 V-8" stroke="var(--bad)" stroke-width="4" fill="none"/></g>'
         + person(230, 100, s=0.7, face=MASK, extra=BAG) + label(115, 172, "⟦도둑은 그대로 와요|the thief still comes⟧", 11, "var(--bad)")
         + person(360, 90, s=0.8, face=SMILE, **MERCHANT) + sack(450, 150, 0.9) + label(400, 205, "⟦돈은 돌려줘요|the money comes back⟧", 11, "var(--good)")
         + '<path d="M520 40 V220" stroke="var(--line)" stroke-width="2" stroke-dasharray="6 8"/>'
         + label(640, 60, "⟦돌려주지 못하는 것|what it cannot return⟧", 12, "var(--ink)", cls="d")
         + '<g transform="translate(565,110)"><path d="M0 14 C-18 0 -14 -18 0 -10 C14 -18 18 0 0 14z" fill="var(--bad)"/><path d="M-2 -6 l4 8 l-4 6" stroke="#FFF" stroke-width="2" fill="none"/></g>' + label(565, 150, "⟦손님의 믿음|the guests\' trust⟧", 9, "var(--muted)")
         + '<g transform="translate(632,110)"><rect x="-16" y="-14" width="32" height="30" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="-16" y="-14" width="32" height="8" rx="3" fill="var(--accent)"/><path d="M-8 6 l16 -12 M-8 -6 l16 12" stroke="var(--bad)" stroke-width="2.5"/></g>' + label(632, 150, "⟦지나간 날들|the days lost⟧", 9, "var(--muted)")
         + '<g transform="translate(712,110)"><circle r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><rect x="6" y="-2" width="22" height="5" fill="#E9B44C"/><rect x="18" y="3" width="3" height="6" fill="#E9B44C"/></g>' + label(712, 150, "⟦잠그는 건 우리 일|locking is our job⟧", 9, "var(--muted)")
         + label(380, 245, "⟦도둑에게 몸값을 대신 내주는지는 상인마다 달라요|whether it pays the thief\'s ransom differs by merchant⟧", 10, "var(--muted)")
         + label(380, 282, "⟦보험은 돈을 돌려줘요 — 문은 여전히 우리가 잠가야 해요|insurance returns money — the door is still ours to lock⟧", 12, "var(--ink)", cls="d"))

COIN_I = icon(f'<circle cx="24" cy="40" r="11" fill="{GOLD}" stroke="{GOLD_DARK}" stroke-width="3"/><circle cx="40" cy="32" r="11" fill="{GOLD}" stroke="{GOLD_DARK}" stroke-width="3"/><circle cx="32" cy="20" r="11" fill="{GOLD}" stroke="{GOLD_DARK}" stroke-width="3"/><circle cx="32" cy="20" r="4" fill="none" stroke="{GOLD_DARK}" stroke-width="2"/>')
SACK_I = icon(f'<path d="M12 40 q-4 -22 14 -30 l-4 -6 h20 l-4 6 q18 8 14 30 q-2 16 -20 16 q-18 0 -20 -16z" fill="#8B5E3C"/><path d="M22 16 h20" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="40" r="7" fill="{GOLD}" stroke="{GOLD_DARK}" stroke-width="2"/>')
ASK_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="22" cy="22" r="5" fill="var(--good)"/><circle cx="22" cy="34" r="5" fill="var(--good)"/><circle cx="22" cy="46" r="5" fill="var(--bad)"/><path d="M32 22 h14 M32 34 h14 M32 46 h10" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
NOLOCK_I = icon('<rect x="14" y="28" width="30" height="24" rx="4" fill="var(--stone-dark)"/><path d="M20 28 V20 a9 9 0 0 1 18 0 V28" stroke="var(--stone-dark)" stroke-width="5" fill="none"/><circle cx="29" cy="40" r="4" fill="var(--accent)"/><circle cx="54" cy="18" r="6" fill="#E8C9A8"/><rect x="49" y="26" width="10" height="14" rx="3" fill="#7B3FA0"/><path d="M50 40 l-6 6" stroke="#E8C9A8" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "cyberinsurance", "order": 100,
    "title": ("도둑 보험", "Thief Insurance"),
    "h1": ("<em>사이버 보험</em>이 뭐예요?", "What is <em>Cyber Insurance</em>?"),
    "sub": ("사이버 보험(Cyber Insurance)을 미리 조금 내고 털리면 많이 받는 도둑 보험 상인 이야기로 풀어봤어요.",
            "Cyber insurance, told as a story about a merchant who takes a little now and pays out a lot on the day you are robbed."),
    "panels": [
        {"svg": P1, "alt": ("경비 둘과 짖는 경비견이 지키는 성. 그런데도 오른쪽 구석으로 도둑이 자루를 들고 빠져나간다", "A castle guarded by two guards and a barking dog. Even so, in the right corner, a thief slips away with a sack"),
         "caption": ("아무리 잘 지켜도 털릴 수 있어요.", "However well you guard, you can still be robbed."),
         "small": ('문도 잠그고 <a href="edr-ko.html">개</a>도 깨어 있어요. 그래도 가끔은 하나가 빠져나가요 — 완벽한 성은 없어요.',
                   'The doors are locked and the <a href="edr-en.html">dog</a> is awake. And still, now and then, one gets through — no castle is perfect.')},
        {"svg": P2, "alt": ("금화 더미 네 개: 잠긴 상자를 고치는 되돌리기, 손님에게 보내는 편지들, 빨간 도장 찍힌 벌금 종이, 닫힘 팻말이 걸린 가게", "Four piles of gold coins: putting back a locked chest, letters to the guests, a fine paper with a red seal, and a shop with a CLOSED sign"),
         "caption": ("털리면 돈이 많이 들어요. 고치고, 알리고, 벌금 내고, 장사도 못 해요.", "A break-in costs a lot. Fixing, telling, fines, and days with no trade."),
         "small": ('상자를 되돌리고, <a href="privacy-ko.html">손님에게 편지</a>를 보내고, <a href="compliance-ko.html">검사관에게 벌금</a>을 내고, 문 닫은 동안 장사도 못 해요. 도둑이 가져간 것보다 더 들어요.',
                   'Putting the chest back, <a href="privacy-en.html">letters to the guests</a>, a <a href="compliance-en.html">fine to the inspector</a>, and no trade while the doors are shut. It costs more than the thief took.')},
        {"svg": P3, "hero": True, "alt": ("보험 상인과 왕 사이에 화살표 둘. 위쪽은 왕에게서 상인에게로 작은 금화들 — 매달 조금씩. 아래쪽은 상인에게서 왕에게로 큰 자루 — 털린 날엔 큰 자루. 구석엔 도둑", "Two arrows between the insurance merchant and the king. On top, small coins flow from king to merchant — a little every month. Below, a big sack flows from merchant to king — on the day you are robbed. A thief in the corner"),
         "caption": ("사이버 보험은 미리 조금 내고, 털리면 많이 받는 약속이에요.", "Cyber insurance is a promise: pay a little now, get a lot back if you are robbed."),
         "small": ("왕은 매달 상인에게 금화 몇 닢을 내요. 도둑이 든 날, 상인이 큰 자루를 가져와요 — 고치고, 알리고, 벌금 내는 돈이요.", "Every month the king pays the merchant a few coins. On the day a thief gets in, the merchant brings a big sack — for the fixing, the telling and the fines."),
         "tricks": (4, [
             (COIN_I, ("미리 조금", "A little in advance"), ("매달 금화 몇 닢", "a few coins every month"), "calm"),
             (SACK_I, ("털리면 받아요", "Paid when robbed"), ("고치고 알리고 벌금 내는 돈", "for fixing, telling and fines"), "calm"),
             (ASK_I, ("상인이 먼저 물어요", "The merchant asks first"), ("문은 잠그나요? 여분 상자는요?", "locked doors? a spare chest?"), "warm"),
             (NOLOCK_I, ("문은 안 잠가줘요", "It won\'t lock the door"), ("잠그는 건 여전히 우리 일", "locking is still our job"), "warm"),
         ])},
        {"svg": P4, "alt": ("상인의 질문표: 문에서 세 번 확인 체크, 여분 상자 멀리 체크, 도둑 들었을 때 순서표 X, 목수가 판자 대기 체크. 왕이 땀을 흘리고 '순서표가 없으면 값이 두 배'", "The merchant\'s checklist: three checks at the door yes, spare chest far away yes, a plan for when a thief gets in no, carpenter patches holes yes. The king sweats — no plan? the price doubles"),
         "caption": ("상인은 먼저 물어요. 문은 잠그나요? 여분 상자는요? 순서표는요?", "The merchant asks first. Do you lock the door? A spare chest? A plan?"),
         "small": ('<a href="mfa-ko.html">세 번 확인하는 문지기</a>, <a href="backup-ko.html">멀리 둔 여분 상자</a>, <a href="incident-ko.html">도둑 들었을 때 순서표</a>가 없으면 안 받아주거나 비싸요. 잘 지키는 성일수록 싸요.',
                   'No <a href="mfa-en.html">three-check doorkeeper</a>, no <a href="backup-en.html">spare chest far away</a>, no <a href="incident-en.html">plan for when a thief gets in</a> — then no deal, or a dear one. The better-guarded the castle, the cheaper.')},
        {"svg": P5, "alt": ("왼쪽: 성문에 도둑 자물쇠, 도둑은 그대로 온다. 가운데: 상인이 자루를 건넨다 — 돈은 돌려줘요. 오른쪽: 돌려주지 못하는 것 — 깨진 하트(손님의 믿음), X 친 달력(지나간 날), 열쇠(잠그는 건 우리 일)", "Left: the thief\'s lock on the gate — the thief still comes. Middle: the merchant hands over a sack — the money comes back. Right: what it cannot return — a cracked heart (the guests\' trust), a crossed-out calendar (the days lost), a key (locking is our job)"),
         "caption": ("보험은 돈을 돌려줘요. 문은 여전히 우리가 잠가야 해요.", "Insurance returns money. The door is still ours to lock."),
         "small": ('보험은 <a href="risk-ko.html">위험을 상인에게 넘기는</a> 거지, 위험을 없애는 게 아니에요. <a href="ransomware-ko.html">도둑에게 주는 몸값</a>까지 내주는지는 상인마다 달라요.',
                   'Insurance <a href="risk-en.html">hands the risk to the merchant</a>; it does not make the risk go away. Whether it also pays the <a href="ransomware-en.html">ransom to the thief</a> differs by merchant.')},
    ],
    "summary": (("<b>사이버 보험</b> = <b>미리 조금 내고, 털리면 많이 받는</b> 약속. 상인은 <b>문을 잠그는지 먼저 묻고</b>, 잘 지키는 성일수록 싸요. 돈은 돌려줘도 <b>문은 대신 안 잠가줘요</b>.",
                 "<b>Cyber insurance</b> = a promise to <b>pay a little now and get a lot back if robbed</b>. The merchant <b>asks first whether you lock the door</b>, and a well-guarded castle pays less. It returns money — it <b>never locks the door for you</b>."),
                ("Cyber Insurance. 사고 대응, 복구, 고객 통지, 법적 비용, 벌금, 영업 중단 손실 같은 사이버 사고 비용을 보장하는 보험이에요. 인수 심사에서 MFA·백업·사고 대응 계획 같은 통제를 요구하고, 없으면 가입을 거절하거나 보험료를 올려요. 랜섬 지급 보장 여부와 면책 조항은 보험사마다 달라요.",
                 "A policy covering the costs of a cyber incident: response, recovery, customer notification, legal fees, fines and business interruption. Underwriting requires controls like MFA, backups and an incident response plan, and refuses or raises premiums without them. Ransom coverage and exclusions vary by insurer.")),
    "glossary": [
        ("사이버 보험", "Cyber insurance", ("도둑 보험.", "Thief insurance."), ("털렸을 때 드는 돈을 상인이 대신 내줘요. 매달 조금 내는 대신.", "The merchant pays the cost of a break-in — in exchange for a little every month.")),
        ("위험 전가", "Risk transfer", ("위험을 상인에게 넘기기.", "Handing the risk to the merchant."), ('위험을 없애는 게 아니라 옮기는 거예요. → <a href="risk-ko.html">위험 장부</a>', 'The risk is moved, not removed. → <a href="risk-en.html">the risk ledger</a>')),
        ("보장 범위", "Coverage", ("자루에 들어가는 것.", "What goes in the sack."), ("되돌리기, 손님에게 알리기, 벌금, 장사 못 한 날 — 어디까지 내주는지 약속에 적혀 있어요.", "Fixing, telling the guests, fines, days with no trade — the promise says how far it goes.")),
        ("면책", "Exclusions", ("자루에 안 들어가는 것.", "What stays out of the sack."), ("문을 열어둔 채 털리면 안 내줘요. 전쟁, 오래된 구멍, 거짓 답변도요.", "Robbed with the door left open? Not covered. Nor war, old known holes, or false answers.")),
        ("인수 심사", "Underwriting", ("상인의 질문표.", "The merchant\'s checklist."), ('문지기, 여분 상자, 순서표, 목수가 있는지 먼저 물어요. → <a href="mfa-ko.html">세 번 확인하는 문지기</a>', 'Asks first about the doorkeeper, the spare chest, the plan and the carpenter. → <a href="mfa-en.html">the doorkeeper who checks three times</a>')),
        ("랜섬 지급 논쟁", "The ransom debate", ("도둑에게 주는 돈.", "Money paid to the thief."), ('상인이 몸값까지 내주면 도둑이 더 몰려온다는 걱정이 있어요. → <a href="ransomware-ko.html">상자마다 채운 도둑의 자물쇠</a>', 'If the merchant pays ransoms, more thieves may come — so goes the worry. → <a href="ransomware-en.html">the thief\'s lock on every chest</a>')),
        ("사고 대응 비용", "Incident response costs", ("순서표를 도는 데 드는 돈.", "The cost of working the plan."), ('밖에서 부른 파수꾼, 밤샘 일, 편지 값. → <a href="incident-ko.html">도둑 들었을 때 순서표</a>', 'Outside watchmen, nights of work, the price of letters. → <a href="incident-en.html">the plan for when a thief gets in</a>')),
        ("보험료", "Premium", ("매달 내는 금화.", "The monthly coins."), ("잘 지키는 성은 적게, 허술한 성은 많이 — 아예 못 들기도 해요.", "A well-guarded castle pays little, a careless one pays a lot — or cannot buy in at all.")),
    ],
}
