from _draw import *
from _world import *

# 1. 남이 우리 자료를 보려면 매번 전화해서 따로 부탁해야 해요
P1 = svg(300, sky(300)
         + bookshelf(320, 110, 1.1, n=4)
         + person(150, 150, s=0.8, face=EYES, **READER) + bubble(60, 70, 180, 40, "⟦그 자료 좀 볼 수 있을까요?|could I take a look at that data?⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + person(600, 150, s=0.8, face=SWEAT, **EDITOR) + bubble(500, 70, 220, 40, "⟦음… 양식부터 다시 설명드릴게요|um... let me explain the form again⟧", 11, "var(--panel)", "var(--line)", "bottom")
         + label(380, 280, "⟦사람마다 요청 방식이 달라서 매번 새로 설명해야 해요|every requester asks differently, so it's explained from scratch each time⟧", 12, "var(--bad)"))

# 2. 양식이 저마다 달라 확인하는 데 오래 걸려요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + manuscript(180, 140, 0.55, marks=1) + manuscript(300, 140, 0.55, marks=2) + manuscript(420, 140, 0.55) + manuscript(540, 140, 0.55, marks=1)
         + label(380, 70, "⟦신청서마다 양식이 다 달라요|every request form looks different⟧", 13, "var(--ink)", cls="d")
         + person(380, 200, s=0.55, face=FROWN, **EDITOR)
         + label(380, 290, "⟦편집장이 하나하나 다시 확인해야 해서 느려요|the editor has to check each one by hand — slow going⟧", 12, "var(--muted)"))

# 3. 개방형 API = 표준 신청서식을 공개한 열람실 (hero)
FORM_I = icon('<rect x="12" y="8" width="40" height="48" rx="3" fill="#FFF8E7" stroke="#C9A86A" stroke-width="3"/><path d="M20 20 h24 M20 30 h24 M20 40 h16" stroke="#142033" stroke-width="2.5"/><path d="M38 44 l6 6 l10 -12" stroke="var(--good)" stroke-width="3" fill="none" stroke-linecap="round"/>')
DESK_I = icon('<rect x="8" y="34" width="48" height="10" rx="2" fill="var(--stone-dark)"/><rect x="14" y="14" width="36" height="20" rx="3" fill="var(--panel)" stroke="var(--line)" stroke-width="2"/>')
KEY_I = icon('<circle cx="22" cy="24" r="10" fill="none" stroke="#E9B44C" stroke-width="5"/><rect x="30" y="22" width="22" height="6" fill="#E9B44C"/><rect x="44" y="28" width="6" height="8" fill="#E9B44C"/>')
SCOPE2_I = icon('<rect x="10" y="12" width="44" height="40" rx="3" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M10 28 H54" stroke="var(--accent)" stroke-width="3" stroke-dasharray="4 3"/>')

P3 = svg(340, sky(340)
         + label(380, 30, "⟦개방형 API = 표준 신청서식을 공개한 열람실|Open API = a reading room whose request form is published as a standard⟧", 13, "var(--ink)", cls="d")
         + bookshelf(560, 150, 1.1, n=3)
         + person(330, 210, s=0.7, face=SMILE, **READER)
         + styleguide(70, 90, 220, 160, "⟦표준 신청서식|STANDARD REQUEST FORM⟧",
                      ("⟦무엇을: 분야·범위|what: topic and scope⟧", "⟦어떻게: 정해진 형식으로|how: in the fixed format⟧", "⟦받기: 바로 자동으로|get it: automatically, right away⟧"), 0.95)
         + label(380, 325, "⟦이 서식대로만 쓰면, 누구나 바로 자료를 빌려볼 수 있어요|fill out this one form, and anyone can borrow the data right away⟧", 12, "var(--muted)"))

PAGE = {
    "slug": "openapi", "order": 21,
    "title": ("서식 하나로 열어둔 열람실", "The Reading Room Opened With a Single Form"),
    "h1": ("<em>개방형 API(Open API)</em>가 뭐예요?", "What is an <em>Open API</em>?"),
    "sub": ("개방형 API를, 전화로 매번 따로 부탁하는 대신 표준 신청서식 하나로 누구나 자료를 빌려볼 수 있게 연 열람실 이야기로 풀어봤어요.",
            "Open API, told as a story about a reading room opened with one standard request form, instead of everyone calling in separately to ask."),
    "panels": [
        {"svg": P1, "alt": ("독자가 '그 자료 좀 볼 수 있을까요?' 묻고, 편집장은 땀을 흘리며 '양식부터 다시 설명드릴게요'라고 말함", "A reader asks to see the data, and a sweating editor says they'll have to explain the form again from scratch"),
         "caption": ("남이 우리 자료를 보려면 매번 전화해서 따로 부탁해야 해요.", "To see our data, outsiders have to call in and ask separately every time."),
         "small": ("사람마다 요청 방식이 달라서 매번 새로 설명해야 해요.", "Every requester asks differently, so it's explained from scratch each time.")},
        {"svg": P2, "alt": ("저마다 다른 모양의 신청서 네 장과, 하나하나 확인하느라 지친 편집장", "Four request forms, each shaped differently, and a weary editor checking them one by one"),
         "caption": ("양식이 저마다 달라 확인하는 데 오래 걸려요.", "Every form looks different, so checking takes a long time."),
         "small": ("편집장이 하나하나 다시 확인해야 해서 느려요.", "The editor has to check each one by hand — slow going.")},
        {"svg": P3, "hero": True, "alt": ("표준 신청서식 안내판 앞에서 독자가 웃으며 서가를 바라봄", "A reader smiles toward the shelf, standing before a sign showing the standard request form"),
         "caption": ("개방형 API는 표준 신청서식을 공개한 열람실이에요.", "An Open API is a reading room whose request form is published as a standard."),
         "small": ("이 서식대로만 쓰면, 누구나 바로 자료를 빌려볼 수 있어요.", "Fill out this one form, and anyone can borrow the data right away."),
         "tricks": (4, [
             (FORM_I, ("신청서식 표준화", "Standardize the form"), ("요청 방법을 미리 정해 공개해요", "the request format is fixed and published"), "calm"),
             (DESK_I, ("열람 창구 열기", "Open a reading desk"), ("서식대로 오면 누구나 받아줘요", "anyone using the form gets served")),
             (KEY_I, ("이용키 발급", "Issue a usage key"), ("누가 빌려 가는지는 확인해요", "but who's borrowing is still tracked")),
             (SCOPE2_I, ("이용 범위 정하기", "Set the usage scope"), ("어디까지 빌릴 수 있는지 정해둬요", "how much can be borrowed is set in advance"), "warm"),
         ])},
        {"svg": svg(320, '<rect width="760" height="320" fill="var(--good-soft)"/>'
                    + styleguide(60, 30, 640, 250, "⟦신청서식 명세서|THE REQUEST FORM SPEC⟧",
                                 ("⟦요청 항목: 어떤 자료를, 어떤 조건으로|request fields: which data, under what conditions⟧",
                                  "⟦응답 형식: 정해진 모양으로 돌려줘요|response format: comes back in a fixed shape⟧",
                                  "⟦이용키: 신청하면 자동으로 발급|usage key: issued automatically on request⟧",
                                  "⟦이 명세서만 보면, 코드를 몰라도 신청할 수 있어요|read just this spec, and you can request it without knowing any code⟧"), 1.0)),
         "alt": ("요청 항목, 응답 형식, 이용키 발급 절차를 적은 신청서식 명세서", "A spec sheet listing request fields, response format, and the usage-key issuing process"),
         "caption": ("이 명세서 하나로 누구나 신청할 수 있어요.", "This one spec sheet lets anyone make a request."),
         "small": ("무엇을 어떻게 요청하고, 무엇을 돌려받는지 미리 다 적혀 있어요.", "What to ask for and how, and what comes back — all written down in advance.")},
        {"svg": svg(300, sky(300)
                    + person(190, 150, s=0.8, face=SMILE, **EDITOR) + label(190, 265, "⟦열람실은 열었어요|the reading room is open⟧", 11, "var(--ink)")
                    + person(560, 150, s=0.8, face=EYES, **PRINTER) + label(560, 265, "⟦몰리는 줄은 안내소가 따로 맡아요|the front gate handles the crowding, separately⟧", 11, "var(--ink)")
                    + label(380, 30, "⟦여는 것과 줄 세우는 건 다른 일이에요|opening it and managing the line are different jobs⟧", 13, "var(--bad)", cls="d")),
         "alt": ("편집장은 열람실을 열었다 말하고, 인쇄 감독은 몰리는 줄은 안내소가 따로 맡는다고 말함", "The editor says the reading room is open; the print supervisor says the crowding is handled separately, by the front gate"),
         "caption": ("여는 것과 줄 세우는 건 다른 일이에요.", "Opening it and managing the line are different jobs."),
         "small": ('개방형 API는 무엇을 공개할지의 정책이고, 몰려드는 요청을 실제로 다루는 건 → <a href="apigateway-ko.html">정문 안내소</a> 쪽 몫이에요.',
                   'Open API is the policy of what to make public — handling the flood of requests itself is the job of → <a href="apigateway-en.html">the front gate information booth</a>.')},
    ],
    "summary": (("<b>개방형 API(Open API)</b> = 전화로 매번 따로 부탁하는 대신, <b>표준 신청서식</b>을 미리 공개해서 <b>누구나 같은 방식으로</b> 자료를 빌려볼 수 있게 하는 것.",
                 "<b>Open API</b> = instead of everyone calling in separately, publishing a <b>standard request form</b> in advance so <b>anyone can use the same way</b> to borrow the data."),
                ("개방형 API는 공공기관이나 기업이 보유한 데이터·기능을 표준화된 명세(요청 형식, 응답 형식, 인증 방식)로 외부에 공개해, 누구나 이 명세대로 요청하면 이용할 수 있게 하는 정책이자 기술 방식이에요. OpenAPI(Swagger) 같은 명세 표준으로 문서화하고, 이용키 발급과 쿼터로 이용 범위를 관리해요. 공공데이터포털의 '오픈API'가 대표적인 예예요.",
                 "An Open API is both a policy and a technical approach: a public institution or company publishes its data or functionality externally through a standardized spec (request format, response format, authentication method), so that anyone following that spec can use it. It's documented with a spec standard like OpenAPI (Swagger), with usage keys and quotas managing how much gets used. Korea's public data portal 'Open API' is a well-known example.")),
    "glossary": [
        ("개방형 API", "Open API", ("표준 서식 하나로 연 열람실.", "The reading room opened with one standard form."), ("누구나 같은 방식으로 자료를 요청해요.", "Anyone can request data the same way.")),
        ("API 명세(스펙)", "API Specification", ("신청서식 그 자체를 적은 문서.", "The document that writes down the request form itself."), ('OpenAPI(Swagger) 같은 표준으로 적어요.', 'Written using a standard like OpenAPI (Swagger).')),
        ("이용키(인증키)", "API Key", ("누가 빌려 가는지 확인하는 열쇠.", "The key that confirms who's borrowing."), ("신청하면 자동으로 발급돼요.", "Issued automatically once you apply.")),
        ("공공데이터포털", "Public Data Portal", ("정부가 연 가장 큰 열람실.", "The government's biggest reading room of all."), ("수많은 기관의 개방형 API가 여기 모여 있어요.", "Open APIs from many agencies are gathered here.")),
        ("데이터 표준화", "Data Standardization", ("응답 모양을 다 같이 맞추는 것.", "Making the response shape the same for everyone."), ("모양이 다르면 서식이 있어도 쓰기 어려워요.", "Even with a form, a mismatched shape is hard to use.")),
        ("API 게이트웨이", "API Gateway", ("몰려드는 요청을 실제로 다루는 안내소.", "The booth that actually handles the flood of requests."), ('개방형 API는 정책, 게이트웨이는 그 요청을 다루는 인프라예요 → <a href="apigateway-ko.html">정문 안내소</a>.', 'Open API is the policy; the gateway is the infrastructure that handles the requests → <a href="apigateway-en.html">the front gate information booth</a>.')),
        ("EIF(외부연계파일)", "External Interface File", ("다른 출판사 자료를 참고하는 연결점.", "The connection point for referencing another publisher's data."), ('규모를 잴 때 이 연결도 하나로 세어요 → <a href="fpruler-ko.html">매수를 재는 자</a>.', 'This kind of link gets counted too, when sizing up the work → <a href="fpruler-en.html">the ruler that measures page count</a>.')),
        ("이용 쿼터", "Usage Quota", ("한 열쇠로 하루에 빌릴 수 있는 한도.", "The daily limit on how much one key can borrow."), ("너무 많이 요청하면 그날은 더 못 빌려요.", "Ask too much, and that key is done for the day.")),
    ],
}
