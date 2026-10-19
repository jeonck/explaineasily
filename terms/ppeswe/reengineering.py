from _draw import *
from _world import *

# 1. 원본 원고는 사라지고, 인쇄된 책만 남았어요
P1 = svg(300, sky(300)
         + person(140, 150, s=0.8, face=SWEAT + EYES, **WRITER)
         + bookshelf(280, 140, 0.9, n=4, hl=2) + printplate(500, 170, 0.6)
         + label(380, 230, "⟦원본 원고는 사라지고, 인쇄된 책만 남아 있어요|the original manuscript is gone — only the printed book remains⟧", 12, "var(--bad)")
         + label(380, 280, "⟦그런데 이 책을 다시 손봐서 내고 싶어요|but we want to rework it and publish it again⟧", 13, "var(--ink)"))

# 2. 그냥 새로 쓰자는 말, 그러면 더 비싸진다는 반박
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + person(200, 150, s=0.85, face=SMILE, **EDITOR)
         + bubble(140, 80, 200, 36, "⟦그냥 새로 쓰면 되잖아요|just write it from scratch again⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(560, 150, s=0.7, face=FROWN, **WRITER) + bubble(460, 80, 230, 36, "⟦그럼 20년 치를 다 다시 만들어야 해요|that means remaking twenty years of content⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사라진 원본을 무시하고 새로 짓는 건 더 비싸요|ignoring the lost original and rebuilding from nothing costs more⟧", 12, "var(--ink)"))

# 3. 역공학으로 개요를 되짚고, 재공학으로 다시 써 재출간 (hero)
P3 = svg(340, sky(340)
         + person(380, 120, s=0.9, face=EYES, **WRITER)
         + printplate(240, 190, 0.6, label_text="⟦완성본|finished book⟧")
         + manuscript(380, 260, 0.7, text="⟦되짚은 개요|outline reconstructed⟧")
         + printplate(520, 190, 0.6, label_text="⟦재출간본|re-published⟧")
         + label(380, 30, "⟦역공학 = 완성본만 보고 개요를 거꾸로 추정, 재공학 = 정리해서 요즘 말로 다시 써 재출간|reverse engineering = inferring the outline from the finished book; reengineering = reworking it and republishing⟧", 12, "var(--ink)", cls="d")
         + label(380, 320, "⟦역공학 → 재구조화 → 재공학, 이 순서를 3R이라고 불러요|reverse engineering → restructuring → reengineering — these three together are called 3R⟧", 12, "var(--muted)"))

# 4. 3R 순서
P4 = svg(320, sky(320)
         + styleguide(60, 40, 320, 240, "⟦3R 순서|THE THREE Rs, IN ORDER⟧",
                      ("⟦역공학 — 완성본에서 개요를 거꾸로 추정|reverse engineering — inferring the outline from the book⟧",
                       "⟦재구조화 — 추정한 개요를 정리정돈|restructuring — tidying up the inferred outline⟧",
                       "⟦재공학 — 요즘 말로 다시 써서 재출간|reengineering — rewriting in today's language⟧",
                       "⟦순공학과 차이 — 순공학은 원고부터 새로 써요|vs forward engineering — writes a fresh manuscript⟧"), 1.0)
         + person(560, 150, s=0.75, face=EYES, **WRITER)
         + label(560, 250, "⟦사라진 원본을 되살리는 복원 작업에 가까워요|closer to a restoration, bringing back what was lost⟧", 11, "var(--muted)")
         + label(380, 300, "⟦되짚은 개요가 완벽히 맞다는 보장은 없어요|there's no guarantee the reconstructed outline is exactly right⟧", 12, "var(--ink)"))

# 5. 새 책만큼 깔끔하진 않아요
P5 = svg(300, '<rect width="380" height="300" fill="var(--accent-soft)"/><rect x="380" width="380" height="300" fill="var(--good-soft)"/>'
         + person(190, 150, s=0.8, face=EYES, **WRITER) + label(190, 240, "⟦오래된 책도 다시 살릴 수 있어요|it can revive even an old out-of-print book⟧", 11, "var(--ink)")
         + person(570, 150, s=0.8, face=SMILE, **EDITOR) + manuscript(570, 220, 0.6) + label(570, 270, "⟦새 책만큼 깔끔하진 않을 수 있어요|but it may not come out as clean as a brand-new book⟧", 11, "var(--ink)")
         + label(380, 282, "⟦재공학은 과거를 되살리는 일이지, 처음부터 완벽하게 새로 짓는 일은 아니에요|reengineering revives the past — it isn't building something perfectly new from scratch⟧", 12, "var(--ink)", cls="d"))

ANALYZE_I = icon('<rect x="12" y="10" width="28" height="36" rx="2" fill="#FFF8E7" stroke="#C9822B" stroke-width="3"/><circle cx="42" cy="40" r="12" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M51 49 l9 9" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
INFER_I = icon('<path d="M46 16 a20 20 0 1 0 4 28" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M50 30 l0 -14 -14 0" stroke="var(--good)" stroke-width="5" fill="none" stroke-linecap="round"/>')
TIDY_I = icon('<rect x="10" y="12" width="16" height="12" rx="2" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/><rect x="10" y="28" width="16" height="12" rx="2" fill="var(--good-soft)" stroke="var(--good)" stroke-width="2"/><rect x="34" y="20" width="20" height="24" rx="2" fill="none" stroke="var(--ink)" stroke-width="3"/>')
REWRITE_I = icon('<path d="M14 50 l4 -14 26 -26 10 10 -26 26 z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="3"/><path d="M40 14 l10 10" stroke="var(--accent)" stroke-width="3"/>')

PAGE = {
    "slug": "reengineering", "order": 8,
    "title": ("사라진 원본을 되짚어 다시 짓기", "Tracing Back a Lost Original to Rebuild It"),
    "h1": ("<em>재공학/역공학(3R)</em>이 뭐예요?", "What is <em>Re-engineering/Reverse Engineering (3R)</em>?"),
    "sub": ("재공학과 역공학(3R)을, 원본 원고가 사라진 오래된 절판본을 완성본만 보고 되짚어 다시 손보는 이야기로 풀어봤어요.",
            "Reengineering and reverse engineering (3R), told as a story about reviving an old out-of-print book whose original manuscript is gone, working backward from the finished copy."),
    "panels": [
        {"svg": P1, "alt": ("작가가 진땀을 흘리며 서가 속 오래된 절판본을 바라봄, 원본 원고는 없음", "A writer sweats, looking at an old out-of-print book on the shelf with no surviving original manuscript"),
         "caption": ("원본 원고는 사라지고, 인쇄된 책만 남아 있어요.", "The original manuscript is gone — only the printed book remains."),
         "small": ("그런데 이 책을 다시 손봐서 내고 싶어요.", "But we want to rework it and publish it again.")},
        {"svg": P2, "alt": ("편집장은 그냥 새로 쓰자고 하고, 작가는 그러면 20년 치를 다 다시 만들어야 한다고 반박함", "The editor suggests writing it fresh; the writer objects that it means remaking twenty years of content"),
         "caption": ("그냥 새로 쓰자는 말, 그러면 더 비싸진다는 반박.", "A suggestion to just start fresh, met with the fact that doing so costs more."),
         "small": ("사라진 원본을 무시하고 새로 짓는 건 더 비싸요.", "Ignoring the lost original and rebuilding from nothing costs more.")},
        {"svg": P3, "hero": True, "alt": ("작가가 완성본을 보고 개요를 되짚어 재구성한 뒤, 새 재출간본을 만듦", "A writer studies the finished book, reconstructs its outline, and produces a newly republished edition"),
         "caption": ("역공학으로 개요를 되짚고, 재공학으로 다시 써 재출간해요.", "Reverse engineering traces back the outline; reengineering rewrites it and republishes."),
         "small": ("역공학 → 재구조화 → 재공학, 이 순서를 3R이라고 불러요.", "Reverse engineering → restructuring → reengineering — together these three are called 3R."),
         "tricks": (4, [
             (ANALYZE_I, ("완성본 뜯어보기", "Study the finished book"), ("있는 그대로 자세히 봐요", "examining it closely as it is"), "calm"),
             (INFER_I, ("거꾸로 개요 추정하기", "Infer the outline backward"), ("있던 구조를 되짚어요", "tracing back the original structure")),
             (TIDY_I, ("정리정돈하기", "Tidy it up"), ("되짚은 개요를 가지런히 해요", "straightening out the reconstructed outline"), "warm"),
             (REWRITE_I, ("요즘 말로 다시 쓰기", "Rewrite in today's language"), ("바뀐 독자에 맞게 고쳐요", "adapting it for today's readers")),
         ])},
        {"svg": P4, "alt": ("3R 순서표: 역공학·재구조화·재공학·순공학과의 차이 네 항목", "A 3R order board: reverse engineering, restructuring, reengineering, and the contrast with forward engineering"),
         "caption": ("3R은 이 순서로 진행돼요.", "The 3Rs proceed in this order."),
         "small": ("사라진 원본을 되살리는 복원 작업에 가까워요.", "Closer to a restoration, bringing back what was lost.")},
        {"svg": P5, "alt": ("왼쪽: 작가가 오래된 책도 다시 살릴 수 있다고 말함. 오른쪽: 편집장이 새 책만큼 깔끔하진 않을 수 있다고 말함", "Left: the writer says even an old book can be revived. Right: the editor says it may not come out as clean as a new one"),
         "caption": ("새 책만큼 깔끔하진 않을 수 있어요.", "It may not come out as clean as a brand-new book."),
         "small": ("과거를 되살리는 일이지, 완벽하게 새로 짓는 일은 아니에요.", "It revives the past — it isn't building something perfectly new.")},
    ],
    "summary": (("<b>재공학/역공학(3R)</b> = 사라진 원본을 <b>완성본에서 거꾸로 되짚어</b> 정리하고 <b>다시 써 재출간</b>하는 일.",
                 "<b>Re-engineering/reverse engineering (3R)</b> = <b>tracing a lost original backward</b> from the finished product, tidying it up, and <b>rewriting it for republication</b>."),
                ("3R은 역공학(Reverse Engineering, 산출물에서 설계를 되짚기)·재구조화(Restructuring, 기능은 그대로 두고 구조만 정리)·재공학(Reengineering, 현대 기술로 다시 구축)을 함께 부르는 말이에요. 원본 설계 문서나 소스가 부실한 레거시 시스템을 다루는 대표적 방법이고, 처음부터 새로 짓는 순공학(Forward Engineering)보다 기존 자산을 살리는 데 집중해요.",
                 "3R refers together to reverse engineering (tracing design back from the output), restructuring (tidying structure while keeping function the same), and reengineering (rebuilding with modern technology). It's a standard approach for legacy systems with poor original design documents or source, focused on reviving existing assets rather than building fresh, as forward engineering would.")),
    "glossary": [
        ("역공학", "Reverse Engineering", ("완성본을 보고 개요를 거꾸로 추정하는 일.", "Inferring the outline backward from the finished product."), ("설계 문서가 없을 때 특히 써요.", "Especially useful when design docs are missing.")),
        ("재구조화", "Restructuring", ("내용은 그대로, 구조만 정리정돈하는 일.", "Tidying up structure while keeping content the same."), ("역공학과 재공학 사이 단계예요.", "The stage between reverse engineering and reengineering.")),
        ("재공학", "Reengineering", ("요즘 말로 다시 써서 재출간하는 일.", "Rewriting in today's language and republishing."), ("3R의 마지막 단계예요.", "The final stage of the 3Rs.")),
        ("순공학", "Forward Engineering", ("원고부터 새로 써 내려가는 일.", "Writing a fresh manuscript from scratch."), ("3R과 반대 방향이에요.", "The opposite direction from 3R.")),
        ("레거시 시스템", "Legacy System", ("오래돼서 원본 자료가 부실한 책.", "An old book with poor surviving original materials."), ("3R이 다루는 대상이에요.", "What 3R work is applied to.")),
        ("형상관리", "Configuration Management", ("원고를 보관하는 서가.", "The shelf where manuscripts are kept."), ('원본이 잘 보관됐다면 3R 자체가 필요 없었을 거예요. → <a href="scmshelf-ko.html">원고를 지키는 보관 서가</a>', 'If the original had been kept properly, 3R might not have been needed at all. → <a href="scmshelf-en.html">the shelf that protects the manuscript</a>')),
        ("기술 부채", "Technical Debt", ("나중으로 미룬 정리를 쌓아두는 일.", "Piling up cleanup that keeps getting postponed."), ("오래 쌓이면 3R이 더 커져요.", "The longer it piles up, the bigger the 3R job gets.")),
        ("GoF 디자인패턴", "GoF Design Patterns", ("검증된 글쓰기 공식들의 모음.", "A collection of proven writing formulas."), ('재공학으로 다시 쓸 때 이 공식들을 적용하곤 해요. → <a href="gofpattern-ko.html">검증된 글쓰기 공식집</a>', 'These formulas often get applied while reengineering a rewrite. → <a href="gofpattern-en.html">the collection of proven writing formulas</a>')),
    ],
}
