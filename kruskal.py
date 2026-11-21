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


if __name__ == "__main__":
    N, edges = read_graph("data.txt")
    mst, total = kruskal(N, edges)
    show(N, mst, total)