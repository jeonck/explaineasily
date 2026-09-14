from _draw import *
from _world import *

CANDS = ("⟦좋다  ★★★★|nice   ★★★★⟧", "⟦춥다  ★★|cold   ★★⟧", "⟦바나나 ☆|banana ☆⟧")

# 1. 같은 질문에 앵무새가 매번 다른 답 — 손님 당황
P1 = svg(300, sky(300)
         + person(70, 110, s=0.9, face=FROWN, **GUEST) + bubble(20, 30, 220, 40, "⟦고양이 이름 하나만!|one name for my cat!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(100, 240, "⟦세 번 물었어요|asked three times⟧", 11, "var(--muted)")
         + perch(330, 200, 140) + parrot(330, 160, 1.1, talk=True)
         + bubble(430, 40, 150, 34, "⟦1번: 나비|1st: Nabi⟧", 12, "var(--panel)", "var(--line)", "left")
         + bubble(430, 100, 150, 34, "⟦2번: 구름|2nd: Cloud⟧", 12, "var(--panel)", "var(--line)", "left")
         + bubble(430, 160, 150, 34, "⟦3번: 치즈|3rd: Cheese⟧", 12, "var(--panel)", "var(--line)", "left")
         + label(660, 120, "⟦매번 달라요!|different every time!⟧", 12, "var(--accent)", cls="d")
         + label(380, 282, "⟦같은 질문인데 답이 자꾸 바뀌어요 — 왜?|same question, yet the answer keeps changing — why?⟧", 13, "var(--ink)"))

# 2. 왜: 다음 콩 후보가 여럿 — 늘 1등만 고르면 지루, 아래도 가끔 고르면 엉뚱
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + beans(80, 100, ("⟦오늘|Today⟧", "⟦날씨가|the weather⟧", "⟦참|is⟧"), 1.0, 60)
         + '<rect x="250" y="78" width="52" height="44" rx="8" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>' + label(276, 106, "⟦?|?⟧", 22, "var(--accent)", cls="d")
         + note(330, 40, 180, 130, "⟦다음 콩 후보|NEXT BEAN⟧", CANDS, 1.0, 0)
         + label(640, 70, "⟦늘 1등만 고르면|always pick the top⟧", 12, "var(--ink)", cls="d") + label(640, 90, "⟦똑같고 지루해요|same and boring⟧", 11, "var(--muted)")
         + label(640, 140, "⟦아래 것도 가끔 고르면|sometimes pick lower⟧", 12, "var(--ink)", cls="d") + label(640, 160, "⟦새롭지만 엉뚱해요|fresh but odd⟧", 11, "var(--muted)")
         + label(300, 215, "⟦후보가 여럿이에요 — 어느 걸 고를까요?|there are several candidates — which to pick?⟧", 12, "var(--ink)")
         + label(380, 282, "⟦1등만? 아래도? 고르는 버릇이 답을 바꿔요|only the top? lower too? the picking habit changes the answer⟧", 12, "var(--bad)"))

# 3. temperature = 엉뚱함 다이얼 (hero)
P3 = svg(360, sky(360)
         + label(200, 60, "⟦엉뚱함 다이얼|WHIMSY DIAL⟧", 14, "var(--ink)", cls="d")
         + dial(200, 140, 2.0, 0.5)
         + label(140, 215, "⟦0 늘 같은 답|0 same answer⟧", 11, "var(--muted)") + label(265, 215, "⟦높음 엉뚱한 답|high odd answers⟧", 11, "var(--muted)")
         + person(290, 110, s=0.9, face=SMILE, **TRAINER) + label(322, 245, "⟦조련사가 돌려요|the trainer turns it⟧", 11, "var(--muted)")
         + perch(500, 240, 150) + parrot(500, 200, 1.3, talk=True)
         + bubble_parrot(400, 60, 160, 40, "⟦춥다!|cold!⟧", 12)
         + note(580, 40, 160, 110, "⟦다음 콩 후보|NEXT BEAN⟧", CANDS, 1.0)
         + label(500, 300, "⟦다이얼 따라 1등 콩만, 또는 아래 콩도|top bean only, or lower beans too, as the dial says⟧", 11, "var(--muted)")
         + label(380, 340, "⟦temperature = 1등 콩만? 아래 콩도? 를 정하는 엉뚱함 다이얼|temperature is the whimsy dial: top bean only, or lower ones too⟧", 13, "var(--ink)", cls="d"))


def _col(x, level, txt, answer, desc, mood=""):
    return (dial(x, 62, 1.0, level, txt) + bubble(x - 80, 120, 160, 36, answer, 12, "var(--panel)", "var(--line)", "bottom")
            + parrot(x, 215, 1.0, talk=True, mood=mood) + label(x, 280, desc, 11, "var(--muted)"))


# 4. 다이얼 0 / 0.7 / 1.5 — 같은 질문, 답 셋
P4 = svg(320, sky(320)
         + label(380, 22, "⟦같은 질문: 고양이 이름 지어 줘|same question: name my cat⟧", 12, "var(--ink)", cls="d")
         + _col(130, 0.0, "⟦0|0⟧", "⟦나비, 나비, 나비|Nabi, Nabi, Nabi⟧", "⟦늘 같은 답|always the same⟧")
         + _col(380, 0.4, "⟦0.7|0.7⟧", "⟦나비, 구름, 치즈|Nabi, Cloud, Cheese⟧", "⟦조금씩 달라요|a little different⟧")
         + _col(630, 0.9, "⟦1.5|1.5⟧", "⟦양말 대왕 3세|Sock King III⟧", "⟦새롭지만 엉뚱해요|fresh but odd⟧", "sweat")
         + label(380, 304, "⟦다이얼만 달라요 — 답이 이렇게 달라져요|only the dial changes — and the answers change like this⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 다이얼을 올려도 새 지식은 안 생겨요 + 할루시네이션 위험
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + dial(90, 110, 1.2, 1.0, "⟦끝까지 올려도|all the way up⟧")
         + note(160, 50, 190, 130, "⟦다음 콩 후보|NEXT BEAN⟧", CANDS, 1.0)
         + label(190, 215, "⟦후보 목록은 그대로예요|the candidate list stays the same⟧", 11, "var(--ink)")
         + label(190, 240, "⟦읽은 책 밖의 콩은 안 나와요|no bean from outside its books⟧", 11, "var(--muted)")
         + parrot(470, 140, 1.0, color=PARROT_BAD, talk=True, mood="sweat")
         + bubble_parrot(520, 50, 210, 40, "⟦고양이는 달에서 왔어요|cats came from the moon⟧", 11, bad=True)
         + label(590, 210, "⟦높을수록 엉뚱한 콩이 자주 나와요|higher means odd beans slip in more⟧", 11, "var(--ink)")
         + label(590, 235, "⟦그럴듯한 거짓말 위험도 커져요|and plausible lies get likelier⟧", 11, "var(--bad)")
         + label(380, 300, "⟦다이얼은 고르는 버릇만 바꿔요 — 새 지식은 안 생겨요|the dial only changes the picking habit — no new knowledge appears⟧", 12, "var(--ink)", cls="d"))

LOW_I = icon('<circle cx="32" cy="34" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 L17 44" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="4" fill="var(--accent)"/><text x="12" y="16" font-size="12" font-weight="700" fill="var(--muted)">0</text>')
HIGH_I = icon('<circle cx="32" cy="34" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/><path d="M32 34 L47 44" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="34" r="4" fill="var(--accent)"/><path d="M50 8 l3 6 l6 3 l-6 3 l-3 6 l-3 -6 l-6 -3 l6 -3z" fill="var(--accent)"/>')
FACT_I = icon('<rect x="12" y="10" width="40" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 22 h24 M20 30 h24 M20 38 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M38 44 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none"/>')
SAME_I = icon(f'<ellipse cx="20" cy="40" rx="12" ry="8" fill="{BEAN}"/><ellipse cx="44" cy="40" rx="12" ry="8" fill="{BEAN}"/><path d="M14 38 q6 -4 12 0 M38 38 q6 -4 12 0" stroke="#5A3B22" stroke-width="1.5" fill="none"/><path d="M20 14 q6 8 12 0 q6 -8 12 0" stroke="var(--muted)" stroke-width="3" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "temperature", "order": 11,
    "title": ("엉뚱함 다이얼", "The Whimsy Dial"),
    "h1": ("<em>temperature</em>가 뭐예요?", "What is <em>temperature</em>?"),
    "sub": ("temperature(온도)를 앵무새가 1등 콩만 고를지 아래 콩도 가끔 고를지 정하는 엉뚱함 다이얼 이야기로 풀어봤어요.",
            "Temperature, told as a story about a dial that decides whether the parrot picks only the top bean or sometimes a lower one."),
    "panels": [
        {"svg": P1, "alt": ("손님이 '고양이 이름 하나만!'이라고 세 번 묻고, 횃대 위 앵무새가 나비, 구름, 치즈라고 매번 다르게 답함", "A guest asks for one cat name three times; the parrot on the perch answers Nabi, Cloud, Cheese — different each time"),
         "caption": ("같은 질문인데 답이 자꾸 바뀌어요.", "Same question, yet the answer keeps changing."),
         "small": ("어제는 나비, 오늘은 구름, 방금은 치즈. 손님은 앵무새가 고장 났나 싶어요.", "Yesterday Nabi, today Cloud, just now Cheese. The guest wonders if the parrot is broken.")},
        {"svg": P2, "alt": ("'오늘 날씨가 참 …' 콩 세 개와 물음표, '다음 콩 후보' 쪽지에 좋다 ★★★★, 춥다 ★★, 바나나 ☆. 오른쪽: 늘 1등만 고르면 똑같고 지루, 아래 것도 가끔 고르면 새롭지만 엉뚱", "Three beans reading Today the weather is … and a question mark; a note ranks next beans nice ★★★★, cold ★★, banana ☆; on the right: always the top is boring, sometimes lower is fresh but odd"),
         "caption": ("다음 콩 후보가 여럿이에요. 어느 걸 고를지가 문제예요.", "There are several candidates for the next bean. Which one to pick is the question."),
         "small": ('늘 1등 <a href="token-ko.html">콩</a>만 고르면 답이 똑같고 지루해요. 아래 콩도 가끔 고르면 새롭지만 가끔 엉뚱해요.',
                   'Always pick the top <a href="token-en.html">bean</a> and the answer is the same and boring. Sometimes pick a lower one and it is fresh — but sometimes odd.')},
        {"svg": P3, "hero": True, "alt": ("큰 엉뚱함 다이얼(0 늘 같은 답 … 높음 엉뚱한 답)을 조련사가 돌리고, 횃대 위 앵무새가 '춥다!'라고 답함. 옆에 다음 콩 후보 쪽지", "A big whimsy dial (0 same answer … high odd answers) turned by the trainer; the parrot on the perch says cold!; a next-bean candidate note beside it"),
         "caption": ("temperature는 1등 콩만 고를지, 아래 콩도 가끔 고를지 정하는 엉뚱함 다이얼이에요.", "Temperature is the whimsy dial: only the top bean, or sometimes a lower one."),
         "small": ("다이얼을 0에 두면 늘 1등 콩. 올릴수록 아래 콩도 자주 뽑혀요. 조련사가 일에 맞게 돌려요.", "At 0 the parrot always takes the top bean. The higher the dial, the more often a lower bean gets picked. The trainer sets it to fit the job."),
         "tricks": (4, [
             (LOW_I, ("0에 가까우면 늘 같은 답", "Near 0: the same answer"), ("정리·코드·뽑아내기에 좋아요", "good for sorting, code, extraction"), "calm"),
             (HIGH_I, ("높이면 새로운 답", "Higher: fresh answers"), ("아이디어·이야기에 좋아요", "good for ideas and stories")),
             (FACT_I, ("사실 질문은 낮게", "Facts: keep it low"), ("엉뚱한 콩이 끼면 틀려요", "an odd bean makes it wrong"), "warm"),
             (SAME_I, ("같은 다이얼도 완전히 같진 않아요", "Same dial, not identical"), ("0이어도 가끔 달라요", "even at 0 it can differ a bit"), "warm"),
         ])},
        {"svg": P4, "alt": ("같은 질문 '고양이 이름 지어 줘'에 다이얼 0은 나비, 나비, 나비 / 0.7은 나비, 구름, 치즈 / 1.5는 양말 대왕 3세(땀 흘리는 앵무새)", "Same question, name my cat: dial 0 gives Nabi, Nabi, Nabi; 0.7 gives Nabi, Cloud, Cheese; 1.5 gives Sock King III from a sweating parrot"),
         "caption": ("다이얼만 달라요. 답이 이렇게 달라져요.", "Only the dial changes — and the answers change like this."),
         "small": ("0은 늘 같은 답, 0.7은 조금씩 다른 답, 1.5는 새롭지만 엉뚱한 답. 대부분의 일은 가운데쯤이 편해요.", "0 always gives the same answer, 0.7 varies a little, 1.5 gets fresh but odd. Most jobs sit comfortably in the middle.")},
        {"svg": P5, "alt": ("왼쪽 초록: 다이얼을 끝까지 올려도 다음 콩 후보 쪽지는 그대로. 오른쪽 빨강: 빨간 앵무새가 '고양이는 달에서 왔어요' — 높을수록 그럴듯한 거짓말 위험이 커짐", "Left, green: even with the dial all the way up the candidate note is unchanged. Right, red: a red parrot says cats came from the moon — the higher the dial, the likelier a plausible lie"),
         "caption": ("다이얼은 고르는 버릇만 바꿔요. 새 지식은 안 생겨요.", "The dial only changes the picking habit. No new knowledge appears."),
         "small": ('있는 후보 중에서 고를 뿐이라 읽은 책 밖의 콩은 안 나와요. 대신 높일수록 <a href="hallucination-ko.html">그럴듯한 거짓말</a>이 끼기 쉬워요.',
                   'It only picks among the candidates it has, so no bean from outside its books appears. But the higher the dial, the easier a <a href="hallucination-en.html">plausible lie</a> slips in.')},
    ],
    "summary": (("<b>temperature</b> = 앵무새가 <b>1등 콩만</b> 고를지 <b>아래 콩도 가끔</b> 고를지 정하는 <b>엉뚱함 다이얼</b>. 낮으면 늘 같은 답, 높이면 새롭지만 엉뚱한 답 — 새 지식이 생기는 건 아니에요.",
                 "<b>Temperature</b> = the <b>whimsy dial</b> that decides whether the parrot picks <b>only the top bean</b> or <b>sometimes a lower one</b>. Low means the same answer every time, high means fresh but odd answers — and no new knowledge either way."),
                ("다음 토큰 확률 분포를 얼마나 평평하게 만들지 정하는 샘플링 파라미터예요. 0에 가까우면 최고 확률 토큰만 골라 거의 결정적이고, 높이면 낮은 확률 토큰도 뽑혀 다양해지지만 오류·할루시네이션 확률이 올라가요. top-p, top-k 와 함께 써요.",
                 "A sampling parameter that flattens or sharpens the next-token probability distribution. Near 0 it almost always takes the top token (near-deterministic); higher values let low-probability tokens through — more variety, more errors and hallucinations. Used together with top-p and top-k.")),
    "glossary": [
        ("temperature", "Temperature", ("엉뚱함 다이얼.", "The whimsy dial."), ("0에 가까우면 1등 콩만, 높이면 아래 콩도 가끔. 보통 0~2 사이.", "Near 0 only the top bean; higher lets lower beans in. Usually between 0 and 2.")),
        ("샘플링", "Sampling", ("후보 중에서 하나 뽑기.", "Drawing one from the candidates."), ("별 개수(확률)에 따라 콩을 뽑는 일. 다이얼은 이 뽑기의 버릇을 바꿔요.", "Picking a bean according to its stars (probability). The dial changes how this draw behaves.")),
        ("top-p", "Top-p (nucleus)", ("별 합이 p가 될 때까지만 후보로.", "Keep candidates until their stars add up to p."), ("바나나 ☆ 같은 꼬리 후보를 잘라내요. 다이얼과 같이 써요.", "Cuts off tail candidates like banana ☆. Used together with the dial.")),
        ("top-k", "Top-k", ("위에서 k개만 후보로.", "Only the top k candidates."), ("예: k=3이면 좋다·춥다·바나나까지만.", "For example k=3 keeps nice, cold, banana only.")),
        ("결정적 출력", "Deterministic output", ("다이얼 0.", "Dial at 0."), ("늘 1등 콩이라 거의 같은 답. 완전히 똑같진 않을 수 있어요.", "Always the top bean, so nearly the same answer — though not guaranteed identical.")),
        ("시드", "Seed", ("뽑기 주사위의 시작 번호.", "The starting number of the draw dice."), ("같은 시드면 같은 뽑기가 나오도록 해 봐요. 모든 앵무새가 지원하진 않아요.", "Same seed, same draw — in principle. Not every parrot supports it.")),
        ("창의성 vs 정확성", "Creativity vs accuracy", ("다이얼의 양 끝.", "The two ends of the dial."), ("이야기·아이디어는 높게, 사실·코드·정리는 낮게.", "Stories and ideas high; facts, code and sorting low.")),
        ("다음 토큰 후보", "Next-token candidates", ("다음 콩 후보 쪽지.", "The next-bean note."), ('별이 많은 콩이 1등. → <a href="token-ko.html">콩</a>', 'The bean with the most stars is the top. → <a href="token-en.html">beans</a>')),
    ],
}
