from _draw import *
from _world import *


def glyph(x, y, s, inner):
    return f'<g transform="translate({x},{y}) scale({s})">{inner}</g>'


def spinner(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-10" width="28" height="20" rx="4" fill="#1B2A44"/>'
            f'<circle r="10" fill="none" stroke="var(--accent)" stroke-width="3"/><circle r="3" fill="var(--accent)"/></g>')


LASER = ''.join(f'<path d="M0 0 L{dx} {dy}" stroke="var(--accent)" stroke-width="1.5" opacity="0.7"/>'
                 for dx, dy in ((120, -50), (130, -10), (125, 30), (100, 60), (60, 75)))
DOT_P = '<circle cx="20" cy="20" r="5" fill="var(--good)"/><circle cx="40" cy="26" r="5" fill="var(--good)"/><circle cx="24" cy="40" r="5" fill="var(--good)"/><circle cx="44" cy="44" r="5" fill="var(--good)"/>'
RULER_P = '<rect x="10" y="26" width="44" height="12" rx="2" fill="#E0E0E0" stroke="#8A8A8A" stroke-width="2"/><path d="M18 26 v12 M28 26 v12 M38 26 v12 M48 26 v12" stroke="#8A8A8A" stroke-width="2"/>'
CLOUD3D_P = ''.join(f'<circle cx="{c[0]}" cy="{c[1]}" r="3" fill="var(--accent)"/>' for c in
                     ((14, 44), (22, 30), (30, 48), (34, 20), (42, 36), (48, 50), (50, 16), (18, 16)))
SPIN_P = '<rect x="18" y="20" width="28" height="20" rx="4" fill="#1B2A44"/><circle cx="32" cy="30" r="10" fill="none" stroke="var(--accent)" stroke-width="3"/>'
DOT_I, RULER_I, CLOUD3D_I, SPIN_I = icon(DOT_P), icon(RULER_P), icon(CLOUD3D_P), icon(SPIN_P)

# 1. 안내원이 전시장 지도를 손으로 재서 그리느라 고생해요
P1 = svg(300, sky(300)
         + person(220, 150, s=0.85, face=SWEAT, **GUIDE)
         + infoboard(340, 90, 220, 140, "⟦손으로 그린 지도|HAND-DRAWN MAP⟧", ("⟦대충 그린 거리|rough guesses at distance⟧", "⟦모서리가 어긋나요|corners don't quite line up⟧"), 1.0)
         + label(380, 260, "⟦줄자로 벽까지 거리를 하나하나 재는 건 너무 오래 걸려요|measuring every wall's distance with a tape measure takes forever⟧", 12, "var(--ink)"))

# 2. 눈으로 보고 어림잡으면 자꾸 틀려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.85, face=FROWN, **GUIDE)
         + bubble(300, 70, 240, 44, "⟦저기까지 한 5미터쯤 되려나...|that looks about 5 meters away, maybe...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 270, "⟦눈대중은 사람마다 다르고, 어두우면 더 어려워요|eyeballing it differs person to person — and it's worse in the dark⟧", 12, "var(--ink)"))

# 3. LiDAR = 레이저를 쏘고 되돌아오는 시간으로 거리를 정확히 재는 눈 (hero)
P3 = svg(340, sky(340)
         + spinner(260, 200, 1.6)
         + f'<g transform="translate(260,200)">{LASER}</g>'
         + booth(420, 120, 220, 110, 1.0, "var(--stone-dark)", None)
         + person(600, 240, s=0.7, face=SMILE, **DEMO)
         + label(380, 30, "⟦LiDAR = 레이저를 쏘고 돌아오는 시간을 재서, 거리를 정확하게 아는 눈|LiDAR = an eye that times a laser's round trip to know distance exactly⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦빛의 속도는 늘 똑같으니, 시간만 재면 거리가 나와요|light always travels at the same speed, so timing it gives the distance⟧", 12, "var(--muted)"))

# 4. 레이저 점들이 모여 3D 지도가 돼요
P4 = svg(320, sky(320)
         + infoboard(60, 40, 320, 240, "⟦작동 순서|HOW IT WORKS⟧",
                     ("⟦① 레이저를 사방으로 빠르게 쏴요|① fire a laser rapidly in every direction⟧",
                      "⟦② 벽에 부딪혀 돌아오는 시간을 재요|② time how long it takes to bounce back⟧",
                      "⟦③ 거리 점 수백만 개가 쌓여요|③ millions of distance points pile up⟧",
                      "⟦④ 점들이 모여 3D 지도가 돼요|④ the points together form a 3D map⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **GUIDE)
         + label(560, 250, "⟦이 점들의 모임을 '포인트 클라우드'라고 불러요|this cluster of points is called a point cloud⟧", 11, "var(--muted)"))

# 5. 한계 - 비·안개엔 약하고, 가격도 비싸요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + glyph(166, 110, 1.3, CLOUD3D_P)
         + label(190, 250, "⟦맑은 날엔 밀리미터 단위로 정확해요|on a clear day it's accurate down to the millimeter⟧", 11, "var(--ink)")
         + spinner(570, 150, 1.2)
         + label(570, 250, "⟦비·안개에 레이저가 흩어지고, 장비도 비싸요|rain and fog scatter the laser, and the gear is pricey⟧", 11, "var(--ink)")
         + label(380, 282, "⟦정확한 눈이지만, 날씨와 가격이라는 벽은 남아 있어요|a precise eye, but weather and cost remain real walls⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "lidar", "order": 20,
    "title": ("레이저로 거리를 재는 회전하는 눈", "The Spinning Eye That Measures Distance with Lasers"),
    "h1": ("<em>LiDAR</em>가 뭐예요?", "What is <em>LiDAR</em>?"),
    "sub": ("LiDAR를, 레이저를 쏘고 돌아오는 시간으로 거리를 정확히 재는 회전하는 눈 이야기로 풀어봤어요.",
            "LiDAR, told as a story about a spinning eye that times a laser's round trip to measure distance exactly."),
    "panels": [
        {"svg": P1, "alt": ("안내원이 줄자로 전시장을 재서 지도를 그리느라 진땀을 흘림", "A guide sweats, measuring the hall with a tape measure to draw a map"),
         "caption": ("안내원이 전시장 지도를 손으로 재서 그리느라 고생해요.", "The guide struggles to hand-measure and draw the hall's map."),
         "small": ("줄자로 벽까지 거리를 하나하나 재는 건 너무 오래 걸려요.", "Measuring every wall's distance with a tape measure takes forever.")},
        {"svg": P2, "alt": ("안내원이 눈대중으로 거리를 어림잡으며 자신 없어함", "A guide eyeballs the distance, unsure of the number"),
         "caption": ("눈으로 보고 어림잡으면 자꾸 틀려요.", "Eyeballing it keeps being wrong."),
         "small": ("눈대중은 사람마다 다르고, 어두우면 더 어려워요.", "Eyeballing it differs person to person — and it's worse in the dark.")},
        {"svg": P3, "hero": True, "alt": ("회전하는 레이저 장치가 부스를 향해 레이저를 쏘고, 시연 담당자가 지켜봄", "A spinning laser device fires beams at a booth while a demo staffer watches"),
         "caption": ("LiDAR는 레이저를 쏘고 돌아오는 시간을 재서 거리를 정확히 아는 눈이에요.", "LiDAR is an eye that times a laser's round trip to know distance exactly."),
         "small": ("빛의 속도는 늘 똑같으니, 시간만 재면 거리가 나와요.", "Light always travels at the same speed, so timing it gives the distance."),
         "tricks": (4, [
             (SPIN_I, ("레이저 쏘기", "Fire the laser"), ("사방으로 빠르게 쏴요", "fired rapidly in every direction")),
             (DOT_I, ("되돌아오는 시간 재기", "Time the return"), ("벽에 맞고 돌아와요", "bounces back off a wall"), "calm"),
             (CLOUD3D_I, ("점 쌓기", "Stack up points"), ("거리 점이 수백만 개 쌓여요", "millions of distance points pile up")),
             (RULER_I, ("3D 지도 만들기", "Build a 3D map"), ("점들이 모여 모양이 돼요", "the points together form a shape"), "warm"),
         ])},
        {"svg": P4, "alt": ("작동 순서 설명판: 쏘기→재기→쌓기→지도 만들기. 안내원이 포인트 클라우드를 설명", "A board shows fire, time, stack, map; a guide explains the point cloud"),
         "caption": ("레이저 점들이 모여 3D 지도가 돼요.", "The laser points together form a 3D map."),
         "small": ("이 점들의 모임을 '포인트 클라우드'라고 불러요.", "This cluster of points is called a point cloud.")},
        {"svg": P5, "alt": ("왼쪽: 맑은 날 정확한 3D 점구름. 오른쪽: 비 오는 날 레이저가 흩어짐", "Left: a crisp 3D point cloud on a clear day. Right: the laser scattering in the rain"),
         "caption": ("비나 안개엔 약하고, 가격도 비싸요.", "It's weak in rain or fog, and the gear is pricey."),
         "small": ("정확한 눈이지만, 날씨와 가격이라는 벽은 남아 있어요.", "A precise eye, but weather and cost remain real walls.")},
    ],
    "summary": (("<b>LiDAR</b> = 레이저를 쏘고 돌아오는 <b>시간을 재서</b>, 사방의 <b>정확한 거리</b>를 포인트 클라우드로 그려내는 센서.",
                 "<b>LiDAR</b> = a sensor that times a laser's return trip to draw out the <b>exact distance</b> in every direction, as a point cloud."),
                ("LiDAR(Light Detection and Ranging)는 레이저 펄스를 쏘고 반사되어 돌아오는 시간을 측정해 주변 물체까지의 거리를 정밀하게 계산하는 센서예요. 수많은 거리 점(포인트 클라우드)을 모아 3차원 지도를 만들며, 자율주행차·로봇·측량 등에 널리 쓰여요. 단, 비·안개·눈 같은 악천후에는 성능이 떨어지고 비용도 높아요.",
                 "LiDAR (Light Detection and Ranging) is a sensor that fires laser pulses and measures the time it takes for them to bounce back, precisely calculating distance to surrounding objects. It gathers huge numbers of distance points — a point cloud — into a 3D map, widely used in self-driving cars, robotics, and surveying. Its performance drops in rain, fog, or snow, and it remains costly.")),
    "glossary": [
        ("포인트 클라우드", "Point Cloud", ("거리 점들이 모인 구름.", "A cloud made of distance points."), ("점이 많이 모일수록 지도가 선명해져요.", "The more points gathered, the sharper the map.")),
        ("ToF(비행시간)", "Time of Flight", ("빛이 갔다 오는 시간을 재는 원리.", "The principle of timing light's round trip."), ("LiDAR가 거리를 재는 바로 그 방법이에요.", "The very method LiDAR uses to measure distance.")),
        ("3D 스캐닝", "3D Scanning", ("실제 공간을 입체로 옮기는 것.", "Transferring real space into 3D form."), ("LiDAR는 이 스캐닝의 한 방법이에요.", "LiDAR is one way of doing this kind of scanning.")),
        ("자율주행", "Autonomous Driving", ("LiDAR를 눈으로 쓰는 대표적인 곳.", "A prime place where LiDAR serves as the eyes."), ('이 눈을 가장 많이 쓰는 이웃 부스예요. → <a href="autodrive-ko.html">자율주행</a>', 'The neighboring booth that relies on this eye the most. → <a href="autodrive-en.html">Autonomous Driving</a>')),
        ("디지털 트윈", "Digital Twin", ("실제 공간을 그대로 옮긴 쌍둥이 화면.", "A twin screen that mirrors real space exactly."), ('포인트 클라우드가 이 쌍둥이의 재료가 돼요. → <a href="cps-ko.html">사이버물리시스템(CPS)</a>', "Point clouds become the raw material for that twin. → <a href=\"cps-en.html\">Cyber-Physical Systems</a>")),
        ("드론 보안위협", "Drone Security Threats", ("드론도 LiDAR로 주변을 살펴봐요.", "A drone, too, scans its surroundings with LiDAR."), ('그 드론을 노리는 위협은 다른 페이지에서 다뤄요. → <a href="dronesecurity-ko.html">보이지 않는 줄로 매달린 드론</a>', 'What threatens that drone is covered on another page. → <a href="dronesecurity-en.html">the drone held up by an invisible string</a>')),
        ("레이더/카메라", "Radar/Camera", ("LiDAR의 이웃 센서들.", "LiDAR's sensor cousins."), ("날씨엔 강하지만 정밀도는 서로 달라요.", "Sturdier in bad weather, but each with its own precision trade-off.")),
        ("4차 산업혁명", "4th Industrial Revolution", ("여러 신기술이 모여 만드는 큰 흐름.", "The big wave made when many new technologies combine."), ('이 전시장 전체를 아우르는 이야기예요. → <a href="fourthindustry-ko.html">4차 산업혁명</a>', 'The story that frames this whole exhibit hall. → <a href="fourthindustry-en.html">the 4th Industrial Revolution</a>')),
    ],
}
