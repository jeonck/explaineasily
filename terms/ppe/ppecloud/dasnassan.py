from _draw import *
from _world import *

# 1. 서류함이 꽉 찼어요 — 어디에 더 보관할까요?
P1 = svg(300, sky(300)
         + office(260, 160, 1.0, label_text="⟦내 사무실|my office⟧")
         + person(430, 198, s=0.8, face=FROWN + SWEAT, **TENANT)
         + bubble(480, 70, 260, 60, "⟦서류함이 꽉 찼어요, 어디에 더 보관하죠?|the filing cabinet is full — where do I put more?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦각자 책상 서랍만으론 보관이 금방 한계예요|each desk's own drawer runs out of room fast⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 사무실마다 따로 보관하면 중복되고 나눠 쓰기 힘들어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + office(140, 90, 0.8) + office(340, 90, 0.8) + office(540, 90, 0.8)
         + label(180, 210, "⟦같은 서류 복사본|same doc, copied⟧", 10, "var(--bad)")
         + label(380, 210, "⟦같은 서류 복사본|same doc, copied⟧", 10, "var(--bad)")
         + label(580, 210, "⟦같은 서류 복사본|same doc, copied⟧", 10, "var(--bad)")
         + label(380, 262, "⟦사무실마다 따로 보관하면 중복되고, 서로 꺼내 보기도 힘들어요|store separately in each office, and you get duplicates nobody can easily share⟧", 12, "var(--ink)"))

# 3. hero: DAS=책상서랍, NAS=건물공용자료실, SAN=건물전용창고망
P3 = svg(360, sky(360)
         + '<rect x="40" y="220" width="70" height="50" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(75, 300, "⟦DAS: 내 책상 서랍|DAS: my own desk drawer⟧", 11, "var(--ink)")
         + '<rect x="220" y="190" width="110" height="90" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>' + label(275, 300, "⟦NAS: 건물 공용 자료실|NAS: the building's shared file room⟧", 11, "var(--ink)")
         + '<rect x="440" y="170" width="140" height="110" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="4"/>' + label(510, 300, "⟦SAN: 건물 전용 창고망|SAN: the building's dedicated storage network⟧", 11, "var(--ink)")
         + person(680, 262, s=0.7, face=EYES, **MANAGER)
         + label(380, 30, "⟦DAS=내 서랍, NAS=공용 자료실, SAN=전용 창고망이에요|DAS=my drawer, NAS=shared file room, SAN=dedicated storage network⟧", 13, "var(--ink)", cls="d")
         + label(380, 340, "⟦연결 방식과 나눠쓰는 범위가 셋 다 달라요|how they connect, and how widely they're shared, differ all three⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 연결방식·공유범위·속도 비교
P4 = svg(320, sky(320)
         + floorplan(60, 20, 640, 280, "⟦DAS vs NAS vs SAN|DAS vs NAS vs SAN⟧",
                     ("⟦DAS: 내 책상에 직접 연결, 혼자만 써요|DAS: plugs directly into my desk, mine alone⟧",
                      "⟦NAS: 복도망으로 연결, 여러 사무실이 파일 단위로 나눠 써요|NAS: connects over the hallway network, shared file-by-file⟧",
                      "⟦SAN: 건물 전용망으로 연결, 블록 단위라 더 빠르고 비싸요|SAN: a dedicated building network, block-level — faster, pricier⟧",
                      "⟦나눠쓰는 범위가 넓을수록 관리도 복잡해져요|the wider the sharing, the more complex the upkeep⟧"), 1.0))

# 5. 깨지는 곳: 작은 사무실엔 전용 창고망(SAN)이 오히려 과해요
P5 = svg(365, '<rect width="380" height="365" fill="var(--good-soft)"/><rect x="380" width="380" height="365" fill="var(--accent-soft)"/>'
         + office(100, 190, 0.8) + person(60, 268, s=0.55, face=SMILE, **TENANT)
         + label(190, 345, "⟦작은 사무실엔 책상 서랍(DAS)으로 충분해요|a small office does fine with just a desk drawer (DAS)⟧", 11, "var(--ink)")
         + '<rect x="460" y="170" width="140" height="110" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="4"/>' + person(650, 278, s=0.55, face=FROWN + SWEAT, **TENANT)
         + label(570, 345, "⟦전용 창고망(SAN)은 설치·관리가 복잡하고 비싸요|a dedicated storage network (SAN) is complex and costly to run⟧", 11, "var(--ink)"))

PLUG_I = icon('<rect x="10" y="20" width="44" height="24" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M4 32 h6" stroke="#C9A86A" stroke-width="4"/>')
SHARE_I = icon('<circle cx="20" cy="32" r="10" fill="var(--good)"/><circle cx="44" cy="20" r="8" fill="var(--good)"/><circle cx="44" cy="44" r="8" fill="var(--good)"/><path d="M28 32 L38 22 M28 32 L38 42" stroke="var(--good)" stroke-width="3"/>')
BLOCK_I = icon('<rect x="10" y="10" width="18" height="18" fill="var(--accent)"/><rect x="36" y="10" width="18" height="18" fill="var(--accent)"/><rect x="10" y="36" width="18" height="18" fill="var(--accent)"/><rect x="36" y="36" width="18" height="18" fill="var(--accent)"/>')
COST_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="4"/><text x="32" y="40" font-size="22" font-weight="800" text-anchor="middle" fill="var(--bad)">₩</text>')

PAGE = {
    "slug": "dasnassan", "order": 7,
    "title": ("내 서랍, 공용 자료실, 전용 창고망", "My Drawer, the Shared File Room, the Dedicated Warehouse Network"),
    "h1": ("<em>DAS/NAS/SAN</em>이 뭐예요?", "What are <em>DAS / NAS / SAN</em>?"),
    "sub": ("DAS/NAS/SAN 스토리지를, 내 책상 서랍·건물 공용 자료실·건물 전용 창고망의 차이로 풀어봤어요.",
            "DAS, NAS, and SAN storage, told as the difference between my own desk drawer, the building's shared file room, and its dedicated storage network."),
    "panels": [
        {"svg": P1, "alt": ("서류함이 꽉 차서 땀 흘리는 입주사가 어디에 더 보관할지 묻는 말풍선을 띄움", "A sweating tenant with a full filing cabinet asks where to store more"),
         "caption": ("각자 책상 서랍만으론 보관이 금방 한계예요.", "Each desk's own drawer runs out of room fast."),
         "small": ("더 보관할 곳이 필요해요.", "Somewhere else to store things is needed.")},
        {"svg": P2, "alt": ("사무실 세 곳이 각각 같은 서류 복사본을 따로 보관하고 있음", "Three separate offices each storing their own copy of the same document"),
         "caption": ("사무실마다 따로 보관하면 중복되고 나누기 힘들어요.", "Store separately in each office, and you get duplicates nobody can easily share."),
         "small": ("나눠 쓸 방법이 필요해요.", "There needs to be a way to share it.")},
        {"svg": P3, "hero": True, "alt": ("내 책상 서랍, 건물 공용 자료실, 건물 전용 창고망 세 가지 보관 방식이 크기 순으로 나란히 있고 관리사무소 직원이 지켜봄", "Three storage options side by side by size: my desk drawer, the building's shared file room, and its dedicated storage network, watched by a manager"),
         "caption": ("DAS=내 서랍, NAS=공용 자료실, SAN=전용 창고망이에요.", "DAS=my drawer, NAS=shared file room, SAN=dedicated storage network."),
         "small": ("연결 방식과 나눠쓰는 범위가 셋 다 달라요.", "How they connect, and how widely they're shared, differ all three."),
         "tricks": (4, [
             (PLUG_I, ("DAS는 내 책상에 직접 꽂아요", "DAS plugs directly into my own desk"), ("혼자만 쓸 수 있어요", "mine alone to use"), "calm"),
             (SHARE_I, ("NAS는 복도망으로 나눠 써요", "NAS shares over the hallway network"), ("파일 단위로 여러 사무실이 써요", "file-by-file, across offices")),
             (BLOCK_I, ("SAN은 전용망, 블록 단위예요", "SAN uses a dedicated network, block-level"), ("더 빠르지만 비싸요", "faster, but pricier"), "warm"),
             (COST_I, ("나눠쓸수록 관리도 복잡해져요", "Wider sharing means more upkeep"), ("비용도 같이 올라가요", "and cost climbs with it")),
         ])},
        {"svg": P4, "alt": ("안내판: DAS는 직접 연결로 혼자, NAS는 복도망으로 파일 단위 공유, SAN은 전용망으로 블록 단위, 공유 범위가 넓을수록 관리가 복잡해짐", "A board: DAS connects directly for one user, NAS shares files over the hallway network, SAN uses a dedicated block-level network, and wider sharing means more upkeep"),
         "caption": ("연결 방식과 공유 범위로 세 가지가 갈려요.", "Connection method and sharing scope split the three apart."),
         "small": ("속도·비용·공유범위가 함께 움직여요.", "Speed, cost, and sharing scope move together.")},
        {"svg": P5, "alt": ("왼쪽: 작은 사무실은 책상 서랍(DAS)으로 충분해 웃음. 오른쪽: 전용 창고망(SAN)은 설치·관리가 복잡하고 비싸 땀 흘림", "Left: a small office is fine with just a desk drawer (DAS), tenant smiling. Right: a dedicated storage network (SAN) is complex and costly, tenant sweating"),
         "caption": ("작은 사무실엔 전용 창고망(SAN)이 오히려 과해요.", "A dedicated storage network (SAN) is overkill for a small office."),
         "small": ("규모에 맞는 걸 고르는 게 중요해요.", "Picking the one that fits the scale matters.")},
    ],
    "summary": (("<b>DAS</b> = 내 책상에 <b>직접 연결</b>된 서랍(혼자 사용). <b>NAS</b> = 복도망으로 연결된 <b>건물 공용 자료실</b>(파일 단위 공유). <b>SAN</b> = <b>건물 전용 창고망</b>(블록 단위, 빠르고 비쌈).",
                 "<b>DAS</b> is a drawer <b>plugged directly</b> into my own desk (just for me). <b>NAS</b> is the <b>building's shared file room</b>, reached over the hallway network (shared file-by-file). <b>SAN</b> is the <b>building's dedicated storage network</b> (block-level, fast, and pricey)."),
                ("DAS(Direct Attached Storage)는 서버에 직접 연결되는 저장장치, NAS(Network Attached Storage)는 일반 네트워크로 연결해 파일 단위로 여러 서버가 공유하는 저장장치, SAN(Storage Area Network)은 전용 고속 네트워크로 연결해 블록 단위로 접근하는 저장 전용망이에요. 공유 범위와 속도·비용이 DAS < NAS < SAN 순으로 커져요.",
                 "DAS (Direct Attached Storage) connects straight to one server. NAS (Network Attached Storage) connects over a regular network and shares files across multiple servers. SAN (Storage Area Network) uses a dedicated high-speed network for block-level access. Sharing scope, speed, and cost all increase in the order DAS < NAS < SAN.")),
    "glossary": [
        ("DAS", "DAS (Direct Attached Storage)", ("내 책상에 직접 연결된 서랍.", "A drawer plugged directly into my own desk."), ("혼자만 쓸 수 있어요.", "Mine alone to use.")),
        ("NAS", "NAS (Network Attached Storage)", ("복도망으로 연결된 건물 공용 자료실.", "The building's shared file room, over the hallway network."), ("파일 단위로 여러 사무실이 나눠 써요.", "Shared file-by-file across offices.")),
        ("SAN", "SAN (Storage Area Network)", ("건물 전용 고속 창고망.", "The building's dedicated high-speed storage network."), ("블록 단위라 더 빠르지만 더 비싸요.", "Block-level — faster, but pricier.")),
        ("블록 스토리지", "Block storage", ("벽돌처럼 조각난 저장 단위.", "Storage carved into brick-like chunks."), ('더 자세한 비교는 다른 페이지에서 다뤄요. → <a href="storagetype-ko.html">블록·파일·오브젝트</a>', 'Covered in more depth on another page. → <a href="storagetype-en.html">block, file, object</a>')),
        ("파일 스토리지", "File storage", ("폴더 트리처럼 정리된 저장 방식.", "Storage organized like a folder tree."), ("NAS가 쓰는 방식이에요.", "The style NAS uses.")),
        ("네트워크 대역폭", "Network bandwidth", ("복도망이 한 번에 나를 수 있는 양.", "How much the hallway network can carry at once."), ("NAS·SAN 속도에 직접 영향을 줘요.", "Directly affects NAS and SAN speed.")),
        ("클라우드 스토리지", "Cloud storage", ("건물 전체가 대신 보관해 주는 서비스.", "The building itself storing things for you."), ("DAS/NAS/SAN 중 무엇이든 그 바탕이 될 수 있어요.", "Any of DAS, NAS, or SAN can sit underneath it.")),
        ("백업", "Backup", ("자료실 사본을 따로 하나 더 두는 일.", "Keeping one more copy of the file room elsewhere."), ("공유 범위가 넓을수록 백업도 더 중요해져요.", "The wider the sharing, the more backup matters.")),
    ],
}
