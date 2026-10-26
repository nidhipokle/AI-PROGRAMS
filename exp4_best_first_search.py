import heapq

n = int(input("Enter number of nodes: "))

graph = {}

for i in range(n):
    node = input(f"Enter node {i + 1}: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

heuristic = {}

print("\nEnter heuristic values:")
for node in graph:
    heuristic[node] = int(input(f"Heuristic value of {node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

priority_queue = []
heapq.heappush(priority_queue, (heuristic[start], start))

visited = set()
path = []

while priority_queue:
    h, current = heapq.heappop(priority_queue)

    if current in visited:
        continue

    visited.add(current)
    path.append(current)

    print("Visiting:", current)

    if current == goal:
        print("\nGoal node found!")
        break

    for neighbor in graph[current]:
        if neighbor not in visited:
            heapq.heappush(
                priority_queue,
                (heuristic[neighbor], neighbor)
            )

else:
    print("\nGoal node not found!")

print("Best First Search Path:", " -> ".join(path))