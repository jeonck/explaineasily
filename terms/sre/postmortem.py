from _draw import *
from _world import *

# 1. 사고 후 범인 찾기부터 시작해요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(260, 260 - 112 * 0.65, s=0.65, face=FROWN, **MANAGER)
         + person(480, 260 - 112 * 0.6, s=0.6, face=SWEAT, **ROOKIE)
         + bubble(150, 100, 220, 46, "⟦누가 그 버튼 눌렀어요?!|who pressed that button?!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + bubble(460, 140, 200, 44, "⟦저... 그게...|uh... well...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦사고 후 범인 찾기부터 시작해요 — '누가 그 버튼 눌렀어?'|right after the incident, the hunt for who's at fault begins — 'who pressed that button?!'⟧", 12, "var(--ink)"))

# 2. 왜: 탓하면 숨기게 되고, 같은 사고가 또 나요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(160, 260 - 112 * 0.6, s=0.6, face=EYES, **ROOKIE)
         + bubble(60, 120, 220, 44, "⟦이번엔 그냥 숨겨야지|better just hide it this time⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + ride(560, 260, 0.9, color="var(--bad)", closed=True, label_text="⟦또 같은 사고|the same incident again⟧")
         + label(380, 282, "⟦탓하면 사람들이 실수를 숨기게 되고, 그럼 같은 사고가 또 나요|blame makes people hide mistakes — and the same incident happens again⟧", 12, "var(--ink)"))

# 3. hero: 탓하지 않고, 무슨 일이 있었는지만 모여서 적어요
P3 = svg(340, sky(340)
         + board(230, 60, 300, 170, "⟦사후 분석|POSTMORTEM⟧", ("⟦무슨 일이 있었나|what happened⟧", "⟦왜 못 막았나|why didn't we catch it⟧", "⟦어떻게 고칠까|how we'll fix it⟧"), 1.2)
         + person(120, 340 - 112 * 0.55, s=0.55, face=SMILE, **MECHANIC)
         + person(620, 340 - 112 * 0.55, s=0.55, face=SMILE, **OPERATOR)
         + label(380, 40, "⟦사고 끝나면 모두 모여서, 탓하지 않고 무슨 일이 있었는지 적어요|when it's over, everyone gathers and writes what happened — without blame⟧", 14, "var(--ink)", cls="d")
         + label(380, 300, "⟦범인이 아니라 사실과 고칠 점만 남겨요|not who's to blame — just the facts, and what to fix⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 시간순 + 근본 원인 + 할 일을 같이 적어요
P4 = svg(320, sky(320)
         + board(40, 40, 320, 190, "⟦기록|THE RECORD⟧", ("⟦시간순: 몇 시 몇 분에 뭐가|timeline: minute by minute⟧", "⟦근본 원인: 왜 못 막았나|root cause: why we missed it⟧", "⟦할 일: 다음엔 이렇게|action items: what changes next⟧"), 1.0)
         + person(500, 260 - 112 * 0.55, s=0.55, face=SMILE, extra=CLIPBOARD, **MECHANIC)
         + person(630, 260 - 112 * 0.5, s=0.5, face=SMILE, **OPERATOR)
         + '<path d="M360 170 L500 198" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + label(380, 300, "⟦시간순 기록 + 근본 원인 + 할 일 — 이 세 가지를 같이 적어요|timeline, root cause, and action items — all written down together⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 말로만 "탓 안 해"하면 소용없어요 — 문화가 돼야 해요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(140, 260 - 112 * 0.6, s=0.6, face=FROWN, **MANAGER)
         + bubble(40, 120, 230, 50, "⟦말로만 안 탓한다면서, 표정은 왜 그래요|you say no blame, but why that look⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(190, 282, "⟦말로만 하면 소용없어요|just saying it isn't enough⟧", 12, "var(--bad)", cls="d")
         + person(560, 260 - 112 * 0.6, s=0.6, face=SMILE, **MANAGER)
         + board(460, 70, 260, 110, "⟦우리 문화|OUR CULTURE⟧", ("⟦실수해도 괜찮아요|mistakes are okay⟧", "⟦사람 말고 시스템을 고쳐요|fix the system, not the person⟧"), 1.0)
         + label(590, 282, "⟦문화로 자리 잡아야 진짜예요|it has to actually become the culture⟧", 12, "var(--ink)"))

NOBLAME_I = icon('<path d="M14 46 L40 20" stroke="var(--stone-dark)" stroke-width="8" stroke-linecap="round"/><circle cx="44" cy="16" r="7" fill="var(--stone-dark)"/><path d="M8 8 L56 56 M56 8 L8 56" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')
TIMELINE_I = icon('<path d="M8 32 H56" stroke="var(--muted)" stroke-width="3"/><circle cx="16" cy="32" r="5" fill="var(--accent)"/><circle cx="32" cy="32" r="5" fill="var(--accent)"/><circle cx="48" cy="32" r="5" fill="var(--accent)"/>')
TODO_I = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="20" y="20" width="8" height="8" fill="var(--good)"/><path d="M34 24 h12" stroke="#142033" stroke-width="2.5"/><rect x="20" y="36" width="8" height="8" fill="none" stroke="var(--muted)" stroke-width="2.5"/><path d="M34 40 h12" stroke="#142033" stroke-width="2.5"/>')
SHARE_I = icon('<circle cx="16" cy="32" r="8" fill="var(--accent)"/><circle cx="48" cy="16" r="8" fill="var(--accent)"/><circle cx="48" cy="48" r="8" fill="var(--accent)"/><path d="M23 28 L41 18 M23 36 L41 46" stroke="var(--muted)" stroke-width="3"/>')

PAGE = {
    "slug": "postmortem", "order": 45,
    "title": ("탓하지 않고 모여 쓰는 기록", "The Record Everyone Writes Without Blame"),
    "h1": ("<em>포스트모템</em>이 뭐예요?", "What is a <em>Postmortem</em>?"),
    "sub": ("포스트모템(사후 분석)을, 범인을 찾는 대신 무슨 일이 있었는지만 적는 모임 이야기로 풀어봤어요.",
            "Postmortem, told as a story about a meeting that writes down what happened instead of hunting for who's to blame."),
    "panels": [
        {"svg": P1, "alt": ("공원장이 신참 정비사를 가리키며 누가 그 버튼을 눌렀냐고 화를 내고, 신참은 겁먹어 얼버무림", "The manager points at a rookie mechanic, demanding to know who pressed that button, while the rookie mumbles nervously"),
         "caption": ("사고 후 범인 찾기부터 시작해요.", "Right after the incident, the hunt for who's at fault begins."),
         "small": ("'누가 그 버튼 눌렀어?' 하고 다들 추궁부터 해요.", "Everyone jumps straight to 'who pressed that button?!'")},
        {"svg": P2, "alt": ("신참이 '이번엔 그냥 숨겨야지' 하고 속으로 다짐하고, 멀리서 똑같은 사고가 또 일어남", "A rookie quietly resolves to hide the next mistake, while the same incident happens again elsewhere"),
         "caption": ("탓하면 사람들이 실수를 숨기게 돼요.", "Blame makes people hide their mistakes."),
         "small": ("그럼 같은 사고가 또 나요.", "And then the same incident happens again.")},
        {"svg": P3, "hero": True, "alt": ("안내판에 '무슨 일이 있었나 / 왜 못 막았나 / 어떻게 고칠까'가 적히고, 정비사와 관제실 요원이 양쪽에서 웃으며 함께함", "A board reads 'what happened / why we missed it / how we'll fix it', with a mechanic and an operator smiling on either side"),
         "caption": ("탓하지 않고, 무슨 일이 있었는지만 적어요.", "Without blame — just writing down what happened."),
         "small": ("범인이 아니라 사실과 고칠 점만 남겨요.", "Not who's to blame — just the facts, and what to fix."),
         "tricks": (4, [
             (NOBLAME_I, ("사람 탓 대신 시스템 탓", "Blame the system, not the person"), ("'왜 경고가 없었나' 처럼요", "like 'why wasn't there a warning'"), "calm"),
             (TIMELINE_I, ("시간순으로 적어요", "Lay it out in order"), ("무슨 일이 언제 있었는지요", "what happened, and when")),
             (TODO_I, ("다음엔 뭘 바꿀지 할 일로", "Turn it into action items"), ("다음엔 뭘 바꿀지요", "what changes next"), "warm"),
             (SHARE_I, ("다른 팀도 볼 수 있게 공유", "Shared so other teams can read it"), ("같은 실수를 막아줘요", "stops the same mistake elsewhere")),
         ])},
        {"svg": P4, "alt": ("기록판에 시간순 타임라인, 근본 원인, 할 일 세 칸이 적혀 있고 사람들이 함께 둘러앉아 씀", "A record board lists a timeline, root cause, and action items in three sections, with people writing it together"),
         "caption": ("시간순 기록, 근본 원인, 할 일 — 이 세 가지를 같이 적어요.", "Timeline, root cause, and action items — all written down together."),
         "small": ("몇 시 몇 분에 무슨 일이 있었는지부터 시작해요.", "It starts with what happened, minute by minute.")},
        {"svg": P5, "alt": ("왼쪽: 공원장이 '탓 안 한다'면서도 표정이 안 좋음. 오른쪽: '실수해도 괜찮다'는 문화 안내판과 웃는 공원장", "Left: the manager says 'no blame' but still looks displeased. Right: a culture board says mistakes are okay, and the manager smiles"),
         "caption": ("말로만 '탓 안 해'하면 소용없어요.", "Just saying 'no blame' out loud isn't enough."),
         "small": ("실제로 문화로 자리 잡아야 해요.", "It has to actually become the culture.")},
    ],
    "summary": (("<b>포스트모템</b> = 사고가 끝나면 <b>사람 탓 없이</b>, 무슨 일이 있었고 <b>어떻게 고칠지</b>만 모여서 적는 일.",
                 "<b>Postmortem</b> = after an incident, gathering <b>without blaming anyone</b> to write down what happened and <b>how it'll be fixed</b>."),
                ("Postmortem. 블레임리스(무탓) 문화 아래, 사고의 타임라인·근본 원인·액션 아이템을 적고 공유하는 문서예요. 사람의 실수를 탓하는 대신 '왜 시스템이 그걸 막지 못했는지'를 물어서, 같은 사고가 반복되지 않게 해요.",
                 "A document written under a blameless culture, recording an incident's timeline, root cause, and action items, then sharing it. Instead of blaming a person's mistake, it asks why the system failed to catch it — so the same incident doesn't repeat.")),
    "glossary": [
        ("포스트모템", "Postmortem", ("탓하지 않고 쓰는 사후 분석 기록.", "The blameless record written after an incident."), ("무슨 일이 있었는지만 남겨요.", "It only keeps what actually happened.")),
        ("블레임리스 문화", "Blameless culture", ("사람 말고 시스템을 고치는 태도.", "An attitude of fixing the system, not the person."), ("말이 아니라 실제 문화여야 해요.", "It has to be a real culture, not just words.")),
        ("타임라인 재구성", "Timeline reconstruction", ("몇 시 몇 분에 뭐가 있었는지 순서대로.", "What happened, minute by minute, in order."), ("기록의 첫 줄이에요.", "It's the first thing written down.")),
        ("근본 원인", "Root cause", ("왜 못 막았는지에 대한 답.", "The answer to why it wasn't caught."), ("증상이 아니라 원인을 찾아요.", "It looks for the cause, not just the symptom.")),
        ("액션 아이템", "Action items", ("다음엔 뭘 바꿀지 남긴 할 일.", "The to-dos for what changes next."), ("누가, 언제까지 할지도 적어요.", "It also says who does it, and by when.")),
        ("공유 문서화", "Shared documentation", ("다른 팀도 볼 수 있게 남기는 것.", "Writing it so other teams can read it too."), ("같은 사고를 다른 팀도 피할 수 있어요.", "It helps other teams avoid the same incident.")),
        ("인시던트 커맨더", "Incident commander", ("사고 중 지휘봉을 들었던 사람.", "The one who held the baton during the incident."), ('사후 분석이 제대로 열리게 챙겨요. → <a href="incidentcommand-ko.html">지휘봉을 든 사람</a>', 'Makes sure the postmortem actually happens. → <a href="incidentcommand-en.html">the one holding the baton</a>')),
        ("플레이북 개선", "Playbook improvement", ("여기서 배운 걸 공책에 추가하는 것.", "Adding what was learned here into the notebook."), ('다음에 더 빨리 고치게 돼요. → <a href="runbook-ko.html">정비사의 공책</a>', 'It means fixing it faster next time. → <a href="runbook-en.html">the mechanic\'s notebook</a>')),
    ],
}
