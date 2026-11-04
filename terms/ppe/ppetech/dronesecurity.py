from _draw import *
from _world import *

DRONE_P = ('<circle cx="32" cy="32" r="10" fill="#5B8DEF"/>'
           '<path d="M10 14 L24 26 M54 14 L40 26 M10 50 L24 38 M54 50 L40 38" stroke="#5B8DEF" stroke-width="4" stroke-linecap="round"/>'
           '<circle cx="10" cy="14" r="6" fill="none" stroke="#5B8DEF" stroke-width="3"/><circle cx="54" cy="14" r="6" fill="none" stroke="#5B8DEF" stroke-width="3"/>'
           '<circle cx="10" cy="50" r="6" fill="none" stroke="#5B8DEF" stroke-width="3"/><circle cx="54" cy="50" r="6" fill="none" stroke="#5B8DEF" stroke-width="3"/>')
SIGNAL_P = '<path d="M32 14 a20 20 0 0 1 0 36 M32 22 a12 12 0 0 1 0 20" fill="none" stroke="var(--bad)" stroke-width="4"/><circle cx="32" cy="32" r="4" fill="var(--bad)"/>'
MASKFACE = '<path d="M14 24 h36 v14 h-36z" fill="#111C30"/><circle cx="24" cy="31" r="3" fill="var(--bad)"/><circle cx="40" cy="31" r="3" fill="var(--bad)"/>'
LOCATION_P = '<path d="M32 10 a16 16 0 0 1 16 16 c0 14 -16 28 -16 28 s-16 -14 -16 -28 a16 16 0 0 1 16 -16z" fill="none" stroke="var(--good)" stroke-width="4"/><circle cx="32" cy="26" r="6" fill="var(--good)"/>'
DRONE_I, SIGNAL_I, MASK2_I, LOCATION_I = icon(DRONE_P), icon(SIGNAL_P), icon(MASKFACE), icon(LOCATION_P)


def glyph(x, y, s, inner):
    """패널 SVG 안에 직접 박는 작은 그림(아이콘을 nested <svg>로 끼우면 XML 파싱이 깨져서, <g>로 대신 그린다)."""
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'

# 1. 드론 시연장이 인기 만점이에요
P1 = svg(300, sky(300)
         + person(560, 120, s=0.5, face=SMILE, **DEMO) + glyph(536, 70, 0.75, DRONE_P)
         + person(180, 145, s=0.85, face=SMILE, **VISITOR)
         + bubble(260, 90, 220, 40, "⟦드론이 혼자 하늘을 날아다녀요!|the drone flies around all by itself!⟧", 12, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦드론을 무선 신호로 조종하는 모습을 다들 신기하게 쳐다봐요|everyone watches, amazed that radio signals steer the drone⟧", 12, "var(--ink)"))

# 2. 그 무선 신호를 누가 가로채면 어떡하죠?
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(560, 120, s=0.5, face=FROWN, **DEMO) + glyph(536, 70, 0.75, DRONE_P)
         + glyph(420, 60, 0.7, SIGNAL_P)
         + person(220, 150, s=0.75, face=MASKFACE, hat=None, shirt="#3A3A3A")
         + bubble(140, 70, 210, 40, "⟦제가 대신 조종해도 되죠?|mind if I take the controls instead?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦무선 신호는 눈에 안 보여서, 공격자가 끼어들어도 알아채기 어려워요|radio signals are invisible, so it's hard to notice an attacker slipping in⟧", 12, "var(--ink)"))

# 3. 드론 보안위협 = 보이지 않는 조종 신호를 노리는 위협들 (hero)
P3 = svg(340, sky(340)
         + glyph(356, 90, 0.75, DRONE_P)
         + person(220, 220, s=0.85, face=EYES, **DEMO) + person(540, 220, s=0.75, face=FROWN, hat=None, shirt="#3A3A3A")
         + label(380, 30, "⟦드론 보안위협 = 하늘을 나는 드론을 노리는, 보이지 않는 공격들|drone security threats = unseen attacks that target a drone in the sky⟧", 13, "var(--ink)", cls="d")
         + label(380, 332, "⟦공격자는 조종 신호·위치 정보·촬영 영상을 모두 노릴 수 있어요|attackers can target the control signal, the location data, even the camera feed⟧", 12, "var(--muted)"))

# 4. 네 가지 공격 경로 비교표
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 260, "⟦시연장 드론, 이렇게 뚫려요|HOW THE DEMO DRONE GETS HIT⟧",
                     ("⟦재밍 — 신호를 방해해 조종을 끊어요|jamming — block the signal, cut off control⟧",
                      "⟦스푸핑 — 가짜 GPS로 드론 길을 속여요|spoofing — fake GPS, the drone strays⟧",
                      "⟦하이재킹 — 조종을 통째로 빼앗아요|hijacking — seize the controls entirely⟧",
                      "⟦도청 — 촬영 영상을 몰래 훔쳐봐요|eavesdropping — secretly watch the camera feed⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦막으려면: 신호를 암호화하고, 끊기면 드론을 복귀시켜요|defense: encrypt the link; return the drone if it's cut⟧", 11, "var(--muted)"))

# 5. 시연장 vs 실제 하늘 - 간극은 더 커요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 70, 0.75, DRONE_P) + glyph(166, 150, 0.6, LOCATION_P)
         + label(190, 250, "⟦시연장은 신호를 관리하는 좁은 공간이에요|the demo hall is a small space with managed signal⟧", 11, "var(--ink)")
         + glyph(546, 70, 0.75, DRONE_P) + label(570, 148, "⟦?|?⟧", 26, "var(--bad)", cls="d")
         + label(570, 250, "⟦진짜 하늘에서는 전파가 뒤섞이고 간섭도 많아요|the real sky is noisy — signals mix and interfere⟧", 11, "var(--ink)")
         + label(380, 282, "⟦시연장에서 잘 날아도, 실제 하늘에는 안 보이는 위협이 훨씬 많아요|a drone that flies fine in the hall faces far more unseen threats in the real sky⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "dronesecurity", "order": 16,
    "title": ("보이지 않는 줄로 매달린 드론", "The Drone Held Up by an Invisible String"),
    "h1": ("<em>드론 보안위협</em>이 뭐예요?", "What are <em>Drone Security Threats</em>?"),
    "sub": ("드론 보안위협을, 전시장 드론 시연을 노릴 수 있는 보이지 않는 공격 이야기로 풀어봤어요.",
            "Drone security threats, told as a story about the unseen attacks that could target the hall's drone demo."),
    "panels": [
        {"svg": P1, "alt": ("관람객이 드론 시연을 보며 신기해함", "A visitor watches the drone demo, amazed"),
         "caption": ("드론 시연장이 인기 만점이에요.", "The drone demo booth is a hit."),
         "small": ("드론을 무선 신호로 조종하는 모습을 다들 신기하게 쳐다봐요.", "Everyone watches, amazed that radio signals steer the drone.")},
        {"svg": P2, "alt": ("수상한 사람이 드론 조종 신호에 끼어들려 함", "A suspicious figure tries to slip into the drone's control signal"),
         "caption": ("드론을 조종하는 무선 신호를 누가 가로채면 어떡하죠?", "What if someone intercepts the radio signal steering the drone?"),
         "small": ("무선 신호는 눈에 안 보여서, 공격자가 끼어들어도 알아채기 어려워요.", "Radio signals are invisible, so it's hard to notice an attacker slipping in.")},
        {"svg": P3, "hero": True, "alt": ("드론이 하늘에 떠 있고, 시연 담당자와 수상한 인물이 양쪽에 서 있음", "A drone hovers in the air with a demo staffer on one side and a suspicious figure on the other"),
         "caption": ("드론 보안위협은 드론을 노리는 보이지 않는 공격들이에요.", "Drone security threats are unseen attacks that target a drone in the sky."),
         "small": ("공격자는 조종 신호·위치 정보·촬영 영상을 모두 노릴 수 있어요.", "Attackers can target the control signal, the location data, even the camera feed."),
         "tricks": (4, [
             (SIGNAL_I, ("재밍", "Jamming"), ("조종 신호를 방해해 조종을 끊어요", "jams the control signal to cut off control"), "warm"),
             (LOCATION_I, ("스푸핑", "Spoofing"), ("가짜 GPS로 드론의 위치를 속여요", "fools the drone with fake GPS positions")),
             (DRONE_I, ("하이재킹", "Hijacking"), ("드론 조종을 통째로 뺏어요", "seizes the drone's controls entirely"), "warm"),
             (MASK2_I, ("도청", "Eavesdropping"), ("드론 촬영 영상을 몰래 훔쳐봐요", "secretly watches the drone's camera feed")),
         ])},
        {"svg": P4, "alt": ("드론이 뚫리는 네 가지 경로 설명판: 재밍·스푸핑·하이재킹·도청", "A board lists four ways the demo drone gets attacked: jamming, spoofing, hijacking, eavesdropping"),
         "caption": ("드론은 재밍·스푸핑·하이재킹·도청, 네 가지 경로로 뚫릴 수 있어요.", "A drone can be hit four ways: jamming, spoofing, hijacking, and eavesdropping."),
         "small": ("막으려면 조종 신호를 암호화하고, 신호가 끊기면 드론을 자동 복귀시켜요.", "To defend, encrypt the control link, and have the drone auto-return if the signal is cut.")},
        {"svg": P5, "alt": ("왼쪽: 시연장은 신호가 관리되는 좁은 공간. 오른쪽: 진짜 하늘은 전파가 뒤섞여 더 위험함", "Left: the demo hall is a small, managed space. Right: the real sky is noisy and more dangerous"),
         "caption": ("시연장은 신호가 관리되지만, 진짜 하늘은 전파가 뒤섞여 드론이 더 위험해요.", "The demo hall has managed signals, but in the real sky radio waves mix and the drone is at greater risk."),
         "small": ("시연장에서 잘 날아도, 실제 하늘에는 안 보이는 위협이 훨씬 많아요.", "A drone that flies fine in the hall faces far more unseen threats in the real sky.")},
    ],
    "summary": (("<b>드론 보안위협</b> = 드론을 조종하는 <b>보이지 않는 무선 신호와 위치 정보</b>를 노리는 공격들.",
                 "<b>Drone security threats</b> = attacks that target the invisible radio link and location data that steer a drone."),
                ("드론 보안위협은 GPS 스푸핑, 전파 재밍, 조종 신호 하이재킹, 영상 데이터 도청 등 무선 통신에 의존하는 드론의 구조적 약점을 노리는 공격을 말해요. 암호화된 통신, 이상 신호 탐지, 신호 두절 시 자동 복귀(fail-safe) 같은 대응이 함께 쓰여요.",
                 "Drone security threats refer to attacks — GPS spoofing, RF jamming, control-link hijacking, video eavesdropping — that exploit a drone's structural reliance on wireless communication. Countermeasures include encrypted links, anomaly detection, and fail-safe auto-return when the signal is lost.")),
    "glossary": [
        ("GPS 스푸핑", "GPS Spoofing", ("가짜 GPS 신호로 드론의 위치를 속이는 것.", "Faking GPS signals to lie to a drone about its location."), ("드론이 자기 위치를 잘못 믿게 만들어요.", "Tricks the drone into trusting the wrong position.")),
        ("전파 재밍", "RF Jamming", ("강한 전파로 조종 신호를 눌러버리는 것.", "Drowning out the control signal with strong radio noise."), ("신호를 잃은 드론은 기종과 설정에 따라 자동 복귀하거나, 제자리에 멈추거나, 추락해요.", "A drone that loses signal returns home, hovers, or falls, depending on its model and settings.")),
        ("하이재킹", "Hijacking", ("드론 조종을 통째로 빼앗는 것.", "Seizing a drone's controls entirely."), ("가장 직접적인 드론 탈취예요.", "The most direct form of taking over a drone.")),
        ("IoT 보안", "IoT Security", ("드론을 포함한 무선 기기를 지키는 보안.", "Security for wireless devices, drones included."), ('비슷한 위협을 더 넓게 다루는 세계가 있어요. → <a href="iotsec-ko.html">말 못 하는 기계들</a>', 'A broader take on the same kind of threat lives in another field. → <a href="iotsec-en.html">the machines that cannot speak</a>')),
        ("DDoS", "DDoS", ("한꺼번에 몰려와 먹통으로 만드는 공격.", "An attack that floods a target until it chokes."), ('조종 신호 대신 서버를 노리는 사촌 격 공격이에요. → <a href="ddos-ko.html">DDoS</a>', 'A cousin attack that floods a server instead of a control link. → <a href="ddos-en.html">DDoS</a>')),
        ("자율주행", "Autonomous Driving", ("센서로 보고 스스로 달리는 차.", "A car that senses its surroundings and drives itself."), ('드론과 달리 무선 신호보다 센서에 더 기대는 차를 다루는 부스예요. → <a href="autodrive-ko.html">자율주행</a>', 'A neighboring booth: unlike a drone, the car leans more on sensors than on radio signal. → <a href="autodrive-en.html">Autonomous Driving</a>')),
        ("CPS", "CPS", ("컴퓨터와 실제 기계가 맞물려 움직이는 것.", "Computer and real machine moving in lockstep."), ('드론도 이 틀 안의 한 예시예요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', 'A drone is one example living inside this bigger frame. → <a href="cps-en.html">Cyber-Physical Systems</a>')),
        ("정량적 위험분석", "Quantitative Risk Analysis", ("위협을 숫자로 매기는 방법.", "A way to score a threat with numbers."), ('이 드론 위협들의 크기도 이렇게 재요. → <a href="quantrisk-ko.html">정량적 위험분석 기법</a>', 'These drone threats get sized up the same way. → <a href="quantrisk-en.html">Quantitative Risk Analysis</a>')),
    ],
}
