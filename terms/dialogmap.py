from _draw import *


def box(x, y, text, w=150, h=56, fill="var(--panel)", stroke="var(--ink)"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
            + label(x + w / 2, y + h / 2 + 7, text, 18, "var(--ink)", cls="d"))


def arrow(x1, y1, x2, y2, text="", color="var(--accent)", dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 14 * math.cos(ang), y2 - 14 * math.sin(ang)
    px, py = 7 * math.sin(ang), -7 * math.cos(ang)
    head = f'<path d="M{x2} {y2} L{hx + px:.0f} {hy + py:.0f} L{hx - px:.0f} {hy - py:.0f} Z" fill="{color}"/>'
    lab = label((x1 + x2) / 2, (y1 + y2) / 2 - 8, text, 13, "var(--muted)") if text else ""
    return f'<path d="M{x1} {y1} L{hx:.0f} {hy:.0f}" stroke="{color}" stroke-width="3"{d}/>{head}{lab}'


VISITOR = dict(hat=None, shirt="#4A5A72", face=SMILE)

# 1. 앱은 방이 많은 집
HOUSE = ('<path d="M100 110 L380 30 L660 110 Z" fill="var(--stone-dark)"/>'
         '<rect x="120" y="110" width="520" height="180" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="6"/>'
         '<path d="M380 110 V290 M120 200 H640" stroke="var(--stone-dark)" stroke-width="6"/>'
         + label(250, 165, "⟦현관|Home⟧", 20, cls="d") + label(510, 165, "⟦상품|Product⟧", 20, cls="d")
         + label(250, 255, "⟦장바구니|Cart⟧", 20, cls="d") + label(510, 255, "⟦계산대|Checkout⟧", 20, cls="d")
         + '<rect x="170" y="230" width="34" height="60" rx="3" fill="#8B5E3C"/>')
P1 = svg(320, sky(320) + HOUSE + person(40, 170, s=0.8, **VISITOR)
         + "".join(f'<g transform="translate({x},{y})"><rect x="-14" y="-10" width="28" height="18" rx="2" fill="var(--sky)" stroke="var(--stone-dark)" stroke-width="2"/></g>'
                   for x, y in ((320, 135), (580, 135), (320, 222), (580, 222))))

# 2. 문을 안 그려두면 길을 잃는다
P2 = svg(260, '<rect width="760" height="260" fill="var(--accent-soft)"/>'
         '<rect x="230" y="40" width="300" height="190" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="10"/>'
         + label(380, 80, "⟦계산대|Checkout⟧", 20, "var(--muted)", cls="d")
         + person(350, 100, s=0.9, hat=None, shirt="#4A5A72", face=FROWN + SWEAT)
         + label(440, 130, "?", 44, "var(--accent)", cls="d")
         + label(380, 250, "⟦나가는 문이 없어요|no way out⟧", 15, "var(--muted)"))

# 3. 다이얼로그 맵 = 방과 문의 지도 (hero)
MAP = (box(40, 60, "⟦현관|Home⟧") + box(300, 60, "⟦상품|Product⟧") + box(560, 60, "⟦장바구니|Cart⟧")
       + box(560, 220, "⟦계산대|Checkout⟧") + box(300, 220, "⟦완료|Done⟧")
       + arrow(190, 80, 300, 80, "⟦상품 누름|tap item⟧") + arrow(300, 100, 190, 100, "⟦뒤로|back⟧")
       + arrow(450, 80, 560, 80, "⟦담기|add⟧") + arrow(560, 100, 450, 100, "⟦더 보기|keep shopping⟧")
       + arrow(635, 116, 635, 220, "⟦결제|pay⟧") + arrow(560, 248, 450, 248, "⟦확인|OK⟧")
       + arrow(375, 220, 115, 116, "⟦처음으로|home⟧"))
P3 = svg(320, '<rect width="760" height="320" fill="var(--panel)"/>' + MAP)

# 4. 레시피가 아니라 지도
RECIPE = ('<rect x="60" y="30" width="260" height="200" rx="6" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>'
          + "".join(f'<circle cx="90" cy="{y}" r="11" fill="var(--stone-dark)"/>' + label(90, y + 5, str(i + 1), 13, "#FFF")
                    + f'<rect x="112" y="{y - 5}" width="{w}" height="10" rx="5" fill="var(--line)"/>'
                    for i, (y, w) in enumerate(((70, 150), (110, 120), (190, 140))))
          + '<path d="M90 135 L112 150 L90 165 L68 150 Z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>'
          + label(200, 155, "⟦맞나요?|yes / no?⟧", 13, "var(--muted)")
          + label(190, 262, "⟦순서도: 다음에 뭘 하나|flowchart: what do I do next⟧", 15, "var(--muted)"))
MINIMAP = (box(430, 50, "⟦현관|Home⟧", 110, 44) + box(600, 50, "⟦상품|Product⟧", 110, 44) + box(600, 170, "⟦장바구니|Cart⟧", 110, 44) + box(430, 170, "⟦계산대|Checkout⟧", 110, 44)
           + arrow(540, 66, 600, 66) + arrow(600, 80, 540, 80) + arrow(655, 94, 655, 170) + arrow(600, 192, 540, 192) + arrow(485, 170, 485, 94)
           + label(570, 262, "⟦지도: 어디로 갈 수 있나|map: where can I get to⟧", 15, "var(--muted)"))
P4 = svg(280, '<rect width="380" height="280" fill="var(--good-soft)"/><rect x="380" width="380" height="280" fill="var(--sky)"/>' + RECIPE + MINIMAP)

# 5. 그려보면 빠진 문이 보인다
GAP = (box(300, 60, "⟦장바구니|Cart⟧") + box(300, 220, "⟦계산대|Checkout⟧")
       + arrow(375, 116, 375, 220, "⟦결제|pay⟧")
       + arrow(450, 248, 560, 248, "", "var(--bad)", "8 8") + label(505, 232, "⟦취소?|cancel?⟧", 15, "var(--bad)")
       + '<path d="M540 226 L580 270 M580 226 L540 270" stroke="var(--bad)" stroke-width="5" stroke-linecap="round"/>'
       + '<g transform="translate(90,150) rotate(-40)"><rect x="-8" y="-50" width="16" height="90" rx="3" fill="#E9B44C"/><path d="M-8 40 L0 58 L8 40 Z" fill="#E8C9A8"/><rect x="-8" y="-50" width="16" height="12" fill="var(--bad)"/></g>'
       + label(100, 240, "⟦종이 위에서 고쳐요|fix it on paper⟧", 15, "var(--muted)"))
P5 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>' + GAP)

BOX_I = icon('<rect x="8" y="16" width="48" height="32" rx="5" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/><rect x="16" y="24" width="20" height="4" fill="var(--line)"/><rect x="16" y="32" width="28" height="4" fill="var(--line)"/>')
ARROW_I = icon('<path d="M8 32 H44" stroke="var(--accent)" stroke-width="4"/><path d="M40 20 L56 32 L40 44 Z" fill="var(--accent)"/>')

PAGE = {
    "slug": "dialogmap", "order": 11,
    "title": ("방과 문의 지도", "The Room Map"),
    "h1": ("<em>다이얼로그 맵</em>이 뭐예요?", "What is a <em>Dialog Map</em>?"),
    "sub": ("앱 화면 사이를 어떻게 오가는지 그리는 다이얼로그 맵(Dialog Map)을, 방과 문이 있는 집 이야기로 풀어봤어요.",
            "A dialog map draws how you move between an app's screens. Here it's a house with rooms and doors."),
    "panels": [
        {"svg": P1, "alt": ("현관, 상품, 장바구니, 계산대 네 방이 있는 집과 앞에 선 방문객", "A house with four rooms — Home, Product, Cart, Checkout — and a visitor outside"),
         "caption": ("앱은 방이 많은 집이에요.", "An app is a house with many rooms."),
         "small": ("화면 하나가 방 하나예요.", "Every screen is a room.")},
        {"svg": P2, "alt": ("문이 없는 계산대 방 안에서 당황한 방문객", "A visitor stuck in a Checkout room that has no door"),
         "caption": ("문을 안 그려두면 길을 잃어요.", "Forget to draw the doors and people get lost."),
         "small": ("들어갔는데 나가는 문이 없는 방이 생겨요.", "You end up with rooms you can enter but never leave.")},
        {"svg": P3, "hero": True, "alt": ("현관, 상품, 장바구니, 계산대, 완료 상자가 '누름', '담기', '결제', '뒤로' 같은 화살표로 이어진 지도", "Boxes for Home, Product, Cart, Checkout and Done joined by arrows labeled tap, add, pay, back"),
         "caption": ("다이얼로그 맵은 방과 문을 그린 지도예요.", "A dialog map is a map of the rooms and doors."),
         "small": ("상자는 방, 화살표는 문. 누르면 어디로 가는지.", "Boxes are rooms, arrows are doors: press this, land there."),
         "tricks": (2, [
             (BOX_I, ("상자 = 방", "Box = room"), ("화면, 메뉴, 팝업", "a screen, a menu, a pop-up"), "calm"),
             (ARROW_I, ("화살표 = 문", "Arrow = door"), ("버튼을 누르거나, 시간이 다 되거나", "a button press, or a timer running out"), "warm"),
         ])},
        {"svg": P4, "alt": ("왼쪽은 번호가 붙은 레시피와 마름모, 오른쪽은 상자와 화살표 지도", "Left: a numbered recipe with a decision diamond; right: a box-and-arrow map"),
         "caption": ("레시피가 아니라 지도예요.", "It's a map, not a recipe."),
         "small": ("순서도는 '다음에 뭘 하나', 다이얼로그 맵은 '어디로 갈 수 있나'.", "A flowchart says what to do next. A dialog map says where you can get to.")},
        {"svg": P5, "alt": ("장바구니에서 계산대로 가는 화살표는 있지만, 계산대에서 나가는 '취소' 화살표가 빨간 점선과 X로 표시됨", "An arrow from Cart to Checkout, and a missing 'cancel' arrow out of Checkout drawn in red dashes with an X"),
         "caption": ("그려보면 빠진 문이 보여요.", "Draw it, and the missing doors show."),
         "small": ("'취소' 문이 없는 계산대. 집을 짓기 전에 종이 위에서 고치면 싸요.", "A Checkout with no cancel. Fixing it on paper, before the house is built, is cheap.")},
    ],
    "summary": (("<b>다이얼로그 맵</b> = 앱의 방(화면)과 문(이동)을 그린 <b>지도</b>. 짓기 전에 길 잃을 곳을 찾아요.",
                 "A <b>dialog map</b> = a <b>map</b> of an app's rooms (screens) and doors (moves). It finds where people get lost, before building."),
                ("칼 위거스(Karl Wiegers)가 『소프트웨어 요구사항』에서 소개한 기법. 방 안의 가구(화면 레이아웃)는 그리지 않아요 — 그건 다른 그림이에요.",
                 "A technique from Karl Wiegers' <em>Software Requirements</em>. It doesn't draw the furniture (screen layout) — that's a different picture.")),
    "glossary": [
        ("상태", "State", ("방.", "A room."), ("웹페이지, 메뉴, 대화상자 — 지금 사용자가 서 있는 화면.", "A web page, a menu, a dialog box — the screen the user is standing in.")),
        ("전이", "Transition", ("문.", "A door."), ("버튼을 누르거나, 시스템이 어떤 일을 하면 다른 방으로 가는 것.", "How a button press or a system event moves you to another room.")),
        ("상태 전이도", "State-transition diagram", ("이 지도의 어른 이름.", "The grown-up name for this map."), ("다이얼로그 맵은 그걸 화면에 쓴 것.", "A dialog map is one applied to screens.")),
        ("순서도", "Flowchart", ("레시피.", "A recipe."), ("순서와 갈림길을 그려요. 지도와는 다른 질문에 답해요.", "Draws order and decisions. Answers a different question than the map.")),
        ("취소 경로", "Cancel path", ("나가는 문.", "The way out."), ("지도를 그리면 제일 자주 빠져 있는 문.", "The door most often found missing once you draw the map.")),
        ("요구사항", "Requirements", ("집 짓기 전 설계 종이.", "The plans before building."), ("여기서 고치면 싸고, 지은 뒤 고치면 비싸요.", "Cheap to fix here, expensive after it's built.")),
        ("칼 위거스", "Karl Wiegers", ("이 지도를 알린 사람.", "Who made the map well known."), ('<a href="https://www.processimpact.com/pubs.html#SR3E">Software Requirements, 3rd ed.</a>', '<a href="https://www.processimpact.com/pubs.html#SR3E">Software Requirements, 3rd ed.</a>')),
    ],
}
