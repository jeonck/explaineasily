from _draw import *
from _world import *


def partbox(x, y, s=1.0, text="", hl=False):
    fill = "var(--accent-soft)" if hl else "#E9B44C"
    stroke = "var(--accent)" if hl else "#C9822B"
    out = f'<g transform="translate({x},{y}) scale({s})"><circle r="24" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    out += label(0, 6, text, 14, "#142033", cls="d")
    return out + '</g>'


def branch(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#C9822B" stroke-width="3"/>'


# 1. 번호를 모르면 한 줄로 늘어선 박스를 하나씩 다 열어봐야 해요
P1 = svg(320, sky(320)
         + partbox(90, 220, 0.8, "12") + partbox(150, 220, 0.8, "47") + partbox(210, 220, 0.8, "8")
         + partbox(270, 220, 0.8, "63") + partbox(330, 220, 0.8, "31") + partbox(390, 220, 0.8, "19")
         + partbox(450, 220, 0.8, "54") + partbox(510, 220, 0.8, "27", hl=True)
         + person(620, 160, s=0.8, face=SWEAT + EYES, **MECH1)
         + label(380, 30, "⟦부품 #27을 찾아야 하는데, 순서가 뒤죽박죽이에요|need to find part #27, but they're all jumbled up⟧", 13, "var(--ink)", cls="d")
         + label(380, 295, "⟦하나씩 다 열어봐야 해요, 운 나쁘면 끝까지 다 봐야 해요|you have to open them one by one — worst case, every single box⟧", 12, "var(--ink)"))

# 2. 한 줄로 가지런히 정렬해도, 여전히 하나씩 짚어가야 해요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + partbox(90, 200, 0.75, "8") + partbox(150, 200, 0.75, "12") + partbox(210, 200, 0.75, "19")
         + partbox(270, 200, 0.75, "27", hl=True) + partbox(330, 200, 0.75, "31") + partbox(390, 200, 0.75, "47")
         + partbox(450, 200, 0.75, "54") + partbox(510, 200, 0.75, "63")
         + person(630, 150, s=0.75, face=EYES, **MECH1)
         + label(380, 40, "⟦작은 것부터 큰 것까지 한 줄로 늘어놔도|even lined up smallest to largest, in one row⟧", 13, "var(--ink)", cls="d")
         + label(380, 280, "⟦맨 앞부터 하나씩 짚어가야 하는 건 똑같아요|you still have to step through from the front, one at a time⟧", 12, "var(--ink)"))

# 3. 이진트리 탐색 = 갈림길에서 반씩 줄여가는 선반 지도 (hero)
P3 = svg(340, sky(340)
         + branch(380, 90, 230, 170) + branch(380, 90, 530, 170)
         + branch(230, 170, 140, 250) + branch(230, 170, 320, 250)
         + branch(530, 170, 440, 250) + branch(530, 170, 620, 250)
         + partbox(380, 90, 1.0, "31")
         + partbox(230, 170, 0.9, "12") + partbox(530, 170, 0.9, "47")
         + partbox(140, 250, 0.8, "8") + partbox(320, 250, 0.8, "19", hl=True)
         + partbox(440, 250, 0.8, "27") + partbox(620, 250, 0.8, "54")
         + label(380, 25, "⟦이진트리 탐색 = 갈림길마다 왼쪽·오른쪽만 골라 반씩 줄여가는 지도|binary search = pick left or right at every fork, halving the search each time⟧", 13, "var(--ink)", cls="d")
         + label(380, 325, "⟦19를 찾을 땐 31→작으니 왼쪽→12→크니 오른쪽→19|looking for 19: 31→smaller, go left→12→bigger, go right→19⟧", 11, "var(--muted)"))

# 4. 작은 쪽은 왼쪽, 큰 쪽은 오른쪽
P4 = svg(320, sky(320)
         + branch(380, 70, 260, 140) + branch(380, 70, 500, 140)
         + partbox(380, 70, 0.9, "31")
         + partbox(260, 140, 0.8, "&lt;31", hl=True) + partbox(500, 140, 0.8, "&gt;31", hl=True)
         + label(260, 200, "⟦작으면 왼쪽|smaller goes left⟧", 11, "var(--muted)")
         + label(500, 200, "⟦크면 오른쪽|bigger goes right⟧", 11, "var(--muted)")
         + queueboard(560, 230, 160, 70, "⟦BST 규칙|BST RULE⟧", ["⟦왼쪽 &lt; 나 &lt; 오른쪽|left &lt; me &lt; right⟧"], 0.95)
         + label(190, 280, "⟦이 규칙을 모든 갈림길에서 똑같이 지켜요|every single fork follows this same rule⟧", 12, "var(--ink)"))

# 5. 한쪽으로 쏠리면 다시 한 줄처럼 느려져요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + branch(190, 90, 140, 150) + branch(190, 90, 240, 150)
         + branch(140, 150, 115, 210) + branch(140, 150, 165, 210)
         + partbox(190, 90, 0.7, "31") + partbox(140, 150, 0.6, "12") + partbox(240, 150, 0.6, "47")
         + partbox(115, 210, 0.5, "8") + partbox(165, 210, 0.5, "19")
         + label(190, 250, "⟦균형 잡힌 트리는 매번 반씩 줄어요|a balanced tree halves it every step⟧", 11, "var(--ink)")
         + branch(570, 90, 570, 140) + branch(570, 140, 570, 180) + branch(570, 180, 570, 220)
         + partbox(570, 90, 0.6, "8") + partbox(570, 140, 0.55, "12") + partbox(570, 180, 0.5, "19") + partbox(570, 220, 0.45, "27")
         + label(570, 255, "⟦한쪽으로만 쏠리면 다시 한 줄이 돼요|lean all one way, and it's a line again⟧", 11, "var(--ink)")
         + label(380, 282, "⟦그래서 트리의 균형을 맞추는 알고리즘도 따로 있어요|that's why algorithms exist just to rebalance the tree⟧", 12, "var(--ink)", cls="d"))

NODE_I = icon('<circle cx="32" cy="32" r="18" fill="var(--accent)"/>')
LR_I = icon('<path d="M32 12 v16" stroke="#C9822B" stroke-width="3"/><path d="M32 28 L16 44 M32 28 L48 44" stroke="#C9822B" stroke-width="3"/><circle cx="16" cy="48" r="7" fill="var(--good)"/><circle cx="48" cy="48" r="7" fill="var(--bad)"/>')
HALVE_I = icon('<rect x="8" y="26" width="48" height="12" fill="var(--muted)"/><rect x="8" y="26" width="24" height="12" fill="var(--accent)"/>')
BALANCE_I = icon('<path d="M32 10 v44" stroke="var(--muted)" stroke-width="3"/><path d="M10 20 h44" stroke="var(--muted)" stroke-width="3"/><circle cx="10" cy="20" r="7" fill="var(--good)"/><circle cx="54" cy="20" r="7" fill="var(--good)"/>')

PAGE = {
    "slug": "bintree", "order": 10,
    "title": ("갈림길에서 반씩 줄여가는 선반 지도", "The Shelf Map That Halves the Search at Every Fork"),
    "h1": ("<em>이진트리·이진탐색트리</em>가 뭐예요?", "What is a <em>Binary Tree / BST</em>?"),
    "sub": ("이진트리와 이진탐색트리를, 갈림길마다 왼쪽·오른쪽만 골라 부품을 찾는 선반 지도 이야기로 풀어봤어요.",
            "Binary trees and BSTs, told as a story about a shelf map where every fork picks left or right to find a part."),
    "panels": [
        {"svg": P1, "alt": ("번호가 뒤죽박죽인 부품 상자들 사이에서 정비사가 #27을 찾으려 진땀을 흘림", "A mechanic sweats, searching for part #27 among jumbled, out-of-order boxes"),
         "caption": ("번호를 모르면 한 줄로 늘어선 박스를 하나씩 다 열어봐야 해요.", "Without a map, you open boxes one by one down the line."),
         "small": ("운 나쁘면 끝까지 다 봐야 해요.", "Worst case, you check every single one.")},
        {"svg": P2, "alt": ("부품 상자가 작은 번호부터 큰 번호까지 한 줄로 가지런히 정렬되어 있음", "Boxes are neatly lined up from smallest to largest number"),
         "caption": ("한 줄로 가지런히 정렬해도 여전히 하나씩 짚어가야 해요.", "Even sorted in a neat row, you still step through one at a time."),
         "small": ("맨 앞부터 하나씩 짚어가야 하는 건 똑같아요.", "You still have to go front to back, one at a time.")},
        {"svg": P3, "hero": True, "alt": ("31을 뿌리로 왼쪽엔 더 작은 수, 오른쪽엔 더 큰 수가 갈라지는 나무 모양 지도", "A tree-shaped map rooted at 31, branching smaller numbers left and bigger numbers right"),
         "caption": ("이진트리 탐색 = 갈림길마다 반씩 줄여가는 선반 지도예요.", "Binary search = a map that halves the search at every fork."),
         "small": ("19를 찾을 땐 31→작으니 왼쪽→12→크니 오른쪽→19예요.", "Looking for 19: 31→smaller, left→12→bigger, right→19."),
         "tricks": (4, [
             (NODE_I, ("노드", "Node"), ("갈림길 하나, 부품 번호가 적힌 칸", "one fork, a square with a part number")),
             (LR_I, ("왼쪽<나<오른쪽", "Left < Me < Right"), ("작으면 왼쪽, 크면 오른쪽", "smaller goes left, bigger goes right"), "calm"),
             (HALVE_I, ("매번 반씩", "Halving Each Step"), ("한 번 갈 때마다 후보가 절반으로", "each step cuts the candidates in half"), "warm"),
             (BALANCE_I, ("균형(Balance)", "Balance"), ("한쪽으로 쏠리면 효과가 사라져요", "lean too far, and the benefit vanishes")),
         ])},
        {"svg": P4, "alt": ("뿌리 31에서 왼쪽은 더 작은 값, 오른쪽은 더 큰 값이라는 이진탐색트리 규칙을 보여줌", "The root 31 shows the BST rule: smaller values go left, bigger values go right"),
         "caption": ("작은 쪽은 왼쪽, 큰 쪽은 오른쪽이에요.", "Smaller goes left, bigger goes right."),
         "small": ("이 규칙을 모든 갈림길에서 똑같이 지켜요.", "Every single fork follows this same rule.")},
        {"svg": P5, "alt": ("왼쪽: 균형 잡힌 나무가 매번 반씩 줄어듦. 오른쪽: 한쪽으로 쏠린 나무가 한 줄처럼 늘어짐", "Left: a balanced tree halves the search each step. Right: a lopsided tree stretches out like a plain line"),
         "caption": ("한쪽으로 쏠리면 다시 한 줄처럼 느려져요.", "Lean too far one way, and it slows back down to a line."),
         "small": ("그래서 트리의 균형을 맞추는 알고리즘도 따로 있어요.", "That's why algorithms exist just to rebalance the tree.")},
    ],
    "summary": (("<b>이진트리</b> = 갈림길마다 <b>왼쪽·오른쪽 둘로만</b> 갈라지는 지도. <b>이진탐색트리(BST)</b>는 거기에 <b>왼쪽은 작은 값, 오른쪽은 큰 값</b>이라는 규칙을 더한 것.",
                 "<b>Binary tree</b> = a map that branches only left or right at every fork. A <b>binary search tree (BST)</b> adds one rule: smaller values go left, bigger values go right."),
                ("이진트리는 각 노드가 최대 두 자식(왼쪽·오른쪽)을 갖는 트리 구조예요. 이진탐색트리(BST)는 여기에 '왼쪽 서브트리의 모든 값 < 노드 값 < 오른쪽 서브트리의 모든 값' 규칙을 더해, 탐색·삽입·삭제를 평균 O(log n)에 할 수 있게 해요. 하지만 삽입 순서가 한쪽으로 치우치면 트리가 일렬로 늘어서 최악의 경우 O(n)이 되고, 이를 막기 위해 AVL 트리·레드-블랙 트리 같은 균형 트리가 쓰여요.",
                 "A binary tree is a tree structure where each node has at most two children (left and right). A binary search tree (BST) adds the rule that every value in the left subtree is less than the node, and every value in the right subtree is greater — giving average O(log n) search, insert, and delete. But if insertions skew one way, the tree degenerates into a line, with worst-case O(n); self-balancing trees like AVL or red-black trees exist to prevent that.")),
    "glossary": [
        ("노드", "Node", ("갈림길 하나, 부품 번호가 적힌 칸.", "One fork, a square with a part number."), ("최대 두 개의 가지(왼쪽·오른쪽)를 가져요.", "Has at most two branches, left and right.")),
        ("이진탐색트리(BST) 규칙", "BST Rule", ("왼쪽은 작은 값, 오른쪽은 큰 값.", "Smaller to the left, bigger to the right."), ("모든 갈림길에서 똑같이 지켜져요.", "Holds true at every single fork.")),
        ("균형(Balance)", "Balance", ("트리가 한쪽으로 쏠리지 않게 하는 것.", "Keeping the tree from leaning to one side."), ("쏠리면 탐색이 다시 한 줄처럼 느려져요.", "Lean too far, and search slows back to a line.")),
        ("스택·큐(선형 구조)", "Stack/Queue (linear structures)", ("물건을 쌓거나 줄 세우는 한 줄짜리 규칙.", "Rules for a single line — stacking or queuing."), ('가지 없는 \'한 줄\' 구조는 여기서 다뤄요. → <a href="stackqueue-ko.html">상자는 쌓고, 차는 줄 세우고</a>', 'The branch-free, single-line structures live here. → <a href="stackqueue-en.html">boxes get stacked, cars get queued</a>')),
        ("복잡도(Big-O)", "Time Complexity", ("자료가 늘 때 걸리는 시간을 재는 자.", "The ruler for how time grows as data grows."), ('균형 트리는 O(log n), 한 줄은 O(n)이에요. → <a href="bigofunc-ko.html">차가 많아질 때 얼마나 느려질까</a>', 'A balanced tree is O(log n); a plain line is O(n). → <a href="bigofunc-en.html">how much slower as cars pile up</a>')),
        ("캐시 메모리", "Cache Memory", ("자주 쓰는 공구만 담는 작은 공구함.", "A small toolbox holding only the frequent tools."), ('빠르게 찾는 또 다른 방법이에요(구조가 아니라 위치로). → <a href="cachemem-ko.html">자주 쓰는 공구만 담는 공구함</a>', 'Another way to search fast — by location, not structure. → <a href="cachemem-en.html">the toolbox that holds only the frequent tools</a>')),
        ("가상메모리·페이지 테이블", "Virtual Memory/Page Table", ("가상 칸과 진짜 칸의 대응표.", "The table matching virtual slots to real ones."), ('실제로는 페이지 테이블도 트리 모양으로 구현되곤 해요. → <a href="virtualmem-ko.html">창고 전체를 내 것처럼 보여주는 가짜 지도</a>', 'Page tables themselves are often implemented as tree structures. → <a href="virtualmem-en.html">the fake map that makes the whole warehouse yours</a>')),
        ("CPU 스케줄링", "CPU Scheduling", ("순서판에 적힌 차 순서 규칙.", "The rule that sets the car order on the board."), ('일부 스케줄러도 내부적으로 트리 구조를 써요. → <a href="cpusched-ko.html">리프트에 누가 먼저 올라갈까</a>', 'Some schedulers use tree structures internally too. → <a href="cpusched-en.html">who gets the lift first</a>')),
    ],
}
