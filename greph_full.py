class Graph:
    def __init__(self):
        self.graph = {}

    def breadth_first_search(self, v):
        if v not in self.graph:
            raise Exception("vertex not in graph")
        visited_list = []
        waiting_queue = []
        waiting_queue.append(v)
        while len(waiting_queue) > 0:
            vis = waiting_queue[0]
            del waiting_queue[0]
            visited_list.append(vis)
            sorted_list = sorted(self.graph[vis])
            for sn in sorted_list:
                if sn not in visited_list and sn not in waiting_queue:
                    waiting_queue.append(sn)
        return visited_list

    def unconnected_vertices(self):
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected

    def adjacent_nodes(self, node):
        return self.graph[node]

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    
    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


# Properties
# - Graphs can have any number of vertices.
# - An undirected graph can have up to n(n - 1)/2 edges for n vertices.
# - Vertices can exist without edges but may be disconnected (and thus kinda useless)
# - Typically graphs (with the exception of multigraphs) can only have a single edge between two vertices
# - Weighted graphs assign values (costs) to edges (we'll cover this in a future course)