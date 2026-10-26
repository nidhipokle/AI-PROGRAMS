import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    queue = [(h[start], start, [start], 0)]

    while queue:
        f, node, path, cost = heapq.heappop(queue)

        print("Visiting Node:", node)
        print("Cost:", cost)
        print("Heuristic:", h[node])
        print("F value:", f)
        print("----------------------")

        if node == goal:
            print("\n======================")
            print("      A* RESULT")
            print("======================")
            print("Start Node :", start)
            print("Goal Node  :", goal)
            print("Best Path  :", " -> ".join(path))
            print("Total Cost :", cost)
            print("======================")
            return

        for next_node, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_f = new_cost + h[next_node]

            heapq.heappush(
                queue,
                (new_f, next_node, path + [next_node], new_cost)
            )

astar('A', 'D')