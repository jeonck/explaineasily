from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
ME = dict(hat=None, shirt="#4A5A72", face=SMILE)


def building(x, y, name, roof="var(--stone)", s=1.0, awning=False):
    top = (f'<path d="M-46 0 h92 l-8 -20 h-76 z" fill="var(--accent)"/>' + "".join(f'<rect x="{-46 + i * 18}" y="-20" width="9" height="20" fill="#FFD9B8"/>' for i in range(5))
           if awning else f'<path d="M-50 0 L0 -30 L50 0 Z" fill="{roof}"/>')
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="64" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'{top}<rect x="-10" y="30" width="20" height="34" fill="{WOOD}"/><rect x="-32" y="12" width="14" height="12" fill="var(--sky)"/><rect x="18" y="12" width="14" height="12" fill="var(--sky)"/>'
            f'{label(0, 84, name, 12, "var(--muted)")}</g>')


def alley(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-10" width="80" height="120" fill="var(--night)"/>'
            f'<rect x="-34" y="-34" width="68" height="26" rx="4" fill="#FFE97A"/>{label(0, -16, "⟦공짜 선물!|FREE GIFTS!⟧", 11, "#142033")}'
            f'<circle cx="0" cy="40" r="14" fill="{SKIN}"/><path d="M-14 36 Q0 18 14 36 Z" fill="var(--bad)"/><path d="M-10 36 h20 v6 h-20z" fill="#111C30"/></g>')


def crate(x, y, s=1.0, bug=False, sealed=False, opened=False):
    b = ('<g transform="translate(0,-4)"><ellipse rx="9" ry="6" fill="var(--bad)"/><circle cx="-9" r="4" fill="var(--bad)"/>'
         '<path d="M-6 -6 l-5 -5 M6 -6 l5 -5 M-6 6 l-5 5 M6 6 l5 5" stroke="var(--bad)" stroke-width="2"/></g>') if bug else ""
    seal = '<rect x="-26" y="-6" width="52" height="12" fill="#E9B44C"/><circle r="7" fill="var(--bad)"/>' if sealed else ""
    lid = '<rect x="-30" y="-36" width="60" height="10" fill="#8B5E3C" transform="rotate(-25 -30 -26)"/>' if opened else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-22" width="52" height="44" rx="3" fill="#8B5E3C"/>'
            f'<path d="M-26 -22 L26 22 M26 -22 L-26 22" stroke="#5A3B22" stroke-width="3"/>{seal}{lid}{b}</g>')


def town_map(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="80" height="60" rx="4" fill="#FFF3D6" stroke="#C9A86A" stroke-width="2"/>'
            f'<path d="M8 12 h64 M8 30 h64 M8 48 h64 M28 6 v48 M52 6 v48" stroke="#C9A86A" stroke-width="2"/>'
            f'<rect x="30" y="32" width="20" height="14" fill="var(--bad)"/><rect x="54" y="14" width="16" height="14" fill="var(--bad)"/><rect x="10" y="14" width="16" height="14" fill="var(--good)"/></g>')


TOWN = building(480, 120, "⟦시장|market⟧", awning=True) + building(590, 120, "⟦도서관|library⟧") + building(700, 120, "⟦극장|theater⟧", "var(--accent)")

# 1. 매일 바깥 마을에 나간다
P1 = svg(300, sky(300) + castle(10, 90, 0.45)
         + '<path d="M215 210 C300 210 340 200 430 200" stroke="var(--stone-dark)" stroke-width="10" fill="none" stroke-linecap="round"/>'
         + person(240, 110, s=0.7, **ME) + person(320, 100, s=0.7, hat="#E9B44C", shirt="#4A5A72", face=SMILE) + person(380, 115, s=0.7, hat="#5B8DEF", shirt="#4A5A72", face=SMILE)
         + TOWN + label(600, 50, "⟦바깥 마을|the outside town⟧", 14, "var(--ink)", cls="d")
         + label(380, 280, "⟦시장, 도서관, 극장… 인터넷이에요|market, library, theater… that\'s the internet⟧", 13, "var(--muted)"))

# 2. 위험한 골목
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + building(120, 100, "⟦시장|market⟧", awning=True, s=0.9) + alley(300, 90)
         + person(460, 120, s=0.85, **ME, extra='<g transform="translate(70,60)">' + crate(0, 0, 0.7, bug=True) + "</g>")
         + '<path d="M540 190 L640 190" stroke="var(--bad)" stroke-width="3" stroke-dasharray="8 8"/><path d="M630 180 L642 190 L630 200" stroke="var(--bad)" stroke-width="3" fill="none"/>'
         + small_castle(650, 120, 0.5)
         + label(300, 240, "⟦위험한 골목|a bad alley⟧", 13, "var(--bad)")
         + label(500, 270, "⟦받아온 상자에 벌레가 들어 있어요|the box they brought home has a bug in it⟧", 13, "var(--muted)"))

# 3. SWG = 마을로 나가는 성문의 검문소 (hero)
P3 = svg(340, sky(340) + castle(0, 120, 0.4)
         + '<path d="M190 235 C260 235 280 225 320 225 M440 225 C480 225 500 215 540 215" stroke="var(--stone-dark)" stroke-width="10" fill="none" stroke-linecap="round"/>'
         + gatehouse(380, 130) + label(380, 250, "⟦검문소|the checkpoint⟧", 13, "var(--ink)", cls="d")
         + person(430, 110, s=0.7, face=EYES, **GUARD) + town_map(470, 190, 0.8)
         + person(230, 150, s=0.7, **ME, extra='<g transform="translate(70,60)">' + crate(0, 0, 0.5) + "</g>")
         + building(580, 90, "⟦시장|market⟧", awning=True, s=0.7) + alley(660, 70, 0.7) + building(730, 90, "⟦극장|theater⟧", "var(--accent)", 0.6)
         + label(380, 320, "⟦어디 가는지 보고, 위험한 골목이면 막고, 들고 오는 상자를 열어봐요|sees where you\'re going, blocks bad alleys, opens the boxes you bring back⟧", 13, "var(--muted)"))

# 4. 막고, 열어보고, 봉인도 뜯는다
SIGN = ('<g transform="translate(120,70)"><rect x="-70" y="0" width="140" height="70" rx="8" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/>'
        + label(0, 28, "⟦도박 골목|gambling alley⟧", 14, "var(--ink)") + '<rect x="-50" y="40" width="100" height="22" rx="4" fill="var(--bad)"/>' + label(0, 56, "⟦막힘|BLOCKED⟧", 12, "#FFF") + "</g>")
P4 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>' + SIGN + label(120, 230, "⟦위험한 골목은 막아요|bad alleys are blocked⟧", 13, "var(--ink)", cls="d")
         + crate(380, 110, 1.1, bug=True, opened=True) + person(430, 40, s=0.7, face=EYES, **GUARD)
         + '<path d="M355 100 l50 50 M405 100 l-50 50" stroke="var(--bad)" stroke-width="6" stroke-linecap="round"/>'
         + label(380, 230, "⟦벌레 든 상자는 압수|bug inside: confiscated⟧", 13, "var(--ink)", cls="d")
         + crate(620, 110, 1.1, sealed=True, opened=True)
         + label(620, 180, "⟦검문소만 열 수 있어요|only the checkpoint may open it⟧", 11, "var(--muted)")
         + label(620, 230, "⟦봉인도 뜯어봐요|even sealed boxes get opened⟧", 13, "var(--ink)", cls="d")
         + label(380, 275, "⟦봉인을 뜯는 건 성 사람들과 미리 약속해요|opening seals is agreed with the castle folk beforehand⟧", 12, "var(--muted)"))

# 5. 성문을 안 지나면 못 본다 → 검문소를 마을 곳곳에
HOUSE = ('<g transform="translate(80,150)"><rect x="-40" y="0" width="80" height="60" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
         '<path d="M-50 0 L0 -36 L50 0 Z" fill="var(--bad)"/><rect x="-10" y="26" width="20" height="34" fill="#8B5E3C"/>' + label(0, 80, "⟦집|home⟧", 12, "var(--muted)") + "</g>")
MINI = "".join(gatehouse(x, y, 0.4) + label(x, y + 52, "⟦검문소|checkpoint⟧", 9, "var(--good)") for x, y in ((470, 60), (600, 40), (700, 80), (560, 150)))
P5 = svg(300, sky(300) + HOUSE
         + '<path d="M120 240 C220 250 300 260 420 230" stroke="var(--bad)" stroke-width="10" fill="none" stroke-linecap="round" stroke-dasharray="14 10"/>'
         + person(230, 140, s=0.7, **ME)
         + gatehouse(330, 40, 0.6) + label(330, 130, "?", 26, "var(--accent)", cls="d")
         + building(500, 190, "⟦시장|market⟧", awning=True, s=0.6) + building(640, 200, "⟦극장|theater⟧", "var(--accent)", 0.6)
         + MINI + label(600, 270, "⟦요즘은 검문소를 마을 곳곳에 둬요|these days checkpoints sit all over town⟧", 12, "var(--good)")
         + label(200, 290, "⟦집에서 바로 마을로 가면요?|straight from home into town?⟧", 12, "var(--muted)"))

MAP_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="14" height="10" fill="var(--bad)"/><rect x="16" y="18" width="12" height="10" fill="var(--good)"/><path d="M10 26 h44 M28 12 v40" stroke="#C9A86A" stroke-width="2"/>')
BOX_I = icon('<rect x="12" y="20" width="40" height="34" rx="3" fill="#8B5E3C"/><path d="M12 20 L52 54 M52 20 L12 54" stroke="#5A3B22" stroke-width="3"/><ellipse cx="32" cy="34" rx="7" ry="5" fill="var(--bad)"/>')
SEAL_I = icon('<rect x="12" y="20" width="40" height="34" rx="3" fill="#8B5E3C"/><rect x="12" y="32" width="40" height="10" fill="#E9B44C"/><circle cx="32" cy="37" r="6" fill="var(--bad)"/><path d="M12 20 l40 -8" stroke="#8B5E3C" stroke-width="8"/>')
LEDGER_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF3D6" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="#C9A86A"/><rect x="22" y="30" width="16" height="3" fill="#C9A86A"/><rect x="22" y="40" width="18" height="3" fill="#C9A86A"/>')

PAGE = {
    "slug": "swg", "order": 23,
    "title": ("마을로 나가는 성문 검문소", "The Checkpoint to Town"),
    "h1": ("<em>SWG</em>가 뭐예요?", "What is an <em>SWG</em>?"),
    "sub": ("보안 웹 게이트웨이(Secure Web Gateway)를 바깥 마을로 나가는 성문 검문소 이야기로 풀어봤어요.",
            "Secure Web Gateway, told as a story about the checkpoint on the way out to town."),
    "panels": [
        {"svg": P1, "alt": ("성에서 길을 따라 시장, 도서관, 극장이 있는 바깥 마을로 걸어가는 사람들", "People walking from the castle along a road to a town with a market, a library and a theater"),
         "caption": ("성 사람들은 매일 바깥 마을에 나가요.", "Castle folk go out to town every day."),
         "small": ("시장, 도서관, 극장… 인터넷이에요.", "The market, the library, the theater… that's the internet.")},
        {"svg": P2, "alt": ("'공짜 선물!' 간판이 걸린 어두운 골목에 도둑이 있고, 한 사람이 벌레 든 상자를 들고 성으로 돌아감", "A thief in a dark alley under a FREE GIFTS! sign; someone carries a box with a bug in it back to the castle"),
         "caption": ("마을엔 위험한 골목도 있어요.", "Town has some bad alleys."),
         "small": ('"공짜 선물" 골목에서 받아온 상자에 벌레가 들어 있어요. 성에 들어오면 <a href="edr-ko.html">경비견</a>이 짖어야 해요.',
                   'The box from the "free gifts" alley has a bug inside. Once it\'s in, the <a href="edr-en.html">dog</a> has to catch it.')},
        {"svg": P3, "hero": True, "alt": ("성과 마을 사이 길 한가운데 검문소, 마을 지도를 든 경비, 상자를 든 사람이 지나감", "A checkpoint in the middle of the road between castle and town; a guard with a town map; a person with a box passing through"),
         "caption": ("SWG는 마을로 나가는 성문의 검문소예요.", "An SWG is the checkpoint on the road to town."),
         "small": ("나갈 때 어디 가는지 보고, 위험한 골목이면 막고, 들고 오는 상자를 열어봐요.", "It sees where you're going, blocks bad alleys, and opens the boxes you bring back."),
         "tricks": (4, [
             (MAP_I, ("마을 지도", "The town map"), ("골목마다 색이 칠해져 있어요", "every alley is color-coded"), "warm"),
             (BOX_I, ("상자 검사", "Box check"), ("벌레가 들었나", "any bugs inside")),
             (SEAL_I, ("봉인 뜯기", "Breaking seals"), ("검문소만 할 수 있어요", "only the checkpoint may"), "calm"),
             (LEDGER_I, ("대장", "The ledger"), ("누가 어디 갔는지", "who went where"), "calm"),
         ])},
        {"svg": P4, "alt": ("'도박 골목 — 막힘' 팻말, 벌레 든 상자에 X, 봉인이 뜯긴 상자", "A sign reading gambling alley — BLOCKED, a bug-filled box crossed out, and a box with its seal broken open"),
         "caption": ("위험한 골목은 막고, 상자는 열어봐요.", "Bad alleys are blocked; boxes get opened."),
         "small": ("봉해진 상자(암호화)도 검문소에선 열어봐요. 대신 그건 성 사람들과 미리 약속해요.", "Even sealed boxes (encryption) are opened at the checkpoint — but that's agreed with the castle folk beforehand.")},
        {"svg": P5, "alt": ("집에서 검문소를 거치지 않고 바로 마을로 가는 사람, 검문소엔 물음표. 마을 곳곳에 작은 검문소들", "Someone goes from home straight into town, skipping the checkpoint, which shows a question mark; small checkpoints dotted around town"),
         "caption": ("성문을 안 지나면 못 봐요.", "Skip the gate, and it sees nothing."),
         "small": ('집에서 바로 마을로 가면요? 그래서 요즘은 검문소를 마을 곳곳에 두고(클라우드), 어디서 나가든 거치게 해요. <a href="casb-ko.html">창고 문지기</a>와 같은 고민이에요.',
                   'Straight from home into town? So these days checkpoints sit all over town (in the cloud), and you pass one wherever you start. Same problem the <a href="casb-en.html">shed broker</a> has.')},
    ],
    "summary": (("<b>SWG</b> = 바깥 마을(인터넷)로 나가는 <b>성문 검문소</b>. 위험한 골목은 막고, 가져오는 상자는 열어보고, 어디 갔는지 적어요.",
                 "An <b>SWG</b> = the <b>checkpoint</b> on the road to town (the internet). It blocks bad alleys, opens the boxes you bring back, and writes down where you went."),
                ("Secure Web Gateway. 옛날엔 '웹 프록시'라고 불렀어요. 요즘은 창고 문지기(CASB), 문마다 묻는 성(ZTNA)과 함께 SSE라는 묶음으로 팔려요. Zscaler, Netskope, Cisco Umbrella 같은 것들.",
                 "Secure Web Gateway — what used to be called a web proxy. Today it's sold in an SSE bundle with the shed broker (CASB) and the castle that always asks (ZTNA): Zscaler, Netskope, Cisco Umbrella.")),
    "glossary": [
        ("웹 프록시", "Web proxy", ("검문소.", "The checkpoint."), ("내 대신 마을에 갔다 와요. 그래서 다 볼 수 있어요.", "Goes to town on my behalf — which is why it sees everything.")),
        ("URL 필터링", "URL filtering", ("마을 지도.", "The town map."), ("골목마다 색이 있어요: 도박 골목 빨강, 도서관 초록.", "Every alley has a color: gambling red, library green.")),
        ("평판", "Reputation", ("골목 소문.", "Alley gossip."), ('"저 골목에서 도둑맞은 사람이 많대요." → <a href="cti-ko.html">망루 위의 친구</a>가 알려줘요', '"Lots of people got robbed in that alley." → the <a href="cti-en.html">watchtower friend</a> passes it on')),
        ("멀웨어 검사", "Malware scanning", ("상자 열어보기.", "Opening the box."), ('벌레가 들었으면 성에 못 들어와요. 놓치면 <a href="edr-ko.html">경비견</a> 차례.', 'A bug inside means it never enters. Miss it, and it\'s the <a href="edr-en.html">dog</a>\'s turn.')),
        ("TLS 검사", "TLS inspection", ("봉인 뜯어보기.", "Breaking the seal."), ('봉해진 상자(암호화)를 검문소에서 열어요. <a href="ndr-ko.html">복도 파수꾼</a>은 못 하는 일.', 'Opening sealed (encrypted) boxes at the checkpoint — something the <a href="ndr-en.html">hallway watcher</a> can\'t do.')),
        ("샌드박스", "Sandbox", ("따로 방에서 열어보기.", "Opening it in a side room."), ("수상한 상자는 빈 방에서 먼저 열어요. 벌레가 튀어나와도 거기서 끝.", "Suspicious boxes get opened in an empty room first. If a bug jumps out, it ends there.")),
        ("클라우드 SWG", "Cloud SWG", ("마을 곳곳의 검문소.", "Checkpoints all over town."), ("성문 하나가 아니라 어디서 나가든 거치는 검문소.", "Not one gate, but a checkpoint wherever you start from.")),
        ("SSE", "SSE", ("검문소 묶음.", "The checkpoint bundle."), ('검문소(SWG) + <a href="casb-ko.html">창고 문지기</a>(CASB) + <a href="zerotrust-ko.html">문마다 묻는 성</a>(ZTNA).', 'Checkpoint (SWG) + <a href="casb-en.html">shed broker</a> (CASB) + <a href="zerotrust-en.html">castle that always asks</a> (ZTNA).')),
    ],
}
