def astar_algo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node : 0}
    parents = {start_node : start_node}
    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
                
        if n is None:
            print("No path found!")
            return None
            
        if n == stop_node:
            path = [n]
            while parents[n] != n:
                n = parents[n]
                path.insert(0, n)
            print("Path: ", path)
            return path
            
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                        
        open_set.remove(n)
        closed_set.add(n)
    print("No path found!")
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return H_dist.get(n, 0)

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)]
}

astar_algo('A', 'G')
