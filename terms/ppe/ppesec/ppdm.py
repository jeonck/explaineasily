from _draw import *

RESEARCHER = dict(hat="#5B8DEF", shirt="#5B8DEF")
VILLAGER1 = dict(hat=None, shirt="#4A7A6A")
VILLAGER2 = dict(hat=None, shirt="#7B3FA0")
VILLAGER3 = dict(hat=None, shirt="#B5651D")
FORGER = dict(hat="var(--bad)")


def card(x, y, w, h, rows):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="2.5"/>'
    for i, r in enumerate(rows):
        out += label(x + w / 2, y + 20 + i * 18, r, 10, "#142033", cls="d")
    return out


def groupbox(x, y, w, h, n, color="var(--good-soft)"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}" stroke="var(--good)" stroke-width="2.5" stroke-dasharray="6 4"/>' + label(x + w / 2, y - 8, f"⟦최소 {n}명|at least {n}⟧", 11, "var(--good)")


# 1. 조사관이 마을 전체 경향을 알고 싶어요
P1 = svg(320, sky(320)
         + person(190, 120, s=0.85, face=EYES, **RESEARCHER)
         + bubble(60, 30, 250, 42, "⟦마을 평균 수입이 얼마나 되는지 알고 싶어요|I want to know the village's average income⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + card(430, 60, 90, 70, ("⟦이름 A|name A⟧", "⟦수입 120|income 120⟧"))
         + card(540, 100, 90, 70, ("⟦이름 B|name B⟧", "⟦수입 95|income 95⟧"))
         + card(430, 170, 90, 70, ("⟦이름 C|name C⟧", "⟦수입 140|income 140⟧"))
         + label(380, 280, "⟦장부엔 마을 사람 하나하나의 기록이 다 있어요|the ledger holds every single villager's own record⟧", 13, "var(--ink)", cls="d"))

# 2. 이름만 지워도, 몇 가지 단서로 다시 찾아낼 수 있어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + card(150, 70, 110, 90, ("⟦이름 ×|name ×⟧", "⟦30대·대장간|30s·smith⟧", "⟦수입 140|income 140⟧"))
         + person(330, 150, s=0.75, **FORGER, face=MASK)
         + bubble(400, 40, 250, 50, "⟦30대 대장장이는 마을에 한 명뿐이네요, C 아저씨죠?|only one smith in their 30s — that's Mr. C, isn't it?⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦이름만 지워선, 몇 가지 단서로도 다시 찾아낼 수 있어요|erase just the name, and a few other clues can still find them again⟧", 11, "var(--ink)", cls="d"))

# 3. PPDM = 개인은 흐리고, 흐름은 보이게 하는 여러 기법 (hero)
P3 = svg(390, sky(390)
         + groupbox(90, 70, 230, 120, 3)
         + card(110, 90, 90, 60, ("⟦A|A⟧", "⟦120|120⟧")) + card(210, 90, 90, 60, ("⟦B|B⟧", "⟦~120|~120⟧"))
         + label(205, 210, "⟦① k명씩 묶기|① bundle k together⟧", 12, "var(--ink)", cls="d")
         + card(400, 90, 100, 60, ("⟦120 + 노이즈|120 + noise⟧", "⟦≈ 115|≈ 115⟧"))
         + label(450, 210, "⟦② 살짝 흔들기|② add a little noise⟧", 12, "var(--ink)", cls="d")
         + card(580, 90, 120, 60, ("⟦평균 118|average: 118⟧",))
         + label(640, 210, "⟦③ 통계만 내보내기|③ export statistics only⟧", 12, "var(--ink)", cls="d")
         + person(380, 280, s=0.8, face=SMILE, **RESEARCHER)
         + label(380, 375, "⟦PPDM = 개인 한 명 한 명은 흐리게, 마을 전체 흐름은 선명하게|PPDM = blur each individual, while the village's overall trend stays clear⟧", 12, "var(--ink)", cls="d"))

KANON_I = icon('<circle cx="18" cy="32" r="9" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="32" cy="24" r="9" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="46" cy="32" r="9" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><rect x="6" y="14" width="52" height="34" rx="8" fill="none" stroke="var(--good)" stroke-width="2" stroke-dasharray="4 3"/>')
NOISE_I = icon('<path d="M8 32 q8 -16 16 0 t16 0 t16 0" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
SEAL_I = icon('<rect x="12" y="20" width="40" height="28" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><circle cx="42" cy="18" r="9" fill="var(--bad)"/>')
STAT_I = icon('<rect x="12" y="38" width="10" height="16" fill="var(--good)"/><rect x="27" y="28" width="10" height="26" fill="var(--good)"/><rect x="42" y="16" width="10" height="38" fill="var(--good)"/>')

PAGE = {
    "slug": "ppdm", "order": 23,
    "title": ("이름은 가리고, 흐름은 보는 통계 조사관", "The Statistician Who Hides Names but Still Sees the Trend"),
    "h1": ("<em>PPDM</em>이 뭐예요?", "What is <em>PPDM</em>?"),
    "sub": ("프라이버시 보존형 데이터 마이닝(PPDM)을, 사람 한 명 한 명은 흐리게 하면서 마을 전체 흐름은 그대로 읽어내는 조사관 이야기로 풀어봤어요.",
            "Privacy-Preserving Data Mining (PPDM), told as a story about a statistician who blurs each person while still reading the village's overall trend."),
    "panels": [
        {"svg": P1, "alt": ("조사관이 마을 평균 수입을 알고 싶어하고, 장부엔 이름과 수입이 그대로 적힌 카드들이 있음", "A statistician wants to know the village's average income, and the ledger holds cards with each name and income written out in full"),
         "caption": ("조사관이 마을 전체 경향을 알고 싶어요.", "The statistician wants to know the village's overall trend."),
         "small": ("장부엔 마을 사람 하나하나의 이름과 수입이 그대로 다 적혀 있어요.", "The ledger spells out every single villager's name and income in full.")},
        {"svg": P2, "alt": ("이름을 지운 카드에 나이와 직업만 남아 있는데, 위조자가 이걸 보고 30대 대장장이는 C 아저씨뿐이라고 알아챔", "A card with the name erased still shows age and job, and a forger figures out from that alone that the 30-something smith must be Mr. C"),
         "caption": ("이름만 지워도, 몇 가지 단서로 다시 찾아낼 수 있어요.", "Erase just the name, and a few remaining clues can still find the person again."),
         "small": ('<a href="masking-ko.html">이름만 지우는 것(마스킹)</a>으로는 부족해요. 나이·동네·직업만 남아도 한 명으로 좁혀질 수 있어요.',
                   'Just <a href="masking-en.html">erasing the name (masking)</a> isn\'t enough. Age, neighborhood, and job alone can narrow it down to one person.')},
        {"svg": P3, "hero": True, "alt": ("최소 3명씩 묶기, 값에 노이즈 섞기, 통계만 내보내기 세 가지 기법을 거쳐 조사관이 웃으며 평균만 확인함", "Bundling at least three people together, mixing in noise, and exporting only the statistic — after these three techniques, the statistician smiles, holding just the average"),
         "caption": ("PPDM은 개인은 흐리고, 흐름은 보이게 하는 여러 기법이에요.", "PPDM is a bundle of techniques that blur the individual while keeping the trend visible."),
         "small": ('<a href="homoenc-ko.html">동형암호</a>처럼 봉인한 채로 계산하는 방법도 PPDM의 한 가지 도구예요.',
                   'A technique like <a href="homoenc-en.html">homomorphic encryption</a> — computing while still sealed — is one of PPDM\'s tools too.'),
         "tricks": (4, [
             (KANON_I, ("k명씩 묶기", "Bundle k people together"), ("최소 k명은 똑같아 보이게 해요", "at least k people are made to look alike"), "calm"),
             (NOISE_I, ("살짝 흔들어 섞기", "Mix in a little noise"), ("차분 프라이버시, 값을 살짝 바꿔요", "differential privacy — nudges each value a bit")),
             (SEAL_I, ("봉인한 채 계산", "Compute while still sealed"), ("동형암호 같은 방법도 써요", "techniques like homomorphic encryption"), "warm"),
             (STAT_I, ("통계만 내보내기", "Export only the statistic"), ("한 사람 한 사람의 줄은 안 나가요", "no single person's row ever leaves")),
         ])},
        {"svg": svg(340, sky(340)
                    + '<rect x="30" y="30" width="700" height="260" rx="8" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><rect x="30" y="30" width="700" height="34" rx="8" fill="#C9A86A"/>'
                    + label(130, 53, "⟦기법|technique⟧", 13, "#142033", cls="d") + label(400, 53, "⟦하는 일|what it does⟧", 13, "#142033", cls="d") + label(610, 53, "⟦대가|the trade-off⟧", 13, "#142033", cls="d")
                    + "".join(f'<path d="M30 {64 + i * 75} h700" stroke="#C9A86A" stroke-width="1.5"/>' for i in range(1, 3))
                    + label(130, 100, "⟦k-익명성|k-anonymity⟧", 13, "#142033", cls="d") + label(400, 100, "⟦최소 k명이 똑같아 보이게|at least k people look identical⟧", 11, "#142033") + label(610, 100, "⟦k가 클수록 뭉뚱그려져요|the bigger k, the blurrier it gets⟧", 11, "#142033")
                    + label(130, 175, "⟦차분 프라이버시|differential privacy⟧", 13, "#142033", cls="d") + label(400, 175, "⟦값에 수학적 노이즈를 더해요|adds mathematically-controlled noise to the value⟧", 11, "#142033") + label(610, 175, "⟦노이즈가 클수록 덜 정확해요|more noise means less accuracy⟧", 11, "#142033")
                    + label(130, 250, "⟦동형암호|homomorphic encryption⟧", 13, "#142033", cls="d") + label(400, 250, "⟦봉인한 채로 계산해요|computes while still sealed⟧", 11, "#142033") + label(610, 250, "⟦훨씬 느려요|much slower⟧", 11, "#142033")),
         "alt": ("표: k-익명성 — 최소 k명 묶기 / 뭉뚱그려짐, 차분 프라이버시 — 노이즈 추가 / 정확도 저하, 동형암호 — 봉인 계산 / 느림", "Table: k-anonymity — bundle k people / blurrier, differential privacy — add noise / less accurate, homomorphic encryption — compute sealed / slower"),
         "caption": ("기법마다 대가가 달라요.", "Each technique trades off something different."),
         "small": ('<a href="homoenc-ko.html">동형암호</a>는 PPDM이 쓰는 도구 중 하나예요. 보호를 세게 할수록 통계의 쓸모는 줄어들어요.',
                   '<a href="homoenc-en.html">Homomorphic encryption</a> is one of the tools PPDM reaches for. The stronger the protection, the less useful the statistic becomes.')},
        {"svg": svg(330, sky(330)
                    + person(190, 125, s=0.85, face=EYES, **RESEARCHER) + label(190, 260, "⟦보호를 세게 하면 통계가 덜 정확해져요|stronger protection makes the statistic less accurate⟧", 11, "var(--ink)")
                    + person(560, 125, s=0.85, face=FROWN, **VILLAGER1) + label(560, 260, "⟦재식별 위험은 완전히 0이 되진 않아요|the re-identification risk never quite reaches zero⟧", 11, "var(--bad)")
                    + label(380, 305, "⟦그래서 얼마나 가릴지는 늘 저울질해야 해요|so how much to blur is always a balance to strike⟧", 12, "var(--ink)", cls="d")),
         "alt": ("보호를 세게 할수록 통계가 덜 정확해지고, 재식별 위험은 완전히 0이 되지 않음", "The stronger the protection, the less accurate the statistic — and the re-identification risk never fully reaches zero"),
         "caption": ("보호와 쓸모는 늘 저울 위에 있어요.", "Protection and usefulness always sit on the same scale."),
         "small": ('재식별 위험은 0이 되지 않아요. → <a href="data3law-ko.html">가명정보</a>·<a href="privacy-ko.html">개인정보 보호</a>와 같은 고민을 데이터 분석에 적용한 거예요.',
                   'The risk of re-identification never hits zero. → the same worry behind <a href="data3law-en.html">pseudonymized data</a> and <a href="privacy-en.html">privacy</a>, applied to data analysis.')},
    ],
    "summary": (("<b>PPDM</b> = 사람 <b>한 명 한 명은 흐리게</b> 하면서, 마을 전체의 <b>흐름(통계)은 그대로 읽어내는</b> 여러 기법의 묶음.",
                 "<b>PPDM</b> = a bundle of techniques that <b>blur each individual</b> while still letting you <b>read the village's overall trend (the statistics)</b>."),
                ("Privacy-Preserving Data Mining, 프라이버시 보존형 데이터 마이닝. 개인 식별이 가능한 원본 데이터를 그대로 분석하지 않고, k-익명성(동일 속성을 가진 개체를 k개 이상으로 묶음), 차분 프라이버시(결과에 수학적으로 제어된 노이즈를 추가), 동형암호(암호문 상태로 연산) 같은 기법으로 개인을 보호하면서 통계적 패턴은 추출하는 방법들을 통칭해요. 보호 강도와 분석 정확도는 трейд-off 관계예요.",
                 "Privacy-Preserving Data Mining (PPDM) is an umbrella term for methods that extract statistical patterns while protecting individuals, instead of analyzing identifiable raw data directly — k-anonymity (bundling entities sharing attributes into groups of at least k), differential privacy (adding mathematically-controlled noise to results), and homomorphic encryption (computing directly on ciphertext) among them. Protection strength and analytical accuracy trade off against each other.")),
    "glossary": [
        ("PPDM", "Privacy-Preserving Data Mining", ("개인은 흐리고 흐름은 보이게 하는 기법 묶음.", "A bundle of techniques that blur the person but keep the trend visible."), ("여러 기법을 아우르는 이름이에요.", "An umbrella name covering several techniques.")),
        ("k-익명성", "k-anonymity", ("최소 k명이 똑같아 보이게 묶는 것.", "Bundling so at least k people look identical."), ("한 명으로 좁혀지는 걸 막아요.", "Prevents narrowing a record down to just one person.")),
        ("차분 프라이버시", "Differential privacy", ("값에 수학적으로 노이즈를 더하는 것.", "Adding mathematically-controlled noise to a value."), ("개별 값은 흐려지고, 전체 통계는 거의 그대로예요.", "Blurs the individual value while the overall statistic stays nearly intact.")),
        ("재식별", "Re-identification", ("지운 이름을 도로 찾아내는 것.", "Finding the erased name back again."), ('남은 몇 가지 단서만으로도 가능해요. → <a href="masking-ko.html">이름 대신 번호표</a>', 'Possible from just a few remaining clues. → <a href="masking-en.html">a number tag instead of a name</a>')),
        ("동형암호", "Homomorphic encryption", ("봉인한 채로 셈하는 방법.", "A way to compute while things stay sealed."), ('PPDM이 쓰는 도구 중 하나예요. → <a href="homoenc-ko.html">뜯지 않고 셈하는 봉인 편지</a>', 'One of the tools PPDM reaches for. → <a href="homoenc-en.html">the sealed letter you can do math on</a>')),
        ("가명정보", "Pseudonymized data", ("이름을 지운 기록.", "A record with the name removed."), ('PPDM은 이 가명정보로 통계를 낼 때 특히 쓰여요. → <a href="data3law-ko.html">데이터 3법 개정</a>', 'PPDM is especially used when mining statistics from this kind of data. → <a href="data3law-en.html">the Three Data Acts amendment</a>')),
        ("정확도 trade-off", "Accuracy trade-off", ("보호를 세게 할수록 덜 정확해지는 것.", "The stronger the protection, the less accurate it gets."), ("완벽한 보호와 완벽한 정확도를 동시에 가질 순 없어요.", "You can't have perfect protection and perfect accuracy at the same time.")),
        ("개인정보 보호", "Privacy", ("보호해야 할 대상 그 자체.", "The very thing being protected."), ('PPDM은 통계·연구 목적에서 이 약속을 지키는 기술적 방법이에요. → <a href="privacy-ko.html">손님 이름표는 손님 것</a>', 'PPDM is the technical way to keep this promise for statistics and research. → <a href="privacy-en.html">the visitor\'s name tag belongs to the visitor</a>')),
    ],
}
