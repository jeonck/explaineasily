from _draw import *
from _world import *

# 1. 창고 하나에 전국 요청이 다 몰려요
P1 = svg(300, sky(300)
         + shelfzone(280, 120, 200, 90, 1.1)
         + person(160, 160, s=0.75, face=SWEAT + EYES, **DRIVER)
         + person(600, 160, s=0.75, face=SWEAT + EYES, **DRIVER)
         + label(380, 250, "⟦전국 모든 주문이 창고 하나로만 몰려요|every order nationwide piles onto one single warehouse⟧", 12, "var(--bad)")
         + label(380, 40, "⟦창고가 멀면 배송도 느려요|a far-away warehouse means slow delivery too⟧", 13, "var(--ink)"))

# 2. 그냥 다 복제해두면 되는 거 아냐?
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **SORTER)
         + bubble(110, 70, 220, 44, "⟦지점마다 똑같이 복제해두면 끝 아닌가요?|just copy everything to every branch, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + box(560, 150, 0.9, twin=True)
         + label(560, 230, "⟦그런데 숫자가 서로 달라지면?|but what if the copies stop matching?⟧", 12, "var(--bad)")
         + label(380, 280, "⟦동시에 고치면 복제본끼리 틀어져요|edit both at once, and the copies drift apart⟧", 12, "var(--ink)"))

# 3. 분산 데이터베이스 = 여러 지점으로 나눈 창고 네트워크 (hero)
P3 = svg(340, sky(340, ground=False)
         + shelfzone(60, 140, 180, 80, 0.9, label_text="⟦서울 지점|Seoul branch⟧")
         + shelfzone(290, 140, 180, 80, 0.9, label_text="⟦부산 지점|Busan branch⟧")
         + shelfzone(520, 140, 180, 80, 0.9, label_text="⟦대전 지점|Daejeon branch⟧")
         + '<path d="M240 180 h50 M470 180 h50" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 30, "⟦분산 데이터베이스 = 여러 지점으로 나눠 두고 서로 맞춰가는 창고 네트워크|Distributed DB = a warehouse network split across branches that keep each other in sync⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦가까운 지점에서 빠르게, 그래도 전체는 하나처럼 보이게|fast from the nearest branch, yet it all still looks like one warehouse⟧", 12, "var(--muted)"))

# 4. DB 모델링 관점: 중앙집중 vs 분산 비교표
P4 = svg(320, sky(320, ground=False)
         + '<rect x="40" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="390" y="40" width="330" height="240" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + label(205, 66, "⟦중앙집중 창고|Centralized⟧", 13, "var(--ink)", weight=700)
         + label(555, 66, "⟦분산 창고|Distributed⟧", 13, "var(--ink)", weight=700)
         + label(205, 100, "⟦빠른 조인, 느린 원거리 요청|fast joins, slow far-away requests⟧", 10.5, "var(--muted)")
         + label(205, 130, "⟦건물 하나 고장 = 전체 중단|one building down = everything down⟧", 10.5, "var(--bad)")
         + label(205, 160, "⟦규칙 하나로 정합성 지키기 쉬움|one rulebook makes consistency easy⟧", 10.5, "var(--good)")
         + label(555, 100, "⟦가까운 지점에서 빠르게 응답|fast local answers, each near its branch⟧", 10.5, "var(--good)")
         + label(555, 130, "⟦한 지점 고장도 나머진 계속 동작|one branch down, the rest keep going⟧", 10.5, "var(--good)")
         + label(555, 160, "⟦지점 간 조인·정합성 맞추기 어려움|cross-branch joins and consistency get hard⟧", 10.5, "var(--bad)")
         + label(380, 300, "⟦시험에서는 이 트레이드오프(속도 vs 정합성/조인 비용)를 물어요|exams ask about exactly this trade-off — speed vs. consistency and join cost⟧", 12, "var(--ink)"))

# 5. 더 깊은 이론은 SRE 세계에서
P5 = svg(300, sky(300, ground=False)
         + person(380, 150, s=0.85, face=EYES, **MANAGER)
         + box(260, 190, 0.8) + box(500, 190, 0.8, twin=True)
         + label(380, 250, "⟦나누기(샤딩)·복제·합의는 분산 DB 모델링의 기본기예요|sharding, replication, and consensus are the basics of distributed DB modeling⟧", 12, "var(--ink)")
         + label(380, 285, "⟦분산 이론 자체는 SRE 세계에서 더 깊이 다뤄요|the deeper theory lives in the SRE world⟧", 12, "var(--muted)"))

SPLIT_I = icon('<rect x="8" y="22" width="20" height="30" rx="3" fill="var(--accent)"/><rect x="36" y="22" width="20" height="30" rx="3" fill="var(--accent)"/><path d="M32 16 v32" stroke="var(--muted)" stroke-width="3" stroke-dasharray="4 3"/>')
COPY_I = icon('<rect x="12" y="14" width="26" height="24" rx="3" fill="var(--good)"/><rect x="26" y="26" width="26" height="24" rx="3" fill="var(--good)" opacity="0.6"/>')
VOTE_I = icon('<circle cx="18" cy="40" r="8" fill="var(--accent)"/><circle cx="32" cy="18" r="8" fill="var(--accent)"/><circle cx="46" cy="40" r="8" fill="var(--accent)"/><path d="M18 40 L32 18 L46 40" stroke="var(--muted)" stroke-width="2.5" fill="none"/>')
WAIT_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--muted)" stroke-width="4"/><path d="M32 20 v12 l8 4" stroke="var(--accent)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "distdb", "order": 10,
    "title": ("여러 지점으로 나뉜 창고", "The Warehouse Split Across Branches"),
    "h1": ("<em>분산 데이터베이스</em>가 뭐예요?", "What is a <em>Distributed Database</em>?"),
    "sub": ("분산 데이터베이스를, 하나의 거대한 창고 대신 여러 지역 지점으로 나눠 서로 맞춰가는 이야기로 풀어봤어요. 깊은 분산 이론은 SRE 세계에서 더 다뤄요.",
            "A distributed database, told as a story about splitting one giant warehouse into regional branches that keep each other in sync. The deeper distributed-systems theory lives in the SRE world."),
    "panels": [
        {"svg": P1, "alt": ("전국의 배송 기사들이 멀리 있는 창고 하나에만 몰려듦", "Drivers from across the country all converge on one distant warehouse"),
         "caption": ("전국 모든 주문이 창고 하나로만 몰려요.", "Every order nationwide piles onto one single warehouse."),
         "small": ("창고가 멀면 배송도 느려요.", "A far-away warehouse means slow delivery too.")},
        {"svg": P2, "alt": ("분류 담당이 그냥 복제하면 된다고 말하지만, 복제 상자 두 개가 서로 틀어질 위험이 있음", "The modeler suggests just copying everything, but twin boxes risk drifting apart"),
         "caption": ("그냥 다 복제해두면 되는 거 아냐?", "Just copy everything to every branch, right?"),
         "small": ("동시에 고치면 복제본끼리 틀어져요.", "Edit both at once, and the copies drift apart.")},
        {"svg": P3, "hero": True, "alt": ("서울·부산·대전 세 지점으로 나뉜 창고가 점선으로 서로 이어짐", "A warehouse split into Seoul, Busan, and Daejeon branches, linked by dashed lines"),
         "caption": ("분산 데이터베이스는 여러 지점으로 나눈 창고 네트워크예요.", "A distributed database is a warehouse network split across branches."),
         "small": ("가까운 지점에서 빠르게, 그래도 전체는 하나처럼 보이게.", "Fast from the nearest branch, yet it all still looks like one warehouse."),
         "tricks": (4, [
             (SPLIT_I, ("지역별로 나누기", "Split by region"), ("샤딩/파티셔닝이에요", "that's sharding / partitioning")),
             (COPY_I, ("복제해서 안전하게", "Copy for safety"), ("지점 하나가 쉬어도 돼요", "one branch can go down safely"), "calm"),
             (VOTE_I, ("합의로 맞추기", "Agree with a vote"), ("여럿이 투표해 정해요", "several branches vote to decide"), "warm"),
             (WAIT_I, ("적당한 지연 받아들이기", "Accept a little delay"), ("완벽한 동시성 대신요", "instead of perfect simultaneity")),
         ])},
        {"svg": P4, "alt": ("중앙집중 창고와 분산 창고를 속도·장애내성·정합성 기준으로 비교한 표", "A table comparing a centralized warehouse and a distributed one on speed, fault tolerance, and consistency"),
         "caption": ("중앙집중 vs 분산, 속도와 정합성을 맞바꿔요.", "Centralized vs. distributed trades off speed and consistency."),
         "small": ("시험에서는 이 트레이드오프를 자주 물어요.", "Exams often ask about exactly this trade-off.")},
        {"svg": P5, "alt": ("관리자가 나뉜 상자와 복제 상자를 보며 서 있음", "A manager stands beside split and duplicated boxes"),
         "caption": ("나누기·복제·합의는 분산 DB 모델링의 기본기예요.", "Sharding, replication, and consensus are the basics of distributed DB modeling."),
         "small": ("분산 이론 자체는 SRE 세계에서 더 깊이 다뤄요.", "The deeper theory lives in the SRE world.")},
    ],
    "summary": (("<b>분산 데이터베이스</b>는 하나의 논리적 DB를 <b>여러 지점(노드)에 나눠 저장</b>하고, 복제와 합의로 <b>하나처럼 보이게</b> 맞추는 구조예요.",
                 "A <b>distributed database</b> stores one logical database <b>split across many nodes</b>, using replication and consensus to make it <b>look like a single database</b>."),
                ("DB 모델링 시험 관점에서는 데이터를 어떻게 나눌지(샤딩 키 설계), 어떻게 복제할지(동기/비동기), 조인·트랜잭션 비용이 어떻게 늘어나는지를 다뤄요. CAP 정리·합의 알고리즘 같은 분산 시스템 이론 자체는 SRE 세계의 관련 페이지에서 더 깊이 설명해요.",
                 "From a DB-modeling exam angle, this is about choosing a sharding key, picking sync vs. async replication, and the rising cost of cross-node joins and transactions. The deeper distributed-systems theory — CAP theorem, consensus algorithms — is covered in more depth over in the SRE world.")),
    "glossary": [
        ("샤딩", "Sharding", ("지점별로 나눠 담기.", "Splitting goods by branch."), ('나누는 기준(키) 설계는 이 세계에서 더 다뤄요. → <a href="dbsharding-ko.html">너무 커진 창고를 구역으로 쪼개기</a>', 'Choosing the split key is covered right here. → <a href="dbsharding-en.html">splitting an overgrown warehouse into zones</a>')),
        ("복제", "Replication", ("지점마다 복제 상자 두기.", "Keeping a duplicate box at each branch."), ('동기/비동기 복제의 차이를 다뤄요. → <a href="replication-ko.html">복제 상자의 세계</a>', 'Covers sync vs. async replication. → <a href="replication-en.html">the world of duplicate boxes</a>')),
        ("합의 알고리즘", "Consensus", ("여럿이 투표해서 하나로 정하기.", "Several branches voting on one answer."), ('Raft/Paxos 같은 알고리즘을 다뤄요. → <a href="consensus-ko.html">여러 명이 투표로 정하기</a>', 'Covers algorithms like Raft/Paxos. → <a href="consensus-en.html">deciding by a vote among many</a>')),
        ("CAP 정리", "CAP Theorem", ("셋 다 완벽히는 못 가져요.", "You can't have all three perfectly."), ('일관성·가용성·분단내성의 트레이드오프예요. → <a href="captheorem-ko.html">세 가지를 동시에 가질 수 없는 법칙</a>', "The consistency/availability/partition trade-off. → <a href=\"captheorem-en.html\">the law you can't have all three of at once</a>")),
        ("최종적 일관성", "Eventual Consistency", ("조금 늦게라도 결국 맞춰짐.", "Eventually matching up, even if a bit late."), ('당장은 숫자가 달라도 돼요. → <a href="eventualconsistency-ko.html">결국엔 맞춰지는 이야기</a>', 'Numbers can differ for a moment. → <a href="eventualconsistency-en.html">the story of eventually matching up</a>')),
        ("데이터 지역성", "Data Locality", ("가까운 지점에서 처리하기.", "Handling it at the nearest branch."), ("가까울수록 응답이 빨라요.", "The closer it is, the faster the answer.")),
        ("분산 트랜잭션(2PC)", "Distributed Transaction (2PC)", ("여러 지점에 걸친 출납 전표.", "A transaction slip spanning several branches."), ("모든 지점이 동의해야 확정돼요.", "It only finalizes once every branch agrees.")),
        ("NoSQL", "NoSQL", ("고정된 선반 칸이 아닌 창고.", "A warehouse without fixed shelf slots."), ("분산에 유리하게 구조를 느슨하게 둬요.", "Loosens the structure to make distribution easier.")),
    ],
}
