# explaineasily

어려운 보안 용어를 **그림책**으로. 글은 적게, 그림은 크게, 다섯 살 눈높이로.

배포: `main` 브랜치의 `/docs` 폴더 (GitHub Pages)

## 문서

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| CTI | 망루 위의 친구 | [cti-ko](docs/cti-ko.html) | [cti-en](docs/cti-en.html) |
| IOC | 남겨진 발자국 | [ioc-ko](docs/ioc-ko.html) | [ioc-en](docs/ioc-en.html) |
| TTP | 도둑의 버릇 | [ttp-ko](docs/ttp-ko.html) | [ttp-en](docs/ttp-en.html) |
| MITRE ATT&CK | 도둑 백과사전 | [attack-ko](docs/attack-ko.html) | [attack-en](docs/attack-en.html) |
| Pyramid of Pain | 고통의 피라미드 | [pyramid-ko](docs/pyramid-ko.html) | [pyramid-en](docs/pyramid-en.html) |
| TLP | 비밀 신호등 | [tlp-ko](docs/tlp-ko.html) | [tlp-en](docs/tlp-en.html) |
| SOC | 성의 경비실 | [soc-ko](docs/soc-ko.html) | [soc-en](docs/soc-en.html) |

## 구조

```
terms/<slug>.py   원본. 한 파일에 한글·영문을 같이 적는다 — 문장은 (ko, en) 튜플, SVG 글자는 ⟦ko|en⟧
terms/_draw.py    같이 쓰는 SVG 조각 (사람, 성, 말풍선, 방패 …)
build.py          terms/ → docs/*-ko.html, docs/*-en.html, docs/index.html
```

```bash
python3 build.py
```

의존성 없음. **`docs/*.html` 은 생성물이라 직접 고치지 말 것** — `terms/` 를 고치고 다시 빌드한다.

### 페이지 한 장의 구성

1. 제목 — `<em>용어</em>가 뭐예요?`
2. 그림 패널 3~5장 — 큰 SVG 한 장 + 한 문장 + 작은 부연. 필요하면 카드 3~4개나 말풍선
3. 한 줄 요약 (어두운 상자)
4. "어른들은 이렇게 불러요" — 쉬운 말 → 원어 대응표
5. 다음 이야기 링크

### 새 용어 추가

`terms/<slug>.py` 를 만들고 `PAGE` 딕셔너리에 `slug`, `order`, `title`, `h1`, `sub`, `panels`, `summary`, `glossary` 를 채운다. 기존 파일 하나를 복사해서 시작하면 된다.

## 작성 원칙

- 쉬움을 위해 사실을 왜곡하지 않는다.
- 비유는 하나만 쓰고, 그 비유가 깨지는 지점을 함께 밝힌다. (발자국 → "신발을 바꾸면 발자국도 바뀐다")
- 전문 용어는 쉬운 말로 먼저 쓰고 원어를 병기한다 — 나중에 검색할 수 있어야 한다.
- 어휘를 낮추는 것이지, 읽는 사람을 낮추는 것이 아니다.

## 스킬

`.claude/skills/eli5/SKILL.md` — 새 용어를 위 그림책 형식으로 만드는 절차 (비유 고르기 → 패널 3~5장 → `_draw.py` 조각으로 그리기 → `terms/<slug>.py` → 빌드·점검). 위 문서들이 이 스킬의 결과물이다. 다른 프로젝트에서 쓰려면 디렉터리를 복사한다.

```bash
cp -r .claude/skills/eli5 ~/.claude/skills/
```
