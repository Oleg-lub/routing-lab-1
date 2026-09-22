from graph import Graph
from bellman_ford import bellman_ford, reconstruct_path as bf_path
from dijkstra import dijkstra
from bellman_ford import reconstruct_path as dj_path
import time


def main():
    n = int(input("Число вершин n (>100 для теста): "))
    density = float(input("Плотность рёбер (0..1, напр. 0.05): "))
    src = int(input("Вершина-источник: "))
    dst = int(input("Вершина-получатель: "))

    g = Graph.random_graph(n, density)

    t0 = time.perf_counter()
    d_bf, p_bf = bellman_ford(g, src)
    t_bf = time.perf_counter() - t0

    t0 = time.perf_counter()
    d_dj, p_dj = dijkstra(g, src)
    t_dj = time.perf_counter() - t0

    path_bf = bf_path(p_bf, src, dst)
    path_dj = dj_path(p_dj, src, dst)

    print(f"\nБеллман-Форд: d({dst}) = {d_bf[dst]}, "
          f"путь = {path_bf}, время = {t_bf*1000:.3f} мс")
    print(f"Дейкстра:     d({dst}) = {d_dj[dst]}, "
          f"путь = {path_dj}, время = {t_dj*1000:.3f} мс")
    assert d_bf[dst] == d_dj[dst], "Расхождение результатов!"
    print("Результаты совпадают.")


if __name__ == "__main__":
    main()