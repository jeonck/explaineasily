from _draw import *

RED, AMBER, GREEN, CLEAR = "#D9362B", "#F2A900", "#2E9E5B", "#F4F6F8"

LIGHT = ('<rect x="150" y="270" width="24" height="40" fill="var(--stone-dark)"/>'
         '<rect x="110" y="20" width="104" height="256" rx="20" fill="var(--night)"/>'
         + "".join(f'<circle cx="162" cy="{y}" r="24" fill="{c}" stroke="var(--line)" stroke-width="{2 if c == CLEAR else 0}"/>'
                   for y, c in ((58, RED), (118, AMBER), (178, GREEN), (238, CLEAR)))
         + label(250, 64, "⟦빨강|RED⟧", 18, "var(--ink)", "start") + label(250, 124, "⟦주황|AMBER⟧", 18, "var(--ink)", "start")
         + label(250, 184, "⟦초록|GREEN⟧", 18, "var(--ink)", "start") + label(250, 244, "⟦투명|CLEAR⟧", 18, "var(--ink)", "start"))
ENVELOPE = ('<g transform="translate(470,100)"><rect width="220" height="140" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/>'
            '<path d="M0 10 L110 80 L220 10" stroke="var(--line)" stroke-width="3" fill="none"/>'
            f'<circle cx="190" cy="30" r="20" fill="{RED}"/>' + label(110, 120, "⟦비밀 편지|secret letter⟧", 16, "var(--muted)") + "</g>")
P1 = svg(320, '<rect width="760" height="320" fill="var(--sky)"/>' + LIGHT + ENVELOPE)

RINGS = (f'<circle cx="380" cy="190" r="170" fill="{CLEAR}" stroke="var(--line)" stroke-width="2"/>'
         f'<circle cx="380" cy="190" r="125" fill="{GREEN}" fill-opacity="0.75"/>'
         f'<circle cx="380" cy="190" r="80" fill="{AMBER}" fill-opacity="0.85"/>'
         f'<circle cx="380" cy="190" r="36" fill="{RED}"/>')
TINY = "".join(person(x, y, hat=None, shirt="var(--night)", s=0.35, face=EYES) for x, y in
               ((320, 120), (420, 120), (330, 230), (415, 235),
                (270, 90), (470, 90), (255, 250), (490, 245),
                (200, 150), (540, 150), (560, 280), (180, 280)))
P2 = svg(380, '<rect width="760" height="380" fill="var(--panel)"/>' + RINGS + TINY
         + person(360, 150, hat="var(--good)", shirt="var(--good)", s=0.6, face=SMILE)
         + label(380, 30, "⟦아무나|anyone⟧", 15, "var(--muted)") + label(380, 76, "⟦우리 마을|our village⟧", 15, "#FFF")
         + label(380, 120, "⟦우리 성|our castle⟧", 15, "var(--night)"))

WHISPER = '<path d="M60 40 q10 -6 20 0" stroke="var(--night)" stroke-width="3" fill="none" stroke-linecap="round"/>'
P3 = svg(240, sky(240)
         + person(220, 70, hat="var(--good)", shirt="var(--good)", face=SMILE)
         + person(360, 70, hat="var(--accent)", shirt="#4A5A72", face=SMILE)
         + f'<g transform="translate(300,80)"><rect x="-30" y="-16" width="60" height="40" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="18" cy="-8" r="8" fill="{RED}"/></g>'
         + label(300, 50, "⟦쉿|shh⟧", 22, "var(--muted)", cls="d")
         + '<g transform="translate(560,110)"><rect x="-28" y="-6" width="56" height="44" rx="8" fill="var(--night)"/><path d="M-18 -6 V-20 a18 18 0 0 1 36 0 V-6" stroke="var(--night)" stroke-width="8" fill="none"/><circle cy="14" r="6" fill="var(--accent)"/></g>'
         + label(560, 190, "⟦약속|a promise⟧", 16, "var(--muted)"))

PAGE = {
    "slug": "tlp", "order": 6,
    "title": ("비밀 신호등", "The Secret Traffic Light"),
    "h1": ("<em>TLP</em>가 뭐예요?", "What is <em>TLP</em>?"),
    "sub": ("공유 신호등(Traffic Light Protocol)을 비밀 편지 이야기로 풀어봤어요.",
            "The Traffic Light Protocol, told as a story about secret letters."),
    "panels": [
        {"svg": P1, "alt": ("빨강, 주황, 초록, 투명 네 개의 등이 달린 신호등과 빨간 스티커가 붙은 편지", "A traffic light with red, amber, green and clear lamps, and a letter with a red sticker"),
         "caption": ("비밀 편지에 색깔 스티커를 붙여요.", "Every secret letter gets a colored sticker."),
         "small": ("'이거 어디까지 말해도 돼?'의 답이에요.", "It answers: \"how far can I pass this on?\"")},
        {"svg": P2, "hero": True, "alt": ("가운데 나, 바깥으로 우리 성, 우리 마을, 아무나로 넓어지는 원", "Rings widening from me, to our castle, to our village, to anyone"),
         "caption": ("색깔마다 말해도 되는 범위가 달라요.", "Each color is a bigger circle."),
         "small": ("빨강은 나 혼자. 투명은 온 세상.", "Red is just me. Clear is the whole world."),
         "tricks": (4, [
             (dot_icon(RED), ("빨강", "RED"), ("받은 사람만", "only who got it")),
             (dot_icon(AMBER), ("주황", "AMBER"), ("우리 성 안", "inside our castle"), "warm"),
             (dot_icon(GREEN), ("초록", "GREEN"), ("우리 마을", "our village"), "calm"),
             (dot_icon(CLEAR), ("투명", "CLEAR"), ("아무나", "anyone"), "calm"),
         ])},
        {"svg": P3, "alt": ("귓속말하는 두 친구와 자물쇠", "Two friends whispering, and a padlock"),
         "caption": ("약속을 지켜야 다음 비밀도 들어요.", "Keep the promise, and you'll hear the next secret."),
         "small": ("퍼뜨리면 친구는 다시 말 안 해줘요.", "Spread it, and your friend stops telling you things.")},
    ],
    "summary": (("<b>TLP</b> = \"이 비밀 <b>어디까지</b> 말해도 돼?\"를 색으로 정한 약속.",
                 "<b>TLP</b> = a color that says <b>how far</b> a secret may travel."),
                ("Traffic Light Protocol. 지금 쓰는 건 2022년의 2.0판이에요. WHITE가 CLEAR로 바뀌었고, AMBER+STRICT가 새로 생겼어요.",
                 "Traffic Light Protocol. The current version is 2.0 (2022): WHITE became CLEAR, and AMBER+STRICT was added.")),
    "glossary": [
        ("TLP:RED", "TLP:RED", ("받은 사람만.", "Recipients only."), ("회의에서 들었으면 그 방 사람들만.", "Heard it in a meeting? Stays in that room.")),
        ("TLP:AMBER", "TLP:AMBER", ("우리 조직 안.", "Inside our organization."), ("알아야 하는 동료와 고객까지.", "Colleagues and clients who need it.")),
        ("TLP:AMBER+STRICT", "TLP:AMBER+STRICT", ("우리 조직만.", "Our organization only."), ("고객에게도 안 돼요.", "Not even clients.")),
        ("TLP:GREEN", "TLP:GREEN", ("우리 동네.", "Our community."), ("같은 업계 친구들까지. 인터넷엔 안 돼요.", "Peers in the same field. Never the open internet.")),
        ("TLP:CLEAR", "TLP:CLEAR", ("아무나.", "Anyone."), ("공개해도 돼요. 예전 이름은 WHITE.", "Free to publish. Used to be called WHITE.")),
        ("FIRST", "FIRST", ("약속을 정한 곳.", "Who wrote the rules."), ("전 세계 보안 대응팀 모임. TLP 2.0을 냈어요.", "A global forum of security response teams. Published TLP 2.0.")),
    ],
}
