from _draw import *

BUILDER = dict(hat="#E9B44C", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def wall(x, y, w, h, crack=None, patch=False):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="var(--stone-dark)"/>{battlements(x, y - 18, w, max(3, int(w / 40)), "var(--stone-dark)", 20)}'
    if crack:
        cx, cy = crack
        out += f'<path d="M{cx} {cy} l6 14 l-8 12 l10 16 l-6 14" stroke="#0A1120" stroke-width="4" fill="none" stroke-linecap="round"/>'
        if patch:
            out += f'<rect x="{cx - 18}" y="{cy - 6}" width="36" height="68" rx="2" fill="#8B5E3C"/><circle cx="{cx - 10}" cy="{cy + 2}" r="2" fill="var(--night)"/><circle cx="{cx + 10}" cy="{cy + 54}" r="2" fill="var(--night)"/>'
    return out


GLASS = '<g transform="translate(70,60)"><circle r="16" fill="var(--panel)" fill-opacity="0.4" stroke="var(--night)" stroke-width="4"/><path d="M12 12 L26 26" stroke="var(--night)" stroke-width="6" stroke-linecap="round"/></g>'
PLANS = '<g transform="translate(50,60)"><rect width="40" height="50" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M8 12 h24 M8 22 h24 M8 32 h16" stroke="#C9A86A" stroke-width="2"/></g>'

# 1. 성벽은 목수가 지었다
P1 = svg(300, sky(300, ground=False) + wall(300, 80, 460, 220, crack=(620, 150))
         + person(120, 120, s=0.9, face=SMILE, **BUILDER, extra=PLANS) + label(150, 265, "⟦목수|the builder⟧", 13, "var(--ink)", cls="d")
         + label(620, 60, "⟦작은 틈|a small crack⟧", 12, "var(--muted)")
         + label(380, 40, "⟦큰 성벽엔 목수도 모르는 틈이 있기 마련이에요|any big wall has cracks even the builder doesn\'t know about⟧", 13, "var(--ink)", cls="d"))

# 2. 도둑이 먼저 찾았다
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + wall(300, 80, 460, 220, crack=(620, 150))
         + person(540, 90, s=0.9, face=MASK, extra=GLASS)
         + person(80, 120, s=0.8, face=SMILE, **BUILDER) + person(180, 130, s=0.8, face=SMILE, **GUARD)
         + bubble(60, 40, 200, 34, "⟦틈? 우리 성벽에?|A crack? In our wall?⟧", 13, "var(--panel)", "var(--line)", "bottom")
         + '<g transform="translate(660,250)"><rect x="-36" y="-14" width="72" height="28" rx="6" fill="#E9B44C"/>' + label(0, 5, "⟦비싸게 팔아요|sold dearly⟧", 10, "#142033") + "</g>"
         + label(380, 285, "⟦목수도, 경비도 몰라요. 도둑만 알아요|the builder and the guards don\'t know — only the thief⟧", 13, "var(--muted)"))

# 3. 제로데이 = 고칠 시간이 0일이었던 틈 (hero)
STEPS = (("⟦도둑이 틈을 찾음|thief finds the crack⟧", "var(--bad)"), ("⟦도둑이 씀|thief uses it⟧", "var(--bad)"), ("⟦누군가 알아챔|somebody notices⟧", "var(--accent)"), ("⟦목수가 판자를 만듦|builder makes a patch⟧", "var(--good)"), ("⟦성마다 붙임|every castle nails it on⟧", "var(--good)"))
TIMELINE = '<path d="M60 200 H700" stroke="var(--line)" stroke-width="4"/>' + "".join(
    f'<circle cx="{80 + i * 150}" cy="200" r="12" fill="{c}"/>' + label(80 + i * 150, 240 + (i % 2) * 18, t, 11, "var(--ink)") for i, (t, c) in enumerate(STEPS))
ZERO = ('<g transform="translate(155,90)"><rect x="-50" y="-40" width="100" height="80" rx="8" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><rect x="-50" y="-40" width="100" height="22" rx="8" fill="var(--bad)"/>'
        + label(0, -25, "⟦고칠 시간|days to fix⟧", 11, "#FFF") + label(0, 24, "0", 44, "var(--bad)", cls="d") + "</g>")
P3 = svg(320, '<rect width="760" height="320" fill="var(--panel)"/>' + TIMELINE + ZERO
         + '<rect x="60" y="170" width="290" height="8" fill="var(--bad)" fill-opacity="0.35"/>' + label(205, 160, "⟦막을 판자가 없는 시간|time with no patch to nail on⟧", 12, "var(--bad)")
         + label(380, 300, "⟦틈이 알려진 날부터 세요. 그 전에 쓰이면 막을 판자가 없어요|count from the day the crack is known; used before that, there\'s nothing to nail on⟧", 12, "var(--muted)"))

# 4. 틈은 몰라도 행동은 보인다
P4 = svg(320, sky(320, ground=False) + wall(0, 60, 240, 260, crack=(180, 130))
         + person(200, 140, s=0.7, face=MASK) + '<path d="M250 200 L320 200" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 6"/>'
         + dog(370, 230, 0.9, bark=True)
         + '<rect x="450" y="60" width="8" height="260" fill="var(--stone-dark)"/>' + label(454, 50, "⟦복도 나누기|hallway split⟧", 11, "var(--muted)")
         + '<g transform="translate(560,170)"><circle r="12" fill="none" stroke="#E9B44C" stroke-width="6"/><rect x="10" y="-4" width="36" height="8" fill="#E9B44C"/></g>' + label(580, 210, "⟦방 하나 열쇠|one-room key⟧", 12, "var(--muted)")
         + person(660, 100, s=0.7, face=EYES, **GUARD) + label(680, 220, "⟦복도 파수꾼|hallway watcher⟧", 11, "var(--muted)")
         + label(480, 300, "⟦틈 하나로 성 전체를 못 열어요|one crack can\'t open the whole castle⟧", 13, "var(--good)", cls="d"))

# 5. 판자가 나와도 안 붙이면 그대로
P5 = svg(300, '<rect width="760" height="300" fill="var(--accent-soft)"/>'
         + wall(40, 90, 200, 180, crack=(180, 150), patch=True) + label(140, 60, "⟦판자 붙임|patched⟧", 13, "var(--good)")
         + wall(290, 90, 200, 180, crack=(430, 150)) + label(390, 60, "⟦판자 있는데 안 붙임|patch exists, not nailed on⟧", 12, "var(--bad)")
         + wall(540, 90, 200, 180, crack=(680, 150)) + label(640, 60, "⟦안 붙임|not nailed on⟧", 12, "var(--bad)")
         + person(600, 150, s=0.6, face=MASK, extra=GLASS)
         + label(380, 290, "⟦제로데이는 드물어요. 대부분은 판자를 안 붙인 틈으로 당해요|zero-days are rare; most break-ins come through cracks with a patch nobody nailed on⟧", 12, "var(--muted)"))

CRACK_I = icon('<rect x="8" y="14" width="48" height="40" fill="var(--stone-dark)"/><path d="M30 14 l4 10 l-6 8 l8 10 l-4 12" stroke="#0A1120" stroke-width="3" fill="none" stroke-linecap="round"/>')
HOWTO_I = icon('<rect x="14" y="8" width="36" height="48" rx="3" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/><path d="M22 22 h20 M22 32 h14 M22 42 h18" stroke="var(--bad)" stroke-width="3"/>')
PATCH_I = icon('<rect x="8" y="14" width="48" height="40" fill="var(--stone-dark)"/><rect x="24" y="12" width="16" height="44" rx="2" fill="#8B5E3C"/><circle cx="28" cy="18" r="1.5" fill="var(--night)"/><circle cx="36" cy="50" r="1.5" fill="var(--night)"/>')
ZERO_I = icon('<rect x="12" y="12" width="40" height="40" rx="6" fill="var(--panel)" stroke="var(--bad)" stroke-width="3"/><rect x="12" y="12" width="40" height="12" rx="6" fill="var(--bad)"/><text x="32" y="46" text-anchor="middle" font-size="20" font-weight="700" fill="var(--bad)">0</text>')

PAGE = {
    "slug": "zeroday", "order": 41,
    "title": ("아무도 모르는 구멍", "The Hole Nobody Knows About"),
    "h1": ("<em>제로데이</em>가 뭐예요?", "What is a <em>Zero-day</em>?"),
    "sub": ("제로데이(Zero-day)를 목수도 모르는 성벽 틈 이야기로 풀어봤어요.",
            "Zero-days, told as a story about a crack in the wall that even the builder doesn't know about."),
    "panels": [
        {"svg": P1, "alt": ("설계도를 든 목수와 큰 성벽, 벽 한쪽의 작은 틈", "A builder with plans and a big wall; a small crack on one side of it"),
         "caption": ("성벽은 목수가 지었어요.", "The wall was built by a builder."),
         "small": ("큰 성벽엔 목수도 모르는 작은 틈이 있기 마련이에요.", "Any big wall has small cracks even the builder doesn't know about.")},
        {"svg": P2, "alt": ("돋보기를 든 도둑이 틈을 찾았고, 목수와 경비는 '틈? 우리 성벽에?' 하고, 옆에 '비싸게 팔아요' 금화", "A thief with a magnifying glass finds the crack; the builder and guard say A crack? In our wall?; a bag of gold reads sold dearly"),
         "caption": ("도둑이 그 틈을 먼저 찾았어요.", "The thief found the crack first."),
         "small": ("목수도, 경비도 몰라요. 도둑만 알아요. 다른 도둑에게 비싸게 팔기도 해요.", "The builder and the guards have no idea. Only the thief knows — and sometimes sells it to other thieves for a lot.")},
        {"svg": P3, "hero": True, "alt": ("'고칠 시간 0' 달력과, 도둑이 틈을 찾음 → 도둑이 씀 → 누군가 알아챔 → 목수가 판자를 만듦 → 성마다 붙임 순서의 시간표. 앞 구간은 '막을 판자가 없는 시간'", "A calendar reading days to fix: 0, and a timeline — thief finds the crack → thief uses it → somebody notices → builder makes a patch → every castle nails it on; the first stretch is labeled time with no patch"),
         "caption": ("제로데이는 목수가 고칠 시간이 0일이었던 틈이에요.", "A zero-day is a crack the builder had zero days to fix."),
         "small": ("틈이 알려진 날부터 세요. 알려지기 전에 쓰이면 막을 판자가 없어요.", "Count from the day the crack becomes known. Used before that, there's no patch to nail on."),
         "tricks": (4, [
             (CRACK_I, ("틈", "The crack"), ("취약점", "a vulnerability")),
             (HOWTO_I, ("틈으로 들어가는 법", "How to get through it"), ("익스플로잇", "an exploit"), "warm"),
             (PATCH_I, ("판자", "The patch"), ("목수가 만든 덧댐", "the builder\'s fix"), "calm"),
             (ZERO_I, ("0일", "Zero days"), ("알려지기 전에 쓰였어요", "used before anyone knew")),
         ])},
        {"svg": P4, "alt": ("틈으로 들어온 도둑에게 경비견이 짖고, 복도는 벽으로 나뉘어 있고, 방 하나 열쇠와 복도 파수꾼", "A thief slipping through the crack is barked at by the dog; the hallway is split by a wall; a one-room key and the hallway watcher"),
         "caption": ("틈은 몰라도 들어온 뒤 행동은 보여요.", "You may not know the crack, but you can see what comes through it."),
         "small": ('<a href="edr-ko.html">경비견</a>이 짖고, <a href="vlan-ko.html">복도가 나뉘어</a> 있고, <a href="zerotrust-ko.html">방 하나 열쇠</a>만 있으면 틈 하나로 성 전체를 못 열어요.',
                   'With the <a href="edr-en.html">dog</a> barking, the <a href="vlan-en.html">hallway split</a>, and <a href="zerotrust-en.html">one-room keys</a>, one crack can\'t open the whole castle.')},
        {"svg": P5, "alt": ("성벽 셋: 하나는 판자를 붙였고, 둘은 판자가 있는데도 틈이 그대로. 도둑이 그 틈을 살핌", "Three walls: one patched, two still cracked though a patch exists; a thief inspects the open cracks"),
         "caption": ("판자가 나와도 안 붙이면 그대로예요.", "A patch nobody nails on fixes nothing."),
         "small": ("제로데이는 드물어요. 대부분은 판자가 있는데 안 붙인 틈으로 당해요. 붙이는 날짜를 정해두세요.", "Zero-days are rare. Most break-ins come through cracks that already had a patch. Set a day to nail them on.")},
    ],
    "summary": (("<b>제로데이</b> = 목수도 모르는 성벽 틈을 도둑이 <b>먼저</b> 찾아, 고칠 <b>판자가 없는 채로</b> 쓰는 것.",
                 "A <b>zero-day</b> = a crack the builder doesn't know about, found <b>first</b> by the thief and used <b>before any patch exists</b>."),
                ("Zero-day. 틈(취약점) + 들어가는 법(익스플로잇) + 판자(패치). 틈마다 CVE 번호가 붙어요. 드물고 비싸요 — 대부분의 사고는 판자를 안 붙인 틈(N-day)이에요.",
                 "Zero-day: the crack (vulnerability) + the way through (exploit) + the patch. Every crack gets a CVE number. They're rare and expensive — most incidents come through unpatched cracks (N-days).")),
    "glossary": [
        ("취약점", "Vulnerability", ("틈.", "The crack."), ("목수가 실수로 남긴 구멍. 큰 성벽엔 늘 있어요.", "A hole the builder left by mistake. Every big wall has some.")),
        ("익스플로잇", "Exploit", ("틈으로 들어가는 법.", "How to get through the crack."), ("틈이 있어도 지나가는 법을 알아야 도둑이 써요.", "A crack alone isn\'t enough — the thief needs the way through.")),
        ("패치", "Patch", ("판자.", "The patch board."), ('목수가 만든 덧댐. 붙이는 건 성 주인 몫. → <a href="malware-ko.html">열린 문 고치기</a>', 'The builder\'s fix; nailing it on is the castle\'s job. → <a href="malware-en.html">fixing the open door</a>')),
        ("CVE", "CVE", ("틈 번호.", "The crack\'s number."), ("CVE-2024-1234 처럼 틈마다 붙는 이름. 온 세상이 같은 번호로 불러요.", "A name like CVE-2024-1234 for every crack, so the whole world says the same thing.")),
        ("N-day", "N-day", ("판자 있는데 안 붙인 틈.", "A crack with a patch nobody nailed on."), ("알려진 지 N일. 제로데이보다 훨씬 흔해요.", "Known for N days. Far more common than zero-days.")),
        ("버그 바운티", "Bug bounty", ("틈 찾으면 상금.", "A reward for finding cracks."), ("착한 사람이 도둑보다 먼저 찾게 하는 방법.", "So the good folks find them before the thieves do.")),
        ("가상 패치", "Virtual patch", ("판자 나올 때까지 문지기가 그 틈 앞에.", "A guard at the crack until the board arrives."), ('<a href="waf-ko.html">검토원</a>이나 <a href="idsips-ko.html">전단 파수꾼</a>이 그 틈만 지켜요.', 'The <a href="waf-en.html">note checker</a> or the <a href="idsips-en.html">poster-watcher</a> covers that one crack.')),
        ("심층 방어", "Defense in depth", ("여러 겹.", "Many layers."), ('틈 하나로 못 뚫게. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', 'So one crack never opens everything. → <a href="zerotrust-en.html">the castle that always asks</a>')),
    ],
}
