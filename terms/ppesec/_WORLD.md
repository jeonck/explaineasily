# PPE·정보보안 세계관: 성(城) — 기존 `security` 분야와 세계관을 공유

## 무대
- 이 분야는 **새 세계관을 만들지 않는다**. 이미 있는 `security`(보안) 분야의 성(城) 세계관을 그대로 쓴다 — 내 컴퓨터/조직 = 성, 인터넷 = 마을, 공격자 = 도둑, 방어자 = 경비.
- 전체 등장인물·소품·배경 규칙은 `terms/security/_WORLD.md` 를 그대로 따른다. **이 폴더에는 `_world.py` 가 없다** — `security` 분야도 별도 `_world.py` 없이 `terms/_draw.py` 의 `castle()`, `person()`, `dog()`, `corridor()`, `gate()`, `gatehouse()`, `shield()` 를 직접 쓴다. 이 분야도 똑같이 `from _draw import *` 만 쓰고, 역할별 색 dict(`ME = dict(hat=..., shirt=...)` 등)는 각 페이지 안에서 바로 정의한다 — `security` 폴더의 아무 페이지나 열어 그 패턴을 그대로 베낀다.
- 이 분야를 **별도 탭(PPE·정보보안)으로 분리한 이유**는 세계관이 달라서가 아니라, 시험(정보관리기술사/컴퓨터시스템응용기술사) 출제 범위 중 `security` 분야에 아직 없는 더 심화된 항목(ISMS-P, 제로트러스트, 양자암호, FIDO, CPU 보안취약점 등)을 시험 맥락으로 모아 보여주기 위함이다.
- **중복 금지**: 이미 `security` 분야에 있는 용어(VPN, DNS, 포렌식, 랜섬웨어, IDS/IPS, SIEM, SOAR, WAF, SBOM 등)는 여기서 다시 쓰지 않고 해당 페이지로 링크만 한다. 새로 쓰는 페이지는 `security` 에 없는, 시험에만 나오는 심화 항목이다.

## 이미 쓴 비유 (order 순)
| slug | 제목 |
|---|---|
| ismsp | 성 전체에 거는 인증 현판 |
| pseudonymize | 번호표로 바꿔 달고, 진짜 이름은 다른 금고에 |
| privacysafeguard | 손님 정보 창고의 전담 단속 수칙 |
| qkdcomm | 엿들으면 바로 티 나는 빛 알갱이 열쇠 |
| bcsecurity | 모두가 들고 다니는, 지문으로 이어 붙인 장부 |
| cpuvuln | 미리 짐작해서 일하다 생긴 흔적 |
| n2sf | 다리를 끊는 대신 검문소를 촘촘히 |
| pet | 손님을 지키는 여러 다른 도구상자 |
| safezone | 밖으로 못 들고 나가는 특별 열람실 |
| homoenc | 뜯지 않고 셈하는 봉인 편지 |
| accesscontrolppe | 열쇠 주인을 정하는 세 가지 방식 |
| cbpr | 여러 나라가 같이 인정하는 통행 증명 |
| mydataSec | 내 장부는 내가 들고 다닐 권리 |
| csap | 빌린 창고에 찍는 왕의 안전 도장 |
| machmac | 비밀 도장틀로 찍는 확인 도장 |
| blpbiba | 비밀은 안 새게, 거짓은 안 섞이게 — 사다리 두 규칙 |
| pkicert | 하나뿐이던 도장집, 이제는 여럿 |
| data3law | 세 권의 규칙서를 한 검사관 아래로 |
| ppdm | 이름은 가리고, 흐름은 보는 통계 조사관 |
