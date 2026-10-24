"""오픈소스 소프트웨어와 라이선스."""
from _draw import *
from _world import *

FREE_I = icon('<rect x="12" y="24" width="40" height="28" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 24 v-6 a10 10 0 0 1 20 0" stroke="var(--good)" stroke-width="4" fill="none"/><path d="M26 36 l5 5 l10 -10" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>')
CREDIT_I = icon('<rect x="14" y="16" width="36" height="32" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="25" cy="30" r="5" fill="var(--accent)"/><path d="M35 26 h11 M35 34 h11" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
SHARE_I = icon('<path d="M14 32 h20" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/><path d="M28 24 l11 8 l-11 8z" fill="var(--accent)"/><rect x="44" y="19" width="14" height="26" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>')
NOCLAIM_I = icon('<circle cx="32" cy="32" r="21" fill="none" stroke="var(--bad)" stroke-width="4"/><path d="M19 19 L45 45 M45 19 L19 45" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>')


def box(x, y, w, h):
    return (f'<rect x="{x}" y="{y - 10}" width="{w}" height="10" rx="4" fill="#5A3B22"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{WOOD}"/>')


# 1. 학생회 — 공용 준비물 상자에 아직 라벨이 없어요
P1 = svg(300, sky(300)
         + label(380, 24, "⟦여기, 학생회 — 학교의 규칙과 표준을 정하는 곳이에요|Here at the student council, where the school's rules and standards get made⟧", 11, "var(--muted)", cls="d")
         + '<rect x="330" y="50" width="12" height="40" rx="4" fill="var(--accent)"/><rect x="368" y="50" width="12" height="40" rx="4" fill="var(--good)"/><rect x="406" y="50" width="12" height="40" rx="4" fill="var(--bad)"/>'
         + box(290, 90, 180, 70)
         + person(150, 150, s=0.85, face=EYES, **STUDENT) + bubble(60, 70, 190, 40, "⟦이거 막 복사해도 돼요?|can I just copy this freely?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.85, face=FROWN, **REP) + bubble(470, 70, 220, 40, "⟦다시 나눠줄 땐 뭘 지켜야 해요?|what do I follow when I pass it on?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦공용 준비물 상자에 아직 규칙 라벨이 없어요|the shared supply box has no rule tag yet⟧", 13, "var(--ink)", cls="d"))

# 2. 라벨이 없으면 서로 다르게 알아들어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **STUDENT) + bubble(140, 70, 210, 40, "⟦제가 만든 거예요! (사실 베꼈어요)|I made this! (actually copied it)⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **REP) + bubble(460, 70, 230, 40, "⟦근데 출처가 하나도 없는데요?|but there's no credit anywhere⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦규칙이 없으면 누가 만들었는지도, 뭘 지켜야 하는지도 몰라요|without rules, nobody knows who made it or what to follow⟧", 12, "var(--ink)", cls="d"))

# 3. 오픈소스 라이선스 = 공용 준비물에 붙이는 규칙 라벨 (hero)
P3 = svg(340, sky(340)
         + label(380, 30, "⟦오픈소스 라이선스 = 공용 준비물에 붙이는 규칙 라벨|Open-source license = the rule tag on shared supplies⟧", 14, "var(--ink)", cls="d")
         + person(170, 130, s=0.9, face=EYES, **PRESIDENT)
         + box(300, 150, 160, 80) + suppliestag(380, 150, 1.4)
         + person(560, 140, s=0.8, face=SMILE, **REP)
         + label(380, 320, "⟦자유롭게 쓰되, 라벨에 적힌 대로 지켜야 해요|free to use, but only by what the tag says⟧", 12, "var(--muted)"))

# 4. 두 종류의 라벨
P4 = svg(320, sky(320, ground=False)
         + rulesboard(40, 40, 320, 240, "⟦허용적 라이선스 (MIT 등)|PERMISSIVE (MIT, etc.)⟧",
                      ("⟦그냥 써도 돼요|just use it⟧", "⟦출처만 적으면 끝|just credit the source⟧", "⟦다시 나눠줄 때 비공개도 OK|can keep the new version closed⟧"), 1.0)
         + rulesboard(400, 40, 320, 240, "⟦카피레프트 (GPL)|COPYLEFT (GPL)⟧",
                      ("⟦자유롭게 써도 돼요|free to use too⟧", "⟦근데 고쳐서 나눠줄 땐|but when you reshare a fix⟧", "⟦너도 소스를 공개해야 해요|you must open your source too⟧"), 1.0)
         + label(380, 300, "⟦섞어 쓰면 규칙이 충돌할 수 있어요 — 조합을 꼭 확인해요|mixing them can clash — always check the combination⟧", 12, "var(--ink)", cls="d"))

# 5. 라벨은 법적 효력이 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 140, s=0.8, face=FROWN, **STUDENT) + gavel(190, 215, 0.9)
         + label(190, 260, "⟦규칙을 어기면 못 쓰게 돼요|break it, and you lose the right to use it⟧", 11, "var(--bad)")
         + person(570, 140, s=0.8, face=SMILE, **REP) + checkmachine(570, 215, 0.9)
         + label(570, 260, "⟦재료표로 어떤 라벨이 섞였는지 추적해요|a parts list tracks which tags got mixed in⟧", 11, "var(--good)")
         + label(380, 285, "⟦라벨은 법적 효력이 있어요 — 추적 도구는 다른 세계에도 있어요|the tag has legal force — a tracking tool exists in another world too⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "osslicense", "order": 1,
    "title": ("다 같이 쓰는 준비물 규칙 라벨", "The Rule Tag on Shared Supplies"),
    "h1": ("<em>오픈소스 라이선스</em>가 뭐예요?", "What is an <em>Open-Source License</em>?"),
    "sub": ("오픈소스 라이선스를, 학생회가 공용 준비물에 붙이는 규칙 라벨 이야기로 풀어봤어요.",
            "Open-source licenses, told as a story about the rule tag the student council puts on shared supplies."),
    "panels": [
        {"svg": P1, "alt": ("학생회 공용 준비물 상자에 라벨이 없어 학생들이 궁금해함", "The student council's shared supply box has no tag, and students are confused"),
         "caption": ("학생회는 학교 규칙과 표준을 정하는 곳이에요.", "The student council is where the school's rules and standards get made."),
         "small": ("공용 준비물 상자에 아직 규칙 라벨이 없어요.", "The shared supply box has no rule tag yet.")},
        {"svg": P2, "alt": ("한 학생은 베낀 걸 자기 것이라 하고, 다른 학생은 출처가 없다고 지적함", "One student claims a copy as their own; another points out there's no credit"),
         "caption": ("라벨이 없으면 서로 다르게 알아들어요.", "Without a tag, everyone understands it differently."),
         "small": ("규칙이 없으면 누가 만들었는지도, 뭘 지켜야 하는지도 몰라요.", "Without rules, nobody knows who made it or what to follow.")},
        {"svg": P3, "hero": True, "alt": ("학생회장이 공용 준비물 상자에 규칙 라벨을 붙임", "The student council president puts a rule tag on the shared supply box"),
         "caption": ("오픈소스 라이선스는 공용 준비물에 붙이는 규칙 라벨이에요.", "An open-source license is the rule tag on shared supplies."),
         "small": ("자유롭게 쓰되, 라벨에 적힌 대로 지켜야 해요.", "Free to use — but only by what the tag says."),
         "tricks": (4, [
             (FREE_I, ("자유롭게 쓰기", "Free to use"), ("복제·수정·배포 허용", "copy, modify, redistribute"), "calm"),
             (CREDIT_I, ("출처는 꼭 밝히기", "Always credit it"), ("만든 사람 이름을 남겨요", "keep the maker's name"), "warm"),
             (SHARE_I, ("다시 나눌 땐 라벨대로", "Reshare by the tag"), ("라벨마다 규칙이 달라요", "each tag's rule differs")),
             (NOCLAIM_I, ("내 것인 척 하지 않기", "Don't claim it as yours"), ("저작권 표시는 그대로", "copyright notice stays")),
         ])},
        {"svg": P4, "alt": ("허용적 라이선스와 카피레프트 라이선스를 나란히 비교한 규칙판 두 개", "Two rule boards comparing permissive and copyleft licenses side by side"),
         "caption": ("라벨은 크게 두 종류예요.", "Tags come in two broad kinds."),
         "small": ("섞어 쓰면 규칙이 충돌할 수 있어요 — 조합을 꼭 확인해요.", "Mixing them can clash — always check the combination.")},
        {"svg": P5, "alt": ("왼쪽: 규칙을 어겨 혼나는 학생. 오른쪽: 자동 검사기로 라벨을 추적하는 대표", "Left: a student scolded for breaking the rule. Right: a rep tracking tags with an automatic checker"),
         "caption": ("라벨은 법적 효력이 있어요.", "The tag has legal force."),
         "small": ("규칙을 어기면 못 쓰게 돼요. 재료표로 추적하는 도구는 다른 세계에도 있어요.", "Break it, and you lose the right to use it. A tracking tool exists in another world too.")},
    ],
    "summary": (("<b>오픈소스 라이선스</b> = 공용 준비물에 붙이는 <b>규칙 라벨</b>. 자유롭게 쓰되, 라벨이 정한 대로 출처를 밝히고 다시 나눠줄 때의 규칙을 지켜야 해요.",
                 "<b>Open-source license</b> = the <b>rule tag</b> on shared supplies. Free to use, but you must credit the source and follow the tag's rule when you pass it on."),
                ("오픈소스 라이선스는 소스코드의 이용·수정·배포 조건을 정한 법적 문서예요. MIT/BSD/Apache처럼 조건이 가벼운 '허용적(permissive) 라이선스'와, GPL처럼 수정본도 같은 조건으로 공개해야 하는 '카피레프트(copyleft) 라이선스'로 크게 나뉘어요. 라이선스를 어기면 저작권 침해로 법적 책임을 질 수 있어요.",
                 "Open-source licenses are legal terms governing how source code may be used, modified, and redistributed. They range from lightweight 'permissive' licenses like MIT/BSD/Apache to 'copyleft' licenses like GPL, which require derivative works to be released under the same terms. Breaking a license can mean legal liability for copyright infringement.")),
    "glossary": [
        ("오픈소스", "Open Source", ("소스코드를 공개해 자유롭게 쓰고 고치게 하는 것.", "Publishing source code so anyone can use and change it."), ("다만 '자유'의 범위는 라이선스마다 달라요.", "But how free depends on which license.")),
        ("카피레프트", "Copyleft (e.g. GPL)", ("고치면 너도 공개해야 하는 라벨.", "The tag that says: fix it, and you must open it too."), ("섞어 쓰면 전체가 공개 대상이 될 수 있어요(전염성).", "Mix it in, and the whole thing may have to open up too.")),
        ("허용적 라이선스", "Permissive License (MIT/BSD/Apache)", ("출처만 적으면 자유로운 라벨.", "The tag that's free as long as you credit it."), ("독점 소프트웨어에 섞어도 괜찮아요.", "Safe to mix into closed, proprietary software.")),
        ("라이선스 호환성", "License Compatibility", ("서로 다른 라벨을 섞어도 되는지.", "Whether two different tags can be mixed."), ("섞으면 안 되는 조합도 있어요.", "Some combinations simply can't be mixed.")),
        ("고지 의무", "Attribution / Notice Obligation", ("누가 만들었는지 꼭 적기.", "Always writing down who made it."), ("라벨 대부분이 요구하는 최소 조건이에요.", "The minimum almost every tag asks for.")),
        ("SBOM", "SBOM (Software Bill of Materials)", ("어떤 재료(코드)가 들어갔는지 적은 재료표.", "The parts list of which code went in."), ('라이선스 추적도 여기 포함돼요. → <a href="sbom-ko.html">성의 재료표</a>', 'License tracking is part of it too. → <a href="sbom-en.html">the castle\'s parts list</a>')),
        ("저작권", "Copyright", ("원래 만든 사람의 권리.", "The original maker's right."), ("오픈소스도 저작권은 그대로 있어요 — 포기한 게 아니에요.", "Open source doesn't give up copyright — it's still there.")),
        ("이중 라이선스", "Dual Licensing", ("공짜 라벨과 유료 라벨을 둘 다 붙이는 것.", "Putting both a free tag and a paid tag on the same thing."), ("무료로 쓰거나, 돈 내고 다른 조건으로 쓰거나 고를 수 있어요.", "Use it free under one tag, or pay for different terms.")),
    ],
}
