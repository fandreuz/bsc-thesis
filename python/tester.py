import networkx as nx
import matplotlib.pyplot as plt
import rank
import randomcolor

MATERIAL_COLORS = ['#26A69A', '#9FA8DA', '#80DEEA', '#FDD835', '#FF8A65', '#A1887F']

def test_wf(graph):
    rank.well_founded_nodes(graph)

    colors = list(map(lambda wf: '#8a8e94' if wf else 'red', nx.get_node_attributes(graph, 'wf').values()))

    plt.subplot(111)

    pos=nx.spring_layout(graph, k=2)
    nx.draw(graph, pos, node_color=colors, with_labels=True, font_weight='bold', connectionstyle='arc3, rad = 0.1')

    plt.savefig("graph_wf.png", dpi=300)

    for node in graph.nodes:
        print('{} is {}'.format(node, 'wf' if graph.nodes[node]['wf'] else 'nwf'))

def test_rank(graph):
    rank.compute_rank(graph)

    graph_scc = rank.prepare_scc(graph)
    scc_map = rank.build_map_to_scc(graph_scc, graph)

    if len(MATERIAL_COLORS) < len(graph_scc.nodes):
        random_color = randomcolor.RandomColor()
        for i in range(len(graph_scc.nodes) - len(MATERIAL_COLORS)):
            MATERIAL_COLORS.append(random_color.generate()[0])

    scc_color_map = {scc: MATERIAL_COLORS[index] for index,scc in enumerate(graph_scc.nodes)}

    labels = {node: '{}({})'.format(node, graph.nodes[node]['rank']) for node in graph.nodes}
    colors = [scc_color_map[scc_map[node]] for node in graph.nodes]

    plt.subplot(111)
    pos=nx.spring_layout(graph, k=4)
    nx.draw(graph, pos, labels=labels, node_size=700, node_color=colors, with_labels=True, font_weight='bold', connectionstyle='arc3, rad = 0.1')

    #plt.subplot(122)
    #pos=nx.spring_layout(graph_scc, k=2)
    #nx.draw(graph_scc, pos, labels={node:'{}'.format(','.join(map(str,node))) for node in graph_scc.nodes}, with_labels=True, font_weight='bold', connectionstyle='arc3, rad = 0.1')

    plt.savefig("graph_rank.png", dpi=300)

graph = nx.erdos_renyi_graph(10, 0.15, directed=True)
test_rank(graph)
