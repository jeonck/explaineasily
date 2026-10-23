from _draw import *
from _world import *

# 1. 입주사마다 보관하고 싶은 게 다 달라요
P1 = svg(320, sky(320)
         + person(140, 170, s=0.7, face=EYES, **TENANT) + label(140, 280, "⟦벽돌 자재|raw brick⟧", 11, "var(--muted)")
         + person(380, 170, s=0.7, face=EYES, **TENANT) + label(380, 280, "⟦서류 폴더|paper folders⟧", 11, "var(--muted)")
         + person(620, 170, s=0.7, face=EYES, **TENANT) + label(620, 280, "⟦태그 붙은 박스|tagged boxes⟧", 11, "var(--muted)")
         + label(380, 302, "⟦입주사마다 보관하고 싶은 형태가 다 달라요|every tenant wants to store things in a different shape⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 한 가지 보관 방식만 있으면 누군가는 불편해요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + '<rect x="320" y="90" width="120" height="100" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(380, 145, "⟦서류 폴더함만|only paper folders⟧", 11, "var(--ink)")
         + person(220, 178, s=0.6, face=FROWN, **TENANT) + label(220, 280, "⟦벽돌은 폴더에 안 들어가요|bricks don't fit in a folder⟧", 10, "var(--bad)")
         + person(560, 178, s=0.6, face=FROWN, **TENANT) + label(560, 280, "⟦박스 태그도 못 붙여요|can't even tag a box here⟧", 10, "var(--bad)")
         + label(380, 302, "⟦한 가지 방식만 있으면 누군가의 짐은 늘 안 맞아요|with only one storage shape, somebody's stuff never fits⟧", 12, "var(--ink)"))

# 3. hero: 블록=벽돌 자재, 파일=폴더 트리, 오브젝트=태그 붙은 박스 창고
P3 = svg(365, sky(365)
         + '<rect x="60" y="230" width="18" height="18" fill="var(--stone-dark)"/><rect x="82" y="230" width="18" height="18" fill="var(--stone-dark)"/><rect x="60" y="252" width="18" height="18" fill="var(--stone-dark)"/><rect x="82" y="252" width="18" height="18" fill="var(--stone-dark)"/>'
         + label(90, 300, "⟦블록: 벽돌 자재|block: raw bricks⟧", 11, "var(--ink)")
         + '<rect x="290" y="210" width="110" height="90" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M320 230 h50 M320 250 h50 M320 270 h30" stroke="#142033" stroke-width="2"/>'
         + label(345, 320, "⟦파일: 폴더 트리|file: folder tree⟧", 11, "var(--ink)")
         + '<rect x="500" y="220" width="40" height="30" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="550" y="235" width="40" height="30" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="525" y="260" width="40" height="30" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
         + label(555, 320, "⟦오브젝트: 태그 붙은 박스|object: tagged boxes⟧", 11, "var(--ink)")
         + label(380, 30, "⟦블록=벽돌, 파일=폴더 트리, 오브젝트=태그 붙은 박스예요|block=bricks, file=folder tree, object=tagged boxes⟧", 13, "var(--ink)", cls="d")
         + label(380, 350, "⟦셋 다 '어떻게 저장하고 꺼내나'의 방식이 달라요|all three differ in HOW things get stored and retrieved⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 구조·접근방식·확장성·용도 비교
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦블록 vs 파일 vs 오브젝트|block vs file vs object⟧",
                     ("⟦구조: 벽돌 조각 vs 폴더 트리 vs 태그 붙은 박스|structure: raw bricks vs folder tree vs tagged boxes⟧",
                      "⟦접근: 가장 빠름 vs 사람에게 익숙함 vs API로 조회|access: fastest vs human-familiar vs via API lookup⟧",
                      "⟦확장성: 보통 vs 보통 vs 무제한에 가까움|scalability: moderate vs moderate vs near-unlimited⟧",
                      "⟦대표 용도: 데이터베이스 vs 공유 문서 vs 사진·백업·로그|typical use: databases vs shared docs vs photos, backups, logs⟧"), 1.0))

# 5. 깨지는 곳: 오브젝트는 박스 하나를 통째로 바꿔야 해서, 일부만 살짝 고치는 덴 느려요
P5 = svg(320, sky(320)
         + '<rect x="130" y="170" width="40" height="30" rx="3" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
         + person(230, 178, s=0.6, face=SWEAT, **TENANT)
         + label(190, 285, "⟦박스 하나를 통째로 다시 보내야 해요|has to resend the whole box, just for one tweak⟧", 11, "var(--ink)")
         + '<rect x="500" y="180" width="18" height="18" fill="var(--stone-dark)"/>' + person(600, 178, s=0.6, face=SMILE, **TENANT)
         + label(570, 285, "⟦벽돌(블록)은 한 조각만 바꿔도 빨라요|a block lets you swap just one brick, quickly⟧", 11, "var(--ink)"))

RAW_I = icon('<rect x="10" y="30" width="18" height="18" fill="var(--stone-dark)"/><rect x="34" y="30" width="18" height="18" fill="var(--stone-dark)"/><rect x="10" y="12" width="18" height="18" fill="var(--stone-dark)"/>')
TREE_I = icon('<path d="M32 10 v18 M20 44 L32 28 L44 44" stroke="#8B5E3C" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
TAG_I = icon('<path d="M12 12 L36 12 L52 28 L36 44 L12 44 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><circle cx="24" cy="28" r="3" fill="var(--accent)"/>')
SCALE_I = icon('<circle cx="20" cy="44" r="8" fill="var(--good)"/><circle cx="36" cy="30" r="8" fill="var(--good)"/><circle cx="52" cy="16" r="8" fill="var(--good)"/>')

PAGE = {
    "slug": "storagetype", "order": 9,
    "title": ("벽돌, 폴더 트리, 태그 붙은 박스", "Bricks, a Folder Tree, and Tagged Boxes"),
    "h1": ("<em>블록·파일·오브젝트 스토리지</em>가 뭐예요?", "What are <em>Block, File, and Object Storage</em>?"),
    "sub": ("블록·파일·오브젝트 스토리지를, 벽돌 자재·폴더 트리·태그 붙은 박스 창고의 차이로 풀어봤어요.",
            "Block, file, and object storage, told as the difference between raw bricks, a folder tree, and a warehouse of tagged boxes."),
    "panels": [
        {"svg": P1, "alt": ("입주사 셋이 각각 벽돌 자재, 서류 폴더, 태그 붙은 박스를 들고 서 있음", "Three tenants stand holding raw bricks, paper folders, and tagged boxes respectively"),
         "caption": ("입주사마다 보관하고 싶은 형태가 다 달라요.", "Every tenant wants to store things in a different shape."),
         "small": ("벽돌, 폴더, 박스 — 다 다른 모양이에요.", "Bricks, folders, boxes — all different shapes.")},
        {"svg": P2, "alt": ("서류 폴더함만 있는 공간에서 벽돌 든 사람과 박스 든 사람이 각각 안 맞는다고 불평함", "In a space with only paper-folder filing, one tenant holding bricks and another holding a box both complain things don't fit"),
         "caption": ("한 가지 방식만 있으면 누군가의 짐은 늘 안 맞아요.", "With only one storage shape, somebody's stuff never fits."),
         "small": ("벽돌도, 박스 태그도 여기선 안 통해요.", "Neither bricks nor box tags work here.")},
        {"svg": P3, "hero": True, "alt": ("벽돌 더미, 폴더 트리가 그려진 자료함, 태그 붙은 박스 더미가 나란히 놓여 있음", "A pile of bricks, a filing cabinet with a folder tree drawn on it, and a pile of tagged boxes sit side by side"),
         "caption": ("블록=벽돌, 파일=폴더 트리, 오브젝트=태그 붙은 박스예요.", "Block=bricks, file=folder tree, object=tagged boxes."),
         "small": ("셋 다 저장하고 꺼내는 방식이 달라요.", "All three differ in how things get stored and retrieved."),
         "tricks": (4, [
             (RAW_I, ("블록 = 벽돌 조각", "Block = raw bricks"), ("가장 날것이고 가장 빨라요", "the rawest, and the fastest"), "calm"),
             (TREE_I, ("파일 = 폴더 트리", "File = a folder tree"), ("사람에게 가장 익숙해요", "most familiar to people")),
             (TAG_I, ("오브젝트 = 태그 붙은 박스", "Object = tagged boxes"), ("API로 태그를 조회해 찾아요", "found by querying tags via an API"), "warm"),
             (SCALE_I, ("오브젝트는 거의 무제한으로 쌓여요", "Object storage piles up almost without limit"), ("창고가 끝없이 늘어나요", "the warehouse just keeps growing")),
         ])},
        {"svg": P4, "alt": ("구조·접근 방식·확장성·대표 용도를 블록·파일·오브젝트로 비교한 안내판", "A board comparing block, file, and object storage on structure, access, scalability, and typical use"),
         "caption": ("네 가지 기준에서 성격이 다 갈려요.", "They differ on all four measures."),
         "small": ("쓰임새가 뚜렷이 갈려요 — DB엔 블록, 공유문서엔 파일, 사진·백업엔 오브젝트.", "Use cases split clearly — block for databases, file for shared docs, object for photos and backups.")},
        {"svg": P5, "alt": ("오른쪽: 벽돌(블록)은 한 조각만 바꿔도 빨라 웃는 사람. 왼쪽: 박스(오브젝트)는 통째로 다시 보내야 해서 땀 흘리는 사람", "Right: swapping just one brick (block) is quick, tenant smiling. Left: a box (object) has to be resent whole, tenant sweating"),
         "caption": ("오브젝트는 박스 하나를 통째로 바꿔야 해서 느려요.", "Object storage is slow because the whole box has to be resent."),
         "small": ("블록은 한 조각만 바꿔도 빨라요.", "Block storage lets you swap just one piece, quickly.")},
    ],
    "summary": (("<b>블록</b> = 벽돌 조각(가장 빠르고 날것). <b>파일</b> = 폴더 트리(사람에게 익숙). <b>오브젝트</b> = 태그 붙은 박스(무한 확장, 메타데이터로 조회).",
                 "<b>Block</b> is raw bricks (fast, unstructured). <b>File</b> is a folder tree (familiar to people). <b>Object</b> is tagged boxes (near-infinite scale, found by metadata)."),
                ("블록 스토리지는 고정 크기 블록 단위로 접근해 DB처럼 빠른 입출력이 필요한 곳에 쓰이고, 파일 스토리지는 디렉터리·파일 계층 구조로 사람이 다루기 쉬워요. 오브젝트 스토리지는 파일을 메타데이터·고유 ID가 붙은 객체로 저장해 API로 조회하며, 수평 확장이 거의 무제한이라 사진·백업·로그 같은 비정형 대용량 데이터에 적합해요. 다만 객체는 일부만 수정하는 덴 비효율적이에요.",
                 "Block storage is accessed in fixed-size chunks, suited to fast I/O like databases. File storage uses a directory/file hierarchy that's easy for people to navigate. Object storage keeps data as objects tagged with metadata and a unique ID, queried via an API, with near-unlimited horizontal scale — ideal for unstructured bulk data like photos, backups, and logs. But objects are inefficient to partially modify.")),
    "glossary": [
        ("블록 스토리지", "Block storage", ("벽돌처럼 조각난 저장 단위.", "Storage carved into brick-like chunks."), ("가장 빠르지만 날것 그대로예요.", "Fastest, but completely unstructured.")),
        ("파일 스토리지", "File storage", ("폴더 트리처럼 정리된 저장 방식.", "Storage organized like a folder tree."), ("사람이 다루기 가장 익숙해요.", "Most familiar for a person to navigate.")),
        ("오브젝트 스토리지", "Object storage", ("태그(메타데이터) 붙은 박스 창고.", "A warehouse of boxes tagged with metadata."), ("API로 태그를 조회해 찾아요.", "Found by querying tags via an API.")),
        ("메타데이터", "Metadata", ("박스에 붙이는 태그.", "The tag attached to the box."), ("오브젝트를 찾는 열쇠예요.", "The key used to find an object.")),
        ("DAS/NAS/SAN", "DAS / NAS / SAN", ("연결 방식과 나눠쓰는 범위의 차이.", "A difference in connection method and sharing scope."), ('이건 다른 축이에요 — 데이터 모양이 아니라 연결 방식 이야기예요. → <a href="dasnassan-ko.html">내 서랍, 공용 자료실, 전용 창고망</a>', "A different axis — connection method, not data shape. → <a href=\"dasnassan-en.html\">my drawer, the shared file room, the dedicated network</a>")),
        ("수평 확장", "Horizontal scaling", ("창고를 옆으로 계속 늘리는 것.", "Adding more warehouse space sideways, endlessly."), ("오브젝트 스토리지가 이 방식으로 거의 무제한 늘어나요.", "This is how object storage scales almost without limit.")),
        ("백업", "Backup", ("자료 사본을 따로 하나 더 두는 일.", "Keeping one more copy of the data elsewhere."), ("오브젝트 스토리지가 자주 쓰이는 용도예요.", "A common use case for object storage.")),
        ("클라우드 서비스 모델", "Cloud service model", ("뼈대만/인테리어까지/완제품.", "Bare shell / interior done / move-in ready."), ('어느 모델을 빌리든 이 세 저장 방식 중 하나를 골라요. → <a href="cloudmodel-ko.html">셋 중 골라 빌리기</a>', 'Whichever model you rent, you still pick one of these three. → <a href="cloudmodel-en.html">pick one to rent</a>')),
    ],
}
