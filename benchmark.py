import time
import statistics
from graph import Graph
from bellman_ford import bellman_ford
from dijkstra import dijkstra


def bench(n, density, repeats=5):
    g = Graph.random_graph(n, density)
    tb, td = [], []
    for _ in range(repeats):
        t0 = time.perf_counter(); bellman_ford(g, 0); tb.append(time.perf_counter() - t0)
        t0 = time.perf_counter(); dijkstra(g, 0);     td.append(time.perf_counter() - t0)
    return statistics.median(tb), statistics.median(td)


if __name__ == "__main__":
    print(f"{'n':>6} {'m':>8} {'BF, мс':>10} {'DJ, мс':>10} {'ускорение':>10}")
    for n in (100, 200, 500, 1000, 2000):
        density = 0.05
        g = Graph.random_graph(n, density)
        m = sum(1 for _ in g.edges())
        tb, td = bench(n, density)
        print(f"{n:>6} {m:>8} {tb*1000:>10.3f} {td*1000:>10.3f} {tb/td:>9.2f}x")