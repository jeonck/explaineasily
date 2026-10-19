# AI 보안 세계관: 주문받는 주방

## 무대
- 주방 = AI 모델이 돌아가는 서비스. 주방장 = AI 모델(LLM). 손님 = 요청을 보내는 사람/시스템.
- 주문서 = 프롬프트. 완성된 요리(접시) = 모델 출력. 재료 창고 = 학습 데이터 + 외부에서 들여오는 모델/플러그인(공급망).
- 맛보기 검수대 = 가드레일(출력 필터). 비밀 레시피북 = 모델 가중치/시스템 프롬프트. 잠긴 칼 서랍 = 도구(함수 호출) 샌드박스.
- 위생 검사관 = AI 레드팀/보안 감사관. 사장님 = 거버넌스 책임자(최종 승인권자). 견습생(심부름꾼) = 자율 에이전트.
- 배경: 낮 `sky()` = 평상시 영업, `bad-soft` = 공격·사고 패널, `good-soft` = 막아내거나 고친 패널. `night()` 는 몰래 하는 공격(모델 추출, 섀도 AI)에 써도 된다.
- 긴장: 주방장은 **손님이 시키는 대로 요리하는 게 본능**이다 — 주문서에 적힌 대로 믿고 따른다. 그래서 "진짜 손님의 부탁"과 "몰래 끼운 나쁜 부탁"을 글만 보고는 잘 구분하지 못한다. 이게 다른 보안 분야와 다른 지점.

## 등장인물 (헬퍼는 `terms/llmsec/_world.py`)
| 인물 | 그림 | 실제 |
|---|---|---|
| 주방장 | `person(..., **CHEF)` 흰 모자 | AI 모델 (LLM) |
| 손님 | `person(..., **GUEST)` | 정상 사용자 / 정상 요청 |
| 몰래 쪽지 끼우는 손님 | `person(..., **SNEAK)` 어두운 색 | 공격자 (프롬프트 인젝션 등) |
| 맛보기 검수원 | `person(..., **TASTER)` 초록 | 가드레일 / 출력 필터 |
| 위생 검사관 | `person(..., **INSPECTOR)` + `badge()` | AI 레드팀 / 보안 감사관 |
| 사장님 | `person(..., **MANAGER)` 보라 | 거버넌스 책임자 / 최종 승인자 |
| 견습생 | `person(..., **RUNNER)` 파란 모자 | 자율 에이전트 / 도구 호출 |
| 재료 공급업체 | `person(..., **SUPPLIER)` 갈색 | 모델/데이터 공급망 (오픈 웨이트, 서드파티 플러그인) |

## 소품 = 개념 (헬퍼 함수)
| 소품 | 헬퍼 | 실제 | 처음 쓴 페이지 |
|---|---|---|---|
| 주문서 (뒤에 빨간 쪽지 삐져나오면 sneaky) | `ticket()` | 프롬프트 / 몰래 끼운 명령 | llmthreats |
| 완성된 요리(접시) | `dish()` | 모델 출력 | llmthreats |
| 재료 창고 선반 | `pantry()` | 학습 데이터 / 모델 공급망 | datapoisoning |
| 비밀 레시피북 | `recipebook()` | 모델 가중치 / 시스템 프롬프트 | promptleak |
| 잠긴 칼 서랍 | `knifedrawer()` | 도구(함수 호출) 샌드박스 | toolsandbox |
| 비상벨 | `bell()` | AI 사고 대응 | aiincident |
| 주문 기록 장부 | `logbook()` | 감사 로그 | aiaudit |
| 안내판 / 규칙판 | `board()` | 정책/문서 (사이트 공통 크림색 스타일) | aigovernance |
| 위생 검사관 배지 | `badge()` | 레드팀 / 감사 | airedteam |
| 표식/도장 | `stamp()` | 워터마크 / 출처 인증 | watermark |

## 깨지는 곳 (패널 ⑤ 필수)
- 주방장은 "거짓말을 하려는" 게 아니다 — 모르면서도 그럴듯하게 이어 붙이는 버릇이 있을 뿐이다(→ `ai` 세계의 `hallucination` 과 같은 뿌리, 다른 얼굴: 여기서는 "위험한 요리를 자신 있게 내놓는 것"이 문제).
- 사람 주방장은 "이 주문 이상한데?"를 경험으로 눈치채지만, AI 주방장은 글자만 본다 — 그래서 쪽지를 아주 그럴듯하게 꾸미면(인코딩, 역할극) 매번 속을 수 있다. "한 번 막았다"가 "항상 막힌다"를 보장하지 않는다.
- 위생 검사관(레드팀)이 통과시켜도 완벽하지 않다 — 검사관이 생각 못 한 새 쪽지 문구는 여전히 통할 수 있다.

## 다른 세계와의 다리
- `ai`(앵무새) 세계의 `prompt`/`agent`/`rag`/`toolcall`/`guardrail`/`hallucination`/`finetune`/`pretraining`/`aiprivacy` 는 AI가 **어떻게 동작하는지**를 설명한다. 이 세계(`llmsec`)는 그 동작을 **누가 악용하거나 어떻게 망가지는지**를 다룬다 — 겹치는 용어는 서로 링크하고 새로 쓰지 않는다.
- `security`(성) 세계의 `aisec`(이 분야 전체의 첫 소개였던 페이지)·`injection`·`redteam`·`sandbox`·`supplychain`·`sbom`·`apisec`·`openweights` 는 **일반 보안** 개념이다. `llmsec` 의 각 페이지는 "AI/LLM에 적용하면 구체적으로 이렇게 다르다"를 보여주고 그 일반 개념 페이지로 링크한다 (중복 설명 금지).
- `sre`(놀이공원) 세계의 `incidentcommand`/`postmortem`/`runbook`/`observability` 와 역할이 비슷한 짝(`aiincident`/`aiaudit`)이 있다 — 이름이 비슷해도 다른 세계이므로 소품을 혼용하지 않는다.

## 이미 쓴 비유 (order 순)
| slug | 챕터 | 제목 |
|---|---|---|
| llmthreats | ① 프롬프트 공격 | 다 받아주는 주방 |
| promptinjection | ① 프롬프트 공격 | 주문서 뒤에 몰래 끼운 쪽지 |
| indirectinjection | ① 프롬프트 공격 | 재료 포장지에 적힌 몰래 쪽지 |
| jailbreak | ① 프롬프트 공격 | 주방장을 구슬려 규칙을 깨게 하기 |
| promptleak | ① 프롬프트 공격 | 비밀 레시피 수칙을 캐내기 |
| promptevasion | ① 프롬프트 공격 | 암호처럼 꼬아 쓴 주문서 |
| imageinjection | ① 프롬프트 공격 | 메뉴판 사진 속에 숨긴 글자 |
| adversarialexample | ② 모델 공격 | 눈속임 그림 주문서 |
| modelextraction | ② 모델 공격 | 레시피북 통째로 베껴가기 |
| modelinversion | ② 모델 공격 | 접시 더미에서 되살린 얼굴 |
| membershipinference | ② 모델 공격 | 눈 감고도 만드는 요리 |
| memorization | ② 모델 공격 | 그대로 베낀 접시 |
| datapoisoning | ② 모델 공격 | 수상한 재료 자루 |
| ragpoisoning | ② 모델 공격 | 참고 카드함에 끼운 가짜 카드 |
| backdoor | ② 모델 공격 | 숨겨진 암호 주문어 |
| trojanmodel | ② 모델 공격 | 다듬는 중에 몰래 심은 버릇 |
| excessiveagency | ③ 에이전트·도구 | 너무 많은 열쇠를 받은 견습생 |
| unsafeoutput | ③ 에이전트·도구 | 접시를 그대로 기계에 넣다가 |
| zeroclick | ③ 에이전트·도구 | 가만히 있어도 실행되는 공격 |
| toolsandbox | ③ 에이전트·도구 | 잠긴 칼 서랍 |
| toolpermission | ③ 에이전트·도구 | 도구별 권한 배지 |
| llmdos | ③ 에이전트·도구 | 화구를 멈추지 않는 주문 |
| aibom | ④ 공급망·투명성 | 재료 출처 인증서 |
| modelcard | ④ 공급망·투명성 | 요리 설명표 |
| watermark | ④ 공급망·투명성 | 요리에 새긴 표식 |
| airedteam | ⑤ 거버넌스·운영 | 위생 검사관의 불시 방문 |
| safetyeval | ⑤ 거버넌스·운영 | 손님 받기 전 맛 평가 테스트 |
| humanapproval | ⑤ 거버넌스·운영 | 사장님 최종 승인 |
| aigovernance | ⑤ 거버넌스·운영 | 주방 규칙판 |
| shadowai | ⑤ 거버넌스·운영 | 몰래 들여온 배달 상자 |
| aiincident | ⑤ 거버넌스·운영 | 울리는 비상벨 |
| aiaudit | ⑤ 거버넌스·운영 | 매일 적는 주문 기록 장부 |
