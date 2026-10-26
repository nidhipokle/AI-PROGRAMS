import heapq

def astar(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {start: None}

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g[goal]

        for neighbor, cost in graph[current]:
            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h[neighbor]

                parent[neighbor] = current
                heapq.heappush(open_list, (f, neighbor))

    return None, None


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic values
h = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = astar(graph, start, goal, h)

print("Path:", path)
print("Cost:", cost)