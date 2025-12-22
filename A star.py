def a_star(graph, heuristic, start, goal):
    open_list = [(start, 0)]   # (node, cost)
    closed_list = set()
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        # choose node with lowest f(n)
        open_list.sort(key=lambda x: g_cost[x[0]] + heuristic[x[0]])
        current, _ = open_list.pop(0)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                open_list.append((neighbor, new_g))

    return None


# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 2,
    'F': 0
}

path = a_star(graph, heuristic, 'A', 'F')
print("Path found:", path)
