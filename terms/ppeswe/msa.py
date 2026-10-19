from _draw import *
from _world import *

# 1. 오탈자 하나 고치려 해도 책 전체를 다시 찍어야 해요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **PRINTER)
         + manuscript(280, 130, 1.0, marks=4) + printplate(460, 150, 0.8)
         + label(380, 230, "⟦백과사전 한 챕터만 고쳐도 책 전체를 다시 찍어야 해요|fixing even one chapter means reprinting the entire encyclopedia⟧", 12, "var(--bad)")
         + label(380, 280, "⟦한 부분이 늦어지면, 책 전체 출간이 다 늦어져요|if one part falls behind, the whole book's release falls behind too⟧", 13, "var(--ink)"))

# 2. 더 빨리 쓰라는 말, 묶여 있어서 따로 낼 수 없다는 반박
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 220, 36, "⟦그냥 더 빨리 써서 맞추면 되잖아요|just write faster to make the deadline⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **WRITER) + bubble(460, 80, 230, 36, "⟦전부 한 책에 묶여서 따로 낼 수가 없어요|it's all bound into one book — we can't release any part separately⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦하나로 묶여 있으면, 일부만 먼저 낼 방법이 없어요|when everything's bound together, there's no way to release just part of it early⟧", 12, "var(--ink)"))

# 3. 마이크로서비스 아키텍처 = 두꺼운 책을 작은 소책자들로 쪼개기 (hero)
P3 = svg(340, sky(340)
         + person(230, 130, s=0.65, face=SMILE, **WRITER) + printplate(230, 245, 0.5, label_text="⟦동물편|animals⟧")
         + person(380, 130, s=0.65, face=SMILE, **PROOFER) + printplate(380, 245, 0.5, label_text="⟦역사편|history⟧")
         + person(530, 130, s=0.65, face=SMILE, **PRINTER) + printplate(530, 245, 0.5, label_text="⟦과학편|science⟧")
         + label(380, 30, "⟦마이크로서비스 아키텍처 = 두꺼운 책 한 권을 작은 소책자들로 쪼개, 각자 따로 쓰고 따로 찍는 구조|microservices architecture = splitting one thick book into small standalone volumes, each written and printed independently⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦소책자끼리는 목차로 서로를 가리킬 뿐, 내용을 안 섞어요|the volumes only point to each other through a shared index — they never mix content⟧", 12, "var(--muted)"))

# 4. 소책자 구조의 특징
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦소책자 구조의 특징|TRAITS OF THE SPLIT STRUCTURE⟧",
                      ("⟦독립 출간 — 한 편만 먼저 낼 수 있어요|independent release — one volume can ship alone⟧",
                       "⟦독립 팀 — 편마다 전담 팀이 따로 있어요|independent teams — each volume has its own team⟧",
                       "⟦목차로 연결 — 차례로만 서로 참조해요|connected by index — refers via table of contents only⟧",
                       "⟦분량도 따로 — 잘 팔리는 편만 더 찍어요|sized independently — a popular volume alone gets reprinted⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **EDITOR)
         + label(560, 250, "⟦소책자 수만큼 조율할 목차도 늘어나요|the more volumes, the more index-coordination there is⟧", 11, "var(--muted)")
         + label(380, 300, "⟦작은 출판사엔 오히려 버거울 수 있어요|for a small publishing house, this can be more than it can handle⟧", 12, "var(--ink)"))

# 5. 묶임을 풀면, 조율이라는 새 일이 생겨요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **EDITOR) + label(190, 240, "⟦한 편이 안 팔려도 다른 편엔 안 번져요|if one volume flops, it doesn't spread to the others⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **PRINTER) + manuscript(570, 220, 0.6) + label(570, 270, "⟦목차를 맞추는 조율 비용은 늘어나요|but the cost of coordinating the index goes up⟧", 11, "var(--ink)")
         + label(380, 282, "⟦마이크로서비스는 묶임을 푸는 대신, 조율이라는 새 일을 만들어요|microservices trade away being bound together — but create a new job: coordination⟧", 12, "var(--ink)", cls="d"))

SPLIT_I = icon('<rect x="8" y="16" width="20" height="32" rx="2" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="32" y="16" width="20" height="32" rx="2" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/><path d="M28 8 l8 8 -8 8" stroke="var(--ink)" stroke-width="2" fill="none"/>')
TEAM_I = icon('<circle cx="18" cy="20" r="8" fill="var(--accent)"/><circle cx="46" cy="20" r="8" fill="var(--good)"/><path d="M10 44 q8 -10 16 0 M38 44 q8 -10 16 0" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/>')
INDEX_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><path d="M22 20 h20 M22 28 h12 M22 36 h16 M22 44 h10" stroke="#142033" stroke-width="2"/>')
SCALE_I = icon('<rect x="10" y="30" width="16" height="20" rx="2" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="32" y="12" width="22" height="38" rx="2" fill="var(--good-soft)" stroke="var(--good)" stroke-width="3"/>')

PAGE = {
    "slug": "msa", "order": 10,
    "title": ("두꺼운 책을 소책자들로 쪼개기", "Splitting the Thick Book into Small Volumes"),
    "h1": ("<em>마이크로서비스 아키텍처(MSA)</em>가 뭐예요?", "What is <em>Microservices Architecture (MSA)</em>?"),
    "sub": ("마이크로서비스 아키텍처를, 두꺼운 백과사전 한 권을 동물편·역사편·과학편처럼 작은 소책자들로 쪼개 따로 쓰고 따로 찍는 이야기로 풀어봤어요.",
            "Microservices architecture, told as a story about splitting one thick encyclopedia into small standalone volumes — animals, history, science — each written and printed on its own."),
    "panels": [
        {"svg": P1, "alt": ("인쇄 감독이 진땀을 흘리며 오탈자 하나 때문에 책 전체를 다시 찍어야 하는 상황을 봄", "A print supervisor sweats, realizing a single typo means reprinting the whole encyclopedia"),
         "caption": ("오탈자 하나 고치려 해도 책 전체를 다시 찍어야 해요.", "Fixing even one chapter means reprinting the entire encyclopedia."),
         "small": ("한 부분이 늦어지면, 책 전체 출간이 다 늦어져요.", "If one part falls behind, the whole book's release falls behind too.")},
        {"svg": P2, "alt": ("편집장은 더 빨리 쓰라 하고, 작가는 한 책에 묶여 따로 낼 수 없다고 반박함", "The editor says to write faster; the writer objects that it's all bound into one book"),
         "caption": ("더 빨리 쓰라는 말, 묶여 있어서 따로 낼 수 없다는 반박.", "A push to write faster, met with the fact that it's all bound together."),
         "small": ("하나로 묶여 있으면, 일부만 먼저 낼 방법이 없어요.", "When everything's bound together, there's no way to release just part of it early.")},
        {"svg": P3, "hero": True, "alt": ("동물편·역사편·과학편 세 소책자를 각각 다른 작가팀이 따로 만듦", "Three separate teams each make their own volume — animals, history, science"),
         "caption": ("마이크로서비스 아키텍처는 두꺼운 책을 작은 소책자들로 쪼개요.", "Microservices architecture splits one thick book into small standalone volumes."),
         "small": ("소책자끼리는 목차로 서로를 가리킬 뿐, 내용을 안 섞어요.", "The volumes only point to each other through a shared index — they never mix content."),
         "tricks": (4, [
             (SPLIT_I, ("작게 쪼개기", "Split it small"), ("소책자 단위로 나눠요", "dividing it into standalone volumes"), "calm"),
             (TEAM_I, ("팀도 따로 두기", "Give each its own team"), ("편마다 전담 팀이 있어요", "each volume has its own dedicated team")),
             (INDEX_I, ("목차로만 연결하기", "Connect only through the index"), ("내용은 안 섞어요", "never mixing the content"), "warm"),
             (SCALE_I, ("따로 키우기", "Grow each on its own"), ("잘 팔리는 편만 더 찍어요", "reprinting only the popular volume")),
         ])},
        {"svg": P4, "alt": ("소책자 구조 특징표: 독립 출간·독립 팀·목차 연결·독립 분량 네 항목", "A board of split-structure traits: independent release, independent teams, index-only links, independent sizing"),
         "caption": ("소책자 구조는 이런 특징을 가져요.", "The split structure has these traits."),
         "small": ("소책자 수만큼 조율할 목차도 늘어나요.", "The more volumes, the more index-coordination there is.")},
        {"svg": P5, "alt": ("왼쪽: 편집장이 한 편이 안 팔려도 다른 편엔 안 번진다고 말함. 오른쪽: 인쇄 감독이 조율 비용은 늘어난다고 말함", "Left: the editor says one failing volume doesn't spread to others. Right: the print supervisor says coordination cost still rises"),
         "caption": ("묶임을 풀면, 조율이라는 새 일이 생겨요.", "Untying the bundle creates a new job: coordination."),
         "small": ("공짜로 얻는 구조는 아니에요.", "It isn't a structure that comes for free.")},
    ],
    "summary": (("<b>마이크로서비스 아키텍처</b> = 두꺼운 책 한 권을 <b>독립된 소책자들</b>로 쪼개, <b>목차로만 연결</b>하는 구조.",
                 "<b>Microservices architecture</b> = splitting one thick book into <b>independent standalone volumes</b>, <b>linked only through a shared index</b>."),
                ("마이크로서비스 아키텍처는 하나의 거대한 애플리케이션(모놀리스)을, 각자 독립적으로 개발·배포·확장할 수 있는 작은 서비스 단위로 나누는 방식이에요. 서비스끼리는 API로만 통신하고 내부 구현을 서로 숨겨요. 장애나 트래픽 급증이 한 서비스에 머물 수 있다는 장점이 있지만, 서비스가 많아질수록 서로 맞추는 조율·운영 비용도 함께 커져요.",
                 "Microservices architecture splits one giant application (a monolith) into small services that can each be developed, deployed, and scaled independently. Services communicate only through APIs, hiding their internal implementation from each other. A failure or traffic spike can stay contained to one service, but as services multiply, the cost of coordinating and operating them all grows too.")),
    "glossary": [
        ("마이크로서비스 아키텍처", "Microservices Architecture", ("독립 소책자로 쪼갠 구조.", "A structure split into independent volumes."), ("서비스마다 따로 배포·확장해요.", "Each service deploys and scales on its own.")),
        ("모놀리스", "Monolith", ("하나로 묶인 두꺼운 백과사전.", "One thick, bound-together encyclopedia."), ("마이크로서비스가 쪼개는 대상이에요.", "What microservices architecture splits apart.")),
        ("API", "API", ("소책자들이 서로 가리키는 목차.", "The index the volumes use to point to one another."), ("내용을 안 섞고 참조만 해요.", "Refers without mixing content.")),
        ("독립 배포", "Independent Deployment", ("한 편만 먼저 찍어 낼 수 있는 일.", "Being able to print one volume alone, first."), ("모놀리스에서는 불가능해요.", "Impossible in a monolith.")),
        ("서비스 메시", "Service Mesh", ("소책자 사이를 오가는 전용 통로.", "The dedicated path between the volumes."), ('소책자들 사이의 통신을 따로 전담하는 장치예요. → <a href="servicemesh-ko.html">기구 사이 전용 통로</a>', 'A dedicated layer handling communication between the volumes. → <a href="servicemesh-en.html">the dedicated path between rides</a>')),
        ("API 게이트웨이", "API Gateway", ("독자가 늘 드나드는 대표 창구.", "The single front desk readers always go through."), ("여러 소책자 앞에 세운 창구예요.", "A single window set up in front of many volumes.")),
        ("소프트웨어 아키텍처 모델", "Software Architecture Model", ("책 모양을 미리 정하는 큰 틀.", "The big framework that decides a book's overall shape."), ('마이크로서비스는 그중 한 가지 모델이에요. → <a href="swarchmodel-ko.html">책 전체를 미리 짜 두는 구조 밑그림</a>', 'Microservices is just one of those models. → <a href="swarchmodel-en.html">the blueprint that shapes the whole book ahead of time</a>')),
        ("정보시스템 감리/PMO", "IS Audit/PMO", ("출간 전 마지막 검수관.", "The last checker before publication."), ('소책자가 많아질수록 감리도 더 여러 곳을 봐야 해요. → <a href="pmoaudit-ko.html">출간 전 마지막 검수관</a>', 'The more volumes there are, the more places audit has to check. → <a href="pmoaudit-en.html">the last checker before publication</a>')),
    ],
}
