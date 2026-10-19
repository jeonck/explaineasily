from _draw import *
from _world import *


def datadrawer(x, y, s=1.0, label_text=None, color="var(--muted)"):
    out = f'<g transform="translate({x},{y}) scale({s})"><rect x="-30" y="-24" width="60" height="48" rx="4" fill="{color}"/><rect x="-22" y="-10" width="44" height="8" rx="2" fill="#FFF8E7"/>'
    if label_text:
        out += label(0, 42, label_text, 11, "var(--ink)")
    return out + '</g>'


def dashboard(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="100" height="70" rx="4" fill="#1B2A44"/>'
            f'<rect x="8" y="8" width="40" height="24" rx="2" fill="var(--good)"/><rect x="52" y="8" width="40" height="24" rx="2" fill="var(--accent)"/>'
            f'<rect x="8" y="38" width="84" height="24" rx="2" fill="#5B8DEF"/></g>')


def sensorline(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 4"/>'


# 1. 내 정보가 뿔뿔이 흩어져 있어요
P1 = svg(350, sky(350, ground=False)
         + datadrawer(150, 110, 1.0, "⟦은행|bank⟧", "#5B8DEF")
         + datadrawer(380, 110, 1.0, "⟦병원|hospital⟧", "#2E8B57")
         + datadrawer(610, 110, 1.0, "⟦통신사|telecom⟧", "#C9822B")
         + person(380, 220, s=0.75, face=FROWN, **VISITOR)
         + label(380, 335, "⟦내 정보인데, 나는 한눈에 못 봐요|it's my own data, but I can't see it all at once⟧", 13, "var(--ink)"))

# 2. 각 기관은 자기네 것만 보여줘요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + datadrawer(190, 140, 1.2, "⟦은행은 은행 것만|bank shows only bank data⟧", "#5B8DEF")
         + datadrawer(570, 140, 1.2, "⟦병원은 병원 것만|hospital shows only hospital data⟧", "#2E8B57")
         + label(380, 250, "⟦정보 소유권이 모호해서, 기업들이 각자 쌓아만 둬요|unclear ownership means each company just stockpiles its own⟧", 12, "var(--ink)")
         + label(380, 280, "⟦나는 내 정보를 다른 곳으로 옮길 방법이 없었어요|I had no way to move my own data elsewhere⟧", 11, "var(--muted)"))

# 3. 마이데이터 = 내가 허락해서 한곳에 모아보기 (hero)
P3 = svg(350, sky(350, ground=False)
         + datadrawer(140, 110, 0.8, color="#5B8DEF") + datadrawer(260, 110, 0.8, color="#2E8B57") + datadrawer(380, 110, 0.8, color="#C9822B")
         + person(260, 210, s=0.8, face=EYES, **VISITOR) + label(260, 330, "⟦좋아요, 동의할게요|okay, I agree⟧", 11, "var(--ink)")
         + dashboard(500, 140, 1.4)
         + sensorline(190, 140, 540, 170) + sensorline(300, 140, 560, 170) + sensorline(400, 140, 580, 170)
         + label(380, 30, "⟦마이데이터 = 내가 허락해서, 내 정보를 한곳에 모아보고 다른 곳으로 옮길 수도 있는 제도|MyData = with my consent, my data gathers into one view — and can move elsewhere too⟧", 13, "var(--ink)", cls="d"))


MD_CONSENT = icon('<rect x="14" y="10" width="36" height="44" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M24 34 l6 6 l12 -14" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
MD_API = icon('<rect x="8" y="26" width="18" height="12" rx="3" fill="var(--accent)"/><rect x="38" y="26" width="18" height="12" rx="3" fill="var(--accent)"/><path d="M26 32 h12" stroke="var(--good)" stroke-width="4"/>')
MD_UNIFY = icon('<circle cx="20" cy="20" r="8" fill="var(--accent)"/><circle cx="44" cy="20" r="8" fill="var(--accent)"/><circle cx="32" cy="44" r="8" fill="var(--accent)"/><circle cx="32" cy="32" r="10" fill="var(--good)"/>')
MD_RECOMMEND = icon('<path d="M32 10 l6 14 h-12z" fill="var(--accent)"/><rect x="22" y="30" width="20" height="24" rx="3" fill="var(--accent)"/>')

# 4. 데이터 흐름
P4 = svg(360, sky(360, ground=False)
         + infoboard(130, 30, 500, 290, "⟦마이데이터 흐름|HOW IT FLOWS⟧",
                     ("⟦은행·통신·병원 — 흩어진 내 정보|bank, telecom, hospital — my scattered data⟧",
                      "⟦내가 동의 — 어디로 보낼지 내가 정해요|I consent — I decide where it goes⟧",
                      "⟦마이데이터 사업자 — 표준 API로 모아요|a MyData provider — gathers it via a standard API⟧",
                      "⟦내 통합 대시보드 — 한눈에 보여요|my unified dashboard — sees it all at once⟧"), 1.3)
         + label(380, 345, "⟦동의 없이는 이 흐름이 시작되지 않아요|nothing moves without my consent, first⟧", 12, "var(--ink)"))

# 5. 한계: 동의해도 유출 위험, 모든 기관이 다 참여하진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + dashboard(140, 150, 1.3) + label(190, 90, "⟦동의해도 유출 위험은 남아요|consenting doesn't erase breach risk⟧", 11, "var(--ink)")
         + datadrawer(600, 150, 1.0, "⟦표준 안 맞으면 못 가져와요|can't import it if standards don't match⟧", "var(--muted)")
         + label(380, 282, "⟦모든 기관이 다 참여하는 건 아니에요|not every institution participates⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "mydataTech", "order": 11,
    "title": ("흩어진 서랍을 내가 한곳에 모으기", "Gathering My Own Scattered Drawers Into One"),
    "h1": ("<em>마이데이터(MyData)</em>가 뭐예요?", "What is <em>MyData</em>?"),
    "sub": ("마이데이터를, 은행·병원·통신사에 흩어진 내 정보를 내가 직접 허락해서 한곳에 모아보는 이야기로 풀어봤어요.",
            "MyData, told as a story about gathering my own information — scattered across the bank, hospital, and telecom — into one view, with my own consent."),
    "panels": [
        {"svg": P1, "alt": ("은행·병원·통신사 서랍에 각각 내 정보가 흩어져 있고, 관람객은 한눈에 보지 못함", "My data sits scattered in separate drawers for bank, hospital, and telecom, and the visitor can't see it all"),
         "caption": ("내 정보인데, 나는 한눈에 못 봐요.", "It's my own data, but I can't see it all at once."),
         "small": ("각 기관에 뿔뿔이 흩어져 있어요.", "It's scattered across each institution.")},
        {"svg": P2, "alt": ("은행은 은행 것만, 병원은 병원 것만 보여줌", "The bank shows only its own data, and the hospital shows only its own"),
         "caption": ("각 기관은 자기네 것만 보여줘요.", "Each institution shows only its own data."),
         "small": ("나는 내 정보를 다른 곳으로 옮길 방법이 없었어요.", "I had no way to move my own data elsewhere.")},
        {"svg": P3, "hero": True, "alt": ("관람객이 동의하자 은행·병원·통신사의 정보가 선으로 이어져 통합 대시보드로 모임", "The visitor consents, and lines from bank, hospital, and telecom gather into a unified dashboard"),
         "caption": ("마이데이터는 내가 허락해서, 내 정보를 한곳에 모아보고 다른 곳으로 옮길 수도 있는 제도예요.", "MyData means that, with my consent, my data gathers into one view — and can move elsewhere too."),
         "small": ("'내 정보는 나의 것'이라는 생각에서 출발해요.", "It starts from the idea that 'my data is mine.'"),
         "tricks": (4, [
             (MD_CONSENT, ("본인이 동의해야 이동", "Moves only with my consent"), ("내가 허락해야 움직여요", "it moves only if I say yes"), "calm"),
             (MD_API, ("표준 API로 전송", "Transferred via standard API"), ("오픈뱅킹 같은 방식이에요", "like open banking")),
             (MD_UNIFY, ("한곳에서 통합 조회", "Viewed all in one place"), ("여러 기관 정보를 한눈에", "several institutions, one view")),
             (MD_RECOMMEND, ("맞춤 서비스 추천", "Personalized recommendations"), ("모은 정보로 더 맞게요", "tailored from the gathered data"), "warm"),
         ])},
        {"svg": P4, "alt": ("흩어진 정보가 동의를 거쳐 마이데이터 사업자를 통해 통합 대시보드로 흐르는 과정도", "A flow diagram: scattered data, consent, a MyData provider, then a unified dashboard"),
         "caption": ("동의 없이는 이 흐름이 시작되지 않아요.", "Nothing moves without my consent, first."),
         "small": ("표준화된 API로 흐르고, 마지막엔 내 대시보드에 모여요.", "It flows through a standard API and ends up on my own dashboard.")},
        {"svg": P5, "alt": ("왼쪽: 동의해도 유출 위험이 남음. 오른쪽: 표준이 안 맞으면 정보를 못 가져옴", "Left: consenting doesn't erase breach risk. Right: mismatched standards mean data can't be imported"),
         "caption": ("동의해도 유출 위험은 남고, 모든 기관이 다 참여하는 건 아니에요.", "Consenting doesn't erase breach risk, and not every institution participates."),
         "small": ("표준이 안 맞으면 가져올 수가 없어요.", "If the standards don't match, it can't be imported.")},
    ],
    "summary": (("<b>마이데이터</b>는 '<b>내 정보는 나의 것</b>'이라는 생각에서, 내가 직접 동의해 여러 기관의 내 정보를 한곳에 모아보고 다른 곳으로 옮길 수도 있게 하는 제도예요.",
                 "<b>MyData</b> starts from the idea that '<b>my data is mine</b>' — letting me consent to gather my own information from several institutions into one view, and move it elsewhere too."),
                ("마이데이터는 정보주체(개인)가 자신에 관한 데이터의 전송을 직접 요구할 수 있는 개인정보 이동권에 기반한 제도예요. 표준화된 API(오픈뱅킹 등)로 은행·통신·의료 등 여러 기관의 데이터를 본인 동의 하에 통합 조회하거나 제3자에게 전송할 수 있어요. 동의 절차가 있어도 유출 위험이 사라지는 건 아니고, 모든 기관이 표준을 지원하는 것도 아니라는 한계가 있어요.",
                 "MyData is a system built on the data subject's (an individual's) right to data portability — the right to directly request that their own data be transferred. Through standardized APIs (like open banking), it lets individuals view data from multiple institutions (banking, telecom, healthcare) together, or send it to a third party, all with their own consent. Even with a consent process, breach risk doesn't disappear, and not every institution supports the standard.")),
    "glossary": [
        ("마이데이터", "MyData", ("내 정보를 내가 모아보는 제도.", "A system letting me gather my own data."), ("본인 동의가 시작점이에요.", "It all starts with my own consent.")),
        ("개인정보 이동권", "Data Portability Right", ("내 데이터 전송을 내가 요구할 권리.", "My right to request my own data be transferred."), ("마이데이터 제도의 법적 기반이에요.", "The legal basis MyData rests on.")),
        ("오픈뱅킹", "Open Banking", ("표준 API로 은행 데이터를 주고받는 방식.", "Exchanging bank data via a standard API."), ("마이데이터의 대표적인 적용 사례예요.", "A leading example of MyData in practice.")),
        ("마이데이터 사업자", "MyData Provider", ("여러 기관의 데이터를 모아주는 중개자.", "The go-between that gathers data from several institutions."), ("표준 API로 데이터를 연결해요.", "Connects the data through standard APIs.")),
        ("데이터 유출", "Data Breach", ("동의해도 사라지지 않는 위험.", "A risk that doesn't vanish just because I consented."), ("마이데이터도 예외는 아니에요.", "MyData is no exception.")),
        ("스마트시티", "Smart City", ("도시 곳곳의 데이터를 모아 조율하는 것.", "Gathering citywide data to coordinate services."), ('개인정보 수집 범위 고민이 여기와 맞닿아요. → <a href="smartcity-ko.html">스마트시티 부스</a>', "Shares the same personal-data concern. → <a href=\"smartcity-en.html\">the Smart City booth</a>")),
        ("표준화", "Standardization", ("기관마다 형식이 달라 못 맞는 부분.", "The format mismatch between institutions."), ("표준이 안 맞으면 데이터를 못 가져와요.", "Without matching standards, data can't be imported.")),
        ("개인정보보호법", "Personal Data Protection Law", ("동의와 이동권을 뒷받침하는 법.", "The law behind consent and portability rights."), ("마이데이터 제도 운영의 근거예요.", "The legal ground MyData operates on.")),
    ],
}
