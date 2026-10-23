# explaineasily

어려운 용어를 **그림책**으로. 글은 적게, 그림은 크게, 다섯 살 눈높이로.

배포: https://explaineasily.metacog.co.kr (GitHub Pages, `main` 브랜치의 `/docs` 폴더, `docs/CNAME`)

## 소개

보안·AI·SRE 같은 분야의 전문 용어를, SVG 그림 다섯 장짜리 그림책 한 권으로 풀어 설명하는 사이트다.
한 페이지는 이야기 흐름을 따른다 — 문제 상황 → 왜 어려운가 → **이 용어가 비유 속에서 뭔가(히어로 패널 + 요령 카드 4개)** → 작동 디테일 → 결과·한계. 한글·영문을 한 파일에 같이 적어 두 언어로 동시에 나온다.

핵심은 **분야 하나 = 세계관 하나**라는 점이다. 같은 분야의 용어는 전부 같은 비유 세계를 공유해서, 한 번 익힌 그림이 다음 페이지에서도 그대로 쓰인다.

| 분야 | 세계관 | 용어 수 |
|---|---|---|
| 보안 | 내 컴퓨터는 성, 공격자는 도둑, 방어자는 망루 친구·경비실·경비견 | 113 |
| AI | 책을 산더미로 읽고 다음 말을 이어 붙이는 앵무새 | 40 |
| SRE | 하루도 안 닫는 놀이공원 — 놀이기구는 서비스, 손님은 요청 | 47 |
| AI 보안 | 뭐든 시키는 대로 믿고 따르는 주방장과, 그 주방을 노리는 사람들 | 32 |
| 소프트웨어 설계 | 앱은 집, 화면은 방, 화면 사이 이동은 문과 복도 | 1 |
| PPE·SW공학 | 원고를 쓰고 교정하고 찍어내는 출판사 | 40 |
| PPE·DB/데이터 | 재고를 나눠 보관하는 물류창고 | 16 |
| PPE·AI이론 | 작물을 등급별로 가려내는 품질검사장 | 23 |
| PPE·네트워크 | 집집마다 봉투를 나르는 우체국 배송망 | 25 |
| PPE·정보보안 | 보안 분야와 세계관을 공유하는 심화 성(城) | 19 |
| PPE·시스템SW | 리프트 한 대를 돌려쓰는 자동차 정비공장 | 25 |
| PPE·클라우드 | 사무실을 빌려 쓰는 공유 오피스 빌딩 | 12 |
| PPE·신기술 | 부스마다 다른 기술을 보여주는 과학관 전시장 | 25 |
| PPE·IT관리 | 공연을 준비하는 콘서트 투어 기획사 | 8 |
| PPE·법제도 | 학교 규칙을 정하는 학생회 | 20 |

총 446개 용어가 올라와 있다. 새 용어는 [용어 요청](#용어-요청)으로, 새 분야는 `.claude/skills/picture-book/`(세계관 설계·대량 작성 루프·시각 검수 스크립트를 담은 일반화 스킬)로 연다.

## 용어 요청

그림책으로 보고 싶은 용어가 있으면 이슈로 남겨주세요. 사이트 각 페이지 맨 아래의 "요청하기"도 같은 곳으로 갑니다.

→ [요청하기](https://github.com/jeonck/explaineasily/issues/new?template=term-request.yml)

이슈에 `term-request` 라벨이 붙으면(양식이 자동으로 붙임) GitHub Actions 가 Claude Code 로 페이지를 만들어 `term/<slug>` 브랜치에 PR 을 엽니다.
PR 을 확인하고 머지하면 배포됩니다. 워크플로: [`.github/workflows/term-request.yml`](.github/workflows/term-request.yml), 시크릿: `CLAUDE_CODE_OAUTH_TOKEN`.

## 문서

### 보안

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| CTI | 망루 위의 친구 | [cti-ko](docs/cti-ko.html) | [cti-en](docs/cti-en.html) |
| IOC | 남겨진 발자국 | [ioc-ko](docs/ioc-ko.html) | [ioc-en](docs/ioc-en.html) |
| TTP | 도둑의 버릇 | [ttp-ko](docs/ttp-ko.html) | [ttp-en](docs/ttp-en.html) |
| MITRE ATT&CK | 도둑 백과사전 | [attack-ko](docs/attack-ko.html) | [attack-en](docs/attack-en.html) |
| Pyramid of Pain | 고통의 피라미드 | [pyramid-ko](docs/pyramid-ko.html) | [pyramid-en](docs/pyramid-en.html) |
| TLP | 비밀 신호등 | [tlp-ko](docs/tlp-ko.html) | [tlp-en](docs/tlp-en.html) |
| SOC | 성의 경비실 | [soc-ko](docs/soc-ko.html) | [soc-en](docs/soc-en.html) |
| SIEM | 경비실의 큰 화면 | [siem-ko](docs/siem-ko.html) | [siem-en](docs/siem-en.html) |
| Log | 성 곳곳의 한 줄 일지 | [log-ko](docs/log-ko.html) | [log-en](docs/log-en.html) |
| EDR | 방마다 한 마리 경비견 | [edr-ko](docs/edr-ko.html) | [edr-en](docs/edr-en.html) |
| XDR | 한 무리가 된 파수꾼들 | [xdr-ko](docs/xdr-ko.html) | [xdr-en](docs/xdr-en.html) |
| NDR | 복도를 지키는 사람 | [ndr-ko](docs/ndr-ko.html) | [ndr-en](docs/ndr-en.html) |
| Zero Trust | 문마다 물어보는 성 | [zerotrust-ko](docs/zerotrust-ko.html) | [zerotrust-en](docs/zerotrust-en.html) |
| OAuth | 열쇠 대신 입장권 | [oauth-ko](docs/oauth-ko.html) | [oauth-en](docs/oauth-en.html) |
| MFA | 세 번 확인하는 문지기 | [mfa-ko](docs/mfa-ko.html) | [mfa-en](docs/mfa-en.html) |
| SSO | 마을 통행증 | [sso-ko](docs/sso-ko.html) | [sso-en](docs/sso-en.html) |
| Passkey | 성문을 알아보는 반지 | [passkey-ko](docs/passkey-ko.html) | [passkey-en](docs/passkey-en.html) |
| RBAC | 모자마다 열쇠 꾸러미 | [rbac-ko](docs/rbac-ko.html) | [rbac-en](docs/rbac-en.html) |
| ABAC | 문지기의 조건 문장 | [abac-ko](docs/abac-ko.html) | [abac-en](docs/abac-en.html) |
| PAM | 금고 속 마스터 열쇠 | [pam-ko](docs/pam-ko.html) | [pam-en](docs/pam-en.html) |
| IAM | 성의 명부 관리소 | [iam-ko](docs/iam-ko.html) | [iam-en](docs/iam-en.html) |
| DLP | 빨간 도장 찍힌 종이 | [dlp-ko](docs/dlp-ko.html) | [dlp-en](docs/dlp-en.html) |
| CASB | 바깥 창고 문지기 | [casb-ko](docs/casb-ko.html) | [casb-en](docs/casb-en.html) |
| SWG | 마을로 나가는 성문 검문소 | [swg-ko](docs/swg-ko.html) | [swg-en](docs/swg-en.html) |
| ZTNA | 방 하나까지만 데려다주는 안내인 | [ztna-ko](docs/ztna-ko.html) | [ztna-en](docs/ztna-en.html) |
| SASE | 마을 곳곳의 역 | [sase-ko](docs/sase-ko.html) | [sase-en](docs/sase-en.html) |
| NAC | 복도 구멍마다 문지기 | [nac-ko](docs/nac-ko.html) | [nac-en](docs/nac-en.html) |
| WAF | 창구 앞 쪽지 검토원 | [waf-ko](docs/waf-ko.html) | [waf-en](docs/waf-en.html) |
| IDS / IPS | 수배 전단 든 파수꾼 | [idsips-ko](docs/idsips-ko.html) | [idsips-en](docs/idsips-en.html) |
| Firewall | 문이 많은 성벽 | [firewall-ko](docs/firewall-ko.html) | [firewall-en](docs/firewall-en.html) |
| VPN | 봉인된 땅굴 | [vpn-ko](docs/vpn-ko.html) | [vpn-en](docs/vpn-en.html) |
| Proxy | 대신 다녀오는 심부름꾼 | [proxy-ko](docs/proxy-ko.html) | [proxy-en](docs/proxy-en.html) |
| Load Balancer | 줄 안내원 | [loadbalancer-ko](docs/loadbalancer-ko.html) | [loadbalancer-en](docs/loadbalancer-en.html) |
| CDN | 마을마다 복사본 창고 | [cdn-ko](docs/cdn-ko.html) | [cdn-en](docs/cdn-en.html) |
| DNS | 마을 안내소 | [dns-ko](docs/dns-ko.html) | [dns-en](docs/dns-en.html) |
| DHCP | 번호표 나눠주는 창구 | [dhcp-ko](docs/dhcp-ko.html) | [dhcp-en](docs/dhcp-en.html) |
| VLAN | 색 리본으로 나눈 복도 | [vlan-ko](docs/vlan-ko.html) | [vlan-en](docs/vlan-en.html) |
| DDoS | 성문 앞 가짜 손님 떼 | [ddos-ko](docs/ddos-ko.html) | [ddos-en](docs/ddos-en.html) |
| Ransomware | 상자마다 채운 도둑의 자물쇠 | [ransomware-ko](docs/ransomware-ko.html) | [ransomware-en](docs/ransomware-en.html) |
| Phishing | 우체국인 척하는 편지 | [phishing-ko](docs/phishing-ko.html) | [phishing-en](docs/phishing-en.html) |
| Malware | 선물 상자 속 벌레 | [malware-ko](docs/malware-ko.html) | [malware-en](docs/malware-en.html) |
| Zero-day | 아무도 모르는 구멍 | [zeroday-ko](docs/zeroday-ko.html) | [zeroday-en](docs/zeroday-en.html) |
| Patch | 목수가 보낸 판자 | [patch-ko](docs/patch-ko.html) | [patch-en](docs/patch-en.html) |
| Backup | 멀리 둔 여분 상자 | [backup-ko](docs/backup-ko.html) | [backup-en](docs/backup-en.html) |
| Encryption | 열쇠 없이는 못 읽는 편지 | [encryption-ko](docs/encryption-ko.html) | [encryption-en](docs/encryption-en.html) |
| Hashing | 물건마다 찍는 지문 | [hashing-ko](docs/hashing-ko.html) | [hashing-en](docs/hashing-en.html) |
| Honeypot | 반짝이는 가짜 금고 방 | [honeypot-ko](docs/honeypot-ko.html) | [honeypot-en](docs/honeypot-en.html) |
| Sandbox | 창문 없는 빈 방 | [sandbox-ko](docs/sandbox-ko.html) | [sandbox-en](docs/sandbox-en.html) |
| SBOM | 도구에 붙은 부품 목록표 | [sbom-ko](docs/sbom-ko.html) | [sbom-en](docs/sbom-en.html) |
| Pentest | 우리가 고용한 도둑 | [pentest-ko](docs/pentest-ko.html) | [pentest-en](docs/pentest-en.html) |
| Incident Response | 도둑 들었을 때 순서표 | [incident-ko](docs/incident-ko.html) | [incident-en](docs/incident-en.html) |
| Threat Hunting | 종을 기다리지 않는 파수꾼 | [hunting-ko](docs/hunting-ko.html) | [hunting-en](docs/hunting-en.html) |
| Purple Team | 같은 책상에 앉은 도둑과 파수꾼 | [purpleteam-ko](docs/purpleteam-ko.html) | [purpleteam-en](docs/purpleteam-en.html) |
| Red Team | 진짜 도둑인 척하는 팀 | [redteam-ko](docs/redteam-ko.html) | [redteam-en](docs/redteam-en.html) |
| Blue Team | 성을 지키는 파란 모자들 | [blueteam-ko](docs/blueteam-ko.html) | [blueteam-en](docs/blueteam-en.html) |
| Bug Bounty | 성문에 붙인 상금 방 | [bugbounty-ko](docs/bugbounty-ko.html) | [bugbounty-en](docs/bugbounty-en.html) |
| Vulnerability Management | 매달 도는 틈 장부 | [vulnmgmt-ko](docs/vulnmgmt-ko.html) | [vulnmgmt-en](docs/vulnmgmt-en.html) |
| Attack Surface Management | 바깥에서 세는 우리 성의 문 | [asm-ko](docs/asm-ko.html) | [asm-en](docs/asm-en.html) |
| Security Awareness Training | 성 사람 모두가 듣는 도둑 수업 | [awareness-ko](docs/awareness-ko.html) | [awareness-en](docs/awareness-en.html) |
| Data Classification | 종이마다 찍는 색 도장 | [classification-ko](docs/classification-ko.html) | [classification-en](docs/classification-en.html) |
| Data Retention | 종이마다 정해둔 태우는 날 | [retention-ko](docs/retention-ko.html) | [retention-en](docs/retention-en.html) |
| Password | 문지기에게 속삭이는 암호말 | [password-ko](docs/password-ko.html) | [password-en](docs/password-en.html) |
| PKI | 왕의 도장이 찍힌 신분증 | [pki-ko](docs/pki-ko.html) | [pki-en](docs/pki-en.html) |
| TLS | 상점과 주고받는 봉인 약속 | [tls-ko](docs/tls-ko.html) | [tls-en](docs/tls-en.html) |
| Least Privilege | 딱 필요한 열쇠만 | [leastprivilege-ko](docs/leastprivilege-ko.html) | [leastprivilege-en](docs/leastprivilege-en.html) |
| Man-in-the-Middle Attack | 편지를 중간에서 뜯어보는 배달부 | [mitm-ko](docs/mitm-ko.html) | [mitm-en](docs/mitm-en.html) |
| Brute-Force Attack | 열쇠 천 개를 다 꽂아보는 도둑 | [bruteforce-ko](docs/bruteforce-ko.html) | [bruteforce-en](docs/bruteforce-en.html) |
| Injection Attack | 쪽지에 숨긴 명령 | [injection-ko](docs/injection-ko.html) | [injection-en](docs/injection-en.html) |
| Botnet | 홀려서 조종당하는 마을 사람들 | [botnet-ko](docs/botnet-ko.html) | [botnet-en](docs/botnet-en.html) |
| APT | 몇 달을 기다리는 끈질긴 도둑 무리 | [apt-ko](docs/apt-ko.html) | [apt-en](docs/apt-en.html) |
| Kill Chain | 도둑의 일곱 걸음 | [killchain-ko](docs/killchain-ko.html) | [killchain-en](docs/killchain-en.html) |
| Insider Threat | 안에서 문을 여는 사람 | [insider-ko](docs/insider-ko.html) | [insider-en](docs/insider-en.html) |
| Supply Chain Attack | 목수의 연장통에 숨어 들어온 벌레 | [supplychain-ko](docs/supplychain-ko.html) | [supplychain-en](docs/supplychain-en.html) |
| Risk Management | 어느 문부터 지킬지 정하는 저울 | [risk-ko](docs/risk-ko.html) | [risk-en](docs/risk-en.html) |
| Compliance | 이웃 나라 규칙 검사관 | [compliance-ko](docs/compliance-ko.html) | [compliance-en](docs/compliance-en.html) |
| Security Policy | 성의 규칙 두루마리 | [policy-ko](docs/policy-ko.html) | [policy-en](docs/policy-en.html) |
| Disaster Recovery | 성이 불타도 다음 날 장사하는 법 | [drp-ko](docs/drp-ko.html) | [drp-en](docs/drp-en.html) |
| DevSecOps | 짓는 동안 같이 보는 목수와 경비 | [devsecops-ko](docs/devsecops-ko.html) | [devsecops-en](docs/devsecops-en.html) |
| Threat Modeling | 짓기 전에 도둑 눈으로 보는 도면 | [threatmodel-ko](docs/threatmodel-ko.html) | [threatmodel-en](docs/threatmodel-en.html) |
| Secrets Management | 열쇠를 벽에 못 박아 두지 않기 | [secrets-ko](docs/secrets-ko.html) | [secrets-en](docs/secrets-en.html) |
| Code Scanning | 도면 검사와 두드려 보기 | [codescan-ko](docs/codescan-ko.html) | [codescan-en](docs/codescan-en.html) |
| SOAR | 경비실의 자동 순서표 기계 | [soar-ko](docs/soar-ko.html) | [soar-en](docs/soar-en.html) |
| Digital Forensics | 발자국을 굳혀서 보관하기 | [forensics-ko](docs/forensics-ko.html) | [forensics-en](docs/forensics-en.html) |
| Data Masking | 이름 대신 번호표 | [masking-ko](docs/masking-ko.html) | [masking-en](docs/masking-en.html) |
| Cloud Security | 빌린 창고 문단속 점검 | [cspm-ko](docs/cspm-ko.html) | [cspm-en](docs/cspm-en.html) |
| Email Security | 우체국 도장 세 개 | [emailsec-ko](docs/emailsec-ko.html) | [emailsec-en](docs/emailsec-en.html) |
| Antivirus | 벌레 그림 카드를 든 경비 | [antivirus-ko](docs/antivirus-ko.html) | [antivirus-en](docs/antivirus-en.html) |
| UEBA | 평소와 다른 걸음걸이 | [ueba-ko](docs/ueba-ko.html) | [ueba-en](docs/ueba-en.html) |
| Spyware | 몰래 엿보고, 몰래 일 시키는 벌레들 | [spyware-ko](docs/spyware-ko.html) | [spyware-en](docs/spyware-en.html) |
| API Security | 창구 뒷문으로 오는 심부름꾼 | [apisec-ko](docs/apisec-ko.html) | [apisec-en](docs/apisec-en.html) |
| Container Security | 똑같이 찍어낸 짐칸 | [container-ko](docs/container-ko.html) | [container-en](docs/container-en.html) |
| IoT / OT Security | 말 못 하는 성 안 기계들 | [iotsec-ko](docs/iotsec-ko.html) | [iotsec-en](docs/iotsec-en.html) |
| Privacy | 손님 이름표는 손님 것 | [privacy-ko](docs/privacy-ko.html) | [privacy-en](docs/privacy-en.html) |
| Session Hijacking | 입장 팔찌를 훔치는 도둑 | [session-ko](docs/session-ko.html) | [session-en](docs/session-en.html) |
| AI Security | 왕의 목소리를 흉내 내는 앵무새 | [aisec-ko](docs/aisec-ko.html) | [aisec-en](docs/aisec-en.html) |
| Security Framework | 성 지키기 다섯 기둥 | [framework-ko](docs/framework-ko.html) | [framework-en](docs/framework-en.html) |
| Security Metrics | 얼마나 빨리 알아채고, 얼마나 빨리 쫓아내나 | [metrics-ko](docs/metrics-ko.html) | [metrics-en](docs/metrics-en.html) |
| Air Gap | 다리 없는 섬 창고 | [airgap-ko](docs/airgap-ko.html) | [airgap-en](docs/airgap-en.html) |
| HSM | 열쇠를 만드는 쇠금고 | [hsm-ko](docs/hsm-ko.html) | [hsm-en](docs/hsm-en.html) |
| Allowlist | 명단에 있는 사람만 | [allowlist-ko](docs/allowlist-ko.html) | [allowlist-en](docs/allowlist-en.html) |
| Cyber Insurance | 도둑 보험 | [cyberinsurance-ko](docs/cyberinsurance-ko.html) | [cyberinsurance-en](docs/cyberinsurance-en.html) |
| the CIA Triad | 지키는 것 세 가지: 못 보게, 못 바꾸게, 늘 쓰게 | [ciatriad-ko](docs/ciatriad-ko.html) | [ciatriad-en](docs/ciatriad-en.html) |
| Defense in Depth | 겹겹이 두른 성벽 | [defenseindepth-ko](docs/defenseindepth-ko.html) | [defenseindepth-en](docs/defenseindepth-en.html) |
| DMZ | 성벽과 성벽 사이의 마당 | [dmz-ko](docs/dmz-ko.html) | [dmz-en](docs/dmz-en.html) |
| Hardening | 새 방을 쓰기 전에 하는 문단속 | [hardening-ko](docs/hardening-ko.html) | [hardening-en](docs/hardening-en.html) |
| MDM and BYOD | 성 밖으로 들고 나가는 작은 상자 | [mdm-ko](docs/mdm-ko.html) | [mdm-en](docs/mdm-en.html) |
| Wi-Fi Security | 마을 광장의 공짜 우체통 | [wifi-ko](docs/wifi-ko.html) | [wifi-en](docs/wifi-en.html) |
| BEC, Smishing and Vishing | 왕의 글씨체로 온 편지 | [bec-ko](docs/bec-ko.html) | [bec-en](docs/bec-en.html) |
| Trojans, Worms, Rootkits and Backdoors | 벌레 도감: 선물 벌레, 기어 다니는 벌레, 숨는 벌레, 뒷문 벌레 | [malwaretypes-ko](docs/malwaretypes-ko.html) | [malwaretypes-en](docs/malwaretypes-en.html) |
| Active Directory | 성의 명부와 열쇠를 한꺼번에 쥔 관리소 | [activedirectory-ko](docs/activedirectory-ko.html) | [activedirectory-en](docs/activedirectory-en.html) |
| CSRF | 손님 팔찌를 빌려 몰래 보내는 쪽지 | [csrf-ko](docs/csrf-ko.html) | [csrf-en](docs/csrf-en.html) |
| OSINT | 마을 소문만 모아도 성 지도가 나와요 | [osint-ko](docs/osint-ko.html) | [osint-en](docs/osint-en.html) |
| Physical Security | 성문을 잠가도 창문이 열려 있으면 | [physical-ko](docs/physical-ko.html) | [physical-en](docs/physical-en.html) |

보안 용어는 하나의 세계를 공유한다 — 내 컴퓨터는 성, 공격자는 수상한 사람, 방어자는 망루 위의 친구·경비실·경비견·복도 파수꾼.

### 소프트웨어 설계

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| Dialog Map | 방과 문의 지도 | [dialogmap-ko](docs/dialogmap-ko.html) | [dialogmap-en](docs/dialogmap-en.html) |

### AI

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| LLM | 책을 산더미로 읽은 앵무새 | [llm-ko](docs/llm-ko.html) | [llm-en](docs/llm-en.html) |
| Token | 앵무새가 말을 콩으로 세요 | [token-ko](docs/token-ko.html) | [token-en](docs/token-en.html) |
| Prompt | 앵무새에게 주는 조련 쪽지 | [prompt-ko](docs/prompt-ko.html) | [prompt-en](docs/prompt-en.html) |
| Context Window | 앵무새 앞의 쟁반 | [context-ko](docs/context-ko.html) | [context-en](docs/context-en.html) |
| Hallucination | 그럴듯 앵무새 | [hallucination-ko](docs/hallucination-ko.html) | [hallucination-en](docs/hallucination-en.html) |
| Fine-tuning | 짧은 특훈 | [finetune-ko](docs/finetune-ko.html) | [finetune-en](docs/finetune-en.html) |
| Embedding | 낱말마다 좌표 딱지 | [embedding-ko](docs/embedding-ko.html) | [embedding-en](docs/embedding-en.html) |
| Vector DB | 딱지로 정리한 서가 | [vectordb-ko](docs/vectordb-ko.html) | [vectordb-en](docs/vectordb-en.html) |
| RAG | 사서가 찾아온 페이지 | [rag-ko](docs/rag-ko.html) | [rag-en](docs/rag-en.html) |
| Memory | 앵무새의 수첩 | [memory-ko](docs/memory-ko.html) | [memory-en](docs/memory-en.html) |
| temperature | 엉뚱함 다이얼 | [temperature-ko](docs/temperature-ko.html) | [temperature-en](docs/temperature-en.html) |
| prompt caching | 미리 놓아둔 콩 | [promptcaching-ko](docs/promptcaching-ko.html) | [promptcaching-en](docs/promptcaching-en.html) |
| structured output | 정해진 칸에 쓰기 | [structuredoutput-ko](docs/structuredoutput-ko.html) | [structuredoutput-en](docs/structuredoutput-en.html) |
| streaming | 콩을 하나씩 바로 보여주기 | [streaming-ko](docs/streaming-ko.html) | [streaming-en](docs/streaming-en.html) |
| Tool Calling | 도구 상자 | [toolcall-ko](docs/toolcall-ko.html) | [toolcall-en](docs/toolcall-en.html) |
| Agent | 심부름 목록을 스스로 짜는 앵무새 | [agent-ko](docs/agent-ko.html) | [agent-en](docs/agent-en.html) |
| MCP | 도구 상자 규격 | [mcp-ko](docs/mcp-ko.html) | [mcp-en](docs/mcp-en.html) |
| Multi-agent | 앵무새 회의 | [multiagent-ko](docs/multiagent-ko.html) | [multiagent-en](docs/multiagent-en.html) |
| Guardrail | 울타리 | [guardrail-ko](docs/guardrail-ko.html) | [guardrail-en](docs/guardrail-en.html) |
| Reasoning | 답하기 전 혼자 중얼거리기 | [reasoning-ko](docs/reasoning-ko.html) | [reasoning-en](docs/reasoning-en.html) |
| Evaluation | 시험관의 채점표 | [evaluation-ko](docs/evaluation-ko.html) | [evaluation-en](docs/evaluation-en.html) |
| Human-in-the-Loop | 마지막은 사람이 | [humanloop-ko](docs/humanloop-ko.html) | [humanloop-en](docs/humanloop-en.html) |
| Multimodal | 그림도 보는 앵무새 | [multimodal-ko](docs/multimodal-ko.html) | [multimodal-en](docs/multimodal-en.html) |
| Diffusion Model | 안개에서 그림 꺼내기 | [diffusion-ko](docs/diffusion-ko.html) | [diffusion-en](docs/diffusion-en.html) |
| Code Generation | 코드 쓰는 앵무새 | [codegen-ko](docs/codegen-ko.html) | [codegen-en](docs/codegen-en.html) |
| Workflow | 심부름 순서표 | [workflow-ko](docs/workflow-ko.html) | [workflow-en](docs/workflow-en.html) |
| Distillation | 작은 앵무새에게 흉내 가르치기 | [distillation-ko](docs/distillation-ko.html) | [distillation-en](docs/distillation-en.html) |
| Quantization | 콩을 굵게 세기 | [quantization-ko](docs/quantization-ko.html) | [quantization-en](docs/quantization-en.html) |
| Inference | 앵무새가 답하는 값과 시간 | [inference-ko](docs/inference-ko.html) | [inference-en](docs/inference-en.html) |
| Pricing | 콩 값 | [pricing-ko](docs/pricing-ko.html) | [pricing-en](docs/pricing-en.html) |
| Attention | 앵무새의 눈길 | [attention-ko](docs/attention-ko.html) | [attention-en](docs/attention-en.html) |
| Pre-training | 책 읽는 학교 | [pretraining-ko](docs/pretraining-ko.html) | [pretraining-en](docs/pretraining-en.html) |
| Alignment | 앵무새 예절 교육 | [alignment-ko](docs/alignment-ko.html) | [alignment-en](docs/alignment-en.html) |
| Knowledge Cutoff | 책을 덮은 날 | [knowledgecutoff-ko](docs/knowledgecutoff-ko.html) | [knowledgecutoff-en](docs/knowledgecutoff-en.html) |
| Open Weights | 우리 집 앵무새 vs 빌린 앵무새 | [openweights-ko](docs/openweights-ko.html) | [openweights-en](docs/openweights-en.html) |
| Routing | 어느 앵무새에게 시킬까 | [routing-ko](docs/routing-ko.html) | [routing-en](docs/routing-en.html) |
| LLMOps | 앵무새 돌보기 | [llmops-ko](docs/llmops-ko.html) | [llmops-en](docs/llmops-en.html) |
| Bias | 앵무새가 읽은 책의 치우침 | [bias-ko](docs/bias-ko.html) | [bias-en](docs/bias-en.html) |
| AI Privacy | 앵무새에게 준 비밀 콩 | [aiprivacy-ko](docs/aiprivacy-ko.html) | [aiprivacy-en](docs/aiprivacy-en.html) |
| Synthetic Data | 앵무새가 쓴 책으로 앵무새 가르치기 | [synthetic-ko](docs/synthetic-ko.html) | [synthetic-en](docs/synthetic-en.html) |

AI 용어는 하나의 세계를 공유한다 — 모델은 책을 산더미로 읽은 앵무새, 토큰은 콩, 프롬프트는 조련 쪽지, 컨텍스트 창은 쟁반, RAG 는 사서, 도구는 공방의 도구 상자 (`terms/ai/_WORLD.md`).

### SRE

| 단계 | 용어 | 이야기 | 한글 | English |
|---|---|---|---|---|
| Plan | SRE | 쉬지 않는 공원을 돌보는 사람들 | [reliability-ko](docs/reliability-ko.html) | [reliability-en](docs/reliability-en.html) |
| Plan | SLI | 오늘 운행 기록판 | [sli-ko](docs/sli-ko.html) | [sli-en](docs/sli-en.html) |
| Plan | SLO | 우리끼리 정한 목표 줄 | [slo-ko](docs/slo-ko.html) | [slo-en](docs/slo-en.html) |
| Plan | SLA | 손님과 맺은 약속 계약서 | [sla-ko](docs/sla-ko.html) | [sla-en](docs/sla-en.html) |
| Plan | Error Budget | 허용된 고장 티켓 묶음 | [errorbudget-ko](docs/errorbudget-ko.html) | [errorbudget-en](docs/errorbudget-en.html) |
| Plan | Capacity Planning | 내년 손님 수를 미리 세어보기 | [capacityplanning-ko](docs/capacityplanning-ko.html) | [capacityplanning-en](docs/capacityplanning-en.html) |
| Plan | API Gateway | 정문 안내소 | [apigateway-ko](docs/apigateway-ko.html) | [apigateway-en](docs/apigateway-en.html) |
| Plan | Service Mesh | 기구 사이 전용 통로 | [servicemesh-ko](docs/servicemesh-ko.html) | [servicemesh-en](docs/servicemesh-en.html) |
| Plan | Caching | 자주 묻는 질문 미리 적어둔 메모판 | [caching-ko](docs/caching-ko.html) | [caching-en](docs/caching-en.html) |
| Plan | Sharding | 번호별로 나뉜 매표 창구 | [sharding-ko](docs/sharding-ko.html) | [sharding-en](docs/sharding-en.html) |
| Plan | Replication | 손님 명부를 두 창고에 똑같이 | [replication-ko](docs/replication-ko.html) | [replication-en](docs/replication-en.html) |
| Plan | Consensus | 여러 관제실이 손 들어 정하기 | [consensus-ko](docs/consensus-ko.html) | [consensus-en](docs/consensus-en.html) |
| Plan | Split-Brain | 두 관제실이 서로 자기가 진짜라고 | [splitbrain-ko](docs/splitbrain-ko.html) | [splitbrain-en](docs/splitbrain-en.html) |
| Plan | CAP Theorem | 정확함과 항상 열림, 둘 다는 못 가져요 | [captheorem-ko](docs/captheorem-ko.html) | [captheorem-en](docs/captheorem-en.html) |
| Plan | Eventual Consistency | 조금 늦게 맞춰지는 재고판 | [eventualconsistency-ko](docs/eventualconsistency-ko.html) | [eventualconsistency-en](docs/eventualconsistency-en.html) |
| Plan | Multi-region | 쌍둥이 공원 | [multiregion-ko](docs/multiregion-ko.html) | [multiregion-en](docs/multiregion-en.html) |
| Plan | Infrastructure as Code | 설계도 한 장으로 공원 통째로 짓기 | [iac-ko](docs/iac-ko.html) | [iac-en](docs/iac-en.html) |
| Plan | GitOps | 설계도가 바뀌면 자동으로 공사 | [gitops-ko](docs/gitops-ko.html) | [gitops-en](docs/gitops-en.html) |
| Do | Rate Limiting | 한 번에 몇 명까지만 | [ratelimiting-ko](docs/ratelimiting-ko.html) | [ratelimiting-en](docs/ratelimiting-en.html) |
| Do | Health Check | 안전바 딸깍 확인 | [healthcheck-ko](docs/healthcheck-ko.html) | [healthcheck-en](docs/healthcheck-en.html) |
| Do | Service Discovery | 지금 열린 창구 안내판 | [servicediscovery-ko](docs/servicediscovery-ko.html) | [servicediscovery-en](docs/servicediscovery-en.html) |
| Do | Orchestration | 몇 대를 켤지 정하는 운영 본부 | [orchestration-ko](docs/orchestration-ko.html) | [orchestration-en](docs/orchestration-en.html) |
| Do | Message Queue | 주문서를 쌓아두는 바구니 | [messagequeue-ko](docs/messagequeue-ko.html) | [messagequeue-en](docs/messagequeue-en.html) |
| Do | Dead-letter Queue | 아무도 안 찾아간 바구니함 | [deadletterqueue-ko](docs/deadletterqueue-ko.html) | [deadletterqueue-en](docs/deadletterqueue-en.html) |
| Do | Backpressure | 입구를 잠깐 막기 | [backpressure-ko](docs/backpressure-ko.html) | [backpressure-en](docs/backpressure-en.html) |
| Do | Bulkhead | 불이 안 번지게 나눈 구역 | [bulkhead-ko](docs/bulkhead-ko.html) | [bulkhead-en](docs/bulkhead-en.html) |
| Do | Circuit Breaker | 고장나면 누르는 빨간 버튼 | [circuitbreaker-ko](docs/circuitbreaker-ko.html) | [circuitbreaker-en](docs/circuitbreaker-en.html) |
| Do | Retry with Backoff | 잠깐 쉬었다 다시 줄서기 | [retrybackoff-ko](docs/retrybackoff-ko.html) | [retrybackoff-en](docs/retrybackoff-en.html) |
| Do | Idempotency | 같은 티켓으로 두 번 못 타요 | [idempotency-ko](docs/idempotency-ko.html) | [idempotency-en](docs/idempotency-en.html) |
| Do | Autoscaling | 줄이 길어지면 직원을 더 부르기 | [autoscaling-ko](docs/autoscaling-ko.html) | [autoscaling-en](docs/autoscaling-en.html) |
| Do | Graceful Degradation | 일부만 고장나도 나머지는 그대로 | [gracefuldegradation-ko](docs/gracefuldegradation-ko.html) | [gracefuldegradation-en](docs/gracefuldegradation-en.html) |
| Do | Failover | 발전기가 꺼지면 예비 발전기가 | [failover-ko](docs/failover-ko.html) | [failover-en](docs/failover-en.html) |
| Do | Feature Flag | 새 기구에 친 커튼 | [featureflag-ko](docs/featureflag-ko.html) | [featureflag-en](docs/featureflag-en.html) |
| Do | Canary Deployment | 구석에서 몰래 하는 시험 운행 | [canary-ko](docs/canary-ko.html) | [canary-en](docs/canary-en.html) |
| Do | Blue-Green Deployment | 쌍둥이 기구를 번갈아 운영 | [bluegreen-ko](docs/bluegreen-ko.html) | [bluegreen-en](docs/bluegreen-en.html) |
| Do | Rollback | 이상하면 바로 어제 버전으로 | [rollback-ko](docs/rollback-ko.html) | [rollback-en](docs/rollback-en.html) |
| Check | Golden Signals | 관제실의 계기판 네 개 | [goldensignals-ko](docs/goldensignals-ko.html) | [goldensignals-en](docs/goldensignals-en.html) |
| Check | Observability | 세 가지로 들여다보기 | [observability-ko](docs/observability-ko.html) | [observability-en](docs/observability-en.html) |
| Check | Alerting | 몇 번 울려야 진짜 비상인가 | [alerting-ko](docs/alerting-ko.html) | [alerting-en](docs/alerting-en.html) |
| Check | Chaos Engineering | 일부러 내는 가짜 고장 | [chaosengineering-ko](docs/chaosengineering-ko.html) | [chaosengineering-en](docs/chaosengineering-en.html) |
| Check | Game Day | 가짜 화재 훈련일 | [gameday-ko](docs/gameday-ko.html) | [gameday-en](docs/gameday-en.html) |
| Check | DORA Metrics | 우리 공사팀 네 가지 성적표 | [dorametrics-ko](docs/dorametrics-ko.html) | [dorametrics-en](docs/dorametrics-en.html) |
| Act | On-call | 이번 주 호출기를 든 사람 | [oncall-ko](docs/oncall-ko.html) | [oncall-en](docs/oncall-en.html) |
| Act | Incident Commander | 지휘봉을 든 사람 | [incidentcommand-ko](docs/incidentcommand-ko.html) | [incidentcommand-en](docs/incidentcommand-en.html) |
| Act | Runbook | 정비사의 공책 | [runbook-ko](docs/runbook-ko.html) | [runbook-en](docs/runbook-en.html) |
| Act | Postmortem | 탓하지 않고 모여 쓰는 기록 | [postmortem-ko](docs/postmortem-ko.html) | [postmortem-en](docs/postmortem-en.html) |
| Act | Toil | 매일 똑같이 반복하는 허드렛일 | [toil-ko](docs/toil-ko.html) | [toil-en](docs/toil-en.html) |
SRE 용어는 하나의 세계를 공유한다 — 공원은 우리 시스템, 놀이기구는 서비스, 손님은 요청, 관제실은 모니터링, 정비사는 엔지니어 (`terms/sre/_WORLD.md`).
순서는 PDCA(Plan-Do-Check-Act) 틀을 따른다 — 목표를 정하고 설계(Plan) → 설계대로 운영·배포(Do) → 제대로 되는지 관측·검증(Check) → 이상 신호에 대응하고 교훈을 다음 계획에 반영(Act).

### AI 보안

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| AI Security | 다 받아주는 주방 | [llmthreats-ko](docs/llmthreats-ko.html) | [llmthreats-en](docs/llmthreats-en.html) |
| Prompt Injection | 주문서 뒤에 몰래 끼운 쪽지 | [promptinjection-ko](docs/promptinjection-ko.html) | [promptinjection-en](docs/promptinjection-en.html) |
| Indirect Prompt Injection | 재료 포장지에 적힌 몰래 쪽지 | [indirectinjection-ko](docs/indirectinjection-ko.html) | [indirectinjection-en](docs/indirectinjection-en.html) |
| Jailbreak | 주방장을 구슬려 규칙을 깨게 하기 | [jailbreak-ko](docs/jailbreak-ko.html) | [jailbreak-en](docs/jailbreak-en.html) |
| Prompt Leak | 비밀 레시피 수칙을 캐내기 | [promptleak-ko](docs/promptleak-ko.html) | [promptleak-en](docs/promptleak-en.html) |
| Prompt Filter Evasion | 암호처럼 꼬아 쓴 주문서 | [promptevasion-ko](docs/promptevasion-ko.html) | [promptevasion-en](docs/promptevasion-en.html) |
| Image Prompt Injection | 메뉴판 사진 속에 숨긴 글자 | [imageinjection-ko](docs/imageinjection-ko.html) | [imageinjection-en](docs/imageinjection-en.html) |
| Adversarial Example | 눈속임 그림 주문서 | [adversarialexample-ko](docs/adversarialexample-ko.html) | [adversarialexample-en](docs/adversarialexample-en.html) |
| Model Extraction Attack | 레시피북 통째로 베껴가기 | [modelextraction-ko](docs/modelextraction-ko.html) | [modelextraction-en](docs/modelextraction-en.html) |
| Model Inversion | 접시 더미에서 되살린 얼굴 | [modelinversion-ko](docs/modelinversion-ko.html) | [modelinversion-en](docs/modelinversion-en.html) |
| Membership Inference | 눈 감고도 만드는 요리 | [membershipinference-ko](docs/membershipinference-ko.html) | [membershipinference-en](docs/membershipinference-en.html) |
| Memorization | 그대로 베낀 접시 | [memorization-ko](docs/memorization-ko.html) | [memorization-en](docs/memorization-en.html) |
| Data Poisoning | 수상한 재료 자루 | [datapoisoning-ko](docs/datapoisoning-ko.html) | [datapoisoning-en](docs/datapoisoning-en.html) |
| RAG Poisoning | 참고 카드함에 끼운 가짜 카드 | [ragpoisoning-ko](docs/ragpoisoning-ko.html) | [ragpoisoning-en](docs/ragpoisoning-en.html) |
| Backdoor | 숨겨진 암호 주문어 | [backdoor-ko](docs/backdoor-ko.html) | [backdoor-en](docs/backdoor-en.html) |
| Trojan Model | 다듬는 중에 몰래 심은 버릇 | [trojanmodel-ko](docs/trojanmodel-ko.html) | [trojanmodel-en](docs/trojanmodel-en.html) |
| Excessive Agency | 너무 많은 열쇠를 받은 견습생 | [excessiveagency-ko](docs/excessiveagency-ko.html) | [excessiveagency-en](docs/excessiveagency-en.html) |
| Unsafe Output Handling | 접시를 그대로 기계에 넣다가 | [unsafeoutput-ko](docs/unsafeoutput-ko.html) | [unsafeoutput-en](docs/unsafeoutput-en.html) |
| Zero-click Attack | 가만히 있어도 실행되는 공격 | [zeroclick-ko](docs/zeroclick-ko.html) | [zeroclick-en](docs/zeroclick-en.html) |
| Tool Sandbox | 잠긴 칼 서랍 | [toolsandbox-ko](docs/toolsandbox-ko.html) | [toolsandbox-en](docs/toolsandbox-en.html) |
| Per-tool Permission | 도구별 권한 배지 | [toolpermission-ko](docs/toolpermission-ko.html) | [toolpermission-en](docs/toolpermission-en.html) |
| LLMDoS | 화구를 멈추지 않는 주문 | [llmdos-ko](docs/llmdos-ko.html) | [llmdos-en](docs/llmdos-en.html) |
| AIBOM | 재료 출처 인증서 | [aibom-ko](docs/aibom-ko.html) | [aibom-en](docs/aibom-en.html) |
| Model Card | 요리 설명표 | [modelcard-ko](docs/modelcard-ko.html) | [modelcard-en](docs/modelcard-en.html) |
| Watermark | 요리에 새긴 표식 | [watermark-ko](docs/watermark-ko.html) | [watermark-en](docs/watermark-en.html) |
| AI Red Team | 위생 검사관의 불시 방문 | [airedteam-ko](docs/airedteam-ko.html) | [airedteam-en](docs/airedteam-en.html) |
| Safety Evaluation | 손님 받기 전 맛 평가 테스트 | [safetyeval-ko](docs/safetyeval-ko.html) | [safetyeval-en](docs/safetyeval-en.html) |
| Human Approval Gate | 사장님 최종 승인 | [humanapproval-ko](docs/humanapproval-ko.html) | [humanapproval-en](docs/humanapproval-en.html) |
| AI Governance | 주방 규칙판 | [aigovernance-ko](docs/aigovernance-ko.html) | [aigovernance-en](docs/aigovernance-en.html) |
| Shadow AI | 몰래 들여온 배달 상자 | [shadowai-ko](docs/shadowai-ko.html) | [shadowai-en](docs/shadowai-en.html) |
| AI Incident Response | 울리는 비상벨 | [aiincident-ko](docs/aiincident-ko.html) | [aiincident-en](docs/aiincident-en.html) |
| AI Audit Log | 매일 적는 주문 기록 장부 | [aiaudit-ko](docs/aiaudit-ko.html) | [aiaudit-en](docs/aiaudit-en.html) |
AI 보안 용어는 하나의 세계를 공유한다 — 주방은 AI 시스템, 주방장은 모델, 손님은 요청, 위생 검사관은 레드팀 (`terms/llmsec/_WORLD.md`).
순서는 다섯 챕터를 따른다 — 프롬프트 단계 공격 → 모델 자체를 노리는 공격 → 에이전트·도구 시대의 위험 → 공급망과 투명성 → 막고 지키기(거버넌스·운영).

## PPE (정보관리기술사·컴퓨터시스템응용기술사)

탭 바에서는 아래 10개 분야가 "PPE" 구분선 아래 모여 보인다 — 각자 독립된 세계관과 슬러그 공간을 가진 별도 분야이고, 시험 범위상 한 그룹으로 묶여 있을 뿐이다. 이미 다른 분야(보안·AI·SRE)에 있는 용어는 다시 쓰지 않고 그 페이지로 링크했다.

### PPE·SW공학

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 정보시스템 감리/PMO | 출간 전 마지막 검수관 | [pmoaudit-ko](docs/pmoaudit-ko.html) | [pmoaudit-en](docs/pmoaudit-en.html) |
| ISP/ISMP | 출판 로드맵을 그리는 사람 | [ispismp-ko](docs/ispismp-ko.html) | [ispismp-en](docs/ispismp-en.html) |
| 요구공학/요구사항 명세 | 쓰기 전에 먼저 묻는 사람 | [reqeng-ko](docs/reqeng-ko.html) | [reqeng-en](docs/reqeng-en.html) |
| 애자일/스크럼 | 한 챕터씩 보여주며 쓰기 | [agilescrum-ko](docs/agilescrum-ko.html) | [agilescrum-en](docs/agilescrum-en.html) |
| 화이트박스/블랙박스 테스트 | 속을 펼쳐 볼지, 겉만 읽을지 | [wbblacktest-ko](docs/wbblacktest-ko.html) | [wbblacktest-en](docs/wbblacktest-en.html) |
| 데이터 품질관리 | 독자 주소록을 돌보는 일 | [dataqual-ko](docs/dataqual-ko.html) | [dataqual-en](docs/dataqual-en.html) |
| 소프트웨어 안전/기능안전 | 오탈자 하나의 무게가 다른 책 | [swsafety-ko](docs/swsafety-ko.html) | [swsafety-en](docs/swsafety-en.html) |
| 재공학/역공학(3R) | 사라진 원본을 되짚어 다시 짓기 | [reengineering-ko](docs/reengineering-ko.html) | [reengineering-en](docs/reengineering-en.html) |
| GoF 디자인패턴 | 검증된 글쓰기 공식집 | [gofpattern-ko](docs/gofpattern-ko.html) | [gofpattern-en](docs/gofpattern-en.html) |
| 마이크로서비스 아키텍처(MSA) | 두꺼운 책을 소책자들로 쪼개기 | [msa-ko](docs/msa-ko.html) | [msa-en](docs/msa-en.html) |
| UML 다이어그램 작성 | 쓰기 전에 그리는 설계 지도 | [umldiagram-ko](docs/umldiagram-ko.html) | [umldiagram-en](docs/umldiagram-en.html) |
| 기능점수(FP) | 매수를 재는 자 | [fpruler-ko](docs/fpruler-ko.html) | [fpruler-en](docs/fpruler-en.html) |
| 소프트웨어 형상관리(SCM) | 원고를 지키는 보관 서가 | [scmshelf-ko](docs/scmshelf-ko.html) | [scmshelf-en](docs/scmshelf-en.html) |
| MLOps/ModelOps | 자동 교정 기계 돌보기 | [mlops-ko](docs/mlops-ko.html) | [mlops-en](docs/mlops-en.html) |
| SW 사업 대가산정 | 매수를 돈으로 바꾸는 계산 | [swcost-ko](docs/swcost-ko.html) | [swcost-en](docs/swcost-en.html) |
| SW사업 영향평가 | 고치기 전에 그려보는 연결 지도 | [swimpact-ko](docs/swimpact-ko.html) | [swimpact-en](docs/swimpact-en.html) |
| 명세기반 테스트 설계기법 | 규칙서만 보고 고르는 대표 사례 | [spectest-ko](docs/spectest-ko.html) | [spectest-en](docs/spectest-en.html) |
| DevOps | 담장을 허문 작가와 인쇄소 | [devopsswe-ko](docs/devopsswe-ko.html) | [devopsswe-en](docs/devopsswe-en.html) |
| 개방형 API(Open API) | 서식 하나로 열어둔 열람실 | [openapi-ko](docs/openapi-ko.html) | [openapi-en](docs/openapi-en.html) |
| 캡슐화·정보은닉 | 작가의 잠긴 서랍 | [encapsulation-ko](docs/encapsulation-ko.html) | [encapsulation-en](docs/encapsulation-en.html) |
| SW 성능테스트 | 미리 몰려보는 가짜 독자들 | [perftest-ko](docs/perftest-ko.html) | [perftest-en](docs/perftest-en.html) |
| 통계적 가설검정 | 두 표지 중 뭐가 진짜 더 잘 팔릴까 | [hypothesistest-ko](docs/hypothesistest-ko.html) | [hypothesistest-en](docs/hypothesistest-en.html) |
| 리팩토링 | 줄거리는 그대로, 문장만 다시 다듬기 | [refactorppe-ko](docs/refactorppe-ko.html) | [refactorppe-en](docs/refactorppe-en.html) |
| 빅데이터 플랫폼 | 전국 창고 네트워크 | [bigdataplatform-ko](docs/bigdataplatform-ko.html) | [bigdataplatform-en](docs/bigdataplatform-en.html) |
| 메타모픽 테스트 | 정답 없이도 관계로 확인하기 | [metamorphictest-ko](docs/metamorphictest-ko.html) | [metamorphictest-en](docs/metamorphictest-en.html) |
| WBS | 책 만들기를 나뭇가지로 늘어놓기 | [wbsswe-ko](docs/wbsswe-ko.html) | [wbsswe-en](docs/wbsswe-en.html) |
| 기술부채 | 지금 빨리 가려고 쌓아둔 빚 | [techdebt-ko](docs/techdebt-ko.html) | [techdebt-en](docs/techdebt-en.html) |
| 개발방법론 테일러링 | 책마다 다른 편집 규칙 | [tailoring-ko](docs/tailoring-ko.html) | [tailoring-en](docs/tailoring-en.html) |
| 제품계열(Product Line) 방법론 | 같은 틀, 다른 표지 | [productline-ko](docs/productline-ko.html) | [productline-en](docs/productline-en.html) |
| 품질보증(QA)과 품질관리(QC) | 규칙을 지켰나, 책이 맞나 | [qaqc-ko](docs/qaqc-ko.html) | [qaqc-en](docs/qaqc-en.html) |
| 프로젝트 갈등관리 | 작가와 편집장이 다툴 때 | [conflictmgmt-ko](docs/conflictmgmt-ko.html) | [conflictmgmt-en](docs/conflictmgmt-en.html) |
| 좋은 소프트웨어 | 좋은 책의 조건 | [goodsw-ko](docs/goodsw-ko.html) | [goodsw-en](docs/goodsw-en.html) |
| 상용SW 직접구매 | 인쇄기를 중간상인 없이 바로 사기 | [swpurchase-ko](docs/swpurchase-ko.html) | [swpurchase-en](docs/swpurchase-en.html) |
| 결합도와 응집도 | 챕터가 서로 얼마나 엮여있나 | [couplingcohesion-ko](docs/couplingcohesion-ko.html) | [couplingcohesion-en](docs/couplingcohesion-en.html) |
| 아키텍처 평가(ATAM/CBAM) | 출간 전 시나리오 리허설 | [atamcbam-ko](docs/atamcbam-ko.html) | [atamcbam-en](docs/atamcbam-en.html) |
| SW 품질인증 | 책 표지의 공식 마크 | [swcert-ko](docs/swcert-ko.html) | [swcert-en](docs/swcert-en.html) |
| 디자인 씽킹 | 책상 추측 대신 독자에게 직접 묻기 | [designthinking-ko](docs/designthinking-ko.html) | [designthinking-en](docs/designthinking-en.html) |
| 의존성 주입/역전(DI/DIP) | 아무 기계나 꽂을 수 있는 콘센트 | [diprinciple-ko](docs/diprinciple-ko.html) | [diprinciple-en](docs/diprinciple-en.html) |
| 사용성평가(Usability) | 독자가 책을 쓱 넘겨보는 시험 | [usability-ko](docs/usability-ko.html) | [usability-en](docs/usability-en.html) |
| 소프트웨어 아키텍처 모델 | 책 전체를 미리 짜 두는 구조 밑그림 | [swarchmodel-ko](docs/swarchmodel-ko.html) | [swarchmodel-en](docs/swarchmodel-en.html) |

### PPE·DB/데이터

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 정규화/반정규화 | 한 칸에 한 번만 적는 규칙 | [normalization-ko](docs/normalization-ko.html) | [normalization-en](docs/normalization-en.html) |
| NoSQL 유형·모델링 | 상자 모양에 맞춰 선반을 바꾸는 창고 | [nosqltype-ko](docs/nosqltype-ko.html) | [nosqltype-en](docs/nosqltype-en.html) |
| 데이터베이스 샤딩·파티셔닝 | 너무 커진 창고를 구역으로 쪼개기 | [dbsharding-ko](docs/dbsharding-ko.html) | [dbsharding-en](docs/dbsharding-en.html) |
| 트랜잭션 격리 수준 | 동시에 손댈 때 얼마나 가려 볼지 정하는 규칙 | [isolevel-ko](docs/isolevel-ko.html) | [isolevel-en](docs/isolevel-en.html) |
| LOD·오픈 데이터 | 문을 열고 번호표를 달아 연결해두는 창고 | [lodopendata-ko](docs/lodopendata-ko.html) | [lodopendata-en](docs/lodopendata-en.html) |
| 트랜잭션과 ACID | 출납 전표가 지키는 네 가지 약속 | [acid-ko](docs/acid-ko.html) | [acid-en](docs/acid-en.html) |
| 데이터베이스 병행제어 | 동시에 손대도 안 부딪히게 막는 규칙 | [concurrency-ko](docs/concurrency-ko.html) | [concurrency-en](docs/concurrency-en.html) |
| 인메모리 컴퓨팅(In-Memory DB/IMDG) | 깊은 선반 대신 바로 꺼내는 특급 출고대 | [inmemorydb-ko](docs/inmemorydb-ko.html) | [inmemorydb-en](docs/inmemorydb-en.html) |
| SCADA | 창고 전체를 한눈에 보는 관제실 | [scada-ko](docs/scada-ko.html) | [scada-en](docs/scada-en.html) |
| 분산 데이터베이스 | 여러 지점으로 나뉜 창고 | [distdb-ko](docs/distdb-ko.html) | [distdb-en](docs/distdb-en.html) |
| 다차원 색인구조 | 여러 딱지로 한 번에 찾기 | [multiindex-ko](docs/multiindex-ko.html) | [multiindex-en](docs/multiindex-en.html) |
| 동적 SQL | 그 자리에서 맞춤 주문서 쓰기 | [dynamicsql-ko](docs/dynamicsql-ko.html) | [dynamicsql-en](docs/dynamicsql-en.html) |
| RAID | 선반을 쪼개고 겹쳐서 쌓기 | [raid-ko](docs/raid-ko.html) | [raid-en](docs/raid-en.html) |
| 데이터 웨어하우스 | 다듬어 둔 창고 vs 쌓아만 둔 야적장 | [dwlake-ko](docs/dwlake-ko.html) | [dwlake-en](docs/dwlake-en.html) |
| OLAP | 전체를 썰어보는 창고 관리자 | [olap-ko](docs/olap-ko.html) | [olap-en](docs/olap-en.html) |
| SDDC | 소프트웨어로 다시 짓는 창고 | [sddc-ko](docs/sddc-ko.html) | [sddc-en](docs/sddc-en.html) |

### PPE·AI이론

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| AI 학습용 데이터 품질관리 | 상한 씨앗으로 가르친 선별기 | [aidataqual-ko](docs/aidataqual-ko.html) | [aidataqual-en](docs/aidataqual-en.html) |
| AI 윤리기준·거버넌스 | 모든 검사장이 함께 쓰는 등급 원칙판 | [aiethicsgov-ko](docs/aiethicsgov-ko.html) | [aiethicsgov-en](docs/aiethicsgov-en.html) |
| 적대적 공격 | 작물에 몰래 붙인 가짜 점무늬 | [advattack-ko](docs/advattack-ko.html) | [advattack-en](docs/advattack-en.html) |
| 혼동행렬 | 네 칸으로 나눈 도장 기록부 | [confmatrix-ko](docs/confmatrix-ko.html) | [confmatrix-en](docs/confmatrix-en.html) |
| AI 리스크 관리 프레임워크 | 검사장 전체를 도는 운영 지도 | [airiskframe-ko](docs/airiskframe-ko.html) | [airiskframe-en](docs/airiskframe-en.html) |
| 군집분석 | 이름표 없이 비슷한 것끼리 모으기 | [clustering-ko](docs/clustering-ko.html) | [clustering-en](docs/clustering-en.html) |
| CNN(합성곱 신경망) | 작은 창으로 조금씩 살펴보는 눈 | [cnn-ko](docs/cnn-ko.html) | [cnn-en](docs/cnn-en.html) |
| 로지스틱 회귀분석 | 저울 눈금을 S자 곡선에 넣어 보기 | [logisticreg-ko](docs/logisticreg-ko.html) | [logisticreg-en](docs/logisticreg-en.html) |
| 이상치 | 무리에서 유난히 튀는 작물 | [outlier-ko](docs/outlier-ko.html) | [outlier-en](docs/outlier-en.html) |
| 인공지능기본법·고영향 AI | 나라가 정한 최소 등급 기준 | [aibasiclaw-ko](docs/aibasiclaw-ko.html) | [aibasiclaw-en](docs/aibasiclaw-en.html) |
| 피지컬 AI | 사진만 보던 눈이 팔다리를 얻다 | [physicalai-ko](docs/physicalai-ko.html) | [physicalai-en](docs/physicalai-en.html) |
| AX(AI 전환) | 검사장 전체를 다시 설계하다 | [axtransform-ko](docs/axtransform-ko.html) | [axtransform-en](docs/axtransform-en.html) |
| AI 개인정보보호 | 출하자 명부를 지키는 서류함 | [aiprivacyppe-ko](docs/aiprivacyppe-ko.html) | [aiprivacyppe-en](docs/aiprivacyppe-en.html) |
| OWASP LLM 보안 위협 Top 10 | 검사장 입구의 업계 공용 위험 게시판 | [owaspllm-ko](docs/owaspllm-ko.html) | [owaspllm-en](docs/owaspllm-en.html) |
| 시계열분석(AR/MA) | 지난 며칠을 보고 내일을 가늠하는 검수반장 | [timeseries-ko](docs/timeseries-ko.html) | [timeseries-en](docs/timeseries-en.html) |
| AI 신뢰성 | 정확도 하나로는 못 받는 품질인증 등급판 | [aitrust-ko](docs/aitrust-ko.html) | [aitrust-en](docs/aitrust-en.html) |
| AIaaS(AI as a Service) | 선별기를 사지 않고 구독하는 농가들 | [aiaas-ko](docs/aiaas-ko.html) | [aiaas-en](docs/aiaas-en.html) |
| 온디바이스 AI | 창고 안에 직접 둔 작은 선별기 | [ondeviceai-ko](docs/ondeviceai-ko.html) | [ondeviceai-en](docs/ondeviceai-en.html) |
| 불편추정량 | 치우치지 않은 저울눈금 | [unbiasedest-ko](docs/unbiasedest-ko.html) | [unbiasedest-en](docs/unbiasedest-en.html) |
| 회귀모형 가정 | 저울을 똑바로 걸기 위한 네 가지 조건 | [regassumption-ko](docs/regassumption-ko.html) | [regassumption-en](docs/regassumption-en.html) |
| 강화학습 | 정답표 없이 점수로 배우는 신입 조작원 | [rl-ko](docs/rl-ko.html) | [rl-en](docs/rl-en.html) |
| 교차검증 | 조를 돌아가며 시험지로 쓰는 검수반장 | [crossval-ko](docs/crossval-ko.html) | [crossval-en](docs/crossval-en.html) |
| 앙상블(Ensemble) 기법 | 세 조작원의 의견을 모아 결정하는 검사장 | [ensemble-ko](docs/ensemble-ko.html) | [ensemble-en](docs/ensemble-en.html) |

### PPE·네트워크

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 5G 특화망 | 이 공장만을 위한 전용 배송망 | [5gprivate-ko](docs/5gprivate-ko.html) | [5gprivate-en](docs/5gprivate-en.html) |
| TCP/UDP | 등기봉투와 일반봉투 | [tcpudp-ko](docs/tcpudp-ko.html) | [tcpudp-en](docs/tcpudp-en.html) |
| SDN/NFV | 소프트웨어로 길을 바꾸는 관제탑 | [sdnnfv-ko](docs/sdnnfv-ko.html) | [sdnnfv-en](docs/sdnnfv-en.html) |
| 무선충전기술 | 줄 없이 세우기만 하면 되는 충전판 | [wirelesscharge-ko](docs/wirelesscharge-ko.html) | [wirelesscharge-en](docs/wirelesscharge-en.html) |
| 5G 네트워크 슬라이싱 | 한 도로를 차선으로 나누기 | [5gslicing-ko](docs/5gslicing-ko.html) | [5gslicing-en](docs/5gslicing-en.html) |
| 다중접속·매체접근제어 | 하나의 통로를 안 부딪히고 나눠 쓰는 법 | [macprotocol-ko](docs/macprotocol-ko.html) | [macprotocol-en](docs/macprotocol-en.html) |
| TCP 오류·흐름·혼잡 제어 | 등기 배송을 끝까지 지키는 세 장치 | [tcpcontrol-ko](docs/tcpcontrol-ko.html) | [tcpcontrol-en](docs/tcpcontrol-en.html) |
| 동적 라우팅 프로토콜 | 스스로 고쳐 그리는 배송 지도 | [dynamicrouting-ko](docs/dynamicrouting-ko.html) | [dynamicrouting-en](docs/dynamicrouting-en.html) |
| 인터럽트(네트워크 I/O) | 소포가 도착했다고 알리는 벨소리 | [interruptnet-ko](docs/interruptnet-ko.html) | [interruptnet-en](docs/interruptnet-en.html) |
| 소켓 | 이 대화만을 위한 전용 우편함 구멍 | [socket-ko](docs/socket-ko.html) | [socket-en](docs/socket-en.html) |
| 무선 측위 | 신호탑 세 개로 위치 찾기 | [wirelesspos-ko](docs/wirelesspos-ko.html) | [wirelesspos-en](docs/wirelesspos-en.html) |
| IPv6 | 끝없이 늘어난 새 번지수 | [ipv6-ko](docs/ipv6-ko.html) | [ipv6-en](docs/ipv6-en.html) |
| 5G 이동통신 핵심기술 | 상황별 전용 차선을 가진 배송망 | [5gcore-ko](docs/5gcore-ko.html) | [5gcore-en](docs/5gcore-en.html) |
| 트래픽 폴리싱·쉐이핑 | 접수량을 조절하는 창구 규칙 | [trafficshaping-ko](docs/trafficshaping-ko.html) | [trafficshaping-en](docs/trafficshaping-en.html) |
| 네트워크 서브네팅 | 동네를 작은 우편번호 구역으로 나누기 | [subnetting-ko](docs/subnetting-ko.html) | [subnetting-en](docs/subnetting-en.html) |
| Modbus 프로토콜 | 우체국장이 순서대로 묻는 쪽지 규칙 | [modbus-ko](docs/modbus-ko.html) | [modbus-en](docs/modbus-en.html) |
| IPC(네트워크 프로세스 간 통신) | 멀리 떨어진 건물 사이에 여는 전용 편지함 | [ipc-ko](docs/ipc-ko.html) | [ipc-en](docs/ipc-en.html) |
| Ad-hoc 라우팅 프로토콜 | 집배원끼리 서로 길을 찾아 건네는 법 | [adhocrouting-ko](docs/adhocrouting-ko.html) | [adhocrouting-en](docs/adhocrouting-en.html) |
| L4 스위치 | 창구 번호까지 보는 분류소 직원 | [l4switch-ko](docs/l4switch-ko.html) | [l4switch-en](docs/l4switch-en.html) |
| AMI(지능형 검침 인프라) | 계량기가 스스로 편지를 보내는 망 | [ami-ko](docs/ami-ko.html) | [ami-en](docs/ami-en.html) |
| V2X 차량 통신 | 트럭끼리 주고받는 쪽지 | [v2x-ko](docs/v2x-ko.html) | [v2x-en](docs/v2x-en.html) |
| 회선교환·패킷교환 | 전용 도로냐, 조각내 보내기냐 | [circuitpacket-ko](docs/circuitpacket-ko.html) | [circuitpacket-en](docs/circuitpacket-en.html) |
| OSI 7계층 | 7단계로 나뉜 배송 공정 | [osi7-ko](docs/osi7-ko.html) | [osi7-en](docs/osi7-en.html) |
| 전송계층 | 포트를 나누고 신뢰도를 고르는 단계 | [transportlayer-ko](docs/transportlayer-ko.html) | [transportlayer-en](docs/transportlayer-en.html) |
| SCTP | 한 계약, 여러 개의 전용 차선 | [sctp-ko](docs/sctp-ko.html) | [sctp-en](docs/sctp-en.html) |

### PPE·정보보안

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| ISMS/ISMS-P | 성 전체에 거는 인증 현판 | [ismsp-ko](docs/ismsp-ko.html) | [ismsp-en](docs/ismsp-en.html) |
| 개인정보 비식별·가명처리 | 번호표로 바꿔 달고, 진짜 이름은 다른 금고에 | [pseudonymize-ko](docs/pseudonymize-ko.html) | [pseudonymize-en](docs/pseudonymize-en.html) |
| 개인정보 안전성 확보조치·내부관리계획 | 손님 정보 창고의 전담 단속 수칙 | [privacysafeguard-ko](docs/privacysafeguard-ko.html) | [privacysafeguard-en](docs/privacysafeguard-en.html) |
| 양자암호통신 | 엿들으면 바로 티 나는 빛 알갱이 열쇠 | [qkdcomm-ko](docs/qkdcomm-ko.html) | [qkdcomm-en](docs/qkdcomm-en.html) |
| 블록체인 보안 고려사항 | 모두가 들고 다니는, 지문으로 이어 붙인 장부 | [bcsecurity-ko](docs/bcsecurity-ko.html) | [bcsecurity-en](docs/bcsecurity-en.html) |
| CPU 보안 취약점(Meltdown/Spectre) | 미리 짐작해서 일하다 생긴 흔적 | [cpuvuln-ko](docs/cpuvuln-ko.html) | [cpuvuln-en](docs/cpuvuln-en.html) |
| 국가 망 보안체계(N2SF) | 다리를 끊는 대신 검문소를 촘촘히 | [n2sf-ko](docs/n2sf-ko.html) | [n2sf-en](docs/n2sf-en.html) |
| 개인정보 보호강화기술(PET) | 손님을 지키는 여러 다른 도구상자 | [pet-ko](docs/pet-ko.html) | [pet-en](docs/pet-en.html) |
| 개인정보 안심구역 | 밖으로 못 들고 나가는 특별 열람실 | [safezone-ko](docs/safezone-ko.html) | [safezone-en](docs/safezone-en.html) |
| 동형암호 | 뜯지 않고 셈하는 봉인 편지 | [homoenc-ko](docs/homoenc-ko.html) | [homoenc-en](docs/homoenc-en.html) |
| 접근통제 모델 | 열쇠 주인을 정하는 세 가지 방식 | [accesscontrolppe-ko](docs/accesscontrolppe-ko.html) | [accesscontrolppe-en](docs/accesscontrolppe-en.html) |
| CBPR | 여러 나라가 같이 인정하는 통행 증명 | [cbpr-ko](docs/cbpr-ko.html) | [cbpr-en](docs/cbpr-en.html) |
| 마이데이터 | 내 장부는 내가 들고 다닐 권리 | [mydataSec-ko](docs/mydataSec-ko.html) | [mydataSec-en](docs/mydataSec-en.html) |
| CSAP | 빌린 창고에 찍는 왕의 안전 도장 | [csap-ko](docs/csap-ko.html) | [csap-en](docs/csap-en.html) |
| MAC/HMAC | 비밀 도장틀로 찍는 확인 도장 | [machmac-ko](docs/machmac-ko.html) | [machmac-en](docs/machmac-en.html) |
| BLP/Biba | 비밀은 안 새게, 거짓은 안 섞이게 — 사다리 두 규칙 | [blpbiba-ko](docs/blpbiba-ko.html) | [blpbiba-en](docs/blpbiba-en.html) |
| 공인인증서·사설인증 | 하나뿐이던 도장집, 이제는 여럿 | [pkicert-ko](docs/pkicert-ko.html) | [pkicert-en](docs/pkicert-en.html) |
| 데이터 3법 개정 | 세 권의 규칙서를 한 검사관 아래로 | [data3law-ko](docs/data3law-ko.html) | [data3law-en](docs/data3law-en.html) |
| PPDM | 이름은 가리고, 흐름은 보는 통계 조사관 | [ppdm-ko](docs/ppdm-ko.html) | [ppdm-en](docs/ppdm-en.html) |

### PPE·시스템SW

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| CPU 스케줄링 | 리프트에 누가 먼저 올라갈까 | [cpusched-ko](docs/cpusched-ko.html) | [cpusched-en](docs/cpusched-en.html) |
| 프로세스 동기화 | 리프트 열쇠는 하나뿐 | [syncprim-ko](docs/syncprim-ko.html) | [syncprim-en](docs/syncprim-en.html) |
| 캐시 메모리 | 바로 옆에 놓아둔 공구함 | [cachemem-ko](docs/cachemem-ko.html) | [cachemem-en](docs/cachemem-en.html) |
| 가상메모리·페이징 | 창고 전체를 내 것처럼 보여주는 가짜 지도 | [virtualmem-ko](docs/virtualmem-ko.html) | [virtualmem-en](docs/virtualmem-en.html) |
| 교착상태와 기아현상 | 서로의 열쇠를 기다리며 멈춘 정비공장 | [deadlockstarve-ko](docs/deadlockstarve-ko.html) | [deadlockstarve-en](docs/deadlockstarve-en.html) |
| GPU/GPGPU | 수백 명이 함께 움직이는 보조 정비팀 | [gpu-ko](docs/gpu-ko.html) | [gpu-en](docs/gpu-en.html) |
| 스택과 큐 | 상자는 쌓고, 차는 줄 세우고 | [stackqueue-ko](docs/stackqueue-ko.html) | [stackqueue-en](docs/stackqueue-en.html) |
| AI 가속기(TPU·NPU) | 오직 그 계산 하나만을 위한 전용 로봇팔 | [aiaccel-ko](docs/aiaccel-ko.html) | [aiaccel-en](docs/aiaccel-en.html) |
| 프로세스와 스레드 | 같은 차, 여러 손 | [processthread-ko](docs/processthread-ko.html) | [processthread-en](docs/processthread-en.html) |
| 이진트리·이진탐색트리 | 갈림길에서 반씩 줄여가는 선반 지도 | [bintree-ko](docs/bintree-ko.html) | [bintree-en](docs/bintree-en.html) |
| 알고리즘 복잡도(Big-O) | 차가 많아질 때 얼마나 느려질까 | [bigofunc-ko](docs/bigofunc-ko.html) | [bigofunc-en](docs/bigofunc-en.html) |
| 정렬 알고리즘 | 크기 순서로 차를 세우는 여러 방법 | [sortalgo-ko](docs/sortalgo-ko.html) | [sortalgo-en](docs/sortalgo-en.html) |
| 플래시 메모리 | 전원이 꺼져도 기억하는 부품 창고 | [flashmem-ko](docs/flashmem-ko.html) | [flashmem-en](docs/flashmem-en.html) |
| 인터럽트 처리 과정 | 벨이 울리면 적어두고 바로 달려가기 | [interruptproc-ko](docs/interruptproc-ko.html) | [interruptproc-en](docs/interruptproc-en.html) |
| BPR(업무 프로세스 재설계) | 정비 공정을 처음부터 다시 그리는 일 | [bpr-ko](docs/bpr-ko.html) | [bpr-en](docs/bpr-en.html) |
| HBM(고대역폭 메모리) | 엔진 바로 옆에 쌓은 공구탑 | [hbm-ko](docs/hbm-ko.html) | [hbm-en](docs/hbm-en.html) |
| 프로세스 메모리 구조 | 작업 공간을 구역으로 나눠 쓰는 규칙 | [memlayout-ko](docs/memlayout-ko.html) | [memlayout-en](docs/memlayout-en.html) |
| 유전 알고리즘 | 잘 나가는 다이얼 설정끼리 섞어보기 | [geneticalgo-ko](docs/geneticalgo-ko.html) | [geneticalgo-en](docs/geneticalgo-en.html) |
| CPU 파이프라인 | 여러 작업대에서 동시에 겹쳐 고치기 | [cpupipeline-ko](docs/cpupipeline-ko.html) | [cpupipeline-en](docs/cpupipeline-en.html) |
| 해시 알고리즘 | 번호만 계산해서 바로 칸을 짚기 | [hashalgo-ko](docs/hashalgo-ko.html) | [hashalgo-en](docs/hashalgo-en.html) |
| 차세대 비휘발성 메모리 | 지우지 않고 바로바로 바꿔 쓰는 새 창고들 | [nextnvm-ko](docs/nextnvm-ko.html) | [nextnvm-en](docs/nextnvm-en.html) |
| 최소신장트리(MST) | 가장 싼 배관만 골라 모든 지점 잇기 | [mstalgo-ko](docs/mstalgo-ko.html) | [mstalgo-en](docs/mstalgo-en.html) |
| 플래시 변환계층(FTL) | 덮어쓰지 않는 부품 창고 관리인 | [ftl-ko](docs/ftl-ko.html) | [ftl-en](docs/ftl-en.html) |
| 우선순위 역전/상속 | 급한 차가 유령처럼 멈춰요 | [priorityinv-ko](docs/priorityinv-ko.html) | [priorityinv-en](docs/priorityinv-en.html) |
| UNIX 시스템 | 정비소의 보이지 않는 운영자 | [unixsys-ko](docs/unixsys-ko.html) | [unixsys-en](docs/unixsys-en.html) |

### PPE·클라우드

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 클라우드 서비스 모델 | 뼈대만, 인테리어까지, 완제품 — 셋 중 골라 빌리기 | [cloudmodel-ko](docs/cloudmodel-ko.html) | [cloudmodel-en](docs/cloudmodel-en.html) |
| 가상머신(VM)과 컨테이너 | 독채 사무실과 칸막이 책상 | [vmcontainer-ko](docs/vmcontainer-ko.html) | [vmcontainer-en](docs/vmcontainer-en.html) |
| 공공부문 클라우드 활용 | 검증된 건물에만, 등급에 맞춰 입주하기 | [govcloud-ko](docs/govcloud-ko.html) | [govcloud-en](docs/govcloud-en.html) |
| 서버리스 컴퓨팅 | 쓸 때만 여는 시간제 회의실 | [serverless-ko](docs/serverless-ko.html) | [serverless-en](docs/serverless-en.html) |
| 엣지·포그 컴퓨팅 | 동네 가까운 지점과 그 사이 중간 허브 | [edgefog-ko](docs/edgefog-ko.html) | [edgefog-en](docs/edgefog-en.html) |
| SVM(서포트벡터머신) | 두 그룹을 가장 넓게 갈라놓는 선 | [svm-ko](docs/svm-ko.html) | [svm-en](docs/svm-en.html) |
| DAS/NAS/SAN | 내 서랍, 공용 자료실, 전용 창고망 | [dasnassan-ko](docs/dasnassan-ko.html) | [dasnassan-en](docs/dasnassan-en.html) |
| AI 데이터센터 | GPU만을 위한 전용 별관 | [aidc-ko](docs/aidc-ko.html) | [aidc-en](docs/aidc-en.html) |
| 블록·파일·오브젝트 스토리지 | 벽돌, 폴더 트리, 태그 붙은 박스 | [storagetype-ko](docs/storagetype-ko.html) | [storagetype-en](docs/storagetype-en.html) |
| 쿠버네티스(Kubernetes) | 자동 배정 배지의 그 유명한 제품 이름 | [k8s-ko](docs/k8s-ko.html) | [k8s-en](docs/k8s-en.html) |
| 멀티클라우드 | 여러 건물에 동시에 입주하기 | [multicloud-ko](docs/multicloud-ko.html) | [multicloud-en](docs/multicloud-en.html) |
| 스케일업/스케일아웃과 오토스케일 | 사무실을 키울까, 더 빌릴까 | [scaleupout-ko](docs/scaleupout-ko.html) | [scaleupout-en](docs/scaleupout-en.html) |

### PPE·신기술

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 디지털 트윈 | 화면 속 쌍둥이 로봇 | [digitaltwin-ko](docs/digitaltwin-ko.html) | [digitaltwin-en](docs/digitaltwin-en.html) |
| 엣지 컴퓨팅 | 바로 옆에서 계산하는 작은 서버 | [edgecompute-ko](docs/edgecompute-ko.html) | [edgecompute-en](docs/edgecompute-en.html) |
| 스마트팩토리 | 스스로를 지켜보는 공장 | [smartfactory-ko](docs/smartfactory-ko.html) | [smartfactory-en](docs/smartfactory-en.html) |
| 퍼블릭·프라이빗 블록체인 | 펼친 장부와 자물쇠 장부 | [bcpublicprivate-ko](docs/bcpublicprivate-ko.html) | [bcpublicprivate-en](docs/bcpublicprivate-en.html) |
| 블록체인 기술요소·보안 | 지문으로 이어진 장부 | [bctech-ko](docs/bctech-ko.html) | [bctech-en](docs/bctech-en.html) |
| 스마트시티 | 함께 숨 쉬는 도시 모형 | [smartcity-ko](docs/smartcity-ko.html) | [smartcity-en](docs/smartcity-en.html) |
| 메타버스 | 아바타들이 모인 가상 전시관 | [metaverse-ko](docs/metaverse-ko.html) | [metaverse-en](docs/metaverse-en.html) |
| 가상현실(VR) | 눈앞 전체를 바꾸는 헤드셋 | [vrtech-ko](docs/vrtech-ko.html) | [vrtech-en](docs/vrtech-en.html) |
| 모바일 엣지 컴퓨팅(MEC) | 기지국 옆에 붙은 작은 서버 | [mec-ko](docs/mec-ko.html) | [mec-en](docs/mec-en.html) |
| 오류 제어(ARQ) | 틀렸으니 다시 보내달라고 외치기 | [arq-ko](docs/arq-ko.html) | [arq-en](docs/arq-en.html) |
| 마이데이터(MyData) | 흩어진 서랍을 내가 한곳에 모으기 | [mydataTech-ko](docs/mydataTech-ko.html) | [mydataTech-en](docs/mydataTech-en.html) |
| 안티드론 | 하늘의 불청객을 찾아 막는 삼단계 | [antidrone-ko](docs/antidrone-ko.html) | [antidrone-en](docs/antidrone-en.html) |
| 양자키분배(QKD) | 엿보면 반드시 들통나는 빛의 열쇠 | [qkdtech-ko](docs/qkdtech-ko.html) | [qkdtech-en](docs/qkdtech-en.html) |
| 앰비언트 컴퓨팅 | 말 안 해도 알아서 척척인 전시관 | [ambientcompute-ko](docs/ambientcompute-ko.html) | [ambientcompute-en](docs/ambientcompute-en.html) |
| RPA | 규칙대로만 반복하는 로봇 직원 | [rpa-ko](docs/rpa-ko.html) | [rpa-en](docs/rpa-en.html) |
| 드론 보안위협 | 보이지 않는 줄로 매달린 드론 | [dronesecurity-ko](docs/dronesecurity-ko.html) | [dronesecurity-en](docs/dronesecurity-en.html) |
| 스마트팜 | 센서가 돌보는 온실 부스 | [smartfarm-ko](docs/smartfarm-ko.html) | [smartfarm-en](docs/smartfarm-en.html) |
| 양자 컴퓨팅 | 동시에 앞뒤인 신기한 동전 부스 | [quantumcompute-ko](docs/quantumcompute-ko.html) | [quantumcompute-en](docs/quantumcompute-en.html) |
| NFT | 그림에 붙이는 위조 못 하는 증명서 | [nft-ko](docs/nft-ko.html) | [nft-en](docs/nft-en.html) |
| LiDAR | 레이저로 거리를 재는 회전하는 눈 | [lidar-ko](docs/lidar-ko.html) | [lidar-en](docs/lidar-en.html) |
| 정량적 위험분석 기법 | 위험을 숫자 하나로 적는 전광판 | [quantrisk-ko](docs/quantrisk-ko.html) | [quantrisk-en](docs/quantrisk-en.html) |
| 자율주행 | 운전석이 비어 있는 시연 트랙의 차 | [autodrive-ko](docs/autodrive-ko.html) | [autodrive-en](docs/autodrive-en.html) |
| 사이버물리시스템(CPS) | 화면 속 쌍둥이와 함께 움직이는 기계팔 | [cps-ko](docs/cps-ko.html) | [cps-en](docs/cps-en.html) |
| 4차 산업혁명 | 전시장 모든 부스를 잇는 하나의 흐름 | [fourthindustry-ko](docs/fourthindustry-ko.html) | [fourthindustry-en](docs/fourthindustry-en.html) |
| 핀테크·간편결제 | 나가는 길, 폰 하나로 찍는 매표소 | [fintech-ko](docs/fintech-ko.html) | [fintech-en](docs/fintech-en.html) |

### PPE·IT관리

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| IT 투자성과 평가 | 공연 끝난 뒤의 성적표 | [itinvesteval-ko](docs/itinvesteval-ko.html) | [itinvesteval-en](docs/itinvesteval-en.html) |
| 프로젝트 위험관리 | 비 오는 날에도 챙기는 우산 | [projrisk-ko](docs/projrisk-ko.html) | [projrisk-en](docs/projrisk-en.html) |
| SLA/SLM | 공연을 보장하는 티켓 | [slappe-ko](docs/slappe-ko.html) | [slappe-en](docs/slappe-en.html) |
| 협상에 의한 계약·제안서 평가 | 조건을 조율해 서명하기 | [negotiation-ko](docs/negotiation-ko.html) | [negotiation-en](docs/negotiation-en.html) |
| ESG 경영과 IT | 환경·사회·투명성까지 챙기는 투어 | [esgit-ko](docs/esgit-ko.html) | [esgit-en](docs/esgit-en.html) |
| BCP(업무 연속성 계획) | 정전에도 멈추지 않는 투어 | [bcpplan-ko](docs/bcpplan-ko.html) | [bcpplan-en](docs/bcpplan-en.html) |
| WBS(작업분류체계) | 공연 준비를 쪼갠 체크리스트 | [wbsppm-ko](docs/wbsppm-ko.html) | [wbsppm-en](docs/wbsppm-en.html) |
| 정보시스템 운영 성과관리 | 공연 끝난 뒤의 운영실 | [opsperf-ko](docs/opsperf-ko.html) | [opsperf-en](docs/opsperf-en.html) |

### PPE·법제도

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| 오픈소스 라이선스 | 다 같이 쓰는 준비물 규칙 라벨 | [osslicense-ko](docs/osslicense-ko.html) | [osslicense-en](docs/osslicense-en.html) |
| 정보시스템 하드웨어 규모산정 | 축제 준비물 개수 미리 정하기 | [hwsizing-ko](docs/hwsizing-ko.html) | [hwsizing-en](docs/hwsizing-en.html) |
| 망중립성 | 급식 줄은 다 똑같이 서야 해요 | [netneutral-ko](docs/netneutral-ko.html) | [netneutral-en](docs/netneutral-en.html) |
| ISO/IEC 25000(SQuaRE) | 좋은 준비물의 기준표 | [iso25000-ko](docs/iso25000-ko.html) | [iso25000-en](docs/iso25000-en.html) |
| 맨체스터 부호화 | 박자를 스스로 알려주는 신호 | [manchestercode-ko](docs/manchestercode-ko.html) | [manchestercode-en](docs/manchestercode-en.html) |
| ISO/IEC 42001 | AI도 규칙대로 쓰는지 도장 찍기 | [iso42001-ko](docs/iso42001-ko.html) | [iso42001-en](docs/iso42001-en.html) |
| 공공데이터 제공과 품질 | 공지 게시판에 다 보이게 붙이기 | [opendataqual-ko](docs/opendataqual-ko.html) | [opendataqual-en](docs/opendataqual-en.html) |
| 관계 무결성 제약 | 출석부에 없는 이름은 반장이 될 수 없어요 | [refintegrity-ko](docs/refintegrity-ko.html) | [refintegrity-en](docs/refintegrity-en.html) |
| AI 윤리·법적 이슈 | AI가 사고 치면 누가 책임져요? | [aiethicslaw-ko](docs/aiethicslaw-ko.html) | [aiethicslaw-en](docs/aiethicslaw-en.html) |
| 슈퍼앱 | 학생증 하나로 다 되는 앱 | [superapp-ko](docs/superapp-ko.html) | [superapp-en](docs/superapp-en.html) |
| 데이터 표준화 | 전교가 함께 쓰는 공통 기준표 | [datastd-ko](docs/datastd-ko.html) | [datastd-en](docs/datastd-en.html) |
| 위험·안전성 분석(FTA/FMEA/HAZOP) | 사고를 거꾸로, 또는 미리 훑어보기 | [riskanalysis-ko](docs/riskanalysis-ko.html) | [riskanalysis-en](docs/riskanalysis-en.html) |
| 지능정보화 기본법 | 학교 전체의 디지털 생활을 아우르는 기본 헌장 | [intellinfolaw-ko](docs/intellinfolaw-ko.html) | [intellinfolaw-en](docs/intellinfolaw-en.html) |
| 페이징·세그멘테이션 | 창고를 나누는 두 가지 다른 방식 | [pagingseg-ko](docs/pagingseg-ko.html) | [pagingseg-en](docs/pagingseg-en.html) |
| 디지털 증거수집의 법적 절차 | 정당하게 거뒀는가를 따지는 절차 | [forensiclaw-ko](docs/forensiclaw-ko.html) | [forensiclaw-en](docs/forensiclaw-en.html) |
| UN 전자정부 평가(EGDI) | 같은 잣대로 모든 학교를 재는 평가단 | [egdi-ko](docs/egdi-ko.html) | [egdi-en](docs/egdi-en.html) |
| 기능안전 표준(ISO 26262·IEC 61508) | 안전 등급을 매기는 공통 규칙서 | [funcsafetystd-ko](docs/funcsafetystd-ko.html) | [funcsafetystd-en](docs/funcsafetystd-en.html) |
| 경사하강법 | 안개 낀 산을 한 걸음씩 내려가기 | [gradientdescent-ko](docs/gradientdescent-ko.html) | [gradientdescent-en](docs/gradientdescent-en.html) |
| 분할정복·탐욕법·동적계획법 | 쪼개고, 급한 것부터, 기억해두고 | [algoparadigm-ko](docs/algoparadigm-ko.html) | [algoparadigm-en](docs/algoparadigm-en.html) |
| 레그테크(RegTech) | 흩어진 규칙판을 한꺼번에 대조하는 자동 검사기 | [regtech-ko](docs/regtech-ko.html) | [regtech-en](docs/regtech-en.html) |

## 구조

```
terms/<분야>/<slug>.py   원본. 한 파일에 한글·영문을 같이 적는다 — 문장은 (ko, en) 튜플, SVG 글자는 ⟦ko|en⟧
terms/_draw.py           같이 쓰는 SVG 조각 (사람, 성, 개, 말풍선, 방패 …)
build.py                 terms/ → docs/*-ko.html, docs/*-en.html, docs/index.html
.github/ISSUE_TEMPLATE/  용어 요청 양식
.github/workflows/       이슈 → Claude Code → PR 자동화
```

```bash
python3 build.py
```

의존성 없음. **`docs/*.html` 은 생성물이라 직접 고치지 말 것** — `terms/` 를 고치고 다시 빌드한다.

### 분야 (카테고리)

분야는 `terms/` 아래 폴더 이름이고, `build.py` 의 `CATEGORIES` 에 한글·영문 이름을 등록한다.
목록 페이지에는 검색창(제목·용어·원어로 찾기)이 있고, 맨 위 분야 탭으로 나뉘며, 탭 안에서 10개씩 페이지로 나눠 보여준다(`#cat=<폴더>&page=N`, `build.py` 의 `PER_PAGE`). "다음 이야기" 링크는 같은 분야 안에서만 돈다.

```python
CATEGORIES = {
    "security": ("보안", "Security"),
    "design": ("소프트웨어 설계", "Software Design"),
    "ai": ("AI", "AI"),
    "sre": ("SRE", "SRE"),
    "llmsec": ("AI 보안", "AI Security"),
    "ppeswe": ("SW공학", "SW Eng"),
    "ppedata": ("DB/데이터", "Database"),
    "ppeai": ("AI이론", "AI Theory"),
    "ppenet": ("네트워크", "Network"),
    "ppesec": ("정보보안", "InfoSec"),
    "ppesys": ("시스템SW", "Systems"),
    "ppecloud": ("클라우드", "Cloud"),
    "ppetech": ("신기술", "Emerging Tech"),
    "ppepm": ("IT관리", "IT Mgmt"),
    "ppelaw": ("법제도", "Law/Policy"),
}
```

새 분야: 폴더를 만들고 위에 한 줄 추가.

### 페이지 한 장의 구성

1. 제목 — `<em>용어</em>가 뭐예요?`
2. 그림 패널 3~5장 — 큰 SVG 한 장 + 한 문장 + 작은 부연. 필요하면 카드 2~4개나 말풍선
3. 한 줄 요약 (어두운 상자)
4. "어른들은 이렇게 불러요" — 쉬운 말 → 원어 대응표
5. 다음 이야기 링크, 용어 요청 링크

### 새 용어 추가

`terms/<분야>/<slug>.py` 를 만들고 `PAGE` 딕셔너리에 `slug`, `order`, `title`, `h1`, `sub`, `panels`, `summary`, `glossary` 를 채운다. 기존 파일 하나를 복사해서 시작하면 된다. 절차는 아래 스킬에 있다.

## 작성 원칙

- 쉬움을 위해 사실을 왜곡하지 않는다.
- 비유는 하나만 쓰고, 그 비유가 깨지는 지점을 함께 밝힌다. (발자국 → "신발을 바꾸면 발자국도 바뀐다")
- 전문 용어는 쉬운 말로 먼저 쓰고 원어를 병기한다 — 나중에 검색할 수 있어야 한다.
- 어휘를 낮추는 것이지, 읽는 사람을 낮추는 것이 아니다.

## 스킬

`.claude/skills/picture-book/` — 분야에 상관없이 그림책 용어집을 만드는 일반화 스킬 (세계관 설계 `references/world-design.md`, 대량 작성 루프 `references/batch-loop.md`, 스크립트 `validate.py`·`render_qa.py`·`update_tables.py`·`coverage_audit.py`). 분야별 세계관은 `terms/<분야>/_WORLD.md`.
`.claude/skills/eli5/SKILL.md` — 보안 분야의 구체 예시. 새 용어를 위 그림책 형식으로 만드는 절차 (분야 정하기 → 비유 고르기 → 패널 3~5장 → `_draw.py` 조각으로 그리기 → `terms/<분야>/<slug>.py` → 빌드·점검). 위 문서들이 이 스킬의 결과물이다. 다른 프로젝트에서 쓰려면 디렉터리를 복사한다.

```bash
cp -r .claude/skills/eli5 ~/.claude/skills/
```
