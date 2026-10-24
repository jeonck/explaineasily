from _draw import *
from _world import *


def headset(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-24" y="-16" width="48" height="32" rx="12" fill="#2E3D57"/>'
            f'<rect x="-30" y="-6" width="10" height="20" rx="4" fill="#1B2A44"/><rect x="20" y="-6" width="10" height="20" rx="4" fill="#1B2A44"/></g>')


def personvr(x, y, s=1.0, face=""):
    return (f'<g transform="translate({x},{y}) scale({s})">{person(0, 0, s=1.0, face=face, **VISITOR)}'
            f'{headset(30, 30)}</g>')


def photo(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="100" height="70" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M10 50 l24 -24 l18 16 l20 -26 l18 34z" fill="#8FA6C7"/></g>'


def flatscreen(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect width="140" height="90" rx="4" fill="#1B2A44"/><rect x="8" y="8" width="124" height="74" rx="2" fill="#0A1120"/></g>'


# 1. 사진으로는 높은 곳 공포를 못 느껴요
P1 = svg(300, sky(300, ground=False)
         + photo(160, 100, 1.4)
         + person(480, 170, s=0.85, face=EYES, **DEMO)
         + bubble(540, 90, 200, 46, "⟦사진만 봐서는 하나도 안 무서운데요?|just looking at a photo, it's not scary at all?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦평면 사진으로는 '거기 있다'는 느낌이 안 나요|a flat photo gives no sense of actually being there⟧", 13, "var(--ink)"))

# 2. 평면 화면은 몰입감을 못 줘요
P2 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + flatscreen(300, 80, 1.6)
         + label(380, 280, "⟦훈련·교육용으로 쓰려 해도, 화면 밖은 그냥 교실이에요|try to use it for training, but outside the screen it's still just a classroom⟧", 12, "var(--ink)"))


# 3. VR = 눈앞 전체가 가상 세계로 바뀜 (hero)
P3 = svg(340, '<rect width="760" height="340" fill="var(--night)"/>'
         + personvr(220, 120, 1.1, face=EYES)
         + label(220, 270, "⟦헤드셋을 쓴 관람객|a visitor wearing the headset⟧", 11, "#C9D5E6")
         + screen(480, 90, 1.8, '<path d="M10 40 l20 -22 l16 14 l16 -24 l18 32z" fill="#8FA6C7"/>')
         + label(380, 30, "⟦VR = 눈앞 전체가 가상 세계로 바뀌어, 그 안에 있는 것처럼 느끼게 하는 기술|VR = your whole field of view becomes a virtual world, making you feel like you're inside it⟧", 13, "#F5E6B8", cls="d")
         + label(380, 320, "⟦고개를 돌리면 가상 세계도 같이 돌아가요|turn your head, and the virtual world turns with you⟧", 12, "#C9D5E6"))

VR_COVER = icon('<rect x="8" y="20" width="48" height="24" rx="12" fill="var(--accent)"/><rect x="2" y="26" width="8" height="12" rx="3" fill="#2E3D57"/><rect x="54" y="26" width="8" height="12" rx="3" fill="#2E3D57"/>')
VR_TRACK = icon('<circle cx="32" cy="32" r="20" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M32 12 v10 M32 42 v10 M12 32 h10 M42 32 h10" stroke="var(--accent)" stroke-width="3"/>')
VR_CONTROL = icon('<rect x="12" y="24" width="18" height="28" rx="8" fill="var(--accent)"/><rect x="34" y="24" width="18" height="28" rx="8" fill="var(--accent)"/><circle cx="21" cy="30" r="4" fill="#fff"/><circle cx="43" cy="30" r="4" fill="#fff"/>')
VR_HAPTIC = icon('<path d="M20 44 q-8 -14 0 -26 M44 44 q8 -14 0 -26" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="32" cy="32" r="6" fill="var(--accent)"/>')

# 4. VR vs AR vs MR 비교
P4 = svg(360, sky(360, ground=False)
         + infoboard(50, 30, 220, 290, "⟦VR|VIRTUAL⟧", ("⟦완전 가상 세계|fully virtual⟧", "⟦현실은 안 보여요|real world hidden⟧"), 1.0)
         + infoboard(290, 30, 220, 290, "⟦AR|AUGMENTED⟧", ("⟦현실 + 가상 겹침|real world + overlay⟧", "⟦현실이 그대로 보여요|real world stays visible⟧"), 1.0)
         + infoboard(530, 30, 220, 290, "⟦MR|MIXED⟧", ("⟦현실·가상이 서로 반응|real and virtual react to each other⟧", "⟦가상 물체를 만지듯|virtual objects feel touchable⟧"), 1.0)
         + label(380, 345, "⟦가상을 얼마나 많이 보여주느냐가 다를 뿐이에요|they differ in how much virtual content they show⟧", 12, "var(--ink)"))

# 5. 한계: 멀미, 피로, 비싼 장비
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + personvr(190, 150, 1.0, face=SWEAT + EYES)
         + label(190, 240, "⟦지연이 생기면 멀미가 나요|a delay in response causes dizziness⟧", 11, "var(--ink)")
         + headset(570, 150, 1.5)
         + label(570, 240, "⟦장시간 착용 피로, 비싼 장비도 걸림돌이에요|long wear tires you out, and the gear is pricey too⟧", 11, "var(--ink)")
         + label(380, 282, "⟦VR은 메타버스를 체험하는 한 가지 방법일 뿐이에요|VR is just one way to experience the metaverse⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "vrtech", "order": 8,
    "title": ("눈앞 전체를 바꾸는 헤드셋", "The Headset That Replaces Your Whole View"),
    "h1": ("<em>가상현실(VR)</em>이 뭐예요?", "What is <em>Virtual Reality (VR)</em>?"),
    "sub": ("가상현실을, 헤드셋을 쓰면 눈앞 전체가 가상 세계로 바뀌는 체험 부스 이야기로 풀어봤어요.",
            "Virtual reality, told as a story about a booth where putting on a headset replaces your whole field of view with a virtual world."),
    "panels": [
        {"svg": P1, "alt": ("시연 담당자가 높은 곳 사진을 보며 하나도 안 무섭다고 말함", "A demonstrator looks at a photo of a high place and says it's not scary at all"),
         "caption": ("사진만 봐서는 하나도 안 무서운데요?", "Just looking at a photo, it's not scary at all?"),
         "small": ("평면 사진으로는 '거기 있다'는 느낌이 안 나요.", "A flat photo gives no sense of actually being there.")},
        {"svg": P2, "alt": ("커다란 평면 화면 한 대가 놓여 있지만 몰입감을 주지 못함", "A big flat screen sits there but fails to give any sense of immersion"),
         "caption": ("훈련·교육용으로 쓰려 해도, 화면 밖은 그냥 교실이에요.", "Try to use it for training, but outside the screen it's still just a classroom."),
         "small": ("평면 화면은 몰입감을 못 줘요.", "A flat screen can't give that sense of immersion.")},
        {"svg": P3, "hero": True, "alt": ("헤드셋을 쓴 관람객 앞에 가상의 높은 산 풍경이 펼쳐짐", "A visitor wearing a headset, a virtual mountain view unfolding before them"),
         "caption": ("VR은 눈앞 전체가 가상 세계로 바뀌어, 그 안에 있는 것처럼 느끼게 하는 기술이에요.", "VR makes your whole field of view become a virtual world, so you feel like you're inside it."),
         "small": ("고개를 돌리면 가상 세계도 같이 돌아가요.", "Turn your head, and the virtual world turns with you."),
         "tricks": (4, [
             (VR_COVER, ("시야 전체 덮기", "Cover the whole view"), ("헤드셋으로 눈앞을 가려요", "the headset blocks everything else"), "calm"),
             (VR_TRACK, ("머리 움직임 추적", "Track head movement"), ("고개 따라 화면이 바뀌어요", "the view follows your head")),
             (VR_CONTROL, ("컨트롤러로 조작", "Handle with controllers"), ("가상 물체를 직접 만져요", "reach out and touch virtual objects")),
             (VR_HAPTIC, ("햅틱으로 촉감 흉내", "Fake touch with haptics"), ("진동으로 느낌을 줘요", "a buzz stands in for touch"), "warm"),
         ])},
        {"svg": P4, "alt": ("VR·AR·MR을 가상 비율로 비교하는 세 개의 설명판", "Three boards comparing VR, AR, and MR by how much virtual content they show"),
         "caption": ("VR·AR·MR은 가상을 얼마나 많이 보여주느냐가 달라요.", "VR, AR, and MR differ in how much virtual content they show."),
         "small": ("VR은 완전 가상, AR은 현실 위에 겹침, MR은 서로 반응해요.", "VR is fully virtual, AR overlays onto reality, and MR lets the two react to each other.")},
        {"svg": P5, "alt": ("왼쪽: 관람객이 멀미를 느낌. 오른쪽: 커다란 헤드셋과 피로·비용 문제", "Left: a visitor feels dizzy. Right: a bulky headset with fatigue and cost problems"),
         "caption": ("지연이 생기면 멀미가 나고, 장시간 착용은 피곤해요.", "A delay causes dizziness, and long wear tires you out."),
         "small": ("VR은 메타버스를 체험하는 한 가지 방법일 뿐이에요.", "VR is just one way to experience the metaverse.")},
    ],
    "summary": (("<b>가상현실(VR)</b>은 헤드셋으로 눈앞 전체를 가상 세계로 바꿔, <b>그 안에 있는 것처럼 느끼게</b> 하는 기술이에요.",
                 "<b>Virtual reality (VR)</b> uses a headset to replace your whole field of view with a virtual world, making you <b>feel like you're inside it</b>."),
                ("VR은 머리 장착형 디스플레이(HMD)로 사용자의 시야를 완전히 가상 콘텐츠로 대체하고, 머리·손 움직임을 추적해 실시간으로 반응시키는 기술이에요. 현실을 그대로 보여주며 가상 정보를 겹치는 AR, 현실과 가상이 서로 반응하는 MR과 구분돼요. 지연시간이 생기면 멀미(사이버 멀미)가 나타날 수 있고, 장시간 착용 피로와 장비 비용은 대중화의 걸림돌이에요.",
                 "VR uses a head-mounted display (HMD) to fully replace the user's view with virtual content, tracking head and hand movement to react in real time. It's distinct from AR, which overlays virtual information on an unobstructed view of reality, and MR, where reality and virtual content react to each other. Latency can trigger motion sickness ('cybersickness'), and extended-wear fatigue plus equipment cost remain barriers to wider adoption.")),
    "glossary": [
        ("가상현실(VR)", "Virtual Reality", ("눈앞 전체를 가상으로 바꾸는 헤드셋.", "A headset that replaces your whole view with virtual content."), ("시야 전체를 가상 세계로 덮어요.", "Covers your entire field of view.")),
        ("증강현실(AR)", "Augmented Reality", ("현실 위에 가상 정보를 겹치는 것.", "Overlaying virtual info onto reality."), ("현실은 그대로 보여요.", "Reality stays fully visible.")),
        ("혼합현실(MR)", "Mixed Reality", ("현실과 가상이 서로 반응하는 것.", "Reality and virtual content reacting to each other."), ("가상 물체를 만지듯 다룰 수 있어요.", "Lets you handle virtual objects as if touching them.")),
        ("메타버스", "Metaverse", ("아바타로 함께 머무는 가상 공간.", "The shared virtual space avatars gather in."), ('VR은 메타버스를 체험하는 한 방법이에요. → <a href="metaverse-ko.html">메타버스 부스</a>', "VR is one way to experience it. → <a href=\"metaverse-en.html\">the Metaverse booth</a>")),
        ("HMD(머리 장착형 디스플레이)", "HMD", ("눈앞을 완전히 가리는 헤드셋.", "The headset that fully covers your view."), ("VR 체험의 핵심 장비예요.", "The core piece of VR hardware.")),
        ("사이버 멀미", "Cybersickness / VR Sickness", ("지연 때문에 생기는 어지럼증.", "Dizziness caused by response delay."), ("추적·반응이 느릴수록 심해져요.", "Worse the slower the tracking and response.")),
        ("헤드 트래킹", "Head Tracking", ("고개 방향을 읽어 화면을 바꾸는 기술.", "Reading head direction to change the view."), ("몰입감을 만드는 핵심 기술이에요.", "The key technology behind immersion.")),
        ("디지털 트윈", "Digital Twin", ("현실 기계를 그대로 복제한 쌍둥이.", "A twin that copies a real machine exactly."), ('VR로 트윈 안을 직접 둘러볼 수도 있어요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', "VR can even let you walk around inside a twin. → <a href=\"digitaltwin-en.html\">the Digital Twin booth</a>")),
    ],
}
