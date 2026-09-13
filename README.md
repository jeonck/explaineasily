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

보안 용어는 하나의 세계를 공유한다 — 내 컴퓨터는 성, 공격자는 수상한 사람, 방어자는 망루 위의 친구·경비실·경비견·복도 파수꾼.

### 소프트웨어 설계

| 용어 | 이야기 | 한글 | English |
|---|---|---|---|
| Dialog Map | 방과 문의 지도 | [dialogmap-ko](docs/dialogmap-ko.html) | [dialogmap-en](docs/dialogmap-en.html) |

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
목록 페이지는 맨 위 분야 탭으로 나뉘고, 탭 안에서 10개씩 페이지로 나눠 보여준다(`#cat=<폴더>&page=N`, `build.py` 의 `PER_PAGE`). "다음 이야기" 링크는 같은 분야 안에서만 돈다.

```python
CATEGORIES = {
    "security": ("보안", "Security"),
    "design": ("소프트웨어 설계", "Software Design"),
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

`.claude/skills/eli5/SKILL.md` — 새 용어를 위 그림책 형식으로 만드는 절차 (분야 정하기 → 비유 고르기 → 패널 3~5장 → `_draw.py` 조각으로 그리기 → `terms/<분야>/<slug>.py` → 빌드·점검). 위 문서들이 이 스킬의 결과물이다. 다른 프로젝트에서 쓰려면 디렉터리를 복사한다.

```bash
cp -r .claude/skills/eli5 ~/.claude/skills/
```
