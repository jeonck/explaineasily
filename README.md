# explaineasily

어려운 것을 정확하게, 쉽게 설명하기 위한 Claude Code 스킬 모음.

## 스킬

### `eli5`

개념·코드·에러·문서를 비전문가도 이해할 수 있게 풀어준다.

- **트리거**: "쉽게 설명해줘", "ELI5", "초등학생도 알아듣게", "비유로 설명해줘", "explain like I'm 5"
- **핵심 원칙**: 쉬움을 위해 사실을 왜곡하지 않는다. 비유는 하나만 쓰고, 비유가 깨지는 지점을 함께 밝힌다.
- **위치**: `.claude/skills/eli5/SKILL.md`

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
