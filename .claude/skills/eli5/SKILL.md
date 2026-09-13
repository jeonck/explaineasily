---
name: eli5
description: 어려운 용어·개념을 "다섯 살도 알 수 있게" 그림책 한 권으로 만드는 스킬. 큰 SVG 그림 한 장 + 한 문장 짜리 패널 3~5장, 한 줄 요약, 쉬운 말→원어 대응표로 구성된 한글·영문 HTML 페이지를 terms/<분야>/<slug>.py 로 작성하고 build.py 로 생성한다. 사용자가 "쉽게 설명해줘", "ELI5", "그림책으로 만들어줘", "다섯 살도 알게", "explain like I'm 5", "이 용어도 같은 형식으로" 라고 하거나, 새 용어를 이 저장소에 추가하거나, term-request 라벨이 붙은 GitHub 이슈를 처리할 때 사용한다. 정밀한 스펙·API 시그니처·엄밀한 정의를 원할 때는 쓰지 않는다.
---

# ELI5 — 그림책으로 설명하기

## 목적

어려운 걸 **틀리지 않게**, **그림으로** 쉽게 만든다. 글은 적게, 그림은 크게.
목표는 "그림만 넘겨봐도 무슨 얘긴지 알고, 읽고 나면 스스로 한 문장으로 다시 말할 수 있는 상태".

결과물은 이 저장소의 `terms/<분야>/<slug>.py` 한 파일이다. `python3 build.py` 가 한글·영문 HTML을 만든다.
설명을 채팅으로만 요청받았더라도, 저장소 안에서 작업 중이면 파일로 만든다 — 다음 사람이 다시 쓸 수 있어야 한다.

요청은 GitHub 이슈(`term-request` 라벨, 양식 `.github/ISSUE_TEMPLATE/term-request.yml`)로도 들어온다.
이슈에는 용어·분야·막힌 상황·참고 링크가 있다. 막힌 상황이 비유를 고르는 가장 좋은 단서다.
이슈를 처리했으면 커밋 메시지에 `Closes #번호` 를 넣는다.

## 절차

### 0. 분야를 정한다

분야는 `terms/` 아래 **폴더**다. `build.py` 의 `CATEGORIES` 에 등록된 것만 빌드된다.

| 폴더 | 분야 | 세계관 |
|---|---|---|
| `security` | 보안 | 성(castle) — 내 컴퓨터는 성, 공격자는 수상한 사람, 방어자는 망루 친구·경비실·경비견·복도 파수꾼 |
| `design` | 소프트웨어 설계 | 용어마다 고른다 (Dialog Map: 앱은 집, 화면은 방) |

맞는 분야가 없으면 폴더를 새로 만들고 `CATEGORIES` 에 `"폴더": ("한글", "English")` 한 줄을 추가한다.
분야 하나가 세계관 하나를 공유하면 페이지끼리 이어진다. 억지로 다른 분야의 세계에 끼워 넣지 않는다.

### 1. 비유를 하나 고른다

용어를 읽고, 다섯 살이 **직접 겪어본 세계**에서 비유를 하나만 고른다.
같은 분야에 이미 세계관이 있으면 그 안에서 푼다. 기존 캐릭터를 재사용하면 페이지끼리 이어진다.

| 분야 | 용어 | 비유 |
|---|---|---|
| security | CTI | 망루 위의 친구 |
| security | IOC | 남겨진 발자국 |
| security | TTP | 도둑의 버릇 |
| security | ATT&CK | 도둑 백과사전 |
| security | Pyramid of Pain | 고통의 피라미드 |
| security | TLP | 비밀 신호등 |
| security | SOC | 성의 경비실 |
| security | SIEM | 경비실의 큰 화면 |
| security | EDR | 방마다 한 마리 경비견 |
| security | XDR | 한 무리가 된 파수꾼들 |
| security | NDR | 복도를 지키는 사람 |
| security | Zero Trust | 문마다 물어보는 성 |
| security | OAuth | 열쇠 대신 입장권 |
| security | MFA | 세 번 확인하는 문지기 |
| security | SSO | 마을 통행증 |
| security | Passkey | 성문을 알아보는 반지 |
| security | RBAC | 모자마다 열쇠 꾸러미 |
| security | ABAC | 문지기의 조건 문장 |
| security | PAM | 금고 속 마스터 열쇠 |
| security | IAM | 성의 명부 관리소 |
| security | DLP | 빨간 도장 찍힌 종이 |
| security | CASB | 바깥 창고 문지기 |
| security | SWG | 마을로 나가는 성문 검문소 |
| security | ZTNA | 방 하나까지만 데려다주는 안내인 |
| security | SASE | 마을 곳곳의 역 |
| security | NAC | 복도 구멍마다 문지기 |
| security | WAF | 창구 앞 쪽지 검토원 |
| security | IDS / IPS | 수배 전단 든 파수꾼 |
| security | Firewall | 문이 많은 성벽 |
| security | VPN | 봉인된 땅굴 |
| security | Proxy | 대신 다녀오는 심부름꾼 |
| security | Load Balancer | 줄 안내원 |
| security | CDN | 마을마다 복사본 창고 |
| security | DNS | 마을 안내소 |
| security | DHCP | 번호표 나눠주는 창구 |
| security | VLAN | 색 리본으로 나눈 복도 |
| security | DDoS | 성문 앞 가짜 손님 떼 |
| security | Ransomware | 상자마다 채운 도둑의 자물쇠 |
| security | Phishing | 우체국인 척하는 편지 |
| security | Malware | 선물 상자 속 벌레 |
| security | Zero-day | 아무도 모르는 구멍 |
| security | Patch | 목수가 보낸 판자 |
| security | Backup | 멀리 둔 여분 상자 |
| design | Dialog Map | 방과 문의 지도 |

비유가 **깨지는 지점**을 반드시 패널 하나로 넣는다. 이게 정직한 설명과 거짓말의 차이다.
(발자국 → "신발을 바꾸면 발자국도 바뀌어요")

### 2. 패널 3~5장을 짠다

패널 하나 = 그림 한 장 + 한 문장 + (선택) 부연 한 줄. 순서는 이야기 순서다.

```
1. 무대       — 비유의 세계를 보여준다          "내 컴퓨터는 성이에요."
2. 문제       — 뭐가 곤란한가                   "수상한 사람들이 들어오려 해요."
3. 용어 등장  — 이 용어가 비유 속에서 뭔가 (hero) "CTI는 망루 위의 친구예요."
4. 작동       — 그래서 무슨 일이 일어나나        "친구가 수법을 미리 알려줘요."
5. 한계/결과  — 비유가 깨지는 곳, 또는 결말      "신발을 바꾸면 발자국도 바뀌어요."
```

짧은 용어면 3장. 길이는 이해도가 아니라 용어의 크기에 맞춘다.
문장은 **한 패널에 한 개념**. 부연(`small`)에도 두 문장을 넘기지 않는다.

### 3. 그림을 그린다

`terms/_draw.py` 의 조각을 먼저 쓴다. 새로 그리는 건 최소한으로.

| 조각 | 용도 |
|---|---|
| `person(x, y, hat, shirt, s, face, extra)` | 사람. 모자 색이 정체 — `var(--bad)` 나쁜 사람, `var(--good)` 친구, `hat=None` 모자 없음 |
| `SMILE` `FROWN` `EYES` `MASK` `SWEAT` | 얼굴·표정. `face=` 와 `extra=` 에 넣는다 |
| `castle()` `small_castle()` | 우리 성, 다른 성 |
| `sky(h)` `night(h)` | 낮 배경, 밤 배경 |
| `bubble(x, y, w, h, text, size, fill, stroke, tail)` | 말풍선 |
| `shield(x, y, s)` | 방어 |
| `foot(x, y, rot)` | 발자국 |
| `corridor(h, doors, night_mode, marks)` | 문 다섯 개짜리 복도 (NDR·Zero Trust 가 같이 씀) |
| `gate(x, y, s)` | 성문 (XDR·MFA 가 같이 씀) |
| `gatehouse(x, y, s)` | 길 위의 검문소 (CASB·SWG 가 같이 씀) |
| `dog(x, y, s, bark, asleep)` | 경비견 (EDR·XDR·NDR 이 같이 씀) |
| `label(x, y, text, size, fill, anchor, cls)` | 글자. `cls="d"` 면 제목 서체 |
| `icon(inner)` `dot_icon(color)` | 카드용 64×64 아이콘 |

규칙:
- viewBox 폭은 항상 760. 높이는 내용에 맞춘다 (170~380).
- 색은 CSS 토큰만 — `var(--bad)`, `var(--good)`, `var(--accent)`, `var(--sky)`, `var(--night)` … 다크 모드에서도 맞아야 한다. 실제 색이 의미인 경우(신호등, 피라미드 층)만 리터럴 허용.
- 그림 속 글자는 `⟦한글|영문⟧` 으로 적는다. 빌드가 언어별로 고른다.
- 요소가 겹치지 않는지 좌표를 한 번 더 본다. 특히 말풍선과 사람, 방패와 라벨.
- 자세한 손그림보다 단순한 도형. 다섯 살 그림책이다.

### 4. 파일을 쓴다

`terms/<분야>/<slug>.py` — 같은 분야의 기존 파일 하나를 복사해서 시작한다. 구조:

```python
from _draw import *

P1 = svg(300, sky(300) + castle() + ...)          # 패널 그림들
...

PAGE = {
    "slug": "ioc", "order": 2,                     # order 는 같은 분야 안에서의 순서 (목록·다음 이야기)
    "title": ("남겨진 발자국", "The Footprint"),    # 비유의 이름. 용어 이름이 아니다
    "h1": ("<em>IOC</em>가 뭐예요?", "What is an <em>IOC</em>?"),
    "sub": ("원어(영문 풀네임)를 … 이야기로 풀어봤어요.", "…, told as a story about …"),
    "panels": [
        {"svg": P1, "alt": (…), "caption": (…), "small": (…)},
        {"svg": P2, "alt": (…), "caption": (…), "small": (…),
         "tricks": (3, [(ICON, (b_ko, b_en), (s_ko, s_en), "warm"|"calm"), …])},  # 카드 2~4개
        {"svg": P3, "hero": True, …},               # 용어가 등장하는 패널 하나만 hero
        {"svg": P4, …, "bubbles": [((left_ko, left_en), (right_ko, right_en)), …]},
    ],
    "summary": ((h2_ko, h2_en), (p_ko, p_en)),      # 한 줄 요약. <b> 로 핵심어 강조
    "glossary": [(term_ko, term_en, (bold_ko, bold_en), (rest_ko, rest_en)), …],
}
```

- 모든 문장은 `(한글, 영문)` 튜플. 한쪽만 쓰지 않는다.
- `alt` 는 그림을 못 보는 사람에게 그림을 설명하는 문장이다. 캡션을 반복하지 않는다.
- `glossary` 는 **쉬운 말 → 원어** 대응표. 그림책에서 쓴 말(발자국)이 어른 말(IOC)로 무엇인지 잇는다. 나중에 검색할 수 있어야 한다. 4~6개.
- 관련 용어 페이지가 있으면 `small` 이나 `glossary` 에서 `<a href="<slug>-ko.html">` / `-en.html` 로 잇는다.
- `&` 는 `&amp;` 로 쓴다 (ATT&amp;CK).

### 5. 빌드하고 확인한다

```bash
python3 build.py
```

확인:
- 빌드가 통과했나 (SVG 가 XML 로 정상인가, 링크가 존재하는 파일을 가리키나 — 빌드가 검사한다)
- 브라우저에서 한글·영문 각 한 번씩 본다. 겹침, 잘린 글자, 빈 패널이 없나.
- `docs/*.html` 은 생성물이다. 직접 고치지 않는다.

## 문장 규칙

- 첫 패널의 캡션만 읽어도 무대가 보여야 한다. 배경 설명으로 시작하지 않는다.
- 한 문장 = 한 개념. 접속사로 이어 붙이지 않는다.
- 주어를 생략하지 않는다. **누가** 무엇을 하는지가 이해의 90%다.
- 숫자는 감각으로: "10분", "1초", "몇 달". 정확한 수치는 glossary 로.
- 전문 용어는 그림책 본문에 쓰지 않는다. glossary 에서만 원어를 만난다. 예외는 용어 자체(제목의 `<em>`).
- 말투는 "~예요/~해요". 어린이 흉내("자, 친구들~")는 쓰지 않는다. **어휘를 낮추는 것이지 상대를 낮추는 게 아니다.**

## 하지 말 것

| 금지 | 이유 |
|---|---|
| 비유 두 개 이상 섞기 | 어느 쪽을 믿어야 할지 모른다 |
| 비유가 깨지는 지점을 생략하기 | 틀린 단순화가 된다 |
| 그림 없이 글로만 채운 패널 | 그림책이 아니다. 그림이 안 떠오르면 비유가 틀린 것 |
| 한 패널에 문장 세 개 이상 | 글이 그림을 이긴다 |
| 리터럴 색상 (`#333`) | 다크 모드에서 깨진다 |
| 한 언어만 쓰기 | 두 언어가 같은 파일의 계약이다 |
| `docs/*.html` 직접 수정 | 다음 빌드에서 사라진다 |

## 점검 체크리스트

파일을 쓴 뒤 확인한다. 하나라도 ❌면 다시 쓴다.

- [ ] 그림만 순서대로 봐도 이야기가 이어지나?
- [ ] 비유가 하나이고, 깨지는 지점이 패널로 있나?
- [ ] 쉬워지려고 **틀린 말**을 하진 않았나? (수치·연도·이름은 실제 출처와 맞나)
- [ ] 본문에 설명 없이 등장한 전문 용어가 있나?
- [ ] glossary 를 보면 다음에 뭘 검색해야 할지 아나?
- [ ] 한글·영문 모두 채웠고, 빌드가 통과했나?
