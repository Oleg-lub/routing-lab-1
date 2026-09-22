import heapq
from graph import Graph

INF = float("inf")


def dijkstra(g: Graph, src: int):
    """Алгоритм Дейкстры с бинарной пирамидой."""
    dist = [INF] * g.n
    prev = [None] * g.n
    dist[src] = 0
    visited = [False] * g.n
    heap = [(0, src)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in g.adj[u]:
            if d_u + w < dist[v]:
                dist[v] = d_u + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, prev