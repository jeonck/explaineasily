from _draw import *
from _world import *


def branch(x, y, s=1.0, label_text=None):
    """정비공장 지점(그래프의 노드)."""
    out = f'<g transform="translate({x},{y}) scale({s})"><circle r="16" fill="var(--panel)" stroke="var(--accent)" stroke-width="3"/>'
    if label_text:
        out += label(0, 32, label_text, 11, "var(--ink)")
    return out + '</g>'


def pipe(x1, y1, x2, y2, cost, used=False, skipped=False):
    color = "var(--good)" if used else ("var(--bad)" if skipped else "var(--line)")
    dash = ' stroke-dasharray="5 4"' if skipped else ""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 10
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="4"{dash}/>'
            + label(mx, my, str(cost), 12, color, cls="d"))


# 1. 다섯 지점을 다 배관으로 연결해야 해요
P1 = svg(300, sky(300)
         + branch(140, 150, 1.0, "A") + branch(320, 100, 1.0, "B") + branch(500, 150, 1.0, "C") + branch(380, 250, 1.0, "D") + branch(600, 240, 1.0, "E")
         + pipe(140, 150, 320, 100, 7) + pipe(320, 100, 500, 150, 4) + pipe(140, 150, 380, 250, 6)
         + pipe(500, 150, 380, 250, 3) + pipe(500, 150, 600, 240, 5) + pipe(380, 250, 600, 240, 8) + pipe(320, 100, 380, 250, 9)
         + person(680, 140, s=0.7, face=EYES, **CHIEF)
         + label(380, 40, "⟦지점 다섯 곳을 전부 배관으로 이어야 해요|all five branches must be piped together⟧", 13, "var(--ink)")
         + label(380, 285, "⟦길도 많고 비용도 제각각이라 고민이에요|so many possible paths, each a different cost⟧", 12, "var(--muted)"))

# 2. 아무 배관이나 다 놓으면 돈이 너무 많이 들어요
P2 = svg(300, '<rect width="760" height="300" fill="var(--bad-soft)"/>'
         + branch(140, 150, 1.0, "A") + branch(320, 100, 1.0, "B") + branch(500, 150, 1.0, "C") + branch(380, 250, 1.0, "D") + branch(600, 240, 1.0, "E")
         + pipe(140, 150, 320, 100, 7, used=True) + pipe(320, 100, 500, 150, 4, used=True) + pipe(140, 150, 380, 250, 6, used=True)
         + pipe(500, 150, 380, 250, 3, used=True) + pipe(500, 150, 600, 240, 5, used=True) + pipe(380, 250, 600, 240, 8, used=True) + pipe(320, 100, 380, 250, 9, used=True)
         + label(380, 40, "⟦배관을 전부 다 놓으면 연결은 되지만 돈이 너무 들어요|piping every path connects everything, but costs far too much⟧", 13, "var(--ink)")
         + label(380, 285, "⟦꼭 필요한 배관만 골라 돈을 아끼고 싶어요|we want only the needed pipes to save money⟧", 12, "var(--muted)"))

# 3. 최소신장트리 = 가장 싼 배관만 골라 사이클 없이 모두 잇는 것 (hero)
P3 = svg(340, sky(340)
         + branch(140, 170, 1.0, "A") + branch(320, 120, 1.0, "B") + branch(500, 170, 1.0, "C") + branch(380, 270, 1.0, "D") + branch(600, 260, 1.0, "E")
         + pipe(320, 120, 500, 170, 4, used=True) + pipe(140, 170, 380, 270, 6, used=True)
         + pipe(500, 170, 380, 270, 3, used=True) + pipe(500, 170, 600, 260, 5, used=True)
         + pipe(140, 170, 320, 120, 7, skipped=True) + pipe(380, 270, 600, 260, 8, skipped=True) + pipe(320, 120, 380, 270, 9, skipped=True)
         + label(380, 30, "⟦최소신장트리 = 가장 싼 배관만 골라 사이클 없이 모두 잇는 것|MST: pick only the cheapest pipes, no loops, connecting everyone⟧", 13, "var(--ink)", cls="d")
         + label(380, 320, "⟦초록 배관 네 개(3+4+5+6)만으로 다섯 지점이 다 이어져요|just four green pipes (3+4+5+6) connect all five branches⟧", 12, "var(--muted)"))

CHEAP_I = icon('<path d="M10 40 h44" stroke="var(--ink)" stroke-width="3"/><rect x="14" y="22" width="8" height="18" fill="var(--good)"/><rect x="28" y="30" width="8" height="10" fill="var(--good)"/><rect x="42" y="16" width="8" height="24" fill="var(--line)"/>')
NOLOOP_I = icon('<circle cx="24" cy="24" r="8" fill="var(--accent)"/><circle cx="44" cy="24" r="8" fill="var(--accent)"/><circle cx="34" cy="44" r="8" fill="var(--accent)"/><path d="M24 24 L44 24 M24 24 L34 44" stroke="var(--good)" stroke-width="3"/><path d="M44 24 L34 44" stroke="var(--bad)" stroke-width="3" stroke-dasharray="3 3"/>')
GROW_I = icon('<circle cx="20" cy="32" r="8" fill="var(--good)"/><circle cx="44" cy="20" r="8" fill="var(--line)"/><circle cx="44" cy="44" r="8" fill="var(--line)"/><path d="M20 32 L44 20" stroke="var(--good)" stroke-width="3"/>')
PICKALL_I = icon('<circle cx="16" cy="20" r="7" fill="var(--line)"/><circle cx="32" cy="14" r="7" fill="var(--line)"/><circle cx="48" cy="22" r="7" fill="var(--line)"/><circle cx="24" cy="38" r="7" fill="var(--line)"/><circle cx="42" cy="40" r="7" fill="var(--line)"/><path d="M16 20 L24 38 M24 38 L32 14 M32 14 L48 22 M48 22 L42 40" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="3 3"/>')

# 4. 크루스칼 vs 프림 두 가지 고르는 방법
P4 = svg(320, sky(320)
         + queueboard(60, 40, 320, 240, "⟦크루스칼 — 싼 길부터 고르기|Kruskal — pick cheapest first⟧",
                      ("⟦모든 배관을 값싼 순으로 줄 세워요|line up every pipe by cost⟧",
                       "⟦사이클만 안 생기면 계속 골라요|keep picking as long as no loop forms⟧",
                       "⟦전체를 내려다보며 골라요|chooses by looking at everything at once⟧"), 1.0)
         + queueboard(410, 40, 300, 240, "⟦프림 — 한 지점에서 넓혀가기|Prim — grow from one branch⟧",
                      ("⟦한 지점에서 시작해요|starts from a single branch⟧",
                       "⟦이미 이어진 곳 중 가장 싼 길만 넓혀가요|extends by the cheapest edge from what's connected⟧",
                       "⟦연결망을 점점 키워가요|grows the connected network step by step⟧"), 1.0, hl=1))

# 5. 가장 싼 길만 고집하면 끊길 수도 있어요
P5 = svg(300, '<rect width="380" height="300" fill="var(--good-soft)"/><rect x="380" width="380" height="300" fill="var(--bad-soft)"/>'
         + branch(150, 140, 0.9, "A") + branch(230, 190, 0.9, "B") + pipe(150, 140, 230, 190, 3, used=True)
         + label(190, 250, "⟦무조건 싼 것만 고르되, 이미 이어졌으면 건너뛰어요|always pick cheap, but skip it if it would reconnect⟧", 11, "var(--ink)")
         + branch(560, 140, 0.9, "C") + branch(640, 140, 0.9, "D") + branch(600, 220, 0.9, "E")
         + pipe(560, 140, 640, 140, 2, skipped=True)
         + label(600, 260, "⟦사이클을 막는 규칙을 빼먹으면 빙 둘러 연결돼 돈이 또 새요|skip the no-loop rule, and money leaks right back out⟧", 11, "var(--ink)")
         + label(380, 282, "⟦'가장 싸게'와 '사이클 없이' 둘 다 지켜야 진짜 최소신장트리예요|both 'cheapest' and 'no loop' must hold for a true MST⟧", 12, "var(--ink)", cls="d"))

PAGE = {
    "slug": "mstalgo", "order": 22,
    "title": ("가장 싼 배관만 골라 모든 지점 잇기", "Piping Every Branch Together for the Least Cost"),
    "h1": ("<em>최소신장트리(MST)</em>가 뭐예요?", "What is a <em>Minimum Spanning Tree (MST)</em>?"),
    "sub": ("최소신장트리를, 정비공장 여러 지점을 가장 싼 배관만 골라 사이클 없이 모두 연결하는 이야기로 풀어봤어요.",
            "Minimum spanning trees, told as a story about piping every garage branch together using only the cheapest connections, with no loops."),
    "panels": [
        {"svg": P1, "alt": ("다섯 지점 A~E가 여러 가능한 배관 경로와 비용으로 얽혀 있음", "Five branches A–E tangled in many possible pipe routes, each with a different cost"),
         "caption": ("지점 다섯 곳을 전부 배관으로 이어야 해요.", "All five branches must be piped together."),
         "small": ("길도 많고 비용도 제각각이라 고민이에요.", "So many possible paths, each a different cost.")},
        {"svg": P2, "alt": ("모든 배관을 다 놓아 다섯 지점이 연결되지만 비용이 과도함", "All pipes are laid, connecting every branch, but at excessive cost"),
         "caption": ("아무 배관이나 다 놓으면 돈이 너무 많이 들어요.", "Laying every possible pipe connects everything, but costs far too much."),
         "small": ("꼭 필요한 배관만 골라 돈을 아끼고 싶어요.", "We want only the needed pipes to save money.")},
        {"svg": P3, "hero": True, "alt": ("가장 싼 배관 네 개만 초록색으로 남고 나머지는 점선으로 빠져 다섯 지점이 모두 연결됨", "Only the four cheapest pipes stay green while the rest are dashed out, still connecting all five branches"),
         "caption": ("최소신장트리는 가장 싼 배관만 골라 사이클 없이 모두 잇는 것이에요.", "An MST picks only the cheapest pipes, with no loops, to connect everyone."),
         "small": ("초록 배관 네 개만으로 다섯 지점이 다 이어져요.", "Just four green pipes connect all five branches."),
         "tricks": (4, [
             (CHEAP_I, ("가장 싼 것부터", "Cheapest first"), ("비용이 적은 배관을 먼저 봐요", "looks at the lowest-cost pipe first"), "calm"),
             (NOLOOP_I, ("사이클 금지", "No cycles allowed"), ("이미 이어진 곳은 다시 안 이어요", "skips a pipe that would just loop back")),
             (GROW_I, ("연결망 넓히기", "Grow the network"), ("이어진 범위를 조금씩 키워요", "extends the connected set step by step")),
             (PICKALL_I, ("다섯 지점 모두 연결", "Connect all five branches"), ("하나도 빠짐없이 이어져요", "every branch ends up connected"), "warm"),
         ])},
        {"svg": P4, "alt": ("크루스칼은 모든 배관을 값싼 순으로 줄 세워 고르고, 프림은 한 지점에서 시작해 연결망을 넓혀가는 두 방법 비교표", "A board comparing Kruskal (sorts all edges by cost) and Prim (grows outward from one branch)"),
         "caption": ("고르는 방법은 두 가지가 있어요.", "There are two ways to pick the pipes."),
         "small": ("크루스칼은 전체를 보고, 프림은 한 곳에서 넓혀가요.", "Kruskal looks at everything at once; Prim grows from one point.")},
        {"svg": P5, "alt": ("왼쪽: 싼 길을 고르되 이미 이어졌으면 건너뜀. 오른쪽: 사이클 금지 규칙을 빼먹으면 돈이 다시 샘", "Left: pick cheap, but skip if already connected. Right: skipping the no-loop rule lets money leak out again"),
         "caption": ("가장 싼 길만 고집하면 사이클이 생길 수 있어요.", "Chasing only the cheapest path can create a cycle."),
         "small": ("'가장 싸게'와 '사이클 없이' 둘 다 지켜야 진짜 MST예요.", "Both 'cheapest' and 'no loop' must hold for a true MST.")},
    ],
    "summary": (("<b>최소신장트리(MST)</b>는 여러 지점을 <b>가장 싼 비용의 길</b>만 골라 <b>사이클 없이 전부 연결</b>하는 방법이에요.",
                 "A <b>minimum spanning tree (MST)</b> connects every point using only the <b>lowest-cost edges</b>, with <b>no cycles</b>, so all points stay linked."),
                ("최소신장트리는 가중치가 있는 그래프에서 모든 정점을 사이클 없이 연결하면서 간선 가중치의 합이 최소가 되는 부분 그래프예요. 크루스칼 알고리즘은 모든 간선을 가중치 순으로 정렬한 뒤, 사이클을 만들지 않는 한 가장 싼 간선부터 차례로 선택해요(유니온-파인드로 사이클을 검사). 프림 알고리즘은 한 정점에서 시작해 이미 연결된 집합과 바깥을 잇는 가장 싼 간선을 반복해서 추가하며 트리를 키워가요. 둘 다 정점이 n개면 간선이 n-1개인 트리가 만들어져요.",
                 "A minimum spanning tree is a subgraph of a weighted graph that connects every vertex, has no cycles, and minimizes the total edge weight. Kruskal's algorithm sorts all edges by weight and repeatedly adds the cheapest one that doesn't create a cycle (checked via union-find). Prim's algorithm starts from one vertex and repeatedly adds the cheapest edge connecting the growing tree to the outside, growing the tree one edge at a time. Both produce a tree with n-1 edges for n vertices.")),
    "glossary": [
        ("최소신장트리(MST)", "Minimum Spanning Tree", ("가장 싼 배관으로 모두 잇는 연결망.", "The network that connects everyone using the cheapest pipes."), ("정점이 n개면 간선은 n-1개예요.", "n vertices means n-1 edges.")),
        ("크루스칼 알고리즘", "Kruskal's Algorithm", ("싼 배관부터 차례로 고르는 방법.", "The method of picking cheap pipes in order."), ("전체 배관을 미리 정렬해두고 골라요.", "Sorts all edges up front, then picks.")),
        ("프림 알고리즘", "Prim's Algorithm", ("한 지점에서 시작해 넓혀가는 방법.", "The method of growing outward from one branch."), ("이미 이은 곳에서 가장 싼 길만 넓혀가요.", "Extends only via the cheapest edge from what's connected.")),
        ("사이클(순환)", "Cycle", ("배관이 빙 둘러 다시 이어지는 것.", "Pipes looping back to reconnect the same branches."), ("MST에서는 생기면 안 돼요.", "Must never occur in an MST.")),
        ("가중치 그래프", "Weighted Graph", ("배관마다 비용이 적힌 지도.", "The map with a cost written on every pipe."), ("MST는 이 비용의 합을 최소화해요.", "An MST minimizes the sum of these costs.")),
        ("유니온-파인드", "Union-Find", ("이미 이어졌는지 빠르게 확인하는 도구.", "The tool that quickly checks if two branches are already connected."), ("크루스칼에서 사이클 검사에 써요.", "Used by Kruskal to check for cycles.")),
        ("탐욕 알고리즘", "Greedy Algorithm", ("매번 당장 가장 싼 것을 고르는 전략.", "The strategy of always picking the cheapest option right now."), ("크루스칼·프림 둘 다 이 전략이에요.", "Both Kruskal and Prim follow this strategy.")),
        ("최단경로 알고리즘", "Shortest Path Algorithm", ("두 지점 사이 가장 싼 '한 길'을 찾는 것.", "Finding the single cheapest route between two specific points."), ("MST는 '모두 잇기'가 목표라 다른 문제예요.", "A different problem — MST's goal is connecting everyone, not one pair.")),
    ],
}
