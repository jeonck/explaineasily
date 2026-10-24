from _draw import *

GUARD = dict(hat="var(--good)", shirt="var(--good)")
CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
WATER = "#5B9BD5"


def no_bridge(x, y):
    return (f'<path d="M{x} {y} h60" stroke="#8B5E3C" stroke-width="8" stroke-dasharray="10 12"/>'
            f'<path d="M{x + 20} {y - 12} l20 24 M{x + 40} {y - 12} l-20 24" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>')


def checkpost(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-6" width="36" height="46" rx="3" fill="var(--panel)" stroke="var(--good)" stroke-width="3"/>'
            '<path d="M-24 -6 L0 -26 L24 -6 Z" fill="var(--good)"/></g>')


def grade_castle(x, y, s=1.0, grade=1, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-50" y="0" width="100" height="70" fill="var(--stone-dark)"/>'
            f'{battlements(-50, -20, 100, 3, "var(--stone-dark)")}<path d="M-16 70 V40 a16 16 0 0 1 32 0 V70 Z" fill="var(--night)"/>'
            f'<circle cx="40" cy="-6" r="16" fill="{color}"/>' + label(40, -1, str(grade), 16, "#FFF", cls="d") + "</g>")


def cloud(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="-20" cy="0" rx="26" ry="18" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            '<ellipse cx="15" cy="-8" rx="32" ry="22" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            '<ellipse cx="45" cy="6" rx="24" ry="16" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/></g>')


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


# 1. 나라의 모든 성이 다리를 아예 끊었어요
P1 = svg(300, sky(300)
         + f'<rect x="320" y="150" width="200" height="110" fill="{WATER}" opacity="0.5"/>'
         + castle(20, 70, 0.6) + label(140, 190, "⟦공공기관 성|a public-sector castle⟧", 11, "var(--muted)")
         + no_bridge(330, 195) + label(420, 130, "⟦다리가 없어요|no bridge at all⟧", 13, "var(--bad)", cls="d")
         + cloud(600, 90, 1.1) + label(600, 140, "⟦클라우드|the cloud⟧", 11, "var(--muted)")
         + label(380, 280, "⟦도둑도 못 오지만, 바깥 도구도 전혀 못 써요|no thief can get in — but no outside tool can either⟧", 13, "var(--ink)"))

# 2. 그런데 업무엔 점점 바깥 도구가 필요해요
P2 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + person(160, 150, s=0.85, face=FROWN + SWEAT, **CLERK)
         + bubble(90, 60, 230, 40, "⟦클라우드 없인 일이 안 돌아가요|nothing works without the cloud now⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + cloud(560, 100, 1.2) + no_bridge(420, 195)
         + label(380, 258, "⟦다리를 다시 놓자니 도둑이 걱정이에요|rebuild the bridge, and the old worry about thieves comes back⟧", 13, "var(--ink)"))

# 3. N2SF = 다리는 다시 놓되, 검문소를 촘촘히 (hero)
P3 = svg(340, sky(340)
         + grade_castle(110, 120, 0.8, 1, "var(--bad)") + label(110, 230, "⟦1등급|grade 1⟧", 11, "var(--muted)")
         + '<path d="M190 230 h70" stroke="#8B5E3C" stroke-width="10" stroke-linecap="round"/>' + checkpost(230, 205, 0.6)
         + grade_castle(330, 140, 0.6, 2, "var(--accent)") + label(330, 215, "⟦2등급|grade 2⟧", 10, "var(--muted)")
         + '<path d="M380 215 h70" stroke="#8B5E3C" stroke-width="10" stroke-linecap="round"/>' + checkpost(420, 195, 0.55)
         + cloud(560, 110, 1.0)
         + label(380, 30, "⟦N2SF = 다리는 놓되, 다리 위 검문소를 촘촘히 세워요|N2SF = rebuild the bridge, but line it with checkpoints, one after another⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦중요도별로 성 등급도 나눠요|castles are also graded by how critical they are⟧", 12, "var(--muted)"))

# 4. 비교표
P4 = svg(300, sky(300)
         + box(50, 30, 310, 240, "⟦기존 — 물리적 망분리|OLD — physical separation⟧",
               ("⟦다리를 아예 끊어요|the bridge is cut entirely⟧", "⟦가장 안전하지만 가장 불편해요|safest, but least convenient⟧", "⟦클라우드를 거의 못 써요|cloud tools barely usable⟧"), 12)
         + box(400, 30, 310, 240, "⟦N2SF — 논리적 분리|N2SF — logical separation⟧",
               ("⟦다리는 열되 구간마다 확인해요|the bridge stays open, checked section by section⟧", "⟦제로 트러스트 방식과 같아요|the same idea as zero trust⟧", "⟦등급에 맞으면 클라우드도 써요|cloud use allowed, matched to the grade⟧"), 12))

# 5. 아직 초기 단계예요
P5 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + small_castle(100, 60, 0.5) + label(200, 180, "⟦바꾼 기관|a castle that switched⟧", 11, "var(--good)")
         + small_castle(380, 90, 0.42) + label(460, 185, "⟦아직 그대로인 기관|a castle that hasn't yet⟧", 11, "var(--muted)")
         + person(640, 150, s=0.8, face=EYES, **GUARD)
         + bubble(560, 70, 200, 40, "⟦등급 나누는 기준부터 어려워요|even grading the castles is hard⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦모든 공공기관이 다 바꾸진 않았고, 등급 기준도 아직 다듬는 중이에요|not every public castle has switched, and the grading itself is still being refined⟧", 11, "var(--ink)"))

PAGE = {
    "slug": "n2sf", "order": 9,
    "title": ("다리를 끊는 대신 검문소를 촘촘히", "Instead of Cutting the Bridge, Checkpoints All Along It"),
    "h1": ("<em>국가 망 보안체계(N2SF)</em>가 뭐예요?", "What is the <em>National Network Security Framework (N2SF)</em>?"),
    "sub": ("국가 망 보안체계(N2SF)를 다리를 끊는 대신 검문소를 촘촘히 세우는 이야기로 풀어봤어요.",
            "N2SF, Korea's national network security framework, told as a story about rebuilding the bridge but lining it with checkpoints."),
    "panels": [
        {"svg": P1, "alt": ("공공기관 성과 클라우드 사이 다리가 완전히 끊겨 있음", "The bridge between a public-sector castle and the cloud is cut entirely"),
         "caption": ("나라의 모든 성이 다리를 아예 끊었어요.", "Every public-sector castle had its bridge cut entirely."),
         "small": ('<a href="airgap-ko.html">다리 없는 섬</a>처럼요 — 도둑도 못 오지만, 바깥 도구도 전혀 못 써요.',
                   'Like an <a href="airgap-en.html">island with no bridge</a> — no thief can get in, but no outside tool can either.')},
        {"svg": P2, "alt": ("서기가 땀을 흘리며 '클라우드 없인 일이 안 돌아가요'라고 말하는데 다리는 여전히 끊겨 있음", "A sweating clerk says nothing works without the cloud now, while the bridge remains cut"),
         "caption": ("그런데 업무엔 점점 바깥 도구가 필요해요.", "But more and more work needs outside tools."),
         "small": ("다리를 다시 놓자니 도둑이 걱정이에요.", "Rebuild the bridge, and the old worry about thieves comes right back.")},
        {"svg": P3, "hero": True, "alt": ("등급이 다른 두 성 사이 다리마다 검문소가 줄지어 서 있고, 그 너머에 구름 모양 클라우드가 있음", "Checkpoints line the bridges between castles of different grades, with a cloud shape beyond them"),
         "caption": ("N2SF는 다리는 다시 놓되, 다리 위 검문소를 촘촘히 세우는 거예요.", "N2SF rebuilds the bridge, but lines it with checkpoints, one after another."),
         "small": ("중요도별로 성 등급도 나눠서, 등급에 맞게 통제 수준을 다르게 해요.", "Castles are also graded by how critical they are, with controls matched to each grade."),
         "tricks": (4, [
             (icon('<circle cx="32" cy="24" r="16" fill="none" stroke="var(--bad)" stroke-width="4"/>' + label(32, 29, "1", 14, "var(--bad)", cls="d")),
              ("등급별로 성을 나눠요", "Castles are graded"), ("중요도에 따라 통제 수준이 달라요", "control level matches how critical it is"), "warm"),
             (icon('<path d="M10 40 h44" stroke="#8B5E3C" stroke-width="6"/><path d="M22 40 V26 L32 16 L42 26 V40" fill="var(--good)"/>'),
              ("다리는 놓되 검문소 촘촘히", "Bridge rebuilt, checkpoints everywhere"), ("구간마다 다시 확인해요", "re-checked section by section"), "calm"),
             (icon('<ellipse cx="20" cy="36" rx="16" ry="11" fill="none" stroke="var(--accent)" stroke-width="3"/><ellipse cx="40" cy="30" rx="18" ry="13" fill="none" stroke="var(--accent)" stroke-width="3"/>'),
              ("클라우드도 쓸 수 있게", "Cloud use becomes possible"), ("등급에 맞으면 허용해요", "allowed when it matches the grade")),
             (icon('<circle cx="32" cy="32" r="18" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 24 v8 l6 4" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>'),
              ("계속 지켜봐요", "Watched continuously"), ("한 번 통과가 끝이 아니에요", "passing once isn't the end")),
         ])},
        {"svg": P4, "alt": ("기존 물리적 망분리(다리 끊기, 가장 안전하지만 불편, 클라우드 거의 못 씀) vs N2SF(다리는 열고 구간마다 확인, 제로 트러스트 방식, 클라우드도 사용 가능) 비교", "Old physical separation (bridge cut, safest but least convenient, cloud barely usable) vs N2SF (bridge open but checked section by section, same idea as zero trust, cloud usable) compared"),
         "caption": ("기존 방식과 N2SF는 다리를 다루는 법이 달라요.", "The old way and N2SF handle the bridge differently."),
         "small": ('N2SF의 검문소 방식은 <a href="zerotrust-ko.html">문마다 물어보는 성</a>과 같은 생각이에요.',
                   "N2SF's checkpoint approach is the same idea as the <a href=\"zerotrust-en.html\">castle that always asks</a>.")},
        {"svg": P5, "alt": ("이미 바꾼 작은 성과 아직 그대로인 작은 성이 나란히 있고, 경비가 '등급 나누는 기준부터 어려워요'라고 말함", "A castle that already switched stands beside one that hasn't, while a guard says even grading the castles is hard"),
         "caption": ("아직 초기 단계예요.", "It's still early days."),
         "small": ("모든 공공기관이 다 바꾸진 않았고, 등급 기준도 아직 다듬는 중이에요.", "Not every public-sector castle has switched yet, and the grading criteria themselves are still being refined.")},
    ],
    "summary": (("<b>N2SF</b> = 다리를 <b>아예 끊는</b> 대신, <b>등급별로 성을 나누고</b> 다리 위에 <b>검문소를 촘촘히</b> 세우는 나라의 새 망 보안 틀.",
                 "<b>N2SF</b> = the nation's new network security framework — instead of <b>cutting the bridge entirely</b>, it <b>grades castles by criticality</b> and lines the bridge with <b>checkpoints, one after another</b>."),
                ("N2SF(국가 사이버안보 기본틀, National Network Security Framework)는 국가정보원이 추진하는 공공부문 망 보안체계로, 기존의 물리적 망분리 중심 정책을 등급제와 제로 트러스트 기반의 논리적 망분리로 전환하는 것을 핵심으로 해요. 업무 중요도에 따라 보안 등급을 나누고, 등급에 맞는 통제를 적용해 공공기관도 클라우드 등 외부 서비스를 활용할 수 있게 하는 게 목표예요.",
                 "N2SF is a public-sector network security framework led by South Korea's National Intelligence Service, shifting the country's traditional physical network-separation policy toward a grade-based, zero-trust-driven logical separation. Systems are graded by how critical their work is, with controls matched to each grade, aiming to let public institutions use cloud and other outside services while still staying protected.")),
    "glossary": [
        ("N2SF", "N2SF", ("나라의 새 망 보안 틀.", "The nation's new network security framework."), ("국가정보원이 추진하는 공공부문 망 보안체계예요.", "A public-sector framework led by Korea's National Intelligence Service.")),
        ("물리적 망분리", "Physical network separation", ("다리를 아예 끊기.", "Cutting the bridge entirely."), ('기존 방식. → <a href="airgap-ko.html">다리 없는 섬 창고</a>', 'The old approach. → <a href="airgap-en.html">the island shed with no bridge</a>')),
        ("논리적 망분리", "Logical network separation", ("다리는 열되 검문소로.", "Bridge open, but checkpointed."), ("물리적으로 끊지 않고, 접근을 통제해서 같은 효과를 내요.", "No physical cut — access control achieves a similar effect.")),
        ("등급제", "Grading system", ("성마다 매긴 등급.", "A grade assigned to each castle."), ("업무 중요도에 따라 1~3등급처럼 나누고, 등급별로 통제 수준이 달라요.", "Systems are graded, roughly 1 to 3, by how critical their work is, with controls matched to each.")),
        ("제로 트러스트 기반", "Zero-trust based", ("문마다 다시 물어봐요.", "Every door asks again."), ('N2SF의 검문소 방식이 기대는 생각이에요. → <a href="zerotrust-ko.html">문마다 물어보는 성</a>', "The idea N2SF's checkpoints lean on. → <a href=\"zerotrust-en.html\">the castle that always asks</a>")),
        ("공공 클라우드 이용", "Public-sector cloud use", ("등급에 맞으면 허용.", "Allowed when it matches the grade."), ("물리적 망분리 아래선 거의 불가능했던 일이에요.", "Something that was nearly impossible under physical separation.")),
        ("상시 모니터링", "Continuous monitoring", ("계속 지켜보기.", "Watching continuously."), ("검문소를 한 번 통과했다고 끝이 아니에요.", "Passing a checkpoint once isn't the end of the watching.")),
        ("단계적 전환", "Phased rollout", ("아직 다 바뀌진 않았어요.", "Not everything has switched yet."), ("기관마다, 등급 기준 자체도 계속 다듬는 중이에요.", "It varies by institution, and the grading criteria themselves are still being refined.")),
    ],
}
