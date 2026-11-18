from collections import deque

def dfs(graph, node, visited, weight=0):
    visited.add(node)

    print(f"{node}({weight})", end=" ")

    for neighbor, w in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, w)

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append((start, 0))

    while queue:
        node, weight = queue.popleft()

        print(f"{node}({weight})", end=" ")

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, w))

with open("data.txt", "r") as file:
    N, M = map(int, file.readline().split())

    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, file.readline().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

visited = set()

dfs(graph, 0, visited)
print("\n")
bfs(graph, 0)