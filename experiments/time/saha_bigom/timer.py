from itertools import product
from math import pow, floor, ceil
import random
from networkx.algorithms.operators.unary import complement
import numpy as np
import networkx as nx

random.seed()

# 0: PTA
# 1: FBA
# 2: n of edges

ns = [10,50,100,250,500,750,1000,1250,1500,1750,2000]
new_edges_count = 3
ntests = 100

for n_idx, n in enumerate(ns):
    print('doing n={}'.format(n))

    result = np.zeros((ntests, 1+new_edges_count+1))
    for test in range(ntests):
        print('test n: {}'.format(test))

        graph = nx.fast_gnp_random_graph(n, 0.001, directed=True)
        edges = random.choices(list(complement(graph).edges), k=new_edges_count)

        print('\t\tgraph: {},{}'.format(len(graph.nodes), len(graph.edges)))
        print('\t\tnew edges: {}'.format(edges))

        setup_saha = """\
import networkx as nx
from bispy import dovier_piazza_policriti
from bispy.saha.saha import update_rscp
from bispy.paige_tarjan.pta import pta
from bispy.utilities.graph_decorator import decorate_nx_graph
from itertools import cycle

graph = nx.DiGraph()
graph.add_nodes_from({})
graph.add_edges_from({})
initial_partition = [tuple(range(len(graph.nodes)))]

new_edges = {}

qblocks_arr = []
vertexes_arr = []

ntests = {}

for i in range(ntests):
    vertexes, qblocks = decorate_nx_graph(graph, initial_partition)
    qblocks = pta(qblocks)

    qblocks_arr.append(qblocks)
    vertexes_arr.append(vertexes)

iterator = cycle(range(ntests))

import sys
sys.setrecursionlimit(80000)""".format(graph.nodes, graph.edges, edges, 10)

        setup_fba = """\
import networkx as nx
from bispy import dovier_piazza_policriti

graph = nx.DiGraph()
graph.add_nodes_from({})
graph.add_edges_from({})

graph.add_edges_from({})""".format(graph.nodes, graph.edges, edges)
        import timeit

        print('\t\tedges: {}'.format(edges))

        fba = timeit.timeit('dovier_piazza_policriti(graph, is_integer_graph=True)', setup=setup_fba, number=10) / 10

        saha = []
        for i in range(len(edges)):
            saha.append(timeit.timeit(
                'idx = next(iterator); qblocks = update_rscp(qblocks_arr[idx], vertexes_arr[idx], new_edges[{}])'.format(i),
                setup=setup_saha,
                number=10)
                / 10)

        print('\t\t{} --- {}'.format(round(fba, 5), [round(i, 5) for i in saha]))
        result[test] = np.array([fba, *saha, sum(saha)])

    np.save('/scratch/fandreuz/altro/bisi/src_saha_random/result{}.npy'.format(n), result)
