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

    for d in depths:
        results = np.zeros((len(branching_factors), 4))

        print('doing depth={}'.format(d))
        for r_idx, r in enumerate(branching_factors):
            print('\t doing r={}'.format(r))

            import networkx as nx
            graph = nx.balanced_tree(r, d, create_using=nx.DiGraph)

            setup = """\
import networkx as nx
from bisimulation_algorithms import paige_tarjan, dovier_piazza_policriti

graph = nx.balanced_tree({}, {}, create_using=nx.DiGraph)

import sys
sys.setrecursionlimit(20000)""" .format(r, d)

            import timeit
            pta = timeit.timeit('paige_tarjan(graph, is_integer_graph=True)', setup=setup, number=number) / number
            fba = timeit.timeit('dovier_piazza_policriti(graph, is_integer_graph=True)', setup=setup, number=number) / number

            results[r_idx] = np.array([pta, fba, len(graph.nodes), len(graph.edges)])

            print('\t\t{},{}'.format(pta, fba))
        np.save('altro/src/tree_depth{}.npy'.format(d), results)
