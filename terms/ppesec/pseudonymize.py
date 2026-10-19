from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
GUARD = dict(hat="var(--good)", shirt="var(--good)")


def tag(x, y, s=1.0, text="김민수", color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-34" y="-14" width="68" height="28" rx="6" fill="#FFF8E7" stroke="{color}" stroke-width="2"/>'
            + label(0, 6, text, 13, "#142033", cls="d") + "</g>")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


def vault(x, y, s=1.0, locked=True):
    lk = '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/>' if locked else ""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-24" width="52" height="48" rx="4" fill="var(--night)"/>{lk}</g>'


# 1. 손님 명부에 진짜 이름이 그대로 있어요
P1 = svg(280, sky(280)
         + person(130, 150, s=0.85, face=SMILE, **CLERK)
         + box(260, 60, 300, 160, "⟦손님 명부|GUEST LIST⟧", ("⟦김민수 · 1990.3.2 · 서울 ○○동|Kim · 1990-03-02 · Seoul, OO-dong⟧", "⟦이지은 · 1985.7.9 · 부산 △△동|Lee · 1985-07-09 · Busan, XX-dong⟧"))
         + label(380, 260, "⟦연구팀에 그대로 넘기면 이름까지 다 보여요|hand it straight to a research team and even names show⟧", 13, "var(--ink)"))

# 2. 이름만 지워도 다시 알아낼 수 있어요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + box(60, 50, 300, 160, "⟦손님 명부(이름 지움)|GUEST LIST (name removed)⟧", ("⟦●●● · 1990.3.2 · 서울 ○○동|●●● · 1990-03-02 · Seoul, OO-dong⟧", "⟦●●● · 1985.7.9 · 부산 △△동|●●● · 1985-07-09 · Busan, XX-dong⟧"))
         + person(500, 130, s=0.85, face=EYES)
         + bubble(440, 40, 260, 46, "⟦그 동네에 그 생일인 사람, 한 명뿐인데요?|only one person in that dong was born that day⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦다른 단서를 모으면 다시 알아내요 — 재식별이에요|other clues put the name back — that's re-identification⟧", 13, "var(--ink)"))

# 3. 가명처리 = 번호표로 바꿔 달고, 연결표는 따로 잠긴 금고에 (hero)
P3 = svg(340, sky(340)
         + box(40, 50, 260, 150, "⟦손님 명부|GUEST LIST⟧", ("⟦A017 · 1990.3.2 · 서울|A017 · 1990-03-02 · Seoul⟧", "⟦A038 · 1985.7.9 · 부산|A038 · 1985-07-09 · Busan⟧"), 11)
         + tag(220, 230, 0.9, "A017") + tag(380, 230, 0.9, "A038")
         + '<path d="M330 150 L470 150" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 6"/>'
         + vault(560, 110, 1.1) + label(560, 150, "⟦연결표 금고|the key-table vault⟧", 12, "var(--muted)")
         + label(560, 170, "⟦A017 = 김민수|A017 = Kim⟧", 11, "var(--ink)", cls="d")
         + person(660, 150, s=0.8, face=EYES, **GUARD)
         + label(380, 30, "⟦가명처리 = 번호표로 바꿔 달고, 진짜 이름표는 다른 금고에|pseudonymization = swap in a number tag; the real name goes in a separate vault⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦금고 열쇠가 따로 있어야 다시 연결할 수 있어요|only the vault's own key can reconnect them⟧", 12, "var(--muted)"))

# 4. 비교표: 원본 · 가명처리 · 익명처리
P4 = svg(300, sky(300)
         + box(50, 30, 660, 240, "⟦원본 vs 가명처리 vs 익명처리|ORIGINAL vs PSEUDONYMIZED vs ANONYMIZED⟧",
               ("⟦원본 — 이름 그대로, 재식별 바로 됨, 개인정보임|original — real names, instantly identifiable, personal data⟧",
                "⟦가명처리 — 번호표+연결표, 금고 열쇠 있으면 재식별, 여전히 개인정보임|pseudonymized — tag + vault key reconnects it, still personal data⟧",
                "⟦익명처리 — 연결표 자체를 태움, 재식별 불가, 개인정보 아님|anonymized — the key-table is burned, no re-identification, not personal data⟧",
                "⟦k-익명성 — 비슷한 손님 k명을 한 묶음으로 묶어 구분 못 하게|k-anonymity — group k similar guests so none stands out⟧"), 12))

# 5. 데이터가 많아지면 다시 식별될 위험이 커져요
P5 = svg(280, '<rect width="760" height="280" fill="var(--accent-soft)"/>'
         + tag(150, 100, 0.9, "A017") + tag(150, 150, 0.9, "A017")
         + '<path d="M190 100 L560 60" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/><path d="M190 150 L560 200" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4"/>'
         + box(480, 40, 260, 180, "⟦다른 장부들|other ledgers⟧", ("⟦구매 기록|purchase logs⟧", "⟦위치 기록|location logs⟧", "⟦합치면… 한 명으로 좁혀져요|combined... narrows to one person⟧"), 11)
         + label(380, 260, "⟦여러 장부를 합칠수록 재식별 위험은 다시 커져요|the more ledgers combined, the higher the re-identification risk⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "pseudonymize", "order": 2,
    "title": ("번호표로 바꿔 달고, 진짜 이름은 다른 금고에", "Swap in a Number Tag, Lock the Real Name in a Separate Vault"),
    "h1": ("<em>개인정보 비식별·가명처리</em>가 뭐예요?", "What is <em>De-identification/Pseudonymization</em>?"),
    "sub": ("개인정보 비식별·가명처리를 손님 이름표를 번호표로 바꿔 달고 진짜 이름은 다른 금고에 넣는 이야기로 풀어봤어요.",
            "De-identification and pseudonymization, told as a story about swapping a guest's name tag for a number, with the real name locked in a separate vault."),
    "panels": [
        {"svg": P1, "alt": ("서기가 '손님 명부'를 들고 있는데 이름·생일·동네가 그대로 적혀 있음", "A clerk holds a guest list with names, birthdates, and neighborhoods written out in full"),
         "caption": ("손님 명부에 진짜 이름이 그대로 있어요.", "The guest list has real names written out in full."),
         "small": ("연구팀에 그대로 넘기면 이름까지 다 보여요.", "Hand it straight to a research team, and even the names show.")},
        {"svg": P2, "alt": ("이름을 지운 명부를 보던 사람이 '그 동네에 그 생일인 사람, 한 명뿐인데요?'라고 말함", "Someone looking at the name-redacted list says only one person in that dong was born that day"),
         "caption": ("이름만 지워도 다시 알아낼 수 있어요.", "Erasing just the name doesn't stop re-identification."),
         "small": ("다른 단서(생일·동네)를 모으면 다시 알아내요 — 이게 재식별이에요.", "Combine other clues — birthdate, neighborhood — and the name comes back. That's re-identification.")},
        {"svg": P3, "hero": True, "alt": ("명부의 이름이 번호표(A017, A038)로 바뀌고, 진짜 이름과 번호의 연결표는 잠긴 금고 안에 경비가 지킴", "The list's names become number tags (A017, A038); the real-name-to-number key table sits locked in a vault, watched by a guard"),
         "caption": ("가명처리는 번호표로 바꿔 달고, 진짜 이름표는 다른 금고에 넣는 거예요.", "Pseudonymization swaps in a number tag and locks the real name in a separate vault."),
         "small": ("금고 열쇠가 따로 있어야 다시 연결할 수 있어요.", "Only the vault's own key can reconnect the two."),
         "tricks": (4, [
             (icon('<rect x="14" y="20" width="36" height="24" rx="6" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/><text x="32" y="37" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bad)">A017</text>'),
              ("번호표로 바꿔요", "Swap in a number tag"), ("이름 대신 코드", "a code instead of a name"), "warm"),
             (icon('<rect x="18" y="8" width="28" height="48" rx="4" fill="var(--night)"/><rect x="26" y="26" width="12" height="10" rx="2" fill="#E9B44C"/>'),
              ("연결표는 금고에", "The key table, in a vault"), ("따로 잠가 보관해요", "stored and locked separately")),
             (icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--good)" stroke-width="4"/><path d="M32 16 v16 l10 6" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>'),
              ("재식별은 양쪽 열쇠가 있어야", "Re-ID needs both keys"), ("한쪽만으론 못 열어요", "one side alone can't open it")),
             (icon('<path d="M16 48 L32 16 L48 48 Z" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linejoin="round"/><circle cx="32" cy="40" r="3" fill="var(--accent)"/>'),
              ("익명처리는 연결표 자체를 태워요", "Anonymization burns the key table"), ("그러면 아예 재식별이 안 돼요", "then re-ID is impossible at all"), "calm"),
         ])},
        {"svg": P4, "alt": ("원본·가명처리·익명처리·k-익명성을 비교한 네 줄 표", "A four-row comparison: original, pseudonymized, anonymized, k-anonymity"),
         "caption": ("원본, 가명처리, 익명처리는 서로 달라요.", "Original, pseudonymized, and anonymized are not the same thing."),
         "small": ("가명처리는 금고 열쇠가 있으면 재식별되므로 여전히 개인정보예요. 익명처리는 연결표 자체가 없어 개인정보가 아니에요.", "Pseudonymized data is still personal data, since the vault key can reconnect it. Anonymized data has no key table at all, so it isn't personal data.")},
        {"svg": P5, "alt": ("같은 번호표 A017이 구매 기록·위치 기록과 선으로 이어지며 '합치면 한 명으로 좁혀져요'", "The same tag A017 is linked by lines to purchase logs and location logs: combined, it narrows to one person"),
         "caption": ("데이터가 많아지면 다시 식별될 위험이 커져요.", "The more data combined, the higher the re-identification risk."),
         "small": ('그래서 재식별 위험을 미리 평가해요. 여러 성의 장부를 안전하게 합치려면 <a href="safezone-ko.html">특별 열람실</a>에서만 해요.',
                   'So re-identification risk gets assessed up front. Combining ledgers from several castles safely happens only in the <a href="safezone-en.html">special reading room</a>.')},
    ],
    "summary": (("<b>가명처리</b> = 이름표를 <b>번호표</b>로 바꾸고 진짜 이름과의 <b>연결표는 따로 잠가</b> 두는 것. <b>익명처리</b>는 그 연결표 자체를 태워 <b>되돌릴 수 없게</b> 만드는 것.",
                 "<b>Pseudonymization</b> = swapping a name for a <b>number tag</b> and locking the <b>key table</b> away separately. <b>Anonymization</b> burns that key table so it's <b>irreversible</b>."),
                ("가명처리(Pseudonymization)는 추가정보(연결정보) 없이는 특정 개인을 알아볼 수 없게 처리하는 것으로, 그 추가정보가 존재하는 한 여전히 개인정보로 취급돼요. 익명처리(Anonymization)는 어떤 방법으로도 재식별이 불가능하게 만든 것으로 더 이상 개인정보가 아니에요. k-익명성·l-다양성 등은 비식별 조치의 적정성을 평가하는 지표예요.",
                 "Pseudonymization processes data so an individual can't be identified without additional information; as long as that extra information exists, the data is still legally personal data. Anonymization makes re-identification impossible by any means, so it is no longer personal data. Measures like k-anonymity and l-diversity are used to assess whether de-identification is adequate.")),
    "glossary": [
        ("가명처리", "Pseudonymization", ("번호표로 바꿔 달기.", "Swapping in a number tag."), ("연결표(추가정보)가 있으면 되돌릴 수 있어요. 여전히 개인정보예요.", "Reversible with the key table (additional information). Still counted as personal data.")),
        ("익명처리", "Anonymization", ("연결표 자체를 태우기.", "Burning the key table itself."), ("어떤 방법으로도 재식별 불가능해요. 개인정보가 아니에요.", "Re-identification is impossible by any means. No longer personal data.")),
        ("추가정보(연결표)", "Additional information", ("번호와 이름을 잇는 표.", "The table linking number to name."), ("가명처리의 핵심. 본체와 분리해서 따로 암호화·잠가 보관해요.", "The core of pseudonymization. Kept separate from the data, encrypted and locked.")),
        ("재식별", "Re-identification", ("다른 단서로 다시 알아내기.", "Finding the name again from other clues."), ("생일·동네 같은 조합만으로도 한 명으로 좁혀질 수 있어요.", "A combination like birthdate and neighborhood can narrow it to one person.")),
        ("k-익명성", "k-anonymity", ("k명을 한 묶음으로.", "Grouping k people together."), ("비슷한 특징을 가진 손님을 최소 k명 묶어 어느 한 명인지 구분 못 하게 해요.", "Groups at least k similar guests so no individual stands out.")),
        ("개인정보 3법", "Korea's data-protection law set", ("나라가 정한 처리 규칙.", "The kingdom's rules for handling data."), ("개인정보보호법 등이 가명정보의 처리 근거와 한계를 정해요.", "Korea's Personal Information Protection Act and related laws set the grounds and limits for handling pseudonymized data.")),
        ("데이터 마스킹", "Data masking", ("일부만 가리기.", "Hiding only part of it."), ('가명처리와 비슷하지만 보통 비가역적으로 가려요. → <a href="masking-ko.html">이름 대신 번호표</a>', 'Similar to pseudonymization, but usually irreversible. → <a href="masking-en.html">a number instead of a name</a>')),
        ("개인정보 보호 원칙", "Privacy principles", ("손님 이름표는 손님 것.", "The name tag belongs to the guest."), ('가명처리도 이 원칙 위에서 움직여요. → <a href="privacy-ko.html">손님 이름표는 손님 것</a>', 'Pseudonymization still operates under this principle. → <a href="privacy-en.html">the name tag belongs to the guest</a>')),
    ],
}
