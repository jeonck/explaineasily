from _draw import *
from _world import *

# 1. 주 발전기가 꺼져서 공원 전체가 깜깜해짐, 예비가 없어서 한참 복구
P1 = svg(300, night(300)
         + shed(160, 230, 1.0)
         + label(160, 160, "⟦주 발전기|MAIN GENERATOR⟧", 11, "#C9D5E6", cls="d")
         + '<g transform="translate(160,205)"><rect x="-46" y="-6" width="92" height="10" fill="var(--bad)" transform="rotate(-8)"/><rect x="-46" y="10" width="92" height="10" fill="var(--bad)" transform="rotate(6)"/></g>'
         + ride(420, 230, 0.8, color="#3A4A68") + ride(540, 230, 0.6, color="#3A4A68")
         + person(650, 163, s=0.6, face=SWEAT, extra=WRENCH, **MECHANIC)
         + bubble(540, 70, 200, 50, "⟦예비가 없어서 한참 걸려요...|no spare, so this takes forever...⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 285, "⟦주 발전기가 꺼져서 공원 전체가 깜깜해졌어요 — 예비가 없어서 한참 걸려요|the main generator died and the whole park went dark — with no spare, it takes forever⟧", 12, "#F5E6B8", cls="d"))

# 2. 왜: 하나에만 의존하면 그게 멈추는 순간 전부 멈춰요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + shed(220, 230, 1.0, label_text="⟦발전기 딱 하나|only one generator⟧")
         + '<path d="M260 180 Q400 140 540 180" stroke="var(--bad)" stroke-width="3" stroke-dasharray="6 4" fill="none"/>'
         + ride(540, 230, 0.6, color="var(--stone)", closed=True) + ride(640, 230, 0.55, color="var(--stone)", closed=True)
         + label(590, 150, "⟦연결된 기구가 다 같이 멈춰요|everything connected stops together⟧", 11, "var(--bad)")
         + label(380, 285, "⟦하나에만 의존하면, 그게 멈추는 순간 전부 멈춰요|depend on just one thing, and the moment it stops, everything stops⟧", 12, "var(--ink)"))

# 3. hero: 평소엔 꺼둔 예비 발전기를, 주 발전기가 꺼지는 순간 자동으로 켜서 넘겨요
P3 = svg(340, sky(340)
         + shed(140, 280, 1.0, label_text="⟦주 발전기(꺼짐)|MAIN (down)⟧")
         + '<g transform="translate(140,250)"><rect x="-46" y="-6" width="92" height="10" fill="var(--bad)" transform="rotate(-8)"/><rect x="-46" y="10" width="92" height="10" fill="var(--bad)" transform="rotate(6)"/></g>'
         + '<path d="M210 230 L420 200" stroke="var(--accent)" stroke-width="4" stroke-dasharray="4 4"/><path d="M400 192 l22 10 -8 20z" fill="var(--accent)"/>'
         + shed(480, 280, 1.0, label_text="⟦예비 발전기(켜짐)|SPARE (now on)⟧")
         + person(600, 202, s=0.7, face=SMILE, **OPERATOR) + walkie(660, 182, 0.8)
         + ride(700, 280, 0.55, color="var(--good)")
         + label(380, 30, "⟦주 발전기가 꺼지면, 예비 발전기가 자동으로 넘겨받아요|when the main generator dies, the spare automatically takes over⟧", 14, "var(--ink)", cls="d")
         + label(380, 325, "⟦평소엔 꺼둔 예비가, 그 순간엔 스스로 켜져요|normally off, the spare switches itself on the moment it's needed⟧", 12, "var(--muted)"))

# 4. 주 발전기(꺼짐) → 신호 → 예비 발전기(켜짐)로 자동 전환되는 화살표 그림
P4 = svg(300, sky(300)
         + board(40, 30, 280, 160, "⟦자동 전환 순서|AUTO-SWITCH STEPS⟧", ("⟦① 주 발전기 꺼짐 감지|① main found down⟧", "⟦② 예비에 신호 보내기|② signal sent to spare⟧", "⟦③ 예비가 넘겨받음|③ spare takes over⟧", "⟦④ 다시 켜지면 안내|④ announce when it's back⟧"), 1.0)
         + shed(480, 240, 0.8, label_text="⟦주 발전기|MAIN⟧")
         + '<g transform="translate(480,215)"><rect x="-37" y="-5" width="74" height="8" fill="var(--bad)" transform="rotate(-8)"/><rect x="-37" y="7" width="74" height="8" fill="var(--bad)" transform="rotate(6)"/></g>'
         + '<path d="M540 200 Q610 170 660 220" stroke="var(--good)" stroke-width="3" stroke-dasharray="6 4" fill="none"/><path d="M645 206 l20 14 -22 6z" fill="var(--good)"/>'
         + shed(690, 240, 0.65, label_text="⟦예비|SPARE⟧")
         + label(380, 282, "⟦감지 → 신호 → 전환, 이 세 가지가 자동으로 이어져요|detect, signal, switch — the three happen automatically, one after another⟧", 12, "var(--ink)"))

# 5. 깨지는 곳: 전환 순간은 느껴질 수 있고, 테스트 안 한 예비는 고장나 있을 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--bad-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + person(130, 174, s=0.6, face=EYES, shirt="#7B3FA0")
         + bubble(60, 90, 200, 46, "⟦어, 잠깐 멈췄었나?|huh, did it just stop for a second?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(190, 245, "⟦전환하는 그 짧은 순간은 손님이 느낄 수 있어요|that brief instant of switching can still be felt⟧", 11, "var(--ink)")
         + shed(590, 230, 0.8) + '<g transform="translate(590,205)"><rect x="-37" y="-5" width="74" height="8" fill="var(--bad)" transform="rotate(-8)"/><rect x="-37" y="7" width="74" height="8" fill="var(--bad)" transform="rotate(6)"/></g>'
         + label(590, 150, "⟦테스트 안 한 예비|an untested spare⟧", 11, "var(--bad)", cls="d")
         + label(590, 245, "⟦가끔 테스트 안 하면, 예비도 고장나 있을 수 있어요|skip the occasional test, and the spare might be broken too⟧", 11, "var(--ink)")
         + label(380, 288, "⟦그 둘 다 신경 써야 진짜 장애 조치예요|a true failover has to account for both⟧", 12, "var(--ink)", cls="d"))

OFFCOST_I = icon('<rect x="10" y="24" width="44" height="30" rx="4" fill="var(--stone)"/><path d="M20 24 V16 h24 v8" stroke="var(--stone-dark)" stroke-width="4" fill="none"/><text x="32" y="44" text-anchor="middle" font-size="14" font-weight="700" fill="var(--panel)">zZ</text>')
DETECT_I = icon('<circle cx="26" cy="26" r="16" fill="none" stroke="var(--accent)" stroke-width="5"/><path d="M38 38 L54 54" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/><path d="M18 26 h6 l3 -8 4 16 3 -8 h6" stroke="var(--bad)" stroke-width="3" fill="none"/>')
SWITCH_I = icon('<path d="M10 20 h30" stroke="var(--good)" stroke-width="5"/><path d="M32 12 l10 8 -10 8z" fill="var(--good)"/><path d="M54 44 h-30" stroke="var(--bad)" stroke-width="5"/><path d="M32 36 l-10 8 10 8z" fill="var(--bad)"/>')
TEST_I = icon('<rect x="14" y="10" width="36" height="44" rx="4" fill="var(--panel)" stroke="var(--line)" stroke-width="3"/><path d="M22 22 h20 M22 30 h20 M22 38 h12" stroke="var(--muted)" stroke-width="3" stroke-linecap="round"/><circle cx="46" cy="44" r="9" fill="var(--good)"/><path d="M42 44 l3 4 6 -8" stroke="#FFF8E7" stroke-width="2.5" fill="none" stroke-linecap="round"/>')

PAGE = {
    "slug": "failover", "order": 28,
    "title": ("발전기가 꺼지면 예비 발전기가", "When the Generator Dies, the Spare Takes Over"),
    "h1": ("<em>장애 조치</em>가 뭐예요?", "What is <em>Failover</em>?"),
    "sub": ("장애 조치를, 주 발전기가 꺼지면 예비 발전기가 자동으로 넘겨받는 이야기로 풀어봤어요.",
            "Failover, told as a story about a spare generator that automatically takes over when the main one dies."),
    "panels": [
        {"svg": P1, "alt": ("밤에 주 발전기가 고장나 공원이 어둡고, 정비사가 땀을 흘리며 예비가 없어서 오래 걸린다고 말함", "At night the main generator is down and the park is dark; a sweating mechanic says it takes forever with no spare"),
         "caption": ("주 발전기가 꺼져서 공원 전체가 깜깜해졌어요.", "The main generator died and the whole park went dark."),
         "small": ("예비가 없어서 한참 걸려요.", "With no spare, it takes forever.")},
        {"svg": P2, "alt": ("발전기 하나에 연결된 기구 두 개가 함께 고장남을 화살표로 보여줌", "An arrow shows two rides both failing because they're tied to one generator"),
         "caption": ("하나에만 의존하면, 그게 멈추는 순간 전부 멈춰요.", "Depend on just one thing, and the moment it stops, everything stops."),
         "small": ("연결된 기구가 다 같이 멈춰요.", "Everything connected stops together.")},
        {"svg": P3, "hero": True, "alt": ("꺼진 주 발전기에서 화살표가 예비 발전기로 이어지고, 예비가 켜져 기구를 돌림", "An arrow runs from the dead main generator to the spare, which switches on and keeps a ride running"),
         "caption": ("주 발전기가 꺼지면, 예비 발전기가 자동으로 넘겨받아요.", "When the main generator dies, the spare automatically takes over."),
         "small": ("평소엔 꺼둔 예비가, 그 순간엔 스스로 켜져요.", "Normally off, the spare switches itself on the moment it's needed."),
         "tricks": (4, [
             (OFFCOST_I, ("평소엔 예비를 꺼둬요", "Normally keep the spare off"), ("비용 때문이에요", "it costs money to run"), "calm"),
             (DETECT_I, ("자동으로 알아채요", "Automatically detect the failure"), ("주 발전기가 꺼지면요", "the moment the main one dies")),
             (SWITCH_I, ("자동으로 전환해요", "Switch over automatically"), ("수동이면 늦어요", "manual is too slow"), "warm"),
             (TEST_I, ("가끔 예비도 테스트해요", "Test the spare now and then"), ("안 켜지면 소용없어요", "useless if it won't turn on")),
         ])},
        {"svg": P4, "alt": ("안내판에 자동 전환 네 단계가 적혀 있고, 꺼진 주 발전기에서 예비 발전기로 신호 화살표가 이어짐", "A sign lists the four auto-switch steps, with a signal arrow from the dead main generator to the spare"),
         "caption": ("감지 → 신호 → 전환, 이 세 가지가 자동으로 이어져요.", "Detect, signal, switch — the three happen automatically, one after another."),
         "small": ("주 발전기가 멈추면, 예비가 바로 넘겨받아요.", "The moment the main one stops, the spare takes over right away.")},
        {"svg": P5, "alt": ("왼쪽: 손님이 짧은 멈춤을 느낌. 오른쪽: 테스트 안 한 예비 발전기도 고장나 있음", "Left: a guest notices a brief pause. Right: an untested spare generator turns out to be broken too"),
         "caption": ("전환하는 그 짧은 순간은 손님이 느낄 수 있어요.", "That brief instant of switching can still be felt."),
         "small": ("가끔 테스트 안 하면, 예비도 고장나 있을 수 있어요.", "Skip the occasional test, and the spare might be broken too.")},
    ],
    "summary": (("<b>장애 조치</b> = 평소엔 꺼둔 <b>예비</b>를, 주 발전기가 멈추는 순간 <b>자동으로 알아채고 전환</b>해 서비스를 이어가는 일. 전환 순간은 완전히 안 느껴지게는 못 해도, <b>가끔 테스트</b>해 두면 예비가 멀쩡한지 확인돼요.",
                 "<b>Failover</b> = keeping a <b>spare</b> off until it's needed, then <b>automatically detecting and switching</b> to it the moment the main one dies, to keep the service going. The switch is never perfectly invisible, but <b>testing it now and then</b> confirms the spare actually works."),
                ("한 구성 요소가 실패했을 때 대기 중인 다른 구성 요소로 자동 전환하는 메커니즘이에요. 액티브-패시브(평소엔 대기)와 액티브-액티브(둘 다 받음) 방식이 있고, 전환에 걸리는 시간을 failover time이라고 불러요.",
                 "A mechanism that automatically switches to a standby component when one fails. It can be active-passive (the spare waits idle) or active-active (both take traffic), and the time a switch takes is called the failover time.")),
    "glossary": [
        ("장애 조치", "Failover", ("주 발전기가 꺼지면 예비로 넘어가는 일.", "Switching to the spare when the main generator dies."), ("자동으로, 빠르게 일어나야 의미가 있어요.", "It only works if it happens automatically and fast.")),
        ("액티브-패시브", "Active-passive", ("예비는 평소엔 대기만 해요.", "The spare just waits, idle, most of the time."), ("주 발전기가 멈춰야 그제서야 켜져요.", "It only switches on once the main one stops.")),
        ("액티브-액티브", "Active-active", ("둘 다 평소에도 손님을 받아요.", "Both take guests at the same time, all along."), ("하나가 멈춰도 나머지가 이미 돌고 있어요.", "If one stops, the other is already running.")),
        ("자동 전환", "Automatic switch", ("사람이 누르지 않아도 스스로 넘어가는 것.", "Switching over by itself, with no one pressing a button."), ("수동으로 하면 그만큼 늦어져요.", "A manual switch is slower by exactly that much.")),
        ("전환 시간", "Failover time", ("전환이 끝날 때까지 걸리는 시간.", "How long the switch takes from start to finish."), ("0초는 어려워요 — 그 짧은 순간은 손님이 느낄 수 있어요.", "Zero seconds is hard — that brief instant can still be felt.")),
        ("헬스 체크", "Health check", ("주 발전기가 살아 있는지 계속 확인하는 일.", "Continually checking whether the main generator is still alive."), ("이게 있어야 '꺼졌다'는 걸 자동으로 알아채요.", "Without it, nothing can automatically notice the main one is down.")),
        ("다중 리전", "Multi-region", ("발전기가 아니라 도시 전체를 예비로 두는 것.", "Keeping a whole spare city, not just a spare generator."), ('장애 조치를 도시 단위로 키운 이야기예요. → <a href="multiregion-ko.html">쌍둥이 공원</a>', 'Failover scaled up to the size of a city. → <a href="multiregion-en.html">the twin park</a>')),
        ("복제", "Replication", ("명부도 예비 쪽에 미리 똑같이 적어 두는 일.", "Keeping the same log copied over to the spare side too."), ("예비가 넘겨받아도 명부가 없으면 소용없어요.", "A spare that takes over with no log is useless.")),
    ],
}
