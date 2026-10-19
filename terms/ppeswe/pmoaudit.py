from _draw import *
from _world import *

# 1. 편집장이 책을 여러 권 동시에 맡아 정신없어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **EDITOR)
         + manuscript(260, 130, 0.8) + manuscript(360, 150, 0.8) + manuscript(460, 120, 0.8)
         + label(380, 230, "⟦책 세 권이 동시에 늦어지고 있어요|three books are all running late at once⟧", 12, "var(--bad)")
         + label(380, 280, "⟦편집장 혼자서는 전부를 다 챙길 수 없어요|one editor can't watch everything alone⟧", 13, "var(--ink)"))

# 2. 작가는 자기 책만 보느라 전체 일정을 놓쳐요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **WRITER)
         + bubble(140, 80, 180, 36, "⟦제 원고는 잘 쓰고 있는데요?|my own manuscript is going great⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **PRINTER) + bubble(470, 80, 220, 36, "⟦근데 인쇄 일정 전체가 꼬였어요|but the whole print schedule is a mess⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦각자 자기 몫만 보면, 전체 그림은 아무도 안 봐요|everyone watching their own part means nobody watches the whole picture⟧", 12, "var(--ink)"))

# 3. 감리/PMO = 출간 전 전체를 점검하는 사람 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **PRINTER) + inkstamp(460, 90, 0.8)
         + manuscript(260, 180, 0.7) + manuscript(380, 200, 0.7) + manuscript(500, 180, 0.7)
         + label(380, 30, "⟦감리/PMO = 모든 책을 바깥에서 점검하는 사람|Audit/PMO = someone who checks every book from the outside⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦일정·품질·위험을 한눈에 보고, 늦기 전에 알려줘요|watching schedule, quality, and risk together — flagging trouble early⟧", 12, "var(--muted)"))

# 4. 감리 체크리스트
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦감리 점검표|AUDIT CHECKLIST⟧",
                      ("⟦일정 — 제때 끝나나|schedule — on time?⟧",
                       "⟦품질 — 교정 기준 지켰나|quality — proofing standard met?⟧",
                       "⟦위험 — 막힌 곳은 없나|risk — any blockers?⟧",
                       "⟦보고 — 윗선에 투명하게|reporting — transparent upward⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **PRINTER)
         + label(560, 250, "⟦작가 대신 쓰지 않아요, 확인만 해요|doesn't write for the author — only checks⟧", 11, "var(--muted)")
         + label(380, 300, "⟦PMO 는 이 점검을 여러 책(프로젝트)에 걸쳐 동시에 해요|PMO does this checking across many books at once⟧", 12, "var(--ink)"))

# 5. 감리가 다 해결해주진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **PRINTER) + label(190, 240, "⟦늦는 걸 알려줄 순 있어요|can flag that it's running late⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **WRITER) + manuscript(570, 220, 0.6) + label(570, 270, "⟦직접 쓰는 건 결국 작가예요|but the author still has to write it⟧", 11, "var(--ink)")
         + label(380, 282, "⟦감리/PMO는 확인하고 조율하는 역할이지, 개발을 대신하지 않아요|audit/PMO checks and coordinates — it doesn't do the development itself⟧", 12, "var(--ink)", cls="d"))

CHECK_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 32 l8 8 l16 -18" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
FLAG_I = icon('<rect x="18" y="8" width="4" height="48" fill="#5A3B22"/><path d="M22 10 h26 l-8 10 l8 10 h-26 z" fill="var(--bad)"/>')
REPORT_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5"/>')

PAGE = {
    "slug": "pmoaudit", "order": 1,
    "title": ("출간 전 마지막 검수관", "The Last Checker Before Publication"),
    "h1": ("<em>정보시스템 감리/PMO</em>가 뭐예요?", "What is <em>IS Audit/PMO</em>?"),
    "sub": ("정보시스템 감리와 PMO를, 여러 책의 출간을 동시에 바깥에서 점검하는 검수관 이야기로 풀어봤어요.",
            "IS audit and PMO, told as a story about an outside checker watching several books head toward publication at once."),
    "panels": [
        {"svg": P1, "alt": ("편집장이 책 세 권을 동시에 맡아 진땀을 흘림", "An editor sweats, juggling three books at once"),
         "caption": ("책 세 권이 동시에 늦어지고 있어요.", "Three books are all running late at once."),
         "small": ("편집장 혼자서는 전부를 다 챙길 수 없어요.", "One editor can't watch everything alone.")},
        {"svg": P2, "alt": ("작가는 자기 원고만 보며 만족하지만, 인쇄 감독은 전체 일정이 꼬였다고 말함", "The author is happy with their own manuscript, while the print supervisor says the whole schedule is a mess"),
         "caption": ("작가는 자기 책만 보느라 전체 일정을 놓쳐요.", "The author, watching only their own book, misses the full schedule."),
         "small": ("각자 자기 몫만 보면, 전체 그림은 아무도 안 봐요.", "When everyone watches only their own part, nobody watches the whole picture.")},
        {"svg": P3, "hero": True, "alt": ("인쇄 감독이 승인 도장을 들고 여러 원고를 바깥에서 점검함", "A print supervisor holds an approval stamp, checking several manuscripts from the outside"),
         "caption": ("감리/PMO는 모든 책을 바깥에서 점검하는 사람이에요.", "Audit/PMO is someone who checks every book from the outside."),
         "small": ("일정·품질·위험을 한눈에 보고, 늦기 전에 알려줘요.", "Watching schedule, quality, and risk together — flagging trouble early."),
         "tricks": (4, [
             (CHECK_I, ("기준대로 확인하기", "Check against the standard"), ("정해진 점검표로요", "using a fixed checklist"), "calm"),
             (CLOCK_I, ("일정 지켜보기", "Watch the schedule"), ("늦기 전에 알려줘요", "flag it before it slips")),
             (FLAG_I, ("위험 미리 표시하기", "Flag risk early"), ("막힌 곳을 찾아요", "spot the blockers"), "warm"),
             (REPORT_I, ("투명하게 보고하기", "Report transparently"), ("윗선도 같이 봐요", "so leadership sees it too")),
         ])},
        {"svg": P4, "alt": ("감리 점검표: 일정·품질·위험·보고 네 항목. 인쇄 감독은 작가 대신 쓰지 않고 확인만 함", "An audit checklist: schedule, quality, risk, reporting. The supervisor only checks — doesn't write for the author"),
         "caption": ("감리는 이 네 가지를 점검해요.", "Audit checks these four things."),
         "small": ("작가 대신 쓰지 않아요, 확인만 해요. PMO는 이걸 여러 책에 걸쳐 동시에 해요.", "It doesn't write for the author — only checks. PMO does this across many books at once.")},
        {"svg": P5, "alt": ("왼쪽: 인쇄 감독이 늦는 걸 알려줌. 오른쪽: 결국 쓰는 건 작가", "Left: the supervisor flags the delay. Right: the author still has to write it"),
         "caption": ("감리가 다 해결해주진 않아요.", "Audit doesn't solve everything."),
         "small": ("확인하고 조율하는 역할이지, 개발을 대신하지 않아요.", "It checks and coordinates — it doesn't do the development itself.")},
    ],
    "summary": (("<b>정보시스템 감리/PMO</b> = 여러 프로젝트를 <b>바깥에서 동시에 점검</b>하며 <b>일정·품질·위험</b>을 미리 알려주는 역할.",
                 "<b>IS Audit/PMO</b> = an outside role that checks several projects at once, flagging <b>schedule, quality, and risk</b> before they become real problems."),
                ("정보시스템 감리는 외부 전문가가 사업 전반(관리·품질·보안)을 독립적으로 점검해 발주자에게 보고하는 제도이고, PMO(Project Management Office)는 여러 프로젝트를 표준화된 기준으로 총괄 관리하는 조직이에요. 감리는 '진단'에, PMO는 '운영 지원'에 더 가까워요.",
                 "IS audit is an independent review by outside experts covering management, quality, and security, reported to the client. PMO (Project Management Office) oversees multiple projects under standardized criteria. Audit leans toward diagnosis; PMO leans toward operational support.")),
    "glossary": [
        ("정보시스템 감리", "IS Audit", ("바깥에서 하는 독립 점검.", "An independent check from the outside."), ("발주자에게 직접 보고해요.", "Reports straight to the client.")),
        ("PMO", "Project Management Office", ("여러 프로젝트를 총괄하는 조직.", "The office that oversees many projects."), ("표준 기준으로 관리해요.", "Manages them against one shared standard.")),
        ("ISP/ISMP", "ISP/ISMP", ("출판 계획 자체를 세우는 단계.", "The stage of planning the publishing roadmap itself."), ('감리 이전, 무엇을 만들지부터 정해요. → <a href="ispismp-ko.html">출판 로드맵을 그리는 사람</a>', 'Before audit — deciding what to build at all. → <a href="ispismp-en.html">the one who maps the publishing roadmap</a>')),
        ("WBS", "WBS", ("공연/출판 준비 체크리스트.", "The prep checklist for a show or a book."), ('비슷한 점검 도구가 다른 세계에도 있어요. → <a href="wbsppm-ko.html">PPE·IT관리 세계의 체크리스트</a>', 'A similar tool exists in another world too. → <a href="wbsppm-en.html">the checklist in the PPE·IT Mgmt world</a>')),
        ("품질보증(QA/QC)", "QA/QC", ("교정자가 하는 일.", "What the proofreader does."), ("감리는 이걸 포함해 더 넓게 봐요.", "Audit covers this and looks even wider.")),
        ("형상관리", "Configuration Management", ("원고를 보관하는 서가.", "The shelf where manuscripts are kept."), ('감리가 점검하는 항목 중 하나예요. → <a href="scmshelf-ko.html">원고를 지키는 보관 서가</a>', "One of the things audit checks. → <a href=\"scmshelf-en.html\">the shelf that protects the manuscript</a>")),
        ("SLA", "SLA", ("관객에게 보장한 약속.", "The promise made to the audience."), ('다른 세계(IT관리)에서 자세히 다뤄요. → <a href="slappe-ko.html">공연 보장 티켓</a>', 'Covered in depth in another world (IT Mgmt). → <a href="slappe-en.html">the ticket that guarantees the show</a>')),
        ("기능점수(FP)", "Function Point", ("매수 계산 자.", "The measuring ruler for page count."), ('감리가 규모를 가늠할 때 써요. → <a href="fpruler-ko.html">매수를 재는 자</a>', "Used by audit to gauge project size. → <a href=\"fpruler-en.html\">the ruler that measures page count</a>")),
    ],
}
