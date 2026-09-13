# explaineasily

어려운 것을 정확하게, 쉽게 설명하기 위한 문서와 스킬 모음.

## 작성 원칙

- 쉬움을 위해 사실을 왜곡하지 않는다.
- 비유는 하나만 쓰고, 그 비유가 깨지는 지점을 함께 밝힌다.
- 전문 용어는 쉬운 말로 먼저 쓰고 원어를 괄호에 병기한다 — 나중에 검색할 수 있어야 한다.
- 어휘를 낮추는 것이지, 읽는 사람을 낮추는 것이 아니다.

## 문서

| 주제 | 한글 | English |
|---|---|---|
| CTI (사이버 위협 인텔리전스) | [docs/cti-ko.md](docs/cti-ko.md) | [docs/cti-en.md](docs/cti-en.md) |

마크다운이 원본이고, HTML은 여기서 생성한다.

```bash
python3 build.py
```

`docs/*.html` 과 `docs/index.html` 이 만들어진다. 의존성은 없고 파이썬 3만 있으면 된다.
**생성된 HTML은 직접 고치지 말 것** — 다음 빌드에서 덮어써진다. 내용은 `.md` 를 고친다.

GitHub Pages 를 `main` 브랜치의 `/docs` 폴더로 설정하면 그대로 배포된다.

## 스킬

### `eli5`

위 원칙을 절차로 만든 Claude Code 스킬. 개념·코드·에러·문서를 비전문가도 이해할 수 있게 풀어준다.

- **트리거**: "쉽게 설명해줘", "ELI5", "초등학생도 알아듣게", "비유로 설명해줘", "explain like I'm 5"
- **내용**: 5층 설명 구조, 비유 한 개 규칙, 용어 병기, 에러 설명 전용 흐름, 자가 점검 체크리스트
- **위치**: [`.claude/skills/eli5/SKILL.md`](.claude/skills/eli5/SKILL.md)

위 문서들이 이 스킬로 쓴 결과물이다.

## 사용법

이 레포를 열고 작업하면 `.claude/skills/` 아래 스킬이 자동으로 로드된다.
세션 중에 스킬을 추가하거나 수정했다면 `/reload-skills` 로 다시 읽어들인다.

다른 프로젝트에서 쓰려면 스킬 디렉터리를 복사한다.

```bash
cp -r .claude/skills/eli5 /path/to/project/.claude/skills/
```

모든 프로젝트에서 쓰려면 사용자 스킬 디렉터리에 둔다.

```bash
cp -r .claude/skills/eli5 ~/.claude/skills/
```
