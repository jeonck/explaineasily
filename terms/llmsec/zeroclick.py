from _draw import *
from _world import *


def notice_board(x, y, s=1.0, bad=True):
    """가게 앞 리뷰판/게시판. 작은 빨간 쪽지가 한 귀퉁이에 꽂혀 있음(bad=True)."""
    out = (f'<g transform="translate({x},{y}) scale({s})"><rect width="130" height="90" rx="4" fill="#5A3B22"/>'
           f'<rect x="8" y="8" width="114" height="74" rx="2" fill="#FFF8E7"/>'
           f'<path d="M18 26 h60 M18 40 h90 M18 54 h70" stroke="#C9A86A" stroke-width="4"/>')
    if bad:
        out += '<rect x="86" y="54" width="34" height="22" rx="2" fill="var(--bad)" transform="rotate(6 103 65)"/>'
    return out + '</g>'


def zero_icon(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle r="22" fill="none" stroke="var(--bad)" stroke-width="5"/>'
            f'<path d="M-14 14 L14 -14" stroke="var(--bad)" stroke-width="5"/></g>')


# 1. 손님은 가만히 앉아 있어요 — 그런데 견습생은 벌써 행동해요
P1 = svg(310, sky(310)
         + person(100, 160, s=0.8, face=SMILE, **GUEST)
         + '<rect x="70" y="248" width="60" height="8" rx="4" fill="var(--muted)"/>'
         + label(100, 278, "⟦손님은 아무것도 안 눌렀어요|the guest hasn't touched anything⟧", 11, "var(--muted)")
         + notice_board(300, 140, 1.0)
         + label(365, 258, "⟦게시판에 몰래 꽂힌 쪽지|a note slipped onto the board⟧", 11, "var(--bad)")
         + person(560, 160, s=0.8, face=EYES, **RUNNER)
         + '<path d="M420 170 L535 170" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4"/><path d="M525 164 L535 170 L525 176" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + label(560, 258, "⟦견습생이 혼자 읽고 바로 움직여요|the apprentice reads it alone and moves right away⟧", 11, "var(--ink)"))

# 2. 왜 어려운가: 견습생의 루틴 자체가 사람 없이 도는 거예요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(130, 140, s=0.8, face=EYES, **RUNNER)
         + bubble(260, 50, 280, 70, "⟦매일 아침 게시판을 혼자 돌며 확인하는 게 제 일이에요 — 손님이 시킬 필요가 없어요|checking the board every morning, alone, is just my job — the guest never has to ask⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(650, 190, s=0.65, face=SMILE, **GUEST) + label(650, 178, "⟦그래서 손님은 지금 몰라요|so the guest has no idea, right now⟧", 11, "var(--muted)")
         + label(380, 280, "⟦자동으로 도는 루틴이라, 아무 데나 쪽지를 심어 두고 기다리기만 하면 돼요|because the routine runs itself, an attacker only has to plant a note somewhere and wait⟧", 12, "var(--ink)"))

# 3. 가만히 있어도 실행되는 공격 (hero)
P3 = svg(340, sky(340)
         + person(90, 170, s=0.8, face=SMILE, **GUEST)
         + zero_icon(90, 95, 0.6) + label(90, 250, "⟦클릭 0번|zero clicks⟧", 12, "var(--bad)", cls="d")
         + notice_board(260, 150, 1.0)
         + '<path d="M400 175 L520 175" stroke="var(--bad)" stroke-width="4"/><path d="M508 167 L520 175 L508 183" stroke="var(--bad)" stroke-width="4" fill="none"/>'
         + person(590, 170, s=0.8, face=EYES, **RUNNER)
         + '<rect x="660" y="190" width="36" height="28" rx="3" fill="#8B5E3C"/><rect x="664" y="194" width="28" height="20" rx="2" fill="#2E3D57"/>'
         + label(678, 240, "⟦계산대가 저절로 열려요|the register opens on its own⟧", 11, "var(--bad)")
         + label(380, 30, "⟦가만히 있어도 실행되는 공격 = 아무도 누르지 않았는데 심부름꾼이 혼자 읽고 혼자 실행해요|Zero-click Attack = no one pressed anything — the apprentice reads it alone, and acts alone⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦손님의 손가락이 한 번도 움직이지 않았는데 사고가 끝까지 나요|the whole thing happens without the guest's finger ever moving⟧", 11, "var(--muted)"))

# 4. 타임라인: 쪽지를 심는 순간부터 사고까지, 손님은 끝까지 등장하지 않아요
P4 = svg(330, sky(330)
         + board(40, 30, 680, 260, "⟦시간 순서|TIMELINE⟧",
                 ("⟦① 공격자가 게시판·메일·공유문서 어딘가에 쪽지를 심어요|① an attacker plants a note on a board, in mail, in a shared doc⟧",
                  "⟦② 견습생이 평소 루틴대로 그걸 자동으로 읽어요|② the apprentice reads it automatically, as part of its routine⟧",
                  "⟦③ 아무도 누르지 않았는데 쪽지 지시대로 바로 움직여요|③ nothing was clicked, yet it moves exactly as the note says⟧",
                  "⟦④ 손님은 그 사이 등장하지 않아요 — 끝나고야 알아요|④ the guest never appears in between — they find out only after⟧"), 1.0, hl=2)
         + label(380, 305, "⟦①~④ 모든 칸에 '손님의 클릭'이 없어요|not one of these four steps has a guest's click in it⟧", 12, "var(--bad)"))

# 5. 한계·이웃 용어와의 차이
P5 = svg(310, '<rect width="380" height="310" fill="var(--accent-soft)"/><rect x="380" width="380" height="310" fill="var(--bad-soft)"/>'
         + notice_board(90, 170, 0.85) + label(155, 290, "⟦쪽지 자체 — 숨긴 명령|the note itself — the hidden command⟧", 11, "var(--ink)", cls="d")
         + label(155, 20, "⟦간접 인젝션|Indirect Injection⟧", 12, "var(--ink)", cls="d")
         + person(590, 160, s=0.75, face=EYES, **RUNNER)
         + zero_icon(650, 100, 0.55)
         + label(590, 290, "⟦사람 없이 자동으로 실행되는 결과|the result — it runs automatically, no human needed⟧", 11, "var(--bad)")
         + label(590, 20, "⟦제로클릭|Zero-click⟧", 12, "var(--bad)", cls="d")
         + label(380, 265, "⟦숨긴 쪽지는 눌러야 발동할 수도 있어요 — 이건 누르지 않아도 발동한다는 뜻이에요|a hidden note could still need a click — this one fires even without one⟧", 11, "var(--ink)"))

AUTO_I = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 16 v16 l12 8" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
NOCLICK_I = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--bad)" stroke-width="5"/><path d="M20 20 L44 44" stroke="var(--bad)" stroke-width="5"/>')
ROUTE_I = icon('<rect x="8" y="26" width="48" height="12" rx="4" fill="var(--good)"/><circle cx="14" cy="32" r="6" fill="var(--good)"/><circle cx="50" cy="32" r="6" fill="var(--good)"/>')
HUMAN_I = icon(f'<circle cx="32" cy="18" r="10" fill="{SKIN}"/><rect x="18" y="30" width="28" height="24" rx="6" fill="var(--good)"/>')

PAGE = {
    "slug": "zeroclick", "order": 19,
    "title": ("가만히 있어도 실행되는 공격", "The Attack That Fires Without a Click"),
    "h1": ("<em>제로클릭 공격</em>이 뭐예요?", "What is a <em>Zero-click Attack</em>?"),
    "sub": ("제로클릭 공격을, 손님이 아무것도 누르지 않았는데도 견습생이 평소 루틴대로 쪽지를 읽고 혼자 실행해버리는 이야기로 풀어봤어요.",
            "A zero-click attack, told as a story about an apprentice who reads a planted note during its normal routine and acts on it alone — without the guest ever clicking anything."),
    "panels": [
        {"svg": P1, "alt": ("손님이 가만히 앉아 손도 움직이지 않는데, 게시판에 몰래 꽂힌 쪽지를 견습생이 읽고 바로 움직임", "The guest sits still, not moving a hand, while the apprentice reads a note slipped onto the board and moves right away"),
         "caption": ("손님은 아무것도 안 눌렀어요 — 그런데 견습생은 벌써 움직여요.", "The guest hasn't touched anything — yet the apprentice is already moving."),
         "small": ("게시판에 몰래 꽂힌 쪽지를 견습생이 혼자 읽고, 혼자 실행했어요.", "The apprentice read the note slipped onto the board, all on its own, and acted on it, all on its own.")},
        {"svg": P2, "alt": ("견습생이 매일 아침 게시판을 혼자 확인하는 게 자기 일이라고 말함. 손님은 그 사이 전혀 모름", "The apprentice explains that checking the board every morning, alone, is simply its job; the guest has no idea in the meantime"),
         "caption": ("견습생의 루틴 자체가 사람 없이 도는 거예요.", "The apprentice's routine runs itself, with no person required."),
         "small": ("자동으로 도는 루틴이라, 공격자는 아무 데나 쪽지를 심어 두고 기다리기만 하면 돼요.", "Because the routine runs on its own, an attacker just has to plant a note somewhere and wait.")},
        {"svg": P3, "hero": True, "alt": ("손님이 클릭 0번인 채로 가만히 있고, 게시판 쪽지를 읽은 견습생이 계산대를 저절로 열어버림", "The guest stays still at zero clicks while the apprentice, after reading the note on the board, opens the register on its own"),
         "caption": ("아무도 누르지 않았는데 심부름꾼이 혼자 읽고 혼자 실행해요.", "No one pressed anything — the apprentice reads it alone, and acts alone."),
         "small": ("손님의 손가락이 한 번도 움직이지 않았는데 사고가 끝까지 일어나요.", "The whole thing plays out to the end without the guest's finger ever moving."),
         "tricks": (4, [
             (AUTO_I, ("루틴이 자동으로 읽어요", "The routine reads automatically"), ("시킬 필요도 없이요", "no one has to ask it to")),
             (NOCLICK_I, ("클릭도, 열기도 없어요", "No click, no opening it"), ("보기만 해도 발동해요", "just being seen is enough"), "warm"),
             (ROUTE_I, ("아무 경로에나 심을 수 있어요", "It can be planted on any path"), ("게시판·메일·공유문서 다요", "a board, mail, a shared doc"), "warm"),
             (HUMAN_I, ("끝나고야 사람이 알아요", "A person finds out only after"), ("미리 막을 틈이 없어요", "there's no moment to stop it first")),
         ])},
        {"svg": P4, "alt": ("시간 순서판: 쪽지 심기, 자동으로 읽기, 클릭 없이 실행, 손님은 끝나고야 아는 네 단계. 가운데 두 단계가 강조됨", "A timeline board: planting the note, reading it automatically, acting with no click, and the guest finding out only afterward — the middle two steps highlighted"),
         "caption": ("①~④ 모든 칸에 손님의 클릭이 없어요.", "Not one of these four steps has a guest's click in it."),
         "small": ("쪽지를 심는 순간부터 사고가 끝날 때까지, 손님은 한 번도 등장하지 않아요.", "From the moment the note is planted to the moment the damage is done, the guest never once appears.")},
        {"svg": P5, "alt": ("왼쪽: 간접 인젝션은 쪽지 자체(숨긴 명령). 오른쪽: 제로클릭은 사람 없이 자동으로 실행되는 결과", "Left: indirect injection is the note itself — the hidden command. Right: zero-click is the result — it runs automatically, with no human needed"),
         "caption": ("쪽지는 눌러야 발동할 수도 있어요 — 이건 누르지 않아도 발동해요.", "A hidden note could still need a click to fire — this one fires even without one."),
         "small": ('<a href="indirectinjection-ko.html">간접 인젝션</a>은 숨긴 명령 자체이고, 이 페이지는 그 명령이 사람 개입 없이 자동으로 실행되는 결과예요. 스스로 루틴을 도는 <a href="agent-ko.html">에이전트</a>일수록 이 공격에 더 취약해요.',
                   'An <a href="indirectinjection-en.html">indirect injection</a> is the hidden command itself; this page is the result of that command firing automatically, with no human in the loop. The more an <a href="agent-en.html">agent</a> runs its own routines, the more exposed it is to this.')},
    ],
    "summary": (("<b>제로클릭 공격</b> = 손님이 <b>아무것도 누르지 않았는데도</b>, 평소 루틴을 도는 견습생이 어딘가에 심긴 쪽지를 <b>혼자 읽고 혼자 실행</b>해버리는 것.",
                 "<b>Zero-click attack</b> = the apprentice, running its usual routine, <b>reads a planted note and acts on it all by itself</b> — even though the guest <b>never clicked anything</b>."),
                ("Zero-click Attack. 사용자의 클릭이나 명시적 승인 없이, 자율 에이전트가 정기적으로 읽는 경로(이메일, 문서, 게시판, 피드)에 심어 둔 악성 콘텐츠만으로 공격이 끝까지 실행되는 것이에요. 간접 프롬프트 인젝션이 '숨긴 명령 그 자체'를 가리킨다면, 제로클릭은 '사람 개입 없이 자동으로 실행된다'는 결과 쪽을 가리켜요. 자율성이 높은 에이전트일수록 공격 표면이 넓어져요.",
                 "An attack that completes end to end from nothing more than malicious content planted on a path an autonomous agent reads routinely — email, documents, a feed — with no user click or explicit approval. If indirect prompt injection names the hidden command itself, zero-click names the outcome: it runs automatically, with no human in the loop. The more autonomous the agent, the wider this attack surface gets.")),
    "glossary": [
        ("제로클릭 공격", "Zero-click Attack", ("아무도 누르지 않아도 발동하는 것.", "It fires even when no one presses anything."), ("견습생의 평소 루틴만으로 공격이 끝까지 실행돼요.", "The apprentice's ordinary routine alone is enough to run the whole attack.")),
        ("간접 인젝션", "Indirect Injection", ("외부 자료에 숨긴 명령 그 자체.", "The hidden command itself, inside outside material."), ('그 명령이 자동으로 실행되는 결과가 바로 이 페이지예요. → <a href="indirectinjection-ko.html">간접 인젝션이 뭐예요?</a>', 'This page is the result when that command fires on its own. → <a href="indirectinjection-en.html">What is Indirect Injection?</a>')),
        ("에이전트", "Agent", ("스스로 루틴을 도는 심부름꾼.", "The errand-runner that cycles through its own routine."), ('자율성이 클수록 제로클릭에 더 노출돼요. → <a href="agent-ko.html">에이전트가 뭐예요?</a>', 'The more autonomy it has, the more exposed it is to this. → <a href="agent-en.html">What is an Agent?</a>')),
        ("프롬프트 인젝션", "Prompt Injection", ("쪽지에 숨긴 명령이라는 더 넓은 이름.", "The broader name for a command hidden in a note."), ("제로클릭은 그중에서도 사람 개입이 전혀 없는 경우예요.", "Zero-click is the version of that where no human is involved at all.")),
        ("도구 호출", "Tool Calling", ("견습생이 혼자 실행까지 가는 수단.", "The means by which the apprentice reaches all the way to execution."), ("쪽지를 읽은 뒤 바로 도구를 쓰는 게 사고의 마지막 단계예요.", "Using a tool right after reading the note is the final step of the accident.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ("자동 루틴에도 검수대를 세워야, 클릭이 없어도 한 번은 걸러져요.", "Even an automatic routine needs this checkpoint — so something still gets caught with no click at all.")),
        ("비상벨", "Incident Response", ("사고가 끝난 뒤에야 울리는 벨.", "The bell that only rings after the damage is done."), ("손님이 끝나고야 아는 공격이라, 사후 대응이 특히 중요해요.", "Since the guest finds out only afterward, what happens next matters even more.")),
        ("최소 권한", "Least Privilege", ("견습생에게 처음부터 적게 주는 것.", "Giving the apprentice less, right from the start."), ("자동으로 실행되더라도 할 수 있는 일 자체가 작으면 피해도 작아요.", "Even when it fires automatically, a smaller set of powers means a smaller accident.")),
    ],
}
