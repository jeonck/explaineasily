from _draw import *
from _world import *


def stamp(x, y, s=1.0, mark="⟦✓|✓⟧", color="var(--good)"):
    """도장. 손잡이 + 바닥 + 찍힌 자국."""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="-34" width="12" height="20" rx="4" fill="#5A3B22"/>'
            f'<rect x="-18" y="-14" width="36" height="12" rx="3" fill="#8B5E3C"/><circle cy="14" r="12" fill="none" stroke="{color}" stroke-width="3"/>'
            + label(0, 19, mark, 14, color, cls="d") + "</g>")


def arrow(x1, y1, x2, y2, color="var(--muted)", dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3"{d}/>'
            f'<path d="M{x2 - 10} {y2 - 7} L{x2} {y2} L{x2 - 10} {y2 + 7}" stroke="{color}" stroke-width="3" fill="none"/>')


def pill(x, y, w, text, fill, color):
    return f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{fill}"/>' + label(x + w / 2, y + 18, text, 11, color, cls="d")


# 1. 앵무새가 환불 이메일을 손님에게 바로 보냈어요 — 금액이 틀려요
P1 = svg(300, sky(300)
         + perch(150, 200, 140) + parrot(150, 160, 1.1, talk=True) + label(150, 262, "⟦혼자 바로 보냈어요|sent it all by itself⟧", 12, "var(--bad)")
         + note(290, 60, 190, 110, "⟦환불 이메일|REFUND EMAIL⟧", ("⟦손님께, 환불로|Dear guest, refunding⟧", "⟦500,000원 보내요|500,000 won⟧", "⟦(진짜는 50,000원)|(should be 50,000)⟧"), 1.0, 1)
         + arrow(490, 115, 540, 115)
         + person(560, 90, s=0.9, face=SMILE, **GUEST) + label(587, 225, "⟦손님이 벌써 받았어요|the guest already has it⟧", 11, "var(--muted)")
         + label(380, 282, "⟦앵무새 답이 확인 없이 바로 나갔어요 — 0이 하나 더 붙었어요|the parrot\'s answer went straight out, unchecked — with one extra zero⟧", 12, "var(--ink)"))

# 2. 왜: 앵무새 답은 초안인데, 확인 없이 밖으로 나가면 실수가 곧 사고예요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(50, 50, 180, 120, "⟦초안|DRAFT⟧", ("⟦500,000원|500,000 won⟧", "⟦손님 이름 틀림|wrong guest name⟧", "⟦존댓말 빠짐|not polite⟧"), 1.0)
         + label(140, 200, "⟦앵무새 답은 초안이에요|the parrot\'s answer is a draft⟧", 11, "var(--ink)")
         + arrow(240, 110, 330, 110, "var(--bad)") + label(285, 95, "⟦확인 없이|unchecked⟧", 10, "var(--bad)")
         + person(360, 60, s=0.8, face=FROWN, **GUEST) + label(387, 175, "⟦손님|guest⟧", 11, "var(--muted)")
         + note(500, 50, 220, 120, "⟦실수 → 사고|MISTAKE → ACCIDENT⟧", ("⟦돈이 벌써 나갔어요|the money already left⟧", "⟦되돌리기 어려워요|hard to take back⟧", "⟦앵무새는 몰라요|the parrot has no idea⟧"), 1.0, 1)
         + label(380, 240, "⟦쪽지대로 이어 붙인 초안이 곧바로 세상으로 나가요|a draft stitched from the note goes straight into the world⟧", 12, "var(--ink)")
         + label(380, 282, "⟦확인 없이 밖으로 나가면, 실수가 곧 사고예요|out the door unchecked, a mistake becomes an accident⟧", 12, "var(--bad)"))

# 3. human-in-the-loop = 앵무새가 준비하고, 사람이 보고 도장 찍은 뒤에 나가요 (hero)
P3 = svg(360, sky(360)
         + pill(290, 34, 90, "⟦도장 ✓|stamp ✓⟧", "var(--good-soft)", "var(--good)") + pill(390, 34, 90, "⟦고쳐요|fix it⟧", "var(--accent-soft)", "var(--accent)") + pill(490, 34, 90, "⟦반려 ×|reject ×⟧", "var(--bad-soft)", "var(--bad)")
         + perch(110, 240, 120) + parrot(110, 200, 1.2) + label(110, 300, "⟦앵무새가 준비|the parrot prepares⟧", 11, "var(--muted)")
         + arrow(160, 170, 196, 170) + note(200, 120, 130, 80, "⟦초안|DRAFT⟧", ("⟦환불 50,000원|refund 50,000⟧",), 1.0)
         + person(370, 110, s=1.0, face=SMILE, **TRAINER) + stamp(450, 150, 1.0) + label(410, 250, "⟦사람이 보고 도장|a person looks and stamps⟧", 11, "var(--muted)")
         + arrow(470, 170, 536, 170) + note(540, 120, 120, 80, "⟦발송|SENT⟧", ("⟦확인된 것만|checked only⟧",), 1.0)
         + person(675, 120, s=0.7, face=SMILE, **GUEST) + label(700, 220, "⟦손님|guest⟧", 11, "var(--muted)")
         + '<path d="M390 235 Q260 300 160 262" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 5" fill="none"/><path d="M172 256 L158 262 L170 270" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(300, 300, "⟦반려된 건 앵무새에게 다시|rejected ones go back to the parrot⟧", 10, "var(--bad)")
         + label(380, 340, "⟦앵무새가 준비하고, 사람이 보고 도장을 찍은 뒤에야 밖으로 나가요|the parrot prepares, a person looks and stamps, and only then does it go out⟧", 12, "var(--ink)", cls="d"))

# 4. 세 단계: 초안 → 검토(도장 / 수정 / 반려) → 발송, 반려는 앵무새에게 다시
P4 = svg(320, sky(320)
         + label(130, 50, "⟦1. 앵무새 초안|1. parrot drafts⟧", 12, "var(--ink)", cls="d") + label(380, 50, "⟦2. 사람 검토|2. a person reviews⟧", 12, "var(--ink)", cls="d") + label(630, 50, "⟦3. 발송|3. send⟧", 12, "var(--ink)", cls="d")
         + '<rect x="40" y="60" width="180" height="140" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="270" y="60" width="220" height="140" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + '<rect x="540" y="60" width="180" height="140" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + parrot(85, 135, 0.8) + note(125, 95, 80, 60, "⟦초안|DRAFT⟧", ("⟦50,000원|50,000⟧",), 0.9)
         + arrow(224, 130, 266, 130)
         + person(285, 85, s=0.75, face=EYES, **TRAINER)
         + pill(360, 76, 115, "⟦도장 ✓ 보내요|stamp ✓ send⟧", "var(--good-soft)", "var(--good)") + pill(360, 116, 115, "⟦고쳐서 ✓ 보내요|fix ✓ send⟧", "var(--accent-soft)", "var(--accent)") + pill(360, 156, 115, "⟦반려 × 다시|reject × redo⟧", "var(--bad-soft)", "var(--bad)")
         + arrow(494, 130, 536, 130)
         + note(560, 95, 90, 60, "⟦발송|SENT⟧", ("⟦✓|✓⟧",), 0.9) + person(660, 90, s=0.7, face=SMILE, **GUEST)
         + '<path d="M380 200 v24 h-250 v-22" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 5" fill="none"/><path d="M123 210 L130 200 L137 210" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(255, 244, "⟦반려 → 앵무새가 다시 초안|rejected → the parrot drafts again⟧", 10, "var(--bad)")
         + label(380, 272, "⟦자신 없을 땐 앵무새가 먼저 물어요 — 이건 사람이 봐 주세요|when unsure, the parrot asks first — please check this one⟧", 11, "var(--ink)")
         + label(380, 300, "⟦되돌리기 어려운 일일수록 도장이 중요해요 — 보내기, 결제, 삭제|the harder it is to undo, the more the stamp matters — sending, paying, deleting⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 도장만 찍는 습관 = 자동 승인, 울타리가 아니에요
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
         + person(50, 100, s=0.9, face=EYES, extra=SWEAT, **TRAINER)
         + bubble(40, 30, 250, 34, "⟦안 읽고 도장, 도장, 도장|stamp, stamp, stamp — unread⟧", 11, "var(--panel)", "var(--bad)", "left")
         + "".join(note(180 + i * 22, 110 + i * 14, 110, 60, "⟦초안|DRAFT⟧", ("⟦✓|✓⟧",), 0.85) for i in range(3))
         + label(190, 240, "⟦도장만 찍으면 울타리가 아니에요|a stamp without a look is no fence⟧", 12, "var(--bad)", cls="d")
         + label(190, 262, "⟦= 자동 승인|= auto-approval⟧", 11, "var(--muted)")
         + label(450, 74, "⟦위험 낮음|low risk⟧", 11, "var(--ink)") + arrow(500, 70, 530, 70) + parrot(565, 80, 0.6) + arrow(600, 70, 630, 70) + label(680, 74, "⟦바로 나가요|goes right out⟧", 11, "var(--good)")
         + label(450, 174, "⟦위험 높음|high risk⟧", 11, "var(--ink)") + arrow(500, 170, 530, 170) + person(545, 130, s=0.7, face=EYES, **TRAINER) + stamp(612, 160, 0.8) + arrow(630, 170, 660, 170) + label(700, 174, "⟦도장 뒤에|after the stamp⟧", 11, "var(--good)")
         + label(570, 240, "⟦사람이 다 보면 느려요 — 위험한 것만|a person on everything is slow — only the risky ones⟧", 11, "var(--ink)")
         + label(380, 300, "⟦도장은 보고 찍어야 울타리예요 — 그리고 위험한 것만 사람에게|a stamp is a fence only when you look first — and only the risky ones go to a person⟧", 12, "var(--ink)", cls="d"))

STAMP_I = icon('<rect x="26" y="6" width="12" height="18" rx="4" fill="#5A3B22"/><rect x="14" y="24" width="36" height="10" rx="3" fill="#8B5E3C"/><circle cx="32" cy="48" r="10" fill="none" stroke="var(--good)" stroke-width="3"/><path d="M27 48 l4 4 l7 -8" stroke="var(--good)" stroke-width="3" fill="none"/>')
ASK_I = icon(f'<circle cx="24" cy="38" r="12" fill="{PARROT}"/><circle cx="24" cy="20" r="9" fill="{PARROT}"/><path d="M31 17 l10 3 l-10 4z" fill="#E9B44C"/><text x="50" y="30" text-anchor="middle" font-size="24" font-weight="700" fill="var(--accent)">?</text>')
COLLECT_I = icon('<rect x="10" y="14" width="28" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="18" y="8" width="28" height="36" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M26 20 h12 M26 28 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/><path d="M50 40 v14 M44 48 l6 6 l6 -6" stroke="var(--accent)" stroke-width="3" fill="none" stroke-linecap="round"/>')
FUNNEL_I = icon('<path d="M8 10 h48 l-18 22 v20 l-12 6 v-26z" fill="var(--stone)" stroke="var(--stone-dark)" stroke-width="3"/><text x="32" y="26" text-anchor="middle" font-size="16" font-weight="700" fill="var(--bad)">!</text>')

PAGE = {
    "slug": "humanloop", "order": 22,
    "title": ("마지막은 사람이", "A Person at the End"),
    "h1": ("<em>휴먼 인 더 루프</em>가 뭐예요?", "What is <em>Human-in-the-Loop</em>?"),
    "sub": ("human-in-the-loop 를, 앵무새가 준비한 것을 사람이 보고 도장을 찍은 뒤에야 밖으로 내보내는 이야기로 풀어봤어요.",
            "Human-in-the-loop, told as a story where the parrot prepares, a person looks and stamps, and only then does anything go out."),
    "panels": [
        {"svg": P1, "alt": ("앵무새가 환불 이메일을 혼자 보냄. 이메일엔 500,000원(진짜는 50,000원). 손님이 벌써 웃으며 받음", "The parrot sends a refund email by itself; it says 500,000 won (should be 50,000). The guest, smiling, already has it"),
         "caption": ("앵무새가 환불 이메일을 손님에게 바로 보냈어요. 금액이 틀렸어요.", "The parrot sent a refund email straight to the guest. The amount is wrong."),
         "small": ("0이 하나 더 붙었어요. 손님은 벌써 받았고, 앵무새는 자기가 틀린 줄 몰라요.", "One extra zero. The guest already has it, and the parrot has no idea it was wrong.")},
        {"svg": P2, "alt": ("초안 쪽지(500,000원, 손님 이름 틀림, 존댓말 빠짐)가 확인 없이 화살표를 따라 찡그린 손님에게. 옆엔 실수 → 사고 쪽지: 돈이 벌써 나갔어요, 되돌리기 어려워요", "A draft note (500,000 won, wrong guest name, not polite) follows an unchecked arrow to a frowning guest; a note reads mistake → accident: the money already left, hard to take back"),
         "caption": ("앵무새 답은 초안이에요. 확인 없이 밖으로 나가면 실수가 곧 사고예요.", "The parrot\'s answer is a draft. Out the door unchecked, a mistake becomes an accident."),
         "small": ('<a href="llm-ko.html">앵무새 답은 초안</a>이라고 했죠. 초안이 집 안에 있으면 고치면 되지만, 밖으로 나간 초안은 되돌리기 어려워요.',
                   'Remember, <a href="llm-en.html">a parrot\'s answer is a draft</a>. A draft inside the house can be fixed; a draft that went out the door is hard to take back.')},
        {"svg": P3, "hero": True, "alt": ("앵무새가 초안(환불 50,000원)을 준비 → 조련사가 도장을 들고 봄(도장 ✓ / 고쳐요 / 반려 ×) → 발송 쪽지 → 손님. 반려된 건 빨간 점선으로 앵무새에게 되돌아감", "The parrot prepares a draft (refund 50,000) → a trainer with a stamp looks (stamp ✓ / fix it / reject ×) → a sent note → the guest. A red dashed line returns rejected ones to the parrot"),
         "caption": ("앵무새가 준비하고, 사람이 보고 도장을 찍은 뒤에야 밖으로 나가요.", "The parrot prepares, a person looks and stamps, and only then does it go out."),
         "small": ("사람은 도장을 찍거나, 고치거나, 반려해요. 반려된 건 앵무새에게 돌아가요. 앵무새는 그대로 빠르고, 나가는 건 사람이 본 것뿐이에요.", "The person stamps, fixes, or rejects. Rejected ones go back to the parrot. The parrot stays fast; only what a person saw goes out."),
         "tricks": (4, [
             (STAMP_I, ("되돌리기 어려운 일엔 도장", "Stamp what is hard to undo"), ("보내기 · 결제 · 삭제", "sending, paying, deleting"), "calm"),
             (ASK_I, ("자신 없을 땐 앵무새가 먼저 물어요", "Unsure? The parrot asks first"), ("이건 사람이 봐 주세요", "please check this one"), "calm"),
             (COLLECT_I, ("사람이 고친 건 모아요", "Keep what people fixed"), ("다음 특훈의 예시가 돼요", "examples for the next drill"), "warm"),
             (FUNNEL_I, ("위험한 것만 사람에게", "Only the risky ones"), ("다 보면 느려요", "looking at everything is slow"), "warm"),
         ])},
        {"svg": P4, "alt": ("세 상자: 1. 앵무새 초안(50,000원) → 2. 사람 검토(도장 ✓ 보내요 / 고쳐서 ✓ 보내요 / 반려 × 다시) → 3. 발송 ✓ 손님. 반려는 빨간 점선으로 1번으로 돌아감", "Three boxes: 1. parrot drafts (50,000) → 2. a person reviews (stamp ✓ send / fix ✓ send / reject × redo) → 3. sent ✓ to the guest. A red dashed line takes rejects back to box 1"),
         "caption": ("초안 → 검토(도장 · 수정 · 반려) → 발송. 반려는 앵무새에게 다시.", "Draft → review (stamp · fix · reject) → send. Rejects go back to the parrot."),
         "small": ('자신 없을 땐 앵무새가 먼저 "이건 사람이 봐 주세요" 하고 물어요. 사람이 고친 건 모아 두면 다음 <a href="finetune-ko.html">특훈</a>의 예시가 돼요.',
                   'When unsure, the parrot asks first: please check this one. What people fix gets collected — it becomes the examples for the next <a href="finetune-en.html">drill</a>.')},
        {"svg": P5, "alt": ("왼쪽 빨강: 땀 흘리는 조련사가 안 읽고 초안마다 도장, 도장, 도장. 오른쪽 초록: 위험 낮은 건 앵무새가 바로 내보내고, 위험 높은 건 사람이 도장을 찍은 뒤에", "Left, red: a sweating trainer stamps draft after draft unread. Right, green: low-risk ones go right out from the parrot; high-risk ones go after a person stamps"),
         "caption": ("도장은 보고 찍어야 울타리예요. 사람이 도장만 찍는 습관이 들면 자동 승인이에요.", "A stamp is a fence only when you look first. A person who just stamps is auto-approval."),
         "small": ('그래서 위험한 것만 사람에게 보내요 — 사람이 다 보면 느리고, 느리면 안 보게 돼요. 사람 앞의 자동 검사는 <a href="guardrail-ko.html">울타리</a>에서, 심부름을 스스로 짜는 앵무새에게 어디에 도장을 둘지는 <a href="agent-ko.html">에이전트</a>에서.',
                   'So only the risky ones go to a person — a person on everything is slow, and slow turns into not looking. The automatic checks before the person are in <a href="guardrail-en.html">the fence</a>; where to put the stamp for a parrot that plans its own errands is in <a href="agent-en.html">the agent</a>.')},
    ],
    "summary": (("<b>휴먼 인 더 루프</b> = 앵무새가 <b>준비</b>하고, 사람이 <b>보고 도장</b>을 찍은 뒤에야 밖으로 나가는 것. 되돌리기 어려운 일(보내기·결제·삭제)에 두고, 자신 없으면 앵무새가 먼저 묻고, <b>위험한 것만</b> 사람에게 — 도장만 찍는 습관은 울타리가 아니에요.",
                 "<b>Human-in-the-loop</b> = the parrot <b>prepares</b>, a person <b>looks and stamps</b>, and only then does it go out. Put it on what is hard to undo (sending, paying, deleting), let the parrot ask when unsure, and send <b>only the risky ones</b> to a person — a stamp without a look is no fence."),
                ("Human-in-the-loop (HITL). 모델 출력이 실행되기 전에 사람이 승인·수정·반려하는 단계를 워크플로에 넣는 설계예요. 되돌리기 어려운 행동(발송·결제·삭제)에 승인 단계를 두고, 신뢰도 임계값 아래면 에스컬레이션하며, 승인·수정 기록은 감사 로그와 파인튜닝 데이터가 돼요. 자동화 수준을 위험에 따라 나누고, 승인이 형식적(rubber-stamp)이 되지 않도록 검토 부담을 줄이는 게 핵심이에요.",
                 "A workflow design where a person approves, edits, or rejects model output before it takes effect. Put an approval step on hard-to-undo actions (sending, paying, deleting), escalate when confidence falls below a threshold, and keep approvals and edits as an audit log and fine-tuning data. Tier the level of automation by risk, and keep review load low enough that approval never becomes rubber-stamping.")),
    "glossary": [
        ("휴먼 인 더 루프", "Human-in-the-loop", ("마지막은 사람이.", "A person at the end."), ("앵무새가 준비하고, 사람이 보고 도장 찍은 뒤에 나가요.", "The parrot prepares, a person looks and stamps, then it goes out.")),
        ("승인 단계", "Approval step", ("도장 찍는 자리.", "Where the stamp goes."), ("보내기·결제·삭제 앞에 둬요. 되돌리기 어려울수록 꼭.", "Before sending, paying, deleting. The harder to undo, the more it matters.")),
        ("신뢰도 임계값", "Confidence threshold", ("앵무새가 먼저 묻는 선.", "The line where the parrot asks first."), ("자신이 이만큼 없으면 사람에게 — 이건 봐 주세요.", "Below this much confidence, it goes to a person: please check this one.")),
        ("에스컬레이션", "Escalation", ("사람에게 올리기.", "Handing it up to a person."), ("앵무새가 못 정하는 건 사람에게, 사람이 못 정하는 건 윗사람에게.", "What the parrot cannot decide goes to a person; what they cannot, to someone above.")),
        ("감사 로그", "Audit log", ("누가 언제 도장 찍었는지 적은 공책.", "The notebook of who stamped what, when."), ('사고가 나면 여기서 되짚어요. → <a href="log-ko.html">보안 마을의 일지</a>', 'When something goes wrong, you trace it back here. → <a href="log-en.html">the security world\'s logbook</a>')),
        ("자동화 수준", "Level of automation", ("어디까지 앵무새 혼자.", "How much the parrot does alone."), ("인사 이메일은 혼자, 환불은 도장 뒤에, 삭제는 사람이 직접.", "Greetings alone, refunds after a stamp, deletions by a person.")),
        ("가드레일", "Guardrail", ("사람 앞의 자동 울타리.", "The automatic fence before the person."), ('기계가 먼저 거르고, 남은 걸 사람이 봐요. → <a href="guardrail-ko.html">울타리</a>', 'A machine filters first; a person looks at what is left. → <a href="guardrail-en.html">the fence</a>')),
        ("에이전트", "Agent", ("심부름을 스스로 짜는 앵무새.", "The parrot that plans its own errands."), ('심부름 중간중간 어디에 도장을 둘지 정해요. → <a href="agent-ko.html">에이전트</a>', 'Decide where along the errand the stamps go. → <a href="agent-en.html">the agent</a>')),
    ],
}
