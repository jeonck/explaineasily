from _draw import *

CLERK = dict(hat="var(--stone-dark)", shirt="#4A5A72")
ANALYST = dict(hat="#5B8DEF", shirt="#5B8DEF")


def box(x, y, w, h, title, rows, size=11):
    out = (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
           + label(w / 2, 26, title, 13, "#142033", cls="d"))
    for i, r in enumerate(rows):
        out += label(16, 52 + i * 24, r, size, "#142033", "start")
    return out + "</g>"


def cloudy_chart(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            + "".join(f'<rect x="{i * 20}" y="{40 - h}" width="14" height="{h}" fill="var(--accent)" opacity="0.6"/>' for i, h in enumerate((22, 30, 18, 34, 24)))
            + '<rect x="-6" y="-6" width="112" height="56" rx="4" fill="none" stroke="var(--line)" stroke-dasharray="4 4" stroke-width="2"/></g>')


def locked_box(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-20" width="52" height="40" rx="4" fill="var(--night)"/>'
            '<rect x="-7" y="-6" width="14" height="12" rx="2" fill="#E9B44C"/><path d="M-4 -6 v-5 a4 4 0 0 1 8 0 v5" stroke="#E9B44C" stroke-width="3" fill="none"/></g>')


def small_house(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-6" width="48" height="36" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
            '<path d="M-30 -6 L0 -32 L30 -6 Z" fill="var(--good)"/></g>')


# 1. 다 가리면 분석을 못 해요
P1 = svg(280, sky(280)
         + box(60, 50, 280, 170, "⟦손님 명부(다 가림)|GUEST LIST (all hidden)⟧", ("⟦●●● · ●● · ●●●●|●●● · ●● · ●●●●⟧", "⟦●●● · ●● · ●●●●|●●● · ●● · ●●●●⟧"), 12)
         + person(500, 150, s=0.8, face=FROWN, **ANALYST)
         + bubble(440, 60, 250, 40, "⟦이래선 아무 분석도 못 해요|there's nothing left to analyze⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 258, "⟦다 가리면 안전하지만 쓸모가 없어요|hide everything and it's safe, but useless⟧", 13, "var(--ink)"))

# 2. 다 보여주면 위험해요
P2 = svg(280, '<rect width="760" height="280" fill="var(--bad-soft)"/>'
         + box(60, 50, 280, 170, "⟦손님 명부(원본)|GUEST LIST (original)⟧", ("⟦김민수 · 32 · 서울|Kim · 32 · Seoul⟧", "⟦이지은 · 28 · 부산|Lee · 28 · Busan⟧"), 12)
         + person(500, 150, s=0.8, face=MASK)
         + label(380, 258, "⟦다 보여주면 분석은 잘 되지만 손님이 위험해요|show everything, and the analysis is great — but guests are exposed⟧", 13, "var(--ink)"))

# 3. PET = 가리는 방법이 여럿인 도구상자 (hero)
P3 = svg(340, sky(340)
         + box(40, 40, 310, 260, "⟦도구상자|THE TOOLBOX⟧",
               ("⟦① 흐림을 살짝 섞기|① mix in a little blur⟧",
                "⟦② 자물쇠 채운 채 계산하기|② compute while still locked⟧",
                "⟦③ 집집마다 따로 배우기|③ learn separately, at each house⟧",
                "⟦④ 닮은 가짜 명부 만들기|④ make a look-alike fake list⟧"), 13)
         + cloudy_chart(430, 100, 1.1) + locked_box(540, 100, 1.0) + small_house(620, 100, 0.9) + box(500, 200, 180, 60, "⟦가짜 명부|fake list⟧", (), 11)
         + label(380, 30, "⟦개인정보 보호강화기술(PET) = 손님을 지키는 여러 다른 도구|privacy-enhancing technologies = several different tools, all protecting the guest⟧", 13, "var(--ink)", cls="d"))

# 4. 네 기법 비교표
P4 = svg(320, sky(320)
         + box(50, 20, 660, 280, "⟦기법마다 쓰는 상황이 달라요|EACH TOOL FITS A DIFFERENT SITUATION⟧",
               ("⟦차분 프라이버시 — 통계 결과만 내보낼 때, 계산 빠름|differential privacy — releasing only stats, fast⟧",
                "⟦동형암호 — 암호화한 채 계산이 꼭 필요할 때, 느리고 비쌈|homomorphic encryption — must compute while encrypted, slow and costly⟧",
                "⟦연합학습 — 데이터를 모을 수 없을 때, 통신 비용 큼|federated learning — data can't be gathered, high communication cost⟧",
                "⟦합성데이터 — 테스트·개발용 가짜 데이터가 필요할 때|synthetic data — for testing and development, not real guests⟧"), 13))

# 5. 완벽한 프라이버시와 완벽한 정확도는 같이 안 돼요
P5 = svg(280, '<rect width="380" height="280" fill="var(--good-soft)"/><rect x="380" width="380" height="280" fill="var(--accent-soft)"/>'
         + label(190, 50, "⟦흐림을 많이 섞으면|mix in more blur⟧", 13, "var(--ink)", cls="d")
         + cloudy_chart(130, 140, 1.3) + label(190, 230, "⟦더 안전, 덜 정확|safer, less accurate⟧", 12, "var(--good)")
         + label(570, 50, "⟦흐림을 적게 섞으면|mix in less blur⟧", 13, "var(--ink)", cls="d")
         + cloudy_chart(510, 140, 1.3) + label(570, 230, "⟦덜 안전, 더 정확|less safe, more accurate⟧", 12, "var(--bad)")
         + label(380, 266, "⟦프라이버시와 정확도는 시소처럼 맞바꿔야 해요|privacy and accuracy trade off, like a seesaw⟧", 12, "var(--ink)"))

PAGE = {
    "slug": "pet", "order": 10,
    "title": ("손님을 지키는 여러 다른 도구상자", "The Toolbox With Many Different Ways to Protect a Guest"),
    "h1": ("<em>개인정보 보호강화기술(PET)</em>이 뭐예요?", "What are <em>Privacy-Enhancing Technologies (PET)</em>?"),
    "sub": ("개인정보 보호강화기술(PET)을 손님을 지키는 여러 다른 도구가 담긴 도구상자 이야기로 풀어봤어요.",
            "Privacy-enhancing technologies, told as a story about a toolbox with several different ways to protect a guest."),
    "panels": [
        {"svg": P1, "alt": ("명부의 모든 글자가 가려져 있고, 분석가가 '이래선 아무 분석도 못 해요'라며 찡그림", "Every character in the list is hidden, and a frowning analyst says there's nothing left to analyze"),
         "caption": ("다 가리면 분석을 못 해요.", "Hide everything, and there's nothing left to analyze."),
         "small": ("안전하지만 쓸모가 없어요.", "Safe, but useless.")},
        {"svg": P2, "alt": ("명부에 이름과 나이, 사는 곳이 그대로 있고 가면 쓴 사람이 들여다봄", "The list shows real names, ages, and neighborhoods, while a masked figure looks on"),
         "caption": ("다 보여주면 위험해요.", "Show everything, and it's dangerous."),
         "small": ("분석은 잘 되지만 손님이 위험해져요.", "The analysis works great — but it puts guests at risk.")},
        {"svg": P3, "hero": True, "alt": ("도구상자 안에 네 가지 방법이 적혀 있고, 옆에 흐릿한 차트·자물쇠 채운 상자·작은 집·가짜 명부가 놓여 있음", "A toolbox lists four methods, beside a blurry chart, a padlocked box, a small house, and a fake list"),
         "caption": ("PET는 손님을 지키는 여러 다른 도구가 담긴 도구상자예요.", "PET is a toolbox holding several different tools, each protecting the guest its own way."),
         "small": ("한 가지 방법만 있는 게 아니라, 상황에 맞춰 고를 수 있어요.", "There isn't just one way — you pick the tool that fits the situation."),
         "tricks": (4, [
             (icon('<rect x="8" y="20" width="12" height="24" fill="var(--accent)" opacity="0.6"/><rect x="24" y="12" width="12" height="32" fill="var(--accent)" opacity="0.6"/><rect x="40" y="26" width="12" height="18" fill="var(--accent)" opacity="0.6"/>'),
              ("차분 프라이버시", "Differential privacy"), ("결과에 살짝 흐림을 섞어요", "a little blur mixed into the result"), "calm"),
             (icon('<rect x="18" y="20" width="28" height="26" rx="3" fill="var(--night)"/><rect x="26" y="26" width="12" height="10" rx="2" fill="#E9B44C"/>'),
              ("동형암호", "Homomorphic encryption"), ("자물쇠 채운 채로 계산해요", "computes while still locked"), "warm"),
             (icon('<rect x="8" y="26" width="18" height="16" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M4 26 L17 12 L30 26 Z" fill="var(--good)"/><rect x="36" y="26" width="18" height="16" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><path d="M32 26 L45 12 L58 26 Z" fill="var(--good)"/>'),
              ("연합학습", "Federated learning"), ("데이터는 각자 집에 두고요", "the data stays at each house")),
             (icon('<rect x="14" y="16" width="36" height="32" rx="3" fill="#FFF8E7" stroke="var(--accent)" stroke-width="3" stroke-dasharray="5 4"/>'),
              ("합성데이터", "Synthetic data"), ("닮은 가짜 명부를 만들어요", "a look-alike fake list"), "calm"),
         ])},
        {"svg": P4, "alt": ("네 기법이 언제 쓰이는지 정리한 표: 차분 프라이버시(통계), 동형암호(암호화 계산), 연합학습(데이터 분산), 합성데이터(테스트용)", "A table listing when each method fits: differential privacy (stats), homomorphic encryption (encrypted compute), federated learning (distributed data), synthetic data (testing)"),
         "caption": ("네 기법은 쓰는 상황이 서로 달라요.", "Each of the four fits a different situation."),
         "small": ("빠르고 가벼운 것도 있고, 느리지만 안전한 것도 있어요.", "Some are fast and light; others are slow but very safe.")},
        {"svg": P5, "alt": ("흐림을 많이 섞은 차트는 더 안전하지만 덜 정확하고, 흐림을 적게 섞은 차트는 덜 안전하지만 더 정확함", "A heavily blurred chart is safer but less accurate; a lightly blurred chart is less safe but more accurate"),
         "caption": ("완벽한 프라이버시와 완벽한 정확도는 같이 안 돼요.", "Perfect privacy and perfect accuracy can't both happen at once."),
         "small": ('<a href="pseudonymize-ko.html">가명처리</a>와 마찬가지로, 어디까지 가릴지는 늘 맞바꿈이에요.',
                   'Just like <a href="pseudonymize-en.html">pseudonymization</a>, how much to hide is always a trade-off.')},
    ],
    "summary": (("<b>PET(개인정보 보호강화기술)</b> = <b>차분 프라이버시·동형암호·연합학습·합성데이터</b> 같이, 데이터를 보호하면서도 <b>쓸 수 있게</b> 만드는 여러 도구.",
                 "<b>PET (privacy-enhancing technologies)</b> = a set of tools — <b>differential privacy, homomorphic encryption, federated learning, synthetic data</b> — that protect data while keeping it <b>usable</b>."),
                ("PET는 개인정보를 가리거나 암호화한 상태에서도 분석·학습이 가능하도록 돕는 기술들을 통칭해요. 차분 프라이버시는 결과값에 통계적 잡음을 더해 한 개인의 존재 여부를 숨기고, 동형암호는 암호문 상태 그대로 연산해 복호화 없이 결과를 얻고, 연합학습은 원본 데이터를 모으지 않고 각 기기에서 학습한 모델만 모으고, 합성데이터는 실제 분포를 흉내 낸 가짜 데이터를 생성해요. 어떤 기법도 프라이버시와 정확도·효율을 동시에 완벽히 만족시키진 못해, 상황에 맞춰 조합해서 써요.",
                 "PET is an umbrella term for technologies that let data be analyzed or used for training while still protected or encrypted. Differential privacy adds statistical noise to results so no single individual's presence can be detected; homomorphic encryption computes directly on ciphertext without ever decrypting it; federated learning gathers only trained models from each device, never the raw data itself; synthetic data generates fake records that mimic the real distribution. No single technique perfectly satisfies both privacy and accuracy or efficiency at once, so they are mixed and matched to fit the situation.")),
    "glossary": [
        ("차분 프라이버시", "Differential privacy", ("결과에 살짝 흐림 섞기.", "Mixing a little blur into the result."), ("통계적 잡음을 더해 한 사람 때문에 결과가 바뀌었는지 못 알아보게 해요.", "Adds statistical noise so no one can tell whether a single person changed the result.")),
        ("동형암호", "Homomorphic encryption", ("자물쇠 채운 채 계산.", "Computing while still locked."), ('열어 보지 않고도 답만 얻어요. → <a href="encryption-ko.html">열쇠 없이는 못 읽는 편지</a>', 'Gets the answer without ever opening the lock. → <a href="encryption-en.html">the letter nobody can read without the key</a>')),
        ("연합학습", "Federated learning", ("집집마다 따로 배우기.", "Learning separately, at each house."), ("데이터는 그 자리에 두고, 배운 결과만 모아요.", "The data never leaves home — only what was learned gets collected.")),
        ("합성데이터", "Synthetic data", ("닮은 가짜 명부.", "A look-alike fake list."), ("진짜 손님 대신 비슷한 특성의 가짜 손님을 만들어 분석·테스트에 써요.", "Fake guests with similar traits stand in for real ones, in analysis or testing.")),
        ("영지식증명", "Zero-knowledge proof", ("내용 안 보여주고 증명하기.", "Proving something without showing it."), ("비밀번호를 말하지 않고도 안다는 걸 증명하는 것 같은 기법이에요.", "Lets you prove you know a password without ever saying it.")),
        ("프라이버시-정확도 트레이드오프", "Privacy-accuracy trade-off", ("시소.", "A seesaw."), ("더 가리면 더 안전하지만 덜 정확해져요.", "Hide more, and it's safer but less accurate.")),
        ("가명처리", "Pseudonymization", ("번호표로 바꿔 달기.", "Swapping in a number tag."), ('PET보다 먼저 쓰는 기본 도구예요. → <a href="pseudonymize-ko.html">번호표로 바꿔 달고, 진짜 이름은 다른 금고에</a>', 'The basic tool used before reaching for PET. → <a href="pseudonymize-en.html">swap in a number tag, lock the real name away</a>')),
        ("데이터 결합", "Data linkage/combination", ("여러 성의 장부 합치기.", "Combining ledgers from several castles."), ('안전하게 합치려면 특별한 방에서만 해요. → <a href="safezone-ko.html">밖으로 못 들고 나가는 특별 열람실</a>', 'Done safely only inside a special room. → <a href="safezone-en.html">the special reading room you can\'t carry data out of</a>')),
    ],
}
