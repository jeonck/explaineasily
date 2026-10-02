from _draw import *
from _world import *

# 1. 같은 질문을 손님마다 또 물어봐요
P1 = svg(320, sky(320)
         + booth(560, 230, 0.9) + person(500, 174, s=0.5, face=FROWN + SWEAT, **OPERATOR)
         + queueline(30, 180, 3, 0.45, 40)
         + bubble(60, 130, 190, 44, "⟦오늘 몇 시에 닫아요?|what time do you close today?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 300, "⟦같은 질문을 손님마다 또 물어봐요|every guest asks the exact same question⟧", 13, "var(--ink)", cls="d"))

# 2. 왜 어려운가 — 매번 안쪽 창고까지 가서 확인하면 오래 걸려요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + booth(130, 230, 0.9) + shed(660, 230, 0.9, label_text="⟦안쪽 창고|back warehouse⟧")
         + queueline(30, 185, 2, 0.4, 30)
         + person(400, 174, s=0.5, face=FROWN + SWEAT, **OPERATOR)
         + '<path d="M165 200 Q400 130 610 215" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="6 4"/>'
         + '<path d="M610 235 Q400 290 165 225" stroke="var(--bad)" stroke-width="2" fill="none" stroke-dasharray="2 4"/>'
         + label(380, 300, "⟦매번 안쪽 창고까지 가서 확인하면 오래 걸려요|checking the back warehouse every single time takes forever⟧", 13, "var(--bad)", cls="d"))

# 3. hero — 메모판에 미리 적어두면 바로 보여줄 수 있어요
FAQ_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M26 22 a7 7 0 1 1 5 12" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="31" cy="42" r="2.5" fill="var(--accent)"/>')
EDIT_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 42 L36 20 L44 26 L30 48 L20 50z" fill="var(--accent)"/>')
TTL_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M32 18 V32 L42 38" stroke="var(--accent)" stroke-width="5" fill="none" stroke-linecap="round"/>')
EVICT_I = icon('<rect x="18" y="10" width="28" height="11" rx="2" fill="var(--stone)"/><rect x="18" y="23" width="28" height="11" rx="2" fill="var(--stone)"/><rect x="18" y="36" width="28" height="11" rx="2" fill="var(--bad)"/><path d="M14 47 L50 47" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>')

P3 = svg(340, sky(340)
         + board(60, 50, 300, 170, "⟦자주 묻는 질문|FAQ⟧", ("⟦문 닫는 시간: 9시|closes at 9pm⟧", "⟦화장실: 정문 옆|restroom by the gate⟧", "⟦우산 대여: 안내소|umbrella at the booth⟧"), 1.0)
         + person(120, 233, s=0.6, face=SMILE, **OPERATOR)
         + booth(560, 250, 0.9) + person(500, 194, s=0.5, face=SMILE, hat=FOLK[2][0], shirt=FOLK[2][1])
         + '<path d="M480 212 Q420 170 365 185" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(380, 25, "⟦안내소 앞 메모판에 미리 적어두면 바로 보여줄 수 있어요|write the answer on the memo board in advance, and you can show it right away⟧", 13, "var(--ink)", cls="d")
         + label(380, 328, "⟦창고까지 안 가도 메모판만 보면 끝이에요|no trip to the warehouse — the board alone is enough⟧", 12, "var(--muted)"))

# 4. 메모판 길 vs 창고 길 — 빠름과 느림 비교
P4 = svg(300, sky(300, ground=False)
         + booth(190, 210, 0.9)
         + board(380, 50, 180, 90, "⟦메모판|BOARD⟧", ("⟦바로 보여줘요|shows right away⟧",), 0.9)
         + shed(650, 210, 0.85, label_text="⟦안쪽 창고|warehouse⟧")
         + '<path d="M225 175 L375 130" stroke="var(--good)" stroke-width="3" fill="none"/>' + label(300, 120, "⟦1초|1s⟧", 12, "var(--good)", cls="d")
         + '<path d="M225 200 L600 203" stroke="var(--bad)" stroke-width="3" fill="none"/>' + label(430, 190, "⟦10초|10s⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦메모판은 빠르고, 창고까지 가면 느려요|the board is fast — the trip to the warehouse is slow⟧", 13, "var(--ink)", cls="d"))

# 5. 깨지는 곳 — 틀린 답을 적으면 다 같이 틀리고, 한꺼번에 몰리면 그 순간은 느려요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + board(40, 40, 280, 90, "⟦자주 묻는 질문|FAQ⟧", ("⟦문 닫는 시간: 7시|closes at 7pm⟧",), 1.0, hl=0)
         + person(100, 194, s=0.5, face=FROWN, hat=FOLK[1][0], shirt=FOLK[1][1]) + person(220, 194, s=0.5, face=FROWN, hat=FOLK[2][0], shirt=FOLK[2][1])
         + label(190, 270, "⟦틀린 답이면 다 같이 틀려요|a wrong answer means everyone gets it wrong⟧", 11, "var(--bad)")
         + board(430, 40, 280, 90, "⟦자주 묻는 질문|FAQ⟧", ("⟦문 닫는 시간: 9시|closes at 9pm⟧",), 1.0)
         + queueline(420, 206, 5, 0.42, 30)
         + label(570, 270, "⟦한꺼번에 몰리면 그 순간은 느려요|everyone rushing at once slows that moment down⟧", 11, "var(--ink)")
         + label(380, 288, "⟦메모판도 틀리거나 몰리면 말썽이에요|the board can still go wrong — bad answers or a sudden rush⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "caching", "order": 9,
    "title": ("자주 묻는 질문 미리 적어둔 메모판", "The Memo Board of Frequent Answers"),
    "h1": ("<em>캐싱</em>이 뭐예요?", "What is <em>Caching</em>?"),
    "sub": ("캐싱을 안내소 앞에 자주 묻는 질문을 미리 적어둔 메모판 이야기로 풀어봤어요.",
            "Caching, told as a story about the memo board that answers frequent questions in advance."),
    "panels": [
        {"svg": P1, "alt": ("손님 셋이 차례로 같은 질문을 하고, 요원이 지쳐서 땀을 흘림", "Three guests ask the same question one after another, and the tired operator sweats"),
         "caption": ("같은 질문을 손님마다 또 물어봐요.", "Every guest asks the exact same question."),
         "small": ("똑같은 답을 매번 다시 해주느라 창구가 느려져요.", "Repeating the same answer every time slows the booth down.")},
        {"svg": P2, "alt": ("요원이 안쪽 창고까지 왔다 갔다 하고, 손님들은 창구 앞에서 기다림", "The operator keeps walking back and forth to the warehouse while guests wait at the booth"),
         "caption": ("매번 안쪽 창고까지 가서 확인하면 오래 걸려요.", "Checking the back warehouse every single time takes forever."),
         "small": ("확인할 게 많아질수록 왔다 갔다 하는 시간도 쌓여요.", "The more there is to check, the more those round trips add up.")},
        {"svg": P3, "hero": True, "alt": ("안내소 앞 메모판에 자주 묻는 질문 세 개가 미리 적혀 있고, 요원이 바로 가리켜 보여줌", "A memo board in front of the booth has three frequent answers written in advance, and the operator points right to it"),
         "caption": ("안내소 앞 메모판에 미리 적어두면 바로 보여줄 수 있어요.", "Write the answer on the memo board in advance, and you can show it right away."),
         "small": ("창고까지 안 가도 메모판만 보면 끝이에요.", "No trip to the warehouse — the board alone is enough."),
         "tricks": (4, [
             (FAQ_I, ("자주 묻는 것만 적어요", "Write only the frequent ones"), ("아무거나 다 적진 않아요", "not everything gets a spot"), "calm"),
             (EDIT_I, ("답 바뀌면 메모판도 고쳐요", "Fix the board when it changes"), ("캐시 무효화예요", "this is cache invalidation")),
             (TTL_I, ("유효기간을 적어둬요", "Write an expiry date"), ("TTL이라고 불러요", "it's called a TTL"), "warm"),
             (EVICT_I, ("꽉 차면 오래된 것부터 지워요", "Full board, oldest goes first"), ("자리를 늘 비워둬요", "keeps room for new answers")),
         ])},
        {"svg": P4, "alt": ("창구에서 메모판까지는 짧은 화살표로 1초, 안쪽 창고까지는 긴 화살표로 10초", "A short arrow to the board takes 1 second; a long arrow to the warehouse takes 10 seconds"),
         "caption": ("메모판은 빠르고, 창고까지 가면 느려요.", "The board is fast — the trip to the warehouse is slow."),
         "small": ("같은 답이라도 어디서 찾는지에 따라 걸리는 시간이 크게 달라요.", "The same answer takes very different amounts of time depending on where you look it up.")},
        {"svg": P5, "alt": ("왼쪽: 메모판에 틀린 시간이 적혀 손님들이 틀린 답을 듣고 얼굴을 찌푸림. 오른쪽: 손님들이 한꺼번에 메모판으로 몰려듦", "Left: the board has the wrong time written, and guests frown at the wrong answer. Right: guests all rush the board at once"),
         "caption": ("메모판도 틀리거나 몰리면 말썽이에요.", "The board can still go wrong — bad answers or a sudden rush."),
         "small": ("틀린 답을 적어두면 다 같이 틀리고, 한꺼번에 몰리면 그 순간은 느려요.", "A wrong answer gets copied to everyone, and a sudden rush slows that one moment down.")},
    ],
    "summary": (("<b>캐싱</b> = 자주 묻는 답을 <b>안내소 앞 메모판에 미리 적어둬서</b>, 매번 안쪽 창고까지 안 가고도 <b>바로 보여주는</b> 요령.",
                 "<b>Caching</b> = writing frequent answers on a <b>memo board in advance</b>, so you can show them right away without a trip to the back warehouse every time."),
                ("캐시(cache)는 자주 쓰는 데이터를 더 빠른 자리에 미리 복사해 두는 저장 공간이에요. 원본이 바뀌면 캐시도 갱신하거나 지워야 하는데(invalidation), 이 타이밍을 맞추는 게 캐싱에서 가장 어려운 부분이에요.",
                 "A cache is a storage layer that keeps a copy of frequently used data somewhere faster to reach. When the original changes, the cache must be updated or invalidated — getting that timing right is the hardest part of caching.")),
    "glossary": [
        ("캐시", "Cache", ("안내소 앞 메모판.", "The memo board in front of the booth."), ("자주 쓰는 답을 미리 적어 놔요.", "It holds frequent answers written in advance.")),
        ("TTL", "TTL", ("메모판에 적힌 유효기간.", "The expiry date written on the board."), ("지나면 다시 확인하고 새로 적어요.", "Once it passes, you check again and rewrite it.")),
        ("캐시 무효화", "Cache invalidation", ("답이 바뀌어서 메모판을 고치는 일.", "Fixing the board because the answer changed."), ("제때 안 고치면 틀린 답이 남아요.", "Forget to fix it in time, and the wrong answer stays.")),
        ("캐시 히트 / 미스", "Cache hit / miss", ("메모판에 있었는지(히트), 없었는지(미스).", "Whether the board already had it (hit) or not (miss)."), ("미스면 결국 창고까지 가야 해요.", "A miss still means a trip to the warehouse.")),
        ("캐시 스탬피드", "Cache stampede", ("손님들이 한꺼번에 메모판으로 몰리는 일.", "Everyone rushing the board at the same moment."), ("몰리는 그 순간은 오히려 더 느려요.", "That one moment is actually slower, not faster.")),
        ("캐시 계층", "Cache layers", ("안내소 메모판과 창구 메모판처럼 단계가 여럿인 것.", "Having more than one level, like a booth board and a gate board."), ("가까운 메모판부터 차례로 확인해요.", "The closest board gets checked first.")),
        ("일관성", "Consistency", ("메모판과 창고 답이 서로 맞는지.", "Whether the board and the warehouse agree."), ('조금 늦게 맞춰져도 괜찮을 때가 많아요. → <a href="reliability-ko.html">쉬지 않는 공원을 돌보는 사람들</a>', 'Often it\'s fine if they sync up a little late. → <a href="reliability-en.html">the people who keep the park open</a>')),
        ("레이턴시", "Latency", ("손님이 답을 받기까지 걸리는 시간.", "How long a guest waits for an answer."), ('메모판을 쓰면 이 시간이 확 줄어요. → <a href="goldensignals-ko.html">관제실의 계기판 네 개</a>', 'Using the board cuts this time way down. → <a href="goldensignals-en.html">the four gauges on the wall</a>')),
    ],
}
