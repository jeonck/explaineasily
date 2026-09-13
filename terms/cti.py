from _draw import *

LAPTOP = ('<rect x="20" y="20" width="120" height="76" rx="8" fill="var(--panel)" stroke="var(--line)"/>'
          '<rect x="32" y="30" width="96" height="50" rx="3" fill="var(--night)"/>'
          '<rect x="20" y="88" width="120" height="8" rx="4" fill="var(--stone-dark)"/>'
          + label(80, 62, "= 🏰", 20, "#FFFFFF"))

P1 = svg(300, sky(300) + castle() + LAPTOP)

LADDER = ('<path d="M52 56 L96 30 M60 68 L104 42" stroke="#C9A86A" stroke-width="6" stroke-linecap="round"/>'
          '<path d="M66 62 L58 62 M78 55 L70 55 M90 48 L82 48" stroke="#C9A86A" stroke-width="5"/>')
PIZZA = ('<rect x="46" y="66" width="60" height="18" rx="3" fill="#C9822B"/>'
         + label(76, 80, "⟦피자요?|PIZZA?⟧", 11, "#FFF"))
P2 = svg(240, night(240)
         + '<rect x="560" y="120" width="140" height="110" fill="#111C30"/>' + battlements(560, 105, 140, 4, "#111C30", 18)
         + person(110, 110, extra=LADDER)
         + person(300, 110, hat=None, face=MASK, extra=PIZZA)
         + f'<g transform="translate(450,120)"><ellipse cx="50" cy="90" rx="60" ry="34" fill="#173A2E"/>'
           f'<circle cx="50" cy="60" r="22" fill="{SKIN}"/><circle cx="42" cy="58" r="4" fill="#111C30"/><circle cx="58" cy="58" r="4" fill="#111C30"/></g>')

FLAME = ('<g class="flame"><path d="M485 100 C470 80 472 62 485 46 C488 62 496 66 498 56 C508 72 506 88 485 100 Z" fill="var(--accent)"/>'
         '<path d="M485 96 C478 86 480 76 485 68 C488 76 492 78 493 72 C498 82 496 90 485 96 Z" fill="#FFC875"/></g>')
SPYGLASS = ('<rect x="-36" y="30" width="48" height="12" rx="4" fill="var(--night)" transform="rotate(-18 -12 36)"/>'
            '<rect x="-60" y="26" width="30" height="16" rx="4" fill="var(--stone-dark)" transform="rotate(-18 -45 34)"/>')
P3 = svg(320, sky(320)
         + '<rect x="40" y="230" width="60" height="50" fill="var(--stone)"/><path d="M36 232 L70 205 L104 232 Z" fill="var(--stone-dark)"/>'
         + '<rect x="130" y="240" width="50" height="40" fill="var(--stone)"/><path d="M126 242 L155 220 L184 242 Z" fill="var(--stone-dark)"/>'
         + f'<circle cx="110" cy="270" r="8" fill="{SKIN}"/><path d="M102 266 Q110 254 118 266 Z" fill="var(--bad)"/>'
         + '<rect x="430" y="120" width="110" height="200" fill="var(--stone-dark)"/><rect x="418" y="104" width="134" height="26" fill="var(--stone)"/>'
         + battlements(418, 88, 134, 4, "var(--stone)", 18) + FLAME
         + person(560, 20, hat="var(--good)", shirt="var(--good)", face=SMILE, extra=SPYGLASS)
         + '<path d="M520 52 L120 262" stroke="var(--accent)" stroke-width="3" stroke-dasharray="8 8" fill="none"/>')

P4 = svg(170, '<rect width="760" height="170" fill="var(--accent-soft)"/>'
         + f'<g transform="translate(60,30)"><circle cx="40" cy="40" r="32" fill="{SKIN}"/><path d="M8 34 Q40 -4 72 34 Z" fill="var(--good)"/>'
           '<ellipse cx="40" cy="54" rx="9" ry="12" fill="var(--night)"/><circle cx="28" cy="36" r="4" fill="var(--night)"/><circle cx="52" cy="36" r="4" fill="var(--night)"/></g>'
         + '<g transform="translate(150,40)"><path d="M0 40 h40 l40 -30 v60 l-40 -30 z" fill="var(--accent)"/>'
           '<path d="M100 25 a30 30 0 0 1 0 30 M116 12 a48 48 0 0 1 0 56" stroke="var(--accent)" stroke-width="6" fill="none" stroke-linecap="round"/></g>'
         + label(470, 98, "⟦조심해!|HEADS UP!⟧", 50, "var(--accent)", cls="d"))

P5 = svg(260, '<rect width="760" height="260" fill="var(--good-soft)"/>'
         + '<rect x="230" y="100" width="300" height="160" fill="var(--stone-dark)"/>' + battlements(230, 80, 300, 5, "var(--stone-dark)")
         + shield(290, 40)
         + person(600, 150, extra=label(60, 20, "⟦에이, 망했다|aw, nuts⟧", 18, "var(--bad)", "start")))

WINDOW = icon('<rect x="12" y="10" width="40" height="44" rx="4" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><path d="M12 32 h40 M32 10 v44" stroke="var(--bad)" stroke-width="3"/>')
PIZZA_I = icon('<path d="M32 8 L58 56 H6 Z" fill="#E9B44C"/><circle cx="26" cy="40" r="4" fill="var(--bad)"/><circle cx="38" cy="34" r="4" fill="var(--bad)"/><circle cx="32" cy="50" r="4" fill="var(--bad)"/>')
MOON = icon('<path d="M40 8 a24 24 0 1 0 16 40 a20 20 0 0 1 -16 -40 z" fill="var(--bad)"/>')

PAGE = {
    "slug": "cti", "order": 1,
    "title": ("망루 위의 친구", "The Watchtower Friend"),
    "h1": ("<em>CTI</em>가 뭐예요?", "What is <em>CTI</em>?"),
    "sub": ("사이버 위협 인텔리전스를 성과 망루 위의 친구 이야기로 풀어봤어요.",
            "Cyber Threat Intelligence, told as a story about a castle and a friend on a tower."),
    "panels": [
        {"svg": P1, "alt": ("파란 하늘 아래 깃발이 꽂힌 성", "A castle with a flag under a blue sky"),
         "caption": ("내 컴퓨터는 성이에요.", "Your computer is a castle."),
         "small": ("소중한 것들이 들어 있어요. 지켜야 해요.", "It holds your stuff. You want to keep it safe.")},
        {"svg": P2, "alt": ("밤에 성으로 다가오는 수상한 사람 셋", "Three sneaky figures approaching a castle at night"),
         "caption": ("수상한 사람들이 들어오려 해요.", "Sneaky people want to get in."),
         "small": ("저마다 좋아하는 수법이 있어요.", "Each one has a favorite trick."),
         "tricks": (3, [
             (WINDOW, ("창문으로 기어올라요", "Climbs in windows"), ("빨간 모자 아저씨", "the red-hat one")),
             (PIZZA_I, ("피자 배달인 척해요", "Pretends to be pizza"), ("문을 열게 하려고", "so you open the door")),
             (MOON, ("깜깜할 때 와요", "Comes after dark"), ("아무도 안 볼 때", "when nobody's looking")),
         ])},
        {"svg": P3, "hero": True, "alt": ("높은 망루에서 망원경을 든 친구와 봉화", "A friend on a tall watchtower with a spyglass and a beacon fire"),
         "caption": ("CTI는 망루 위의 친구예요.", "CTI is a friend on the watchtower."),
         "small": ("마을 전체를 지켜보며 나쁜 사람들이 뭘 하는지 알아내요.", "They watch the whole town and learn what the sneaky people are doing.")},
        {"svg": P4, "alt": ("망루에서 외치는 친구", "The friend shouting down from the tower"),
         "caption": ("친구가 수법을 미리 알려줘요.", "The friend tells you the tricks."),
         "small": ("누가 문을 두드리기 전에요.", "Before anyone knocks."),
         "bubbles": [
             (("🧢 빨간 모자가 이번 주 세 집을 털었대", "🧢 Red hat robbed 3 houses this week"), ("창문 잠그기", "lock the windows")),
             (("🍕 가짜 피자 배달이 돌고 있대", "🍕 Fake pizza is going around"), ("시킨 적 없는 피자엔 문 열지 않기", "don't open for pizza you didn't order")),
             (("🌙 밤에 온대", "🌙 They come at night"), ("자기 전에 문 확인하기", "check the doors at bedtime")),
         ]},
        {"svg": P5, "alt": ("성 앞의 자물쇠가 달린 큰 초록 방패", "A big green shield with a lock in front of the castle"),
         "caption": ("그래서 두드리기 전에 잠가요.", "So you lock up before they knock."),
         "small": ("이미 아는 수법은 막기 쉬워요.", "It's easy to stop a trick you already know.")},
    ],
    "summary": (("<b>CTI</b> = 나쁜 사람들의 수법을 당하기 <b>전에</b> 미리 아는 것.",
                 "<b>CTI</b> = knowing the bad guys' tricks <b>before</b> they try them on you."),
                ("사이버 위협 인텔리전스는 사고가 난 뒤에 알게 되는 게 아니라, 착한 편이 먼저 준비할 수 있게 해주는 \"조심해!\"예요.",
                 "Cyber Threat Intelligence is the \"heads up!\" that lets the good guys get ready first, instead of finding out after something breaks.")),
    "glossary": [
        ("위협 행위자", "Threat actor", ("나쁜 사람.", "The sneaky person."), ("해커, 범죄 조직, 어떤 나라의 스파이.", "A hacker, a gang, or a country's spies.")),
        ("공격 수법", "TTPs", ("즐겨 쓰는 수법.", "Their favorite tricks."), ('보통 어떻게 들어오고, 들어와서 뭘 하는지. → <a href="ttp-ko.html">버릇 이야기</a>', 'How they usually get in and what they do next. → <a href="ttp-en.html">the habit story</a>')),
        ("침해 지표", "IOC", ("발자국.", "A footprint."), ('"빨간 모자" 같은 단서 — 나쁜 사람이 늘 쓰는 주소나 파일. → <a href="ioc-ko.html">발자국 이야기</a>', 'A clue like "the red hat" — an address or a file the bad guy always uses. → <a href="ioc-en.html">the footprint story</a>')),
        ("위협 피드", "Threat feed", ("친구의 외침.", "The friend's shouting."), ("하루 종일 흘러오는 새 경고들.", "A stream of new warnings, all day long.")),
        ("위협 보고서", "Threat report", ("친구의 이야기책.", "The friend's storybook."), ("한 조직이 저지른 일을 처음부터 끝까지 적은 것.", "The full tale of one gang and everything they did.")),
    ],
}
