from _draw import *
from _world import *

# 1. 마감이 코앞, "일단 이대로 내고 나중에 고치자"
P1 = svg(300, sky(300)
         + person(300, 140, s=0.9, face=SWEAT + EYES, **EDITOR)
         + manuscript(420, 150, 0.9, marks=2)
         + bubble(420, 50, 240, 40, "⟦일단 이대로 내고, 나중에 고쳐요!|let's just ship it like this and fix it later!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦마감이 코앞이라 어쩔 수 없이 넘어가요|the deadline's right here, so it slides through anyway⟧", 13, "var(--ink)"))

# 2. 나중에 고치려니 손댈 데가 더 많아짐 (빚처럼 불어남)
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(160, 140, 0.6, marks=1) + manuscript(260, 150, 0.6, marks=2) + manuscript(360, 140, 0.6, marks=4)
         + '<path d="M160 190 h260" stroke="var(--bad)" stroke-width="3" marker-end="url(#arrdebt)"/>'
         + '<defs><marker id="arrdebt" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--bad)"/></marker></defs>'
         + person(560, 150, s=0.8, face=FROWN, **PROOFER)
         + bubble(440, 60, 240, 44, "⟦미뤄둔 게 쌓여서, 손댈 데가 점점 더 많아져요|what got postponed has piled up — now there's more and more to fix⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦당장은 빨랐지만, 나중은 더 느려져요|fast now, but slower and slower later⟧", 12, "var(--ink)"))

# 3. 기술부채 = 나중에 갚아야 할 빚, 안 갚으면 이자처럼 불어남 (hero)
P3 = svg(340, sky(340)
         + '<rect x="260" y="130" width="240" height="90" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
         + label(380, 160, "⟦장부: 미룬 일 목록|LEDGER: postponed work⟧", 13, "#142033", cls="d")
         + '<path d="M280 180 h200 M280 198 h160" stroke="#142033" stroke-width="2"/>'
         + person(160, 170, s=0.85, face=EYES, **EDITOR) + person(560, 170, s=0.85, face=SWEAT + EYES, **WRITER)
         + label(380, 30, "⟦기술부채 = 지금 빨리 가려고 쌓아둔, 나중에 갚아야 할 빚|technical debt = a debt piled up to move fast now, to be repaid later⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦안 갚으면 이자(수정 비용)처럼 계속 불어나요|leave it unpaid, and it grows like interest (rising cost to fix)⟧", 12, "var(--muted)"))

# 4. 의도적 빚 vs 무의식적 빚, 당장 비용 vs 나중 비용
P4 = svg(320, sky(320)
         + styleguide(60, 30, 300, 260, "⟦빚이 쌓이는 방식|HOW THE DEBT PILES UP⟧",
                      ("⟦의도적 — 알면서 급하게 선택|deliberate — knowingly chosen, for speed⟧",
                       "⟦무의식적 — 모르고 저지른 실수|inadvertent — a mistake, unnoticed⟧"), 1.0)
         + styleguide(400, 30, 300, 260, "⟦갚는 시점|WHEN TO REPAY⟧",
                      ("⟦당장은 비용이 적어요|costs little right now⟧",
                       "⟦나중엔 이자처럼 불어나요|grows like interest later⟧"), 1.0, hl=1)
         + label(380, 300, "⟦의도적이든 아니든, 장부에 적어두고 계획적으로 갚아야 해요|deliberate or not, write it in the ledger and repay it on purpose⟧", 12, "var(--ink)"))

# 5. 빚을 0으로 만들 필요는 없음, 기록하고 계획적으로 갚는 게 핵심
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=FROWN, **EDITOR)
         + label(190, 240, "⟦빚을 완전히 0으로 만들면 마감을 못 맞춰요|driving the debt to zero means missing every deadline⟧", 11, "var(--ink)")
         + '<rect x="540" y="130" width="60" height="70" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + person(600, 180, s=0.7, face=SMILE, **PROOFER)
         + label(570, 230, "⟦장부에 적어두고 계획적으로 갚아요|write it down, repay it on purpose⟧", 11, "var(--ink)")
         + label(380, 282, "⟦핵심은 빚을 없애는 게 아니라, 기록하고 계획적으로 갚는 거예요|the point isn't erasing debt — it's recording and repaying it on purpose⟧", 12, "var(--ink)", cls="d"))

LEDGER_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')
INTEREST_I = icon('<path d="M14 46 L26 28 L38 36 L50 14" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
DELIBERATE_I = icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 22 v10 l8 4" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
REPAY_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M24 32 l6 6 l12 -14" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "techdebt", "order": 30,
    "title": ("지금 빨리 가려고 쌓아둔 빚", "The Debt You Pile Up to Move Fast Now"),
    "h1": ("<em>기술부채</em>가 뭐예요?", "What is <em>Technical Debt</em>?"),
    "sub": ("기술부채를, 마감에 쫓겨 '일단 이대로 내고 나중에 고치자'고 넘긴 일들이 쌓이는 출판사 이야기로 풀어봤어요.",
            "Technical debt, told as a story about a publishing house piling up the things it kept postponing under deadline pressure."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 마감에 쫓겨 결함 있는 원고를 일단 내자고 함", "Under deadline pressure, the editor says to ship the flawed manuscript now and fix it later"),
         "caption": ("마감이 코앞이라 '일단 이대로 내자'고 넘어가요.", "The deadline is right here, so it slides through as 'ship it now'."),
         "small": ("마감이 코앞이라 어쩔 수 없이 넘어가요.", "The deadline's right here, so it slides through anyway.")},
        {"svg": P2, "alt": ("미뤄둔 결함이 원고마다 쌓여 늘어나고 교정자가 힘들어함", "Postponed flaws pile up across manuscripts and the proofreader struggles"),
         "caption": ("미뤄둔 게 쌓여서, 손댈 데가 점점 더 많아져요.", "What got postponed has piled up — there's more and more to fix."),
         "small": ("당장은 빨랐지만, 나중은 더 느려져요.", "Fast now, but slower and slower later.")},
        {"svg": P3, "hero": True, "alt": ("편집장과 작가 사이에 '미룬 일 목록' 장부가 놓여 있음", "A ledger of postponed work sits between the editor and the writer"),
         "caption": ("기술부채는 지금 빨리 가려고 쌓아둔, 나중에 갚을 빚이에요.", "Technical debt is a debt piled up to move fast now, repaid later."),
         "small": ("안 갚으면 이자처럼 계속 불어나요.", "Leave it unpaid, and it grows like interest."),
         "tricks": (4, [
             (DELIBERATE_I, ("알면서 쌓는 빚", "Debt taken on knowingly"), ("급할 때 일부러 선택해요", "chosen on purpose, when it's urgent"), "calm"),
             (LEDGER_I, ("모르고 쌓는 빚", "Debt piled up unnoticed"), ("실수나 무지로 생겨요", "from a mistake or not knowing better")),
             (INTEREST_I, ("안 갚으면 이자처럼", "Left unpaid, it grows like interest"), ("수정 비용이 계속 불어나요", "the cost to fix just keeps rising"), "warm"),
             (REPAY_I, ("장부에 적고 계획적으로", "Record it, repay it on purpose"), ("언젠가 갚을 계획을 세워요", "with a real plan to pay it off")),
         ])},
        {"svg": P4, "alt": ("의도적/무의식적 빚이 쌓이는 방식과, 당장 비용 vs 나중 비용(이자)을 정리한 표", "Tables comparing deliberate vs. inadvertent debt, and cost now vs. cost later (interest)"),
         "caption": ("빚은 알면서 쌓을 수도, 모르고 쌓일 수도 있어요.", "Debt can be taken on knowingly, or pile up without anyone noticing."),
         "small": ("의도적이든 아니든, 적어두고 계획적으로 갚아야 해요.", "Deliberate or not, it needs to be recorded and repaid on purpose.")},
        {"svg": P5, "alt": ("왼쪽: 빚을 완전히 0으로 만들려다 마감을 놓침. 오른쪽: 장부에 적어 계획적으로 갚음", "Left: trying to zero out the debt misses every deadline. Right: writing it in a ledger and repaying it on purpose"),
         "caption": ("빚을 0으로 만들 필요는 없어요.", "The debt doesn't need to hit zero."),
         "small": ("핵심은 빚을 없애는 게 아니라, 기록하고 계획적으로 갚는 거예요.", "The point isn't erasing debt — it's recording and repaying it on purpose.")},
    ],
    "summary": (("<b>기술부채</b>는 지금 <b>빨리 가려고 미뤄둔 일</b>이 쌓인 '빚'이에요. 갚지 않으면 <b>이자처럼 수정 비용</b>이 계속 불어나요.",
                 "<b>Technical debt</b> is the 'debt' of work postponed <b>to move fast now</b>. Left unpaid, the cost to fix it keeps growing <b>like interest</b>."),
                ("기술부채는 더 나은 설계·구현을 미루고 당장 빠른 방법을 택했을 때 쌓이는, 나중에 치러야 할 대가를 빚에 비유한 개념이에요. 알면서 선택하는 의도적 부채와 모르고 쌓이는 무의식적 부채로 나뉘고, 갚지 않고 방치하면 코드 수정 비용이 복리 이자처럼 불어나요. 목표는 부채를 0으로 만드는 게 아니라, 장부(백로그)에 기록하고 계획적으로 상환하는 거예요.",
                 "Technical debt is a metaphor for the future cost incurred when a faster, lower-quality approach is chosen over a better design now. It splits into deliberate debt (knowingly taken on) and inadvertent debt (accumulated without realizing it); left unpaid, the cost to fix it compounds like interest. The goal isn't zero debt — it's tracking it in a backlog and repaying it deliberately.")),
    "glossary": [
        ("기술부채", "Technical Debt", ("나중에 갚아야 할 빚.", "A debt that must be repaid later."), ("안 갚으면 이자처럼 불어나요.", "Left unpaid, it grows like interest.")),
        ("의도적 부채", "Deliberate Debt", ("알면서 급하게 선택한 빚.", "Debt knowingly taken on, for speed."), ("나쁜 게 아니라, 기록이 중요해요.", "Not bad in itself — recording it is what matters.")),
        ("무의식적 부채", "Inadvertent Debt", ("모르고 저지른 실수가 쌓인 빚.", "Debt that piles up from an unnoticed mistake."), ("뒤늦게 발견되는 경우가 많아요.", "Often discovered only much later.")),
        ("리팩토링", "Refactoring", ("빚을 갚는 대표적인 방법.", "The classic way to repay this debt."), ('줄거리는 그대로 두고 구조만 다시 다듬어요. → <a href="refactorppe-ko.html">줄거리는 그대로, 문장만 다시 다듬기</a>', 'Keeping the plot the same while reworking the structure. → <a href="refactorppe-en.html">same plot, retouched sentences</a>')),
        ("코드 스멜", "Code Smell", ("문장이 꼬여 보이는 낌새.", "The whiff of sentences gone tangled."), ("빚이 쌓이고 있다는 신호예요.", "A sign the debt is piling up.")),
        ("WBS", "WBS", ("일정에 쫓기면 빚이 쌓이기 쉬운 이유.", "Why schedule pressure makes debt easy to accumulate."), ('일정이 너무 빠듯하면 이 빚이 쌓여요. → <a href="wbsswe-ko.html">책 만들기를 나뭇가지로 늘어놓기</a>', 'Too tight a schedule, and this debt piles up. → <a href="wbsswe-en.html">laying out the book as a tree</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("빚이 너무 쌓였는지 바깥에서 점검하는 사람.", "The outside checker watching whether debt has piled up too far."), ('여러 프로젝트의 빚을 한눈에 봐요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'Watches debt across many projects at once. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
        ("단위테스트", "Unit Test", ("빚을 갚을 때 줄거리가 안 바뀌었나 보는 교정.", "The proofing that checks the plot held while the debt is repaid."), ("테스트 없인 안전하게 갚을 수 없어요.", "Without tests, repaying debt safely is hard.")),
    ],
}
