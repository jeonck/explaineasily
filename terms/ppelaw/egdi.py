"""UN 전자정부 평가·EGDI."""
from _draw import *
from _world import *

OSI_I = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M18 22 h28 M18 32 h28 M18 42 h18" stroke="#142033" stroke-width="2.5" stroke-linecap="round"/>')
TII_I = icon('<path d="M12 50 h40 M20 50 V34 M32 50 V22 M44 50 V38" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>')
HCI_I = icon('<circle cx="24" cy="20" r="8" fill="var(--good)"/><rect x="12" y="32" width="24" height="20" rx="4" fill="var(--good)"/><circle cx="46" cy="26" r="6" fill="var(--good)" opacity="0.6"/><rect x="38" y="36" width="18" height="16" rx="3" fill="var(--good)" opacity="0.6"/>')
RULER_I = icon('<rect x="10" y="26" width="44" height="12" rx="2" fill="var(--accent)"/><path d="M18 26 v12 M26 26 v8 M34 26 v12 M42 26 v8" stroke="#FFF" stroke-width="2"/>')

# 1. 우리 학교 온라인 시스템, 최고인 줄 알았어요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SMILE, **REP) + bubble(130, 70, 260, 44, "⟦우리 학교 온라인 투표 시스템, 전국 최고 아니에요?|our school's online voting system — best in the country, right?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + noticeboard(560, 130, 1.1, "⟦온라인 투표|ONLINE VOTE⟧")
         + label(380, 280, "⟦비교 없이 혼자 '최고'라고 믿고 있었어요|believing we're \"the best,\" with nothing to compare against⟧", 13, "var(--ink)", cls="d"))

# 2. 막상 비교해보니 기준이 제각각이었어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SWEAT + EYES, **REP) + label(220, 250, "⟦옆 학교는 와이파이가 훨씬 빠르던데요|the school next door has way faster wifi⟧", 11, "var(--ink)")
         + person(560, 150, s=0.8, face=FROWN, **PRESIDENT) + label(560, 250, "⟦근데 뭘 기준으로 비교하죠?|but what standard do we even compare by?⟧", 11, "var(--ink)")
         + label(380, 285, "⟦같은 잣대가 없으면, 누가 더 나은지도 알 수 없어요|without a shared ruler, you can't even tell who's ahead⟧", 12, "var(--ink)", cls="d"))

# 3. EGDI = 외부 평가단이 같은 잣대로 모든 학교를 재는 평가 (hero)
P3 = svg(340, sky(340)
         + label(380, 26, "⟦EGDI = 외부 평가단이 같은 잣대로 모든 학교를 재는 평가|EGDI = an outside board measuring every school by the same ruler⟧", 13, "var(--ink)", cls="d")
         + person(380, 110, s=0.9, face=EYES, **TEACHER)
         + '<rect x="350" y="150" width="70" height="16" rx="3" fill="var(--accent)"/><path d="M360 150 v16 M375 150 v10 M390 150 v16 M405 150 v10" stroke="#fff" stroke-width="2"/>'
         + noticeboard(180, 170, 1.0, "⟦우리 학교|OUR SCHOOL⟧") + noticeboard(320, 190, 0.85, "⟦옆 학교|NEXT SCHOOL⟧") + noticeboard(460, 170, 1.0, "⟦이웃 학교|ANOTHER SCHOOL⟧")
         + noticeboard(600, 190, 0.85, "⟦먼 학교|A FAR SCHOOL⟧")
         + label(380, 330, "⟦모든 학교가 같은 세 가지 잣대로 비교당해요|every school gets compared by the same three measures⟧", 12, "var(--muted)"))

# 4. EGDI를 이루는 세 지수
P4 = svg(320, sky(320, ground=False)
         + rulesboard(60, 40, 640, 240, "⟦EGDI = 세 지수의 평균|EGDI = THE AVERAGE OF THREE INDEXES⟧",
                      ("⟦OSI(온라인서비스지수) — 웹사이트·서비스 수준|OSI (Online Service Index) — website and service quality⟧",
                       "⟦TII(통신인프라지수) — 인터넷 환경(와이파이·회선)|TII (Telecom Infrastructure Index) — internet environment⟧",
                       "⟦HCI(인적자본지수) — 학생·교직원이 얼마나 잘 쓰는가|HCI (Human Capital Index) — how well people use it⟧",
                       "⟦셋을 평균 내 하나의 EGDI 점수로|all three averaged into one EGDI score⟧"), 1.0)
         + label(380, 295, "⟦서비스만 좋아도, 회선이 느리면 점수가 낮아져요|great service alone isn't enough if the connection is slow⟧", 12, "var(--ink)", cls="d"))

# 5. 점수가 전부는 아니에요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + person(190, 150, s=0.8, face=SMILE, **TEACHER) + label(190, 250, "⟦같은 잣대로 재니 비교는 공정해요|the same ruler makes the comparison fair⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=FROWN, **REP) + label(570, 250, "⟦근데 학생들이 실제로 만족하는지는 또 다른 얘기예요|but whether students are actually happy is a different story⟧", 11, "var(--ink)")
         + label(380, 285, "⟦점수는 2년마다 한 번 찍는 사진이지, 매일의 진짜 모습은 아니에요|the score is a snapshot taken every two years — not the everyday reality⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "egdi", "order": 17,
    "title": ("같은 잣대로 모든 학교를 재는 평가단", "The Board That Measures Every School by the Same Ruler"),
    "h1": ("<em>UN 전자정부 평가(EGDI)</em>가 뭐예요?", "What is the <em>UN E-Government Development Index (EGDI)</em>?"),
    "sub": ("UN 전자정부 평가(EGDI)를, 외부 평가단이 모든 학교의 온라인서비스·통신환경·활용능력을 같은 잣대로 재는 이야기로 풀어봤어요.",
            "The UN's E-Government Development Index, told as a story about an outside board measuring every school's online services, connectivity, and how well people use them — all by the same ruler."),
    "panels": [
        {"svg": P1, "alt": ("대표가 우리 학교 온라인 투표 시스템이 전국 최고라고 자신하며 게시판을 가리킴", "A rep confidently points at a notice board, claiming their school's online voting system is the best in the country"),
         "caption": ("우리 학교 온라인 시스템, 최고인 줄 알았어요.", "We believed our school's online system was the best."),
         "small": ("비교 없이 혼자 '최고'라고 믿고 있었어요.", "Believing we're \"the best,\" with nothing to compare against.")},
        {"svg": P2, "alt": ("대표가 옆 학교 와이파이가 더 빠르다고 땀 흘리며 말하고, 학생회장은 비교 기준이 뭐냐고 물음", "A sweating rep admits a neighboring school's wifi is faster; the president asks what standard they're even comparing by"),
         "caption": ("막상 비교해보니 기준이 제각각이었어요.", "Trying to compare, the standards turned out to differ."),
         "small": ("같은 잣대가 없으면, 누가 더 나은지도 알 수 없어요.", "Without a shared ruler, you can't even tell who's ahead.")},
        {"svg": P3, "hero": True, "alt": ("선생님이 자를 들고 네 학교의 게시판을 같은 기준으로 잼", "A teacher holds a ruler, measuring four schools' notice boards against the same standard"),
         "caption": ("EGDI는 외부 평가단이 같은 잣대로 모든 학교를 재는 평가예요.", "EGDI is an outside board measuring every school by the same ruler."),
         "small": ("모든 학교가 같은 세 가지 잣대로 비교당해요.", "Every school gets compared by the same three measures."),
         "tricks": (4, [
             (OSI_I, ("온라인서비스지수(OSI)", "Online Service Index"), ("웹사이트·서비스 수준을 재요", "measures website and service quality"), "calm"),
             (TII_I, ("통신인프라지수(TII)", "Telecom Infrastructure Index"), ("와이파이·회선 환경을 재요", "measures the internet environment")),
             (HCI_I, ("인적자본지수(HCI)", "Human Capital Index"), ("쓰는 사람의 역량을 재요", "measures the people who use it"), "warm"),
             (RULER_I, ("같은 잣대로 비교", "Same ruler for everyone"), ("전세계 공통 기준으로요", "a single shared global standard")),
         ])},
        {"svg": P4, "alt": ("EGDI가 OSI·TII·HCI 세 지수의 평균으로 계산된다는 기준표", "A board showing EGDI calculated as the average of OSI, TII, and HCI"),
         "caption": ("EGDI는 세 지수를 평균 낸 점수예요.", "EGDI is the average of three sub-indexes."),
         "small": ("서비스만 좋아도, 회선이 느리면 점수가 낮아져요.", "Great service alone isn't enough if the connection is slow.")},
        {"svg": P5, "alt": ("왼쪽: 선생님이 같은 잣대라 공정하다고 말함. 오른쪽: 대표가 실제 만족도는 다른 얘기라고 말함", "Left: the teacher says the same ruler makes it fair. Right: the rep says real satisfaction is a different story"),
         "caption": ("점수가 전부는 아니에요.", "The score isn't everything."),
         "small": ("점수는 2년마다 한 번 찍는 사진이지, 매일의 진짜 모습은 아니에요.", "The score is a snapshot taken every two years — not the everyday reality.")},
    ],
    "summary": (("<b>EGDI</b> = UN이 <b>온라인서비스(OSI)·통신인프라(TII)·인적자본(HCI)</b> 세 지수를 <b>같은 잣대로 평균</b> 내 전 세계 전자정부 수준을 비교하는 지표.",
                 "<b>EGDI</b> = a UN index that compares e-government maturity worldwide by <b>averaging three sub-indexes, measured by the same ruler</b> — <b>Online Service (OSI), Telecom Infrastructure (TII), and Human Capital (HCI)</b>."),
                ("UN 전자정부 평가(E-Government Development Index)는 UN DESA(유엔 경제사회국)가 2년마다 193개 회원국을 대상으로 발표하는 지표예요. 온라인서비스지수(OSI, 정부 웹사이트·서비스 수준)·통신인프라지수(TII, 인터넷 보급·속도)·인적자본지수(HCI, 교육 수준·문해율)를 각각 측정해 평균을 내요. 국가 간 전자정부 수준을 같은 기준으로 비교할 수 있게 해주지만, 2년 주기 스냅샷이라 실시간 변화나 실제 이용 만족도까지는 담지 못해요.",
                 "The UN E-Government Development Index is published every two years by UN DESA for 193 member states. It averages three sub-indexes: the Online Service Index (OSI, government websites and services), the Telecommunication Infrastructure Index (TII, internet penetration and speed), and the Human Capital Index (HCI, education and literacy). It lets countries be compared by a shared standard, but being a two-year snapshot, it can't capture real-time change or actual user satisfaction.")),
    "glossary": [
        ("EGDI", "EGDI (E-Government Development Index)", ("같은 잣대로 모든 나라를 재는 평가.", "An index that measures every country by the same ruler."), ("2년마다 UN이 다시 발표해요.", "Re-published by the UN every two years.")),
        ("OSI", "OSI (Online Service Index)", ("웹사이트·서비스 수준을 재는 지수.", "Measures the quality of websites and services."), ("세 지수 중 '보이는 서비스' 담당이에요.", "The one in charge of the visible services.")),
        ("TII", "TII (Telecommunication Infrastructure Index)", ("와이파이·회선 환경을 재는 지수.", "Measures the internet and connectivity environment."), ("서비스가 좋아도 이게 나쁘면 점수가 낮아져요.", "Great service still scores low if this is weak.")),
        ("HCI", "HCI (Human Capital Index)", ("쓰는 사람의 역량(교육·문해율)을 재는 지수.", "Measures the people who use it — education and literacy."), ("기술이 좋아도 쓸 줄 모르면 소용없어요.", "Great tech is wasted if nobody can use it.")),
        ("UN DESA", "UN DESA", ("이 평가를 실제로 발표하는 기관.", "The body that actually publishes this index."), ("유엔 경제사회국이에요.", "The UN Department of Economic and Social Affairs.")),
        ("전자정부", "e-Government", ("행정 서비스를 온라인으로 제공하는 것.", "Delivering administrative services online."), ("EGDI가 재는 대상 그 자체예요.", "The very thing EGDI is measuring.")),
        ("디지털정부평가", "Digital Government Assessment", ("OECD 등 다른 기관의 비슷한 평가.", "A similar assessment by other bodies, like the OECD."), ("EGDI 말고도 평가 기준은 여럿 있어요.", "EGDI isn't the only yardstick out there.")),
        ("공공데이터 개방", "Open Government Data", ("온라인서비스지수를 끌어올리는 요소 중 하나.", "One factor that helps raise the online-service score."), ('표준을 지킨 데이터라야 열 수 있어요. → <a href="datastd-ko.html">전교가 함께 쓰는 공통 기준표</a>', 'Only standardized data is fit to open up. → <a href="datastd-en.html">the shared standard the whole school uses</a>')),
    ],
}
