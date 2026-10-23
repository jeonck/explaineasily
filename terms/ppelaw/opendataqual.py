"""공공데이터 제공·품질."""
from _draw import *
from _world import *

OPEN_I = icon('<rect x="14" y="14" width="36" height="36" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 28 h20 M22 36 h20" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
FORMAT_I = icon('<rect x="10" y="14" width="44" height="36" rx="4" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M10 28 h44 M32 14 v36" stroke="var(--accent)" stroke-width="2"/>')
FRESH_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 20 v12 l10 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
FIX_I = icon('<rect x="14" y="16" width="36" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 40 l6 -20 M34 24 l6 16" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/><path d="M22 20 l4 4 l8 -9" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')

# 1. 학생회만 알고 안 알려줘요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=EYES, **STUDENT) + bubble(130, 70, 220, 44, "⟦급식표가 언제 바뀌는지 알 수 있어요?|can I find out when the lunch menu changes?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=EYES, **PRESIDENT) + bubble(470, 70, 220, 44, "⟦그건 저희만 보는 자료인데요|that's only on our own sheet⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦학생들이 알고 싶은 자료가 학생회 안에만 있어요|the information students want sits inside the council alone⟧", 13, "var(--ink)", cls="d"))

# 2. 정보 격차 — 소문으로 듣는 반, 못 듣는 반
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + person(220, 135, s=0.8, face=SMILE, **STUDENT) + label(220, 265, "⟦저흰 소문으로 들었어요|we heard it through the grapevine⟧", 11, "var(--ink)")
         + person(560, 135, s=0.8, face=FROWN, **STUDENT) + label(560, 265, "⟦저흰 전혀 몰랐어요|we had no idea at all⟧", 11, "var(--bad)")
         + label(380, 300, "⟦알리지 않으면, 듣는 반과 못 듣는 반 사이에 불공평이 생겨요|not announcing it creates unfairness between classes that hear and don't⟧", 12, "var(--ink)", cls="d"))

# 3. 공공데이터 제공·품질 = 누구나 보게 게시판에 공개하고 품질을 지키는 것 (hero)
P3 = svg(340, sky(340)
         + person(220, 140, s=0.9, face=SMILE, **REP)
         + noticeboard(360, 130, 1.6, "⟦급식표 / 동아리실 현황 / 행사 일정|lunch menu / club-room status / event schedule⟧")
         + person(620, 180, s=0.75, face=SMILE, **STUDENT)
         + label(380, 30, "⟦공공데이터 제공 = 누구나 볼 수 있게 게시판에 공개하는 것|public data provision = posting it where anyone can see⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦공개뿐 아니라 품질(최신·정확)도 같이 책임져요|not just posting it — keeping it fresh and accurate too⟧", 12, "var(--muted)"))

# 4. 품질 체크표 네 항목
P4 = svg(300, sky(300, ground=False)
         + rulesboard(60, 30, 640, 240, "⟦공공데이터 품질 체크표|PUBLIC DATA QUALITY CHECKLIST⟧",
                      ("⟦완전성 — 빠진 항목 없이|completeness — nothing missing⟧",
                       "⟦정확성 — 틀린 값 없이|accuracy — nothing wrong⟧",
                       "⟦일관성 — 다른 자료와 안 어긋나게|consistency — matches other records⟧",
                       "⟦적시성 — 최신 상태로|timeliness — kept up to date⟧"), 1.0)
         + label(380, 285, "⟦네 가지를 다 지켜야 '쓸 수 있는' 공개 데이터예요|all four together make data that's actually usable⟧", 12, "var(--ink)", cls="d"))

# 5. 공개했다고 다 쓸모 있는 건 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + noticeboard(190, 130, 1.1, "⟦제대로 공개됨|properly posted⟧")
         + person(570, 140, s=0.8, face=FROWN, **STUDENT) + '<rect x="552" y="100" width="36" height="46" rx="3" fill="#8B5E3C" opacity="0.5"/>' + label(570, 250, "⟦사진으로 찍어 올려서 못 읽어요|it's a photo of a page — can't even read it⟧", 11, "var(--bad)")
         + label(380, 285, "⟦게시했다고 끝이 아니에요 — 쓸 수 있는 형식과 품질관리가 계속 필요해요|posting it isn't the end — it still needs a usable format and ongoing quality care⟧", 11, "var(--muted)", cls="d"))

PAGE = {
    "slug": "opendataqual", "order": 8,
    "title": ("공지 게시판에 다 보이게 붙이기", "Posting It All Where Everyone Can See"),
    "h1": ("<em>공공데이터 제공과 품질</em>이 뭐예요?", "What is <em>Public Data Provision & Quality</em>?"),
    "sub": ("공공데이터 제공과 품질관리를, 학생회가 게시판에 자료를 공개하고 계속 돌보는 이야기로 풀어봤어요.",
            "Public data provision and quality management, told as a story about the student council posting data on the board and keeping it in shape."),
    "panels": [
        {"svg": P1, "alt": ("학생이 급식표 변경을 묻자 학생회장이 그건 우리만 보는 자료라고 답함", "A student asks about a lunch-menu change; the president says it's only on the council's own sheet"),
         "caption": ("학생들이 알고 싶은 자료가 학생회 안에만 있어요.", "The information students want sits inside the council alone."),
         "small": ("물어봐야만 알 수 있는 자료는 공개된 게 아니에요.", "Data you can only learn by asking isn't truly open.")},
        {"svg": P2, "alt": ("한 반은 소문으로 듣고, 다른 반은 전혀 모름", "One class hears it through rumor; another has no idea at all"),
         "caption": ("정보 격차가 생겨요 — 소문으로 듣는 반, 못 듣는 반.", "An information gap opens up — classes that hear, and classes that don't."),
         "small": ("알리지 않으면, 듣는 반과 못 듣는 반 사이에 불공평이 생겨요.", "Not announcing it creates unfairness between classes that hear and don't.")},
        {"svg": P3, "hero": True, "alt": ("대표가 급식표·동아리실 현황·행사 일정을 게시판에 공개하고 학생이 와서 봄", "A rep posts the lunch menu, club-room status, and event schedule on the board, and a student comes to check it"),
         "caption": ("공공데이터 제공은 누구나 볼 수 있게 게시판에 공개하는 거예요.", "Public data provision means posting it where anyone can see."),
         "small": ("공개뿐 아니라 품질(최신·정확)도 같이 책임져요.", "Not just posting it — keeping it fresh and accurate too."),
         "tricks": (4, [
             (OPEN_I, ("누구나 보게 공개하기", "Open it to everyone"), ("물어보지 않아도 보여요", "no need to ask to see it"), "calm"),
             (FORMAT_I, ("다시 쓰기 쉬운 형식으로", "Use a reusable format"), ("표 형식 등 공통 양식으로", "a common format like a table")),
             (FRESH_I, ("최신 상태로 유지", "Keep it current"), ("바뀌면 바로 고쳐요", "update it the moment it changes"), "warm"),
             (FIX_I, ("틀린 자료 바로잡기", "Fix wrong entries"), ("정확성을 계속 점검해요", "quality is checked continuously")),
         ])},
        {"svg": P4, "alt": ("완전성·정확성·일관성·적시성 네 항목으로 된 공공데이터 품질 체크표", "A public-data quality checklist with four rows: completeness, accuracy, consistency, timeliness"),
         "caption": ("품질은 이 네 가지로 점검해요.", "Quality is checked against these four things."),
         "small": ("네 가지를 다 지켜야 '쓸 수 있는' 공개 데이터예요.", "All four together make data that's actually usable.")},
        {"svg": P5, "alt": ("왼쪽: 제대로 공개된 게시판. 오른쪽: 사진으로 찍어 올려 읽을 수 없는 자료에 불만인 학생", "Left: a properly posted board. Right: a student frustrated that a posting is just an unreadable photo"),
         "caption": ("공개했다고 다 쓸모 있는 건 아니에요.", "Posting it doesn't automatically make it useful."),
         "small": ("게시했다고 끝이 아니에요 — 쓸 수 있는 형식과 품질관리가 계속 필요해요.", "Posting it isn't the end — it still needs a usable format and ongoing quality care.")},
    ],
    "summary": (("<b>공공데이터 제공·품질</b> = 누구나 볼 수 있게 <b>게시판에 공개</b>하고, <b>완전성·정확성·일관성·적시성</b>을 계속 챙기는 것.",
                 "<b>Public data provision & quality</b> = <b>posting data where anyone can see it</b>, and continuing to look after its <b>completeness, accuracy, consistency, and timeliness</b>."),
                ("공공데이터법은 공공기관이 보유한 데이터를 기계 판독이 가능한 형태로, 누구나 자유롭게 이용·재배포할 수 있도록 개방하게 해요. 단순 공개를 넘어, 완전성·정확성·일관성·적시성 같은 품질지표와 메타데이터 등록까지 함께 관리해야 실제로 활용 가능한 공공데이터가 돼요.",
                 "Public data law requires public agencies to publish the data they hold in a machine-readable form, open for anyone to freely use and redistribute. Beyond simply publishing it, quality indicators such as completeness, accuracy, consistency, and timeliness, along with registered metadata, have to be managed too for the data to actually be usable.")),
    "glossary": [
        ("공공데이터", "Public Data", ("공공기관이 가진, 공개해야 하는 자료.", "Data a public agency holds that must be published."), ("법으로 공개 의무가 정해져 있어요.", "Publishing it is a legal obligation.")),
        ("완전성", "Completeness", ("빠진 항목 없이 다 있는 것.", "Nothing is missing from the record."), ("품질 체크표의 첫 번째 항목이에요.", "The first row on the quality checklist.")),
        ("정확성", "Accuracy", ("틀린 값이 없는 것.", "Nothing in it is wrong."), ("틀리면 믿고 쓸 수가 없어요.", "If it's wrong, nobody can rely on it.")),
        ("적시성", "Timeliness", ("바뀌면 바로 고쳐 최신으로 두는 것.", "Updating it the moment something changes."), ("낡은 자료는 공개해도 쓸모가 줄어요.", "Stale data loses its usefulness even if it's public.")),
        ("메타데이터", "Metadata", ("자료에 대해 설명해두는 꼬리표.", "The tag that explains what the data is."), ("없으면 자료를 찾기도 이해하기도 어려워요.", "Without it, data is hard to find or understand.")),
        ("개방형 표준 형식", "Open Standard Format", ("누구나 읽을 수 있는 공통 형식.", "A common format anyone can read."), ("사진이나 PDF 스캔본은 다시 쓰기 어려워요.", "A scanned photo or PDF is hard to reuse.")),
        ("품질관리 진단", "Quality Diagnosis", ("공개한 자료를 주기적으로 점검하는 제도.", "A system that periodically checks published data."), ("공개 이후에도 계속 돌봐야 해요.", "Data needs ongoing care even after it's published.")),
        ("LOD(연계 공개 데이터)", "Linked Open Data", ("자료에 번호표를 달아 서로 연결하는 기술.", "Tagging data with IDs and linking records together."), ('형식·연결 기술은 다른 세계에서 자세히 다뤄요. → <a href="lodopendata-ko.html">문을 열고 번호표를 달아 연결해두는 창고</a>', 'The format and linking technique are covered in depth in another world. → <a href="lodopendata-en.html">the warehouse that opens its door and links its tags</a>')),
    ],
}
