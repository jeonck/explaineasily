from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
INSPECTOR = dict(hat="#E9B44C", shirt="#7B3FA0")
KEEPER = dict(hat=None, shirt="#B5651D")


def warehouse(x, y, s=1.0, stamped=False):
    st = ('<circle cx="34" cy="-10" r="16" fill="var(--good)"/><path d="M26 -10 l5 6 l12 -14" stroke="#FFF" stroke-width="3" fill="none" stroke-linecap="round"/>') if stamped else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-44" y="-10" width="88" height="70" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-50 -10 L0 -46 L50 -10 Z" fill="var(--stone-dark)"/><rect x="-16" y="18" width="32" height="42" fill="var(--night)"/>{st}</g>')


def clipboard(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-28" width="44" height="56" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            + '<rect x="-10" y="-34" width="20" height="10" rx="3" fill="#C9A86A"/><path d="M-12 -10 h24 M-12 -2 h24 M-12 6 h16 M-12 14 h24" stroke="#142033" stroke-width="2" stroke-linecap="round"/></g>')


# 1. 관청이 바깥 창고를 빌리고 싶은데
P1 = svg(320, sky(320)
         + person(190, 130, s=0.85, face=EYES, **CLERK) + bubble(60, 40, 240, 42, "⟦우리 장부를 바깥 창고에 맡겨도 될까요?|can we trust our records to an outside warehouse?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + warehouse(500, 160, 1.0) + person(560, 220, s=0.6, face=SMILE, **KEEPER) + label(500, 260, "⟦빌린 창고(클라우드)|the rented warehouse (cloud)⟧", 11, "var(--muted)"))

# 2. 창고마다 안전하다고만 말해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + warehouse(170, 160) + person(230, 220, s=0.55, face=SMILE, **KEEPER) + bubble(60, 60, 200, 36, "⟦저희 창고 완전 안전해요!|our warehouse is totally safe!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + warehouse(460, 160) + person(520, 220, s=0.55, face=SMILE, **KEEPER) + bubble(390, 60, 200, 36, "⟦저희도 안전한데요!|so is ours!⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + person(670, 130, s=0.7, face=FROWN, **CLERK)
         + label(380, 282, "⟦다 안전하다는데, 기준이 없어 확인할 길이 없어요|everyone claims it's safe, but there's no shared standard to check it against⟧", 11, "var(--ink)", cls="d"))

# 3. CSAP = 왕의 점검관이 검사하고 도장을 찍어줌 (hero)
P3 = svg(340, sky(340)
         + person(170, 140, s=0.85, face=EYES, **INSPECTOR) + clipboard(280, 110, 0.9)
         + warehouse(470, 170, 1.1, stamped=True)
         + '<path d="M250 150 L410 160" stroke="var(--good)" stroke-width="3" stroke-dasharray="5 5"/>'
         + person(620, 230, s=0.7, face=EYES, **CLERK) + label(620, 300, "⟦이 도장 찍힌 창고만 관청이 빌려요|only a stamped warehouse may be rented by a government office⟧", 11, "var(--good)")
         + label(380, 320, "⟦CSAP = 왕의 점검관이 정해진 표로 검사하고 도장을 찍는 제도|CSAP = the king's inspector checks against a fixed list and stamps it⟧", 13, "var(--ink)", cls="d"))

LIST_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 30 h24 M20 38 h16" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
TIER_I = icon('<rect x="12" y="38" width="12" height="16" fill="var(--good)"/><rect x="26" y="26" width="12" height="28" fill="#E9B44C"/><rect x="40" y="14" width="12" height="40" fill="var(--bad)"/>')
GOV_I = icon('<path d="M20 50 h24 M14 36 l18 -20 l18 20" fill="none" stroke="#7B3FA0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><rect x="18" y="36" width="6" height="14" fill="#7B3FA0"/><rect x="29" y="36" width="6" height="14" fill="#7B3FA0"/><rect x="40" y="36" width="6" height="14" fill="#7B3FA0"/>')
RECHECK_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 16 A16 16 0 1 1 18 24" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M14 18 l4 8 l8 -3" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')

PAGE = {
    "slug": "csap", "order": 17,
    "title": ("빌린 창고에 찍는 왕의 안전 도장", "The King's Safety Stamp on a Rented Warehouse"),
    "h1": ("<em>CSAP</em>가 뭐예요?", "What is <em>CSAP</em>?"),
    "sub": ("CSAP(클라우드 보안인증제)를, 빌린 창고(클라우드)를 왕의 점검관이 검사해 도장 찍어주는 이야기로 풀어봤어요.",
            "CSAP (Cloud Security Assurance Program), told as a story about the king's inspector checking a rented warehouse and stamping it."),
    "panels": [
        {"svg": P1, "alt": ("관청 서기가 바깥 빌린 창고에 장부를 맡겨도 되는지 걱정함", "A government clerk worries about whether it's safe to entrust records to an outside rented warehouse"),
         "caption": ("관청이 바깥 창고를 빌리고 싶은데 걱정돼요.", "The office wants to rent an outside warehouse, but isn't sure it's safe."),
         "small": ("빌린 창고(클라우드)에 우리 장부를 맡겨도 될지, 서기는 확신이 없어요.", "The clerk isn't sure whether it's safe to trust the office's records to a rented warehouse (the cloud).")},
        {"svg": P2, "alt": ("두 창고 주인이 모두 자기 창고가 완전 안전하다고 말하지만, 서기는 확인할 기준이 없어 곤란해함", "Two warehouse keepers both claim their warehouse is totally safe, but the clerk has no shared standard to check it against"),
         "caption": ("창고마다 안전하다고만 말해요.", "Every warehouse just claims to be safe."),
         "small": ("저마다 안전하다고 하는데, 공통 기준이 없어서 뭘 믿어야 할지 알 수 없어요.", "Everyone says they're safe, but with no common standard, there's no way to know who to believe.")},
        {"svg": P3, "hero": True, "alt": ("왕의 점검관이 점검표를 들고 창고를 검사해 도장을 찍고, 도장 찍힌 창고만 관청이 빌릴 수 있음", "The king's inspector checks the warehouse with a checklist and stamps it, and only a stamped warehouse may be rented by a government office"),
         "caption": ("CSAP는 왕의 점검관이 검사하고 도장을 찍는 제도예요.", "CSAP is the king's inspector checking it and stamping it."),
         "small": ('정해진 점검표로 검사하고 통과한 창고에만 도장을 찍어요. → <a href="cspm-ko.html">빌린 창고 문단속 점검</a>은 도장을 찍은 뒤에도 계속해요.',
                   'It checks against a fixed list and stamps only the ones that pass. → <a href="cspm-en.html">ongoing door-checks on the rented warehouse</a> continue even after the stamp.'),
         "tricks": (4, [
             (LIST_I, ("정해진 점검표로 확인", "Checked against a fixed list"), ("물리 보안·접근통제·분리 등", "physical security, access control, isolation"), "calm"),
             (TIER_I, ("등급을 나눠요", "Graded into tiers"), ("상·중·하 등급으로 나뉘어요", "split into high/medium/low tiers")),
             (GOV_I, ("공공기관은 의무예요", "Mandatory for public agencies"), ("도장 없는 창고는 못 빌려요", "no stamp, no rental"), "warm"),
             (RECHECK_I, ("주기적으로 다시 검사", "Re-inspected periodically"), ("도장은 영원하지 않아요", "the stamp doesn't last forever")),
         ])},
        {"svg": svg(330, sky(330)
                    + '<rect x="40" y="30" width="680" height="250" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="40" y="30" width="680" height="34" rx="8" fill="#C9A86A"/>'
                    + label(130, 53, "⟦등급|tier⟧", 13, "#142033", cls="d") + label(400, 53, "⟦맡길 수 있는 장부|what it may hold⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M40 {64 + i * 70} h680" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(100, 100, "⟦상등급|high tier⟧", 13, "#142033", cls="d") + label(400, 100, "⟦민감한 행정·기밀 장부까지|even sensitive administrative, classified records⟧", 11, "#142033")
                    + label(100, 170, "⟦중·하등급|mid/low tier⟧", 13, "#142033", cls="d") + label(400, 170, "⟦일반 업무 장부|ordinary day-to-day records⟧", 11, "#142033")
                    + label(100, 240, "⟦도장 없음|no stamp⟧", 13, "var(--bad)", cls="d") + label(400, 240, "⟦관청은 아예 못 빌려요|government offices can't rent it at all⟧", 11, "var(--bad)")),
         "alt": ("표: 상등급은 민감한 기밀 장부까지, 중·하등급은 일반 업무 장부, 도장 없음은 관청이 아예 못 빌림", "Table: high tier up to sensitive classified records, mid/low tier for ordinary records, no stamp means government offices can't rent it at all"),
         "caption": ("등급에 따라 맡길 수 있는 장부가 달라요.", "The tier decides what kind of record can go there."),
         "small": ("중요한 장부일수록 더 높은 등급의 창고가 필요해요.", "The more sensitive the record, the higher the tier it needs.")},
        {"svg": svg(300, sky(300)
                    + warehouse(190, 150, 1.0, stamped=True) + label(190, 230, "⟦관청에 의무, 민간은 참고로 많이 써요|mandatory for government, many private firms follow it too⟧", 11, "var(--muted)")
                    + person(560, 150, s=0.85, face=EYES, **INSPECTOR) + label(560, 230, "⟦도장이 다가 아니에요, 계속 점검해야 해요|the stamp isn't the finish line — checking continues⟧", 11, "var(--bad)")
                    + label(380, 280, "⟦우리나라만의 제도라, 해외 창고는 별도 기준을 따로 봐야 해요|a Korea-specific system — a warehouse abroad needs its own separate standard checked⟧", 12, "var(--ink)", cls="d")),
         "alt": ("관청엔 의무, 민간은 참고용. 도장 이후에도 지속적인 점검이 필요하고, 다른 나라 창고는 별도 기준이 필요함", "Mandatory for government, a reference for private firms. Checking continues even after the stamp, and warehouses abroad need their own separate standard"),
         "caption": ("도장 하나로 끝나는 게 아니에요.", "The stamp alone doesn't end the story."),
         "small": ('우리나라 제도라 해외엔 안 통하고, 도장 이후에도 <a href="cspm-ko.html">문단속 점검</a>은 계속돼요.',
                   'It\'s a Korea-specific system that doesn\'t carry abroad, and the <a href="cspm-en.html">door-checking</a> continues even after the stamp.')},
    ],
    "summary": (("<b>CSAP</b> = 왕의 점검관이 빌린 창고(클라우드)를 <b>정해진 표</b>로 검사해 <b>도장</b>을 찍는 제도. <b>도장 없는 창고는 관청이 못 빌려요.</b>",
                 "<b>CSAP</b> = the king's inspector checks a rented warehouse (the cloud) against a <b>fixed list</b> and gives it a <b>stamp</b>. <b>No stamp, and a government office can't rent it.</b>"),
                ("CSAP, Cloud Security Assurance Program(클라우드 보안인증제). 한국인터넷진흥원(KISA)이 클라우드 서비스의 물리적·기술적·관리적 보안 수준을 심사해 인증하는 제도예요. 공공기관이 클라우드를 이용하려면 CSAP 인증을 받은 서비스를 써야 하고, 다루는 정보의 민감도에 따라 등급(기존 상·중·하에서 다등급제로 개편)이 나뉘어요.",
                 "CSAP, Cloud Security Assurance Program. KISA (Korea Internet & Security Agency) reviews and certifies a cloud service's physical, technical, and managerial security level. Korean public agencies must use a CSAP-certified cloud service, and the certification is tiered (originally high/medium/low, now a more granular multi-tier system) by how sensitive the information is.")),
    "glossary": [
        ("CSAP", "CSAP", ("빌린 창고에 찍는 왕의 안전 도장.", "The king's safety stamp on a rented warehouse."), ("한국 클라우드 보안인증제예요.", "Korea's Cloud Security Assurance Program.")),
        ("KISA", "KISA", ("점검하는 왕의 점검관.", "The king's inspector who checks it."), ("한국인터넷진흥원. 실제 심사를 맡아요.", "The Korea Internet & Security Agency, which runs the actual review.")),
        ("다등급제", "Multi-tier system", ("창고를 안전도별로 나눈 것.", "Grading warehouses by how safe they are."), ("다루는 정보의 민감도에 따라 받을 수 있는 등급이 달라요.", "Which tier you can earn depends on how sensitive the data is.")),
        ("공공기관 의무화", "Mandatory for public agencies", ("도장 없는 창고는 관청이 못 빌려요.", "No stamp, and a government office can't rent it."), ("공공 클라우드 전환의 전제 조건이에요.", "A precondition for any public-sector cloud migration.")),
        ("CSPM", "CSPM", ("도장 이후에도 계속하는 문단속.", "The door-checking that continues after the stamp."), ('CSAP는 한 번의 인증, CSPM은 이후의 지속 점검이에요. → <a href="cspm-ko.html">빌린 창고 문단속 점검</a>', 'CSAP is a one-time certification; CSPM is the ongoing check afterward. → <a href="cspm-en.html">door-checking the rented warehouse</a>')),
        ("클라우드", "Cloud", ("빌린 창고.", "The rented warehouse."), ("성 밖에 두고 빌려 쓰는 창고예요.", "A warehouse kept outside the castle and rented for use.")),
        ("물리 보안", "Physical security", ("창고 건물 자체의 안전.", "The safety of the warehouse building itself."), ("점검표의 한 항목이에요.", "One of the items on the inspector's checklist.")),
        ("규정 준수", "Compliance", ("점검관이 확인해주는 것 전반.", "The broader idea of being checked and confirmed."), ('CSAP는 클라우드에 한정된 규정 준수 제도예요. → <a href="compliance-ko.html">이웃 나라 규칙 검사관</a>', 'CSAP is a compliance program specific to the cloud. → <a href="compliance-en.html">the inspector from the neighboring kingdom</a>')),
    ],
}
