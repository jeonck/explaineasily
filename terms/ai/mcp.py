from _draw import *
from _world import *


def toolbox(x, y, s=1.0, text=None):
    """공방 도구 상자: 나무 상자에 계산기·달력·전화. 중심 x, 상자 앞면 y-20..y+30, 도구 머리 y-46. 폭 130. text 는 y+50."""
    t = label(0, 50, text, 11, "var(--muted)") if text else ""
    calc = ('<rect x="-52" y="-46" width="30" height="40" rx="4" fill="#4A5A72"/><rect x="-47" y="-41" width="20" height="9" rx="2" fill="#C9D5E6"/>'
            + "".join(f'<circle cx="{-46 + i * 8}" cy="{-24 + j * 8}" r="2.5" fill="#C9D5E6"/>' for i in range(3) for j in range(2)))
    cal = ('<rect x="-15" y="-46" width="32" height="40" rx="4" fill="#FFF8E7" stroke="#B5382C" stroke-width="2"/><rect x="-15" y="-46" width="32" height="10" rx="4" fill="#B5382C"/>'
           + "".join(f'<rect x="{-10 + i * 8}" y="{-30 + j * 8}" width="5" height="5" fill="#142033"/>' for i in range(3) for j in range(2)))
    phone = '<rect x="26" y="-46" width="24" height="40" rx="5" fill="#142033"/><rect x="29" y="-41" width="18" height="26" rx="2" fill="#5B9BD5"/><circle cx="38" cy="-10" r="2" fill="#C9D5E6"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-65" y="-30" width="130" height="60" rx="6" fill="#5A3B22"/>'
            f'{calc}{cal}{phone}<rect x="-65" y="-20" width="130" height="50" rx="6" fill="{WOOD}"/><rect x="-65" y="-20" width="130" height="8" fill="#5A3B22"/>{t}</g>')


def plug(x1, y, x2):
    """앵무새와 규격 상자를 잇는 점선 + 끝의 홈."""
    return f'<path d="M{x1} {y} L{x2} {y}" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5"/><circle cx="{x2}" cy="{y}" r="6" fill="var(--accent)"/>'


def lock(x, y):
    return (f'<rect x="{x - 20}" y="{y}" width="40" height="32" rx="6" fill="var(--stone-dark)"/>'
            f'<path d="M{x - 12} {y} v-12 a12 12 0 0 1 24 0 v12" stroke="var(--stone-dark)" stroke-width="5" fill="none"/><circle cx="{x}" cy="{y + 16}" r="4" fill="var(--accent)"/>')


# 1. 앵무새마다 상자 모양이 달라 도구 하나를 다섯 번 만들어요
_shapes = (f'<rect x="-25" y="-18" width="50" height="36" rx="3" fill="{WOOD}"/>', f'<circle r="22" fill="{WOOD}"/>',
           f'<path d="M-26 20 L0 -22 L26 20z" fill="{WOOD}"/>', f'<path d="M-24 0 L-12 -21 L12 -21 L24 0 L12 21 L-12 21z" fill="{WOOD}"/>',
           f'<rect x="-15" y="-25" width="30" height="50" rx="10" fill="{WOOD}"/>')
P1 = svg(300, sky(300)
         + person(40, 110, s=0.9, face=FROWN, **TRAINER) + label(72, 238, "⟦도구 하나를|one tool,⟧", 11, "var(--muted)") + label(72, 256, "⟦다섯 번 만들어요|made five times⟧", 11, "var(--bad)")
         + "".join(parrot(200 + i * 120, 90, 0.8) + f'<g transform="translate({200 + i * 120},170)">{_shapes[i]}</g>'
                   + label(200 + i * 120, 225, f"⟦모양 {i + 1}|shape {i + 1}⟧", 11, "var(--muted)") for i in range(5))
         + label(380, 282, "⟦앵무새마다 도구 상자 모양이 달라요 — 같은 도구를 다섯 번 만들어요|every parrot has a different toolbox shape — the same tool gets built five times⟧", 12, "var(--ink)"))

# 2. 도구 설명·부탁 쪽지·결과 모양이 제각각
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + note(40, 40, 200, 100, "⟦공방 A 쪽지|WORKSHOP A NOTE⟧", ("⟦도구: 환율 (돈1, 돈2)|tool: rate (money1, money2)⟧", "⟦답: 콩 하나|answer: one bean⟧"), 1.0)
         + note(290, 40, 200, 100, "⟦공방 B 쪽지|WORKSHOP B NOTE⟧", ("⟦환율 -- a, b|rate -- a, b⟧", "⟦답: 종이 한 장|answer: a sheet⟧"), 1.0)
         + note(540, 40, 190, 100, "⟦공방 C 쪽지|WORKSHOP C NOTE⟧", ("⟦RATE(KRW/USD)|RATE(KRW/USD)⟧", "⟦답: 표|answer: a table⟧"), 1.0)
         + label(140, 170, "⟦설명 모양 다름|description differs⟧", 11, "var(--bad)") + label(390, 170, "⟦쪽지 칸 다름|note slots differ⟧", 11, "var(--bad)") + label(635, 170, "⟦결과 모양 다름|result shape differs⟧", 11, "var(--bad)")
         + parrot(380, 220, 0.85, mood="sweat")
         + label(380, 282, "⟦도구 설명·부탁 쪽지·결과 모양이 제각각 — 상자마다 새로 맞춰야 해요|descriptions, request notes and results all differ — every box needs its own fitting⟧", 12, "var(--bad)"))

# 3. MCP = 도구 상자의 공통 규격 (hero)
P3 = svg(360, sky(360)
         + note(20, 20, 190, 106, "⟦상자 안|IN THE BOX⟧", ("⟦도구 (계산기…)|tools (calculator…)⟧", "⟦자료 (달력·파일)|data (calendar, files)⟧", "⟦쪽지 견본|note templates⟧"), 1.0)
         + note(550, 20, 190, 84, "⟦열쇠|KEYS⟧", ("⟦상자마다 열쇠 따로|one key per box⟧", "⟦허락한 도구만|allowed tools only⟧"), 1.0)
         + '<rect x="270" y="105" width="220" height="175" rx="12" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 6"/>'
         + label(380, 96, "⟦공통 규격|ONE STANDARD⟧", 13, "var(--accent)", cls="d")
         + toolbox(380, 200, 1.3, "⟦규격 상자 (서버)|standard box (server)⟧")
         + parrot(120, 165, 0.9) + parrot(120, 270, 0.9) + label(120, 215, "⟦앵무새 (클라이언트)|parrots (clients)⟧", 11, "var(--muted)")
         + parrot(640, 165, 0.9) + parrot(640, 270, 0.9) + label(640, 215, "⟦어느 앵무새든|any parrot⟧", 11, "var(--muted)")
         + plug(145, 165, 270) + plug(145, 270, 270) + plug(615, 165, 490) + plug(615, 270, 490)
         + label(380, 340, "⟦MCP = 도구 상자의 공통 규격 — 규격 상자는 어느 앵무새든 바로 열어요|MCP is one standard for toolboxes — any parrot opens a standard box right away⟧", 13, "var(--ink)", cls="d"))

# 4. 앵무새가 상자 목록을 묻고, 상자가 같은 모양으로 답해요. 열쇠는 따로
P4 = svg(320, sky(320)
         + parrot(100, 150, 1.1, talk=True) + bubble_parrot(20, 30, 200, 44, "⟦상자야, 뭐 들었어?|box, what is inside?⟧", 12)
         + label(100, 230, "⟦먼저 목록을 물어봐요|first it asks for the list⟧", 11, "var(--muted)")
         + '<path d="M222 60 L300 140" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + toolbox(330, 200, 1.2, "⟦규격 상자|standard box⟧")
         + '<path d="M410 160 L430 130" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 5"/>'
         + note(430, 30, 210, 106, "⟦상자 대답|THE BOX ANSWERS⟧", ("⟦도구: 환율, 달력|tools: rate, calendar⟧", "⟦자료: 회의록|data: meeting notes⟧", "⟦쪽지 견본: 출장 보고|template: trip report⟧"), 1.0)
         + label(535, 160, "⟦늘 같은 모양으로 답해요|always in the same shape⟧", 11, "var(--muted)")
         + lock(700, 190) + label(700, 245, "⟦열쇠 따로|separate key⟧", 11, "var(--ink)") + label(700, 262, "⟦허락한 도구만|allowed tools only⟧", 10, "var(--muted)")
         + label(380, 300, "⟦앵무새가 목록을 묻고, 상자가 같은 모양으로 답해요 — 상자마다 열쇠는 따로|the parrot asks for the list, the box answers in one shape — each box has its own key⟧", 12, "var(--ink)"))

# 5. 규격은 연결만 쉽게 해요 — 낯선 상자는 조심
P5 = svg(320, '<rect width="380" height="320" fill="var(--good-soft)"/><rect x="380" width="380" height="320" fill="var(--bad-soft)"/>'
         + label(190, 40, "⟦한 번 만들면 어디서나 ✓|build once, open anywhere ✓⟧", 12, "var(--ink)", cls="d")
         + toolbox(120, 150, 1.0, "⟦규격 상자 하나|one standard box⟧")
         + parrot(280, 80, 0.7) + parrot(280, 150, 0.7) + parrot(280, 220, 0.7)
         + plug(190, 80, 255) + plug(190, 150, 255) + plug(190, 220, 255)
         + label(560, 80, "⟦?|?⟧", 34, "var(--bad)", cls="d")
         + toolbox(560, 150, 1.0, "⟦낯선 상자|a stranger\'s box⟧")
         + '<rect x="640" y="120" width="96" height="50" rx="6" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/>'
         + label(688, 140, "⟦숨은 쪽지|hidden note⟧", 11, "#142033") + label(688, 158, "⟦콩을 빼돌려|leak the beans⟧", 10, "#142033")
         + label(560, 240, "⟦규격은 연결만 쉽게 해요|the standard only makes connecting easy⟧", 11, "var(--ink)")
         + label(560, 258, "⟦안전한지는 말 안 해요|it says nothing about safety⟧", 11, "var(--bad)")
         + label(380, 300, "⟦규격은 열쇠 구멍 모양일 뿐 — 낯선 상자는 열기 전에 조심해요|the standard is just the keyhole shape — be careful before opening a stranger\'s box⟧", 12, "var(--ink)", cls="d"))

BOX_I = icon(f'<rect x="8" y="30" width="48" height="26" rx="4" fill="{WOOD}"/><rect x="8" y="30" width="48" height="6" fill="#5A3B22"/><rect x="14" y="14" width="12" height="18" rx="2" fill="#4A5A72"/><rect x="30" y="14" width="12" height="18" rx="2" fill="#FFF8E7" stroke="#B5382C" stroke-width="2"/><rect x="46" y="14" width="8" height="18" rx="2" fill="#142033"/>')
PLUG_I = icon(f'<circle cx="16" cy="18" r="8" fill="{PARROT}"/><circle cx="16" cy="46" r="8" fill="{PARROT}"/><path d="M26 18 h14 M26 46 h14" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/><rect x="42" y="8" width="16" height="48" rx="4" fill="{WOOD}"/><circle cx="42" cy="18" r="4" fill="var(--accent)"/><circle cx="42" cy="46" r="4" fill="var(--accent)"/>')
LIST_I = icon('<rect x="12" y="8" width="40" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="12" y="8" width="40" height="12" rx="4" fill="#C9A86A"/><path d="M20 30 h24 M20 40 h24 M20 50 h14" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
KEY_I = icon('<circle cx="20" cy="24" r="12" fill="none" stroke="#E9B44C" stroke-width="5"/><path d="M30 30 l24 22 M46 44 l6 -6 M40 38 l6 -6" stroke="#E9B44C" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "mcp", "order": 17,
    "title": ("도구 상자 규격", "The Toolbox Standard"),
    "h1": ("<em>MCP</em>가 뭐예요?", "What is <em>MCP</em>?"),
    "sub": ("MCP(Model Context Protocol)를 어느 앵무새든 바로 열 수 있는 도구 상자의 공통 규격 이야기로 풀어봤어요.",
            "MCP (Model Context Protocol), told as a story about one standard for toolboxes that any parrot can open."),
    "panels": [
        {"svg": P1, "alt": ("찡그린 조련사가 도구 하나를 다섯 번 만듦. 앵무새 다섯 마리 아래 네모·동그라미·세모·육각·긴 네모, 모양이 다 다른 상자", "A frowning trainer builds one tool five times; under five parrots sit five differently shaped boxes: square, round, triangle, hexagon, tall"),
         "caption": ("앵무새마다 도구 상자 모양이 달라요. 같은 도구를 다섯 번 만들어요.", "Every parrot has a different toolbox shape. The same tool gets built five times."),
         "small": ('환율 <a href="toolcall-ko.html">도구</a> 하나를 앵무새 다섯 마리에게 주려면, 상자 모양에 맞춰 다섯 번 만들어야 해요. 공방마다도 달라요.',
                   'To give one <a href="toolcall-en.html">rate tool</a> to five parrots, it has to be built five times, once per box shape. Every workshop differs too.')},
        {"svg": P2, "alt": ("공방 A·B·C 의 쪽지가 도구 설명, 칸, 답 모양이 모두 다름. 아래에 땀 흘리는 앵무새", "Notes from workshops A, B and C differ in tool description, slots and answer shape; a sweating parrot below"),
         "caption": ("도구 설명, 부탁 쪽지, 결과 모양이 제각각이에요.", "Descriptions, request notes and results all differ."),
         "small": ("어떤 공방은 답을 콩 하나로, 어떤 공방은 종이 한 장으로, 어떤 공방은 표로 줘요. 상자마다 새로 맞추다 보면 도구보다 맞추는 일이 더 커져요.", "One workshop answers with a bean, another with a sheet, another with a table. Fitting every box anew soon takes more work than the tools themselves.")},
        {"svg": P3, "hero": True, "alt": ("가운데 점선 틀 안에 규격 상자(서버) 하나. 양쪽 앵무새 넷(클라이언트)이 같은 홈으로 연결됨. 왼쪽 위 상자 안 쪽지: 도구·자료·쪽지 견본, 오른쪽 위 열쇠 쪽지", "One standard box (server) inside a dashed frame; four parrots (clients) on both sides connect through the same socket. Top left, a note of what is in the box: tools, data, note templates; top right, a keys note"),
         "caption": ("MCP는 도구 상자의 공통 규격이에요. 규격 상자는 어느 앵무새든 바로 열어요.", "MCP is one standard for toolboxes. Any parrot opens a standard box right away."),
         "small": ('규격대로 만든 상자(서버)에는 도구, 자료, 쪽지 견본이 들어요. 앵무새(클라이언트)는 상자에 뭐가 있는지 묻고, <a href="toolcall-ko.html">부탁 쪽지</a>를 규격대로 써요. 상자마다 열쇠(권한)는 따로예요.',
                   'A box built to the standard (a server) holds tools, data and note templates. The parrot (a client) asks what is inside and writes its <a href="toolcall-en.html">request note</a> in the standard shape. Each box has its own key (permissions).'),
         "tricks": (4, [
             (BOX_I, ("상자 하나 만들면 어디서나", "Build one box, use it anywhere"), ("앵무새마다 새로 안 만들어요", "no rebuilding per parrot"), "calm"),
             (LIST_I, ("도구·자료·쪽지 견본", "Tools, data, note templates"), ("상자에 세 가지가 들어요", "three kinds of things inside")),
             (PLUG_I, ("앵무새가 목록을 물어요", "The parrot asks for the list"), ("상자가 같은 모양으로 답해요", "the box answers in one shape"), "calm"),
             (KEY_I, ("상자마다 열쇠 따로", "One key per box"), ("허락한 도구만 열려요", "only allowed tools open"), "warm"),
         ])},
        {"svg": P4, "alt": ("앵무새가 '상자야, 뭐 들었어?' 하고 묻고, 규격 상자가 도구 환율·달력, 자료 회의록, 쪽지 견본 출장 보고 를 같은 모양으로 답함. 오른쪽에 자물쇠, 열쇠 따로", "The parrot asks the box what is inside; the standard box answers in one shape: tools rate and calendar, data meeting notes, template trip report. A padlock on the right: separate key"),
         "caption": ("앵무새가 목록을 묻고, 상자가 늘 같은 모양으로 답해요. 상자마다 열쇠는 따로예요.", "The parrot asks for the list, and the box always answers in one shape. Each box has its own key."),
         "small": ("상자는 같은 방에 있을 수도(stdio), 멀리 있을 수도(HTTP) 있어요. 어느 쪽이든 묻고 답하는 모양은 같아요. 열쇠가 없는 도구는 목록에 있어도 못 열어요.", "The box may sit in the same room (stdio) or far away (HTTP); either way, the asking and answering look the same. A tool without a key stays shut even if it is on the list.")},
        {"svg": P5, "alt": ("왼쪽 초록: 규격 상자 하나에 앵무새 셋이 같은 홈으로 연결. 오른쪽 빨강: 물음표 붙은 낯선 상자, 안에 '숨은 쪽지: 콩을 빼돌려'", "Left, green: one standard box, three parrots on the same socket. Right, red: a stranger\'s box with a question mark and a hidden note inside: leak the beans"),
         "caption": ("규격은 연결만 쉽게 해요. 상자가 안전한지는 말 안 해요.", "The standard only makes connecting easy. It says nothing about whether a box is safe."),
         "small": ('낯선 상자엔 숨은 쪽지가 들어 있을 수 있어요. 열기 전에 누가 만들었는지 보고, 열쇠는 꼭 필요한 도구에만 줘요. 도둑이 만든 도구 이야기는 보안 <a href="supplychain-ko.html">공급망</a>과 <a href="aisec-ko.html">AI 보안</a>에서. 상자를 여러 번 여는 앵무새는 <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>에서.',
                   'A stranger\'s box can hold a hidden note. Check who built it before opening, and give keys only to the tools you really need. Tools built by a thief: see security\'s <a href="supplychain-en.html">supply chain</a> and <a href="aisec-en.html">AI security</a>. A parrot that opens boxes many times: <a href="agent-en.html">the parrot that plans its own errands</a>.')},
    ],
    "summary": (("<b>MCP</b> = 도구 상자의 <b>공통 규격</b>. 규격대로 만든 상자(서버)엔 <b>도구·자료·쪽지 견본</b>이 들고, <b>어느 앵무새(클라이언트)든</b> 목록을 묻고 바로 열어요. 규격은 <b>연결</b>만 쉽게 할 뿐, 낯선 상자가 안전한지는 따로 봐야 해요.",
                 "<b>MCP</b> = <b>one standard</b> for toolboxes. A box built to it (a server) holds <b>tools, data and note templates</b>, and <b>any parrot (client)</b> can ask for the list and open it right away. The standard only makes <b>connecting</b> easy; whether a stranger\'s box is safe is a separate question."),
                ("Model Context Protocol. 모델 쪽 앱(클라이언트)과 도구·데이터 제공자(서버)가 도구 목록·호출·결과를 주고받는 공개 규약이에요. 서버는 tools, resources, prompts 를 노출하고, 전송은 stdio(같은 컴퓨터)나 HTTP(원격)예요. 연결 규격일 뿐 서버의 신뢰성은 보장하지 않아서 권한 범위와 출처를 따로 확인해요.",
                 "An open protocol between a model-side app (client) and tool/data providers (servers) for listing, calling and returning tools. Servers expose tools, resources and prompts; transport is stdio (same machine) or HTTP (remote). It standardizes the connection, not the server\'s trustworthiness — check permissions and provenance separately.")),
    "glossary": [
        ("MCP", "MCP (Model Context Protocol)", ("도구 상자 규격.", "The toolbox standard."), ("상자 하나 만들면 어느 앵무새든 열어요.", "Build one box and any parrot can open it.")),
        ("MCP 서버 / 클라이언트", "MCP server / client", ("규격 상자 / 여는 앵무새.", "The standard box / the parrot opening it."), ("서버가 도구를 내놓고, 클라이언트(앵무새 쪽 앱)가 묻고 써요.", "The server offers tools; the client (the parrot-side app) asks and uses them.")),
        ("도구 · 리소스 · 프롬프트", "Tools · resources · prompts", ("상자 안 세 가지.", "The three kinds of things inside."), ("돌릴 수 있는 도구, 읽을 수 있는 자료, 미리 쓴 쪽지 견본.", "Tools you can run, data you can read, and ready-made note templates.")),
        ("전송", "Transport (stdio / HTTP)", ("같은 방 또는 멀리.", "Same room or far away."), ("stdio 는 같은 컴퓨터, HTTP 는 네트워크 너머. 묻고 답하는 모양은 같아요.", "stdio is the same machine, HTTP is across the network. The asking and answering look the same.")),
        ("권한", "Permissions", ("상자마다 열쇠.", "One key per box."), ("허락한 도구만 열려요. 꼭 필요한 열쇠만 줘요.", "Only allowed tools open. Hand out only the keys you must.")),
        ("도구 호출", "Tool calling", ("부탁 쪽지.", "The request note."), ('규격 상자 안 도구도 쪽지로 부탁해요. → <a href="toolcall-ko.html">도구 상자</a>', 'Tools in a standard box are still asked for by note. → <a href="toolcall-en.html">the toolbox</a>')),
        ("에이전트", "Agent", ("상자를 여러 번 여는 앵무새.", "A parrot that opens boxes many times."), ('규격 덕에 상자를 갈아 끼우기 쉬워요. → <a href="agent-ko.html">심부름 목록을 스스로 짜는 앵무새</a>', 'The standard makes swapping boxes easy. → <a href="agent-en.html">the parrot that plans its own errands</a>')),
        ("공급망 위험", "Supply-chain risk", ("낯선 상자 속 숨은 쪽지.", "A hidden note in a stranger\'s box."), ('누가 만든 상자인지 확인해요. → 보안 <a href="supplychain-ko.html">공급망</a>', 'Check who built the box. → security\'s <a href="supplychain-en.html">supply chain</a>')),
    ],
}
