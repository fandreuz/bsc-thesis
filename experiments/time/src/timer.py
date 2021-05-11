from itertools import product
from math import pow, floor, ceil

if __name__ == "__main__":
    depths = range(11,12)
    bf = range(1,4)

    ntests = lambda tp: 10 if tp[0] >= 8 and tp[1] == 3 else 100

    import numpy as np
    import networkx as nx

    # 0: PTA
    # 1: FBA
    # 2: n of edges

    ratio = 2

    for d_idx, d in enumerate(depths):
        results = np.zeros((len(bf), 4+4+2))

        print('doing d={}'.format(d))
        for b_idx, b in enumerate(bf):
            print('\tbf={}'.format(b))
            graph = nx.balanced_tree(b, d, create_using=nx.DiGraph)

            print('\t\tgraph: {},{}'.format(len(graph.nodes), len(graph.edges)))

            tests = ntests((d, b))
            print('\t\tdoing {} tests'.format(tests))

            anode_in_last_row = len(graph.nodes) - 1
            parent = lambda x: ceil(x / b) - 1 if ceil(x / b) > 1 else 0
            pparent = lambda x: parent(parent(x))
            ppparent = lambda x: pparent(parent(x))
            pppparent = lambda x: pparent(pparent(x))
            pppppparent = lambda x: ppparent(ppparent(x))

            new_edges = [(0, len(graph.nodes) - 1),
                (anode_in_last_row, parent(anode_in_last_row)),
                (anode_in_last_row, ppparent(anode_in_last_row)),
                (anode_in_last_row, pppppparent(anode_in_last_row))]

            setup_saha = """\
import networkx as nx
from bisimulation_algorithms import dovier_piazza_policriti
from bisimulation_algorithms.saha.saha import update_rscp
from bisimulation_algorithms.paige_tarjan.pta import pta
from bisimulation_algorithms.paige_tarjan.graph_decorator import initialize
from bisimulation_algorithms.saha.graph_decorator import prepare_internal_graph

b,d = {}, {}
graph = nx.balanced_tree(b,d, create_using=nx.DiGraph)
initial_partition = [tuple(range(len(graph.nodes)))]

new_edges = {}

def old_vertexes_and_qblocks():
    copies = []
    for i in range({}):
        qblocks, vertexes = initialize(graph, initial_partition)
        qblocks = pta(qblocks)
        prepare_internal_graph(vertexes, initial_partition)
        copies.append((qblocks, vertexes))
    return copies

saha_copies = old_vertexes_and_qblocks()
copies_idx=0

import sys
sys.setrecursionlimit(20000)""".format(b, d, new_edges, tests)

            setup_fba = """\
import networkx as nx
from bisimulation_algorithms import dovier_piazza_policriti

new_edges = {}

def generate_fba_graphs(index):
    new_graph = nx.balanced_tree({},{}, create_using=nx.DiGraph)
    new_graph.add_edge(*new_edges[index])
    return new_graph

graphs = [generate_fba_graphs(i) for i in range(len(new_edges))]""".format(new_edges, b, d)
            import timeit

            print('\t\tedges: {}'.format(new_edges))

            fba = []
            for i in range(len(new_edges)):
                fba.append(timeit.timeit('dovier_piazza_policriti(graphs[{}], is_integer_graph=True)'.format(i), setup=setup_fba, number=tests) / tests)

            saha = []
            for i in range(len(new_edges)):
                saha.append(timeit.timeit('qblocks, vertexes=saha_copies[copies_idx]; update_rscp(qblocks, new_edges[{}], vertexes); copies_idx+=1'.format(i), setup=setup_saha, number=tests) / tests)

            results[b_idx] = np.array([*fba, *saha, len(graph.nodes), len(graph.edges)])

            print('\t\t{} --- {}'.format([round(i,5) for i in fba], [round(i,5) for i in saha]))
        np.save('/scratch/fandreuz/bisi/tree_saha/result{}.npy'.format(d), results)
