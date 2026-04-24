def add_edge(graph, node1, node2):
    graph.setdefault(node1, []).append(node2)
    graph.setdefault(node2, []).append(node1)
    return graph
