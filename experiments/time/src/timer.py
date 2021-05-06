if __name__ == "__main__":
    ns = [10, 20, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 11000]
    numbers = [100, 100, 100, 100, 100, 100, 25, 25, 25, 15, 15, 10, 5]

    import numpy as np
    import networkx as nx
    from itertools import chain

    # 0: PTA
    # 1: FBA
    # 2: n of edges

    n = 2
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1,n+1))
    graph.add_edges_from([(i, n // 2 + 2 * i - 1) for i in range(1, n+1)])
    graph.add_edges_from([(n//2+i, 2*i-1) for i in range(n//2+1, n+1)])
    graph.add_edges_from([(n // 4 + 1, 2 * i - 1) for i in range(1, n // 4 + 1)])

    print(graph.edges)

    results = np.zeros((len(ns), 4))
    for n_idx, n, number in zip(range(len(ns)), ns, numbers):
        print('doing n={}'.format(n))

        graph = nx.DiGraph()
        graph.add_nodes_from(range(1,n+1))
        graph.add_edges_from([(i, n // 2 + 2 * i - 1) for i in range(1, n+1)])
        graph.add_edges_from([(n//2+i, 2*i-1) for i in range(n//2+1, n+1)])
        graph.add_edges_from([(n//4+1, 2*i-1) for i in range(1,n//4+1)])

        setup = """\
import networkx as nx
from bisimulation_algorithms import paige_tarjan, dovier_piazza_policriti

graph = nx.DiGraph()
graph.add_nodes_from(range({}))
graph.add_edges_from({})

import sys
sys.setrecursionlimit(20000)""" .format(n,list(graph.edges))

        import timeit
        pta = timeit.timeit('paige_tarjan(graph, is_integer_graph=False)', setup=setup, number=number) / number
        fba = timeit.timeit('dovier_piazza_policriti(graph, is_integer_graph=False)', setup=setup, number=number) / number

        results[n_idx] = np.array([pta, fba, len(graph.nodes), len(graph.edges)])

        print('\t{},{}'.format(pta, fba))
    np.save('bisi/hopcroft/result_second_class.npy', results)
