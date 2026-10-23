from _draw import *
from _world import *


def avatar(x, y, s=1.0, color="var(--accent)"):
    return (f'<g transform="translate({x},{y}) scale({s})"><circle cy="0" r="18" fill="{color}" opacity="0.85"/>'
            f'<circle cx="-6" cy="-4" r="3" fill="#fff"/><circle cx="6" cy="-4" r="3" fill="#fff"/>'
            f'<rect x="-14" y="18" width="28" height="36" rx="10" fill="{color}"/></g>')


def flatscreen(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="140" height="90" rx="4" fill="#1B2A44"/>'
            f'<rect x="8" y="8" width="124" height="74" rx="2" fill="#0A1120"/>{avatar(70,50,0.8,"#5B8DEF")}</g>')


# 1. 화상회의는 평면이라 같이 있는 느낌이 안 나요
P1 = svg(300, sky(300, ground=False)
         + flatscreen(120, 110, 1.0)
         + person(400, 170, s=0.85, face=FROWN, **VISITOR)
         + bubble(440, 90, 230, 46, "⟦다 같이 모인 건데 왠지 따로 있는 것 같아요|we're all here, but it still feels like we're apart⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦평면 화면엔 '같이 있다'는 느낌이 없어요|a flat screen has no sense of 'being together'⟧", 13, "var(--ink)"))

# 2. 2D 화면은 공간감이 없어요
P2 = svg(320, '<rect width="760" height="320" fill="var(--accent-soft)"/>'
         + flatscreen(190, 100, 1.4) + flatscreen(420, 100, 1.4) + flatscreen(560, 100, 0.8)
         + label(380, 270, "⟦각자 네모 칸 안에만 있어요, 같은 공간이 아니에요|everyone's stuck in their own little box — not a shared space⟧", 12, "var(--ink)")
         + label(380, 300, "⟦그래서 몰입감이 생기지 않아요|so it never quite feels immersive⟧", 11, "var(--muted)"))

# 3. 메타버스 = 아바타로 함께 있는 가상 공간 (hero)
P3 = svg(340, sky(340)
         + avatar(260, 180, 1.4, "var(--accent)") + avatar(400, 190, 1.2, "#5B8DEF") + avatar(500, 175, 1.1, "#C9822B")
         + booth(540, 60, 160, 110, 0.9, "var(--good)", "⟦가상 전시관|virtual pavilion⟧")
         + label(380, 30, "⟦메타버스 = 아바타로 들어가 서로 같은 가상 공간에 함께 있는 인터넷|Metaverse = an internet where avatars share the same virtual space together⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦각자 아바타로 한 공간에 모였어요|everyone's gathered in one space, as avatars⟧", 12, "var(--muted)"))

META_AVATAR = icon('<circle cx="32" cy="22" r="12" fill="var(--accent)"/><rect x="18" y="36" width="28" height="22" rx="8" fill="var(--accent)"/>')
META_SPACE = icon('<rect x="10" y="10" width="44" height="44" rx="4" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 10 L54 54 M54 10 L10 54" stroke="var(--accent)" stroke-width="2" opacity="0.5"/>')
META_LIVE = icon('<circle cx="22" cy="32" r="10" fill="var(--good)"/><circle cx="42" cy="32" r="10" fill="var(--accent)"/><path d="M28 28 q4 6 10 0" stroke="#fff" stroke-width="2" fill="none"/>')
META_ECON = icon('<circle cx="32" cy="32" r="22" fill="var(--accent)"/><text x="32" y="40" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">$</text>')

# 4. 구성요소
P4 = svg(360, sky(360, ground=False)
         + infoboard(130, 30, 500, 290, "⟦메타버스를 이루는 것들|WHAT IT'S MADE OF⟧",
                     ("⟦아바타 — 나를 대신하는 모습|avatar — a stand-in for me⟧",
                      "⟦가상 공간 — 함께 머무는 3D 세계|virtual space — a shared 3D world⟧",
                      "⟦실시간 상호작용 — 목소리·동작이 그대로|real-time interaction — voice and motion, live⟧",
                      "⟦가상경제 — 아이템을 사고팔기|virtual economy — buying and selling items⟧"), 1.3)
         + label(380, 345, "⟦이 네 가지가 모여야 '같이 있다'는 느낌이 나요|all four together make it feel like 'being there'⟧", 12, "var(--ink)"))

# 5. 한계: 멀미, 비싼 기기, 서로 호환 안 됨
P5 = svg(330, '<rect width="380" height="330" fill="var(--bad-soft)"/><rect x="380" width="380" height="330" fill="var(--accent-soft)"/>'
         + person(190, 125, s=0.85, face=SWEAT + EYES, **VISITOR)
         + label(190, 260, "⟦오래 쓰면 어지럽고, 기기도 비싸요|wear it too long and it's dizzying, and the gear is pricey⟧", 11, "var(--ink)")
         + avatar(540, 150, 1.3, "var(--accent)") + label(650, 150, "✕", 28, "var(--bad)", cls="d") + avatar(700, 150, 1.0, "#C9822B")
         + label(620, 260, "⟦서로 다른 메타버스끼리는 아직 호환이 안 돼요|different metaverses still don't talk to each other⟧", 11, "var(--ink)")
         + label(380, 305, "⟦기기 자체는 다음 부스, VR에서 자세히 봐요|the headset itself gets its own booth next: VR⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "metaverse", "order": 7,
    "title": ("아바타들이 모인 가상 전시관", "The Virtual Pavilion Full of Avatars"),
    "h1": ("<em>메타버스</em>가 뭐예요?", "What is the <em>Metaverse</em>?"),
    "sub": ("메타버스를, 평면 화상회의 대신 아바타로 들어가 함께 머무는 가상 전시관 이야기로 풀어봤어요.",
            "Metaverse, told as a story about a virtual pavilion where avatars gather together, instead of a flat video call."),
    "panels": [
        {"svg": P1, "alt": ("평면 화상회의 화면을 보며 관람객이 같이 있는 느낌이 안 난다고 말함", "A visitor looks at a flat video-call screen and says it doesn't feel like being together"),
         "caption": ("다 같이 모인 건데 왠지 따로 있는 것 같아요.", "We're all here, but it still feels like we're apart."),
         "small": ("평면 화면엔 '같이 있다'는 느낌이 없어요.", "A flat screen has no sense of 'being together.'")},
        {"svg": P2, "alt": ("세 개의 화상회의 화면이 각각 따로 떨어져 있음", "Three video-call screens, each its own separate box"),
         "caption": ("각자 네모 칸 안에만 있어요, 같은 공간이 아니에요.", "Everyone's stuck in their own little box — not a shared space."),
         "small": ("그래서 몰입감이 생기지 않아요.", "So it never quite feels immersive.")},
        {"svg": P3, "hero": True, "alt": ("세 아바타가 가상 전시관이라는 같은 공간에 함께 모여 있음", "Three avatars gathered together in the same virtual pavilion"),
         "caption": ("메타버스는 아바타로 들어가 서로 같은 가상 공간에 함께 있는 인터넷이에요.", "Metaverse is an internet where avatars share the same virtual space together."),
         "small": ("각자 아바타로 한 공간에 모였어요.", "Everyone's gathered in one space, as avatars."),
         "tricks": (4, [
             (META_AVATAR, ("아바타로 나를 표현", "Represent myself as an avatar"), ("진짜 나 대신이에요", "a stand-in for the real me"), "calm"),
             (META_SPACE, ("3D 공간 공유", "Share a 3D space"), ("같은 곳에 함께 있어요", "together in the same place")),
             (META_LIVE, ("실시간 상호작용", "Interact in real time"), ("목소리·동작도 그대로", "voice and motion, live")),
             (META_ECON, ("가상경제 참여", "Join a virtual economy"), ("아이템을 사고팔아요", "buy and sell items"), "warm"),
         ])},
        {"svg": P4, "alt": ("메타버스를 이루는 네 요소: 아바타, 가상공간, 실시간 상호작용, 가상경제", "A board showing four parts of the metaverse: avatar, virtual space, real-time interaction, virtual economy"),
         "caption": ("이 네 가지가 모여야 '같이 있다'는 느낌이 나요.", "All four together make it feel like 'being there.'"),
         "small": ("하나라도 빠지면 그냥 또 다른 화면일 뿐이에요.", "Missing even one, and it's just another screen.")},
        {"svg": P5, "alt": ("왼쪽: 관람객이 멀미와 비싼 기기를 호소함. 오른쪽: 서로 다른 메타버스 아바타가 호환되지 않음", "Left: a visitor complains of dizziness and pricey gear. Right: avatars from different metaverses can't connect"),
         "caption": ("오래 쓰면 어지럽고, 기기도 비싸요.", "Wear it too long and it's dizzying, and the gear is pricey."),
         "small": ("서로 다른 메타버스끼리는 아직 호환이 안 돼요.", "Different metaverses still don't talk to each other.")},
    ],
    "summary": (("<b>메타버스</b>는 아바타로 들어가 <b>같은 가상 공간에 함께 있는 느낌</b>을 주는 인터넷으로, 가상공간·실시간 상호작용·가상경제가 함께 있어야 완성돼요.",
                 "The <b>metaverse</b> is an internet that gives you the <b>feeling of being together in the same virtual space</b>, as an avatar — complete only with a shared space, real-time interaction, and a virtual economy together."),
                ("메타버스는 아바타를 통해 사용자가 몰입형 3D 가상 공간에서 실시간으로 상호작용하고, 가상 재화를 거래할 수 있는 확장된 인터넷 환경이에요. VR·AR 기기는 메타버스에 들어가는 한 가지 방법일 뿐이고, 서로 다른 메타버스 플랫폼 간 상호운용성 부족과 장시간 착용의 피로는 아직 풀어야 할 과제예요.",
                 "The metaverse is an extended internet environment where users, through avatars, interact in real time in immersive 3D virtual spaces and trade virtual goods. VR/AR headsets are just one way to enter it, and a lack of interoperability between different metaverse platforms, plus fatigue from extended wear, remain unresolved challenges.")),
    "glossary": [
        ("메타버스", "Metaverse", ("아바타가 함께 머무는 가상 공간.", "The virtual space avatars share together."), ("가상공간·상호작용·경제가 다 있어야 해요.", "Needs space, interaction, and an economy, all together.")),
        ("아바타", "Avatar", ("나를 대신하는 가상 모습.", "A virtual stand-in for me."), ("메타버스 안에서 나를 표현해요.", "Represents me inside the metaverse.")),
        ("가상현실(VR)", "Virtual Reality", ("가상 세계로 들어가는 헤드셋 기술.", "The headset technology for entering a virtual world."), ('메타버스에 들어가는 한 방법이에요. → <a href="vrtech-ko.html">VR 부스</a>', "One way to enter the metaverse. → <a href=\"vrtech-en.html\">the VR booth</a>")),
        ("디지털 트윈", "Digital Twin", ("현실을 그대로 복제하는 쌍둥이.", "A twin that copies reality exactly."), ('트윈은 현실 복제, 메타버스는 새 세계도 만들 수 있어요. → <a href="digitaltwin-ko.html">디지털 트윈 부스</a>', 'A twin copies reality; the metaverse can invent new worlds too. → <a href="digitaltwin-en.html">the Digital Twin booth</a>')),
        ("가상경제", "Virtual Economy", ("가상 세계 안의 아이템 거래.", "Trading items inside the virtual world."), ("실제 돈과 연결되기도 해요.", "Sometimes connects to real money.")),
        ("상호운용성", "Interoperability", ("서로 다른 메타버스끼리 통하는 정도.", "How well different metaverses talk to each other."), ("지금은 아직 낮은 편이에요.", "Still fairly low right now.")),
        ("몰입감", "Immersion", ("정말 거기 있는 것 같은 느낌.", "The feeling of really being there."), ("평면 화면이 못 주는 바로 그것이에요.", "The very thing a flat screen can't give.")),
        ("실감형 콘텐츠", "Immersive Content", ("몰입감을 만드는 영상·공간 콘텐츠.", "Video and spatial content built to create immersion."), ("메타버스·VR 둘 다에서 쓰여요.", "Used in both metaverse and VR.")),
    ],
}
