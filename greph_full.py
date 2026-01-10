class Graph:
    def __init__(self):
        self.graph = {}

    def unconnected_vertices(self):
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected

    def adjacent_nodes(self, node):
        return self.graph[node]

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u} 

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False


# Properties
# - Graphs can have any number of vertices.
# - An undirected graph can have up to n(n - 1)/2 edges for n vertices.
# - Vertices can exist without edges but may be disconnected (and thus kinda useless)
# - Typically graphs (with the exception of multigraphs) can only have a single edge between two vertices
# - Weighted graphs assign values (costs) to edges (we'll cover this in a future course)