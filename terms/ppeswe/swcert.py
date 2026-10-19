from _draw import *
from _world import *

# 이 페이지 전용 인물/소품 (분야 공용 _world.py 는 건드리지 않음)
CERTIFIER = dict(hat="#5C5C5C", shirt="#5C5C5C")   # 인증기관 심사관 (출판사 바깥 사람)
RIVAL = dict(hat="#C0392B", shirt="#8B2E2E")        # 다른 출판사 (이 페이지 한정 일회성 등장)


def seal(x, y, s=1.0, color="var(--good)"):
    """인증 마크(둥근 도장 + 리본)."""
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="34" fill="{color}"/>'
            f'<circle r="34" fill="none" stroke="#FFF8E7" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M-14 0 l9 9 l19 -20" stroke="#FFF8E7" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<path d="M-10 30 l-14 24 l16 -4 l8 14 l12 -26z" fill="{color}"/>'
            f'<path d="M10 30 l14 24 l-16 -4 l-8 14 l-12 -26z" fill="{color}"/></g>')


# 1. 출판사마다 자기 책이 최고라고 우겨요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SMILE, **EDITOR) + bubble(40, 40, 190, 40, "⟦저희 책이 최고예요!|Ours is the best book!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(420, 150, s=0.8, face=SMILE, **RIVAL) + bubble(330, 40, 190, 40, "⟦아뇨, 저희가 최고예요!|No, ours is the best!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(630, 180, s=0.7, face=FROWN, **READER)
         + label(630, 280, "⟦뭘 믿고 사야 하죠?|Which one should I believe?⟧", 12, "var(--bad)")
         + label(380, 25, "⟦출판사마다 자기 책이 최고라고 말해요|Every publisher claims its own book is the best⟧", 13, "var(--ink)"))

# 2. 각자 말만으론 비교할 방법이 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(200, 140, 0.8) + manuscript(380, 140, 0.8) + manuscript(560, 140, 0.8)
         + label(380, 230, "⟦원고마다 자기 기준으로만 말하니 비교가 안 돼요|each one only speaks to its own standard — nothing lines up⟧", 12, "var(--ink)")
         + label(380, 270, "⟦확인해 줄 바깥 눈이 필요해요|we need an outside eye to check⟧", 12, "var(--muted)"))

# 3. 품질인증 = 바깥 기관이 공통 기준으로 검사해 마크를 줌 (hero)
P3 = svg(340, sky(340)
         + person(360, 110, s=0.9, face=EYES, **CERTIFIER) + seal(470, 90, 0.6)
         + printplate(300, 220, 0.9, "⟦시험용 표본|sample copy⟧")
         + label(380, 30, "⟦품질인증 = 바깥 기관이 공통 기준으로 검사해 주는 공식 마크예요|Quality certification = an outside body checks it against one shared standard⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦내가 좋다고 말하는 게 아니라, 밖에서 확인해 줘요|Not self-proclaimed — it's confirmed from the outside⟧", 12, "var(--muted)"))

STANDARD_I = icon('<rect x="10" y="8" width="44" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 20 h24 M20 28 h24 M20 36 h16" stroke="#142033" stroke-width="2.5"/><path d="M24 46 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SAMPLE_I = icon('<rect x="14" y="16" width="36" height="28" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="30" cy="30" r="8" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M37 37 l9 9" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
VALID_I = icon('<circle cx="32" cy="26" r="18" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 14 v12 l8 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M16 52 h32" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/>')
TRUST_I = icon('<path d="M32 8 L54 18 V32 C54 46 44 54 32 58 C20 54 10 46 10 32 V18 Z" fill="var(--good)"/><path d="M24 32 l6 6 l12 -14" stroke="#FFF8E7" stroke-width="4" fill="none" stroke-linecap="round"/>')

# 4. 심사표
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 230, "⟦품질 심사표|QUALITY CHECKLIST⟧",
                      ("⟦기능 적합성 — 할 일을 다 하나|functionality — does it do the job?⟧",
                       "⟦신뢰성 — 자주 안 망가지나|reliability — does it hold up?⟧",
                       "⟦사용성 — 쓰기 편한가|usability — is it easy to use?⟧",
                       "⟦보안성 — 함부로 안 새나|security — nothing leaks?⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **CERTIFIER)
         + label(560, 250, "⟦이 네 가지를 똑같은 기준으로 봐요|the same four items, checked the same way every time⟧", 11, "var(--muted)")
         + label(380, 300, "⟦사용성만 깊게 보는 시험도 따로 있어요|there's a whole separate test just for usability⟧", 12, "var(--ink)"))

# 5. 마크가 있어도 완벽을 뜻하진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + seal(190, 140, 0.7) + label(190, 240, "⟦완벽을 보장하진 않아요|doesn't guarantee perfection⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **READER) + label(570, 240, "⟦그래도 최소 기준은 확인됐어요|but a minimum standard is confirmed⟧", 11, "var(--ink)")
         + label(380, 282, "⟦인증은 '이 기준은 통과했다'는 뜻이지, 모든 문제가 없다는 뜻은 아니에요|certification means the standard was met — not that every problem is gone⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "swcert", "order": 42,
    "title": ("책 표지의 공식 마크", "The Official Mark on the Cover"),
    "h1": ("<em>SW 품질인증</em>이 뭐예요?", "What is <em>Software Quality Certification</em>?"),
    "sub": ("SW 품질인증을, 바깥 기관이 공통 기준으로 책을 검사해 마크를 붙여주는 이야기로 풀어봤어요.",
            "Software quality certification, told as a story about an outside body checking a book against a shared standard and awarding it a mark."),
    "panels": [
        {"svg": P1, "alt": ("두 출판사가 서로 자기 책이 최고라고 우기고, 독자는 헷갈려함", "Two publishers each insist their own book is best, and a reader looks confused"),
         "caption": ("출판사마다 자기 책이 최고라고 말해요.", "Every publisher claims its own book is the best."),
         "small": ("뭘 믿고 사야 하는지 아무도 몰라요.", "Nobody knows which claim to trust.")},
        {"svg": P2, "alt": ("원고 세 뭉치가 각자 다른 기준을 내세우고 있음", "Three manuscripts, each pointing to its own standard"),
         "caption": ("각자 말만으론 비교가 안 돼요.", "Self-declared claims alone can't be compared."),
         "small": ("확인해 줄 바깥 눈이 필요해요.", "An outside eye is needed to check.")},
        {"svg": P3, "hero": True, "alt": ("심사관이 표본 한 부를 검사하고 인증 마크를 준비함", "An examiner inspects a sample copy and prepares a certification seal"),
         "caption": ("품질인증은 바깥 기관이 공통 기준으로 검사해 마크를 주는 거예요.", "Quality certification is an outside body checking against one shared standard, then awarding a mark."),
         "small": ("내가 좋다고 말하는 게 아니라, 밖에서 확인해 줘요.", "Not self-proclaimed — it's confirmed from the outside."),
         "tricks": (4, [
             (STANDARD_I, ("고정된 공통 기준", "A fixed, shared standard"), ("누구 책이든 같은 표로 봐요", "the same checklist for every book"), "calm"),
             (SAMPLE_I, ("표본만 시험", "Tests a sample"), ("책 한 부를 떼어 확인해요", "pulls one copy to check")),
             (VALID_I, ("유효기간이 있어요", "Comes with an expiry date"), ("몇 년 뒤엔 다시 받아야 해요", "needs renewing after a few years"), "warm"),
             (TRUST_I, ("다른 서점도 믿어줘요", "Other bookstores trust it too"), ("매번 다시 확인할 필요가 없어요", "no need to re-check it each time")),
         ])},
        {"svg": P4, "alt": ("품질 심사표: 기능 적합성·신뢰성·사용성·보안성 네 항목을 심사관이 확인함", "A quality checklist: functionality, reliability, usability, security — an examiner checks each"),
         "caption": ("심사표는 이 네 가지를 같은 기준으로 봐요.", "The checklist covers these four items, the same way every time."),
         "small": ("사용성만 깊게 보는 시험도 따로 있어요.", "There's also a separate, deeper test just for usability.")},
        {"svg": P5, "alt": ("왼쪽: 마크가 완벽을 보장하진 않음. 오른쪽: 그래도 최소 기준은 확인됨", "Left: the mark doesn't guarantee perfection. Right: a minimum standard is still confirmed"),
         "caption": ("마크가 있어도 완벽을 뜻하진 않아요.", "Having the mark doesn't mean it's perfect."),
         "small": ("'이 기준은 통과했다'는 뜻일 뿐이에요.", "It only means the standard was met.")},
    ],
    "summary": (("<b>SW 품질인증</b> = 출판사가 아니라 <b>바깥 기관</b>이, 모든 책에 <b>같은 기준</b>으로 검사해 주는 공식 마크.",
                 "<b>Software quality certification</b> = an official mark from an <b>outside body</b>, applying the <b>same standard</b> to every book, not the publisher's own word."),
                ("SW 품질인증은 지정된 시험기관이 ISO/IEC 25010 등 정해진 품질특성 기준으로 제품을 검사해 공식 마크(예: GS인증)를 부여하는 제도예요. 책 한 권(제품)을 보는 인증과, CMMI처럼 출판사 전체(조직)의 일하는 성숙도를 보는 인증은 서로 대상이 달라요.",
                 "Software quality certification is a designated test lab checking a product against fixed criteria such as ISO/IEC 25010, then awarding an official mark (e.g. GS Certification in Korea). A product-level mark like this differs from something like CMMI, which rates the maturity of the whole organization's process, not one product.")),
    "glossary": [
        ("SW 품질인증", "Software Quality Certification", ("정해진 기준을 통과했다는 공인 마크.", "An official mark saying a fixed standard was met."), ("마크엔 유효기간이 있어요.", "The mark comes with an expiry date.")),
        ("GS인증", "GS Certification", ("한국의 대표적인 SW 품질 인증 제도.", "Korea's flagship software quality certification."), ("지정 시험기관이 직접 시험해요.", "A designated test lab runs the tests.")),
        ("CMMI", "CMMI", ("책 한 권이 아니라 출판사 전체의 일하는 수준을 매기는 등급.", "A maturity rating for the whole publishing house's way of working, not one book."), ("조직 성숙도를 보는 인증이에요.", "It certifies organizational maturity.")),
        ("ISO/IEC 25010", "ISO/IEC 25010", ("심사표 항목들이 따르는 국제 품질특성 표준.", "The international standard the checklist's categories follow."), ("기능적합성·신뢰성·사용성·보안성 등 8가지예요.", "Eight characteristics, including functionality, reliability, usability, and security.")),
        ("품질보증(QA)", "QA", ("교정자가 날마다 하는 내부 품질 활동.", "The proofreader's day-to-day internal quality work."), ("인증은 바깥에서 가끔 확인하는 거예요.", "Certification is an outside check, done only now and then.")),
        ("정보시스템 감리/PMO", "IS Audit / PMO", ("그 책 한 권의 진행 과정을 들여다봐요.", "Looks into how one book's process is going, from the inside out."), ('인증은 결과물이 기준을 통과했는지만 봐요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Certification only checks whether the finished result meets the standard. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("사용성평가", "Usability Test", ("심사표 속 '사용성' 항목을 깊게 파고드는 시험.", "A test that digs deep into the checklist's one 'usability' item."), ('→ <a href="usability-ko.html">독자가 책을 쓱 넘겨보는 시험</a>', '→ <a href="usability-en.html">the test where a reader just tries the book cold</a>')),
        ("방법론 테일러링", "Methodology Tailoring", ("편집 규칙을 책마다 다르게 적용하는 것.", "Applying editing rules differently from book to book."), ('인증 기준은 공통이어도, 일하는 방식은 책마다 달라도 돼요. → <a href="tailoring-ko.html">책마다 다른 편집 규칙</a>', 'The certification standard is shared, but how each book gets made can still differ. → <a href="tailoring-en.html">different editing rules for each book</a>')),
    ],
}
