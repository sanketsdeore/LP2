import heapq

def add_edge(adj, u, v, w):
    adj[u].append((int(w), v))
    adj[v].append((int(w), u))

def prims(vertices, adj):
    start = vertices[0]
    visited = set([start])
    edges = adj[start][:]
    heapq.heapify(edges)
    mst = []
    while edges and len(visited) < len(vertices):
        weight, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((weight, v))
            for next_weight, next_vertex in adj[v]:
                if next_vertex not in visited:
                    heapq.heappush(edges, (next_weight, next_vertex))
    return mst

n = int(input("No. of vertices: "))
vertices = []

print("Enter vertices: ")

for i in range(n):
    v = input()
    vertices.append(v)

adj = {v:[] for v in vertices}

m = int(input("No. of edges: "))
print("Enter (from, to, weight): ")

for i in range(m):
    u, v, w = input().split()
    add_edge(adj, u, v, w)

mst = prims(vertices, adj)
print("Prim's MST:")
for weight, v in mst:
    print(f"Node: {v} Weight: {weight}")
