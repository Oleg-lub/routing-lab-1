from graph import Graph

INF = float("inf")


def bellman_ford(g: Graph, src: int):
    """
    Возвращает (dist, prev).
    dist[v] — кратчайшее расстояние от src до v,
    prev[v] — предшественник v на кратчайшем пути.
    Обнаруживает отрицательные циклы.
    """
    dist = [INF] * g.n
    prev = [None] * g.n
    dist[src] = 0

    for _ in range(g.n - 1):
        updated = False
        for u, v, w in g.edges():
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:          # ранняя остановка
            break

    # проверка на отрицательный цикл
    for u, v, w in g.edges():
        if dist[u] != INF and dist[u] + w < dist[v]:
            raise ValueError("Граф содержит отрицательный цикл")

    return dist, prev


def reconstruct_path(prev, src: int, dst: int):
    if src == dst:
        return [src]
    if prev[dst] is None:
        return []
    path = [dst]
    while path[-1] != src:
        path.append(prev[path[-1]])
        if path[-1] is None:
            return []
    return path[::-1]