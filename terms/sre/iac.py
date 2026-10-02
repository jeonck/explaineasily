from _draw import *
from _world import *

# 1. 새 공원을 지을 때마다, 사람이 기억에 의존해 하나씩 지어요
P1 = svg(300, sky(300)
         + ride(220, 260, 0.9, color="var(--accent)")
         + person(340, 260 - 112 * 0.6, s=0.6, face=EYES, extra=CLIPBOARD, **MECHANIC)
         + bubble(380, 80, 230, 56, "⟦음... 저번엔 어떻게 지었더라...|hmm... how did I build it last time...⟧", 11, "var(--panel)", "var(--line)", "left")
         + label(380, 282, "⟦새 공원을 지을 때마다, 사람이 기억에 의존해 하나씩 지어요|every time a new park goes up, someone builds it from memory, one at a time⟧", 12, "var(--ink)"))

# 2. 왜 어려운가: 손으로 지으면 사람마다 다르고, 기록도 안 남아요
P2 = svg(320, '<rect width="760" height="320" fill="var(--bad-soft)"/>'
         + label(210, 36, "⟦도시 A 공원|City A Park⟧", 12, "var(--muted)")
         + ride(170, 240, 0.75, color="var(--accent)") + booth(265, 240, 0.5)
         + label(210, 295, "⟦창구 있음|has a booth⟧", 11, "var(--ink)")
         + label(590, 36, "⟦도시 B 공원|City B Park⟧", 12, "var(--muted)")
         + ride(590, 240, 0.75, color="var(--accent)")
         + label(590, 295, "⟦창구 없음?|no booth?⟧", 11, "var(--bad)", cls="d")
         + person(400, 240 - 112 * 0.5, s=0.5, face=FROWN + SWEAT, extra=CLIPBOARD, **MECHANIC)
         + bubble(320, 100, 220, 55, "⟦손으로 지으면 사람마다 달라요...|build it by hand, and it turns out different each time...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 312, "⟦손으로 지으면 사람마다 다르고, 기록도 안 남아요|build it by hand, and it differs person to person, with no record of how⟧", 12, "var(--ink)"))

# 3. hero: 설계도 한 장(코드)만 있으면, 어디서든 똑같은 공원을 지을 수 있어요
P3 = svg(340, sky(340)
         + board(30, 30, 230, 170, "⟦설계도(코드)|BLUEPRINT (CODE)⟧", ("⟦기구: 주황 1개|ride: orange x1⟧", "⟦창구: 1개|booth: x1⟧", "⟦대기줄: 4명|queue: 4⟧"), 1.0)
         + '<path d="M265 90 Q380 60 470 110" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + '<path d="M265 150 Q380 200 470 250" fill="none" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4"/>'
         + ride(520, 120, 0.5, color="var(--accent)") + booth(590, 120, 0.35) + label(555, 165, "⟦도시 A|City A⟧", 11, "var(--muted)")
         + ride(520, 260, 0.5, color="var(--accent)") + booth(590, 260, 0.35) + label(555, 305, "⟦도시 B|City B⟧", 11, "var(--muted)")
         + label(380, 20, "⟦설계도 한 장만 있으면, 어디서든 똑같은 공원을 지을 수 있어요|with just one blueprint, you can build the exact same park anywhere⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦사람이 아니라 설계도가 정답이에요|the blueprint is the source of truth, not any one person⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 설계도 한 장 → 다른 사람이 지어도 결과는 똑같아요
P4 = svg(320, sky(320)
         + board(20, 40, 170, 170, "⟦설계도|BLUEPRINT⟧", ("⟦기구: 주황 1개|ride: orange x1⟧", "⟦창구: 1개|booth: x1⟧", "⟦대기줄: 4명|queue: 4⟧"), 1.0)
         + label(225, 155, "=", 40, "var(--muted)", cls="d")
         + label(330, 160, "✓", 22, "var(--good)", cls="d") + ride(330, 250, 0.55, color="var(--accent)") + booth(400, 260, 0.4) + label(365, 305, "⟦도시 A|City A⟧", 11, "var(--muted)")
         + label(560, 160, "✓", 22, "var(--good)", cls="d") + ride(560, 250, 0.55, color="var(--accent)") + booth(630, 260, 0.4) + label(595, 305, "⟦도시 B|City B⟧", 11, "var(--muted)")
         + label(380, 20, "⟦같은 설계도를 읽으면, 다른 사람이 지어도 똑같이 나와요|read the same blueprint, and even a different builder gets the identical result⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 몰래 손으로 고치면 설계도와 실제가 달라져요(드리프트)
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + board(50, 30, 260, 110, "⟦설계도|BLUEPRINT⟧", ("⟦기구: 1개|ride: x1⟧",), 1.0)
         + ride(190, 230, 0.6, color="var(--accent)")
         + label(190, 265, "⟦설계도대로예요|matches the blueprint⟧", 11, "var(--ink)")
         + ride(500, 230, 0.55, color="var(--accent)")
         + person(575, 230 - 112 * 0.5, s=0.5, face=SMILE, hat=None, shirt="#7B3FA0", extra=WRENCH)
         + ride(650, 230, 0.5, color="#5B8DEF")
         + bubble(460, 100, 220, 50, "⟦몰래 하나 더 지었어요|secretly built one more⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(575, 265, "⟦실제는 2개 — 설계도와 달라요|reality has 2 — it no longer matches⟧", 11, "var(--bad)", cls="d")
         + label(380, 282, "⟦몰래 손으로 고치면 설계도와 실제가 달라져요(드리프트)|secretly hand-edit it, and the blueprint no longer matches reality (drift)⟧", 12, "var(--ink)"))

CODE_I = icon('<rect x="10" y="8" width="44" height="48" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 20 h20 M18 28 h26 M18 36 h14 M18 44 h22" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>')
CLONE_I = icon('<rect x="6" y="20" width="20" height="24" rx="3" fill="var(--accent)"/><rect x="38" y="20" width="20" height="24" rx="3" fill="var(--accent)"/><path d="M28 30 h8 M28 36 h8" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>')
HISTORY_I = icon('<circle cx="32" cy="34" r="20" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 20 v14 l10 6" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M20 12 l-6 2 2 -6z" fill="var(--good)"/>')
INSPECT_I = icon('<rect x="8" y="30" width="26" height="20" rx="2" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2"/><path d="M12 36 h18 M12 42 h12" stroke="#142033" stroke-width="2"/><circle cx="44" cy="24" r="11" fill="var(--sky)" fill-opacity="0.5" stroke="var(--stone-dark)" stroke-width="4"/><path d="M52 32 l8 8" stroke="var(--stone-dark)" stroke-width="5" stroke-linecap="round"/>')

PAGE = {
    "slug": "iac", "order": 17,
    "title": ("설계도 한 장으로 공원 통째로 짓기", "Building the Whole Park from One Blueprint"),
    "h1": ("<em>코드형 인프라</em>가 뭐예요?", "What is <em>Infrastructure as Code</em>?"),
    "sub": ("코드형 인프라(IaC)를 설계도 한 장으로 공원을 통째로 짓는 이야기로 풀어봤어요.",
            "Infrastructure as Code, told as a story about building a whole park from a single blueprint."),
    "panels": [
        {"svg": P1, "alt": ("정비사가 기구 하나를 기억에 의존해 짓고, 저번엔 어떻게 지었는지 혼잣말함", "A mechanic builds a ride from memory, muttering about how it was built last time"),
         "caption": ("새 공원을 지을 때마다, 사람이 기억에 의존해 하나씩 지어요.", "Every time a new park goes up, someone builds it from memory, one at a time."),
         "small": ("도시마다 조금씩 다르게 지어져요.", "And it comes out a little different, city to city.")},
        {"svg": P2, "alt": ("도시 A 공원엔 창구가 있고 도시 B 공원엔 창구가 없음. 정비사가 땀을 흘리며 손으로 지으면 사람마다 다르다고 말함", "City A's park has a booth but City B's doesn't; a sweating mechanic says building by hand differs each time"),
         "caption": ("손으로 지으면 사람마다 다르고, 기록도 안 남아요.", "Build it by hand, and it differs person to person, with no record of how."),
         "small": ("도시 A 공원과 도시 B 공원이 미묘하게 달라져요.", "City A's park and City B's park end up subtly different.")},
        {"svg": P3, "hero": True, "alt": ("설계도(코드) 한 장에서 화살표 두 개가 뻗어 나가 도시 A 공원과 도시 B 공원을 각각 짓고, 둘 다 똑같은 기구와 창구를 가짐", "One blueprint (code) sends two arrows out, building City A's park and City B's park, both with the identical ride and booth"),
         "caption": ("설계도 한 장만 있으면, 어디서든 똑같은 공원을 지을 수 있어요.", "With just one blueprint, you can build the exact same park anywhere."),
         "small": ("사람이 아니라 설계도가 정답이에요.", "The blueprint is the source of truth, not any one person."),
         "tricks": (4, [
             (CODE_I, ("설계도를 글로 적어요", "Write the blueprint down"), ("코드로 남겨요", "as code"), "calm"),
             (CLONE_I, ("누구나 같은 공원을 지어요", "Anyone builds the same park"), ("설계도만 있으면요", "with just the blueprint")),
             (HISTORY_I, ("수정 기록이 남아요", "Changes leave a record"), ("언제 뭐가 바뀌었는지요", "what changed, and when"), "warm"),
             (INSPECT_I, ("설계도만 보고도 알아요", "You can tell from the blueprint alone"), ("잘못 지었는지도요", "whether it was built wrong")),
         ])},
        {"svg": P4, "alt": ("설계도 한 장 = 도시 A 공원 = 도시 B 공원. 두 도시 모두 체크 표시와 함께 기구, 창구가 똑같이 지어짐", "One blueprint equals City A's park equals City B's park — both cities show a checkmark, with the identical ride and booth"),
         "caption": ("같은 설계도를 읽으면, 다른 사람이 지어도 똑같이 나와요.", "Read the same blueprint, and even a different builder gets the identical result."),
         "small": ("바뀐 점은 설계도 수정 기록으로 남아요.", "And any change leaves a record in the blueprint's history.")},
        {"svg": P5, "alt": ("왼쪽: 기구 1개로 설계도와 똑같음. 오른쪽: 기구가 몰래 하나 더 생겨 설계도와 실제가 달라짐(드리프트)", "Left: one ride, matching the blueprint. Right: a ride was secretly added, so reality no longer matches the blueprint (drift)"),
         "caption": ("몰래 손으로 고치면 설계도와 실제가 달라져요(드리프트).", "Secretly hand-edit it, and the blueprint no longer matches reality (drift)."),
         "small": ("그러면 설계도를 적어 둔 의미가 없어져요.", "And then there was no point writing the blueprint at all.")},
    ],
    "summary": (("<b>코드형 인프라</b> = 공원 설계도를 <b>종이(코드) 한 장</b>에 적어 두고, 그 설계도만 있으면 <b>누가, 어디서 짓든 똑같은 공원</b>이 나오게 하는 일.",
                 "<b>Infrastructure as Code</b> = writing the park's blueprint down <b>as a single piece of code</b>, so that <b>whoever builds it, wherever</b>, the result is the identical park."),
                ("Infrastructure as Code(IaC). 서버·네트워크 같은 인프라를 선언적 설계도(코드)로 적어 버전 관리하는 방식이에요. 손으로 몰래 바꾸면 설계도와 실제가 어긋나는 드리프트가 생기고, 같은 설계도는 몇 번을 다시 실행해도 같은 결과가 나와야 해요(멱등성). GitOps는 이 설계도 보관함을 유일한 정답으로 삼는 다음 단계예요.",
                 "Writing infrastructure like servers and networks as declarative blueprints (code) and keeping them under version control. A sneaky manual edit causes drift, where reality no longer matches the blueprint, and running the same blueprint again and again should always produce the same result (idempotency). GitOps is the next step — treating that blueprint repository as the one source of truth.")),
    "glossary": [
        ("코드형 인프라", "Infrastructure as Code", ("설계도를 종이 한 장(코드)에 적어 두는 일.", "Writing the blueprint down as a single piece of code."), ("그 설계도만 있으면 누구나 같은 공원을 지어요.", "With just that blueprint, anyone builds the same park.")),
        ("선언적 설계도", "Declarative blueprint", ("\"기구 1개, 창구 1개\" 같은 설계도.", "A blueprint like \"ride x1, booth x1\"."), ("방법이 아니라 원하는 결과만 적어요.", "You write the desired result, not the steps to get there.")),
        ("드리프트", "Drift", ("설계도와 실제가 어긋나는 것.", "Reality no longer matching the blueprint."), ("몰래 손으로 고치면 생겨요.", "Happens when someone secretly hand-edits things.")),
        ("버전 관리", "Version control", ("설계도가 언제 어떻게 바뀌었는지 남기는 일.", "A record of when and how the blueprint changed."), ("누가 뭘 고쳤는지 나중에도 알 수 있어요.", "You can always see later who changed what.")),
        ("재현성", "Reproducibility", ("똑같은 설계도면 똑같은 공원이 나오는 것.", "The same blueprint always producing the same park."), ("도시 A든 도시 B든 결과가 같아요.", "City A or City B, the result is the same.")),
        ("멱등성", "Idempotency", ("설계도를 몇 번 다시 실행해도 결과가 같은 것.", "Running the blueprint again and again gives the same result."), ("두 번 지어도 공원이 두 개가 되진 않아요.", "Run it twice, and you still don't get two parks.")),
        ("GitOps", "GitOps", ("설계도 보관함이 바뀌면 자동으로 공사가 따라오는 방식.", "A way where construction follows automatically when the blueprint changes."), ('설계도를 넣는 것과 짓는 것을 자동으로 이어 붙여요. → <a href="gitops-ko.html">설계도가 바뀌면 자동으로 공사</a>', 'It automatically connects updating the blueprint to building it. → <a href="gitops-en.html">construction that follows the blueprint automatically</a>')),
        ("불변 인프라", "Immutable infrastructure", ("고치지 않고 새로 짓고 헌 걸 버리는 방식.", "Not patching — building new and discarding the old."), ("손으로 고칠 일 자체를 없애서 드리프트를 막아요.", "Removes the chance to hand-edit at all, which prevents drift.")),
    ],
}
