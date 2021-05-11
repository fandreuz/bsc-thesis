from bisimulation_algorithms.saha.saha import update_rscp
import networkx as nx
from bisimulation_algorithms import dovier_piazza_policriti
from bisimulation_algorithms.saha.saha import update_rscp
from bisimulation_algorithms.paige_tarjan.pta import pta
from bisimulation_algorithms.paige_tarjan.graph_decorator import initialize
from bisimulation_algorithms.saha.graph_decorator import prepare_internal_graph

graph = nx.balanced_tree(4,5, create_using=nx.DiGraph)
new_edge1 = (len(graph.nodes)-1, 0)

qblocks, vertexes = initialize(graph, [(i,) for i in graph.nodes])
qblocks = pta(qblocks)
prepare_internal_graph(vertexes, [(i,) for i in graph.nodes])

update_rscp(qblocks, new_edge1, vertexes)
