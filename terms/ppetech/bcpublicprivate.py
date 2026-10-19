from _draw import *
from _world import *


def ledger(x, y, s=1.0, open_book=True):
    """장부. open_book=True 면 누구나 보는 펼친 책, False 면 자물쇠 달린 닫힌 책."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    if open_book:
        out += ('<path d="M-40 -10 h36 v50 h-36z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
                '<path d="M4 -10 h36 v50 h-36z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
                '<path d="M-30 2 h20 M-30 12 h20 M8 2 h20 M8 12 h20" stroke="#142033" stroke-width="2"/>')
    else:
        out += ('<rect x="-30" y="-10" width="60" height="50" rx="4" fill="#4A5A72"/>'
                '<rect x="-12" y="4" width="24" height="18" rx="3" fill="var(--night)"/>'
                '<path d="M-6 4 v-8 a6 6 0 0 1 12 0 v8" stroke="var(--night)" stroke-width="4" fill="none"/>')
    return out + '</g>'


def peoplerow(x, y, n, s=0.55, **colors):
    return "".join(person(x + i * 46, y, s=s, face=EYES, **colors) for i in range(n))


# 1. 모든 블록체인이 다 같다고 생각해서 헷갈려요
P1 = svg(300, sky(300, ground=False)
         + ribbon(130, 50, 1.0, "⟦블록체인 비교 부스|Public vs Private Blockchain Booth⟧")
         + person(300, 180, s=0.85, face=EYES, **VISITOR)
         + bubble(360, 100, 260, 50, "⟦블록체인은 다 똑같은 거 아니에요?|Isn't blockchain all just... the same thing?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사실 누가 참여하느냐에 따라 완전히 달라요|actually, who's allowed to join changes everything⟧", 13, "var(--ink)"))

# 2. 공개 여부에 따라 쓰임새가 완전히 달라요
P2 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + ledger(190, 140, 1.3, open_book=True) + peoplerow(100, 230, 4, **VISITOR)
         + label(190, 265, "⟦누구나 참여 가능|anyone can join⟧", 12, "var(--ink)")
         + ledger(570, 140, 1.3, open_book=False) + person(530, 225, s=0.6, face=EYES, **GUIDE) + person(610, 225, s=0.6, face=EYES, **DEMO)
         + label(570, 265, "⟦허가받은 사람만|only approved members⟧", 12, "var(--ink)")
         + label(380, 40, "⟦둘은 완전히 다른 쓰임새를 가져요|the two serve completely different purposes⟧", 13, "var(--ink)"))

# 3. 퍼블릭 vs 프라이빗 (hero)
P3 = svg(340, sky(340, ground=False)
         + ledger(220, 150, 1.6, open_book=True) + label(220, 260, "⟦퍼블릭|PUBLIC⟧", 14, "var(--ink)", cls="d")
         + ledger(540, 150, 1.6, open_book=False) + label(540, 260, "⟦프라이빗|PRIVATE⟧", 14, "var(--ink)", cls="d")
         + label(380, 30, "⟦퍼블릭 = 누구나 보고 검증하는 공개 장부, 프라이빗 = 허가된 사람만 쓰는 장부|Public = an open ledger anyone can see and verify, Private = a ledger only approved members use⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦둘 다 블록체인이지만, 참여 자격부터 달라요|both are blockchains, but who may join is different from the start⟧", 12, "var(--muted)"))

BC_WHO = icon('<circle cx="22" cy="24" r="9" fill="var(--accent)"/><circle cx="42" cy="24" r="9" fill="var(--accent)"/><path d="M10 50 q12 -16 24 0 M30 50 q12 -16 24 0" stroke="var(--accent)" stroke-width="3" fill="none"/>')
BC_SPEED = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l8 4" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
BC_OPEN = icon('<rect x="14" y="20" width="36" height="28" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="32" cy="34" r="6" fill="none" stroke="var(--ink)" stroke-width="2"/>')
BC_USE = icon('<rect x="16" y="16" width="32" height="32" rx="4" fill="var(--accent)"/><path d="M24 32 h16 M32 24 v16" stroke="#fff" stroke-width="3"/>')

# 4. 비교표
P4 = svg(360, sky(360, ground=False)
         + infoboard(60, 30, 300, 290, "⟦퍼블릭|PUBLIC⟧",
                     ("⟦참여 — 누구나|anyone may join⟧", "⟦속도 — 느려요|slower⟧",
                      "⟦투명성 — 전부 공개|fully transparent⟧", "⟦예시 — 비트코인|e.g. Bitcoin⟧"), 1.3)
         + infoboard(400, 30, 300, 290, "⟦프라이빗|PRIVATE⟧",
                     ("⟦참여 — 허가받은 사람만|only approved members⟧", "⟦속도 — 빨라요|faster⟧",
                      "⟦투명성 — 제한적 공개|limited visibility⟧", "⟦예시 — 기업 간 공급망|e.g. enterprise supply chain⟧"), 1.3)
         + label(380, 345, "⟦참여 자격이 속도와 투명성까지 결정해요|who may join decides speed and transparency too⟧", 12, "var(--ink)"))

# 5. 둘 다 극단, 실제론 섞인 형태도 많아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + ledger(190, 150, 1.2, open_book=True) + ledger(230, 150, 1.0, open_book=False)
         + label(210, 240, "⟦컨소시엄형 — 일부만 섞은 절충안|consortium type — a mix of the two⟧", 11, "var(--ink)")
         + person(570, 150, s=0.85, face=EYES, **GUIDE)
         + label(570, 240, "⟦보안 요소는 다음 부스에서 더 자세히 봐요|the security side gets its own booth next⟧", 11, "var(--ink)")
         + label(380, 282, "⟦완전 공개도 완전 비공개도 한쪽 끝일 뿐이에요|fully open and fully closed are just two ends of the spectrum⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "bcpublicprivate", "order": 4,
    "title": ("펼친 장부와 자물쇠 장부", "The Open Ledger and the Locked Ledger"),
    "h1": ("<em>퍼블릭·프라이빗 블록체인</em>이 뭐가 달라요?", "What's the Difference Between <em>Public and Private Blockchain</em>?"),
    "sub": ("퍼블릭·프라이빗 블록체인을, 누구나 보는 펼친 장부와 허가된 사람만 보는 자물쇠 장부로 비교해봤어요.",
            "Public vs private blockchain, told as a story comparing an open ledger anyone can read with a locked ledger only approved members use."),
    "panels": [
        {"svg": P1, "alt": ("관람객이 블록체인이 다 같은 게 아니냐고 질문함", "A visitor asks whether all blockchains are the same thing"),
         "caption": ("블록체인은 다 똑같은 거 아니에요?", "Isn't blockchain all just the same thing?"),
         "small": ("사실 누가 참여하느냐에 따라 완전히 달라요.", "Actually, who's allowed to join changes everything.")},
        {"svg": P2, "alt": ("왼쪽: 펼친 장부와 누구나 모인 관람객들. 오른쪽: 자물쇠 달린 장부와 허가된 소수", "Left: an open ledger with a crowd of visitors. Right: a locked ledger with only a few approved members"),
         "caption": ("공개 여부에 따라 쓰임새가 완전히 달라요.", "The two serve completely different purposes."),
         "small": ("참여 자격이 전체 그림을 바꿔요.", "Who may join changes the whole picture.")},
        {"svg": P3, "hero": True, "alt": ("펼친 장부(퍼블릭)와 자물쇠 장부(프라이빗)가 나란히 놓임", "An open ledger (public) and a locked ledger (private) side by side"),
         "caption": ("퍼블릭은 누구나 보고 검증하는 공개 장부, 프라이빗은 허가된 사람만 쓰는 장부예요.", "Public is an open ledger anyone can see and verify; private is a ledger only approved members use."),
         "small": ("둘 다 블록체인이지만, 참여 자격부터 달라요.", "Both are blockchains, but who may join is different from the start."),
         "tricks": (4, [
             (BC_WHO, ("참여 자격", "Who may join"), ("누구나 vs 허가받은 사람", "anyone vs approved members"), "calm"),
             (BC_SPEED, ("처리 속도", "Processing speed"), ("느림 vs 빠름", "slower vs faster")),
             (BC_OPEN, ("투명성", "Transparency"), ("전부 공개 vs 제한 공개", "fully open vs limited")),
             (BC_USE, ("대표 쓰임새", "Typical use"), ("암호화폐 vs 기업 거래", "cryptocurrency vs enterprise deals"), "warm"),
         ])},
        {"svg": P4, "alt": ("퍼블릭과 프라이빗을 참여·속도·투명성·예시로 비교하는 두 설명판", "Two boards comparing public and private on participation, speed, transparency, and examples"),
         "caption": ("참여 자격이 속도와 투명성까지 결정해요.", "Who may join decides speed and transparency too."),
         "small": ("퍼블릭은 비트코인처럼, 프라이빗은 기업 간 공급망처럼 쓰여요.", "Public looks like Bitcoin; private looks like an enterprise supply chain.")},
        {"svg": P5, "alt": ("왼쪽: 펼친 장부와 자물쇠 장부가 섞인 컨소시엄형. 오른쪽: 보안은 다음 부스에서", "Left: a consortium type mixing open and locked ledgers. Right: security gets covered at the next booth"),
         "caption": ("완전 공개도 완전 비공개도 한쪽 끝일 뿐이에요.", "Fully open and fully closed are just two ends of the spectrum."),
         "small": ("실제로는 컨소시엄형처럼 섞은 형태도 많아요.", "Many real systems mix the two, like a consortium type.")},
    ],
    "summary": (("<b>퍼블릭 블록체인</b>은 누구나 참여·검증하는 공개 장부이고, <b>프라이빗 블록체인</b>은 허가받은 사람만 쓰는 장부예요. 그 사이에 컨소시엄형도 있어요.",
                 "A <b>public blockchain</b> is an open ledger anyone can join and verify; a <b>private blockchain</b> is one only approved members use. Consortium types sit in between."),
                ("퍼블릭 블록체인은 참여자 제한이 없는 탈중앙형 네트워크로 투명성이 높지만 합의 과정이 느리고, 프라이빗 블록체인은 허가된 참여자만으로 구성돼 속도는 빠르지만 중앙화 정도가 높아요. 컨소시엄형은 복수의 허가된 기관이 함께 운영하는 중간 형태예요. 기술 구성요소와 보안 고려사항은 블록체인 기술요소·보안 페이지에서 더 다뤄요.",
                 "A public blockchain is a permissionless, decentralized network — highly transparent but with slower consensus. A private blockchain is made up of only approved participants — faster, but more centralized. Consortium blockchains sit in between, run jointly by multiple approved organizations. Technical components and security considerations are covered in the blockchain tech & security page.")),
    "glossary": [
        ("퍼블릭 블록체인", "Public Blockchain", ("누구나 참여하는 공개 장부.", "An open ledger anyone can join."), ("탈중앙성과 투명성이 강점이에요.", "Its strength is decentralization and transparency.")),
        ("프라이빗 블록체인", "Private Blockchain", ("허가받은 사람만 쓰는 장부.", "A ledger only approved members use."), ("속도와 통제가 강점이에요.", "Its strength is speed and control.")),
        ("컨소시엄 블록체인", "Consortium Blockchain", ("여러 기관이 함께 운영하는 절충안.", "A middle ground run jointly by several organizations."), ("퍼블릭·프라이빗의 중간이에요.", "Sits between public and private.")),
        ("블록체인 기술요소·보안", "Blockchain Tech & Security", ("해시·합의·분산저장 같은 속 구조.", "The inner workings — hashing, consensus, distributed storage."), ('두 종류 모두가 공유하는 기술 뼈대예요. → <a href="bctech-ko.html">블록체인 기술요소·보안 부스</a>', 'The technical skeleton both types share. → <a href="bctech-en.html">the Blockchain Tech & Security booth</a>')),
        ("합의 알고리즘", "Consensus Algorithm", ("다수가 동의해야 장부에 적는 규칙.", "The rule requiring agreement before writing to the ledger."), ("퍼블릭일수록 느려지는 주된 이유예요.", "The main reason public chains are slower.")),
        ("탈중앙화", "Decentralization", ("한 곳이 아니라 여럿이 나눠 가진 힘.", "Power spread across many, not held by one."), ("퍼블릭이 프라이빗보다 훨씬 높아요.", "Much higher in public than in private.")),
        ("스마트 컨트랙트", "Smart Contract", ("조건을 걸어두면 자동 실행되는 약속.", "A promise that runs itself once conditions are met."), ("퍼블릭·프라이빗 둘 다에서 쓰여요.", "Used in both public and private chains.")),
        ("디지털 트윈", "Digital Twin", ("화면 속에서 먼저 실험해보는 쌍둥이.", "The twin you test things on first, on screen."), ('같은 과학관의 다른 전시 방식이에요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "A different kind of exhibit in the same expo hall. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
    ],
}
