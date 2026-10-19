from _draw import *

VILLAGER = dict(hat=None, shirt="#4A7A6A")
CLERK_A = dict(hat="var(--stone-dark)", shirt="#4A5A72", face=EYES)
CLERK_B = dict(hat="#E9B44C", shirt="#7B3FA0", face=SMILE)
CLERK_C = dict(hat="#5B8DEF", shirt="#5B8DEF", face=SMILE)


def sealshop(x, y, s=1.0, color="var(--panel)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="0" width="80" height="54" fill="{color}" stroke="var(--stone-dark)" stroke-width="3"/>'
            f'<path d="M-46 0 L0 -28 L46 0 Z" fill="var(--stone-dark)"/><circle cy="24" r="14" fill="#E9B44C"/>'
            + '<path d="M-6 24 l5 5 l9 -11" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/></g>')


def idcard(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-20" width="60" height="40" rx="5" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/>'
            + '<circle cx="-12" cy="0" r="9" fill="#C9A86A"/><path d="M4 -8 h18 M4 0 h18 M4 8 h12" stroke="#142033" stroke-width="2" stroke-linecap="round"/><circle cx="18" cy="10" r="7" fill="#E9B44C"/></g>')


# 1. 도장집이 딱 하나뿐이던 시절
P1 = svg(320, sky(320)
         + sealshop(380, 160, 1.3)
         + label(380, 40, "⟦나라가 정한 도장집이 딱 하나뿐이었어요|there used to be exactly one state-designated seal-shop⟧", 13, "var(--ink)", cls="d")
         + person(170, 230, s=0.7, face=SMILE, **VILLAGER) + label(170, 290, "⟦빵 하나 사려 해도 여길 들러야 했어요|even to buy a loaf of bread, you had to stop here first⟧", 10, "var(--muted)")
         + person(600, 230, s=0.7, face=SMILE, **VILLAGER) + label(600, 290, "⟦나라 서류 내려 해도 똑같이요|same, even to file a government paper⟧", 10, "var(--muted)"))

# 2. 복잡하고 불편해도 다른 길이 없었어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=FROWN + SWEAT, **VILLAGER)
         + bubble(60, 40, 260, 50, "⟦특별한 상자에 담아 늘 들고 다녀야 하고, 다른 성엔 못 써요|had to carry it around in a special box, and it wouldn't work at any other castle⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + sealshop(560, 160, 1.1)
         + label(380, 282, "⟦불편해도 법이 그 도장집만 쓰라고 정해뒀어요|inconvenient as it was, the law said only that one shop counted⟧", 12, "var(--ink)", cls="d"))

# 3. 법이 바뀌어 도장집이 여럿 생겼어요 (hero)
P3 = svg(340, sky(340)
         + sealshop(140, 170, 0.9, "var(--panel)") + label(140, 250, "⟦공동인증서(옛 공인인증서)|the Joint Certificate (the old mandatory one)⟧", 10, "var(--muted)")
         + sealshop(380, 170, 0.9, "var(--good-soft)") + label(380, 250, "⟦카카오·토스 같은 민간 인증|private ones, like KakaoPay or Toss⟧", 10, "var(--muted)")
         + sealshop(620, 170, 0.9, "var(--accent-soft)") + label(620, 250, "⟦통신사 PASS 인증|carrier PASS authentication⟧", 10, "var(--muted)")
         + person(380, 70, s=0.6, face=SMILE, **VILLAGER) + label(380, 40, "⟦이제 아무 도장집이나 똑같이 통해요|now any of these shops carries equal weight⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦전자서명법 개정(2020) = 법이 특혜를 없애고, 선택지를 열었어요|the amended Digital Signature Act (2020) ended the monopoly and opened up the choice⟧", 13, "var(--ink)", cls="d"))

LAW_I = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
MANY_I = icon('<circle cx="18" cy="32" r="10" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="32" cy="20" r="10" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/><circle cx="46" cy="32" r="10" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2.5"/>')
EQUAL_I = icon('<path d="M16 24 h32 M16 36 h32" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>')
TECH_I = icon('<rect x="18" y="20" width="28" height="30" rx="3" fill="#8B5E3C"/><circle cx="32" cy="12" r="10" fill="#E9B44C"/>')

PAGE = {
    "slug": "pkicert", "order": 21,
    "title": ("하나뿐이던 도장집, 이제는 여럿", "The One Seal-Shop That's Now Many"),
    "h1": ("<em>공인인증서·사설인증</em>이 뭐예요?", "What are <em>Accredited and Private Certificates</em>?"),
    "sub": ("공인인증서와 사설(민간) 인증서를, 나라가 정한 도장집이 하나뿐이던 시절과 여럿이 된 지금을 비교하는 이야기로 풀어봤어요.",
            "Accredited (공인) vs. private (사설) certificates, told as a story comparing the days of one state-designated seal-shop with today's many."),
    "panels": [
        {"svg": P1, "alt": ("나라가 정한 도장집이 성 한가운데 딱 하나 있고, 빵을 사거나 서류를 내려는 손님 모두 이곳을 거쳐야 함", "A single state-designated seal-shop sits at the center of the castle, and every villager — whether buying bread or filing a paper — must pass through it"),
         "caption": ("도장집이 딱 하나뿐이던 시절이 있었어요.", "There used to be exactly one state-designated seal-shop."),
         "small": ("공인인증서. 전자서명을 하려면 법이 정한 이 도장집만 써야 했어요.", "The 공인인증서 (accredited certificate). To sign anything electronically, the law said this one shop was the only option.")},
        {"svg": P2, "alt": ("손님이 땀 흘리며 특별한 상자에 담아 늘 들고 다녀야 하고 다른 성엔 못 쓴다고 불평함", "A sweating villager complains about having to carry it in a special box, and that it wouldn't work at any other castle"),
         "caption": ("복잡하고 불편해도 다른 길이 없었어요.", "Inconvenient as it was, there was no other way."),
         "small": ("특별한 상자(보안 프로그램)에 담아 들고 다녀야 했고, 다른 컴퓨터로 옮기기도 번거로웠어요.", "It had to be carried around in a special box (security software), and moving it to another computer was a hassle.")},
        {"svg": P3, "hero": True, "alt": ("법이 바뀌어 공동인증서, 카카오·토스 같은 민간 인증, 통신사 PASS 인증이 나란히 서 있고 손님이 아무거나 고를 수 있음", "After the law changed, the Joint Certificate, private certificates like KakaoPay or Toss, and carrier PASS authentication stand side by side, and the villager can pick any of them"),
         "caption": ("법이 바뀌어 도장집이 여럿 생겼어요.", "The law changed, and now there are several seal-shops."),
         "small": ('전자서명법 개정(2020)으로 공인인증서의 법적 특혜가 사라지고, <a href="mydataSec-ko.html">본인확인</a>에 쓰는 여러 민간 인증서가 똑같은 효력을 가지게 됐어요.',
                   'The 2020 amendment to the Digital Signature Act ended the accredited certificate\'s special legal status — several private certificates used for <a href="mydataSec-en.html">identity verification</a> now carry the very same legal weight.'),
         "tricks": (4, [
             (LAW_I, ("법이 특혜를 없앴어요", "The law ended the privilege"), ("전자서명법 개정, 2020년", "the Digital Signature Act, amended in 2020"), "calm"),
             (MANY_I, ("여러 도장집이 생겼어요", "Several shops sprang up"), ("카카오페이, 토스, PASS, 네이버 등", "KakaoPay, Toss, PASS, Naver, and more")),
             (EQUAL_I, ("법적 효력은 똑같아요", "Equal legal effect"), ("어느 걸 써도 서명으로 인정돼요", "any of them counts as a valid signature"), "warm"),
             (TECH_I, ("기술(PKI)은 그대로예요", "The underlying tech (PKI) is unchanged"), ("바뀐 건 법이지, 암호 방식이 아니에요", "what changed was the law, not the cryptography")),
         ])},
        {"svg": svg(320, '<rect width="380" height="320" fill="var(--bad-soft)"/><rect x="380" width="380" height="320" fill="var(--good-soft)"/>'
                    + label(190, 30, "⟦2020년 이전|before 2020⟧", 13, "var(--ink)", cls="d")
                    + label(190, 80, "⟦공인인증서 하나만 법적 효력|only the accredited certificate counted⟧", 11, "var(--ink)") + label(190, 110, "⟦특정 보안 프로그램 강제|a specific security program was mandatory⟧", 11, "var(--ink)")
                    + label(570, 30, "⟦2020년 이후|after 2020⟧", 13, "var(--ink)", cls="d")
                    + label(570, 80, "⟦여러 민간 인증서가 동등한 효력|many private certificates carry equal effect⟧", 11, "var(--ink)") + label(570, 110, "⟦앱 하나로 간편 인증 가능|simple app-based authentication is enough⟧", 11, "var(--ink)")
                    + idcard(190, 220) + idcard(570, 220)
                    + label(380, 290, "⟦신분증 자체는 그대로, 발급하는 곳이 늘었을 뿐이에요|the ID card itself didn't change — only who may issue it did⟧", 12, "var(--ink)", cls="d")),
         "alt": ("왼쪽: 2020년 이전엔 공인인증서만 법적 효력. 오른쪽: 2020년 이후엔 여러 민간 인증서가 동등한 효력", "Left: before 2020, only the accredited certificate had legal effect. Right: after 2020, many private certificates carry equal effect"),
         "caption": ("전과 후를 나란히 보면 이래요.", "Side by side, here's before and after."),
         "small": ("신분증(인증서) 자체의 구조는 그대로예요. 달라진 건 누가 발급할 수 있느냐예요.", "The ID card (the certificate) itself is structurally unchanged — what changed is who's allowed to issue one.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.85, **CLERK_A) + label(190, 230, "⟦도장 찍는 방식(PKI)은 여전히 똑같아요|the stamping mechanism (PKI) is still exactly the same⟧", 11, "var(--muted)")
                    + person(560, 150, s=0.85, **CLERK_B) + label(560, 230, "⟦어느 도장집을 믿을지는 여전히 중요해요|which shop to trust still matters just as much⟧", 11, "var(--ink)")
                    + label(380, 280, "⟦바뀐 건 법이지, 왕의 도장이 찍히는 원리는 그대로예요|the law changed — the principle behind the king's seal did not⟧", 12, "var(--ink)", cls="d")),
         "alt": ("도장 찍는 방식(PKI)은 그대로이며, 어느 도장집을 믿을지는 여전히 중요함. 바뀐 건 법일 뿐 원리는 그대로", "The stamping mechanism (PKI) stayed the same, and which shop to trust still matters. Only the law changed, not the underlying principle"),
         "caption": ("바뀐 건 법이지, 암호 원리가 아니에요.", "What changed was the law — not the underlying cryptography."),
         "small": ('도장을 실제로 찍고 확인하는 방식은 그대로 <a href="pki-ko.html">PKI</a>예요. → <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>',
                   'The actual mechanism for stamping and checking the seal is still plain old <a href="pki-en.html">PKI</a>. → <a href="pki-en.html">the badge with the king\'s seal</a>')},
    ],
    "summary": (("과거엔 <b>공인인증서</b> 하나만 법적 효력이 있는 도장집이었지만, <b>2020년 전자서명법 개정</b>으로 그 특혜가 사라지고 여러 <b>사설(민간) 인증서</b>가 <b>동등한 법적 효력</b>을 갖게 됐어요.",
                 "There used to be only one seal-shop with legal effect — the <b>accredited certificate</b> — but the <b>2020 amendment to the Digital Signature Act</b> ended that privilege, giving several <b>private certificates</b> <b>equal legal standing</b>."),
                ("공인인증서는 1999년 전자서명법 제정 이후 정부가 지정한 공인인증기관만 발급할 수 있었고, 민간 전자서명보다 높은 법적 추정력을 가졌어요. 2020년 전자서명법 전부개정으로 이 특별한 지위가 폐지되고, 기존 공인인증서는 '공동인증서'라는 이름으로 남아 카카오페이·PASS·네이버 등 다른 사설인증과 동등한 효력을 갖게 됐어요. 기술적으로는 공인·사설 모두 PKI(공개키 기반 구조)를 쓰며, 달라진 건 법적 지위일 뿐이에요.",
                 "After the 1999 Digital Signature Act, only government-designated accredited certificate authorities could issue a 공인인증서, which carried a stronger legal presumption than private electronic signatures. The 2020 full revision of the Act abolished that special status; the old certificate survives as the renamed '공동인증서' (Joint Certificate), now standing on equal legal footing with other private certificates like KakaoPay, PASS, and Naver. Technically, both accredited and private certificates run on PKI (Public Key Infrastructure) — what changed was the legal status, not the cryptography.")),
    "glossary": [
        ("공인인증서", "Accredited certificate", ("예전엔 하나뿐이던 법적 도장집.", "Once the only seal-shop with legal weight."), ("2020년 개정 후 '공동인증서'로 이름이 바뀌었어요.", "Renamed '공동인증서' (Joint Certificate) after the 2020 amendment.")),
        ("사설(민간) 인증서", "Private certificate", ("새로 생긴 다른 도장집들.", "The new, other seal-shops."), ("카카오페이·PASS·네이버 등, 이제 법적 효력이 동등해요.", "KakaoPay, PASS, Naver, and more — now carrying equal legal effect.")),
        ("전자서명법", "Digital Signature Act", ("도장집 자격을 정하는 법.", "The law that decides who may run a seal-shop."), ("2020년 전부개정으로 공인인증서의 특별 지위를 없앴어요.", "The 2020 full revision ended the accredited certificate's special status.")),
        ("공동인증서", "Joint certificate", ("옛 공인인증서의 새 이름.", "The old accredited certificate's new name."), ("특혜는 사라졌지만, 여전히 쓸 수 있는 선택지 중 하나예요.", "The privilege is gone, but it's still one option among many.")),
        ("PKI", "PKI", ("도장을 실제로 찍고 확인하는 기술.", "The actual mechanism for stamping and checking the seal."), ('공인·사설 모두 이 기술을 써요. → <a href="pki-ko.html">왕의 도장이 찍힌 신분증</a>', 'Both accredited and private certificates run on this. → <a href="pki-en.html">the badge with the king\'s seal</a>')),
        ("전자서명", "Digital signature", ("편지 끝에 찍는 왕의 도장.", "The king's seal stamped at the end of a letter."), ("법적으로 손으로 쓴 서명과 같은 효력을 가져요.", "Legally carries the same weight as a handwritten signature.")),
        ("간편 인증", "Simple authentication", ("앱 하나로 끝나는 본인 확인.", "Identity verification done with just one app."), ('마이데이터·금융 서비스에서 흔히 봐요. → <a href="mydataSec-ko.html">내 장부는 내가 들고 다닐 권리</a>', 'Commonly seen across MyData and financial services. → <a href="mydataSec-en.html">my right to carry my own ledger</a>')),
        ("법적 추정력", "Legal presumption", ("법이 신뢰해주는 정도.", "How much trust the law grants it."), ("공인인증서만 특별히 더 높았던 것이, 개정 후 동등해졌어요.", "Once uniquely stronger for the accredited certificate — equalized after the amendment.")),
    ],
}
