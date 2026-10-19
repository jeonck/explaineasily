"""디지털 포렌식·증거수집 — 법적 절차(적법성·증거능력) 관점. 기술적 보존·분석은 security/forensics 쪽."""
from _draw import *
from _world import *

PERMIT_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M26 18 h12 v10 l-6 6 l-6 -6z" fill="var(--accent)"/><path d="M22 40 h20 M22 46 h12" stroke="#142033" stroke-width="2"/>')
SCOPE_I = icon('<rect x="10" y="10" width="44" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/><rect x="22" y="22" width="20" height="20" rx="3" fill="var(--good)"/>')
WITNESS_I = icon('<circle cx="22" cy="24" r="9" fill="var(--good)"/><rect x="12" y="36" width="20" height="18" rx="4" fill="var(--good)"/><circle cx="46" cy="24" r="9" fill="var(--accent)"/><rect x="36" y="36" width="20" height="18" rx="4" fill="var(--accent)"/>')
CHAIN_I = icon('<circle cx="16" cy="20" r="8" fill="none" stroke="var(--ink)" stroke-width="4"/><circle cx="32" cy="32" r="8" fill="none" stroke="var(--ink)" stroke-width="4"/><circle cx="48" cy="44" r="8" fill="none" stroke="var(--ink)" stroke-width="4"/><path d="M22 24 l6 4 M38 36 l6 4" stroke="var(--ink)" stroke-width="3"/>')

# 1. 조사 위원이 당장 휴대폰부터 가져가려 해요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=EYES, **TEACHER) + bubble(130, 70, 240, 40, "⟦휴대폰 당장 압수할게요!|hand over the phone right now!⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.8, face=SWEAT + EYES, **STUDENT) + bubble(460, 70, 230, 44, "⟦그냥 가져가셔도 돼요?|can you really just take it like that?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦조사 위원이 당장 휴대폰부터 가져가려 해요|an investigator wants to grab the phone right away⟧", 13, "var(--ink)", cls="d"))

# 2. 절차 없이 가져가면 나중에 다 무효가 돼요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=FROWN, **PRESIDENT) + bubble(130, 70, 250, 44, "⟦허락도 없이 가져간 거라 못 써요|it was taken without permission — it can't be used⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(570, 150, s=0.75, face=SWEAT + EYES, **TEACHER) + label(570, 250, "⟦분명 진짜 증거였는데…|but it really was the real evidence…⟧", 11, "var(--bad)")
         + label(380, 285, "⟦제대로 된 절차 없이 가져가면, 나중에 증거로 못 써요|take it without proper procedure, and it can't be used as evidence later⟧", 12, "var(--ink)", cls="d"))

# 3. 법적 증거수집 절차 = 권한 받고, 범위 정하고, 입회하고, 기록하는 것 (hero)
P3 = svg(360, sky(360)
         + label(380, 26, "⟦법적 증거수집 절차 = 권한 받고 범위 정해 입회 아래 기록하며 거두는 것|legal evidence collection = get permission, set the scope, collect it with a witness, and keep a record⟧", 13, "var(--ink)", cls="d")
         + person(140, 140, s=0.9, face=EYES, **TEACHER)
         + rulesboard(250, 70, 300, 240, "⟦절차 네 가지|THE FOUR STEPS⟧",
                      ("⟦1. 선생님 허락서(영장격) 먼저|1. permission slip first (like a warrant)⟧",
                       "⟦2. 꼭 필요한 것만(범위 한정)|2. only what's needed (limited scope)⟧",
                       "⟦3. 학생 입회 아래 수거|3. collected with the student present⟧",
                       "⟦4. 누가·언제 받았는지 기록|4. record who took it, and when⟧"), 0.95)
         + person(640, 160, s=0.8, face=EYES, **STUDENT)
         + label(380, 335, "⟦기술로 보존하는 것과는 다른, '정당하게 얻었는가'의 문제예요|different from preserving it technically — this is about whether it was obtained lawfully⟧", 11, "var(--muted)"))

# 4. 절차를 지켰을 때 vs 안 지켰을 때
P4 = svg(320, sky(320, ground=False)
         + rulesboard(50, 40, 320, 230, "⟦절차를 지켰을 때|FOLLOWED THE PROCEDURE⟧", ("⟦위원회가 증거로 인정해요|the committee accepts it as evidence⟧", "⟦학생도 결과에 승복하기 쉬워요|the student finds it easier to accept the result⟧"), 1.0)
         + rulesboard(400, 40, 320, 230, "⟦절차를 안 지켰을 때|SKIPPED THE PROCEDURE⟧", ("⟦\"위법하게 얻었다\"며 증거가 빠져요|thrown out as \"unlawfully obtained\"⟧", "⟦진짜였어도 못 써서 사건 전체가 흔들려요|even if real, it can't be used — the whole case wobbles⟧"), 1.0)
         + label(380, 295, "⟦내용이 진짜인가와, 정당하게 얻었는가는 서로 다른 질문이에요|is it real? and was it lawfully obtained? are two different questions⟧", 11, "var(--ink)", cls="d"))

# 5. 절차를 지켜도 내용 판단은 또 다른 문제예요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **PRESIDENT) + label(190, 250, "⟦절차는 지켰으니 증거로 받아들여요|the procedure was followed, so it's admitted⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=EYES, **TEACHER) + label(570, 250, "⟦근데 이게 무슨 뜻인지는 또 따져봐야죠|but what it actually means still needs figuring out⟧", 11, "var(--ink)")
         + label(380, 285, "⟦정당하게 얻었다고 해서 결론까지 저절로 정해지진 않아요|lawfully obtained doesn't mean the conclusion is automatic⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "forensiclaw", "order": 16,
    "title": ("정당하게 거뒀는가를 따지는 절차", "The Procedure That Checks Whether It Was Lawfully Taken"),
    "h1": ("<em>디지털 증거수집의 법적 절차</em>가 뭐예요?", "What are the <em>Legal Procedures for Digital Evidence Collection</em>?"),
    "sub": ("디지털 증거수집의 법적 절차를, 학교 조사위원회가 휴대폰을 함부로 가져가지 않고 허락·범위·입회·기록을 갖춰 거두는 이야기로 풀어봤어요.",
            "The legal procedures for collecting digital evidence, told as a story about a school investigation committee that never just grabs a phone — it gets permission, limits the scope, collects it with a witness, and keeps a record."),
    "panels": [
        {"svg": P1, "alt": ("선생님이 당장 휴대폰을 압수하겠다 하고, 학생은 그냥 가져가도 되냐고 땀 흘리며 되물음", "A teacher demands the phone be handed over immediately; a sweating student asks if that's really allowed"),
         "caption": ("조사 위원이 당장 휴대폰부터 가져가려 해요.", "An investigator wants to grab the phone right away."),
         "small": ("급하다고 그냥 가져가도 되는 걸까요?", "Is grabbing it right away, just because it's urgent, really okay?")},
        {"svg": P2, "alt": ("학생회장이 허락 없이 가져간 거라 못 쓴다고 말하고, 선생님은 진짜 증거였는데 하며 땀 흘림", "The council president says it can't be used because it was taken without permission; the teacher sweats, insisting it really was the evidence"),
         "caption": ("절차 없이 가져가면 나중에 다 무효가 돼요.", "Take it without proper procedure, and it all becomes invalid later."),
         "small": ("제대로 된 절차 없이 가져가면, 나중에 증거로 못 써요.", "Take it without proper procedure, and it can't be used as evidence later.")},
        {"svg": P3, "hero": True, "alt": ("선생님이 허락서·범위·입회·기록 네 단계가 적힌 절차표를 들고, 학생이 그 옆에서 지켜봄", "A teacher holds up a four-step procedure board — permission, scope, witness, record — while a student looks on"),
         "caption": ("법적 증거수집 절차는 권한 받고, 범위 정하고, 입회하고, 기록하는 것이에요.", "Legal evidence collection means getting permission, setting the scope, collecting it with a witness, and keeping a record."),
         "small": ("기술로 보존하는 것과는 다른, '정당하게 얻었는가'의 문제예요.", "Different from preserving it technically — this is about whether it was obtained lawfully."),
         "tricks": (4, [
             (PERMIT_I, ("허락서 먼저", "Get permission first"), ("영장과 같은 역할이에요", "plays the same role as a warrant"), "warm"),
             (SCOPE_I, ("범위 한정하기", "Limit the scope"), ("꼭 필요한 것만 거둬요", "collects only what's needed")),
             (WITNESS_I, ("입회 아래 거두기", "Collect with a witness"), ("몰래 거두지 않아요", "never collected in secret")),
             (CHAIN_I, ("누가·언제 기록", "Record who, and when"), ("관리 연속성을 남겨요", "keeps the chain of custody"), "calm"),
         ])},
        {"svg": P4, "alt": ("왼쪽 기준표는 절차를 지켜 증거가 받아들여지는 경우, 오른쪽은 절차를 어겨 위법하게 얻었다며 증거가 빠지는 경우를 비교함", "Left board: procedure followed, evidence accepted. Right board: procedure skipped, evidence thrown out as unlawfully obtained"),
         "caption": ("절차를 지켰을 때와 안 지켰을 때는 이렇게 갈려요.", "Following the procedure or not makes this much difference."),
         "small": ("내용이 진짜인가와, 정당하게 얻었는가는 서로 다른 질문이에요.", "Is it real? and was it lawfully obtained? are two different questions.")},
        {"svg": P5, "alt": ("왼쪽: 학생회장이 절차를 지켰으니 증거로 받아들인다고 말함. 오른쪽: 선생님이 내용의 의미는 또 따져봐야 한다고 말함", "Left: the president says it's admitted since procedure was followed. Right: the teacher says what it means still needs figuring out"),
         "caption": ("절차를 지켜도 내용 판단은 또 다른 문제예요.", "Even with procedure followed, judging the content is a separate matter."),
         "small": ("정당하게 얻었다고 해서 결론까지 저절로 정해지진 않아요.", "Lawfully obtained doesn't mean the conclusion is automatic.")},
    ],
    "summary": (("<b>디지털 증거수집의 법적 절차</b> = <b>권한(영장)</b>을 받고 <b>범위를 한정</b>해, <b>당사자 참여</b> 아래 <b>관리 연속성을 기록</b>하며 거둬서, 나중에 증거로 인정받게(증거능력) 하는 일.",
                 "<b>Legal digital evidence procedure</b> = obtaining <b>authorization (a warrant)</b>, keeping the <b>scope limited</b>, collecting it with the <b>affected party present</b>, and <b>documenting the chain of custody</b> — so it later counts as admissible evidence."),
                ("디지털 증거수집은 기술적 보존(이미징·해시)과는 별개로, 압수수색영장 등 적법한 권한 안에서, 필요 최소 범위로, 당사자의 참여권을 보장하며 수행되어야 해요. 이 요건을 어기면 '위법수집증거배제법칙'에 따라 내용이 진짜라도 법정에서 증거능력이 부정될 수 있어요. 관리 연속성(chain of custody)이 끊기지 않게 문서화하는 것도 핵심 요건이에요.",
                 "Separate from technical preservation (imaging, hashing), digital evidence collection must be carried out under lawful authority (such as a search warrant), limited to the minimum necessary scope, and with the affected party's right to be present respected. Violating these requirements can make even genuine evidence inadmissible in court under the exclusionary rule for unlawfully obtained evidence. Documenting an unbroken chain of custody is also a core requirement.")),
    "glossary": [
        ("적법절차", "Due Process", ("정해진 순서를 제대로 밟는 것.", "Properly following the set sequence of steps."), ("순서를 건너뛰면 결과가 무효가 될 수 있어요.", "Skip a step, and the result can be voided.")),
        ("증거능력", "Admissibility of Evidence", ("법정(위원회)이 증거로 받아줄 자격.", "Whether a court (or committee) will accept it as evidence at all."), ("내용이 맞고 틀리고와는 다른 문제예요.", "A separate question from whether the content is true.")),
        ("위법수집증거배제법칙", "Exclusionary Rule", ("잘못 거둔 증거는 진짜여도 못 쓰는 원칙.", "The rule that improperly collected evidence can't be used, even if genuine."), ("절차가 왜 중요한지의 핵심 이유예요.", "The core reason procedure matters so much.")),
        ("압수수색영장", "Search Warrant", ("학교의 허락서 같은 공식 권한.", "An official authorization, like the school's permission slip."), ("권한 없이 거두면 처음부터 무효예요.", "Collect without it, and it's invalid from the start.")),
        ("참여권", "Right to Be Present", ("당사자가 몰래가 아니라 지켜보며 입회하는 권리.", "The right to witness collection, not have it happen in secret."), ("나중에 \"몰래 조작했다\"는 의심을 막아줘요.", "Prevents later claims of secret tampering.")),
        ("관리연속성", "Chain of Custody", ("누가 언제 받아 누구에게 넘겼는지 기록.", "A record of who held it, and handed it to whom, when."), ('기술적으로 굳히는 작업과 짝을 이뤄요. → <a href="forensics-ko.html">발자국을 굳혀서 보관하기</a>', 'Pairs with the technical side of setting evidence in place. → <a href="forensics-en.html">setting the footprint in plaster</a>')),
        ("비례원칙", "Principle of Proportionality", ("필요한 만큼만 거두고, 더는 건드리지 않는 것.", "Collecting only as much as needed, and no more."), ("사생활 보호와 조사 필요성 사이의 균형이에요.", "Balances privacy against the need to investigate.")),
        ("디지털 포렌식(기술적 보존)", "Digital Forensics (Technical Preservation)", ("증거를 그대로 굳혀 분석하는 기술 작업.", "The technical work of setting and analyzing evidence untouched."), ('이 페이지는 법적 절차만, 보존·분석 기법은 다른 페이지에서. → <a href="forensics-ko.html">발자국을 굳혀서 보관하기</a>', 'This page covers only legal procedure — preservation technique lives elsewhere. → <a href="forensics-en.html">setting the footprint in plaster</a>')),
    ],
}
