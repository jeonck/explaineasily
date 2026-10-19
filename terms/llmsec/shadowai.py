from _draw import *
from _world import *

STAFF = dict(hat=None, shirt="#6B5B95")  # 직원 (세계관 인물표엔 없는, 현장에서 일하는 사람)


def box(x, y, s=1.0, warn=False):
    """뒷문으로 몰래 들어오는 포장 상자 (섀도 AI 도구). warn=True 면 물음표가 붙어요."""
    c = "var(--bad)" if warn else "#C9A86A"
    out = (f'<g transform="translate({x},{y}) scale({s})">'
           f'<rect x="-26" y="-20" width="52" height="40" rx="3" fill="#D8B57A" stroke="{c}" stroke-width="3"/>'
           f'<path d="M-26 -4 h52 M0 -20 v40" stroke="#8B5E3C" stroke-width="2"/>')
    if warn:
        out += '<text x="0" y="6" text-anchor="middle" font-size="22" font-weight="700" fill="var(--bad)">?</text>'
    return out + '</g>'


# 1. 정식 도구는 승인 대기 중인데, 뒷문으론 상자가 몰래 들어와요
P1 = svg(320, sky(320)
         + board(30, 24, 230, 86, "⟦정식 도구 신청|OFFICIAL TOOL REQUEST⟧", ("⟦승인 대기 중...|still pending...⟧",), 0.95)
         + person(120, 280 - 112 * 0.65, s=0.65, face=SWEAT, **STAFF)
         + label(153, 300, "⟦기다리는 직원|an employee, waiting⟧", 11, "var(--muted)")
         + '<rect x="560" y="50" width="10" height="230" fill="#8B5E3C"/>' + label(565, 40, "⟦뒷문|BACK DOOR⟧", 11, "var(--muted)")
         + person(640, 280 - 112 * 0.6, s=0.6, face=SMILE, **STAFF) + box(715, 232, 0.9, warn=True)
         + label(685, 300, "⟦몰래 들여온 상자|a box brought in quietly⟧", 11, "var(--bad)")
         + label(380, 312, "⟦승인을 기다리기 지겨워서, 뒷문으로 다른 걸 몰래 들여와요|tired of waiting, someone brings something else in through the back⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 사장님은 앞문만 봐요 — 뒷문은 아예 안 보여요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(140, 260 - 112 * 0.7, s=0.7, face=EYES, **MANAGER)
         + bubble(40, 50, 230, 54, "⟦이 상자는 처음 보는데...|I've never seen this box before...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + box(430, 195, 1.0, warn=True) + person(480, 260 - 112 * 0.55, s=0.55, face=SMILE, **STAFF)
         + logbook(600, 140, 0.9) + label(650, 230, "⟦장부엔 안 적혀요|it's not written in the logbook⟧", 11, "var(--muted)")
         + label(380, 280, "⟦직원은 그냥 빨리 끝내고 싶었을 뿐이지만, 사장님은 이 상자를 아예 볼 수가 없어요|the employee just wanted to finish faster — the manager can't see this box at all⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 섀도 AI = 회사 몰래 들여와 쓰는 바깥 도구
P3 = svg(360, sky(360)
         + label(380, 30, "⟦섀도 AI = 회사가 모르는 사이 몰래 들여와 쓰는 바깥 도구예요|Shadow AI = an outside tool quietly brought in and used, without the company knowing⟧", 13, "var(--ink)", cls="d")
         + board(40, 60, 230, 150, "⟦앞문 (정식)|FRONT DOOR (official)⟧", ("⟦신청 → 승인|request → approval⟧", "⟦검수대 거쳐요|through the taster⟧", "⟦장부에 기록|logged in the book⟧"), 0.95)
         + '<path d="M300 150 H460" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 4"/>'
         + box(560, 130, 1.1, warn=True) + person(640, 300 - 112 * 0.6, s=0.6, face=SMILE, **STAFF)
         + '<path d="M558 155 Q580 205 640 232" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + label(600, 320, "⟦뒷문 (섀도) — 검사를 다 건너뛰어요|BACK DOOR (shadow) — skips every check⟧", 12, "var(--bad)")
         + label(380, 345, "⟦앞문은 겹겹이 검사하지만, 뒷문 상자는 아무도 몰라요|the front door checks layer by layer — nobody even knows about the back-door box⟧", 12, "var(--muted)"))

# 4. 앞문과 뒷문을 나란히 비교해요
P4 = svg(330, sky(330)
         + board(40, 30, 320, 270, "⟦앞문 (정식 도구)|FRONT DOOR (sanctioned)⟧",
                 ("⟦승인: 사장님이 허락|approval: the manager signs off⟧",
                  "⟦검수: 맛보기 검수원이 봐요|check: the taster looks it over⟧",
                  "⟦기록: 장부에 남아요|record: written in the logbook⟧",
                  "⟦권한: 칼서랍만큼만|access: only what the drawer allows⟧"), 1.0)
         + board(400, 30, 320, 270, "⟦뒷문 (섀도 도구)|BACK DOOR (shadow tool)⟧",
                 ("⟦승인: 아무도 몰라요|approval: nobody signed off⟧",
                  "⟦검수: 건너뛰어요|check: skipped entirely⟧",
                  "⟦기록: 장부에 없어요|record: not in any logbook⟧",
                  "⟦권한: 뭐든 다 넣을 수 있어요|access: whatever goes in, goes⟧"), 1.0)
         + label(380, 318, "⟦같은 일을 시켜도, 앞문과 뒷문은 완전히 다르게 다뤄져요|the same task is handled completely differently at the front door vs. the back⟧", 12, "var(--ink)"))

# 5. 결과·한계·이웃 차이: 터져야 알아요, 금지만으론 못 막아요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + box(140, 115, 1.1, warn=True) + person(140, 300 - 112 * 0.7, s=0.7, face=FROWN, **STAFF)
         + label(140, 170, "⟦비밀 재료가 그 상자로 같이 나가요|a secret ingredient slips out through that same box⟧", 11, "var(--bad)")
         + label(190, 313, "⟦터지고 나서야 알아요|found out only after it breaks⟧", 12, "var(--bad)", cls="d")
         + board(420, 50, 300, 190, "⟦규칙판엔 이미 적혀 있어요|THE RULES BOARD ALREADY SAYS SO⟧",
                 ("⟦\"뒷문 금지\" 라고만 써봐야|just writing \"no back door\" isn't enough⟧",
                  "⟦앞문을 더 빠르게 만들어야|the front door has to get faster too⟧"), 1.0)
         + label(570, 282, "⟦금지보다 '더 빠른 앞문'이 섀도 AI를 줄여요|a faster front door shrinks shadow AI more than a ban does⟧", 12, "var(--ink)", cls="d"))

NOBODY_I = icon('<rect x="8" y="20" width="48" height="30" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M14 42 h20" stroke="#142033" stroke-width="2.5"/><path d="M10 10 L54 54 M54 10 L10 54" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
SKIP_I = icon('<rect x="22" y="8" width="8" height="34" fill="var(--good)"/><rect x="38" y="8" width="8" height="34" fill="var(--good)"/><rect x="18" y="16" width="32" height="6" fill="var(--good)"/><rect x="18" y="30" width="32" height="6" fill="var(--good)"/><path d="M8 52 L56 12" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')
LEAK_I = icon('<rect x="14" y="20" width="30" height="24" rx="3" fill="#D8B57A" stroke="var(--bad)" stroke-width="3"/><path d="M44 32 L58 32" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/><path d="M52 26 L58 32 L52 38" stroke="var(--bad)" stroke-width="4" fill="none" stroke-linecap="round"/>')
RESP_I = icon('<path d="M32 8 L50 16 V34 C50 46 42 54 32 58 C22 54 14 46 14 34 V16 Z" fill="var(--accent)"/><rect x="29" y="22" width="6" height="18" rx="2" fill="#FFF8E7"/><circle cx="32" cy="46" r="3" fill="#FFF8E7"/>')

PAGE = {
    "slug": "shadowai", "order": 30,
    "title": ("몰래 들여온 배달 상자", "The Takeout Box Nobody Signed For"),
    "h1": ("<em>섀도 AI</em>가 뭐예요?", "What is <em>Shadow AI</em>?"),
    "sub": ("섀도 AI를, 회사가 모르는 사이 직원이 뒷문으로 몰래 들여오는 배달 상자 이야기로 풀어봤어요.",
            "Shadow AI, told as a story about a delivery box an employee quietly brings in through the back door, without the company knowing."),
    "panels": [
        {"svg": P1, "alt": ("정식 도구 신청은 승인 대기 중이고, 직원은 기다리다가 뒷문으로 몰래 상자를 들여옴", "The official tool request is still pending, and a waiting employee instead brings a box in quietly through the back door"),
         "caption": ("승인을 기다리기 지겨워서, 뒷문으로 다른 걸 몰래 들여와요.", "Tired of waiting for approval, someone brings something else in through the back."),
         "small": ("정식 신청은 느리고, 뒷문은 바로 쓸 수 있어요.", "The official request is slow — the back door works right away.")},
        {"svg": P2, "alt": ("사장님이 처음 보는 상자를 보고 놀라는데, 그 상자는 장부에 전혀 적혀 있지 않음", "The manager is startled by a box they've never seen — one that isn't written in the logbook at all"),
         "caption": ("직원은 그냥 빨리 끝내고 싶었을 뿐이지만, 사장님은 이 상자를 아예 볼 수가 없어요.", "The employee just wanted to finish faster — the manager can't see this box at all."),
         "small": ("나쁜 마음이 아니라, 그냥 안 보여서 몰랐던 거예요.", "It's not malice — it's just invisible, so nobody knew.")},
        {"svg": P3, "hero": True, "alt": ("앞문은 신청·검수·기록을 거치는 정식 경로, 뒷문은 상자 하나가 모든 검사를 건너뛰고 직원에게 바로 들어가는 경로", "The front door goes through request, taster, and logbook; the back door lets a box skip every check and go straight to an employee"),
         "caption": ("섀도 AI = 회사가 모르는 사이 몰래 들여와 쓰는 바깥 도구예요.", "Shadow AI = an outside tool quietly brought in and used, without the company knowing."),
         "small": ("앞문은 겹겹이 검사하지만, 뒷문 상자는 아무도 몰라요.", "The front door checks layer by layer — nobody even knows about the back-door box."),
         "tricks": (4, [
             (NOBODY_I, ("아무도 모르게 들어와요", "Nobody signs it in"), ("승인 서류가 아예 없어요", "there's no approval paperwork at all"), "calm"),
             (SKIP_I, ("검사를 다 건너뛰어요", "Skips every checkpoint"), ("맛보기 검수대도 없이요", "no taster, no check")),
             (LEAK_I, ("회사 비밀도 같이 나가요", "Leaks data out the same door"), ("들어온 길로 그대로 샐 수 있어요", "it can leak right back out the way it came in"), "warm"),
             (RESP_I, ("그래도 사장님 책임이에요", "Still the manager's responsibility"), ("몰랐다고 책임이 없어지진 않아요", "not knowing doesn't erase the responsibility")),
         ])},
        {"svg": P4, "alt": ("앞문(정식 도구)과 뒷문(섀도 도구)을 승인·검수·기록·권한 네 줄로 나란히 비교한 규칙판 두 개", "Two rules boards comparing the front door (sanctioned tool) and back door (shadow tool) across approval, check, record, and access"),
         "caption": ("같은 일을 시켜도, 앞문과 뒷문은 완전히 다르게 다뤄져요.", "The same task is handled completely differently at the front door vs. the back."),
         "small": ("승인·검수·기록·권한, 네 가지가 전부 달라요.", "Approval, checking, record-keeping, and access — all four differ.")},
        {"svg": P5, "alt": ("왼쪽: 비밀 재료가 상자로 같이 빠져나가고 나서야 알아챔. 오른쪽: 규칙판엔 이미 금지라고 적혀 있지만, 앞문을 더 빠르게 만드는 게 진짜 해결책", "Left: a secret ingredient slips out through the box, discovered only afterward. Right: the rules board already bans it, but making the front door faster is the real fix"),
         "caption": ("터지고 나서야 알아요 — 금지만으론 못 막아요.", "You find out only after it breaks — a ban alone doesn't stop it."),
         "small": ("금지보다 '더 빠른 앞문'이 섀도 AI를 줄여요. 거버넌스 규칙판은 '정식으로 뭘 써야 하는지'를 적어두는 일이고, 섀도 AI는 바로 그 규칙판 밖에서 몰래 벌어지는 일이에요.",
                   "A faster front door shrinks shadow AI more than a ban does. AI governance is writing down what the sanctioned tools are — shadow AI is exactly what happens quietly outside that board.")},
    ],
    "summary": (("<b>섀도 AI</b> = 회사가 모르는 사이, 직원이 <b>뒷문으로 몰래 들여와 쓰는 바깥 AI 도구</b>. 승인·검수·기록 중 어느 것도 거치지 않아요.",
                 "<b>Shadow AI</b> = an outside AI tool an employee <b>quietly brings in through the back door</b>, without the company knowing — skipping approval, review, and record-keeping alike."),
                ("섀도 AI(Shadow AI)는 회사가 승인하거나 파악하지 못한 AI 도구를 직원들이 업무에 쓰는 것을 말해요. IT 부서의 정식 심사·가드레일·로깅을 거치지 않기 때문에, 데이터 유출·공급망 위험·정책 위반이 생겨도 알아채기까지 시간이 오래 걸려요. 금지 공고만으론 줄지 않고, 승인된 도구를 충분히 빠르고 쓰기 쉽게 만들어야 실제로 줄어들어요.",
                 "Shadow AI refers to employees using AI tools the company hasn't approved or even knows about. Because it bypasses IT's formal review, guardrails, and logging, data leaks, supply-chain risk, or policy violations can go undetected for a long time. A ban notice alone rarely reduces it — the sanctioned tool has to be fast and easy enough to use instead.")),
    "glossary": [
        ("섀도 AI", "Shadow AI", ("회사 몰래 들여와 쓰는 바깥 도구.", "An outside tool quietly brought in and used, without the company knowing."), ("뒷문으로 들어와서, 아무도 그 존재를 몰라요.", "It comes in through the back door — nobody even knows it exists.")),
        ("승인된 도구 목록", "Sanctioned tool list", ("앞문으로 들어온, 허락받은 도구들.", "Tools that came through the front door, with approval."), ('도구 하나하나를 허락받고 쓰는 일이에요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'Using each tool only with sign-off. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("데이터 유출", "Data leakage", ("비밀 재료가 상자에 같이 실려 나가는 일.", "A secret ingredient riding out in that same box."), ('뒷문 도구가 특히 위험한 지점이에요. → <a href="aiprivacy-ko.html">AI 프라이버시가 뭐예요?</a>', 'Especially risky with a back-door tool. → <a href="aiprivacy-en.html">What is AI Privacy?</a>')),
        ("공급망 위험", "Supply-chain risk", ("어디서 왔는지 모르는 상자를 들이는 위험.", "The risk of letting in a box you can't trace."), ('재료창고 전체의 일반 보안 개념이에요. → <a href="supplychain-ko.html">공급망 공격이 뭐예요?</a>', 'The general security concept behind the pantry. → <a href="supplychain-en.html">What is a Supply Chain Attack?</a>')),
        ("최소 권한", "Least privilege", ("칼서랍처럼, 필요한 만큼만 쓰게 하는 것.", "Like the knife drawer — only as much access as needed."), ('뒷문 상자엔 이 제한이 아예 없어요. → <a href="leastprivilege-ko.html">보안 마을의 열쇠 이야기</a>', 'The back-door box has none of this limit. → <a href="leastprivilege-en.html">the security world\'s key story</a>')),
        ("감사 기록", "Audit trail", ("누가 언제 무엇을 썼는지 적어두는 장부.", "The logbook that writes down who used what, and when."), ('이 장부가 바로 다음 페이지예요. → <a href="aiaudit-ko.html">주문 기록 장부</a>', 'That logbook is the next page. → <a href="aiaudit-en.html">the order logbook</a>')),
        ("정책 준수", "Compliance", ("회사가 정한 규칙을 실제로 지키는 일.", "Actually following the rules the company set."), ('뒷문이 많아지면 이것부터 깨져요. → <a href="compliance-ko.html">컴플라이언스가 뭐예요?</a>', 'More back doors, and this is the first thing to break. → <a href="compliance-en.html">What is Compliance?</a>')),
        ("거버넌스 규칙판", "AI governance", ("주방 벽에 걸린, 정식 규칙을 적은 판.", "The board on the wall with the official rules written down."), ('섀도 AI는 바로 이 규칙판 밖에서 몰래 벌어지는 일이에요. → <a href="aigovernance-ko.html">주방 규칙판</a>', 'Shadow AI is exactly what happens quietly outside that rules board. → <a href="aigovernance-en.html">The Kitchen Rules Board</a>')),
    ],
}
