from _draw import *
from _world import *

# 1. 손님이 몰려오는데 직원 수는 그대로예요
P1 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + booth(600, 230, 1.0, label_text="⟦창구|BOOTH⟧")
         + person(520, 163, s=0.6, face=SWEAT, **OPERATOR)
         + queueline(40, 174, 7, 0.45, 26)
         + label(230, 250, "⟦줄이 끝없이 길어져요|the line keeps growing forever⟧", 12, "var(--bad)", cls="d")
         + label(380, 282, "⟦손님이 갑자기 몰려오는데 직원 수가 그대로예요|guests suddenly flood in, but the staff count stays the same⟧", 12, "var(--ink)"))

# 2. 왜: 평소 기준으로 직원 수를 정하면 바쁠 땐 모자라고 한가할 땐 남아요
P2 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + booth(190, 230, 0.9, label_text="⟦바쁜 시간|BUSY⟧") + queueline(40, 174, 5, 0.4, 24)
         + person(300, 174, s=0.5, face=SWEAT, **OPERATOR) + label(190, 290, "⟦일손이 모자라요|short on hands⟧", 11, "var(--bad)")
         + booth(590, 230, 0.9, label_text="⟦한가한 시간|QUIET⟧")
         + person(530, 174, s=0.5, face=SMILE, **OPERATOR) + person(590, 174, s=0.5, face=SMILE, **MECHANIC) + person(650, 174, s=0.5, face=SMILE, **ROOKIE)
         + label(590, 290, "⟦직원이 남아요|staff sit idle⟧", 11, "var(--ink)")
         + label(380, 40, "⟦평소 기준으로 직원 수를 정하면, 바쁠 땐 모자라고 한가할 땐 남아요|size staff for the average, and you're short when busy, idle when quiet⟧", 12, "var(--ink)", cls="d"))

# 3. hero: 줄 길이를 보고 자동으로 직원을 더 부르거나 돌려보내요
P3 = svg(340, sky(340)
         + gauge(120, 130, 1.2, level=0.85, label_text="⟦줄 길이|QUEUE LENGTH⟧")
         + '<path d="M170 130 L300 180" stroke="var(--accent)" stroke-width="3" stroke-dasharray="6 4"/>'
         + booth(400, 270, 1.0, label_text="⟦창구|BOOTH⟧") + queueline(460, 214, 3, 0.45, 26)
         + person(330, 214, s=0.55, face=SMILE, **ROOKIE) + label(330, 198, "⟦+2 직원 투입|+2 staff called in⟧", 10, "var(--good)")
         + person(610, 160, s=0.5, face=SMILE, **MECHANIC) + label(610, 110, "⟦한가하면 돌려보내요|send them home when quiet⟧", 10, "var(--muted)")
         + label(380, 40, "⟦줄 길이를 보고 자동으로 직원을 더 부르거나 돌려보내요|watch the line length, and automatically call in more staff or send them home⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦바쁠 때 늘고, 한가할 때 줄어요|more when it's busy, fewer when it's quiet⟧", 12, "var(--muted)"))

# 4. 작동 디테일: 시간대별 손님 수 그래프 + 직원 수 그래프가 따라 움직여요
HOURS = (0.3, 0.4, 0.9, 1.0, 0.6, 0.3)
def _bars(x, y, vals, w=90, h=90, color="var(--accent)"):
    out = ""
    for i, v in enumerate(vals):
        bh = h * v
        out += f'<rect x="{x + i * w}" y="{y + h - bh}" width="{w - 10}" height="{bh}" fill="{color}"/>'
    return out
P4 = svg(320, sky(320)
         + _bars(60, 60, HOURS, 100, 90, "var(--accent)") + label(380, 40, "⟦시간대별 손님 수|guests by hour⟧", 12, "var(--ink)", cls="d")
         + '<path d="M105 230 L205 220 L305 170 L405 160 L505 200 L605 230" stroke="var(--good)" stroke-width="4" fill="none" stroke-linecap="round"/>'
         + "".join(f'<circle cx="{105 + i * 100}" cy="{[230,220,170,160,200,230][i]}" r="6" fill="var(--good)"/>' for i in range(6))
         + label(380, 265, "⟦직원 수도 그 모양을 따라 움직여요|the staff count follows the same shape⟧", 12, "var(--good)")
         + label(380, 295, "⟦손님이 늘면 직원도 늘고, 줄면 같이 줄어요|more guests, more staff — fewer guests, fewer staff⟧", 11, "var(--muted)"))

# 5. 깨지는 곳: 늘리는 데도 시간이 걸려요
P5 = svg(300, sky(300)
         + booth(560, 230, 1.0, label_text="⟦창구|BOOTH⟧") + queueline(380, 174, 5, 0.45, 26)
         + person(620, 163, s=0.6, face=EYES, **ROOKIE) + bubble(480, 70, 220, 50, "⟦아직 교육 중이라... 조금만요|still in training... just a bit more⟧", 11, "var(--panel)", "var(--line)", "right")
         + person(80, 163, s=0.6, face=EYES, **MANAGER) + bubble(10, 100, 200, 44, "⟦미리 예측해서 당겨 늘려요|predict ahead and scale early⟧", 10, "var(--panel)", "var(--line)", "bottom")
         + label(380, 282, "⟦늘리는 데 시간이 걸리면, 그 사이는 여전히 힘들어요|scaling up takes time, so the gap in between is still rough⟧", 12, "var(--ink)"))

WATCH2_I = icon('<circle cx="24" cy="24" r="14" fill="none" stroke="var(--accent)" stroke-width="4"/><circle cx="24" cy="24" r="5" fill="var(--accent)"/><path d="M14 44 h40" stroke="var(--muted)" stroke-width="4" stroke-linecap="round"/>')
CLOCK_I = icon('<circle cx="32" cy="32" r="22" fill="var(--panel)" stroke="var(--stone-dark)" stroke-width="4"/><path d="M32 18 V32 L44 40" stroke="var(--accent)" stroke-width="4" fill="none" stroke-linecap="round"/>')
ZIGZAG_I = icon('<path d="M8 44 L20 16 L32 44 L44 16 L56 44" stroke="var(--bad)" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
MINMAX_I = icon('<path d="M14 12 h12 M14 12 v14 M50 12 h-12 M50 12 v14" stroke="var(--good)" stroke-width="4" fill="none"/><path d="M14 52 h12 M14 52 v-14 M50 52 h-12 M50 52 v-14" stroke="var(--good)" stroke-width="4" fill="none"/>')

PAGE = {
    "slug": "autoscaling", "order": 30,
    "title": ("줄이 길어지면 직원을 더 부르기", "Call In More Staff When the Line Grows"),
    "h1": ("<em>오토스케일링</em>이 뭐예요?", "What is <em>Autoscaling</em>?"),
    "sub": ("오토스케일링을 줄 길이를 보고 직원을 자동으로 부르거나 돌려보내는 이야기로 풀어봤어요.",
            "Autoscaling, told as a story about calling in staff — or sending them home — automatically, based on how long the line is."),
    "panels": [
        {"svg": P1, "alt": ("손님 일곱 명이 줄을 서 있고 직원은 한 명뿐이라 줄이 끝없이 길어짐", "Seven guests wait in line while only one staff member is on duty, and the line keeps growing"),
         "caption": ("손님이 갑자기 몰려오는데 직원 수가 그대로예요.", "Guests suddenly flood in, but the staff count stays the same."),
         "small": ("사람 수를 안 늘리면 줄은 계속 길어지기만 해요.", "Without more hands, the line just keeps growing.")},
        {"svg": P2, "alt": ("왼쪽: 바쁜 시간엔 일손이 모자람. 오른쪽: 한가한 시간엔 직원 셋이 남아돎", "Left: short on hands during the busy hour. Right: three staff sitting idle during the quiet hour"),
         "caption": ("평소 기준으로 직원 수를 정하면, 바쁠 땐 모자라고 한가할 땐 남아요.", "Size staff for the average, and you're short when busy, idle when quiet."),
         "small": ("한 가지 숫자로는 둘 다 맞출 수 없어요.", "One fixed number can't fit both.")},
        {"svg": P3, "hero": True, "alt": ("계기판이 줄 길이를 보여주고, 신참 직원 둘이 창구로 투입되며, 한가해지면 정비사가 집으로 돌아감", "A gauge shows the queue length, two rookie staff are called in to the booth, and a mechanic heads home once it's quiet"),
         "caption": ("줄 길이를 보고 자동으로 직원을 더 부르거나 돌려보내요.", "Watch the line length, and automatically call in more staff or send them home."),
         "small": ("바쁠 때 늘고, 한가할 때 줄어요.", "More when it's busy, fewer when it's quiet."),
         "tricks": (4, [
             (WATCH2_I, ("뭘 보고 늘릴지 정해요", "Decide what to watch"), ("줄 길이나 계기판이에요", "the queue length, a gauge"), "calm"),
             (CLOCK_I, ("늘리는 데도 시간이 걸려요", "Scaling up takes time too"), ("새 직원 교육처럼요", "like training new staff")),
             (ZIGZAG_I, ("너무 자주 늘렸다 줄이면 피곤해요", "Flip-flopping too often is tiring"), ("스레싱이라고 불러요", "that's called thrashing"), "warm"),
             (MINMAX_I, ("최대·최소 한도를 정해둬요", "Set a max and a min"), ("너무 늘거나 줄지 않게요", "so it never goes too far either way")),
         ])},
        {"svg": P4, "alt": ("시간대별 손님 수를 보여주는 막대그래프와, 그 모양을 따라 오르내리는 직원 수 선그래프", "A bar chart of guests by hour, with a line showing staff count rising and falling along the same shape"),
         "caption": ("직원 수도 손님 수의 모양을 따라 움직여요.", "The staff count follows the same shape as the guest count."),
         "small": ("손님이 늘면 직원도 늘고, 줄면 같이 줄어요.", "More guests, more staff — fewer guests, fewer staff.")},
        {"svg": P5, "alt": ("손님이 몰려 줄이 길어졌는데 신참 직원은 아직 교육 중이라 못 돕고, 공원장은 미리 예측해서 당겨 늘리자고 말함", "The line has grown but a rookie staffer is still in training and can't help yet, while the manager suggests predicting ahead and scaling early"),
         "caption": ("늘리는 데 시간이 걸리면, 그 사이는 여전히 힘들어요.", "Scaling up takes time, so the gap in between is still rough."),
         "small": ("그래서 미리 예측해서 당겨 늘리기도 해요.", "That's why some systems predict ahead and scale early.")},
    ],
    "summary": (("<b>오토스케일링</b> = 줄 길이(또는 계기판)를 보고 <b>직원 수(서버 수)를 자동으로</b> 늘리거나 줄이는 일. 최대·최소 한도 안에서 움직여요.",
                 "<b>Autoscaling</b> = watching the queue (or a gauge) and <b>automatically</b> adding or removing staff (servers) — always within a set max and min."),
                ("서버 수를 트래픽에 맞춰 자동으로 늘리거나 줄이는 기법이에요. 서버를 늘리는 수평 확장(스케일 아웃)과 서버 자체를 키우는 수직 확장이 있고, 지표를 보고 결정해요. 너무 자주 오르내리면 스레싱이 생겨 최대·최소 한도와 안정화 시간을 둬요.",
                 "A technique that automatically adds or removes servers to match traffic. It can mean scaling out (adding more servers) or scaling up (making a server bigger), decided by watching metrics. Flipping too often causes thrashing, so systems set a max/min and a cooldown period.")),
    "glossary": [
        ("오토스케일링", "Autoscaling", ("직원 수를 자동으로 늘리고 줄이는 일.", "Automatically adding and removing staff."), ("줄 길이나 계기판을 보고 판단해요.", "It decides by watching the queue or a gauge.")),
        ("수평/수직 확장", "Horizontal / Vertical scaling", ("직원을 늘리는 두 가지 방법.", "Two ways to add more hands."), ("사람을 더 뽑거나(수평), 한 사람을 더 세게 쓰거나(수직)예요.", "Hire more people (horizontal), or make one person work harder (vertical).")),
        ("스케일링 지표", "Scaling metric", ("뭘 보고 늘릴지 정하는 숫자.", "The number that decides when to scale."), ("줄 길이, 계기판 바늘 같은 거예요.", "Things like queue length or a gauge reading.")),
        ("스케일 아웃 지연", "Scale-out delay", ("새 직원이 일할 수 있을 때까지 걸리는 시간.", "How long until a new hire can actually help."), ("그 사이는 여전히 힘들어요.", "The gap in between is still rough.")),
        ("스레싱", "Thrashing", ("너무 자주 늘렸다 줄였다 하는 것.", "Scaling up and down too often."), ("안정화 시간을 둬서 막아요.", "A cooldown period keeps this from happening.")),
        ("최대/최소 한도", "Max / Min limits", ("너무 늘거나 줄지 않게 정해둔 울타리.", "The fence that keeps scaling from going too far."), ("이 안에서만 늘고 줄어요.", "Scaling only happens within these bounds.")),
        ("예측 스케일링", "Predictive scaling", ("미리 예측해서 당겨 늘리는 방법.", "Scaling up early, based on a prediction."), ("내년 손님 수를 미리 세어보는 것과 통해요.", "This connects to estimating next year's guest count in advance.")),
        ("오케스트레이션", "Orchestration", ("몇 대를 켤지 정하는 운영 본부.", "The control room deciding how many to run."), ("오토스케일링의 결정을 실제로 실행에 옮기는 역할이에요.", "It's what actually carries out the autoscaling decision.")),
    ],
}
