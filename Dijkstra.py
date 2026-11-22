import heapq

def dijkstra(graph, start, end):
    distances = [float('inf')] * len(graph)
    previous = [None] * len(graph)
    edge_weights = [0] * len(graph)

    distances[start] = 0
    pq = [(0, start)]

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > distances[node]:
            continue

        if node == end:
            break

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                edge_weights[neighbor] = weight

                heapq.heappush(pq, (new_distance, neighbor))

    if distances[end] == float('inf'):
        return None, None

    path = []
    current = end

    while current is not None:
        path.append((current, edge_weights[current]))
        current = previous[current]

    path.reverse()

    return path, distances[end]

with open("data.txt", "r") as file:
    N, M = map(int, file.readline().split())

    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, file.readline().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

start = 0
end = 4

path, total = dijkstra(graph, start, end)

if path is None:
    print("No path found")
else:
    print(" -> ".join(f"{node}({weight})" for node, weight in path))
    print("Total weight:", total)