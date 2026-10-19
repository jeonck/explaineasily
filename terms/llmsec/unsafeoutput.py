from _draw import *
from _world import *


def machine(x, y, s=1.0, running=False):
    """자동 처리 기계 (출력을 그대로 받아 실행하는 장치). running=True 면 레버가 당겨져 있음."""
    c = "var(--bad)" if running else "#5A3B22"
    out = (f'<g transform="translate({x},{y}) scale({s})">'
           f'<rect x="-40" y="-10" width="80" height="60" rx="6" fill="#8B5E3C"/>'
           f'<rect x="-32" y="-2" width="64" height="20" rx="3" fill="#2E3D57"/>'
           f'<circle cx="-18" cy="8" r="4" fill="{c}"/><circle cx="0" cy="8" r="4" fill="{c}"/><circle cx="18" cy="8" r="4" fill="{c}"/>'
           f'<rect x="-6" y="-34" width="12" height="26" rx="3" fill="{c}" transform="rotate({-28 if running else 0} 0 -10)"/>')
    if running:
        out += '<path d="M-44 -16 l-10 -10 M44 -16 l10 -10" stroke="var(--bad)" stroke-width="3" stroke-linecap="round"/>'
    return out + '</g>'


def belt(x1, x2, y, color="#8B5E3C"):
    return f'<rect x="{x1}" y="{y - 5}" width="{x2 - x1}" height="10" fill="{color}"/>'


# 1. 접시가 검수대 없이 바로 기계로 들어가요
P1 = svg(320, sky(320)
         + person(80, 150, s=0.75, face=EYES, **CHEF) + dish(200, 190, 0.6)
         + label(80, 262, "⟦주방장|chef⟧", 11, "var(--muted)")
         + belt(230, 480, 195)
         + label(350, 165, "⟦검수 없이 그대로|no check, just as it is⟧", 12, "var(--bad)")
         + machine(560, 190, 0.85)
         + label(560, 262, "⟦자동 처리 기계|auto-processing machine⟧", 11, "var(--muted)")
         + label(380, 300, "⟦접시에 적힌 대로 기계가 바로 움직여요|the machine moves exactly as the dish says, right away⟧", 13, "var(--ink)"))

# 2. 왜 어려운가: 접시엔 위험한지 표시가 없어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + dish(170, 130, 1.0, bad=True) + label(170, 200, "⟦위험한 접시|a dangerous dish⟧", 11, "var(--bad)")
         + dish(170, 250, 1.0) + label(170, 290, "⟦보통 접시|an ordinary dish⟧", 11, "var(--muted)")
         + bubble(320, 90, 260, 60, "⟦둘 다 모양이 똑같아요 — 글자를 읽어 보지 않으면 몰라요|they look the same — you can't tell without reading the words⟧", 12, "var(--panel)", "var(--line)", "left")
         + machine(640, 190, 0.85) + label(640, 255, "⟦기계는 모양을 안 따져요, 글자를 그대로 따라요|the machine doesn't judge the shape — it just obeys the words⟧", 11, "var(--ink)")
         + label(380, 280, "⟦주방장도 기계도 서로를 의심하지 않아요|neither the chef nor the machine doubts the other⟧", 12, "var(--ink)"))

# 3. 안전하지 않은 출력 처리 = 요리를 그대로 기계에 넣었다가 사고 (hero)
P3 = svg(340, sky(340)
         + person(70, 150, s=0.7, face=EYES, **CHEF) + dish(170, 200, 0.55, bad=True)
         + belt(200, 400, 205)
         + machine(430, 200, 0.95, running=True)
         + label(430, 275, "⟦경보!|ALARM!⟧", 16, "var(--bad)", cls="d")
         + '<path d="M470 150 q14 -20 28 0 q4 10 -4 16 q-14 6 -24 -6 z" fill="var(--bad)"/>'
         + person(630, 160, s=0.65, face=FROWN, **MANAGER)
         + label(630, 240, "⟦사장님이 뒷수습해요|the manager cleans up the mess⟧", 11, "var(--muted)")
         + label(380, 30, "⟦안전하지 않은 출력 처리 = 요리를 그대로 기계에 넣었다가 사고|Unsafe Output Handling = feeding the dish straight into the machine — and it breaks⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦접시(출력)를 검사 없이 다른 기계(시스템)에 바로 넣어서 생기는 일이에요|it happens when the dish — the model's output — is fed straight into another system, unchecked⟧", 12, "var(--muted)"))

# 4. 안전한 길 vs 위험한 길
P4 = svg(330, sky(330)
         + label(130, 55, "⟦위험한 길|the risky path⟧", 13, "var(--bad)", cls="d")
         + person(40, 110, s=0.6, face=EYES, **CHEF) + dish(130, 140, 0.5)
         + '<path d="M165 140 L270 140" stroke="var(--bad)" stroke-width="3"/><path d="M260 134 L270 140 L260 146" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + machine(320, 140, 0.6, running=True)
         + label(410, 55, "⟦안전한 길|the safe path⟧", 13, "var(--good)", cls="d")
         + person(460, 220, s=0.6, face=EYES, **CHEF) + dish(550, 250, 0.5)
         + '<path d="M585 250 L630 250" stroke="var(--good)" stroke-width="3"/><path d="M620 244 L630 250 L620 256" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + person(660, 205, s=0.55, face=SMILE, **TASTER)
         + '<path d="M690 220 L690 250" stroke="var(--good)" stroke-width="3"/><path d="M684 240 L690 250 L696 240" stroke="var(--good)" stroke-width="3" fill="none"/>'
         + machine(690, 280, 0.5)
         + label(690, 320, "⟦허락된 모양만 통과|only the expected shape gets through⟧", 11, "var(--good)")
         + label(190, 190, "⟦글자 그대로 바로 실행|runs the words exactly, right away⟧", 11, "var(--bad)"))

# 5. 결과·이웃 용어와의 차이
P5 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + machine(150, 150, 0.9, running=True)
         + label(150, 225, "⟦코드를 그대로 실행|runs code as-is⟧", 11, "var(--ink)")
         + machine(380, 150, 0.9, running=True)
         + label(380, 225, "⟦장부에 글자를 그대로 심음|plants text straight into the records⟧", 11, "var(--ink)")
         + machine(610, 150, 0.9, running=True)
         + label(610, 225, "⟦화면에 그대로 떠요|shows up on screen as-is⟧", 11, "var(--ink)")
         + label(380, 265, "⟦맛보기 검수대(가드레일)는 늘 세워 두는 울타리, 이건 검수대 없이 실제로 터진 사고예요|a taster (guardrail) is the fence you always keep up — this is the accident that happens without one⟧", 12, "var(--ink)", cls="d")
         + label(380, 295, "⟦기계가 받는 몫도 꼭 필요한 만큼만이어야 해요|the machine itself should only ever get as much power as it needs⟧", 11, "var(--muted)"))

RUN_I = icon('<rect x="8" y="8" width="48" height="48" rx="6" fill="#8B5E3C"/><rect x="16" y="16" width="32" height="12" rx="2" fill="#2E3D57"/><circle cx="24" cy="44" r="5" fill="var(--bad)"/><circle cx="40" cy="44" r="5" fill="var(--bad)"/>')
CHECK_I = icon('<ellipse cx="32" cy="40" rx="22" ry="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><circle cx="32" cy="32" r="10" fill="var(--good)"/><path d="M26 32 l4 5 l9 -11" stroke="#fff" stroke-width="3" fill="none"/>')
SHAPE_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M22 32 h20 M32 22 v20" stroke="var(--accent)" stroke-width="4"/>')
KEY_I = icon('<rect x="8" y="30" width="30" height="22" rx="3" fill="#8B5E3C"/><circle cx="48" cy="18" r="8" fill="none" stroke="#E9B44C" stroke-width="4"/><path d="M48 26 v18 M48 38 h6 M48 44 h8" stroke="#E9B44C" stroke-width="4" stroke-linecap="round"/>')

PAGE = {
    "slug": "unsafeoutput", "order": 18,
    "title": ("접시를 그대로 기계에 넣다가", "Feeding the Dish Straight Into the Machine"),
    "h1": ("<em>안전하지 않은 출력 처리</em>가 뭐예요?", "What is <em>Unsafe Output Handling</em>?"),
    "sub": ("안전하지 않은 출력 처리를, 완성된 접시를 검수 없이 자동 처리 기계에 그대로 넣었다가 사고가 나는 이야기로 풀어봤어요.",
            "Unsafe output handling, told as a story about a finished dish being fed straight into an automatic machine, unchecked — and the accident that follows."),
    "panels": [
        {"svg": P1, "alt": ("주방장이 만든 접시가 검수대를 거치지 않고 벨트를 타고 바로 자동 처리 기계로 들어감", "A dish the chef made rides a belt straight into an auto-processing machine, skipping any check"),
         "caption": ("접시에 적힌 대로 기계가 바로 움직여요.", "The machine moves exactly as the dish says, right away."),
         "small": ("검수대 없이, 접시가 그대로 다음 기계의 명령이 돼요.", "With no check in between, the dish becomes the next machine's command, exactly as written.")},
        {"svg": P2, "alt": ("위험한 접시와 보통 접시가 모양은 똑같음. 자동 처리 기계는 모양을 따지지 않고 글자를 그대로 따름", "A dangerous dish and an ordinary dish look identical; the machine doesn't judge shape — it just obeys the words"),
         "caption": ("주방장도 기계도 서로를 의심하지 않아요.", "Neither the chef nor the machine doubts the other."),
         "small": ("접시가 위험한지는 읽어 보지 않으면 몰라요 — 모양만으론 구별이 안 돼요.", "You can't tell a dangerous dish from a safe one just by looking — only by reading the words.")},
        {"svg": P3, "hero": True, "alt": ("위험한 접시가 벨트를 타고 기계로 들어가 경보가 울리고 사장님이 뒷수습함", "A dangerous dish rides the belt into the machine, an alarm sounds, and the manager cleans up the mess"),
         "caption": ("요리를 그대로 기계에 넣었다가 사고가 나요.", "Feeding the dish straight into the machine — and it breaks."),
         "small": ("접시(출력)를 검사 없이 다른 기계(시스템)에 바로 넣어서 생기는 구체적인 사고예요.", "A concrete accident that happens when the dish — the model's output — is fed straight into another system, unchecked."),
         "tricks": (4, [
             (CHECK_I, ("넣기 전에 한 번 봐요", "Check it before it runs"), ("기계 앞에 검수대를 세워요", "put a check before the machine")),
             (SHAPE_I, ("허락된 모양만 받아요", "Accept only the expected shape"), ("자유 글자보다 정해진 칸이 안전해요", "a fixed form beats free text"), "calm"),
             (RUN_I, ("곧바로 실행은 피해요", "Avoid running it immediately"), ("코드·명령은 특히 더요", "especially code and commands"), "warm"),
             (KEY_I, ("기계 몫도 최소한만", "Give the machine only what it needs"), ("터져도 작게 터지게요", "so a break stays small")),
         ])},
        {"svg": P4, "alt": ("위: 위험한 길, 접시가 바로 기계로 들어가 실행됨. 아래: 안전한 길, 접시가 맛보기 검수원을 지나 허락된 모양만 기계로 들어감", "Top: the risky path, the dish goes straight into the machine and runs. Bottom: the safe path, the dish passes a taster first and only the expected shape reaches the machine"),
         "caption": ("글자 그대로 바로 실행하는 길과, 한 번 더 보는 길이에요.", "One path runs the words exactly, right away. The other looks once more first."),
         "small": ("안전한 길은 접시를 한 번 더 보고, 허락된 모양만 기계로 보내요.", "The safe path checks the dish once more, and only lets the expected shape through to the machine.")},
        {"svg": P5, "alt": ("세 기계가 각각 코드·장부·화면에 글자를 그대로 심음. 검수대는 평소 세워 두는 울타리고, 이건 검수대 없이 실제로 터진 사고라는 설명", "Three machines each plant text as-is into code, records, and a screen; a note explains that a taster is the fence you keep up, while this is the accident without one"),
         "caption": ("코드로, 장부로, 화면으로 — 다 같은 방식으로 터져요.", "Into code, into records, onto a screen — it breaks the same way each time."),
         "small": ('맛보기 검수대(<a href="guardrail-ko.html">가드레일</a>)는 늘 세워 두는 울타리고, 이건 그 검수대 없이 접시가 <a href="toolcall-ko.html">도구</a>처럼 바로 실행돼 터진 구체적인 사고예요.',
                   'A taster — a <a href="guardrail-en.html">guardrail</a> — is the fence you always keep up. This is the concrete accident that happens when the dish runs like a <a href="toolcall-en.html">tool call</a>, with no taster at all.')},
    ],
    "summary": (("<b>안전하지 않은 출력 처리</b> = 주방장이 만든 <b>접시를 검수 없이 그대로</b> 자동 처리 기계에 넣었다가, 접시에 적힌 위험한 말을 기계가 <b>그대로 따라 해서</b> 생기는 사고.",
                 "<b>Unsafe output handling</b> = feeding the chef's <b>dish straight into an automatic machine, unchecked</b> — and the machine <b>obeys</b> whatever dangerous words were written on it."),
                ("Unsafe Output Handling. LLM의 출력(코드, SQL, 셸 명령, HTML 등)을 검증·이스케이프·샌드박싱 없이 그대로 다른 시스템(해석기, DB, 셸, 브라우저)에 넘겨 실행하는 취약점이에요. 결과는 원격 코드 실행, SQL/명령 인젝션, XSS 등 전통적인 인젝션 사고와 같은 모양으로 나타나요. 가드레일이 입출력을 거르는 일반 장치라면, 이건 그 장치가 없을 때 실제로 터지는 구체적 사고예요.",
                 "A vulnerability where an LLM's output (code, SQL, shell commands, HTML, …) is passed to another system — an interpreter, a database, a shell, a browser — and executed without validation, escaping, or sandboxing. The result looks like classic injection: remote code execution, SQL/command injection, XSS. A guardrail is the general device that filters input and output; this is the concrete accident that happens when that device is missing.")),
    "glossary": [
        ("안전하지 않은 출력 처리", "Unsafe Output Handling", ("접시를 그대로 기계에 넣는 것.", "Feeding the dish straight into the machine."), ("기계가 접시에 적힌 말을 그대로 따라 해요.", "The machine obeys whatever is written on the dish, exactly.")),
        ("가드레일", "Guardrail", ("맛보기 검수대.", "The tasting checkpoint."), ('AI 세계의 일반 장치예요, 이건 그게 없을 때 터지는 사고. → <a href="guardrail-ko.html">가드레일이 뭐예요?</a>', 'The general device in the AI world — this page is the accident when it is missing. → <a href="guardrail-en.html">What is a Guardrail?</a>')),
        ("도구 호출", "Tool Calling", ("기계가 바로 움직이는 몫.", "The part where the machine just acts."), ('출력이 도구 호출처럼 바로 실행되는 게 문제예요. → <a href="toolcall-ko.html">도구 호출이 뭐예요?</a>', 'The problem is output running immediately, like a tool call. → <a href="toolcall-en.html">What is Tool Calling?</a>')),
        ("코드 생성", "Code Generation", ("주방장이 직접 적는 조리법 쪽지.", "A recipe note the chef writes out directly."), ('생성된 코드를 그대로 실행하는 게 가장 흔한 사고예요. → <a href="codegen-ko.html">코드 생성이 뭐예요?</a>', 'Running generated code as-is is the most common version of this accident. → <a href="codegen-en.html">What is Code Generation?</a>')),
        ("인젝션", "Injection", ("기계에 글자를 명령으로 심는 일.", "Planting text into a machine as a command."), ('보안 마을의 일반 개념이에요, 모양이 똑같아요. → <a href="injection-ko.html">인젝션이 뭐예요?</a>', 'The general concept in the security world — the shape is identical. → <a href="injection-en.html">What is Injection?</a>')),
        ("최소 권한", "Least Privilege", ("기계에게도 꼭 필요한 만큼만.", "Even the machine gets only what it needs."), ("기계 권한이 작을수록 사고도 작아요.", "The smaller the machine's power, the smaller the accident.")),
        ("샌드박스", "Sandbox", ("사고가 나도 주방 전체로 안 퍼지게 담는 상자.", "A box that keeps an accident from spreading to the whole kitchen."), ("실행은 항상 격리된 곳에서 하는 게 안전해요.", "Running things inside isolation is always the safer choice.")),
        ("출력 검증", "Output Validation", ("기계 앞에 세운 한 번 더 보는 눈.", "One more look, right before the machine."), ("허락된 모양만 통과시키고 나머지는 돌려보내요.", "Only the expected shape passes through — everything else is sent back.")),
    ],
}
