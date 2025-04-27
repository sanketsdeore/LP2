from collections import defaultdict

graph = defaultdict(list)
n = int(input("Enter number of edges: "))
print("Enter (from, to):")

for i in range(n):
    u, v = input().split()
    graph[u].append(v)

def DFS(graph, node):
    stack = [node]
    visited = set()
    print("DFS: ")
    while stack:
        s = stack.pop()
        if s not in visited:
            visited.add(s)
            print(s, end = " ")
            for neighbour in reversed(graph[s]):
                if neighbour not in visited:
                    stack.append(neighbour)
                    
def BFS(graph, node):
    queue = [node]
    visited = set()
    print("BFS: ")
    while (queue):
        m = queue.pop(0)
        print(m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

start = input("Starting node: ")
BFS(graph, start)
