import heapq


def uniform_cost_search(graph, start, goal):
    if start not in graph or goal not in graph:
        return None, None, []

    priority_queue = [(0, start, [start])]
    best_cost = {start: 0}
    explored = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in explored:
            continue

        explored.append(node)

        if node == goal:
            return path, cost, explored

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost

            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path + [neighbor])
                )

    return None, None, explored
