---
name: eli5
description: 어려운 용어·개념을 "다섯 살도 알 수 있게" 그림책 한 권으로 만드는 스킬. 큰 SVG 그림 한 장 + 한 문장 짜리 패널 3~5장, 한 줄 요약, 쉬운 말→원어 대응표로 구성된 한글·영문 HTML 페이지를 terms/<분야>/<slug>.py 로 작성하고 build.py 로 생성한다. 사용자가 "쉽게 설명해줘", "ELI5", "그림책으로 만들어줘", "다섯 살도 알게", "explain like I'm 5", "이 용어도 같은 형식으로" 라고 하거나, 새 용어를 이 저장소에 추가하거나, term-request 라벨이 붙은 GitHub 이슈를 처리할 때 사용한다. 정밀한 스펙·API 시그니처·엄밀한 정의를 원할 때는 쓰지 않는다.
---

# ELI5 — 그림책으로 설명하기

> 분야에 상관없이 쓰는 일반화 버전은 `.claude/skills/picture-book/` (세계관 설계 · 병렬 배치 루프 · 헤드리스 시각 검수 스크립트 포함). 이 문서는 보안 성(castle) 세계관의 구체 예시다. 세계관 카드는 `terms/security/_WORLD.md`.

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
| security | Log | 성 곳곳의 한 줄 일지 |
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
| security | Encryption | 열쇠 없이는 못 읽는 편지 |
| security | Hashing | 물건마다 찍는 지문 |
| security | Honeypot | 반짝이는 가짜 금고 방 |
| security | Sandbox | 창문 없는 빈 방 |
| security | SBOM | 도구에 붙은 부품 목록표 |
| security | Pentest | 우리가 고용한 도둑 |
| security | Incident Response | 도둑 들었을 때 순서표 |
| security | Threat Hunting | 종을 기다리지 않는 파수꾼 |
| security | Purple Team | 같은 책상에 앉은 도둑과 파수꾼 |
| security | Red Team | 진짜 도둑인 척하는 팀 |
| security | Blue Team | 성을 지키는 파란 모자들 |
| security | Bug Bounty | 성문에 붙인 상금 방 |
| security | Vulnerability Management | 매달 도는 틈 장부 |
| security | Attack Surface Management | 바깥에서 세는 우리 성의 문 |
| security | Security Awareness Training | 성 사람 모두가 듣는 도둑 수업 |
| security | Data Classification | 종이마다 찍는 색 도장 |
| security | Data Retention | 종이마다 정해둔 태우는 날 |
| security | Password | 문지기에게 속삭이는 암호말 |
| security | PKI | 왕의 도장이 찍힌 신분증 |
| security | TLS | 상점과 주고받는 봉인 약속 |
| security | Least Privilege | 딱 필요한 열쇠만 |
| security | Man-in-the-Middle Attack | 편지를 중간에서 뜯어보는 배달부 |
| security | Brute-Force Attack | 열쇠 천 개를 다 꽂아보는 도둑 |
| security | Injection Attack | 쪽지에 숨긴 명령 |
| security | Botnet | 홀려서 조종당하는 마을 사람들 |
| security | APT | 몇 달을 기다리는 끈질긴 도둑 무리 |
| security | Kill Chain | 도둑의 일곱 걸음 |
| security | Insider Threat | 안에서 문을 여는 사람 |
| security | Supply Chain Attack | 목수의 연장통에 숨어 들어온 벌레 |
| security | Risk Management | 어느 문부터 지킬지 정하는 저울 |
| security | Compliance | 이웃 나라 규칙 검사관 |
| security | Security Policy | 성의 규칙 두루마리 |
| security | Disaster Recovery | 성이 불타도 다음 날 장사하는 법 |
| security | DevSecOps | 짓는 동안 같이 보는 목수와 경비 |
| security | Threat Modeling | 짓기 전에 도둑 눈으로 보는 도면 |
| security | Secrets Management | 열쇠를 벽에 못 박아 두지 않기 |
| security | Code Scanning | 도면 검사와 두드려 보기 |
| security | SOAR | 경비실의 자동 순서표 기계 |
| security | Digital Forensics | 발자국을 굳혀서 보관하기 |
| security | Data Masking | 이름 대신 번호표 |
| security | Cloud Security | 빌린 창고 문단속 점검 |
| security | Email Security | 우체국 도장 세 개 |
| security | Antivirus | 벌레 그림 카드를 든 경비 |
| security | UEBA | 평소와 다른 걸음걸이 |
| security | Spyware | 몰래 엿보고, 몰래 일 시키는 벌레들 |
| security | API Security | 창구 뒷문으로 오는 심부름꾼 |
| security | Container Security | 똑같이 찍어낸 짐칸 |
| security | IoT / OT Security | 말 못 하는 성 안 기계들 |
| security | Privacy | 손님 이름표는 손님 것 |
| security | Session Hijacking | 입장 팔찌를 훔치는 도둑 |
| security | AI Security | 왕의 목소리를 흉내 내는 앵무새 |
| security | Security Framework | 성 지키기 다섯 기둥 |
| security | Security Metrics | 얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나 |
| security | Air Gap | 다리 없는 섬 창고 |
| security | HSM | 열쇠를 만드는 쇠금고 |
| security | Allowlist | 명단에 있는 사람만 |
| security | Cyber Insurance | 도둑 보험 |
| security | the CIA Triad | 지키는 것 세 가지: 못 보게, 못 바꾸게, 늘 쓰게 |
| security | Defense in Depth | 겹겹이 두른 성벽 |
| security | DMZ | 성벽과 성벽 사이의 마당 |
| security | Hardening | 새 방을 쓰기 전에 하는 문단속 |
| security | MDM and BYOD | 성 밖으로 들고 나가는 작은 상자 |
| security | Wi-Fi Security | 마을 광장의 공짜 우체통 |
| security | BEC, Smishing and Vishing | 왕의 글씨체로 온 편지 |
| security | Trojans, Worms, Rootkits and Backdoors | 벌레 도감: 선물 벌레, 기어 다니는 벌레, 숨는 벌레, 뒷문 벌레 |
| security | Active Directory | 성의 명부와 열쇠를 한꺼번에 쥔 관리소 |
| security | CSRF | 손님 팔찌를 빌려 몰래 보내는 쪽지 |
| security | OSINT | 마을 소문만 모아도 성 지도가 나와요 |
| security | Physical Security | 성문을 잠가도 창문이 열려 있으면 |
| design | Dialog Map | 방과 문의 지도 |
| ai | LLM | 책을 산더미로 읽은 앵무새 |
| ai | Token | 앵무새가 말을 콩으로 세요 |
| ai | Prompt | 앵무새에게 주는 조련 쪽지 |
| ai | Context Window | 앵무새 앞의 쟁반 |
| ai | Hallucination | 그럴듯 앵무새 |
| ai | Fine-tuning | 짧은 특훈 |
| ai | Embedding | 낱말마다 좌표 딱지 |
| ai | Vector DB | 딱지로 정리한 서가 |
| ai | RAG | 사서가 찾아온 페이지 |
| ai | Memory | 앵무새의 수첩 |
| ai | temperature | 엉뚱함 다이얼 |
| ai | prompt caching | 미리 놓아둔 콩 |
| ai | structured output | 정해진 칸에 쓰기 |
| ai | streaming | 콩을 하나씩 바로 보여주기 |
| ai | Tool Calling | 도구 상자 |
| ai | Agent | 심부름 목록을 스스로 짜는 앵무새 |
| ai | MCP | 도구 상자 규격 |
| ai | Multi-agent | 앵무새 회의 |
| ai | Guardrail | 울타리 |
| ai | Reasoning | 답하기 전 혼자 중얼거리기 |
| ai | Evaluation | 시험관의 채점표 |
| ai | Human-in-the-Loop | 마지막은 사람이 |
| ai | Multimodal | 그림도 보는 앵무새 |
| ai | Diffusion Model | 안개에서 그림 꺼내기 |
| ai | Code Generation | 코드 쓰는 앵무새 |
| ai | Workflow | 심부름 순서표 |
| ai | Distillation | 작은 앵무새에게 흉내 가르치기 |
| ai | Quantization | 콩을 굵게 세기 |
| ai | Inference | 앵무새가 답하는 값과 시간 |
| ai | Pricing | 콩 값 |
| ai | Attention | 앵무새의 눈길 |
| ai | Pre-training | 책 읽는 학교 |
| ai | Alignment | 앵무새 예절 교육 |
| ai | Knowledge Cutoff | 책을 덮은 날 |
| ai | Open Weights | 우리 집 앵무새 vs 빌린 앵무새 |
| ai | Routing | 어느 앵무새에게 시킬까 |
| ai | LLMOps | 앵무새 돌보기 |
| ai | Bias | 앵무새가 읽은 책의 치우침 |
| ai | AI Privacy | 앵무새에게 준 비밀 콩 |
| ai | Synthetic Data | 앵무새가 쓴 책으로 앵무새 가르치기 |

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
    "slug": "ioc", "order": 2,                     # order 는 같은 분야 안에서의 순서 (목록·다음 이야기). 사이에 끼울 땐 8.5 처럼 소수도 됨
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

| sre | SRE | 쉬지 않는 공원을 돌보는 사람들 |
| sre | SLI | 오늘 운행 기록판 |
| sre | SLO | 우리끼리 정한 목표 줄 |
| sre | SLA | 손님과 맺은 약속 계약서 |
| sre | Error Budget | 허용된 고장 티켓 묶음 |
| sre | Capacity Planning | 내년 손님 수를 미리 세어보기 |
| sre | API Gateway | 정문 안내소 |
| sre | Service Mesh | 기구 사이 전용 통로 |
| sre | Caching | 자주 묻는 질문 미리 적어둔 메모판 |
| sre | Sharding | 번호별로 나뉜 매표 창구 |
| sre | Replication | 손님 명부를 두 창고에 똑같이 |
| sre | Consensus | 여러 관제실이 손 들어 정하기 |
| sre | Split-Brain | 두 관제실이 서로 자기가 진짜라고 |
| sre | CAP Theorem | 정확함과 항상 열림, 둘 다는 못 가져요 |
| sre | Eventual Consistency | 조금 늦게 맞춰지는 재고판 |
| sre | Multi-region | 쌍둥이 공원 |
| sre | Infrastructure as Code | 설계도 한 장으로 공원 통째로 짓기 |
| sre | GitOps | 설계도가 바뀌면 자동으로 공사 |
| sre | Rate Limiting | 한 번에 몇 명까지만 |
| sre | Health Check | 안전바 딸깍 확인 |
| sre | Service Discovery | 지금 열린 창구 안내판 |
| sre | Orchestration | 몇 대를 켤지 정하는 운영 본부 |
| sre | Message Queue | 주문서를 쌓아두는 바구니 |
| sre | Dead-letter Queue | 아무도 안 찾아간 바구니함 |
| sre | Backpressure | 입구를 잠깐 막기 |
| sre | Bulkhead | 불이 안 번지게 나눈 구역 |
| sre | Circuit Breaker | 고장나면 누르는 빨간 버튼 |
| sre | Retry with Backoff | 잠깐 쉬었다 다시 줄서기 |
| sre | Idempotency | 같은 티켓으로 두 번 못 타요 |
| sre | Autoscaling | 줄이 길어지면 직원을 더 부르기 |
| sre | Graceful Degradation | 일부만 고장나도 나머지는 그대로 |
| sre | Failover | 발전기가 꺼지면 예비 발전기가 |
| sre | Feature Flag | 새 기구에 친 커튼 |
| sre | Canary Deployment | 구석에서 몰래 하는 시험 운행 |
| sre | Blue-Green Deployment | 쌍둥이 기구를 번갈아 운영 |
| sre | Rollback | 이상하면 바로 어제 버전으로 |
| sre | Golden Signals | 관제실의 계기판 네 개 |
| sre | Observability | 세 가지로 들여다보기 |
| sre | Alerting | 몇 번 울려야 진짜 비상인가 |
| sre | Chaos Engineering | 일부러 내는 가짜 고장 |
| sre | Game Day | 가짜 화재 훈련일 |
| sre | DORA Metrics | 우리 공사팀 네 가지 성적표 |
| sre | On-call | 이번 주 호출기를 든 사람 |
| sre | Incident Commander | 지휘봉을 든 사람 |
| sre | Runbook | 정비사의 공책 |
| sre | Postmortem | 탓하지 않고 모여 쓰는 기록 |
| sre | Toil | 매일 똑같이 반복하는 허드렛일 |

| llmsec | AI Security | 다 받아주는 주방 |
| llmsec | Prompt Injection | 주문서 뒤에 몰래 끼운 쪽지 |
| llmsec | Indirect Prompt Injection | 재료 포장지에 적힌 몰래 쪽지 |
| llmsec | Jailbreak | 주방장을 구슬려 규칙을 깨게 하기 |
| llmsec | Prompt Leak | 비밀 레시피 수칙을 캐내기 |
| llmsec | Prompt Filter Evasion | 암호처럼 꼬아 쓴 주문서 |
| llmsec | Image Prompt Injection | 메뉴판 사진 속에 숨긴 글자 |
| llmsec | Adversarial Example | 눈속임 그림 주문서 |
| llmsec | Model Extraction Attack | 레시피북 통째로 베껴가기 |
| llmsec | Model Inversion | 접시 더미에서 되살린 얼굴 |
| llmsec | Membership Inference | 눈 감고도 만드는 요리 |
| llmsec | Memorization | 그대로 베낀 접시 |
| llmsec | Data Poisoning | 수상한 재료 자루 |
| llmsec | RAG Poisoning | 참고 카드함에 끼운 가짜 카드 |
| llmsec | Backdoor | 숨겨진 암호 주문어 |
| llmsec | Trojan Model | 다듬는 중에 몰래 심은 버릇 |
| llmsec | Excessive Agency | 너무 많은 열쇠를 받은 견습생 |
| llmsec | Unsafe Output Handling | 접시를 그대로 기계에 넣다가 |
| llmsec | Zero-click Attack | 가만히 있어도 실행되는 공격 |
| llmsec | Tool Sandbox | 잠긴 칼 서랍 |
| llmsec | Per-tool Permission | 도구별 권한 배지 |
| llmsec | LLMDoS | 화구를 멈추지 않는 주문 |
| llmsec | AIBOM | 재료 출처 인증서 |
| llmsec | Model Card | 요리 설명표 |
| llmsec | Watermark | 요리에 새긴 표식 |
| llmsec | AI Red Team | 위생 검사관의 불시 방문 |
| llmsec | Safety Evaluation | 손님 받기 전 맛 평가 테스트 |
| llmsec | Human Approval Gate | 사장님 최종 승인 |
| llmsec | AI Governance | 주방 규칙판 |
| llmsec | Shadow AI | 몰래 들여온 배달 상자 |
| llmsec | AI Incident Response | 울리는 비상벨 |
| llmsec | AI Audit Log | 매일 적는 주문 기록 장부 |
| ppeswe | 정보시스템 감리/PMO | 출간 전 마지막 검수관 |
| ppeswe | ISP/ISMP | 출판 로드맵을 그리는 사람 |
| ppeswe | 요구공학/요구사항 명세 | 쓰기 전에 먼저 묻는 사람 |
| ppeswe | 애자일/스크럼 | 한 챕터씩 보여주며 쓰기 |
| ppeswe | 화이트박스/블랙박스 테스트 | 속을 펼쳐 볼지, 겉만 읽을지 |
| ppeswe | 데이터 품질관리 | 독자 주소록을 돌보는 일 |
| ppeswe | 소프트웨어 안전/기능안전 | 오탈자 하나의 무게가 다른 책 |
| ppeswe | 재공학/역공학(3R) | 사라진 원본을 되짚어 다시 짓기 |
| ppeswe | GoF 디자인패턴 | 검증된 글쓰기 공식집 |
| ppeswe | 마이크로서비스 아키텍처(MSA) | 두꺼운 책을 소책자들로 쪼개기 |
| ppeswe | UML 다이어그램 작성 | 쓰기 전에 그리는 설계 지도 |
| ppeswe | 기능점수(FP) | 매수를 재는 자 |
| ppeswe | 소프트웨어 형상관리(SCM) | 원고를 지키는 보관 서가 |
| ppeswe | MLOps/ModelOps | 자동 교정 기계 돌보기 |
| ppeswe | SW 사업 대가산정 | 매수를 돈으로 바꾸는 계산 |
| ppeswe | SW사업 영향평가 | 고치기 전에 그려보는 연결 지도 |
| ppeswe | 명세기반 테스트 설계기법 | 규칙서만 보고 고르는 대표 사례 |
| ppeswe | DevOps | 담장을 허문 작가와 인쇄소 |
| ppeswe | 개방형 API(Open API) | 서식 하나로 열어둔 열람실 |
| ppeswe | 캡슐화·정보은닉 | 작가의 잠긴 서랍 |
| ppeswe | SW 성능테스트 | 미리 몰려보는 가짜 독자들 |
| ppeswe | 통계적 가설검정 | 두 표지 중 뭐가 진짜 더 잘 팔릴까 |
| ppeswe | 리팩토링 | 줄거리는 그대로, 문장만 다시 다듬기 |
| ppeswe | 빅데이터 플랫폼 | 전국 창고 네트워크 |
| ppeswe | 메타모픽 테스트 | 정답 없이도 관계로 확인하기 |
| ppeswe | WBS | 책 만들기를 나뭇가지로 늘어놓기 |
| ppeswe | 기술부채 | 지금 빨리 가려고 쌓아둔 빚 |
| ppeswe | 개발방법론 테일러링 | 책마다 다른 편집 규칙 |
| ppeswe | 제품계열(Product Line) 방법론 | 같은 틀, 다른 표지 |
| ppeswe | 품질보증(QA)과 품질관리(QC) | 규칙을 지켰나, 책이 맞나 |
| ppeswe | 프로젝트 갈등관리 | 작가와 편집장이 다툴 때 |
| ppeswe | 좋은 소프트웨어 | 좋은 책의 조건 |
| ppeswe | 상용SW 직접구매 | 인쇄기를 중간상인 없이 바로 사기 |
| ppeswe | 결합도와 응집도 | 챕터가 서로 얼마나 엮여있나 |
| ppeswe | 아키텍처 평가(ATAM/CBAM) | 출간 전 시나리오 리허설 |
| ppeswe | SW 품질인증 | 책 표지의 공식 마크 |
| ppeswe | UNIX 시스템 | 기계실의 보이지 않는 운영자 |
| ppeswe | 디자인 씽킹 | 책상 추측 대신 독자에게 직접 묻기 |
| ppeswe | 의존성 주입/역전(DI/DIP) | 아무 기계나 꽂을 수 있는 콘센트 |
| ppeswe | 사용성평가(Usability) | 독자가 책을 쓱 넘겨보는 시험 |
| ppeswe | 소프트웨어 아키텍처 모델 | 책 전체를 미리 짜 두는 구조 밑그림 |
| ppedata | 정규화/반정규화 | 한 칸에 한 번만 적는 규칙 |
| ppedata | NoSQL 유형·모델링 | 상자 모양에 맞춰 선반을 바꾸는 창고 |
| ppedata | 데이터베이스 샤딩·파티셔닝 | 너무 커진 창고를 구역으로 쪼개기 |
| ppedata | 트랜잭션 격리 수준 | 동시에 손댈 때 얼마나 가려 볼지 정하는 규칙 |
| ppedata | LOD·오픈 데이터 | 문을 열고 번호표를 달아 연결해두는 창고 |
| ppedata | 트랜잭션과 ACID | 출납 전표가 지키는 네 가지 약속 |
| ppedata | 데이터베이스 병행제어 | 동시에 손대도 안 부딪히게 막는 규칙 |
| ppedata | 인메모리 컴퓨팅(In-Memory DB/IMDG) | 깊은 선반 대신 바로 꺼내는 특급 출고대 |
| ppedata | SCADA | 창고 전체를 한눈에 보는 관제실 |
| ppedata | 분산 데이터베이스 | 여러 지점으로 나뉜 창고 |
| ppedata | 다차원 색인구조 | 여러 딱지로 한 번에 찾기 |
| ppedata | 동적 SQL | 그 자리에서 맞춤 주문서 쓰기 |
| ppedata | RAID | 선반을 쪼개고 겹쳐서 쌓기 |
| ppedata | 데이터 웨어하우스 | 다듬어 둔 창고 vs 쌓아만 둔 야적장 |
| ppedata | OLAP | 전체를 썰어보는 창고 관리자 |
| ppedata | SDDC | 소프트웨어로 다시 짓는 창고 |
| ppeai | AI 학습용 데이터 품질관리 | 상한 씨앗으로 가르친 선별기 |
| ppeai | AI 윤리기준·거버넌스 | 모든 검사장이 함께 쓰는 등급 원칙판 |
| ppeai | 적대적 공격 | 작물에 몰래 붙인 가짜 점무늬 |
| ppeai | 혼동행렬 | 네 칸으로 나눈 도장 기록부 |
| ppeai | AI 리스크 관리 프레임워크 | 검사장 전체를 도는 운영 지도 |
| ppeai | 군집분석 | 이름표 없이 비슷한 것끼리 모으기 |
| ppeai | CNN(합성곱 신경망) | 작은 창으로 조금씩 살펴보는 눈 |
| ppeai | 로지스틱 회귀분석 | 저울 눈금을 S자 곡선에 넣어 보기 |
| ppeai | 이상치 | 무리에서 유난히 튀는 작물 |
| ppeai | 인공지능기본법·고영향 AI | 나라가 정한 최소 등급 기준 |
| ppeai | 피지컬 AI | 사진만 보던 눈이 팔다리를 얻다 |
| ppeai | AX(AI 전환) | 검사장 전체를 다시 설계하다 |
| ppeai | AI 개인정보보호 | 출하자 명부를 지키는 서류함 |
| ppeai | OWASP LLM 보안 위협 Top 10 | 검사장 입구의 업계 공용 위험 게시판 |
| ppeai | 시계열분석(AR/MA) | 지난 며칠을 보고 내일을 가늠하는 검수반장 |
| ppeai | AI 신뢰성 | 정확도 하나로는 못 받는 품질인증 등급판 |
| ppeai | AIaaS(AI as a Service) | 선별기를 사지 않고 구독하는 농가들 |
| ppeai | 온디바이스 AI | 창고 안에 직접 둔 작은 선별기 |
| ppeai | 불편추정량 | 치우치지 않은 저울눈금 |
| ppeai | 회귀모형 가정 | 저울을 똑바로 걸기 위한 네 가지 조건 |
| ppeai | 강화학습 | 정답표 없이 점수로 배우는 신입 조작원 |
| ppeai | 교차검증 | 조를 돌아가며 시험지로 쓰는 검수반장 |
| ppeai | 앙상블(Ensemble) 기법 | 세 조작원의 의견을 모아 결정하는 검사장 |
| ppenet | 5G 특화망 | 이 공장만을 위한 전용 배송망 |
| ppenet | TCP/UDP | 등기봉투와 일반봉투 |
| ppenet | SDN/NFV | 소프트웨어로 길을 바꾸는 관제탑 |
| ppenet | 무선충전기술 | 줄 없이 세우기만 하면 되는 충전판 |
| ppenet | 5G 네트워크 슬라이싱 | 한 도로를 차선으로 나누기 |
| ppenet | 다중접속·매체접근제어 | 하나의 통로를 안 부딪히고 나눠 쓰는 법 |
| ppenet | TCP 오류·흐름·혼잡 제어 | 등기 배송을 끝까지 지키는 세 장치 |
| ppenet | 동적 라우팅 프로토콜 | 스스로 고쳐 그리는 배송 지도 |
| ppenet | 인터럽트(네트워크 I/O) | 소포가 도착했다고 알리는 벨소리 |
| ppenet | 소켓 | 이 대화만을 위한 전용 우편함 구멍 |
| ppenet | 무선 측위 | 신호탑 세 개로 위치 찾기 |
| ppenet | IPv6 | 끝없이 늘어난 새 번지수 |
| ppenet | 5G 이동통신 핵심기술 | 상황별 전용 차선을 가진 배송망 |
| ppenet | 트래픽 폴리싱·쉐이핑 | 접수량을 조절하는 창구 규칙 |
| ppenet | 네트워크 서브네팅 | 동네를 작은 우편번호 구역으로 나누기 |
| ppenet | Modbus 프로토콜 | 우체국장이 순서대로 묻는 쪽지 규칙 |
| ppenet | IPC(네트워크 프로세스 간 통신) | 멀리 떨어진 건물 사이에 여는 전용 편지함 |
| ppenet | Ad-hoc 라우팅 프로토콜 | 집배원끼리 서로 길을 찾아 건네는 법 |
| ppenet | L4 스위치 | 창구 번호까지 보는 분류소 직원 |
| ppenet | AMI(지능형 검침 인프라) | 계량기가 스스로 편지를 보내는 망 |
| ppenet | V2X 차량 통신 | 트럭끼리 주고받는 쪽지 |
| ppenet | 회선교환·패킷교환 | 전용 도로냐, 조각내 보내기냐 |
| ppenet | OSI 7계층 | 7단계로 나뉜 배송 공정 |
| ppenet | 전송계층 | 포트를 나누고 신뢰도를 고르는 단계 |
| ppenet | SCTP | 한 계약, 여러 개의 전용 차선 |
| ppesec | ISMS/ISMS-P | 성 전체에 거는 인증 현판 |
| ppesec | 개인정보 비식별·가명처리 | 번호표로 바꿔 달고, 진짜 이름은 다른 금고에 |
| ppesec | 개인정보 안전성 확보조치·내부관리계획 | 손님 정보 창고의 전담 단속 수칙 |
| ppesec | 양자암호통신 | 엿들으면 바로 티 나는 빛 알갱이 열쇠 |
| ppesec | 블록체인 보안 고려사항 | 모두가 들고 다니는, 지문으로 이어 붙인 장부 |
| ppesec | CPU 보안 취약점(Meltdown/Spectre) | 미리 짐작해서 일하다 생긴 흔적 |
| ppesec | 국가 망 보안체계(N2SF) | 다리를 끊는 대신 검문소를 촘촘히 |
| ppesec | 개인정보 보호강화기술(PET) | 손님을 지키는 여러 다른 도구상자 |
| ppesec | 개인정보 안심구역 | 밖으로 못 들고 나가는 특별 열람실 |
| ppesec | 동형암호 | 뜯지 않고 셈하는 봉인 편지 |
| ppesec | 접근통제 모델 | 열쇠 주인을 정하는 세 가지 방식 |
| ppesec | CBPR | 여러 나라가 같이 인정하는 통행 증명 |
| ppesec | 마이데이터 | 내 장부는 내가 들고 다닐 권리 |
| ppesec | CSAP | 빌린 창고에 찍는 왕의 안전 도장 |
| ppesec | MAC/HMAC | 비밀 도장틀로 찍는 확인 도장 |
| ppesec | BLP/Biba | 비밀은 안 새게, 거짓은 안 섞이게 — 사다리 두 규칙 |
| ppesec | 공인인증서·사설인증 | 하나뿐이던 도장집, 이제는 여럿 |
| ppesec | 데이터 3법 개정 | 세 권의 규칙서를 한 검사관 아래로 |
| ppesec | PPDM | 이름은 가리고, 흐름은 보는 통계 조사관 |
| ppesys | CPU 스케줄링 | 리프트에 누가 먼저 올라갈까 |
| ppesys | 프로세스 동기화 | 리프트 열쇠는 하나뿐 |
| ppesys | 캐시 메모리 | 바로 옆에 놓아둔 공구함 |
| ppesys | 가상메모리·페이징 | 창고 전체를 내 것처럼 보여주는 가짜 지도 |
| ppesys | 교착상태와 기아현상 | 서로의 열쇠를 기다리며 멈춘 정비공장 |
| ppesys | GPU/GPGPU | 수백 명이 함께 움직이는 보조 정비팀 |
| ppesys | 스택과 큐 | 상자는 쌓고, 차는 줄 세우고 |
| ppesys | AI 가속기(TPU·NPU) | 오직 그 계산 하나만을 위한 전용 로봇팔 |
| ppesys | 프로세스와 스레드 | 같은 차, 여러 손 |
| ppesys | 이진트리·이진탐색트리 | 갈림길에서 반씩 줄여가는 선반 지도 |
| ppesys | 알고리즘 복잡도(Big-O) | 차가 많아질 때 얼마나 느려질까 |
| ppesys | 정렬 알고리즘 | 크기 순서로 차를 세우는 여러 방법 |
| ppesys | 플래시 메모리 | 전원이 꺼져도 기억하는 부품 창고 |
| ppesys | 인터럽트 처리 과정 | 벨이 울리면 적어두고 바로 달려가기 |
| ppesys | BPR(업무 프로세스 재설계) | 정비 공정을 처음부터 다시 그리는 일 |
| ppesys | HBM(고대역폭 메모리) | 엔진 바로 옆에 쌓은 공구탑 |
| ppesys | 프로세스 메모리 구조 | 작업 공간을 구역으로 나눠 쓰는 규칙 |
| ppesys | 유전 알고리즘 | 잘 나가는 다이얼 설정끼리 섞어보기 |
| ppesys | CPU 파이프라인 | 여러 작업대에서 동시에 겹쳐 고치기 |
| ppesys | 해시 알고리즘 | 번호만 계산해서 바로 칸을 짚기 |
| ppesys | 차세대 비휘발성 메모리 | 지우지 않고 바로바로 바꿔 쓰는 새 창고들 |
| ppesys | 최소신장트리(MST) | 가장 싼 배관만 골라 모든 지점 잇기 |
| ppesys | 플래시 변환계층(FTL) | 덮어쓰지 않는 부품 창고 관리인 |
| ppesys | 우선순위 역전/상속 | 급한 차가 유령처럼 멈춰요 |
| ppecloud | 클라우드 서비스 모델 | 뼈대만, 인테리어까지, 완제품 — 셋 중 골라 빌리기 |
| ppecloud | 가상머신(VM)과 컨테이너 | 독채 사무실과 칸막이 책상 |
| ppecloud | 공공부문 클라우드 활용 | 검증된 건물에만, 등급에 맞춰 입주하기 |
| ppecloud | 서버리스 컴퓨팅 | 쓸 때만 여는 시간제 회의실 |
| ppecloud | 엣지·포그 컴퓨팅 | 동네 가까운 지점과 그 사이 중간 허브 |
| ppecloud | SVM(서포트벡터머신) | 두 그룹을 가장 넓게 갈라놓는 선 |
| ppecloud | DAS/NAS/SAN | 내 서랍, 공용 자료실, 전용 창고망 |
| ppecloud | AI 데이터센터 | GPU만을 위한 전용 별관 |
| ppecloud | 블록·파일·오브젝트 스토리지 | 벽돌, 폴더 트리, 태그 붙은 박스 |
| ppecloud | 쿠버네티스(Kubernetes) | 자동 배정 배지의 그 유명한 제품 이름 |
| ppecloud | 멀티클라우드 | 여러 건물에 동시에 입주하기 |
| ppecloud | 스케일업/스케일아웃과 오토스케일 | 사무실을 키울까, 더 빌릴까 |
| ppetech | 디지털 트윈 | 화면 속 쌍둥이 로봇 |
| ppetech | 엣지 컴퓨팅 | 바로 옆에서 계산하는 작은 서버 |
| ppetech | 스마트팩토리 | 스스로를 지켜보는 공장 |
| ppetech | 퍼블릭·프라이빗 블록체인 | 펼친 장부와 자물쇠 장부 |
| ppetech | 블록체인 기술요소·보안 | 지문으로 이어진 장부 |
| ppetech | 스마트시티 | 함께 숨 쉬는 도시 모형 |
| ppetech | 메타버스 | 아바타들이 모인 가상 전시관 |
| ppetech | 가상현실(VR) | 눈앞 전체를 바꾸는 헤드셋 |
| ppetech | 모바일 엣지 컴퓨팅(MEC) | 기지국 옆에 붙은 작은 서버 |
| ppetech | 오류 제어(ARQ) | 틀렸으니 다시 보내달라고 외치기 |
| ppetech | 마이데이터(MyData) | 흩어진 서랍을 내가 한곳에 모으기 |
| ppetech | 안티드론 | 하늘의 불청객을 찾아 막는 삼단계 |
| ppetech | 양자키분배(QKD) | 엿보면 반드시 들통나는 빛의 열쇠 |
| ppetech | 앰비언트 컴퓨팅 | 말 안 해도 알아서 척척인 전시관 |
| ppetech | RPA | 규칙대로만 반복하는 로봇 직원 |
| ppetech | 드론 보안위협 | 보이지 않는 줄로 매달린 드론 |
| ppetech | 스마트팜 | 센서가 돌보는 온실 부스 |
| ppetech | 양자 컴퓨팅 | 동시에 앞뒤인 신기한 동전 부스 |
| ppetech | NFT | 그림에 붙이는 위조 못 하는 증명서 |
| ppetech | LiDAR | 레이저로 거리를 재는 회전하는 눈 |
| ppetech | 정량적 위험분석 기법 | 위험을 숫자 하나로 적는 전광판 |
| ppetech | 자율주행 | 운전석이 비어 있는 시연 트랙의 차 |
| ppetech | 사이버물리시스템(CPS) | 화면 속 쌍둥이와 함께 움직이는 기계팔 |
| ppetech | 4차 산업혁명 | 전시장 모든 부스를 잇는 하나의 흐름 |
| ppetech | 핀테크·간편결제 | 나가는 길, 폰 하나로 찍는 매표소 |
| ppepm | IT 투자성과 평가 | 공연 끝난 뒤의 성적표 |
| ppepm | 프로젝트 위험관리 | 비 오는 날에도 챙기는 우산 |
| ppepm | SLA/SLM | 공연을 보장하는 티켓 |
| ppepm | 협상에 의한 계약·제안서 평가 | 조건을 조율해 서명하기 |
| ppepm | ESG 경영과 IT | 환경·사회·투명성까지 챙기는 투어 |
| ppepm | BCP(업무 연속성 계획) | 정전에도 멈추지 않는 투어 |
| ppepm | WBS(작업분류체계) | 공연 준비를 쪼갠 체크리스트 |
| ppepm | 정보시스템 운영 성과관리 | 공연 끝난 뒤의 운영실 |
| ppelaw | 오픈소스 라이선스 | 다 같이 쓰는 준비물 규칙 라벨 |
| ppelaw | 정보시스템 하드웨어 규모산정 | 축제 준비물 개수 미리 정하기 |
| ppelaw | 망중립성 | 급식 줄은 다 똑같이 서야 해요 |
| ppelaw | ISO/IEC 25000(SQuaRE) | 좋은 준비물의 기준표 |
| ppelaw | 맨체스터 부호화 | 박자를 스스로 알려주는 신호 |
| ppelaw | ISO/IEC 42001 | AI도 규칙대로 쓰는지 도장 찍기 |
| ppelaw | 공공데이터 제공과 품질 | 공지 게시판에 다 보이게 붙이기 |
| ppelaw | 관계 무결성 제약 | 출석부에 없는 이름은 반장이 될 수 없어요 |
| ppelaw | AI 윤리·법적 이슈 | AI가 사고 치면 누가 책임져요? |
| ppelaw | 슈퍼앱 | 학생증 하나로 다 되는 앱 |
| ppelaw | 데이터 표준화 | 전교가 함께 쓰는 공통 기준표 |
| ppelaw | 위험·안전성 분석(FTA/FMEA/HAZOP) | 사고를 거꾸로, 또는 미리 훑어보기 |
| ppelaw | 지능정보화 기본법 | 학교 전체의 디지털 생활을 아우르는 기본 헌장 |
| ppelaw | 페이징·세그멘테이션 | 창고를 나누는 두 가지 다른 방식 |
| ppelaw | 디지털 증거수집의 법적 절차 | 정당하게 거뒀는가를 따지는 절차 |
| ppelaw | UN 전자정부 평가(EGDI) | 같은 잣대로 모든 학교를 재는 평가단 |
| ppelaw | 기능안전 표준(ISO 26262·IEC 61508) | 안전 등급을 매기는 공통 규칙서 |
| ppelaw | 경사하강법 | 안개 낀 산을 한 걸음씩 내려가기 |
| ppelaw | 분할정복·탐욕법·동적계획법 | 쪼개고, 급한 것부터, 기억해두고 |
| ppelaw | 레그테크(RegTech) | 흩어진 규칙판을 한꺼번에 대조하는 자동 검사기 |
