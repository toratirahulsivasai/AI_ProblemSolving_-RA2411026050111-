def add_weighted_edge(graph, node1, node2, cost):
    if node1 not in graph:
        graph[node1] = []

    if node2 not in graph:
        graph[node2] = []

    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))


def clear_graph(graph):
    graph.clear()
