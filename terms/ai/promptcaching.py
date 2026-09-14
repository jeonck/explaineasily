from _draw import *
from _world import *

GREY = "#8A93A3"  # 이미 읽어 둔 콩
RULES = ("⟦규정|rule⟧",)


def arrow(x1, y1, x2, y2):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<path d="M{x2 - 10} {y2 - 8} L{x2} {y2} L{x2 - 10} {y2 + 8}" stroke="var(--muted)" stroke-width="3" fill="none"/>')


# 1. 손님이 매번 같은 긴 규정집을 쟁반에 올려요 — 콩 값과 시간이 매번
P1 = svg(300, sky(300)
         + person(60, 110, s=0.9, face=FROWN, **GUEST)
         + note(150, 50, 150, 150, "⟦규정집 (30장)|RULEBOOK (30 pages)⟧", ("⟦1. 환불은 7일|1. refunds: 7 days⟧", "⟦2. 배송은 3일|2. delivery: 3 days⟧", "⟦3. …|3. …⟧", "⟦(매번 같은 내용)|(same every time)⟧"), 1.0)
         + label(225, 232, "⟦아침, 점심, 저녁 매번 올려요|morning, noon, night — every time⟧", 11, "var(--muted)")
         + arrow(310, 125, 335, 125)
         + tray(340, 120, 220, 70, "⟦쟁반|tray⟧") + beans(370, 108, RULES * 4 + ("⟦질문|Q⟧",), 0.9, 44)
         + label(450, 70, "⟦매번: 콩 값 + 기다림|every time: bean cost + waiting⟧", 12, "var(--bad)", cls="d")
         + parrot(650, 150, 1.0, mood="sweat") + label(650, 215, "⟦또 처음부터…|from the top again…⟧", 11, "var(--muted)")
         + label(380, 282, "⟦같은 규정집을 매번 다시 올려요 — 값도 시간도 매번 들어요|the same rulebook goes on the tray every time — paying and waiting every time⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새는 쟁반 위 콩을 매번 처음부터 다시 읽어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + label(270, 60, "⟦앵무새는 쟁반 위 콩을 매번 처음부터 다시 읽어요|the parrot re-reads every bean on the tray from the start⟧", 12, "var(--ink)", cls="d")
         + tray(60, 110, 420, 70) + beans(90, 98, RULES * 6 + ("⟦질문|Q⟧",), 0.9, 55)
         + '<path d="M90 130 L440 130" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><path d="M430 122 L442 130 L430 138" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + label(270, 205, "⟦읽은 콩 수만큼 값을 내고, 기다려요|you pay and wait for every bean it reads⟧", 11, "var(--muted)")
         + parrot(600, 130, 1.1, mood="sweat") + label(600, 215, "⟦같은 걸 또, 또|the same thing, again and again⟧", 11, "var(--muted)")
         + note(660, 40, 90, 60, "⟦청구서|BILL⟧", ("⟦100콩 × 3|100 beans × 3⟧",), 0.9)
         + label(380, 282, "⟦앞부분이 똑같아도 앵무새는 모르고 다시 읽어요|even when the front is identical, the parrot does not know — it reads again⟧", 12, "var(--bad)"))

# 3. 프롬프트 캐싱 = 자주 쓰는 앞부분 콩을 미리 놓아두고, 새 콩만 올리기 (hero)
P3 = svg(360, sky(360)
         + label(180, 70, "⟦미리 놓아둔 콩 (이미 읽음)|beans laid out ahead (already read)⟧", 12, "var(--muted)", cls="d")
         + label(390, 70, "⟦새 콩만|only new⟧", 12, "var(--accent)", cls="d")
         + tray(40, 120, 420, 80) + beans(80, 108, RULES * 5, 0.9, 50, GREY) + beans(360, 108, ("⟦질문|Q⟧", "⟦?|?⟧"), 0.9, 50)
         + '<path d="M62 140 v8 h236 v-8" stroke="var(--muted)" stroke-width="2" fill="none"/><path d="M340 140 v8 h80 v-8" stroke="var(--accent)" stroke-width="2" fill="none"/>'
         + label(250, 235, "⟦앞부분은 건너뛰고, 새 콩만 읽어요|skips the front, reads only the new beans⟧", 12, "var(--ink)")
         + perch(600, 250, 150) + parrot(600, 210, 1.3, talk=True)
         + bubble_parrot(500, 60, 200, 40, "⟦앞부분은 기억나요!|I remember the front!⟧", 12)
         + person(690, 130, s=0.8, face=SMILE, **TRAINER) + label(718, 240, "⟦조련사|trainer⟧", 11, "var(--muted)")
         + label(380, 300, "⟦앞부분이 똑같을 때만 돼요|only works while the front is identical⟧", 11, "var(--muted)")
         + label(380, 340, "⟦프롬프트 캐싱 = 자주 쓰는 앞부분 콩을 미리 놓아두고, 새 콩만 올리기|prompt caching: lay out the usual front beans ahead, then add only the new ones⟧", 13, "var(--ink)", cls="d"))

# 4. 쟁반 두 장 비교: 캐시 없음 vs 캐시 있음
P4 = svg(320, sky(320)
         + label(30, 30, "⟦캐시 없음|NO CACHE⟧", 13, "var(--bad)", cls="d", anchor="start")
         + tray(60, 70, 460, 60) + beans(90, 58, RULES * 6 + ("⟦질문|Q⟧", "⟦?|?⟧"), 0.9, 55)
         + note(560, 40, 160, 80, "⟦값|COST⟧", ("⟦100콩 전부|all 100 beans⟧", "⟦느려요|slow⟧"), 0.9)
         + label(30, 160, "⟦캐시 있음|WITH CACHE⟧", 13, "var(--good)", cls="d", anchor="start")
         + tray(60, 200, 460, 60) + beans(90, 188, RULES * 6, 0.9, 55, GREY) + beans(420, 188, ("⟦질문|Q⟧", "⟦?|?⟧"), 0.9, 55)
         + note(560, 170, 160, 80, "⟦값|COST⟧", ("⟦새 콩 20개만|only 20 new beans⟧", "⟦빨라요|fast⟧"), 0.9)
         + label(290, 283, "⟦회색 콩 = 미리 놓아둔 콩, 값은 조금만|grey beans = laid out ahead, tiny cost⟧", 11, "var(--muted)")
         + label(380, 304, "⟦앞부분이 같으면 두 번째부터 싸고 빨라요|same front, so from the second time it is cheap and fast⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 앞부분을 한 글자만 바꿔도 처음부터 — 쪽지 순서 설계
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + note(40, 50, 150, 130, "⟦앞: 안 바뀌는 것|FRONT: fixed⟧", ("⟦주인 쪽지|owner note⟧", "⟦규정집|rulebook⟧", "⟦예시|samples⟧"), 1.0)
         + note(210, 50, 150, 90, "⟦뒤: 바뀌는 것|BACK: changes⟧", ("⟦손님 질문|guest question⟧", "⟦오늘 날짜|the date⟧"), 1.0)
         + label(200, 215, "⟦고정된 것은 앞, 바뀌는 건 뒤|fixed at the front, changing at the back⟧", 11, "var(--ink)")
         + label(200, 240, "⟦✓ 캐시가 살아요|✓ the cache stays alive⟧", 12, "var(--good)", cls="d")
         + note(420, 50, 150, 130, "⟦앞|FRONT⟧", ("⟦오늘 날짜: 9/14|the date: 9/14⟧", "⟦주인 쪽지|owner note⟧", "⟦규정집|rulebook⟧"), 1.0, 0)
         + label(495, 200, "⟦한 글자만 달라도|one character differs⟧", 11, "var(--ink)")
         + parrot(660, 120, 1.0, mood="sweat") + label(660, 200, "⟦처음부터 다시!|from the top again!⟧", 11, "var(--bad)")
         + label(570, 240, "⟦× 캐시가 깨져요|× the cache breaks⟧", 12, "var(--bad)", cls="d")
         + label(380, 300, "⟦쪽지 순서 설계가 중요해요 — 앞은 늘 똑같이|so the order of notes matters — keep the front identical⟧", 12, "var(--ink)", cls="d"))

FRONT_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="28" rx="3" fill="#8A93A3" opacity="0.6"/><path d="M20 44 h24 M20 50 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
BACK_I = icon(f'<ellipse cx="18" cy="34" rx="11" ry="7" fill="#8A93A3"/><ellipse cx="40" cy="34" rx="11" ry="7" fill="{BEAN}"/><text x="40" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="#FFF8E7">?</text><path d="M52 18 l4 -6 M56 24 l6 -3" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
BREAK_I = icon('<rect x="10" y="12" width="20" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="36" y="12" width="20" height="40" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M30 12 l4 8 l-4 8 l4 8 l-4 8 l4 8" stroke="var(--bad)" stroke-width="3" fill="none"/>')
CLOCK_I = icon('<circle cx="32" cy="34" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 V18 M32 34 L42 40" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="3" fill="var(--accent)"/>')

PAGE = {
    "slug": "promptcaching", "order": 12,
    "title": ("미리 놓아둔 콩", "Beans Laid Out Ahead"),
    "h1": ("<em>프롬프트 캐싱</em>이 뭐예요?", "What is <em>prompt caching</em>?"),
    "sub": ("프롬프트 캐싱을 자주 쓰는 앞부분 콩을 미리 놓아두고 새 콩만 올리는 쟁반 이야기로 풀어봤어요.",
            "Prompt caching, told as a story about laying out the usual front beans ahead of time and adding only the new ones."),
    "panels": [
        {"svg": P1, "alt": ("손님이 30장짜리 규정집을 아침, 점심, 저녁 매번 쟁반에 올림. 쟁반 위 규정 콩 넷과 질문 콩 하나, '매번: 콩 값 + 기다림', 땀 흘리는 앵무새 '또 처음부터…'", "A guest puts a 30-page rulebook on the tray morning, noon and night; four rule beans and one question bean on the tray, every time: bean cost + waiting; a sweating parrot says from the top again"),
         "caption": ("같은 규정집을 매번 다시 올려요. 값도 시간도 매번 들어요.", "The same rulebook goes on the tray every time — and costs money and time every time."),
         "small": ('질문은 한 줄인데 규정집이 30장이에요. 앵무새는 30장을 다 읽고 나서야 답해요. <a href="pricing-ko.html">콩 값</a>이 매번 들어요.',
                   'The question is one line, but the rulebook is 30 pages. The parrot reads all 30 before answering — and the <a href="pricing-en.html">bean cost</a> comes every time.')},
        {"svg": P2, "alt": ("쟁반 위 규정 콩 여섯과 질문 콩, 처음부터 끝까지 읽는 점선 화살표, 땀 흘리는 앵무새, '100콩 × 3' 청구서", "Six rule beans and a question bean on the tray, a dotted arrow reading from start to end, a sweating parrot, a bill for 100 beans × 3"),
         "caption": ("앵무새는 쟁반 위 콩을 매번 처음부터 다시 읽어요.", "The parrot re-reads every bean on the tray from the start, every time."),
         "small": ('앞부분이 어제와 똑같아도 앵무새는 몰라요. <a href="context-ko.html">쟁반</a>에 올라온 콩은 전부 새로 읽고, 읽은 만큼 값을 내요.',
                   'Even if the front is identical to yesterday, the parrot cannot tell. Every bean on the <a href="context-en.html">tray</a> is read fresh, and you pay for each.')},
        {"svg": P3, "hero": True, "alt": ("쟁반 앞쪽에 회색 콩 다섯(미리 놓아둔 콩, 이미 읽음), 뒤에 새 콩 둘(질문). 횃대 위 앵무새 '앞부분은 기억나요!', 옆에 조련사", "Five grey beans at the front of the tray (laid out ahead, already read) and two new beans at the back; the parrot on the perch says I remember the front; a trainer beside it"),
         "caption": ("프롬프트 캐싱은 자주 쓰는 앞부분 콩을 미리 놓아두고, 새 콩만 올리는 거예요.", "Prompt caching lays out the usual front beans ahead of time, then adds only the new ones."),
         "small": ("앵무새가 한 번 읽은 앞부분을 잠깐 기억해 둬요. 다음 손님 때는 앞부분을 건너뛰고 새 콩만 읽어요 — 싸고 빨라요.", "The parrot briefly remembers a front part it has already read. For the next guest it skips that part and reads only the new beans — cheaper and faster."),
         "tricks": (4, [
             (FRONT_I, ("안 바뀌는 건 앞에", "Fixed things go first"), ("규정집·주인 쪽지·예시", "rulebook, owner note, samples"), "calm"),
             (BACK_I, ("바뀌는 건 뒤에", "Changing things go last"), ("손님 질문은 맨 뒤", "the guest question at the end")),
             (BREAK_I, ("순서가 바뀌면 깨져요", "Reorder it and it breaks"), ("앞부분은 글자 하나까지 똑같이", "the front must match to the letter"), "warm"),
             (CLOCK_I, ("잠깐만 살아요", "It lives only a while"), ("몇 분 지나면 다시 읽어요", "after some minutes it reads again"), "warm"),
         ])},
        {"svg": P4, "alt": ("위: 캐시 없음 — 쟁반의 콩 여덟이 모두 갈색, 값은 100콩 전부, 느림. 아래: 캐시 있음 — 앞 여섯은 회색(이미 읽음), 새 콩 둘만 갈색, 값은 새 콩 20개만, 빠름", "Top: no cache — all eight beans on the tray are brown, cost all 100 beans, slow. Bottom: with cache — the first six are grey (already read), only two new beans brown, cost only 20 new beans, fast"),
         "caption": ("앞부분이 같으면 두 번째부터 싸고 빨라요.", "With the same front, it is cheap and fast from the second time on."),
         "small": ("회색 콩은 값을 조금만 내요. 첫 번째는 놓아두는 값이 조금 더 들지만, 두 번째부터 이득이에요.", "Grey beans cost only a little. The first time costs slightly more to lay them out; from the second time on you win.")},
        {"svg": P5, "alt": ("왼쪽 초록: 앞 쪽지(주인 쪽지·규정집·예시)와 뒤 쪽지(손님 질문·오늘 날짜), 캐시가 살아요. 오른쪽 빨강: 앞 쪽지 맨 위에 '오늘 날짜: 9/14' — 한 글자만 달라도 처음부터 다시, 캐시가 깨져요", "Left, green: a front note (owner note, rulebook, samples) and a back note (guest question, the date) — the cache stays alive. Right, red: the date 9/14 at the top of the front note — one character differs, from the top again, the cache breaks"),
         "caption": ("앞부분을 한 글자만 바꿔도 처음부터예요. 그래서 쪽지 순서 설계가 중요해요.", "Change one character at the front and it starts over. That is why the order of notes matters."),
         "small": ('오늘 날짜나 손님 이름을 <a href="prompt-ko.html">주인 쪽지</a> 맨 위에 쓰면 매번 깨져요. 바뀌는 건 뒤로 보내세요.',
                   'Put the date or the guest name at the top of the <a href="prompt-en.html">owner note</a> and it breaks every time. Move what changes to the back.')},
    ],
    "summary": (("<b>프롬프트 캐싱</b> = 자주 쓰는 <b>앞부분 콩을 미리 놓아두고</b>, 다음엔 <b>새 콩만 올리기</b>. 안 바뀌는 건 앞에, 바뀌는 건 뒤에 — 앞부분이 한 글자라도 다르면 처음부터예요.",
                 "<b>Prompt caching</b> = <b>lay out the usual front beans ahead</b>, then <b>add only the new ones</b>. Fixed things go first, changing things last — if the front differs by one character, it starts over."),
                ("Prompt caching. 프롬프트의 앞부분(프리픽스)을 처리한 결과를 짧은 시간(TTL) 동안 저장해 두고, 같은 프리픽스로 시작하는 다음 요청에서 재사용해요. 캐시 적중이면 입력 토큰 비용이 크게 줄고 지연 시간도 짧아져요. 시스템 프롬프트·긴 문서·예시를 앞에, 사용자 질문을 뒤에 두는 배치가 핵심이에요.",
                 "Stores the processed result of a prompt prefix for a short time (TTL) and reuses it for later requests that start with the same prefix. On a cache hit, input-token cost drops sharply and latency shrinks. The key is layout: system prompt, long documents and examples first, the user question last.")),
    "glossary": [
        ("프롬프트 캐싱", "Prompt caching", ("미리 놓아둔 콩.", "Beans laid out ahead."), ("앞부분을 한 번 읽어 두고 다음엔 건너뛰어요. 싸고 빨라요.", "Read the front once, skip it next time. Cheaper and faster.")),
        ("캐시 적중", "Cache hit", ("앞부분이 딱 맞았어요.", "The front matched exactly."), ("회색 콩으로 처리돼요. 안 맞으면 캐시 미스 — 전부 다시.", "Handled as grey beans. If it does not match, a cache miss — everything again.")),
        ("프리픽스", "Prefix", ("쟁반 앞부분.", "The front of the tray."), ("첫 콩부터 어디까지 똑같은지. 여기까지만 캐시가 돼요.", "How far from the first bean things are identical. Only that part is cached.")),
        ("TTL", "TTL (time to live)", ("잠깐만 살아요.", "It lives only a while."), ("보통 몇 분. 지나면 다시 놓아둬야 해요.", "Usually a few minutes. After that it must be laid out again.")),
        ("시스템 프롬프트 배치", "System prompt placement", ("주인 쪽지는 맨 앞에.", "The owner note goes first."), ('안 바뀌는 쪽지가 앞에 있어야 캐시가 살아요. → <a href="prompt-ko.html">조련 쪽지</a>', 'The fixed note must sit at the front for the cache to survive. → <a href="prompt-en.html">the trainer note</a>')),
        ("컨텍스트", "Context", ("쟁반.", "The tray."), ('캐시는 쟁반 위 콩의 앞부분을 기억해요. → <a href="context-ko.html">앵무새 앞의 쟁반</a>', 'The cache remembers the front of the beans on the tray. → <a href="context-en.html">the tray</a>')),
        ("비용", "Cost", ("콩 값.", "The bean price."), ('회색 콩은 값이 훨씬 싸요. → <a href="pricing-ko.html">콩 값</a>', 'Grey beans are much cheaper. → <a href="pricing-en.html">the bean price</a>')),
        ("지연 시간", "Latency", ("답이 나오기까지 기다림.", "The wait until an answer."), ('앞부분을 건너뛰니 첫 답이 빨라요. → <a href="inference-ko.html">앵무새가 답하는 값과 시간</a>', 'Skipping the front makes the first answer faster. → <a href="inference-en.html">what answering costs</a>')),
    ],
}
