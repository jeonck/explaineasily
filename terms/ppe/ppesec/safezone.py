from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")
ANALYST = dict(hat="#5B8DEF", shirt="#5B8DEF")


def ledger(x, y, s=1.0, color="#FFF8E7"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-32" width="52" height="64" rx="3" fill="{color}" stroke="#C9A86A" stroke-width="2"/>'
            '<path d="M-16 -18 h32 M-16 -8 h32 M-16 2 h20" stroke="#C9A86A" stroke-width="2" stroke-linecap="round"/></g>')


def reading_room(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-90" y="-10" width="180" height="140" fill="var(--panel)" stroke="var(--good)" stroke-width="5"/>'
            f'<path d="M-100 -10 L0 -56 L100 -10 Z" fill="var(--good)"/>'
            + label(0, -70, "⟦안심구역|SAFE ZONE⟧", 13, "var(--muted)") + "</g>")


def paper_small(x, y, s=1.0, text=""):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-16" width="44" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
            + label(0, 4, text, 10, "#142033", cls="d") + "</g>")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 각자 장부를 성 밖으로 못 들고 나가요
P1 = svg(280, sky(280)
         + small_castle(60, 70, 0.5) + ledger(150, 190, 0.9) + label(150, 230, "⟦성 A|castle A⟧", 11, "var(--muted)")
         + small_castle(560, 70, 0.5) + ledger(650, 190, 0.9) + label(650, 230, "⟦성 B|castle B⟧", 11, "var(--muted)")
         + '<path d="M250 190 L560 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 4"/>'
         + label(405, 170, "⟦못 보내요|can\'t send it⟧", 13, "var(--bad)", cls="d")
         + label(380, 258, "⟦합치면 더 좋은 답이 나오는데, 장부를 성 밖으로 못 들고 나가요|combining them would help — but neither ledger may leave its own castle⟧", 12, "var(--ink)"))

# 2. 그렇다고 그냥 보내주면 위험해요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + ledger(150, 130, 1.0) + person(220, 160, s=0.6, face=MASK)
         + label(190, 230, "⟦그냥 보내면 도둑도 가로채요|send it plainly, and a thief can grab it too⟧", 12, "var(--bad)")
         + person(560, 150, s=0.75, face=FROWN, **CLERK)
         + bubble(480, 60, 240, 40, "⟦그래서 아무도 안 보내줘요|so no one sends anything, ever⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦결국 각자 성 안에서만 보다 보니 더 좋은 분석을 못 해요|everyone stays locked inside their own castle, and the better analysis never happens⟧", 12, "var(--ink)"))

# 3. 안심구역 = 밖으로 못 들고 나가는 특별 열람실 (hero)
P3 = svg(340, sky(340)
         + reading_room(380, 150, 1.0)
         + ledger(300, 160, 0.8) + ledger(460, 160, 0.8) + person(380, 220, s=0.65, face=EYES, **ANALYST)
         + paper_small(380, 260, 0.9, "⟦요약 결과|summary⟧")
         + person(640, 180, s=0.7, face=SMILE, **GUARD)
         + '<path d="M470 270 L600 220" stroke="var(--good)" stroke-width="2" stroke-dasharray="4 4"/>'
         + label(380, 30, "⟦안심구역 = 장부를 한 방에 모아, 그 안에서만 보고, 결과만 들고 나가요|a safe zone = ledgers gathered in one room, viewed only inside, only the result ever leaves⟧", 13, "var(--ink)", cls="d"))

# 4. 절차 타임라인
P4 = svg(300, sky(300)
         + box(50, 30, 660, 240, "⟦반출 절차|THE CHECK-OUT PROCESS⟧",
               ("⟦1. 신청 — 어떤 분석을 할지 먼저 적어요|1. apply — write down what analysis you plan⟧",
                "⟦2. 승인 — 결합전문기관이 괜찮은지 봐요|2. approval — the linkage body reviews it⟧",
                "⟦3. 분석 — 안심구역 안에서만 계산해요|3. analyze — computed only inside the safe zone⟧",
                "⟦4. 반출심사 — 결과가 재식별 위험 없는지 확인해요|4. export review — checked for re-identification risk⟧"), 13))

# 5. 승인이 오래 걸리고, 다 허락되진 않아요
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + person(160, 150, s=0.85, face=FROWN + SWEAT, **ANALYST)
         + '<g transform="translate(260,130)"><rect x="-26" y="-22" width="52" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="-26" y="-22" width="52" height="12" rx="4" fill="var(--accent)"/></g>'
         + label(260, 196, "⟦몇 주가 걸려요|it can take weeks⟧", 11, "var(--muted)")
         + paper_small(560, 150, 1.2, "⟦반출 불가|denied⟧") + person(650, 170, s=0.7, face=EYES, **GUARD)
         + label(380, 258, "⟦결과가 재식별될 수 있으면 반출 자체가 거부돼요|if the result could still be re-identified, the export itself is refused⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "safezone", "order": 12,
    "title": ("밖으로 못 들고 나가는 특별 열람실", "The Special Reading Room You Can't Carry Data Out Of"),
    "h1": ("<em>개인정보 안심구역</em>이 뭐예요?", "What is a <em>Personal-Data Safe Zone</em>?"),
    "sub": ("개인정보 안심구역을 여러 성의 장부를 모아 보되 밖으로는 못 들고 나가는 특별 열람실 이야기로 풀어봤어요.",
            "A personal-data safe zone, told as a story about a special reading room where several castles' ledgers can be viewed together, but never carried out."),
    "panels": [
        {"svg": P1, "alt": ("두 성이 각자 장부를 들고 있는데, 가운데 '못 보내요' 표시와 함께 선이 막혀 있음", "Two castles each hold a ledger, with a blocked line between them marked can't send it"),
         "caption": ("각자 장부를 성 밖으로 못 들고 나가요.", "Neither castle's ledger may leave its own walls."),
         "small": ("합치면 더 좋은 답이 나오는데, 각자 성 안에 갇혀 있어요.", "Combining them would give a far better answer — but each stays locked inside its own castle.")},
        {"svg": P2, "alt": ("장부를 그냥 보내다가 가면 쓴 사람이 가로채고, 서기가 '그래서 아무도 안 보내줘요'라고 말함", "A ledger sent plainly is intercepted by a masked figure, while a clerk says so no one sends anything, ever"),
         "caption": ("그렇다고 그냥 보내주면 위험해요.", "But sending it over in the open is dangerous."),
         "small": ("결국 각자 성 안에서만 보다 보니 더 좋은 분석을 못 해요.", "So everyone stays locked inside their own castle, and the better analysis never happens.")},
        {"svg": P3, "hero": True, "alt": ("특별 열람실 안에 두 성의 장부가 모여 있고 분석가가 그 안에서만 보고, 요약 결과 쪽지만 경비를 통해 밖으로 나감", "Inside a special reading room, two castles' ledgers sit together; an analyst views them only inside, and only a summary slip is carried out past a guard"),
         "caption": ("안심구역은 장부를 한 방에 모아, 그 안에서만 보고, 결과만 들고 나가는 열람실이에요.", "A safe zone is a reading room where ledgers are gathered in one place, viewed only inside, with only the result ever carried out."),
         "small": ("장부 자체는 절대 그 방을 떠나지 않아요.", "The ledgers themselves never leave the room at all."),
         "tricks": (4, [
             (icon('<rect x="8" y="20" width="18" height="24" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="38" y="20" width="18" height="24" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M26 32 h12" stroke="var(--good)" stroke-width="3"/>'),
              ("여러 성의 장부를 한 방에", "Many castles' ledgers, one room"), ("결합해서 함께 봐요", "gathered and viewed together"), "calm"),
             (icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M20 20 L44 44 M44 20 L20 44" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'),
              ("그 안에서만 보고 계산", "Viewed and computed only inside"), ("반출은 원칙적으로 금지예요", "taking it out is forbidden"), "warm"),
             (icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 32 l7 7 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'),
              ("나갈 땐 검사", "Checked on the way out"), ("승인받은 결과만 반출돼요", "only approved results leave")),
             (icon('<circle cx="32" cy="22" r="10" fill="none" stroke="var(--accent)" stroke-width="4"/><rect x="18" y="36" width="28" height="18" rx="6" fill="var(--accent)"/>'),
              ("드나드는 사람도 기록", "Everyone who enters is logged"), ("출입통제와 로그로요", "access control and a log"), "calm"),
         ])},
        {"svg": P4, "alt": ("신청·승인·분석·반출심사 네 단계 절차표", "A four-step process: apply, approval, analyze, export review"),
         "caption": ("안심구역을 쓰려면 정해진 절차를 거쳐요.", "Using a safe zone follows a set process."),
         "small": ("신청하고, 승인받고, 방 안에서 분석하고, 나가기 전에 한 번 더 검사받아요.", "Apply, get approved, analyze inside the room, then undergo one more check before anything leaves.")},
        {"svg": P5, "alt": ("분석가가 땀을 흘리며 몇 주짜리 달력을 기다리고, 다른 결과는 '반출 불가' 도장이 찍힘", "A sweating analyst waits through a weeks-long calendar, while another result is stamped export denied"),
         "caption": ("승인이 오래 걸리고, 다 허락되진 않아요.", "Approval can take a long time, and not everything is allowed out."),
         "small": ('결과가 <a href="pseudonymize-ko.html">재식별</a>될 수 있으면 반출 자체가 거부돼요.',
                   'If the result could still be <a href="pseudonymize-en.html">re-identified</a>, the export is refused outright.')},
    ],
    "summary": (("<b>개인정보 안심구역</b> = 여러 기관의 데이터를 <b>한 방에 모아</b> 그 안에서만 분석하고, <b>결과만 승인받아 반출</b>하는 특별 열람실.",
                 "A <b>personal-data safe zone</b> = a special reading room where data from several organizations is <b>gathered in one place</b>, analyzed only inside, with <b>only approved results ever exported</b>."),
                ("데이터 안심구역은 여러 기관의 가명정보·결합정보를 물리적·논리적으로 통제된 공간에 모아 분석하되, 원본 데이터의 반출은 원천 차단하고 분석 결과만 재식별 위험 평가를 거쳐 반출을 허용하는 제도예요. 결합전문기관이 신청을 심사하고 결합을 수행하며, 반출심사위원회가 결과물의 재식별 가능성을 확인한 뒤에만 밖으로 나갈 수 있어요. 여러 기관의 데이터를 안전하게 활용하면서도 유출 위험을 최소화하는 것이 목적이에요.",
                 "A data safe zone gathers pseudonymized and linked data from multiple organizations into a physically and logically controlled space for analysis, while blocking the raw data from ever leaving and allowing only the analysis results out, after a re-identification risk review. A data linkage agency screens applications and performs the linkage, and an export review committee checks the results for re-identification risk before anything is released. The goal is to let organizations use combined data safely while keeping leak risk to a minimum.")),
    "glossary": [
        ("개인정보 안심구역", "Personal-data safe zone", ("특별 열람실.", "The special reading room."), ("여러 기관의 데이터를 모아 분석하되 원본은 못 나가는 통제된 공간이에요.", "A controlled space where data from several organizations is analyzed, but the raw data never leaves.")),
        ("결합전문기관", "Data linkage agency", ("여러 장부를 합치는 전담 기관.", "The dedicated agency that combines the ledgers."), ("신청을 심사하고 가명정보끼리의 결합을 전문적으로 수행해요.", "Screens applications and professionally performs the linkage between pseudonymized datasets.")),
        ("반출심사", "Export review", ("나갈 때 검사.", "The check on the way out."), ("결과가 재식별 위험이 없는지 반출심사위원회가 확인해요.", "An export review committee checks the result poses no re-identification risk.")),
        ("재식별 위험 평가", "Re-identification risk assessment", ("다시 알아낼 수 있는지 재기.", "Measuring whether the name can come back."), ('<a href="pseudonymize-ko.html">가명처리</a>된 데이터라도 결합되면 위험이 다시 커질 수 있어요.', 'Even <a href="pseudonymize-en.html">pseudonymized</a> data can grow risky again once combined.')),
        ("가명정보 결합", "Pseudonymized data linkage", ("번호표끼리 이어 붙이기.", "Stitching number tags together."), ("서로 다른 기관의 가명정보를 연결해 더 풍부한 분석을 가능하게 해요.", "Links pseudonymized records across organizations, enabling richer analysis.")),
        ("출입통제·접속기록", "Access control and logging", ("드나드는 사람 기록.", "A record of who comes and goes."), ('<a href="privacysafeguard-ko.html">손님 정보 창고 수칙</a>과 같은 원리예요.', 'The same principle as the <a href="privacysafeguard-en.html">guest-info storeroom rulebook</a>.')),
        ("안전한 데이터 활용", "Safe data utilization", ("가두고도 쓰는 법.", "Using data without letting it out."), ("데이터를 밖으로 꺼내지 않고도 가치를 뽑아내는 접근이에요.", "An approach that extracts value from data without ever taking it out of its room.")),
        ("개인정보 보호강화기술(PET)", "Privacy-enhancing technologies", ("도구상자.", "The toolbox."), ('안심구역 안에서도 PET를 같이 써서 위험을 더 줄여요. → <a href="pet-ko.html">손님을 지키는 여러 다른 도구상자</a>', 'PET tools are often used inside the safe zone too, to cut risk further. → <a href="pet-en.html">the toolbox with many different ways to protect a guest</a>')),
    ],
}
