# {{PROJECT}} 용어 그림책 작성 브리프 — 분야: {{CATEGORY}}

리포: {{REPO_PATH}} (정적 사이트 생성기 build.py, 의존성 없음)
당신의 임무: 아래 배정된 용어 각각에 대해 `terms/{{CATEGORY}}/<slug>.py` 를 **기존 형식과 똑같이** 작성하고, 빌드가 경고 없이 통과하게 만드는 것.
커밋/푸시/README/SKILL.md 수정은 하지 마세요(총괄이 일괄 처리). 브라우저/스크린샷/http.server 도 사용하지 마세요(공유 자원 충돌).
공유 scratchpad 에 보조 스크립트를 만들 땐 파일 이름에 배정 번호를 붙이세요(다른 에이전트가 덮어씁니다).

## 반드시 먼저 읽을 것
1. `.claude/skills/picture-book/SKILL.md` 와 `references/world-design.md` — 방법과 세계관 설계
2. `terms/{{CATEGORY}}/_WORLD.md` — 이 분야의 세계관 (등장인물·소품·색 규칙). 없으면 총괄에게 알리고 멈추세요.
3. `terms/_draw.py` — 공용 드로잉 헬퍼. 시그니처를 정확히 확인.
4. 최근 예시 3개: {{EXAMPLES}} — PAGE dict 구조, 패널 5개, hero+tricks, summary, glossary 8개, 교차 링크 방식.
5. `ls terms/{{CATEGORY}}` 로 현재 존재하는 slug 목록 확인 → 링크는 존재하는 slug 로만. 배정표에 있는 다른 새 slug 로도 링크 가능(동시에 만들어짐).

## 형식 규칙
- 파일 상단 `from _draw import *`. 모든 문자열은 `(ko, en)` 튜플, SVG 안 텍스트는 `⟦한글|English⟧`.
- PAGE: slug, order(배정표 숫자), title(비유 이름, 용어 이름 아님), h1(`<em>용어</em>가 뭐예요?` / `What is <em>Term</em>?`), sub, panels 5개(하나만 `"hero": True` + `"tricks": (4, [...])`), summary((h_ko,h_en),(p_ko,p_en)), glossary 8개 = (term_ko, term_en, (bold_ko,bold_en), (rest_ko,rest_en)).
- 패널 흐름: ① 문제 상황 ② 왜 어려운가/잘못하면 ③(hero) 용어 = 비유 한 문장 + 4 tricks ④ 작동 디테일 ⑤ 결과/한계/다른 페이지와 연결.
- 다섯 살 눈높이, 짧게. 원어 용어는 summary 두 번째 문단과 glossary 에서만.
- SVG 폭 760, 높이 300~360. 모든 요소 0..760 안. 사람 person(x,y,s)은 폭 ≈70s, 높이 ≈110s. castle() 원본 460×200.
- 라벨끼리/사람과 라벨 겹치지 않게. 하단 캡션은 h-20 근처, 그 위 요소 바닥은 최소 25px 위. 배경 헬퍼(night 등)가 그리는 달·별 위치도 피하세요.
- 고정 크림색 종이(#FFF8E7) 위 글자는 반드시 `#142033`. 고정 배경 위 텍스트도 literal 색. 나머지는 CSS 토큰.
- bubble tail 은 "left"/"right"/"bottom" 만. Python 문자열 안 같은 따옴표 중첩 금지. 특수 기호는 ✓ 와 × 만.
- tricks 아이콘: icon('<64×64 내부>') 4개 새로 그리기.

## 검증 (각 파일 작성 후 반드시)
```
cd {{REPO_PATH}} && python3 -W error build.py | grep <slug>
python3 .claude/skills/picture-book/scripts/validate.py --category {{CATEGORY}} --slugs <slug> --strict
```
좌표 자가 점검: (a) 오른쪽/아래로 넘치는 요소 (b) 라벨이 사람/상자 위에 겹침 — 좌표로 계산해 확인.

## 배정표 (slug / order / 제목 제안 / 비유 제안 / glossary 제안)
{{ASSIGNMENTS}}

제목/비유는 제안이며 세계관 안에서 더 좋은 안이 있으면 바꿔도 됩니다.

## 최종 보고 형식
slug 별로: 제목(ko), 비유 한 줄, 링크한 slug 목록, 검증 결과(ok / 미해결). 짧게.
