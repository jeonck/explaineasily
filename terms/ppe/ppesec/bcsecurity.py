from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")


def ledger(x, y, s=1.0, color="#FFF8E7", check=False):
    tick = '<path d="M-10 0 l6 7 l14 -16" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>' if check else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-32" width="52" height="64" rx="3" fill="{color}" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M-16 -18 h32 M-16 -8 h32 M-16 2 h20" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/>{tick}</g>')


def chain_link(x, y, s=1.0, broken=False):
    c = "var(--bad)" if broken else "var(--good)"
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="-8" width="32" height="16" rx="8" fill="none" stroke="{c}" stroke-width="4"/></g>'


def key(x, y, s=1.0, color="#E9B44C"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="10" fill="none" stroke="{color}" stroke-width="5"/><rect x="8" y="-3" width="30" height="6" fill="{color}"/>'
            f'<rect x="24" y="3" width="4" height="7" fill="{color}"/><rect x="32" y="3" width="4" height="9" fill="{color}"/></g>')


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 장부를 한 사람만 들고 있으면 몰래 고칠 수 있어요
P1 = svg(280, sky(280)
         + person(200, 150, s=0.9, face=EYES, **CLERK) + ledger(280, 140, 1.1)
         + label(240, 240, "⟦서기 혼자 든 장부|a ledger only the clerk holds⟧", 12, "var(--muted)")
         + bubble(360, 70, 220, 40, "⟦여기 숫자, 살짝 바꿔도 아무도 몰라요|tweak this number — no one will know⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 262, "⟦한 사람만 들고 있으면 몰래 고칠 수 있어요|held by just one person, it can be quietly changed⟧", 13, "var(--ink)"))

# 2. 사본을 다 나눠 가져도 새 걱정이 생겨요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + "".join(person(90 + i * 110, 150, s=0.65, face=SMILE) for i in range(6))
         + "".join(ledger(90 + i * 110, 90, 0.7) for i in range(6))
         + label(380, 240, "⟦장부 사본을 마을 사람 전부가 나눠 가지면 안전해 보여요|a ledger copy in every villager's hand looks safe⟧", 12, "var(--good)", cls="d")
         + label(380, 262, "⟦그런데 그 자체로 새 걱정거리가 생겨요|but this brings brand-new worries of its own⟧", 13, "var(--bad)"))

# 3. 블록체인 = 모두가 들고 다니는, 서로 지문으로 이어 붙인 장부 (hero)
P3 = svg(340, sky(340)
         + "".join(person(60 + i * 160, 150, s=0.6, face=SMILE) for i in range(5))
         + "".join(ledger(60 + i * 160, 90, 0.65) for i in range(5))
         + "".join(chain_link(140 + i * 160, 120, 0.9) for i in range(4))
         + label(380, 30, "⟦블록체인 = 마을 사람 모두가 든 장부, 페이지마다 이전 페이지의 지문을 적어요|blockchain = a ledger everyone holds, each page carrying the fingerprint of the page before it⟧", 13, "var(--ink)", cls="d")
         + label(380, 230, "⟦과반수 사본이 똑같아야 그 페이지가 진짜로 인정돼요|a page only counts as real once most copies agree⟧", 12, "var(--muted)")
         + label(380, 320, "⟦한 명이 몰래 고치면 지문이 안 맞아서 바로 티나요|if one person quietly changes it, the fingerprint breaks — and it shows⟧", 12, "var(--muted)"))

# 4. 보안 고려사항 표
P4 = svg(320, sky(320)
         + box(50, 20, 660, 280, "⟦블록체인을 쓸 때 조심할 것|THINGS TO WATCH WITH BLOCKCHAIN⟧",
               ("⟦열쇠(개인키) 분실 — 관리자가 없어 되찾을 길이 없어요|lost private key — no administrator to recover it for you⟧",
                "⟦51% 공격 — 작은 마을일수록 과반수를 장악하기 쉬워요|51% attack — easier in a small village to seize the majority⟧",
                "⟦스마트 계약 버그 — 자동 실행이라 멈추거나 되돌리기 어려워요|smart-contract bugs — auto-run code is hard to pause or undo⟧",
                "⟦거래소·지갑 해킹 — 장부 자체보다 지갑과 거래소가 더 약해요|exchange/wallet hacks — the wallet and exchange are weaker than the ledger itself⟧"), 13))

# 5. 장부는 안전해도 열쇠 관리와 코드 버그는 못 막아요
P5 = svg(280, '<rect width="380" height="280" fill="var(--good-soft)"/><rect x="380" width="380" height="280" fill="var(--bad-soft)"/>'
         + ledger(190, 130, 1.2, check=True) + label(190, 220, "⟦장부 자체는 안전해요|the ledger itself is safe⟧", 12, "var(--good)", cls="d")
         + key(570, 100, 1.1) + '<path d="M570 130 q0 40 -40 60" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4" fill="none"/>'
         + label(570, 220, "⟦열쇠를 잃으면 아무도 못 찾아줘요|lose the key and no one can recover it⟧", 11, "var(--bad)", cls="d")
         + label(380, 262, "⟦안전은 장부가 아니라 열쇠 관리와 코드 품질에 달려 있어요|safety depends on key management and code quality, not the ledger⟧", 11, "var(--ink)"))

PAGE = {
    "slug": "bcsecurity", "order": 6,
    "title": ("모두가 들고 다니는, 지문으로 이어 붙인 장부", "The Ledger Everyone Carries, Stitched Together by Fingerprints"),
    "h1": ("<em>블록체인 보안 고려사항</em>이 뭐예요?", "What are <em>Blockchain Security Considerations</em>?"),
    "sub": ("블록체인 보안 고려사항을 마을 사람 모두가 들고 다니는, 지문으로 이어 붙인 장부 이야기로 풀어봤어요.",
            "Blockchain security considerations, told as a story about a ledger everyone in the village carries, stitched together page by page with fingerprints."),
    "panels": [
        {"svg": P1, "alt": ("서기 혼자 장부를 들고 '여기 숫자, 살짝 바꿔도 아무도 몰라요'라고 말함", "A clerk alone holds the ledger: tweak this number, no one will know"),
         "caption": ("장부를 한 사람만 들고 있으면 몰래 고칠 수 있어요.", "A ledger held by just one person can be quietly changed."),
         "small": ("아무도 안 보고 있으니까요.", "Because no one else is watching.")},
        {"svg": P2, "alt": ("마을 사람 여섯 명이 각자 장부 사본을 들고 웃고 있음", "Six villagers each hold a copy of the ledger, smiling"),
         "caption": ("사본을 다 나눠 가져도 새 걱정이 생겨요.", "Sharing a copy with everyone brings new worries of its own."),
         "small": ("안전해 보이지만, 그 자체로 새로운 문제들이 생겨요.", "It looks safe, but it comes with brand-new problems.")},
        {"svg": P3, "hero": True, "alt": ("다섯 사람이 각자 장부를 들고 고리로 연결된 모습. '과반수 사본이 똑같아야 진짜로 인정'", "Five people each hold a ledger, linked by rings between them, with the note that a page counts only once most copies agree"),
         "caption": ("블록체인은 모두가 들고 다니는, 지문으로 이어 붙인 장부예요.", "A blockchain is a ledger everyone carries, stitched together by fingerprints."),
         "small": ("한 명이 몰래 고치면 지문이 안 맞아서 바로 티나요.", "If one person quietly changes it, the fingerprint breaks — and it shows."),
         "tricks": (4, [
             (icon('<rect x="8" y="12" width="20" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="36" y="18" width="20" height="26" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'),
              ("장부 사본을 모두가", "Everyone holds a copy"), ("한 사람만 가진 게 아니에요", "not just one person"), "calm"),
             (icon('<circle cx="22" cy="32" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="42" cy="32" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/>'),
              ("이전 페이지 지문을 다음 페이지에", "Each page carries the last page's fingerprint"), ("해시로 이어 붙여요", "linked by a hash"), "warm"),
             (icon('<path d="M12 40 l12 -24 l12 24z" fill="none" stroke="var(--good)" stroke-width="4" stroke-linejoin="round"/><path d="M36 40 l12 -24 l12 24z" fill="none" stroke="var(--bad)" stroke-width="4" stroke-linejoin="round"/>'),
              ("과반수가 맞아야 진짜", "Majority agreement = real"), ("51% 공격은 그래서 위험해요", "which is why a 51% attack matters")),
             (icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 40 l20 -20" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'),
              ("한 번 적으면 못 지워요", "Once written, can't be erased"), ("코드 버그도 못 지워 더 위험해요", "even a buggy line stays — which is riskier"), "warm"),
         ])},
        {"svg": P4, "alt": ("블록체인을 쓸 때 조심할 것 네 가지: 개인키 분실, 51% 공격, 스마트 계약 버그, 거래소·지갑 해킹", "Four things to watch with blockchain: lost private keys, 51% attacks, smart-contract bugs, exchange and wallet hacks"),
         "caption": ("블록체인에는 또 다른 보안 고려사항이 있어요.", "Blockchain brings its own extra security considerations."),
         "small": ("장부 자체는 지문으로 지켜지지만, 열쇠·코드·지갑은 따로 지켜야 해요.", "The ledger itself is protected by fingerprints, but keys, code, and wallets each need their own protection.")},
        {"svg": P5, "alt": ("왼쪽: 초록 체크가 붙은 장부, '장부 자체는 안전해요'. 오른쪽: 열쇠가 사라지며 '열쇠를 잃으면 아무도 못 찾아줘요'", "Left: a ledger with a green check — the ledger itself is safe. Right: a key fading away — lose the key and no one can recover it"),
         "caption": ("장부는 안전해도 열쇠 관리와 코드 버그는 못 막아요.", "A safe ledger can't stop lost keys or buggy code."),
         "small": ('장부의 지문 구조는 <a href="hashing-ko.html">지문 찍기</a>와 같은 원리예요. 안전은 결국 <a href="password-ko.html">열쇠 관리</a>에 달려 있어요.',
                   'The ledger\'s fingerprint structure works the same way as <a href="hashing-en.html">fingerprinting</a>. Safety still comes down to <a href="password-en.html">key management</a>.')},
    ],
    "summary": (("<b>블록체인</b> = <b>모두가 사본</b>을 들고, 페이지마다 <b>이전 페이지 지문을 이어 붙여</b> 몰래 고치면 바로 티나는 장부. 하지만 <b>열쇠 분실·51% 공격·코드 버그</b>는 따로 조심해야 해요.",
                 "A <b>blockchain</b> = a ledger where <b>everyone holds a copy</b>, each page <b>stitched to the fingerprint of the one before</b>, so a quiet change shows instantly. But <b>lost keys, 51% attacks, and code bugs</b> still need their own watching."),
                ("블록체인은 거래 기록(블록)을 해시로 연결해 분산 저장하고, 과반수 합의로 유효성을 검증하는 분산원장 기술이에요. 데이터 자체의 위변조는 어렵지만, 개인키 분실은 복구가 불가능하고, 네트워크 참여자가 적으면 51% 공격 위험이 커지며, 스마트 계약의 코드 결함은 자동 실행되어 되돌리기 어렵고, 실제 침해 사고 대부분은 장부가 아니라 거래소·지갑 같은 주변 시스템에서 일어나요.",
                 "Blockchain links transaction records (blocks) with hashes into a distributed ledger, validated by majority consensus among participants. While tampering with the data itself is hard, a lost private key can never be recovered, a smaller network faces greater risk of a 51% attack, a flaw in smart-contract code runs automatically and is hard to reverse, and most real breaches happen not in the ledger but in surrounding systems like exchanges and wallets.")),
    "glossary": [
        ("분산원장", "Distributed ledger", ("모두가 든 장부 사본.", "A ledger copy in everyone's hands."), ("한 사람의 장부가 아니라 참여자 전체가 똑같은 사본을 들어요.", "Not one person's ledger — every participant holds an identical copy.")),
        ("해시 체인", "Hash chaining", ("페이지마다 이전 지문을 적기.", "Each page records the last one's fingerprint."), ('한 글자만 바꿔도 지문이 통째로 달라져요. → <a href="hashing-ko.html">물건마다 찍는 지문</a>', 'Change even one character, and the whole fingerprint changes. → <a href="hashing-en.html">a fingerprint for everything</a>')),
        ("합의 알고리즘", "Consensus (PoW/PoS)", ("과반수가 맞아야 진짜.", "Majority agreement makes it real."), ("일을 많이 한 사람(작업증명)이나 많이 맡긴 사람(지분증명)이 투표권을 더 가져요.", "Whoever did more work (proof of work) or staked more (proof of stake) gets more say.")),
        ("51% 공격", "51% attack", ("과반수를 장악하는 공격.", "Seizing the majority."), ("참여자가 적은 작은 마을일수록 과반수를 뺏기 쉬워요.", "Easier in a small, sparsely populated network to seize the majority.")),
        ("스마트 계약 취약점", "Smart-contract vulnerabilities", ("자동 실행 코드의 버그.", "A bug in self-running code."), ("한 번 배포되면 자동으로 실행돼서 멈추거나 되돌리기 어려워요.", "Once deployed, it runs automatically — hard to pause or reverse.")),
        ("개인키 분실", "Lost private key", ("잃어버리면 못 찾아줘요.", "Lose it, and no one can recover it for you."), ("비밀번호 재설정 같은 구제 수단이 없어요.", "There's no password-reset-style recovery.")),
        ("거래소·지갑 보안", "Exchange and wallet security", ("장부보다 약한 주변 시설.", "The surrounding buildings, weaker than the ledger."), ("실제 사고는 대부분 장부가 아니라 지갑·거래소에서 일어나요.", "Most real incidents happen in wallets and exchanges, not the ledger itself.")),
        ("불변성", "Immutability", ("한 번 적으면 못 지워요.", "Once written, it can't be erased."), ("장점이자 단점 — 버그가 섞여도 지울 수 없어요.", "Both a strength and a weakness — even a bug can't be erased.")),
    ],
}
