# explaineasily

어려운 용어를 **그림책**으로. 글은 적게, 그림은 크게, 다섯 살 눈높이로.

배포: https://explaineasily.metacog.co.kr (GitHub Pages, `main` 브랜치의 `/docs` 폴더, `docs/CNAME`)

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
