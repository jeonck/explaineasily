from _draw import *
from _world import *

# 1. 번역 원고, 정답이 뭔지 교정자도 모름
P1 = svg(300, sky(300)
         + manuscript(240, 140, 0.9, text="⟦원문|original text⟧")
         + '<path d="M300 150 h40" stroke="var(--line)" stroke-width="3" marker-end="url(#arr2)"/>'
         + '<defs><marker id="arr2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--line)"/></marker></defs>'
         + manuscript(420, 140, 0.9, text="⟦번역문|translation⟧")
         + person(540, 150, s=0.8, face=FROWN + '<path d="M18 46 h-6" stroke="var(--night)" stroke-width="2"/>', **PROOFER)
         + bubble(500, 60, 220, 40, "⟦이 번역이 맞는지 정답을 몰라요|I don't know the right answer to compare against⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦번역엔 '유일한 정답'이 없을 때가 많아요|translation often has no single correct answer⟧", 12, "var(--ink)"))

# 2. 정답과 비교하는 보통 방법을 못 씀
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(220, 150, s=0.8, face=SWEAT + EYES, **PROOFER)
         + '<rect x="330" y="120" width="100" height="70" rx="4" fill="#FFF8E7" stroke="var(--bad)" stroke-width="3"/>'
         + label(380, 160, "⟦정답지|answer key⟧", 14, "var(--bad)", cls="d")
         + '<path d="M345 135 L415 175 M415 135 L345 175" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>'
         + person(560, 150, s=0.8, face=EYES, **WRITER)
         + label(380, 30, "⟦'정답과 비교하기'라는 평소 방법을 못 써요|the usual trick — 'compare to the answer key' — just doesn't work here⟧", 13, "var(--ink)")
         + label(380, 280, "⟦그럼 번역이 맞는지 아예 확인을 못 할까요|so is there no way at all to check the translation?⟧", 12, "var(--ink)"))

# 3. 메타모픽 테스트 = 정답 없이, 관계로 확인하기 (hero)
P3 = svg(340, sky(340)
         + manuscript(140, 140, 0.75, text="⟦문장|a sentence⟧")
         + label(140, 220, "⟦문장을 두 번 반복|repeat the sentence twice⟧", 11, "var(--muted)")
         + '<path d="M200 150 h50" stroke="var(--line)" stroke-width="3" marker-end="url(#arr3)"/>'
         + '<defs><marker id="arr3" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--line)"/></marker></defs>'
         + manuscript(290, 120, 0.6) + manuscript(290, 160, 0.6)
         + label(290, 210, "⟦입력: 문장+문장|input: sentence + sentence⟧", 11, "var(--muted)")
         + '<path d="M350 150 h50" stroke="var(--accent)" stroke-width="3" marker-end="url(#arr4)"/>'
         + '<defs><marker id="arr4" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--accent)"/></marker></defs>'
         + manuscript(440, 120, 0.6) + manuscript(440, 160, 0.6)
         + person(560, 150, s=0.85, face=SMILE, **PROOFER)
         + label(440, 215, "⟦출력도 번역문+번역문이어야 해요|the output should also be translation + translation⟧", 11, "var(--good)")
         + label(380, 30, "⟦메타모픽 테스트 = 정답은 몰라도, 입력이 바뀌면 출력도 '이렇게' 바뀌어야 한다는 관계로 확인하기|metamorphic testing = no known answer, but checking a relationship: change the input this way, and the output must change that way too⟧", 13, "var(--ink)", cls="d"))

# 4. 입력 변화 → 기대되는 출력 관계 예시표
P4 = svg(320, sky(320)
         + styleguide(60, 40, 640, 240, "⟦메타모픽 관계 예시|EXAMPLE METAMORPHIC RELATIONS⟧",
                      ("⟦문장을 두 번 반복 → 번역문도 두 번 반복돼야 함|repeat the sentence → the translation repeats too⟧",
                       "⟦단어 순서를 살짝 바꿔도 → 핵심 단어 수는 똑같아야 함|reorder words slightly → the key word count stays the same⟧",
                       "⟦같은 문장을 두 번 넣으면 → 같은 번역이 두 번 나와야 함|feed the same sentence twice → the same translation comes out twice⟧"), 1.0)
         + label(380, 300, "⟦관계가 깨지면, 정답을 몰라도 뭔가 잘못된 거예요|break the relationship, and something's wrong — even without knowing the right answer⟧", 12, "var(--ink)"))

# 5. 관계를 잘못 세우면 놓침, 정답 비교를 대체하진 않음
P5 = svg(330, '<rect width="380" height="330" fill="var(--accent-soft)"/><rect x="380" width="380" height="330" fill="var(--good-soft)"/>'
         + person(190, 130, s=0.8, face=FROWN, **PROOFER)
         + label(190, 260, "⟦관계를 잘못 세우면 진짜 버그를 놓쳐요|a badly chosen relation can miss a real bug⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **WRITER) + '<rect x="540" y="200" width="60" height="50" rx="3" fill="#FFF8E7" stroke="var(--good)" stroke-width="3"/>'
         + label(570, 265, "⟦정답을 아는 경우엔 정답 비교가 더 정확해요|when the answer IS known, comparing to it is more precise⟧", 11, "var(--ink)")
         + label(380, 305, "⟦메타모픽 테스트는 '정답 비교'를 완전히 대신하진 않아요|metamorphic testing doesn't fully replace comparing to a known answer⟧", 12, "var(--ink)", cls="d"))

NOREF_I = icon('<rect x="14" y="14" width="36" height="36" rx="6" fill="none" stroke="var(--muted)" stroke-width="4" stroke-dasharray="6 4"/><text x="32" y="40" text-anchor="middle" font-size="22" font-weight="700" fill="var(--muted)">?</text>')
CHANGE_I = icon('<path d="M14 32 h36" stroke="var(--accent)" stroke-width="4" marker-end="url(#mi1)"/><defs><marker id="mi1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="var(--accent)"/></marker></defs>')
RELATION_I = icon('<circle cx="20" cy="32" r="8" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/><circle cx="44" cy="32" r="8" fill="var(--good)" stroke="var(--line)" stroke-width="2"/><path d="M28 32 h8" stroke="var(--line)" stroke-width="2" stroke-dasharray="3 2"/>')
BREAK_I = icon('<path d="M14 32 h14 l6 -10 l8 20 l6 -10 h12" stroke="var(--bad)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

PAGE = {
    "slug": "metamorphictest", "order": 27,
    "title": ("정답 없이도 관계로 확인하기", "Checking by Relationship, With No Answer Key"),
    "h1": ("<em>메타모픽 테스트</em>가 뭐예요?", "What is <em>Metamorphic Testing</em>?"),
    "sub": ("메타모픽 테스트를, 정답이 없는 번역 원고를 '문장을 반복하면 번역도 반복돼야 한다'는 관계로 검증하는 출판사 이야기로 풀어봤어요.",
            "Metamorphic testing, told as a story about checking a translation with no single right answer by a relationship: repeat the sentence, and the translation should repeat too."),
    "panels": [
        {"svg": P1, "alt": ("교정자가 번역문이 맞는지 비교할 정답을 몰라 당황함", "A proofreader is stumped because there's no answer key to check the translation against"),
         "caption": ("번역이 맞는지 정답을 몰라요.", "There's no known right answer to check the translation against."),
         "small": ("번역엔 '유일한 정답'이 없을 때가 많아요.", "Translation often has no single correct answer.")},
        {"svg": P2, "alt": ("정답지에 가위표가 그어져 있고, 평소 방법을 못 쓴다는 걸 보여줌", "An answer key is crossed out, showing the usual method just doesn't work"),
         "caption": ("'정답과 비교하기'라는 평소 방법을 못 써요.", "The usual trick — comparing to an answer key — doesn't work here."),
         "small": ("그럼 아예 확인할 방법이 없을까요?", "So is there no way at all to check it?")},
        {"svg": P3, "hero": True, "alt": ("같은 문장을 두 번 반복해 넣으면, 번역문도 두 번 반복되어 나와야 한다는 관계를 보여줌", "Feeding the same sentence twice should make the translation come out twice as well — a relationship check"),
         "caption": ("메타모픽 테스트는 정답 없이도 관계로 확인해요.", "Metamorphic testing checks via a relationship, even with no known answer."),
         "small": ("문장을 두 번 넣으면, 번역문도 두 번 나와야 해요.", "Feed the sentence twice, and the translation should come out twice too."),
         "tricks": (4, [
             (NOREF_I, ("정답 없이도 테스트", "Test without an answer key"), ("정답을 몰라도 괜찮아요", "not knowing the answer is fine"), "calm"),
             (CHANGE_I, ("입력을 규칙적으로 바꾸기", "Change the input in a known way"), ("예: 문장을 반복해요", "e.g. repeating the sentence")),
             (RELATION_I, ("출력도 같은 규칙으로", "Output should follow the same rule"), ("반복이면 반복으로요", "repeated input, repeated output")),
             (BREAK_I, ("관계가 깨지면 버그", "Broken relation = a bug"), ("정답을 몰라도 알 수 있어요", "catchable even without the answer"), "warm"),
         ])},
        {"svg": P4, "alt": ("문장 반복, 단어 순서 변경, 같은 문장 재투입 세 가지 메타모픽 관계 예시표", "A table of three example metamorphic relations: repeating a sentence, reordering words, feeding the same sentence twice"),
         "caption": ("이런 '관계'들을 미리 정해두고 확인해요.", "These relationships are decided in advance and checked."),
         "small": ("관계가 깨지면, 정답을 몰라도 뭔가 잘못된 거예요.", "Break the relationship, and something's wrong — even without knowing the right answer.")},
        {"svg": P5, "alt": ("왼쪽: 관계를 잘못 세워 버그를 놓침. 오른쪽: 정답을 아는 경우엔 정답 비교가 더 정확함", "Left: a badly chosen relation misses a bug. Right: when the answer is known, comparing to it is more precise"),
         "caption": ("관계를 잘못 세우면 버그를 놓칠 수 있어요.", "A badly chosen relationship can miss a real bug."),
         "small": ("정답을 아는 경우엔, 정답과 비교하는 쪽이 더 정확해요.", "When the answer is known, comparing to it directly is still more precise.")},
    ],
    "summary": (("<b>메타모픽 테스트</b>는 '정답'을 몰라도, 입력이 바뀌면 출력도 <b>이렇게 바뀌어야 한다는 관계</b>를 확인해 버그를 찾는 테스트예요.",
                 "<b>Metamorphic testing</b> finds bugs by checking a <b>relationship</b> — if the input changes a known way, the output must change a known way too — even with no answer key."),
                ("메타모픽 테스트는 '오라클 문제'(정답을 알 수 없거나 정답 하나를 정하기 어려운 경우)가 있는 프로그램을 위한 테스트 기법이에요. 번역기, 검색엔진, 머신러닝 모델처럼 유일한 정답이 없는 경우, 입력을 특정 방식으로 변형했을 때 출력이 만족해야 할 '메타모픽 관계'를 정의하고, 그 관계가 지켜지는지로 결함을 찾아요.",
                 "Metamorphic testing is a technique for programs with the 'oracle problem' — where there's no known correct output, or no single one to pin down. For systems like translators, search engines, or ML models, it defines 'metamorphic relations' that the output must satisfy when the input is transformed in a known way, and detects faults when those relations are violated.")),
    "glossary": [
        ("메타모픽 테스트", "Metamorphic Testing", ("정답 없이 관계로 확인하기.", "Checking by relationship, with no answer key."), ("오라클 문제가 있을 때 써요.", "Used when the oracle problem exists.")),
        ("오라클 문제", "Oracle Problem", ("정답지가 아예 없는 상황.", "A situation with no answer key at all."), ("번역·검색·ML에서 자주 생겨요.", "Common in translation, search, and ML.")),
        ("메타모픽 관계", "Metamorphic Relation", ("입력을 바꾸면 출력도 이렇게 바뀐다는 규칙.", "The rule that a given input change implies a given output change."), ("미리 정의해둬야 해요.", "Must be defined ahead of time.")),
        ("회귀테스트", "Regression Test", ("줄거리가 그대로인지 확인하는 교정.", "The proofing that checks the plot hasn't shifted."), ("정답을 아는 쪽에서 더 흔히 써요.", "More common where the answer is known.")),
        ("가설검정", "Hypothesis Testing", ("우연인지 진짜 차이인지 숫자로 가리기.", "Telling a real difference from coincidence, with numbers."), ("다른 방식으로 '모르는 것'을 다루는 방법이에요. → <a href=\"hypothesistest-ko.html\">두 표지 중 뭐가 진짜 더 잘 팔릴까</a>", 'A different way of handling uncertainty. → <a href="hypothesistest-en.html">which cover really sells better</a>')),
        ("블랙박스테스트", "Black-box Testing", ("내부는 안 보고 결과만 보는 교정.", "Checking only the result, without looking inside."), ('메타모픽 테스트도 이 계열이에요. → <a href="wbblacktest-ko.html">속을 펼쳐 볼지, 겉만 읽을지</a>', 'Metamorphic testing belongs to this family. → <a href="wbblacktest-en.html">looking inside, or just reading the outside</a>')),
        ("단위테스트", "Unit Test", ("정답지를 두고 비교하는 보통 교정.", "The usual proofing that compares against a known answer."), ("정답이 있을 때는 이쪽이 더 정확해요.", "More precise when the right answer is actually known.")),
        ("AI 환각", "AI Hallucination", ("그럴듯하지만 틀린 답을 내놓는 현상.", "Producing a plausible-sounding but wrong answer."), ('정답 없는 AI 결과를 검증할 때도 메타모픽 발상이 쓰여요. → <a href="hallucination-ko.html">앵무새 세계의 그럴듯한 거짓말</a>', "The same metamorphic idea helps verify AI output with no answer key. → <a href=\"hallucination-en.html\">the parrot world's plausible lies</a>")),
    ],
}
