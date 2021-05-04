if __name__ == "__main__":
    #realizations = 10
    #ns = [10, 20, 50, 100, 250, 500, 1000]
    #ps = [0.1, 0.3, 0.5]

    ns = [10, 20, 50, 100, 250, 500, 1000]

    import numpy as np
    import networkx as nx

    # 0: PTA
    # 1: FBA
    # 2: n of edges

    results = np.zeros((len(ns), 4))
    for n_idx, n in enumerate(ns):
        print('doing n={}'.format(n))

        graph = nx.complete_graph(n, create_using=nx.DiGraph)

        setup = """\
import networkx as nx
from bisimulation_algorithms import paige_tarjan, dovier_piazza_policriti

graph = nx.complete_graph({}, create_using=nx.DiGraph)

import sys
sys.setrecursionlimit(20000)""" .format(n)

        import timeit
        pta = timeit.timeit('paige_tarjan(graph, is_integer_graph=True)', setup=setup, number=100) / 100
        fba = timeit.timeit('dovier_piazza_policriti(graph, is_integer_graph=True)', setup=setup, number=100) / 100

        results[n_idx] = np.array([pta, fba, len(graph.nodes), len(graph.edges)])

        print('\t{},{}'.format(pta, fba))
    np.save('bisi/complete/result.npy', results)
