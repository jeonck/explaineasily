from _draw import *
from _world import *

# 1. 문제: 창고 안에 뭐가 있는지 바깥 사람은 몰라요
P1 = svg(320, sky(320)
         + shelfzone(260, 140, 300, 100, 0.9, n=3)
         + person(620, 180, s=0.8, face=SWEAT + EYES, **DRIVER)
         + label(380, 90, "⟦이 창고 안에 뭐가 있는지 아무도 몰라요|nobody outside knows what's in this warehouse⟧", 12, "var(--bad)")
         + label(380, 280, "⟦문이 잠겨 있고, 안내문도 없어요|the door is locked, and there's no label either⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 공개해도 제각각 형식이면 못 써요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + receipt(220, 150, 0.8, text="⟦사진으로만|photo only⟧")
         + receipt(380, 150, 0.8, text="⟦손글씨 표|handwritten table⟧")
         + receipt(540, 150, 0.8, text="⟦PDF 문서|PDF document⟧")
         + label(380, 230, "⟦공개는 했지만 프로그램이 읽을 수 없어요|published, but no program can read it⟧", 12, "var(--bad)")
         + label(380, 270, "⟦형식이 제각각이면 다시 쓰기 어려워요|mismatched formats make reuse hard⟧", 13, "var(--ink)"))

# 3. hero: LOD/오픈 데이터 = 문을 열고, 표준 번호표를 달고, 끈으로 연결해 공개하는 것
OPEN_I = icon('<path d="M10 54 V10 h30 l10 10 v34 z" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M10 54 L54 44" stroke="var(--accent)" stroke-width="4"/>')
TABLE_I = icon('<rect x="10" y="14" width="44" height="36" fill="none" stroke="#2E8B57" stroke-width="3"/><path d="M10 28 h44 M10 42 h44 M32 14 v36" stroke="#2E8B57" stroke-width="2"/>')
URI_I = icon('<rect x="10" y="24" width="30" height="16" rx="8" fill="var(--accent)"/><circle cx="48" cy="32" r="10" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3"/>')
LINK_I = icon('<circle cx="16" cy="32" r="9" fill="var(--accent)"/><circle cx="48" cy="32" r="9" fill="var(--good)"/><path d="M25 32 h14" stroke="#8B5E3C" stroke-width="3"/>')

P3 = svg(340, sky(340)
         + person(220, 130, s=0.9, face=EYES, **MANAGER)
         + gate(150, 260, 0.55)
         + indexcard(460, 200, 0.8, tags=["URI"]) + indexcard(580, 200, 0.7, tags=["URI"])
         + person(680, 170, s=0.7, face=SMILE, **DRIVER)
         + label(380, 30, "⟦오픈 데이터/LOD = 문을 열고, 표준 번호표를 달고, 끈으로 연결해 공개하는 것|open data/LOD = opening the door, tagging with a standard ID, and linking it for anyone⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦누구나 와서 꺼내 쓸 수 있어요|anyone can come and reuse it⟧", 12, "var(--muted)"))

# 4. 오픈 데이터 성숙도 사다리 (4단계)
P4 = svg(320, sky(320, ground=False)
         + label(380, 30, "⟦공개 데이터가 좋아지는 네 단계|four steps toward better open data⟧", 14, "var(--ink)", cls="d")
         + receipt(160, 230, 0.55, text="⟦①사진/PDF|①photo/PDF⟧")
         + receipt(300, 190, 0.6, text="⟦②표로 정리|②as a table⟧")
         + receipt(460, 150, 0.65, text="⟦③CSV 같은 열린 형식|③open format like CSV⟧")
         + indexcard(620, 110, 0.8, tags=["URI"])
         + label(620, 70, "⟦④번호표 달고 서로 연결|④tagged and linked⟧", 11, "var(--muted)")
         + '<path d="M190 240 L270 210 M330 200 L420 170 M500 160 L580 130" stroke="var(--accent)" stroke-width="3" fill="none" stroke-dasharray="4 4"/>')

# 5. 한계: 공개한다고 품질까지 보장되진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + indexcard(190, 150, 1.0, tags=["URI"]) + label(190, 210, "⟦누구나 찾고 연결할 수 있어요|anyone can find and link it⟧", 11, "var(--ink)")
         + receipt(570, 150, 0.9, void=True) + label(570, 240, "⟦낡았거나 틀린 데이터일 수도 있어요|it might still be stale or wrong⟧", 11, "var(--ink)")
         + label(380, 280, "⟦공개는 형식의 문제지, 품질까지 보장하진 않아요|openness fixes format, not quality⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "lodopendata", "order": 5,
    "title": ("문을 열고 번호표를 달아 연결해두는 창고", "The Warehouse That Opens Its Door and Links Its Tags"),
    "h1": ("<em>LOD·오픈 데이터</em>가 뭐예요?", "What is <em>LOD & Open Data</em>?"),
    "sub": ("LOD(연계 공개 데이터)와 오픈 데이터를, 문을 열고 표준 번호표를 달아 서로 연결해두는 창고 이야기로 풀어봤어요.",
            "LOD (Linked Open Data) and open data, told as a story about a warehouse that opens its door and links its tags."),
    "panels": [
        {"svg": P1, "alt": ("배송 기사가 잠긴 창고 앞에서 안에 뭐가 있는지 몰라 진땀을 흘림", "A driver sweats outside a locked warehouse, not knowing what's inside"),
         "caption": ("이 창고 안에 뭐가 있는지 아무도 몰라요.", "Nobody outside knows what's in this warehouse."),
         "small": ("문이 잠겨 있고, 안내문도 없어요.", "The door is locked, and there's no label either.")},
        {"svg": P2, "alt": ("사진, 손글씨 표, PDF처럼 제각각 형식으로 공개된 전표들", "Receipts published in mismatched formats: photo, handwritten table, PDF"),
         "caption": ("공개는 했지만 프로그램이 읽을 수 없어요.", "Published, but no program can read it."),
         "small": ("형식이 제각각이면 다시 쓰기 어려워요.", "Mismatched formats make reuse hard.")},
        {"svg": P3, "hero": True, "alt": ("창고 관리자가 문을 열고, 번호표가 붙은 카드들이 서로 연결되어 배송 기사가 웃으며 찾아옴", "A manager opens the gate, tagged cards link to each other, and a driver smiles while finding one"),
         "caption": ("LOD/오픈 데이터 = 문을 열고, 표준 번호표를 달고, 끈으로 연결해 공개하는 것이에요.", "Open data/LOD opens the door, tags with a standard ID, and links it for anyone."),
         "small": ("누구나 와서 꺼내 쓸 수 있어요.", "Anyone can come and reuse it."),
         "tricks": (4, [
             (OPEN_I, ("문 열기", "Open the door"), ("누구나 볼 수 있게 공개해요", "make it visible to anyone"), "calm"),
             (TABLE_I, ("표로 정리하기", "Organize as a table"), ("구조를 갖춰요", "give it structure")),
             (URI_I, ("표준 번호표 달기", "Attach a standard tag"), ("프로그램 특정 형식에 안 묶여요", "not locked to one program's format"), "warm"),
             (LINK_I, ("다른 창고와 연결하기", "Link to other warehouses"), ("끈으로 이어 더 풍부해져요", "linked data becomes richer")),
         ])},
        {"svg": P4, "alt": ("사진/PDF에서 번호표가 붙어 서로 연결되는 데이터까지 좋아지는 네 단계", "Four steps from photo/PDF up to tagged, linked data"),
         "caption": ("공개 데이터는 이 네 단계를 거쳐 좋아져요.", "Open data improves through these four steps."),
         "small": ("마지막 단계가 바로 LOD(연계 공개 데이터)예요.", "The last step is exactly LOD (Linked Open Data)."),
        },
        {"svg": P5, "alt": ("왼쪽: 누구나 찾고 연결할 수 있음. 오른쪽: 무효 표시된 전표로 낡거나 틀린 데이터일 수 있음을 나타냄", "Left: anyone can find and link it. Right: a voided receipt shows it may still be stale or wrong"),
         "caption": ("공개한다고 품질까지 보장되진 않아요.", "Openness doesn't guarantee quality."),
         "small": ("공개는 형식의 문제지, 내용의 정확함을 보장하진 않아요.", "Openness fixes format, not the accuracy of the content.")},
    ],
    "summary": (("<b>오픈 데이터/LOD</b> = 창고 문을 <b>누구나 볼 수 있게 열고</b>, 상자에 <b>표준 번호표(URI)</b>를 달아 <b>다른 창고와 끈으로 연결</b>해 공개하는 것.",
                 "<b>Open data/LOD</b> opens the warehouse door to everyone, tags boxes with a <b>standard ID (URI)</b>, and <b>links them to other warehouses</b>."),
                ("오픈 데이터는 누구나 자유롭게 접근·재사용·재배포할 수 있게 공개한 데이터이고, LOD(Linked Open Data)는 팀 버너스리가 제안한 5성 등급 중 최상위 단계로, 데이터에 URI를 부여하고 RDF 등으로 다른 데이터와 링크를 맺어 '연결된 공개 데이터망'을 만드는 것이에요. 공개 여부와 품질·최신성은 별개의 문제예요.",
                 "Open data is data published so anyone can freely access, reuse, and redistribute it. LOD (Linked Open Data), the top tier of Tim Berners-Lee's 5-star model, assigns URIs to data and links it to other data via RDF, forming a connected web of open data. Publishing it openly is a separate matter from its quality or freshness.")),
    "glossary": [
        ("오픈 데이터", "Open Data", ("누구나 쓸 수 있게 연 창고.", "A warehouse opened for anyone to use."), ("라이선스까지 명확해야 진짜 오픈이에요.", "Real openness needs a clear license too.")),
        ("LOD(연계 공개 데이터)", "Linked Open Data", ("번호표를 달아 서로 연결한 창고.", "Warehouses tagged and linked to each other."), ("5성 등급 중 가장 높은 단계예요.", "The highest tier of the 5-star model.")),
        ("5성 등급", "5-Star Open Data", ("창고가 좋아지는 다섯 단계.", "Five steps a warehouse improves through."), ("별이 늘수록 재사용이 쉬워져요.", "More stars, easier reuse.")),
        ("URI", "URI", ("상자마다 달린 표준 번호표.", "The standard tag attached to every box."), ("프로그램이 서로 가리킬 수 있게 해요.", "Lets programs point to the same thing.")),
        ("RDF", "RDF", ("상자와 상자를 잇는 끈의 규칙.", "The rule for the string linking box to box."), ("주어-서술어-목적어 형태로 적어요.", "Written as subject–predicate–object.")),
        ("NoSQL 모델링", "NoSQL Modeling", ("상자 모양에 맞춰 선반을 바꾸는 창고.", "A warehouse reshaping shelves to fit each box."), ('그래프형 NoSQL은 연결 표현에 잘 맞아요. → <a href="nosqltype-ko.html">자유로운 선반 창고</a>', 'Graph-type NoSQL fits linked data well. → <a href="nosqltype-en.html">the free-shelf warehouse</a>')),
        ("정규화", "Normalization", ("선반 한 칸에 한 번만 적는 규칙.", "Writing shared info on one shelf once."), ('공개 데이터도 중복을 줄이면 더 다루기 쉬워요. → <a href="normalization-ko.html">한 칸에 한 번만 적는 규칙</a>', 'Open data is easier to manage with less duplication too. → <a href="normalization-en.html">the rule of writing it once</a>')),
        ("개인정보/프라이버시", "AI Privacy", ("공개 전에 가려야 하는 정보.", "Information that must be masked before publishing."), ('앵무새 세계의 다른 페이지에서 자세히 다뤄요. → <a href="aiprivacy-ko.html">AI 개인정보</a>', 'Covered in depth on another page in the parrot world. → <a href="aiprivacy-en.html">AI privacy</a>')),
    ],
}
