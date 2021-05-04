if __name__ == "__main__":
    #ns = [10, 20, 50, 100, 250, 500, 1000, 2000, 2500, 5000, 10000, 25000, 50000, 100000]
    ns = [1000, 2000, 2500, 5000, 10000, 25000, 50000, 100000]
    ps = [0.01, 0.05, 0.1, 0.2]
    tests = 1000

    import sys
    sys.setrecursionlimit(200000)

    import networkx as nx
    from bisimulation_algorithms import dovier_piazza_policriti
    import numpy as np

    for n in ns:
        results = np.zeros((len(ps), tests))
        for p_idx, p in enumerate(ps):
            for test in range(tests):
                graph = nx.fast_gnp_random_graph(n, p, directed=True)
                results[p_idx, test] = len(dovier_piazza_policriti(graph, is_integer_graph=True))
        print('done {}'.format(n))
        np.save('altro/dim/result{}.npy'.format(n), results)
