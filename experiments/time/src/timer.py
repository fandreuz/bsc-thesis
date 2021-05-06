from itertools import product

if __name__ == "__main__":
    ns = [10, 20, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 11000]
    ratios = range(1,10)

    import numpy as np
    import networkx as nx
    from itertools import chain

    # 0: PTA
    # 1: FBA
    # 2: n of edges

    ratio = 2

    results = np.zeros((len(ns), len(ratios), 4))
    for n_idx, n in enumerate(ns):
        print('doing n={}'.format(n))
        for r_idx, ratio in enumerate(ratios):
            print('\tr={}'.format(ratio))
            p = ratio / n
            graph = nx.fast_gnp_random_graph(n, p, directed=True)

            setup = """\
import networkx as nx
from bisimulation_algorithms import paige_tarjan, dovier_piazza_policriti

graph = nx.DiGraph()
graph.add_nodes_from(range({}))
graph.add_edges_from({})

import sys
sys.setrecursionlimit(20000)""" .format(n,list(graph.edges))
            import timeit
            pta = timeit.timeit('paige_tarjan(graph, is_integer_graph=False)', setup=setup, number=10) / 10
            fba = timeit.timeit('dovier_piazza_policriti(graph, is_integer_graph=False)', setup=setup, number=10) / 10

            results[n_idx, r_idx] = np.array([pta, fba, len(graph.nodes), len(graph.edges)])

            print('\t\t{},{}'.format(pta, fba))
    np.save('bisi/random/result.npy', results)
