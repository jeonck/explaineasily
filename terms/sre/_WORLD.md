# SRE 세계관: 쉬지 않는 놀이공원

## 무대
- 공원 = 우리가 운영하는 서비스/시스템. 놀이기구 = 각각의 서비스·애플리케이션. 손님 = 요청(트래픽).
- 대기줄 = 요청 큐. 매표 창구 = API 진입점. 관제실 = 모니터링/관측 센터.
- 공원 지도 = 시스템 아키텍처. 쌍둥이 공원(다른 도시) = 다른 리전.
- 배경: 낮 `sky()` = 평상시 운영, `bad-soft` = 장애·문제 패널, `good-soft` = 해결·정상. `night()` 는 보통 안 쓰되, 한밤의 온콜 호출 장면엔 써도 된다.
- 긴장: 공원은 하루도 닫으면 안 된다 — 손님은 계속 오고, 기구는 계속 고장 날 수 있다. "완벽하게 안 고장"이 아니라 "고장 나도 손님이 못 느끼게"가 목표.

## 등장인물 (헬퍼는 `terms/sre/_world.py`)
| 인물 | 그림 | 실제 |
|---|---|---|
| 관제실 요원 | `person(..., **OPERATOR)` 초록 | SRE / 온콜 엔지니어 |
| 정비사 | `person(..., **MECHANIC)` 노란 모자 + `WRENCH` | 개발자 / 배포 담당 |
| 공원장 | `person(..., **MANAGER)` 보라 | 제품 책임자 / 경영진 / 손님과의 약속 당사자 |
| 신참 정비사 | `person(..., **ROOKIE)` 파란 모자 | 새 코드 / 카나리 배포 대상 |
| 손님 | `person(..., hat=FOLK[i][0], shirt=FOLK[i][1])` | 사용자 요청 (트래픽) |

## 소품 = 개념 (헬퍼 함수)
| 소품 | 헬퍼 | 실제 | 처음 쓴 페이지 |
|---|---|---|---|
| 놀이기구 | `ride()` | 서비스/애플리케이션 | reliability |
| 매표 창구 | `booth()` | API 진입점 / 엔드포인트 | reliability |
| 대기줄 | `queueline()` | 요청 큐 / 트래픽 | reliability |
| 관제실 화면 | `controlroom()` | 모니터링 대시보드 | goldensignals |
| 계기판 바늘 | `gauge()` | 지표 값 (레이턴시·에러율 등) | goldensignals |
| 무전기 | `walkie()` | 알림/페이징 | alerting |
| 빨간 비상 버튼 | `bigbutton()` | 서킷 브레이커 | circuitbreaker |
| 여분 부품 창고 | `shed()` | 백업/리던던시 | failover |
| 쌍둥이 공원 | `minipark()` | 다른 리전 | multiregion |
| 티켓 | `ticket()` | 요청 식별자 / 멱등 키 | idempotency |
| 안내판·메모판 | `board()` | 문서/장부/정책 (사이트 공통 크림색 스타일) | 전반 |

## 깨지는 곳 (패널 ⑤ 필수)
- "완벽히 안 고장"은 목표가 아니다 — 고장이 **손님에게 안 보이게** 하는 것이 목표. 100% 가동은 현실에 없고, 그걸 추구하면 비용이 무한대로 든다(→slo, →errorbudget).
- 사람(관제실)이 다 보는 건 못 한다 — 규모가 커지면 자동화(→autoscaling, →orchestration)가 사람을 대신한다. 그래도 마지막 판단은 사람(→incidentcommand, →postmortem).

## 보안·AI 세계와의 다리
- `failover`/`backup`(보안 세계 `backup.py` 여분 상자)와 소품이 비슷하지만 SRE는 "서비스 지속"이 목적, 보안은 "데이터 보존"이 목적 — 혼동하지 않게 ⑤에서 구분.
- `ratelimiting`은 보안의 `ddos`/`waf`와 다르다 — 보안은 공격자를 막고, SRE는 **우리 시스템 자신을 보호**한다.

| slug | 단계 | 제목 |
|---|---|---|
| reliability | Plan | 쉬지 않는 공원을 돌보는 사람들 |
| sli | Plan | 오늘 운행 기록판 |
| slo | Plan | 우리끼리 정한 목표 줄 |
| sla | Plan | 손님과 맺은 약속 계약서 |
| errorbudget | Plan | 허용된 고장 티켓 묶음 |
| capacityplanning | Plan | 내년 손님 수를 미리 세어보기 |
| apigateway | Plan | 정문 안내소 |
| servicemesh | Plan | 기구 사이 전용 통로 |
| caching | Plan | 자주 묻는 질문 미리 적어둔 메모판 |
| sharding | Plan | 번호별로 나뉜 매표 창구 |
| replication | Plan | 손님 명부를 두 창고에 똑같이 |
| consensus | Plan | 여러 관제실이 손 들어 정하기 |
| splitbrain | Plan | 두 관제실이 서로 자기가 진짜라고 |
| captheorem | Plan | 정확함과 항상 열림, 둘 다는 못 가져요 |
| eventualconsistency | Plan | 조금 늦게 맞춰지는 재고판 |
| multiregion | Plan | 쌍둥이 공원 |
| iac | Plan | 설계도 한 장으로 공원 통째로 짓기 |
| gitops | Plan | 설계도가 바뀌면 자동으로 공사 |
| ratelimiting | Do | 한 번에 몇 명까지만 |
| healthcheck | Do | 안전바 딸깍 확인 |
| servicediscovery | Do | 지금 열린 창구 안내판 |
| orchestration | Do | 몇 대를 켤지 정하는 운영 본부 |
| messagequeue | Do | 주문서를 쌓아두는 바구니 |
| deadletterqueue | Do | 아무도 안 찾아간 바구니함 |
| backpressure | Do | 입구를 잠깐 막기 |
| bulkhead | Do | 불이 안 번지게 나눈 구역 |
| circuitbreaker | Do | 고장나면 누르는 빨간 버튼 |
| retrybackoff | Do | 잠깐 쉬었다 다시 줄서기 |
| idempotency | Do | 같은 티켓으로 두 번 못 타요 |
| autoscaling | Do | 줄이 길어지면 직원을 더 부르기 |
| gracefuldegradation | Do | 일부만 고장나도 나머지는 그대로 |
| failover | Do | 발전기가 꺼지면 예비 발전기가 |
| featureflag | Do | 새 기구에 친 커튼 |
| canary | Do | 구석에서 몰래 하는 시험 운행 |
| bluegreen | Do | 쌍둥이 기구를 번갈아 운영 |
| rollback | Do | 이상하면 바로 어제 버전으로 |
| goldensignals | Check | 관제실의 계기판 네 개 |
| observability | Check | 세 가지로 들여다보기 |
| alerting | Check | 몇 번 울려야 진짜 비상인가 |
| chaosengineering | Check | 일부러 내는 가짜 고장 |
| gameday | Check | 가짜 화재 훈련일 |
| dorametrics | Check | 우리 공사팀 네 가지 성적표 |
| oncall | Act | 이번 주 호출기를 든 사람 |
| incidentcommand | Act | 지휘봉을 든 사람 |
| runbook | Act | 정비사의 공책 |
| postmortem | Act | 탓하지 않고 모여 쓰는 기록 |
| toil | Act | 매일 똑같이 반복하는 허드렛일 |
