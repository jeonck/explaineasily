# 보안 세계관: 내 컴퓨터(조직)는 성, 인터넷은 마을, 공격자는 도둑

## 무대
- 성 = 내 컴퓨터 / 우리 조직, 성벽 = 경계, 방 = 서버·계정, 복도 = 네트워크
- 마을 = 인터넷/외부, 빌린 창고 = 클라우드, 마을 안내소 = DNS, 장터 = 공개 시장, 나쁜 시장 = 다크웹
- 낮 `sky()` = 평상시, 밤 `night()` = 공격 중(달은 (660,50) r=26 — 그 자리 비우기), `bad-soft` 배경 = 문제 패널, `good-soft` = 해결/비교

## 등장인물 (모자/옷 색 = 정체)
| 인물 | 그림 | 실제 |
|---|---|---|
| 도둑 | `hat="var(--bad)"`, `face=MASK` (+BAG) | 공격자 |
| 고용한 도둑 | 도둑 차림 + 초록 완장 ARMBAND | 펜테스터 / 레드팀 |
| 경비 | `GUARD = hat/shirt var(--good)` | 방어자, 문지기, 파수꾼 |
| 파란 모자 | `BLUE = #5B8DEF` | 경비실(SOC) 친구, 블루팀, 관리소 |
| 목수 | 파란 모자 + `HAMMER` | 패치/개발자/엔지니어 |
| 왕 | `hat=#E9B44C, shirt=#7B3FA0` | 경영진/CEO |
| 서기 | `hat=var(--stone-dark), shirt=#4A5A72` | 관리자/사무 |
| 요리사·하녀·마을 사람 | 흰 옷 / 보라 옷 / 다양한 옷, `hat=None` | 일반 사용자, 외부인 |
| 망루 친구 | 초록 경비 + `SPYGLASS` | 위협 인텔(CTI) |
| 경비견 `dog()` | | EDR |

## 소품 = 개념
| 소품 | 실제 | 처음 쓴 페이지 |
|---|---|---|
| 열쇠 / 열쇠 꾸러미 | 인증 정보 / 권한·역할 | rbac, pam, leastprivilege |
| 암호말 | 비밀번호 | password |
| 입장권·통행증·팔찌 | 토큰·SSO·세션 | oauth, sso, session |
| 반지 | 패스키 | passkey |
| 종 | 경보·탐지 규칙 | soc, siem |
| 일지 | 로그 | log |
| 순서표 | 플레이북/IR 절차 | incident |
| 봉인 편지 | 암호화·TLS | encryption, tls |
| 지문 | 해시 | hashing |
| 왕의 도장 / 신분증 | 서명·인증서 | pki |
| 색 도장 | 데이터 분류 | classification |
| 빨간 도장 종이 | 민감 데이터 | dlp |
| 여분 상자 | 백업 | backup |
| 판자 | 패치 | patch |
| 틈 / 틈 장부 | 취약점 / 취약점 관리 | zeroday, vulnmgmt |
| 벌레 | 멀웨어 | malware |
| 도둑의 자물쇠 | 랜섬웨어 | ransomware |
| 가짜 편지 | 피싱 | phishing |
| 수배 전단 | 시그니처/차단 목록 | idsips |
| 리본으로 나눈 복도 | VLAN/세그먼트 | vlan |
| 땅굴 | VPN | vpn |
| 모래 방(창문 없는 빈 방) | 샌드박스 | sandbox |
| 가짜 금고 방 | 허니팟 | honeypot |
| 부품 목록표 | SBOM | sbom |
| 바깥 지도 | 공격 표면 | asm |
| 두루마리 | 정책 | policy |
| 검사관 | 감사/규정 | compliance |
| 저울 | 위험 평가 | risk |

## 이미 쓴 비유 (order 순)
| slug | 제목 |
|---|---|
| cti | 망루 위의 친구 |
| ioc | 남겨진 발자국 |
| ttp | 도둑의 버릇 |
| attack | 도둑 백과사전 |
| pyramid | 고통의 피라미드 |
| tlp | 비밀 신호등 |
| soc | 성의 경비실 |
| siem | 경비실의 큰 화면 |
| log | 성 곳곳의 한 줄 일지 |
| edr | 방마다 한 마리 경비견 |
| xdr | 한 무리가 된 파수꾼들 |
| ndr | 복도를 지키는 사람 |
| zerotrust | 문마다 물어보는 성 |
| oauth | 열쇠 대신 입장권 |
| mfa | 세 번 확인하는 문지기 |
| sso | 마을 통행증 |
| passkey | 성문을 알아보는 반지 |
| rbac | 모자마다 열쇠 꾸러미 |
| abac | 문지기의 조건 문장 |
| pam | 금고 속 마스터 열쇠 |
| iam | 성의 명부 관리소 |
| dlp | 빨간 도장 찍힌 종이 |
| casb | 바깥 창고 문지기 |
| swg | 마을로 나가는 성문 검문소 |
| ztna | 방 하나까지만 데려다주는 안내인 |
| sase | 마을 곳곳의 역 |
| nac | 복도 구멍마다 문지기 |
| waf | 창구 앞 쪽지 검토원 |
| idsips | 수배 전단 든 파수꾼 |
| firewall | 문이 많은 성벽 |
| vpn | 봉인된 땅굴 |
| proxy | 대신 다녀오는 심부름꾼 |
| loadbalancer | 줄 안내원 |
| cdn | 마을마다 복사본 창고 |
| dns | 마을 안내소 |
| dhcp | 번호표 나눠주는 창구 |
| vlan | 색 리본으로 나눈 복도 |
| ddos | 성문 앞 가짜 손님 떼 |
| ransomware | 상자마다 채운 도둑의 자물쇠 |
| phishing | 우체국인 척하는 편지 |
| malware | 선물 상자 속 벌레 |
| zeroday | 아무도 모르는 구멍 |
| patch | 목수가 보낸 판자 |
| backup | 멀리 둔 여분 상자 |
| encryption | 열쇠 없이는 못 읽는 편지 |
| hashing | 물건마다 찍는 지문 |
| honeypot | 반짝이는 가짜 금고 방 |
| sandbox | 창문 없는 빈 방 |
| sbom | 도구에 붙은 부품 목록표 |
| pentest | 우리가 고용한 도둑 |
| incident | 도둑 들었을 때 순서표 |
| hunting | 종을 기다리지 않는 파수꾼 |
| purpleteam | 같은 책상에 앉은 도둑과 파수꾼 |
| redteam | 진짜 도둑인 척하는 팀 |
| blueteam | 성을 지키는 파란 모자들 |
| bugbounty | 성문에 붙인 상금 방 |
| vulnmgmt | 매달 도는 틈 장부 |
| asm | 바깥에서 세는 우리 성의 문 |
| awareness | 성 사람 모두가 듣는 도둑 수업 |
| classification | 종이마다 찍는 색 도장 |
| retention | 종이마다 정해둔 태우는 날 |
| password | 문지기에게 속삭이는 암호말 |
| pki | 왕의 도장이 찍힌 신분증 |
| tls | 상점과 주고받는 봉인 약속 |
| leastprivilege | 딱 필요한 열쇠만 |
| mitm | 편지를 중간에서 뜯어보는 배달부 |
| bruteforce | 열쇠 천 개를 다 꽂아보는 도둑 |
| injection | 쪽지에 숨긴 명령 |
| botnet | 홀려서 조종당하는 마을 사람들 |
| apt | 몇 달을 기다리는 끈질긴 도둑 무리 |
| killchain | 도둑의 일곱 걸음 |
| insider | 안에서 문을 여는 사람 |
| supplychain | 목수의 연장통에 숨어 들어온 벌레 |
| risk | 어느 문부터 지킬지 정하는 저울 |
| compliance | 이웃 나라 규칙 검사관 |
| policy | 성의 규칙 두루마리 |
| drp | 성이 불타도 다음 날 장사하는 법 |
| devsecops | 짓는 동안 같이 보는 목수와 경비 |
| threatmodel | 짓기 전에 도둑 눈으로 보는 도면 |
| secrets | 열쇠를 벽에 못 박아 두지 않기 |
| codescan | 도면 검사와 두드려 보기 |
| soar | 경비실의 자동 순서표 기계 |
| forensics | 발자국을 굳혀서 보관하기 |
| masking | 이름 대신 번호표 |
| cspm | 빌린 창고 문단속 점검 |
| emailsec | 우체국 도장 세 개 |
| antivirus | 벌레 그림 카드를 든 경비 |
| ueba | 평소와 다른 걸음걸이 |
| spyware | 몰래 엿보고, 몰래 일 시키는 벌레들 |
| apisec | 창구 뒷문으로 오는 심부름꾼 |
| container | 똑같이 찍어낸 짐칸 |
| iotsec | 말 못 하는 성 안 기계들 |
| privacy | 손님 이름표는 손님 것 |
| session | 입장 팔찌를 훔치는 도둑 |
| aisec | 왕의 목소리를 흉내 내는 앵무새 |
| framework | 성 지키기 다섯 기둥 |
| metrics | 얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나 |
| airgap | 다리 없는 섬 창고 |
| hsm | 열쇠를 만드는 쇠금고 |
| allowlist | 명단에 있는 사람만 |
| cyberinsurance | 도둑 보험 |
| ciatriad | 지키는 것 세 가지: 못 보게, 못 바꾸게, 늘 쓰게 |
| defenseindepth | 겹겹이 두른 성벽 |
| dmz | 성벽과 성벽 사이의 마당 |
| hardening | 새 방을 쓰기 전에 하는 문단속 |
| mdm | 성 밖으로 들고 나가는 작은 상자 |
| wifi | 마을 광장의 공짜 우체통 |
| bec | 왕의 글씨체로 온 편지 |
| malwaretypes | 벌레 도감: 선물 벌레, 기어 다니는 벌레, 숨는 벌레, 뒷문 벌레 |
| activedirectory | 성의 명부와 열쇠를 한꺼번에 쥔 관리소 |
| csrf | 손님 팔찌를 빌려 몰래 보내는 쪽지 |
| osint | 마을 소문만 모아도 성 지도가 나와요 |
| physical | 성문을 잠가도 창문이 열려 있으면 |
