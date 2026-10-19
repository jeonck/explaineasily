from _draw import *
from _world import *


def trafficlight(x, y, s=1.0, color="var(--bad)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-8" y="-30" width="16" height="40" fill="#2E3D57"/>'
            f'<circle r="7" fill="{color}"/></g>')


def citygrid(x, y, s=1.0):
    out = f'<g transform="translate({x},{y}) scale({s})">'
    for i, h in enumerate((70, 110, 50, 90, 60)):
        out += f'<rect x="{i*44}" y="{130-h}" width="34" height="{h}" fill="#5A6B85"/>'
    return out + '</g>'


def car(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-26" y="-10" width="52" height="20" rx="6" fill="var(--accent)"/>'
            f'<circle cx="-14" cy="12" r="7" fill="#142033"/><circle cx="14" cy="12" r="7" fill="#142033"/></g>')


# 1. 신호등이 교통량과 상관없이 정해진 대로만 바뀌어요
P1 = svg(300, sky(300)
         + trafficlight(300, 150, 1.2) + trafficlight(460, 150, 1.2, color="var(--good)")
         + car(150, 200, 1.0) + car(220, 200, 0.9) + car(190, 230, 0.8)
         + person(560, 190, s=0.8, face=FROWN, **DEMO)
         + bubble(500, 90, 220, 46, "⟦이쪽은 꽉 막혔는데 신호는 그대로예요|this side is jammed, but the light won't change⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦차가 없는 쪽도, 많은 쪽도 똑같은 시간만 기다려요|empty side or packed side, the timer doesn't care⟧", 12, "var(--ink)"))


# 2. 도시 시스템이 따로 놀아요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(60, 60, 200, 150, 1.0, "var(--muted)", "⟦교통|TRAFFIC⟧")
         + booth(290, 60, 200, 150, 1.0, "var(--muted)", "⟦전력|POWER⟧")
         + booth(520, 60, 200, 150, 1.0, "var(--muted)", "⟦수도|WATER⟧")
         + label(380, 250, "⟦각자 자기 것만 보느라 도시 전체는 아무도 안 봐요|each watches only its own, nobody watches the whole city⟧", 13, "var(--ink)")
         + label(380, 282, "⟦그래서 비효율이 생겨요|and that's where the inefficiency comes from⟧", 12, "var(--muted)"))

# 3. 스마트시티 = 도시가 함께 조율됨 (hero)
P3 = svg(340, sky(340, ground=False)
         + citygrid(80, 60, 1.0)
         + screen(380, 70, 1.6, citygrid(10, 54, 0.5))
         + trafficlight(300, 220, 0.8, color="var(--good)") + car(130, 250, 0.9)
         + label(380, 30, "⟦스마트시티 = 도시 곳곳 데이터를 모아 교통·에너지·안전을 함께 조율해요|Smart City = citywide data gathered to coordinate traffic, energy, and safety together⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦차가 몰리는 쪽 신호가 먼저 바뀌어요|the busier side's light changes first⟧", 12, "var(--muted)"))

CITY_TRAFFIC = icon('<rect x="24" y="8" width="16" height="40" rx="4" fill="#2E3D57"/><circle cx="32" cy="18" r="6" fill="var(--bad)"/><circle cx="32" cy="32" r="6" fill="var(--accent)"/><circle cx="32" cy="46" r="6" fill="var(--good)"/>')
CITY_ENERGY = icon('<path d="M34 8 L16 34 h12 l-6 22 l22 -28 h-12z" fill="var(--accent)"/>')
CITY_ALERT = icon('<path d="M32 8 L54 48 H10 Z" fill="var(--bad)"/><rect x="29" y="22" width="6" height="14" fill="#fff"/><circle cx="32" cy="42" r="3" fill="#fff"/>')
CITY_DATA = icon('<circle cx="32" cy="32" r="22" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="32" cy="32" r="6" fill="var(--accent)"/><circle cx="18" cy="18" r="4" fill="var(--good)"/><circle cx="46" cy="18" r="4" fill="var(--good)"/><circle cx="18" cy="46" r="4" fill="var(--good)"/>')

# 4. 네 겹 구조
P4 = svg(360, sky(360, ground=False)
         + infoboard(130, 30, 500, 290, "⟦스마트시티 구조|HOW IT'S LAYERED⟧",
                     ("⟦센서망 — 도시 곳곳에서 데이터 수집|sensor network — gathers data citywide⟧",
                      "⟦데이터 플랫폼 — 한곳에 모아 분석|data platform — collects and analyzes it⟧",
                      "⟦교통·환경 서비스 — 신호·대기질 조율|traffic/environment services — coordinate lights, air quality⟧",
                      "⟦안전 서비스 — 재난 조기경보|safety services — early disaster warning⟧"), 1.3)
         + label(380, 345, "⟦스마트팩토리와 같은 뼈대를, 도시 규모로 키운 거예요|the same skeleton as a smart factory, scaled up to a city⟧", 12, "var(--ink)"))

# 5. 한계: 개인정보와 단일장애점
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(190, 150, s=0.85, face=EYES, **VISITOR) + label(190, 80, "⟦내 이동 기록도 모이나요?|does it collect my movements too?⟧", 11, "var(--ink)")
         + label(190, 240, "⟦개인정보 수집 범위를 늘 따져봐야 해요|how much personal data it collects needs constant scrutiny⟧", 11, "var(--ink)")
         + screen(570, 100, 1.3, '<text x="40" y="30" text-anchor="middle" font-size="22" fill="var(--bad)">✕</text>')
         + label(570, 240, "⟦데이터 플랫폼이 멈추면 도시 전체가 흔들려요|if the data platform goes down, the whole city wobbles⟧", 11, "var(--ink)")
         + label(380, 282, "⟦마이데이터처럼, 누구 정보인지·어떻게 지키는지가 중요해요|like MyData, whose information it is and how it's protected matters⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "smartcity", "order": 6,
    "title": ("함께 숨 쉬는 도시 모형", "The City Model That Breathes Together"),
    "h1": ("<em>스마트시티</em>가 뭐예요?", "What is a <em>Smart City</em>?"),
    "sub": ("스마트시티를, 교통·전력·수도가 따로 놀던 도시가 데이터로 함께 조율되는 이야기로 풀어봤어요.",
            "Smart city, told as a story about traffic, power, and water — once disconnected — now coordinated together by data."),
    "panels": [
        {"svg": P1, "alt": ("차가 몰린 쪽 신호등은 그대로인데 빈 쪽 신호등만 초록불임", "The jammed side's light stays red while the empty side turns green anyway"),
         "caption": ("이쪽은 꽉 막혔는데 신호는 그대로예요.", "This side is jammed, but the light won't change."),
         "small": ("차가 없는 쪽도, 많은 쪽도 똑같은 시간만 기다려요.", "Empty side or packed side, the timer doesn't care.")},
        {"svg": P2, "alt": ("교통·전력·수도 부스가 서로 떨어져 따로 운영됨", "Traffic, power, and water booths sit apart, each run on its own"),
         "caption": ("각자 자기 것만 보느라 도시 전체는 아무도 안 봐요.", "Each watches only its own — nobody watches the whole city."),
         "small": ("그래서 비효율이 생겨요.", "And that's where the inefficiency comes from.")},
        {"svg": P3, "hero": True, "alt": ("도시 모형과 화면 속 도시 쌍둥이가 나란히 있고, 차가 몰린 쪽 신호가 바뀜", "A city model and its on-screen twin side by side, the busier light changing first"),
         "caption": ("스마트시티는 도시 곳곳 데이터를 모아 교통·에너지·안전을 함께 조율해요.", "A smart city gathers citywide data to coordinate traffic, energy, and safety together."),
         "small": ("차가 몰리는 쪽 신호가 먼저 바뀌어요.", "The busier side's light changes first."),
         "tricks": (4, [
             (CITY_TRAFFIC, ("교통 신호 조정", "Adjust traffic lights"), ("실시간 교통량대로요", "based on live traffic"), "calm"),
             (CITY_ENERGY, ("에너지 최적화", "Optimize energy use"), ("쓰는 만큼만 보내요", "sent just as much as needed")),
             (CITY_ALERT, ("재난 조기경보", "Early disaster warning"), ("더 빨리 알려요", "warns sooner")),
             (CITY_DATA, ("시민 데이터 활용", "Use citizen data"), ("서비스를 더 낫게 해요", "to improve services"), "warm"),
         ])},
        {"svg": P4, "alt": ("센서망·데이터 플랫폼·교통환경 서비스·안전 서비스 네 겹 구조도", "A four-layer diagram: sensor network, data platform, traffic/environment, safety services"),
         "caption": ("스마트팩토리와 같은 뼈대를 도시 규모로 키운 거예요.", "The same skeleton as a smart factory, scaled up to a city."),
         "small": ("센서망이 모은 데이터를 데이터 플랫폼이 모아 서비스로 내보내요.", "The sensor network's data flows through the platform into services.")},
        {"svg": P5, "alt": ("왼쪽: 관람객이 개인정보 수집을 걱정함. 오른쪽: 데이터 플랫폼이 멈추면 도시 전체가 흔들림", "Left: a visitor worries about personal data collection. Right: the data platform going down wobbles the whole city"),
         "caption": ("개인정보 수집 논란과 단일장애점 위험이 따라와요.", "Personal-data concerns and single-point-of-failure risk come along with it."),
         "small": ("마이데이터처럼, 누구 정보인지·어떻게 지키는지가 중요해요.", "Like MyData, whose information it is and how it's protected matters.")},
    ],
    "summary": (("<b>스마트시티</b>는 도시 곳곳의 센서 데이터를 모아 <b>교통·에너지·안전을 함께 조율</b>하는 도시로, 개인정보 보호와 단일장애점 위험을 함께 관리해야 해요.",
                 "A <b>smart city</b> gathers citywide sensor data to <b>coordinate traffic, energy, and safety together</b> — while managing personal-data protection and single-point-of-failure risk."),
                ("스마트시티는 IoT 센서망·통합 데이터 플랫폼·각종 서비스(교통·에너지·안전·행정)를 연결해 도시 자원을 실시간으로 최적화하는 개념이에요. 스마트팩토리의 구조를 도시 규모로 확장한 형태에 가깝고, 수집되는 데이터의 양이 많은 만큼 개인정보 보호와 데이터 플랫폼 장애 시 여러 서비스가 동시에 영향받는 위험을 함께 설계해야 해요.",
                 "A smart city connects IoT sensor networks, an integrated data platform, and various services (traffic, energy, safety, administration) to optimize city resources in real time. It's close to a smart factory's structure scaled up to city size, and because it collects so much data, personal-data protection and the risk of a platform outage hitting many services at once both need to be designed for.")),
    "glossary": [
        ("스마트시티", "Smart City", ("도시 곳곳의 데이터로 함께 조율되는 도시.", "A city coordinated by citywide data."), ("스마트팩토리의 도시 버전이에요.", "The city-scale version of a smart factory.")),
        ("스마트팩토리", "Smart Factory", ("공장 규모의 같은 생각.", "The same idea, at factory scale."), ('구조가 거의 같아요. → <a href="smartfactory-ko.html">스마트팩토리 부스</a>', "Nearly the same structure. → <a href=\"smartfactory-en.html\">the Smart Factory booth</a>")),
        ("디지털 트윈", "Digital Twin", ("도시를 화면 속에 그대로 복제한 쌍둥이.", "A twin of the city, replicated on screen."), ('스마트시티 화면도 이 기술을 써요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "The city's screen uses this same technology. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
        ("마이데이터", "MyData", ("내 정보를 내가 통제하는 제도.", "A system letting you control your own data."), ('개인정보 수집 논란과 맞닿아요. → <a href="mydataTech-ko.html">마이데이터 부스</a>', 'Connects to the personal-data concern here. → <a href="mydataTech-en.html">the MyData booth</a>')),
        ("단일장애점", "Single Point of Failure", ("한 곳이 멈추면 전체가 흔들리는 지점.", "The one spot whose failure wobbles everything."), ("데이터 플랫폼이 이 지점이 되기 쉬워요.", "The data platform easily becomes this spot.")),
        ("IoT 센서망", "IoT Sensor Network", ("도시 곳곳에 심어둔 눈과 귀.", "Eyes and ears planted all over the city."), ("모든 서비스의 출발점이에요.", "The starting point for every service.")),
        ("엣지 컴퓨팅", "Edge Computing", ("신호등처럼 급한 판단은 가까이서.", "Urgent calls, like traffic lights, decided nearby."), ('교차로 근처에서 즉시 판단할 때 쓰여요. → <a href="edgecompute-ko.html">엣지 컴퓨팅 부스</a>', 'Used for instant decisions near the intersection. → <a href="edgecompute-en.html">the Edge Computing booth</a>')),
        ("도시 행정", "Urban Administration", ("데이터를 받아 실제 정책으로 옮기는 몫.", "The job of turning data into actual policy."), ("기술이 다가 아니라, 운영도 중요해요.", "Technology alone isn't enough — operations matter too.")),
    ],
}
