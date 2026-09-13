from _draw import *

ME = dict(hat=None, shirt="#4A5A72", face=SMILE)
RUNNER = dict(hat="var(--accent)", shirt="var(--accent)")
CLERK = dict(hat="#5B8DEF", shirt="#4A5A72")
NOTE = '<rect x="48" y="66" width="26" height="32" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><rect x="53" y="74" width="16" height="3" fill="#C9A86A"/><rect x="53" y="82" width="12" height="3" fill="#C9A86A"/>'
BASKET = '<g transform="translate(66,90)"><path d="M-18 -4 h36 l-5 22 h-26z" fill="#C9A86A"/><path d="M-12 -4 a12 12 0 0 1 24 0" stroke="#8B5E3C" stroke-width="3" fill="none"/><circle cx="-6" cy="-6" r="5" fill="var(--bad)"/><circle cx="6" cy="-7" r="5" fill="var(--good)"/></g>'


def market(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="0" width="100" height="64" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-58 0 h116 l-8 -22 h-100 z" fill="var(--accent)"/>' + "".join(f'<rect x="{-58 + i * 20}" y="-22" width="10" height="22" fill="#FFD9B8"/>' for i in range(6))
            + f'<rect x="-40" y="24" width="80" height="12" fill="#C9A86A"/>' + "".join(f'<circle cx="{-30 + i * 15}" cy="20" r="6" fill="{c}"/>' for i, c in enumerate(("var(--bad)", "var(--good)", "#E9B44C", "var(--bad)", "var(--good)")))
            + f'{label(0, 84, "⟦시장|market⟧", 12, "var(--muted)")}</g>')


EYE = '<path d="M-14 0 Q0 -10 14 0 Q0 10 -14 0 Z" fill="#FFF" stroke="var(--night)" stroke-width="2"/><circle r="4" fill="var(--night)"/>'

# 1. 직접 가면 얼굴이 다 보인다
P1 = svg(300, sky(300) + castle(10, 90, 0.4) + market(600, 120)
         + '<path d="M200 230 C300 230 450 220 540 210" stroke="var(--stone-dark)" stroke-width="8" fill="none" stroke-linecap="round"/>'
         + person(380, 120, s=0.85, **ME, extra=NOTE)
         + person(560, 60, s=0.6, hat="#E9B44C", shirt="#4A5A72", face=EYES) + f'<g transform="translate(560,140)">{EYE}</g>'
         + bubble(520, 10, 200, 34, "⟦지민이가 사과 두 개 샀네|Jimin bought two apples⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦누가 뭘 샀는지 시장 사람들이 다 알아요|the whole market knows who bought what⟧", 13, "var(--muted)"))

# 2. 심부름꾼에게 부탁하면
P2 = svg(300, sky(300) + castle(10, 90, 0.4) + market(600, 120)
         + person(150, 130, s=0.8, **ME) + '<path d="M210 180 L250 180" stroke="var(--accent)" stroke-width="3"/><path d="M240 170 L252 180 L240 190" stroke="var(--accent)" stroke-width="3" fill="none"/>'
         + person(270, 120, s=0.85, face=SMILE, **RUNNER, extra=NOTE) + label(300, 250, "⟦심부름꾼|the runner⟧", 12, "var(--ink)", cls="d")
         + '<path d="M350 200 C420 200 480 210 540 210" stroke="var(--stone-dark)" stroke-width="8" fill="none" stroke-linecap="round" stroke-dasharray="12 8"/>'
         + person(560, 60, s=0.6, hat="#E9B44C", shirt="#4A5A72", face=EYES)
         + bubble(500, 10, 220, 34, "⟦주황 모자가 사과 두 개 샀네|orange hat bought two apples⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦시장은 심부름꾼 얼굴만 봐요. 내 얼굴은 성 밖으로 안 나가요|the market sees only the runner; my face never leaves the castle⟧", 12, "var(--muted)"))

# 3. 프록시 = 대신 다녀오는 심부름꾼 (hero)
CROWD = "".join(person(30 + i * 60, 110 + (i % 2) * 40, s=0.55, hat=h, shirt="#4A5A72", face=SMILE, extra=NOTE) for i, h in enumerate((None, "#E9B44C", "#5B8DEF", None)))
ALLEYS = ('<g transform="translate(400,40)"><rect width="110" height="56" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>'
          + label(55, 20, "⟦가면 안 되는 골목|alleys to avoid⟧", 10, "var(--bad)") + '<rect x="12" y="30" width="60" height="4" fill="var(--bad)"/><rect x="12" y="40" width="44" height="4" fill="var(--bad)"/></g>')
P3 = svg(340, sky(340) + CROWD
         + "".join(f'<path d="M{60 + i * 60} 200 L300 200" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 5"/>' for i in range(4))
         + person(300, 110, s=1.0, face=SMILE, **RUNNER, extra=BASKET) + label(330, 260, "⟦심부름꾼 한 명|one runner⟧", 13, "var(--ink)", cls="d")
         + ALLEYS
         + '<path d="M400 230 C480 230 540 220 600 210" stroke="var(--stone-dark)" stroke-width="8" fill="none" stroke-linecap="round"/>'
         + market(650, 120, 0.9)
         + label(380, 322, "⟦성 사람 모두가 심부름꾼 한 명을 시켜요|the whole castle sends the same runner⟧", 14, "var(--muted)"))

# 4. 거꾸로 심부름꾼: 창구 접수원
WALL = ('<rect x="380" y="40" width="380" height="260" fill="var(--stone-dark)"/>' + battlements(380, 22, 380, 8, "var(--stone-dark)", 20)
        + "".join(f'<rect x="{440 + i * 100}" y="90" width="70" height="70" rx="6" fill="var(--sky)"/>' + person(452 + i * 100, 82, s=0.55, face=SMILE, **CLERK) + label(475 + i * 100, 180, f"⟦창구 {i + 1}|counter {i + 1}⟧", 11, "#C9D5E6") for i in range(3)))
TOWNSFOLK = "".join(person(x, 150, s=0.65, hat=h, shirt="#4A5A72", face=SMILE, extra=NOTE) for x, h in ((30, "#E9B44C"), (100, None), (170, "var(--stone-dark)")))
P4 = svg(320, sky(320) + WALL + TOWNSFOLK
         + person(290, 130, s=0.85, face=SMILE, **RUNNER) + label(320, 250, "⟦접수원|receptionist⟧", 12, "var(--ink)", cls="d")
         + '<path d="M350 190 C400 200 410 125 440 125 M350 190 C420 200 500 130 540 125 M350 190 C450 210 600 140 640 125" stroke="var(--accent)" stroke-width="2" stroke-dasharray="5 5" fill="none"/>'
         + label(570, 60, "⟦한가한 창구로 나눠줘요|hands notes to whichever counter is free⟧", 12, "#F5E6B8")
         + label(200, 300, "⟦마을 사람은 성 안 지도를 몰라요|townsfolk never see the castle\'s layout⟧", 12, "var(--muted)"))

# 5. 심부름꾼은 쪽지를 다 볼 수 있다
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(60, 80, s=0.9, face=MASK, **dict(hat="var(--accent)", shirt="var(--accent)")) + '<g transform="translate(150,110)"><rect width="90" height="60" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/>' + label(45, 24, "⟦지민 → 약국|Jimin → pharmacy⟧", 10, "#142033") + label(45, 44, "⟦…약 이름…|…medicine…⟧", 10, "var(--bad)") + "</g>"
         + f'<g transform="translate(130,90)">{EYE}</g>'
         + label(190, 240, "⟦심부름꾼이 나쁘면 다 읽어요|a bad runner reads everything⟧", 13, "var(--bad)")
         + label(190, 275, "⟦누구를 시키느냐가 전부예요|who you send is everything⟧", 12, "var(--muted)")
         + person(440, 80, s=0.9, face=FROWN + SWEAT, **RUNNER) + label(470, 200, "⟦심부름꾼이 아파요|the runner is sick⟧", 12, "var(--bad)")
         + "".join(person(x, 140, s=0.55, hat=h, shirt="#4A5A72", face=FROWN) for x, h in ((560, None), (620, "#E9B44C"), (680, "#5B8DEF")))
         + label(620, 240, "⟦아무도 시장에 못 가요|nobody can reach the market⟧", 13, "var(--bad)")
         + label(620, 275, "⟦한 명이 다 하니까요|because one runner does it all⟧", 12, "var(--muted)"))

MASK_I = icon(f'<circle cx="32" cy="28" r="14" fill="{SKIN}"/><path d="M18 22 Q32 6 46 22 Z" fill="var(--accent)"/><path d="M14 44 h36" stroke="var(--bad)" stroke-width="3" stroke-dasharray="4 3"/>')
BASKET_I = icon('<path d="M12 28 h40 l-6 26 h-28z" fill="#C9A86A"/><path d="M20 28 a12 12 0 0 1 24 0" stroke="#8B5E3C" stroke-width="3" fill="none"/><circle cx="26" cy="24" r="5" fill="var(--bad)"/><circle cx="38" cy="23" r="5" fill="var(--good)"/>')
ALLEY_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="22" width="20" height="3" fill="var(--bad)"/><rect x="22" y="32" width="16" height="3" fill="var(--bad)"/><rect x="22" y="42" width="18" height="3" fill="var(--bad)"/>')
LEDGER_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="22" y="20" width="20" height="3" fill="#C9A86A"/><rect x="22" y="30" width="16" height="3" fill="#C9A86A"/><rect x="22" y="40" width="18" height="3" fill="#C9A86A"/>')

PAGE = {
    "slug": "proxy", "order": 31,
    "title": ("대신 다녀오는 심부름꾼", "The Errand Runner"),
    "h1": ("<em>프록시</em>가 뭐예요?", "What is a <em>Proxy</em>?"),
    "sub": ("프록시(Proxy)를 내 대신 시장에 다녀오는 심부름꾼 이야기로 풀어봤어요.",
            "Proxies, told as a story about the runner who goes to market on your behalf."),
    "panels": [
        {"svg": P1, "alt": ("성에서 시장까지 직접 간 사람을 시장 상인이 보며 '지민이가 사과 두 개 샀네'", "Someone walks from the castle to the market; the vendor watches and says Jimin bought two apples"),
         "caption": ("시장에 직접 가면 내 얼굴이 다 보여요.", "Go to market yourself and everyone sees your face."),
         "small": ("누가 뭘 샀는지 시장 사람들이 다 알아요.", "The whole market knows who bought what.")},
        {"svg": P2, "alt": ("내가 주황 모자 심부름꾼에게 쪽지를 주고, 시장 상인은 '주황 모자가 사과 두 개 샀네'", "I hand a note to a runner in an orange hat; the vendor says orange hat bought two apples"),
         "caption": ("심부름꾼에게 부탁하면 시장은 심부름꾼 얼굴만 봐요.", "Send a runner, and the market sees only the runner."),
         "small": ("내 얼굴은 성 밖으로 안 나가요.", "My face never leaves the castle.")},
        {"svg": P3, "hero": True, "alt": ("성 사람 넷이 한 심부름꾼에게 쪽지를 보내고, 심부름꾼은 바구니와 '가면 안 되는 골목' 목록을 들고 시장으로 감", "Four castle folk send notes to one runner, who carries a basket and a list of alleys to avoid on the way to market"),
         "caption": ("프록시는 대신 다녀오는 심부름꾼이에요.", "A proxy is the runner who goes in your place."),
         "small": ("성 사람 모두가 심부름꾼 한 명을 시켜요. 자주 사는 건 바구니에 미리 챙겨두고, 가면 안 되는 골목은 안 가요.", "The whole castle sends the same runner, who keeps popular items in a basket and steers clear of bad alleys."),
         "tricks": (4, [
             (MASK_I, ("얼굴 감추기", "Hidden face"), ("시장은 심부름꾼만 봐요", "the market sees only the runner"), "warm"),
             (BASKET_I, ("바구니", "The basket"), ("자주 사는 건 미리 — 캐시", "popular items ready — a cache"), "calm"),
             (ALLEY_I, ("가면 안 되는 골목", "Alleys to avoid"), ("도박 골목은 안 가요", "no gambling alley")),
             (LEDGER_I, ("대장", "The ledger"), ("누가 뭘 부탁했는지", "who asked for what"), "calm"),
         ])},
        {"svg": P4, "alt": ("마을 사람들이 쪽지를 접수원에게 주면 접수원이 성벽 안 창구 1·2·3 중 한가한 곳으로 나눠줌", "Townsfolk hand notes to a receptionist, who passes them to whichever of counters 1, 2 and 3 behind the wall is free"),
         "caption": ("거꾸로 심부름꾼도 있어요 — 창구 접수원.", "There's a runner the other way too — the receptionist."),
         "small": ('마을 사람은 성 안 방으로 직접 못 가고 접수원에게 줘요. 접수원이 한가한 창구에 나눠주고, 성 안 지도는 안 보여줘요. <a href="waf-ko.html">쪽지 검토원</a>도 여기 서요.',
                   'Townsfolk can\'t walk into the castle; they hand notes to the receptionist, who spreads them across free counters and never reveals the layout. The <a href="waf-en.html">note checker</a> stands here too.')},
        {"svg": P5, "alt": ("왼쪽: 가면 쓴 심부름꾼이 '지민 → 약국 …약 이름…' 쪽지를 읽음. 오른쪽: 심부름꾼이 아프자 성 사람 셋이 시장에 못 감", "Left: a masked runner reads a note — Jimin → pharmacy …medicine…. Right: the runner is sick and three castle folk can't reach the market"),
         "caption": ("심부름꾼은 내 쪽지를 다 볼 수 있어요.", "The runner can read every note."),
         "small": ("누구를 시키느냐가 전부예요. 봉인된 쪽지(HTTPS)는 못 읽지만 어디 가는지는 알아요. 그리고 심부름꾼이 아프면 다 멈춰요.", "Who you send is everything. A sealed note (HTTPS) can't be read, but the runner still knows where it's going. And when the runner is sick, everything stops.")},
    ],
    "summary": (("<b>프록시</b> = 내 <b>대신 다녀오는</b> 심부름꾼. 시장은 심부름꾼 얼굴만 보고, 심부름꾼은 <b>바구니</b>와 <b>골목 목록</b>을 들고 다녀요.",
                 "A <b>proxy</b> = the runner who <b>goes in your place</b>. The market sees only the runner, who carries a <b>basket</b> and a <b>list of alleys</b>."),
                ("Proxy. 포워드 프록시는 성의 심부름꾼, 리버스 프록시는 창구 접수원이에요. 검문소(SWG)는 심부름꾼에게 규칙책을 얹은 것. Squid, nginx, HAProxy, Cloudflare 같은 것들.",
                 "A forward proxy is the castle's runner; a reverse proxy is the receptionist at the counter. The checkpoint (SWG) is a runner with a rulebook. Squid, nginx, HAProxy, Cloudflare.")),
    "glossary": [
        ("포워드 프록시", "Forward proxy", ("성의 심부름꾼.", "The castle's runner."), ("나 대신 밖으로 나가요. 시장은 내 얼굴을 몰라요.", "Goes out on my behalf. The market never sees my face.")),
        ("리버스 프록시", "Reverse proxy", ("창구 접수원.", "The receptionist."), ("마을 대신 안으로 전달해요. 성 안 지도는 안 보여줘요.", "Passes notes inward for the town, hiding the castle's layout.")),
        ("캐시", "Cache", ("바구니.", "The basket."), ("자주 사는 건 미리 챙겨둬요. 시장에 안 가도 바로 줘요.", "Popular items kept ready — handed over without a trip to market.")),
        ("부하 분산", "Load balancing", ("한가한 창구에 나눠주기.", "Spreading notes to free counters."), ("접수원이 창구 1·2·3에 골고루.", "The receptionist shares work across counters 1, 2 and 3.")),
        ("IP 숨김", "IP masking", ("내 얼굴 대신 심부름꾼 얼굴.", "The runner's face instead of mine."), ('바깥엔 심부름꾼 주소만 보여요. → <a href="vpn-ko.html">봉인된 땅굴</a>과 비슷하지만 봉인은 없어요', 'Outside sees only the runner\'s address. → like the <a href="vpn-en.html">sealed tunnel</a>, minus the seal')),
        ("투명 프록시", "Transparent proxy", ("시킨 적 없는 심부름꾼.", "The runner nobody asked for."), ("성이 알아서 심부름꾼을 거치게 해요. 나는 모르고 지나가요.", "The castle routes everyone through the runner automatically, unnoticed.")),
        ("TLS 종료", "TLS termination", ("접수원이 봉인을 뜯음.", "The receptionist breaks the seal."), ('봉인된 쪽지를 접수원이 열어 안 사람에게 펼쳐 줘요. → <a href="swg-ko.html">봉인 뜯기</a>', 'The receptionist opens sealed notes and hands them in unsealed. → <a href="swg-en.html">breaking seals</a>')),
        ("SWG", "SWG", ("규칙책 든 심부름꾼.", "A runner with a rulebook."), ('심부름꾼에 검문소 규칙을 얹은 것. → <a href="swg-ko.html">마을로 나가는 성문 검문소</a>', 'The runner plus checkpoint rules. → <a href="swg-en.html">the checkpoint to town</a>')),
    ],
}
