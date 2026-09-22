import random
from collections import defaultdict


class Graph:
    """Взвешенный ориентированный граф."""

    def __init__(self, n: int):
        self.n = n
        self.adj = defaultdict(list)  # u -> [(v, w), ...]

    def add_edge(self, u: int, v: int, w: float):
        self.adj[u].append((v, w))

    def edges(self):
        for u in self.adj:
            for v, w in self.adj[u]:
                yield u, v, w

    @staticmethod
    def random_graph(n: int, density: float = 0.1,
                     max_w: int = 100, seed: int = 42) -> "Graph":
        """Связный граф: дерево + случайные рёбра."""
        rnd = random.Random(seed)
        g = Graph(n)
        # каркас связности — дерево
        for v in range(1, n):
            u = rnd.randint(0, v - 1)
            w = rnd.randint(1, max_w)
            g.add_edge(u, v, w)
            g.add_edge(v, u, w)
        # дополнительные рёбра
        extra = int(density * n * (n - 1) / 2)
        for _ in range(extra):
            u = rnd.randint(0, n - 1)
            v = rnd.randint(0, n - 1)
            if u != v:
                g.add_edge(u, v, rnd.randint(1, max_w))
        return g