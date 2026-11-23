import heapq
import sys


def read_graph(filename):
    with open(filename, "r") as file:
        N, M = map(int, file.readline().split())
        graph = [[] for _ in range(N)]
        for _ in range(M):
            u, v, w = map(int, file.readline().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
    return N, graph


def prim(graph, N, start):
    visited = [False] * N
    mst_edges = []
    total_weight = 0

    heap = [(0, -1, start)]

    while heap:
        w, frm, to = heapq.heappop(heap)

        if visited[to]:
            continue  

        visited[to] = True
        if frm != -1:  
            mst_edges.append((frm, to, w))
            total_weight += w

        for neighbor, weight in graph[to]:
            if not visited[neighbor]:
                heapq.heappush(heap, (weight, to, neighbor))

    return mst_edges, total_weight, all(visited)


def show_result(mst_edges, total_weight, connected):
    print("Prim's Algorithm")
    print("MST edges:")
    for u, v, w in mst_edges:
        print(f"  ({u}, {v})  weight {w}")
    print(f"Total weight: {total_weight}")
    if not connected:
        print("Warning: graph is disconnected, result covers only the "
              "start vertex's component.")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "data.txt"

    try:
        N, graph = read_graph(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    if len(sys.argv) > 2:
        start = int(sys.argv[2])
    else:
        start = int(input("Enter the starting node for Prim's algorithm: "))

    if not (0 <= start < N):
        print(f"Start vertex must be between 0 and {N - 1}")
        sys.exit(1)

    edges, total, connected = prim(graph, N, start)
    show_result(edges, total, connected)
