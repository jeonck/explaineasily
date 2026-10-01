from _draw import *
from _world import *

# 1. 장부를 보관한 창고에 불이 나서 명부를 통째로 잃어요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shed(300, 240, 1.3)
         + '<path d="M270 160 q10 -24 -4 -34 q10 4 8 -14 q14 10 6 28 q14 -4 6 16z" fill="var(--bad)"/>'
         + person(420, 174, s=0.6, face=FROWN + SWEAT, **OPERATOR)
         + bubble(460, 90, 230, 50, "⟦명부가... 전부 사라졌어요|the log... it's all gone⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(380, 282, "⟦창고에 불이 나서 명부를 통째로 잃었어요|a fire in the warehouse, and the whole log is gone⟧", 12, "var(--ink)"))

# 2. 왜: 한 곳에만 두면 그곳이 잘못되면 끝이에요
P2 = svg(300, sky(300)
         + shed(380, 240, 1.3)
         + '<path d="M340 150 L420 150" stroke="var(--bad)" stroke-width="5" fill="none"/><path d="M335 145 l10 10 M330 150 l10 10 M335 155 l10 -10" stroke="var(--bad)" stroke-width="4" fill="none"/>'
         + label(380, 190, "⟦딱 한 곳|only one place⟧", 12, "var(--bad)", cls="d")
         + person(200, 174, s=0.6, face=EYES, **MANAGER) + bubble(100, 90, 210, 50, "⟦한 곳만 믿어도 될까요?|can we trust just one place?⟧", 12, "var(--panel)", "var(--line)", "right")
         + label(380, 282, "⟦한 곳에만 두면 그곳이 잘못되면 끝이에요|keep it in one place, and if that place fails, it's gone⟧", 12, "var(--ink)"))

# 3. hero: 같은 명부를 창고 두세 곳에 똑같이 적어 둬요
P3 = svg(340, sky(340)
         + shed(190, 280, 1.0, label_text="⟦원본|LEADER⟧")
         + shed(400, 280, 0.85, label_text="⟦복사본 1|FOLLOWER 1⟧") + shed(580, 280, 0.85, label_text="⟦복사본 2|FOLLOWER 2⟧")
         + '<path d="M250 230 Q320 200 360 235" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + '<path d="M250 240 Q440 210 540 240" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(380, 40, "⟦같은 명부를 창고 두세 곳에 똑같이 적어 둬요|the same log, copied into two or three warehouses⟧", 14, "var(--ink)", cls="d")
         + label(380, 320, "⟦하나가 타도 나머지가 있어요|if one burns down, the rest still have it⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 원본이 쓰기 담당, 나머지는 베끼기만, 지연이 있어요
P4 = svg(320, sky(320)
         + shed(160, 250, 0.95, label_text="⟦원본(쓰기)|LEADER (writes)⟧")
         + shed(420, 250, 0.8, label_text="⟦복제본(읽기)|FOLLOWER (reads)⟧")
         + ticket(290, 170, 0.8, "⟦새 기록|new entry⟧") + '<path d="M210 185 L420 220" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(420, 300, "⟦도착까지 아주 잠깐 걸려요(복제 지연)|arriving takes a short moment (replication lag)⟧", 11, "var(--muted)")
         + board(580, 60, 150, 90, "⟦원본 고장?|LEADER DOWN?⟧", ("⟦복제본 하나가|a follower⟧", "⟦원본이 돼요|becomes leader⟧"), 1.0)
         + label(380, 286, "⟦원본이 쓰기를 맡고, 나머지는 베끼기만 해요|the leader handles writes, the rest just copy⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 베끼는 중엔 살짝 옛날 답, 서로 원본이라 우기면 스플릿 브레인
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + shed(190, 240, 0.85) + person(190, 150, s=0.55, face=EYES, hat=None, shirt="#7B3FA0")
         + bubble(90, 60, 200, 46, "⟦방금 바뀐 거 맞아요?|did it just change?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(190, 300, "⟦베끼는 중엔 살짝 옛날 답을 받을 수 있어요|while copying, you might get a slightly stale answer⟧", 11, "var(--ink)")
         + shed(560, 240, 0.85, label_text="⟦내가 원본!|I'M THE LEADER!⟧") + shed(680, 240, 0.6, label_text="⟦내가 원본!|I'M THE LEADER!⟧")
         + label(620, 300, "⟦둘이 원본이라 우기면 안 돼요|two warehouses both claiming to be the leader is a problem⟧", 11, "var(--ink)"))

LEADER_I = icon('<rect x="8" y="24" width="48" height="30" rx="4" fill="var(--accent)"/><path d="M8 24 l24 -16 24 16z" fill="var(--good)"/>')
COPY_I = icon('<rect x="6" y="10" width="30" height="36" rx="3" fill="var(--good)"/><rect x="24" y="22" width="30" height="36" rx="3" fill="none" stroke="var(--good)" stroke-width="4"/>')
LAG_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 18 V32 L44 40" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" fill="none"/>')
SWAP_I = icon('<path d="M14 24 h30 l-8 -8" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M50 40 h-30 l8 8" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "replication", "order": 7,
    "title": ("손님 명부를 두 창고에 똑같이", "The Same Guest Log in Two Warehouses"),
    "h1": ("<em>복제</em>가 뭐예요?", "What is <em>Replication</em>?"),
    "sub": ("복제를 같은 손님 명부를 창고 여러 곳에 똑같이 적어 두는 이야기로 풀어봤어요.",
            "Replication, told as a story about keeping the same guest log copied in several warehouses."),
    "panels": [
        {"svg": P1, "alt": ("명부를 보관한 창고에서 불이 나고, 요원이 명부가 전부 사라졌다며 당황함", "The warehouse holding the log catches fire while an operator panics that it's all gone"),
         "caption": ("창고에 불이 나서 명부를 통째로 잃었어요.", "A fire in the warehouse, and the whole log is gone."),
         "small": ("딱 한 곳에만 있던 명부라 되살릴 수가 없어요.", "It only lived in one place, so there's nothing to recover.")},
        {"svg": P2, "alt": ("창고 하나에 금 간 자국이 보이고, 공원장이 '한 곳만 믿어도 될까요?' 묻는 장면", "A cracked warehouse while a manager asks whether trusting just one place is wise"),
         "caption": ("한 곳에만 두면 그곳이 잘못되면 끝이에요.", "Keep it in one place, and if that place fails, it's gone."),
         "small": ("한 군데가 전부를 쥐고 있으면 위험해요.", "Betting everything on a single spot is risky.")},
        {"svg": P3, "hero": True, "alt": ("원본 창고 하나와 복사본 창고 두 곳이 화살표로 연결되어 명부를 똑같이 복사함", "One leader warehouse connected by arrows to two follower warehouses copying the same log"),
         "caption": ("같은 명부를 창고 두세 곳에 똑같이 적어 둬요.", "The same log, copied into two or three warehouses."),
         "small": ("하나가 타도 나머지가 있어요.", "If one burns down, the rest still have it."),
         "tricks": (4, [
             (LEADER_I, ("원본 창고 하나", "One leader warehouse"), ("쓰기는 여기서만 해요", "only it handles writing"), "calm"),
             (COPY_I, ("나머지는 베끼기만", "The rest just copy"), ("읽기 담당이에요", "they handle reading")),
             (LAG_I, ("베끼는 데 시간이 조금", "Copying takes a moment"), ("복제 지연이라 불러요", "called replication lag"), "warm"),
             (SWAP_I, ("원본이 망가지면", "If the leader breaks"), ("복제본 하나가 원본이 돼요", "a follower becomes the new leader")),
         ])},
        {"svg": P4, "alt": ("원본 창고가 새 기록을 받아 복제본으로 화살표를 보내고, 원본이 고장나면 복제본이 원본이 된다는 안내판", "The leader warehouse sends a new entry by arrow to the follower, with a sign noting a follower takes over if the leader goes down"),
         "caption": ("원본이 쓰기를 맡고, 나머지는 베끼기만 해요.", "The leader handles writes, the rest just copy."),
         "small": ("도착까지 아주 잠깐 걸리고, 원본이 고장나면 복제본 하나가 원본이 돼요.", "It takes a moment to arrive, and if the leader fails, a follower takes over.")},
        {"svg": P5, "alt": ("왼쪽: 사람이 방금 바뀐 게 맞는지 묻는 장면. 오른쪽: 창고 둘이 동시에 자기가 원본이라고 우김", "Left: someone asks if a change just happened. Right: two warehouses both claim to be the leader at once"),
         "caption": ("베끼는 중엔 살짝 옛날 답을 받을 수 있어요.", "While copying, you might get a slightly stale answer."),
         "small": ("그리고 창고 둘이 서로 원본이라고 우기면 큰 문제예요.", "And two warehouses both insisting they're the leader is a real problem.")},
    ],
    "summary": (("<b>복제</b> = 같은 명부를 <b>창고 여러 곳에 똑같이</b> 적어 두는 일. <b>원본이 쓰기</b>를 맡고 나머지는 <b>베끼기만</b> 해서, 하나가 망가져도 서비스는 계속돼요.",
                 "<b>Replication</b> = keeping the same log <b>copied across several warehouses</b>. The <b>leader handles writes</b> and the rest just <b>copy</b>, so the service survives even if one warehouse fails."),
                ("데이터를 여러 서버에 복사해 두는 방식이에요. 원본(leader)과 복제본(follower)으로 나뉘고, 동기 복제는 즉시, 비동기 복제는 살짝 늦게 맞춰져요(→일관성). 원본 장애 시 복제본 중 하나가 원본이 되는 걸 장애 조치라 해요.",
                 "Copying data across multiple servers. There's a leader and followers; synchronous replication updates immediately, asynchronous replication catches up a bit later (consistency). When a follower takes over from a failed leader, that's called failover.")),
    "glossary": [
        ("복제", "Replication", ("명부를 여러 창고에 똑같이 두는 일.", "Keeping the same log in several warehouses."), ("하나가 망가져도 서비스가 멈추지 않아요.", "The service keeps running even if one warehouse fails.")),
        ("원본/복제본", "Leader/follower", ("쓰기 담당 창고와 베끼기만 하는 창고.", "The warehouse that writes, and the ones that just copy."), ("원본이 하나, 복제본은 여럿일 수 있어요.", "There's one leader, but there can be many followers.")),
        ("복제 지연", "Replication lag", ("베끼는 데 걸리는 짧은 시간.", "The short time it takes to copy over."), ("그 사이엔 복제본이 살짝 옛날 답을 줘요.", "During that gap a follower may answer with slightly old data.")),
        ("읽기 복제본", "Read replica", ("읽기만 맡는 복제본.", "A follower dedicated to reads."), ("원본의 쓰기 부담을 덜어줘요.", "It takes read load off the leader.")),
        ("동기/비동기 복제", "Sync / async replication", ("즉시 맞추는지, 조금 늦게 맞추는지.", "Whether copying happens instantly or a bit later."), ("즉시는 더 안전하지만 더 느려요.", "Instant is safer but slower.")),
        ("다중 리전", "Multi-region", ("복제본을 아예 다른 도시에 두는 일.", "Putting a follower in a whole different city."), ("한 도시가 통째로 문제여도 버텨요.", "It survives even if one whole city has trouble.")),
        ("일관성", "Eventual consistency", ("베끼는 중 살짝 다른 답이 나오는 것.", "Getting a slightly different answer while copying is still in progress."), ("시간이 지나면 다 같은 답이 돼요.", "Given enough time, every copy agrees.")),
        ("장애 조치", "Failover", ("원본이 망가지면 복제본이 원본이 되는 일.", "A follower stepping up to be leader when the leader fails."), ('누가 새 원본이 될지는 투표로 정해요. → <a href="consensus-ko.html">여러 관제실이 손 들어 정하기</a>', 'Deciding who becomes the new leader is a vote. → <a href="consensus-en.html">control rooms raising hands to decide</a>')),
    ],
}
