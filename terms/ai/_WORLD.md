# AI 세계관: 말 잘하는 앵무새 키우기

## 무대
- 앵무새 학교 = 모델을 만들고 가르치는 곳 (학습·평가·파인튜닝)
- 우리 집 = 모델을 쓰는 곳 (프롬프트·컨텍스트·에이전트)
- 도서관 = 앵무새가 모르는 걸 사서가 찾아 읽어주는 곳 (RAG·임베딩·벡터 DB)
- 공방 = 앵무새에게 도구를 쥐여주는 곳 (도구 호출·에이전트·MCP)
- 긴장: 앵무새는 뜻을 아는 게 아니라 **다음 말을 잘 이어 붙이는 새** — 잘 시키면 놀랍고, 잘못 시키면 그럴듯한 거짓말을 한다.
- 배경: 낮 `sky()` = 평상시, `bad-soft` = 잘못된 사용/오해 패널, `good-soft` = 해결. `night()` 는 안 쓴다(밤 = 보안 세계의 공격).

## 등장인물 (헬퍼는 `terms/ai/_world.py`)
| 인물 | 그림 | 실제 |
|---|---|---|
| 파란 앵무새 | `parrot(x, y)` 색 PARROT | LLM / 우리 모델 (보안 `aisec` 의 파란 앵무새와 같은 새) |
| 큰 앵무새 / 작은 앵무새 | `parrot(..., s=1.3)` / `s=0.7` | 파라미터가 많은 모델 / 작은 모델 |
| 그럴듯 앵무새 | `parrot(..., color=PARROT_BAD)` + 빨간 말풍선 | 할루시네이션 (자신 있게 틀린 답) |
| 조련사 | `person(..., **TRAINER)` 초록 | 개발자, 프롬프트 쓰는 사람 |
| 사서 | `person(..., **LIBRARIAN)` 회색 + 책 | 검색기 (RAG) |
| 시험관 | `person(..., **EXAMINER)` 노란 모자 + 채점표 | 평가·벤치마크 |
| 손님 | `person(..., **GUEST)` 보라 옷 | 최종 사용자 |

## 소품 = 개념
| 소품 | 헬퍼 | 실제 | 처음 쓴 페이지 |
|---|---|---|---|
| 책 더미 (읽은 양) | `books()` | 학습 데이터 / 사전 학습 | llm |
| 콩 (낱말 조각) | `bean()`, `beans()` | 토큰 | token |
| 조련 쪽지 | `note()` | 프롬프트 / 시스템 프롬프트 | prompt |
| 예시 카드 | `note()` 작은 것 | few-shot | prompt |
| 쟁반 (한 번에 올릴 수 있는 콩 수) | `tray()` | 컨텍스트 창 | context |
| 말풍선 (빨간 테두리 = 거짓말) | `bubble_parrot(bad=True)` | 할루시네이션 | hallucination |
| 낱말마다 붙은 좌표 딱지 | — | 임베딩 | embedding |
| 딱지로 정리한 서가 | — | 벡터 DB | vectordb |
| 사서가 찾아온 페이지를 쟁반에 올림 | — | RAG | rag |
| 짧은 특훈 | — | 파인튜닝 | finetune |
| 잘했을 때 주는 간식 | — | RLHF / 보상 | rlhf |
| 엉뚱함 다이얼 | `dial()` | temperature | temperature |
| 도구 상자 (계산기·달력·전화) | — | 함수 호출 / 도구 | toolcall |
| 도구 상자 규격 | — | MCP | mcp |
| 심부름 목록을 스스로 짜는 앵무새 | — | 에이전트 | agent |
| 앵무새 여러 마리 회의 | — | 멀티에이전트 | multiagent |
| 울타리 | — | 가드레일 | guardrail |
| 답하기 전 혼자 중얼거리기 | `parrot(mood="think")` | 추론 모델 / chain of thought | reasoning |

## 깨지는 곳 (패널 ⑤ 필수)
- 앵무새는 "이해"하지 않는다 — 그런데 사람보다 잘 푸는 문제가 있다. 첫 페이지 `llm` 에서 명시.
- 도구 비유: 앵무새가 도구를 직접 쓰는 게 아니라 "도구를 써 달라는 쪽지"를 쓰고 조련사(런타임)가 실행한다.
- 콩 비유: 콩 하나가 낱말 하나가 아니다 (긴 낱말은 콩 여러 개, 한글은 더 잘게).

## 보안 세계와의 다리
- `aisec` (보안): 도둑이 기른 앵무새·프롬프트 인젝션 → 이 분야의 `guardrail`, `agent` 에서 링크.
- `injection` (보안): 쪽지에 숨긴 명령 → `prompt` 의 ⑤에서 링크.

## 이미 쓴 비유 (order 순)
| slug | 제목 |
|---|---|
| llm | 책을 산더미로 읽은 앵무새 |
| token | 앵무새가 말을 콩으로 세요 |
| prompt | 앵무새에게 주는 조련 쪽지 |
| context | 앵무새 앞의 쟁반 |
| hallucination | 그럴듯 앵무새 |
| finetune | 짧은 특훈 |
| embedding | 낱말마다 좌표 딱지 |
| vectordb | 딱지로 정리한 서가 |
| rag | 사서가 찾아온 페이지 |
| memory | 앵무새의 수첩 |
| temperature | 엉뚱함 다이얼 |
| promptcaching | 미리 놓아둔 콩 |
| structuredoutput | 정해진 칸에 쓰기 |
| streaming | 콩을 하나씩 바로 보여주기 |
| toolcall | 도구 상자 |
| agent | 심부름 목록을 스스로 짜는 앵무새 |
| mcp | 도구 상자 규격 |
| multiagent | 앵무새 회의 |
| guardrail | 울타리 |
| reasoning | 답하기 전 혼자 중얼거리기 |
| evaluation | 시험관의 채점표 |
| humanloop | 마지막은 사람이 |
| multimodal | 그림도 보는 앵무새 |
| diffusion | 안개에서 그림 꺼내기 |
| codegen | 코드 쓰는 앵무새 |
| workflow | 심부름 순서표 |
| distillation | 작은 앵무새에게 흉내 가르치기 |
| quantization | 콩을 굵게 세기 |
| inference | 앵무새가 답하는 값과 시간 |
| pricing | 콩 값 |
| attention | 앵무새의 눈길 |
| pretraining | 책 읽는 학교 |
| alignment | 앵무새 예절 교육 |
| knowledgecutoff | 책을 덮은 날 |
| openweights | 우리 집 앵무새 vs 빌린 앵무새 |
| routing | 어느 앵무새에게 시킬까 |
| llmops | 앵무새 돌보기 |
| bias | 앵무새가 읽은 책의 치우침 |
| aiprivacy | 앵무새에게 준 비밀 콩 |
| synthetic | 앵무새가 쓴 책으로 앵무새 가르치기 |
