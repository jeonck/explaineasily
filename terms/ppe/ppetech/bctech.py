from _draw import *
from _world import *


def blockchain(x, y, n=4, s=1.0, broken_at=-1):
    """지문(해시)으로 이어진 블록 n개."""
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i in range(n):
        bx = i * 90
        fill = "var(--bad)" if i == broken_at else "var(--accent)"
        out += f'<rect x="{bx}" y="0" width="70" height="56" rx="6" fill="{fill}" opacity="0.85"/>'
        out += f'<circle cx="{bx+16}" cy="16" r="6" fill="#fff" opacity="0.8"/>'
        if i > 0:
            stroke = "var(--bad)" if (i == broken_at or i - 1 == broken_at) else "var(--line)"
            out += f'<path d="M{bx-20} 28 h20" stroke="{stroke}" stroke-width="3"/>'
    return out + '</g>'


def singleserver(x, y, s=1.0, cracked=False):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-30" width="48" height="60" rx="4" fill="#5A6B85"/><circle cy="-14" r="4" fill="#fff"/><circle cy="0" r="4" fill="#fff"/>'
    if cracked:
        out += '<path d="M-8 -26 l8 14 l-6 8 l10 14" stroke="var(--bad)" stroke-width="3" fill="none"/>'
    return out + '</g>'


# 1. 중앙 장부 한 곳만 고치면 믿을 수 없어요
P1 = svg(300, sky(300, ground=False)
         + singleserver(220, 160, 1.4, cracked=True)
         + person(380, 170, s=0.8, face=EYES, **DEMO)
         + bubble(440, 90, 250, 50, "⟦여기 한 곳만 몰래 고치면 아무도 몰라요|just quietly edit this one spot and nobody knows⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦중앙 장부는 서버 한 곳만 뚫리면 기록을 마음대로 바꿀 수 있어요|with a central ledger, one breached server lets anyone rewrite the records⟧", 13, "var(--bad)"))

# 2. 블록체인은 블록마다 지문을 물고 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + blockchain(110, 110, 4, 1.0)
         + label(380, 230, "⟦블록마다 이전 블록의 지문(해시)을 물고 있어요|each block holds the previous block's fingerprint (hash)⟧", 12, "var(--ink)")
         + label(380, 270, "⟦블록 하나를 고치면 뒤 블록들의 지문이 전부 어긋나요|change one block, and every fingerprint after it stops matching⟧", 12, "var(--ink)"))

# 3. 블록체인 = 지문으로 이어진 장부 (hero)
P3 = svg(340, sky(340, ground=False)
         + blockchain(110, 130, 4, 1.1, broken_at=1)
         + label(380, 30, "⟦블록체인 = 블록마다 지문을 물고 있어, 몰래 고치면 들통나는 장부|Blockchain = a ledger of blocks holding each other's fingerprints, so tampering shows⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦2번 블록을 고치자 3·4번 블록의 지문이 전부 안 맞아요|change block 2, and blocks 3 and 4's fingerprints no longer match⟧", 12, "var(--bad)")
         + label(380, 320, "⟦그래서 장부를 몰래 고치는 게 사실상 불가능해요|that's why quietly altering the ledger is practically impossible⟧", 12, "var(--muted)"))

BC_HASH = icon('<rect x="14" y="20" width="36" height="24" rx="4" fill="var(--accent)"/><circle cx="24" cy="32" r="4" fill="#fff"/><path d="M40 20 v24" stroke="#fff" stroke-width="3" stroke-dasharray="2 2"/>')
BC_CONSENSUS = icon('<circle cx="18" cy="18" r="8" fill="var(--accent)"/><circle cx="46" cy="18" r="8" fill="var(--accent)"/><circle cx="32" cy="46" r="8" fill="var(--accent)"/><path d="M18 18 L46 18 L32 46 Z" stroke="var(--good)" stroke-width="3" fill="none"/>')
BC_DIST = icon('<rect x="8" y="8" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="38" y="8" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="8" y="38" width="18" height="18" rx="3" fill="var(--accent)"/><rect x="38" y="38" width="18" height="18" rx="3" fill="var(--accent)"/>')
BC_CONTRACT = icon('<rect x="16" y="10" width="32" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 22 h16 M24 30 h16" stroke="#142033" stroke-width="2.5"/><path d="M26 40 l5 5 l9 -10" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 4. 보안 고려사항
P4 = svg(360, sky(360, ground=False)
         + infoboard(55, 30, 500, 230, "⟦블록체인 보안, 조심할 점|SECURITY, THINGS TO WATCH⟧",
                     ("⟦51% 공격 — 합의 힘의 과반을 잡으면 장부가 뚫려요|51% attack — seize most consensus power, rewrite the ledger⟧",
                      "⟦개인키 분실 — 자산을 되찾을 수 없어요|lost private key — the assets can't be recovered⟧",
                      "⟦스마트 컨트랙트 버그 — 자동 실행이라 되돌리기 어려워요|smart contract bugs — hard to undo once the code runs⟧",
                      "⟦프라이버시 — 공개 장부는 거래 기록이 다 보여요|privacy — a public ledger shows every transaction⟧"), 1.3)
         + label(380, 345, "⟦구조가 안전해도 개인키 관리와 코드 품질은 사람 몫이에요|even with a secure structure, key care and code quality are up to people⟧", 12, "var(--ink)"))

# 5. 한계: 느리고, 한 번 적으면 못 지워요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + blockchain(210, 130, 2, 0.9) + label(290, 230, "⟦장부 변조는 거의 불가능해요|tampering with the ledger is nearly impossible⟧", 11, "var(--ink)")
         + person(600, 125, s=0.8, face=FROWN, **VISITOR)
         + label(600, 240, "⟦대신 합의에 시간이 걸려 느리고 비용도 커요|but consensus takes time, so it's slow and costly⟧", 11, "var(--ink)")
         + label(380, 282, "⟦퍼블릭·프라이빗 어느 쪽이든, 변조 방지와 느린 속도는 정도만 다를 뿐 함께 와요|public or private, tamper resistance and slowness come together, only in different degrees⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "bctech", "order": 5,
    "title": ("지문으로 이어진 장부", "The Ledger Linked by Fingerprints"),
    "h1": ("<em>블록체인 기술요소·보안</em>이 뭐예요?", "What are <em>Blockchain Tech Components & Security</em>?"),
    "sub": ("블록체인의 속 구조를, 블록마다 이전 블록의 지문을 물고 있는 장부 이야기로 풀어봤어요.",
            "Blockchain's inner workings, told as a story about a ledger whose blocks each hold the previous block's fingerprint."),
    "panels": [
        {"svg": P1, "alt": ("시연 담당자가 중앙 서버 한 곳만 몰래 고치면 아무도 모른다고 말함", "A demonstrator says quietly editing just one central server goes unnoticed"),
         "caption": ("중앙 장부는 서버 한 곳만 뚫리면 기록을 마음대로 바꿀 수 있어요.", "With a central ledger, one breached server lets anyone rewrite the records."),
         "small": ("중앙 장부 한 곳만 고치면 아무도 몰라요.", "Quietly edit one central ledger, and nobody knows.")},
        {"svg": P2, "alt": ("네 개의 블록이 서로의 지문(해시)을 물고 이어짐", "Four blocks, each holding the previous one's fingerprint (hash)"),
         "caption": ("블록마다 이전 블록의 지문을 물고 있어요.", "Each block holds the previous block's fingerprint."),
         "small": ("블록 하나를 고치면 뒤 블록들의 지문이 전부 어긋나요.", "Change one block, and every fingerprint after it stops matching.")},
        {"svg": P3, "hero": True, "alt": ("두 번째 블록을 고치자 뒤 블록들의 지문이 전부 어긋남", "Editing the second block makes every later fingerprint mismatch"),
         "caption": ("블록체인은 블록마다 지문을 물고 있어, 몰래 고치면 들통나는 장부예요.", "Blockchain is a ledger of blocks holding each other's fingerprints, so tampering shows."),
         "small": ("그래서 장부를 몰래 고치는 게 사실상 불가능해요.", "That's why quietly altering the ledger is practically impossible."),
         "tricks": (4, [
             (BC_HASH, ("해시로 연결하기", "Link by hash"), ("블록마다 앞 블록의 지문을 물어요", "each block holds the previous fingerprint"), "calm"),
             (BC_CONSENSUS, ("합의로 추가하기", "Add by consensus"), ("다수가 동의해야 장부에 적어요", "writes to the ledger only if most agree")),
             (BC_DIST, ("분산 저장하기", "Store it distributed"), ("장부가 여러 컴퓨터에 복사돼요", "the ledger is copied to many computers")),
             (BC_CONTRACT, ("스마트 컨트랙트", "Smart contracts"), ("조건이 맞으면 코드가 자동 실행돼요", "code runs itself when conditions are met"), "warm"),
         ])},
        {"svg": P4, "alt": ("블록체인 보안 체크리스트: 51% 공격, 개인키 분실, 스마트 컨트랙트 버그, 프라이버시", "A security checklist: 51% attacks, lost private keys, smart contract bugs, privacy"),
         "caption": ("블록체인 구조가 안전해도, 사람이 조심할 점은 따로 있어요.", "Even with blockchain's secure structure, people still have separate things to watch."),
         "small": ("개인키 관리와 코드 품질은 사람 몫이에요.", "Private-key care and code quality are up to people.")},
        {"svg": P5, "alt": ("왼쪽: 변조가 거의 불가능함. 오른쪽: 관람객이 느리고 비용이 크다고 말함", "Left: tampering is nearly impossible. Right: a visitor notes it's slow and costly"),
         "caption": ("블록체인은 변조를 막는 대신, 합의에 시간이 걸려 느리고 비용도 커요.", "Blockchain prevents tampering at a price: consensus takes time, so it's slow and costly."),
         "small": ("장부에 한 번 적으면 못 지운다는 건, 변조를 막는 장점이자 실수도 못 고치는 단점이에요.", "A ledger entry can't be erased: that stops tampering, but mistakes can't be fixed either.")},
    ],
    "summary": (("<b>블록체인</b>은 블록마다 이전 블록의 <b>지문(해시)을 물고 있어</b>, 하나라도 몰래 고치면 뒤가 전부 어긋나 <b>들통나는 장부</b> 구조예요.",
                 "<b>Blockchain</b> is a ledger where each block holds the previous block's <b>fingerprint (hash)</b>, so tampering with any one block breaks every link after it — making it a <b>ledger where tampering shows</b>."),
                ("블록체인의 핵심 기술요소는 해시 체인, 합의 알고리즘(작업증명·지분증명 등), 분산 저장, 스마트 컨트랙트예요. 변조에 강하지만 51% 공격, 개인키 분실 시 복구 불가, 스마트 컨트랙트 코드 버그, 공개형의 프라이버시 노출은 별도로 관리해야 할 보안 고려사항이에요. 퍼블릭·프라이빗 구분은 블록체인 비교 페이지에서 다뤄요.",
                 "Blockchain's core technical components are the hash chain, consensus algorithms (proof-of-work, proof-of-stake, etc.), distributed storage, and smart contracts. It resists tampering well, but 51% attacks, unrecoverable lost private keys, smart contract code bugs, and privacy exposure on public chains are security considerations that still need separate management. Public vs private is covered in the comparison page.")),
    "glossary": [
        ("해시", "Hash", ("블록 하나하나의 고유한 지문.", "Each block's own unique fingerprint."), ("블록 내용이 조금만 바뀌어도 지문이 바뀌어요.", "Change anything in the block, and the fingerprint changes too.")),
        ("합의 알고리즘", "Consensus Algorithm", ("다수가 동의해야 장부에 적는 규칙.", "The rule requiring agreement before writing to the ledger."), ("블록체인이 느린 이유이자 안전한 이유예요.", "The reason blockchain is both slow and secure.")),
        ("스마트 컨트랙트", "Smart Contract", ("조건이 맞으면 자동 실행되는 약속.", "A promise that runs itself once conditions are met."), ("코드 버그는 되돌리기 어려워요.", "A code bug is hard to undo once it runs.")),
        ("51% 공격", "51% Attack", ("합의 힘의 과반을 장악해 장부를 고치는 공격.", "An attack that seizes over half the consensus power to rewrite the ledger."), ("참여자가 적은 블록체인일수록 더 위험해요.", "Chains with fewer participants are at greater risk.")),
        ("개인키", "Private Key", ("잃어버리면 아무도 되찾아줄 수 없는 열쇠.", "The key nobody can recover for you if lost."), ("분실하면 자산도 함께 잃어요.", "Lose it, and the assets go with it.")),
        ("퍼블릭·프라이빗 블록체인", "Public/Private Blockchain", ("누가 참여하느냐에 따른 두 형태.", "Two forms, split by who may join."), ('이 보안 요소는 두 형태 모두에 적용돼요. → <a href="bcpublicprivate-ko.html">퍼블릭·프라이빗 비교 부스</a>', 'These security points apply to both forms. → <a href="bcpublicprivate-en.html">the Public vs Private booth</a>')),
        ("분산 원장", "Distributed Ledger", ("여러 군데에 똑같이 복사된 장부.", "The same ledger, copied identically in many places."), ("한 곳이 사라져도 기록은 남아요.", "The record survives even if one copy disappears.")),
        ("디지털 트윈", "Digital Twin", ("실제 기계를 화면에 옮겨 먼저 실험해보는 쌍둥이.", "An on-screen twin of a real machine, used to test things first."), ('같은 과학관의 다른 전시예요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "A different exhibit in the same expo hall. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
    ],
}
