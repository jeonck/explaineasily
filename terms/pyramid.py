from _draw import *

LAYERS = (  # 아래부터 위로. (라벨, 색)  — David Bianco, 2013
    ("⟦해시|Hash⟧", "#5B8DEF"),
    ("⟦IP 주소|IP address⟧", "#5FAFC4"),
    ("⟦도메인|Domain⟧", "#7FBF6A"),
    ("⟦흔적|Artifacts⟧", "#E0B14A"),
    ("⟦도구|Tools⟧", "#EE7F3A"),
    ("TTP", "#D9362B"),
)


def pyramid(cx, y, w, h, colored=6):
    """밑변 w, 높이 h, 꼭대기 폭은 밑변의 15%. colored 개수만 색을 칠하고 나머진 회색."""
    n = len(LAYERS)
    lh = h / n
    out = ""
    for i, (name, color) in enumerate(LAYERS):
        b = 1 - 0.85 * (i / n)
        t = 1 - 0.85 * ((i + 1) / n)
        yb, yt = y + h - i * lh, y + h - (i + 1) * lh
        fill = color if i < colored else "var(--stone)"
        out += (f'<path d="M{cx - w * b / 2:.0f} {yb:.0f} L{cx + w * b / 2:.0f} {yb:.0f} '
                f'L{cx + w * t / 2:.0f} {yt:.0f} L{cx - w * t / 2:.0f} {yt:.0f} Z" fill="{fill}" stroke="var(--panel)" stroke-width="3"/>'
                + label(cx, (yb + yt) / 2 + 6, name, 16, "#FFF"))
    return out


FACE_OK = f'<circle r="22" fill="{SKIN}"/><circle cx="-8" cy="-4" r="3" fill="var(--night)"/><circle cx="8" cy="-4" r="3" fill="var(--night)"/><path d="M-10 6 Q0 14 10 6" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/>'
FACE_HURT = f'<circle r="22" fill="{SKIN}"/><path d="M-12 -8 l8 6 M-4 -8 l-8 6 M4 -8 l8 6 M12 -8 l-8 6" stroke="var(--night)" stroke-width="3" stroke-linecap="round"/><path d="M-10 12 Q0 2 10 12" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/>'
P1 = svg(340, '<rect width="760" height="340" fill="var(--panel)"/>' + pyramid(330, 30, 520, 280)
         + f'<g transform="translate(680,60)">{FACE_HURT}</g>' + label(680, 110, "⟦아파요|hurts⟧", 16, "var(--bad)")
         + f'<g transform="translate(680,250)">{FACE_OK}</g>' + label(680, 300, "⟦안 아파요|doesn't hurt⟧", 16, "var(--good)")
         + '<path d="M680 130 V218" stroke="var(--muted)" stroke-width="3" stroke-dasharray="6 6"/><path d="M672 142 L680 130 L688 142" stroke="var(--muted)" stroke-width="3" fill="none"/>')

SHOE = '<path d="M0 0 h50 a18 18 0 0 1 18 18 v8 h-80 v-14 a12 12 0 0 1 12 -12z" fill="var(--bad)"/>'
BLOCK_LOW = '<rect x="40" y="90" width="260" height="60" rx="10" fill="#5B8DEF"/>' + label(170, 127, "⟦해시 · IP 막음|hash · IP blocked⟧", 18, "#FFF")
P2 = svg(240, '<rect width="760" height="240" fill="var(--good-soft)"/>' + BLOCK_LOW + shield(290, 50, 0.5)
         + person(480, 80, face=SMILE, extra=f'<g transform="translate(70,40)">{SHOE}</g>')
         + bubble(400, 14, 320, 44, "⟦새 신발 사면 되지 뭐|I'll just buy new shoes⟧", 17, "var(--panel)", "var(--line)", "bottom")
         + label(660, 200, "⟦1초|1 sec⟧", 28, "var(--good)", cls="d"))

BLOCK_HIGH = '<rect x="40" y="90" width="260" height="60" rx="10" fill="#D9362B"/>' + label(170, 127, "⟦버릇(TTP) 막음|habit (TTP) blocked⟧", 18, "#FFF")
NOTEBOOK = ('<g transform="translate(66,44)"><rect width="56" height="70" rx="4" fill="var(--panel)" stroke="var(--night)" stroke-width="3"/>'
            + "".join(f'<rect x="8" y="{y}" width="40" height="4" fill="var(--line)"/>' for y in (12, 24, 36, 48)) + "</g>")
P3 = svg(260, '<rect width="760" height="260" fill="var(--bad-soft)"/>' + BLOCK_HIGH + shield(290, 50, 0.5)
         + person(480, 90, face=FROWN, extra=SWEAT + NOTEBOOK)
         + bubble(380, 14, 360, 44, "⟦일하는 법을 전부 다시 짜야 해…|I have to redo how I work… all of it⟧", 16, "var(--panel)", "var(--bad)", "bottom")
         + label(660, 230, "⟦몇 달|months⟧", 28, "var(--bad)", cls="d"))

P4 = svg(340, '<rect width="760" height="340" fill="var(--panel)"/>' + pyramid(330, 30, 520, 280, colored=2)
         + bubble(560, 220, 190, 44, "⟦대부분 여기서 멈춰요|most stop here⟧", 15, "var(--accent-soft)", "var(--accent)", "left")
         + bubble(540, 40, 210, 44, "⟦진짜 방어는 여기|the real defense is here⟧", 15, "var(--accent-soft)", "var(--accent)", "left")
         + '<path d="M600 210 L600 100" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 6"/><path d="M590 112 L600 98 L610 112" stroke="var(--accent)" stroke-width="3" fill="none"/>')

PAGE = {
    "slug": "pyramid", "order": 5,
    "title": ("고통의 피라미드", "The Pyramid of Pain"),
    "h1": ("<em>고통의 피라미드</em>가 뭐예요?", "What is the <em>Pyramid of Pain</em>?"),
    "sub": ("막았을 때 나쁜 사람이 얼마나 아픈지를 층으로 그린 그림이에요.",
            "A picture of how much each kind of blocking hurts the bad guy."),
    "panels": [
        {"svg": P1, "hero": True, "alt": ("여섯 층 피라미드, 아래는 파랑 위는 빨강, 옆에 웃는 얼굴과 아픈 얼굴", "A six-layer pyramid, blue at the bottom and red at the top, with a happy and a hurt face beside it"),
         "caption": ("막을 수 있는 건 여섯 층이에요.", "There are six things you can block."),
         "small": ("위로 갈수록 나쁜 사람이 더 아파요.", "The higher you go, the more it hurts the bad guy.")},
        {"svg": P2, "alt": ("아래층을 막은 방패와 새 신발을 든 나쁜 사람", "A shield on the bottom layer and a bad guy holding new shoes"),
         "caption": ("아래층을 막으면?", "Block the bottom?"),
         "small": ('"새 신발 사면 되지." 1초. <a href="ioc-ko.html">발자국 이야기</a>와 같아요.',
                   '"I\'ll just buy new shoes." One second. Same as the <a href="ioc-en.html">footprint story</a>.')},
        {"svg": P3, "alt": ("위층을 막은 방패와 땀 흘리며 공책을 든 나쁜 사람", "A shield on the top layer and a sweating bad guy with a notebook"),
         "caption": ("위층을 막으면?", "Block the top?"),
         "small": ('<a href="ttp-ko.html">버릇</a>을 통째로 바꿔야 해요. 몇 달.',
                   'They have to change their whole <a href="ttp-en.html">habit</a>. Months.')},
        {"svg": P4, "alt": ("아래 두 층만 칠해진 피라미드와 위로 향한 화살표", "The pyramid with only the bottom two layers colored and an arrow pointing up"),
         "caption": ("대부분은 아래 두 칸만 해요.", "Most people only do the bottom two."),
         "small": ("그래서 '해봤는데 소용없다'는 말이 나와요.", "That's why you hear \"we tried it and it didn't help.\"")},
    ],
    "summary": (("위로 갈수록 막기 <b>어렵지만</b>, 나쁜 사람은 더 <b>아파요</b>.",
                 "Higher up is <b>harder</b> to block, but it <b>hurts</b> the bad guy more."),
                ("David Bianco가 2013년에 그린 그림. 방어 노력을 어디에 쓸지 정하는 기준이에요.",
                 "Drawn by David Bianco in 2013. It's the yardstick for where to spend your defense effort.")),
    "glossary": [
        ("해시", "Hash values", ("1초.", "One second."), ("파일에 한 글자만 더해도 바뀌어요.", "Add one byte to the file and it changes.")),
        ("IP 주소", "IP addresses", ("10분.", "Ten minutes."), ("서버를 새로 빌리면 돼요.", "Rent a new server.")),
        ("도메인", "Domain names", ("몇 시간.", "Hours."), ("새로 사면 돼요.", "Buy a new one.")),
        ("흔적", "Network / host artifacts", ("며칠.", "Days."), ("설정과 도구 자국을 고쳐야 해요.", "Fix the settings and marks the tools leave.")),
        ("도구", "Tools", ("몇 주.", "Weeks."), ("새 도구를 만들거나 배워야 해요.", "Build or learn a new tool.")),
        ("버릇", "TTPs", ("몇 달.", "Months."), ('일하는 방식 자체를 다시 짜야 해요. → <a href="ttp-ko.html">버릇 이야기</a>', 'Rewrite how they work. → <a href="ttp-en.html">the habit story</a>')),
    ],
}
