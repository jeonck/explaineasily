from _draw import *
from _world import *

# 1. 옛날 전화선: 통화 내내 도로를 혼자 독점
P1 = svg(300, sky(300)
         + tollgate(260, 170, 1.0, open_=True)
         + person(180, 200, s=0.7, face=SMILE, **SENDER) + person(420, 200, s=0.7, face=SMILE, **RECEIVER)
         + label(380, 40, "⟦통화하는 내내 도로 하나를 둘이서만 써요|while they talk, the whole road is reserved just for the two of them⟧", 13, "var(--ink)")
         + label(380, 270, "⟦아무도 말을 안 해도 그 도로는 계속 비워둬요|even during silence, that road stays reserved, unused⟧", 13, "var(--bad)"))

# 2. 트럭이 많아지면 전용 도로 방식은 금방 한계
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + tollgate(160, 170, 0.8) + tollgate(300, 170, 0.8) + tollgate(440, 170, 0.8)
         + person(600, 170, s=0.7, face=SWEAT + FROWN, **SENDER)
         + label(380, 70, "⟦사람이 늘어날수록 전용 도로도 더 많이 필요해요|more people means more dedicated roads are needed⟧", 12, "var(--ink)")
         + label(380, 270, "⟦도로는 한정돼 있는데 쓰는 사람은 계속 늘어나요|the roads are limited, but the number of users keeps growing⟧", 12, "var(--ink)"))

# 3. hero: 패킷교환 = 봉투를 조각내 여러 길로 보냈다가 모으는 것
P3 = svg(340, sky(340)
         + person(160, 150, s=0.75, face=EYES, **SENDER)
         + envelope(300, 110, 0.45, text="①") + envelope(300, 190, 0.45, text="②") + envelope(300, 270, 0.45, text="③")
         + postoffice(460, 190, 0.7)
         + person(620, 150, s=0.75, face=SMILE, **RECEIVER)
         + label(380, 30, "⟦패킷교환 = 봉투를 조각내 각자 다른 길로 보냈다가, 도착지에서 다시 모으는 것|packet switching = splitting the envelope into pieces, sending each by a different road, then reassembling at the end⟧", 11, "var(--ink)", cls="d")
         + label(380, 320, "⟦도로를 독점하지 않으니 여러 사람이 같이 나눠 써요|no one hogs a road, so many people share it at once⟧", 12, "var(--muted)"))

I1 = icon('<rect x="12" y="24" width="12" height="16" rx="2" fill="var(--accent)"/><rect x="26" y="24" width="12" height="16" rx="2" fill="var(--accent)"/><rect x="40" y="24" width="12" height="16" rx="2" fill="var(--accent)"/>')
I2 = icon('<path d="M10 20 Q32 10 54 20" stroke="var(--good)" stroke-width="3" fill="none"/><path d="M10 44 Q32 54 54 44" stroke="var(--accent)" stroke-width="3" fill="none"/>')
I3 = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="4"/><text x="32" y="38" font-size="16" font-weight="700" fill="var(--accent)" text-anchor="middle">3/5</text>')
I4 = icon('<circle cx="18" cy="32" r="8" fill="var(--good)"/><circle cx="46" cy="18" r="8" fill="var(--good)"/><circle cx="46" cy="46" r="8" fill="var(--good)"/>')

# 4. 두 방식 비교
P4 = svg(320, sky(320)
         + routemap(60, 40, 640, 240, "⟦회선교환 vs 패킷교환|CIRCUIT vs PACKET SWITCHING⟧",
                    ("⟦회선교환 — 통화 내내 도로를 독점, 품질은 안정적|circuit — reserves the road for the whole call, steady quality⟧",
                     "⟦패킷교환 — 도로를 나눠 쓰고, 조각마다 다른 길로 갈 수 있어요|packet — shares the road, each piece may take a different route⟧",
                     "⟦순서 번호 — 패킷교환은 조각에 번호를 매겨 도착지에서 다시 맞춰요|sequence number — packets get numbered to be reassembled at the end⟧",
                     "⟦효율 — 패킷교환은 쉬는 도로를 남한테 빌려줄 수 있어요|efficiency — packet switching lets an idle road serve someone else⟧"), 1.0))

# 5. 한계: 패킷교환은 길이 제각각이라 순서가 뒤섞이거나 늦게 올 수 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--accent-soft)"/>'
         + tollgate(190, 160, 1.0) + label(190, 250, "⟦회선교환은 도로를 낭비하지만 안정적이에요|circuit wastes the road but stays steady⟧", 11, "var(--ink)")
         + envelope(540, 130, 0.5) + envelope(600, 170, 0.5) + envelope(560, 210, 0.5)
         + label(570, 260, "⟦패킷교환은 효율적이지만 순서가 뒤섞일 수 있어요|packet is efficient but pieces can arrive out of order⟧", 11, "var(--ink)")
         + label(380, 40, "⟦등기(TCP)는 패킷교환 위에서 순서까지 맞춰주는 방식이에요|registered mail (TCP) is how packet switching still fixes the order⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "circuitpacket", "order": 22,
    "title": ("전용 도로냐, 조각내 보내기냐", "A Dedicated Road, or Splitting It Into Pieces"),
    "h1": ("<em>회선교환·패킷교환</em>이 뭐예요?", "What are <em>Circuit & Packet Switching</em>?"),
    "sub": ("회선교환·패킷교환을, 통화 내내 도로를 독점할지 봉투를 조각내 나눠 보낼지 고르는 이야기로 풀어봤어요.",
            "Circuit and packet switching, told as a story about choosing between reserving a whole road for a call, or splitting an envelope into pieces to share the road."),
    "panels": [
        {"svg": P1, "alt": ("두 사람이 통화하는 내내 도로 하나를 독점해 톨게이트가 열려 있음", "Two people keep a road reserved for themselves through an open tollgate, for the whole call"),
         "caption": ("통화하는 내내 도로 하나를 둘이서만 써요.", "While they talk, the whole road is reserved just for the two of them."),
         "small": ("아무도 말을 안 해도 그 도로는 계속 비워둬요.", "Even during silence, that road stays reserved, unused.")},
        {"svg": P2, "alt": ("톨게이트 세 개가 늘어서 있고, 한 사람이 땀을 흘리며 더 필요한 도로를 기다림", "Three tollgates line up, and a person sweats, waiting for yet another dedicated road"),
         "caption": ("사람이 많아지면 전용 도로 방식은 한계에 부딪혀요.", "More people pushes the dedicated-road method to its limit."),
         "small": ("도로는 한정돼 있는데 쓰는 사람은 계속 늘어나요.", "The roads are limited, but the number of users keeps growing.")},
        {"svg": P3, "hero": True, "alt": ("봉투가 셋으로 조각나 각각 다른 길로 가다가 우체국에서 다시 모여 받는 사람에게 도착함", "An envelope splits into three pieces, travels different roads, and is reassembled at a post office before reaching the receiver"),
         "caption": ("패킷교환 = 봉투를 조각내 보냈다가 다시 모으는 거예요.", "Packet switching = splitting the envelope into pieces, then reassembling them."),
         "small": ("도로를 독점하지 않으니 여러 사람이 같이 나눠 써요.", "No one hogs a road, so many people share it at once."),
         "tricks": (4, [
             (I1, ("조각내기", "Split Into Pieces"), ("봉투를 여러 개로", "breaks it into several parts")),
             (I2, ("각자 다른 길", "Different Roads"), ("조각마다 길이 달라요", "each piece may take a different road"), "calm"),
             (I3, ("번호 매기기", "Number Them"), ("도착지에서 다시 맞춰요", "reassembled at the destination"), "warm"),
             (I4, ("나눠 쓰기", "Shared Use"), ("도로를 독점 안 해요", "no one hogs the road")),
         ])},
        {"svg": P4, "alt": ("회선교환과 패킷교환을 비교하는 안내판: 전용 도로, 공유, 순서 번호, 효율 네 줄", "A comparison board for circuit vs packet switching: dedicated road, sharing, sequence number, efficiency"),
         "caption": ("두 방식은 트레이드오프가 달라요.", "The two methods trade off different things."),
         "small": ("회선교환은 안정적이고, 패킷교환은 효율적이에요.", "Circuit switching is steady; packet switching is efficient.")},
        {"svg": P5, "alt": ("왼쪽: 회선교환은 도로를 낭비하지만 안정적임. 오른쪽: 패킷교환은 효율적이지만 순서가 뒤섞일 수 있음", "Left: circuit switching wastes the road but stays steady. Right: packet switching is efficient but order can get scrambled"),
         "caption": ("패킷교환은 순서가 뒤섞일 수 있어요.", "Packet switching can have pieces arrive out of order."),
         "small": ("등기(TCP)는 패킷교환 위에서 순서까지 맞춰주는 방식이에요.", "Registered mail (TCP) is how packet switching still fixes the order on top.")},
    ],
    "summary": (("<b>회선교환</b> = 통화 내내 <b>도로 하나를 독점</b>. <b>패킷교환</b> = 봉투를 <b>조각내 나눠 보냈다가 다시 모으는</b> 방식.",
                 "<b>Circuit switching</b> = <b>reserving one whole road</b> for the duration of a call. <b>Packet switching</b> = <b>splitting into pieces</b>, sending them separately, and reassembling them."),
                ("회선교환은 통신이 끝날 때까지 전용 회선을 독점적으로 점유해 품질은 안정적이지만 자원 낭비가 크고(전화망이 대표적), 패킷교환은 데이터를 패킷 단위로 쪼개 공유 회선을 거쳐 보낸 뒤 도착지에서 순서대로 재조립해요(인터넷이 대표적). 패킷교환이 자원을 효율적으로 쓰지만, 혼잡·지연·순서 뒤섞임이 생길 수 있어요.",
                 "Circuit switching dedicates a line exclusively until the session ends — stable quality, but wasteful of resources (the classic phone network). Packet switching splits data into packets, sends them over a shared line, and reassembles them in order at the destination (the classic internet). It uses resources efficiently, but can suffer congestion, delay, and out-of-order arrival.")),
    "glossary": [
        ("회선교환", "Circuit Switching", ("통화 내내 독점하는 전용 도로.", "The dedicated road reserved for the whole call."), ("전통적인 전화망 방식이에요.", "The classic telephone-network method.")),
        ("패킷교환", "Packet Switching", ("봉투를 조각내 나눠 보내는 방식.", "Splitting the envelope into pieces to send separately."), ("오늘날 인터넷의 기본 방식이에요.", "The basic method of today's internet.")),
        ("패킷", "Packet", ("조각난 봉투 하나하나.", "Each individual piece of the split envelope."), ("순서 번호가 붙어 재조립돼요.", "Carries a sequence number for reassembly.")),
        ("전송계층(TCP/UDP)", "Transport Layer (TCP/UDP)", ("등기냐 일반우편이냐를 정하는 단계.", "The stage that decides registered mail or plain."), ('패킷교환 위에서 순서·신뢰도를 책임져요. → <a href="transportlayer-ko.html">포트를 나누고 신뢰도를 고르는 단계</a>', "Handles order and reliability on top of packet switching. → <a href=\"transportlayer-en.html\">the stage that splits ports and picks reliability</a>")),
        ("OSI 7계층", "OSI 7 Layers", ("배송 전체를 7단계로 나눈 공정.", "The whole delivery process split into 7 stages."), ('교환 방식은 이 공정의 특정 단계에 해당해요. → <a href="osi7-ko.html">7단계로 나뉜 배송 공정</a>', 'Switching corresponds to specific stages in this process. → <a href="osi7-en.html">the delivery process split into 7 stages</a>')),
        ("Modbus", "Modbus", ("산업 현장의 단순한 쪽지 규칙.", "A simple note rule used on factory floors."), ('이 규칙도 결국 어느 교환 방식 위에서 오가요. → <a href="modbus-ko.html">우체국장이 순서대로 묻는 쪽지 규칙</a>', 'This rule, too, ultimately rides on one of these switching methods. → <a href="modbus-en.html">the note rule where the clerk asks one at a time</a>')),
        ("Ad-hoc 라우팅", "Ad-hoc Routing", ("고정 우체국 없이 서로 길을 찾는 법.", "Finding the way among themselves, with no fixed post office."), ('패킷이 매번 다른 길을 찾는 상황의 극단적인 예예요. → <a href="adhocrouting-ko.html">집배원끼리 길을 찾아 전달하는 법</a>', "An extreme case of packets finding a fresh path each time. → <a href=\"adhocrouting-en.html\">how carriers find the way among themselves</a>")),
        ("5G 네트워크 슬라이싱", "5G Network Slicing", ("도로를 상황별 차선으로 나누는 기술.", "The technology that splits the road into situational lanes."), ('전용 차선을 만든다는 점에서 회선교환과 닮았어요. → <a href="5gcore-ko.html">상황별 전용 차선을 가진 배송망</a>', "Carves out dedicated lanes, echoing circuit switching's idea. → <a href=\"5gcore-en.html\">the network with a lane for every need</a>")),
    ],
}
