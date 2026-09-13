from _draw import *

USHER = dict(hat="var(--accent)", shirt="var(--accent)")
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
NOTE = '<rect x="48" y="66" width="26" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="53" y="74" width="16" height="3" fill="#C9A86A"/><rect x="53" y="82" width="12" height="3" fill="#C9A86A"/>'
HATS = (None, "#E9B44C", "var(--stone-dark)", None, "#E9B44C", "var(--good)", None, "var(--stone-dark)")


def counters(n, closed=(), x0=470, y=80, gap=100, faces=None):
    out = ""
    for i in range(n):
        x = x0 + i * gap
        if i in closed:
            out += (f'<rect x="{x}" y="{y}" width="70" height="70" rx="6" fill="var(--stone)"/><path d="M{x + 10} {y + 10} l50 50 M{x + 60} {y + 10} l-50 50" stroke="var(--bad)" stroke-width="4"/>'
                    + label(x + 35, y + 92, "⟦닫힘|closed⟧", 11, "var(--bad)"))
        else:
            f = faces[i] if faces else SMILE
            out += (f'<rect x="{x}" y="{y}" width="70" height="70" rx="6" fill="var(--sky)"/>' + person(x + 12, y - 8, s=0.55, face=f, **CLERK)
                    + label(x + 35, y + 92, f"⟦창구 {i + 1}|counter {i + 1}⟧", 11, "#C9D5E6"))
    return out


def wall(x=380):
    return f'<rect x="{x}" y="40" width="{760 - x}" height="260" fill="var(--stone-dark)"/>' + battlements(x, 22, 760 - x, 8, "var(--stone-dark)", 20)


def queue(xs, y=150, s=0.6, faces=None):
    return "".join(person(x, y, s=s, hat=HATS[i % len(HATS)], shirt="#4A5A72", face=(faces[i % len(faces)] if faces else SMILE), extra=NOTE) for i, x in enumerate(xs))


# 1. 창구가 하나면 줄이 길다
P1 = svg(300, sky(300) + wall(560) + counters(1, x0=610, y=90)
         + queue(range(20, 520, 62), 160, 0.6, faces=[FROWN] * 8)
         + '<g transform="translate(680,230)"><circle r="22" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M0 -14 V0 L9 6" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
         + label(380, 285, "⟦마을 사람이 많아지면 창구 직원 한 명이 못 받아요|as the town grows, one clerk can\'t keep up⟧", 13, "var(--muted)"))

# 2. 창구를 늘려도 한 줄에만 선다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + wall(440) + counters(3, x0=470, y=90, gap=95)
         + queue((30, 95, 160, 225, 290, 355), 130, 0.6, faces=[FROWN] * 6)
         + '<path d="M410 190 L470 130" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/>'
         + label(660, 250, "⟦비어 있어요|empty⟧", 12, "#C9D5E6") + label(560, 250, "⟦비어 있어요|empty⟧", 12, "#C9D5E6")
         + label(220, 275, "⟦어느 창구가 비었는지 아무도 몰라요|nobody knows which counter is free⟧", 13, "var(--muted)"))

# 3. 로드 밸런서 = 줄 안내원 (hero)
BOARD = ('<g transform="translate(60,-20)"><rect width="96" height="70" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
         + "".join(label(10, 20 + i * 18, t, 11, "var(--ink)", "start") for i, t in enumerate(("⟦창구 1 ●●|counter 1 ●●⟧", "⟦창구 2 ●|counter 2 ●⟧", "⟦창구 3 ○|counter 3 ○⟧"))) + "</g>")
P3 = svg(340, sky(340) + wall(440) + counters(3, x0=470, y=90, gap=95)
         + queue((20, 85, 150), 170, 0.6)
         + person(280, 110, s=0.95, face=SMILE, **USHER, extra=BOARD) + label(310, 260, "⟦줄 안내원|the usher⟧", 13, "var(--ink)", cls="d")
         + '<path d="M350 170 C400 170 430 130 470 125 M350 175 C420 175 500 135 565 125 M350 180 C440 190 580 140 660 125" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>'
         + bubble(240, 30, 150, 34, "⟦이쪽으로 오세요|this way, please⟧", 13, "var(--panel)", "var(--accent)", "bottom")
         + label(380, 322, "⟦한가한 창구로 나눠 보내요. 마을은 창구가 몇 개인지 몰라도 돼요|spreads people to free counters; the town needn\'t know how many there are⟧", 12, "var(--muted)"))

# 4. 창구 하나가 닫혀도 아무도 모른다
P4 = svg(300, sky(300) + wall(440) + counters(3, closed=(1,), x0=470, y=90, gap=95)
         + queue((20, 85, 150), 150, 0.6)
         + person(280, 100, s=0.9, face=EYES, **USHER)
         + '<path d="M350 160 C400 160 430 130 470 125 M350 170 C440 190 580 140 660 125" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>'
         + '<path d="M350 165 C420 170 500 150 560 130" stroke="var(--bad)" stroke-width="2" stroke-dasharray="3 6" fill="none"/><path d="M540 118 l16 16 M556 118 l-16 16" stroke="var(--bad)" stroke-width="3"/>'
         + label(380, 282, "⟦안내원이 문 닫힌 창구엔 안 보내요|the usher never sends anyone to a closed counter⟧", 13, "var(--muted)"))

# 5. 안내원이 쓰러지면 다 멈춘다 / 장부가 다르다
P5 = svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--accent-soft)"/>'
         + f'<g transform="translate(120,190) rotate(-80)">{person(0, 0, s=0.8, face=FROWN + SWEAT, **USHER)}</g>'
         + queue((20, 80, 140, 200), 60, 0.55, faces=[FROWN] * 4)
         + label(190, 275, "⟦안내원이 쓰러지면 줄이 멈춰요|the usher collapses and the line stops⟧", 13, "var(--bad)")
         + label(190, 300, "⟦그래서 안내원도 둘 둬요|so there are two ushers⟧", 12, "var(--muted)")
         + '<rect x="420" y="60" width="70" height="70" rx="6" fill="var(--sky)"/>' + person(432, 52, s=0.55, face=EYES, **CLERK) + label(455, 150, "⟦창구 3|counter 3⟧", 11, "var(--muted)")
         + person(540, 90, s=0.8, hat="#E9B44C", shirt="#4A5A72", face=FROWN)
         + bubble(500, 14, 240, 34, "⟦아까 창구 1에서 얘기했는데요?|I told counter 1 all this already?⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(570, 275, "⟦창구마다 장부가 다르면 못 알아들어요|different ledgers, and counters don\'t remember you⟧", 12, "var(--bad)")
         + label(570, 300, "⟦장부를 한 곳에 두거나, 같은 창구로 보내요|share one ledger, or send you back to the same counter⟧", 11, "var(--muted)"))

SPLIT_I = icon('<circle cx="14" cy="32" r="6" fill="var(--accent)"/><path d="M20 32 L44 14 M20 32 L44 32 M20 32 L44 50" stroke="var(--accent)" stroke-width="3"/><rect x="44" y="8" width="12" height="12" fill="var(--sky)"/><rect x="44" y="26" width="12" height="12" fill="var(--sky)"/><rect x="44" y="44" width="12" height="12" fill="var(--sky)"/>')
HEALTH_I = icon('<rect x="12" y="12" width="40" height="40" rx="6" fill="var(--sky)"/><path d="M22 34 l7 7 l14 -16" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
STICKY_I = icon('<rect x="30" y="12" width="26" height="26" rx="4" fill="var(--sky)"/><circle cx="16" cy="44" r="7" fill="var(--good)"/><path d="M22 40 C30 30 32 30 34 26" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M28 30 l6 -4 -2 7" fill="var(--good)"/>')
SCALE_I = icon('<rect x="8" y="30" width="14" height="14" fill="var(--sky)"/><rect x="25" y="30" width="14" height="14" fill="var(--sky)"/><rect x="42" y="30" width="14" height="14" fill="var(--sky)" stroke="var(--accent)" stroke-width="2" stroke-dasharray="3 2"/><path d="M49 18 v8 M45 22 h8" stroke="var(--accent)" stroke-width="3"/>')

PAGE = {
    "slug": "loadbalancer", "order": 32,
    "title": ("줄 안내원", "The Queue Usher"),
    "h1": ("<em>로드 밸런서</em>가 뭐예요?", "What is a <em>Load Balancer</em>?"),
    "sub": ("로드 밸런서(Load Balancer)를 창구 앞 줄 안내원 이야기로 풀어봤어요.",
            "Load balancers, told as a story about the usher in front of the counters."),
    "panels": [
        {"svg": P1, "alt": ("창구 하나 앞에 찡그린 사람 여덟 명이 긴 줄을 섰고 시계가 있음", "Eight frowning people queue at a single counter; a clock sits beside it"),
         "caption": ("창구가 하나면 줄이 길어져요.", "One counter, one long line."),
         "small": ('마을 사람이 많아지면 <a href="waf-ko.html">창구</a> 직원 한 명이 못 받아요.', 'As the town grows, one <a href="waf-en.html">counter</a> clerk can\'t keep up.')},
        {"svg": P2, "alt": ("창구가 셋인데 모두 창구 1에만 줄을 섰고, 창구 2와 3은 비어 있음", "Three counters, but everyone queues at counter 1 while 2 and 3 sit empty"),
         "caption": ("창구를 늘려도 다들 한 줄에만 서요.", "Add counters, and people still crowd one line."),
         "small": ("어느 창구가 비었는지 아무도 몰라요.", "Nobody knows which counter is free.")},
        {"svg": P3, "hero": True, "alt": ("주황 모자 안내원이 '이쪽으로 오세요' 하며 창구 셋의 줄 길이가 적힌 판을 들고 사람들을 나눠 보냄", "An usher in an orange hat says this way, please, holding a board with each counter's line length, and spreads people out"),
         "caption": ("로드 밸런서는 줄 안내원이에요.", "A load balancer is the queue usher."),
         "small": ("'이쪽으로 오세요.' 한가한 창구로 나눠 보내요. 마을 사람은 창구가 몇 개인지 몰라도 돼요.", "'This way, please.' It spreads people to free counters — and the town never needs to know how many there are."),
         "tricks": (4, [
             (SPLIT_I, ("나눠 보내기", "Spreading"), ("차례대로, 또는 제일 짧은 줄로", "in turn, or to the shortest line"), "warm"),
             (HEALTH_I, ("열린 창구 확인", "Open-counter check"), ("매 분 문을 두드려 봐요", "knocks on every door each minute"), "calm"),
             (STICKY_I, ("같은 창구로 다시", "Same counter again"), ("아까 그 직원에게", "back to the clerk you had")),
             (SCALE_I, ("창구 늘리기", "More counters"), ("바쁘면 하나 더 열어요", "busy? open another"), "calm"),
         ])},
        {"svg": P4, "alt": ("창구 2에 닫힘 표시, 안내원이 창구 1과 3으로만 보내고 창구 2 쪽 점선엔 X", "Counter 2 is marked closed; the usher routes only to 1 and 3, with an X on the line toward 2"),
         "caption": ("창구 하나가 닫혀도 아무도 몰라요.", "One counter closes and nobody notices."),
         "small": ("안내원이 문 닫힌 창구엔 안 보내요. 고치는 동안 다른 창구가 받아요.", "The usher never sends anyone to a closed counter. The others cover while it's fixed.")},
        {"svg": P5, "alt": ("왼쪽: 안내원이 쓰러져 줄이 멈춤. 오른쪽: 창구 3 앞 손님이 '아까 창구 1에서 얘기했는데요?'", "Left: the usher has collapsed and the line is stuck. Right: a customer at counter 3 says I told counter 1 all this already?"),
         "caption": ("안내원이 쓰러지면 다 멈춰요.", "If the usher collapses, everything stops."),
         "small": ("그래서 안내원도 둘 둬요. 그리고 창구마다 장부가 다르면 '아까 그 얘기'를 못 알아들어요 — 장부를 한 곳에 두거나, 같은 창구로 보내요.", "So there are two ushers. And if each counter keeps its own ledger, nobody remembers what you said — so they share one ledger, or send you back to the same counter.")},
    ],
    "summary": (("<b>로드 밸런서</b> = 마을 사람들을 <b>한가한 창구</b>로 나눠 보내는 줄 안내원. 닫힌 창구엔 안 보내고, 창구가 몇 개인지 마을은 몰라요.",
                 "A <b>load balancer</b> = the usher who sends people to whichever <b>counter is free</b>, skips closed ones, and never lets the town see how many counters there are."),
                ("Load Balancer. 접수원(리버스 프록시)이 하는 일 중 하나예요. 겉봉만 보고 나누면 L4, 쪽지를 읽고 나누면 L7. nginx, HAProxy, AWS ALB/NLB 같은 것들.",
                 "One of the receptionist's (reverse proxy's) jobs. Sorting by the envelope alone is L4; reading the note first is L7. nginx, HAProxy, AWS ALB/NLB.")),
    "glossary": [
        ("라운드 로빈", "Round robin", ("차례대로 한 명씩.", "One each, in turn."), ("1, 2, 3, 1, 2, 3… 제일 단순한 나누기.", "1, 2, 3, 1, 2, 3… the simplest way to spread.")),
        ("최소 연결", "Least connections", ("제일 짧은 줄로.", "To the shortest line."), ("지금 손님이 제일 적은 창구로.", "Whichever counter has the fewest people right now.")),
        ("헬스 체크", "Health check", ("창구 문 두드려 보기.", "Knocking on the counter door."), ("대답 없는 창구엔 안 보내요.", "No answer, no customers sent.")),
        ("스티키 세션", "Sticky session", ("아까 그 창구로.", "Back to the same counter."), ("장부가 창구마다 따로일 때 쓰는 방법.", "The fix when each counter keeps its own ledger.")),
        ("오토스케일", "Autoscaling", ("창구 더 열기.", "Opening more counters."), ("줄이 길어지면 창구를 늘리고, 한가하면 닫아요.", "Long lines open counters; quiet hours close them.")),
        ("L4 · L7", "L4 · L7", ("겉봉만 vs 쪽지 읽고.", "Envelope only vs. reading the note."), ('L4는 주소만 보고 나누고, L7은 쪽지 내용을 보고 나눠요. → <a href="proxy-ko.html">접수원 이야기</a>', 'L4 sorts by address alone; L7 reads the note first. → <a href="proxy-en.html">the receptionist story</a>')),
        ("단일 장애점", "Single point of failure", ("안내원 하나.", "One usher."), ("쓰러지면 다 멈춰요. 그래서 둘 둬요.", "Collapses, and everything stops — hence two.")),
        ("공유 세션 저장소", "Shared session store", ("창구들이 같이 보는 장부.", "The ledger all counters share."), ("어느 창구로 가도 '아까 그 얘기'를 알아요.", "Whichever counter you reach, it remembers you.")),
    ],
}
