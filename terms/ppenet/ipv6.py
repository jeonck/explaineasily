from _draw import *
from _world import *

# 1. 번지수가 다 떨어졌어요
P1 = svg(345, sky(345)
         + postoffice(220, 170, 0.8) + postoffice(380, 170, 0.8) + postoffice(540, 170, 0.8)
         + person(460, 230, s=0.7, face=SWEAT + EYES, **CLERK)
         + label(460, 328, "⟦세상에 집이 너무 많아져서 번지수가 동났어요|so many houses now that the addresses ran out⟧", 11, "var(--ink)")
         + label(380, 30, "⟦번지수 체계(IPv4)의 숫자가 다 쓰였어요|the numbers in the old address system (IPv4) are all used up⟧", 13, "var(--ink)", cls="d"))

# 2. 한 번지수를 여러 집이 억지로 나눠 써요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + postoffice(380, 150, 0.8, "⟦번지 1.2.3.4|address 1.2.3.4⟧")
         + person(280, 230, s=0.55, face=EYES, **SENDER) + person(380, 240, s=0.55, face=EYES, **RECEIVER) + person(480, 230, s=0.55, face=EYES, **CLERK)
         + label(380, 282, "⟦새 집은 번지수를 못 받고, 임시방편(공유 주소)도 한계가 있어요|a new house can't get its own address — and sharing one is only a stopgap⟧", 12, "var(--ink)", cls="d"))

# 3. IPv6 = 번지수 체계를 훨씬 길게 늘린 것 (hero)
P3 = svg(340, sky(340)
         + routemap(80, 70, 260, 150, "⟦IPv4 번지수|IPv4 address⟧", ("⟦1 . 2 . 3 . 4|1 . 2 . 3 . 4⟧",), 1.0)
         + routemap(400, 70, 280, 220, "⟦IPv6 번지수|IPv6 address⟧", ("⟦2001:0db8:85a3|2001:0db8:85a3⟧", "⟦:0000:0000:8a2e|:0000:0000:8a2e⟧", "⟦:0370:7334|:0370:7334⟧"), 1.0)
         + label(380, 30, "⟦IPv6 = 번지수 체계를 훨씬 길게 늘려 사실상 무한한 새 주소를 만든 것|IPv6 = stretching the address system far longer, creating addresses that are practically endless⟧", 13, "var(--ink)", cls="d"))

# 4. IPv4 vs IPv6 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 310, 250, "⟦IPv4|IPv4⟧",
                    ("⟦길이 — 4덩이(32비트)|length — 4 groups (32 bits)⟧",
                     "⟦개수 — 약 43억 개|count — about 4.3 billion⟧",
                     "⟦NAT — 거의 필수|NAT — almost required⟧",
                     "⟦표기 — 1.2.3.4|notation — 1.2.3.4⟧"), 1.0)
         + routemap(390, 40, 310, 250, "⟦IPv6|IPv6⟧",
                    ("⟦길이 — 8덩이(128비트)|length — 8 groups (128 bits)⟧",
                     "⟦개수 — 거의 무한|count — practically endless⟧",
                     "⟦NAT — 필요 없음|NAT — not needed⟧",
                     "⟦표기 — 2001:...:7334|notation — 2001:...:7334⟧"), 1.0, hl=1))

# 5. 아직 완전히 바뀌진 않았어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + postoffice(190, 170, 0.6, "⟦IPv6 우체국|IPv6 office⟧") + postoffice(570, 170, 0.6, "⟦IPv4 우체국|IPv4 office⟧")
         + '<path d="M250 200 Q380 160 510 200" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 5" fill="none"/>'
         + label(380, 282, "⟦당분간은 두 체계를 함께 쓰는 과도기예요(듀얼스택)|for now, both systems run side by side — a transition period (dual-stack)⟧", 12, "var(--ink)", cls="d"))

LEN_I = icon('<path d="M10 32 h44" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/><path d="M10 24 v16 M54 24 v16" stroke="var(--accent)" stroke-width="3"/>')
INF_I = icon('<path d="M20 32 a10 10 0 1 1 0 .1z" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M44 32 a10 10 0 1 1 0 .1z" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M30 32 h4" stroke="var(--good)" stroke-width="4"/>')
AUTO_I = icon('<rect x="14" y="20" width="36" height="24" rx="4" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><path d="M22 32 l6 6 l14 -14" stroke="var(--good)" stroke-width="3" fill="none"/>')
BRIDGE_I = icon('<path d="M10 44 q22 -24 44 0" stroke="var(--accent)" stroke-width="4" fill="none"/><path d="M10 44 v6 M54 44 v6" stroke="var(--ink)" stroke-width="3"/>')

PAGE = {
    "slug": "ipv6", "order": 12,
    "title": ("끝없이 늘어난 새 번지수", "The New, Nearly Endless Address System"),
    "h1": ("<em>IPv6</em>가 뭐예요?", "What is <em>IPv6</em>?"),
    "sub": ("IPv6를, 동나버린 번지수 체계를 훨씬 길게 늘려 새로 만든 주소 이야기로 풀어봤어요.",
            "IPv6, told as a story about stretching an address system that ran out into a far longer new one."),
    "panels": [
        {"svg": P1, "alt": ("우체국 직원이 세상에 집이 너무 많아져 번지수가 동났다고 걱정함", "A clerk worries that there are now so many houses the addresses have run out"),
         "caption": ("번지수가 다 떨어졌어요.", "The addresses have all run out."),
         "small": ("번지수 체계(IPv4)의 숫자가 다 쓰였어요.", "The numbers in the old address system (IPv4) are all used up.")},
        {"svg": P2, "alt": ("한 번지수 아래 세 사람이 억지로 함께 몰려 있음", "Three people crowded together under one single address"),
         "caption": ("한 번지수를 여러 집이 억지로 나눠 써요.", "Several houses are forced to share one address."),
         "small": ("새 집은 번지수를 못 받고, 임시방편도 한계가 있어요.", "A new house can't get its own address, and sharing one is only a stopgap.")},
        {"svg": P3, "hero": True, "alt": ("짧은 IPv4 번지수 옆에 훨씬 긴 IPv6 번지수가 나란히 놓임", "A short IPv4 address next to a much longer IPv6 address"),
         "caption": ("IPv6는 번지수 체계를 훨씬 길게 늘린 거예요.", "IPv6 stretches the address system far longer."),
         "small": ("4덩이에서 8덩이로 늘려 사실상 무한한 새 주소를 만들었어요.", "Stretched from 4 groups to 8, creating addresses that are practically endless."),
         "tricks": (4, [
             (LEN_I, ("훨씬 긴 주소", "A much longer address"), ("32비트에서 128비트로 늘었어요", "grew from 32 bits to 128 bits"), "calm"),
             (INF_I, ("거의 무한한 개수", "Practically endless count"), ("지구 모래알보다 많아요", "more addresses than grains of sand on Earth")),
             (AUTO_I, ("자동 주소 할당", "Self-assigning addresses"), ("스스로 주소를 만들어 받기도 해요", "a device can generate its own address"), "warm"),
             (BRIDGE_I, ("호환 작업 필요", "Needs compatibility work"), ("옛 체계와 당장은 안 섞여요", "doesn't mix with the old system right away")),
         ])},
        {"svg": P4, "alt": ("IPv4와 IPv6를 길이·개수·NAT 필요 여부·표기법으로 비교한 두 안내판", "Two boards comparing IPv4 and IPv6 by length, count, NAT need, and notation"),
         "caption": ("IPv4와 IPv6는 네 가지가 달라요.", "IPv4 and IPv6 differ on four things."),
         "small": ("IPv6는 훨씬 길고 많고, NAT도 필요 없어요.", "IPv6 is far longer, far more plentiful, and doesn't need NAT.")},
        {"svg": P5, "alt": ("IPv6 우체국과 IPv4 우체국이 점선으로 연결돼 나란히 함께 운영됨", "An IPv6 post office and an IPv4 post office running side by side, linked by a dashed line"),
         "caption": ("아직 완전히 바뀌진 않았어요.", "The switch isn't complete yet."),
         "small": ("당분간은 두 체계를 함께 쓰는 과도기예요(듀얼스택).", "For now, both systems run side by side — a transition period (dual-stack).")},
    ],
    "summary": (("<b>IPv6</b>는 <b>번지수 체계를 32비트에서 128비트로 훨씬 길게 늘려</b>, 사실상 <b>무한에 가까운 새 주소</b>를 만든 것이에요.",
                 "<b>IPv6</b> stretches the <b>address system from 32 bits to a far longer 128 bits</b>, creating a <b>practically endless supply of new addresses</b>."),
                ("IPv6(Internet Protocol version 6)는 약 43억 개뿐인 IPv4 주소 고갈 문제를 해결하기 위해 주소 길이를 128비트로 늘린 차세대 인터넷 프로토콜이에요. NAT 없이도 기기마다 고유 주소를 줄 수 있고, 자동 주소 설정(SLAAC) 같은 기능도 갖췄어요. IPv4와 직접 호환되지 않아 듀얼스택·터널링 같은 과도기 기법을 함께 써요.",
                 "IPv6 (Internet Protocol version 6) is the next-generation protocol that stretches address length to 128 bits, solving the exhaustion of IPv4's roughly 4.3 billion addresses. It can give every device its own unique address without NAT, and includes features like stateless address autoconfiguration (SLAAC). Since it isn't directly compatible with IPv4, transition techniques like dual-stack and tunneling are used alongside it.")),
    "glossary": [
        ("IPv6", "IPv6", ("훨씬 길게 늘린 새 번지수 체계.", "The far longer new address system."), ("128비트, 8덩이로 표기해요.", "128 bits, written as 8 groups.")),
        ("IPv4", "IPv4", ("예전부터 쓰던 번지수 체계.", "The address system used from the start."), ("32비트, 약 43억 개뿐이에요.", "32 bits — only about 4.3 billion addresses.")),
        ("NAT", "NAT", ("한 번지수를 여럿이 억지로 나눠 쓰는 임시방편.", "The stopgap of forcing several houses to share one address."), ("IPv6에선 대부분 필요 없어요.", "Mostly unnecessary under IPv6.")),
        ("듀얼스택", "Dual-stack", ("IPv4와 IPv6 우체국을 둘 다 운영하는 과도기 방식.", "Running both an IPv4 and an IPv6 post office during the transition."), ("지금 많은 곳이 이 방식을 써요.", "Widely used right now.")),
        ("SLAAC", "SLAAC", ("기기가 스스로 번지수를 만들어 받는 기능.", "A device generating and assigning itself an address."), ("IPv6가 갖춘 자동 할당 방법이에요.", "IPv6's own automatic-assignment method.")),
        ("동적 라우팅 프로토콜", "Dynamic routing protocol", ("우체국들이 지도를 스스로 고치는 규칙.", "The rule letting post offices redraw their map themselves."), ('새 번지수 체계로도 지도를 계속 자동으로 고쳐야 해요. → <a href="dynamicrouting-ko.html">스스로 고쳐 그리는 배송 지도</a>', 'The map still has to keep redrawing itself under the new addresses. → <a href="dynamicrouting-en.html">the delivery map that redraws itself</a>')),
        ("소켓", "Socket", ("집주소+호실번호로 만든 전용 구멍.", "A dedicated hole made from an address and a room number."), ('소켓 주소의 집 부분(IP)이 이 체계로 바뀌어 가요. → <a href="socket-ko.html">전용 우편함 구멍</a>', "The house part of a socket address is moving to this system. → <a href=\"socket-en.html\">the dedicated mailbox hole</a>")),
        ("DNS", "DNS", ("동네 주소록.", "The neighborhood address book."), ('번지수가 길어진 만큼 주소록이 더 중요해졌어요. → <a href="dns-ko.html">동네 주소록</a>', "With addresses this long, the address book matters even more. → <a href=\"dns-en.html\">the neighborhood address book</a>")),
    ],
}
