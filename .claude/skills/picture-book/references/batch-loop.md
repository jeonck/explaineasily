# 대량 작성 루프 — 병렬 에이전트 + 완성도 루프

용어 10개 이상을 한 번에 채울 때 쓴다. 한 세션에서 보안 용어 59→113개를 이 루프로 채웠다 (에이전트 13개 × 4용어, 배치당 약 15분, 총괄이 시각 검수).

## 1. 갭 목록 만들기

```
python3 .claude/skills/picture-book/scripts/coverage_audit.py --category <cat> --ref <cat>-reference.txt
```
- `reference.txt` 는 그 분야의 표준 용어 목록(자격증 도메인, 교과서 목차, 업계 용어집)에서 100~200개를 뽑아 한 줄에 하나. 표기 변형은 `|` 로.
- 출력의 `missing` 이 갭. 여기서 **4개씩 묶어** 배치를 만든다. 묶음은 주제가 가까운 것끼리(정체성/공격/거버넌스/엔지니어링…) — 같은 에이전트가 교차 링크를 자연스럽게 건다.

## 2. 브리프와 배정표

- `assets/BRIEF.template.md` 를 복사해 `{{...}}` 를 채우고 scratchpad 에 둔다. 브리프는 모든 에이전트가 같은 것을 읽는다.
- 배정표 한 줄 = `slug / order / 제목 제안 / 비유 제안(패널 흐름 요약) / glossary 8개 제안(→링크 slug 포함)`. 총괄이 비유를 미리 제안해야 세계관이 흔들리지 않는다. 에이전트는 더 좋은 안이 있으면 바꿔도 된다.
- order 는 겹치지 않게 총괄이 미리 배정한다 (마지막 order + 1부터 연속).

## 3. 병렬 실행

- 에이전트 1개 = 용어 4개. 동시에 6~10개까지 문제없음 (같은 폴더에 서로 다른 파일만 씀).
- 에이전트에게 금지: 커밋/푸시, README/SKILL 수정, 브라우저·http.server(공유 자원), 공유 scratchpad 파일 덮어쓰기.
- 에이전트에게 요구: `python3 -W error build.py` 통과 + `validate.py --slugs <slug> --strict` + 좌표 자가 점검 + 짧은 최종 보고.
- 동시 작성 중엔 다른 에이전트의 미완성 파일이 전체 빌드를 잠깐 깨뜨릴 수 있다. 에이전트는 자기 slug 만 격리 렌더해 검증하고 보고에 명시한다. 총괄은 마지막에 전체 빌드를 다시 돌린다.
- 대기는 background `sleep` 로. 에이전트 transcript(TaskOutput)는 크므로 읽지 않는다 — 완료 알림의 요약만 본다.

## 4. 시각 검수 (총괄)

```
python3 .claude/skills/picture-book/scripts/render_qa.py <out_dir> slug1 slug2 ...
```
- 페이지당 PNG 한 장(패널 5개 세로 결합). Read 로 본다. 페이지당 호출 1번 — 브라우저 스크린샷(페이지당 5번)보다 5배 빠르다.
- 보는 것: 캔버스 밖으로 나간 요소, 라벨이 사람/상자 위에 겹침, 배경 헬퍼의 달/별과 겹침, 크림색 종이 위 어두운 글자인지, 말풍선이 다른 요소를 덮는지, 하단 캡션이 그림과 붙는지.
- 고치는 방법: 좌표 몇 개면 총괄이 직접 `python3 - <<EOF` 문자열 치환으로 고친다 (에이전트 재호출보다 빠름). 구조적 문제(비유가 틀림, 패널 빔)면 해당 에이전트에게 SendMessage 로 되돌린다.
- 고친 뒤엔 그 패널만 crop 해 다시 본다.

## 5. 마무리

```
python3 .claude/skills/picture-book/scripts/validate.py --category <cat>
python3 .claude/skills/picture-book/scripts/update_tables.py --category <cat>
python3 .claude/skills/picture-book/scripts/coverage_audit.py --category <cat> --ref ... --threshold 90
git add -A && git commit -m "Add N <cat> terms: ..." && git push origin main
```
커버리지가 목표 미만이면 `missing` 으로 다음 배치를 만들어 2번부터 반복한다. 목표에 닿으면 끝.

## 흔한 실패와 처방

| 실패 | 처방 |
|---|---|
| `person() got multiple values for 'face'` | dict 에 face 가 있는데 `face=` 도 넘김 — 둘 중 하나만 |
| `SyntaxError` 따옴표 | `"⟦"…"⟧"` 처럼 같은 따옴표 중첩 → 작은따옴표 |
| bubble tail KeyError | tail 은 left/right/bottom 만 |
| 링크 assert 실패 | 동시 작성 중인 slug — 마지막 전체 빌드에서 재확인 |
| 글자가 네모로 렌더 | 특수 기호(✗ ✕ ☒) — ✓ 와 × 만 사용 |
| 달/별과 겹침 | `night()` 는 달을 (660,50) r=26 에 그림 — 그 자리 비우기 |
| 캡션이 그림과 붙음 | 캡션 y = 높이-20, 그 위 요소 바닥 ≤ 높이-45 |
