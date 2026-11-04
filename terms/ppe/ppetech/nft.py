from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


PAINT_P = '<rect x="10" y="10" width="44" height="34" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="26" cy="26" r="7" fill="var(--accent)"/><path d="M14 38 L28 24 L38 32 L50 18" stroke="var(--good)" stroke-width="3" fill="none"/>'
STAMP_P = '<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3"/><circle cx="32" cy="32" r="14" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M26 32 l4 5 l9 -10" stroke="var(--accent)" stroke-width="3" fill="none"/>'
CHAIN_P = ''.join(f'<circle cx="{14+i*12}" cy="32" r="7" fill="none" stroke="var(--good)" stroke-width="4"/>' for i in range(5))
COPY_P = '<rect x="8" y="14" width="30" height="36" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="24" y="22" width="30" height="36" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
PAINT_I, STAMP_I, CHAIN_I, COPY_I = icon(PAINT_P), icon(STAMP_P), icon(CHAIN_P), icon(COPY_P)


def canvas(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="90" height="70" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="4"/><circle cx="30" cy="30" r="10" fill="var(--accent)"/><path d="M14 56 L34 30 L50 44 L76 16" stroke="var(--good)" stroke-width="4" fill="none"/></g>'


# 1. 디지털 그림 부스 — 누구나 복사할 수 있어요
P1 = svg(300, sky(300)
         + canvas(330, 90, 1.4)
         + person(180, 160, s=0.8, face=EYES, **VISITOR)
         + label(380, 250, "⟦이 그림, 저장하면 저도 똑같이 가질 수 있는데요?|if I just save this, don't I have the exact same picture?⟧", 12, "var(--bad)")
         + label(380, 280, "⟦디지털 그림은 복사해도 원본과 한 치도 다르지 않아요|a digital picture, copied, is pixel-for-pixel identical to the original⟧", 12, "var(--ink)"))

# 2. 그럼 '진짜 원본'은 누가 가진 건지 알 수 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + glyph(260, 90, 0.9, COPY_P) + glyph(420, 90, 0.9, COPY_P)
         + person(560, 150, s=0.8, face=FROWN, **DEMO)
         + label(380, 275, "⟦그림이 열 장 복사돼도, 어느 게 '진짜'인지 구별이 안 돼요|even with ten copies, there's no way to tell which one is 'the real one'⟧", 12, "var(--ink)"))

# 3. NFT = 그림에 붙이는, 위조 못 하는 일련번호 증명서 (hero)
P3 = svg(340, sky(340)
         + canvas(310, 90, 1.4)
         + glyph(430, 130, 1.1, STAMP_P)
         + person(670, 220, s=0.8, face=SMILE, **VISITOR)
         + label(380, 30, "⟦NFT = 그림은 그대로 두고, 그 그림에 '이건 진짜예요'라는 증명서만 따로 붙이는 것|NFT = leaving the picture as-is, but attaching a separate 'this one is the real one' certificate⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦증명서는 모두가 함께 적는 장부(블록체인)에 기록돼, 몰래 고칠 수 없어요|the certificate goes into a shared ledger (blockchain) everyone keeps, so it can't be quietly altered⟧", 12, "var(--muted)"))

# 4. 증명서에는 무엇이 적히나요
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦증명서에 적히는 것|WHAT THE CERTIFICATE RECORDS⟧",
                     ("⟦이 작품의 고유 번호|this work's unique ID⟧",
                      "⟦지금 누가 갖고 있는지|who currently holds it⟧",
                      "⟦누구 손을 거쳐 왔는지(거래 기록)|whose hands it passed through (history)⟧",
                      "⟦증명서는 작품 자체가 아니에요|the certificate is not the artwork itself⟧"), 1.0, hl=3)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦그림 파일은 여전히 누구나 볼 수 있고 복사할 수 있어요|the image file itself can still be viewed and copied by anyone⟧", 11, "var(--muted)"))

# 5. 한계 - 증명서만 유일할 뿐, 그림 자체는 막을 수 없어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 110, 1.3, STAMP_P)
         + label(190, 250, "⟦증명서 주인이 누구인지는 장부 기록으로 확실히 증명돼요|the ledger proves, for certain, who holds the certificate⟧", 11, "var(--ink)")
         + canvas(550, 110, 1.0) + glyph(560, 170, 0.6, COPY_P)
         + label(570, 262, "⟦그림 자체는 여전히 누구나 내려받고 복사할 수 있어요|the picture itself can still be downloaded and copied by anyone⟧", 11, "var(--ink)")
         + label(380, 282, "⟦NFT는 '이 번호의 주인' 기록이지, 복제를 막는 자물쇠가 아니에요|an NFT records who holds this token, not a lock against copying⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "nft", "order": 19,
    "title": ("그림에 붙이는 몰래 못 고치는 증명서", "The Certificate Nobody Can Quietly Alter, Stuck to the Picture"),
    "h1": ("<em>NFT</em>가 뭐예요?", "What is <em>NFT</em>?"),
    "sub": ("NFT를, 복사되는 디지털 그림에 '이게 진짜예요'라고 붙이는 증명서 이야기로 풀어봤어요.",
            "NFTs, told as a story about a certificate stuck onto a copyable digital picture, saying 'this one is the real one.'"),
    "panels": [
        {"svg": P1, "alt": ("관람객이 디지털 그림을 보며 저장하면 똑같이 가질 수 있는지 물음", "A visitor looks at a digital picture and asks if saving it gives them an identical copy"),
         "caption": ("이 그림, 저장하면 저도 똑같이 가질 수 있는데요?", "If I just save this, don't I have the exact same picture?"),
         "small": ("디지털 그림은 복사해도 원본과 한 치도 다르지 않아요.", "A digital picture, copied, is pixel-for-pixel identical to the original.")},
        {"svg": P2, "alt": ("그림이 여러 장 복사되어 있고, 시연 담당자가 어느 게 진짜인지 몰라 곤란해함", "The picture is copied several times, and a demo staffer can't tell which is the real one"),
         "caption": ("그럼 '진짜 원본'은 누가 가진 건지 알 수 없어요.", "Then there's no telling who holds the 'real original.'"),
         "small": ("그림이 열 장 복사돼도, 어느 게 '진짜'인지 구별이 안 돼요.", "Even with ten copies, there's no way to tell which one is 'the real one.'")},
        {"svg": P3, "hero": True, "alt": ("그림 옆에 위조 방지 도장이 찍힌 증명서가 붙고, 관람객이 흐뭇해함", "A tamper-proof certificate is stamped beside the picture while a visitor looks pleased"),
         "caption": ("NFT는 그림은 그대로 두고 '이건 진짜예요'라는 증명서만 따로 붙이는 거예요.", "An NFT leaves the picture as-is, but attaches a separate 'this one is real' certificate."),
         "small": ("증명서는 모두가 함께 적는 장부(블록체인)에 기록돼, 몰래 고칠 수 없어요.", "The certificate is written into a shared ledger (blockchain) everyone keeps, so it can't be quietly altered."),
         "tricks": (4, [
             (PAINT_I, ("원본은 그대로", "The artwork stays as-is"), ("그림 자체는 안 바뀌어요", "the picture itself doesn't change")),
             (STAMP_I, ("증명서 붙이기", "Attach a certificate"), ("고유 번호를 하나 붙여요", "attaches one unique ID"), "calm"),
             (CHAIN_I, ("모두의 장부에 기록", "Record on a shared ledger"), ("다 같이 적어서 기록을 몰래 못 고쳐요", "everyone keeps the record, so it can't be quietly altered")),
             (COPY_I, ("그래도 복사는 돼요", "Still copyable"), ("그림 파일 복사 자체는 못 막아요", "it can't stop the image file from being copied"), "warm"),
         ])},
        {"svg": P4, "alt": ("증명서 설명판: 고유 번호, 현재 소유자, 거래 기록, 작품 자체는 아님", "A board lists what the certificate records: unique ID, current owner, history, and that it is not the artwork itself"),
         "caption": ("증명서에는 번호와 소유자, 거래 기록이 적혀요.", "The certificate records an ID, the owner, and the trade history."),
         "small": ("그림 파일은 여전히 누구나 볼 수 있고 복사할 수 있어요.", "The image file itself can still be viewed and copied by anyone.")},
        {"svg": P5, "alt": ("왼쪽: 증명서가 소유자를 확실히 보여줌. 오른쪽: 그림은 여전히 복사됨", "Left: the certificate clearly shows the owner. Right: the picture is still copied"),
         "caption": ("증명서만 유일할 뿐, 그림 복사 자체는 막을 수 없어요.", "Only the certificate is unique — it can't stop the picture from being copied."),
         "small": ("NFT는 '이 번호의 주인' 기록이지, 복제를 막는 자물쇠가 아니에요. 저작권까지 넘어오는 것도 아니에요.", "An NFT records who holds this token; it isn't a lock against copying, and it doesn't transfer copyright by itself.")},
    ],
    "summary": (("<b>NFT</b> = 디지털 작품에 <b>고유 번호(토큰)</b>를 붙여, <b>누가 그 토큰을 가졌는지</b>만 증명하는 기술.",
                 "<b>NFT</b> = a technology that attaches a <b>unique ID (a token)</b> to a digital work, proving only <b>who holds that token</b>."),
                ("NFT(Non-Fungible Token)는 디지털 자산과 연결된 고유 토큰으로, 누가 가졌는지와 거래 이력이 블록체인에 기록돼요. 자산 파일 자체를 암호화하거나 복제를 막는 것이 아니라, 누가 이 토큰을 가졌는지만 증명해요. 그림 파일은 보통 블록체인 밖에 있고 토큰엔 그 주소만 적혀요. 토큰을 샀다고 저작권이 따라오지 않고, 다른 사람이 같은 그림으로 또 다른 NFT를 만드는 것도 기술만으로는 못 막아요.",
                 "An NFT (Non-Fungible Token) is a unique token linked to a digital asset, with its holder and transaction history recorded on a blockchain. It doesn't encrypt the asset file or prevent copying — it only proves who holds the token. The image file usually sits off-chain, with only its address in the token. Buying a token doesn't bring the copyright with it, and technology alone can't stop someone from minting another NFT of the same picture.")),
    "glossary": [
        ("NFT", "NFT", ("그림에 붙는 몰래 못 고치는 증명서.", "The certificate nobody can quietly alter, stuck to a picture."), ("그림 자체가 아니라 '이 토큰의 주인'을 증명해요.", "It proves who holds this token, not the artwork itself.")),
        ("블록체인", "Blockchain", ("모두가 함께 적는 장부.", "The ledger everyone keeps together."), ("증명서가 적히는 바로 그 장부예요.", "The very ledger the certificate is written into.")),
        ("대체 불가능", "Non-Fungible", ("세상에 하나뿐이라는 뜻.", "Meaning there's only one in the whole world."), ("일련번호가 있어 다른 토큰과 안 바뀌어요.", "Its serial number means it can't be swapped for another token.")),
        ("가상자산", "Virtual Asset", ("디지털로만 존재하는 재산.", "Property that exists only digitally."), ("한국 금융당국은 수집용 NFT는 원칙적으로 가상자산에서 빼지만, 대량 발행되거나 지급수단처럼 쓰이면 가상자산으로 볼 수 있다고 해요.", "Korean regulators generally exclude collectible NFTs from virtual assets, but ones issued in bulk or used like payment can count as virtual assets.")),
        ("디지털 저작권", "Digital Copyright", ("원본을 베끼지 못하게 막는 권리.", "The right that's meant to stop copying."), ("NFT는 이 권리를 대신해주지 않아요.", "An NFT doesn't substitute for this right.")),
        ("핀테크", "Fintech", ("금융에 IT를 더한 서비스.", "Financial services combined with IT."), ('NFT 거래에도 이런 결제 기술이 쓰이기도 해요. → <a href="fintech-ko.html">핀테크·간편결제</a>', 'NFT trades can use this same kind of payment tech too. → <a href="fintech-en.html">Fintech & simple payment</a>')),
        ("정량적 위험분석", "Quantitative Risk Analysis", ("가치 변동 위험을 숫자로 재는 방법.", "A way to score value swings with numbers."), ('NFT 가격의 급등락 위험도 이렇게 가늠해요. → <a href="quantrisk-ko.html">정량적 위험분석 기법</a>', "An NFT's wild price swings get sized up the same way. → <a href=\"quantrisk-en.html\">Quantitative Risk Analysis</a>")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
