from collections import deque
from re import match
import heapq

file_name = input("Enter the file path (e.g., data.txt): ")

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

def read_graph(filename):
    with open(filename, "r") as file:
        N, M = map(int, file.readline().split())
        edges = []
        for _ in range(M):
            u, v, w = map(int, file.readline().split())
            edges.append((w, u, v))
    return N, edges


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False  
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True


def kruskal(N, edges):
    edges = sorted(edges)  
    parent = list(range(N))
    rank = [0] * N
    mst, total = [], 0

    for w, u, v in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == N - 1:
                break
    return mst, total


def show(N, mst, total):
    print("Kruskal's Algorithm")
    print("MST edges:")
    for u, v, w in mst:
        print(f"  ({u}, {v})  weight {w}")
    print(f"Total weight: {total}")
    if len(mst) < N - 1:
        print("Warning: graph is disconnected, result is a spanning forest.")

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


def k():
    N, edges = read_graph(file_name)
    mst, total = kruskal(N, edges)
    show(N, mst, total)

def DFSBFS():
    start = input("Enter the starting node for DFS and BFS: ").strip()
    visited = set()
    print("DFS-BFS Algorithm")
    print("DFS:")
    dfs(graph, start, visited)
    print("\n")
    print("BFS:")
    bfs(graph, start)

def d():
    start = int(input("Enter the starting node for Dijkstra's algorithm: "))
    end = int(input("Enter the ending node for Dijkstra's algorithm: "))

    path, total = dijkstra(graph, start, end)

    if path is None:
        print("No path found")
    else:
        print(" -> ".join(f"{node}({weight})" for node, weight in path))
        print("Total weight:", total)

with open(file_name, "r") as file:
    N, M = map(int, file.readline().split())

    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, file.readline().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

match input("Enter fs (for DFS-BFS), d (for Dijkstra's algorithm), or k (for Kruskal's algorithm): ").strip().lower():
    case "fs":
        DFSBFS()
    case "k":
        k()
    case "d":
        d()
    case _:
        print("Invalid input. Please enter 'fs' or 'k'.")